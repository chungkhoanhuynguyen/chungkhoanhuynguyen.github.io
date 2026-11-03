# Báo cáo tài chính đầy đủ cho trang mã cổ phiếu (/ma/MÃ.html): Cân đối kế toán, Kết quả kinh doanh, Lưu chuyển tiền tệ
# 8 quý + 5 năm gần nhất, đơn vị tỷ đồng -> data/bctc/MÃ.bin (đọc bằng /bctc.js). Chạy tuần/lần trên GitHub (miễn phí).
import json, time, urllib.request, os, base64, sys
import hncodec
ROOT = os.path.dirname(os.path.abspath(__file__))
W = """TCB VPB MBB ACB CTG BID VCB HDB STB SHB TPB MSB VIB LPB NAB OCB EIB SSB VAB KLB
SSI VND HCM VCI VIX SHS FTS CTS TCX
HPG HSG NKG FPT CMG MWG FRT DGW PNJ VNM MSN MSR SAB QNS VIC VHM VRE KDH NLG DXG KBC IDC SZC
GAS BSR PLX PVS PVD PVT PVP POW NT2 REE GMD HAH VSC VJC HVN DGC DCM DPM DHC BMP DHG VEA BVH TNG CTR""".split()  # giống kqkd.py
API = base64.b64decode("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==").decode(); UA = {"User-Agent": "Mozilla/5.0"}
MODEL = {"bank": (101, 102, 103), "ck": (89, 90, 91), "dn": (1, 2, 3)}
def get(path):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(API + path, headers=UA), timeout=30) as r: return json.load(r).get("data") or []
        except Exception as e: err = e; time.sleep(2)
    print("loi", path[:90], err); return []
FM = {}
for x in get("financial_models?size=10000"):
    FM.setdefault(int(x["modelType"]), []).append((x.get("displayOrder") or 0, int(x["itemCode"]), x["itemVnName"].strip(), int(x.get("displayLevel") or 1)))
def bang(code, m, rt, n):
    d = get(f"financial_statements?q=code:{code}~reportType:{rt}~modelType:{m}&sort=fiscalDate:desc&size={n * 220}")
    ds = sorted({x["fiscalDate"] for x in d}, reverse=True)[:n]
    v = {}
    for x in d:
        if x["fiscalDate"] in ds: v.setdefault(int(x["itemCode"]), {})[x["fiscalDate"]] = x["numericValue"]
    return ds, v
def form_of(code):
    for f, (bs, is_, cf) in MODEL.items():
        if get(f"financial_statements?q=code:{code}~reportType:QUARTER~modelType:{is_}&size=1"): return f
    return None
def mot(code):
    f = form_of(code)
    if not f: return None
    out = {"f": f, "m": {}, "q": {}, "y": {}}
    for key, m in zip(("bs", "is", "cf"), MODEL[f]):
        items = sorted(FM.get(m, []))
        for rt, n, tgt in (("QUARTER", 8, "q"), ("ANNUAL", 5, "y")):
            ds, v = bang(code, m, rt, n)
            if not ds: continue
            out[tgt].setdefault("d", ds)
            rows = []
            for o, ic, name, lv in items:
                if ic not in v: continue
                vals = [None if v[ic].get(d) is None else round(v[ic][d] / 1e9, 1) for d in out[tgt]["d"]]
                if all(x in (None, 0) for x in vals): continue
                rows.append([name, lv, vals])
            out[tgt][key] = rows
    return out
if __name__ == "__main__":
    codes = sys.argv[1:] or W; ok = 0
    for c in codes:
        try:
            o = mot(c)
            if o and o["q"]:
                hncodec.dump(o, os.path.join(ROOT, "data/bctc/%s.bin" % c)); ok += 1
                print(c, o["f"], len(o["q"].get("bs", [])), len(o["q"].get("is", [])), len(o["q"].get("cf", [])), o["q"]["d"][:2], flush=True)
        except Exception as e: print(c, "loi", e)
        time.sleep(0.3)
    print("xong", ok, "/", len(codes))
