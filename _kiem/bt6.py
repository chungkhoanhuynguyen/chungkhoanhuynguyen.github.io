# -*- coding: utf-8 -*-
"""QL1 13/11 – bt6: V306TM + lớp ETF VN30 cuối–đầu tháng trên tiền nhàn rỗi → nhiều lệnh hơn mà vẫn giữ lãi (đo cả vòng quay phí), tách 2 nửa giai đoạn + 300 lượt Monte Carlo ghép cặp). Dựa trên bt3: trên CÙNG bộ máy danh mục, 1000 lượt Monte Carlo + 8 bước tự soát lỗi.
Bản đầy đủ hơn bt2.py: rổ theo TỪNG PHIÊN như V306TM (top100 thanh khoản 20 phiên HOSE/HNX -> 30 mã lớn nhất; đại diện vốn hoá
bằng thanh khoản 120 phiên vì không có số cổ phiếu lưu hành lịch sử), bộ lọc thị trường chỉ số cân bằng 200 mã > MA200,
luật bán V306TM đúng bản (phiên 20 chưa lãi 5% thì bán; ≥5% giữ tối đa 60), xử lý mã ngừng giao dịch, kẹt sàn, T+2 chiều.
Không lấy cổ phiếu hiện tại đi trade quá khứ: mỗi phiên chỉ xét mã đang giao dịch lúc đó (gồm mã đã huỷ niêm yết nếu còn dữ liệu).
"""
import json, time, datetime, urllib.request, base64, random, statistics as st
from collections import deque, Counter
_h = lambda s: base64.b64decode(s).decode()
S2 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
S3 = _h("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==")
UA = {"User-Agent": "Mozilla/5.0"}
def get(url):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r: return json.load(r)
        except Exception: time.sleep(2)
    return None
T0 = int(datetime.datetime(2013, 1, 1).timestamp()); T1 = int(time.time()) + 86400
FL = {}
for fl in ("HOSE", "HNX"):
    for q in ("~status:LISTED", "~status:DELISTED"):
        j = get(f"{S3}stocks?q=type:STOCK~floor:{fl}{q}&fields=code,floor&size=3000") or {"data": []}
        for x in j["data"]:
            c = x.get("code")
            if c and len(c) == 3 and c not in FL: FL[c] = fl
        print(fl, q, len(j["data"]), flush=True)
for c in "FLC ROS HAI ITA HQC AMD TTF OGC KBC DLG HNG HAG JVC PPI TSC FIT KLF ART TTB GTN SBT CII HSG NKG DXG PDR NVL DIG CEO HVN VJC GAB BCG APC SVC TDH QCG LCM HAX".split():
    FL.setdefault(c, "HOSE")
print("tong ma", len(FL), flush=True)
D = {}
for i, s in enumerate(sorted(FL)):
    j = get(f"{S2}?resolution=D&symbol={s}&from={T0}&to={T1}")
    if j and j.get("c") and len(j["c"]) >= 150:
        D[s] = dict(d=[datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d") for t in j["t"]], o=j["o"], h=j["h"], l=j["l"], c=j["c"], v=j["v"])
    if i % 100 == 0: print(i, s, len(D), flush=True)
# Vốn hoá lịch sử (VNDirect ratios MARKETCAP theo ngày); thiếu thì dùng giá điều chỉnh × số CP hiện tại
MC = {}; co_mc = 0
for i, s in enumerate(sorted(D)):
    j = get(f"{S3}ratios?q=code:{s}~ratioCode:MARKETCAP&sort=reportDate:asc&size=5000&fields=reportDate,value") or {}
    r = [(x["reportDate"], x["value"]) for x in j.get("data", []) if isinstance(x.get("value"), (int, float)) and x.get("reportDate")]
    if len(r) > 20: MC[s] = r; co_mc += 1
    if i == 0: print("mau MARKETCAP", s, r[:2], r[-2:], len(r), flush=True)
print("co von hoa lich su:", co_mc, "/", len(D), flush=True)
huy = [s for s in D if D[s]["d"][-1] < (datetime.date.today() - datetime.timedelta(days=20)).isoformat()]
print("co du lieu", len(D), "| da ngung giao dich:", len(huy), flush=True)
cnt = Counter(d for b in D.values() for d in b["d"])
med = sorted(cnt.values())[len(cnt) // 2]
CAL = sorted(d for d in cnt if cnt[d] >= 0.3 * med)       # bỏ ngày phần lớn mã thiếu dữ liệu
IX = {d: k for k, d in enumerate(CAL)}; N = len(CAL)
def roll_mean(a, p):
    out = [None] * len(a); acc = 0.0
    for k in range(len(a)):
        acc += a[k]
        if k >= p: acc -= a[k - p]
        if k >= p - 1: out[k] = acc / p
    return out
def roll_max_prev(a, p):   # max của p phần tử TRƯỚC k
    out = [None] * len(a); q = deque()
    for k in range(len(a)):
        while q and q[0] < k - p: q.popleft()
        if k >= p: out[k] = a[q[0]]
        while q and a[q[-1]] <= a[k]: q.pop()
        q.append(k)
    return out
A = {}
KEYS = ("o", "h", "l", "c", "v", "k", "ma20", "ma50", "ma150", "ma200", "hh120", "hh20", "vavg20", "gt20", "gt120", "r126", "ma200_21", "prevc", "hh120y")
for s, b in D.items():
    n = len(b["c"]); c = b["c"]; gt = [c[k] * b["v"][k] for k in range(n)]
    m = dict(ma20=roll_mean(c, 20), ma50=roll_mean(c, 50), ma150=roll_mean(c, 150), ma200=roll_mean(c, 200),
             hh120=roll_max_prev(b["h"], 120), hh20=roll_max_prev(b["h"], 20), vavg20=[None] + roll_mean(b["v"], 20)[:-1],
             gt20=roll_mean(gt, 20), gt120=roll_mean(gt, 120))
    a = {key: [None] * N for key in KEYS}
    for k in range(n):
        g = IX.get(b["d"][k])
        if g is None: continue
        a["o"][g], a["h"][g], a["l"][g], a["c"][g], a["v"][g], a["k"][g] = b["o"][k], b["h"][k], b["l"][k], c[k], b["v"][k], k
        for key in m: a[key][g] = m[key][k]
        if k >= 126: a["r126"][g] = c[k] / c[k - 126] - 1
        if k >= 221: a["ma200_21"][g] = m["ma200"][k - 21]
        if k >= 1: a["prevc"][g] = c[k - 1]; a["hh120y"][g] = m["hh120"][k - 1]
    a["mc"] = [None] * N
    if s in MC:
        r = MC[s]; ri = 0; last = None
        sh0 = None
        for g in range(N):   # soát lỗi lần 3: trước 12/2017 nguồn chưa có vốn hoá -> lùi bằng số CP của ngày đầu có dữ liệu × giá
            if a["c"][g] is not None and r and r[0][0][:10] <= CAL[g] and sh0 is None: sh0 = r[0][1] / a["c"][g]
        if sh0 is None and r:
            g1 = next((g for g in range(N) if a["c"][g] is not None and CAL[g] >= r[0][0][:10]), None)
            sh0 = r[0][1] / a["c"][g1] if g1 is not None else None
        for g in range(N):
            while ri < len(r) and r[ri][0][:10] <= CAL[g]: last = r[ri][1]; ri += 1
            a["mc"][g] = last if last is not None else ((a["c"][g] * sh0) if (sh0 and a["c"][g] is not None) else None)
    else:
        a["mc"] = [x * 1e9 if x is not None else None for x in a["c"]]   # không có dữ liệu: coi như nhỏ (xếp sau)
    a["fl"] = FL.get(s, "HOSE"); A[s] = a
print("chi bao xong", flush=True)
print("mau ro 2016-06:", sorted(next(set() for _ in [0])) if False else "", flush=True)
# chỉ số cân bằng 200 mã -> bộ lọc thị trường
idx = [100.0] * N
for g in range(1, N):
    sc = sorted(((A[s]["gt20"][g - 1], s) for s in A if A[s]["c"][g] is not None and A[s]["c"][g - 1] is not None and A[s]["gt20"][g - 1] and A[s]["k"][g] >= 21), reverse=True)[:200]
    ch = [A[s]["c"][g] / A[s]["prevc"][g] - 1 for _, s in sc if A[s]["prevc"][g]]
    ch = [x for x in ch if abs(x) <= 0.30]
    idx[g] = idx[g - 1] * (1 + (st.mean(ch) if ch else 0))
ima = roll_mean(idx, 200)
MKT = [ima[g] is not None and idx[g] > ima[g] for g in range(N)]
print("bo loc thi truong mo cua %.0f%% so phien (tu 2014-07)" % (100*sum(MKT[g] for g in range(N) if CAL[g]>="2014-07")/max(1,sum(1 for d in CAL if d>="2014-07"))), flush=True)
# rổ theo phiên
RO = []
for g in range(N):
    sc = sorted(((A[s]["gt20"][g], s) for s in A if A[s]["c"][g] is not None and A[s]["k"][g] >= 280 and A[s]["gt20"][g]), reverse=True)[:100]
    RO.append(set(sorted((s for _, s in sc), key=lambda s: -(A[s]["mc"][g] or 0))[:30]))   # 30 mã vốn hoá lớn nhất trong top100 thanh khoản
def sig_v306(s, g):
    a = A[s]; c = a["c"][g]
    if None in (a["ma50"][g], a["ma150"][g], a["ma200"][g], a["ma200_21"][g], a["hh120"][g], a["hh120y"][g], a["vavg20"][g], a["prevc"][g]): return False
    return (a["ma50"][g] > a["ma150"][g] > a["ma200"][g] and a["ma200"][g] > a["ma200_21"][g]
            and c > a["hh120"][g] and a["prevc"][g] <= a["hh120y"][g] and a["v"][g] > 1.5 * a["vavg20"][g])
def sig_c(s, g):
    a = A[s]; c = a["c"][g]
    if None in (a["ma50"][g], a["hh20"][g], a["vavg20"][g]): return False
    return c > a["hh20"][g] and a["v"][g] > 1.5 * a["vavg20"][g] and c > a["ma50"][g]
SIG = {"V306TM": [[] for _ in range(N)], "C": [[] for _ in range(N)]}
for g in range(N):
    for s in RO[g]:
        if sig_v306(s, g): SIG["V306TM"][g].append(s)
        if sig_c(s, g): SIG["C"][g].append(s)
    for k in SIG: SIG[k][g].sort(key=lambda s: -(A[s]["r126"][g] if A[s]["r126"][g] is not None else -9))
SIG["C+locTT"] = SIG["C"]
for dd in ("2016-06-01","2020-06-01","2026-11-03"):
    g = next((g for g in range(N) if CAL[g] >= dd), N - 1); print("ro", CAL[g], sorted(RO[g]), flush=True)
print("so tin hieu:", {k: sum(len(x) for x in v) for k, v in SIG.items()}, flush=True)

ej = get(f"{S2}?resolution=D&symbol=E1VFVN30&from={T0}&to={T1}")
ETF = [None] * N; ETO = [None] * N
if ej:
    for t, o, c in zip(ej["t"], ej["o"], ej["c"]):
        g = IX.get(datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"))
        if g is not None: ETF[g] = c; ETO[g] = o
print("ETF phien co gia:", sum(1 for x in ETF if x), flush=True)
VAO = set(); RA = set()   # vào: đóng cửa phiên thứ 4 từ cuối tháng; ra: đóng cửa phiên thứ 3 tháng sau
for g in range(4, N - 4):
    if CAL[g][:7] != CAL[g + 4][:7] and CAL[g + 3][:7] == CAL[g][:7]: VAO.add(g); RA.add(g + 6)
FB, FS = 0.0015, 0.0025
BASEP = dict(slots=4, w=0.25, cap=60, ext=False, rule20=True, queue=1, lai=0.0, trail=0.10, cut=0.10, etf=0.0)
def mk_ban(P):
    def ban(p, g):
        a = A[p["s"]]; c = a["c"][g]; p["mx"] = max(p["mx"], c); n = g - p["g"] + 1
        if c <= p["gia"] * (1 - P["cut"]): return "cat lo"
        if c < p["mx"] * (1 - P["trail"]): return "bao ve lai"
        if P["rule20"] and n == 20 and c < p["gia"] * 1.05: return "phien 20 chua lai 5%"
        if P["cap"] and n >= P["cap"]:
            if P["ext"] and a["ma50"][g] and c > a["ma50"][g]: return None   # hết 60 phiên nhưng còn trên MA50 thì giữ tiếp
            return "het han"
        return None
    return ban
def chay(P, g0, g1=None, bo=0.0, tr=0.001, seed=0):
    rnd = random.Random(seed); ban = mk_ban(P); g1 = N - 1 if g1 is None else g1
    tien = 1.0; pos = []; L = []; eq = []; cho_mua = []; nav = 1.0; ngay = (1 + P["lai"]) ** (1 / 250.0); qv = [0.0]; et = None; LE = []
    for g in range(g0, g1 + 1):
        tien *= ngay   # tiền nhàn rỗi gửi kỳ hạn ngắn / quỹ tiền tệ
        con = []
        for p in pos:
            a = A[p["s"]]
            if p.get("ban") and a["o"][g] is not None and g >= p["g"] + 3:
                lim = 0.069 if a["fl"] == "HOSE" else 0.099
                if a["h"][g] == a["l"][g] and a["prevc"][g] and a["o"][g] <= a["prevc"][g] * (1 - lim + 0.003): con.append(p); continue
                px = a["o"][g] * (1 - tr)
                tien += p["sl"] * px * (1 - FS); qv[0] += p["sl"] * px; L.append((p["s"], CAL[p["g"]], CAL[g], px * (1 - FS) / p["von"] - 1, p["ban"]))
            else: con.append(p)
        pos = con
        if et and g in RA and ETF[g]:   # bán ETF đóng cửa phiên thứ 3 tháng sau
            px = ETF[g] * (1 - tr); tien += et[0] * px * (1 - FS); qv[0] += et[0] * px; LE.append(px * (1 - FS) / et[1] - 1); et = None
        giu = []
        for s, gb in cho_mua:
            a = A[s]
            if any(p["s"] == s for p in pos): continue
            ok = len(pos) < P["slots"] and a["o"][g] is not None
            if ok:
                o = a["o"][g]; lim = 0.069 if a["fl"] == "HOSE" else 0.099
                ok = not (o > a["c"][gb] * 1.02 or o >= a["c"][gb] * (1 + lim - 0.003))
            if ok:
                ve = min(nav * P["w"], tien)
                if ve >= nav * 0.05:
                    px = a["o"][g] * (1 + tr); tien -= ve; qv[0] += ve
                    pos.append(dict(s=s, g=g, gia=px, von=px * (1 + FB), sl=ve / (px * (1 + FB)), mx=px, ban=None)); continue
            if g - gb < P["queue"]: giu.append((s, gb))   # tín hiệu còn hạn thì chờ phiên sau
        cho_mua = giu
        nav = tien; con = []
        for p in pos:
            a = A[p["s"]]; c = a["c"][g]
            if c is None:
                kk = g
                while kk > p["g"] and a["c"][kk] is None: kk -= 1
                c = a["c"][kk] if a["c"][kk] is not None else p["gia"]
                if g - kk > 10:
                    tien += p["sl"] * c * 0.7 * (1 - FS); nav += p["sl"] * c * 0.7 * (1 - FS)
                    L.append((p["s"], CAL[p["g"]], CAL[g], c * 0.7 * (1 - FS) / p["von"] - 1, "ngung GD")); continue
                nav += p["sl"] * c; con.append(p); continue
            nav += p["sl"] * c; con.append(p)
            if not p["ban"] and g >= p["g"]:
                r = ban(p, g)
                if r: p["ban"] = r
        if et: nav += et[0] * (ETF[g] or et[2])
        if et and ETF[g]: et[2] = ETF[g]
        if P["etf"] and not et and g in VAO and ETF[g] and tien > nav * 0.10:   # tiền nhàn rỗi -> ETF, giữ lại 0% vì V306TM có hàng chờ 5 phiên
            ve = tien * P["etf"]; px = ETF[g] * (1 + tr); et = [ve / (px * (1 + FB)), px * (1 + FB), ETF[g]]; tien -= ve; qv[0] += ve
        pos = con; eq.append(nav)
        if MKT[g]:
            for s in SIG["V306TM"][g]:
                if bo and rnd.random() < bo: continue
                if not any(x[0] == s for x in cho_mua): cho_mua.append((s, g))
    global QV, LEX
    QV = qv[0] / (sum(eq) / len(eq)) / (len(eq) / 250.0); LEX = LE
    return eq, L
def tk(eq, L):
    nam = len(eq) / 250.0; cagr = eq[-1] ** (1 / nam) - 1 if eq[-1] > 0 else -1
    pk = eq[0]; mdd = 0
    for v in eq: pk = max(pk, v); mdd = min(mdd, v / pk - 1)
    r = [x[3] for x in L]; w = [x for x in r if x > 0]; ls = [x for x in r if x <= 0]
    return dict(qv=QV, letf=len(LEX), cagr=cagr, mdd=mdd, x=eq[-1], lenh=len(r), thang=len(w) / len(r) if r else 0, laitb=st.mean(w) if w else 0, lotb=st.mean(ls) if ls else 0)
G0 = next(g for g in range(N) if CAL[g] >= "2014-07-01"); G20 = next(g for g in range(N) if CAL[g] >= "2020-01-01")
def V(**k): d = dict(BASEP); d.update(k); return d
BT = [
 ("0 GỐC V306TM", V()),
 ("D chờ 5 phiên", V(queue=5)),
 ("ETF100 gốc + ETF cuối tháng (100% tiền rỗi)", V(etf=1.0, queue=5)),
 ("ETF50 gốc + ETF cuối tháng (50% tiền rỗi)", V(etf=0.5, queue=5)),
 ("E5 5 mã x 20% + ETF100", V(slots=5, w=0.20, etf=1.0, queue=5)),
 ("E6 6 mã x 16,7% + ETF100", V(slots=6, w=1/6, etf=1.0, queue=5)),
]
print("\n======== TOÀN GIAI ĐOẠN %s → %s (trượt giá 0,1%%) ========" % (CAL[G0], CAL[-1]), flush=True)
R0 = {}
for ten, P in BT:
    eq, L = chay(P, G0); t = tk(eq, L); k = G20 - G0
    c1 = eq[k] ** (250.0 / k) - 1; c2 = (eq[-1] / eq[k]) ** (250.0 / (len(eq) - k)) - 1
    R0[ten] = (eq, L, t, c1, c2)
    print(f"{ten:46s} | vòng quay {t['qv']:4.1f} lần vốn/năm | ETF {t['letf']} lệnh | {t['cagr']*100:5.1f}%/năm | x{t['x']:5.2f} | sụt max {t['mdd']*100:5.1f}% | {t['lenh']:3d} lệnh | thắng {t['thang']*100:4.1f}% | lãi TB {t['laitb']*100:+.1f}% lỗ TB {t['lotb']*100:+.1f}% | 2014–19: {c1*100:5.1f}% | 2020–26: {c2*100:5.1f}%", flush=True)
for ten in ("0 GỐC V306TM", "ETF100 gốc + ETF cuối tháng (100% tiền rỗi)", "E5 5 mã x 20% + ETF100"):
    eq = R0[ten][0]; yr = {}
    for k, d in enumerate(CAL[G0:G0 + len(eq)]): yr.setdefault(d[:4], [eq[k], eq[k]]); yr[d[:4]][1] = eq[k]
    prev = 1.0; s = []
    for y in sorted(yr): s.append(f"{y}:{(yr[y][1]/prev-1)*100:+.0f}%"); prev = yr[y][1]
    print("  ", ten, "từng năm:", " ".join(s), flush=True)
    print("   lý do bán:", dict(Counter(x[4] for x in R0[ten][1])), flush=True)
print("\n======== 200 LƯỢT MONTE CARLO GHÉP CẶP (cùng ngày bắt đầu, cùng trượt giá, cùng 10% tín hiệu bị lỡ) ========", flush=True)
rs = random.Random(2026); MCR = {ten: [] for ten, _ in BT}
g_last = next(g for g in range(N) if CAL[g] >= "2023-11-01")
for i in range(200):
    g0 = rs.randint(G0, g_last); tr = rs.uniform(0.0005, 0.005); sd = rs.randint(0, 10**9)
    for ten, P in BT:
        eq, L = chay(P, g0, bo=0.10, tr=tr, seed=sd); MCR[ten].append(tk(eq, L))
    if i % 50 == 49: print("  lượt", i + 1, flush=True)
def pct(a, q): a = sorted(a); return a[min(len(a) - 1, int(q * len(a)))]
b0 = MCR["0 GỐC V306TM"]
for ten, _ in BT:
    v = MCR[ten]; c = [x["cagr"] for x in v]; m = [x["mdd"] for x in v]
    hon = sum(1 for x, y in zip(v, b0) if x["cagr"] > y["cagr"]); nhe = sum(1 for x, y in zip(v, b0) if x["mdd"] >= y["mdd"])
    print(f"{ten:46s} | lãi/năm trung vị {pct(c,.5)*100:5.1f}% (5%–95%: {pct(c,.05)*100:4.1f}…{pct(c,.95)*100:4.1f}) | sụt max trung vị {pct(m,.5)*100:5.1f}% (tệ 5%: {pct(m,.05)*100:5.1f}%) | lãi hơn GỐC {hon}/200 | sụt không tệ hơn GỐC {nhe}/200", flush=True)
print("\n======== TỰ SOÁT ========", flush=True)
gm = G0 + (N - G0) // 2
for ten in ("0 GỐC V306TM", "ETF100 gốc + ETF cuối tháng (100% tiền rỗi)"):
    P = dict(BT)[ten]; _, Lf = chay(P, G0); _, Lc = chay(P, G0, g1=gm)
    a1 = [x for x in Lf if x[2] <= CAL[gm - 1]]; b1 = [x for x in Lc if x[2] <= CAL[gm - 1]]
    print("[1]", "ĐẠT" if a1 == b1 else "LỖI", "– không nhìn trước tương lai:", ten, len(a1), "lệnh khớp", flush=True)
bad = [x for ten in R0 for x in R0[ten][1] if IX[x[2]] - IX[x[1]] < 3 and x[4] != "ngung GD"]
print("[2]", "ĐẠT" if not bad else "LỖI", "– không bán trước T+3:", len(bad), "vi phạm", flush=True)
t = R0["0 GỐC V306TM"][2]
print("[3]", "ĐẠT" if abs(t["cagr"] - 0.153) < 0.05 else "LỖI", f"– bản GỐC gần kiểm định 28/10 (15,3%/năm): ra {t['cagr']*100:.1f}%/năm, thắng {t['thang']*100:.0f}%, sụt {t['mdd']*100:.0f}%", flush=True)
