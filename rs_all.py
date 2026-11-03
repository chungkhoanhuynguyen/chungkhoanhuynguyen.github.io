"""RS = Sức mạnh giá (SMG) theo đúng công thức WiData, xếp hạng trên TOÀN thị trường (HOSE+HNX+UPCoM).
smg = 0.4*%(giá/EMA20) + 0.3*%(giá/EMA60) + 0.3*%(giá/EMA120); điểm = (1 - thứ hạng/tổng số mã)*100.
Chạy 1 lần/ngày sau phiên trên GitHub (miễn phí), ghi data/rs_wi.bin để update.py dùng."""
import datetime, time, json, urllib.request, base64
from concurrent.futures import ThreadPoolExecutor
import hncodec
_h = lambda s: base64.b64decode(s).decode()
_S1 = _h("aHR0cHM6Ly9kY2hhcnQtYXBpLnZuZGlyZWN0LmNvbS52bi9kY2hhcnQvaGlzdG9yeQ==")
UA = {"User-Agent": "Mozilla/5.0"}
def closes(s):
    to = int(time.time()); fr = to - 420*86400
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"{_S1}?resolution=D&symbol={s}&from={fr}&to={to}", headers=UA), timeout=20) as r:
                j = json.load(r)
            return s, j.get("t") or [], j.get("c") or [], j.get("v") or []
        except Exception:
            time.sleep(1 + k)
    return s, [], [], []
def ema(c, n):
    a = 2/(n+1); e = c[0]
    for x in c[1:]: e = a*x + (1-a)*e
    return e
def smg(c):
    x = c[-1]
    return 0.4*100*(x/ema(c, 20)-1) + 0.3*100*(x/ema(c, 60)-1) + 0.3*100*(x/ema(c, 120)-1)
syms = [r[0] for r in hncodec.load("data/c/syms.bin")["s"] if r[1] in ("H", "X", "U") and len(r[0]) == 3]
with ThreadPoolExecutor(8) as ex: res = list(ex.map(closes, syms))
last = max((t[-1] for _, t, c, v in res if t), default=0)
# Chỉ xếp hạng mã còn giao dịch (giá có thay đổi trong 5 phiên) — khớp cách WiData (lệch TB ~1,3 điểm)
raw = {s: smg(c) for s, t, c, v in res if len(c) >= 20 and t[-1] >= last - 10*86400 and len(set(c[-5:])) > 1}
val = {s: sum(c[i]*(v[i] if i < len(v) else 0) for i in range(-20, 0))/20*1000/1e9 for s, t, c, v in res if len(c) >= 20}
od = sorted(raw, key=lambda s: -raw[s]); Y = len(od)
sc = {s: round((1 - (i+1)/Y)*100, 4) for i, s in enumerate(od)}
ngay = datetime.datetime.fromtimestamp(last + 7*3600, datetime.timezone.utc).strftime("%Y-%m-%d")
hncodec.dump(dict(ngay=ngay, nguon="SMG tự tính (công thức WiData)", tong=Y, smg=sc, ung=sorted(x for x in sc if sc[x] >= 85 and val.get(x, 0) >= 10)), "data/rs_wi.bin")
print("ok", ngay, Y)
