# Ảnh minh hoạ thật, miễn phí (Wikimedia Commons, giấy phép CC/PD) cho từng cảnh video dài.
import json, os, re, urllib.request, urllib.parse, urllib.error, io, hashlib
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
 (r"nhà máy điện|giá điện|ngành điện|năng lượng|thuỷ điện|nhiệt điện", "power plant Vietnam"), (r"bán lẻ|siêu thị|tiêu dùng", "supermarket Vietnam"),
 (r"P/E|định giá|bẫy|cổ phiếu|chứng khoán|VN-Index|thị trường", "Ho Chi Minh City Stock Exchange"),
]
NEN = ["Ho Chi Minh City skyline", "Hanoi skyline", "Bitexco Financial Tower", "Saigon river night", "Landmark 81"]

import time
_LAST = [0.0]
HAN = [0.0]   # QL1 11/11: hạn chót cả bước ảnh (render đặt = now + 20 phút). VT5DATNEN bị huỷ vì bước ảnh chạy 72 phút > giới hạn 90 phút.
class HetGio(Exception): pass
def _get(u, t=20):
    """Tải có giãn cách + thử lại khi Wikimedia báo 429 (quá nhiều yêu cầu) – lỗi 7/11 làm cảnh trống ảnh."""
    for k in range(6):
        if HAN[0] and time.time() > HAN[0]: raise HetGio("het gio buoc anh")
        dt = time.time() - _LAST[0]
        if dt < 0.8: time.sleep(0.8 - dt)
        _LAST[0] = time.time()
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and k < 5:
                w = float(e.headers.get("Retry-After") or 0) or 4 * 2 ** k; print("anh: 429, cho %.0fs" % w, flush=True); time.sleep(min(w, 30, max(0, (HAN[0] or 9e18) - time.time()))); continue
            raise

NGUOI = re.compile(r"confederate|counterfeit|people|person|portrait|men of|women of|businesspeople|business people|politician|chairman|ceo|founder|births|living people|selfie|headshot|ông |bà |chân dung|doanh nhân|chủ tịch|giám đốc|lãnh đạo|_em\\.|nguyen|nguyễn|tran |trần |le van|lê văn|pham|phạm|hoang|hoàng|võ |đỗ |doan|đoàn")
def tim_ov(q, n=20):
    """QL1 11/11 (anh Huy: ảnh minh hoạ phải sát nội dung): Openverse – kho ảnh CC lớn (Flickr, v.v.), khớp ý nghĩa tốt hơn Commons.
    Dùng: anh='ov:elderly woman bank counter'. Chỉ lấy giấy phép cho phép dùng thương mại, ảnh ngang ≥1200px."""
    rs = []; w = q.split()
    for qq, extra in ((q, {}), (" ".join(w[:2]) if len(w) > 2 else "", {})):   # 2 lần tối đa (lần 3 bị quá 90 phút)
        if not qq: continue
        u = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(dict({"q": qq, "page_size": n, "license_type": "commercial", "aspect_ratio": "wide", "mature": "false"}, **extra))
        try: rs = [r for r in json.loads(_get(u, 15)).get("results", []) if (r.get("width") or 0) >= 1200 and "sketchfab" not in (r.get("foreign_landing_url") or "")]
        except Exception as e: print("anh: loi openverse", qq, e); rs = []
        if rs: break
    out = []
    for r in rs:
        if (r.get("width") or 0) < 1200 or XAU.search((r.get("title") or "") + " " + " ".join(t.get("name", "") for t in r.get("tags") or [])): continue
        lic = ("CC " + (r.get("license") or "").upper() + " " + (r.get("license_version") or "")).replace("CC CC0", "CC0").replace("CC PDM", "Public domain").strip()
        out.append({"u": r["url"], "tg": (r.get("creator") or "không rõ")[:60], "lic": lic, "trang": r.get("foreign_landing_url") or r.get("url")})
    print("anh: openverse", q, len(out), flush=True)
    return out

def tim(q, n=12):
    if q.startswith("ov:"): return tim_ov(q[3:].strip())
    if q.startswith("File:"):   # đúng 1 file Commons (cho cả bản đồ .svg → ảnh PNG), dùng cho cảnh bản đồ
        u = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({"action": "query", "format": "json", "titles": q, "prop": "imageinfo", "iiprop": "url|extmetadata", "iiurlwidth": 1600})
        try: pg = list(json.loads(_get(u))["query"]["pages"].values())[0]; ii = pg["imageinfo"][0]
        except Exception as e: print("anh: loi file", q, e); return []
        md = ii.get("extmetadata", {}); tg = re.sub("<[^>]+>", "", md.get("Artist", {}).get("value", "")).strip()[:60]
        return [{"u": ii.get("thumburl") or ii["url"], "tg": tg or "không rõ", "lic": md.get("LicenseShortName", {}).get("value", ""), "trang": ii.get("descriptionurl", "")}]
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
        if NGUOI.search(cat): continue
        if XAU.search(cat): continue            # 10/11: lọt ảnh hồ sơ vụ án (EFTA), ảnh lưu trữ NARA không liên quan
        if any(w[:5] not in cat for w in re.findall(r"[a-z]{3,}", q.lower())): continue   # mọi từ khoá phải có trong tên/mô tả/danh mục (tránh 'red stock' → cây thông)          # không dùng ảnh chân dung / người thật (nhất là người nổi tiếng)
        tg = re.sub("<[^>]+>", "", md.get("Artist", {}).get("value", "")).strip()[:60]
        out.append({"u": ii.get("thumburl") or ii["url"], "tg": tg or "không rõ", "lic": lic, "trang": ii.get("descriptionurl", "")})
    return out

XAU = re.compile(r"efta\d|epstein|nara|evidence|court|crime|police|prison|\.tif|ceremony|Stake_acquisition|signing|wordpress|wordcamp|mascot|plush|logo|sticker|state.bank|bank_of|ngân.hàng|vietcombank|bidv|techcombank|agribank|politician|press.conference|congress|senator|president|minister|portrait|damaged|wreck|accident|protest", re.I)

class Kho:
    def __init__(s, wd): s.wd = wd; os.makedirs(wd, exist_ok=True); s.cache = {}; s.dung = set(); s.credit = []; s.img = {}
    def _ds(s, q):
        if q not in s.cache:
            r = tim(q)
            if not r: return []          # lỗi/không có: không lưu, lần sau thử lại
            s.cache[q] = r
        return s.cache[q]
    def cho(s, sc, chu_de=""):
        """Chọn 1 ảnh chưa dùng cho cảnh. Trả về PIL.Image hoặc None."""
        txt = " ".join(str(sc.get(k, "")) for k in ("anh", "label", "say", "ch")) + " " + chu_de
        qs = []
        if sc.get("anh"): qs.extend(q.strip() for q in str(sc["anh"]).split("||") if q.strip())   # nhiều từ khoá dự phòng: "ov:...||Commons..."
        for m in re.findall(r"\b([A-Z]{3})\b", txt):
            if m in MA and MA[m] not in qs: qs.append(MA[m])
        for pat, q in CHU:
            if re.search(pat, txt, re.I) and q not in qs: qs.append(q)
        if sc.get("chat") and not isinstance(sc["chat"], dict): qs = [q.strip() for q in str(sc.get("anh") or "").split("||") if q.strip()]   # reel: chỉ đúng từ khoá cảnh
        else: qs += NEN
        for q in [q for q in qs if q]:
            if HAN[0] and time.time() > HAN[0]: return None
            for it in s._ds(q):
                if it["u"] in s.dung:
                    # 11/11 NV1: ảnh chỉ định đích danh (File:) được dùng lại cho cảnh sau, thay vì rơi xuống từ khoá chung lạc đề
                    if q.startswith("File:") and q == sc.get("anh") and it["u"] in s.img: return s.img[it["u"]].copy()
                    continue
                try:
                    im = Image.open(io.BytesIO(_get(it["u"], 15))); im = (Image.alpha_composite(Image.new("RGBA", im.size, (255, 255, 255, 255)), im.convert("RGBA")) if im.mode in ("RGBA", "LA", "P") else im).convert("RGB")
                except Exception as e: print("anh: loi tai", e); s.dung.add(it["u"]); continue
                s.dung.add(it["u"]); s.img[it["u"]] = im; s.credit.append("%s – %s (%s) %s" % (q, it["tg"], it["lic"], it["trang"]))
                return im
        return None
