# Ảnh minh hoạ thật, miễn phí (Wikimedia Commons, giấy phép CC/PD) cho từng cảnh video dài.
import json, os, re, urllib.request, urllib.parse, io, hashlib
from PIL import Image
UA = {"User-Agent": "HuyNguyenVideoBot/1.0 (chungkhoanhuynguyen.com)"}
OKLIC = re.compile(r"^(CC BY|CC0|Public domain|PD|CC-BY)", re.I)
MA = {  # mã -> từ khoá ảnh
 "VCB": "Vietcombank", "CTG": "VietinBank", "BID": "BIDV bank", "TCB": "Techcombank", "MBB": "MB Bank Vietnam",
 "VPB": "VPBank", "ACB": "Asia Commercial Bank Vietnam", "STB": "Sacombank", "HDB": "HDBank", "SHB": "SHB bank Hanoi",
 "BSR": "Dung Quat refinery", "PVD": "drilling rig Vietnam", "GAS": "PetroVietnam Gas", "PLX": "Petrolimex",
 "VHM": "Vinhomes", "VIC": "Vingroup Landmark 81", "VRE": "Vincom", "NVL": "Novaland", "KDH": "Ho Chi Minh City apartments",
 "HPG": "Hoa Phat steel", "HSG": "Hoa Sen steel roof", "NKG": "steel coils", "MWG": "Thegioididong store",
 "MSN": "Masan Vietnam", "VNM": "Vinamilk", "FPT": "FPT Corporation", "SSI": "SSI securities", "GMD": "Cat Lai port",
 "VJC": "Vietjet Air", "HVN": "Vietnam Airlines", "DGC": "chemical plant", "POW": "power plant Vietnam", "REE": "REE Tower",
}
CHU = [  # từ trong câu -> từ khoá
 (r"ngân hàng|tín dụng|nợ xấu|NIM|lãi vay|tiền gửi", "bank Vietnam"),
 (r"dầu|lọc hoá|xăng", "oil refinery"), (r"thép", "steel mill"), (r"bất động sản|căn hộ|nhà ở", "Ho Chi Minh City apartments"),
 (r"tích sản|góp đều|tiết kiệm|tiền", "Vietnamese dong banknotes"), (r"cảng|xuất khẩu|logistics", "container port Vietnam"),
 (r"điện|năng lượng", "power plant Vietnam"), (r"bán lẻ|siêu thị|tiêu dùng", "supermarket Vietnam"),
 (r"P/E|định giá|bẫy|cổ phiếu|chứng khoán|VN-Index|thị trường", "Ho Chi Minh City Stock Exchange"),
]
NEN = ["Ho Chi Minh City skyline", "Hanoi skyline", "Bitexco Financial Tower", "Saigon river night", "Landmark 81"]

def _get(u, t=20):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read()

NGUOI = re.compile(r"confederate|counterfeit|people|person|portrait|men of|women of|businesspeople|business people|politician|chairman|ceo|founder|births|living people|selfie|headshot|ông |bà |chân dung|doanh nhân|chủ tịch|giám đốc|lãnh đạo|_em\\.|nguyen|nguyễn|tran |trần |le van|lê văn|pham|phạm|hoang|hoàng|võ |đỗ |doan|đoàn")
def tim(q, n=12):
    u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query", "format": "json", "generator": "search", "gsrsearch": "filetype:bitmap " + q,
        "gsrnamespace": 6, "gsrlimit": n, "prop": "imageinfo", "iiprop": "url|extmetadata|size", "iiurlwidth": 1920})
    try: pages = json.loads(_get(u)).get("query", {}).get("pages", {})
    except Exception as e: print("anh: loi tim", q, e); return []
    out = []
    for p in sorted(pages.values(), key=lambda x: x.get("index", 99)):
        ii = (p.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata", {})
        lic = md.get("LicenseShortName", {}).get("value", "")
        if not OKLIC.match(lic) or ii.get("width", 0) < 1000 or ii.get("width", 0) < ii.get("height", 1): continue
        cat = (md.get("Categories", {}).get("value", "") + "|" + p.get("title", "") + "|" + re.sub("<[^>]+>", "", md.get("ImageDescription", {}).get("value", ""))).lower()
        if NGUOI.search(cat): continue          # không dùng ảnh chân dung / người thật (nhất là người nổi tiếng)
        tg = re.sub("<[^>]+>", "", md.get("Artist", {}).get("value", "")).strip()[:60]
        out.append({"u": ii.get("thumburl") or ii["url"], "tg": tg or "không rõ", "lic": lic, "trang": ii.get("descriptionurl", "")})
    return out

class Kho:
    def __init__(s, wd): s.wd = wd; os.makedirs(wd, exist_ok=True); s.cache = {}; s.dung = set(); s.credit = []
    def _ds(s, q):
        if q not in s.cache: s.cache[q] = tim(q)
        return s.cache[q]
    def cho(s, sc, chu_de=""):
        """Chọn 1 ảnh chưa dùng cho cảnh. Trả về PIL.Image hoặc None."""
        txt = " ".join(str(sc.get(k, "")) for k in ("anh", "label", "say", "ch")) + " " + chu_de
        qs = []
        if sc.get("anh"): qs.append(sc["anh"])
        for m in re.findall(r"\b([A-Z]{3})\b", txt):
            if m in MA and MA[m] not in qs: qs.append(MA[m])
        for pat, q in CHU:
            if re.search(pat, txt, re.I) and q not in qs: qs.append(q)
        qs += NEN
        for q in qs:
            for it in s._ds(q):
                if it["u"] in s.dung: continue
                try:
                    im = Image.open(io.BytesIO(_get(it["u"], 30))).convert("RGB")
                except Exception as e: print("anh: loi tai", e); s.dung.add(it["u"]); continue
                s.dung.add(it["u"]); s.credit.append("%s – %s (%s) %s" % (q, it["tg"], it["lic"], it["trang"]))
                return im
        return None
