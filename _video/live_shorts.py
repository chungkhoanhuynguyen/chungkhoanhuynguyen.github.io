"""Live/video YouTube -> N clip doc 1080x1920 (cat lang, phu de burn-in, loudnorm). Chay trong GitHub Actions."""
import argparse, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from live_common import sh, tai_video, probe, transcribe

KW = ["giảm", "tăng", "lãi", "lỗ", "vàng", "lãi suất", "bán", "mua", "sập", "đỉnh", "đáy", "cảnh báo", "vn-index", "vnindex", "khủng hoảng", "nên", "đừng", "bí mật", "sai lầm"]

def diem_cau(t):
    t0 = t.lower(); d = 0
    if re.search(r"\d", t0): d += 2
    if "?" in t0 or re.match(r"^(tại sao|vì sao|làm sao|liệu|có nên|bao giờ|khi nào|điều gì|ai)\b", t0): d += 2
    d += min(3, sum(1 for k in KW if k in t0))
    return d

def chon_doan(segs, n, tmin=30, tmax=60):
    cands = []
    for i, s in enumerate(segs):
        st = s["start"]; j = i
        while j + 1 < len(segs) and segs[j + 1]["end"] - st <= tmax - 2 and segs[j]["end"] - st < tmin:
            j += 1
        # mo rong toi thieu tmin
        while j + 1 < len(segs) and segs[j]["end"] - st < tmin and segs[j + 1]["end"] - st <= tmax:
            j += 1
        dur = segs[j]["end"] - st
        if dur < tmin or dur > tmax: continue
        txt = " ".join(x["text"] for x in segs[i:j + 1])
        sc = diem_cau(s["text"]) * 3 + sum(diem_cau(x["text"]) for x in segs[i + 1:j + 1]) * 0.5
        cands.append((sc, st, segs[j]["end"], i, j, txt))
    cands.sort(reverse=True)
    pick = []
    for c in cands:
        if all(c[2] <= p[1] or c[1] >= p[2] for p in pick):
            pick.append(c)
        if len(pick) >= n: break
    return sorted(pick, key=lambda c: c[1])

def ts(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def ass(path, words, t0):
    """words: list {s,e,t}. Chia cum ~7 tu, 2 dong."""
    hdr = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\n\n[V4+ Styles]\n"
           "Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding\n"
           "Style: D,DejaVu Sans,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,6,0,2,50,50,430,1\n\n"
           "[Events]\nFormat: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text\n")
    ev = []; i = 0
    while i < len(words):
        ch = words[i:i + 6]; i += 6
        if len(ch) == 1 and ev and False: pass
        a = max(0, ch[0]["s"] - t0); b = max(a + 0.3, ch[-1]["e"] - t0)
        k = (len(ch) + 1) // 2
        l1 = " ".join(w["t"] for w in ch[:k]); l2 = " ".join(w["t"] for w in ch[k:])
        txt = l1 + (r"\N" + l2 if l2 else "")
        ev.append(f"Dialogue: 0,{ts(a)},{ts(b)},D,,0,0,0,,{txt}")
    open(path, "w", encoding="utf8").write(hdr + "\n".join(ev) + "\n")

def render(src, st, en, assf, out):
    w, h, _ = probe(src)
    if h >= w * 1.2:  # da doc: giu ty le, chi scale
        vf = ("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5[bg];"
              "[b]scale=1080:1920:force_original_aspect_ratio=decrease[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,")
    else:  # ngang: crop giua 3:4, nen mo
        vf = ("[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:5[bg];"
              "[b]crop='min(iw,ih*3/4)':ih,scale=1080:1440[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2-80,")
    vf += f"ass={assf}[v]"
    sh(["ffmpeg", "-y", "-v", "error", "-ss", f"{st:.2f}", "-to", f"{en:.2f}", "-i", src,
        "-filter_complex", vf, "-map", "[v]", "-map", "0:a:0", "-af", "loudnorm=I=-13:TP=-1.5:LRA=11",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
        "-r", "30", "-movflags", "+faststart", out])

def tieu_de(txt):
    s = re.split(r"(?<=[.?!])\s", txt.strip())[0]
    return s if len(s) <= 60 else s[:57].rsplit(" ", 1)[0] + "..."

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=""); ap.add_argument("--so_clip", type=int, default=5)
    ap.add_argument("--release_asset", default=""); ap.add_argument("--max_phut", type=float, default=45)
    a = ap.parse_args()
    src, vid = tai_video(a.url, a.release_asset)
    open("vid.txt", "w").write(vid)
    w, h, dur = probe(src)
    print("video", w, h, dur)
    cut = "cut.mp4"
    r = subprocess.run(["auto-editor", src, "--margin", "0.2sec", "--edit", "audio:threshold=4%", "-o", cut, "--no-open"])
    if r.returncode != 0 or not os.path.exists(cut):
        print("auto-editor loi -> dung ban goc"); cut = src
    if probe(cut)[2] > a.max_phut * 60:
        sh(["ffmpeg", "-y", "-v", "error", "-i", cut, "-t", str(int(a.max_phut * 60)), "-c", "copy", "cut2.mp4"]); cut = "cut2.mp4"
    print("sau cat lang", probe(cut)[2])
    sh(["ffmpeg", "-y", "-v", "error", "-i", cut, "-vn", "-ac", "1", "-ar", "16000", "a.wav"])
    segs = transcribe("a.wav", "small", words=True)
    print("so cau", len(segs))
    pick = chon_doan(segs, a.so_clip)
    os.makedirs("out", exist_ok=True)
    for n, (sc, st, en, i, j, txt) in enumerate(pick, 1):
        words = [w for s in segs[i:j + 1] for w in s["words"]]
        if not words:
            words = [{"s": s["start"], "e": s["end"], "t": s["text"]} for s in segs[i:j + 1]]
        ass(f"c{n}.ass", words, st)
        render(cut, st, en, f"c{n}.ass", f"out/clip_{n}.mp4")
        open(f"out/clip_{n}.txt", "w", encoding="utf8").write(
            f"TIEU DE: {tieu_de(segs[i]['text'])}\nDIEM: {sc:.1f}  ({st:.0f}s-{en:.0f}s)\n\n{txt}\n")
    print("XONG", len(pick), "clip")
    if not pick: sys.exit(4)

main()
