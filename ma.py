# Tạo trang từng mã cổ phiếu /ma/<MÃ>.html (dữ liệu thật trong data/*.bin) + /ma/index.html + bổ sung sitemap.xml
# Chạy sau hoc.py mỗi ngày (GitHub Actions). Không đưa điểm mua/bán.
import os, re, json, html, datetime
ZBOX = '<div style="margin:20px 0;padding:14px 16px;border-radius:12px;background:#0068ff12;border:1px solid #0068ff55"><b>💬 Nhận cảnh báo khi {s} công bố BCTC, bảng tổng hợp BCTC quý mới nhất và nhận định thị trường mỗi ngày</b><br><a href="https://zalo.me/g/jbnbiq994" target="_blank" rel="noopener" style="display:inline-block;margin-top:8px;background:#0068ff;color:#fff;padding:9px 16px;border-radius:999px;font-weight:700;text-decoration:none">Tham gia nhóm Zalo cộng đồng (miễn phí)</a></div>'
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

# Ngành từng mã: data/sec.bin (mw.py ghi mỗi 15 phút); thiếu thì dùng danh sách nhóm trong mw.py + bản đồ nhiệt
_mw = open(os.path.join(ROOT, "mw.py"), encoding="utf-8").read()
SECM = {}
for _nm, _var in (("Ngân hàng", "BANK"), ("Chứng khoán", "CK"), ("Bất động sản", "BDS"), ("Bảo hiểm", "BH")):
    _m = re.search(_var + r' = set\("([^"]+)"', _mw)
    if _m: SECM.update({t: _nm for t in _m.group(1).split()})
try:
    for _r in (D("data/mw.bin") or {}).get("heat", []): SECM.setdefault(_r[0], _r[3])
except Exception: pass
try: SECM.update((D("data/sec.bin") or {}).get("m", {}))
except Exception: pass
SYMS = sorted(s for s, x in S.items() if x[1] in EXN and s in FD and (FD[s].get("v10") or 0) >= 20000 and os.path.exists(os.path.join(ROOT, "data/c", s + ".bin")))

def head(title, desc, url, ld):
    return f"""<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'none'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; object-src 'none'; base-uri 'self'; form-action 'none'; upgrade-insecure-requests"><meta name="referrer" content="strict-origin-when-cross-origin">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta property="og:type" content="article"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{B}/img/og.png"><meta property="og:locale" content="vi_VN">
<link rel="icon" href="/img/fav-32.png"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;800&family=Playfair+Display:wght@800;900&display=swap">
<style>{CSS}.mt{{width:100%;border-collapse:collapse;font-size:15px;margin:8px 0 18px}}.mt td{{border-bottom:1px solid var(--line);padding:8px 6px}}.mt td.r{{text-align:right;font-variant-numeric:tabular-nums}}.mt td.n{{color:var(--mute);font-size:13px;text-align:right}}.up{{color:#0a8a4a}}.dn{{color:#c0392b}}.az{{columns:4 120px;font-size:15px;line-height:1.9}}.az a{{text-decoration:none}}.tag{{display:inline-block;font-size:12px;font-weight:700;border-radius:6px;padding:2px 8px;background:#f1eef6}}</style><script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script></head><body>
<header class="top"><div class="in"><a class="brand" href="/">HUY NGUYỄN <b>·</b> CHỨNG KHOÁN</a><nav class="nav"><a href="/mo-tai-khoan-chung-khoan.html">Mở TK</a><a href="/ma/">Mã CP</a><a href="/f0/">F0</a><a href="/hoc/">Bài học</a></nav></div></header>"""
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
    if k and k.get("h"):
        H = k["h"]; mx = max([abs(z[1]) for z in H] + [1e-9]); W0 = 640; bw = W0 / len(H)
        svg = [f'<svg viewBox="0 0 {W0} 230" role="img" aria-label="Lợi nhuận sau thuế {e(s)} theo quý" style="width:100%;height:auto;max-width:720px">']
        base = 170
        for j, (tgq, lnv, rvv) in enumerate(H):
            hgt = abs(lnv) / mx * 140; x0 = j * bw + bw * 0.18; col = "#0a8a4a" if lnv >= 0 else "#c0392b"
            y0 = base - hgt if lnv >= 0 else base
            svg.append(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{bw*0.64:.1f}" height="{max(hgt,1):.1f}" rx="3" fill="{col}"/>')
            svg.append(f'<text x="{x0+bw*0.32:.1f}" y="{(y0-4 if lnv>=0 else y0+hgt+12):.1f}" font-size="11" text-anchor="middle" fill="#444">{nf(lnv,0)}</text>')
            svg.append(f'<text x="{x0+bw*0.32:.1f}" y="222" font-size="11" text-anchor="middle" fill="#666">{e(tgq)}</text>')
        svg.append(f'<line x1="0" y1="{base}" x2="{W0}" y2="{base}" stroke="#ccc"/></svg>')
        P.append(f"<h2>Lợi nhuận sau thuế {e(s)} {len(H)} quý gần nhất (tỷ đồng)</h2>" + "".join(svg))
        if any(z[2] for z in H):
            lab2 = "Thu nhập lãi thuần" if k.get("form") == "bank" else "Doanh thu thuần"
            P.append(f"<table class='mt'><tr><td><b>Quý</b></td><td class='r'><b>{lab2}</b></td><td class='r'><b>LNST</b></td></tr>" + "".join(f"<tr><td>{e(t1)}</td><td class='r'>{nf(r1,0)}</td><td class='r'>{nf(l1,0)}</td></tr>" for t1, l1, r1 in reversed(H[-8:])) + "</table>")
    if k:
        lab = {"pos": "Tích cực", "mid": "Trung tính", "neg": "Tiêu cực"}.get(k.get("v"), "")
        P.append(f"<h2>Kết quả kinh doanh {e(k.get('q',''))}</h2><p><span class='tag'>{e(lab)}</span></p><ul>" + "".join(f"<li>{e(i)}</li>" for i in k.get("info", [])) + "</ul>")
        if k.get("good"): P.append("<h3>Điểm cộng</h3><ul>" + "".join(f"<li>{e(i)}</li>" for i in k["good"]) + "</ul>")
        if k.get("bad"): P.append("<h3>Điểm cần lưu ý</h3><ul>" + "".join(f"<li>{e(i)}</li>" for i in k["bad"]) + "</ul>")
    if nx: P.append(f"<h2>Nhận định của Huy Nguyễn về {e(s)}</h2><blockquote>{e(nx)}</blockquote>")
    P.append(ZBOX.format(s=e(s)))
    P.append(f'<div class="cta"><a class="btn b1" href="/#ma={e(s)}">Xem biểu đồ {e(s)}</a><a class="btn b2" href="/#hoidap">Hỏi đáp chuyên sâu về {e(s)}</a><a class="btn b2" href="https://zalo.me/0365188286" rel="noopener">Tư vấn 1:1</a></div>')
    P.append("<h2>Câu hỏi thường gặp về cổ phiếu " + e(s) + "</h2>" + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in faq))
    ng = SECM.get(s)
    if ng and ng not in ("Khác", "Tài chính"):
        peers = sorted([t for t in SYMS if SECM.get(t) == ng], key=lambda t: -(FD[t].get("mc") or 0))
        if s not in peers[:8]: peers = peers[:7] + [s]
        peers = peers[:8]
        if len(peers) >= 3:
            def _y(t):
                bb = bars(t); cc = [q[4] for q in bb if q[4] > 0]
                return (cc[-1] if cc else None), chg(cc, 250)
            trs = []
            for t in peers:
                ft = FD[t]; pt, yt = _y(t)
                lk = e(t) if t == s else f'<a href="/ma/{t}.html">{t}</a>'
                hl = ' style="background:#f1eef6"' if t == s else ''
                trs.append(f"<tr{hl}><td><b>{lk}</b></td><td class='r'>{nf(pt)}</td><td class='r'>{nf(ft.get('pe'),1) if (ft.get('pe') or 0) > 0 else '–'}</td><td class='r'>{nf(ft.get('pb'),2) if (ft.get('pb') or 0) > 0 else '–'}</td><td class='r'>{nf(ft.get('roe'),1)}%</td><td class='r {'up' if (yt or 0) >= 0 else 'dn'}'>{pc(yt)}</td></tr>")
            pes = sorted(FD[t]["pe"] for t in peers if (FD[t].get("pe") or 0) > 0)
            mpe = pes[len(pes) // 2] if pes else None
            note = ""
            if mpe and pe and pe > 0:
                note = f"<p>P/E của {e(s)} ({nf(pe,1)} lần) đang {'cao hơn' if pe > mpe else 'thấp hơn'} trung vị nhóm {e(ng.lower())} ({nf(mpe,1)} lần). Định giá thấp hơn chưa chắc rẻ: cần xem thêm tăng trưởng lợi nhuận và chất lượng tài sản.</p>"
            P.append(f"<h2>So sánh {e(s)} với cổ phiếu cùng ngành {e(ng.lower())}</h2>" + note +
                     "<div style='overflow-x:auto'><table class='mt'><tr><td><b>Mã</b></td><td class='r'><b>Giá</b></td><td class='r'><b>P/E</b></td><td class='r'><b>P/B</b></td><td class='r'><b>ROE</b></td><td class='r'><b>1 năm</b></td></tr>" + "".join(trs) + "</table></div>")
    same = [t for t in SYMS if S[t][1] == x[1] and t != s]
    i0 = SYMS.index(s); near = [t for t in SYMS[max(0, i0 - 4): i0 + 5] if t != s][:8]
    P.append("<h2>Mã cổ phiếu khác</h2><p>" + " · ".join(f'<a href="/ma/{t}.html">{t}</a>' for t in near) + ' · <a href="/ma/">Tất cả mã</a></p>')
    P.append(f'<p>Chưa có tài khoản để mua {e(s)}? Xem <a href="/mo-tai-khoan-chung-khoan.html">hướng dẫn mở tài khoản chứng khoán online</a> (miễn phí, 5 phút).</p>')
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


# ---- Trang chủ đề cho tìm kiếm thương hiệu: thị trường hôm nay, định giá cổ phiếu, tư vấn ----
def page(fn, title, desc, h1, body, ld_extra=None):
    url = B + "/" + fn
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Trang chủ", "item": B + "/"}, {"@type": "ListItem", "position": 2, "name": h1, "item": url}]},
        {"@type": "WebPage", "name": title, "description": desc, "url": url, "inLanguage": "vi", "dateModified": today,
         "publisher": {"@type": "Organization", "name": "Chứng Khoán Huy Nguyễn", "url": B + "/"}}] + (ld_extra or [])}
    P = [head(title, desc, url, ld), "<main><article>", f'<div class="bc"><a href="/">Trang chủ</a> › {e(h1)}</div><h1>{e(h1)}</h1>'] + body + ["</article></main>" + FOOT]
    open(os.path.join(ROOT, fn), "w", encoding="utf-8").write("\n".join(P))
    return url
CTA = ('<div class="cta"><a class="btn b1" href="/mo-tai-khoan-chung-khoan.html">Mở tài khoản chứng khoán</a>'
       '<a class="btn b2" href="https://zalo.me/0365188286" rel="noopener">Tư vấn 1:1 qua Zalo</a><a class="btn b2" href="https://zalo.me/g/jbnbiq994" rel="noopener">Nhóm Zalo cộng đồng</a><a class="btn b2" href="/#hoidap">Hỏi đáp PRO</a></div>')
NAV = ('<h2>Khám phá thêm</h2><ul><li><a href="/thi-truong-chung-khoan-hom-nay.html">Thị trường chứng khoán hôm nay</a></li><li><a href="/dinh-gia-co-phieu.html">Định giá cổ phiếu</a></li>'
       '<li><a href="/bao-cao-2026.html">Báo cáo lệnh 2016–2026</a></li><li><a href="/tu-van-dau-tu-chung-khoan.html">Tư vấn đầu tư chứng khoán</a></li><li><a href="/hoc/">Học chứng khoán</a></li><li><a href="/f0/">Cẩm nang F0</a></li><li><a href="/ma/">Tra cứu mã cổ phiếu</a></li></ul>')
EXTRA = []
# 1) Thị trường hôm nay
IX = {}
for code, nm in (("VNINDEX", "VN-Index"), ("VN30", "VN30"), ("HNX", "HNX-Index")):
    bb = bars(code)
    if len(bb) > 30:
        cc = [q[4] for q in bb]; IX[code] = (nm, bb[-1][0], cc[-1], chg(cc, 1), chg(cc, 5), chg(cc, 21), chg(cc, 250), ma(cc, 20), ma(cc, 50), ma(cc, 200), rsi(cc))
mv = []
for t in made:
    bb = bars(t)
    if len(bb) > 2 and bb[-2][4]: mv.append((t, bb[-1][4], (bb[-1][4] / bb[-2][4] - 1) * 100, bb[-1][5] * bb[-1][4]))
up = sorted(mv, key=lambda z: -z[2])[:10]; dn = sorted(mv, key=lambda z: z[2])[:10]; liq = sorted(mv, key=lambda z: -z[3])[:10]
nup = sum(1 for z in mv if z[2] > 0); ndn = sum(1 for z in mv if z[2] < 0)
body = []
if "VNINDEX" in IX:
    nm, dd, v, d1, d5, d21, d250, a20, a50, a200, rr = IX["VNINDEX"]
    ab = sum(1 for m in (a20, a50, a200) if m and v > m)
    st = "xu hướng tăng" if ab == 3 else "xu hướng giảm" if ab == 0 else "giằng co"
    body.append(f"<p>Phiên {dmy(dd)}, <b>VN-Index</b> đóng cửa <b>{nf(v)}</b> điểm ({pc(d1)} trong phiên, {pc(d5)} trong 1 tuần, {pc(d250)} trong 1 năm). Chỉ số nằm trên {ab}/3 đường trung bình MA20, MA50, MA200, trạng thái <b>{st}</b>; RSI 14 phiên {nf(rr,0)}. Trong {len(mv)} mã có thanh khoản, {nup} mã tăng và {ndn} mã giảm.</p>")
body.append("<h2>Các chỉ số chính</h2><table class='mt'>" + "".join(f"<tr><td>{e(z[0])}</td><td class='r'><b>{nf(z[2])}</b></td><td class='r {'up' if (z[3] or 0)>=0 else 'dn'}'>{pc(z[3])}</td><td class='n'>1 tháng {pc(z[5])}</td></tr>" for z in IX.values()) + "</table>")
def tb(L, lab): return f"<h2>{lab}</h2><table class='mt'>" + "".join(f"<tr><td><a href='/ma/{t}.html'>{t}</a></td><td class='r'>{nf(p)}</td><td class='r {'up' if c>=0 else 'dn'}'>{pc(c)}</td></tr>" for t, p, c, _ in L) + "</table>"
body += [tb(up, "Top 10 cổ phiếu tăng mạnh nhất"), tb(dn, "Top 10 cổ phiếu giảm mạnh nhất"), tb(liq, "Top 10 cổ phiếu thanh khoản cao nhất"),
         "<p>Nhận định thị trường hằng ngày của Huy Nguyễn được chia sẻ trong nhóm Zalo cộng đồng và video lúc 20:00 trên kênh YouTube Chứng Khoán Huy Nguyễn.</p>", CTA, NAV]
EXTRA.append(page("thi-truong-chung-khoan-hom-nay.html", f"Thị trường chứng khoán hôm nay {dmy(today)}: VN-Index, cổ phiếu tăng giảm mạnh | Chứng Khoán Huy Nguyễn",
     "Thị trường chứng khoán hôm nay: VN-Index, VN30, HNX-Index, top cổ phiếu tăng giảm mạnh, thanh khoản cao, xu hướng và nhận định của Huy Nguyễn. Cập nhật mỗi ngày.",
     "Thị trường chứng khoán hôm nay", body))
# 2) Định giá cổ phiếu
top = sorted(made, key=lambda t: -(FD[t].get("mc") or 0))[:40]
body = ["<p>Định giá cổ phiếu là ước tính giá trị hợp lý của doanh nghiệp để so với giá thị trường. Cách nhanh nhất là so các chỉ số <b>P/E</b>, <b>P/B</b>, <b>ROE</b> với trung vị thị trường và với cùng ngành; sâu hơn là chiết khấu dòng tiền và so sánh tăng trưởng lợi nhuận.</p>",
        f"<p>Trung vị thị trường hiện nay (các mã vốn hóa từ 1.000 tỷ): P/E {nf(MED['pe'],1)}, P/B {nf(MED['pb'],2)}, ROE {nf(MED['roe'],1)}%, cổ tức {nf(MED['dy'],1)}%.</p>",
        "<h2>Bảng định giá 40 cổ phiếu vốn hóa lớn</h2><table class='mt'><tr><td><b>Mã</b></td><td class='r'><b>Giá</b></td><td class='r'><b>P/E</b></td><td class='r'><b>P/B</b></td><td class='r'><b>ROE</b></td></tr>" +
        "".join(f"<tr><td><a href='/ma/{t}.html'>{t}</a></td><td class='r'>{nf(bars(t)[-1][4])}</td><td class='r'>{nf(FD[t].get('pe'),1)}</td><td class='r'>{nf(FD[t].get('pb'),2)}</td><td class='r'>{nf(FD[t].get('roe'),1)}%</td></tr>" for t in top) + "</table>",
        "<p>Xem định giá chi tiết từng mã (kèm đánh giá báo cáo tài chính và xu hướng giá) trong <a href='/ma/'>danh sách mã cổ phiếu</a>, hoặc học cách dùng chỉ số ở bài <a href='/f0/pe-la-gi.html'>P/E là gì</a>.</p>", CTA, NAV]
EXTRA.append(page("dinh-gia-co-phieu.html", "Định giá cổ phiếu: bảng P/E, P/B, ROE các mã vốn hóa lớn, cập nhật mỗi ngày | Chứng Khoán Huy Nguyễn",
     "Định giá cổ phiếu Việt Nam: bảng P/E, P/B, ROE của 40 mã vốn hóa lớn so với trung vị thị trường, cách định giá cổ phiếu cho người mới. Cập nhật hằng ngày.",
     "Định giá cổ phiếu", body))
# 3) Tư vấn
body = ["<p>Huy Nguyễn tư vấn đầu tư chứng khoán 1:1 qua Zalo hoặc điện thoại, kết hợp ba lớp: <b>phân tích kỹ thuật</b> (xu hướng, dòng tiền, điểm mua và cắt lỗ), <b>phân tích cơ bản</b> (báo cáo tài chính, định giá) và <b>vĩ mô</b> (lãi suất, tỷ giá, dòng vốn ngoại).</p>",
        "<h2>Dịch vụ</h2><ul><li>Khám danh mục: rà từng mã anh chị đang cầm, mã nào nên giữ, mã nào cần kế hoạch thoát.</li><li>Dựng danh mục theo số vốn, thời gian và mức chịu rủi ro.</li><li>Kế hoạch mua và cắt lỗ cho từng lệnh.</li><li>Cập nhật theo mùa báo cáo tài chính.</li></ul>",
        "<h2>Kết quả công khai</h2><p>Toàn bộ lệnh đầu cơ từ 2016 đến nay được công bố trong <a href='/bao-cao-2026.html'>Báo cáo lệnh 2016–2026</a>. Các lệnh tiêu biểu như MSR 2026, VIX 2025, FPT 2024, GEE 2024–2025 có video kể lại trên kênh YouTube.</p>",
        "<h2>Bắt đầu thế nào?</h2><ol><li><a href='/mo-tai-khoan-chung-khoan.html'>Mở tài khoản chứng khoán</a> qua link của Huy Nguyễn (không cần nhập mã), hoặc nếu đã có tài khoản VPS thì đổi người tư vấn sang ID BJIE theo <a href='/mo-tai-khoan-chung-khoan.html'>hướng dẫn có ảnh</a>.</li><li>Nhắn Zalo 0365.188.286 để nhận mã kích hoạt khách hàng và vào nhóm cộng đồng.</li><li>Dùng mục Hỏi đáp chuyên sâu PRO trên web để hỏi về từng mã.</li></ol>", CTA, NAV]
EXTRA.append(page("tu-van-dau-tu-chung-khoan.html", "Tư vấn đầu tư chứng khoán 1:1 cùng Huy Nguyễn | Chứng Khoán Huy Nguyễn",
     "Tư vấn đầu tư chứng khoán 1:1: khám danh mục, dựng danh mục theo vốn, kế hoạch mua và cắt lỗ, cập nhật BCTC. Lệnh thật công khai từ 2016. Zalo 0365.188.286.",
     "Tư vấn đầu tư chứng khoán", body))

sp = os.path.join(ROOT, "sitemap.xml"); sm = open(sp, encoding="utf-8").read()
sm = re.sub(r"<url><loc>" + re.escape(B) + r"/(ma/[^<]*|thi-truong-chung-khoan-hom-nay\.html|dinh-gia-co-phieu\.html|tu-van-dau-tu-chung-khoan\.html)</loc>.*?</url>\n", "", sm)
add = "".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\n" for u in EXTRA) + f"<url><loc>{B}/ma/</loc><lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>0.9</priority></url>\n" + \
      "".join(f"<url><loc>{B}/ma/{t}.html</loc><lastmod>{today}</lastmod><changefreq>daily</changefreq><priority>0.7</priority></url>\n" for t in made)
sm = sm.replace("</urlset>", add + "</urlset>")
open(sp, "w", encoding="utf-8").write(sm)
print("ma:", len(made), "trang")
