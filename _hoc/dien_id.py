# Gắn id YouTube vào _hoc/videos.json bằng cách so tiêu đề với data/view/hist.json (yt-dlp, miễn phí).
# Video đã công khai trên kênh → có id → hoc.py xuất bản trang /hoc/<slug>.html. Chạy hằng ngày trong do_view.yml.
import json, os, re, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VP = os.path.join(ROOT, "_hoc/videos.json"); HP = os.path.join(ROOT, "data/view/hist.json")
if not os.path.exists(HP): raise SystemExit("chua co hist.json")
def norm(s):
    s = unicodedata.normalize("NFC", s or "").lower().replace("#shorts", "")
    return re.sub(r"[^\w]+", " ", s).strip()
V = json.load(open(VP, encoding="utf-8")); H = json.load(open(HP, encoding="utf-8"))
by_t = {}
for vid, h in H.items():
    if h.get("l") == "dai": by_t.setdefault(norm(h.get("t")), vid)
da = {v["id"] for v in V if v.get("id")}
n = 0
for v in V:
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})$", v.get("d") or "")
    if m: v["d"] = f"{m[3]}-{int(m[2]):02d}-{int(m[1]):02d}"
for v in V:
    if v.get("id"): continue
    vid = by_t.get(norm(v.get("title"))) or by_t.get(norm(v.get("h1")))
    if vid and vid not in da:
        v["id"] = vid; da.add(vid); n += 1
json.dump(V, open(VP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("gan id", n, "/ con thieu", sum(1 for v in V if not v.get("id")))
