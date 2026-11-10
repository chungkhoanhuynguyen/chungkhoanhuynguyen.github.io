# -*- coding: utf-8 -*-
"""QL1 11/11 – Cắt Shorts/Reels dọc 1080x1920 từ video dài (anh Huy: 'video short cứ cắt từ video dài').
Cách dùng: python3 cat_short.py video.mp4 out.mp4 BAT_DAU DAI_TOI_DA "DÒNG 1|DÒNG 2" "Xem full: ..."
- Tự tìm chỗ ngắt lặng gần cuối (không cắt giữa câu), tối đa 58 giây.
- Nền là chính video phóng to làm mờ, video gốc nằm giữa, chữ hook to phía trên, lời mời xem full phía dưới.
"""
import os, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "engine"))
os.environ.setdefault("HN_PX", os.path.join(HERE, "queue", "20261110_2300_vt", "px_tuan.json")); import dx2

def _lang(src, a, d):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-ss", str(a), "-t", str(d), "-i", src, "-af", "highpass=f=200,lowpass=f=3500,silencedetect=n=-28dB:d=0.4", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]

def ngat_cau(srt, a, dmax=58.0, dmin=30.0):
    """Cắt đúng cuối câu theo phụ đề .srt của video dài; ưu tiên câu hỏi ở 18 giây cuối để người xem tò mò bấm xem full."""
    tx = open(srt, encoding="utf-8").read()
    cue = re.findall(r"\d\d:\d\d:\d\d,\d+ --> (\d\d):(\d\d):(\d\d),(\d+)\n(.+?)(?:\n\n|\Z)", tx, re.S)
    seg = [(int(h) * 3600 + int(m) * 60 + int(x) + int(ms) / 1000 - a, t.strip().replace("\n", " ")) for h, m, x, ms, t in cue]
    ok = [(e, t) for e, t in seg if dmin <= e <= dmax - 0.3 and re.search(r"[.?!…]$", t)]
    if not ok: return None
    hoi = [(e, t) for e, t in ok if t.endswith("?") and e >= dmax - 18]
    e, t = (hoi or ok)[-1]; print("cat sau cau:", t, flush=True); return e + 0.35

def ngat(src, a, dmax=58.0, dmin=30.0):
    try:
        srt = os.environ.get("SRT") or os.path.splitext(src)[0] + ".srt"
        e = ngat_cau(srt, a, dmax, dmin) if os.path.exists(srt) else None
        if e: return e
    except Exception as ex: print("srt bo qua:", ex, flush=True)
    st = [t for t in _lang(src, a, dmax) if dmin <= t <= dmax - 0.3]
    return (st[-1] + 0.25) if st else dmax

def lop(hook, cta, out):
    im = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    dong = [x.strip() for x in hook.split("|") if x.strip()]
    y = 250
    for i, s in enumerate(dong):
        f = dx2.fit(d, s, "Black", 980, 92)
        w = d.textlength(s, font=f); h = f.size + 26
        if i == 1:
            d.rounded_rectangle([540 - w / 2 - 24, y - 6, 540 + w / 2 + 24, y + h - 4], 14, fill=(255, 196, 0, 255))
            d.text((540, y + h / 2 - 4), s, font=f, fill=(18, 18, 24), anchor="mm")
        else:
            d.text((540, y + h / 2 - 4), s, font=f, fill=(255, 255, 255), anchor="mm", stroke_width=6, stroke_fill=(0, 0, 0))
        y += h + 18
    f2 = dx2.fit(d, cta, "Bold", 900, 44)
    w = d.textlength(cta, font=f2)
    d.rounded_rectangle([540 - w / 2 - 30, 1500, 540 + w / 2 + 30, 1590], 45, fill=(225, 38, 38, 255))
    d.text((540, 1545), cta, font=f2, fill=(255, 255, 255), anchor="mm")
    d.text((540, 1650), "Huy Nguyễn Chứng Khoán", font=dx2.F("Bold", 34), fill=(255, 255, 255, 220), anchor="mm")
    im.save(out)

def cat(src, out, a, dmax, hook, cta):
    d = ngat(src, a, dmax, float(os.environ.get("DMIN", 30))); png = out + ".png"; lop(hook, cta, png)
    fc = ("[0:v]split=2[b][f];[b]scale=-2:1920,crop=1080:1920,boxblur=28:2,eq=brightness=-0.18[bg];"
          "[f]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2+40[v1];[v1][1:v]overlay=0:0,format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(a), "-t", "%.2f" % d, "-i", src, "-i", png,
                    "-filter_complex", fc, "-map", "[v]", "-map", "0:a", "-af", "afade=t=out:st=%.2f:d=0.4" % (d - 0.4),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-r", "30", out], check=True)
    os.remove(png); return d

if __name__ == "__main__":
    src, out, a, dm, hook, cta = sys.argv[1:7]
    print(out, "%.1fs" % cat(src, out, float(a), float(dm), hook, cta))
