import os
import sys
import base64
import shutil
import asyncio
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
from playwright.async_api import async_playwright

ROOT = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")
ASSETS_DIR = ROOT / "assets"
PLATES_DIR = ASSETS_DIR / "plates"
EXPORTS_DIR = ROOT / "exports" / "v2_production"
PORTRAIT_DIR = EXPORTS_DIR / "portrait_social"
STAGE_DIR = EXPORTS_DIR / "stage_venue"
SOCIAL_DIR = EXPORTS_DIR / "social_media"
GUESTS_DIR = EXPORTS_DIR / "guests_motion"

for d in [EXPORTS_DIR, PORTRAIT_DIR, STAGE_DIR, SOCIAL_DIR, GUESTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


# 100% CLEAN PHALE MASTER PLATE (NO BAKED TEXT, PRISTINE FLUTED PRISM)
u_clean_phale = to_data_uri(PLATES_DIR / "clean_phale_master_4k.png")
u_prism_caustics = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u_logo = to_data_uri(ASSETS_DIR / "vmaa_logo_white_transparent.png")
u_wordmark = to_data_uri(ASSETS_DIR / "vmaa_wordmark_white_transparent.png")

TYPO_CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
<style>
  :root {
    --obsidian: #070D20;
    --navy-deep: #0A1628;
    --amethyst: #6B2D9B;
    --violet: #9B4DFF;
    --cobalt: #245BFF;
    --lavender: #E9D5FF;
    --ice: #63B4FF;
    --gold: #F59E0B;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--obsidian);
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }
  .mono { font-family: 'Space Grotesk', monospace; letter-spacing: 0.18em; text-transform: uppercase; }
  .grotesk { font-family: 'Space Grotesk', sans-serif; }
  .inter { font-family: 'Inter', sans-serif; }
  .pjs { font-family: 'Plus Jakarta Sans', sans-serif; }
</style>
"""


# =========================================================================
# 1. KEY VISUAL HTML GENERATOR (Pha Le Master Architecture)
# =========================================================================
def build_master_kv_html(w=1080, h=1350, aspect_type="portrait", lang="vi"):
    is_vi = (lang == "vi")
    title_eyebrow = "D I Ễ N   Đ À N" if is_vi else "F O R U M"
    title_main = "M&A"
    title_year = "2026"
    title_region = "MIỀN TRUNG" if is_vi else "CENTRAL VIETNAM"
    theme_concept = "Kiến trúc giá trị" if is_vi else "Architecture of value"
    theme_sector = "BẤT ĐỘNG SẢN × CÔNG NGHỆ" if is_vi else "REAL ESTATE × TECHNOLOGY"
    lbl_date = "Ngày" if is_vi else "Date"
    val_date = "13.12.2026"
    lbl_time = "Giờ" if is_vi else "Time"
    val_time = "13:30–17:30"
    lbl_venue = "Địa điểm" if is_vi else "Location"
    val_venue = "Đà Nẵng, Việt Nam" if is_vi else "Da Nang, Vietnam"
    lbl_org = "Đơn vị tổ chức" if is_vi else "Organized by"
    lbl_sponsor_main = "Nhà tài trợ đồng hành" if is_vi else "Co-Sponsor"
    lbl_sponsor_gold = "Nhà tài trợ vàng" if is_vi else "Gold Sponsor"
    lbl_academic = "Đối tác học thuật" if is_vi else "Academic Partner"
    lbl_support = "Đơn vị hỗ trợ" if is_vi else "Supporting Partners"
    val_support = "VMAA CENTRAL CHAPTER"

    # Specific tuning per aspect ratio to prevent collapsing or clipping
    if aspect_type == "square":
        # 1080x1080 Square
        bg_pos = "right center"
        pad_top, pad_sides, pad_bot = 44, 48, 44
        font_eyebrow = "26px"
        font_ma = "124px"
        font_year = "114px"
        font_region = "86px"
        pad_region_top = "38px"
        margin_region_top = "-14px"
        font_concept = "26px"
        font_sector = "38px"
        title_margin_top = "auto"
        hero_padding_top = "0px"
        aurora_style = """
          radial-gradient(900px 750px at 75% 30%, rgba(155,77,255,0.42) 0%, rgba(36,91,255,0.28) 45%, transparent 75%),
          radial-gradient(650px 500px at 25% 65%, rgba(107,45,155,0.32) 0%, transparent 70%)
        """
        readability_style = """
          linear-gradient(180deg, rgba(7,13,32,0.65) 0%, transparent 16%, transparent 72%, rgba(7,13,32,0.85) 100%),
          radial-gradient(850px 600px at 28% 60%, rgba(7,11,28,0.55) 0%, transparent 75%)
        """

    elif aspect_type == "portrait":
        # 1080x1350 Feed 4:5
        bg_pos = "right center"
        pad_top, pad_sides, pad_bot = 48, 52, 48
        font_eyebrow = "26px"
        font_ma = "124px"
        font_year = "114px"
        font_region = "86px"
        pad_region_top = "38px"
        margin_region_top = "-14px"
        font_concept = "26px"
        font_sector = "38px"
        title_margin_top = "auto"
        hero_padding_top = "0px"
        aurora_style = """
          radial-gradient(950px 800px at 75% 30%, rgba(155,77,255,0.42) 0%, rgba(36,91,255,0.28) 45%, transparent 75%),
          radial-gradient(650px 500px at 25% 65%, rgba(107,45,155,0.32) 0%, transparent 70%)
        """
        readability_style = """
          linear-gradient(180deg, rgba(7,13,32,0.65) 0%, transparent 16%, transparent 72%, rgba(7,13,32,0.85) 100%),
          radial-gradient(850px 600px at 28% 60%, rgba(7,11,28,0.55) 0%, transparent 75%)
        """

    elif aspect_type == "story":
        # 1080x1920 Story 9:16
        # Calibrated 35% crop showcases tall organ pipes and avoids blinding center core!
        bg_pos = "35% center"
        pad_top, pad_sides, pad_bot = 80, 56, 72
        font_eyebrow = "28px"
        font_ma = "136px"
        font_year = "126px"
        font_region = "96px"
        pad_region_top = "42px"
        margin_region_top = "-16px"
        font_concept = "30px"
        font_sector = "44px"
        title_margin_top = "auto"
        hero_padding_top = "40px"
        aurora_style = """
          radial-gradient(1000px 900px at 70% 30%, rgba(155,77,255,0.40) 0%, rgba(36,91,255,0.25) 45%, transparent 75%),
          radial-gradient(750px 650px at 25% 65%, rgba(107,45,155,0.30) 0%, transparent 70%)
        """
        readability_style = """
          linear-gradient(180deg, rgba(7,13,32,0.72) 0%, transparent 16%, transparent 72%, rgba(7,13,32,0.90) 100%),
          radial-gradient(900px 750px at 30% 55%, rgba(7,11,28,0.58) 0%, transparent 75%)
        """

    elif aspect_type == "landscape":
        # 1920x1080 Landscape 16:9
        bg_pos = "center center"
        pad_top, pad_sides, pad_bot = 44, 72, 44
        font_eyebrow = "26px"
        font_ma = "132px"
        font_year = "120px"
        font_region = "92px"
        pad_region_top = "40px"
        margin_region_top = "-16px"
        font_concept = "28px"
        font_sector = "40px"
        title_margin_top = "auto"
        hero_padding_top = "0px"
        aurora_style = """
          radial-gradient(950px 750px at 75% 35%, rgba(155,77,255,0.38) 0%, rgba(36,91,255,0.22) 45%, transparent 75%),
          radial-gradient(700px 550px at 22% 52%, rgba(107,45,155,0.28) 0%, transparent 70%)
        """
        readability_style = """
          linear-gradient(90deg, rgba(7,11,28,0.85) 0%, rgba(10,16,40,0.60) 36%, rgba(14,16,45,0.20) 65%, transparent 85%),
          linear-gradient(180deg, rgba(7,13,32,0.82) 0%, transparent 18%, transparent 80%, rgba(7,13,32,0.92) 100%)
        """

    elif aspect_type == "stage":
        # 3840x1080 Stage Curved 32:9
        bg_pos = "right 62%"
        pad_top, pad_sides, pad_bot = 60, 120, 60
        font_eyebrow = "32px"
        font_ma = "168px"
        font_year = "154px"
        font_region = "118px"
        pad_region_top = "48px"
        margin_region_top = "-20px"
        font_concept = "34px"
        font_sector = "50px"
        title_margin_top = "auto"
        hero_padding_top = "0px"
        aurora_style = """
          radial-gradient(1600px 900px at 70% 40%, rgba(155,77,255,0.40) 0%, rgba(36,91,255,0.25) 50%, transparent 75%)
        """
        readability_style = """
          linear-gradient(90deg, rgba(7,11,28,0.95) 0%, rgba(10,16,40,0.82) 28%, rgba(14,16,45,0.35) 55%, transparent 75%),
          linear-gradient(180deg, rgba(7,13,32,0.85) 0%, transparent 20%, transparent 80%, rgba(7,13,32,0.95) 100%)
        """

    # Stage 32:9 has unique ultra-wide layout
    if aspect_type == "stage":
        return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
          body {{
            width: 3840px; height: 1080px;
            background: #070D20;
          }}
          .plate-bg {{
            position: absolute; inset: 0;
            background-image: url('{u_clean_phale}');
            background-size: cover; background-position: {bg_pos};
            filter: brightness(1.15) contrast(1.12) saturate(1.25);
          }}
          .aurora-wash {{
            position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
            background: {aurora_style};
          }}
          .readability-gradient {{
            position: absolute; inset: 0; pointer-events: none;
            background: {readability_style};
          }}
          .container {{
            position: absolute; inset: {pad_top}px {pad_sides}px {pad_bot}px {pad_sides}px;
            display: flex; justify-content: space-between; align-items: center;
            z-index: 10;
          }}
          .title-hero {{
            max-width: 1400px; padding-left: 10px;
          }}
          .eyebrow {{
            font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600; font-size: {font_eyebrow};
            letter-spacing: 0.42em; color: #FFFFFF; text-shadow: 0 0 20px rgba(155,77,255,0.85); margin-bottom: 12px;
          }}
          .main-row {{
            display: flex; align-items: baseline; gap: 24px; white-space: nowrap; line-height: 0.92;
          }}
          .t-ma {{
            font-weight: 800; font-size: {font_ma}; letter-spacing: -0.02em; color: #FFFFFF;
            text-shadow: 0 0 36px rgba(155,77,255,0.75), 0 4px 18px rgba(0,0,0,0.85);
          }}
          .t-year {{
            font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: {font_year};
            color: transparent; -webkit-text-stroke: 3.5px #FFFFFF;
            filter: drop-shadow(0 0 18px rgba(155,77,255,0.85));
          }}
          .t-region {{
            display: inline-block; font-weight: 800; font-size: {font_region}; letter-spacing: -0.01em;
            line-height: 1.28; padding-top: {pad_region_top}; margin-top: {margin_region_top};
            background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 44%, #63B4FF 72%, #A5D8FF 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 4px 18px rgba(36,91,255,0.65));
          }}
          .theme-strip {{
            margin-top: 28px; display: flex; flex-direction: column; gap: 10px;
          }}
          .theme-concept {{
            display: flex; align-items: center; gap: 16px;
            font-size: {font_concept}; font-weight: 600; color: #E9D5FF;
            text-shadow: 0 0 14px rgba(155,77,255,0.6);
          }}
          .theme-concept::before {{
            content: ''; display: inline-block; width: 56px; height: 4px;
            background: linear-gradient(90deg, #9B4DFF, #63B4FF);
            box-shadow: 0 0 10px #9B4DFF;
          }}
          .theme-sector {{
            font-size: {font_sector}; font-weight: 800; color: #FFFFFF;
            letter-spacing: -0.01em; text-shadow: 0 2px 16px rgba(0,0,0,0.9);
          }}
          .stage-logistics {{
            margin-top: 40px; display: flex; gap: 36px; align-items: center;
            font-family: 'Space Grotesk', sans-serif; font-size: 18px; font-weight: 700; color: #93C5FD;
            letter-spacing: 0.10em; text-transform: uppercase;
          }}
          .stage-logistics span {{ color: #FFFFFF; }}
          .stage-crest {{
            text-align: right; display: flex; flex-direction: column; align-items: flex-end; gap: 14px;
          }}
          .stage-crest img {{
            height: 90px; width: auto; display: block;
          }}
          .stage-badge {{
            font-family: 'Space Grotesk', sans-serif; font-size: 14px; font-weight: 700;
            color: #C084FC; letter-spacing: 0.18em; text-transform: uppercase;
          }}
        </style></head><body>
          <div class="plate-bg"></div>
          <div class="aurora-wash"></div>
          <div class="readability-gradient"></div>
          <div class="container">
            <div class="title-hero">
              <div class="eyebrow">{title_eyebrow}</div>
              <div class="main-row"><span class="t-ma">{title_main}</span><span class="t-year">{title_year}</span></div>
              <div class="t-region">{title_region}</div>
              <div class="theme-strip">
                <div class="theme-concept">{theme_concept}</div>
                <div class="theme-sector">{theme_sector}</div>
              </div>
              <div class="stage-logistics">
                <span>{val_date}</span> • <span>{val_time}</span> • <span>{val_venue.upper()}</span>
              </div>
            </div>
            <div class="stage-crest">
              <img src="{u_logo}" alt="VMAA Logo"/>
              <div class="stage-badge">CENTRAL VIETNAM CHAPTER · SUMMIT STAGE DISPLAY</div>
            </div>
          </div>
        </body></html>"""

    # Standard Square, Portrait, Story, Landscape layout
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_clean_phale}');
        background-size: cover; background-position: {bg_pos};
        filter: brightness(1.18) contrast(1.15) saturate(1.28);
      }}
      .aurora-wash {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background: {aurora_style};
      }}
      .readability-gradient {{
        position: absolute; inset: 0; pointer-events: none;
        background: {readability_style};
      }}
      .container {{
        position: absolute; inset: {pad_top}px {pad_sides}px {pad_bot}px {pad_sides}px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .top-band {{
        display: flex; justify-content: space-between; align-items: flex-start;
        padding-bottom: 16px; border-bottom: 1px solid rgba(233,213,255,0.25);
      }}
      .slot-cap {{
        font-family: 'Space Grotesk', sans-serif; font-size: 10px; font-weight: 600;
        color: rgba(233,213,255,0.8); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 6px;
      }}
      .slot-box {{
        display: flex; align-items: center; min-height: 44px;
      }}
      .slot-box img {{
        max-height: 48px; width: auto; display: block;
      }}
      .title-hero {{
        margin-top: {title_margin_top}; margin-bottom: auto; padding-left: 4px; max-width: 960px;
        padding-top: {hero_padding_top};
      }}
      .eyebrow {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600; font-size: {font_eyebrow};
        letter-spacing: 0.40em; color: #FFFFFF; text-shadow: 0 0 18px rgba(155,77,255,0.85); margin-bottom: 8px;
      }}
      .main-row {{
        display: flex; align-items: baseline; gap: 18px; white-space: nowrap; line-height: 0.92;
      }}
      .t-ma {{
        font-weight: 800; font-size: {font_ma}; letter-spacing: -0.02em; color: #FFFFFF;
        text-shadow: 0 0 32px rgba(155,77,255,0.75), 0 4px 16px rgba(0,0,0,0.85);
      }}
      .t-year {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: {font_year};
        color: transparent; -webkit-text-stroke: 2.8px #FFFFFF;
        filter: drop-shadow(0 0 16px rgba(155,77,255,0.85));
      }}
      .t-region {{
        display: inline-block;
        font-weight: 800; font-size: {font_region}; letter-spacing: -0.01em;
        line-height: 1.28;
        padding-top: {pad_region_top};
        margin-top: {margin_region_top};
        background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 44%, #63B4FF 72%, #A5D8FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 4px 18px rgba(36,91,255,0.65));
      }}
      .theme-strip {{
        margin-top: 24px; display: flex; flex-direction: column; gap: 8px;
      }}
      .theme-concept {{
        display: flex; align-items: center; gap: 14px;
        font-size: {font_concept}; font-weight: 600; color: #E9D5FF;
        text-shadow: 0 0 14px rgba(155,77,255,0.6);
      }}
      .theme-concept::before {{
        content: ''; display: inline-block; width: 44px; height: 3.5px;
        background: linear-gradient(90deg, #9B4DFF, #63B4FF);
        box-shadow: 0 0 10px #9B4DFF;
      }}
      .theme-sector {{
        font-size: {font_sector}; font-weight: 800; color: #FFFFFF;
        letter-spacing: -0.01em; text-shadow: 0 2px 14px rgba(0,0,0,0.85);
      }}
      .bottom-band {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-top: 18px; border-top: 1px solid rgba(233,213,255,0.22);
      }}
      .logistics {{
        display: flex; gap: 40px; white-space: nowrap;
      }}
      .log-item small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600;
        color: #63B4FF; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 3px;
      }}
      .log-item b {{
        display: block; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 24px; color: #FFFFFF;
      }}
      .support-box small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600;
        color: rgba(233,213,255,0.75); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 3px; text-align: right;
      }}
      .support-box b {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 13px;
        color: #E9D5FF; text-align: right;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="aurora-wash"></div>
      <div class="readability-gradient"></div>

      <div class="container">
        <!-- Top Frameless Partner / Sponsor Slots -->
        <div class="top-band">
          <div style="flex:1;">
            <div class="slot-cap">{lbl_org}</div>
            <div class="slot-box">
              <img src="{u_logo}" alt="VMAA Logo"/>
            </div>
          </div>
          <div style="flex:1.2;">
            <div class="slot-cap">{lbl_sponsor_main}</div>
            <div class="slot-box" data-slot="sponsor-main">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; color:#60A5FA;">[NHÀ TÀI TRỢ ĐỒNG HÀNH]</span>
            </div>
          </div>
          <div style="flex:1;">
            <div class="slot-cap">{lbl_sponsor_gold}</div>
            <div class="slot-box" data-slot="sponsor-gold">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; color:#FDE047;">[NHÀ TÀI TRỢ VÀNG]</span>
            </div>
          </div>
          <div style="flex:1;">
            <div class="slot-cap">{lbl_academic}</div>
            <div class="slot-box" data-slot="academic">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; color:#F87171;">[ĐỐI TÁC HỌC THUẬT · DUE]</span>
            </div>
          </div>
        </div>

        <!-- Hero Typography (Unboxed, Pure Luxury Architecture) -->
        <div class="title-hero">
          <div class="eyebrow">{title_eyebrow}</div>
          <div class="main-row">
            <span class="t-ma">{title_main}</span>
            <span class="t-year">{title_year}</span>
          </div>
          <div class="t-region">{title_region}</div>

          <div class="theme-strip">
            <div class="theme-concept">{theme_concept}</div>
            <div class="theme-sector">{theme_sector}</div>
          </div>
        </div>

        <!-- Bottom Logistics & Support Bands -->
        <div class="bottom-band">
          <div class="logistics">
            <div class="log-item">
              <small>{lbl_date}</small>
              <b>{val_date}</b>
            </div>
            <div class="log-item">
              <small>{lbl_time}</small>
              <b>{val_time}</b>
            </div>
            <div class="log-item">
              <small>{lbl_venue}</small>
              <b>{val_venue}</b>
            </div>
          </div>

          <div class="support-box">
            <small>{lbl_support}</small>
            <b>{val_support}</b>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 2. SOCIAL MEDIA POSTS HTML GENERATOR (Pha Le Crystal Styling, ZERO Ghost Text)
# =========================================================================
def build_clean_social_post_html(post_id: int, w: int, h: int, lang="vi"):
    is_vi = (lang == "vi")
    scale = min(w / 1080.0, h / 1350.0)

    # Use clean plates alternately: Pha Le (1, 3, 5, 6) & Fluted Caustics (2, 4)
    bg_img = u_clean_phale if post_id not in (2, 4) else u_prism_caustics
    bg_pos = "38% center" if h > w else "center center"

    posts_data = {
        1: {
            "tag": "CÔNG BỐ CHÍNH THỨC" if is_vi else "OFFICIAL ANNOUNCEMENT",
            "kicker": "RA MẮT VMAA MIỀN TRUNG · ĐÀ NẴNG 2026",
            "headline": "DIỄN ĐÀN M&A 2026 MIỀN TRUNG",
            "subhead": "Kiến trúc giá trị: Bất động sản × Công nghệ",
            "body": "Sự kiện thượng đỉnh quy tụ 1,500+ nhà lãnh đạo, tập đoàn kinh tế và các quỹ đầu tư quốc tế hàng đầu tại Đà Nẵng.",
            "cta": "ĐĂNG KÝ THAM DỰ VIP ↗"
        },
        2: {
            "tag": "Ý NIỆM CHỦ ĐỀ" if is_vi else "THEMATIC CONCEPT",
            "kicker": "THIẾT KẾ GIÁ TRỊ VƯỢT THỜI GIAN",
            "headline": "KIẾN TRÚC GIÁ TRỊ",
            "subhead": "Sự hội tụ chiến lược giữa Bất động sản & Công nghệ",
            "body": "Tái cấu trúc dòng vốn, định giá PropTech và tối ưu hóa danh mục tài sản thông qua sức mạnh dữ liệu số.",
            "cta": "KHÁM PHÁ Ý NIỆM ↗"
        },
        3: {
            "tag": "TIÊU ĐIỂM BẤT ĐỘNG SẢN" if is_vi else "SECTOR: REAL ESTATE",
            "kicker": "CHIẾN LƯỢC QUỸ ĐẤT & DÒNG TIỀN",
            "headline": "TÁI CẤU TRÚC QUỸ ĐẤT & VỐN",
            "subhead": "Cơ hội M&A Bất động sản nghỉ dưỡng & công nghiệp Miền Trung",
            "body": "Phân tích biến động pháp lý, mở rộng quỹ đất và các thương vụ hợp tác chiến lược đón đầu chu kỳ tăng trưởng mới.",
            "cta": "XEM BÁO CÁO M&A ↗"
        },
        4: {
            "tag": "TIÊU ĐIỂM CÔNG NGHỆ" if is_vi else "SECTOR: TECHNOLOGY",
            "kicker": "PROPTECH & AI ĐỊNH GIÁ DOANH NGHIỆP",
            "headline": "CÔNG NGHỆ × TÀI CHÍNH M&A",
            "subhead": "Công nghệ nâng tầm giá trị và tính thanh khoản thương vụ",
            "body": "Ứng dụng mô hình AI thẩm định giá tài sản, chuyển đổi số và nâng cao biên lợi nhuận cho các dự án quy mô lớn.",
            "cta": "XEM GIẢI PHÁP TECH ↗"
        },
        5: {
            "tag": "DIỄN GIẢ TIÊU BIỂU" if is_vi else "KEYNOTE SPEAKER",
            "kicker": "CHUYÊN GIA ĐẦU NGÀNH",
            "headline": "TS. TRẦN ĐÌNH THIÊN",
            "subhead": "Nguyên Viện trưởng Viện Kinh tế Việt Nam",
            "body": "Chuyên đề: 'Kiến trúc Giá trị Mới & Xu hướng Tái cấu trúc Bất động sản — Công nghệ tại Miền Trung giai đoạn 2026–2030'.",
            "cta": "GẶP GỠ DIỄN GIẢ ↗"
        },
        6: {
            "tag": "LỊCH TRÌNH & ĐĂNG KÝ" if is_vi else "AGENDA & REGISTRATION",
            "kicker": "CHỦ NHẬT · 13.12.2026",
            "headline": "13.12.2026 · 13:30–17:30",
            "subhead": "Ariyana Convention Centre · Đà Nẵng, Việt Nam",
            "body": "3 phiên tọa đàm chiến lược, lễ ký kết thương vụ MOU và phòng Deal Room kết nối đầu tư 1:1 bảo mật.",
            "cta": "ĐĂNG KÝ VÉ SỚM VIP ↗"
        }
    }
    p = posts_data[post_id]

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        position: relative; overflow: hidden;
        background: #070D20;
      }}
      .plate-layer {{
        position: absolute; inset: 0;
        background-image: url('{bg_img}');
        background-size: cover; background-position: {bg_pos};
        filter: brightness(1.15) contrast(1.12) saturate(1.22);
      }}
      .aurora-layer {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient({int(w*0.8)}px {int(h*0.6)}px at 75% 35%, rgba(155,77,255,0.40) 0%, rgba(36,91,255,0.25) 50%, transparent 80%),
          radial-gradient({int(w*0.6)}px {int(h*0.5)}px at 20% 50%, rgba(107,45,155,0.32) 0%, transparent 75%);
      }}
      .shade-layer {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(180deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.35) 30%, rgba(7,13,32,0.55) 65%, rgba(7,13,32,0.95) 100%),
          linear-gradient(90deg, rgba(7,13,32,0.75) 0%, transparent 65%);
      }}
      .content {{
        position: absolute; inset: {int(48*scale)}px {int(52*scale)}px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .tag-pill {{
        display: inline-flex; align-items: center; gap: 8px;
        padding: {int(7*scale)}px {int(18*scale)}px;
        background: rgba(155,77,255,0.22); border: 1px solid rgba(233,213,255,0.45);
        font-family: 'Space Grotesk', monospace; font-size: {int(12*scale)}px; font-weight: 700;
        color: #E9D5FF; letter-spacing: 0.16em; text-transform: uppercase;
        border-radius: 4px;
      }}
      .cta-btn {{
        display: inline-flex; align-items: center; gap: 10px;
        padding: {int(14*scale)}px {int(28*scale)}px;
        background: linear-gradient(90deg, #9B4DFF, #245BFF);
        font-family: 'Space Grotesk', sans-serif; font-size: {int(15*scale)}px; font-weight: 700;
        color: #FFFFFF; letter-spacing: 0.12em; text-transform: uppercase;
        box-shadow: 0 0 24px rgba(155,77,255,0.5); border: 1px solid #FFFFFF;
        border-radius: 6px;
      }}
      .plinth-box {{
        background: linear-gradient(180deg, rgba(30,42,88,0.88) 0%, rgba(11,18,44,0.96) 100%);
        border: 1.5px solid rgba(192,132,252,0.45);
        border-top: 3px solid #C084FC;
        box-shadow: 0 15px 45px rgba(107,45,155,0.4), inset 0 1px 0 rgba(255,255,255,0.3);
        border-radius: 12px;
        padding: {int(20*scale)}px {int(26*scale)}px;
        margin-top: {int(18*scale)}px;
        max-width: {int(w*0.82)}px;
      }}
    </style></head><body>
      <div class="plate-layer"></div>
      <div class="aurora-layer"></div>
      <div class="shade-layer"></div>

      <div class="content">
        <!-- Top Lockup -->
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo}" alt="VMAA Logo" style="height:{int(42*scale)}px; width:auto;"/>
          <div class="tag-pill">{p['tag']}</div>
        </div>

        <!-- Middle Hero Message -->
        <div style="margin:auto 0; max-width:{int(w*0.88)}px;">
          <div style="font-family:'Space Grotesk',sans-serif; font-size:{int(15*scale)}px; font-weight:700; color:#63B4FF; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:{int(10*scale)}px;">
            {p['kicker']}
          </div>
          <h1 style="font-family:'Plus Jakarta Sans',sans-serif; font-size:{int(46*scale)}px; font-weight:800; line-height:1.15; color:#FFFFFF; text-shadow:0 0 24px rgba(155,77,255,0.7); margin-bottom:{int(14*scale)}px;">
            {p['headline']}
          </h1>
          <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:{int(22*scale)}px; font-weight:700; color:#E9D5FF; margin-bottom:{int(14*scale)}px; line-height:1.35;">
            {p['subhead']}
          </div>
          <div class="plinth-box">
            <p style="font-size:{int(16*scale)}px; line-height:1.55; color:rgba(255,255,255,0.92); margin-bottom:{int(16*scale)}px;">
              {p['body']}
            </p>
            <div class="cta-btn">{p['cta']}</div>
          </div>
        </div>

        <!-- Bottom Event Stamp -->
        <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-top:{int(16*scale)}px; border-top:1px solid rgba(233,213,255,0.22);">
          <div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:{int(11*scale)}px; font-weight:600; color:#63B4FF; text-transform:uppercase; margin-bottom:3px;">
              NGÀY & ĐỊA ĐIỂM
            </div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:{int(18*scale)}px; color:#FFFFFF;">
              13.12.2026 · ĐÀ NẴNG, VIỆT NAM
            </div>
          </div>
          <div style="font-family:'Space Grotesk',sans-serif; font-size:{int(12*scale)}px; font-weight:700; color:#E9D5FF; text-align:right;">
            VMAA CENTRAL CHAPTER
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 3. MASTER RENDER PIPELINE
# =========================================================================
async def run_pipeline():
    print("=" * 70)
    print("STARTING UNIFIED MASTER PHA LE RENDER PIPELINE")
    print("=" * 70)

    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--force-color-profile=srgb"])

        # -------------------------------------------------------------
        # 1. RENDER KEY VISUALS (SQUARE 1:1, PORTRAIT 4:5, STORY 9:16, LANDSCAPE 16:9, STAGE 32:9)
        # -------------------------------------------------------------
        kv_targets = [
            # 1. Square 1:1 (2160x2160 @2x)
            ("Square Pha Le VI", "square", 1080, 1080, 2, "vi",
             PORTRAIT_DIR / "KV_v2_Square_1080x1080_PhaLe.html", PORTRAIT_DIR / "KV_v2_Square_1080x1080_PhaLe.png"),
            ("Square VI Default", "square", 1080, 1080, 2, "vi",
             EXPORTS_DIR / "KV_v2_Square_1080x1080_VI.html", EXPORTS_DIR / "KV_v2_Square_1080x1080_VI.png"),
            ("Square ThapSang (Synced PhaLe)", "square", 1080, 1080, 2, "vi",
             PORTRAIT_DIR / "KV_v2_Square_1080x1080_ThapSang.html", PORTRAIT_DIR / "KV_v2_Square_1080x1080_ThapSang.png"),

            # 2. Portrait Feed 4:5 (2160x2700 @2x)
            ("Portrait Pha Le VI", "portrait", 1080, 1350, 2, "vi",
             PORTRAIT_DIR / "KV_v2_Portrait_1080x1350_PhaLe.html", PORTRAIT_DIR / "KV_v2_Portrait_1080x1350_PhaLe.png"),
            ("Portrait VI Default", "portrait", 1080, 1350, 2, "vi",
             EXPORTS_DIR / "KV_v2_Portrait_1080x1350_VI.html", EXPORTS_DIR / "KV_v2_Portrait_1080x1350_VI.png"),
            ("Portrait EN", "portrait", 1080, 1350, 2, "en",
             PORTRAIT_DIR / "KV_v2_Portrait_1080x1350_EN.html", PORTRAIT_DIR / "KV_v2_Portrait_1080x1350_EN.png"),
            ("Portrait ThapSang (Synced PhaLe)", "portrait", 1080, 1350, 2, "vi",
             PORTRAIT_DIR / "KV_v2_Portrait_1080x1350_ThapSang.html", PORTRAIT_DIR / "KV_v2_Portrait_1080x1350_ThapSang.png"),

            # 3. Story 9:16 (2160x3840 @2x) - RE-FRAMED & NON-COLLAPSING!
            ("Story Pha Le VI", "story", 1080, 1920, 2, "vi",
             PORTRAIT_DIR / "KV_v2_Story_1080x1920_PhaLe.html", PORTRAIT_DIR / "KV_v2_Story_1080x1920_PhaLe.png"),
            ("Story VI Default", "story", 1080, 1920, 2, "vi",
             EXPORTS_DIR / "KV_v2_Story_1080x1920_VI.html", EXPORTS_DIR / "KV_v2_Story_1080x1920_VI.png"),
            ("Story EN", "story", 1080, 1920, 2, "en",
             PORTRAIT_DIR / "KV_v2_Story_1080x1920_EN.html", PORTRAIT_DIR / "KV_v2_Story_1080x1920_EN.png"),
            ("Story ThapSang (Synced PhaLe)", "story", 1080, 1920, 2, "vi",
             PORTRAIT_DIR / "KV_v2_Story_1080x1920_ThapSang.html", PORTRAIT_DIR / "KV_v2_Story_1080x1920_ThapSang.png"),

            # 4. Landscape 16:9 (3840x2160 UHD @2x)
            ("Landscape VI", "landscape", 1920, 1080, 2, "vi",
             EXPORTS_DIR / "KV_v2_Landscape_1920x1080_VI.html", EXPORTS_DIR / "KV_v2_Landscape_1920x1080_VI.png"),
            ("Landscape EN", "landscape", 1920, 1080, 2, "en",
             EXPORTS_DIR / "KV_v2_Landscape_1920x1080_EN.html", EXPORTS_DIR / "KV_v2_Landscape_1920x1080_EN.png"),

            # 5. Curved Stage 32:9 (3840x1080 @1x)
            ("Curved Stage VI", "stage", 3840, 1080, 1, "vi",
             STAGE_DIR / "KV_v2_Curved_Stage_32x9_VI.html", STAGE_DIR / "KV_v2_Curved_Stage_32x9_VI.png"),
            ("Curved Stage EN", "stage", 3840, 1080, 1, "en",
             STAGE_DIR / "KV_v2_Curved_Stage_32x9_EN.html", STAGE_DIR / "KV_v2_Curved_Stage_32x9_EN.png"),
        ]

        print("\n--- 1. Rendering Key Visual Masters ---")
        for name, atype, w, h, dsf, lang, html_path, png_path in kv_targets:
            code = build_master_kv_html(w=w, h=h, aspect_type=atype, lang=lang)
            html_path.write_text(code, encoding="utf-8")
            page = await browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=dsf)
            await page.goto(html_path.as_uri(), wait_until="networkidle")
            await page.wait_for_timeout(450)
            await page.screenshot(path=str(png_path))
            await page.close()
            shutil.copy2(png_path, BRAIN_DIR / png_path.name)
            # Also sync into portrait_social if outside
            if html_path.parent == EXPORTS_DIR and "portrait_social" not in str(png_path):
                sync_p = PORTRAIT_DIR / png_path.name
                if sync_p.parent.exists():
                    shutil.copy2(png_path, sync_p)
            print(f"  ✓ {name}: {png_path.name} ({w*dsf}x{h*dsf})")

        # -------------------------------------------------------------
        # 2. RENDER 6 DISTINCT SOCIAL MEDIA POSTS (4 KEY RATIOS: 4:5, 1:1, 9:16, 16:9)
        # -------------------------------------------------------------
        print("\n--- 2. Rendering 6 Clean Social Media Posts ---")
        post_ratios = [
            ("1080x1350", 1080, 1350, 1),
            ("1080x1080", 1080, 1080, 1),
            ("1080x1920", 1080, 1920, 1),
            ("1920x1080", 1920, 1080, 1),
        ]

        for p_idx in range(1, 7):
            for r_name, pw, ph, p_dsf in post_ratios:
                p_code = build_clean_social_post_html(p_idx, pw, ph, lang="vi")
                out_html = SOCIAL_DIR / f"POST_{p_idx:02d}_{r_name}.html"
                out_png = SOCIAL_DIR / f"POST_{p_idx:02d}_{r_name}.png"
                out_html.write_text(p_code, encoding="utf-8")
                pg = await browser.new_page(viewport={"width": pw, "height": ph}, device_scale_factor=p_dsf)
                await pg.goto(out_html.as_uri(), wait_until="networkidle")
                await pg.wait_for_timeout(350)
                await pg.screenshot(path=str(out_png))
                await pg.close()
                shutil.copy2(out_png, BRAIN_DIR / out_png.name)
            print(f"  ✓ Post #{p_idx:02d} rendered in all 4 core aspect ratios!")

        await browser.close()

    print("\n[SUCCESS] Unified Pha Le Master Pipeline Complete!")


if __name__ == "__main__":
    asyncio.run(run_pipeline())
