# Tự động đọc BCTC quý và viết đánh giá KQKD ngắn.
# Chỉ đánh giá chất lượng kết quả kinh doanh, không đưa giá mua/bán.
import json, time, datetime, urllib.request, os
import hncodec

W = """TCB VPB MBB ACB CTG BID VCB HDB STB SHB TPB MSB VIB LPB NAB OCB EIB SSB VAB KLB
SSI VND HCM VCI VIX SHS FTS CTS TCX
HPG HSG NKG FPT CMG MWG FRT DGW PNJ VNM MSN MSR SAB QNS VIC VHM VRE KDH NLG DXG KBC IDC SZC
GAS BSR PLX PVS PVD PVT PVP POW NT2 REE GMD HAH VSC VJC HVN DGC DCM DPM DHC BMP DHG VEA BVH TNG CTR""".split()
UA = {"User-Agent": "Mozilla/5.0"}
import base64
API = base64.b64decode("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==").decode()

def get(path):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(API + path, headers=UA), timeout=25) as r:
                return json.load(r).get("data") or []
        except Exception as e:
            err = e; time.sleep(2)
    print("loi", path[:80], err); return []

def stmt(code):
    for m, form in ((102, "bank"), (90, "ck"), (2, "dn")):
        d = get(f"financial_statements?q=code:{code}~reportType:QUARTER~modelType:{m}&sort=fiscalDate:desc&size=900")
        if d:
            q = {}
            for x in d: q.setdefault(x["fiscalDate"], {})[int(x["itemCode"])] = x["numericValue"] or 0.0
            return form, q
    return None, {}

def ratio(code, item, n=2):
    d = get(f"ratios?q=code:{code}~itemCode:{item}&sort=reportDate:desc&size={n}")
    return [(x["reportDate"], x["value"]) for x in d]

def ty(v): return v / 1e9
def fmt_ty(v):
    v = ty(v); s = f"{abs(v):,.0f}".replace(",", ".")
    return ("−" if v < 0 else "") + s + " tỷ"
def pct(a, b):
    if b is None or a is None or b == 0: return None
    if b < 0 and a >= 0: return 999.0
    if b < 0: return None
    if a < 0: return -999.0
    return (a / b - 1) * 100
def fp(p):
    if p is None: return "–"
    if p >= 999: return "chuyển từ lỗ sang lãi"
    if p <= -999: return "chuyển từ lãi sang lỗ"
    return ("+" if p >= 0 else "−") + f"{abs(p):.1f}".replace(".", ",") + "%"

def prev_year(d): return str(int(d[:4]) - 1) + d[4:]

def analyse(code):
    form, q = stmt(code)
    if not q: return None
    ds = sorted(q)
    d0 = ds[-1]; dy = prev_year(d0); dq = ds[-2] if len(ds) > 1 else None
    c, y = q[d0], q.get(dy)
    if y is None: return None
    LN = 23000
    ln, lny = c.get(LN, 0), y.get(LN, 0)
    if ln == 0 and c.get(23003): LN = 23003; ln, lny = c.get(23003, 0), y.get(23003, 0)
    ytd = [d for d in ds if d[:4] == d0[:4]]; ytdy = [prev_year(d) for d in ytd]
    acc = sum(q[d].get(LN, 0) for d in ytd); accy = sum(q.get(d, {}).get(LN, 0) for d in ytdy)
    g, b, info = [], [], []
    p_ln, p_acc = pct(ln, lny), pct(acc, accy)
    qn = (int(d0[5:7]) - 1) // 3 + 1; tag = f"Q{qn}/{d0[:4]}"
    info.append(f"LNST công ty mẹ {tag}: {fmt_ty(ln)} ({fp(p_ln)} so với cùng kỳ)")
    if len(ytd) > 1: info.append(f"Lũy kế {len(ytd)*3} tháng: {fmt_ty(acc)} ({fp(p_acc)})")
    if ln < 0: b.append(f"Quý {qn} lỗ {fmt_ty(-ln)}")
    elif p_ln is not None and p_ln >= 999: g.append("Lợi nhuận quý chuyển từ lỗ sang lãi so với cùng kỳ")
    elif p_ln is not None and p_ln >= 15: g.append(f"Lợi nhuận quý tăng {fp(p_ln)} so với cùng kỳ")
    elif p_ln is not None and p_ln <= -15: b.append(f"Lợi nhuận quý giảm {fp(p_ln)} so với cùng kỳ")
    if dq and q[dq].get(LN, 0) > 0 and ln > 0:
        pq = pct(ln, q[dq][LN])
        if pq is not None and -999 < pq <= -25: b.append(f"So với quý trước, lợi nhuận giảm {fp(pq)}")
        if pq is not None and pq >= 30 and pq < 999: g.append(f"So với quý trước, lợi nhuận tăng {fp(pq)}")
    if form == "bank":
        nii, niiy = c.get(421900, 0), y.get(421900, 0)
        fee, feey = c.get(423200, 0), y.get(423200, 0)
        pr, pry = abs(c.get(422900, 0)), abs(y.get(422900, 0))
        p1 = pct(nii, niiy)
        if p1 is not None:
            info.append(f"Thu nhập lãi thuần: {fmt_ty(nii)} ({fp(p1)})")
            if p1 >= 10: g.append(f"Thu nhập lãi thuần (mảng cho vay cốt lõi) tăng {fp(p1)}")
            elif p1 <= -3: b.append(f"Thu nhập lãi thuần (mảng cho vay cốt lõi) giảm {fp(p1)}")
        p2 = pct(fee, feey)
        if p2 is not None and fee > 0:
            if p2 >= 25: g.append(f"Lãi dịch vụ {fp(p2)}, đạt {fmt_ty(fee)}")
            elif p2 <= -20: b.append(f"Lãi dịch vụ giảm {fp(p2)}")
        p3 = pct(pr, pry)
        if p3 is not None and pry > 0:
            if p3 <= -20 and (p_ln or 0) > 0: b.append(f"Chi phí dự phòng giảm {fp(p3)}: một phần lợi nhuận tăng nhờ trích lập ít hơn")
            elif p3 >= 40: b.append(f"Chi phí dự phòng tăng {fp(p3)}, ngân hàng đang phải trích lập nhiều hơn")
        npl = ratio(code, 57016); cov = ratio(code, 57017, 1); nim = ratio(code, 57050, 1)
        if npl and npl[0][0] == d0:
            v = npl[0][1] * 100; s = f"Tỷ lệ nợ xấu {v:.2f}%".replace(".", ",")
            if len(npl) > 1:
                dv = v - npl[1][1] * 100
                if dv >= 0.15: b.append(s + f", tăng so với quý trước ({npl[1][1]*100:.2f}%)".replace(".", ","))
                elif dv <= -0.15: g.append(s + f", giảm so với quý trước ({npl[1][1]*100:.2f}%)".replace(".", ","))
                else: info.append(s)
            else: info.append(s)
        if cov and cov[0][0] == d0:
            v = cov[0][1] * 100
            if v < 70: b.append(f"Bao phủ nợ xấu chỉ khoảng {v:.0f}%, bộ đệm dự phòng mỏng")
            elif v >= 150: g.append(f"Bao phủ nợ xấu khoảng {v:.0f}%, bộ đệm dự phòng dày")
            else: info.append(f"Bao phủ nợ xấu khoảng {v:.0f}%")
        if nim and nim[0][0] == d0: info.append(f"NIM khoảng {nim[0][1]*100:.2f}%".replace(".", ","))
    elif form == "ck":
        br, bry = c.get(621110, 0), y.get(621110, 0)
        fv, fvy = c.get(700039, 0) - c.get(700046, 0), y.get(700039, 0) - y.get(700046, 0)
        mg, mgy = c.get(700044, 0), y.get(700044, 0)
        p = pct(br, bry)
        if p is not None and bry > 0:
            if p >= 20: g.append(f"Doanh thu môi giới {fp(p)}")
            elif p <= -20: b.append(f"Doanh thu môi giới giảm {fp(p)}")
        p = pct(mg, mgy)
        if p is not None and mgy > 0:
            if p >= 20: g.append(f"Lãi cho vay ký quỹ {fp(p)}, đạt {fmt_ty(mg)}")
            elif p <= -20: b.append(f"Lãi cho vay ký quỹ giảm {fp(p)}")
        if fv < 0: b.append(f"Mảng tự doanh lỗ ròng {fmt_ty(-fv)} trong quý")
        elif fvy > 0 and fv < fvy * 0.5: b.append("Lãi tự doanh giảm hơn một nửa so với cùng kỳ")
        elif fvy > 0 and fv > fvy * 1.5: g.append("Lãi tự doanh tăng mạnh so với cùng kỳ")
        if ln > 0 and fv > 0 and fv > 0.6 * c.get(23800, 1): b.append("Lợi nhuận phụ thuộc nhiều vào tự doanh, dễ biến động theo thị trường")
    else:
        rv, rvy = c.get(21001, 0), y.get(21001, 0)
        p = pct(rv, rvy)
        if p is not None and rv > 0:
            info.append(f"Doanh thu thuần: {fmt_ty(rv)} ({fp(p)})")
            if p >= 15: g.append(f"Doanh thu tăng {fp(p)}")
            elif p <= -10: b.append(f"Doanh thu giảm {fp(p)}")
        if rv > 0 and rvy > 0:
            gm, gmy = c.get(23100, 0) / rv * 100, y.get(23100, 0) / rvy * 100
            dg = gm - gmy
            s = f"Biên lợi nhuận gộp {gm:.1f}% (cùng kỳ {gmy:.1f}%)".replace(".", ",")
            if dg >= 2: g.append(s + ", cải thiện")
            elif dg <= -2: b.append(s + ", thu hẹp")
        pbt = c.get(23800, 0)
        oth = c.get(23900, 0)
        if pbt > 0 and oth > 0.25 * pbt: b.append(f"Lợi nhuận khác {fmt_ty(oth)}, chiếm {oth/pbt*100:.0f}% lợi nhuận trước thuế: cần xem có phải khoản một lần không")
        fin = c.get(21500, 0) - c.get(22500, 0)
        if pbt > 0 and fin > 0.4 * pbt and c.get(23110, 0) > 0: b.append("Lãi phụ thuộc nhiều vào doanh thu tài chính, không đến từ hoạt động cốt lõi")
        iv, ivy = c.get(22510, 0), y.get(22510, 0)
        p = pct(iv, ivy)
        if p is not None and ivy > 0 and p >= 30 and pbt > 0 and iv > 0.15 * pbt: b.append(f"Chi phí lãi vay tăng {fp(p)}, ăn vào lợi nhuận")
    sc = len(g) - len(b)
    if ln < 0 or (p_ln is not None and p_ln <= -20 and sc <= 0): v = "neg"
    elif sc >= 2 or (sc >= 1 and (p_ln or 0) >= 15): v = "pos"
    else: v = "mid"
    return dict(s=code, form=form, q=tag, date=d0, v=v, info=info[:4], good=g[:4], bad=b[:4])

out = []
for s in W:
    try:
        r = analyse(s)
        if r: out.append(r)
    except Exception as e: print(s, e)
    time.sleep(0.2)
out.sort(key=lambda r: (r["date"], r["s"]), reverse=True)
os.makedirs("data", exist_ok=True)
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
hncodec.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), items=out), "data/kqkd.bin"); hncodec.drop("data/kqkd.json")
# Nhận xét tay: bản gốc để ở _nhanxet.json (GitHub Pages không phục vụ file bắt đầu bằng "_"), web đọc bản .bin
NX = None
for p in ("_nhanxet.json", "data/nhanxet.json"):
    try: NX = json.load(open(p, encoding="utf-8")); break
    except Exception: pass
if NX is not None:
    if not os.path.exists("_nhanxet.json"): json.dump(NX, open("_nhanxet.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    hncodec.dump(NX, "data/nx.bin"); hncodec.drop("data/nhanxet.json")
print("ok", len(out), sum(1 for r in out if r["date"] == out[0]["date"]))
