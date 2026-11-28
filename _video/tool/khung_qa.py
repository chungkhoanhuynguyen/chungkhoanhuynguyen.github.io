# khung_qa.py VIDEO – soát TỪNG KHUNG HÌNH video dọc (QL1 28/11, học từ mromidev/claude-animated-shorts
# templates/scripts/short_qa.py, giấy phép MIT © 2026 Mr omi – bản rút gọn, chỉ numpy + ffmpeg).
# Dò: khung đen, khung trắng chói, đoạn đứng hình >=0,4s (12 khung), "giật/nhảy hình" (khung khác hẳn 2 bên),
# tỉ lệ khung đứng yên, độ sáng/bão hoà trung bình. In ra vài dòng để tu_soat.sh ghép vào KEY_soat.txt.
import subprocess, sys
import numpy as np

vid = sys.argv[1]
W, H = 90, 160
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", vid, "-vf", f"fps=30,scale={W}:{H}:flags=area",
                      "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
n = len(F)
if n < 30:
    print(f"== KHUNG HÌNH: chỉ đọc được {n} khung – bỏ qua"); sys.exit(0)
f32 = F.astype(np.float32) / 255
luma = f32 @ np.array([0.2126, 0.7152, 0.0722], np.float32)
mx, mn = f32.max(-1), f32.min(-1)
sat = np.where(mx > 0.06, (mx - mn) / np.maximum(mx, 1e-6), 0).reshape(n, -1).mean(1)
mean = luma.reshape(n, -1).mean(1)
diff = np.abs(np.diff(F.astype(np.int16), axis=0)).mean(axis=(1, 2, 3))
med = np.array([np.median(diff[max(0, i - 8):i + 9]) for i in range(len(diff))])
t = lambda i: f"{i / 30:.1f}s"
pops = [i + 1 for i in range(len(diff)) if diff[i] > 3 * med[i] + 4.0]
pops = [p for k, p in enumerate(pops) if k == 0 or p - pops[k - 1] > 3]
black = [i for i in range(n) if mean[i] < 0.04]
white = [i for i in range(n) if mean[i] > 0.93]
frozen, s0 = [], None
for i in range(len(diff)):
    if diff[i] < 0.02:
        s0 = i if s0 is None else s0
    else:
        if s0 is not None and i - s0 >= 12: frozen.append((s0, i))
        s0 = None
if s0 is not None and len(diff) - s0 >= 12: frozen.append((s0, len(diff)))

def gom(ix):  # gộp chỉ số khung liền nhau thành khoảng thời gian
    out, a = [], None
    for k, i in enumerate(ix):
        if a is None: a = i
        if k == len(ix) - 1 or ix[k + 1] != i + 1:
            out.append(t(a) if a == i else f"{t(a)}–{t(i)}"); a = None
    return ", ".join(out[:12]) or "không"

print(f"== KHUNG HÌNH ({n} khung @30fps, học claude-animated-shorts)")
print(f"Khung đen: {gom(black)}")
print(f"Khung trắng chói: {gom(white)}")
print("Đứng hình >=0,4s: " + (", ".join(f"{t(a)}–{t(b)}" for a, b in frozen[:12]) or "không"))
print(f"Giật/nhảy hình (đổi cảnh cứng cũng hiện ở đây): {len(pops)} lần" + (" tại " + ", ".join(t(i) for i in pops[:15]) if pops else ""))
print(f"Khung gần đứng yên: {(diff < 0.3).mean() * 100:.0f}% | sáng TB {mean.mean():.2f} | bão hoà TB {sat.mean():.2f} (kênh mẫu 20 Shorts: sáng 0,43–0,54, bão hoà 0,38–0,65)")
canh = []
if black: canh.append("có khung đen")
if sum(b - a for a, b in frozen) > 60: canh.append("đứng hình tổng >2s")
if mean.mean() < 0.15: canh.append("video quá tối")
print("CẢNH BÁO KHUNG: " + ("; ".join(canh) if canh else "không"))
