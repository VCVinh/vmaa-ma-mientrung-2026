import os
import sys
import base64
import shutil
import asyncio
import subprocess
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
EXPORTS_DIR = ROOT / "exports" / "v2_production"
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
SOCIAL_DIR = EXPORTS_DIR / "social_media"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)
GUESTS_DIR = EXPORTS_DIR / "guests_motion"
GUESTS_DIR.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


u_plate = to_data_uri(ASSETS_DIR / "plates" / "purple_opt01_hero_convergence.jpg")
u_prism = to_data_uri(ASSETS_DIR / "plates" / "purple_opt02_fluted_caustics.jpg")
u_logo = to_data_uri(ASSETS_DIR / "vmaa_logo_white_transparent.png")
u_wordmark = to_data_uri(ASSETS_DIR / "vmaa_wordmark_white_transparent.png")

# Local typography definitions ensuring complete offline Vietnamese rendering
TYPO_CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=Outfit:wght@300;600;800&family=Unbounded:wght@700;800&display=swap" rel="stylesheet">
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
  }
  .mono { font-family: 'Space Grotesk', monospace; letter-spacing: 0.18em; text-transform: uppercase; }
  .grotesk { font-family: 'Space Grotesk', sans-serif; }
  .inter { font-family: 'Inter', sans-serif; }
  .pjs { font-family: 'Plus Jakarta Sans', sans-serif; }
</style>
"""

# Da Nang Dragon Bridge (Cầu Rồng) & Han River water horizon SVG
def get_dragon_bridge_svg(w=1920, h=400, opacity=0.85):
    return f"""
    <svg width="{w}" height="{h}" viewBox="0 0 1920 400" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:{opacity}; mix-blend-mode:screen; pointer-events:none;">
      <defs>
        <linearGradient id="db_arch" x1="0" y1="0" x2="1920" y2="0" gradientUnits="userSpaceOnUse">
          <stop offset="10%" stop-color="#D97706" stop-opacity="0.2"/>
          <stop offset="35%" stop-color="#F59E0B" stop-opacity="0.95"/>
          <stop offset="60%" stop-color="#FDE047" stop-opacity="0.9"/>
          <stop offset="85%" stop-color="#245BFF" stop-opacity="0.7"/>
          <stop offset="100%" stop-color="#63B4FF" stop-opacity="0.3"/>
        </linearGradient>
        <linearGradient id="db_water" x1="0" y1="0" x2="0" y2="200" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.35"/>
          <stop offset="40%" stop-color="#245BFF" stop-opacity="0.25"/>
          <stop offset="100%" stop-color="#070D20" stop-opacity="0"/>
        </linearGradient>
        <filter id="db_glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="6" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      <!-- Han River Waterline & Shimmering Reflections -->
      <line x1="0" y1="300" x2="1920" y2="300" stroke="rgba(99,180,255,0.4)" stroke-width="1.5" stroke-dasharray="12 6"/>
      <rect x="250" y="302" width="1420" height="90" fill="url(#db_water)"/>

      <!-- Da Nang City Skyline Silhouette in background -->
      <path d="M120 300 L120 270 L140 270 L140 285 L160 285 L160 260 L175 260 L175 300 
               M220 300 L220 250 L235 240 L250 250 L250 300 
               M280 300 L280 275 L310 275 L310 300 
               M1380 300 L1380 255 L1410 255 L1410 240 L1425 240 L1425 300 
               M1450 300 L1450 265 L1480 265 L1480 300 
               M1520 300 L1520 230 L1540 230 L1540 300" 
            stroke="rgba(233,213,255,0.22)" stroke-width="1.2" fill="rgba(10,22,48,0.5)"/>

      <!-- 5 Undulating Steel Arches of Dragon Bridge (Cầu Rồng Đà Nẵng) -->
      <g filter="url(#db_glow)">
        <!-- Arch 1 (Tail / West) -->
        <path d="M 320 300 Q 420 220, 520 300" stroke="url(#db_arch)" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        <!-- Arch 2 -->
        <path d="M 520 300 Q 640 170, 760 300" stroke="url(#db_arch)" stroke-width="5.5" fill="none" stroke-linecap="round"/>
        <!-- Arch 3 (Main High Arch) -->
        <path d="M 760 300 Q 900 130, 1040 300" stroke="url(#db_arch)" stroke-width="6.5" fill="none" stroke-linecap="round"/>
        <!-- Arch 4 -->
        <path d="M 1040 300 Q 1160 175, 1280 300" stroke="url(#db_arch)" stroke-width="5.5" fill="none" stroke-linecap="round"/>
        <!-- Arch 5 (Head facing East / Sea) -->
        <path d="M 1280 300 Q 1380 215, 1460 300" stroke="url(#db_arch)" stroke-width="4.5" fill="none" stroke-linecap="round"/>

        <!-- Stylized Dragon Head & Mouth breathing light -->
        <path d="M 1440 240 C 1465 230, 1485 240, 1500 235 C 1485 248, 1480 260, 1460 265 Z" fill="#F59E0B" opacity="0.95"/>
        <circle cx="1500" cy="235" r="4" fill="#FFFFFF"/>
        <path d="M 1500 235 Q 1540 228, 1570 232" stroke="#FDE047" stroke-width="2.5" stroke-dasharray="3 3"/>

        <!-- Vertical Suspension Cable Rigs -->
        <g stroke="rgba(245,158,11,0.4)" stroke-width="1.2">
          <line x1="420" y1="260" x2="420" y2="300"/>
          <line x1="640" y1="235" x2="640" y2="300"/>
          <line x1="700" y1="250" x2="700" y2="300"/>
          <line x1="840" y1="210" x2="840" y2="300"/>
          <line x1="900" y1="195" x2="900" y2="300"/>
          <line x1="960" y1="210" x2="960" y2="300"/>
          <line x1="1160" y1="240" x2="1160" y2="300"/>
          <line x1="1380" y1="260" x2="1380" y2="300"/>
        </g>
      </g>

      <!-- Water Reflection Ripples -->
      <g stroke="rgba(245,158,11,0.3)" stroke-width="1.5">
        <line x1="820" y1="315" x2="980" y2="315"/>
        <line x1="860" y1="328" x2="940" y2="328"/>
        <line x1="600" y1="318" x2="700" y2="318"/>
        <line x1="1120" y1="318" x2="1220" y2="318"/>
      </g>
    </svg>
    """


# =========================================================================
# 1. KEY VISUAL PORTRAIT MASTER (1080x1350 Feed & 1080x1920 Story)
# =========================================================================
def build_portrait_kv_html(w=1080, h=1350, lang="vi", show_guides=False):
    is_vi = (lang == "vi")
    title_eyebrow = "DIỄN ĐÀN" if is_vi else "FORUM"
    title_main = "M&A"
    title_region = "MIỀN TRUNG" if is_vi else "CENTRAL VIETNAM"
    theme_concept = "Kiến trúc giá trị" if is_vi else "Architecture of value"
    theme_sector = "Bất động sản × Công nghệ" if is_vi else "Real Estate — Technology"
    lbl_date = "Ngày" if is_vi else "Date"
    lbl_time = "Giờ" if is_vi else "Time"
    lbl_venue = "Địa điểm" if is_vi else "Location"
    lbl_org = "Đơn vị tổ chức" if is_vi else "Organized by"
    lbl_sponsor_main = "Nhà tài trợ đồng hành" if is_vi else "Co-Sponsor"
    lbl_sponsor_gold = "Nhà tài trợ vàng" if is_vi else "Gold Sponsor"
    lbl_academic = "Đối tác học thuật" if is_vi else "Academic Partner"
    lbl_support = "Đơn vị hỗ trợ" if is_vi else "Supporting Partners"
    lbl_media = "Đối tác truyền thông" if is_vi else "Media Partners"

    guide_class = "guides" if show_guides else ""

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_plate}');
        background-size: cover;
        background-position: 72% center;
        filter: brightness(1.18) contrast(1.1) saturate(1.22);
      }}
      .aurora-wash {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient(850px 700px at 78% 35%, rgba(155,77,255,0.42) 0%, rgba(36,91,255,0.28) 48%, transparent 80%),
          radial-gradient(700px 550px at 20% 50%, rgba(107,45,155,0.38) 0%, transparent 75%),
          radial-gradient(550px 400px at 50% 15%, rgba(233,213,255,0.22) 0%, transparent 70%);
      }}
      .dragon-bridge-layer {{
        position: absolute; bottom: {220 if h==1350 else 320}px; left: -180px; width: 1440px; pointer-events: none;
        opacity: 0.72;
      }}
      .readability-gradient {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(180deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.3) 15%, transparent 35%, rgba(7,13,32,0.55) 70%, rgba(7,13,32,0.95) 100%),
          linear-gradient(90deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.5) 45%, transparent 75%);
      }}
      .container {{
        position: absolute; inset: 48px 52px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .top-band {{
        display: flex; justify-content: space-between; align-items: flex-start;
        padding-bottom: 20px; border-bottom: 1px solid rgba(233,213,255,0.22);
      }}
      .slot-cap {{
        font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600;
        color: rgba(233,213,255,0.75); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 8px;
      }}
      .slot-box {{
        display: flex; align-items: center; min-height: 44px;
      }}
      .slot-box img {{
        max-height: 48px; width: auto; display: block;
      }}
      .guides .slot-box {{
        outline: 1px dashed rgba(99,180,255,0.7); outline-offset: 4px;
        color: rgba(99,180,255,0.9); font-size: 10px; font-family: 'Space Grotesk', monospace;
      }}
      .title-hero {{
        margin-top: auto; margin-bottom: auto; padding-top: 30px;
      }}
      .eyebrow {{
        font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 26px;
        letter-spacing: 0.42em; color: #E9D5FF; text-shadow: 0 0 20px rgba(155,77,255,0.85); margin-bottom: 4px;
      }}
      .main-row {{
        display: flex; align-items: baseline; gap: 18px; white-space: nowrap;
      }}
      .t-ma {{
        font-weight: 800; font-size: 108px; line-height: 0.92; letter-spacing: -0.03em; color: #FFFFFF;
        text-shadow: 0 0 28px rgba(155,77,255,0.65), 0 0 54px rgba(36,91,255,0.55);
      }}
      .t-year {{
        font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 96px; line-height: 0.92;
        color: transparent; -webkit-text-stroke: 2px #E9D5FF;
        filter: drop-shadow(0 0 16px rgba(155,77,255,0.85));
      }}
      .t-region {{
        font-weight: 800; font-size: 72px; line-height: 1.05; letter-spacing: -0.015em;
        background: linear-gradient(90deg, #FFFFFF 0%, #F3E8FF 48%, #93C5FD 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 26px rgba(155,77,255,0.75)); margin-top: 2px;
      }}
      .theme-strip {{
        margin-top: 24px; display: flex; flex-direction: column; gap: 6px;
      }}
      .theme-sub {{
        display: flex; align-items: center; gap: 14px;
        font-family: 'Space Grotesk', sans-serif; font-size: 16px; font-weight: 600; color: #C084FC; letter-spacing: 0.16em; text-transform: uppercase;
      }}
      .theme-sub::before {{
        content: ""; width: 38px; height: 2px; background: linear-gradient(90deg, #9B4DFF, #63B4FF);
        box-shadow: 0 0 10px #9B4DFF;
      }}
      .theme-main {{
        font-weight: 800; font-size: 28px; letter-spacing: 0.04em; color: #FFFFFF;
        text-shadow: 0 0 20px rgba(155,77,255,0.6);
      }}
      .bottom-band {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-top: 20px; border-top: 1px solid rgba(233,213,255,0.22);
      }}
      .logistics {{
        display: flex; gap: 26px; white-space: nowrap;
      }}
      .log-item small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600;
        color: #63B4FF; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 3px;
      }}
      .log-item b {{
        display: block; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 20px; color: #FFFFFF;
      }}
    </style></head><body class="{guide_class}">
      <div class="plate-bg"></div>
      <div class="aurora-wash"></div>
      <div class="dragon-bridge-layer">
        {get_dragon_bridge_svg(w=1440, h=300, opacity=0.75)}
      </div>
      <div class="readability-gradient"></div>

      <div class="container">
        <!-- Top Logo Slots (Frameless, clean) -->
        <div class="top-band">
          <div>
            <div class="slot-cap">{lbl_org}</div>
            <div class="slot-box">
              <img src="{u_logo}" alt="VMAA Logo"/>
            </div>
          </div>
          <div>
            <div class="slot-cap">{lbl_sponsor_main}</div>
            <div class="slot-box" data-slot="sponsor-main">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; color:#60A5FA;">[NHÀ TÀI TRỢ ĐỒNG HÀNH]</span>
            </div>
          </div>
          <div>
            <div class="slot-cap">{lbl_sponsor_gold}</div>
            <div class="slot-box" data-slot="sponsor-gold">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; color:#FDE047;">[NHÀ TÀI TRỢ VÀNG]</span>
            </div>
          </div>
        </div>

        <!-- Hero Typography (Unboxed, pure typography, diacritic-safe) -->
        <div class="title-hero">
          <div class="eyebrow">{title_eyebrow}</div>
          <div class="main-row">
            <span class="t-ma">{title_main}</span>
            <span class="t-year">2026</span>
          </div>
          <div class="t-region">{title_region}</div>

          <div class="theme-strip">
            <div class="theme-sub">{theme_concept}</div>
            <div class="theme-main">{theme_sector}</div>
          </div>
        </div>

        <!-- Bottom Logistics & Partner Bands -->
        <div class="bottom-band">
          <div class="logistics">
            <div class="log-item">
              <small>{lbl_date}</small>
              <b>13.12.2026</b>
            </div>
            <div class="log-item">
              <small>{lbl_time}</small>
              <b>13:30–17:30</b>
            </div>
            <div class="log-item">
              <small>{lbl_venue}</small>
              <b>Đà Nẵng, Việt Nam</b>
            </div>
          </div>

          <div>
            <div class="slot-cap" style="text-align:right;">{lbl_support}</div>
            <div class="slot-box" style="justify-content:flex-end;">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:600; color:#E9D5FF;">VMAA CENTRAL CHAPTER</span>
            </div>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 2. KEY VISUAL LANDSCAPE MASTER & 32:9 CURVED LED STAGE
# =========================================================================
def build_landscape_kv_html(w=1920, h=1080, lang="vi", show_guides=False):
    is_vi = (lang == "vi")
    title_eyebrow = "DIỄN ĐÀN" if is_vi else "FORUM"
    title_main = "M&A"
    title_region = "MIỀN TRUNG" if is_vi else "CENTRAL VIETNAM"
    theme_concept = "Kiến trúc giá trị" if is_vi else "Architecture of value"
    theme_sector = "Bất động sản × Công nghệ" if is_vi else "Real Estate — Technology"
    lbl_date = "Ngày" if is_vi else "Date"
    lbl_time = "Giờ" if is_vi else "Time"
    lbl_venue = "Địa điểm" if is_vi else "Location"
    lbl_org = "Đơn vị tổ chức" if is_vi else "Organized by"
    lbl_sponsor_main = "Nhà tài trợ đồng hành" if is_vi else "Co-Sponsor"
    lbl_sponsor_gold = "Nhà tài trợ vàng" if is_vi else "Gold Sponsor"
    lbl_academic = "Đối tác học thuật" if is_vi else "Academic Partner"
    lbl_support = "Đơn vị hỗ trợ" if is_vi else "Supporting Partners"
    lbl_media = "Đối tác truyền thông" if is_vi else "Media Partners"

    guide_class = "guides" if show_guides else ""

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_plate}');
        background-size: cover; background-position: 72% center;
        filter: brightness(1.18) contrast(1.1) saturate(1.22);
      }}
      .aurora-wash {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient(960px 750px at 74% 45%, rgba(155,77,255,0.40) 0%, rgba(36,91,255,0.25) 50%, transparent 80%),
          radial-gradient(750px 580px at 24% 48%, rgba(107,45,155,0.32) 0%, transparent 75%),
          radial-gradient(600px 420px at 60% 18%, rgba(233,213,255,0.24) 0%, transparent 70%);
      }}
      .dragon-bridge-layer {{
        position: absolute; bottom: 120px; left: 0; right: 0; pointer-events: none;
        opacity: 0.85;
      }}
      .readability-gradient {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(90deg, rgba(7,11,28,0.85) 0%, rgba(12,16,42,0.60) 36%, rgba(18,14,48,0.22) 52%, transparent 68%),
          linear-gradient(180deg, rgba(7,13,32,0.80) 0%, transparent 20%, transparent 78%, rgba(7,13,32,0.92) 100%);
      }}
      .container {{
        position: absolute; inset: 48px 74px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .top-band {{
        display: flex; justify-content: space-between; align-items: flex-start;
        padding-bottom: 20px; border-bottom: 1px solid rgba(233,213,255,0.24);
      }}
      .slot-cap {{
        font-family: 'Space Grotesk', sans-serif; font-size: 12px; font-weight: 600;
        color: rgba(233,213,255,0.78); letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 10px;
      }}
      .slot-box {{
        display: flex; align-items: center; min-height: 52px;
      }}
      .slot-box img {{
        max-height: 56px; width: auto; display: block;
      }}
      .guides .slot-box {{
        outline: 1px dashed rgba(99,180,255,0.7); outline-offset: 4px;
        color: rgba(99,180,255,0.95); font-size: 11px; font-family: 'Space Grotesk', monospace;
      }}
      .title-hero {{
        margin-top: auto; margin-bottom: auto; max-width: 980px;
      }}
      .eyebrow {{
        font-family: 'Outfit', sans-serif; font-weight: 600; font-size: 34px;
        letter-spacing: 0.42em; color: #E9D5FF; text-shadow: 0 0 22px rgba(155,77,255,0.85); margin-bottom: 4px;
      }}
      .main-row {{
        display: flex; align-items: baseline; gap: 24px; white-space: nowrap;
      }}
      .t-ma {{
        font-weight: 800; font-size: 130px; line-height: 0.94; letter-spacing: -0.03em; color: #FFFFFF;
        text-shadow: 0 0 28px rgba(155,77,255,0.65), 0 0 64px rgba(36,91,255,0.55);
      }}
      .t-year {{
        font-family: 'Outfit', sans-serif; font-weight: 800; font-size: 116px; line-height: 0.94;
        color: transparent; -webkit-text-stroke: 2.2px #E9D5FF;
        filter: drop-shadow(0 0 18px rgba(155,77,255,0.85));
      }}
      .t-region {{
        font-weight: 800; font-size: 88px; line-height: 1.05; letter-spacing: -0.015em;
        background: linear-gradient(90deg, #FFFFFF 0%, #F3E8FF 48%, #93C5FD 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 30px rgba(155,77,255,0.75)); margin-top: 2px;
      }}
      .theme-strip {{
        margin-top: 26px; display: flex; align-items: center; gap: 20px;
      }}
      .theme-accent-line {{
        width: 64px; height: 3px; background: linear-gradient(90deg, #9B4DFF, #63B4FF);
        box-shadow: 0 0 12px #9B4DFF;
      }}
      .theme-text {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 30px; font-weight: 700; color: #F3E8FF;
        text-shadow: 0 0 20px rgba(155,77,255,0.6);
      }}
      .bottom-band {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-top: 22px; border-top: 1px solid rgba(233,213,255,0.24);
      }}
      .logistics {{
        display: flex; gap: 48px; white-space: nowrap;
      }}
      .log-item small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: 12px; font-weight: 600;
        color: #63B4FF; letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 4px;
      }}
      .log-item b {{
        display: block; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 26px; color: #FFFFFF;
      }}
    </style></head><body class="{guide_class}">
      <div class="plate-bg"></div>
      <div class="aurora-wash"></div>
      <div class="dragon-bridge-layer">
        {get_dragon_bridge_svg(w=1920, h=380, opacity=0.85)}
      </div>
      <div class="readability-gradient"></div>

      <div class="container">
        <!-- Top Logo Slots -->
        <div class="top-band">
          <div style="width:330px;">
            <div class="slot-cap">{lbl_org}</div>
            <div class="slot-box">
              <img src="{u_logo}" alt="VMAA Logo"/>
            </div>
          </div>
          <div style="flex:1;">
            <div class="slot-cap">{lbl_sponsor_main}</div>
            <div class="slot-box" data-slot="sponsor-main">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:13px; font-weight:700; color:#60A5FA;">[NHÀ TÀI TRỢ ĐỒNG HÀNH · 440×64]</span>
            </div>
          </div>
          <div style="flex:1;">
            <div class="slot-cap">{lbl_sponsor_gold}</div>
            <div class="slot-box" data-slot="sponsor-gold">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:13px; font-weight:700; color:#FDE047;">[NHÀ TÀI TRỢ VÀNG · 440×64]</span>
            </div>
          </div>
          <div style="flex:1;">
            <div class="slot-cap">{lbl_academic}</div>
            <div class="slot-box" data-slot="academic">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:13px; font-weight:700; color:#F87171;">[ĐỐI TÁC HỌC THUẬT · DUE]</span>
            </div>
          </div>
        </div>

        <!-- Hero Typography -->
        <div class="title-hero">
          <div class="eyebrow">{title_eyebrow}</div>
          <div class="main-row">
            <span class="t-ma">{title_main}</span>
            <span class="t-year">2026</span>
          </div>
          <div class="t-region">{title_region}</div>

          <div class="theme-strip">
            <div class="theme-accent-line"></div>
            <div class="theme-text">
              <span style="color:#C084FC; font-weight:600;">{theme_concept}:</span> {theme_sector}
            </div>
          </div>
        </div>

        <!-- Bottom Logistics & Partner Bands -->
        <div class="bottom-band">
          <div class="logistics">
            <div class="log-item">
              <small>{lbl_date}</small>
              <b>13.12.2026</b>
            </div>
            <div class="log-item">
              <small>{lbl_time}</small>
              <b>13:30–17:30</b>
            </div>
            <div class="log-item">
              <small>{lbl_venue}</small>
              <b>Đà Nẵng, Việt Nam</b>
            </div>
          </div>

          <div style="display:flex; gap:36px;">
            <div>
              <div class="slot-cap">{lbl_support}</div>
              <div class="slot-box" data-slot="support">
                <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:600; color:#E9D5FF;">HIỆP HỘI DN ĐÀ NẴNG · CLB BĐS</span>
              </div>
            </div>
            <div>
              <div class="slot-cap">{lbl_media}</div>
              <div class="slot-box" data-slot="media">
                <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; color:#38BDF8;">CAFEF · VCCORP · FORBES VIETNAM</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 3. SIX DISTINCT SOCIAL-MEDIA DESIGNS (ALL RATIOS)
# =========================================================================
def build_social_post_html(post_id: int, w: int, h: int, lang="vi"):
    is_vi = (lang == "vi")

    # Common background elements
    bg_style = f"background-image:url('{u_plate}'); background-size:cover; background-position:center;"
    if post_id in (2, 4):
        bg_style = f"background-image:url('{u_prism}'); background-size:cover; background-position:center;"

    # Content configurations for each of the 6 distinct post types
    if post_id == 1:
        # 01. Official Event Announcement
        tag = "OFFICIAL ANNOUNCEMENT" if not is_vi else "CÔNG BỐ CHÍNH THỨC"
        headline = "DIỄN ĐÀN M&A MIỀN TRUNG 2026" if is_vi else "CENTRAL VIETNAM M&A FORUM 2026"
        subhead = "Kiến trúc giá trị: Bất động sản × Công nghệ" if is_vi else "Architecture of Value: Real Estate × Technology"
        body = "Sự kiện thượng đỉnh quy tụ 1,500+ nhà lãnh đạo, tập đoàn kinh tế và các quỹ đầu tư quốc tế hàng đầu tại Đà Nẵng." if is_vi else "The premier summit convening 1,500+ leaders, conglomerates and top PE funds in Da Nang."
        cta = "ĐĂNG KÝ THAM DỰ VIP ↗" if is_vi else "REGISTER VIP PASS ↗"
    elif post_id == 2:
        # 02. Real Estate × Technology Concept
        tag = "THEMATIC CONCEPT" if not is_vi else "Ý NIỆM CHỦ ĐỀ"
        headline = "KIẾN TRÚC GIÁ TRỊ" if is_vi else "ARCHITECTURE OF VALUE"
        subhead = "Sự hội tụ chiến lược giữa Bất động sản & Công nghệ" if is_vi else "Strategic convergence of Real Estate & Technology"
        body = "Tái cấu trúc dòng vốn, định giá PropTech và tối ưu hóa danh mục tài sản thông qua sức mạnh dữ liệu số." if is_vi else "Capital restructuring, PropTech valuation, and asset portfolio optimization powered by digital infrastructure."
        cta = "KHÁM PHÁ Ý NIỆM ↗" if is_vi else "EXPLORE CONCEPT ↗"
    elif post_id == 3:
        # 03. Real Estate Thematic Post
        tag = "SECTOR INSIGHT: REAL ESTATE" if not is_vi else "TIÊU ĐIỂM BẤT ĐỘNG SẢN"
        headline = "TÁI CẤU TRÚC QUỸ ĐẤT & DÒNG VỐN CHIẾN LƯỢC" if is_vi else "LAND BANK RESTRUCTURING & CAPITAL INFLOWS"
        subhead = "Cơ hội M&A Bất động sản nghỉ dưỡng & công nghiệp Miền Trung" if is_vi else "M&A opportunities in Central Vietnam hospitality & industrial assets"
        body = "Phân tích biến động pháp lý, mở rộng quỹ đất và các thương vụ hợp tác chiến lược đón đầu chu kỳ phục hồi 2026–2030." if is_vi else "Analyzing regulatory shifts, land expansion, and strategic partnerships for the 2026–2030 growth cycle."
        cta = "XEM BÁO CÁO M&A ↗" if is_vi else "VIEW M&A REPORT ↗"
    elif post_id == 4:
        # 04. Technology Thematic Post
        tag = "SECTOR INSIGHT: TECHNOLOGY" if not is_vi else "TIÊU ĐIỂM CÔNG NGHỆ"
        headline = "PROPTECH & AI ĐỊNH GIÁ TÀI SẢN DOANH NGHIỆP" if is_vi else "PROPTECH & AI-DRIVEN ENTERPRISE VALUATION"
        subhead = "Công nghệ nâng tầm giá trị thương vụ M&A" if is_vi else "Technology elevating M&A transaction certainty"
        body = "Ứng dụng mô hình AI thẩm định giá tài sản, chuyển đổi số và nâng cao biên lợi nhuận cho các dự án quy mô lớn." if is_vi else "Deploying AI asset valuation, digital transformation, and margin optimization for mega projects."
        cta = "XEM GIẢI PHÁP TECH ↗" if is_vi else "VIEW TECH SUITE ↗"
    elif post_id == 5:
        # 05. Guest / Panelist Announcement
        tag = "KEYNOTE SPEAKER SPOTLIGHT" if not is_vi else "DIỄN GIẢ TIÊU BIỂU"
        headline = "TS. NGUYỄN VĂN A" if is_vi else "DR. NGUYEN VAN A"
        subhead = "Chủ tịch HĐQT / Managing Partner · Quỹ Đầu tư Quốc tế" if is_vi else "Chairman & Managing Partner · Global Investment Fund"
        body = "Chuyên đề: 'Kiến trúc Giá trị Mới & Xu hướng Định giá Bất động sản Công nghệ tại Miền Trung 2026'." if is_vi else "Topic: 'New Architecture of Value & PropTech Valuation Trends in Central Vietnam 2026'."
        cta = "GẶP GỠ DIỄN GIẢ ↗" if is_vi else "MEET THE SPEAKER ↗"
    else:
        # 06. Event Details and Registration CTA
        tag = "EVENT AGENDA & DEAL ROOM" if not is_vi else "LỊCH TRÌNH & ĐĂNG KÝ"
        headline = "13.12.2026 · 13:30–17:30"
        subhead = "Ariyana Convention Centre · Đà Nẵng, Việt Nam"
        body = "Chương trình gồm 3 phiên tọa đàm chiến lược, lễ ký kết thương vụ MOU và phòng Deal Room kết nối đầu tư 1:1." if is_vi else "Featuring 3 strategic plenary sessions, MOU deal signings, and 1:1 institutional deal rooms."
        cta = "ĐĂNG KÝ VÉ SỚM VIP ↗" if is_vi else "SECURE EARLY VIP PASS ↗"

    scale_factor = min(w / 1080.0, h / 1350.0)

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        position: relative; overflow: hidden;
      }}
      .plate-layer {{
        position: absolute; inset: 0; {bg_style}
        filter: brightness(1.15) contrast(1.1) saturate(1.2);
      }}
      .aurora-layer {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient({int(w*0.8)}px {int(h*0.6)}px at 75% 35%, rgba(155,77,255,0.42) 0%, rgba(36,91,255,0.25) 50%, transparent 80%),
          radial-gradient({int(w*0.6)}px {int(h*0.5)}px at 20% 50%, rgba(107,45,155,0.35) 0%, transparent 75%);
      }}
      .shade-layer {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(180deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.4) 30%, rgba(7,13,32,0.6) 65%, rgba(7,13,32,0.95) 100%),
          linear-gradient(90deg, rgba(7,13,32,0.75) 0%, transparent 60%);
      }}
      .content {{
        position: absolute; inset: {int(44*scale_factor)}px {int(48*scale_factor)}px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .tag-pill {{
        display: inline-flex; align-items: center; gap: 8px;
        padding: {int(6*scale_factor)}px {int(16*scale_factor)}px;
        background: rgba(155,77,255,0.25); border: 1px solid rgba(233,213,255,0.45);
        font-family: 'Space Grotesk', monospace; font-size: {int(12*scale_factor)}px; font-weight: 700;
        color: #E9D5FF; letter-spacing: 0.16em; text-transform: uppercase;
      }}
      .cta-btn {{
        display: inline-flex; align-items: center; gap: 10px;
        padding: {int(14*scale_factor)}px {int(28*scale_factor)}px;
        background: linear-gradient(90deg, #9B4DFF, #245BFF);
        font-family: 'Space Grotesk', sans-serif; font-size: {int(15*scale_factor)}px; font-weight: 700;
        color: #FFFFFF; letter-spacing: 0.12em; text-transform: uppercase;
        box-shadow: 0 0 24px rgba(155,77,255,0.5); border: 1px solid #FFFFFF;
      }}
    </style></head><body>
      <div class="plate-layer"></div>
      <div class="aurora-layer"></div>
      <div class="shade-layer"></div>

      <div class="content">
        <!-- Top Lockup -->
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo}" alt="VMAA Logo" style="height:{int(42*scale_factor)}px; width:auto;"/>
          <div class="tag-pill">{tag}</div>
        </div>

        <!-- Middle Hero Message -->
        <div style="margin:auto 0; max-width:{int(w*0.88)}px;">
          <div style="font-family:'Space Grotesk',sans-serif; font-size:{int(18*scale_factor)}px; font-weight:700; color:#63B4FF; letter-spacing:0.18em; text-transform:uppercase; margin-bottom:{int(10*scale_factor)}px;">
            VMAA · CENTRAL VIETNAM 2026
          </div>
          <h1 style="font-family:'Plus Jakarta Sans',sans-serif; font-size:{int(48*scale_factor)}px; font-weight:800; line-height:1.12; color:#FFFFFF; text-shadow:0 0 24px rgba(155,77,255,0.7); margin-bottom:{int(14*scale_factor)}px;">
            {headline}
          </h1>
          <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:{int(22*scale_factor)}px; font-weight:600; color:#E9D5FF; line-height:1.3; margin-bottom:{int(16*scale_factor)}px;">
            {subhead}
          </div>
          <div style="font-family:'Inter',sans-serif; font-size:{int(15*scale_factor)}px; font-weight:400; color:rgba(233,213,255,0.85); line-height:1.55; max-width:{int(w*0.8)}px; margin-bottom:{int(26*scale_factor)}px;">
            {body}
          </div>
          <div>
            <span class="cta-btn">{cta}</span>
          </div>
        </div>

        <!-- Bottom Event Stamp -->
        <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-top:{int(16*scale_factor)}px; border-top:1px solid rgba(233,213,255,0.2);">
          <div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:{int(11*scale_factor)}px; color:#63B4FF; letter-spacing:0.14em; text-transform:uppercase;">
              THỜI GIAN &amp; ĐỊA ĐIỂM
            </div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:700; font-size:{int(16*scale_factor)}px; color:#FFFFFF; margin-top:2px;">
              13.12.2026 · 13:30–17:30 · Đà Nẵng, Việt Nam
            </div>
          </div>
          <div style="font-family:'Space Grotesk',sans-serif; font-size:{int(12*scale_factor)}px; font-weight:700; color:#C084FC; letter-spacing:0.18em;">
            POST #{post_id:02d}
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 4. CHOREOGRAPHED LOWER-THIRD & GUEST INVITATION SYSTEM
# =========================================================================
def build_guest_lower_third_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: 1920px; height: 1080px;
        background: transparent;
      }}
      /* Choreographed Nameplate Architecture */
      .lower-third-wrap {{
        position: absolute; bottom: 90px; left: 100px;
        display: flex; align-items: stretch;
        z-index: 100;
      }}
      .accent-pillar {{
        width: 8px; background: linear-gradient(180deg, #9B4DFF, #245BFF);
        box-shadow: 0 0 18px #9B4DFF;
      }}
      .glass-card {{
        background: linear-gradient(90deg, rgba(7,13,32,0.96) 0%, rgba(18,24,56,0.90) 65%, rgba(107,45,155,0.85) 100%);
        border: 1px solid rgba(233,213,255,0.3);
        border-left: none;
        padding: 24px 44px;
        min-width: 780px;
        box-shadow: 0 24px 60px rgba(0,0,0,0.85), 0 0 35px rgba(155,77,255,0.3);
        position: relative;
        overflow: hidden;
      }}
      .sweep-light {{
        position: absolute; top: 0; bottom: 0; width: 120px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
        transform: skewX(-25deg);
        animation: sweep 4s infinite ease-in-out;
      }}
      @keyframes sweep {{
        0% {{ left: -150px; opacity: 0; }}
        20% {{ opacity: 1; }}
        60% {{ left: 950px; opacity: 0; }}
        100% {{ left: 950px; opacity: 0; }}
      }}
      .guest-session {{
        font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 700;
        color: #63B4FF; letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 6px;
      }}
      .guest-name {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 42px; font-weight: 800;
        color: #FFFFFF; letter-spacing: -0.01em; text-shadow: 0 0 24px rgba(155,77,255,0.7);
      }}
      .guest-title {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 18px; font-weight: 600;
        color: #E9D5FF; margin-top: 4px;
      }}
      .guest-org {{
        font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 500;
        color: rgba(233,213,255,0.8); margin-top: 2px;
      }}
      .event-tag {{
        display: flex; align-items: center; gap: 14px; margin-top: 14px; padding-top: 10px;
        border-top: 1px solid rgba(233,213,255,0.25);
        font-family: 'Space Grotesk', monospace; font-size: 11px; font-weight: 600; color: #C084FC;
      }}
    </style></head><body>
      <div class="lower-third-wrap">
        <div class="accent-pillar"></div>
        <div class="glass-card">
          <div class="sweep-light"></div>
          <div class="guest-session">TỌA ĐÀM CẤP CAO // BẤT ĐỘNG SẢN &amp; CÔNG NGHỆ</div>
          <div class="guest-name">TS. TRẦN ĐÌNH THIÊN</div>
          <div class="guest-title">Nguyên Viện trưởng Viện Kinh tế Việt Nam</div>
          <div class="guest-org">Chuyên gia Cố vấn Kinh tế Vĩ mô &amp; Tái cấu trúc M&amp;A</div>
          <div class="event-tag">
            <img src="{u_wordmark}" alt="VMAA" style="height:18px; width:auto;"/>
            <span>DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · 13.12.2026 · ĐÀ NẴNG</span>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 5. ASYNC PLAYWRIGHT BATCH RENDERER
# =========================================================================
async def run_production():
    print("[INIT] Starting VMAA Visual Identity & Motion v2 Production Suite...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--force-color-profile=srgb"])

        # -------------------------------------------------------------
        # 1. RENDER KEY VISUAL PORTRAIT MASTERS (1080x1350 & 1080x1920)
        # -------------------------------------------------------------
        print("\n--- 1. Render Key Visual Portrait Masters ---")
        for lang in ("vi", "en"):
            # 1080x1350 Feed
            h_feed = build_portrait_kv_html(1080, 1350, lang=lang, show_guides=False)
            feed_file = EXPORTS_DIR / f"KV_v2_Portrait_1080x1350_{lang.upper()}.html"
            feed_png = EXPORTS_DIR / f"KV_v2_Portrait_1080x1350_{lang.upper()}.png"
            feed_file.write_text(h_feed, encoding="utf-8")
            pg = await browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
            await pg.goto(feed_file.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(600)
            await pg.screenshot(path=str(feed_png))
            await pg.close()
            shutil.copy(feed_png, BRAIN_DIR / feed_png.name)
            print(f"Rendered {feed_png.name} (2160x2700 @2x)")

            # 1080x1920 Story / Vertical
            h_story = build_portrait_kv_html(1080, 1920, lang=lang, show_guides=False)
            story_file = EXPORTS_DIR / f"KV_v2_Portrait_1080x1920_{lang.upper()}.html"
            story_png = EXPORTS_DIR / f"KV_v2_Portrait_1080x1920_{lang.upper()}.png"
            story_file.write_text(h_story, encoding="utf-8")
            pg = await browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
            await pg.goto(story_file.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(600)
            await pg.screenshot(path=str(story_png))
            await pg.close()
            shutil.copy(story_png, BRAIN_DIR / story_png.name)
            print(f"Rendered {story_png.name} (2160x3840 @2x)")

        # -------------------------------------------------------------
        # 2. RENDER KEY VISUAL LANDSCAPE & 32:9 STAGE
        # -------------------------------------------------------------
        print("\n--- 2. Render Key Visual Landscape & 32:9 Stage ---")
        for lang in ("vi", "en"):
            h_land = build_landscape_kv_html(1920, 1080, lang=lang, show_guides=False)
            land_file = EXPORTS_DIR / f"KV_v2_Landscape_1920x1080_{lang.upper()}.html"
            land_png = EXPORTS_DIR / f"KV_v2_Landscape_1920x1080_{lang.upper()}.png"
            land_file.write_text(h_land, encoding="utf-8")
            pg = await browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
            await pg.goto(land_file.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(600)
            await pg.screenshot(path=str(land_png))
            await pg.close()
            shutil.copy(land_png, BRAIN_DIR / land_png.name)
            print(f"Rendered {land_png.name} (3840x2160 4K UHD)")

        # -------------------------------------------------------------
        # 3. RENDER 6 DISTINCT SOCIAL MEDIA DESIGNS (ALL 7 RATIOS)
        # -------------------------------------------------------------
        print("\n--- 3. Render 6 Distinct Social Media Designs ---")
        ratios = [
            ("1080x1350", 1080, 1350),
            ("1080x1080", 1080, 1080),
            ("1080x1920", 1080, 1920),
            ("1200x1500", 1200, 1500),
            ("1200x1200", 1200, 1200),
            ("1600x900", 1600, 900),
            ("1920x1080", 1920, 1080),
        ]

        social_pg = await browser.new_page()
        for post_idx in range(1, 7):
            for r_name, r_w, r_h in ratios:
                h_post = build_social_post_html(post_idx, r_w, r_h, lang="vi")
                out_html = SOCIAL_DIR / f"POST_{post_idx:02d}_{r_name}.html"
                out_png = SOCIAL_DIR / f"POST_{post_idx:02d}_{r_name}.png"
                out_html.write_text(h_post, encoding="utf-8")
                await social_pg.set_viewport_size({"width": r_w, "height": r_h})
                await social_pg.goto(out_html.as_uri(), wait_until="load")
                await social_pg.wait_for_timeout(150)
                await social_pg.screenshot(path=str(out_png), timeout=10000)
            print(f"Exported Post #{post_idx:02d} in all 7 platform aspect ratios!")
        await social_pg.close()

        # -------------------------------------------------------------
        # 4. RENDER GUEST LOWER-THIRD & INVITATION MOTION
        # -------------------------------------------------------------
        print("\n--- 4. Render Guest Lower-Third & Motion Assets ---")
        lt_html = build_guest_lower_third_html()
        lt_file = GUESTS_DIR / "VMAA_Guest_LowerThird_Master.html"
        lt_png = GUESTS_DIR / "VMAA_Guest_LowerThird_Master.png"
        lt_file.write_text(lt_html, encoding="utf-8")
        pg = await browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        await pg.goto(lt_file.as_uri(), wait_until="networkidle")
        await pg.wait_for_timeout(500)
        await pg.screenshot(path=str(lt_png))
        await pg.close()
        shutil.copy(lt_png, BRAIN_DIR / lt_png.name)
        print("Rendered VMAA_Guest_LowerThird_Master.png (3840x2160 4K)")

        await browser.close()

    print("\n[SUCCESS] Completed VMAA Visual Identity & Motion v2 Production Suite!")


if __name__ == "__main__":
    asyncio.run(run_production())
