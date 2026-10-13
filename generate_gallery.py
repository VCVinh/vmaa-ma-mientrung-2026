import os

base_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026\exports\v2_production"
html_path = os.path.join(base_dir, "GALLERY_PREVIEW.html")

categories = {
    "1. Dạng Đứng & Story Master (Tháp Sáng vs Pha Lê @2x Retina)": [
        ("portrait_social/KV_v2_Story_1080x1920_ThapSang.png", "Tháp Sáng - Story 9:16 (2160x3840)"),
        ("portrait_social/KV_v2_Portrait_1080x1350_ThapSang.png", "Tháp Sáng - Feed Dọc 4:5 (2160x2700)"),
        ("portrait_social/KV_v2_Square_1080x1080_ThapSang.png", "Tháp Sáng - Vuông 1:1 (2160x2160)"),
        ("portrait_social/KV_v2_Story_1080x1920_PhaLe.png", "Pha Lê - Story 9:16 (2160x3840)"),
        ("portrait_social/KV_v2_Portrait_1080x1350_PhaLe.png", "Pha Lê - Feed Dọc 4:5 (2160x2700)"),
        ("portrait_social/KV_v2_Square_1080x1080_PhaLe.png", "Pha Lê - Vuông 1:1 (2160x2160)")
    ],
    "2. Hero Key Visual & Sân Khấu (Landscape 16:9 & LED 32:9)": [
        ("KV_v2_Landscape_1920x1080_VI.png", "Hero Landscape 16:9 (3840x2160 UHD)"),
        ("KV_v2_Landscape_1920x1080_EN.png", "Hero Landscape English 16:9"),
        ("stage_venue/KV_v2_Curved_Stage_32x9_VI.png", "Màn LED Cong 32:9 (3840x1080)"),
        ("VMAA_2026_Production_Contact_Sheet_4K.png", "Bảng tổng hợp Contact Sheet 4K")
    ],
    "3. Diễn Giả & Khách Mời VIP (Crystal Fluted Suite)": [
        ("guests_motion/GUEST_01_Portrait_1080x1350.png", "Thiệp Diễn Giả Feed 4:5"),
        ("guests_motion/GUEST_01_Story_1080x1920.png", "Thiệp Diễn Giả Story 9:16"),
        ("guests_motion/GUEST_01_Square_1200x1200.png", "Thiệp Diễn Giả Vuông 1:1"),
        ("guests_motion/VMAA_Guest_LowerThird_Master.png", "Bảng tên Lower-Third Broadcast 4K")
    ],
    "4. Ma Trận 6 Chủ Đề Social Media (42 Định Dạng)": [
        ("social_media/POST_01_1080x1350.png", "POST 01 - Công Bố Sự Kiện (4:5)"),
        ("social_media/POST_02_1080x1350.png", "POST 02 - Kiến Trúc Giá Trị (4:5)"),
        ("social_media/POST_03_1080x1350.png", "POST 03 - Bất Động Sản (4:5)"),
        ("social_media/POST_04_1080x1350.png", "POST 04 - Công Nghệ (4:5)"),
        ("social_media/POST_05_1080x1350.png", "POST 05 - Diễn Giả (4:5)"),
        ("social_media/POST_06_1080x1350.png", "POST 06 - Đăng Ký Tham Gia (4:5)")
    ]
}

html = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VMAA 2026 - Master Image Gallery & Production Deliverables</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #050814;
    color: #F8FAFC;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    padding: 30px;
  }
  header {
    text-align: center;
    margin-bottom: 40px;
    padding-bottom: 25px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
  }
  h1 {
    font-size: 32px;
    font-weight: 800;
    letter-spacing: 1px;
    background: linear-gradient(135deg, #FFFFFF 30%, #38BDF8 70%, #A855F7 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
  }
  .subtitle {
    font-size: 16px;
    color: #94A3B8;
  }
  .folder-bar {
    margin-top: 15px;
    padding: 10px 18px;
    background: rgba(56, 189, 248, 0.08);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 8px;
    display: inline-block;
    font-family: monospace;
    font-size: 13px;
    color: #38BDF8;
  }
  .section-title {
    font-size: 22px;
    font-weight: 700;
    color: #38BDF8;
    margin: 35px 0 15px 0;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 24px;
    margin-bottom: 30px;
  }
  .card {
    background: #0D1424;
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    display: flex;
    flex-direction: column;
  }
  .card:hover {
    transform: translateY(-4px);
    border-color: #38BDF8;
    box-shadow: 0 12px 30px rgba(56, 189, 248, 0.25);
  }
  .card-img-wrap {
    background: #020617;
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 280px;
    max-height: 440px;
    overflow: hidden;
    cursor: pointer;
  }
  .card img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    transition: transform 0.3s;
  }
  .card:hover img {
    transform: scale(1.02);
  }
  .card-body {
    padding: 14px 18px;
    background: #0D1424;
    border-top: 1px solid rgba(255,255,255,0.06);
  }
  .card-title {
    font-size: 15px;
    font-weight: 600;
    color: #F1F5F9;
    margin-bottom: 6px;
  }
  .card-meta {
    font-size: 12px;
    color: #64748B;
    font-family: monospace;
  }
  .btn-open {
    display: inline-block;
    margin-top: 8px;
    padding: 6px 14px;
    font-size: 12px;
    font-weight: 600;
    background: rgba(56, 189, 248, 0.15);
    color: #38BDF8;
    text-decoration: none;
    border-radius: 6px;
    border: 1px solid rgba(56, 189, 248, 0.3);
  }
  .btn-open:hover {
    background: #38BDF8;
    color: #000;
  }
  /* Lightbox */
  #lightbox {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.94);
    z-index: 9999;
    justify-content: center;
    align-items: center;
    padding: 20px;
  }
  #lightbox img {
    max-width: 95vw;
    max-height: 95vh;
    border-radius: 8px;
    box-shadow: 0 0 50px rgba(56,189,248,0.5);
  }
  #lightbox-close {
    position: absolute;
    top: 20px; right: 30px;
    color: #FFF;
    font-size: 40px;
    cursor: pointer;
    font-weight: bold;
  }
</style>
</head>
<body>

<header>
  <h1>DIỄN ĐÀN M&A MIỀN TRUNG 2026</h1>
  <div class="subtitle">BẤT ĐỘNG SẢN × CÔNG NGHỆ · 13.12.2026 · ĐÀ NẴNG | BỘ SƯU TẬP HÌNH ẢNH TOÀN DIỆN (RETINA @2X)</div>
  <div class="folder-bar">📂 Thư mục chứa ảnh: exports/v2_production/</div>
</header>
"""

for cat, items in categories.items():
    html += f'<div class="section-title">{cat}</div><div class="grid">'
    for rel_path, title in items:
        html += f"""
        <div class="card">
          <div class="card-img-wrap" onclick="openLightbox('{rel_path}')">
            <img src="{rel_path}" alt="{title}" loading="lazy">
          </div>
          <div class="card-body">
            <div class="card-title">{title}</div>
            <div class="card-meta">{rel_path}</div>
            <a class="btn-open" href="{rel_path}" target="_blank">Xem ảnh gốc kích thước lớn</a>
          </div>
        </div>
        """
    html += "</div>"

html += """
<div id="lightbox" onclick="closeLightbox()">
  <span id="lightbox-close">&times;</span>
  <img id="lightbox-img" src="" alt="">
</div>

<script>
function openLightbox(src) {
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox').style.display = 'flex';
}
function closeLightbox() {
  document.getElementById('lightbox').style.display = 'none';
}
</script>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Generated {html_path} successfully!")
