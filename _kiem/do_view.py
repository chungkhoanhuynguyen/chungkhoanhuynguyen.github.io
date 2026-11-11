# Đo view miễn phí (thay vidIQ) – chạy trên GitHub Actions bằng yt-dlp, không cần API key.
# Ra: data/view/hist.json (lịch sử view từng video), data/view/bao_cao.md (top/bottom 7 ngày),
#     data/view/xu_huong.md (video tài chính tiếng Việt nhiều view trong tuần – thay vidIQ trending/outliers).
import json, os, subprocess, statistics, datetime as dt

KENH = {
    "chinh": "https://www.youtube.com/channel/UCnRCl2_UcgVVs82d1_CcA8A",
    "@5 Vĩ Mô Nóng": "https://www.youtube.com/channel/UCbeiGmJ1yZL4kLE5bwf471g",
    "@6 Đầu Tư Tích Sản": "https://www.youtube.com/channel/UCGImFAPw_IG_Ov7yomYn84g",
    "@2 Cổ Phiếu Mỗi Ngày": "https://www.youtube.com/@chungkhoanhuynguyen2",
    "@3 Huy Invest": "https://www.youtube.com/@chungkhoanhuynguyen3",
    "@4 Lướt Sóng Thần": "https://www.youtube.com/@chungkhoanhuynguyen4",
    "@7 Y3 Vĩ Mô": "https://www.youtube.com/@chungkhoanhuynguyen7",
    "@8 Y2 Soi BCTC": "https://www.youtube.com/@chungkhoanhuynguyen8",
}
TU_KHOA = ["chứng khoán", "vĩ mô việt nam", "giá vàng", "lãi suất ngân hàng", "kinh tế việt nam", "bất động sản", "cổ phiếu"]
D = "data/view"
os.makedirs(D, exist_ok=True)
hom_nay = dt.date.today().isoformat()


def ytdlp(url, n=None):
    cmd = ["yt-dlp", "--flat-playlist", "-J", "--no-warnings", "--extractor-args", "youtubetab:approximate_date"]
    if n:
        cmd += ["--playlist-end", str(n)]
    try:
        out = subprocess.run(cmd + [url], capture_output=True, text=True, timeout=300).stdout
        return json.loads(out).get("entries") or []
    except Exception as e:
        print("loi", url, e)
        return []


hist = json.load(open(f"{D}/hist.json")) if os.path.exists(f"{D}/hist.json") else {}
dem = {}
for ten, url in KENH.items():
    dem[ten] = 0
    for tab, loai in (("/videos", "dai"), ("/shorts", "short")):
        for e in ytdlp(url + tab, 300):
            vid, v = e.get("id"), e.get("view_count")
            if not vid or v is None:
                continue
            h = hist.setdefault(vid, {"t": e.get("title", ""), "k": ten, "l": loai, "first": hom_nay, "v": {}})
            h["t"] = e.get("title", h["t"])
            if e.get("upload_date"):
                h["up"] = e["upload_date"]
            h["v"][hom_nay] = v
            dem[ten] += 1
json.dump(hist, open(f"{D}/hist.json", "w"), ensure_ascii=False, separators=(",", ":"))


def tang(h, ngay):
    ds = sorted(h["v"])
    if not ds:
        return None
    moc = (dt.date.fromisoformat(hom_nay) - dt.timedelta(days=ngay)).isoformat()
    cu = [d for d in ds if d <= moc]
    goc = h["v"][cu[-1]] if cu else 0 if h["first"] > moc else None
    return None if goc is None else h["v"][ds[-1]] - goc


L = [f"# Đo view {hom_nay} (yt-dlp, miễn phí)\n", "Số video đọc được: " + ", ".join(f"{k} {v}" for k, v in dem.items()) + "\n"]
for ten in KENH:
    for loai in ("dai", "short"):
        rows = [(tang(h, 7), h) for h in hist.values() if h["k"] == ten and h["l"] == loai and hom_nay in h["v"]]
        rows = [(g, h) for g, h in rows if g is not None]
        if not rows:
            continue
        rows.sort(key=lambda x: -x[0])
        tong = sum(g for g, _ in rows)
        tv = statistics.median([g for g, _ in rows])
        L.append(f"\n## {ten} – {'video dài' if loai == 'dai' else 'Shorts'}: +{tong} view 7 ngày, trung vị +{tv:g}/video")
        for g, h in rows[:5]:
            L.append(f"- TOP +{g} | {h['v'][hom_nay]} tổng | {h['t'][:80]}")
        for g, h in rows[-3:] if len(rows) > 8 else []:
            L.append(f"- ĐÁY +{g} | {h['t'][:80]}")
open(f"{D}/bao_cao.md", "w").write("\n".join(L) + "\n")

# Xu hướng tuần: tìm kiếm YouTube lọc "tuần này" (sp=EgIIAw%3D%3D), xếp theo view
X, thay = [], set()
for kw in TU_KHOA:
    url = "https://www.youtube.com/results?search_query=" + kw.replace(" ", "+") + "&sp=EgIIAw%253D%253D"
    for e in ytdlp(url, 40):
        if e.get("id") in thay or e.get("view_count") is None:
            continue
        thay.add(e["id"])
        X.append((e["view_count"], e.get("channel") or e.get("uploader") or "", e.get("title", ""), e.get("duration"), kw))
X.sort(key=lambda x: -x[0])
M = [f"# Xu hướng YouTube tài chính tiếng Việt – tuần tới {hom_nay} (yt-dlp, miễn phí)\n",
     "| view | kênh | tiêu đề | dài (s) | từ khoá |", "|---|---|---|---|---|"]
for v, ch, t, du, kw in X[:30]:
    M.append(f"| {v} | {ch[:30]} | {t[:90].replace('|', '/')} | {du or ''} | {kw} |")
open(f"{D}/xu_huong.md", "w").write("\n".join(M) + "\n")
print("xong", dem, len(X))
