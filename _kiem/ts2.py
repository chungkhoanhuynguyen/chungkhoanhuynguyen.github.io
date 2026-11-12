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
# ----- Luật -----
def q1(f): return f["roe"] >= 0.12 and f["npl"] < 0.03
def q2(f): return f["roe"] >= 0.15 and f["npl"] < 0.02 and f["cov"] >= 0.70
LOC = [
    ("", lambda f: True),
    ("+ROE>=12,NX<3", q1),
    ("+ROE>=15,NX<2,baophu>=70", q2),
    ("+baophu>=100", lambda f: f["cov"] >= 1.0),
    ("+NIM khong giam", lambda f: f["nim"] >= f["nim4"] * 0.97),
    ("+no xau khong tang", lambda f: f["npl"] <= f["npl4"] * 1.15),
    ("+NIM day 5N (nguoc)", lambda f: len(f["nimh"]) >= 6 and f["nim"] <= min(f["nimh"]) * 1.03),
    ("+baophu day 5N (nguoc)", lambda f: len(f["covh"]) >= 8 and f["cov"] <= min(f["covh"]) * 1.05),
    ("+baophu>=trung vi rieng", lambda f: len(f["covh"]) >= 8 and f["cov"] >= st.median(f["covh"])),
    ("+gia>=MA50", lambda f: f["ma50"]),
    ("+bat>=10% tu day 60p", lambda f: f["bat"]),
    ("+ca nganh hoang", lambda f: f["hoang"]),
    ("+ROE12NX3+gia>=MA50", lambda f: q1(f) and f["ma50"]),
    ("+ROE12NX3+NIM kg giam+NX kg tang", lambda f: q1(f) and f["nim"] >= f["nim4"] * 0.97 and f["npl"] <= f["npl4"] * 1.15),
    ("+ROE15NX2BP70+gia>=MA50", lambda f: q2(f) and f["ma50"]),
    ("+ROE12NX3+ca nganh hoang", lambda f: q1(f) and f["hoang"]),
]
VUNG = [
    ("A0 mua moi thang", lambda f: True),
    ("A1 PB<=day5N", lambda f: f["pb"] <= f["mn"]),
    ("A2 PB<=day5N+10%", lambda f: f["pb"] <= f["mn"] * 1.10),
    ("A3 PB<=day5N+20%", lambda f: f["pb"] <= f["mn"] * 1.20),
    ("A4 PB nhom 20% thap 5N", lambda f: f["pct"] <= 0.20),
    ("A5 PB nhom 10% thap 5N", lambda f: f["pct"] <= 0.10),
    ("A6 PB<=0.8xtrungvi5N", lambda f: f["pb"] <= 0.8 * f["med"]),
    ("A7 PE<=6.5", lambda f: f["pe"] <= 6.5),
    ("A8 PE<=6.5 & PB 20% thap", lambda f: f["pe"] <= 6.5 and f["pct"] <= 0.20),
]
nimnx = lambda f: f["nim"] >= f["nim4"] * 0.97 and f["npl"] <= f["npl4"] * 1.15
RULES = [("A0 mua moi thang ", lambda f: True)]
for x in (5.5, 6, 6.5, 7, 7.5, 8, 9, 10):
    RULES.append((f"PE<={x}", lambda f, x=x: f["pe"] <= x))
    RULES.append((f"PE<={x} +ROE12NX3", lambda f, x=x: f["pe"] <= x and q1(f)))
RULES += [
    ("PE<=7 +NIM kg giam+NX kg tang", lambda f: f["pe"] <= 7 and nimnx(f)),
    ("PE<=7 +ROE12NX3+NIM kg giam+NX kg tang", lambda f: f["pe"] <= 7 and q1(f) and nimnx(f)),
    ("PE<=7 +ca nganh hoang", lambda f: f["pe"] <= 7 and f["hoang"]),
    ("PE<=7 +PB nhom 30% thap", lambda f: f["pe"] <= 7 and f["pct"] <= 0.3),
    ("PE<=7 +PB nhom 20% thap +ROE12NX3", lambda f: f["pe"] <= 7 and f["pct"] <= 0.2 and q1(f)),
    ("PE<=7 +gia>=MA50 +ROE12NX3", lambda f: f["pe"] <= 7 and f["ma50"] and q1(f)),
    ("PE<=7 +baophu>=70 +ROE12NX3", lambda f: f["pe"] <= 7 and f["cov"] >= 0.7 and q1(f)),
    ("PE 7-10 +ROE12NX3 (doi chung)", lambda f: 7 < f["pe"] <= 10 and q1(f)),
    ("PE>10 (doi chung)", lambda f: f["pe"] > 10),
    ("ROE12NX3 khong xet gia (doi chung)", q1),
    ("CU: PB<=day5N+10% +ROE12NX3", lambda f: f["pb"] <= f["mn"] * 1.10 and q1(f)),
    ("PB nhom 20% thap +ROE12NX3+ca nganh hoang", lambda f: f["pct"] <= 0.2 and q1(f) and f["hoang"]),
    ("PB<=0.8xtrungvi5N +ROE12NX3", lambda f: f["pb"] <= 0.8 * f["med"] and q1(f)),
]
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
print("\n===== KET QUA TUNG LUAT (xet cuoi thang, mua mo cua phien sau, phi 0,15%) =====")
print("N=so lan mua | nh=so ngan hang | th=so thang co tin hieu | dot=so dot (gop cac thang lien nhau) | tv=trung vi | lo=ty le lan mua bi lo")
KQ = {}
for name, rule in RULES:
    ev = [(s, k) for k in ME for s in BANKS if qua(rule, F[k][s])]
    if not ev: print(f"{name:44s}| khong co tin hieu"); continue
    dot = 0
    for s in set(e[0] for e in ev):
        ks = sorted(ME.index(k) for ss, k in ev if ss == s); dot += 1 + sum(1 for a, b in zip(ks, ks[1:]) if b - a > 3)
    r = {h: [x for x in (lai(s, k, h) for s, k in ev) if x is not None] for h in (250, 500, 750)}
    gt = [x for x in (giam_them(s, k) for s, k in ev) if x is not None]
    a = [x for x in (lai(s, k, 250) for s, k in ev if CAL[k] < "2023-01-01") if x is not None]
    b = [x for x in (lai(s, k, 250) for s, k in ev if CAL[k] >= "2023-01-01") if x is not None]
    g = gop_deu(rule)
    def seg(x): return f"n={len(x):<4d} tv={f1(st.median(x)):>5s} lo={sum(1 for v in x if v < 0) / len(x) * 100:3.0f}%" if x else "n=0"
    print(f"{name:44s}| N={len(ev):<4d} nh={len(set(e[0] for e in ev)):<2d} th={len(set(e[1] for e in ev)):<2d} dot={dot:<3d}"
          f"| 1n {seg(r[250])} p10={f1(pc(r[250], 0.1)) if r[250] else '-':>5s}| 2n {seg(r[500])}| 3n {seg(r[750])}"
          f"| giam them 12th tv={f1(st.median(gt)) if gt else '-':>5s} xau(p10)={f1(pc(gt, 0.1)) if gt else '-':>5s}"
          f"| 20-22: {seg(a)} | 23-26: {seg(b)}"
          f"| GOP DEU: x{g[0]:.2f} IRR {g[1] * 100:.1f}%/n am sau nhat {f1(g[2])} tien cho {g[3] * 100:.0f}% ma lon nhat {g[4] * 100:.0f}%", flush=True)
    yr = Counter(CAL[k][:4] for s, k in ev)
    ys = []
    for y in sorted(yr):
        x = [v for v in (lai(s, k, 250) for s, k in ev if CAL[k][:4] == y) if v is not None]
        ys.append(f"{y}:{yr[y]}" + (f"/{f1(st.median(x))}" if x else ""))
    print(f"{'':44s}  theo nam (so lan/tv lai 1n): " + "  ".join(ys))
    KQ[name] = ev
if C["VNINDEX"][ME[0]]:
    g = gop_deu(None, "VNINDEX"); print(f"\nDOI CHUNG gop deu VN-Index (chua co co tuc): x{g[0]:.2f} IRR {g[1] * 100:.1f}%/n am sau nhat {f1(g[2])}")
n = len(ME); T = n - 1 + 0.4
print(f"DOI CHUNG gui tiet kiem 5%/nam: x{sum((1 + 0.05 / 12) ** (T - i) for i in range(n)) / n:.2f}")
# ----- Tự soát -----
print("\n===== TU SOAT =====")
WI_NOW = dict(VCB=1.830, BID=1.303, CTG=1.214, TCB=1.266, MBB=1.246, ACB=1.168, VPB=1.180, HDB=1.654, STB=2.122, TPB=0.883, SHB=0.795, LPB=2.404,
              VIB=1.064, MSB=1.301, OCB=0.892, EIB=1.260, NAB=1.018, VAB=0.740, KLB=0.855, SSB=1.235, BAB=0.927, NVB=1.928, BVB=1.421, ABB=1.168, PGB=0.837)
WI_MIN = dict(VCB=1.816, BID=1.287, CTG=0.921, TCB=0.677, MBB=0.863, ACB=1.031, VPB=0.866, HDB=0.971, STB=0.787, TPB=0.771, SHB=0.614, LPB=0.597,
              VIB=0.977, MSB=0.665, OCB=0.675, EIB=1.239, NAB=0.498, VAB=0.447, KLB=0.548, SSB=1.135, BAB=0.838, NVB=1.096, BVB=0.647, ABB=0.457, PGB=0.819)
k0 = idx_le("2021-11-13")
lech = []
for s in BANKS:
    w = [x for x in PB[s][k0:] if x]
    if not w or not PB[s][N - 1]: continue
    a, b = PB[s][N - 1] / WI_NOW[s], min(w) / WI_MIN[s]; lech.append((s, a, b))
print("So voi nguon thu 2 (P/B hom nay ; day 5 nam): " + " ".join(f"{s}:{a:.2f};{b:.2f}" for s, a, b in lech))
print("  -> ty so trung vi hom nay", round(st.median(a for _, a, _ in lech), 3), "| day", round(st.median(b for _, _, b in lech), 3), "(1.00 = khop; lech deu la do cach tinh so sach khac nhau)")
print("1) Khong nhin truoc: chi so quy dung sau ngay ket thuc quy 30 ngay; day/phan vi P/B chi tinh tren cac phien TRUOC ngay xet.")
print("2) He so quy doi diem P/B truoc 12/2017:", " ".join(f"{s}:{len(EXTRA[s])}" for s in BANKS if EXTRA[s]))
ev0 = KQ.get("A0 mua moi thang ", [])
print("3) So lan mua A0:", len(ev0), "| thang:", len(ME), "| trung binh NH moi thang:", round(len(ev0) / len(ME), 1))
for nm in ("PE<=7 +ROE12NX3", "PE<=6.5 +ROE12NX3"):
    ev = KQ.get(nm, []); print("\nTHEO TUNG NGAN HANG –", nm)
    for s in sorted(set(e[0] for e in ev)):
        x = [v for v in (lai(ss, k, 250) for ss, k in ev if ss == s) if v is not None]
        if x: print(f"  {s}: n={len(x)} tv1n={f1(st.median(x))} lo={sum(1 for v in x if v < 0)}/{len(x)} xau nhat={f1(min(x))}")
    lo = sorted((lai(s, k, 250), s, CAL[k]) for s, k in ev if lai(s, k, 250) is not None and lai(s, k, 250) < 0)
    print("  Cac lan lo sau 1 nam:", " ".join(f"{s}@{d}:{f1(v)}" for v, s, d in lo))
    for bo in ("VPB", "MBB", "CTG"):
        x = [v for v in (lai(ss, k, 250) for ss, k in ev if ss != bo) if v is not None]
        print(f"  Bo {bo}: n={len(x)} tv1n={f1(st.median(x))} lo={sum(1 for v in x if v < 0) / len(x) * 100:.0f}%")
# ----- Trạng thái hôm nay -----
print(f"\n===== TRANG THAI {CAL[N - 1]} =====")
print("ma | gia | PB | day5N | cach day | phanvi | PB/trungvi | PE | ROE4q | noxau(1n truoc) | baophu | NIM4q(1n truoc) | >=MA50 | gia de PB=day+10% | gia de vao nhom 20% thap | gia de PE=6.5 | gia de PE=7")
for s in BANKS:
    f = F[N - 1][s]
    if not f: print(s, "| thieu du lieu"); continue
    g = lambda x, m=100, nd=1: "-" if x is None else f"{x * m:.{nd}f}"
    print(f"{s} | {f['c']:.2f} | {f['pb']:.2f} | {f['mn']:.2f} | {f1(f['pb'] / f['mn'] - 1)} | {f['pct'] * 100:.0f}% | {f['pb'] / f['med']:.2f} | {g(f['pe'], 1)} | {g(f.get('roe'))} | "
          f"{g(f.get('npl'), 100, 2)}({g(f.get('npl4'), 100, 2)}) | {g(f.get('cov'), 100, 0)} | {g(f.get('nim'), 100, 2)}({g(f.get('nim4'), 100, 2)}) | {'co' if f['ma50'] else 'khong'} | "
          f"{f['c'] * f['mn'] * 1.1 / f['pb']:.2f} | {f['c'] * f['p20'] / f['pb']:.2f} | {(f['c'] * 6.5 / f['pe']) if f['pe'] else 0:.2f} | {(f['c'] * 7 / f['pe']) if f['pe'] else 0:.2f} | quy {f.get('q')}")
print("\nNH dat tung luat hom nay:")
for name, rule in RULES:
    if name.startswith("A0"): continue
    d = [s for s in BANKS if qua(rule, F[N - 1][s])]
    print(f"  {name:44s}: {' '.join(d) if d else '-'}")
# ----- Dò nguồn dữ liệu dài hơn (không ảnh hưởng kết quả trên) -----
try:
    q = {"query": "query Q($ticker:String!,$period:String!){CompanyFinancialRatio(ticker:$ticker,period:$period){ratio{ticker yearReport lengthReport roe pb bvps eps}}}",
         "variables": {"ticker": "ACB", "period": "Q"}}
    j = get(_h("aHR0cHM6Ly90cmFkaW5nLnZpZXRjYXAuY29tLnZuL2RhdGEtbXQvZ3JhcGhxbA=="), data=json.dumps(q).encode(),
            hdr={"Content-Type": "application/json", "Referer": _h("aHR0cHM6Ly90cmFkaW5nLnZpZXRjYXAuY29tLnZuLw=="), "Origin": _h("aHR0cHM6Ly90cmFkaW5nLnZpZXRjYXAuY29tLnZu")})
    L = (((j or {}).get("data") or {}).get("CompanyFinancialRatio") or {}).get("ratio") or []
    print("\nDO NGUON 2:", len(L), sorted((x["yearReport"], x["lengthReport"]) for x in L)[:3], L[:1], str(j)[:200] if not L else "")
except Exception as e: print("DO NGUON 2 loi", repr(e))
