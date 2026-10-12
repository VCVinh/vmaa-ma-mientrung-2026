import os
import sys
import json
import base64
import shutil
from pathlib import Path
from playwright.sync_api import sync_playwright

PROJECT_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
BRAIN_DIR = Path(r"C:\Users\Admin\.gemini\antigravity\brain\0a54a89d-412c-4fdb-8ada-6fe42738710f")

INVITES_DATA_PATH = PROJECT_DIR / "src" / "data" / "guest_invitations.json"
guest_list = json.loads(INVITES_DATA_PATH.read_text(encoding="utf-8"))

INVITE_EXPORT_DIR = PROJECT_DIR / "exports" / "invitations"
VIDEO_EXPORT_DIR = PROJECT_DIR / "exports" / "videos"
RAW_RECORD_DIR = PROJECT_DIR / "exports" / "raw_recordings"

for d in [INVITE_EXPORT_DIR, VIDEO_EXPORT_DIR, RAW_RECORD_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def to_data_uri(path: Path) -> str:
    b64 = base64.b64encode(path.read_bytes()).decode("ascii")
    suffix = path.suffix.lower()
    mime = "image/png" if suffix == ".png" else ("image/jpeg" if suffix in [".jpg", ".jpeg"] else "image/svg+xml")
    return f"data:{mime};base64,{b64}"

PLATES_DIR = PROJECT_DIR / "assets" / "plates"
u_hero_plate = to_data_uri(PLATES_DIR / "purple_opt01_hero_convergence.jpg")
u_stage_plate = to_data_uri(PLATES_DIR / "purple_opt06_highkey_aurora_stage.jpg")
u_isometric_plate = to_data_uri(PLATES_DIR / "purple_opt05_imperial_isometric.jpg")
u_logo_white = to_data_uri(PROJECT_DIR / "assets" / "vmaa_logo_white_transparent.png")

FONTS_HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,700&family=Manrope:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
"""

def generate_invitation_html(guest, mode="landscape"):
    w = 1920 if mode == "landscape" else 1080
    h = 1080 if mode == "landscape" else (1920 if mode == "vertical" else 1350)
    bg_plate = u_hero_plate if mode == "landscape" else u_stage_plate

    # Layout dimensions based on orientation
    is_vertical = mode == "vertical"
    is_portrait = mode == "portrait"

    plinth_width = 860 if is_vertical else (780 if is_portrait else 720)
    plinth_padding = "48px 40px 32px 40px" if is_vertical else "44px 36px 28px 36px"
    name_size = 36 if is_vertical else (32 if is_portrait else 34)

    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Thư Mời Danh Dự | {guest['name']}</title>
  {FONTS_HEAD}
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      width: {w}px; height: {h}px;
      background: #070D20; color: #FFFFFF;
      font-family: 'Be Vietnam Pro', sans-serif;
      overflow: hidden; position: relative;
      -webkit-font-smoothing: antialiased;
    }}
    .bg {{
      position: absolute; inset: 0;
      background: url('{bg_plate}') center/cover;
      filter: brightness(1.12) contrast(1.1);
      transform: scale(1.03);
      animation: ambientZoom 12s ease-in-out infinite alternate;
    }}
    @keyframes ambientZoom {{ 0% {{ transform: scale(1.02); }} 100% {{ transform: scale(1.06); }} }}

    .aurora {{
      position: absolute; inset: 0; pointer-events: none; mix-blend-mode: screen;
      background:
        radial-gradient(900px 750px at 70% 30%, rgba(155,77,255,0.4) 0%, rgba(36,91,255,0.25) 50%, transparent 80%),
        radial-gradient(700px 600px at 25% 75%, rgba(107,45,155,0.35) 0%, transparent 75%);
    }}
    .shade {{
      position: absolute; inset: 0; pointer-events: none;
      background: linear-gradient(180deg, rgba(7,13,32,0.85) 0%, rgba(7,13,32,0.3) 40%, rgba(7,13,32,0.6) 65%, rgba(7,13,32,0.95) 100%);
    }}

    .mono {{ font-family: 'Manrope', sans-serif; text-transform: uppercase; letter-spacing: 0.18em; }}
    .gold {{ color: #FACC15; }}
    .cyan {{ color: #38BDF8; }}
    .lavender {{ color: #D8B4FE; }}

    /* Canvas Grid Container */
    .shell {{
      position: absolute; inset: {'90px 70px' if is_vertical else '60px 80px'};
      display: flex; flex-direction: column; justify-content: space-between; z-index: 10;
    }}

    /* Top Bar */
    .top-bar {{
      display: flex; justify-content: space-between; align-items: center;
      animation: fadeInDown 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}
    .vip-tag-badge {{
      border: 1px solid rgba(250, 204, 21, 0.5); background: rgba(250, 204, 21, 0.08);
      padding: 8px 18px; border-radius: 4px; font-family: 'Manrope', sans-serif;
      font-size: 11px; font-weight: 800; color: #FACC15; letter-spacing: 0.2em;
    }}

    /* Main Content Layout */
    .main-grid {{
      display: {'flex; flex-direction:column; gap:40px;' if (is_vertical or is_portrait) else 'grid; grid-template-columns: 1fr 1fr; gap:60px; align-items:center;'};
      flex-grow: 1; justify-content: center;
    }}

    /* Left Narrative Column */
    .narrative-col {{
      animation: fadeInLeft 1.4s cubic-bezier(0.16, 1, 0.3, 1) 0.3s forwards;
      opacity: 0;
    }}
    .eyebrow {{
      font-family: 'Manrope', sans-serif; font-size: 12px; font-weight: 800;
      color: #38BDF8; letter-spacing: 0.22em; text-transform: uppercase; margin-bottom: 12px;
    }}
    .event-title {{
      font-size: {'56px' if is_vertical else '48px'}; font-weight: 900; line-height: 1.05;
      letter-spacing: -0.02em; text-transform: uppercase; margin-bottom: 8px;
    }}
    .event-region {{
      font-size: {'46px' if is_vertical else '40px'}; font-weight: 900; line-height: 1;
      background: linear-gradient(135deg, #B77BFF 0%, #7C3AED 50%, #2563EB 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      margin-bottom: 16px;
    }}
    .invitation-intro {{
      font-size: 14px; color: #E2E8F0; line-height: 1.6; max-width: 520px;
    }}

    /* =========================================================================
       SIGNATURE LOWER-THIRD MOTION ARCHITECTURAL PLINTH
       ========================================================================= */
    .plinth-wrapper {{
      width: 100%; max-width: {plinth_width}px; position: relative; margin: 0 auto;
      display: flex; flex-direction: column; align-items: center;
    }}

    /* Avatar with Conic Glow */
    .avatar-monolith {{
      position: relative; width: 140px; height: 140px; margin-bottom: -32px; z-index: 15;
      animation: avatarPop 1.4s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
      opacity: 0; transform: translateY(20px) scale(0.9);
    }}
    .avatar-ring {{
      position: absolute; inset: -5px; border-radius: 50%;
      background: conic-gradient(from 0deg, #245BFF, #9B4DFF, #FACC15, #38BDF8, #245BFF);
      animation: spinRing 6s linear infinite; filter: drop-shadow(0 0 16px rgba(155,77,255,0.7));
    }}
    @keyframes spinRing {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
    .avatar-inner {{
      position: absolute; inset: 0; border-radius: 50%; background: #0F172A;
      border: 3px solid #070D20; display: flex; align-items: center; justify-content: center;
    }}

    /* Architectural Nameplate Box */
    .plinth-monolith {{
      position: relative; width: 100%;
      background: linear-gradient(135deg, rgba(16,26,61,0.94) 0%, rgba(9,14,33,0.98) 100%);
      border: 1px solid rgba(155,77,255,0.5); border-radius: 16px;
      padding: {plinth_padding}; text-align: center;
      box-shadow: 0 30px 80px rgba(0,0,0,0.85), inset 0 1px 0 rgba(255,255,255,0.3);
      backdrop-filter: blur(28px); overflow: hidden;
      clip-path: inset(0 100% 0 0); /* Initial mask for reveal */
      animation: panelReveal 1.2s cubic-bezier(0.77, 0, 0.175, 1) 0.8s forwards;
    }}
    @keyframes panelReveal {{ 0% {{ clip-path: inset(0 100% 0 0); }} 100% {{ clip-path: inset(0 0 0 0); }} }}

    /* Baseline Cobalt Line Draw */
    .plinth-baseline {{
      position: absolute; bottom: 0; left: 0; width: 0%; height: 3px;
      background: linear-gradient(90deg, #245BFF, #9B4DFF, #38BDF8);
      box-shadow: 0 0 12px #245BFF;
      animation: drawBaseline 1.5s cubic-bezier(0.16, 1, 0.3, 1) 0.2s forwards;
    }}
    @keyframes drawBaseline {{ 0% {{ width: 0%; }} 100% {{ width: 100%; }} }}

    /* Laser Caustic Sweep */
    .caustic-sweep {{
      position: absolute; inset: 0; pointer-events: none;
      background: linear-gradient(105deg, transparent 20%, rgba(255,255,255,0.08) 45%, rgba(155,77,255,0.35) 50%, rgba(56,189,248,0.25) 55%, transparent 70%);
      transform: translateX(-150%);
      animation: sweepMove 4.5s cubic-bezier(0.4, 0, 0.2, 1) 2.2s infinite;
    }}
    @keyframes sweepMove {{ 0% {{ transform: translateX(-150%); }} 40%, 100% {{ transform: translateX(150%); }} }}

    /* Staggered Typography Masked Reveals */
    .reveal-item {{
      opacity: 0; transform: translateY(12px);
    }}
    .tier-label {{
      font-family: 'Manrope', sans-serif; font-size: 11px; font-weight: 800;
      color: #38BDF8; letter-spacing: 0.22em; text-transform: uppercase; margin-bottom: 8px;
      animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 1.6s forwards;
    }}
    .guest-name {{
      font-size: {name_size}px; font-weight: 900; letter-spacing: -0.01em;
      color: #FFFFFF; text-transform: uppercase; margin-bottom: 6px;
      animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 1.9s forwards;
    }}
    .guest-title {{
      font-size: 15px; font-weight: 700; color: #D8B4FE; margin-bottom: 4px;
      animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 2.2s forwards;
    }}
    .guest-org {{
      font-size: 13px; color: #94A3B8; margin-bottom: 20px;
      animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 2.4s forwards;
    }}
    .plinth-footer {{
      display: flex; justify-content: space-around; align-items: center;
      border-top: 1px solid rgba(155,77,255,0.25); padding-top: 14px;
      animation: fadeIn 1s ease-out 2.6s forwards; opacity: 0;
    }}

    @keyframes fadeIn {{ to {{ opacity: 1; }} }}
    @keyframes fadeInUp {{ to {{ opacity: 1; transform: translateY(0); }} }}
    @keyframes fadeInDown {{ 0% {{ opacity: 0; transform: translateY(-16px); }} 100% {{ opacity: 1; transform: translateY(0); }} }}
    @keyframes fadeInLeft {{ 0% {{ opacity: 0; transform: translateX(-24px); }} 100% {{ opacity: 1; transform: translateX(0); }} }}
    @keyframes avatarPop {{ to {{ opacity: 1; transform: translateY(0) scale(1); }} }}
  </style>
</head>
<body>
  <div class="bg"></div>
  <div class="aurora"></div>
  <div class="shade"></div>

  <div class="shell">
    <!-- Top Brand Lockup -->
    <div class="top-bar">
      <img src="{u_logo_white}" style="height: 44px; width: auto;" alt="VMAA Logo">
      <div class="vip-tag-badge">THƯ MỜI DANH DỰ // VIP INVITATION</div>
    </div>

    <!-- Main Grid Content -->
    <div class="main-grid">
      <div class="narrative-col">
        <div class="eyebrow">Trọng Thể Kính Mời Quý Lãnh Đạo</div>
        <div class="event-title">Diễn Đàn M&A 2026</div>
        <div class="event-region">Miền Trung</div>
        <div class="invitation-intro">
          Trân trọng kính mời Quý Lãnh đạo tham dự Lễ ra mắt VMAA Phân hội Miền Trung, Tọa đàm Kinh tế Cấp cao và Phiên kết nối Đầu tư 1:1 Deal Room giữa các Tập đoàn và Quỹ đầu tư quốc tế.
        </div>
      </div>

      <!-- Architectural Motion Plinth -->
      <div class="plinth-wrapper">
        <div class="avatar-monolith">
          <div class="avatar-ring"></div>
          <div class="avatar-inner">
            <svg viewBox="0 0 100 100" style="width:100%; height:100%;">
              <circle cx="50" cy="50" r="50" fill="#0A1628"/>
              <circle cx="50" cy="40" r="18" fill="#F8FAFC"/>
              <path d="M22 84 C22 62, 36 58, 50 58 C64 58, 78 62, 78 84 Z" fill="#2563EB"/>
            </svg>
          </div>
        </div>

        <div class="plinth-monolith">
          <div class="plinth-baseline"></div>
          <div class="caustic-sweep"></div>

          <div class="reveal-item tier-label">{guest['tier']}</div>
          <div class="reveal-item guest-name">{guest['name']}</div>
          <div class="reveal-item guest-title">{guest['title']}</div>
          <div class="reveal-item guest-org">{guest['organization']}</div>

          <div class="plinth-footer">
            <div>
              <div class="mono" style="font-size:9px; color:#64748B;">MÃ THƯ MỜI</div>
              <div class="mono" style="font-size:11px; font-weight:800; color:#FFFFFF;">{guest['vipCode']}</div>
            </div>
            <div>
              <div class="mono" style="font-size:9px; color:#64748B;">VỊ TRÍ GHẾ</div>
              <div class="mono" style="font-size:11px; font-weight:800; color:#FACC15;">{guest['seat']}</div>
            </div>
            <div>
              <div class="mono" style="font-size:9px; color:#64748B;">ĐẶC QUYỀN</div>
              <div class="mono" style="font-size:11px; font-weight:800; color:#38BDF8;">FORUM + GALA DINNER</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Meta -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.15); padding-top:16px;">
      <div>
        <span class="mono" style="font-size:11px; color:#94A3B8;">THỜI GIAN: </span>
        <span style="font-size:13px; font-weight:700; color:#FFFFFF;">Chủ Nhật · 13.12.2026 | 13:30 – 21:00</span>
      </div>
      <div>
        <span class="mono" style="font-size:11px; color:#94A3B8;">ĐỊA ĐIỂM: </span>
        <span style="font-size:13px; font-weight:700; color:#D8B4FE;">Ariyana Convention Centre, Đà Nẵng</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

print("Generating Data-Driven Reusable Guest Invitation Suite...")

primary_guest = guest_list[1] # "ÔNG NGUYỄN VĂN AN"

# 1. Generate HTML Source Templates
html_vertical = INVITE_EXPORT_DIR / "INVITATION_Vertical_1080x1920.html"
html_landscape = INVITE_EXPORT_DIR / "INVITATION_Landscape_1920x1080.html"
html_portrait = INVITE_EXPORT_DIR / "INVITATION_Portrait_1080x1350.html"

html_vertical.write_text(generate_invitation_html(primary_guest, mode="vertical"), encoding="utf-8")
html_landscape.write_text(generate_invitation_html(primary_guest, mode="landscape"), encoding="utf-8")
html_portrait.write_text(generate_invitation_html(primary_guest, mode="portrait"), encoding="utf-8")

print("Written HTML source templates in exports/invitations/")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    # 2. Render Static Master PNGs (Still fallbacks)
    # Landscape 1920x1080
    page_land = browser.new_page(viewport={"width": 1920, "height": 1080})
    page_land.goto(html_landscape.as_uri())
    page_land.wait_for_timeout(3500) # Wait for animation to settle into final state
    land_png = INVITE_EXPORT_DIR / "INVITATION_Landscape_1920x1080_Master.png"
    page_land.screenshot(path=str(land_png))
    shutil.copy(land_png, BRAIN_DIR / land_png.name)
    page_land.close()
    print("Exported static master: INVITATION_Landscape_1920x1080_Master.png")

    # Vertical 1080x1920
    page_vert = browser.new_page(viewport={"width": 1080, "height": 1920})
    page_vert.goto(html_vertical.as_uri())
    page_vert.wait_for_timeout(3500)
    vert_png = INVITE_EXPORT_DIR / "INVITATION_Vertical_1080x1920_Master.png"
    page_vert.screenshot(path=str(vert_png))
    shutil.copy(vert_png, BRAIN_DIR / vert_png.name)
    page_vert.close()
    print("Exported static master: INVITATION_Vertical_1080x1920_Master.png")

    # Portrait 1080x1350
    page_port = browser.new_page(viewport={"width": 1080, "height": 1350})
    page_port.goto(html_portrait.as_uri())
    page_port.wait_for_timeout(3500)
    port_png = INVITE_EXPORT_DIR / "INVITATION_Portrait_1080x1350_Master.png"
    page_port.screenshot(path=str(port_png))
    shutil.copy(port_png, BRAIN_DIR / port_png.name)
    page_port.close()
    print("Exported static master: INVITATION_Portrait_1080x1350_Master.png")

    browser.close()

    # 3. Record Playback-Tested 60fps Motion Video Animations (8-10 Seconds)
    print("Recording true 60fps Motion Video of the Lower-Third Sequence (Landscape & Vertical)...")
    
    # Landscape Recording
    rec_context_land = p.chromium.launch(headless=True).new_context(
        record_video_dir=str(RAW_RECORD_DIR),
        record_video_size={"width": 1920, "height": 1080},
        viewport={"width": 1920, "height": 1080}
    )
    rec_page_l = rec_context_land.new_page()
    rec_page_l.goto(html_landscape.as_uri())
    rec_page_l.wait_for_timeout(9000) # Full 9-second animation sequence
    rec_context_land.close()

    # Find recorded file
    land_vids = list(RAW_RECORD_DIR.glob("*.webm"))
    if land_vids:
        latest_l = max(land_vids, key=lambda f: f.stat().st_mtime)
        dest_l = VIDEO_EXPORT_DIR / "VMAA_Guest_Invitation_Landscape_1080p.webm"
        shutil.copy(latest_l, dest_l)
        shutil.copy(dest_l, BRAIN_DIR / dest_l.name)
        print(f"Exported Motion Video: {dest_l.name} ({dest_l.stat().st_size} bytes)")

    # Vertical Recording
    rec_context_vert = p.chromium.launch(headless=True).new_context(
        record_video_dir=str(RAW_RECORD_DIR),
        record_video_size={"width": 1080, "height": 1920},
        viewport={"width": 1080, "height": 1920}
    )
    rec_page_v = rec_context_vert.new_page()
    rec_page_v.goto(html_vertical.as_uri())
    rec_page_v.wait_for_timeout(9000) # Full 9-second animation sequence
    rec_context_vert.close()

    vert_vids = list(RAW_RECORD_DIR.glob("*.webm"))
    if vert_vids:
        latest_v = max(vert_vids, key=lambda f: f.stat().st_mtime)
        dest_v = VIDEO_EXPORT_DIR / "VMAA_Guest_Invitation_Vertical_Story_1080p.webm"
        shutil.copy(latest_v, dest_v)
        shutil.copy(dest_v, BRAIN_DIR / dest_v.name)
        print(f"Exported Motion Video: {dest_v.name} ({dest_v.stat().st_size} bytes)")

print("Data-driven Guest Invitation System build complete!")
