# -*- coding: utf-8 -*-
"""QL1 11/11 – TỰ cắt 3 Shorts từ 1 video dài (chạy trong xưởng ngay sau render, hoặc tay):
    python3 tu_cat_short.py <thư mục out> KEY <lô>   (tên nút "Xem full" lấy từ tiêu đề trong meta.json)
Chọn đoạn:
  1) Mở đầu (cold open) – cảnh đắt nhất theo khuôn chuẩn, cắt ở câu hỏi/cuối câu 20–58s.
  2–3) Hai cảnh "đắt" nhất phía sau: ưu tiên cuộc gọi/thông báo/tin nhắn/giấy tờ (kịch tính), rồi số lớn/thẻ số;
       cách nhau ≥ 60s, không trùng mở đầu, không lấy cảnh kết/CTA.
Hook trên Short = dòng 'cap' của cảnh. Ra: <out>/<KEY>_S1.mp4.. + <KEY>_shorts.json (start, dài, hook) để NV3 đăng.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cat_short

DIEM = {"call": 5, "noti": 4, "chat": 4, "giay": 4, "bignum": 3, "cards": 3, "bars": 2, "checklist": 1, "text": 1}

def chon(canh, tong):
    out = [dict(a=0.0, dmin=20, hook=canh[0]["cap"])]
    cand = []
    for i, c in enumerate(canh):
        if i == 0 or c["k"] in ("end", "hook") or c["a"] < 35 or c["a"] > tong - 50: continue
        d = DIEM.get(c["k"], 1) + (1 if c.get("ch") else 0) + (1 if any(ch.isdigit() for ch in " ".join(c["cap"])) else 0)
        cand.append((d, c["a"], c))
    cand.sort(key=lambda x: (-x[0], x[1]))
    for d, a, c in cand:
        if len(out) >= 3: break
        if all(abs(a - o["a"]) >= 60 for o in out): out.append(dict(a=a, dmin=25, hook=c["cap"]))
    return out

if __name__ == "__main__":
    od, key, lo = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        t = json.load(open(os.path.join(HERE, "queue", lo, "meta.json"), encoding="utf-8"))[key].get("title", key)
    except Exception: t = key
    ten = t.split(" | ")[0].split(": ")[0].strip()
    if len(ten) > 46: ten = ten[:44].rsplit(" ", 1)[0] + "…"
    src = os.path.join(od, key + ".mp4"); os.environ["SRT"] = os.path.join(od, key + ".srt")
    canh = json.load(open(os.path.join(od, key + "_canh.json"), encoding="utf-8"))
    tong = canh[-1]["e"]; kq = []
    for n, s in enumerate(chon(canh, tong), 1):
        os.environ["DMIN"] = str(s["dmin"])
        hook = "|".join(str(x) for x in s["hook"][:2]) or ten.upper()
        o = os.path.join(od, "%s_S%d.mp4" % (key, n))
        try:
            d = cat_short.cat(src, o, s["a"], 58, hook, "Xem full: " + ten)
            kq.append(dict(file=os.path.basename(o), start=s["a"], dai=round(d, 1), hook=hook)); print(o, round(d, 1), hook, flush=True)
        except Exception as e: print("short loi", n, e, flush=True)
    json.dump(kq, open(os.path.join(od, key + "_shorts.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
