# Thẻ số liệu cho reel "Vì sao Việt Nam đòi tăng trưởng hai con số" – chạy: python mk_the.py
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "engine"))
from PIL import Image, ImageDraw
os.environ.setdefault("HN_PX", "/tmp/_px.json")
if not os.path.exists(os.environ["HN_PX"]): open(os.environ["HN_PX"], "w").write("{}")
import dx2
F = dx2.F; W, H = 1008, 860
BG = (24, 12, 44); TIM = (124, 58, 237); TS = (196, 140, 255); VANG = (255, 214, 64); TR = (255, 255, 255); MO = (170, 160, 200); DO = (255, 107, 107); XANH = (74, 222, 128)
OUT = os.path.dirname(os.path.abspath(__file__))
def base(tieu, nguon):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    d.rounded_rectangle([6, 6, W - 6, H - 6], 36, outline=(90, 50, 150), width=4)
    d.text((W / 2, 50), tieu, font=F("ExtraBold", 44), fill=TS, anchor="ma")
    d.text((W / 2, H - 58), "Nguồn: " + nguon, font=F("Medium", 26), fill=MO, anchor="ma")
    return im, d
def bars(name, tieu, nguon, rows, mx, unit, hl=None):
    im, d = base(tieu, nguon); n = len(rows); x0, x1 = 110, W - 110; bw = (x1 - x0) / n; yb = H - 150; top = 190
    for i, (lab, v) in enumerate(rows):
        h = (yb - top) * v / mx; cx = x0 + bw * i + bw / 2; c = VANG if (hl is not None and i in hl) else TIM
        d.rounded_rectangle([cx - bw * 0.32, yb - h, cx + bw * 0.32, yb], 14, fill=c)
        d.text((cx, yb - h - 62), (f"{v:.2f}".replace(".", ",") + unit), font=F("Black", 46), fill=TR, anchor="ma")
        d.text((cx, yb + 16), lab, font=F("Bold", 32), fill=MO, anchor="ma")
    im.save(os.path.join(OUT, name))
def ladder(name, tieu, nguon, rows):
    im, d = base(tieu, nguon); y = 180 + (3 - len(rows)) * 95
    mx = max(v for _, v, _ in rows)
    for lab, v, c in rows:
        d.text((70, y), lab, font=F("Bold", 34), fill=MO)
        w = (W - 140) * v / mx; d.rounded_rectangle([70, y + 50, 70 + w, y + 130], 18, fill=c)
        s = f"{v:,.0f}".replace(",", ".") + " USD"; fs = F("Black", 48)
        if w < d.textlength(s, font=fs) + 50: d.text((70 + w + 20, y + 64), s, font=fs, fill=TR)
        else: d.text((90, y + 64), s, font=fs, fill=(20, 10, 30) if c == VANG else TR)
        y += 190
    im.save(os.path.join(OUT, name))
def big(name, tieu, nguon, lines):
    im, d = base(tieu, nguon); y = 230
    for s, sz, c in lines:
        d.text((W / 2, y), s, font=F("Black", sz), fill=c, anchor="ma"); y += int(sz * 1.35)
    im.save(os.path.join(OUT, name))
bars("the_gdp.png", "TĂNG TRƯỞNG GDP VIỆT NAM", "Cục Thống kê", [("2025", 8.02), ("Q1/26", 8.15), ("Q2/26", 8.81), ("Q3/26", 9.95)], 11, "%", hl={3})
ladder("the_thang.png", "GDP BÌNH QUÂN ĐẦU NGƯỜI", "Cục Thống kê, NQ Đại hội XIV, Ngân hàng Thế giới", [("Năm 2025", 5026, TIM), ("Mục tiêu năm 2030", 8500, TS), ("Ngưỡng thu nhập cao", 14375, VANG)])
big("the_toan.png", "CẦN GẤP GẦN 3 LẦN", "Tính đơn giản theo mức tăng thực bình quân", [("10%/năm", 92, VANG), ("≈ 11 năm", 76, TR), ("6%/năm", 92, TS), ("≈ 18 năm", 76, TR)])
big("the_danso.png", "ĐỒNG HỒ DÂN SỐ", "Cục Thống kê – UNFPA, 12/2025", [("2034", 110, VANG), ("bước vào dân số già", 44, TR), ("2036", 110, DO), ("hết thời kỳ dân số vàng", 44, TR)])
big("the_bay.png", "BẪY THU NHẬP TRUNG BÌNH", "Ngân hàng Thế giới, 2024", [("108", 120, TS), ("nước thu nhập trung bình", 44, TR), ("34", 120, VANG), ("lên được thu nhập cao từ 1990", 44, TR)])
ladder("the_han.png", "HÀN QUỐC: THU NHẬP ĐẦU NGƯỜI", "Ngân hàng Thế giới", [("Năm 1960", 1200, TIM), ("Cuối năm 2023", 33000, VANG)])
print("ok")
