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
            v = int(235 * max(0.0, 1 - x / (LW * 0.72)) ** 1.25)
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
