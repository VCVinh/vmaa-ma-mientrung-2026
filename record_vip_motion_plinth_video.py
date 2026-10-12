import os
import sys
import time
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

PROJECT_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")
VIDEO_EXPORT_DIR = PROJECT_DIR / "exports" / "videos"
VIDEO_EXPORT_DIR.mkdir(parents=True, exist_ok=True)

# Path to the landing page
LANDING_PAGE_PATH = PROJECT_DIR / "landing_page.html"
LANDING_PAGE_URI = LANDING_PAGE_PATH.as_uri()

print("Launching Playwright to capture Landing Page UI and record Motion Graphic Plinth...")

with sync_playwright() as p:
    # 1. Capture High-Resolution Landing Page Screenshots
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    
    page.goto(LANDING_PAGE_URI)
    page.wait_for_timeout(2500) # Wait for fonts & WebGL initialization
    
    # Snapshot Hero Slide
    hero_snap = PROJECT_DIR / "exports" / "LANDING_PAGE_Slide0_Hero.png"
    page.screenshot(path=str(hero_snap))
    shutil.copy(hero_snap, BRAIN_DIR / "LANDING_PAGE_Slide0_Hero.png")
    print("Captured LANDING_PAGE_Slide0_Hero.png")
    
    # Go to Slide 2 (Speaker & Motion Plinth)
    page.evaluate("goToSlide(2)")
    page.wait_for_timeout(1500)
    plinth_snap = PROJECT_DIR / "exports" / "LANDING_PAGE_Slide2_MotionPlinth.png"
    page.screenshot(path=str(plinth_snap))
    shutil.copy(plinth_snap, BRAIN_DIR / "LANDING_PAGE_Slide2_MotionPlinth.png")
    print("Captured LANDING_PAGE_Slide2_MotionPlinth.png")
    
    browser.close()

    # 2. Record 6-Second Silky-Smooth 60fps Motion Video of the VIP Plinth
    print("Recording video of the Motion Graphic Plinth...")
    record_dir = PROJECT_DIR / "exports" / "raw_recordings"
    record_dir.mkdir(parents=True, exist_ok=True)
    
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(
        record_video_dir=str(record_dir),
        record_video_size={"width": 1920, "height": 1080},
        viewport={"width": 1920, "height": 1080}
    )
    
    rec_page = context.new_page()
    rec_page.goto(LANDING_PAGE_URI)
    rec_page.wait_for_timeout(1000)
    
    # Jump directly to Motion Plinth Slide
    rec_page.evaluate("goToSlide(2)")
    
    # Let it record the caustic light sweeps, rotating avatar ring, and neon pulse for 6 seconds
    rec_page.wait_for_timeout(6000)
    
    # Close context to flush video to disk
    context.close()
    browser.close()

    # Find the generated video file in record_dir
    video_files = list(record_dir.glob("*.webm"))
    if video_files:
        latest_video = max(video_files, key=lambda f: f.stat().st_mtime)
        dest_video = VIDEO_EXPORT_DIR / "VMAA_VIP_Invitation_Motion_Plinth.webm"
        shutil.copy(latest_video, dest_video)
        shutil.copy(dest_video, BRAIN_DIR / "VMAA_VIP_Invitation_Motion_Plinth.webm")
        print(f"Successfully recorded and exported: {dest_video} ({dest_video.stat().st_size} bytes)")
    else:
        print("Warning: No video file found in record_dir")

print("Motion Plinth capture and video generation complete!")
