# Dựng video KỂ CHUYỆN dọc 1080x1920 từ ảnh nhân vật chibi (AI vẽ sẵn) + bối cảnh + giọng chốt + hiệu ứng âm thanh + nhạc.
# Dùng: python _video/story/ke_chuyen.py <file_truyen.json> <out.mp4>
# Truyện: {"bg": {"ten": "assets/bg_pho.png"}, "canh": [{"bg": "...", "nv": [{"anh": "assets/cun_bo_vui.png", "x": 0.3, "vao": "nhay|truot_trai|truot_phai|hien", "dien": "giat_minh|nga|..."}],
#          "say": "lời đọc", "chu": ["DÒNG 1", "DÒNG 2"], "sfx": ["ting", ...]}]}
import sys, os, json, math, subprocess, time, io
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); VID = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(VID, "engine")); sys.path.insert(0, os.path.dirname(VID))
import am_thanh, music
W, H, FPS = 1080, 1920, 30
truyen = json.load(open(sys.argv[1], encoding="utf-8")); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
WORK = "/tmp/kc_" + os.path.basename(OUT).split(".")[0]; os.makedirs(WORK, exist_ok=True)
FONT = os.path.join(VID, "engine", "fonts", "BeVietnamPro-Black.ttf")

# ---------- 1) tách nền nhân vật (rembg, miễn phí) ----------
from rembg import remove, new_session
ses = new_session("isnet-general-use")
_SP = {}; _BOX = {}
import cv2
def _cut(p):
    src = Image.open(os.path.join(base, p)).convert("RGBA")
    src = src.crop((0, 0, src.width, int(src.height * DE)))            # bỏ bệ tượng
    cut = np.array(remove(src, session=ses)); a = (cut[..., 3] > 40).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(a, 8)
    if n > 1:
        k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])); keep = lab == k
        keep = cv2.dilate(keep.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0
        cut[..., 3] = np.where(keep, cut[..., 3], 0)
    return Image.fromarray(cut)
DE = truyen.get("cat_de", 0.915)
def sprite(p, h_px, ref=None):
    k = (p, h_px)
    if k not in _SP:
        cut = _cut(p); bb = _BOX.get(ref) or cut.getbbox(); _BOX.setdefault(p, bb)
        cut = cut.crop(bb); r = h_px / cut.height
        _SP[k] = np.array(cut.resize((int(cut.width * r), h_px), Image.LANCZOS))
    return _SP[k]
def warp(sp, t, kieu, seed):
    """Biến dạng sống động: đầu nghiêng quanh cổ, thở, tóc đung đưa (giống rối 2.5D)."""
    h, w = sp.shape[:2]; yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    up = 1 - yy / h                                                # 0 chân -> 1 đỉnh đầu
    head = np.clip((up - 0.42) / 0.2, 0, 1) ** 2
    amp = {"noi": 5.0, "vui": 7.0, "ngai": 9.0, "khoc": 4.0}.get(kieu, 3.5)
    ang = math.radians(amp * math.sin(t * 2.3 + seed) + (2.5 * math.sin(t * 9) if kieu == "noi" else 0)) * head
    px, py = w / 2, h * 0.55
    dx = xx - px; dy = yy - py
    sx = px + dx * np.cos(ang) - dy * np.sin(ang); sy = py + dx * np.sin(ang) + dy * np.cos(ang)
    br = 0.018 * math.sin(t * 3.1 + seed)                            # thở: phồng ngang, nén dọc
    sx = w / 2 + (sx - w / 2) / (1 + br * (1 - up) * 0.8)
    sy = h - (h - sy) / (1 - br * 0.5)
    sx += 3.0 * np.sin(t * 2.7 + yy * 0.018 + seed) * np.clip((up - 0.3) / 0.7, 0, 1) * (np.abs(xx - px) / (w / 2))   # tóc đung đưa ở mép
    return cv2.remap(sp, sx, sy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
_BG = {}
def nen(p):
    if p not in _BG:
        im = Image.open(os.path.join(base, p)).convert("RGB")
        r = max(W * 1.12 / im.width, H * 1.12 / im.height)
        _BG[p] = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    return _BG[p]

# ---------- 3) khung hình ----------
def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3
def back(x): x = max(0.0, min(1.0, x)); c = 1.7; return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2
def chu(im, lines, t):
    d = ImageDraw.Draw(im); y = 300
    for i, (txt, col) in enumerate(lines):
        a = ease((t - 0.15 - i * 0.2) / 0.3)
        if a <= 0: continue
        s = 92
        while True:
            f = ImageFont.truetype(FONT, s)
            if d.textlength(txt, font=f) < W - 120 or s < 50: break
            s -= 4
        tw = d.textlength(txt, font=f); x = (W - tw) / 2; yy = y + (1 - a) * 40
        d.text((x, yy), txt, font=f, fill=col, stroke_width=12, stroke_fill=(255, 255, 255))
        y += int(s * 1.25)
DIEN_FX = {"giat_minh": "nhay", "nga": "nga", "khoc_hu": "run", "ngai": "lac", "gai_dau": "lac", "sang_mat": "nhun", "vo_bung": "nhun"}
def draw_nv(im, nv, t, n):
    H0 = int(nv.get("cao", 0.5) * H); anh = nv["anh"]
    if nv.get("noi") and nv.get("anh_noi"):                       # mấp máy môi: đổi 2 ảnh nhịp không đều
        ph = (t * 7.3 + 0.6 * math.sin(t * 3.1)) % 2
        if ph < 1 and int(t * 2.2) % 5 != 4: anh = nv["anh_noi"]
    sp = sprite(anh, H0, nv["anh"] if anh != nv["anh"] else None)
    if anh != nv["anh"]: sprite(nv["anh"], H0)
    kieu = "noi" if nv.get("noi") else {"khoc_hu": "khoc", "ngai": "ngai", "gai_dau": "ngai", "sang_mat": "vui"}.get(nv.get("dien", ""), "")
    arr = warp(sp, t, kieu, n * 1.7 + nv.get("x", 0.5) * 5)
    cx = nv.get("x", 0.5) * W; by = nv.get("y", 0.95) * H
    vao = nv.get("vao", "hien"); dx = dy = 0; sc = 1.0; rot = 0; sx = sy = 1.0
    if vao == "nhay":
        k = t / 0.5; sc = back(k)
        if k < 1.4: sy = 1 + 0.12 * math.sin(min(k, 1.4) * math.pi * 2) * math.exp(-k * 2); sx = 2 - sy   # nảy dẻo khi đáp
    elif vao == "truot_trai": dx = -(1 - ease(t / 0.6)) * W
    elif vao == "truot_phai": dx = (1 - ease(t / 0.6)) * W
    if nv.get("noi"): dy = -abs(math.sin(t * 5.5)) * 12
    else: dy = math.sin(t * 2.2) * 5
    fx = DIEN_FX.get(nv.get("dien", ""), "")
    if fx == "nhay" and t < 0.7:
        k = t / 0.7; dy -= math.sin(k * math.pi) * 160; sy *= 1 + 0.15 * math.sin(k * math.pi); sx = 2 - sy
    if fx == "run": dx += math.sin(t * 40) * 7
    if fx == "lac": rot = math.sin(t * 5) * 3
    if fx == "nhun": s_ = abs(math.sin(t * 6)) * 0.05; sy *= 1 - s_; sx *= 1 + s_
    if fx == "nga": rot = -min(1, t / 0.4) * 18
    if sc <= 0.01: return
    s2 = Image.fromarray(arr)
    nw, nh = max(1, int(s2.width * sc * sx)), max(1, int(s2.height * sc * sy))
    if (nw, nh) != s2.size: s2 = s2.resize((nw, nh), Image.BILINEAR)
    if rot: s2 = s2.rotate(rot, resample=Image.BILINEAR, expand=True)
    sh = Image.new("RGBA", (s2.width, 40), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([s2.width * 0.2, 0, s2.width * 0.8, 40], fill=(0, 0, 0, 80))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)), (int(cx + dx - s2.width / 2), int(by - 22)))
    im.alpha_composite(s2, (int(cx + dx - s2.width / 2), int(by + dy - s2.height)))
def cam(im, c, t, T):
    k = c.get("cam", "")
    z = 1.0; fx, fy = W / 2, H * 0.55; ox = oy = 0
    if k == "can":                                              # đẩy vào cận mặt nhân vật đầu tiên
        nv = c["nv"][0]; fx = nv.get("x", 0.5) * W; fy = nv.get("y", 0.95) * H - nv.get("cao", 0.5) * H * 0.72
        z = 1 + 0.55 * ease(t / 0.7)
    elif k == "giat":                                           # zoom giật + rung
        z = 1.25 if t > 0.12 else 1.0
        fx = c["nv"][0].get("x", 0.5) * W; fy = H * 0.6
    elif k == "lui": z = 1.35 - 0.35 * ease(t / 1.2)
    else: z = 1 + 0.06 * t / max(T, 0.1)
    if any(nv.get("dien") in ("giat_minh", "nga") for nv in c.get("nv", [])) and t < 0.5:
        ox = math.sin(t * 70) * 14 * (1 - t / 0.5); oy = math.cos(t * 55) * 10 * (1 - t / 0.5)
    if z == 1 and not ox: return im
    ww, hh = W / z, H / z
    x0 = min(max(fx - ww / 2 + ox, 0), W - ww); y0 = min(max(fy - hh / 2 + oy, 0), H - hh)
    return im.crop((int(x0), int(y0), int(x0 + ww), int(y0 + hh))).resize((W, H), Image.BILINEAR)
def frame(c, t, T, i):
    bg = nen(c.get("bg") or truyen["bg"]); par = 0.03 * math.sin(t * 0.5)
    ox = int((bg.width - W) / 2 + par * W); oy = (bg.height - H) // 2
    im = bg.crop((ox, oy, ox + W, oy + H)).convert("RGBA")
    for nv in c.get("nv", []): draw_nv(im, nv, t, i)
    im = cam(im, c, t, T)
    chu(im, [(l, tuple(c.get("mau", [(40, 44, 60), (230, 60, 70)])[j % 2])) for j, l in enumerate(c.get("chu", []))], t)
    d = ImageDraw.Draw(im); f = ImageFont.truetype(FONT, 30); s = "chungkhoanhuynguyen.com"
    d.text(((W - d.textlength(s, font=f)) / 2, H - 90), s, font=f, fill=(255, 255, 255), stroke_width=4, stroke_fill=(60, 60, 80))
    return im.convert("RGB")
if os.environ.get("KC_KHUNG"):                 # chế độ xem nhanh khung hình (không đọc giọng)
    ims = [frame(c, tt, 3, i) for i, c in enumerate(truyen["canh"]) for tt in (0.25, 1.2)]
    sm = [x.resize((270, 480)) for x in ims]; o = Image.new("RGB", (270 * 10, 480 * ((len(sm) + 9) // 10)))
    for k, x in enumerate(sm): o.paste(x, ((k % 10) * 270, (k // 10) * 480))
    o.save(OUT); sys.exit()
# ---------- 2) giọng chốt ----------
from vieneu import Vieneu
import hncodec
v = hncodec.load(os.path.join(VID, "engine", "giong.bin"))
VOICE = {"speaker_emb": np.asarray(v["speaker_emb"], dtype=np.float32), "codes": np.asarray(v["codes"], dtype=v.get("codes_dtype", "int64"))}
tts = Vieneu(); dur = []; wavs = []
for i, c in enumerate(truyen["canh"]):
    p = "%s/%02d.wav" % (WORK, i)
    tts.save(np.asarray(tts.infer(c["say"], voice=VOICE, temperature=0.7), dtype=np.float32), p)
    q = "%s/%02dt.wav" % (WORK, i)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", p, "-af",
                    "silenceremove=start_periods=1:start_threshold=-40dB,areverse,silenceremove=start_periods=1:start_threshold=-40dB,areverse,apad=pad_dur=0.35",
                    "-ar", "44100", "-ac", "1", q])
    import wave
    with wave.open(q) as w: dur.append(w.getnframes() / w.getframerate())
    wavs.append(q)
b = [0.0]
for d in dur: b.append(b[-1] + d)
lst = WORK + "/l.txt"; open(lst, "w").write("".join("file '%s'\n" % q for q in wavs))
VOX = WORK + "/vox.wav"; subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", VOX])

tmp = WORK + "/v.mp4"
p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H), "-r", str(FPS), "-i", "-",
                      "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", tmp], stdin=subprocess.PIPE)
fr = 0; ev = []
for i, c in enumerate(truyen["canh"]):
    n = int(round(b[i + 1] * FPS)) - fr
    for nv in c.get("nv", []):
        if nv.get("dien") in am_thanh.DIEN: ev.append((b[i] + 0.1, nv["dien"]))
    for k, s in enumerate(c.get("sfx", [])): ev.append((b[i] + 0.15 + k * 0.4, s))
    if i: ev.append((b[i], "whoosh"))
    for j in range(n): p.stdin.write(frame(c, j / FPS, dur[i], i).tobytes())
    fr += n
p.stdin.close(); p.wait()
# ---------- 4) âm thanh: giọng + hiệu ứng + âm nền, rồi nhạc ----------
sfx = am_thanh.track(b[-1] + 1, ev, truyen.get("am_nen"), nen_db=-26)
SF = WORK + "/sfx.wav"; import wave
with wave.open(SF, "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(44100); w.writeframes((sfx * 32767 * 0.6).astype(np.int16).tobytes())
MIX = WORK + "/mix.mp4"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", VOX, "-i", SF, "-filter_complex",
                "[1:a]loudnorm=I=-15:TP=-1.5[v];[v][2:a]amix=inputs=2:duration=first:normalize=0[a]", "-map", "0:v", "-map", "[a]",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", MIX])
music.mix(MIX, b, OUT)
print("xong", OUT, "%.1fs" % b[-1])
