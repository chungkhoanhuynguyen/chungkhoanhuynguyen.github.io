# Xưng hô lễ phép cho lời đọc + phụ đề (anh Huy chốt 6/11): người nói xưng "em", gọi người xem "anh chị".
# Không nói trống không / không gọi "bạn". Áp tự động trong render.py và reel.py.
import re
_GIU = r"(?!\s*(bè|đời|học|thân|đồng hành|hàng|gái|trai|cũ)\b)"
QUY = [
    (r"\b(các|những) bạn\b", "anh chị"), (r"\b(Các|Những) bạn\b", "Anh chị"),
    (r"(?<!người )(?<!làm )\bbạn\b" + _GIU, "anh chị"), (r"(?<!Người )\bBạn\b" + _GIU, "Anh chị"),
    (r"\bchúng tôi\b", "chúng em"), (r"\bChúng tôi\b", "Chúng em"),
    (r"\btôi\b", "em"), (r"\bTôi\b", "Em"),
    (r"\bchúng mình\b", "chúng em"), (r"\bChúng mình\b", "Chúng em"),
    # "mình" tự xưng -> "em"; giữ nghĩa phản thân ("của mình", "riêng mình", "tự mình", "bản thân mình", "một mình")
    (r"(?<!của )(?<!riêng )(?<!tự )(?<!thân )(?<!một )(?<!cho )(?<!biết )(?<!nghĩ )(?<!hỏi )(?<!ra )(?<!thấy )(?<!cứu )(?<!giúp )(?<!với )(?<!về )(?<!tin )(?<!khi )(?<!nếu )(?<!Nếu )(?<!lúc )(?<!để )(?<!rằng )(?<!là )\bmình\b(?=\s+(sẽ|đã|đang|vừa|cùng|đi|nói|kể|chọn|giải thích|mổ xẻ|đọc|phân tích|xem|làm|tóm|tổng|luôn|chỉ|có|muốn|gửi|để|hay|thường|nhấn|so|nhắc|tính|lấy|dùng|bắt|ghi|thấy|tin|nghĩ|cho|hỏi|trả|nhìn|lật|mở|đếm|liệt|dừng|quay|thử|thêm|bàn|đưa|rút|trình bày|tổng hợp))", "em"),
    (r"(?<![\w])Mình\b(?=\s+(sẽ|đã|đang|vừa|cùng|đi|nói|kể|chọn|giải thích|mổ xẻ|đọc|phân tích|xem|làm|tóm|tổng|luôn|chỉ|có|muốn|gửi|để|hay|thường|nhấn|so|nhắc|tính|lấy|dùng|bắt|ghi|thấy|tin|nghĩ|cho|hỏi|trả|nhìn|lật|mở|đếm|liệt|dừng|quay|thử|thêm|bàn|đưa|rút|trình bày|tổng hợp))", "Em"),
    (r"\b(video này|bài này|phần này|hôm nay) mình\b", r"\1 em"),
    (r"\banh chị anh chị\b", "anh chị"),
]
def le_phep(t):
    if not t or not isinstance(t, str): return t
    for a, b in QUY: t = re.sub(a, b, t)
    return t

if __name__ == "__main__":
    for s in ["Theo bạn, 48.800 tỷ này sẽ chảy vào đâu? Bình luận phe của bạn.", "Trong video này mình mổ xẻ báo cáo.", "công sức của mình mới là phần chính",
              "Bạn bè hỏi tôi", "Giờ mình đi tiếp.", "Mình chọn ba câu sau.", "Các bạn nhớ đăng ký", "số tiền của riêng mình", "Đó là lý do mình luôn nhấn mạnh"]:
        print(s, "=>", le_phep(s))
