# Doc kich ban bang giong chot Huy70_HaiDang30, tung cau; ra voice.wav + timing.json (moc tung cau de lam phu de + dung canh).
import json, os, re, sys, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
kb = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
from vieneu import Vieneu
vj = os.environ.get("HN_VOICE_JSON")
if vj: v = json.loads(vj)
else:
    sys.path.insert(0, ROOT); import hncodec; v = hncodec.load(os.path.join(ROOT, "_video", "engine", "giong.bin"))
VOICE = {"speaker_emb": np.asarray(v["speaker_emb"], dtype=np.float32), "codes": np.asarray(v["codes"], dtype=v.get("codes_dtype", "int64"))}
tts = Vieneu(); SR = tts.sample_rate
def cau(t):
    t = re.sub(r"\s+", " ", t.strip()); return [x.strip() for x in re.findall(r"[^.!?…]+[.!?…]*", t) if x.strip()]
def nghi(c):
    n = len(c.split())
    if c.endswith("…"): return 0.7
    if c.endswith("?"): return 0.65
    if n <= 6: return 0.72
    return 0.42
HOLD = {"S01": 1.4, "S02": 2.0, "S04": 0.8, "S06": 1.2, "S08": 1.0, "S11": 1.0, "S12": 0.8, "S14": 1.0, "S16": 1.4, "S17": 1.4, "S18": 0.8, "S19": 2.2, "S20": 1.0, "S21": 2.4, "S22": 3.5}
LEAD = {"S01": 1.2, "S02": 0.6, "S08": 1.6, "S19": 0.6, "S21": 1.2}
TEMPO = 0.95  # đọc chậm lại 5% cho giọng kể chuyện (giữ cao độ)
parts = []; t = 0.0; tim = []; t0 = time.time()
for sc in kb["scenes"]:
    lead = LEAD.get(sc["id"], 0.0); parts.append(np.zeros(int(SR * lead), np.float32)); t += lead
    s0 = t; sens = []
    xs = cau(sc["say"])
    for j, c in enumerate(xs):
        n = len(c.split()); temp = 0.78 if (n <= 8 or c.endswith("?")) else 0.7
        a = np.asarray(tts.infer(c, voice=VOICE, temperature=temp), dtype=np.float32).reshape(-1)
        # cat khoang lang dau/cuoi cho moc phu de chinh xac
        nz = np.where(np.abs(a) > 0.012)[0]
        if len(nz): a = a[max(0, nz[0] - int(SR * 0.04)): nz[-1] + int(SR * 0.08)]
        if n <= 6 or c.endswith("?"): a = a * 1.1
        sens.append({"text": c, "a": round(t, 3), "b": round(t + len(a) / SR, 3)})
        parts.append(a); t += len(a) / SR
        p = nghi(c) if j < len(xs) - 1 else 0.0
        parts.append(np.zeros(int(SR * p), np.float32)); t += p
    hold = 0.75 + HOLD.get(sc["id"], 0.0)
    parts.append(np.zeros(int(SR * hold), np.float32)); t += hold
    tim.append({"id": sc["id"], "a": round(s0 - lead, 3), "b": round(t, 3), "sens": sens})
    print(sc["id"], "%.1fs" % (t - s0), "tong %.0fs" % t, "may %.0fs" % (time.time() - t0), flush=True)
tts.save(np.clip(np.concatenate(parts), -1, 1), os.path.join(out, "raw.wav"))
import subprocess
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", os.path.join(out, "raw.wav"), "-af", "atempo=%.3f" % TEMPO, os.path.join(out, "voice.wav")], check=True)
k = 1 / TEMPO; t *= k
for sc in tim:
    sc["a"] = round(sc["a"] * k, 3); sc["b"] = round(sc["b"] * k, 3)
    for z in sc["sens"]: z["a"] = round(z["a"] * k, 3); z["b"] = round(z["b"] * k, 3)
json.dump({"total": round(t, 3), "scenes": tim}, open(os.path.join(out, "timing.json"), "w"), ensure_ascii=False, indent=1)
print("XONG", round(t, 1))
