"""Kiem goi tieu de + bia (hoc tu youtube-agent-skill/yt-package, viet lai cho tieng Viet). QL1 20/11/2026.
Luat: tieu de <=60 ky tu (desktop), y chinh trong 40 ky tu dau (mobile); co con so/ten/ngay;
<=2 tu IN HOA trong tieu de; bia KHONG lap lai tieu de (trung <50% tu); bia <=2 dong, moi dong <=4 tu."""
import re, sys, json
def _w(s): return [x for x in re.findall(r"[\wÀ-ỹ+.,%]+", s.lower()) if len(x) > 1]
def kiem(title, bia):
    L = []; t = str(title or ""); b = [str(x) for x in (bia or [])]
    if len(t) > 60: L.append("LỖI tiêu đề %d ký tự > 60 (desktop cắt)" % len(t))
    if not re.search(r"\d", t[:40]): L.append("CẢNH BÁO 40 ký tự đầu (mobile) chưa có con số")
    hoa = [w for w in re.findall(r"\b[A-ZÀ-Ỹ]{3,}\b", t) if not re.fullmatch(r"[A-Z]{2,5}", w)]
    if len(hoa) > 2: L.append("CẢNH BÁO tiêu đề có %d từ IN HOA (>2 trông như spam)" % len(hoa))
    if len(b) > 2: L.append("LỖI bìa %d dòng > 2" % len(b))
    for x in b:
        if len(x.split()) > 4: L.append("CẢNH BÁO bìa dòng '%s' > 4 từ – nhỏ trên điện thoại" % x)
    tw, bw = set(_w(t)), set(_w(" ".join(b)))
    if bw and len(tw & bw) / len(bw) > 0.5: L.append("CẢNH BÁO bìa lặp lại tiêu đề (%d%% từ trùng) – cùng lời hứa, khác chữ" % (100 * len(tw & bw) // len(bw)))
    return L
if __name__ == "__main__":
    m = json.load(open(sys.argv[1], encoding="utf-8"))
    for k, v in m.items():
        if isinstance(v, dict) and (v.get("title") or v.get("tieu_de")):
            for l in kiem(v.get("title") or v.get("tieu_de"), v.get("bia_hook")): print(k, l)
