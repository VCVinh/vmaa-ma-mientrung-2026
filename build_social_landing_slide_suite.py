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
SOCIAL_DIR = EXPORTS_DIR / "social_media"
LANDING_DIR = EXPORTS_DIR / "landing_page"
SLIDES_DIR = EXPORTS_DIR / "slide_deck"

for d in [EXPORTS_DIR, SOCIAL_DIR, LANDING_DIR, SLIDES_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


p1_path = PLATES_DIR / "purple_opt01_hero_convergence.jpg"
p2_path = PLATES_DIR / "purple_opt02_fluted_caustics.jpg"
p3_path = PLATES_DIR / "purple_opt03_ascending_cantilevers.jpg"
p6_path = PLATES_DIR / "purple_opt06_highkey_aurora_stage.jpg"

u1 = to_data_uri(p1_path)
u2 = to_data_uri(p2_path)
u3 = to_data_uri(p3_path)
u6 = to_data_uri(p6_path)

u_logo_full = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")
u_logo_wordmark = to_data_uri(PROJECT_DIR / "assets" / "vmaa_wordmark_white_transparent.png")

FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Chakra+Petch:wght@600;700&family=JetBrains+Mono:wght@500;600;700&family=Outfit:wght@200;300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&family=Space+Grotesk:wght@500;600;700&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet">
"""

SVG_VMAA_MARK = f"""
<div style="display:inline-flex; align-items:center; justify-content:center; padding:6px 14px; background:rgba(11,18,44,0.86); border:1.5px solid rgba(192,132,252,0.58); border-radius:8px; box-shadow:0 8px 22px rgba(107,45,155,0.35);">
  <img src="{u_logo_full}" alt="VMAA Official Logo" style="height:34px; width:auto; display:block; filter:drop-shadow(0 2px 8px rgba(192,132,252,0.45));"/>
</div>
"""

SVG_ARROW_NE = """
<svg width="20" height="20" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M5 17L17 5M17 5H7M17 5V15" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="square"/>
</svg>
"""

# =========================================================================
# 1. SOCIAL MEDIA PACK (1:1 Square, 4:5 Portrait, 9:16 Story/Reels, 1.91:1 Cover)
# =========================================================================

# 1A. 1:1 SQUARE POST (1080x1080 @ 2x = 2160x2160)
social_1x1_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px; height: 1080px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u1}');
    background-size: cover; background-position: 62% center;
    filter: brightness(1.12) contrast(1.08) saturate(1.18);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background:
      radial-gradient(650px 550px at 65% 42%, rgba(155,77,255,0.34) 0%, rgba(36,91,255,0.22) 50%, transparent 80%),
      radial-gradient(500px 380px at 30% 25%, rgba(233,213,255,0.20) 0%, transparent 75%);
  }}
  .shade {{
    position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(180deg,
      rgba(7,11,28,0.82) 0%,
      rgba(10,14,36,0.28) 38%,
      rgba(10,14,36,0.35) 64%,
      rgba(7,11,28,0.92) 100%
    );
  }}
  .shell {{
    position: absolute; inset: 48px;
    border: 1px solid rgba(233,213,255,0.28);
    padding: 40px 44px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.2em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>
  <div class="shade"></div>

  <div class="shell">
    <!-- Top Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:20px; border-bottom:1px solid rgba(233,213,255,0.25);">
      <div style="display:flex; align-items:center; gap:14px;">
        {SVG_VMAA_MARK}
        <div>
          <div class="grotesk" style="font-size:15px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF;">ORGANIZED BY VMAA · CENTRAL VIETNAM</div>
          <div class="mono" style="font-size:9.5px; color:#D8B4FE; margin-top:3px;">ARCHITECTURE OF VALUE · GLOBAL M&amp;A SUMMIT</div>
        </div>
      </div>
      <div class="mono" style="padding:6px 12px; background:rgba(155,77,255,0.28); border:1px solid #C084FC; border-radius:4px; font-size:10px; color:#F3E8FF;">1:1 FEED</div>
    </div>

    <!-- Center Focal Typography -->
    <div style="margin-top:auto; margin-bottom:28px;">
      <div style="display:inline-flex; align-items:center; gap:10px; padding:6px 16px; background:rgba(107,45,155,0.55); border:1px solid #E9D5FF; border-radius:999px; margin-bottom:18px; box-shadow:0 0 24px rgba(155,77,255,0.5);">
        <span style="width:8px; height:8px; border-radius:50%; background:#63B4FF; box-shadow:0 0 10px #63B4FF;"></span>
        <span class="mono" style="font-size:10.5px; font-weight:600; color:#FFFFFF;">ĐÀ NẴNG, VIỆT NAM · 2026 EDITION</span>
      </div>

      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:32px; letter-spacing:0.42em; color:#E9D5FF; text-shadow:0 0 24px rgba(155,77,255,0.9);">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:20px; white-space:nowrap;">
        <span style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:122px; line-height:0.94; letter-spacing:-0.03em; color:#FFFFFF; text-shadow:0 0 32px rgba(155,77,255,0.75), 0 0 64px rgba(36,91,255,0.6);">
          M&amp;A
        </span>
        <span style="font-family:'Outfit',sans-serif; font-weight:800; font-size:106px; line-height:0.94; color:transparent; -webkit-text-stroke:2.2px #E9D5FF; filter:drop-shadow(0 0 20px rgba(155,77,255,0.9));">
          2026
        </span>
      </div>

      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:84px; line-height:1.04; letter-spacing:-0.015em; margin-top:4px; white-space:nowrap; background:linear-gradient(90deg, #FFFFFF 0%, #F3E8FF 50%, #93C5FD 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; filter:drop-shadow(0 0 28px rgba(155,77,255,0.8));">
        MIỀN TRUNG
      </div>

      <div style="margin-top:26px;">
        <div style="display:inline-flex; align-items:center; gap:18px; padding:13px 28px; background:linear-gradient(90deg, #6B2D9B 0%, #9B4DFF 45%, #245BFF 100%); border:1.5px solid #E9D5FF; border-left:5px solid #FFFFFF; border-radius:4px; box-shadow:0 0 32px rgba(155,77,255,0.65);">
          <span class="grotesk" style="font-size:19px; font-weight:700; letter-spacing:0.3em; color:#FFFFFF;">REAL ESTATE — TECHNOLOGY</span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    <!-- Bottom Logistics Bar -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-top:20px; border-top:1px solid rgba(233,213,255,0.28); white-space:nowrap;">
      <div>
        <div class="mono" style="font-size:10px; color:#C084FC; margin-bottom:3px;">DATE</div>
        <div class="grotesk" style="font-size:24px; font-weight:700; color:#FFFFFF;">13.12.2026</div>
      </div>
      <div style="width:1.5px; height:34px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
      <div>
        <div class="mono" style="font-size:10px; color:#63B4FF; margin-bottom:3px;">TIME</div>
        <div class="grotesk" style="font-size:24px; font-weight:700; color:#FFFFFF;">13:30–17:30</div>
      </div>
      <div style="width:1.5px; height:34px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
      <div>
        <div class="mono" style="font-size:10px; color:#E9D5FF; margin-bottom:3px;">LOCATION</div>
        <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:24px; font-weight:800; color:#FFFFFF;">Đà Nẵng, Việt Nam</div>
      </div>
    </div>
  </div>
</body></html>"""


# 1B. 4:5 PORTRAIT FEED POST (1080x1350 @ 2x = 2160x2700)
social_4x5_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px; height: 1350px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u2}');
    background-size: cover; background-position: 55% center;
    filter: brightness(1.12) contrast(1.08) saturate(1.18);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background:
      radial-gradient(750px 650px at 55% 38%, rgba(155,77,255,0.36) 0%, rgba(36,91,255,0.24) 55%, transparent 82%);
  }}
  .shade {{
    position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(180deg,
      rgba(7,11,28,0.82) 0%,
      rgba(10,14,36,0.18) 32%,
      rgba(10,14,36,0.36) 58%,
      rgba(7,11,28,0.94) 100%
    );
  }}
  .shell {{
    position: absolute; inset: 52px;
    border: 1px solid rgba(233,213,255,0.30);
    padding: 44px 48px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.2em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>
  <div class="shade"></div>

  <div class="shell">
    <!-- Top Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:22px; border-bottom:1px solid rgba(233,213,255,0.26);">
      <div style="display:flex; align-items:center; gap:14px;">
        {SVG_VMAA_MARK}
        <div>
          <div class="grotesk" style="font-size:15px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF;">ORGANIZED BY VMAA · CENTRAL VIETNAM</div>
          <div class="mono" style="font-size:9.5px; color:#D8B4FE; margin-top:3px;">HIỆP HỘI MUA BÁN &amp; SÁP NHẬP DOANH NGHIỆP VIỆT NAM</div>
        </div>
      </div>
      <div class="mono" style="padding:6px 12px; background:rgba(155,77,255,0.32); border:1px solid #E9D5FF; border-radius:4px; font-size:10px; color:#FFFFFF;">4:5 PORTRAIT</div>
    </div>

    <!-- Upper-Middle 3D Showcase Breathing Room -->
    <div style="margin-top:auto; margin-bottom:36px;">
      <div style="display:inline-flex; align-items:center; gap:10px; padding:7px 18px; background:rgba(107,45,155,0.55); border:1px solid #E9D5FF; border-radius:999px; margin-bottom:22px; box-shadow:0 0 26px rgba(155,77,255,0.55);">
        <span style="width:8px; height:8px; border-radius:50%; background:#E9D5FF; box-shadow:0 0 12px #FFFFFF;"></span>
        <span class="mono" style="font-size:11px; font-weight:600; color:#FFFFFF; letter-spacing:0.24em;">ARCHITECTURE OF VALUE · 2026 EDITION</span>
      </div>

      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:34px; letter-spacing:0.44em; color:#E9D5FF; text-shadow:0 0 24px rgba(155,77,255,0.9); margin-bottom:6px;">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:22px; white-space:nowrap;">
        <span style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:128px; line-height:0.94; letter-spacing:-0.03em; color:#FFFFFF; text-shadow:0 0 34px rgba(155,77,255,0.8), 0 0 68px rgba(36,91,255,0.6);">
          M&amp;A
        </span>
        <span style="font-family:'Caveat',cursive; font-weight:700; font-size:98px; color:#E9D5FF; text-shadow:0 0 28px #9B4DFF, 0 0 54px #245BFF; transform:rotate(-4deg) translateY(-8px); display:inline-block;">
          Miền Trung
        </span>
      </div>

      <div style="display:flex; align-items:center; gap:24px; margin-top:16px; white-space:nowrap;">
        <span style="font-family:'Outfit',sans-serif; font-weight:200; font-size:84px; line-height:0.9; color:#FFFFFF; text-shadow:0 0 28px rgba(155,77,255,0.85);">
          20<span style="color:#C084FC; font-weight:300;">/</span>26
        </span>
        <div style="height:52px; width:2px; background:linear-gradient(180deg, #E9D5FF, #9B4DFF, #245BFF);"></div>
        <div style="display:inline-flex; align-items:center; gap:16px; padding:14px 26px; background:linear-gradient(90deg, #6B2D9B 0%, #9B4DFF 45%, #245BFF 100%); border:1.5px solid #E9D5FF; border-left:5px solid #FFFFFF; border-radius:4px; box-shadow:0 0 34px rgba(155,77,255,0.65);">
          <span class="grotesk" style="font-size:18.5px; font-weight:700; letter-spacing:0.28em; color:#FFFFFF;">REAL ESTATE — TECHNOLOGY</span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    <!-- Bottom Logistics Card -->
    <div style="background:rgba(10,16,38,0.78); border:1px solid rgba(192,132,252,0.45); border-radius:8px; padding:24px 30px; display:flex; justify-content:space-between; align-items:center; backdrop-filter:blur(14px); box-shadow:0 12px 36px rgba(0,0,0,0.5);">
      <div>
        <div class="mono" style="font-size:10px; color:#C084FC; margin-bottom:4px;">DATE</div>
        <div class="grotesk" style="font-size:25px; font-weight:700; color:#FFFFFF;">13.12.2026</div>
      </div>
      <div style="width:1.5px; height:38px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
      <div>
        <div class="mono" style="font-size:10px; color:#63B4FF; margin-bottom:4px;">TIME</div>
        <div class="grotesk" style="font-size:25px; font-weight:700; color:#FFFFFF;">13:30–17:30</div>
      </div>
      <div style="width:1.5px; height:38px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
      <div>
        <div class="mono" style="font-size:10px; color:#E9D5FF; margin-bottom:4px;">LOCATION</div>
        <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:25px; font-weight:800; color:#FFFFFF;">Đà Nẵng, Việt Nam</div>
      </div>
    </div>
  </div>
</body></html>"""


# 1C. 9:16 VERTICAL STORY / REELS / TIKTOK / STAGE STANDEE (1080x1920 @ 2x = 2160x3840)
social_9x16_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px; height: 1920px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u1}');
    background-size: cover; background-position: 64% center;
    filter: brightness(1.14) contrast(1.08) saturate(1.2);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background:
      radial-gradient(800px 900px at 55% 45%, rgba(155,77,255,0.36) 0%, rgba(36,91,255,0.24) 55%, transparent 85%);
  }}
  .shade {{
    position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(180deg,
      rgba(7,11,28,0.88) 0%,
      rgba(10,14,36,0.22) 28%,
      rgba(10,14,36,0.26) 52%,
      rgba(7,11,28,0.94) 100%
    );
  }}
  .shell {{
    position: absolute; inset: 72px 56px;
    border: 1.5px solid rgba(233,213,255,0.32);
    padding: 52px 48px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.22em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>
  <div class="shade"></div>

  <div class="shell">
    <!-- Top Story / Standee Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:26px; border-bottom:1px solid rgba(233,213,255,0.28);">
      <div style="display:flex; align-items:center; gap:16px;">
        {SVG_VMAA_MARK}
        <div>
          <div class="grotesk" style="font-size:16px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF;">ORGANIZED BY VMAA</div>
          <div class="mono" style="font-size:10px; color:#D8B4FE; margin-top:4px;">CENTRAL VIETNAM · 2026 EDITION</div>
        </div>
      </div>
      <div class="mono" style="padding:7px 14px; background:rgba(155,77,255,0.32); border:1px solid #E9D5FF; border-radius:4px; font-size:10.5px; color:#FFFFFF;">9:16 STORY / STANDEE</div>
    </div>

    <!-- Center-Bottom Hero Stack -->
    <div style="margin-top:auto; margin-bottom:54px;">
      <div style="display:inline-flex; align-items:center; gap:12px; padding:8px 20px; background:rgba(107,45,155,0.55); border:1px solid #E9D5FF; border-radius:999px; margin-bottom:28px; box-shadow:0 0 28px rgba(155,77,255,0.6);">
        <span style="width:9px; height:9px; border-radius:50%; background:#63B4FF; box-shadow:0 0 12px #63B4FF;"></span>
        <span class="mono" style="font-size:11.5px; font-weight:600; color:#FFFFFF;">ARCHITECTURE OF VALUE</span>
      </div>

      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:38px; letter-spacing:0.44em; color:#E9D5FF; text-shadow:0 0 24px rgba(155,77,255,0.9); margin-bottom:8px;">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:24px; white-space:nowrap;">
        <span style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:136px; line-height:0.92; letter-spacing:-0.03em; color:#FFFFFF; text-shadow:0 0 36px rgba(155,77,255,0.85), 0 0 72px rgba(36,91,255,0.65);">
          M&amp;A
        </span>
        <span style="font-family:'Outfit',sans-serif; font-weight:800; font-size:112px; line-height:0.92; color:transparent; -webkit-text-stroke:2.4px #E9D5FF; filter:drop-shadow(0 0 24px rgba(155,77,255,0.95));">
          2026
        </span>
      </div>

      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:90px; line-height:1.05; letter-spacing:-0.015em; margin-top:8px; white-space:nowrap; background:linear-gradient(90deg, #FFFFFF 0%, #F3E8FF 50%, #93C5FD 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; filter:drop-shadow(0 0 32px rgba(155,77,255,0.85));">
        MIỀN TRUNG
      </div>

      <div style="margin-top:34px;">
        <div style="display:flex; justify-content:space-between; align-items:center; padding:18px 30px; background:linear-gradient(90deg, #6B2D9B 0%, #9B4DFF 48%, #245BFF 100%); border:1.5px solid #E9D5FF; border-left:6px solid #FFFFFF; border-radius:4px; box-shadow:0 0 38px rgba(155,77,255,0.7);">
          <span class="grotesk" style="font-size:21px; font-weight:700; letter-spacing:0.3em; color:#FFFFFF;">REAL ESTATE — TECHNOLOGY</span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    <!-- Bottom Vertical Logistics Stack -->
    <div style="background:rgba(10,16,38,0.84); border:1px solid rgba(192,132,252,0.5); border-radius:10px; padding:30px 34px; display:flex; flex-direction:column; gap:20px; backdrop-filter:blur(16px);">
      <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:18px; border-bottom:1px solid rgba(233,213,255,0.2);">
        <div>
          <div class="mono" style="font-size:11px; color:#C084FC; margin-bottom:4px;">DATE</div>
          <div class="grotesk" style="font-size:30px; font-weight:700; color:#FFFFFF;">13.12.2026</div>
        </div>
        <div style="width:1.5px; height:42px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
        <div style="text-align:right;">
          <div class="mono" style="font-size:11px; color:#63B4FF; margin-bottom:4px;">TIME</div>
          <div class="grotesk" style="font-size:30px; font-weight:700; color:#FFFFFF;">13:30–17:30</div>
        </div>
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
          <div class="mono" style="font-size:11px; color:#E9D5FF; margin-bottom:4px;">LOCATION</div>
          <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:28px; font-weight:800; color:#FFFFFF;">Đà Nẵng, Việt Nam</div>
        </div>
        <div style="padding:10px 18px; background:linear-gradient(135deg, #9B4DFF, #245BFF); border-radius:4px; font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; letter-spacing:0.2em; color:#FFFFFF;">
          VMAA · 2026
        </div>
      </div>
    </div>
  </div>
</body></html>"""


# 1D. 1.91:1 EVENT COVER & OPENGRAPH LINK PREVIEW (1200x628 @ 2x = 2400x1256)
social_og_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1200px; height: 628px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u1}');
    background-size: cover; background-position: center;
    filter: brightness(1.12) contrast(1.08) saturate(1.18);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background: radial-gradient(680px 440px at 74% 48%, rgba(155,77,255,0.34) 0%, rgba(36,91,255,0.22) 50%, transparent 82%);
  }}
  .shade {{
    position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(90deg, rgba(7,11,28,0.84) 0%, rgba(12,16,42,0.56) 36%, rgba(0,0,0,0) 66%);
  }}
  .shell {{
    position: absolute; inset: 32px 44px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.2em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>
  <div class="shade"></div>

  <div class="shell">
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:14px; border-bottom:1px solid rgba(233,213,255,0.24);">
      <div style="display:flex; align-items:center; gap:12px;">
        {SVG_VMAA_MARK}
        <span class="grotesk" style="font-size:13px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF;">ORGANIZED BY VMAA · CENTRAL VIETNAM</span>
      </div>
      <span class="mono" style="padding:5px 12px; background:rgba(155,77,255,0.3); border:1px solid #C084FC; border-radius:4px; font-size:9.5px; color:#F3E8FF;">1.91:1 EVENT COVER &amp; OG LINK</span>
    </div>

    <div style="my:auto;">
      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:24px; letter-spacing:0.4em; color:#E9D5FF; margin-bottom:4px;">DIỄN ĐÀN</div>
      <div style="display:flex; align-items:baseline; gap:18px; white-space:nowrap;">
        <span style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:88px; line-height:0.94; letter-spacing:-0.03em; color:#FFFFFF; text-shadow:0 0 28px rgba(155,77,255,0.75);">M&amp;A</span>
        <span style="font-family:'Outfit',sans-serif; font-weight:800; font-size:76px; line-height:0.94; color:transparent; -webkit-text-stroke:2px #E9D5FF;">2026</span>
      </div>
      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:60px; line-height:1.05; letter-spacing:-0.015em; background:linear-gradient(90deg, #FFFFFF 0%, #E9D5FF 55%, #93C5FD 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
        MIỀN TRUNG
      </div>
      <div style="margin-top:16px;">
        <div style="display:inline-flex; align-items:center; gap:14px; padding:10px 22px; background:linear-gradient(90deg, #6B2D9B 0%, #9B4DFF 48%, #245BFF 100%); border:1.5px solid #E9D5FF; border-left:4px solid #FFFFFF; border-radius:4px;">
          <span class="grotesk" style="font-size:14px; font-weight:700; letter-spacing:0.28em; color:#FFFFFF;">REAL ESTATE — TECHNOLOGY</span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; padding-top:14px; border-top:1px solid rgba(233,213,255,0.24);">
      <div style="display:flex; align-items:center; gap:28px;">
        <span class="grotesk" style="font-size:18px; font-weight:700; color:#FFFFFF;">13.12.2026</span>
        <span style="color:#9B4DFF;">·</span>
        <span class="grotesk" style="font-size:18px; font-weight:700; color:#63B4FF;">13:30–17:30</span>
        <span style="color:#9B4DFF;">·</span>
        <span style="font-family:'Plus Jakarta Sans',sans-serif; font-size:18px; font-weight:800; color:#FFFFFF;">Đà Nẵng, Việt Nam</span>
      </div>
      <span class="mono" style="font-size:10px; color:#E9D5FF;">ARCHITECTURE OF VALUE</span>
    </div>
  </div>
</body></html>"""


# =========================================================================
# 2. LANDING PAGE HERO & ABOVE-THE-FOLD WEB UI (1920x1080 @ 2x = 3840x2160)
# =========================================================================
landing_page_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u1}');
    background-size: cover; background-position: center;
    filter: brightness(1.10) contrast(1.08) saturate(1.16);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background:
      radial-gradient(960px 680px at 70% 44%, rgba(155,77,255,0.34) 0%, rgba(36,91,255,0.22) 50%, transparent 82%);
  }}
  .left-grad {{
    position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(90deg, rgba(7,11,28,0.86) 0%, rgba(12,16,42,0.58) 38%, rgba(0,0,0,0) 66%);
  }}
  .bottom-grad {{
    position: absolute; left: 0; right: 0; bottom: 0; height: 260px; pointer-events: none;
    background: linear-gradient(180deg, transparent 0%, rgba(7,11,28,0.92) 65%, #070D20 100%);
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.2em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
  /* Sticky Glass Navigation Bar */
  .navbar {{
    position: absolute; top: 0; left: 0; right: 0; height: 88px;
    padding: 0 76px;
    background: rgba(7, 13, 32, 0.72);
    border-bottom: 1px solid rgba(233, 213, 255, 0.22);
    backdrop-filter: blur(18px);
    display: flex; justify-content: space-between; align-items: center;
    z-index: 20;
  }}
  .nav-links {{
    display: flex; align-items: center; gap: 36px;
    font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 0.16em; color: #E9D5FF;
  }}
  .cta-primary {{
    padding: 15px 32px;
    background: linear-gradient(90deg, #9B4DFF 0%, #245BFF 100%);
    border: 1.5px solid #FFFFFF;
    border-radius: 6px;
    font-family: 'Space Grotesk', sans-serif; font-size: 14px; font-weight: 700; letter-spacing: 0.2em; color: #FFFFFF;
    box-shadow: 0 0 32px rgba(155, 77, 255, 0.75);
    display: inline-flex; align-items: center; gap: 12px;
  }}
  .cta-secondary {{
    padding: 15px 28px;
    background: rgba(14, 22, 52, 0.72);
    border: 1.5px solid rgba(192, 132, 252, 0.65);
    border-radius: 6px;
    font-family: 'Space Grotesk', sans-serif; font-size: 14px; font-weight: 700; letter-spacing: 0.18em; color: #E9D5FF;
    backdrop-filter: blur(12px);
  }}
  .feature-card {{
    background: rgba(11, 18, 44, 0.80);
    border: 1px solid rgba(192, 132, 252, 0.38);
    border-top: 3px solid #9B4DFF;
    border-radius: 8px;
    padding: 20px 26px;
    backdrop-filter: blur(16px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
  }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>
  <div class="left-grad"></div>
  <div class="bottom-grad"></div>

  <!-- Top Sticky Web Navigation Bar -->
  <div class="navbar">
    <div style="display:flex; align-items:center; gap:16px;">
      {SVG_VMAA_MARK}
      <div>
        <div class="grotesk" style="font-size:16px; font-weight:700; letter-spacing:0.22em; color:#FFFFFF;">VMAA · CENTRAL VIETNAM</div>
        <div class="mono" style="font-size:9.5px; color:#C084FC;">OFFICIAL SUMMIT PORTAL · 13.12.2026</div>
      </div>
    </div>

    <div class="nav-links">
      <span style="color:#FFFFFF; border-bottom:2px solid #9B4DFF; padding-bottom:4px;">OVERVIEW</span>
      <span>ARCHITECTURE OF VALUE</span>
      <span>KEYNOTE SPEAKERS</span>
      <span>DEAL ROOM</span>
      <span>AGENDA (13:30–17:30)</span>
      <span>SPONSORS</span>
    </div>

    <div style="display:flex; align-items:center; gap:16px;">
      <span class="mono" style="padding:6px 12px; background:rgba(36,91,255,0.28); border:1px solid #63B4FF; border-radius:4px; font-size:10px; color:#63B4FF;">VI / EN</span>
      <div class="cta-primary" style="padding:11px 22px; font-size:12px;">REGISTER VIP PASS {SVG_ARROW_NE}</div>
    </div>
  </div>

  <!-- Main Above-the-Fold Hero Content -->
  <div style="position:absolute; top:142px; left:76px; right:76px; bottom:42px; display:flex; flex-direction:column; justify-content:space-between; z-index:15;">
    <div style="max-width:960px; margin-top:16px;">
      <div style="display:inline-flex; align-items:center; gap:12px; padding:7px 18px; background:rgba(107,45,155,0.5); border:1px solid #E9D5FF; border-radius:999px; margin-bottom:22px; box-shadow:0 0 26px rgba(155,77,255,0.5);">
        <span style="width:8px; height:8px; border-radius:50%; background:#63B4FF; box-shadow:0 0 12px #63B4FF;"></span>
        <span class="mono" style="font-size:11px; font-weight:600; color:#FFFFFF;">GLOBAL CONFERENCE LANDING PAGE · 13.12.2026 · ĐÀ NẴNG</span>
      </div>

      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:34px; letter-spacing:0.42em; color:#E9D5FF; text-shadow:0 0 24px rgba(155,77,255,0.85); margin-bottom:6px;">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:24px; white-space:nowrap;">
        <span style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:118px; line-height:0.94; letter-spacing:-0.03em; color:#FFFFFF; text-shadow:0 0 32px rgba(155,77,255,0.75);">
          M&amp;A
        </span>
        <span style="font-family:'Outfit',sans-serif; font-weight:800; font-size:104px; line-height:0.94; color:transparent; -webkit-text-stroke:2.2px #E9D5FF; filter:drop-shadow(0 0 20px rgba(155,77,255,0.9));">
          2026
        </span>
      </div>

      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:82px; line-height:1.05; letter-spacing:-0.015em; margin-top:4px; white-space:nowrap; background:linear-gradient(90deg, #FFFFFF 0%, #F3E8FF 50%, #93C5FD 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
        MIỀN TRUNG
      </div>

      <!-- Sector Subtitle + Dual Conversion CTAs -->
      <div style="display:flex; align-items:center; gap:18px; margin-top:28px; white-space:nowrap;">
        <div style="padding:14px 26px; background:linear-gradient(90deg, #6B2D9B 0%, #9B4DFF 48%, #245BFF 100%); border:1.5px solid #E9D5FF; border-left:5px solid #FFFFFF; border-radius:4px; font-family:'Space Grotesk',sans-serif; font-size:18px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF; box-shadow:0 0 32px rgba(155,77,255,0.6); white-space:nowrap;">
          REAL ESTATE — TECHNOLOGY
        </div>
        <div class="cta-primary" style="white-space:nowrap; padding:14px 26px; font-size:13.5px;">ĐĂNG KÝ THAM DỰ VIP {SVG_ARROW_NE}</div>
        <div class="cta-secondary" style="white-space:nowrap; padding:14px 24px; font-size:13.5px;">TẢI HỒ SƠ DIỄN ĐÀN (PDF)</div>
      </div>
    </div>

    <!-- Bottom Above-the-Fold 4-Column Event Highlights & Logistics Strip -->
    <div style="display:grid; grid-template-columns: 1.3fr 1fr 1fr 1fr; gap:22px;">
      <div class="feature-card" style="border-top-color:#FFFFFF; background:linear-gradient(135deg, rgba(107,45,155,0.55), rgba(14,22,52,0.88));">
        <div class="mono" style="font-size:10px; color:#E9D5FF; margin-bottom:6px;">DATE · TIME · VENUE</div>
        <div class="grotesk" style="font-size:24px; font-weight:700; color:#FFFFFF;">13.12.2026 · 13:30–17:30</div>
        <div style="font-size:15px; font-weight:700; color:#63B4FF; margin-top:4px;">Đà Nẵng, Việt Nam · Organized by VMAA</div>
      </div>
      <div class="feature-card">
        <div class="mono" style="font-size:10px; color:#C084FC; margin-bottom:6px;">PILLAR 01 · REAL ESTATE</div>
        <div class="grotesk" style="font-size:20px; font-weight:700; color:#FFFFFF;">Cấu trúc Vốn &amp; Quỹ Đất</div>
        <div style="font-size:13px; color:#CBD5E1; margin-top:4px;">Tái cấu trúc danh mục dự án &amp; dòng vốn FDI chiến lược Miền Trung</div>
      </div>
      <div class="feature-card" style="border-top-color:#245BFF;">
        <div class="mono" style="font-size:10px; color:#63B4FF; margin-bottom:6px;">PILLAR 02 · TECHNOLOGY</div>
        <div class="grotesk" style="font-size:20px; font-weight:700; color:#FFFFFF;">PropTech &amp; Định Giá AI</div>
        <div style="font-size:13px; color:#CBD5E1; margin-top:4px;">Hạ tầng số, dữ liệu định giá &amp; chuyển đổi số tài sản</div>
      </div>
      <div class="feature-card" style="border-top-color:#63B4FF;">
        <div class="mono" style="font-size:10px; color:#E9D5FF; margin-bottom:6px;">PILLAR 03 · DEAL MATCHING</div>
        <div class="grotesk" style="font-size:20px; font-weight:700; color:#FFFFFF;">1:1 Institutional Deal Room</div>
        <div style="font-size:13px; color:#CBD5E1; margin-top:4px;">Kết nối trực tiếp Quỹ đầu tư quốc tế, Chủ đầu tư &amp; Tập đoàn Công nghệ</div>
      </div>
    </div>
  </div>
</body></html>"""


# =========================================================================
# 3. PRESENTATION SLIDE DECK SUITE (16:9 1920x1080 @ 2x = 3840x2160)
#    - Slide 02: Executive Agenda & Timeline (13:30–17:30)
#    - Slide 03: Keynote & Panelist Spotlight Slide
#    - Slide 04: M&A Data & Valuation Architecture Content Slide
# =========================================================================

slide_agenda_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u3}');
    background-size: cover; background-position: center;
    opacity: 0.42; filter: brightness(1.1) saturate(1.2);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background:
      radial-gradient(900px 600px at 82% 28%, rgba(155,77,255,0.32) 0%, rgba(36,91,255,0.22) 55%, transparent 85%),
      radial-gradient(700px 500px at 18% 80%, rgba(107,45,155,0.28) 0%, transparent 80%);
  }}
  .shell {{
    position: absolute; inset: 52px 72px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.2em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
  .agenda-row {{
    display: grid; grid-template-columns: 220px 1fr 240px; align-items: center; gap: 28px;
    padding: 20px 30px;
    background: rgba(11, 18, 44, 0.78);
    border: 1px solid rgba(192, 132, 252, 0.32);
    border-left: 5px solid #9B4DFF;
    border-radius: 6px;
    backdrop-filter: blur(14px);
  }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>

  <div class="shell">
    <!-- Top Slide Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:20px; border-bottom:1px solid rgba(233,213,255,0.24);">
      <div style="display:flex; align-items:center; gap:16px;">
        {SVG_VMAA_MARK}
        <div>
          <div class="grotesk" style="font-size:16px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF;">DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · REAL ESTATE — TECHNOLOGY</div>
          <div class="mono" style="font-size:10px; color:#C084FC; margin-top:3px;">SLIDE 02 // EXECUTIVE PROGRAM &amp; AGENDA TIMELINE</div>
        </div>
      </div>
      <div class="mono" style="font-size:12px; color:#E9D5FF;">13.12.2026 · 13:30–17:30 · ĐÀ NẴNG</div>
    </div>

    <!-- Slide Title + 5 Agenda Blocks -->
    <div style="my:auto;">
      <div style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom:28px;">
        <div>
          <div class="mono" style="font-size:11px; color:#63B4FF; margin-bottom:8px;">PROGRAM ARCHITECTURE · AFTERNOON PLENARY</div>
          <div style="font-size:48px; font-weight:800; letter-spacing:-0.02em; color:#FFFFFF; text-shadow:0 0 28px rgba(155,77,255,0.6);">
            LỊCH TRÌNH DIỄN ĐÀN <span style="color:#C084FC;">13:30 – 17:30</span>
          </div>
        </div>
        <div style="padding:10px 20px; background:linear-gradient(90deg, #6B2D9B, #245BFF); border:1px solid #E9D5FF; border-radius:4px; font-family:'Space Grotesk',sans-serif; font-size:13px; font-weight:700; letter-spacing:0.2em;">
          16:9 PRESENTATION SLIDE
        </div>
      </div>

      <div style="display:flex; flex-direction:column; gap:14px;">
        <div class="agenda-row" style="border-left-color:#63B4FF;">
          <div class="grotesk" style="font-size:26px; font-weight:700; color:#63B4FF;">13:30 – 14:00</div>
          <div>
            <div style="font-size:21px; font-weight:700; color:#FFFFFF;">Đón khách VIP &amp; Khai mở Không gian Kết nối Đầu tư (VIP Deal Lounge)</div>
            <div style="font-size:14px; color:#CBD5E1; margin-top:3px;">Check-in đại biểu, giao lưu trực tiếp giữa các Quỹ đầu tư, Chủ đầu tư BĐS &amp; Doanh nghiệp Công nghệ</div>
          </div>
          <div class="mono" style="font-size:11px; color:#E9D5FF; text-align:right;">VIP NETWORKING</div>
        </div>

        <div class="agenda-row" style="border-left-color:#9B4DFF;">
          <div class="grotesk" style="font-size:26px; font-weight:700; color:#E9D5FF;">14:00 – 14:30</div>
          <div>
            <div style="font-size:21px; font-weight:700; color:#FFFFFF;">Phát biểu Khai mạc VMAA &amp; Báo cáo Toàn cảnh M&amp;A Miền Trung 2026</div>
            <div style="font-size:14px; color:#CBD5E1; margin-top:3px;">Tầm nhìn chiến lược của Hiệp hội Mua bán &amp; Sáp nhập Doanh nghiệp Việt Nam (VMAA) tại tâm điểm Đà Nẵng</div>
          </div>
          <div class="mono" style="font-size:11px; color:#C084FC; text-align:right;">OPENING KEYNOTE</div>
        </div>

        <div class="agenda-row" style="border-left-color:#245BFF; background:linear-gradient(90deg, rgba(107,45,155,0.42), rgba(11,18,44,0.85)); border-color:#C084FC;">
          <div class="grotesk" style="font-size:26px; font-weight:700; color:#FFFFFF;">14:30 – 15:30</div>
          <div>
            <div style="font-size:21px; font-weight:700; color:#FFFFFF;">Phiên Trọng tâm 1: Tái cấu trúc Dòng vốn Bất động sản &amp; Hạ tầng Công nghệ</div>
            <div style="font-size:14px; color:#E9D5FF; margin-top:3px;">Architecture of Value: Hợp nhất tài sản thực (Real Estate) và hệ sinh thái công nghệ định giá (PropTech / AI)</div>
          </div>
          <div class="mono" style="font-size:11px; color:#63B4FF; text-align:right;">CORE TRACK 01–02</div>
        </div>

        <div class="agenda-row" style="border-left-color:#EC4899;">
          <div class="grotesk" style="font-size:26px; font-weight:700; color:#F472B6;">15:30 – 16:45</div>
          <div>
            <div style="font-size:21px; font-weight:700; color:#FFFFFF;">Tọa đàm Cấp cao (Executive Panel): Khơi thông Thương vụ Chiến lược 2026–2030</div>
            <div style="font-size:14px; color:#CBD5E1; margin-top:3px;">Đối thoại trực diện cùng Lãnh đạo Quỹ đầu tư quốc tế, Tập đoàn Bất động sản &amp; Định chế Tài chính</div>
          </div>
          <div class="mono" style="font-size:11px; color:#F472B6; text-align:right;">HIGH-LEVEL PANEL</div>
        </div>

        <div class="agenda-row" style="border-left-color:#FFFFFF;">
          <div class="grotesk" style="font-size:26px; font-weight:700; color:#FFFFFF;">16:45 – 17:30</div>
          <div>
            <div style="font-size:21px; font-weight:700; color:#FFFFFF;">Lễ Ký kết Thỏa thuận Hợp tác Chiến lược (MOU) &amp; Vinh danh Thương vụ Tiêu biểu</div>
            <div style="font-size:14px; color:#CBD5E1; margin-top:3px;">Nghi thức chạm tay kích hoạt hợp tác đầu tư &amp; Tiệc trà kết nối riêng tư (Private Deal Matching)</div>
          </div>
          <div class="mono" style="font-size:11px; color:#FFFFFF; text-align:right;">MOU &amp; AWARDS</div>
        </div>
      </div>
    </div>

    <!-- Slide Footer -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-top:18px; border-top:1px solid rgba(233,213,255,0.22);">
      <span class="mono" style="font-size:10.5px; color:#94A3B8;">ORGANIZED BY VMAA · CENTRAL VIETNAM</span>
      <span class="mono" style="font-size:10.5px; color:#E9D5FF;">SLIDE 02 / 04 · MASTER DECK TEMPLATE</span>
    </div>
  </div>
</body></html>"""


slide_data_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u2}');
    background-size: cover; background-position: center;
    opacity: 0.35; filter: brightness(1.1) saturate(1.2);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background: radial-gradient(900px 600px at 78% 45%, rgba(155,77,255,0.30) 0%, rgba(36,91,255,0.20) 55%, transparent 85%);
  }}
  .shell {{
    position: absolute; inset: 52px 72px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.2em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
  .kpi-box {{
    background: rgba(11, 18, 44, 0.82);
    border: 1px solid rgba(192, 132, 252, 0.38);
    border-top: 4px solid #9B4DFF;
    border-radius: 8px;
    padding: 28px 30px;
    backdrop-filter: blur(16px);
  }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>

  <div class="shell">
    <!-- Top Slide Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:20px; border-bottom:1px solid rgba(233,213,255,0.24);">
      <div style="display:flex; align-items:center; gap:16px;">
        {SVG_VMAA_MARK}
        <div>
          <div class="grotesk" style="font-size:16px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF;">DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · REAL ESTATE — TECHNOLOGY</div>
          <div class="mono" style="font-size:10px; color:#63B4FF; margin-top:3px;">SLIDE 03 // ARCHITECTURE OF VALUE &amp; MARKET METRICS</div>
        </div>
      </div>
      <div class="mono" style="font-size:12px; color:#E9D5FF;">13.12.2026 · 13:30–17:30 · ĐÀ NẴNG</div>
    </div>

    <!-- Slide Body: 3 Pillar Columns + Luminous Data Visualization -->
    <div style="my:auto;">
      <div style="margin-bottom:32px;">
        <div class="mono" style="font-size:11px; color:#C084FC; margin-bottom:8px;">CENTRAL CONCEPT · KEYNOTE DATA SLIDE LAYOUT</div>
        <div style="font-size:46px; font-weight:800; letter-spacing:-0.02em; color:#FFFFFF;">
          KIẾN TRÚC GIÁ TRỊ: <span style="background:linear-gradient(90deg, #E9D5FF, #9B4DFF, #63B4FF); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</span>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:26px; margin-bottom:28px;">
        <div class="kpi-box" style="border-top-color:#245BFF;">
          <div class="mono" style="font-size:11px; color:#63B4FF; margin-bottom:10px;">01 // REAL ESTATE VOLUMES</div>
          <div class="grotesk" style="font-size:56px; font-weight:700; color:#FFFFFF; text-shadow:0 0 24px rgba(36,91,255,0.65);">[DRAFT KPI]</div>
          <div style="font-size:20px; font-weight:700; color:#E9D5FF; margin-top:8px;">Quỹ đất &amp; Tổ hợp Đô thị — Du lịch</div>
          <div style="font-size:14px; color:#CBD5E1; margin-top:8px; line-height:1.5;">
            Tái cấu trúc pháp lý, hợp nhất quỹ đất ven biển Đà Nẵng – Hội An – Miền Trung và chuẩn hóa tiêu chuẩn ESG quốc tế.
          </div>
        </div>

        <div class="kpi-box" style="border-top-color:#9B4DFF; background:linear-gradient(180deg, rgba(107,45,155,0.45), rgba(11,18,44,0.88));">
          <div class="mono" style="font-size:11px; color:#E9D5FF; margin-bottom:10px;">02 // TECHNOLOGY &amp; PROPTECH</div>
          <div class="grotesk" style="font-size:56px; font-weight:700; color:#FFFFFF; text-shadow:0 0 24px rgba(155,77,255,0.75);">+3.4x</div>
          <div style="font-size:20px; font-weight:700; color:#E9D5FF; margin-top:8px;">Định giá Dữ liệu &amp; Hạ tầng Số</div>
          <div style="font-size:14px; color:#CBD5E1; margin-top:8px; line-height:1.5;">
            Ứng dụng AI thẩm định giá trị tài sản, quản trị vận hành thông minh (Smart Building) và minh bạch hóa hồ sơ thương vụ M&amp;A.
          </div>
        </div>

        <div class="kpi-box" style="border-top-color:#E9D5FF;">
          <div class="mono" style="font-size:11px; color:#C084FC; margin-bottom:10px;">03 // CAPITAL CONVERGENCE</div>
          <div class="grotesk" style="font-size:56px; font-weight:700; color:#FFFFFF; text-shadow:0 0 24px rgba(233,213,255,0.65);">100%</div>
          <div style="font-size:20px; font-weight:700; color:#E9D5FF; margin-top:8px;">Hợp lực Dòng vốn Đầu tư Quốc tế</div>
          <div style="font-size:14px; color:#CBD5E1; margin-top:8px; line-height:1.5;">
            Kết nối trực tiếp các định chế tài chính Singapore, Nhật Bản, Hàn Quốc với hệ sinh thái doanh nghiệp Miền Trung.
          </div>
        </div>
      </div>

      <!-- Bottom Visual Convergence Diagram Bar -->
      <div style="background:rgba(11,18,44,0.85); border:1px solid rgba(192,132,252,0.45); border-radius:8px; padding:24px 34px; display:flex; justify-content:space-between; align-items:center;">
        <div style="display:flex; align-items:center; gap:20px;">
          <span style="padding:10px 18px; background:rgba(36,91,255,0.3); border:1px solid #63B4FF; border-radius:4px; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px;">REAL ESTATE ASSETS</span>
          <span style="font-size:24px; color:#C084FC;">+</span>
          <span style="padding:10px 18px; background:rgba(155,77,255,0.3); border:1px solid #C084FC; border-radius:4px; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px;">TECHNOLOGY INFRASTRUCTURE</span>
          <span style="font-size:24px; color:#63B4FF;">+</span>
          <span style="padding:10px 18px; background:rgba(236,72,153,0.28); border:1px solid #F472B6; border-radius:4px; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:15px;">INSTITUTIONAL CAPITAL</span>
        </div>
        <div style="display:flex; align-items:center; gap:16px;">
          <span style="font-size:24px; color:#E9D5FF;">➔</span>
          <span style="padding:12px 26px; background:linear-gradient(90deg, #6B2D9B, #9B4DFF, #245BFF); border:1.5px solid #FFFFFF; border-radius:4px; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:16px; letter-spacing:0.2em; box-shadow:0 0 28px rgba(155,77,255,0.65);">
            ARCHITECTURE OF VALUE
          </span>
        </div>
      </div>
    </div>

    <!-- Slide Footer -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-top:18px; border-top:1px solid rgba(233,213,255,0.22);">
      <span class="mono" style="font-size:10.5px; color:#94A3B8;">ORGANIZED BY VMAA · CENTRAL VIETNAM</span>
      <span class="mono" style="font-size:10.5px; color:#E9D5FF;">SLIDE 03 / 04 · MASTER DECK TEMPLATE</span>
    </div>
  </div>
</body></html>"""


slide_speaker_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px; height: 1080px; overflow: hidden;
    background: #070D20; font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF; position: relative;
  }}
  .plate {{
    position: absolute; inset: 0;
    background-image: url('{u1}');
    background-size: cover; background-position: center;
    opacity: 0.45; filter: brightness(1.1) saturate(1.2);
  }}
  .aurora {{
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background: radial-gradient(900px 600px at 72% 45%, rgba(155,77,255,0.34) 0%, rgba(36,91,255,0.22) 55%, transparent 85%);
  }}
  .shell {{
    position: absolute; inset: 52px 72px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }}
  .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.2em; text-transform: uppercase; }}
  .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
  .speaker-card {{
    background: rgba(11, 18, 44, 0.84);
    border: 1.5px solid rgba(192, 132, 252, 0.45);
    border-radius: 10px;
    padding: 32px;
    display: flex; flex-direction: column; justify-content: space-between;
    backdrop-filter: blur(16px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.55);
  }}
</style></head><body>
  <div class="plate"></div>
  <div class="aurora"></div>

  <div class="shell">
    <!-- Top Slide Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:20px; border-bottom:1px solid rgba(233,213,255,0.24);">
      <div style="display:flex; align-items:center; gap:16px;">
        {SVG_VMAA_MARK}
        <div>
          <div class="grotesk" style="font-size:16px; font-weight:700; letter-spacing:0.24em; color:#FFFFFF;">DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · REAL ESTATE — TECHNOLOGY</div>
          <div class="mono" style="font-size:10px; color:#E9D5FF; margin-top:3px;">SLIDE 04 // KEYNOTE &amp; EXECUTIVE PANELIST TEMPLATE</div>
        </div>
      </div>
      <div class="mono" style="font-size:12px; color:#E9D5FF;">13.12.2026 · 13:30–17:30 · ĐÀ NẴNG</div>
    </div>

    <div style="my:auto;">
      <div style="margin-bottom:32px;">
        <div class="mono" style="font-size:11px; color:#63B4FF; margin-bottom:8px;">SPEAKER SPOTLIGHT &amp; PANEL DISCUSSION SLIDE</div>
        <div style="font-size:46px; font-weight:800; letter-spacing:-0.02em; color:#FFFFFF;">
          DIỄN GIẢ TRỌNG TÂM &amp; <span style="color:#E9D5FF;">HỘI ĐỒNG CHUYÊN GIA</span>
        </div>
      </div>

      <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:28px;">
        <div class="speaker-card" style="border-top:5px solid #9B4DFF;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:22px;">
              <span class="mono" style="padding:6px 14px; background:rgba(155,77,255,0.32); border:1px solid #E9D5FF; border-radius:4px; font-size:10px; color:#FFFFFF;">KEYNOTE SPEAKER 01</span>
              <span class="mono" style="font-size:11px; color:#C084FC;">REAL ESTATE CAPITAL</span>
            </div>
            <div style="height:220px; border-radius:8px; background:linear-gradient(135deg, rgba(107,45,155,0.45), rgba(36,91,255,0.35)); border:1px dashed rgba(233,213,255,0.5); display:flex; align-items:center; justify-content:center; margin-bottom:24px;">
              <span class="mono" style="font-size:12px; color:#E9D5FF;">[PORTRAIT CUTOUT SLOT · 800×800 PNG]</span>
            </div>
            <div style="font-size:26px; font-weight:800; color:#FFFFFF;">[TS. NGUYỄN VĂN A]</div>
            <div style="font-size:15px; font-weight:600; color:#C084FC; margin-top:6px;">Managing Partner · [Quỹ Đầu Tư Chiến Lược]</div>
          </div>
          <div style="margin-top:22px; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2); font-size:13.5px; color:#CBD5E1;">
            Chủ đề: Cấu trúc Vốn &amp; Làn sóng M&amp;A Bất động sản Thế hệ mới tại Miền Trung
          </div>
        </div>

        <div class="speaker-card" style="border-top:5px solid #245BFF;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:22px;">
              <span class="mono" style="padding:6px 14px; background:rgba(36,91,255,0.35); border:1px solid #63B4FF; border-radius:4px; font-size:10px; color:#FFFFFF;">KEYNOTE SPEAKER 02</span>
              <span class="mono" style="font-size:11px; color:#63B4FF;">PROPTECH &amp; AI</span>
            </div>
            <div style="height:220px; border-radius:8px; background:linear-gradient(135deg, rgba(36,91,255,0.45), rgba(155,77,255,0.35)); border:1px dashed rgba(99,180,255,0.5); display:flex; align-items:center; justify-content:center; margin-bottom:24px;">
              <span class="mono" style="font-size:12px; color:#63B4FF;">[PORTRAIT CUTOUT SLOT · 800×800 PNG]</span>
            </div>
            <div style="font-size:26px; font-weight:800; color:#FFFFFF;">[BÀ LÊ HOÀNG B]</div>
            <div style="font-size:15px; font-weight:600; color:#63B4FF; margin-top:6px;">CEO &amp; Co-Founder · [Tập Đoàn Công Nghệ / PropTech]</div>
          </div>
          <div style="margin-top:22px; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2); font-size:13.5px; color:#CBD5E1;">
            Chủ đề: Định giá Tài sản bằng Dữ liệu Lớn &amp; Chuyển đổi số Chuỗi giá trị BĐS
          </div>
        </div>

        <div class="speaker-card" style="border-top:5px solid #E9D5FF;">
          <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:22px;">
              <span class="mono" style="padding:6px 14px; background:rgba(236,72,153,0.32); border:1px solid #F472B6; border-radius:4px; font-size:10px; color:#FFFFFF;">PANEL MODERATOR</span>
              <span class="mono" style="font-size:11px; color:#F472B6;">VMAA ADVISORY</span>
            </div>
            <div style="height:220px; border-radius:8px; background:linear-gradient(135deg, rgba(155,77,255,0.4), rgba(236,72,153,0.3)); border:1px dashed rgba(244,114,182,0.5); display:flex; align-items:center; justify-content:center; margin-bottom:24px;">
              <span class="mono" style="font-size:12px; color:#F5D0FE;">[PORTRAIT CUTOUT SLOT · 800×800 PNG]</span>
            </div>
            <div style="font-size:26px; font-weight:800; color:#FFFFFF;">[ÔNG TRẦN MINH C]</div>
            <div style="font-size:15px; font-weight:600; color:#F472B6; margin-top:6px;">Đại diện Ban Điều hành · VMAA Central Vietnam</div>
          </div>
          <div style="margin-top:22px; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2); font-size:13.5px; color:#CBD5E1;">
            Điều phối Phiên Tọa đàm Cấp cao: Khơi thông dòng vốn M&amp;A Miền Trung 2026
          </div>
        </div>
      </div>
    </div>

    <!-- Slide Footer -->
    <div style="display:flex; justify-content:space-between; align-items:center; padding-top:18px; border-top:1px solid rgba(233,213,255,0.22);">
      <span class="mono" style="font-size:10.5px; color:#94A3B8;">ORGANIZED BY VMAA · CENTRAL VIETNAM</span>
      <span class="mono" style="font-size:10.5px; color:#E9D5FF;">SLIDE 04 / 04 · MASTER DECK TEMPLATE</span>
    </div>
  </div>
</body></html>"""


# Save interactive Landing Page HTML in project root for web deployment
(PROJECT_DIR / "landing_page.html").write_text(landing_page_html, encoding="utf-8")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # 1. Render Social Media Pack at @2x Retina / 4K resolution
    print("Rendering Social Media Aspect Ratio Pack...")
    # 1:1 Square (2160x2160)
    page_1x1 = browser.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=2)
    page_1x1.set_content(social_1x1_html, wait_until="networkidle")
    page_1x1.wait_for_timeout(400)
    out_1x1 = SOCIAL_DIR / "SOCIAL_1x1_Square_Post_4K.png"
    page_1x1.screenshot(path=str(out_1x1))
    shutil.copy2(out_1x1, BRAIN_DIR / "SOCIAL_1x1_Square_Post_4K.png")
    page_1x1.close()

    # 4:5 Portrait Feed (2160x2700)
    page_4x5 = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
    page_4x5.set_content(social_4x5_html, wait_until="networkidle")
    page_4x5.wait_for_timeout(400)
    out_4x5 = SOCIAL_DIR / "SOCIAL_4x5_Portrait_Feed_4K.png"
    page_4x5.screenshot(path=str(out_4x5))
    shutil.copy2(out_4x5, BRAIN_DIR / "SOCIAL_4x5_Portrait_Feed_4K.png")
    page_4x5.close()

    # 9:16 Vertical Story / Reels / Standee (2160x3840)
    page_9x16 = browser.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=2)
    page_9x16.set_content(social_9x16_html, wait_until="networkidle")
    page_9x16.wait_for_timeout(400)
    out_9x16 = SOCIAL_DIR / "SOCIAL_9x16_Story_Reels_Standee_4K.png"
    page_9x16.screenshot(path=str(out_9x16))
    shutil.copy2(out_9x16, BRAIN_DIR / "SOCIAL_9x16_Story_Reels_Standee_4K.png")
    page_9x16.close()

    # 1.91:1 Event Cover / OpenGraph Link Preview (2400x1256)
    page_og = browser.new_page(viewport={"width": 1200, "height": 628}, device_scale_factor=2)
    page_og.set_content(social_og_html, wait_until="networkidle")
    page_og.wait_for_timeout(400)
    out_og = SOCIAL_DIR / "SOCIAL_191x1_Event_Cover_OG_4K.png"
    page_og.screenshot(path=str(out_og))
    shutil.copy2(out_og, BRAIN_DIR / "SOCIAL_191x1_Event_Cover_OG_4K.png")
    page_og.close()

    # 2. Render Landing Page Hero UI (3840x2160) & Slides (3840x2160)
    print("Rendering Landing Page Hero UI & 16:9 Presentation Slide Deck Suite...")
    page_16x9 = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)

    page_16x9.set_content(landing_page_html, wait_until="networkidle")
    page_16x9.wait_for_timeout(400)
    out_landing = LANDING_DIR / "LANDING_PAGE_Hero_UI_4K.png"
    page_16x9.screenshot(path=str(out_landing))
    shutil.copy2(out_landing, BRAIN_DIR / "LANDING_PAGE_Hero_UI_4K.png")

    # Slide 01 (Cover is our Hero Master Key Visual)
    hero_kv = EXPORTS_DIR / "01_VMAA_HERO_KEY_VISUAL_4K.png"
    out_slide01 = SLIDES_DIR / "SLIDE_01_Title_Cover_16x9_4K.png"
    if hero_kv.exists():
        shutil.copy2(hero_kv, out_slide01)

    # Slide 02: Agenda Timeline
    page_16x9.set_content(slide_agenda_html, wait_until="networkidle")
    page_16x9.wait_for_timeout(400)
    out_slide02 = SLIDES_DIR / "SLIDE_02_Agenda_Timeline_16x9_4K.png"
    page_16x9.screenshot(path=str(out_slide02))
    shutil.copy2(out_slide02, BRAIN_DIR / "SLIDE_02_Agenda_Timeline_16x9_4K.png")

    # Slide 03: Data & Architecture of Value
    page_16x9.set_content(slide_data_html, wait_until="networkidle")
    page_16x9.wait_for_timeout(400)
    out_slide03 = SLIDES_DIR / "SLIDE_03_Architecture_Data_16x9_4K.png"
    page_16x9.screenshot(path=str(out_slide03))
    shutil.copy2(out_slide03, BRAIN_DIR / "SLIDE_03_Architecture_Data_16x9_4K.png")

    # Slide 04: Keynote & Panelist Spotlight
    page_16x9.set_content(slide_speaker_html, wait_until="networkidle")
    page_16x9.wait_for_timeout(400)
    out_slide04 = SLIDES_DIR / "SLIDE_04_Speaker_Keynote_16x9_4K.png"
    page_16x9.screenshot(path=str(out_slide04))
    shutil.copy2(out_slide04, BRAIN_DIR / "SLIDE_04_Speaker_Keynote_16x9_4K.png")

    # 3. Render Master Multi-Ratio Overview Sheet (Social Media + Landing Page + Slide Deck)
    print("Rendering Master Social Media + Landing Page + Slide Deck Overview Sheet...")
    uri_1x1 = to_data_uri(out_1x1)
    uri_4x5 = to_data_uri(out_4x5)
    uri_9x16 = to_data_uri(out_9x16)
    uri_og = to_data_uri(out_og)
    uri_landing = to_data_uri(out_landing)
    uri_s02 = to_data_uri(out_slide02)
    uri_s03 = to_data_uri(out_slide03)
    uri_s04 = to_data_uri(out_slide04)

    overview_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: radial-gradient(circle at 50% 25%, #170F38 0%, #070D20 75%);
        font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif; color: #FFFFFF;
        padding: 34px 48px;
        display: flex; flex-direction: column; justify-content: space-between;
      }}
      .mono {{ font-family: 'JetBrains Mono', monospace; letter-spacing: 0.18em; text-transform: uppercase; }}
      .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
      .panel {{
        background: rgba(11, 18, 42, 0.84);
        border: 1px solid rgba(192, 132, 252, 0.35);
        border-radius: 10px;
        padding: 14px;
        display: flex; flex-direction: column; justify-content: space-between;
        box-shadow: 0 12px 32px rgba(0,0,0,0.55);
      }}
      .badge {{
        display: inline-block; padding: 4px 10px; border-radius: 4px;
        background: linear-gradient(90deg, #6B2D9B, #245BFF);
        border: 1px solid #E9D5FF;
        font-family: 'JetBrains Mono', monospace; font-size: 9.5px; font-weight: 700; color: #FFFFFF;
      }}
    </style></head><body>
      <!-- Header -->
      <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:14px; border-bottom:1px solid rgba(233,213,255,0.24);">
        <div style="display:flex; align-items:center; gap:14px;">
          {SVG_VMAA_MARK}
          <div>
            <div class="grotesk" style="font-size:20px; font-weight:700; letter-spacing:0.18em; color:#FFFFFF;">
              MULTI-RATIO DIGITAL, SOCIAL MEDIA, LANDING PAGE &amp; SLIDE DECK SUITE
            </div>
            <div class="mono" style="font-size:10px; color:#C084FC; margin-top:3px;">
              DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · REAL ESTATE — TECHNOLOGY · 13.12.2026 · ĐÀ NẴNG
            </div>
          </div>
        </div>
        <div class="badge" style="font-size:11px; padding:7px 14px;">ALL NATIVE 4K STANDALONE FILES EXPORTED</div>
      </div>

      <!-- Main Grid: Left = Social Ratios (9:16, 4:5, 1:1, 1.91:1) | Right = Landing Page + 16:9 Slide Deck -->
      <div style="display:grid; grid-template-columns: 1.05fr 1.25fr; gap:22px; height:890px; margin-top:14px;">

        <!-- LEFT COLUMN: SOCIAL MEDIA FORMATS -->
        <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="grotesk" style="font-size:14px; font-weight:700; letter-spacing:0.2em; color:#E9D5FF;">01 // SOCIAL MEDIA POST &amp; STORY RATIOS</span>
            <span class="mono" style="font-size:10px; color:#63B4FF;">FACEBOOK · LINKEDIN · INSTAGRAM · TIKTOK · ZALO</span>
          </div>

          <!-- Top Social Row: 9:16 Story + 4:5 Portrait + 1:1 Square -->
          <div style="display:grid; grid-template-columns: 0.82fr 1.04fr 1.14fr; gap:14px; height:510px;">
            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; white-space:nowrap;">
                <span class="badge">9:16 STORY</span>
                <span class="mono" style="font-size:8.5px; color:#C084FC;">2160×3840</span>
              </div>
              <div style="flex:1; background-image:url('{uri_9x16}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; white-space:nowrap;">
                <span class="badge">4:5 PORTRAIT</span>
                <span class="mono" style="font-size:8.5px; color:#63B4FF;">2160×2700</span>
              </div>
              <div style="flex:1; background-image:url('{uri_4x5}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; white-space:nowrap;">
                <span class="badge">1:1 SQUARE</span>
                <span class="mono" style="font-size:8.5px; color:#E9D5FF;">2160×2160</span>
              </div>
              <div style="flex:1; background-image:url('{uri_1x1}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
            </div>
          </div>

          <!-- Bottom Social Row: 1.91:1 Event Cover & OpenGraph Link Preview -->
          <div class="panel" style="flex:1;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="badge">1.91:1 FACEBOOK / LINKEDIN EVENT COVER &amp; OPENGRAPH LINK PREVIEW</span>
              <span class="mono" style="font-size:9.5px; color:#E9D5FF;">2400×1256 (1200×628 @2x)</span>
            </div>
            <div style="flex:1; background-image:url('{uri_og}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px;"></div>
          </div>
        </div>

        <!-- RIGHT COLUMN: LANDING PAGE HERO UI + 16:9 PRESENTATION SLIDE DECK -->
        <div style="display:flex; flex-direction:column; gap:16px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="grotesk" style="font-size:14px; font-weight:700; letter-spacing:0.2em; color:#E9D5FF;">02 // LANDING PAGE HERO UI &amp; 16:9 SLIDE DECK TEMPLATES</span>
            <span class="mono" style="font-size:10px; color:#C084FC;">WEB PORTAL + POWERPOINT / KEYNOTE 16:9</span>
          </div>

          <!-- Landing Page Hero Mockup -->
          <div class="panel" style="height:560px; border-color:#9B4DFF;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <span class="badge" style="background:linear-gradient(90deg, #9B4DFF, #245BFF);">16:9 LANDING PAGE ABOVE-THE-FOLD HERO UI (WITH LIVE HTML/CSS)</span>
              <span class="mono" style="font-size:9.5px; color:#63B4FF;">3840×2160 + landing_page.html</span>
            </div>
            <div style="flex:1; background-color:#070D20; background-image:url('{uri_landing}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:6px; border:1px solid rgba(233,213,255,0.3);"></div>
          </div>

          <!-- 3 Presentation Slide Templates (16:9) -->
          <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:14px; flex:1;">
            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="badge">SLIDE 02 · AGENDA</span>
                <span class="mono" style="font-size:8.5px; color:#C084FC;">16:9 4K</span>
              </div>
              <div style="flex:1; background-color:#070D20; background-image:url('{uri_s02}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:4px; border:1px solid rgba(233,213,255,0.25);"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="badge">SLIDE 03 · M&amp;A DATA</span>
                <span class="mono" style="font-size:8.5px; color:#63B4FF;">16:9 4K</span>
              </div>
              <div style="flex:1; background-color:#070D20; background-image:url('{uri_s03}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:4px; border:1px solid rgba(233,213,255,0.25);"></div>
            </div>

            <div class="panel">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="badge">SLIDE 04 · SPEAKERS</span>
                <span class="mono" style="font-size:8.5px; color:#E9D5FF;">16:9 4K</span>
              </div>
              <div style="flex:1; background-color:#070D20; background-image:url('{uri_s04}'); background-size:contain; background-repeat:no-repeat; background-position:center; border-radius:4px; border:1px solid rgba(233,213,255,0.25);"></div>
            </div>
          </div>
        </div>

      </div>
    </body></html>"""

    page_16x9.set_content(overview_html, wait_until="networkidle")
    page_16x9.wait_for_timeout(400)
    out_overview = EXPORTS_DIR / "10_VMAA_Social_Landing_Slide_Ratio_Suite.png"
    page_16x9.screenshot(path=str(out_overview))
    shutil.copy2(out_overview, BRAIN_DIR / "10_VMAA_Social_Landing_Slide_Ratio_Suite.png")

    page_16x9.close()
    browser.close()
    print("ALL SOCIAL MEDIA, LANDING PAGE, AND SLIDE DECK ASPECT RATIOS EXPORTED SUCCESSFULLY!")
