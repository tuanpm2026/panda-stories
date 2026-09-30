# Panda-stories — hướng dẫn cho Codex

Đây là series truyện tiếng Việt cho bé Panda trong thế giới Paw Patrol. Panda là bé trai người thật, 5.5 tuổi, cao khoảng 110 cm; không vẽ thành gấu trúc. Đọc `CLAUDE.md` để nắm quy trình, rồi đọc `Characters/CHARACTERS.md` trước khi viết truyện hoặc prompt ảnh.

## Quy trình

- Mỗi truyện ở `Panda-story-N/`: `content` → `image-prompts-plan.md` → ảnh `cover.png`, `pageK.png` → `narration.json` và `audio/` → `index.html`.
- Khi viết prompt ảnh, theo `.claude/skills/panda-story-prompts/SKILL.md`. Khi tạo slideshow và giọng đọc, theo `.claude/skills/panda-story-slideshow/SKILL.md`.
- Dùng `tools/build_story_slideshow.py` và `tools/build_webapp.py` để sinh HTML; sửa template/công cụ nguồn thay vì chỉnh HTML sinh ra bằng tay.
- Thông tin nhân vật còn đánh dấu TODO hoặc CHỜ XÁC NHẬN thì giữ là chưa biết; hỏi người dùng khi chi tiết đó cần thiết cho truyện hoặc ảnh.

## Riêng tư và xuất bản

- Không commit ảnh thật, ảnh tham chiếu trong `Characters/`, `albums/`, hoặc ảnh gốc trong `Panda-story-N/`.
- `docs/` là bản để đưa lên web công khai, có thể chứa hình bé đã chuyển thể và âm thanh. Kiểm tra nội dung với người dùng trước khi đưa lên remote hoặc bật GitHub Pages.
- Repo nguồn `Shopee-robocar-stories` chỉ là mẫu quy trình. Không sửa repo đó, không mang nhân vật hoặc quy tắc xe có mặt của Robocar Poli sang đây.
