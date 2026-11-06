# Nhạc nền tự tổng hợp, kịch tính (không bản quyền): braam + boom ở hook, ostinato dây staccato, trống trận, impact chuyển cảnh
import numpy as np, wave, subprocess
SR = 44100; BPM = 104; rng = np.random.default_rng(7)
def env(n, a=0.005, r=0.3):
    t = np.arange(n)/SR; return np.minimum(1, t/a)*np.exp(-t/r)
def saw(f, n, harm=8):
    t = np.arange(n)/SR; return sum(((-1)**(k+1))*np.sin(2*np.pi*f*k*t)/k for k in range(1, harm+1))
def lp(x, k=6): return np.convolve(x, np.ones(k)/k, "same")
def kick(d=0.5):
    n = int(SR*d); t = np.arange(n)/SR; f = 42 + 110*np.exp(-t*28)
    return np.tanh(2.2*np.sin(2*np.pi*np.cumsum(f)/SR))*env(n, 0.002, 0.2)
def tom(f0=90, d=0.5):
    n = int(SR*d); t = np.arange(n)/SR; f = f0*(1 + 0.6*np.exp(-t*18))
    s = np.sin(2*np.pi*np.cumsum(f)/SR)*env(n, 0.002, 0.22); nz = lp(rng.standard_normal(n), 12)*env(n, 0.001, 0.05)*0.4
    return np.tanh(1.8*(s+nz))
def boom(d=3.0, g=1.0):
    n = int(SR*d); t = np.arange(n)/SR; f = 30 + 70*np.exp(-t*5)
    s = np.tanh(2.5*np.sin(2*np.pi*np.cumsum(f)/SR))*env(n, 0.003, 1.1)
    nz = lp(rng.standard_normal(n), 25)*env(n, 0.001, 0.25)*0.6
    return (s + nz)*g
def braam(d=3.0, root=55.0):
    n = int(SR*d); s = saw(root/2, n, 12) + saw(root/2*1.498, n, 10)*0.7 + saw(root, n, 8)*0.5
    return np.tanh(1.5*lp(s, 10))*env(n, 0.04, 1.4)*0.6
def riser(d=1.2):
    n = int(SR*d); t = np.arange(n)/SR; x = lp(rng.standard_normal(n), 40)*(t/d)**2*2
    tone = np.sin(2*np.pi*np.cumsum(200 + 900*(t/d)**2)/SR)*(t/d)**3*0.3
    return x + tone
def string_note(f, d):
    n = int(SR*d); return lp(saw(f, n, 7), 4)*env(n, 0.004, d*0.45)
def track(total, bounds):
    n = int(SR*(total+4)); out = np.zeros(n)
    def add(s, at, g=1.0):
        i = int(at*SR)
        if i >= n: return
        j = min(n, i+len(s)); out[i:j] += s[:j-i]*g
    add(boom(3.0), 0.0, 1.1); add(braam(3.2), 0.0, 1.0)
    beat = 60/BPM; six = beat/4
    # vòng hợp âm thứ: Am – F – G – E (căng, kịch tính)
    prog = [(110.0, 130.8, 164.8), (87.3, 110.0, 130.8), (98.0, 123.5, 146.8), (82.4, 103.8, 123.5)]
    t = 1.4; bar = 0
    while t < total - 0.8:
        ch = prog[bar % 4]
        # ostinato dây 16 nốt/ô nhịp
        pat = [0, 1, 2, 1, 0, 2, 1, 2, 0, 1, 2, 1, 0, 2, 1, 2]
        for i, p in enumerate(pat): add(string_note(ch[p]*2, six*0.9), t + i*six, 0.22)
        # bass xung
        for i in range(8): add(np.sin(2*np.pi*ch[0]/2*np.arange(int(SR*beat/2))/SR)*env(int(SR*beat/2), 0.003, 0.12), t + i*beat/2, 0.35)
        # trống trận: kick 1 & 3, tom dồn cuối ô nhịp
        add(kick(), t, 0.8); add(kick(), t + 2*beat, 0.8)
        add(tom(110), t + beat, 0.55); add(tom(95), t + 3*beat, 0.55); add(tom(80), t + 3.5*beat, 0.6)
        t += 4*beat; bar += 1
    for b in bounds[1:-1]:
        add(riser(1.0), max(0, b-1.0), 0.45); add(boom(1.6), b, 0.55)
    e = int(SR*total); fo = int(SR*1.8); out[e-fo:e] *= np.linspace(1, 0, fo); out[e:] = 0
    out = np.tanh(out[:e]*1.2)
    return out/(np.abs(out).max()+1e-9)*0.9
def write(path, x):
    with wave.open(path, "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(x, -1, 1)*32767).astype(np.int16).tobytes())
def ket_hop(total, bounds, lofi=False):
    """Anh Huy chốt 6/11: kết hợp mẫu 2 (kịch tính) + mẫu 3 (lo-fi).
    Mở bài (cảnh đầu) = 2 để giật người xem; thân bài = 3 nhẹ, dễ nghe giọng; cảnh cuối (kêu gọi/câu hỏi) = 2 để chốt mạnh."""
    import nhac20
    n = int(SR*total); b = list(bounds)
    a_end = min(max(b[1] if len(b) > 2 else total*.2, 4.0), total*.35)       # hết cảnh mở đầu
    z_beg = max(b[-2] if len(b) > 3 else total*.85, a_end + 4.0)             # đầu cảnh cuối
    if z_beg > total - 3: z_beg = total
    kt = nhac20.tao(2, total + 2)[:n]; lf = nhac20.tao(3, total + 2)[:n]
    kt = np.pad(kt, (0, max(0, n-len(kt)))); lf = np.pad(lf, (0, max(0, n-len(lf))))
    _r = lambda a: a / (np.sqrt(np.mean(a**2)) + 1e-9)          # cân bằng độ to 2 mẫu, không bị bật to ở mở/kết (anh Huy phản ánh 7/11)
    kt = _r(kt); lf = _r(lf)
    t = np.arange(n)/SR; xf = 1.6
    w = np.clip((t - a_end)/xf + .5, 0, 1)                                  # 0 -> 2, 1 -> 3
    if z_beg < total: w = w * np.clip((z_beg - t)/xf + .5, 0, 1)
    if lofi: w = np.ones_like(t)          # video kể chuyện: lo-fi chill cả bài (anh Huy 7/11)
    out = kt*np.sqrt(1-w) + lf*np.sqrt(w)
    fo = int(SR*1.8); out[-fo:] *= np.linspace(1, 0, fo)
    out = out/(np.sqrt(np.mean(out**2))+1e-9)*0.12            # chuẩn hoá theo RMS (không theo đỉnh)
    return np.clip(out, -0.95, 0.95)
def mix(video, bounds, out, music_db=-8, lofi=False):
    total = bounds[-1]
    try: x = ket_hop(total, bounds, lofi)
    except Exception as e: print("nhac ket hop loi, dung mau 2:", e, flush=True); x = track(total, bounds)
    write("/tmp/bgm.wav", x)
    fc = ("[1:a]volume=%ddB,aresample=44100[m];[0:a]asplit=2[v][sc];"
          "[m][sc]sidechaincompress=threshold=0.04:ratio=6:attack=20:release=350[md];"
          "[v][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]") % music_db
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", "/tmp/bgm.wav", "-filter_complex", fc,
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", out])
