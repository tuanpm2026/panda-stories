---
name: panda-story-prompts
description: Generate AI image-prompt plan for stories in the Panda-stories series (bé Panda + Paw Patrol universe). Auto-trigger when the user opens, references, edits, or pastes the content of a `content` file inside a `Panda-story-N/` folder (or asks to gen/tạo prompts/ảnh for such a story). Reads the plain-text story content, breaks it into 8-11 scenes, asks the user about any new side characters (gender, age, outfit), then writes `image-prompts-plan.md` next to the content file with: cover + scene prompts + infographic, character refs matrix, A5 portrait (--ar 5:7), Pixar-like 3D style. Output guide is Vietnamese, prompts are English. Skill is project-local for the Panda-stories series only.
---

# Panda Story → Image Prompts Plan

You are generating an AI image-generation plan for a children's storybook in the **Panda-stories** series — nhân vật chính là **bé Panda** (bé trai người thật, 5.5 tuổi) phiêu lưu cùng thế giới **Paw Patrol**. The plan is consumed by the user (Vietnamese parent/creator) to copy-paste prompts into Midjourney/Nano Banana/Flux/Sora/ChatGPT.

> Skill này được chuyển từ series Shopee-robocar-stories (15 truyện đã validate). Các HARD RULES dưới đây là lỗi thật đã gặp ở series đó + lỗi đặc thù dự kiến của Panda/Paw Patrol. Chỗ nào ghi **[CHỜ XÁC NHẬN]** là mặc định tạm — cập nhật khi user gửi thông tin Paw Patrol / ref ảnh.

## ⚠️ LESSONS LEARNED — HARD RULES (đọc TRƯỚC, áp dụng cho MỌI prompt)

**Mọi prompt phải tự động phòng các lỗi này** — đừng để user phải nhắc lại từng lần.

1. **PANDA LÀ EM BÉ NGƯỜI — KHÔNG PHẢI GẤU TRÚC.** Tên "Panda" trong prompt tiếng Anh rất dễ khiến AI vẽ con gấu trúc, hoặc em bé có tai gấu / lông đen-trắng / mặc đồ gấu trúc.
   - Lần đầu nhắc trong mỗi prompt luôn viết: *"a little human boy named Panda (a real human child, NOT a panda bear, no animal ears, no panda costume)"*. Các lần sau: *"the boy Panda"*.
   - Đuôi `--no` của mọi prompt có người luôn có `panda bear, bear ears, panda costume`.
   - Với tool không có `--no`: viết khẳng định *"Panda is a human boy — do NOT draw any panda bear or bear-like features"*.
   - Ngoại lệ: chỉ khi cốt truyện **cố ý** có đồ vật gấu trúc (thú bông, áo in hình…) thì mô tả rõ đó là đồ vật, và bỏ `panda bear` khỏi `--no` của riêng scene đó.

2. **PANDA LÀ BÉ TRAI 5.5 TUỔI, CAO ~1m10.** he/him/his/little boy/son. Không bao giờ girl/she/her/daughter.
   - Tỉ lệ cơ thể **bé mẫu giáo lớn** (đầu to vừa phải, chân tay dài hơn em bé 2–3 tuổi) — **KHÔNG** chibi/toddler. Luôn ghi *"a 5-and-a-half-year-old boy, about 110 cm tall, kindergarten-age proportions (not a toddler)"* ở lần nhắc đầu.
   - Style Bible dùng `cute stylized proportions` (không dùng `cute chibi proportions` như series Shopee — sẽ làm Panda trông như 3 tuổi).

3. **CÚN LÀ CHÓ — KHÔNG CÓ TAY NGƯỜI. XE PAW PATROL KHÔNG CÓ MẶT.** (Ngược với Robocar Poli: ở đó xe có mặt; ở đây **cún** mới là nhân vật, **xe chỉ là phương tiện cún lái**.)
   - Cún (pups) là **chó con hoạt hình**: 4 chân, **bàn chân chó (paws)**, đuôi, mặc áo vest đồng phục + mũ bảo hiểm + ba lô (pup pack) theo đúng ref. **KHÔNG** bàn tay người, ngón tay, găng tay. Được đứng 4 chân, ngồi kiểu chó, đôi khi đứng 2 chân sau ngắn khi vui mừng; giơ **một chân trước** (paw) để chào/chỉ — ghi rõ *"raising one front paw (a dog paw, not a hand)"*.
   - **Bộ phận máy của pup pack được phép:** thang, móc kéo, cần kẹp, vòi nước, cánh bay… (mô tả rõ *"a mechanical tool extending from the pup pack, not a hand"*).
   - **Xe của cún** là phương tiện cứu hộ bình thường, **KHÔNG mắt, KHÔNG miệng, KHÔNG mặt** ở kính/đầu xe. Cún **ngồi ở ghế lái**.
   - Tránh động từ *"pointing / gesturing / grabbing / holding with hands"* cho cún → dùng *"nudging with its nose / raising a paw / carrying in its mouth / using the pup-pack tool"*.
   - **Con người (Panda, Bố, Mẹ, Ryder…) VẪN có tay bình thường** → chỉ chặn `human hands on dogs, humanoid dogs, faces on vehicles` — **TUYỆT ĐỐI không** ghi `--no hands` trống.

4. **CHẶN CHỮ RÁC NHƯNG GIỮ LOGO/KÝ HIỆU MONG MUỐN.** AI hay tự sinh bong bóng thoại + chữ ngẫu nhiên; nhưng nếu chặn chữ quá mạnh thì **mất luôn logo áo / huy hiệu** (lỗi đã gặp ở series Shopee: "gen ra toàn thiếu logo").
   - **GIỮ:** chữ/logo in trên áo Panda **[CHỜ XÁC NHẬN: màu áo + chữ in]**, **huy hiệu trên vòng cổ (collar tag/badge)** của từng cún, logo/biểu tượng trên xe của cún **[CHỜ XÁC NHẬN theo CHARACTERS.md]**.
   - **CHẶN:** speech bubble, dialogue balloon, thought bubble, caption, signboard, **random floating text**.
   - **TUYỆT ĐỐI KHÔNG** dùng `--no text` / `--no words` / `--no letters` → xoá luôn logo. Suffix `--no` chuẩn xem mục "Prompt construction rules" #8.
   - Tool không có `--no` (Nano Banana/Flux/Sora/ChatGPT): viết khẳng định *"no speech bubbles or random floating text, but DO keep the printed wordmark on the boy's shirt and the pups' collar badges"*.
   - Chữ nhỏ AI hay méo → khuyến nghị **overlay logo sạch khi hậu kỳ** cho ảnh in to.

5. **TRANG PHỤC/LOGO ÁO PHẢI ĐƯỢC TẢ RÕ + NHÌN THẤY.** Mỗi prompt có Panda luôn tả đúng trang phục trong `Characters/CHARACTERS.md` (vd *"Panda in his [color] T-shirt with the printed wordmark [X] clearly visible on the chest"*) và **luôn upload đúng ref** `Characters/Panda.png` (+ bố mẹ nếu có).

6. **PHỐI CẢNH XA-GẦN cho scene đông hoặc cảnh rộng.** Scene nhiều nhân vật dễ bị "dàn phẳng, sai tỉ lệ". Bắt buộc mô tả **chiều sâu 3 lớp**: nhân vật chính lớn nhất ở **foreground (đáy khung)**; nhóm hoạt động ở **midground**; vật/nhân vật xa **nhỏ hơn + mờ nhẹ (atmospheric perspective)** ở background. Thêm: đường/vạch kẻ **lùi dần về điểm tụ (vanishing point)**, *eye-level hoặc slightly low camera angle, wide cinematic lens, deep depth of field*. Dùng **upper/lower half** (không dùng left/right) cho khung dọc.

7. **NHÂN VẬT ĐÃ CÓ TRONG CHARACTERS.md → KHÔNG HỎI USER.** Nếu nhân vật được mô tả trong `Characters/CHARACTERS.md` (có hoặc chưa có file PNG), **dùng luôn** mô tả đó. Chỉ hỏi khi nhân vật **hoàn toàn mới**. (Xem Step 3–4.)
   - Nếu mô tả có nhưng **file ref PNG chưa có** → vẫn viết prompt, nhưng trong Bước 1 của plan ghi rõ *"⚠️ Chưa có ref — gen character sheet trước (prompt ở Bước 2)"*.

8. **TIÊU ĐỀ trên cover & infographic → RENDER THẲNG vào ảnh (đừng để trống).** Scene 0 (cover) render đúng **tên truyện**; scene infographic cuối render đúng **tiêu đề bài học**, dạng *"render the title as a large, bold, clean, neatly-spelled storybook title banner reading exactly: «…» with correct Vietnamese diacritics"*.
   - Cover: **bỏ `captions`** khỏi đuôi `--no`. Infographic: **bỏ hẳn `--no`** (trừ `panda bear` nếu có Panda — giữ lại dạng câu khẳng định trong prompt).
   - AI dễ méo chữ Việt nhiều dấu → ghi chú user **gen 2–3 lần** hoặc **overlay tiêu đề sạch khi hậu kỳ** (Canva/Photoshop).

9. **TỈ LỆ NGƯỜI–CÚN–XE PHẢI ĐÚNG.** Lỗi đã gặp ở series Shopee: AI gen xe quá nhỏ/quá to so với em bé. Mốc tỉ lệ cho Panda (~110 cm):
   - **Cún Paw Patrol** **[CHỜ XÁC NHẬN]**: đứng 4 chân, đỉnh đầu cún ngang khoảng **hông/thắt lưng** Panda.
   - **Xe của cún** **[CHỜ XÁC NHẬN]**: kích thước "pup-size" như trong phim (cỡ xe go-kart) — nóc xe thấp hơn vai Panda.
   - **Xe thật của người lớn**: ô tô con cao ~1m45 → đầu Panda chỉ tới ngang **mép dưới cửa kính**; xe buýt / xe tải / tàu hoả = **rất to**, Panda chỉ cao tới **nửa bánh xe đến cửa dưới**.
   - Bố mẹ: Panda cao tới khoảng **ngực/bụng** người lớn.
   - Câu mẫu: *"render correct scale: the boy Panda is about 110 cm tall; [X] is [size relation] — do NOT shrink or enlarge anyone."* Sai tỉ lệ → thêm *"exaggerate the size difference"*.

10. **NHÂN VẬT PHỤ KHÔNG GIỐNG REF → 2 nguyên nhân, phải chặn cả hai.** (Lỗi đã gặp ở series Shopee: scene 4 nhân vật thì nhân vật phụ chỉ giống ~60–70%.)
    - **Nguyên nhân 1 — "mô tả chốt" quá sơ sài.** Đọc kỹ character sheet (đọc ảnh PNG) và tả **ĐẦY ĐỦ chi tiết đặc trưng**: giống chó, màu lông từng mảng, màu áo vest, kiểu mũ, huy hiệu vòng cổ, pup pack có công cụ gì, tai cụp/dựng… Thiếu chi tiết nào → AI tự chế chỗ đó.
    - **Nguyên nhân 2 — loãng multi-ref.** MJ chỉ bám tốt 2–3 `--cref`. Cách chặn: gen từng nhân vật **solo (1 ref) trước để khoá 1 ảnh chuẩn 90–100%**, rồi dùng ảnh đó làm ref cho scene đông; hoặc dùng tool multi-ref mạnh (Nano Banana / Flux Kontext / Sora); hoặc inpaint. → "Khoá nhân vật trước" luôn đứng đầu mục "Thứ tự gen đề xuất".

11. **NGƯỜI/CÚN Ở CỬA SỔ XE → THÂN PHẢI Ở TRONG XE.** Lỗi đã gặp: tả *"head and hand out the window"* → AI vẽ nhoài nửa thân ra ngoài — sai vật lý và **phản tác dụng với truyện dạy an toàn**.
    - Mặc định: *"visible through the window, bodies fully inside the vehicle"*.
    - Nếu truyện cần "định thò ra" (để bị nhắc): chỉ cho **chớm** + câu khoá *"CRITICAL: no character's torso, chest or shoulders may extend outside the window"*.
    - Thêm vào `--no`: `people hanging out of windows, torsos leaning out of windows`.
    - Truyện dạy an toàn: ảnh không được vẽ hành vi nguy hiểm đậm hơn mức "chớm vi phạm để được nhắc".

12. **ĐỊA ĐIỂM CÓ TÊN/ĐẶC TRƯNG → TẢ KIẾN TRÚC CỤ THỂ, ĐỪNG CHỈ NÊU TÊN.** Lỗi đã gặp: prompt chỉ ghi tên ga → AI ra sân ke trống trơn.
    - Tả rõ kiến trúc + đạo cụ đặc trưng (vd trạm Lookout của Paw Patrol: **[CHỜ XÁC NHẬN mô tả]**; trường học: cổng trường, sân cờ…) và đặt địa điểm ở **mid/upper frame**.
    - Scene cần hiện tên địa điểm: viết khẳng định *"a sign reading exactly: «Tên» — DO render this sign"*, bỏ `signboards` khỏi câu cấm và bỏ `captions` khỏi `--no` của riêng scene đó.

13. **SCENE FULL-CAST (>6 nhân vật, vd cả đội cún) → AI BỎ SÓT NHÂN VẬT + LẪN ĐẶC ĐIỂM.** Paw Patrol có nhiều cún cùng dáng → rất dễ bị gộp/nhầm màu. Cách chặn:
    - Thêm **CHECKLIST ĐẾM** cuối prompt: liệt kê đích danh từng nhân vật + 1 đặc điểm khoá (vd *"[tên] (the [breed] pup in the [color] vest with [badge])"*) + *"render ALL of these, do not omit anyone. Count: N pups + M humans."*
    - Sau khi gen: **đếm lại theo checklist**; thiếu ai thì inpaint bổ sung thay vì gen lại cả ảnh.

14. **TÊN THƯƠNG HIỆU/STUDIO TRONG PROMPT → CHATGPT TỪ CHỐI ("similarity to third-party content").** Lỗi đã gặp ở series Shopee với cụm "3D Pixar-style". **Paw Patrol là thương hiệu có bản quyền → rủi ro còn cao hơn.**
    - **KHÔNG viết "Paw Patrol", "Nickelodeon", "Spin Master" trong prompt.** Chỉ dùng tên riêng nhân vật + **mô tả ngoại hình đầy đủ** + **ảnh ref**.
    - Mỗi plan kèm sẵn "câu style thay thế không thương hiệu" trong TIPS: thay `3D Pixar-style children's book illustration` bằng `cute stylized 3D-animated children's storybook illustration in an original art style (not imitating any specific studio or franchise)`; thay `art directed by Pixar` bằng `with the polished warmth of a high-end animated feature film`.
    - Thứ tự khi bị từ chối: (1) retry nguyên prompt 1 lần (guardrail stochastic) → (2) swap câu style → (3) bỏ tên riêng các cún, chỉ để mô tả ngoại hình → (4) bỏ tham số MJ (`--ar`, `--style raw`, `--no`), viết thành câu khẳng định (*"Vertical 5:7 portrait image"*).
    - Giữ "3D Pixar-style" làm mặc định cho Midjourney/Flux; chỉ swap khi bị chặn.

15. **SCENE CHIA TAY / DI CHUYỂN → KHOÁ HƯỚNG TỪNG NHÂN VẬT SO VỚI CAMERA.** Lỗi đã gặp: *"waves goodbye, looking back"* → AI vẽ ngược hướng. Với mọi scene chia tay, rời đi, đón chào, đi bộ:
    - Khoá **hướng di chuyển của cả nhóm so với camera**: *"the family is walking AWAY from X, TOWARD the camera"*.
    - Khoá **mặt từng nhân vật**: ai *"faces clearly visible to the camera"*, ai *"turned around in three-quarter rear view, looking back at X"*.
    - Đối tượng được chào đặt rõ **ở background**.
    - Chốt bằng 1 câu: *"The walking direction is unmistakable: [A] face the camera, [Panda] faces the [X]."*

---

## Series character roster (HARD-CODED — do not ask user about these)

| Character | Giới tính / Loại | Pronoun (EN) | Ref file |
|-----------|------------------|--------------|----------|
| Panda | **bé trai (boy), 5.5 tuổi, ~110 cm** — nhân vật chính, **người thật, KHÔNG phải gấu trúc** | **he / him / his** | `Characters/Panda.png` |
| Mother (Mẹ) | nữ, 165 cm | she / her | `Characters/mother.png` |
| Father (Bố) | nam, 168 cm | he / him | `Characters/father.png` |
| _Đội Paw Patrol_ | **[CHỜ user gửi thông tin]** — thêm vào `Characters/CHARACTERS.md` | he/she theo CHARACTERS.md | `Characters/<tên>.png` |

**🚨 CRITICAL GUARDRAIL:** Panda là **bé trai người thật**. NEVER "girl / daughter / she / her", NEVER a panda bear. Always "little human boy / he / him / his / son". Double-check every prompt before writing.

### Extended cast

**Nguồn chuẩn:** [`Characters/CHARACTERS.md`](../../../Characters/CHARACTERS.md) — tên, loài/giống chó, giới tính, màu sắc, đồng phục, huy hiệu, xe, công cụ pup pack, tính cách.

**Phong cách gia đình đã chốt:** `Characters/Panda.png`, `Characters/mother.png`, `Characters/father.png` (bản v2) là ref chính. Khi gen scene có người, mô tả rõ tạo hình 3D hoạt hình điện ảnh với mắt to biểu cảm, nét mặt cách điệu, da CGI mịn, màu bão hòa, ánh sáng viền; tránh photorealism và cảm giác ảnh chân dung/chụp catalog. Không dùng file `*-v1.png` làm ref.

→ Khi story dùng các nhân vật này: **đọc CHARACTERS.md, lấy mô tả + ref PNG, KHÔNG PAUSE hỏi user.** Viết "mô tả chốt" (Bước 2 của output) cho mỗi nhân vật và lặp lại nguyên trong mọi prompt liên quan.

## Workflow (must follow in order)

### Step 1 — Locate inputs

- Story content file: `Panda-story-N/content` (plain text, no extension)
- Character reference folder: `Characters/` — kèm `Characters/CHARACTERS.md`.
- Output target: `Panda-story-N/image-prompts-plan.md`

If invoked but the path doesn't match this pattern, ask the user to clarify which story folder.

### Step 2 — Read & analyze the story content

Read the `content` file. Parse:
- **Title** (dòng đầu, hoặc sau "Bài học:")
- **Topic / lesson** (dòng "Chủ đề:"; mục "Bài học cho bé" ở cuối)
- **Narrative body** + character dialogues

### Step 3 — Identify characters in this story

For each character, resolve in THIS order:
1. **Trong roster lõi** (bảng trên) → dùng gender/pronoun/ref hard-coded.
2. **Có trong `Characters/CHARACTERS.md`** → dùng mô tả đó. **KHÔNG hỏi user.** Nếu thiếu file PNG → ghi cảnh báo "chưa có ref" + đưa prompt character sheet vào Bước 2.
3. **Hoàn toàn mới** → PAUSE workflow (Step 4).

### Step 4 — Ask about new characters (CHỈ khi thật sự mới)

> "Story này có nhân vật mới chưa có trong CHARACTERS.md: **[tên]**. Cho mình biết: (1) người hay cún/con vật (giống gì), giới tính & độ tuổi, (2) màu sắc/trang phục/đặc điểm nhận dạng, (3) vai trò trong truyện?"

Wait for answers. Then generate a **character sheet prompt** for each new character (Bước 2 of the plan), và đề nghị thêm nhân vật đó vào `Characters/CHARACTERS.md`.

### Step 5 — Break the story into scenes

Aim for **8–11 narrative scenes** + 1 cover (Scene 0) + 1 infographic ending. Decide autonomously ("skill tự quyết, user xem rồi sửa").

Common beats: setup → inciting moment → emotional reaction → flashback/lời dặn → calming/decision → first attempt → help arrives (Paw Patrol mission — thường là scene đông, áp dụng HARD RULE #6 + #13) → reunion/payoff → celebration/praise → final lesson (infographic).

### Step 6 — Map characters to scenes

| Scene | Panda | Mother | Father | [pups] | [others] |
|-------|:-----:|:------:|:------:|:------:|:--------:|

Goes near the top of the output. Dùng `(bg)` cho nhân vật chỉ xuất hiện mờ ở background.

### Step 7 — Write the output file

Use the **EXACT template** below. Write to `Panda-story-N/image-prompts-plan.md`.
- Story có **cún / xe** → MỞ ĐẦU file bằng khối **"⚠️ 3 QUY TẮC BẮT BUỘC"**.
- Đưa "mô tả chốt" từng nhân vật vào **Bước 2**.

### Step 8 — Confirm with user

Summarize: scene count, characters used, nhân vật nào **chưa có ref**, file path. Mention they can request edits.

---

## Output template (write EXACTLY this structure)

```markdown
# Plan tạo ảnh AI cho Story N: "[Tên truyện]"

## Tổng quan
- **Chủ đề:** [topic / lesson]
- **Số scene đề xuất:** [total] ảnh (1 cover + [N] scene nội dung + 1 infographic bài học)
- **Khổ in:** Sách A5 (148 × 210 mm) — **portrait/dọc**, aspect ratio `5:7` hoặc `2:3` nếu tool không hỗ trợ 5:7
- **Character refs cần upload:** [list] (đánh dấu ⚠️ nhân vật chưa có ref)

---

## ⚠️ 3 QUY TẮC BẮT BUỘC CHO MỌI PROMPT

1. **Panda là em bé NGƯỜI (bé trai 5.5 tuổi), không phải gấu trúc** — luôn có `panda bear, bear ears, panda costume` trong `--no`.
2. **Cún là chó (4 chân, bàn chân chó) — không tay người; xe của cún KHÔNG có mặt.** Công cụ pup pack được phép. Con người vẫn có tay.
3. **Chặn bong bóng thoại/chữ rác NHƯNG giữ logo áo Panda + huy hiệu vòng cổ + ký hiệu xe.** Không dùng `--no text/words/letters`.

---

## QUY TRÌNH THỰC HIỆN (Step-by-step)

### Bước 1: Chuẩn bị reference characters
- [Characters/<file>.png](../Characters/<file>.png) → <Tên> (+ ghi chú trang phục / huy hiệu)
- ⚠️ <Tên> — chưa có ref, gen character sheet ở Bước 2 trước

### Bước 2: Tạo / mô tả chốt nhân vật
- Nhân vật **đã có ref**: viết **"mô tả chốt"** (tiếng Anh) — với cún: giống chó, màu lông, vest, mũ, huy hiệu, pup pack, "dog paws, no human hands"; với xe: "no face on the vehicle".
- Nhân vật **chưa có ref**: gen character sheet trước:
\`\`\`
Character sheet of <description>, front view, 3/4 view and side view, white background, consistent character design for children's book. 3D Pixar-style children's book illustration, soft cinematic lighting, warm vibrant colors, cute stylized proportions, high detail, friendly atmosphere, professional children's storybook art. --ar 1:1 --style raw
\`\`\`

### Bước 3: Gen từng scene theo thứ tự
Với mỗi scene: **upload đúng refs → copy nguyên prompt → paste → gen**.

#### 📋 Bảng tra cứu nhanh: Scene nào cần ref nào
| Scene | Panda | Mother | Father | ... |
|-------|:-----:|:------:|:------:|:---:|
| 0 — Cover | ... |

> **Lưu ý:** Midjourney chỉ bám tốt ~2–3 `--cref`; scene đông nên gen 2–3 lần hoặc dùng Nano Banana / Flux Kontext / Sora. Ưu tiên giữ chuẩn Panda + 1–2 nhân vật gần nhất.

---

## CÁC PROMPT CHI TIẾT (Copy & Paste 1 lần là xong)

### 🎬 SCENE 0 — COVER (Bìa truyện)
**Mục đích:** Ảnh bìa, giới thiệu chủ đề.
**👥 Refs cần upload:** <list>
\`\`\`
<English prompt>
\`\`\`

### 🎬 SCENE 1 — [Tên scene tiếng Việt]
**Bối cảnh:** [1-2 câu tiếng Việt]
**👥 Refs cần upload:** <list>
\`\`\`
<English prompt>
\`\`\`

[... repeat ...]

### 🎬 SCENE [N] — Bài học kết (Infographic)
**Mục đích:** Trang tổng kết bài học cho bé.
**👥 Refs cần upload:** Panda (+ ai khác nếu hợp lý)
\`\`\`
<English infographic prompt>
\`\`\`

---

## TIPS QUAN TRỌNG

### 🐼 Nếu AI vẽ ra gấu trúc / tai gấu
- Nhấn mạnh: `the boy Panda is a completely normal human child with human ears and human skin; there is no panda bear anywhere in this image`.
- Thêm vào `--no`: `panda, bear, animal ears, black-and-white fur`.

### 🐶 Nếu cún mọc tay người / xe mọc mặt
- Cún: thêm `the pup has only four dog legs with round dog paws; absolutely no human hands, fingers or gloves` + `--no human hands, fingers, gloves, humanoid dog`.
- Xe: thêm `the vehicle is an ordinary vehicle with no eyes, no mouth and no face` + `--no face on vehicle, eyes on vehicle`.
- Công cụ pup pack → giữ, đừng chặn. Người vẫn có tay → không dùng `--no hands` trống.

### 🚫 Nếu hiện chữ rác / bong bóng
Tăng `--no speech bubble, caption, signboard, typography`. ⚠️ **Đừng** thêm `--no text/words/letters` (mất logo áo + huy hiệu).

### ⛔ Nếu ChatGPT từ chối (bản quyền)
Swap style: `cute stylized 3D-animated children's storybook illustration in an original art style (not imitating any specific studio or franchise)`; bỏ tên riêng các cún nếu vẫn bị chặn (xem HARD RULE #14).

### Phối cảnh xa-gần (scene đông / cảnh rộng)
*"Strong three-layer depth with correct near-far perspective: [main char] largest in the immediate foreground at the bottom; [group] in the midground; [distant things] farther back, smaller and softly hazy with atmospheric perspective. Lines recede toward a vanishing point. Eye-level, slightly low camera angle, wide cinematic lens, deep depth of field."*

### Nếu nhân vật bị lệch style
`consistent character design matching the reference image, same face shape, same outfit, same proportions`

### Nếu ảnh quá "AI-generated"
`hand-painted storybook quality, subtle texture, not overly glossy, with the polished warmth of a high-end animated feature film`

### Tỷ lệ in A5 (148 × 210 mm)
- `--ar 5:7` (chuẩn nhất) · thay thế `--ar 2:3`
- Export DPI ≥ 300, tối thiểu **1748 × 2480 px**.

### Thứ tự gen đề xuất
1. **Khoá nhân vật trước:** gen solo từng nhân vật (1 ref) → chọn ảnh chuẩn 90–100% làm ref cho scene đông.
2. Gen **Scene 0 (cover)** → chốt style tổng.
3. Gen **scene đông nhân vật nhất** (nhiệm vụ Paw Patrol).
4. Gen lần lượt **Scene 1 → N-1**.
5. Gen **Scene N (infographic)** cuối cùng.

---

## CHECKLIST HOÀN THÀNH
- [ ] Character sheet nhân vật chưa có ref (nếu có)
- [ ] Scene 0 — Cover
- [ ] Scene 1 — [tên]
- ...
```

---

## Prompt construction rules (CRITICAL — apply to every scene prompt)

Each scene prompt is **one long English paragraph** containing these elements in order:

1. **Opening narrative**: action, who does what, emotion, posture, gaze.
   - First mention: `"a little human boy named Panda (a real 5-and-a-half-year-old human child about 110 cm tall, NOT a panda bear)"`, then `"the boy Panda"` / `"he"`.
   - Other characters: correct gender per roster / CHARACTERS.md. Cún: `"the [breed] pup named X in its [color] vest"`.

2. **Setting**: nơi diễn ra + lighting mood (warm overhead light, soft golden hour, desaturated cool tones for anxiety…).

3. **Composition note (portrait)**: "Vertical portrait composition…", "low camera angle", "medium close-up", "split upper/lower half" (NOT left/right). Scene đông/rộng → khối phối cảnh 3 lớp (HARD RULE #6).

4. **Pup & vehicle instruction** (BẮT BUỘC nếu có cún/xe):
   > `IMPORTANT: every pup is a cartoon puppy with four dog legs and round dog paws — NO human hands, NO fingers, NO gloves; tools extending from the pup packs are mechanical parts, not hands. Every vehicle is an ordinary rescue vehicle with NO face, NO eyes and NO mouth; pups sit in the driver's seat. Pups emote through their faces, ears, tails and body posture.`

5. **Text-handling instruction** (BẮT BUỘC):
   > `No speech bubbles, no dialogue balloons, no signboards and no random floating text or captions anywhere in the image — but DO keep the printed wordmark on the boy's shirt, the pups' collar badges and the vehicles' emblems (they are part of the character design, not unwanted text).`

6. **Character match instruction** (mandatory):
   > `[Names] must exactly match the uploaded reference images — same face, same outfit — Panda in his [outfit from CHARACTERS.md] clearly visible — same proportions[, same pup uniforms and badges].`

7. **Style Bible** (verbatim, every prompt):
   > `3D Pixar-style children's book illustration, soft cinematic lighting, warm vibrant colors, cute stylized proportions, high detail, friendly atmosphere, professional children's storybook art, A5 portrait page layout with safe margins for print, leave safe margins, no important details near edges.`

8. **Suffix** (verbatim):
   - Có Panda + cún/xe: `--ar 5:7 --style raw --no speech bubbles, dialogue balloons, thought bubbles, captions, panda bear, bear ears, panda costume, human hands on dogs, humanoid dogs, faces on vehicles, watermark, signature`
   - Chỉ có người: `--ar 5:7 --style raw --no speech bubbles, dialogue balloons, thought bubbles, captions, panda bear, bear ears, panda costume, watermark, signature`
   - **Cover (Scene 0):** như trên nhưng **bỏ `captions`**.
   - **Infographic:** chỉ `--ar 5:7 --style raw` (KHÔNG `--no`) — nhưng trong prompt vẫn phải có câu *"Panda is a human boy, not a panda bear"*.

**Pronoun guardrails** (re-check before writing each prompt):
- Panda → `he / him / his / boy / son`. **Never** `she / her / girl / daughter`, **never** a bear.
- Mother → `she / her`. Father → `he / him`.
- Cún → he/she theo CHARACTERS.md.

**Special elements when appropriate:**
- Flashback → thought bubble with cloud-like edges, upper half of portrait
- Emotional anxiety → "slightly desaturated cooler tones, still child-friendly and not scary"
- Calm/decision → "subtle glowing aura of calm"
- Reunion joy → "sparkles and small heart particles floating in the air"
- Movement → "subtle motion blur lines"
- Sound / siren → "little sound-burst marks" (đừng dùng chữ "BEEP"/"WOOF")
- Infographic → "soft rounded pastel-colored bubbles", "clean white background with subtle dotted pattern", numbered tips, **render tiêu đề** ở banner trên cùng: *"a title banner at the top rendering exactly: «Bài học: …» in large bold clean lettering with correct Vietnamese diacritics"* (HARD RULE #8)
- Cover → RENDER tên truyện ở banner trên cùng (HARD RULE #8)

---

## Canonical reference
- **Cấu trúc & tone (series gốc đã validate):** `~/work/Shopee-robocar-stories/Shopee-story-1/image-prompts-plan.md`; mẫu scene đông + mô tả chốt: `~/work/Shopee-robocar-stories/Shopee-story-10/image-prompts-plan.md`. Chỉ lấy **cấu trúc**, KHÔNG lấy nhân vật/luật xe-có-mặt của Robocar Poli.
- Khi series Panda đã có truyện user validate → thay canonical bằng `Panda-story-1/image-prompts-plan.md`.
- **Danh bạ nhân vật:** `Characters/CHARACTERS.md`.

## When the user says "edit scene X" or "thêm/bớt scene"
Edit the existing `image-prompts-plan.md` directly — don't regenerate the whole file. Preserve all other scenes.
