# Panda-stories

Series truyện tranh thiếu nhi (tiếng Việt) cho **bé Panda** trong thế giới **Paw Patrol**.
Quy trình chuyển từ series `~/work/Shopee-robocar-stories` (Shopee + Robocar Poli, 15 truyện).

## Nhân vật
- **Panda: bé trai NGƯỜI THẬT, 5.5 tuổi, ~110 cm** — không phải gấu trúc. he/him.
- Danh bạ nhân vật: `Characters/CHARACTERS.md`; ref gia đình và đội hình Paw Patrol gốc đã có local trong `Characters/`.
- Kế hoạch 10 truyện ở `STORY_ROADMAP.md`; Bố và Mẹ có vai trò cụ thể trong 8/10 truyện (truyện 1 đã làm không có gia đình).

## Quy trình mỗi truyện
1. `Panda-story-N/content` — dòng 1 `Bài học: <tên truyện>`, dòng 3 `Chủ đề: ...`, rồi nội dung, cuối là mục "Bài học cho bé".
2. Skill `panda-story-prompts` → `Panda-story-N/image-prompts-plan.md`.
3. User gen ảnh → `cover.png`, `page1.png` … `pageK.png` trong thư mục truyện.
4. Skill `panda-story-slideshow` → `narration.json`, `audio/*.mp3`, `index.html`.
5. `python3 tools/build_webapp.py --deploy` → `docs/` → GitHub Pages (branch main, folder /docs).

## Preferences
- Gen ảnh AI ở **quality low + ảnh ref nhỏ** để tiết kiệm; user rất để ý chi phí token.
- Giọng đọc đã chốt: ElevenLabs `eleven_v4`, tiếng Việt, tốc độ tự nhiên; Voice ID/key ở `.env`. `series-config.json` chọn `elevenlabs-v4` cho thư viện và deploy. Audio nằm riêng ở `Panda-story-N/elevenlabs-v4/`. Giữ Flash v2.5 speed `0.9` trong `elevenlabs/` và Edge TTS `vi-VN-HoaiMyNeural`, rate `-10%` (venv `~/.venvs/edge-tts`) làm bản dự phòng local.
- Lỗi gen ảnh lặp lại → cập nhật `SKILL.md` (HARD RULES), không chỉ vá từng truyện.
- Không ghi "Paw Patrol"/"Nickelodeon" trong prompt ảnh (dễ bị ChatGPT chặn bản quyền).

## Privacy
Ảnh thật của bé, ảnh gốc độ phân giải cao, ref trong `Characters/` → chỉ giữ local (xem `.gitignore`). `Characters/CHARACTERS.md` được lưu trong Git. `docs/` là bản xuất bản công khai, cần kiểm tra trước khi push.
