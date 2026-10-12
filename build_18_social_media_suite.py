import os
import sys
import json
import base64
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

PROJECT_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")

TOKENS_PATH = PROJECT_DIR / "src" / "tokens" / "design_tokens.json"
DATA_PATH = PROJECT_DIR / "src" / "data" / "event_data.json"

tokens = json.loads(TOKENS_PATH.read_text(encoding="utf-8"))
data = json.loads(DATA_PATH.read_text(encoding="utf-8"))

EXPORT_BASE = PROJECT_DIR / "exports" / "social_media"
DIR_1350 = EXPORT_BASE / "1080x1350"
DIR_1920 = EXPORT_BASE / "1080x1920"
DIR_1080 = EXPORT_BASE / "1080x1080"

for d in [DIR_1350, DIR_1920, DIR_1080]:
    d.mkdir(parents=True, exist_ok=True)

def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    suffix = path.suffix.lower()
    if suffix == ".png":
        mime = "image/png"
    elif suffix in [".jpg", ".jpeg"]:
        mime = "image/jpeg"
    elif suffix == ".svg":
        mime = "image/svg+xml"
    else:
        mime = "application/octet-stream"
    return f"data:{mime};base64,{b64}"

PLATES_DIR = PROJECT_DIR / "assets" / "plates"
u_hero_plate = to_data_uri(PLATES_DIR / "purple_opt01_hero_convergence.jpg")
u_fluted_plate = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u_ascending_plate = to_data_uri(PLATES_DIR / "purple_opt03_ascending_cantilevers.jpg")
u_contours_plate = to_data_uri(PLATES_DIR / "purple_opt04_ultraviolet_contours.jpg")
u_isometric_plate = to_data_uri(PLATES_DIR / "purple_opt05_imperial_isometric.jpg")
u_aurora_plate = to_data_uri(PLATES_DIR / "purple_opt06_highkey_aurora_stage.jpg")
u_logo_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")

FONTS_HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,800&family=Manrope:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
"""

COMMON_STYLE = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #070D20;
  color: #FFFFFF;
  font-family: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, sans-serif;
  overflow: hidden;
  position: relative;
  -webkit-font-smoothing: antialiased;
}
.mono { font-family: 'Manrope', sans-serif; text-transform: uppercase; letter-spacing: 0.18em; }
.aurora {
  position: absolute; inset: 0; pointer-events: none; mix-blend-mode: screen;
  background:
    radial-gradient(850px 750px at 70% 35%, rgba(155,77,255,0.38) 0%, rgba(36,91,255,0.22) 50%, transparent 80%),
    radial-gradient(650px 550px at 25% 70%, rgba(107,45,155,0.32) 0%, transparent 75%);
}
.shade {
  position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(180deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.35) 40%, rgba(7,13,32,0.5) 65%, rgba(7,13,32,0.95) 100%);
}
.gold { color: #FACC15; }
.cyan { color: #38BDF8; }
.lavender { color: #D8B4FE; }
"""

# Template definitions for the 6 posts
# Each post generator takes (width, height, ratio_name)

def generate_post_01(w, h, ratio):
    """POST 01: OFFICIAL EVENT ANNOUNCEMENT"""
    pad_top = 100 if h == 1920 else (80 if h == 1350 else 60)
    pad_side = 80 if w == 1080 else 60
    title_size = 92 if h == 1920 else (84 if h == 1350 else 76)
    region_size = 76 if h == 1920 else (68 if h == 1350 else 62)
    logo_h = 52 if h == 1920 else 46

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS_HEAD}
    <style>{COMMON_STYLE}
      body {{ width: {w}px; height: {h}px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_hero_plate}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:{pad_side}px {pad_side}px {pad_top}px {pad_side}px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .tag {{ font-family:'Manrope',sans-serif; font-size:13px; font-weight:800; letter-spacing:0.22em; color:#38BDF8; text-transform:uppercase; margin-bottom:12px; }}
      .title {{ font-size:{title_size}px; font-weight:900; line-height:0.95; letter-spacing:-0.03em; text-transform:uppercase; color:#FFFFFF; margin-bottom:6px; }}
      .region {{ font-size:{region_size}px; font-weight:900; line-height:1; letter-spacing:-0.02em; text-transform:uppercase; background: linear-gradient(135deg, #B77BFF 0%, #7C3AED 50%, #2563EB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:24px; filter: drop-shadow(0 0 25px rgba(155,77,255,0.5)); }}
      .theme {{ font-size:20px; font-weight:700; color:#F1F5F9; line-height:1.4; margin-bottom:20px; }}
      .footer-meta {{ border-top:1px solid rgba(155,77,255,0.3); padding-top:20px; display:flex; justify-content:space-between; align-items:flex-end; }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:{logo_h}px; width:auto;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#94A3B8;">OFFICIAL ANNOUNCEMENT</div>
        </div>
        <div>
          <div class="tag">● RA MẮT VMAA MIỀN TRUNG · ĐÀ NẴNG 2026</div>
          <div class="mono" style="font-size:26px; font-weight:800; letter-spacing:0.1em; color:#FFFFFF; margin-bottom:4px;">DIỄN ĐÀN</div>
          <div class="title">M&A 2026</div>
          <div class="region">MIỀN TRUNG</div>
          <div class="theme">KIẾN TRÚC GIÁ TRỊ: <span class="gold" style="font-style:italic; font-weight:800;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</span></div>
        </div>
        <div class="footer-meta">
          <div>
            <div class="mono" style="font-size:11px; font-weight:700; color:#94A3B8; margin-bottom:4px;">THỜI GIAN & ĐỊA ĐIỂM</div>
            <div style="font-size:18px; font-weight:800; color:#FFFFFF;">Chủ Nhật · 13.12.2026</div>
            <div style="font-size:13px; font-weight:600; color:#D8B4FE;">13:30 – 17:30 · Đà Nẵng, Việt Nam</div>
          </div>
          <div class="mono" style="font-size:13px; font-weight:800; color:#FACC15; letter-spacing:0.18em;">1,500+ DELEGATES</div>
        </div>
      </div>
    </body></html>"""

def generate_post_02(w, h, ratio):
    """POST 02: THE CENTRAL CONCEPT (REAL ESTATE × TECHNOLOGY)"""
    pad_side = 80 if w == 1080 else 60
    head_size = 64 if h == 1920 else (56 if h == 1350 else 50)

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS_HEAD}
    <style>{COMMON_STYLE}
      body {{ width: {w}px; height: {h}px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_fluted_plate}') center/cover; filter: brightness(1.1) contrast(1.15); }}
      .shell {{ position:absolute; inset:{pad_side}px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .concept-box {{ background: rgba(10,16,38,0.78); border: 1px solid rgba(155,77,255,0.45); border-radius:14px; padding:36px; backdrop-filter:blur(24px); box-shadow:0 20px 50px rgba(0,0,0,0.6); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:46px; width:auto;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#38BDF8;">CENTRAL CONCEPT</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; font-weight:800; letter-spacing:0.24em; color:#D8B4FE; margin-bottom:12px;">ARCHITECTURE OF VALUE</div>
          <div style="font-size:{head_size}px; font-weight:900; line-height:1.05; letter-spacing:-0.02em; text-transform:uppercase; margin-bottom:24px;">
            BẤT ĐỘNG SẢN<br><span style="color:#245BFF;">×</span> CÔNG NGHỆ
          </div>
          <div class="concept-box">
            <div style="font-size:16px; font-weight:700; color:#FFFFFF; line-height:1.6; margin-bottom:16px;">
              Sự hội tụ giữa các khối kiến trúc bất động sản kiên cố và dòng dữ liệu công nghệ quang học, giải phóng thanh khoản và định hình cấu trúc giá trị tương lai.
            </div>
            <div class="mono" style="font-size:11px; font-weight:700; color:#94A3B8;">
              CAPITAL FLOW · DIGITAL TWIN · CROSS-BORDER M&A
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.15); padding-top:18px;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FACC15;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

def generate_post_03(w, h, ratio):
    """POST 03: REAL ESTATE THEMATIC POST"""
    pad_side = 80 if w == 1080 else 60
    head_size = 58 if h == 1920 else (52 if h == 1350 else 46)

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS_HEAD}
    <style>{COMMON_STYLE}
      body {{ width: {w}px; height: {h}px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_ascending_plate}') center/cover; filter: brightness(1.1) contrast(1.12); }}
      .shell {{ position:absolute; inset:{pad_side}px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .stat-card {{ background: rgba(10,16,38,0.75); border: 1px solid rgba(155,77,255,0.35); border-radius:12px; padding:28px; backdrop-filter:blur(20px); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:46px; width:auto;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#38BDF8;">THEMATIC PILLAR 01</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; font-weight:800; letter-spacing:0.24em; color:#D8B4FE; margin-bottom:10px;">INFRASTRUCTURE & URBAN CAPITAL</div>
          <div style="font-size:{head_size}px; font-weight:900; line-height:1.05; letter-spacing:-0.02em; text-transform:uppercase; margin-bottom:24px;">
            BẤT ĐỘNG SẢN &amp;<br>HẠ TẦNG DUYÊN HẢI
          </div>
          <div class="stat-card">
            <div style="font-size:15px; color:#CBD5E1; line-height:1.6; margin-bottom:20px;">
              Tái cấu trúc danh mục tài sản, khai mở dòng vốn đầu tư thế hệ mới và hoàn thiện pháp lý các dự án nghỉ dưỡng, công nghiệp và logistics trọng điểm Miền Trung.
            </div>
            <div style="display:flex; gap:36px; border-top:1px solid rgba(255,255,255,0.1); padding-top:16px;">
              <div><div style="font-size:24px; font-weight:900; color:#9B4DFF;">$2.5B+</div><div class="mono" style="font-size:10px; color:#94A3B8;">DÒNG VỐN DỰ KIẾN</div></div>
              <div><div style="font-size:24px; font-weight:900; color:#38BDF8;">45+</div><div class="mono" style="font-size:10px; color:#94A3B8;">TẬP ĐOÀN ĐỊA ỐC</div></div>
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.15); padding-top:18px;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FACC15;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

def generate_post_04(w, h, ratio):
    """POST 04: TECHNOLOGY THEMATIC POST"""
    pad_side = 80 if w == 1080 else 60
    head_size = 58 if h == 1920 else (52 if h == 1350 else 46)

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS_HEAD}
    <style>{COMMON_STYLE}
      body {{ width: {w}px; height: {h}px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_contours_plate}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:{pad_side}px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .stat-card {{ background: rgba(10,16,38,0.75); border: 1px solid rgba(155,77,255,0.35); border-radius:12px; padding:28px; backdrop-filter:blur(20px); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:46px; width:auto;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#38BDF8;">THEMATIC PILLAR 02</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; font-weight:800; letter-spacing:0.24em; color:#D8B4FE; margin-bottom:10px;">COMPUTATIONAL CAPITAL & PROPTECH</div>
          <div style="font-size:{head_size}px; font-weight:900; line-height:1.05; letter-spacing:-0.02em; text-transform:uppercase; margin-bottom:24px;">
            CÔNG NGHỆ AI &amp;<br>CHUYỂN ĐỔI SỐ TÀI SẢN
          </div>
          <div class="stat-card">
            <div style="font-size:15px; color:#CBD5E1; line-height:1.6; margin-bottom:20px;">
              Ứng dụng Trí tuệ nhân tạo, Digital Twin và PropTech vào chuẩn hóa dữ liệu, giải phóng thanh khoản và nâng cao tính minh bạch cho các thương vụ M&A xuyên biên giới.
            </div>
            <div style="display:flex; gap:36px; border-top:1px solid rgba(255,255,255,0.1); padding-top:16px;">
              <div><div style="font-size:24px; font-weight:900; color:#38BDF8;">300+</div><div class="mono" style="font-size:10px; color:#94A3B8;">DOANH NGHIỆP CÔNG NGHỆ</div></div>
              <div><div style="font-size:24px; font-weight:900; color:#9B4DFF;">1:1</div><div class="mono" style="font-size:10px; color:#94A3B8;">DEAL ROOM ĐẦU TƯ</div></div>
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.15); padding-top:18px;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FACC15;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

def generate_post_05(w, h, ratio):
    """POST 05: SPEAKER ANNOUNCEMENT TEMPLATE (ARCHITECTURAL PLINTH)"""
    pad_side = 80 if w == 1080 else 60
    avatar_size = 170 if h == 1920 else (150 if h == 1350 else 130)

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS_HEAD}
    <style>{COMMON_STYLE}
      body {{ width: {w}px; height: {h}px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_isometric_plate}') center/cover; filter: brightness(1.1) contrast(1.12); }}
      .shell {{ position:absolute; inset:{pad_side}px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .avatar-wrap {{ position:relative; width:{avatar_size}px; height:{avatar_size}px; margin: 0 auto -30px auto; z-index:15; }}
      .avatar-ring {{ position:absolute; inset:-5px; border-radius:50%; background:conic-gradient(from 0deg, #245BFF, #9B4DFF, #FACC15, #38BDF8, #245BFF); filter:drop-shadow(0 0 16px rgba(155,77,255,0.7)); }}
      .avatar-inner {{ position:absolute; inset:0; border-radius:50%; background:#0F172A; border:3px solid #070D20; display:flex; align-items:center; justify-content:center; overflow:hidden; }}
      .plinth-box {{ background: linear-gradient(135deg, rgba(16,26,61,0.92) 0%, rgba(9,14,33,0.96) 100%); border:1px solid rgba(155,77,255,0.5); border-radius:14px; padding:45px 36px 30px 36px; text-align:center; box-shadow:0 30px 70px rgba(0,0,0,0.85); backdrop-filter:blur(28px); position:relative; overflow:hidden; }}
      .laser-edge {{ position:absolute; top:0; left:15%; right:15%; height:2px; background:linear-gradient(90deg, transparent, #9B4DFF, #38BDF8, transparent); box-shadow:0 0 10px #9B4DFF; }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:46px; width:auto;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#FACC15;">KEYNOTE SPEAKER</div>
        </div>
        <div>
          <div class="avatar-wrap">
            <div class="avatar-ring"></div>
            <div class="avatar-inner">
              <svg viewBox="0 0 100 100" style="width:100%; height:100%;">
                <circle cx="50" cy="50" r="50" fill="#0A1628"/>
                <circle cx="50" cy="40" r="18" fill="#F8FAFC"/>
                <path d="M22 84 C22 62, 36 58, 50 58 C64 58, 78 62, 78 84 Z" fill="#2563EB"/>
              </svg>
            </div>
          </div>
          <div class="plinth-box">
            <div class="laser-edge"></div>
            <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.2em; margin-bottom:10px;">DIỄN GIẢ CHỦ TRÌ TỌA ĐÀM</div>
            <div style="font-size:32px; font-weight:900; color:#FFFFFF; text-transform:uppercase; margin-bottom:6px;">TS. TRẦN ĐÌNH THIÊN</div>
            <div style="font-size:15px; font-weight:700; color:#D8B4FE; margin-bottom:4px;">Nguyên Viện trưởng Viện Kinh tế Việt Nam</div>
            <div style="font-size:12px; color:#94A3B8; margin-bottom:18px;">Chuyên gia Cố vấn Kinh tế Vĩ mô &amp; Tái cấu trúc M&A</div>
            <div style="display:flex; justify-content:space-around; border-top:1px solid rgba(155,77,255,0.25); padding-top:14px;">
              <div><div class="mono" style="font-size:9px; color:#64748B;">MÃ VIP</div><div class="mono" style="font-size:11px; font-weight:800; color:#FFFFFF;">VMAA-2026-VIP-001</div></div>
              <div><div class="mono" style="font-size:9px; color:#64748B;">VỊ TRÍ</div><div class="mono" style="font-size:11px; font-weight:800; color:#FACC15;">ROW A · SEAT 01</div></div>
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.15); padding-top:18px;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FACC15;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

def generate_post_06(w, h, ratio):
    """POST 06: REGISTRATION & EVENT INFORMATION CTA"""
    pad_side = 80 if w == 1080 else 60
    head_size = 54 if h == 1920 else (48 if h == 1350 else 42)

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS_HEAD}
    <style>{COMMON_STYLE}
      body {{ width: {w}px; height: {h}px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_aurora_plate}') center/cover; filter: brightness(1.1) contrast(1.12); }}
      .shell {{ position:absolute; inset:{pad_side}px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .reg-card {{ background: rgba(10,16,38,0.8); border: 1px solid rgba(155,77,255,0.45); border-radius:14px; padding:32px; backdrop-filter:blur(24px); box-shadow:0 24px 60px rgba(0,0,0,0.7); }}
      .btn-cta {{ display:inline-block; background:linear-gradient(135deg, #245BFF 0%, #9B4DFF 100%); color:#FFFFFF; font-family:'Manrope',sans-serif; font-weight:800; font-size:13px; letter-spacing:0.16em; text-transform:uppercase; padding:14px 28px; border-radius:6px; border:1px solid rgba(255,255,255,0.3); box-shadow:0 6px 25px rgba(155,77,255,0.5); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:46px; width:auto;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#38BDF8;">REGISTRATION PORTAL</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; font-weight:800; letter-spacing:0.24em; color:#D8B4FE; margin-bottom:10px;">XÁC NHẬN THAM DỰ &amp; ĐĂNG KÝ VÉ VIP</div>
          <div style="font-size:{head_size}px; font-weight:900; line-height:1.05; letter-spacing:-0.02em; text-transform:uppercase; margin-bottom:24px;">
            HỘI TỤ ĐỈNH CAO<br>M&amp;A MIỀN TRUNG
          </div>
          <div class="reg-card">
            <div style="display:grid; grid-template-columns:1fr auto; gap:24px; align-items:center;">
              <div>
                <div style="font-size:14px; color:#E2E8F0; line-height:1.6; margin-bottom:16px;">
                  Cổng đăng ký chính thức dành cho Lãnh đạo Tập đoàn, Quỹ đầu tư và Đại biểu danh dự.
                </div>
                <div style="font-size:12px; color:#94A3B8; margin-bottom:18px;">
                  📍 Ariyana Convention Centre (Furama Resort), Đà Nẵng<br>
                  📞 Hotline BTC: (+84) 905 123 456 · Email: vip@vmaa.vn
                </div>
                <div class="btn-cta">ĐĂNG KÝ THAM DỰ // VIP PASS</div>
              </div>
              <div style="background:#FFFFFF; padding:10px; border-radius:8px; display:flex; flex-direction:column; align-items:center;">
                <!-- Clean Vector QR Code Simulation -->
                <svg width="100" height="100" viewBox="0 0 100 100" fill="#070D20">
                  <rect x="5" y="5" width="25" height="25" fill="#070D20"/>
                  <rect x="10" y="10" width="15" height="15" fill="#FFFFFF"/>
                  <rect x="13" y="13" width="9" height="9" fill="#070D20"/>
                  <rect x="70" y="5" width="25" height="25" fill="#070D20"/>
                  <rect x="75" y="10" width="15" height="15" fill="#FFFFFF"/>
                  <rect x="78" y="13" width="9" height="9" fill="#070D20"/>
                  <rect x="5" y="70" width="25" height="25" fill="#070D20"/>
                  <rect x="10" y="75" width="15" height="15" fill="#FFFFFF"/>
                  <rect x="13" y="78" width="9" height="9" fill="#070D20"/>
                  <rect x="40" y="10" width="15" height="10"/>
                  <rect x="45" y="30" width="10" height="20"/>
                  <rect x="35" y="60" width="20" height="15"/>
                  <rect x="65" y="45" width="25" height="15"/>
                  <rect x="65" y="75" width="15" height="15"/>
                </svg>
                <div class="mono" style="font-size:9px; font-weight:800; color:#070D20; margin-top:4px;">SCAN FOR VIP</div>
              </div>
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.15); padding-top:18px;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FACC15;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

GENERATORS = [
    ("POST_01_Announcement", generate_post_01, "Official Event Announcement: Establishing core institutional identity, 1,500+ scale, and luxury authority."),
    ("POST_02_CentralConcept", generate_post_02, "Central Concept: Convergence of physical real estate volumes and luminous tech data structures."),
    ("POST_03_RealEstate", generate_post_03, "Thematic Pillar 01: Real Estate & Urban Infrastructure restructuring along the Central Vietnam coast."),
    ("POST_04_Technology", generate_post_04, "Thematic Pillar 02: Computational capital, PropTech, and AI automated cross-border valuation models."),
    ("POST_05_SpeakerSpotlight", generate_post_05, "Keynote Speaker Announcement: Architectural lower-third plinth with TS. Trần Đình Thiên spotlight."),
    ("POST_06_RegistrationCTA", generate_post_06, "Registration & VIP Information CTA: Direct actionable funnel with verified venue and scan QR code.")
]

RATIOS = [
    ("1080x1350", 1080, 1350, "Portrait Feed (4:5)", DIR_1350),
    ("1080x1920", 1080, 1920, "Story / Reels / Totem (9:16)", DIR_1920),
    ("1080x1080", 1080, 1080, "Square Feed (1:1)", DIR_1080)
]

print("Starting deterministic rendering of 18 social media post variants across 3 ratios...")

manifest = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for slug, gen_func, rationale in GENERATORS:
        post_item = {"slug": slug, "rationale": rationale, "variants": []}
        for ratio_key, w, h, ratio_name, out_dir in RATIOS:
            html_content = gen_func(w, h, ratio_key)
            html_file = out_dir / f"{slug}_{ratio_key}.html"
            png_file = out_dir / f"{slug}_{ratio_key}.png"

            html_file.write_text(html_content, encoding="utf-8")

            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            page.set_content(html_content)
            page.wait_for_timeout(400) # Wait for fonts to paint cleanly
            page.screenshot(path=str(png_file))
            page.close()

            # Copy to brain artifacts
            shutil.copy(png_file, BRAIN_DIR / png_file.name)

            post_item["variants"].append({
                "ratio": ratio_key,
                "label": ratio_name,
                "width": w,
                "height": h,
                "png": png_file.name,
                "rel_path": f"{ratio_key}/{png_file.name}",
                "html_path": f"{ratio_key}/{html_file.name}"
            })
            print(f"Rendered: {png_file.name} ({w}x{h})")

        manifest.append(post_item)

    browser.close()

# Generate Interactive Preview Contact Sheet (index.html)
gallery_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>VMAA M&A Miền Trung 2026 | 18 Social Media Post Deliverables Gallery</title>
  {FONTS_HEAD}
  <style>
    * {{ box-sizing: border-box; margin:0; padding:0; }}
    body {{ background: #070D20; color: #FFFFFF; font-family: 'Be Vietnam Pro', sans-serif; padding: 48px; }}
    header {{ margin-bottom: 40px; border-bottom: 1px solid rgba(155,77,255,0.3); padding-bottom: 24px; display:flex; justify-content:space-between; align-items:flex-end; }}
    h1 {{ font-size: 32px; font-weight: 900; letter-spacing: -0.02em; }}
    .subtitle {{ font-family: 'Manrope', sans-serif; font-size: 13px; color: #38BDF8; letter-spacing: 0.16em; text-transform: uppercase; margin-top: 6px; }}
    .filter-bar {{ display: flex; gap: 12px; margin-bottom: 32px; }}
    .filter-btn {{ padding: 10px 20px; border-radius: 6px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.15); color: #FFFFFF; font-family: 'Manrope', sans-serif; font-size: 12px; font-weight: 700; cursor: pointer; transition: all 0.2s; }}
    .filter-btn.active {{ background: #245BFF; border-color: #38BDF8; box-shadow: 0 0 15px rgba(36,91,255,0.6); }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 32px; }}
    .card {{ background: rgba(10,16,38,0.7); border: 1px solid rgba(155,77,255,0.3); border-radius: 12px; overflow: hidden; backdrop-filter: blur(16px); display:flex; flex-direction:column; transition: transform 0.3s; }}
    .card:hover {{ transform: translateY(-4px); border-color: #9B4DFF; }}
    .card-preview {{ width: 100%; height: 380px; background: #050814; display: flex; align-items: center; justify-content: center; overflow: hidden; padding: 12px; }}
    .card-preview img {{ max-width: 100%; max-height: 100%; object-fit: contain; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.8); }}
    .card-info {{ padding: 20px; display: flex; flex-direction: column; gap: 8px; flex-grow: 1; }}
    .card-tag {{ font-family: 'Manrope', sans-serif; font-size: 10px; font-weight: 800; color: #FACC15; letter-spacing: 0.18em; text-transform: uppercase; }}
    .card-title {{ font-size: 16px; font-weight: 800; }}
    .card-rationale {{ font-size: 12px; color: #94A3B8; line-height: 1.5; }}
    .card-meta {{ font-family: 'Manrope', sans-serif; font-size: 11px; color: #38BDF8; font-weight: 700; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px; margin-top: auto; display:flex; justify-content:space-between; }}
  </style>
</head>
<body>
  <header>
    <div>
      <div class="subtitle">Deliverable A · Complete 18-Variant Contact Sheet</div>
      <h1>Diễn đàn M&A Miền Trung 2026 — Social Media Identity Suite</h1>
    </div>
    <div style="font-family:'Manrope',sans-serif; font-size:12px; color:#D8B4FE;">
      6 Concepts × 3 Aspect Ratios = 18 Deterministic Production Exports
    </div>
  </header>

  <div class="filter-bar">
    <button class="filter-btn active" onclick="filterRatio('all')">Show All (18)</button>
    <button class="filter-btn" onclick="filterRatio('1080x1350')">Portrait Feed 4:5 (6)</button>
    <button class="filter-btn" onclick="filterRatio('1080x1920')">Story / Reels 9:16 (6)</button>
    <button class="filter-btn" onclick="filterRatio('1080x1080')">Square Feed 1:1 (6)</button>
  </div>

  <div class="grid" id="gallery-grid">
"""

for item in manifest:
    for v in item["variants"]:
        gallery_html += f"""
    <div class="card" data-ratio="{v['ratio']}">
      <div class="card-preview">
        <a href="{v['rel_path']}" target="_blank">
          <img src="{v['rel_path']}" alt="{item['slug']}">
        </a>
      </div>
      <div class="card-info">
        <div class="card-tag">{v['label']}</div>
        <div class="card-title">{item['slug'].replace('_', ' ')}</div>
        <div class="card-rationale">{item['rationale']}</div>
        <div class="card-meta">
          <span>{v['width']} × {v['height']} px</span>
          <a href="{v['html_path']}" target="_blank" style="color:#D8B4FE; text-decoration:none;">Inspect Source &rarr;</a>
        </div>
      </div>
    </div>
"""

gallery_html += """
  </div>

  <script>
    function filterRatio(r) {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      event.target.classList.add('active');
      document.querySelectorAll('.card').forEach(c => {
        if (r === 'all' || c.getAttribute('data-ratio') === r) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

index_file = EXPORT_BASE / "index.html"
index_file.write_text(gallery_html, encoding="utf-8")
shutil.copy(index_file, BRAIN_DIR / "social_media_18_contact_sheet.html")

print("Generated interactive contact sheet: exports/social_media/index.html")
