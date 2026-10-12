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
INVITE_DIR = EXPORTS_DIR / "invitations"

for d in [EXPORTS_DIR, SOCIAL_DIR, INVITE_DIR]:
    d.mkdir(parents=True, exist_ok=True)


def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{b64}"


u_hero_plate = to_data_uri(PLATES_DIR / "purple_opt01_hero_convergence.jpg")
u_prism_plate = to_data_uri(PLATES_DIR / "purple_opt02_fluted_caustics.jpg")
u_cantilever_plate = to_data_uri(PLATES_DIR / "purple_opt03_ascending_cantilevers.jpg")
u_aurora_plate = to_data_uri(PLATES_DIR / "purple_opt06_highkey_aurora_stage.jpg")
u_logo_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")
u_logo_blue = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_blue_transparent.png")

FONTS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,800&family=Manrope:wght@300;400;500;600;700;800&family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
"""

# Common CSS styles
SHARED_CSS = """
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #070D20; font-family: 'Be Vietnam Pro', sans-serif; color: #FFFFFF; position: relative; overflow: hidden;
  }
  .mono { font-family: 'Manrope', sans-serif; text-transform: uppercase; letter-spacing: 0.18em; }
  .aurora {
    position: absolute; inset: 0; mix-blend-mode: screen; pointer-events: none;
    background:
      radial-gradient(750px 650px at 70% 40%, rgba(155,77,255,0.40) 0%, rgba(36,91,255,0.25) 50%, transparent 80%),
      radial-gradient(600px 500px at 25% 65%, rgba(107,45,155,0.38) 0%, transparent 75%);
  }
  .shade {
    position: absolute; inset: 0; pointer-events: none;
    background: linear-gradient(180deg, rgba(7,11,28,0.85) 0%, rgba(7,11,28,0.3) 38%, rgba(7,11,28,0.4) 60%, rgba(7,11,28,0.95) 100%);
  }
"""

# =========================================================================
# 1. 6 SOCIAL MEDIA POSTS SUITE (1:1 Square 2160x2160 & 4:5 Portrait 2160x2700)
# =========================================================================

# POST 01: Master Announcement
def get_post_01_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{SHARED_CSS}
      body {{ width: 1080px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_hero_plate}') center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:50px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:38px; width:auto;"/>
          <div class="mono" style="font-size:11px; font-weight:700; color:#38BDF8;">OFFICIAL ANNOUNCEMENT</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#C084FC; margin-bottom:8px;">RA MẮT VMAA MIỀN TRUNG · ĐÀ NẴNG 2026</div>
          <div style="font-size:32px; font-weight:800; letter-spacing:0.2em; text-transform:uppercase;">DIỄN ĐÀN</div>
          <div style="font-size:78px; font-weight:900; line-height:0.92; margin-top:2px;">M&amp;A 2026</div>
          <div style="font-size:56px; font-weight:900; color:#A855F7; line-height:0.98; margin-top:4px;">MIỀN TRUNG</div>
          <div style="margin-top:18px;">
            <div style="font-size:22px; font-weight:800; color:#FFFFFF;">KIẾN TRÚC GIÁ TRỊ:</div>
            <div style="font-size:22px; font-weight:800; font-style:italic; color:#FDE047;">BẤT ĐỘNG SẢN × CÔNG NGHỆ</div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-top:16px; border-top:1px solid rgba(233,213,255,0.25);">
          <div>
            <div class="mono" style="font-size:10px; color:#C084FC; margin-bottom:3px;">THỜI GIAN &amp; ĐỊA ĐIỂM</div>
            <div style="font-size:18px; font-weight:800;">Chủ Nhật · 13.12.2026</div>
            <div style="font-size:13px; font-weight:600; color:#93C5FD;">13:30 – 17:30 · Đà Nẵng, Việt Nam</div>
          </div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FDE047;">1,500+ DELEGATES</div>
        </div>
      </div>
    </body></html>"""

# POST 02: Keynote Speaker Spotlight (Featuring the Architectural Plinth / Bệ Đỡ)
def get_post_02_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{SHARED_CSS}
      body {{ width: 1080px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_prism_plate}') center/cover; filter: brightness(1.12) contrast(1.1); }}
      .shell {{ position:absolute; inset:50px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      /* Architectural Illuminated Plinth / Bệ Đỡ Phát Sáng */
      .plinth {{
        background: linear-gradient(180deg, rgba(30,42,88,0.88) 0%, rgba(11,18,44,0.96) 100%);
        border: 1.5px solid rgba(192,132,252,0.45);
        border-top: 3px solid #C084FC;
        box-shadow: 0 15px 45px rgba(107,45,155,0.4), inset 0 1px 0 rgba(255,255,255,0.3);
        border-radius: 12px;
        padding: 22px 28px;
        position: relative;
        overflow: hidden;
      }}
      .plinth::after {{
        content: ''; position: absolute; top:0; left:-100%; width: 60%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.18), transparent);
        transform: skewX(-25deg);
      }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:36px; width:auto;"/>
          <div class="mono" style="font-size:11px; font-weight:700; color:#FDE047;">KEYNOTE SPEAKER SPOTLIGHT</div>
        </div>

        <!-- Speaker Avatar + Dedicated Motion Plinth -->
        <div style="display:flex; flex-direction:column; align-items:center; text-align:center; margin: auto 0;">
          <!-- Glowing Avatar Frame -->
          <div style="width:190px; height:190px; border-radius:50%; padding:5px; background:linear-gradient(135deg, #FDE047, #C084FC, #245BFF); box-shadow:0 0 35px rgba(155,77,255,0.6); margin-bottom:20px;">
            <div style="width:100%; height:100%; border-radius:50%; background:#131B38; display:flex; align-items:center; justify-content:center; overflow:hidden;">
              <svg width="150" height="150" viewBox="0 0 150 150" fill="none">
                <circle cx="75" cy="55" r="32" fill="#FED7AA"/>
                <path d="M48 52 C48 28 60 20 75 20 C90 20 102 28 102 52 C98 44 88 38 75 38 C62 38 52 44 48 52 Z" fill="#334155"/>
                <path d="M22 150 C22 105 45 92 75 92 C105 92 128 105 128 150 Z" fill="#3B82F6"/>
                <polygon points="62,92 88,92 75,120" fill="#FFFFFF"/>
                <polygon points="73,98 77,98 76,128 74,128" fill="#F59E0B"/>
              </svg>
            </div>
          </div>

          <!-- Dedicated Architectural Plinth (Bệ Đỡ Chỗ Tên & Đơn Vị) -->
          <div class="plinth" style="width:100%; max-width:620px;">
            <div class="mono" style="font-size:11px; color:#93C5FD; margin-bottom:5px;">DIỄN GIẢ CHỦ TRÌ TỌA ĐÀM</div>
            <div style="font-size:28px; font-weight:900; letter-spacing:0.04em; color:#FFFFFF; text-transform:uppercase;">
              TS. TRẦN ĐÌNH THIÊN
            </div>
            <div style="font-size:15px; font-weight:700; color:#E9D5FF; margin-top:4px;">
              Nguyên Viện trưởng Viện Kinh tế Việt Nam
            </div>
            <div style="font-size:13px; font-weight:500; color:#94A3B8; margin-top:4px;">
              Chuyên gia Cố vấn Kinh tế Vĩ mô &amp; Tái cấu trúc M&amp;A
            </div>
          </div>
        </div>

        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2);">
          <div style="font-size:14px; font-weight:700; color:#E2E8F0;">DIỄN ĐÀN M&amp;A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:11px; color:#FDE047;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

# POST 03: Executive Program Timeline (Forum & Gala Dinner)
def get_post_03_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{SHARED_CSS}
      body {{ width: 1080px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_cantilever_plate}') center/cover; filter: brightness(1.1) contrast(1.12); }}
      .shell {{ position:absolute; inset:50px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
      .agenda-row {{
        display:flex; align-items:center; gap:20px; padding:16px 20px;
        background:rgba(18,26,60,0.78); border-left:4px solid #C084FC; border-radius:0 10px 10px 0; margin-bottom:12px;
      }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:36px; width:auto;"/>
          <div class="mono" style="font-size:11px; font-weight:700; color:#38BDF8;">EXECUTIVE AGENDA</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; color:#C084FC; margin-bottom:6px;">LỊCH TRÌNH CHÍNH THỨC · 2 GIAI ĐOẠN</div>
          <div style="font-size:38px; font-weight:900; line-height:1.1; margin-bottom:20px;">
            CHƯƠNG TRÌNH DIỄN ĐÀN
          </div>
          <!-- Agenda 1 -->
          <div class="agenda-row">
            <div class="mono" style="font-size:18px; font-weight:800; color:#FDE047; width:110px;">13:30</div>
            <div>
              <div style="font-size:16px; font-weight:800;">LỄ RA MẮT VMAA MIỀN TRUNG &amp; BÁO CÁO TOÀN CẢNH M&amp;A</div>
              <div style="font-size:12.5px; color:#CBD5E1; margin-top:2px;">Công bố mạng lưới 30+ hội viên sáng lập và báo cáo độc quyền</div>
            </div>
          </div>
          <!-- Agenda 2 -->
          <div class="agenda-row" style="border-left-color:#38BDF8;">
            <div class="mono" style="font-size:18px; font-weight:800; color:#38BDF8; width:110px;">14:30</div>
            <div>
              <div style="font-size:16px; font-weight:800;">PHIÊN TỌA ĐÀM: BẤT ĐỘNG SẢN &amp; HẠ TẦNG CÔNG NGHỆ</div>
              <div style="font-size:12.5px; color:#CBD5E1; margin-top:2px;">Tái cấu trúc danh mục tài sản và giải pháp chuyển đổi PropTech</div>
            </div>
          </div>
          <!-- Agenda 3 -->
          <div class="agenda-row" style="border-left-color:#FDE047;">
            <div class="mono" style="font-size:18px; font-weight:800; color:#FDE047; width:110px;">16:00</div>
            <div>
              <div style="font-size:16px; font-weight:800;">1:1 DEAL ROOM &amp; KÝ KẾT HỢP TÁC CHIẾN LƯỢC (MOU)</div>
              <div style="font-size:12.5px; color:#CBD5E1; margin-top:2px;">Kết nối trực tiếp Chủ đầu tư và các Quỹ đầu tư FDI</div>
            </div>
          </div>
          <!-- Agenda 4 -->
          <div class="agenda-row" style="border-left-color:#EC4899; margin-bottom:0;">
            <div class="mono" style="font-size:18px; font-weight:800; color:#EC4899; width:110px;">18:00</div>
            <div>
              <div style="font-size:16px; font-weight:800;">GALA DINNER: NETWORKING &amp; VINH DANH THƯƠNG VỤ</div>
              <div style="font-size:12.5px; color:#CBD5E1; margin-top:2px;">Tiệc tối thượng đỉnh kết nối các định chế tài chính</div>
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2);">
          <div class="mono" style="font-size:11px; color:#93C5FD;">GRAND BALLROOM · ĐÀ NẴNG</div>
          <div class="mono" style="font-size:11px; color:#FDE047;">13.12.2026</div>
        </div>
      </div>
    </body></html>"""

# POST 04: Pillar 01 - Real Estate & Capital Influx
def get_post_04_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{SHARED_CSS}
      body {{ width: 1080px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_hero_plate}') 75% center/cover; filter: brightness(1.15) contrast(1.12); }}
      .shell {{ position:absolute; inset:50px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:36px; width:auto;"/>
          <div class="mono" style="font-size:11px; font-weight:700; color:#38BDF8;">PILLAR 01 · REAL ESTATE</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#C084FC; margin-bottom:8px;">TRỌNG TÂM CHIẾN LƯỢC M&amp;A</div>
          <div style="font-size:48px; font-weight:900; line-height:1.05;">
            TÁI CẤU TRÚC VỐN &amp;<br/><span style="color:#38BDF8;">QUỸ ĐẤT CHIẾN LƯỢC</span>
          </div>
          <p style="font-size:16px; font-weight:500; color:#CBD5E1; line-height:1.55; max-width:680px; margin-top:18px;">
            Giải pháp M&amp;A toàn diện giúp giải phóng nguồn lực tài chính, kết nối quỹ đất đô thị, nghỉ dưỡng và công nghiệp tại Miền Trung với dòng vốn FDI dài hạn.
          </p>
          <div style="display:flex; gap:36px; margin-top:28px;">
            <div>
              <div style="font-size:36px; font-weight:900; color:#FDE047;">$1.2B+</div>
              <div class="mono" style="font-size:10px; color:#93C5FD; margin-top:2px;">DÒNG VỐN QUỐC TẾ CHỜ GIẢI NGÂN</div>
            </div>
            <div style="width:1.5px; height:45px; background:rgba(233,213,255,0.3); align-self:center;"></div>
            <div>
              <div style="font-size:36px; font-weight:900; color:#FFFFFF;">30+</div>
              <div class="mono" style="font-size:10px; color:#93C5FD; margin-top:2px;">DỰ ÁN SẴN SÀNG DEAL ROOM</div>
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2);">
          <div style="font-size:14px; font-weight:700;">DIỄN ĐÀN M&amp;A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:11px; color:#FDE047;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

# POST 05: Pillar 02 - Technology, AI Valuation & PropTech
def get_post_05_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{SHARED_CSS}
      body {{ width: 1080px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_prism_plate}') 60% center/cover; filter: brightness(1.15) contrast(1.1); }}
      .shell {{ position:absolute; inset:50px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:36px; width:auto;"/>
          <div class="mono" style="font-size:11px; font-weight:700; color:#C084FC;">PILLAR 02 · TECHNOLOGY</div>
        </div>
        <div>
          <div class="mono" style="font-size:12px; font-weight:700; color:#38BDF8; margin-bottom:8px;">CÔNG NGHỆ &amp; THẨM ĐỊNH GIÁ AI</div>
          <div style="font-size:48px; font-weight:900; line-height:1.05;">
            PROPTECH &amp;<br/><span style="color:#C084FC;">ĐỊNH GIÁ SỐ HÓA</span>
          </div>
          <p style="font-size:16px; font-weight:500; color:#CBD5E1; line-height:1.55; max-width:680px; margin-top:18px;">
            Ứng dụng trí tuệ nhân tạo (AI) và phân tích dữ liệu lớn trong thẩm định giá trị tài sản, tăng tốc độ thẩm định pháp lý và minh bạch hóa quy trình sáp nhập.
          </p>
          <div style="display:flex; gap:36px; margin-top:28px;">
            <div>
              <div style="font-size:36px; font-weight:900; color:#38BDF8;">3.4x</div>
              <div class="mono" style="font-size:10px; color:#93C5FD; margin-top:2px;">TỐC ĐỘ THẨM ĐỊNH DEAL NHANH HƠN</div>
            </div>
            <div style="width:1.5px; height:45px; background:rgba(233,213,255,0.3); align-self:center;"></div>
            <div>
              <div style="font-size:36px; font-weight:900; color:#FDE047;">100%</div>
              <div class="mono" style="font-size:10px; color:#93C5FD; margin-top:2px;">MINH BẠCH HÓA THẨM ĐỊNH VỐN</div>
            </div>
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2);">
          <div style="font-size:14px; font-weight:700;">DIỄN ĐÀN M&amp;A 2026 MIỀN TRUNG</div>
          <div class="mono" style="font-size:11px; color:#FDE047;">13.12.2026 · ĐÀ NẴNG</div>
        </div>
      </div>
    </body></html>"""

# POST 06: VIP Registration Call-To-Action
def get_post_06_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{SHARED_CSS}
      body {{ width: 1080px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_aurora_plate}') center/cover; filter: brightness(1.18) contrast(1.1); }}
      .shell {{ position:absolute; inset:50px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <img src="{u_logo_white}" style="height:36px; width:auto;"/>
          <div class="mono" style="font-size:11px; font-weight:700; color:#FDE047;">REGISTRATION OPEN</div>
        </div>
        <div style="text-align:center; max-width:800px; margin: auto;">
          <div class="mono" style="font-size:13px; font-weight:700; color:#C084FC; margin-bottom:10px;">SỐ LƯỢNG GIỚI HẠN · DÀNH CHO LÃNH ĐẠO CẤP CAO</div>
          <div style="font-size:52px; font-weight:900; line-height:1.05;">
            ĐĂNG KÝ THAM DỰ<br/><span style="color:#FDE047;">VIP DELEGATE PASS</span>
          </div>
          <p style="font-size:17px; font-weight:500; color:#E2E8F0; line-height:1.55; margin-top:20px; max-width:640px; margin-left:auto; margin-right:auto;">
            Quyền lợi trọn gói: Tham dự Diễn đàn M&amp;A, tiếp cận 1:1 Deal Matching Room, Báo cáo Nghiên cứu Độc quyền và vé VIP Gala Dinner.
          </p>
          <div style="display:inline-block; margin-top:30px; padding:16px 42px; background:linear-gradient(135deg, #FDE047, #EAB308); color:#070D20; font-size:18px; font-weight:900; border-radius:8px; box-shadow:0 12px 35px rgba(253,224,71,0.45); letter-spacing:0.04em;">
            ĐĂNG KÝ NGAY HÔM NAY ↗
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; padding-top:16px; border-top:1px solid rgba(233,213,255,0.2);">
          <div style="font-size:14px; font-weight:700;">HẠN ĐĂNG KÝ: 05.12.2026</div>
          <div class="mono" style="font-size:11px; color:#38BDF8;">WWW.VMAA.VN/MIENTRUNG2026</div>
        </div>
      </div>
    </body></html>"""


# =========================================================================
# 2. VIP INVITATION SUITE WITH ARCHITECTURAL MOTION PLINTH (BỆ ĐỠ CHỖ TÊN)
# =========================================================================

def get_vip_invitation_html():
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8">{FONTS}<style>{SHARED_CSS}
      body {{ width: 1920px; height: 1080px; }}
      .bg {{ position:absolute; inset:0; background: url('{u_hero_plate}') 65% center/cover; filter: brightness(1.15) contrast(1.12); }}
      .shell {{ position:absolute; inset:48px 64px; display:flex; flex-direction:column; justify-content:space-between; z-index:10; }}

      /* The Architectural Motion Plinth / Bệ Đỡ Phát Sáng Cho Khách Mời */
      .plinth-container {{
        width: 100%; max-width: 820px;
        background: linear-gradient(180deg, rgba(22,32,72,0.92) 0%, rgba(10,16,42,0.98) 100%);
        border: 2px solid rgba(192,132,252,0.55);
        border-top: 4px solid #C084FC;
        border-radius: 16px;
        box-shadow:
          0 25px 60px rgba(107,45,155,0.45),
          0 0 40px rgba(36,91,255,0.25),
          inset 0 1px 0 rgba(255,255,255,0.4);
        padding: 32px 42px;
        position: relative;
        overflow: hidden;
      }}
      /* Luminous light sweep on plinth */
      .plinth-container::before {{
        content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%;
        background: radial-gradient(circle at 30% 20%, rgba(233,213,255,0.18) 0%, transparent 60%);
        pointer-events:none;
      }}
      .plinth-pedestal-base {{
        display:flex; align-items:center; justify-content:space-between; margin-top:20px; padding-top:16px;
        border-top: 1px solid rgba(192,132,252,0.28);
      }}
    </style></head><body>
      <div class="bg"></div><div class="aurora"></div><div class="shade"></div>
      <div class="shell">
        <!-- Top Invitation Header -->
        <div style="display:flex; justify-content:space-between; align-items:center; padding-bottom:18px; border-bottom:1px solid rgba(233,213,255,0.22);">
          <div style="display:flex; align-items:center; gap:18px;">
            <img src="{u_logo_white}" style="height:44px; width:auto;"/>
            <div>
              <div style="font-family:'Manrope',sans-serif; font-size:13px; font-weight:800; letter-spacing:0.18em; color:#FFFFFF;">
                HIỆP HỘI MUA BÁN VÀ SÁP NHẬP DOANH NGHIỆP VIỆT NAM
              </div>
              <div class="mono" style="font-size:10px; color:#C084FC; margin-top:2px;">VIETNAM MERGERS &amp; ACQUISITIONS ASSOCIATION</div>
            </div>
          </div>
          <div class="mono" style="font-size:12px; font-weight:800; color:#FDE047; padding:8px 20px; background:rgba(253,224,71,0.12); border:1.5px solid #FDE047; border-radius:6px;">
            THƯ MỜI DANH DỰ // VIP INVITATION
          </div>
        </div>

        <!-- Center: Invitation Text + The Hero Plinth -->
        <div style="display:flex; justify-content:space-between; align-items:center; gap:60px;">
          <!-- Left: Event Name & Formal Salutation -->
          <div style="flex:1;">
            <div class="mono" style="font-size:13px; font-weight:700; color:#38BDF8; margin-bottom:8px;">
              TRỌNG THỂ KÍNH MỜI QUÝ LÃNH ĐẠO
            </div>
            <div style="font-size:46px; font-weight:900; line-height:1.05;">
              DIỄN ĐÀN M&amp;A 2026<br/><span style="color:#A855F7;">MIỀN TRUNG</span>
            </div>
            <div style="font-size:22px; font-weight:800; color:#FDE047; margin-top:12px; font-style:italic;">
              Kiến trúc Giá trị: Bất động sản × Công nghệ
            </div>
            <p style="font-size:16px; font-weight:500; color:#CBD5E1; line-height:1.6; margin-top:16px; max-width:540px;">
              Trân trọng kính mời Quý Khách quý tham dự Lễ ra mắt VMAA Miền Trung, Tọa đàm Kinh tế Cấp cao và Phiên kết nối đầu tư 1:1 Deal Room giữa các Tập đoàn và Quỹ đầu tư quốc tế.
            </p>
          </div>

          <!-- Right: The Dedicated Plinth / Bệ Đỡ Chỗ Tên & Đơn Vị -->
          <div class="plinth-container">
            <div style="display:flex; align-items:center; gap:24px;">
              <!-- Portrait frame -->
              <div style="width:110px; height:110px; border-radius:50%; padding:3px; background:linear-gradient(135deg, #FDE047, #C084FC); box-shadow:0 0 25px rgba(155,77,255,0.6); flex-shrink:0;">
                <div style="width:100%; height:100%; border-radius:50%; background:#0B122C; display:flex; align-items:center; justify-content:center; overflow:hidden;">
                  <svg width="85" height="85" viewBox="0 0 100 100" fill="none">
                    <circle cx="50" cy="38" r="22" fill="#FED7AA"/>
                    <path d="M30 36 C30 18 40 12 50 12 C60 12 70 18 70 36 Z" fill="#334155"/>
                    <path d="M15 100 C15 70 30 60 50 60 C70 60 85 70 85 100 Z" fill="#3B82F6"/>
                    <polygon points="42,60 58,60 50,78" fill="#FFFFFF"/>
                  </svg>
                </div>
              </div>

              <!-- Name & Title on the Plinth -->
              <div>
                <div class="mono" style="font-size:11px; font-weight:700; color:#93C5FD; margin-bottom:4px;">
                  ĐẠI BIỂU DANH DỰ / VIP GUEST
                </div>
                <div style="font-size:32px; font-weight:900; letter-spacing:0.02em; color:#FFFFFF; text-transform:uppercase;">
                  ÔNG NGUYỄN VĂN AN
                </div>
                <div style="font-size:16px; font-weight:700; color:#FDE047; margin-top:4px;">
                  Chủ tịch Hội đồng Quản trị &amp; Tổng Giám đốc
                </div>
                <div style="font-size:14px; font-weight:500; color:#E9D5FF; margin-top:2px;">
                  Tập đoàn Bất động sản &amp; Đầu tư Phát triển Miền Trung
                </div>
              </div>
            </div>

            <!-- Plinth Pedestal Base details -->
            <div class="plinth-pedestal-base">
              <div>
                <div class="mono" style="font-size:9.5px; color:#C084FC;">MÃ THƯ MỜI VIP</div>
                <div class="mono" style="font-size:15px; font-weight:800; color:#FFFFFF; margin-top:2px;">VMAA-2026-VIP-0089</div>
              </div>
              <div>
                <div class="mono" style="font-size:9.5px; color:#C084FC;">VỊ TRÍ GHẾ NGỒI</div>
                <div class="mono" style="font-size:15px; font-weight:800; color:#38BDF8; margin-top:2px;">ROW A · SEAT 08 (VIP 1)</div>
              </div>
              <div>
                <div class="mono" style="font-size:9.5px; color:#C084FC;">ĐẶC QUYỀN THAM DỰ</div>
                <div class="mono" style="font-size:15px; font-weight:800; color:#FDE047; margin-top:2px;">FORUM + GALA DINNER</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bottom Venue & Program Meta -->
        <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-top:18px; border-top:1px solid rgba(233,213,255,0.22);">
          <div>
            <div class="mono" style="font-size:10.5px; color:#C084FC; margin-bottom:3px;">THỜI GIAN &amp; ĐỊA ĐIỂM</div>
            <div style="font-size:19px; font-weight:800;">Chủ Nhật · 13.12.2026 | 13:30 – 21:00</div>
            <div style="font-size:14px; font-weight:500; color:#93C5FD;">Grand Ballroom · Ariyana Convention Centre (Furama Resort), Đà Nẵng</div>
          </div>
          <div style="text-align:right;">
            <div class="mono" style="font-size:10px; color:#C084FC; margin-bottom:3px;">XÁC NHẬN THAM DỰ TRƯỚC 05.12.2026</div>
            <div class="mono" style="font-size:14px; font-weight:800; color:#FFFFFF;">HOTLINE BTC: (+84) 905 123 456</div>
          </div>
        </div>
      </div>
    </body></html>"""


def render_all_assets():
    posts = [
        ("POST_01_Announcement_1x1", get_post_01_html()),
        ("POST_02_SpeakerSpotlight_1x1", get_post_02_html()),
        ("POST_03_AgendaTimeline_1x1", get_post_03_html()),
        ("POST_04_Pillar_RealEstate_1x1", get_post_04_html()),
        ("POST_05_Pillar_Technology_1x1", get_post_05_html()),
        ("POST_06_VIPPass_Registration_1x1", get_post_06_html()),
    ]

    rendered_posts = []
    for name, html in posts:
        h_file = SOCIAL_DIR / f"{name}.html"
        p_file = SOCIAL_DIR / f"{name}_4K.png"
        h_file.write_text(html, encoding="utf-8")
        rendered_posts.append((h_file, p_file))

    invite_html_file = INVITE_DIR / "INVITATION_VIP_Card.html"
    invite_png_file = INVITE_DIR / "INVITATION_VIP_Card_4K.png"
    invite_html_file.write_text(get_vip_invitation_html(), encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 1:1 Social Posts (1080x1080 @ 2x = 2160x2160)
        page = browser.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=2)
        for h_f, p_f in rendered_posts:
            page.goto(h_f.as_uri(), wait_until="networkidle")
            page.wait_for_timeout(600)
            page.screenshot(path=str(p_f), type="png")
            print(f"Rendered {p_f.name} (2160x2160 4K Square)")
            shutil.copy2(p_f, BRAIN_DIR / p_f.name)

        # VIP Invitation (1920x1080 @ 2x = 3840x2160 4K UHD)
        page_invite = browser.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=2)
        page_invite.goto(invite_html_file.as_uri(), wait_until="networkidle")
        page_invite.wait_for_timeout(800)
        page_invite.screenshot(path=str(invite_png_file), type="png")
        print(f"Rendered {invite_png_file.name} (3840x2160 4K UHD)")
        shutil.copy2(invite_png_file, BRAIN_DIR / invite_png_file.name)

        browser.close()


if __name__ == "__main__":
    render_all_assets()
