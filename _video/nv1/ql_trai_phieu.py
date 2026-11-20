# -*- coding: utf-8 -*-
# NV1 21/11/2026 – VIDEO DÀI kênh chính, phim kể chuyện tuần (khuôn "manh mối – suy luận" kiểu thám tử):
#   lãi tiết kiệm giảm, nhân viên mời "trái phiếu lãi 9%" – 3 chi tiết bà Tâm suýt bỏ qua. Ghép với "lần trước" 2022 (35.824 trái chủ, 30.081 tỷ).
# Lý do chọn: QL1 giao phim kể chuyện tuần hẹn 28/11 (ql_giao_viec_2011); xu_huong.md tuần tới 20/11: "Lãi suất đang đổi chiều? 5 tín hiệu người gửi tiền" ~38 nghìn,
#   "Trương Mỹ Lan rút ruột… bằng cách nào" ~52 nghìn (vụ án – chỉ dùng số kết luận điều tra, tên tổ chức); tin 16–17/11: lãi huy động giảm 0,5–1 điểm, trái phiếu ngân hàng vẫn sát 10%.
#   TIỀN TÚI NGƯỜI THƯỜNG (sổ tiết kiệm người về hưu). Khác góc NONG1711A (SCB lãi 0%, 17/11) và CH2011VON (lãi thật, 20/11): ở đây là phân biệt tiết kiệm với trái phiếu.
# Nguồn:
#  - VietnamFinance 17/11/2026: lãi huy động đồng loạt giảm 0,5–1 điểm % từ giữa tháng 10 sau Công văn 9736/NHNN (giảm lãi tiền gửi bình quân giao dịch mới kỳ hạn trên 6 tháng);
#    VCBS: lãi 6 tháng bình quân tháng 10 còn 4,47%; trái phiếu ngân hàng 9–10,5%/năm (một lô 10 năm 9,7%; một ngân hàng 9%, kỳ hạn 24–36 tháng);
#    VBMA: 10 tháng 2026 ngân hàng phát hành khoảng 260.000 tỷ, 55% thị trường trái phiếu doanh nghiệp; từ 18/10, 13 lô trái phiếu ngân hàng hơn 15.600 tỷ.
#  - VietnamFinance 15/11/2026: NHNN yêu cầu thanh tra việc thực hiện giảm lãi suất tại các ngân hàng trong tháng 11.
#  - Bảo hiểm tiền gửi: hạn mức 350 triệu đồng/người/tổ chức tín dụng từ 13/7/2026 (Thông tư 05/2026/TT-NHNN; VietnamPlus, Báo Đầu tư) – dùng ở NONG1711A.
#  - div.gov.vn (Bảo hiểm tiền gửi Việt Nam) 27/2/2023: "rủi ro của trái phiếu vẫn là rủi ro của doanh nghiệp phát hành"; ngân hàng, công ty chứng khoán phân phối trái phiếu không có nghĩa là bảo lãnh;
#    div.gov.vn 27/9/2023: trái phiếu ngân hàng kỳ hạn 2–10 năm, nhận gốc khi đáo hạn, thanh khoản qua chuyển nhượng, rủi ro thanh khoản lớn; tiết kiệm có thể rút trước hạn.
#  - VnEconomy 28/9/2024: vụ án liên quan tập đoàn Vạn Thịnh Phát giai đoạn 2 – chiếm đoạt hơn 30.081 tỷ đồng của 35.824 nhà đầu tư, 25 mã trái phiếu qua 4 công ty.
#  - Stockbiz/VietNamNet 9/6/2024 (kết luận điều tra): hơn 2.000 nhân viên của 239 chi nhánh ngân hàng SCB được tập huấn bán trái phiếu; khách được giới thiệu là "một hình thức tiết kiệm linh hoạt, lãi suất cao".
#  - Thông tư 04/2022/TT-NHNN: rút tiết kiệm trước hạn hưởng lãi không kỳ hạn thấp nhất (div.gov.vn 27/2/2023).
# TỰ TÍNH (giả định, bà Tâm 800 triệu): tiết kiệm 12 tháng giả định 5% → 40 triệu/năm; trái phiếu 9% → 72 triệu/năm; chênh 32 triệu/năm ≈ 2,67 triệu/tháng; 3 năm 96 triệu.
#   800 triệu ở 1 ngân hàng: được bảo hiểm tối đa 350 triệu, 450 triệu ngoài hạn mức. 30.081 tỷ / 35.824 người ≈ 839,7 triệu/người (bình quân).
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261121_0200'
KEY = 'CH2811TP'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
HA = 'ov:Hanoi apartment buildings||Hanoi skyline night'
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
BX = 'ov:Bitexco Financial Tower||Ho Chi Minh City skyline night'
HS = 'ov:Ho Chi Minh City Stock Exchange||Ho Chi Minh City skyline night'
BT = 'ov:Ben Thanh Market||Ho Chi Minh City skyline night'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('SỔ 800 TRIỆU ĐÁO HẠN', 'LÃI MỚI THẤP HƠN'), cols=CC, noti=dict(gio='08:05', ngay='Thứ Hai', items=[
        ('Ngân hàng', 'Thông báo', 'Sổ tiết kiệm 800.000.000đ đến hạn. Lãi suất kỳ mới thấp hơn kỳ trước', V_),
        ('Tin tức', 'Ngân hàng', 'Lãi huy động đồng loạt giảm 0,5 đến 1 điểm phần trăm', R_)]),
      say=("Tám giờ sáng thứ Hai, bà Tâm, giáo viên về hưu sáu mươi ba tuổi, ngồi chờ ở quầy giao dịch. "
           "Sổ tiết kiệm tám trăm triệu đồng, tiền dành dụm cả đời, vừa đến hạn, và lãi kỳ mới thấp hơn kỳ trước. "
           "Cô nhân viên trẻ mỉm cười, đưa bà một tờ giấy: cô ơi, có sản phẩm lãi chín phần trăm, gần gấp đôi, cũng như gửi tiết kiệm thôi cô. "
           "Bà Tâm cầm tờ giấy về nhà. Bà có nên ký không?")),
 dict(k='bignum', anh=TP, cap=('TIẾT KIỆM GIẢM', 'LỜI MỜI LÃI 9%'), cols=CC, value=9, fmt='{:,.0f}', unit='%', top='LÃI SUẤT GHI TRÊN TỜ GIẤY Ở QUẦY',
      sub='lãi tiết kiệm 6 tháng bình quân thị trường tháng 10 còn 4,47% – VCBS', col=GOLD,
      say=("Lời mời đó không lạ. Theo VietnamFinance, từ giữa tháng mười, lãi huy động đã đồng loạt giảm từ nửa điểm đến một điểm phần trăm. "
           "Lãi sáu tháng bình quân thị trường chỉ còn khoảng bốn phẩy năm phần trăm. "
           "Trong khi đó, những con số chín, mười phần trăm vẫn xuất hiện ở nhiều nơi.")),
 dict(k='checklist', anh=HA, cap=('3 CHI TIẾT', 'TRẢ LỜI CUỐI PHIM'), cols=CC,
      items=[('1. Biểu lãi có dòng: được bảo hiểm', V_), ('2. Một dòng chữ mờ trên tờ giấy', X_), ('3. Câu nói của cô nhân viên', G_)],
      say=("Trong buổi sáng đó có ba chi tiết nhỏ, anh chị nhớ giúp em, cuối phim sẽ cần đến. "
           "Một: tờ biểu lãi dán trên quầy, ở góc có dòng chữ nhỏ: tiền gửi được bảo hiểm. "
           "Hai: một dòng chữ in mờ trên tờ giấy cô nhân viên đưa. "
           "Ba: câu nói, cũng như gửi tiết kiệm thôi cô.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Vì sao lãi tiết kiệm giảm?', cap=('LÃI 6 THÁNG BÌNH QUÂN', 'CÒN 4,47%'), cols=CC, moc=True, giay=dict(tieu_de='LÃI TIỀN GỬI THÁNG 10/2026', so='VCBS, VietnamFinance 17/11/2026', dau='BÌNH QUÂN', dieu=[
        ('Mức giảm từ giữa tháng 10', '0,5 ĐẾN 1 ĐIỂM'),
        ('Kỳ hạn 6 tháng, bình quân', '4,47%'),
        ('Kỳ hạn 1 đến 3 tháng', 'DƯỚI 4%'),
        ('Văn bản của NHNN', 'CÔNG VĂN 9736')]),
      say=("Tối đó, Khoa, con trai bà, kỹ sư phần mềm ở Thành phố Hồ Chí Minh, gọi về. Hai mẹ con xem lại từ đầu. "
           "Ngân hàng Nhà nước đã có công văn yêu cầu giảm lãi tiền gửi các kỳ hạn trên sáu tháng. "
           "Theo VCBS, trong tháng mười, lãi kỳ hạn ngắn bình quân chỉ còn dưới bốn phần trăm.")),
 dict(k='noti', cap=('NHNN YÊU CẦU', 'THANH TRA VIỆC GIẢM LÃI'), cols=CR, moc=True, noti=dict(gio='21:10', ngay='Thứ Hai', items=[
        ('Tin tức', 'Ngân hàng', 'NHNN yêu cầu thanh tra việc thực hiện giảm lãi suất trong tháng 11', V_),
        ('Zalo', 'Khoa', 'Lãi tiết kiệm có thể còn giảm nữa mẹ ạ', X_)]),
      say=("Khoa gửi cho mẹ thêm một tin: Ngân hàng Nhà nước yêu cầu thanh tra việc thực hiện giảm lãi suất ngay trong tháng mười một. "
           "Tức là lãi tiết kiệm chưa chắc đã dừng ở đây. Bà Tâm thở dài: thế thì trách gì người ta chẳng tìm chỗ lãi cao hơn.")),
 dict(k='giay', short=True, cap=('800 TRIỆU, LÃI 5% HAY 9%', 'CHÊNH 32 TRIỆU MỘT NĂM'), cols=CC, moc=True, giay=dict(tieu_de='PHÉP TÍNH CỦA BÀ TÂM', so='Em giả định, em tự tính', dau='TỰ TÍNH', dieu=[
        ('Số tiền', '800 TRIỆU'),
        ('Tiết kiệm, giả định 5%', '40 TRIỆU'),
        ('Tờ giấy ở quầy, 9%', '72 TRIỆU'),
        ('Chênh mỗi năm', '32 TRIỆU')]),
      say=("Bà Tâm lấy giấy bút tính. Em giả định tiết kiệm mười hai tháng khoảng năm phần trăm: mỗi năm được bốn mươi triệu. "
           "Lãi chín phần trăm: bảy mươi hai triệu. "
           "Chênh ba mươi hai triệu một năm, tức khoảng hai triệu bảy mỗi tháng, gần nửa tháng lương hưu của bà.")),
 dict(k='chat', cap=('"TÔI KÝ RỒI', 'LÃI 9% SƯỚNG LẮM"'), cols=CR, moc=True, chat=dict(ten='Chị Hoa', tv='Đang hoạt động', gio='21:40', mau=V_, msgs=[
        ('Chị Hoa', 'Tôi ký cái lãi 9% đó tuần trước rồi'),
        ('Chị Hoa', 'Bà ký đi, để tiết kiệm lãi bèo lắm'),
        ('me', 'Để tôi hỏi thằng Khoa đã')]),
      say=("Đúng lúc đó, chị Hoa, đồng nghiệp cũ ở trường, nhắn tin. Chị bảo tuần trước đã ký cái lãi chín phần trăm đó rồi, khuyên bà Tâm ký nhanh kẻo hết suất. "
           "Bà Tâm trả lời: để hỏi thằng Khoa đã. Một lời mời từ người quen bao giờ cũng khó từ chối hơn lời mời từ người lạ.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='giay', ch='Chương 2 – Tờ giấy ở quầy', cap=('LÃI 9%, 36 THÁNG', 'CÒN MỘT DÒNG IN MỜ'), cols=CR, moc=True, giay=dict(tieu_de='TỜ GIẤY Ở QUẦY', so='Chi tiết trong truyện, em giả định', dau='CHƯA KÝ', dieu=[
        ('Lãi suất', '9% MỘT NĂM'),
        ('Kỳ hạn', '36 THÁNG'),
        ('Trả lãi', 'MỖI NĂM'),
        ('Dòng in mờ cuối trang', '???')]),
      say=("Giờ đến tờ giấy. Lãi suất chín phần trăm, kỳ hạn ba mươi sáu tháng, trả lãi mỗi năm. "
           "Cuối trang có một dòng in mờ, bà Tâm đeo kính vẫn chưa đọc rõ. Khoa bảo mẹ cứ chụp lại, để đó đã.")),
 dict(k='bignum', anh=BX, cap=('NGÂN HÀNG ĐANG CẦN VỐN DÀI', 'KHOẢNG 260.000 TỶ TRÁI PHIẾU'), cols=CC, moc=True, value=260000, fmt='{:,.0f}', unit=' TỶ ĐỒNG', top='TRÁI PHIẾU DO NGÂN HÀNG PHÁT HÀNH, 10 THÁNG 2026',
      sub='55% thị trường trái phiếu doanh nghiệp – VBMA, VietnamFinance 17/11', col=GOLD,
      say=("Vì sao lãi tiết kiệm giảm mà vẫn có nơi trả chín phần trăm? Có một lý do nằm ở đây. "
           "Theo Hiệp hội Thị trường Trái phiếu, mười tháng năm nay các ngân hàng đã phát hành khoảng hai trăm sáu mươi nghìn tỷ đồng trái phiếu. Con số đó bằng năm mươi lăm phần trăm thị trường trái phiếu doanh nghiệp. "
           "Lãi của những lô mới từ chín đến hơn mười phần trăm.")),
 dict(k='text', anh=TP, cap=('KỲ HẠN DÀI', 'THƯỜNG TRẢ LÃI CAO HƠN'),
      say=("Ngân hàng cần những khoản vốn dài hạn, và kỳ hạn dài thường phải trả lãi cao hơn. Phần lãi cao không phải món quà, mà là tiền trả cho việc khóa tiền lâu.")),
 dict(k='call', cap=('"MẸ CÓ CHẮC', '3 NĂM KHÔNG ĐỤNG ĐẾN?"'), cols=CC, moc=True, call=dict(ten='Khoa', phu='Đang gọi', mau=X_, loi=[
        'Ba năm tới mẹ có chắc không cần đến tiền?', 'Năm ngoái mẹ mổ mắt phải rút sổ giữa chừng']),
      say=("Khoa hỏi mẹ một câu rất đời: ba năm tới mẹ có chắc không cần đến số tiền này không? Năm ngoái mẹ đi mổ mắt, phải rút một sổ giữa chừng. "
           "Bà Tâm nhớ lần đó. Rút sổ tiết kiệm trước hạn, bà chỉ được hưởng lãi không kỳ hạn, nhưng lấy lại được tiền gốc.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='giay', ch='Chương 3 – Lần trước: vụ án khởi tố năm 2022', cap=('35.824 NGƯỜI MUA TRÁI PHIẾU', 'BỊ CHIẾM ĐOẠT 30.081 TỶ'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='VnEconomy 28/9/2024; VietNamNet 9/6/2024', dau='ĐÃ XẢY RA', dieu=[
        ('Số người mua trái phiếu bị hại', '35.824'),
        ('Số tiền bị chiếm đoạt', '30.081 TỶ'),
        ('Số mã trái phiếu', '25 MÃ'),
        ('Chi nhánh có nhân viên được tập huấn', '239')]),
      say=("Phải nói công bằng trước: trái phiếu do chính ngân hàng phát hành hôm nay là sản phẩm hợp pháp. "
           "Nhưng Khoa vẫn nhớ đến một vụ án khởi tố năm hai nghìn hai mươi hai, liên quan tập đoàn Vạn Thịnh Phát. "
           "Theo hồ sơ vụ án đưa ra xét xử, hơn ba mươi nghìn tỷ đồng của gần ba mươi sáu nghìn người mua trái phiếu đã bị chiếm đoạt.")),
 dict(k='bignum', anh=HA, cap=('BÌNH QUÂN MỖI NGƯỜI', 'KHOẢNG 840 TRIỆU'), cols=CR, moc=True, value=840, fmt='{:,.0f}', unit=' TRIỆU', top='30.081 TỶ CHIA CHO 35.824 NGƯỜI (EM TỰ TÍNH)',
      sub='gần bằng cuốn sổ 800 triệu của bà Tâm', col=RED,
      say=("Em chia thử. Bình quân mỗi người khoảng tám trăm bốn mươi triệu đồng, gần bằng cuốn sổ của bà Tâm. "
           "Theo kết luận điều tra, hơn hai nghìn nhân viên ở hai trăm ba mươi chín chi nhánh của ngân hàng SCB đã được tập huấn để bán những trái phiếu đó.")),
 dict(k='call', cap=('"NĂM ĐÓ CHÚ CŨNG', 'CHỈ NHỚ CON SỐ LÃI"'), cols=CR, moc=True, call=dict(ten='Chú Bảy', phu='Hàng xóm cũ', mau=R_, loi=[
        'Năm đó chú cũng chỉ nhớ con số lãi', 'Giấy tờ chú ký mà chú không đọc hết']),
      say=("Khoa gọi cho chú Bảy, hàng xóm cũ của nhà mình, người từng mua trái phiếu trong vụ án ấy. "
           "Chú kể: năm đó chú cũng chỉ nhớ con số lãi. Giấy tờ chú ký, chú không đọc hết. Đến lúc cần tiền mới biết đó không phải sổ tiết kiệm. "
           "Chú Bảy là nhân vật hư cấu.")),
 dict(k='checklist', anh=HN, cap=('LẦN TRƯỚC VÀ HÔM NAY', 'GIỐNG 2, KHÁC 2'), cols=CC, moc=True,
      items=[('Lãi cao hơn tiết kiệm rất nhiều', R_), ('Được mời ngay tại quầy giao dịch', R_), ('Hôm nay: ngân hàng tự phát hành', G_), ('Tiền gửi: bảo hiểm lên 350 triệu', G_)],
      say=("Khoa so lần trước với lời mời hôm nay. Giống nhau hai điểm: lãi cao hơn tiết kiệm rất nhiều, và người mua được mời ngay tại quầy. "
           "Khác nhau hai điểm: tổ chức phát hành hôm nay là chính ngân hàng, không phải các công ty như trong vụ án. "
           "Và hạn mức bảo hiểm tiền gửi đã được nâng lên ba trăm năm mươi triệu đồng.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='checklist', ch='Chương 4 – Huy Nguyễn ghép ba chi tiết', anh=HA, cap=('CHI TIẾT THỨ NHẤT', 'TỜ BIỂU LÃI TRÊN QUẦY'), cols=CC, moc=True,
      items=[('Biểu lãi: có dòng bảo hiểm tiền gửi', G_), ('Tờ giấy 9%: không có dòng đó', R_)],
      say=("Giờ quay lại ba chi tiết đầu phim. Chi tiết thứ nhất, tờ biểu lãi trên quầy. Ở góc tờ biểu có dòng chữ: tiền gửi được bảo hiểm. "
           "Bà Tâm lật tờ giấy chín phần trăm ra so. Tờ giấy đó không có dòng nào như vậy.")),
 dict(k='checklist', anh=HN, cap=('CHI TIẾT THỨ HAI', 'DÒNG IN MỜ: TRÁI PHIẾU'), cols=CC, moc=True,
      items=[('Loại sản phẩm: trái phiếu', R_), ('Không phải tiền gửi, ngoài bảo hiểm', R_), ('Muốn lấy tiền sớm: phải bán lại', V_)],
      say=("Chi tiết thứ hai, dòng in mờ. Phóng to ảnh chụp, Khoa đọc được: loại sản phẩm, trái phiếu. "
           "Trái phiếu không phải tiền gửi, nên không nằm trong danh mục được bảo hiểm tiền gửi.")),
 dict(k='cards', anh=HS, cap=('TIẾT KIỆM VÀ TRÁI PHIẾU', 'KHÁC NHAU 3 ĐIỂM'), cols=CC, moc=True,
      cards=[('Bảo hiểm', 'Tiết kiệm: tối đa 350 triệu', 'Trái phiếu: không có'), ('Rút sớm', 'Tiết kiệm: lãi không kỳ hạn', 'Trái phiếu: phải bán lại'), ('Rủi ro', 'Thuộc tổ chức phát hành', 'Người bán không bảo lãnh')],
      say=("Đặt hai thứ cạnh nhau. Bảo hiểm: tiền gửi tiết kiệm có, trái phiếu không. "
           "Rút sớm: tiết kiệm rút được, chỉ hưởng lãi không kỳ hạn; trái phiếu phải tìm người mua lại. "
           "Rủi ro: trái phiếu mang rủi ro của tổ chức phát hành. Bảo hiểm tiền gửi Việt Nam còn lưu ý, việc ngân hàng hay công ty chứng khoán đứng ra phân phối không có nghĩa là họ bảo lãnh.")),
 dict(k='checklist', anh=TP, cap=('CHI TIẾT THỨ BA', 'CÂU NÓI Ở QUẦY'), cols=CC, moc=True,
      items=[('"Cũng như gửi tiết kiệm thôi cô"', R_), ('Rất giống lời giới thiệu năm xưa', R_), ('Lời giải: không phải tiền gửi', V_)],
      say=("Chi tiết thứ ba, câu nói cũng như gửi tiết kiệm thôi cô. Kết luận điều tra vụ án năm xưa ghi lại: khách được giới thiệu trái phiếu là một hình thức tiết kiệm linh hoạt, lãi suất cao. "
           "Sản phẩm hôm nay có thể khác, nhưng một câu so sánh sai vẫn là câu so sánh sai. "
           "Ghép ba chi tiết lại, lời giải không nằm ở chín phần trăm, mà ở bốn chữ: không phải tiền gửi.")),
 dict(k='bignum', anh=HA, cap=('800 TRIỆU Ở MỘT NGÂN HÀNG', '450 TRIỆU NGOÀI HẠN MỨC'), cols=CR, moc=True, value=450, fmt='{:,.0f}', unit=' TRIỆU', top='PHẦN VƯỢT HẠN MỨC BẢO HIỂM 350 TRIỆU (GỐC VÀ LÃI)',
      sub='hạn mức 350 triệu/người/ngân hàng từ 13/7/2026 – em tự tính', col=RED,
      say=("Và còn một điều bà chưa từng để ý, nằm ngay trong cuốn sổ cũ. Hạn mức bảo hiểm tiền gửi là ba trăm năm mươi triệu đồng cho mỗi người tại mỗi ngân hàng, tính cả gốc và lãi. "
           "Tám trăm triệu để ở một ngân hàng thì bốn trăm năm mươi triệu nằm ngoài hạn mức. "
           "Vượt hạn mức không có nghĩa là sẽ mất. Đó chỉ là lưới an toàn cuối cùng, và bà nên biết lưới rộng đến đâu.")),
 dict(k='cards', anh=TP, cap=('800 TRIỆU, 3 NGÂN HÀNG', 'CÁCH BÀ TÂM CHIA'), cols=CC, moc=True,
      cards=[('300 triệu', 'Tiết kiệm ngân hàng thứ nhất', 'Cả gốc lẫn lãi dưới 350'), ('300 triệu', 'Tiết kiệm ngân hàng thứ hai', 'Cả gốc lẫn lãi dưới 350'), ('200 triệu', 'Ngân hàng thứ ba, kỳ hạn ngắn', 'Phòng khi ốm đau')],
      say=("Cuối cùng bà Tâm chia tám trăm triệu vào ba ngân hàng: ba trăm triệu, ba trăm triệu, và hai trăm triệu kỳ hạn ngắn phòng khi ốm đau. "
           "Mỗi nơi, cả gốc lẫn lãi đều dưới ba trăm năm mươi triệu. "
           "Bà chấp nhận lãi thấp hơn, đổi lại ngủ ngon hơn. Đó là lựa chọn của bà, không phải công thức cho mọi người.")),
 dict(k='checklist', anh=TP, cap=('PHÉP THỬ CỦA ANH CHỊ', 'TRƯỚC KHI KÝ'), cols=CC, moc=True,
      items=[('Tên sản phẩm có chữ tiền gửi?', X_), ('Rút trước hạn thì mất gì?', X_), ('Có cần số tiền này trong kỳ hạn?', V_)],
      say=("Phép thử cho anh chị trước khi ký bất kỳ tờ giấy nào lãi cao hơn tiết kiệm. "
           "Một: tên sản phẩm có phải tiền gửi, tiết kiệm không, hay là trái phiếu, chứng chỉ quỹ, bảo hiểm? "
           "Hai: rút trước hạn thì mất gì? "
           "Ba: anh chị có thể cần số tiền này trong kỳ hạn đó không? Có một câu trả lời không chắc chắn, hãy mang giấy về nhà đọc lại.")),
 dict(k='checklist', ch='Chương 5 – Theo dõi gì tiếp theo?', anh=BX, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY ĐẾN TẾT'), cols=CC, moc=True,
      items=[('Lãi tiết kiệm sau đợt thanh tra', V_), ('Lãi trái phiếu ngân hàng mới', V_), ('Hạn mức bảo hiểm tiền gửi', G_)],
      say=("Em gợi ý theo dõi ba điều. Một: lãi tiết kiệm sau đợt thanh tra tháng mười một, còn giảm hay đứng lại. "
           "Hai: lãi các lô trái phiếu ngân hàng mới. Khoảng cách với tiết kiệm càng lớn, càng nhiều lời mời như của bà Tâm. "
           "Ba: hạn mức bảo hiểm tiền gửi, để chia tiền cho đúng. Số liệu lãi suất và vĩ mô hằng tháng, anh chị xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn của mẹ', cap=('"LÃI CAO THÌ ĐỌC', 'CHỮ NHỎ TRƯỚC"'), cols=CC, moc=True, chat=dict(ten='Mẹ', tv='Đang hoạt động', gio='22:15', mau=V_, msgs=[
        ('Mẹ', 'Mai mẹ ra chia làm ba sổ, ba ngân hàng'),
        ('Mẹ', 'Từ giờ lãi cao thì mẹ đọc chữ nhỏ trước'),
        ('me', 'Dạ, mẹ hỏi thẳng: đây có phải tiền gửi không')]),
      say=("Gần khuya, bà Tâm nhắn cho con: mai mẹ ra chia làm ba sổ, ba ngân hàng. Từ giờ thấy lãi cao, mẹ đọc chữ nhỏ trước. "
           "Khoa dặn thêm một câu: mẹ cứ hỏi thẳng, đây có phải tiền gửi không. "
           "Chín phần trăm không sai, ba mươi sáu tháng không sai. Chỉ có câu cũng như gửi tiết kiệm là sai.")),
 dict(k='end', cap=('ANH CHỊ ĐÃ TỪNG ĐƯỢC MỜI', 'SẢN PHẨM LÃI CAO Ở QUẦY?'), cols=CC,
      say=("Còn anh chị thì sao: anh chị đã bao giờ được mời một sản phẩm lãi cao hơn tiết kiệm ngay tại quầy, và anh chị đã hỏi câu gì trước khi quyết định? "
           "Kể cho em và mọi người ở phần bình luận nhé. Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu chuyện tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=75)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Sổ 800 Triệu Đáo Hạn, Được Mời Lãi 9%: 3 Chi Tiết Phải Đọc'
MT = ("Lãi tiết kiệm giảm 0,5–1 điểm % từ giữa tháng 10, trong khi trái phiếu ngân hàng vẫn trả 9 đến hơn 10%/năm. Bà Tâm, giáo viên về hưu, cầm cuốn sổ 800 triệu đáo hạn và một tờ giấy \"lãi 9%, cũng như gửi tiết kiệm thôi cô\". "
      "Ba chi tiết nhỏ – tờ biểu lãi, dòng in mờ trên tờ giấy, câu nói ở quầy – ghép lại thành lời giải: trái phiếu không phải tiền gửi, không nằm trong hạn mức bảo hiểm 350 triệu, kỳ hạn dài, khó rút sớm. "
      "Lần trước (vụ án khởi tố năm 2022): 30.081 tỷ đồng của 35.824 người mua trái phiếu bị chiếm đoạt – bình quân khoảng 840 triệu mỗi người.\n\n"
      "Nguồn số liệu:\n"
      "• VietnamFinance 17/11/2026: lãi huy động giảm 0,5–1 điểm % từ giữa tháng 10 sau Công văn 9736/NHNN; VCBS: lãi 6 tháng bình quân tháng 10 khoảng 4,47%, kỳ hạn 1–3 tháng 3,43–3,85%; trái phiếu ngân hàng 9–10,5%/năm (một lô 10 năm 9,7%; một ngân hàng 9%, kỳ hạn 24–36 tháng); VBMA: 10 tháng 2026 ngân hàng phát hành khoảng 260.000 tỷ, 55% thị trường\n"
      "• VietnamFinance 15/11/2026: NHNN yêu cầu thanh tra việc thực hiện giảm lãi suất trong tháng 11\n"
      "• Hạn mức bảo hiểm tiền gửi 350 triệu đồng/người/tổ chức tín dụng, gồm gốc và lãi, từ 13/7/2026 (Thông tư 05/2026/TT-NHNN); trước đó 125 triệu (div.gov.vn 2023). Luật Bảo hiểm tiền gửi: trái phiếu không thuộc tiền gửi được bảo hiểm\n"
      "• Bảo hiểm tiền gửi Việt Nam (div.gov.vn) 27/2/2023: rủi ro của trái phiếu là rủi ro của tổ chức phát hành; ngân hàng phân phối không có nghĩa là bảo lãnh. div.gov.vn 27/9/2023: trái phiếu ngân hàng kỳ hạn 2–10 năm, rủi ro thanh khoản; tiết kiệm có thể rút trước hạn. Thông tư 04/2022/TT-NHNN: rút trước hạn hưởng lãi không kỳ hạn thấp nhất\n"
      "• VnEconomy 28/9/2024 (TAND TP.HCM thông báo trước xét xử): vụ án liên quan tập đoàn Vạn Thịnh Phát giai đoạn 2 – hơn 30.081 tỷ đồng của 35.824 nhà đầu tư bị chiếm đoạt, 25 mã trái phiếu của 4 công ty\n"
      "• VietNamNet 9/6/2024 (qua Stockbiz, kết luận điều tra): hơn 2.000 nhân viên của 239 chi nhánh ngân hàng SCB được tập huấn bán trái phiếu, khách được giới thiệu là \"một hình thức tiết kiệm linh hoạt, lãi suất cao\"\n"
      "• Em tự tính (giả định): 800 triệu, tiết kiệm giả định 5% = 40 triệu/năm; lãi 9% = 72 triệu/năm; chênh 32 triệu/năm. 800 triệu ở một ngân hàng: 450 triệu ngoài hạn mức 350 triệu. Chia 300/300/200 ở ba ngân hàng: 300 × 1,05 = 315 triệu dưới 350. 30.081 tỷ / 35.824 người ≈ 840 triệu/người\n\n"
      "Số liệu lãi suất, vĩ mô hằng tháng: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật bà Tâm, anh Khoa, chị Hoa, chú Bảy, tờ giấy và tờ biểu lãi ở quầy là hư cấu; số liệu là thật. Trái phiếu do ngân hàng phát hành là sản phẩm hợp pháp; video chỉ phân biệt nó với tiền gửi tiết kiệm.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán hay tư vấn đầu tư.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Phim kể chuyện', ngay='2026-11-28', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['lãi suất tiết kiệm', 'trái phiếu ngân hàng', 'bảo hiểm tiền gửi', 'gửi tiết kiệm', 'lãi suất giảm', 'trái phiếu doanh nghiệp', 'tài chính cá nhân', 'người về hưu', 'kinh tế Việt Nam'],
    bia_hook=['CŨNG NHƯ', 'TIẾT KIỆM???'], badge='LỜI MỜI LÃI 9%',
    bia_anh='Ho Chi Minh City skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['GỬI 800 TRIỆU', 'BẢO HIỂM 350'], badge_b='450TR NGOÀI HẠN MỨC',
    bia_hook_c=['TIẾT KIỆM 5%', 'TỜ GIẤY 9%'], badge_c='SỔ 800 TRIỆU ĐÁO HẠN',
    reel_hook='LÃI TIẾT KIỆM GIẢM|MỜI TRÁI PHIẾU 9% CÓ NÊN KÝ???',
    fb_post=("Sổ tiết kiệm 800 triệu đáo hạn, lãi kỳ mới thấp hơn – và một tờ giấy \"lãi 9%, cũng như gửi tiết kiệm thôi cô\" 🧾\n\n"
             "👉 Lãi huy động giảm 0,5–1 điểm % từ giữa tháng 10\n👉 Trái phiếu ngân hàng vẫn 9 đến hơn 10%/năm\n👉 Bảo hiểm tiền gửi tối đa 350 triệu – chỉ cho tiền gửi, không cho trái phiếu\n"
             "👉 Năm 2022: 35.824 người mua trái phiếu mất 30.081 tỷ\n\nAnh chị đã từng được mời sản phẩm lãi cao ở quầy chưa?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – phim kể chuyện: lãi tiết kiệm giảm, mời trái phiếu 9 phần trăm, 3 chi tiết (NV1 21/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
CX = {'noti': ('tò mò', 'chuông thông báo'), 'chat': ('tâm sự', 'tiếng gõ phím'), 'call': ('trầm, lo', 'chuông gọi'), 'giay': ('căng', 'lật giấy'),
      'bignum': ('sốc', 'trống nhấn'), 'cards': ('suy nghĩ', 'nền phố'), 'bars': ('so sánh', 'nền phố'), 'checklist': ('quyết tâm', 'tick'), 'text': ('ngộ ra', 'nền nhẹ'), 'end': ('mở', 'nhạc kết')}
with open(LO + '/phan_canh.md', 'w', encoding='utf-8') as f:
    f.write('| # | loại | hình (thẻ form cũ) | cảm xúc | tiếng động |\n|---|---|---|---|---|\n')
    for i, c in enumerate(S, 1):
        cx = CX.get(c['k'], ('', '')); f.write('| %d | the/%s | %s | %s | %s |\n' % (i, c['k'], ' / '.join(c.get('cap', ('', ''))), cx[0], cx[1]))
if __name__ == '__main__':
    from collections import Counter
    cnt = Counter(c['k'] for c in S); dt = sum(cnt[k] for k in ('chat', 'noti', 'call', 'giay'))
    print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dien thoai/giay %d/%d' % (dt, len(S)), 'tieu de', len(TIEU))
    for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
    for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
    sys.path.insert(0, CW + '/_video'); import kiem_loi, kiem_goi
    print('goi', kiem_goi.kiem(TIEU, META[KEY]['bia_hook']))
    for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
        if 'câu cụt' not in q: print(q)
    from xung_ho import le_phep
    for c in S:
        if le_phep(c['say']) != c['say']: print('XUNG_HO', c['say'][:80])
    for c in S:
        for x in c.get('cards', []):
            for y in x:
                if isinstance(y, str) and len(y) > 30: print('CARD DAI', y)
        for x in c.get('items', []):
            if len(x[0]) > 40: print('ITEM DAI', len(x[0]), x[0])
        for x in c.get('cap', ()):
            if len(x) > 30: print('CAP DAI', len(x), x)
