# Cảnh BẢN ĐỒ / THƯỚC SO SÁNH / MẶT CẮT cho video dài ngang (NV1 23/11/2026, loạt "Vì sao…" theo bản đồ – claude/chi_dao/series_vi_sao_ban_do_2311.md).
# render.py gọi frame(sc, t) cho k in ('map', 'scale', 'section'); phụ đề do render.py vẽ (chừa 230px đáy).
#
# 'map': ảnh vệ tinh Sentinel-2 cloudless 2016 (CC BY 4.0 – "Sentinel-2 cloudless – s2maps.eu by EOX IT Services GmbH"),
#   bay/zoom liên tục giữa các mốc, nhãn địa danh + đường nối hiện dần theo thời gian.
#   sc['map'] = {'kf': [(lat, lon, zoom, u), ...]   # u = 0..1 vị trí mốc trong cảnh (zoom thập phân, tối đa 13)
#                'nhan': [(lat, lon, 'CHỮ', u_hien, 'diem'|'cang'|'vung'|'chu'), ...],
#                'duong': [([(lat, lon), ...], (r,g,b), u_bat_dau, u_xong, 'nhãn giữa đường' hoặc ''), ...],
#                'dim': 0.15}                    # làm tối ảnh nền cho chữ nổi
# 'scale': thước so sánh ngang, cùng một tỷ lệ: sc['scale'] = {'tieu_de': '...', 'don_vi': 'm', 'muc': [(nhãn, giá trị, 'tau'|'thap'|'xe'|'thanh', màu, ghi chú), ...]}
# 'section': mặt cắt luồng: sc['section'] = {'sau': 15.5, 'tang': 3.1, 'nhan_sau': 'LUỒNG SÂU 15,5 M', 'ghi': [...], 'tau': [(nhãn, mớn m, dài tương đối 0..1, màu)]}
import os, math, io, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageDraw, ImageFilter
import dx2

LW, LH = 1920, 1080
HERE = os.path.dirname(os.path.abspath(__file__))
ZMAX = 13
URL = "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless_3857/default/g/%d/%d/%d.jpg"
KHO = [os.path.join(HERE, "ban_do", "tiles"), os.path.join(HERE, "out", "tiles")]
NGUON = "Ảnh vệ tinh: Sentinel-2 cloudless – s2maps.eu by EOX IT Services GmbH (CC BY 4.0)"
VANG = (255, 196, 0); TRANG = (255, 255, 255); DO = (239, 68, 68); XANH = (34, 197, 94); LAM = (56, 189, 248); NEN = (10, 12, 17)
ease = lambda x: (lambda u: u * u * (3 - 2 * u))(max(0.0, min(1.0, x)))
_T = {}


def _tile(z, x, y):
    k = (z, x, y)
    if k in _T: return _T[k]
    n = 2 ** z; x %= n
    if y < 0 or y >= n: im = Image.new("RGB", (256, 256), (8, 22, 46)); _T[k] = im; return im
    for d in KHO:
        p = "%s/%d/%d/%d.jpg" % (d, z, x, y)
        if os.path.exists(p):
            try: im = Image.open(p).convert("RGB"); _T[k] = im; return im
            except Exception: pass
    p = "%s/%d/%d/%d.jpg" % (KHO[1], z, x, y)
    for _ in range(3):
        try:
            b = urllib.request.urlopen(urllib.request.Request(URL % (z, y, x), headers={"User-Agent": "chungkhoanhuynguyen-video"}), timeout=30).read()
            os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "wb").write(b)
            im = Image.open(io.BytesIO(b)).convert("RGB"); _T[k] = im; return im
        except Exception: pass
    im = Image.new("RGB", (256, 256), (8, 22, 46)); _T[k] = im; return im


def _merc(lat, lon):
    """toạ độ chuẩn hoá 0..1 (Web Mercator)."""
    s = math.sin(math.radians(lat))
    return (lon + 180) / 360, 0.5 - math.log((1 + s) / (1 - s)) / (4 * math.pi)


def _cam(sc, u):
    """(x chuẩn hoá, y chuẩn hoá, zoom) của máy quay tại u (0..1)."""
    kf = sc["map"]["kf"]
    if u <= kf[0][3]: a = b = kf[0]; w = 0
    elif u >= kf[-1][3]: a = b = kf[-1]; w = 0
    else:
        i = max(j for j in range(len(kf)) if kf[j][3] <= u); a, b = kf[i], kf[min(i + 1, len(kf) - 1)]
        w = ease((u - a[3]) / max(1e-6, b[3] - a[3]))
    za, zb = a[2], b[2]; z = za + (zb - za) * w
    (xa, ya), (xb, yb) = _merc(a[0], a[1]), _merc(b[0], b[1])
    # bay theo đường thẳng trên mặt phẳng zoom: tâm nội suy theo tỷ lệ phóng để điểm đích không trôi
    if abs(zb - za) > 0.05:
        sa, sb, s = 2 ** za, 2 ** zb, 2 ** z
        r = (1 / sa - 1 / s) / (1 / sa - 1 / sb) if (1 / sa - 1 / sb) != 0 else w
    else: r = w
    return xa + (xb - xa) * r, ya + (yb - ya) * r, z


def _nen(cx, cy, z):
    L = min(ZMAX, max(1, int(math.ceil(z - 1e-6)))); f = 2 ** (z - L)   # f <= 1 (đôi khi > 1 nếu z > ZMAX)
    W, H = LW / f, LH / f; px, py = cx * (2 ** L) * 256, cy * (2 ** L) * 256
    x0, y0 = px - W / 2, py - H / 2
    tx0, ty0, tx1, ty1 = int(math.floor(x0 / 256)), int(math.floor(y0 / 256)), int(math.floor((x0 + W) / 256)), int(math.floor((y0 + H) / 256))
    js = [(x, y) for x in range(tx0, tx1 + 1) for y in range(ty0, ty1 + 1)]
    miss = [j for j in js if (L, j[0] % (2 ** L), j[1]) not in _T]
    if len(miss) > 4:
        with ThreadPoolExecutor(12) as ex: list(ex.map(lambda a: _tile(L, *a), miss))
    im = Image.new("RGB", ((tx1 - tx0 + 1) * 256, (ty1 - ty0 + 1) * 256))
    for x, y in js: im.paste(_tile(L, x, y), ((x - tx0) * 256, (y - ty0) * 256))
    ox, oy = x0 - tx0 * 256, y0 - ty0 * 256
    return im.resize((LW, LH), Image.BILINEAR, box=(ox, oy, ox + W, oy + H))


def _scr(lat, lon, cx, cy, z):
    x, y = _merc(lat, lon); s = (2 ** z) * 256
    return LW / 2 + (x - cx) * s, LH / 2 + (y - cy) * s


def _pill(d, x, y, s, f, fg, bg, a, anchor="l"):
    tw = d.textlength(s, font=f); h = f.size * 1.25
    if anchor == "c": x -= tw / 2 + 16
    d.rounded_rectangle([x, y - h / 2, x + tw + 32, y + h / 2], int(h / 2.6), fill=dx2.mix(bg, a, (0, 0, 0)))
    d.text((x + 16, y - f.size * 0.62), s, font=f, fill=dx2.mix(fg, a, bg))
    return x + tw + 32


def _cap(im, d, sc, t):
    cap = [c for c in (sc.get("cap") or ()) if c]
    if not cap: return
    cols = sc.get("cols") or (TRANG, VANG)
    ov = Image.new("RGBA", (LW, LH), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    for i in range(260): od.line([0, i, LW, i], fill=(0, 0, 0, int(170 * (1 - i / 260) ** 1.3)))
    im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im)
    y = 40
    for i, l in enumerate(cap[:2]):
        a = ease((t - 0.2 - i * 0.15) / 0.4)
        if a <= 0: continue
        f = dx2.fit(d, l, "Black", 1300, 78 if i == 0 else 66)
        c = cols[i] if i < len(cols) else TRANG
        d.text((60 + 3, y + 3), l, font=f, fill=(0, 0, 0)); d.text((60, y + (1 - a) * 18), l, font=f, fill=dx2.mix(c, a, (0, 0, 0)))
        y += int(f.size * 1.18)
    dx2.brand(im, d, LW - 190, 34, 0.62, 1.0, (0, 0, 0))


def _map(sc, t):
    T = max(1.0, sc.get("_T", 8.0)); u = min(1.0, t / T); m = sc["map"]
    cx, cy, z = _cam(sc, u)
    im = _nen(cx, cy, z)
    dim = m.get("dim", 0.12)
    if dim: im = Image.blend(im, Image.new("RGB", (LW, LH), (0, 0, 0)), dim)
    d = ImageDraw.Draw(im, "RGBA")
    for pts, col, u0, u1, nh in m.get("duong", []):
        a = (u - u0) / max(1e-6, u1 - u0)
        if a <= 0: continue
        a = min(1.0, a); P = [_scr(la, lo, cx, cy, z) for la, lo in pts]
        seg = [0.0]
        for p, q in zip(P, P[1:]): seg.append(seg[-1] + math.hypot(q[0] - p[0], q[1] - p[1]))
        L = seg[-1] * a; Q = [P[0]]
        for i in range(1, len(P)):
            if seg[i] <= L: Q.append(P[i])
            else:
                r = (L - seg[i - 1]) / max(1e-6, seg[i] - seg[i - 1]); Q.append((P[i - 1][0] + (P[i][0] - P[i - 1][0]) * r, P[i - 1][1] + (P[i][1] - P[i - 1][1]) * r)); break
        if len(Q) > 1:
            d.line(Q, fill=(0, 0, 0, 150), width=14, joint="curve"); d.line(Q, fill=col + (255,), width=7, joint="curve")
            hx, hy = Q[-1]; d.ellipse([hx - 11, hy - 11, hx + 11, hy + 11], fill=col + (255,), outline=(255, 255, 255, 255), width=3)
        if nh and a >= 1:
            mx, my = P[len(P) // 2]; _pill(d, mx, my - 40, nh, dx2.F("ExtraBold", 34), (10, 12, 17), col, ease((u - u1) * T / 0.4), "c")
    for it in m.get("nhan", []):
        la, lo, s, u0 = it[:4]; kieu = it[4] if len(it) > 4 else "diem"
        a = ease((u - u0) * T / 0.45)
        if a <= 0: continue
        x, y = _scr(la, lo, cx, cy, z)
        if not (-200 < x < LW + 200 and -200 < y < LH + 200): continue
        if kieu == "vung":
            f = dx2.F("Black", 54); tw = d.textlength(s, font=f)
            d.text((x - tw / 2 + 3, y - 30 + 3), s, font=f, fill=(0, 0, 0, int(200 * a))); d.text((x - tw / 2, y - 30), s, font=f, fill=TRANG + (int(235 * a),))
            continue
        if kieu == "chu":
            f = dx2.F("ExtraBold", 36); tw = d.textlength(s, font=f)
            d.text((x - tw / 2 + 2, y - 20 + 2), s, font=f, fill=(0, 0, 0, int(210 * a))); d.text((x - tw / 2, y - 20), s, font=f, fill=(225, 240, 255, int(255 * a)))
            continue
        col = VANG if kieu == "cang" else TRANG; r = 13 if kieu == "cang" else 9
        pu = (t * 1.6) % 1.0
        d.ellipse([x - r - 26 * pu, y - r - 26 * pu, x + r + 26 * pu, y + r + 26 * pu], outline=col + (int(200 * (1 - pu) * a),), width=4)
        d.ellipse([x - r, y - r, x + r, y + r], fill=col + (int(255 * a),), outline=(0, 0, 0, int(200 * a)), width=3)
        f = dx2.F("ExtraBold", 40 if kieu == "cang" else 34)
        tw = d.textlength(s, font=f); lx = x + 26 if x + 26 + tw + 40 < LW - 20 else x - 26 - tw - 32
        _pill(d, lx, y, s, f, (10, 12, 17) if kieu == "cang" else TRANG, VANG if kieu == "cang" else (16, 20, 28), a)
    d.text((24, LH - 34), NGUON, font=dx2.F("SemiBold", 18), fill=(200, 206, 214, 200))
    _cap(im, ImageDraw.Draw(im), sc, t)
    return im


def _bg():
    if "bg" not in _T:
        g = Image.new("RGB", (LW, LH), (12, 15, 22)); d = ImageDraw.Draw(g)
        for r, c in ((1100, (16, 20, 29)), (700, (20, 25, 36))): d.ellipse([LW / 2 - r, LH * 0.55 - r, LW / 2 + r, LH * 0.55 + r], fill=c)
        _T["bg"] = g.filter(ImageFilter.GaussianBlur(120))
    return _T["bg"].copy()


def _tau(d, x0, yb, w, h, col, a, n_cont=True):
    """tàu container nhìn ngang: thân + đài chỉ huy + hàng container (đáy ở yb, dài w)."""
    hull = [(x0, yb - h * 0.55), (x0 + w * 0.96, yb - h * 0.55), (x0 + w, yb - h * 0.75), (x0 + w * 0.93, yb), (x0 + w * 0.04, yb)]
    d.polygon(hull, fill=dx2.mix((30, 40, 58), a, NEN)); d.line(hull + [hull[0]], fill=dx2.mix(col, a, NEN), width=3)
    if n_cont:
        cw = max(6, w / 46); ch = h * 0.16
        pal = [(214, 84, 60), (60, 130, 200), (230, 170, 60), (70, 160, 110), (150, 150, 160)]
        x = x0 + w * 0.06; k = 0
        while x + cw < x0 + w * 0.9:
            if abs(x - (x0 + w * 0.78)) < cw * 1.5: x += cw * 2; continue
            for r in range(3):
                d.rectangle([x, yb - h * 0.55 - ch * (r + 1), x + cw - 2, yb - h * 0.55 - ch * r - 2], fill=dx2.mix(pal[(k + r) % 5], a, NEN))
            x += cw; k += 1
    bx = x0 + w * 0.78
    d.rectangle([bx, yb - h * 1.15, bx + max(10, w * 0.045), yb - h * 0.55], fill=dx2.mix((235, 238, 242), a, NEN))


def _thap(d, x0, yc, w, h, col, a):
    """toà tháp nằm ngang (chân bên trái), có tầng kẻ vạch."""
    pts = [(x0, yc - h / 2), (x0 + w * 0.9, yc - h * 0.32), (x0 + w, yc), (x0 + w * 0.9, yc + h * 0.32), (x0, yc + h / 2)]
    d.polygon(pts, fill=dx2.mix((70, 84, 110), a, NEN)); d.line(pts + [pts[0]], fill=dx2.mix(col, a, NEN), width=3)
    for i in range(1, 24): xx = x0 + w * 0.9 * i / 24; d.line([xx, yc - h * 0.42, xx, yc + h * 0.42], fill=dx2.mix((110, 124, 150), a, NEN), width=1)


def _scale(sc, t):
    T = max(1.0, sc.get("_T", 8.0)); s = sc["scale"]; im = _bg(); d = ImageDraw.Draw(im)
    muc = s["muc"]; vmax = max(m[1] for m in muc); x0 = 120; wmax = LW - 2 * x0 - 40
    top = 300; gap = min(200, (LH - 260 - top) / max(1, len(muc)))
    # thước chia vạch
    d.line([x0, top - 40, x0 + wmax, top - 40], fill=(110, 118, 134), width=2)
    st = next(v for v in (1, 2, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 5000, 10000) if vmax / v <= 10)
    v = 0
    while v <= vmax * 1.001:
        xx = x0 + wmax * v / vmax; d.line([xx, top - 52, xx, top - 28], fill=(140, 148, 164), width=2)
        d.text((xx - 20, top - 92), "%g" % v, font=dx2.F("SemiBold", 24), fill=(160, 168, 184)); v += st
    d.text((x0 + wmax + 12, top - 62), s.get("don_vi", "m"), font=dx2.F("Bold", 26), fill=(160, 168, 184))
    for i, m in enumerate(muc):
        nh, val, kieu, col = m[:4]; ghi = m[4] if len(m) > 4 else ""
        u0 = 0.4 + i * (T - 2.0) / max(1, len(muc)) * 0.8
        a = ease((t - u0) / 0.5); g = ease((t - u0) / 1.2)
        if a <= 0: continue
        y = top + i * gap + gap * 0.55; w = wmax * val / vmax * g
        if kieu == "tau": _tau(d, x0, y + 40, max(20, w), 70, col, a)
        elif kieu == "thap": _thap(d, x0, y, max(20, w), 64, col, a)
        else: d.rounded_rectangle([x0, y - 22, x0 + max(8, w), y + 22], 10, fill=dx2.mix(col, a, NEN))
        f = dx2.F("ExtraBold", 38); lab = nh + ("  ·  " + ghi if ghi else "")
        d.text((x0, y - gap * 0.55 + 2), lab, font=dx2.fit(d, lab, "ExtraBold", wmax, 38), fill=dx2.mix(col, a, NEN))
    _cap(im, ImageDraw.Draw(im), sc, t)
    return im


def _section(sc, t):
    T = max(1.0, sc.get("_T", 8.0)); s = sc["section"]; im = _bg(); d = ImageDraw.Draw(im, "RGBA")
    sau = s.get("sau", 15.5); tang = s.get("tang", 3.1)
    ym = 420; ppm = 300 / max(sau, 1)   # mặt nước ở y=420, đáy luồng = ym + sau*ppm
    yd = ym + sau * ppm; a0 = ease((t - 0.3) / 0.8)
    # nước + đáy
    for y in range(int(ym), int(yd) + 1):
        k = (y - ym) / (yd - ym); d.line([80, y, LW - 80, y], fill=(int(20 + 10 * (1 - k)), int(70 + 50 * (1 - k)), int(120 + 60 * (1 - k)), int(230 * a0)))
    bed = [(80, yd + 90), (80, ym + 40), (300, yd - 40), (520, yd), (LW - 520, yd), (LW - 300, yd - 40), (LW - 80, ym + 40), (LW - 80, yd + 90)]
    d.polygon(bed, fill=(92, 74, 52, int(255 * a0)))
    d.line([80, ym, LW - 80, ym], fill=(170, 220, 255, int(255 * a0)), width=3)
    # nhãn độ sâu
    a1 = ease((t - 1.0) / 0.6)
    if a1 > 0:
        xr = LW - 420; d.line([xr, ym, xr, yd], fill=VANG + (int(255 * a1),), width=5)
        for yy in (ym, yd): d.line([xr - 22, yy, xr + 22, yy], fill=VANG + (int(255 * a1),), width=5)
        _pill(d, xr + 34, (ym + yd) / 2, s.get("nhan_sau", "SÂU %g M" % sau), dx2.F("Black", 44), (10, 12, 17), VANG, a1)
    # nhà n tầng đặt dưới nước để so độ sâu
    a2 = ease((t - 1.8) / 0.6); n = int(round(sau / tang))
    if a2 > 0 and s.get("nha", True):
        xh = 330; wh = 170; hh = tang * ppm
        for i in range(n):
            yb = yd - i * hh
            d.rectangle([xh, yb - hh + 3, xh + wh, yb], fill=(236, 226, 205, int(235 * a2)), outline=(120, 100, 80, int(255 * a2)), width=2)
            for j in range(3): d.rectangle([xh + 18 + j * 52, yb - hh + 16, xh + 52 + j * 52, yb - 12], fill=(90, 140, 190, int(220 * a2)))
        _pill(d, xh - 40, ym - 52, s.get("nhan_nha", "%d TẦNG NHÀ" % n), dx2.F("ExtraBold", 36), TRANG, (16, 20, 28), a2)
    # tàu trên mặt nước (minh hoạ mớn chìm), đặt bên phải nhà để không che
    for i, (nh, mon, dai, col) in enumerate(s.get("tau", [])):
        a3 = ease((t - 2.6 - i * 0.9) / 0.6)
        if a3 <= 0: continue
        w = 600 * dai; x = 740 + i * 30; yb = ym + mon * ppm; top = ym - 34
        hull = [(x, top), (x + w * 0.97, top), (x + w, top - 26), (x + w * 0.93, yb), (x + w * 0.05, yb)]
        d.polygon(hull, fill=(30, 40, 58, int(255 * a3))); d.line(hull + [hull[0]], fill=col + (int(255 * a3),), width=3)
        cw = w / 40; pal = [(214, 84, 60), (60, 130, 200), (230, 170, 60), (70, 160, 110), (150, 150, 160)]; xx = x + w * 0.05; k = 0
        while xx + cw < x + w * 0.86:
            if abs(xx - (x + w * 0.74)) < cw * 1.4: xx += cw * 2; continue
            for r in range(4): d.rectangle([xx, top - 26 * (r + 1), xx + cw - 2, top - 26 * r - 2], fill=pal[(k + r) % 5] + (int(255 * a3),))
            xx += cw; k += 1
        d.rectangle([x + w * 0.74, top - 150, x + w * 0.74 + 26, top], fill=(235, 238, 242, int(255 * a3)))
        _pill(d, x, top - 190 - i * 60, nh, dx2.F("ExtraBold", 34), (10, 12, 17), col, a3)
    for i, g in enumerate(s.get("ghi", [])):
        a4 = ease((t - 3.4 - i * 0.6) / 0.5)
        if a4 > 0: _pill(d, 110, yd + 40 + i * 0, g, dx2.F("Bold", 30), TRANG, (16, 20, 28), a4)
    _cap(im, ImageDraw.Draw(im), sc, t)
    return im


def frame(sc, t):
    k = sc.get("k")
    if k == "map": return _map(sc, t)
    if k == "scale": return _scale(sc, t)
    return _section(sc, t)


def tai_truoc(sc, fps=24, buoc=4):
    """tải sẵn ô ảnh cho cả cảnh map (thử mỗi 'buoc' khung) – gọi trước khi dựng để khỏi chờ mạng giữa chừng."""
    if sc.get("k") != "map": return 0
    T = sc.get("_T", 8.0); n = 0
    for j in range(0, int(T * fps) + 1, buoc):
        cx, cy, z = _cam(sc, min(1.0, j / fps / T)); _nen(cx, cy, z); n += 1
    return n
