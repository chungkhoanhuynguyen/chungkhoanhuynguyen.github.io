# Tải các gói CC0 của Kenney (kenney.nl) – giấy phép CC0, dùng thương mại không cần ghi công. Ghi nguồn vào catalog.
import json, os, re, sys, zipfile, urllib.request, io, time
OUT = sys.argv[1]; NG = json.load(open(os.path.join(os.path.dirname(__file__), "nguon.json")))
UA = {"User-Agent": "Mozilla/5.0 (thu-vien-3d HuyNguyen)"}
def get(u, raw=False):
    for i in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
            return r if raw else r.decode("utf-8", "ignore")
        except Exception as e: err = e; time.sleep(3)
    raise err
bao = []
if os.environ.get("NHANH"): NG = {"kenney_3d": NG["kenney_3d"][:2], "kenney_audio": NG["kenney_audio"][:1]}
for loai in ("kenney_3d", "kenney_audio"):
    for slug in NG[loai]:
        try:
            h = get(f"https://kenney.nl/assets/{slug}")
            z = re.findall(r'href="([^"]+\.zip)"', h) or re.findall(r'(https?://[^"\' <>]+\.zip)', h) or re.findall(r'(/media/[^"\' <>]+\.zip)', h)
            if not z:
                bao.append(dict(goi=slug, loi="khong thay zip")); print("KHONG ZIP", slug, len(h))
                if slug == NG[loai][0]:
                    for m in re.finditer(r"(?i)download", h): print("  ...", h[max(0, m.start()-200):m.start()+200].replace("\n", " "))
                continue
            u = z[0] if z[0].startswith("http") else "https://kenney.nl" + z[0]
            b = get(u, raw=True); d = os.path.join(OUT, loai, slug); os.makedirs(d, exist_ok=True)
            zipfile.ZipFile(io.BytesIO(b)).extractall(d)
            dem = {}
            for r, _, fs in os.walk(d):
                for f in fs: e = f.rsplit(".", 1)[-1].lower(); dem[e] = dem.get(e, 0) + 1
            bao.append(dict(goi=slug, loai=loai, url=u, mb=round(len(b) / 1e6, 1), tep=dem)); print("OK", slug, round(len(b) / 1e6, 1), "MB", {k: v for k, v in dem.items() if k in ("glb", "gltf", "fbx", "obj", "ogg", "wav", "mp3")}, flush=True)
        except Exception as e: bao.append(dict(goi=slug, loi=repr(e)[:200])); print("LOI", slug, e, flush=True)
json.dump(bao, open(os.path.join(OUT, "kenney_bao_cao.json"), "w"), ensure_ascii=False, indent=1)
