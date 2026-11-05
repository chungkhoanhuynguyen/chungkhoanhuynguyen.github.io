# Ảnh bìa YouTube ĐỒNG BỘ cho mọi video dài (anh Huy chốt 5/11): nền tím đậm, CHỮ TO IN HOA trái
# (trắng / vàng xen kẽ), nhãn đỏ có con số, ảnh thật bên phải mờ dần, logo HUY NGUYỄN góc phải trên.
# Dùng trong render.py (make) hoặc chạy riêng: python3 _video/bia.py <lô> [KEY ...] -> _video/out/<KEY>_bia.png
import os, re, sys, json
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "engine"))
import dx2
W, H = 1280, 720
TIM0, TIM1 = (24, 12, 40), (58, 24, 88)
VANG = (255, 204, 0); TRANG = (255, 255, 255); DO = (226, 46, 46)
SO = re.compile(r"[-+−]?\d[\d.,]*\s?(?:%|lần|tỷ|nghìn tỷ|triệu|điểm|năm|bảng|x)", re.I)

def _lines(sc, meta):
    L = meta.get("bia") or sc.get("cap") or ()
    if isinstance(L, str): L = L.split("\n")
    L = [str(x).strip().upper() for x in L if str(x).strip()]
    if not L: L = [str(meta.get("title", "")).split(":")[0].upper()[:36]]
    return L[:3]

def _badge(sc, meta, L):
    b = meta.get("badge")
    if b: return str(b).upper()
    joined = " ".join(L)
    for src in (sc.get("label", ""), meta.get("title", ""), sc.get("say", "")):
        for m in SO.finditer(str(src)):
            t = m.group(0).strip()
            if t not in joined: return t.upper()
    return ""

def _fit(d, s, mw, st, mn=64):
    while st > mn and d.textlength(s, font=dx2.F("Black", st)) > mw: st -= 4
    return dx2.F("Black", st)

def _size(d, L, mw):
    st = 156 if len(L) <= 2 else 128
    while st > 60 and (max(d.textlength(l, font=dx2.F("Black", st)) for l in L) > mw or len(L)*st*1.08 > 400): st -= 4
    return st

def _wrap(d, L, mw):
    # giữ ngắt dòng gốc nếu chữ đủ to (>=112), không thì chia lại từ thành 2–3 dòng cho chữ to nhất
    best = (L, _size(d, L, mw))
    if best[1] >= 112: return best
    w = [x for x in " ".join(L).split() if x not in ("·", "-", "–", "|")]
    for n in (2, 3):
        if len(w) < n: continue
        import itertools
        for cut in itertools.combinations(range(1, len(w)), n-1):
            idx = (0,) + cut + (len(w),); c = [" ".join(w[idx[i]:idx[i+1]]) for i in range(n)]
            st = _size(d, c, mw)
            if st > best[1]: best = (c, st)
    return best

def _nen_chart(im, seed, up):
    # biểu đồ nến cách điệu phát sáng phía sau (luôn có, kể cả khi thiếu ảnh)
    import random
    r = random.Random(seed); lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dd = ImageDraw.Draw(lay)
    for gx in range(0, W, 80): dd.line([(gx, 0), (gx, H)], fill=(255, 255, 255, 10))
    for gy in range(0, H, 80): dd.line([(0, gy), (W, gy)], fill=(255, 255, 255, 10))
    n = 34; x0 = 420; step = (W - x0 - 20) / n; v = 0.55; pts = []
    for i in range(n):
        drift = (-0.012 if up else 0.012); o = v; c = min(0.85, max(0.15, v + drift + r.uniform(-0.05, 0.05)))
        hi = max(o, c) + r.uniform(0, 0.03); lo = min(o, c) - r.uniform(0, 0.03)
        X = x0 + i*step; Y = lambda q: int(H*q)
        col = (46, 204, 113, 120) if c < o else (231, 76, 60, 120)
        dd.line([(X+step*0.35, Y(hi)), (X+step*0.35, Y(lo))], fill=col, width=2)
        dd.rectangle([X+step*0.1, Y(min(o, c)), X+step*0.6, Y(max(o, c))+2], fill=col)
        pts.append((X+step*0.35, Y(c))); v = c
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); gd = ImageDraw.Draw(glow)
    gd.line(pts, fill=(255, 204, 0, 200), width=8); glow = glow.filter(ImageFilter.GaussianBlur(10))
    lay.alpha_composite(glow); ImageDraw.Draw(lay).line(pts, fill=(255, 220, 90, 230), width=3)
    im.paste(lay, (0, 0), lay)

def _sticker(pt, w=7):
    # anh Huy 6/11 00:14: bỏ viền trắng dày -> viền sáng mảnh (rim light) tím thương hiệu (anh Huy 00:23) + bóng đổ mềm, chân dung tự nhiên
    a = pt.getchannel("A"); pad = 30
    W2, H2 = pt.width + pad*2, pt.height + pad
    A = Image.new("L", (W2, H2)); A.paste(a, (pad, pad))
    out = Image.new("RGBA", (W2, H2), (0, 0, 0, 0))
    sh = A.filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v*0.75))  # bóng đổ
    s_ = Image.new("RGBA", (W2, H2), (8, 4, 18, 0)); s_.putalpha(sh)
    out.alpha_composite(s_, (10, 4))
    rim = A.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(3)).point(lambda v: int(v*0.85))  # viền sáng 2-3px
    r_ = Image.new("RGBA", (W2, H2), (196, 140, 255, 0)); r_.putalpha(rim)
    out.alpha_composite(r_)
    body = Image.new("RGBA", (W2, H2), (0, 0, 0, 0)); body.paste(pt, (pad, pad)); out.alpha_composite(body)
    # cắt đáy phẳng, không lộ hiệu ứng ở mép dưới
    return out.crop((0, 0, W2, H2))

def _arrow(d, x, y, up, s=1.0):
    col = (46, 204, 113) if up else (231, 76, 60)
    if up: pts = [(x, y+60*s), (x+40*s, y), (x+80*s, y+60*s), (x+55*s, y+60*s), (x+55*s, y+110*s), (x+25*s, y+110*s), (x+25*s, y+60*s)]
    else: pts = [(x, y+50*s), (x+40*s, y+110*s), (x+80*s, y+50*s), (x+55*s, y+50*s), (x+55*s, y), (x+25*s, y), (x+25*s, y+50*s)]
    d.polygon(pts, fill=col, outline=(0, 0, 0))

def make(sc, meta=None, ph=None, out=None):
    meta = meta or {}
    im = Image.new("RGB", (W, H), TIM0); d = ImageDraw.Draw(im)
    for y in range(H):  # nền chuyển tím
        a = y / H; d.line([(0, y), (W, y)], fill=tuple(int(TIM0[i] + (TIM1[i]-TIM0[i])*a) for i in range(3)))
    if ph is not None:  # ảnh minh hoạ thật bên phải, mờ dần sang trái
        pw = 620; r = max(pw/ph.width, H/ph.height); p = ph.convert("RGB").resize((int(ph.width*r)+1, int(ph.height*r)+1), Image.LANCZOS)
        p = p.crop(((p.width-pw)//2, (p.height-H)//2, (p.width-pw)//2+pw, (p.height-H)//2+H))
        p = Image.blend(p, Image.new("RGB", p.size, TIM0), 0.25)
        m = Image.new("L", (pw, H))
        for x in range(pw): ImageDraw.Draw(m).line([(x, 0), (x, H)], fill=int(255*min(1, x/260)))
        im.paste(p, (W-pw, 0), m); d = ImageDraw.Draw(im)
    _txt = " ".join(_lines(sc, meta)) + " " + str(meta.get("badge") or sc.get("label") or "")
    _up = not re.search(r"(^|\s)[-−]\d|GIẢM|SẬP|LỖ|MẤT|BONG BÓNG|CÒN \d|SAI|BẪY|CHÁY", _txt.upper())
    _nen_chart(im, hash(_txt) & 0xffff, _up); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 14, H], fill=VANG)
    CK = os.path.join(HERE, "engine", "chu_kenh.png")
    if os.path.exists(CK):  # chân dung tách nền, nhỏ vừa ở góc phải dưới (anh Huy 5/11 23:41), nền là ảnh minh hoạ
        pt = Image.open(CK).convert("RGBA"); ph_ = 480; pt = pt.resize((int(pt.width*ph_/pt.height), ph_), Image.LANCZOS)
        a_ = pt.getchannel("A"); rm = Image.new("L", pt.size, 255)
        for x in range(70): ImageDraw.Draw(rm).line([(x, 0), (x, pt.height)], fill=int(255*x/70))
        pt = _sticker(pt)  # ảnh gốc nét, đủ 2 vai -> không làm mờ mép
        px_ = W - pt.width + 6
        gl = Image.new("L", (W, H)); ImageDraw.Draw(gl).ellipse([px_+30, H-ph_-20, px_+pt.width, H+150], fill=170)
        gl = gl.filter(ImageFilter.GaussianBlur(50)); im.paste(Image.new("RGB", (W, H), (20, 10, 34)), (0, 0), gl)
        im.paste(pt, (px_, H - pt.height), pt); d = ImageDraw.Draw(im)
        fl = dx2.F("Black", 30); d.text((60, 30), "HUY NGUYỄN", font=fl, fill=TRANG)
        d.text((60 + d.textlength("HUY NGUYỄN ", font=fl), 36), "CHỨNG KHOÁN", font=dx2.F("SemiBold", 22), fill=VANG)
        fu = dx2.F("Bold", 30); u = "chungkhoanhuynguyen.com"
        d.rounded_rectangle([50, H-78, 50 + d.textlength(u, font=fu) + 32, H-28], 12, fill=(0, 0, 0))
        d.text((66, H-74), u, font=fu, fill=VANG)
        MW = 720
    else:
        try: dx2.brand(im, d, W-170, 30, 0.62, 1.0, TIM0)
        except Exception: d.text((W-280, 34), "HUY NGUYỄN", font=dx2.F("Black", 34), fill=TRANG)
        MW = 740
    L = _lines(sc, meta); x0, mw = 60, MW
    L, st = _wrap(d, L, mw); fs = [dx2.F("Black", st) for _ in L]
    hh = sum(int(f.size*1.08) for f in fs) + (60 if len(fs) >= 2 else 0); y = max(96, (H - hh)//2 - 70)
    cols = [TRANG, VANG, TRANG]
    for i, (l, f) in enumerate(zip(L, fs)):
        if i == 1 and len(L) >= 2:  # dòng nhấn: chữ đen trên dải vàng
            y += 34; tw = d.textlength(l, font=f); bb = d.textbbox((x0, y), l, font=f)
            d.rounded_rectangle([x0-14, bb[1]-12, x0+tw+14, bb[3]+14], 10, fill=VANG)
            d.text((x0, y), l, font=f, fill=(15, 10, 25)); y += int(f.size*1.08) + 22; continue
        for dx, dy in ((5, 6), (3, 3)): d.text((x0+dx, y+dy), l, font=f, fill=(0, 0, 0))  # bóng chữ
        d.text((x0, y), l, font=f, fill=TRANG); y += int(f.size*1.08)
    b = _badge(sc, meta, L)
    if b:
        fb = dx2.F("Black", 54); tw = d.textlength(b, font=fb); y += 18
        d.rounded_rectangle([x0, y, x0+tw+48, y+82], 14, fill=DO); d.text((x0+24, y+8), b, font=fb, fill=TRANG)
        _arrow(d, x0+tw+66, y+2, not b.strip().startswith(("-", "−")), 0.72)
    if out: im.save(out)
    return im

if __name__ == "__main__":
    lo = sys.argv[1]; keys = sys.argv[2:]
    sys.path.insert(0, HERE); import anh
    g = {"__name__": "kb"}; exec(open(os.path.join(HERE, "queue", lo, "video_dai.py"), encoding="utf-8").read(), g)
    S = g["S"]; META = g.get("META", {}) if isinstance(g.get("META"), dict) else {}
    od = os.path.join(HERE, "out"); os.makedirs(od, exist_ok=True)
    kho = anh.Kho("/tmp/anh_bia")
    for k in (keys or list(S)):
        raw = S[k]; sc = dict(raw[0]); mt = META.get(k, {})
        try:
            _mj = json.load(open(os.path.join(HERE, "queue", lo, "meta.json"), encoding="utf-8")).get(k, {})
            if not mt.get("bia"): mt = dict(mt, bia=_mj.get("bia_hook") or _mj.get("bia"), title=mt.get("title") or _mj.get("tieu_de", ""))
        except Exception: pass
        if isinstance(sc.get("cap"), str): sc["cap"] = tuple(sc["cap"].split("\n"))
        ph = None
        for s in raw[:4]:
            try: ph = kho.cho(dict(s), mt.get("title", ""))
            except Exception: ph = None
            if ph is not None: break
        make(sc, mt, ph, os.path.join(od, k + "_bia.png")); print("bia", k, flush=True)
