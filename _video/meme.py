# KIỂU SHORT "MEME ĐỐI LẬP" (Studio 26/11, học reel FPT anh Huy 24/11 – 20 giây, 1,6K view).
# Bật bằng "kieu": "meme" trong reel.json; reel.py tự chuyển sang đây, các kiểu Short cũ KHÔNG đổi.
# Màn dọc chia đôi: NỬA TRÊN = tiêu đề cố định 2 dòng + biểu đồ giá (điểm trong json hoặc ảnh) + câu chốt chơi chữ;
# NỬA DƯỚI = clip thật đời thường đối lập (tiệc, nhảy…), KHÔNG lời đọc, nhạc lofi nhẹ; số liệu nằm ở caption dài.
# reel.json (1 phần tử):
#  {"key": "SN2611MEME", "kieu": "meme", "thoi_luong": 20,
#   "tieu_de": ["DÒNG 1 TRẮNG", "DÒNG 2 VÀNG"], "nhan": "25/11/2026", "cau_chot": "Câu chốt chơi chữ",
#   "bieu_do": {"tieu": "...", "diem": [["nhãn", giá trị], ...], "dv": "", "nguon": "...", "mau": "do"|"xanh"}
#        hoặc "anh_bieu_do": "file.png" (ảnh trong thư mục lô),
#   "clip": {"url": "...", "tu": 2, "den": 8}  hoặc  [ {..}, {..}, {..} ]   (≤7 giây mỗi đoạn, tối đa 3 đoạn; tự lặp/nối cho đủ),
#   "clip_du_phong": [ {..} ]     (tải đoạn chính lỗi thì thử các đoạn này),
#   "nguon_clip": "Wikimedia Commons – tên file (CC BY-SA)", "giu_tieng": 0|1,
#   "anh_duoi": "file.jpg" hoặc "tu_khoa_anh": "Commons query"   (không có clip -> ảnh tĩnh Ken Burns),
#   "caption": "caption dài có số liệu + nguồn", "binh_chon": ["1: ...", "2: ..."], "tags": [], "music_db": -6}
import os, re, json, subprocess, shutil, urllib.request
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import reel
from reel import W, H, FPS, F, fit, TRANG, VANG, TIM_S, TIM0, TIM1
import dx2

H_TREN = 980                 # nửa trên (tiêu đề + biểu đồ + câu chốt)
H_DUOI = H - H_TREN          # nửa dưới: clip thật
DO = (255, 72, 72); XANH = (64, 214, 120); MO = (176, 164, 206)
CACHE = os.path.expanduser("~/.cache/hn_clip")

def _seg(x):
    """Chuẩn hoá đoạn clip: ≤7 giây (luật bản quyền QL1 26/11)."""
    tu = float(x.get("tu", 0)); den = float(x.get("den", tu + 6))
    den = min(den, tu + 7.0)
    return {"url": x["url"], "tu": tu, "den": max(den, tu + 1.0)}

def _media(url):
    return bool(re.search(r"\.(mp4|webm|mov|m4v|ogv|mkv)(\?|$)", url, re.I) or "Special:FilePath" in url)

def tai(url):
    """Tải clip 1 lần (cache ~/.cache/hn_clip). Link file trực tiếp -> urllib; còn lại (YouTube, báo) -> yt-dlp."""
    os.makedirs(CACHE, exist_ok=True)
    k = re.sub(r"[^A-Za-z0-9]+", "_", url)[-80:]
    for f in os.listdir(CACHE):
        if f.startswith(k + ".") and os.path.getsize(os.path.join(CACHE, f)) > 10000: return os.path.join(CACHE, f)
    if _media(url):
        dst = os.path.join(CACHE, k + ".bin")
        rq = urllib.request.Request(url, headers={"User-Agent": "HuyNguyenStudio/1.0 (chungkhoanhuynguyen.com)"})
        with urllib.request.urlopen(rq, timeout=120) as r, open(dst, "wb") as o: shutil.copyfileobj(r, o)
        return dst
    ytd = shutil.which("yt-dlp") or "yt-dlp"
    subprocess.run([ytd, "-q", "--no-playlist", "-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]/b",
                    "--merge-output-format", "mp4", "-o", os.path.join(CACHE, k + ".%(ext)s"), url], check=True, timeout=600)
    for f in os.listdir(CACHE):
        if f.startswith(k + "."): return os.path.join(CACHE, f)
    raise RuntimeError("yt-dlp không ra file")

def _dai(p):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-i", p], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", e)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0

def cat(src, s, dst, giu):
    """Cắt 1 đoạn, phủ kín khung nửa dưới 1080xH_DUOI, 30 fps; tắt tiếng gốc trừ khi giu_tieng."""
    vf = "scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,fps=%d,setsar=1" % (W, H_DUOI, W, H_DUOI, FPS)
    a = ["-c:a", "aac", "-ar", "44100", "-ac", "2"] if giu else ["-an"]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "%.2f" % s["tu"], "-i", src, "-t", "%.2f" % (s["den"] - s["tu"]),
                    "-vf", vf] + a + ["-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p", dst], check=True)
    d = _dai(dst)
    if d < 0.8: raise RuntimeError("đoạn cắt quá ngắn (%.1fs) – kiểm tra tu/den" % d)
    return d

def lam_duoi(R, WORK, T):
    """Ghép nửa dưới đủ T giây: nối các đoạn, lặp lại cho đủ. Trả (đường dẫn mp4, danh sách nguồn) hoặc (None, [])."""
    giu = int(R.get("giu_tieng", 0))
    cl = R.get("clip") or []; cl = cl if isinstance(cl, list) else [cl]
    du = R.get("clip_du_phong") or []; du = du if isinstance(du, list) else [du]
    segs = []; dung = []
    for nhom in ([_seg(c) for c in cl if c.get("url")], [_seg(c) for c in du if c.get("url")]):   # đoạn chính lỗi hết mới dùng dự phòng
        if segs: break
        for x in nhom:
            if len(segs) >= 3: break
            try:
                p = "%s/seg%d.mp4" % (WORK, len(segs)); d = cat(tai(x["url"]), x, p, giu); segs.append((p, d)); dung.append(x)
                print("clip: dung", x["url"], "%.1f-%.1fs" % (x["tu"], x["den"]), flush=True)
            except Exception as e: print("clip: bo qua", x["url"], e, flush=True)
    if not segs: return None, []
    lst = []; tot = 0.0; i = 0
    while tot < T + 0.5: p, d = segs[i % len(segs)]; lst.append(p); tot += d; i += 1
    open(WORK + "/duoi.txt", "w").write("".join("file '%s'\n" % p for p in lst))
    out = WORK + "/duoi.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", WORK + "/duoi.txt", "-t", "%.2f" % T,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-pix_fmt", "yuv420p"] + (["-c:a", "aac"] if giu else ["-an"]) + [out], check=True)
    return out, dung

def anh_tinh(R, QD, WORK):
    """Không có clip: ảnh tĩnh trong lô (anh_duoi) hoặc tìm theo từ khoá (Kho ảnh Commons) -> Ken Burns."""
    if R.get("anh_duoi"):
        try: return Image.open(os.path.join(QD, R["anh_duoi"])).convert("RGB")
        except Exception as e: print("anh_duoi: loi", e, flush=True)
    if R.get("tu_khoa_anh"):
        try:
            import anh; kho = anh.Kho(WORK + "/anh")
            ph = kho.cho({"anh": R["tu_khoa_anh"], "chat": 1}, "")
            if ph is not None: R["_credit"] = getattr(kho, "credit", []); return ph.convert("RGB")
        except Exception as e: print("tu_khoa_anh: loi", e, flush=True)
    return None

def doc_khung(p):
    """Đọc lần lượt từng khung nửa dưới từ mp4 (không nạp cả clip vào RAM)."""
    pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", p, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    n = W * H_DUOI * 3; last = None
    while True:
        b = pr.stdout.read(n)
        if len(b) < n: break
        last = Image.frombytes("RGB", (W, H_DUOI), b); yield last
    while last is not None: yield last   # clip hụt vài khung: giữ khung cuối

# ---------------- NỬA TRÊN ----------------
def nen_tren():
    g = np.linspace(0, 1, H_TREN)[:, None]
    a = np.array(TIM1)[None, None, :] * (1 - g[..., None]) + np.array(TIM0)[None, None, :] * g[..., None]
    return Image.fromarray(np.repeat(a, W, axis=1).astype(np.uint8))
NEN_T = nen_tren()

def so(v, nd=2):
    return ("{:,.%df}" % nd).format(v).replace(",", "§").replace(".", ",").replace("§", ".")

def ve_tieu_de(im, td, nhan):
    d = ImageDraw.Draw(im, "RGBA"); y = 40
    if nhan:
        fn = F("Bold", 28); tw = d.textlength(nhan.upper(), font=fn)
        d.rounded_rectangle([W/2 - tw/2 - 22, y, W/2 + tw/2 + 22, y + 48], 24, fill=(196, 40, 52)); d.text((W/2 - tw/2, y + 7), nhan.upper(), font=fn, fill=TRANG)
        y += 66
    for i, s in enumerate((td or ["", ""])[:2]):
        f = fit(d, s, "Black", W - 80, 86); tw = d.textlength(s, font=f)
        d.text((W/2 - tw/2, y), s, font=f, fill=TRANG if i == 0 else VANG, stroke_width=7, stroke_fill=(12, 4, 24)); y += int(f.size * 1.18)
    return y

def ve_bieu_do(im, bd, t, y0, y1, anh_bd=None):
    """Đường giá vẽ dần trong 2,2 giây (đỏ nếu giảm), chấm + nhãn từng điểm, số cuối nổi bật."""
    d = ImageDraw.Draw(im, "RGBA"); x0, x1 = 60, W - 60
    d.rounded_rectangle([x0 - 20, y0, x1 + 20, y1], 30, fill=(16, 6, 32, 220), outline=TIM_S + (160,), width=3)
    if anh_bd is not None:
        r = min((x1 - x0) / anh_bd.width, (y1 - y0 - 40) / anh_bd.height); q = anh_bd.resize((int(anh_bd.width * r), int(anh_bd.height * r)))
        im.paste(q, (W // 2 - q.width // 2, (y0 + y1) // 2 - q.height // 2)); return
    if not bd or not bd.get("diem"): return
    if bd.get("tieu"): d.text((W/2, y0 + 22), bd["tieu"], font=fit(d, bd["tieu"], "ExtraBold", x1 - x0 - 40, 36), fill=TIM_S, anchor="ma")
    if bd.get("nguon"): d.text((W/2, y1 - 40), "Nguồn: " + bd["nguon"], font=F("Medium", 22), fill=MO, anchor="ma")
    P = bd["diem"]; v = [float(p[1]) for p in P]; lo, hi = min(v), max(v); pad = (hi - lo) * 0.18 or 1
    gy0, gy1 = y0 + 120, y1 - 120; gx0, gx1 = x0 + 70, x1 - 70
    xs = [gx0 + (gx1 - gx0) * i / max(1, len(v) - 1) for i in range(len(v))]
    ys = [gy1 - (gy1 - gy0) * (z - lo + pad) / (hi - lo + 2 * pad) for z in v]
    for k in range(5):  # lưới mờ
        yy = gy0 + (gy1 - gy0) * k / 4; d.line([gx0 - 30, yy, gx1 + 30, yy], fill=(90, 60, 140, 90), width=2)
    giam = v[-1] < v[0] if bd.get("mau") not in ("do", "xanh") else bd["mau"] == "do"
    mau = DO if giam else XANH
    u = dx2.ease(min(1, t / 2.2)); L = (len(v) - 1) * u; k_ = int(L); fr = L - k_
    pts = [(xs[i], ys[i]) for i in range(k_ + 1)]
    if k_ < len(v) - 1: pts.append((xs[k_] + (xs[k_ + 1] - xs[k_]) * fr, ys[k_] + (ys[k_ + 1] - ys[k_]) * fr))
    if len(pts) > 1:
        poly = pts + [(pts[-1][0], gy1 + 40), (pts[0][0], gy1 + 40)]
        d.polygon(poly, fill=mau + (46,))
        d.line(pts, fill=mau + (255,), width=9, joint="curve")
    fl = F("Bold", 26); fv = F("ExtraBold", 34)
    for i in range(min(len(v), k_ + 1)):
        d.ellipse([xs[i] - 11, ys[i] - 11, xs[i] + 11, ys[i] + 11], fill=TRANG, outline=mau, width=4)
        tren = ys[i] <= (sum(ys) / len(ys))
        yv = ys[i] - 64 if tren else ys[i] + 18; yl = ys[i] - 96 if tren else ys[i] + 56
        c = (VANG if i == len(v) - 1 else TRANG)
        d.text((xs[i], yv), so(v[i], bd.get("nd", 2)) + bd.get("dv", ""), font=fv, fill=c, anchor="ma", stroke_width=4, stroke_fill=(12, 4, 24))
        d.text((xs[i], yl), str(P[i][0]), font=fl, fill=MO, anchor="ma")

def ve_cau_chot(im, s, t, T, y):
    """Câu chốt chơi chữ: dập vào sau 35% thời lượng, ô vàng chữ tối, nằm ngay trên mép chia đôi."""
    if not s: return
    t0 = max(2.4, T * 0.3)
    if t < t0: return
    d = ImageDraw.Draw(im, "RGBA"); a = dx2.ease(min(1, (t - t0) / 0.3)); sc = 1.2 - 0.2 * a
    ls = s.split("\n") if "\n" in s else [s]
    f = F("Black", int(fit(d, max(ls, key=len), "Black", W - 140, 64).size * sc)); hh = int(f.size * 1.22)
    tw = max(d.textlength(l, font=f) for l in ls)
    yb = y - hh * len(ls) - 30
    d.rounded_rectangle([W/2 - tw/2 - 30, yb - 14, W/2 + tw/2 + 30, y - 12], 20, fill=VANG + (int(255 * a),))
    for i, l in enumerate(ls):
        d.text((W/2, yb + i * hh), l, font=f, fill=(24, 8, 44, int(255 * a)), anchor="ma")

def khung_tren(R, t, T, anh_bd, yb):
    im = NEN_T.copy()
    ve_bieu_do(im, R.get("bieu_do"), t, yb + 10, H_TREN - 215, anh_bd)
    ve_cau_chot(im, R.get("cau_chot", ""), t, T, H_TREN)
    return im

def ghep(R, tren, duoi, t, T):
    im = Image.new("RGB", (W, H)); im.paste(tren, (0, 0)); im.paste(duoi, (0, H_TREN))
    d = ImageDraw.Draw(im, "RGBA")
    d.rectangle([0, H_TREN - 4, W, H_TREN + 4], fill=VANG)               # vạch chia đôi
    if R.get("nguon_clip"):
        s = "Clip: " + R["nguon_clip"]; f = F("Medium", 22); tw = d.textlength(s, font=f)
        if tw > W - 60: s = s[:60] + "…"; tw = d.textlength(s, font=f)
        d.rounded_rectangle([24, H_TREN + 20, 24 + tw + 24, H_TREN + 56], 12, fill=(0, 0, 0, 140)); d.text((36, H_TREN + 25), s, font=f, fill=(230, 230, 230))
    u1, u2 = "chungkhoanhuynguyen", ".com"; fu = F("Bold", 32); fd = F("SemiBold", 32)
    wu = d.textlength(u1, font=fu) + d.textlength(u2, font=fd); x = W/2 - wu/2; yu = H - 120
    d.rounded_rectangle([x - 22, yu - 10, x + wu + 22, yu + 48], 18, fill=(16, 6, 32, 190))
    d.text((x, yu), u1, font=fu, fill=TRANG); d.text((x + d.textlength(u1, font=fu), yu), u2, font=fd, fill=VANG)
    d.rectangle([0, H - 8, int(W * t / max(T, .1)), H], fill=TIM_S)   # vạch tiến độ mảnh
    return im

def lam(R, QD, OUT, WORK, key):
    T = max(15.0, min(25.0, float(R.get("thoi_luong", 20))))
    anh_bd = None
    if R.get("anh_bieu_do"):
        try: anh_bd = Image.open(os.path.join(QD, R["anh_bieu_do"])).convert("RGB")
        except Exception as e: print("anh_bieu_do: loi", e, flush=True)
    yb = ve_tieu_de(NEN_T, R.get("tieu_de_2dong") or R.get("hook") or ["", ""], R.get("nhan"))   # tiêu đề cố định: vẽ thẳng vào nền 1 lần
    duoi, dung = lam_duoi(R, WORK, T)
    if duoi: src = doc_khung(duoi); ph = None
    else:
        src = None; ph = anh_tinh(R, QD, WORK)
        print("meme: KHONG co clip ->", "anh tinh Ken Burns" if ph is not None else "nen trong", flush=True)
    giu = int(R.get("giu_tieng", 0)) and duoi
    tmp = WORK + "/v.mp4"; n = int(round(T * FPS))
    ain = ["-i", duoi] if giu else ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H), "-r", str(FPS), "-i", "-"] + ain +
                         ["-map", "0:v", "-map", "1:a", "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "17", "-g", "60", "-preset", "veryfast",
                          "-c:a", "aac", "-b:a", "192k", "-t", "%.3f" % T, tmp], stdin=subprocess.PIPE)
    bia = None
    for j in range(n):
        t = j / FPS
        if src is not None: dd = next(src)
        elif ph is not None: dd = reel.anh_khung(ph, t, T, W, H_DUOI, 0)
        else: dd = Image.new("RGB", (W, H_DUOI), (34, 16, 60))
        fr = ghep(R, khung_tren(R, t, T, anh_bd, yb), dd, t, T)
        if bia is None and t >= T * 0.55: bia = fr.copy()
        p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
    out = os.path.join(OUT, key + ".mp4")
    try:
        import music
        music.mix(tmp, [0.0, T], out, music_db=R.get("music_db", -4 if giu else 0), lofi=True, whoosh=0)
    except Exception as e:
        print("nhac: bo qua", e, flush=True); os.replace(tmp, out)
    (bia or fr).resize((540, 960), Image.LANCZOS).save(os.path.join(OUT, key + "_bia.png"))
    cap = (R.get("caption") or "").strip()
    bc = R.get("binh_chon")
    if bc: cap += "\n\n👉 Anh chị chọn " + " hay ".join(str(i + 1) for i in range(len(bc))) + "?\n" + "\n".join(bc)
    nguon = [c["url"] for c in dung]
    if R.get("nguon_clip") or nguon: cap += "\n\n🎬 Clip minh hoạ: " + (R.get("nguon_clip") or "") + ((" – " + " ; ".join(nguon)) if nguon else "")
    if R.get("_credit"): cap += "\n🖼 Ảnh: " + "; ".join(R["_credit"])
    open(os.path.join(OUT, key + "_mo_ta.txt"), "w", encoding="utf-8").write(
        cap + "\n\n📌 Huy Nguyễn Chứng Khoán\n🌐 chungkhoanhuynguyen.com\n" + " ".join("#" + t_.lstrip("#") for t_ in R.get("tags", [])) + "\n")
    qc = [] if duoi else ["CẢNH BÁO: không tải được clip, nửa dưới dùng " + ("ảnh tĩnh" if ph is not None else "nền trống")]
    open(os.path.join(OUT, key + "_qc.txt"), "w", encoding="utf-8").write(("\n".join(qc) or "ĐẠT (kiểu meme, không lời đọc)") + "\n")
    print(key, "meme xong", out, "%.1fs" % T, flush=True)
