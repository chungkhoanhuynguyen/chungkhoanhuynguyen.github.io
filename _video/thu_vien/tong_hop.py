# Gộp danh mục + làm bảng ảnh xem trước theo từng gói (để duyệt nhanh)
import json, os, sys
from PIL import Image, ImageDraw, ImageFont
W, ANH, OUT = sys.argv[1], sys.argv[2], sys.argv[3]; os.makedirs(OUT, exist_ok=True)
cat = json.load(open(os.path.join(ANH, "_catalog.json")))
kb = {x["goi"]: x for x in json.load(open(os.path.join(W, "kenney_bao_cao.json"))) if "loi" not in x}
ph = {x["id"]: x for x in json.load(open(os.path.join(W, "polyhaven_bao_cao.json")))}
for x in cat:
    p = x["tep"].split(os.sep)
    if p[0] == "polyhaven": x.update(nguon="Poly Haven", goi="polyhaven-" + p[1], giay_phep="CC0", trang=ph.get(p[2], {}).get("nguon"), the=ph.get(p[2], {}).get("the"))
    else: x.update(nguon="Kenney", goi=p[1], giay_phep="CC0", trang=f"https://kenney.nl/assets/{p[1]}")
am = []
for loai in ("kenney_audio",):
    for r, _, fs in os.walk(os.path.join(W, loai)):
        for f in fs:
            if f.lower().endswith((".ogg", ".wav", ".mp3")): am.append(dict(tep=os.path.relpath(os.path.join(r, f), W), goi=os.path.relpath(r, W).split(os.sep)[1], nguon="Kenney", giay_phep="CC0"))
hd = [dict(tep=f"polyhaven/hdris/{x['id']}.hdr", ten=x["ten"], nhom=x["nhom"], trang=x["nguon"], giay_phep="CC0") for x in ph.values() if x["loai"] == "hdris"]
vl = [dict(tep=f"polyhaven/textures/{x['id']}", ten=x["ten"], nhom=x["nhom"], trang=x["nguon"], giay_phep="CC0") for x in ph.values() if x["loai"] == "textures"]
json.dump(dict(mo_hinh=cat, am_thanh=am, bau_troi_hdri=hd, vat_lieu=vl), open(os.path.join(OUT, "catalog.json"), "w"), ensure_ascii=False, indent=1)
try: ft = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
except Exception: ft = ImageFont.load_default()
goi = {}
for x in cat: goi.setdefault(x["goi"], []).append(x)
tom = []
for g, ds in sorted(goi.items()):
    for k in range(0, len(ds), 48):
        part = ds[k:k + 48]; cols = 8; rows = (len(part) + cols - 1) // cols; S = 200
        im = Image.new("RGB", (cols * S, rows * (S + 18)), (28, 12, 60)); d = ImageDraw.Draw(im)
        for i, x in enumerate(part):
            try: t = Image.open(os.path.join(ANH, x["anh"])).resize((S, S))
            except Exception: continue
            X, Y = (i % cols) * S, (i // cols) * (S + 18); im.paste(t, (X, Y)); d.text((X + 4, Y + S + 2), os.path.basename(x["tep"]).rsplit(".", 1)[0][:30], fill=(255, 210, 63), font=ft)
        f = f"{g}_{k // 48 + 1}.jpg"; im.save(os.path.join(OUT, f), quality=82); tom.append(f)
print("mo hinh", len(cat), "| am thanh", len(am), "| hdri", len(hd), "| vat lieu", len(vl), "| bang anh", len(tom))
json.dump(dict(so_mo_hinh=len(cat), so_am_thanh=len(am), so_hdri=len(hd), so_vat_lieu=len(vl), goi={g: len(v) for g, v in goi.items()}, bang_anh=tom), open(os.path.join(OUT, "tom_tat.json"), "w"), ensure_ascii=False, indent=1)
