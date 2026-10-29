# Lịch sử 1 năm: VN-Index, P/E, P/B thị trường, tỷ lệ mã trên MA50/MA200 (chạy 1 lần/ngày sau phiên).
import json, time, datetime, urllib.request, os, base64
import hncodec
_h = lambda s: base64.b64decode(s).decode()
S1 = _h("aHR0cHM6Ly9zY2FubmVyLnRyYWRpbmd2aWV3LmNvbS92aWV0bmFtL3NjYW4=")
S2 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
S3 = _h("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==")
UA = {"User-Agent": "Mozilla/5.0"}
def get(url, data=None):
    for k in range(3):
        try:
            h = dict(UA);
            if data: h["Content-Type"] = "application/json"
            req = urllib.request.Request(url, data=json.dumps(data).encode() if data else None, headers=h)
            with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)
        except Exception as e:
            err = e; time.sleep(2)
    print("lỗi", err); return None
def bars(sym, days):
    to = int(time.time()); j = get(f"{S2}?resolution=D&symbol={sym}&from={to-days*86400}&to={to}")
    if not j or not j.get("c"): return {}
    return {datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"): c for t, c in zip(j["t"], j["c"])}
vn = bars("VNINDEX", 400)
dates = sorted(vn)[-250:]
def ratio(rc):
    j = get(f"{S3}ratios?q=code:VNINDEX~ratioCode:{rc}&sort=reportDate:desc&size=400") or {}
    return {x["reportDate"]: x["value"] for x in j.get("data", [])}
pe, pb = ratio("PRICE_TO_EARNINGS"), ratio("PRICE_TO_BOOK")
def ff(dct, ds):
    out, last = [], None
    for d in ds:
        if d in dct: last = dct[d]
        out.append(round(last, 2) if last else None)
    return out
j = get(S1, {"filter": [{"left": "exchange", "operation": "equal", "right": "HOSE"}, {"left": "type", "operation": "equal", "right": "stock"},
                        {"left": "market_cap_basic", "operation": "greater", "right": 3e11}],
             "columns": ["name"], "range": [0, 600]}) or {"data": []}
U = [x["d"][0] for x in j["data"]]
c50 = [0]*len(dates); c200 = [0]*len(dates); n50 = [0]*len(dates); n200 = [0]*len(dates)
for s in U:
    b = bars(s, 680); ks = sorted(b); px = [b[k] for k in ks]; idx = {k: i for i, k in enumerate(ks)}
    for di, d in enumerate(dates):
        i = idx.get(d)
        if i is None: continue
        if i >= 49:
            m = sum(px[i-49:i+1])/50; n50[di] += 1; c50[di] += px[i] > m
        if i >= 199:
            m = sum(px[i-199:i+1])/200; n200[di] += 1; c200[di] += px[i] > m
    time.sleep(0.15)
a50 = [round(100*c/n, 1) if n else None for c, n in zip(c50, n50)]
a200 = [round(100*c/n, 1) if n else None for c, n in zip(c200, n200)]
def flow(a50, a200):
    ms, sg, e = [], [], None
    for x, y in zip(a50, a200):
        if x is None: ms.append(None); sg.append(0); continue
        e = x if e is None else e + (x - e) * 0.5
        ms.append(round(e, 1))
        sg.append(1 if (x <= 25 and y is not None and x < y) else (-1 if x >= 75 else (-2 if x >= 55 else 0)))
    return ms, sg
ms, sg = flow(a50, a200)
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
os.makedirs("data", exist_ok=True)
hncodec.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), n=len(U), dates=dates, vn=[round(vn[d], 2) for d in dates], pe=ff(pe, dates), pb=ff(pb, dates), a50=a50, a200=a200, ms=ms, sg=sg),
             "data/mwh.bin"); hncodec.drop("data/mwh.json")
print("ok", len(U), len(dates), a50[-1], a200[-1])
