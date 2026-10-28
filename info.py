# Thông tin doanh nghiệp cho web:
#  - data/ev.bin   : lịch sự kiện (cổ tức, ĐHCĐ, phát hành, niêm yết, cảnh báo) từ 10 ngày trước tới 75 ngày tới
#  - data/news.bin : tin công bố thông tin chính thức của doanh nghiệp (Sở GDCK) 7 ngày gần nhất
#  - data/fund.bin : chỉ số định giá, hiệu quả (P/E, P/B, ROE...) để so sánh mã
# Chỉ lấy văn bản chính thức của Sở; không chép bài báo. Ghi dạng .bin (hncodec).
import json, time, datetime, urllib.request, os, base64, re
from concurrent.futures import ThreadPoolExecutor
import hncodec
_h = lambda s: base64.b64decode(s).decode()
S2 = _h("aHR0cHM6Ly9hcGktZmluZm8udm5kaXJlY3QuY29tLnZuL3Y0Lw==")
UA = {"User-Agent": "Mozilla/5.0"}
now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
today = now.date()
STAMP = now.strftime("%H:%M %d/%m/%Y")


def get(url):
    err = None
    for k in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.load(r)
        except Exception as e:
            err = e; time.sleep(2 + k)
    print("lỗi", url[:60], err)
    return None


def put(path, key, val):
    """Chỉ ghi khi nội dung đổi (bỏ qua giờ cập nhật)."""
    if (hncodec.load(path, {}) or {}).get(key) == val:
        return False
    return hncodec.dump({"updated": STAMP, key: val}, path)


def stock(code):
    return bool(re.fullmatch(r"[A-Z0-9]{3}", code or ""))


# ---------- 1) Lịch sự kiện ----------
EV = {  # loại: (nhóm lọc, nhãn, nhãn ngày 1, nhãn ngày 2, trường ngày 2)
    "DIVIDEND": ("tien", "Cổ tức tiền", "GDKHQ", "Thanh toán", "actualDate"),
    "STOCKDIV": ("cp", "Cổ tức cổ phiếu", "GDKHQ", "", ""),
    "KINDDIV": ("cp", "Cổ phiếu thưởng", "GDKHQ", "", ""),
    "meetingRight": ("dhcd", "Chốt quyền ĐHCĐ", "GDKHQ", "Ngày họp", "actualDate"),
    "MEETING": ("dhcd", "Họp ĐHCĐ", "Ngày họp", "", ""),
    "POLL": ("dhcd", "Lấy ý kiến cổ đông", "GDKHQ", "", ""),
    "ISSUE": ("ph", "Phát hành thêm", "GDKHQ", "Hạn đăng ký mua", "registerEndDate"),
    "LISTED": ("ph", "Giao dịch bổ sung", "Ngày GD", "", ""),
    "nomargin": ("cb", "Không được ký quỹ", "Hiệu lực", "", ""),
    "control": ("cb", "Bị kiểm soát", "Hiệu lực", "", ""),
    "alert": ("cb", "Bị cảnh báo", "Hiệu lực", "", ""),
    "halt": ("cb", "Hạn chế giao dịch", "Hiệu lực", "", ""),
    "suspend": ("cb", "Tạm ngừng giao dịch", "Hiệu lực", "", ""),
    "noticed": ("cb", "Diện chú ý", "Hiệu lực", "", ""),
}


def ev_type(t):
    if t in EV:
        return EV[t]
    if t.startswith("listed"):
        return ("ph", "Niêm yết mới", "Ngày niêm yết", "", "")
    if t.startswith("delisted"):
        return ("cb", "Hủy niêm yết", "Hiệu lực", "", "")
    if t.startswith("lastTrade"):
        return ("cb", "Ngày GD cuối cùng", "Ngày", "", "")
    return None


def events():
    a = (today - datetime.timedelta(days=10)).isoformat(); b = (today + datetime.timedelta(days=75)).isoformat()
    j = get(f"{S2}events?q=locale:VN~effectiveDate:gte:{a}~effectiveDate:lte:{b}&sort=effectiveDate:asc&size=4000")
    if not j:
        return None
    out, seen = [], set()
    for x in j.get("data", []):
        code = x.get("code"); t = ev_type(x.get("type") or "")
        d1 = x.get("effectiveDate")
        if not t or not stock(code) or not d1:
            continue
        key = (code, x.get("type"), d1)
        if key in seen:
            continue
        seen.add(key)
        grp, lab, l1, l2, f2 = t
        d2 = x.get(f2) if f2 else None
        note = re.sub(r"\s+", " ", (x.get("note") or "")).strip()
        if x.get("type") == "ISSUE" and x.get("price"):
            note = note or "Giá phát hành %s đ/cp" % format(int(x["price"]), ",").replace(",", ".")
        out.append([code, grp, lab, note[:140], l1, d1, l2 if d2 and d2 != d1 else "", d2 if d2 and d2 != d1 else ""])
    return out


# ---------- 2) Tin công bố thông tin ----------
NT = {"financialstatement": "bctc", "dividend": "quyen", "issue": "quyen", "other_rights": "quyen",
      "meeting": "dhcd", "resolutions": "dhcd", "personnel": "ns",
      "investor_transaction": "nb", "investor_trans_register": "nb"}
OK_HOST = re.compile(r"^https?://([a-z0-9-]+\.)*(hsx\.vn|hnx\.vn)/", re.I)


def news():
    a = (today - datetime.timedelta(days=7)).isoformat()
    out, page = [], 1
    while page <= 6:
        j = get(f"{S2}news?q=newsGroup:disclosure,rights_disclosure~locale:VN~newsDate:gte:{a}&sort=newsDate:desc"
                f"&size=1000&page={page}&fields=newsId,newsDate,newsTime,newsType,newsSource,tagCodes,newsTitle,newsUrl,attachments")
        if not j:
            break
        d = j.get("data", [])
        for x in d:
            if x.get("newsType") in ("etf", "bond") or x.get("newsSource") not in ("HOSE", "HNX", "UPCOM"):
                continue
            codes = [c for c in (x.get("tagCodes") or "").split(",") if stock(c)]
            if not codes:
                continue
            code = codes[0]
            title = re.sub(r"\s+", " ", x.get("newsTitle") or "").strip()
            title = re.sub(r"^%s\s*:\s*" % code, "", title)
            url = x.get("newsUrl") or ""
            if not OK_HOST.match(url):
                url = next((a.get("sourceUrl") for a in (x.get("attachments") or []) if OK_HOST.match(a.get("sourceUrl") or "")), "")
            out.append([str(x.get("newsId")), x.get("newsDate"), (x.get("newsTime") or "")[:5], code, NT.get(x.get("newsType"), "khac"), title[:220], url])
        if len(d) < 1000:
            break
        page += 1
    out.sort(key=lambda r: (r[1], r[2]), reverse=True)
    return out


# ---------- 3) Chỉ số so sánh ----------
F = [("MARKETCAP", "mc", 1e-9, 0), ("PRICE_TO_EARNINGS", "pe", 1, 2), ("PRICE_TO_BOOK", "pb", 1, 2), ("PRICE_TO_SALES", "ps", 1, 2),
     ("ROAE_TR_AVG5Q", "roe", 100, 1), ("ROAA_TR_AVG5Q", "roa", 100, 1), ("EPS_TR", "eps", 1, 0), ("BVPS_CR", "bvps", 1, 0),
     ("DIVIDEND_YIELD", "dy", 100, 2), ("BETA", "beta", 1, 2), ("FOREIGN_OWNERSHIP", "fo", 100, 1), ("FREEFLOAT", "ff", 100, 0),
     ("PRICE_HIGHEST_CR_52W", "h52", 1e-3, 2), ("PRICE_LOWEST_CR_52W", "l52", 1e-3, 2), ("NMVOLUME_AVG_CR_10D", "v10", 1, 0)]


def fund(codes):
    keys = [f[1] for f in F]; M = {f[0]: (i, f[2], f[3]) for i, f in enumerate(F)}
    flt = ",".join(f[0] for f in F)
    chunks = [codes[i:i + 60] for i in range(0, len(codes), 60)]
    def one(ch):
        return get(f"{S2}ratios/latest?filter=ratioCode:{flt}&where=code:{','.join(ch)}&order=reportDate&fields=code,ratioCode,value")
    D = {}
    with ThreadPoolExecutor(4) as ex:
        for j in ex.map(one, chunks):
            for x in (j or {}).get("data", []):
                i, k, nd = M.get(x.get("ratioCode"), (None, 0, 0))
                v = x.get("value")
                if i is None or not isinstance(v, (int, float)):
                    continue
                row = D.setdefault(x["code"], [None] * len(F))
                row[i] = round(v * k, nd) if nd else int(round(v * k))
    D = {c: r for c, r in D.items() if any(v is not None for v in r)}
    return {"f": keys, "d": D}


def main():
    os.makedirs("data", exist_ok=True)
    ev = events()
    if ev is not None:
        print("sự kiện", len(ev), put("data/ev.bin", "e", ev))
    nw = news()
    if nw:
        print("tin", len(nw), put("data/news.bin", "n", nw))
    syms = (hncodec.load("data/c/syms.bin", {}) or {}).get("s", [])
    codes = sorted(set(r[0] for r in syms if r[1] in ("H", "X", "U") and stock(r[0])))
    if codes:
        fd = fund(codes)
        print("chỉ số", len(fd["d"]), put("data/fund.bin", "v", fd))


if __name__ == "__main__":
    main()
