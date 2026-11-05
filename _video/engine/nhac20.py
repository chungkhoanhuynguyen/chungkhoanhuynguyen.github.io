# 20 kiểu nhạc nền TỰ TỔNG HỢP (không bản quyền) cho video Huy Nguyễn.
# Dùng: import nhac20; x = nhac20.tao(so_kieu, giay)  -> mảng mono 44100Hz [-1..1]
#       python nhac20.py <thư mục>  -> xuất 20 file mẫu 20 giây
import numpy as np, sys, os, wave
SR = 44100
R = np.random.default_rng(11)
KIEU = [
 (1, "Doanh nghiệp tích cực", "piano + pluck, nhịp vừa, sáng sủa – video giáo dục, đọc BCTC"),
 (2, "Tin nóng kịch tính", "dây staccato + trống trận – tin nóng, vĩ mô (đang dùng)"),
 (3, "Lo-fi thư giãn", "trống lo-fi, phím điện ấm, tiếng đĩa than – video dài, tích sản"),
 (4, "Ambient suy ngẫm", "nền pad chậm, không trống – kể chuyện, bài học"),
 (5, "Piano cảm xúc", "rải piano chậm – câu chuyện nhà đầu tư, mất mát, bài học"),
 (6, "Công nghệ tương lai", "arp synth 16 nốt – AI, công nghệ, dữ liệu"),
 (7, "Trap nhẹ", "808 + hi-hat dồn – TikTok trẻ, giật tít"),
 (8, "Phố Wall tự tin", "bass funk + vỗ tay – thị trường tăng, cổ phiếu khỏe"),
 (9, "Hồi hộp", "drone trầm + kim đồng hồ – trước phiên quan trọng, rủi ro"),
 (10, "Điện ảnh hùng tráng", "braam + trống lớn + dây – mở đầu kênh, video lớn"),
 (11, "Synthwave thập niên 80", "pad gated + arp retro – lịch sử thị trường"),
 (12, "Deep house", "kick đều 4 phách, hi-hat lệch – reel nhịp nhanh"),
 (13, "Acoustic tươi sáng", "gảy kiểu guitar, giọng trưởng – mẹo đầu tư, tích sản"),
 (14, "Marimba vui", "marimba giai điệu nhẹ – mẹo nhanh, kiến thức cơ bản"),
 (15, "Thời sự", "bass xung + tick – bản tin sáng, điểm tin"),
 (16, "Nhiệt đới thư thái", "pluck + marimba, nhịp lắc – nội dung nhẹ cuối tuần"),
 (17, "Tối giản đồng hồ", "tick + sub bass – số liệu, so sánh, bảng"),
 (18, "Căng thẳng u tối", "hợp âm thứ đi xuống – thị trường giảm, cảnh báo bẫy"),
 (19, "Truyền cảm hứng", "piano + pad dâng + trống vào dần – kết video, kêu gọi"),
 (20, "Á Đông ngũ cung", "chuông ngũ cung + trống nhẹ – tích sản dài hạn, triết lý"),
]

def mtof(m): return 440.0 * 2 ** ((m - 69) / 12)
def env(n, a=0.005, r=0.3, s=None):
    t = np.arange(n) / SR; e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / r)
    return e
def adsr(n, a, rel):
    e = np.ones(n); na = min(n, int(a * SR)); nr = min(n, int(rel * SR))
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e
def lp(x, k): return np.convolve(x, np.ones(k) / k, "same") if k > 1 else x
def hp(x, k=8): return x - lp(x, k)
def saw(f, n, h=8):
    t = np.arange(n) / SR; return sum(((-1) ** (k + 1)) * np.sin(2 * np.pi * f * k * t) / k for k in range(1, h + 1))
def sq(f, n, h=7):
    t = np.arange(n) / SR; return sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, h + 1, 2))
def sine(f, n, ph=0): return np.sin(2 * np.pi * f * np.arange(n) / SR + ph)

# ---- nhạc cụ ----
def piano(f, d=1.2):
    n = int(SR * d); t = np.arange(n) / SR
    x = sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (2.2 + k * 1.3)) for k, a in ((1, 1), (2, .45), (3, .22), (4, .12), (5, .06)))
    return x * np.minimum(1, t / .004)
def rhodes(f, d=1.4):
    n = int(SR * d); t = np.arange(n) / SR
    m = np.sin(2 * np.pi * f * t) * 1.2 * np.exp(-t * 3)
    return np.sin(2 * np.pi * f * t + m) * np.exp(-t * 1.6) * np.minimum(1, t / .006) * (1 + .15 * np.sin(2 * np.pi * 4.5 * t))
def pluck(f, d=.6):
    n = int(SR * d); p = max(2, int(SR / f)); buf = R.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = .5 * (buf[i % p] + buf[(i + 1) % p]) * .996
    return out
def marimba(f, d=.5):
    n = int(SR * d); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) * np.exp(-t * 9) + .35 * np.sin(2 * np.pi * f * 3.93 * t) * np.exp(-t * 30)) * np.minimum(1, t / .002)
def bell(f, d=2.0):
    n = int(SR * d); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * f * t) * np.exp(-t * 1.5) + .5 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 3) + .25 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 6))
def pad(fs, d, a=.8, rel=1.0, br=10):
    n = int(SR * d); x = np.zeros(n)
    for f in fs:
        for dt in (-.08, .0, .08): x += saw(f * 2 ** (dt / 12), n, 6)
    return lp(x / (len(fs) * 3), br) * adsr(n, a, rel)
def strings(f, d): n = int(SR * d); return lp(saw(f, n, 7), 4) * env(n, .004, d * .45)
def synth(f, d, br=3): n = int(SR * d); return lp(sq(f, n) * .6 + saw(f * 1.005, n, 6) * .4, br) * env(n, .003, d * .5)
def bass(f, d): n = int(SR * d); return (sine(f, n) + .25 * lp(saw(f, n, 4), 6)) * adsr(n, .005, .05) * env(n, .001, d * 1.2)
def b808(f, d=.8):
    n = int(SR * d); t = np.arange(n) / SR; ff = f * (1 + 1.5 * np.exp(-t * 30))
    return np.tanh(1.6 * np.sin(2 * np.pi * np.cumsum(ff) / SR)) * np.exp(-t * 2.2)
def kick(d=.45, g=1.0):
    n = int(SR * d); t = np.arange(n) / SR; f = 45 + 120 * np.exp(-t * 30)
    return np.tanh(2 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * env(n, .002, .16) * g
def snare(d=.25):
    n = int(SR * d); return hp(R.standard_normal(n), 3) * env(n, .001, .07) * .7 + sine(190, n) * env(n, .001, .05) * .5
def clap(d=.25):
    n = int(SR * d); x = hp(R.standard_normal(n), 4); e = np.zeros(n)
    for o in (0, .011, .022): i = int(o * SR); e[i:] += env(n - i, .001, .03 if o < .02 else .09)
    return x * e * .6
def hat(d=.06, o=False):
    n = int(SR * (.25 if o else d)); return hp(R.standard_normal(n), 2) * env(n, .001, .09 if o else .018) * .35
def tom(f0=100, d=.5):
    n = int(SR * d); t = np.arange(n) / SR; f = f0 * (1 + .6 * np.exp(-t * 18))
    return np.tanh(1.8 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * env(n, .002, .22)
def tick(d=.03): n = int(SR * d); return hp(R.standard_normal(n), 2) * env(n, .0005, .006) * .6 + sine(2400, n) * env(n, .0005, .01) * .3
def braam(d=3.0, root=55.0):
    n = int(SR * d); s = saw(root / 2, n, 12) + saw(root / 2 * 1.498, n, 10) * .7 + saw(root, n, 8) * .5
    return np.tanh(1.5 * lp(s, 10)) * env(n, .04, 1.4) * .6
def boom(d=2.5):
    n = int(SR * d); t = np.arange(n) / SR; f = 30 + 70 * np.exp(-t * 5)
    return np.tanh(2.5 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * env(n, .003, 1.0)
def vinyl(n): x = lp(R.standard_normal(n), 30) * .04; c = (R.random(n) > .9995) * R.uniform(-.6, .6, n); return x + lp(c, 3)

# hợp âm: (gốc midi, thứ/trưởng)
def chord(root, minor=False, seven=False):
    ns = [root, root + (3 if minor else 4), root + 7]
    if seven: ns.append(root + (10 if minor else 11))
    return [mtof(m) for m in ns]

class Mix:
    def __init__(s, sec): s.n = int(SR * (sec + 3)); s.x = np.zeros(s.n); s.sec = sec
    def add(s, sig, at, g=1.0):
        i = int(at * SR)
        if i >= s.n or i < 0: return
        j = min(s.n, i + len(sig)); s.x[i:j] += sig[:j - i] * g
    def done(s, fade=1.5):
        e = int(SR * s.sec); y = s.x[:e].copy(); f = int(SR * fade); y[-f:] *= np.linspace(1, 0, f)
        y[:int(SR * .05)] *= np.linspace(0, 1, int(SR * .05))
        y = np.tanh(y * 1.1); return y / (np.abs(y).max() + 1e-9) * .9

def drums(M, bpm, sec, kind="pop", start=0.0):
    b = 60 / bpm; t = start; bar = 0
    while t < sec:
        if kind == "pop":
            M.add(kick(), t, .9); M.add(kick(), t + 2 * b, .9); M.add(clap(), t + b, .55); M.add(clap(), t + 3 * b, .55)
            for i in range(8): M.add(hat(), t + i * b / 2, .5)
        elif kind == "four":
            for i in range(4): M.add(kick(), t + i * b, 1.0); M.add(hat(o=True), t + i * b + b / 2, .45)
            M.add(clap(), t + b, .5); M.add(clap(), t + 3 * b, .5)
        elif kind == "lofi":
            M.add(kick(g=.8), t, .8); M.add(kick(g=.8), t + 2.5 * b, .7); M.add(lp(snare(), 5), t + b, .5); M.add(lp(snare(), 5), t + 3 * b, .5)
            for i in range(8): M.add(lp(hat(), 2), t + i * b / 2 + (.03 if i % 2 else 0), .4)
        elif kind == "trap":
            M.add(kick(), t, 1.0); M.add(clap(), t + 2 * b, .7)
            for i in range(16 if bar % 2 else 8):
                st = b / 4 if bar % 2 else b / 2; M.add(hat(), t + i * st, .45)
        elif kind == "epic":
            M.add(tom(110), t, .7); M.add(tom(95), t + b, .6); M.add(tom(110), t + 2 * b, .7); M.add(tom(80), t + 3 * b, .6); M.add(tom(70), t + 3.5 * b, .6)
            M.add(kick(), t, .8)
        elif kind == "soft":
            M.add(kick(g=.7), t, .7); M.add(lp(snare(), 3), t + 2 * b, .35)
            for i in range(4): M.add(hat(), t + i * b + b / 2, .3)
        elif kind == "shaker":
            for i in range(8): M.add(lp(hat(.08), 2), t + i * b / 2, .35 if i % 2 else .2)
            M.add(kick(g=.7), t, .7); M.add(kick(g=.7), t + 1.5 * b, .5); M.add(lp(snare(), 3), t + 3 * b, .3)
        t += 4 * b; bar += 1

def tao(k, sec=20.0):
    M = Mix(sec)
    if k == 1:   # doanh nghiệp tích cực
        bpm = 110; b = 60 / bpm; prog = [(60, 0), (67, 0), (69, 1), (65, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi)
            for f in c: M.add(piano(f, 2.2), t, .25)
            for j in range(8): M.add(pluck(c[j % 3] * 2, .4), t + j * b / 2, .22)
            M.add(bass(mtof(r - 24), b * 4), t, .5); t += 4 * b; i += 1
        drums(M, bpm, sec, "pop", 60 / bpm * 4)
    elif k == 2:  # tin nóng kịch tính
        bpm = 104; b = 60 / bpm; six = b / 4; prog = [57, 53, 55, 52]; mi = [1, 0, 0, 0]
        M.add(boom(), 0, 1.0); M.add(braam(), 0, .9); t = 1.4; i = 0
        while t < sec:
            c = chord(prog[i % 4], mi[i % 4]); pat = [0, 1, 2, 1, 0, 2, 1, 2] * 2
            for j, p in enumerate(pat): M.add(strings(c[p] * 2, six * .9), t + j * six, .22)
            for j in range(8): M.add(bass(c[0] / 2, b / 2), t + j * b / 2, .35)
            M.add(kick(), t, .8); M.add(kick(), t + 2 * b, .8); M.add(tom(110), t + b, .5); M.add(tom(95), t + 3 * b, .5); M.add(tom(80), t + 3.5 * b, .55)
            t += 4 * b; i += 1
    elif k == 3:  # lo-fi
        bpm = 78; b = 60 / bpm; prog = [(62, 1), (67, 0), (60, 0), (57, 1)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi, True)
            for j, f in enumerate(c): M.add(lp(rhodes(f, 3.0), 3), t + j * .02, .22)
            M.add(lp(rhodes(c[-1] * 2, 1.0), 3), t + 2.5 * b, .12)
            M.add(bass(mtof(r - 24), b * 3.5), t, .45); t += 4 * b; i += 1
        drums(M, bpm, sec, "lofi"); M.x += vinyl(M.n) * 1.0
    elif k == 4:  # ambient
        prog = [(57, 1), (53, 0), (60, 0), (55, 0)]; t = 0; i = 0; L = 5.0
        while t < sec:
            r, mi = prog[i % 4]; M.add(pad(chord(r, mi) + [mtof(r + 12)], L + 1.5, a=1.5, rel=1.5, br=16), t, .5)
            M.add(bell(mtof(r + 24), 3), t + 1.0, .08); t += L; i += 1
    elif k == 5:  # piano cảm xúc
        bpm = 72; b = 60 / bpm; prog = [(57, 1), (53, 0), (60, 0), (55, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi); arp = [mtof(r - 12)] + c + [c[1] * 2, c[2]]
            for j, f in enumerate(arp): M.add(piano(f, 2.5), t + j * b / 2, .3)
            M.add(piano(mtof(r - 24), 3.5), t, .3); t += 4 * b; i += 1
        M.add(pad([mtof(45), mtof(52)], sec, a=3, rel=2, br=20), 0, .12)
    elif k == 6:  # công nghệ
        bpm = 120; b = 60 / bpm; prog = [(57, 1), (53, 0), (55, 0), (52, 1)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi)
            for j in range(16): M.add(synth(c[j % 3] * (2 if j % 4 < 2 else 4), b / 4 * .9, 2), t + j * b / 4, .14)
            M.add(pad(c, b * 4, a=.3, rel=.4, br=12), t, .25); M.add(bass(c[0] / 2, b * 4), t, .4); t += 4 * b; i += 1
        drums(M, bpm, sec, "four", 60 / bpm * 8)
    elif k == 7:  # trap nhẹ
        bpm = 140; b = 60 / bpm * 2; prog = [57, 53, 55, 52]; t = 0; i = 0
        while t < sec:
            r = prog[i % 4]; M.add(b808(mtof(r - 24), b * 1.5), t, .9); M.add(b808(mtof(r - 24), b), t + 2.5 * b / 2, .7)
            M.add(bell(mtof(r + 12), 1.2), t, .15); M.add(bell(mtof(r + 15), 1.2), t + b, .12); M.add(bell(mtof(r + 19), 1.2), t + 1.5 * b, .1)
            t += 2 * b; i += 1
        drums(M, 140 / 2, sec, "trap")
    elif k == 8:  # phố Wall tự tin (funk)
        bpm = 100; b = 60 / bpm; t = 0; i = 0; prog = [(52, 1), (52, 1), (57, 1), (55, 0)]
        line = [0, None, 0, 12, None, 10, 7, None, 0, None, 0, 3, 5, None, 7, 10]
        while t < sec:
            r, mi = prog[i % 4]
            for j, s_ in enumerate(line):
                if s_ is not None: M.add(bass(mtof(r - 24 + s_), b / 4 * .9), t + j * b / 4, .55)
            for j in (1, 3): M.add(lp(rhodes(chord(r + 12, mi, True)[1], .3), 2), t + j * b + b / 4, .2)
            M.add(clap(), t + b, .6); M.add(clap(), t + 3 * b, .6); t += 4 * b; i += 1
        drums(M, bpm, sec, "pop")
    elif k == 9:  # hồi hộp
        b = .5; t = 0
        M.add(pad([mtof(38), mtof(45), mtof(46)], sec, a=3, rel=2, br=30), 0, .5)
        while t < sec: M.add(tick(), t, .5); M.add(tick(), t + b / 2, .2); t += b
        for s_ in np.arange(0, sec, 4): M.add(boom(2), s_, .35); M.add(strings(mtof(70), 1.5), s_ + 2, .06)
    elif k == 10:  # điện ảnh hùng tráng
        bpm = 90; b = 60 / bpm; prog = [(50, 1), (46, 0), (53, 0), (48, 0)]; t = 0; i = 0
        M.add(braam(4), 0, 1.0); M.add(boom(3), 0, .9)
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi)
            M.add(pad([f / 2 for f in c] + c, b * 4 + .5, a=.2, rel=.6, br=8), t, .45)
            for j in range(8): M.add(strings(c[j % 3] * 2, b / 2 * .9), t + j * b / 2, .18)
            if i % 2 == 1: M.add(boom(2), t, .5)
            t += 4 * b; i += 1
        drums(M, bpm, sec, "epic", 60 / bpm * 4)
    elif k == 11:  # synthwave
        bpm = 105; b = 60 / bpm; prog = [(57, 1), (53, 0), (60, 0), (55, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi)
            p = pad(c, b * 4, a=.01, rel=.05, br=6); g = np.repeat((np.arange(len(p) // int(SR * b / 4) + 1) % 2 == 0) * 1.0, int(SR * b / 4))[:len(p)]
            M.add(lp(p * g, 40), t, .35)
            for j in range(8): M.add(bass(c[0] / 2, b / 2 * .9), t + j * b / 2, .45)
            for j in range(16): M.add(synth(c[(j * 2) % 3] * 4, b / 4 * .8, 4), t + j * b / 4, .08)
            M.add(kick(), t, .9); M.add(kick(), t + 2 * b, .9); M.add(lp(snare(.4), 2), t + b, .6); M.add(lp(snare(.4), 2), t + 3 * b, .6)
            t += 4 * b; i += 1
    elif k == 12:  # deep house
        bpm = 122; b = 60 / bpm; prog = [(57, 1), (52, 1), (53, 0), (55, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi, True)
            for j in (0.5, 1.5, 2.75, 3.5):
                for f in c: M.add(lp(rhodes(f, .35), 2), t + j * b, .12)
            for j in range(8): M.add(bass(c[0] / 2, b / 2 * .7), t + j * b / 2 + b / 4, .4)
            t += 4 * b; i += 1
        drums(M, bpm, sec, "four")
    elif k == 13:  # acoustic tươi sáng
        bpm = 96; b = 60 / bpm; prog = [(55, 0), (62, 0), (64, 1), (60, 0)]; t = 0; i = 0
        pat = [0, 2, 1, 2, 0, 2, 1, 2]
        while t < sec:
            r, mi = prog[i % 4]; c = [mtof(r - 12)] + chord(r, mi)
            for j, p in enumerate(pat): M.add(pluck(c[p + 1 if j else 0] if j else c[0], 1.2), t + j * b / 2, .35)
            for j in (1, 3): M.add(pluck(c[2] * 2, .5), t + j * b + b / 4, .15)
            t += 4 * b; i += 1
        drums(M, bpm, sec, "shaker", 60 / bpm * 4)
    elif k == 14:  # marimba vui
        bpm = 112; b = 60 / bpm; prog = [(60, 0), (65, 0), (67, 0), (60, 0)]; t = 0; i = 0
        mel = [0, 4, 7, 12, 7, 4, 9, 7]
        while t < sec:
            r, mi = prog[i % 4]
            for j, s_ in enumerate(mel): M.add(marimba(mtof(r + 12 + s_), .5), t + j * b / 2, .35)
            M.add(marimba(mtof(r - 12), .8), t, .4); M.add(marimba(mtof(r - 5), .8), t + 2 * b, .35)
            t += 4 * b; i += 1
        drums(M, bpm, sec, "soft", 60 / bpm * 4)
    elif k == 15:  # thời sự
        bpm = 120; b = 60 / bpm; prog = [(50, 1), (50, 1), (46, 0), (48, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi)
            for j in range(16): M.add(bass(c[0] / 2, b / 4 * .8), t + j * b / 4, .4 if j % 4 == 0 else .25)
            for j in range(16): M.add(tick(), t + j * b / 4, .35 if j % 4 == 0 else .15)
            M.add(pad(c, b * 4, a=.4, rel=.4, br=14), t, .3)
            if i % 2 == 0: M.add(bell(c[2] * 2, 1.5), t, .1)
            M.add(kick(), t, .7); M.add(kick(), t + 2 * b, .7); t += 4 * b; i += 1
    elif k == 16:  # nhiệt đới
        bpm = 100; b = 60 / bpm; prog = [(57, 1), (53, 0), (60, 0), (55, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r + 12, mi)
            for j in (0, .75, 1.5, 2.5, 3.25): M.add(pluck(c[int(j * 2) % 3], .5), t + j * b, .3)
            for j in (1, 2.5, 3): M.add(marimba(c[2] * 2, .4), t + j * b, .18)
            M.add(bass(mtof(r - 24), b * 1.5), t, .45); M.add(bass(mtof(r - 17), b), t + 2.5 * b, .35)
            t += 4 * b; i += 1
        drums(M, bpm, sec, "shaker")
    elif k == 17:  # tối giản đồng hồ
        b = .5; t = 0; prog = [45, 41, 48, 43]; i = 0
        while t < sec:
            for j in range(8): M.add(tick(), t + j * b / 2, .4 if j % 2 == 0 else .18)
            M.add(b808(mtof(prog[i % 4] - 12), 2.0), t, .55); M.add(bell(mtof(prog[i % 4] + 24), 1.8), t + 1, .07)
            t += 4 * b; i += 1
    elif k == 18:  # căng thẳng u tối
        bpm = 70; b = 60 / bpm; prog = [(50, 1), (49, 0), (48, 0), (47, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, True)
            M.add(pad([f / 2 for f in c] + [c[0]], b * 4 + .4, a=.6, rel=.6, br=22), t, .55)
            M.add(piano(mtof(r + 12), 3), t, .2); M.add(piano(mtof(r + 13), 2.5), t + 2 * b, .14)
            M.add(boom(2), t, .4); t += 4 * b; i += 1
    elif k == 19:  # truyền cảm hứng
        bpm = 100; b = 60 / bpm; prog = [(60, 0), (67, 0), (69, 1), (65, 0)]; t = 0; i = 0
        while t < sec:
            r, mi = prog[i % 4]; c = chord(r, mi)
            for j in range(8): M.add(piano(c[j % 3] * (2 if j % 2 else 1), 1.2), t + j * b / 2, .22)
            M.add(pad(c, b * 4 + .3, a=1.0, rel=.6, br=12), t, .12 + .04 * i)
            M.add(bass(mtof(r - 24), b * 4), t, .25 + .05 * min(i, 4)); t += 4 * b; i += 1
        drums(M, bpm, sec, "soft", 60 / bpm * 8); drums(M, bpm, sec, "pop", 60 / bpm * 16)
    elif k == 20:  # Á Đông ngũ cung
        bpm = 84; b = 60 / bpm; ngu = [0, 2, 4, 7, 9, 12, 14]; t = 0; i = 0
        mel = [4, 3, 2, 3, 5, 4, 2, 1, 0, 1, 2, 4, 3, 2, 1, 0]
        M.add(pad([mtof(50), mtof(57)], sec, a=2, rel=2, br=24), 0, .3)
        while t < sec:
            for j in range(4): M.add(bell(mtof(62 + ngu[mel[(i * 4 + j) % 16]]), 2.2), t + j * b, .22)
            M.add(tom(70, .7), t, .45); M.add(tom(90, .5), t + 2.5 * b, .3); t += 4 * b; i += 1
    return M.done()

def ghi(path, x):
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())

if __name__ == "__main__":
    od = sys.argv[1] if len(sys.argv) > 1 else "/tmp/nhac20"; os.makedirs(od, exist_ok=True)
    for k, ten, _ in KIEU:
        ghi(os.path.join(od, "%02d.wav" % k), tao(k, 20.0)); print(k, ten, flush=True)
