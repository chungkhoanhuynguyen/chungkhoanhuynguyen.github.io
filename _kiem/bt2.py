# -*- coding: utf-8 -*-
"""QL1 11/11 – So sánh V306TM và cách C (bứt phá đỉnh 20 phiên) trên CÙNG một bộ máy:
- Rổ theo thời điểm: đầu mỗi tháng 30 mã HOSE+HNX thanh khoản lớn nhất 60 phiên trước, chỉ mã đang giao dịch lúc đó,
  có cả mã đã huỷ niêm yết (nếu nguồn còn giá). (Không có số cổ phiếu lưu hành lịch sử nên không xếp theo vốn hoá được.)
- Danh mục: tối đa 4 mã, mỗi lệnh 25% tổng tài sản, không margin. Tín hiệu theo đóng cửa, mua mở cửa phiên sau,
  bỏ nếu mở cửa cao hơn giá tín hiệu >2%. Bán mở cửa phiên sau tín hiệu, sớm nhất phiên T+2 sau ngày mua (dùng giá đóng cửa).
  Phí mua 0,15%, bán 0,15% + thuế 0,1%.
- 1000 lượt mỗi phương pháp: mỗi lượt chọn ngẫu nhiên ngày bắt đầu (2015-07 → 2023-10), chạy 3 năm, bỏ ngẫu nhiên 10% tín hiệu.
"""
import json, time, datetime, urllib.request, base64, random, statistics as st
from collections import defaultdict
_h = lambda s: base64.b64decode(s).decode()
S2 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
S3 = _h("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==")
UA = {"User-Agent": "Mozilla/5.0"}
def get(url):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r: return json.load(r)
        except Exception as e: err = e; time.sleep(2)
    return None
T0 = int(datetime.datetime(2013, 6, 1).timestamp()); T1 = int(time.time()) + 86400
syms = {}
for fl in ("HOSE", "HNX"):
    for q in ("status:LISTED", "status:DELISTED"):
        j = get(f"{S3}stocks?q=type:STOCK~floor:{fl}~{q}&fields=code&size=3000") or {"data": []}
        for x in j["data"]:
            if x.get("code") and len(x["code"]) == 3: syms[x["code"]] = fl
for s in "FLC ROS HAI ITA HQC AMD TTF OGC KBC DLG HNG HAG JVC PPI TSC FIT KLF ART TTB GTN SBT CII DXG GAB BCG APC QCG LCM HAX".split(): syms.setdefault(s, "HOSE")
print("so ma", len(syms), flush=True)
D = {}
for i, s in enumerate(sorted(syms)):
    j = get(f"{S2}?resolution=D&symbol={s}&from={T0}&to={T1}")
    if j and j.get("c") and len(j["c"]) >= 150:
        D[s] = dict(d=[datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d") for t in j["t"]], o=j["o"], h=j["h"], l=j["l"], c=j["c"], v=j["v"])
    if i % 100 == 0: print(i, len(D), flush=True)
print("co du lieu", len(D), flush=True)
cnt = defaultdict(int)
for b in D.values():
    for d in b["d"]: cnt[d] += 1
cal = sorted(d for d, n in cnt.items() if n >= max(30, 0.3 * max(cnt.values()) if d > "2016" else 30))
CI = {d: k for k, d in enumerate(cal)}
N = len(cal)
# đưa mọi mã về lịch chung (None nếu không giao dịch)
for s, b in D.items():
    m = {d: k for k, d in enumerate(b["d"])}
    for f in "ohlcv": b[f + "x"] = [b[f][m[d]] if d in m else None for d in cal]
    c = b["cx"]
    def ma(p):
        out = [None] * N; w = []
        for k in range(N):
            if c[k] is None: w = []; continue
            w.append(c[k]);
            if len(w) > p: w.pop(0)
            if len(w) == p: out[k] = sum(w) / p
        return out
    b["m20"], b["m50"], b["m150"], b["m200"] = ma(20), ma(50), ma(150), ma(200)
    b["gt"] = [(c[k] * b["vx"][k]) if c[k] is not None else 0 for k in range(N)]
    b["n"] = [0] * N; run = 0
    for k in range(N): run = run + 1 if c[k] is not None else 0; b["n"][k] = run
# chỉ số cân bằng (200 mã thanh khoản TB 20 phiên lớn nhất)
idx = [100.0] * N
for k in range(21, N):
    sc = sorted(((sum(b["gt"][k-20:k]) / 20, s) for s, b in D.items() if b["n"][k] >= 21), reverse=True)[:200]
    ch = [D[s]["cx"][k] / D[s]["cx"][k-1] - 1 for _, s in sc if D[s]["cx"][k-1]]
    ch = [x for x in ch if abs(x) <= 0.3]
    idx[k] = idx[k-1] * (1 + (st.mean(ch) if ch else 0))
ima = [None] * N
for k in range(199, N): ima[k] = sum(idx[k-199:k+1]) / 200
mo_cua = [ima[k] is not None and idx[k] > ima[k] for k in range(N)]
# rổ theo tháng
ro = {}
for k in range(N):
    m = cal[k][:7]
    if m in ro: continue
    sc = sorted(((sum(b["gt"][k-60:k]) / 60, s) for s, b in D.items() if b["n"][k] >= 200), reverse=True)[:30]
    ro[m] = {s for _, s in sc}
def r126(b, k): return b["cx"][k] / b["cx"][k-126] - 1 if k >= 126 and b["cx"][k-126] else -9
# tín hiệu mua theo ngày: list (ưu tiên, mã)
def tin_v(b, k):
    c, h, v = b["cx"], b["hx"], b["vx"]
    if b["n"][k] < 230 or not mo_cua[k]: return False
    if not (b["m50"][k] and b["m150"][k] and b["m200"][k] and b["m200"][k-21]): return False
    if not (b["m50"][k] > b["m150"][k] > b["m200"][k] and b["m200"][k] > b["m200"][k-21]): return False
    dinh = max(h[k-120:k]); dinh_hq = max(h[k-121:k-1])
    return c[k] > dinh and not (c[k-1] > dinh_hq) and v[k] > 1.5 * st.mean(v[k-20:k])
def tin_c(b, k):
    c, h, v = b["cx"], b["hx"], b["vx"]
    if b["n"][k] < 60 or not b["m50"][k]: return False
    return c[k] > max(h[k-20:k]) and v[k] > 1.5 * st.mean(v[k-20:k]) and c[k] > b["m50"][k]
SIG = {"V306TM": defaultdict(list), "C": defaultdict(list)}
for k in range(230, N - 1):
    for s in ro[cal[k][:7]]:
        b = D[s]
        if b["cx"][k] is None or b["n"][k] < 60: continue
        if tin_v(b, k): SIG["V306TM"][k].append((r126(b, k), s))
        if tin_c(b, k): SIG["C"][k].append((r126(b, k), s))
for t in SIG.values():
    for k in t: t[k].sort(reverse=True)
print("so tin hieu", {t: sum(len(x) for x in v.values()) for t, v in SIG.items()}, flush=True)
def ban_v(b, p, k):
    c = b["cx"][k]; g = k - p["kb"]
    return c <= p["gia"] * 0.9 or c < p["dinh"] * 0.9 or (g >= 20 and c < p["gia"] * 1.05) or g >= 60
def ban_c(b, p, k):
    c = b["cx"][k]
    return c <= p["gia"] * 0.93 or (b["m20"][k] and c < b["m20"][k]) or k - p["kb"] >= 40
BAN = {"V306TM": ban_v, "C": ban_c}
def chay(ten, k0, k1, bo=0.0, rng=None):
    tien = 1.0; pos = {}; L = []; eq = []; cho_ban = set()
    for k in range(k0, k1):
        # 1) bán ở giá mở cửa các mã có tín hiệu hôm qua
        for s in list(cho_ban):
            b = D[s]; p = pos[s]; px = b["ox"][k]
            if px is None: continue
            if k - p["kb"] < 2: continue
            if b["hx"][k] == b["lx"][k] and b["cx"][k-1] and b["ox"][k] <= b["cx"][k-1] * 0.94: continue   # sàn trắng
            tien += p["sl"] * px * (1 - 0.0025); L.append(px / p["gia"] * (1 - 0.0025) / 1.0015 - 1); del pos[s]; cho_ban.discard(s)
        # 2) mua ở giá mở cửa theo tín hiệu hôm qua
        if k - 1 >= k0:
            ts = sum(p["sl"] * (D[s]["cx"][k-1] or p["gia"]) for s, p in pos.items()) + tien
            for _, s in SIG[ten].get(k - 1, []):
                if len(pos) >= 4: break
                if s in pos or (rng and rng.random() < bo): continue
                b = D[s]; o = b["ox"][k]
                if o is None or o > b["cx"][k-1] * 1.02: continue
                v = min(ts * 0.25, tien)
                if v < ts * 0.05: break
                tien -= v; pos[s] = dict(gia=o, sl=v / (o * 1.0015), kb=k, dinh=o)
        # 3) cuối phiên: cập nhật đỉnh, tín hiệu bán, giá trị
        for s, p in pos.items():
            c = D[s]["cx"][k]
            if c is None: continue
            p["dinh"] = max(p["dinh"], c)
            if BAN[ten](D[s], p, k): cho_ban.add(s)
        eq.append(tien + sum(p["sl"] * (D[s]["cx"][k] or p["gia"]) for s, p in pos.items()))
    nam = (k1 - k0) / 250
    cagr = eq[-1] ** (1 / nam) - 1
    pk = 0; dd = 0
    for x in eq: pk = max(pk, x); dd = min(dd, x / pk - 1)
    return cagr, dd, L, eq
kS = next(k for k in range(N) if cal[k] >= "2015-01") ; kE = N - 1
print("\n===== TOAN GIAI DOAN", cal[kS], "->", cal[kE], "=====", flush=True)
FULL = {}
for ten in ("V306TM", "C"):
    cagr, dd, L, eq = chay(ten, kS, kE)
    FULL[ten] = eq
    w = [x for x in L if x > 0]; ls = [x for x in L if x <= 0]
    print(f"{ten}: {cagr*100:.1f}%/nam | sut giam max {dd*100:.1f}% | {len(L)} lenh | thang {len(w)/max(1,len(L))*100:.1f}% | lai TB {st.mean(w)*100 if w else 0:.1f}% | lo TB {st.mean(ls)*100 if ls else 0:.1f}% | von x{eq[-1]:.2f}", flush=True)
    yr = {}
    for k in range(kS, kE): yr.setdefault(cal[k][:4], [k, k]); yr[cal[k][:4]][1] = k
    print("  tung nam:", " ".join(f"{y}:{(eq[b-kS]/eq[max(a-kS-1,0)]-1)*100:+.0f}%" for y, (a, b) in sorted(yr.items())), flush=True)
# đối chứng chỉ số cân bằng
print(f"Chi so can bang (200 ma): {((idx[kE]/idx[kS])**(250/(kE-kS))-1)*100:.1f}%/nam", flush=True)
print("\n===== 1000 LUOT: bat dau ngau nhien 2015-07 -> 2023-10, chay 3 nam, bo ngau nhien 10% tin hieu =====", flush=True)
rng = random.Random(11); starts = [k for k in range(N) if "2015-07" <= cal[k] <= "2023-10"]
KQ = {"V306TM": [], "C": []}
for r in range(1000):
    k0 = rng.choice(starts); k1 = min(k0 + 750, kE); seed = rng.random()
    for ten in KQ:
        cagr, dd, L, _ = chay(ten, k0, k1, 0.10, random.Random(seed))
        KQ[ten].append((cagr, dd, sum(1 for x in L if x > 0) / max(1, len(L)), len(L)))
    if r % 100 == 0: print("luot", r, flush=True)
def pct(a, q): a = sorted(a); return a[int(q * (len(a) - 1))]
for ten, R in KQ.items():
    c = [x[0] for x in R]; d = [x[1] for x in R]; w = [x[2] for x in R]
    print(f"{ten}: lai/nam trung vi {pct(c,.5)*100:.1f}% (5%-95%: {pct(c,.05)*100:.1f}% .. {pct(c,.95)*100:.1f}%) | lo 3 nam: {sum(1 for x in c if x<0)/10:.1f}% so luot"
          f" | sut giam trung vi {pct(d,.5)*100:.1f}% (te nhat 5%: {pct(d,.05)*100:.1f}%) | ty le thang trung vi {pct(w,.5)*100:.0f}% | so lenh TB {st.mean(x[3] for x in R):.0f}", flush=True)
hon = sum(1 for a, b in zip(KQ["V306TM"], KQ["C"]) if a[0] > b[0])
print(f"V306TM lai hon C o {hon}/1000 luot ({hon/10:.1f}%)", flush=True)
ra = sum(1 for a, b in zip(KQ["V306TM"], KQ["C"]) if a[0] / -min(a[1], -0.01) > b[0] / -min(b[1], -0.01))
print(f"V306TM lai/sut giam tot hon C o {ra}/1000 luot", flush=True)
