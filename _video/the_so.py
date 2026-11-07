# Thẻ số liệu CHẠY (animation) cho reel dọc: cột mọc lên, số đếm lên, dòng hiện lần lượt.
# spec trong reel.json: "the": {"loai": "cot"|"thang"|"lon", "tieu": "...", "nguon": "...", ...}
#   cot:   "hang": [[nhãn, giá trị], ...], "noi": [chỉ số tô vàng], "dv": "%", "max": 11
#   thang: "hang": [[nhãn, giá trị, "tim"|"tim2"|"vang"], ...], "dv": " USD"
#   lon:   "dong": [[chữ, cỡ, "vang"|"trang"|"tim2"|"do"], ...]
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "engine"))
from PIL import Image, ImageDraw
import dx2
F = dx2.F; ease = dx2.ease
W, H = 1008, 860
BG = (24, 12, 44); MAU = {"tim": (124, 58, 237), "tim2": (196, 140, 255), "vang": (255, 214, 64), "trang": (255, 255, 255), "do": (255, 107, 107)}
MO = (170, 160, 200)

def so(v, dv="", nd=None):
    if nd is None: nd = 0 if abs(v) >= 100 else 2
    s = f"{v:,.{nd}f}".replace(",", "§").replace(".", ",").replace("§", ".")
    return s + dv

def nen(sp, t):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, W - 6, H - 6], 36, outline=(90, 50, 150), width=4)
    a = ease(t / 0.4)
    d.text((W / 2, 50 + (1 - a) * 20), sp.get("tieu", ""), font=F("ExtraBold", 44), fill=tuple(int(c * a + 24 * (1 - a)) for c in MAU["tim2"]), anchor="ma")
    if sp.get("nguon"): d.text((W / 2, H - 58), "Nguồn: " + sp["nguon"], font=F("Medium", 26), fill=MO, anchor="ma")
    return im, d

def cot(sp, t):
    im, d = nen(sp, t); rows = sp["hang"]; n = len(rows); mx = sp.get("max") or max(v for _, v in rows) * 1.15
    x0, x1 = 110, W - 110; bw = (x1 - x0) / n; yb = H - 150; top = 200; hl = set(sp.get("noi", []))
    for i, (lab, v) in enumerate(rows):
        a = ease((t - 0.3 - i * 0.35) / 0.9)
        h = (yb - top) * v / mx * a; cx = x0 + bw * i + bw / 2; c = MAU["vang"] if i in hl else MAU["tim"]
        if a > 0: d.rounded_rectangle([cx - bw * 0.32, yb - max(h, 4), cx + bw * 0.32, yb], 14, fill=c)
        d.text((cx, yb + 16), lab, font=F("Bold", 32), fill=MO, anchor="ma")
        if a > 0.05: d.text((cx, yb - h - 62), so(v * a, sp.get("dv", "")), font=F("Black", 46), fill=MAU["trang"], anchor="ma")
    return im

def thang(sp, t):
    im, d = nen(sp, t); rows = sp["hang"]; mx = max(r[1] for r in rows); n = len(rows)
    y = 200 + (3 - n) * 95
    for i, (lab, v, c) in enumerate(rows):
        a = ease((t - 0.3 - i * 0.7) / 1.0)
        if a <= 0: y += 190; continue
        d.text((70, y), lab, font=F("Bold", 34), fill=MO)
        w = max(18, (W - 140) * v / mx * a); col = MAU.get(c, MAU["tim"])
        d.rounded_rectangle([70, y + 50, 70 + w, y + 130], 18, fill=col)
        s = so(v * a, sp.get("dv", " USD"), 0); fs = F("Black", 48)
        if w < d.textlength(s, font=fs) + 50: d.text((70 + w + 20, y + 64), s, font=fs, fill=MAU["trang"])
        else: d.text((90, y + 64), s, font=fs, fill=(20, 10, 30) if c == "vang" else MAU["trang"])
        y += 190
    return im

def lon(sp, t):
    im, d = nen(sp, t); y = 220
    for i, (s, sz, c) in enumerate(sp["dong"]):
        a = ease((t - 0.3 - i * 0.55) / 0.5)
        if a > 0:
            col = tuple(int(x * a + 24 * (1 - a)) for x in MAU.get(c, MAU["trang"]))
            d.text((W / 2, y + (1 - a) * 30), s, font=F("Black", sz), fill=col, anchor="ma")
        y += int(sz * 1.35)
    return im

def ve(sp, t):
    return {"cot": cot, "thang": thang, "lon": lon}[sp.get("loai", "lon")](sp, t)
