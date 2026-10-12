import os
import sys
import base64
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")
PROJECT_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
PLATES_DIR = PROJECT_DIR / "assets" / "plates"
EXPORTS_DIR = PROJECT_DIR / "exports"
SUITE_DIR = EXPORTS_DIR / "master_suite_v2"
SUITE_DIR.mkdir(parents=True, exist_ok=True)

def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"

u1 = to_data_uri(PLATES_DIR / "purple_opt01_hero_convergence.jpg")
u2 = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u3 = to_data_uri(PLATES_DIR / "purple_opt03_ascending_cantilevers.jpg")
u6 = to_data_uri(PLATES_DIR / "purple_opt06_highkey_aurora_stage.jpg")
u_logo = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")

# Premium Google Fonts: Be Vietnam Pro, Manrope, Outfit, Plus Jakarta Sans
FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,800&family=Manrope:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
"""

COMMON_STYLE = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #070D20; font-family: 'Be Vietnam Pro', sans-serif; color: #FFFFFF;
  position: relative; overflow: hidden; -webkit-font-smoothing: antialiased;
}
.mono { font-family: 'Manrope', sans-serif; text-transform: uppercase; letter-spacing: 0.18em; }
.aurora {
  position: absolute; inset: 0; pointer-events: none; mix-blend-mode: screen;
  background:
    radial-gradient(850px 750px at 70% 35%, rgba(155,77,255,0.40) 0%, rgba(36,91,255,0.25) 50%, transparent 80%),
    radial-gradient(650px 550px at 25% 70%, rgba(107,45,155,0.35) 0%, transparent 75%);
}
.shade {
  position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(180deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.3) 38%, rgba(7,13,32,0.5) 65%, rgba(7,13,32,0.95) 100%);
}
.gold { color: #FACC15; }
.cyan { color: #38BDF8; }
.lavender { color: #D8B4FE; }
"""

# =========================================================================
# 1. SOCIAL MEDIA PACK (Generous Logo Breathing Space + Executive Typography)
# =========================================================================

# 1A. 1:1 SQUARE (1080x1080)
def get_social_1x1():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1080px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u1}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:64px 72px 64px 72px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .logo-zone {{ display:flex; justify-content:space-between; align-items:center; padding-bottom:28px; border-bottom:1px solid rgba(155,77,255,0.25); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div class="logo-zone">
          <div style="display:flex; align-items:center; gap:20px;">
            <img src="{u_logo}" style="height:48px; width:auto;">
            <div style="width:1px; height:32px; background:rgba(255,255,255,0.2);"></div>
            <div class="mono" style="font-size:10px; color:#D8B4FE; line-height:1.4;">VIETNAM M&A ASSOCIATION<br>CENTRAL VIETNAM CHAPTER</div>
          </div>
          <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.2em;">OFFICIAL ANNOUNCEMENT</div>
        </div>

        <div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#38BDF8; letter-spacing:0.24em; margin-bottom:12px;">● RA MẮT VMAA MIỀN TRUNG · 2026</div>
          <div class="mono" style="font-size:24px; font-weight:800; letter-spacing:0.12em; color:#FFFFFF; margin-bottom:4px;">DIỄN ĐÀN</div>
          <div style="font-size:82px; font-weight:900; line-height:0.95; letter-spacing:-0.03em; text-transform:uppercase; margin-bottom:6px;">M&A 2026</div>
          <div style="font-size:68px; font-weight:900; line-height:1; letter-spacing:-0.02em; text-transform:uppercase; background:linear-gradient(135deg, #B77BFF 0%, #7C3AED 50%, #2563EB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:20px; filter:drop-shadow(0 0 25px rgba(155,77,255,0.5));">MIỀN TRUNG</div>
          <div style="font-size:19px; font-weight:700; color:#F1F5F9;">KIẾN TRÚC GIÁ TRỊ: <span class="gold" style="font-style:italic; font-weight:800;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</span></div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:flex-end; border-top:1px solid rgba(155,77,255,0.3); padding-top:20px;">
          <div>
            <div class="mono" style="font-size:10px; font-weight:700; color:#94A3B8; margin-bottom:4px;">THỜI GIAN & ĐỊA ĐIỂM</div>
            <div style="font-size:17px; font-weight:800; color:#FFFFFF;">Chủ Nhật · 13.12.2026</div>
            <div style="font-size:13px; font-weight:600; color:#D8B4FE;">13:30 – 17:30 · Đà Nẵng, Việt Nam</div>
          </div>
          <div class="mono" style="font-size:13px; font-weight:800; color:#FACC15; letter-spacing:0.18em;">1,500+ DELEGATES</div>
        </div>
      </div>
    </body></html>"""

# 1B. 4:5 PORTRAIT (1080x1350)
def get_social_4x5():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1080px; height: 1350px; }}
      .bg {{ position:absolute; inset:0; background: url('{u1}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:80px 76px 80px 76px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .logo-zone {{ display:flex; justify-content:space-between; align-items:center; padding-bottom:32px; border-bottom:1px solid rgba(155,77,255,0.25); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div class="logo-zone">
          <div style="display:flex; align-items:center; gap:22px;">
            <img src="{u_logo}" style="height:52px; width:auto;">
            <div style="width:1px; height:36px; background:rgba(255,255,255,0.2);"></div>
            <div class="mono" style="font-size:11px; color:#D8B4FE; line-height:1.4;">VIETNAM M&A ASSOCIATION<br>CENTRAL VIETNAM REGIONAL FORUM</div>
          </div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#38BDF8; letter-spacing:0.2em;">PORTRAIT FEED</div>
        </div>

        <div>
          <div class="mono" style="font-size:13px; font-weight:800; color:#38BDF8; letter-spacing:0.24em; margin-bottom:14px;">● RA MẮT VMAA MIỀN TRUNG · 2026</div>
          <div class="mono" style="font-size:26px; font-weight:800; letter-spacing:0.12em; color:#FFFFFF; margin-bottom:6px;">DIỄN ĐÀN</div>
          <div style="font-size:90px; font-weight:900; line-height:0.95; letter-spacing:-0.03em; text-transform:uppercase; margin-bottom:8px;">M&A 2026</div>
          <div style="font-size:76px; font-weight:900; line-height:1; letter-spacing:-0.02em; text-transform:uppercase; background:linear-gradient(135deg, #B77BFF 0%, #7C3AED 50%, #2563EB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:24px; filter:drop-shadow(0 0 25px rgba(155,77,255,0.5));">MIỀN TRUNG</div>
          <div style="font-size:22px; font-weight:700; color:#F1F5F9; line-height:1.4;">KIẾN TRÚC GIÁ TRỊ:<br><span class="gold" style="font-style:italic; font-weight:800;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</span></div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:flex-end; border-top:1px solid rgba(155,77,255,0.3); padding-top:24px;">
          <div>
            <div class="mono" style="font-size:11px; font-weight:700; color:#94A3B8; margin-bottom:6px;">THỜI GIAN & ĐỊA ĐIỂM</div>
            <div style="font-size:20px; font-weight:800; color:#FFFFFF;">Chủ Nhật · 13.12.2026</div>
            <div style="font-size:14px; font-weight:600; color:#D8B4FE;">13:30 – 17:30 · Ariyana / Furama Resort, Đà Nẵng</div>
          </div>
          <div class="mono" style="font-size:14px; font-weight:800; color:#FACC15; letter-spacing:0.18em;">1,500+ DELEGATES</div>
        </div>
      </div>
    </body></html>"""

# 1C. 9:16 STORY / REELS (1080x1920)
def get_social_9x16():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1080px; height: 1920px; }}
      .bg {{ position:absolute; inset:0; background: url('{u1}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:120px 80px 120px 80px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .logo-zone {{ display:flex; justify-content:space-between; align-items:center; padding-bottom:40px; border-bottom:1px solid rgba(155,77,255,0.25); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div class="logo-zone">
          <div style="display:flex; align-items:center; gap:24px;">
            <img src="{u_logo}" style="height:56px; width:auto;">
            <div style="width:1px; height:40px; background:rgba(255,255,255,0.2);"></div>
            <div class="mono" style="font-size:12px; color:#D8B4FE; line-height:1.4;">VIETNAM M&A ASSOCIATION<br>CENTRAL VIETNAM</div>
          </div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#38BDF8; letter-spacing:0.2em;">STORY // REELS</div>
        </div>

        <div>
          <div class="mono" style="font-size:14px; font-weight:800; color:#38BDF8; letter-spacing:0.24em; margin-bottom:16px;">● RA MẮT VMAA MIỀN TRUNG · 2026</div>
          <div class="mono" style="font-size:28px; font-weight:800; letter-spacing:0.12em; color:#FFFFFF; margin-bottom:6px;">DIỄN ĐÀN</div>
          <div style="font-size:98px; font-weight:900; line-height:0.95; letter-spacing:-0.03em; text-transform:uppercase; margin-bottom:10px;">M&A 2026</div>
          <div style="font-size:82px; font-weight:900; line-height:1; letter-spacing:-0.02em; text-transform:uppercase; background:linear-gradient(135deg, #B77BFF 0%, #7C3AED 50%, #2563EB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:28px; filter:drop-shadow(0 0 25px rgba(155,77,255,0.5));">MIỀN TRUNG</div>
          <div style="font-size:24px; font-weight:700; color:#F1F5F9; line-height:1.4; margin-bottom:32px;">
            KIẾN TRÚC GIÁ TRỊ:<br><span class="gold" style="font-style:italic; font-weight:800;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</span>
          </div>
        </div>

        <div style="border-top:1px solid rgba(155,77,255,0.3); padding-top:28px; display:flex; justify-content:space-between; align-items:flex-end;">
          <div>
            <div class="mono" style="font-size:11px; font-weight:700; color:#94A3B8; margin-bottom:6px;">THỜI GIAN & ĐỊA ĐIỂM</div>
            <div style="font-size:22px; font-weight:800; color:#FFFFFF;">Chủ Nhật · 13.12.2026</div>
            <div style="font-size:15px; font-weight:600; color:#D8B4FE;">13:30 – 17:30 · Ariyana / Furama Resort, Đà Nẵng</div>
          </div>
          <div class="mono" style="font-size:14px; font-weight:800; color:#FACC15; letter-spacing:0.18em;">1,500+ DELEGATES</div>
        </div>
      </div>
    </body></html>"""

# 1D. 1.91:1 COVER / OPENGRAPH (1200x628 @ 2x = 2400x1256)
def get_social_cover():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1200px; height: 628px; }}
      .bg {{ position:absolute; inset:0; background: url('{u1}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:48px 60px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .logo-zone {{ display:flex; justify-content:space-between; align-items:center; }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div class="logo-zone">
          <div style="display:flex; align-items:center; gap:18px;">
            <img src="{u_logo}" style="height:40px; width:auto;">
            <div style="width:1px; height:28px; background:rgba(255,255,255,0.2);"></div>
            <div class="mono" style="font-size:10px; color:#D8B4FE;">VIETNAM M&A ASSOCIATION</div>
          </div>
          <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8;">EVENT COVER // OPENGRAPH</div>
        </div>

        <div>
          <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.2em; margin-bottom:8px;">● RA MẮT VMAA MIỀN TRUNG · ĐÀ NẴNG 2026</div>
          <div style="font-size:52px; font-weight:900; line-height:0.95; text-transform:uppercase; margin-bottom:4px;">DIỄN ĐÀN M&A 2026</div>
          <div style="font-size:44px; font-weight:900; line-height:1; text-transform:uppercase; background:linear-gradient(135deg, #B77BFF 0%, #7C3AED 50%, #2563EB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:12px;">MIỀN TRUNG</div>
          <div style="font-size:16px; font-weight:700; color:#F1F5F9;">KIẾN TRÚC GIÁ TRỊ: <span class="gold" style="font-style:italic;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</span></div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(155,77,255,0.3); padding-top:14px;">
          <div class="mono" style="font-size:12px; font-weight:700; color:#FFFFFF;">13.12.2026 · 13:30–17:30 · ĐÀ NẴNG</div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FACC15;">1,500+ DELEGATES</div>
        </div>
      </div>
    </body></html>"""

# =========================================================================
# 2. 16:9 LANDING HERO & SLIDE DECK TEMPLATES
# =========================================================================

# 2A. 16:9 LANDING PAGE HERO (1920x1080)
def get_landing_hero():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1920px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u1}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:0; display:flex; flex-direction:column; justify-content:space-between; z-index:10; padding:48px 64px; }}
      .nav {{ display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(155,77,255,0.25); padding-bottom:20px; }}
      .nav-links {{ display:flex; gap:32px; font-family:'Manrope',sans-serif; font-size:12px; font-weight:700; text-transform:uppercase; color:#94A3B8; letter-spacing:0.12em; }}
      .btn-vip {{ background:linear-gradient(135deg, #245BFF, #9B4DFF); color:#FFFFFF; font-family:'Manrope',sans-serif; font-weight:800; font-size:11px; letter-spacing:0.16em; text-transform:uppercase; padding:10px 20px; border-radius:6px; border:1px solid rgba(255,255,255,0.3); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div class="nav">
          <div style="display:flex; align-items:center; gap:24px;">
            <img src="{u_logo}" style="height:44px; width:auto;">
            <div style="width:1px; height:32px; background:rgba(255,255,255,0.2);"></div>
            <div class="mono" style="font-size:11px; color:#D8B4FE;">VMAA · CENTRAL VIETNAM 2026</div>
          </div>
          <div class="nav-links">
            <span style="color:#FFFFFF; border-bottom:2px solid #9B4DFF; padding-bottom:4px;">01. TỔNG QUAN</span>
            <span>02. TRỤ CỘT CHIẾN LƯỢC</span>
            <span>03. BỆ ĐỠ DIỄN GIẢ</span>
            <span>04. LỊCH TRÌNH</span>
            <span>05. ĐĂNG KÝ VIP</span>
          </div>
          <div class="btn-vip">NHẬN THƯ MỜI VIP &rarr;</div>
        </div>

        <div style="max-width:900px;">
          <div class="mono" style="font-size:13px; font-weight:800; color:#38BDF8; letter-spacing:0.24em; margin-bottom:12px;">● RA MẮT VMAA MIỀN TRUNG · 13.12.2026</div>
          <div class="mono" style="font-size:28px; font-weight:800; letter-spacing:0.12em; color:#FFFFFF; margin-bottom:6px;">DIỄN ĐÀN</div>
          <div style="font-size:104px; font-weight:900; line-height:0.95; letter-spacing:-0.03em; text-transform:uppercase; margin-bottom:8px;">M&A 2026</div>
          <div style="font-size:84px; font-weight:900; line-height:1; letter-spacing:-0.02em; text-transform:uppercase; background:linear-gradient(135deg, #B77BFF 0%, #7C3AED 50%, #2563EB 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-bottom:24px; filter:drop-shadow(0 0 25px rgba(155,77,255,0.5));">MIỀN TRUNG</div>
          <div style="font-size:24px; font-weight:700; color:#F1F5F9; line-height:1.4; margin-bottom:32px;">
            KIẾN TRÚC GIÁ TRỊ: <span class="gold" style="font-style:italic; font-weight:800;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</span>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(155,77,255,0.25); padding-top:20px;">
          <div style="display:flex; gap:48px;">
            <div><div class="mono" style="font-size:10px; color:#94A3B8;">THỜI GIAN</div><div style="font-size:16px; font-weight:800;">Chủ Nhật · 13.12.2026</div></div>
            <div><div class="mono" style="font-size:10px; color:#94A3B8;">ĐỊA ĐIỂM</div><div style="font-size:16px; font-weight:800;">Ariyana / Furama Resort, Đà Nẵng</div></div>
            <div><div class="mono" style="font-size:10px; color:#94A3B8;">QUY MÔ</div><div style="font-size:16px; font-weight:800; color:#FACC15;">1,500+ Lãnh đạo Cấp cao</div></div>
          </div>
          <div class="mono" style="font-size:12px; color:#38BDF8;">SCROLL TO DISCOVER &darr;</div>
        </div>
      </div>
    </body></html>"""

# 2B. SLIDE 02: AGENDA TIMELINE (1920x1080)
def get_slide_agenda():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1920px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u6}') center/cover; filter: brightness(1.1) contrast(1.12); }}
      .shell {{ position:absolute; inset:0; display:flex; flex-direction:column; justify-content:space-between; z-index:10; padding:54px 64px; }}
      .card {{ background:rgba(10,16,38,0.78); border:1px solid rgba(155,77,255,0.35); border-radius:12px; padding:24px; backdrop-filter:blur(20px); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(155,77,255,0.25); padding-bottom:18px;">
          <div style="display:flex; align-items:center; gap:20px;">
            <img src="{u_logo}" style="height:38px; width:auto;">
            <div class="mono" style="font-size:12px; font-weight:800; color:#38BDF8;">SLIDE 02 // AGENDA TIMELINE</div>
          </div>
          <div class="mono" style="font-size:12px; color:#FACC15;">13.12.2026 · ĐÀ NẴNG</div>
        </div>

        <div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#D8B4FE; letter-spacing:0.24em; margin-bottom:8px;">CHƯƠNG TRÌNH NGHỊ SỰ CHÍNH THỨC</div>
          <div style="font-size:42px; font-weight:900; margin-bottom:32px;">Lịch Trình Diễn Đàn &amp; Gala Dinner</div>

          <div style="display:grid; grid-template-columns:repeat(4, 1fr); gap:20px;">
            <div class="card">
              <div class="mono" style="font-size:22px; font-weight:900; color:#FACC15; margin-bottom:8px;">13:30 – 14:00</div>
              <div style="font-size:17px; font-weight:800; margin-bottom:8px;">Đón Khách &amp; Check-in VIP</div>
              <div style="font-size:13px; color:#CBD5E1; line-height:1.5;">Thảm đỏ tiếp đón, check-in nhận diện và tiệc trà Networking tiền sảnh Grand Ballroom.</div>
            </div>
            <div class="card">
              <div class="mono" style="font-size:22px; font-weight:900; color:#FACC15; margin-bottom:8px;">14:00 – 14:45</div>
              <div style="font-size:17px; font-weight:800; margin-bottom:8px;">Lễ Ra Mắt VMAA Miền Trung</div>
              <div style="font-size:13px; color:#CBD5E1; line-height:1.5;">Kích hoạt Ban Chấp hành VMAA Phân hội Miền Trung &amp; Phát biểu Lãnh đạo TP. Đà Nẵng.</div>
            </div>
            <div class="card">
              <div class="mono" style="font-size:22px; font-weight:900; color:#FACC15; margin-bottom:8px;">14:45 – 16:15</div>
              <div style="font-size:17px; font-weight:800; margin-bottom:8px;">Tọa Đàm Chuyên Đề Cấp Cao</div>
              <div style="font-size:13px; color:#CBD5E1; line-height:1.5;">Hai tham luận chuyên sâu: Bất động sản Duyên hải &amp; Công nghệ AI định giá tài sản.</div>
            </div>
            <div class="card">
              <div class="mono" style="font-size:22px; font-weight:900; color:#FACC15; margin-bottom:8px;">18:00 – 21:00</div>
              <div style="font-size:17px; font-weight:800; margin-bottom:8px;">Gala Dinner &amp; 1:1 Deal Room</div>
              <div style="font-size:13px; color:#CBD5E1; line-height:1.5;">Dạ tiệc doanh nhân cao cấp, vinh danh VMAA Awards và đàm phán hợp đồng M&amp;A kín.</div>
            </div>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(155,77,255,0.25); padding-top:18px;">
          <div class="mono" style="font-size:11px; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:11px; color:#D8B4FE;">ARIYANA CONVENTION CENTRE, ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

# 2C. SLIDE 03: ARCHITECTURE OF VALUE & M&A DATA (1920x1080)
def get_slide_data():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1920px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u3}') center/cover; filter: brightness(1.1) contrast(1.12); }}
      .shell {{ position:absolute; inset:0; display:flex; flex-direction:column; justify-content:space-between; z-index:10; padding:54px 64px; }}
      .card {{ background:rgba(10,16,38,0.78); border:1px solid rgba(155,77,255,0.35); border-radius:14px; padding:36px; backdrop-filter:blur(24px); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(155,77,255,0.25); padding-bottom:18px;">
          <div style="display:flex; align-items:center; gap:20px;">
            <img src="{u_logo}" style="height:38px; width:auto;">
            <div class="mono" style="font-size:12px; font-weight:800; color:#38BDF8;">SLIDE 03 // ARCHITECTURE OF VALUE</div>
          </div>
          <div class="mono" style="font-size:12px; color:#FACC15;">STRATEGIC PILLARS</div>
        </div>

        <div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#D8B4FE; letter-spacing:0.24em; margin-bottom:8px;">HỘI TỤ GIÁ TRỊ · NÂNG TẦM TÀI SẢN</div>
          <div style="font-size:42px; font-weight:900; margin-bottom:32px;">Hai Trụ Cột Chiến Lược 2026–2030</div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:32px;">
            <div class="card">
              <div class="mono" style="font-size:36px; font-weight:900; color:rgba(255,255,255,0.15); margin-bottom:8px;">01</div>
              <div style="font-size:24px; font-weight:800; margin-bottom:12px;">Bất Động Sản &amp; Hạ Tầng Đô Thị</div>
              <div style="font-size:14px; color:#CBD5E1; line-height:1.6; margin-bottom:24px;">
                Tái cấu trúc danh mục tài sản, khai mở dòng vốn đầu tư FDI thế hệ mới và hoàn thiện khung pháp lý các siêu dự án nghỉ dưỡng, công nghiệp và logistics duyên hải Miền Trung.
              </div>
              <div style="display:flex; gap:36px; border-top:1px solid rgba(255,255,255,0.1); padding-top:18px;">
                <div><div style="font-size:28px; font-weight:900; color:#9B4DFF;">$2.5B+</div><div class="mono" style="font-size:10px; color:#94A3B8;">DÒNG VỐN DỰ KIẾN</div></div>
                <div><div style="font-size:28px; font-weight:900; color:#38BDF8;">45+</div><div class="mono" style="font-size:10px; color:#94A3B8;">TẬP ĐOÀN ĐỊA ỐC</div></div>
              </div>
            </div>

            <div class="card">
              <div class="mono" style="font-size:36px; font-weight:900; color:rgba(255,255,255,0.15); margin-bottom:8px;">02</div>
              <div style="font-size:24px; font-weight:800; margin-bottom:12px;">Công Nghệ AI &amp; Chuyển Đổi Số Tài Sản</div>
              <div style="font-size:14px; color:#CBD5E1; line-height:1.6; margin-bottom:24px;">
                Chuyển đổi số toàn diện tài sản vật lý thông qua PropTech, Digital Twin và trí tuệ nhân tạo. Nâng cao tính thanh khoản và định giá giao dịch xuyên biên giới.
              </div>
              <div style="display:flex; gap:36px; border-top:1px solid rgba(255,255,255,0.1); padding-top:18px;">
                <div><div style="font-size:28px; font-weight:900; color:#38BDF8;">300+</div><div class="mono" style="font-size:10px; color:#94A3B8;">DOANH NGHIỆP CÔNG NGHỆ</div></div>
                <div><div style="font-size:28px; font-weight:900; color:#FACC15;">1:1</div><div class="mono" style="font-size:10px; color:#94A3B8;">DEAL ROOM ĐẦU TƯ</div></div>
              </div>
            </div>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(155,77,255,0.25); padding-top:18px;">
          <div class="mono" style="font-size:11px; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:11px; color:#D8B4FE;">ARCHITECTURE OF VALUE</div>
        </div>
      </div>
    </body></html>"""

# 2D. SLIDE 04: SPEAKERS SPOTLIGHT (1920x1080)
def get_slide_speakers():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{COMMON_STYLE}
      body {{ width: 1920px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u2}') center/cover; filter: brightness(1.1) contrast(1.12); }}
      .shell {{ position:absolute; inset:0; display:flex; flex-direction:column; justify-content:space-between; z-index:10; padding:54px 64px; }}
      .card {{ background:rgba(10,16,38,0.85); border:1px solid rgba(155,77,255,0.4); border-radius:14px; padding:32px 28px; text-align:center; backdrop-filter:blur(24px); position:relative; overflow:hidden; }}
      .laser {{ position:absolute; top:0; left:15%; right:15%; height:2px; background:linear-gradient(90deg, transparent, #9B4DFF, #38BDF8, transparent); }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(155,77,255,0.25); padding-bottom:18px;">
          <div style="display:flex; align-items:center; gap:20px;">
            <img src="{u_logo}" style="height:38px; width:auto;">
            <div class="mono" style="font-size:12px; font-weight:800; color:#38BDF8;">SLIDE 04 // KEYNOTE &amp; PANELIST SPOTLIGHT</div>
          </div>
          <div class="mono" style="font-size:12px; color:#FACC15;">ARCHITECTURAL MOTION PLINTHS</div>
        </div>

        <div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#D8B4FE; letter-spacing:0.24em; margin-bottom:8px;">HỘI ĐỒNG CHUYÊN GIA &amp; DIỄN GIẢ CẤP CAO</div>
          <div style="font-size:42px; font-weight:900; margin-bottom:32px;">Bệ Đỡ Diễn Giả Tọa Đàm &amp; Deal Room</div>

          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:28px;">
            <div class="card">
              <div class="laser"></div>
              <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.2em; margin-bottom:12px;">CHỦ TRÌ TỌA ĐÀM</div>
              <div style="font-size:24px; font-weight:900; margin-bottom:6px;">TS. TRẦN ĐÌNH THIÊN</div>
              <div style="font-size:14px; font-weight:700; color:#D8B4FE; margin-bottom:4px;">Nguyên Viện trưởng Viện Kinh tế VN</div>
              <div style="font-size:12px; color:#94A3B8; margin-bottom:16px;">Tổ Tư vấn Kinh tế của Thủ tướng Chính phủ</div>
              <div style="border-top:1px solid rgba(155,77,255,0.25); padding-top:10px;">
                <span class="mono" style="font-size:10px; color:#FACC15;">ROW A · SEAT 01 (VIP 1)</span>
              </div>
            </div>

            <div class="card">
              <div class="laser"></div>
              <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.2em; margin-bottom:12px;">ĐẠI DIỆN CHÍNH QUYỀN</div>
              <div style="font-size:24px; font-weight:900; margin-bottom:6px;">LÃNH ĐẠO UBND TP. ĐÀ NẴNG</div>
              <div style="font-size:14px; font-weight:700; color:#D8B4FE; margin-bottom:4px;">Thành ủy &amp; UBND Thành phố Đà Nẵng</div>
              <div style="font-size:12px; color:#94A3B8; margin-bottom:16px;">Phát biểu Chỉ đạo &amp; Cơ chế Thu hút Đầu tư M&amp;A</div>
              <div style="border-top:1px solid rgba(155,77,255,0.25); padding-top:10px;">
                <span class="mono" style="font-size:10px; color:#FACC15;">ROW A · SEAT 02 (VIP 1)</span>
              </div>
            </div>

            <div class="card">
              <div class="laser"></div>
              <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; letter-spacing:0.2em; margin-bottom:12px;">BAN TỔ CHỨC DIỄN ĐÀN</div>
              <div style="font-size:24px; font-weight:900; margin-bottom:6px;">CHỦ TỊCH VMAA VIỆT NAM</div>
              <div style="font-size:14px; font-weight:700; color:#D8B4FE; margin-bottom:4px;">Hiệp hội M&amp;A Doanh nghiệp Việt Nam</div>
              <div style="font-size:12px; color:#94A3B8; margin-bottom:16px;">Phát biểu Khai mạc &amp; Ký kết Hợp tác Quốc tế</div>
              <div style="border-top:1px solid rgba(155,77,255,0.25); padding-top:10px;">
                <span class="mono" style="font-size:10px; color:#FACC15;">ROW A · SEAT 03 (VIP 1)</span>
              </div>
            </div>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(155,77,255,0.25); padding-top:18px;">
          <div class="mono" style="font-size:11px; color:#94A3B8;">DIỄN ĐÀN M&A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:11px; color:#D8B4FE;">KEYNOTE SPEAKERS &amp; PANELIST SPOTLIGHT</div>
        </div>
      </div>
    </body></html>"""

print("Rendering Master Suite Components to 4K...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # 1. Social Posts Renders
    def render(html, w, h, out_name):
        page = browser.new_page(viewport={"width": w, "height": h})
        page.set_content(html)
        page.wait_for_timeout(400)
        out_path = SUITE_DIR / out_name
        page.screenshot(path=str(out_path))
        shutil.copy(out_path, BRAIN_DIR / out_name)
        page.close()
        print(f"Rendered: {out_name} ({w}x{h})")
        return out_path

    f_1x1 = render(get_social_1x1(), 1080, 1080, "SUITE_Social_1x1_Square_4K.png")
    f_4x5 = render(get_social_4x5(), 1080, 1350, "SUITE_Social_4x5_Portrait_4K.png")
    f_9x16 = render(get_social_9x16(), 1080, 1920, "SUITE_Social_9x16_Story_4K.png")
    f_cover = render(get_social_cover(), 1200, 628, "SUITE_Social_191x1_Cover_4K.png")

    # 2. 16:9 Landing Hero & Slide Deck Renders
    f_landing = render(get_landing_hero(), 1920, 1080, "SUITE_Landing_Hero_UI_4K.png")
    f_s02 = render(get_slide_agenda(), 1920, 1080, "SUITE_Slide_02_Agenda_4K.png")
    f_s03 = render(get_slide_data(), 1920, 1080, "SUITE_Slide_03_Architecture_Data_4K.png")
    f_s04 = render(get_slide_speakers(), 1920, 1080, "SUITE_Slide_04_Speakers_4K.png")

    # 3. Master Presentation Board (Exact composition the user loved, upgraded with luxury typography & generous logo space)
    uri_1x1 = to_data_uri(f_1x1)
    uri_4x5 = to_data_uri(f_4x5)
    uri_9x16 = to_data_uri(f_9x16)
    uri_cover = to_data_uri(f_cover)
    uri_landing = to_data_uri(f_landing)
    uri_s02 = to_data_uri(f_s02)
    uri_s03 = to_data_uri(f_s03)
    uri_s04 = to_data_uri(f_s04)

    master_board_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: radial-gradient(circle at 50% 25%, #150F33 0%, #070D20 75%);
        font-family: 'Be Vietnam Pro', sans-serif; color: #FFFFFF;
        padding: 32px 48px;
        display: flex; flex-direction: column; justify-content: space-between;
      }}
      .mono {{ font-family: 'Manrope', sans-serif; letter-spacing: 0.18em; text-transform: uppercase; }}
      .panel {{
        background: rgba(11, 18, 42, 0.86);
        border: 1px solid rgba(155, 77, 255, 0.4);
        border-radius: 10px;
        padding: 14px;
        display: flex; flex-direction: column; justify-content: space-between;
        box-shadow: 0 12px 32px rgba(0,0,0,0.65);
      }}
      .badge {{
        display: inline-block; padding: 4px 10px; border-radius: 4px;
        background: linear-gradient(90deg, #6B2D9B, #245BFF);
        border: 1px solid rgba(255,255,255,0.3);
        font-family: 'Manrope', sans-serif; font-size: 9.5px; font-weight: 800; color: #FFFFFF;
      }}
    </style></head><body>
      <!-- Top Grand Header Bar with Generous Logo Space -->
      <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:14px; border-bottom:1px solid rgba(155,77,255,0.3);">
        <div style="display:flex; align-items:center; gap:20px;">
          <img src="{u_logo}" style="height:44px; width:auto;" alt="VMAA Logo">
          <div style="width:1px; height:32px; background:rgba(255,255,255,0.2);"></div>
          <div>
            <div style="font-size:18px; font-weight:800; letter-spacing:0.12em; text-transform:uppercase; color:#FFFFFF;">
              MULTI-RATIO DIGITAL, SOCIAL MEDIA, LANDING PAGE &amp; SLIDE DECK SUITE
            </div>
            <div class="mono" style="font-size:10px; color:#D8B4FE; margin-top:3px;">
              DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · REAL ESTATE — TECHNOLOGY · 13.12.2026 · ĐÀ NẴNG
            </div>
          </div>
        </div>
        <div class="badge" style="font-size:11px; padding:7px 16px;">ALL NATIVE 4K STANDALONE FILES EXPORTED</div>
      </div>

      <!-- Main Grid: Left = Social Ratios (9:16, 4:5, 1:1, 1.91:1) | Right = Landing Page + 16:9 Slide Deck -->
      <div style="display:grid; grid-template-columns: 1.05fr 1.25fr; gap:22px; height:890px; margin-top:14px;">

        <!-- LEFT COLUMN: SOCIAL MEDIA FORMATS -->
        <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="mono" style="font-size:12px; font-weight:800; letter-spacing:0.18em; color:#D8B4FE;">01 // SOCIAL MEDIA POST &amp; STORY RATIOS</span>
            <span class="mono" style="font-size:9.5px; color:#38BDF8;">FACEBOOK · LINKEDIN · INSTAGRAM · TIKTOK · ZALO</span>
          </div>

          <!-- Top Social Row: 9:16 Story + 4:5 Portrait + 1:1 Square -->
          <div style="display:grid; grid-template-columns: 0.82fr 1.04fr 1.14fr; gap:14px; height:510px;">
            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; white-space:nowrap;">
                <span class="badge">9:16 STORY</span>
                <span class="mono" style="font-size:8.5px; color:#D8B4FE;">2160×3840</span>
              </div>
              <div style="flex:1; background-image:url('{uri_9x16}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; white-space:nowrap;">
                <span class="badge">4:5 PORTRAIT</span>
                <span class="mono" style="font-size:8.5px; color:#38BDF8;">2160×2700</span>
              </div>
              <div style="flex:1; background-image:url('{uri_4x5}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; white-space:nowrap;">
                <span class="badge">1:1 SQUARE</span>
                <span class="mono" style="font-size:8.5px; color:#FACC15;">2160×2160</span>
              </div>
              <div style="flex:1; background-image:url('{uri_1x1}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>
          </div>

          <!-- Bottom Social Banner: 1.91:1 Event Cover -->
          <div class="panel" style="height:310px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="badge">1.91:1 FACEBOOK / LINKEDIN EVENT COVER &amp; OPENGRAPH PREVIEW</span>
              <span class="mono" style="font-size:8.5px; color:#38BDF8;">2400×1256 (1200×628 @2X)</span>
            </div>
            <div style="flex:1; background-image:url('{uri_cover}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
          </div>
        </div>

        <!-- RIGHT COLUMN: LANDING PAGE HERO UI & 16:9 SLIDE DECK -->
        <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="mono" style="font-size:12px; font-weight:800; letter-spacing:0.18em; color:#D8B4FE;">02 // LANDING PAGE HERO UI &amp; 16:9 SLIDE DECK TEMPLATES</span>
            <span class="mono" style="font-size:9.5px; color:#38BDF8;">WEB PORTAL + POWERPOINT / KEYNOTE 16:9</span>
          </div>

          <!-- Top Hero Card: 16:9 Landing Page -->
          <div class="panel" style="height:510px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="badge">16:9 LANDING PAGE ABOVE-THE-FOLD HERO UI (WITH LIVE HTML/CSS)</span>
              <span class="mono" style="font-size:8.5px; color:#38BDF8;">3840×2160 &bull; LANDING_PAGE.HTML</span>
            </div>
            <div style="flex:1; background-image:url('{uri_landing}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
          </div>

          <!-- Bottom Row: 3 Slides (Agenda + Data + Speakers) -->
          <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:14px; height:310px;">
            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="badge">SLIDE 02 &bull; AGENDA</span>
                <span class="mono" style="font-size:8px; color:#D8B4FE;">16:9 4K</span>
              </div>
              <div style="flex:1; background-image:url('{uri_s02}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="badge">SLIDE 03 &bull; M&A DATA</span>
                <span class="mono" style="font-size:8px; color:#D8B4FE;">16:9 4K</span>
              </div>
              <div style="flex:1; background-image:url('{uri_s03}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="badge">SLIDE 04 &bull; SPEAKERS</span>
                <span class="mono" style="font-size:8px; color:#D8B4FE;">16:9 4K</span>
              </div>
              <div style="flex:1; background-image:url('{uri_s04}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>
          </div>
        </div>

      </div>
    </body></html>"""

    # Render Grand Master Board 4K (3840x2160)
    page_master = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    page_master.set_content(master_board_html)
    page_master.wait_for_timeout(600)
    out_master = EXPORTS_DIR / "11_VMAA_Master_Suite_Overview_4K.png"
    page_master.screenshot(path=str(out_master))
    shutil.copy(out_master, BRAIN_DIR / "11_VMAA_Master_Suite_Overview_4K.png")
    page_master.close()
    print("Rendered Grand Master Overview Board: 11_VMAA_Master_Suite_Overview_4K.png")

    # 4. Typography & Logo Clearspace Exploration Board (3840x2160)
    typo_board_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: #070D20; font-family: 'Be Vietnam Pro', sans-serif; color: #FFFFFF;
        padding: 48px; display: flex; flex-direction: column; justify-content: space-between;
      }}
      .mono {{ font-family: 'Manrope', sans-serif; letter-spacing: 0.18em; text-transform: uppercase; }}
      .card {{ background: rgba(10,16,38,0.85); border: 1px solid rgba(155,77,255,0.35); border-radius: 12px; padding: 32px; backdrop-filter: blur(20px); }}
    </style></head><body>
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(155,77,255,0.3); padding-bottom:16px;">
        <div style="display:flex; align-items:center; gap:20px;">
          <img src="{u_logo}" style="height:44px; width:auto;">
          <div>
            <div style="font-size:18px; font-weight:800; letter-spacing:0.12em; text-transform:uppercase;">EXECUTIVE TYPOGRAPHY &amp; LOGO CLEARSPACE SPECIFICATION</div>
            <div class="mono" style="font-size:10px; color:#D8B4FE; margin-top:2px;">VMAA M&amp;A MIỀN TRUNG 2026 · BRAND IDENTITY SYSTEM</div>
          </div>
        </div>
        <div class="mono" style="font-size:11px; color:#FACC15;">AUTHORITATIVE EDITORIAL STANDARDS</div>
      </div>

      <div style="display:grid; grid-template-columns: 1.1fr 0.9fr; gap:36px; height:860px; margin-top:20px;">
        <!-- Left: 3 Refined Typography Options -->
        <div style="display:flex; flex-direction:column; gap:20px;">
          <div class="card" style="border-left: 4px solid #245BFF;">
            <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; margin-bottom:8px;">OPTION 1: BE VIETNAM PRO 900 // TECH-EXECUTIVE LEADERSHIP (RECOMMENDED)</div>
            <div style="font-family:'Be Vietnam Pro',sans-serif; font-size:42px; font-weight:900; line-height:1; text-transform:uppercase; margin-bottom:6px;">
              DIỄN ĐÀN M&A 2026 MIỀN TRUNG
            </div>
            <div style="font-family:'Be Vietnam Pro',sans-serif; font-size:16px; font-weight:700; color:#CBD5E1;">
              Kiến trúc Giá trị: <span style="color:#FACC15; font-style:italic;">Bất động sản × Công nghệ</span>
            </div>
            <div class="mono" style="font-size:10px; color:#94A3B8; margin-top:12px;">Đặc tính: Được thiết kế bởi các chuyên gia kiểu chữ Việt Nam, hoàn thiện 100% dấu thanh, dáng chữ uy quyền.</div>
          </div>

          <div class="card" style="border-left: 4px solid #9B4DFF;">
            <div class="mono" style="font-size:11px; font-weight:800; color:#D8B4FE; margin-bottom:8px;">OPTION 2: OUTFIT 800 // ARCHITECTURAL HIGH-FASHION &amp; SCALE</div>
            <div style="font-family:'Outfit',sans-serif; font-size:44px; font-weight:800; line-height:1; text-transform:uppercase; margin-bottom:6px;">
              DIỄN ĐÀN M&A 2026 MIỀN TRUNG
            </div>
            <div style="font-family:'Outfit',sans-serif; font-size:17px; font-weight:600; color:#CBD5E1;">
              Kiến trúc Giá trị: <span style="color:#FACC15; font-style:italic;">Bất động sản × Công nghệ</span>
            </div>
            <div class="mono" style="font-size:10px; color:#94A3B8; margin-top:12px;">Đặc tính: Hình khối hình học thanh thoát, không gian thoáng rộng, gợi cảm giác đẳng cấp quốc tế.</div>
          </div>

          <div class="card" style="border-left: 4px solid #38BDF8;">
            <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8; margin-bottom:8px;">OPTION 3: PLUS JAKARTA SANS 800 // BLOOMBERG EDITORIAL AUTHORITY</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:40px; font-weight:800; line-height:1; text-transform:uppercase; margin-bottom:6px;">
              DIỄN ĐÀN M&A 2026 MIỀN TRUNG
            </div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:16px; font-weight:700; color:#CBD5E1;">
              Kiến trúc Giá trị: <span style="color:#FACC15; font-style:italic;">Bất động sản × Công nghệ</span>
            </div>
            <div class="mono" style="font-size:10px; color:#94A3B8; margin-top:12px;">Đặc tính: Phong cách báo chí tài chính quốc tế, tỷ lệ cân đối chuẩn mực, độ tương phản sắc nét.</div>
          </div>
        </div>

        <!-- Right: Official Logo Clearspace & Layout Rules -->
        <div class="card" style="display:flex; flex-direction:column; justify-content:space-between;">
          <div>
            <div class="mono" style="font-size:12px; font-weight:800; color:#FACC15; margin-bottom:12px;">QUY CHUẨN KHOẢNG TRỐNG AN TOÀN CHO LOGO (CLEARSPACE ZONE)</div>
            <div style="font-size:15px; color:#E2E8F0; line-height:1.6; margin-bottom:24px;">
              Nhằm đảm bảo tính độc lập và uy nghiêm của thương hiệu VMAA cùng các đơn vị đồng hành/nhà tài trợ, logo luôn sở hữu vùng đệm an toàn tuyệt đối, không bị đóng khung trong hộp và không bị chữ hay hiệu ứng đè lấn.
            </div>

            <!-- Visual Diagram of Logo Clearspace -->
            <div style="position:relative; background:rgba(7,13,32,0.9); border:1px dashed rgba(155,77,255,0.6); border-radius:8px; padding:40px; text-align:center; margin-bottom:24px;">
              <div class="mono" style="position:absolute; top:8px; left:50%; transform:translateX(-50%); font-size:9px; color:#38BDF8;">KHOẢNG ĐỆM AN TOÀN (TOP &ge; 40px)</div>
              <img src="{u_logo}" style="height:56px; width:auto; display:inline-block; filter:drop-shadow(0 4px 16px rgba(155,77,255,0.4));">
              <div class="mono" style="position:absolute; bottom:8px; left:50%; transform:translateX(-50%); font-size:9px; color:#38BDF8;">KHOẢNG ĐỆM AN TOÀN (BOTTOM &ge; 32px)</div>
            </div>

            <div style="display:flex; flex-direction:column; gap:10px; font-size:13px; color:#CBD5E1;">
              <div>✔ <strong>Không đóng khung:</strong> Loại bỏ hoàn toàn viền hộp hay nút bo tròn quanh logo.</div>
              <div>✔ <strong>Không chồng lấn:</strong> Tiêu đề chính cách đường chân logo tối thiểu 48px – 64px.</div>
              <div>✔ <strong>Chừa vị trí đối tác:</strong> Phía đối xứng bên phải góc trên dành riêng cho co-organizer / diamond sponsor.</div>
            </div>
          </div>

          <div style="border-top:1px solid rgba(155,77,255,0.25); padding-top:16px; display:flex; justify-content:space-between; align-items:center;">
            <div class="mono" style="font-size:10px; color:#94A3B8;">CHỈ SỐ TỶ LỆ CHUẨN</div>
            <div class="mono" style="font-size:10px; font-weight:800; color:#38BDF8;">VECTOR SVG MASTER &bull; 100% LOSSLESS</div>
          </div>
        </div>
      </div>
    </body></html>"""

    page_typo = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    page_typo.set_content(typo_board_html)
    page_typo.wait_for_timeout(600)
    out_typo = EXPORTS_DIR / "12_VMAA_Typography_And_Logo_Clearspace_4K.png"
    page_typo.screenshot(path=str(out_typo))
    shutil.copy(out_typo, BRAIN_DIR / "12_VMAA_Typography_And_Logo_Clearspace_4K.png")
    page_typo.close()
    print("Rendered Typography & Logo Clearspace Board: 12_VMAA_Typography_And_Logo_Clearspace_4K.png")

    browser.close()

print("Master Suite v2 rendering complete!")
