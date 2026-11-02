# Dựng video KỂ CHUYỆN dọc 1080x1920 từ ảnh nhân vật chibi (AI vẽ sẵn) + bối cảnh + giọng chốt + hiệu ứng âm thanh + nhạc.
# Dùng: python _video/story/ke_chuyen.py <file_truyen.json> <out.mp4>
# Truyện: {"bg": {"ten": "assets/bg_pho.png"}, "canh": [{"bg": "...", "nv": [{"anh": "assets/cun_bo_vui.png", "x": 0.3, "vao": "nhay|truot_trai|truot_phai|hien", "dien": "giat_minh|nga|..."}],
#          "say": "lời đọc", "chu": ["DÒNG 1", "DÒNG 2"], "sfx": ["ting", ...]}]}
import sys, os, json, math, subprocess, time, io
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); VID = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(VID, "engine")); sys.path.insert(0, VID)
import am_thanh, music
W, H, FPS = 1080, 1920, 30
truyen = json.load(open(sys.argv[1], encoding="utf-8")); OUT = sys.argv[2]
base = os.path.dirname(os.path.abspath(sys.argv[1]))
WORK = "/tmp/kc_" + os.path.basename(OUT).split(".")[0]; os.makedirs(WORK, exist_ok=True)
FONT = os.path.join(VID, "engine", "fonts", "BeVietnamPro-Black.ttf")

# ---------- 1) tách nền nhân vật (rembg, miễn phí) ----------
from rembg import remove, new_session
ses = new_session("isnet-general-use")
_SP = {}
def sprite(p, h_px):
    k = (p, h_px)
    if k not in _SP:
        src = Image.open(os.path.join(base, p)).convert("RGBA")
        cut = remove(src, session=ses)
        bb = cut.getbbox(); cut = cut.crop(bb)
        r = h_px / cut.height; cut = cut.resize((int(cut.width * r), h_px), Image.LANCZOS)
        _SP[k] = cut
    return _SP[k]
_BG = {}
def nen(p):
    if p not in _BG:
        im = Image.open(os.path.join(base, p)).convert("RGB")
        r = max(W * 1.12 / im.width, H * 1.12 / im.height)
        _BG[p] = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    return _BG[p]

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
    sp = sprite(nv["anh"], int(nv.get("cao", 0.5) * H))
    cx = nv.get("x", 0.5) * W; by = nv.get("y", 0.93) * H
    vao = nv.get("vao", "hien"); a = 1.0; dx = dy = 0; sc = 1.0; rot = 0
    if vao == "nhay": sc = back(t / 0.45)
    elif vao == "truot_trai": dx = -(1 - ease(t / 0.6)) * W
    elif vao == "truot_phai": dx = (1 - ease(t / 0.6)) * W
    dy = -abs(math.sin(t * 5.5)) * 10 if nv.get("noi") else math.sin(t * 2.2) * 6       # nhún khi nói / thở
    fx = DIEN_FX.get(nv.get("dien", ""), "")
    if fx == "nhay" and t < 0.6: dy -= math.sin(t / 0.6 * math.pi) * 120
    if fx == "run": dx += math.sin(t * 40) * 6
    if fx == "lac": rot = math.sin(t * 6) * 4
    if fx == "nhun": sc *= 1 + abs(math.sin(t * 7)) * 0.03
    if fx == "nga": rot = -min(1, t / 0.4) * 20
    if sc <= 0.01: return
    s2 = sp.resize((max(1, int(sp.width * sc)), max(1, int(sp.height * sc))), Image.BILINEAR) if sc != 1 else sp
    if rot: s2 = s2.rotate(rot, resample=Image.BILINEAR, expand=True)
    sh = Image.new("RGBA", (s2.width, 40), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse([s2.width * 0.15, 0, s2.width * 0.85, 40], fill=(0, 0, 0, 70))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)), (int(cx + dx - s2.width / 2), int(by - 22)))
    im.alpha_composite(s2, (int(cx + dx - s2.width / 2), int(by + dy - s2.height)))
def frame(c, t, T, i):
    bg = nen(c.get("bg") or truyen["bg"]); z = 1 + 0.04 * t / max(T, 0.1)
    ww, hh = int(W * z), int(H * z); ox = (bg.width - ww) // 2; oy = (bg.height - hh) // 2
    im = bg.crop((ox, oy, ox + ww, oy + hh)).resize((W, H), Image.BILINEAR).convert("RGBA")
    for nv in c.get("nv", []): draw_nv(im, nv, t, i)
    chu(im, [(l, tuple(c.get("mau", [(40, 44, 60), (230, 60, 70)])[j % 2])) for j, l in enumerate(c.get("chu", []))], t)
    d = ImageDraw.Draw(im); f = ImageFont.truetype(FONT, 30); s = "chungkhoanhuynguyen.com"
    d.text(((W - d.textlength(s, font=f)) / 2, H - 90), s, font=f, fill=(255, 255, 255), stroke_width=4, stroke_fill=(60, 60, 80))
    return im.convert("RGB")
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
