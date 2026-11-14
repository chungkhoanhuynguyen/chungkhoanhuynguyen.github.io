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
# ===== QL1 14/11: tim cach ngan han ty le thang cao, 1-3 lenh/tuan (kiem tra trung thuc, co phi thue, T+2,5) =====
PHI = 0.0015 + 0.0015 + 0.001
def rsi_n(c, p):
    out = [None] * len(c); ag = al = None
    for k in range(1, len(c)):
        g = max(c[k] - c[k-1], 0); l = max(c[k-1] - c[k], 0)
        if ag is None: ag, al = g, l
        else: ag = (ag * (p - 1) + g) / p; al = (al * (p - 1) + l) / p
        out[k] = 100 if al == 0 else 100 - 100 / (1 + ag / al)
    return out
for s, b in D.items():
    c = b["c"]; n = len(c)
    def ma(p):
        out = [None] * n; acc = 0
        for k in range(n):
            acc += c[k]
            if k >= p: acc -= c[k - p]
            if k >= p - 1: out[k] = acc / p
        return out
    b["ma10"] = ma(10); b["rsi3"] = rsi_n(c, 3)
    vv = b["v"]; b["v20"] = [None if k < 20 else sum(vv[k-20:k]) / 20 for k in range(n)]
# chi so can bang cua ro (TB % thay doi cac ma trong ro thang do) + MA50/MA200
ix = [1.0]; ixd = {}
for i, d in enumerate(cal):
    if i == 0: ixd[d] = 0; continue
    m = d[:7]; rs = []
    for s in ro.get(m, ()):
        b = D[s]; k = b["ix"].get(d)
        if k and k > 0 and b["c"][k-1] > 0:
            x = b["c"][k] / b["c"][k-1] - 1
            if abs(x) < 0.3: rs.append(x)
    ix.append(ix[-1] * (1 + (sum(rs) / len(rs) if rs else 0))); ixd[d] = i
def sma(a, p): return [None if k < p - 1 else sum(a[k-p+1:k+1]) / p for k in range(len(a))]
im50, im200, im20 = sma(ix, 50), sma(ix, 200), sma(ix, 20)
def mk(d, kind):
    i = ixd.get(d)
    if i is None or im200[i] is None: return False
    if kind == 0: return True
    if kind == 1: return ix[i] > im50[i]
    if kind == 2: return ix[i] > im200[i] and ix[i] > im50[i]
    if kind == 3: return ix[i] > im20[i] and im20[i] > im50[i]
    return True
def lenh(b, k, tp, sl, tmax, kieu_ra="tp"):
    n = len(b["c"])
    if k + 3 >= n: return None
    o = b["o"][k+1]
    if o >= b["c"][k] * 1.065 or o <= 0: return None
    T = o * (1 + tp); Sx = o * (1 - sl)
    for j in range(k + 3, n):
        if b["o"][j] <= Sx: return (b["d"][k+1], b["d"][j], b["o"][j] / o - 1 - PHI)
        if b["l"][j] <= Sx: return (b["d"][k+1], b["d"][j], -sl - PHI)          # cung phien cham ca 2: tinh la cat lo (than trong)
        if b["o"][j] >= T: return (b["d"][k+1], b["d"][j], b["o"][j] / o - 1 - PHI)
        if b["h"][j] >= T: return (b["d"][k+1], b["d"][j], tp - PHI)
        if kieu_ra == "ma5" and b["c"][j] > b["ma5"][j]: return (b["d"][k+1], b["d"][j], b["c"][j] / o - 1 - PHI)
        if j - (k + 1) >= tmax: return (b["d"][k+1], b["d"][j], b["c"][j] / o - 1 - PHI)
    return None
def xu_huong(b, k): return b["ma200"][k] and b["ma50"][k] and b["c"][k] > b["ma50"][k] > b["ma200"][k] and b["ma20"][k] > b["ma20"][k-5]
def t_chinh(b, k):      # chinh nhe trong xu huong tang manh
    return xu_huong(b, k) and b["rsi2"][k] is not None and b["rsi2"][k] < 15 and b["l"][k] > b["ma50"][k]
def t_chinh3(b, k):     # 3 phien giam lien tiep trong xu huong tang
    c = b["c"]; return xu_huong(b, k) and c[k] < c[k-1] < c[k-2] < c[k-3] and c[k] > b["ma50"][k]
def t_butpha(b, k):
    if not b["ma50"][k] or not b["v20"][k]: return False
    return b["c"][k] > max(b["h"][k-20:k]) and b["v"][k] > 1.5 * b["v20"][k] and b["c"][k] > b["ma50"][k]
def t_rutchan(b, k):    # ru xuong MA20 roi rut chan, dong cua gan dinh phien, KL lon
    if not xu_huong(b, k) or not b["v20"][k]: return False
    h, l, c, o = b["h"][k], b["l"][k], b["c"][k], b["o"][k]
    return h > l and l <= b["ma20"][k] * 1.005 and c > b["ma20"][k] and (c - l) / (h - l) > 0.7 and c > o and b["v"][k] > 1.2 * b["v20"][k]
def t_manh(b, k):       # suc manh tuong doi: tang 60 phien > 15%, chinh ve MA10
    c = b["c"]
    return xu_huong(b, k) and k > 60 and c[k] / c[k-60] > 1.15 and b["l"][k] <= b["ma10"][k] and c[k] > b["ma20"][k] and b["rsi3"][k] is not None and b["rsi3"][k] < 35
def chay2(ten, th, mkk, tp, sl, tmax, kieu="tp", cap=3, in_ct=False):
    L = []
    for s, b in D.items():
        k = 205; n = len(b["c"])
        while k < n - 3:
            d = b["d"][k]; m = d[:7]
            if m in ro and s in ro[m] and mk(d, mkk) and th(b, k):
                t = lenh(b, k, tp, sl, tmax, kieu)
                if t: L.append((s,) + t + (b["c"][k] / b["c"][k-60] - 1,)); k = b["ix"][t[1]] + 1; continue
            k += 1
    L.sort(key=lambda x: (x[1], -x[4]))
    # gioi han toi da `cap` lenh moi moi tuan (uu tien ma manh hon)
    wk = defaultdict(int); L2 = []
    for x in L:
        w = datetime.date.fromisoformat(x[1]).isocalendar()[:2]
        if wk[w] < cap: wk[w] += 1; L2.append(x)
    r = [x[3] for x in L2]
    if len(r) < 30: print(f"{ten}: chi {len(r)} lenh"); return None
    w = [x for x in r if x > 0]; ls = [x for x in r if x <= 0]
    tuan = len({datetime.date.fromisoformat(d).isocalendar()[:2] for d in cal if d >= "2015-11"})
    # chuoi thua dai nhat + sut giam (moi lenh 20% von)
    mx = cur = 0
    for x in sorted(L2, key=lambda x: x[2]):
        cur = cur + 1 if x[3] <= 0 else 0; mx = max(mx, cur)
    by = defaultdict(float)
    for x in L2: by[x[2]] += x[3] * 0.2
    v = pk = 1.0; dd = 0
    for d in sorted(by): v *= 1 + by[d]; pk = max(pk, v); dd = min(dd, v / pk - 1)
    pr = " | ".join(f"{a[2:]}-{z[2:]}: {len(q)}l {sum(1 for y in q if y>0)/len(q)*100:.0f}% kv{st.mean(q)*100:+.2f}" for a, z in (("2015","2019"),("2020","2022"),("2023","2026")) for q in [[x[3] for x in L2 if a <= x[1][:4] <= z]] if q)
    print(f"{ten:58s} lenh {len(r):4d} ({len(r)/tuan:.2f}/tuan, tuan co lenh {len(wk)/tuan*100:.0f}%) thang {len(w)/len(r)*100:5.1f}% laiTB {st.mean(w)*100:5.2f} loTB {st.mean(ls)*100 if ls else 0:6.2f} kyvong {st.mean(r)*100:+.2f}% PF {sum(w)/-sum(ls) if ls else 99:.2f} thua lien tiep {mx} von x{v:.2f} sut {dd*100:.0f}% || {pr}", flush=True)
    if in_ct:
        yr = defaultdict(list)
        for x in L2: yr[x[1][:4]].append(x[3])
        print("   theo nam: " + "; ".join(f"{y}: {len(q)}l {sum(1 for z in q if z>0)/len(q)*100:.0f}% {sum(q)*20:+.0f}%von" for y, q in sorted(yr.items())), flush=True)
    return L2
TH = {"chinh": t_chinh, "chinh3": t_chinh3, "butpha": t_butpha, "rutchan": t_rutchan, "manh": t_manh}
print("\n##### LUOI THAM SO (ro 30 ma thanh khoan nhat theo thoi diem; toi da 3 lenh/tuan) #####", flush=True)
for ten, th in TH.items():
    for mkk in (0, 1, 2, 3):
        for tp, sl, tm in ((0.03, 0.06, 8), (0.04, 0.06, 8), (0.04, 0.08, 10), (0.05, 0.05, 10), (0.05, 0.08, 12), (0.06, 0.06, 12), (0.07, 0.07, 15)):
            chay2(f"{ten} tt{mkk} chot{int(tp*100)} cat{int(sl*100)} giu{tm}", th, mkk, tp, sl, tm)
    for mkk in (1, 2):
        chay2(f"{ten} tt{mkk} ra MA5 cat8 giu10", th, mkk, 9.9, 0.08, 10, "ma5")
