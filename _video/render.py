# Xưởng video: kịch bản NV1 (S["KEY"]) -> giọng chốt (VieNeu miễn phí) -> dựng dx2 -> nhạc nền -> mp4 + ảnh bìa
# Dùng: python _video/render.py <thư mục lô trong _video/queue> KEY [--preview N]
import sys, re, os, json, subprocess, shutil, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
batch, key = sys.argv[1], sys.argv[2]
prev = int(sys.argv[sys.argv.index("--preview") + 1]) if "--preview" in sys.argv else 0
QD = os.path.join(HERE, "queue", batch)
OUT = os.path.join(HERE, "out"); os.makedirs(OUT, exist_ok=True)
WORK = "/tmp/hnv_" + key; os.makedirs(WORK, exist_ok=True)

# 1) nến tuần -> định dạng engine (mới nhất trước, dict o h l c v)
px = {}
p = os.path.join(QD, "px_tuan.json")
if os.path.exists(p):
    for sym, rows in json.load(open(p, encoding="utf-8")).items():
        px[sym] = [{"d": r[0], "o": r[1], "h": r[2], "l": r[3], "c": r[4], "v": r[5]} for r in rows]
json.dump(px, open(WORK + "/px.json", "w")); os.environ["HN_PX"] = WORK + "/px.json"
sys.path.insert(0, os.path.join(HERE, "engine"))
import dx2, music

# 2) kịch bản
g = {}; exec(open(os.path.join(QD, "video_dai.py"), encoding="utf-8").read(), g)
raw = g["S"][key]
if prev: raw = raw[:prev]
# QL1 11/11: font hiển thị "~" giống dấu trừ ("Gấp -9 lần") -> chữ trên màn dùng "khoảng"
import re as _re
def _bo_nga(v, k=None):
    if k == "say": return v
    if isinstance(v, str): return _re.sub(r"~\s*(?=\d)", "khoảng ", v).replace("~", "≈")
    if isinstance(v, dict): return {kk: _bo_nga(vv, kk) for kk, vv in v.items()}
    if isinstance(v, (list, tuple)): return type(v)(_bo_nga(x) for x in v)
    return v
raw = [_bo_nga(sc) for sc in raw]

# 2b) đọc đúng tên web + chèn lời mời về nhóm tư vấn (giữa video và trước cảnh kết) — áp cho mọi video dài
_WEB = "chứng khoán Huy Nguyễn chấm com"
def _doc_web(t):
    t = re.sub(r"(?i)chung\s*khoan\s*huy\s*nguyen\s*(\.|chấm)\s*com", _WEB, t)
    return re.sub(r"(?i)chungkhoanhuynguyen", "chứng khoán Huy Nguyễn", t)
CTA_GIUA = {"k": "text", "label": "NHÓM TƯ VẤN MIỄN PHÍ", "cap": ("VÀO NHÓM ZALO", "0365 188 286"), "cta": 1,
    "say": "Khoan, nói nhanh một chút. Nếu anh chị không có thời gian tự lọc cổ phiếu, hãy vào nhóm Zalo tư vấn của Huy Nguyễn. Ở đó mỗi ngày có danh sách cổ phiếu khỏe, nhận định thị trường, và anh chị được hỏi trực tiếp về danh mục của mình, hoàn toàn miễn phí. Số Zalo là không ba sáu năm, một tám tám, hai tám sáu, có sẵn trong phần mô tả. Giờ mình đi tiếp."}
CTA_CUOI = {"k": "text", "label": "ĐỪNG ĐẦU TƯ MỘT MÌNH", "cap": ("ZALO 0365 188 286", "CHUNGKHOANHUYNGUYEN.COM"), "cta": 1,
    "say": "Trước khi kết thúc, có hai thứ anh chị nên lưu lại. Một, vào chứng khoán Huy Nguyễn chấm com để xem bảng mười cổ phiếu khỏe nhất thị trường cập nhật liên tục và báo cáo tài chính hơn bốn trăm mã, miễn phí. Hai, nếu anh chị đang kẹt hàng, chưa biết nên giữ hay cơ cấu, hoặc muốn có người đồng hành, nhắn Zalo số không ba sáu năm, một tám tám, hai tám sáu để vào nhóm tư vấn, Huy và đội ngũ sẽ hỗ trợ trực tiếp. Đầu tư một mình rất dễ sai, có người cùng đi sẽ chắc hơn. Nhớ đăng ký kênh và bấm chuông để không bỏ lỡ video tiếp theo."}
CTA_WEB = {"k": "text", "label": "TÀI LIỆU ĐI KÈM VIDEO", "cap": ("TÀI LIỆU MIỄN PHÍ", "CHUNGKHOANHUYNGUYEN.COM"), "cta": 1,
    "say": "Toàn bộ số liệu trong video này, cùng bảng định giá và báo cáo tài chính hơn bốn trăm mã, anh chị xem miễn phí tại chứng khoán Huy Nguyễn chấm com. Ở đó có người tư vấn trực tiếp nếu anh chị cần hỏi về mã mình đang cầm."}
if g.get("CHI_CTA_CUOI") and not any(x.get("cta") for x in raw):   # QL1 11/11: video kể chuyện – không cắt ngang mạch truyện, chỉ 1 lời mời ở cuối
    raw = list(raw); raw.insert(len(raw) - 1 if raw[-1].get("k") == "end" else len(raw), dict(CTA_CUOI))
elif not g.get("NO_CTA") and not any(x.get("cta") for x in raw) and len(raw) >= 6:
    raw = list(raw); raw.insert(max(2, len(raw)//4), dict(CTA_WEB)); raw.insert(len(raw)*2//3, dict(CTA_GIUA))
    raw.insert(len(raw) - 1 if raw[-1].get("k") == "end" else len(raw), dict(CTA_CUOI))
import xung_ho  # xưng em – anh chị, không gọi "bạn" (anh Huy chốt 6/11)
_MT_DOC = re.compile(r"[^.!?]*(?:không phải (?:là )?khuyến nghị|quan điểm cá nhân|chia sẻ kiến thức, không)[^.!?]*[.!?]?\s*", re.I)
# anh Huy 7/11: câu miễn trừ chỉ ghi CHỮ NHỎ trên hình, KHÔNG đọc thành lời
_LP = (lambda t: t) if g.get("XH_BAN") else xung_ho.le_phep  # anh Huy 10/11: kênh @5 kể chuyện nhập vai được gọi "bạn"
for _x in raw:
    _x["say"] = re.sub(r"\s{2,}", " ", _MT_DOC.sub(" ", _LP(_doc_web(_x.get("say", ""))))).strip()
    if isinstance(_x.get("cap"), (list, tuple)): _x["cap"] = tuple(_LP(c) for c in _x["cap"])
    elif isinstance(_x.get("cap"), str): _x["cap"] = _LP(_x["cap"])
try:
    import kiem_loi; _QCV = [q for q in kiem_loi.kiem([{"loi": x.get("say", "")} for x in raw if not x.get("cta")], None, False) if not (g.get("XH_BAN") and "'bạn'" in q)]
except Exception as _e: _QCV = []

def conv(sc):
    s = dict(sc); k = s["k"]
    s.setdefault("label", ""); s.setdefault("cap", ("", ""))
    if isinstance(s["cap"], str): s["cap"] = tuple(s["cap"].split("\n"))  # cap chuỗi -> các dòng
    if k == "hook":
        ch = s.pop("chart", None)
        if ch and ch.get("sym") in px:
            s.update(k="candles", sym=ch["sym"], n=min(int(ch.get("weeks", 52)), len(px[ch["sym"]])),
                     circles=ch.get("circles", []), tag=(lambda t: t if "NẾN TUẦN" in t else t[:40] + " · NẾN TUẦN")((s["label"] or ch["sym"]).upper()), reveal=1.6)
        else: s["k"] = "text"
    elif k == "image":
        if not os.path.exists(os.path.join(HERE, "engine", s.get("img", "?"))): s["k"] = "text"
    elif k == "checklist":
        s["items"] = [it[0] if isinstance(it, (list, tuple)) else it for it in s.get("items", [])]
    elif k == "bars":
        s["bars"] = [(b[0], abs(b[1]) if b[1] else 0.001, b[2], b[3] if len(b) > 3 else str(b[1])) for b in s.get("bars", [])]
    elif k not in dx2.KINDS and k not in ("text", "end", "chat", "noti", "call", "giay"): s["k"] = "text"
    if s["k"] == "text": s.setdefault("y", 860)
    return s
scenes = [conv(s) for s in raw]

# 3) giọng chốt Huy70_HaiDang30 (JSON từ secret HN_VOICE_JSON hoặc file)
from vieneu import Vieneu
vj = os.environ.get("HN_VOICE_JSON")
if vj: v = json.loads(vj)
else:
    sys.path.insert(0, os.path.join(HERE, ".."))
    import hncodec; v = hncodec.load(os.path.join(HERE, "engine", "giong.bin"))
VOICE = {"speaker_emb": np.asarray(v["speaker_emb"], dtype=np.float32), "codes": np.asarray(v["codes"], dtype=v.get("codes_dtype", "int64"))}
tts = Vieneu(); wd = WORK + "/wav"; os.makedirs(wd, exist_ok=True); t0 = time.time()
for i, sc in enumerate(raw):
    say = sc.get("say", "").strip() or "."
    tts.save(np.asarray(tts.infer(say, voice=VOICE, temperature=0.7), dtype=np.float32), "%s/%02d.wav" % (wd, i))
print(key, "giong %.0fs" % (time.time() - t0), flush=True)


# ---- khung NGANG 1920x1080 cho YouTube video dài: ghép từ khung dọc của engine ----
from PIL import Image, ImageDraw, ImageFilter
LW, LH = 1920, 1080
def _bg():
    g = Image.new("RGB", (LW, LH), (13, 16, 23)); d = ImageDraw.Draw(g)
    for r, c in ((900, (18, 22, 31)), (600, (22, 27, 38)), (320, (26, 32, 45))):
        d.ellipse([LW*0.36-r, LH/2-r, LW*0.36+r, LH/2+r], fill=c)
    return g.filter(ImageFilter.GaussianBlur(140))
LBG = _bg()
_CV = {}
def _cover(v, sc):
    key_ = id(sc)
    if key_ not in _CV:
        c = v.resize((480, int(v.height*480/v.width)), Image.BILINEAR).crop((0, 100, 480, 370)).filter(ImageFilter.GaussianBlur(10))
        c = c.resize((LW, LH), Image.BILINEAR)
        _CV[key_] = Image.blend(c, Image.new("RGB", (LW, LH), (8, 10, 15)), 0.55)
    return _CV[key_].copy()
def _kb_bg(sc, t):
    """Ken Burns nhẹ cho ảnh nền cảnh số liệu: zoom 1.00->1.08 + lia chậm, chiều xen kẽ theo cảnh."""
    B = sc["_bg"]; T = max(1.0, sc.get("_T") or 20.0); u = dx2.ease(min(1.0, t / T)) if T < 3 else min(1.0, t / T)
    zin = (sc.get("_idx", 0) % 2 == 0); z = 1.0 + 0.08 * (u if zin else 1 - u)
    w2, h2 = int(LW / z), int(LH / z); dx = int((LW - w2) * (0.3 + 0.4 * u)); dy = (LH - h2) // 2
    return B.crop((dx, dy, dx + w2, dy + h2)).resize((LW, LH), Image.BILINEAR)
def _prep_ph(sc, ph):
    sc["_ph"] = ph
    # nền ảnh thật làm tối + thẻ ảnh sắc nét bên phải
    r = max(LW/ph.width, LH/ph.height); b = ph.resize((int(ph.width*r)+1, int(ph.height*r)+1), Image.LANCZOS)
    b = b.crop(((b.width-LW)//2, (b.height-LH)//2, (b.width-LW)//2+LW, (b.height-LH)//2+LH)).filter(ImageFilter.GaussianBlur(3))
    sc["_bg"] = Image.blend(b, Image.new("RGB", (LW, LH), (8, 10, 15)), 0.66)
    cw, chh = 440, 260; r = max(cw/ph.width, chh/ph.height); c = ph.resize((int(ph.width*r)+1, int(ph.height*r)+1), Image.LANCZOS)
    c = c.crop(((c.width-cw)//2, (c.height-chh)//2, (c.width-cw)//2+cw, (c.height-chh)//2+chh))
    m = Image.new("L", (cw, chh), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, cw-1, chh-1], 18, fill=255)
    sc["_card"] = (c, m)

# --- phụ đề: chia lời đọc thành câu ngắn, rải theo thời lượng giọng thật ---
def _chunks(txt, mx=52):
    import re as _re
    parts = [x.strip() for x in _re.split(r"(?<=[.!?;:,])\s+", (txt or "").strip()) if x.strip()]
    out = []
    for p_ in parts:
        w = p_.split(); cur = ""
        for x in w:
            if len(cur) + len(x) + 1 > mx and cur: out.append(cur); cur = x
            else: cur = (cur + " " + x).strip()
        if cur: out.append(cur)
    m = []
    for c in out:
        if m and (len(m[-1]) + len(c) + 1 <= 34 or (len(c) < 12 and len(m[-1]) + len(c) + 1 <= 64)): m[-1] += " " + c
        else: m.append(c)
    return m
def _doi(t):
    try:
        import so_chu; return so_chu.doi(t)
    except Exception: return t
def _sub_plan(scenes, b, gap):
    for i, sc in enumerate(scenes):
        ch = _chunks(_doi(sc.get("say", ""))); T = max(0.5, b[i+1] - b[i] - gap); n = sum(len(c) for c in ch) or 1; t = 0; sc["_sub"] = []
        for c in ch:
            d_ = T * len(c) / n; sc["_sub"].append((t, t + d_, c)); t += d_
def _srt(scenes, b, path):
    def ts(x): h = int(x // 3600); m = int(x % 3600 // 60); s_ = x % 60; return "%02d:%02d:%06.3f" % (h, m, s_)
    L = []; k = 1
    for i, sc in enumerate(scenes):
        for a, e, c in sc.get("_sub", []):
            L.append("%d\n%s --> %s\n%s\n" % (k, ts(b[i] + a).replace(".", ","), ts(b[i] + e).replace(".", ","), c)); k += 1
    open(path, "w", encoding="utf-8").write("\n".join(L))
SUB_ON = [False]
HU = [os.environ.get("HIEU_UNG", "1") == "1"]
# 11/11 NV1: HIỆU ỨNG 2 – chuyển cảnh đa dạng (whip đổi chương / crossfade / zoom xuyên), Ken Burns ảnh nền cảnh số liệu,
# thanh chương có vạch mốc, whoosh chỉ khi đổi chương. Bật: META/biến HIEU_UNG2=1 hoặc lô >= 20261111 (lô cũ giữ nguyên).
HU2 = [HU[0] and (os.environ.get("HIEU_UNG2") == "1" or bool(g.get("HIEU_UNG2")) or (os.environ.get("HIEU_UNG2") != "0" and batch[:8] >= "20261111"))]   # 10/11: hiệu ứng video dài (chuyển cảnh, phụ đề màu, thanh chương)
_DO = re.compile(r"^(giảm|mất|lỗ|sập|nghèo|khó|âm|bán|tháo|hoảng|đóng|phá|nợ|rơi|bẫy|rủi)", re.I)
_XANH = re.compile(r"^(tăng|lãi|giàu|lời|dương|hồi|mua|gom|khỏe|bền)", re.I)
def _mau(w):
    if re.search(r"\d", w): return (255, 200, 40)
    if _DO.match(w): return (255, 92, 92)
    if _XANH.match(w): return (90, 240, 120)
    return (255, 255, 255)
def _draw_sub(im, sc, t, cx, wmax):
    if not SUB_ON[0]: return
    cur = next(((a, c) for a, e, c in sc.get("_sub", []) if a <= t < e), None)
    if not cur: return
    a0, cur = cur
    d = ImageDraw.Draw(im, "RGBA"); f = dx2.F("Bold", 40)
    while d.textlength(cur, font=f) > wmax - 60 and f.size > 26: f = dx2.F("Bold", f.size - 2)
    if HU[0]:   # nảy nhẹ 1.12 -> 1 trong 0.16s khi đổi cụm
        k = min(1.0, (t - a0) / 0.16); sz = max(20, int(f.size * (1.12 - 0.12 * dx2.ease(k)))); f = dx2.F("Bold", sz)
    tw = d.textlength(cur, font=f); y = LH - 112 if wmax < LW - 300 else LH - 118
    d.rounded_rectangle([cx - tw/2 - 22, y - 10, cx + tw/2 + 22, y + f.size + 14], 14, fill=(0, 0, 0, 170))
    if not HU[0]:
        d.text((cx - tw/2, y), cur, font=f, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0)); return
    x = cx - tw/2; sp = d.textlength(" ", font=f)
    for w in cur.split(" "):
        d.text((x, y), w, font=f, fill=_mau(w), stroke_width=2, stroke_fill=(0, 0, 0)); x += d.textlength(w, font=f) + sp
def _thanh_chuong(im, scenes, i, frac):
    """Thanh tiến độ mảnh trên cùng + nhãn chương ngắn (giúp người xem biết còn bao nhiêu, giữ chân)."""
    d = ImageDraw.Draw(im, "RGBA"); n = len(scenes)
    B = scenes[0].get("_B") if HU2[0] else None
    pr = ((B[i] + frac * (B[i + 1] - B[i])) / B[-1]) if B else (i + frac) / n
    d.rectangle([0, 0, LW, 6], fill=(255, 255, 255, 40)); d.rectangle([0, 0, int(LW * pr), 6], fill=(255, 196, 0, 230))
    if HU2[0]:   # vạch mốc đầu mỗi chương (theo thời lượng thật) – người xem thấy còn mấy phần
        B = scenes[0].get("_B")
        for k, sk in enumerate(scenes):
            if k and sk.get("ch"):
                x = int(LW * ((B[k] / B[-1]) if B else k / n)); d.rectangle([x - 2, 0, x + 2, 12], fill=(255, 255, 255, 200))
    ch = scenes[i].get("ch") or ""
    _tt = frac * (scenes[i].get("_T") or 10)
    if ch and ((0.36 < _tt < 2.8) if HU2[0] else frac < 0.12):   # nhãn chương hiện 1–2s đầu chương (HU2: sau khi chuyển cảnh xong)
        f = dx2.F("Bold", 26); tw = d.textlength(ch, font=f)
        x0 = int((LW - tw - 32) / 2)   # QL1 11/11: giữa trên cùng – không đè logo HUY NGUYỄN góc trái
        d.rounded_rectangle([x0, 18, x0 + tw + 32, 18 + 46], 23, fill=(255, 196, 0, 235)); d.text((x0 + 16, 26), ch, font=f, fill=(10, 12, 17))
AV = [None, None, 0]
def _av_init(wav):
    if os.environ.get('CHAN_DUNG') != '1': return
    try:
        sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..")); import hncodec, chandung, base64
        d = hncodec.load(os.path.join(HERE, "engine", "chandung.bin")); pj = WORK + "/chandung.jpg"
        open(pj, "wb").write(base64.b64decode(d["jpg"]))
        AV[0] = chandung.ChanDung(pj, 170); AV[1] = chandung.dieu_khien(wav, dx2.FPS); print(key, "chan dung ok", flush=True)
    except Exception as e: AV[0] = None; print("chan dung: bo qua", repr(e), flush=True)
def _av_dan(im):
    if AV[0] is None or not SUB_ON[0]: return im
    try:
        o, w, b, n = AV[1]; gf = AV[2]; k = min(gf, len(o) - 1)
        bub = AV[0].bubble(mo=o[k], wide=w[k], blink=b[k], t=gf / dx2.FPS, nod=n[k])
        rgb = Image.fromarray(bub[..., 2::-1].copy() if False else bub[..., [2, 1, 0]].copy()); al = Image.fromarray(bub[..., 3].copy())
        im.paste(rgb, (1605 - 85, 156), al)
    except Exception as e:
        AV[0] = None; print("chan dung: tat", repr(e), flush=True)
    return im
import land_text
def land(v, sc, t):
    k = sc["k"]
    if k in ("chat", "noti", "call", "giay"):   # cảnh điện thoại (chat_ui) – phụ đề dưới cột chữ bên phải
        import chat_ui; im = chat_ui.frame(sc, t); _draw_sub(im, sc, t, 1295, 1100); return im
    if k in ("end", "text"):   # cảnh chữ: ảnh tràn khung + Ken Burns + đổi góc máy (bỏ kiểu cột dọc giữa màn hình)
        im = land_text.frame(sc, t); _draw_sub(im, sc, t, LW/2, LW - 200); return im
    if "_bg" in sc and HU2[0]: im = _kb_bg(sc, t)
    else: im = sc["_bg"].copy() if "_bg" in sc else _cover(v, sc)
    if "_bg" in sc:
        fc = dx2.F("SemiBold", 18); ImageDraw.Draw(im).text((24, LH-34), "Ảnh minh hoạ: Wikimedia Commons", font=fc, fill=(150, 156, 170))
    if k in ("end", "text"):
        c = v.crop((0, 200, 1080, 1720)); s = LH/c.height; c = c.resize((int(c.width*s), LH), Image.LANCZOS)
        im.paste(c, ((LW-c.width)//2, 0)); _draw_sub(im, sc, t, LW/2, LW - 200); return im
    p = v.crop((66, 470, 1014, 1150)); s = 1.32; p = p.resize((int(p.width*s), int(p.height*s)), Image.LANCZOS)
    im.paste(p, (50, 26)); _px, _pw = 50, p.width          # chừa dải dưới cho phụ đề, không che số liệu
    d = ImageDraw.Draw(im); x0 = 50 + p.width + 40; cw = LW - x0 - 50; cx = x0 + cw/2
    dx2.brand(im, d, cx, 70, 0.9, 1.0, (10, 12, 17))
    lab = sc.get("label") or ""
    if lab:
        a = dx2.ease(t/0.4); f = dx2.fit(d, lab, "Bold", cw, 34); tw = d.textlength(lab, font=f)
        d.text((cx - tw/2, 336), lab, font=f, fill=dx2.mix(dx2.GOLD, a, (10, 12, 17)))
        d.line([cx - 60, 388, cx + 60, 388], fill=dx2.mix(dx2.GOLD, a, (10, 12, 17)), width=3)
    cols = sc.get("cols") or [dx2.CREAM, dx2.GOLD]; y = 466
    for i, l in enumerate(sc.get("cap") or []):
        if not l: continue
        a = dx2.ease((t - 0.25 - i*0.18)/0.45)
        if a <= 0: continue
        f = dx2.fit(d, l, "Black", cw, 92); c = cols[i] if i < len(cols) else dx2.CREAM
        tw = d.textlength(l, font=f); d.text((cx - tw/2, y + (1-a)*24), l, font=f, fill=dx2.mix(c, a, (10, 12, 17))); y += int(f.size*1.2)
    if "_card" in sc:
        c, m = sc["_card"]; a = dx2.ease((t - 0.5)/0.5)
        if a > 0:
            yy = LH - 110 - c.height + int((1-a)*30); xx = int(cx - c.width/2)
            ImageDraw.Draw(im).rounded_rectangle([xx-4, yy-4, xx+c.width+3, yy+c.height+3], 21, fill=dx2.GOLD)
            im.paste(c, (xx, yy), m)
    f = dx2.F("SemiBold", 26); u = "chungkhoanhuynguyen.com"; d.text((cx - d.textlength(u, font=f)/2, LH - 70), u, font=f, fill=(120, 128, 146))
    _av_dan(im)
    _draw_sub(im, sc, t, _px + _pw/2, _pw)
    return im
PREV = [None]
def _kieu(scenes, i):
    """Kiểu chuyển: đổi chương = whip (lia nhanh); cảnh thường xen kẽ crossfade / zoom xuyên; vào/ra CTA = crossfade."""
    if scenes[i].get("ch"): return "whip"
    if scenes[i].get("cta") or scenes[i - 1].get("cta"): return "fade"
    return "zoom" if i % 3 == 0 else "fade"
DUR = {"whip": 0.34, "fade": 0.40, "zoom": 0.36}
def _mo_ngang(im, k):
    """mờ chuyển động ngang (rẻ): co chiều ngang rồi phóng lại."""
    k = max(1, int(k)); return im.resize((max(8, LW // k), LH), Image.BILINEAR).resize((LW, LH), Image.BILINEAR) if k > 1 else im
def _chuyen(prev, cur, tt, kieu):
    D = DUR[kieu]
    if tt >= D: return cur
    u = dx2.ease(tt / D)
    if kieu == "fade": return Image.blend(prev, cur, u)
    if kieu == "zoom":   # khung cũ phóng to mờ dần, khung mới thu từ 1.06 về 1
        z1 = 1.0 + 0.14 * u; w1, h1 = int(LW * z1), int(LH * z1)
        a = prev.resize((w1, h1), Image.BILINEAR).crop(((w1 - LW)//2, (h1 - LH)//2, (w1 - LW)//2 + LW, (h1 - LH)//2 + LH))
        z2 = 1.06 - 0.06 * u; w2, h2 = int(LW * z2), int(LH * z2)
        b_ = cur.resize((w2, h2), Image.BILINEAR).crop(((w2 - LW)//2, (h2 - LH)//2, (w2 - LW)//2 + LW, (h2 - LH)//2 + LH))
        return Image.blend(a, b_, u)
    # whip: cả 2 khung trượt sang trái, mờ ngang mạnh nhất ở giữa
    x = int(LW * u); bl = 1 + 22 * (1 - abs(2 * u - 1))
    can = Image.new("RGB", (LW, LH)); can.paste(prev, (-x, 0)); can.paste(cur, (LW - x, 0))
    return _mo_ngang(can, bl)
def build_land(key, scenes, wav_dir, out, gap=0.28, tail=1.2, tempo=1.0):
    import wave, re
    tmpd = "/tmp/hl_%s_parts" % key; os.makedirs(tmpd, exist_ok=True); parts = []; b = [0.0]
    for i in range(len(scenes)):
        src = os.path.join(wav_dir, "%02d.wav" % i); dst = os.path.join(tmpd, "%02d.wav" % i)
        pad = gap + (tail if i == len(scenes)-1 else 0)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-af",
            "silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.05,areverse,silenceremove=start_periods=1:start_threshold=-40dB:start_silence=0.08,areverse,atempo=%.3f,apad=pad_dur=%.2f" % (tempo, pad),
            "-ar", "44100", "-ac", "1", dst])
        with wave.open(dst) as w: dd = w.getnframes()/w.getframerate()
        b.append(b[-1] + dd); parts.append(dst)
    lst = os.path.join(tmpd, "list.txt"); open(lst, "w").write("".join("file '%s'\n" % p for p in parts))
    A = os.path.join(tmpd, "full.wav")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", A])
    _sub_plan(scenes, b, gap); SUB_ON[0] = True; _av_init(A)
    scenes[0]["_B"] = list(b)
    for _k, _s in enumerate(scenes): _s["_idx"] = _k; _s["_hu2"] = HU2[0]
    tmp = "/tmp/hl_%s.mp4" % key; FPS = dx2.FPS
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (LW, LH), "-r", str(FPS), "-i", "-",
                          "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "21", "-g", "60", "-preset", "veryfast", tmp], stdin=subprocess.PIPE)
    fr = 0
    for i, sc in enumerate(scenes):
        n = int(round(b[i+1]*FPS)) - fr; sc["_T"] = n / FPS
        for j in range(n):
            AV[2] = fr + j; im = land(None if sc["k"] in ("text", "end", "chat", "noti", "call", "giay") else dx2.draw(sc, j/FPS, j/max(1, n)), sc, j/FPS)
            if HU2[0]:
                tt = j / FPS
                if i > 0 and PREV[0] is not None: im = _chuyen(PREV[0], im, tt, _kieu(scenes, i))
                _thanh_chuong(im, scenes, i, j / max(1, n))
                if j == n - 1: PREV[0] = im.copy()
            elif HU[0]:
                tt = j / FPS
                if i > 0 and tt < 0.22:   # punch-in 1.06 -> 1 đầu cảnh
                    z = 1.06 - 0.06 * dx2.ease(tt / 0.22); w2, h2 = int(LW * z), int(LH * z)
                    im = im.resize((w2, h2), Image.BILINEAR).crop(((w2 - LW)//2, (h2 - LH)//2, (w2 - LW)//2 + LW, (h2 - LH)//2 + LH))
                if i > 0 and tt < 0.28 and PREV[0] is not None:   # hoà trộn mượt với khung cuối cảnh trước
                    im = Image.blend(PREV[0], im, dx2.ease(tt / 0.28))
                _thanh_chuong(im, scenes, i, j / max(1, n))
                if j == n - 1: PREV[0] = im.copy()
            p.stdin.write(im.tobytes())
        fr += n
    p.stdin.close(); p.wait(); SUB_ON[0] = False
    _srt(scenes, b, os.path.join(OUT, key + ".srt"))
    try:  # QL1 11/11: mốc từng cảnh cho bước tự cắt Shorts (tu_cat_short.py)
        json.dump([dict(a=round(b[i], 2), e=round(b[i + 1], 2), k=sc.get("k"), cap=list(sc.get("cap") or []), ch=sc.get("ch", ""))
                   for i, sc in enumerate(scenes) if i < len(b) - 1], open(os.path.join(OUT, key + "_canh.json"), "w", encoding="utf-8"), ensure_ascii=False)
    except Exception as _e: print("canh.json: bo qua", _e, flush=True)
    af = ("highpass=f=120,acompressor=threshold=-26dB:ratio=4:attack=3:release=60:makeup=6,"
          "loudnorm=I=-14:TP=-1:LRA=7,alimiter=limit=0.95:attack=1:release=40:level=false")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", A, "-af", af, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-shortest", out])
    return b

# 3b) ảnh minh hoạ thật cho từng cảnh (Commons, miễn phí)
try:
    sys.path.insert(0, HERE); import anh
    anh.HAN[0] = time.time() + float(os.environ.get("HAN_ANH", 1200))
    kho = anh.Kho(WORK + "/anh"); chu_de = g.get("META", {}).get(key, {}).get("title", "") if isinstance(g.get("META"), dict) else ""
    nph = 0
    for i, sc in enumerate(scenes):
        sc["anh"] = raw[i].get("anh", ""); sc["say"] = raw[i].get("say", ""); sc["ch"] = raw[i].get("ch", "")
        ph = kho.cho(sc, chu_de)
        if ph is not None:
            _prep_ph(sc, ph); nph += 1
            if sc.get("k") in ("text", "end") and not raw[i].get("cta"):
                try:
                    import wave as _w0
                    with _w0.open("%s/%02d.wav" % (wd, i)) as _ww: _dur = _ww.getnframes() / _ww.getframerate()
                except Exception: _dur = len(sc.get("say", "").split()) / 3.3
                phs = [ph]
                _them = raw[i].get("anh_them") or []
                _file = str(raw[i].get("anh", "")).startswith("File:")
                for _k in range(min(3, int(_dur // land_text.SHOT))):
                    # 11/11 NV1: cảnh đã chọn đúng File: thì góc máy phụ chỉ lấy từ 'anh_them' (tránh ảnh lạc đề như cổng HUTA KATOWICE, sách báo cáo 1979);
                    # không có 'anh_them' thì giữ 1 ảnh, Ken Burns đổi góc máy
                    if _file:
                        if _k >= len(_them): break
                        p2 = kho.cho({"anh": _them[_k], "chat": 1}, chu_de)
                    else: p2 = kho.cho(sc, chu_de)
                    if p2 is None: break
                    phs.append(p2)
                land_text.prep(sc, phs)
    open(os.path.join(OUT, key + "_anh.txt"), "w", encoding="utf-8").write("Ảnh minh hoạ (Wikimedia Commons):\n" + "\n".join(kho.credit) + "\n")
    print(key, "anh minh hoa", nph, "/", len(scenes), flush=True)
except Exception as e:
    print("anh: bo qua", e, flush=True)

# 4) dựng + nhạc nền
rawmp4 = WORK + "/raw.mp4"; out = os.path.join(OUT, key + ".mp4")
for _i, _sc in enumerate(scenes): _sc.setdefault("say", raw[_i].get("say", "") if _i < len(raw) else "")
b = build_land(key, scenes, wd, rawmp4, tempo=1.0)
# 4b) hiệu ứng âm thanh (tự tổng hợp, không bản quyền): lướt khi chuyển cảnh, "ting" mở chương, "tada" kết
try:
    sys.path.insert(0, os.path.join(HERE, "story")); import am_thanh, wave as _wv
    ev = []
    for i in range(1, len(b) - 1):
        if not HU2[0] or raw[i].get("ch"): ev.append((max(0, b[i] - 0.12), "whoosh"))
    for i, r in enumerate(raw):
        if i < len(b) - 1 and r.get("ch"): ev.append((b[i] + 0.25, "ting"))
        elif i < len(b) - 1 and re.search(r"\d+[.,]?\d*\s*(%|tỷ|nghìn tỷ|lần)", r.get("say", "")): ev.append((b[i] + 0.35, "pop"))
    ev.append((max(0, b[-2] + 0.3), "tada"))
    # QL1 11/11: tiếng theo cảnh điện thoại / giấy tờ, khớp đúng nhịp bật của chat_ui
    try:
        import chat_ui as _cu
        for i, sc in enumerate(scenes):
            if i >= len(b) - 1: break
            k = sc.get("k"); t0 = b[i]
            if k == "chat":
                c = sc.get("chat", {}); tms = _cu._thoi_diem(sc, len(c.get("msgs", [])), c.get("co_san", 0))
                for j, tt in enumerate(tms):
                    if tt >= 0: ev.append((t0 + tt, "tin"))
            elif k == "noti":
                n = sc.get("noti", {}); tms = _cu._thoi_diem(sc, len(n.get("items", [])), n.get("co_san", 0))
                for j, tt in enumerate(tms):
                    if tt >= 0: ev.append((t0 + tt, "rung" if j == 0 else "tin"))
            elif k == "call" and not sc.get("co_san"):
                ev.append((t0 + 0.1, "chuong"))
                if sc.get("_T", 0) > 6: ev.append((t0 + 2.4, "rung"))
            elif k == "giay":
                g = sc.get("giay", {}); dk = g.get("dieu", []); tms = _cu._thoi_diem(sc, sum(1 for x in dk if x[1]))
                for tt in tms: ev.append((t0 + tt, "but"))
                if tms: ev.append((t0 + tms[-1] + 0.6, "dau"))
        ev = [e for e in ev if not (e[1] == "pop" and any(abs(e[0] - f[0]) < 0.5 and f[1] in ("tin", "rung", "chuong", "but") for f in ev))]
    except Exception as _e:
        print("sfx dien thoai: bo qua", _e, flush=True)
    x = am_thanh.track(b[-1] + 1, ev) * 0.28
    sf = WORK + "/sfx.wav"
    with _wv.open(sf, "w") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(44100); w.writeframes((x * 32767).astype("int16").tobytes())
    r2 = WORK + "/raw_sfx.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", rawmp4, "-i", sf, "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:normalize=0[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", r2], check=True)
    rawmp4 = r2; print(key, "sfx", len(ev), flush=True)
except Exception as e:
    print("sfx: bo qua", e, flush=True)
try: _NH = json.load(open(os.path.join(HERE, "queue", sys.argv[1], "meta.json"), encoding="utf-8")).get(key, {}).get("nhac", "")
except Exception: _NH = ""
_CANG = re.compile(r"sập|mất trắng|bốc hơi|cháy tài khoản|gọi ký quỹ|bán giải chấp|phá sản|vỡ nợ|lừa|kiện|bắt|trắng tay|nợ nần|hoảng|tháo chạy|lao dốc|thua lỗ", re.I)
_cg = [(b[i], b[i + 1]) for i, r in enumerate(raw) if i < len(b) - 1 and _CANG.search(r.get("say", ""))]
try: music.mix(rawmp4, b, out, lofi=(_NH == "lofi"), cang=_cg or None)
except TypeError: music.mix(rawmp4, b, out, lofi=(_NH == "lofi"))
print(key, "nhac cang", len(_cg), flush=True)
# 5) ảnh bìa = khung cảnh mở đầu lúc 3 giây
try:  # ảnh bìa đồng bộ chữ to (bia.py) – anh Huy chốt 5/11
    import bia as _bia
    _M = g.get("META", {}).get(key, {}) if isinstance(g.get("META"), dict) else {}
    if not _M.get("bia"):  # lấy bìa/tiêu đề từ meta.json của lô (bia_hook, tieu_de)
        try:
            _mj = json.load(open(os.path.join(QD, "meta.json"), encoding="utf-8")).get(key, {})
            _M = dict(_M, bia=_mj.get("bia_hook") or _mj.get("bia"), title=_M.get("title") or _mj.get("tieu_de", ""), badge=_M.get("badge") or _mj.get("badge"))
        except Exception: pass
    _sc0 = dict(raw[0]); _sc0["cap"] = scenes[0].get("cap")
    _bia.make(_sc0, _M, next((x["_ph"] for x in scenes if x.get("_ph") is not None), None), os.path.join(OUT, key + "_bia.png"))
except Exception as e:
    print("bia: dung khung cu", e, flush=True)
    land(dx2.draw(scenes[0], 3.0), scenes[0], 3.0).resize((1280, 720), Image.LANCZOS).save(os.path.join(OUT, key + "_bia.png"))
# 6) mốc chương thật theo giọng (cho mô tả YouTube)
ch = []
for i, sc in enumerate(raw):
    if sc.get("ch"):
        s = int(b[i]); ch.append("%d:%02d %s" % (s // 60, s % 60, sc["ch"]))
if ch and not ch[0].startswith("0:00"): ch[0] = "0:00" + ch[0][ch[0].index(" "):]
open(os.path.join(OUT, key + "_chuong.txt"), "w", encoding="utf-8").write("\n".join(ch) + "\n")
# 7) TỰ KIỂM CHẤT LƯỢNG (ghi KEY_qc.txt; NV3 không đăng nếu có dòng LỖI)
qc = list(_QCV)
try:
    fr = "/tmp/qc_%s.png" % key
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "0.3", "-i", out, "-frames:v", "1", fr])
    br = np.asarray(Image.open(fr).convert("L")).mean()
    if br < 22: qc.append("LỖI khung đầu quá tối (%.0f) – ảnh bìa tự động sẽ đen" % br)
    lu = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", lu); lv = float(m[-1]) if m else -99
    if lv < -24 or lv > -9: qc.append("LỖI âm lượng tổng %.1f LUFS (chuẩn -16 đến -12)" % lv)
    if b[-1] < 300: qc.append("CẢNH BÁO video chỉ %.0f giây (kênh chính nên 8–12 phút)" % b[-1])
    if not os.path.exists(os.path.join(OUT, key + ".srt")): qc.append("LỖI thiếu file phụ đề .srt")
    try:  # QL1 11/11: tự bắt lỗi số trên phụ đề (vd "6.000.001 tháng", "tháng 15", chữ số dính chữ)
        _tx = open(os.path.join(OUT, key + ".srt"), encoding="utf-8").read()
        for _m in re.findall(r"[^\n]*(?:\d{1,3}(?:\.\d{3}){2,}\d*\s*(?:triệu|tỷ|nghìn|tháng|năm)|tháng 1[3-9]\b|tháng [2-9]\d\b|\d[a-zA-ZÀ-ỹ]{2,})[^\n]*", _tx)[:5]:
            qc.append("LỖI phụ đề số nghi sai: " + _m.strip()[:80])
    except Exception: pass
    if not os.path.exists(os.path.join(OUT, key + "_bia.png")): qc.append("LỖI thiếu ảnh bìa")
except Exception as ex:
    qc.append("CẢNH BÁO không tự kiểm được: %s" % ex)
open(os.path.join(OUT, key + "_qc.txt"), "w", encoding="utf-8").write(("\n".join(qc) or "ĐẠT: khung đầu, âm lượng, phụ đề, ảnh bìa") + "\n")
print(key, "QC:", qc or "dat", flush=True)
print(key, "xong %.0fs, dai %.0fs" % (time.time() - t0, b[-1]), flush=True)
