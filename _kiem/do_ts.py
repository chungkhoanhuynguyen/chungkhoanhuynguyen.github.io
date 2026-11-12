# -*- coding: utf-8 -*-
"""QL1 13/11 – dò nguồn dữ liệu cơ bản ngân hàng (miễn phí) cho kiểm định tích sản."""
import json, time, urllib.request, base64
_h = lambda s: base64.b64decode(s).decode()
S3 = _h("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==")
UA = {"User-Agent": "Mozilla/5.0"}
def get(url):
    for k in range(2):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r: return json.load(r)
        except Exception as e: err = repr(e); time.sleep(1)
    print("LOI", url[-90:], err, flush=True); return None
for d in ("2024-12-31", "2019-12-31", "2014-12-31", "2011-12-30"):
    j = get(f"{S3}ratios?q=code:VCB~reportDate:{d}&size=1000") or {}
    L = j.get("data", [])
    print("NGAY", d, len(L), flush=True)
    for x in L: print("  ", x.get("ratioCode"), x.get("itemName"), x.get("value"), x.get("reportDate"), x.get("group"))
    if L: print("  KEYS", list(L[0].keys()))
for rc in ("PRICE_TO_BOOK", "BVPS_CR", "PRICE_TO_EARNINGS", "ROAE_TR_AVG5Q", "ROAA_TR_AVG5Q", "NIM_TR_AVG5Q", "NPL_RATIO", "MARKETCAP", "OUTSTANDING_SHARES", "EPS_TR"):
    j = get(f"{S3}ratios?q=code:VCB~ratioCode:{rc}&sort=reportDate:asc&size=5000&fields=reportDate,value") or {}
    L = j.get("data", [])
    print("MA", rc, len(L), L[:2], L[-2:], flush=True)
j = get(_h("aHR0cHM6Ly9hcGlwdWJhd3MudGNicy5jb20udm4vdGNhbmFseXNpcy92MS9maW5hbmNlL1ZDQi9maW5hbmNpYWxyYXRpbz95ZWFybHk9MCZpc0FsbD10cnVl"))
if j:
    print("TCBS", len(j), list(j[0].keys()) if isinstance(j, list) and j else str(j)[:300])
    if isinstance(j, list) and j: print(j[0]); print(j[-1])
