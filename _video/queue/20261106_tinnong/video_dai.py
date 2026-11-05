# -*- coding: utf-8 -*-
# TIN NÓNG KÊNH CHÍNH – QL1 soạn 06/11/2026 00:30. Nguồn: CafeF 04/11/2026 (NHNN công bố hoán đổi USD/VND 182 ngày).
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)
S = {}
S['TN0611'] = [
 {'k': 'hook', 'ch': 'Mở đầu', 'moc': True, 'label': 'VN-Index – nến tuần',
  'cap': ('NHNN BƠM TIỀN', '182 NGÀY'), 'cols': (WHITE, GOLD),
  'chart': {'sym': 'VNINDEXW', 'tf': 'W', 'weeks': 52, 'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, 'Tuần 2/11/26: 1.741', 2.6]]},
  'anh': 'State Bank of Vietnam building',
  'say': 'Hôm nay, ngày sáu tháng mười một, Ngân hàng Nhà nước mở một đợt hoán đổi ngoại tệ có kỳ hạn một trăm tám mươi hai ngày, tức là khoảng sáu tháng. '
         'Các đợt trước trong năm nay chỉ kéo dài hai mươi mốt ngày, mười bốn ngày, rồi bảy ngày. Lần này kỳ hạn dài gấp hơn hai mươi sáu lần. '
         'Nếu dùng hết hạn mức hai tỷ đô la, hệ thống ngân hàng nhận thêm gần bốn mươi tám nghìn tám trăm tỷ đồng tiền đồng để dùng trong nửa năm. '
         'Vậy đây có phải là bơm tiền? Tiền này đi đâu, ngân hàng nào được dùng, và nhà đầu tư cổ phiếu nên theo dõi những mốc nào? '
         'Mình giải thích trong khoảng bảy phút, bằng số liệu công bố, không phải lời đồn.'},
 {'k': 'cards', 'ch': 'Chương 1 – Tin chính trong 30 giây', 'moc': True, 'label': 'Thông tin NHNN công bố, theo CafeF 04/11/2026',
  'cap': ('3 CON SỐ',), 'cols': (WHITE, GOLD),
  'cards': [('Kỳ hạn', '182 ngày', 'trước đây chỉ 7–21 ngày'), ('Quy mô tối đa', '2 tỷ USD', '≈ 48.800 tỷ đồng'), ('Ngày giá trị', '9/11/2026', 'thu hồi khi đáo hạn')],
  'anh': 'vietnam dong banknotes',
  'say': 'Ba con số cần nhớ. Thứ nhất, kỳ hạn một trăm tám mươi hai ngày. Thứ hai, quy mô tối đa hai tỷ đô la, tương đương gần bốn mươi tám nghìn tám trăm tỷ đồng nếu dùng hết. '
         'Thứ ba, ngày giá trị là chín tháng mười một, tức là tiền về hệ thống từ đầu tuần sau. Khi hợp đồng đáo hạn sau sáu tháng, lượng tiền này được thu về. '
         'Quy mô thật sự còn tùy kết quả đấu thầu, nên hai tỷ đô la là mức trần, không phải con số chắc chắn.'},
 {'k': 'checklist', 'ch': 'Chương 2 – Hoán đổi ngoại tệ là gì', 'moc': True, 'label': 'Cơ chế hoán đổi USD/VND, nói đơn giản',
  'cap': ('HOÁN ĐỔI', 'LÀ GÌ?'), 'cols': (WHITE, GOLD),
  'items': [('Ngân hàng bán USD cho NHNN, nhận VND', BLUE), ('Đồng thời cam kết mua lại số USD đó sau 182 ngày', BLUE), ('Giá mua giao ngay 24.399 đ/USD', GOLD), ('Giá bán kỳ hạn 24.704 đ/USD, chênh 305 đồng', GOLD)],
  'anh': 'currency exchange dollar dong',
  'say': 'Hoán đổi ngoại tệ giống như cầm đồ có hẹn chuộc. Ngân hàng thương mại đưa đô la cho Ngân hàng Nhà nước, nhận về tiền đồng. '
         'Cùng lúc, hai bên ký luôn hợp đồng để sáu tháng sau ngân hàng mua lại số đô la đó. Giá mua giao ngay là hai mươi bốn nghìn ba trăm chín mươi chín đồng một đô la, '
         'giá bán kỳ hạn là hai mươi bốn nghìn bảy trăm lẻ bốn đồng. Phần chênh ba trăm lẻ năm đồng chính là chi phí để ngân hàng được dùng tiền đồng trong sáu tháng. '
         'Nghĩa là tiền không cho không. Đây là vốn có kỳ hạn, có giá, và có ngày trả.'},
 {'k': 'bars', 'ch': 'Chương 3 – Vì sao kỳ hạn dài mới là điểm nóng', 'moc': True, 'label': 'Kỳ hạn các đợt hoán đổi năm 2026 (ngày)',
  'cap': ('DÀI GẤP', '26 LẦN'), 'cols': (WHITE, GOLD),
  'bars': [('Tháng 2', 21, BLUE, '21 ngày'), ('Tháng 6', 14, BLUE, '14 ngày'), ('Tháng 9', 7, BLUE, '7 ngày'), ('Tháng 11', 182, GOLD, '182 ngày')],
  'anh': 'calendar months planning',
  'say': 'Quy mô hai tỷ đô la không mới, các đợt trước cũng từ một đến hai tỷ. Điểm khác là thời gian. Tiền vay bảy ngày chỉ đủ để ngân hàng xoay vòng ngắn. '
         'Tiền sáu tháng thì ngân hàng có thể tính chuyện cân đối vốn cho cả cuối năm hai nghìn không trăm hai mươi sáu và đầu năm hai nghìn không trăm hai mươi bảy, '
         'đúng mùa nhu cầu tín dụng và rút tiền tăng cao. Bạn hình dung thế này: vay bạn bè một tuần thì chỉ đủ trả nợ gấp, vay sáu tháng mới đủ để lên kế hoạch.'},
 {'k': 'checklist', 'ch': 'Chương 4 – Ai được tham gia', 'moc': True, 'label': 'Điều kiện tham gia theo công bố',
  'cap': ('KHÔNG PHẢI', 'AI CŨNG ĐƯỢC'), 'cols': (WHITE, GOLD),
  'items': [('Có nợ vay nước ngoài trung, dài hạn hoặc trái phiếu quốc tế', BLUE), ('Thời hạn còn lại từ 12 tháng trở lên', BLUE), ('Tùy lượng USD sẵn có và nhu cầu vốn VND', GOLD), ('Quy mô thật phụ thuộc kết quả đấu thầu', RED)],
  'anh': 'bank meeting finance',
  'say': 'Không phải ngân hàng nào cũng tham gia được. Điều kiện là ngân hàng có khoản vay nước ngoài trung, dài hạn hoặc trái phiếu quốc tế, với thời hạn còn lại từ mười hai tháng trở lên. '
         'Ngoài ra còn phụ thuộc ngân hàng đó có sẵn đô la hay không, và có thật sự cần thêm tiền đồng hay không. '
         'Vì vậy, đừng vội nghĩ cả ngành ngân hàng hưởng lợi như nhau. Kết quả đấu thầu sẽ cho biết ai thật sự dùng nguồn này.'},
 {'k': 'cards', 'ch': 'Chương 5 – Bối cảnh: chuỗi động thái nới lỏng', 'moc': True, 'label': 'Bối cảnh theo bài báo',
  'cap': ('CHUỖI', 'NỚI LỎNG'), 'cols': (WHITE, GOLD),
  'cards': [('Trước đó', 'Giảm lãi suất', 'NHNN yêu cầu giảm lãi huy động, cho vay'), ('Trước đó', 'Nới giới hạn', 'một loạt điều chỉnh cho hệ thống'), ('Bây giờ', 'Vốn 182 ngày', 'thêm thanh khoản dài hơn')],
  'anh': 'interest rate decrease',
  'say': 'Động thái này không đứng một mình. Trước đó, Ngân hàng Nhà nước đã yêu cầu các tổ chức tín dụng giảm lãi suất huy động và lãi suất cho vay, '
         'đồng thời nới một loạt giới hạn đối với hệ thống. Ghép các mảnh lại, thông điệp khá rõ: cơ quan điều hành muốn tiền trong hệ thống dồi dào hơn và rẻ hơn, '
         'nhưng làm bằng công cụ có kỳ hạn để có thể thu về khi cần.'},
 {'k': 'checklist', 'ch': 'Chương 6 – Ý nghĩa với nhà đầu tư cổ phiếu', 'moc': True, 'label': 'Kênh tác động, không phải khuyến nghị',
  'cap': ('NHÀ ĐẦU TƯ', 'CẦN HIỂU'), 'cols': (WHITE, GOLD),
  'items': [('Thanh khoản dồi dào thường hỗ trợ lãi suất liên ngân hàng', GREEN), ('Áp lực huy động cuối năm của ngân hàng có thể dịu bớt', GREEN), ('Tiền vẫn phải trả lại sau 182 ngày', RED), ('Thị trường có thể đã phản ánh trước một phần tin', RED)],
  'anh': 'stock market trading screen',
  'say': 'Với nhà đầu tư cổ phiếu, có hai mặt cần nhìn. Mặt tích cực: tiền dồi dào thường giúp lãi suất liên ngân hàng bớt căng, ngân hàng bớt phải chạy đua huy động cuối năm, '
         'và môi trường lãi suất thấp nói chung có lợi cho định giá cổ phiếu. Mặt cần thận trọng: đây là vốn có kỳ hạn, sáu tháng sau phải trả lại. '
         'Và tin đã công bố từ ngày bốn tháng mười một, nên giá có thể đã phản ánh một phần. Đừng mua chỉ vì một dòng tít.'},
 {'k': 'checklist', 'ch': 'Chương 7 – Ba mốc cần theo dõi', 'moc': True, 'label': 'Lịch theo dõi',
  'cap': ('3 MỐC', 'THEO DÕI'), 'cols': (WHITE, GOLD),
  'items': [('6/11: kết quả đấu thầu, bao nhiêu ngân hàng, bao nhiêu USD', GOLD), ('9/11 trở đi: lãi suất liên ngân hàng có giảm không', BLUE), ('Tháng 5/2027: đáo hạn, NHNN thu tiền về', RED)],
  'anh': 'checklist calendar',
  'say': 'Mình gợi ý ba mốc. Một, kết quả đấu thầu hôm nay: bao nhiêu ngân hàng tham gia và dùng bao nhiêu trong hạn mức hai tỷ đô la. Con số thấp nghĩa là nhu cầu chưa lớn. '
         'Hai, từ chín tháng mười một, xem lãi suất liên ngân hàng có giảm hay không. Ba, khoảng tháng năm năm sau, khi hợp đồng đáo hạn và tiền được thu về. '
         'Mình sẽ cập nhật kết quả đấu thầu trên web chungkhoanhuynguyen.com ngay khi có.'},
 {'k': 'end', 'label': '', 'cap': ('TIN NÓNG', 'ĐỌC BẰNG SỐ'), 'cols': (WHITE, GOLD),
  'say': 'Thông tin trong video theo công bố của Ngân hàng Nhà nước được báo CafeF đăng ngày bốn tháng mười một năm hai nghìn không trăm hai mươi sáu. '
         'Video chia sẻ kiến thức, không phải khuyến nghị mua bán. Nếu bạn muốn biết cổ phiếu ngân hàng nào phù hợp với danh mục của mình, để lại bình luận hoặc vào chungkhoanhuynguyen.com để được tư vấn trực tiếp.'},
]
