# Lấy giá đóng cửa hằng ngày (VNDirect dchart, dự phòng TCBS) → tính RS → data/rs.json
import json, time, datetime, urllib.request, os
U = sorted(set("ACB BCM BID BMP BSR BVH BWE CII CMG CTD CTG CTR CTS DBC DCM DGC DGW DHC DIG DPM DXG DXS EIB EVF FPT FRT FTS GAS GEX GMD GVR HAG HCM HDB HDC HDG HHV HPG HSG HT1 IMP KBC KDC KDH KOS LPB MBB MSB MSN MWG NAB NKG NLG NT2 NVL OCB PAN PC1 PDR PHR PLX PNJ POW PTB PVD PVT REE SAB SBT SCS SHB SIP SJS SSB SSI STB SZC TCB TCH TPB VCB VCG VCI VDS VGC VHC VHM VIB VIC VIX VJC VND VNM VPB VPI VRE VSC VTP HAH ANV DPG ELC MSR ACV VGI QNS OIL VEA FOX PVS SHS CEO IDC L14 TNG HUT VCS PVC DTD".split()))
UA = {"User-Agent": "Mozilla/5.0"}
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r: return json.load(r)
def bars(sym, days=400):
    to = int(time.time()); fr = to - days*86400
    try:
        j = get(f"https://dchart-api.vndirect.com.vn/dchart/history?resolution=D&symbol={sym}&from={fr}&to={to}")
        if j.get("c"): return j["t"], j["c"], j.get("v") or [0]*len(j["c"])
    except Exception as e: print(sym, "vnd", e)
    try:
        j = get(f"https://apipubaws.tcbs.com.vn/stock-insight/v2/stock/bars-long-term?ticker={sym}&type=stock&resolution=D&from={fr}&to={to}")
        d = j.get("data") or []
        if d: return [x["tradingDate"] for x in d], [x["close"]/1000 for x in d], [x.get("volume", 0) for x in d]
    except Exception as e: print(sym, "tcbs", e)
    return None
def roc(c, n): return c[-1]/c[-n-1]-1 if len(c) > n else None
rows = []
for s in U:
    b = bars(s)
    if not b or len(b[1]) < 130: continue
    t, c, v = b
    val20 = sum(c[i]*v[i] for i in range(-20, 0))/20*1000/1e9  # tỷ đồng/phiên (giá tính bằng nghìn đồng)
    r3, r6, r9, r12 = roc(c, 63), roc(c, 126), roc(c, 189), roc(c, 252)
    score = 0.4*r3 + 0.2*r6 + 0.2*(r9 if r9 is not None else r6) + 0.2*(r12 if r12 is not None else r6)
    hi = max(c[-252:])
    rows.append(dict(s=s, close=round(c[-1], 2), d1=round((c[-1]/c[-2]-1)*100, 2), r3=round(r3*100, 1), r6=round(r6*100, 1),
                     r12=round(r12*100, 1) if r12 is not None else None, fromhi=round((c[-1]/hi-1)*100, 1), val=round(val20, 1), score=score,
                     spark=[round(x, 2) for x in c[-60:]]))
    time.sleep(0.3)
rows.sort(key=lambda r: r["score"])
n = len(rows)
for i, r in enumerate(rows): r["rs"] = max(1, round(99*(i+1)/n))
liq = [r for r in rows if r["val"] >= 10]
top = sorted(liq, key=lambda r: -r["score"])[:10]
for r in top: r.pop("score")
os.makedirs("data", exist_ok=True)
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
json.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), universe=n, top=top), open("data/rs.json", "w"), ensure_ascii=False)
print("ok", n, [r["s"] for r in top])
