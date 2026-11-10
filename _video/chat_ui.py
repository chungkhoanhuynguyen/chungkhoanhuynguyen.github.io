# Cảnh "điện thoại" cho video kể chuyện (QL1 10/11/2026, kênh @5 "Vì sao thật tệ khi…"):
#   k='chat': nhóm chat chung chung (không logo/nhãn hiệu thật) – tin nhắn bật lần lượt theo thời lượng giọng đọc
#   k='noti': màn hình khoá – thông báo trượt xuống lần lượt
# Bố cục ngang 1920x1080: điện thoại bên trái, 2 dòng chữ lớn bên phải, phụ đề do render.py vẽ dưới cột phải.
from PIL import Image, ImageDraw, ImageFilter
import dx2

LW, LH = 1920, 1080
PW, PH = 520, 1000            # thân máy
PX0, PY0 = 120, 40
SX, SY, SW, SH = PX0 + 18, PY0 + 18, PW - 36, PH - 36   # màn hình
DARK = (13, 16, 23)
BUB_L = (38, 44, 58); BUB_R = (0, 104, 255); SYS = (120, 128, 146)
MAU_TEN = [(255, 196, 0), (90, 200, 250), (255, 120, 160), (120, 230, 140), (200, 160, 255), (255, 160, 90)]

def _nen(sc):
    g = Image.new("RGB", (LW, LH), DARK); d = ImageDraw.Draw(g)
    for r, c in ((900, (20, 25, 36)), (560, (26, 32, 46))): d.ellipse([560 - r, LH/2 - r, 560 + r, LH/2 + r], fill=c)
    g = g.filter(ImageFilter.GaussianBlur(120)); d = ImageDraw.Draw(g, "RGBA")
    for x in range(0, LW, 48): d.line([x, 0, x, LH], fill=(255, 255, 255, 6))
    for y in range(0, LH, 48): d.line([0, y, LW, y], fill=(255, 255, 255, 6))
    return g

def _wrap(d, s, f, mw):
    out, cur = [], ""
    for w in s.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= mw or not cur: cur = t
        else: out.append(cur); cur = w
    if cur: out.append(cur)
    return out

def _than_may(im):
    d = ImageDraw.Draw(im, "RGBA")
    sh = Image.new("L", (LW, LH), 0); ImageDraw.Draw(sh).rounded_rectangle([PX0 + 10, PY0 + 24, PX0 + PW + 10, PY0 + PH + 24], 70, fill=170)
    im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(30)))
    d.rounded_rectangle([PX0, PY0, PX0 + PW, PY0 + PH], 66, fill=(30, 33, 40), outline=(90, 96, 110), width=3)
    return d

def _chu_phai(im, sc, t):
    d = ImageDraw.Draw(im); x0 = PX0 + PW + 110; cw = LW - x0 - 90; y = 300
    lab = sc.get("label") or ""
    if lab:
        f = dx2.F("Bold", 32); a = dx2.ease(t / 0.4)
        d.text((x0, y - 70), lab, font=f, fill=dx2.mix((255, 196, 0), a, DARK))
    cols = sc.get("cols") or [(255, 255, 255), (255, 196, 0)]
    for i, l in enumerate(sc.get("cap") or []):
        if not l: continue
        a = dx2.ease((t - 0.2 - i * 0.18) / 0.45)
        if a <= 0: continue
        f = dx2.fit(d, l, "Black", cw, 96); c = cols[i] if i < len(cols) else (255, 255, 255)
        d.text((x0, y + (1 - a) * 24), l, font=f, fill=dx2.mix(c, a, DARK), stroke_width=2, stroke_fill=(0, 0, 0)); y += int(f.size * 1.18)
    if sc.get("cap") and any(sc["cap"]):
        a = dx2.ease((t - 0.6) / 0.4); d.line([x0, y + 20, x0 + int(140 * a), y + 20], fill=(255, 196, 0), width=6)

def _thoi_diem(sc, n, co_san=0):
    T = max(2.0, sc.get("_T", 8.0)); a, b = 0.35, max(0.8, T - 1.4); m = n - co_san
    return [-1.0] * co_san + [a + (b - a) * i / max(1, m) for i in range(m)]

def chat(sc, t):
    im = _nen(sc); d = _than_may(im)
    scr = Image.new("RGB", (SW, SH), (17, 20, 27)); s = ImageDraw.Draw(scr)
    c = sc.get("chat", {}); msgs = c.get("msgs", [])
    # thanh đầu nhóm
    s.rectangle([0, 0, SW, 120], fill=(24, 28, 38))
    s.ellipse([24, 48, 84, 108], fill=c.get("mau", (255, 196, 0)))
    s.text((54, 78), (c.get("ten", "?")[:1]).upper(), font=dx2.F("Black", 30), fill=DARK, anchor="mm")
    s.text((100, 50), c.get("ten", ""), font=dx2.fit(s, c.get("ten", ""), "Bold", SW - 130, 28), fill=(240, 240, 245))
    s.text((100, 86), c.get("tv", ""), font=dx2.F("SemiBold", 20), fill=SYS)
    s.text((SW / 2, 22), c.get("gio", "21:07"), font=dx2.F("Bold", 20), fill=(220, 220, 228), anchor="mt")
    # tin nhắn: dựng toàn bộ chiều cao rồi cuộn theo tin mới nhất
    tms = _thoi_diem(sc, len(msgs), c.get("co_san", 0)); fb = dx2.F("SemiBold", 25); fn = dx2.F("Bold", 20); mw = SW - 150
    blocks = []
    for i, m in enumerate(msgs):
        if t < tms[i]: break
        p = dx2.ease((t - tms[i]) / 0.25)
        ai, txt = m[0], m[1]; kieu = m[2] if len(m) > 2 else ""
        if ai == "*":   # dòng hệ thống
            lines = _wrap(s, txt, dx2.F("SemiBold", 20), SW - 80); h = 30 * len(lines) + 20; blocks.append(("sys", lines, h, p, kieu)); continue
        lines = _wrap(s, txt, fb, mw - 36); h = 34 * len(lines) + 30 + (28 if ai != "me" else 0) + (110 if kieu == "lai" else 0)
        blocks.append((ai, lines, h, p, kieu if kieu != 'lai' else ('lai', m[3] if len(m) > 3 else '')))
    tong = sum(b[2] + 14 for b in blocks); vung = SH - 140 - 90; y = 136 - max(0, tong - vung)
    for ai, lines, h, p, kieu in blocks:
        so_lai = ''
        if isinstance(kieu, tuple): kieu, so_lai = kieu
        if y + h < 120: y += h + 14; continue
        if ai == "sys":
            f = dx2.F("SemiBold", 20)
            for k, l in enumerate(lines): s.text((SW / 2, y + 10 + 30 * k), l, font=f, fill=dx2.mix(SYS, p, (17, 20, 27)), anchor="mt")
            y += h + 14; continue
        me = ai == "me"; bw = max(s.textlength(l, font=fb) for l in lines) + 36
        if kieu == "lai": bw = max(bw, 330)
        if not me: bw = max(bw, s.textlength(ai, font=fn) + 36)
        x = SW - 24 - bw if me else 76; dy = int((1 - p) * 26)
        if not me:
            ci = MAU_TEN[sum(map(ord, ai)) % len(MAU_TEN)]
            s.ellipse([20, y + dy + 4, 62, y + dy + 46], fill=ci); s.text((41, y + dy + 25), ai[:1].upper(), font=dx2.F("Black", 20), fill=DARK, anchor="mm")
        s.rounded_rectangle([x, y + dy, x + bw, y + dy + h], 20, fill=dx2.mix(BUB_R if me else BUB_L, p, (17, 20, 27)))
        yy = y + dy + 14
        if not me:
            s.text((x + 18, yy), ai, font=fn, fill=dx2.mix(MAU_TEN[sum(map(ord, ai)) % len(MAU_TEN)], p, (17, 20, 27))); yy += 28
        for l in lines: s.text((x + 18, yy), l, font=fb, fill=dx2.mix((245, 246, 250), p, (17, 20, 27))); yy += 34
        if kieu == "lai":   # ảnh chụp tài khoản lãi (giả định)
            s.rounded_rectangle([x + 14, yy + 6, x + bw - 14, yy + 98], 14, fill=(10, 40, 26))
            s.text((x + 30, yy + 16), "Lãi/lỗ tạm tính", font=dx2.F("SemiBold", 18), fill=(150, 220, 170))
            s.text((x + 30, yy + 42), so_lai or "+38,2%", font=dx2.F("Black", 40), fill=(60, 230, 120))
        y += h + 14
    # ô nhập
    s.rectangle([0, SH - 86, SW, SH], fill=(24, 28, 38)); s.rounded_rectangle([20, SH - 70, SW - 20, SH - 18], 26, fill=(36, 41, 54))
    s.text((44, SH - 44), "Nhập tin nhắn…", font=dx2.F("SemiBold", 22), fill=SYS, anchor="lm")
    m = Image.new("L", (SW, SH), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, SW - 1, SH - 1], 50, fill=255)
    im.paste(scr, (SX, SY), m)
    _chu_phai(im, sc, t); return im

def noti(sc, t):
    im = _nen(sc); d = _than_may(im)
    scr = Image.new("RGB", (SW, SH)); s = ImageDraw.Draw(scr)
    for y in range(SH): s.line([0, y, SW, y], fill=(int(18 + 22 * y / SH), int(22 + 10 * y / SH), int(40 + 20 * y / SH)))
    n = sc.get("noti", {}); items = n.get("items", [])
    s.text((SW / 2, 120), n.get("gio", "23:04"), font=dx2.F("Black", 110), fill=(240, 242, 250), anchor="mt")
    s.text((SW / 2, 250), n.get("ngay", "Thứ Năm"), font=dx2.F("SemiBold", 26), fill=(200, 204, 220), anchor="mt")
    tms = _thoi_diem(sc, len(items), n.get("co_san", 0)); y = 320; fa, ft, fb = dx2.F("Bold", 18), dx2.F("Bold", 24), dx2.F("SemiBold", 22)
    for i, it in enumerate(items):
        if t < tms[i]: break
        p = dx2.ease((t - tms[i]) / 0.3); app, tieu, than = it[0], it[1], it[2]; mau = it[3] if len(it) > 3 else (255, 196, 0)
        lines = _wrap(s, than, fb, SW - 120)[:4]; h = 92 + 30 * len(lines); yy = y - int((1 - p) * 60)
        box = Image.new("RGBA", (SW - 40, h), (0, 0, 0, 0)); b = ImageDraw.Draw(box)
        b.rounded_rectangle([0, 0, SW - 41, h - 1], 26, fill=(235, 238, 245, int(225 * p)))
        b.rounded_rectangle([18, 16, 50, 48], 9, fill=mau + (int(255 * p),))
        b.text((60, 22), app.upper(), font=fa, fill=(90, 96, 110, int(255 * p)))
        b.text((SW - 70, 22), "bây giờ", font=fa, fill=(120, 126, 140, int(255 * p)), anchor="ra")
        b.text((18, 58), tieu, font=ft, fill=(16, 18, 24, int(255 * p)))
        for k, l in enumerate(lines): b.text((18, 90 + 30 * k), l, font=fb, fill=(40, 44, 54, int(255 * p)))
        scr.paste(box, (20, yy), box); y += h + 16
    m = Image.new("L", (SW, SH), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, SW - 1, SH - 1], 50, fill=255)
    im.paste(scr, (SX, SY), m)
    _chu_phai(im, sc, t); return im

KINDS = dict(chat=chat, noti=noti)
def frame(sc, t): return KINDS[sc["k"]](sc, t)
