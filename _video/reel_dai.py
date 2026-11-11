# -*- coding: utf-8 -*-
"""QL1 11/11 – REEL DỌC 2–3 PHÚT từ video dài, khuôn học từ trang 'Tổ Buôn Chứng Khoán' (reel 28K–228K view):
  - Toàn khung 9:16 nền tím thương hiệu, CÂU HỎI TO đứng yên suốt video (dòng 2 trong ô vàng, có '???'),
  - Hình video dài ở giữa (cắt bỏ dải phụ đề nhỏ gốc), PHỤ ĐỀ TO giữa-dưới (2 dòng, chữ trắng viền đen, đọc được khi tắt tiếng),
  - Dài 90–180 giây (thời gian xem cao hơn Shorts 55s), cắt đúng cuối câu theo .srt.
Dùng: python3 reel_dai.py video.mp4 video.srt out.mp4 BAT_DAU "DÒNG 1|DÒNG 2???" [DAI_TOI_DA=175] [DAI_TOI_THIEU=90]
"""
import os, re, subprocess, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "engine"))
os.environ.setdefault("HN_PX", os.path.join(HERE, "queue", "20261110_2300_vt", "px_tuan.json")); import dx2
import cat_short

def _t(s):
    h, m, x, ms = re.match(r"(\d+):(\d+):(\d+),(\d+)", s).groups(); return int(h) * 3600 + int(m) * 60 + int(x) + int(ms) / 1000
def _ass_t(v):
    v = max(0, v); h = int(v // 3600); m = int(v % 3600 // 60); s = v % 60
    return "%d:%02d:%05.2f" % (h, m, s)

def ass(srt, a, d, out):
    tx = open(srt, encoding="utf-8").read()
    cue = re.findall(r"(\d\d:\d\d:\d\d,\d+) --> (\d\d:\d\d:\d\d,\d+)\n(.+?)(?:\n\n|\Z)", tx, re.S)
    L = ["[Script Info]", "ScriptType: v4.00+", "PlayResX: 1080", "PlayResY: 1920", "WrapStyle: 0", "",
         "[V4+ Styles]",
         "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
         "Style: P,Be Vietnam Pro ExtraBold,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,5,2,8,60,60,1180,1",
         "", "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for s, e, t in cue:
        s, e = _t(s) - a, _t(e) - a
        if e <= 0 or s >= d: continue
        t = t.strip().replace("\n", " ")
        L.append("Dialogue: 0,%s,%s,P,,0,0,0,,%s" % (_ass_t(s), _ass_t(min(e, d)), t))
    open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")

def nen(hook, out):
    """Nền 1080x1920: tím đậm chuyển sắc + logo + câu hỏi to cố định + dòng kêu gọi xem full."""
    im = Image.new("RGB", (1080, 1920)); px = im.load()
    for y in range(1920):
        k = y / 1919
        c = (int(46 + 30 * k), int(16 + 8 * k), int(82 + 40 * (1 - abs(0.5 - k) * 2)))
        for x in range(1080): px[x, y] = c
    d = ImageDraw.Draw(im)
    f0 = dx2.F("Black", 34); w = d.textlength("HUY NGUYỄN", font=f0)
    d.rounded_rectangle([540 - w / 2 - 18, 120, 540 + w / 2 + 18, 172], 10, fill=(124, 58, 237)); d.text((540, 146), "HUY NGUYỄN", font=f0, fill=(255, 255, 255), anchor="mm")
    dong = [x.strip() for x in hook.split("|") if x.strip()]; y = 230
    for i, s in enumerate(dong):
        f = dx2.fit(d, s, "Black", 960, 92 if i else 78)
        w = d.textlength(s, font=f); h = f.size + 30
        if i == len(dong) - 1:
            d.rounded_rectangle([540 - w / 2 - 26, y - 4, 540 + w / 2 + 26, y + h], 16, fill=(255, 196, 0))
            d.text((540, y + h / 2 - 2), s, font=f, fill=(24, 12, 40), anchor="mm")
        else:
            d.text((540, y + h / 2 - 2), s, font=f, fill=(255, 255, 255), anchor="mm", stroke_width=4, stroke_fill=(20, 8, 40))
        y += h + 16
    f2 = dx2.F("Bold", 36)
    d.text((540, 1780), "Xem bản đầy đủ: YouTube Chứng Khoán Huy Nguyễn", font=f2, fill=(255, 255, 255), anchor="mm")
    d.text((540, 1830), "Chia sẻ góc nhìn, không phải khuyến nghị mua bán", font=dx2.F("Bold", 26), fill=(200, 190, 230), anchor="mm")
    im.save(out)

def cat(src, srt, out, a, hook, dmax=175.0, dmin=90.0):
    os.environ["SRT"] = srt
    a = max(0.0, cat_short.bat_dau_cau(src, a))
    d = cat_short.ngat(src, a, dmax, dmin)
    png = out + ".nen.png"; sub = out + ".ass"
    nen(hook, png); ass(srt, a, d, sub)
    # video dài 16:9 -> bỏ 14% đáy (dải phụ đề nhỏ gốc) -> rộng 1080, đặt ở y=530
    fc = ("[1:v]crop=iw:ih*0.86:0:0,scale=1080:-2[v];[0:v][v]overlay=0:530[b];"
          "[b]subtitles='%s'[o]" % sub.replace("'", r"\'"))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", png, "-ss", str(a), "-t", "%.2f" % d, "-i", src,
                    "-filter_complex", fc, "-map", "[o]", "-map", "1:a", "-af", "afade=t=out:st=%.2f:d=0.5" % (d - 0.5), "-t", "%.2f" % d,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-c:a", "aac", "-b:a", "160k", "-r", "30", "-pix_fmt", "yuv420p", out], check=True)
    os.remove(png); os.remove(sub); return a, d

if __name__ == "__main__":
    src, srt, out, a, hook = sys.argv[1:6]
    dm = float(sys.argv[6]) if len(sys.argv) > 6 else 175; dn = float(sys.argv[7]) if len(sys.argv) > 7 else 90
    print(out, cat(src, srt, out, float(a), hook, dm, dn))
