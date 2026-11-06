# -*- coding: utf-8 -*-
# VIDEO DÀI – NV1 soạn 7/11/2026 (lô 20261107_0100: CH1911A, CH1911B, CH1911C, CH2011A, CH2011B, CH2011C, CH2111A, CH2111B, CH2111C). Nến tuần: px_tuan.json. Kênh chính 19–21/11; 1/3 quản trị rủi ro.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['CH1911A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'BID – Đọc BCTC 5 phút',
  'cap': ('LÃI +39,9%', 'GIÁ −37%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank building vietnam',
  'say': 'Một ngân hàng vừa báo lãi quý ba tăng ba mươi chín phẩy chín phần trăm, nhưng giá cổ phiếu lại đang ở gần đáy năm mươi hai tuần, thấp hơn đỉnh tháng '
         'hai khoảng ba mươi bảy phần trăm. Anh chị sẽ tin vào báo cáo lãi, hay tin vào bảng giá? Nhiều người nghĩ lãi tăng thì giá phải tăng. Thực tế, giá cổ '
         'phiếu phản ánh kỳ vọng về tương lai, còn báo cáo tài chính kể lại chuyện đã xảy ra. Video này em đọc báo cáo tài chính quý ba năm hai nghìn không '
         'trăm hai mươi sáu của BIDV, mã BID, theo năm bước: lợi nhuận, thu nhập lãi thuần, chi phí dự phòng, nợ xấu, và định giá. Cuối video là danh sách rủi '
         'ro cần theo dõi. Số liệu tính đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Biểu đồ phía sau là nến tuần thật của BID, chỉ để '
         'minh họa.',
  'chart': {'sym': 'BIDW', 'tf': 'W', 'weeks': 52, 'circles': [[11, 52.37, 'Đỉnh tuần 19/1/26: 52,37', 0.6], [51, 31.6, 'Đáy tuần 2/11/26: 31,60', 1.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'moc': True,
  'label': 'LNST công ty mẹ BID (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'financial charts',
  'say': 'Bước một, nhìn lợi nhuận tám quý liền nhau chứ không nhìn một quý. quý ba năm hai nghìn không trăm hai mươi sáu BIDV lãi sau thuế công ty mẹ khoảng '
         'tám nghìn ba trăm ba mươi mốt tỷ đồng, tăng ba mươi chín phẩy chín phần trăm so với cùng kỳ. Lũy kế chín tháng đạt khoảng hai mươi ba nghìn hai trăm '
         'bảy mươi tám tỷ, tăng hai mươi lăm phẩy năm phần trăm. Nhưng anh chị để ý cột quý bốn năm hai nghìn không trăm hai mươi lăm: lợi nhuận vọt lên '
         'khoảng mười một nghìn ba trăm năm mươi sáu tỷ, cao nhất chuỗi. Ngân hàng thường dồn chi phí và thu nhập vào quý cuối năm, nên so quý với quý liền '
         'trước dễ bị đánh lừa. So cùng kỳ năm trước mới công bằng. quý ba năm hai nghìn không trăm hai mươi lăm chỉ khoảng năm nghìn chín trăm năm mươi ba '
         'tỷ, nền so sánh khá thấp, đó là một phần lý do con số tăng ba mươi chín phẩy chín phần trăm trông rất đẹp.',
  'bars': [('Q4/24', 7810.1, (56, 189, 248), '7.810'),
           ('Q1/25', 5840.4, (56, 189, 248), '5.840'),
           ('Q2/25', 6755.0, (56, 189, 248), '6.755'),
           ('Q3/25', 5953.0, (56, 189, 248), '5.953'),
           ('Q4/25', 11355.9, (56, 189, 248), '11.356'),
           ('Q1/26', 6800.8, (56, 189, 248), '6.801'),
           ('Q2/26', 8146.3, (56, 189, 248), '8.146'),
           ('Q3/26', 8330.7, (34, 197, 94), '8.331')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần BID (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank lending',
  'say': 'Bước hai, xem mảng cốt lõi: thu nhập lãi thuần, tức là tiền lãi cho vay trừ tiền lãi trả cho người gửi. quý ba năm hai nghìn không trăm hai mươi sáu '
         'BIDV có khoảng mười bảy nghìn không trăm năm mươi sáu tỷ, tăng mười hai phẩy bốn phần trăm so với cùng kỳ. Đây là con số quan trọng nhất của một '
         'ngân hàng thương mại, vì nó đến từ hoạt động cho vay hằng ngày. Anh chị thấy độ vênh chưa? Lợi nhuận tăng ba mươi chín phẩy chín phần trăm, nhưng '
         'mảng cốt lõi chỉ tăng mười hai phẩy bốn phần trăm. Khi lợi nhuận tăng nhanh gấp ba lần mảng cốt lõi, câu hỏi tiếp theo luôn là: phần chênh lệch đến '
         'từ đâu? So với quý hai, thu nhập lãi thuần còn giảm nhẹ từ khoảng mười bảy nghìn tám trăm linh bốn tỷ xuống mười bảy nghìn không trăm năm mươi sáu '
         'tỷ.',
  'bars': [('Q4/24', 15638.7, (56, 189, 248), '15.639'),
           ('Q1/25', 13945.6, (56, 189, 248), '13.946'),
           ('Q2/25', 14991.7, (56, 189, 248), '14.992'),
           ('Q3/25', 15172.6, (56, 189, 248), '15.173'),
           ('Q4/25', 19185.2, (56, 189, 248), '19.185'),
           ('Q1/26', 15733.7, (56, 189, 248), '15.734'),
           ('Q2/26', 17804.2, (56, 189, 248), '17.804'),
           ('Q3/26', 17056.0, (34, 197, 94), '17.056')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Chi phí dự phòng',
  'moc': True,
  'label': 'BID Q3/2026 – phần chênh lệch đến từ đâu',
  'cap': ('DỰ PHÒNG', 'GIẢM 25%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk provision',
  'say': 'Bước ba, chi phí dự phòng rủi ro. Trong quý ba năm hai nghìn không trăm hai mươi sáu, chi phí dự phòng của BIDV giảm khoảng hai mươi lăm phẩy không '
         'phần trăm so với cùng kỳ. Dự phòng là khoản ngân hàng trích ra để chuẩn bị cho các khoản vay có thể không thu hồi được. Trích ít đi thì lợi nhuận kế '
         'toán tăng lên ngay, dù hoạt động kinh doanh không thay đổi nhiều. Vì vậy một phần lợi nhuận tăng của quý này đến từ việc trích lập ít hơn. Điều này '
         'không sai, cũng không xấu. Nhưng nó có nghĩa là chất lượng lợi nhuận thấp hơn so với trường hợp lợi nhuận tăng nhờ cho vay nhiều hơn. Nếu quý sau nợ '
         'xấu tăng và ngân hàng phải trích lập trở lại, lợi nhuận có thể đi lùi.',
  'cards': [('Lợi nhuận Q3', '+39,9%', 'so với cùng kỳ'), ('Thu nhập lãi thuần', '+12,4%', 'mảng cốt lõi'), ('Chi phí dự phòng', '−25,0%', 'trích ít hơn')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Nợ xấu',
  'moc': True,
  'label': 'BID – chất lượng tài sản',
  'cap': ('NỢ XẤU', '1,85%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank risk',
  'say': 'Bước bốn, nợ xấu. Tỷ lệ nợ xấu của BIDV cuối quý ba năm hai nghìn không trăm hai mươi sáu khoảng một phẩy tám năm phần trăm. Mức này không cao so '
         'với nhóm ngân hàng, nhưng anh chị cần đọc nó cùng xu hướng. Một tỷ lệ nợ xấu ổn định quanh một phẩy tám phần trăm thì khác hẳn một tỷ lệ đi từ một '
         'phẩy hai phần trăm lên một phẩy tám phần trăm trong hai quý. Con số thứ hai cần đọc là bộ đệm dự phòng, tức là quỹ dự phòng chia cho nợ xấu. Bộ đệm '
         'càng dày thì ngân hàng càng có khả năng giảm trích lập mà không lo. Khi chi phí dự phòng giảm hai mươi lăm phần trăm cùng lúc nợ xấu chưa giảm, bộ '
         'đệm sẽ mỏng đi. Đây là điểm em sẽ theo dõi đầu tiên khi BIDV công bố báo cáo quý bốn.',
  'cards': [('Nợ xấu cuối Q3', '1,85%', 'tỷ lệ trên dư nợ'), ('Cần đọc thêm', 'Xu hướng', '2–4 quý liền'), ('Bộ đệm', 'Dự phòng / nợ xấu', 'dày hay mỏng')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá',
  'moc': True,
  'label': 'BID – định giá ngày 6/11/2026',
  'cap': ('P/B 1,27', 'ROE 18,5%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation',
  'say': 'Bước năm, định giá. Theo dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, BID có P trên E khoảng bảy phẩy hai bốn '
         'lần, P trên B khoảng một phẩy hai bảy lần, ROE khoảng mười tám phẩy năm phần trăm, tỷ suất cổ tức khoảng hai phẩy năm bảy phần trăm, vốn hóa khoảng '
         'hai trăm năm mươi nghìn tám trăm bốn mươi tám tỷ đồng. Giá đóng cửa từ khoảng năm mươi phẩy tám chín nghìn đồng ngày hai tháng hai năm hai nghìn '
         'không trăm hai mươi sáu xuống khoảng ba mươi mốt phẩy chín năm nghìn đồng, giảm khoảng ba mươi bảy phần trăm. Với ngân hàng, P trên B phải đọc cùng '
         'ROE. Một ngân hàng có ROE mười tám phẩy năm phần trăm mà P trên B một phẩy hai bảy lần là mức định giá thấp hơn trước đây, nhưng thị trường đang trả '
         'giá thấp có lý do: lo ngại về chất lượng tài sản và việc lợi nhuận dựa một phần vào giảm dự phòng. P trên B thấp chỉ là điểm bắt đầu để đặt câu hỏi, '
         'không phải kết luận.',
  'cards': [('P/E', '7,24 lần', '6/11/2026'), ('P/B', '1,27 lần', 'ROE 18,5%'), ('Giá từ đỉnh', '−37%', '50,89 → 31,95')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'BID – bốn rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'checklist risk',
  'say': 'Đây là bốn rủi ro cần theo dõi với BID. Một, chi phí dự phòng: nếu quý bốn phải trích lập tăng trở lại, lợi nhuận có thể không giữ được tốc độ tăng. '
         'Hai, nợ xấu: theo dõi xu hướng hai đến bốn quý, không chỉ một con số. Ba, biên lãi: thu nhập lãi thuần đã giảm nhẹ so với quý hai, cần xem quý tới '
         'có hồi lại không. Bốn, rủi ro tỷ trọng: giá đã giảm ba mươi bảy phần trăm từ đỉnh, nên ai đang cầm cổ phiếu này với tỷ trọng lớn cần xem lại kế '
         'hoạch, mức chịu lỗ tối đa và thời gian nắm giữ của mình. Không có cổ phiếu ngân hàng nào là an toàn tuyệt đối, kể cả ngân hàng lớn.',
  'items': [('Chi phí dự phòng quý 4', (255, 196, 0)),
            ('Xu hướng nợ xấu 2–4 quý', (255, 196, 0)),
            ('Thu nhập lãi thuần có hồi lại', (34, 197, 94)),
            ('Tỷ trọng và mức chịu lỗ của mình', (239, 68, 68))]},
 {'k': 'checklist',
  'ch': 'Chương 7 – Năm bước đọc BCTC ngân hàng',
  'moc': True,
  'label': 'Năm bước đọc BCTC ngân hàng',
  'cap': ('NĂM BƯỚC', 'DÙNG LẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'notebook checklist',
  'say': 'Tóm lại năm bước anh chị có thể dùng cho mọi ngân hàng. Một, lợi nhuận tám quý, so cùng kỳ chứ không so quý liền trước. Hai, thu nhập lãi thuần, xem '
         'mảng cốt lõi tăng nhanh hay chậm hơn lợi nhuận. Ba, chi phí dự phòng, tách phần lợi nhuận đến từ trích lập ít hơn. Bốn, nợ xấu và bộ đệm dự phòng. '
         'Năm, định giá P trên B đọc cùng ROE. Với BID quý này, câu chuyện là lợi nhuận đẹp hơn mảng cốt lõi, còn giá thì đang phản ánh sự hoài nghi của thị '
         'trường.',
  'items': [('Lợi nhuận 8 quý, so cùng kỳ', (34, 197, 94)),
            ('Thu nhập lãi thuần', (34, 197, 94)),
            ('Chi phí dự phòng', (255, 196, 0)),
            ('Nợ xấu và bộ đệm', (255, 196, 0)),
            ('P/B đọc cùng ROE', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LÃI TĂNG', 'GIÁ GIẢM – VÌ SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem hết video. Theo anh chị, khi lợi nhuận một ngân hàng tăng gần bốn mươi phần trăm mà giá vẫn ở gần đáy năm mươi hai tuần, thị '
         'trường đang lo điều gì nhất?'}]

S['CH1911B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Quản trị vốn – Quy tắc 1%',
  'cap': ('THUA 10 LỆNH', 'CÒN 35% VỐN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk management trader',
  'say': 'Hai người cùng thua mười lệnh liên tiếp. Người thứ nhất còn khoảng chín mươi phần trăm vốn. Người thứ hai chỉ còn khoảng ba mươi lăm phần trăm. Họ '
         'không khác nhau ở khả năng chọn cổ phiếu, mà khác nhau ở một con số: mỗi lệnh chấp nhận mất bao nhiêu phần trăm tài khoản. Nhiều người nghĩ quản trị '
         'vốn là chuyện của dân chuyên nghiệp. Thực tế, đây là thứ quyết định anh chị còn ở lại thị trường sau một năm xấu hay không. Video này em làm rõ quy '
         'tắc một phần trăm: nó là gì, tính khối lượng mua thế nào, và vì sao toán học của thua lỗ lại khắc nghiệt hơn mình tưởng. Biểu đồ phía sau là nến '
         'tuần VN-Index, chỉ để minh họa.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Mười lệnh thua liên tiếp',
  'moc': True,
  'label': 'Vốn còn lại sau 10 lệnh thua liên tiếp (%)',
  'cap': ('MƯỜI LỆNH THUA', 'CÒN BAO NHIÊU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'losing streak chart',
  'say': 'Chương một, làm một phép thử đơn giản. Giả sử anh chị thua mười lệnh liên tiếp. Nếu mỗi lệnh chỉ mất một phần trăm tài khoản, sau mười lệnh anh chị '
         'còn khoảng chín mươi phẩy bốn phần trăm vốn. Nếu mỗi lệnh mất hai phần trăm, còn khoảng tám mươi mốt phẩy bảy phần trăm. Nếu mỗi lệnh mất năm phần '
         'trăm, còn khoảng năm mươi chín phẩy chín phần trăm. Và nếu mỗi lệnh mất mười phần trăm, chỉ còn khoảng ba mươi tư phẩy chín phần trăm. Mười lệnh '
         'thua liên tiếp nghe có vẻ hiếm, nhưng với người giao dịch thường xuyên, chuỗi năm đến mười lệnh thua xảy ra nhiều lần trong một năm, nhất là khi thị '
         'trường đi xuống như các nhịp giảm trên mười phần trăm của VN-Index những năm gần đây.',
  'bars': [('1%/lệnh', 90.4, (34, 197, 94), '90,4%'),
           ('2%/lệnh', 81.7, (34, 197, 94), '81,7%'),
           ('5%/lệnh', 59.9, (255, 196, 0), '59,9%'),
           ('10%/lệnh', 34.9, (239, 68, 68), '34,9%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Toán học của hồi vốn',
  'moc': True,
  'label': 'Cần lãi bao nhiêu % để hòa vốn',
  'cap': ('LỖ BAO NHIÊU', 'LÃI BAO NHIÊU MỚI HÒA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'math recovery',
  'say': 'Chương hai, toán học của việc hồi vốn. Mất mười phần trăm tài khoản, anh chị cần lãi khoảng mười một phẩy một phần trăm để hòa. Mất hai mươi phần '
         'trăm, cần lãi hai mươi lăm phần trăm. Mất ba mươi lăm phần trăm, cần lãi khoảng năm mươi ba phẩy tám phần trăm. Mất năm mươi phần trăm, cần lãi một '
         'trăm phần trăm, tức là phải nhân đôi tài khoản mới quay về điểm xuất phát. Đây là lý do người mất sáu mươi lăm phần trăm vốn sau mười lệnh thua gần '
         'như không thể tự hồi phục bằng giao dịch bình thường. Họ thường làm điều nguy hiểm hơn: tăng tỷ trọng hoặc dùng margin để gỡ nhanh. Quy tắc một phần '
         'trăm tồn tại để anh chị không bao giờ bước vào vùng toán học đó.',
  'bars': [('Lỗ 10%', 11.1, (34, 197, 94), '+11,1%'),
           ('Lỗ 20%', 25.0, (255, 196, 0), '+25%'),
           ('Lỗ 35%', 53.8, (255, 196, 0), '+53,8%'),
           ('Lỗ 50%', 100.0, (239, 68, 68), '+100%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Quy tắc 1% là gì',
  'moc': True,
  'label': 'Quy tắc 1% – định nghĩa đúng',
  'cap': ('1% LÀ GÌ', 'KHÔNG PHẢI MUA 1%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'calculator money',
  'say': 'Chương ba, hiểu đúng quy tắc một phần trăm. Đây là chỗ nhiều người hiểu sai. Quy tắc một phần trăm không có nghĩa là chỉ mua một phần trăm tài khoản '
         'cho mỗi cổ phiếu. Nó có nghĩa là: nếu lệnh này sai và giá chạm điểm cắt lỗ, số tiền anh chị mất tối đa bằng một phần trăm tổng tài khoản. Ví dụ tài '
         'khoản năm trăm triệu đồng, một phần trăm là năm triệu đồng. Đó là mức rủi ro cho một lệnh. Còn mua bao nhiêu cổ phiếu thì phụ thuộc vào khoảng cách '
         'từ giá mua đến giá cắt lỗ. Điểm cắt lỗ càng gần thì mua được nhiều hơn, điểm cắt lỗ càng xa thì phải mua ít đi.',
  'cards': [('Tài khoản', '500 triệu', 'ví dụ giả định'), ('Rủi ro 1 lệnh', '5 triệu', '1% tài khoản'), ('Khối lượng', 'Theo cắt lỗ', 'không theo cảm giác')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Tính khối lượng mua',
  'moc': True,
  'label': 'Công thức: khối lượng = rủi ro ÷ khoảng cắt lỗ',
  'cap': ('TÍNH KHỐI LƯỢNG', 'MUA BAO NHIÊU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'position sizing',
  'say': 'Chương bốn, tính khối lượng mua. Công thức là: khối lượng bằng số tiền rủi ro chia cho khoảng cách từ giá mua đến giá cắt lỗ. Ví dụ giả định, anh '
         'chị muốn mua một cổ phiếu giá hai mươi nghìn đồng, đặt điểm cắt lỗ ở mười tám nghìn đồng, tức là chấp nhận mất hai nghìn đồng mỗi cổ phiếu. Rủi ro '
         'cho phép là năm triệu đồng. Năm triệu chia cho hai nghìn bằng hai nghìn năm trăm cổ phiếu, tổng giá trị khoảng năm mươi triệu đồng, tức mười phần '
         'trăm tài khoản. Nếu điểm cắt lỗ ở mười chín nghìn đồng, khối lượng lên năm nghìn cổ phiếu, khoảng một trăm triệu đồng. Rủi ro vẫn đúng năm triệu, '
         'chỉ có quy mô vị thế thay đổi.',
  'cards': [('Giá mua / cắt lỗ', '20 / 18', 'mất 2 nghìn/cp'), ('Khối lượng', '2.500 cp', '≈ 50 triệu'), ('Cắt lỗ 19', '5.000 cp', '≈ 100 triệu')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Ba cái bẫy',
  'moc': True,
  'label': 'Ba cái bẫy khi áp dụng quy tắc 1%',
  'cap': ('BA CÁI BẪY', 'HAY GẶP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'trap warning',
  'say': 'Chương năm, ba cái bẫy hay gặp. Bẫy thứ nhất: đặt điểm cắt lỗ rồi dời xuống khi giá chạm. Lúc đó quy tắc một phần trăm biến thành ba phần trăm hay '
         'năm phần trăm mà anh chị không nhận ra. Bẫy thứ hai: cổ phiếu thanh khoản thấp hoặc giảm sàn nhiều phiên, anh chị không bán được ở giá cắt lỗ, nên '
         'mức lỗ thực tế lớn hơn kế hoạch. Với những mã này, nên dùng mức rủi ro thấp hơn một phần trăm. Bẫy thứ ba: mua năm mã cùng ngành, mỗi mã rủi ro một '
         'phần trăm, nhưng khi ngành đó giảm thì cả năm mã cùng chạm cắt lỗ. Rủi ro thật là năm phần trăm chứ không phải một phần trăm.',
  'items': [('Dời điểm cắt lỗ khi giá chạm', (239, 68, 68)),
            ('Mã thanh khoản thấp, giảm sàn', (239, 68, 68)),
            ('Nhiều mã cùng ngành cùng giảm', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Kế hoạch mỗi lệnh',
  'moc': True,
  'label': 'Bốn dòng viết trước mỗi lệnh',
  'cap': ('VIẾT TRƯỚC', 'KHI BẤM MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'trading plan notebook',
  'say': 'Chương sáu, biến quy tắc thành thói quen. Trước mỗi lệnh, anh chị viết bốn dòng. Một, giá mua dự kiến. Hai, giá cắt lỗ và lý do đặt ở đó. Ba, số '
         'tiền rủi ro bằng bao nhiêu phần trăm tài khoản. Bốn, khối lượng tính ra theo công thức. Mất khoảng một phút, nhưng nó buộc anh chị quyết định lúc '
         'còn tỉnh táo, trước khi cảm xúc của thị trường xen vào. Người có kế hoạch vẫn thua lệnh, nhưng họ thua nhỏ và còn vốn cho lần sau.',
  'items': [('Giá mua dự kiến', (34, 197, 94)),
            ('Giá cắt lỗ và lý do', (255, 196, 0)),
            ('Rủi ro = bao nhiêu % tài khoản', (255, 196, 0)),
            ('Khối lượng theo công thức', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('THUA NHỎ', 'ĐỂ CÒN Ở LẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Nếu nhìn lại mười lệnh gần nhất của mình, anh chị nghĩ mỗi lệnh đang chấp nhận rủi ro khoảng bao nhiêu phần trăm tài khoản?'}]

S['CH1911C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'MWG – Đọc BCTC 5 phút',
  'cap': ('LÃI +74,7%', 'GIÁ −20%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'retail store vietnam',
  'say': 'Thế Giới Di Động vừa báo lãi quý ba tăng bảy mươi tư phẩy bảy phần trăm, doanh thu tăng ba mươi hai phần trăm, biên lợi nhuận gộp cải thiện. Một báo '
         'cáo gần như không có điểm xấu. Vậy mà giá cổ phiếu vẫn thấp hơn đỉnh tháng hai khoảng hai mươi phần trăm. Khi mọi con số đều đẹp, câu hỏi khó nhất '
         'lại là: kỳ vọng đã nằm trong giá chưa? Video này em đọc báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của MWG theo năm bước: doanh '
         'thu, biên lợi nhuận gộp, lợi nhuận, chất lượng tăng trưởng, và định giá. Sau đó là phần rủi ro cần theo dõi, vì một báo cáo đẹp vẫn có rủi ro. Số '
         'liệu tính đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'MWGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[13, 91.73, 'Đỉnh tuần 2/2/26: 91,73', 0.6], [37, 60.73, 'Đáy tuần 27/7/26: 60,73', 1.6], [51, 73.7, 'Tuần 2/11/26: 73,70', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Doanh thu tám quý',
  'moc': True,
  'label': 'Doanh thu thuần MWG (tỷ đồng)',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'shopping mall',
  'say': 'Bước một, doanh thu. quý ba năm hai nghìn không trăm hai mươi sáu MWG đạt khoảng năm mươi hai nghìn sáu trăm mười bốn tỷ đồng doanh thu thuần, tăng '
         'ba mươi hai phẩy không phần trăm so với cùng kỳ. Anh chị nhìn chuỗi tám quý: doanh thu tăng gần như liên tục, từ khoảng ba mươi tư nghìn năm trăm '
         'bảy mươi tư tỷ ở quý bốn năm hai nghìn không trăm hai mươi tư lên hơn năm mươi hai nghìn tỷ. Với một nhà bán lẻ quy mô lớn, tăng ba mươi hai phần '
         'trăm là tốc độ rất cao. Điều cần hỏi là tăng trưởng đến từ đâu: mở thêm cửa hàng, bán được nhiều hơn trên mỗi cửa hàng, hay nhờ một nhóm hàng có chu '
         'kỳ thay máy. Mỗi nguồn có độ bền khác nhau.',
  'bars': [('Q4/24', 34573.9, (56, 189, 248), '34.574'),
           ('Q1/25', 36135.0, (56, 189, 248), '36.135'),
           ('Q2/25', 37620.0, (56, 189, 248), '37.620'),
           ('Q3/25', 39852.5, (56, 189, 248), '39.852'),
           ('Q4/25', 42320.7, (56, 189, 248), '42.321'),
           ('Q1/26', 46462.0, (56, 189, 248), '46.462'),
           ('Q2/26', 48751.3, (56, 189, 248), '48.751'),
           ('Q3/26', 52613.6, (34, 197, 94), '52.614')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Biên lợi nhuận gộp',
  'moc': True,
  'label': 'MWG – biên lợi nhuận gộp',
  'cap': ('BIÊN GỘP', '21,7%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit margin',
  'say': 'Bước hai, biên lợi nhuận gộp, tức là phần còn lại sau khi trừ giá vốn hàng bán. quý ba năm hai nghìn không trăm hai mươi sáu biên gộp của MWG khoảng '
         'hai mươi mốt phẩy bảy phần trăm, cùng kỳ năm trước khoảng mười tám phẩy tám phần trăm, cải thiện gần ba điểm phần trăm. Với nhà bán lẻ, ba điểm phần '
         'trăm biên gộp trên doanh thu năm mươi hai nghìn tỷ đồng là một khoản rất lớn, khoảng một nghìn năm trăm tỷ đồng lợi nhuận gộp tăng thêm chỉ nhờ '
         'biên. Doanh thu tăng cùng lúc biên cải thiện là dấu hiệu sức mạnh định giá và cơ cấu hàng tốt hơn. Ngược lại, nếu doanh thu tăng nhờ giảm giá thì '
         'biên sẽ co lại.',
  'cards': [('Biên gộp Q3/2026', '21,7%', 'cùng kỳ 18,8%'), ('Cải thiện', '≈ 2,9 điểm %', 'so với cùng kỳ'), ('Doanh thu', '+32,0%', '52.614 tỷ')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Lợi nhuận tám quý',
  'moc': True,
  'label': 'LNST công ty mẹ MWG (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit growth',
  'say': 'Bước ba, lợi nhuận. quý ba năm hai nghìn không trăm hai mươi sáu MWG lãi sau thuế công ty mẹ khoảng ba nghìn không trăm chín mươi tư tỷ đồng, tăng '
         'bảy mươi tư phẩy bảy phần trăm so với cùng kỳ. Lũy kế chín tháng khoảng chín nghìn một trăm mười một tỷ, tăng tám mươi ba phẩy năm phần trăm. Chuỗi '
         'tám quý đi lên đều từ khoảng tám trăm bốn mươi bảy tỷ ở quý bốn năm hai nghìn không trăm hai mươi tư. Tuy vậy, quý ba năm hai nghìn không trăm hai '
         'mươi sáu thấp hơn quý hai khoảng ba nghìn ba trăm linh ba tỷ. Một quý đi ngang hay giảm nhẹ không làm thay đổi xu hướng, nhưng nó nhắc anh chị rằng '
         'tăng trưởng bảy mươi đến tám mươi phần trăm không thể kéo dài mãi, vì nền so sánh của năm sau sẽ cao hơn nhiều.',
  'bars': [('Q4/24', 847.0, (56, 189, 248), '847'),
           ('Q1/25', 1545.9, (56, 189, 248), '1.546'),
           ('Q2/25', 1648.1, (56, 189, 248), '1.648'),
           ('Q3/25', 1770.9, (56, 189, 248), '1.771'),
           ('Q4/25', 2068.7, (56, 189, 248), '2.069'),
           ('Q1/26', 2714.4, (56, 189, 248), '2.714'),
           ('Q2/26', 3302.5, (56, 189, 248), '3.302'),
           ('Q3/26', 3094.3, (34, 197, 94), '3.094')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Chất lượng tăng trưởng',
  'moc': True,
  'label': 'MWG – lợi nhuận tăng nhanh hơn doanh thu',
  'cap': ('ĐÒN BẨY', 'HOẠT ĐỘNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'operating leverage',
  'say': 'Bước bốn, chất lượng tăng trưởng. Lợi nhuận tăng bảy mươi tư phẩy bảy phần trăm trong khi doanh thu tăng ba mươi hai phần trăm. Khoảng chênh này đến '
         'từ hai thứ: biên gộp tốt hơn, và chi phí cố định như tiền thuê, lương được chia trên doanh thu lớn hơn. Người ta gọi đó là đòn bẩy hoạt động. Đòn '
         'bẩy hoạt động có hai chiều. Khi doanh thu tăng, lợi nhuận tăng nhanh hơn. Khi doanh thu chững lại, lợi nhuận cũng giảm nhanh hơn doanh thu. Vì vậy '
         'chỉ số quan trọng nhất cần theo dõi ở các quý tới là tốc độ tăng doanh thu.',
  'cards': [('Doanh thu', '+32,0%', 'Q3/2026'), ('Lợi nhuận', '+74,7%', 'Q3/2026'), ('Hai chiều', 'Tăng nhanh – giảm nhanh', 'đòn bẩy hoạt động')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá',
  'moc': True,
  'label': 'MWG – định giá ngày 6/11/2026',
  'cap': ('P/E 9,9', 'ROE 29,5%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation retail',
  'say': 'Bước năm, định giá. Theo dữ liệu ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, MWG có P trên E khoảng chín phẩy chín lần, P trên B '
         'khoảng hai phẩy bốn hai lần, ROE khoảng hai mươi chín phẩy năm phần trăm, vốn hóa khoảng một trăm mười nghìn sáu trăm bảy mươi bảy tỷ đồng. Giá đóng '
         'cửa tuần gần nhất khoảng bảy mươi ba phẩy bảy nghìn đồng, thấp hơn mức đóng cửa cao nhất trong năm mươi hai tuần khoảng hai mươi phần trăm. P trên E '
         'dưới mười cho một doanh nghiệp tăng lợi nhuận hơn bảy mươi phần trăm là con số thấp. Nhưng P trên E tính trên lợi nhuận bốn quý gần nhất, vốn đang ở '
         'đỉnh. Nếu thị trường tin tốc độ tăng sẽ chậm lại mạnh trong năm tới, P trên E thấp chỉ phản ánh điều đó.',
  'cards': [('P/E', '9,9 lần', '4 quý gần nhất'), ('P/B', '2,42 lần', 'ROE 29,5%'), ('Giá tuần gần nhất', '73,7', 'thấp hơn đỉnh ≈ 20%')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'MWG – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk list',
  'say': 'Rủi ro cần theo dõi với MWG. Một, nền so sánh: năm sau phải so với các quý đã tăng hơn bảy mươi phần trăm, tốc độ tăng sẽ khó giữ. Hai, sức mua: bán '
         'lẻ điện máy và điện thoại phụ thuộc chu kỳ thay máy và thu nhập người dân. Ba, biên gộp: nếu cạnh tranh giá tăng, biên có thể quay về quanh mười '
         'chín phần trăm. Bốn, chính anh chị: báo cáo đẹp dễ làm người mua tăng tỷ trọng quá mức. Hãy giữ tỷ trọng theo kế hoạch, kể cả với doanh nghiệp mình '
         'thích nhất.',
  'items': [('Nền so sánh cao năm 2027', (255, 196, 0)),
            ('Sức mua và chu kỳ thay máy', (255, 196, 0)),
            ('Biên gộp có giữ được 21%', (255, 196, 0)),
            ('Tỷ trọng theo kế hoạch', (239, 68, 68))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('BÁO CÁO ĐẸP', 'ĐÃ VÀO GIÁ CHƯA?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Với một doanh nghiệp vừa có báo cáo gần như hoàn hảo, anh chị sẽ theo dõi chỉ số nào đầu tiên ở quý tới: doanh thu, biên gộp, '
         'hay lợi nhuận?'}]

S['CH2011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'CTG – Đọc BCTC 5 phút',
  'cap': ('BAO PHỦ 160%', 'GIÁ −22%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank headquarters',
  'say': 'VietinBank vừa báo lãi quý ba tăng hai mươi tám phẩy hai phần trăm, thu nhập lãi thuần tăng hai mươi bảy phần trăm, lãi dịch vụ tăng năm mươi sáu '
         'phẩy bảy phần trăm, và bộ đệm dự phòng phủ khoảng một trăm sáu mươi phần trăm nợ xấu. Đây là kiểu báo cáo mà mảng cốt lõi đi cùng lợi nhuận. Vậy vì '
         'sao giá vẫn thấp hơn đỉnh tháng một khoảng hai mươi hai phần trăm? Video này em đọc báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu '
         'của VietinBank, mã CTG, theo năm bước: lợi nhuận, thu nhập lãi thuần, lãi dịch vụ, nợ xấu cùng bộ đệm, và định giá. Em sẽ đặt CTG cạnh BID để anh '
         'chị thấy hai ngân hàng quốc doanh có cùng lợi nhuận tăng nhưng chất lượng tăng trưởng khác nhau. Số liệu tính đến ngày sáu tháng mười một năm hai '
         'nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'CTGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 42.84, 'Đỉnh tuần 12/1/26: 42,84', 0.6], [36, 28.4, 'Đáy tuần 20/7/26: 28,40', 1.6], [51, 31.85, 'Tuần 2/11/26: 31,85', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'moc': True,
  'label': 'LNST công ty mẹ CTG (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank profit chart',
  'say': 'Bước một, lợi nhuận. quý ba năm hai nghìn không trăm hai mươi sáu VietinBank lãi sau thuế công ty mẹ khoảng mười nghìn tám trăm ba mươi lăm tỷ đồng, '
         'tăng hai mươi tám phẩy hai phần trăm so với cùng kỳ. Lũy kế chín tháng khoảng ba mươi mốt nghìn bốn trăm chín mươi hai tỷ, tăng ba mươi ba phẩy tám '
         'phần trăm. Chuỗi tám quý cho thấy lợi nhuận dao động, có quý như quý một năm hai nghìn không trăm hai mươi lăm chỉ khoảng năm nghìn bốn trăm mười '
         'chín tỷ, nhưng mặt bằng chung đã nâng lên rõ. Ba quý năm hai nghìn không trăm hai mươi sáu đều trên tám nghìn chín trăm tỷ. Khi mặt bằng lợi nhuận '
         'được nâng lên nhiều quý liền, đó là tín hiệu đáng tin hơn một quý tăng đột biến.',
  'bars': [('Q4/24', 9798.3, (56, 189, 248), '9.798'),
           ('Q1/25', 5418.9, (56, 189, 248), '5.419'),
           ('Q2/25', 9669.9, (56, 189, 248), '9.670'),
           ('Q3/25', 8448.8, (56, 189, 248), '8.449'),
           ('Q4/25', 11066.9, (56, 189, 248), '11.067'),
           ('Q1/26', 8917.0, (56, 189, 248), '8.917'),
           ('Q2/26', 11740.1, (56, 189, 248), '11.740'),
           ('Q3/26', 10834.8, (34, 197, 94), '10.835')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần CTG (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'lending growth',
  'say': 'Bước hai, mảng cốt lõi. Thu nhập lãi thuần quý ba năm hai nghìn không trăm hai mươi sáu khoảng hai mươi mốt nghìn tám trăm mười sáu tỷ đồng, tăng '
         'hai mươi bảy phẩy không phần trăm so với cùng kỳ. Điểm khác biệt với nhiều ngân hàng khác là chuỗi này tăng gần như đều đặn qua tám quý, từ khoảng '
         'mười sáu nghìn ba trăm mười hai tỷ lên hai mươi mốt nghìn tám trăm mười sáu tỷ. Lợi nhuận tăng hai mươi tám phẩy hai phần trăm, mảng cốt lõi tăng '
         'hai mươi bảy phẩy không phần trăm, hai con số gần nhau. Nghĩa là lợi nhuận quý này chủ yếu đến từ cho vay nhiều hơn và hiệu quả hơn, chứ không phụ '
         'thuộc vào việc giảm trích lập. Anh chị so với BID: lợi nhuận tăng ba mươi chín phẩy chín phần trăm nhưng thu nhập lãi thuần chỉ tăng mười hai phẩy '
         'bốn phần trăm.',
  'bars': [('Q4/24', 16312.2, (56, 189, 248), '16.312'),
           ('Q1/25', 15475.2, (56, 189, 248), '15.475'),
           ('Q2/25', 15842.6, (56, 189, 248), '15.843'),
           ('Q3/25', 17175.7, (56, 189, 248), '17.176'),
           ('Q4/25', 17959.7, (56, 189, 248), '17.960'),
           ('Q1/26', 19385.2, (56, 189, 248), '19.385'),
           ('Q2/26', 20730.5, (56, 189, 248), '20.730'),
           ('Q3/26', 21815.8, (34, 197, 94), '21.816')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Lãi dịch vụ',
  'moc': True,
  'label': 'CTG – nguồn thu ngoài lãi',
  'cap': ('LÃI DỊCH VỤ', '+56,7%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'digital banking',
  'say': 'Bước ba, lãi dịch vụ, tức là phí thanh toán, phí thẻ, bảo lãnh và các dịch vụ khác. quý ba năm hai nghìn không trăm hai mươi sáu lãi dịch vụ của '
         'VietinBank khoảng hai nghìn bốn trăm tám mươi bảy tỷ đồng, tăng năm mươi sáu phẩy bảy phần trăm. Nguồn thu này quý giá vì không cần dùng nhiều vốn '
         'và ít rủi ro tín dụng. Ngân hàng có lãi dịch vụ tăng nhanh thường ít phụ thuộc vào chu kỳ lãi suất hơn. Tuy vậy, so với thu nhập lãi thuần hơn hai '
         'mươi mốt nghìn tỷ, lãi dịch vụ vẫn chỉ khoảng một phần chín. Động lực chính của CTG vẫn là cho vay.',
  'cards': [('Lãi dịch vụ Q3', '2.487 tỷ', '+56,7%'), ('Thu nhập lãi thuần', '21.816 tỷ', '+27,0%'), ('Tỷ lệ', '≈ 1/9', 'dịch vụ so với lãi')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Nợ xấu và bộ đệm',
  'moc': True,
  'label': 'CTG – chất lượng tài sản',
  'cap': ('NỢ XẤU 1,20%', 'BỘ ĐỆM 160%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'safety buffer',
  'say': 'Bước bốn, nợ xấu và bộ đệm. Cuối quý ba năm hai nghìn không trăm hai mươi sáu tỷ lệ nợ xấu của VietinBank khoảng một phẩy hai không phần trăm, và bộ '
         'đệm dự phòng phủ khoảng một trăm sáu mươi phần trăm nợ xấu. Nói đơn giản, cứ một trăm đồng nợ xấu thì ngân hàng đã để sẵn khoảng một trăm sáu mươi '
         'đồng dự phòng. Bộ đệm dày cho ngân hàng hai lợi thế. Một, chịu được cú sốc nợ xấu mà không làm lợi nhuận đi lùi mạnh. Hai, khi tình hình tốt lên, '
         'ngân hàng có dư địa giảm trích lập và hoàn nhập. So với một số ngân hàng có bộ đệm dưới năm mươi phần trăm, đây là khác biệt lớn về rủi ro.',
  'cards': [('Nợ xấu', '1,20%', 'cuối Q3/2026'), ('Bao phủ nợ xấu', '≈ 160%', 'bộ đệm dày'), ('Ý nghĩa', '100 → 160', 'đồng dự phòng/nợ xấu')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá',
  'moc': True,
  'label': 'CTG – định giá ngày 6/11/2026',
  'cap': ('P/E 5,77', 'ROE 22,5%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation bank',
  'say': 'Bước năm, định giá. Theo dữ liệu ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, CTG có P trên E khoảng năm phẩy bảy bảy lần, P trên '
         'B khoảng một phẩy một chín lần, ROE khoảng hai mươi hai phẩy năm phần trăm, tỷ suất cổ tức khoảng hai phẩy bốn một phần trăm, vốn hóa khoảng hai '
         'trăm bốn mươi lăm nghìn bốn trăm ba mươi lăm tỷ đồng. Giá đóng cửa từ khoảng bốn mươi phẩy tám bảy nghìn đồng ngày mười hai tháng một năm hai nghìn '
         'không trăm hai mươi sáu xuống khoảng hai mươi tám phẩy bảy năm nghìn đồng ngày hai mươi bảy tháng bảy năm hai nghìn không trăm hai mươi sáu, rồi hồi '
         'lên khoảng ba mươi mốt phẩy tám năm nghìn đồng. ROE hai mươi hai phẩy năm phần trăm mà P trên B chỉ một phẩy một chín lần là mức định giá thấp nếu '
         'ROE giữ được. Nhưng giá cổ phiếu ngân hàng quốc doanh còn chịu ảnh hưởng của việc tăng vốn, chia cổ tức bằng cổ phiếu và tâm lý chung của cả nhóm '
         'ngân hàng.',
  'cards': [('P/E', '5,77 lần', '6/11/2026'), ('P/B', '1,19 lần', 'ROE 22,5%'), ('Giá', '31,85', 'đỉnh 40,87 · đáy 28,75')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'CTG – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk checklist',
  'say': 'Rủi ro cần theo dõi với CTG. Một, tăng vốn: ngân hàng quốc doanh thường cần bổ sung vốn để tăng trưởng tín dụng, việc phát hành thêm làm pha loãng '
         'lợi nhuận trên mỗi cổ phiếu. Hai, tăng trưởng tín dụng nhanh: cho vay tăng mạnh hôm nay có thể là nợ xấu của hai, ba năm sau. Ba, rủi ro cả nhóm: '
         'khi dòng tiền rút khỏi ngân hàng, cổ phiếu tốt cũng giảm theo, như nhịp giảm từ tháng một đến tháng bảy năm nay. Bốn, tỷ trọng: nhiều nhà đầu tư cầm '
         'ba, bốn mã ngân hàng cùng lúc, đó vẫn là rủi ro tập trung vào một ngành.',
  'items': [('Tăng vốn, pha loãng EPS', (255, 196, 0)),
            ('Tín dụng tăng nhanh → nợ xấu sau', (255, 196, 0)),
            ('Cả nhóm ngân hàng cùng giảm', (239, 68, 68)),
            ('Nhiều mã cùng ngành = tập trung', (239, 68, 68))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('MẢNG CỐT LÕI', 'ĐI CÙNG LỢI NHUẬN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Giữa hai ngân hàng, một bên lợi nhuận tăng nhờ cho vay, một bên tăng nhờ giảm trích lập, anh chị sẽ tin con số tăng trưởng '
         'của bên nào hơn, và vì sao?'}]

S['CH2011B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Quản trị rủi ro – Rủi ro tập trung',
  'cap': ('CỔ PHIẾU TỐT', 'VẪN −57%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'portfolio concentration',
  'say': 'Một cổ phiếu công nghệ hàng đầu từng giảm khoảng năm mươi bảy phần trăm từ đỉnh tháng một năm hai nghìn không trăm hai mươi lăm. Một cổ phiếu khí '
         'lớn nhất thị trường giảm năm mươi phần trăm chỉ trong bốn tháng năm nay. Đó không phải cổ phiếu yếu, mà là những cái tên nhiều người coi là an toàn '
         'nhất. Nếu một trong hai mã đó chiếm một nửa tài khoản của anh chị, chuyện gì sẽ xảy ra? Video này nói về rủi ro tập trung: vì sao dồn tiền vào một '
         'mã, kể cả mã tốt, là rủi ro lớn nhất của nhà đầu tư cá nhân, và cách chia tỷ trọng để một cú sai không làm hỏng cả năm. Số liệu giá đóng cửa từ '
         'tháng mười năm hai nghìn không trăm hai mươi ba đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Biểu đồ phía sau là nến tuần FPT, '
         'chỉ để minh họa.',
  'chart': {'sym': 'FPTW', 'tf': 'W', 'weeks': 52, 'circles': [[11, 97.48, 'Đỉnh tuần 19/1/26: 97,48', 0.6], [51, 49.55, 'Đáy tuần 2/11/26: 49,55', 1.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Cổ phiếu lớn cũng giảm sâu',
  'moc': True,
  'label': 'Mức giảm sâu nhất từ đỉnh (giá đóng cửa, %)',
  'cap': ('CỔ PHIẾU LỚN', 'GIẢM SÂU THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'stock drop',
  'say': 'Chương một, những cổ phiếu lớn cũng giảm sâu. Tính theo giá đóng cửa từ tháng mười năm hai nghìn không trăm hai mươi ba đến ngày sáu tháng mười một '
         'năm hai nghìn không trăm hai mươi sáu: FPT có lúc thấp hơn đỉnh khoảng năm mươi bảy phẩy năm phần trăm. GAS giảm khoảng năm mươi phần trăm từ ngày '
         'bốn tháng ba năm hai nghìn không trăm hai mươi sáu đến ngày hai mươi hai tháng bảy năm hai nghìn không trăm hai mươi sáu. VHM giảm khoảng bốn mươi '
         'phẩy chín phần trăm chỉ trong hai tháng đầu năm hai nghìn không trăm hai mươi sáu. MSN giảm khoảng ba mươi tám phần trăm, BID khoảng ba mươi bảy '
         'phẩy bảy phần trăm, MWG khoảng ba mươi ba phẩy chín phần trăm. Trong cùng thời gian, VN-Index giảm sâu nhất khoảng mười tám phẩy một phần trăm. Anh '
         'chị thấy khoảng cách chưa? Một chỉ số gồm nhiều cổ phiếu giảm nhẹ hơn nhiều so với từng cổ phiếu riêng lẻ, kể cả cổ phiếu tốt.',
  'bars': [('FPT', 57.5, (239, 68, 68), '−57,5%'),
           ('GAS', 50.0, (239, 68, 68), '−50,0%'),
           ('VHM', 40.9, (239, 68, 68), '−40,9%'),
           ('MSN', 38.0, (255, 196, 0), '−38,0%'),
           ('BID', 37.7, (255, 196, 0), '−37,7%'),
           ('MWG', 33.9, (255, 196, 0), '−33,9%'),
           ('VN-Index', 18.1, (56, 189, 248), '−18,1%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Một mã chiếm 50% tài khoản',
  'moc': True,
  'label': 'Mô phỏng: tài khoản 500 triệu, một mã giảm 50%',
  'cap': ('MỘT MÃ 50%', 'MẤT BAO NHIÊU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'portfolio pie chart',
  'say': 'Chương hai, làm phép tính với tài khoản giả định năm trăm triệu đồng. Nếu một mã chiếm năm mươi phần trăm tài khoản, tức hai trăm năm mươi triệu, và '
         'mã đó giảm năm mươi phần trăm như GAS năm nay, anh chị mất một trăm hai mươi lăm triệu, tức hai mươi lăm phần trăm tài khoản. Muốn hòa vốn, phần còn '
         'lại phải lãi khoảng ba mươi ba phần trăm. Nếu mã đó chỉ chiếm mười phần trăm tài khoản, cùng cú giảm năm mươi phần trăm chỉ làm mất hai mươi lăm '
         'triệu, tức năm phần trăm tài khoản. Một năm bình thường có thể bù lại được. Cùng một cổ phiếu, cùng một cú giảm, nhưng kết quả cho tài khoản khác '
         'nhau năm lần, chỉ vì tỷ trọng.',
  'cards': [('Tỷ trọng 50%', '−25% tài khoản', 'mất 125 triệu'),
            ('Tỷ trọng 10%', '−5% tài khoản', 'mất 25 triệu'),
            ('Cùng cú giảm', '−50%', 'khác nhau 5 lần')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Vì sao người ta vẫn dồn tiền',
  'moc': True,
  'label': 'Ba lý do dẫn đến tập trung',
  'cap': ('VÌ SAO', 'VẪN DỒN TIỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'overconfidence',
  'say': 'Chương ba, vì sao nhà đầu tư vẫn dồn tiền dù biết rủi ro. Lý do thứ nhất là quá tự tin: càng nghiên cứu kỹ một doanh nghiệp, mình càng tin chắc nó '
         'không thể giảm sâu. Lý do thứ hai là mua thêm khi giá giảm, gọi là trung bình giá xuống, khiến tỷ trọng phình lên đúng lúc mã đó yếu nhất. Lý do thứ '
         'ba là để mã tăng mạnh chạy mà không cân bằng lại, đến lúc một mã chiếm sáu mươi hay bảy mươi phần trăm tài khoản mà không ai quyết định điều đó. Cả '
         'ba đều là quyết định trôi dạt, không phải quyết định có kế hoạch.',
  'cards': [('Quá tự tin', '"mã này không thể giảm sâu"', ''),
            ('Trung bình giá xuống', 'tỷ trọng phình khi yếu', ''),
            ('Không cân bằng lại', 'mã tăng chiếm 60–70%', '')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Giới hạn tỷ trọng',
  'moc': True,
  'label': 'Bốn giới hạn tham khảo cho danh mục cá nhân',
  'cap': ('GIỚI HẠN', 'TỶ TRỌNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'portfolio limits',
  'say': 'Chương bốn, đặt giới hạn trước khi cần đến. Đây là khung tham khảo, anh chị điều chỉnh theo khẩu vị của mình. Một, mỗi cổ phiếu không quá mười lăm '
         'đến hai mươi phần trăm tài khoản. Hai, mỗi ngành không quá ba mươi đến ba mươi lăm phần trăm, vì ba mã ngân hàng vẫn là một ngành. Ba, mã thanh '
         'khoản thấp không quá năm đến mười phần trăm. Bốn, khi một mã vượt giới hạn do tăng giá, chốt bớt phần vượt để đưa về mức cũ. Quan trọng nhất là viết '
         'các giới hạn này ra giấy khi thị trường còn bình thường, để không phải quyết định giữa lúc hoảng loạn.',
  'items': [('Mỗi mã ≤ 15–20% tài khoản', (34, 197, 94)),
            ('Mỗi ngành ≤ 30–35%', (34, 197, 94)),
            ('Mã thanh khoản thấp ≤ 5–10%', (255, 196, 0)),
            ('Vượt giới hạn → cân bằng lại', (255, 196, 0))]},
 {'k': 'bars',
  'ch': 'Chương 5 – Tập trung và đa dạng hóa',
  'moc': True,
  'label': 'Mức giảm sâu nhất: mã đơn lẻ và chỉ số (%)',
  'cap': ('ĐA DẠNG HÓA', 'GIẢM CÚ SỐC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'diversification',
  'say': 'Chương năm, nhìn lại bằng số. Mức giảm sâu nhất trung bình của sáu cổ phiếu lớn em nêu ở trên khoảng bốn mươi ba phần trăm. VN-Index, đại diện cho '
         'một danh mục rất đa dạng, giảm sâu nhất khoảng mười tám phẩy một phần trăm. Đa dạng hóa không làm anh chị giàu nhanh hơn, và cũng không làm danh mục '
         'không bao giờ giảm. Nó chỉ làm một việc: đảm bảo không có một cú sai duy nhất nào đủ lớn để đẩy anh chị ra khỏi thị trường. Với nhà đầu tư cá nhân, '
         'còn ở lại thị trường là điều kiện đầu tiên để lãi kép phát huy tác dụng.',
  'bars': [('TB 6 mã lớn', 43.0, (239, 68, 68), '−43%'), ('VN-Index', 18.1, (56, 189, 248), '−18,1%')]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('MÃ TỐT NHẤT', 'CŨNG CÓ LÚC −50%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Nhìn vào tài khoản của mình hôm nay, mã lớn nhất đang chiếm bao nhiêu phần trăm, và nếu mã đó giảm năm mươi phần trăm, anh '
         'chị có ổn không?'}]

S['CH2011C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VNM – Đọc BCTC 5 phút',
  'cap': ('CỔ TỨC 8,18%', 'MÀ GIÁ ĐI NGANG?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'dairy milk factory',
  'say': 'Vinamilk đang có tỷ suất cổ tức khoảng tám phẩy một tám phần trăm theo giá hiện tại, ROE khoảng ba mươi mốt phần trăm, lợi nhuận chín tháng tăng ba '
         'mươi phẩy ba phần trăm. Ba con số đều đẹp. Nhưng giá cổ phiếu sau ba năm gần như đứng yên, chỉ cao hơn tháng mười năm hai nghìn không trăm hai mươi '
         'ba khoảng một phẩy bốn phần trăm. Một doanh nghiệp tốt có phải là một khoản đầu tư tốt không? Video này em đọc báo cáo tài chính quý ba năm hai '
         'nghìn không trăm hai mươi sáu của VNM theo năm bước: doanh thu, lợi nhuận, biên và chất lượng lợi nhuận, cổ tức, và định giá. Phần cuối là rủi ro '
         'cần theo dõi. Số liệu tính đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'VNMW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[11, 73.11, 'Đỉnh tuần 19/1/26: 73,11', 0.6], [0, 54.52, 'Đáy tuần 3/11/25: 54,52', 1.6], [51, 57.8, 'Tuần 2/11/26: 57,80', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Doanh thu tám quý',
  'moc': True,
  'label': 'Doanh thu thuần VNM (tỷ đồng)',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'supermarket dairy',
  'say': 'Bước một, doanh thu. quý ba năm hai nghìn không trăm hai mươi sáu Vinamilk đạt khoảng mười tám nghìn bốn trăm sáu mươi lăm tỷ đồng doanh thu thuần, '
         'tăng tám phẩy chín phần trăm so với cùng kỳ. Chuỗi tám quý dao động trong khoảng mười hai nghìn chín trăm đến mười tám nghìn tám trăm tỷ, không có '
         'bước nhảy lớn. Đây là đặc trưng của ngành hàng tiêu dùng thiết yếu: người ta vẫn uống sữa khi kinh tế tốt hay xấu, nên doanh thu ổn định. Nhưng '
         'chính sự ổn định đó cũng có nghĩa là khó có những năm tăng trưởng đột biến như bán lẻ hay thép.',
  'bars': [('Q4/24', 15477.1, (56, 189, 248), '15.477'),
           ('Q1/25', 12934.5, (56, 189, 248), '12.934'),
           ('Q2/25', 16724.6, (56, 189, 248), '16.725'),
           ('Q3/25', 16953.2, (56, 189, 248), '16.953'),
           ('Q4/25', 17033.6, (56, 189, 248), '17.034'),
           ('Q1/26', 16148.7, (56, 189, 248), '16.149'),
           ('Q2/26', 18847.3, (56, 189, 248), '18.847'),
           ('Q3/26', 18465.2, (34, 197, 94), '18.465')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'moc': True,
  'label': 'LNST công ty mẹ VNM (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit chart',
  'say': 'Bước hai, lợi nhuận. quý ba năm hai nghìn không trăm hai mươi sáu VNM lãi sau thuế công ty mẹ khoảng hai nghìn chín trăm sáu mươi tư tỷ đồng, tăng '
         'mười bảy phẩy ba phần trăm so với cùng kỳ. Lũy kế chín tháng khoảng tám nghìn năm trăm sáu mươi tỷ, tăng ba mươi phẩy ba phần trăm. Lợi nhuận tăng '
         'nhanh hơn doanh thu khá nhiều: doanh thu quý tăng tám phẩy chín phần trăm nhưng lợi nhuận tăng mười bảy phẩy ba phần trăm. Khoảng chênh thường đến '
         'từ giá nguyên liệu như sữa bột nhập khẩu và đường, cùng với kiểm soát chi phí bán hàng. quý một năm hai nghìn không trăm hai mươi lăm là quý thấp '
         'nhất chuỗi, khoảng một nghìn năm trăm sáu mươi chín tỷ, nên mức tăng chín tháng ba mươi phẩy ba phần trăm có một phần nhờ nền so sánh thấp.',
  'bars': [('Q4/24', 2123.6, (56, 189, 248), '2.124'),
           ('Q1/25', 1568.5, (56, 189, 248), '1.568'),
           ('Q2/25', 2474.6, (56, 189, 248), '2.475'),
           ('Q3/25', 2526.8, (56, 189, 248), '2.527'),
           ('Q4/25', 2840.4, (56, 189, 248), '2.840'),
           ('Q1/26', 2428.7, (56, 189, 248), '2.429'),
           ('Q2/26', 3167.0, (56, 189, 248), '3.167'),
           ('Q3/26', 2964.2, (34, 197, 94), '2.964')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Chất lượng lợi nhuận',
  'moc': True,
  'label': 'VNM – lợi nhuận tăng nhanh hơn doanh thu',
  'cap': ('LỢI NHUẬN', 'NHỜ BIÊN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'quality check',
  'say': 'Bước ba, chất lượng lợi nhuận. Khi lợi nhuận tăng nhờ biên chứ không nhờ sản lượng, anh chị cần hỏi: biên tốt lên vì doanh nghiệp làm tốt hơn, hay '
         'vì giá nguyên liệu đang thuận lợi? Nếu vì nguyên liệu rẻ, biên có thể quay đầu khi giá sữa bột thế giới tăng lại. Với VNM, doanh thu tăng một chữ số '
         'qua nhiều quý là tín hiệu thị trường trong nước đã khá bão hòa. Động lực dài hạn phải đến từ xuất khẩu, sản phẩm cao cấp, hoặc thị phần. Đây là câu '
         'hỏi quan trọng hơn con số lợi nhuận một quý.',
  'cards': [('Doanh thu Q3', '+8,9%', 'sản lượng ổn định'), ('Lợi nhuận Q3', '+17,3%', 'nhờ biên'), ('Câu hỏi', 'Biên có bền?', 'giá nguyên liệu')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Cổ tức',
  'moc': True,
  'label': 'VNM – cổ tức và ROE',
  'cap': ('CỔ TỨC 8,18%', 'ROE 31,1%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'dividend income',
  'say': 'Bước bốn, cổ tức. Theo dữ liệu ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, tỷ suất cổ tức của VNM khoảng tám phẩy một tám phần '
         'trăm so với giá hiện tại, cao hơn lãi suất tiết kiệm mười hai tháng phổ biến. ROE khoảng ba mươi mốt phẩy một phần trăm, rất cao. Doanh nghiệp có '
         'ROE cao nhưng tăng trưởng chậm thường chọn trả phần lớn lợi nhuận cho cổ đông, vì giữ lại cũng không có chỗ đầu tư đủ hiệu quả. Đó là lý do VNM '
         'giống một cổ phiếu thu nhập hơn là cổ phiếu tăng trưởng. Anh chị cần nhớ: tỷ suất cổ tức tính trên giá hiện tại và mức chi trả năm trước, không đảm '
         'bảo cho năm sau.',
  'cards': [('Tỷ suất cổ tức', '8,18%', 'theo giá 6/11/2026'), ('ROE', '31,1%', 'hiệu quả vốn cao'), ('Tính chất', 'Cổ phiếu thu nhập', 'tăng trưởng chậm')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá',
  'moc': True,
  'label': 'VNM – định giá ngày 6/11/2026',
  'cap': ('P/E 10,54', '3 NĂM +1,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation consumer',
  'say': 'Bước năm, định giá. VNM có P trên E khoảng mười phẩy năm bốn lần, P trên B khoảng ba phẩy bốn chín lần, vốn hóa khoảng một trăm hai mươi nghìn một '
         'trăm bảy mươi hai tỷ đồng. Giá đóng cửa tuần gần nhất khoảng năm mươi bảy phẩy tám nghìn đồng, chỉ cao hơn tháng mười năm hai nghìn không trăm hai '
         'mươi ba khoảng một phẩy bốn phần trăm. Nghĩa là trong ba năm, người nắm giữ chủ yếu nhận lợi nhuận từ cổ tức chứ không từ chênh lệch giá. Với cổ '
         'phiếu thu nhập, anh chị nên đo kết quả bằng tổng lợi nhuận gồm cả cổ tức, và so với lãi tiết kiệm, thay vì so với các mã tăng mạnh.',
  'cards': [('P/E', '10,54 lần', '6/11/2026'), ('P/B', '3,49 lần', 'ROE 31,1%'), ('Giá 3 năm', '+1,4%', '10/2023 → 11/2026')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'VNM – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk list',
  'say': 'Rủi ro cần theo dõi với VNM. Một, giá nguyên liệu: sữa bột và đường tăng sẽ bóp biên gộp. Hai, tăng trưởng doanh thu: nếu doanh thu đi ngang nhiều '
         'năm, P trên E khó mở rộng. Ba, chi trả cổ tức: mức tám phần trăm hiện nay phụ thuộc vào việc doanh nghiệp tiếp tục trả gần hết lợi nhuận. Bốn, chi '
         'phí cơ hội: giữ một mã tăng giá chậm trong ba năm nghĩa là bỏ lỡ những nơi khác. Điều này không sai nếu anh chị chủ động chọn thu nhập ổn định, '
         'nhưng cần là lựa chọn có ý thức.',
  'items': [('Giá sữa bột, đường', (255, 196, 0)),
            ('Doanh thu đi ngang nhiều năm', (255, 196, 0)),
            ('Mức chi trả cổ tức', (255, 196, 0)),
            ('Chi phí cơ hội', (239, 68, 68))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('DOANH NGHIỆP TỐT', 'CÓ PHẢI ĐẦU TƯ TỐT?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Với một cổ phiếu cổ tức cao nhưng giá đi ngang ba năm, anh chị chấm nó là khoản đầu tư thành công hay chưa thành công, và anh '
         'chị đo bằng thước đo nào?'}]

S['CH2111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'MSB – Đọc BCTC 5 phút',
  'cap': ('LÃI +29,4%', 'ĐỆM CHỈ 47%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank vietnam city',
  'say': 'MSB vừa báo lãi quý ba tăng hai mươi chín phẩy bốn phần trăm, giá cổ phiếu đang ở vùng cao nhất năm mươi hai tuần. Nhìn bề ngoài, mọi thứ đều thuận. '
         'Nhưng trong cùng báo cáo, nợ xấu tăng lên hai phẩy bảy không phần trăm, và bộ đệm dự phòng chỉ phủ khoảng bốn mươi bảy phần trăm nợ xấu. Khi giá '
         'đang ở đỉnh mà bộ đệm mỏng, anh chị nên đọc điều gì trước? Video này em đọc báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của Ngân '
         'hàng Hàng Hải, mã MSB, theo năm bước: lợi nhuận, thu nhập lãi thuần, lãi dịch vụ, nợ xấu cùng bộ đệm, và định giá. Số liệu tính đến ngày sáu tháng '
         'mười một năm hai nghìn không trăm hai mươi sáu. Biểu đồ phía sau là nến tuần MSB, chỉ để minh họa.',
  'chart': {'sym': 'MSBW', 'tf': 'W', 'weeks': 52, 'circles': [[51, 16.6, 'Đỉnh tuần 2/11/26: 16,60', 0.6], [17, 9.0, 'Đáy tuần 9/3/26: 9,00', 1.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'moc': True,
  'label': 'LNST công ty mẹ MSB (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit bars',
  'say': 'Bước một, lợi nhuận. quý ba năm hai nghìn không trăm hai mươi sáu MSB lãi sau thuế công ty mẹ khoảng một nghìn sáu trăm bốn mươi chín tỷ đồng, tăng '
         'hai mươi chín phẩy bốn phần trăm so với cùng kỳ và tăng ba mươi mốt phẩy chín phần trăm so với quý trước. Lũy kế chín tháng khoảng bốn nghìn bốn '
         'trăm mười bốn tỷ, tăng mười sáu phẩy chín phần trăm. Chuỗi tám quý khá phẳng, phần lớn các quý nằm quanh một nghìn hai trăm bốn mươi đến một nghìn '
         'sáu trăm năm mươi tỷ, chỉ có quý bốn năm hai nghìn không trăm hai mươi lăm vọt lên khoảng một nghìn tám trăm năm mươi mốt tỷ. Một quý tăng mạnh sau '
         'nhiều quý đi ngang là tín hiệu tốt, nhưng cần thêm một hai quý nữa để biết đó là xu hướng mới hay chỉ là một quý thuận lợi.',
  'bars': [('Q4/24', 1617.0, (56, 189, 248), '1.617'),
           ('Q1/25', 1265.6, (56, 189, 248), '1.266'),
           ('Q2/25', 1237.5, (56, 189, 248), '1.238'),
           ('Q3/25', 1274.2, (56, 189, 248), '1.274'),
           ('Q4/25', 1851.2, (56, 189, 248), '1.851'),
           ('Q1/26', 1514.2, (56, 189, 248), '1.514'),
           ('Q2/26', 1250.6, (56, 189, 248), '1.251'),
           ('Q3/26', 1649.2, (34, 197, 94), '1.649')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần MSB (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'lending',
  'say': 'Bước hai, mảng cốt lõi. Thu nhập lãi thuần quý ba năm hai nghìn không trăm hai mươi sáu khoảng ba nghìn bốn trăm hai mươi hai tỷ đồng, tăng hai mươi '
         'mốt phẩy sáu phần trăm so với cùng kỳ, cao nhất trong tám quý. Biên lãi ròng NIM khoảng hai phẩy tám ba phần trăm. Thu nhập lãi thuần tăng hai mươi '
         'mốt phẩy sáu phần trăm và lợi nhuận tăng hai mươi chín phẩy bốn phần trăm là hai con số khá gần nhau, nghĩa là lợi nhuận quý này phần lớn có nền '
         'tảng từ cho vay. Đây là điểm tích cực. Tuy vậy NIM dưới ba phần trăm thấp hơn nhiều ngân hàng bán lẻ, nên dư địa tăng lợi nhuận từ biên lãi không '
         'lớn.',
  'bars': [('Q4/24', 3138.9, (56, 189, 248), '3.139'),
           ('Q1/25', 2503.8, (56, 189, 248), '2.504'),
           ('Q2/25', 2584.8, (56, 189, 248), '2.585'),
           ('Q3/25', 2815.3, (56, 189, 248), '2.815'),
           ('Q4/25', 3043.6, (56, 189, 248), '3.044'),
           ('Q1/26', 3197.5, (56, 189, 248), '3.198'),
           ('Q2/26', 3001.2, (56, 189, 248), '3.001'),
           ('Q3/26', 3422.0, (34, 197, 94), '3.422')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Lãi dịch vụ',
  'moc': True,
  'label': 'MSB – nguồn thu ngoài lãi',
  'cap': ('LÃI DỊCH VỤ', '+51,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'banking services',
  'say': 'Bước ba, lãi dịch vụ. quý ba năm hai nghìn không trăm hai mươi sáu MSB có khoảng ba trăm linh hai tỷ đồng lãi dịch vụ, tăng năm mươi mốt phẩy bốn '
         'phần trăm so với cùng kỳ. Tốc độ tăng cao, nhưng quy mô còn nhỏ, chỉ khoảng một phần mười một thu nhập lãi thuần. Lãi dịch vụ tăng nhanh giúp ngân '
         'hàng bớt phụ thuộc vào biên lãi, nhưng với quy mô này nó chưa đủ để thay đổi bức tranh lợi nhuận. Anh chị nên coi đây là điểm cộng, không phải động '
         'lực chính.',
  'cards': [('Lãi dịch vụ', '302 tỷ', '+51,4%'), ('Thu nhập lãi thuần', '3.422 tỷ', '+21,6%'), ('NIM', '≈ 2,83%', 'biên lãi ròng')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Nợ xấu và bộ đệm',
  'moc': True,
  'label': 'MSB – chất lượng tài sản',
  'cap': ('NỢ XẤU 2,70%', 'ĐỆM ≈ 47%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'thin buffer warning',
  'say': 'Bước bốn, đây là phần quan trọng nhất của báo cáo này. Tỷ lệ nợ xấu của MSB cuối quý ba năm hai nghìn không trăm hai mươi sáu khoảng hai phẩy bảy '
         'không phần trăm, tăng từ hai phẩy năm ba phần trăm ở quý trước. Bộ đệm dự phòng chỉ phủ khoảng bốn mươi bảy phần trăm nợ xấu. Nói đơn giản, cứ một '
         'trăm đồng nợ xấu, ngân hàng mới để sẵn khoảng bốn mươi bảy đồng dự phòng. So với CTG có bộ đệm khoảng một trăm sáu mươi phần trăm, khác biệt rất '
         'lớn. Bộ đệm mỏng có hai hệ quả. Một, nếu nợ xấu tiếp tục tăng, ngân hàng phải trích lập nhiều hơn và lợi nhuận bị ảnh hưởng trực tiếp. Hai, ngân '
         'hàng không có dư địa để giảm trích lập làm đẹp lợi nhuận như một số ngân hàng khác.',
  'cards': [('Nợ xấu', '2,70%', 'quý trước 2,53%'), ('Bao phủ nợ xấu', '≈ 47%', 'bộ đệm mỏng'), ('So sánh', 'CTG ≈ 160%', 'cùng quý')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá',
  'moc': True,
  'label': 'MSB – định giá ngày 6/11/2026',
  'cap': ('P/B 1,31', 'ROE 14,3%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation compare',
  'say': 'Bước năm, định giá. Theo dữ liệu ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, MSB có P trên E khoảng chín phẩy tám ba lần, P trên '
         'B khoảng một phẩy ba một lần, ROE khoảng mười bốn phẩy ba phần trăm, vốn hóa khoảng sáu mươi mốt nghìn năm trăm tám mươi chín tỷ đồng. Giá đóng cửa '
         'tuần gần nhất khoảng mười sáu phẩy ba năm nghìn đồng, gần mức cao nhất năm mươi hai tuần, trong khi đáy tháng ba năm hai nghìn không trăm hai mươi '
         'sáu khoảng chín phẩy không nghìn đồng. Đặt cạnh nhau: MSB có ROE mười bốn phẩy ba phần trăm mà P trên B một phẩy ba một lần, còn CTG có ROE hai mươi '
         'hai phẩy năm phần trăm mà P trên B một phẩy một chín lần. Thị trường đang trả giá cao hơn cho một ngân hàng có hiệu quả vốn thấp hơn và bộ đệm mỏng '
         'hơn. Điều đó có thể có lý do riêng, nhưng anh chị cần biết mình đang trả giá cho kỳ vọng nào.',
  'cards': [('P/E', '9,83 lần', '6/11/2026'), ('P/B · ROE', '1,31 · 14,3%', 'CTG: 1,19 · 22,5%'), ('Giá', '16,35', 'đáy 3/2026: 9,0')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'MSB – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk list',
  'say': 'Rủi ro cần theo dõi với MSB. Một, nợ xấu: đã tăng hai quý, cần xem quý bốn có dừng lại không. Hai, bộ đệm bốn mươi bảy phần trăm: nếu nợ xấu tăng, '
         'chi phí trích lập sẽ tăng nhanh. Ba, định giá: giá đã tăng gần gấp đôi từ đáy tháng ba, kỳ vọng trong giá đã cao hơn. Bốn, quản trị vị thế: với cổ '
         'phiếu đã tăng mạnh, người đang có lãi nên xác định trước mức chốt lời từng phần và mức bảo vệ lợi nhuận, thay vì để lãi trôi theo cảm xúc.',
  'items': [('Nợ xấu tăng 2 quý liền', (239, 68, 68)),
            ('Bộ đệm chỉ ≈ 47%', (239, 68, 68)),
            ('Giá gần gấp đôi từ đáy', (255, 196, 0)),
            ('Kế hoạch chốt lời từng phần', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LÃI TĂNG', 'ĐỆM MỎNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Khi lợi nhuận một ngân hàng tăng gần ba mươi phần trăm nhưng nợ xấu cũng tăng và bộ đệm chỉ bốn mươi bảy phần trăm, anh chị '
         'sẽ đặt trọng số nhiều hơn cho con số nào?'}]

S['CH2111B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Quản trị rủi ro – Thanh khoản',
  'cap': ('BÁN 5 TỶ', 'MẤT 5 PHIÊN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'stock exchange liquidity',
  'say': 'Hai cổ phiếu đều có lãi, đều có ROE cao. Một mã khớp lệnh khoảng năm trăm tỷ đồng mỗi ngày, mã kia khoảng mười tỷ. Nếu cần bán năm tỷ đồng cổ phiếu '
         'trong một ngày xấu, ở mã thứ nhất anh chị bán xong trong vài phút. Ở mã thứ hai, có thể mất năm phiên hoặc phải chấp nhận bán giá thấp hơn nhiều. '
         'Rủi ro thanh khoản là rủi ro mà người mới hay bỏ qua nhất, vì nó chỉ lộ ra đúng lúc mình cần bán. Video này em giải thích cách đo thanh khoản, quy '
         'tắc giới hạn khối lượng, và cách đặt tỷ trọng cho mã ít giao dịch. Số liệu khối lượng trung bình mười phiên tính đến ngày sáu tháng mười một năm hai '
         'nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'BMPW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[6, 180.67, 'Đỉnh tuần 15/12/25: 180,67', 0.6],
                        [19, 114.64, 'Đáy tuần 23/3/26: 114,64', 1.6],
                        [51, 136.4, 'Tuần 2/11/26: 136,40', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Giá trị giao dịch mỗi ngày',
  'moc': True,
  'label': 'Giá trị giao dịch trung bình 10 phiên (tỷ đồng/ngày, ước tính)',
  'cap': ('THANH KHOẢN', 'CHÊNH 50 LẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'trading volume',
  'say': 'Chương một, đo thanh khoản bằng giá trị giao dịch mỗi ngày, tức khối lượng trung bình nhân với giá. Theo khối lượng trung bình mười phiên đến ngày '
         'sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, HPG giao dịch khoảng bốn trăm chín mươi tám tỷ đồng mỗi ngày, SSI khoảng bốn trăm bốn mươi '
         'bảy tỷ, MBB khoảng hai trăm bốn mươi tám tỷ. Ở nhóm vừa và nhỏ, REE khoảng mười lăm phẩy sáu tỷ, BMP khoảng mười phẩy hai tỷ, QNS khoảng tám phẩy '
         'năm tỷ, CMG khoảng năm phẩy bốn tỷ. Khoảng cách giữa HPG và BMP gần năm mươi lần. Đây là con số ước tính, nhưng đủ để thấy hai nhóm cổ phiếu sống '
         'trong hai thế giới thanh khoản rất khác nhau.',
  'bars': [('HPG', 498.0, (34, 197, 94), '≈ 498'),
           ('SSI', 447.0, (34, 197, 94), '≈ 447'),
           ('MBB', 248.0, (34, 197, 94), '≈ 248'),
           ('REE', 15.6, (255, 196, 0), '≈ 15,6'),
           ('BMP', 10.2, (255, 196, 0), '≈ 10,2'),
           ('QNS', 8.5, (239, 68, 68), '≈ 8,5'),
           ('CMG', 5.4, (239, 68, 68), '≈ 5,4')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Quy tắc 10%',
  'moc': True,
  'label': 'Không bán quá 10% giá trị giao dịch một phiên',
  'cap': ('QUY TẮC 10%', 'BÁN BAO LÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'time hourglass',
  'say': 'Chương hai, quy tắc mười phần trăm. Nhiều nhà đầu tư chuyên nghiệp đặt giới hạn: không mua hoặc bán quá mười phần trăm giá trị giao dịch trung bình '
         'một phiên, để không tự đẩy giá đi ngược mình. Áp dụng thử: với BMP khoảng mười phẩy hai tỷ một ngày, mười phần trăm là khoảng một tỷ. Muốn bán năm '
         'tỷ đồng mà không làm giá biến động mạnh, anh chị cần khoảng năm phiên. Với HPG, mười phần trăm là khoảng năm mươi tỷ một phiên, năm tỷ chỉ là một '
         'phần nhỏ. Trong ngày thị trường hoảng loạn, thanh khoản mã nhỏ còn có thể giảm mạnh, nên năm phiên có thể thành mười phiên.',
  'cards': [('BMP', '≈ 1 tỷ/phiên', '5 tỷ ≈ 5 phiên'),
            ('HPG', '≈ 50 tỷ/phiên', '5 tỷ < 1 phiên'),
            ('Ngày hoảng loạn', 'Thanh khoản co lại', '5 phiên → 10 phiên')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Cái giá của việc bán gấp',
  'moc': True,
  'label': 'Bán gấp mã ít giao dịch: chênh lệch giá mua – bán',
  'cap': ('BÁN GẤP', 'MẤT THÊM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'order book',
  'say': 'Chương ba, cái giá của việc bán gấp. Với mã ít giao dịch, khoảng cách giữa giá mua tốt nhất và giá bán tốt nhất thường rộng hơn, và mỗi mức giá chỉ '
         'có ít cổ phiếu chờ. Khi anh chị bán một lượng lớn ngay lập tức, lệnh sẽ ăn dần xuống nhiều mức giá thấp hơn. Mức lỗ thực tế vì thế lớn hơn điểm cắt '
         'lỗ trên giấy. Đây cũng là lý do quy tắc rủi ro một phần trăm cần giảm xuống, ví dụ còn không phẩy năm phần trăm, cho các mã thanh khoản thấp: vì anh '
         'chị không chắc bán được đúng giá cắt lỗ.',
  'cards': [('Chênh lệch mua – bán', 'Rộng hơn', 'mã ít giao dịch'),
            ('Lệnh lớn', 'Ăn nhiều mức giá', 'lỗ > kế hoạch'),
            ('Rủi ro mỗi lệnh', '1% → 0,5%', 'với mã kém thanh khoản')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Tỷ trọng theo thanh khoản',
  'moc': True,
  'label': 'Bốn quy tắc tỷ trọng theo thanh khoản',
  'cap': ('TỶ TRỌNG', 'THEO THANH KHOẢN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'rules list',
  'say': 'Chương bốn, đặt tỷ trọng theo thanh khoản. Một, trước khi mua, tính giá trị giao dịch trung bình mười hoặc hai mươi phiên. Hai, giữ vị thế của mình '
         'dưới khoảng một đến hai phiên giao dịch ở mức mười phần trăm, để có thể thoát trong vài ngày. Ba, mã có giá trị giao dịch dưới mười tỷ một ngày chỉ '
         'nên chiếm phần nhỏ của danh mục. Bốn, không dùng margin cho mã thanh khoản thấp, vì khi bị gọi ký quỹ, anh chị không bán kịp. Các mức này là tham '
         'khảo, quan trọng là anh chị có một con số và tuân thủ nó.',
  'items': [('Tính GTGD trung bình 10–20 phiên', (34, 197, 94)),
            ('Vị thế thoát được trong vài phiên', (34, 197, 94)),
            ('Mã < 10 tỷ/ngày: tỷ trọng nhỏ', (255, 196, 0)),
            ('Không dùng margin cho mã kém thanh khoản', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 5 – Thanh khoản không phải chất lượng',
  'moc': True,
  'label': 'Thanh khoản thấp ≠ doanh nghiệp xấu',
  'cap': ('THANH KHOẢN', '≠ CHẤT LƯỢNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'quality vs liquidity',
  'say': 'Chương năm, một hiểu lầm cần tránh. Thanh khoản thấp không có nghĩa là doanh nghiệp xấu. BMP có ROE khoảng bốn mươi mốt phẩy một phần trăm và tỷ '
         'suất cổ tức khoảng mười phẩy bảy tám phần trăm theo dữ liệu ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, nhưng giao dịch chỉ '
         'khoảng mười tỷ đồng mỗi ngày vì cổ đông lớn nắm phần lớn cổ phiếu. Ngược lại, thanh khoản cao cũng không đảm bảo an toàn: VIX giao dịch hàng nghìn '
         'tỷ mỗi ngày, nhưng lợi nhuận quý ba giảm chín mươi hai phẩy chín phần trăm. Thanh khoản trả lời câu hỏi khác: nếu mình sai, mình thoát ra nhanh đến '
         'đâu.',
  'cards': [('BMP', 'ROE 41,1%', 'GTGD ≈ 10 tỷ/ngày'),
            ('VIX', 'Thanh khoản rất cao', 'LN quý 3 −92,9%'),
            ('Câu hỏi đúng', 'Sai thì thoát nhanh?', 'không phải tốt hay xấu')]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('MUA DỄ', 'BÁN CÓ DỄ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Trong danh mục của mình, anh chị có mã nào mà nếu cần bán hết trong một ngày xấu, anh chị sẽ phải mất nhiều phiên không?'}]

S['CH2111C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Bài học lịch sử – Ngân hàng 2026',
  'cap': ('LÃI ĐẾN +34%', 'GIÁ ĐẾN −38%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank stocks history',
  'say': 'Năm hai nghìn không trăm hai mươi sáu, nhóm ngân hàng lớn báo lợi nhuận chín tháng tăng từ khoảng mười tám phần trăm đến ba mươi tư phần trăm. Cùng '
         'thời gian, giá cổ phiếu của chính những ngân hàng đó có lúc giảm từ hai mươi hai phần trăm đến gần ba mươi tám phần trăm so với đỉnh. Lợi nhuận đi '
         'một đường, giá đi một nẻo. Đây không phải lần đầu thị trường như vậy, và cũng sẽ không phải lần cuối. Video này em ghi lại bài học lịch sử của năm '
         'hai nghìn không trăm hai mươi sáu với năm ngân hàng lớn: VCB, BID, CTG, MBB và TCB. Ta sẽ đặt lợi nhuận và giá cạnh nhau, rồi rút ra bốn bài học cho '
         'người nắm giữ cổ phiếu ngân hàng. Số liệu giá đóng cửa đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'VCBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 78.15, 'Đỉnh tuần 12/1/26: 78,15', 0.6], [36, 52.6, 'Đáy tuần 20/7/26: 52,60', 1.6], [51, 53.6, 'Tuần 2/11/26: 53,60', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận chín tháng',
  'moc': True,
  'label': 'Tăng trưởng LNST 9 tháng 2026 so với cùng kỳ (%)',
  'cap': ('LỢI NHUẬN', '9 THÁNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit growth bank',
  'say': 'Chương một, lợi nhuận. Lũy kế chín tháng năm hai nghìn không trăm hai mươi sáu so với cùng kỳ: CTG tăng khoảng ba mươi ba phẩy tám phần trăm, MBB '
         'tăng khoảng ba mươi hai phẩy không phần trăm, BID tăng khoảng hai mươi lăm phẩy năm phần trăm, VCB tăng khoảng hai mươi tư phẩy bốn phần trăm, TCB '
         'tăng khoảng mười tám phẩy không phần trăm. Cả năm ngân hàng đều tăng hai chữ số. Nếu chỉ đọc báo cáo tài chính, năm hai nghìn không trăm hai mươi '
         'sáu là một năm tốt của ngành ngân hàng. Không có ngân hàng nào trong nhóm này báo lỗ hay lợi nhuận đi lùi.',
  'bars': [('CTG', 33.8, (34, 197, 94), '+33,8%'),
           ('MBB', 32.0, (34, 197, 94), '+32,0%'),
           ('BID', 25.5, (34, 197, 94), '+25,5%'),
           ('VCB', 24.4, (34, 197, 94), '+24,4%'),
           ('TCB', 18.0, (34, 197, 94), '+18,0%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Giá giảm từ đỉnh',
  'moc': True,
  'label': 'Mức giảm sâu nhất từ đỉnh, giá đóng cửa (%)',
  'cap': ('GIÁ', 'GIẢM TỪ ĐỈNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank stock fall',
  'say': 'Chương hai, giá. Tính theo giá đóng cửa, BID giảm khoảng ba mươi bảy phẩy bảy phần trăm từ ngày hai tháng hai năm hai nghìn không trăm hai mươi sáu '
         'đến ngày ba tháng mười một năm hai nghìn không trăm hai mươi sáu. TCB giảm khoảng ba mươi phẩy năm phần trăm từ tháng mười năm hai nghìn không trăm '
         'hai mươi lăm đến tháng bốn năm hai nghìn không trăm hai mươi sáu. CTG giảm khoảng hai mươi chín phẩy bảy phần trăm từ tháng một đến tháng bảy năm '
         'hai nghìn không trăm hai mươi sáu. VCB giảm khoảng hai mươi chín phẩy không phần trăm từ tháng một đến đầu tháng mười một năm hai nghìn không trăm '
         'hai mươi sáu. MBB giảm khoảng hai mươi hai phẩy bốn phần trăm từ tháng hai đến tháng bảy năm hai nghìn không trăm hai mươi sáu. Người mua ở đỉnh đầu '
         'năm, dù chọn đúng ngân hàng có lợi nhuận tăng, vẫn có lúc lỗ từ hai mươi hai phần trăm đến gần ba mươi tám phần trăm.',
  'bars': [('BID', 37.7, (239, 68, 68), '−37,7%'),
           ('TCB', 30.5, (239, 68, 68), '−30,5%'),
           ('CTG', 29.7, (239, 68, 68), '−29,7%'),
           ('VCB', 29.0, (239, 68, 68), '−29,0%'),
           ('MBB', 22.4, (255, 196, 0), '−22,4%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Vì sao giá và lãi đi ngược',
  'moc': True,
  'label': 'Ba lý do giá đi ngược lợi nhuận',
  'cap': ('VÌ SAO', 'ĐI NGƯỢC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'market psychology',
  'say': 'Chương ba, vì sao giá và lợi nhuận đi ngược nhau. Lý do thứ nhất: giá đã đi trước. Nhiều mã ngân hàng tăng mạnh trong năm hai nghìn không trăm hai '
         'mươi lăm, kỳ vọng tăng trưởng hai nghìn không trăm hai mươi sáu đã nằm trong giá từ trước khi lợi nhuận được công bố. Lý do thứ hai: chất lượng lợi '
         'nhuận. Có ngân hàng tăng lãi nhờ giảm trích lập, như BID với chi phí dự phòng giảm hai mươi lăm phần trăm trong quý ba, thị trường sẽ chiết khấu '
         'phần đó. Lý do thứ ba: dòng tiền. Khi dòng tiền xoay sang ngành khác hoặc rút khỏi thị trường, cổ phiếu vốn hóa lớn bị bán ra trước vì dễ bán nhất.',
  'cards': [('Giá đi trước', 'kỳ vọng đã vào giá', ''), ('Chất lượng lợi nhuận', 'tăng nhờ giảm trích lập', ''), ('Dòng tiền', 'mã lớn bị bán trước', '')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Bốn bài học',
  'moc': True,
  'label': 'Bốn bài học từ ngân hàng năm 2026',
  'cap': ('BỐN BÀI HỌC', 'NĂM 2026'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'lessons',
  'say': 'Chương bốn, bốn bài học. Một, lợi nhuận tăng không bảo vệ anh chị khỏi giảm giá nếu anh chị mua ở mức giá đã phản ánh kỳ vọng cao. Hai, đọc chất '
         'lượng lợi nhuận, không chỉ đọc tốc độ tăng. Ba, ngân hàng là một ngành: cầm năm mã ngân hàng vẫn là một khoản cược tập trung, khi cả nhóm giảm thì '
         'cả năm mã cùng giảm. Bốn, người đi qua được những nhịp như thế này thường là người có tỷ trọng hợp lý và không dùng margin, vì họ không bị buộc phải '
         'bán ở đáy.',
  'items': [('Lãi tăng ≠ giá tăng nếu mua đắt', (255, 196, 0)),
            ('Đọc chất lượng lợi nhuận', (34, 197, 94)),
            ('Năm mã ngân hàng = một ngành', (239, 68, 68)),
            ('Tỷ trọng hợp lý, không margin', (34, 197, 94))]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá hôm nay',
  'moc': True,
  'label': 'P/B và ROE ngày 6/11/2026',
  'cap': ('ĐỊNH GIÁ', 'HÔM NAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation table',
  'say': 'Chương năm, định giá hôm nay. Theo dữ liệu ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu: CTG có P trên B khoảng một phẩy một chín '
         'lần với ROE hai mươi hai phẩy năm phần trăm. MBB có P trên B khoảng một phẩy hai năm lần với ROE hai mươi mốt phẩy tám phần trăm. TCB có P trên B '
         'khoảng một phẩy hai năm lần với ROE mười lăm phẩy bốn phần trăm. BID có P trên B khoảng một phẩy hai bảy lần với ROE mười tám phẩy năm phần trăm. '
         'VCB có P trên B khoảng một phẩy bảy chín lần với ROE mười bảy phẩy sáu phần trăm. Mặt bằng định giá đã thấp hơn đầu năm khá nhiều. Nhưng định giá '
         'thấp hơn không có nghĩa giá sẽ hồi ngay. Lịch sử cho thấy giá có thể ở vùng thấp nhiều tháng trước khi thị trường thay đổi cách nhìn.',
  'cards': [('CTG · MBB', 'P/B 1,19 · 1,25', 'ROE 22,5% · 21,8%'), ('TCB · BID', 'P/B 1,25 · 1,27', 'ROE 15,4% · 18,5%'), ('VCB', 'P/B 1,79', 'ROE 17,6%')]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LÃI ĐI MỘT ĐƯỜNG', 'GIÁ ĐI MỘT NẺO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Nhìn lại năm hai nghìn không trăm hai mươi sáu, nếu được làm lại từ đầu năm với cổ phiếu ngân hàng, anh chị sẽ thay đổi điều '
         'gì: thời điểm mua, tỷ trọng, hay cách chọn mã?'}]

META = {'CH1911A': {'title': 'Đọc BCTC 5 phút | BID: lãi quý +39,9% nhưng giá −37% từ đỉnh', 'bia': ('LÃI +39,9%', 'GIÁ −37%'), 'badge': '−37%'},
 'CH1911B': {'title': 'Quản trị vốn | Quy tắc 1%: thua 10 lệnh liên tiếp còn bao nhiêu vốn?', 'bia': ('THUA 10 LỆNH', 'CÒN 35%?'), 'badge': '1%'},
 'CH1911C': {'title': 'Đọc BCTC 5 phút | MWG: lãi +74,7%, biên gộp 21,7% – đã vào giá chưa?', 'bia': ('LÃI +74,7%', 'GIÁ −20%'), 'badge': '+74,7%'},
 'CH2011A': {'title': 'Đọc BCTC 5 phút | CTG: lãi +28,2%, bao phủ nợ xấu 160% – vì sao giá chưa hồi?', 'bia': ('BAO PHỦ 160%', 'GIÁ −22%'), 'badge': '160%'},
 'CH2011B': {'title': 'Quản trị rủi ro | Rủi ro tập trung: cổ phiếu tốt vẫn có lúc giảm 50–57%', 'bia': ('MÃ TỐT', 'VẪN −57%'), 'badge': '−57%'},
 'CH2011C': {'title': 'Đọc BCTC 5 phút | VNM: cổ tức 8,18%, ROE 31% nhưng giá 3 năm chỉ +1,4%', 'bia': ('CỔ TỨC 8,18%', 'GIÁ ĐI NGANG'), 'badge': '8,18%'},
 'CH2111A': {'title': 'Đọc BCTC 5 phút | MSB: lãi +29,4% nhưng bao phủ nợ xấu chỉ khoảng 47%', 'bia': ('LÃI +29,4%', 'ĐỆM CHỈ 47%'), 'badge': '47%'},
 'CH2111B': {'title': 'Quản trị rủi ro | Thanh khoản: bán 5 tỷ cổ phiếu mất 1 phút hay 5 phiên?', 'bia': ('BÁN 5 TỶ', 'MẤT 5 PHIÊN?'), 'badge': '×50'},
 'CH2111C': {'title': 'Bài học lịch sử | Ngân hàng 2026: lãi 9 tháng +18–34% nhưng giá có lúc −22–38%', 'bia': ('LÃI +34%', 'GIÁ −38%'), 'badge': '2026'}}
