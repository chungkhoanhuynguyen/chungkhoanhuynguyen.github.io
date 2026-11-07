# -*- coding: utf-8 -*-
# Thư viện NV1: đổi số -> chữ cho lời đọc, nến tuần, số liệu kqkd/fund/bctc. (NV1 8/11/2026)
import re, json, datetime, sys, os
CW = os.environ.get('CW', '/tmp/cw'); sys.path.insert(0, CW)
import hncodec
CS = "không một hai ba bốn năm sáu bảy tám chín".split()
def _ba(n, full):
    tr, ch, dv = n // 100, n // 10 % 10, n % 10; o = []
    if full or tr: o += [CS[tr], "trăm"]
    if ch == 0:
        if dv and (full or tr): o.append("linh")
    elif ch == 1: o.append("mười")
    else: o += [CS[ch], "mươi"]
    if dv:
        if dv == 1 and ch > 1: o.append("mốt")
        elif dv == 5 and ch > 0: o.append("lăm")
        else: o.append(CS[dv])
    return o
def so(n):
    n = int(n)
    if n == 0: return "không"
    if n < 0: return "âm " + so(-n)
    U = ["", "nghìn", "triệu", "tỷ"]; g = []
    while n: g.append(n % 1000); n //= 1000
    o = []; top = len(g) - 1
    for i in range(top, -1, -1):
        v = g[i]
        if v == 0: continue
        o += _ba(v, i != top)
        if U[i % 4 if i < 4 else 3] and i: o.append(U[i] if i < 4 else "tỷ")
    return " ".join(o)
def _num(s):
    s = s.replace(".", ""); a, _, b = s.partition(",")
    if b and not b.strip("0"): b = ""
    r = so(int(a))
    if b:
        z = len(b) - len(b.lstrip("0")); r += " phẩy " + " ".join(["không"] * z) + ((" " if z else "") + so(int(b.lstrip("0"))) if b.lstrip("0") else "")
    return r.strip()
REP = [(r"P/E", "P trên E"), (r"P/B", "P trên B"), (r"P/S", "P trên S"), (r"\bUSD\b", "đô la Mỹ"), (r"\bVND\b(?! )", "đồng"),
       (r"\bVN-Index\b", "VN Index"), (r"\bROE\b", "ROE"), (r"\s*–\s*", ", "), (r"\s*—\s*", ", "), (r"×", " nhân "), (r"→", " sang ")]
def doc(t):
    t = re.sub(r"\bQ(\d)/(\d{4})", lambda m: "quý %s năm %s" % (so(m.group(1)), m.group(2)), t)
    t = re.sub(r"\bQ(\d)/(\d{2})\b", lambda m: "quý %s năm 20%s" % (so(m.group(1)), m.group(2)), t)
    t = re.sub(r"(?:ngày )?\b(\d{1,2})/(\d{1,2})/(\d{4})\b", lambda m: "ngày %s tháng %s năm %s" % (m.group(1), m.group(2), m.group(3)), t)
    t = re.sub(r"(?:ngày )?\b(\d{1,2})/(\d{1,2})\b(?!/)", lambda m: "ngày %s tháng %s" % (m.group(1), m.group(2)), t)
    for a, b in REP: t = re.sub(a, b, t)
    t = re.sub(r"[−-](?=\d)", "âm ", t); t = re.sub(r"\+(?=\d)", "", t)
    t = re.sub(r"(\d)\s*%", r"\1 phần trăm", t)
    t = re.sub(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?", lambda m: _num(m.group(0)), t)
    t = re.sub(r"tháng bốn\b", "tháng tư", t)
    return re.sub(r"\s+", " ", t).strip()
def vn(x, d=1):   # 1234.5 -> '1.234,5'
    s = ("{:,.%df}" % d).format(x); return s.replace(",", "X").replace(".", ",").replace("X", ".")
def pct(x, d=1, sign=True): return (("+" if x > 0 else "−") if sign and x != 0 else "") + vn(abs(x), d) + "%"
# ---- dữ liệu
KQ = {x['s']: x for x in hncodec.load(CW + '/data/kqkd.bin')['items']}
_F = hncodec.load(CW + '/data/fund.bin')['v']; FN = _F['f']; FD = _F['d']
def fund(s): return dict(zip(FN, FD.get(s, [])))
SEC = hncodec.load(CW + '/data/sec.bin')['m']
RECENT = hncodec.load(CW + '/data/c/recent.bin')['b']
def _arr(v): return json.loads(v) if isinstance(v, str) else v
def daily(sym):
    c = hncodec.load(CW + '/data/c/%s.bin' % sym)
    d0 = datetime.date.fromisoformat(c['d0']); g = _arr(c['g']); o, h, l, cl, v = [_arr(c[k]) for k in 'ohlcv']
    rows = {}; d = d0
    for i in range(len(g)):
        d = d + datetime.timedelta(days=g[i]) if i else d0
        rows[d.isoformat()] = [o[i], h[i], l[i], cl[i], v[i]]
    for r in RECENT.get(sym, []): rows[r[0]] = list(r[1:6])
    return sorted([[k] + v for k, v in rows.items()])
def weekly(sym, n=52):
    W = {}
    for r in daily(sym):
        dt = datetime.date.fromisoformat(r[0]); mon = (dt - datetime.timedelta(days=dt.weekday())).isoformat()
        if mon not in W: W[mon] = [mon, r[1], r[2], r[3], r[4], r[5]]
        else: w = W[mon]; w[2] = max(w[2], r[2]); w[3] = min(w[3], r[3]); w[4] = r[4]; w[5] += r[5]
    L = [[w[0]] + [round(x / 100, 2) for x in w[1:5]] + [w[5]] for w in sorted(W.values())][-n:]
    return L[::-1]   # mới nhất trước
def circles(wk):   # wk mới nhất trước -> vòng tròn đỉnh, đáy, tuần cuối (chỉ số theo thứ tự thời gian)
    ch = wk[::-1]; n = len(ch)
    ih = max(range(n), key=lambda i: ch[i][2]); il = min(range(n), key=lambda i: ch[i][3])
    f = lambda d: "%d/%d/%s" % (int(d[8:]), int(d[5:7]), d[2:4])
    return [[ih, ch[ih][2], "Đỉnh tuần %s: %s" % (f(ch[ih][0]), vn(ch[ih][2], 2)), 0.6],
            [il, ch[il][3], "Đáy tuần %s: %s" % (f(ch[il][0]), vn(ch[il][3], 2)), 1.6],
            [n - 1, ch[-1][4], "Tuần %s: %s" % (f(ch[-1][0]), vn(ch[-1][4], 2)), 2.6]]
def close(sym): return daily(sym)[-1][4] / 100
def bq(sym, part, name):
    b = hncodec.load(CW + '/data/bctc/%s.bin' % sym)['q']
    for r in b[part]:
        if r[0] == name: return r[2]   # mới nhất trước
    return None
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255); CC = (WHITE, GOLD)
import unicodedata
def slug(t, n=72):
    t = unicodedata.normalize('NFD', t.replace('đ', 'd').replace('Đ', 'D')); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn').lower()
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    if len(t) > n: t = t[:n].rsplit('-', 1)[0]
    return t
def noi(s):   # câu kqkd -> lời nói
    s = s.replace("LNST công ty mẹ", "Lợi nhuận sau thuế công ty mẹ")
    s = re.sub(r"\(([+−])([\d.,]+%)( so với cùng kỳ)?\)", lambda m: ", " + ("tăng " if m.group(1) == "+" else "giảm ") + m.group(2) + (m.group(3) or ""), s)
    s = re.sub(r"\((gấp [\d,]+ lần)\)", r", \1", s)
    s = re.sub(r"\(chuyển từ lãi sang lỗ so với cùng kỳ\)", ", chuyển từ lãi sang lỗ so với cùng kỳ", s)
    s = re.sub(r"(giảm|tăng) [+−]", r"\1 ", s)
    s = re.sub(r"[+]([\d.,]+%)", r"tăng \1", s); s = re.sub(r"−([\d.,]+%)", r"giảm \1", s)
    s = re.sub(r"\(([^)]*)\)", r", \1", s); s = re.sub(r":\s*", " đạt ", s); s = re.sub(r"\s+,", ",", s)
    return s.rstrip(". ") + "."
def ql(q):   # 'Q3/26' -> 'Q3/26' giữ để doc() đọc
    return q
def dong_tien(x): return vn(x, 0) if abs(x) >= 100 else vn(x, 1)
CS_AN = ["Cần trao đổi riêng về danh mục: Zalo 0365.188.286", "Chia sẻ góc nhìn, không phải khuyến nghị mua bán."]
def mo_ta(title, nguon, seri, link):
    return ("%s. %s\n\nDữ liệu từng mã và tài liệu kèm video: https://chungkhoanhuynguyen.com\n📂 Thư viện bài học: https://chungkhoanhuynguyen.com/hoc/\n\n%s\n%s\n\n📚 Seri %s – bài viết, bảng số và tài liệu kèm video: %s\n📂 Thư viện bài học: https://chungkhoanhuynguyen.com/hoc/"
            % (title, nguon, CS_AN[0], CS_AN[1], seri, link))
def fb(h, pts, q, link, icon="📌"):
    return "%s %s\n\n%s\n\n%s\n\n🎬 Xem đầy đủ: {LINK}\n%s\n📚 Tài liệu: %s" % (icon, h, "\n".join("👉 " + p for p in pts), q, CS_AN[0], link)
def dem(scenes): return sum(len(c['say'].split()) for c in scenes)
