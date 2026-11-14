# -*- coding: utf-8 -*-
# NV1 15/11/2026 – kênh @5 "Vì Sao Thật Tệ Khi Bắt Đáy Cổ Phiếu Đã Giảm 40%". KHUÔN CHUẨN chi_dao/kenh5_vi_sao_that_te_1011 (XH_BAN, NO_CTA).
# Vụ thật có nguồn:
#  - Giá FLC (WiData, giá điều chỉnh): đỉnh 22.550 ngày 7/1/2022; 10/1 21.400; 19/1 13.000; 21/3 14.950; 29/4 8.820; phiên cuối 8/9/2022 3.570.
#  - VnEconomy 1/2022: HoSE huỷ giao dịch bán 74,8 triệu cổ phiếu FLC của chủ tịch tập đoàn thực hiện ngày 10/1/2022 không báo cáo trước;
#    Thời báo Tài chính VN 1/2022: chủ tịch FLC bị phạt 1,5 tỷ đồng, đình chỉ giao dịch 5 tháng (sau đó UBCKNN huỷ quyết định – Nhà Đầu Tư; KHÔNG nhắc chi tiết này).
#  - Thời báo Tài chính VN 2/2023: đầu tháng 9/2022 HoSE đình chỉ giao dịch FLC (chưa họp ĐHĐCĐ, chưa công bố BCTC kiểm toán 2021, chưa chọn kiểm toán);
#    huỷ niêm yết bắt buộc 709.997.807 cổ phiếu từ 20/2/2023 vì vi phạm nghiêm trọng công bố thông tin.
#  - VnEconomy / Thời báo Tài chính VN 3/2023: FLC lên UPCoM ngày 3/3/2023 và bị đình chỉ giao dịch ngay trong ngày.
#  - Vietnambiz 31/8/2026: FLC mất tư cách công ty đại chúng từ 18/12/2025, VSDC huỷ đăng ký gần 710 triệu cổ phiếu; từ 6/3/2026 chỉ chuyển nhượng qua CTCK Artex.
#  - Stockbiz 28/7/2026 (BCTC quý 2/2026 Artex): danh mục cổ phiếu hệ sinh thái FLC giá gốc hơn 269 tỷ, giá trị hợp lý khoảng 9,2 tỷ, giảm gần 97%.
# SỐ TỰ TÍNH (nhân vật giả định): 13.000/22.550 = 0,576 → đã giảm 42%; 100 triệu/13.000 = 7.692 cp; 100 triệu/8.820 = 11.338 cp; tổng 19.030 cp,
#   giá vốn bình quân 200 triệu/19.030 = 10.510; × 3.570 = 67,9 triệu → mất 132 triệu = 66%. 22.550/3.570 = 6,32 → phải tăng 532% mới về đỉnh.
#   14.950/13.000 = +15%.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261115_0100_vt'
KEY = 'VT5BATDAY'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
SGD = 'ov:Ho Chi Minh City Stock Exchange||Bitexco Financial Tower'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('BỐN NĂM KHÔNG BÁN ĐƯỢC', 'MỘT CỔ PHIẾU NÀO'), cols=CR, noti=dict(gio='20:10', ngay='Thứ Sáu', items=[
        ('App chứng khoán', 'Danh mục', 'Mã FLC: giá 3.570, giao dịch lần cuối 08/09/2022', R_),
        ('Zalo', 'Hùng', 'Ông còn ôm FLC không? Giờ chỉ bán được qua một công ty thôi', V_),
        ('App chứng khoán', 'Tài sản', 'Lỗ: 132.000.000 đồng, tương đương 66%', R_)]),
      say=("Tối thứ sáu, bạn mở ứng dụng chứng khoán. Dòng thứ hai trong danh mục vẫn đứng im ở một con số: ba nghìn năm trăm bảy mươi đồng. Lần giao dịch cuối cùng là ngày 8/9/2022. "
           "Bốn năm rồi, bạn chưa bán được một cổ phiếu nào. Hai trăm triệu tiền tiết kiệm, giờ trên màn hình chỉ còn sáu mươi tám triệu, mà sáu mươi tám triệu đó cũng không rút ra được. "
           "Điều trớ trêu là: bạn mua nó vì nghĩ nó đã rẻ. Đây là câu chuyện vì sao thật tệ khi bắt đáy một cổ phiếu chỉ vì nó đã giảm bốn mươi phần trăm.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Giảm bốn mươi phần trăm, rẻ rồi', cap=('"GIẢM 42% RỒI', 'CÒN ĐI ĐÂU NỮA"'), cols=CR, moc=True, chat=dict(ten='Hùng', tv='Đang hoạt động', gio='14:50', mau=V_, msgs=[
        ('Hùng', 'Mã này tuần trước 22.550, nay còn 13.000'),
        ('Hùng', 'Giảm hơn 40% rồi, đáy rồi ông ạ'),
        ('me', 'Chuyện gì mà giảm nhanh vậy?'),
        ('Hùng', 'Tin xấu ra hết rồi, giờ chỉ có lên thôi')]),
      say=("Tháng một năm 2022. Hùng, đồng nghiệp ngồi bàn bên, nhắn cho bạn: mã này tuần trước còn hai mươi hai nghìn năm trăm năm mươi, nay chỉ còn mười ba nghìn. Giảm hơn bốn mươi phần trăm rồi, đáy rồi. "
           "Bạn hỏi chuyện gì mà giảm nhanh vậy. Hùng bảo: tin xấu ra hết rồi, giờ chỉ có lên thôi. Bạn chưa đọc tin xấu đó là gì. Bạn chỉ nhìn thấy một chữ: rẻ.")),
 dict(k='giay', cap=('LỆNH MUA ĐẦU TIÊN', '100 TRIỆU Ở GIÁ 13.000'), cols=CC, moc=True, giay=dict(tieu_de='XÁC NHẬN LỆNH KHỚP 19/01/2022', so='Giả định minh hoạ', dau='ĐÃ KHỚP', dieu=[
        ('Mã cổ phiếu: FLC', 'MUA'),
        ('Giá khớp', '13.000'),
        ('Số lượng', '7.692 CP'),
        ('Tổng tiền', '100 TRIỆU')]),
      say=("Sáng 19/1/2022, bạn đặt lệnh. Một trăm triệu, giá mười ba nghìn, được khoảng bảy nghìn sáu trăm chín mươi hai cổ phiếu. "
           "Hai tháng sau, giá hồi lên mười bốn nghìn chín trăm năm mươi, bạn lãi mười lăm phần trăm. Bạn chụp màn hình gửi Hùng: thấy chưa, bắt đáy là phải dứt khoát.")),
 dict(k='bignum', anh=SGD, cap=('ĐỈNH 22.550 NGÀY 7/1/2022', 'BA TUẦN SAU CÒN 11.200'), cols=CR, moc=True, value=-50, fmt='{:+,.0f}', unit='%', top='TRONG 13 PHIÊN', sub='22.550 xuống 11.200, giá điều chỉnh – WiData', col=RED,
      say=("Nhưng bạn không biết vì sao giá rơi. Phiên 7/1/2022, mã này đóng cửa ở hai mươi hai nghìn năm trăm năm mươi đồng. Chỉ mười ba phiên sau, phiên 25/1/2022, còn mười một nghìn hai trăm. Mất một nửa. "
           "Và người bán đầu tiên, trước khi bạn kịp hiểu chuyện gì, lại là người hiểu doanh nghiệp này rõ nhất.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='giay', ch='Chương 2 – Người bán là ai?', cap=('NGƯỜI BÁN ĐẦU TIÊN', 'LÀ CHÍNH CHỦ TỊCH'), cols=CR, moc=True, giay=dict(tieu_de='CHUYỆN NÀY CÓ THẬT – THÁNG 1/2022', so='VnEconomy 1/2022, giá WiData', dau='ĐÃ XẢY RA', dieu=[
        ('Ngày bán không báo trước', '10/01/2022'),
        ('Số cổ phiếu chủ tịch bán ra', '74,8 TRIỆU'),
        ('Sở giao dịch', 'HUỶ GIAO DỊCH'),
        ('Giá 13 phiên sau đỉnh', 'MẤT 50%')]),
      say=("Chuyện này có thật. Phiên 10/1/2022, chủ tịch tập đoàn FLC bán ra bảy mươi bốn phẩy tám triệu cổ phiếu mà không báo cáo trước. Sở Giao dịch Chứng khoán Thành phố Hồ Chí Minh sau đó huỷ giao dịch này. "
           "Khi tin này lan ra, giá giảm sàn nhiều phiên liền. "
           "Cú giảm bốn mươi phần trăm mà bạn gọi là rẻ, thật ra là lúc người trong cuộc đang tìm cách thoát ra.")),
 dict(k='call', cap=('"TRUNG BÌNH GIÁ ĐI,', 'GIÁ VỐN XUỐNG CÒN 10.500"'), cols=CR, moc=True, call=dict(ten='Hùng', phu='Cuộc gọi đến', mau=V_, loi=[
        'Giá 8.820 rồi, mua thêm đi cho giá vốn thấp xuống', 'Mua càng rẻ, lúc hồi càng lãi nhiều']),
      say=("Cuối tháng tư, giá còn tám nghìn tám trăm hai mươi. Hùng gọi: mua thêm đi, trung bình giá, giá vốn sẽ xuống. Mua càng rẻ, lúc hồi càng lãi nhiều. "
           "Bạn rút nốt một trăm triệu, mua thêm khoảng mười một nghìn ba trăm cổ phiếu. Giá vốn bình quân của bạn còn khoảng mười nghìn năm trăm. Nghe rất hợp lý. Cho tới khi bạn biết công ty này đang thiếu thứ gì.")),
 dict(k='giay', cap=('SỔ LỆNH CỦA BẠN', 'GẤP ĐÔI TIỀN, CHƯA ĐỌC TRANG NÀO'), cols=CR, moc=True, giay=dict(tieu_de='SỔ LỆNH – MÃ FLC', so='Giả định minh hoạ', dau='ĐÃ KHỚP', dieu=[
        ('Lệnh 1, ngày 19/01/2022, giá 13.000', '100 TR'),
        ('Lệnh 2, ngày 29/04/2022, giá 8.820', '100 TR'),
        ('Tổng số cổ phiếu', '19.030'),
        ('Giá vốn bình quân', '10.510')]),
      say=("Bạn mở sổ lệnh ra xem lại. Lệnh thứ nhất một trăm triệu ở giá mười ba nghìn. Lệnh thứ hai một trăm triệu ở giá tám nghìn tám trăm hai mươi. Tổng cộng khoảng mười chín nghìn cổ phiếu, giá vốn bình quân mười nghìn năm trăm mười đồng. "
           "Bạn thấy yên tâm hơn vì giá vốn đã thấp xuống. Nhưng sự thật là bạn vừa nhân đôi số tiền đặt vào một doanh nghiệp mà bạn chưa đọc nổi một trang báo cáo nào.")),
 dict(k='text', cap=('CÁI BẪY TÊN LÀ', 'NEO GIÁ'), cols=CR, anh=HN,
      say=("Cái bẫy này có tên: neo giá. Não của bạn neo vào con số hai mươi hai nghìn năm trăm năm mươi, nên mười ba nghìn trông như hàng giảm giá, tám nghìn trông như hàng thanh lý. "
           "Nhưng thị trường không quan tâm bạn từng thấy giá bao nhiêu. Giá cũ chỉ là ký ức. Thứ duy nhất quyết định một cổ phiếu đắt hay rẻ là doanh nghiệp phía sau nó đang làm ăn ra sao, và có nói thật với cổ đông hay không.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='giay', ch='Chương 3 – Cánh cửa đóng lại', cap=('ĐÌNH CHỈ GIAO DỊCH', 'TỪ ĐẦU THÁNG 9/2022'), cols=CR, moc=True, giay=dict(tieu_de='THÔNG BÁO CỦA SỞ GIAO DỊCH – 9/2022', so='Thời báo Tài chính Việt Nam', dau='ĐÌNH CHỈ', dieu=[
        ('Chưa họp đại hội cổ đông năm 2022', 'VI PHẠM'),
        ('Chưa công bố báo cáo kiểm toán 2021', 'VI PHẠM'),
        ('Chưa chọn công ty kiểm toán', 'VI PHẠM'),
        ('Giao dịch cổ phiếu', 'ĐÌNH CHỈ')]),
      say=("Đầu tháng chín năm 2022, Sở Giao dịch chuyển mã này từ hạn chế sang đình chỉ giao dịch. Lý do: công ty chưa họp đại hội cổ đông, chưa công bố báo cáo tài chính kiểm toán năm 2021, và chưa chọn được công ty kiểm toán. "
           "Phiên cuối cùng, ngày 8/9/2022, giá đóng cửa ba nghìn năm trăm bảy mươi đồng. Từ hôm đó, cánh cửa đóng lại. Bạn không còn nút bán.")),
 dict(k='cards', anh=TP, cap=('TÀI KHOẢN CỦA BẠN', 'MẤT 66% VÀ BỊ KHOÁ'), cols=CR, moc=True,
      cards=[('200 triệu', 'Tiền bạn bỏ vào, 2 lần mua', 'Tiền tiết kiệm nhiều năm'), ('67,9 triệu', 'Giá trị ở phiên cuối', 'Mất 66% vốn'), ('4 năm', 'Không có phiên nào để bán', 'Tiền bị khoá')],
      say=("Mười chín nghìn cổ phiếu nhân với ba nghìn năm trăm bảy mươi đồng, bạn còn khoảng sáu mươi bảy phẩy chín triệu. Mất sáu mươi sáu phần trăm vốn. "
           "Nhưng lỗ chưa phải phần tệ nhất. Phần tệ nhất là bạn không thể bán, kể cả khi chấp nhận lỗ. Số tiền đó bị khoá lại, không biết đến bao giờ.")),
 dict(k='bignum', anh=HN, cap=('MUỐN VỀ LẠI ĐỈNH', 'PHẢI TĂNG 532%'), cols=CR, moc=True, value=532, fmt='{:,.0f}', unit='%', top='TỪ 3.570 VỀ LẠI 22.550', sub='mình tự tính: 22.550 chia 3.570', col=RED,
      say=("Mình làm một phép tính. Từ ba nghìn năm trăm bảy mươi muốn quay về hai mươi hai nghìn năm trăm năm mươi, giá phải tăng năm trăm ba mươi hai phần trăm. "
           "Đó là lý do người ta nói: cổ phiếu đã giảm tám mươi phần trăm vẫn có thể giảm thêm một nửa. Giảm nhiều không có nghĩa là rẻ. Có khi nó chỉ đang phản ánh đúng giá trị thật.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='noti', ch='Chương 4 – Bốn năm sau', cap=('LÊN UPCOM ĐÚNG MỘT NGÀY', 'RỒI ĐÌNH CHỈ NGAY'), cols=CR, moc=True, noti=dict(gio='09:00', ngay='Thứ Sáu', items=[
        ('Tin tức', '20/02/2023', 'Huỷ niêm yết bắt buộc gần 710 triệu cổ phiếu FLC', R_),
        ('Tin tức', '03/03/2023', 'Lên UPCoM rồi bị đình chỉ giao dịch ngay trong ngày', R_),
        ('Tin tức', '18/12/2025', 'Mất tư cách công ty đại chúng', R_)]),
      say=("Từ 20/2/2023, gần bảy trăm mười triệu cổ phiếu bị huỷ niêm yết bắt buộc vì vi phạm nghiêm trọng việc công bố thông tin. Sáng 3/3/2023, mã này lên sàn UPCoM, rồi bị đình chỉ giao dịch ngay trong ngày. "
           "Đến 18/12/2025, công ty mất tư cách công ty đại chúng, theo báo Vietnambiz. Từ tháng ba năm nay, cổ đông chỉ còn chuyển nhượng được qua đúng một công ty chứng khoán.")),
 dict(k='chat', cap=('"CÔNG TY CHỨNG KHOÁN', 'CŨNG ĐANG KẸT NHƯ ÔNG"'), cols=CR, moc=True, chat=dict(ten='Hùng', tv='Đang hoạt động', gio='21:30', mau=V_, msgs=[
        ('me', 'Bán qua công ty đó được giá bao nhiêu?'),
        ('Hùng', 'Chính họ cũng đang kẹt cổ phiếu cùng hệ đấy'),
        ('Hùng', 'Giá gốc 269 tỷ, giờ ghi nhận còn 9,2 tỷ'),
        ('me', 'Mất 97%...')]),
      say=("Bạn hỏi Hùng: bán qua công ty đó thì được giá bao nhiêu. Hùng gửi một bài báo. Theo báo cáo tài chính quý hai năm nay, chính công ty chứng khoán đó đang giữ cổ phiếu cùng hệ sinh thái, giá gốc hơn hai trăm sáu mươi chín tỷ đồng. "
           "Giờ giá trị hợp lý chỉ còn khoảng chín phẩy hai tỷ. Mất gần chín mươi bảy phần trăm. Người được giao giữ sổ cổ đông cũng đang kẹt giống bạn.")),
 dict(k='chat', cap=('"TIỀN ĐẶT CỌC NHÀ', 'MÌNH ĐÂU ANH?"'), cols=CR, moc=True, chat=dict(ten='Hà – vợ', tv='Đang hoạt động', gio='22:40', mau=X_, msgs=[
        ('Hà – vợ', 'Chủ nhà hỏi tiền đặt cọc căn hộ đấy anh'),
        ('me', 'Anh để trong cổ phiếu, chưa bán được em ạ'),
        ('Hà – vợ', 'Chưa bán được là sao? Bao giờ mới bán được?'),
        ('me', 'Anh cũng không biết nữa')]),
      say=("Tối đó, Hà, vợ bạn, nhắn tin: chủ nhà hỏi tiền đặt cọc căn hộ. Hai trăm triệu ấy vốn là tiền để dành mua nhà. Bạn trả lời: anh để trong cổ phiếu, chưa bán được. "
           "Hà hỏi lại: chưa bán được là sao, bao giờ mới bán được. Bạn nhìn màn hình rất lâu, rồi gõ một câu thật nhất trong bốn năm qua: anh cũng không biết nữa.")),
 dict(k='text', cap=('BẮT ĐÁY KHÔNG SAI', 'BẮT ĐÁY MÙ MỚI SAI'), cols=CR, anh=SGD,
      say=("Bắt đáy không phải lúc nào cũng sai. Có những cổ phiếu tốt bị bán tháo cùng thị trường, rồi hồi lại. Cái sai của bạn là mua chỉ vì giá đã giảm, mà không hỏi giá giảm vì đâu. "
           "Khi người trong cuộc bán ra và báo cáo kiểm toán chưa có, cú giảm không phải cơ hội. Đó là lời cảnh báo.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Bốn câu hỏi trước khi bắt đáy', anh=TP, cap=('4 CÂU HỎI', 'TRƯỚC KHI BẮT ĐÁY'), cols=CC, moc=True,
      items=[('Vì sao giá giảm? Đọc tin gốc', GOLD),
             ('Ban lãnh đạo đang mua hay bán?', RED),
             ('Có báo cáo kiểm toán đúng hạn?', RED),
             ('Mất hết khoản này có sao không?', GOLD)],
      say=("Trước khi bắt đáy, bạn tự hỏi bốn câu. Một: giá giảm vì đâu, đọc tin gốc trên trang của sở giao dịch chứ không đọc lời đồn. Hai: ban lãnh đạo và cổ đông lớn đang mua vào hay bán ra. "
           "Ba: công ty có công bố báo cáo tài chính kiểm toán đúng hạn không, chậm nộp là cờ đỏ lớn nhất. Bốn: nếu khoản tiền này mất trắng và bị khoá nhiều năm, cuộc sống của bạn có bị ảnh hưởng không.")),
 dict(k='cards', anh=HN, cap=('NẾU VẪN MUỐN BẮT ĐÁY', '3 NGUYÊN TẮC TỰ ĐẶT'), cols=CC, moc=True,
      cards=[('Dưới 10%', 'Tiền cho một lệnh bắt đáy', 'Mất cũng không đau'), ('0 lần', 'Trung bình giá khi chưa rõ lý do', 'Không mua thêm mù'), ('1 mức cắt', 'Viết ra trước khi bấm mua', 'Sai thì thoát')],
      say=("Nếu vẫn muốn bắt đáy, đây là ba nguyên tắc mình tự đặt cho mình, không phải quy định chung. Một lệnh bắt đáy không quá mười phần trăm số tiền đầu tư. "
           "Không trung bình giá khi chưa biết vì sao giá giảm. Và viết ra mức chấp nhận sai trước khi bấm nút mua, để khi sai thì còn đường ra, lúc sàn vẫn còn mở cửa.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối', cap=('"LẦN SAU,', 'ĐỌC TIN TRƯỚC KHI ĐỌC GIÁ"'), cols=CC, moc=True, chat=dict(ten='Hùng', tv='Đang hoạt động', gio='22:15', mau=V_, msgs=[
        ('Hùng', 'Xin lỗi ông, hồi đó tôi cũng chỉ nhìn giá'),
        ('me', 'Không sao. Lần sau đọc tin trước khi đọc giá'),
        ('me', 'Và không bao giờ bỏ hết tiền vào một mã')]),
      say=("Hùng nhắn một câu xin lỗi, hồi đó anh ấy cũng chỉ nhìn giá. Bạn trả lời: không sao, lần sau đọc tin trước khi đọc giá, và không bao giờ dồn hết tiền vào một mã. "
           "Hai trăm triệu là học phí đắt. Nhưng nếu câu chuyện này giúp ai đó dừng tay trước một lệnh bắt đáy mù, thì nó không hoàn toàn mất trắng.")),
 dict(k='end', cap=('BẠN ĐÃ TỪNG', 'BẮT ĐÁY HỤT CHƯA?'), cols=CC,
      say=("Bạn đã từng bắt đáy một cổ phiếu rồi kẹt chưa, và bạn đã thoát ra thế nào? Kể ở phần bình luận để mọi người cùng tránh nhé. "
           "Tập sau: vì sao thật tệ khi dồn hết tiền vào một mã cổ phiếu.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vì Sao Thật Tệ Khi Bắt Đáy Cổ Phiếu "Đã Giảm 40%" | 4 Năm Không Bán Được, Mất 66%'
MT = ("Tháng 1/2022, một cổ phiếu giảm từ 22.550 xuống 13.000 đồng chỉ trong vài tuần. \"Giảm hơn 40% rồi, đáy rồi\". Bạn bỏ 100 triệu bắt đáy, rồi trung bình giá thêm 100 triệu. "
      "Đầu tháng 9/2022, cổ phiếu bị đình chỉ giao dịch ở 3.570 đồng. Bốn năm sau, vẫn không có phiên nào để bán.\n\n"
      "Câu chuyện nhân vật là giả định, nhưng vụ việc là thật:\n"
      "• Giá cổ phiếu FLC (WiData, giá điều chỉnh): 22.550 ngày 7/1/2022; 13.000 ngày 19/1; 11.200 ngày 25/1; 14.950 ngày 21/3; 8.820 ngày 29/4; phiên cuối 8/9/2022: 3.570\n"
      "• VnEconomy 1/2022: HoSE huỷ giao dịch bán 74,8 triệu cổ phiếu FLC của chủ tịch tập đoàn thực hiện ngày 10/1/2022 không báo cáo trước\n"
      "• Thời báo Tài chính Việt Nam 2/2023: HoSE đình chỉ giao dịch FLC từ đầu tháng 9/2022 (chưa họp ĐHĐCĐ, chưa công bố BCTC kiểm toán 2021, chưa chọn kiểm toán); huỷ niêm yết bắt buộc 709.997.807 cổ phiếu từ 20/2/2023\n"
      "• VnEconomy 3/2023: FLC lên UPCoM ngày 3/3/2023 và bị đình chỉ giao dịch ngay trong ngày\n"
      "• Vietnambiz 31/8/2026: FLC mất tư cách công ty đại chúng từ 18/12/2025; từ 6/3/2026 cổ đông chuyển nhượng qua một công ty chứng khoán quản lý sổ cổ đông\n"
      "• Stockbiz 28/7/2026 (BCTC quý 2/2026 của công ty chứng khoán đó): danh mục cổ phiếu hệ sinh thái FLC giá gốc hơn 269 tỷ, giá trị hợp lý khoảng 9,2 tỷ, giảm gần 97%\n"
      "• Tự tính: 13.000/22.550 = giảm 42%; 100 triệu/13.000 = 7.692 cổ phiếu, 100 triệu/8.820 = 11.338 cổ phiếu; 19.030 × 3.570 = 67,9 triệu (mất 66%); 22.550/3.570 = 6,32 → phải tăng 532%\n\n"
      "Kênh chính: https://www.youtube.com/@chungkhoanhuynguyen\n\n"
      "Nhân vật là hư cấu; 3 nguyên tắc ở chương 5 là mốc tự đặt, không phải quy định. Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen5', seri='Vì sao thật tệ khi…', ngay='2026-11-20', gio_goi_y='20:00', gio='20:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['bắt đáy cổ phiếu', 'trung bình giá', 'cổ phiếu FLC', 'huỷ niêm yết', 'đình chỉ giao dịch', 'bán chui cổ phiếu', 'bài học đầu tư', 'vì sao thật tệ khi'],
    bia_hook=['GIẢM 42%', 'TƯỞNG LÀ ĐÁY'], badge='VÌ SAO THẬT TỆ KHI…',
    bia_anh='Ho Chi Minh City skyline night||Hanoi skyline night',
    bia_hook_b=['4 NĂM', 'KHÔNG BÁN ĐƯỢC'], badge_b='CHUYỆN THẬT 2022',
    bia_hook_c=['200 TRIỆU', 'CÒN 67,9 TRIỆU'], badge_c='VÌ SAO THẬT TỆ KHI…',
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh phụ @chungkhoanhuynguyen5 – 'bắt đáy cổ phiếu đã giảm 40 phần trăm' (NV1 15/11/2026).\n"
    "XH_BAN = True; NO_CTA = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
cnt = Counter(c['k'] for c in S); dt = sum(cnt[k] for k in ('chat', 'noti', 'call', 'giay'))
print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dien thoai/giay %d/%d' % (dt, len(S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
