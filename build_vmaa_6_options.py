import os
import sys
import json
import math
import wave
import struct
import shutil
import base64
import subprocess
from pathlib import Path

import cv2
import numpy as np
import imageio_ffmpeg
from playwright.sync_api import sync_playwright

BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")
PROJECT_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
PLATES_DIR = PROJECT_DIR / "assets" / "plates"
EXPORTS_DIR = PROJECT_DIR / "exports"
VIDEOS_DIR = PROJECT_DIR / "videos"

for d in [PLATES_DIR, EXPORTS_DIR, VIDEOS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------------------
# 1. COPY & SYNTHESIZE HIGH-LUMINOSITY PURPLE × ELECTRIC COBALT 3D PLATES
# -------------------------------------------------------------------------
src_p1 = BRAIN_DIR / "vmaa_hero_purple_cobalt_convergence_1791775110348.jpg"
src_p2 = BRAIN_DIR / "vmaa_purple_fluted_caustic_prism_1791775124922.jpg"
src_p3 = BRAIN_DIR / "vmaa_purple_ascending_cantilevers_1791775137159.jpg"

src_contours = PLATES_DIR / "opt03_contours.jpg"
src_iso = PLATES_DIR / "opt05_isometric.jpg"
src_aud = PLATES_DIR / "gitex_auditorium.jpg"


def enhance_luminosity_and_bloom(img_bgr: np.ndarray, boost: float = 1.18, bloom_strength: float = 0.32) -> np.ndarray:
    """Applies HDR specular bloom and contrast lift so dark areas feel internally lit and radiant."""
    f = img_bgr.astype(np.float32) / 255.0
    # Lift midtones and highlights while keeping deep obsidian shadows (#070D20)
    lifted = np.power(np.clip(f, 0.0, 1.0), 0.88) * boost
    # Extract bright highlights for soft volumetric bloom
    lum = 0.114 * f[:, :, 0] + 0.587 * f[:, :, 1] + 0.299 * f[:, :, 2]
    mask = np.clip((lum - 0.35) / 0.65, 0.0, 1.0)[:, :, None]
    bright = f * mask
    bloom1 = cv2.GaussianBlur(bright, (0, 0), sigmaX=28, sigmaY=28)
    bloom2 = cv2.GaussianBlur(bright, (0, 0), sigmaX=75, sigmaY=75)
    out = lifted + bloom_strength * (0.6 * bloom1 + 0.8 * bloom2)
    return np.clip(out * 255.0, 0, 255).astype(np.uint8)


def apply_purple_cobalt_aurora_shader(
    img_bgr: np.ndarray,
    mode: str = "ultraviolet_contours"
) -> np.ndarray:
    """
    Transforms an abstract 3D cobalt plate into a radiant, multi-tonal Purple (#6B2D9B -> #9B4DFF)
    + Electric Cobalt (#245BFF) + Soft Lavender (#E9D5FF) + Magenta/Cyan ('loan loan') master plate.
    """
    H, W = img_bgr.shape[:2]
    f = img_bgr.astype(np.float32) / 255.0
    # Compute luminance & edge energy
    lum = 0.114 * f[:, :, 0] + 0.587 * f[:, :, 1] + 0.299 * f[:, :, 2]
    lum_lift = np.power(np.clip(lum, 0.0, 1.0), 0.72)

    y_grid, x_grid = np.meshgrid(
        np.linspace(0, 1, H, dtype=np.float32),
        np.linspace(0, 1, W, dtype=np.float32),
        indexing="ij"
    )

    # Create smooth 'loan loan' iridescent aurora waves across the 3D geometry
    wave1 = 0.5 + 0.5 * np.sin(5.2 * x_grid - 3.4 * y_grid + 0.7)
    wave2 = 0.5 + 0.5 * np.cos(3.8 * x_grid + 4.6 * y_grid - 1.1)

    # Colors in BGR float32 [0..1]
    obsidian = np.array([0x20 / 255.0, 0x0D / 255.0, 0x07 / 255.0], dtype=np.float32)      # #070D20
    royal_purple = np.array([0x9B / 255.0, 0x2D / 255.0, 0x6B / 255.0], dtype=np.float32)  # #6B2D9B
    elec_violet = np.array([0xFF / 255.0, 0x4D / 255.0, 0x9B / 255.0], dtype=np.float32)   # #9B4DFF
    elec_cobalt = np.array([0xFF / 255.0, 0x5B / 255.0, 0x24 / 255.0], dtype=np.float32)   # #245BFF
    ice_cyan = np.array([0xFF / 255.0, 0xE5 / 255.0, 0x40 / 255.0], dtype=np.float32)      # #40E5FF
    lavender = np.array([0xFF / 255.0, 0xD8 / 255.0, 0xF5 / 255.0], dtype=np.float32)      # #F5D8FF
    magenta_edge = np.array([0xB8 / 255.0, 0x38 / 255.0, 0xEC / 255.0], dtype=np.float32)  # #EC38B8

    if mode == "ultraviolet_contours":
        mid_tone = wave1[:, :, None] * elec_violet + (1.0 - wave1[:, :, None]) * elec_cobalt
        high_tone = wave2[:, :, None] * lavender + (1.0 - wave2[:, :, None]) * ice_cyan
    elif mode == "imperial_isometric":
        mid_tone = wave1[:, :, None] * royal_purple + (1.0 - wave1[:, :, None]) * elec_violet
        high_tone = wave2[:, :, None] * magenta_edge + (1.0 - wave2[:, :, None]) * lavender
    else:
        mid_tone = 0.6 * elec_violet + 0.4 * elec_cobalt
        high_tone = lavender

    # Map luminance through multi-tonal layers: obsidian -> royal purple -> electric violet/cobalt -> lavender/white
    t1 = np.clip(lum_lift * 1.6, 0.0, 1.0)[:, :, None]
    t2 = np.clip((lum_lift - 0.28) * 1.85, 0.0, 1.0)[:, :, None]
    t3 = np.clip((lum_lift - 0.62) * 2.6, 0.0, 1.0)[:, :, None]

    graded = (1.0 - t1) * obsidian + t1 * royal_purple
    graded = (1.0 - t2) * graded + t2 * mid_tone
    graded = (1.0 - t3) * graded + t3 * high_tone

    # Add volumetric diagonal light beam ('loan loan' aurora glow) on the right side
    beam_dist = np.abs((x_grid - 0.68) * 0.82 + (y_grid - 0.48) * 0.58)
    beam = np.exp(-(beam_dist ** 2) / (2 * (0.18 ** 2)))[:, :, None]
    spot = np.exp(-(((x_grid - 0.72) ** 2 + (y_grid - 0.42) ** 2) / (2 * (0.22 ** 2))))[:, :, None]

    graded += 0.38 * beam * elec_violet + 0.30 * spot * lavender

    # Specular bloom pass
    bright = np.clip(graded - 0.45, 0.0, 1.0)
    bloom = cv2.GaussianBlur(bright, (0, 0), sigmaX=42, sigmaY=42)
    final = np.clip((graded + 0.65 * bloom) * 255.0, 0, 255).astype(np.uint8)
    return final


# Build & save the 6 High-Luminosity Purple-Cobalt 3D Plates
p1_path = PLATES_DIR / "purple_opt01_hero_convergence.jpg"
p2_path = PLATES_DIR / "purple_opt02_fluted_caustics.jpg"
p3_path = PLATES_DIR / "purple_opt03_ascending_cantilevers.jpg"
p4_path = PLATES_DIR / "purple_opt04_ultraviolet_contours.jpg"
p5_path = PLATES_DIR / "purple_opt05_imperial_isometric.jpg"
p6_path = PLATES_DIR / "purple_opt06_highkey_aurora_stage.jpg"
p_aud_path = PLATES_DIR / "purple_gitex_auditorium.jpg"

img1_raw = cv2.imread(str(src_p1))
img2_raw = cv2.imread(str(src_p2))
img3_raw = cv2.imread(str(src_p3))
img_contours_raw = cv2.imread(str(src_contours))
img_iso_raw = cv2.imread(str(src_iso))
img_aud_raw = cv2.imread(str(src_aud))

h1 = cv2.resize(img1_raw, (1920, 1080))
h2 = cv2.resize(img2_raw, (1920, 1080))
h3 = cv2.resize(img3_raw, (1920, 1080))
h_contours = cv2.resize(img_contours_raw, (1920, 1080))
h_iso = cv2.resize(img_iso_raw, (1920, 1080))

cv2.imwrite(str(p1_path), enhance_luminosity_and_bloom(h1, boost=1.22, bloom_strength=0.42), [cv2.IMWRITE_JPEG_QUALITY, 96])
cv2.imwrite(str(p2_path), enhance_luminosity_and_bloom(h2, boost=1.20, bloom_strength=0.38), [cv2.IMWRITE_JPEG_QUALITY, 96])
cv2.imwrite(str(p3_path), enhance_luminosity_and_bloom(h3, boost=1.22, bloom_strength=0.42), [cv2.IMWRITE_JPEG_QUALITY, 96])

# Tone 04: Ultraviolet × Ice-Cyan Coastal Meridian Contours fused with 3D Ascending Crystal Light Beams
c4_shaded = apply_purple_cobalt_aurora_shader(h_contours, mode="ultraviolet_contours")
c4_screen = 255 - ((255 - c4_shaded.astype(np.uint16)) * (255 - (h3 * 0.72).astype(np.uint16)) // 255)
cv2.imwrite(str(p4_path), enhance_luminosity_and_bloom(c4_screen.astype(np.uint8), boost=1.18, bloom_strength=0.36), [cv2.IMWRITE_JPEG_QUALITY, 96])

# Tone 05: Imperial Purple × Magenta-Lavender Isometric Crystal Matrix fused with 3D Caustic Prisms
c5_shaded = apply_purple_cobalt_aurora_shader(h_iso, mode="imperial_isometric")
c5_screen = 255 - ((255 - c5_shaded.astype(np.uint16)) * (255 - (h2 * 0.68).astype(np.uint16)) // 255)
cv2.imwrite(str(p5_path), enhance_luminosity_and_bloom(c5_screen.astype(np.uint8), boost=1.18, bloom_strength=0.36), [cv2.IMWRITE_JPEG_QUALITY, 96])

# Tone 06: High-Key Singapore Stage Aurora (Blend of Hero Convergence + Fluted Caustics with intense Lavender-Cobalt Aurora)
highkey_blend = cv2.addWeighted(h1, 0.58, h2, 0.52, 14)
cv2.imwrite(str(p6_path), enhance_luminosity_and_bloom(highkey_blend, boost=1.24, bloom_strength=0.44), [cv2.IMWRITE_JPEG_QUALITY, 96])

# Auditorium with Purple-Cobalt ambient stage wash
aud_purple = apply_purple_cobalt_aurora_shader(img_aud_raw, mode="ultraviolet_contours")
aud_blend = cv2.addWeighted(img_aud_raw, 0.55, aud_purple, 0.45, 0)
cv2.imwrite(str(p_aud_path), aud_blend, [cv2.IMWRITE_JPEG_QUALITY, 95])


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


u1 = to_data_uri(p1_path)
u2 = to_data_uri(p2_path)
u3 = to_data_uri(p3_path)
u4 = to_data_uri(p4_path)
u5 = to_data_uri(p5_path)
u6 = to_data_uri(p6_path)
u_aud = to_data_uri(p_aud_path)

u_logo_full = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")
u_logo_wordmark = to_data_uri(PROJECT_DIR / "assets" / "vmaa_wordmark_white_transparent.png")

# -------------------------------------------------------------------------
# 2. SHARED FONTS, OFFICIAL VMAA LOGO & HIGH-IMPACT 'LOAN LOAN' PURPLE-COBALT CSS
# -------------------------------------------------------------------------
FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Chakra+Petch:wght@600;700&family=JetBrains+Mono:wght@500;600;700&family=Outfit:wght@200;300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@600;700;800&family=Space+Grotesk:wght@500;600;700&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet">
"""

SVG_VMAA_MARK = f"""
<div style="padding:7px 16px; background:rgba(12, 18, 46, 0.78); border:1.5px solid rgba(233, 213, 255, 0.48); border-radius:6px; box-shadow:0 0 26px rgba(155, 77, 255, 0.42), inset 0 1px 1px rgba(255,255,255,0.35); display:inline-flex; align-items:center; backdrop-filter:blur(12px);">
  <img src="{u_logo_full}" style="height:44px; width:auto; display:block; filter:drop-shadow(0 0 10px rgba(155,77,255,0.75));" alt="Official VMAA Logo" />
</div>
"""

SVG_ARROW_SW = """
<svg width="36" height="36" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M29 7L7 29M7 29H24M7 29V12" stroke="#E9D5FF" stroke-width="2.8" stroke-linecap="square"/>
</svg>
"""

SVG_ARROW_NE = """
<svg width="20" height="20" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M5 17L17 5M17 5H7M17 5V15" stroke="#FFFFFF" stroke-width="2.4" stroke-linecap="square"/>
</svg>
"""

COMMON_STYLE = """
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px; height: 1080px; overflow: hidden;
    background: #070D20;
    font-family: 'Plus Jakarta Sans', 'Outfit', sans-serif;
    color: #FFFFFF;
    position: relative;
  }
  .plate {
    position: absolute; inset: 0;
    background-size: cover; background-position: center;
    filter: brightness(1.08) contrast(1.08) saturate(1.16);
  }
  /* Pure Additive 'Loan Loan' Iridescent Purple-Cobalt-Lavender Light Diffusion (Never Darkens!) */
  .aurora-wash {
    position: absolute; inset: 0; pointer-events: none;
    mix-blend-mode: screen;
    background:
      radial-gradient(960px 700px at 72% 46%, rgba(155, 77, 255, 0.32) 0%, rgba(36, 91, 255, 0.20) 48%, transparent 80%),
      radial-gradient(680px 520px at 28% 46%, rgba(107, 45, 155, 0.28) 0%, rgba(36, 91, 255, 0.14) 55%, transparent 85%),
      radial-gradient(640px 420px at 64% 22%, rgba(233, 213, 255, 0.22) 0%, transparent 72%);
  }
  /* Focused left-side contrast gradient for razor-sharp typography while leaving 50%-100% 3D hero structure 100% radiant */
  .left-readability-gradient {
    position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(90deg,
      rgba(7, 11, 28, 0.80) 0%,
      rgba(12, 16, 42, 0.52) 32%,
      rgba(18, 14, 48, 0.14) 48%,
      rgba(0, 0, 0, 0.0) 62%
    );
  }
  .shell {
    position: absolute; inset: 54px 74px;
    display: flex; flex-direction: column; justify-content: space-between;
    z-index: 10;
  }
  .mono {
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.22em; text-transform: uppercase;
  }
  .grotesk {
    font-family: 'Space Grotesk', sans-serif;
  }
  .script-vn {
    font-family: 'Caveat', cursive;
    font-weight: 700;
    color: #E9D5FF;
    white-space: nowrap;
    text-shadow: 0 0 24px rgba(155, 77, 255, 0.95), 0 0 48px rgba(36, 91, 255, 0.85);
  }
  /* VIP Luminous Hero Title Effect */
  .hero-title-glow {
    color: #FFFFFF;
    text-shadow:
      0 0 28px rgba(155, 77, 255, 0.65),
      0 0 64px rgba(36, 91, 255, 0.55),
      0 4px 20px rgba(0, 0, 0, 0.75);
  }
  .year-outline-glow {
    color: transparent;
    -webkit-text-stroke: 2.2px #E9D5FF;
    filter: drop-shadow(0 0 18px rgba(155, 77, 255, 0.85)) drop-shadow(0 0 36px rgba(36, 91, 255, 0.65));
  }
  .sector-pill {
    display: inline-flex; align-items: center; gap: 22px;
    padding: 15px 34px;
    background: linear-gradient(90deg, #6B2D9B 0%, #9B4DFF 42%, #245BFF 100%);
    border: 1.5px solid #E9D5FF;
    border-left: 5px solid #FFFFFF;
    border-radius: 4px;
    box-shadow:
      0 0 38px rgba(155, 77, 255, 0.65),
      0 12px 32px rgba(36, 91, 255, 0.45),
      inset 0 1px 1px rgba(255, 255, 255, 0.6);
  }
  .swatch-pill {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 6px 14px; border-radius: 999px;
    background: rgba(10, 18, 42, 0.72);
    border: 1px solid rgba(233, 213, 255, 0.35);
    backdrop-filter: blur(12px);
  }
  .swatch-dot {
    width: 11px; height: 11px; border-radius: 50%;
    box-shadow: 0 0 10px currentColor;
  }
"""


def build_top_header(tone_badge: str) -> str:
    return f"""
    <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:22px; border-bottom:1px solid rgba(233, 213, 255, 0.24);">
      <div style="display:flex; align-items:center; gap:20px;">
        {SVG_VMAA_MARK}
        <div style="width:1.5px; height:40px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
        <div>
          <div class="grotesk" style="font-weight:700; font-size:18px; letter-spacing:0.26em; color:#FFFFFF; text-shadow:0 0 16px rgba(155,77,255,0.6);">
            ORGANIZED BY VMAA · CENTRAL VIETNAM
          </div>
          <div class="mono" style="font-size:10px; color:#D8B4FE; letter-spacing:0.18em; margin-top:4px;">
            VIETNAM MERGERS &amp; ACQUISITIONS ASSOCIATION · HIỆP HỘI MUA BÁN VÀ SÁP NHẬP DOANH NGHIỆP VIỆT NAM
          </div>
        </div>
      </div>

      <div style="display:flex; align-items:center; gap:20px;">
        <!-- Multi-Tonal Spectrum Swatch Indicator ('Các loại và các sắc độ') -->
        <div class="swatch-pill">
          <span class="swatch-dot" style="background:#070D20; color:#245BFF; border:1px solid #63B4FF;"></span>
          <span class="swatch-dot" style="background:#245BFF; color:#245BFF;"></span>
          <span class="swatch-dot" style="background:#6B2D9B; color:#6B2D9B;"></span>
          <span class="swatch-dot" style="background:#9B4DFF; color:#9B4DFF;"></span>
          <span class="swatch-dot" style="background:#E9D5FF; color:#E9D5FF;"></span>
          <span class="swatch-dot" style="background:#63B4FF; color:#63B4FF;"></span>
          <span class="mono" style="font-size:10px; color:#F3E8FF; letter-spacing:0.16em; margin-left:4px;">{tone_badge}</span>
        </div>
        {SVG_ARROW_SW}
      </div>
    </div>
    """


def build_bottom_footer() -> str:
    return f"""
    <div style="display:flex; justify-content:space-between; align-items:center; padding-top:22px; border-top:1px solid rgba(233, 213, 255, 0.26);">
      <!-- High-Contrast Event Logistics (Date · Time · Location) -->
      <div style="display:flex; align-items:center; gap:44px; white-space:nowrap;">
        <div>
          <div class="mono" style="font-size:10.5px; color:#C084FC; margin-bottom:4px;">DATE</div>
          <div class="grotesk" style="font-size:28px; font-weight:700; letter-spacing:0.04em; color:#FFFFFF; text-shadow:0 0 20px rgba(155,77,255,0.55);">13.12.2026</div>
        </div>
        <div style="width:1.5px; height:38px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
        <div>
          <div class="mono" style="font-size:10.5px; color:#63B4FF; margin-bottom:4px;">TIME</div>
          <div class="grotesk" style="font-size:28px; font-weight:700; letter-spacing:0.04em; color:#FFFFFF; text-shadow:0 0 20px rgba(36,91,255,0.55);">13:30–17:30</div>
        </div>
        <div style="width:1.5px; height:38px; background:linear-gradient(180deg, transparent, #9B4DFF, #63B4FF, transparent);"></div>
        <div>
          <div class="mono" style="font-size:10.5px; color:#E9D5FF; margin-bottom:4px;">LOCATION</div>
          <div style="font-family:'Plus Jakarta Sans',sans-serif; font-size:28px; font-weight:800; letter-spacing:0.01em; color:#FFFFFF; text-shadow:0 0 22px rgba(155,77,255,0.65);">Đà Nẵng, Việt Nam</div>
        </div>
      </div>

      <!-- Concise Global Prestige Organizer Lockup with Official VMAA Interlocking Wordmark -->
      <div style="display:flex; align-items:center; gap:22px; white-space:nowrap;">
        <img src="{u_logo_wordmark}" style="height:28px; width:auto; display:block; filter:drop-shadow(0 0 12px rgba(155,77,255,0.75));" alt="VMAA" />
        <div style="width:1px; height:32px; background:rgba(233,213,255,0.35);"></div>
        <div style="text-align:right;">
          <div class="grotesk" style="font-size:13px; font-weight:700; letter-spacing:0.24em; color:#F3E8FF;">ORGANIZED BY VMAA · CENTRAL VIETNAM</div>
          <div class="mono" style="font-size:9.5px; color:#9B4DFF; letter-spacing:0.2em; margin-top:3px;">ARCHITECTURE OF VALUE · 2026 SUMMIT</div>
        </div>
        <div style="padding:10px 18px; background:linear-gradient(135deg, rgba(155,77,255,0.32), rgba(36,91,255,0.32)); border:1px solid #C084FC; border-radius:4px; font-family:'Space Grotesk',sans-serif; font-size:12px; font-weight:700; letter-spacing:0.22em; color:#FFFFFF; box-shadow:0 0 24px rgba(155,77,255,0.4);">
          2026 EDITION
        </div>
      </div>
    </div>
    """


# -------------------------------------------------------------------------
# 3. BUILD 6 LUMINOUS PURPLE × COBALT KEY VISUALS (CONCISE, BOLD, EYE-HITTING)
# -------------------------------------------------------------------------

# TONE 01 ★ (PRIMARY HERO MASTER): Royal Amethyst (#6B2D9B) × Electric Violet (#9B4DFF) × Electric Cobalt (#245BFF)
# Uses Bold Modern Geometric Display (Plus Jakarta Sans 800 + Luminous 2026 Outline)
opt01_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
{COMMON_STYLE}
</style></head><body>
  <div class="plate" style="background-image:url('{u1}');"></div>
  <div class="aurora-wash"></div>
  <div class="left-readability-gradient"></div>

  <!-- Subtle Luminous Geometric Framing Line -->
  <svg style="position:absolute; inset:0; pointer-events:none; z-index:4;" width="1920" height="1080" viewBox="0 0 1920 1080">
    <defs>
      <linearGradient id="lineGrad1" x1="0" y1="0" x2="1920" y2="1080" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#9B4DFF" stop-opacity="0.75"/>
        <stop offset="50%" stop-color="#245BFF" stop-opacity="0.45"/>
        <stop offset="100%" stop-color="#63B4FF" stop-opacity="0.85"/>
      </linearGradient>
    </defs>
    <line x1="74" y1="500" x2="960" y2="500" stroke="url(#lineGrad1)" stroke-width="1" stroke-dasharray="4 8" opacity="0.45"/>
    <circle cx="960" cy="500" r="4" fill="#E9D5FF"/>
  </svg>

  <div class="shell">
    {build_top_header("TONE 01 ★ HERO MASTER // ROYAL AMETHYST × ELECTRIC COBALT")}

    <!-- Center Left Hero Focal Lockup (Concise, Massive, Luminous, Zero Clutter) -->
    <div style="my:auto; max-width:980px;">
      <!-- Luminous Eyebrow -->
      <div style="display:inline-flex; align-items:center; gap:12px; padding:7px 18px; background:rgba(107,45,155,0.42); border:1px solid rgba(192,132,252,0.65); border-radius:999px; margin-bottom:24px; box-shadow:0 0 24px rgba(155,77,255,0.45);">
        <span style="width:8px; height:8px; border-radius:50%; background:#E9D5FF; box-shadow:0 0 12px #FFFFFF;"></span>
        <span class="mono" style="font-size:11.5px; font-weight:600; color:#F3E8FF; letter-spacing:0.26em;">ARCHITECTURE OF VALUE · CENTRAL VIETNAM</span>
      </div>

      <!-- Primary Event Title: Largest, Most Luminous Element on Canvas -->
      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:38px; letter-spacing:0.42em; color:#E9D5FF; text-shadow:0 0 24px rgba(155,77,255,0.85); margin-bottom:6px;">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:26px; white-space:nowrap;">
        <span class="hero-title-glow" style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:134px; line-height:0.94; letter-spacing:-0.03em;">
          M&amp;A
        </span>
        <span class="year-outline-glow" style="font-family:'Outfit',sans-serif; font-weight:800; font-size:118px; line-height:0.94; letter-spacing:-0.02em;">
          2026
        </span>
      </div>

      <div style="display:flex; align-items:center; gap:28px; margin-top:8px; white-space:nowrap;">
        <span style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:92px; line-height:1.04; letter-spacing:-0.015em; background:linear-gradient(90deg, #FFFFFF 0%, #F3E8FF 48%, #93C5FD 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; filter:drop-shadow(0 0 32px rgba(155,77,255,0.75));">
          MIỀN TRUNG
        </span>
      </div>

      <!-- High-Contrast Glowing Sector Bar -->
      <div style="margin-top:34px;">
        <div class="sector-pill">
          <span class="grotesk" style="font-size:22px; font-weight:700; letter-spacing:0.32em; color:#FFFFFF; white-space:nowrap;">
            REAL ESTATE — TECHNOLOGY
          </span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    {build_bottom_footer()}
  </div>
</body></html>"""


# TONE 02 ★: Prismatic Fluted Caustics (Electric Violet #9B4DFF × Soft Lavender #E9D5FF × Creative 20/26 + Script Hybrid)
opt02_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
{COMMON_STYLE}
</style></head><body>
  <div class="plate" style="background-image:url('{u2}');"></div>
  <div class="aurora-wash" style="background:
    radial-gradient(900px 650px at 70% 50%, rgba(192, 132, 252, 0.30) 0%, rgba(36, 91, 255, 0.22) 50%, transparent 80%),
    radial-gradient(760px 600px at 22% 50%, rgba(7, 13, 32, 0.88) 0%, rgba(16, 18, 52, 0.65) 55%, transparent 100%);"></div>
  <div class="left-readability-gradient"></div>

  <div class="shell">
    {build_top_header("TONE 02 ★ // ELECTRIC VIOLET × PRISMATIC FLUTED CAUSTICS")}

    <div style="my:auto; max-width:980px;">
      <div style="display:inline-flex; align-items:center; gap:12px; padding:7px 18px; background:rgba(155,77,255,0.32); border:1px solid #E9D5FF; border-radius:999px; margin-bottom:24px; box-shadow:0 0 28px rgba(155,77,255,0.55);">
        <span style="width:8px; height:8px; border-radius:50%; background:#63B4FF; box-shadow:0 0 12px #63B4FF;"></span>
        <span class="mono" style="font-size:11.5px; font-weight:600; color:#FFFFFF; letter-spacing:0.26em;">OPTICAL CLARITY · CAPITAL × PROPTECH CONVERGENCE</span>
      </div>

      <div style="font-family:'Outfit',sans-serif; font-weight:500; font-size:36px; letter-spacing:0.44em; color:#E9D5FF; text-shadow:0 0 22px rgba(155,77,255,0.9); margin-bottom:8px;">
        DIỄN ĐÀN
      </div>

      <!-- Creative Stencil M&A + Luminous Script 'Miền Trung' + Fractional 20/26 -->
      <div style="display:flex; align-items:baseline; gap:26px; white-space:nowrap;">
        <span class="hero-title-glow" style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:128px; line-height:0.95; letter-spacing:-0.03em; position:relative;">
          M&amp;A
        </span>
        <span class="script-vn" style="font-size:102px; transform:rotate(-4deg) translateY(-8px); display:inline-block;">
          Miền Trung
        </span>
      </div>

      <div style="display:flex; align-items:center; gap:28px; margin-top:16px; white-space:nowrap;">
        <div style="font-family:'Outfit',sans-serif; font-weight:200; font-size:86px; line-height:0.9; letter-spacing:-0.04em; color:#FFFFFF; text-shadow:0 0 28px rgba(155,77,255,0.85);">
          20<span style="color:#C084FC; font-weight:300;">/</span>26
        </div>
        <div style="height:56px; width:2px; background:linear-gradient(180deg, #E9D5FF, #9B4DFF, #245BFF);"></div>
        <div class="sector-pill">
          <span class="grotesk" style="font-size:21px; font-weight:700; letter-spacing:0.3em; color:#FFFFFF; white-space:nowrap;">
            REAL ESTATE — TECHNOLOGY
          </span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    {build_bottom_footer()}
  </div>
</body></html>"""


# TONE 03 ★: Stretched Futuristic Display ('Unbounded' 800) × Ascending Amethyst-Sapphire Cantilevers
opt03_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
{COMMON_STYLE}
</style></head><body>
  <div class="plate" style="background-image:url('{u3}');"></div>
  <div class="aurora-wash"></div>
  <div class="left-readability-gradient" style="background:linear-gradient(90deg, rgba(7,11,28,0.88) 0%, rgba(12,16,44,0.64) 42%, rgba(0,0,0,0) 76%);"></div>

  <div class="shell">
    {build_top_header("TONE 03 ★ // STRETCHED FUTURISTIC SANS × ASCENDING CANTILEVERS")}

    <div style="my:auto; max-width:1040px;">
      <div style="display:inline-flex; align-items:center; gap:12px; padding:7px 18px; background:rgba(36,91,255,0.35); border:1px solid #63B4FF; border-radius:999px; margin-bottom:24px; box-shadow:0 0 24px rgba(36,91,255,0.5);">
        <span style="width:8px; height:8px; border-radius:50%; background:#C084FC; box-shadow:0 0 12px #C084FC;"></span>
        <span class="mono" style="font-size:11.5px; font-weight:600; color:#FFFFFF; letter-spacing:0.24em;">ASCENDING VALUATION EQUILIBRIUM · SINGAPORE PRESTIGE</span>
      </div>

      <!-- Stretched Futuristic Sans-Serif with 100% Uniform Vietnamese Diacritics -->
      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:34px; letter-spacing:0.36em; color:#D8B4FE; text-shadow:0 0 20px rgba(155,77,255,0.85); margin-bottom:10px; transform:scaleX(1.06); transform-origin:left center;">
        DIỄN ĐÀN
      </div>

      <div class="hero-title-glow" style="font-family:'Unbounded',sans-serif; font-weight:900; font-size:112px; line-height:0.98; letter-spacing:-0.02em; white-space:nowrap;">
        M&amp;A <span style="color:#E9D5FF; font-weight:700;">2026</span>
      </div>

      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:86px; line-height:1.08; letter-spacing:0.04em; margin-top:6px; white-space:nowrap; transform:scaleX(1.06); transform-origin:left center; background:linear-gradient(90deg, #FFFFFF 0%, #E9D5FF 55%, #63B4FF 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; filter:drop-shadow(0 0 28px rgba(155,77,255,0.85));">
        MIỀN TRUNG
      </div>

      <div style="margin-top:34px;">
        <div class="sector-pill" style="background:linear-gradient(90deg, #245BFF 0%, #9B4DFF 60%, #EC4899 100%);">
          <span class="grotesk" style="font-size:21px; font-weight:700; letter-spacing:0.32em; color:#FFFFFF; white-space:nowrap;">
            REAL ESTATE — TECHNOLOGY
          </span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    {build_bottom_footer()}
  </div>
</body></html>"""


# TONE 04: Ultraviolet × Ice-Cyan Coastal Meridian Contours (100% Unobstructed Abstract Contours + Condensed Futuristic Sans)
opt04_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
{COMMON_STYLE}
</style></head><body>
  <div class="plate" style="background-image:url('{u4}');"></div>
  <div class="aurora-wash"></div>
  <div class="left-readability-gradient"></div>

  <div class="shell">
    {build_top_header("TONE 04 // ULTRAVIOLET × ICE-CYAN COASTAL MERIDIAN")}

    <div style="my:auto; max-width:960px;">
      <div style="display:inline-flex; align-items:center; gap:12px; padding:7px 18px; background:rgba(107,45,155,0.45); border:1px solid #63B4FF; border-radius:999px; margin-bottom:24px;">
        <span style="width:8px; height:8px; border-radius:50%; background:#63B4FF; box-shadow:0 0 12px #63B4FF;"></span>
        <span class="mono" style="font-size:11.5px; font-weight:600; color:#E9D5FF; letter-spacing:0.24em;">16.0544° N, 108.2022° E · ĐÀ NẴNG COASTAL MERIDIAN</span>
      </div>

      <div style="font-family:'Chakra Petch',sans-serif; font-weight:700; font-size:38px; letter-spacing:0.38em; color:#63B4FF; text-shadow:0 0 20px rgba(99,180,255,0.8); margin-bottom:4px;">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:24px; white-space:nowrap;">
        <span class="hero-title-glow" style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:130px; line-height:0.95; letter-spacing:-0.03em;">
          M&amp;A
        </span>
        <span style="font-family:'Chakra Petch',sans-serif; font-weight:700; font-size:112px; line-height:0.95; color:#E9D5FF; text-shadow:0 0 32px rgba(155,77,255,0.95);">
          20/26
        </span>
      </div>

      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:90px; line-height:1.05; letter-spacing:-0.01em; color:#FFFFFF; text-shadow:0 0 32px rgba(155,77,255,0.85); margin-top:6px; white-space:nowrap;">
        MIỀN TRUNG
      </div>

      <div style="margin-top:34px;">
        <div class="sector-pill">
          <span class="grotesk" style="font-size:21px; font-weight:700; letter-spacing:0.32em; color:#FFFFFF; white-space:nowrap;">
            REAL ESTATE — TECHNOLOGY
          </span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    {build_bottom_footer()}
  </div>
</body></html>"""


# TONE 05: Imperial Purple × Magenta-Lavender Isometric Crystal Matrix
opt05_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
{COMMON_STYLE}
</style></head><body>
  <div class="plate" style="background-image:url('{u5}');"></div>
  <div class="aurora-wash"></div>
  <div class="left-readability-gradient"></div>

  <div class="shell">
    {build_top_header("TONE 05 // IMPERIAL PURPLE × MAGENTA-COBALT CRYSTAL MATRIX")}

    <div style="my:auto; max-width:960px;">
      <div style="display:inline-flex; align-items:center; gap:12px; padding:7px 18px; background:rgba(155,77,255,0.38); border:1px solid #F472B6; border-radius:999px; margin-bottom:24px; box-shadow:0 0 24px rgba(236,72,153,0.45);">
        <span style="width:8px; height:8px; border-radius:50%; background:#F472B6; box-shadow:0 0 12px #F472B6;"></span>
        <span class="mono" style="font-size:11.5px; font-weight:600; color:#FCE7F3; letter-spacing:0.24em;">MODULAR DEAL STRUCTURING · INSTITUTIONAL CAPITAL</span>
      </div>

      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:36px; letter-spacing:0.42em; color:#F5D0FE; margin-bottom:6px;">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:24px; white-space:nowrap;">
        <span class="hero-title-glow" style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:132px; line-height:0.95; letter-spacing:-0.03em;">
          M&amp;A
        </span>
        <span class="year-outline-glow" style="font-family:'Outfit',sans-serif; font-weight:800; font-size:116px; line-height:0.95; -webkit-text-stroke: 2.2px #F472B6;">
          2026
        </span>
      </div>

      <div style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:90px; line-height:1.05; letter-spacing:-0.015em; margin-top:6px; white-space:nowrap; background:linear-gradient(90deg, #FFFFFF 0%, #F5D0FE 55%, #93C5FD 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; filter:drop-shadow(0 0 30px rgba(192,38,211,0.75));">
        MIỀN TRUNG
      </div>

      <div style="margin-top:34px;">
        <div class="sector-pill" style="background:linear-gradient(90deg, #86198F 0%, #9B4DFF 50%, #245BFF 100%); border-color:#F5D0FE;">
          <span class="grotesk" style="font-size:21px; font-weight:700; letter-spacing:0.32em; color:#FFFFFF; white-space:nowrap;">
            REAL ESTATE — TECHNOLOGY
          </span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    {build_bottom_footer()}
  </div>
</body></html>"""


# TONE 06 ★: High-Key Lavender-Aurora × Cobalt Stage Portal (Maximum Stage Brightness)
opt06_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
{COMMON_STYLE}
</style></head><body>
  <div class="plate" style="background-image:url('{u6}'); filter:brightness(1.12) contrast(1.08) saturate(1.18);"></div>
  <div class="aurora-wash" style="background:
    radial-gradient(1100px 760px at 68% 45%, rgba(233, 213, 255, 0.35) 0%, rgba(155, 77, 255, 0.32) 40%, rgba(36, 91, 255, 0.25) 70%, transparent 100%),
    radial-gradient(700px 600px at 20% 50%, rgba(10, 16, 40, 0.82) 0%, rgba(18, 20, 58, 0.52) 60%, transparent 100%);"></div>
  <div class="left-readability-gradient" style="background:linear-gradient(90deg, rgba(7,11,28,0.80) 0%, rgba(14,18,52,0.48) 40%, rgba(0,0,0,0) 70%);"></div>

  <div class="shell">
    {build_top_header("TONE 06 ★ // HIGH-KEY LAVENDER AURORA × ELECTRIC COBALT")}

    <div style="my:auto; max-width:980px;">
      <div style="display:inline-flex; align-items:center; gap:12px; padding:7px 18px; background:linear-gradient(90deg, rgba(155,77,255,0.55), rgba(36,91,255,0.55)); border:1px solid #FFFFFF; border-radius:999px; margin-bottom:24px; box-shadow:0 0 32px rgba(233,213,255,0.6);">
        <span style="width:8px; height:8px; border-radius:50%; background:#FFFFFF; box-shadow:0 0 14px #FFFFFF;"></span>
        <span class="mono" style="font-size:11.5px; font-weight:700; color:#FFFFFF; letter-spacing:0.26em;">HIGH-LUMINOSITY LED STAGE MASTER · WEF / NEXT FORUM GRADE</span>
      </div>

      <div style="font-family:'Outfit',sans-serif; font-weight:600; font-size:38px; letter-spacing:0.42em; color:#FFFFFF; text-shadow:0 0 28px rgba(155,77,255,0.95); margin-bottom:6px;">
        DIỄN ĐÀN
      </div>

      <div style="display:flex; align-items:baseline; gap:26px; white-space:nowrap;">
        <span class="hero-title-glow" style="font-family:'Plus Jakarta Sans',sans-serif; font-weight:800; font-size:134px; line-height:0.94; letter-spacing:-0.03em;">
          M&amp;A
        </span>
        <span class="script-vn" style="font-size:104px; color:#FFFFFF; text-shadow:0 0 28px #9B4DFF, 0 0 56px #245BFF; transform:rotate(-4deg) translateY(-8px); display:inline-block;">
          Miền Trung
        </span>
      </div>

      <div style="display:flex; align-items:center; gap:28px; margin-top:16px; white-space:nowrap;">
        <span style="font-family:'Unbounded',sans-serif; font-weight:800; font-size:74px; line-height:0.95; color:#E9D5FF; text-shadow:0 0 32px rgba(155,77,255,0.95);">
          2026
        </span>
        <div class="sector-pill" style="background:linear-gradient(90deg, #9B4DFF 0%, #245BFF 55%, #00E5FF 100%); border-color:#FFFFFF;">
          <span class="grotesk" style="font-size:21px; font-weight:700; letter-spacing:0.3em; color:#FFFFFF; white-space:nowrap;">
            REAL ESTATE — TECHNOLOGY
          </span>
          {SVG_ARROW_NE}
        </div>
      </div>
    </div>

    {build_bottom_footer()}
  </div>
</body></html>"""


# -------------------------------------------------------------------------
# 4. VERTICAL 9:16 STAGE TOTEMS & GITEX HANGING BANNERS (PURPLE × COBALT)
# -------------------------------------------------------------------------
gitex_banners_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
{COMMON_STYLE}
  .banner-card {{
    width: 350px; height: 750px;
    background: linear-gradient(180deg, #070D20 0%, #1E1048 38%, #6B2D9B 72%, #245BFF 100%);
    border: 1.5px solid rgba(233, 213, 255, 0.55);
    border-top: 5px solid #E9D5FF;
    box-shadow: 0 36px 90px rgba(0,0,0,0.88), 0 0 65px rgba(155, 77, 255, 0.42);
    padding: 34px 32px;
    display: flex; flex-direction: column; justify-content: space-between;
    position: relative;
    overflow: hidden;
  }}
  .banner-glow {{
    position: absolute; inset: 0; pointer-events: none;
    background: radial-gradient(circle at 75% 30%, rgba(155,77,255,0.45) 0%, rgba(36,91,255,0.25) 45%, transparent 75%);
  }}
  .wire {{
    position: absolute; top: -120px; width: 1.5px; height: 120px;
    background: linear-gradient(180deg, rgba(255,255,255,0.1), rgba(233,213,255,0.85));
  }}
</style></head><body>
  <div class="plate" style="background-image:url('{u_aud}');"></div>
  <div style="position:absolute; inset:0; background:radial-gradient(circle at 50% 45%, rgba(107,45,155,0.28) 0%, rgba(7,13,32,0.82) 100%);"></div>

  <!-- Top Title Overlay -->
  <div style="position:absolute; top:32px; left:56px; right:56px; display:flex; justify-content:space-between; align-items:center; z-index:10;">
    <div>
      <span class="mono" style="font-size:11px; color:#E9D5FF;">9:16 VERTICAL STAGE TOTEMS &amp; HANGING BANNERS // PURPLE × ELECTRIC COBALT EDITION</span>
      <h2 style="font-size:24px; font-weight:800; margin-top:4px; color:#FFFFFF; text-shadow:0 0 20px rgba(155,77,255,0.7);">
        ARCHITECTURE OF VALUE · VERTICAL 90° LOCKUP &amp; STAGE PILLARS
      </h2>
    </div>
    <span class="mono" style="font-size:11px; color:#E9D5FF;">13.12.2026 · 13:30–17:30 · ĐÀ NẴNG, VIỆT NAM</span>
  </div>

  <!-- 3 Suspended Vertical 9:16 Banners -->
  <div style="position:absolute; top:124px; left:0; right:0; display:flex; justify-content:center; gap:64px; z-index:10;">

    <!-- Banner 1: Left Editorial Headline -->
    <div class="banner-card" style="transform:translateY(14px);">
      <div class="banner-glow"></div>
      <div class="wire" style="left:24px;"></div>
      <div class="wire" style="right:24px;"></div>
      <div style="display:flex; justify-content:space-between; align-items:center; position:relative; z-index:2;">
        <img src="{u_logo_full}" style="height:34px; width:auto; filter:drop-shadow(0 0 8px rgba(155,77,255,0.7));" alt="VMAA"/>
        {SVG_ARROW_SW}
      </div>
      <div style="position:relative; z-index:2; font-family:'Plus Jakarta Sans',sans-serif; font-size:44px; font-weight:800; line-height:1.08; letter-spacing:-0.02em; color:#FFFFFF; text-shadow:0 0 24px rgba(155,77,255,0.75);">
        Architecture<br>of Value<br>in Central<br>Vietnam
      </div>
      <div class="grotesk" style="position:relative; z-index:2; font-size:12px; font-weight:700; letter-spacing:0.22em; line-height:1.8; color:#F3E8FF;">
        REAL ESTATE<br>
        TECHNOLOGY<br>
        CAPITAL FLOWS<br>
        CONVERGENCE
      </div>
    </div>

    <!-- Banner 2: Center Hero Vertical 90° Lockup -->
    <div class="banner-card" style="border-color:#FFFFFF; box-shadow:0 36px 95px rgba(0,0,0,0.92), 0 0 80px rgba(155,77,255,0.65); background:linear-gradient(180deg, #070D20 0%, #2A125E 35%, #9B4DFF 72%, #245BFF 100%);">
      <div class="banner-glow"></div>
      <div class="wire" style="left:24px;"></div>
      <div class="wire" style="right:24px;"></div>
      <div style="display:flex; justify-content:space-between; align-items:center; position:relative; z-index:2;">
        <img src="{u_logo_full}" style="height:36px; width:auto; filter:drop-shadow(0 0 10px rgba(255,255,255,0.6));" alt="VMAA"/>
        {SVG_ARROW_SW}
      </div>

      <!-- Rotated -90deg Centerpiece -->
      <div style="flex:1; display:flex; align-items:center; justify-content:center; position:relative; z-index:2;">
        <div style="transform:rotate(-90deg); white-space:nowrap; display:flex; flex-direction:column; gap:6px;">
          <div style="display:flex; align-items:baseline; gap:18px; white-space:nowrap;">
            <span style="font-family:'Outfit',sans-serif; font-size:15px; font-weight:600; letter-spacing:0.38em; color:#E9D5FF;">DIỄN ĐÀN</span>
            <span class="hero-title-glow" style="font-family:'Plus Jakarta Sans',sans-serif; font-size:68px; font-weight:800; letter-spacing:0.06em; line-height:0.92;">
              M&amp;A
            </span>
            <span style="font-family:'Outfit',sans-serif; font-size:64px; font-weight:300; letter-spacing:-0.04em; line-height:0.92; color:#FFFFFF;">
              20<span style="color:#E9D5FF;">/</span>26
            </span>
          </div>

          <div style="display:flex; align-items:center; justify-content:space-between; gap:22px; padding-left:4px; white-space:nowrap;">
            <div class="grotesk" style="font-size:11.5px; font-weight:700; letter-spacing:0.24em; line-height:1.55; border-left:2px solid #E9D5FF; padding-left:12px; color:#FFFFFF; white-space:nowrap;">
              13.12.2026 &nbsp;·&nbsp; <span style="color:#E9D5FF;">— ĐÀ NẴNG —</span>
            </div>
            <span class="script-vn" style="font-size:60px; line-height:0.9; color:#FFFFFF;">
              Miền Trung
            </span>
          </div>
        </div>
      </div>

      <div class="grotesk" style="position:relative; z-index:2; font-size:11.5px; font-weight:700; letter-spacing:0.18em; line-height:1.6; color:#FFFFFF;">
        ORGANIZED BY VMAA · CENTRAL VIETNAM<br>
        <span style="color:#E9D5FF;">REAL ESTATE — TECHNOLOGY</span>
      </div>
    </div>

    <!-- Banner 3: Right Editorial Headline -->
    <div class="banner-card" style="transform:translateY(14px);">
      <div class="banner-glow"></div>
      <div class="wire" style="left:24px;"></div>
      <div class="wire" style="right:24px;"></div>
      <div style="display:flex; justify-content:space-between; align-items:center; position:relative; z-index:2;">
        <img src="{u_logo_full}" style="height:34px; width:auto; filter:drop-shadow(0 0 8px rgba(155,77,255,0.7));" alt="VMAA"/>
        {SVG_ARROW_SW}
      </div>
      <div style="position:relative; z-index:2; font-family:'Plus Jakarta Sans',sans-serif; font-size:44px; font-weight:800; line-height:1.08; letter-spacing:-0.02em; color:#FFFFFF; text-shadow:0 0 24px rgba(155,77,255,0.75);">
        Vietnam's<br>Next<br>Investment<br>Gateway
      </div>
      <div class="grotesk" style="position:relative; z-index:2; font-size:12px; font-weight:700; letter-spacing:0.18em; line-height:1.7; color:#F3E8FF;">
        13.12.2026 · 13:30–17:30<br>
        ĐÀ NẴNG, VIỆT NAM
      </div>
    </div>

  </div>
</body></html>"""


options_list = [
    ("OPT_01_Monolith_Convergence", opt01_html, "Tone 01 ★ · Royal Amethyst × Electric Cobalt", "PRIMARY HERO MASTER · Blazing Core Beam + Geometric VIP Display"),
    ("OPT_02_Ascending_Equilibrium", opt02_html, "Tone 02 ★ · Electric Violet × Fluted Caustics", "Iridescent 'Loan Loan' Prisms + Creative 20/26 & Script Lockup"),
    ("OPT_03_Coastal_Meridian_Contours", opt03_html, "Tone 03 ★ · Neon Amethyst × Sapphire Cantilevers", "Stretched Futuristic Sans ('Unbounded') + 7 Ascending Glass Towers"),
    ("OPT_04_Luminous_Tri_Portal", opt04_html, "Tone 04 · Ultraviolet × Ice-Cyan Meridian", "100% Abstract Coastal Contours + Condensed Futuristic Display"),
    ("OPT_05_Isometric_Deal_Matrix", opt05_html, "Tone 05 · Imperial Purple × Magenta-Cobalt Matrix", "Interlocking Isometric Crystal Volumes + Orchid-Magenta Rim Glow"),
    ("OPT_06_Fluted_Prism_Curtain", opt06_html, "Tone 06 ★ · High-Key Lavender Aurora × Cobalt", "Maximum LED Stage Luminosity + Multi-Tonal Aurora Diffusion"),
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
    page = context.new_page()

    rendered_uris = {}
    for name, html_code, title, desc in options_list:
        html_file = EXPORTS_DIR / f"{name}.html"
        html_file.write_text(html_code, encoding="utf-8")
        page.goto(html_file.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(500)
        png_path = EXPORTS_DIR / f"{name}.png"
        brain_path = BRAIN_DIR / f"{name}.png"
        page.screenshot(path=str(png_path), full_page=False)
        shutil.copy(png_path, brain_path)
        rendered_uris[name] = "data:image/png;base64," + base64.b64encode(png_path.read_bytes()).decode("ascii")
        print(f"Rendered {name}.png (3840x2160 4K UHD)")

    # Save Primary Hero Master explicitly as 01_VMAA_HERO_KEY_VISUAL_4K.png as well!
    hero_png = EXPORTS_DIR / "01_VMAA_HERO_KEY_VISUAL_4K.png"
    shutil.copy(EXPORTS_DIR / "OPT_01_Monolith_Convergence.png", hero_png)
    shutil.copy(hero_png, BRAIN_DIR / "01_VMAA_HERO_KEY_VISUAL_4K.png")
    print("Saved Primary Hero Key Visual Master -> 01_VMAA_HERO_KEY_VISUAL_4K.png")

    # Render 08_VMAA_GITEX_Hanging_Banners_Stage.png
    g_file = EXPORTS_DIR / "08_VMAA_GITEX_Hanging_Banners_Stage.html"
    g_file.write_text(gitex_banners_html, encoding="utf-8")
    page.goto(g_file.as_uri(), wait_until="networkidle")
    page.wait_for_timeout(450)
    g_png = EXPORTS_DIR / "08_VMAA_GITEX_Hanging_Banners_Stage.png"
    page.screenshot(path=str(g_png), full_page=False)
    shutil.copy(g_png, BRAIN_DIR / "08_VMAA_GITEX_Hanging_Banners_Stage.png")
    u_gitex = "data:image/png;base64," + base64.b64encode(g_png.read_bytes()).decode("ascii")
    print("Rendered 08_VMAA_GITEX_Hanging_Banners_Stage.png (3840x2160 4K UHD)")

    # -------------------------------------------------------------------------
    # RENDER 00_VMAA_6_Options_Comparison_Matrix.png (6 Purple-Cobalt Tonal Shades)
    # -------------------------------------------------------------------------
    cards_html = ""
    for name, _, title, desc in options_list:
        is_fav = "★" in title
        border_col = "#C084FC" if is_fav else "rgba(155,77,255,0.42)"
        badge_bg = "linear-gradient(90deg, #9B4DFF, #245BFF)" if is_fav else "rgba(26,18,64,0.85)"
        badge_txt = "EYE-HITTING ★" if is_fav else "4K TONE"
        cards_html += f"""
        <div style="background:#050A19; border:1.5px solid {border_col}; display:flex; flex-direction:column; overflow:hidden; box-shadow:0 0 28px rgba(155,77,255,0.2);">
          <div style="flex:1; background-image:url('{rendered_uris[name]}'); background-size:contain; background-repeat:no-repeat; background-position:center; background-color:#050A19;"></div>
          <div style="padding:10px 16px; background:linear-gradient(90deg, #09112A, #190E3A); border-top:1px solid rgba(192,132,252,0.32); display:flex; justify-content:space-between; align-items:center; gap:10px;">
            <div style="min-width:0;">
              <div style="font-size:14px; font-weight:700; color:#FFFFFF; white-space:nowrap;">{title}</div>
              <div class="mono" style="font-size:9px; color:#E9D5FF; letter-spacing:0.08em; white-space:nowrap;">{desc}</div>
            </div>
            <span class="mono" style="font-size:9px; padding:4px 10px; background:{badge_bg}; border:1px solid #E9D5FF; color:#FFFFFF; white-space:nowrap;">{badge_txt}</span>
          </div>
        </div>
        """

    matrix_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
    {COMMON_STYLE}
    body {{
      background: #040714; padding: 26px 40px;
      display: flex; flex-direction: column; justify-content: space-between;
    }}
    </style></head><body>
      <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:14px; border-bottom:1px solid rgba(192,132,252,0.35);">
        <div style="display:flex; align-items:center; gap:18px;">
          {SVG_VMAA_MARK}
          <div>
            <div class="mono" style="font-size:11px; color:#C084FC;">HIGH-LUMINOSITY PURPLE × ELECTRIC COBALT SPECTRUM // 6 TONAL &amp; TYPOGRAPHIC VARIATIONS</div>
            <h1 style="font-size:21px; font-weight:800; margin-top:4px; white-space:nowrap; color:#FFFFFF; text-shadow:0 0 20px rgba(155,77,255,0.7);">
              DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026 — 6 SẮC ĐỘ TÍM × COBALT LẤP LÁNH ("LOAN LOAN" LUMINOUS GRADIENT)
            </h1>
          </div>
        </div>
        <div class="mono" style="font-size:10px; text-align:right; color:#E9D5FF; white-space:nowrap;">
          #070D20 OBSIDIAN · #245BFF COBALT · #6B2D9B→#9B4DFF VIOLET · #E9D5FF LAVENDER<br>
          13.12.2026 | 13:30–17:30 · ĐÀ NẴNG, VIỆT NAM
        </div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); grid-template-rows:repeat(2, 1fr); gap:18px; height:905px; margin-top:16px;">
        {cards_html}
      </div>
    </body></html>"""

    matrix_file = EXPORTS_DIR / "00_VMAA_6_Options_Comparison_Matrix.html"
    matrix_file.write_text(matrix_html, encoding="utf-8")
    page.goto(matrix_file.as_uri(), wait_until="networkidle")
    page.wait_for_timeout(450)
    m_png = EXPORTS_DIR / "00_VMAA_6_Options_Comparison_Matrix.png"
    page.screenshot(path=str(m_png), full_page=False)
    shutil.copy(m_png, BRAIN_DIR / "00_VMAA_6_Options_Comparison_Matrix.png")
    print("Rendered 00_VMAA_6_Options_Comparison_Matrix.png (3840x2160 4K UHD)")

    # -------------------------------------------------------------------------
    # RENDER 07_VMAA_Multi_Aspect_Venue_Suite.png (Purple × Cobalt Stage Expansion)
    # -------------------------------------------------------------------------
    suite_html = f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
    {COMMON_STYLE}
    body {{
      background: #040714; padding: 24px 36px;
      display: flex; flex-direction: column; gap: 16px;
    }}
    .card {{
      background: #070D20; border: 1px solid rgba(192,132,252,0.38);
      position: relative; overflow: hidden; padding: 20px 26px;
      display: flex; flex-direction: column; justify-content: space-between;
      box-shadow: 0 0 28px rgba(155,77,255,0.16);
    }}
    </style></head><body>
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(192,132,252,0.32); padding-bottom:10px;">
        <div style="display:flex; align-items:center; gap:16px;">
          {SVG_VMAA_MARK}
          <div>
            <span class="mono" style="font-size:10.5px; color:#C084FC;">COMPLETE VENUE &amp; BROADCAST DELIVERY SUITE // PURPLE × ELECTRIC COBALT LUMINOUS SYSTEM</span>
            <h2 style="font-size:22px; font-weight:800; color:#FFFFFF; text-shadow:0 0 18px rgba(155,77,255,0.65);">
              32:9 LED STAGE WALL · 9:16 VERTICAL TOTEMS · 16:9 SPEAKER INTRO · IMAG LOWER-THIRD &amp; AWARD
            </h2>
          </div>
        </div>
        <span class="mono" style="font-size:10.5px; color:#E9D5FF;">13.12.2026 · 13:30–17:30 · ĐÀ NẴNG, VIỆT NAM</span>
      </div>

      <!-- 1. 32:9 Ultra-Wide Curved LED Stage Wall (Sphere-Free Architectural Modules!) -->
      <div class="card" style="height:255px; background-image:url('{u1}'); background-size:cover; background-position:center 42%;">
        <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(7,13,32,0.92) 0%, rgba(28,14,68,0.68) 45%, rgba(7,13,32,0.78) 100%);"></div>
        <div style="position:relative; z-index:2; display:flex; justify-content:space-between; align-items:center;">
          <span class="mono" style="font-size:10px; color:#E9D5FF;">01 // 32:9 ULTRA-WIDE AUDITORIUM LED WALL (7680×2160 MASTER · ARCHITECTURE OF VALUE)</span>
          <span class="mono" style="font-size:10px; color:#63B4FF;">LOWER 22% STAGE ARMCHAIRS SAFE ZONE</span>
        </div>

        <div style="position:relative; z-index:2; display:grid; grid-template-columns: 1.25fr 1fr 1fr 1fr; gap:24px; align-items:center; margin:auto 0;">
          <div>
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:6px;">
              <img src="{u_logo_wordmark}" style="height:22px; width:auto;" alt="VMAA"/>
              <span style="font-family:'Outfit',sans-serif; font-weight:600; font-size:14px; letter-spacing:0.36em; color:#E9D5FF;">DIỄN ĐÀN</span>
            </div>
            <div style="display:flex; align-items:baseline; gap:14px; white-space:nowrap;">
              <span class="hero-title-glow" style="font-size:46px; font-weight:800; letter-spacing:-0.03em;">M&amp;A MIỀN TRUNG</span>
              <span style="font-family:'Outfit',sans-serif; font-weight:300; font-size:38px; color:#E9D5FF;">2026</span>
            </div>
            <div class="grotesk" style="font-size:11.5px; font-weight:700; letter-spacing:0.24em; color:#63B4FF; margin-top:4px;">REAL ESTATE — TECHNOLOGY · 13.12.2026</div>
          </div>

          <!-- 3 Faceted Crystal Architectural Modules (Strictly No Generic Spheres!) -->
          <div style="height:128px; background:linear-gradient(135deg, rgba(107,45,155,0.55), rgba(10,22,40,0.88)); border:1px solid #C084FC; border-left:4px solid #E9D5FF; display:flex; flex-direction:column; justify-content:center; padding:0 24px; box-shadow:0 0 32px rgba(155,77,255,0.35);">
            <div class="mono" style="font-size:9.5px; color:#E9D5FF;">PILLAR 01 // REAL ESTATE</div>
            <div style="font-size:15px; font-weight:700; margin-top:4px; color:#FFFFFF;">Strategic Real Estate &amp; Land Bank Convergence</div>
          </div>
          <div style="height:128px; background:linear-gradient(135deg, rgba(155,77,255,0.65), rgba(36,91,255,0.55)); border:1.5px solid #FFFFFF; border-left:4px solid #63B4FF; display:flex; flex-direction:column; justify-content:center; padding:0 24px; box-shadow:0 0 42px rgba(155,77,255,0.5);">
            <div class="mono" style="font-size:9.5px; color:#FFFFFF;">PILLAR 02 // M&amp;A CAPITAL</div>
            <div style="font-size:15px; font-weight:700; margin-top:4px; color:#FFFFFF;">Institutional Capital Delivering Tangible Value</div>
          </div>
          <div style="height:128px; background:linear-gradient(135deg, rgba(36,91,255,0.55), rgba(10,22,40,0.88)); border:1px solid #63B4FF; border-left:4px solid #9B4DFF; display:flex; flex-direction:column; justify-content:center; padding:0 24px; box-shadow:0 0 32px rgba(36,91,255,0.35);">
            <div class="mono" style="font-size:9.5px; color:#63B4FF;">PILLAR 03 // TECHNOLOGY</div>
            <div style="font-size:15px; font-weight:700; margin-top:4px; color:#FFFFFF;">PropTech &amp; AI Valuation Driving Efficiencies</div>
          </div>
        </div>

        <div style="position:relative; z-index:2; border-top:1px solid rgba(233,213,255,0.28); padding-top:6px; display:flex; justify-content:space-between;" class="mono">
          <span style="font-size:9px; color:#E9D5FF;">▲ PANELIST ARMCHAIR HEAD-CLEARANCE BOUNDARY</span>
          <span style="font-size:9px; color:#C084FC;">ORGANIZED BY VMAA · CENTRAL VIETNAM</span>
        </div>
      </div>

      <!-- Lower 3-Column Grid -->
      <div style="display:grid; grid-template-columns: 460px 1fr 1fr; gap:16px; height:665px;">

        <!-- Col 1: 9:16 Vertical Stage Totems (Wide View + 90° Closeup) -->
        <div class="card" style="background:#060B1E; display:flex; flex-direction:column; justify-content:space-between; gap:12px;">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="mono" style="font-size:10px; color:#E9D5FF;">02 // 9:16 VERTICAL STAGE TOTEMS</span>
            <span class="mono" style="font-size:9.5px; color:#C084FC;">90° VERTICAL LOCKUP</span>
          </div>

          <div style="width:100%; height:228px; background-image:url('{u_gitex}'); background-size:100% 100%; background-position:center; border:1px solid rgba(192,132,252,0.5); position:relative;">
            <span class="mono" style="position:absolute; bottom:6px; left:10px; font-size:8.5px; color:#E9D5FF; background:rgba(7,13,32,0.85); padding:2px 6px;">A · 3 HANGING AUDITORIUM TOTEMS (WIDE STAGE)</span>
          </div>

          <div style="width:100%; flex:1; background-image:url('{u_gitex}'); background-size:235%; background-position:50% 54%; border:1px solid #E9D5FF; position:relative; box-shadow:0 0 28px rgba(155,77,255,0.38);">
            <span class="mono" style="position:absolute; bottom:6px; left:10px; font-size:8.5px; color:#FFFFFF; background:rgba(7,13,32,0.88); padding:2px 6px;">B · 90° ROTATED 'M&amp;A 20/26 MIỀN TRUNG' CLOSEUP</span>
          </div>

          <div class="mono" style="display:flex; justify-content:space-between;">
            <span style="font-size:9px; color:#E9D5FF;">4K MASTER: 08_VMAA_GITEX_Hanging_Banners_Stage.png</span>
          </div>
        </div>

        <!-- Col 2: Speaker Intro Stinger + Live IMAG Lower-Third -->
        <div style="display:grid; grid-template-rows:1fr 1fr; gap:16px;">
          <div class="card" style="background-image:url('{u2}'); background-size:cover;">
            <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(7,13,32,0.92) 0%, rgba(28,12,64,0.55) 100%);"></div>
            <div style="position:relative; z-index:2; display:flex; justify-content:space-between; align-items:center;">
              <span class="mono" style="font-size:10px; color:#E9D5FF;">03 // KEYNOTE SPEAKER INTRO STINGER (16:9)</span>
              <img src="{u_logo_wordmark}" style="height:20px; width:auto;" alt="VMAA"/>
            </div>
            <div style="position:relative; z-index:2; display:flex; align-items:center; gap:26px;">
              <div style="width:126px; height:156px; background:radial-gradient(circle at 50% 25%, #9B4DFF 0%, #245BFF 48%, #070D20 95%); border:1.5px solid #E9D5FF; box-shadow:0 0 32px rgba(155,77,255,0.55); display:flex; flex-direction:column; justify-content:flex-end; align-items:center; padding:12px;">
                <div style="width:44px; height:44px; border-radius:50%; background:rgba(233,213,255,0.45); margin-bottom:8px;"></div>
                <div style="width:74px; height:32px; border-radius:36px 36px 0 0; background:rgba(233,213,255,0.35);"></div>
                <span class="mono" style="font-size:8px; color:#FFFFFF; margin-top:8px;">SPEAKER PORTRAIT</span>
              </div>
              <div>
                <div class="mono" style="font-size:10px; color:#E9D5FF; margin-bottom:6px;">KEYNOTE ADDRESS · REAL ESTATE × TECH</div>
                <div class="hero-title-glow" style="font-size:36px; font-weight:800; letter-spacing:-0.02em;">TS. Nguyễn Văn A</div>
                <div style="font-size:14.5px; color:#E9D5FF; margin-top:4px;">Chủ tịch HĐQT / Managing Partner · Quỹ Đầu tư Chiến lược</div>
                <div style="margin-top:12px; padding-top:10px; border-top:1px solid rgba(233,213,255,0.3); font-size:13.5px; color:#FFFFFF;">
                  “Kiến trúc Giá trị Mới &amp; Định giá Tài sản Công nghệ tại Miền Trung 2026”
                </div>
              </div>
            </div>
            <div style="position:relative; z-index:2; display:flex; justify-content:space-between;" class="mono">
              <span style="font-size:9px; color:#E9D5FF;">DIỄN ĐÀN M&amp;A MIỀN TRUNG 2026</span>
              <span style="font-size:9px; color:#63B4FF;">13.12.2026 · ĐÀ NẴNG</span>
            </div>
          </div>

          <div class="card" style="background-image:url('{u_aud}'); background-size:cover; background-position:center 35%;">
            <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(7,13,32,0.55) 0%, rgba(7,13,32,0.88) 100%);"></div>
            <div style="position:relative; z-index:2; display:flex; justify-content:space-between;">
              <span class="mono" style="font-size:10px; color:#E9D5FF;">04 // LIVE IMAG CAMERA WING + ALPHA LOWER-THIRD</span>
              <span class="mono" style="font-size:10px; color:#FFFFFF;">SDI / NDI KEY</span>
            </div>
            <div style="position:relative; z-index:2; margin-top:auto; background:linear-gradient(90deg, rgba(10,16,42,0.95) 0%, rgba(107,45,155,0.88) 55%, rgba(36,91,255,0.85) 100%); border-left:4px solid #E9D5FF; border-bottom:1px solid #C084FC; padding:16px 24px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 12px 36px rgba(0,0,0,0.8);">
              <div>
                <div style="font-size:22px; font-weight:800; color:#FFFFFF;">Ông Trần Minh B</div>
                <div class="mono" style="font-size:10px; color:#E9D5FF; margin-top:4px;">TỔNG GIÁM ĐỐC · TẬP ĐOÀN BẤT ĐỘNG SẢN &amp; CÔNG NGHỆ</div>
              </div>
              <div style="display:flex; align-items:center; gap:14px; white-space:nowrap;">
                <img src="{u_logo_wordmark}" style="height:22px; width:auto;" alt="VMAA"/>
                <div>
                  <span style="font-size:20px; font-weight:800; color:#FFFFFF;">M&amp;A</span>
                  <span style="font-family:'Outfit',sans-serif; font-size:20px; font-weight:300; color:#E9D5FF;">2026</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Col 3: MOU Signing Backdrop + Award Reveal Frame -->
        <div style="display:grid; grid-template-rows:1fr 1fr; gap:16px;">
          <div class="card" style="background-image:url('{u1}'); background-size:cover;">
            <div style="position:absolute; inset:0; background:rgba(7,13,32,0.78);"></div>
            <div style="position:relative; z-index:2; display:flex; justify-content:space-between;">
              <span class="mono" style="font-size:10px; color:#E9D5FF;">05 // STRATEGIC M&amp;A DEAL SIGNING CEREMONY (MOU)</span>
              <span class="mono" style="font-size:10px; color:#C084FC;">✦</span>
            </div>
            <div style="position:relative; z-index:2; text-align:center; margin:auto 0;">
              <div class="mono" style="font-size:10.5px; color:#E9D5FF; letter-spacing:0.26em;">LỄ KÝ KẾT THỎA THUẬN HỢP TÁC CHIẾN LƯỢC</div>
              <div class="hero-title-glow" style="font-size:28px; font-weight:800; margin-top:6px;">
                STRATEGIC M&amp;A PARTNERSHIP <span style="font-weight:300; color:#E9D5FF;">2026</span>
              </div>
              <div style="display:flex; justify-content:center; align-items:center; gap:32px; margin-top:18px; padding:14px 24px; background:linear-gradient(90deg, rgba(107,45,155,0.45), rgba(36,91,255,0.45)); border-top:1px solid #E9D5FF; border-bottom:1px solid #63B4FF;">
                <span class="grotesk" style="font-size:14px; font-weight:700; letter-spacing:0.18em;">INVESTMENT FUND A</span>
                <span style="color:#E9D5FF;">✦</span>
                <span class="grotesk" style="font-size:14px; font-weight:700; letter-spacing:0.18em;">RE / TECH ENTERPRISE B</span>
              </div>
            </div>
            <div style="position:relative; z-index:2; text-align:center;" class="mono">
              <span style="font-size:9px; color:#E9D5FF;">13.12.2026 · ĐÀ NẴNG, VIỆT NAM · ORGANIZED BY VMAA</span>
            </div>
          </div>

          <div class="card" style="background-image:url('{u3}'); background-size:cover;">
            <div style="position:absolute; inset:0; background:linear-gradient(90deg, rgba(7,13,32,0.90) 0%, rgba(28,12,64,0.48) 100%);"></div>
            <div style="position:relative; z-index:2; display:flex; justify-content:space-between;">
              <span class="mono" style="font-size:10px; color:#E9D5FF;">06 // VMAA M&amp;A EXCELLENCE AWARD REVEAL</span>
              <span class="mono" style="font-size:10px; color:#FFFFFF;">AWARD MASTER</span>
            </div>
            <div style="position:relative; z-index:2; margin:auto 0;">
              <div class="mono" style="font-size:10px; color:#E9D5FF;">VINH DANH THƯƠNG VỤ &amp; DOANH NGHIỆP TIÊU BIỂU</div>
              <div style="display:flex; align-items:baseline; gap:16px; margin:6px 0 12px; white-space:nowrap;">
                <span class="hero-title-glow" style="font-size:34px; font-weight:800;">DEAL OF THE YEAR</span>
                <span class="script-vn" style="font-size:36px;">Miền Trung</span>
              </div>
              <div class="sector-pill" style="padding:9px 22px;">
                <span class="grotesk" style="font-size:13px; font-weight:700; letter-spacing:0.22em;">HONOREE ORGANIZATION 2026</span>
                {SVG_ARROW_NE}
              </div>
            </div>
            <div style="position:relative; z-index:2; display:flex; justify-content:space-between;" class="mono">
              <span style="font-size:9px; color:#E9D5FF;">VMAA M&amp;A MIỀN TRUNG 2026</span>
              <span style="font-size:9px; color:#FFFFFF;">13.12.2026 · ĐÀ NẴNG</span>
            </div>
          </div>
        </div>

      </div>
    </body></html>"""

    suite_file = EXPORTS_DIR / "07_VMAA_Multi_Aspect_Venue_Suite.html"
    suite_file.write_text(suite_html, encoding="utf-8")
    page.goto(suite_file.as_uri(), wait_until="networkidle")
    page.wait_for_timeout(450)
    s_png = EXPORTS_DIR / "07_VMAA_Multi_Aspect_Venue_Suite.png"
    page.screenshot(path=str(s_png), full_page=False)
    shutil.copy(s_png, BRAIN_DIR / "07_VMAA_Multi_Aspect_Venue_Suite.png")
    print("Rendered 07_VMAA_Multi_Aspect_Venue_Suite.png (3840x2160 4K UHD)")

    # -------------------------------------------------------------------------
    # CAPTURE 05_VMAA_Live_WebGL_Motion_Engine.png
    # -------------------------------------------------------------------------
    index_file = PROJECT_DIR / "index.html"
    if index_file.exists():
        page.goto(index_file.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(900)
        w_png = EXPORTS_DIR / "05_VMAA_Live_WebGL_Motion_Engine.png"
        page.screenshot(path=str(w_png), full_page=False)
        shutil.copy(w_png, BRAIN_DIR / "05_VMAA_Live_WebGL_Motion_Engine.png")
        print("Rendered 05_VMAA_Live_WebGL_Motion_Engine.png (3840x2160 4K UHD)")

    browser.close()

if "--skip-video" in sys.argv:
    sys.exit(0)

# -------------------------------------------------------------------------
# 5. OPEN-SOURCE VIDEO SYNTHESIS PIPELINE (OpenCV Shader + FFmpeg 7.1 H.264 MP4 + Audio)
# -------------------------------------------------------------------------
print("Synthesizing 1080p 30fps H.264 MP4 & WebM Motion Opener with OpenCV + FFmpeg 7.1...")
fps = 30
duration_sec = 12
total_frames = fps * duration_sec
W, H = 1920, 1080

img_opt1 = cv2.resize(cv2.imread(str(EXPORTS_DIR / "OPT_01_Monolith_Convergence.png")), (W, H), interpolation=cv2.INTER_AREA)
img_opt2 = cv2.resize(cv2.imread(str(EXPORTS_DIR / "OPT_02_Ascending_Equilibrium.png")), (W, H), interpolation=cv2.INTER_AREA)
img_opt3 = cv2.resize(cv2.imread(str(EXPORTS_DIR / "OPT_03_Coastal_Meridian_Contours.png")), (W, H), interpolation=cv2.INTER_AREA)
img_gitex = cv2.resize(cv2.imread(str(EXPORTS_DIR / "08_VMAA_GITEX_Hanging_Banners_Stage.png")), (W, H), interpolation=cv2.INTER_AREA)
raw_plate1 = cv2.resize(cv2.imread(str(p1_path)), (W, H), interpolation=cv2.INTER_AREA)

wav_path = VIDEOS_DIR / "opener_audio.wav"
sample_rate = 44100
with wave.open(str(wav_path), "w") as wf:
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(sample_rate)
    samples = []
    for s in range(sample_rate * duration_sec):
        t = s / sample_rate
        env = min(1.0, t / 1.0) * min(1.0, (duration_sec - t) / 1.2)
        sub = 0.25 * math.sin(2 * math.pi * 55.0 * t)
        pad = 0.15 * math.sin(2 * math.pi * 110.0 * t) + 0.10 * math.sin(2 * math.pi * 165.0 * t)
        beat_phase = (t % 0.5)
        tick = 0.18 * math.exp(-beat_phase * 28.0) * math.sin(2 * math.pi * 880.0 * t)
        val = int(max(-1.0, min(1.0, env * (sub + pad + tick))) * 32767)
        samples.append(struct.pack("<hh", val, val))
    wf.writeframes(b"".join(samples))

tmp_raw_mp4 = VIDEOS_DIR / "tmp_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
vw = cv2.VideoWriter(str(tmp_raw_mp4), fourcc, fps, (W, H))

x_grid = np.linspace(0, 1, W, dtype=np.float32)
for f in range(total_frames):
    t = f / fps
    if t < 3.0:
        p = t / 3.0
        ease = p * p * (3 - 2 * p)
        base = cv2.addWeighted(raw_plate1, 1.0 - ease * 0.35, img_opt1, ease, 0)
    elif t < 6.0:
        p = (t - 3.0) / 3.0
        ease = min(1.0, p * 2.2)
        base = cv2.addWeighted(img_opt1, 1.0 - ease, img_opt2, ease, 0)
    elif t < 9.0:
        p = (t - 6.0) / 3.0
        ease = min(1.0, p * 2.2)
        base = cv2.addWeighted(img_opt2, 1.0 - ease, img_opt3, ease, 0)
    else:
        p = (t - 9.0) / 3.0
        ease = min(1.0, p * 2.2)
        base = cv2.addWeighted(img_opt3, 1.0 - ease, img_gitex, ease, 0)

    # Moving Purple-Violet-Cobalt ('loan loan') optical caustic light sweep
    sweep_pos = 0.58 + 0.32 * math.sin(2 * math.pi * (t / 4.0))
    beam_profile = np.exp(-((x_grid - sweep_pos) ** 2) / (2 * (0.055 ** 2)))
    beam_img = np.zeros_like(base, dtype=np.uint8)
    # BGR for luminous electric violet-lavender (#9B4DFF -> B=255, G=90, R=165)
    beam_img[:, :, 0] = (beam_profile * 125).astype(np.uint8)
    beam_img[:, :, 1] = (beam_profile * 55).astype(np.uint8)
    beam_img[:, :, 2] = (beam_profile * 105).astype(np.uint8)
    frame = cv2.add(base, beam_img)

    prog_w = int((f / total_frames) * W)
    frame[H - 3:H, :prog_w] = (255, 132, 192)
    vw.write(frame)

vw.release()

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
final_mp4 = VIDEOS_DIR / "VMAA_2026_Opener_Master.mp4"
final_webm = VIDEOS_DIR / "VMAA_2026_Opener_Preview.webm"

subprocess.run([
    ffmpeg_exe, "-y",
    "-i", str(tmp_raw_mp4),
    "-i", str(wav_path),
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "fast",
    "-c:a", "aac", "-b:a", "192k", "-shortest",
    str(final_mp4)
], check=True)

subprocess.run([
    ffmpeg_exe, "-y",
    "-i", str(tmp_raw_mp4),
    "-i", str(wav_path),
    "-c:v", "libvpx-vp9", "-b:v", "4M", "-deadline", "realtime", "-cpu-used", "4",
    "-c:a", "libopus", "-shortest",
    str(final_webm)
], check=True)

tmp_raw_mp4.unlink(missing_ok=True)
shutil.copy(final_mp4, BRAIN_DIR / "VMAA_2026_Opener_Master.mp4")
shutil.copy(final_webm, BRAIN_DIR / "VMAA_2026_Opener_Preview.webm")
print("Exported Purple-Cobalt H.264 MP4 & VP9 WebM with synthesized audio to videos/ and BRAIN_DIR!")
