# Thẻ "Soi 3 dòng" (A1, 26/11/2026): lỗ lũy kế so vốn góp, lãi vay so lợi nhuận trước lãi vay và thuế 4 quý,
# dòng tiền kinh doanh 4 quý. Dùng chung cho trang /ma/<MÃ>.html (ma.py, HTML tĩnh) và mục #bctc trang chủ
# (data/bctc/_soi.bin, index.html tự vẽ). Chỉ đọc số, không khuyến nghị mua bán.
import os, re, html, hncodec
ROOT = os.path.dirname(os.path.abspath(__file__))
e = lambda s: html.escape(str(s if s is not None else ""), quote=True)
try:
    _m = re.search(r'BH = set\("([^"]+)"', open(os.path.join(ROOT, "mw.py"), encoding="utf-8").read())
    BH = set(_m.group(1).split()) if _m else set()
except Exception:
    BH = set()
BH |= {"BVH", "BMI", "PVI", "MIG", "PTI", "BIC", "ABI", "VNR", "PGI"}
TEN = {"bank": "ngân hàng", "ck": "công ty chứng khoán", "bh": "công ty bảo hiểm"}
DEN = {"xanh": "Ổn", "vang": "Cần để ý", "do": "Cảnh báo", "xam": "Thiếu số"}


def ql(d): return "Q%d/%s" % ((int(d[5:7]) - 1) // 3 + 1, d[:4])


def ty(v):
    """Số tỷ đồng kiểu Việt: 3.607 hoặc 8,4 (giá trị nhỏ)."""
    a = abs(v)
    s = f"{a:,.1f}" if a < 10 else f"{a:,.0f}"
    s = s.replace(",", "#").replace(".", ",").replace("#", ".")
    return ("−" if v < 0 else "") + s


def _row(rows, *names):
    for n in names:
        for r in rows:
            if r[0].strip().lower() == n.lower(): return r[2]
    return None


def _sum4(v):
    if not v or len(v) < 4 or any(x is None for x in v[:4]): return None
    return sum(v[:4])


def tinh(s, B):
    """Trả về dict {ma, loai, ky, rows:[{ten, den, so, cau, ky}]} hoặc None nếu không có dữ liệu quý."""
    q = (B or {}).get("q") or {}
    d = q.get("d") or []
    if not d: return None
    bs, is_, cf = q.get("bs", []), q.get("is", []), q.get("cf", [])
    loai = "bh" if s in BH else B.get("f", "dn")
    tc = loai in TEN
    k1 = "cuối " + ql(d[0])
    k4 = f"4 quý {ql(d[3])}–{ql(d[0])}" if len(d) >= 4 else ""
    R = []
    # (1) Lỗ lũy kế so với vốn góp chủ sở hữu
    lp, vg = _row(bs, "Lợi nhuận sau thuế chưa phân phối"), _row(bs, "Vốn góp", "Vốn góp của chủ sở hữu")
    L = lp[0] if lp else None; V = vg[0] if vg else None
    r = {"ten": "Lỗ lũy kế so với vốn góp", "ky": k1}
    if L is None:
        r.update(den="xam", so="–", cau="Báo cáo chưa có dòng lợi nhuận sau thuế chưa phân phối.")
    elif L >= 0:
        r.update(den="xanh", so=f"Lãi giữ lại {ty(L)} tỷ đồng" + (f" · vốn góp {ty(V)} tỷ" if V else ""),
                 cau="Chưa có lỗ dồn từ các năm trước: công ty vẫn còn tiền lãi giữ lại trên sổ.")
    elif not V:
        r.update(den="xam", so=f"Lỗ lũy kế {ty(-L)} tỷ đồng", cau="Thiếu số vốn góp để so sánh.")
    else:
        t = -L / V * 100
        r["so"] = f"Lỗ lũy kế {ty(-L)} tỷ / vốn góp {ty(V)} tỷ ({round(t)}%)"
        if t > 100: r.update(den="do", cau="Lỗ dồn lại còn lớn hơn cả số vốn cổ đông góp: phần vốn góp coi như đã bị lỗ ăn hết.")
        elif t > 50: r.update(den="vang", cau="Lỗ dồn lại đã ăn hơn một nửa số vốn cổ đông góp.")
        else: r.update(den="xanh", cau="Có lỗ dồn từ trước nhưng còn nhỏ so với vốn cổ đông góp.")
    R.append(r)
    # (2) Chi phí lãi vay so với lợi nhuận trước lãi vay và thuế, 4 quý
    r = {"ten": "Lãi vay so với lợi nhuận trước lãi vay và thuế", "ky": k4}
    if tc:
        r.update(den="na", so="", ky="", cau=f"Không áp dụng cho {TEN[loai]}: tiền vay, tiền huy động là nguyên liệu kinh doanh, nên lãi vay không đo được sức chịu nợ như doanh nghiệp thường.")
    else:
        lt = _sum4(_row(is_, "Lợi nhuận kế toán trước thuế"))
        lvr = _row(is_, "Trong đó: Chi phí lãi vay", "Chi phí lãi vay")
        lv = 0.0 if lvr is None else _sum4([None if x is None else abs(x) for x in lvr])
        if lt is None or lv is None:
            r.update(den="xam", so="–", cau="Chưa đủ 4 quý dữ liệu để tính.")
        elif lv < 0.05:
            r.update(den="xanh", so=f"Lãi vay 0 tỷ · lợi nhuận trước thuế {ty(lt)} tỷ", cau="Không ghi nhận chi phí lãi vay trong 4 quý: không phải gánh lãi ngân hàng.")
        else:
            eb = lt + lv
            if eb <= 0:
                r.update(den="do", so=f"Lãi vay {ty(lv)} tỷ / lợi nhuận trước lãi vay và thuế {ty(eb)} tỷ",
                         cau="Làm ăn chưa ra lời mà vẫn phải trả lãi vay: tiền lãi đang ăn dần vào vốn.")
            else:
                t = lv / eb * 100
                r["so"] = f"Lãi vay {ty(lv)} tỷ / lợi nhuận trước lãi vay và thuế {ty(eb)} tỷ ({round(t)}%)"
                c = f"Cứ 100 đồng lời làm ra (trước lãi vay và thuế), khoảng {round(t)} đồng phải đem trả lãi vay"
                if t >= 70: r.update(den="do", cau=c + ": phần lớn công sức làm ra là để trả nợ.")
                elif t >= 30: r.update(den="vang", cau=c + ": nợ vay đang chiếm phần đáng kể.")
                else: r.update(den="xanh", cau=c + ".")
    R.append(r)
    # (3) Dòng tiền từ hoạt động kinh doanh, 4 quý
    r = {"ten": "Dòng tiền từ hoạt động kinh doanh", "ky": k4}
    if tc:
        r.update(den="na", so="", ky="", cau=f"Không áp dụng cho {TEN[loai]}: dòng tiền kinh doanh lên xuống theo tiền gửi, cho vay, đầu tư, nên không dùng để soi chất lượng lãi.")
    else:
        cfo = _sum4(_row(cf, "Lưu chuyển tiền thuần từ hoạt động kinh doanh"))
        ln = _sum4(_row(is_, "Lợi nhuận sau thuế thu nhập doanh nghiệp", "Lợi nhuận sau thuế"))
        if cfo is None:
            r.update(den="xam", so="–", cau="Chưa đủ 4 quý dữ liệu để tính.")
        else:
            r["so"] = f"Dòng tiền kinh doanh {ty(cfo)} tỷ" + ("" if ln is None else f" · lãi sau thuế {ty(ln)} tỷ")
            if cfo < 0 and ln is not None and ln > 0: r.update(den="do", cau="Sổ sách báo lãi nhưng tiền thật thu về từ kinh doanh lại âm: lãi đang nằm ở khoản phải thu, hàng tồn kho.")
            elif cfo < 0: r.update(den="vang", cau="Kinh doanh đang tiêu nhiều tiền hơn số tiền thu về.")
            elif ln is not None and ln <= 0: r.update(den="xanh", cau="Dòng tiền kinh doanh vẫn dương dù sổ sách đang lỗ: bán hàng vẫn thu được tiền về.")
            else: r.update(den="xanh", cau="Kinh doanh thu về tiền thật, không chỉ lãi trên giấy.")
    R.append(r)
    return {"ma": s, "loai": loai, "ky": ql(d[0]), "rows": R}


CSS = (".s3{margin:16px 0 20px;padding:14px 16px;border:1px solid var(--line,#e3dfe9);border-radius:12px;background:var(--panel,#fff);max-width:100%;box-sizing:border-box}"
       ".s3 h2{margin:0 0 2px;font-size:19px}.s3 .s3k{margin:0 0 8px;color:var(--mute,#5f5a69);font-size:13px}"
       ".s3 ul{list-style:none;margin:0;padding:0}.s3 li{display:flex;gap:10px;padding:10px 0;border-top:1px solid var(--line,#e3dfe9)}"
       ".s3 li:first-child{border-top:0}.s3 i{flex:none;width:14px;height:14px;border-radius:50%;margin-top:4px;background:#9a95a3}"
       ".s3 .xanh i{background:#0a8a4a}.s3 .vang i{background:#e0a419}.s3 .do i{background:#c0392b}.s3 .na i{background:transparent;border:2px solid #b9b4c2;box-sizing:border-box}"
       ".s3 li>div{min-width:0;flex:1}.s3 b{display:block;font-size:15px}.s3 .s3d{font-size:12px;font-weight:700;border-radius:6px;padding:1px 7px;margin-left:6px;vertical-align:1px;background:#f1eef6}"
       ".s3 .xanh .s3d{color:#0a6a3a;background:#e6f3ec}.s3 .vang .s3d{color:#7a5a06;background:#fbf1d6}.s3 .do .s3d{color:#a12e22;background:#fbeceb}"
       ".s3 .s3s{font-variant-numeric:tabular-nums;font-weight:600;font-size:14px;margin:2px 0;overflow-wrap:anywhere}.s3 p{margin:2px 0;font-size:14px;line-height:1.5}.s3 small{color:var(--mute,#5f5a69);font-size:12px}"
       ".s3 .s3g{margin:10px 0 0;padding-top:10px;border-top:1px dashed var(--line,#e3dfe9);font-size:14px}"
       ".s3 .s3g button{border:0;background:none;padding:0;color:var(--acc,#6a2d86);font:700 14px inherit;font-family:inherit;text-decoration:underline;cursor:pointer;text-align:left}")


def the_html(o, h="h2"):
    """HTML thẻ Soi 3 dòng (trang mã)."""
    li = []
    for r in o["rows"]:
        dn = r["den"]
        lab = "" if dn == "na" else f'<span class="s3d">{DEN[dn]}</span>'
        li.append(f'<li class="{dn}"><i aria-hidden="true"></i><div><b>{e(r["ten"])}{lab}</b>'
                  + (f'<div class="s3s">{e(r["so"])}</div>' if r.get("so") else "")
                  + f'<p>{e(r["cau"])}</p>' + (f'<small>Kỳ dữ liệu: {e(r["ky"])}</small>' if r.get("ky") else "") + "</div></li>")
    s = e(o["ma"])
    return (f'<section class="s3" id="soi3" aria-label="Soi 3 dòng báo cáo tài chính {s}"><{h}>Soi 3 dòng BCTC {s}</{h}>'
            f'<p class="s3k">Đèn xanh, vàng, đỏ cho 3 dòng hay giấu rủi ro nhất · số liệu tỷ đồng, BCTC hợp nhất đến {e(o["ky"])}</p><ul>' + "".join(li) +
            f'</ul><p class="s3g">Đọc vẫn rối? <button type="button" data-soima="{s}">Gửi mã này để em soi cùng</button> <span class="s3t" aria-live="polite"></span></p></section>')


def tat_ca():
    """Tính cho mọi mã có data/bctc/<MÃ>.bin, ghi data/bctc/_soi.bin cho trang chủ."""
    out = {}
    dd = os.path.join(ROOT, "data/bctc")
    for f in sorted(os.listdir(dd)):
        if f.startswith("_") or not f.endswith(".bin"): continue
        try:
            o = tinh(f[:-4], hncodec.load(os.path.join(dd, f)))
            if o: out[f[:-4]] = o
        except Exception as ex:
            print("soi3 loi", f, ex)
    hncodec.dump(out, os.path.join(dd, "_soi.bin"))
    return out


if __name__ == "__main__":
    A = tat_ca()
    import collections
    print(len(A), "mã", collections.Counter(r["den"] for o in A.values() for r in o["rows"]))
