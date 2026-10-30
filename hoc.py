# Tạo trang bài học /hoc/*.html từ _hoc/videos.json cho các video đã ra mắt + cập nhật sitemap.xml
# Chạy: python hoc.py   (GitHub Actions chạy mỗi ngày 20:10 giờ VN)
import json, os, html, datetime
B = "https://chungkhoanhuynguyen.com"
YT = "https://www.youtube.com/@chungkhoanhuynguyen"
ROOT = os.path.dirname(os.path.abspath(__file__))
V = json.load(open(os.path.join(ROOT, "_hoc/videos.json"), encoding="utf-8"))
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
def live(v):
    return now >= datetime.datetime.fromisoformat(v["d"] + "T20:00:00")
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
.fimg{margin:18px 0}.fimg img{width:100%;max-width:620px;height:auto;border-radius:12px;border:1px solid #ddd;display:block}.fimg figcaption{font-size:14px;color:var(--mute);margin-top:6px}.cta{display:flex;flex-wrap:wrap;gap:10px;margin:28px 0}.cta p{flex-basis:100%;margin:0}.f0l{padding-left:22px}.f0l li{margin:0 0 16px;line-height:1.5}.f0l small{color:var(--mute)}article ul,article ol{line-height:1.7}.btn{display:inline-block;padding:10px 16px;border-radius:999px;font-weight:700;text-decoration:none;font-size:15px}
.b1{background:#c4302b;color:#fff}.b2{border:1px solid var(--line);background:var(--panel);color:var(--fg)}
.pn{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:24px 0}.pn a{display:block;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 12px;text-decoration:none;color:var(--fg);font-size:14px}.pn small{color:var(--mute);display:block}
.src{font-size:13px;color:var(--mute);border-top:1px solid var(--line);margin-top:28px;padding-top:12px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px;margin:12px 0 28px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;color:var(--fg)}.card img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}.card span{display:block;padding:10px 12px;font-weight:600;font-size:15px;line-height:1.45}
footer{text-align:center;color:var(--mute);font-size:13px;padding:24px 16px;border-top:1px solid var(--line)}
@media(max-width:560px){.pn{grid-template-columns:1fr}.nav a.hide{display:none}.brand{min-width:0;overflow:hidden;text-overflow:ellipsis}.brand{font-size:13px}.nav{gap:10px;font-size:13px}.top .in{gap:8px}}"""

def head(title, desc, url, img, ld):
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data: https://i.ytimg.com; frame-src https://www.youtube-nocookie.com; object-src 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests"><meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{img}"><meta property="og:locale" content="vi_VN"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/fav-32.png"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;800&family=Playfair+Display:wght@800;900&display=swap">
<style>{CSS}</style><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>
<header class="top"><div class="in"><a class="brand" href="/">HUY NGUYỄN <b>·</b> CHỨNG KHOÁN</a><nav class="nav"><a href="/mo-tai-khoan-chung-khoan.html">Mở TK</a><a href="/ma/">Mã CP</a><a href="/f0/">F0</a><a href="/hoc/">Bài học</a><a class="hide" href="/">Bảng giá &amp; định giá</a><a href="{YT}?sub_confirmation=1" rel="noopener">YouTube</a></nav></div></header>"""

FOOT = """<footer>© Chứng Khoán Huy Nguyễn · <a href="/">chungkhoanhuynguyen.com</a><br>Nội dung chia sẻ kiến thức và quan điểm cá nhân, không phải khuyến nghị mua bán.</footer></body></html>"""

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
    p = [head(v["h1"] + " | Chứng Khoán Huy Nguyễn", desc_of(v), url, thumb, ld), "<main><article>",
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
          "Học chứng khoán từ đầu: lịch sử thị trường Việt Nam và thế giới, tư duy nhà đầu tư huyền thoại, đọc báo cáo tài chính, định giá cổ phiếu. Mỗi bài có video và bài viết.",
          url, B + "/img/og.png", ld), "<main>",
     '<div class="bc"><a href="/">Trang chủ</a> › Thư viện bài học</div><h1>Thư viện bài học chứng khoán</h1>',
     '<p class="meta">Kiến thức chứng khoán cho người mới bắt đầu, kể bằng câu chuyện và số liệu có nguồn. Mỗi tối 20:00 có một bài mới.</p>']
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
FM = {x["slug"]: x for x in F}
FP = lambda x: ("/%s.html" if x.get("root") else "/f0/%s.html") % x["slug"]
os.makedirs(os.path.join(ROOT, "f0"), exist_ok=True)
fkeep = set()
FDATE = "2026-10-30"
def blk(t, c):
    if t == "p": return "<p>%s</p>" % c
    if t == "h2": return "<h2>%s</h2>" % e(c)
    if t in ("ul", "ol"): return "<%s>%s</%s>" % (t, "".join("<li>%s</li>" % x for x in c), t)
    return ""
for x in F:
    url = B + FP(x)
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B + "/"},
            {"@type": "ListItem", "position": 2, "name": "Cẩm nang F0", "item": B + "/f0/"},
            {"@type": "ListItem", "position": 3, "name": x["title"], "item": url}]},
        {"@type": "Article", "headline": x["title"][:110], "description": x["desc"], "image": [B + "/img/og.png"], "datePublished": FDATE + "T17:00:00+07:00", "dateModified": today_iso if False else FDATE + "T17:00:00+07:00",
         "inLanguage": "vi", "mainEntityOfPage": url, "keywords": x["kw"] + ", chứng khoán cho người mới, F0",
         "author": {"@type": "Person", "name": "Huy Nguyễn", "url": B + "/"},
         "publisher": {"@type": "Organization", "name": "Chứng Khoán Huy Nguyễn", "logo": {"@type": "ImageObject", "url": B + "/img/icon-512.png"}}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in x["faq"]]}]}
    p = [head(x["title"] + " | Chứng Khoán Huy Nguyễn", x["desc"], url, B + "/img/og.png", ld), "<main><article>",
         '<div class="bc"><a href="/">Trang chủ</a> › <a href="/f0/">Cẩm nang F0</a></div>',
         f'<h1>{e(x["title"])}</h1><div class="meta">Cẩm nang chứng khoán cho người mới · Huy Nguyễn</div>',
         f'<div class="sum"><b>Tóm tắt:</b> {e(x["desc"])}</div>']
    for b in x["body"]:
        if b[0] == "cta":
            p.append(f'<div class="cta"><p>{e(b[1])}</p><a class="btn b1" href="{e(b[2])}" target="_blank" rel="noopener nofollow">{e(b[3])}</a></div>')
        elif b[0] == "img":
            p.append(f'<figure class="fimg"><img src="{e(b[1])}" alt="{e(b[2])}" loading="lazy" width="907" height="873"><figcaption>{e(b[3])}</figcaption></figure>')
        else:
            p.append(blk(b[0], b[1]))
    p.append("<h2>Câu hỏi thường gặp</h2>" + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in x["faq"]))
    p.append('<h2>Đọc tiếp</h2><ul>' + "".join(f'<li><a href="{FP(FM[r])}">{e(FM[r]["title"])}</a></li>' for r in x["rel"] if r in FM) + '<li><a href="/hoc/">Thư viện bài học có video</a></li></ul>')
    p.append(f'<div class="cta"><a class="btn b1" href="{YT}?sub_confirmation=1" rel="noopener">Đăng ký kênh YouTube</a><a class="btn b2" href="/">Bảng giá &amp; định giá cổ phiếu</a><a class="btn b2" href="https://zalo.me/g/jbnbiq994" rel="noopener">Nhóm Zalo hỏi đáp</a></div>')
    p.append("</article></main>" + FOOT)
    fn = FP(x)[1:]; fkeep.add(fn)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write("\n".join(p))
url = B + "/f0/"
ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Cẩm nang chứng khoán cho người mới (F0)", "url": url, "inLanguage": "vi",
      "hasPart": [{"@type": "Article", "headline": x["title"][:110], "url": B + FP(x)} for x in F]}
p = [head("Chứng khoán cho người mới bắt đầu: cẩm nang F0 từ A đến Z | Chứng Khoán Huy Nguyễn",
          "Cẩm nang chứng khoán cho người mới: chứng khoán là gì, mở tài khoản, cách mua cổ phiếu, đọc bảng giá, P/E, cắt lỗ, margin, T+2, cổ tức, phí và thuế.",
          url, B + "/img/og.png", ld), "<main>",
     '<div class="bc"><a href="/">Trang chủ</a> › Cẩm nang F0</div><h1>Chứng khoán cho người mới bắt đầu: cẩm nang F0</h1>',
     '<p class="meta">Học theo thứ tự từ trên xuống. Mỗi bài ngắn gọn, ví dụ thực tế trên thị trường Việt Nam.</p><ol class="f0l">' +
     "".join(f'<li><a href="{FP(x)}"><b>{e(x["title"])}</b></a><br><small>{e(x["desc"])}</small></li>' for x in F) + "</ol>",
     f'<div class="cta"><a class="btn b1" href="/hoc/">Thư viện bài học có video</a><a class="btn b2" href="{YT}?sub_confirmation=1" rel="noopener">Kênh YouTube</a></div></main>' + FOOT]
open(os.path.join(ROOT, "f0/index.html"), "w", encoding="utf-8").write("\n".join(p))
for f in os.listdir(os.path.join(ROOT, "f0")):
    if f != "index.html" and "f0/" + f not in fkeep: os.remove(os.path.join(ROOT, "f0", f))

today = now.strftime("%Y-%m-%d")
U = [(B + "/", today, "daily", "1.0"), (B + "/hoc/", today, "daily", "0.9"), (B + "/bao-cao-2026.html", today, "weekly", "0.7")]
U += [(f"{B}/hoc/{v['slug']}.html", v["d"], "monthly", "0.8") for v in R]
U += [(B + "/f0/", today, "weekly", "0.9")] + [(B + FP(x), FDATE, "monthly", "0.9" if x.get("root") else "0.8") for x in F]
open(os.path.join(ROOT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod><changefreq>{c}</changefreq><priority>{pr}</priority></url>\n" for u, d, c, pr in U) + "</urlset>\n")
print("hoc:", len(R), "bai")
