# -*- coding: utf-8 -*-
# NV1B 16/11/2026 – VIDEO NÓNG kênh chính: dư nợ margin kỷ lục 457.500 tỷ + làn bán giải chấp cổ phiếu người liên quan lãnh đạo DN (11–16/11).
# Lý do chọn: tin chứng khoán nóng nhất tuần (CafeF 11/11, Người Quan Sát 12/11, Dân trí + VietTimes 13/11, Vietstock "Đọc gì" 16/11 nhắc lại);
#   chủ đề NỖI SỢ / CÚ SẬP / TIỀN TRONG TÚI (công thức thắng của kênh). WiData hết credit tới 00:00 20/11 → nguồn báo, ghi tên báo + ngày.
#   Khác CH2111FED (Fed/2022, vay ký quỹ chỉ là ví dụ phụ): video này nói hệ thống margin – ai thu lãi, cơ chế giải chấp dây chuyền.
# Nguồn:
#  - SGI Capital (báo cáo triển vọng tháng 11, dữ liệu FiinTrade) qua VietTimes 13/11, CafeF 11/11, Người Quan Sát 12/11/2026:
#    margin cuối Q3/2026 457.500 tỷ; >5,3% vốn hoá, 14,2% free-float; gấp 2,5 lần đỉnh Q1/2022; tiền mặt NĐT 71.500 tỷ (−15%);
#    lãi NĐT trả ~13.000 tỷ mỗi quý (~52.000 tỷ/năm nếu giữ – Người Quan Sát); cho vay bình quân 40% thị giá → khoảng 1/3 free-float HoSE+HNX cầm cố;
#    một số người vay cầm cổ phiếu rồi rút tiền khỏi thị trường; vài mã giảm sàn nhiều phiên, lượng bán 15–50% vốn hoá; định giá đã hấp dẫn hơn nhưng cần giảm đòn bẩy.
#  - VietTimes 13/11: VDSC – GTGD bình quân HoSE tháng 10: 12.380 tỷ/phiên, thấp nhất từ đầu 2025; chuyên gia ABS: CTCK chỉ cho vay tối đa 2 lần vốn chủ, rủi ro đáng chú ý nhưng chưa báo động.
#  - Báo Pháp luật (Doanh nhân) 11/2026: 78 CTCK; margin +11.700 tỷ so Q2, +14,1% (56.400 tỷ) so cuối 2025; GTGD bình quân Q3/2026 ~14.800 tỷ/phiên, −22,6% so Q2, −63,6% so Q3/2025.
#  - Dân trí 13/11/2026: 2,8 triệu cp của người nhà Chủ tịch một DN dự kiến bị bán giải chấp từ 12/11; 7 cá nhân, tổ chức liên quan ban lãnh đạo một DN khác bị bán giải chấp >45,33 triệu cp từ 27/10 đến 10/11;
#    một mã HNX còn 2.800 đồng so ~8.500 đầu năm (≈ −67%).
#  - Vietstock 16/11/2026: tuần 9–13/11 VN-Index tăng gần 10 điểm; mã đó (HNX) giảm sàn toàn bộ các phiên; dư nợ margin tăng mạnh, một số CTCK vừa và nhỏ liên tiếp thông báo bán giải chấp.
#  - VN-Index 31/12/2021: 1.498,28; 30/12/2022: 1.007,09 (BSC Daily Review 30/12/2022) → −32,8% (tự tính).
# SỐ TỰ TÍNH: 13.000 tỷ ÷ 91 ngày ≈ 143 tỷ mỗi ngày; 457.500 ÷ 71.500 ≈ 6,4 lần.
#   Giả định anh Dũng: 600 triệu cổ phiếu, vay ký quỹ 240 triệu (40%), vốn thật 360 triệu; lãi giả định 12% mỗi năm → 28,8 triệu/năm = 2,4 triệu mỗi tháng = 4,8% giá trị danh mục.
#   Giảm 20%: 480 − 240 = 240 → mất 120/360 = 33,3% vốn. Ngưỡng gọi ký quỹ giả định 40%: 1 − 240/(600(1−x)) = 0,4 → x = 33,3%.
#   Trả nửa nợ (bán 120 triệu): 480 cổ phiếu, nợ 120, vốn 360; giảm 20%: 384 − 120 = 264 → mất 96/360 = 26,7%; ngưỡng: 480(1−x) = 200 → x ≈ 58,3%; lãi còn 1,2 triệu mỗi tháng.
#   Phép thử: giảm 20% → mất 20% × (tài sản ÷ vốn): không vay 20%; vay bằng nửa vốn 30%; vay bằng vốn 40%.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261116_0830_nong'
KEY = 'NONG1611A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
BX = 'ov:Bitexco Financial Tower||Bitexco Financial Tower'
NHA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('MARGIN KỶ LỤC 457.500 TỶ', 'TÀI KHOẢN ANH CÓ TRONG ĐÓ?'), cols=CR, noti=dict(gio='08:05', ngay='Thứ Hai', items=[
        ('Tin tức', 'Chứng khoán', 'Dư nợ vay ký quỹ lập kỷ lục 457.500 tỷ đồng, cảnh báo bán giải chấp', X_),
        ('Công ty chứng khoán', 'Tài khoản ký quỹ', 'Tỷ lệ ký quỹ hiện tại: 60%. Ngưỡng cảnh báo: 40%', R_)]),
      say=("Tám giờ sáng thứ Hai, anh Dũng đọc tin nóng của tuần. Dư nợ vay ký quỹ chứng khoán, tức margin, đã lập kỷ lục bốn trăm năm mươi bảy nghìn năm trăm tỷ đồng vào cuối quý ba. "
           "Cùng lúc, cổ phiếu của người liên quan lãnh đạo nhiều doanh nghiệp niêm yết bị bán giải chấp. Một phút sau, ứng dụng chứng khoán báo: tỷ lệ ký quỹ của anh là sáu mươi phần trăm, ngưỡng cảnh báo là bốn mươi. Anh chưa bao giờ để ý khoảng cách đó.")),
 dict(k='bignum', anh=TP, cap=('143 TỶ TIỀN LÃI', 'MỖI NGÀY'), cols=CR, value=143, fmt='{:,.0f}', unit=' tỷ đồng', top='LÃI VAY KÝ QUỸ MỖI NGÀY', sub='Em tự tính từ 13.000 tỷ mỗi quý', col=RED,
      say=("Theo SGI Capital, người vay ký quỹ đang trả khoảng mười ba nghìn tỷ đồng tiền lãi mỗi quý. Em chia cho chín mươi mốt ngày, ra khoảng một trăm bốn mươi ba tỷ đồng mỗi ngày, kể cả thứ Bảy, Chủ nhật. "
           "Vậy tiền vay đang nằm ở đâu, ai hưởng lợi, và ai đang ngồi gần ngưỡng bị bán giải chấp?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Con số kỷ lục nói gì?', cap=('"457 NGHÌN TỶ', 'LÀ NHIỀU HAY ÍT?"'), cols=CC, moc=True, chat=dict(ten='Hải', tv='Đang hoạt động', gio='08:20', mau=G_, msgs=[
        ('me', 'Margin kỷ lục 457 nghìn tỷ, nhiều hay ít hả ông?'),
        ('Hải', 'So với tiền mặt nhà đầu tư đang để chờ mua thì gấp hơn 6 lần'),
        ('Hải', 'Ông đang vay bao nhiêu?')]),
      say=("Anh Dũng nhắn cho Hải, người quen làm kế toán: bốn trăm năm mươi bảy nghìn tỷ là nhiều hay ít? Hải trả lời gọn: so với tiền mặt nhà đầu tư đang để chờ mua, thì gấp hơn sáu lần. Rồi Hải hỏi lại: ông đang vay bao nhiêu?")),
 dict(k='giay', cap=('BÁO CÁO THÁNG 11', 'NỢ TĂNG, TIỀN MẶT GIẢM'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ VAY KÝ QUỸ', so='Theo SGI Capital, dữ liệu FiinTrade, cuối quý 3/2026', dau='ĐÃ ĐỌC', dieu=[
        ('Dư nợ vay ký quỹ: 457.500 tỷ đồng.', 'KỶ LỤC'),
        ('Bằng 14,2% giá trị cổ phiếu tự do chuyển nhượng.', '14,2%'),
        ('Gấp 2,5 lần đỉnh quý 1/2022.', 'GẤP 2,5 LẦN'),
        ('Tiền mặt nhà đầu tư: 71.500 tỷ, giảm 15%.', 'TIỀN MẶT GIẢM')]),
      say=("Hải gửi sang bản tóm tắt báo cáo tháng mười một của SGI Capital. Một, dư nợ vay ký quỹ cuối quý ba là bốn trăm năm mươi bảy nghìn năm trăm tỷ đồng. Hai, con số đó bằng mười bốn phẩy hai phần trăm giá trị cổ phiếu tự do chuyển nhượng. "
           "Ba, gấp hai phẩy năm lần đỉnh của quý một năm 2022. Bốn, tiền mặt nhà đầu tư để ở công ty chứng khoán chỉ còn bảy mươi mốt nghìn năm trăm tỷ, giảm mười lăm phần trăm.")),
 dict(k='bignum', anh=HN, cap=('TIỀN VAY GẤP 6,4 LẦN', 'TIỀN MẶT CHỜ MUA'), cols=CR, moc=True, value=6.4, fmt='{:,.1f}', unit=' lần', top='NỢ KÝ QUỸ SO VỚI TIỀN MẶT', sub='Em tự tính: 457.500 chia 71.500', col=RED,
      say=("Em lấy bốn trăm năm mươi bảy nghìn năm trăm chia cho bảy mươi mốt nghìn năm trăm, ra sáu phẩy bốn lần. Cứ một đồng tiền mặt đang chờ mua, có hơn sáu đồng tiền vay đã nằm sẵn trong cổ phiếu.")),
 dict(k='cards', anh=TP, cap=('NỢ TĂNG', 'NGƯỜI MUA THƯA DẦN'), cols=CR, moc=True,
      cards=[('14,1%', 'Nợ ký quỹ tăng so cuối 2025', 'NỢ VẪN TĂNG'), ('63,6%', 'Giao dịch quý 3 giảm so cùng kỳ', 'NGƯỜI MUA THƯA'), ('12.380 tỷ', 'Giao dịch HoSE mỗi phiên T10', 'THẤP NHẤT TỪ ĐẦU 2025')],
      say=("Đáng lo hơn, nợ tăng khi người mua thưa đi. Từ đầu năm, dư nợ vay ký quỹ tăng mười bốn phẩy một phần trăm. Nhưng giá trị giao dịch bình quân quý ba chỉ khoảng mười bốn nghìn tám trăm tỷ mỗi phiên, giảm sáu mươi ba phẩy sáu phần trăm so với cùng kỳ. "
           "Sang tháng mười, sàn HoSE còn khoảng mười hai nghìn ba trăm tám mươi tỷ mỗi phiên, thấp nhất từ đầu năm 2025.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Tiền lãi đi đâu?', anh=BX, cap=('13.000 TỶ MỖI QUÝ', 'CHẢY VỀ ĐÂU?'), cols=CC, moc=True,
      cards=[('13.000 tỷ', 'Lãi người vay trả mỗi quý', 'VỀ CÔNG TY CHỨNG KHOÁN'), ('52.000 tỷ', 'Nếu giữ mức này cả năm', 'MỖI NĂM')],
      say=("Mười ba nghìn tỷ tiền lãi mỗi quý đi về công ty chứng khoán, bên cho vay. Giữ mức này cả năm là khoảng năm mươi hai nghìn tỷ đồng. "
           "Thị trường lên hay xuống, tiền lãi vẫn chạy. Người hưởng lợi chắc chắn nhất từ đòn bẩy là người cho vay.")),
 dict(k='giay', cap=('LÃI VAY 2,4 TRIỆU', 'MỖI THÁNG'), cols=CR, moc=True, giay=dict(tieu_de='TÀI KHOẢN CỦA ANH DŨNG', so='Số liệu em giả định để minh hoạ', dau='ĐÃ TÍNH', dieu=[
        ('Cổ phiếu đang giữ: 600 triệu.', '600 TRIỆU'),
        ('Trong đó vay ký quỹ: 240 triệu.', 'VAY 40%'),
        ('Lãi vay 12% mỗi năm: 2,4 triệu mỗi tháng.', '2,4 TRIỆU'),
        ('Danh mục phải tăng 4,8% mỗi năm chỉ để hoà lãi.', 'HOÀ LÃI 4,8%')]),
      say=("Anh Dũng mở tài khoản ra, số này em giả định để minh hoạ. Anh giữ sáu trăm triệu cổ phiếu, trong đó hai trăm bốn mươi triệu là tiền vay ký quỹ. Vốn thật của anh là ba trăm sáu mươi triệu. "
           "Với lãi vay em giả định mười hai phần trăm mỗi năm, anh trả khoảng hai phẩy bốn triệu đồng mỗi tháng. Cả danh mục phải tăng bốn phẩy tám phần trăm mỗi năm chỉ để hoà tiền lãi.")),
 dict(k='call', cap=('"CÓ NGƯỜI CẦM CỔ PHIẾU', 'RỒI RÚT TIỀN RA NGOÀI"'), cols=CC, moc=True, call=dict(ten='Anh Phong', phu='Làm phân tích đầu tư', mau=X_, loi=[
        'Có người vay rồi rút tiền khỏi thị trường', 'Giá giảm thì không còn tiền nộp thêm']),
      say=("Anh Dũng gọi cho anh Phong, người quen làm phân tích đầu tư. Anh Phong nói: báo cáo của SGI chỉ ra một rủi ro ít ai thấy. Có người cầm cổ phiếu để vay, rồi rút tiền ra ngoài thị trường dùng vào việc khác. "
           "Khi giá giảm, họ không còn tiền nộp thêm. Nhưng cũng phải nói công bằng. Một chuyên gia công ty chứng khoán cho rằng rủi ro này đáng chú ý, nhưng chưa đến mức báo động. Lý do là mỗi công ty chỉ được cho vay tối đa gấp hai lần vốn chủ sở hữu.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='noti', ch='Chương 3 – Giải chấp lan thế nào?', cap=('45 TRIỆU CỔ PHIẾU', 'BỊ BÁN GIẢI CHẤP'), cols=CR, moc=True, noti=dict(gio='10:30', ngay='Thứ Hai', items=[
        ('Tin tức', 'Doanh nghiệp', 'Hơn 45 triệu cổ phiếu của 7 cá nhân, tổ chức liên quan lãnh đạo bị bán giải chấp', R_),
        ('Tin tức', 'Doanh nghiệp', 'Dự kiến bán giải chấp 2,8 triệu cổ phiếu của người nhà chủ tịch từ 12/11', R_)]),
      say=("Mười giờ rưỡi, thêm hai tin theo báo Dân trí. Ở một doanh nghiệp niêm yết, bảy cá nhân và tổ chức liên quan ban lãnh đạo đã bị bán giải chấp hơn bốn mươi lăm triệu cổ phiếu. Chuyện đó diễn ra từ hai mươi bảy tháng mười đến mười tháng mười một. "
           "Ở doanh nghiệp khác, hai phẩy tám triệu cổ phiếu của người nhà chủ tịch dự kiến bị bán từ ngày mười hai tháng mười một. Người trong cuộc còn bị gọi ký quỹ, huống chi nhà đầu tư nhỏ.")),
 dict(k='cards', anh=TP, cap=('CỨ 3 CỔ PHIẾU', 'CÓ 1 ĐANG BỊ CẦM CỐ'), cols=CR, moc=True,
      cards=[('33%', 'Cổ phiếu tự do chuyển nhượng', 'ĐANG LÀM TÀI SẢN CẦM CỐ'), ('40%', 'Tỷ lệ cho vay bình quân', 'GIẢ ĐỊNH CỦA SGI')],
      say=("SGI còn ước tính thêm. Giả sử công ty chứng khoán cho vay bình quân bốn mươi phần trăm giá cổ phiếu. Khi đó, khoảng ba mươi ba phần trăm cổ phiếu tự do chuyển nhượng trên hai sàn HoSE và HNX đang nằm làm tài sản bảo đảm. "
           "Cứ ba cổ phiếu lưu hành tự do, có khoảng một cổ phiếu có thể bị bán ra nếu giá rơi quá ngưỡng.")),
 dict(k='checklist', anh=HN, cap=('GIẢI CHẤP DÂY CHUYỀN', 'DIỄN RA THẾ NÀO?'), cols=CR, moc=True,
      items=[('Giá giảm dưới ngưỡng an toàn', GOLD), ('Bị gọi nộp thêm tiền', GOLD), ('Không nộp kịp: bị bán giải chấp', RED), ('Giá giảm tiếp, kéo người khác', RED)],
      say=("Cơ chế dây chuyền diễn ra theo bốn bước. Giá giảm dưới ngưỡng an toàn. Công ty chứng khoán gọi nộp thêm tiền. Không nộp kịp thì cổ phiếu bị bán giải chấp, bán bằng mọi giá. "
           "Giá giảm tiếp, kéo tài khoản của người khác đang cầm cùng mã xuống dưới ngưỡng. Thanh khoản càng mỏng, vòng này càng quay nhanh.")),
 dict(k='cards', anh=TP, cap=('CHỈ SỐ XANH', 'MÃ NHỎ GIẢM SÀN CẢ TUẦN'), cols=CR, moc=True,
      cards=[('10 điểm', 'VN-Index tuần 9 đến 13/11', 'VẪN TĂNG NHẸ'), ('5 phiên', 'Một mã trên sàn HNX', 'GIẢM SÀN CẢ TUẦN'), ('67%', 'Mã đó từ đầu năm', '8.500 CÒN 2.800 ĐỒNG')],
      say=("Tuần trước là ví dụ. Theo Vietstock, VN-Index cả tuần vẫn tăng gần mười điểm. Nhưng một mã trên sàn HNX, có người liên quan lãnh đạo bị bán giải chấp, đã giảm sàn toàn bộ các phiên. "
           "Mã đó từ khoảng tám nghìn năm trăm đồng đầu năm còn hai nghìn tám trăm đồng. Nhìn chỉ số xanh, nhiều người không biết tài khoản bên cạnh đang cháy.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='call', ch='Chương 4 – Lần trước là năm 2022', cap=('"NĂM 2022 CHÚ BỊ', 'BÁN GIẢI CHẤP 2 LẦN"'), cols=CC, moc=True, call=dict(ten='Chú Bảy', phu='Đầu tư chứng khoán từ 2007', mau=V_, loi=[
        'Đầu năm 2022 ai cũng vay', 'Cuối năm VN-Index mất 32,8%']),
      say=("Trưa đó anh Dũng gọi cho chú Bảy, hàng xóm đầu tư chứng khoán từ năm 2007. Chú kể: đầu năm 2022 ai cũng vay. Rồi giá giảm, chú bị bán giải chấp hai lần, lần nào cũng đúng phiên thấp nhất. "
           "Lúc bị gọi ký quỹ, người vay không còn được chọn giá bán nữa.")),
 dict(k='giay', cap=('NĂM 2022 VÀ HÔM NAY', 'KHÁC NHAU Ở ĐÂU?'), cols=CC, moc=True, giay=dict(tieu_de='HAI LẦN NỢ KÝ QUỸ LÊN ĐỈNH', so='Theo BSC 30/12/2022 và SGI Capital 11/2026', dau='SO SÁNH', dieu=[
        ('Quý 1/2022: nợ ký quỹ lên đỉnh cũ.', 'ĐỈNH CŨ'),
        ('VN-Index 2022: 1.498,28 xuống 1.007,09 điểm.', 'MẤT 32,8%'),
        ('Cuối quý 3/2026: nợ gấp 2,5 lần đỉnh cũ.', 'GẤP 2,5 LẦN')]),
      say=("Quý một năm 2022, nợ ký quỹ lên đỉnh. Cả năm đó, VN-Index đi từ một nghìn bốn trăm chín mươi tám phẩy hai tám điểm xuống một nghìn không trăm linh bảy phẩy không chín điểm, mất ba mươi hai phẩy tám phần trăm. "
           "Còn hôm nay, theo SGI, dư nợ đã gấp hai phẩy năm lần đỉnh cũ.")),
 dict(k='checklist', anh=TP, cap=('GIỐNG 2, KHÁC 2', 'CHƯA CÓ NGHĨA LÀ SẼ SẬP'), cols=CC, moc=True,
      items=[('Giống: nợ vay lên đỉnh', RED), ('Giống: giao dịch teo lại', RED), ('Khác: trần vay 2 lần vốn chủ', GREEN), ('Khác: giá đã giảm khá lâu', GREEN)],
      say=("Có hai điểm giống và hai điểm khác. Giống ở chỗ nợ vay lên đỉnh và giao dịch teo lại. Khác ở chỗ có trần cho vay gấp hai lần vốn chủ, và theo SGI, nhiều cổ phiếu đã giảm khá lâu nên định giá hấp dẫn hơn. "
           "Nhưng SGI cũng cảnh báo: một tin xấu bất ngờ có thể kích hoạt làn bán giải chấp vượt sức mua của thị trường. Chưa xảy ra, không có nghĩa là không thể.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='bignum', ch='Chương 5 – Phép tính của anh Dũng', anh=TP, cap=('GIẢM 20%', 'MẤT 33,3% VỐN'), cols=CR, moc=True, value=33.3, fmt='{:,.1f}', unit='%', top='CỔ PHIẾU GIẢM 20%', sub='Tài khoản giả định: vay 240, vốn 360 triệu', col=RED,
      say=("Anh Dũng tự tính. Cổ phiếu giảm hai mươi phần trăm, sáu trăm triệu còn bốn trăm tám mươi triệu, trả nợ xong còn hai trăm bốn mươi triệu. "
           "Anh mất một trăm hai mươi triệu trên ba trăm sáu mươi triệu vốn thật, tức ba mươi ba phẩy ba phần trăm. Thị trường giảm hai mươi, anh mất ba mươi ba.")),
 dict(k='chat', cap=('"GIẢM 33% LÀ BỊ GỌI', 'KÝ QUỸ À ANH?"'), cols=CR, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='19:45', mau=G_, msgs=[
        ('me', 'Ngưỡng của công ty là 40%. Cổ phiếu giảm 33% là anh bị gọi'),
        ('Vợ', 'Mỗi tháng trả 2,4 triệu tiền lãi, giảm 20% thì mất 120 triệu?'),
        ('Vợ', 'Vậy nhà mình đang đặt cược bằng tiền ai?')]),
      say=("Tối đó anh kể với vợ. Em giả định ngưỡng cảnh báo là bốn mươi phần trăm, nghĩa là cổ phiếu giảm khoảng ba mươi ba phần trăm thì anh bị gọi nộp thêm tiền. "
           "Chị Lan, vợ anh, hỏi lại: vậy nhà mình đang đặt cược bằng tiền của ai?")),
 dict(k='cards', anh=NHA, cap=('TRẢ NỬA NỢ', 'NGƯỠNG GỌI XA GẤP ĐÔI'), cols=CC, moc=True,
      cards=[('1,2 triệu', 'Lãi mỗi tháng còn lại', 'NỢ CÒN 120 TRIỆU'), ('26,7%', 'Vốn mất nếu giảm 20%', 'THAY VÌ 33,3%'), ('58%', 'Giảm tới mức này mới bị gọi', 'THAY VÌ 33%')],
      say=("Có một con đường khác, không cần đoán đúng thị trường. Nếu anh Dũng bán bớt một trăm hai mươi triệu để trả nửa khoản vay, tiền lãi còn một phẩy hai triệu đồng mỗi tháng. "
           "Cổ phiếu giảm hai mươi phần trăm, anh mất hai mươi sáu phẩy bảy phần trăm vốn thay vì ba mươi ba phẩy ba. Và phải giảm tới khoảng năm mươi tám phần trăm mới chạm ngưỡng bị gọi ký quỹ, thay vì ba mươi ba.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='checklist', ch='Chương 6 – Phép thử của anh chị', anh=HN, cap=('PHÉP THỬ', 'GIẢM 20% THÌ MẤT BAO NHIÊU?'), cols=CC, moc=True,
      items=[('Không vay: mất 20% vốn', GREEN), ('Vay bằng nửa vốn: mất 30%', GOLD), ('Vay bằng vốn: mất 40%', RED), ('Trên 40%: sát ngưỡng gọi', RED)],
      say=("Em gợi ý một phép thử tự soi. Cổ phiếu giảm hai mươi phần trăm thì tài khoản mất bao nhiêu phần trăm vốn thật? Không vay, mất hai mươi. Vay bằng nửa số vốn, mất ba mươi. Vay bằng đúng số vốn, mất bốn mươi. "
           "Con số càng vượt bốn mươi, tài khoản càng sát vùng bị gọi ký quỹ. Đây là mốc tự soi, không phải lời khuyên mua bán.")),
 dict(k='checklist', anh=TP, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI CUỐI NĂM'), cols=CC, moc=True,
      items=[('Nợ ký quỹ quý 4 tăng hay giảm?', GOLD), ('Giao dịch có về trên 15.000 tỷ?', GOLD), ('Thêm tin bán giải chấp lãnh đạo?', RED)],
      say=("Ba điều đáng theo dõi tới cuối năm. Dư nợ vay ký quỹ quý bốn tăng tiếp hay bắt đầu giảm. Giá trị giao dịch có quay lại trên mười lăm nghìn tỷ mỗi phiên hay không. "
           "Và còn bao nhiêu thông báo bán giải chấp cổ phiếu của người liên quan lãnh đạo doanh nghiệp. Muốn xem mã đang nắm giữ lãi lỗ ra sao qua từng quý, anh chị có thể tra miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"ĐÒN BẨY KHÔNG XẤU', 'CHỈ LÀ ANH KHÔNG NGỦ ĐƯỢC"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:15', mau=G_, msgs=[
        ('me', 'Mai anh bán bớt, trả nửa khoản vay'),
        ('Vợ', 'Lãi còn 1,2 triệu mỗi tháng, em thấy nhẹ người'),
        ('me', 'Đòn bẩy không xấu, chỉ là anh không ngủ được')]),
      say=("Mười giờ tối, anh Dũng nhắn cho vợ: mai anh bán bớt, trả nửa khoản vay. Chị Lan trả lời: lãi còn một phẩy hai triệu mỗi tháng, em thấy nhẹ người. "
           "Anh gõ thêm một dòng: đòn bẩy không xấu, chỉ là anh không ngủ được.")),
 dict(k='end', cap=('GIẢM 20% THÌ TÀI KHOẢN', 'MẤT 20, 30 HAY 40%?'), cols=CC,
      say=("Còn anh chị, nếu cổ phiếu giảm hai mươi phần trăm, tài khoản của anh chị mất bao nhiêu phần trăm vốn thật: hai mươi, ba mươi hay trên bốn mươi phần trăm? Kể cho em và mọi người ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Margin Kỷ Lục 457.500 Tỷ: Mỗi Ngày 143 Tỷ Tiền Lãi – Ai Hưởng Lợi, Ai Đang Bị Bán Giải Chấp?'
MT = ("NÓNG: dư nợ vay ký quỹ (margin) lập kỷ lục 457.500 tỷ đồng cuối quý 3/2026, gấp 2,5 lần đỉnh quý 1/2022, trong khi tiền mặt nhà đầu tư chỉ còn 71.500 tỷ và giao dịch giảm hơn 60%. "
      "Cùng lúc, cổ phiếu của người liên quan lãnh đạo nhiều doanh nghiệp niêm yết liên tiếp bị bán giải chấp. Tiền lãi 13.000 tỷ mỗi quý đi đâu, giải chấp dây chuyền diễn ra thế nào, và phép thử cho chính tài khoản của anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• SGI Capital, báo cáo triển vọng tháng 11/2026 (dữ liệu FiinTrade), qua VietTimes 13/11/2026, CafeF 11/11/2026, Người Quan Sát 12/11/2026: dư nợ margin cuối Q3/2026 457.500 tỷ đồng, hơn 5,3% vốn hoá và 14,2% giá trị free-float; gấp 2,5 lần đỉnh Q1/2022; "
      "tiền mặt nhà đầu tư 71.500 tỷ (−15%); lãi nhà đầu tư trả khoảng 13.000 tỷ mỗi quý (khoảng 52.000 tỷ/năm nếu giữ mức này – Người Quan Sát); với tỷ lệ cho vay bình quân 40% giá, khoảng 1/3 free-float trên HoSE và HNX làm tài sản bảo đảm; "
      "một số người vay rút tiền khỏi thị trường; định giá hấp dẫn hơn nhưng cần giảm đòn bẩy; tin xấu bất ngờ có thể kích hoạt làn bán giải chấp vượt sức hấp thụ\n"
      "• VietTimes 13/11/2026: GTGD bình quân HoSE tháng 10 khoảng 12.380 tỷ/phiên, thấp nhất từ đầu 2025 (VDSC); chuyên gia ABS: công ty chứng khoán cho vay tối đa 2 lần vốn chủ sở hữu, rủi ro đáng chú ý nhưng chưa báo động\n"
      "• Báo Pháp luật Việt Nam (Doanh nhân) 11/2026: dư nợ tại 78 công ty chứng khoán tăng 14,1% (56.400 tỷ) so cuối 2025; GTGD bình quân Q3/2026 khoảng 14.800 tỷ/phiên, giảm 63,6% so Q3/2025\n"
      "• Dân trí 13/11/2026: 7 cá nhân, tổ chức liên quan ban lãnh đạo một doanh nghiệp bị bán giải chấp hơn 45,33 triệu cổ phiếu (27/10–10/11); 2,8 triệu cổ phiếu của người nhà chủ tịch một doanh nghiệp khác dự kiến bị bán giải chấp từ 12/11; một mã HNX còn 2.800 đồng so khoảng 8.500 đồng đầu năm\n"
      "• Vietstock 16/11/2026: tuần 9–13/11 VN-Index tăng gần 10 điểm; mã HNX nói trên giảm sàn toàn bộ các phiên\n"
      "• VN-Index 31/12/2021: 1.498,28 điểm; 30/12/2022: 1.007,09 điểm (BSC Daily Review 30/12/2022) → −32,8% (tự tính)\n"
      "• Tự tính: 13.000 tỷ ÷ 91 ngày ≈ 143 tỷ mỗi ngày; 457.500 ÷ 71.500 ≈ 6,4 lần. Tài khoản anh Dũng là giả định: cổ phiếu 600 triệu, vay 240 triệu, vốn 360 triệu, lãi 12%/năm → 2,4 triệu mỗi tháng (4,8% danh mục); "
      "giảm 20% → mất 120/360 = 33,3% vốn; ngưỡng gọi ký quỹ giả định 40% → chạm khi giảm khoảng 33%; trả nửa nợ (nợ 120 triệu) → lãi 1,2 triệu mỗi tháng, giảm 20% mất 26,7% vốn, chạm ngưỡng khi giảm khoảng 58%. "
      "Phép thử: mức mất vốn = 20% × (tổng cổ phiếu ÷ vốn thật)\n\n"
      "Margin – con dao hai lưỡi, khi nào bị gọi ký quỹ: https://chungkhoanhuynguyen.com/hoc/margin-con-dao-hai-luoi-giam-30-mat-60-von-khi-nao-bi-call.html\n"
      "Tra lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật anh Dũng, chị Lan, Hải, anh Phong, chú Bảy là hư cấu; số liệu thị trường là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-16', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['margin', 'dư nợ margin', 'vay ký quỹ', 'bán giải chấp', 'call margin', 'chứng khoán hôm nay', 'VN-Index', 'đòn bẩy chứng khoán', 'tin nóng tài chính', 'SGI Capital'],
    bia_hook=['MARGIN KỶ LỤC', '457.500 TỶ'], badge='NÓNG: BÁN GIẢI CHẤP',
    bia_anh='Ho Chi Minh City skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['NỢ 457.500 TỶ', 'TIỀN 71.500 TỶ'], badge_b='GẤP 2,5 LẦN NĂM 2022',
    bia_hook_c=['LÃI 143 TỶ', 'MỖI NGÀY???'], badge_c='AI ĐANG HƯỞNG LỢI?',
    reel_hook='MARGIN KỶ LỤC 457.500 TỶ|AI ĐANG BỊ GIẢI CHẤP???',
    fb_post=("Dư nợ margin lập kỷ lục 457.500 tỷ 😳\n\n👉 Người vay trả khoảng 13.000 tỷ tiền lãi mỗi quý\n👉 Tiền mặt chờ mua chỉ còn 71.500 tỷ\n"
             "👉 Cổ phiếu người liên quan lãnh đạo nhiều doanh nghiệp bị bán giải chấp\n\nNếu cổ phiếu giảm 20%, tài khoản anh chị mất bao nhiêu phần trăm vốn?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 16/11: margin kỷ lục 457.500 tỷ, bán giải chấp lan rộng (NV1B 16/11/2026).\n"
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
