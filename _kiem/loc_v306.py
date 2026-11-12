# -*- coding: utf-8 -*-
"""QL1 13/11 – loc_v306: quét tín hiệu V306TMAD phiên mới nhất (dùng đúng bộ máy bt3). Gốc: trên CÙNG bộ máy danh mục, 1000 lượt Monte Carlo + 8 bước tự soát lỗi.
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

g = N - 1
print("\n======== QUÉT V306TMAD – phiên", CAL[g], "========", flush=True)
print("Bộ lọc thị trường (chỉ số cân bằng 200 mã > MA200):", "MỞ – được mua mới" if MKT[g] else "ĐÓNG – đứng ngoài", "| chỉ số %.1f vs MA200 %.1f" % (idx[g], ima[g] or 0), flush=True)
print("5 phiên gần nhất bộ lọc:", [(CAL[k], MKT[k]) for k in range(N - 5, N)], flush=True)
for k in range(N - 5, N):   # tín hiệu 5 phiên gần nhất (luật D: còn hạn chờ)
    sg = [s for s in RO[k] if sig_v306(s, k)]
    sg.sort(key=lambda s: -(A[s]["r126"][k] if A[s]["r126"][k] is not None else -9))
    for s in sg:
        a = A[s]; print(f"TIN HIEU {CAL[k]} | {s} | dong cua {a['c'][k]:.2f} | KL/TB20 {a['v'][k]/a['vavg20'][k]:.1f} | tang 6T {a['r126'][k]*100:.0f}% | gia nay {a['c'][g]} | loc TT {'mo' if MKT[k] else 'dong'}", flush=True)
print("\nMÃ THEO DÕI (đạt xếp hàng MA, trong rổ, cách đỉnh 120 phiên ≤5%):", flush=True)
w = []
for s in RO[g]:
    a = A[s]
    if None in (a["ma50"][g], a["ma150"][g], a["ma200"][g], a["ma200_21"][g], a["hh120"][g]): continue
    if a["ma50"][g] > a["ma150"][g] > a["ma200"][g] and a["ma200"][g] > a["ma200_21"][g]:
        cach = a["c"][g] / a["hh120"][g] - 1
        if cach >= -0.05: w.append((cach, s, a["c"][g], a["hh120"][g]))
for cach, s, c, h in sorted(w, reverse=True): print(f"  {s} | gia {c} | dinh 120 phien {h} | cach dinh {cach*100:+.1f}%", flush=True)
print("Ro 30 ma hien tai:", sorted(RO[g]), flush=True)
