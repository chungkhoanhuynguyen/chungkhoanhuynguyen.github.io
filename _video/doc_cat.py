# Cắt video dài NGANG (đã dựng) thành 2–3 clip DỌC 1080x1920 cho TikTok/Reel/Shorts phụ.
# Dùng: python _video/doc_cat.py <thư_mục_vào> <KEY> "<tiêu đề video>"
#   thư mục vào có KEY.mp4, KEY.srt, KEY_chuong.txt  -> ra _video/out/KEY_d1.mp4, _d2, _d3 + KEY_d.json (hook từng clip)
# Khung: nền là chính video phóng to + mờ, video gốc giữa khung, tiêu đề 2 dòng to phía trên, phụ đề to phía dưới.
import sys, os, re, json, subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); FD = os.path.join(HERE, "engine", "fonts")
W, H = 1080, 1920
VANG = (255, 214, 64); TRANG = (255, 255, 255)

def F(n, s): return ImageFont.truetype(os.path.join(FD, f"BeVietnamPro-{n}.ttf"), s)

def ts(s):
    p = [float(x) for x in s.split(":")]; v = 0
    for x in p: v = v * 60 + x
    return v

def srt(path):
    out = []
    for b in re.split(r"\n\s*\n", open(path, encoding="utf-8").read().strip()):
        L = b.strip().splitlines()
        if len(L) < 3: continue
        a, c = L[1].split(" --> ")
        f = lambda x: ts(x.replace(",", "."))
        out.append((f(a), f(c), " ".join(L[2:]).strip()))
    return out

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout.strip())

def cut_at(cues, t):  # mốc kết thúc câu gần nhất <= t
    e = [c[1] for c in cues if c[1] <= t + 0.05]
    return e[-1] if e else t

def wrap(d, s, f, mw):
    w = s.split(); L = []; cur = ""
    for x in w:
        t = (cur + " " + x).strip()
        if d.textlength(t, font=f) <= mw: cur = t
        else: L.append(cur); cur = x
    if cur: L.append(cur)
    return L

def top_png(l1, l2, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 470], fill=(8, 10, 18, 215))
    f1 = F("Black", 78); L1 = wrap(d, l1.upper(), f1, W - 100)
    while len(L1) > 2 and f1.size > 54: f1 = F("Black", f1.size - 6); L1 = wrap(d, l1.upper(), f1, W - 100)
    y = 120
    for s in L1[:3]:
        d.text((W / 2, y), s, font=f1, fill=VANG, anchor="ma", stroke_width=3, stroke_fill=(0, 0, 0)); y += f1.size + 14
    if l2:
        f2 = F("Bold", 40)
        for s in wrap(d, l2, f2, W - 140)[:2]:
            d.text((W / 2, y + 10), s, font=f2, fill=TRANG, anchor="ma"); y += 52
    fb = F("ExtraBold", 34); d.text((W / 2, 52), "HUY NGUYỄN · CÂU CHUYỆN ĐẦU TƯ", font=fb, fill=(196, 140, 255), anchor="ma")
    d.rectangle([0, H - 140, W, H], fill=(8, 10, 18, 200))
    d.text((W / 2, H - 100), "Xem đủ câu chuyện ở kênh chính Chứng Khoán Huy Nguyễn", font=F("SemiBold", 32), fill=KEM, anchor="ma")
    im.save(path)
KEM = (242, 234, 216)

def ass(cues, a, b, path):
    hd = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
          "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
          "Style: D,Be Vietnam Pro,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,-1,0,0,0,100,100,0,0,1,5,2,8,70,70,1240,1\n\n"
          "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    def t(x):
        x = max(0, x); h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
        return f"{h}:{m:02d}:{s:05.2f}"
    ev = []
    for s, e, tx in cues:
        if e <= a or s >= b: continue
        ev.append(f"Dialogue: 0,{t(s - a)},{t(min(e, b) - a)},D,,0,0,0,,{tx}")
    open(path, "w", encoding="utf-8").write(hd + "\n".join(ev) + "\n")

def clip(src, a, b, l1, l2, out, cues):
    tp = out + "_top.png"; top_png(l1, l2, tp)
    ap = out + ".ass"; ass(cues, a, b, ap)
    fc = (f"[0:v]split[a][b];[a]scale=-2:{H},crop={W}:{H},boxblur=30:2,eq=brightness=-0.25[bg];"
          f"[b]scale={W}:-2[fg];[bg][fg]overlay=0:520[v1];[v1][1:v]overlay=0:0[v2];"
          f"[v2]subtitles={ap}:fontsdir={FD}[v]")
    af = f"afade=t=in:d=0.3,afade=t=out:st={max(0, b - a - 0.6):.2f}:d=0.6"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{a:.2f}", "-t", f"{b - a:.2f}", "-i", src, "-i", tp,
                    "-filter_complex", fc, "-map", "[v]", "-map", "0:a", "-af", af,
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-r", "30",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", out], check=True)
    for p in (tp, ap): os.remove(p)

def main(d, key, title):
    src = os.path.join(d, key + ".mp4"); cues = srt(os.path.join(d, key + ".srt")); T = dur(src)
    ch = []
    for l in open(os.path.join(d, key + "_chuong.txt"), encoding="utf-8"):
        m = re.match(r"(\d+:\d\d(?::\d\d)?)\s+(.*)", l.strip())
        if m: ch.append((ts(m.group(1)), m.group(2).strip()))
    ch.append((T, "")); seg = []
    def span(i, lo=38, hi=72):
        a = ch[i][0]; j = i + 1
        while j < len(ch) - 1 and ch[j][0] - a < lo: j += 1
        b = min(ch[j][0], a + hi); b = cut_at(cues, b) if b < T - 0.5 else T
        return a, max(b, a + 15)
    clean = lambda s: re.sub(r"^(Chương \d+\s*[–-]\s*|Mở đầu:\s*|Tổng kết:?\s*)", "", s).strip()
    a, b = span(0); seg.append((a, b, title, ""))
    n = len(ch) - 1
    if n >= 4:
        i = n // 2; a, b = span(i); seg.append((a, b, clean(ch[i][1]) or title, title))
    if n >= 3:
        i = n - 1
        while i > 1 and ch[n][0] - ch[i][0] < 35: i -= 1
        a, b = ch[i][0], T - 0.3
        if b - a > 75: b = cut_at(cues, a + 72)
        seg.append((a, b, clean(ch[i][1]) or "Bài học rút ra", title))
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True); meta = []
    for k, (a, b, l1, l2) in enumerate(seg, 1):
        o = os.path.join(HERE, "out", f"{key}_d{k}.mp4"); clip(src, a, b, l1, l2, o, cues)
        meta.append({"file": os.path.basename(o), "tu": round(a, 1), "den": round(b, 1), "hook": l1, "video": title})
        print(o, round(b - a, 1))
    json.dump(meta, open(os.path.join(HERE, "out", key + "_d.json"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
