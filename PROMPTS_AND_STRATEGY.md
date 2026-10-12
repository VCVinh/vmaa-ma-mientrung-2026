# Cẩm Nang Prompt Engineering, Mỹ Thuật & Chiến Lược AI Motion Graphics

Tài liệu này đúc kết toàn bộ phương pháp luận sáng tạo, prompt manifests, thông số kỹ thuật tạo hình và chuyển động AI áp dụng cho **Diễn đàn M&A Miền Trung 2026**.

---

## 1. Triết Lý Mỹ Thuật & Chỉ Đạo Nghệ Thuật (Creative Direction)

### 1.1. Khắc phục triệt để "Căn bệnh Hội nghị Cũ" (Anti-Patterns to Reject)
- **CẤM:** Nền đen phẳng lì, tăm tối, thiếu tương phản.
- **CẤM:** Quả cầu phát sáng vô hồn, các mảnh ghép puzzle ghép hình lỗi thời, ảnh chụp skyline thành phố chung chung từ kho ảnh stock.
- **CẤM:** Font chữ mỏng manh, yếu ớt, lỗi dấu tiếng Việt hoặc chữ do AI vẽ méo mó.
- **CẤM:** Hiệu ứng nổ hạt bụi lộn xộn, rối mắt, làm mất tập trung vào thông tin chính.

### 1.2. Chuẩn mực Đẳng cấp Toàn Cầu ("Đập Vào Mắt · Luminous Luxury")
- **Tính điêu khắc khúc chiết (Sculptural Precision):** Khối kiến trúc pha lê, kính mạ màu dichroic, phản xạ ánh sáng chân thực như thiết kế của Zaha Hadid hay OMA.
- **Dải màu "Loan Loan" Tím - Cobalt:** Phối hợp chuyển màu mượt mà giữa Deep Obsidian Navy (`#070D20`), Royal Amethyst (`#6B2D9B`), Electric Violet (`#9B4DFF`), Electric Cobalt (`#245BFF`), Soft Lavender (`#E9D5FF`), và Ice Cyan (`#63B4FF`).
- **Phân lớp ánh sáng (Multi-layer Lighting):** Lõi ánh sáng trung tâm bừng sáng (Volumetric Core Light Beam) $\to$ Vệt sáng viền cạnh phản quang (Specular Edge Glow) $\to$ Mạng lưới đường dẫn dữ liệu sợi quang tinh xảo (Fiber-optic Data Streams).

---

## 2. Thư Viện Prompt AI (Midjourney & ComfyUI Prompt Manifest)

### Prompt 01: Hero Architecture Convergence Plate (Dùng cho Key Visual & Khối Điêu Khắc)
```text
Award-winning keynote stage visual for premier international economic summit, monumental architectural convergence sculpture rising upward, translucent monolithic fluted glass prisms and titanium cantilevered pavilions representing real estate assets, infused with glowing fiber-optic data channels and luminous laser meridians representing financial technology and AI, deep obsidian navy atmosphere (#070D20), vibrant volumetric purple and royal amethyst aurora wash (#6B2D9B to #9B4DFF), intense electric cobalt light beams (#245BFF) exploding with specular highlights, soft lavender caustics and ice-cyan edges, cinematic volumetric god rays, hyper-clean architectural surfaces, luxury Singapore WEF Milken Institute scale, ultra-photorealistic, Octane Render 8k, architectural digest, raytracing caustics, no text, no artifacts --ar 16:9 --style raw --v 6.1
```

### Prompt 02: Fluted Prism Refraction & Violet Caustics (Dùng cho Sân Khấu & Bìa Tài Liệu)
```text
Macro architectural close-up of fluted ribbed glass columns refracturing electric violet and royal purple light, sharp precision caustics casting delicate lavender and cobalt patterns, glowing data particles suspended inside frosted crystal volumes, high contrast specular reflections, deep navy background, luxurious financial prestige, award-winning motion design key visual, 8k resolution, photorealistic glass shader --ar 16:9 --style raw --v 6.1
```

### Prompt 03: Ascending Cantilevers & Coastal Meridian (Dùng cho Miền Trung / Đà Nẵng)
```text
Futuristic coastal architectural superstructure overlooking a luminous horizon, sweeping cantilevered terraces symbolizing Da Nang economic gateway, dynamic flowing ribbons of purple-blue light weaving through modular glass architecture, sunrise cobalt and amethyst volumetric haze, architectural model craft, high-end real estate and technological M&A summit identity, wide cinematic shot, masterwork --ar 16:9 --style raw --v 6.1
```

### Prompt 04: High-Key Platinum & Lavender Stage (Dùng cho Poster Định Dạng Next Forum)
```text
Bright high-key luxury conference background, pearlescent ivory and soft champagne canvas, sweeping ribbons of luminous electric blue and lavender-violet light curving dynamically through space, abstract kinetic crystal helm floating at bottom corner, clean minimalist spatial composition, ample negative space for keynote speaker typography, high-end Milken Institute World Economic Forum aesthetic, soft studio lighting, pristine clean render --ar 16:9 --style raw --v 6.1
```

---

## 3. Video & Motion Prompt Manifest (Wan 2.2 & LTX-2.5)

### Scene 1: Lõi Năng Lượng Thức Giấc (The Genesis Core — 0.0s - 3.0s)
- **Prompt:** `Slow camera dolly-in toward a deep obsidian void. A vertical seam of intense royal amethyst and electric cobalt light fractures open. Slender fluted glass needles catch the specular bloom, casting prismatic lavender caustics across the camera lens. Gentle anamorphic horizontal lens flare.`
- **Camera Move:** Slow Dolly In ($Z+ 12\%$), F-stop 2.8, 24fps.

### Scene 2: Khối Kiến Trúc Lắp Ghép (Architectural Alignment — 3.0s - 6.5s)
- **Prompt:** `Multiple monolithic geometric slabs made of translucent dark glass and frosted acrylic slide smoothly and lock into place with magnetic precision. Fine cyan and violet laser meridians trace the bevels of each volume, pulsating with high-frequency capital flow data.`
- **Camera Move:** Orbit Pan 15° Right, Elevation Rise ($Y+ 8\%$).

### Scene 3: Bùng Nổ Hội Tụ Giá Trị (The Apex Convergence — 6.5s - 9.5s)
- **Prompt:** `The separate architectural volumes unify into a monumental central beacon of value. A massive vertical beam of pure white-violet volumetric light erupts toward the sky, illuminating sweeping iridescent ribbons that spiral around the core.`
- **Camera Move:** Crane Pedestal Up, Tilt Up 12°, dramatic volumetric expansion.

### Scene 4: Khóa Nhận Diện Thương Hiệu (The Hero Title Reveal — 9.5s - 12.0s)
- **Prompt:** `The camera slows to a steady authoritative hold. The radiant purple-cobalt atmosphere breathes gently with micro-particles of golden-lavender light. High-contrast typography VMAA DIỄN ĐÀN M&A MIỀN TRUNG 2026 resolves with razor-sharp luminescence.`
- **Camera Move:** Ease-out deceleration to dead stop, subtle slow background drift.

---

## 4. Bảng Tra Cứu Thông Số Kỹ Thuật (Technical Spec Sheet)

| Hạng mục | Quy cách | Mục đích sử dụng |
| :--- | :--- | :--- |
| **Stage Master Video** | `1920×1080` @ 30fps (H.264 High Profile, MP4) | Chiếu màn hình LED hội trường & Livestream |
| **Key Visual Still** | `3840×2160` (4K UHD, 24-bit PNG) | Backdrop sân khấu, Báo chí, Slide Master |
| **Social Media 1:1** | `2160×2160` (PNG) | Facebook, Instagram, LinkedIn Feed |
| **Social Media 4:5** | `2160×2700` (PNG) | Feed tối ưu tỉ lệ vàng trên thiết bị di động |
| **Social Media 9:16** | `2160×3840` (PNG) | Story, Reels, TikTok & Standee điện tử dọc |
| **Event Cover 1.91:1**| `2400×1256` (PNG) | Cover sự kiện Facebook, Banner LinkedIn, Zalo OG |
| **Web Landing Page** | HTML5 / CSS3 / Vanilla JS | Cổng thông tin đăng ký đại biểu & deal matching |
| **3D Engine** | WebGL / Three.js r128 | Trình diễn mô hình 3D tương tác trên web |
