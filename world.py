# Thị trường thế giới và lãi suất Fed cho web:
#  - data/wm.bin  : giá đóng cửa ngày 3 năm của vàng, dầu Brent, dầu WTI, chứng khoán Mỹ, Nhật, Hàn, DXY, lợi suất Mỹ 10 năm
#  - data/mac.bin : lãi suất Fed (quyết định gần nhất, lịch sử, cuộc họp tới), tin vĩ mô tự tạo từ số liệu, lịch họp Fed
# Tin vĩ mô được viết lại từ số liệu chính thức (thông cáo FOMC, giá đóng cửa), không chép bài báo, không gắn link ra ngoài.
import json, time, datetime, urllib.request, urllib.parse, re, html, base64
from zoneinfo import ZoneInfo
import hncodec

_h = lambda s: base64.b64decode(s).decode()
Q1 = _h("aHR0cHM6Ly9xdWVyeTEuZmluYW5jZS55YWhvby5jb20vdjgvZmluYW5jZS9jaGFydC8=")
FR = _h("aHR0cHM6Ly93d3cuZmVkZXJhbHJlc2VydmUuZ292Lw==")
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}
VN, NY = ZoneInfo("Asia/Ho_Chi_Minh"), ZoneInfo("America/New_York")
now = datetime.datetime.now(VN)
today = now.date()
STAMP = now.strftime("%H:%M %d/%m/%Y")
EPOCH = datetime.date(1970, 1, 1)


def get(url, raw=False, tries=3):
    err = None
    for k in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                b = r.read()
                return b.decode("utf-8", "ignore") if raw else json.loads(b)
        except Exception as e:
            err = e; time.sleep(2 + 2 * k)
    print("lỗi", url[:70], err)
    return None


def num(v, d=2):
    s = f"{abs(v):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" if v < 0 else "") + s


def pct(v, d=2):
    return ("+" if v >= 0 else "−") + f"{abs(v):.{d}f}".replace(".", ",") + "%"


def dmy(d): return d.strftime("%d/%m/%Y")
def dm(d): return d.strftime("%d/%m")


def put(path, obj):
    """Chỉ ghi khi nội dung đổi (bỏ qua giờ cập nhật)."""
    old = hncodec.load(path, {}) or {}
    if {k: v for k, v in old.items() if k != "updated"} == obj:
        return False
    return hncodec.dump(dict(updated=STAMP, **obj), path)


# ---------- 1) Giá thế giới ----------
# khoá, tên, đơn vị, số lẻ, nhóm, mã nguồn, giờ đóng cửa (giờ địa phương), múi giờ
SER = [
    ("gold", "Vàng thế giới", "USD/ounce", 1, "hh", "GC=F"),
    ("brent", "Dầu Brent", "USD/thùng", 2, "hh", "BZ=F"),
    ("wti", "Dầu WTI", "USD/thùng", 2, "hh", "CL=F"),
    ("spx", "S&P 500", "điểm", 2, "my", "^GSPC"),
    ("dji", "Dow Jones", "điểm", 2, "my", "^DJI"),
    ("ixic", "Nasdaq", "điểm", 2, "my", "^IXIC"),
    ("n225", "Nikkei 225", "điểm", 2, "a", "^N225"),
    ("kospi", "KOSPI", "điểm", 2, "a", "^KS11"),
    ("dxy", "DXY (chỉ số USD)", "điểm", 2, "ls", "DX-Y.NYB"),
    ("us10", "TP Mỹ 10 năm (lợi suất)", "%", 3, "ls", "^TNX"),
]


def series(sym):
    j = get(f"{Q1}{urllib.parse.quote(sym)}?range=3y&interval=1d")
    try:
        r = j["chart"]["result"][0]
        m, ts, cl = r["meta"], r["timestamp"], r["indicators"]["quote"][0]["close"]
    except Exception:
        return None
    off = m.get("gmtoffset", 0)
    pts = {}
    for t, c in zip(ts, cl):
        if c is None:
            continue
        d = datetime.datetime.fromtimestamp(t + off, datetime.timezone.utc).date()
        pts[d] = c
    # phiên mới nhất: nếu nến cuối chưa có giá đóng cửa thì dùng giá khớp gần nhất
    p, t = m.get("regularMarketPrice"), m.get("regularMarketTime")
    if p and t:
        d = datetime.datetime.fromtimestamp(t + off, datetime.timezone.utc).date()
        if not pts or d >= max(pts):
            pts[d] = p
    ks = sorted(pts)
    return ks, [pts[k] for k in ks]


S = []
data = {}
for key, name, unit, dec, grp, sym in SER:
    x = series(sym)
    time.sleep(0.4)
    if not x or len(x[0]) < 120:
        print("bỏ qua", key)
        continue
    ks, cs = x
    data[key] = (ks, cs, name, unit, dec)
    S.append([key, name, unit, dec, grp, [(k - EPOCH).days for k in ks], [round(c, dec) for c in cs]])
fxs = series("VND=X")
fx = round(fxs[1][-1]) if fxs else None
if S:
    put("data/wm.bin", {"s": S, "fx": fx})
else:
    print("không có dữ liệu giá thế giới, giữ file cũ")


# ---------- 2) Lãi suất Fed ----------
def frac(s):
    s = s.strip()
    if "-" in s and "/" in s:          # 3-3/4
        a, b = s.split("-", 1)
        n, d = b.split("/")
        return int(a) + int(n) / int(d)
    if "/" in s:                        # 1/4
        n, d = s.split("/")
        return int(n) / int(d)
    return float(s)


def clean(t):
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = t.replace("‑", "-").replace("‐", "-").replace("–", "-").replace("—", "-").replace("\xa0", " ")
    return re.sub(r"\s+", " ", t)


ACT = {"maintain": "hold", "raise": "hike", "lower": "cut"}


def statement(url):
    t = get(url, raw=True)
    if not t:
        return None
    t = clean(t)
    m = re.search(r"decided to (maintain|raise|lower) the target range for the federal funds rate"
                  r"(?: by ([0-9/\- ]+?) percentage points?)? (?:at|to) ([0-9][0-9/\-]*) to ([0-9][0-9/\-]*) percent", t)
    if not m:
        return None
    out = dict(act=ACT[m.group(1)], bps=round(frac(m.group(2)) * 100) if m.group(2) else 0,
               lo=frac(m.group(3)), hi=frac(m.group(4)))
    v = re.search(r"by an? (\d+)\s*-\s*(\d+) vote", t)
    if v:
        out["vote"] = [int(v.group(1)), int(v.group(2))]
    p = re.findall(r"preferred (?:to (raise|lower|maintain)(?:[^.]*? by ([0-9/\- ]+?) percentage points?)?|no change)", t)
    if p:
        prefs = {(ACT.get(a, "hold") if a else "hold", round(frac(b) * 100) if b else 0) for a, b in p}
        if len(prefs) == 1:
            out["diss"] = list(prefs)[0]
    return out


def feed():
    x = get(FR + "feeds/press_monetary.xml", raw=True)
    if not x:
        return []
    out = []
    for it in re.findall(r"<item>(.*?)</item>", x, re.S):
        g = lambda tag: re.sub(r"<!\[CDATA\[|\]\]>", "", (re.search(rf"<{tag}>(.*?)</{tag}>", it, re.S) or [None, ""])[1]).strip()
        if "FOMC statement" not in g("title"):
            continue
        try:
            dt = datetime.datetime.strptime(g("pubDate"), "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=datetime.timezone.utc)
        except Exception:
            continue
        out.append((dt.astimezone(VN), g("link")))
    return out


MONTHS = {m: i + 1 for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August",
                                          "September", "October", "November", "December"])}


def openmarket():
    """Lịch sử thay đổi biên độ lãi suất (ngày hiệu lực, trên, dưới)."""
    t = get(FR + "monetarypolicy/openmarket.htm", raw=True)
    if not t:
        return []
    rows = []
    heads = [(m.start(), int(m.group(1))) for m in re.finditer(r"<h4[^>]*>\s*(\d{4})\s*</h4>", t)]
    for i, (pos, yr) in enumerate(heads):
        if yr < 2019:
            break
        end = heads[i + 1][0] if i + 1 < len(heads) else len(t)
        for r in re.findall(r"<tr[^>]*>(.*?)</tr>", t[pos:end], re.S):
            c = [clean(x).strip() for x in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)]
            if len(c) < 4:
                continue
            m = re.match(r"([A-Za-z]+) (\d+)", c[0]); lv = re.match(r"([\d.]+)\s*-\s*([\d.]+)", c[3])
            if not m or not lv or m.group(1) not in MONTHS:
                continue
            try:
                d = datetime.date(yr, MONTHS[m.group(1)], int(m.group(2)))
            except ValueError:
                continue
            rows.append([d, float(lv.group(1)), float(lv.group(2)), int(c[1] or 0), int(c[2] or 0)])
    return sorted(rows)


def calendar():
    """Các cuộc họp FOMC: (ngày 1, ngày 2, có dự báo kinh tế)."""
    t = get(FR + "monetarypolicy/fomccalendars.htm", raw=True)
    if not t:
        return []
    heads = [(m.start(), int(m.group(1))) for m in re.finditer(r"(\d{4}) FOMC Meetings", t)]
    out = []
    for i, (pos, yr) in enumerate(heads):
        nxt = [p for p, _ in heads if p > pos]
        seg = t[pos:min(nxt) if nxt else len(t)]
        for mo, dd in re.findall(r"fomc-meeting__month[^>]*>(.*?)</div>.*?fomc-meeting__date[^>]*>(.*?)</div>", seg, re.S):
            mo, dd = clean(mo).strip(), clean(dd).strip()
            if "notation" in dd or "unscheduled" in dd.lower():
                continue
            sep = "*" in dd
            dd = dd.replace("*", "").strip()
            mm = mo.split("/")
            m2 = re.match(r"(\d+)\s*-\s*(\d+)", dd)
            if not m2 or mm[0] not in MONTHS or (len(mm) > 1 and mm[1][:3] not in [k[:3] for k in MONTHS]):
                continue
            a, b = int(m2.group(1)), int(m2.group(2))
            m1 = MONTHS[mm[0]]
            mb = m1 if len(mm) == 1 else [v for k, v in MONTHS.items() if k[:3] == mm[1][:3]][0]
            try:
                out.append((datetime.date(yr, m1, a), datetime.date(yr if mb >= m1 else yr + 1, mb, b), sep))
            except ValueError:
                pass
    return sorted(set(out))


def ann(d2):
    """Giờ công bố quyết định (14:00 New York) quy ra giờ Việt Nam."""
    return datetime.datetime(d2.year, d2.month, d2.day, 14, 0, tzinfo=NY).astimezone(VN)


def rng(lo, hi): return f"{num(lo, 2)}–{num(hi, 2)}%"


def bp(b): return num(b / 100, 2).rstrip("0").rstrip(",") + " điểm %"


ACTV = {"hold": "giữ nguyên", "hike": "tăng", "cut": "giảm"}


def title(s):
    r = rng(s["lo"], s["hi"])
    if s["act"] == "hold":
        t = f"Fed giữ nguyên lãi suất điều hành ở {r}"
    elif s["act"] == "hike":
        t = f"Fed tăng lãi suất {bp(s['bps'])} lên {r}"
    else:
        t = f"Fed giảm lãi suất {bp(s['bps'])} về {r}"
    v = s.get("vote")
    if v:
        t += f" (biểu quyết {v[0]}–{v[1]}"
        if v[1] and s.get("diss"):
            a, b = s["diss"]
            t += f", {v[1]} thành viên muốn {ACTV[a]}" + (f" {bp(b)}" if b else "")
        t += ")"
    return t


fed, news, evs = {}, [], []
stm = []
for dt, link in feed()[:6]:
    s = statement(link)
    time.sleep(0.4)
    if s:
        stm.append((dt, s))
stm.sort(key=lambda x: x[0])
om = openmarket()
cal = calendar()
nexts = [c for c in cal if ann(c[1]) > now]
if stm:
    dt, s = stm[-1]
    fed = dict(lo=s["lo"], hi=s["hi"], act=s["act"], bps=s["bps"], d=dt.strftime("%Y-%m-%d"), t=dt.strftime("%H:%M"),
               vote=s.get("vote"), ttl=title(s))
elif om:
    fed = dict(lo=om[-1][1], hi=om[-1][2], act="", bps=0, d=om[-1][0].isoformat(), t="", vote=None, ttl="")
if fed:
    if om:
        last = om[-1]
        fed["chg"] = dict(d=last[0].isoformat(), act="hike" if last[3] else "cut", bps=last[3] or last[4])
        # thông cáo mới có thể chưa kịp vào bảng lịch sử
        if stm and stm[-1][1]["act"] != "hold" and (stm[-1][1]["lo"], stm[-1][1]["hi"]) != (last[1], last[2]):
            d = stm[-1][0].date() + datetime.timedelta(days=1)
            om.append([d, stm[-1][1]["lo"], stm[-1][1]["hi"], 0, 0])
            fed["chg"] = dict(d=d.isoformat(), act=stm[-1][1]["act"], bps=stm[-1][1]["bps"])
    since = today - datetime.timedelta(days=3 * 366)
    h = [r for r in om if r[0] >= since]
    before = [r for r in om if r[0] < since]
    if before:
        h = [[since] + before[-1][1:]] + h
    fed["hist"] = [[(r[0] - EPOCH).days, r[1], r[2]] for r in h]
    if nexts:
        n1 = nexts[0]
        fed["next"] = dict(d1=n1[0].isoformat(), d2=n1[1].isoformat(), sep=n1[2], ann=ann(n1[1]).strftime("%Y-%m-%d %H:%M"))


def meet_txt(c):
    a, b = c[0], c[1]
    return (f"{a.day}–{b.day}/{b.month}/{b.year}" if a.month == b.month else f"{dm(a)}–{dm(b)}/{b.year}")


# Tin Fed (30 ngày gần nhất)
for dt, s in stm:
    if (today - dt.date()).days > 30:
        continue
    t = title(s)
    nx = [c for c in cal if c[0] > dt.date()]
    if nx:
        t += f". Cuộc họp tiếp theo {meet_txt(nx[0])}"
    news.append(["fed" + dt.strftime("%Y%m%d"), dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M"), "Fed", "vm", t, ""])

# Lịch họp Fed: 10 ngày trước tới 120 ngày tới
smap = {dt.astimezone(NY).date(): s for dt, s in stm}
for c in cal:
    a = ann(c[1])
    dd = (a.date() - today).days
    if dd < -10 or dd > 120:
        continue
    note = f"Họp FOMC {meet_txt(c)}" + (", kèm dự báo kinh tế" if c[2] else "")
    s = smap.get(c[1])
    if s:
        note = f"{ACTV[s['act']].capitalize()}" + (f" {bp(s['bps'])}" if s["bps"] else "") + f", biên độ {rng(s['lo'], s['hi'])}. " + note
    evs.append(["Fed", "vm", "Fed công bố lãi suất", note, f"Khoảng {a.strftime('%H:%M')}", a.date().isoformat(), "", ""])


# Tin phiên giao dịch thế giới (7 ngày gần nhất), viết từ giá đóng cửa
def close_vn(d, h, m, tz):
    return datetime.datetime(d.year, d.month, d.day, h, m, tzinfo=tz).astimezone(VN)


def moves(keys, d):
    out = []
    for k in keys:
        if k not in data:
            continue
        ks, cs, name, unit, dec = data[k]
        if d in ks:
            i = ks.index(d)
            if i > 0:
                out.append((k, name, unit, dec, cs[i], (cs[i] / cs[i - 1] - 1) * 100))
    return out


GRP = [("my", ["spx", "dji", "ixic"], "Chứng khoán Mỹ", "Mỹ", (16, 0, NY)),
       ("a", ["n225", "kospi"], "Chứng khoán Nhật, Hàn", "Châu Á", (15, 30, ZoneInfo("Asia/Tokyo"))),
       ("hh", ["gold", "brent", "wti"], "Vàng và dầu", "Hàng hoá", (16, 0, NY))]
for g, keys, lab, tag, (hh, mi, tz) in GRP:
    days = sorted({d for k in keys if k in data for d in data[k][0] if (today - d).days <= 7})
    for d in days:
        mv = moves(keys, d)
        if not mv:
            continue
        parts = []
        for i, (k, name, unit, dec, c, p) in enumerate(mv):
            val = num(c, 1 if k in ("gold",) else 2) + (" " + unit if unit != "điểm" else " điểm")
            nm = {"gold": "vàng", "brent": "Brent", "wti": "WTI"}.get(k, name)
            parts.append(f"{nm} {pct(p)} ({val})" if i == 0 or k in ("brent",) else f"{nm} {pct(p)}")
        vn = close_vn(d, hh, mi, tz)
        news.append([f"{g}{d:%Y%m%d}", vn.strftime("%Y-%m-%d"), vn.strftime("%H:%M"), tag, "vm",
                     f"{lab} phiên {dm(d)}: " + ", ".join(parts), ""])

news.sort(key=lambda x: (x[1], x[2]), reverse=True)
if fed or news or evs:
    put("data/mac.bin", {"fed": fed, "n": news, "e": evs})
print("world:", len(S), "chuỗi giá; fed", fed.get("ttl"), "; tin", len(news), "; lịch", len(evs))
