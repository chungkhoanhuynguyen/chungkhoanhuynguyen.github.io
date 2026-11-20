# NHỊP HÌNH cho video dài (QL1 20/11, học quy trình motion graphics): cứ 3–5 giây phải có 1 thay đổi hình đi theo lời nói.
#  - mốc câu: phụ đề (_sub, chia theo câu/dấu phẩy, rải theo thời lượng giọng thật) + bám điểm lặng thật trong wav (TTS đọc từng câu, có nghỉ)
#  - "nhịp" = đầu câu cách nhau >= 2,6s; khoảng > 5s thì chèn thêm nhịp -> máy quay đổi hướng + nảy nhẹ ở mỗi nhịp
#  - thẻ/ô/cột/tin nhắn hiện theo CÂU nhắc tới nó (lich); bignum nổi (zoom 1,04 + viền sáng) khi câu nhắc số
#  - 5 giây đầu: tiêu đề IN HOA thật lớn trên ô vàng thương hiệu (bia_hook của meta)
# Chỉ bật cho lô MỚI: lô có tên trong _video/nhip_lo_cu.txt (đã dựng/hẹn trước 20/11) giữ nguyên giao diện cũ.
import os, re, wave, unicodedata
import numpy as np
from PIL import Image, ImageDraw
import dx2

HERE = os.path.dirname(os.path.abspath(__file__))
LW, LH = 1920, 1080
VANG = (255, 196, 0); DO = (255, 92, 92); XANH = (90, 240, 120); INK = (10, 12, 17)
_DO = re.compile(r"^(giảm|mất|lỗ|sập|nghèo|khó|âm|bán|tháo|hoảng|đóng|phá|nợ|rơi|bẫy|rủi|xả|thủng)", re.I)
_XANH = re.compile(r"^(tăng|lãi|giàu|lời|dương|hồi|mua|gom|khỏe|bền|vượt)", re.I)


def bat(batch, g):
    e = os.environ.get("NHIP")
    if e in ("0", "1"): return e == "1"
    if g.get("NHIP") is not None: return bool(g["NHIP"])
    try: cu = set(open(os.path.join(HERE, "nhip_lo_cu.txt"), encoding="utf-8").read().split())
    except Exception: cu = set()
    return batch not in cu


def _lang(path):
    """các mốc 'bắt đầu nói lại' sau 1 quãng lặng >= 0,2s (giây, theo file wav đã cắt/đệm của cảnh)."""
    try:
        with wave.open(path) as w:
            sr = w.getframerate(); x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    except Exception: return []
    hop = int(sr * 0.02); n = len(x) // hop
    if n < 10: return []
    db = 20 * np.log10(np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(1)) + 1e-9)
    q = db < max(-48.0, db.max() - 32); out = []; run = 0
    for i, v in enumerate(q):
        if v: run += 1
        else:
            if run * 0.02 >= 0.2 and i > 15: out.append(i * 0.02)
            run = 0
    return out


def lap(sc, wav, T):
    """sc['_cau'] = [(giây bắt đầu, chữ)], sc['_beats'] = các nhịp hình (giây trong cảnh)."""
    sc["_T"] = T
    ls = _lang(wav); cau = []
    for a, e, c in sc.get("_sub", []):
        if a > 0.05 and ls:
            m = min(ls, key=lambda x: abs(x - a))
            if abs(m - a) < 0.9: a = m
        if cau and a <= cau[-1][0] + 0.3: a = cau[-1][0] + 0.3
        cau.append((round(a, 3), c))
    sc["_cau"] = cau
    bt = [0.0]
    for a, _ in cau:
        if a - bt[-1] >= 2.6 and a < T - 1.2: bt.append(a)
    full = bt + [T]; out = [0.0]
    for x0, x1 in zip(full, full[1:]):
        k = int(np.ceil((x1 - x0) / 4.4))
        for j in range(1, k): out.append(x0 + (x1 - x0) * j / k)
        if x1 < T: out.append(x1)
    sc["_beats"] = sorted(set(round(x, 3) for x in out))
    for k_ in [k for k in sc if k.startswith("_lich")]: sc.pop(k_)


def _bo_dau(s):
    s = unicodedata.normalize("NFD", s.lower()).replace("đ", "d")
    return "".join(ch for ch in s if unicodedata.category(ch) != "Mn")


def _tu(s):
    """dấu hiệu nhận ra 1 mục trong lời đọc: con số (>= 2 chữ số) + cụm 2 chữ liền nhau của nhãn (tránh chữ chung chung)."""
    s = _bo_dau(str(s)); so = [re.sub(r"\D", "", x) for x in re.findall(r"\d[\d.,]*", s)]
    w = re.findall(r"[a-z0-9]+", s)
    return [x for x in so if len(x) >= 2] + [" ".join(w[i:i + 2]) for i in range(len(w) - 1)]


def lich(sc, n, nhan=None, t_min=0.3):
    """thời điểm hiện n mục (thẻ/ô/cột/tin): ưu tiên câu nhắc tới nhãn của mục, còn lại rải đều theo đầu câu."""
    key = "_lich%d" % n
    if key in sc: return sc[key]
    cau = sc.get("_cau") or [(0.0, "")]; T = sc.get("_T", 8.0); hi = max(t_min + 0.5, T - 1.0)
    st = [max(t_min, a) for a, _ in cau]
    out = []
    for i in range(n):
        j = min(len(st) - 1, int(round(i * len(st) / max(1, n))))
        out.append(st[j] if i else t_min)
    if nhan:
        txt = [_bo_dau(c) for _, c in cau]; txt_so = [re.sub(r"[.,]", "", x) for x in txt]; j0 = 0
        for i, lb in enumerate(nhan[:n]):
            for j in range(j0, len(cau)):
                tk = _tu(lb)
                if tk and any((t in txt_so[j]) if t.isdigit() else (t in txt[j]) for t in tk[:6]):
                    out[i] = max(t_min, cau[j][0]); j0 = j; break
    for i in range(n):   # tăng dần, cách nhau >= 0,45s, không quá cuối cảnh
        if i: out[i] = max(out[i], out[i - 1] + 0.45)
    if out and out[-1] > hi:
        sh = out[-1] - hi; out = [max(t_min, x - sh * (k + 1) / n) for k, x in enumerate(out)]
        for i in range(1, n): out[i] = max(out[i], out[i - 1] + 0.3)
    sc[key] = out; return out


def _bump(t, beats, d=0.45):
    """nảy ngắn sau mỗi nhịp (0..1)."""
    for b in beats:
        if b > 0 and 0 <= t - b < d: return np.sin(np.pi * (t - b) / d)
    return 0.0


def cam(im, sc, t):
    """máy quay: zoom/lia liên tục, ĐỔI HƯỚNG ở mỗi nhịp + nảy 1,5% ngay nhịp -> không còn hình đứng yên."""
    bt = sc.get("_beats") or [0.0]; T = sc.get("_T", 8.0); full = bt + [max(T, bt[-1] + 0.5)]
    k = max(i for i, b in enumerate(bt) if b <= t + 1e-6); u = (t - full[k]) / max(0.3, full[k + 1] - full[k]); u = min(1.0, max(0.0, u))
    u = u * u * (3 - 2 * u)
    zk = lambda i: 1.0 + (0.03 if (i + sc.get("_idx", 0)) % 2 else 0.006)
    xk = lambda i: (0.42, 0.58, 0.5, 0.46)[(i + sc.get("_idx", 0)) % 4]
    z = zk(k) + (zk(k + 1) - zk(k)) * u + 0.015 * _bump(t, bt); fx = xk(k) + (xk(k + 1) - xk(k)) * u
    w, h = LW / z, LH / z; x0 = (LW - w) * fx; y0 = (LH - h) * 0.5
    return im.resize((LW, LH), Image.BILINEAR, box=(x0, y0, x0 + w, y0 + h))


def noi_so(sc, t):
    """bignum: 0..1 khi câu đang đọc có con số (zoom 1,04 + viền sáng)."""
    for a, c in sc.get("_cau", []):
        if re.search(r"\d", c) and 0 <= t - a < 0.9: return float(np.sin(np.pi * min(1.0, (t - a) / 0.9)))
    return 0.0


def vien(im, box, a):
    if a <= 0.01: return
    d = ImageDraw.Draw(im, "RGBA")
    for r, al in ((10, 60), (5, 120), (0, 230)):
        d.rounded_rectangle([box[0] - r, box[1] - r, box[2] + r, box[3] + r], 22 + r, outline=VANG + (int(al * a),), width=4)


def mau_tu(w, base):
    if re.search(r"\d", w): return VANG if base != VANG else (255, 236, 150)
    if _DO.match(w): return DO
    if _XANH.match(w): return XANH
    return base


def chu_mau(d, x, y, line, f, base, a=1.0, bg=INK, stroke=0):
    """vẽ 1 dòng cap từng chữ: số nổi VÀNG, chữ xấu ĐỎ, chữ tốt XANH."""
    sp = d.textlength(" ", font=f)
    for w in line.split(" "):
        c = dx2.mix(mau_tu(w, base), a, bg)
        d.text((x, y), w, font=f, fill=c, stroke_width=stroke, stroke_fill=(0, 0, 0)); x += d.textlength(w, font=f) + sp


def hook(im, t, title):
    """5 giây đầu: tiêu đề IN HOA thật lớn (>= 96px) trên ô vàng thương hiệu."""
    if not title or t >= 5.0: return im
    a = min(1.0, t / 0.25) * (1.0 if t < 4.5 else max(0.0, (5.0 - t) / 0.5))
    ps = [re.sub(r"\s+", " ", x.upper().strip()) for x in ([title] if isinstance(title, str) else title)]; d = ImageDraw.Draw(im, "RGBA")
    sz = 120; mw = 1560
    while True:
        f = dx2.F("Black", sz); ln = []
        for s in ps:
            ln.append("")
            for w in s.split():
                if not ln[-1] or d.textlength(ln[-1] + " " + w, font=f) <= mw: ln[-1] = (ln[-1] + " " + w).strip()
                else: ln.append(w)
        if (len(ln) <= len(ps) and len(ln) <= 3) or sz <= 96: break   # mỗi phần 1 dòng nếu được, chữ không dưới 96px
        sz -= 4
    lh = int(sz * 1.16); tw = max(d.textlength(l, font=f) for l in ln); bh = lh * len(ln) + 70
    sc_ = 1.0; bw = (tw + 110) * sc_; bh2 = bh * sc_
    x0 = (LW - bw) / 2; y0 = (LH - bh2) / 2 - 40
    d.rectangle([0, 0, LW, LH], fill=(0, 0, 0, int(120 * a)))
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh2], 28, fill=VANG + (int(245 * a),))
    y = y0 + 35 * sc_
    for l in ln:
        w_ = d.textlength(l, font=f); d.text(((LW - w_) / 2, y), l, font=f, fill=INK + (int(255 * a),)); y += lh
    return im
