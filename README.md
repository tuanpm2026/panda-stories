# Truyện Panda & Paw Patrol

Bộ 10 truyện tranh tiếng Việt cho bé Panda trước khi vào lớp Một. Mỗi truyện có tranh, lời đọc và trình chiếu.

**Đọc và nghe online:** https://tuanpm2026.github.io/panda-stories/

## Cập nhật website

Chạy `python3 tools/validate_series.py Panda-story-{1..10}/elevenlabs-v4`, sau đó `python3 tools/build_webapp.py --deploy`. GitHub Pages xuất bản từ nhánh `main`, thư mục `/docs`.

Giọng đọc đang dùng: ElevenLabs v4, tốc độ tự nhiên, chọn bằng `series-config.json`. Audio nằm trong `Panda-story-N/elevenlabs-v4/audio/`; bản Flash v2.5 và Hoài My vẫn giữ local trong `elevenlabs/audio/` và `audio/`.

Tạo hoặc chạy tiếp audio bằng `python3 tools/gen_story_audio_elevenlabs.py Panda-story-N` (mặc định v4). Key và Voice ID nằm trong `.env` và không được commit. Kiểm tra bản mới bằng `python3 tools/validate_series.py Panda-story-N/elevenlabs-v4`. Build với `--narration elevenlabs` để dùng Flash v2.5, hoặc `--narration edge` để dùng Hoài My.

Ảnh gốc độ phân giải cao, ảnh tham chiếu gia đình và thư mục `albums/` chỉ lưu trên máy. Thư mục `docs/` chứa bản ảnh chuyển thể WebP và âm thanh dùng để xem công khai.
