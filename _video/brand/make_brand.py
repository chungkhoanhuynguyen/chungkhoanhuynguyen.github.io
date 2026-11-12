# Bộ nhận diện đồng bộ cho kênh phụ (QL1 12/11/2026): ảnh đại diện 800x800 + biểu ngữ 2560x1440 (vùng an toàn 1546x423 ở giữa).
import os
from PIL import Image, ImageDraw, ImageFilter
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine", "fonts")
def font(w, s): return __import__("PIL.ImageFont", fromlist=["x"]).truetype(os.path.join(F, "BeVietnamPro-%s.ttf" % w), s)
GOLD = (255, 196, 0); WHITE = (255, 255, 255); MUTE = (190, 196, 214)
K = [  # handle, tên, chữ viết tắt, dòng 2 trên avatar, khẩu hiệu, màu nhấn
 ("2", "Cổ Phiếu Mỗi Ngày", "CP", "MỖI NGÀY", "Tin nóng · Dòng tiền · Cổ phiếu", (56, 189, 248)),
 ("3", "Huy Invest", "HI", "INVEST", "Thế giới biến động · Tiền của bạn ra sao?", (255, 196, 0)),
 ("4", "Chứng Khoán Lướt Sóng Thần", "LST", "LƯỚT SÓNG", "Margin · FOMO · Bài học từ những cú sập", (249, 115, 22)),
 ("5", "Vĩ Mô Nóng", "VMN", "VĨ MÔ", "Đất nền · Bảo hiểm · Vay mua nhà – thật tệ khi…", (239, 68, 68)),
 ("6", "Đầu Tư Tích Sản", "TS", "TÍCH SẢN", "Nếu… chuyện tiền bạc của người Việt", (34, 197, 94)),
 ("7", "Vĩ Mô Chứng Khoán Dễ Hiểu", "VM", "DỄ HIỂU", "Lãi suất · Tỷ giá · Ngân hàng Nhà nước", (168, 85, 247)),
 ("8", "Soi Báo Cáo Tài Chính", "BCTC", "SOI SỐ", "Doanh nghiệp sụp đổ · Bài học từ con số", (20, 184, 166)),
 ("9", "Đầu Tư Cổ Phiếu", "ĐT", "CỔ PHIẾU", "Vì sao thật tệ khi là… · Chuyện tiền bạc đời thật", (236, 72, 153)),
]
def nen(w, h, c):
    im = Image.new("RGB", (w, h), (12, 14, 24)); d = ImageDraw.Draw(im)
    for y in range(h):
        a = y / h; d.line([(0, y), (w, y)], fill=(int(12 + 10 * a), int(14 + 6 * a), int(24 + 18 * a)))
    g = Image.new("L", (w, h)); ImageDraw.Draw(g).ellipse([w * 0.18, h * 0.05, w * 0.82, h * 0.95], fill=95)
    g = g.filter(ImageFilter.GaussianBlur(min(w, h) // 5))
    im.paste(Image.new("RGB", (w, h), tuple(int(x * 0.55) for x in c)), (0, 0), g)
    d = ImageDraw.Draw(im)
    for i in range(0, w, max(40, w // 48)): d.line([(i, 0), (i, h)], fill=(255, 255, 255, 0) if False else (22, 25, 38), width=1)
    return im
def fit(d, s, w0, st, kieu="Black"):
    while st > 20 and d.textlength(s, font=font(kieu, st)) > w0: st -= 4
    return font(kieu, st)
def avatar(h, ten, vt, d2, kh, c, out):
    W = 800; im = nen(W, W, c); d = ImageDraw.Draw(im)
    d.ellipse([60, 60, W - 60, W - 60], outline=c, width=14)
    f = fit(d, vt, 500, 300 if len(vt) <= 2 else 230)
    bb = d.textbbox((0, 0), vt, font=f); tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((W - tw) / 2 - bb[0], 360 - th / 2 - bb[1] - 20), vt, font=f, fill=WHITE)
    f2 = fit(d, d2, 440, 60, "ExtraBold"); bb2 = d.textbbox((0, 0), d2, font=f2)
    d.text(((W - (bb2[2] - bb2[0])) / 2 - bb2[0], 540 - bb2[1]), d2, font=f2, fill=c)
    im.save(out, quality=95)
def banner(h, ten, vt, d2, kh, c, out):
    W, H = 2560, 1440; im = nen(W, H, c); d = ImageDraw.Draw(im)
    x0, y0, sw, sh = (W - 1546) // 2, (H - 423) // 2, 1546, 423   # vùng an toàn
    # chữ viết tắt mờ lớn bên phải làm điểm nhấn
    fb = font("Black", 420); d.text((x0 + sw - d.textlength(vt, font=fb) + 40, y0 - 40), vt, font=fb, fill=tuple(int(x * 0.28) + 10 for x in c))
    d.text((x0 + 20, y0 + 22), "HUY NGUYỄN", font=font("Black", 40), fill=WHITE)
    d.text((x0 + 20 + d.textlength("HUY NGUYỄN ", font=font("Black", 40)), y0 + 30), "CHỨNG KHOÁN", font=font("SemiBold", 30), fill=GOLD)
    ft = fit(d, ten.upper(), sw - 80, 128); d.text((x0 + 20, y0 + 92), ten.upper(), font=ft, fill=WHITE)
    yb = y0 + 92 + int(ft.size * 1.12)
    d.rectangle([x0 + 22, yb + 6, x0 + 22 + 140, yb + 16], fill=c)
    fk = fit(d, kh, sw - 80, 56, "Bold"); d.text((x0 + 20, yb + 34), kh, font=fk, fill=MUTE)
    d.text((x0 + 20, y0 + sh - 62), "chungkhoanhuynguyen.com", font=font("SemiBold", 38), fill=GOLD)
    im.save(out, quality=92)
if __name__ == "__main__":
    o = os.path.dirname(os.path.abspath(__file__))
    for k in K:
        avatar(*k, os.path.join(o, "avatar_%s.jpg" % k[0])); banner(*k, os.path.join(o, "banner_%s.jpg" % k[0]))
    print("ok", len(K))
