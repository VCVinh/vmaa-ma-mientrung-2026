import asyncio
from pathlib import Path
from playwright.async_api import async_playwright
import shutil

ROOT = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")
EXPORTS_DIR = ROOT / "exports" / "v2_production"

async def render():
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--force-color-profile=srgb"])
        
        # 1. Landscape VI (3840x2160 UHD @2x)
        html_land = EXPORTS_DIR / "KV_v2_Landscape_1920x1080_VI.html"
        png_land = EXPORTS_DIR / "KV_v2_Landscape_1920x1080_VI.png"
        page = await browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        await page.goto(html_land.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(400)
        await page.screenshot(path=str(png_land))
        await page.close()
        shutil.copy(png_land, BRAIN_DIR / png_land.name)
        print("Rendered Landscape VI 4K!")

        # 2. Landscape EN (3840x2160 UHD @2x)
        html_land_en = EXPORTS_DIR / "KV_v2_Landscape_1920x1080_EN.html"
        png_land_en = EXPORTS_DIR / "KV_v2_Landscape_1920x1080_EN.png"
        page = await browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        await page.goto(html_land_en.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(400)
        await page.screenshot(path=str(png_land_en))
        await page.close()
        shutil.copy(png_land_en, BRAIN_DIR / png_land_en.name)
        print("Rendered Landscape EN 4K!")

        # 3. Stage VI (3840x1080 32:9 @1x or @2x)
        html_stage = EXPORTS_DIR / "stage_venue" / "KV_v2_Curved_Stage_32x9_VI.html"
        png_stage = EXPORTS_DIR / "stage_venue" / "KV_v2_Curved_Stage_32x9_VI.png"
        page = await browser.new_page(viewport={"width": 3840, "height": 1080}, device_scale_factor=1)
        await page.goto(html_stage.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(400)
        await page.screenshot(path=str(png_stage))
        await page.close()
        shutil.copy(png_stage, BRAIN_DIR / png_stage.name)
        print("Rendered Stage VI 32:9!")

        # 4. Stage EN (3840x1080 32:9)
        html_stage_en = EXPORTS_DIR / "stage_venue" / "KV_v2_Curved_Stage_32x9_EN.html"
        png_stage_en = EXPORTS_DIR / "stage_venue" / "KV_v2_Curved_Stage_32x9_EN.png"
        page = await browser.new_page(viewport={"width": 3840, "height": 1080}, device_scale_factor=1)
        await page.goto(html_stage_en.as_uri(), wait_until="networkidle")
        await page.wait_for_timeout(400)
        await page.screenshot(path=str(png_stage_en))
        await page.close()
        shutil.copy(png_stage_en, BRAIN_DIR / png_stage_en.name)
        print("Rendered Stage EN 32:9!")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(render())
