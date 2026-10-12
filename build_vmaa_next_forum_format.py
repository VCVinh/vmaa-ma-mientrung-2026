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
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


u_hero_plate = to_data_uri(PLATES_DIR / "purple_opt01_hero_convergence.jpg")
u_prism_plate = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u_logo_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")
u_logo_blue = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_blue_transparent.png")
u_wordmark_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_wordmark_white_transparent.png")
u_wordmark_blue = to_data_uri(PROJECT_DIR / "assets" / "vmaa_wordmark_blue_transparent.png")

FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Chakra+Petch:wght@600;700&family=JetBrains+Mono:wght@500;600;700&family=Outfit:wght@200;300;400;500;600;700;800&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700;1,800&family=Space+Grotesk:wght@500;600;700&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet">
"""

# Speaker data modeled after high-level M&A real estate & tech VIPs
SPEAKERS = [
    {
        "name": "TS. TRẦN ĐÌNH THIÊN",
        "role": "Nguyên Viện trưởng Viện Kinh tế Việt Nam",
        "sub": "Chuyên gia Cố vấn Kinh tế Vĩ mô & Tái cấu trúc M&A",
        "gender": "m1"
    },
    {
        "name": "MICHAEL R. CHEN",
        "role": "Giám đốc Điều hành Quỹ Đầu tư Châu Á - TBD",
        "sub": "Đại diện Liên minh Quỹ PE Quốc tế (Singapore / HK)",
        "gender": "m2"
    },
    {
        "name": "ÔNG MAI HỮU TÍN",
        "role": "Chủ tịch HĐQT & Tổng Giám đốc",
        "sub": "U&I Investment Corporation · Cố vấn Cao cấp M&A",
        "gender": "m3"
    },
    {
        "name": "BÀ ĐẶNG HUỲNH ỨC MY",
        "role": "Chủ tịch HĐQT AgriS & Betrimex",
        "sub": "Tiên phong Tái cấu trúc Vốn & Chuỗi Giá trị Công nghệ",
        "gender": "f1"
    },
    {
        "name": "ÔNG NGUYỄN BÁ DIỆP",
        "role": "Đồng sáng lập & Phó Chủ tịch Cấp cao MoMo",
        "sub": "Chuyên gia Công nghệ Tài chính & Thẩm định FinTech",
        "gender": "m4"
    },
    {
        "name": "BÀ NGUYỄN THỊ MINH GIANG",
        "role": "Nhà sáng lập & Tổng Giám đốc Newing",
        "sub": "Cựu Giám đốc Nhân tài & Văn hóa Mekong Capital",
        "gender": "f2"
    }
]

def generate_avatar_svg(idx: int, is_dark: bool = False) -> str:
    # Stylized executive silhouettes with radiant multi-layer glow rims (matching Next Forum 2026 glowing rims)
    rim_color_1 = "#9B4DFF" if is_dark else "#245BFF"
    rim_color_2 = "#63B4FF" if is_dark else "#C084FC"
    bg_circle = "rgba(18,24,56,0.92)" if is_dark else "rgba(240,244,255,0.95)"
    suit_color = "#3B82F6" if (idx % 2 == 0) else "#8B5CF6"
    tie_color = "#EC4899" if (idx % 3 == 0) else "#F59E0B"
    skin_color = "#FED7AA"
    hair_color = "#1E293B" if (idx != 0) else "#64748B"
    
    return f"""
    <svg width="180" height="180" viewBox="0 0 180 180" fill="none" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="halo_{idx}_{is_dark}" cx="50%" cy="50%" r="50%">
          <stop offset="60%" stop-color="{rim_color_1}" stop-opacity="0.35"/>
          <stop offset="90%" stop-color="{rim_color_2}" stop-opacity="0.75"/>
          <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.95"/>
        </radialGradient>
        <linearGradient id="ringGrad_{idx}_{is_dark}" x1="0" y1="0" x2="180" y2="180" gradientUnits="userSpaceOnUse">
          <stop offset="0%" stop-color="{rim_color_2}"/>
          <stop offset="50%" stop-color="#FFFFFF"/>
          <stop offset="100%" stop-color="{rim_color_1}"/>
        </linearGradient>
        <clipPath id="circleClip_{idx}">
          <circle cx="90" cy="90" r="76"/>
        </clipPath>
      </defs>
      <!-- Outer Dynamic Glow Halo (as in Next Forum glowing oval) -->
      <circle cx="90" cy="90" r="86" stroke="url(#ringGrad_{idx}_{is_dark})" stroke-width="3" stroke-dasharray="14 4" opacity="0.85"/>
      <circle cx="90" cy="90" r="82" fill="url(#halo_{idx}_{is_dark})"/>
      <circle cx="90" cy="90" r="77" fill="{bg_circle}" stroke="url(#ringGrad_{idx}_{is_dark})" stroke-width="2.5"/>
      
      <!-- Executive Portrait Inside Clip -->
      <g clip-path="url(#circleClip_{idx})">
        <!-- Body / Suit -->
        <path d="M40 180 C40 135 60 120 90 120 C120 120 140 135 140 180 Z" fill="{suit_color}"/>
        <!-- Shirt -->
        <polygon points="76,120 104,120 90,150" fill="#FFFFFF"/>
        <!-- Tie -->
        <polygon points="87,125 93,125 91,158 89,158" fill="{tie_color}"/>
        <!-- Neck -->
        <rect x="82" y="98" width="16" height="26" fill="{skin_color}"/>
        <!-- Head -->
        <ellipse cx="90" cy="78" rx="26" ry="32" fill="{skin_color}"/>
        <!-- Hair -->
        <path d="M64 74 C64 50 75 42 90 42 C105 42 116 50 116 74 C112 66 102 60 90 60 C78 60 68 66 64 74 Z" fill="{hair_color}"/>
        <!-- Eyeglasses for some -->
        {"<rect x='74' y='72' width='13' height='9' rx='2' fill='none' stroke='#334155' stroke-width='1.8'/><rect x='93' y='72' width='13' height='9' rx='2' fill='none' stroke='#334155' stroke-width='1.8'/><line x1='87' y1='76' x2='93' y2='76' stroke='#334155' stroke-width='1.8'/>" if idx in [0, 4] else ""}
      </g>
    </svg>
    """


# =========================================================================
# 1. OPTION A: HIGH-KEY PLATINUM & IVORY GOLD (DIRECT NEXT FORUM FORMAT MATCH)
# =========================================================================
def build_html_highkey():
    speakers_html = ""
    for i, sp in enumerate(SPEAKERS):
        avatar = generate_avatar_svg(i, is_dark=False)
        speakers_html += f"""
        <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
          <div style="margin-bottom:14px; position:relative;">
            {avatar}
          </div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:17.5px; font-weight:700; color:#0A1628; letter-spacing:0.04em; text-transform:uppercase; margin-bottom:5px;">
            {sp['name']}
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:12.5px; font-weight:600; color:#3B4860; line-height:1.35; max-width:260px; margin-bottom:3px;">
            {sp['role']}
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:11.5px; font-weight:500; color:#6B7280; line-height:1.3; max-width:250px;">
            {sp['sub']}
          </div>
        </div>
        """

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: #F9FAFB; font-family: 'Plus Jakarta Sans', sans-serif; color: #0A1628; position: relative;
      }}
      .bg-canvas {{
        position: absolute; inset: 0;
        background:
          radial-gradient(1200px 900px at 20% 80%, rgba(216,180,254,0.32) 0%, rgba(243,232,255,0.15) 40%, transparent 75%),
          radial-gradient(1000px 800px at 85% 20%, rgba(191,219,254,0.35) 0%, transparent 65%),
          linear-gradient(135deg, #FCFDFF 0%, #F5F7FA 45%, #EFF2F7 100%);
      }}
      .fluid-swirl {{
        position: absolute; bottom: -80px; left: -100px; width: 950px; height: 750px;
        background:
          radial-gradient(ellipse 650px 450px at 45% 65%, rgba(155,77,255,0.22) 0%, rgba(36,91,255,0.25) 45%, transparent 75%);
        filter: blur(40px); pointer-events: none;
      }}
      .container {{
        position: absolute; inset: 0; padding: 36px 64px 30px 64px;
        display: flex; flex-direction: column; justify-content: space-between; z-index: 10;
      }}
      .sponsor-title {{
        font-family: 'Space Grotesk', sans-serif; font-size: 10px; font-weight: 700;
        letter-spacing: 0.16em; text-transform: uppercase; color: #4B5563; margin-bottom: 7px;
      }}
      .sponsor-badge {{
        font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 14.5px;
        display: flex; align-items: center; gap: 8px; color: #111827;
      }}
    </style></head><body>
      <div class="bg-canvas"></div>
      <div class="fluid-swirl"></div>

      <div class="container">
        <!-- 1. TOP SPONSOR & ORGANIZER BAR (Directly matching Next Forum Header Structure) -->
        <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:18px; border-bottom:1.5px solid rgba(209,213,219,0.7);">
          <div>
            <div class="sponsor-title">NHÀ TÀI TRỢ ĐỒNG HÀNH</div>
            <div class="sponsor-badge" style="color:#2563EB;">
              <span style="display:inline-block; width:12px; height:12px; border-radius:50%; background:#2563EB;"></span>
              CENTRAL CAPITAL GROUP
            </div>
          </div>
          <div>
            <div class="sponsor-title">NHÀ TÀI TRỢ VÀNG</div>
            <div class="sponsor-badge" style="color:#D97706; font-size:16px;">
              <span style="display:inline-block; width:14px; height:14px; border-radius:3px; background:linear-gradient(135deg, #F59E0B, #B45309);"></span>
              SUNSHINE HERITAGE HOLDINGS
            </div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <div class="sponsor-title" style="color:#6B2D9B;">ĐƠN VỊ TỔ CHỨC CHỦ TRÌ</div>
            <img src="{u_logo_blue}" alt="VMAA Logo" style="height:44px; width:auto; filter:drop-shadow(0 4px 10px rgba(0,66,138,0.22));"/>
          </div>
          <div>
            <div class="sponsor-title">ĐỐI TÁC HỌC THUẬT &amp; VIỆN NGHIÊN CỨU</div>
            <div class="sponsor-badge" style="color:#DC2626;">
              <span style="display:inline-block; width:12px; height:12px; border-radius:50%; background:#DC2626;"></span>
              ĐẠI HỌC KINH TẾ ĐÀ NẴNG · DUE
            </div>
          </div>
          <div>
            <div class="sponsor-title">NHÀ TÀI TRỢ BẠC</div>
            <div class="sponsor-badge" style="color:#4B5563;">
              <span style="display:inline-block; width:12px; height:12px; border-radius:2px; background:#9CA3AF;"></span>
              VILAF LEGAL · KPMG ADVISORY
            </div>
          </div>
        </div>

        <!-- 2. MAIN BODY (LEFT 38% BRAND & THEME | RIGHT 62% 6 KEYNOTE SPEAKERS GRID) -->
        <div style="display:flex; flex:1; margin-top:22px; margin-bottom:18px; gap:48px;">
          <!-- Left Column (Brand + Theme + Metadata) -->
          <div style="flex:0 0 540px; display:flex; flex-direction:column; justify-content:flex-start;">
            <!-- Brand Mark / Main Event Name (Sleek Geometric Style like NEXT Forum) -->
            <div style="display:flex; align-items:baseline; gap:16px;">
              <div style="font-family:'Space Grotesk', sans-serif; font-size:78px; font-weight:800; letter-spacing:0.18em; color:#0A1628; line-height:0.95;">
                VMAA
              </div>
              <div style="font-family:'Space Grotesk', sans-serif; font-size:32px; font-weight:600; letter-spacing:0.32em; color:#6B2D9B; text-transform:uppercase;">
                FORUM 2026
              </div>
            </div>

            <!-- Subtitle Title -->
            <div style="font-family:'Space Grotesk', sans-serif; font-size:25px; font-weight:700; letter-spacing:0.22em; color:#1E3A8A; margin-top:6px; margin-bottom:20px; text-transform:uppercase;">
              DIỄN ĐÀN M&amp;A MIỀN TRUNG
            </div>

            <!-- Theme Slogan (Bold Italic Accent like "TĂNG TỐC GIỮA BIẾN ĐỘNG: KHÁT VỌNG HAY THỰC LỰC") -->
            <div style="margin-bottom:26px; padding:18px 24px; background:linear-gradient(135deg, rgba(155,77,255,0.08) 0%, rgba(36,91,255,0.06) 100%); border-left:4px solid #6B2D9B; border-radius:0 12px 12px 0;">
              <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:24px; font-weight:800; color:#0A1628; line-height:1.25; letter-spacing:-0.01em;">
                KIẾN TRÚC GIÁ TRỊ:
              </div>
              <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:24px; font-weight:800; font-style:italic; color:#6B2D9B; line-height:1.25; letter-spacing:0.02em;">
                BẤT ĐỘNG SẢN × CÔNG NGHỆ
              </div>
              <div style="font-family:'JetBrains Mono', monospace; font-size:11.5px; font-weight:600; color:#3B82F6; letter-spacing:0.14em; text-transform:uppercase; margin-top:8px;">
                ARCHITECTURE OF VALUE · STRATEGIC M&amp;A CONVERGENCE
              </div>
            </div>

            <!-- Date & Venue Details (Clean tabular metadata like Next Forum) -->
            <div style="display:flex; flex-direction:column; gap:12px; margin-bottom:20px; max-width:440px;">
              <div style="display:flex; align-items:center; gap:20px;">
                <div style="font-family:'Space Grotesk', sans-serif; font-size:12px; font-weight:700; letter-spacing:0.1em; color:#6B7280; width:90px; text-transform:uppercase;">
                  Diễn ra vào
                </div>
                <div>
                  <div style="font-family:'Space Grotesk', sans-serif; font-size:19px; font-weight:700; color:#0A1628;">
                    Chủ Nhật · 13.12.2026
                  </div>
                  <div style="font-family:'JetBrains Mono', monospace; font-size:13px; font-weight:600; color:#6B2D9B;">
                    13h30 – 17h30 (VIP Reception &amp; Deal Room)
                  </div>
                </div>
              </div>

              <div style="display:flex; align-items:center; gap:20px;">
                <div style="font-family:'Space Grotesk', sans-serif; font-size:12px; font-weight:700; letter-spacing:0.1em; color:#6B7280; width:90px; text-transform:uppercase;">
                  Địa điểm
                </div>
                <div>
                  <div style="font-family:'Space Grotesk', sans-serif; font-size:19px; font-weight:700; color:#0A1628;">
                    Grand Ballroom · Ariyana Convention Centre
                  </div>
                  <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:13px; font-weight:500; color:#4B5563;">
                    Võ Nguyên Giáp, Ngũ Hành Sơn, TP. Đà Nẵng
                  </div>
                </div>
              </div>
            </div>

            <!-- 3D Hero Sculpture (Flows safely inside left column without touching footer) -->
            <div style="width:480px; height:185px; border-radius:14px; overflow:hidden; box-shadow:0 12px 32px rgba(107,45,155,0.22); border:1.5px solid rgba(155,77,255,0.38); margin-top:2px;">
              <img src="{u_hero_plate}" alt="3D Architecture of Value Hero" style="width:100%; height:100%; object-fit:cover; filter:brightness(1.06) contrast(1.1);"/>
            </div>
          </div>

          <!-- Right Section: 6 Keynote Speakers / VIP Leaders in 2x3 Grid -->
          <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); grid-template-rows:repeat(2, 1fr); gap:26px 20px;">
              {speakers_html}
            </div>
          </div>
        </div>

        <!-- 3. BOTTOM FOOTER PARTNERS (Directly matching Next Forum Footer) -->
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1.5px solid rgba(209,213,219,0.7);">
          <div>
            <div class="sponsor-title">ĐƠN VỊ HỖ TRỢ &amp; ĐỒNG HÀNH</div>
            <div style="display:flex; gap:16px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:700; font-size:12.5px; color:#374151;">
              <span>HIỆP HỘI DN ĐÀ NẴNG (DPA)</span>
              <span>·</span>
              <span>CLB BẤT ĐỘNG SẢN MIỀN TRUNG</span>
            </div>
          </div>
          <div>
            <div class="sponsor-title" style="text-align:center;">ĐỐI TÁC QUỐC TẾ &amp; QUỸ ĐẦU TƯ</div>
            <div style="display:flex; gap:18px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:700; font-size:12.5px; color:#2563EB;">
              <span>ALIBABA GLOBAL INITIATIVES</span>
              <span>·</span>
              <span>SINGAPORE PE COUNCIL</span>
              <span>·</span>
              <span>DEALROOM ASIA</span>
            </div>
          </div>
          <div>
            <div class="sponsor-title" style="text-align:right;">ĐỐI TÁC TRUYỀN THÔNG</div>
            <div style="display:flex; gap:14px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:800; font-size:13px; color:#1F2937;">
              <span style="color:#DC2626;">VCCORP</span>
              <span style="color:#2563EB;">CAFEF</span>
              <span style="color:#7C3AED;">FORBES VIETNAM</span>
              <span style="color:#059669;">VIETSUCCESS</span>
            </div>
          </div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 2. OPTION B: LUMINOUS OBSIDIAN & ELECTRIC PURPLE (HIGH-IMPACT VIP STAGE)
# =========================================================================
def build_html_dark():
    speakers_html = ""
    for i, sp in enumerate(SPEAKERS):
        avatar = generate_avatar_svg(i, is_dark=True)
        speakers_html += f"""
        <div style="display:flex; flex-direction:column; align-items:center; text-align:center;">
          <div style="margin-bottom:14px; position:relative;">
            {avatar}
          </div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:17.5px; font-weight:700; color:#FFFFFF; letter-spacing:0.04em; text-transform:uppercase; margin-bottom:5px; text-shadow:0 0 15px rgba(192,132,252,0.4);">
            {sp['name']}
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:12.5px; font-weight:600; color:#E9D5FF; line-height:1.35; max-width:260px; margin-bottom:3px;">
            {sp['role']}
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:11.5px; font-weight:500; color:#93C5FD; line-height:1.3; max-width:250px;">
            {sp['sub']}
          </div>
        </div>
        """

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: #070D20; font-family: 'Plus Jakarta Sans', sans-serif; color: #FFFFFF; position: relative;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_hero_plate}');
        background-size: cover; background-position: 72% center;
        filter: brightness(1.15) contrast(1.1) saturate(1.22);
      }}
      .aurora-layer {{
        position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
        background:
          radial-gradient(900px 750px at 78% 45%, rgba(155,77,255,0.42) 0%, rgba(36,91,255,0.28) 50%, transparent 80%),
          radial-gradient(800px 600px at 20% 60%, rgba(107,45,155,0.45) 0%, transparent 75%),
          radial-gradient(600px 450px at 50% 15%, rgba(233,213,255,0.25) 0%, transparent 70%);
      }}
      .shade-layer {{
        position: absolute; inset: 0; pointer-events: none;
        background:
          linear-gradient(90deg, rgba(7,11,28,0.94) 0%, rgba(7,11,28,0.88) 42%, rgba(7,11,28,0.65) 68%, rgba(7,11,28,0.85) 100%),
          linear-gradient(180deg, rgba(7,11,28,0.85) 0%, transparent 25%, transparent 75%, rgba(7,11,28,0.92) 100%);
      }}
      .container {{
        position: absolute; inset: 0; padding: 36px 64px 30px 64px;
        display: flex; flex-direction: column; justify-content: space-between; z-index: 10;
      }}
      .sponsor-title {{
        font-family: 'Space Grotesk', sans-serif; font-size: 10px; font-weight: 700;
        letter-spacing: 0.16em; text-transform: uppercase; color: #C084FC; margin-bottom: 7px;
      }}
      .sponsor-badge {{
        font-family: 'Space Grotesk', sans-serif; font-weight: 700; font-size: 14.5px;
        display: flex; align-items: center; gap: 8px; color: #FFFFFF;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="aurora-layer"></div>
      <div class="shade-layer"></div>

      <div class="container">
        <!-- 1. TOP SPONSOR & ORGANIZER BAR -->
        <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:18px; border-bottom:1.5px solid rgba(233,213,255,0.25);">
          <div>
            <div class="sponsor-title">NHÀ TÀI TRỢ ĐỒNG HÀNH</div>
            <div class="sponsor-badge" style="color:#60A5FA;">
              <span style="display:inline-block; width:12px; height:12px; border-radius:50%; background:#60A5FA; box-shadow:0 0 10px #60A5FA;"></span>
              CENTRAL CAPITAL GROUP
            </div>
          </div>
          <div>
            <div class="sponsor-title" style="color:#FDE047;">NHÀ TÀI TRỢ VÀNG</div>
            <div class="sponsor-badge" style="color:#FDE047; font-size:16px;">
              <span style="display:inline-block; width:14px; height:14px; border-radius:3px; background:linear-gradient(135deg, #FDE047, #EAB308); box-shadow:0 0 12px #FDE047;"></span>
              SUNSHINE HERITAGE HOLDINGS
            </div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:center;">
            <div class="sponsor-title" style="color:#F3E8FF;">ĐƠN VỊ TỔ CHỨC CHỦ TRÌ</div>
            <div style="display:inline-flex; align-items:center; padding:6px 16px; background:rgba(11,18,44,0.85); border:1.5px solid #C084FC; border-radius:8px; box-shadow:0 8px 24px rgba(155,77,255,0.4);">
              <img src="{u_logo_white}" alt="VMAA Logo" style="height:40px; width:auto; filter:drop-shadow(0 2px 8px #C084FC);"/>
            </div>
          </div>
          <div>
            <div class="sponsor-title" style="color:#FCA5A5;">ĐỐI TÁC HỌC THUẬT &amp; VIỆN NGHIÊN CỨU</div>
            <div class="sponsor-badge" style="color:#F87171;">
              <span style="display:inline-block; width:12px; height:12px; border-radius:50%; background:#F87171; box-shadow:0 0 10px #F87171;"></span>
              ĐẠI HỌC KINH TẾ ĐÀ NẴNG · DUE
            </div>
          </div>
          <div>
            <div class="sponsor-title">NHÀ TÀI TRỢ BẠC</div>
            <div class="sponsor-badge" style="color:#E2E8F0;">
              <span style="display:inline-block; width:12px; height:12px; border-radius:2px; background:#CBD5E1;"></span>
              VILAF LEGAL · KPMG ADVISORY
            </div>
          </div>
        </div>

        <!-- 2. MAIN BODY (LEFT 38% BRAND & THEME | RIGHT 62% 6 KEYNOTE SPEAKERS GRID) -->
        <div style="display:flex; flex:1; margin-top:22px; margin-bottom:18px; gap:48px;">
          <!-- Left Column (Brand + Theme + Metadata) -->
          <div style="flex:0 0 540px; display:flex; flex-direction:column; justify-content:center;">
            <!-- Brand Mark / Main Event Name -->
            <div style="display:flex; align-items:baseline; gap:16px;">
              <div style="font-family:'Space Grotesk', sans-serif; font-size:78px; font-weight:800; letter-spacing:0.18em; color:#FFFFFF; line-height:0.95; text-shadow:0 0 35px rgba(155,77,255,0.7);">
                VMAA
              </div>
              <div style="font-family:'Space Grotesk', sans-serif; font-size:32px; font-weight:600; letter-spacing:0.32em; color:#C084FC; text-transform:uppercase;">
                FORUM 2026
              </div>
            </div>

            <!-- Subtitle Title -->
            <div style="font-family:'Space Grotesk', sans-serif; font-size:25px; font-weight:700; letter-spacing:0.22em; color:#93C5FD; margin-top:6px; margin-bottom:20px; text-transform:uppercase;">
              DIỄN ĐÀN M&amp;A MIỀN TRUNG
            </div>

            <!-- Theme Slogan -->
            <div style="margin-bottom:26px; padding:18px 24px; background:linear-gradient(135deg, rgba(155,77,255,0.22) 0%, rgba(36,91,255,0.18) 100%); border-left:4px solid #C084FC; border-radius:0 12px 12px 0; border:1px solid rgba(233,213,255,0.3); border-left-width:4px;">
              <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:24px; font-weight:800; color:#FFFFFF; line-height:1.25; letter-spacing:-0.01em;">
                KIẾN TRÚC GIÁ TRỊ:
              </div>
              <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:24px; font-weight:800; font-style:italic; color:#FDE047; line-height:1.25; letter-spacing:0.02em; text-shadow:0 0 20px rgba(253,224,71,0.5);">
                BẤT ĐỘNG SẢN × CÔNG NGHỆ
              </div>
              <div style="font-family:'JetBrains Mono', monospace; font-size:11.5px; font-weight:600; color:#93C5FD; letter-spacing:0.14em; text-transform:uppercase; margin-top:8px;">
                ARCHITECTURE OF VALUE · STRATEGIC M&amp;A CONVERGENCE
              </div>
            </div>

            <!-- Date & Venue Details -->
            <div style="display:flex; flex-direction:column; gap:14px; margin-bottom:20px; max-width:460px;">
              <div style="display:flex; align-items:center; gap:20px;">
                <div style="font-family:'Space Grotesk', sans-serif; font-size:12px; font-weight:700; letter-spacing:0.1em; color:#C084FC; width:90px; text-transform:uppercase;">
                  Diễn ra vào
                </div>
                <div>
                  <div style="font-family:'Space Grotesk', sans-serif; font-size:19px; font-weight:700; color:#FFFFFF;">
                    Chủ Nhật · 13.12.2026
                  </div>
                  <div style="font-family:'JetBrains Mono', monospace; font-size:13px; font-weight:600; color:#F3E8FF;">
                    13h30 – 17h30 (VIP Reception &amp; Deal Room)
                  </div>
                </div>
              </div>

              <div style="display:flex; align-items:center; gap:20px;">
                <div style="font-family:'Space Grotesk', sans-serif; font-size:12px; font-weight:700; letter-spacing:0.1em; color:#C084FC; width:90px; text-transform:uppercase;">
                  Địa điểm
                </div>
                <div>
                  <div style="font-family:'Space Grotesk', sans-serif; font-size:19px; font-weight:700; color:#FFFFFF;">
                    Grand Ballroom · Ariyana Convention Centre
                  </div>
                  <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:13px; font-weight:500; color:#CBD5E1;">
                    Võ Nguyên Giáp, Ngũ Hành Sơn, TP. Đà Nẵng
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Section: 6 Keynote Speakers / VIP Leaders in 2x3 Grid -->
          <div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
            <div style="display:grid; grid-template-columns:repeat(3, 1fr); grid-template-rows:repeat(2, 1fr); gap:26px 20px;">
              {speakers_html}
            </div>
          </div>
        </div>

        <!-- 3. BOTTOM FOOTER PARTNERS -->
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1.5px solid rgba(233,213,255,0.25);">
          <div>
            <div class="sponsor-title">ĐƠN VỊ HỖ TRỢ &amp; ĐỒNG HÀNH</div>
            <div style="display:flex; gap:16px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:700; font-size:12.5px; color:#E2E8F0;">
              <span>HIỆP HỘI DN ĐÀ NẴNG (DPA)</span>
              <span>·</span>
              <span>CLB BẤT ĐỘNG SẢN MIỀN TRUNG</span>
            </div>
          </div>
          <div>
            <div class="sponsor-title" style="text-align:center;">ĐỐI TÁC QUỐC TẾ &amp; QUỸ ĐẦU TƯ</div>
            <div style="display:flex; gap:18px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:700; font-size:12.5px; color:#60A5FA;">
              <span>ALIBABA GLOBAL INITIATIVES</span>
              <span>·</span>
              <span>SINGAPORE PE COUNCIL</span>
              <span>·</span>
              <span>DEALROOM ASIA</span>
            </div>
          </div>
          <div>
            <div class="sponsor-title" style="text-align:right;">ĐỐI TÁC TRUYỀN THÔNG</div>
            <div style="display:flex; gap:14px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:800; font-size:13px; color:#FFFFFF;">
              <span style="color:#F87171;">VCCORP</span>
              <span style="color:#60A5FA;">CAFEF</span>
              <span style="color:#C084FC;">FORBES VIETNAM</span>
              <span style="color:#34D499;">VIETSUCCESS</span>
            </div>
          </div>
        </div>
      </div>
    </body></html>"""


def render_posters():
    html_highkey = build_html_highkey()
    html_dark = build_html_dark()

    out_highkey_html = EXPORTS_DIR / "09_VMAA_Next_Forum_Format_HighKey.html"
    out_highkey_png = EXPORTS_DIR / "09_VMAA_Next_Forum_Format_HighKey_4K.png"
    out_dark_html = EXPORTS_DIR / "09_VMAA_Next_Forum_Format_ObsidianPurple.html"
    out_dark_png = EXPORTS_DIR / "09_VMAA_Next_Forum_Format_ObsidianPurple_4K.png"

    out_highkey_html.write_text(html_highkey, encoding="utf-8")
    out_dark_html.write_text(html_dark, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Render at 2x scale for 3840x2160 4K UHD
        page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)

        # 1. High Key
        page.goto(out_highkey_html.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(out_highkey_png), type="png")
        print(f"Rendered {out_highkey_png.name} (3840x2160 4K UHD)")
        shutil.copy2(out_highkey_png, BRAIN_DIR / out_highkey_png.name)

        # 2. Obsidian Purple
        page.goto(out_dark_html.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(out_dark_png), type="png")
        print(f"Rendered {out_dark_png.name} (3840x2160 4K UHD)")
        shutil.copy2(out_dark_png, BRAIN_DIR / out_dark_png.name)

        browser.close()


if __name__ == "__main__":
    render_posters()
