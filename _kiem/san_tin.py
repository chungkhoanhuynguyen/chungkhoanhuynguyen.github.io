# Săn tin nóng miễn phí (QL1 12/11/2026) – chạy GitHub Actions mỗi sáng, thay cho tìm web tốn token.
# Ra: data/tin/<ngày>.md + data/tin/moi_nhat.md: tin thế giới/kinh tế mới nhất từ RSS báo lớn, chấm điểm "sốc" để NV1B chọn đề tài kênh C (@2).
import os, re, html, datetime as dt, urllib.request, xml.etree.ElementTree as ET
NGUON = {
 "VnExpress Thế giới": "https://vnexpress.net/rss/the-gioi.rss",
 "VnExpress Kinh doanh": "https://vnexpress.net/rss/kinh-doanh.rss",
 "Tuổi Trẻ Thế giới": "https://tuoitre.vn/rss/the-gioi.rss",
 "Tuổi Trẻ Kinh doanh": "https://tuoitre.vn/rss/kinh-doanh.rss",
 "VnEconomy": "https://vneconomy.vn/rss/home.rss",
 "Thanh Niên Thế giới": "https://thanhnien.vn/rss/the-gioi.rss",
}
SOC = ["chiến tranh", "hạt nhân", "khủng hoảng", "sụp", "vỡ nợ", "phá sản", "kỷ lục", "lao dốc", "tăng vọt", "cấm", "trừng phạt",
       "thiếu", "tích trữ", "lạm phát", "giá vàng", "giá dầu", "tỷ giá", "lãi suất", "Fed", "Iran", "Trung Quốc", "Mỹ", "thuế",
       "bơm tiền", "ngân hàng", "thảm hoạ", "động đất", "bão", "dịch", "AI", "tỷ USD", "nghìn tỷ"]
def lay(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
        for it in root.iter("item"):
            t = html.unescape((it.findtext("title") or "").strip()); l = (it.findtext("link") or "").strip()
            d = re.sub(r"<[^>]+>", " ", html.unescape(it.findtext("description") or "")); d = re.sub(r"\s+", " ", d).strip()
            yield t, l, d[:220], it.findtext("pubDate") or ""
    except Exception as e:
        print("loi", url, e)
ds = []
for ten, url in NGUON.items():
    for t, l, d, p in lay(url):
        diem = sum(2 if k.lower() in t.lower() else (1 if k.lower() in d.lower() else 0) for k in SOC)
        ds.append((diem, ten, t, l, d, p))
seen = set(); top = []
for x in sorted(ds, key=lambda x: -x[0]):
    k = x[2][:40]
    if k in seen: continue
    seen.add(k); top.append(x)
hom = (dt.datetime.utcnow() + dt.timedelta(hours=7)).strftime("%Y-%m-%d")
os.makedirs("data/tin", exist_ok=True)
L = [f"# Tin nóng {hom} (tự động, {len(ds)} tin từ {len(NGUON)} nguồn) – NV1B chọn 1–2 tin điểm cao làm kênh C", ""]
for diem, ten, t, l, d, p in top[:25]:
    L.append(f"- **[{diem}] {t}** – {ten} · {p[:16]}\n  {d}\n  {l}")
open(f"data/tin/{hom}.md", "w", encoding="utf-8").write("\n".join(L)); open("data/tin/moi_nhat.md", "w", encoding="utf-8").write("\n".join(L))
print("ok", len(ds), "tin")
