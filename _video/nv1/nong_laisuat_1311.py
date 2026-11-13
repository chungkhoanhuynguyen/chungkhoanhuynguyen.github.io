# -*- coding: utf-8 -*-
# NV1B 13/11/2026 – VIDEO NÓNG kênh chính: 46/46 ngân hàng giảm lãi suất (11/11) – nhưng "lãi vay khó xuống dưới 10%" (12/11) và 2027 cần 6,4 triệu tỷ vốn (12/11).
# Lý do chọn: tin lãi suất chạm túi người vay nhà + người gửi tiết kiệm; 7 ngày qua chưa làm lãi vay mua nhà (đã làm: NHNN mua USD, GDP-lương, nợ, XK, vàng, IPO).
# Nguồn (WiData news_feed + wi_data_macro, đọc 13/11/2026):
#  - MarketTimes 11/11/2026 "46 ngân hàng đồng loạt giảm lãi suất": 46/46 NHTM giảm ít nhất 0,5 điểm % lãi huy động kỳ hạn từ 6 tháng (NHTM nhà nước, vốn ngoại 0,5; cổ phần 0,5–0,7);
#    NHNN yêu cầu giảm 0,5–1%/năm lãi huy động TIỀN GỬI MỚI từ 6 tháng, làm điểm tựa giảm 1,5–2% lãi cho vay lĩnh vực SXKD ưu tiên; lãi vay mới bình quân giảm 0,2–0,5%/năm so đầu tháng 10;
#    >20 NH có gói giảm 1,5–2%; một NH cổ phần lớn giảm 1,5% cho 5 lĩnh vực ưu tiên (nông nghiệp nông thôn; SXKD hàng XK; DN nhỏ và vừa; CN hỗ trợ; DN công nghệ cao);
#    lãi thực nhận người gửi ở một số kỳ hạn cao hơn biểu công bố tới 2,9 điểm %; ví dụ VAMC: huy động 5.000 tỷ, 1.000 tỷ nợ xấu → 4.000 tỷ còn lại gánh.
#  - vietnamfinance 12/11/2026 + Nhà Đầu Tư 12/11/2026 (Vietnam Investment Forum 2027): PTGĐ TPBank: lãi USD ~5% + bù tỷ giá 2 + 2,5 → chi phí vốn ~9,5%, "lãi cho vay khó xuống dưới 10%";
#    10 tháng 2026 tín dụng tăng hơn 11%, huy động gần 10%; TS Cấn Văn Lực: định hướng tín dụng 15–16% điều chỉnh lên ~19%; NIM ~3% cuối 2025 → 2,8% QI → ~2,5% hiện nay.
#  - vietnambiz 12/11/2026: Thủ tướng báo cáo QH chiều 12/11: vốn đầu tư toàn xã hội 2027 cần 36–38% GDP ≈ 6–6,4 triệu tỷ đồng.
#  - Hà Nội Mới 11/11/2026: lãi vay mua nhà phổ biến 8,5–11%/năm thời gian ưu đãi; thả nổi sau ưu đãi 13–15%/năm.
#  - vietnamfinance 21/10/2026: lãi thả nổi = lãi cơ sở/tham chiếu + biên độ 3–5%/năm.
#  - vietnamfinance 26/10/2026 (TS Lê Hồng Hạnh, RMIT): đến 31/8 tín dụng kinh doanh BĐS +19,59%, cho vay mua nhà để ở +1,02%.
#  - WiData macro: lãi huy động 12 tháng bình quân NHTM nhà nước 5,4% (12/11/2026, id 202886); CPI 10/2026 +5,09% yoy (id 75701);
#    qua đêm 6,07% (6/11) → 4,33% (11/11) (id 82237); OMO 4,5% (id 81522).
#  - NHNN năm 2023 giảm lãi suất điều hành 4 lần, tái cấp vốn từ 6% xuống 4,5% (NHNN, các quyết định 2023).
# SỐ TỰ TÍNH (giả định nhân vật): vay 1,5 tỷ, 20 năm, trả góp đều: năm đầu 9% → 13,50 triệu mỗi tháng; dư nợ sau 12 tháng 1,472 tỷ;
#   228 tháng còn lại ở 13% → 17,44 triệu (thêm 3,94 triệu mỗi tháng, ≈ 47,3 triệu mỗi năm); ở 12,5% → 16,93 triệu (bớt ≈ 0,51 triệu); ở 11% → 15,42 triệu.
#   Sổ 500 triệu: lãi 5,4% = 27 triệu; trượt giá 5,09% = 25,45 triệu → dư 1,55 triệu; nếu lãi 4,9% = 24,5 triệu → thua trượt giá 0,95 triệu.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261113_0810_nong'
KEY = 'NONG1311A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
NHA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
CHO = 'ov:Ben Thanh Market||Ben Thanh Market'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('46 NGÂN HÀNG GIẢM LÃI', 'SAO TÔI VẪN TRẢ 13%?'), cols=CR, noti=dict(gio='08:15', ngay='Thứ Tư', items=[
        ('Tin tức', 'Lãi suất', '46/46 ngân hàng giảm lãi huy động, lãi vay có thể giảm 1,5 đến 2%', X_),
        ('Ngân hàng', 'Khoản vay mua nhà', 'Hết ưu đãi. Lãi suất kỳ tới: 13%/năm', R_)]),
      say=("Sáng thứ Tư, mười một tháng mười một, anh Tuấn đọc được tin nóng: cả bốn mươi sáu ngân hàng thương mại đã đồng thuận giảm lãi suất huy động. Mục tiêu là kéo lãi cho vay xuống từ một phẩy năm đến hai điểm phần trăm. Anh thở phào. "
           "Năm phút sau, ứng dụng ngân hàng báo một tin khác: khoản vay mua nhà của anh đã hết thời gian ưu đãi, kỳ tới lãi suất là mười ba phần trăm mỗi năm.")),
 dict(k='bignum', anh=NHA, cap=('TRẢ THÊM GẦN 4 TRIỆU', 'MỖI THÁNG'), cols=CR, value=3.94, fmt='{:,.2f}', unit=' triệu đồng', top='VAY 1,5 TỶ: LÃI 9% LÊN 13%', sub='Em tự tính, trả góp 20 năm', col=RED,
      say=("Anh Tuấn vay một tỷ rưỡi mua căn hộ, trả góp trong hai mươi năm. Năm đầu lãi ưu đãi chín phần trăm, mỗi tháng anh trả khoảng mười ba phẩy năm triệu cả gốc lẫn lãi. Sang mức mười ba phần trăm, con số lên khoảng mười bảy phẩy bốn triệu. "
           "Thêm gần bốn triệu đồng mỗi tháng, theo phép tính em tự làm. Vậy đợt giảm lãi này rơi vào túi ai?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Tin gốc nói gì?', cap=('"GIẢM LÃI RỒI', 'SAO CỦA ANH LẠI TĂNG?"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='08:30', mau=G_, msgs=[
        ('me', 'Ngân hàng giảm lãi 2% rồi mà sao khoản vay của anh lên 13%?'),
        ('Vợ', 'Anh đọc kỹ chưa? Giảm cho ai?'),
        ('Vợ', 'Sổ tiết kiệm 500 triệu của em tuần sau đáo hạn đấy')]),
      say=("Anh nhắn cho vợ: ngân hàng giảm lãi hai phần trăm rồi, sao khoản vay của anh lại lên mười ba phần trăm? Chị Hạnh, vợ anh, làm kế toán, trả lời gọn: anh đọc kỹ chưa, giảm cho ai? "
           "Rồi chị nhắn thêm: sổ tiết kiệm năm trăm triệu của em tuần sau đáo hạn đấy.")),
 dict(k='giay', cap=('ĐỌC KỸ TIN GỐC', 'NGƯỜI GỬI TIỀN GIẢM TRƯỚC'), cols=CC, moc=True, giay=dict(tieu_de='GIẢM LÃI SUẤT THÁNG 11/2026', so='Tóm tắt theo báo chí ngày 11/11/2026', dau='ĐÃ ĐỌC', dieu=[
        ('46/46 ngân hàng giảm ít nhất 0,5 điểm lãi huy động.', 'NGƯỜI GỬI GIẢM'),
        ('Áp dụng cho tiền gửi mới, kỳ hạn từ 6 tháng.', 'TIỀN GỬI MỚI'),
        ('Cho vay giảm 1,5 đến 2 điểm: lĩnh vực ưu tiên.', 'CHỈ NHÓM ƯU TIÊN'),
        ('Lãi vay mới bình quân giảm 0,2 đến 0,5 điểm.', 'MỚI GIẢM ÍT')]),
      say=("Chị Hạnh đọc chậm từng dòng. Một, cả bốn mươi sáu ngân hàng giảm ít nhất không phẩy năm điểm phần trăm lãi huy động. Hai, áp dụng cho tiền gửi mới, kỳ hạn từ sáu tháng trở lên. "
           "Ba, lãi cho vay giảm một phẩy năm đến hai điểm, nhưng dành cho các lĩnh vực sản xuất kinh doanh ưu tiên. Và dòng thứ tư ít ai để ý. Lãi suất bình quân của các khoản vay mới chỉ giảm từ không phẩy hai đến không phẩy năm điểm so với đầu tháng mười.")),
 dict(k='cards', anh=TP, cap=('GIẢM 2% CHỈ LÀ MỨC TỐI ĐA', 'CHO NHÓM ƯU TIÊN'), cols=CC, moc=True,
      cards=[('2%', 'Mức giảm tối đa cho vay', 'CHỈ NHÓM ƯU TIÊN'), ('0,5%', 'Vay mới bình quân giảm tối đa', 'SO VỚI ĐẦU THÁNG 10')],
      say=("Nghĩa là hai phần trăm trên tiêu đề là mức giảm tối đa, cho một nhóm khách hàng cụ thể. Còn khoản vay cũ đang thả nổi như của anh Tuấn thì không nằm trong dòng nào cả.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='checklist', ch='Chương 2 – Ai được giảm, ai chưa?', anh=TP, cap=('AI ĐƯỢC GIẢM', 'AI CHƯA TỚI LƯỢT'), cols=CC, moc=True,
      items=[('Nông nghiệp, hàng xuất khẩu', GREEN), ('DN nhỏ và vừa, công nghệ cao', GREEN), ('Công nghiệp hỗ trợ', GREEN), ('Vay mua nhà, tiêu dùng: chưa', RED)],
      say=("Một ngân hàng cổ phần lớn giảm một phẩy năm điểm cho năm lĩnh vực ưu tiên. Đó là nông nghiệp, hàng xuất khẩu, doanh nghiệp nhỏ và vừa, công nghiệp hỗ trợ và công nghệ cao. Vay mua nhà để ở, vay tiêu dùng, chưa phải đối tượng được ưu tiên ở đợt này.")),
 dict(k='bars', anh=NHA, cap=('VỐN CHẢY VỀ CHỦ ĐẦU TƯ', 'NGƯỜI MUA NHÀ ĐỨNG NGOÀI'), cols=CR, moc=True,
      bars=[('KD bất động sản', 19.59, GOLD, '+19,59%'), ('Mua nhà để ở', 1.02, RED, '+1,02%')],
      say=("Tính đến ba mươi mốt tháng tám, tín dụng cho kinh doanh bất động sản, tức là cho chủ đầu tư, tăng mười chín phẩy năm chín phần trăm. "
           "Trong khi cho vay mua nhà để ở chỉ tăng một phẩy không hai phần trăm. Tiền vẫn chảy vào bất động sản, nhưng chủ yếu vào phía người xây, chưa phải phía người mua để ở.")),
 dict(k='call', cap=('"KHOẢN CŨ CỦA ÔNG', 'CHỈ ĐỔI Ở KỲ ĐIỀU CHỈNH"'), cols=CC, moc=True, call=dict(ten='Anh Long', phu='Làm tín dụng ngân hàng', mau=X_, loi=[
        'Gói giảm lãi là cho sản xuất kinh doanh', 'Thả nổi = lãi cơ sở cộng biên độ 3 đến 5%']),
      say=("Anh Tuấn gọi cho anh Long, người quen làm tín dụng ngân hàng. Anh Long nói: gói giảm lãi đợt này là cho sản xuất kinh doanh. Khoản vay nhà thả nổi của ông tính bằng lãi cơ sở cộng biên độ, thường từ ba đến năm điểm phần trăm. "
           "Lãi cơ sở có giảm thì ông mới được giảm, và chỉ đổi vào đúng kỳ điều chỉnh ghi trong hợp đồng.")),
 dict(k='cards', anh=NHA, cap=('LÃI VAY MUA NHÀ', 'THÁNG 11/2026'), cols=CR, moc=True,
      cards=[('8,5 đến 11%', 'Thời gian ưu đãi', 'MỨC PHỔ BIẾN'), ('13 đến 15%', 'Thả nổi sau ưu đãi', 'CÓ THỂ LÊN TỚI')],
      say=("Theo báo Hà Nội Mới ngày mười một tháng mười một, lãi vay mua nhà phổ biến từ tám phẩy năm đến mười một phần trăm trong thời gian ưu đãi. "
           "Hết ưu đãi, lãi thả nổi có thể lên mười ba đến mười lăm phần trăm, tùy từng nơi. Anh Tuấn ở mức mười ba, chưa phải tệ nhất.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='bignum', ch='Chương 3 – Vì sao lãi vay khó giảm sâu?', anh=HN, cap=('NĂM 2027 CẦN', '6,4 TRIỆU TỶ VỐN'), cols=CC, moc=True, value=6.4, fmt='{:,.1f}', unit=' triệu tỷ', top='VỐN ĐẦU TƯ TOÀN XÃ HỘI 2027', sub='Khoảng 36 đến 38% GDP', col=GOLD,
      say=("Vì sao ngân hàng không giảm đều cho tất cả? Chiều mười hai tháng mười một, Thủ tướng báo cáo trước Quốc hội. Theo đó, năm 2027 cần huy động tới sáu phẩy bốn triệu tỷ đồng vốn đầu tư toàn xã hội. Con số đó tương đương ba mươi sáu đến ba mươi tám phần trăm GDP. "
           "Nhu cầu vốn khổng lồ như vậy, mà phần lớn vốn trung và dài hạn vẫn đang đi qua ngân hàng.")),
 dict(k='cards', anh=HN, cap=('CHO VAY CHẠY NHANH HƠN', 'TIỀN GỬI'), cols=CR, moc=True,
      cards=[('11%', 'Tín dụng 10 tháng 2026', 'TĂNG HƠN 11%'), ('10%', 'Huy động 10 tháng 2026', 'TĂNG GẦN 10%'), ('19%', 'Định hướng tín dụng cả năm', 'NÂNG TỪ 15 ĐẾN 16%')],
      say=("Cùng ngày, tại một diễn đàn đầu tư, các chuyên gia đưa ra ba con số. Mười tháng đầu năm, tín dụng tăng hơn mười một phần trăm, trong khi huy động chỉ tăng gần mười phần trăm. "
           "Và định hướng tăng trưởng tín dụng cả năm đã được nâng từ mười lăm, mười sáu phần trăm lên khoảng mười chín phần trăm. Cho vay chạy nhanh hơn tiền gửi, nên ngân hàng khó hạ lãi quá sâu.")),
 dict(k='giay', cap=('PHÉP TÍNH CỦA MỘT NGÂN HÀNG', 'KHÓ XUỐNG DƯỚI 10%'), cols=CR, moc=True, giay=dict(tieu_de='CHI PHÍ VỐN CỦA NGÂN HÀNG', so='Phát biểu tại diễn đàn ngày 12/11/2026', dau='LƯU Ý', dieu=[
        ('Lãi suất đô la Mỹ: khoảng 5%.', '5%'),
        ('Cộng phần bù tỷ giá: khoảng 2 điểm.', 'THÊM 2 ĐIỂM'),
        ('Cộng chi phí khác: khoảng 2,5 điểm.', 'THÊM 2,5 ĐIỂM'),
        ('Chi phí vốn khoảng 9,5%.', 'KHÓ DƯỚI 10%')]),
      say=("Lãnh đạo một ngân hàng cổ phần còn đưa ra phép tính. Lãi suất đô la Mỹ khoảng năm phần trăm, cộng phần bù tỷ giá chừng hai điểm, cộng chừng hai phẩy năm điểm chi phí khác. Chi phí vốn đã lên khoảng chín phẩy năm phần trăm. "
           "Với cấu trúc đó, theo ông, lãi suất cho vay khó xuống dưới mười phần trăm.")),
 dict(k='cards', anh=TP, cap=('BIÊN LÃI NGÂN HÀNG', 'ĐANG MỎNG DẦN'), cols=CC, moc=True,
      cards=[('3%', 'Biên lãi cuối năm 2025', 'NIM TOÀN NGÀNH'), ('2,5%', 'Biên lãi hiện nay', 'CÒN ÍT DƯ ĐỊA')],
      say=("Thêm một sức ép: theo chuyên gia Cấn Văn Lực, biên lãi ròng toàn ngành đã giảm từ khoảng ba phần trăm cuối năm 2025 xuống khoảng hai phẩy năm phần trăm. Nợ xấu lại đang tăng. Ngân hàng huy động năm nghìn tỷ mà một nghìn tỷ thành nợ xấu, thì bốn nghìn tỷ còn lại phải gánh cả tiền lãi trả người gửi. Khách hàng tốt đang trả thay cho khách hàng xấu.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='noti', ch='Chương 4 – Ai trả tiền cho đợt giảm lãi?', cap=('SỔ 500 TRIỆU ĐÁO HẠN', 'LÃI MỚI GIẢM 0,5 ĐIỂM'), cols=CR, moc=True, noti=dict(gio='19:40', ngay='Thứ Tư', items=[
        ('Ngân hàng', 'Tiết kiệm', 'Sổ 500.000.000đ đáo hạn ngày 20/11', X_),
        ('Tin tức', 'Lãi suất', 'Lãi tiền gửi mới kỳ hạn từ 6 tháng giảm ít nhất 0,5 điểm', R_)]),
      say=("Tối đó đến lượt chị Hạnh lo. Sổ năm trăm triệu của chị đáo hạn ngày hai mươi tháng mười một. Gửi lại là tiền gửi mới, đúng nhóm bị giảm lãi. "
           "Người gửi tiền chính là người góp phần trả cho đợt giảm lãi lần này.")),
 dict(k='bars', anh=CHO, cap=('LÃI TIẾT KIỆM', 'ĐANG SÁT LẠM PHÁT'), cols=CR, moc=True,
      bars=[('Lãi gửi 12 tháng', 5.4, GREEN, '5,4%'), ('Lạm phát T10', 5.09, RED, '5,09%'), ('Nếu giảm 0,5', 4.9, GOLD, '4,9%')],
      say=("Theo dữ liệu WiData, lãi huy động mười hai tháng bình quân nhóm ngân hàng nhà nước đang là năm phẩy bốn phần trăm. Trong khi chỉ số giá tiêu dùng tháng mười tăng năm phẩy không chín phần trăm so với cùng kỳ. "
           "Nếu lãi giảm thêm không phẩy năm điểm, còn bốn phẩy chín phần trăm, thấp hơn tốc độ tăng giá.")),
 dict(k='giay', cap=('NẾU LÃI CÒN 4,9%', 'TIỀN GỬI THUA TRƯỢT GIÁ'), cols=CR, moc=True, giay=dict(tieu_de='SỔ CHI TIÊU CỦA CHỊ HẠNH', so='Sổ tiết kiệm 500 triệu, em giả định', dau='ĐÃ TÍNH', dieu=[
        ('Lãi 5,4%: nhận 27 triệu.', '27 TRIỆU'),
        ('Giá cả tăng 5,09%: mất 25,45 triệu sức mua.', '25,45 TRIỆU'),
        ('Lãi 4,9%: nhận 24,5 triệu, thua trượt giá.', 'HỤT 0,95 TRIỆU')]),
      say=("Chị Hạnh tính ngay trên sổ chi tiêu. Lãi năm phẩy bốn phần trăm cho chị hai mươi bảy triệu. Giá cả tăng năm phẩy không chín phần trăm thì sức mua hao khoảng hai mươi lăm phẩy bốn lăm triệu. Chị chỉ thật sự giàu thêm hơn một triệu rưỡi. "
           "Nếu lãi còn bốn phẩy chín phần trăm, chị nhận hai mươi bốn phẩy năm triệu, hụt gần một triệu so với trượt giá.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='cards', ch='Chương 5 – Lịch sử và dòng chữ nhỏ', anh=TP, cap=('THỨ TỰ QUEN THUỘC', 'TIỀN GỬI GIẢM TRƯỚC'), cols=CC, moc=True,
      cards=[('4 lần', 'NHNN giảm lãi điều hành 2023', 'TÁI CẤP VỐN XUỐNG 4,5%'), ('0,5%', 'Huy động giảm ít nhất, 11/2026', 'NGƯỜI GỬI ĐI TRƯỚC'), ('0,2%', 'Vay mới giảm ít nhất', 'NGƯỜI VAY ĐI SAU')],
      say=("Chuyện này không mới. Trong năm 2023, Ngân hàng Nhà nước giảm lãi suất điều hành bốn lần, đưa lãi tái cấp vốn từ sáu phần trăm xuống bốn phẩy năm phần trăm. Cơ chế luôn theo một thứ tự: lãi tiền gửi giảm trước, khoản vay mới giảm sau, khoản vay cũ thả nổi chờ đến kỳ điều chỉnh. Tháng này cũng vậy.")),
 dict(k='giay', cap=('DÒNG CHỮ NHỎ', 'TRONG CÙNG BẢN TIN'), cols=CR, moc=True, giay=dict(tieu_de='GHI CHÚ ÍT AI ĐỌC', so='Theo báo chí ngày 11 và 12/11/2026', dau='LƯU Ý', dieu=[
        ('Có kỳ hạn, lãi thực nhận cao hơn biểu niêm yết tới 2,9 điểm.', 'ĐUA GOM TIỀN'),
        ('NHNN sẽ xử lý ngân hàng không thực hiện chỉ đạo.', 'CÓ GIÁM SÁT'),
        ('Lãi qua đêm 6,07% ngày 6/11, về 4,33% ngày 11/11.', 'ĐÃ HẠ NHIỆT')]),
      say=("Và đây là ba dòng chữ nhỏ. Một, cuộc đua gom tiền gửi vẫn âm ỉ: qua các gói cộng thêm, có kỳ hạn người gửi thực nhận cao hơn biểu công bố tới hai phẩy chín điểm. "
           "Hai, Ngân hàng Nhà nước nói sẽ xử lý nghiêm ngân hàng không thực hiện đúng chỉ đạo. Ba, lãi qua đêm liên ngân hàng từng lên sáu phẩy không bảy phần trăm ngày sáu tháng mười một, rồi về khoảng bốn phẩy ba phần trăm ngày mười một. Áp lực đã dịu, nhưng chưa biến mất.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='giay', ch='Chương 6 – Phép thử của anh chị', cap=('HỢP ĐỒNG VAY', 'ĐỌC ĐÚNG 3 DÒNG'), cols=CC, moc=True, giay=dict(tieu_de='HỢP ĐỒNG TÍN DỤNG CỦA ANH TUẤN', so='Các điều khoản em giả định', dau='ĐÃ ĐỌC', dieu=[
        ('Lãi thả nổi: lãi cơ sở cộng biên độ 3,5 điểm.', 'BIÊN ĐỘ 3,5'),
        ('Điều chỉnh lãi: 3 tháng một lần.', '3 THÁNG'),
        ('Phí trả nợ trước hạn năm thứ 2: 2%.', 'PHÍ 2%')]),
      say=("Đêm đó anh Tuấn lôi hợp đồng vay ra, đọc đúng ba dòng, em giả định để minh họa. Lãi thả nổi bằng lãi cơ sở cộng biên độ ba phẩy năm điểm. Điều chỉnh ba tháng một lần. Phí trả nợ trước hạn năm thứ hai là hai phần trăm. "
           "Nếu kỳ tới lãi cơ sở giảm không phẩy năm điểm, lãi của anh còn mười hai phẩy năm, mỗi tháng nhẹ đi khoảng năm trăm nghìn đồng. Có, nhưng còn xa con số hai phần trăm trên tiêu đề.")),
 dict(k='checklist', anh=TP, cap=('PHÉP THỬ', 'HAI CON SỐ CỦA NHÀ MÌNH'), cols=CC, moc=True,
      items=[('Lãi tiết kiệm trên 5,09%?', GREEN), ('Lãi vay của mình trên 10%?', GOLD), ('Kỳ điều chỉnh lãi tới là khi nào?', GOLD), ('Biên độ trong hợp đồng là mấy?', RED)],
      say=("Em gợi ý anh chị một phép thử nhỏ. Lấy sổ tiết kiệm ra: lãi có cao hơn năm phẩy không chín, tức lạm phát tháng mười, hay không? Nếu thấp hơn, tiền gửi chỉ đang giữ chỗ. "
           "Lấy hợp đồng vay ra: lãi trên hay dưới mười phần trăm, kỳ điều chỉnh tới là khi nào, biên độ là bao nhiêu. Biên độ là phần ngân hàng không giảm cho mình.")),
 dict(k='checklist', anh=HN, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI CUỐI NĂM'), cols=CC, moc=True,
      items=[('Lãi cơ sở có hạ ở kỳ tới?', GREEN), ('Lạm phát tháng 11 bao nhiêu?', GOLD), ('Qua đêm có vọt lại trên 6%?', GOLD)],
      say=("Từ nay tới cuối năm, có ba điều đáng theo dõi. Ngân hàng của anh chị có hạ lãi cơ sở ở kỳ tới không. Chỉ số giá tháng mười một có vượt lãi tiết kiệm không. Và liệu lãi qua đêm có vọt lại trên mức sáu phần trăm lần nữa. Muốn xem biên lãi và nợ xấu của từng ngân hàng qua các quý, anh chị có thể tra miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"GIẢM LÃI CÓ THẬT', 'CHỈ CHƯA TỚI LƯỢT MÌNH"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:10', mau=G_, msgs=[
        ('me', 'Mai anh gọi ngân hàng hỏi kỳ điều chỉnh tới'),
        ('Vợ', 'Sổ 500 triệu em chưa gửi lại vội, so lãi 3 nơi đã'),
        ('me', 'Giảm lãi có thật, chỉ là chưa tới lượt nhà mình')]),
      say=("Mười giờ tối, anh Tuấn nhắn cho vợ: mai anh gọi ngân hàng hỏi kỳ điều chỉnh tới. Chị Hạnh trả lời: sổ năm trăm triệu em chưa gửi lại vội, so lãi ba nơi đã. "
           "Anh gõ thêm một dòng: giảm lãi là có thật, chỉ là chưa tới lượt nhà mình.")),
 dict(k='end', cap=('LÃI CỦA ANH CHỊ', 'TRÊN HAY DƯỚI 5,09%?'), cols=CC,
      say=("Còn anh chị, lãi khoản vay hoặc sổ tiết kiệm của anh chị đang là bao nhiêu, cao hơn hay thấp hơn mức lạm phát năm phẩy không chín phần trăm? Kể cho em và mọi người ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Lãi Suất Giảm Ở 46 Ngân Hàng: Ai Được Giảm 2%, Vì Sao Khoản Vay Mua Nhà Vẫn 13%?'
MT = ("NÓNG: 46/46 ngân hàng đồng loạt giảm lãi huy động, mở đường giảm lãi cho vay 1,5–2 điểm (11/11/2026). Nhưng mức giảm 2% chỉ dành cho lĩnh vực sản xuất kinh doanh ưu tiên; "
      "lãi vay mua nhà thả nổi vẫn 13–15%, lãnh đạo ngân hàng cảnh báo lãi vay khó xuống dưới 10%, và năm 2027 cần huy động tới 6,4 triệu tỷ đồng vốn. Ai được lợi, ai chưa, và vì sao người gửi tiết kiệm là người góp phần trả tiền cho đợt giảm lãi.\n\n"
      "Nguồn số liệu:\n"
      "• 46/46 NHTM giảm ít nhất 0,5 điểm % lãi huy động kỳ hạn từ 6 tháng; NHNN yêu cầu giảm 0,5–1%/năm lãi tiền gửi mới từ 6 tháng để giảm 1,5–2% lãi cho vay lĩnh vực SXKD ưu tiên; lãi vay mới bình quân giảm 0,2–0,5%/năm so đầu tháng 10; hơn 20 ngân hàng có gói giảm 1,5–2%; lãi thực nhận ở một số kỳ hạn cao hơn biểu công bố tới 2,9 điểm %; ví dụ huy động 5.000 tỷ, 1.000 tỷ nợ xấu (MarketTimes 11/11/2026)\n"
      "• Lãi USD ~5% + bù tỷ giá ~2 + ~2,5 điểm → chi phí vốn ~9,5%, lãi cho vay khó xuống dưới 10% (PTGĐ TPBank); tín dụng 10 tháng 2026 tăng hơn 11%, huy động gần 10%; định hướng tín dụng nâng từ 15–16% lên ~19%; NIM toàn ngành ~3% cuối 2025 → ~2,5% hiện nay (TS Cấn Văn Lực) – Vietnam Investment Forum 2027, qua VietnamFinance và Nhà Đầu Tư 12/11/2026\n"
      "• Vốn đầu tư toàn xã hội 2027 cần 36–38% GDP, khoảng 6–6,4 triệu tỷ đồng (Thủ tướng báo cáo Quốc hội 12/11/2026, qua Vietnambiz)\n"
      "• Lãi vay mua nhà 8,5–11%/năm thời gian ưu đãi; thả nổi 13–15%/năm (Hà Nội Mới 11/11/2026); thả nổi = lãi cơ sở + biên độ 3–5%/năm (VietnamFinance 21/10/2026)\n"
      "• Đến 31/8/2026: tín dụng kinh doanh bất động sản +19,59%, cho vay mua nhà để ở +1,02% (TS Lê Hồng Hạnh, RMIT, qua VietnamFinance 26/10/2026)\n"
      "• Lãi huy động 12 tháng bình quân NHTM nhà nước 5,4% (12/11/2026); CPI 10/2026 +5,09% so cùng kỳ; lãi suất qua đêm liên ngân hàng 6,07% (6/11) và 4,33% (11/11) – WiData\n"
      "• Năm 2023 NHNN giảm lãi suất điều hành 4 lần, lãi tái cấp vốn từ 6% xuống 4,5% (NHNN)\n"
      "• Tự tính (giả định): vay 1,5 tỷ, 20 năm, trả góp đều: năm đầu 9% ≈ 13,50 triệu/tháng; 228 tháng còn lại ở 13% ≈ 17,44 triệu (thêm ≈ 3,94 triệu/tháng), ở 12,5% ≈ 16,93 triệu; "
      "sổ 500 triệu: lãi 5,4% = 27 triệu, trượt giá 5,09% ≈ 25,45 triệu; lãi 4,9% = 24,5 triệu (hụt ≈ 0,95 triệu)\n\n"
      "Video trước – NHNN mua USD giá 25.500, tiền đi đâu: https://chungkhoanhuynguyen.com/hoc/nhnn-bom-tien-kieu-moi-mua-usd-gia-25-500-co-the-toi-255-000-ty-tien.html\n"
      "Lãi suất tăng thì doanh nghiệp trả giá thế nào qua chi phí lãi vay: https://chungkhoanhuynguyen.com/hoc/lai-suat-tien-gui-6-38-hsg-nkg-frt-tra-gia-the-nao-qua-chi-phi-lai-vay.html\n"
      "Tra biên lãi, nợ xấu, lợi nhuận từng ngân hàng qua các quý: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật anh Tuấn, chị Hạnh, anh Long và các điều khoản hợp đồng là hư cấu; số liệu thị trường là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-13', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['lãi suất ngân hàng', 'giảm lãi suất', 'lãi suất vay mua nhà', 'lãi suất thả nổi', 'lãi suất tiết kiệm', '46 ngân hàng giảm lãi suất', 'lạm phát', 'vay mua nhà', 'tin nóng tài chính', 'vĩ mô Việt Nam'],
    bia_hook=['GIẢM LÃI 2%', 'SAO VẪN 13%?'], badge='NÓNG: 46 NGÂN HÀNG',
    bia_anh=NHA,
    bia_hook_b=['TIẾT KIỆM 5,4%', 'GIÁ TĂNG 5,09%'], badge_b='AI TRẢ TIỀN GIẢM LÃI?',
    bia_hook_c=['TRẢ THÊM 3,9TR', 'MỖI THÁNG???'], badge_c='VAY MUA NHÀ THẢ NỔI',
    fb_post=("46 ngân hàng giảm lãi suất – nhưng khoản vay mua nhà vẫn 13% 😳\n\n"
             "👉 Giảm 2% chỉ dành cho sản xuất kinh doanh ưu tiên\n👉 Vay mới bình quân mới giảm 0,2–0,5 điểm\n👉 Lãi tiết kiệm 12 tháng 5,4% đã sát lạm phát 5,09%\n\n"
             "Ai được lợi, ai chưa – xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 13/11: 46 ngân hàng giảm lãi, vay mua nhà vẫn 13 phần trăm (NV1B 13/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
cnt = Counter(c['k'] for c in S); dt = sum(cnt[k] for k in ('noti', 'chat', 'call', 'giay'))
print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dt/giay', dt, '%.0f%%' % (100 * dt / len(S)), 'tieu', len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
