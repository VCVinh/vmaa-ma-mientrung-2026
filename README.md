# Diễn Đàn M&A Miền Trung 2026 — Master Visual Identity & Motion Design System

> **International Conference Brand & Motion Graphics System**  
> **Event:** Diễn đàn M&A Miền Trung 2026  
> **Focus:** Bất Động Sản — Công Nghệ (Real Estate — Technology)  
> **Date & Time:** 13.12.2026 · 13:30 – 17:30 · Đà Nẵng, Việt Nam  
> **Host:** Hiệp hội Mua bán và Sáp nhập Doanh nghiệp Việt Nam (VMAA) · Central Vietnam Chapter  

---

## 🌟 1. Tổng Quan Dự Án & Ý Niệm Sáng Tạo (Architecture of Value)

Dự án thiết kế nhận diện hình ảnh và chuyển động (Motion Graphics) cho **Diễn đàn M&A Miền Trung 2026** được xây dựng dựa trên tiêu chuẩn các hội nghị kinh tế - công nghệ thượng đỉnh thế giới (Milken Institute, Next Forum, World Economic Forum, GITEX Global):

- **Ý niệm trung tâm — "Architecture of Value" (Kiến trúc Giá trị):** Sự hội tụ và chuyển hóa giữa các khối hình học kiến trúc khúc chiết (Bất động sản) và mạng lưới dữ liệu phát sáng (Công nghệ), hòa nhập thành một cấu trúc giá trị tối thượng, bền vững.
- **Dải màu "Loan Loan" Đột Phá (High-Luminosity Purple × Cobalt Spectrum):** Thoát khỏi cảm giác tối hoặc chìm màu truyền thống. Ánh sáng phát quang đa tầng (Multi-layered Volumetric Luminescence) tỏa rực từ lõi pha lê:
  - **Base:** Obsidian Navy (`#070D20` – `#0A1628`)
  - **Core Purple Accent:** Royal Amethyst (`#6B2D9B`) $\to$ Electric Violet (`#9B4DFF`) $\to$ Soft Lavender (`#E9D5FF`)
  - **Primary Tech Accent:** Electric Cobalt (`#245BFF`) $\to$ Ice Cyan (`#63B4FF`) $\to$ Specular White (`#FFFFFF`)
  - **High-Contrast Warm Accent:** Imperial Gold / Champagne (`#F59E0B` – `#FDE047`)

---

## 📂 2. Cấu Trúc Thư Mục Dự Án (Repository Structure)

```text
vmaa-ma-mientrung-2026/
├── assets/
│   ├── Logo_VMAA_5_2026.svg               # Vector gốc logo VMAA
│   ├── vmaa_logo_white_transparent.png     # Logo VMAA trắng tách nền siêu sắc nét (1454x605)
│   ├── vmaa_logo_blue_transparent.png      # Logo VMAA xanh chuẩn nhận diện (1454x605)
│   ├── vmaa_wordmark_white_transparent.png # Wordmark VMAA trắng tách nền (1454x400)
│   ├── vmaa_wordmark_blue_transparent.png  # Wordmark VMAA xanh tách nền (1454x400)
│   └── plates/                             # Bộ plates kết xuất 3D & AI khuếch tán cao cấp
├── exports/
│   ├── 01_VMAA_HERO_KEY_VISUAL_4K.png      # Key Visual Master 4K (16:9)
│   ├── 00_VMAA_6_Options_Comparison_Matrix.png # Bảng đối chiếu 6 sắc độ tím-cobalt 4K
│   ├── 07_VMAA_Multi_Aspect_Venue_Suite.png# Sân khấu LED (32:9, 9:16, Lower-Third, MOU)
│   ├── 08_VMAA_GITEX_Hanging_Banners_Stage.png # Standee & Banner treo quy mô GITEX
│   ├── 09_VMAA_Next_Forum_Format_HighKey_4K.png # Poster Diễn giả định dạng Next Forum (High-Key)
│   ├── 09_VMAA_Next_Forum_Format_ObsidianPurple_4K.png # Poster Diễn giả Next Forum (Dark)
│   ├── 10_VMAA_Social_Landing_Slide_Ratio_Suite.png # Tổng hợp mọi tỉ lệ đa kênh 4K
│   ├── OPT_01_Monolith_Convergence.png     # Sắc độ 01: Royal Amethyst Hero
│   ├── OPT_02_Ascending_Equilibrium.png    # Sắc độ 02: Electric Violet & Script 20/26
│   ├── OPT_03_Coastal_Meridian_Contours.png# Sắc độ 03: Sapphire & Cantilevers
│   ├── OPT_04_Luminous_Tri_Portal.png      # Sắc độ 04: Ultraviolet Contours
│   ├── OPT_05_Isometric_Deal_Matrix.png    # Sắc độ 05: Crystal Deal Matrix
│   ├── OPT_06_Fluted_Prism_Curtain.png     # Sắc độ 06: High-Key Lavender Aurora
│   ├── social_media/                       # Trọn bộ ảnh Social Media (1:1, 4:5, 9:16, 1.91:1)
│   ├── landing_page/                       # Above-the-fold Hero UI (4K UHD)
│   └── slide_deck/                         # Bộ Slide thuyết trình 4K (Slides 01 - 04)
├── videos/
│   ├── VMAA_2026_Opener_Master.mp4         # Video mở màn sân khấu 1080p 30fps H.264
│   ├── VMAA_2026_Opener_Preview.webm       # Video web preview VP9
│   └── opener_audio.wav                    # Âm thanh synth cinematic mở màn
├── index.html                              # WebGL 3D Interactive Motion Studio
├── landing_page.html                       # Landing Page đầy đủ tính năng HTML5/CSS3
├── vmaa_draft_content_config.json          # File cấu hình nội dung nguồn duy nhất (Single Source of Truth)
├── shot_prompts_manifest.json              # Prompt manifest AI tạo hình ảnh & video
├── blender_architecture_of_value.py        # Script Blender 3D procedural animation
├── build_vmaa_6_options.py                 # Pipeline xuất 6 Option Key Visual 4K & Video
├── build_vmaa_next_forum_format.py         # Pipeline xuất Poster Next Forum Format 4K
├── build_social_landing_slide_suite.py     # Pipeline xuất Social Media, Landing & Slides 4K
├── COLLABORATION_GUIDE.md                  # Hướng dẫn chi tiết cho thành viên cộng tác
├── PROMPTS_AND_STRATEGY.md                 # Cẩm nang Prompt Engineering & Chiến lược Mỹ thuật
└── requirements.txt                        # Thư viện phụ thuộc Python
```

---

## 🎨 3. Hệ Thống Tài Nguyên Đã Xuất Bản (Deliverables)

### 3.1. Master Key Visuals & 6 Sắc Độ ("Loan Loan" Spectrum)
1. **01_VMAA_HERO_KEY_VISUAL_4K.png:** Key Visual chính 16:9 4K (`3840×2160`), ánh sáng tím quang phổ hội tụ từ lõi, chữ sắc nét, sẵn sàng cho màn hình LED chính.
2. **6 Sắc độ Tùy biến (`OPT_01` $\to$ `OPT_06`):**
   - *Tone 01:* Royal Amethyst × Electric Cobalt
   - *Tone 02:* Electric Violet × Prismatic Caustics (chữ nghệ thuật `20/26` & handwriting script)
   - *Tone 03:* Stretched Futuristic Display (`Unbounded`)
   - *Tone 04:* Ultraviolet × Ice-Cyan Contours
   - *Tone 05:* Imperial Purple × Isometric Crystal Matrix
   - *Tone 06:* High-Key Lavender Aurora Stage Portal

### 3.2. Poster Diễn Giả Định Dạng Next Forum 2026
Được thiết kế lấy cảm hứng trực tiếp từ bố cục poster **Next Forum 2026**:
- **Dải Header Nhà tài trợ:** Phân loại minh bạch (`NHÀ TÀI TRỢ ĐỒNG HÀNH`, `NHÀ TÀI TRỢ VÀNG`, `ĐƠN VỊ TỔ CHỨC VMAA`, `ĐỐI TÁC HỌC THUẬT DUE`, `NHÀ TÀI TRỢ BẠC`).
- **Cột Trái (Brand & Chủ đề):** Logo `VMAA FORUM 2026`, Tiêu đề `DIỄN ĐÀN M&A MIỀN TRUNG`, Slogan nổi bật `KIẾN TRÚC GIÁ TRỊ: BẤT ĐỘNG SẢN × CÔNG NGHỆ`, thời gian & địa điểm, kèm khối điêu khắc 3D Hero.
- **Khu vực Phải (Lưới 6 Diễn Giả VIP):** 6 Diễn giả trong khung oval viền sáng hào quang (Dual-ring halo) với tên viết hoa hiện đại và chức danh vĩ mô.
- **Footer Đối tác:** Đơn vị hỗ trợ, Quỹ đầu tư quốc tế và các cơ quan truyền thông lớn.
- **File xuất:**
  - `09_VMAA_Next_Forum_Format_HighKey_4K.png` (Phiên bản High-Key Platinum sang trọng)
  - `09_VMAA_Next_Forum_Format_ObsidianPurple_4K.png` (Phiên bản Deep Obsidian Purple quyền lực)

### 3.3. Bộ Tỉ Lệ Đa Nền Tảng (Social, Landing, Slides)
- **1:1 Square Post (`2160×2160`):** Facebook/LinkedIn/Instagram square feed.
- **4:5 Portrait Feed (`2160×2700`):** Tỉ lệ vàng tối ưu tương tác trên mobile feed.
- **9:16 Vertical (`2160×3840`):** Story, Reels, TikTok, Zalo video & Standee sân khấu dọc.
- **1.91:1 Landscape (`2400×1256`):** Facebook/LinkedIn Event Cover & link preview OG.
- **Landing Page Hero (`3840×2160` + `landing_page.html`):** Giao diện web hoàn chỉnh với bộ đếm ngược, form đăng ký VIP và lịch trình.
- **Slide Deck 16:9 (`3840×2160`):** Bìa thuyết trình, Agenda timeline, Biểu đồ dữ liệu M&A, Giới thiệu diễn giả.

### 3.4. Video & Motion Graphics
- **`VMAA_2026_Opener_Master.mp4` (`1920×1080` 30fps H.264):** Phim mở màn sân khấu 12 giây hoàn chỉnh hiệu ứng ánh sáng quang sai, chùm sáng tím-cobalt hội tụ và âm thanh stereo ambient.
- **`index.html`:** Trình duyệt 3D WebGL với Three.js cho phép quay camera 360°, đổi 6 tone màu trực tiếp trên trình duyệt.

---

## 🚀 4. Hướng Dẫn Nhanh Cho Thành Viên Đội Ngũ (Quickstart)

### Cài đặt môi trường
Yêu cầu Python 3.10+ và các thư viện cần thiết:
```bash
pip install -r requirements.txt
playwright install chromium
```

### Thay đổi nội dung hội nghị (Tên, ngày, diễn giả, số liệu)
Chỉ cần chỉnh sửa trực tiếp file **`vmaa_draft_content_config.json`**. Tất cả các script sẽ tự động nạp dữ liệu từ file này.

### Xuất lại toàn bộ hình ảnh 4K & Video
```bash
# Xuất 6 Key Visuals, Sân khấu LED & Video mở màn:
python build_vmaa_6_options.py

# Xuất Poster định dạng Next Forum (High-Key & Dark):
python build_vmaa_next_forum_format.py

# Xuất trọn bộ Social Media, Landing Page & Slides:
python build_social_landing_slide_suite.py
```

Xem chi tiết quy trình phối hợp làm việc tại [COLLABORATION_GUIDE.md](./COLLABORATION_GUIDE.md).
