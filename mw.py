# Bảng thị trường trong phiên: độ rộng, nhóm dẫn dắt, bản đồ nhiệt, thanh khoản, tỷ lệ mã trên MA.
import json, time, datetime, urllib.request, os, base64
_h = lambda s: base64.b64decode(s).decode()
SRC = _h("aHR0cHM6Ly9zY2FubmVyLnRyYWRpbmd2aWV3LmNvbS92aWV0bmFtL3NjYW4=")
UA = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}
BANK = set("VCB BID CTG TCB MBB VPB ACB HDB STB SHB TPB VIB LPB MSB OCB EIB SSB NAB VAB KLB BVB ABB SGB PGB NVB BAB".split())
CK = set("SSI VND HCM VCI VIX SHS FTS CTS BSI MBS TCX VPX ORS AGR TVS DSE APG VDS BVS".split())
BDS = set("VIC VHM VRE NVL KDH NLG DXG PDR DIG KBC IDC SZC BCM NTL DXS CEO HDG KHG HDC SCR TCH CRE QCG HQC ITA SJS LHG IJC".split())
BH = set("BVH BMI PVI MIG PTI".split())
SEC = {"Finance": "Tài chính", "Non-Energy Minerals": "Khoáng sản, thép", "Energy Minerals": "Dầu khí", "Utilities": "Điện, nước",
       "Process Industries": "Hóa chất, phân bón", "Producer Manufacturing": "Sản xuất", "Consumer Non-Durables": "Tiêu dùng",
       "Retail Trade": "Bán lẻ", "Transportation": "Vận tải, cảng", "Technology Services": "Công nghệ", "Industrial Services": "Xây dựng, dịch vụ CN",
       "Commercial Services": "Dịch vụ", "Communications": "Viễn thông", "Health Technology": "Dược, y tế", "Consumer Durables": "Hàng lâu bền",
       "Distribution Services": "Phân phối", "Electronic Technology": "Điện tử", "Consumer Services": "Dịch vụ tiêu dùng", "Health Services": "Dịch vụ y tế"}
def nganh(s, sec):
    if s in BANK: return "Ngân hàng"
    if s in CK: return "Chứng khoán"
    if s in BDS: return "Bất động sản"
    if s in BH: return "Bảo hiểm"
    return SEC.get(sec or "", "Khác")

def scan():
    body = {"filter": [{"left": "exchange", "operation": "equal", "right": "HOSE"}, {"left": "type", "operation": "equal", "right": "stock"}],
            "columns": ["name", "close", "change", "market_cap_basic", "SMA50", "SMA200", "sector", "Value.Traded", "open", "high", "low", "volume"],
            "sort": {"sortBy": "market_cap_basic", "sortOrder": "desc"}, "range": [0, 600]}
    for k in range(3):
        try:
            req = urllib.request.Request(SRC, data=json.dumps(body).encode(), headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r: return json.load(r)["data"]
        except Exception as e:
            err = e; time.sleep(3)
    raise SystemExit("scan lỗi %s" % err)

rows = []; LIVE = {}
for x in scan():
    s, c, ch, mc, m50, m200, sec, val, o, hi, lo, vol = x["d"]
    if c: LIVE[s] = [o or c, hi or c, lo or c, c, vol or 0, 1000]
    if not c or mc is None or ch is None: continue
    rows.append(dict(s=s, c=c, ch=ch, mc=mc, m50=m50, m200=m200, n=nganh(s, sec), v=val or 0))
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
today = now.strftime("%Y-%m-%d"); hm = now.strftime("%H:%M")
adv = sum(1 for r in rows if r["ch"] > 0.0001); dec = sum(1 for r in rows if r["ch"] < -0.0001); unc = len(rows) - adv - dec
# đóng góp điểm (ước tính theo vốn hóa, không tính free-float)
os.makedirs("data", exist_ok=True)
old = {}
try: old = json.load(open("data/mw.json"))
except Exception: pass
vn = old.get("vn_prev")
try:
    IX = {"HOSE:VNINDEX": "VNINDEX", "HOSE:VN30": "VN30", "HOSE:VN100": "VN100", "HNX:HNXINDEX": "HNX"}
    req = urllib.request.Request(SRC, data=json.dumps({"symbols": {"tickers": list(IX)}, "columns": ["close", "change", "open", "high", "low", "volume"]}).encode(), headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r: dd = {x["s"]: x["d"] for x in json.load(r)["data"]}
    for k, d in dd.items():
        if d[0]: LIVE[IX[k]] = [d[2] or d[0], d[3] or d[0], d[4] or d[0], d[0], d[5] or 0, 1]
    d = dd["HOSE:VNINDEX"]
    vn_close, vn_ch = d[0], d[1]; vn = vn_close / (1 + vn_ch/100)
except Exception: vn_close = vn_ch = None
prev_tot = sum(r["mc"]/(1 + r["ch"]/100) for r in rows)
for r in rows: r["pt"] = (vn or 1700) * (r["mc"]/(1 + r["ch"]/100)) / prev_tot * (r["ch"]/100)
lead = sorted(rows, key=lambda r: -r["pt"])
up = [[r["s"], round(r["pt"], 2)] for r in lead[:10] if r["pt"] > 0]
dn = [[r["s"], round(r["pt"], 2)] for r in lead[::-1][:10] if r["pt"] < 0]
heat = [[r["s"], round(r["mc"]/1e9), round(r["ch"], 2), r["n"]] for r in rows[:60]]
topv = [[r["s"], round(r["v"]/1e9, 1), round(r["ch"], 2)] for r in sorted(rows, key=lambda r: -r["v"])[:10]]
w50 = [r for r in rows if r["m50"]]; w200 = [r for r in rows if r["m200"]]
a50 = round(100*sum(1 for r in w50 if r["c"] > r["m50"])/max(1, len(w50)), 1)
a200 = round(100*sum(1 for r in w200 if r["c"] > r["m200"])/max(1, len(w200)), 1)
intr = old.get("intraday", []) if old.get("date") == today else []
in_session = now.weekday() < 5 and ("09:00" <= hm <= "15:05")
if in_session and (not intr or intr[-1][0] != hm): intr.append([hm, adv, unc, dec])
nganh_ch = {}
for r in rows[:150]:
    g = nganh_ch.setdefault(r["n"], [0, 0]); g[0] += r["mc"]*r["ch"]; g[1] += r["mc"]
sec = sorted([[k, round(v[0]/v[1], 2)] for k, v in nganh_ch.items() if v[1] > 0], key=lambda x: -x[1])
json.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), date=today, n=len(rows), breadth=[adv, unc, dec], intraday=intr,
               up=up, dn=dn, heat=heat, topv=topv, a50=a50, a200=a200, sec=sec,
               vn=[round(vn_close, 2) if vn_close else None, round(vn_ch, 2) if vn_ch is not None else None], vn_prev=vn),
          open("data/mw.json", "w"), ensure_ascii=False)
# nến trong phiên cho mục Soi chart (giá x100, khối lượng /100), bỏ qua ngày nghỉ
def last_bar(sym):
    try:
        r = json.load(open("data/c/recent.json")).get("b", {}).get(sym)
        if r: return r[-1]
        j = json.load(open("data/c/%s.json" % sym)); return [None, j["o"][-1], j["h"][-1], j["l"][-1], j["c"][-1]]
    except Exception: return None
lb = last_bar("VNINDEX"); P = lambda x, k: int(round(x / k * 100))
lv = {s: [P(b[0], b[5]), P(b[1], b[5]), P(b[2], b[5]), P(b[3], b[5]), int(round(b[4] / 100))] for s, b in LIVE.items()}
stale = bool(lb and "VNINDEX" in lv and all(abs(a - b) <= 1 for a, b in zip(lv["VNINDEX"][1:4], lb[2:5])))  # cao, thấp, đóng cửa trùng phiên trước = ngày nghỉ
write = now.weekday() < 5 and hm >= "09:00" and bool(lv) and not stale
if write:
    os.makedirs("data/c", exist_ok=True)
    json.dump({"d": today, "t": hm, "b": lv}, open("data/c/live.json", "w"), separators=(",", ":"))
print("ok", len(rows), adv, unc, dec, len(intr), "ghi nến" if write else ("ngày nghỉ, không ghi nến" if stale else "ngoài giờ, không ghi nến"))
