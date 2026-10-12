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
u_wordmark_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_wordmark_white_transparent.png")

# Comprehensive Google Fonts with complete Vietnamese character set support
FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:ital,wght@0,600;0,700;1,600;1,700&family=JetBrains+Mono:wght@500;600;700&family=Outfit:wght@300;400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,600;1,700;1,800&family=Space+Grotesk:ital,wght@0,500;0,600;0,700;1,600;1,700&family=Syne:wght@700;800&family=Unbounded:wght@700;800;900&display=swap" rel="stylesheet">
"""


# Top sponsor row HTML (Clean, unboxed, pure logos and crisp categories like Next Forum)
def get_top_sponsors_html():
    return f"""
    <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:20px; border-bottom:1px solid rgba(233,213,255,0.22); width:100%;">
      <!-- 1. Nhà tài trợ Đồng hành -->
      <div>
        <div style="font-family:'Space Grotesk', sans-serif; font-size:10px; font-weight:700; letter-spacing:0.18em; text-transform:uppercase; color:#93C5FD; margin-bottom:6px;">
          NHÀ TÀI TRỢ ĐỒNG HÀNH
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Space Grotesk', sans-serif; font-size:14px; font-weight:700; color:#FFFFFF;">
          <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#38BDF8; box-shadow:0 0 10px #38BDF8;"></span>
          CENTRAL CAPITAL
        </div>
      </div>

      <!-- 2. Nhà tài trợ Vàng -->
      <div>
        <div style="font-family:'Space Grotesk', sans-serif; font-size:10px; font-weight:700; letter-spacing:0.18em; text-transform:uppercase; color:#FDE047; margin-bottom:6px;">
          NHÀ TÀI TRỢ VÀNG
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Space Grotesk', sans-serif; font-size:15px; font-weight:800; color:#FDE047; text-shadow:0 0 12px rgba(253,224,71,0.4);">
          <span style="display:inline-block; width:12px; height:12px; border-radius:3px; background:linear-gradient(135deg, #FDE047, #EAB308);"></span>
          GELEX GROUP
        </div>
      </div>

      <!-- 3. Đơn vị tổ chức chủ trì (Official VMAA Logo - Pure, No arbitrary frame/box) -->
      <div style="display:flex; flex-direction:column; align-items:center;">
        <div style="font-family:'Space Grotesk', sans-serif; font-size:10px; font-weight:700; letter-spacing:0.2em; text-transform:uppercase; color:#E9D5FF; margin-bottom:6px;">
          ĐƠN VỊ TỔ CHỨC CHỦ TRÌ
        </div>
        <img src="{u_logo_white}" alt="VMAA Logo" style="height:44px; width:auto; display:block; filter:drop-shadow(0 4px 14px rgba(155,77,255,0.4));"/>
      </div>

      <!-- 4. Đối tác Học thuật & Nghiên cứu -->
      <div>
        <div style="font-family:'Space Grotesk', sans-serif; font-size:10px; font-weight:700; letter-spacing:0.18em; text-transform:uppercase; color:#FCA5A5; margin-bottom:6px;">
          ĐỐI TÁC HỌC THUẬT &amp; VIỆN
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Space Grotesk', sans-serif; font-size:14px; font-weight:700; color:#FFFFFF;">
          <span style="display:inline-block; width:10px; height:10px; border-radius:50%; background:#F87171; box-shadow:0 0 10px #F87171;"></span>
          ĐH KINH TẾ ĐÀ NẴNG · DUE
        </div>
      </div>

      <!-- 5. Nhà tài trợ Bạc -->
      <div>
        <div style="font-family:'Space Grotesk', sans-serif; font-size:10px; font-weight:700; letter-spacing:0.18em; text-transform:uppercase; color:#C084FC; margin-bottom:6px;">
          NHÀ TÀI TRỢ BẠC
        </div>
        <div style="display:flex; align-items:center; gap:8px; font-family:'Space Grotesk', sans-serif; font-size:14px; font-weight:700; color:#E2E8F0;">
          <span style="display:inline-block; width:10px; height:10px; border-radius:2px; background:#CBD5E1;"></span>
          VILAF LEGAL · KPMG ADVISORY
        </div>
      </div>
    </div>
    """


# Bottom metadata & partner footer HTML (No pill boxes, clear high-contrast typography)
def get_bottom_section_html():
    return f"""
    <!-- Metadata: Date / Time / Venue (Tabular, High Contrast, Large Readable Text) -->
    <div style="display:flex; justify-content:space-between; align-items:flex-end; width:100%; padding-top:22px; border-top:1px solid rgba(233,213,255,0.22);">
      <!-- Left: Date & Time & Venue -->
      <div style="display:flex; gap:44px; align-items:flex-start;">
        <div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:11.5px; font-weight:700; color:#C084FC; text-transform:uppercase; letter-spacing:0.14em; margin-bottom:5px;">
            Thời gian diễn ra
          </div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:24px; font-weight:800; color:#FFFFFF; letter-spacing:0.02em;">
            Chủ Nhật · 13.12.2026
          </div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:13px; font-weight:600; color:#93C5FD; margin-top:3px;">
            13:30 – 17:30 (Diễn đàn) · 18:00 – 21:00 (Gala Dinner)
          </div>
        </div>

        <div style="width:1.5px; height:54px; background:rgba(192,132,252,0.35); align-self:center;"></div>

        <div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:11.5px; font-weight:700; color:#C084FC; text-transform:uppercase; letter-spacing:0.14em; margin-bottom:5px;">
            Địa điểm tổ chức
          </div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:24px; font-weight:800; color:#FFFFFF; letter-spacing:0.02em;">
            Đà Nẵng, Việt Nam
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:13.5px; font-weight:600; color:#CBD5E1; margin-top:3px;">
            Furama Resort / Ariyana Convention Centre
          </div>
        </div>
      </div>

      <!-- Right: Supporting & Media Partners List (Like Next Forum Footer) -->
      <div style="display:flex; gap:36px; align-items:flex-end;">
        <div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:10px; font-weight:700; color:#93C5FD; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:6px; text-align:right;">
            ĐƠN VỊ HỖ TRỢ &amp; QUỸ ĐẦU TƯ
          </div>
          <div style="display:flex; gap:16px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:700; font-size:13px; color:#E2E8F0;">
            <span>HIỆP HỘI DN ĐÀ NẴNG</span>
            <span>·</span>
            <span>CLB BẤT ĐỘNG SẢN MIỀN TRUNG</span>
            <span>·</span>
            <span style="color:#60A5FA;">MEKONG CAPITAL</span>
          </div>
        </div>

        <div style="width:1.5px; height:46px; background:rgba(233,213,255,0.22); align-self:center;"></div>

        <div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:10px; font-weight:700; color:#C084FC; letter-spacing:0.16em; text-transform:uppercase; margin-bottom:6px; text-align:right;">
            ĐỐI TÁC TRUYỀN THÔNG
          </div>
          <div style="display:flex; gap:14px; align-items:center; font-family:'Space Grotesk', sans-serif; font-weight:800; font-size:13.5px;">
            <span style="color:#F87171;">VCCORP</span>
            <span style="color:#60A5FA;">CAFEF</span>
            <span style="color:#C084FC;">FORBES VIETNAM</span>
            <span style="color:#34D399;">VIETSUCCESS</span>
          </div>
        </div>
      </div>
    </div>
    """


# =========================================================================
# 6 TYPOGRAPHY OPTIONS BUILDER (Italic, Non-Italic, Futuristic, Intelligent)
# =========================================================================

TYPO_CONFIGS = [
    {
        "id": "TYPO_01",
        "name": "Option 01: Next Forum Hybrid (Bold Sans + Dynamic Italic Slogan)",
        "desc": "Lấy cảm hứng trực tiếp từ Next Forum: Tiêu đề hình học khúc chiết kết hợp Slogan in nghiêng Dynamic Italic màu tím-vàng rực rỡ.",
        "html_title": """
        <!-- Pre-title label (No pill container, clean tracking) -->
        <div style="font-family:'JetBrains Mono', monospace; font-size:13px; font-weight:600; letter-spacing:0.28em; color:#C084FC; text-transform:uppercase; margin-bottom:12px;">
          GLOBAL SUMMIT · CENTRAL VIETNAM 2026
        </div>

        <!-- Main Title (Razor-sharp, correct Vietnamese diacritics MIỀN TRUNG) -->
        <div style="font-family:'Space Grotesk', sans-serif; font-size:38px; font-weight:700; letter-spacing:0.26em; color:#FFFFFF; text-transform:uppercase; line-height:1.1;">
          DIỄN ĐÀN
        </div>
        <div style="font-family:'Space Grotesk', sans-serif; font-size:94px; font-weight:800; letter-spacing:0.04em; color:#FFFFFF; line-height:0.92; margin-top:6px; text-shadow:0 0 35px rgba(155,77,255,0.65);">
          M&amp;A 2026
        </div>
        <div style="font-family:'Space Grotesk', sans-serif; font-size:74px; font-weight:800; letter-spacing:0.08em; color:#C084FC; line-height:0.98; margin-top:4px; text-shadow:0 0 30px rgba(192,132,252,0.5);">
          MIỀN TRUNG
        </div>

        <!-- Theme Headline (Dynamic Bold Italic Accent like Next Forum) -->
        <div style="margin-top:22px;">
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:26px; font-weight:800; color:#FFFFFF; line-height:1.2;">
            KIẾN TRÚC GIÁ TRỊ:
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:26px; font-weight:800; font-style:italic; color:#FDE047; line-height:1.2; text-shadow:0 0 20px rgba(253,224,71,0.45);">
            BẤT ĐỘNG SẢN × CÔNG NGHỆ
          </div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:13px; font-weight:600; color:#93C5FD; letter-spacing:0.18em; text-transform:uppercase; margin-top:8px;">
            REAL ESTATE — TECHNOLOGY · ARCHITECTURE OF VALUE
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_02",
        "name": "Option 02: World Economic Forum (Monumental Geometric · Non-Italic)",
        "desc": "Phong cách Diễn đàn Kinh tế Thế giới: Cân bằng tuyệt đối, cấu trúc chữ đứng Monumental vững chãi, uy quyền và không in nghiêng.",
        "html_title": """
        <div style="font-family:'JetBrains Mono', monospace; font-size:13px; font-weight:600; letter-spacing:0.32em; color:#93C5FD; text-transform:uppercase; margin-bottom:12px;">
          ARCHITECTURE OF VALUE // SUMMIT
        </div>

        <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:32px; font-weight:700; letter-spacing:0.32em; color:#E9D5FF; text-transform:uppercase; line-height:1.1;">
          DIỄN ĐÀN M&amp;A
        </div>
        <div style="display:flex; align-items:baseline; gap:16px; margin-top:4px;">
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:86px; font-weight:800; letter-spacing:0.02em; color:#FFFFFF; line-height:0.94; text-shadow:0 0 35px rgba(255,255,255,0.4);">
            2026
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:70px; font-weight:800; letter-spacing:0.06em; color:#C084FC; line-height:0.94;">
            MIỀN TRUNG
          </div>
        </div>

        <div style="margin-top:24px; padding-left:16px; border-left:3.5px solid #245BFF;">
          <div style="font-family:'Space Grotesk', sans-serif; font-size:24px; font-weight:700; color:#FFFFFF; letter-spacing:0.04em;">
            KIẾN TRÚC GIÁ TRỊ: BẤT ĐỘNG SẢN &amp; CÔNG NGHỆ
          </div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:12.5px; font-weight:600; color:#60A5FA; letter-spacing:0.18em; text-transform:uppercase; margin-top:6px;">
            CAPITAL FLOWS · PROPTECH · STRATEGIC DEAL ROOM
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_03",
        "name": "Option 03: Milken Global Modernist (Extended Futuristic · Stretched 2026)",
        "desc": "Chuẩn mực viện nghiên cứu kinh tế quốc tế Milken: Chữ dàn ngang hiện đại (Extended Sans), số 2026 dạng nét đôi thanh lịch.",
        "html_title": """
        <div style="font-family:'Space Grotesk', sans-serif; font-size:13px; font-weight:700; letter-spacing:0.3em; color:#C084FC; text-transform:uppercase; margin-bottom:12px;">
          THE CENTRAL VIETNAM M&amp;A CONVERGENCE
        </div>

        <div style="font-family:'Unbounded', sans-serif; font-size:42px; font-weight:800; letter-spacing:0.06em; color:#FFFFFF; line-height:1.05;">
          DIỄN ĐÀN M&amp;A
        </div>
        <div style="display:flex; align-items:center; gap:20px; margin-top:8px;">
          <div style="font-family:'Unbounded', sans-serif; font-size:62px; font-weight:800; color:#A855F7; letter-spacing:0.04em; text-shadow:0 0 35px rgba(168,85,247,0.6);">
            MIỀN TRUNG
          </div>
          <div style="font-family:'Outfit', sans-serif; font-size:62px; font-weight:300; color:#FFFFFF; letter-spacing:0.18em; opacity:0.85;">
            2026
          </div>
        </div>

        <div style="margin-top:24px;">
          <div style="font-family:'Outfit', sans-serif; font-size:25px; font-weight:700; color:#FFFFFF; letter-spacing:0.03em;">
            KIẾN TRÚC GIÁ TRỊ: <span style="color:#60A5FA; font-weight:800;">BẤT ĐỘNG SẢN</span> × <span style="color:#C084FC; font-weight:800;">CÔNG NGHỆ</span>
          </div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:12px; font-weight:500; color:#CBD5E1; letter-spacing:0.16em; margin-top:6px;">
            ORGANIZED BY VMAA · HIGH-LEVEL INVESTMENT PLATFORM
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_04",
        "name": "Option 04: GITEX Tech Kinetic (High-Tech Italic Speed · Cutting-Edge)",
        "desc": "Phong cách GITEX Tech Summit: Font góc cạnh thể thao công nghệ cao (Kinetic Slanted), toàn bộ tiêu đề nghiêng tạo cảm giác tăng tốc bứt phá.",
        "html_title": """
        <div style="font-family:'Chakra Petch', sans-serif; font-size:14px; font-weight:700; letter-spacing:0.25em; color:#38BDF8; text-transform:uppercase; margin-bottom:10px;">
          // ANNUAL STRATEGIC FORUM //
        </div>

        <div style="font-family:'Chakra Petch', sans-serif; font-size:36px; font-weight:700; font-style:italic; letter-spacing:0.16em; color:#FFFFFF; text-transform:uppercase;">
          DIỄN ĐÀN
        </div>
        <div style="font-family:'Chakra Petch', sans-serif; font-size:92px; font-weight:700; font-style:italic; letter-spacing:0.04em; color:#FFFFFF; line-height:0.92; text-shadow:0 0 40px rgba(56,189,248,0.5);">
          M&amp;A <span style="color:#A855F7;">2026</span>
        </div>
        <div style="font-family:'Chakra Petch', sans-serif; font-size:68px; font-weight:700; font-style:italic; letter-spacing:0.08em; color:#38BDF8; line-height:0.96; margin-top:4px;">
          MIỀN TRUNG
        </div>

        <div style="margin-top:22px;">
          <div style="font-family:'Chakra Petch', sans-serif; font-size:24px; font-weight:700; font-style:italic; color:#FDE047;">
            TĂNG TỐC GIÁ TRỊ: BẤT ĐỘNG SẢN × CÔNG NGHỆ
          </div>
          <div style="font-family:'JetBrains Mono', monospace; font-size:12px; font-weight:600; color:#E9D5FF; letter-spacing:0.2em; text-transform:uppercase; margin-top:6px;">
            TECH-DRIVEN ASSETS · M&amp;A INNOVATION
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_05",
        "name": "Option 05: Sovereign Capital & Private Equity (Bilingual Dignified · Elegant)",
        "desc": "Phong cách hội nghị quỹ đầu tư & định chế tài chính thượng tầng: Song ngữ Anh-Việt tinh tế, khoảng cách chữ thoáng, sang trọng vượt thời gian.",
        "html_title": """
        <div style="font-family:'Space Grotesk', sans-serif; font-size:12.5px; font-weight:700; letter-spacing:0.35em; color:#C084FC; text-transform:uppercase; margin-bottom:14px;">
          VIETNAM M&amp;A ASSOCIATION · CENTRAL CHAPTER
        </div>

        <div style="font-family:'Syne', sans-serif; font-size:78px; font-weight:800; letter-spacing:0.02em; color:#FFFFFF; line-height:0.94;">
          M&amp;A 2026
        </div>
        <div style="font-family:'Space Grotesk', sans-serif; font-size:36px; font-weight:700; letter-spacing:0.28em; color:#93C5FD; text-transform:uppercase; margin-top:8px;">
          DIỄN ĐÀN MIỀN TRUNG
        </div>

        <div style="margin-top:24px;">
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:23px; font-weight:700; color:#FFFFFF; line-height:1.3;">
            KIẾN TRÚC GIÁ TRỊ: <span style="color:#C084FC; font-weight:800;">BẤT ĐỘNG SẢN — CÔNG NGHỆ</span>
          </div>
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:15px; font-weight:500; font-style:italic; color:#94A3B8; margin-top:4px;">
            Architecture of Value: Real Estate &amp; Technology Convergence
          </div>
        </div>
        """
    },
    {
        "id": "TYPO_06",
        "name": "Option 06: Apple Keynote Ultra-Clean (Pure Minimalist · Maximum Impact)",
        "desc": "Phong cách tối giản toàn cầu: Bỏ hết mọi chi tiết thừa, tập trung toàn bộ trọng tâm thị giác vào khối chữ trắng băng và dải sáng tím lan tỏa.",
        "html_title": """
        <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:14px; font-weight:700; letter-spacing:0.3em; color:#E9D5FF; text-transform:uppercase; margin-bottom:12px;">
          HIỆP HỘI MUA BÁN &amp; SÁP NHẬP DOANH NGHIỆP VIỆT NAM
        </div>

        <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:92px; font-weight:800; letter-spacing:-0.02em; color:#FFFFFF; line-height:0.92; text-shadow:0 0 35px rgba(255,255,255,0.45);">
          M&amp;A 2026
        </div>
        <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:54px; font-weight:800; letter-spacing:0.04em; color:#A855F7; line-height:1.0; margin-top:6px; text-shadow:0 0 30px rgba(168,85,247,0.6);">
          DIỄN ĐÀN MIỀN TRUNG
        </div>

        <div style="margin-top:22px;">
          <div style="font-family:'Plus Jakarta Sans', sans-serif; font-size:25px; font-weight:700; color:#FFFFFF;">
            Kiến trúc Giá trị: <span style="color:#60A5FA; font-weight:800;">Bất động sản</span> &amp; <span style="color:#FDE047; font-weight:800;">Công nghệ</span>
          </div>
          <div style="font-family:'Space Grotesk', sans-serif; font-size:13px; font-weight:600; color:#CBD5E1; letter-spacing:0.16em; text-transform:uppercase; margin-top:8px;">
            1,500+ LEADERS &amp; INVESTORS · SINGAPORE WEF SCALE
          </div>
        </div>
        """
    }
]


def build_full_keyvisual_html(config: dict) -> str:
    top_sponsors = get_top_sponsors_html()
    bottom_section = get_bottom_section_html()
    title_html = config["html_title"]

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: #070D20; font-family: 'Plus Jakarta Sans', sans-serif; color: #FFFFFF; position: relative;
      }}
      .plate-bg {{
        position: absolute; inset: 0;
        background-image: url('{u_hero_plate}');
        background-size: cover; background-position: 70% center;
        filter: brightness(1.18) contrast(1.12) saturate(1.22);
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
          linear-gradient(90deg, rgba(7,11,28,0.92) 0%, rgba(7,11,28,0.85) 44%, rgba(7,11,28,0.45) 70%, rgba(7,11,28,0.75) 100%),
          linear-gradient(180deg, rgba(7,11,28,0.88) 0%, transparent 22%, transparent 75%, rgba(7,11,28,0.94) 100%);
      }}
      .shell {{
        position: absolute; inset: 0; padding: 34px 64px 30px 64px;
        display: flex; flex-direction: column; justify-content: space-between; z-index: 10;
      }}
    </style></head><body>
      <div class="plate-bg"></div>
      <div class="aurora-layer"></div>
      <div class="shade-layer"></div>

      <div class="shell">
        <!-- 1. TOP SPONSOR & ORGANIZER ROW -->
        {top_sponsors}

        <!-- 2. MAIN BODY (LEFT HERO TITLE · RIGHT PRISM ILLUMINATION) -->
        <div style="display:flex; flex:1; align-items:center; margin-top:20px; margin-bottom:20px;">
          <div style="flex:0 0 680px; display:flex; flex-direction:column; justify-content:center;">
            {title_html}
          </div>
        </div>

        <!-- 3. BOTTOM METADATA & PARTNERS -->
        {bottom_section}
      </div>
    </body></html>"""


def build_comparison_matrix_html():
    cards_html = ""
    for cfg in TYPO_CONFIGS:
        cards_html += f"""
        <div style="background:rgba(11,18,44,0.88); border:1px solid rgba(192,132,252,0.35); border-radius:14px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 12px 35px rgba(0,0,0,0.5);">
          <!-- Top Title Bar -->
          <div style="padding:12px 18px; background:rgba(25,35,75,0.7); border-bottom:1px solid rgba(192,132,252,0.25); display:flex; justify-content:space-between; align-items:center;">
            <div style="font-family:'Space Grotesk', sans-serif; font-size:15px; font-weight:700; color:#FFFFFF;">
              {cfg['name']}
            </div>
            <div style="font-family:'JetBrains Mono', monospace; font-size:11px; font-weight:700; color:#38BDF8;">
              {cfg['id']}
            </div>
          </div>
          <!-- Preview Frame -->
          <div style="flex:1; padding:24px 28px; position:relative; overflow:hidden; background:linear-gradient(135deg, rgba(7,11,28,0.95) 0%, rgba(15,23,55,0.95) 100%);">
            {cfg['html_title']}
          </div>
          <!-- Bottom Description -->
          <div style="padding:10px 18px; background:rgba(11,18,44,0.9); font-size:12px; color:#CBD5E1; border-top:1px solid rgba(233,213,255,0.15);">
            {cfg['desc']}
          </div>
        </div>
        """

    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>
      * {{ box-sizing: border-box; margin: 0; padding: 0; }}
      body {{
        width: 1920px; height: 1080px; overflow: hidden;
        background: #070D20; font-family: 'Plus Jakarta Sans', sans-serif; color: #FFFFFF; position: relative;
        padding: 30px 48px; display: flex; flex-direction: column; justify-content: space-between;
      }}
      .mono {{ font-family: 'JetBrains Mono', monospace; }}
      .grotesk {{ font-family: 'Space Grotesk', sans-serif; }}
    </style></head><body>
      <!-- Top Title -->
      <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-bottom:16px; border-bottom:1px solid rgba(192,132,252,0.3);">
        <div style="display:flex; align-items:center; gap:20px;">
          <img src="{u_logo_white}" alt="VMAA" style="height:40px; width:auto;"/>
          <div>
            <div class="grotesk" style="font-size:24px; font-weight:800; letter-spacing:0.12em; color:#FFFFFF;">
              VMAA M&amp;A 2026 MIỀN TRUNG — 6 PHƯƠNG ÁN TYPOGRAPHY ĐỈNH CAO
            </div>
            <div class="mono" style="font-size:12px; color:#C084FC; margin-top:2px;">
              FORWARD-LOOKING · FUTURISTIC · INTELLIGENT · DYNAMIC ITALIC &amp; NON-ITALIC SELECTION MATRIX
            </div>
          </div>
        </div>
        <div class="mono" style="font-size:12px; color:#38BDF8; padding:6px 14px; background:rgba(36,91,255,0.25); border:1px solid #38BDF8; border-radius:6px;">
          4K COMPARISON MATRIX (16:9)
        </div>
      </div>

      <!-- 6 Grid Cards -->
      <div style="display:grid; grid-template-columns:repeat(3, 1fr); grid-template-rows:repeat(2, 1fr); gap:20px; flex:1; margin-top:20px; margin-bottom:16px;">
        {cards_html}
      </div>

      <!-- Footer -->
      <div style="display:flex; justify-content:space-between; align-items:center; padding-top:12px; border-top:1px solid rgba(192,132,252,0.2); font-size:12px; color:#94A3B8;">
        <div>ĐÃ KHẮC PHỤC TRIỆT ĐỂ: Bỏ 100% khung viền/pill giả AI · Logo VMAA đứng trực tiếp không viền · Đầy đủ dấu tiếng Việt chuẩn MIỀN TRUNG.</div>
        <div class="mono" style="color:#FDE047;">CHỌN 1 TRONG 6 PHƯƠNG ÁN ĐỂ ÁP DỤNG LÊN BẢN CHÍNH THỨC</div>
      </div>
    </body></html>"""


def render_all_redesigned_assets():
    # 1. Render Primary Redesigned Key Visual (Using Option 01 - Next Forum Dynamic Italic as Hero Master)
    hero_cfg = TYPO_CONFIGS[0]
    hero_html = build_full_keyvisual_html(hero_cfg)
    hero_html_file = EXPORTS_DIR / "01_VMAA_HERO_KEY_VISUAL_4K.html"
    hero_png_file = EXPORTS_DIR / "01_VMAA_HERO_KEY_VISUAL_4K.png"
    hero_html_file.write_text(hero_html, encoding="utf-8")

    # 2. Render each of the 6 Typography Options
    rendered_typo_files = []
    for cfg in TYPO_CONFIGS:
        opt_html = build_full_keyvisual_html(cfg)
        opt_html_file = EXPORTS_DIR / f"{cfg['id']}_KeyVisual.html"
        opt_png_file = EXPORTS_DIR / f"{cfg['id']}_KeyVisual_4K.png"
        opt_html_file.write_text(opt_html, encoding="utf-8")
        rendered_typo_files.append((opt_html_file, opt_png_file))

    # 3. Render 6 Typography Options Matrix
    matrix_html = build_comparison_matrix_html()
    matrix_html_file = EXPORTS_DIR / "00_VMAA_6_Typography_Options_Matrix.html"
    matrix_png_file = EXPORTS_DIR / "00_VMAA_6_Typography_Options_Matrix.png"
    matrix_html_file.write_text(matrix_html, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Render at 2x scale for 3840x2160 4K UHD
        page = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)

        # 1. Primary Hero
        page.goto(hero_html_file.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(hero_png_file), type="png")
        print(f"Rendered {hero_png_file.name} (3840x2160 4K UHD)")
        shutil.copy2(hero_png_file, BRAIN_DIR / hero_png_file.name)

        # 2. 6 Individual Typo Options
        for h_file, p_file in rendered_typo_files:
            page.goto(h_file.as_uri(), wait_until="networkidle")
            page.wait_for_timeout(800)
            page.screenshot(path=str(p_file), type="png")
            print(f"Rendered {p_file.name} (3840x2160 4K UHD)")
            shutil.copy2(p_file, BRAIN_DIR / p_file.name)

        # 3. Matrix
        page.goto(matrix_html_file.as_uri(), wait_until="networkidle")
        page.wait_for_timeout(1000)
        page.screenshot(path=str(matrix_png_file), type="png")
        print(f"Rendered {matrix_png_file.name} (3840x2160 4K UHD)")
        shutil.copy2(matrix_png_file, BRAIN_DIR / matrix_png_file.name)

        browser.close()


if __name__ == "__main__":
    render_all_redesigned_assets()
