# Đổi số đọc bằng chữ (cho giọng đọc) thành chữ số trong phụ đề: "bốn mươi bốn phẩy chín phần trăm" -> "44,9%"
import re
D = {"không": 0, "một": 1, "mốt": 1, "hai": 2, "ba": 3, "bốn": 4, "tư": 4, "năm": 5, "lăm": 5, "nhăm": 5, "sáu": 6, "bảy": 7, "tám": 8, "chín": 9}
M = {"nghìn": 10**3, "ngàn": 10**3, "triệu": 10**6, "tỷ": 10**9, "tỉ": 10**9}
W = set(D) | set(M) | {"mười", "mươi", "trăm", "linh", "lẻ"}
def _num(ws):
    tot = 0; grp = 0; cur = 0; seen = False; hd = False
    for i, w in enumerate(ws):
        if w in D:
            v = D[w]
            if w == "tư" and not (i and ws[i-1] == "mươi"): return None
            if w in ("mốt", "lăm", "nhăm") and not (i and ws[i-1] in ("mươi", "mười")): v = 1 if w == "mốt" else 5
            cur += v; seen = True; hd = True
        elif w == "mười": cur += 10; seen = True
        elif w == "mươi": cur = (cur or 1) * 10 if cur < 10 else cur * 10
        elif w == "trăm": grp += (cur if hd else 1) * 100; cur = 0; hd = False
        elif w in ("linh", "lẻ"): pass
        elif w in M: tot += (grp + cur) * M[w]; grp = 0; cur = 0; hd = False
    return tot + grp + cur if seen else None
def _fmt(n): return "{:,}".format(n).replace(",", ".")
def doi(s):
    toks = s.split(" "); out = []; i = 0
    while i < len(toks):
        j = i
        while j < len(toks) and toks[j].lower().strip(",.") in W and not (j > i and toks[j-1][-1:] in ",."):
            w = toks[j].lower().strip(",.")
            if w == "năm":   # "năm" là số chỉ khi đứng sau từ số hoặc trước đơn vị số
                prv = toks[j-1].lower().strip(",.") if j > i else ""
                nxt = toks[j+1].lower().strip(",.") if j + 1 < len(toks) else ""
                # QL1 11/11: sau "mười/mươi" số 5 đọc là "lăm", nên "tháng mười năm hai nghìn…" / "hai mươi năm" là NĂM (thời gian), không phải 15/25
                if not (prv in ("linh", "lẻ") or nxt in ("mươi", "trăm", "nghìn", "ngàn", "triệu", "tỷ", "tỉ", "phẩy", "phần")): break
            if j > i and toks[j-1].lower().strip(",.") in D and w in D: break   # 2 chữ số liền nhau = 2 số khác nhau
            j += 1
        if j > i:
            seg = [t.lower().strip(",.") for t in toks[i:j]]
            # bỏ đơn vị lớn đứng cuối để giữ chữ (vd "hai trăm tỷ" -> "200 tỷ")
            unit = ""
            # QL1 11/11: "một tỷ một trăm triệu" -> "1 tỷ 100 triệu" (trước bị thành "1.000.000.100 triệu")
            if len(seg) > 2 and seg[-1] in M and any(w in M and M[w] > M[seg[-1]] for w in seg[:-1]):
                parts = []; grp = []
                for w in seg:
                    if w in M and grp:
                        v = _num(grp); parts.append(("%s %s" % (_fmt(v), w)) if v is not None else None); grp = []
                    else: grp.append(w)
                if all(parts) and not grp:
                    out.append(" ".join(parts) + (toks[j-1][-1] if toks[j-1][-1:] in ",." else "")); i = j; continue
            if len(seg) > 1 and seg[-1] in M and seg[-2] not in M: unit = " " + toks[j-1].strip(",."); seg = seg[:-1]
            n = _num(seg)
            nxt = toks[j].lower() if j < len(toks) else ""
            if n is not None and not (n < 10 and len(seg) == 1 and not unit and nxt not in ("phẩy", "phần")):
                prv = toks[i-1].lower() if i else ""
                txt = (str(n) if prv == "năm" and 1900 <= n <= 2100 else _fmt(n)) + unit; tail = toks[j-1][-1] if toks[j-1][-1:] in ",." else ""
                # phẩy + phần thập phân
                if j + 1 < len(toks) and toks[j] == "phẩy":
                    k = j + 1; dec = ""
                    while k < len(toks) and toks[k].lower().strip(",.") in D: dec += str(D[toks[k].lower().strip(",.")]); tail = toks[k][-1] if toks[k][-1:] in ",." else ""; k += 1
                    if dec and not unit: txt = _fmt(n) + "," + dec; j = k
                out.append(txt + tail); i = j; continue
        out.append(toks[i]); i += 1
    r = " ".join(out)
    r = re.sub(r"(\d) phần trăm", r"\1%", r)
    return r
if __name__ == "__main__":
    for t in ["Lợi nhuận chín tháng tăng bốn mươi bốn phẩy chín phần trăm, đạt hai mươi ba nghìn hai trăm hai mươi bảy tỷ đồng.",
              "Quý ba năm ngoái lợi nhuận đã nhảy từ bốn nghìn tám trăm sáu mươi hai tỷ lên bảy nghìn hai trăm bảy mươi lăm tỷ.",
              "Năm hai nghìn không trăm hai mươi lăm, một USD đổi hai mươi lăm nghìn tám trăm linh hai đồng.", "Có ba lý do, và một bài học."]:
        print(doi(t))
