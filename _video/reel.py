# Khung REEL DỌC 1080x1920 (TikTok / FB Reel / YouTube Shorts) – thương hiệu tím-vàng Huy Nguyễn.
# Học công thức "9 PHÚT KINH DOANH": tiêu đề vàng 2 tầng cố định trên cùng, ảnh thật ở giữa, chữ to theo lời,
# cuối khung: chungkhoanhuynguyen.com (anh Huy chốt 6/11: bỏ dải vàng, bỏ câu miễn trừ).
# Kết bài = CÂU HỎI MỞ gây tranh luận (R["cau_hoi"] = {chu_to, loi, loi_doc}) thay cảnh "xem video đầy đủ".
# Đầu vào: _video/queue/<LÔ>/reel.json = [{key, hook:[dòng1, dòng2], canh:[{chu_to, loi, loi_doc, anh?}], nhan?}]
# Dùng: python _video/reel.py <LÔ> <KEY>        (--khung: chỉ xuất 3 ảnh khung mẫu, không đọc giọng)
import sys, os, re, json, subprocess, wave, time
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "engine")); sys.path.insert(0, HERE)
os.environ.setdefault("HN_PX", "/tmp/_px_rong.json")
if not os.path.exists(os.environ["HN_PX"]): json.dump({}, open(os.environ["HN_PX"], "w"))
import dx2
W, H, FPS = 1080, 1920, 30
TIM0, TIM1 = (22, 9, 40), (58, 22, 96)
TIM = (124, 58, 237); TIM_S = (196, 140, 255)
VANG = (255, 214, 64); VANG2 = (242, 176, 38); TRANG = (255, 255, 255); KEM = (242, 234, 216)
F = dx2.F

def nen():
    g = np.linspace(0, 1, H)[:, None]
    a = np.array(TIM1)[None, None, :] * (1 - g[..., None]) + np.array(TIM0)[None, None, :] * g[..., None]
    a = np.repeat(a, W, axis=1).astype(np.uint8); im = Image.fromarray(a)
    gl = Image.new("L", (W, H), 0); ImageDraw.Draw(gl).ellipse([W*.15, 300, W*.85, 1400], fill=90)
    gl = gl.filter(ImageFilter.GaussianBlur(160))
    return Image.composite(Image.new("RGB", (W, H), TIM), im, gl)
NEN = nen()

def fit(d, s, w, mw, st):
    f = F(w, st)
    while d.textlength(s, font=f) > mw and f.size > 30: f = F(w, f.size - 3)
    return f

def ve_dau(im, hook, nhan, a=1.0):
    """Tiêu đề 2 tầng cố định trên cùng (vàng / trắng) + nhãn nhỏ."""
    d = ImageDraw.Draw(im, "RGBA")
    nhan = (nhan or "TIN NÓNG · VĨ MÔ").upper(); fn = F("Bold", 30); tw = d.textlength(nhan, font=fn)
    d.rounded_rectangle([W/2 - tw/2 - 26, 92, W/2 + tw/2 + 26, 146], 27, fill=(196, 40, 52))
    d.text((W/2 - tw/2, 99), nhan, font=fn, fill=TRANG)
    y = 176
    for i, s in enumerate((hook or ["", ""])[:2]):
        if not s: continue
        if i == 1 and s.rstrip().endswith("?"):   # QL1 11/11: khuôn câu hỏi (học trang reel 28K–228K view): dòng 2 trong ô vàng, chữ tối
            f = fit(d, s, "Black", W - 130, 92); tw = d.textlength(s, font=f); h = int(f.size * 1.22)
            d.rounded_rectangle([W/2 - tw/2 - 26, y + 4, W/2 + tw/2 + 26, y + h + 8], 18, fill=VANG)
            d.text((W/2 - tw/2, y + 6), s, font=f, fill=(24, 10, 40))
            y += h + 22; continue
        f = fit(d, s, "Black", W - 90, 104 if i == 0 else 88); tw = d.textlength(s, font=f)
        c = TRANG if (len(hook) > 1 and str(hook[1]).rstrip().endswith("?")) else (VANG if i == 0 else TRANG)
        d.text((W/2 - tw/2, y), s, font=f, fill=c, stroke_width=7, stroke_fill=(12, 4, 24))
        y += int(f.size * 1.16)
    return y

def anh_khung(ph, t, T, bw, bh, k=0):
    """Cắt 1 khung ảnh: Ken Burns đổi hướng theo k (phóng vào / lùi ra / lia trái-phải)."""
    if ph.info.get("the"):  # thẻ số liệu CHẠY: cột mọc, số đếm lên (anh Huy 7/11)
        import the_so; ph = the_so.ve(ph.info["the"], t); ph.info["fit"] = 1
    if ph.info.get("fit"):  # thẻ số liệu: giữ trọn khung, phóng rất nhẹ
        r = min(bw / ph.width, bh / ph.height) * (1.0 + 0.02 * min(1, t / max(T, 0.1)))
        q = ph.resize((int(ph.width * r), int(ph.height * r)), Image.BILINEAR)
        p = Image.new("RGB", (bw, bh), (20, 10, 38)); p.paste(q, ((bw - q.width) // 2, (bh - q.height) // 2)); return p
    u = dx2.ease(min(1, t / max(T, 0.1))) if hasattr(dx2, "ease") else min(1, t / max(T, 0.1))
    z = 1.04 + 0.10 * (u if k % 2 == 0 else 1 - u)
    r = max(bw / ph.width, bh / ph.height) * z
    q = ph.resize((int(ph.width * r) + 1, int(ph.height * r) + 1), Image.BILINEAR)
    mx, my = q.width - bw, q.height - bh
    px = (u if k % 4 in (1, 2) else 1 - u) if k % 4 else 0.5
    return q.crop((int(mx * px), my // 2, int(mx * px) + bw, my // 2 + bh))

def ve_anh(im, ph, t, T, y0, y1, ready=None):
    """Ảnh thật ở giữa (zoom chậm Ken Burns), viền tím sáng."""
    bw, bh = W - 72, y1 - y0; x0 = 36
    if ready is not None: p = ready
    elif ph is not None: p = anh_khung(ph, t, T, bw, bh)
    else:
        p = Image.new("RGB", (bw, bh), (34, 16, 60)); dd = ImageDraw.Draw(p)
        for k in range(0, bw + bh, 46): dd.line([k, 0, k - bh, bh], fill=(44, 22, 76), width=14)
    m = Image.new("L", (bw, bh), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, bw - 1, bh - 1], 34, fill=255)
    gl = Image.new("L", (W, H), 0); ImageDraw.Draw(gl).rounded_rectangle([x0 - 6, y0 - 6, x0 + bw + 5, y0 + bh + 5], 40, fill=255)
    im.paste(Image.new("RGB", (W, H), TIM_S), (0, 0), gl.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(im).rounded_rectangle([x0 - 4, y0 - 4, x0 + bw + 3, y0 + bh + 3], 38, fill=TIM_S)
    im.paste(p, (x0, y0), m)
    if ph is not None and ph.info.get("fit"): return
    sh = Image.new("RGBA", (bw, 260), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    for k in range(260): sd.line([0, k, bw, k], fill=(10, 4, 20, int(200 * k / 260)))
    im.paste(sh, (x0, y0 + bh - 260), Image.composite(sh, Image.new("RGBA", sh.size), m.crop((0, bh - 260, bw, bh))))

def ve_chu_to(im, s, t, yb, hoi=0):
    """Chữ to của cảnh: dập vào cuối khung ảnh."""
    if not s: return
    s = s.replace("→", "»")
    d = ImageDraw.Draw(im, "RGBA"); a = dx2.ease(t / 0.35); sc = 1.25 - 0.25 * a
    f = fit(d, s, "Black", W - 170, int(84 * sc)); tw = d.textlength(s, font=f)
    x = W/2 - tw/2; y = yb - f.size - 46
    nen_, chu_ = ((214, 38, 52), (255, 255, 255)) if hoi else (VANG, (24, 8, 44))
    d.rounded_rectangle([x - 28, y - 14, x + tw + 28, y + f.size + 22], 18, fill=nen_ + (int(255 * a),))
    d.text((x, y), s, font=f, fill=chu_ + (int(255 * a),))

PD_F = 54; PD_W = W - 130
def _rong(s): return ImageDraw.Draw(NEN).textlength(s, font=F("ExtraBold", PD_F))
def _chia2(ws):
    """Chia 1 cụm thành ≤2 dòng cân nhau (độ dài gần bằng nhau, không dòng nào vượt khung)."""
    if _rong(" ".join(ws)) <= PD_W: return [" ".join(ws)]
    best = None
    for k in range(1, len(ws)):
        a, b = " ".join(ws[:k]), " ".join(ws[k:]); ra, rb = _rong(a), _rong(b)
        if ra > PD_W or rb > PD_W: continue
        sc = abs(ra - rb) - (40 if ws[k - 1][-1:] in ",;:" else 0)
        if best is None or sc < best[0]: best = (sc, [a, b])
    return best[1] if best else None
def tach(txt):
    """Phụ đề kiểu chuẩn: tách theo câu/dấu phẩy thành cụm ≤2 dòng cân đối."""
    cum = []
    for cau in re.split(r"(?<=[.!?…])\s+", (txt or "").strip()):
        ws = cau.split()
        while ws:
            n = len(ws)
            while n > 1 and _chia2(ws[:n]) is None: n -= 1
            # ưu tiên ngắt ở dấu phẩy gần cuối cụm
            for m in range(n, max(1, n - 5), -1):
                if ws[m - 1][-1:] in ",;:" and m < len(ws): n = m; break
            cum.append(_chia2(ws[:n]) or [" ".join(ws[:n])]); ws = ws[n:]
    return cum

XANH = (90, 240, 120); DO = (255, 92, 92)
_DO = re.compile(r"^(giảm|mất|lỗ|sập|nghèo|khó|âm|bán|tháo|hoảng|đóng|phá|nợ)", re.I)
_XANH = re.compile(r"^(tăng|lãi|giàu|lời|dương|hồi|mua|gom)", re.I)
def _mau(w):
    """Từ khoá đổi màu như video mẫu: số = vàng, xấu = đỏ, tốt = xanh."""
    if re.search(r"\d", w): return VANG
    if _DO.match(w): return DO
    if _XANH.match(w): return XANH
    return TRANG
def ve_phu_de(im, loi, t, T, y, pop=True):
    """Phụ đề: từng cụm 1–2 dòng căn giữa, đổi cụm theo tỉ lệ số chữ; cụm mới NẢY lên + từ khoá đổi màu (học video mẫu 9/11)."""
    cum = tach(loi)
    if not cum: return
    L = [len(" ".join(c)) for c in cum]; tot = sum(L); a = 0; k = len(cum) - 1; st = 0
    for i, l in enumerate(L):
        if t < a + l / tot * T: k = i; st = a; break
        a += l / tot * T
    else: st = a - L[-1] / tot * T
    sc = 1 + (0.14 * (1 - dx2.ease(min(1, (t - st) / 0.16))) if pop else 0)
    d = ImageDraw.Draw(im); f = F("ExtraBold", int(PD_F * sc)); ls = cum[k]; sp = d.textlength(" ", font=f)
    y0 = y + (40 if len(ls) == 1 else 0) - int((sc - 1) * 40)
    for i, s_ in enumerate(ls):
        ws = s_.split(); tw = d.textlength(s_, font=f); x = W/2 - tw/2
        for w_ in ws:
            c_ = _mau(w_)
            d.text((x, y0 + i * 80), w_, font=f, fill=c_, stroke_width=5, stroke_fill=(12, 4, 24))
            x += d.textlength(w_, font=f) + sp

MIEN_TRU = "Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán."
_MT = re.compile(r"\s*[^.!?]*(chia sẻ kiến thức|không phải (là )?khuyến nghị)[^.!?]*[.!?]?", re.I)
def bo_mien_tru(t):
    """Bỏ hẳn câu miễn trừ khỏi lời đọc, phụ đề, mô tả (tin nóng không khuyến nghị mua bán)."""
    return _MT.sub("", t or "").strip()

def ve_cuoi(im, prog):
    """Cuối khung: vạch tiến độ mảnh + tên web (anh Huy 6/11: bỏ câu miễn trừ)."""
    d = ImageDraw.Draw(im); y0 = H - 190
    d.rectangle([0, y0, W, y0 + 5], fill=(46, 20, 78)); d.rectangle([0, y0, int(W * prog), y0 + 5], fill=TIM_S)
    u1, u2 = "chungkhoanhuynguyen", ".com"; fu = F("Bold", 32); fd = F("SemiBold", 32)
    wu = d.textlength(u1, font=fu) + d.textlength(u2, font=fd); x = W/2 - wu/2; yu = H - 130
    d.text((x, yu), u1, font=fu, fill=TRANG); d.text((x + d.textlength(u1, font=fu), yu), u2, font=fd, fill=VANG)
    if prog > 0.9:   # anh Huy 8/11: câu miễn trừ chỉ là chữ nhỏ ở góc, hiện thoáng ở cuối, không đọc
        a = min(1, (prog - 0.9) / 0.02); fm = F("Medium", 22)
        d.text((40, H - 62), "Quan điểm cá nhân, không phải khuyến nghị đầu tư.", font=fm, fill=tuple(int(c * a + 20 * (1 - a)) for c in (150, 140, 175)))

def ve_web_to(im, t, y):
    """Cảnh kéo về web: tên web to giữa khung ảnh."""
    d = ImageDraw.Draw(im, "RGBA"); a = dx2.ease(t / 0.4)
    u1, u2 = "chungkhoanhuynguyen", ".com"; fu = F("Black", 56); fd = F("Bold", 56)
    wu = d.textlength(u1, font=fu) + d.textlength(u2, font=fd); x = W/2 - wu/2
    d.rounded_rectangle([x - 34, y - 26, x + wu + 34, y + 92], 26, fill=(22, 9, 40, int(225 * a)), outline=TIM_S + (int(255 * a),), width=4)
    d.text((x, y), u1, font=fu, fill=TRANG + (int(255 * a),)); d.text((x + d.textlength(u1, font=fu), y), u2, font=fd, fill=VANG + (int(255 * a),))

XF = 0.7   # chuyển cảnh mờ dần (giây)
def doan(seq, t, T, force=None):
    """Chia thời gian cảnh cho chuỗi ảnh; thẻ số liệu (fit) ở cuối giữ 55% thời lượng."""
    n = len(seq); card = n > 1 and seq[-1].info.get("fit")
    if card: lens = [T * 0.22 / (n - 1)] * (n - 1) + [T * 0.78]   # thẻ số liệu giữ lâu cho kịp đọc
    else: lens = [T / n] * n
    if force is not None: return force, 0, lens[force]
    a = 0
    for j, L in enumerate(lens):
        if t < a + L or j == n - 1: return j, t - a, L
        a += L

def ve_tien_do(im, i, n, t, T):
    """Thanh tiến độ chương trên cùng: PHẦN i/n + vạch chạy (học video mẫu 9/11)."""
    d = ImageDraw.Draw(im, "RGBA"); f = F("Bold", 24); s_ = "PHẦN %d/%d" % (i + 1, n); tw = d.textlength(s_, font=f)
    x0, x1, y0 = 250, W - 250, 34
    d.rounded_rectangle([x0, y0, x1, y0 + 44], 14, fill=(16, 6, 32, 210), outline=TIM_S + (200,), width=2)
    d.text((x0 + 22, y0 + 8), s_, font=f, fill=TRANG)
    bx0 = x0 + 44 + tw; bx1 = x1 - 22; p_ = (i + min(1, t / max(T, .1))) / n
    d.rounded_rectangle([bx0, y0 + 18, bx1, y0 + 26], 4, fill=(60, 30, 100, 255))
    d.rounded_rectangle([bx0, y0 + 18, bx0 + int((bx1 - bx0) * p_), y0 + 26], 4, fill=TIM_S + (255,))

def ve_theo_doi(im, t, T):
    """Cảnh cuối: nút THEO DÕI có con trỏ bấm vào rồi chuyển ĐÃ THEO DÕI (học video mẫu 9/11)."""
    t0 = T * 0.35
    if t < t0: return
    d = ImageDraw.Draw(im, "RGBA"); a = dx2.ease(min(1, (t - t0) / 0.3)); da = t > t0 + 1.2
    s_ = "ĐÃ THEO DÕI" if da else "+ THEO DÕI"; f = F("Black", 46); tw = d.textlength(s_, font=f)
    sc = 1 - (0.08 if t0 + 1.1 < t < t0 + 1.3 else 0); w_ = (tw + 90) * sc; h_ = 96 * sc; cx, cy = W / 2, 1645
    nen_ = (70, 60, 90) if da else (236, 40, 64)
    d.rounded_rectangle([cx - w_ / 2, cy - h_ / 2, cx + w_ / 2, cy + h_ / 2], 48, fill=nen_ + (int(245 * a),))
    d.text((cx, cy), s_, font=F("Black", int(46 * sc)), fill=(255, 255, 255, int(255 * a)), anchor="mm")
    k = min(1, max(0, (t - t0 - 0.3) / 0.8)); px, py = cx + 260 - 200 * dx2.ease(k), cy + 140 - 110 * dx2.ease(k)
    d.polygon([(px, py), (px, py + 52), (px + 14, py + 40), (px + 26, py + 64), (px + 36, py + 59), (px + 24, py + 36), (px + 42, py + 36)], fill=(255, 255, 255, int(255 * a)), outline=(0, 0, 0, 255))

def khung(R, i, t, T, ph, tong_t, tong_T):
    im = NEN.copy(); c = R["canh"][i]; hu = R.get("hieu_ung", 1)
    seq0 = ph if isinstance(ph, list) else ([ph] if ph is not None else [])
    if hu and seq0 and not seq0[0].info.get("fit"):   # nền = chính ảnh phóng to, mờ, tối (học video mẫu 9/11)
        b_ = seq0[doan(seq0, t, T)[0]]
        if "_mo" not in b_.info:
            r_ = max(108 / b_.width, 192 / b_.height); q_ = b_.convert("RGB").resize((int(b_.width * r_) + 1, int(b_.height * r_) + 1))
            q_ = q_.crop(((q_.width - 108) // 2, (q_.height - 192) // 2, (q_.width - 108) // 2 + 108, (q_.height - 192) // 2 + 192)).filter(ImageFilter.GaussianBlur(5))
            b_.info["_mo"] = Image.blend(q_.resize((W, H), Image.BILINEAR), NEN, 0.55)
        im = b_.info["_mo"].copy()
    yb = ve_dau(im, R.get("hook"), R.get("nhan"))
    if hu: ve_tien_do(im, i, len(R["canh"]), t, T)
    y0 = max(yb + 24, 430); y1 = 1360
    seq = ph if isinstance(ph, list) else ([ph] if ph is not None else [])
    bw, bh = W - 72, y1 - y0; ready = None; cur = None
    if seq:
        j, tl, Ts = doan(seq, t, T); cur = seq[j]
        ready = anh_khung(cur, tl, Ts, bw, bh, i * 3 + j)
        prev = None
        if tl < XF:
            if j > 0: pj, pT = seq[j - 1], doan(seq, 0, T, j - 1)[2]
            elif i > 0 and R.get("_phs") and R["_phs"][i - 1]: pj = R["_phs"][i - 1][-1]; pT = 4.0
            else: pj = None
            if pj is not None:
                prev = anh_khung(pj, pT, pT, bw, bh, i * 3 + j - 1)
                ready = Image.blend(prev, ready, dx2.ease(tl / XF) if hasattr(dx2, "ease") else tl / XF)
    ve_anh(im, cur, t, T, y0, y1, ready)
    if cur is None or not cur.info.get("fit"): ve_chu_to(im, c.get("chu_to", ""), t, y1, c.get("hoi", 0))
    if c.get("web"): ve_web_to(im, t, (y0 + y1) // 2 - 60)
    ve_phu_de(im, bo_mien_tru(c.get("loi", "")), t, T, 1420)
    ve_cuoi(im, tong_t / max(tong_T, 0.1))
    if hu and c.get("hoi"): ve_theo_doi(im, t, T)
    if hu and i > 0 and t < 0.22:   # punch-in khi sang cảnh mới
        z = 1 + 0.06 * (1 - dx2.ease(t / 0.22)); cw_, ch_ = int(W / z), int(H / z)
        im = im.crop(((W - cw_) // 2, (H - ch_) // 2, (W - cw_) // 2 + cw_, (H - ch_) // 2 + ch_)).resize((W, H), Image.BILINEAR)
    return im

def anh_canh(R, kho, qd=""):
    """Ảnh ĐÚNG lời: mỗi cảnh 1–2 ảnh theo thứ tự câu (đổi ~7 giây/lần, anh Huy 7/11 chê chuyển cảnh nhiều);
    chỉ tìm đúng từ khoá cảnh, không lấy ảnh chung chung. Cảnh có thẻ số liệu: 1 ảnh mở rồi thẻ chạy."""
    out = []
    for c in R["canh"]:
        seq = []; qs = c.get("anh", "")
        qs = qs if isinstance(qs, list) else ([qs] if qs else [])
        dur = len((c.get("loi_doc") or c.get("loi") or "").split()) / 2.6
        co_the = c.get("the") or c.get("hinh")
        can = 1 if co_the else max(1, min(len(qs) or 1, round(dur / 7.0)))
        if co_the and not qs: can = 0
        if kho is not None:
            for k in range(can):
                q = qs[k % len(qs)] if qs else ""
                try:
                    ph = kho.cho({"anh": q, "chat": 1 if q else 0, "label": c.get("chu_to", ""), "say": c.get("loi", "")}, R.get("tieu_de", ""))
                    if ph is not None: seq.append(ph)
                except Exception as e: print("anh: bo qua", e, flush=True)
        if c.get("the"):
            ph = Image.new("RGB", (8, 8)); ph.info["the"] = c["the"]; ph.info["fit"] = 1; seq.append(ph)
        elif c.get("hinh"):
            try: ph = Image.open(os.path.join(qd, c["hinh"])).convert("RGB"); ph.info["fit"] = 1; seq.append(ph)
            except Exception as e: print("hinh: loi", e, flush=True)
        if not seq and out and out[-1]: seq = [x for x in out[-1] if not x.info.get("fit")][-1:]   # không tìm được ảnh: dùng lại ảnh cảnh trước, không để khung trống
        out.append(seq or None)
    R["_phs"] = out
    return out

KEO_WEB = {"chu_to": "SỐ LIỆU 400+ MÃ",   # anh Huy 9/11: nhắc web nhẹ, KHÔNG bảo khách rời nền tảng
    "loi": "Số liệu em dùng lấy từ bảng báo cáo hơn 400 mã em cập nhật mỗi phiên trên chungkhoanhuynguyen.com.",
    "loi_doc": "Số liệu em dùng lấy từ bảng báo cáo hơn bốn trăm mã em cập nhật mỗi phiên trên chứng khoán Huy Nguyễn chấm com."}
def ket_cau_hoi(R):
    """Cảnh cuối là câu hỏi mở để khách bình luận, tranh luận."""
    w = R.get("keo_web", KEO_WEB)          # tin nóng vẫn phải kéo khách về web (anh Huy 6/11)
    if w:
        w = dict(w); w.setdefault("anh", "Ho Chi Minh City Stock Exchange"); w["web"] = 1
        if re.search(r"XEM VIDEO|VIDEO ĐẦY ĐỦ", R["canh"][-1].get("chu_to", ""), re.I): R["canh"][-1] = w
        else: R["canh"].append(w)
    q = R.get("cau_hoi")
    if not q: return
    q = dict(q); q.setdefault("anh", R["canh"][-1].get("anh", "")); q["hoi"] = 1
    R["canh"].append(q)

def main():
    lo, key = sys.argv[1], sys.argv[2]; QD = os.path.join(HERE, "queue", lo)
    OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True); WORK = "/tmp/reel_" + key; os.makedirs(WORK, exist_ok=True)
    R = next(r for r in json.load(open(os.path.join(QD, "reel.json"), encoding="utf-8")) if r["key"] == key)
    ket_cau_hoi(R)
    try:
        import kiem_loi; QC = kiem_loi.kiem([c for c in R["canh"] if not c.get("web") and not c.get("hoi")], R.get("cau_hoi"), True)
    except Exception as e: QC = ["CẢNH BÁO không tự kiểm được văn phong: %s" % e]
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    open(os.path.join(HERE, "out", key + "_qc.txt"), "w", encoding="utf-8").write(("\n".join(QC) or "ĐẠT văn phong") + "\n")
    print(key, "van phong:", QC or "dat", flush=True)
    import xung_ho                      # xưng em – anh chị (anh Huy chốt 6/11)
    for c in R["canh"]:
        for k_ in ("loi", "loi_doc", "chu_to"): c[k_] = xung_ho.le_phep(c.get(k_, ""))
    for k_ in ("short_caption", "tieu_de"): R[k_] = xung_ho.le_phep(R.get(k_, ""))
    if R.get("cau_hoi"): R["cau_hoi"] = {k_: xung_ho.le_phep(v_) for k_, v_ in R["cau_hoi"].items()}
    try:
        import anh; kho = anh.Kho(WORK + "/anh")
    except Exception: kho = None
    phs = anh_canh(R, kho, QD) if "--khong-anh" not in sys.argv else [None] * len(R["canh"])
    if "--khung" in sys.argv:
        for i in (0, len(R["canh"]) // 2, len(R["canh"]) - 1):
            khung(R, i, 1.2, 4, phs[i], i * 4 + 1.2, len(R["canh"]) * 4).save(os.path.join(OUT, "%s_khung%d.png" % (key, i)))
        return
    # giọng chốt (miễn phí, như video dài)
    from vieneu import Vieneu
    vj = os.environ.get("HN_VOICE_JSON")
    if vj: v = json.loads(vj)
    else:
        sys.path.insert(0, os.path.join(HERE, "..")); import hncodec; v = hncodec.load(os.path.join(HERE, "engine", "giong.bin"))
    VOICE = {"speaker_emb": np.asarray(v["speaker_emb"], dtype=np.float32), "codes": np.asarray(v["codes"], dtype=v.get("codes_dtype", "int64"))}
    tts = Vieneu(); parts = []; b = [0.0]; t0 = time.time()
    for i, c in enumerate(R["canh"]):
        src = "%s/%02d_raw.wav" % (WORK, i); dst = "%s/%02d.wav" % (WORK, i)
        tts.save(np.asarray(tts.infer((bo_mien_tru(c.get("loi_doc") or c.get("loi")) or ".").strip(), voice=VOICE, temperature=0.7), dtype=np.float32), src)
        pad = 0.18 + (0.9 if i == len(R["canh"]) - 1 else 0)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af",
            "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.08,areverse,atempo=%.2f,apad=pad_dur=%.2f" % (float(R.get("toc", 1.08)), pad),
            "-ar", "44100", "-ac", "1", dst])
        with wave.open(dst) as w: b.append(b[-1] + w.getnframes() / w.getframerate())
        parts.append(dst)
    print(key, "giong %.0fs, dai %.1fs" % (time.time() - t0, b[-1]), flush=True)
    lst = WORK + "/list.txt"; open(lst, "w").write("".join("file '%s'\n" % p for p in parts)); A = WORK + "/full.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", A])
    tmp = WORK + "/v.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H), "-r", str(FPS), "-i", "-",
                          "-i", A, "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "17", "-g", "60", "-preset", "veryfast",
                          "-af", "highpass=f=120,loudnorm=I=-14:TP=-1:LRA=7", "-c:a", "aac", "-b:a", "192k", "-shortest", tmp], stdin=subprocess.PIPE)
    fr = 0
    for i in range(len(R["canh"])):
        n = int(round(b[i + 1] * FPS)) - fr; T = n / FPS
        for j in range(n): p.stdin.write(khung(R, i, j / FPS, T, phs[i], (fr + j) / FPS, b[-1]).tobytes())
        fr += n
    p.stdin.close(); p.wait()
    out = os.path.join(OUT, key + ".mp4")
    try:
        import music; music.mix(tmp, b, out, music_db=R.get("music_db", -17), lofi=(R.get("nhac") == "lofi"), whoosh=R.get("hieu_ung", 1))
    except Exception as e:
        print("nhac: bo qua", e, flush=True); os.replace(tmp, out)
    khung(R, 0, 1.5, 4, phs[0], 1.5, b[-1]).resize((540, 960), Image.LANCZOS).save(os.path.join(OUT, key + "_bia.png"))
    cap = bo_mien_tru(R.get("short_caption") or R.get("tieu_de", ""))
    if R.get("cau_hoi"): cap = "💬 " + R["cau_hoi"].get("loi", "") + "\n\n" + cap
    open(os.path.join(OUT, key + "_mo_ta.txt"), "w", encoding="utf-8").write(
        cap + "\n\n📌 Huy Nguyễn Chứng Khoán\n🌐 chungkhoanhuynguyen.com\n💬 Zalo tư vấn: 0365 188 286\n" +
        (" ".join("#" + t.lstrip("#") for t in R.get("tags", [])) + "\n"))
    if kho is not None and getattr(kho, "credit", None):
        open(os.path.join(OUT, key + "_anh.txt"), "w", encoding="utf-8").write("Ảnh minh hoạ (Wikimedia Commons):\n" + "\n".join(kho.credit) + "\n" + ("Đã bỏ %d ảnh có mặt người: %s\n" % (len(kho.chan_mat), "; ".join(kho.chan_mat)) if getattr(kho, "chan_mat", None) else ""))
    print(key, "xong", out, "%.1fs" % b[-1], flush=True)

if __name__ == "__main__":
    main()
