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
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
SOCIAL_DIR = EXPORTS_DIR / "social_media"
SOCIAL_DIR.mkdir(parents=True, exist_ok=True)
GUESTS_DIR = EXPORTS_DIR / "guests_motion"
GUESTS_DIR.mkdir(parents=True, exist_ok=True)
STAGE_DIR = EXPORTS_DIR / "stage_venue"
STAGE_DIR.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


# Approved User Assets
u_guest_bg = to_data_uri(PLATES_DIR / "guest_bg_crystal_fluted.jpg")
u_kv_bottom_4k = to_data_uri(PLATES_DIR / "kv_ref_bottom_4k.png")
u_kv_top_4k = to_data_uri(PLATES_DIR / "kv_ref_top_4k.png")
u_prism = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u_cantilever = to_data_uri(PLATES_DIR / "opt_ascending_cantilevers.png")
u_logo = to_data_uri(ASSETS_DIR / "vmaa_logo_white_transparent.png")
u_wordmark = to_data_uri(ASSETS_DIR / "vmaa_wordmark_white_transparent.png")

TYPO_CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=Outfit:wght@400;600;800&family=Unbounded:wght@700;800&display=swap" rel="stylesheet">
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


def get_dragon_bridge_svg(w=1920, h=300, opacity=0.75):
    return f"""
    <svg width="{w}" height="{h}" viewBox="0 0 1920 300" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:{opacity}; mix-blend-mode:screen; pointer-events:none;">
      <defs>
        <linearGradient id="db_arch_grad" x1="0" y1="0" x2="1920" y2="0" gradientUnits="userSpaceOnUse">
          <stop offset="10%" stop-color="#D97706" stop-opacity="0.3"/>
          <stop offset="35%" stop-color="#F59E0B" stop-opacity="0.95"/>
          <stop offset="60%" stop-color="#FDE047" stop-opacity="0.9"/>
          <stop offset="85%" stop-color="#245BFF" stop-opacity="0.75"/>
          <stop offset="100%" stop-color="#63B4FF" stop-opacity="0.3"/>
        </linearGradient>
        <filter id="db_glow_f" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="5" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      <!-- Han River Waterline & Shimmer -->
      <line x1="0" y1="230" x2="1920" y2="230" stroke="rgba(99,180,255,0.4)" stroke-width="1.2" stroke-dasharray="10 5"/>
      <rect x="250" y="232" width="1420" height="65" fill="rgba(36,91,255,0.15)"/>

      <!-- 5 Undulating Steel Arches of Dragon Bridge (Cầu Rồng Đà Nẵng) -->
      <g filter="url(#db_glow_f)">
        <path d="M 320 230 Q 420 160, 520 230" stroke="url(#db_arch_grad)" stroke-width="4" fill="none" stroke-linecap="round"/>
        <path d="M 520 230 Q 640 120, 760 230" stroke="url(#db_arch_grad)" stroke-width="5" fill="none" stroke-linecap="round"/>
        <path d="M 760 230 Q 900 80, 1040 230" stroke="url(#db_arch_grad)" stroke-width="6" fill="none" stroke-linecap="round"/>
        <path d="M 1040 230 Q 1160 125, 1280 230" stroke="url(#db_arch_grad)" stroke-width="5" fill="none" stroke-linecap="round"/>
        <path d="M 1280 230 Q 1380 165, 1460 230" stroke="url(#db_arch_grad)" stroke-width="4" fill="none" stroke-linecap="round"/>

        <!-- Stylized Dragon Head & Mouth facing sea -->
        <path d="M 1440 185 C 1465 175, 1485 185, 1500 180 C 1485 193, 1480 205, 1460 210 Z" fill="#F59E0B" opacity="0.95"/>
        <circle cx="1500" cy="180" r="3.5" fill="#FFFFFF"/>
        <path d="M 1500 180 Q 1540 173, 1570 177" stroke="#FDE047" stroke-width="2.5" stroke-dasharray="3 3"/>
      </g>
    </svg>
    """


# =========================================================================
# 1. PRIMARY KEY VISUAL LANDSCAPE (1920x1080 -> 4K 3840x2160)
# =========================================================================
def build_primary_landscape_kv_html(w=1920, h=1080, lang="vi"):
    is_vi = (lang == "vi")
    title_eyebrow = "D I Ễ N   Đ À N" if is_vi else "F O R U M"
    title_main = "M&A"
    title_region = "MIỀN TRUNG" if is_vi else "CENTRAL VIETNAM"
    theme_concept = "—— Kiến trúc giá trị" if is_vi else "—— Architecture of value"
    theme_sector = "BẤT ĐỘNG SẢN × CÔNG NGHỆ" if is_vi else "REAL ESTATE × TECHNOLOGY"
    lbl_date = "Ngày" if is_vi else "Date"
    lbl_time = "Giờ" if is_vi else "Time"
    lbl_venue = "Địa điểm" if is_vi else "Location"
    lbl_org = "Đơn vị tổ chức" if is_vi else "Organized by"
    lbl_sponsor_main = "Nhà tài trợ đồng hành" if is_vi else "Co-Sponsor"
    lbl_sponsor_gold = "Nhà tài trợ vàng" if is_vi else "Gold Sponsor"
    lbl_academic = "Đối tác học thuật" if is_vi else "Academic Partner"
    lbl_support = "Đơn vị hỗ trợ" if is_vi else "Supporting Partners"
    lbl_media = "Đối tác truyền thông" if is_vi else "Media Partners"

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_kv_bottom_4k}');
        background-size: cover; background-position: center;
        filter: brightness(1.08) contrast(1.05);
      }}
      .aurora-accent {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient(850px 650px at 75% 42%, rgba(155,77,255,0.35) 0%, rgba(36,91,255,0.20) 45%, transparent 75%),
          radial-gradient(650px 500px at 22% 48%, rgba(107,45,155,0.28) 0%, transparent 70%);
      }}
      .dragon-bridge-layer {{
        position: absolute; bottom: 80px; left: 0; right: 0; pointer-events: none;
        opacity: 0.65;
      }}
      .vignette-readability {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(90deg, rgba(7,11,28,0.85) 0%, rgba(10,16,40,0.60) 36%, rgba(14,16,45,0.20) 54%, transparent 72%),
          linear-gradient(180deg, rgba(7,13,32,0.82) 0%, transparent 18%, transparent 80%, rgba(7,13,32,0.92) 100%);
      }}
      .container {{
        position: absolute; inset: 44px 72px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .top-band {{
        display: flex; justify-content: space-between; align-items: flex-start;
        padding-bottom: 16px; border-bottom: 1px solid rgba(233,213,255,0.22);
      }}
      .slot-cap {{
        font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600;
        color: rgba(233,213,255,0.78); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 8px;
      }}
      .slot-box {{
        display: flex; align-items: center; min-height: 48px;
      }}
      .slot-box img {{
        max-height: 52px; width: auto; display: block;
      }}
      .title-hero {{
        margin-top: auto; margin-bottom: auto; max-width: 980px; padding-left: 6px;
      }}
      .eyebrow {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600; font-size: 26px;
        letter-spacing: 0.38em; color: #FFFFFF; text-shadow: 0 0 20px rgba(155,77,255,0.75); margin-bottom: 8px;
      }}
      .main-row {{
        display: flex; align-items: baseline; gap: 20px; white-space: nowrap; line-height: 0.92;
      }}
      .t-ma {{
        font-weight: 800; font-size: 132px; letter-spacing: -0.02em; color: #FFFFFF;
        text-shadow: 0 0 30px rgba(155,77,255,0.7), 0 0 60px rgba(36,91,255,0.6);
      }}
      .t-year {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 122px;
        color: transparent; -webkit-text-stroke: 2.4px #FFFFFF;
        filter: drop-shadow(0 0 16px rgba(155,77,255,0.8));
      }}
      .t-region {{
        font-weight: 800; font-size: 92px; line-height: 1.04; letter-spacing: -0.015em;
        background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 48%, #7DD3FC 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 28px rgba(155,77,255,0.7)); margin-top: 4px;
      }}
      .theme-strip {{
        margin-top: 26px; display: flex; flex-direction: column; gap: 4px;
      }}
      .theme-concept {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 24px; font-weight: 500;
        color: #E9D5FF; letter-spacing: 0.05em;
      }}
      .theme-sector {{
        font-weight: 800; font-size: 40px; letter-spacing: -0.01em; color: #FFFFFF;
        text-shadow: 0 0 24px rgba(155,77,255,0.65);
      }}
      .bottom-band {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-top: 18px; border-top: 1px solid rgba(233,213,255,0.22);
      }}
      .logistics {{
        display: flex; gap: 44px; white-space: nowrap;
      }}
      .log-item small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600;
        color: #63B4FF; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 3px;
      }}
      .log-item b {{
        display: block; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 24px; color: #FFFFFF;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="aurora-accent"></div>
      <div class="dragon-bridge-layer">
        {get_dragon_bridge_svg(w=1920, h=260, opacity=0.7)}
      </div>
      <div class="vignette-readability"></div>

      <div class="container">
        <!-- Top Partner / Sponsor Slots -->
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

        <!-- Hero Typography (Exact Unboxed Master Lockup) -->
        <div class="title-hero">
          <div class="eyebrow">{title_eyebrow}</div>
          <div class="main-row">
            <span class="t-ma">{title_main}</span>
            <span class="t-year">2026</span>
          </div>
          <div class="t-region">{title_region}</div>

          <div class="theme-strip">
            <div class="theme-concept">{theme_concept}</div>
            <div class="theme-sector">{theme_sector}</div>
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
                <span style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:600; color:#E9D5FF;">HIỆP HỘI DN ĐÀ NẴNG · CLB BĐS</span>
              </div>
            </div>
            <div>
              <div class="slot-cap">{lbl_media}</div>
              <div class="slot-box" data-slot="media">
                <span style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:700; color:#38BDF8;">CAFEF · VCCORP · FORBES VIETNAM</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 2. 32:9 CURVED LED STAGE WALL (3840x1080)
# =========================================================================
def build_curved_stage_32x9_html(w=3840, h=1080, lang="vi"):
    is_vi = (lang == "vi")
    title_eyebrow = "D I Ễ N   Đ À N" if is_vi else "F O R U M"
    title_main = "M&A"
    title_region = "MIỀN TRUNG" if is_vi else "CENTRAL VIETNAM"
    theme_concept = "—— Kiến trúc giá trị" if is_vi else "—— Architecture of value"
    theme_sector = "BẤT ĐỘNG SẢN × CÔNG NGHỆ" if is_vi else "REAL ESTATE × TECHNOLOGY"

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_kv_bottom_4k}');
        background-size: cover; background-position: right center;
        filter: brightness(1.12) contrast(1.06);
      }}
      .stage-vignette {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(90deg, rgba(7,11,28,0.92) 0%, rgba(10,16,40,0.80) 28%, rgba(14,16,45,0.40) 50%, transparent 70%),
          linear-gradient(180deg, rgba(7,13,32,0.85) 0%, transparent 20%, transparent 80%, rgba(7,13,32,0.95) 100%);
      }}
      .dragon-layer {{
        position: absolute; bottom: 60px; left: 0; width: 3840px; pointer-events: none; opacity: 0.6;
      }}
      .container {{
        position: absolute; inset: 60px 100px;
        display: flex; justify-content: space-between; align-items: center;
        z-index: 10;
      }}
      .left-identity {{
        max-width: 1400px;
      }}
      .eyebrow {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600; font-size: 34px;
        letter-spacing: 0.40em; color: #FFFFFF; text-shadow: 0 0 24px rgba(155,77,255,0.8); margin-bottom: 12px;
      }}
      .main-row {{
        display: flex; align-items: baseline; gap: 28px; white-space: nowrap; line-height: 0.92;
      }}
      .t-ma {{
        font-weight: 800; font-size: 160px; letter-spacing: -0.02em; color: #FFFFFF;
        text-shadow: 0 0 36px rgba(155,77,255,0.7), 0 0 72px rgba(36,91,255,0.6);
      }}
      .t-year {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 148px;
        color: transparent; -webkit-text-stroke: 3px #FFFFFF;
        filter: drop-shadow(0 0 20px rgba(155,77,255,0.8));
      }}
      .t-region {{
        font-weight: 800; font-size: 110px; line-height: 1.04; letter-spacing: -0.015em;
        background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 48%, #7DD3FC 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 32px rgba(155,77,255,0.7)); margin-top: 6px;
      }}
      .theme-strip {{
        margin-top: 36px; display: flex; flex-direction: column; gap: 6px;
      }}
      .theme-concept {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 28px; font-weight: 500; color: #E9D5FF; letter-spacing: 0.05em;
      }}
      .theme-sector {{
        font-weight: 800; font-size: 48px; letter-spacing: -0.01em; color: #FFFFFF;
        text-shadow: 0 0 28px rgba(155,77,255,0.7);
      }}
      .meta-stage {{
        margin-top: 48px; display: flex; gap: 48px; font-family: 'Space Grotesk', sans-serif; font-size: 22px; font-weight: 700; color: #63B4FF;
        letter-spacing: 0.12em; text-transform: uppercase;
      }}
      .center-stage-clearance {{
        /* Keeps center free for speaking podium & keynote panelists */
        flex: 1; min-width: 600px;
      }}
      .right-emblem {{
        display: flex; flex-direction: column; align-items: flex-end; gap: 20px;
      }}
      .right-emblem img {{
        height: 80px; width: auto;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="stage-vignette"></div>
      <div class="dragon-layer">
        {get_dragon_bridge_svg(w=3840, h=300, opacity=0.6)}
      </div>

      <div class="container">
        <div class="left-identity">
          <div class="eyebrow">{title_eyebrow}</div>
          <div class="main-row">
            <span class="t-ma">{title_main}</span>
            <span class="t-year">2026</span>
          </div>
          <div class="t-region">{title_region}</div>
          <div class="theme-strip">
            <div class="theme-concept">{theme_concept}</div>
            <div class="theme-sector">{theme_sector}</div>
          </div>
          <div class="meta-stage">
            <span>13.12.2026</span>
            <span>•</span>
            <span>13:30–17:30</span>
            <span>•</span>
            <span>ĐÀ NẴNG, VIỆT NAM</span>
          </div>
        </div>

        <div class="center-stage-clearance"></div>

        <div class="right-emblem">
          <img src="{u_wordmark}" alt="VMAA Wordmark"/>
          <div style="font-family:'Space Grotesk',sans-serif; font-size:16px; font-weight:600; color:rgba(233,213,255,0.7); letter-spacing:0.18em; text-align:right;">
            CENTRAL VIETNAM CHAPTER<br>SUMMIT STAGE DISPLAY
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 3. VIP GUEST & SPEAKER SUITE (USING USER PREFERRED FLUTED CRYSTAL BG)
# =========================================================================
def build_guest_spotlight_html(w=1080, h=1350, format_name="feed"):
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .guest-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_guest_bg}');
        background-size: cover; background-position: right center;
        filter: brightness(1.08) contrast(1.15) saturate(1.2);
      }}
      .aurora-glow {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient(900px 700px at 80% 35%, rgba(155,77,255,0.45) 0%, rgba(36,91,255,0.30) 45%, transparent 75%),
          radial-gradient(700px 600px at 20% 50%, rgba(107,45,155,0.40) 0%, transparent 70%);
      }}
      .readability-mask {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(90deg, rgba(7,11,28,0.92) 0%, rgba(10,16,40,0.78) 46%, rgba(14,16,45,0.35) 75%, transparent 100%),
          linear-gradient(180deg, rgba(7,13,32,0.85) 0%, transparent 18%, transparent 75%, rgba(7,13,32,0.95) 100%);
      }}
      .container {{
        position: absolute; inset: 48px 52px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .top-band {{
        display: flex; justify-content: space-between; align-items: center;
        padding-bottom: 20px; border-bottom: 1px solid rgba(233,213,255,0.25);
      }}
      .top-tag {{
        font-family: 'Space Grotesk', monospace; font-size: 13px; font-weight: 700;
        color: #63B4FF; letter-spacing: 0.16em; text-transform: uppercase;
      }}
      .content-center {{
        margin-top: auto; margin-bottom: auto; max-width: 780px; padding-left: 6px;
      }}
      .speaker-badge {{
        display: inline-flex; align-items: center; gap: 10px;
        padding: 6px 16px; border-radius: 999px;
        background: rgba(155,77,255,0.18); border: 1px solid rgba(155,77,255,0.45);
        font-family: 'Space Grotesk', sans-serif; font-size: 12px; font-weight: 700;
        color: #E9D5FF; letter-spacing: 0.16em; text-transform: uppercase;
        margin-bottom: 18px; box-shadow: 0 0 16px rgba(155,77,255,0.3);
      }}
      .speaker-name {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 56px;
        line-height: 1.05; letter-spacing: -0.02em; color: #FFFFFF;
        text-shadow: 0 0 32px rgba(155,77,255,0.7), 0 0 64px rgba(36,91,255,0.5);
        margin-bottom: 14px;
      }}
      .speaker-title {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 700; font-size: 24px;
        color: #93C5FD; margin-bottom: 6px;
      }}
      .speaker-role {{
        font-family: 'Inter', sans-serif; font-weight: 500; font-size: 18px;
        color: rgba(233,213,255,0.85); margin-bottom: 28px; line-height: 1.4;
      }}
      .topic-card {{
        background: rgba(10, 22, 48, 0.75);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(233,213,255,0.25);
        border-left: 4px solid #9B4DFF;
        border-radius: 8px; padding: 22px 26px;
        box-shadow: 0 12px 32px rgba(0,0,0,0.5);
      }}
      .topic-cap {{
        font-family: 'Space Grotesk', sans-serif; font-size: 12px; font-weight: 700;
        color: #C084FC; letter-spacing: 0.16em; text-transform: uppercase; margin-bottom: 8px;
      }}
      .topic-text {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 20px; font-weight: 600;
        color: #FFFFFF; line-height: 1.45;
      }}
      .bottom-band {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-top: 20px; border-top: 1px solid rgba(233,213,255,0.25);
      }}
      .event-lockup small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: 11px; font-weight: 600;
        color: #63B4FF; letter-spacing: 0.14em; text-transform: uppercase; margin-bottom: 4px;
      }}
      .event-lockup b {{
        display: block; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 20px; color: #FFFFFF;
      }}
    </style></head><body>
      <div class="guest-bg"></div>
      <div class="aurora-glow"></div>
      <div class="readability-mask"></div>

      <div class="container">
        <!-- Top Band -->
        <div class="top-band">
          <img src="{u_logo}" alt="VMAA" style="height:44px; width:auto;"/>
          <div class="top-tag">DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 // KEYNOTE SPEAKER</div>
          <div style="font-family:'Space Grotesk',monospace; font-size:12px; font-weight:600; color:#E9D5FF;">13.12.2026 · ĐÀ NẴNG</div>
        </div>

        <!-- Speaker Spotlight Content -->
        <div class="content-center">
          <div class="speaker-badge">
            <span style="display:inline-block; width:7px; height:7px; border-radius:50%; background:#9B4DFF; box-shadow:0 0 8px #9B4DFF;"></span>
            DIỄN GIẢ TIÊU BIỂU // TỌA ĐÀM CẤP CAO
          </div>
          <div class="speaker-name">TS. TRẦN ĐÌNH THIÊN</div>
          <div class="speaker-title">Nguyên Viện trưởng Viện Kinh tế Việt Nam</div>
          <div class="speaker-role">Chuyên gia Cố vấn Kinh tế Vĩ mô &amp; Tái cấu trúc M&amp;A</div>

          <div class="topic-card">
            <div class="topic-cap">CHUYÊN ĐỀ CHIA SẺ</div>
            <div class="topic-text">
              “Kiến trúc Giá trị Mới &amp; Xu hướng Tái cấu trúc Bất động sản — Công nghệ tại Miền Trung giai đoạn 2026–2030”
            </div>
          </div>
        </div>

        <!-- Bottom Band -->
        <div class="bottom-band">
          <div class="event-lockup">
            <small>THỜI GIAN &amp; ĐỊA ĐIỂM</small>
            <b>13.12.2026 · 13:30–17:30 · Ariyana Convention Centre, Đà Nẵng</b>
          </div>

          <div style="text-align:right;">
            <div style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:600; color:#63B4FF; letter-spacing:0.12em; text-transform:uppercase; margin-bottom:4px;">ĐƠN VỊ TỔ CHỨC</div>
            <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:16px; color:#E9D5FF;">VMAA CENTRAL CHAPTER</div>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 4. GUEST LOWER-THIRD MASTER (3840x2160 4K)
# =========================================================================
def build_guest_lower_third_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: 1920px; height: 1080px;
        background: transparent;
      }}
      .lower-third-wrap {{
        position: absolute; bottom: 90px; left: 100px;
        display: flex; align-items: stretch; gap: 0;
        filter: drop-shadow(0 20px 40px rgba(0,0,0,0.85));
      }}
      .accent-pillar {{
        width: 8px; border-radius: 6px 0 0 6px;
        background: linear-gradient(180deg, #9B4DFF 0%, #245BFF 60%, #63B4FF 100%);
        box-shadow: 0 0 24px rgba(155,77,255,0.85);
      }}
      .glass-card {{
        background: rgba(7, 13, 32, 0.88);
        background-image:
          radial-gradient(400px 250px at 100% 0%, rgba(155,77,255,0.25) 0%, transparent 70%),
          linear-gradient(90deg, rgba(7,13,32,0.95) 0%, rgba(10,22,48,0.85) 100%);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(233,213,255,0.22);
        border-left: none;
        border-radius: 0 10px 10px 0;
        padding: 24px 44px 22px 32px;
        position: relative; overflow: hidden;
      }}
      .sweep-light {{
        position: absolute; top: 0; left: -200px; width: 120px; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(233,213,255,0.25), transparent);
        transform: skewX(-25deg);
      }}
      .guest-session {{
        font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 700;
        color: #63B4FF; letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 6px;
      }}
      .guest-name {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 44px; font-weight: 800;
        color: #FFFFFF; letter-spacing: -0.01em; text-shadow: 0 0 24px rgba(155,77,255,0.7);
      }}
      .guest-title {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 19px; font-weight: 600;
        color: #E9D5FF; margin-top: 4px;
      }}
      .guest-org {{
        font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 500;
        color: rgba(233,213,255,0.85); margin-top: 2px;
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
# 5. SIX DISTINCT SOCIAL MEDIA DESIGNS (ALL 7 RATIOS)
# =========================================================================
def build_social_post_html(post_id: int, w: int, h: int, lang="vi"):
    is_vi = (lang == "vi")

    # Pick background plate based on theme & user preference
    if post_id == 5:
        # Keynote Speaker Spotlight uses user's preferred fluted crystal background!
        bg_url = u_guest_bg
    elif post_id in (1, 6):
        bg_url = u_kv_bottom_4k
    elif post_id == 2:
        bg_url = u_cantilever
    else:
        bg_url = u_prism

    # Content configurations for 6 distinct post types
    if post_id == 1:
        tag = "OFFICIAL ANNOUNCEMENT" if not is_vi else "CÔNG BỐ CHÍNH THỨC"
        headline = "DIỄN ĐÀN M&A 2026 MIỀN TRUNG" if is_vi else "CENTRAL VIETNAM M&A FORUM 2026"
        subhead = "Kiến trúc giá trị: Bất động sản × Công nghệ" if is_vi else "Architecture of Value: Real Estate × Technology"
        body = "Sự kiện quy tụ 1,500+ nhà lãnh đạo tập đoàn kinh tế và các quỹ đầu tư quốc tế hàng đầu tại Đà Nẵng." if is_vi else "The premier summit convening 1,500+ leaders, conglomerates and top PE funds in Da Nang."
        cta = "ĐĂNG KÝ THAM DỰ VIP ↗" if is_vi else "REGISTER VIP PASS ↗"
    elif post_id == 2:
        tag = "THEMATIC CONCEPT" if not is_vi else "Ý NIỆM CHỦ ĐỀ"
        headline = "KIẾN TRÚC GIÁ TRỊ" if is_vi else "ARCHITECTURE OF VALUE"
        subhead = "Hội tụ chiến lược giữa Bất động sản & Công nghệ" if is_vi else "Strategic convergence of Real Estate & Technology"
        body = "Tái cấu trúc dòng vốn, định giá PropTech và tối ưu hóa danh mục tài sản thông qua sức mạnh dữ liệu số." if is_vi else "Capital restructuring, PropTech valuation, and asset portfolio optimization powered by digital infrastructure."
        cta = "KHÁM PHÁ Ý NIỆM ↗" if is_vi else "EXPLORE CONCEPT ↗"
    elif post_id == 3:
        tag = "SECTOR INSIGHT: REAL ESTATE" if not is_vi else "TIÊU ĐIỂM BẤT ĐỘNG SẢN"
        headline = "TÁI CẤU TRÚC QUỸ ĐẤT & DÒNG VỐN" if is_vi else "LAND BANK RESTRUCTURING & CAPITAL"
        subhead = "Cơ hội M&A BĐS nghỉ dưỡng & công nghiệp Miền Trung" if is_vi else "M&A opportunities in Central Vietnam hospitality & industrial"
        body = "Phân tích biến động pháp lý, mở rộng quỹ đất và các thương vụ hợp tác chiến lược đón đầu chu kỳ mới 2026–2030." if is_vi else "Analyzing regulatory shifts, land expansion, and strategic partnerships for 2026–2030."
        cta = "XEM BÁO CÁO M&A ↗" if is_vi else "VIEW M&A REPORT ↗"
    elif post_id == 4:
        tag = "SECTOR INSIGHT: TECHNOLOGY" if not is_vi else "TIÊU ĐIỂM CÔNG NGHỆ"
        headline = "PROPTECH & AI ĐỊNH GIÁ TÀI SẢN" if is_vi else "PROPTECH & AI VALUATION"
        subhead = "Công nghệ nâng tầm giá trị thương vụ M&A" if is_vi else "Technology elevating M&A transaction value"
        body = "Ứng dụng mô hình AI thẩm định giá tài sản, chuyển đổi số và nâng cao biên lợi nhuận cho các dự án quy mô lớn." if is_vi else "Deploying AI valuation models, digital transformation, and margin optimization."
        cta = "XEM GIẢI PHÁP TECH ↗" if is_vi else "VIEW TECH SUITE ↗"
    elif post_id == 5:
        tag = "KEYNOTE SPEAKER SPOTLIGHT" if not is_vi else "DIỄN GIẢ TIÊU BIỂU"
        headline = "TS. TRẦN ĐÌNH THIÊN" if is_vi else "DR. TRAN DINH THIEN"
        subhead = "Nguyên Viện trưởng Viện Kinh tế Việt Nam" if is_vi else "Former Director, Vietnam Institute of Economics"
        body = "Chuyên đề: 'Kiến trúc Giá trị Mới & Xu hướng Tái cấu trúc Bất động sản — Công nghệ Miền Trung 2026–2030'." if is_vi else "Topic: 'New Architecture of Value & Real Estate — Tech Restructuring in Central Vietnam'."
        cta = "GẶP GỠ DIỄN GIẢ ↗" if is_vi else "MEET THE SPEAKER ↗"
    else:
        tag = "EVENT AGENDA & DEAL ROOM" if not is_vi else "LỊCH TRÌNH & ĐĂNG KÝ"
        headline = "13.12.2026 · 13:30–17:30"
        subhead = "Ariyana Convention Centre · Đà Nẵng, Việt Nam"
        body = "3 phiên tọa đàm chiến lược, lễ ký kết thương vụ MOU và phòng Deal Room kết nối đầu tư 1:1." if is_vi else "3 strategic plenary sessions, MOU deal signings, and 1:1 institutional deal rooms."
        cta = "ĐĂNG KÝ VÉ SỚM VIP ↗" if is_vi else "SECURE EARLY VIP PASS ↗"

    scale_factor = min(w / 1080.0, h / 1350.0)
    pad = int(48 * scale_factor)
    font_h = int(58 * scale_factor)
    font_sub = int(22 * scale_factor)
    font_b = int(16 * scale_factor)

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{bg_url}');
        background-size: cover; background-position: center;
        filter: brightness(1.10) contrast(1.1);
      }}
      .readability-mask {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          radial-gradient(circle at 80% 30%, rgba(155,77,255,0.3) 0%, transparent 60%),
          linear-gradient(180deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.4) 30%, rgba(7,13,32,0.7) 70%, rgba(7,13,32,0.95) 100%);
      }}
      .card-wrap {{
        position: absolute; inset: {pad}px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .top-row {{
        display: flex; justify-content: space-between; align-items: center;
        padding-bottom: {int(16*scale_factor)}px; border-bottom: 1px solid rgba(233,213,255,0.22);
      }}
      .tag-pill {{
        font-family: 'Space Grotesk', sans-serif; font-size: {int(12*scale_factor)}px; font-weight: 700;
        color: #63B4FF; letter-spacing: 0.16em; text-transform: uppercase;
      }}
      .main-body {{
        margin-top: auto; margin-bottom: auto; max-width: 90%;
      }}
      .headline {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: {font_h}px;
        line-height: 1.05; letter-spacing: -0.02em; color: #FFFFFF;
        text-shadow: 0 0 24px rgba(155,77,255,0.7); margin-bottom: {int(12*scale_factor)}px;
      }}
      .subhead {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600; font-size: {font_sub}px;
        color: #93C5FD; margin-bottom: {int(14*scale_factor)}px; line-height: 1.3;
      }}
      .body-text {{
        font-family: 'Inter', sans-serif; font-weight: 400; font-size: {font_b}px;
        color: rgba(233,213,255,0.88); line-height: 1.5; margin-bottom: {int(20*scale_factor)}px;
      }}
      .cta-button {{
        display: inline-flex; align-items: center; gap: 8px;
        padding: {int(10*scale_factor)}px {int(22*scale_factor)}px;
        border-radius: 999px; background: linear-gradient(90deg, #9B4DFF, #245BFF);
        font-family: 'Space Grotesk', sans-serif; font-size: {int(13*scale_factor)}px; font-weight: 700;
        color: #FFFFFF; letter-spacing: 0.1em; box-shadow: 0 0 16px rgba(155,77,255,0.5);
      }}
      .bottom-row {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-top: {int(16*scale_factor)}px; border-top: 1px solid rgba(233,213,255,0.22);
      }}
      .date-col small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: {int(10*scale_factor)}px; font-weight: 600;
        color: #63B4FF; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 2px;
      }}
      .date-col b {{
        display: block; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800;
        font-size: {int(16*scale_factor)}px; color: #FFFFFF;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="readability-mask"></div>

      <div class="card-wrap">
        <div class="top-row">
          <img src="{u_logo}" alt="VMAA" style="height:{int(38*scale_factor)}px; width:auto;"/>
          <div class="tag-pill">{tag}</div>
        </div>

        <div class="main-body">
          <div class="headline">{headline}</div>
          <div class="subhead">{subhead}</div>
          <div class="body-text">{body}</div>
          <div class="cta-button">{cta}</div>
        </div>

        <div class="bottom-row">
          <div class="date-col">
            <small>NGÀY &amp; ĐỊA ĐIỂM</small>
            <b>13.12.2026 · ĐÀ NẴNG, VIỆT NAM</b>
          </div>
          <div style="text-align:right;">
            <div style="font-family:'Space Grotesk',sans-serif; font-size:{int(10*scale_factor)}px; font-weight:600; color:#E9D5FF; letter-spacing:0.12em;">VMAA CENTRAL CHAPTER</div>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 6. MASTER PRODUCTION SUITE CONTACT SHEET (3840x2160 4K)
# =========================================================================
def build_master_contact_sheet_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: 3840px; height: 2160px;
        background: #040714;
        display: flex; flex-direction: column; justify-content: space-between;
        padding: 50px 70px;
      }}
      .header-bar {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-bottom: 24px; border-bottom: 2px solid rgba(155,77,255,0.4);
      }}
      .header-title {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 38px; font-weight: 800;
        letter-spacing: -0.01em; color: #FFFFFF;
      }}
      .header-meta {{
        font-family: 'Space Grotesk', monospace; font-size: 16px; font-weight: 600;
        color: #93C5FD; letter-spacing: 0.16em; text-transform: uppercase;
      }}
      .grid-showcase {{
        display: grid;
        grid-template-columns: 2fr 1.2fr 1fr;
        grid-template-rows: auto auto;
        gap: 36px;
        margin-top: 36px; margin-bottom: 36px;
      }}
      .show-card {{
        background: rgba(10,22,48,0.7);
        border: 1px solid rgba(233,213,255,0.25);
        border-radius: 12px; overflow: hidden;
        display: flex; flex-direction: column;
      }}
      .card-label {{
        padding: 14px 20px; background: rgba(7,13,32,0.9);
        border-bottom: 1px solid rgba(233,213,255,0.18);
        font-family: 'Space Grotesk', sans-serif; font-size: 14px; font-weight: 700;
        color: #63B4FF; letter-spacing: 0.14em; text-transform: uppercase;
        display: flex; justify-content: space-between;
      }}
      .card-preview {{
        position: relative; flex: 1; min-height: 280px; overflow: hidden;
        background-size: cover; background-position: center;
      }}
      .footer-swatches {{
        display: flex; justify-content: space-between; align-items: center;
        padding-top: 24px; border-top: 1px solid rgba(233,213,255,0.22);
      }}
      .swatch-group {{
        display: flex; gap: 18px; align-items: center;
      }}
      .swatch {{
        display: flex; align-items: center; gap: 8px;
        font-family: 'Space Grotesk', monospace; font-size: 13px; color: rgba(233,213,255,0.8);
      }}
      .swatch-dot {{
        width: 18px; height: 18px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.3);
      }}
    </style></head><body>
      <div class="header-bar">
        <div>
          <div style="font-family:'Space Grotesk',monospace; font-size:14px; font-weight:700; color:#C084FC; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:6px;">
            VMAA CENTRAL VIETNAM // MASTER VISUAL IDENTITY &amp; MOTION PRODUCTION SYSTEM
          </div>
          <div class="header-title">DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · HỆ THỐNG ẤN PHẨM SỐ V2</div>
        </div>
        <div style="text-align:right;">
          <img src="{u_wordmark}" alt="VMAA" style="height:32px; width:auto; margin-bottom:6px;"/>
          <div class="header-meta">13.12.2026 · ĐÀ NẴNG, VIỆT NAM · ARCHITECTURE OF VALUE</div>
        </div>
      </div>

      <div class="grid-showcase">
        <!-- 1. Hero Landscape 16:9 -->
        <div class="show-card" style="grid-column: 1 / 2; grid-row: 1 / 2;">
          <div class="card-label">
            <span>01. PRIMARY KEY VISUAL MASTER (16:9 4K)</span>
            <span>UNBOXED · DRAGON BRIDGE INTEGRATED</span>
          </div>
          <div class="card-preview" style="background-image:url('{u_kv_bottom_4k}'); height:460px;"></div>
        </div>

        <!-- 2. 32:9 Curved LED Stage -->
        <div class="show-card" style="grid-column: 2 / 4; grid-row: 1 / 2;">
          <div class="card-label">
            <span>02. 32:9 CURVED LED STAGE WALL (3840×1080)</span>
            <span>CENTRAL PODIUM CLEARANCE</span>
          </div>
          <div class="card-preview" style="background-image:url('{u_kv_bottom_4k}'); height:460px; background-position:right center;"></div>
        </div>

        <!-- 3. Keynote Speaker Spotlight (Fluted Crystal BG) -->
        <div class="show-card" style="grid-column: 1 / 2; grid-row: 2 / 3;">
          <div class="card-label">
            <span>03. KEYNOTE GUEST SPOTLIGHT (4:5 FEED &amp; STORY)</span>
            <span>USER PREFERRED CRYSTAL FLUTED BACKGROUND</span>
          </div>
          <div class="card-preview" style="background-image:url('{u_guest_bg}'); height:460px;"></div>
        </div>

        <!-- 4. Broadcast Lower-Third -->
        <div class="show-card" style="grid-column: 2 / 3; grid-row: 2 / 3;">
          <div class="card-label">
            <span>04. LIVE IMAG &amp; BROADCAST LOWER-THIRD (4K)</span>
            <span>FROSTED GLASS CARD · SWEEP LIGHT</span>
          </div>
          <div class="card-preview" style="background-image:url('{u_prism}'); height:460px;"></div>
        </div>

        <!-- 5. Multi-Ratio Social Matrix -->
        <div class="show-card" style="grid-column: 3 / 4; grid-row: 2 / 3;">
          <div class="card-label">
            <span>05. 6 SOCIAL POST THEMES (7 RATIOS)</span>
            <span>42 VARIANTS AUTOMATED</span>
          </div>
          <div class="card-preview" style="background-image:url('{u_cantilever}'); height:460px;"></div>
        </div>
      </div>

      <div class="footer-swatches">
        <div class="swatch-group">
          <span style="font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; color:#63B4FF; letter-spacing:0.14em;">COLOR INVARIANTS:</span>
          <div class="swatch"><div class="swatch-dot" style="background:#070D20;"></div>Obsidian #070D20</div>
          <div class="swatch"><div class="swatch-dot" style="background:#245BFF;"></div>Electric Cobalt #245BFF</div>
          <div class="swatch"><div class="swatch-dot" style="background:#6B2D9B;"></div>Amethyst #6B2D9B</div>
          <div class="swatch"><div class="swatch-dot" style="background:#9B4DFF;"></div>Violet #9B4DFF</div>
          <div class="swatch"><div class="swatch-dot" style="background:#E9D5FF;"></div>Soft Lavender #E9D5FF</div>
          <div class="swatch"><div class="swatch-dot" style="background:#63B4FF;"></div>Ice Cyan #63B4FF</div>
          <div class="swatch"><div class="swatch-dot" style="background:#F59E0B;"></div>Dragon Gold #F59E0B</div>
        </div>

        <div style="font-family:'Space Grotesk',monospace; font-size:12px; color:rgba(233,213,255,0.7); letter-spacing:0.12em;">
          ENGINEERED WITH PLAYWRIGHT CHROMIUM @2X RETINA · ZERO-PILL UNBOXED TYPOGRAPHY · DIACRITIC SAFE
        </div>
      </div>
    </body></html>"""


# =========================================================================
# ASYNC PLAYWRIGHT MASTER EXPORT PIPELINE
# =========================================================================
async def run_master_production():
    print("[INIT] Starting VMAA Visual Identity v2 Master Production Suite...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--force-color-profile=srgb"])

        # -------------------------------------------------------------
        # 1. RENDER PRIMARY LANDSCAPE KV (1920x1080 @2x -> 3840x2160 4K)
        # -------------------------------------------------------------
        print("\n--- 1. Render Primary Landscape Key Visuals ---")
        for lang in ("vi", "en"):
            h_land = build_primary_landscape_kv_html(1920, 1080, lang=lang)
            land_html = EXPORTS_DIR / f"KV_v2_Landscape_1920x1080_{lang.upper()}.html"
            land_png = EXPORTS_DIR / f"KV_v2_Landscape_1920x1080_{lang.upper()}.png"
            land_html.write_text(h_land, encoding="utf-8")
            pg = await browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
            await pg.goto(land_html.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(land_png))
            await pg.close()
            shutil.copy(land_png, BRAIN_DIR / land_png.name)
            print(f"Rendered {land_png.name} (3840x2160 4K UHD)")

        # -------------------------------------------------------------
        # 2. RENDER 32:9 CURVED LED STAGE WALL (3840x1080)
        # -------------------------------------------------------------
        print("\n--- 2. Render 32:9 Curved LED Stage Wall ---")
        for lang in ("vi", "en"):
            h_stage = build_curved_stage_32x9_html(3840, 1080, lang=lang)
            stage_html = STAGE_DIR / f"KV_v2_Curved_Stage_32x9_{lang.upper()}.html"
            stage_png = STAGE_DIR / f"KV_v2_Curved_Stage_32x9_{lang.upper()}.png"
            stage_html.write_text(h_stage, encoding="utf-8")
            pg = await browser.new_page(viewport={"width": 3840, "height": 1080}, device_scale_factor=1)
            await pg.goto(stage_html.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(stage_png))
            await pg.close()
            shutil.copy(stage_png, BRAIN_DIR / stage_png.name)
            print(f"Rendered {stage_png.name} (3840x1080 32:9 Curved LED Wall)")

        # -------------------------------------------------------------
        # 3. RENDER VIP GUEST & SPEAKER SUITE (FLUTED CRYSTAL BG)
        # -------------------------------------------------------------
        print("\n--- 3. Render VIP Guest & Speaker Suite ---")
        guest_formats = [
            ("GUEST_01_Portrait_1080x1350.png", 1080, 1350, 2),
            ("GUEST_01_Story_1080x1920.png", 1080, 1920, 2),
            ("GUEST_01_Square_1200x1200.png", 1200, 1200, 1),
        ]
        for fname, gw, gh, dsf in guest_formats:
            h_guest = build_guest_spotlight_html(gw, gh)
            out_html = GUESTS_DIR / fname.replace(".png", ".html")
            out_png = GUESTS_DIR / fname
            out_html.write_text(h_guest, encoding="utf-8")
            pg = await browser.new_page(viewport={"width": gw, "height": gh}, device_scale_factor=dsf)
            await pg.goto(out_html.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(out_png))
            await pg.close()
            shutil.copy(out_png, BRAIN_DIR / out_png.name)
            print(f"Rendered {fname} (Speaker Spotlight with Crystal Fluted BG)")

        # Guest Lower-Third Master
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

        # -------------------------------------------------------------
        # 4. RENDER 6 SOCIAL MEDIA DESIGNS (ALL 7 RATIOS)
        # -------------------------------------------------------------
        print("\n--- 4. Render 6 Distinct Social Media Designs ---")
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
            print(f"Exported Post #{post_idx:02d} across 7 platform ratios!")
        await social_pg.close()

        # -------------------------------------------------------------
        # 5. RENDER MASTER CONTACT SHEET (3840x2160 4K)
        # -------------------------------------------------------------
        print("\n--- 5. Render Master Production Contact Sheet ---")
        cs_html = build_master_contact_sheet_html()
        cs_file = EXPORTS_DIR / "VMAA_2026_Production_Contact_Sheet_4K.html"
        cs_png = EXPORTS_DIR / "VMAA_2026_Production_Contact_Sheet_4K.png"
        cs_file.write_text(cs_html, encoding="utf-8")
        pg = await browser.new_page(viewport={"width": 3840, "height": 2160}, device_scale_factor=1)
        await pg.goto(cs_file.as_uri(), wait_until="networkidle")
        await pg.wait_for_timeout(600)
        await pg.screenshot(path=str(cs_png))
        await pg.close()
        shutil.copy(cs_png, BRAIN_DIR / cs_png.name)
        print("Rendered VMAA_2026_Production_Contact_Sheet_4K.png (3840x2160 4K)")

        await browser.close()

    print("\n[SUCCESS] Completed VMAA Visual Identity v2 Master Production Suite!")


if __name__ == "__main__":
    asyncio.run(run_master_production())
