import subprocess, os, sys, json, glob, shutil

def sh(cmd, check=True):
    print("+", " ".join(cmd) if isinstance(cmd, list) else cmd, flush=True)
    return subprocess.run(cmd, check=check)

def tai_video(url, release_asset, out="src.mp4", cao=720):
    tag = os.environ.get("RELEASE_TAG") or "nguon-video"
    """Tai video: release_asset (asset mp4 trong release nguon-video) hoac yt-dlp. Tra ve (path, id)."""
    if release_asset:
        sh(["gh", "release", "download", tag, "-p", release_asset, "-O", out, "--clobber"])
        return out, os.path.splitext(os.path.basename(release_asset))[0]
    vid = subprocess.run(["yt-dlp", "--get-id", "--no-playlist", url], capture_output=True, text=True).stdout.strip().split("\n")[0]
    fmt = f"bv*[height<={cao}]+ba/b[height<={cao}]/b"
    base = ["yt-dlp", "--no-playlist", "-f", fmt, "--merge-output-format", "mp4", "-o", out,
            "--js-runtimes", "node", "--remote-components", "ejs:github"]
    r = subprocess.run(base + [url])
    if r.returncode != 0:
        # thu lai khong co tuy chon moi
        r = subprocess.run(["yt-dlp", "--no-playlist", "-f", fmt, "--merge-output-format", "mp4", "-o", out, url])
    if r.returncode != 0 or not os.path.exists(out):
        print("LOI_TAI: YouTube co the chan IP GitHub (bot check). Dung input release_asset (mp4 upload san vao release 'nguon-video').")
        sys.exit(3)
    return out, vid or "video"

def probe(path):
    j = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v:0",
        "-show_entries", "stream=width,height:format=duration", "-of", "json", path]))
    s = j["streams"][0]
    return int(s["width"]), int(s["height"]), float(j["format"]["duration"])

def transcribe(path, model="small", words=False):
    from faster_whisper import WhisperModel
    m = WhisperModel(model, device="cpu", compute_type="int8")
    segs, _ = m.transcribe(path, language="vi", vad_filter=True, word_timestamps=words, beam_size=1)
    out = []
    for s in segs:
        d = {"start": s.start, "end": s.end, "text": s.text.strip()}
        if words:
            d["words"] = [{"s": w.start, "e": w.end, "t": w.word.strip()} for w in (s.words or [])]
        out.append(d)
    return out
