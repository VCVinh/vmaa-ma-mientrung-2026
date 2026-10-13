import base64
import re
from pathlib import Path

ROOT = Path(r"C:\Users\Admin\.gemini\antigravity\scratch\vmaa-ma-mientrung-2026")
clean_b64 = base64.b64encode((ROOT / "assets" / "plates" / "clean_thap_sang_master_4k.png").read_bytes()).decode("ascii")
clean_data_uri = f"data:image/png;base64,{clean_b64}"

targets = [
    ROOT / "exports" / "v2_production" / "KV_v2_Landscape_1920x1080_VI.html",
    ROOT / "exports" / "v2_production" / "KV_v2_Landscape_1920x1080_EN.html",
    ROOT / "exports" / "v2_production" / "stage_venue" / "KV_v2_Curved_Stage_32x9_VI.html",
    ROOT / "exports" / "v2_production" / "stage_venue" / "KV_v2_Curved_Stage_32x9_EN.html",
]

for t in targets:
    if not t.exists():
        print(f"Skipping {t}, does not exist")
        continue
    txt = t.read_text(encoding="utf-8")
    new_txt = re.sub(
        r"background-image:\s*url\('data:image/png;base64,[A-Za-z0-9+/=]+'\);",
        f"background-image: url('{clean_data_uri}');",
        txt
    )
    # Also clean up any lingering unused .dragon-layer or .dragon-bridge-layer CSS rules
    new_txt = re.sub(
        r"\.dragon-layer\s*\{[^}]*\}",
        "",
        new_txt
    )
    new_txt = re.sub(
        r"\.dragon-bridge-layer\s*\{[^}]*\}",
        "",
        new_txt
    )
    t.write_text(new_txt, encoding="utf-8")
    print(f"Updated {t.name} with clean background plate!")
