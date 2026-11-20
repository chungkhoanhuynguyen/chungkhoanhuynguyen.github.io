# Cảnh 3D kể chuyện cho video dài (render.py, 'k': '3d') – 20/11/2026.
# prep(sc, n, FPS): dựng đoạn 3D bằng xưởng anim3d (Remotion, composition "Canh3D", cờ chiTiet) đúng n khung của câu đọc,
#   dựng thưa ở CANH3D_FPS (mặc định 10) rồi nội suy lên FPS video; có KHO theo mã băm (nội dung cảnh + mã nguồn xưởng) ở CANH3D_CACHE.
# frame(sc, t): khung 1920x1080 của cảnh tại thời điểm t + thẻ nhãn/số liệu góc trên trái (cap, label).
# Cảnh 3D: {'k': '3d', 'set': 'sapvai'|'phongkhach'|'vanphong'|'nganhang'|'cafevh'|'suaxe2'|'showroom2'|'phoxe2',
#           'cam': [[x,y,z],[nhìn x,y,z],fov] hoặc {'from': [...], 'to': [...]}, 'cast': [{'a': khoá nhân vật, 'p': [x,y,z], 'act': ..., 'side': ±1, 'ngoi': True, 'to': [...]}],
#           'light': 'day' (mặc định, sáng)|'golden'|'room'|..., 'cap': (...), 'label': ..., 'say': ...}
import os, json, hashlib, subprocess, math
try: from PIL import Image, ImageDraw
except ImportError: Image = ImageDraw = None   # máy r3d chỉ dựng khúc khung, không cần PIL
HERE = os.path.dirname(os.path.abspath(__file__)); A3 = os.path.join(HERE, "anim3d")
LW, LH = 1920, 1080
FPS3 = int(os.environ.get("CANH3D_FPS", "10")); SCALE = float(os.environ.get("CANH3D_SCALE", "1"))
# PX: độ phân giải trong của cảnh (0.5 = 960x540 rồi phóng lên, nhanh ~2x); TAT: tắt hiệu ứng nặng, vd "ink,bloom" (mặc định giữ đủ nét mực)
PX = float(os.environ.get("CANH3D_PX", "0.5")); TAT = [x for x in os.environ.get("CANH3D_TAT", "").split(",") if x]
CACHE = os.environ.get("CANH3D_CACHE", os.path.join(HERE, "out", "cache3d")); os.makedirs(CACHE, exist_ok=True)
BUNDLE = os.environ.get("CANH3D_BUNDLE", "/tmp/canh3d_bundle")
_SRC = [None]
def _src_hash():
    """mã băm mã nguồn xưởng dùng cho cảnh 3D (sửa xưởng → dựng lại; không sửa → lấy kho)."""
    if _SRC[0]: return _SRC[0]
    h = hashlib.sha1()
    for d in ("src", "public/chitiet", "public/xe", "public/suaxe2"):
        for root, _, fs in sorted(os.walk(os.path.join(A3, d))):
            for f in sorted(fs):
                p = os.path.join(root, f); h.update(p[len(A3):].encode()); h.update(open(p, "rb").read())
    for f in ("package.json", "canh3d_render.mjs"): h.update(open(os.path.join(A3, f), "rb").read())
    _SRC[0] = h.hexdigest()[:16]; return _SRC[0]
def _props(sc, n3):
    cam = sc.get("cam") or [[0, 1.5, 4.2], [0, 1.0, -1.0], 40]
    if isinstance(cam, list): cam = {"from": cam}
    return {"set": sc.get("set", "sapvai"), "light": sc.get("light", "day"), "cam": cam, "cast": sc.get("cast", []), "frames": int(n3), "fps": FPS3, "px": PX, "tat": TAT}
def plan(sc, n, FPS):
    """(mã băm, props, đường dẫn mp4 trong kho) của cảnh 3D dài n khung ở FPS video."""
    n3 = max(2, int(math.ceil(n * FPS3 / FPS)) + 1); pr = _props(sc, n3)
    hk = hashlib.sha1((json.dumps(pr, sort_keys=True, ensure_ascii=False) + _src_hash() + "s%.2f" % SCALE).encode()).hexdigest()[:20]
    return hk, pr, os.path.join(CACHE, "c3_%s.mp4" % hk)
def _ghep(hk, n3, mp4):
    """nối các khúc c3_<hk>.p<a>-<b>.mp4 do các máy r3d dựng song song (đủ liền 0..n3-1) thành mp4 của cảnh."""
    import glob, re
    ps = []
    for f in glob.glob(os.path.join(CACHE, "c3_%s.p*.mp4" % hk)):
        m = re.search(r"\.p(\d+)-(\d+)\.mp4$", f)
        if m: ps.append((int(m.group(1)), int(m.group(2)), f))
    ps.sort(); k = 0
    for a, b, _ in ps:
        if a != k: return False
        k = b + 1
    if not ps or k != n3: return False
    lst = mp4 + ".txt"; open(lst, "w").write("".join("file '%s'\n" % f for _, _, f in ps))
    r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", mp4 + ".tmp.mp4"])
    if r.returncode != 0: return False
    os.replace(mp4 + ".tmp.mp4", mp4); print("canh 3d ghep", hk, len(ps), "khuc", flush=True); return True
def _dung(pr, out, rng=None):
    pj = "/tmp/c3_%d_%s.json" % (os.getpid(), os.path.basename(out)); json.dump(pr, open(pj, "w"), ensure_ascii=False)
    env = dict(os.environ, CANH3D_BUNDLE=BUNDLE)
    if rng: env["CANH3D_RANGE"] = "%d-%d" % rng
    return subprocess.run(["node", "canh3d_render.mjs", pj, out, str(SCALE)], cwd=A3, env=env, capture_output=True, text=True)
def prep(sc, n, FPS, key="", i=0):
    hk, pr, mp4 = plan(sc, n, FPS); n3 = pr["frames"]
    if not os.path.exists(mp4): _ghep(hk, n3, mp4)
    if not os.path.exists(mp4):
        r = _dung(pr, mp4 + ".tmp.mp4")
        print(key, "canh 3d", i, pr["set"], n3, "khung:", (r.stdout.strip().splitlines() or ["?"])[-1], flush=True)
        if r.returncode != 0 or not os.path.exists(mp4 + ".tmp.mp4"): print(r.stderr[-1500:], flush=True); raise RuntimeError("canh 3d loi: %s" % pr["set"])
        os.replace(mp4 + ".tmp.mp4", mp4)
    else: print(key, "canh 3d", i, "lay tu kho", hk, flush=True)
    sc["_r3mp4"] = mp4; sc["_r3n"] = n; sc["_r3fps"] = FPS; sc["_r3rd"] = None
class _Doc:
    """đọc tuần tự khung đã nội suy (không giữ cả cảnh trong RAM: 25 giây 1080p = 4,6 GB)."""
    def __init__(s, mp4, n, FPS):
        s.p = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", mp4, "-vf", "minterpolate=fps=%d:mi_mode=blend,scale=%d:%d:flags=bicubic" % (FPS, LW, LH),
                                "-frames:v", str(n), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE); s.k = -1; s.last = None
    def get(s, k):
        while s.k < k:
            b = s.p.stdout.read(LW * LH * 3)
            if len(b) < LW * LH * 3: break
            s.last = b; s.k += 1
        return Image.frombytes("RGB", (LW, LH), s.last) if s.last else Image.new("RGB", (LW, LH), (10, 12, 17))
    def close(s):
        try: s.p.stdout.close(); s.p.kill()
        except Exception: pass
def _the(im, sc, t):
    """thẻ nhãn + số liệu góc trên trái (giữ thông tin như cảnh thẻ cũ)."""
    import dx2
    cap = [c for c in (sc.get("cap") or []) if c]; lab = sc.get("label") or ""
    if not cap and not lab: return
    a = dx2.ease(min(1.0, max(0.0, (t - 0.3) / 0.45)))
    if a <= 0: return
    d = ImageDraw.Draw(im, "RGBA"); x0, y0 = 46, 70; fl = dx2.F("Bold", 26); fc = [dx2.F("Black", 54), dx2.F("Black", 44)]
    w = max([d.textlength(lab, font=fl)] + [d.textlength(c, font=fc[min(j, 1)]) for j, c in enumerate(cap)]) + 56
    h = (40 if lab else 0) + sum(int(fc[min(j, 1)].size * 1.22) for j in range(len(cap))) + 30
    dx = int((1 - a) * -60)
    d.rounded_rectangle([x0 + dx, y0, x0 + dx + w, y0 + h], 20, fill=(8, 10, 15, int(200 * a))); d.rectangle([x0 + dx, y0, x0 + dx + 8, y0 + h], fill=(255, 196, 0, int(255 * a)))
    y = y0 + 16
    if lab: d.text((x0 + dx + 28, y), lab, font=fl, fill=(255, 196, 0, int(255 * a))); y += 40
    cols = sc.get("cols") or [(255, 255, 255), (255, 196, 0)]
    for j, c in enumerate(cap):
        f = fc[min(j, 1)]; col = tuple(cols[j]) if j < len(cols) else (255, 255, 255)
        d.text((x0 + dx + 28, y), c, font=f, fill=col + (int(255 * a),), stroke_width=2, stroke_fill=(0, 0, 0, int(200 * a))); y += int(f.size * 1.22)
def frame(sc, t):
    if not sc.get("_r3mp4"): return Image.new("RGB", (LW, LH), (10, 12, 17))
    k = min(sc["_r3n"] - 1, int(round(t * sc["_r3fps"])))
    rd = sc.get("_r3rd")
    if rd is None or k < rd.k:
        if rd: rd.close()
        rd = sc["_r3rd"] = _Doc(sc["_r3mp4"], sc["_r3n"], sc["_r3fps"])
    im = rd.get(k)
    if k >= sc["_r3n"] - 1: rd.close()
    _the(im, sc, t); return im

def chia(jobs, ns):
    """chia đều KHUNG của mọi cảnh cần dựng cho ns máy: -> [[(job, a, b), ...] cho từng máy] (khúc liền, a..b gồm cả b)."""
    tot = sum(j["props"]["frames"] for j in jobs); out = [[] for _ in range(ns)]; g0 = 0
    for j in jobs:
        n3 = j["props"]["frames"]; a = 0
        while a < n3:
            s_ = max(k for k in range(ns) if k * tot // ns <= g0 + a); end_s = (s_ + 1) * tot // ns   # khung toàn cục cuối (không gồm) của máy s_
            b = min(n3, max(a + 1, end_s - g0)); out[s_].append((j, a, b - 1)); a = b
        g0 += n3
    return out
if __name__ == "__main__" and len(__import__("sys").argv) > 1 and __import__("sys").argv[1] == "dung":
    # python _video/r3d.py dung <máy thứ> <số máy> <j3d.json ...>: dựng phần khung của máy này vào CACHE (c3_<hk>.p<a>-<b>.mp4)
    import sys, time
    me, ns = int(sys.argv[2]), int(sys.argv[3]); jobs = []
    for f in sys.argv[4:]: jobs += json.load(open(f))
    seen = set(); jobs = [j for j in jobs if not (j["hk"] in seen or seen.add(j["hk"]))]
    mine = chia(jobs, ns)[me]; print("may", me, "/", ns, ":", [(j["hk"][:8], a, b) for j, a, b in mine], flush=True)
    for j, a, b in mine:
        out = os.path.join(CACHE, "c3_%s.p%05d-%05d.mp4" % (j["hk"], a, b)); t0 = time.time()
        if os.path.exists(out): continue
        r = _dung(j["props"], out + ".tmp.mp4", (a, b))
        print(j.get("key"), "canh", j.get("i"), j["props"]["set"], a, b, "%.0fs" % (time.time() - t0), (r.stdout.strip().splitlines() or ["?"])[-1], flush=True)
        if r.returncode != 0 or not os.path.exists(out + ".tmp.mp4"): print(r.stderr[-2000:], flush=True); sys.exit(1)
        os.replace(out + ".tmp.mp4", out)
