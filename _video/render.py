# Xưởng video: kịch bản NV1 (S["KEY"]) -> giọng chốt (VieNeu miễn phí) -> dựng dx2 -> nhạc nền -> mp4 + ảnh bìa
# Dùng: python _video/render.py <thư mục lô trong _video/queue> KEY [--preview N]
import sys, os, json, subprocess, shutil, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
batch, key = sys.argv[1], sys.argv[2]
prev = int(sys.argv[sys.argv.index("--preview") + 1]) if "--preview" in sys.argv else 0
QD = os.path.join(HERE, "queue", batch)
OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
WORK = "/tmp/hnv_" + key; os.makedirs(WORK, exist_ok=True)

# 1) nến tuần -> định dạng engine (mới nhất trước, dict o h l c v)
px = {}
p = os.path.join(QD, "px_tuan.json")
if os.path.exists(p):
    for sym, rows in json.load(open(p, encoding="utf-8")).items():
        px[sym] = [{"d": r[0], "o": r[1], "h": r[2], "l": r[3], "c": r[4], "v": r[5]} for r in rows]
json.dump(px, open(WORK + "/px.json", "w")); os.environ["HN_PX"] = WORK + "/px.json"
sys.path.insert(0, os.path.join(HERE, "engine"))
import dx2, music

# 2) kịch bản
g = {}; exec(open(os.path.join(QD, "video_dai.py"), encoding="utf-8").read(), g)
raw = g["S"][key]
if prev: raw = raw[:prev]

def conv(sc):
    s = dict(sc); k = s["k"]
    s.setdefault("label", ""); s.setdefault("cap", ("", ""))
    if k == "hook":
        ch = s.pop("chart", None)
        if ch and ch.get("sym") in px:
            s.update(k="candles", sym=ch["sym"], n=min(int(ch.get("weeks", 52)), len(px[ch["sym"]])),
                     circles=ch.get("circles", []), tag=(lambda t: t if "NẾN TUẦN" in t else t[:40] + " · NẾN TUẦN")((s["label"] or ch["sym"]).upper()), reveal=1.6)
        else: s["k"] = "text"
    elif k == "image":
        if not os.path.exists(os.path.join(HERE, "engine", s.get("img", "?"))): s["k"] = "text"
    elif k == "checklist":
        s["items"] = [it[0] if isinstance(it, (list, tuple)) else it for it in s.get("items", [])]
    elif k == "bars":
        s["bars"] = [(b[0], abs(b[1]) if b[1] else 0.001, b[2], b[3] if len(b) > 3 else str(b[1])) for b in s.get("bars", [])]
    elif k not in dx2.KINDS and k not in ("text", "end"): s["k"] = "text"
    if s["k"] == "text": s.setdefault("y", 860)
    return s
scenes = [conv(s) for s in raw]

# 3) giọng chốt Huy70_HaiDang30 (JSON từ secret HN_VOICE_JSON hoặc file)
from vieneu import Vieneu
vj = os.environ.get("HN_VOICE_JSON")
if vj: v = json.loads(vj)
else:
    sys.path.insert(0, os.path.join(HERE, ".."))
    import hncodec; v = hncodec.load(os.path.join(HERE, "engine", "giong.bin"))
VOICE = {"speaker_emb": np.asarray(v["speaker_emb"], dtype=np.float32), "codes": np.asarray(v["codes"], dtype=v.get("codes_dtype", "int64"))}
tts = Vieneu(); wd = WORK + "/wav"; os.makedirs(wd, exist_ok=True); t0 = time.time()
for i, sc in enumerate(raw):
    say = sc.get("say", "").strip() or "."
    tts.save(np.asarray(tts.infer(say, voice=VOICE, temperature=0.7), dtype=np.float32), "%s/%02d.wav" % (wd, i))
print(key, "giong %.0fs" % (time.time() - t0), flush=True)


# ---- khung NGANG 1920x1080 cho YouTube video dài: ghép từ khung dọc của engine ----
from PIL import Image, ImageDraw, ImageFilter
LW, LH = 1920, 1080
def _bg():
    g = Image.new("RGB", (LW, LH), (13, 16, 23)); d = ImageDraw.Draw(g)
    for r, c in ((900, (18, 22, 31)), (600, (22, 27, 38)), (320, (26, 32, 45))):
        d.ellipse([LW*0.36-r, LH/2-r, LW*0.36+r, LH/2+r], fill=c)
    return g.filter(ImageFilter.GaussianBlur(140))
LBG = _bg()
_CV = {}
def _cover(v, sc):
    key_ = id(sc)
    if key_ not in _CV:
        c = v.resize((480, int(v.height*480/v.width)), Image.BILINEAR).crop((0, 100, 480, 370)).filter(ImageFilter.GaussianBlur(10))
        c = c.resize((LW, LH), Image.BILINEAR)
        _CV[key_] = Image.blend(c, Image.new("RGB", (LW, LH), (8, 10, 15)), 0.55)
    return _CV[key_].copy()
def _prep_ph(sc, ph):
    # nền ảnh thật làm tối + thẻ ảnh sắc nét bên phải
    r = max(LW/ph.width, LH/ph.height); b = ph.resize((int(ph.width*r)+1, int(ph.height*r)+1), Image.LANCZOS)
    b = b.crop(((b.width-LW)//2, (b.height-LH)//2, (b.width-LW)//2+LW, (b.height-LH)//2+LH)).filter(ImageFilter.GaussianBlur(3))
    sc["_bg"] = Image.blend(b, Image.new("RGB", (LW, LH), (8, 10, 15)), 0.66)
    cw, chh = 440, 260; r = max(cw/ph.width, chh/ph.height); c = ph.resize((int(ph.width*r)+1, int(ph.height*r)+1), Image.LANCZOS)
    c = c.crop(((c.width-cw)//2, (c.height-chh)//2, (c.width-cw)//2+cw, (c.height-chh)//2+chh))
    m = Image.new("L", (cw, chh), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, cw-1, chh-1], 18, fill=255)
    sc["_card"] = (c, m)
def land(v, sc, t):
    k = sc["k"]; im = sc["_bg"].copy() if "_bg" in sc else _cover(v, sc)
    if "_bg" in sc:
        fc = dx2.F("SemiBold", 18); ImageDraw.Draw(im).text((24, LH-34), "Ảnh minh hoạ: Wikimedia Commons", font=fc, fill=(150, 156, 170))
    if k in ("end", "text"):
        c = v.crop((0, 200, 1080, 1720)); s = LH/c.height; c = c.resize((int(c.width*s), LH), Image.LANCZOS)
        im.paste(c, ((LW-c.width)//2, 0)); return im
    p = v.crop((66, 470, 1014, 1150)); s = 1.42; p = p.resize((int(p.width*s), int(p.height*s)), Image.LANCZOS)
    im.paste(p, (50, (LH-p.height)//2 + 20))
    d = ImageDraw.Draw(im); x0 = 50 + p.width + 40; cw = LW - x0 - 50; cx = x0 + cw/2
    dx2.brand(im, d, cx, 70, 0.9, 1.0, (10, 12, 17))
    lab = sc.get("label") or ""
    if lab:
        a = dx2.ease(t/0.4); f = dx2.fit(d, lab, "Bold", cw, 34); tw = d.textlength(lab, font=f)
        d.text((cx - tw/2, 300), lab, font=f, fill=dx2.mix(dx2.GOLD, a, (10, 12, 17)))
        d.line([cx - 60, 352, cx + 60, 352], fill=dx2.mix(dx2.GOLD, a, (10, 12, 17)), width=3)
    cols = sc.get("cols") or [dx2.CREAM, dx2.GOLD]; y = 430
    for i, l in enumerate(sc.get("cap") or []):
        if not l: continue
        a = dx2.ease((t - 0.25 - i*0.18)/0.45)
        if a <= 0: continue
        f = dx2.fit(d, l, "Black", cw, 92); c = cols[i] if i < len(cols) else dx2.CREAM
        tw = d.textlength(l, font=f); d.text((cx - tw/2, y + (1-a)*24), l, font=f, fill=dx2.mix(c, a, (10, 12, 17))); y += int(f.size*1.2)
    if "_card" in sc:
        c, m = sc["_card"]; a = dx2.ease((t - 0.5)/0.5)
        if a > 0:
            yy = LH - 110 - c.height + int((1-a)*30); xx = int(cx - c.width/2)
            ImageDraw.Draw(im).rounded_rectangle([xx-4, yy-4, xx+c.width+3, yy+c.height+3], 21, fill=dx2.GOLD)
            im.paste(c, (xx, yy), m)
    f = dx2.F("SemiBold", 26); u = "chungkhoanhuynguyen.com"; d.text((cx - d.textlength(u, font=f)/2, LH - 70), u, font=f, fill=(120, 128, 146))
    return im
def build_land(key, scenes, wav_dir, out, gap=0.28, tail=1.2, tempo=1.0):
    import wave, re
    tmpd = "/tmp/hl_%s_parts" % key; os.makedirs(tmpd, exist_ok=True); parts = []; b = [0.0]
    for i in range(len(scenes)):
        src = os.path.join(wav_dir, "%02d.wav" % i); dst = os.path.join(tmpd, "%02d.wav" % i)
        pad = gap + (tail if i == len(scenes)-1 else 0)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af",
            "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.08,areverse,atempo=%.3f,apad=pad_dur=%.2f" % (tempo, pad),
            "-ar", "44100", "-ac", "1", dst])
        with wave.open(dst) as w: dd = w.getnframes()/w.getframerate()
        b.append(b[-1] + dd); parts.append(dst)
    lst = os.path.join(tmpd, "list.txt"); open(lst, "w").write("".join("file '%s'\n" % p for p in parts))
    A = os.path.join(tmpd, "full.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", A])
    tmp = "/tmp/hl_%s.mp4" % key; FPS = dx2.FPS
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (LW, LH), "-r", str(FPS), "-i", "-",
                          "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", tmp], stdin=subprocess.PIPE)
    fr = 0
    for i, sc in enumerate(scenes):
        n = int(round(b[i+1]*FPS)) - fr
        for j in range(n): p.stdin.write(land(dx2.draw(sc, j/FPS, j/max(1, n)), sc, j/FPS).tobytes())
        fr += n
    p.stdin.close(); p.wait()
    af = ("highpass=f=120,acompressor=threshold=-26dB:ratio=4:attack=3:release=60:makeup=6,"
          "loudnorm=I=-14:TP=-1:LRA=7,alimiter=limit=0.95:attack=1:release=40:level=false")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", A, "-af", af, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest", out])
    return b

# 3b) ảnh minh hoạ thật cho từng cảnh (Commons, miễn phí)
try:
    sys.path.insert(0, HERE); import anh
    kho = anh.Kho(WORK + "/anh"); chu_de = g.get("META", {}).get(key, {}).get("title", "") if isinstance(g.get("META"), dict) else ""
    nph = 0
    for i, sc in enumerate(scenes):
        sc["anh"] = raw[i].get("anh", ""); sc["say"] = raw[i].get("say", ""); sc["ch"] = raw[i].get("ch", "")
        ph = kho.cho(sc, chu_de)
        if ph is not None: _prep_ph(sc, ph); nph += 1
    open(os.path.join(OUT, key + "_anh.txt"), "w", encoding="utf-8").write("Ảnh minh hoạ (Wikimedia Commons):\n" + "\n".join(kho.credit) + "\n")
    print(key, "anh minh hoa", nph, "/", len(scenes), flush=True)
except Exception as e:
    print("anh: bo qua", e, flush=True)

# 4) dựng + nhạc nền
rawmp4 = WORK + "/raw.mp4"; out = os.path.join(OUT, key + ".mp4")
b = build_land(key, scenes, wd, rawmp4, tempo=1.0)
music.mix(rawmp4, b, out)
# 5) ảnh bìa = khung cảnh mở đầu lúc 3 giây
land(dx2.draw(scenes[0], 3.0), scenes[0], 3.0).resize((1280, 720), Image.LANCZOS).save(os.path.join(OUT, key + "_bia.png"))
# 6) mốc chương thật theo giọng (cho mô tả YouTube)
ch = []
for i, sc in enumerate(raw):
    if sc.get("ch"):
        s = int(b[i]); ch.append("%d:%02d %s" % (s // 60, s % 60, sc["ch"]))
if ch and not ch[0].startswith("0:00"): ch[0] = "0:00" + ch[0][ch[0].index(" "):]
open(os.path.join(OUT, key + "_chuong.txt"), "w", encoding="utf-8").write("\n".join(ch) + "\n")
print(key, "xong %.0fs, dai %.0fs" % (time.time() - t0, b[-1]), flush=True)
