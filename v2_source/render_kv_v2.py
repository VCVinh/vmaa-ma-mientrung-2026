"""Render KV_Hero_Motion_v2.html -> stills (clean + slot guides) and 1080p30 motion video.
Usage: python render_kv_v2.py [still|video|all]
"""
import sys, subprocess, pathlib, asyncio
from playwright.async_api import async_playwright
ROOT = pathlib.Path(__file__).parent; SRC = (ROOT/"exports/KV_Hero_Motion_v2.html").as_uri()
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT/"exports"/"kv_v2"; OUT.mkdir(parents=True, exist_ok=True)
FPS, DUR = 30, 10

async def main(mode):
    async with async_playwright() as p:
        b = await p.chromium.launch(args=["--force-color-profile=srgb"])
        if mode in ("still", "all"):
            for name, qs in (("KV_v2_Master_4K.png", "?hold=1"), ("KV_v2_LogoSlot_Guides_4K.png", "?hold=1&guides=1")):
                pg = await b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
                await pg.goto(SRC + qs); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(600)
                await pg.screenshot(path=str(OUT/name)); await pg.close()
        if mode in ("video", "all"):
            fr = OUT/"frames"; fr.mkdir(exist_ok=True)
            pg = await b.new_page(viewport={"width": 1920, "height": 1080})
            await pg.goto(SRC + "?t=0"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(600)
            for i in range(FPS*DUR + 1):
                await pg.evaluate(f"__seek({i/FPS})"); await pg.screenshot(path=str(fr/f"f{i:04d}.jpg"), type="jpeg", quality=95)
            subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",str(fr/"f%04d.jpg"),"-c:v","libx264","-preset","slow","-crf","14","-pix_fmt","yuv420p","-movflags","+faststart",str(OUT/"VMAA_KV_v2_Motion_1080p30.mp4")], check=True)
        await b.close()
asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "all"))
