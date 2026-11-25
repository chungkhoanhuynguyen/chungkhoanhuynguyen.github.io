# QL1 25/11/2026: tổ Shorts tin nóng báo "data/*.bin mã hoá, không đọc được" → 0 Short lượt 16:30.
# Chạy: python3 _video/tool/du_lieu_nong.py  (từ gốc repo). In ra SỐ ĐÃ XÁC MINH (dữ liệu web mình)
# để làm tối thiểu 3 Shorts/lượt: VN-Index phiên gần nhất, mã kéo/đè, mã khớp nhiều, SJC vs thế giới,
# vàng/dầu/USD/chứng khoán Mỹ (đổi 1 ngày, 7 ngày, 30 ngày). Ghi kèm --json để lấy dạng máy đọc.
import sys, os, json, datetime
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import hncodec

def ngay(n):
    return (datetime.date(1970, 1, 1) + datetime.timedelta(days=int(n))).strftime("%d/%m/%Y")

def pct(a, b):
    return (a / b - 1) * 100 if b else 0.0

out = {}
mw = hncodec.load("data/mw.bin", {}) or {}
if mw:
    vn, d1 = mw.get("vn", [None, None])
    up, flat, dn = (mw.get("breadth") or [0, 0, 0])[:3]
    out["vnindex"] = {"phien": mw.get("date"), "cap_nhat": mw.get("updated"), "diem": vn, "pct_1phien": d1,
                      "phien_truoc": mw.get("vn_prev"), "ma_tang": up, "dung": flat, "ma_giam": dn,
                      "keo_len_diem": mw.get("up", [])[:5], "de_xuong_diem": mw.get("dn", [])[:5],
                      "khop_nhieu_ty": mw.get("topv", [])[:5]}
sjc = hncodec.load("data/sjc.bin", {}) or {}
if sjc:
    out["sjc"] = {k: sjc.get(k) for k in ("ngay", "gio", "mua", "ban", "tg", "vang_tg", "usdvnd", "chenh", "chenh_pct", "nguon")}
wm = hncodec.load("data/wm.bin", {}) or {}
tg = []
for s in wm.get("s", []):
    key, ten, dv, _, _, d, v = s[:7]
    if not v: continue
    def ago(k):
        return pct(v[-1], v[-1 - k]) if len(v) > k else None
    tg.append({"ma": key, "ten": ten, "don_vi": dv, "ngay": ngay(d[-1]), "gia": v[-1],
               "pct_1": ago(1), "pct_5phien": ago(5), "pct_21phien": ago(21),
               "dinh_1nam": max(v[-252:]), "day_1nam": min(v[-252:])})
out["the_gioi"] = tg
vimo = hncodec.load("data/vimo.bin", {}) or {}
out["vi_mo"] = [{"ten": i.get("name"), "gia_tri": i.get("val"), "don_vi": i.get("unit"), "pct_1ngay": i.get("d1"), "pct_1thang": i.get("m1")} for i in vimo.get("items", [])]

if "--json" in sys.argv:
    print(json.dumps(out, ensure_ascii=False, indent=1)); sys.exit()
f = lambda x: "—" if x is None else ("%+.2f%%" % x).replace(".", ",")
v = out.get("vnindex")
if v:
    print("VN-INDEX phiên %s (cập nhật %s): %s điểm, %s; tăng %s / đứng %s / giảm %s mã" % (v["phien"], v["cap_nhat"], v["diem"], f(v["pct_1phien"]), v["ma_tang"], v["dung"], v["ma_giam"]))
    print("  Kéo lên (điểm): " + ", ".join("%s %+.2f" % (a, b) for a, b in v["keo_len_diem"]))
    print("  Đè xuống (điểm): " + ", ".join("%s %+.2f" % (a, b) for a, b in v["de_xuong_diem"]))
    print("  Khớp nhiều (tỷ đồng, %): " + ", ".join("%s %.0f tỷ %s" % (x[0], x[1], f(x[2])) for x in v["khop_nhieu_ty"]))
s = out.get("sjc")
if s:
    print("SJC %s %s: mua %s / bán %s triệu/lượng; thế giới quy đổi %s triệu (%s USD/oz, USD %s) → chênh %s triệu (%s%%) – nguồn %s" % (
        s["ngay"], s["gio"], s["mua"], s["ban"], s["tg"], s["vang_tg"], s["usdvnd"], s["chenh"], s["chenh_pct"], s["nguon"]))
for t in tg:
    print("%s (%s) ngày %s: %s | 1 phiên %s | 1 tuần %s | 1 tháng %s | đỉnh/đáy 1 năm %s / %s" % (
        t["ten"], t["don_vi"], t["ngay"], t["gia"], f(t["pct_1"]), f(t["pct_5phien"]), f(t["pct_21phien"]), t["dinh_1nam"], t["day_1nam"]))
for i in out["vi_mo"]:
    print("Vĩ mô – %s: %s %s | 1 ngày %s | 1 tháng %s" % (i["ten"], i["gia_tri"], i["don_vi"], f(i["pct_1ngay"]), f(i["pct_1thang"])))
print("Nguồn ghi trên thẻ: 'Dữ liệu chungkhoanhuynguyen.com, <ngày>'. Số tự tính ghi cách tính.")
