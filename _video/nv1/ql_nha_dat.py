# -*- coding: utf-8 -*-
# NV1 15/11/2026 00:40 – VIDEO DÀI kênh chính, "câu hỏi lớn": 87% tài sản gia đình Việt nằm ở nhà đất – có đi vết xe Trung Quốc? (cặp reel RV1511ND)
# Lý do chọn: data/view/xu_huong.md tuần tới 14/11: "China: thời bất động sản tạo tỷ phú đã hết – còn Việt Nam?" ~82 nghìn view,
#   "Siết phân lô bán nền, giới đầu cơ vỡ trận" ~59 nghìn, PEWPEW bất động sản ~232 nghìn; tin 12–13/11 (Vietnambiz, VnBusiness): 87% tài sản gia đình Việt ở BĐS.
#   Kênh 7 ngày chưa làm BĐS ở dạng câu hỏi lớn (đã làm: nợ công 14/11, GDP-lương 16/11, xuất khẩu 17/11, Thái Lan 18/11, lãi suất 13/11).
# Nguồn và SỐ TỰ TÍNH:
#  - Vietnambiz 13/11/2026, VnBusiness 12/11/2026: khoảng 87% tài sản của các gia đình Việt Nam nằm trong bất động sản (khảo sát do ông Duc Tran, VIG, dẫn tại Vietnam Investment Forum).
#  - The Real Deal 7/7/2026: nhà ở khoảng 70% tài sản hộ gia đình thành thị Trung Quốc; giá nhà mới 70 thành phố giảm tháng thứ 35 liên tiếp (5/2026, -3,5% so cùng kỳ);
#    bất động sản lấy đi khoảng 2 điểm % tăng trưởng GDP mỗi năm 2024–2025; Evergrande bị thanh lý năm 2024 với khoảng 300 tỷ USD nợ.
#  - Người Quan Sát 2/12/2025: giá nhà Trung Quốc giảm 20% đến 40% so với đỉnh 2021 tuỳ cách đo.
#  - Caproasia 26/8/2025: Evergrande huỷ niêm yết tại Hong Kong ngày 25/8/2025.
#  - WiData (Cục Thống kê Trung Quốc): doanh số bán BĐS luỹ kế (197642) 2021 cả năm 18.193 tỷ NDT (đỉnh); 9T/2021 13.479,5; 9T/2026 5.379,9 → 5.379,9/13.479,5 = 0,399 → GIẢM 60%.
#    Đầu tư BĐS theo quý (197018): 9T/2021 = 2.757,6+4.460,3+4.038,9 = 11.256,8; 9T/2026 = 1.772,0+2.035,4+1.529,0 = 5.336,4 → 0,474 → GIẢM 53%.
#    Diện tích khởi công luỹ kế so cùng kỳ (193968): 2022 -39,4%; 2023 -20,4%; 2024 -23%; 2025 -20,4%; 9T/2026 -24,9% → giảm hơn 20% mỗi năm, 5 năm liền.
#  - Bộ Xây dựng (VietnamFinance 13/10/2026): quý 3/2026 khoảng 92.004 giao dịch BĐS thành công, bằng 92% quý trước.
#  - NHNN, Phó Thống đốc Nguyễn Ngọc Cảnh (Kinh tế Chứng khoán 13/10/2026): 31/8/2026 dư nợ tín dụng BĐS 5,21 triệu tỷ, +9,49% so cuối 2025, 25,39% tổng dư nợ;
#    cho vay kinh doanh BĐS 2,59 triệu tỷ, +19,59%; tiêu dùng tự sử dụng 2,61 triệu tỷ, +1,02%.
#  - Savills (VietnamFinance 16/10/2026): chung cư Hà Nội quý 3/2026 giá sơ cấp bình quân 107 triệu/m², 70% số căn bán được giá trên 6 tỷ; giá thứ cấp giảm quý thứ ba liên tiếp.
#  - DKRA (VietnamFinance 26/10/2026): đất nền Đà Nẵng quý 3/2026 giá sơ cấp giảm khoảng 7% so với quý trước.
#  - WiData/Cục Thống kê (280708): thu nhập bình quân lao động quý 3/2026 khoảng 9,18 triệu đồng/tháng (9.184,9 nghìn), quý 3/2025 8.361,1 → +9,85%.
#  - TỰ TÍNH: căn 6 tỷ / (9,185 triệu x 12 tháng x 2 người) = 27,2 năm thu nhập của hai vợ chồng, không chi tiêu gì.
#  - GIẢ ĐỊNH minh hoạ (nhà chị Lan): nhà ở 5 tỷ + căn hộ cho thuê 4 tỷ (còn nợ 2 tỷ) + tiền gửi 600 triệu + vàng, cổ phiếu 400 triệu = 10 tỷ → nhà đất 9/10 = 90%.
#    Căn cho thuê: tiền thuê 12 triệu/tháng = 144 triệu/năm; lãi vay giả định 10%/năm trên 2 tỷ = 200 triệu/năm → bù 56 triệu/năm ≈ 4,7 triệu/tháng.
#    Nếu căn hộ 4 tỷ giảm 20% → 3,2 tỷ; trả 2 tỷ nợ còn 1,2 tỷ (vốn bỏ ra 2 tỷ → mất 40% vốn).
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261115_0040'
KEY = 'CH1911ND'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
NHA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
WM = 'Blue Marble||World map'     # cảnh số Trung Quốc: không dùng ảnh thành phố nước ngoài theo từ khoá (PPC v1.6)
SGD = 'ov:Ho Chi Minh City Stock Exchange||Bitexco Financial Tower'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('87% TÀI SẢN NGƯỜI VIỆT', 'NẰM Ở NHÀ ĐẤT'), cols=CR, noti=dict(gio='21:05', ngay='Thứ Năm', items=[
        ('Tin tức', 'Vietnambiz', '87% tài sản gia đình Việt nằm ở bất động sản', V_),
        ('Zalo', 'Tiểu Vũ', 'Căn hộ tôi mua năm 2021, giờ hạ giá mà vẫn không ai hỏi', R_),
        ('Ngân hàng', 'Nhắc nợ', 'Kỳ trả góp căn hộ tháng 11 đến hạn ngày 25', X_)]),
      say=("Tám mươi bảy phần trăm. Đó là phần tài sản của các gia đình Việt Nam đang nằm trong nhà đất, theo một khảo sát được báo Vietnambiz đưa tin tuần này. "
           "Tối nay chị Lan, kế toán ở Hà Nội, vừa đọc xong tin đó thì nhận tin nhắn của Tiểu Vũ, người quen Trung Quốc học cùng lớp tiếng Anh ngày trước. "
           "Tiểu Vũ kể: căn hộ mua năm 2021, giờ hạ giá rồi mà vẫn không ai hỏi. Cùng lúc, ngân hàng nhắc kỳ trả góp căn hộ thứ hai của nhà chị.")),
 dict(k='bignum', anh=NHA, cap=('NGƯỜI VIỆT DỒN HẾT VÀO NHÀ', 'TRUNG QUỐC KHOẢNG 70%'), cols=CR, value=87, fmt='{:,.0f}', unit='%', top='TÀI SẢN GIA ĐÌNH VIỆT', sub='nằm ở nhà đất – Vietnambiz 13/11/2026', col=RED,
      say=("Người Trung Quốc từng được xem là dân tộc mê nhà đất nhất thế giới, khoảng bảy mươi phần trăm tài sản của các gia đình thành thị là nhà ở. "
           "Người Việt còn dồn nhiều hơn thế. Và từ năm 2021 tới nay, Trung Quốc đã cho thấy chuyện gì xảy ra khi cả một dân tộc để gần hết của cải trong một loại tài sản. "
           "Câu hỏi là: nhà đất Việt Nam có đang đi đúng vết xe đó, và nhà anh chị đang đứng ở đâu?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Cuốn sổ tài sản nhà chị Lan', cap=('SỔ TÀI SẢN NHÀ CHỊ LAN', '90% LÀ NHÀ ĐẤT'), cols=CC, moc=True, giay=dict(tieu_de='TÀI SẢN NHÀ LAN VÀ MINH', so='Em giả định để minh hoạ, đơn vị đồng', dau='TỰ KÊ', dieu=[
        ('Căn nhà đang ở', '5 TỶ'),
        ('Căn hộ cho thuê, còn nợ 2 tỷ', '4 TỶ'),
        ('Tiền gửi, vàng, cổ phiếu', '1 TỶ'),
        ('Phần nằm ở nhà đất', '90%')]),
      say=("Chị Lan mở cuốn sổ ghi tài sản của hai vợ chồng, số này em giả định để minh hoạ. Căn nhà đang ở khoảng năm tỷ. "
           "Căn hộ chung cư mua năm 2024 để cho thuê khoảng bốn tỷ, vẫn còn nợ ngân hàng hai tỷ. Tiền gửi, vàng và ít cổ phiếu cộng lại khoảng một tỷ. "
           "Tổng mười tỷ, thì chín tỷ nằm ở nhà đất. Chín mươi phần trăm, còn cao hơn mức trung bình tám mươi bảy phần trăm của cả nước.")),
 dict(k='giay', cap=('CĂN HỘ CHO THUÊ', 'THÁNG NÀO CŨNG BÙ TIỀN'), cols=CR, moc=True, giay=dict(tieu_de='CĂN HỘ CHO THUÊ – MỘT NĂM', so='Em giả định, lãi vay 10% mỗi năm', dau='TỰ TÍNH', dieu=[
        ('Tiền thuê thu về một năm', '144 TR'),
        ('Lãi vay 2 tỷ một năm', '200 TR'),
        ('Mỗi năm phải bù thêm', '56 TR'),
        ('Tính ra mỗi tháng', '4,7 TR')]),
      say=("Căn hộ cho thuê được mười hai triệu mỗi tháng, tính ra một năm là một trăm bốn mươi bốn triệu. Nhưng lãi vay hai tỷ, nếu em giả định mười phần trăm mỗi năm, là hai trăm triệu. "
           "Vậy mỗi năm vợ chồng chị bù năm mươi sáu triệu, tức khoảng bốn triệu bảy trăm nghìn mỗi tháng. "
           "Chị chấp nhận vì tin một điều mà gần như ai cũng tin: nhà đất không bao giờ giảm, giữ lâu là thắng.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='chat', ch='Chương 2 – Trung Quốc cũng từng tin như vậy', cap=('"HỒI 2021 AI CŨNG BẢO', 'NHÀ KHÔNG BAO GIỜ GIẢM"'), cols=CR, moc=True, chat=dict(ten='Tiểu Vũ', tv='Đang hoạt động', gio='21:20', mau=R_, msgs=[
        ('Tiểu Vũ', 'Hồi 2021 ai cũng bảo nhà không bao giờ giảm'),
        ('Tiểu Vũ', 'Tôi vay mua thêm căn thứ hai, chờ con lớn bán'),
        ('Tiểu Vũ', 'Giờ rao thấp hơn 30% vẫn không ai gọi'),
        ('me', 'Thật à? Bên đó giảm nhiều vậy sao?')]),
      say=("Tiểu Vũ nhắn tiếp: hồi năm 2021, ai cũng bảo nhà không bao giờ giảm. Cô vay mua căn hộ thứ hai, định để dành cho con. "
           "Bây giờ rao thấp hơn khoảng ba mươi phần trăm mà vẫn không ai gọi. Chị Lan hỏi lại: bên đó giảm nhiều vậy thật sao. Câu trả lời nằm trong số liệu chính thức.")),
 dict(k='giay', cap=('DOANH SỐ BÁN NHÀ', 'MẤT 60% SO VỚI 2021'), cols=CR, moc=True, giay=dict(tieu_de='TRUNG QUỐC: NHỮNG CON SỐ CỦA CÚ SẬP', so='Cục Thống kê Trung Quốc, qua WiData', dau='ĐÃ XẢY RA', dieu=[
        ('Doanh số bán nhà 9 tháng, so với 2021', 'GIẢM 60%'),
        ('Tiền đầu tư xây nhà 9 tháng, so với 2021', 'GIẢM 53%'),
        ('Diện tích khởi công mới mỗi năm', 'GIẢM HƠN 20%'),
        ('Số năm liền khởi công giảm', '5 NĂM')]),
      say=("Năm 2021, Trung Quốc bán được hơn mười tám nghìn tỷ nhân dân tệ nhà đất, mức kỷ lục. Chín tháng đầu năm nay, doanh số chỉ còn khoảng bốn mươi phần trăm so với cùng kỳ năm 2021, tức mất sáu mươi phần trăm. "
           "Tiền đầu tư xây nhà giảm năm mươi ba phần trăm. Diện tích khởi công mới giảm hơn hai mươi phần trăm mỗi năm, liên tục từ năm 2022 tới nay. Em tự tính từ số của Cục Thống kê Trung Quốc, cách tính có trong mô tả.")),
 dict(k='call', cap=('"CĂN HỘ TRẢ TRƯỚC', 'ĐẾN GIỜ VẪN CHƯA XÂY XONG"'), cols=CR, moc=True, call=dict(ten='Tiểu Vũ', phu='Gọi video', mau=R_, loi=[
        'Chủ đầu tư hết tiền, công trường dừng', 'Mình vẫn phải trả góp cho căn chưa có']),
      say=("Tiểu Vũ gọi video. Căn thứ hai của cô mua theo kiểu trả trước khi nhà chưa xây. Chủ đầu tư hết tiền, công trường dừng, cô vẫn phải trả góp hằng tháng cho một căn hộ chưa tồn tại. "
           "Tập đoàn lớn nhất nhì ngành, Evergrande, bị tòa Hồng Kông ra lệnh thanh lý năm 2024 với khoảng ba trăm tỷ đô la nợ. Tháng tám năm 2025, tập đoàn này bị hủy niêm yết tại Hồng Kông.")),
 dict(k='cards', anh=WM, cap=('GIÁ NHÀ TRUNG QUỐC', 'GIẢM 20 ĐẾN 40% TỪ ĐỈNH'), cols=CR, moc=True,
      cards=[('20 đến 40%', 'Giá giảm từ đỉnh năm 2021', 'Tuỳ cách đo'), ('35 tháng', 'Giá nhà mới giảm liên tiếp', 'Tính tới tháng 5/2026'), ('Khoảng 2 điểm', 'Tăng trưởng GDP mất mỗi năm', 'Năm 2024 và 2025')],
      say=("Giá nhà Trung Quốc đã giảm từ hai mươi đến bốn mươi phần trăm so với đỉnh năm 2021, tùy cách đo. Giá nhà mới ở bảy mươi thành phố lớn giảm ba mươi lăm tháng liên tiếp, tính tới giữa năm nay. "
           "Cú sập nhà đất lấy đi khoảng hai điểm phần trăm tăng trưởng của cả nền kinh tế, mỗi năm, trong năm 2024 và năm 2025.")),
 dict(k='text', cap=('NHÀ KHÔNG BAO GIỜ GIẢM', 'CHỈ ĐÚNG KHI CÒN NGƯỜI MUA'), cols=CR, anh=NHA,
      say=("Anh chị thấy đấy, câu nhà đất không bao giờ giảm chỉ đúng khi vẫn còn người mua mới với giá cao hơn. Khi người mua dừng lại, giá không cần giảm mạnh, chỉ cần không bán được là gia đình đã kẹt. "
           "Với một gia đình để bảy mươi phần trăm, hay tám mươi bảy phần trăm tài sản trong nhà, đó là kẹt gần hết của cải.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='cards', ch='Chương 3 – Việt Nam đang ở đâu?', anh=HN, cap=('TÍN DỤNG NHÀ ĐẤT VIỆT NAM', 'NHNN, NGÀY 31/8/2026'), cols=CR, moc=True,
      cards=[('5,21 triệu tỷ', 'Dư nợ tín dụng bất động sản', 'Hơn 1/4 tổng dư nợ'), ('+19,59%', 'Cho vay kinh doanh nhà đất', 'Tăng nhanh nhất'), ('+1,02%', 'Vay mua nhà để ở', 'Gần như đứng yên')],
      say=("Quay về Việt Nam. Theo Ngân hàng Nhà nước, tới cuối tháng tám, dư nợ tín dụng bất động sản khoảng năm phẩy hai triệu tỷ đồng, bằng hơn hai mươi lăm phần trăm tổng dư nợ cả nền kinh tế. "
           "Cú lật nằm ở bên trong. Vay để kinh doanh nhà đất tăng mười chín phẩy sáu phần trăm chỉ sau tám tháng. Còn vay để mua nhà ở thật gần như đứng yên, tăng khoảng một phần trăm.")),
 dict(k='giay', cap=('THỊ TRƯỜNG QUÝ 3/2026', 'GIAO DỊCH CHẬM LẠI'), cols=CR, moc=True, giay=dict(tieu_de='NHÀ ĐẤT VIỆT NAM QUÝ 3/2026', so='Bộ Xây dựng, Savills, DKRA', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Giao dịch cả nước, so với quý trước', '92%'),
        ('Chung cư Hà Nội, giá sơ cấp mỗi m²', '107 TR'),
        ('Căn bán được có giá trên 6 tỷ', '70%'),
        ('Đất nền Đà Nẵng, giá sơ cấp', 'GIẢM 7%')]),
      say=("Còn thị trường quý ba thì sao? Bộ Xây dựng cho biết cả nước có khoảng chín mươi hai nghìn giao dịch, chỉ bằng chín mươi hai phần trăm quý trước. "
           "Ở Hà Nội, theo Savills, chung cư mới bán bình quân một trăm linh bảy triệu đồng một mét vuông, bảy mươi phần trăm số căn bán được có giá trên sáu tỷ. Trong khi đó, giá căn hộ cũ đã giảm ba quý liên tiếp. "
           "Ở Đà Nẵng, giá đất nền sơ cấp giảm khoảng bảy phần trăm chỉ trong một quý.")),
 dict(k='bignum', anh=NHA, cap=('CĂN HỘ 6 TỶ', '= 27 NĂM LƯƠNG HAI VỢ CHỒNG'), cols=CR, moc=True, value=27, fmt='{:,.0f}', unit=' NĂM', top='CĂN HỘ 6 TỶ BẰNG', sub='lương 2 người, không tiêu gì – em tự tính', col=RED,
      say=("Và đây là con số khiến chị Lan im lặng. Thu nhập bình quân của một người lao động Việt Nam quý ba khoảng chín phẩy hai triệu đồng mỗi tháng. "
           "Một căn hộ sáu tỷ ở Hà Nội bằng khoảng hai mươi bảy năm lương của cả hai vợ chồng, nếu không tiêu một đồng nào. Em tự tính, cách tính có trong mô tả.")),
 dict(k='checklist', anh=TP, cap=('VIỆT NAM VÀ TRUNG QUỐC', 'GIỐNG 2, KHÁC 1'), cols=CR, moc=True,
      items=[('Tài sản dồn vào nhà: giống', RED),
             ('Vay kinh doanh nhà tăng nhanh', RED),
             ('Giao dịch chậm, chưa sập', GOLD)],
      say=("Đặt hai nước cạnh nhau. Giống thứ nhất: của cải gia đình dồn vào nhà đất, Việt Nam còn cao hơn. Giống thứ hai: tiền vay để kinh doanh nhà đất tăng nhanh hơn thu nhập, thu nhập chỉ tăng khoảng mười phần trăm trong một năm. "
           "Điểm khác: thị trường Việt Nam đang chậm lại, giá cũ giảm ở vài nơi, nhưng chưa có cú sập kiểu doanh số mất một nửa như Trung Quốc. Chưa, không có nghĩa là không thể.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='chat', ch='Chương 4 – Nếu căn hộ giảm hai mươi phần trăm', cap=('NẾU CĂN HỘ GIẢM 20%', 'VỐN NHÀ LAN MẤT 40%'), cols=CR, moc=True, chat=dict(ten='Minh', tv='Đang hoạt động', gio='22:30', mau=G_, msgs=[
        ('me', 'Nếu căn hộ giảm 20% như bên Tiểu Vũ thì sao anh?'),
        ('Minh', '4 tỷ còn 3,2 tỷ, trả nợ 2 tỷ, còn lại 1,2 tỷ'),
        ('me', 'Mình bỏ vào 2 tỷ, vậy là mất 40% vốn'),
        ('Minh', 'Mà phải bán gấp thì còn thấp hơn nữa')]),
      say=("Chị Lan nhắn chồng: nếu căn hộ giảm hai mươi phần trăm như bên Tiểu Vũ thì sao anh. Anh Minh tính ngay: bốn tỷ còn ba phẩy hai tỷ, trả hai tỷ nợ, còn lại một phẩy hai tỷ. "
           "Vợ chồng bỏ vào hai tỷ tiền thật, vậy là mất bốn mươi phần trăm vốn, dù giá nhà chỉ giảm hai mươi phần trăm. Đòn bẩy làm khoản lỗ to gấp đôi. Mà nếu phải bán gấp, giá còn thấp hơn nữa.")),
 dict(k='cards', anh=SGD, cap=('PHƯƠNG ÁN KHÁC', 'ĐỂ TÀI SẢN CÓ CHÂN THỨ HAI'), cols=CC, moc=True,
      cards=[('4,7 triệu', 'Tiền bù căn hộ mỗi tháng', 'Có thể để dành đều'), ('6 tháng', 'Quỹ dự phòng chi tiêu', 'Không phải bán gấp'), ('Dưới 70%', 'Mốc nhà đất em tự đặt', 'Giảm dần qua từng năm')],
      say=("Có một con đường khác, không cần bán nhà ngay. Thay vì mua thêm căn thứ ba, khoản bốn triệu bảy trăm nghìn mỗi tháng đang bù cho căn hộ có thể dần chuyển thành một phần tiết kiệm và đầu tư có thể rút ra nhanh. "
           "Trước hết là quỹ dự phòng đủ sáu tháng chi tiêu, để không bao giờ phải bán nhà gấp. Sau đó giảm dần phần nhà đất trong tài sản, em tự đặt mốc dưới bảy mươi phần trăm, qua nhiều năm chứ không làm một lần.")),
 dict(k='chat', cap=('KẾ HOẠCH CỦA NHÀ LAN', 'KHÔNG MUA CĂN THỨ BA'), cols=CC, moc=True, chat=dict(ten='Minh', tv='Đang hoạt động', gio='23:05', mau=G_, msgs=[
        ('Minh', 'Thôi, mình dừng ý định mua căn thứ ba'),
        ('me', 'Ừ, trả bớt nợ căn hộ trước'),
        ('Minh', 'Để riêng 6 tháng chi tiêu cho chắc'),
        ('me', 'Rồi mỗi tháng để dành một phần ra kênh khác')]),
      say=("Anh Minh nhắn lại: thôi, mình dừng ý định mua căn thứ ba. Chị Lan đáp: ừ, trả bớt nợ căn hộ trước để tiền lãi nhẹ đi. "
           "Anh thêm: để riêng sáu tháng chi tiêu cho chắc. Chị nhắn tiếp: rồi mỗi tháng để dành một phần ra kênh khác. Không ai biết giá nhà sẽ đi đâu, nhưng nhà mình không còn phải đặt cược tất cả vào một hướng.")),
 dict(k='checklist', anh=NHA, cap=('PHÉP THỬ CỦA ANH CHỊ', 'NHÀ ĐẤT CHIẾM BAO NHIÊU?'), cols=CC, moc=True,
      items=[('Dưới 50%: còn linh hoạt', GREEN),
             ('50 đến 80%: nên có quỹ dự phòng', GOLD),
             ('Trên 80%: như nhà chị Lan', RED)],
      say=("Và đây là phép thử anh chị tự làm được tối nay. Cộng giá trị nhà đất nhà mình, chia cho tổng tài sản. Dưới năm mươi phần trăm thì còn linh hoạt. "
           "Từ năm mươi đến tám mươi phần trăm thì nên có quỹ dự phòng thật chắc. Trên tám mươi phần trăm là đang giống nhà chị Lan. "
           "Thêm một câu hỏi: nếu căn đang vay giảm hai mươi phần trăm và phải bán trong ba tháng, nhà mình có trả hết nợ được không. Đây là mốc em đặt để tự soi, không phải quy định.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Theo dõi gì để biết sớm?', anh=SGD, cap=('3 CON SỐ CẦN THEO DÕI', 'MỖI QUÝ MỘT LẦN'), cols=CC, moc=True,
      items=[('Số giao dịch nhà đất mỗi quý', GOLD),
             ('Giá căn hộ cũ có giảm tiếp', RED),
             ('Vay kinh doanh nhà đất', GOLD)],
      say=("Muốn biết sớm Việt Nam đi đường nào, em gợi ý theo dõi ba con số, mỗi quý một lần. Một: số giao dịch nhà đất Bộ Xây dựng công bố, ở Trung Quốc doanh số luôn giảm trước giá. "
           "Hai: giá căn hộ cũ có giảm tiếp không. Ba: tiền vay kinh doanh nhà đất có tiếp tục tăng nhanh hơn thu nhập không. "
           "Riêng lợi nhuận từng quý của các doanh nghiệp bất động sản và ngân hàng trên sàn, anh chị xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn từ Trung Quốc', cap=('"ĐỪNG ĐỂ CẢ NHÀ', 'NẰM TRONG MỘT CĂN HỘ"'), cols=CC, moc=True, chat=dict(ten='Tiểu Vũ', tv='Đang hoạt động', gio='23:40', mau=R_, msgs=[
        ('Tiểu Vũ', 'Bọn tôi từng nghĩ nhà là chỗ cất tiền an toàn nhất'),
        ('Tiểu Vũ', 'Đừng để cả nhà nằm trong một căn hộ như tôi nhé'),
        ('me', 'Cảm ơn bạn. Mình bắt đầu từ cuốn sổ tài sản nhà mình')]),
      say=("Gần nửa đêm, Tiểu Vũ nhắn thêm: hồi đó cả nhà cô từng nghĩ nhà là chỗ cất tiền an toàn nhất, và dặn chị đừng để cả nhà nằm trong một căn hộ như cô. "
           "Chị Lan trả lời: cảm ơn, mình bắt đầu từ cuốn sổ tài sản nhà mình. Nhà đất vẫn là chỗ ở và là tài sản quý, nhưng Trung Quốc cho thấy, dồn gần hết vào một chỗ thì một cú trượt cũng đủ làm cả nhà chao đảo.")),
 dict(k='end', cap=('NHÀ ĐẤT VIỆT NAM', 'CÓ ĐI VẾT XE TRUNG QUỐC?'), cols=CC,
      say=("Còn anh chị thì sao: nhà mình đang để bao nhiêu phần tài sản trong nhà đất, và anh chị nghĩ nhà đất Việt Nam có đi vết xe của Trung Quốc không? Kể cho em và mọi người ở phần bình luận nhé. "
           "Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = '87% Tài Sản Người Việt Nằm Ở Nhà Đất: Có Đi Vết Xe Trung Quốc? Doanh Số Bán Nhà Bên Đó Đã Mất 60%'
MT = ("Khoảng 87% tài sản của các gia đình Việt Nam nằm ở nhà đất, cao hơn cả Trung Quốc (khoảng 70%). Từ năm 2021, doanh số bán nhà Trung Quốc mất 60%, giá giảm 20–40% từ đỉnh, Evergrande bị thanh lý. "
      "Việt Nam đang ở đâu: tín dụng bất động sản 5,21 triệu tỷ, vay kinh doanh nhà đất tăng 19,59% trong 8 tháng, căn hộ 6 tỷ bằng 27 năm lương hai vợ chồng. Câu chuyện của chị Lan, người bạn Trung Quốc Tiểu Vũ, và phép thử cho chính gia đình anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• Vietnambiz 13/11/2026, VnBusiness 12/11/2026: khoảng 87% tài sản gia đình Việt Nam nằm trong bất động sản (khảo sát do VIG dẫn tại Vietnam Investment Forum)\n"
      "• The Real Deal 7/7/2026: nhà ở khoảng 70% tài sản hộ gia đình thành thị Trung Quốc; giá nhà mới 70 thành phố giảm 35 tháng liên tiếp tới 5/2026; bất động sản lấy đi khoảng 2 điểm % tăng trưởng GDP năm 2024 và 2025; Evergrande bị thanh lý năm 2024 với khoảng 300 tỷ USD nợ\n"
      "• Người Quan Sát 2/12/2025: giá nhà Trung Quốc giảm 20–40% so với đỉnh 2021 tuỳ cách đo\n"
      "• Caproasia 26/8/2025: Evergrande huỷ niêm yết tại Hong Kong ngày 25/8/2025\n"
      "• Cục Thống kê Trung Quốc (qua WiData): doanh số bán bất động sản 2021: 18.193 tỷ NDT; 9 tháng 2021: 13.479,5 tỷ; 9 tháng 2026: 5.379,9 tỷ. Đầu tư bất động sản 9 tháng 2021: 11.256,8 tỷ; 9 tháng 2026: 5.336,4 tỷ. Diện tích khởi công so cùng kỳ: 2022 −39,4%, 2023 −20,4%, 2024 −23%, 2025 −20,4%, 9 tháng 2026 −24,9%\n"
      "• Ngân hàng Nhà nước (Kinh tế Chứng khoán 13/10/2026): 31/8/2026 dư nợ tín dụng bất động sản 5,21 triệu tỷ, 25,39% tổng dư nợ; cho vay kinh doanh bất động sản +19,59%, tiêu dùng tự sử dụng +1,02% so với cuối 2025\n"
      "• Bộ Xây dựng (VietnamFinance 13/10/2026): quý 3/2026 khoảng 92.004 giao dịch, bằng 92% quý trước\n"
      "• Savills (VietnamFinance 16/10/2026): chung cư Hà Nội quý 3/2026 giá sơ cấp bình quân 107 triệu/m², 70% số căn bán được trên 6 tỷ, giá thứ cấp giảm quý thứ ba liên tiếp\n"
      "• DKRA (VietnamFinance 26/10/2026): đất nền Đà Nẵng quý 3/2026 giá sơ cấp giảm khoảng 7% so với quý trước\n"
      "• Cục Thống kê (WiData): thu nhập bình quân lao động quý 3/2026 khoảng 9,18 triệu đồng/tháng, +9,85% so cùng kỳ\n"
      "• Tự tính: 5.379,9/13.479,5 = 0,40 (giảm 60%); 5.336,4/11.256,8 = 0,47 (giảm 53%); 6 tỷ / (9,185 triệu × 12 × 2) = 27,2 năm\n"
      "• Tài sản và căn hộ cho thuê nhà chị Lan là giả định minh hoạ: 9/10 tỷ ở nhà đất = 90%; tiền thuê 144 triệu/năm, lãi vay giả định 10% trên 2 tỷ = 200 triệu → bù 56 triệu/năm (khoảng 4,7 triệu/tháng); căn 4 tỷ giảm 20% còn 3,2 tỷ, trả 2 tỷ nợ còn 1,2 tỷ trên 2 tỷ vốn = mất 40%\n\n"
      "Tra lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật chị Lan, anh Minh và Tiểu Vũ là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-19', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['bất động sản Việt Nam', 'nhà đất', 'bất động sản Trung Quốc', 'Evergrande', 'giá chung cư Hà Nội', 'tín dụng bất động sản', 'tài sản gia đình', 'kinh tế Việt Nam', 'vĩ mô'],
    bia_hook=['TÀI SẢN 87%', 'LÀ NHÀ ĐẤT???'], badge='TÀI SẢN NGƯỜI VIỆT',
    bia_anh='Hanoi apartment buildings||Hanoi skyline night',
    bia_hook_b=['TRUNG QUỐC', 'MẤT 60%???'], badge_b='DOANH SỐ BÁN NHÀ',
    bia_hook_c=['CĂN HỘ 6 TỶ', '= 27 NĂM LƯƠNG'], badge_c='HAI VỢ CHỒNG',
    reel_hook='87% TÀI SẢN LÀ NHÀ ĐẤT|CÓ ĐI VẾT XE TRUNG QUỐC???',
    fb_post=("87% tài sản gia đình Việt nằm ở nhà đất 🏠\n\n👉 Trung Quốc khoảng 70%, doanh số bán nhà đã mất 60% so với 2021\n👉 Vay kinh doanh nhà đất ở Việt Nam tăng 19,59% trong 8 tháng\n"
             "👉 Căn hộ 6 tỷ ở Hà Nội bằng 27 năm lương hai vợ chồng\n\nNhà anh chị đang để bao nhiêu phần tài sản trong nhà đất?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: 87 phần trăm tài sản ở nhà đất, có đi vết xe Trung Quốc (NV1 15/11/2026).\n"
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
