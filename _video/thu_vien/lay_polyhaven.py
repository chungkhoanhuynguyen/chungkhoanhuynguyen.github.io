# Tải tài nguyên CC0 của Poly Haven (polyhaven.com): HDRI bầu trời (ánh sáng sáng/chiều/tối/mây), mô hình, vật liệu.
import json, os, sys, urllib.request, time
OUT = sys.argv[1]; NG = json.load(open(os.path.join(os.path.dirname(__file__), "nguon.json")))["polyhaven"]
UA = {"User-Agent": "thu-vien-3d HuyNguyen"}
def get(u, raw=False):
    for i in range(3):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
            return r if raw else json.loads(r)
        except Exception as e: err = e; time.sleep(3)
    raise err
def luu(u, p):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if not os.path.exists(p): open(p, "wb").write(get(u, raw=True))
bao = []
for t, n in (("hdris", NG["hdris"]), ("models", NG["models"]), ("textures", NG["textures"])):
    A = get(f"https://api.polyhaven.com/assets?t={t}")
    ds = sorted(A.items(), key=lambda kv: -kv[1].get("download_count", 0))[:n]
    for aid, meta in ds:
        try:
            f = get(f"https://api.polyhaven.com/files/{aid}")
            if t == "hdris":
                u = f["hdri"]["2k"]["hdr"]["url"]; luu(u, f"{OUT}/polyhaven/hdris/{aid}.hdr")
            elif t == "models":
                g = f["gltf"]["1k"]["gltf"]; luu(g["url"], f"{OUT}/polyhaven/models/{aid}/{aid}.gltf")
                for rel, inc in g.get("include", {}).items(): luu(inc["url"], f"{OUT}/polyhaven/models/{aid}/{rel}")
            else:
                for m in ("Diffuse", "nor_gl", "Rough"):
                    k = f.get(m, {}).get("1k", {}).get("jpg")
                    if k: luu(k["url"], f"{OUT}/polyhaven/textures/{aid}/{m}.jpg")
            bao.append(dict(id=aid, loai=t, ten=meta.get("name"), nhom=meta.get("categories"), the=meta.get("tags"), nguon=f"https://polyhaven.com/a/{aid}", giay_phep="CC0"))
        except Exception as e: print("LOI", t, aid, e, flush=True)
    print("XONG", t, sum(1 for b in bao if b["loai"] == t), flush=True)
json.dump(bao, open(f"{OUT}/polyhaven_bao_cao.json", "w"), ensure_ascii=False, indent=1)
