# Tạo trang từng mã cổ phiếu /ma/<MÃ>.html (dữ liệu thật trong data/*.bin) + /ma/index.html + bổ sung sitemap.xml
# Chạy sau hoc.py mỗi ngày (GitHub Actions). Không đưa điểm mua/bán.
import os, re, json, html, datetime
import hncodec
B = "https://chungkhoanhuynguyen.com"
YT = "https://www.youtube.com/@chungkhoanhuynguyen"
ROOT = os.path.dirname(os.path.abspath(__file__))
D = lambda p: hncodec.load(os.path.join(ROOT, p))
e = lambda s: html.escape(str(s if s is not None else ""), quote=True)
src = open(os.path.join(ROOT, "hoc.py"), encoding="utf-8").read()
CSS = re.search(r'CSS = """(.*?)"""', src, re.S).group(1)
EXN = {"H": "HOSE", "X": "HNX", "U": "UPCoM"}
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
today = now.strftime("%Y-%m-%d")

def nf(x, d=2):
    if x is None: return "–"
    s = f"{abs(x):,.{d}f}".replace(",", "#").replace(".", ",").replace("#", ".")
    return ("−" if x < 0 else "") + s
def pc(x): return "–" if x is None else ("+" if x >= 0 else "−") + nf(abs(x), 1) + "%"
def dmy(d): y, m, dd = d.split("-"); return f"{int(dd)}/{int(m)}/{y}"

S = {x[0]: x for x in D("data/c/syms.bin")["s"]}
fv = D("data/fund.bin"); fv = fv.get("v", fv); FL = fv["f"]
FD = {k: dict(zip(FL, a)) for k, a in fv["d"].items()}
KQ = {}
for x in (D("data/kqkd.bin") or {}).get("items", []):
    KQ.setdefault(x["s"], x)
try:
    NX = D("data/nx.bin") or {}
    NX = NX.get("v", NX) if isinstance(NX, dict) and "v" in NX and isinstance(NX["v"], dict) else NX
except Exception:
    NX = {}
big = [r for r in FD.values() if (r.get("mc") or 0) >= 1000 and (r.get("v10") or 0) >= 50000]
def med(k, pos=True):
    a = sorted(r[k] for r in big if r.get(k) is not None and (r[k] > 0 or not pos))
    return a[len(a) // 2] if a else None
MED = {"pe": med("pe"), "pb": med("pb"), "roe": med("roe", False), "dy": med("dy")}

def bars(sym):
    p = os.path.join(ROOT, "data/c", sym + ".bin")
    if not os.path.exists(p): return []
    j = hncodec.load(p); d = datetime.date.fromisoformat(j["d0"]); out = []
    for g, o, h, l, c, v in zip(j["g"], j["o"], j["h"], j["l"], j["c"], j["v"]):
        d += datetime.timedelta(g); out.append((d.isoformat(), o / 100, h / 100, l / 100, c / 100, v))
    return out
def ma(c, n): return sum(c[-n:]) / n if len(c) >= n else None
def rsi(c, p=14):
    if len(c) <= p: return None
    g = l = 0.0
    for i in range(1, p + 1):
        d = c[i] - c[i - 1]; g += max(d, 0); l += max(-d, 0)
    g /= p; l /= p
    for i in range(p + 1, len(c)):
        d = c[i] - c[i - 1]; g = (g * (p - 1) + max(d, 0)) / p; l = (l * (p - 1) + max(-d, 0)) / p
    return 100 - 100 / (1 + g / l) if l else 100.0
def chg(c, k): return (c[-1] / c[-1 - k] - 1) * 100 if len(c) > k and c[-1 - k] else None

SYMS = sorted(s for s, x in S.items() if x[1] in EXN and s in FD and (FD[s].get("v10") or 0) >= 20000 and os.path.exists(os.path.join(ROOT, "data/c", s + ".bin")))

def head(title, desc, url, ld):
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; object-src 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests"><meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{B}/img/og.png"><meta property="og:locale" content="vi_VN">
<link rel="icon" href="/img/fav-32.png"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;800&family=Playfair+Display:wght@800;900&display=swap">
<style>{CSS}.mt{{width:100%;border-collapse:collapse;font-size:15px;margin:8px 0 18px}}.mt td{{border-bottom:1px solid var(--line);padding:8px 6px}}.mt td.r{{text-align:right;font-variant-numeric:tabular-nums}}.mt td.n{{color:var(--mute);font-size:13px;text-align:right}}.up{{color:#0a8a4a}}.dn{{color:#c0392b}}.az{{columns:4 120px;font-size:15px;line-height:1.9}}.az a{{text-decoration:none}}.tag{{display:inline-block;font-size:12px;font-weight:700;border-radius:6px;padding:2px 8px;background:#f1eef6}}</style><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>
<header class="top"><div class="in"><a class="brand" href="/">HUY NGUYỄN <b>·</b> CHỨNG KHOÁN</a><nav class="nav"><a href="/ma/">Mã CP</a><a href="/f0/">F0</a><a href="/hoc/">Bài học</a></nav></div></header>"""
FOOT = """<footer>© Chứng Khoán Huy Nguyễn · <a href="/">chungkhoanhuynguyen.com</a><br>Thông tin tổng hợp từ dữ liệu thị trường và báo cáo tài chính, tham khảo, không phải khuyến nghị mua bán.</footer></body></html>"""

os.makedirs(os.path.join(ROOT, "ma"), exist_ok=True)
keep = set(); made = []
for s in SYMS:
    x = S[s]; r = FD[s]; name = x[2] if x[2] and x[2] != s else s; ex = EXN[x[1]]
    b = bars(s)
    if len(b) < 30: continue
    c = [q[4] for q in b if q[4] > 0]; p = c[-1]; last = b[-1][0]
    y = b[-250:]; hi = max(q[2] for q in y); lo = min(q[3] for q in y if q[3] > 0)
    m20, m50, m200 = ma(c, 20), ma(c, 50), ma(c, 200); R = rsi(c)
    ms = [m for m in (m20, m50, m200) if m]; ab = sum(1 for m in ms if p > m)
    tr = "xu hướng tăng" if ab == len(ms) else "xu hướng giảm" if ab == 0 else "trạng thái giằng co"
    w, mo, yr = chg(c, 5), chg(c, 21), chg(c, 250)
    pe, pb, roe, dy = r.get("pe"), r.get("pb"), r.get("roe"), r.get("dy")
    def cmp(v, m, lowword="thấp hơn", highword="cao hơn"):
        if v is None or m is None or v <= 0: return ""
        return f"{highword if v > m else lowword} trung vị thị trường ({nf(m, 1)})"
    k = KQ.get(s); nx = NX.get(s) if isinstance(NX, dict) else None
    url = f"{B}/ma/{s}.html"
    nm2 = f" ({name})" if name != s else ""
    title = f"Cổ phiếu {s}{nm2}: giá hôm nay, định giá P/E, kết quả kinh doanh"
    desc = f"{s} giá {nf(p)} nghìn đồng ngày {dmy(last)}, {pc(yr)} trong 1 năm. P/E {nf(pe,1)}, P/B {nf(pb,2)}, ROE {nf(roe,1)}%. Xu hướng, đỉnh đáy 52 tuần, đánh giá BCTC {s}."
    intro = (f"Cổ phiếu <b>{e(s)}</b>" + (f" của {e(name)}" if name != s else "") + f" niêm yết trên sàn {ex}. Phiên {dmy(last)}, {e(s)} đóng cửa ở <b>{nf(p)}</b> nghìn đồng, "
             f"<span class='{'up' if (w or 0)>=0 else 'dn'}'>{pc(w)}</span> trong 1 tuần và <span class='{'up' if (yr or 0)>=0 else 'dn'}'>{pc(yr)}</span> trong 1 năm. "
             f"Giá đang ở {tr} (trên {ab}/{len(ms)} đường trung bình MA20, MA50, MA200).")
    val = []
    if pe and pe > 0: val.append(f"P/E {nf(pe,1)} lần, {cmp(pe, MED['pe'])}")
    if pb and pb > 0: val.append(f"P/B {nf(pb,2)} lần, {cmp(pb, MED['pb'])}")
    if roe is not None: val.append(f"ROE {nf(roe,1)}%, {cmp(roe, MED['roe'])}")
    rows = [("Giá đóng cửa", nf(p), dmy(last)), ("Thay đổi 1 tuần / 1 tháng", f"{pc(w)} / {pc(mo)}", ""), ("Thay đổi 1 năm", pc(yr), ""),
            ("Cao nhất / thấp nhất 52 tuần", f"{nf(hi)} / {nf(lo)}", f"cách đỉnh {pc((p/hi-1)*100)}"),
            ("MA20 / MA50 / MA200", f"{nf(m20)} / {nf(m50)} / {nf(m200)}", tr), ("RSI 14", nf(R, 0), "vùng nóng" if R and R >= 70 else "vùng lạnh" if R and R <= 30 else "trung tính"),
            ("P/E", nf(pe, 1), cmp(pe, MED["pe"])), ("P/B", nf(pb, 2), cmp(pb, MED["pb"])), ("ROE", nf(roe, 1) + "%", cmp(roe, MED["roe"])),
            ("ROA", nf(r.get("roa"), 1) + "%", ""), ("EPS (đồng)", nf(r.get("eps"), 0), ""), ("Giá trị sổ sách/cp (đồng)", nf(r.get("bvps"), 0), ""),
            ("Tỷ suất cổ tức", nf(dy, 1) + "%", ""), ("Vốn hóa (tỷ đồng)", nf(r.get("mc"), 0), ""), ("Khối ngoại sở hữu", nf(r.get("fo"), 1) + "%", ""), ("Beta", nf(r.get("beta"), 2), "")]
    faq = [(f"Giá cổ phiếu {s} hôm nay là bao nhiêu?", f"Phiên {dmy(last)}, {s} đóng cửa ở {nf(p)} nghìn đồng/cổ phiếu ({pc(w)} trong 1 tuần). Giá cập nhật hằng ngày trên trang này và bảng giá chungkhoanhuynguyen.com."),
           (f"P/E của {s} là bao nhiêu?", f"P/E hiện khoảng {nf(pe,1)} lần" + (f", {cmp(pe, MED['pe'])}." if pe and pe > 0 else ".") + " P/E cần so cùng ngành và chất lượng lợi nhuận."),
           (f"{s} có trả cổ tức không?", f"Tỷ suất cổ tức gần đây khoảng {nf(dy,1)}%." if dy else f"Chưa ghi nhận cổ tức tiền mặt gần đây của {s} trong dữ liệu."),
           (f"Có nên mua cổ phiếu {s} không?", f"Trang này không đưa khuyến nghị mua bán. Quyết định nên dựa trên định giá, kết quả kinh doanh, xu hướng giá và khẩu vị rủi ro của từng người. Khách hàng có thể hỏi chuyên sâu về {s} ở mục Hỏi đáp PRO hoặc trao đổi 1:1 với Huy Nguyễn.")]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B + "/"},
            {"@type": "ListItem", "position": 2, "name": "Mã cổ phiếu", "item": B + "/ma/"}, {"@type": "ListItem", "position": 3, "name": f"Cổ phiếu {s}", "item": url}]},
        {"@type": "WebPage", "name": title, "description": desc, "url": url, "inLanguage": "vi", "dateModified": today,
         "about": {"@type": "Corporation", "name": name, "tickerSymbol": f"{ex}:{s}"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    P = [head(title + " | Chứng Khoán Huy Nguyễn", desc, url, ld), "<main><article>",
         f'<div class="bc"><a href="/">Trang chủ</a> › <a href="/ma/">Mã cổ phiếu</a> › {e(s)}</div>',
         f'<h1>Cổ phiếu {e(s)}' + (f' – {e(name)}' if name != s else '') + '</h1><div class="meta">Sàn {ex} · cập nhật {dmy(today)} · giá điều chỉnh, nghìn đồng</div>',
         f"<p>{intro}</p>"]
    if val: P.append("<p>Về định giá: " + "; ".join(e(v) for v in val) + ".</p>")
    P.append("<h2>Chỉ số chính của " + e(s) + "</h2><table class='mt'>" + "".join(f"<tr><td>{e(a)}</td><td class='r'><b>{e(bv)}</b></td><td class='n'>{e(cv)}</td></tr>" for a, bv, cv in rows) + "</table>")
    if k:
        lab = {"pos": "Tích cực", "mid": "Trung tính", "neg": "Tiêu cực"}.get(k.get("v"), "")
        P.append(f"<h2>Kết quả kinh doanh {e(k.get('q',''))}</h2><p><span class='tag'>{e(lab)}</span></p><ul>" + "".join(f"<li>{e(i)}</li>" for i in k.get("info", [])) + "</ul>")
        if k.get("good"): P.append("<h3>Điểm cộng</h3><ul>" + "".join(f"<li>{e(i)}</li>" for i in k["good"]) + "</ul>")
        if k.get("bad"): P.append("<h3>Điểm cần lưu ý</h3><ul>" + "".join(f"<li>{e(i)}</li>" for i in k["bad"]) + "</ul>")
    if nx: P.append(f"<h2>Nhận định của Huy Nguyễn về {e(s)}</h2><blockquote>{e(nx)}</blockquote>")
    P.append(f'<div class="cta"><a class="btn b1" href="/#ma={e(s)}">Xem biểu đồ {e(s)}</a><a class="btn b2" href="/#hoidap">Hỏi đáp chuyên sâu về {e(s)}</a><a class="btn b2" href="https://zalo.me/0365188286" rel="noopener">Tư vấn 1:1</a></div>')
    P.append("<h2>Câu hỏi thường gặp về cổ phiếu " + e(s) + "</h2>" + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in faq))
    same = [t for t in SYMS if S[t][1] == x[1] and t != s]
    i0 = SYMS.index(s); near = [t for t in SYMS[max(0, i0 - 4): i0 + 5] if t != s][:8]
    P.append("<h2>Mã cổ phiếu khác</h2><p>" + " · ".join(f'<a href="/ma/{t}.html">{t}</a>' for t in near) + ' · <a href="/ma/">Tất cả mã</a></p>')
    P.append('<p>Mới đầu tư? Đọc <a href="/f0/pe-la-gi.html">P/E là gì</a>, <a href="/f0/cach-doc-bang-gia-chung-khoan.html">cách đọc bảng giá</a> và <a href="/f0/">cẩm nang F0</a>.</p>')
    P.append("</article></main>" + FOOT)
    fn = f"ma/{s}.html"; keep.add(fn); made.append(s)
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write("\n".join(P))

url = B + "/ma/"
ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Danh sách mã cổ phiếu Việt Nam", "url": url, "inLanguage": "vi"}
P = [head("Danh sách mã cổ phiếu HOSE, HNX, UPCoM: giá, P/E, định giá | Chứng Khoán Huy Nguyễn",
          f"Tra cứu {len(made)} mã cổ phiếu Việt Nam: giá hôm nay, P/E, P/B, ROE, cổ tức, xu hướng giá và đánh giá kết quả kinh doanh, cập nhật mỗi ngày.", url, ld),
     '<main><div class="bc"><a href="/">Trang chủ</a> › Mã cổ phiếu</div><h1>Danh sách mã cổ phiếu Việt Nam</h1>',
     f'<p class="meta">{len(made)} mã có thanh khoản trên HOSE, HNX, UPCoM · cập nhật {dmy(today)}</p>']
for code, nm in (("H", "HOSE"), ("X", "HNX"), ("U", "UPCoM")):
    L = [t for t in made if S[t][1] == code]
    if L: P.append(f"<h2>Sàn {nm}</h2><div class='az'>" + "".join(f'<a href="/ma/{t}.html">{t}</a><br>' for t in L) + "</div>")
P.append("</main>" + FOOT)
open(os.path.join(ROOT, "ma/index.html"), "w", encoding="utf-8").write("\n".join(P))
for f in os.listdir(os.path.join(ROOT, "ma")):
    if f != "index.html" and "ma/" + f not in keep: os.remove(os.path.join(ROOT, "ma", f))

sp = os.path.join(ROOT, "sitemap.xml"); sm = open(sp, encoding="utf-8").read()
sm = re.sub(r"<url><loc>" + re.escape(B) + r"/ma/[^<]*</loc>.*?</url>\n", "", sm)
add = f"<url><loc>{B}/ma/</loc><lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\n" + \
      "".join(f"<url><loc>{B}/ma/{t}.html</loc><lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>0.7</priority></url>\n" for t in made)
sm = sm.replace("</urlset>", add + "</urlset>")
open(sp, "w", encoding="utf-8").write(sm)
print("ma:", len(made), "trang")
