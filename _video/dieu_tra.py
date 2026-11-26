# KIỂU REEL "ĐIỀU TRA" (Studio 26/11/2026, anh Huy duyệt 12:37 – học CÁCH LÀM reel kể chuyện thuế Mỹ, không chép hình/chữ của ai).
# Bật bằng "kieu": "dieu_tra" trong reel.json; reel.py dùng chung phần giọng đọc/nhạc/LUFS, chỉ thay khung hình. Kiểu cũ KHÔNG đổi.
#  - NỀN = b-roll VIDEO THẬT (Wikimedia Commons / Pexels / Pixabay giấy phép mở) phủ tím tối đồng nhất, ghi nguồn trong mô tả + góc khung.
#  - Cảnh "dt": {"loai": "lat"|"ban_goc"|"ban_do"|"so_sanh"} ; cảnh có "the" (thẻ the_so) vẫn chạy, đặt nổi trên nền video.
#  - Phụ đề 1 DÒNG NHỎ ở đáy, tô vàng đúng 1 từ khoá (số, hoặc từ trong "tu_khoa").
# reel.json thêm:
#   "broll": [{"url": "https://commons.wikimedia.org/wiki/Special:FilePath/<Tên>.webm", "tu": 3, "den": 23}, {"pexels": "container port"}, ...]
#   "broll_tim": "container ship"     (dự phòng: tự tìm clip Commons theo từ khoá nếu các link trên hỏng)
#   canh[i]["nen"] = chỉ số clip (mặc định xoay vòng)
#   lat:     {"hoi": ["DÒNG 1", "DÒNG 2?"], "lat": "MỚI LÀ ĐỀ XUẤT", "tu": "Khoan"}     – câu hỏi to, tới chữ "tu" trong lời thì dập dấu lật
#   ban_goc: {"dong": [[chữ, "dau"|"dam"|"nho"|""], ...], "to": [[chỉ số dòng, "từ trong lời"], ...], "nhan": "BẢN GỐC", "nguon": "..."}
#   ban_do:  {"vung": [lon0, lat0, lon1, lat1], "noi": {"VNM": "vang", "CHN": "tim2"}, "nhan": [[lon, lat, "CHỮ"]],
#             "o_so": {"so": "159,4", "dv": "TỶ USD", "phu": "...", "o": [lon, lat]}, "mui_ten": [[lon, lat], [lon, lat], "SANG MỸ"], "nguon": "..."}
#   so_sanh: {"tieu": "...", "a": [nhãn, số], "b": [nhãn, số], "dv": "%", "tu_b": "từ trong lời", "max": 40, "nguon": "..."}
import os, re, json, math, subprocess, urllib.request, urllib.parse
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import dx2
from reel import W, H, FPS, F, fit, TRANG, VANG, TIM_S
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "HuyNguyenStudio/1.0 (chungkhoanhuynguyen.com)"
TINT = np.array([30, 10, 58], dtype=np.float32)
MO = (196, 184, 226); DO = (255, 84, 84); TOI = (16, 6, 32)
BW, BH = 720, 1280
P_Y0, P_Y1 = 360, 1470          # vùng hình chính
SUB_Y = 1600                      # phụ đề 1 dòng

# ---------------------------------------------------------------- B-ROLL
def _dai(p):
    e = subprocess.run(["ffmpeg", "-hide_banner", "-i", p], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", e)
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3)) if m else 0.0

def _cat(src, tu, den, dst, ua=False):
    vf = "scale=%d:%d:force_original_aspect_ratio=increase,crop=%d:%d,fps=%d,setsar=1" % (BW, BH, BW, BH, FPS)
    cmd = ["ffmpeg", "-y", "-loglevel", "error"] + (["-user_agent", UA] if ua else []) + ["-ss", "%.2f" % tu, "-i", src, "-t", "%.2f" % (den - tu),
           "-vf", vf, "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", dst]
    subprocess.run(cmd, check=True, timeout=600)
    d = _dai(dst)
    if d < 1.5: raise RuntimeError("clip quá ngắn %.1fs" % d)
    return d

def _json(url, hd=None):
    rq = urllib.request.Request(url, headers=dict({"User-Agent": UA}, **(hd or {})))
    return json.load(urllib.request.urlopen(rq, timeout=40))

def _pexels(q):
    k = os.environ.get("PEXELS_API_KEY")
    if not k: return []
    d = _json("https://api.pexels.com/videos/search?" + urllib.parse.urlencode({"query": q, "orientation": "portrait", "per_page": 5}), {"Authorization": k})
    out = []
    for v in d.get("videos", []):
        fs = sorted([f for f in v.get("video_files", []) if (f.get("height") or 0) >= 1000], key=lambda f: f.get("height") or 0)
        if fs: out.append({"url": fs[0]["link"], "tu": 0, "den": 20, "nguon": "Pexels – %s (Giấy phép Pexels) %s" % (v.get("user", {}).get("name", "?"), v.get("url", ""))})
    return out

def _pixabay(q):
    k = os.environ.get("PIXABAY_API_KEY")
    if not k: return []
    d = _json("https://pixabay.com/api/videos/?" + urllib.parse.urlencode({"key": k, "q": q, "per_page": 5}))
    return [{"url": h["videos"]["medium"]["url"], "tu": 0, "den": 20, "nguon": "Pixabay – %s (Giấy phép Pixabay) %s" % (h.get("user", "?"), h.get("pageURL", ""))}
            for h in d.get("hits", []) if h.get("videos", {}).get("medium", {}).get("url")]

def _commons_tim(q, n=6):
    d = _json("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({"action": "query", "list": "search", "srsearch": q + " filetype:video", "srnamespace": 6, "srlimit": n, "format": "json"}))
    return [{"url": "https://commons.wikimedia.org/wiki/Special:FilePath/" + urllib.parse.quote(x["title"][5:].replace(" ", "_")), "tu": 2, "den": 22} for x in d["query"]["search"]]

def _nguon(x):
    if x.get("nguon"): return x["nguon"]
    m = re.search(r"Special:FilePath/([^?]+)", x["url"])
    if not m: return x["url"]
    ten = urllib.parse.unquote(m.group(1)).replace("_", " ")
    try:
        import meme; gp = meme.giay_phep(x["url"])
    except Exception: gp = ""
    return "Wikimedia Commons – %s%s" % (ten, (" (" + gp + ")") if gp else "")

KHO_DU_PHONG = [   # clip Commons đã cắt sẵn trong repo – dùng khi mạng/Commons 429 (luôn có nền thật)
    {"url": "broll/cang_cork.mp4", "tu": 0, "den": 24, "nguon": "Wikimedia Commons – Aerial views of a container terminal at the Port of Cork (FILMING CORK, CC BY 3.0)"},
    {"url": "broll/tau_container.mp4", "tu": 0, "den": 18, "nguon": "Wikimedia Commons – Container ship.webm (Jan Ainali, CC BY-SA 4.0)"}]

def _upload(url):
    """Special:FilePath bị 429 trên máy GitHub (26/11) -> đọc thẳng upload.wikimedia.org: bản chuyển mã 720p/480p trước, bản gốc sau."""
    m = re.search(r"Special:FilePath/([^?]+)", url)
    if not m: return [url]
    import hashlib
    ten = urllib.parse.unquote(m.group(1)).replace(" ", "_"); h = hashlib.md5(ten.encode("utf-8")).hexdigest(); q = urllib.parse.quote(ten)
    goc = "https://upload.wikimedia.org/wikipedia/commons/%s/%s/%s" % (h[0], h[:2], q)
    tc = "https://upload.wikimedia.org/wikipedia/commons/transcoded/%s/%s/%s/%s" % (h[0], h[:2], q, q)
    return [tc + ".720p.vp9.webm", tc + ".480p.vp9.webm", tc + ".720p.webm", tc + ".480p.webm", goc]

def _tai1(x, dst):
    import time
    if x.get("pexels"): ds = _pexels(x["pexels"])
    elif x.get("pixabay"): ds = _pixabay(x["pixabay"])
    else: ds = [x]
    for y in ds:
        tu, den = float(y.get("tu", 0)), float(y.get("den", float(y.get("tu", 0)) + 20))
        if not re.match(r"https?://", y["url"]):   # file trong repo (_video/...)
            try: return _cat(os.path.join(HERE, y["url"]), tu, den, dst), y
            except Exception as e: print("broll: file repo loi", y["url"], e, flush=True); continue
        for u in _upload(y["url"]):
            for lan in range(3):
                try: return _cat(u, tu, den, dst, ua=True), y          # đọc thẳng qua HTTP (chỉ lấy đoạn cần)
                except Exception as e:
                    print("broll: doc thang loi", u[-70:], str(e)[-60:], flush=True)
                    if "429" in str(e) or "status 8" in str(e): time.sleep(8 + 6 * lan); continue   # Commons giới hạn tốc độ: chờ rồi thử lại
                    if tu > 0 and lan == 0: tu = 0; continue           # clip ngắn hơn điểm cắt: cắt từ đầu
                    break
            time.sleep(2)
        try:
            import meme; return _cat(meme.tai(y["url"]), tu, den, dst), y   # tải cả file rồi cắt
        except Exception as e: print("broll: bo qua", y["url"][-70:], e, flush=True)
    return None, None

def chuan_bi(R, WORK):
    """Tải b-roll (chạy trong reel.yml). Trả danh sách (đường dẫn, thời lượng) theo thứ tự R["broll"]; hỏng -> clip Commons dự phòng."""
    os.makedirs(WORK, exist_ok=True); clips = []; R["_nguon_nen"] = []
    lst = list(R.get("broll") or [])
    for k, x in enumerate(lst):
        p = "%s/br%d.mp4" % (WORK, k); d, y = _tai1(x, p)
        if d: clips.append((p, d)); R["_nguon_nen"].append(_nguon(y)); print("broll %d: %.1fs %s" % (k, d, y["url"][-80:]), flush=True)
    if len(clips) < 2:   # luôn có clip Commons dự phòng
        du = list(R.get("broll_du_phong") or []) + KHO_DU_PHONG
        for q in ([R.get("broll_tim")] if R.get("broll_tim") else []) + ["container ship", "cargo ship"]:
            try: du += _commons_tim(q)
            except Exception as e: print("broll: tim Commons loi", e, flush=True)
        for x in du:
            if len(clips) >= 3: break
            p = "%s/br%d.mp4" % (WORK, 100 + len(clips)); d, y = _tai1(x, p)
            if d: clips.append((p, d)); R["_nguon_nen"].append(_nguon(y)); print("broll du phong: %.1fs %s" % (d, y["url"][-80:]), flush=True)
    if not clips: print("broll: KHONG co clip nao -> nen tim chuyen dong", flush=True)
    R["_clips"] = clips
    return [None] * len(R["canh"])

def _vignette():
    y, x = np.mgrid[0:BH, 0:BW].astype(np.float32)
    r = np.sqrt(((x - BW / 2) / (BW * 0.62)) ** 2 + ((y - BH / 2) / (BH * 0.6)) ** 2)
    return np.clip(1.08 - 0.5 * r ** 2, 0.45, 1.0)[..., None]
VIG = _vignette()

class Nen:
    def __init__(self): self.k = None; self.fi = -9; self.pr = None
    def _mo(self, path, ss):
        if self.pr:
            try: self.pr.kill()
            except Exception: pass
        self.pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-stream_loop", "-1", "-ss", "%.3f" % ss, "-i", path, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                   stdout=subprocess.PIPE)
    def lay(self, R, i, t):
        cl = R.get("_clips") or []
        if not cl:   # không có clip: nền tím có dải sáng trôi
            a = np.zeros((BH, BW, 3), np.float32) + TINT
            yy = np.arange(BH, dtype=np.float32)[:, None, None]
            a += 40 * np.exp(-((yy - (BH * ((t * 0.07 + i * 0.3) % 1))) / 220) ** 2)
            return Image.fromarray(np.clip(a * VIG, 0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)
        c = R["canh"][i]; k = int(c.get("nen", i)) % len(cl); path, dur = cl[k]
        fi = int(round(t * FPS))
        if not (self.k == (i, k) and fi == self.fi + 1 and self.pr):
            self._mo(path, ((i * 2.3) + t) % max(0.5, dur - 0.2)); self.k = (i, k)
        self.fi = fi
        b = self.pr.stdout.read(BW * BH * 3)
        if len(b) < BW * BH * 3:
            self._mo(path, 0); b = self.pr.stdout.read(BW * BH * 3)
        a = np.frombuffer(b, np.uint8).reshape(BH, BW, 3).astype(np.float32)
        g = a.mean(axis=2, keepdims=True)
        a = (0.55 * a + 0.45 * g) * 0.42 + TINT * 0.75          # phủ tím tối đồng nhất
        return Image.fromarray(np.clip(a * VIG, 0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)
NEN = Nen()

# ---------------------------------------------------------------- tiện ích
def moc(loi, tu, T, mac_dinh=None):
    """Thời điểm lời đọc tới chữ `tu` (tỉ lệ ký tự)."""
    if not tu or not loi: return mac_dinh if mac_dinh is not None else 0.3
    p = loi.lower().find(tu.lower())
    if p < 0: return mac_dinh if mac_dinh is not None else 0.3
    return max(0.2, p / max(1, len(loi)) * T)

def so_vn(v, nd):
    return ("{:,.%df}" % nd).format(v).replace(",", "§").replace(".", ",").replace("§", ".")

def _so_nd(s):
    m = re.match(r"^\s*([\d.]*\d)(?:,(\d+))?", s)
    if not m: return None, 0
    return float(m.group(1).replace(".", "") + ("." + m.group(2) if m.group(2) else "")), len(m.group(2) or "")

def the_card(im, card, cx, cy, a=1.0, r=36):
    m = Image.new("L", card.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, card.width - 1, card.height - 1], r, fill=int(255 * a))
    sh = Image.new("L", (W, H), 0); ImageDraw.Draw(sh).rounded_rectangle([cx - card.width // 2 - 4, cy - card.height // 2 + 10, cx + card.width // 2 + 4, cy + card.height // 2 + 22], r, fill=int(150 * a))
    im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(18)))
    im.paste(card, (int(cx - card.width / 2), int(cy - card.height / 2)), m)

# ---------------------------------------------------------------- cảnh LẬT (hook)
def ve_lat(im, sp, t, T, loi):
    d = ImageDraw.Draw(im, "RGBA"); t_l = moc(loi, sp.get("tu"), T, 3.0)
    hoi = sp.get("hoi", []); y = 560
    a0 = dx2.ease(t / 0.3)
    for k, s in enumerate(hoi):
        f = fit(d, s, "Black", W - 120, 104); tw = d.textlength(s, font=f)
        al = int(255 * a0 * (0.55 if t > t_l else 1))
        d.text((W / 2 - tw / 2, y + (1 - a0) * 30), s, font=f, fill=(VANG if k == 0 else TRANG) + (al,), stroke_width=8, stroke_fill=(10, 4, 20, al))
        y += int(f.size * 1.22)
    if t > t_l:   # cú lật: dấu đỏ dập xuống
        a = dx2.ease((t - t_l) / 0.25); s = sp.get("lat", ""); f = F("Black", 84); tw = d.textlength(s, font=f)
        st = Image.new("RGBA", (int(tw + 90), 150), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
        sd.rounded_rectangle([4, 4, st.width - 5, 145], 20, fill=(200, 30, 46, 235), outline=(255, 255, 255, 255), width=6)
        sd.text((45, 24), s, font=f, fill=(255, 255, 255, 255))
        st = st.rotate(-5, expand=True, resample=Image.BICUBIC); k = 1.6 - 0.6 * a
        st = st.resize((int(st.width * k), int(st.height * k)), Image.BILINEAR)
        if a < 1: st.putalpha(st.getchannel("A").point(lambda v: int(v * a)))
        im.paste(st, (int(W / 2 - st.width / 2), int(y + 40 - (st.height - 170) / 2)), st)
        if sp.get("phu") and t > t_l + 0.8:
            b = dx2.ease((t - t_l - 0.8) / 0.4); s2 = sp["phu"]; f2 = fit(d, s2, "Bold", W - 160, 46)
            d.text((W / 2, y + 260), s2, font=f2, fill=TRANG + (int(255 * b),), anchor="ma", stroke_width=4, stroke_fill=(10, 4, 20, int(255 * b)))

# ---------------------------------------------------------------- cảnh BẢN GỐC
def _serif(dam, sz):
    for p in (["/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"] if dam else
              ["/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]):
        if os.path.exists(p): return ImageFont.truetype(p, sz)
    return F("Bold" if dam else "Medium", sz - 4)

_GIAY = {}
def giay(sp):
    """Ảnh trang văn bản (dựng lại chữ từ văn bản công khai) + toạ độ từng dòng logic."""
    k = json.dumps(sp.get("dong"), ensure_ascii=False)
    if k in _GIAY: return _GIAY[k]
    PW = 920; pad = 64; mw = PW - 2 * pad
    tmp = ImageDraw.Draw(Image.new("RGB", (8, 8))); rows = []
    for s, kieu in sp["dong"]:
        dam = kieu in ("dau", "dam"); sz = 30 if kieu == "nho" else (36 if kieu == "dau" else 34); f = _serif(dam, sz)
        ws = s.split(); ln = []; cur = ""
        for w_ in ws:
            c_ = (cur + " " + w_).strip()
            if tmp.textlength(c_, font=f) <= mw: cur = c_
            else: ln.append(cur); cur = w_
        if cur: ln.append(cur)
        rows.append((ln, f, kieu, int(sz * 1.42)))
    Hp = pad + sum(len(ln) * lh + 22 for ln, _, _, lh in rows) + pad
    pg = Image.new("RGB", (PW, Hp), (247, 245, 238)); d = ImageDraw.Draw(pg); y = pad; rect = []
    for ln, f, kieu, lh in rows:
        y0 = y
        for s in ln:
            if kieu == "dau": d.text((PW / 2, y), s, font=f, fill=(20, 20, 24), anchor="ma")
            else: d.text((pad, y), s, font=f, fill=(90, 90, 96) if kieu == "nho" else (28, 28, 32))
            y += lh
        rect.append((y0 - 8, y - 4)); y += 22
    for yy in range(0, Hp, 4):   # vân giấy rất nhẹ
        if (yy // 4) % 9 == 0: d.line([0, yy, PW, yy], fill=(240, 238, 230))
    _GIAY[k] = (pg, rect); return pg, rect

def ve_ban_goc(im, sp, t, T, loi):
    pg, rect = giay(sp); to = sp.get("to", [])
    ts = [moc(loi, tu, T, 0.5 + j * 1.5) for j, (_, tu) in enumerate(to)]
    j = max([k for k, x in enumerate(ts) if t >= x] or [-1])
    vh = P_Y1 - P_Y0 - 60
    def tam(k): r = rect[to[k][0]]; return (r[0] + r[1]) / 2
    if j < 0: cy, r_ = (tam(0) if to else vh / 2), None
    else:
        u = dx2.ease((t - ts[j]) / 0.45); r1 = rect[to[j][0]]
        r0 = rect[to[j - 1][0]] if j > 0 else (r1[0] - 60, r1[0] - 20)
        r_ = (r0[0] + (r1[0] - r0[0]) * u, r0[1] + (r1[1] - r0[1]) * u)
        cy = (tam(j - 1) if j > 0 else tam(0)) + (tam(j) - (tam(j - 1) if j > 0 else tam(0))) * u
    oy = int(min(max(0, cy - vh * 0.45), max(0, pg.height - vh)))
    view = pg.crop((0, oy, pg.width, oy + vh)).convert("RGBA")
    if r_ is not None:
        hl = Image.new("RGBA", view.size, (0, 0, 0, 0)); ImageDraw.Draw(hl).rounded_rectangle([40, r_[0] - oy, view.width - 40, r_[1] - oy], 10, fill=(255, 214, 64, 120))
        view = Image.alpha_composite(view, hl)
        ImageDraw.Draw(view).rounded_rectangle([34, r_[0] - oy - 4, view.width - 34, r_[1] - oy + 4], 12, outline=(242, 176, 38, 255), width=5)
    a = dx2.ease(t / 0.4); z = 1.0 + 0.04 * min(1, t / max(T, 1))
    view = view.convert("RGB").resize((int(view.width * z), int(view.height * z)), Image.BILINEAR)
    the_card(im, view, W / 2, (P_Y0 + P_Y1) / 2 + 30 + (1 - a) * 120, a, 14)
    d = ImageDraw.Draw(im, "RGBA")   # nhãn "bản gốc"
    s = sp.get("nhan", "BẢN GỐC"); f = F("Black", 36); tw = d.textlength(s, font=f); x0 = W / 2 - view.width / 2 + 10; y0 = (P_Y0 + P_Y1) / 2 + 30 - view.height / 2 - 34 + (1 - a) * 120
    d.rounded_rectangle([x0, y0, x0 + tw + 44, y0 + 62], 12, fill=(200, 30, 46, int(245 * a)))
    d.text((x0 + 22, y0 + 9), s, font=f, fill=(255, 255, 255, int(255 * a)))
    if sp.get("nguon"):
        f2 = F("Medium", 24); d.text((W / 2, P_Y1 + 48), sp["nguon"], font=fit(d, sp["nguon"], "Medium", W - 100, 24), fill=MO + (int(255 * a),), anchor="ma")

# ---------------------------------------------------------------- cảnh BẢN ĐỒ (tự vẽ từ Natural Earth 1:110m, phạm vi công cộng)
_BD = None
def _bd():
    global _BD
    if _BD is None: _BD = json.load(open(os.path.join(HERE, "dieu_tra_ban_do.json"), encoding="utf-8"))
    return _BD
def _merc(lat): return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
MAU = {"vang": VANG, "tim2": TIM_S, "do": DO, "trang": TRANG}
DAO_VN = [(16.5, 112.0, "QĐ. HOÀNG SA"), (10.0, 114.0, "QĐ. TRƯỜNG SA")]

def ve_ban_do(im, sp, t, T, loi):
    lon0, lat0, lon1, lat1 = sp.get("vung", [92, 0, 128, 30])
    pw, ph = W - 80, P_Y1 - P_Y0 - 70; z = 1.0 + 0.06 * dx2.ease(min(1, t / max(T, 1)))
    cx_l, cy_m = (lon0 + lon1) / 2, (_merc(lat0) + _merc(lat1)) / 2
    sx = min(pw / (lon1 - lon0), ph / ((_merc(lat1) - _merc(lat0)) * 180 / math.pi)) * z   # px mỗi độ kinh; vĩ theo Mercator cùng tỉ lệ
    sy2 = sx * 180 / math.pi
    def P(lon, lat): return (pw / 2 + (lon - cx_l) * sx, ph / 2 - (_merc(lat) - cy_m) * sy2)
    mp = Image.new("RGBA", (pw, ph), (12, 6, 28, 225)); d = ImageDraw.Draw(mp, "RGBA")
    for g in range(-180, 181, 5):
        x, _ = P(g, 0); d.line([x, 0, x, ph], fill=(70, 50, 120, 70), width=1)
    for g in range(-60, 61, 5):
        _, y = P(0, g); d.line([0, y, pw, y], fill=(70, 50, 120, 70), width=1)
    noi = sp.get("noi", {}); bd = _bd()
    for iso, v in bd.items():
        for poly in v["p"]:
            d.polygon([P(x, y) for x, y in poly], fill=(58, 32, 98, 255), outline=(130, 92, 190, 255))
    for k, (iso, mau) in enumerate(noi.items()):
        if iso not in bd: continue
        a = dx2.ease((t - 0.3 - k * 0.45) / 0.5)
        if a <= 0: continue
        col = MAU.get(mau, VANG)
        lay = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        for poly in bd[iso]["p"]: ld.polygon([P(x, y) for x, y in poly], fill=col + (int(235 * a),))
        if iso == "VNM":
            for la, lo, _ in DAO_VN:
                x, y = P(lo, la); ld.ellipse([x - 9, y - 9, x + 9, y + 9], fill=col + (int(255 * a),))
            puls = 0.5 + 0.5 * math.sin(t * 4)
            gl = lay.getchannel("A").filter(ImageFilter.GaussianBlur(10 + 8 * puls)).point(lambda v: min(255, int(v * 1.6)))
            mp.paste(col + (255,), (0, 0), gl.point(lambda v: int(v * 0.6)))
        mp.alpha_composite(lay)
    if "VNM" in noi:
        a = dx2.ease((t - 0.8) / 0.5)
        for la, lo, ten in DAO_VN:
            x, y = P(lo, la)
            if 0 < x < pw - 60 and 0 < y < ph: d.text((x + 16, y - 12), ten, font=F("Bold", 22), fill=TRANG + (int(220 * a),))
    for k, (lo, la, ten) in enumerate(sp.get("nhan", [])):
        a = dx2.ease((t - 0.5 - k * 0.45) / 0.4)
        if a <= 0: continue
        x, y = P(lo, la); f = F("Black", 34); tw = d.textlength(ten, font=f)
        d.rounded_rectangle([x - tw / 2 - 14, y - 26, x + tw / 2 + 14, y + 26], 12, fill=(10, 4, 20, int(200 * a)))
        d.text((x, y), ten, font=f, fill=TRANG + (int(255 * a),), anchor="mm")
    mt = sp.get("mui_ten")
    if mt:
        a = dx2.ease((t - 1.2) / 1.0)
        if a > 0:
            (xa, ya), (xb, yb) = P(*mt[0]), P(*mt[1]); xe, ye = xa + (xb - xa) * a, ya + (yb - ya) * a
            d.line([xa, ya, xe, ye], fill=VANG + (255,), width=12)
            ang = math.atan2(ye - ya, xe - xa)
            d.polygon([(xe + 30 * math.cos(ang), ye + 30 * math.sin(ang)), (xe + 22 * math.cos(ang + 2.2), ye + 22 * math.sin(ang + 2.2)), (xe + 22 * math.cos(ang - 2.2), ye + 22 * math.sin(ang - 2.2))], fill=VANG + (255,))
            if len(mt) > 2 and a > 0.9:
                f = F("Black", 40); tw = d.textlength(mt[2], font=f); x = min(pw - tw - 30, xb - tw / 2)
                d.rounded_rectangle([x - 14, yb - 86, x + tw + 14, yb - 28], 12, fill=VANG + (255,)); d.text((x, yb - 82), mt[2], font=f, fill=TOI)
    o = sp.get("o_so")
    if o:
        a = dx2.ease((t - 1.0) / 0.4)
        if a > 0:
            v, nd = _so_nd(o["so"]); u = dx2.ease((t - 1.0) / 1.4)
            s = so_vn(v * u, nd) if v is not None else o["so"]
            fs = F("Black", 92); fd = F("Black", 44); fp = F("Bold", 28)
            bw_ = max(d.textlength(so_vn(v, nd) if v is not None else o["so"], font=fs) + d.textlength(" " + o.get("dv", ""), font=fd), d.textlength(o.get("phu", ""), font=fp)) + 60
            if o.get("o"): bx, by = P(*o["o"]); bx = min(max(20, bx - bw_ / 2), pw - bw_ - 20); by = min(max(20, by), ph - 190)
            else: bx, by = pw - bw_ - 30, ph - 200
            d.rounded_rectangle([bx, by, bx + bw_, by + 170], 22, fill=(16, 6, 32, int(235 * a)), outline=VANG + (int(255 * a),), width=5)
            d.text((bx + 30, by + 12), s, font=fs, fill=VANG + (int(255 * a),))
            d.text((bx + 30 + d.textlength(so_vn(v, nd) if v is not None else o["so"], font=fs) + 14, by + 52), o.get("dv", ""), font=fd, fill=TRANG + (int(255 * a),))
            d.text((bx + 30, by + 122), o.get("phu", ""), font=fp, fill=MO + (int(255 * a),))
    a = dx2.ease(t / 0.4)
    the_card(im, mp.convert("RGB"), W / 2, (P_Y0 + P_Y1) / 2 - 10 + (1 - a) * 80, a, 28)
    dd = ImageDraw.Draw(im, "RGBA"); ng = sp.get("nguon", "") + ("  ·  " if sp.get("nguon") else "") + "Bản đồ: Natural Earth"
    dd.text((W / 2, P_Y1 + 10), ng, font=fit(dd, ng, "Medium", W - 100, 24), fill=MO, anchor="ma")

# ---------------------------------------------------------------- THANH SO SÁNH 2 MỨC
def ve_so_sanh(im, sp, t, T, loi):
    cw, ch = W - 80, 760; card = Image.new("RGB", (cw, ch), (20, 8, 40)); d = ImageDraw.Draw(card)
    d.rounded_rectangle([3, 3, cw - 4, ch - 4], 30, outline=(100, 60, 160), width=4)
    d.text((cw / 2, 46), sp.get("tieu", ""), font=fit(d, sp.get("tieu", ""), "ExtraBold", cw - 80, 44), fill=TIM_S, anchor="ma")
    mx = sp.get("max") or max(sp["a"][1], sp["b"][1]) * 1.12; dv = sp.get("dv", "")
    tb = max(1.6, moc(loi, sp.get("tu_b"), T, 1.8))
    for k, ((lab, v), t0, col) in enumerate([(sp["a"], 0.3, TIM_S), (sp["b"], tb, VANG)]):
        y = 190 + k * 260; u = dx2.ease((t - t0) / 1.1)
        d.text((50, y), lab, font=F("Bold", 40), fill=(220, 210, 240))
        d.rounded_rectangle([50, y + 64, cw - 50, y + 164], 22, fill=(44, 24, 76))
        if u > 0:
            ww = max(30, (cw - 100) * v / mx * u); d.rounded_rectangle([50, y + 64, 50 + ww, y + 164], 22, fill=col)
            nd = 0 if float(v).is_integer() else 1; s = so_vn(v * u, nd) + dv; fs = F("Black", 72)
            if ww > d.textlength(s, font=fs) + 60: d.text((50 + ww - 24, y + 114), s, font=fs, fill=TOI, anchor="rm")
            else: d.text((50 + ww + 20, y + 114), s, font=fs, fill=TRANG, anchor="lm")
    if sp.get("nguon"): d.text((cw / 2, ch - 56), "Nguồn: " + sp["nguon"], font=fit(d, "Nguồn: " + sp["nguon"], "Medium", cw - 80, 26), fill=MO, anchor="ma")
    a = dx2.ease(t / 0.35)
    the_card(im, card, W / 2, (P_Y0 + P_Y1) / 2 + (1 - a) * 80, a, 30)

# ---------------------------------------------------------------- PHỤ ĐỀ 1 DÒNG
FS = 46; SW = W - 200
def dong_pd(loi):
    d = ImageDraw.Draw(Image.new("RGB", (8, 8))); f = F("ExtraBold", FS); out = []
    for cau in re.split(r"(?<=[.!?…:])\s+", (loi or "").strip()):
        cur = ""
        for w_ in cau.split():
            c_ = (cur + " " + w_).strip()
            if d.textlength(c_, font=f) <= SW: cur = c_
            else: out.append(cur); cur = w_
        if cur: out.append(cur)
    return [s for s in out if s]

def ve_pd(im, c, loi, t, T):
    ls = dong_pd(loi)
    if not ls: return
    L = [len(s) + 4 for s in ls]; tot = sum(L); a = 0; k = len(ls) - 1
    for i, l in enumerate(L):
        if t < a + l / tot * T: k = i; break
        a += l / tot * T
    s = ls[k]; d = ImageDraw.Draw(im, "RGBA"); f = F("ExtraBold", FS); ws = s.split(); sp = d.textlength(" ", font=f)
    tk = [x.lower() for x in (c.get("tu_khoa") or [])]; hl = -1
    for j, w_ in enumerate(ws):
        if re.search(r"\d", w_) or any(w_.lower().strip(".,:;?!").startswith(x) for x in tk): hl = j; break
    tw = d.textlength(s, font=f); x = W / 2 - tw / 2
    d.rounded_rectangle([x - 26, SUB_Y - 14, x + tw + 26, SUB_Y + FS + 22], 18, fill=(8, 2, 18, 190))
    for j, w_ in enumerate(ws):
        d.text((x, SUB_Y), w_, font=f, fill=VANG if j == hl else TRANG); x += d.textlength(w_, font=f) + sp

# ---------------------------------------------------------------- KHUNG
def ve_dau(im, R, i, t):
    d = ImageDraw.Draw(im, "RGBA")
    nh = (R.get("nhan") or "ĐIỀU TRA").upper(); fn = F("Bold", 28); tw = d.textlength(nh, font=fn)
    d.rounded_rectangle([W / 2 - tw / 2 - 22, 86, W / 2 + tw / 2 + 22, 134], 24, fill=(196, 40, 52)); d.text((W / 2 - tw / 2, 92), nh, font=fn, fill=TRANG)
    if i > 0:   # tiêu đề nhỏ cố định
        hk = R.get("hook") or []; s1 = hk[0] if hk else ""; s2 = (" " + hk[1]) if len(hk) > 1 else ""
        f = F("Black", 50); tw = d.textlength(s1 + s2, font=f)
        if tw > W - 100: f = fit(d, s1 + s2, "Black", W - 100, 50); tw = d.textlength(s1 + s2, font=f)
        x = W / 2 - tw / 2
        d.text((x, 160), s1, font=f, fill=VANG, stroke_width=5, stroke_fill=(10, 4, 20)); d.text((x + d.textlength(s1, font=f), 160), s2, font=f, fill=TRANG, stroke_width=5, stroke_fill=(10, 4, 20))
    c = R["canh"][i]; s = (c.get("chu_to") or "").replace("→", "»")
    if s and not (c.get("dt") or {}).get("loai") == "lat":
        a = dx2.ease(t / 0.3); sc = 1.15 - 0.15 * a; f = F("Black", int(46 * sc)); tw = d.textlength(s, font=f)
        d.rounded_rectangle([W / 2 - tw / 2 - 24, 250, W / 2 + tw / 2 + 24, 250 + f.size + 26], 14, fill=VANG + (int(250 * a),))
        d.text((W / 2 - tw / 2, 258), s, font=f, fill=TOI + (int(255 * a),))

def ve_cuoi(im, R, prog):
    d = ImageDraw.Draw(im, "RGBA"); y0 = H - 178
    d.rectangle([0, y0, W, y0 + 5], fill=(46, 20, 78)); d.rectangle([0, y0, int(W * prog), y0 + 5], fill=TIM_S)
    u1, u2 = "chungkhoanhuynguyen", ".com"; fu = F("Bold", 32); fd = F("SemiBold", 32)
    wu = d.textlength(u1, font=fu) + d.textlength(u2, font=fd); x = W / 2 - wu / 2; yu = H - 128
    d.text((x, yu), u1, font=fu, fill=TRANG); d.text((x + d.textlength(u1, font=fu), yu), u2, font=fd, fill=VANG)
    if R.get("_clips"): d.text((W - 30, 34), "Video nền: " + R.get("nguon_nen_ngan", "Wikimedia Commons"), font=F("Medium", 20), fill=(200, 190, 225, 170), anchor="ra")

def khung(R, i, t, T, ph, tong_t, tong_T):
    import reel
    im = NEN.lay(R, i, tong_t); c = R["canh"][i]; loi = reel.bo_mien_tru(c.get("loi", ""))
    ve_dau(im, R, i, t)
    dt = c.get("dt") or {}; lo = dt.get("loai")
    if lo == "lat": ve_lat(im, dt, t, T, loi)
    elif lo == "ban_goc": ve_ban_goc(im, dt, t, T, loi)
    elif lo == "ban_do": ve_ban_do(im, dt, t, T, loi)
    elif lo == "so_sanh": ve_so_sanh(im, dt, t, T, loi)
    elif c.get("the"):
        import the_so; card = the_so.ve(c["the"], t); a = dx2.ease(t / 0.35)
        the_card(im, card, W / 2, (P_Y0 + P_Y1) / 2 + (1 - a) * 80, a, 36)
    if c.get("web"): reel.ve_web_to(im, t, (P_Y0 + P_Y1) // 2 - 60)
    ve_pd(im, c, loi, t, T)
    ve_cuoi(im, R, tong_t / max(tong_T, 0.1))
    if c.get("hoi"):   # nút theo dõi đặt trên phụ đề (không đè chữ)
        lp = Image.new("RGBA", (W, H), (0, 0, 0, 0)); reel.ve_theo_doi(lp, t, T)
        im.paste(lp, (0, -215), lp)
    if i > 0 and t < 0.2:   # punch-in nhẹ khi sang cảnh
        z = 1 + 0.04 * (1 - dx2.ease(t / 0.2)); cw_, ch_ = int(W / z), int(H / z)
        im = im.crop(((W - cw_) // 2, (H - ch_) // 2, (W - cw_) // 2 + cw_, (H - ch_) // 2 + ch_)).resize((W, H), Image.BILINEAR)
    return im

def ghi_nguon(R, OUT, key):
    ng = list(dict.fromkeys(R.get("_nguon_nen") or []))
    if not ng: return
    s = "🎬 Video nền: " + " ; ".join(ng) + "\n🗺 Bản đồ: Natural Earth (phạm vi công cộng)\n"
    p = os.path.join(OUT, key + "_mo_ta.txt")
    try: open(p, "a", encoding="utf-8").write("\n" + s)
    except Exception: pass
    open(os.path.join(OUT, key + "_anh.txt"), "w", encoding="utf-8").write(s)
