# -*- coding: utf-8 -*-
"""QL1 11/11 – So sánh V306TM và cách C trên CÙNG bộ máy danh mục, 1000 lượt Monte Carlo + 8 bước tự soát lỗi.
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
    a["fl"] = FL.get(s, "HOSE"); A[s] = a
print("chi bao xong", flush=True)
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
    RO.append(set(sorted((s for _, s in sc), key=lambda s: -(A[s]["gt120"][g] or 0))[:30]))
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
print("so tin hieu:", {k: sum(len(x) for x in v) for k, v in SIG.items()}, flush=True)
def ban_v306(p, g):
    c = A[p["s"]]["c"][g]; p["mx"] = max(p["mx"], c); n = g - p["g"] + 1
    if c <= p["gia"] * 0.90: return "cat -10%"
    if c < p["mx"] * 0.90: return "bao ve lai"
    if n == 20 and c < p["gia"] * 1.05: return "phien 20 chua lai 5%"
    if n >= 60: return "du 60 phien"
    return None
def ban_c(p, g):
    a = A[p["s"]]; c = a["c"][g]; n = g - p["g"] + 1
    if c <= p["gia"] * 0.93: return "cat -7%"
    if a["ma20"][g] and c < a["ma20"][g]: return "thung MA20"
    if n >= 40: return "du 40 phien"
    return None
RULE = {"V306TM": (ban_v306, True), "C": (ban_c, False), "C+locTT": (ban_c, True)}
FB, FS = 0.0015, 0.0025
def chay(ten, g0, g1=None, bo=0.0, tr=0.001, seed=0):
    rnd = random.Random(seed); ban, loc = RULE[ten]; g1 = N - 1 if g1 is None else g1
    tien = 1.0; pos = []; L = []; eq = []; cho_mua = []
    for g in range(g0, g1 + 1):
        con = []
        for p in pos:   # bán: mở cửa phiên sau tín hiệu; nếu đó là phiên T+2 thì bán chiều (giá đóng cửa) khi hàng về
            a = A[p["s"]]
            if p.get("ban") and a["o"][g] is not None and g >= p["g"] + 2:
                lim = 0.069 if a["fl"] == "HOSE" else 0.099
                if a["h"][g] == a["l"][g] and a["prevc"][g] and a["o"][g] <= a["prevc"][g] * (1 - lim + 0.003): con.append(p); continue   # sàn trắng
                px = (a["c"][g] if g == p["g"] + 2 else a["o"][g]) * (1 - tr)
                tien += p["sl"] * px * (1 - FS); L.append((p["s"], CAL[p["g"]], CAL[g], px * (1 - FS) / p["von"] - 1, p["ban"]))
            else: con.append(p)
        pos = con
        for s, gb, nav in cho_mua:
            a = A[s]
            if len(pos) >= 4 or any(p["s"] == s for p in pos) or a["o"][g] is None: continue
            o = a["o"][g]; lim = 0.069 if a["fl"] == "HOSE" else 0.099
            if o > a["c"][gb] * 1.02 or o >= a["c"][gb] * (1 + lim - 0.003): continue
            ve = min(nav * 0.25, tien)
            if ve < nav * 0.05: continue
            px = o * (1 + tr); tien -= ve
            pos.append(dict(s=s, g=g, gia=px, von=px * (1 + FB), sl=ve / (px * (1 + FB)), mx=px, ban=None))
        cho_mua = []
        nav = tien; con = []
        for p in pos:
            a = A[p["s"]]; c = a["c"][g]
            if c is None:
                kk = g
                while kk > p["g"] and a["c"][kk] is None: kk -= 1
                c = a["c"][kk] if a["c"][kk] is not None else p["gia"]
                if g - kk > 10:   # ngừng giao dịch hẳn: thoát ở giá cuối −30% (thận trọng)
                    tien += p["sl"] * c * 0.7 * (1 - FS); nav += p["sl"] * c * 0.7 * (1 - FS)
                    L.append((p["s"], CAL[p["g"]], CAL[g], c * 0.7 * (1 - FS) / p["von"] - 1, "ngung GD")); continue
                nav += p["sl"] * c; con.append(p); continue
            nav += p["sl"] * c; con.append(p)
            if not p["ban"] and g >= p["g"]:
                r = ban(p, g)
                if r: p["ban"] = r
        pos = con; eq.append(nav)
        if (not loc) or MKT[g]:
            for s in SIG[ten][g]:
                if bo and rnd.random() < bo: continue
                cho_mua.append((s, g, nav))
    return eq, L
def tk(eq, L):
    nam = len(eq) / 250.0; cagr = eq[-1] ** (1 / nam) - 1 if eq[-1] > 0 else -1
    pk = eq[0]; mdd = 0
    for v in eq: pk = max(pk, v); mdd = min(mdd, v / pk - 1)
    r = [x[3] for x in L]; w = [x for x in r if x > 0]; ls = [x for x in r if x <= 0]
    return dict(cagr=cagr, mdd=mdd, x=eq[-1], lenh=len(r), thang=len(w) / len(r) if r else 0, laitb=st.mean(w) if w else 0, lotb=st.mean(ls) if ls else 0, pf=sum(w) / -sum(ls) if ls else 0)
G0 = next(g for g in range(N) if CAL[g] >= "2014-07-01")
vni = get(f"{S2}?resolution=D&symbol=VNINDEX&from={T0}&to={T1}")
if vni:
    vd = {datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"): c for t, c in zip(vni["t"], vni["c"])}
    a0 = next(vd[d] for d in CAL[G0:] if d in vd); a1 = vd[max(vd)]
    print(f"VN-Index {CAL[G0]} -> {max(vd)}: {((a1/a0)**(250/(N-G0))-1)*100:.1f}%/năm", flush=True)
print("\n======== CƠ SỞ: toàn giai đoạn %s → %s, trượt giá 0,1%% ========" % (CAL[G0], CAL[-1]), flush=True)
BASE = {}
for ten in ("V306TM", "C", "C+locTT"):
    eq, L = chay(ten, G0); t = tk(eq, L); BASE[ten] = (eq, L, t)
    print(f"{ten:8s} | {t['cagr']*100:5.1f}%/năm | x{t['x']:.2f} | sụt max {t['mdd']*100:5.1f}% | {t['lenh']} lệnh | thắng {t['thang']*100:4.1f}% | lãi TB {t['laitb']*100:+.1f}% lỗ TB {t['lotb']*100:+.1f}% | PF {t['pf']:.2f}", flush=True)
    yr = {}
    for k, d in enumerate(CAL[G0:G0 + len(eq)]): yr.setdefault(d[:4], [eq[k], eq[k]]); yr[d[:4]][1] = eq[k]
    prev = 1.0; s = []
    for y in sorted(yr): s.append(f"{y}:{(yr[y][1]/prev-1)*100:+.0f}%"); prev = yr[y][1]
    print("   từng năm:", " ".join(s), flush=True)
    print("   lý do bán:", dict(Counter(x[4] for x in L)), flush=True)
print("\n======== 1000 LƯỢT MONTE CARLO ========", flush=True)
print("Mỗi lượt: ngày bắt đầu ngẫu nhiên 7/2014–11/2023 chạy tới nay (≥3 năm), bỏ lỡ ngẫu nhiên 10% tín hiệu, trượt giá ngẫu nhiên 0,05–0,5%.", flush=True)
rs = random.Random(2026); MC = {"V306TM": [], "C": [], "C+locTT": []}
g_last = next(g for g in range(N) if CAL[g] >= "2023-11-01")
for i in range(1000):
    g0 = rs.randint(G0, g_last); tr = rs.uniform(0.0005, 0.005); sd = rs.randint(0, 10**9)
    for ten in MC:
        eq, L = chay(ten, g0, bo=0.10, tr=tr, seed=sd); MC[ten].append(tk(eq, L))
    if i % 100 == 99: print("  lượt", i + 1, flush=True)
def pct(a, q): a = sorted(a); return a[min(len(a) - 1, int(q * len(a)))]
for ten, v in MC.items():
    c = [x["cagr"] for x in v]; m = [x["mdd"] for x in v]; w = [x["thang"] for x in v]
    print(f"{ten:8s} | lãi/năm trung vị {pct(c,.5)*100:5.1f}% (5%–95%: {pct(c,.05)*100:.1f}%…{pct(c,.95)*100:.1f}%) | lượt lỗ {sum(1 for x in c if x<0)/10:.1f}% | sụt max trung vị {pct(m,.5)*100:.1f}% (tệ 5%: {pct(m,.05)*100:.1f}%) | thắng trung vị {pct(w,.5)*100:.0f}%", flush=True)
for b in ("C", "C+locTT"):
    print(f"V306TM lãi/năm cao hơn {b}: {sum(1 for x, y in zip(MC['V306TM'], MC[b]) if x['cagr'] > y['cagr'])}/1000 lượt | sụt giảm nhẹ hơn: {sum(1 for x, y in zip(MC['V306TM'], MC[b]) if x['mdd'] > y['mdd'])}/1000", flush=True)
cal_ = {t: st.median([x["cagr"] / -x["mdd"] if x["mdd"] < 0 else 0 for x in v]) for t, v in MC.items()}
print("Lãi/năm ÷ sụt max (trung vị, cao = tốt):", {k: round(v, 2) for k, v in cal_.items()}, flush=True)
print("\n======== TỰ SOÁT LỖI (8 lần) ========", flush=True)
OK = [0]
def kiem(n, ten, dk, ghi=""):
    OK[0] += bool(dk); print(f"[{n}] {'ĐẠT' if dk else 'LỖI'} – {ten} {ghi}", flush=True)
gm = G0 + (N - G0) // 2
for t in ("V306TM", "C"):
    _, Lf = chay(t, G0); _, Lc = chay(t, G0, g1=gm)
    a1 = [x for x in Lf if x[2] <= CAL[gm - 1]]; b1 = [x for x in Lc if x[2] <= CAL[gm - 1]]
    kiem(1, f"{t}: không nhìn trước tương lai (chạy tới giữa kỳ = cả kỳ ở nửa đầu)", a1 == b1, f"{len(a1)} lệnh khớp")
e1, _ = chay("C", G0, bo=0.1, seed=7); e2, _ = chay("C", G0, bo=0.1, seed=7)
kiem(2, "chạy lại cùng tham số ra cùng kết quả", e1 == e2)
bad = [x for t in BASE for x in BASE[t][1] if IX[x[2]] - IX[x[1]] < 2]
kiem(3, "không bán trước khi hàng về (T+2 chiều)", not bad, f"{len(bad)} vi phạm")
viol = 0
for t in BASE:
    ev = []
    for s, a, e, r, why in BASE[t][1]: ev += [(IX[a], 1, s), (IX[e], 0, s)]
    held = Counter(); mx = 0
    for g, d, s in sorted(ev):
        held[s] += 1 if d else -1; mx = max(mx, sum(1 for v in held.values() if v > 0))
        if held[s] > 1: viol += 1
    viol += mx > 4
kiem(4, "tối đa 4 mã, không giữ trùng mã", viol == 0, f"{viol} vi phạm")
sai = sum(1 for g in range(G0, N, 23) for s in RO[g] if A[s]["c"][g] is None or A[s]["k"][g] < 280)
moi = [s for s in D if D[s]["d"][0] > "2019-01-01"]
som = [s for s in moi if any(s in RO[g] for g in range(G0, min(N, IX.get(D[s]["d"][0], N) + 280)))]
kiem(5, "rổ chỉ có mã đang giao dịch; mã niêm yết sau không vào rổ trước khi đủ 280 phiên", sai == 0 and not som, f"(mã đã ngừng GD trong dữ liệu: {len(huy)}; mã từng vào rổ rồi ngừng GD: {sum(1 for s in huy if any(s in r for r in RO))})")
r0 = (1 - FS) / (1 + FB) - 1
kiem(6, "phí + thuế được trừ (mua bán cùng giá = %.2f%%)" % (r0 * 100), -0.0045 < r0 < -0.0035)
eq = BASE["V306TM"][0]
kiem(7, "tài sản luôn dương, tiền không âm", min(eq) > 0)
t = BASE["V306TM"][2]
kiem(8, "V306TM gần kiểm định 28/10 (15,3%/năm ±5, thắng 40–60%)", abs(t["cagr"] - 0.153) < 0.05 and 0.4 < t["thang"] < 0.6, f"ra {t['cagr']*100:.1f}%/năm, thắng {t['thang']*100:.0f}%, sụt {t['mdd']*100:.0f}%")
print(f"TỰ SOÁT: {OK[0]}/9 đạt", flush=True)
