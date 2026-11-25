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
    if nd is None: nd = 0 if abs(v) >= 100 else 1
    s = f"{v:,.{nd}f}".replace(",", "§").replace(".", ",").replace("§", ".")
    return s + dv

def nen(sp, t):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, W - 6, H - 6], 36, outline=(90, 50, 150), width=4)
    a = ease(t / 0.4)
    tv = sp.get("tieu", ""); ft = 44
    while ft > 26 and d.textlength(tv, font=F("ExtraBold", ft)) > W - 80: ft -= 2   # (15/11 NV1, RV1511ND: tiêu đề dài tràn 2 mép) tự co chữ
    d.text((W / 2, 50 + (1 - a) * 20), tv, font=F("ExtraBold", ft), fill=tuple(int(c * a + 24 * (1 - a)) for c in MAU["tim2"]), anchor="ma")
    if sp.get("nguon"): d.text((W / 2, H - 58), "Nguồn: " + sp["nguon"], font=F("Medium", 26), fill=MO, anchor="ma")
    return im, d

def cot(sp, t):
    im, d = nen(sp, t); rows = sp["hang"]; n = len(rows)
    mxp = max([v for _, v in rows] + [0]); mxn = -min([v for _, v in rows] + [0]); mx = sp.get("max") or (mxp + mxn) * 1.15 or 1
    x0, x1 = 110, W - 110; bw = (x1 - x0) / n; top = 200; bot = H - 150; hl = set(sp.get("noi", []))
    if any(d.textlength(l_, font=F("Bold", 32)) > bw * 0.94 for l_, _ in rows): bot -= 40   # nhãn 2 dòng: nâng trục để không chạm dòng nguồn
    # 13/11 NV1: giữ đúng số chữ số thập phân của số liệu gốc (RV1311GDP V1: 9,95 hiện "9,9%", 9,85 hiện "9,8%" – lệch lời đọc)
    def _nd(v):
        if sp.get("nd") is not None: return sp["nd"]
        return min(2, len(("%r" % float(v)).split(".")[1].rstrip("0")))   # (17/11 NV1, RV1711VANG V1: 134,5 hiện "134", 49 hiện "49,0") giữ đúng số lẻ gốc, số nguyên không thêm ",0"
    yb = top + (bot - top) * (mxp * 1.08 / ((mxp + mxn) * 1.08 or 1)) if mxn else bot   # trục 0 (có số âm thì trục nâng lên)
    for i, (lab, v) in enumerate(rows):
        a = ease((t - 0.3 - i * 0.35) / 0.9)
        h = (bot - top) / 1.15 * v / mx * a; cx = x0 + bw * i + bw / 2
        c = MAU["do"] if v < 0 else (MAU["vang"] if i in hl else MAU["tim"])
        if a > 0:
            y_a, y_b = (yb - max(h, 4), yb) if v >= 0 else (yb, yb - h)
            d.rounded_rectangle([cx - bw * 0.32, y_a, cx + bw * 0.32, max(y_b, y_a + 4)], 14, fill=c)
        # (25/11 NV1, RV2411LS V1: 3 nhãn "Cao nhất 12/2023"... đè nhau) nhãn rộng hơn cột thì xuống 2 dòng + tự co chữ
        fz = 32; dl = [lab]
        if d.textlength(lab, font=F("Bold", fz)) > bw * 0.94 and " " in lab:
            w_ = lab.split(" "); k = min(range(1, len(w_)), key=lambda j: max(d.textlength(" ".join(w_[:j]), font=F("Bold", fz)), d.textlength(" ".join(w_[j:]), font=F("Bold", fz))))
            dl = [" ".join(w_[:k]), " ".join(w_[k:])]
        while fz > 22 and max(d.textlength(s_, font=F("Bold", fz)) for s_ in dl) > bw * 0.94: fz -= 2
        y_l = (yb + 16) if v >= 0 else (yb - 56 - (len(dl) - 1) * (fz + 4))
        for j, s_ in enumerate(dl): d.text((cx, y_l + j * (fz + 4)), s_, font=F("Bold", fz), fill=MO, anchor="ma")
        if a > 0.05: d.text((cx, (yb - h - 62) if v >= 0 else (yb - h + 14)), so(v * a, sp.get("dv", ""), _nd(v)), font=F("Black", 46), fill=MAU["trang"], anchor="ma")
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
    # 13/11 NV1: canh giữa theo chiều dọc + tự co chữ khi tràn ngang (RV1311GDP V1: chữ dồn mép trên, nửa dưới thẻ trống)
    im, d = nen(sp, t); dong = []
    for s, sz, c in sp["dong"]:
        s = s.replace("→", "»")   # (25/11 QL1, SN2511NOXAU: font Black không có ký tự mũi tên → bị mất, hiện khoảng trắng)
        while sz > 30 and d.textlength(s, font=F("Black", sz)) > W - 90: sz -= 4
        dong.append((s, sz, c))
    tong = sum(int(sz * 1.35) for _, sz, _ in dong); y = max(200, int(200 + (H - 150 - 200 - tong) / 2))
    for i, (s, sz, c) in enumerate(dong):
        a = ease((t - 0.3 - i * 0.55) / 0.5)
        if a > 0:
            col = tuple(int(x * a + 24 * (1 - a)) for x in MAU.get(c, MAU["trang"]))
            d.text((W / 2, y + (1 - a) * 30), s, font=F("Black", sz), fill=col, anchor="ma")
        y += int(sz * 1.35)
    return im

# ======= ĐỒ HOẠ CHUYỂN ĐỘNG (25/11 QL1, học awesome-opus5-5-videos + anh Huy: "ảnh có liên quan không"):
# mỗi cảnh 1 Ý HÌNH vẽ bằng code thay ảnh Wikimedia lạc đề. Dùng trong "the" với "anh": [] để không chèn ảnh.
#   giam:    "a": [nhãn, số], "b": [nhãn, số], "dv": " TỶ", "dau": "MẤT GẦN MỘT NỬA"   – 2 cột trước/sau, cột sau tụt xuống, dấu đỏ
#   dem:     "n": 26, "to": "26 THỬA ĐẤT", "phu": "..."                               – ô đất bật lên từng ô, đếm số
#   chuoi:   "buoc": ["ĐẤT KHÓ BÁN", "NỢ XẤU KHÓ XỬ LÝ", ...], "mau": ["trang","do",...] – chuỗi nhân quả, mũi tên vẽ tay
#   dong_ho: "a": 128, "b": 107, "dv": "%", "max": 150, "moc": 100, "nhan": "TECHCOMBANK", "phu": "..." – kim tụt
#   pheu:    "tren": ["NỢ NHÓM 2", "1,63%", "TRỄ HẠN < 90 NGÀY"], "duoi": ["NỢ XẤU", "2,12%"] – hạt rơi từ nhóm 2 xuống nợ xấu
import math
def _mui_ten(d, x, y0, y1, col, a):
    if a <= 0: return
    yb = y0 + (y1 - y0) * a
    d.line([(x, y0), (x, yb)], fill=col, width=10)
    if a > 0.6: d.polygon([(x - 26, yb - 24), (x + 26, yb - 24), (x, yb + 8)], fill=col)

def giam(sp, t):
    im, d = nen(sp, t); (la, va), (lb, vb) = sp["a"], sp["b"]; dv = sp.get("dv", "")
    bot = H - 190; top = 330; hmax = bot - top - 60
    def _n(v): return sp.get("nd", min(2, len(("%r" % float(v)).split(".")[1].rstrip("0"))))
    for i, (lab, v, col) in enumerate([(la, va, MAU["tim2"]), (lb, vb, MAU["vang"])]):
        cx = W * (0.3 if i == 0 else 0.7)
        a = ease((t - 0.3) / 0.8) if i == 0 else ease((t - 1.4) / 1.2)
        if i == 1:   # cột sau: mọc bằng cột trước rồi TỤT xuống mức thật
            hh = hmax * (1 - (1 - vb / va) * ease((t - 1.4) / 1.6)) * min(1, (t - 0.9) / 0.5) if t > 0.9 else 0
        else: hh = hmax * a
        if hh > 2: d.rounded_rectangle([cx - 120, bot - hh, cx + 120, bot], 20, fill=col)
        d.text((cx, bot + 18), lab, font=F("Bold", 34), fill=MO, anchor="ma")
        if hh > 2:
            vv = va if i == 0 else va - (va - vb) * ease((t - 1.4) / 1.6)
            d.text((cx, bot - hh - 66), so(vv, dv, _n(va if i == 0 else vb)), font=F("Black", 54), fill=MAU["trang"], anchor="ma")
    a = ease((t - 3.0) / 0.4)
    if a > 0 and sp.get("dau"):
        txt = sp["dau"]; f = F("Black", 50); tw = d.textlength(txt, font=f)
        st = Image.new("RGBA", (int(tw + 60), 90), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
        sd.rounded_rectangle([0, 0, st.width - 1, 89], 16, outline=MAU["do"] + (255,), width=6)
        sd.text((30, 14), txt, font=f, fill=MAU["do"] + (255,))
        st = st.rotate(-6, expand=True, resample=Image.BICUBIC); k = (1.3 - 0.4 * a) * 0.85
        st = st.resize((int(st.width * k), int(st.height * k)))
        im.paste(st, (int(W / 2 - st.width / 2), int(118)), st)
    return im

def dem(sp, t):
    im, d = nen(sp, t); n = int(sp["n"]); cols = 7 if n > 20 else 5; rows = math.ceil(n / cols)
    cw = (W - 160) / cols; ch = min(cw * 0.8, (H - 470) / rows); x0 = 80; y0 = 190
    shown = 0
    for i in range(n):
        a = ease((t - 0.3 - i * 0.07) / 0.25)
        if a <= 0: continue
        shown = i + 1; r, c = divmod(i, cols); cx = x0 + cw * c + cw / 2; cy = y0 + ch * r + ch / 2
        s = (ch * 0.36) * (0.6 + 0.4 * a)
        d.rectangle([cx - s, cy - s * 0.2, cx + s, cy + s * 0.9], fill=MAU["tim2"])           # nền nhà/thửa
        d.polygon([(cx - s * 1.15, cy - s * 0.15), (cx, cy - s), (cx + s * 1.15, cy - s * 0.15)], fill=MAU["vang"])  # mái
        d.rectangle([cx - s * 0.2, cy + s * 0.35, cx + s * 0.2, cy + s * 0.9], fill=BG)
    yt = y0 + ch * rows + 40
    d.text((W / 2, yt), sp.get("to", "%d" % shown).replace(str(n), str(shown), 1), font=F("Black", 78), fill=MAU["vang"], anchor="ma")
    if sp.get("phu"):
        a = ease((t - 0.3 - n * 0.07) / 0.5)
        if a > 0: d.text((W / 2, yt + 100), sp["phu"], font=F("Bold", 38), fill=tuple(int(x * a + 24 * (1 - a)) for x in MAU["trang"]), anchor="ma")
    return im

def chuoi(sp, t):
    im, d = nen(sp, t); b = sp["buoc"]; n = len(b); mau = sp.get("mau", [])
    gap = 70; bh = min(120, (H - 330 - gap * (n - 1)) / n); y = 200 + ((H - 330) - (bh * n + gap * (n - 1))) / 2
    for i, s in enumerate(b):
        a = ease((t - 0.3 - i * 0.9) / 0.5)
        if a > 0:
            col = MAU.get(mau[i] if i < len(mau) else ("do" if i == n - 1 else "tim"), MAU["tim"])
            w = (W - 160) * (0.85 + 0.15 * a); x = (W - w) / 2
            d.rounded_rectangle([x, y + (1 - a) * 20, x + w, y + bh + (1 - a) * 20], 24, fill=col)
            fz = 50
            while fz > 28 and d.textlength(s, font=F("Black", fz)) > w - 50: fz -= 2
            d.text((W / 2, y + bh / 2 + (1 - a) * 20), s, font=F("Black", fz), fill=(20, 10, 30) if col == MAU["vang"] else MAU["trang"], anchor="mm")
        if i < n - 1: _mui_ten(d, W / 2, y + bh + 6, y + bh + gap - 14, MAU["vang"], ease((t - 0.3 - i * 0.9 - 0.5) / 0.35))
        y += bh + gap
    return im

def dong_ho(sp, t):
    im, d = nen(sp, t); mx = sp.get("max", 150); cx, cy, R = W / 2, H - 230, 290
    d.arc([cx - R, cy - R, cx + R, cy + R], 180, 360, fill=(70, 40, 110), width=46)
    if sp.get("moc") is not None:   # vùng dưới mốc = đỏ
        am = 180 + 180 * sp["moc"] / mx
        d.arc([cx - R, cy - R, cx + R, cy + R], 180, am, fill=(120, 40, 60), width=46)
        x = cx + (R + 40) * math.cos(math.radians(am)); y = cy + (R + 40) * math.sin(math.radians(am))
        d.text((x, y - 10), "%s%s" % (sp["moc"], sp.get("dv", "")), font=F("Bold", 30), fill=MO, anchor="mm")
    v = sp["a"] + (sp["b"] - sp["a"]) * ease((t - 0.8) / 1.6) if t > 0.3 else sp["a"]
    ang = math.radians(180 + 180 * min(v, mx) / mx)
    d.line([(cx, cy), (cx + (R - 40) * math.cos(ang), cy + (R - 40) * math.sin(ang))], fill=MAU["vang"], width=14)
    d.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=MAU["vang"])
    d.text((cx, cy + 40), so(v, sp.get("dv", ""), 0), font=F("Black", 96), fill=MAU["do"] if v < sp.get("moc", -1e9) + 10 else MAU["trang"], anchor="ma")
    if sp.get("nhan"): d.text((cx, 150), sp["nhan"], font=F("Black", 46), fill=MAU["trang"], anchor="ma")
    if sp.get("phu"):
        a = ease((t - 2.6) / 0.5)
        if a > 0: d.text((cx, 214), sp["phu"], font=F("Bold", 34), fill=MAU["vang"], anchor="ma")
    return im

def pheu(sp, t):
    im, d = nen(sp, t); tr, du = sp["tren"], sp["duoi"]
    bx = [(140, 170, W - 140, 400), (140, H - 330, W - 140, H - 120)]
    for k, (box, info, col) in enumerate([(bx[0], tr, MAU["vang"]), (bx[1], du, MAU["do"])]):
        a = ease((t - 0.3 - k * 0.6) / 0.5)
        if a <= 0: continue
        d.rounded_rectangle(box, 28, outline=col, width=6)
        d.text((W / 2, box[1] + 22), info[0], font=F("Black", 46), fill=col, anchor="ma")
        d.text((W / 2, box[1] + 82), info[1], font=F("Black", 84), fill=MAU["trang"], anchor="ma")
        if len(info) > 2: d.text((W / 2, box[3] - 46), info[2], font=F("Bold", 30), fill=MO, anchor="ma")
    if t > 1.2:   # hạt rơi: nợ nhóm 2 trượt xuống nợ xấu
        for j in range(14):
            ph_ = ((t - 1.2) * 0.55 + j / 14) % 1
            x = W / 2 + math.sin(j * 2.1) * 150 * (1 - ph_ * 0.6); y = 410 + (H - 330 - 420) * ph_
            r = 11
            d.ellipse([x - r, y - r, x + r, y + r], fill=MAU["do"] if ph_ > 0.6 else MAU["vang"])
    return im

def ve(sp, t):
    return {"cot": cot, "thang": thang, "lon": lon, "giam": giam, "dem": dem, "chuoi": chuoi, "dong_ho": dong_ho, "pheu": pheu}[sp.get("loai", "lon")](sp, t)
