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
        if x and n_pb >= 750: out.append((math.log(f["mn"]), dict(x, lroe=math.log(max(0.03, x["roe"]))), s))
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
RULES = [("A0 mua moi thang ", lambda f: True), ("CU dung day 5N", lambda f: f["pb"] <= f["mn"]), ("CU day5N+10% +ROE12NX3", lambda f: f["pb"] <= f["mn"] * 1.1 and q1(f))]
for mm, ten in (("m1", "M1(ROE)"), ("m2", "M2(6 chi so)")):
    for kx in (0.9, 1.0, 1.1, 1.2, 1.3, 1.5):
        RULES.append((f"{ten} PB<=day hop ly x{kx}", lambda f, mm=mm, kx=kx: f["pb"] <= f[mm] * kx))
        RULES.append((f"{ten} x{kx} +ROE12NX3", lambda f, mm=mm, kx=kx: f["pb"] <= f[mm] * kx and q1(f)))
def qua(rule, f):
    if not f: return False
    try: return bool(rule(f))
    except (TypeError, KeyError): return False
def pc(a, p): a = sorted(a); return a[min(len(a) - 1, int(p * len(a)))]
def lai(s, k, h):
    e = k + 1
    if e + h >= N or not O[s][e] or not C[s][e + h]: return None
    return C[s][e + h] / (O[s][e] * 1.0015) - 1
def giam_them(s, k, h=250):
    e = k + 1
    if e + h >= N or not O[s][e]: return None
    w = [x for x in C[s][e:e + h + 1] if x]
    return min(w) / (O[s][e] * 1.0015) - 1
def irr(n, final, T):
    lo, hi = -0.05, 0.10
    for _ in range(80):
        r = (lo + hi) / 2
        if sum((1 + r) ** (T - i) for i in range(n)) > final: hi = r
        else: lo = r
    return (1 + lo) ** 12 - 1
def gop_deu(rule, sym_fix=None):
    cash = 0.0; u = {}; uw = 0.0; kq = None
    for i, k in enumerate(ME):
        cash = cash * (1 + 0.05 / 12) + 1.0
        val = cash + sum(n * C[s][k] for s, n in u.items())
        uw = min(uw, val / (i + 1) - 1)
        Q = [sym_fix] if sym_fix else [s for s in BANKS if qua(rule, F[k][s]) and O[s][k + 1]]
        if Q:
            amt = min(cash, 3.0)
            for s in Q:
                px = O[s][k + 1] * 1.0015
                u[s] = u.get(s, 0) + amt / len(Q) / px
            cash -= amt
    n = len(ME); last = N - 1
    val = cash + sum(nn * C[s][last] for s, nn in u.items())
    T = n - 1 + (datetime.date.fromisoformat(CAL[last]) - datetime.date.fromisoformat(CAL[ME[-1]])).days / 30.4
    top = max((nn * C[s][last] / val for s, nn in u.items()), default=0)
    return val / n, irr(n, val, T), uw, cash / val, top
def f1(x): return f"{x * 100:+.0f}%"

print("\n===== KET QUA (mo hinh chi dung so lieu TRUOC thoi diem mua) =====")
for name, rule in RULES:
    ev = [(s, k) for k in ME for s in BANKS if qua(rule, F[k][s])]
    if not ev: print(f"{name:34s}| khong co tin hieu"); continue
    r = {h: [x for x in (lai(s, k, h) for s, k in ev) if x is not None] for h in (250, 750)}
    a = [x for x in (lai(s, k, 250) for s, k in ev if CAL[k] < "2023-01-01") if x is not None]
    b = [x for x in (lai(s, k, 250) for s, k in ev if CAL[k] >= "2023-01-01") if x is not None]
    gt = [x for x in (giam_them(s, k) for s, k in ev) if x is not None]
    g = gop_deu(rule)
    def seg(x): return f"n={len(x)} tv={f1(st.median(x))} lo={sum(1 for v in x if v < 0) / len(x) * 100:.0f}%" if x else "n=0"
    print(f"{name:34s}| N={len(ev)} nh={len(set(e[0] for e in ev))} thang co hang={len(set(e[1] for e in ev))}/{len(ME)} | 1n {seg(r[250])} p10={f1(pc(r[250], 0.1)) if r[250] else '-'} | 3n {seg(r[750])} | giam them xau={f1(pc(gt, 0.1)) if gt else '-'} | 20-22 {seg(a)} | 23-26 {seg(b)} | gop deu x{g[0]:.2f} IRR {g[1] * 100:.1f}% am {f1(g[2])} cho {g[3] * 100:.0f}%", flush=True)
print("\n===== CONG THUC (khop tren cac moc cuoi nam 2019-2025) =====")
m1, m2, nr = MODEL[max(MODEL, key=len)]
rows = [r for d in DEC for r in snap(d)]
print("so quan sat", len(rows), "| M1: ln(day) =", round(m1[0], 3), "+", round(m1[3][0] / m1[2][0], 3), "x (ln ROE -", round(m1[1][0], 3), ")  => day hop ly = ", round(math.exp(m1[0] - m1[3][0] / m1[2][0] * m1[1][0]), 3), "x ROE^", round(m1[3][0] / m1[2][0], 3))
print("M2 he so chuan hoa (tang 1 do lech chuan -> day thay doi %):", " ".join(f"{c}:{(math.exp(b) - 1) * 100:+.0f}%(tb {mu:.3f} dlc {sd:.3f})" for c, b, mu, sd in zip(COLS, m2[3], m2[1], m2[2])), "| goc", round(math.exp(m2[0]), 3))
def r2(m, rows): 
    yb = sum(r[0] for r in rows) / len(rows); return 1 - sum((r[0] - math.log(pred(m, r[1]))) ** 2 for r in rows) / sum((r[0] - yb) ** 2 for r in rows)
print("R2 trong mau: M1", round(r2(m1, rows), 2), "M2", round(r2(m2, rows), 2))
for cols, lam, ten in ((["lroe"], 0.0, "M1"), (COLS, 2.0, "M2")):
    e = []
    for b in BANKS:
        tr = [r for r in rows if r[2] != b]; te = [r for r in rows if r[2] == b]
        if te: m = fit(tr, cols, lam); e += [abs(math.log(pred(m, r[1])) - r[0]) for r in te]
    print(f"Bo tung ngan hang ra roi du doan lai ({ten}): sai so trung vi {(math.exp(st.median(e)) - 1) * 100:.0f}% | 80% truong hop sai duoi {(math.exp(pc(e, 0.8)) - 1) * 100:.0f}%")
print(f"\n===== BANG {CAL[N - 1]} =====")
print("ma | gia | PB | day thuc 5N | day hop ly M1 | M2 | gia tai day thuc | gia tai M2 x1.0 | x1.1 | x1.2 | x1.3 | ROE5N | NIM5N | noxau5N | baophu5N | CIR5N | duphong/thunhap5N | ROE4q | noxau | dat ROE12NX3")
for s in BANKS:
    f = F[N - 1][s]
    if not f or "m2" not in f: print(s, "| thieu du lieu"); continue
    x = f["x5"]; g = f["c"] / f["pb"]
    print(f"{s} | {f['c']:.2f} | {f['pb']:.2f} | {f['mn']:.2f} | {f['m1']:.2f} | {f['m2']:.2f} | {g * f['mn']:.2f} | {g * f['m2']:.2f} | {g * f['m2'] * 1.1:.2f} | {g * f['m2'] * 1.2:.2f} | {g * f['m2'] * 1.3:.2f} | "
          f"{x['roe'] * 100:.1f} | {x['nim'] * 100:.2f} | {x['npl'] * 100:.2f} | {x['cov'] * 100:.0f} | {x['cir'] * 100:.0f} | {x['prov'] * 100:.0f} | {(f.get('roe') or 0) * 100:.1f} | {(f.get('npl') or 0) * 100:.2f} | {'co' if qua(q1, f) else 'khong'}")
