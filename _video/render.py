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
                     circles=ch.get("circles", []), tag=(s["label"] or ch["sym"]).upper()[:40] + " · NẾN TUẦN", reveal=1.6)
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

# 4) dựng + nhạc nền
rawmp4 = WORK + "/raw.mp4"; out = os.path.join(OUT, key + ".mp4")
b = dx2.build_scenes(key, scenes, wd, rawmp4, tempo=1.0)
music.mix(rawmp4, b, out)
# 5) ảnh bìa = khung cảnh mở đầu lúc 3 giây
dx2.draw(scenes[0], 3.0).save(os.path.join(OUT, key + "_bia.png"))
# 6) mốc chương thật theo giọng (cho mô tả YouTube)
ch = []
for i, sc in enumerate(raw):
    if sc.get("ch"):
        s = int(b[i]); ch.append("%d:%02d %s" % (s // 60, s % 60, sc["ch"]))
if ch and not ch[0].startswith("0:00"): ch[0] = "0:00" + ch[0][ch[0].index(" "):]
open(os.path.join(OUT, key + "_chuong.txt"), "w", encoding="utf-8").write("\n".join(ch) + "\n")
print(key, "xong %.0fs, dai %.0fs" % (time.time() - t0, b[-1]), flush=True)
