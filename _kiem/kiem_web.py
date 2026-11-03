# Tự kiểm web mỗi lần đẩy (miễn phí, chạy trên GitHub): link nội bộ hỏng, link lỗi kiểu "{...}", sitemap tụt trang,
# trang thiếu tiêu đề/mô tả/canonical, tiêu đề > 65 hoặc mô tả > 160 ký tự, trang trùng tiêu đề. Có lỗi -> báo đỏ.
import os, re, sys, glob, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages = [p for p in glob.glob(ROOT + "/**/*.html", recursive=True) if "/_" not in p.replace(ROOT, "") and "/node_modules/" not in p]
loi, canh = [], []
def exists(href, src):
    u = href.split("#")[0].split("?")[0]
    if not u or u.startswith(("http", "mailto:", "tel:", "javascript:", "data:", "//")): return True
    if "'" in u or "+" in u: return True                      # link tạo bằng JS trong trang
    path = os.path.join(ROOT, u.lstrip("/")) if u.startswith("/") else os.path.join(os.path.dirname(src), u)
    return os.path.isfile(path) or os.path.isfile(os.path.join(path, "index.html")) or os.path.isfile(path + ".html")
titles = {}
for p in pages:
    s = open(p, encoding="utf-8", errors="ignore").read(); rel = p.replace(ROOT, "")
    for h in re.findall(r'href="([^"]*)"', s):
        if "{" in h or "}" in h: loi.append(f"{rel}: link lỗi mẫu chưa điền {h[:60]}")
        elif not exists(html.unescape(h), p): loi.append(f"{rel}: link nội bộ hỏng {h[:80]}")
    if "<meta name=\"robots\" content=\"noindex" in s or rel.startswith(("/bao-cao-2026", "/404")): continue
    t = re.search(r"<title>([^<]*)</title>", s); d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not t: loi.append(f"{rel}: thiếu <title>"); continue
    tt = html.unescape(t.group(1)).replace(" | Chứng Khoán Huy Nguyễn", "")
    if not d: loi.append(f"{rel}: thiếu mô tả")
    elif len(html.unescape(d.group(1))) > 165: canh.append(f"{rel}: mô tả dài {len(d.group(1))} ký tự")
    if len(tt) > 70: canh.append(f"{rel}: tiêu đề dài {len(tt)} ký tự")
    if 'rel="canonical"' not in s: canh.append(f"{rel}: thiếu canonical")
    titles.setdefault(tt, []).append(rel)
for t, ps in titles.items():
    if len(ps) > 1: canh.append(f"trùng tiêu đề '{t[:50]}': {', '.join(ps[:3])}")
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read(); n = sm.count("<loc>")
MIN = int(open(os.path.join(ROOT, "_kiem/sitemap_min.txt")).read().strip()) if os.path.exists(os.path.join(ROOT, "_kiem/sitemap_min.txt")) else 0
if n < MIN * 0.95: loi.append(f"sitemap chỉ còn {n} URL (mốc {MIN}) – có thể bị ghi đè thiếu")
for u in re.findall(r"<loc>https://chungkhoanhuynguyen\.com(/[^<]*)</loc>", sm):
    if not exists(u, ROOT + "/index.html"): loi.append(f"sitemap trỏ tới trang không tồn tại: {u}")
print(f"Đã kiểm {len(pages)} trang, sitemap {n} URL: {len(loi)} LỖI, {len(canh)} cảnh báo")
for x in loi[:80]: print("LỖI   ", x)
for x in canh[:40]: print("CẢNH BÁO", x)
open(os.path.join(ROOT, "_kiem/ket_qua.txt"), "w", encoding="utf-8").write("\n".join([f"{len(loi)} lỗi, {len(canh)} cảnh báo"] + loi + canh) + "\n")
sys.exit(1 if loi else 0)
