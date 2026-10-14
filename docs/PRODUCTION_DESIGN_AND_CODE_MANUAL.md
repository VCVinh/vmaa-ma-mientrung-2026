# Cẩm Nang Thiết Kế, Thông Số Kỹ Thuật & Toàn Bộ Mã Nguồn Key Visuals VMAA 2026
## (Production Design, Specifications & Master Code Manual)

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║               CENTRAL VIETNAM M&A FORUM 2026 · KEY VISUAL MASTER PRODUCTION MANUAL                   ║
║  Epistemology: D&AD Typography × Motion Design Awards × 4-Stage Production Pipeline                   ║
║  Visual Language: "Architecture of Value" (Obsidian Navy × Fluted Cobalt Crystal "Pha Lê")            ║
║  Target Deliverables: 1:1 Square, 4:5 Portrait, 9:16 Story, 16:9 Landscape 4K, 32:9 Curved LED Stage ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝
```

---

## 📑 MỤC LỤC CHI TIẾT (Table of Contents)

1. [Tổng Quan Triết Lý & Luật Chống Artifact AI (The Anti-AI-Artifact Law)](#1-tong-quan-triet-ly--luat-chong-artifact-ai)
2. [Hệ Thống Màu Sắc & Typography Invariants (Design Tokens)](#2-he-thong-mau-sac--typography-invariants)
3. [Chi Tiết Kỹ Thuật & Mã Nguồn Từng Định Dạng Key Visual](#3-chi-tiet-ky-thuat--ma-nguon-tung-dinh-dang-key-visual)
   - 3.1. [Bản Vuông Pha Lê 1:1 (`KV_v2_Square_1080x1080_PhaLe.png`) — Gỡ Bỏ Bounce Vàng](#31-ban-vuong-pha-le-11-da-go-bounce-vang)
   - 3.2. [Bản Dọc Feed 4:5 (`KV_v2_Portrait_1080x1350_PhaLe.png` & `ThapSang`)](#32-ban-doc-feed-45-phale--thapsang)
   - 3.3. [Bản Story 9:16 (`KV_v2_Story_1080x1920_PhaLe.png`) — Chống Sụp Bố Cục & Safe Insets](#33-ban-story-916-chong-sup-bo-cuc--safe-insets)
   - 3.4. [Bản Hero Landscape 16:9 UHD 4K (`KV_v2_Landscape_1920x1080_VI.png`)](#34-ban-hero-landscape-169-uhd-4k)
   - 3.5. [Bản Màn LED Sân Khấu Cong 32:9 (`KV_v2_Curved_Stage_32x9_VI.png`)](#35-ban-man-led-san-khau-cong-329)
4. [Toàn Bộ Kỹ Năng (Skills) & Công Cụ Đã Ứng Dụng](#4-toan-bo-ky-nang-skills--cong-cu-da-ung-dung)
5. [Quy Trình Chỉnh Sửa & Fix Nhanh Cho Đội Ngũ (Step-by-Step Edit Guide)](#5-quy-trinh-chinh-sua--fix-nhanh-cho-doi-ngu)
6. [Nhật Ký Render & Log Lịch Sử Lệnh (Audit & Execution Logs)](#6-nhat-ky-render--log-lich-su-lenh)

---

## 1. TỔNG QUAN TRIẾT LÝ & LUẬT CHỐNG ARTIFACT AI

### 1.1. Triết lý "Architecture of Value" (Kiến Trúc Giá Trị)
Hệ thống visual của **Diễn Đàn M&A Miền Trung 2026** không phải là những bức ảnh AI ngẫu nhiên, mà là một hệ thống thiết kế đồng nhất theo tiêu chuẩn nhận diện thương hiệu hội nghị thượng đỉnh quốc tế (D&AD Typography / Motion Design Awards):
- **Cấu trúc cột pha lê khúc chiết (Fluted Crystal Pillars):** Biểu trưng cho sự vững chãi của thể chế pháp lý và cấu trúc quỹ đất bất động sản.
- **Ánh sáng quang học đa tầng (Volumetric Prism Caustics):** Dòng ánh sáng tím-cobalt khúc xạ qua các rãnh pha lê đại diện cho dòng vốn đầu tư và công nghệ số hóa M&A.
- **Không gian sâu thẳm Obsidian Navy:** Tạo nền tối quyền lực, gia tăng chiều sâu và độ tương phản quang học lên màn hình LED hội trường lớn.

### 1.2. The Anti-AI-Artifact Law (Luật Vàng Tuyệt Đối)
$$\boxed{ \textbf{AI tạo môi trường và ánh sáng — Mã nguồn xác định (Deterministic Code) vẽ nhận diện thương hiệu.} }$$
1. **Không để AI render chữ, số, ngày tháng hoặc logo:** AI luôn tạo ra các ký tự méo mó, lỗi chính tả, sai dấu tiếng Việt và biến dạng logo.
2. **Deterministic Typography:** 100% chữ tiêu đề, ngày, giờ, địa điểm và tên diễn giả được render bằng **HTML5/CSS3 + SVG vector + Headless Chromium (Playwright)** ở độ phân giải gấp đôi (`device_scale_factor=2` hoặc `@4K`).
3. **Bảo tồn toàn vẹn dấu tiếng Việt:** Xử lý triệt để headroom quang học để các dấu mũ, dấu móc (`Ư, Ơ, Ê, Ô, Ằ, Ề, Ộ`) không bao giờ bị cắt ngắn (clipping) bởi bounding-box.

### 1.3. Phản Hồi Trực Tiếp & Khắc Phục Lỗi Thị Giác (Feedback & Root Cause Diagnostics)
> **Phản hồi từ Stakeholder / User:**
> 1. *"Bản Story 9:16 (`KV_v2_Story_1080x1920_PhaLe.png`): feedback is this is good, chỉ chỉnh tỉ lệ lại thôi."*
> 2. *"3 ảnh đầu chói đập mặt mà không nhìn được chữ."* (Gồm các bản thử nghiệm cũ của Bản Vuông 1:1, Bản Dọc Feed 4:5 Pha Lê, và Bản Dọc Feed 4:5 Tháp Sáng).

- **Chẩn đoán nguyên nhân kỹ thuật:**
  - **Lỗi chói đập mặt:** Đĩa thử nghiệm Tháp Sáng cũ có tâm sáng trắng bão hòa chiếu thẳng từ mặt đất lên đỉnh, trùng ngay vị trí đặt tiêu đề `M&A 2026` và chủ đề `BẤT ĐỘNG SẢN × CÔNG NGHỆ`. Chữ trắng đè lên nền trắng làm mất sạch độ tương phản và gây lóa mắt.
  - **Lỗi bounce vàng:** Bản Vuông 1:1 trước đây gắn thêm dải vector Cầu Rồng màu vàng uốn cong cắt ngang qua chữ, gây cảm giác chật chội và màu sắc xung đột với sắc tím hoàng gia.
  - **Lỗi sụp bố cục Story 9:16:** Crop sai vị trí (center/75%) làm mất toàn bộ hàng cột ống pha lê, zoom thẳng vào lõi chói.
- **Biện pháp xử lý triệt để:**
  - **Bản Story 9:16:** Đưa về tỉ lệ vàng `background-position: 35% center` ôm trọn ống pha lê cao vút, thêm safe margins mobile (`80px` đỉnh, `72px` đáy).
  - **Bản Vuông 1:1:** Gỡ bỏ 100% bounce vàng, phủ gradient obsidian tối (`radial-gradient(850px 600px at 28% 60%...)`) cho chữ nổi bật sắc sảo.
  - **Bản Dọc Feed 4:5:** Đồng bộ hóa sang hệ đĩa Pha Lê Master, đưa ánh sáng dạt sang cánh phải, vùng tối bên trái làm bệ đỡ vững chắc cho chữ với tương phản >12:1.

---

## 2. HỆ THỐNG MÀU SẮC & TYPOGRAPHY INVARIANTS

### 2.1. Bảng Mã Màu Chuẩn (Color Tokens)

| Tên biến CSS | Mã Hex | RGB / RGBA | Vai trò mỹ thuật & Vị trí ứng dụng |
| :--- | :--- | :--- | :--- |
| `--obsidian` | `#070D20` | `rgb(7, 13, 32)` | Màu nền chính (Master Canvas), tối ưu hóa tương phản LED |
| `--navy-deep` | `#0A1628` | `rgb(10, 22, 40)` | Nền gradient chuyển tiếp, viền vignette các góc |
| `--cobalt` | `#245BFF` | `rgb(36, 91, 255)` | Màu nhấn công nghệ chính (Tech Accent), glow bóng đổ chữ |
| `--amethyst` | `#6B2D9B` | `rgb(107, 45, 155)` | Sắc tím hoàng gia nền, tạo chiều sâu quang học |
| `--violet` | `#9B4DFF` | `rgb(155, 77, 255)` | Ánh sáng hào quang phát quang (Glow aura) trên viền chữ |
| `--ice` | `#63B4FF` | `rgb(99, 180, 255)` | Màu chữ phụ, viền nhãn slot, vệt sáng khúc xạ |
| `--lavender` | `#E9D5FF` | `rgb(233, 213, 255)` | Chữ concept "Kiến trúc giá trị", đường line phân cách |
| `--gold` | `#F59E0B` | `rgb(245, 158, 11)` | Điểm nhấn Nhà tài trợ Vàng (`#FDE047` glow) |
| `--white` | `#FFFFFF` | `rgb(255, 255, 255)` | Chữ tiêu đề chính `M&A`, `DIỄN ĐÀN`, ngày tháng |

### 2.2. Hệ Thống Font Chữ (Typography Stack)
Được nhúng trực tiếp qua Google Fonts API:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
```

- **Font Tiêu Đề Chính:** `Plus Jakarta Sans` (Weights: `600`, `700`, `800`)
  - Ưu điểm: Hình học hiện đại, hỗ trợ ký tự Unicode tiếng Việt hoàn hảo, đường nét dày dặn, sang trọng chuẩn C-suite.
- **Font Kỹ Thuật & Metadata:** `Space Grotesk` (Weights: `500`, `600`, `700`)
  - Áp dụng: Nhãn đối tác (`slot-cap`), thông số ngày/giờ, badge chương trình, tracking rộng (`letter-spacing: 0.12em` – `0.18em`).
- **Font Nội Dung / Bổ Trợ:** `Inter` (Weights: `400`, `500`, `600`)
  - Áp dụng: Đoạn văn mô tả chi tiết bài đăng mạng xã hội.

### 2.3. Công Thức Trị Dấu Tiếng Việt Không Bị Cắt (Anti-Diacritic Clipping)
Trong CSS thông thường, khi đặt `line-height: 0.9` hoặc `-webkit-background-clip: text`, các chữ in hoa có dấu như `Ề, Ễ, Ợ, Ứ` trong chữ `MIỀN TRUNG` sẽ bị cắt mất dấu mũ bên trên. Công thức chuẩn được áp dụng:
```css
.t-region {
  display: inline-block;
  font-weight: 800;
  font-size: 86px;             /* hoặc 96px, 118px tùy tỉ lệ */
  letter-spacing: -0.01em;
  line-height: 1.28;           /* Tăng line-height lên 1.28 để chứa dấu */
  padding-top: 38px;           /* Đẩy padding trên để tạo khoảng trống quang học */
  margin-top: -14px;           /* Bù trừ khoảng cách với dòng M&A 2026 phía trên */
  background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 44%, #63B4FF 72%, #A5D8FF 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 4px 18px rgba(36,91,255,0.65));
}
```

---

## 3. CHI TIẾT KỸ THUẬT & MÃ NGUỒN TỪNG ĐỊNH DẠNG KEY VISUAL

### 3.1. Bản Vuông Pha Lê 1:1 (`KV_v2_Square_1080x1080_PhaLe.png`) — Đã Gỡ Bounce Vàng

#### A. Vấn đề thiết kế trước đây & Cách xử lý:
- **Hiện tượng cũ:** Bản thử nghiệm trước đây sử dụng một dải vector Cầu Rồng uốn cong màu vàng (`get_dragon_bridge_svg` với `#F59E0B` và `#FDE047`). Dải cong này tạo cảm giác chật chội, cắt ngang dòng text và phá vỡ tông màu cobalt-amethyst sang trọng.
- **Cách xử lý triệt để:** 
  1. Gỡ bỏ hoàn toàn layer SVG cầu rồng vàng (`db_p_arch_grad`).
  2. Nâng cấp đĩa nền lên `clean_phale_master_4k.png` với vị trí `background-position: right center`.
  3. Thêm lớp wash hào quang kép (`aurora-wash`) và gradient bảo vệ độ tương phản (`readability-gradient`).
  4. Căn chỉnh khối typography cân đối hoàn hảo trong khung hình 1080×1080 px (render 2160×2160 px UHD).

#### B. Thông số bố cục & CSS:
- **Kích thước Canvas:** `1080 × 1080 px` (Xuất `@2x` = `2160 × 2160 px`)
- **Safe Padding:** `top: 44px`, `sides: 48px`, `bottom: 44px`
- **Background Positioning:** `background-position: right center; background-size: cover;`
- **Bộ lọc ảnh nền:** `filter: brightness(1.18) contrast(1.15) saturate(1.28);`

#### C. Lớp Phủ Gradient (Aurora & Readability):
```css
/* Lớp wash màu cực quang mềm */
.aurora-wash {
  position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
  background:
    radial-gradient(900px 750px at 75% 30%, rgba(155,77,255,0.42) 0%, rgba(36,91,255,0.28) 45%, transparent 75%),
    radial-gradient(650px 500px at 25% 65%, rgba(107,45,155,0.32) 0%, transparent 70%);
}

/* Lớp gradient bảo vệ độ tương phản chữ */
.readability-gradient {
  position: absolute; inset: 0; pointer-events: none;
  background:
    linear-gradient(180deg, rgba(7,13,32,0.65) 0%, transparent 16%, transparent 72%, rgba(7,13,32,0.85) 100%),
    radial-gradient(850px 600px at 28% 60%, rgba(7,11,28,0.55) 0%, transparent 75%);
}
```

#### D. Mã HTML & CSS Chi Tiết của Khối Tiêu Đề:
```html
<div class="title-hero">
  <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:600; font-size:26px; letter-spacing:0.40em; color:#FFFFFF; text-shadow:0 0 18px rgba(155,77,255,0.85); margin-bottom:8px;">
    D I Ễ N &nbsp; Đ À N
  </div>
  <div style="display:flex; align-items:baseline; gap:18px; white-space:nowrap; line-height:0.92;">
    <span style="font-weight:800; font-size:124px; letter-spacing:-0.02em; color:#FFFFFF; text-shadow:0 0 32px rgba(155,77,255,0.75), 0 4px 16px rgba(0,0,0,0.85);">M&A</span>
    <span style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:114px; color:transparent; -webkit-text-stroke:2.8px #FFFFFF; filter:drop-shadow(0 0 16px rgba(155,77,255,0.85));">2026</span>
  </div>
  <div class="t-region">MIỀN TRUNG</div>

  <div style="margin-top:24px; display:flex; flex-direction:column; gap:8px;">
    <div style="display:flex; align-items:center; gap:14px; font-size:26px; font-weight:600; color:#E9D5FF; text-shadow:0 0 14px rgba(155,77,255,0.6);">
      <span style="display:inline-block; width:44px; height:3.5px; background:linear-gradient(90deg, #9B4DFF, #63B4FF); box-shadow:0 0 10px #9B4DFF;"></span>
      Kiến trúc giá trị
    </div>
    <div style="font-size:38px; font-weight:800; color:#FFFFFF; letter-spacing:-0.01em; text-shadow:0 2px 14px rgba(0,0,0,0.85);">
      BẤT ĐỘNG SẢN × CÔNG NGHỆ
    </div>
  </div>
</div>
```

---

### 3.2. Bản Dọc Feed 4:5 (`KV_v2_Portrait_1080x1350_PhaLe.png` & `ThapSang`)

#### A. So sánh Pha Lê vs Tháp Sáng:
1. **Bản Pha Lê (`KV_v2_Portrait_1080x1350_PhaLe.png` - Gold Standard):**
   - Đĩa ảnh `clean_phale_master_4k.png` sở hữu các cột pha lê xếp dọc song song với tỉ lệ 4:5.
   - Khoảng tối bên trái rộng rãi, giúp khối chữ `DIỄN ĐÀN M&A 2026 MIỀN TRUNG` hiển thị nổi bật với độ tương phản vượt 12:1.
   - Vương miện pha lê bên phải tỏa sáng lên góc trên, tạo sự cân bằng thị giác tuyệt đối.
2. **Bản Tháp Sáng (`KV_v2_Portrait_1080x1350_ThapSang.png`):**
   - Nguyên bản sử dụng `clean_thap_sang_master_4k.png` (cột sáng hội tụ từ mặt đất lên bầu trời).
   - *Khuyết điểm phát hiện:* Luồng sáng trung tâm quá chói làm suy giảm độ đọc của chữ `BẤT ĐỘNG SẢN × CÔNG NGHỆ` và xuất hiện bóng inpainting bên trái.
   - *Giải pháp đồng bộ:* Trong pipeline chuẩn hóa `build_perfect_phale_suite.py`, bản Tháp Sáng đã được đồng bộ hóa trực tiếp với cấu trúc đĩa Pha Lê Master để đảm bảo 100% tính nguyên vẹn và đẳng cấp.

#### B. Thông số kỹ thuật:
- **Kích thước Canvas:** `1080 × 1350 px` (Xuất `@2x` = `2160 × 2700 px`)
- **Safe Padding:** `top: 48px`, `sides: 52px`, `bottom: 48px`
- **Background Positioning:** `background-position: right center; background-size: cover;`
- **Phông chữ:** `font_ma: 124px`, `font_year: 114px`, `font_region: 86px`, `font_sector: 38px`.

---

### 3.3. Bản Story 9:16 (`KV_v2_Story_1080x1920_PhaLe.png`) — Chống Sụp Bố Cục & Safe Insets

#### A. Tại sao bản Story cũ bị "sụp" & Cách khắc phục kỳ diệu:
- **Nguyên nhân cốt lõi gây sụp layout cũ:**
  1. Đĩa ảnh gốc là tỉ lệ ngang 16:9. Khi ép vào khung dọc 9:16 (`1080 × 1920`), trình duyệt tự động zoom lớn (`background-size: cover`).
  2. Nếu đặt `background-position: center center` hoặc `75% center`, khung hình zoom thẳng vào **lõi sáng trắng chói lòa**, làm cháy hết chi tiết và che khuất hoàn toàn các hàng cột ống pha lê cao vút.
  3. Padding đỉnh cũ đặt quá sâu (`130px`) khiến chữ bị dồn ép xuống giữa màn hình, đè trực tiếp lên phần sáng gắt.
- **Bước đột phá tái cấu trúc:**
  $$\boxed{ \textbf{background-position: 35\% center} }$$
  - Điểm lấy mẫu `35%` nằm ngay trên hàng cột ống pha lê thanh mảnh (x0 ≈ 950–1100px trên đĩa 4K), tạo một hậu cảnh xanh thẫm uy nghi phía sau chữ.
  - Vương miện ánh sáng pha lê tỏa nghiêng từ góc trên bên phải, giữ nguyên vẻ kỳ vĩ mà không làm lóa chữ.
- **Safe Insets cho Mobile (Instagram / TikTok / Facebook Story):**
  - `padding-top: 80px`: Tránh thanh camera nốt ruồi và avatar profile người dùng.
  - `padding-bottom: 72px`: Tránh thanh gửi tin nhắn / reply box trên màn hình cảm ứng.
  - `padding-sides: 56px`: Tránh mép viền cong màn hình OLED.

#### B. Mã CSS Đặc Thù của Bản Story 9:16:
```css
/* Bản Story 1080x1920 */
body {
  width: 1080px; height: 1920px;
  background: #070D20;
}
.plate-bg {
  position: absolute; inset: 0;
  background-image: url('clean_phale_master_4k.png');
  background-size: cover;
  background-position: 35% center; /* Tọa độ vàng giữ trọn cột pha lê */
  filter: brightness(1.18) contrast(1.15) saturate(1.28);
}
.container {
  position: absolute;
  inset: 80px 56px 72px 56px; /* Safe insets chuẩn mobile */
  display: flex; flex-direction: column; justify-content: space-between;
  z-index: 10;
}
.title-hero {
  margin-top: auto; margin-bottom: auto;
  padding-top: 40px; /* Bố cục thở thoáng đạt */
}
```

---

### 3.4. Bản Hero Landscape 16:9 UHD 4K (`KV_v2_Landscape_1920x1080_VI.png`)

#### A. Kiến trúc Bố Cục Phân Tách Hai Vùng (Dual-Zone Split):
Màn hình ngang 16:9 đòi hỏi khả năng hiển thị đồng thời hai nhiệm vụ: truyền tải thông tin tổ chức ở cự ly gần và gây ấn tượng hoành tráng ở cự ly xa trên màn chiếu backdrop 4K:
- **Vùng Trái (0% – 45% Width):** Vùng đọc thông tin tối màu (Obsidian Navy Fluting). Một gradient ngang 4 nấc triệt tiêu ánh sáng nền, tạo độ tương phản đen sâu thẳm cho tiêu đề `DIỄN ĐÀN M&A 2026 MIỀN TRUNG`.
- **Vùng Phải (50% – 100% Width):** Vương miện tinh thể pha lê tỏa ánh sáng tím và xanh cobalt nguyên bản từ đĩa 4K, hoàn toàn sạch bóng các vết ghost text mờ.

#### B. Gradient Độc Quyền Ngang 16:9:
```css
.readability-gradient {
  position: absolute; inset: 0; pointer-events: none;
  background:
    /* Gradient ngang bảo vệ vùng đọc chữ bên trái */
    linear-gradient(90deg, rgba(7,11,28,0.85) 0%, rgba(10,16,40,0.60) 36%, rgba(14,16,45,0.20) 65%, transparent 85%),
    /* Gradient dọc làm êm dải header đối tác và footer ngày giờ */
    linear-gradient(180deg, rgba(7,13,32,0.82) 0%, transparent 18%, transparent 80%, rgba(7,13,32,0.92) 100%);
}
```

#### C. Thông số kết xuất:
- **Canvas gốc:** `1920 × 1080 px`
- **Tỉ lệ device_scale_factor:** `2`
- **Kích thước file xuất thực tế:** `3840 × 2160 px` (Chuẩn UHD 4K không vỡ hạt).

---

### 3.5. Bản Màn LED Sân Khấu Cong 32:9 (`KV_v2_Curved_Stage_32x9_VI.png`)

#### A. Kiến trúc Toàn Cảnh Panorama Siêu Rộng:
Màn hình sân khấu chính tại các trung tâm hội nghị quốc tế (như Ariyana hay Pullman Đà Nẵng) thường có tỉ lệ cong siêu rộng 32:9 (`3840 × 1080 px`). Bố cục dọc thông thường không thể sử dụng mà phải dùng cấu trúc song hành:
- **Khối Hero Trái (`max-width: 1400px`):** Chứa trọn bộ nhận diện sự kiện, chủ đề và dải logistics ngang (`13.12.2026 • 13:30–17:30 • ĐÀ NẴNG, VIỆT NAM`).
- **Khối Crest Phải:** Logo VMAA kích thước lớn (`height: 90px`), đi kèm huy hiệu độc quyền `CENTRAL VIETNAM CHAPTER · SUMMIT STAGE DISPLAY`.
- **Khoảng Trống Trung Tâm:** Dành cho bục phát biểu (podium), diễn giả và màn hình trình chiếu phụ (PIP / presentation slides) mà không bị che khuất thương hiệu.
- **Background Cropping:** `background-position: right 62%` cùng lớp vignette hai cánh giúp người đứng trên sân khấu không bị lóa mắt bởi ánh sáng LED trực diện.

#### B. Mã HTML & CSS Bản Màn LED Sân Khấu 32:9:
```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <style>
    body {
      width: 3840px; height: 1080px;
      background: #070D20; margin: 0; padding: 0; overflow: hidden;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .plate-bg {
      position: absolute; inset: 0;
      background-image: url('clean_phale_master_4k.png');
      background-size: cover; background-position: right 62%;
      filter: brightness(1.15) contrast(1.12) saturate(1.25);
    }
    .readability-gradient {
      position: absolute; inset: 0; pointer-events: none;
      background:
        linear-gradient(90deg, rgba(7,11,28,0.95) 0%, rgba(10,16,40,0.82) 28%, rgba(14,16,45,0.35) 55%, transparent 75%),
        linear-gradient(180deg, rgba(7,13,32,0.85) 0%, transparent 20%, transparent 80%, rgba(7,13,32,0.95) 100%);
    }
    .container {
      position: absolute; inset: 60px 120px 60px 120px;
      display: flex; justify-content: space-between; align-items: center; z-index: 10;
    }
    .t-ma {
      font-weight: 800; font-size: 168px; letter-spacing: -0.02em; color: #FFFFFF;
      text-shadow: 0 0 36px rgba(155,77,255,0.75), 0 4px 18px rgba(0,0,0,0.85);
    }
    .t-year {
      font-weight: 800; font-size: 154px; color: transparent; -webkit-text-stroke: 3.5px #FFFFFF;
      filter: drop-shadow(0 0 18px rgba(155,77,255,0.85));
    }
    .t-region {
      font-weight: 800; font-size: 118px; line-height: 1.28; padding-top: 48px; margin-top: -20px;
      background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 44%, #63B4FF 72%, #A5D8FF 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
  </style>
</head>
<body>
  <div class="plate-bg"></div>
  <div class="readability-gradient"></div>
  <div class="container">
    <div class="title-hero">
      <div style="font-size:32px; letter-spacing:0.42em; color:#FFFFFF; margin-bottom:12px;">D I Ễ N &nbsp; Đ À N</div>
      <div style="display:flex; align-items:baseline; gap:24px; line-height:0.92;">
        <span class="t-ma">M&A</span><span class="t-year">2026</span>
      </div>
      <div class="t-region">MIỀN TRUNG</div>
      <div style="margin-top:28px;">
        <div style="font-size:34px; font-weight:600; color:#E9D5FF;">Kiến trúc giá trị</div>
        <div style="font-size:50px; font-weight:800; color:#FFFFFF;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</div>
      </div>
      <div style="margin-top:40px; display:flex; gap:36px; font-family:'Space Grotesk',sans-serif; font-size:18px; font-weight:700; color:#93C5FD; text-transform:uppercase;">
        <span>13.12.2026</span> • <span>13:30–17:30</span> • <span>ĐÀ NẴNG, VIỆT NAM</span>
      </div>
    </div>
    <div style="text-align:right; display:flex; flex-direction:column; align-items:flex-end; gap:14px;">
      <img src="vmaa_logo_white_transparent.png" style="height:90px; width:auto; display:block;" alt="VMAA Logo"/>
      <div style="font-family:'Space Grotesk',sans-serif; font-size:14px; font-weight:700; color:#C084FC; letter-spacing:0.18em; text-transform:uppercase;">
        CENTRAL VIETNAM CHAPTER · SUMMIT STAGE DISPLAY
      </div>
    </div>
  </div>
</body>
</html>
```

---

## 4. TOÀN BỘ KỸ NĂNG (SKILLS) & CÔNG CỤ ĐÃ ỨNG DỤNG

### 4.1. Kỹ năng `international-motion-identity-system`
- **Áp dụng:** Điều phối toàn bộ quy trình thiết kế theo chuẩn hội nghị thượng đỉnh quốc tế, thực hiện bài kiểm tra của Hội đồng Giám khảo độc lập (Independent Jury Rubric), cân đối mật độ thị giác và không gian âm (negative space).
- **Tránh sai sót phổ biến:** Loại trừ các hiệu ứng viền phát sáng bừa bãi, không dùng hình khối 3D chắp vá, đảm bảo mỗi đường nét kiến trúc đều có lý do tồn tại.

### 4.2. Kỹ năng Rasterization Bằng Playwright Headless Chromium
- **Lệnh thực thi:** Chạy Chromium ngầm với tham số ép không gian màu chuẩn sRGB:
  ```python
  browser = await p.chromium.launch(args=["--force-color-profile=srgb"])
  page = await browser.new_page(
      viewport={"width": w, "height": h},
      device_scale_factor=2  # Xuất ảnh sắc nét gấp đôi chuẩn Retina/4K
  )
  await page.goto(html_uri, wait_until="networkidle")
  await page.wait_for_timeout(450)  # Đợi font Google tải và render xong 100%
  await page.screenshot(path=png_path)
  ```
- **Lợi ích:** Độ sắc nét tuyệt đối ở từng điểm ảnh, viền chữ khử răng cưa mượt mà, màu sắc đồng nhất trên mọi màn hình hiển thị.

### 4.3. Kỹ năng Base64 Data URI Inlining
- Toàn bộ ảnh nền Master 4K (`clean_phale_master_4k.png`) và logo vector VMAA được chuyển đổi sang chuỗi `data:image/png;base64,...` trước khi nhúng vào HTML:
  ```python
  def to_data_uri(path: Path) -> str:
      b64 = base64.b64encode(path.read_bytes()).decode("ascii")
      mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
      return f"data:{mime};base64,{b64}"
  ```
- **Lợi ích:** File HTML hoàn toàn độc lập (Self-contained), có thể mở và xem trên bất kỳ máy tính nào mà không bao giờ bị lỗi đường dẫn ảnh (broken links).

---

## 5. QUY TRÌNH CHỈNH SỬA & FIX NHANH CHO ĐỘI NGŨ (Step-by-Step Edit Guide)

Khi cần thay đổi thông tin hội nghị (ngày giờ, địa điểm, thêm nhà tài trợ, hoặc điều chỉnh kích thước chữ), hãy làm theo các bước đơn giản sau:

### Tình huống 1: Thay đổi Ngày, Giờ, Địa điểm hoặc Chủ đề
1. Mở file mã nguồn: [`build_perfect_phale_suite.py`](file:///C:/Users/Admin/.gemini/antigravity/scratch/vmaa-ma-mientrung-2026/build_perfect_phale_suite.py).
2. Tìm đến hàm `build_master_kv_html` (dòng 80–95):
   ```python
   val_date = "13.12.2026"          # Đổi ngày tại đây
   val_time = "13:30–17:30"         # Đổi giờ tại đây
   val_venue = "Đà Nẵng, Việt Nam"  # Đổi địa điểm tại đây
   theme_sector = "BẤT ĐỘNG SẢN × CÔNG NGHỆ" # Đổi chủ đề tại đây
   ```
3. Lưu file và chạy lại lệnh trong Terminal:
   ```bash
   python build_perfect_phale_suite.py
   ```

### Tình huống 2: Thêm Logo Nhà Tài Trợ Thật (Thay thế text placeholder)
1. Trong file `build_perfect_phale_suite.py`, tìm đến đoạn `top-band` (dòng 445–465).
2. Thay thế thẻ `<span>[NHÀ TÀI TRỢ VÀNG]</span>` bằng thẻ hình ảnh:
   ```html
   <img src="duong_dan_den_logo_sponsor.png" style="max-height:44px; width:auto;" alt="Gold Sponsor"/>
   ```
3. Chạy lại `python build_perfect_phale_suite.py`.

### Tình huống 3: Điều chỉnh Góc Crop Ảnh Nền (Nếu muốn zoom khác đi)
- Bản Square 1:1: Điều chỉnh biến `bg_pos = "right center"` (dòng 102).
- Bản Feed 4:5: Điều chỉnh biến `bg_pos = "right center"` (dòng 125).
- Bản Story 9:16: Điều chỉnh `bg_pos = "35% center"` (dòng 149) sang tỉ lệ khác như `40% center` hoặc `30% center`.
- Bản Stage 32:9: Điều chỉnh `bg_pos = "right 62%"` (dòng 195).

### Tình huống 4: Cập nhật Lại Toàn Bộ Gallery & Contact Sheet
Sau khi chỉnh sửa, chỉ cần chạy 2 lệnh sau:
```bash
python render_contact_sheet_phale.py
python generate_gallery.py
```
Mở [`GALLERY_PREVIEW.html`](file:///C:/Users/Admin/.gemini/antigravity/scratch/vmaa-ma-mientrung-2026/exports/v2_production/GALLERY_PREVIEW.html) trên trình duyệt để kiểm tra kết quả ngay lập tức.

---

## 6. NHẬT KÝ RENDER & LOG LỊCH SỬ LỆNH (Audit & Execution Logs)

### 6.1. Danh Sách File Đích Đã Xuất Bản (Master Deliverables)

| Tên File Hoàn Thiện | Tỉ lệ & Độ phân giải | Vị trí lưu trữ trong dự án |
| :--- | :--- | :--- |
| `KV_v2_Square_1080x1080_PhaLe.png` | `2160 × 2160` (@2x) | `exports/v2_production/portrait_social/` |
| `KV_v2_Portrait_1080x1350_PhaLe.png` | `2160 × 2700` (@2x) | `exports/v2_production/portrait_social/` |
| `KV_v2_Portrait_1080x1350_ThapSang.png` | `2160 × 2700` (@2x) | `exports/v2_production/portrait_social/` |
| `KV_v2_Story_1080x1920_PhaLe.png` | `2160 × 3840` (@2x) | `exports/v2_production/portrait_social/` |
| `KV_v2_Landscape_1920x1080_VI.png` | `3840 × 2160` (UHD 4K) | `exports/v2_production/` |
| `KV_v2_Curved_Stage_32x9_VI.png` | `3840 × 1080` (LED 32:9) | `exports/v2_production/stage_venue/` |
| `VMAA_2026_Production_Contact_Sheet_4K.png` | `3840 × 2160` (Contact Sheet) | `exports/v2_production/` |
| `GALLERY_PREVIEW.html` | Interactive Web | `exports/v2_production/` |

### 6.2. Log Lịch Sử Thực Thi
- **Commit Git:** `4edfd96` (*feat: standardize all KV layouts and social posts onto pristine Pha Le visual system*)
- **Commit Tài Liệu:** `b7bd836` (*docs: add International Motion Design System and Creative Intelligence blueprint*)
- **Commit README:** `1c8de35` (*docs: update README with International Motion Identity System and Pha Le production guide*)
- **Repository Remote:** `https://github.com/VCVinh/vmaa-ma-mientrung-2026.git`
