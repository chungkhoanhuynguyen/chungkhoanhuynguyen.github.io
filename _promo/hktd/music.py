import numpy as np, wave
SR = 44100
SHIFT = 0.0
BND = [0, 4, 8, 13, 21, 26, 34, 40, 50, 54]
DUR = BND[-1] + .5
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
BPM = 120; B = 60 / BPM  # 0.5 s per beat
def t_(d): return np.arange(int(SR * d)) / SR
def add(sig, at, pan=0.0, g=1.0):
    _add(sig, at + SHIFT, pan, g)
def _add(sig, at, pan=0.0, g=1.0):
    i = int(at * SR); j = min(N, i + len(sig))
    if i >= N: return
    s = sig[:j - i] * g
    L[i:j] += s * (1 - max(0, pan)); R[i:j] += s * (1 + min(0, pan))
def env(d, a=0.005, r=None):
    t = t_(d); e = np.minimum(1, t / a)
    if r: e *= np.exp(-t / r)
    return e
def lp(x, k):  # one-pole lowpass
    y = np.empty_like(x); acc = 0.0
    for i in range(len(x)):
        acc += k * (x[i] - acc); y[i] = acc
    return y
def hz(n): return 440 * 2 ** ((n - 69) / 12)

# --- instruments ---
def taiko(g=1.0, big=False):
    d = 1.6 if big else 0.7; t = t_(d)
    f = (48 if big else 62) * (1 + 1.4 * np.exp(-t * 18))
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / (0.5 if big else 0.22))
    sk = rng.standard_normal(len(t)) * np.exp(-t / 0.02) * 0.5
    return np.tanh((body + sk) * (2.4 if big else 1.8)) * g
def snare(g=.5):
    t = t_(.3); n = rng.standard_normal(len(t)) * np.exp(-t / .07)
    return (n * .7 + np.sin(2 * np.pi * 190 * t) * np.exp(-t / .05)) * g
def hat(g=.12):
    t = t_(.06); n = rng.standard_normal(len(t)); n = n - lp(n, .3)
    return n * np.exp(-t / .015) * g
def pluck(n, d=.9, g=.35):  # guzheng-ish karplus strong
    f = hz(n); p = int(SR / f); buf = rng.uniform(-1, 1, p); out = np.zeros(int(SR * d))
    for i in range(len(out)):
        out[i] = buf[i % p]; buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .996
    return out * g * env(d, .002)
def erhu(n, d, g=.22, bend=0):
    t = t_(d); f = hz(n) * (1 + .012 * np.sin(2 * np.pi * 5.5 * t) * np.minimum(1, t / .25)) * (1 + bend * np.exp(-t * 12))
    ph = np.cumsum(f) / SR; s = 2 * (ph % 1) - 1
    s = lp(s, .12) + .3 * np.sin(2 * np.pi * ph * 2)
    e = np.minimum(1, t / .06) * np.minimum(1, (d - t) / .08)
    return s * e * g
def bass(n, d, g=.4, dist=1.0):
    t = t_(d); f = hz(n); s = np.sin(2 * np.pi * f * t) + .5 * np.sin(4 * np.pi * f * t)
    return np.tanh(s * dist) * env(d, .004, d * .7) * g
def pad(notes, d, g=.1):
    t = t_(d); s = np.zeros(len(t))
    for n in notes:
        for dt in (-.08, 0, .08):
            ph = np.cumsum(np.full(len(t), hz(n) * (1 + dt / 100))) / SR; s += 2 * (ph % 1) - 1
    s = lp(s, .05)
    e = np.minimum(1, t / .8) * np.minimum(1, (d - t) / .8)
    return s * e * g / len(notes)
def boom(g=1.0):
    t = t_(3.0); f = 36 * (1 + 2 * np.exp(-t * 6))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / .9)
    n = lp(rng.standard_normal(len(t)), .05) * np.exp(-t / .6) * 2
    return np.tanh((s + n) * 2) * g
def riser(d, g=.25):
    t = t_(d); n = rng.standard_normal(len(t))
    out = np.zeros(len(t)); acc = 0.0
    for i in range(len(t)):
        k = .01 + .4 * (t[i] / d) ** 2; acc += k * (n[i] - acc); out[i] = acc
    return out * (t / d) ** 2 * g
def thunder(g=.6):
    t = t_(2.5); n = lp(rng.standard_normal(len(t)), .08)
    return n * np.exp(-t / .7) * np.minimum(1, t / .01) * g * 3

# scale: D minor pentatonic-ish (D F G A C)
D3 = 50
SC = [0, 3, 5, 7, 10, 12, 15, 17, 19, 22, 24]
def sc(i, base=62): return base + SC[i % len(SC)] + 12 * (i // len(SC))

# --- arrangement ---
# 0-4 tối: drone + tim đập + riser; 4-8 tên game: plucks + boom
_add(pad([26, 33, 38], 4.4, .3), 0)
for k, at in enumerate([0.3, 0.7, 1.5, 1.9, 2.7, 3.1]): _add(taiko(.7 if k % 2 == 0 else .45), at)
_add(riser(1.6, .4), 2.4)
_add(boom(1.2), 4.0); _add(taiko(1, True), 4.0)
add(pad([38, 45, 50], 4.2, .2), 4.0)
for k, n in enumerate([0, 2, 3, 4, 3, 5, 4, 6]): add(pluck(sc(n), 1.2), 4.1 + k * .48, pan=(-.4 if k % 2 else .4))
add(riser(1.4, .3), 6.6)
melody = [(0, 1), (2, .5), (3, .5), (4, 1), (3, .5), (2, .5), (3, 2), (5, 1), (4, .5), (3, .5), (2, 1), (0, 1), (1, 2),
          (4, 1), (5, .5), (6, .5), (7, 1.5), (6, .5), (5, 1), (4, 1), (3, 2), (2, .5), (3, .5), (4, 1), (2, 1), (0, 2)]
bassline = [D3 - 12, D3 - 12, D3 - 14, D3 - 9, D3 - 12, D3 - 12, D3 - 7, D3 - 9]
END = BND[-2]
t = 8.0; bar = 0
while t < END - .05:
    heavy = BND[6] <= t < BND[8]
    for b in range(4):
        tb = t + b * B
        if tb >= END - .05: break
        add(taiko(.9), tb, g=1.0 if b in (0, 2) else .55)
        if b in (1, 3): add(snare(.45 if heavy else .3), tb)
        if heavy: add(taiko(.5), tb + B / 2, g=.5)
        for h in range(2): add(hat(.1), tb + h * B / 2, pan=.3)
        bn = bassline[bar % len(bassline)]
        for s16 in range(4):
            add(bass(bn + (12 if s16 == 2 else 0), B / 4 * .9, .32, 3.0 if heavy else 1.4), tb + s16 * B / 4)
    ch = [[50, 57, 62], [48, 55, 60], [46, 53, 58], [45, 52, 57]][bar % 4]
    add(pad(ch, 2.05, .13), t)
    bar += 1; t += 4 * B
tm = 9.0; mi = 0
while tm < END - .3:
    n, d = melody[mi % len(melody)]; d *= B * 2
    add(erhu(sc(n, 74), min(d, END - tm), .2, bend=-.03), tm, pan=-.15)
    tm += d; mi += 1
for at in BND[2:-1]: add(boom(.9), at); add(taiko(1, True), at, g=.9)
for at in [BND[3] + 2, BND[3] + 4, BND[3] + 6]: add(taiko(1, True), at, g=.8)
for k in range(6): add(thunder(.5), BND[5] + 2 + k * 1.05, pan=rng.uniform(-.5, .5))
add(boom(1.3), BND[6] + 50 / 30)
add(riser(2.0, .35), END - 2)
add(boom(1.4), END); add(taiko(1, True), END)
add(pad([38, 45, 50, 57, 62], 4.5, .25), END)
for k, n in enumerate([4, 5, 6, 8]): add(pluck(sc(n), 2.0, .3), END + .1 + k * .3, pan=(k - 1.5) / 3)

# --- reverb (simple stereo convolution) ---
def rev(x, seed):
    r = np.random.default_rng(seed); d = int(SR * 1.8)
    ir = r.standard_normal(d) * np.exp(-np.arange(d) / SR / .45); ir[0] = 0
    ir = ir / np.sqrt((ir ** 2).sum())
    n = len(x) + d; F = 1 << (n - 1).bit_length()
    return np.fft.irfft(np.fft.rfft(x, F) * np.fft.rfft(ir, F), F)[:len(x)]
L2 = L + .28 * rev(L, 1); R2 = R + .28 * rev(R, 2)
m = np.stack([L2, R2], 1)
m = np.tanh(m / np.abs(m).max() * 1.6) * .89
fo = int(SR * 1.2); m[-fo:] *= np.linspace(1, 0, fo)[:, None]
pcm = (m * 32767).astype(np.int16)
with wave.open('music.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print('ok', DUR)
