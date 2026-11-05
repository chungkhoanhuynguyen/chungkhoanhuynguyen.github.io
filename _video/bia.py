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
    while st > 60 and (max(d.textlength(l, font=dx2.F("Black", st)) for l in L) > mw or len(L)*st*1.08 > 480): st -= 4
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
    d.rectangle([0, 0, 14, H], fill=VANG)
    CK = os.path.join(HERE, "engine", "chu_kenh.png")
    if os.path.exists(CK):  # mặt chủ kênh NHỎ ở góc (anh Huy 5/11 23:39: không để to)
        pt = Image.open(CK).convert("RGBA"); D_ = 210
        sq = pt.crop((int(pt.width*0.12), int(pt.height*0.02), int(pt.width*0.88), int(pt.height*0.02) + int(pt.width*0.76))).resize((D_, D_), Image.LANCZOS)
        bgc = Image.new("RGBA", (D_, D_), (58, 24, 88, 255)); bgc.alpha_composite(sq)
        cm = Image.new("L", (D_, D_)); ImageDraw.Draw(cm).ellipse([0, 0, D_-1, D_-1], fill=255)
        cx_, cy_ = W - D_ - 36, H - D_ - 36
        ImageDraw.Draw(im).ellipse([cx_-7, cy_-7, cx_+D_+6, cy_+D_+6], fill=VANG)
        im.paste(bgc.convert("RGB"), (cx_, cy_), cm); d = ImageDraw.Draw(im)
        fl = dx2.F("Black", 30); d.text((60, 30), "HUY NGUYỄN", font=fl, fill=TRANG)
        d.text((60 + d.textlength("HUY NGUYỄN ", font=fl), 36), "CHỨNG KHOÁN", font=dx2.F("SemiBold", 22), fill=VANG)
        fu = dx2.F("Bold", 30); u = "chungkhoanhuynguyen.com"
        d.rounded_rectangle([50, H-78, 50 + d.textlength(u, font=fu) + 32, H-28], 12, fill=(0, 0, 0))
        d.text((66, H-74), u, font=fu, fill=VANG)
        MW = 740
    else:
        try: dx2.brand(im, d, W-170, 30, 0.62, 1.0, TIM0)
        except Exception: d.text((W-280, 34), "HUY NGUYỄN", font=dx2.F("Black", 34), fill=TRANG)
        MW = 740
    L = _lines(sc, meta); x0, mw = 60, MW
    L, st = _wrap(d, L, mw); fs = [dx2.F("Black", st) for _ in L]
    hh = sum(int(f.size*1.08) for f in fs); y = max(70, (H - hh)//2 - 40)
    cols = [TRANG, VANG, TRANG]
    for i, (l, f) in enumerate(zip(L, fs)):
        for dx, dy in ((5, 6), (3, 3)): d.text((x0+dx, y+dy), l, font=f, fill=(0, 0, 0))  # bóng chữ
        d.text((x0, y), l, font=f, fill=cols[i % 3]); y += int(f.size*1.08)
    b = _badge(sc, meta, L)
    if b:
        fb = dx2.F("Black", 54); tw = d.textlength(b, font=fb); y += 18
        d.rounded_rectangle([x0, y, x0+tw+48, y+82], 14, fill=DO); d.text((x0+24, y+8), b, font=fb, fill=TRANG)
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
