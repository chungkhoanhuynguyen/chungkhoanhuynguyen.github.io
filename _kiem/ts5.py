# -*- coding: utf-8 -*-
"""QL1 13/11 – ts1: kiểm định ĐIỂM VÀO TÍCH SẢN cổ phiếu ngân hàng.
Câu hỏi: mua khi P/B về đáy 5 năm có chuẩn không; thêm điều kiện gì (ROE, nợ xấu, bao phủ, NIM, giá bật lại...) thì chắc hơn.
Dữ liệu: P/B và P/E THEO NGÀY (VNDirect, từ 12/2017, tính tại thời điểm), giá điều chỉnh theo ngày, chỉ số quý (ROE, NIM, nợ xấu,
bao phủ – file ts_data.json, từ Q4/2016). Chỉ số quý chỉ được dùng sau ngày kết thúc quý 30 ngày (không nhìn trước tương lai).
Xét tín hiệu vào NGÀY GIAO DỊCH CUỐI MỖI THÁNG, mua giá mở cửa phiên kế tiếp, phí 0,15%. Đo: lãi sau 1-2-3 năm, tỷ lệ lỗ,
mức giảm thêm sau khi mua (12 tháng), và mô phỏng góp đều mỗi tháng (tiền chờ hưởng 5%/năm).
"""
import json, time, datetime, urllib.request, base64, os, statistics as st
from collections import Counter
_h = lambda s: base64.b64decode(s).decode()
S2 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
S3 = _h("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==")
UA = {"User-Agent": "Mozilla/5.0"}
def get(url, data=None, hdr=None):
    err = None
    for k in range(3):
        try:
            rq = urllib.request.Request(url, data=data, headers=dict(UA, **(hdr or {})))
            with urllib.request.urlopen(rq, timeout=40) as r: return json.load(r)
        except Exception as e: err = repr(e); time.sleep(2)
    print("LOI", url[-80:], err, flush=True); return None
HERE = os.path.dirname(os.path.abspath(__file__))
FD = json.load(open(os.path.join(HERE, "ts_data.json")))["d"]      # [pb, roe_q, nim_q, npl, cov]
BANKS = sorted(FD)
T0 = int(datetime.datetime(2017, 6, 1).timestamp()); T1 = int(time.time()) + 86400
RAW = {}
for s in BANKS + ["VNINDEX"]:
    j = get(f"{S2}?resolution=D&symbol={s}&from={T0}&to={T1}")
    if j and j.get("c"):
        RAW[s] = {datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"): (o, c) for t, o, c in zip(j["t"], j["o"], j["c"]) if c}
RB, RE = {}, {}
for s in BANKS:
    for code, dst in (("PRICE_TO_BOOK", RB), ("PRICE_TO_EARNINGS", RE)):
        j = get(f"{S3}ratios?q=code:{s}~ratioCode:{code}&sort=reportDate:asc&size=5000&fields=reportDate,value") or {}
        dst[s] = {x["reportDate"]: x["value"] for x in j.get("data", []) if isinstance(x.get("value"), (int, float)) and x["value"] > 0}
    print("tai", s, "gia", len(RAW.get(s, {})), "pb", len(RB[s]), "pe", len(RE[s]), "tu", min(RB[s]) if RB[s] else None, flush=True)
cnt = Counter(d for s in BANKS for d in RAW.get(s, {}))
CAL = sorted(d for d in cnt if cnt[d] >= 5 and d >= "2017-12-15")
N = len(CAL); print("so phien", N, CAL[0], CAL[-1], flush=True)
C, O, PB, PE = {}, {}, {}, {}
RB["VNINDEX"] = {}; RE["VNINDEX"] = {}
for s in BANKS + ["VNINDEX"]:
    c = [None] * N; o = [None] * N; pb = [None] * N; pe = [None] * N; lc = lpb = lpe = None; raw = RAW.get(s, {})
    for k, d in enumerate(CAL):
        if d in raw: o[k], lc = raw[d][0] or raw[d][1], raw[d][1]
        elif lc is not None: o[k] = lc
        c[k] = lc
        if d in RB[s]: lpb = RB[s][d]
        if d in RE[s]: lpe = RE[s][d]
        if lc is not None: pb[k] = lpb; pe[k] = lpe
    # Sửa gai dữ liệu: "sổ sách điều chỉnh" b = giá/PB nhảy >12% rồi quay lại trong 20 phiên = lỗi cập nhật số cổ phiếu
    b = [(c[k] / pb[k]) if (c[k] and pb[k]) else None for k in range(N)]; sua = 0; buoc = []
    k = 1
    while k < N:
        if b[k] and b[k - 1] and not (0.88 <= b[k] / b[k - 1] <= 1.12):
            j2 = next((j for j in range(k + 1, min(N, k + 21)) if b[j] and abs(b[j] / b[k - 1] - 1) < 0.05), None)
            if j2:
                for i in range(k, j2): b[i] = b[k - 1]; pb[i] = c[i] / b[i]
                sua += 1; k = j2; continue
            buoc.append(f"{CAL[k]}x{b[k] / b[k - 1]:.2f}")
        k += 1
    if sua or buoc: print("  soat PB", s, "gai da sua:", sua, "| buoc nhay giu nguyen:", " ".join(buoc[:8]), flush=True)
    C[s], O[s], PB[s], PE[s] = c, o, pb, pe
IX = {d: k for k, d in enumerate(CAL)}
def idx_le(d):      # chỉ số phiên cuối cùng có ngày <= d
    lo, hi = 0, N - 1
    if CAL[0] > d: return None
    while lo < hi:
        m = (lo + hi + 1) // 2
        if CAL[m] <= d: lo = m
        else: hi = m - 1
    return lo
def qend(y, q): return datetime.date(y, 3 * q, [31, 30, 30, 31][q - 1])
# Chỉ số quý -> đặc trưng (ROE, NIM cộng 4 quý)
FQ = {}; EXTRA = {}
for s in BANKS:
    ql = sorted((int(k[:4]), int(k[5])) for k in FD[s]); rows = {q: FD[s][f"{q[0]}Q{q[1]}"] for q in ql}; feat = {}
    for i, q in enumerate(ql):
        l4 = ql[max(0, i - 3):i + 1]
        ok = len(l4) == 4 and (l4[3][0] * 4 + l4[3][1]) - (l4[0][0] * 4 + l4[0][1]) == 3
        roe = sum(rows[x][1] for x in l4) if ok and all(rows[x][1] is not None for x in l4) else None
        nim = sum(rows[x][2] for x in l4) if ok and all(rows[x][2] is not None for x in l4) else None
        feat[q] = dict(roe=roe, nim=nim, npl=rows[q][3], cov=rows[q][4])
    FQ[s] = (ql, feat)
    # điểm P/B cuối quý trước 12/2017 (nguồn quý) để nới cửa sổ đáy 5 năm, quy về thang P/B ngày bằng hệ số trung vị
    rs = []
    for q in ql:
        if (2018, 1) <= q <= (2019, 4) and rows[q][0]:
            k = idx_le(qend(*q).isoformat())
            if k is not None and PB[s][k]: rs.append(PB[s][k] / rows[q][0])
    kk = st.median(rs) if len(rs) >= 4 else None
    EXTRA[s] = [(qend(*q).isoformat(), rows[q][0] * kk) for q in ql if q <= (2017, 3) and rows[q][0]] if kk and 0.6 <= kk <= 1.4 else []
def asof(s, d):
    ql, feat = FQ[s]; dd = datetime.date.fromisoformat(d); i = None
    for j, q in enumerate(ql):
        if qend(*q) + datetime.timedelta(days=30) <= dd: i = j
    if i is None: return None
    f = dict(feat[ql[i]]); f["q"] = ql[i]
    p4 = feat[ql[i - 4]] if i >= 4 else {}
    f["nim4"] = p4.get("nim"); f["npl4"] = p4.get("npl")
    f["covh"] = [feat[ql[j]]["cov"] for j in range(max(0, i - 20), i) if feat[ql[j]]["cov"] is not None]
    f["nimh"] = [feat[ql[j]]["nim"] for j in range(max(0, i - 20), i) if feat[ql[j]]["nim"] is not None]
    return f
def dac_trung(s, k):
    pbk = PB[s][k]
    if not pbk or not C[s][k]: return None
    hist = [x for x in PB[s][max(0, k - 1250):k] if x]
    if len(hist) < 500: return None
    d = CAL[k]; d5 = (datetime.date.fromisoformat(d) - datetime.timedelta(days=1826)).isoformat()
    ex = [v for dq, v in EXTRA[s] if dq >= d5]
    f = asof(s, d) or {}
    hs = sorted(hist)
    f.update(pb=pbk, mn=min(hist + ex), pct=sum(1 for x in hist if x < pbk) / len(hist), med=st.median(hist), p20=hs[int(0.2 * len(hs))],
             pe=PE[s][k], c=C[s][k])
    w = [x for x in C[s][max(0, k - 49):k + 1] if x]; f["ma50"] = C[s][k] >= sum(w) / len(w)
    w = [x for x in C[s][max(0, k - 59):k + 1] if x]; f["bat"] = C[s][k] >= 1.10 * min(w)
    return f
ME = [k for k in range(N - 1) if CAL[k][:7] != CAL[k + 1][:7] and CAL[k] >= "2019-12-01"]
F = {}
for k in ME + [N - 1]:
    F[k] = {s: dac_trung(s, k) for s in BANKS}
    co = [f for f in F[k].values() if f]
    hoang = (sum(1 for f in co if f["pct"] <= 0.2) / len(co) >= 0.4) if co else False
    for f in co: f["hoang"] = hoang
print("thang xet:", len(ME), CAL[ME[0]], "->", CAL[ME[-1]], "| NH co du lieu thang dau:", sum(1 for f in F[ME[0]].values() if f), "thang cuoi:", sum(1 for f in F[ME[-1]].values() if f), flush=True)

# ===== ts3: tìm "P/B đáy hợp lý" từ chất lượng ngân hàng =====
def tb5(s, d):
    """Trung bình 5 năm (tối đa 20 quý đã công bố tính tới ngày d) của ROE năm, NIM năm, nợ xấu, bao phủ, CIR, chi phí dự phòng/thu nhập."""
    ql, feat = FQ[s]; dd = datetime.date.fromisoformat(d)
    qs = [q for q in ql if qend(*q) + datetime.timedelta(days=30) <= dd][-20:]
    if len(qs) < 8: return None
    R = [FD[s][f"{q[0]}Q{q[1]}"] for q in qs]
    def tb(i, lo, hi, m=1.0):
        v = [min(hi, max(lo, r[i])) * m for r in R if r[i] is not None]
        return sum(v) / len(v) if len(v) >= 6 else None
    x = dict(roe=tb(1, -0.02, 0.12, 4), nim=tb(2, 0, 0.03, 4), npl=tb(3, 0, 0.08), cov=tb(4, 0, 3.0), cir=tb(5, 0.1, 1.2), prov=tb(6, -0.1, 0.8))
    return None if any(v is None for v in x.values()) else x
COLS = ["roe", "nim", "npl", "cov", "cir", "prov"]
import math
def fit(rows, cols, lam):
    n = len(rows); yb = sum(r[0] for r in rows) / n
    mu = [sum(r[1][c] for r in rows) / n for c in cols]
    sd = [max(1e-9, (sum((r[1][c] - m) ** 2 for r in rows) / n) ** 0.5) for c, m in zip(cols, mu)]
    Z = [[(r[1][c] - m) / s_ for c, m, s_ in zip(cols, mu, sd)] for r in rows]; p = len(cols)
    A = [[sum(z[i] * z[j] for z in Z) + (lam if i == j else 0) for j in range(p)] + [sum(z[i] * (r[0] - yb) for z, r in zip(Z, rows))] for i in range(p)]
    for i in range(p):
        piv = max(range(i, p), key=lambda r_: abs(A[r_][i])); A[i], A[piv] = A[piv], A[i]
        for r_ in range(p):
            if r_ != i:
                f_ = A[r_][i] / A[i][i]
                A[r_] = [a - f_ * b for a, b in zip(A[r_], A[i])]
    beta = [A[i][p] / A[i][i] for i in range(p)]
    return (yb, mu, sd, beta, cols)
def pred(m, x):
    yb, mu, sd, beta, cols = m
    return math.exp(yb + sum(b * (x[c] - mu_) / s_ for b, c, mu_, s_ in zip(beta, cols, mu, sd)))
def snap(k):
    out = []
    for s in BANKS:
        f = F[k][s]
        if not f: continue
        n_pb = sum(1 for v in PB[s][max(0, k - 1250):k] if v)
        x = tb5(s, CAL[k])
        if x and n_pb >= 480: out.append((math.log(f["mn"]), dict(x, lroe=math.log(max(0.03, x["roe"]))), s))
    return out
DEC = [k for k in ME if CAL[k][5:7] == "12"]
MODEL = {}
for k in ME + [N - 1]:
    ks = [d for d in DEC if d < k] or [DEC[0]]
    if k == DEC[0]: ks = [DEC[0]]
    rows = [r for d in ks for r in snap(d)]
    key = tuple(ks)
    if key not in MODEL: MODEL[key] = (fit(rows, ["lroe"], 0.0), fit(rows, COLS, 2.0), len(rows))
    m1, m2, _ = MODEL[key]
    for s in BANKS:
        f = F[k][s]
        if not f: continue
        x = tb5(s, CAL[k])
        if x:
            x["lroe"] = math.log(max(0.03, x["roe"])); f["m1"] = pred(m1, x); f["m2"] = pred(m2, x); f["x5"] = x
def q1(f): return f["roe"] >= 0.12 and f["npl"] < 0.03

def qua(rule, f):
    if not f: return False
    try: return bool(rule(f))
    except (TypeError, KeyError): return False
def f1(x): return f"{x * 100:+.0f}%"
# Mô hình "P/B trung bình hợp lý" (trung vị 5 năm) theo ROE, khớp giống mô hình đáy
def snap_med(k):
    out = []
    for s in BANKS:
        f = F[k][s]
        if not f: continue
        x = tb5(s, CAL[k])
        if x and sum(1 for v in PB[s][max(0, k - 1250):k] if v) >= 480: out.append((math.log(f["med"]), dict(lroe=math.log(max(0.03, x["roe"]))), s))
    return out
MM = {}
for k in ME + [N - 1]:
    ks = tuple([d for d in DEC if d < k] or [DEC[0]])
    if ks not in MM: MM[ks] = fit([r for d in ks for r in snap_med(d)], ["lroe"], 0.0)
    for s in BANKS:
        f = F[k][s]
        if f and "x5" in f: f["mm"] = pred(MM[ks], f["x5"])
mmL = MM[max(MM, key=len)]
print("CONG THUC TRUNG BINH HOP LY: PB =", round(math.exp(mmL[0] - mmL[3][0] / mmL[2][0] * mmL[1][0]), 3), "x ROE^", round(mmL[3][0] / mmL[2][0], 3))
LOC = {"thuong": q1, "ky": lambda f: f["roe"] >= 0.12 and f["npl"] < 0.025 and f["cov"] >= 0.6 and f["roe"] >= f["x5"]["roe"] * 0.9}
BAN = {"khong ban": lambda f: False, "PB>=trung vi 5N rieng": lambda f: f["pct"] >= 0.5, "PB>=nhom 80% cao 5N rieng": lambda f: f["pct"] >= 0.8,
       "PB>=TB hop ly (cong thuc)": lambda f: f["pb"] >= f["mm"], "PB>=TB hop ly x1.2": lambda f: f["pb"] >= f["mm"] * 1.2, "PB>=day hop ly x1.5": lambda f: f["pb"] >= f["m1"] * 1.5,
       "PB>=day hop ly x2": lambda f: f["pb"] >= f["m1"] * 2.0}
START = ME[0]; NEXT = {k + 1: k for k in ME}
def sim(kb, ban, loc, L=1.0, allin=False, nslot=5):
    cash = 1.0; debt = 0.0; pos = {}; nav = []; inv = []; nb = 0; ns = 0; worst_eq = 9.9
    for t in range(START, N):
        cash *= (1 + 0.05 / 250); debt *= (1 + 0.10 / 250)
        if t in NEXT:
            k = NEXT[t]
            for s in list(pos):
                if qua(BAN[ban], F[k][s]) and O[s][t]:
                    cash += pos.pop(s) * O[s][t] * 0.9975; ns += 1
            pay = min(cash, debt); cash -= pay; debt -= pay
            pv = sum(u * C[s][t] for s, u in pos.items()); nv = cash + pv - debt
            c = sorted((F[k][s]["pb"] / F[k][s]["m1"], s) for s in BANKS if s not in pos and qua(lambda f: f["pb"] <= f["m1"] * kb and LOC[loc](f), F[k][s]) and O[s][t])
            c = [s for _, s in c][:nslot - len(pos)]
            if c:
                room = nv * L - pv
                per = min(room / len(c), 0.5 * nv * L) if allin else nv * L / nslot
                for s in c:
                    amt = min(per, room)
                    if L <= 1.0: amt = min(amt, cash)
                    if amt < 0.01 * nv: continue
                    pos[s] = amt / (O[s][t] * 1.0015); room -= amt; nb += 1
                    if cash >= amt: cash -= amt
                    else: debt += amt - cash; cash = 0.0
        pv = sum(u * C[s][t] for s, u in pos.items()); nv = cash + pv - debt
        nav.append(nv); inv.append(pv / nv if nv > 0 else 9)
        if debt > 0 and pv > 0: worst_eq = min(worst_eq, nv / pv)
    yrs = (N - START) / 250; cagr = nav[-1] ** (1 / yrs) - 1 if nav[-1] > 0 else -1
    pk = 0; dd = 0
    for v in nav: pk = max(pk, v); dd = min(dd, v / pk - 1)
    ye = {}
    for i, v in enumerate(nav): ye[CAL[START + i][:4]] = v
    ys = sorted(y for y in ye if y >= "2020"); prev = ye.get("2019", 1.0); yr = []
    for y in ys: yr.append(f"{y[2:]}:{f1(ye[y] / prev - 1)}"); prev = ye[y]
    return f"x{nav[-1]:.2f} | {cagr * 100:.1f}%/n | sut sau nhat {f1(dd)} | co phieu TB {sum(inv) / len(inv) * 100:.0f}% | mua {nb} ban {ns}" + (f" | von/CP thap nhat {worst_eq * 100:.0f}%" if L > 1 else "") + " | " + " ".join(yr)
print("\n===== MO PHONG TAI KHOAN 1 LAN VON (5 ma x 20%, tien cho 5%/n, xet cuoi thang) – tu", CAL[START], "den", CAL[N - 1])
print("TAI KHOAN TICH SAN THAT (web): 20:+199% 21:+53% 22:-17% 23:+37% 24:+22% 25:+65% 26:+4% (den 28/10)")
for kb in (1.0, 1.1, 1.2):
    for ban in BAN:
        print(f"mua x{kb} loc thuong | ban: {ban:28s} | {sim(kb, ban, 'thuong')}", flush=True)
print("\n--- Loc ky (NX<2.5, baophu>=60, ROE khong giam) ---")
for kb in (1.0, 1.1):
    for ban in ("khong ban", "PB>=TB hop ly (cong thuc)", "PB>=day hop ly x1.5"):
        print(f"mua x{kb} loc ky | ban: {ban:28s} | {sim(kb, ban, 'ky')}", flush=True)
print("\n--- Don het tien vao ma dat (toi da 5 ma, moi ma <=50%) ---")
for kb in (1.0, 1.1):
    for ban in ("khong ban", "PB>=TB hop ly (cong thuc)", "PB>=day hop ly x1.5"):
        for loc in ("thuong", "ky"):
            print(f"ALLIN mua x{kb} loc {loc:6s} | ban: {ban:28s} | {sim(kb, ban, loc, allin=True)}", flush=True)
print("\n--- Margin (lai vay 10%/n; suc mua = von x he so) ---")
for L in (1.3, 1.5, 2.0):
    for kb in (1.0, 1.1):
        for loc in ("thuong", "ky"):
            for ban in ("khong ban", "PB>=TB hop ly (cong thuc)"):
                print(f"MG x{L} mua x{kb} loc {loc:6s} | ban: {ban:28s} | {sim(kb, ban, loc, L=L, allin=True)}", flush=True)
# đối chứng
v0 = [s for s in BANKS if C[s][START]]
ew = sum(C[s][N - 1] / C[s][START] for s in v0) / len(v0); yrs = (N - START) / 250
print(f"\nDOI CHUNG: giu deu {len(v0)} NH tu dau: x{ew:.2f} ({(ew ** (1 / yrs) - 1) * 100:.1f}%/n) | VN-Index: x{C['VNINDEX'][N - 1] / C['VNINDEX'][START]:.2f}")
print(f"\n===== GIA MUA / GIA BAN {CAL[N - 1]} =====")
print("ma | gia | gia mua (day hop ly x1.0) | x1.1 | gia ban = TB hop ly | gia ban = trung vi 5N rieng | gia ban = day hop ly x1.5 | loc thuong | loc ky")
for s in BANKS:
    f = F[N - 1][s]
    if not f or "mm" not in f: continue
    g = f["c"] / f["pb"]
    print(f"{s} | {f['c']:.2f} | {g * f['m1']:.2f} | {g * f['m1'] * 1.1:.2f} | {g * f['mm']:.2f} | {g * f['med']:.2f} | {g * f['m1'] * 1.5:.2f} | {'dat' if qua(LOC['thuong'], f) else '-'} | {'dat' if qua(LOC['ky'], f) else '-'}")
