import urllib.request
import re

url = "https://docs.google.com/spreadsheets/d/1U5KbAfdX0ycptc3Hy1plXbY4IXZnZMzYU4zLFuj-U4Q/htmlview"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8", errors="ignore")

tabs = re.findall(r'id="sheet-button-([^"]+)"[^>]*><a[^>]*>([^<]+)</a>', html)
print("Sheet tabs found:", tabs)

# Download each sheet as CSV or table
for gid, name in tabs:
    csv_url = f"https://docs.google.com/spreadsheets/d/1U5KbAfdX0ycptc3Hy1plXbY4IXZnZMzYU4zLFuj-U4Q/export?format=csv&gid={gid}"
    try:
        content = urllib.request.urlopen(csv_url).read().decode("utf-8", errors="ignore")
        safe_name = "".join(c for c in name if c.isalnum() or c in (" ", "_", "-")).strip()
        filename = f"assets/sheet_{gid}_{safe_name}.csv"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"Error fetching gid {gid}: {e}")
