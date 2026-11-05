# Khung REEL DỌC 1080x1920 (TikTok / FB Reel / YouTube Shorts) – thương hiệu tím-vàng Huy Nguyễn.
# Học công thức "9 PHÚT KINH DOANH": tiêu đề vàng 2 tầng cố định trên cùng, ảnh thật ở giữa, chữ to theo lời,
# cuối khung: miễn trừ chữ nhỏ (không đọc) + chungkhoanhuynguyen.com (anh Huy chốt 6/11: bỏ dải vàng).
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
        f = fit(d, s, "Black", W - 90, 104 if i == 0 else 88); tw = d.textlength(s, font=f)
        c = VANG if i == 0 else TRANG
        d.text((W/2 - tw/2, y), s, font=f, fill=c, stroke_width=7, stroke_fill=(12, 4, 24))
        y += int(f.size * 1.16)
    return y

def ve_anh(im, ph, t, T, y0, y1):
    """Ảnh thật ở giữa (zoom chậm Ken Burns), viền tím sáng."""
    bw, bh = W - 72, y1 - y0; x0 = 36
    if ph is not None:
        z = 1.0 + 0.08 * min(1, t / max(T, 0.1))
        r = max(bw / ph.width, bh / ph.height) * z
        p = ph.resize((int(ph.width * r) + 1, int(ph.height * r) + 1), Image.BILINEAR)
        ox = (p.width - bw) // 2; oy = (p.height - bh) // 2
        p = p.crop((ox, oy, ox + bw, oy + bh))
    else:
        p = Image.new("RGB", (bw, bh), (34, 16, 60)); dd = ImageDraw.Draw(p)
        for k in range(0, bw + bh, 46): dd.line([k, 0, k - bh, bh], fill=(44, 22, 76), width=14)
    m = Image.new("L", (bw, bh), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, bw - 1, bh - 1], 34, fill=255)
    gl = Image.new("L", (W, H), 0); ImageDraw.Draw(gl).rounded_rectangle([x0 - 6, y0 - 6, x0 + bw + 5, y0 + bh + 5], 40, fill=255)
    im.paste(Image.new("RGB", (W, H), TIM_S), (0, 0), gl.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(im).rounded_rectangle([x0 - 4, y0 - 4, x0 + bw + 3, y0 + bh + 3], 38, fill=TIM_S)
    im.paste(p, (x0, y0), m)
    sh = Image.new("RGBA", (bw, 260), (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    for k in range(260): sd.line([0, k, bw, k], fill=(10, 4, 20, int(200 * k / 260)))
    im.paste(sh, (x0, y0 + bh - 260), Image.composite(sh, Image.new("RGBA", sh.size), m.crop((0, bh - 260, bw, bh))))

def ve_chu_to(im, s, t, yb):
    """Chữ to của cảnh: dập vào cuối khung ảnh."""
    if not s: return
    s = s.replace("→", "»")
    d = ImageDraw.Draw(im, "RGBA"); a = dx2.ease(t / 0.35); sc = 1.25 - 0.25 * a
    f = fit(d, s, "Black", W - 170, int(84 * sc)); tw = d.textlength(s, font=f)
    x = W/2 - tw/2; y = yb - f.size - 46
    d.rounded_rectangle([x - 28, y - 14, x + tw + 28, y + f.size + 22], 18, fill=(VANG[0], VANG[1], VANG[2], int(255 * a)))
    d.text((x, y), s, font=f, fill=(24, 8, 44, int(255 * a)))

def tach(txt, mx=30):
    w = txt.split(); out = []; cur = ""
    for x in w:
        if len(cur) + len(x) + 1 > mx and cur: out.append(cur); cur = x
        else: cur = (cur + " " + x).strip()
    if cur: out.append(cur)
    return out

def ve_phu_de(im, loi, t, T, y):
    """Lời chạy theo giọng: 2 dòng/lượt, dòng đang đọc sáng vàng."""
    ds = tach(loi); n = len(ds)
    if not n: return
    k = min(n - 1, int(t / max(T, 0.1) * n)); g0 = (k // 3) * 3
    d = ImageDraw.Draw(im); f = F("ExtraBold", 56)
    for i, s in enumerate(ds[g0:g0 + 3]):
        c = VANG if g0 + i == k else TRANG; tw = d.textlength(s, font=f)
        d.text((W/2 - tw/2, y + i * 78), s, font=f, fill=c, stroke_width=5, stroke_fill=(12, 4, 24))

MIEN_TRU = "Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán."
_MT = re.compile(r"\s*[^.!?]*(chia sẻ kiến thức|không phải (là )?khuyến nghị)[^.!?]*[.!?]?", re.I)
def bo_mien_tru(t):
    """Câu miễn trừ không đọc, không chạy phụ đề – đã in chữ nhỏ cố định ở cuối khung."""
    return _MT.sub("", t or "").strip()

def ve_cuoi(im, prog):
    """Cuối khung: vạch tiến độ mảnh + chữ miễn trừ nhỏ + tên web."""
    d = ImageDraw.Draw(im); y0 = H - 190
    d.rectangle([0, y0, W, y0 + 5], fill=(46, 20, 78)); d.rectangle([0, y0, int(W * prog), y0 + 5], fill=TIM_S)
    fm = F("Medium", 24); d.text((W/2 - d.textlength(MIEN_TRU, font=fm)/2, y0 + 34), MIEN_TRU, font=fm, fill=(168, 150, 196))
    u1, u2 = "chungkhoanhuynguyen", ".com"; fu = F("Bold", 32); fd = F("SemiBold", 32)
    wu = d.textlength(u1, font=fu) + d.textlength(u2, font=fd); x = W/2 - wu/2; yu = H - 96
    d.text((x, yu), u1, font=fu, fill=TRANG); d.text((x + d.textlength(u1, font=fu), yu), u2, font=fd, fill=VANG)

def khung(R, i, t, T, ph, tong_t, tong_T):
    im = NEN.copy(); c = R["canh"][i]
    yb = ve_dau(im, R.get("hook"), R.get("nhan"))
    y0 = max(yb + 24, 430); y1 = 1360
    ve_anh(im, ph, t, T, y0, y1)
    ve_chu_to(im, c.get("chu_to", ""), t, y1)
    ve_phu_de(im, bo_mien_tru(c.get("loi", "")), t, T, 1420)
    ve_cuoi(im, tong_t / max(tong_T, 0.1))
    return im

def anh_canh(R, kho):
    out = []
    for c in R["canh"]:
        ph = None
        if kho is not None:
            try: ph = kho.cho({"anh": c.get("anh", ""), "label": c.get("chu_to", ""), "say": c.get("loi", "")}, R.get("tieu_de", ""))
            except Exception as e: print("anh: bo qua", e, flush=True)
        out.append(ph)
    return out

def main():
    lo, key = sys.argv[1], sys.argv[2]; QD = os.path.join(HERE, "queue", lo)
    OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True); WORK = "/tmp/reel_" + key; os.makedirs(WORK, exist_ok=True)
    R = next(r for r in json.load(open(os.path.join(QD, "reel.json"), encoding="utf-8")) if r["key"] == key)
    try:
        import anh; kho = anh.Kho(WORK + "/anh")
    except Exception: kho = None
    phs = anh_canh(R, kho) if "--khong-anh" not in sys.argv else [None] * len(R["canh"])
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
            "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.08,areverse,atempo=1.08,apad=pad_dur=%.2f" % pad,
            "-ar", "44100", "-ac", "1", dst])
        with wave.open(dst) as w: b.append(b[-1] + w.getnframes() / w.getframerate())
        parts.append(dst)
    print(key, "giong %.0fs, dai %.1fs" % (time.time() - t0, b[-1]), flush=True)
    lst = WORK + "/list.txt"; open(lst, "w").write("".join("file '%s'\n" % p for p in parts)); A = WORK + "/full.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", A])
    tmp = WORK + "/v.mp4"
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H), "-r", str(FPS), "-i", "-",
                          "-i", A, "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "21", "-preset", "veryfast",
                          "-af", "highpass=f=120,loudnorm=I=-14:TP=-1:LRA=7", "-c:a", "aac", "-b:a", "192k", "-shortest", tmp], stdin=subprocess.PIPE)
    fr = 0
    for i in range(len(R["canh"])):
        n = int(round(b[i + 1] * FPS)) - fr; T = n / FPS
        for j in range(n): p.stdin.write(khung(R, i, j / FPS, T, phs[i], (fr + j) / FPS, b[-1]).tobytes())
        fr += n
    p.stdin.close(); p.wait()
    out = os.path.join(OUT, key + ".mp4")
    try:
        import music; music.mix(tmp, b, out, music_db=-17)
    except Exception as e:
        print("nhac: bo qua", e, flush=True); os.replace(tmp, out)
    khung(R, 0, 1.5, 4, phs[0], 1.5, b[-1]).resize((540, 960), Image.LANCZOS).save(os.path.join(OUT, key + "_bia.png"))
    cap = R.get("short_caption") or R.get("tieu_de", "")
    open(os.path.join(OUT, key + "_mo_ta.txt"), "w", encoding="utf-8").write(
        cap + "\n\n📌 Huy Nguyễn Chứng Khoán\n🌐 chungkhoanhuynguyen.com\n💬 Zalo tư vấn: 0365 188 286\n" +
        (" ".join("#" + t.lstrip("#") for t in R.get("tags", [])) + "\n"))
    if kho is not None and getattr(kho, "credit", None):
        open(os.path.join(OUT, key + "_anh.txt"), "w", encoding="utf-8").write("Ảnh minh hoạ (Wikimedia Commons):\n" + "\n".join(kho.credit) + "\n")
    print(key, "xong", out, "%.1fs" % b[-1], flush=True)

if __name__ == "__main__":
    main()
