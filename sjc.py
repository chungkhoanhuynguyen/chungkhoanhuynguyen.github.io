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
    cap_nhat_trang(obj)
    print(f"SJC {ngay} {obj['gio']}: bán {ban:.2f} tr, thế giới quy đổi {tg:.2f} tr, chênh {ban - tg:.2f} tr ({obj['chenh_pct']}%) – {nguon}")


# ---- B1 (Phòng Web 28/11): trang /gia-vang-sjc-hom-nay.html – ma.py dựng cả trang mỗi ngày,
# sjc.py (info.yml 4 lần/ngày) chỉ thay khối giữa 2 dấu <!--sjc--> … <!--/sjc--> để số luôn mới.
TRANG = "gia-vang-sjc-hom-nay.html"
_vn = lambda v, k: f"{v:,.{k}f}".replace(",", "#").replace(".", ",").replace("#", ".")
_f1 = lambda v: f"{v:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".").rstrip("0").rstrip(",")


def _svg(lich):
    """Biểu đồ đường giá SJC bán ra và thế giới quy đổi (SVG tĩnh, không JS)."""
    L = lich[-30:]
    if len(L) < 5: return ""
    W, H, pl, pr, pt, pb = 640, 220, 44, 10, 12, 26
    vs = [r[1] for r in L] + [r[2] for r in L]; lo, hi = min(vs), max(vs); pad = (hi - lo) * .08 or 1; lo -= pad; hi += pad
    X = lambda i: pl + i * (W - pl - pr) / (len(L) - 1); Y = lambda v: pt + (hi - v) * (H - pt - pb) / (hi - lo)
    pts = lambda k: " ".join(f"{X(i):.1f},{Y(r[k]):.1f}" for i, r in enumerate(L))
    g = "".join(f'<line x1="{pl}" x2="{W-pr}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" class="gl"/><text x="{pl-6}" y="{Y(v)+4:.1f}" text-anchor="end">{v:.0f}</text>'
                for v in [lo + (hi - lo) * t for t in (.1, .5, .9)])
    xl = "".join(f'<text x="{X(i):.1f}" y="{H-6}" text-anchor="middle">{L[i][0][:5]}</text>' for i in sorted({0, len(L) // 2, len(L) - 1}))
    return (f'<figure class="vg"><svg viewBox="0 0 {W} {H}" role="img" aria-label="Giá vàng SJC bán ra và giá thế giới quy đổi {len(L)} ngày gần nhất">{g}{xl}'
            f'<polyline points="{pts(1)}" class="l1"/><polyline points="{pts(2)}" class="l2"/></svg>'
            f'<figcaption><i class="c1"></i>SJC bán ra <i class="c2"></i>Thế giới quy đổi (triệu đồng/lượng)</figcaption></figure>')


def khoi(d):
    """Khối số liệu động của trang giá vàng (HTML)."""
    if not d or not d.get("ban"): return "<p>Chưa có số liệu giá vàng SJC.</p>"
    L = d.get("lich", []); t5 = L[-6] if len(L) > 5 else None
    o = [f'<div class="vgk"><div><p class="k">SJC mua vào</p><p class="v">{_f1(d["mua"])}</p></div><div><p class="k">SJC bán ra</p><p class="v">{_f1(d["ban"])}</p></div>'
         f'<div><p class="k">Thế giới quy đổi</p><p class="v">{_f1(d["tg"])}</p></div><div><p class="k">Chênh lệch</p><p class="v do">{_f1(d["chenh"])} <small>({str(d["chenh_pct"]).replace(".", ",")}%)</small></p></div></div>',
         f'<p class="vgt">Đơn vị: triệu đồng/lượng. Cập nhật {d["gio"]} ngày {d["ngay"]}. Nguồn giá SJC: {d["nguon"]}. Thế giới quy đổi = vàng thế giới {_vn(d["vang_tg"], 1)} USD/ounce × tỷ giá {_vn(d["usdvnd"], 0)} đồng/USD × 1,2057 ounce/lượng, chưa gồm thuế, phí. Mua vào – bán ra chênh {_f1(d["ban"] - d["mua"])} triệu/lượng.</p>',
         ]
    if t5: o.append(f'<p>Mức chênh với thế giới 5 lần cập nhật trước ({t5[0]}) là <b>{_f1(t5[3])} triệu đồng/lượng</b>, nay là <b>{_f1(d["chenh"])} triệu</b>.</p>')
    o.append(_svg(L))
    o.append("<h2>Lịch sử giá vàng SJC và chênh lệch</h2><div style='overflow-x:auto'><table class='mt'><tr><td><b>Ngày</b></td><td class='r'><b>Bán ra</b></td><td class='r'><b>Thế giới</b></td><td class='r'><b>Chênh</b></td></tr>"
             + "".join(f"<tr><td>{r[0]}</td><td class='r'>{_f1(r[1])}</td><td class='r'>{_f1(r[2])}</td><td class='r'>{_f1(r[3])}</td></tr>" for r in L[::-1][:30]) + "</table></div>")
    return "\n".join(o)


CSS_VG = (".vgk{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:14px 0 6px}.vgk>div{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:10px 12px}"
          ".vgk .k{margin:0;font-size:13px;color:var(--mute)}.vgk .v{margin:0;font-size:22px;font-weight:800;font-variant-numeric:tabular-nums}.vgk .v.do{color:#c0392b}.vgk small{font-size:14px;font-weight:600}"
          ".vgt{font-size:13px;color:var(--mute);line-height:1.6}.vg{margin:18px 0}.vg svg{width:100%;height:auto;display:block}.vg text{font-size:12px;fill:var(--mute)}.vg .gl{stroke:var(--line)}"
          ".vg polyline{fill:none;stroke-width:2.5;stroke-linejoin:round}.vg .l1{stroke:var(--gold)}.vg .l2{stroke:var(--acc)}.vg figcaption{font-size:13px;color:var(--mute)}"
          ".vg i{display:inline-block;width:12px;height:3px;margin:0 6px 3px 10px;vertical-align:middle}.vg .c1{background:var(--gold)}.vg .c2{background:var(--acc)}"
          "@media(max-width:600px){.vgk{grid-template-columns:1fr 1fr}.vgk .v{font-size:19px}}")


def cap_nhat_trang(d):
    import os
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), TRANG)
    if not os.path.exists(p): return
    s = open(p, encoding="utf-8").read(); a, b = s.find("<!--sjc-->"), s.find("<!--/sjc-->")
    if a < 0 or b < 0: return
    open(p, "w", encoding="utf-8").write(s[:a + 10] + khoi(d) + s[b:])


if __name__ == "__main__":
    main()
