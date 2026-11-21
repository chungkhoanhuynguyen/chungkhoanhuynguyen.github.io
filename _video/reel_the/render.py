"""Dựng reel "kiểu thẻ": python3 render.py cfg.json timing.json out.mp4 [fps=24] [rong=720]
Khung HTML (the.html) vẽ theo thời gian t (setT) -> Playwright chụp từng khung -> ffmpeg ghép (giọng voice.wav do tts.py tạo)."""
import json, os, sys, subprocess, shutil, tempfile
from concurrent.futures import ProcessPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "_fb", "anh_lo")); from lay_gia import lay
def chup(a):
    k, f0, f1, plan, fps, W, tmp = a
    from playwright.sync_api import sync_playwright
    html = open(os.path.join(HERE, "the.html"), encoding="utf-8").read().replace("FONT", "file://" + os.path.join(ROOT, "_video", "engine", "fonts"))
    open(os.path.join(tmp, "p%d.html" % k), "w", encoding="utf-8").write(html)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=W / 1080)
        pg.add_init_script("window.PLAN=" + json.dumps(plan, ensure_ascii=False)); pg.goto("file://" + os.path.join(tmp, "p%d.html" % k)); pg.evaluate("document.fonts.ready")
        for f in range(f0, f1):
            pg.evaluate("setT(%f)" % (f / fps)); pg.screenshot(path=os.path.join(tmp, "f%05d.jpg" % f), type="jpeg", quality=92)
        b.close()
if __name__ == "__main__":
    sys.argv[1:4] = [os.path.abspath(a) for a in sys.argv[1:4]]; os.chdir(ROOT)  # lay_gia đọc data/c/*.bin theo gốc repo
    cfg = json.load(open(sys.argv[1], encoding="utf-8")); tm = json.load(open(sys.argv[2])); out = sys.argv[3]
    fps = int(sys.argv[4]) if len(sys.argv) > 4 else 24; W = int(sys.argv[5]) if len(sys.argv) > 5 else 720
    plan = {"cfg": cfg, "timing": tm, "px": lay(cfg["ma"], cfg.get("gia_n", 125))}
    tmp = tempfile.mkdtemp(prefix="reel_the_"); n = int((tm["total"] + 0.3) * fps); N = os.cpu_count() or 2
    ch = [(k, k * n // N, (k + 1) * n // N, plan, fps, W, tmp) for k in range(N)]
    with ProcessPoolExecutor(N) as ex: list(ex.map(chup, ch))
    wav = os.path.join(os.path.dirname(os.path.abspath(sys.argv[2])), "mix.wav")
    if not os.path.exists(wav): wav = os.path.join(os.path.dirname(os.path.abspath(sys.argv[2])), "voice.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", os.path.join(tmp, "f%05d.jpg"), "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "24", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out], check=True)
    shutil.rmtree(tmp, ignore_errors=True); print("XONG", out)
