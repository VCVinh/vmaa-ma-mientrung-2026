import os
import shutil
import base64
from pathlib import Path
from playwright.sync_api import sync_playwright

BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")
PROJECT_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
PLATES_DIR = PROJECT_DIR / "assets" / "plates"
EXPORTS_DIR = PROJECT_DIR / "exports"

PLATES_DIR.mkdir(parents=True, exist_ok=True)
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Locate the generated plates
hero_plate = next(BRAIN_DIR.glob("vmaa_arch_plate_hero_*.jpg"))
stage_plate = next(BRAIN_DIR.glob("vmaa_stage_plate_wide_*.jpg"))
fluted_plate = next(BRAIN_DIR.glob("vmaa_fluted_refraction_plate_*.jpg"))

shutil.copy(hero_plate, PLATES_DIR / "vmaa_arch_plate_hero.jpg")
shutil.copy(stage_plate, PLATES_DIR / "vmaa_stage_plate_wide.jpg")
shutil.copy(fluted_plate, PLATES_DIR / "vmaa_fluted_refraction_plate.jpg")

def img_to_data_uri(path: Path) -> str:
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/jpeg;base64,{b64}"

hero_uri = img_to_data_uri(hero_plate)
stage_uri = img_to_data_uri(stage_plate)
fluted_uri = img_to_data_uri(fluted_plate)

# Shared CSS with Plus Jakarta Sans + Space Grotesk + JetBrains Mono (100% Vietnamese diacritic support)
FONTS_HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
"""

# -------------------------------------------------------------------------
# 1. PRIMARY KEY VISUAL MASTER (01_VMAA_Key_Visual_Master.png)
# -------------------------------------------------------------------------
html_key_visual = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
{FONTS_HEAD}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #070D20;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #F4F7FF;
    position: relative;
  }}
  .bg-plate {{
    position: absolute; inset: 0;
    background-image: url('{hero_uri}');
    background-size: cover; background-position: center;
    filter: contrast(1.06) brightness(0.96);
  }}
  .gradient-veil {{
    position: absolute; inset: 0;
    background: linear-gradient(90deg,
      rgba(7,13,32,0.96) 0%,
      rgba(7,13,32,0.88) 42%,
      rgba(16,31,69,0.35) 68%,
      rgba(7,13,32,0.15) 100%);
  }}
  .radial-glow {{
    position: absolute;
    width: 900px; height: 900px;
    left: 280px; top: 120px;
    background: radial-gradient(circle, rgba(36,91,255,0.18) 0%, rgba(99,180,255,0.04) 45%, transparent 70%);
    pointer-events: none;
  }}
  /* Swiss Architectural Grid Overlay */
  .swiss-grid {{
    position: absolute; inset: 56px 72px;
    border: 1px solid rgba(99, 180, 255, 0.18);
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    grid-template-rows: 92px 1fr 132px;
  }}
  .grid-line-v {{
    position: absolute; top: 0; bottom: 0; left: 57.5%;
    width: 1px; background: linear-gradient(180deg, rgba(99,180,255,0.28), rgba(99,180,255,0.06) 50%, rgba(99,180,255,0.28));
  }}
  .grid-line-h1 {{
    position: absolute; left: 0; right: 0; top: 92px;
    height: 1px; background: rgba(99, 180, 255, 0.18);
  }}
  .grid-line-h2 {{
    position: absolute; left: 0; right: 0; bottom: 132px;
    height: 1px; background: rgba(99, 180, 255, 0.22);
  }}
  .crosshair {{
    position: absolute; width: 11px; height: 11px;
    transform: translate(-50%, -50%);
  }}
  .crosshair::before, .crosshair::after {{
    content: ''; position: absolute; background: #63B4FF;
  }}
  .crosshair::before {{ left: 5px; top: 0; width: 1px; height: 11px; }}
  .crosshair::after {{ top: 5px; left: 0; width: 11px; height: 1px; }}

  /* Header Bar */
  .header-left {{
    grid-column: 1 / 2; grid-row: 1 / 2;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 44px;
  }}
  .vmaa-lockup {{
    display: flex; align-items: center; gap: 18px;
  }}
  .vmaa-mark {{
    width: 44px; height: 44px;
    border: 1.5px solid #63B4FF;
    background: linear-gradient(135deg, rgba(36,91,255,0.35), rgba(7,13,32,0.9));
    display: grid; grid-template-columns: repeat(2, 1fr); gap: 3px; padding: 6px;
    position: relative;
  }}
  .vmaa-mark span {{
    background: #F4F7FF; display: block;
  }}
  .vmaa-mark span:nth-child(2) {{ background: #245BFF; }}
  .vmaa-mark span:nth-child(3) {{ background: #63B4FF; }}
  .vmaa-brand-text {{
    display: flex; flex-direction: column; gap: 2px;
  }}
  .vmaa-acronym {{
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700; font-size: 22px; letter-spacing: 0.22em; color: #F4F7FF;
  }}
  .vmaa-sub {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10.5px; letter-spacing: 0.16em; color: #63B4FF; text-transform: uppercase;
  }}
  .header-right {{
    grid-column: 2 / 3; grid-row: 1 / 2;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 40px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; letter-spacing: 0.16em; color: rgba(244,247,255,0.72);
  }}
  .arrow-motif {{
    width: 34px; height: 34px;
    border: 1px solid rgba(99,180,255,0.45);
    display: flex; align-items: center; justify-content: center;
    color: #63B4FF; font-size: 18px;
  }}

  /* Main Hero Typography */
  .main-content {{
    grid-column: 1 / 2; grid-row: 2 / 3;
    padding: 68px 48px 40px 44px;
    display: flex; flex-direction: column; justify-content: center;
  }}
  .concept-tag {{
    display: inline-flex; align-items: center; gap: 12px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px; font-weight: 500;
    letter-spacing: 0.24em; color: #63B4FF;
    text-transform: uppercase;
    margin-bottom: 28px;
  }}
  .concept-tag .dot {{
    width: 8px; height: 8px; background: #245BFF;
    box-shadow: 0 0 12px #245BFF;
  }}
  .eyebrow-forum {{
    font-weight: 500; font-size: 24px;
    letter-spacing: 0.28em; color: rgba(244, 247, 255, 0.82);
    text-transform: uppercase;
    margin-bottom: 14px;
  }}
  .hero-title {{
    font-weight: 800;
    font-size: 86px;
    line-height: 1.02;
    letter-spacing: -0.025em;
    color: #F4F7FF;
    margin-bottom: 18px;
    text-shadow: 0 16px 48px rgba(7,13,32,0.8);
  }}
  .hero-title .accent {{
    background: linear-gradient(90deg, #F4F7FF 0%, #63B4FF 55%, #245BFF 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .sector-bar {{
    margin-top: 22px;
    display: inline-flex; align-items: center; gap: 20px;
    padding: 14px 26px;
    background: linear-gradient(90deg, rgba(36,91,255,0.28) 0%, rgba(16,31,69,0.65) 100%);
    border-left: 3px solid #245BFF;
    border-top: 1px solid rgba(99,180,255,0.28);
    border-right: 1px solid rgba(99,180,255,0.18);
    border-bottom: 1px solid rgba(99,180,255,0.18);
    width: fit-content;
  }}
  .sector-text {{
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600; font-size: 20px;
    letter-spacing: 0.26em; color: #F4F7FF;
  }}
  .sector-divider {{
    width: 32px; height: 1.5px; background: #63B4FF;
  }}
  .editorial-lead {{
    margin-top: 34px;
    max-width: 680px;
    font-size: 16.5px; line-height: 1.65;
    font-weight: 400;
    color: rgba(244, 247, 255, 0.72);
    border-left: 1px solid rgba(99, 180, 255, 0.25);
    padding-left: 20px;
  }}

  /* Right Architectural Callout Overlay */
  .visual-telemetry {{
    grid-column: 2 / 3; grid-row: 2 / 3;
    position: relative;
    padding: 36px 40px;
    display: flex; flex-direction: column; justify-content: space-between; align-items: flex-end;
  }}
  .telemetry-badge {{
    background: rgba(7, 13, 32, 0.72);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(99, 180, 255, 0.24);
    padding: 12px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; line-height: 1.6;
    color: rgba(244, 247, 255, 0.8);
    letter-spacing: 0.08em;
  }}
  .telemetry-badge strong {{ color: #63B4FF; font-weight: 600; }}

  /* Footer Logistics Bar */
  .footer-left {{
    grid-column: 1 / 2; grid-row: 3 / 4;
    display: grid; grid-template-columns: repeat(3, 1fr);
    align-items: center;
    padding: 0 44px;
  }}
  .meta-block {{
    display: flex; flex-direction: column; gap: 6px;
    padding-right: 24px;
    border-right: 1px solid rgba(99, 180, 255, 0.16);
  }}
  .meta-block:last-child {{ border-right: none; padding-left: 24px; }}
  .meta-block:nth-child(2) {{ padding-left: 24px; }}
  .meta-label {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; letter-spacing: 0.2em; color: #63B4FF;
    text-transform: uppercase;
  }}
  .meta-value {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700; font-size: 24px; color: #F4F7FF;
    letter-spacing: -0.01em;
  }}
  .footer-right {{
    grid-column: 2 / 3; grid-row: 3 / 4;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 40px;
    background: linear-gradient(90deg, rgba(16,31,69,0.55), rgba(7,13,32,0.82));
  }}
  .palette-strip {{
    display: flex; align-items: center; gap: 10px;
  }}
  .swatch {{
    width: 28px; height: 28px; border: 1px solid rgba(244,247,255,0.22);
  }}
  .system-stamp {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; letter-spacing: 0.14em;
    color: rgba(244,247,255,0.68);
    text-align: right;
  }}
</style>
</head>
<body>
  <div class="bg-plate"></div>
  <div class="gradient-veil"></div>
  <div class="radial-glow"></div>

  <div class="swiss-grid">
    <div class="grid-line-v"></div>
    <div class="grid-line-h1"></div>
    <div class="grid-line-h2"></div>
    <div class="crosshair" style="left: 57.5%; top: 92px;"></div>
    <div class="crosshair" style="left: 57.5%; top: calc(100% - 132px);"></div>

    <div class="header-left">
      <div class="vmaa-lockup">
        <div class="vmaa-mark">
          <span></span><span></span><span></span><span></span>
        </div>
        <div class="vmaa-brand-text">
          <div class="vmaa-acronym">VMAA · CENTRAL VIETNAM</div>
          <div class="vmaa-sub">Vietnam Mergers &amp; Acquisitions Association</div>
        </div>
      </div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:11px; letter-spacing:0.18em; color:#63B4FF;">
        EDITION 2026 // FLAGSHIP FORUM
      </div>
    </div>

    <div class="header-right">
      <span>16.0544° N, 108.2022° E · ĐÀ NẴNG</span>
      <div class="arrow-motif">↙</div>
    </div>

    <div class="main-content">
      <div class="concept-tag">
        <span class="dot"></span>
        <span>CAPITAL × TECHNOLOGY · ARCHITECTURE OF VALUE</span>
      </div>
      <div class="eyebrow-forum">DIỄN ĐÀN</div>
      <h1 class="hero-title">
        M&amp;A MIỀN TRUNG<br>
        <span class="accent">2026</span>
      </h1>
      <div class="sector-bar">
        <span class="sector-text">REAL ESTATE</span>
        <span class="sector-divider"></span>
        <span class="sector-text" style="color:#63B4FF;">TECHNOLOGY</span>
      </div>
      <p class="editorial-lead">
        Kiến trúc Giá trị Mới: Hội tụ dòng vốn chiến lược, hạ tầng bất động sản thế hệ mới và nền tảng công nghệ lõi tại tâm điểm tăng trưởng Miền Trung Việt Nam.
      </p>
    </div>

    <div class="visual-telemetry">
      <div class="telemetry-badge">
        <strong>MOTIF SYSTEM // 01–03</strong><br>
        01 · Real Estate as Modular Volume<br>
        02 · Technology as Luminous Filament<br>
        03 · M&amp;A as Structural Alignment
      </div>
      <div class="telemetry-badge" style="text-align:right;">
        <strong>DESIGN SYSTEM // RESTRAINT &amp; PRECISION</strong><br>
        Deterministic Swiss Grid · Fluted Cobalt Optics
      </div>
    </div>

    <div class="footer-left">
      <div class="meta-block">
        <span class="meta-label">DATE // NGÀY TỔ CHỨC</span>
        <span class="meta-value">13.12.2026</span>
      </div>
      <div class="meta-block">
        <span class="meta-label">TIME // THỜI GIAN</span>
        <span class="meta-value">13:30–17:30</span>
      </div>
      <div class="meta-block">
        <span class="meta-label">LOCATION // ĐỊA ĐIỂM</span>
        <span class="meta-value">Đà Nẵng, Việt Nam</span>
      </div>
    </div>

    <div class="footer-right">
      <div class="palette-strip">
        <div class="swatch" style="background:#070D20;" title="#070D20"></div>
        <div class="swatch" style="background:#101F45;" title="#101F45"></div>
        <div class="swatch" style="background:#245BFF;" title="#245BFF"></div>
        <div class="swatch" style="background:#63B4FF;" title="#63B4FF"></div>
        <div class="swatch" style="background:#F4F7FF;" title="#F4F7FF"></div>
      </div>
      <div class="system-stamp">
        ARCHITECTURE OF VALUE · KEY VISUAL MASTER<br>
        <span style="color:#63B4FF;">DETERMINISTIC TYPOGRAPHY + 3D PLATE</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------------------
# 2. COMPLETE BRAND & VISUAL IDENTITY MOODBOARD (02_VMAA_Brand_System_Moodboard.png)
# -------------------------------------------------------------------------
html_moodboard = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
{FONTS_HEAD}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #050915;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #F4F7FF;
    padding: 28px;
    display: grid;
    grid-template-columns: 380px 380px 540px 524px;
    grid-template-rows: 340px 320px 336px;
    gap: 14px;
  }}
  .tile {{
    background: #070D20;
    border: 1px solid rgba(99, 180, 255, 0.16);
    position: relative;
    overflow: hidden;
    padding: 24px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  .mono-label {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px; letter-spacing: 0.18em; color: #63B4FF;
    text-transform: uppercase;
  }}

  /* Tile 1: Digital Portal Hero (Verde Vista equivalent) */
  .tile-portal {{
    grid-column: 1 / 2; grid-row: 1 / 2;
    background: linear-gradient(145deg, #245BFF 0%, #101F45 58%, #070D20 100%);
  }}
  .portal-bar {{
    height: 22px; background: rgba(244,247,255,0.95);
    margin: -24px -24px 16px -24px;
    padding: 0 14px;
    display: flex; align-items: center; justify-content: space-between;
    font-family: 'JetBrains Mono', monospace; font-size: 9px; color: #070D20;
  }}
  .portal-arch {{
    position: absolute; right: -40px; top: 30px;
    width: 220px; height: 220px;
    border: 28px solid rgba(99,180,255,0.22);
    transform: rotate(18deg);
  }}

  /* Tile 2: Executive VIP Badge (Ouweis Madrane / Digital Chrysalis equivalent) */
  .tile-badge {{
    grid-column: 2 / 3; grid-row: 1 / 3;
    background: #080E1E;
    align-items: center; justify-content: center;
  }}
  .lanyard-clip {{
    width: 32px; height: 54px;
    border: 3px solid #9BA9C6;
    border-radius: 8px;
    margin-bottom: -10px;
    z-index: 3;
    background: linear-gradient(180deg, #D5DFEE, #6F82A8);
  }}
  .vip-pass {{
    width: 268px; height: 420px;
    border-radius: 14px;
    background:
      radial-gradient(circle at 88% 72%, rgba(99,180,255,0.75) 0%, rgba(36,91,255,0.55) 32%, rgba(16,31,69,0.95) 68%, #070D20 100%);
    border: 1px solid rgba(99,180,255,0.45);
    box-shadow: 0 28px 60px rgba(0,0,0,0.75), inset 0 1px 1px rgba(255,255,255,0.35);
    padding: 24px;
    display: flex; flex-direction: column; justify-content: space-between;
    transform: rotate(-4deg);
    position: relative;
  }}
  .vip-pass::before {{
    content: ''; position: absolute; top: 14px; left: 50%; transform: translateX(-50%);
    width: 44px; height: 8px; border-radius: 4px; background: #080E1E;
    border: 1px solid rgba(99,180,255,0.3);
  }}

  /* Tile 3: Chromatic System Grid (Brand Color tile) */
  .tile-colors {{
    grid-column: 3 / 4; grid-row: 1 / 2;
    background:
      linear-gradient(rgba(99,180,255,0.09) 1px, transparent 1px),
      linear-gradient(90deg, rgba(99,180,255,0.09) 1px, transparent 1px),
      radial-gradient(circle at 75% 65%, #245BFF 0%, #101F45 52%, #070D20 100%);
    background-size: 64px 64px, 64px 64px, 100% 100%;
  }}
  .swatch-grid {{
    display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px;
    margin-top: auto;
  }}
  .color-node {{
    height: 92px; padding: 10px;
    display: flex; flex-direction: column; justify-content: space-between;
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    border: 1px solid rgba(244,247,255,0.22);
  }}

  /* Tile 4: Executive Deal Cards & Hanging Banners (GITEX Vietnam reference) */
  .tile-banners {{
    grid-column: 4 / 5; grid-row: 1 / 2;
    background: #060B18;
    display: flex; flex-direction: row; gap: 14px; align-items: stretch;
  }}
  .hanging-banner {{
    flex: 1;
    background: linear-gradient(180deg, #070D20 0%, #101F45 48%, #245BFF 100%);
    border: 1px solid rgba(99,180,255,0.32);
    padding: 16px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}

  /* Tile 5: Valuation & Deal Velocity Metrics (42% / 400% cards) */
  .tile-metrics {{
    grid-column: 1 / 2; grid-row: 2 / 3;
    background: linear-gradient(180deg, #0B1636 0%, #183B99 100%);
  }}
  .bars-row {{
    display: flex; align-items: flex-end; gap: 8px; height: 96px; margin-top: auto;
  }}
  .bars-row div {{
    flex: 1; background: linear-gradient(180deg, #63B4FF, rgba(36,91,255,0.35));
    border-top: 2px solid #F4F7FF;
  }}

  /* Tile 6: Central Moodboard Pill + Fluted Glass Refraction (000000 glass pills) */
  .tile-center {{
    grid-column: 3 / 4; grid-row: 2 / 3;
    background-image: url('{fluted_uri}');
    background-size: cover; background-position: center;
    align-items: center; justify-content: center;
  }}
  .moodboard-frame {{
    background: rgba(7, 13, 32, 0.86);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(99, 180, 255, 0.5);
    padding: 22px 42px;
    text-align: center;
    box-shadow: 0 20px 50px rgba(0,0,0,0.8);
  }}
  .fluted-pills {{
    display: flex; gap: 6px; margin-top: 14px; justify-content: center;
  }}
  .fluted-pills span {{
    width: 26px; height: 54px; border-radius: 14px;
    border: 1px solid rgba(244,247,255,0.65);
    background: linear-gradient(180deg, rgba(7,13,32,0.8) 0%, rgba(36,91,255,0.65) 60%, #F4F7FF 100%);
  }}

  /* Tile 7: Editorial Slide System ("CONTENT" / white-cobalt bleed) */
  .tile-editorial {{
    grid-column: 4 / 5; grid-row: 2 / 3;
    background: radial-gradient(circle at 28% 54%, #070D20 0%, #101F45 38%, #245BFF 62%, #F4F7FF 92%);
  }}

  /* Tile 8: Fluted Light Curtain Texture */
  .tile-curtain {{
    grid-column: 1 / 2; grid-row: 3 / 4;
    background: repeating-linear-gradient(
      90deg,
      #070D20 0px,
      #101F45 10px,
      #245BFF 20px,
      #63B4FF 24px,
      #070D20 34px
    );
  }}
  .curtain-vignette {{
    position: absolute; inset: 0;
    background: radial-gradient(circle at 50% 45%, transparent 15%, rgba(7,13,32,0.86) 90%);
    padding: 24px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}

  /* Tile 9: Conversion / Deal Curve Card (400% card equivalent) */
  .tile-curve {{
    grid-column: 2 / 3; grid-row: 3 / 4;
    background: radial-gradient(circle at 50% 95%, rgba(36,91,255,0.55), #070D20 72%);
  }}

  /* Tile 10: Wayfinding Cube + Stage Portal ("Manar Abu Dhabi" + Light Beam) */
  .tile-wayfinding {{
    grid-column: 3 / 4; grid-row: 3 / 4;
    background: linear-gradient(90deg, #070D20 0%, #0D1E4D 50%, #070D20 100%);
    display: grid; grid-template-columns: 1fr 1fr; gap: 16px;
  }}
  .way-cube {{
    background: linear-gradient(135deg, #245BFF 0%, #101F45 100%);
    border: 1px solid #63B4FF;
    padding: 18px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}

  /* Tile 11: Isometric Report Monolith ("Stellar - Connecting the world") */
  .tile-monolith {{
    grid-column: 4 / 5; grid-row: 3 / 4;
    background: #0B101C;
    align-items: center; justify-content: center;
  }}
  .iso-book {{
    width: 390px; height: 230px;
    background:
      linear-gradient(rgba(244,247,255,0.12) 1px, transparent 1px),
      linear-gradient(90deg, rgba(244,247,255,0.12) 1px, transparent 1px),
      radial-gradient(circle at 30% 25%, #F4F7FF 0%, #63B4FF 28%, #245BFF 58%, #070D20 95%);
    background-size: 36px 36px, 36px 36px, 100% 100%;
    border: 1px solid rgba(244,247,255,0.45);
    box-shadow: -18px 22px 0 #101F45, -19px 23px 0 #63B4FF, 0 28px 50px rgba(0,0,0,0.75);
    transform: rotate(-8deg) skewX(8deg);
    padding: 22px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
</style>
</head>
<body>

  <!-- Tile 1: Digital Portal -->
  <div class="tile tile-portal">
    <div class="portal-bar">
      <span>vmaa-mientrung2026.vn</span>
      <span>REAL ESTATE × TECH</span>
    </div>
    <div class="portal-arch"></div>
    <div class="mono-label" style="color:#F4F7FF;">01 // DIGITAL PORTAL SYSTEM</div>
    <div>
      <div style="font-size:28px; font-weight:700; line-height:1.15; letter-spacing:-0.02em;">
        Architecture<br>of Value
      </div>
      <div style="font-size:12px; color:rgba(244,247,255,0.78); margin-top:8px;">
        DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · ĐÀ NẴNG
      </div>
    </div>
  </div>

  <!-- Tile 2: VIP Badge -->
  <div class="tile tile-badge">
    <div class="lanyard-clip"></div>
    <div class="vip-pass">
      <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:9px; letter-spacing:0.14em; color:#63B4FF; margin-top:12px;">
        <span>IDENTITY PASS</span>
        <span>EXECUTIVE VIP</span>
      </div>
      <div style="margin-top:18px;">
        <div style="font-size:28px; font-weight:700; line-height:1.08;">Nguyễn Minh<br>Hoàng</div>
        <div style="height:1px; background:rgba(99,180,255,0.4); margin:12px 0;"></div>
        <div style="font-size:12px; color:rgba(244,247,255,0.8);">Managing Partner · Capital Advisory</div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-family:'JetBrains Mono',monospace; font-size:9px; color:rgba(244,247,255,0.72);">
        <div>DELEGATE ID<br><strong style="color:#F4F7FF;">#VMAA-0426</strong></div>
        <div>SECTOR ACCESS<br><strong style="color:#63B4FF;">RE + TECH</strong></div>
      </div>
      <div style="display:flex; align-items:center; justify-content:space-between; padding-top:10px; border-top:1px solid rgba(99,180,255,0.28);">
        <span style="font-family:'Space Grotesk',sans-serif; font-weight:700; letter-spacing:0.18em; font-size:14px;">VMAA 2026</span>
        <span style="font-family:'JetBrains Mono',monospace; font-size:9px; color:#63B4FF;">13.12.2026</span>
      </div>
    </div>
  </div>

  <!-- Tile 3: Brand Color System -->
  <div class="tile tile-colors">
    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
      <div>
        <div class="mono-label">02 // CHROMATIC ARCHITECTURE</div>
        <div style="font-size:20px; font-weight:700; margin-top:4px;">Approved Brand Palette</div>
      </div>
      <div style="font-size:11px; color:rgba(244,247,255,0.72); max-width:240px; text-align:right;">
        Built on deep obsidian space, cobalt structural energy, and ice-blue telemetry highlights.
      </div>
    </div>
    <div class="swatch-grid">
      <div class="color-node" style="background:#070D20; color:#F4F7FF;"><span>OBSIDIAN</span><strong>#070D20</strong></div>
      <div class="color-node" style="background:#101F45; color:#F4F7FF;"><span>NAVY</span><strong>#101F45</strong></div>
      <div class="color-node" style="background:#245BFF; color:#F4F7FF;"><span>COBALT</span><strong>#245BFF</strong></div>
      <div class="color-node" style="background:#63B4FF; color:#070D20;"><span>ICE BLUE</span><strong>#63B4FF</strong></div>
      <div class="color-node" style="background:#F4F7FF; color:#070D20;"><span>WHITE</span><strong>#F4F7FF</strong></div>
    </div>
  </div>

  <!-- Tile 4: Hanging Venue Banners (GITEX Reference) -->
  <div class="tile tile-banners">
    <div class="hanging-banner">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <span class="mono-label">BANNER A</span>
        <span style="font-size:18px; color:#63B4FF;">↙</span>
      </div>
      <div style="font-size:21px; font-weight:700; line-height:1.18;">
        Building<br>Central Vietnam's<br>Capital Edge
      </div>
      <div class="mono-label" style="color:rgba(244,247,255,0.7);">REAL ESTATE · PROPTECH · M&amp;A</div>
    </div>
    <div class="hanging-banner" style="background:linear-gradient(180deg, #101F45 0%, #245BFF 75%, #63B4FF 100%);">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <span class="mono-label" style="color:#F4F7FF;">BANNER B</span>
        <span style="font-size:18px; color:#F4F7FF;">↙</span>
      </div>
      <div style="font-size:21px; font-weight:800; line-height:1.15;">
        M&amp;A MIỀN TRUNG<br>2026 · ĐÀ NẴNG
      </div>
      <div class="mono-label" style="color:#070D20; font-weight:700;">13.12.2026 | 13:30–17:30</div>
    </div>
  </div>

  <!-- Tile 5: Metric Bar Card -->
  <div class="tile tile-metrics">
    <div class="mono-label">03 // DATA TYPOGRAPHY</div>
    <div>
      <div style="font-family:'Space Grotesk',sans-serif; font-size:48px; font-weight:700; line-height:1;">+68%</div>
      <div style="font-size:12px; color:rgba(244,247,255,0.82); margin-top:4px;">Cross-border Real Estate &amp; Tech M&amp;A deal velocity</div>
    </div>
    <div class="bars-row">
      <div style="height:28%;"></div>
      <div style="height:42%;"></div>
      <div style="height:58%;"></div>
      <div style="height:76%;"></div>
      <div style="height:100%;"></div>
    </div>
  </div>

  <!-- Tile 6: Central Moodboard Identifier -->
  <div class="tile tile-center">
    <div class="moodboard-frame">
      <div class="mono-label" style="margin-bottom:6px;">VMAA M&amp;A MIỀN TRUNG 2026</div>
      <div style="font-family:'Space Grotesk',sans-serif; font-size:28px; font-weight:700; letter-spacing:0.14em;">
        THE DESIGN SYSTEM
      </div>
      <div class="fluted-pills">
        <span></span><span></span><span></span><span></span><span></span><span></span>
      </div>
    </div>
  </div>

  <!-- Tile 7: Presentation Agenda Slide -->
  <div class="tile tile-editorial">
    <div class="mono-label" style="color:#F4F7FF;">04 // DECK &amp; STAGE TYPOGRAPHY</div>
    <div style="font-size:28px; font-weight:700; letter-spacing:0.06em;">AGENDA STRUCTURE</div>
    <div style="border-top:1px solid rgba(244,247,255,0.35); border-bottom:1px solid rgba(244,247,255,0.35); padding:14px 0; display:grid; grid-template-columns:1fr 1fr; gap:8px; font-family:'JetBrains Mono',monospace; font-size:11px;">
      <div>01 · MACRO CAPITAL FLOWS</div>
      <div>04 · TECH VALUATION MODELS</div>
      <div>02 · URBAN INFRASTRUCTURE</div>
      <div>05 · STRATEGIC CONSOLIDATION</div>
      <div>03 · PROPTECH ECOSYSTEM</div>
      <div>06 · DEAL ROOM SIGNING</div>
    </div>
    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:10px;">
      <span>13.12.2026 · ĐÀ NẴNG</span>
      <span style="color:#070D20; font-weight:700;">VMAA // 2026</span>
    </div>
  </div>

  <!-- Tile 8: Fluted Optics -->
  <div class="tile tile-curtain">
    <div class="curtain-vignette">
      <div class="mono-label">05 // OPTICAL REFRACTION</div>
      <div>
        <div style="font-size:18px; font-weight:700;">Fluted Cobalt Glass</div>
        <div style="font-size:12px; color:rgba(244,247,255,0.75); margin-top:4px;">
          Physical shader motif for stage transitions &amp; speaker lower-thirds.
        </div>
      </div>
    </div>
  </div>

  <!-- Tile 9: Valuation Bell Curve -->
  <div class="tile tile-curve">
    <div style="display:flex; justify-content:space-between;">
      <span class="mono-label">SYNERGY MULTIPLE</span>
      <span class="mono-label" style="border:1px solid rgba(99,180,255,0.4); padding:2px 8px;">Q4 2026</span>
    </div>
    <svg viewBox="0 0 300 120" style="width:100%; height:120px; overflow:visible;">
      <path d="M 10 105 C 80 105, 115 18, 150 18 C 185 18, 220 105, 290 105" fill="none" stroke="#63B4FF" stroke-width="2.5"/>
      <circle cx="150" cy="18" r="6" fill="#F4F7FF" stroke="#245BFF" stroke-width="3"/>
      <line x1="150" y1="18" x2="150" y2="105" stroke="rgba(99,180,255,0.35)" stroke-dasharray="4 4"/>
    </svg>
    <div style="text-align:center;">
      <div style="font-size:11px; color:#63B4FF; font-family:'JetBrains Mono',monospace;">CAPITAL CONVERGENCE INDEX</div>
      <div style="font-family:'Space Grotesk',sans-serif; font-size:42px; font-weight:700;">400%</div>
    </div>
  </div>

  <!-- Tile 10: 3D Wayfinding Cubes -->
  <div class="tile tile-wayfinding">
    <div class="way-cube">
      <div style="display:flex; justify-content:space-between;">
        <span class="mono-label" style="color:#F4F7FF;">WAYFINDING CUBE 01</span>
        <span>↑</span>
      </div>
      <div style="font-size:20px; font-weight:700;">Main Plenary<br>Auditorium</div>
      <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(244,247,255,0.3); padding-top:10px; font-size:12px;">
        <span>Stage &amp; Keynotes</span>
        <span>←</span>
      </div>
    </div>
    <div class="way-cube" style="background:linear-gradient(135deg, #101F45 0%, #070D20 100%);">
      <div style="display:flex; justify-content:space-between;">
        <span class="mono-label">WAYFINDING CUBE 02</span>
        <span>↗</span>
      </div>
      <div style="font-size:20px; font-weight:700; color:#63B4FF;">M&amp;A Deal Room<br>&amp; VIP Lounge</div>
      <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(99,180,255,0.3); padding-top:10px; font-size:12px;">
        <span>13:30–17:30</span>
        <span>→</span>
      </div>
    </div>
  </div>

  <!-- Tile 11: Isometric Monolith Report -->
  <div class="tile tile-monolith">
    <div class="iso-book">
      <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono',monospace; font-size:11px; color:#070D20; font-weight:700;">
        <span>■ VMAA 2026</span>
        <span>ĐÀ NẴNG · VIETNAM</span>
      </div>
      <div style="font-size:24px; font-weight:800; line-height:1.15; color:#F4F7FF; text-shadow:0 4px 18px rgba(7,13,32,0.7);">
        Connecting Capital &amp;<br>Urban Intelligence<br>Through M&amp;A.
      </div>
    </div>
  </div>

</body>
</html>
"""

# -------------------------------------------------------------------------
# 3. MAIN STAGE LED SIMULATION (03_VMAA_Main_Stage_LED_Simulation.png)
#    Synthesizing BTG Pactual 3-Screen + VPERIA CX Ascending Blocks & 3D Floor Letters
# -------------------------------------------------------------------------
html_stage = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
{FONTS_HEAD}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #050811;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #F4F7FF;
    position: relative;
  }}
  .stage-photo {{
    position: absolute; inset: 0;
    background-image: url('{stage_uri}');
    background-size: cover; background-position: center;
  }}
  /* Central LED Screen Composite mapped accurately to the auditorium center screen above armchairs */
  .center-led {{
    position: absolute;
    left: 707px; top: 314px;
    width: 506px; height: 272px;
    background:
      radial-gradient(circle at 72% 42%, rgba(36,91,255,0.88) 0%, rgba(16,31,69,0.96) 52%, #070D20 100%);
    border: 1px solid rgba(99,180,255,0.45);
    box-shadow: 0 0 70px rgba(36,91,255,0.45);
    overflow: hidden;
    padding: 16px 24px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  /* Ascending Geometric Architectural Modules positioned on right-center to preserve 100% text contrast */
  .arch-bars {{
    position: absolute;
    left: 165px; bottom: 28px;
    display: flex; align-items: flex-end; gap: 9px;
    opacity: 0.24;
    pointer-events: none;
  }}
  .arch-bars div {{
    width: 28px;
    background: linear-gradient(180deg, rgba(244,247,255,0.85), rgba(36,91,255,0.1));
    border-top: 1.5px solid #63B4FF;
    transform: skewX(-14deg);
  }}
  /* Topographic Contour Lines on Top Right (inspired by BTG Pactual reference) */
  .contour-svg {{
    position: absolute; right: -10px; top: -10px;
    width: 170px; height: 150px; opacity: 0.45;
  }}
  .led-top {{
    display: flex; justify-content: space-between; align-items: center;
    z-index: 2;
    font-family: 'JetBrains Mono', monospace; font-size: 8px; letter-spacing: 0.16em; color: #63B4FF;
  }}
  .led-body {{
    display: grid; grid-template-columns: 1.42fr 0.88fr; gap: 16px;
    align-items: center; z-index: 2;
    margin-top: 2px;
  }}
  .led-title-block h2 {{
    font-size: 22px; font-weight: 800; line-height: 1.18; letter-spacing: -0.015em;
    color: #F4F7FF;
  }}
  .led-sector-pill {{
    display: inline-block; margin-top: 8px;
    padding: 4px 10px;
    background: rgba(36,91,255,0.5);
    border-left: 2px solid #63B4FF;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 8.5px; font-weight: 700; letter-spacing: 0.2em;
  }}
  .speaker-stack {{
    border-left: 1px solid rgba(99,180,255,0.35);
    padding-left: 12px;
    display: flex; flex-direction: column; gap: 6px;
    font-size: 8px; line-height: 1.32;
    background: rgba(7,13,32,0.45);
    padding-top: 6px; padding-bottom: 6px;
  }}
  .speaker-stack strong {{ color: #F4F7FF; font-size: 8.5px; display: block; }}
  .speaker-stack span {{ color: #63B4FF; }}
  /* Step-and-repeat partner row at bottom of LED screen (like BTG Pactual) */
  .led-footer {{
    z-index: 2;
    border-top: 1px solid rgba(99,180,255,0.28);
    padding-top: 6px;
    display: flex; justify-content: space-between; align-items: center;
    font-family: 'JetBrains Mono', monospace; font-size: 7.5px; letter-spacing: 0.12em;
    color: rgba(244,247,255,0.82);
  }}

  /* Left & Right Side Wing Screens mapped accurately to wing LED frames */
  .wing-led {{
    position: absolute;
    top: 448px; width: 186px; height: 110px;
    background: linear-gradient(135deg, #070D20 0%, #101F45 55%, #245BFF 100%);
    border: 1px solid rgba(99,180,255,0.45);
    padding: 12px 14px;
    display: flex; flex-direction: column; justify-content: space-between;
    box-shadow: 0 0 36px rgba(36,91,255,0.35);
  }}
  .wing-left {{ left: 387px; }}
  .wing-right {{ left: 1351px; }}

  /* Physical 3D Illuminated Letters on Stage Floor Left (inspired by VPERIA CX LEADER SUMMIT 2025) */
  .stage-floor-sign {{
    position: absolute;
    left: 472px; top: 586px;
    display: flex; align-items: center; gap: 9px;
    padding: 6px 12px;
    background: rgba(7,13,32,0.92);
    border: 1px solid rgba(99,180,255,0.45);
    border-bottom: 3px solid #63B4FF;
    box-shadow: 0 10px 28px rgba(36,91,255,0.75), 0 0 20px rgba(99,180,255,0.55);
  }}
  .stage-floor-sign .big {{
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 800; font-size: 26px; line-height: 0.95;
    color: #F4F7FF;
    text-shadow: 0 0 12px #63B4FF;
  }}
  .stage-floor-sign .small {{
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700; font-size: 9px; line-height: 1.25;
    color: #63B4FF; letter-spacing: 0.08em;
  }}

  /* Top Production Spec HUD Overlay */
  .hud-bar {{
    position: absolute; top: 28px; left: 40px; right: 40px;
    display: flex; justify-content: space-between; align-items: center;
    padding: 14px 24px;
    background: rgba(7, 13, 32, 0.82);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(99, 180, 255, 0.28);
    font-family: 'JetBrains Mono', monospace; font-size: 11px; letter-spacing: 0.14em;
  }}
</style>
</head>
<body>
  <div class="stage-photo"></div>

  <div class="hud-bar">
    <div><strong style="color:#63B4FF;">STAGE ARCHITECTURE SIMULATION // 03</strong> · PLENARY AUDITORIUM &amp; 3-SCREEN LED MATRIX</div>
    <div>ASPECT: MAIN 16:10 + WINGS 16:9 · SAFE AREA ABOVE PANELISTS VERIFIED · ĐÀ NẴNG 13.12.2026</div>
  </div>

  <!-- Left Wing Screen -->
  <div class="wing-led wing-left">
    <div style="font-family:'JetBrains Mono',monospace; font-size:7.5px; color:#63B4FF; letter-spacing:0.14em;">VMAA · CENTRAL VIETNAM</div>
    <div style="font-size:13px; font-weight:800; line-height:1.22;">M&amp;A MIỀN TRUNG<br><span style="color:#63B4FF;">2026</span></div>
    <div style="font-family:'JetBrains Mono',monospace; font-size:7.5px; color:rgba(244,247,255,0.8);">13.12.2026 · 13:30–17:30</div>
  </div>

  <!-- Center Main LED Screen -->
  <div class="center-led">
    <div class="arch-bars">
      <div style="height:40px;"></div>
      <div style="height:68px;"></div>
      <div style="height:98px;"></div>
      <div style="height:132px;"></div>
      <div style="height:110px;"></div>
      <div style="height:80px;"></div>
    </div>
    <svg class="contour-svg" viewBox="0 0 200 180">
      <path d="M40,0 Q90,90 200,70 M65,0 Q110,70 200,50 M90,0 Q130,50 200,30 M15,0 Q70,115 200,95" fill="none" stroke="#63B4FF" stroke-width="1.2"/>
    </svg>

    <div class="led-top">
      <span>VMAA · VIETNAM M&amp;A ASSOCIATION</span>
      <span>CAPITAL × TECHNOLOGY</span>
      <span>ĐÀ NẴNG · VIETNAM</span>
    </div>

    <div class="led-body">
      <div class="led-title-block">
        <div style="font-family:'JetBrains Mono',monospace; font-size:7.5px; color:#63B4FF; letter-spacing:0.18em; margin-bottom:8px;">
          PLENARY SESSION I · ARCHITECTURE OF VALUE
        </div>
        <h2>DIỄN ĐÀN M&amp;A<br>MIỀN TRUNG 2026</h2>
        <div class="led-sector-pill">REAL ESTATE — TECHNOLOGY</div>
      </div>

      <div class="speaker-stack">
        <div>
          <strong>Phiên thảo luận Chiến lược</strong>
          <span>Cấu trúc Vốn &amp; Công nghệ BĐS</span>
        </div>
        <div>
          <strong>13.12.2026 | 13:30–17:30</strong>
          <span>Đà Nẵng, Việt Nam</span>
        </div>
        <div>
          <strong>Chủ trì: Hiệp hội VMAA</strong>
          <span>Quỹ Đầu tư &amp; Tập đoàn Công nghệ</span>
        </div>
      </div>
    </div>

    <div class="led-footer">
      <span>■ VMAA 2026</span>
      <span>■ CAPITAL × TECHNOLOGY</span>
      <span>■ REAL ESTATE — TECHNOLOGY</span>
      <span>■ 13.12.2026 · ĐÀ NẴNG</span>
    </div>
  </div>

  <!-- Right Wing Screen -->
  <div class="wing-led wing-right">
    <div style="font-family:'JetBrains Mono',monospace; font-size:7.5px; color:#63B4FF; letter-spacing:0.14em;">SECTOR FOCUS</div>
    <div style="font-size:12.5px; font-weight:800; line-height:1.22;">REAL ESTATE<br><span style="color:#63B4FF;">— TECHNOLOGY</span></div>
    <div style="font-family:'JetBrains Mono',monospace; font-size:7.5px; color:rgba(244,247,255,0.8);">ĐÀ NẴNG · VIỆT NAM</div>
  </div>

  <!-- Physical 3D Illuminated Floor Sign -->
  <div class="stage-floor-sign">
    <div class="big">M&amp;A</div>
    <div class="small">MIỀN TRUNG<br>2026</div>
  </div>
</body>
</html>
"""

# -------------------------------------------------------------------------
# 4. 4-SCENE MOTION STORYBOARD SHEET (04_VMAA_Motion_Storyboard_4Scenes.png)
# -------------------------------------------------------------------------
html_storyboard = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
{FONTS_HEAD}
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #050915;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #F4F7FF;
    padding: 32px 44px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  .top-header {{
    display: flex; justify-content: space-between; align-items: flex-end;
    padding-bottom: 18px;
    border-bottom: 1px solid rgba(99, 180, 255, 0.25);
  }}
  .grid-4 {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    gap: 20px;
    height: 830px;
  }}
  .shot-card {{
    background: #070D20;
    border: 1px solid rgba(99, 180, 255, 0.24);
    display: grid;
    grid-template-columns: 1.25fr 0.75fr;
    overflow: hidden;
  }}
  .shot-viewport {{
    position: relative;
    overflow: hidden;
    background: #070D20;
    border-right: 1px solid rgba(99, 180, 255, 0.2);
    padding: 20px;
    display: flex; flex-direction: column; justify-content: space-between;
  }}
  .shot-meta {{
    padding: 20px 22px;
    display: flex; flex-direction: column; justify-content: space-between;
    background: linear-gradient(180deg, #09122B 0%, #070D20 100%);
    font-size: 12px;
  }}
  .tc-pill {{
    display: inline-block;
    padding: 4px 10px;
    background: rgba(36, 91, 255, 0.35);
    border: 1px solid #63B4FF;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; font-weight: 600; color: #F4F7FF;
    width: fit-content;
  }}
  .spec-list {{
    display: flex; flex-direction: column; gap: 8px;
    font-family: 'JetBrains Mono', monospace; font-size: 10.5px; line-height: 1.45;
    color: rgba(244,247,255,0.78);
  }}
  .spec-list strong {{ color: #63B4FF; }}
  .bottom-timeline {{
    height: 52px;
    background: #070D20;
    border: 1px solid rgba(99, 180, 255, 0.25);
    display: grid;
    grid-template-columns: 4fr 6fr 6fr 6fr;
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
  }}
  .tl-seg {{
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 18px;
    border-right: 1px solid rgba(99, 180, 255, 0.25);
  }}
</style>
</head>
<body>
  <div class="top-header">
    <div>
      <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#63B4FF; letter-spacing:0.2em;">
        PHASE 5 // TIMECODED MOTION STORYBOARD (22.0 SECONDS · 60 FPS)
      </div>
      <h1 style="font-size:30px; font-weight:800; letter-spacing:-0.02em; margin-top:4px;">
        VMAA M&amp;A MIỀN TRUNG 2026 — “ARCHITECTURE OF VALUE” OPENER
      </h1>
    </div>
    <div style="font-family:'JetBrains Mono',monospace; font-size:11px; text-align:right; color:rgba(244,247,255,0.75);">
      PIPELINE: COMFYUI (WAN 2.2 PLATES) + BLENDER 4.2 GEOMETRY NODES + DETERMINISTIC SVG TYPOGRAPHY<br>
      QUALITY GATE THRESHOLD: ≥ 80/100 · ZERO AI-GENERATED TEXT
    </div>
  </div>

  <div class="grid-4">
    <!-- SCENE 1 -->
    <div class="shot-card">
      <div class="shot-viewport" style="background:
        linear-gradient(rgba(99,180,255,0.12) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,180,255,0.12) 1px, transparent 1px),
        radial-gradient(ellipse at 50% 55%, rgba(36,91,255,0.45) 0%, #101F45 38%, #070D20 82%);
        background-size: 38px 38px, 38px 38px, 100% 100%;">
        <div class="tc-pill">SHOT 01 // 00:00:00 – 00:04:00</div>
        <svg viewBox="0 0 400 180" style="width:100%; height:180px;">
          <line x1="40" y1="140" x2="360" y2="50" stroke="#63B4FF" stroke-width="1.5" stroke-dasharray="4 4"/>
          <rect x="145" y="45" width="42" height="105" fill="rgba(16,31,69,0.85)" stroke="#245BFF" stroke-width="1.5"/>
          <rect x="200" y="30" width="52" height="120" fill="rgba(36,91,255,0.28)" stroke="#63B4FF" stroke-width="1.5"/>
          <circle cx="145" cy="45" r="3.5" fill="#F4F7FF"/>
          <circle cx="252" cy="30" r="3.5" fill="#F4F7FF"/>
        </svg>
        <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF; display:flex; justify-content:space-between;">
          <span>CAM: 35MM DOLLY PUSH-IN (0.4m/s)</span>
          <span>MOTIF: ARCHITECTURAL GRID EMERGENCE</span>
        </div>
      </div>
      <div class="shot-meta">
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF;">SCENE 01 · ESTABLISH THE WORLD</div>
          <div style="font-size:19px; font-weight:700; margin:4px 0 10px 0;">Precision &amp; Scale in Dark Space</div>
          <div class="spec-list">
            <div><strong>Visual:</strong> Sparse obsidian architectural grid emerges through a narrow cobalt (#245BFF) volumetric light slit.</div>
            <div><strong>Motion:</strong> Controlled forward camera push; high negative space establishes institutional gravity.</div>
            <div><strong>Method:</strong> Blender Cycles volumetric slit + Wan 2.2 atmospheric caustic pass.</div>
          </div>
        </div>
        <div style="padding-top:10px; border-top:1px solid rgba(99,180,255,0.2); font-family:'JetBrains Mono',monospace; font-size:10px; color:#F4F7FF;">
          AUDIO: 38Hz Sub-bass pulse + architectural room tone
        </div>
      </div>
    </div>

    <!-- SCENE 2 -->
    <div class="shot-card">
      <div class="shot-viewport" style="background-image:url('{fluted_uri}'); background-size:cover; background-position:center;">
        <div style="position:absolute; inset:0; background:rgba(7,13,32,0.42);"></div>
        <div class="tc-pill" style="position:relative; z-index:2;">SHOT 02 // 00:04:00 – 00:10:00</div>
        <svg viewBox="0 0 400 160" style="width:100%; height:160px; position:relative; z-index:2;">
          <line x1="70" y1="120" x2="210" y2="55" stroke="#63B4FF" stroke-width="2"/>
          <line x1="210" y1="55" x2="330" y2="85" stroke="#63B4FF" stroke-width="2"/>
          <circle cx="70" cy="120" r="5" fill="#F4F7FF"/>
          <circle cx="210" cy="55" r="6" fill="#63B4FF"/>
          <circle cx="330" cy="85" r="5" fill="#F4F7FF"/>
        </svg>
        <div style="position:relative; z-index:2; font-family:'JetBrains Mono',monospace; font-size:10px; color:#F4F7FF; display:flex; justify-content:space-between;">
          <span>CAM: LATERAL ORBIT 18° + PARALLAX</span>
          <span>MOTIF: DATA FILAMENTS CONNECT VOLUMES</span>
        </div>
      </div>
      <div class="shot-meta">
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF;">SCENE 02 · REVEAL THE CONNECTION</div>
          <div style="font-size:19px; font-weight:700; margin:4px 0 10px 0;">Real Estate × Technology Pathways</div>
          <div class="spec-list">
            <div><strong>Visual:</strong> Distinct modular monoliths move toward alignment as fine ice-blue (#63B4FF) filaments connect nodes.</div>
            <div><strong>Motion:</strong> Measured accelerating slide along orthogonal axes; fluted glass refracts data beams.</div>
            <div><strong>Method:</strong> Blender Geometry Nodes spline growth + ControlNet Depth conditioning.</div>
          </div>
        </div>
        <div style="padding-top:10px; border-top:1px solid rgba(99,180,255,0.2); font-family:'JetBrains Mono',monospace; font-size:10px; color:#F4F7FF;">
          AUDIO: Granular crystalline telemetry ticks (120 BPM subdivision)
        </div>
      </div>
    </div>

    <!-- SCENE 3 -->
    <div class="shot-card">
      <div class="shot-viewport" style="background-image:url('{hero_uri}'); background-size:cover; background-position:right center;">
        <div class="tc-pill">SHOT 03 // 00:10:00 – 00:16:00</div>
        <div style="margin:auto; padding:12px 20px; border:1px solid rgba(99,180,255,0.55); background:rgba(7,13,32,0.72); font-family:'Space Grotesk',sans-serif; font-size:16px; letter-spacing:0.22em;">
          CAPITAL × TECHNOLOGY
        </div>
        <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF; display:flex; justify-content:space-between;">
          <span>CAM: SLOW CRANE CONVERGENCE (50MM)</span>
          <span>CLIMAX: STRUCTURAL CONSOLIDATION</span>
        </div>
      </div>
      <div class="shot-meta">
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF;">SCENE 03 · TRANSFORM (CLIMAX)</div>
          <div style="font-size:19px; font-weight:700; margin:4px 0 10px 0;">M&amp;A as Unified Architecture</div>
          <div class="spec-list">
            <div><strong>Visual:</strong> Separate obsidian and cobalt-glass structures lock into one coherent signature monolith.</div>
            <div><strong>Motion:</strong> Mechanical precision lock at t=14.2s with internal cobalt refraction wave.</div>
            <div><strong>Method:</strong> Deterministic 3D Boolean/Constraint lock in Blender + OCIO AgX grade.</div>
          </div>
        </div>
        <div style="padding-top:10px; border-top:1px solid rgba(99,180,255,0.2); font-family:'JetBrains Mono',monospace; font-size:10px; color:#F4F7FF;">
          AUDIO: Resonant harmonic chord swell + precision mechanical lock
        </div>
      </div>
    </div>

    <!-- SCENE 4 -->
    <div class="shot-card">
      <div class="shot-viewport" style="background-image:url('{hero_uri}'); background-size:cover; background-position:center;">
        <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(7,13,32,0.95) 0%, rgba(7,13,32,0.82) 55%, rgba(7,13,32,0.2) 100%);"></div>
        <div class="tc-pill" style="position:relative; z-index:2;">SHOT 04 // 00:16:00 – 00:22:00</div>
        <div style="padding:10px 8px; position:relative; z-index:2;">
          <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF; letter-spacing:0.2em; margin-bottom:10px;">VMAA · CENTRAL VIETNAM</div>
          <div style="font-size:30px; font-weight:800; line-height:1.16; margin:4px 0 10px 0;">DIỄN ĐÀN M&amp;A<br>MIỀN TRUNG 2026</div>
          <div style="display:inline-block; padding:4px 12px; background:rgba(36,91,255,0.45); border-left:2px solid #63B4FF; font-family:'Space Grotesk',sans-serif; font-size:11px; letter-spacing:0.22em; margin-bottom:12px;">
            REAL ESTATE — TECHNOLOGY
          </div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:11px; color:#F4F7FF;">
            13.12.2026 | 13:30–17:30 · Đà Nẵng, Việt Nam
          </div>
        </div>
        <div style="position:relative; z-index:2; font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF; display:flex; justify-content:space-between;">
          <span>CAM: LOCKED STILLNESS (6.0s HOLD)</span>
          <span>100% VECTOR TYPOGRAPHY</span>
        </div>
      </div>
      <div class="shot-meta">
        <div>
          <div style="font-family:'JetBrains Mono',monospace; font-size:10px; color:#63B4FF;">SCENE 04 · REVEAL THE FORUM</div>
          <div style="font-size:19px; font-weight:700; margin:4px 0 10px 0;">Legible Brand Resolution</div>
          <div class="spec-list">
            <div><strong>Visual:</strong> Structure settles on the right; left negative space reveals official VMAA lockup &amp; forum title.</div>
            <div><strong>Motion:</strong> Restrained 6-second hold for effortless reading across LED auditorium distances.</div>
            <div><strong>Method:</strong> Motion Canvas / Inkscape SVG vector overlay composited in DaVinci/FFmpeg.</div>
          </div>
        </div>
        <div style="padding-top:10px; border-top:1px solid rgba(99,180,255,0.2); font-family:'JetBrains Mono',monospace; font-size:10px; color:#F4F7FF;">
          AUDIO: Clean acoustic tail decay · Full silence at 00:22:00
        </div>
      </div>
    </div>
  </div>

  <div class="bottom-timeline">
    <div class="tl-seg" style="background:rgba(16,31,69,0.5);">
      <span style="color:#63B4FF;">01 ESTABLISH</span><span>00:00–00:04 (4s)</span>
    </div>
    <div class="tl-seg" style="background:rgba(36,91,255,0.22);">
      <span style="color:#63B4FF;">02 CONNECT</span><span>00:04–00:10 (6s)</span>
    </div>
    <div class="tl-seg" style="background:rgba(36,91,255,0.42);">
      <span style="color:#F4F7FF; font-weight:700;">03 TRANSFORM (CLIMAX)</span><span>00:10–00:16 (6s)</span>
    </div>
    <div class="tl-seg" style="background:rgba(99,180,255,0.25); border-right:none;">
      <span style="color:#F4F7FF; font-weight:700;">04 BRAND REVEAL HOLD</span><span>00:16–00:22 (6s)</span>
    </div>
  </div>
</body>
</html>
"""

pages = [
    ("01_VMAA_Key_Visual_Master", html_key_visual),
    ("02_VMAA_Brand_System_Moodboard", html_moodboard),
    ("03_VMAA_Main_Stage_LED_Simulation", html_stage),
    ("04_VMAA_Motion_Storyboard_4Scenes", html_storyboard),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    page = context.new_page()

    for name, html_content in pages:
        html_path = EXPORTS_DIR / f"{name}.html"
        html_path.write_text(html_content, encoding="utf-8")
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(600)
        png_export = EXPORTS_DIR / f"{name}.png"
        png_brain = BRAIN_DIR / f"{name}.png"
        page.screenshot(path=str(png_export), full_page=False)
        shutil.copy(png_export, png_brain)
        print(f"Rendered {name}.png (3840x2160 Retina)")

    # Also capture the live interactive Three.js WebGL motion engine
    index_path = PROJECT_DIR / "index.html"
    if index_path.exists():
        page.goto(index_path.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(800)
        webgl_export = EXPORTS_DIR / "05_VMAA_Live_WebGL_Motion_Engine.png"
        webgl_brain = BRAIN_DIR / "05_VMAA_Live_WebGL_Motion_Engine.png"
        page.screenshot(path=str(webgl_export), full_page=False)
        shutil.copy(webgl_export, webgl_brain)
        print("Rendered 05_VMAA_Live_WebGL_Motion_Engine.png (3840x2160 Retina)")

    browser.close()
