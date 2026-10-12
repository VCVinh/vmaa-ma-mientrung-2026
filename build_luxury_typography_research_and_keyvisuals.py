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
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


u_hero_plate = to_data_uri(PLATES_DIR / "purple_opt01_hero_convergence.jpg")
u_prism_plate = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u_logo_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")
u_logo_blue = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_blue_transparent.png")
u_wordmark_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_wordmark_white_transparent.png")

# CURATED LUXURY & INTELLIGENT GOOGLE FONTS (Zero gaming fonts, 100% Vietnamese diacritic perfection)
# 1. Be Vietnam Pro: Specifically engineered by top Vietnamese typographers for global tech and executive branding.
# 2. Manrope: Modern geometric grotesque used by top European fintechs and international think tanks.
# 3. Outfit: Clean, high-fashion architectural sans with pristine proportions.
# 4. Plus Jakarta Sans: Authoritative, modern editorial sans.
# 5. Cormorant Garamond & Cinzel: Classic high-finance & luxury investment elegance.
FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,600;1,700;1,800&family=Cinzel:wght@600;700;800&family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&family=Manrope:wght@300;400;500;600;700;800&family=Outfit:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,800&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,600;1,700;1,800&display=swap" rel="stylesheet">
"""


# -------------------------------------------------------------------------
# Clean Top Sponsor Header (Pure logos, no enclosing boxes/pills)
# -------------------------------------------------------------------------
def get_clean_sponsors_html():
    return f"""
    <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:20px; border-bottom:1px solid rgba(233,213,255,0.22); width:100%;">
      <div>
        <div style="font-family:'Manrope', sans-serif; font-size:9.5px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#93C5FD; margin-bottom:6px;">
          NHÀ TÀI TRỢ ĐỒNG HÀNH
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Manrope', sans-serif; font-size:14px; font-weight:800; color:#FFFFFF;">
          <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#38BDF8; box-shadow:0 0 10px #38BDF8;"></span>
          CENTRAL CAPITAL
        </div>
      </div>

      <div>
        <div style="font-family:'Manrope', sans-serif; font-size:9.5px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#FDE047; margin-bottom:6px;">
          NHÀ TÀI TRỢ VÀNG
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Manrope', sans-serif; font-size:15px; font-weight:800; color:#FDE047; text-shadow:0 0 12px rgba(253,224,71,0.4);">
          <span style="display:inline-block; width:12px; height:12px; border-radius:3px; background:linear-gradient(135deg, #FDE047, #EAB308);"></span>
          GELEX GROUP
        </div>
      </div>

      <!-- Pure VMAA Official Lockup (No artificial rounded rectangle or bounding pill) -->
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="font-family:'Manrope', sans-serif; font-size:9.5px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase; color:#E9D5FF; margin-bottom:6px;">
          ĐƠN VỊ TỔ CHỨC CHỦ TRÌ
        </div>
        <img src="{u_logo_white}" alt="VMAA Logo" style="height:44px; width:auto; display:block; filter:drop-shadow(0 4px 14px rgba(155,77,255,0.4));"/>
      </div>

      <div>
        <div style="font-family:'Manrope', sans-serif; font-size:9.5px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#FCA5A5; margin-bottom:6px;">
          ĐỐI TÁC HỌC THUẬT &amp; VIỆN
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Manrope', sans-serif; font-size:14px; font-weight:800; color:#FFFFFF;">
          <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#F87171; box-shadow:0 0 10px #F87171;"></span>
          ĐH KINH TẾ ĐÀ NẴNG · DUE
        </div>
      </div>

      <div>
        <div style="font-family:'Manrope', sans-serif; font-size:9.5px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#C084FC; margin-bottom:6px;">
          NHÀ TÀI TRỢ BẠC
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Manrope', sans-serif; font-size:14px; font-weight:800; color:#E2E8F0;">
          <span style="display:inline-block; width:10px; height:10px; border-radius:2px; background:#CBD5E1;"></span>
          VILAF LEGAL · KPMG ADVISORY
        </div>
      </div>
    </div>
    """


# -------------------------------------------------------------------------
# Clean Bottom Metadata & Partners (High contrast, human readable, no pills)
# -------------------------------------------------------------------------
def get_clean_bottom_html():
    return f"""
    <div style="display:flex; justify-content:space-between; align-items:flex-end; width:100%; padding-top:22px; border-top:1px solid rgba(233,213,255,0.22);">
      <div style="display:flex; gap:44px; align-items:flex-start;">
        <div>
          <div style="font-family:'Manrope', sans-serif; font-size:11px; font-weight:700; color:#C084FC; text-transform:uppercase; letter-spacing:0.16em; margin-bottom:5px;">
            Thời gian diễn ra
          </div>
          <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:24px; font-weight:800; color:#FFFFFF; letter-spacing:-0.01em;">
            Chủ Nhật · 13.12.2026
          </div>
          <div style="font-family:'Manrope', sans-serif; font-size:13.5px; font-weight:600; color:#93C5FD; margin-top:3px;">
            13:30 – 17:30 (Diễn đàn) · 18:00 – 21:00 (Gala Dinner)
          </div>
        </div>

        <div style="width:1.5px; height:54px; background:rgba(192,132,252,0.35); align-self:center;"></div>

        <div>
          <div style="font-family:'Manrope', sans-serif; font-size:11px; font-weight:700; color:#C084FC; text-transform:uppercase; letter-spacing:0.16em; margin-bottom:5px;">
            Địa điểm tổ chức
          </div>
          <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:24px; font-weight:800; color:#FFFFFF; letter-spacing:-0.01em;">
            Đà Nẵng, Việt Nam
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:13.5px; font-weight:600; color:#CBD5E1; margin-top:3px;">
            Furama Resort / Ariyana Convention Centre
          </div>
        </div>
      </div>

      <div style="display:flex; gap:36px; align-items:flex-end;">
        <div>
          <div style="font-family:'Manrope', sans-serif; font-size:10px; font-weight:700; color:#93C5FD; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:6px; text-align:right;">
            ĐƠN VỊ HỖ TRỢ &amp; QUỸ ĐẦU TƯ
          </div>
          <div style="display:flex; gap:16px; align-items:center; font-family:'Manrope', sans-serif; font-weight:700; font-size:13px; color:#E2E8F0;">
            <span>HIỆP HỘI DN ĐÀ NẴNG</span>
            <span>·</span>
            <span>CLB BẤT ĐỘNG SẢN MIỀN TRUNG</span>
            <span>·</span>
            <span style="color:#60A5FA;">MEKONG CAPITAL</span>
          </div>
        </div>

        <div style="width:1.5px; height:46px; background:rgba(233,213,255,0.22); align-self:center;"></div>

        <div>
          <div style="font-family:'Manrope', sans-serif; font-size:10px; font-weight:700; color:#C084FC; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:6px; text-align:right;">
            ĐỐI TÁC TRUYỀN THÔNG
          </div>
          <div style="display:flex; gap:14px; align-items:center; font-family:'Manrope', sans-serif; font-weight:800; font-size:13.5px;">
            <span style="color:#F87171;">VCCORP</span>
            <span style="color:#60A5FA;">CAFEF</span>
            <span style="color:#C084FC;">FORBES VIETNAM</span>
            <span style="color:#34D399;">VIETSUCCESS</span>
          </div>
        </div>
      </div>
    </div>
    """


# -------------------------------------------------------------------------
# 6 LUXURY & INTELLIGENT TYPOGRAPHY OPTIONS (Researched & Polished)
# -------------------------------------------------------------------------
RESEARCHED_TYPO_CONFIGS = [
    {
        "id": "TYPO_01",
        "name": "System 01: The Next Forum Benchmark (Be Vietnam Pro 900 + Dynamic Italic Gold)",
        "font_family": "Be Vietnam Pro & Manrope",
        "style_notes": "Pure high-prestige executive authority. Heavy architectural titles, zero gaming cuts, dynamic italic gold-amber slogan accent matching Next Forum 2026.",
        "html_title": """
        <div style="font-family:'Manrope', sans-serif; font-size:12.5px; font-weight:700; letter-spacing:0.28em; color:#C084FC; text-transform:uppercase; margin-bottom:10px;">
          ANNUAL STRATEGIC SUMMIT · CENTRAL VIETNAM
        </div>

        <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:36px; font-weight:800; letter-spacing:0.22em; color:#FFFFFF; text-transform:uppercase; line-height:1.1;">
          DIỄN ĐÀN
        </div>
        <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:94px; font-weight:900; letter-spacing:-0.02em; color:#FFFFFF; line-height:0.92; margin-top:4px; text-shadow:0 0 35px rgba(155,77,255,0.65);">
          M&amp;A 2026
        </div>
        <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:68px; font-weight:900; letter-spacing:0.02em; color:#C084FC; line-height:0.98; margin-top:4px; text-shadow:0 0 28px rgba(192,132,252,0.5);">
          MIỀN TRUNG
        </div>

        <!-- Clean Typography Accent (NO button/capsule box) -->
        <div style="margin-top:22px;">
          <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:25px; font-weight:800; color:#FFFFFF; line-height:1.25;">
            KIẾN TRÚC GIÁ TRỊ:
          </div>
          <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:25px; font-weight:800; font-style:italic; color:#FDE047; line-height:1.25; text-shadow:0 0 20px rgba(253,224,71,0.4);">
            BẤT ĐỘNG SẢN × CÔNG NGHỆ
          </div>
          <div style="font-family:'Manrope', sans-serif; font-size:13px; font-weight:600; color:#93C5FD; letter-spacing:0.18em; text-transform:uppercase; margin-top:8px;">
            REAL ESTATE — TECHNOLOGY · ARCHITECTURE OF VALUE
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_02",
        "name": "System 02: World Economic Forum Davos (Authoritative Non-Italic Monumental)",
        "font_family": "Plus Jakarta Sans & Manrope",
        "style_notes": "Symmetrical, restrained, monumental stability. Strict vertical stance, 100% non-italic, deep intellectual gravitas suitable for government and sovereign ministers.",
        "html_title": """
        <div style="font-family:'Manrope', sans-serif; font-size:12px; font-weight:700; letter-spacing:0.32em; color:#93C5FD; text-transform:uppercase; margin-bottom:12px;">
          GLOBAL ECONOMIC &amp; INVESTMENT FORUM
        </div>

        <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:32px; font-weight:700; letter-spacing:0.28em; color:#E9D5FF; text-transform:uppercase;">
          DIỄN ĐÀN M&amp;A
        </div>
        <div style="display:flex; align-items:baseline; gap:16px; margin-top:4px;">
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:88px; font-weight:800; letter-spacing:-0.01em; color:#FFFFFF; line-height:0.92; text-shadow:0 0 35px rgba(255,255,255,0.4);">
            2026
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:68px; font-weight:800; letter-spacing:0.04em; color:#C084FC; line-height:0.92;">
            MIỀN TRUNG
          </div>
        </div>

        <div style="margin-top:24px; padding-left:16px; border-left:3.5px solid #245BFF;">
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:23px; font-weight:700; color:#FFFFFF; letter-spacing:0.02em;">
            KIẾN TRÚC GIÁ TRỊ: BẤT ĐỘNG SẢN &amp; CÔNG NGHỆ
          </div>
          <div style="font-family:'Manrope', sans-serif; font-size:12.5px; font-weight:600; color:#60A5FA; letter-spacing:0.16em; text-transform:uppercase; margin-top:6px;">
            CAPITAL FLOWS · PROPTECH · STRATEGIC DEAL ROOM
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_03",
        "name": "System 03: Milken Global Institute (High-Fashion Architectural Proportions)",
        "font_family": "Outfit Pro",
        "style_notes": "Modern California/New York economic forum aesthetic: Outfit Pro wide proportions, ultra-clean geometry, balanced luxury contrast between bold and thin weights.",
        "html_title": """
        <div style="font-family:'Outfit', sans-serif; font-size:13px; font-weight:700; letter-spacing:0.26em; color:#C084FC; text-transform:uppercase; margin-bottom:12px;">
          THE CENTRAL VIETNAM M&amp;A CONVERGENCE
        </div>

        <div style="font-family:'Outfit', sans-serif; font-size:40px; font-weight:800; letter-spacing:0.1em; color:#FFFFFF; line-height:1.05;">
          DIỄN ĐÀN M&amp;A
        </div>
        <div style="display:flex; align-items:baseline; gap:16px; margin-top:6px;">
          <div style="font-family:'Outfit', sans-serif; font-size:80px; font-weight:900; color:#A855F7; letter-spacing:-0.02em; line-height:0.94; text-shadow:0 0 35px rgba(168,85,247,0.55);">
            MIỀN TRUNG
          </div>
          <div style="font-family:'Outfit', sans-serif; font-size:62px; font-weight:300; color:#FFFFFF; letter-spacing:0.12em; opacity:0.85;">
            2026
          </div>
        </div>

        <div style="margin-top:24px;">
          <div style="font-family:'Outfit', sans-serif; font-size:24px; font-weight:700; color:#FFFFFF; letter-spacing:0.02em;">
            KIẾN TRÚC GIÁ TRỊ: <span style="color:#60A5FA; font-weight:800;">BẤT ĐỘNG SẢN</span> × <span style="color:#C084FC; font-weight:800;">CÔNG NGHỆ</span>
          </div>
          <div style="font-family:'Manrope', sans-serif; font-size:12px; font-weight:500; color:#CBD5E1; letter-spacing:0.16em; margin-top:6px;">
            ORGANIZED BY VMAA · HIGH-LEVEL DEAL PLATFORM
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_04",
        "name": "System 04: Bloomberg & Financial Times (Sovereign Investment Authority)",
        "font_family": "Manrope & Cormorant Garamond",
        "style_notes": "Sovereign wealth fund & top-tier private equity style. Clean Manrope grotesk combined with an italic Cormorant Garamond luxury accent phrase for maximum financial prestige.",
        "html_title": """
        <div style="font-family:'Manrope', sans-serif; font-size:12px; font-weight:700; letter-spacing:0.28em; color:#93C5FD; text-transform:uppercase; margin-bottom:12px;">
          VIETNAM MERGERS &amp; ACQUISITIONS ASSOCIATION
        </div>

        <div style="font-family:'Manrope', sans-serif; font-size:34px; font-weight:800; letter-spacing:0.2em; color:#FFFFFF; text-transform:uppercase;">
          DIỄN ĐÀN M&amp;A
        </div>
        <div style="font-family:'Manrope', sans-serif; font-size:90px; font-weight:800; letter-spacing:-0.03em; color:#FFFFFF; line-height:0.92; margin-top:4px;">
          2026 <span style="color:#A855F7;">MIỀN TRUNG</span>
        </div>

        <div style="margin-top:22px;">
          <div style="font-family:'Cormorant Garamond', serif; font-size:32px; font-weight:700; font-style:italic; color:#FDE047; letter-spacing:0.02em; line-height:1.15; text-shadow:0 0 16px rgba(253,224,71,0.35);">
            Kiến trúc Giá trị: Bất động sản × Công nghệ
          </div>
          <div style="font-family:'Manrope', sans-serif; font-size:12px; font-weight:600; color:#CBD5E1; letter-spacing:0.16em; text-transform:uppercase; margin-top:6px;">
            ARCHITECTURE OF VALUE · PRIVATE EQUITY &amp; ASSET CONVERGENCE
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_05",
        "name": "System 05: Wall Street / Singapore PE Boardroom (Cinzel & Be Vietnam Pro)",
        "font_family": "Cinzel & Be Vietnam Pro",
        "style_notes": "Old-money sovereign capital elegance combined with modern Vietnamese clarity. High-contrast Roman capitals with crisp geometric structure.",
        "html_title": """
        <div style="font-family:'Cinzel', serif; font-size:13.5px; font-weight:700; letter-spacing:0.32em; color:#C084FC; text-transform:uppercase; margin-bottom:12px;">
          CENTRAL VIETNAM LEADERSHIP FORUM
        </div>

        <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:76px; font-weight:900; letter-spacing:-0.01em; color:#FFFFFF; line-height:0.94;">
          M&amp;A 2026
        </div>
        <div style="font-family:'Cinzel', serif; font-size:44px; font-weight:700; letter-spacing:0.18em; color:#93C5FD; text-transform:uppercase; margin-top:6px;">
          MIỀN TRUNG
        </div>

        <div style="margin-top:22px;">
          <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:23px; font-weight:800; color:#FFFFFF; line-height:1.3;">
            KIẾN TRÚC GIÁ TRỊ: <span style="color:#C084FC; font-weight:900;">BẤT ĐỘNG SẢN — CÔNG NGHỆ</span>
          </div>
          <div style="font-family:'Manrope', sans-serif; font-size:13.5px; font-weight:500; font-style:italic; color:#94A3B8; margin-top:4px;">
            Architecture of Value: Real Estate &amp; Technology Convergence
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_06",
        "name": "System 06: Apple Keynote Ultra-Pure (Be Vietnam Pro Display · Zero Clutter)",
        "font_family": "Be Vietnam Pro Display",
        "style_notes": "World-class Silicon Valley keynote purity. Giant razor-sharp letterforms, zero decorative frills, maximizing human visual impact and instantaneous memorability.",
        "html_title": """
        <div style="font-family:'Manrope', sans-serif; font-size:13px; font-weight:700; letter-spacing:0.3em; color:#E9D5FF; text-transform:uppercase; margin-bottom:12px;">
          HIỆP HỘI MUA BÁN &amp; SÁP NHẬP DOANH NGHIỆP VIỆT NAM
        </div>

        <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:94px; font-weight:900; letter-spacing:-0.03em; color:#FFFFFF; line-height:0.92; text-shadow:0 0 35px rgba(255,255,255,0.45);">
          M&amp;A 2026
        </div>
        <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:56px; font-weight:800; letter-spacing:0.02em; color:#A855F7; line-height:1.0; margin-top:6px; text-shadow:0 0 28px rgba(168,85,247,0.55);">
          DIỄN ĐÀN MIỀN TRUNG
        </div>

        <div style="margin-top:22px;">
          <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:25px; font-weight:800; color:#FFFFFF;">
            Kiến trúc Giá trị: <span style="color:#60A5FA; font-weight:900;">Bất động sản</span> &amp; <span style="color:#FDE047; font-weight:900;">Công nghệ</span>
          </div>
          <div style="font-family:'Manrope', sans-serif; font-size:13px; font-weight:600; color:#CBD5E1; letter-spacing:0.16em; text-transform:uppercase; margin-top:8px;">
            1,500+ LEADERS &amp; INVESTORS · SINGAPORE WEF SCALE
          </div>
        </div>
        """
    }
]


def build_full_keyvisual_html(config: dict) -> str:
    sponsors_html = get_clean_sponsors_html()
    bottom_html = get_clean_bottom_html()
    title_html = config["html_title"]

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: #070D20; font-family: 'Be Vietnam Pro', sans-serif; color: #FFFFFF; position: relative;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_hero_plate}');
        background-size: cover; background-position: 70% center;
        filter: brightness(1.18) contrast(1.12) saturate(1.22);
      }}
      .aurora-layer {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient(900px 750px at 78% 45%, rgba(155,77,255,0.42) 0%, rgba(36,91,255,0.28) 50%, transparent 80%),
          radial-gradient(800px 600px at 20% 60%, rgba(107,45,155,0.45) 0%, transparent 75%),
          radial-gradient(600px 450px at 50% 15%, rgba(233,213,255,0.25) 0%, transparent 70%);
      }}
      .shade-layer {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(90deg, rgba(7,11,28,0.92) 0%, rgba(7,11,28,0.85) 44%, rgba(7,11,28,0.45) 70%, rgba(7,11,28,0.75) 100%),
          linear-gradient(180deg, rgba(7,11,28,0.88) 0%, transparent 22%, transparent 75%, rgba(7,11,28,0.94) 100%);
      }}
      .shell {{
        position: absolute; inset: 0; padding: 34px 64px 30px 64px;
        display: flex; flex-direction: column; justify-content: space-between; z-index: 10;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="aurora-layer"></div>
      <div class="shade-layer"></div>

      <div class="shell">
        {sponsors_html}
        <div style="display:flex; flex:1; align-items:center; margin-top:20px; margin-bottom:20px;">
          <div style="flex:0 0 700px; display:flex; flex-direction:column; justify-content:center;">
            {title_html}
          </div>
        </div>
        {bottom_html}
      </div>
    </body></html>"""


def build_comparison_matrix_html():
    cards_html = ""
    for cfg in RESEARCHED_TYPO_CONFIGS:
        cards_html += f"""
        <div style="background:rgba(11,18,44,0.88); border:1px solid rgba(192,132,252,0.35); border-radius:14px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 12px 35px rgba(0,0,0,0.5);">
          <div style="padding:12px 18px; background:rgba(25,35,75,0.7); border-bottom:1px solid rgba(192,132,252,0.25); display:flex; justify-content:space-between; align-items:center;">
            <div style="font-family:'Manrope', sans-serif; font-size:14.5px; font-weight:800; color:#FFFFFF;">
              {cfg['name']}
            </div>
            <div style="font-family:'Manrope', sans-serif; font-size:11px; font-weight:700; color:#38BDF8;">
              {cfg['id']}
            </div>
          </div>
          <div style="flex:1; padding:24px 28px; position:relative; overflow:hidden; background:linear-gradient(135deg, rgba(7,11,28,0.95) 0%, rgba(15,23,55,0.95) 100%);">
            {cfg['html_title']}
          </div>
          <div style="padding:10px 18px; background:rgba(11,18,44,0.9); font-size:11.5px; color:#CBD5E1; border-top:1px solid rgba(233,213,255,0.15); line-height:1.35;">
            <strong style="color:#C084FC;">Font Family:</strong> {cfg['font_family']}<br/>
            {cfg['style_notes']}
          </div>
        </div>
        """

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: #070D20; font-family: 'Be Vietnam Pro', sans-serif; color: #FFFFFF; position: relative;
        padding: 30px 48px; display: flex; flex-direction: column; justify-content: space-between;
      }}
    </style></head><body>
      <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:16px; border-bottom:1px solid rgba(192,132,252,0.3);">
        <div style="display:flex; align-items:center; gap:20px;">
          <img src="{u_logo_white}" alt="VMAA" style="height:40px; width:auto;"/>
          <div>
            <div style="font-family:'Be Vietnam Pro', sans-serif; font-size:24px; font-weight:800; letter-spacing:0.04em; color:#FFFFFF;">
              VMAA M&amp;A 2026 MIỀN TRUNG — BỘ 6 HỆ THỐNG TYPOGRAPHY THƯỢNG ĐỈNH
            </div>
            <div style="font-family:'Manrope', sans-serif; font-size:12px; color:#C084FC; margin-top:2px; letter-spacing:0.1em;">
              DEEP RESEARCH ON FORWARD-LOOKING, INTELLIGENT &amp; PRESTIGIOUS GLOBAL CONFERENCE TYPOGRAPHY
            </div>
          </div>
        </div>
        <div style="font-family:'Manrope', sans-serif; font-size:12px; font-weight:700; color:#38BDF8; padding:6px 14px; background:rgba(36,91,255,0.25); border:1px solid #38BDF8; border-radius:6px;">
          4K SELECTION MATRIX (16:9)
        </div>
      </div>

      <div style="display:grid; grid-template-columns:repeat(3, 1fr); grid-template-rows:repeat(2, 1fr); gap:20px; flex:1; margin-top:20px; margin-bottom:16px;">
        {cards_html}
      </div>

      <div style="display:flex; justify-content:space-between; align-items:center; padding-top:12px; border-top:1px solid rgba(192,132,252,0.2); font-size:12px; color:#94A3B8;">
        <div>LOẠI BỎ HOÀN TOÀN FONT GAMING · SỬ DỤNG FONT KINH ĐIỂN CHUẨN QUỐC TẾ (BE VIETNAM PRO, MANROPE, OUTFIT, PLUS JAKARTA SANS, CINZEL)</div>
        <div style="font-family:'Manrope', sans-serif; font-weight:700; color:#FDE047;">TẤT CẢ PHƯƠNG ÁN ĐÃ XUẤT 4K ĐỘC LẬP</div>
      </div>
    </body></html>"""


def render_all():
    # 1. Primary Hero Key Visual using System 01 (Next Forum Benchmark)
    hero_cfg = RESEARCHED_TYPO_CONFIGS[0]
    hero_html = build_full_keyvisual_html(hero_cfg)
    hero_html_file = EXPORTS_DIR / "01_VMAA_HERO_KEY_VISUAL_4K.html"
    hero_png_file = EXPORTS_DIR / "01_VMAA_HERO_KEY_VISUAL_4K.png"
    hero_html_file.write_text(hero_html, encoding="utf-8")

    # 2. 6 Individual Typo Option HTML files
    rendered_typos = []
    for cfg in RESEARCHED_TYPO_CONFIGS:
        opt_html = build_full_keyvisual_html(cfg)
        opt_html_file = EXPORTS_DIR / f"{cfg['id']}_KeyVisual.html"
        opt_png_file = EXPORTS_DIR / f"{cfg['id']}_KeyVisual_4K.png"
        opt_html_file.write_text(opt_html, encoding="utf-8")
        rendered_typos.append((opt_html_file, opt_png_file))

    # 3. Matrix HTML
    matrix_html = build_comparison_matrix_html()
    matrix_html_file = EXPORTS_DIR / "00_VMAA_6_Typography_Options_Matrix.html"
    matrix_png_file = EXPORTS_DIR / "00_VMAA_6_Typography_Options_Matrix.png"
    matrix_html_file.write_text(matrix_html, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)

        # Primary Hero
        page.goto(hero_html_file.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(hero_png_file), type="png")
        print(f"Rendered {hero_png_file.name} (3840x2160 4K UHD)")
        shutil.copy2(hero_png_file, BRAIN_DIR / hero_png_file.name)

        # 6 Options
        for h_f, p_f in rendered_typos:
            page.goto(h_f.as_uri(), wait_until="networkidle")
            page.wait_for_timeout(800)
            page.screenshot(path=str(p_f), type="png")
            print(f"Rendered {p_f.name} (3840x2160 4K UHD)")
            shutil.copy2(p_f, BRAIN_DIR / p_f.name)

        # Matrix
        page.goto(matrix_html_file.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(matrix_png_file), type="png")
        print(f"Rendered {matrix_png_file.name} (3840x2160 4K UHD)")
        shutil.copy2(matrix_png_file, BRAIN_DIR / matrix_png_file.name)

        browser.close()


if __name__ == "__main__":
    render_all()
