# Đồng bộ mọi video trong _video/queue/*/ vào thư viện bài học web (_hoc/videos.json) + gắn link bài học vào mô tả.
# Chạy: python _hoc/dong_bo_queue.py  (idempotent: không ghi đè id YouTube đã điền).
# Trang /hoc/<slug>.html chỉ được hoc.py xuất bản khi entry có "id" (video đã lên YouTube).
import json, glob, os, re, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = "https://chungkhoanhuynguyen.com"
SERI_KENH = {"HI": "Huy Invest – Đầu tư thông minh", "K2": "Cổ phiếu mỗi ngày", "LST": "Lịch sử & bài học thị trường",
             "TS": "Đầu tư tích sản", "Y2": "Soi báo cáo tài chính", "Y3": "Vĩ mô dễ hiểu", "TN": "Vĩ mô nóng", "KC": "Kiến thức đầu tư nền tảng"}
def pre(k):
    for p in ("LST", "Y2", "Y3", "K2", "HI", "TS", "TN", "KC", "CH"):
        if k.startswith(p): return p
    return k[:2]
def slugify(s):
    s = s.replace("đ", "d").replace("Đ", "D"); s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-"); return s[:70].rsplit("-", 1)[0] if len(s) > 70 else s
def say_of(src_dir, key):
    f = os.path.join(src_dir, "video_dai.py")
    if not os.path.exists(f): return []
    ns = {}
    try: exec(open(f, encoding="utf-8").read(), ns)
    except Exception: return []
    return (ns.get("S") or {}).get(key, [])
VP = os.path.join(ROOT, "_hoc", "videos.json")
V = json.load(open(VP, encoding="utf-8")); have = {v["k"]: v for v in V}; slugs = {v["slug"] for v in V}
them = 0
for mf in sorted(glob.glob(os.path.join(ROOT, "_video/queue/*/meta.json"))):
    d = os.path.dirname(mf)
    if os.path.basename(d) == "test": continue
    M = json.load(open(mf, encoding="utf-8")); doi = False
    for k, m in M.items():
        if not isinstance(m, dict) or not (m.get("tieu_de") or m.get("title")): continue
        td = m.get("tieu_de") or m.get("title")
        p = pre(k); seri = m.get("seri") if p in ("CH",) and m.get("seri") else SERI_KENH.get(p, m.get("seri") or "Kiến thức đầu tư nền tảng")
        if p == "TN": seri = "Vĩ mô nóng"
        if k in have: slug = have[k]["slug"]
        else:
            slug = slugify(td); base = slug; i = 2
            while slug in slugs: slug = f"{base}-{i}"; i += 1
            sc = say_of(d, k); body = []
            for s in sc:
                if s.get("k") in ("end",): continue
                if s.get("ch") and s.get("moc") and s is not sc[0]: body.append(["h2", re.sub(r"^Chương \d+ – ", "", s["ch"])])
                if s.get("say"): body.append(["p", s["say"]])
            sumr = (m.get("mo_ta") or "").split("\n\n")[0]
            v = {"k": k, "id": "", "d": m.get("ngay") or "", "title": td, "h1": td, "slug": slug, "series": seri,
                 "sum": sumr, "intro": (sc[0].get("say", "") if sc else sumr), "body": body,
                 "src": "Số liệu theo dữ liệu tổng hợp tại chungkhoanhuynguyen.com và nguồn ghi trong video." + (" Nguồn: " + m["nguon"] if m.get("nguon") else ""),
                 "img": "", "tags": (m.get("tags") or [])[:8], "kenh": m.get("kenh", "")}
            V.append(v); have[k] = v; slugs.add(slug); them += 1
        link = f"{B}/hoc/{slug}.html"
        if link not in (m.get("mo_ta") or ""):
            m["mo_ta"] = (m.get("mo_ta") or "").rstrip() + f"\n\n📚 Seri {seri} – bài viết, bảng số và tài liệu kèm video: {link}\n📂 Thư viện bài học: {B}/hoc/"
            doi = True
        if m.get("seri_web") != seri: m["seri_web"] = seri; m["link_web"] = link; doi = True
        if m.get("fb_post") and "{LINK}" in m["fb_post"] and link not in m["fb_post"]:
            m["fb_post"] = m["fb_post"].rstrip() + f"\n📚 Tài liệu: {link}"; doi = True
    if doi: json.dump(M, open(mf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(V, open(VP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("them", them, "tong", len(V))
