# BẢN TIN PHONG THẦN – dữ liệu + thẻ hình hằng ngày cho reel/video thời sự chứng khoán (anh Huy 6/11).
# Đọc data/*.bin của web (sức mạnh dòng tiền, độ rộng, mã kéo/đè chỉ số, ngành, Top 10 khỏe nhất, tin doanh nghiệp)
# -> _video/queue/<LÔ>/du_lieu.json + hinh/*.png (thẻ 1008x880, tông tím-vàng, có chữ chungkhoanhuynguyen.com).
# Dùng: python _video/bantin.py <LÔ> [YYYY-MM-DD]
import os, sys, json
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(HERE, "engine"))
os.environ.setdefault("HN_PX", "/tmp/_px_rong.json")
if not os.path.exists(os.environ["HN_PX"]): json.dump({}, open(os.environ["HN_PX"], "w"))
import hncodec, dx2
F = dx2.F
CW, CH = 1008, 880
NEN0, NEN1 = (20, 10, 38), (44, 18, 76)
VANG = (255, 214, 64); TRANG = (255, 255, 255); XANH = (52, 199, 120); DO = (235, 72, 72); MO = (190, 176, 214); TIM = (196, 140, 255)

def nen(title, sub=""):
    im = Image.new("RGB", (CW, CH), NEN0); d = ImageDraw.Draw(im)
    for y in range(CH):
        a = y / CH; d.line([(0, y), (CW, y)], fill=tuple(int(NEN1[i] + (NEN0[i] - NEN1[i]) * a) for i in range(3)))
    d.text((44, 36), title, font=F("Black", 50), fill=VANG)
    if sub: d.text((44, 104), sub, font=F("Medium", 28), fill=MO)
    u1, u2 = "chungkhoanhuynguyen", ".com"; fu = F("Bold", 26)
    d.text((CW - 44 - d.textlength(u1 + u2, font=fu), CH - 52), u1, font=fu, fill=TRANG)
    d.text((CW - 44 - d.textlength(u2, font=fu), CH - 52), u2, font=fu, fill=VANG)
    return im, d

def the_dong_tien(ms, hist, out):
    im, d = nen("SỨC MẠNH DÒNG TIỀN", "Thang 0–100 · nguồn: chungkhoanhuynguyen.com")
    tt = "TẠO ĐÁY" if ms < 20 else "TRUNG TÍNH – YẾU DẦN" if ms < 45 else "ĐỈNH NGẮN HẠN" if ms < 75 else "TẠO ĐỈNH"
    d.text((44, 170), f"{ms:.0f}", font=F("Black", 220), fill=TRANG)
    d.text((44 + d.textlength(f"{ms:.0f}", font=F("Black", 220)) + 16, 330), "/100", font=F("Bold", 60), fill=MO)
    d.text((44, 440), tt, font=F("Black", 56), fill=VANG)
    x0, x1, y = 44, CW - 44, 560
    for i in range(x1 - x0):  # dải màu xanh -> tím -> đỏ
        a = i / (x1 - x0); c = tuple(int(XANH[k] * (1 - a) + DO[k] * a) for k in range(3)) if a > .5 else tuple(int(XANH[k] * (1 - 2 * a) + (150, 130, 190)[k] * 2 * a) for k in range(3))
        d.line([(x0 + i, y), (x0 + i, y + 34)], fill=c)
    xm = x0 + (x1 - x0) * ms / 100; d.rectangle([xm - 6, y - 14, xm + 6, y + 48], fill=TRANG)
    for t, xx in (("Tạo đáy", x0), ("Trung tính", x0 + 230), ("Đỉnh ngắn hạn", x0 + 470), ("Tạo đỉnh", x1 - 150)):
        d.text((xx, y + 60), t, font=F("Medium", 26), fill=MO)
    if hist:
        h = hist[-20:]; gx0, gy0, gw, gh = 44, 700, CW - 88, 110; lo_, hi_ = min(h + [0]), max(h + [100])
        pts = [(gx0 + gw * i / (len(h) - 1), gy0 + gh - gh * (v - lo_) / (hi_ - lo_)) for i, v in enumerate(h)]
        d.line(pts, fill=TIM, width=5); d.text((gx0, gy0 - 34), "20 phiên gần nhất", font=F("Medium", 24), fill=MO)
    im.save(out)

def the_do_rong(br, up, dn, out):
    im, d = nen("BẢNG ĐIỆN HÔM NAY", "Số mã tăng / đứng giá / giảm · mã ảnh hưởng chỉ số nhiều nhất")
    tot = sum(br); x0, w, y = 44, CW - 88, 170
    cs = (XANH, (230, 190, 60), DO); xx = x0
    for v, c in zip(br, cs):
        ww = w * v / tot; d.rectangle([xx, y, xx + ww, y + 70], fill=c); xx += ww
    for i, (lab, v, c) in enumerate((("Tăng", br[0], XANH), ("Đứng", br[1], (230, 190, 60)), ("Giảm", br[2], DO))):
        d.text((x0 + i * 320, y + 92), f"{lab} {v}", font=F("Black", 44), fill=c)
    d.text((44, 360), "KÉO CHỈ SỐ LÊN", font=F("Bold", 30), fill=XANH); d.text((540, 360), "ĐÈ CHỈ SỐ XUỐNG", font=F("Bold", 30), fill=DO)
    for i in range(5):
        y2 = 420 + i * 78
        if i < len(up): d.text((44, y2), f"{up[i][0]}", font=F("Black", 46), fill=TRANG); d.text((230, y2 + 6), f"+{up[i][1]:.2f} điểm".replace(".", ","), font=F("SemiBold", 36), fill=XANH)
        if i < len(dn): d.text((540, y2), f"{dn[i][0]}", font=F("Black", 46), fill=TRANG); d.text((726, y2 + 6), f"{dn[i][1]:.2f} điểm".replace(".", ","), font=F("SemiBold", 36), fill=DO)
    im.save(out)

def the_top10(top, out, upd=""):
    im, d = nen("TOP %d CỔ PHIẾU KHỎE NHẤT" % min(10, len(top)), "Xếp theo sức mạnh giá · " + upd + " · không phải khuyến nghị")
    hd = F("Bold", 26); d.text((44, 160), "#  MÃ", font=hd, fill=MO); d.text((330, 160), "GIÁ", font=hd, fill=MO); d.text((500, 160), "HÔM NAY", font=hd, fill=MO); d.text((720, 160), "3 THÁNG", font=hd, fill=MO)
    for i, x in enumerate(top[:10]):
        y = 210 + i * 60
        if i % 2 == 0: d.rectangle([30, y - 8, CW - 30, y + 50], fill=(54, 26, 92))
        d.text((44, y), f"{i+1:>2}", font=F("Bold", 34), fill=VANG if i < 3 else MO); d.text((110, y - 2), x["s"], font=F("Black", 40), fill=TRANG)
        d.text((330, y), f"{x['close']:.2f}".rstrip("0").rstrip(".").replace(".", ","), font=F("SemiBold", 34), fill=TRANG)
        c = XANH if x["d1"] >= 0 else DO; d.text((500, y), f"{x['d1']:+.2f}%".replace(".", ","), font=F("SemiBold", 34), fill=c)
        d.text((720, y), f"{x['r3']:+.1f}%".replace(".", ","), font=F("SemiBold", 34), fill=XANH if x["r3"] >= 0 else DO)
    im.save(out)

def the_nganh(sec, out):
    im, d = nen("NGÀNH NÀO MẠNH, NGÀNH NÀO YẾU", "% thay đổi bình quân trong phiên")
    s = sec[:4] + sec[-4:]; mx = max(abs(v) for _, v in s) or 1
    for i, (n, v) in enumerate(s):
        y = 180 + i * 80; c = XANH if v >= 0 else DO
        d.text((44, y), n, font=F("Bold", 36), fill=TRANG)
        bw = 280 * abs(v) / mx; d.rectangle([560, y + 8, 560 + bw, y + 48], fill=c)
        d.text((560 + bw + 14, y + 6), f"{v:+.2f}%".replace(".", ","), font=F("Bold", 34), fill=c)
    im.save(out)

def the_the_gioi(wm, out):
    im, d = nen("THẾ GIỚI ĐÊM QUA – SÁNG NAY", "Chỉ số và hàng hoá phiên gần nhất")
    ten = {"spx": "S&P 500 (Mỹ)", "ixic": "Nasdaq (Mỹ)", "dji": "Dow Jones (Mỹ)", "n225": "Nikkei 225 (Nhật)", "kospi": "KOSPI (Hàn)", "gold": "Vàng thế giới", "brent": "Dầu Brent", "dxy": "Chỉ số USD (DXY)"}
    S = {x[0]: x for x in wm["s"]}; y = 170
    for k in ("spx", "ixic", "dji", "n225", "kospi", "gold", "brent", "dxy"):
        if k not in S: continue
        v = S[k][6]; ch = (v[-1] / v[-2] - 1) * 100; c = XANH if ch >= 0 else DO
        d.text((44, y), ten[k], font=F("Bold", 38), fill=TRANG)
        d.text((560, y), f"{v[-1]:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), font=F("SemiBold", 34), fill=MO)
        d.text((800, y), f"{ch:+.2f}%".replace(".", ","), font=F("Black", 38), fill=c); y += 76
    im.save(out)

def the_gioi_data(wm, mac):
    S = {x[0]: x for x in wm["s"]}; o = {}
    for k, x in S.items():
        v = x[6]
        if len(v) >= 2: o[k] = dict(ten=x[1], gia=v[-1], pct=round((v[-1] / v[-2] - 1) * 100, 2))
    return dict(chi_so=o, tin=[dict(ngay=n[1], vung=n[3], tieu_de=n[5]) for n in mac.get("n", [])[:6]],
                fed=mac.get("fed", {}).get("ttl", ""))

def main():
    lo = sys.argv[1]; ngay = sys.argv[2] if len(sys.argv) > 2 else None
    od = os.path.join(HERE, "queue", lo); hd = os.path.join(od, "hinh"); os.makedirs(hd, exist_ok=True)
    D = lambda f: hncodec.load(os.path.join(ROOT, "data", f + ".bin"))
    mw, mwh, rs, nw = D("mw"), D("mwh"), D("rs"), D("news")
    wm, mac, vimo = D("wm"), D("mac"), D("vimo")
    ngay = ngay or mw.get("date")
    ms_hist = [x for x in mwh.get("ms", []) if x is not None]; ms = ms_hist[-1] if ms_hist else 50
    tin = [dict(ma=x[3], loai=x[4], tieu_de=x[5], gio=x[2]) for x in nw["n"] if x[1] == ngay][:40]
    du = dict(ngay=ngay, cap_nhat=mw.get("updated"), suc_manh_dong_tien=ms, dong_tien_20=ms_hist[-20:], do_rong=mw["breadth"],
              keo_len=mw["up"][:5], de_xuong=mw["dn"][:5], nganh=mw.get("sec", []), a50=mw.get("a50"), a200=mw.get("a200"),
              top10=[{k: x[k] for k in ("s", "close", "d1", "r3", "r6", "r12", "fromhi")} for x in rs["top"][:10]], tin=tin, vn_index=vimo.get("vn"), the_gioi=the_gioi_data(wm, mac))
    json.dump(du, open(os.path.join(od, "du_lieu.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    the_dong_tien(ms, ms_hist, os.path.join(hd, "dong_tien.png"))
    the_do_rong(mw["breadth"], mw["up"], mw["dn"], os.path.join(hd, "do_rong.png"))
    the_top10(rs["top"], os.path.join(hd, "top10.png"), rs.get("updated", ""))
    the_nganh(mw.get("sec", []), os.path.join(hd, "nganh.png"))
    the_the_gioi(wm, os.path.join(hd, "the_gioi.png"))
    print("bantin", lo, ngay, "ms", ms)

if __name__ == "__main__":
    main()
