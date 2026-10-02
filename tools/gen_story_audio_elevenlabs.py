#!/usr/bin/env python3
"""Create a separate ElevenLabs trial; existing Edge audio stays intact.

python3 tools/gen_story_audio_elevenlabs.py Panda-story-1 [--limit 1] [--dry-run]
Credentials: ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID in repo .env or environment.
Successful pages are reused. Paid requests are never automatically retried.
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
MODEL = "eleven_flash_v2_5"


def credentials():
    values = {}
    env_path = ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*?)\s*$", line)
            if not match:
                continue
            name, value = match.groups()
            if value.startswith(("'", '"')) and value.endswith(value[0]):
                value = value[1:-1]
            else:
                value = value.split(" #", 1)[0].strip()
            values[name] = value
    for name in ("ELEVENLABS_API_KEY", "ELEVENLABS_VOICE_ID"):
        values[name] = os.environ.get(name) or values.get(name)
        if not values[name]:
            raise ValueError(f"Thiếu {name} trong .env hoặc environment")
    return values["ELEVENLABS_API_KEY"], values["ELEVENLABS_VOICE_ID"]


def api_request(path, key, payload=None):
    headers = {"xi-api-key": key}
    data = None
    if payload is not None:
        headers.update({"Content-Type": "application/json", "Accept": "audio/mpeg"})
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    try:
        return urlopen(Request("https://api.elevenlabs.io" + path, headers=headers, data=data), timeout=90)
    except HTTPError as exc:
        message = exc.read().decode("utf-8", errors="replace").replace(key, "[REDACTED]")
        raise RuntimeError(f"ElevenLabs HTTP {exc.code}: {message}") from None
    except (URLError, TimeoutError):
        raise RuntimeError("Lỗi mạng. Không tự retry request có thể đã tính credit; kiểm tra ElevenLabs History trước khi chạy lại.") from None


def save_json(path, data):
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def duration(path):
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        check=True, capture_output=True, text=True,
    )
    seconds = float(result.stdout.strip())
    if seconds <= 0:
        raise ValueError(f"Audio không có duration: {path.name}")
    return seconds


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("story_dir", type=Path)
    parser.add_argument("--limit", type=int, help="Số trang đầu cần tạo (vd 1 để thử bìa)")
    parser.add_argument("--dry-run", action="store_true", help="Đếm text, không gọi API")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 1:
        parser.error("--limit phải lớn hơn 0")
    story = args.story_dir.resolve()
    original = json.loads((story / "narration.json").read_text(encoding="utf-8"))
    slides = original["slides"]
    for slide in slides:
        for field in ("image", "audio"):
            path = Path(slide[field])
            if path.is_absolute() or ".." in path.parts:
                raise ValueError(f"Đường dẫn không hợp lệ: {field}")
        if not (story / slide["image"]).is_file():
            raise ValueError(f"Thiếu ảnh {slide['image']}")
        if not slide["text"].strip():
            raise ValueError("Lời đọc trống")
    selected = slides[:args.limit] if args.limit else slides
    characters = sum(len(slide["text"]) for slide in selected)
    print(f"{original['title']}: {len(selected)} trang, {characters} ký tự, model {MODEL}, speed 0.9", flush=True)
    if args.dry_run:
        return

    key, voice_id = credentials()
    output = story / "elevenlabs"
    output.mkdir(exist_ok=True)
    settings = {"stability": 0.5, "similarity_boost": 0.75, "speed": 0.9}
    trial = dict(original)
    trial.pop("rate", None)
    trial.update({"provider": "elevenlabs", "voice": voice_id, "voice_label": "ElevenLabs · Flash v2.5", "model_id": MODEL, "voice_settings": settings})
    for name in ["content", "image-prompts-plan.md", *(slide["image"] for slide in slides)]:
        target = output / name
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.symlink_to(os.path.relpath(story / name, target.parent))
    save_json(output / "narration.json", trial)
    manifest_path = output / "generation.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"pages": {}}
    for slide in selected:
        payload = {"text": slide["text"], "model_id": MODEL, "language_code": "vi", "voice_settings": settings}
        fingerprint = hashlib.sha256(json.dumps({"voice": voice_id, **payload}, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        destination = output / slide["audio"]
        record = manifest["pages"].get(slide["audio"])
        if destination.exists():
            if not record or record.get("fingerprint") != fingerprint:
                raise ValueError(f"{slide['audio']} đã có với cấu hình khác; dùng thư mục khác để thử giọng mới")
            duration(destination)
            print(f"Bỏ qua {slide['audio']} đã có", flush=True)
            continue
        # A prior interruption may have consumed credits even without a saved MP3.
        if record and record.get("state") == "pending":
            raise ValueError(f"{slide['audio']}: request trước chưa xác định kết quả. Kiểm tra ElevenLabs History trước khi tạo lại.")
        destination.parent.mkdir(parents=True, exist_ok=True)
        record = {"fingerprint": fingerprint, "characters": len(slide["text"]), "state": "pending"}
        manifest["pages"][slide["audio"]] = record
        save_json(manifest_path, manifest)
        try:
            with api_request("/v1/text-to-speech/" + quote(voice_id, safe="") + "?output_format=mp3_44100_128", key, payload) as response:
                audio = response.read()
                record["request_id"] = response.headers.get("request-id")
                record["character_cost"] = response.headers.get("character-cost")
        except RuntimeError as exc:
            # An explicit HTTP rejection did not produce audio; retries stay manual.
            if str(exc).startswith("ElevenLabs HTTP "):
                record["state"] = "rejected"
                save_json(manifest_path, manifest)
            raise
        temporary = destination.with_suffix(".tmp.mp3")
        temporary.write_bytes(audio)
        seconds = duration(temporary)
        temporary.replace(destination)
        record.update({"state": "complete", "seconds": seconds})
        save_json(manifest_path, manifest)
        print(f"✓ {slide['audio']}: {seconds:.1f}s; credit header: {record['character_cost']}", flush=True)
    if len(selected) == len(slides):
        subprocess.run([sys.executable, str(ROOT / "tools/build_story_slideshow.py"), str(output)], check=True)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, RuntimeError, OSError, subprocess.CalledProcessError) as exc:
        sys.exit(str(exc))
