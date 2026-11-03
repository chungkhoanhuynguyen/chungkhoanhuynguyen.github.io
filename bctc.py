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
MODEL = {"bank": (101, 102, 103), "ck": (89, 90, 91), "dn": (1, 2, 3)}  # thuyết minh: nguồn miễn phí chưa có
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
    d = get(f"financial_statements?q=code:{code}~reportType:{rt}~modelType:{m}&sort=fiscalDate:desc&size={n * (760 if m in (4, 92, 104) else 220)}")
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
def tom(o):
    """Tóm tắt quý gần nhất để so sánh cùng ngành."""
    q = o["q"]; bs, is_ = q.get("bs", []), q.get("is", [])
    def f(rows, *keys):
        for k in keys:
            for r in rows:
                if r[0].lower().startswith(k): return r[2]
        return None
    ta = f(bs, "tổng cộng tài sản", "tổng tài sản"); vc = f(bs, "vốn chủ sở hữu")
    ln = f(is_, "lợi nhuận sau thuế của công ty mẹ", "lợi nhuận sau thuế của cổ đông", "lợi nhuận sau thuế thu nhập doanh nghiệp")
    dt = f(is_, "tổng thu nhập hoạt động", "doanh thu thuần", "cộng doanh thu hoạt động", "doanh thu hoạt động")
    lg = f(is_, "lợi nhuận gộp")
    g = lambda a, i: a[i] if a and len(a) > i and a[i] is not None else None
    ln4 = sum(x for x in (ln or [])[:4] if x is not None) if ln and len(ln) >= 4 else None
    yoy = (g(ln, 0) / g(ln, 4) - 1) * 100 if g(ln, 0) is not None and g(ln, 4) and g(ln, 4) > 0 else None
    return {"d": q["d"][0], "f": o["f"], "ta": g(ta, 0), "vc": g(vc, 0), "dt": g(dt, 0), "ln": g(ln, 0), "ln4": ln4, "yoy": None if yoy is None else round(yoy, 1),
            "roe": None if not (ln4 and g(vc, 0)) else round(ln4 / g(vc, 0) * 100, 1), "bg": None if not (g(lg, 0) and g(dt, 0)) else round(g(lg, 0) / g(dt, 0) * 100, 1)}
if __name__ == "__main__":
    codes = sys.argv[1:] or sorted({x[:-4] for x in os.listdir(os.path.join(ROOT, "data/c")) if x.endswith(".bin") and x[:-4].isalnum() and len(x[:-4]) == 3})
    ok = 0; T = hncodec.load(os.path.join(ROOT, "data/bctc/_tom.bin"), {}) or {}
    for c in codes:
        try:
            o = mot(c)
            if o and o["q"].get("d"):
                hncodec.dump(o, os.path.join(ROOT, "data/bctc/%s.bin" % c)); ok += 1; T[c] = tom(o)
                print(c, o["f"], {k: len(o["q"].get(k, [])) for k in ("bs", "is", "cf")}, o["q"]["d"][0], flush=True)
        except Exception as e: print(c, "loi", e)
        time.sleep(0.2)
    hncodec.dump(T, os.path.join(ROOT, "data/bctc/_tom.bin"))
    print("xong", ok, "/", len(codes))
