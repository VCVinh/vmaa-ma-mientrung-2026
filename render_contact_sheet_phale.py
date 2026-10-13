import base64
import shutil
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")
EXPORTS_DIR = ROOT / "exports" / "v2_production"

def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"

u_land = to_data_uri(EXPORTS_DIR / "KV_v2_Landscape_1920x1080_VI.png")
u_stage = to_data_uri(EXPORTS_DIR / "stage_venue" / "KV_v2_Curved_Stage_32x9_VI.png")
u_square = to_data_uri(EXPORTS_DIR / "portrait_social" / "KV_v2_Square_1080x1080_PhaLe.png")
u_portrait = to_data_uri(EXPORTS_DIR / "portrait_social" / "KV_v2_Portrait_1080x1350_PhaLe.png")
u_story = to_data_uri(EXPORTS_DIR / "portrait_social" / "KV_v2_Story_1080x1920_PhaLe.png")
u_guest = to_data_uri(EXPORTS_DIR / "guests_motion" / "GUEST_01_Portrait_1080x1350.png")
u_post01 = to_data_uri(EXPORTS_DIR / "social_media" / "POST_01_1080x1350.png")
u_wordmark = to_data_uri(ROOT / "assets" / "vmaa_wordmark_white_transparent.png")

html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 3840px; height: 2160px;
    background: #040714;
    display: flex; flex-direction: column; justify-content: space-between;
    padding: 60px 80px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #FFFFFF;
    position: relative; overflow: hidden;
  }}
  .header-bar {{
    display: flex; justify-content: space-between; align-items: flex-end;
    padding-bottom: 24px; border-bottom: 2px solid rgba(155,77,255,0.4);
  }}
  .header-title {{
    font-size: 38px; font-weight: 800; letter-spacing: -0.01em; color: #FFFFFF;
  }}
  .header-meta {{
    font-family: 'Space Grotesk', monospace; font-size: 16px; font-weight: 600;
    color: #93C5FF; letter-spacing: 0.16em; text-transform: uppercase;
  }}
  .grid-showcase {{
    display: grid;
    grid-template-columns: 1.8fr 1.2fr 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    gap: 32px;
    height: 1720px;
    margin-top: 28px; margin-bottom: 28px;
  }}
  .show-card {{
    background: rgba(10,22,48,0.7);
    border: 1px solid rgba(233,213,255,0.25);
    border-radius: 12px; overflow: hidden;
    display: flex; flex-direction: column;
  }}
  .card-label {{
    padding: 14px 20px; background: rgba(7,13,32,0.92);
    border-bottom: 1px solid rgba(233,213,255,0.18);
    font-family: 'Space Grotesk', sans-serif; font-size: 14px; font-weight: 700;
    color: #63B4FF; letter-spacing: 0.14em; text-transform: uppercase;
    display: flex; justify-content: space-between;
  }}
  .card-label span:last-child {{
    color: #FDE047; font-weight: 600;
  }}
  .card-preview {{
    position: relative; flex: 1; overflow: hidden;
    background-size: contain; background-repeat: no-repeat; background-position: center;
    background-color: #050918;
  }}
  .footer-swatches {{
    display: flex; justify-content: space-between; align-items: center;
    padding-top: 20px; border-top: 1px solid rgba(233,213,255,0.22);
  }}
  .swatch-group {{ display: flex; gap: 24px; align-items: center; }}
  .swatch {{
    display: flex; align-items: center; gap: 10px;
    font-family: 'Space Grotesk', monospace; font-size: 14px; color: rgba(233,213,255,0.85);
  }}
  .swatch-dot {{
    width: 20px; height: 20px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.3);
  }}
</style></head><body>
  <div class="header-bar">
    <div>
      <div style="font-family:'Space Grotesk',monospace; font-size:15px; font-weight:700; color:#C084FC; letter-spacing:0.2em; text-transform:uppercase; margin-bottom:6px;">
        VMAA CENTRAL VIETNAM // MASTER UNIFIED PHA LE VISUAL SUITE 4K
      </div>
      <div class="header-title">DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 · HỆ THỐNG ẤN PHẨM KHÔNG SỤT LÚN BỐ CỤC</div>
    </div>
    <div style="text-align:right;">
      <img src="{u_wordmark}" alt="VMAA" style="height:36px; width:auto; margin-bottom:6px;"/>
      <div class="header-meta">13.12.2026 · ĐÀ NẴNG, VIỆT NAM · ARCHITECTURE OF VALUE</div>
    </div>
  </div>

  <div class="grid-showcase">
    <!-- 1. Hero Landscape 16:9 -->
    <div class="show-card" style="grid-column: 1 / 2; grid-row: 1 / 2;">
      <div class="card-label">
        <span>01. HERO KEY VISUAL MASTER (16:9 4K UHD)</span>
        <span>CLEAN PHA LE PRISM</span>
      </div>
      <div class="card-preview" style="background-image:url('{u_land}');"></div>
    </div>

    <!-- 2. 32:9 Curved LED Stage -->
    <div class="show-card" style="grid-column: 2 / 5; grid-row: 1 / 2;">
      <div class="card-label">
        <span>02. 32:9 CURVED LED STAGE WALL (3840×1080)</span>
        <span>KEYNOTE STAGE PANORAMA</span>
      </div>
      <div class="card-preview" style="background-image:url('{u_stage}');"></div>
    </div>

    <!-- 3. Portrait Feed 4:5 -->
    <div class="show-card" style="grid-column: 1 / 2; grid-row: 2 / 3;">
      <div class="card-label">
        <span>03. PORTRAIT FEED 4:5 (2160×2700)</span>
        <span>GOLD STANDARD MASTER</span>
      </div>
      <div class="card-preview" style="background-image:url('{u_portrait}');"></div>
    </div>

    <!-- 4. Square 1:1 -->
    <div class="show-card" style="grid-column: 2 / 3; grid-row: 2 / 3;">
      <div class="card-label">
        <span>04. SQUARE 1:1 (2160×2160)</span>
        <span>BENCHMARK PHA LE</span>
      </div>
      <div class="card-preview" style="background-image:url('{u_square}');"></div>
    </div>

    <!-- 5. Story 9:16 -->
    <div class="show-card" style="grid-column: 3 / 4; grid-row: 2 / 3;">
      <div class="card-label">
        <span>05. STORY 9:16 (2160×3840)</span>
        <span>TALL ASCENDING PIPES</span>
      </div>
      <div class="card-preview" style="background-image:url('{u_story}');"></div>
    </div>

    <!-- 6. Guest Spotlight & Social Post -->
    <div class="show-card" style="grid-column: 4 / 5; grid-row: 2 / 3;">
      <div class="card-label">
        <span>06. VIP SPEAKER (4:5 FEED)</span>
        <span>CRYSTAL PLINTH</span>
      </div>
      <div class="card-preview" style="background-image:url('{u_guest}');"></div>
    </div>
  </div>

  <div class="footer-swatches">
    <div class="swatch-group">
      <div class="swatch"><div class="swatch-dot" style="background:#070D20;"></div><span>Obsidian #070D20</span></div>
      <div class="swatch"><div class="swatch-dot" style="background:#6B2D9B;"></div><span>Amethyst #6B2D9B</span></div>
      <div class="swatch"><div class="swatch-dot" style="background:#9B4DFF;"></div><span>Violet #9B4DFF</span></div>
      <div class="swatch"><div class="swatch-dot" style="background:#245BFF;"></div><span>Cobalt #245BFF</span></div>
      <div class="swatch"><div class="swatch-dot" style="background:#63B4FF;"></div><span>Ice Cyan #63B4FF</span></div>
      <div class="swatch"><div class="swatch-dot" style="background:#F59E0B;"></div><span>Gold Accent #F59E0B</span></div>
    </div>
    <div style="font-family:'Space Grotesk',monospace; font-size:14px; color:#A5B4FC;">
      PRODUCED WITH UNIFIED PHA LE ARCHITECTURAL DESIGN SYSTEM · 100% CLEAN RETINA @2X
    </div>
  </div>
</body></html>
"""

cs_html_path = EXPORTS_DIR / "VMAA_2026_Production_Contact_Sheet_4K.html"
cs_png_path = EXPORTS_DIR / "VMAA_2026_Production_Contact_Sheet_4K.png"
cs_html_path.write_text(html, encoding="utf-8")

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--force-color-profile=srgb"])
        page = await browser.new_page(viewport={"width": 3840, "height": 2160}, device_scale_factor=1)
        await page.goto(cs_html_path.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(500)
        await page.screenshot(path=str(cs_png_path))
        await page.close()
        await browser.close()
        shutil.copy2(cs_png_path, BRAIN_DIR / cs_png_path.name)
        print("Rendered VMAA_2026_Production_Contact_Sheet_4K.png successfully!")

if __name__ == "__main__":
    asyncio.run(render())
