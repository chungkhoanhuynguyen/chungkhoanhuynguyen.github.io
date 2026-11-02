# Hiệu ứng âm thanh hoạt hình cho video kể chuyện – tự tổng hợp bằng code (không bản quyền, không tốn phí).
# Mỗi biểu cảm ("dien") và hành động có 1 tiếng; thêm âm nền phố Hà Nội / Sài Gòn / quán cà phê.
import numpy as np
SR = 44100
rng = np.random.default_rng(7)
def _t(d): return np.arange(int(SR * d)) / SR
def _env(n, a=0.005, r=0.1):
    e = np.ones(n); na = max(1, int(SR * a)); nr = max(1, min(n, int(SR * r)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] *= np.linspace(1, 0, nr); return e
def _sweep(f0, f1, d, wave="sin"):
    t = _t(d); f = np.geomspace(f0, f1, len(t)); ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) if wave == "sin" else np.sign(np.sin(ph)) * 0.6
def _noise(d, color="white"):
    n = rng.standard_normal(int(SR * d))
    if color == "pink": n = np.cumsum(n); n -= np.convolve(n, np.ones(400) / 400, "same")
    if color == "brown": n = np.cumsum(n); n -= np.convolve(n, np.ones(4000) / 4000, "same")
    return n / (np.abs(n).max() + 1e-9)
def _lp(x, k=20): return np.convolve(x, np.ones(k) / k, "same")

# ---------- tiếng hành động / biểu cảm ----------
def boing():          # giật mình nhảy
    t = _t(0.55); f = 180 + 120 * np.sin(2 * np.pi * 9 * t) * np.exp(-t * 4)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 5) * 0.8
def pop():            # bong bóng / tim bay
    return _sweep(500, 1400, 0.07) * _env(int(SR * 0.07), 0.001, 0.05) * 0.7
def whoosh():         # lướt qua / chuyển cảnh
    n = _noise(0.45); e = np.sin(np.linspace(0, np.pi, len(n))) ** 2
    return _lp(n * e, 12) * 0.9
def thud():           # ngã ngửa
    t = _t(0.35); return (np.sin(2 * np.pi * 70 * t) + 0.5 * _lp(_noise(0.35), 60)) * np.exp(-t * 14) * 1.0
def sparkle():        # mắt lấp lánh
    out = np.zeros(int(SR * 0.7))
    for i, f in enumerate([2093, 2637, 3136, 4186, 3520]):
        s = np.sin(2 * np.pi * f * _t(0.25)) * np.exp(-_t(0.25) * 18) * 0.35; k = int(SR * 0.08 * i); out[k:k + len(s)] += s
    return out
def blush():          # ngại ngùng "pi-pi"
    out = np.zeros(int(SR * 0.5))
    for k in (0, 0.18):
        s = _sweep(900, 1300, 0.12) * _env(int(SR * 0.12), 0.01, 0.06) * 0.45; i = int(SR * k); out[i:i + len(s)] += s
    return out
def drip():           # giọt mồ hôi
    return _sweep(1800, 600, 0.12) * np.exp(-_t(0.12) * 25) * 0.6
def wah():            # khóc hu hu
    t = _t(1.1); f = 420 + 60 * np.sin(2 * np.pi * 5 * t) - 120 * t
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.3 * np.sin(4 * np.pi * np.cumsum(f) / SR)) * _env(len(t), 0.05, 0.3) * 0.35
def ting():           # thông báo điện thoại / chốt đơn
    s = np.zeros(int(SR * 0.5))
    for i, f in enumerate([1568, 2093]):
        x = np.sin(2 * np.pi * f * _t(0.3)) * np.exp(-_t(0.3) * 9) * 0.45; k = int(SR * 0.12 * i); s[k:k + len(x)] += x
    return s
def cash():           # tiếng két tiền / tiêu tiền
    s = np.concatenate([_lp(_noise(0.06), 3) * 0.5 * np.exp(-_t(0.06) * 60), np.zeros(int(SR * 0.04))])
    bell = (np.sin(2 * np.pi * 2637 * _t(0.6)) + 0.5 * np.sin(2 * np.pi * 3951 * _t(0.6))) * np.exp(-_t(0.6) * 6) * 0.4
    return np.concatenate([s, bell])
def step():           # bước chân mũm mĩm
    t = _t(0.12); return (np.sin(2 * np.pi * 110 * t) * 0.8 + _lp(_noise(0.12), 30) * 0.3) * np.exp(-t * 35)
def honk():           # còi xe máy "bíp bíp"
    out = np.zeros(int(SR * 0.6))
    for k in (0, 0.28):
        t = _t(0.18); x = (np.sign(np.sin(2 * np.pi * 420 * t)) * 0.4 + np.sin(2 * np.pi * 520 * t) * 0.3) * _env(len(t), 0.005, 0.03)
        i = int(SR * k); out[i:i + len(x)] += _lp(x, 6) * 0.35
    return out
def slurp():          # húp trà sữa
    n = _lp(_noise(0.5), 8) * (0.5 + 0.5 * np.sin(2 * np.pi * 14 * _t(0.5))); return n * _env(len(n), 0.03, 0.1) * 0.35
def tada():           # chốt bài học
    out = np.zeros(int(SR * 1.0))
    for i, f in enumerate([523, 659, 784, 1047]):
        x = (np.sin(2 * np.pi * f * _t(0.6)) + 0.3 * np.sin(4 * np.pi * f * _t(0.6))) * np.exp(-_t(0.6) * 4) * 0.25
        k = int(SR * (0.09 * i if i < 3 else 0.3)); out[k:k + len(x)] += x
    return out

DIEN = {"giat_minh": boing, "nga": thud, "ngai": blush, "mo_hoi": drip, "sang_mat": sparkle, "tim": pop,
        "khoc_hu": wah, "gai_dau": blush, "vo_bung": thud, "gian": boing}
HANH = {"pop": pop, "whoosh": whoosh, "ting": ting, "cash": cash, "step": step, "honk": honk, "slurp": slurp, "tada": tada}

# ---------- âm nền ----------
def nen(kieu, d):
    if kieu in ("pho_hanoi", "hem_saigon"):
        x = _lp(_noise(d, "brown"), 40) * 0.25 + _lp(_noise(d, "pink"), 200) * 0.06   # tiếng xe ầm ì xa
        for _ in range(int(d / 4)):                                                   # còi xe thỉnh thoảng
            h = honk() * rng.uniform(0.2, 0.45); i = rng.integers(0, max(1, len(x) - len(h))); x[i:i + len(h)] += h
        return x
    if kieu == "quan_ca_phe":
        x = _lp(_noise(d, "pink"), 120) * 0.08
        for _ in range(int(d / 2.5)):                                                 # tiếng cốc thìa
            c = np.sin(2 * np.pi * rng.uniform(2500, 3500) * _t(0.15)) * np.exp(-_t(0.15) * 30) * 0.08
            i = rng.integers(0, max(1, len(x) - len(c))); x[i:i + len(c)] += c
        return x
    if kieu == "mua": return _lp(_noise(d), 3) * 0.12
    return np.zeros(int(SR * d))

def track(total, events, nen_kieu=None, nen_db=-20):
    """events: [(giây, tên)], tên là mã biểu cảm (DIEN) hoặc hành động (HANH)."""
    out = np.zeros(int(SR * total) + SR)
    if nen_kieu: b = nen(nen_kieu, total); out[:len(b)] += b * 10 ** (nen_db / 20) * 4
    for st, k in events:
        f = DIEN.get(k) or HANH.get(k)
        if not f: continue
        s = f(); i = int(st * SR); out[i:i + len(s)] += s[:max(0, len(out) - i)]
    return np.clip(out, -1, 1)

if __name__ == "__main__":   # bản nghe thử: lần lượt từng tiếng trên nền phố Hà Nội
    import wave, sys
    names = list(DIEN) + list(HANH); ev = [(0.6 + i * 1.1, k) for i, k in enumerate(names)]
    x = track(0.6 + len(names) * 1.1 + 1, ev, "pho_hanoi")
    with wave.open(sys.argv[1] if len(sys.argv) > 1 else "sfx_demo.wav", "w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype(np.int16).tobytes())
    print("\n".join("%.1fs %s" % e for e in ev))
