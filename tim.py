# Tạo tim.json cho ô "Tìm nhanh" trên trang chủ: mọi trang + các mục của trang chủ (tiêu đề, đường dẫn, nhóm)
import os, re, glob, json, html
ROOT = os.path.dirname(os.path.abspath(__file__)); out = []
MUC = [("Top 10 cổ phiếu khỏe nhất", "/#top-10-co-phieu-khoe"), ("Thị trường hôm nay", "/thi-truong-chung-khoan-hom-nay.html"), ("Sức mạnh dòng tiền", "/#dongtien"),
       ("Bảng giá chứng khoán 3 sàn", "/#banggia"), ("Soi chart cổ phiếu", "/#soichart"), ("So sánh 2 mã cổ phiếu", "/#sosanh"), ("Vĩ mô Việt Nam", "/#vimo"),
       ("Thị trường thế giới, hàng hóa", "/the-gioi-hang-hoa.html"), ("Đánh giá BCTC kết quả kinh doanh quý", "/#bctc"), ("Tin tức doanh nghiệp và vĩ mô", "/#tintuc"),
       ("Báo cáo phân tích công ty chứng khoán", "/#baocao"), ("Lịch sự kiện, cổ tức, họp ĐHCĐ", "/#lichsk"), ("Bảng theo dõi cổ phiếu", "/#bang"),
       ("Hỏi đáp chuyên sâu PRO", "/#hoidap"), ("Tư vấn đầu tư 1:1", "/tu-van-dau-tu-chung-khoan.html"), ("Gửi tích lũy, lợi suất", "/#tichluy"),
       ("Cộng đồng Zalo miễn phí", "/#congdong"), ("Công cụ quản trị rủi ro, tính lãi lỗ", "/#congcu"), ("Seri phân tích cơ bản cho người mới", "/#seri"),
       ("Học chứng khoán từ số 0: lộ trình 7 bước", "/f0/"), ("Lịch sử và câu chuyện chứng khoán", "/#lichsu"), ("Định giá cổ phiếu", "/dinh-gia-co-phieu.html"),
       ("Tra cứu mã cổ phiếu A–Z", "/ma/"), ("Mở tài khoản chứng khoán", "/mo-tai-khoan-chung-khoan.html"), ("Bài học có video", "/hoc/"),
       ("Từ điển thuật ngữ chứng khoán", "/f0/tu-dien-thuat-ngu-chung-khoan.html"), ("Giới thiệu Huy Nguyễn", "/gioi-thieu.html"), ("Liên hệ", "/lien-he.html")]
for t, u in MUC: out.append([t, u, "Mục"])
NH = {"f0": "Cẩm nang F0", "hoc": "Bài học", "ma": "Mã cổ phiếu"}
for p in sorted(glob.glob(ROOT + "/**/*.html", recursive=True)):
    rel = p.replace(ROOT, "").replace("\\", "/")
    if rel.startswith(("/_", "/node_modules")) or rel in ("/index.html", "/bao-cao-2026.html", "/404.html"): continue
    s = open(p, encoding="utf-8", errors="ignore").read(8000)
    m = re.search(r"<title>([^<]*)</title>", s)
    if not m: continue
    t = html.unescape(m.group(1)).split(" | ")[0].strip()
    u = rel[:-10] or "/" if rel.endswith("/index.html") else rel
    out.append([t, u, NH.get(rel.split("/")[1], "Trang")])
json.dump(out, open(os.path.join(ROOT, "tim.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(len(out), "muc")
