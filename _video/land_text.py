# Cảnh chữ cho VIDEO NGANG YouTube (thay kiểu "cột dọc giữa màn hình" bị anh Huy chê 7/11):
# - ảnh thật tràn toàn khung, chuyển động Ken Burns (zoom/lia chậm), cắt cảnh mỗi ~7 giây đổi góc máy
# - tiêu đề lớn canh trái, nhãn chương vàng, vạch nhấn; phụ đề dưới đáy do render.py vẽ
# - không có ảnh: nền tối chuyển động nhẹ + chữ lớn giữa khung (cảnh CTA/kết)
import math
from PIL import Image, ImageDraw, ImageFilter
import dx2

LW, LH = 1920, 1080
SHOT = 7.0           # giây mỗi góc máy
_GR = {}

def _grad():
    if "g" not in _GR:
        a = Image.new("L", (LW, LH), 0); px = a.load()
        for x in range(LW):
            v = int(240 * min(1.0, max(0.0, 1.25 - x / (LW * 0.62))) ** 0.85)   # vùng chữ bên trái tối đủ để đọc trên mọi ảnh
            for y in range(0, LH, 1): px[x, y] = v
        b = Image.new("L", (LW, LH), 0); d = ImageDraw.Draw(b)
        for y in range(LH - 300, LH): d.line([0, y, LW, y], fill=int(210 * ((y - (LH - 300)) / 300) ** 1.4))
        top = Image.new("L", (LW, LH), 0); d = ImageDraw.Draw(top)
        for y in range(0, 140): d.line([0, y, LW, y], fill=int(150 * (1 - y / 140)))
        m = Image.fromarray(__import__("numpy").maximum(__import__("numpy").maximum(
            __import__("numpy").asarray(a), __import__("numpy").asarray(b)), __import__("numpy").asarray(top)))
        _GR["g"] = Image.composite(Image.new("RGB", (LW, LH), (6, 8, 12)), Image.new("RGB", (LW, LH), (0, 0, 0)), m), m
    return _GR["g"]

def prep(sc, phs):
    # mỗi ảnh nền phủ 1,25 lần khung để có chỗ zoom/lia; nhiều ảnh -> mỗi góc máy một ảnh
    if not isinstance(phs, (list, tuple)): phs = [phs]
    L = []
    for ph in phs:
        r = max(LW * 1.25 / ph.width, LH * 1.25 / ph.height)
        L.append(ph.convert("RGB").resize((int(ph.width * r) + 2, int(ph.height * r) + 2), Image.LANCZOS))
    if L: sc["_kb"] = L

def _shot_bg(sc, t):
    s = int(t // SHOT); u = (t % SHOT) / SHOT; B = sc["_kb"][s % len(sc["_kb"])]
    # góc máy xen kẽ: rộng zoom vào / cận lia ngang / rộng zoom ra
    kind = s % 3
    if kind == 0: z = 1.0 + 0.10 * u; cx, cy = 0.5, 0.5
    elif kind == 1: z = 1.22; cx, cy = 0.62 - 0.14 * u, 0.45
    else: z = 1.12 - 0.10 * u; cx, cy = 0.42 + 0.06 * u, 0.55
    vw, vh = B.width / 1.25 / z * 1.0, B.height / 1.25 / z
    vw = min(vw, B.width); vh = min(vh, B.height)
    x0 = min(max(0, cx * B.width - vw / 2), B.width - vw); y0 = min(max(0, cy * B.height - vh / 2), B.height - vh)
    im = B.crop((int(x0), int(y0), int(x0 + vw), int(y0 + vh))).resize((LW, LH), Image.BILINEAR)
    dark, m = _grad()
    return Image.composite(dark, im, m)

_BGN = {}
def _plain_bg(t):
    k = int(t * 6) % 48
    if k not in _BGN:
        g = Image.new("RGB", (LW, LH), (11, 13, 19)); d = ImageDraw.Draw(g)
        ang = k / 48 * 2 * math.pi
        for r, c in ((820, (20, 24, 34)), (520, (26, 31, 44)), (260, (34, 38, 52))):
            x = LW * 0.5 + 160 * math.cos(ang); y = LH * 0.45 + 90 * math.sin(ang)
            d.ellipse([x - r, y - r, x + r, y + r], fill=c)
        _BGN[k] = g.filter(ImageFilter.GaussianBlur(150))
    return _BGN[k].copy()

def _tag(sc):
    ch = (sc.get("ch") or sc.get("label") or "").strip()
    for sep in (" – ", " - ", ": "):
        if sep in ch and ch.split(sep)[0].lower().startswith(("chương", "câu", "mở đầu", "phần")):
            return ch.split(sep)[0].upper() + "  ·  " + sep.join(ch.split(sep)[1:]).upper()
    return ch.upper()

# ===== THẺ DỮ KIỆN bên phải (anh Huy 7/11: "tài liệu trên video hơi ít, giống nghe audio") =====
# sc["the"] = [{"f":0.0,"so":"1.3 tỷ $","nhan":"Berkshire mua Coca-Cola 1988"}, {"f":0.5,"trich":"...","ai":"Munger"}, {"f":0.7,"ds":["a","b"]}]
def _the(im, sc, t):
    L = sc.get("the") or []
    T = sc.get("_T") or 30.0
    if not L: return
    cur = None; nxt_f = 2.0
    for i, c in enumerate(L):
        if t >= c.get("f", 0) * T: cur = (i, c); nxt_f = L[i + 1].get("f", 2) if i + 1 < len(L) else 2.0
    if not cur: return
    i, c = cur; t0 = c.get("f", 0) * T; te = min(T, nxt_f * T)
    a = dx2.ease((t - t0) / 0.45) * (1 - dx2.ease((t - (te - 0.35)) / 0.35) if te - t < 0.35 else 1)
    if a <= 0.01: return
    d = ImageDraw.Draw(im, "RGBA")
    x0, w = 1110, 700; y0 = 250 + int((1 - a) * 40)
    if "so" in c:
        f1 = dx2.fit(d, c["so"], "Black", w - 80, 120); f2 = dx2.F("SemiBold", 34)
        nh = _wrap(d, c.get("nhan", ""), f2, w - 80)
        h = 70 + f1.size + 20 + len(nh) * 44 + 30
        d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 22, fill=(12, 14, 20, int(225 * a)), outline=(*dx2.GOLD, int(255 * a)), width=3)
        d.text((x0 + 40, y0 + 40), c["so"], font=f1, fill=(*dx2.GOLD, int(255 * a)))
        y = y0 + 60 + f1.size
        for l in nh: d.text((x0 + 40, y), l, font=f2, fill=(235, 238, 245, int(255 * a))); y += 44
    elif "trich" in c:
        f1 = dx2.F("Bold", 42); f2 = dx2.F("SemiBold", 30)
        q = _wrap(d, "\u201c" + c["trich"] + "\u201d", f1, w - 90)
        h = 60 + len(q) * 56 + 70
        d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 22, fill=(250, 246, 236, int(235 * a)))
        d.rectangle([x0, y0 + 20, x0 + 10, y0 + h - 20], fill=(*dx2.GOLD, int(255 * a)))
        y = y0 + 40
        for l in q: d.text((x0 + 50, y), l, font=f1, fill=(20, 22, 30, int(255 * a))); y += 56
        d.text((x0 + 50, y + 10), "— " + c.get("ai", ""), font=f2, fill=(120, 90, 20, int(255 * a)))
    elif "ds" in c:
        f1 = dx2.F("Bold", 36); items = c["ds"]; tt = c.get("tieu", "")
        rows = [ _wrap(d, s, f1, w - 120) for s in items ]
        h = 50 + (54 if tt else 0) + sum(len(r) * 46 + 18 for r in rows) + 20
        d.rounded_rectangle([x0, y0, x0 + w, y0 + h], 22, fill=(12, 14, 20, int(225 * a)), outline=(*dx2.GOLD, int(200 * a)), width=2)
        y = y0 + 30
        if tt: d.text((x0 + 40, y), tt, font=dx2.F("Black", 38), fill=(*dx2.GOLD, int(255 * a))); y += 54
        for k, r in enumerate(rows):
            ak = a * dx2.ease((t - t0 - 0.4 - k * 0.9) / 0.4)
            if ak <= 0.01: break
            d.ellipse([x0 + 40, y + 12, x0 + 62, y + 34], fill=(*dx2.GOLD, int(255 * ak)))
            for l in r: d.text((x0 + 80, y), l, font=f1, fill=(240, 242, 248, int(255 * ak))); y += 46
            y += 18

def _wrap(d, s, f, mw):
    out, cur = [], ""
    for wd in s.split():
        tst = (cur + " " + wd).strip()
        if d.textlength(tst, font=f) <= mw: cur = tst
        else:
            if cur: out.append(cur)
            cur = wd
    if cur: out.append(cur)
    return out

def frame(sc, t):
    cta = sc.get("cta") or sc.get("k") == "end" or "_kb" not in sc
    im = _plain_bg(t) if cta else _shot_bg(sc, t)
    d = ImageDraw.Draw(im)
    # logo nhỏ góc trên trái
    f1 = dx2.F("Black", 30); f2 = dx2.F("SemiBold", 14)
    d.text((64, 44), "HUY NGUYỄN", font=f1, fill=(255, 255, 255))
    dx2.spaced(d, 64 + d.textlength("HUY NGUYỄN", font=f1) / 2, 82, "CHỨNG KHOÁN", f2, dx2.LILAC, 4)
    d.line([64, 106, 112, 106], fill=dx2.LGOLD, width=3)
    caps = [c for c in (sc.get("cap") or []) if c]
    cols = sc.get("cols") or [dx2.CREAM, dx2.GOLD]
    a0 = dx2.ease(t / 0.5)
    if cta:
        lab = sc.get("label") or ""
        y = LH * 0.36
        if lab:
            f = dx2.F("Bold", 34); tw = d.textlength(lab, font=f)
            d.text((LW / 2 - tw / 2, y - 70), lab, font=f, fill=dx2.mix(dx2.GOLD, a0, (11, 13, 19)))
        for i, l in enumerate(caps):
            a = dx2.ease((t - 0.15 - i * 0.18) / 0.45)
            f = dx2.fit(d, l, "Black", LW - 260, 120); tw = d.textlength(l, font=f)
            c = cols[i] if i < len(cols) else dx2.CREAM
            d.text((LW / 2 - tw / 2, y + (1 - a) * 26), l, font=f, fill=dx2.mix(c, a, (11, 13, 19))); y += int(f.size * 1.18)
        return im
    d.text((24, LH - 30), "Ảnh minh hoạ: Wikimedia Commons", font=dx2.F("SemiBold", 16), fill=(150, 156, 170))
    s = int(t // SHOT); big = (s % 3) != 1          # góc cận: chữ thu nhỏ thành nhãn để ảnh "thở"
    _the(im, sc, t); d = ImageDraw.Draw(im)
    if sc.get("the"): big = True     # có thẻ dữ kiện thì giữ tiêu đề trái cố định, thẻ bên phải
    tag = _tag(sc)
    if big:
        x = 110; y = 330
        if tag:
            f = dx2.fit(d, tag, "Bold", 860, 30)
            d.text((x, y - 64), tag, font=f, fill=dx2.mix(dx2.GOLD, a0, (8, 10, 14)))
            d.line([x, y - 18, x + int(90 * a0), y - 18], fill=dx2.GOLD, width=4)
        for i, l in enumerate(caps):
            a = dx2.ease((t - s * SHOT - 0.15 - i * 0.16) / 0.45) if s else dx2.ease((t - 0.2 - i * 0.18) / 0.45)
            f = dx2.fit(d, l, "Black", 900, 112); c = cols[i] if i < len(cols) else dx2.CREAM
            d.text((x + (1 - a) * -30, y), l, font=f, fill=c, stroke_width=1, stroke_fill=(0, 0, 0)); y += int(f.size * 1.14)
    else:
        txt = " ".join(caps)
        f = dx2.fit(d, txt, "Black", 980, 46); tw = d.textlength(txt, font=f)
        d.rounded_rectangle([64, 150, 64 + tw + 56, 150 + f.size + 34], 12, fill=(10, 12, 18))
        d.rectangle([64, 150, 72, 150 + f.size + 34], fill=dx2.GOLD)
        d.text((96, 164), txt, font=f, fill=(255, 255, 255))
    return im
