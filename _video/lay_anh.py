# Tải ảnh Wikimedia Commons theo danh sách (chạy trên GitHub Actions vì máy đám mây bị giới hạn 429).
# Dùng: python3 lay_anh.py <file.json [[ten, truy_van], ...]> <thu_muc_ra>
import json, sys, os, time, urllib.request, urllib.parse
UA = {"User-Agent": "HuyNguyenVideoBot/1.0 (chungkhoanhuynguyen.com)"}
def get(u):
    for k in range(5):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
        except Exception as e: print("thu lai", e, flush=True); time.sleep(5 * (k + 1))
    raise RuntimeError(u)
L = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True); cred = {}
for ten, q in L:
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(dict(action="query", format="json", generator="search", gsrsearch=q + " filetype:bitmap", gsrnamespace=6, gsrlimit=12, prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=1920))
    d = json.loads(get(u)); ps = sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0)); ok = 0
    for p in ps:
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {}); lic = m.get("LicenseShortName", {}).get("value", "")
        if ii["width"] < 1400 or ii["width"] < ii["height"] * 1.2 or not any(x in lic for x in ("CC", "Public", "PD")): continue
        open(f"{out}/{ten}.jpg", "wb").write(get(ii["thumburl"])); cred[ten] = {"title": p["title"], "license": lic, "artist": m.get("Artist", {}).get("value", "")[:120]}
        print("OK", ten, p["title"], lic, flush=True); ok = 1; break
    if not ok: print("KHONG CO", ten, q, flush=True)
    time.sleep(2)
json.dump(cred, open(f"{out}/credits.json", "w"), ensure_ascii=False, indent=1)
