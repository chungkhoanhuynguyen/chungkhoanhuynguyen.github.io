# -*- coding: utf-8 -*-
# NV1 16/11/2026 00:40 – VIDEO DÀI kênh chính, "câu hỏi lớn": 38,5 triệu tỷ cho 5 năm – tiền ở đâu ra, có phải từ sổ tiết kiệm của anh chị? (cặp reel RV1611VON)
# Lý do chọn: data/view/xu_huong.md tuần tới 15/11: "Việt Nam tất tay cho tham vọng Hạ Tầng?" ~82 nghìn view, "2000 tỷ USD kéo VN vào khủng hoảng…" ~79 nghìn,
#   "Việt Nam đang nợ ai? Tiền đang đi đâu?" ~204 nghìn (tuần trước). Tin 12–13/11: Quốc hội chất vấn Thủ tướng về 38,5 triệu tỷ (VietnamFinance 12/11, Vietnambiz 13/11).
#   Kênh 7 ngày chưa làm "nguồn vốn/tiết kiệm" (đã làm: nợ công 14/11, GDP-lương 16/11, xuất khẩu 17/11, Thái Lan 18/11, nhà đất 19/11).
# Nguồn và SỐ TỰ TÍNH:
#  - VnBusiness 22/10/2026 (TS Nguyễn Đức Hiển, Phó Trưởng ban Chính sách, Chiến lược Trung ương): nhu cầu vốn đầu tư 2026–2030 khoảng 38,5 triệu tỷ;
#    Nhà nước 12,5 + ngoài nhà nước 20,4 + FDI 5,6 = 38,5 (đã cộng lại khớp). Khoảng 80% vốn huy động của ngân hàng kỳ hạn dưới 12 tháng.
#    TS Nguyễn Thị Ngọc Hà: tới 30/9 tín dụng +10,9% so đầu năm, huy động +9,8%. TS Cấn Văn Lực: từ 2020 tín dụng ngân hàng hơn 50% nguồn vốn nền kinh tế,
#    cổ phiếu + trái phiếu khoảng 14–15%; nếu tín dụng tăng 15–16%/năm, GDP danh nghĩa khoảng 10%, tín dụng/GDP có thể 180% năm 2030. Mục tiêu thị trường vốn 28–30% năm 2030.
#  - VietnamFinance 12/11/2026 (chất vấn tại Quốc hội): đầu tư công trung hạn 2026–2030 khoảng 8,22 triệu tỷ (Nghị quyết 27), khoảng 1/5 tổng nhu cầu, gần 30 triệu tỷ phải từ nguồn khác.
#  - WiData (Cục Thống kê, NHNN): GDP danh nghĩa 4 quý tới quý 3/2026 = 14.056.614 tỷ (79958); tổng tín dụng 8/2026 = 20.489.434 tỷ (75931);
#    vốn đầu tư toàn xã hội theo quý (82917, nghìn tỷ): Q4/2025 1.445,93 + Q1/2026 748,30 + Q2 1.069,54 + Q3 1.291,24 = 4.555,0 nghìn tỷ ≈ 4,56 triệu tỷ;
#    tín dụng so cùng kỳ 8/2026 +17,38% (75847), tổng tiền gửi +13,65% (265963), tiền gửi dân cư +12,97% (265981);
#    lãi huy động 12 tháng NHTM Nhà nước 5,4% (202886, 13/11/2026); CPI 10/2026 so cùng kỳ +5,09% (75701); GDP 9T/2026 +9,01% (80126).
#  - Vietnamnet 23/6/2025: tín dụng/GDP cuối 2024 khoảng 134%; tín dụng 2007 tăng 53%, 2009 36%; lạm phát 2008 gần 20%; CPI bình quân 2011 18,6%.
#  - TỰ TÍNH: 38,5/5 = 7,7 triệu tỷ mỗi năm; 7,7/14,06 = 55% GDP danh nghĩa; 7,7/4,56 = 1,69 lần mức 4 quý gần nhất;
#    tín dụng/GDP = 20,49/14,06 = 146%; lãi thật = 5,4 − 5,09 = 0,31 điểm %.
#  - GIẢ ĐỊNH minh hoạ (nhà chị Hạnh): sổ tiết kiệm 800 triệu kỳ hạn 12 tháng lãi 5,4% → lãi 43,2 triệu/năm; giá cả tăng 5,09% → sức mua mất 40,7 triệu
#    (800 × 5,09% = 40,72) → còn lại khoảng 2,5 triệu/năm.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261116_0040'
KEY = 'CH2011VON'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
MET = 'ov:Ho Chi Minh City Metro Line 1||Ho Chi Minh City Metro'
CAU = 'ov:Nhat Tan Bridge||Nhat Tan Bridge Hanoi'
SGD = 'ov:Ho Chi Minh City Stock Exchange||Bitexco Financial Tower'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('CẦN 38,5 TRIỆU TỶ', 'TIỀN Ở ĐÂU RA?'), cols=CR, noti=dict(gio='20:15', ngay='Thứ Năm', items=[
        ('Tin tức', 'VietnamFinance', 'Cần 38,5 triệu tỷ đồng vốn cho 5 năm tới', V_),
        ('Zalo', 'Anh Phong', 'Công trường cao tốc tăng ca tới Tết em ơi', G_),
        ('Ngân hàng', 'Tiết kiệm', 'Sổ 800 triệu đáo hạn ngày 20/11, mời gửi tiếp', X_)]),
      say=("Ba mươi tám phẩy năm triệu tỷ đồng. Đó là số vốn Việt Nam cần từ năm 2026 đến năm 2030 để tăng trưởng hai con số. Con số này vừa được nêu ở phiên chất vấn Thủ tướng tại Quốc hội tuần này. "
           "Tối nay chị Hạnh, nhân viên văn phòng ở Đà Nẵng, đọc tin đó ngay lúc chồng chị, anh Phong, kỹ sư một công trường cao tốc, nhắn về: tăng ca tới Tết. "
           "Cùng lúc, ngân hàng nhắc cuốn sổ tiết kiệm tám trăm triệu của chị sắp đáo hạn. Ba tin nhắn tưởng chẳng liên quan, nhưng thật ra là cùng một dòng tiền.")),
 dict(k='bignum', anh=MET, cap=('MỖI NĂM 7,7 TRIỆU TỶ', 'BẰNG 55% GDP'), cols=CR, value=38.5, fmt='{:,.1f}', unit=' TRIỆU TỶ', top='VỐN CẦN CHO 2026–2030', sub='Phó Trưởng ban Chính sách, Chiến lược TƯ', col=RED,
      say=("Chia đều ra, mỗi năm cần khoảng bảy phẩy bảy triệu tỷ đồng, bằng năm mươi lăm phần trăm toàn bộ giá trị nền kinh tế làm ra trong một năm. "
           "Trong bốn quý gần nhất, cả nước mới đầu tư được khoảng bốn phẩy năm sáu triệu tỷ. Tức là phải bỏ vốn gấp khoảng một phẩy bảy lần hiện nay, và giữ như vậy suốt cả giai đoạn. Em tự tính, cách tính có trong mô tả. "
           "Câu hỏi là: tiền đó ở đâu ra, và có bao nhiêu phần đang nằm trong túi của anh chị?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='cards', ch='Chương 1 – 38,5 triệu tỷ chia ra sao?', anh=CAU, cap=('NHÀ NƯỚC CHỈ GÁNH 1/3', 'TƯ NHÂN PHẢI GÁNH HƠN NỬA'), cols=CC, moc=True,
      cards=[('12,5 triệu tỷ', 'Vốn khu vực Nhà nước', 'Khoảng một phần ba'), ('20,4 triệu tỷ', 'Vốn ngoài nhà nước', 'Phần lớn nhất'), ('5,6 triệu tỷ', 'Vốn đầu tư nước ngoài', 'Vốn FDI')],
      say=("Ba mươi tám phẩy năm triệu tỷ được chia làm ba phần. Khu vực Nhà nước khoảng mười hai phẩy năm triệu tỷ. Doanh nghiệp nước ngoài khoảng năm phẩy sáu triệu tỷ. "
           "Phần lớn nhất, hai mươi phẩy bốn triệu tỷ, là của khu vực ngoài nhà nước: doanh nghiệp tư nhân, hộ kinh doanh, và cả những gia đình như nhà chị Hạnh.")),
 dict(k='giay', cap=('ĐẦU TƯ CÔNG 8,22 TRIỆU TỶ', 'CÒN GẦN 30 TRIỆU TỶ PHẢI ĐI VAY'), cols=CR, moc=True, giay=dict(tieu_de='CHẤT VẤN TẠI QUỐC HỘI, 12/11/2026', so='VietnamFinance 12/11/2026', dau='ĐÃ NÊU', dieu=[
        ('Tổng vốn cần cho 5 năm', '38,5 TRIỆU TỶ'),
        ('Đầu tư công trung hạn đã duyệt', '8,22 TRIỆU TỶ'),
        ('Phần đầu tư công gánh được', 'KHOẢNG 1/5'),
        ('Còn lại phải huy động', 'GẦN 30 TRIỆU TỶ')]),
      say=("Tại phiên chất vấn, một đại biểu chỉ ra: kế hoạch đầu tư công trung hạn đã duyệt khoảng tám phẩy hai triệu tỷ, chỉ bằng khoảng hai mươi mốt phần trăm tổng nhu cầu. "
           "Khoảng ba mươi phẩy ba triệu tỷ còn lại phải huy động từ nơi khác. Và đại biểu nói thêm một câu rất quan trọng: nguồn vốn trung và dài hạn của nền kinh tế vẫn phụ thuộc chủ yếu vào ngân hàng.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='chat', ch='Chương 2 – Tiền xây cao tốc đến từ đâu?', cap=('"TIỀN XÂY CAO TỐC', 'CÓ PHẦN SỔ TIẾT KIỆM CỦA EM?"'), cols=CR, moc=True, chat=dict(ten='Anh Phong', tv='Đang hoạt động', gio='20:40', mau=G_, msgs=[
        ('Anh Phong', 'Nhà thầu bên anh vay ngân hàng để làm gói này'),
        ('me', 'Ngân hàng lấy tiền đâu cho vay?'),
        ('Anh Phong', 'Thì từ tiền gửi của những người như em'),
        ('me', 'Vậy cao tốc có phần sổ tiết kiệm của em à?')]),
      say=("Chị Hạnh hỏi chồng gói thầu cao tốc lấy tiền đâu ra. Anh Phong kể nhà thầu của anh vay ngân hàng để làm. Chị hỏi tiếp: vậy ngân hàng lấy tiền đâu cho vay. "
           "Anh trả lời gọn: thì từ tiền gửi của những người như em. Chị Hạnh khựng lại: vậy con đường anh đang làm có cả tiền trong sổ tiết kiệm của em sao?")),
 dict(k='cards', anh=HN, cap=('NGÂN HÀNG GÁNH HƠN 50%', 'CỔ PHIẾU, TRÁI PHIẾU CHỈ 15%'), cols=CR, moc=True,
      cards=[('Trên 50%', 'Vốn nền kinh tế từ ngân hàng', 'Từ năm 2020 tới nay'), ('14 đến 15%', 'Từ cổ phiếu và trái phiếu', 'Chưa tính trái phiếu Chính phủ'), ('28 đến 30%', 'Mục tiêu thị trường vốn', 'Đến năm 2030')],
      say=("Đúng là như vậy. Theo chuyên gia kinh tế trưởng một ngân hàng lớn, từ năm 2020 tới nay, hơn năm mươi phần trăm nguồn vốn của nền kinh tế đi qua ngân hàng. "
           "Cổ phiếu và trái phiếu doanh nghiệp chỉ đáp ứng khoảng mười bốn đến mười lăm phần trăm. Mục tiêu là đến năm 2030, thị trường vốn phải gánh hai mươi tám đến ba mươi phần trăm. "
           "Còn bây giờ, phần lớn vẫn là tiền gửi tiết kiệm của người dân, được ngân hàng cho vay lại.")),
 dict(k='bignum', anh=HN, cap=('80% TIỀN GỬI KỲ HẠN NGẮN', 'NHƯNG CHO VAY XÂY DỰNG CẢ CHỤC NĂM'), cols=CR, moc=True, value=80, fmt='{:,.0f}', unit='%', top='TIỀN GỬI NGÂN HÀNG', sub='có kỳ hạn dưới 12 tháng – VnBusiness 22/10/2026', col=RED,
      say=("Và đây là cú lật thứ nhất. Khoảng tám mươi phần trăm số tiền ngân hàng huy động có kỳ hạn dưới mười hai tháng, giống cuốn sổ của chị Hạnh. "
           "Nhưng một con đường cao tốc, một khu đô thị, cần vốn mười năm, hai mươi năm. Ngân hàng đang lấy tiền ngắn hạn của người dân để cho vay dài hạn. "
           "Chừng nào người gửi vẫn tin và vẫn gửi tiếp, mọi thứ chạy êm. Nhưng cái giá của sự êm ấy, ai đang trả?")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='giay', ch='Chương 3 – Cuốn sổ 800 triệu của chị Hạnh', cap=('LÃI 43 TRIỆU MỘT NĂM', 'NHƯNG GIÁ CẢ ĂN MẤT 41 TRIỆU'), cols=CR, moc=True, giay=dict(tieu_de='SỔ TIẾT KIỆM NHÀ CHỊ HẠNH', so='Em giả định, kỳ hạn 12 tháng', dau='TỰ TÍNH', dieu=[
        ('Tiền gửi', '800 TR'),
        ('Lãi 5,4% một năm', '43,2 TR'),
        ('Giá cả tăng 5,09%, sức mua mất', '40,7 TR'),
        ('Thật sự giàu thêm', '2,5 TR')]),
      say=("Chị Hạnh mở cuốn sổ. Số này em giả định để minh hoạ: tám trăm triệu, kỳ hạn mười hai tháng, lãi năm phẩy bốn phần trăm, bằng mức của các ngân hàng lớn hiện nay. "
           "Một năm được bốn mươi ba triệu hai trăm nghìn tiền lãi. Nghe khá ổn. Nhưng giá cả tháng mười tăng năm phẩy không chín phần trăm so với cùng kỳ. "
           "Tám trăm triệu bị giá cả ăn mất khoảng bốn mươi triệu bảy trăm nghìn sức mua. Sau một năm, chị thật sự giàu thêm chỉ khoảng hai triệu rưỡi.")),
 dict(k='bignum', anh=TP, cap=('LÃI THẬT CỦA SỔ TIẾT KIỆM', 'CHỈ CÒN 0,3%'), cols=CR, moc=True, value=0.31, fmt='{:,.2f}', unit='%', top='LÃI SAU KHI TRỪ GIÁ CẢ', sub='5,4% trừ CPI 5,09% – em tự tính', col=RED,
      say=("Lãi suất năm phẩy bốn, trừ giá cả tăng năm phẩy không chín, lãi thật còn khoảng không phẩy ba phần trăm. "
           "Đó là cú lật thứ hai. Người gửi tiết kiệm đang góp vốn cho cả nền kinh tế chạy, nhưng phần thưởng thật gần như bằng không. "
           "Trong khi đó, nhu cầu vay vẫn tăng nhanh hơn tiền gửi rất nhiều.")),
 dict(k='cards', anh=HN, cap=('TÍN DỤNG CHẠY NHANH HƠN', 'TIỀN GỬI'), cols=CR, moc=True,
      cards=[('+17,38%', 'Tín dụng so cùng kỳ', 'Tháng 8/2026'), ('+13,65%', 'Tiền gửi so cùng kỳ', 'Tháng 8/2026'), ('+10,9%', 'Tín dụng từ đầu năm', 'Huy động chỉ +9,8%')],
      say=("Tới tháng tám, tín dụng tăng mười bảy phẩy ba tám phần trăm so với cùng kỳ, còn tiền gửi chỉ tăng mười ba phẩy sáu lăm phần trăm. Tính từ đầu năm tới cuối tháng chín, tín dụng tăng mười phẩy chín phần trăm, huy động chỉ chín phẩy tám. "
           "Cho vay chạy nhanh hơn tiền gửi nghĩa là ngân hàng ngày càng thiếu nguồn. Và khi thiếu tiền, ngân hàng chỉ có hai cách: trả lãi cao hơn để giữ người gửi, hoặc bớt cho vay.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='call', ch='Chương 4 – Lịch sử từng lặp lại', cap=('"NĂM 2011 MẸ GỬI LÃI 14%', 'MÀ VẪN THẤY NGHÈO ĐI"'), cols=CR, moc=True, call=dict(ten='Mẹ', phu='Gọi thoại', mau=V_, loi=[
        'Hồi đó lãi cao lắm mà giá cả còn tăng nhanh hơn', 'Tiền gửi nhiều năm mua được ít đồ hơn trước']),
      say=("Chị Hạnh gọi cho mẹ. Mẹ chị kể, quanh năm 2011, ngân hàng trả lãi tới mười bốn phần trăm, nghe thì rất cao. "
           "Nhưng giá cả còn tăng nhanh hơn, tiền gửi bao nhiêu năm, rút ra mua được ít đồ hơn trước. Mẹ chị không biết số liệu, nhưng mẹ nhớ cảm giác ấy rất rõ.")),
 dict(k='giay', cap=('2007 TÍN DỤNG TĂNG 53%', 'RỒI LẠM PHÁT GẦN 20%'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ TỪ NĂM 2007 ĐẾN NĂM 2011', so='Vietnamnet 23/6/2025', dau='ĐÃ XẢY RA', dieu=[
        ('Tín dụng năm 2007', 'TĂNG 53%'),
        ('Lạm phát năm 2008', 'GẦN 20%'),
        ('Tín dụng năm 2009', 'TĂNG 36%'),
        ('Giá cả bình quân năm 2011', 'TĂNG 18,6%')]),
      say=("Những gì mẹ chị nhớ có trong số liệu. Năm 2007, tín dụng tăng năm mươi ba phần trăm. Một năm sau, lạm phát lên gần hai mươi phần trăm. "
           "Năm 2009, tín dụng lại tăng ba mươi sáu phần trăm, và đến năm 2011, giá cả bình quân tăng mười tám phẩy sáu phần trăm. "
           "Bài học của giai đoạn đó: khi tiền vay ra quá nhanh so với sức làm ra của nền kinh tế, giá cả sẽ tăng. Và người giữ tiền mặt, giữ sổ tiết kiệm là người trả giá cuối cùng.")),
 dict(k='bars', anh=HN, cap=('TÍN DỤNG SO VỚI GDP', 'TỪ 134% LÊN 146%'), cols=CR, moc=True, bars=[('Cuối năm 2024', 134, GOLD, '134%'), ('Hiện nay', 146, RED, '146%'), ('2030 nếu như cũ', 180, RED, '180%')],
      say=("Bây giờ thì sao? Tổng tín dụng so với giá trị nền kinh tế cuối năm 2024 khoảng một trăm ba mươi tư phần trăm. Em tự tính theo số mới nhất, hiện nay khoảng một trăm bốn mươi sáu phần trăm. "
           "Một chuyên gia cảnh báo: tín dụng cứ tăng mười lăm đến mười sáu phần trăm mỗi năm, trong khi kinh tế danh nghĩa chỉ tăng khoảng mười phần trăm. Khi đó con số này có thể lên một trăm tám mươi phần trăm vào năm 2030.")),
 dict(k='checklist', anh=TP, cap=('BÂY GIỜ VÀ NĂM 2007', 'GIỐNG 2, KHÁC 2'), cols=CR, moc=True,
      items=[('Tín dụng tăng nhanh: giống', RED),
             ('Vay ngắn, cho vay dài: giống', RED),
             ('Giá cả 5%, không phải 20%', GREEN),
             ('Có mục tiêu thị trường vốn', GREEN)],
      say=("Đặt hai thời điểm cạnh nhau cho công bằng. Giống thứ nhất: tín dụng tăng nhanh hơn tiền gửi và nhanh hơn kinh tế. Giống thứ hai: tiền ngắn hạn vẫn đang nuôi dự án dài hạn. "
           "Khác thứ nhất: giá cả hiện tăng khoảng năm phần trăm, chưa phải hai mươi phần trăm. Khác thứ hai: lần này có mục tiêu rõ là kéo thị trường vốn lên gánh khoảng ba mươi phần trăm. "
           "Nghĩa là rủi ro đã được gọi tên. Chưa thành cơn bão, nhưng chưa, không có nghĩa là không thể.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='chat', ch='Chương 5 – Tiền nhà mình nên đứng ở đâu?', cap=('"MÌNH GÓP VỐN CHO CẢ NƯỚC', 'THÌ CŨNG PHẢI ĐƯỢC TRẢ CÔNG"'), cols=CC, moc=True, chat=dict(ten='Anh Phong', tv='Đang hoạt động', gio='22:10', mau=G_, msgs=[
        ('me', 'Sổ 800 triệu đáo hạn, gửi tiếp hết hay sao anh?'),
        ('Anh Phong', 'Gửi tiếp thì an toàn, nhưng lãi thật gần bằng 0'),
        ('me', 'Mình góp vốn cho cả nước thì cũng phải được trả công'),
        ('Anh Phong', 'Chia ra, đừng để một chỗ')]),
      say=("Chị Hạnh nhắn chồng: sổ tám trăm triệu sắp đáo hạn, gửi tiếp hết hay sao anh. Anh Phong đáp: gửi tiếp thì an toàn, nhưng lãi thật gần bằng không. "
           "Chị nhắn: mình góp vốn cho cả nước thì cũng phải được trả công chứ. Anh trả lời: vậy chia ra, đừng để một chỗ.")),
 dict(k='cards', anh=SGD, cap=('3 CON ĐƯỜNG CỦA ĐỒNG TIỀN', 'MỖI ĐƯỜNG MỘT RỦI RO'), cols=CC, moc=True,
      cards=[('5,4%', 'Gửi ngân hàng 12 tháng', 'An toàn, lãi thật thấp'), ('Cổ phiếu', 'Làm chủ một phần doanh nghiệp', 'Lời lỗ theo doanh nghiệp'), ('Trái phiếu', 'Cho doanh nghiệp vay', 'Phải xem kỹ ai vay')],
      say=("Có ba con đường chính để đồng tiền nhà mình tham gia vào ba mươi tám phẩy năm triệu tỷ kia. Một: gửi ngân hàng như hiện nay, an toàn nhất nhưng lãi thật thấp. "
           "Hai: cổ phiếu, tức là trở thành đồng sở hữu doanh nghiệp đang hưởng lợi từ làn sóng đầu tư, lời lỗ đi theo kết quả kinh doanh của doanh nghiệp đó. "
           "Ba: trái phiếu, tức là cho doanh nghiệp vay, lãi cao hơn nhưng phải xem kỹ ai đang vay và lấy gì trả. Không có con đường nào vừa lãi cao vừa không rủi ro.")),
 dict(k='chat', cap=('KẾ HOẠCH NHÀ CHỊ HẠNH', 'CHIA KỲ HẠN, CHIA KÊNH'), cols=CC, moc=True, chat=dict(ten='Anh Phong', tv='Đang hoạt động', gio='22:35', mau=G_, msgs=[
        ('me', 'Giữ 6 tháng chi tiêu ở sổ ngắn hạn'),
        ('Anh Phong', 'Phần còn lại chia vài kỳ hạn'),
        ('me', 'Một phần nhỏ học dần kênh khác'),
        ('Anh Phong', 'Mỗi năm xem lại lãi thật một lần')]),
      say=("Cuối cùng hai vợ chồng thống nhất: giữ đủ sáu tháng chi tiêu ở sổ ngắn hạn để không bao giờ phải rút gấp. Phần còn lại chia ra vài kỳ hạn khác nhau. "
           "Một khoản nhỏ, chị dành để học dần một kênh khác, không dồn hết một lần. Và mỗi năm, hai vợ chồng ngồi lại tính lãi thật một lần.")),
 dict(k='checklist', anh=TP, cap=('PHÉP THỬ CỦA ANH CHỊ', 'LÃI THẬT NHÀ MÌNH BAO NHIÊU?'), cols=CC, moc=True,
      items=[('Âm: tiền đang nghèo đi', RED),
             ('Từ 0 đến 2 điểm: giữ được giá', GOLD),
             ('Trên 2 điểm: đang được trả công', GREEN)],
      say=("Và đây là phép thử anh chị làm được ngay tối nay. Lấy lãi suất trung bình các khoản tiền nhà mình đang để, trừ đi mức tăng giá cả, hiện khoảng năm phẩy một phần trăm. "
           "Nếu ra số âm, tiền nhà mình đang nghèo đi. Từ không đến hai điểm phần trăm, tiền chỉ đang giữ được giá. Trên hai điểm, đồng tiền của anh chị đang thật sự được trả công. "
           "Đây là mốc em đặt để tự soi, không phải quy định.")),
 dict(k='checklist', ch='Chương 6 – Theo dõi gì để biết sớm?', anh=SGD, cap=('3 CON SỐ CẦN THEO DÕI', 'MỖI THÁNG MỘT LẦN'), cols=CC, moc=True,
      items=[('Giá cả tăng bao nhiêu', GOLD),
             ('Tín dụng so với tiền gửi', RED),
             ('Lãi gửi 12 tháng', GOLD)],
      say=("Muốn biết sớm dòng tiền ba mươi tám phẩy năm triệu tỷ có đang làm khổ người gửi tiết kiệm hay không, em gợi ý theo dõi ba con số mỗi tháng. "
           "Một: giá cả tăng bao nhiêu so với cùng kỳ. Hai: tín dụng có tiếp tục chạy nhanh hơn tiền gửi không. Ba: lãi gửi mười hai tháng của các ngân hàng lớn. "
           "Riêng lợi nhuận từng quý của các doanh nghiệp xây dựng, vật liệu và ngân hàng trên sàn, anh chị xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn từ công trường', cap=('"ĐƯỜNG ANH LÀM CÓ TIỀN CỦA EM', 'THÌ EM CŨNG PHẢI ĐƯỢC LỢI"'), cols=CC, moc=True, chat=dict(ten='Anh Phong', tv='Đang hoạt động', gio='23:30', mau=G_, msgs=[
        ('Anh Phong', 'Đường anh làm có một phần tiền của em đấy'),
        ('me', 'Thì em cũng phải được lợi từ nó chứ'),
        ('Anh Phong', 'Ừ, từ giờ mình để tiền làm việc cho mình')]),
      say=("Gần nửa đêm, anh Phong nhắn từ công trường: con đường anh làm có cả tiền của em trong đó đấy. Chị Hạnh trả lời: thì em cũng phải được lợi từ nó chứ. "
           "Con số ba mươi tám phẩy năm triệu tỷ trên báo nghe rất xa xôi. Nhưng trong đó có tiền tiết kiệm của rất nhiều gia đình như nhà chị Hạnh. Câu hỏi chỉ là: mình góp vốn một cách thụ động, hay có tính toán.")),
 dict(k='end', cap=('38,5 TRIỆU TỶ', 'TIỀN NHÀ ANH CHỊ Ở ĐÂU?'), cols=CC,
      say=("Còn anh chị thì sao: lãi thật của tiền nhà mình đang âm, đang hòa, hay đang được trả công? Kể cho em và mọi người ở phần bình luận nhé. "
           "Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Cần 38,5 Triệu Tỷ Cho 5 Năm: Tiền Ở Đâu Ra? Sổ Tiết Kiệm Của Bạn Đang Góp Vốn – Mà Lãi Thật Chỉ 0,3%'
MT = ("Việt Nam cần khoảng 38,5 triệu tỷ đồng vốn đầu tư cho 2026–2030, mỗi năm khoảng 7,7 triệu tỷ, bằng 55% GDP. Đầu tư công chỉ gánh khoảng 1/5, phần còn lại phần lớn đi qua ngân hàng – tức là từ tiền gửi tiết kiệm của người dân. "
      "Lãi gửi 12 tháng 5,4%, giá cả tăng 5,09%: lãi thật chỉ còn khoảng 0,3%. Lịch sử 2007–2011 cho thấy điều gì khi tín dụng chạy nhanh hơn tiền gửi? Câu chuyện của chị Hạnh, anh Phong và phép thử lãi thật cho chính gia đình anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• VnBusiness 22/10/2026 (hội thảo \"Tháo gỡ điểm nghẽn, khơi thông nguồn vốn\"): nhu cầu vốn đầu tư 2026–2030 khoảng 38,5 triệu tỷ (Nhà nước 12,5; ngoài nhà nước 20,4; FDI 5,6); khoảng 80% vốn huy động ngân hàng kỳ hạn dưới 12 tháng; đến 30/9/2026 tín dụng +10,9% so đầu năm, huy động +9,8%; tín dụng ngân hàng hơn 50% nguồn vốn nền kinh tế từ 2020, cổ phiếu và trái phiếu khoảng 14–15%; cảnh báo tín dụng/GDP có thể 180% năm 2030; mục tiêu thị trường vốn 28–30% vào 2030\n"
      "• VietnamFinance 12/11/2026 (phiên chất vấn Thủ tướng tại Quốc hội): đầu tư công trung hạn 2026–2030 khoảng 8,22 triệu tỷ, khoảng 1/5 tổng nhu cầu; gần 30 triệu tỷ phải huy động từ nguồn khác\n"
      "• Cục Thống kê, Ngân hàng Nhà nước (qua WiData): GDP danh nghĩa 4 quý tới quý 3/2026 khoảng 14,06 triệu tỷ; tổng tín dụng 8/2026 khoảng 20,49 triệu tỷ; vốn đầu tư toàn xã hội quý 4/2025 đến quý 3/2026 cộng lại khoảng 4,56 triệu tỷ; tín dụng 8/2026 +17,38% so cùng kỳ, tổng tiền gửi +13,65%; lãi huy động 12 tháng ngân hàng thương mại Nhà nước 5,4% (13/11/2026); CPI tháng 10/2026 +5,09% so cùng kỳ\n"
      "• Vietnamnet 23/6/2025: tín dụng/GDP cuối 2024 khoảng 134%; tín dụng 2007 tăng 53%, 2009 tăng 36%; lạm phát 2008 gần 20%; CPI bình quân 2011 18,6%; trần lãi huy động năm 2011 là 14% (Thông tư 02/2011/TT-NHNN)\n"
      "• Tự tính: 38,5/5 = 7,7 triệu tỷ mỗi năm; 7,7/14,06 = 55% GDP; 7,7/4,56 = 1,7 lần; tín dụng/GDP = 20,49/14,06 = 146%; lãi thật = 5,4% − 5,09% = 0,31 điểm %\n"
      "• Sổ tiết kiệm nhà chị Hạnh là giả định minh hoạ: 800 triệu × 5,4% = 43,2 triệu tiền lãi; 800 triệu × 5,09% = 40,7 triệu sức mua mất đi; còn khoảng 2,5 triệu\n\n"
      "Tra lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật chị Hạnh, anh Phong là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-20', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['38,5 triệu tỷ', 'vốn đầu tư', 'đầu tư công', 'hạ tầng Việt Nam', 'lãi suất tiết kiệm', 'lãi suất thực', 'tín dụng', 'lạm phát', 'kinh tế Việt Nam', 'vĩ mô'],
    bia_hook=['CẦN 38,5', 'TRIỆU TỶ???'], badge='VỐN CHO 5 NĂM TỚI',
    bia_anh='Ho Chi Minh City skyline night||Hanoi skyline night',
    bia_hook_b=['LÃI 5,4%', 'THẬT CÒN 0,3%'], badge_b='SỔ TIẾT KIỆM CỦA BẠN',
    bia_hook_c=['TÍN DỤNG', '146% GDP'], badge_c='TÍN DỤNG SO VỚI GDP',
    reel_hook='CẦN 38,5 TRIỆU TỶ|TIỀN Ở ĐÂU RA???',
    fb_post=("Việt Nam cần 38,5 triệu tỷ đồng vốn cho 5 năm tới 🏗️\n\n👉 Đầu tư công chỉ gánh khoảng 1/5\n👉 Hơn 50% vốn nền kinh tế đi qua ngân hàng – tức là từ sổ tiết kiệm của chúng ta\n"
             "👉 Lãi gửi 12 tháng 5,4%, giá cả tăng 5,09%: lãi thật chỉ còn 0,3%\n\nTiền nhà anh chị đang được trả công hay đang nghèo đi?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: 38,5 triệu tỷ cho 5 năm, tiền ở đâu ra (NV1 16/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
CX = {'noti': ('tò mò', 'chuông thông báo'), 'chat': ('tâm sự', 'tiếng gõ phím'), 'call': ('trầm, lo', 'chuông gọi'), 'giay': ('căng', 'lật giấy'),
      'bignum': ('sốc', 'trống nhấn'), 'cards': ('suy nghĩ', 'nền phố'), 'bars': ('so sánh', 'nền phố'), 'checklist': ('quyết tâm', 'tick'), 'text': ('ngộ ra', 'nền nhẹ'), 'end': ('mở', 'nhạc kết')}
with open(LO + '/phan_canh.md', 'w', encoding='utf-8') as f:
    f.write('| # | loại | hình (thẻ form cũ) | cảm xúc | tiếng động |\n|---|---|---|---|---|\n')
    for i, c in enumerate(S, 1):
        cx = CX.get(c['k'], ('', '')); f.write('| %d | the/%s | %s | %s | %s |\n' % (i, c['k'], ' / '.join(c.get('cap', ('', ''))), cx[0], cx[1]))
from collections import Counter
cnt = Counter(c['k'] for c in S); dt = sum(cnt[k] for k in ('chat', 'noti', 'call', 'giay'))
print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dien thoai/giay %d/%d' % (dt, len(S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
