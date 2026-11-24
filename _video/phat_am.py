"""BẢNG CÁCH ĐỌC DÙNG CHUNG cho mọi xưởng (video dài, reel, Shorts) – anh Huy 22/11:
"STB đọc là sa com banh", "VietinBank là Việt tin banh", "Techcombank là tếch com banh", "FPT đọc ép pi ti",
"bất động sản chấm com". Giọng TTS tiếng Việt tự đánh vần chữ tiếng Anh → mọi tên riêng/mã CK phải qua doc() TRƯỚC khi tạo giọng.
Chỉ áp vào LỜI ĐỌC, phụ đề/thẻ giữ chữ gốc. Gặp tên mới: THÊM VÀO ĐÂY (cụm dài đặt trước cụm ngắn)."""
PHAT_AM = [
    ("cổ phiếu CTG", "cổ phiếu Việt tin banh"), ("cổ phiếu FRT", "cổ phiếu ép pi ti Ri teo"),
    ("cổ phiếu HVN", "cổ phiếu Việt Nam Ê lai"), ("cổ phiếu VHM", "cổ phiếu Vin hôm"),
    ("cổ phiếu TCB", "cổ phiếu Tếch com banh"), ("Cổ phiếu VHM", "Cổ phiếu Vin hôm"), ("cầm FRT", "cầm cổ phiếu ép pi ti Ri teo"),
    ("Sacombank", "Sa com banh"), ("VietinBank", "Việt tin banh"), ("Techcombank", "Tếch com banh"),
    ("FPT Retail", "ép pi ti Ri teo"), ("FPT Shop", "ép pi ti Sóp"), ("FPT", "ép pi ti"), ("Vietcap", "Việt cáp"),
    ("ESOP", "ê sóp"), ("Creador", "Cờ rê a đo"), ("Vietnambiz", "Việt Nam bít"),
    ("CBRE", "xi bi a ri"), ("Mekong ASEAN", "Mê Kông A xê an"), ("Vietcombank", "Việt com banh"), ("VPBank", "Vê pê banh"), ("MBBank", "em bê banh"), ("Batdongsan.com.vn", "bất động sản chấm com"), ("Batdongsan", "bất động sản chấm com"),
    ("APEC", "A péc"),
    ("Sociu", "Sô Ciu"), ("Vinhomes", "Vin hôm"), ("Viconship", "Vi côn síp"), ("Gemadept", "Ghê ma đép"), ("Gemalink", "Ghê ma linh"),  # anh Huy 24/11: Sociu đọc là sô ciu
    ("The Sapphire", "Đờ Sa phai a"), ("Vinhomes Smart City", "Vin hôm Sờ mát Xi ti"),
    ("Lumi Hanoi", "Lu mi Hà Nội"), ("Times City", "Tham Xi ti"), ("Ocean Park", "Âu sần Pác"),
]
def doc(t):
    for a_, b_ in PHAT_AM: t = t.replace(a_, b_)
    return t

