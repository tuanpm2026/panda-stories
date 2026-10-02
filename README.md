# Truyện Panda & Paw Patrol

Bộ 10 truyện tranh tiếng Việt cho bé Panda trước khi vào lớp Một. Mỗi truyện có tranh, lời đọc và trình chiếu.

**Đọc và nghe online:** https://tuanpm2026.github.io/panda-stories/

## Cập nhật website

Chạy `python3 tools/validate_series.py`, sau đó `python3 tools/build_webapp.py --deploy`. GitHub Pages xuất bản từ nhánh `main`, thư mục `/docs`.

Giọng đọc đang dùng: ElevenLabs Flash v2.5, tốc độ 0,9×, chọn bằng `series-config.json`. Audio nằm trong `Panda-story-N/elevenlabs/audio/`; bản Hoài My vẫn giữ local ở `Panda-story-N/audio/`.

Tạo hoặc chạy tiếp audio bằng `python3 tools/gen_story_audio_elevenlabs.py Panda-story-N`. Key và Voice ID nằm trong `.env` và không được commit. Kiểm tra bản mới bằng `python3 tools/validate_series.py Panda-story-N/elevenlabs`. Build với `--narration edge` nếu muốn dùng lại Hoài My.

Ảnh gốc độ phân giải cao, ảnh tham chiếu gia đình và thư mục `albums/` chỉ lưu trên máy. Thư mục `docs/` chứa bản ảnh chuyển thể WebP và âm thanh dùng để xem công khai.
