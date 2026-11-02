# Clip thử 2D (10 giây, dọc 1080x1920): "Mới ngày 26 mà ví đã rỗng"
import sys, os, time, subprocess, math, cairo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import doodle
W, H, FPS, SEC = 1080, 1920, 30, 10
out = sys.argv[1] if len(sys.argv) > 1 else "thu2d.mp4"
FONT = os.path.join(os.path.dirname(__file__), "..", "engine", "fonts", "BeVietnamPro-Black.ttf")
p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                      "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", out], stdin=subprocess.PIPE)
sf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H); c = cairo.Context(sf)
c.select_font_face("Be Vietnam Pro", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
def phong():
    c.set_source_rgb(1.0, 0.95, 0.86); c.paint()
    c.set_source_rgb(0.93, 0.82, 0.66); c.rectangle(0, 1330, W, H); c.fill()
    doodle._p(c, 9); c.move_to(0, 1330); c.line_to(W, 1330); c.stroke()
    # cửa sổ
    c.rectangle(90, 260, 330, 380); c.set_source_rgb(0.75, 0.88, 1.0); c.fill_preserve(); doodle._p(c, 9); c.stroke()
    c.move_to(255, 260); c.line_to(255, 640); c.move_to(90, 450); c.line_to(420, 450); c.stroke()
def lich(t):
    x, y = 640, 250; c.save(); c.translate(x + 150, y); c.rotate(math.sin(t * 2) * 0.03); c.translate(-150, 0)
    c.rectangle(0, 0, 300, 340); c.set_source_rgb(1, 1, 1); c.fill_preserve(); doodle._p(c, 9); c.stroke()
    c.rectangle(0, 0, 300, 90); c.set_source_rgb(0.2, 0.36, 0.62); c.fill_preserve(); doodle._p(c, 9); c.stroke()
    c.set_source_rgb(1, 1, 1); c.set_font_size(48); te = c.text_extents("THÁNG 11"); c.move_to(150 - te.width / 2, 63); c.show_text("THÁNG 11")
    c.set_source_rgb(0.17, 0.2, 0.26); c.set_font_size(170); te = c.text_extents("26"); c.move_to(150 - te.width / 2, 290); c.show_text("26")
    c.restore()
def chu(txt, y, size, col, a):
    if a <= 0: return
    c.set_font_size(size); te = c.text_extents(txt); x = (W - te.width) / 2
    c.set_source_rgba(1, 1, 1, a); c.set_line_width(18); c.move_to(x, y); c.text_path(txt); c.stroke()
    c.set_source_rgba(*col, a); c.move_to(x, y); c.show_text(txt)
t0 = time.time()
for f in range(SEC * FPS):
    t = f / FPS; phong(); lich(t)
    noi1 = abs(math.sin(t * 11)) if 0.5 < t < 4.5 else 0
    noi2 = abs(math.sin(t * 10)) if 5.2 < t < 9.5 else 0
    doodle.ve(c, "cho", 300, 1600, 1.2, t, mood="buon" if t < 5 else "ngac", noi=noi1, tay="om" if t < 5 else "xuoi")
    gx = 1550 - min(1, max(0, (t - 3.8) / 1.2)) * 720
    doodle.ve(c, "gau", gx, 1600, 1.2, t + 1, mood="vui", noi=noi2, tay="chi" if t > 5.5 else "xuoi", huong=-1)
    if t < 5:
        chu("Mới ngày 26", 820, 96, (0.17, 0.2, 0.26), min(1, t * 3)); chu("mà ví đã rỗng…", 940, 96, (0.9, 0.25, 0.25), min(1, (t - 0.6) * 3))
    else:
        chu("Lương về: trích 10%", 820, 84, (0.17, 0.2, 0.26), min(1, (t - 5) * 3)); chu("TRƯỚC khi tiêu", 940, 96, (0.15, 0.6, 0.3), min(1, (t - 5.6) * 3))
    p.stdin.write(sf.get_data())
p.stdin.close(); p.wait()
print("2D: %d khung, %.1fs dựng (%.3fs/khung)" % (SEC * FPS, time.time() - t0, (time.time() - t0) / (SEC * FPS)))
