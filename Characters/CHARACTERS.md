# Danh bạ nhân vật — Panda-stories

Nguồn chuẩn cho skill `panda-story-prompts`. Nhân vật có ở đây → skill dùng luôn, không hỏi lại.
Mỗi nhân vật nên có file ref PNG cùng tên trong thư mục này.

---

## 👦 Gia đình Panda

### Panda — NHÂN VẬT CHÍNH
- **Loại:** bé trai **người thật** — ⚠️ KHÔNG phải gấu trúc
- **Tuổi / chiều cao:** 5.5 tuổi, ~110 cm, tỉ lệ bé mẫu giáo lớn (không chibi/toddler)
- **Pronoun:** he / him / his
- **Ref:** `Panda.png` — character sheet tạo từ ảnh gia đình, lưu local
- **Tóc:** đen, ngắn, để lộ tự nhiên; mũ lưỡi trai trong ảnh gốc không phải phụ kiện cố định
- **Trang phục cố định:** áo phông trắng cổ viền xanh navy, in chữ cong và hình chú chó ở ngực; bên trong là áo dài tay sọc navy-trắng. Quần dài xanh navy, giày thể thao trắng-xanh navy. Khi gen chữ/hình trên áo, ưu tiên bám ảnh ref; chữ AI có thể sai, cần sửa hậu kỳ nếu cần in lớn.
- **Đặc điểm nhận dạng:** gương mặt theo ảnh gia đình và `Panda.png`; mắt đen, nụ cười tươi
- **Tính cách:** [TODO]

### Mẹ
- **Chiều cao:** 165 cm · **Pronoun:** she / her · **Ref:** `mother.png` — character sheet lưu local
- **Ngoại hình / trang phục:** tóc đen buộc thấp, gương mặt và nụ cười theo ảnh gia đình. Áo thun sọc ngang xanh navy-trắng như ảnh; quần dài xanh navy, giày thể thao trắng. Ảnh gốc có nhãn nhỏ trên áo; ảnh ref tạo ra không giữ chi tiết này.

### Bố
- **Chiều cao:** 168 cm · **Pronoun:** he / him · **Ref:** `father.png` — character sheet lưu local
- **Ngoại hình / trang phục:** tóc đen cắt ngắn, vóc dáng chắc, gương mặt và nụ cười theo ảnh gia đình. Áo thun ngắn tay sọc ngang mảnh màu be-trắng như ảnh; quần dài xám than, giày thể thao xám-trắng.

**Phong cách chung của ba người:** 3D hoạt hình điện ảnh rõ nét như bộ ref v2: mắt to biểu cảm, gương mặt và mũi được cách điệu bằng hình khối tròn mềm, da CGI mịn không có lỗ chân lông kiểu ảnh thật, màu bão hòa, ánh sáng viền điện ảnh, nền xanh nhạt trên character sheet. Vẫn giữ nhận diện khuôn mặt gia đình từ ảnh thật. Tránh photorealism, ảnh chân dung chỉnh màu, hoặc dáng catalog thời trang. Dùng `Panda.png`, `mother.png`, `father.png` làm nguồn chuẩn trong mọi truyện. Khi cả nhà đứng cạnh nhau: Bố 168 cm, Mẹ 165 cm, Panda khoảng 110 cm. Bản v1 được giữ local để so sánh nhưng không dùng làm ref chính.

---

## 🐶 Thế giới Paw Patrol — [CHỜ user gửi thông tin]

Mẫu cho mỗi nhân vật (copy khối này):

### [Tên]
- **Loại:** cún [giống chó] / người / ...
- **Giới tính:** · **Pronoun:**
- **Ref:** `[Tên].png`
- **Màu lông / ngoại hình:**
- **Đồng phục:** màu vest, mũ, huy hiệu vòng cổ (collar badge)
- **Pup pack / công cụ:**
- **Xe:** loại xe, màu, biểu tượng — ⚠️ xe KHÔNG có mặt
- **Vai trò / tính cách:**

### Địa điểm cố định
- [TODO: trạm Lookout, thị trấn… — tả kiến trúc cụ thể]

### Mốc tỉ lệ cần chốt
- Cún đứng 4 chân cao tới đâu so với Panda (mặc định tạm: đầu cún ngang hông Panda)
- Xe của cún to cỡ nào (mặc định tạm: cỡ go-kart, nóc thấp hơn vai Panda)

---

## 🎨 Prompt gen character sheet cho Panda (dùng khi có ảnh thật của bé)

Upload 1–2 ảnh chân dung thật của bé làm ref, rồi dùng:

```
Character sheet of a little human boy named Panda (a real 5-and-a-half-year-old human child about 110 cm tall, NOT a panda bear, no animal ears), matching the face in the uploaded photo, [hair], wearing [outfit + printed wordmark], kindergarten-age proportions (not a toddler). Front view, 3/4 view and side view, full body, white background, consistent character design for children's book. 3D Pixar-style children's book illustration, soft cinematic lighting, warm vibrant colors, cute stylized proportions, high detail, friendly atmosphere, professional children's storybook art. --ar 1:1 --style raw --no panda bear, bear ears, panda costume, speech bubbles, watermark
```

Gen ở quality low trước để chốt, ưng rồi mới gen bản đẹp.
