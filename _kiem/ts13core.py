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
import os as _os
PBS = _os.environ.get("PBS", "vnd"); WEEK = _os.environ.get("WEEK", "0") == "1"; LIQ = float(_os.environ.get("LIQ", "0")); NR = int(_os.environ.get("NR", "1000"))
TAG = f"[{PBS} {'tuan' if WEEK else 'thang'} TK>={LIQ:g}ty]"
HERE = os.path.dirname(os.path.abspath(__file__))
FD = json.load(open(os.path.join(HERE, "ts_data.json")))["d"]      # [pb, roe_q, nim_q, npl, cov]
BANKS = sorted(FD)
T0 = int(datetime.datetime(2017, 6, 1).timestamp()); T1 = int(time.time()) + 86400
import pickle
CACHE = "/tmp/ts13_cache.pkl"
if _os.path.exists(CACHE):
    RAW, RB, RE = pickle.load(open(CACHE, "rb"))
else:
    RAW = {}
    for s in BANKS + ["VNINDEX"]:
        j = get(f"{S2}?resolution=D&symbol={s}&from={T0}&to={T1}")
        if j and j.get("c"):
            RAW[s] = {datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"): (o, c, v) for t, o, c, v in zip(j["t"], j["o"], j["c"], j["v"]) if c}
    RB, RE = {}, {}
    for s in BANKS:
        for code, dst in (("PRICE_TO_BOOK", RB), ("PRICE_TO_EARNINGS", RE)):
            j = get(f"{S3}ratios?q=code:{s}~ratioCode:{code}&sort=reportDate:asc&size=5000&fields=reportDate,value") or {}
            dst[s] = {x["reportDate"]: x["value"] for x in j.get("data", []) if isinstance(x.get("value"), (int, float)) and x["value"] > 0}
        print("tai", s, "gia", len(RAW.get(s, {})), "pb", len(RB[s]), "pe", len(RE[s]), "tu", min(RB[s]) if RB[s] else None, flush=True)
    pickle.dump((RAW, RB, RE), open(CACHE, "wb"))
cnt = Counter(d for s in BANKS for d in RAW.get(s, {}))
CAL = sorted(d for d in cnt if cnt[d] >= 5 and d >= "2017-12-15")
N = len(CAL); print("so phien", N, CAL[0], CAL[-1], flush=True)
C, O, PB, PE = {}, {}, {}, {}
ADV = {}
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
    vv = [0.0] * N
    for k, d in enumerate(CAL):
        if d in raw and len(raw[d]) > 2 and raw[d][2] and raw[d][1]: vv[k] = raw[d][1] * 1000 * raw[d][2]
    adv = [None] * N; acc = 0.0
    for k in range(N):
        acc += vv[k]
        if k >= 20: acc -= vv[k - 20]
        if k >= 19: adv[k] = acc / 20
    ADV[s] = adv
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
    if len(hist) < 20: return None
    d = CAL[k]; d5 = (datetime.date.fromisoformat(d) - datetime.timedelta(days=1826)).isoformat()
    ex = [v for dq, v in EXTRA[s] if dq >= d5]
    f = asof(s, d) or {}
    hs = sorted(hist)
    f.update(pb=pbk, mn=min(hist + ex), pct=sum(1 for x in hist if x < pbk) / len(hist), med=st.median(hist), p20=hs[int(0.2 * len(hs))],
             pe=PE[s][k], c=C[s][k])
    w = [x for x in C[s][max(0, k - 49):k + 1] if x]; f["ma50"] = C[s][k] >= sum(w) / len(w)
    w = [x for x in C[s][max(0, k - 59):k + 1] if x]; f["bat"] = C[s][k] >= 1.10 * min(w)
    return f
if PBS == "wi":
    for s_ in BANKS:
        qs = sorted((int(k_[:4]), int(k_[5])) for k_ in FD[s_])
        bv = []
        for q in qs:
            pbq = FD[s_][f"{q[0]}Q{q[1]}"][0]; ke = idx_le(qend(*q).isoformat())
            if pbq and ke is not None and C[s_][ke] and (datetime.date.fromisoformat(CAL[ke]) - qend(*q)).days < 10:
                bv.append(((qend(*q) + datetime.timedelta(days=30)).isoformat(), C[s_][ke] / pbq))
        j_ = 0; cur = None; npb = [None] * N
        for k_ in range(N):
            while j_ < len(bv) and bv[j_][0] <= CAL[k_]: cur = bv[j_][1]; j_ += 1
            if cur and C[s_][k_]: npb[k_] = C[s_][k_] / cur
        a_ = [x for x in npb if x]; b_ = [x for x in PB[s_][-60:] if x]; c_ = [x for x in npb[-60:] if x]
        if b_ and c_: print("  PB nguon moi", s_, "hom nay", round(npb[-1] or 0, 2), "| nguon cu", round(PB[s_][-1] or 0, 2), "| so diem", len(a_), flush=True)
        PB[s_] = npb
ME = [k for k in range(N - 1) if ((datetime.date.fromisoformat(CAL[k]).isocalendar()[1] != datetime.date.fromisoformat(CAL[k + 1]).isocalendar()[1]) if WEEK else (CAL[k][:7] != CAL[k + 1][:7])) and CAL[k] >= "2017-12-01"]
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
    if len(qs) < 4: return None
    R = [FD[s][f"{q[0]}Q{q[1]}"] for q in qs]
    def tb(i, lo, hi, m=1.0):
        v = [min(hi, max(lo, r[i])) * m for r in R if r[i] is not None]
        return sum(v) / len(v) if len(v) >= 3 else None
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
DEC = [k for i_, k in enumerate(ME) if CAL[k][5:7] == "12" and CAL[k] >= "2019-12-01" and (i_ + 1 == len(ME) or CAL[ME[i_ + 1]][5:7] != "12")]
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


def tb_dinh(s, k):
    d = CAL[k]; y0 = int(d[:4]); mx = []
    for y in range(y0 - 5, y0):
        w = [PB[s][i] for i in range(max(0, k - 1300), k) if PB[s][i] and CAL[i][:4] == str(y)]
        if len(w) >= 150: mx.append(max(w))
    return sum(mx) / len(mx) if len(mx) >= 3 else None
def snap_hi(k):
    out = []
    for s in BANKS:
        f = F[k][s]
        if not f: continue
        x = tb5(s, CAL[k]); h = tb_dinh(s, k)
        if x and h: out.append((math.log(h), dict(lroe=math.log(max(0.03, x["roe"]))), s))
    return out
MH = {}
for k in ME + [N - 1]:
    ks = tuple([d for d in DEC if d < k] or [DEC[0]])
    if ks not in MH:
        rows = [r for d in ks for r in snap_hi(d)]
        MH[ks] = fit(rows, ["lroe"], 0.0) if len(rows) >= 8 else None
    for s in BANKS:
        f = F[k][s]
        if f and "x5" in f:
            f["hi_own"] = tb_dinh(s, k)
            if MH[ks]: f["hi"] = pred(MH[ks], f["x5"])
mh = MH[max(MH, key=len)]
print("CONG THUC P/B CAO TB 5 NAM THEO ROE: PB =", round(math.exp(mh[0] - mh[3][0] / mh[2][0] * mh[1][0]), 3), "x ROE^", round(mh[3][0] / mh[2][0], 3), "| so quan sat", len([r for d in DEC for r in snap_hi(d)]))

import random
C2 = json.load(open(os.path.join(HERE, "ts_c2.json"))); END = N
NEXT = {k + 1: i for i, k in enumerate(ME)}
BUY = lambda f: f["pb"] <= f["m1"] and q1(f)
SELL = lambda f: f["pb"] >= f["mm"] * 1.2
NAVD = {}
def run(mode, si=0, banks=BANKS, rng=None, kj=1.0, sj=1.0, skip=0.0, log=None):
    cash = 1.0; pos = {}; t0 = ME[si]; pk = 1.0; dd = 0.0; nv = 1.0
    for t in range(t0, END):
        cash *= (1 + 0.05 / 250)
        i = NEXT.get(t)
        if i is not None and i >= si:
            k = ME[i]
            for x in list(pos):
                f = F[k][x]; u, pm, dm, fails, lq = pos[x]
                if f and f.get("q") and f["q"] != lq and "roe" in f:
                    lq = f["q"]; fails = fails + 1 if not qua(q1, f) else 0
                pos[x] = (u, pm, dm, fails, lq)
                ly = None
                if f and O[x][t] and qua(lambda f: f["pb"] >= f["mm"] * 1.2 * sj, f): ly = "cham gia ban"
                elif mode == 9 and f and O[x][t] and f.get("hi_own") and f["pb"] >= f["hi_own"] * 0.9 * sj: ly = "cham 90% dinh TB rieng"
                elif mode >= 1 and fails >= (1 if mode == 9 else mode): ly = f"truot loc {fails} quy"
                if ly:
                    pos.pop(x); cash += u * O[x][t] * 0.9975
                    if log is not None: log.append([x, dm, pm, CAL[t], O[x][t], O[x][t] * 0.9975 / pm - 1, ly])
            nv = cash + sum(p[0] * C[x][t] for x, p in pos.items())
            c = sorted((F[k][x]["pb"] / F[k][x]["m1"], x) for x in banks if x not in pos and O[x][t] and qua(lambda f: f["pb"] <= f["m1"] * kj and q1(f), F[k][x]) and (LIQ <= 0 or (ADV[x][t - 1] or 0) >= LIQ * 1e9))
            for _, x in c:
                if len(pos) >= 5: break
                if rng and rng.random() < skip: continue
                amt = min(nv / 5, cash)
                if amt < 0.01 * nv: break
                px = O[x][t] * 1.0015 * (1 + (rng.uniform(-0.02, 0.02) if rng else 0)); pos[x] = (amt / px, px, CAL[t], 0, F[k][x].get("q")); cash -= amt
        nv = cash + sum(p[0] * C[x][t] for x, p in pos.items())
        if log is not None: NAVD[CAL[t][:4]] = (nv, C["VNINDEX"][t])
        if nv > pk: pk = nv
        elif nv / pk - 1 < dd: dd = nv / pk - 1
    if log is not None:
        for x, p in pos.items(): log.append([x, p[2], p[1], "", C[x][N - 1], C[x][N - 1] / p[1] - 1, "dang cam"])
    yrs = (END - t0) / 250
    return nv ** (1 / yrs) - 1, dd, nv
TEN = {0: "V2 (chi ban o gia ban)", 1: "V2 + truot loc 1 quy la ban", 9: "V2 + truot loc + ban o 90% dinh TB rieng"}
for mode in (1,):
    lg = []; NAVD = {}; c, d, nv = run(mode, log=lg)
    YR = []; pv = (1.0, C["VNINDEX"][ME[0]])
    for y in sorted(NAVD):
        if y < "2018": continue
        YR.append((y, NAVD[y][0] / pv[0] - 1, NAVD[y][1] / pv[1] - 1)); pv = NAVD[y]
    w = [r for r in lg if r[6] != "dang cam"]
    print(f"\n#KQ {TAG} DUONG LICH SU: x{nv:.2f} | {c * 100:.1f}%/nam | sut {d * 100:.1f}% | lenh {len(lg)}, da ban {len(w)}, thang {sum(1 for r in w if r[5] > 0)}/{len(w)}")
    print(f"#KQ {TAG} nam: " + " ".join(f"{y}:{a * 100:+.0f}%" for y, a, b in YR))
    for r in sorted(lg, key=lambda r: r[1]):
        print(f"#LENH {TAG} {r[0]} | {r[1]} | {r[2]:.2f} | {r[3] or '-'} | {r[4]:.2f} | {r[5] * 100:+.1f}% | {r[6]}")
R = {m: [] for m in (1,)}
print("#KQ", TAG, "so moc xet", len(ME), CAL[ME[0]], "| model dau tien khop tai", CAL[DEC[0]], "-> 2018-2019 dung cong thuc khop 12/2019 (nhin truoc 1-2 nam)")
NLIM = sum(1 for k in ME if CAL[k] <= "2023-11-30")
for r in range(NR):
    g = random.Random(1000 + r); si = g.randrange(0, NLIM); banks = [b for b in BANKS if g.random() < 0.7]
    kj = g.uniform(0.95, 1.05); sj = g.uniform(0.95, 1.05)
    for m in (1,): R[m].append(run(m, si, banks, random.Random(5000 + r), kj, sj, 0.15)[:2])
def pcx(a, p): a = sorted(a); return a[min(len(a) - 1, int(p * len(a)))]

for m in (1,):
    c = [v[0] for v in R[m]]; d = [v[1] for v in R[m]]
    print(f"#KQ {TAG} 1000 LAN | lai/nam giua {pcx(c, .5) * 100:.1f}% (5% xau {pcx(c, .05) * 100:.1f}% .. tot {pcx(c, .95) * 100:.1f}%) | sut giua {pcx(d, .5) * 100:.0f}% (5% xau {pcx(d, .05) * 100:.0f}%) | lan lo ca giai doan: {sum(1 for v in c if v < 0) / len(c) * 100:.0f}%")
