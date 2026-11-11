# -*- coding: utf-8 -*-
"""QL1 11/11 – Kiểm thử 4 phương pháp ngắn hạn trên rổ "VN30 tại thời điểm" (không lấy cổ phiếu hiện tại đi trade quá khứ).
Rổ: đầu mỗi tháng chọn 30 mã HOSE thanh khoản lớn nhất 60 phiên trước đó, trong số các mã ĐANG giao dịch lúc đó
(gồm cả mã đã huỷ niêm yết / chuyển sàn sau này). Dữ liệu giá điều chỉnh. Phí mua 0,15%, bán 0,15% + thuế 0,1%.
Tín hiệu theo giá đóng cửa ngày t, mua giá mở cửa t+1 (bỏ lệnh nếu mở cửa sát giá trần), sớm nhất bán phiên t+3 (T+2,5).
"""
import json, time, datetime, urllib.request, base64, sys, math, statistics as st
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
    print("loi", url[:80], err, flush=True); return None
T0 = int(datetime.datetime(2014, 6, 1).timestamp()); T1 = int(time.time())
def bars(sym):
    j = get(f"{S2}?resolution=D&symbol={sym}&from={T0}&to={T1}")
    if not j or not j.get("c") or len(j["c"]) < 150: return None
    d = [datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d") for t in j["t"]]
    return dict(d=d, o=j["o"], h=j["h"], l=j["l"], c=j["c"], v=j["v"])

# 1) danh sách mã HOSE: đang niêm yết + đã huỷ niêm yết (tránh thiên lệch sống sót)
syms = set()
for q in ("status:LISTED", "status:DELISTED", ""):
    j = get(f"{S3}stocks?q=type:STOCK~floor:HOSE" + ("~" + q if q else "") + "&fields=code,status,floor&size=3000") or {"data": []}
    n0 = len(syms); syms |= {x["code"] for x in j["data"] if x.get("code") and len(x["code"]) == 3}
    print("ds", q or "tat ca", len(j["data"]), "->", len(syms) - n0, "ma moi", flush=True)
# các mã lớn từng ở HOSE/VN30 đã huỷ niêm yết hoặc rời sàn (bổ sung phòng API thiếu)
syms |= set("FLC ROS HAI ITA HQC AMD TTF OGC KBC DLG HNG HAG JVC VHG PPI TSC FIT KLF ART TTB GTN SBT CII HSG NKG DXG PDR NVL DIG CEO HVN VJC GAB BCG APC SVC TDH QCG LCM HAX".split())
print("tong ma", len(syms), flush=True)
D = {}
for i, s in enumerate(sorted(syms)):
    b = bars(s)
    if b: D[s] = b
    if i % 50 == 0: print(i, s, len(D), flush=True)
print("co du lieu", len(D), flush=True)
# 2) lịch phiên chung + chỉ số
cal = sorted({d for b in D.values() for d in b["d"]})
for s, b in D.items():
    b["ix"] = {d: k for k, d in enumerate(b["d"])}
    c = b["c"]; n = len(c)
    def ma(p):
        out = [None] * n; acc = 0
        for k in range(n):
            acc += c[k]
            if k >= p: acc -= c[k - p]
            if k >= p - 1: out[k] = acc / p
        return out
    b["ma5"], b["ma20"], b["ma50"], b["ma200"] = ma(5), ma(20), ma(50), ma(200)
    rsi = [None] * n; ag = al = None
    for k in range(1, n):   # RSI 2 phiên (Wilder)
        g = max(c[k] - c[k-1], 0); l = max(c[k-1] - c[k], 0)
        if ag is None: ag, al = g, l
        else: ag = (ag + g) / 2; al = (al + l) / 2
        rsi[k] = 100 if al == 0 else 100 - 100 / (1 + ag / al)
    b["rsi2"] = rsi
    b["gt"] = [c[k] * b["v"][k] for k in range(n)]
# 3) rổ VN30 theo thời điểm: tháng m dùng thanh khoản 60 phiên trước phiên đầu tháng
months = sorted({d[:7] for d in cal if d >= "2015-01"})
ro = {}
for m in months:
    d0 = next(d for d in cal if d[:7] == m)
    sc = []
    for s, b in D.items():
        k = b["ix"].get(d0)
        if k is None or k < 200: continue     # phải đang giao dịch ngày đầu tháng và có ≥200 phiên lịch sử
        sc.append((sum(b["gt"][k-60:k]) / 60, s))
    ro[m] = {s for _, s in sorted(sc, reverse=True)[:30]}
print("ro mau", months[0], sorted(ro[months[0]]), flush=True)
print("ro mau", months[-1], sorted(ro[months[-1]]), flush=True)
PHI = 0.0015 + 0.0015 + 0.001
def mo_lenh(b, k, ra):
    """tín hiệu ngày k -> mua mở cửa k+1; ra(b, kv, j) trả True để bán ở giá đóng cửa phiên j (j ≥ k+3)."""
    n = len(b["c"])
    if k + 3 >= n: return None
    o = b["o"][k+1]
    if o >= b["c"][k] * 1.065: return None    # mở cửa sát trần – thực tế khó khớp
    for j in range(k + 3, n):
        r = ra(b, k + 1, j, o)
        if r: return (b["d"][k+1], b["d"][j], (b["c"][j] if r is True else r) / o - 1 - PHI)
    return None
def chay(ten, tin_hieu, ra, gioi_han=None):
    L = []
    for s, b in D.items():
        k = 200; n = len(b["c"])
        while k < n - 3:
            m = b["d"][k][:7]
            if m in ro and s in ro[m] and tin_hieu(b, k):
                t = mo_lenh(b, k, ra)
                if t: L.append((s,) + t); k = b["ix"][t[1]] + 1; continue
            k += 1
    bao_cao(ten, L)
    return L
def mdd_von(L, ty_trong=0.1):
    """vốn: mỗi lệnh 10% tài sản, cộng lãi/lỗ theo ngày bán, tính mức sụt giảm lớn nhất."""
    by = defaultdict(float)
    for s, a, e, r in L: by[e] += r * ty_trong
    v = 1.0; pk = 1.0; dd = 0.0; dau = None
    for d in sorted(by):
        v *= (1 + by[d]); pk = max(pk, v); dd = min(dd, v / pk - 1)
    return v, dd
def bao_cao(ten, L):
    if not L: print(ten, "khong co lenh"); return
    r = [x[3] for x in L]; w = [x for x in r if x > 0]; ls = [x for x in r if x <= 0]
    v, dd = mdd_von(L)
    nam = (datetime.date.fromisoformat(L[-1][2]) - datetime.date(2015, 1, 1)).days / 365.25 if L else 1
    print(f"\n=== {ten} ===\nso lenh {len(r)} | thang {len(w)/len(r)*100:.1f}% | lai TB {st.mean(w)*100 if w else 0:.2f}% | lo TB {st.mean(ls)*100 if ls else 0:.2f}%"
          f" | ky vong/lenh {st.mean(r)*100:.2f}% | PF {sum(w)/-sum(ls) if ls else 99:.2f} | lo lon nhat {min(r)*100:.1f}% | von x{v:.2f} (moi lenh 10%) | sut giam max {dd*100:.1f}%", flush=True)
    for a, z in (("2015", "2019"), ("2020", "2022"), ("2023", "2026")):
        q = [x[3] for x in L if a <= x[1][:4] <= z]
        if q: print(f"  {a}-{z}: {len(q)} lenh, thang {sum(1 for x in q if x>0)/len(q)*100:.1f}%, ky vong {st.mean(q)*100:.2f}%", flush=True)
    print("  ma xuat hien nhieu:", sorted(defaultdict(int, {}).items()) or "", end="")
    cnt = defaultdict(int)
    for x in L: cnt[x[0]] += 1
    print(", ".join(f"{s}:{n}" for s, n in sorted(cnt.items(), key=lambda t: -t[1])[:12]), flush=True)
    xs = sorted(L, key=lambda x: x[3])
    print("  5 lenh lo nhat:", "; ".join(f"{s} {a}->{e} {r*100:.1f}%" for s, a, e, r in xs[:5]), flush=True)

# A) Quá bán ngắn hạn trong xu hướng tăng (Connors RSI-2)
def tA(b, k): return b["ma200"][k] and b["c"][k] > b["ma200"][k] and b["rsi2"][k] is not None and b["rsi2"][k] < 10
def rA(b, kv, j, o): return b["c"][j] > b["ma5"][j] or j - kv >= 10
chay("A. Qua ban RSI2<10 tren MA200, ban khi dong cua > MA5 (toi da 10 phien)", tA, rA)
def rA2(b, kv, j, o):   # biến thể có cắt lỗ 8%
    if b["l"][j] <= o * 0.92: return o * 0.92
    return b["c"][j] > b["ma5"][j] or j - kv >= 10
chay("A2. Nhu A + cat lo 8%", tA, rA2)
# B) Nhịp chỉnh về MA20 của cổ phiếu xu hướng tăng
def tB(b, k):
    m20, m50, m200 = b["ma20"][k], b["ma50"][k], b["ma200"][k]
    if not (m20 and m50 and m200) or k < 25: return False
    tren = all(b["c"][k-i] > b["ma20"][k-i] * 1.03 for i in range(3, 8))
    return m50 > m200 and m20 > m50 and tren and b["l"][k] <= m20 * 1.01 and b["c"][k] > m20
def rB(b, kv, j, o):
    if b["l"][j] <= o * 0.95: return o * 0.95
    if b["h"][j] >= o * 1.08: return o * 1.08
    return j - kv >= 20
chay("B. Chinh ve MA20 trong xu huong tang, chot +8% / cat -5% / toi da 20 phien", tB, rB)
# C) Bứt phá đỉnh 20 phiên kèm khối lượng (đối chứng kiểu đầu cơ động lượng)
def tC(b, k):
    if k < 60 or not b["ma50"][k]: return False
    return b["c"][k] > max(b["h"][k-20:k]) and b["v"][k] > 1.5 * st.mean(b["v"][k-20:k]) and b["c"][k] > b["ma50"][k]
def rC(b, kv, j, o):
    if b["l"][j] <= o * 0.93: return o * 0.93
    return b["c"][j] < b["ma20"][j] or j - kv >= 40
chay("C. But pha dinh 20 phien + KL >1,5 lan, ban khi thung MA20 / cat -7%", tC, rC)
# D) Mùa vụ cuối tháng – đầu tháng trên ETF VN30 (E1VFVN30)
e = D.get("E1VFVN30") or bars("E1VFVN30")
if e:
    L = []; d = e["d"]
    for k in range(4, len(d) - 4):
        if d[k][:7] != d[k+4][:7] and d[k+3][:7] == d[k][:7]:   # k = phiên thứ 4 từ cuối tháng
            j = k + 6                                            # bán phiên thứ 3 tháng sau
            if j < len(d): L.append(("E1VFVN30", d[k], d[j], e["c"][j] / e["c"][k] - 1 - PHI))
    bao_cao("D. Mua ETF VN30 4 phien cuoi thang, ban phien thu 3 thang sau", L)
# Đối chứng: mua – giữ ETF VN30
if e:
    k0 = next(k for k, x in enumerate(e["d"]) if x >= "2015-01")
    print(f"\nDoi chung: mua giu E1VFVN30 tu {e['d'][k0]} den {e['d'][-1]}: {(e['c'][-1]/e['c'][k0]-1)*100:.0f}%", flush=True)
