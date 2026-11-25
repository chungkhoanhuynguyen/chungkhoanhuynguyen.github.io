# -*- coding: utf-8 -*-
"""sjc.py (QL1 25/11/2026) – giá vàng miếng SJC + chênh lệch so với vàng thế giới quy đổi.
Ghi data/sjc.bin: {ngay, gio, mua, ban (triệu/lượng), tg (thế giới quy đổi, triệu/lượng, chưa thuế phí),
chenh, chenh_pct, nguon, lich: [[ngay, ban, tg, chenh], ...] tối đa 400 ngày}.
Chỉ công bố MỨC CHÊNH – không công thức vùng giá (bí mật, xem so_viec_ton)."""
import json, re, datetime as dt, urllib.request, urllib.parse
import hncodec

OZ_PER_LUONG = 37.5 / 31.1035
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
VN = dt.timezone(dt.timedelta(hours=7))


def tu_sjc():
    """Nguồn 1: API giá của chính SJC (chi nhánh Hồ Chí Minh)."""
    data = urllib.parse.urlencode({"method": "GetCurrentGoldPricesByBranch", "BranchId": "1"}).encode()
    rq = urllib.request.Request("https://sjc.com.vn/GoldPrice/Services/PriceService.ashx", data=data,
                                headers=dict(UA, **{"Content-Type": "application/x-www-form-urlencoded",
                                                    "Referer": "https://sjc.com.vn/"}))
    d = json.load(urllib.request.urlopen(rq, timeout=30))
    for r in d.get("data", []):
        if re.search(r"SJC\s*1L", r.get("TypeName", "")):
            mua, ban = float(r["BuyValue"]), float(r["SellValue"])
            if mua > 1e6: mua, ban = mua / 1e6, ban / 1e6        # đồng → triệu
            return mua, ban, "SJC (sjc.com.vn)"
    raise ValueError("không thấy dòng Vàng SJC 1L")


def tu_webgia():
    """Nguồn 2 (dự phòng): bảng giá SJC trên webgia.com – số tính theo chỉ."""
    h = urllib.request.urlopen(urllib.request.Request("https://webgia.com/gia-vang/sjc/", headers=UA), timeout=30).read().decode("utf-8", "ignore")
    m = re.search(r"SJC 1L, 10L, 1KG</t[dh]>\s*<td[^>]*>([\d\.]+)</td>\s*<td[^>]*>([\d\.]+)</td>", h)
    if not m: raise ValueError("webgia: không đọc được dòng SJC 1L")
    mua, ban = (float(x.replace(".", "")) for x in m.groups())
    k = 1e5 if mua < 5e7 else 1e6                                   # 14.300.000/chỉ → 143 triệu/lượng
    return mua / k, ban / k, "SJC (webgia.com)"


def the_gioi():
    w = hncodec.load("data/wm.bin", {}) or {}
    s = {r[0]: r for r in w.get("s", [])}
    g, u = s["gold"][6][-1], s["usdvnd"][6][-1]
    return g * OZ_PER_LUONG * u / 1e6, g, u


def main():
    loi = []
    for f in (tu_sjc, tu_webgia):
        try:
            mua, ban, nguon = f(); break
        except Exception as e:
            loi.append(f"{f.__name__}: {type(e).__name__}: {str(e)[:120]}")
    else:
        print("SJC: không lấy được giá –", " | ".join(loi)); return
    if not (60 < ban < 400 and 0 < ban - mua < 15):
        print("SJC: giá bất thường, bỏ qua", mua, ban); return
    tg, g, u = the_gioi()
    now = dt.datetime.now(VN); ngay = now.strftime("%d/%m/%Y")
    old = hncodec.load("data/sjc.bin", {}) or {}
    lich = [r for r in old.get("lich", []) if r[0] != ngay] + [[ngay, round(ban, 2), round(tg, 2), round(ban - tg, 2)]]
    obj = dict(ngay=ngay, gio=now.strftime("%H:%M"), mua=round(mua, 2), ban=round(ban, 2), tg=round(tg, 2),
               vang_tg=g, usdvnd=u, chenh=round(ban - tg, 2), chenh_pct=round((ban / tg - 1) * 100, 1),
               nguon=nguon, lich=lich[-400:])
    hncodec.dump(obj, "data/sjc.bin")
    print(f"SJC {ngay} {obj['gio']}: bán {ban:.2f} tr, thế giới quy đổi {tg:.2f} tr, chênh {ban - tg:.2f} tr ({obj['chenh_pct']}%) – {nguon}")


if __name__ == "__main__":
    main()
