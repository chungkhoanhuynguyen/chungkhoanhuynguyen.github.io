# -*- coding: utf-8 -*-
# NV1B 12/11/2026 – VIDEO NÓNG kênh chính: NHNN bắt đầu mua USD giao ngay giá 25.500 (từ 11/11/2026).
# Lý do chọn: tin chính sách tiền tệ lớn nhất 24h (cafebiz, Thanh Tra, SGGP, tinnhanhchungkhoan, người quan sát 11/11);
#   nối tiếp dạng thắng 'NÓNG: NHNN bơm 48.800 tỷ' (TN0611) nhưng là sự kiện MỚI (mua giao ngay, không bán lại), góc khác: con số 255.000 tỷ là dự báo.
# Nguồn:
#  - NHNN thông báo 9/11, áp dụng 11/11/2026: mua USD giao ngay 25.500 đ/USD, thứ Hai + thứ Tư hằng tuần; bên bán: TCTD/CN NHNNg có trạng thái ngoại tệ dương,
#    tối đa đưa trạng thái về cân bằng; không cam kết bán lại; mỗi 1 tỷ USD ≈ 25.500 tỷ đồng (DTTC/SGGP 11/11, cafebiz 11/11).
#  - Giá mua niêm yết trước đó 24.380 → 25.500 cao hơn 1.120 đồng (~4,6%); liên ngân hàng 9/11: 25.547 (cafebiz 11/11, VDSC).
#  - Hoán đổi 6/11/2026: 2 tỷ USD, 182 ngày, mua 24.399 bán lại 24.704, đặt thầu ~2,4 tỷ USD, ~48.800 tỷ đồng, đáo hạn 10/5/2027 (cafebiz; tinnhanhchungkhoan).
#  - ABS (CK An Bình, báo cáo 10/11/2026, ông Nguyễn Thế Minh): kịch bản tới 31/3/2027: 2 tỷ USD ~51.000 tỷ; 6 tỷ USD ~153.000 tỷ (~123% dư nợ OMO, ~0,74% dư nợ tín dụng);
#    10 tỷ USD ~255.000 tỷ. Dự trữ ~87,6 tỷ USD (~1,9–2 tháng nhập khẩu; IMF khuyến nghị 3 tháng); cơ sở 93,6 tỷ USD.
#    Qua đêm 3,7% (3/11) → 4,6% (9/11); OMO 116.381 → 124.862 tỷ; kịch bản cơ sở qua đêm về 3–4%. Xuất siêu T9 1,30 tỷ USD, T10 7,31 tỷ USD.
#    13 lần NHNN mua USD 2016–2023: VN-Index 1 tháng sau tăng 11/13 lần, bình quân +4,35%, trung vị +4,15%, so với bình quân ~0,7%/tháng; 7/13 rơi vào tháng 1–2;
#    ABS: chỉ là tương quan, lần này tác động có thể thấp hơn. Ngành hưởng lợi theo ABS: ngân hàng, chứng khoán, bất động sản. USD/VND dự báo 25.500–26.000 tới cuối 2026.
#  - Người quan sát 11/11: qua đêm 4,4% ngày 10/11; phiên 11/11 NHNN hút ròng 2.892 tỷ qua OMO.
#  - VCB sáng 11/11: mua 25.410, bán 25.820; tỷ giá trung tâm 11/11: 25.611 (DTTC/SGGP; Thời báo Ngân hàng).
#  - CPI 10/2026: +5,09% so cùng kỳ; bình quân 10 tháng +4,57% (TCTK qua Nhân Dân); mục tiêu ~4,5% (ABS).
#  - Lãi suất tiết kiệm đầu 11/2026: phần lớn NH 12 tháng dưới 7%, giảm phổ biến 0,5 điểm (Thị trường Tài chính Tiền tệ).
#  - Dân số 2025: 102,3 triệu (TCTK, WiData – dùng trong CH1411NO).
# SỐ TỰ TÍNH: 153.000 tỷ / 102,3 triệu dân ≈ 1,5 triệu đồng/người; 255.000/48.800 ≈ 5,2 lần;
#   lô hàng 200.000 USD × 25.410 = 5,082 tỷ; nếu USD giảm thêm 2% → ~101,6 triệu (giả định);
#   300 triệu vốn + margin 1:1 = 600 triệu: giảm 10% mất 60 triệu = 20% vốn tự có; không vay: mất 30 triệu = 10%; tăng 4,35%: 26,1 triệu vs 13,05 triệu (chưa trừ lãi vay).
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261112_0815_nong'
KEY = 'NONG1211A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
USD = 'us dollar||US hundred dollar bill'  # v2: 'ov:us dollar banknotes' ra biểu đồ rúp Nga/DXY (Wikideas1) – bỏ
SAN = 'Ho Chi Minh City Stock Exchange||Bitexco Financial Tower'
NHOM = 'Hội chứng sĩ'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('"BƠM 255.000 TỶ', 'ALL IN ĐI ANH EM"'), cols=CR, noti=dict(gio='15:02', ngay='Thứ Tư', items=[
        ('Tin tức', 'Thị trường tiền tệ', 'Từ hôm nay NHNN mua USD giao ngay giá 25.500 đồng, thứ Hai và thứ Tư hằng tuần', X_),
        ('Zalo', NHOM, 'Nhà nước sắp bơm 255.000 tỷ! All in đi anh em', R_),
        ('Zalo', NHOM, 'Ai chưa có margin thì mở ngay kẻo lỡ tàu', V_)]),
      say=("Chiều thứ Tư, mười một tháng mười một, anh Khoa vừa họp xong thì điện thoại rung liên tục. Tin đầu tiên: từ hôm nay, Ngân hàng Nhà nước bắt đầu mua đô la Mỹ giao ngay với giá hai mươi lăm nghìn năm trăm đồng, mỗi tuần hai lần. "
           "Ngay bên dưới, nhóm Zalo chứng khoán của anh nổ tung: Nhà nước sắp bơm hai trăm năm mươi lăm nghìn tỷ, all in đi anh em. Ai chưa có margin thì mở ngay kẻo lỡ tàu.")),
 dict(k='bignum', anh=USD, cap=('GIÁ NHNN MUA MỖI ĐÔ LA', 'TỪ 11/11/2026'), cols=CC, value=25500, fmt='{:,.0f}', unit=' đồng', top='NHNN MUA USD GIAO NGAY', sub='Thứ Hai và thứ Tư hằng tuần', col=GOLD,
      say=("Anh Khoa có ba trăm triệu trong tài khoản, và tay anh đã đặt lên nút đăng ký vay ký quỹ. Nhưng khoan đã. Hai trăm năm mươi lăm nghìn tỷ, ai nói con số đó? "
           "Tiền này đi đâu, ai hưởng lợi thật, và ai có thể là người trả giá? Em cùng anh chị bóc từng lớp của tin nóng nhất tuần này.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Bơm tiền kiểu mới', cap=('"ANH VAY MARGIN', 'THÊM 300 TRIỆU NHÉ"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='15:20', mau=G_, msgs=[
        ('me', 'Nhà nước bơm 255.000 tỷ, anh vay margin thêm 300 triệu nhé'),
        ('Vợ', 'Con số đó ai nói? Thông báo gốc có ghi không?'),
        ('Vợ', 'Em ngày nào cũng bán đô cho ngân hàng, để em đọc kỹ đã')]),
      say=("Anh Khoa nhắn cho vợ: nhà nước bơm hai trăm năm mươi lăm nghìn tỷ, anh vay thêm ba trăm triệu nhé. Chị Mai, vợ anh, làm kế toán cho một công ty may xuất khẩu, ngày nào cũng bán đô la cho ngân hàng. "
           "Chị trả lời đúng một câu: con số đó ai nói, thông báo gốc có ghi không? Để em đọc kỹ đã.")),
 dict(k='giay', cap=('THÔNG BÁO GỐC', 'KHÔNG HỀ CÓ CON SỐ 255.000 TỶ'), cols=CC, moc=True, giay=dict(tieu_de='MUA NGOẠI TỆ GIAO NGAY', so='Tóm tắt theo báo chí ngày 11/11/2026', dau='ĐÃ ĐỌC', dieu=[
        ('Giá mua: 25.500 đồng/USD, áp dụng từ 11/11/2026.', '25.500'),
        ('Lịch mua: thứ Hai và thứ Tư hằng tuần.', '2 LẦN MỖI TUẦN'),
        ('Chỉ mua của ngân hàng đang thừa đô la, không công bố hạn mức.', 'KHÔNG CÓ TỔNG SỐ'),
        ('Không có cam kết bán lại.', 'TIỀN Ở LẠI')]),
      say=("Chị Mai đọc bản tóm tắt nghiệp vụ. Giá mua hai mươi lăm nghìn năm trăm đồng một đô la. Mua vào thứ Hai và thứ Tư hằng tuần. Chỉ mua của những ngân hàng đang thừa đô la, và không công bố tổng hạn mức. "
           "Dòng cuối cùng mới quan trọng: không có cam kết bán lại. Còn con số hai trăm năm mươi lăm nghìn tỷ, chị tìm mãi không thấy trong thông báo.")),
 dict(k='cards', anh=USD, cap=('KHÁC HẲN LẦN 6/11', 'BƠM XONG KHÔNG RÚT VỀ'), cols=CC, moc=True,
      cards=[('48.800 tỷ', 'Hoán đổi 6/11, 182 ngày', 'Phải trả lại 10/5/2027'), ('25.500 tỷ', 'Mỗi 1 tỷ USD mua giao ngay', 'Ở lại trong hệ thống')],
      say=("Đây là điểm khác với lần bơm tiền tuần trước. Ngày sáu tháng mười một, Ngân hàng Nhà nước hoán đổi hai tỷ đô la, đưa ra khoảng bốn mươi tám nghìn tám trăm tỷ đồng. Nhưng sau một trăm tám mươi hai ngày, tiền đó phải quay về. "
           "Lần này thì khác. Cứ mỗi một tỷ đô la mua vào, khoảng hai mươi lăm nghìn năm trăm tỷ đồng được đưa vào hệ thống ngân hàng, và ở lại đó, không có ngày thu hồi cố định.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – 255.000 tỷ từ đâu ra?', anh=USD, cap=('255.000 TỶ LÀ', 'KỊCH BẢN CAO NHẤT'), cols=CR, moc=True,
      cards=[('51.000 tỷ', 'Nếu mua 2 tỷ USD', 'Kịch bản thấp'), ('153.000 tỷ', 'Nếu mua 6 tỷ USD', 'Kịch bản cơ sở'), ('255.000 tỷ', 'Nếu mua 10 tỷ USD', 'Kịch bản cao')],
      say=("Vậy hai trăm năm mươi lăm nghìn tỷ từ đâu ra? Nó đến từ báo cáo của Chứng khoán An Bình ngày mười tháng mười một. Họ đưa ra ba kịch bản đến hết tháng ba năm sau. "
           "Mua hai tỷ đô la, khoảng năm mươi mốt nghìn tỷ đồng. Mua sáu tỷ đô la, khoảng một trăm năm mươi ba nghìn tỷ, đây là kịch bản cơ sở. Chỉ khi mua tới mười tỷ đô la, con số mới là hai trăm năm mươi lăm nghìn tỷ. "
           "Chính báo cáo nói rõ: đây là dự báo, không phải hạn mức Ngân hàng Nhà nước công bố.")),
 dict(k='chat', cap=('"TIỀN ĐÓ VÀO NGÂN HÀNG', 'KHÔNG VÀO TÀI KHOẢN ANH"'), cols=CR, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='15:45', mau=G_, msgs=[
        ('Vợ', '255.000 tỷ là kịch bản cao nhất, tính đến hết tháng 3 năm sau'),
        ('Vợ', 'Mà tiền đó vào ngân hàng, đâu có vào thẳng tài khoản chứng khoán'),
        ('me', 'Thì tiền rẻ, kiểu gì cũng chảy sang chứng khoán chứ em')]),
      say=("Chị Mai nhắn lại: hai trăm năm mươi lăm nghìn tỷ là kịch bản cao nhất, tính tới hết tháng ba năm sau. Mà tiền đó đi vào ngân hàng, đâu có chảy thẳng vào tài khoản chứng khoán. "
           "Anh Khoa vẫn chưa chịu: thì tiền rẻ, kiểu gì cũng chảy sang chứng khoán chứ em. Câu này đúng một nửa, và nửa còn lại mới đáng sợ.")),
 dict(k='bignum', anh='Hanoi skyline night||Hanoi skyline', cap=('CHIA ĐỀU MỖI NGƯỜI DÂN', 'KỊCH BẢN CƠ SỞ'), cols=CC, moc=True, value=1.5, fmt='{:,.1f}', unit=' triệu đồng', top='153.000 TỶ CHIA 102,3 TRIỆU DÂN', sub='Bằng khoảng 0,74% dư nợ cho vay', col=GOLD,
      say=("Em đặt con số vào đúng tầm của nó. Một trăm năm mươi ba nghìn tỷ đồng nghe rất lớn. Nhưng chia đều cho hơn một trăm lẻ hai triệu dân, mỗi người chỉ khoảng một phẩy năm triệu đồng. "
           "So với tổng dư nợ cho vay của cả nền kinh tế, theo An Bình, nó chỉ bằng khoảng không phẩy bảy tư phần trăm. Đủ để làm dịu lãi suất liên ngân hàng, nhưng không phải cơn mưa tiền như nhóm Zalo đang hô.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='cards', ch='Chương 3 – Vì sao Nhà nước mua đô lúc này?', anh='ov:cargo ship containers port||container port', cap=('ĐÔ LA ĐANG VÀO NHIỀU', 'NHNN ĐẶT GIÁ SÀN'), cols=CC, moc=True,
      cards=[('7,31 tỷ USD', 'Xuất siêu tháng 10/2026', 'Đô la đổ về'), ('25.547', 'Tỷ giá liên ngân hàng 9/11', 'Sát mức 25.500'), ('87,6 tỷ USD', 'Dự trữ ngoại hối', 'Khoảng 2 tháng nhập khẩu')],
      say=("Vậy vì sao Ngân hàng Nhà nước mua đô đúng lúc này? Vì đô la đang vào nhiều. Riêng tháng mười, Việt Nam xuất siêu bảy phẩy ba mốt tỷ đô la. Giá đô liên ngân hàng ngày chín tháng mười một chỉ còn hai mươi lăm nghìn năm trăm bốn mươi bảy đồng, sát mức hai mươi lăm nghìn năm trăm. "
           "Mua vào lúc này vừa chặn đà rơi của đô la, vừa bổ sung dự trữ ngoại hối. Dự trữ hiện khoảng tám mươi bảy phẩy sáu tỷ đô la, chỉ đủ chừng hai tháng nhập khẩu, thấp hơn mức ba tháng mà IMF khuyến nghị.")),
 dict(k='noti', cap=('LÔ HÀNG 200.000 ĐÔ', 'ĐÃ CÓ GIÁ SÀN'), cols=CC, moc=True, noti=dict(gio='16:10', ngay='Thứ Tư', items=[
        ('Ngân hàng', 'Tài khoản ngoại tệ công ty', 'Ghi có +200.000 USD tiền hàng từ khách Mỹ', G_),
        ('Ngân hàng', 'Tỷ giá hôm nay', 'Mua chuyển khoản 25.410 đồng/USD', X_)]),
      say=("Chị Mai là người thấy rõ nhất. Bốn giờ chiều, công ty chị nhận hai trăm nghìn đô la tiền hàng từ khách Mỹ. Theo giá mua chuyển khoản sáng nay ở một ngân hàng lớn, hai mươi lăm nghìn bốn trăm mười đồng, lô hàng đổi được khoảng năm phẩy không tám tỷ đồng. "
           "Nếu đô la rơi thêm hai phần trăm, công ty mất khoảng một trăm triệu, đây là con số giả định em tự tính. Giờ đô la đã có một tấm đệm. Doanh nghiệp xuất khẩu là nhóm hưởng lợi đầu tiên.")),
 dict(k='checklist', cap=('AI ĐƯỢC – AI CHƯA ĐƯỢC', 'KHI NHNN MUA ĐÔ LA'), cols=CC, moc=True,
      items=[('Xuất khẩu: đô la có giá đỡ', GREEN), ('Ngân hàng: thêm vốn không kỳ hạn', GREEN), ('Người vay: lãi có thể hạ dần', GREEN), ('Người gửi: lãi khó tăng lên', GOLD)],
      say=("Nhóm thứ hai là ngân hàng. Lãi suất qua đêm liên ngân hàng đã tăng từ ba phẩy bảy phần trăm ngày ba tháng mười một lên bốn phẩy sáu phần trăm ngày chín tháng mười một. Có thêm tiền không kỳ hạn, An Bình cho rằng lãi suất qua đêm có thể về vùng ba đến bốn phần trăm. "
           "Người đi vay có cơ hội được hưởng lãi thấp hơn. Còn người gửi tiết kiệm thì khó vui: đầu tháng mười một, phần lớn ngân hàng đã đưa lãi mười hai tháng xuống dưới bảy phần trăm, nhiều nơi giảm khoảng nửa điểm phần trăm.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='bignum', ch='Chương 4 – Nửa còn lại: lạm phát', anh='Ben Thanh Market||Ho Chi Minh City skyline', cap=('LẠM PHÁT THÁNG 10', 'ĐÃ VƯỢT MỤC TIÊU'), cols=CR, moc=True, value=5.09, fmt='{:,.2f}', unit='%', top='CPI THÁNG 10/2026 SO VỚI CÙNG KỲ', sub='Mục tiêu khoảng 4,5%', col=RED,
      say=("Và đây là nửa còn lại mà anh Khoa chưa nghĩ tới. Tháng mười vừa rồi, chỉ số giá tiêu dùng tăng năm phẩy không chín phần trăm so với cùng kỳ, cao hơn mục tiêu khoảng bốn phẩy năm phần trăm. "
           "Tiền đưa ra nhiều hơn trong lúc giá cả đang lên là con dao hai lưỡi. Chính An Bình cảnh báo: lạm phát có thể buộc Ngân hàng Nhà nước phải hút bớt tiền về, làm giảm tác dụng của đợt bơm này.")),
 dict(k='call', cap=('"TIỀN BƠM RA', 'CŨNG CÓ THỂ BỊ HÚT VỀ"'), cols=CR, call=dict(ten='Anh Tùng', phu='Làm nguồn vốn ngân hàng', mau=X_, loi=[
        'Phiên 11/11 vẫn hút ròng gần 2.900 tỷ', 'Bơm kênh này, hút kênh kia là chuyện thường']),
      say=("Anh Khoa gọi cho anh Tùng, người quen cũ làm ở phòng nguồn vốn một ngân hàng. Anh Tùng cười: ông có biết đúng ngày mười một tháng mười một, trên kênh thị trường mở, Ngân hàng Nhà nước vẫn hút ròng khoảng hai nghìn tám trăm chín mươi hai tỷ đồng không? "
           "Bơm kênh này, hút kênh kia là chuyện bình thường. Họ điều tiết để lãi suất ổn định, chứ không phải để chứng khoán tăng.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='bars', ch='Chương 5 – Lịch sử từng lặp lại', anh=SAN, cap=('13 LẦN NHNN MUA ĐÔ LA', 'VN-INDEX 1 THÁNG SAU'), cols=CC, moc=True,
      bars=[('Sau khi mua USD', 4.35, GREEN, '+4,35%'), ('Tháng bình thường', 0.7, GOLD, '+0,7%')],
      say=("Nhưng lịch sử thì sao? An Bình thống kê mười ba lần Ngân hàng Nhà nước mua đô la từ năm 2016 đến năm 2023. Một tháng sau, VN-Index tăng điểm mười một trên mười ba lần, bình quân tăng bốn phẩy ba lăm phần trăm. "
           "Trong khi đó, một tháng bình thường cả giai đoạn chỉ tăng khoảng không phẩy bảy phần trăm. Nghe rất hấp dẫn, và đó chính là lúc cần đọc tiếp dòng chữ nhỏ.")),
 dict(k='giay', cap=('DÒNG CHỮ NHỎ', 'TRONG CÙNG BÁO CÁO'), cols=CR, moc=True, giay=dict(tieu_de='GHI CHÚ CỦA BÁO CÁO', so='Chứng khoán An Bình, 10/11/2026', dau='LƯU Ý', dieu=[
        ('11/13 lần tăng chỉ là tương quan, chưa phải nhân quả.', 'TƯƠNG QUAN'),
        ('7/13 lần rơi vào tháng 1 và tháng 2.', 'MÙA TẾT'),
        ('Tác động lần này có thể thấp hơn bình quân.', 'THẤP HƠN')]),
      say=("Ngay trong báo cáo đó, An Bình ghi ba lưu ý. Một, đây chỉ là tương quan, chưa đủ để kết luận nhân quả. Hai, bảy trên mười ba lần rơi vào tháng một và tháng hai, mùa thị trường hay tăng trước Tết. "
           "Ba, tác động lần này có thể thấp hơn mức bình quân lịch sử. Nhóm Zalo chỉ chép dòng đầu, bỏ ba dòng sau.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='giay', ch='Chương 6 – Phép tính của anh Khoa', cap=('CÙNG MỘT CÚ GIẢM 10%', 'MẤT GẤP ĐÔI'), cols=CR, moc=True, giay=dict(tieu_de='PHÉP TÍNH TRÊN GIẤY NHÁP', so='Vốn của anh Khoa: 300 triệu đồng', dau='ĐÃ TÍNH', dieu=[
        ('Vay thêm 300 triệu: thị trường tăng 4,35%, lãi 26,1 triệu.', '+26,1 TRIỆU'),
        ('Thị trường giảm 10%: mất 60 triệu, bằng 20% vốn.', 'MẤT 20% VỐN'),
        ('Không vay: giảm 10% mất 30 triệu, bằng 10% vốn.', 'MẤT 10% VỐN')]),
      say=("Tối đó anh Khoa lấy giấy nháp ra tính. Ba trăm triệu vốn, vay thêm ba trăm triệu thành sáu trăm triệu. Nếu thị trường tăng đúng bằng bình quân lịch sử, bốn phẩy ba lăm phần trăm, anh lãi khoảng hai mươi sáu triệu, chưa trừ lãi vay. "
           "Nhưng nếu thị trường giảm mười phần trăm, anh mất sáu mươi triệu, bằng hai mươi phần trăm số vốn thật của mình. Không vay, cùng cú giảm đó chỉ mất ba mươi triệu. Lãi thêm thì nhỏ, rủi ro thì gấp đôi.")),
 dict(k='checklist', anh=SAN, cap=('3 CÂU HỎI', 'KHI NGHE "NHÀ NƯỚC BƠM TIỀN"'), cols=CC, moc=True,
      items=[('Tiền phải trả lại hay ở lại?', GREEN), ('Con số là cam kết hay dự báo?', GREEN), ('Lạm phát có buộc hút tiền về?', GOLD)],
      say=("Nên lần sau nghe tin Nhà nước bơm tiền, em gợi ý anh chị hỏi ba câu. Một, tiền đó phải trả lại sau vài tháng, hay ở lại hệ thống? Hai, con số đang được chia sẻ là cam kết của cơ quan quản lý, hay chỉ là dự báo của một tổ chức? "
           "Ba, lạm phát đang ở đâu, có buộc Ngân hàng Nhà nước hút tiền về không?")),
 dict(k='text', cap=('THEO DÕI THỨ HAI, THỨ TƯ', 'XEM MUA ĐƯỢC BAO NHIÊU'), cols=CC, anh=USD,
      say=("Điều đáng theo dõi tiếp theo rất cụ thể: khối lượng đô la Ngân hàng Nhà nước mua được ở các phiên thứ Hai và thứ Tư. Tỷ giá có giữ quanh hai mươi lăm nghìn năm trăm hay không. Và chỉ số giá tháng mười một. "
           "Muốn xem lợi nhuận, chi phí vốn của các ngân hàng và công ty chứng khoán qua từng quý, anh chị có thể tra miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"ANH KHÔNG VAY NỮA', 'THỨ HAI MÌNH XEM SỐ ĐÃ"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:05', mau=G_, msgs=[
        ('me', 'Anh huỷ đăng ký margin rồi'),
        ('me', 'Thứ Hai tuần sau xem Nhà nước mua được bao nhiêu đô đã'),
        ('Vợ', 'Cả thứ Tư nữa anh. Hai lần một tuần mà')]),
      say=("Mười giờ tối, anh Khoa nhắn cho vợ: anh huỷ đăng ký vay ký quỹ rồi. Thứ Hai tuần sau xem Nhà nước mua được bao nhiêu đô đã. "
           "Chị Mai trả lời: cả thứ Tư nữa anh, hai lần một tuần mà. Trong nhóm Zalo, người ta vẫn đang hô hai trăm năm mươi lăm nghìn tỷ.")),
 dict(k='end', cap=('NGHE "BƠM TIỀN"', 'ANH CHỊ LÀM GÌ ĐẦU TIÊN?'), cols=CC,
      say=("Còn anh chị, mỗi lần nghe tin Nhà nước bơm tiền, việc đầu tiên anh chị làm là gì: đọc thông báo gốc, hỏi người trong ngành, hay vào lệnh ngay? Kể cho em và mọi người ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'NHNN Bơm Tiền Kiểu Mới: Mua USD Giá 25.500, Có Thể Tới 255.000 Tỷ – Tiền Đi Đâu, Ai Hưởng Lợi?'
MT = ("NÓNG: từ 11/11/2026, Ngân hàng Nhà nước mua USD giao ngay giá 25.500 đồng, thứ Hai và thứ Tư hằng tuần, không cam kết bán lại. Nhóm chứng khoán hô \"bơm 255.000 tỷ\" – nhưng đó là kịch bản cao nhất của một báo cáo dự báo. "
      "Tiền đi đâu, ai hưởng lợi (xuất khẩu, ngân hàng, người vay), ai chưa được lợi (người gửi tiết kiệm), và vì sao lạm phát 5,09% là nửa còn lại của câu chuyện.\n\n"
      "Nguồn số liệu:\n"
      "• NHNN mua USD giao ngay 25.500 đ/USD từ 11/11/2026, thứ Hai và thứ Tư; bên bán là TCTD có trạng thái ngoại tệ dương; không cam kết bán lại; mỗi 1 tỷ USD ≈ 25.500 tỷ đồng (SGGP/Đầu tư Tài chính 11/11/2026; CafeBiz 11/11/2026)\n"
      "• Hoán đổi 6/11/2026: 2 tỷ USD, 182 ngày, ≈ 48.800 tỷ đồng, đáo hạn 10/5/2027 (CafeBiz; Tin nhanh chứng khoán 11/11/2026)\n"
      "• Kịch bản đến 31/3/2027: mua 2 / 6 / 10 tỷ USD ≈ 51.000 / 153.000 / 255.000 tỷ đồng; 153.000 tỷ ≈ 0,74% dư nợ tín dụng; dự trữ ngoại hối ≈ 87,6 tỷ USD; qua đêm 3,7% (3/11) lên 4,6% (9/11), kịch bản cơ sở về 3–4%; xuất siêu tháng 10/2026 7,31 tỷ USD; 13 lần NHNN mua USD 2016–2023: VN-Index sau 1 tháng tăng 11/13 lần, bình quân +4,35% (bình quân tháng ≈ 0,7%), 7/13 lần rơi vào tháng 1–2 – Chứng khoán An Bình (ABS), báo cáo 10/11/2026, qua Người Quan Sát, Tin nhanh chứng khoán, Thanh Tra 11/11/2026\n"
      "• Tỷ giá liên ngân hàng 9/11/2026: 25.547 (VDSC qua CafeBiz); giá mua chuyển khoản một NH lớn sáng 11/11: 25.410\n"
      "• Phiên OMO 11/11/2026: NHNN hút ròng 2.892 tỷ đồng (Người Quan Sát 11/11/2026)\n"
      "• CPI 10/2026 +5,09% so cùng kỳ (Tổng cục Thống kê qua báo Nhân Dân); mục tiêu ≈ 4,5%\n"
      "• Lãi suất tiết kiệm đầu 11/2026: phần lớn NH kỳ hạn 12 tháng dưới 7%/năm, giảm phổ biến 0,5 điểm (Thị trường Tài chính Tiền tệ)\n"
      "• Tự tính: 153.000 tỷ / 102,3 triệu dân ≈ 1,5 triệu đồng/người; 200.000 USD × 25.410 ≈ 5,08 tỷ đồng (giảm 2% ≈ 101,6 triệu, giả định); 300 triệu vốn + vay 300 triệu: tăng 4,35% lãi 26,1 triệu (chưa trừ lãi vay), giảm 10% mất 60 triệu = 20% vốn; không vay mất 30 triệu = 10%\n\n"
      "Video trước: NHNN bơm thanh khoản 182 ngày, gần 48.800 tỷ: https://chungkhoanhuynguyen.com/hoc/nong-nhnn-bom-thanh-khoan-182-ngay-gan-48-800-ty-dong-tien-di-dau-ai.html\n"
      "Tra lợi nhuận, chi phí vốn ngân hàng và công ty chứng khoán từng quý: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật anh Khoa, chị Mai, anh Tùng là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-12', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['NHNN mua USD', 'NHNN bơm tiền', 'mua ngoại tệ giao ngay', 'tỷ giá USD hôm nay', 'tỷ giá 25.500', 'lãi suất', 'lạm phát', 'chứng khoán hôm nay', 'tin nóng chứng khoán', 'vĩ mô Việt Nam'],
    bia_hook=['BƠM 255.000 TỶ', 'THẬT KHÔNG?'], badge='NÓNG: NHNN MUA ĐÔ LA',
    bia_anh=USD,
    bia_hook_b=['MUA ĐÔ 25.500', 'AI HƯỞNG LỢI?'], badge_b='TIỀN KHÔNG PHẢI TRẢ',
    bia_hook_c=['11/13 LẦN', 'VN-INDEX TĂNG?'], badge_c='TIN NÓNG 11/11',
    fb_post=("NHNN bắt đầu mua đô la giá 25.500 – nhóm chứng khoán hô \"bơm 255.000 tỷ\" 😳\n\n"
             "👉 255.000 tỷ là kịch bản CAO NHẤT của một báo cáo dự báo, không phải hạn mức\n👉 Lần này tiền không phải trả lại\n👉 Nhưng lạm phát tháng 10 đã 5,09%\n\n"
             "Tiền đi đâu, ai hưởng lợi, ai chưa – xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 12/11: NHNN mua USD giao ngay 25.500 (NV1B 12/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
cnt = Counter(c['k'] for c in S); dt = sum(cnt[k] for k in ('noti', 'chat', 'call', 'giay'))
print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dt/giay', dt, '%.0f%%' % (100 * dt / len(S)), 'tieu', len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
