# Sinh bảng REP (chữ số đọc -> chữ số) cho data.ts từ kich_ban.json: python3 so_rep.py kich_ban.json
import json, re, sys
D = {"không":0,"một":1,"mốt":1,"hai":2,"ba":3,"bốn":4,"tư":4,"năm":5,"lăm":5,"sáu":6,"bảy":7,"tám":8,"chín":9}
NUMW = set(D) | {"mười","mươi","trăm","nghìn","linh","triệu"}
def parse(ws):
    tot = 0; cur = 0; last = 0
    i = 0
    while i < len(ws):
        w = ws[i]
        if w in D: last = D[w]
        elif w == "mười": last = 10
        elif w == "mươi": last = last * 10
        elif w == "linh": pass
        elif w == "trăm": cur += last * 100; last = 0; i += 1; continue
        elif w == "nghìn": tot += (cur + last) * 1000; cur = 0; last = 0; i += 1; continue
        elif w == "triệu": tot += (cur + last) * 1000000; cur = 0; last = 0; i += 1; continue
        else: return None
        # cộng dồn hàng chục/đơn vị
        if i + 1 < len(ws) and ws[i+1] == "mươi": i += 1; last *= 10
        if i + 1 < len(ws) and ws[i+1] in D and ws[i] in ("mươi", "mười") or (ws[i] == "mười" and i + 1 < len(ws) and ws[i+1] in D):
            pass
        i += 1
        # gộp chục + đơn vị
        if i < len(ws) and ws[i] in D and (ws[i-1] in ("mươi", "mười")): last += D[ws[i]]; i += 1
        if i < len(ws) and ws[i] in D and i >= 2 and ws[i-1] in D and ws[i-2] == "linh": pass
    return tot + cur + last
def fmt(n): return f"{n:,}".replace(",", ".") if n >= 1000 and not (1000 <= n <= 2100) else str(n)
def rep(text):
    out = {}
    toks = re.findall(r"\w+|[^\w\s]", text)
    i = 0
    while i < len(toks):
        if toks[i].lower() in NUMW and toks[i].lower() not in ("mươi", "trăm", "nghìn", "linh", "triệu"):
            j = i
            while j < len(toks) and toks[j].lower() in NUMW: j += 1
            ws = [t.lower() for t in toks[i:j]]
            year = ws[0] == "năm" and len(ws) > 1 and ws[1] != "mươi" and ws[1] != "trăm"
            k = 1 if year else 0
            span = toks[i+k:j]
            low = [t.lower() for t in span]
            for q in range(1, len(low) - 2):
                if low[q] == "năm" and low[q+1] in D and "nghìn" in low[q+1:] and "nghìn" not in low[:q]:
                    span = span[q+1:]; break
            if len(span) > 1 and span[-1].lower() == "năm" and span[-2].lower() != "linh": span = span[:-1]; j -= 1
            pt = j + 1 < len(toks) and toks[j] == "phần" and toks[j+1] == "trăm"
            if span:
                n = parse([t.lower() for t in span])
                if n is not None and (len(span) > 1 or n >= 10 or pt):
                    if pt: out[" ".join(span) + " phần trăm"] = fmt(n) + "%"
                    elif len(span) > 1 or n >= 10: out[" ".join(span)] = fmt(n)
            i = j
        else: i += 1
    return out
if __name__ == "__main__":
    k = json.load(open(sys.argv[1])); R = {}
    for s in k["scenes"]: R.update(rep(s["say"]))
    for a, b in sorted(R.items(), key=lambda x: -len(x[0])): print(f"  [/{a}/g, \"{b}\"],  ")
