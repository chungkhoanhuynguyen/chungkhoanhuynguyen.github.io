# Tự động: chỉ báo vĩ mô thế giới/trong nước và mức độ ảnh hưởng tới kinh tế, chứng khoán Việt Nam.
import json, time, datetime, urllib.request, os, re
UA = {"User-Agent": "Mozilla/5.0"}

def get(url, raw=False):
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                b = r.read(); return b.decode("utf-8", "ignore") if raw else json.loads(b)
        except Exception as e:
            err = e; time.sleep(3)
    print("loi", url[:70], err); return None

def yahoo(sym):
    j = get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=3mo&interval=1d")
    try:
        r = j["chart"]["result"][0]; c = [x for x in r["indicators"]["quote"][0]["close"] if x is not None]
        return c if len(c) > 25 else None
    except Exception: return None

def vnd(sym):
    to = int(time.time()); j = get(f"https://dchart-api.vndirect.com.vn/dchart/history?resolution=D&symbol={sym}&from={to-120*86400}&to={to}")
    return j["c"] if j and j.get("c") else None

def ch(c, n): return (c[-1] / c[-1 - n] - 1) * 100 if c and len(c) > n else None
def f1(v, d=1): return ("+" if v >= 0 else "−") + f"{abs(v):.{d}f}".replace(".", ",")
def a1(v): return f"{abs(v):.1f}".replace(".", ",")
def num(v, d=2): return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")

items = []
def add(key, name, val, unit, d1, m1, level, eff, msg, win, lose):
    items.append(dict(k=key, name=name, val=val, unit=unit, d1=d1, m1=m1, level=level, eff=eff, msg=msg, win=win, lose=lose))

def lvl(a, hi, mid): return "Cao" if abs(a) >= hi else "Trung bình" if abs(a) >= mid else "Thấp"

# 1. Tỷ giá USD/VND
fx = yahoo("VND=X"); vcb = None
x = get("https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx", raw=True)
if x:
    m = re.search(r'CurrencyCode="USD"[^>]*Sell="([\d,\.]+)"', x)
    if m: vcb = float(m.group(1).replace(",", ""))
if fx:
    m1, d1 = ch(fx, 21), ch(fx, 1)
    val = vcb or fx[-1]
    if m1 >= 0.4:
        add("fx", "Tỷ giá USD/VND", num(val, 0), "đồng (giá bán ngân hàng)", d1, m1, lvl(m1, 1.0, 0.4), "neg",
            f"Đồng USD tăng {a1(m1)}% so với tiền đồng trong 1 tháng. Áp lực tỷ giá dễ khiến khối ngoại bán ròng và NHNN phải hút tiền, đẩy lãi suất liên ngân hàng lên.",
            "Xuất khẩu: dệt may, thủy sản, gỗ", "Doanh nghiệp vay nợ USD, nhập khẩu nguyên liệu, hàng không")
    elif m1 <= -0.4:
        add("fx", "Tỷ giá USD/VND", num(val, 0), "đồng (giá bán ngân hàng)", d1, m1, lvl(m1, 1.0, 0.4), "pos",
            f"Tiền đồng lên giá {a1(m1)}% so với USD trong 1 tháng, giảm áp lực tỷ giá và tạo dư địa giữ lãi suất thấp.",
            "Doanh nghiệp nợ USD, nhập khẩu, hàng không; dòng vốn ngoại", "Biên lợi nhuận xuất khẩu")
    else:
        add("fx", "Tỷ giá USD/VND", num(val, 0), "đồng (giá bán ngân hàng)", d1, m1, "Thấp", "mid",
            "Tỷ giá ổn định trong 1 tháng, chưa tạo áp lực lớn lên lãi suất và dòng vốn ngoại.", "", "")

# 2. Dầu Brent
c = yahoo("BZ=F")
if c:
    m1, d1 = ch(c, 21), ch(c, 1); L = lvl(m1, 10, 4)
    if m1 >= 4:
        add("oil", "Giá dầu Brent", num(c[-1]), "USD/thùng", d1, m1, L, "mid",
            f"Dầu tăng {a1(m1)}% trong 1 tháng: tốt cho nhóm dầu khí nhưng làm tăng chi phí vận tải và áp lực lạm phát trong nước.",
            "Dầu khí: BSR, PVS, PVD, GAS, PVT", "Hàng không VJC, HVN; vận tải; nhựa, phân bón dùng nguyên liệu dầu")
    elif m1 <= -4:
        add("oil", "Giá dầu Brent", num(c[-1]), "USD/thùng", d1, m1, L, "mid",
            f"Dầu giảm {a1(m1)}% trong 1 tháng: hạ chi phí đầu vào và lạm phát, nhưng bất lợi cho doanh nghiệp dầu khí.",
            "Hàng không VJC, HVN; vận tải; nhựa BMP", "Dầu khí: BSR, PVS, PVD, GAS, PLX (tồn kho)")
    else:
        add("oil", "Giá dầu Brent", num(c[-1]), "USD/thùng", d1, m1, "Thấp", "mid", "Giá dầu đi ngang trong 1 tháng, ảnh hưởng tới lạm phát và nhóm dầu khí ở mức thấp.", "", "")

# 3. Vàng thế giới
c = yahoo("GC=F")
if c:
    m1, d1 = ch(c, 21), ch(c, 1); L = lvl(m1, 8, 3)
    if m1 >= 3:
        add("gold", "Vàng thế giới", num(c[-1], 0), "USD/ounce", d1, m1, L, "neg",
            f"Vàng tăng {a1(m1)}% trong 1 tháng: dòng tiền trú ẩn hút bớt tiền khỏi chứng khoán, chênh lệch vàng trong nước dễ nới rộng.",
            "Doanh nghiệp vàng bạc (doanh thu)", "Dòng tiền vào chứng khoán; tỷ giá tự do")
    elif m1 <= -3:
        add("gold", "Vàng thế giới", num(c[-1], 0), "USD/ounce", d1, m1, L, "pos",
            f"Vàng giảm {a1(m1)}% trong 1 tháng: người mua vàng ngắn hạn thua lỗ, tiền có thể quay lại kênh chứng khoán, gửi tiết kiệm.",
            "Dòng tiền vào chứng khoán", "Người mua vàng ngắn hạn; biên lợi nhuận bán lẻ vàng khi giá giảm nhanh")
    else:
        add("gold", "Vàng thế giới", num(c[-1], 0), "USD/ounce", d1, m1, "Thấp", "mid", "Giá vàng đi ngang, chưa tác động đáng kể tới dòng tiền trong nước.", "", "")

# 4. Chỉ số USD (DXY)
c = yahoo("DX-Y.NYB")
if c:
    m1, d1 = ch(c, 21), ch(c, 1); L = lvl(m1, 2.5, 1)
    eff = "neg" if m1 >= 1 else "pos" if m1 <= -1 else "mid"
    msg = (f"USD mạnh lên {a1(m1)}% so với rổ tiền tệ: các thị trường mới nổi như Việt Nam chịu áp lực tỷ giá và vốn ngoại rút ra." if eff == "neg" else
           f"USD yếu đi {a1(m1)}%: giảm áp lực tỷ giá, thuận lợi cho dòng vốn quay lại thị trường mới nổi." if eff == "pos" else
           "Chỉ số USD đi ngang, áp lực tỷ giá từ bên ngoài ở mức thấp.")
    add("dxy", "Chỉ số USD (DXY)", num(c[-1]), "điểm", d1, m1, L, eff, msg, "", "")

# 5. Lợi suất trái phiếu Mỹ 10 năm
c = yahoo("^TNX")
if c and len(c) > 21:
    bp = (c[-1] - c[-22]) * 100; d1 = (c[-1] - c[-2]) * 100
    L = "Cao" if abs(bp) >= 40 else "Trung bình" if abs(bp) >= 15 else "Thấp"
    eff = "neg" if bp >= 15 else "pos" if bp <= -15 else "mid"
    msg = (f"Lợi suất Mỹ 10 năm tăng {bp:.0f} điểm cơ bản trong 1 tháng: tiền rẻ toàn cầu ít đi, bất lợi cho định giá cổ phiếu và dòng vốn ngoại." if eff == "neg" else
           f"Lợi suất Mỹ 10 năm giảm {abs(bp):.0f} điểm cơ bản: điều kiện tiền tệ toàn cầu nới lỏng, hỗ trợ thị trường mới nổi." if eff == "pos" else
           "Lợi suất Mỹ ổn định, tác động lên dòng vốn ở mức thấp.")
    items.append(dict(k="us10", name="Lợi suất TPCP Mỹ 10 năm", val=num(c[-1]), unit="%", d1=None, m1=None, bp=round(bp), level=L, eff=eff, msg=msg, win="", lose=""))

# 6. VN-Index (tham chiếu)
c = vnd("VNINDEX")
vn = dict(val=num(c[-1]), d1=ch(c, 1), m1=ch(c, 21)) if c else None

score = sum({"pos": 1, "neg": -1}.get(i["eff"], 0) * {"Cao": 2, "Trung bình": 1, "Thấp": 0}[i["level"]] for i in items)
tone = "pos" if score >= 2 else "neg" if score <= -2 else "mid"
os.makedirs("data", exist_ok=True)
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
json.dump(dict(updated=now.strftime("%H:%M %d/%m/%Y"), tone=tone, score=score, vn=vn, items=items), open("data/vimo.json", "w"), ensure_ascii=False)
print("ok", len(items), tone, score)
