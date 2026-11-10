# Tạo trang bài học /hoc/*.html từ _hoc/videos.json cho các video đã ra mắt + cập nhật sitemap.xml
# Chạy: python hoc.py   (GitHub Actions chạy mỗi ngày 20:10 giờ VN)
import json, os, html, datetime
B = "https://chungkhoanhuynguyen.com"
YT = "https://www.youtube.com/@chungkhoanhuynguyen"
ROOT = os.path.dirname(os.path.abspath(__file__))
V = json.load(open(os.path.join(ROOT, "_hoc/videos.json"), encoding="utf-8"))
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
def live(v):
    # chỉ xuất bản khi đã có id YouTube và đã tới ngày ra mắt (video từ hàng chờ có id rỗng)
    return bool(v.get("id")) and bool(v.get("d")) and now >= datetime.datetime.fromisoformat(v["d"] + "T20:00:00")
R = [v for v in V if live(v)]
e = lambda s: html.escape(s or "", quote=True)
def dmy(d): y, m, dd = d.split("-"); return "%s/%s/%s" % (int(dd), int(m), y)
SER = ["LS", "TG", "BF", "KT"]

CSS = """:root{--bg:#f6f4f8;--panel:#fff;--line:#e3dfe9;--fg:#1f1b26;--mute:#5f5a69;--acc:#6a2d86;--gold:#b8892f}
@media (prefers-color-scheme:dark){:root{--bg:#070b14;--panel:#0e1526;--line:#1f2b45;--fg:#f1ead9;--mute:#9aa4bb;--acc:#c77dff;--gold:#d9b26a}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.75 "Be Vietnam Pro",system-ui,sans-serif}
a{color:var(--acc)}.top{position:sticky;top:0;z-index:5;background:var(--panel);border-bottom:1px solid var(--line)}
.top .in{max-width:880px;margin:auto;padding:10px 16px;display:flex;gap:16px;align-items:center;justify-content:space-between}
.brand{font-weight:800;letter-spacing:.04em;text-decoration:none;color:var(--fg);font-size:15px}.brand b{color:var(--gold)}
.nav{display:flex;gap:14px;font-size:14px;font-weight:600;white-space:nowrap}.brand{white-space:nowrap}.nav a{text-decoration:none}
main{max-width:880px;margin:auto;padding:20px 16px 48px}.bc{font-size:13px;color:var(--mute)}.bc a{color:var(--mute)}
h1{font:900 clamp(26px,5vw,40px)/1.2 "Playfair Display",Georgia,serif;margin:10px 0 8px}h2{font:800 24px/1.3 "Playfair Display",Georgia,serif;margin:36px 0 8px;padding-top:8px;border-top:1px solid var(--line)}
h3{font-size:18px;margin:22px 0 4px}.meta{color:var(--mute);font-size:14px}
.vid{position:relative;aspect-ratio:16/9;margin:18px 0;border-radius:12px;overflow:hidden;background:#000}.vid iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.sum{background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:10px;padding:14px 16px;margin:16px 0}
blockquote{margin:18px 0;padding:10px 16px;border-left:4px solid var(--acc);background:var(--panel);border-radius:8px;font-style:italic}
.fimg{margin:18px 0}.fimg img{width:100%;max-width:620px;height:auto;border-radius:12px;border:1px solid #ddd;display:block}.fimg figcaption{font-size:14px;color:var(--mute);margin-top:6px}.toc{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 16px;margin:16px 0;font-size:15px}.toc ol{margin:6px 0 0;padding-left:20px;line-height:1.7}.step{font-size:13px;font-weight:700;color:var(--gold);letter-spacing:.5px;text-transform:uppercase}.gp{margin:26px 0 8px;padding-top:14px;border-top:1px solid var(--line)}.gp h2{margin:0 0 2px}.gp p{margin:0 0 8px;color:var(--mute);font-size:14px}.f0l li{margin:0 0 12px}.cta{display:flex;flex-wrap:wrap;gap:10px;margin:28px 0}.cta p{flex-basis:100%;margin:0}.f0l{padding-left:22px}.f0l li{margin:0 0 16px;line-height:1.5}.f0l small{color:var(--mute)}article ul,article ol{line-height:1.7}.btn{display:inline-block;padding:10px 16px;border-radius:999px;font-weight:700;text-decoration:none;font-size:15px}
.b1{background:#c4302b;color:#fff}.b2{border:1px solid var(--line);background:var(--panel);color:var(--fg)}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:24px 0}.pn a{display:block;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 12px;text-decoration:none;color:var(--fg);font-size:14px}.pn small{color:var(--mute);display:block}
.src{font-size:13px;color:var(--mute);border-top:1px solid var(--line);margin-top:28px;padding-top:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin:12px 0 28px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;color:var(--fg)}.card img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}.card span{display:block;padding:10px 12px;font-weight:600;font-size:15px;line-height:1.45}
footer{text-align:center;color:var(--mute);font-size:13px;padding:24px 16px;border-top:1px solid var(--line)}
@media(max-width:560px){.pn{grid-template-columns:1fr}.nav a.hide{display:none}.brand{min-width:0;overflow:hidden;text-overflow:ellipsis}.brand{font-size:13px}.nav{gap:10px;font-size:13px}.top .in{gap:8px}}
.tb{overflow-x:auto;margin:14px 0}.tb table{border-collapse:collapse;width:100%;font-size:15px;line-height:1.5}.tb th,.tb td{border-bottom:1px solid var(--line);padding:8px 10px;text-align:right;white-space:nowrap}.tb th:first-child,.tb td:first-child{text-align:left;white-space:normal}.tb th{color:var(--mute);font-weight:600}"""

def _ngan(t, n=64):
    t = t.strip()
    if len(t) <= n: return t
    for sep in (": ", " – ", " - ", ", "):
        if sep in t and len(t.split(sep)[0]) >= 25 and len(t.split(sep)[0]) <= n: return t.split(sep)[0]
    return t[:n].rsplit(" ", 1)[0].rstrip(",:–-") + "…"
def head(title, desc, url, img, ld):
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data: https://i.ytimg.com; frame-src https://www.youtube-nocookie.com; object-src 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests"><meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{img}"><meta property="og:locale" content="vi_VN"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/fav-32.png"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;800&family=Playfair+Display:wght@800;900&display=swap">
<style>{CSS}</style><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>
<header class="top"><div class="in"><a class="brand" href="/">HUY NGUYỄN <b>·</b> CHỨNG KHOÁN</a><nav class="nav"><a href="/#timnhanh">🔎 Tìm</a><a href="/mo-tai-khoan-chung-khoan.html">Mở TK</a><a href="/ma/">Mã CP</a><a href="/f0/">F0</a><a href="/hoc/">Bài học</a><a class="hide" href="/">Bảng giá &amp; định giá</a><a href="{YT}?sub_confirmation=1" rel="noopener">YouTube</a></nav></div></header>"""

FOOT = """<footer>© Chứng Khoán Huy Nguyễn · <a href="/">chungkhoanhuynguyen.com</a><br>Nội dung chia sẻ kiến thức và quan điểm cá nhân, không phải khuyến nghị mua bán.<br><a href="/gioi-thieu.html">Giới thiệu</a> · <a href="/lien-he.html">Liên hệ</a> · <a href="/chinh-sach-bao-mat.html">Chính sách bảo mật</a></footer></body></html>"""

def desc_of(v):
    s = v["sum"].replace("\n", " ")
    return s if len(s) <= 158 else s[:155].rsplit(" ", 1)[0] + "…"

os.makedirs(os.path.join(ROOT, "hoc"), exist_ok=True)
keep = set()
for v in R:
    url = f"{B}/hoc/{v['slug']}.html"; thumb = f"https://i.ytimg.com/vi/{v['id']}/maxresdefault.jpg"
    same = [x for x in R if x.get("series") == v.get("series")]; i = same.index(v)
    prv = same[i - 1] if i > 0 else None; nxt = same[i + 1] if i + 1 < len(same) else None
    up = v["d"] + "T20:00:00+07:00"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B + "/"},
            {"@type": "ListItem", "position": 2, "name": "Thư viện bài học", "item": B + "/hoc/"},
            {"@type": "ListItem", "position": 3, "name": v["h1"], "item": url}]},
        {"@type": "Article", "headline": v["h1"][:110], "description": desc_of(v), "image": [thumb], "datePublished": up, "dateModified": up,
         "inLanguage": "vi", "mainEntityOfPage": url, "keywords": ", ".join(v["tags"]),
         "author": {"@type": "Organization", "name": "Chứng Khoán Huy Nguyễn", "url": B + "/"},
         "publisher": {"@type": "Organization", "name": "Chứng Khoán Huy Nguyễn", "logo": {"@type": "ImageObject", "url": B + "/img/icon-512.png"}}},
        {"@type": "VideoObject", "name": v["title"][:100], "description": v["sum"], "thumbnailUrl": [thumb, f"{B}/img/yt/{v['k']}.jpg"],
         "uploadDate": up, "embedUrl": f"https://www.youtube.com/embed/{v['id']}", "url": f"https://www.youtube.com/watch?v={v['id']}", "inLanguage": "vi"}]}
    p = [head(_ngan(v["h1"]) + " | Chứng Khoán Huy Nguyễn", desc_of(v)[:158], url, thumb, ld), "<main><article>",
         f'<div class="bc"><a href="/">Trang chủ</a> › <a href="/hoc/">Thư viện bài học</a> › {e(v["series"])}</div>',
         f'<h1>{e(v["h1"])}</h1><div class="meta">{e(v["series"])} · {dmy(v["d"])} · Video + bài viết</div>',
         f'<div class="vid"><iframe src="https://www.youtube-nocookie.com/embed/{v["id"]}?rel=0" title="{e(v["h1"])}" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>',
         f'<div class="sum"><b>Tóm tắt:</b> {e(v["sum"])}</div>']
    if v["intro"]: p.append(f"<p>{e(v['intro'])}</p>")
    for t, s in v["body"]:
        p.append({"h2": "<h2>%s</h2>", "h3": "<h3>%s</h3>", "q": "<blockquote>%s</blockquote>"}.get(t, "<p>%s</p>") % e(s))
    p.append(f'<div class="cta"><a class="btn b1" href="{YT}?sub_confirmation=1" rel="noopener">Đăng ký kênh YouTube</a><a class="btn b2" href="https://www.youtube.com/watch?v={v["id"]}" rel="noopener">Xem trên YouTube</a><a class="btn b2" href="/">Xem bảng giá &amp; định giá</a></div>')
    if prv or nxt:
        p.append('<nav class="pn">' + (f'<a href="/hoc/{prv["slug"]}.html"><small>← Bài trước</small>{e(prv["h1"])}</a>' if prv else "<span></span>") +
                 (f'<a href="/hoc/{nxt["slug"]}.html"><small>Bài tiếp →</small>{e(nxt["h1"])}</a>' if nxt else "<span></span>") + "</nav>")
    if v["src"] or v["img"]:
        p.append('<div class="src">' + (f"<b>Nguồn số liệu:</b> {e(v['src'])}<br>" if v["src"] else "") + (f"<b>Ảnh trong video:</b> {e(v['img'])}" if v["img"] else "") + "</div>")
    p.append("</article></main>" + FOOT)
    fn = f"hoc/{v['slug']}.html"; keep.add(fn)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write("\n".join(p))

# Trang mục lục
NAME = {"LS": "Lịch sử chứng khoán Việt Nam", "TG": "Lịch sử chứng khoán thế giới", "BF": "Tư duy nhà đầu tư huyền thoại", "KT": "Kiến thức đầu tư nền tảng"}
url = B + "/hoc/"
ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Thư viện bài học chứng khoán", "url": url, "inLanguage": "vi",
      "hasPart": [{"@type": "Article", "headline": v["h1"][:110], "url": f"{B}/hoc/{v['slug']}.html"} for v in R]}
p = [head("Thư viện bài học chứng khoán cho người mới | Chứng Khoán Huy Nguyễn",
          "Học chứng khoán từ đầu: lịch sử thị trường, tư duy nhà đầu tư huyền thoại, đọc báo cáo tài chính, định giá cổ phiếu. Mỗi bài có video và bài viết.",
          url, B + "/img/og.png", ld), "<main>",
     '<div class="bc"><a href="/">Trang chủ</a> › Thư viện bài học</div><h1>Thư viện bài học chứng khoán</h1>',
     '<p class="meta">Kiến thức chứng khoán cho người mới bắt đầu, kể bằng câu chuyện và số liệu có nguồn. Mỗi tối 20:00 có một bài mới.</p>']
_TS = [x for x in json.load(open(os.path.join(ROOT, "_f0/bai.json"), encoding="utf-8")) if x.get("grp") == 7]
if _TS:
    p.append('<section class="toc" style="margin:18px 0"><b>Chuyên đề có ảnh minh họa: Tích sản &amp; quản trị vốn</b><p class="meta" style="margin:4px 0 6px">Kiến thức quan trọng nhất để sống sót lâu dài trên thị trường.</p><ol>' + "".join(f'<li><a href="/f0/{x["slug"]}.html">{e(x["title"])}</a></li>' for x in _TS) + '</ol></section>')
_SO = ["Lệnh thật & bài học", "Vĩ mô nóng"] + [NAME[x] for x in SER]
for sn in _SO + sorted({v["series"] for v in R} - set(_SO)):
    L = [v for v in R if (v.get("series") or NAME.get(v["k"][:2])) == sn]
    if not L: continue
    p.append(f"<h2>{e(sn)}</h2><div class=\"grid\">" + "".join(
        f'<a class="card" href="/hoc/{v["slug"]}.html"><img src="/img/yt/{v["k"]}.jpg" alt="{e(v["h1"])}" width="480" height="270" loading="lazy"><span>{e(v["h1"])}</span></a>' for v in L) + "</div>")
p.append(f'<div class="cta"><a class="btn b1" href="{YT}?sub_confirmation=1" rel="noopener">Đăng ký kênh để không lỡ bài mới</a></div></main>' + FOOT)
open(os.path.join(ROOT, "hoc/index.html"), "w", encoding="utf-8").write("\n".join(p))

# Xóa trang không còn trong danh sách (đổi slug)
for f in os.listdir(os.path.join(ROOT, "hoc")):
    if f != "index.html" and "hoc/" + f not in keep: os.remove(os.path.join(ROOT, "hoc", f))


# ---- Cẩm nang F0 (/f0/): bài viết chuẩn SEO cho người mới, nội dung trong _f0/bai.json ----
F = json.load(open(os.path.join(ROOT, "_f0/bai.json"), encoding="utf-8"))
GN = {1: "Bắt đầu", 2: "Giao dịch", 3: "Phân tích cơ bản", 4: "Phân tích kỹ thuật", 5: "Quản trị rủi ro & tâm lý", 6: "Sản phẩm khác", 7: "Tích sản & quản trị vốn", 8: "Vĩ mô & ngành"}
GD = {1: "Chứng khoán là gì, mở tài khoản, nạp tiền", 2: "Đọc bảng giá, đặt lệnh, phí và thời gian tiền về", 3: "Đọc báo cáo tài chính, định giá, chọn cổ phiếu", 4: "Xu hướng, đường MA, RSI, dòng tiền", 5: "Cắt lỗ, margin, phân bổ vốn, kiểm soát cảm xúc", 6: "ETF, chứng chỉ quỹ, phái sinh, trái phiếu, IPO", 7: "Tích sản từ A đến Z, rủi ro, quản trị vốn: kiến thức quan trọng nhất", 8: "Giá dầu, lãi suất, tỷ giá, chính sách tác động tới cổ phiếu"}
F = sorted(F, key=lambda x: x.get("grp", 1))
FM = {x["slug"]: x for x in F}
# Trang trụ cột (hub) cho từng cụm từ khóa + từ điển thuật ngữ (NV2 2/11)
HUB = {1: "bat-dau-chung-khoan", 2: "giao-dich-chung-khoan", 3: "phan-tich-co-ban", 4: "phan-tich-ky-thuat", 5: "quan-tri-rui-ro-va-tam-ly", 6: "san-pham-chung-khoan", 7: "tich-san-co-phieu", 8: "vi-mo-va-nganh"}
HT = {1: "Chứng khoán cho người mới bắt đầu: kiến thức nền tảng", 2: "Giao dịch chứng khoán: đặt lệnh, bảng giá, phí, T+2", 3: "Phân tích cơ bản cổ phiếu: đọc BCTC, P/E, P/B, ROE", 4: "Phân tích kỹ thuật cho người mới: nến, MA, RSI, MACD", 5: "Quản trị rủi ro và tâm lý đầu tư chứng khoán", 6: "Sản phẩm chứng khoán: ETF, quỹ, phái sinh, trái phiếu", 7: "Tích sản cổ phiếu: đầu tư dài hạn từ A đến Z", 8: "Vĩ mô và ngành: lãi suất, tỷ giá, giá dầu, cổ phiếu"}
HI = {1: "Bắt đầu từ con số 0: chứng khoán là gì, cổ phiếu là gì, mở tài khoản và nạp tiền thế nào, nên đầu tư bao nhiêu và cách tránh lừa đảo. Đây là nhóm bài nên đọc đầu tiên trước khi đặt lệnh đầu tiên.",
      2: "Mọi thứ cần biết khi bắt đầu mua bán: giờ giao dịch, các loại lệnh, đọc bảng giá, biên độ trần sàn, phí và thuế, thời gian tiền và cổ phiếu về tài khoản, khối ngoại, tự doanh.",
      3: "Phân tích cơ bản giúp hiểu doanh nghiệp bạn sở hữu: đọc ba báo cáo tài chính, các chỉ số định giá P/E, P/B, PEG, EV/EBITDA, chỉ số hiệu quả ROE, ROA và các chỉ số riêng của ngân hàng như NIM, CASA, nợ xấu.",
      4: "Phân tích kỹ thuật dùng biểu đồ giá và khối lượng để tìm xu hướng và vùng giá hợp lý: nến Nhật, hỗ trợ kháng cự, đường MA, RSI, MACD, Bollinger, các mô hình giá. Nên dùng kết hợp với phân tích cơ bản.",
      5: "Giữ được vốn quan trọng hơn kiếm lãi nhanh: cắt lỗ, margin và call margin, phân bổ vốn, kỷ luật, các bẫy tâm lý như FOMO, bắt đáy, và những cờ đỏ cần tránh.",
      6: "Ngoài cổ phiếu còn nhiều sản phẩm khác: quỹ ETF, quỹ mở, chứng chỉ quỹ, chứng quyền, hợp đồng tương lai VN30, trái phiếu, IPO. Mỗi loại có rủi ro và cách dùng khác nhau.",
      7: "Tích sản là con đường bền vững cho người đi làm: mua đều cổ phiếu tốt, tái đầu tư cổ tức, để lãi kép làm việc. Chuyên đề có nhiều bài về tích sản cổ phiếu ngân hàng.",
      8: "Giá cổ phiếu chịu tác động của lãi suất, tỷ giá, lạm phát, giá dầu, giá thép và chính sách. Nhóm bài này giải thích từng mối liên hệ bằng số liệu thật."}
HP = lambda g: "/f0/chu-de-%s.html" % HUB[g]
FP = lambda x: ("/%s.html" if x.get("root") else "/f0/%s.html") % x["slug"]
os.makedirs(os.path.join(ROOT, "f0"), exist_ok=True)
fkeep = set()
FDATE = "2026-10-30"
try: YTM = json.load(open(os.path.join(ROOT, "_f0/yt.json"), encoding="utf-8"))
except Exception: YTM = {}
def ytblk(vs):
    if not vs: return ""
    h = ['<h2>Video giải thích chi tiết</h2>']
    for v in vs[:2]:
        h.append(f'<figure class="fimg"><a href="https://www.youtube.com/watch?v={e(v[0])}" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/{e(v[0])}/hqdefault.jpg" alt="{e(v[1])}" loading="lazy" width="480" height="360"></a><figcaption>▶ {e(v[1])} – xem trên kênh YouTube Chứng Khoán Huy Nguyễn</figcaption></figure>')
    return "".join(h)
def blk(t, c):
    if t == "p": return "<p>%s</p>" % c
    if t == "h2": return "<h2>%s</h2>" % e(c)
    if t in ("ul", "ol"): return "<%s>%s</%s>" % (t, "".join("<li>%s</li>" % x for x in c), t)
    if t == "table": return '<div class="tb"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % ("".join("<th>%s</th>" % x for x in c[0]), "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % x for x in r) for r in c[1:]))
    return ""
for x in F:
    url = B + FP(x)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B + "/"},
            {"@type": "ListItem", "position": 2, "name": "Cẩm nang F0", "item": B + "/f0/"},
            {"@type": "ListItem", "position": 3, "name": GN[x.get("grp", 1)], "item": B + HP(x.get("grp", 1))},
            {"@type": "ListItem", "position": 4, "name": x["title"], "item": url}]},
        {"@type": "Article", "headline": x["title"][:110], "description": x["desc"], "image": [B + "/img/og.png"], "datePublished": x.get("date", FDATE) + "T17:00:00+07:00", "dateModified": x.get("mod", x.get("date", FDATE)) + "T17:00:00+07:00",
         "inLanguage": "vi", "mainEntityOfPage": url, "keywords": x["kw"] + ", chứng khoán cho người mới, F0",
         "author": {"@type": "Person", "name": "Huy Nguyễn", "url": B + "/"},
         "publisher": {"@type": "Organization", "name": "Chứng Khoán Huy Nguyễn", "logo": {"@type": "ImageObject", "url": B + "/img/icon-512.png"}}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in x["faq"]]}]
         + [{"@type": "VideoObject", "name": v[1][:100], "description": x["desc"], "thumbnailUrl": "https://i.ytimg.com/vi/%s/hqdefault.jpg" % v[0], "uploadDate": v[2] + "T12:00:00+07:00", "contentUrl": "https://www.youtube.com/watch?v=" + v[0], "embedUrl": "https://www.youtube.com/embed/" + v[0]} for v in YTM.get(x["slug"], [])[:2]]}
    p = [head(x["title"] + " | Chứng Khoán Huy Nguyễn", x["desc"], (B + "/f0/%s.html" % x["canon"]) if x.get("canon") else url, B + "/img/og.png", ld), "<main><article>",
         '<div class="bc"><a href="/">Trang chủ</a> › <a href="/f0/">Cẩm nang F0</a> › <a href="%s">%s</a></div>' % (HP(x.get("grp", 1)), GN[x.get("grp", 1)]),
         f'<h1>{e(x["title"])}</h1><div class="meta">Cẩm nang chứng khoán cho người mới · Huy Nguyễn</div>',
         f'<div class="sum"><b>Tóm tắt:</b> {e(x["desc"])}</div>',
         '<div style="margin:20px 0;padding:14px 16px;border-radius:12px;background:#0068ff12;border:1px solid #0068ff55"><b>💬 Học cùng cộng đồng: hỏi đáp miễn phí cho người mới, nhận bảng tổng hợp BCTC và nhận định thị trường mỗi ngày</b><br><a href="https://zalo.me/g/jbnbiq994" target="_blank" rel="noopener" style="display:inline-block;margin-top:8px;background:#0068ff;color:#fff;padding:9px 16px;border-radius:999px;font-weight:700;text-decoration:none">Tham gia nhóm Zalo cộng đồng (miễn phí)</a></div>']
    g = x.get("grp", 1); gi = [y for y in F if y.get("grp", 1) == g]; k = gi.index(x)
    p.insert(3, f'<div class="step"><a href="{HP(g)}" style="color:inherit;text-decoration:none">Bước {g}: {GN[g]}</a> · Bài {k + 1}/{len(gi)}</div>')
    hs = [b[1] for b in x["body"] + x.get("add", []) if b[0] == "h2"]
    if len(hs) >= 3:
        p.append('<nav class="toc"><b>Nội dung bài</b><ol>' + "".join(f'<li><a href="#m{i}">{e(h)}</a></li>' for i, h in enumerate(hs)) + '</ol></nav>')
    hi = 0
    for b in x["body"] + x.get("add", []):
        if b[0] == "h2":
            p.append(f'<h2 id="m{hi}">{e(b[1])}</h2>'); hi += 1; continue
        if b[0] == "cta":
            p.append(f'<div class="cta"><p>{e(b[1])}</p><a class="btn b1" href="{e(b[2])}" target="_blank" rel="noopener nofollow">{e(b[3])}</a></div>')
        elif b[0] == "img":
            p.append(f'<figure class="fimg"><img src="{e(b[1])}" alt="{e(b[2])}" loading="lazy" width="{b[4] if len(b)>4 else 1200}" height="{b[5] if len(b)>5 else 675}"><figcaption>{e(b[3])}</figcaption></figure>')
        else:
            p.append(blk(b[0], b[1]))
    i = F.index(x); pv = F[i - 1] if i else None; nx = F[i + 1] if i + 1 < len(F) else None
    p.append(ytblk(YTM.get(x["slug"], [])))
    p.append("<h2>Câu hỏi thường gặp</h2>" + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in x["faq"]))
    p.append('<div class="pn">' + (f'<a href="{FP(pv)}"><small>← Bài trước</small>{e(pv["title"])}</a>' if pv else '<span></span>') + (f'<a href="{FP(nx)}" style="text-align:right"><small>Bài tiếp theo →</small>{e(nx["title"])}</a>' if nx else '<a href="/f0/" style="text-align:right"><small>Hoàn thành lộ trình →</small>Về mục lục cẩm nang</a>') + '</div>')
    p.append('<h2>Đọc tiếp</h2><ul>' + "".join(f'<li><a href="{FP(FM[r])}">{e(FM[r]["title"])}</a></li>' for r in x["rel"] if r in FM) + f'<li><a href="{HP(x.get("grp", 1))}">Tất cả bài chủ đề {e(GN[x.get("grp", 1)])}</a></li><li><a href="/f0/tu-dien-thuat-ngu-chung-khoan.html">Từ điển thuật ngữ chứng khoán A–Z</a></li><li><a href="/hoc/">Thư viện bài học có video</a></li></ul>')
    p.append(f'<div class="cta"><a class="btn b1" href="/mo-tai-khoan-chung-khoan.html">Mở tài khoản chứng khoán</a><a class="btn b2" href="https://zalo.me/0365188286" rel="noopener">Tư vấn 1:1 qua Zalo</a><a class="btn b2" href="https://zalo.me/g/jbnbiq994" rel="noopener">Nhóm Zalo hỏi đáp</a><a class="btn b2" href="{YT}?sub_confirmation=1" rel="noopener">Kênh YouTube</a></div>')
    p.append("</article></main>" + FOOT)
    fn = FP(x)[1:]; fkeep.add(fn)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write("\n".join(p))
HNAV = '<nav class="toc"><b>Chủ đề</b><ol>' + "".join(f'<li><a href="{HP(g)}">{GN[g]}</a></li>' for g in GN) + '<li><a href="/f0/tu-dien-thuat-ngu-chung-khoan.html">Từ điển thuật ngữ A–Z</a></li></ol></nav>'
for g in GN:
    L = [x for x in F if x.get("grp", 1) == g]
    if not L: continue
    url = B + HP(g)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B + "/"},
            {"@type": "ListItem", "position": 2, "name": "Cẩm nang F0", "item": B + "/f0/"},
            {"@type": "ListItem", "position": 3, "name": GN[g], "item": url}]},
        {"@type": "CollectionPage", "name": HT[g], "url": url, "inLanguage": "vi", "description": HI[g][:155],
         "hasPart": [{"@type": "Article", "headline": x["title"][:110], "url": B + FP(x)} for x in L]}]}
    p = [head(HT[g][:65], (HI[g][:152] + "…") if len(HI[g]) > 155 else HI[g], url, B + "/img/og.png", ld), "<main>",
         f'<div class="bc"><a href="/">Trang chủ</a> › <a href="/f0/">Cẩm nang F0</a> › {GN[g]}</div><h1>{e(HT[g])}</h1>',
         f'<p>{e(HI[g])}</p><p class="meta">{len(L)} bài · Bước {g} trong lộ trình cẩm nang chứng khoán cho người mới.</p>',
         '<ol class="f0l">' + "".join(f'<li><a href="{FP(x)}"><b>{e(x["title"])}</b></a><br><small>{e(x["desc"])}</small></li>' for x in L) + '</ol>',
         HNAV, '<div class="cta"><a class="btn b1" href="/f0/">Xem toàn bộ lộ trình</a><a class="btn b2" href="https://zalo.me/0365188286" rel="noopener">Tư vấn 1:1 qua Zalo</a></div></main>' + FOOT]
    fn = HP(g)[1:]; fkeep.add(fn)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write("\n".join(p))
_TD = json.load(open(os.path.join(ROOT, "_f0/tu_dien.json"), encoding="utf-8"))
_TD = sorted([t for t in _TD if not t[2] or t[2] in FM], key=lambda t: t[0].lower())
url = B + "/f0/tu-dien-thuat-ngu-chung-khoan.html"
ld = {"@context": "https://schema.org", "@graph": [
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B + "/"},
        {"@type": "ListItem", "position": 2, "name": "Cẩm nang F0", "item": B + "/f0/"},
        {"@type": "ListItem", "position": 3, "name": "Từ điển thuật ngữ", "item": url}]},
    {"@type": "DefinedTermSet", "name": "Từ điển thuật ngữ chứng khoán A–Z", "url": url, "inLanguage": "vi",
     "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t[0], "description": t[1]} for t in _TD]}]}
_L = sorted({t[0][0].upper() for t in _TD})
p = [head("Từ điển thuật ngữ chứng khoán A–Z cho người mới", "Giải thích ngắn gọn %d thuật ngữ chứng khoán thường gặp từ A đến Z: P/E, ROE, margin, T+2, ATO, ETF, cổ tức… kèm link bài chi tiết cho người mới." % len(_TD), url, B + "/img/og.png", ld), "<main>",
     '<div class="bc"><a href="/">Trang chủ</a> › <a href="/f0/">Cẩm nang F0</a> › Từ điển thuật ngữ</div><h1>Từ điển thuật ngữ chứng khoán A–Z</h1>',
     f'<p>{len(_TD)} thuật ngữ người mới hay gặp, mỗi mục giải thích một câu và dẫn tới bài chi tiết.</p>',
     '<p class="meta">' + " · ".join(f'<a href="#k{i}">{c}</a>' for i, c in enumerate(_L)) + '</p>']
for i, c in enumerate(_L):
    p.append(f'<h2 id="k{i}">{c}</h2><ul>' + "".join(f'<li><b>{e(t[0])}</b>: {e(t[1])}' + (f' <a href="/f0/{t[2]}.html">Xem chi tiết</a>' if t[2] else "") + "</li>" for t in _TD if t[0][0].upper() == c) + "</ul>")
p.append(HNAV + '<div class="cta"><a class="btn b1" href="/f0/">Lộ trình cẩm nang F0</a></div></main>' + FOOT)
fkeep.add("f0/tu-dien-thuat-ngu-chung-khoan.html")
open(os.path.join(ROOT, "f0/tu-dien-thuat-ngu-chung-khoan.html"), "w", encoding="utf-8").write("\n".join(p))
url = B + "/f0/"
ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Cẩm nang chứng khoán cho người mới (F0)", "url": url, "inLanguage": "vi",
      "hasPart": [{"@type": "Article", "headline": x["title"][:110], "url": B + FP(x)} for x in F]}
p = [head("Chứng khoán cho người mới bắt đầu: cẩm nang F0 từ A đến Z | Chứng Khoán Huy Nguyễn",
          "Cẩm nang chứng khoán cho người mới: chứng khoán là gì, mở tài khoản, cách mua cổ phiếu, đọc bảng giá, P/E, cắt lỗ, margin, T+2, cổ tức, phí và thuế.",
          url, B + "/img/og.png", ld), "<main>",
     # QL1 11/11: điện thoại chỉ hiện 6 bài đầu mỗi bước (chỉ tiêu đề) + nút xem đủ, trang từ ~57.000px còn vài màn hình
     '<style>.gp-all{display:none}@media (max-width:600px){.gp .f0l li:nth-child(n+7){display:none}.gp .f0l small{display:none}.gp .f0l li{padding:6px 0}.gp-all{display:block;margin:4px 0 8px;padding:12px 16px;min-height:44px;border:1px solid #d9cdee;border-radius:12px;font-weight:700;text-decoration:none;text-align:center}}</style>',
     '<div class="bc"><a href="/">Trang chủ</a> › Cẩm nang F0</div><h1>Chứng khoán cho người mới bắt đầu: cẩm nang F0</h1>',
     f'<p class="meta">{len(F)} bài, chia {len(GN)} bước. Học lần lượt từ Bước 1, mỗi bài có ví dụ dễ hiểu và nút sang bài tiếp theo.</p>' +
     '<nav class="toc"><b>Lộ trình</b><ol>' + "".join(f'<li><a href="#b{g}">Bước {g}: {GN[g]}</a> <small>({sum(1 for x in F if x.get("grp", 1) == g)} bài)</small></li>' for g in GN if any(x.get("grp", 1) == g for x in F)) + '</ol></nav>' +
     HNAV + "".join(f'<section class="gp" id="b{g}"><h2><a href="{HP(g)}" style="color:inherit;text-decoration:none">Bước {g}: {GN[g]}</a></h2><p>{GD[g]}</p><ol class="f0l">' + "".join(f'<li><a href="{FP(x)}"><b>{e(x["title"])}</b></a><br><small>{e(x["desc"])}</small></li>' for x in F if x.get("grp", 1) == g) + f'</ol><a class="gp-all" href="{HP(g)}">Xem đủ {sum(1 for x in F if x.get("grp", 1) == g)} bài Bước {g} →</a></section>' for g in GN if any(x.get("grp", 1) == g for x in F)),
     f'<div class="cta"><a class="btn b1" href="/hoc/">Thư viện bài học có video</a><a class="btn b2" href="{YT}?sub_confirmation=1" rel="noopener">Kênh YouTube</a></div></main>' + FOOT]
open(os.path.join(ROOT, "f0/index.html"), "w", encoding="utf-8").write("\n".join(p))
for f in os.listdir(os.path.join(ROOT, "f0")):
    if f != "index.html" and "f0/" + f not in fkeep: os.remove(os.path.join(ROOT, "f0", f))

today = now.strftime("%Y-%m-%d")
U = [(B + "/", today, "daily", "1.0"), (B + "/hoc/", today, "daily", "0.9"), (B + "/bao-cao-2026.html", today, "weekly", "0.7")]
U += [(f"{B}/hoc/{v['slug']}.html", v["d"], "monthly", "0.8") for v in R]
U += [(B + "/f0/", today, "weekly", "0.9"), (B + "/f0/tu-dien-thuat-ngu-chung-khoan.html", today, "weekly", "0.9")] + [(B + HP(g), today, "weekly", "0.9") for g in GN] + [(B + FP(x), FDATE, "monthly", "0.9" if x.get("root") else "0.8") for x in F if not x.get("canon")]
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority></url>\n" for u, d, c, pr in U) + "</urlset>\n")
print("hoc:", len(R), "bai")
