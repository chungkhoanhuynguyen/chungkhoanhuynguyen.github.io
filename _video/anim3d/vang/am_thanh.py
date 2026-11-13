# Âm thanh video "Vàng đỉnh": tự tổng hợp (không bản quyền) tiếng môi trường + hiệu ứng khớp cảnh + nhạc nền theo cảm xúc,
# trộn với giọng đọc (nhạc tự hạ khi có lời). Dùng: python am_thanh.py timing.json voice.wav cuts.json out.wav
import json, sys, os, wave, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "engine"))
import nhac20 as N
SR = 44100; R = np.random.default_rng(5)
tim = json.load(open(sys.argv[1])); cuts = json.load(open(sys.argv[3])); OUT = sys.argv[4]
S = {s["id"]: s for s in tim["scenes"]}
TOTAL = tim["total"] + 4.0; NT = int(TOTAL * SR) + SR
def at(sid, j=None, off=0.0):
    s = S[sid]; return (s["a"] if j is None else s["sens"][min(j, len(s["sens"]) - 1)]["a"]) + off
def end(sid): return S[sid]["b"]
def db(x): return 10 ** (x / 20)
def lp(x, k): return N.lp(x, k)
def noise(n): return R.standard_normal(n)
def bp(x, k1, k2): return lp(x, k1) - lp(x, k2)
L = np.zeros(NT); Rr = np.zeros(NT)
def put(x, t0, g=0.0, pan=0.0):
    i = int(t0 * SR); x = x * db(g)
    if i >= NT or i + len(x) <= 0: return
    if i < 0: x = x[-i:]; i = 0
    x = x[: NT - i]; L[i:i + len(x)] += x * (1 - max(0, pan)); Rr[i:i + len(x)] += x * (1 + min(0, pan))
def fade(n, a=0.8, r=0.8):
    e = np.ones(n); na, nr = min(n, int(a * SR)), min(n, int(r * SR))
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e
def bed(t0, t1, gen, g, st=True):
    n = int((t1 - t0) * SR)
    if n <= 0: return
    a = gen(n) * fade(n); put(a, t0, g, 0)

# ---------- ambiences ----------
def rain(n): x = bp(noise(n), 2, 14) * 0.5; drops = np.zeros(n); idx = R.integers(0, n, n // 900); drops[idx] = R.uniform(0.3, 1, len(idx)); return x + lp(drops, 3) * 0.8
def room(n): t = np.arange(n) / SR; return lp(noise(n), 60) * 0.6 + 0.08 * np.sin(2 * np.pi * 60 * t)
def crowd(n):
    x = np.zeros(n); t = np.arange(n) / SR
    for k in range(6): f = R.uniform(2.5, 6); x += bp(noise(n), 6, 30) * (0.5 + 0.5 * np.sin(2 * np.pi * f * t + R.uniform(0, 6))) ** 2
    return x * 0.35
def street_day(n): return lp(noise(n), 25) * 0.5 + crowd(n) * 0.4
def crickets(n):
    t = np.arange(n) / SR; x = np.zeros(n)
    for k in range(4): f = R.uniform(4200, 5200); x += np.sin(2 * np.pi * f * t) * (np.sin(2 * np.pi * R.uniform(18, 26) * t) > 0.6) * (np.sin(2 * np.pi * R.uniform(0.3, 0.7) * t + k) > 0) * 0.06
    return x + lp(noise(n), 80) * 0.25
def water(n): t = np.arange(n) / SR; return bp(noise(n), 30, 200) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.25 * t))
def birds(n):
    x = np.zeros(n)
    for _ in range(int(n / SR * 1.2)):
        i = int(R.integers(0, max(1, n - SR))); d = int(SR * R.uniform(0.08, 0.2)); t = np.arange(d) / SR; f0 = R.uniform(2500, 4200)
        x[i:i + d] += np.sin(2 * np.pi * np.cumsum(f0 + 900 * np.sin(2 * np.pi * 14 * t)) / SR) * np.hanning(d) * 0.12
    return x + lp(noise(n), 40) * 0.2

# ---------- one-shots ----------
def mixs(*xs):
    n = max(len(x) for x in xs); o = np.zeros(n)
    for x in xs: o[:len(x)] += x
    return o
def ting(): return mixs(N.bell(1568, 1.2) * 0.5, N.bell(2093, 1.0) * 0.35) * 0.7
def buzz():
    n = int(SR * 1.1); t = np.arange(n) / SR; return np.sin(2 * np.pi * 160 * t) * ((t % 0.5) < 0.32) * 0.35 * lp(noise(n) * 0 + 1, 1)
def pop(): n = int(SR * 0.06); t = np.arange(n) / SR; return np.sin(2 * np.pi * (900 + 600 * np.exp(-t * 60)) * t) * np.exp(-t * 60) * 0.5
def whoosh(d=0.5):
    n = int(SR * d); t = np.arange(n) / SR; x = noise(n); y = np.zeros(n); k = 2
    for i in range(0, n, 512): k = int(2 + 40 * (1 - np.sin(np.pi * i / n))); y[i:i + 512] = lp(x, k)[i:i + 512]
    return y * np.sin(np.pi * t / d) ** 2 * 0.6
def boom(d=2.4): n = int(SR * d); t = np.arange(n) / SR; f = 34 + 60 * np.exp(-t * 5); return (np.tanh(2.2 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.exp(-t * 1.6) + lp(noise(n), 20) * np.exp(-t * 6) * 0.5) * 0.9
def stamp(): n = int(SR * 0.4); t = np.arange(n) / SR; return (np.sin(2 * np.pi * (90 + 80 * np.exp(-t * 40)) * t) * np.exp(-t * 18) + lp(noise(n), 4) * np.exp(-t * 40) * 0.7) * 0.9
def kaching(): return np.concatenate([N.bell(2637, 0.15) * 0.4, N.bell(3136, 1.0) * 0.5])
def coin(): return N.bell(2400, 0.6) * 0.35
def heart(n_beats=6, bpm=70):
    one = lambda: (lambda n: np.sin(2 * np.pi * 48 * np.arange(n) / SR) * np.exp(-np.arange(n) / SR * 16))(int(SR * 0.3))
    x = np.zeros(int(SR * 60 / bpm * n_beats) + SR); step = int(SR * 60 / bpm)
    for k in range(n_beats): x[k * step:k * step + int(SR * 0.3)] += one(); j = k * step + int(SR * 0.22); x[j:j + int(SR * 0.3)] += one() * 0.7
    return x * 0.9
def ringtone():
    x = np.zeros(int(SR * 3.4)); notes = [76, 79, 84, 79, 76, 79, 84, 88]
    for k, m in enumerate(notes): s = N.marimba(N.mtof(m), 0.4) * 0.5; i = int(k * 0.2 * SR); x[i:i + len(s)] += s; x[int(1.8 * SR) + i:int(1.8 * SR) + i + len(s)] += s if int(1.8 * SR) + i + len(s) <= len(x) else 0
    return x
def keys(d=2.0):
    x = np.zeros(int(SR * d))
    for _ in range(int(d * 9)): i = int(R.integers(0, len(x) - 2000)); c = lp(noise(600), 2) * np.exp(-np.arange(600) / SR * 300) * 0.4; x[i:i + 600] += c
    return x
def steps(d, rate=1.9, soft=1.0):
    x = np.zeros(int(SR * d)); k = 0.0
    while k < d - 0.2: i = int(k * SR); s = lp(noise(2200), 8) * np.exp(-np.arange(2200) / SR * 60) * 0.5 * soft; x[i:i + 2200] += s; k += 1 / rate
    return x
def wheel_tick(d):
    x = np.zeros(int(SR * d)); k = 0.0
    while k < d - 0.05: i = int(k * SR); x[i:i + 300] += lp(noise(300), 2) * np.exp(-np.arange(300) / SR * 500) * 0.25; k += 0.07
    return x
def moto(d=3.0, f0=38):
    n = int(SR * d); t = np.arange(n) / SR; dop = 1 + 0.06 * np.tanh((t - d / 2) * 2.5) * -1; f = f0 * dop * (1 + 0.04 * np.sin(2 * np.pi * 7 * t))
    ph = 2 * np.pi * np.cumsum(f) / SR; x = sum(np.sin(ph * k) / k for k in range(1, 9)) + lp(noise(n), 6) * 0.3
    return lp(x, 3) * np.exp(-((t - d / 2) / (d / 3.2)) ** 2) * 0.45
def clock(d):
    x = np.zeros(int(SR * d)); k = 0.0
    while k < d - 0.05: i = int(k * SR); x[i:i + 400] += np.sin(2 * np.pi * 3200 * np.arange(400) / SR) * np.exp(-np.arange(400) / SR * 200) * 0.25; k += 1.0
    return x
def tvhiss(n): return bp(noise(n), 1, 4) * 0.12
def bike_bell(): return mixs(N.bell(3520, 0.5) * 0.3, N.bell(4186, 0.4) * 0.2)
def horn(d=0.6, f=420):
    n = int(SR * d); t = np.arange(n) / SR; x = (np.sign(np.sin(2 * np.pi * f * t)) * 0.5 + np.sign(np.sin(2 * np.pi * f * 1.26 * t)) * 0.4)
    return lp(x, 4) * fade(n, 0.01, 0.06) * 0.35
def argue(d=4.0):
    # tiếng cãi nhau um xùm: hai "giọng" formant giật cục, to nhỏ thất thường (không có lời thật)
    n = int(SR * d); t = np.arange(n) / SR; x = np.zeros(n)
    for f0, f1, rate, ph in ((140, 900, 5.5, 0), (210, 1300, 6.5, 1.7)):
        pitch = f0 * (1 + 0.25 * np.sin(2 * np.pi * 1.3 * t + ph) + 0.15 * np.sin(2 * np.pi * 3.1 * t))
        src = np.sign(np.sin(2 * np.pi * np.cumsum(pitch) / SR)) * 0.5 + bp(noise(n), 2, 8) * 0.3
        syl = (0.5 + 0.5 * np.sin(2 * np.pi * rate * t + ph)) ** 3 * (np.sin(2 * np.pi * 0.45 * t + ph) > -0.4)
        x += bp(src, 3, 40) * syl
    return x * 0.6
def splash(d=1.0): n = int(SR * d); return bp(noise(n), 2, 12) * np.exp(-np.arange(n) / SR * 4) * 0.5
def temple(): return mixs(N.bell(196, 5.0) * 0.5, N.bell(392, 3.0) * 0.2)

# ---------- ambience map ----------
def amb(a, b, gen, g): bed(a, b, gen, g)
amb(at("S01"), end("S01"), room, -27)
amb(at("S03", 2), at("S03", 4), room, -28); amb(at("S03", 0), at("S03", 2), street_day, -27); amb(at("S03", 4), at("S03", 6), street_day, -28)
amb(at("S04"), end("S04"), birds, -26); amb(at("S05"), end("S05"), street_day, -25)
amb(at("S06"), at("S06", 2), room, -28); amb(at("S06", 2), at("S06", 3), birds, -27)
amb(at("S07"), at("S07", 2), room, -27); amb(at("S07", 2), end("S07"), lambda n: lp(noise(n), 50) * 0.3, -26)
amb(at("S08"), end("S11"), rain, -20); amb(at("S08", 2), end("S11"), crowd, -27)
amb(at("S08", 8), at("S08", 9), lambda n: bp(noise(n), 1, 3) * 0.9, -22)  # mưa lộp độp mái hiên
amb(at("S08", 6), at("S08", 8), water, -18)
amb(at("S09", 1), at("S09", 2), birds, -24); amb(at("S09", 2), at("S09", 3), street_day, -22)
amb(at("S11", 0), at("S11", 2), tvhiss, -20)
amb(at("S12"), at("S12", 2), crowd, -30); amb(at("S13", 2), end("S13"), room, -28)
amb(at("S15", 3), end("S15"), room, -30); amb(at("S16"), end("S16"), rain, -27)
amb(at("S17", 6), at("S17", 9), street_day, -26); amb(at("S18", 2), at("S18", 3), street_day, -24); amb(at("S19", 1), at("S19", 4), lambda n: lp(noise(n), 50) * 0.3, -25)
amb(at("S21"), end("S21"), crickets, -23); amb(at("S21"), end("S21"), water, -27)

# ---------- one-shot cues ----------
C = [
    (at("S01", 2), buzz(), -14), (at("S01", 3, 0.5), ting(), -12), (at("S01", 5), np.concatenate([pop() if k % 2 == 0 else np.zeros(int(SR * 0.12)) for k in range(40)]), -18),
    (at("S01", 7, 1.3), boom(), -10), (at("S01", 8, 2.5), stamp(), -8), (at("S02"), boom(3.0), -8),
    (at("S03", 1, 0.8), coin(), -16), (at("S06", 3, 0.5), ting(), -13), (at("S06", 3, 2.6), ting(), -13),
    (at("S07", 0), keys(3.0), -20), (at("S07", 2), steps(end("S07") - at("S07", 2), 1.6, 0.6), -20), (at("S07", 2), wheel_tick(end("S07") - at("S07", 2) - 0.5), -22),
    (at("S08", 8, 0.9), pop(), -30), (at("S08", 4, 0.2), horn(0.7, 420), -13), (at("S08", 4, 0.9), horn(0.4, 520), -15), (at("S08", 4, 1.6), horn(1.0, 380), -13),
    (at("S08", 5, 0.0), argue(at("S08", 6) - at("S08", 5) + 0.3), -11), (at("S08", 5, 0.6), horn(0.5, 470), -16),
    (at("S08", 6, 0.8), splash(), -18), (at("S08", 7, 0.3), splash(), -16), (at("S08", 7, 1.5), splash(), -17), (at("S09", 1, 0.6), bike_bell(), -16), (at("S09", 2, 0.3), moto(3.2, 42), -14), (at("S09", 2, 1.8), moto(3.0, 36), -16),
    (at("S09", 0, 0.1), whoosh(0.9), -14), (at("S09", 3, 0.5), boom(1.8), -14),
    (at("S10", 1, 0.3), N.bell(3800, 1.6) * 0.3, -18), (at("S11", 3), whoosh(1.4), -16), (at("S11", 4, 0.0), boom(), -9),
    (at("S12", 3, 0.0), kaching(), -12), (at("S12", 3, 1.0), stamp(), -9), (at("S12", 7, 0.3), coin(), -14), (at("S12", 7, 0.6), coin(), -15),
    (at("S13", 0, 1.2), N.bell(1760, 1.5) * 0.4, -16), (at("S13", 4), np.concatenate([pop() if k % 2 == 0 else np.zeros(int(SR * 0.08)) for k in range(60)]), -18),
    (at("S14", 1, 0.3), whoosh(0.8), -16), (at("S15", 1, 1.0), boom(1.6), -12), (at("S15", 4, 0.3), pop(), -16), (at("S15", 4, 1.3), pop(), -16), (at("S15", 3, 2.0), boom(1.4), -13),
    (at("S15", 5), clock(end("S15") - at("S15", 5)), -20), (at("S16", 1, 1.0), stamp(), -8), (at("S16", 2), heart(8, 64), -14),
    (at("S17", 2, 0.2), ringtone(), -14), (at("S17", 4), heart(4, 72), -14), (at("S17", 8), steps(at("S17", 9) - at("S17", 8), 1.4, 0.7), -20), (at("S17", 8), wheel_tick(at("S17", 9) - at("S17", 8) - 0.6), -22),
    (at("S17", 9, 0.5), ting(), -14), (at("S17", 11), boom(2.0), -12),
    (at("S18"), boom(1.6), -14), (at("S18", 0, 2.4), whoosh(0.6), -16), (at("S18", 1, 0.4), ting(), -13), (at("S18", 3), boom(1.4), -14), (at("S18", 4), whoosh(0.6), -16), (at("S18", 5), whoosh(0.6), -16), (at("S19", 0, 0.4), ting(), -13),
    (at("S19", 1), steps(at("S19", 2) - at("S19", 1), 1.5, 0.8), -18), (at("S19", 6, 0.9), stamp(), -6), (at("S19", 6, 0.9), boom(2.6), -12), (at("S19", 5), heart(6, 76), -16),
    (at("S21", 3), heart(4, 60), -20), (at("S21", 17, 0.4), temple(), -14), (at("S21", 10, 0.6), coin(), -16), (at("S21", 12, 0.3), coin(), -15), (at("S22", 3, 1.4), pop(), -12),
]
for t0, x, g in C: put(x, t0, g, float(R.uniform(-0.15, 0.15)))
for t0 in cuts: put(whoosh(0.38), t0 - 0.19, -27, float(R.uniform(-0.3, 0.3)))

# ---------- music beds by mood ----------
def chords_bed(n, prog, inst, bpm, arp=True, padg=0.25, ig=0.35, oct=0):
    x = np.zeros(n); beat = 60 / bpm; bar = beat * 4; t = 0.0; k = 0
    while t < n / SR:
        ch = prog[k % len(prog)]; i = int(t * SR); d = int(bar * SR) + int(SR * 1.2)
        p = N.pad([N.mtof(m + oct) for m in ch], bar + 1.2, a=0.6, rel=1.0, br=14) * padg; x[i:i + len(p)] += p[: max(0, n - i)]
        if inst is not None:
            pat = ch + [ch[1] + 12] if arp else ch
            for b in range(8 if arp else 4):
                m = pat[b % len(pat)] + 12 + oct; s = inst(N.mtof(m), beat * (0.5 if arp else 1) + 0.8) * ig; j = i + int(b * beat * (0.5 if arp else 1) * SR)
                if j < n: x[j:j + len(s)] += s[: n - j]
        t += bar; k += 1
    return x
Am = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]; F = [[53, 57, 60], [48, 52, 55], [50, 53, 57], [46, 50, 53]]
C_ = [[48, 52, 55], [55, 59, 62], [57, 60, 64], [53, 57, 60]]; Dm = [[50, 53, 57], [46, 50, 53], [53, 57, 60], [52, 55, 59]]
MOOD = [
    ("S01", "S02", lambda n: chords_bed(n, Am, None, 60, padg=0.32), -22),
    ("S03", "S03", lambda n: chords_bed(n, C_, N.marimba, 100, ig=0.3), -24),
    ("S04", "S04", lambda n: chords_bed(n, F, N.piano, 70, ig=0.4), -21),
    ("S05", "S05", lambda n: chords_bed(n, C_, N.marimba, 104, ig=0.3), -24),
    ("S06", "S06", lambda n: chords_bed(n, F, N.piano, 66, ig=0.4), -21),
    ("S07", "S11", lambda n: chords_bed(n, Am, N.pluck, 84, ig=0.22, padg=0.2), -24),
    ("S12", "S13", lambda n: chords_bed(n, C_, N.rhodes, 96, ig=0.3), -23),
    ("S14", "S15", lambda n: chords_bed(n, Am, N.piano, 58, arp=False, ig=0.3), -23),
    ("S16", "S17", lambda n: chords_bed(n, Dm, N.piano, 60, ig=0.38, padg=0.3), -20),
    ("S18", "S18", lambda n: chords_bed(n, Am, N.synth, 92, ig=0.18, padg=0.25, oct=-12), -24),
    ("S19", "S19", lambda n: chords_bed(n, Dm, N.piano, 56, arp=False, ig=0.4, padg=0.32), -20),
    ("S20", "S20", lambda n: chords_bed(n, F, None, 70, padg=0.3), -23),
    ("S21", "S21", lambda n: chords_bed(n, F, N.piano, 62, ig=0.42, padg=0.34), -19),
    ("S22", None, lambda n: chords_bed(n, C_, N.piano, 80, ig=0.35, padg=0.3), -22),
]
mus = np.zeros(NT)
for a, b, gen, g in MOOD:
    t0 = at(a) - 0.8; t1 = (end(b) if b else TOTAL) + 0.8; n = int((t1 - t0) * SR); x = gen(n) * fade(n, 1.2, 1.4) * db(g); i = max(0, int(t0 * SR)); mus[i:i + n] += x[: NT - i]
# voice + ducking
def readwav(p):
    with wave.open(p) as w: sr = w.getframerate(); ch = w.getnchannels(); x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    if ch == 2: x = x.reshape(-1, 2).mean(1)
    if sr != SR: idx = np.arange(0, len(x), sr / SR); x = np.interp(idx, np.arange(len(x)), x)
    return x
v = readwav(sys.argv[2]); vv = np.zeros(NT); vv[: min(NT, len(v))] = v[: NT]
envv = lp(np.abs(vv), 2205); envv = envv / (envv.max() + 1e-9); duck = 1 - 0.55 * np.clip(envv * 6, 0, 1)
mus *= lp(duck, 4410)
Lf = vv * 1.0 + L + mus; Rf = vv * 1.0 + Rr + mus
pk = max(np.abs(Lf).max(), np.abs(Rf).max()); g = 0.95 / pk if pk > 0.95 else 1.0
st = np.stack([np.tanh(Lf * g * 1.05), np.tanh(Rf * g * 1.05)], 1)
with wave.open(OUT, "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(st, -1, 1) * 32767).astype(np.int16).tobytes())
print("xong am thanh", round(TOTAL, 1), "s")
