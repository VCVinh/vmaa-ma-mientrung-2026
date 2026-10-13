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
PORTRAIT_DIR.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


# High-Res Crystal & Reference Plates
u_crystal_fluted_4k = to_data_uri(PLATES_DIR / "crystal_fluted_4k.png")
u_purple_caustics = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u_kv_bottom_4k = to_data_uri(PLATES_DIR / "kv_ref_bottom_4k.png")
u_logo = to_data_uri(ASSETS_DIR / "vmaa_logo_white_transparent.png")
u_wordmark = to_data_uri(ASSETS_DIR / "vmaa_wordmark_white_transparent.png")

TYPO_CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=Outfit:wght@400;600;800&display=swap" rel="stylesheet">
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


def get_dragon_bridge_svg(w=1080, h=220, opacity=0.7):
    return f"""
    <svg width="{w}" height="{h}" viewBox="0 0 1080 220" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity:{opacity}; mix-blend-mode:screen; pointer-events:none;">
      <defs>
        <linearGradient id="db_p_arch_grad" x1="0" y1="0" x2="1080" y2="0" gradientUnits="userSpaceOnUse">
          <stop offset="10%" stop-color="#D97706" stop-opacity="0.3"/>
          <stop offset="35%" stop-color="#F59E0B" stop-opacity="0.95"/>
          <stop offset="65%" stop-color="#FDE047" stop-opacity="0.9"/>
          <stop offset="85%" stop-color="#245BFF" stop-opacity="0.75"/>
          <stop offset="100%" stop-color="#63B4FF" stop-opacity="0.3"/>
        </linearGradient>
        <filter id="db_p_glow_f" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="4" result="blur"/>
          <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
        </filter>
      </defs>

      <line x1="0" y1="170" x2="1080" y2="170" stroke="rgba(99,180,255,0.45)" stroke-width="1.2" stroke-dasharray="10 5"/>
      <rect x="80" y="172" width="920" height="45" fill="rgba(36,91,255,0.18)"/>

      <g filter="url(#db_p_glow_f)">
        <path d="M 120 170 Q 200 115, 280 170" stroke="url(#db_p_arch_grad)" stroke-width="3.5" fill="none" stroke-linecap="round"/>
        <path d="M 280 170 Q 380 80, 480 170" stroke="url(#db_p_arch_grad)" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        <path d="M 480 170 Q 600 45, 720 170" stroke="url(#db_p_arch_grad)" stroke-width="5.5" fill="none" stroke-linecap="round"/>
        <path d="M 720 170 Q 820 85, 900 170" stroke="url(#db_p_arch_grad)" stroke-width="4.5" fill="none" stroke-linecap="round"/>
        <path d="M 900 170 Q 960 120, 1010 170" stroke="url(#db_p_arch_grad)" stroke-width="3.5" fill="none" stroke-linecap="round"/>

        <path d="M 1000 135 C 1015 128, 1030 135, 1040 130 C 1030 142, 1025 150, 1010 155 Z" fill="#F59E0B" opacity="0.95"/>
        <circle cx="1040" cy="130" r="3" fill="#FFFFFF"/>
        <path d="M 1040 130 Q 1060 125, 1075 128" stroke="#FDE047" stroke-width="2" stroke-dasharray="2 2"/>
      </g>
    </svg>
    """


# =========================================================================
# 1. DẠNG PHA LÊ MASTER (VERTICAL FLUTED CRYSTAL ARCHITECTURE)
# =========================================================================
def build_portrait_phale_html(w=1080, h=1350, style_variant="phale", lang="vi"):
    is_vi = (lang == "vi")
    title_eyebrow = "D I Ễ N   Đ À N" if is_vi else "F O R U M"
    title_main = "M&A"
    title_region = "MIỀN TRUNG" if is_vi else "CENTRAL VIETNAM"
    theme_concept = "Kiến trúc giá trị" if is_vi else "Architecture of value"
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

    is_story = (h >= 1900)
    is_square = (w == h)

    # Pick background plate
    if style_variant == "phale":
        bg_url = u_crystal_fluted_4k
        bg_pos = "right center" if not is_story else "75% center"
        filter_str = "brightness(1.18) contrast(1.16) saturate(1.28)"
    else:
        # thap_sang
        bg_url = u_kv_bottom_4k
        bg_pos = "74% 25%" if not is_story else "76% 20%"
        filter_str = "brightness(1.16) contrast(1.12) saturate(1.22)"

    pad_h = 48
    pad_v = 44 if not is_story else 60
    bridge_bottom = 120 if not is_story else 180

    font_ma = "118px" if not is_story else "124px"
    font_year = "106px" if not is_story else "112px"
    font_region = "82px" if not is_story else "88px"
    font_sector = "36px" if not is_story else "40px"

    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8">{TYPO_CSS}<style>
      body {{
        width: {w}px; height: {h}px;
        background: #070D20;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{bg_url}');
        background-size: cover; background-position: {bg_pos};
        filter: {filter_str};
      }}
      .aurora-wash {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient(900px 750px at 75% 32%, rgba(155,77,255,0.45) 0%, rgba(36,91,255,0.30) 45%, transparent 75%),
          radial-gradient(650px 500px at 25% 65%, rgba(107,45,155,0.35) 0%, transparent 70%),
          radial-gradient(500px 400px at 50% 15%, rgba(233,213,255,0.25) 0%, transparent 65%);
      }}
      /* Ultra-delicate, localized gradient that preserves 85%+ of background luminosity and details */
      .readability-gradient {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(180deg, rgba(7,13,32,0.65) 0%, transparent 16%, transparent 72%, rgba(7,13,32,0.85) 100%),
          radial-gradient(750px 550px at 28% 60%, rgba(7,11,28,0.58) 0%, transparent 75%);
      }}
      .dragon-layer {{
        position: absolute; bottom: {bridge_bottom}px; left: 0; width: {w}px; pointer-events: none;
        opacity: 0.75;
      }}
      .container {{
        position: absolute; inset: {pad_v}px {pad_h}px;
        display: flex; flex-direction: column; justify-content: space-between;
        z-index: 10;
      }}
      .top-band {{
        display: flex; justify-content: space-between; align-items: flex-start;
        padding-bottom: 16px; border-bottom: 1px solid rgba(233,213,255,0.24);
      }}
      .slot-cap {{
        font-family: 'Space Grotesk', sans-serif; font-size: 10px; font-weight: 600;
        color: rgba(233,213,255,0.8); letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 6px;
      }}
      .slot-box {{
        display: flex; align-items: center; min-height: 44px;
      }}
      .slot-box img {{
        max-height: 46px; width: auto; display: block;
      }}
      .title-hero {{
        margin-top: auto; margin-bottom: auto; padding-left: 4px; max-width: 900px;
        {"padding-top: 140px;" if is_story else ""}
      }}
      .eyebrow {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 600; font-size: 24px;
        letter-spacing: 0.38em; color: #E9D5FF; text-shadow: 0 0 20px rgba(155,77,255,0.85); margin-bottom: 8px;
      }}
      .main-row {{
        display: flex; align-items: baseline; gap: 18px; white-space: nowrap; line-height: 0.92;
      }}
      .t-ma {{
        font-weight: 800; font-size: {font_ma}; letter-spacing: -0.02em; color: #FFFFFF;
        text-shadow: 0 0 32px rgba(155,77,255,0.7), 0 0 64px rgba(36,91,255,0.6);
      }}
      .t-year {{
        font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: {font_year};
        color: transparent; -webkit-text-stroke: 2.4px #FFFFFF;
        filter: drop-shadow(0 0 16px rgba(155,77,255,0.85));
      }}
      .t-region {{
        font-weight: 800; font-size: {font_region}; line-height: 1.05; letter-spacing: -0.015em;
        background: linear-gradient(90deg, #FFFFFF 0%, #FFFFFF 52%, #63B4FF 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 28px rgba(155,77,255,0.7)); margin-top: 4px;
        padding-top: 2px; padding-bottom: 4px;
      }}
      .theme-strip {{
        margin-top: 22px; display: flex; flex-direction: column; gap: 6px;
      }}
      .theme-concept {{
        display: flex; align-items: center; gap: 12px;
        font-family: 'Plus Jakarta Sans', sans-serif; font-size: 21px; font-weight: 500;
        color: #E9D5FF; letter-spacing: 0.05em;
      }}
      .accent-line {{
        width: 38px; height: 2px; background: linear-gradient(90deg, #9B4DFF, #63B4FF);
        box-shadow: 0 0 10px #9B4DFF;
      }}
      .theme-sector {{
        font-weight: 800; font-size: {font_sector}; letter-spacing: -0.01em; color: #FFFFFF;
        text-shadow: 0 0 24px rgba(155,77,255,0.65);
      }}
      .bottom-band {{
        display: flex; justify-content: space-between; align-items: flex-end;
        padding-top: 16px; border-top: 1px solid rgba(233,213,255,0.24);
      }}
      .logistics {{
        display: flex; gap: 28px; white-space: nowrap;
      }}
      .log-item small {{
        display: block; font-family: 'Space Grotesk', sans-serif; font-size: 10px; font-weight: 600;
        color: #63B4FF; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 2px;
      }}
      .log-item b {{
        display: block; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 800; font-size: 19px; color: #FFFFFF;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="aurora-wash"></div>
      <div class="dragon-layer">
        {get_dragon_bridge_svg(w=w, h=220, opacity=0.75)}
      </div>
      <div class="readability-gradient"></div>

      <div class="container">
        <!-- Top Sponsor Bar (Exact 4-column layout from reference image) -->
        <div class="top-band">
          <div style="flex:1;">
            <div class="slot-cap">{lbl_org}</div>
            <div class="slot-box">
              <img src="{u_logo}" alt="VMAA"/>
            </div>
          </div>
          <div style="flex:1.1;">
            <div class="slot-cap">{lbl_sponsor_main}</div>
            <div class="slot-box" data-slot="sponsor-main">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:700; color:#60A5FA;">[NHÀ TÀI TRỢ ĐỒNG HÀNH]</span>
            </div>
          </div>
          <div style="flex:1;">
            <div class="slot-cap">{lbl_sponsor_gold}</div>
            <div class="slot-box" data-slot="sponsor-gold">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:700; color:#FDE047;">[NHÀ TÀI TRỢ VÀNG]</span>
            </div>
          </div>
          <div style="flex:1;">
            <div class="slot-cap">{lbl_academic}</div>
            <div class="slot-box" data-slot="academic">
              <span style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:700; color:#F87171;">[ĐỐI TÁC HỌC THUẬT · DUE]</span>
            </div>
          </div>
        </div>

        <!-- Hero Typography (Unboxed, razor-sharp, zero-pill) -->
        <div class="title-hero">
          <div class="eyebrow">{title_eyebrow}</div>
          <div class="main-row">
            <span class="t-ma">{title_main}</span>
            <span class="t-year">2026</span>
          </div>
          <div class="t-region">{title_region}</div>

          <div class="theme-strip">
            <div class="theme-concept">
              <span class="accent-line"></span>
              <span>{theme_concept}</span>
            </div>
            <div class="theme-sector">{theme_sector}</div>
          </div>
        </div>

        <!-- Bottom Logistics & Support Bands -->
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

          <div style="text-align:right;">
            <div class="slot-cap">{lbl_support}</div>
            <div style="font-family:'Space Grotesk',sans-serif; font-size:11px; font-weight:600; color:#E9D5FF; margin-top:4px;">
              VMAA CENTRAL CHAPTER
            </div>
          </div>
        </div>
      </div>
    </body></html>"""


async def run_phale_render():
    print("[INIT] Starting High-Luminosity Dạng Đứng (Pha Lê & Tháp Sáng) Render...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--force-color-profile=srgb"])

        deliverables = [
            # 1. DẠNG PHA LÊ (Pha Lê Fluted Crystal Pillars)
            ("KV_v2_Portrait_1080x1350_PhaLe.png", 1080, 1350, "phale", "vi", 2),
            ("KV_v2_Story_1080x1920_PhaLe.png", 1080, 1920, "phale", "vi", 2),
            ("KV_v2_Square_1080x1080_PhaLe.png", 1080, 1080, "phale", "vi", 2),
            # 2. DẠNG THÁP SÁNG (Monumental Crystal Tower Burst - Full Luminosity)
            ("KV_v2_Portrait_1080x1350_ThapSang.png", 1080, 1350, "thap_sang", "vi", 2),
            ("KV_v2_Story_1080x1920_ThapSang.png", 1080, 1920, "thap_sang", "vi", 2),
            # 3. OVERWRITE PRIMARY MASTER PORTRAITS with High-Luminosity Crystal Version
            ("KV_v2_Portrait_1080x1350_VI.png", 1080, 1350, "phale", "vi", 2),
            ("KV_v2_Story_1080x1920_VI.png", 1080, 1920, "phale", "vi", 2),
        ]

        for fname, w, h, variant, lang, dsf in deliverables:
            html_content = build_portrait_phale_html(w, h, style_variant=variant, lang=lang)
            out_html = PORTRAIT_DIR / fname.replace(".png", ".html")
            out_png = PORTRAIT_DIR / fname
            out_html.write_text(html_content, encoding="utf-8")

            # Also save in exports/v2_production/
            root_png = EXPORTS_DIR / fname
            root_html = EXPORTS_DIR / fname.replace(".png", ".html")
            root_html.write_text(html_content, encoding="utf-8")

            pg = await browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=dsf)
            await pg.goto(out_html.as_uri(), wait_until="networkidle")
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(out_png))
            await pg.screenshot(path=str(root_png))
            await pg.close()

            shutil.copy(out_png, BRAIN_DIR / fname)
            print(f"Rendered {fname} ({w*dsf}x{h*dsf} @{dsf}x) [{variant.upper()}]")

        await browser.close()

    print("\n[SUCCESS] Completed High-Luminosity Dạng Đứng (Pha Lê & Tháp Sáng) Suite!")


if __name__ == "__main__":
    asyncio.run(run_phale_render())
