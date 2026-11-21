"""Soi video doi thu: thong ke canh + luoi khung + hook 60s. Chay trong GitHub Actions."""
import argparse, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from live_common import sh, tai_video, probe, transcribe

ap = argparse.ArgumentParser()
ap.add_argument("--url", default=""); ap.add_argument("--release_asset", default="")
a = ap.parse_args()
src, vid = tai_video(a.url, a.release_asset, cao=480)
open("vid.txt", "w").write(vid)
w, h, dur = probe(src)
# scene detect
p = subprocess.run(["ffmpeg", "-hide_banner", "-i", src, "-vf", "select='gt(scene,0.3)',metadata=print:file=-", "-an", "-f", "null", "-"],
                   capture_output=True, text=True)
cuts = sorted(float(x) for x in re.findall(r"pts_time:([\d.]+)", p.stdout + p.stderr))
bounds = [0.0] + [c for c in cuts if 0 < c < dur] + [dur]
n = len(bounds) - 1
tb = dur / n if n else 0
n15 = sum(1 for c in cuts if c <= 15) + 1
# luoi 12 khung
os.makedirs("out", exist_ok=True)
sh(["ffmpeg", "-y", "-v", "error", "-i", src, "-vf",
    f"fps=12/{dur:.2f},scale=320:-2,tile=4x3:padding=4:color=black", "-frames:v", "1", f"out/{vid}_luoi.jpg"])
# hook
sh(["ffmpeg", "-y", "-v", "error", "-i", src, "-t", "60", "-vn", "-ac", "1", "-ar", "16000", "a.wav"])
segs = transcribe("a.wav", "small")
hook = "\n".join(f"- [{s['start']:.0f}s] {s['text']}" for s in segs)
md = f"""# Soi video {vid}
Link: {a.url or a.release_asset}
Khung: {w}x{h}

| Chi so | Gia tri |
|---|---|
| Tong thoi luong | {dur:.0f}s ({dur/60:.1f} phut) |
| So canh (nguong 0.3) | {n} |
| Do dai TB moi canh | {tb:.1f}s |
| So canh trong 15s dau | {n15} |
| Canh / phut | {n/(dur/60):.1f} |

Luoi 12 khung: release `soi-{vid}` (file `{vid}_luoi.jpg`)

## Hook (60s dau)
{hook}
"""
os.makedirs("_kiem/soi", exist_ok=True)
open(f"_kiem/soi/{vid}.md", "w", encoding="utf8").write(md)
print(md)
