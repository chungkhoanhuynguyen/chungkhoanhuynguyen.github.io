"""Ảnh động chân dung góc màn hình: miệng mở theo độ to nhỏ của giọng, chớp mắt, gật đầu nhẹ.
Một ảnh duy nhất -> nhiều khung, chạy CPU (numpy + OpenCV), không cần GPU, không cần dịch vụ ngoài."""
import numpy as np, cv2, subprocess

CROP = (85, 125, 645, 685)          # x0,y0,x1,y1 trong ảnh gốc: đầu + vai, không dính logo/nền khác
MC = np.array([358.0, 421.0])        # tâm miệng
HW = 38.0                            # nửa chiều rộng miệng
ML = 421.0                           # đường môi
CHIN = 482.0
EYES = [((325.0, 306.0), 17.0, 7.0, 7.0), ((420.0, 319.0), 18.0, 7.5, 7.0)]  # tâm, nửa rộng, nửa cao, góc nghiêng

def _sm(t, a, b):
    t = np.clip((t - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)

class ChanDung:
    def __init__(self, path, size=256):
        im = cv2.imread(path); self.size = size
        x0, y0, x1, y1 = CROP
        self.im = im[y0:y1, x0:x1].copy()
        self.H, self.W = self.im.shape[:2]
        self.ox, self.oy = x0, y0
        yy, xx = np.mgrid[0:self.H, 0:self.W].astype(np.float32)
        self.X = xx + x0; self.Y = yy + y0           # toạ độ ảnh gốc
        dx = self.X - MC[0]
        self.wn = np.exp(-(dx / (0.62 * HW)) ** 2)    # kéo môi dưới (hẹp, giữ khoé miệng)
        self.ww = np.exp(-0.5 * (dx / 62.0) ** 2)     # kéo cằm (rộng)
        a = 1 - _sm(self.Y, ML + 22, ML + 42)         # vùng môi -> vùng cằm
        self.wy = _sm(self.Y, ML, ML + 5) * (1 - _sm(self.Y, CHIN, CHIN + 55))
        self.wbase = (a * self.wn + (1 - a) * self.ww) * self.wy
        self.gx = np.exp(-(dx / (1.6 * HW)) ** 2) * _sm(self.Y, ML - 20, ML - 8) * (1 - _sm(self.Y, ML + 26, ML + 40))
        self.skin = [self._cheek()] * 2
        self.mask = self._mask()

    def _cheek(self):
        p = np.concatenate([self.im[372 - self.oy:382 - self.oy, 300 - self.ox:320 - self.ox].reshape(-1, 3), self.im[372 - self.oy:382 - self.oy, 400 - self.ox:420 - self.ox].reshape(-1, 3)]).astype(np.float32)
        return tuple(int(v * 0.97) for v in np.median(p, 0))

    def _skin(self, c):
        x, y = int(c[0] - self.ox), int(c[1] - self.oy)
        p = self.im[y - 15:y - 11, x - 6:x + 6].reshape(-1, 3).astype(np.float32)
        return tuple(int(v) for v in np.median(p, 0))

    def _mask(self):
        s = self.size; m = np.zeros((s, s), np.uint8); i = 4; r = int(s * 0.16)
        cv2.rectangle(m, (i + r, i), (s - i - r, s - i), 255, -1); cv2.rectangle(m, (i, i + r), (s - i, s - i - r), 255, -1)
        for cx, cy in ((i + r, i + r), (s - i - r, i + r), (i + r, s - i - r), (s - i - r, s - i - r)): cv2.circle(m, (cx, cy), r, 255, -1, cv2.LINE_AA)
        return cv2.GaussianBlur(m, (3, 3), 0)

    def frame(self, mo, wide=0.0, blink=0.0, t=0.0, nod=0.0):
        """mo 0..1 độ mở miệng; wide -1..1 (tròn <-> bè); blink 0..1; trả BGR size×size (đã bo góc + viền)."""
        h = 17.0 * float(np.clip(mo, 0, 1))
        im = self.im
        if h > 0.3 or abs(wide) > 0.02:
            s = 1.0 + 0.09 * wide
            mx = self.X - self.gx * (self.X - MC[0]) * (1 - 1 / s) * 1.0
            my = self.Y - h * self.wbase
            im = cv2.remap(self.im, (mx - self.ox).astype(np.float32), (my - self.oy).astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        else:
            im = self.im.copy()
        if h > 1.2:
            lay = np.zeros_like(im); a = np.zeros(im.shape[:2], np.float32)
            cx, cy = MC[0] - self.ox, ML - self.oy
            hwid = HW * (0.62 + 0.14 * wide) * (0.8 + 0.2 * mo)
            cv2.ellipse(lay, (int(cx), int(cy + h * 0.5)), (int(hwid), int(h * 0.5 + 1)), 0, 0, 360, (34, 30, 72), -1, cv2.LINE_AA)
            th = int(min(h * 0.32, 7))
            if th >= 2: cv2.ellipse(lay, (int(cx), int(cy + th * 0.5 + 1)), (int(hwid * 0.86), th), 0, 180, 360, (205, 205, 215), -1, cv2.LINE_AA)
            cv2.ellipse(a, (int(cx), int(cy + h * 0.5)), (int(hwid), int(h * 0.5 + 1)), 0, 0, 360, 1.0, -1, cv2.LINE_AA)
            a = cv2.GaussianBlur(a, (0, 0), 1.1)[..., None]
            im = (im * (1 - a) + lay * a).astype(np.uint8)
        if blink > 0.05:
            ov = im.copy()
            for (c, ew, eh, ang), sk in zip(EYES, self.skin):
                ctr = (int(c[0] - self.ox), int(c[1] - self.oy))
                cv2.ellipse(ov, ctr, (int(ew), int(max(1, eh * 1.15 * blink))), ang, 0, 360, sk, -1, cv2.LINE_AA)
                if blink > 0.6:
                    cv2.ellipse(ov, (ctr[0], ctr[1] + int(eh * 0.5 * blink)), (int(ew), 2), ang, 0, 180, (45, 35, 40), 1, cv2.LINE_AA)
            im = cv2.addWeighted(im, 0.25, ov, 0.75, 0)
        # đung đưa nhẹ: xoay, dịch, thở
        rot = 0.9 * np.sin(t * 0.9) + 0.5 * np.sin(t * 2.3 + 1.0)
        dx = 2.0 * np.sin(t * 0.7 + 0.5); dy = 1.5 * np.sin(t * 1.1) + nod * 3.0
        sc = 1.0 + 0.004 * np.sin(t * 1.6)
        M = cv2.getRotationMatrix2D((self.W / 2, self.H * 0.62), rot, sc); M[:, 2] += (dx, dy)
        im = cv2.warpAffine(im, M, (self.W, self.H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        out = cv2.resize(im, (self.size, self.size), interpolation=cv2.INTER_AREA)
        return out

    def bubble(self, **k):
        """BGRA có bo góc + viền vàng."""
        f = self.frame(**k); s = self.size
        a = self.mask.copy()
        ring = cv2.dilate(self.mask, np.ones((5, 5), np.uint8)) - cv2.erode(self.mask, np.ones((5, 5), np.uint8))
        f = f.copy(); f[ring > 0] = (60, 190, 255)         # viền vàng (BGR)
        a = np.maximum(a, ring)
        return np.dstack([f, a])


def dieu_khien(wav, fps=30):
    """Từ file âm thanh -> mảng (mo, wide, blink, nod) mỗi khung hình."""
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", wav, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.float32); sr = 16000; hop = sr // fps; n = len(x) // hop
    fr = x[:n * hop].reshape(n, hop); w = np.hanning(hop)
    rms = np.sqrt((fr ** 2).mean(1) + 1e-10); db = 20 * np.log10(rms + 1e-9)
    sp = np.abs(np.fft.rfft(fr * w, axis=1)); f = np.fft.rfftfreq(hop, 1 / sr)
    cen = (sp * f).sum(1) / (sp.sum(1) + 1e-9)
    top = np.percentile(db, 96); thr = top - 30
    k = 13; loc = np.convolve(np.pad(db, (k // 2, k // 2), mode="edge"), np.ones(k) / k, "valid")   # mức trung bình ~0,4 giây
    ref = np.median(db[db > thr]) if (db > thr).any() else top
    mo = np.clip(0.22 + (db - loc) / 6.5 + (db - ref) / 26.0, 0, 1)       # nhịp âm tiết + độ to của câu
    mo[db < thr] = 0
    # làm mượt: mở nhanh, đóng chậm
    o = np.zeros(n); p = 0.0
    for i in range(n):
        p = mo[i] if mo[i] > p else p + (mo[i] - p) * 0.6
        o[i] = p
    nói = db > thr
    c = np.where(nói, cen, np.nan); lo, hi = np.nanpercentile(c, 15), np.nanpercentile(c, 85)
    wd = np.nan_to_num((cen - (lo + hi) / 2) / ((hi - lo) / 2 + 1e-9), nan=0.0); wd = np.clip(wd, -1, 1)
    wd = np.convolve(wd, np.ones(5) / 5, "same") * (o > 0.08)
    rng = np.random.default_rng(7)
    bl = np.zeros(n); t = rng.uniform(1.2, 3.0)
    while t * fps < n:
        i = int(t * fps)
        for k, v in enumerate((0.5, 1.0, 1.0, 0.6, 0.2)):
            if i + k < n: bl[i + k] = v
        t += rng.uniform(2.4, 5.5)
    nod = np.convolve(np.clip(np.diff(o, prepend=0), 0, None), np.ones(6) / 6, "same")
    return o, wd, bl, np.clip(nod * 2.5, 0, 1)
