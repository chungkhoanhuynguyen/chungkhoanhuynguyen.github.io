# Dữ liệu cho mục Soi chart: giá ngày 3 năm (đã điều chỉnh) của cổ phiếu, ETF sàn HOSE và các chỉ số.
# Chạy sau phiên mỗi ngày. Mỗi mã 1 file data/c/MÃ.json, phần phiên mới ghi vào data/c/recent.json,
# đủ khoảng 25 phiên thì gộp lại vào file từng mã (tránh repo phình to).
import json, time, datetime, urllib.request, os, sys, base64
from concurrent.futures import ThreadPoolExecutor
_h = lambda s: base64.b64decode(s).decode()
S1 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
S2 = _h("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==")
UA = {"User-Agent": "Mozilla/5.0"}
D = "data/c/"
IDX = {"VNINDEX": "Chỉ số VN-Index", "VN30": "Chỉ số VN30", "VN100": "Chỉ số VN100", "HNX": "Chỉ số HNX-Index",
       "HNX30": "Chỉ số HNX30", "UPCOM": "Chỉ số UPCoM-Index", "VN30F1M": "Hợp đồng tương lai VN30 tháng gần nhất"}
FL = {"HOSE": "H", "HNX": "X", "UPCOM": "U"}
FOLD = 25
import re
def ten(n):
    n = re.sub(r"\s+", " ", n or "").strip(" -–")
    for _ in range(2):
        n = re.sub(r"(?i)^ngân hàng thương mại cổ phần", "Ngân hàng TMCP", n)
        n = re.sub(r"(?i)^(tổng công ty|tổng cty|công ty|cty|ctcp)( cổ phần| cp)?\s+", "", n).strip(" -–")
        n = re.sub(r"(?i)\s*-\s*(ctcp|công ty cổ phần)$", "", n)
        n = re.sub(r"(?i)^cổ phần\s+", "", n)
    return n[:1].upper() + n[1:] if n else n

def get(url):
    err = None
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r: return json.load(r)
        except Exception as e:
            err = e; time.sleep(1.5 + k)
    print("lỗi", url[-40:], err); return None

def bars(sym):
    to = int(time.time()); j = get(f"{S1}?resolution=D&symbol={sym}&from={to - 3*365*86400 - 86400*3}&to={to + 86400}")
    if not j or not j.get("t"): return []
    out, seen = [], set()
    for t, o, h, l, c, v in zip(j["t"], j["o"], j["h"], j["l"], j["c"], j.get("v") or [0]*len(j["t"])):
        d = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%d")
        if d in seen or c is None: continue
        seen.add(d)
        P = lambda x: int(round((x if x is not None else c) * 100))
        out.append([d, P(o), P(h), P(l), P(c), int(round((v or 0) / 100))])
    return out

def enc(sym, b):
    d0 = datetime.date.fromisoformat(b[0][0]); g, prev = [], d0
    for x in b:
        dd = datetime.date.fromisoformat(x[0]); g.append((dd - prev).days); prev = dd
    return {"s": sym, "d0": b[0][0], "g": g, "o": [x[1] for x in b], "h": [x[2] for x in b], "l": [x[3] for x in b], "c": [x[4] for x in b], "v": [x[5] for x in b]}

def dec(j):
    d, out = datetime.date.fromisoformat(j["d0"]), []
    for i, gap in enumerate(j["g"]):
        d = d + datetime.timedelta(days=gap)
        out.append([d.isoformat(), j["o"][i], j["h"][i], j["l"][i], j["c"][i], j["v"][i]])
    return out

def main():
    os.makedirs(D, exist_ok=True)
    if not os.path.exists(D + "live.json"): open(D + "live.json", "w").write('{"d":"","t":"","b":{}}')
    full = len(sys.argv) > 1 and sys.argv[1] == "full"
    j = get(f"{S2}stocks?q=type:STOCK,IFC,ETF~status:LISTED&fields=code,companyName,floor,type&size=3000") or {"data": []}
    rows = [(x["code"], FL[x["floor"]], (x.get("companyName") or "").strip(), x.get("type")) for x in j["data"] if x.get("floor") in FL and x.get("code")]
    if len(rows) < 500:  # nguồn danh sách lỗi thì giữ danh sách cũ
        try: old = json.load(open(D + "syms.json")); rows = [(r[0], r[1], r[2], "") for r in old["s"] if r[1] != "I"]
        except Exception: pass
    mine = sorted(set([r[0] for r in rows if r[1] == "H"]) | set(IDX))
    try: R = json.load(open(D + "recent.json")).get("b", {})
    except Exception: R = {}
    if not full and any(len(v) >= FOLD for v in R.values()): full = True; print("gộp dữ liệu vào từng mã")
    def work(sym):
        b = bars(sym)
        if len(b) < 2: return sym, None, "trống", 0
        t = b[-20:]; lq = round(sum(x[4] * x[5] for x in t) / 1e6 / len(t), 1)  # GTGD bình quân 20 phiên, tỷ đồng
        fn = D + sym + ".json"; H = None
        try: H = dec(json.load(open(fn)))
        except Exception: pass
        same = False
        if H and not full:
            m = {x[0]: x for x in b}
            tail = [x for x in H[-4:] if x[0] in m]
            same = len(tail) >= 2 and all(abs(m[x[0]][4] - x[4]) <= max(1, abs(x[4]) * 0.002) for x in tail)
        if same:
            last = H[-1][0]
            return sym, [x for x in b if x[0] > last], "nối", lq
        s = json.dumps(enc(sym, b), separators=(",", ":"))
        try: changed = open(fn).read() != s
        except Exception: changed = True
        if changed: open(fn, "w").write(s)
        return sym, [], "ghi mới" if not H else "điều chỉnh", lq
    st = {}
    newR = {}; LQ = {}
    with ThreadPoolExecutor(6) as ex:
        for sym, rec, how, lq in ex.map(work, mine):
            st[how] = st.get(how, 0) + 1; LQ[sym] = lq
            if rec is None:
                if sym in R: newR[sym] = R[sym]
                continue
            if rec: newR[sym] = rec
    now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
    def put(fn, key, val):  # chỉ ghi khi nội dung đổi, tránh commit thừa
        try:
            if json.load(open(D + fn)).get(key) == val: return
        except Exception: pass
        json.dump({"updated": now.strftime("%H:%M %d/%m/%Y"), key: val}, open(D + fn, "w"), ensure_ascii=False, separators=(",", ":"))
    put("recent.json", "b", newR)
    have = set(x[:-5] for x in os.listdir(D) if x.endswith(".json") and x[:-5] == x[:-5].upper() and not x.startswith("_"))
    S = [[k, "I", v, 1 if k in have else 0, 10000] for k, v in IDX.items()]
    S += [[c, f, ten(n), 1 if c in have else 0, LQ.get(c, 0)] for c, f, n, t in sorted(rows)]
    put("syms.json", "s", S)
    print("ok", len(mine), st, "danh sách", len(S))

if __name__ == "__main__":
    main()
