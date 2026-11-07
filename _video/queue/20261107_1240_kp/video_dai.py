# -*- coding: utf-8 -*-
# VIDEO DÀI – NV1 soạn 7/11/2026 (lô 20261107_1240_kp: HI1211A, HI1311A, Y2_1211A, Y2_1311A, TS1211A, TS1311A, K2_1211A, K2_1311A, LST_1211A, LST_1311A, Y3_1211A, Y3_1311A). Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['HI1211A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'NKG – định giá nhanh',
  'cap': ('NKG P/E 24,6', 'ROE 3,2%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'steel coils',
  'say': 'Thép Nam Kim, mã NKG, đang giao dịch quanh mười hai phẩy mười lăm nghìn đồng, P trên E khoảng hai mươi bốn phẩy năm mươi chín lần, P trên B khoảng '
         'không phẩy bảy mươi bảy lần, ROE khoảng ba phẩy hai phần trăm. Lợi nhuận quý ba năm hai nghìn không trăm hai mươi sáu đạt khoảng một trăm hai mươi '
         'sáu tỷ, tăng một trăm năm mươi bốn phẩy tám phần trăm so với cùng kỳ. Rẻ thật, đắt thật, hay thị trường đang nhìn thấy điều gì khác? Video này em '
         'đặt ba con số định giá cạnh chuỗi lợi nhuận tám quý và rủi ro, để anh chị tự trả lời. Số liệu từ báo cáo quý ba năm hai nghìn không trăm hai mươi '
         'sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'NKGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[2, 16.05, 'Đỉnh tuần 17/11/25: 16,05', 0.6], [47, 9.0, 'Đáy tuần 5/10/26: 9,00', 1.6], [51, 12.15, 'Tuần 2/11/26: 12,15', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Doanh nghiệp kiếm tiền thế nào',
  'label': '',
  'cap': ('NKG', 'KIẾM TIỀN THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, Thép Nam Kim kiếm tiền thế nào. Mảng kinh doanh chính là tôn mạ và ống thép, bán trong nước và xuất khẩu. Với kiểu doanh nghiệp này, lợi '
         'nhuận phụ thuộc vào ba biến số: sản lượng bán ra, biên lợi nhuận trên mỗi đồng doanh thu, và chi phí vốn vay. Khi đọc báo cáo, anh chị nên nhìn ba '
         'biến số này cùng lúc, vì doanh thu tăng mạnh mà biên lợi nhuận mỏng đi hoặc lãi vay tăng nhanh thì lợi nhuận chưa chắc đã tăng theo.',
  'anh': 'steel coils',
  'moc': True,
  'cards': [('Doanh thu quý 3/2026', '≈ 5.472 tỷ', '+45,0% cùng kỳ'),
            ('LNST quý 3/2026', '≈ 126 tỷ', '+154,8% cùng kỳ'),
            ('Lũy kế 9 tháng', '≈ 253 tỷ', '+22,3%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lợi nhuận tám quý. Từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế '
         'công ty mẹ đi từ khoảng mười tám tỷ tới khoảng một trăm hai mươi sáu tỷ, trong đó có năm quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt '
         'là quý bốn năm hai nghìn không trăm hai mươi lăm lỗ chín tỷ, quý một năm hai nghìn không trăm hai mươi sáu lãi hai mươi hai tỷ, quý hai năm hai '
         'nghìn không trăm hai mươi sáu lãi một trăm linh bốn tỷ, quý ba năm hai nghìn không trăm hai mươi sáu lãi một trăm hai mươi sáu tỷ. Điều em muốn anh '
         'chị để ý không phải một quý đẹp, mà là xu hướng: lợi nhuận có đi lên đều, hay tăng giảm thất thường theo từng đợt.',
  'anh': 'financial report chart',
  'bars': [('Q4/24', 18.4, (56, 189, 248), '18'),
           ('Q1/25', 65.4, (56, 189, 248), '65'),
           ('Q2/25', 91.6, (56, 189, 248), '92'),
           ('Q3/25', 49.5, (56, 189, 248), '50'),
           ('Q4/25', 9.4, (239, 68, 68), '−9'),
           ('Q1/26', 22.3, (56, 189, 248), '22'),
           ('Q2/26', 104.1, (56, 189, 248), '104'),
           ('Q3/26', 126.2, (34, 197, 94), '126')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Doanh thu và biên lợi nhuận',
  'label': '',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, doanh thu. Doanh thu thuần quý ba năm hai nghìn không trăm hai mươi sáu đạt khoảng năm nghìn bốn trăm bảy mươi hai tỷ, tăng bốn mươi lăm '
         'phần trăm so với cùng kỳ, còn tám quý trước đó là khoảng bốn nghìn bốn trăm sáu mươi chín tỷ. Theo báo cáo, biên lợi nhuận gộp chín phần trăm (cùng '
         'kỳ bốn phẩy tám phần trăm), cải thiện. Doanh thu là phần khó làm đẹp nhất trong báo cáo, nên khi lợi nhuận tăng nhanh hơn doanh thu nhiều lần, anh '
         'chị cần hỏi phần chênh lệch đến từ đâu.',
  'anh': 'retail sales',
  'bars': [('Q4/24', 4469.1, (56, 189, 248), '4.469'),
           ('Q1/25', 4090.1, (56, 189, 248), '4.090'),
           ('Q2/25', 3808.5, (56, 189, 248), '3.808'),
           ('Q3/25', 3773.1, (56, 189, 248), '3.773'),
           ('Q4/25', 3136.5, (56, 189, 248), '3.136'),
           ('Q1/26', 3261.4, (56, 189, 248), '3.261'),
           ('Q2/26', 4150.2, (56, 189, 248), '4.150'),
           ('Q3/26', 5472.0, (34, 197, 94), '5.472')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Điểm tốt và điểm cần soi',
  'label': '',
  'cap': ('ĐIỂM TỐT', 'VÀ ĐIỂM CẦN SOI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, điểm tốt và điểm cần soi. Điểm tốt: Lợi nhuận quý tăng +một trăm năm mươi bốn phẩy tám phần trăm so với cùng kỳ; Doanh thu tăng +bốn '
         'mươi lăm phần trăm; Biên lợi nhuận gộp chín phần trăm (cùng kỳ bốn phẩy tám phần trăm), cải thiện. Điểm cần soi: Chi phí lãi vay tăng +tám mươi ba '
         'phần trăm, ăn vào lợi nhuận. Một báo cáo tốt hiếm khi tốt ở mọi dòng. Việc của nhà đầu tư là cân xem điểm cần soi là chuyện tạm thời, hay là dấu '
         'hiệu sớm của một xu hướng xấu kéo dài.',
  'anh': 'magnifying glass documents',
  'moc': True,
  'cards': [('Lợi nhuận quý tăng +154,8% so với ', '', ''), ('Doanh thu tăng +45,0%', '', ''), ('Chi phí lãi vay tăng +83,0%, ăn và', '', '')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Ba con số định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, định giá. Với giá khoảng mười hai phẩy mười lăm nghìn đồng, NKG đang có P trên E khoảng hai mươi bốn phẩy năm mươi chín lần, P trên B '
         'khoảng không phẩy bảy mươi bảy lần, ROE khoảng ba phẩy hai phần trăm, gần như không trả cổ tức tiền mặt. Vùng giá năm mươi hai tuần qua dao động từ '
         'khoảng chín phẩy mười lăm đến mười lăm phẩy sáu mươi tám nghìn đồng. P trên E thấp chưa chắc là rẻ nếu lợi nhuận đang ở đỉnh chu kỳ, và P trên E cao '
         'chưa chắc là đắt nếu lợi nhuận đang tăng nhanh. Vì vậy em luôn đặt định giá cạnh chuỗi lợi nhuận tám quý ở chương hai.',
  'anh': 'calculator',
  'cards': [('P/E', '24,59', 'lần'), ('P/B', '0,77', 'lần'), ('ROE', '3,2%', 'trên vốn chủ')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Thứ nhất là các điểm yếu đã thấy trong báo cáo: Chi phí lãi vay tăng +tám mươi ba phần trăm, ăn vào lợi nhuận. Thứ '
         'hai là kỳ vọng: khi giá đã tăng trước, một quý chậm lại có thể làm giá điều chỉnh mạnh. Thứ ba là quản trị vốn của chính mình. Dù doanh nghiệp tốt '
         'tới đâu, một mã không nên chiếm tỷ trọng quá lớn, để một bất ngờ trong báo cáo không làm hỏng cả danh mục.',
  'anh': 'warning sign',
  'items': [('Chi phí lãi vay tăng +83,0%, ăn vào lợi ', (239, 68, 68)),
            ('Giá đã phản ánh bao nhiêu kỳ vọng', (255, 196, 0)),
            ('Tỷ trọng mã này trong danh mục', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('NKG P/E 24,6', 'ANH CHỊ NGHĨ SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với ba con số định giá này, anh chị xếp NKG vào nhóm rẻ, hợp lý hay đắt, và vì sao?'}]

S['HI1311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'DGW – định giá nhanh',
  'cap': ('DGW P/E 9,0', 'ROE 26,9%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'warehouse distribution',
  'say': 'Digiworld, mã DGW, đang giao dịch quanh ba mươi tám phẩy năm nghìn đồng, P trên E khoảng chín phẩy không một lần, P trên B khoảng hai phẩy bảy mươi '
         'hai lần, ROE khoảng hai mươi sáu phẩy chín phần trăm. Lợi nhuận quý ba năm hai nghìn không trăm hai mươi sáu đạt khoảng hai trăm bảy mươi sáu tỷ, '
         'tăng sáu mươi lăm phẩy chín phần trăm so với cùng kỳ. Rẻ thật, đắt thật, hay thị trường đang nhìn thấy điều gì khác? Video này em đặt ba con số định '
         'giá cạnh chuỗi lợi nhuận tám quý và rủi ro, để anh chị tự trả lời. Số liệu từ báo cáo quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng '
         'hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'DGWW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[13, 55.29, 'Đỉnh tuần 2/2/26: 55,29', 0.6], [37, 30.76, 'Đáy tuần 27/7/26: 30,76', 1.6], [51, 38.5, 'Tuần 2/11/26: 38,50', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Doanh nghiệp kiếm tiền thế nào',
  'label': '',
  'cap': ('DGW', 'KIẾM TIỀN THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, Digiworld kiếm tiền thế nào. Mảng kinh doanh chính là phân phối điện thoại, máy tính, thiết bị văn phòng và hàng tiêu dùng. Với kiểu '
         'doanh nghiệp này, lợi nhuận phụ thuộc vào ba biến số: sản lượng bán ra, biên lợi nhuận trên mỗi đồng doanh thu, và chi phí vốn vay. Khi đọc báo cáo, '
         'anh chị nên nhìn ba biến số này cùng lúc, vì doanh thu tăng mạnh mà biên lợi nhuận mỏng đi hoặc lãi vay tăng nhanh thì lợi nhuận chưa chắc đã tăng '
         'theo.',
  'anh': 'warehouse distribution',
  'moc': True,
  'cards': [('Doanh thu quý 3/2026', '≈ 11.022 tỷ', '+49,1% cùng kỳ'),
            ('LNST quý 3/2026', '≈ 276 tỷ', '+65,9% cùng kỳ'),
            ('Lũy kế 9 tháng', '≈ 786 tỷ', '+102,5%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lợi nhuận tám quý. Từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế '
         'công ty mẹ đi từ khoảng một trăm bốn mươi tỷ tới khoảng hai trăm bảy mươi sáu tỷ, trong đó có bốn quý tăng so với quý liền trước. Bốn quý gần nhất '
         'lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm lãi một trăm năm mươi chín tỷ, quý một năm hai nghìn không trăm hai mươi sáu lãi hai trăm '
         'tỷ, quý hai năm hai nghìn không trăm hai mươi sáu lãi ba trăm mười tỷ, quý ba năm hai nghìn không trăm hai mươi sáu lãi hai trăm bảy mươi sáu tỷ. '
         'Điều em muốn anh chị để ý không phải một quý đẹp, mà là xu hướng: lợi nhuận có đi lên đều, hay tăng giảm thất thường theo từng đợt.',
  'anh': 'financial report chart',
  'bars': [('Q4/24', 140.4, (56, 189, 248), '140'),
           ('Q1/25', 105.9, (56, 189, 248), '106'),
           ('Q2/25', 115.8, (56, 189, 248), '116'),
           ('Q3/25', 166.4, (56, 189, 248), '166'),
           ('Q4/25', 159.2, (56, 189, 248), '159'),
           ('Q1/26', 200.2, (56, 189, 248), '200'),
           ('Q2/26', 309.5, (56, 189, 248), '310'),
           ('Q3/26', 276.2, (34, 197, 94), '276')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Doanh thu và biên lợi nhuận',
  'label': '',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, doanh thu. Doanh thu thuần quý ba năm hai nghìn không trăm hai mươi sáu đạt khoảng mười một nghìn không trăm hai mươi hai tỷ, tăng bốn '
         'mươi chín phẩy một phần trăm so với cùng kỳ, còn tám quý trước đó là khoảng năm nghìn tám trăm sáu mươi tỷ. Biên lợi nhuận gộp cần được so với cùng '
         'kỳ để biết doanh nghiệp giữ được giá bán hay không. Doanh thu là phần khó làm đẹp nhất trong báo cáo, nên khi lợi nhuận tăng nhanh hơn doanh thu '
         'nhiều lần, anh chị cần hỏi phần chênh lệch đến từ đâu.',
  'anh': 'retail sales',
  'bars': [('Q4/24', 5859.9, (56, 189, 248), '5.860'),
           ('Q1/25', 5519.3, (56, 189, 248), '5.519'),
           ('Q2/25', 5731.4, (56, 189, 248), '5.731'),
           ('Q3/25', 7390.6, (56, 189, 248), '7.391'),
           ('Q4/25', 7990.1, (56, 189, 248), '7.990'),
           ('Q1/26', 8500.2, (56, 189, 248), '8.500'),
           ('Q2/26', 7273.3, (56, 189, 248), '7.273'),
           ('Q3/26', 11022.2, (34, 197, 94), '11.022')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Điểm tốt và điểm cần soi',
  'label': '',
  'cap': ('ĐIỂM TỐT', 'VÀ ĐIỂM CẦN SOI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, điểm tốt và điểm cần soi. Điểm tốt: Lợi nhuận quý tăng +sáu mươi lăm phẩy chín phần trăm so với cùng kỳ; Doanh thu tăng +bốn mươi chín '
         'phẩy một phần trăm. Điểm cần soi: Chi phí lãi vay tăng +bốn mươi hai phẩy hai phần trăm, ăn vào lợi nhuận. Một báo cáo tốt hiếm khi tốt ở mọi dòng. '
         'Việc của nhà đầu tư là cân xem điểm cần soi là chuyện tạm thời, hay là dấu hiệu sớm của một xu hướng xấu kéo dài.',
  'anh': 'magnifying glass documents',
  'moc': True,
  'cards': [('Lợi nhuận quý tăng +65,9% so với c', '', ''), ('Doanh thu tăng +49,1%', '', ''), ('Chi phí lãi vay tăng +42,2%, ăn và', '', '')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Ba con số định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, định giá. Với giá khoảng ba mươi tám phẩy năm nghìn đồng, DGW đang có P trên E khoảng chín phẩy không một lần, P trên B khoảng hai phẩy '
         'bảy mươi hai lần, ROE khoảng hai mươi sáu phẩy chín phần trăm, tỷ suất cổ tức khoảng hai phẩy sáu phần trăm. Vùng giá năm mươi hai tuần qua dao động '
         'từ khoảng ba mươi hai phẩy bốn mươi hai đến năm mươi ba phẩy bốn mươi tám nghìn đồng. P trên E thấp chưa chắc là rẻ nếu lợi nhuận đang ở đỉnh chu '
         'kỳ, và P trên E cao chưa chắc là đắt nếu lợi nhuận đang tăng nhanh. Vì vậy em luôn đặt định giá cạnh chuỗi lợi nhuận tám quý ở chương hai.',
  'anh': 'calculator',
  'cards': [('P/E', '9,01', 'lần'), ('P/B', '2,72', 'lần'), ('ROE', '26,9%', 'trên vốn chủ')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Thứ nhất là các điểm yếu đã thấy trong báo cáo: Chi phí lãi vay tăng +bốn mươi hai phẩy hai phần trăm, ăn vào lợi '
         'nhuận. Thứ hai là kỳ vọng: khi giá đã tăng trước, một quý chậm lại có thể làm giá điều chỉnh mạnh. Thứ ba là quản trị vốn của chính mình. Dù doanh '
         'nghiệp tốt tới đâu, một mã không nên chiếm tỷ trọng quá lớn, để một bất ngờ trong báo cáo không làm hỏng cả danh mục.',
  'anh': 'warning sign',
  'items': [('Chi phí lãi vay tăng +42,2%, ăn vào lợi ', (239, 68, 68)),
            ('Giá đã phản ánh bao nhiêu kỳ vọng', (255, 196, 0)),
            ('Tỷ trọng mã này trong danh mục', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('DGW P/E 9,0', 'ANH CHỊ NGHĨ SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với ba con số định giá này, anh chị xếp DGW vào nhóm rẻ, hợp lý hay đắt, và vì sao?'}]

S['Y2_1211A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'POW – soi BCTC',
  'cap': ('SOI BCTC POW', 'LÃI +129,8%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'power plant',
  'say': 'Báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của PV Power, mã POW, cho thấy lợi nhuận sau thuế công ty mẹ khoảng một nghìn tám '
         'trăm sáu mươi tỷ, tăng một trăm hai mươi chín phẩy tám phần trăm so với cùng kỳ. Lũy kế chín tháng đạt khoảng sáu nghìn bốn trăm ba mươi bốn tỷ, '
         'tăng hai trăm bốn mươi sáu phẩy năm phần trăm. Con số tổng nhìn qua là một chuyện, còn lợi nhuận đến từ đâu, chi phí nào đang tăng, và điều gì cần '
         'theo dõi tiếp là chuyện khác. Video này em soi từng dòng quan trọng để anh chị tự đánh giá.',
  'chart': {'sym': 'POWW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 16.85, 'Đỉnh tuần 2/3/26: 16,85', 0.6], [0, 11.32, 'Đáy tuần 3/11/25: 11,32', 1.6], [51, 12.35, 'Tuần 2/11/26: 12,35', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Doanh nghiệp kiếm tiền thế nào',
  'label': '',
  'cap': ('POW', 'KIẾM TIỀN THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, PV Power kiếm tiền thế nào. Mảng kinh doanh chính là sản xuất điện từ khí, than và thủy điện. Với kiểu doanh nghiệp này, lợi nhuận phụ '
         'thuộc vào ba biến số: sản lượng bán ra, biên lợi nhuận trên mỗi đồng doanh thu, và chi phí vốn vay. Khi đọc báo cáo, anh chị nên nhìn ba biến số này '
         'cùng lúc, vì doanh thu tăng mạnh mà biên lợi nhuận mỏng đi hoặc lãi vay tăng nhanh thì lợi nhuận chưa chắc đã tăng theo.',
  'anh': 'power plant',
  'moc': True,
  'cards': [('Doanh thu quý 3/2026', '≈ 16.772 tỷ', '+113,5% cùng kỳ'),
            ('LNST quý 3/2026', '≈ 1.860 tỷ', '+129,8% cùng kỳ'),
            ('Lũy kế 9 tháng', '≈ 6.434 tỷ', '+246,5%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lợi nhuận tám quý. Từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế '
         'công ty mẹ đi từ khoảng bốn mươi sáu tỷ tới khoảng một nghìn tám trăm sáu mươi tỷ, trong đó có năm quý tăng so với quý liền trước. Bốn quý gần nhất '
         'lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm lãi năm trăm bảy mươi tỷ, quý một năm hai nghìn không trăm hai mươi sáu lãi một nghìn hai '
         'trăm tỷ, quý hai năm hai nghìn không trăm hai mươi sáu lãi ba nghìn ba trăm bảy mươi lăm tỷ, quý ba năm hai nghìn không trăm hai mươi sáu lãi một '
         'nghìn tám trăm sáu mươi tỷ. Điều em muốn anh chị để ý không phải một quý đẹp, mà là xu hướng: lợi nhuận có đi lên đều, hay tăng giảm thất thường '
         'theo từng đợt.',
  'anh': 'financial report chart',
  'bars': [('Q4/24', 45.8, (56, 189, 248), '46'),
           ('Q1/25', 445.1, (56, 189, 248), '445'),
           ('Q2/25', 602.4, (56, 189, 248), '602'),
           ('Q3/25', 809.3, (56, 189, 248), '809'),
           ('Q4/25', 569.8, (56, 189, 248), '570'),
           ('Q1/26', 1199.6, (56, 189, 248), '1.200'),
           ('Q2/26', 3375.3, (56, 189, 248), '3.375'),
           ('Q3/26', 1859.6, (34, 197, 94), '1.860')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Doanh thu và biên lợi nhuận',
  'label': '',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, doanh thu. Doanh thu thuần quý ba năm hai nghìn không trăm hai mươi sáu đạt khoảng mười sáu nghìn bảy trăm bảy mươi hai tỷ, tăng một trăm '
         'mười ba phẩy năm phần trăm so với cùng kỳ, còn tám quý trước đó là khoảng tám nghìn sáu trăm mười chín tỷ. Theo báo cáo, biên lợi nhuận gộp mười ba '
         'phẩy tám phần trăm (cùng kỳ mười sáu phẩy bốn phần trăm), thu hẹp. Doanh thu là phần khó làm đẹp nhất trong báo cáo, nên khi lợi nhuận tăng nhanh '
         'hơn doanh thu nhiều lần, anh chị cần hỏi phần chênh lệch đến từ đâu.',
  'anh': 'retail sales',
  'bars': [('Q4/24', 8619.2, (56, 189, 248), '8.619'),
           ('Q1/25', 8150.3, (56, 189, 248), '8.150'),
           ('Q2/25', 9398.8, (56, 189, 248), '9.399'),
           ('Q3/25', 7855.2, (56, 189, 248), '7.855'),
           ('Q4/25', 8901.9, (56, 189, 248), '8.902'),
           ('Q1/26', 12327.0, (56, 189, 248), '12.327'),
           ('Q2/26', 20306.3, (56, 189, 248), '20.306'),
           ('Q3/26', 16772.2, (34, 197, 94), '16.772')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Điểm tốt và điểm cần soi',
  'label': '',
  'cap': ('ĐIỂM TỐT', 'VÀ ĐIỂM CẦN SOI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, điểm tốt và điểm cần soi. Điểm tốt: Lợi nhuận quý tăng +một trăm hai mươi chín phẩy tám phần trăm so với cùng kỳ; Doanh thu tăng +một '
         'trăm mười ba phẩy năm phần trăm. Điểm cần soi: So với quý trước, lợi nhuận giảm âm bốn mươi bốn phẩy chín phần trăm; Biên lợi nhuận gộp mười ba phẩy '
         'tám phần trăm (cùng kỳ mười sáu phẩy bốn phần trăm), thu hẹp; Chi phí lãi vay tăng +ba trăm linh bốn phẩy một phần trăm, ăn vào lợi nhuận. Một báo '
         'cáo tốt hiếm khi tốt ở mọi dòng. Việc của nhà đầu tư là cân xem điểm cần soi là chuyện tạm thời, hay là dấu hiệu sớm của một xu hướng xấu kéo dài.',
  'anh': 'magnifying glass documents',
  'moc': True,
  'cards': [('Lợi nhuận quý tăng +129,8% so với ', '', ''),
            ('Doanh thu tăng +113,5%', '', ''),
            ('So với quý trước, lợi nhuận giảm −', '', ''),
            ('Biên lợi nhuận gộp 13,8% (cùng kỳ ', '', '')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Ba con số định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, định giá. Với giá khoảng mười hai phẩy ba mươi lăm nghìn đồng, POW đang có P trên E khoảng sáu phẩy ba mươi sáu lần, P trên B khoảng '
         'không phẩy tám mươi tám lần, ROE khoảng mười lăm phẩy ba phần trăm, gần như không trả cổ tức tiền mặt. Vùng giá năm mươi hai tuần qua dao động từ '
         'khoảng mười một phẩy năm mươi lăm đến mười sáu phẩy năm mươi lăm nghìn đồng. P trên E thấp chưa chắc là rẻ nếu lợi nhuận đang ở đỉnh chu kỳ, và P '
         'trên E cao chưa chắc là đắt nếu lợi nhuận đang tăng nhanh. Vì vậy em luôn đặt định giá cạnh chuỗi lợi nhuận tám quý ở chương hai.',
  'anh': 'calculator',
  'cards': [('P/E', '6,36', 'lần'), ('P/B', '0,88', 'lần'), ('ROE', '15,3%', 'trên vốn chủ')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Thứ nhất là các điểm yếu đã thấy trong báo cáo: So với quý trước, lợi nhuận giảm âm bốn mươi bốn phẩy chín phần '
         'trăm; Biên lợi nhuận gộp mười ba phẩy tám phần trăm (cùng kỳ mười sáu phẩy bốn phần trăm), thu hẹp; Chi phí lãi vay tăng +ba trăm linh bốn phẩy một '
         'phần trăm, ăn vào lợi nhuận. Thứ hai là kỳ vọng: khi giá đã tăng trước, một quý chậm lại có thể làm giá điều chỉnh mạnh. Thứ ba là quản trị vốn của '
         'chính mình. Dù doanh nghiệp tốt tới đâu, một mã không nên chiếm tỷ trọng quá lớn, để một bất ngờ trong báo cáo không làm hỏng cả danh mục.',
  'anh': 'warning sign',
  'items': [('So với quý trước, lợi nhuận giảm −44,9%', (239, 68, 68)),
            ('Biên lợi nhuận gộp 13,8% (cùng kỳ 16,4%)', (239, 68, 68)),
            ('Chi phí lãi vay tăng +304,1%, ăn vào lợi', (239, 68, 68)),
            ('Giá đã phản ánh bao nhiêu kỳ vọng', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('SOI BCTC POW', 'ANH CHỊ NGHĨ SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Trong báo cáo quý này của POW, dòng nào làm anh chị yên tâm nhất và dòng nào làm anh chị lo nhất?'}]

S['Y2_1311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'CMG – soi BCTC',
  'cap': ('SOI BCTC CMG', 'LÃI −1,2%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'data center',
  'say': 'Báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của CMC, mã CMG, cho thấy lợi nhuận sau thuế công ty mẹ khoảng tám mươi chín tỷ, giảm '
         'một phẩy hai phần trăm so với cùng kỳ. Lũy kế chín tháng đạt khoảng hai trăm năm mươi tám tỷ, giảm hai phẩy hai phần trăm. Con số tổng nhìn qua là '
         'một chuyện, còn lợi nhuận đến từ đâu, chi phí nào đang tăng, và điều gì cần theo dõi tiếp là chuyện khác. Video này em soi từng dòng quan trọng để '
         'anh chị tự đánh giá.',
  'chart': {'sym': 'CMGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 39.0, 'Đỉnh tuần 12/1/26: 39,00', 0.6], [51, 17.5, 'Đáy tuần 2/11/26: 17,50', 1.6], [51, 17.6, 'Tuần 2/11/26: 17,60', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Doanh nghiệp kiếm tiền thế nào',
  'label': '',
  'cap': ('CMG', 'KIẾM TIỀN THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, CMC kiếm tiền thế nào. Mảng kinh doanh chính là dịch vụ công nghệ thông tin, viễn thông và xuất khẩu phần mềm. Với kiểu doanh nghiệp '
         'này, lợi nhuận phụ thuộc vào ba biến số: sản lượng bán ra, biên lợi nhuận trên mỗi đồng doanh thu, và chi phí vốn vay. Khi đọc báo cáo, anh chị nên '
         'nhìn ba biến số này cùng lúc, vì doanh thu tăng mạnh mà biên lợi nhuận mỏng đi hoặc lãi vay tăng nhanh thì lợi nhuận chưa chắc đã tăng theo.',
  'anh': 'data center',
  'moc': True,
  'cards': [('Doanh thu quý 3/2026', '≈ 2.579 tỷ', '+6,6% cùng kỳ'), ('LNST quý 3/2026', '≈ 89 tỷ', '−1,2% cùng kỳ'), ('Lũy kế 9 tháng', '≈ 258 tỷ', '−2,2%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lợi nhuận tám quý. Từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế '
         'công ty mẹ đi từ khoảng một trăm hai mươi bảy tỷ tới khoảng tám mươi chín tỷ, trong đó có ba quý tăng so với quý liền trước. Bốn quý gần nhất lần '
         'lượt là quý bốn năm hai nghìn không trăm hai mươi lăm lãi một trăm ba mươi bốn tỷ, quý một năm hai nghìn không trăm hai mươi sáu lãi chín mươi bốn '
         'tỷ, quý hai năm hai nghìn không trăm hai mươi sáu lãi bảy mươi lăm tỷ, quý ba năm hai nghìn không trăm hai mươi sáu lãi tám mươi chín tỷ. Điều em '
         'muốn anh chị để ý không phải một quý đẹp, mà là xu hướng: lợi nhuận có đi lên đều, hay tăng giảm thất thường theo từng đợt.',
  'anh': 'financial report chart',
  'bars': [('Q4/24', 126.6, (56, 189, 248), '127'),
           ('Q1/25', 80.0, (56, 189, 248), '80'),
           ('Q2/25', 94.2, (56, 189, 248), '94'),
           ('Q3/25', 90.0, (56, 189, 248), '90'),
           ('Q4/25', 134.5, (56, 189, 248), '134'),
           ('Q1/26', 94.4, (56, 189, 248), '94'),
           ('Q2/26', 75.1, (56, 189, 248), '75'),
           ('Q3/26', 88.9, (34, 197, 94), '89')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Doanh thu và biên lợi nhuận',
  'label': '',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, doanh thu. Doanh thu thuần quý ba năm hai nghìn không trăm hai mươi sáu đạt khoảng hai nghìn năm trăm bảy mươi chín tỷ, tăng sáu phẩy sáu '
         'phần trăm so với cùng kỳ, còn tám quý trước đó là khoảng hai nghìn ba trăm linh ba tỷ. Biên lợi nhuận gộp cần được so với cùng kỳ để biết doanh '
         'nghiệp giữ được giá bán hay không. Doanh thu là phần khó làm đẹp nhất trong báo cáo, nên khi lợi nhuận tăng nhanh hơn doanh thu nhiều lần, anh chị '
         'cần hỏi phần chênh lệch đến từ đâu.',
  'anh': 'retail sales',
  'bars': [('Q4/24', 2303.2, (56, 189, 248), '2.303'),
           ('Q1/25', 1917.8, (56, 189, 248), '1.918'),
           ('Q2/25', 2210.1, (56, 189, 248), '2.210'),
           ('Q3/25', 2420.1, (56, 189, 248), '2.420'),
           ('Q4/25', 2563.1, (56, 189, 248), '2.563'),
           ('Q1/26', 2367.4, (56, 189, 248), '2.367'),
           ('Q2/26', 2323.2, (56, 189, 248), '2.323'),
           ('Q3/26', 2579.3, (34, 197, 94), '2.579')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Điểm tốt và điểm cần soi',
  'label': '',
  'cap': ('ĐIỂM TỐT', 'VÀ ĐIỂM CẦN SOI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, điểm tốt và điểm cần soi. Điểm tốt: Lợi nhuận lũy kế vẫn dương. Điểm cần soi: Chi phí lãi vay tăng +một trăm mười ba phẩy một phần trăm, '
         'ăn vào lợi nhuận. Một báo cáo tốt hiếm khi tốt ở mọi dòng. Việc của nhà đầu tư là cân xem điểm cần soi là chuyện tạm thời, hay là dấu hiệu sớm của '
         'một xu hướng xấu kéo dài.',
  'anh': 'magnifying glass documents',
  'moc': True,
  'cards': [('Lợi nhuận lũy kế vẫn dương', '', ''), ('Chi phí lãi vay tăng +113,1%, ăn v', '', '')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Ba con số định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, định giá. Với giá khoảng mười bảy phẩy sáu nghìn đồng, CMG đang có P trên E khoảng mười phẩy bốn mươi ba lần, P trên B khoảng một phẩy '
         'hai mươi mốt lần, ROE khoảng chín phẩy sáu phần trăm, tỷ suất cổ tức khoảng không phẩy sáu phần trăm. Vùng giá năm mươi hai tuần qua dao động từ '
         'khoảng mười bảy phẩy năm đến ba mươi bảy phẩy chín nghìn đồng. P trên E thấp chưa chắc là rẻ nếu lợi nhuận đang ở đỉnh chu kỳ, và P trên E cao chưa '
         'chắc là đắt nếu lợi nhuận đang tăng nhanh. Vì vậy em luôn đặt định giá cạnh chuỗi lợi nhuận tám quý ở chương hai.',
  'anh': 'calculator',
  'cards': [('P/E', '10,43', 'lần'), ('P/B', '1,21', 'lần'), ('ROE', '9,6%', 'trên vốn chủ')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Thứ nhất là các điểm yếu đã thấy trong báo cáo: Chi phí lãi vay tăng +một trăm mười ba phẩy một phần trăm, ăn vào '
         'lợi nhuận. Thứ hai là kỳ vọng: khi giá đã tăng trước, một quý chậm lại có thể làm giá điều chỉnh mạnh. Thứ ba là quản trị vốn của chính mình. Dù '
         'doanh nghiệp tốt tới đâu, một mã không nên chiếm tỷ trọng quá lớn, để một bất ngờ trong báo cáo không làm hỏng cả danh mục.',
  'anh': 'warning sign',
  'items': [('Chi phí lãi vay tăng +113,1%, ăn vào lợi', (239, 68, 68)),
            ('Giá đã phản ánh bao nhiêu kỳ vọng', (255, 196, 0)),
            ('Tỷ trọng mã này trong danh mục', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('SOI BCTC CMG', 'ANH CHỊ NGHĨ SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Trong báo cáo quý này của CMG, dòng nào làm anh chị yên tâm nhất và dòng nào làm anh chị lo nhất?'}]

S['TS1211A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'FPT – góp đều 37 tháng',
  'cap': ('GÓP ĐỀU 37 THÁNG', 'LỖ 37%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'piggy bank coins',
  'chart': {'sym': 'FPTW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[11, 97.48, 'Đỉnh tuần 19/1/26: 97,48', 0.6], [51, 49.55, 'Đáy tuần 2/11/26: 49,55', 1.6], [51, 50.8, 'Tuần 2/11/26: 50,80', 2.6]]},
  'say': 'Nếu từ cuối tháng mười năm hai nghìn không trăm hai mươi ba, mỗi tháng anh chị góp đều ba triệu đồng vào cổ phiếu FPT, sau ba mươi bảy tháng anh chị '
         'đã bỏ ra một trăm mười một triệu đồng. Ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, khoản đó có giá trị khoảng bảy mươi phẩy ba '
         'triệu đồng, tức lỗ khoảng ba mươi sáu phẩy sáu phần trăm. Nếu bỏ cùng số tiền một lần ngay từ đầu, kết quả là khoảng chín mươi tám phẩy tám triệu '
         'đồng. Video này em giải thích vì sao có chênh lệch đó và người tích sản rút ra được gì.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Hai cách, hai kết quả',
  'label': '',
  'cap': ('GÓP ĐỀU', 'HAY MỘT LẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, hai cách và hai kết quả. Cách thứ nhất, góp đều ba triệu mỗi tháng vào phiên giao dịch đầu tháng, tổng vốn một trăm mười một triệu, giá '
         'trị hiện tại khoảng bảy mươi phẩy ba triệu. Cách thứ hai, bỏ một trăm mười một triệu một lần ở giá khoảng năm mươi bảy phẩy một nghìn đồng cuối '
         'tháng mười năm hai nghìn không trăm hai mươi ba, giá trị hiện tại khoảng chín mươi tám phẩy tám triệu. Em tính trên giá đóng cửa đã điều chỉnh, chưa '
         'tính phí và thuế, để anh chị so được hai cách trên cùng một mặt bằng.',
  'anh': 'two paths',
  'moc': True,
  'bars': [('Góp đều 37 tháng', 70.3, (255, 196, 0), '70,3'), ('Mua một lần 10/2023', 98.8, (239, 68, 68), '98,8'), ('Vốn bỏ ra', 111, (56, 189, 248), '111')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Giá vốn bình quân',
  'label': '',
  'cap': ('GIÁ VỐN', 'BÌNH QUÂN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, giá vốn bình quân. Góp đều giúp giá vốn bình quân của anh chị ở khoảng tám mươi phẩy mười tám nghìn đồng, so với giá hiện tại khoảng năm '
         'mươi phẩy tám nghìn đồng. Trong ba mươi bảy tháng, giá đầu tháng cao nhất là khoảng một trăm mười sáu phẩy ba mươi mốt nghìn đồng vào tháng một năm '
         'hai nghìn không trăm hai mươi lăm, thấp nhất khoảng năm mươi sáu phẩy không năm nghìn đồng vào tháng mười một năm hai nghìn không trăm hai mươi ba. '
         'Góp đều không giúp mua ở đáy, nó giúp anh chị không phải đoán đáy, và tự động mua nhiều cổ phiếu hơn khi giá thấp.',
  'anh': 'price tags',
  'cards': [('Giá đầu kỳ', '57,10', '27/10/23'), ('Giá vốn bình quân', '≈ 80,18', 'góp đều 37 tháng'), ('Giá hiện tại', '≈ 50,80', '6/11/2026')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Doanh nghiệp làm ăn ra sao',
  'label': '',
  'cap': ('DOANH NGHIỆP', 'LÀM ĂN RA SAO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, phía sau giá là doanh nghiệp. Lợi nhuận sau thuế tám quý gần nhất của FPT đi từ khoảng hai nghìn không trăm chín mươi lăm tỷ lên khoảng '
         'hai nghìn bảy trăm hai mươi ba tỷ. Hiện cổ phiếu có P trên E khoảng chín phẩy ba mươi mốt lần và ROE khoảng hai mươi bốn phẩy ba phần trăm. Với '
         'người tích sản, câu hỏi quan trọng không phải giá tháng tới, mà là lợi nhuận và giá trị doanh nghiệp có tăng đều trong nhiều năm hay không.',
  'anh': 'factory office',
  'bars': [('Q4/24', 2094.7, (56, 189, 248), '2.095'),
           ('Q1/25', 2174.3, (56, 189, 248), '2.174'),
           ('Q2/25', 2257.5, (56, 189, 248), '2.258'),
           ('Q3/25', 2434.8, (56, 189, 248), '2.435'),
           ('Q4/25', 2509.5, (56, 189, 248), '2.510'),
           ('Q1/26', 2487.4, (56, 189, 248), '2.487'),
           ('Q2/26', 2567.6, (56, 189, 248), '2.568'),
           ('Q3/26', 2723.1, (34, 197, 94), '2.723')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Rủi ro của tích sản một mã',
  'label': '',
  'cap': ('RỦI RO', 'TÍCH SẢN MỘT MÃ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, rủi ro khi tích sản chỉ một mã. Kết quả của anh chị phụ thuộc hoàn toàn vào một doanh nghiệp và một ngành. Trong ba mươi bảy tháng qua, '
         'có lúc giá đầu tháng thấp hơn giá cao nhất khoảng năm mươi hai phần trăm. Nếu giai đoạn đó trùng với lúc anh chị cần tiền, khoản tích sản sẽ phải '
         'bán lỗ. Vì vậy người tích sản thường chia cho nhiều mã ở nhiều ngành, hoặc góp vào quỹ chỉ số, và luôn giữ quỹ dự phòng riêng.',
  'anh': 'single basket eggs',
  'moc': True,
  'cards': [('Rủi ro tập trung', 'Một mã, một ngành', ''), ('Rủi ro thời điểm', 'Cần tiền lúc giá thấp', ''), ('Cách giảm', 'Nhiều mã, quỹ dự phòng', '')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Người tích sản nên làm gì',
  'label': '',
  'cap': ('NGƯỜI TÍCH SẢN', 'NÊN LÀM GÌ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, ba việc người tích sản nên làm. Một, góp đều vào nhiều mã hoặc quỹ chỉ số thay vì dồn một mã. Hai, mỗi quý ghi lại giá vốn, tỷ trọng và '
         'lợi nhuận doanh nghiệp, để biết mình đang sở hữu gì. Ba, khi giá vượt xa tốc độ tăng lợi nhuận, có thể giảm tốc góp vào mã đó và chuyển sang mã '
         'khác, thay vì dừng hẳn kế hoạch.',
  'anh': 'planning notebook',
  'items': [('Góp đều nhiều mã hoặc quỹ chỉ số', (34, 197, 94)),
            ('Ghi giá vốn, tỷ trọng mỗi quý', (34, 197, 94)),
            ('Giá vượt xa lợi nhuận: giảm tốc góp', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('GÓP ĐỀU 37 THÁNG', 'LỖ 37%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu tính trên giá đóng cửa đã điều chỉnh, chưa gồm phí và thuế, đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Nếu bắt đầu '
         'tích sản từ hôm nay, anh chị sẽ chia số tiền mỗi tháng cho mấy mã?'}]

S['TS1311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'SSI – góp đều 37 tháng',
  'cap': ('GÓP ĐỀU 37 THÁNG', 'LÃI 3%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'piggy bank coins',
  'chart': {'sym': 'SSIW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 27.98, 'Đỉnh tuần 2/3/26: 27,98', 0.6], [37, 17.34, 'Đáy tuần 27/7/26: 17,34', 1.6], [51, 20.4, 'Tuần 2/11/26: 20,40', 2.6]]},
  'say': 'Nếu từ cuối tháng mười năm hai nghìn không trăm hai mươi ba, mỗi tháng anh chị góp đều ba triệu đồng vào cổ phiếu SSI, sau ba mươi bảy tháng anh chị '
         'đã bỏ ra một trăm mười một triệu đồng. Ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, khoản đó có giá trị khoảng một trăm mười bốn '
         'phẩy một triệu đồng, tức lãi khoảng hai phẩy tám phần trăm. Nếu bỏ cùng số tiền một lần ngay từ đầu, kết quả là khoảng một trăm ba mươi tám phẩy bảy '
         'triệu đồng. Video này em giải thích vì sao có chênh lệch đó và người tích sản rút ra được gì.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Hai cách, hai kết quả',
  'label': '',
  'cap': ('GÓP ĐỀU', 'HAY MỘT LẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, hai cách và hai kết quả. Cách thứ nhất, góp đều ba triệu mỗi tháng vào phiên giao dịch đầu tháng, tổng vốn một trăm mười một triệu, giá '
         'trị hiện tại khoảng một trăm mười bốn phẩy một triệu. Cách thứ hai, bỏ một trăm mười một triệu một lần ở giá khoảng mười sáu phẩy ba mươi hai nghìn '
         'đồng cuối tháng mười năm hai nghìn không trăm hai mươi ba, giá trị hiện tại khoảng một trăm ba mươi tám phẩy bảy triệu. Em tính trên giá đóng cửa đã '
         'điều chỉnh, chưa tính phí và thuế, để anh chị so được hai cách trên cùng một mặt bằng.',
  'anh': 'two paths',
  'moc': True,
  'bars': [('Góp đều 37 tháng', 114.1, (255, 196, 0), '114,1'),
           ('Mua một lần 10/2023', 138.7, (34, 197, 94), '138,7'),
           ('Vốn bỏ ra', 111, (56, 189, 248), '111')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Giá vốn bình quân',
  'label': '',
  'cap': ('GIÁ VỐN', 'BÌNH QUÂN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, giá vốn bình quân. Góp đều giúp giá vốn bình quân của anh chị ở khoảng mười chín phẩy tám mươi bốn nghìn đồng, so với giá hiện tại '
         'khoảng hai mươi phẩy bốn nghìn đồng. Trong ba mươi bảy tháng, giá đầu tháng cao nhất là khoảng hai mươi chín phẩy ba mươi sáu nghìn đồng vào tháng '
         'chín năm hai nghìn không trăm hai mươi lăm, thấp nhất khoảng mười lăm phẩy không năm nghìn đồng vào tháng mười một năm hai nghìn không trăm hai mươi '
         'ba. Góp đều không giúp mua ở đáy, nó giúp anh chị không phải đoán đáy, và tự động mua nhiều cổ phiếu hơn khi giá thấp.',
  'anh': 'price tags',
  'cards': [('Giá đầu kỳ', '16,32', '27/10/23'), ('Giá vốn bình quân', '≈ 19,84', 'góp đều 37 tháng'), ('Giá hiện tại', '≈ 20,40', '6/11/2026')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Doanh nghiệp làm ăn ra sao',
  'label': '',
  'cap': ('DOANH NGHIỆP', 'LÀM ĂN RA SAO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, phía sau giá là doanh nghiệp. Lợi nhuận sau thuế tám quý gần nhất của SSI đi từ khoảng hai trăm chín mươi bảy tỷ lên khoảng một nghìn một '
         'trăm hai mươi lăm tỷ. Hiện cổ phiếu có P trên E khoảng mười ba phẩy bảy mươi lăm lần và ROE khoảng mười hai phẩy hai phần trăm. Với người tích sản, '
         'câu hỏi quan trọng không phải giá tháng tới, mà là lợi nhuận và giá trị doanh nghiệp có tăng đều trong nhiều năm hay không.',
  'anh': 'factory office',
  'bars': [('Q4/24', 296.9, (56, 189, 248), '297'),
           ('Q1/25', 844.0, (56, 189, 248), '844'),
           ('Q2/25', 862.3, (56, 189, 248), '862'),
           ('Q3/25', 1475.1, (56, 189, 248), '1.475'),
           ('Q4/25', 817.5, (56, 189, 248), '818'),
           ('Q1/26', 1277.9, (56, 189, 248), '1.278'),
           ('Q2/26', 1231.1, (56, 189, 248), '1.231'),
           ('Q3/26', 1124.9, (34, 197, 94), '1.125')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Rủi ro của tích sản một mã',
  'label': '',
  'cap': ('RỦI RO', 'TÍCH SẢN MỘT MÃ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, rủi ro khi tích sản chỉ một mã. Kết quả của anh chị phụ thuộc hoàn toàn vào một doanh nghiệp và một ngành. Trong ba mươi bảy tháng qua, '
         'có lúc giá đầu tháng thấp hơn giá cao nhất khoảng bốn mươi chín phần trăm. Nếu giai đoạn đó trùng với lúc anh chị cần tiền, khoản tích sản sẽ phải '
         'bán lỗ. Vì vậy người tích sản thường chia cho nhiều mã ở nhiều ngành, hoặc góp vào quỹ chỉ số, và luôn giữ quỹ dự phòng riêng.',
  'anh': 'single basket eggs',
  'moc': True,
  'cards': [('Rủi ro tập trung', 'Một mã, một ngành', ''), ('Rủi ro thời điểm', 'Cần tiền lúc giá thấp', ''), ('Cách giảm', 'Nhiều mã, quỹ dự phòng', '')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Người tích sản nên làm gì',
  'label': '',
  'cap': ('NGƯỜI TÍCH SẢN', 'NÊN LÀM GÌ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, ba việc người tích sản nên làm. Một, góp đều vào nhiều mã hoặc quỹ chỉ số thay vì dồn một mã. Hai, mỗi quý ghi lại giá vốn, tỷ trọng và '
         'lợi nhuận doanh nghiệp, để biết mình đang sở hữu gì. Ba, khi giá vượt xa tốc độ tăng lợi nhuận, có thể giảm tốc góp vào mã đó và chuyển sang mã '
         'khác, thay vì dừng hẳn kế hoạch.',
  'anh': 'planning notebook',
  'items': [('Góp đều nhiều mã hoặc quỹ chỉ số', (34, 197, 94)),
            ('Ghi giá vốn, tỷ trọng mỗi quý', (34, 197, 94)),
            ('Giá vượt xa lợi nhuận: giảm tốc góp', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('GÓP ĐỀU 37 THÁNG', 'LÃI 3%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu tính trên giá đóng cửa đã điều chỉnh, chưa gồm phí và thuế, đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Nếu bắt đầu '
         'tích sản từ hôm nay, anh chị sẽ chia số tiền mỗi tháng cho mấy mã?'}]

S['K2_1211A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': '8 công ty chứng khoán – quý 3/2026',
  'cap': ('8 CTCK: PHÍ', 'GIẢM ĐẾN 76%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'stock trading screens',
  'chart': {'sym': 'SSIW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 27.98, 'Đỉnh tuần 2/3/26: 27,98', 0.6], [37, 17.34, 'Đáy tuần 27/7/26: 17,34', 1.6], [51, 20.4, 'Tuần 2/11/26: 20,40', 2.6]]},
  'say': 'Quý ba năm hai nghìn không trăm hai mươi sáu, doanh thu phí giao dịch của các công ty chứng khoán niêm yết giảm mạnh, có nơi giảm tới bảy mươi lăm '
         'phẩy chín phần trăm so với cùng kỳ. Lợi nhuận của tám công ty lớn đi theo những hướng rất khác nhau: TCX tăng bảy phẩy chín phần trăm, trong khi VIX '
         'giảm chín mươi hai phẩy chín phần trăm. Cùng một thị trường, cùng một quý, vì sao kết quả chênh lệch xa như vậy? Video này em so sánh lợi nhuận, '
         'định giá và nguồn thu của tám mã để anh chị thấy công ty nào phụ thuộc vào điều gì.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận quý 3 so với cùng kỳ',
  'label': '',
  'cap': ('LỢI NHUẬN QUÝ 3', 'SO VỚI CÙNG KỲ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận quý ba năm hai nghìn không trăm hai mươi sáu so với cùng kỳ. VIX lãi khoảng một trăm bảy mươi bốn tỷ, giảm chín mươi hai phẩy '
         'chín phần trăm. VND lãi khoảng ba trăm hai mươi chín tỷ, giảm sáu mươi bốn phẩy năm phần trăm. SHS lãi khoảng hai trăm linh ba tỷ, giảm năm mươi bảy '
         'phẩy năm phần trăm. FTS lãi khoảng ba mươi sáu tỷ, giảm ba mươi lăm phần trăm. HCM lãi khoảng hai trăm chín mươi bảy tỷ, giảm ba mươi hai phẩy năm '
         'phần trăm. SSI lãi khoảng một nghìn một trăm hai mươi lăm tỷ, giảm hai mươi ba phẩy bảy phần trăm. VCI lãi khoảng ba trăm sáu mươi bảy tỷ, giảm mười '
         'hai phẩy sáu phần trăm. TCX lãi khoảng một nghìn bảy trăm bốn mươi tám tỷ, tăng bảy phẩy chín phần trăm. Cùng một nhóm ngành, cùng một quý, nhưng '
         'kết quả chênh nhau rất xa. Đó là lý do không nên mua cả nhóm chỉ vì một mã báo lãi tốt.',
  'anh': 'comparison chart',
  'moc': True,
  'bars': [('VIX', 92.9, (239, 68, 68), '−92,9%'),
           ('VND', 64.5, (239, 68, 68), '−64,5%'),
           ('SHS', 57.5, (239, 68, 68), '−57,5%'),
           ('FTS', 35.0, (239, 68, 68), '−35,0%'),
           ('HCM', 32.5, (239, 68, 68), '−32,5%'),
           ('SSI', 23.7, (239, 68, 68), '−23,7%'),
           ('VCI', 12.6, (239, 68, 68), '−12,6%'),
           ('TCX', 7.9, (34, 197, 94), '+7,9%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Định giá cả nhóm',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, định giá. SSI có P trên B khoảng một phẩy năm mươi bảy lần, ROE khoảng mười hai phẩy hai phần trăm. VCI có P trên B khoảng một phẩy ba '
         'mươi bảy lần, ROE khoảng tám phẩy năm phần trăm. VND có P trên B khoảng một phẩy không năm lần, ROE khoảng chín phẩy chín phần trăm. HCM có P trên B '
         'khoảng hai phẩy hai mươi ba lần, ROE khoảng tám phẩy sáu phần trăm. VIX có P trên B khoảng một phẩy không năm lần, ROE khoảng sáu phẩy năm phần '
         'trăm. SHS có P trên B khoảng một phẩy không một lần, ROE khoảng năm phẩy chín phần trăm. FTS có P trên B khoảng một phẩy sáu mươi bảy lần, ROE '
         'khoảng chín phẩy một phần trăm. TCX có P trên B khoảng hai phẩy không bốn lần, ROE khoảng mười ba phẩy tám phần trăm. Nhìn P trên B cạnh ROE giúp '
         'anh chị thấy thị trường đang trả giá cao cho mã nào và mã đó có xứng đáng với hiệu quả vốn hay không.',
  'anh': 'calculator desk',
  'cards': [('TCX', 'P/B 2,04', 'ROE 13,8%'), ('SSI', 'P/B 1,57', 'ROE 12,2%'), ('VND', 'P/B 1,05', 'ROE 9,9%'), ('FTS', 'P/B 1,67', 'ROE 9,1%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Phí giao dịch giảm mạnh',
  'label': '',
  'cap': ('PHÍ GIAO DỊCH', 'GIẢM MẠNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, điểm chung của cả nhóm trong quý ba là doanh thu phí giao dịch giảm mạnh, từ khoảng ba mươi bảy phần trăm tới hơn bảy mươi phần trăm so '
         'với cùng kỳ, vì thanh khoản thị trường thấp hơn nhiều so với quý ba năm hai nghìn không trăm hai mươi lăm. Khi phí giao dịch giảm, lợi nhuận phụ '
         'thuộc nhiều hơn vào hai mảng còn lại: cho vay ký quỹ và tự doanh. Mảng tự doanh biến động theo thị trường, nên lợi nhuận cả nhóm dao động mạnh giữa '
         'các quý.',
  'anh': 'trading floor quiet',
  'moc': True,
  'cards': [('Phí giao dịch', '−37% đến −76%', 'so với cùng kỳ'),
            ('Cho vay ký quỹ', 'Đỡ lợi nhuận', 'VCI +50,5%, TCX +53,8%'),
            ('Tự doanh', 'Biến động mạnh', 'VIX lỗ tự doanh 88 tỷ')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, rủi ro cần theo dõi. Thứ nhất, cổ phiếu chứng khoán có độ nhạy cao với thanh khoản thị trường, thường tăng mạnh và giảm mạnh hơn chỉ số. '
         'Thứ hai, dư nợ cho vay ký quỹ tăng nhanh giúp lợi nhuận nhưng cũng làm tăng rủi ro khi thị trường giảm sâu. Thứ ba, lợi nhuận tự doanh không lặp lại '
         'đều đặn. Với nhóm ngành chu kỳ như vậy, tỷ trọng trong danh mục nên được giới hạn rõ ràng.',
  'anh': 'warning sign',
  'items': [('Nhạy với thanh khoản thị trường', (239, 68, 68)),
            ('Dư nợ ký quỹ tăng nhanh', (255, 196, 0)),
            ('Tự doanh không đều', (255, 196, 0)),
            ('Giới hạn tỷ trọng nhóm', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('8 CÔNG TY', 'CHỨNG KHOÁN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Khi thanh khoản thị trường thấp như hiện nay, anh chị ưu tiên công ty chứng khoán có cho vay ký quỹ mạnh hay có tự doanh ít rủi ro?'}]

S['K2_1311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': '7 mã bất động sản – quý 3/2026',
  'cap': ('VHM +453%', 'NLG −96,7%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'city skyline construction',
  'chart': {'sym': 'VHMW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[26, 83.44, 'Đỉnh tuần 11/5/26: 83,44', 0.6], [1, 41.84, 'Đáy tuần 10/11/25: 41,84', 1.6], [51, 62.1, 'Tuần 2/11/26: 62,10', 2.6]]},
  'say': 'Quý ba năm hai nghìn không trăm hai mươi sáu, lợi nhuận của nhóm bất động sản chia làm hai thái cực. VHM lãi khoảng hai mươi ba nghìn một trăm bốn '
         'mươi sáu tỷ, tăng bốn trăm năm mươi ba phẩy hai phần trăm so với cùng kỳ, KBC tăng một trăm chín mươi sáu phẩy sáu phần trăm. Ở chiều ngược lại, NLG '
         'giảm chín mươi sáu phẩy bảy phần trăm, DXG giảm tám mươi ba phẩy sáu phần trăm. Cùng một ngành, vì sao chênh lệch lớn như vậy, và thị trường đang '
         'định giá từng mã ra sao? Video này em so sánh bảy mã bất động sản nhà ở và khu công nghiệp.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận quý 3 so với cùng kỳ',
  'label': '',
  'cap': ('LỢI NHUẬN QUÝ 3', 'SO VỚI CÙNG KỲ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận quý ba năm hai nghìn không trăm hai mươi sáu so với cùng kỳ. NLG lãi khoảng năm tỷ, giảm chín mươi sáu phẩy bảy phần trăm. DXG '
         'lãi khoảng mười lăm tỷ, giảm tám mươi ba phẩy sáu phần trăm. IDC lãi khoảng bốn trăm chín mươi ba tỷ, giảm bốn mươi mốt phẩy năm phần trăm. KDH lãi '
         'khoảng một trăm bảy mươi sáu tỷ, giảm hai mươi lăm phẩy năm phần trăm. SZC lãi khoảng hai mươi hai tỷ, tăng ba phẩy tám phần trăm. KBC lãi khoảng '
         'chín trăm mười một tỷ, tăng một trăm chín mươi sáu phẩy sáu phần trăm. VHM lãi khoảng hai mươi ba nghìn một trăm bốn mươi sáu tỷ, tăng bốn trăm năm '
         'mươi ba phẩy hai phần trăm. Cùng một nhóm ngành, cùng một quý, nhưng kết quả chênh nhau rất xa. Đó là lý do không nên mua cả nhóm chỉ vì một mã báo '
         'lãi tốt.',
  'anh': 'comparison chart',
  'moc': True,
  'bars': [('NLG', 96.7, (239, 68, 68), '−96,7%'),
           ('DXG', 83.6, (239, 68, 68), '−83,6%'),
           ('IDC', 41.5, (239, 68, 68), '−41,5%'),
           ('KDH', 25.5, (239, 68, 68), '−25,5%'),
           ('SZC', 3.8, (34, 197, 94), '+3,8%'),
           ('KBC', 196.6, (34, 197, 94), '+196,6%'),
           ('VHM', 453.2, (34, 197, 94), '+453,2%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Định giá cả nhóm',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, định giá. VHM có P trên B khoảng một phẩy bảy mươi tám lần, ROE khoảng ba mươi sáu phẩy sáu phần trăm. KBC có P trên B khoảng không phẩy '
         'chín mươi tám lần, ROE khoảng sáu phẩy năm phần trăm. IDC có P trên B khoảng hai phẩy không một lần, ROE khoảng hai mươi phẩy chín phần trăm. NLG có '
         'P trên B khoảng không phẩy tám mươi tám lần, ROE khoảng bốn phẩy hai phần trăm. KDH có P trên B khoảng một lần, ROE khoảng tám phẩy hai phần trăm. '
         'DXG có P trên B khoảng không phẩy chín mươi bảy lần, ROE khoảng không phẩy sáu phần trăm. SZC có P trên B khoảng một phẩy hai lần, ROE khoảng năm '
         'phẩy một phần trăm. Nhìn P trên B cạnh ROE giúp anh chị thấy thị trường đang trả giá cao cho mã nào và mã đó có xứng đáng với hiệu quả vốn hay '
         'không.',
  'anh': 'calculator desk',
  'cards': [('VHM', 'P/B 1,78', 'ROE 36,6%'), ('IDC', 'P/B 2,01', 'ROE 20,9%'), ('KDH', 'P/B 1,00', 'ROE 8,2%'), ('KBC', 'P/B 0,98', 'ROE 6,5%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Lợi nhuận theo đợt bàn giao',
  'label': '',
  'cap': ('LỢI NHUẬN', 'THEO ĐỢT BÀN GIAO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, vì sao lợi nhuận bất động sản thất thường. Doanh nghiệp bất động sản chỉ ghi nhận doanh thu khi bàn giao nhà hoặc đất, nên lợi nhuận dồn '
         'vào những quý có dự án bàn giao. KBC có quý hai năm hai nghìn không trăm hai mươi sáu lãi khoảng bảy tỷ, rồi quý ba lãi khoảng chín trăm mười một '
         'tỷ. KDH có doanh thu quý ba chỉ khoảng bốn mươi mốt tỷ. Vì vậy với nhóm này, anh chị nên xem lũy kế cả năm và nguồn hàng sắp bàn giao, thay vì một '
         'quý.',
  'anh': 'construction site',
  'moc': True,
  'cards': [('KBC quý 2 → quý 3', '≈ 7 → 911 tỷ', 'ghi nhận theo đợt'),
            ('KDH doanh thu quý 3', '≈ 41 tỷ', 'giảm 96,2%'),
            ('Nên xem', 'Lũy kế, người mua trả trước', 'và hàng tồn kho')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, rủi ro cần theo dõi. Thứ nhất là nợ vay và chi phí lãi vay, nhiều doanh nghiệp trong nhóm có chi phí lãi vay tăng mạnh. Thứ hai là pháp '
         'lý dự án, quyết định tiến độ bàn giao. Thứ ba là dòng tiền kinh doanh, vì lợi nhuận kế toán có thể dương trong khi tiền mặt vẫn âm. Thứ tư, P trên B '
         'thấp ở nhóm này thường phản ánh rủi ro về giá trị hàng tồn kho, không phải lúc nào cũng là rẻ.',
  'anh': 'legal documents',
  'items': [('Nợ vay, chi phí lãi vay', (239, 68, 68)),
            ('Pháp lý, tiến độ bàn giao', (255, 196, 0)),
            ('Dòng tiền kinh doanh', (255, 196, 0)),
            ('P/B thấp chưa chắc rẻ', (239, 68, 68))]},
 {'k': 'end',
  'label': '',
  'cap': ('7 MÃ BẤT ĐỘNG SẢN', 'AI BỀN NHẤT?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Với cổ phiếu bất động sản, anh chị nhìn vào lợi nhuận quý, nguồn hàng bàn giao hay sức khỏe nợ vay trước tiên?'}]

S['LST_1211A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Thứ Năm Bạc – 27/3/1980',
  'cap': ('BẠC 6 USD', 'LÊN 50 USD?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'silver bars',
  'say': 'Đầu năm một nghìn chín trăm bảy mươi chín, một ounce bạc có giá khoảng sáu đô la Mỹ. Tháng một năm một nghìn chín trăm tám mươi, giá vọt lên gần năm '
         'mươi đô la Mỹ. Hai tháng sau, ngày hai mươi bảy tháng ba năm một nghìn chín trăm tám mươi, giá rơi xuống khoảng mười phẩy tám đô la Mỹ và cả Phố '
         'Wall run rẩy. Đứng giữa câu chuyện là anh em nhà Hunt, từng được xem là gia đình giàu nhất nước Mỹ. Video này em kể vì sao người giàu nhất cũng có '
         'thể sụp đổ, chỉ vì một thứ: mua bằng tiền vay.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Gia đình giàu nhất nước Mỹ',
  'label': '',
  'cap': ('GIA ĐÌNH', 'GIÀU NHẤT MỸ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một. Cha của họ, H. L. Hunt, làm giàu từ dầu mỏ ở bang Texas. Hai người con, Nelson Bunker Hunt và William Herbert Hunt, thừa kế tài sản '
         'khổng lồ. Thập niên một nghìn chín trăm bảy mươi, nước Mỹ chịu lạm phát cao, đồng đô la mất giá. Anh em Hunt tin rằng tiền giấy sẽ còn mất giá nữa, '
         'và bạc là nơi giữ giá trị tốt nhất. Niềm tin đó không vô lý. Cái sai nằm ở cách họ đặt cược.',
  'anh': 'Texas oil field',
  'moc': True,
  'cards': [('Gốc tài sản', 'Dầu mỏ Texas', 'H. L. Hunt'), ('Thập niên 1970', 'Lạm phát cao', 'đô la mất giá'), ('Niềm tin', 'Bạc giữ giá trị', '')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Gom bạc bằng tiền vay',
  'label': '',
  'cap': ('GOM BẠC', 'BẰNG TIỀN VAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai. Từ năm một nghìn chín trăm bảy mươi chín, anh em Hunt cùng một số nhà đầu tư Trung Đông mua vào lượng bạc và hợp đồng bạc rất lớn, phần '
         'lớn bằng tiền vay ký quỹ. Theo các ước tính được trích dẫn nhiều, có thời điểm nhóm này nắm giữ khoảng một phần ba lượng bạc giao dịch được trên thế '
         'giới. Giá càng tăng, tài sản thế chấp càng lớn, họ càng vay thêm để mua tiếp. Đó là một vòng xoáy đi lên, và mọi vòng xoáy bằng tiền vay đều có '
         'chiều ngược lại.',
  'anh': 'commodity trading floor',
  'cards': [('Cách mua', 'Vay ký quỹ', 'mua hợp đồng và bạc thật'),
            ('Quy mô', '≈ 1/3 bạc thế giới', 'ước tính'),
            ('Giá 1/1980', '≈ 50 USD/ounce', 'từ ≈ 6 USD đầu 1979')]},
 {'k': 'checklist',
  'ch': 'Chương 3 – Luật chơi thay đổi',
  'label': '',
  'cap': ('LUẬT CHƠI', 'THAY ĐỔI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, luật chơi thay đổi. Ngày bảy tháng một năm một nghìn chín trăm tám mươi, sàn hàng hóa COMEX ban hành quy định giới hạn mua bạc bằng tiền '
         'vay. Cục Dự trữ Liên bang cũng siết tín dụng cho hoạt động đầu cơ hàng hóa. Khi không thể vay thêm, người mua mới biến mất, và giá bắt đầu trượt. '
         'Với người dùng đòn bẩy, giá không cần về số không. Chỉ cần giảm đủ sâu là lệnh gọi ký quỹ sẽ đến.',
  'anh': 'trading rules document',
  'items': [('7/1/1980: COMEX hạn chế mua bằng ký quỹ', (255, 196, 0)),
            ('Fed siết tín dụng đầu cơ', (255, 196, 0)),
            ('Người mua mới biến mất', (239, 68, 68)),
            ('Giá trượt, gọi ký quỹ', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 4 – Thứ Năm Bạc',
  'label': '',
  'cap': ('THỨ NĂM', 'BẠC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, ngày Thứ Năm Bạc. Ngày hai mươi bảy tháng ba năm một nghìn chín trăm tám mươi, anh em Hunt không đáp ứng được lệnh gọi ký quỹ khoảng một '
         'trăm triệu đô la Mỹ. Giá bạc rơi xuống khoảng mười phẩy tám đô la Mỹ một ounce, giảm hơn năm mươi phần trăm chỉ trong vài ngày. Nỗi lo lan sang cổ '
         'phiếu các công ty chứng khoán đã cho họ vay. Để tránh đổ vỡ dây chuyền, một nhóm ngân hàng phải thu xếp khoản vay khoảng một phẩy một tỷ đô la Mỹ '
         'cho gia đình Hunt.',
  'anh': 'stock exchange panic',
  'moc': True,
  'cards': [('27/3/1980', '≈ 10,8 USD/ounce', 'giảm hơn 50% trong vài ngày'),
            ('Lệnh gọi ký quỹ', '≈ 100 triệu USD', 'không đáp ứng được'),
            ('Giải cứu', '≈ 1,1 tỷ USD', 'nhóm ngân hàng cho vay')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Bài học cho hôm nay',
  'label': '',
  'cap': ('BỐN BÀI HỌC', 'TỪ NHÀ HUNT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, bài học cho hôm nay. Năm một nghìn chín trăm tám mươi tám, anh em Hunt nộp đơn phá sản cá nhân. Bài học thứ nhất: đúng về xu hướng chưa '
         'đủ, vì đòn bẩy có thể buộc mình bán trước khi xu hướng kịp đến. Thứ hai: khi một tài sản tăng chủ yếu nhờ tiền vay, chỉ cần siết tín dụng là giá đảo '
         'chiều. Thứ ba: không ai đủ lớn để chống lại luật chơi. Thứ tư: tiền vay biến một khoản lỗ tạm thời thành khoản lỗ vĩnh viễn.',
  'anh': 'lesson notebook',
  'items': [('Đúng xu hướng vẫn có thể thua vì vay', (239, 68, 68)),
            ('Siết tín dụng là giá đảo chiều', (255, 196, 0)),
            ('Không ai lớn hơn luật chơi', (255, 196, 0)),
            ('Vay biến lỗ tạm thành lỗ thật', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 6 – Ở thị trường Việt Nam',
  'label': '',
  'cap': ('Ở VIỆT NAM', 'THÌ SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, liên hệ với Việt Nam. Trên sàn HOSE, giá một cổ phiếu có thể giảm tối đa bảy phần trăm mỗi phiên. Với tỷ lệ vay ký quỹ một đồng vốn một '
         'đồng vay, ba phiên giảm sàn liên tiếp có thể làm tài khoản mất gần bốn mươi phần trăm vốn tự có và chạm ngưỡng bị bán giải chấp. Những đợt bán giải '
         'chấp lại kéo giá xuống thêm, giống hệt vòng xoáy của bạc năm một nghìn chín trăm tám mươi, chỉ ở quy mô nhỏ hơn.',
  'anh': 'Vietnam stock board',
  'cards': [('Biên độ HOSE', '±7%/phiên', ''), ('Vay 1:1, 3 phiên sàn', '≈ −39% vốn tự có', 'chưa tính lãi vay'), ('Hệ quả', 'Bán giải chấp dây chuyền', '')]},
 {'k': 'end',
  'label': '',
  'cap': ('BẠC −50%', 'TRONG VÀI NGÀY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Anh em Hunt có thể đúng về lạm phát, nhưng tiền vay không cho họ thời gian để đúng. Trong tài khoản của anh chị lúc này, nếu thị trường giảm hai '
         'mươi phần trăm thì có lệnh gọi ký quỹ nào đang chờ không?'}]

S['LST_1311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Archegos – 3/2021',
  'cap': ('MẤT 20 TỶ USD', 'TRONG 2 NGÀY?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'New York skyline night',
  'say': 'Cuối tháng ba năm hai nghìn không trăm hai mươi mốt, một quỹ đầu tư gia đình ít người biết tên ở New York mất khoảng hai mươi tỷ đô la Mỹ chỉ trong '
         'vài ngày. Các ngân hàng lớn nhất thế giới cho quỹ này vay cũng mất tổng cộng hơn mười tỷ đô la Mỹ. Quỹ đó là Archegos Capital của Bill Hwang. Điều '
         'đáng sợ là trước đó gần như không ai biết quỹ này nắm giữ bao nhiêu cổ phiếu. Video này em kể vì sao đòn bẩy giấu kín là quả bom hẹn giờ.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Quỹ gia đình kín tiếng',
  'label': '',
  'cap': ('QUỸ GIA ĐÌNH', 'KÍN TIẾNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một. Bill Hwang từng quản lý quỹ phòng hộ và gặp rắc rối pháp lý năm hai nghìn không trăm mười hai. Sau đó ông lập Archegos dưới dạng văn '
         'phòng quản lý tài sản gia đình, nên không phải công bố danh mục như một quỹ thông thường. Theo hồ sơ vụ án, vốn của Archegos tăng từ khoảng một phẩy '
         'năm tỷ đô la Mỹ đầu năm hai nghìn không trăm hai mươi lên khoảng ba mươi sáu tỷ đô la Mỹ đầu năm hai nghìn không trăm hai mươi mốt. Tốc độ tăng đó '
         'không đến từ thiên tài, mà đến từ đòn bẩy.',
  'anh': 'private office building',
  'moc': True,
  'cards': [('Hình thức', 'Văn phòng gia đình', 'ít phải công bố'), ('Đầu 2020', '≈ 1,5 tỷ USD', 'vốn'), ('Đầu 2021', '≈ 36 tỷ USD', 'vốn, nhờ đòn bẩy')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Đòn bẩy giấu kín',
  'label': '',
  'cap': ('ĐÒN BẨY', 'GIẤU KÍN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, đòn bẩy giấu kín. Archegos không mua trực tiếp nhiều cổ phiếu mà dùng hợp đồng hoán đổi lợi nhuận với nhiều ngân hàng. Ngân hàng đứng '
         'tên cổ phiếu, Archegos hưởng lãi lỗ. Vì dùng nhiều ngân hàng cùng lúc, mỗi ngân hàng chỉ thấy một phần, không ai thấy tổng. Theo các báo cáo sau vụ '
         'việc, tổng giá trị cổ phiếu Archegos nắm gián tiếp có lúc vượt một trăm tỷ đô la Mỹ, tập trung vào vài mã như ViacomCBS.',
  'anh': 'contract papers',
  'cards': [('Công cụ', 'Hợp đồng hoán đổi', 'ngân hàng đứng tên'),
            ('Tổng vị thế', '> 100 tỷ USD', 'ước tính sau vụ việc'),
            ('Danh mục', 'Tập trung vài mã', 'ViacomCBS, Discovery...')]},
 {'k': 'checklist',
  'ch': 'Chương 3 – Một tuần sụp đổ',
  'label': '',
  'cap': ('MỘT TUẦN', 'SỤP ĐỔ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, một tuần sụp đổ. Ngày hai mươi hai tháng ba năm hai nghìn không trăm hai mươi mốt, ViacomCBS công bố phát hành thêm cổ phiếu để huy động '
         'khoảng ba tỷ đô la Mỹ. Giá giảm mạnh trong các phiên sau. Với đòn bẩy rất cao, Archegos không đủ tiền ký quỹ bổ sung. Ngày hai mươi sáu tháng ba, '
         'các ngân hàng đồng loạt bán khối lượng lớn cổ phiếu để thu hồi tiền. Ngân hàng nào bán trước thì lỗ ít, ngân hàng bán sau lỗ nặng.',
  'anh': 'falling stock chart',
  'items': [('22/3: ViacomCBS phát hành thêm ≈ 3 tỷ USD', (255, 196, 0)),
            ('Giá giảm mạnh, gọi ký quỹ', (239, 68, 68)),
            ('26/3: ngân hàng bán khối lớn', (239, 68, 68)),
            ('Ai bán sau lỗ nặng hơn', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 4 – Ai chịu thiệt',
  'label': '',
  'cap': ('AI CHỊU', 'THIỆT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, ai chịu thiệt. Credit Suisse lỗ khoảng năm phẩy năm tỷ đô la Mỹ, Nomura khoảng hai phẩy chín tỷ đô la Mỹ, cùng nhiều ngân hàng khác. Với '
         'Credit Suisse, cú sốc này cộng thêm các vấn đề khác góp phần dẫn tới việc ngân hàng này bị UBS mua lại năm hai nghìn không trăm hai mươi ba. Bill '
         'Hwang bị truy tố, và năm hai nghìn không trăm hai mươi bốn bị tuyên án mười tám năm tù. Cổ đông các công ty liên quan cũng chịu những phiên giảm '
         'mạnh không liên quan gì tới kết quả kinh doanh.',
  'anh': 'bank headquarters',
  'moc': True,
  'cards': [('Credit Suisse', '≈ 5,5 tỷ USD', 'lỗ'), ('Nomura', '≈ 2,9 tỷ USD', 'lỗ'), ('Bill Hwang', '18 năm tù', 'tuyên án 2024')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Bài học quản trị rủi ro',
  'label': '',
  'cap': ('BỐN BÀI HỌC', 'TỪ ARCHEGOS'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, bài học quản trị rủi ro. Một, tập trung cộng đòn bẩy là công thức tăng nhanh nhất và mất nhanh nhất. Hai, khi một mã bị một người hoặc '
         'nhóm nhỏ nắm quá nhiều, giá có thể bị đẩy lên vượt xa giá trị, và rơi rất nhanh khi họ phải bán. Ba, thanh khoản biến mất đúng lúc mình cần bán. '
         'Bốn, người bán sau trong một đợt bán tháo luôn chịu giá tệ nhất.',
  'anh': 'risk dashboard',
  'items': [('Tập trung + đòn bẩy = mất nhanh', (239, 68, 68)),
            ('Coi chừng mã bị nắm giữ tập trung', (255, 196, 0)),
            ('Thanh khoản biến mất khi cần', (239, 68, 68)),
            ('Bán sau chịu giá tệ nhất', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 6 – Liên hệ Việt Nam',
  'label': '',
  'cap': ('LIÊN HỆ', 'VIỆT NAM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, liên hệ Việt Nam. Ở thị trường mình, anh chị nên cảnh giác với những cổ phiếu tăng mạnh liên tục mà thanh khoản thấp, cổ đông lớn cầm cố '
         'cổ phiếu để vay, hoặc giá tăng vượt xa lợi nhuận. Đây là những nơi đòn bẩy có thể đang ẩn bên dưới. Khi một mắt xích phải bán, giá có thể giảm sàn '
         'nhiều phiên liên tiếp mà người ngoài không kịp thoát.',
  'anh': 'Ho Chi Minh City skyline',
  'cards': [('Dấu hiệu 1', 'Tăng mạnh, thanh khoản thấp', ''),
            ('Dấu hiệu 2', 'Cổ đông lớn cầm cố', 'cổ phiếu để vay'),
            ('Dấu hiệu 3', 'Giá vượt xa lợi nhuận', '')]},
 {'k': 'end',
  'label': '',
  'cap': ('ĐÒN BẨY', 'GIẤU KÍN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Archegos cho thấy đòn bẩy nguy hiểm nhất là thứ không ai nhìn thấy cho tới phút cuối. Trong danh mục của anh chị, có mã nào đang tăng mạnh mà anh '
         'chị chưa biết ai đang nắm giữ phần lớn cổ phiếu?'}]

S['Y3_1211A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Fed – lãi suất điều hành',
  'cap': ('FED GIỮ 4%', '2 PHIẾU MUỐN TĂNG?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'Federal Reserve building',
  'say': 'Ngày hai mươi chín tháng mười năm hai nghìn không trăm hai mươi sáu theo giờ Việt Nam, Cục Dự trữ Liên bang Mỹ giữ nguyên lãi suất điều hành ở ba '
         'phẩy bảy mươi lăm đến bốn phần trăm, nhưng có hai trong mười hai thành viên bỏ phiếu muốn tăng thêm không phẩy hai mươi lăm điểm phần trăm. Trước '
         'đó, tháng chín năm hai nghìn không trăm hai mươi sáu, Fed đã tăng lãi suất không phẩy hai mươi lăm điểm phần trăm sau một chuỗi giảm. Cuộc họp tiếp '
         'theo là ngày tám và chín tháng mười hai. Video này em giải thích lãi suất Mỹ ảnh hưởng tới cổ phiếu Việt Nam qua những kênh nào.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Đường đi của lãi suất Fed',
  'label': '',
  'cap': ('LÃI SUẤT FED', 'MỨC TRẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, đường đi của lãi suất Fed. Biên trên lãi suất điều hành từng ở năm phẩy năm phần trăm, rồi Fed giảm dần qua nhiều đợt xuống ba phẩy bảy '
         'mươi lăm phần trăm, trước khi tăng trở lại lên bốn phần trăm vào tháng chín năm hai nghìn không trăm hai mươi sáu. Việc đảo chiều từ giảm sang tăng '
         'là tín hiệu Fed lo lạm phát quay lại. Hai phiếu muốn tăng tiếp trong cuộc họp tháng mười cho thấy khả năng thắt chặt thêm vẫn còn.',
  'anh': 'interest rate chart',
  'moc': True,
  'bars': [('11/23', 5.5, (56, 189, 248), '5,50%'),
           ('09/24', 5.0, (56, 189, 248), '5,00%'),
           ('11/24', 4.75, (56, 189, 248), '4,75%'),
           ('12/24', 4.5, (56, 189, 248), '4,50%'),
           ('09/25', 4.25, (56, 189, 248), '4,25%'),
           ('10/25', 4.0, (56, 189, 248), '4,00%'),
           ('12/25', 3.75, (56, 189, 248), '3,75%'),
           ('09/26', 4.0, (239, 68, 68), '4,00%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Kênh tỷ giá',
  'label': '',
  'cap': ('KÊNH 1', 'TỶ GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, kênh thứ nhất là tỷ giá. Khi lãi suất đô la cao hoặc có xu hướng tăng, đồng đô la thường mạnh lên. Áp lực tỷ giá với đồng Việt Nam tăng, '
         'Ngân hàng Nhà nước có ít dư địa hạ lãi suất trong nước hơn. Doanh nghiệp vay nợ bằng đô la và doanh nghiệp nhập khẩu nguyên liệu chịu chi phí cao '
         'hơn, còn doanh nghiệp xuất khẩu có thể được lợi một phần.',
  'anh': 'currency exchange',
  'cards': [('Đô la mạnh lên', 'Áp lực tỷ giá', ''),
            ('Lãi suất trong nước', 'Ít dư địa giảm', ''),
            ('Ai chịu', 'Nợ USD, nhập khẩu', 'xuất khẩu lợi một phần')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Kênh dòng vốn ngoại',
  'label': '',
  'cap': ('KÊNH 2', 'DÒNG VỐN NGOẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, kênh thứ hai là dòng vốn ngoại. Khi gửi tiền hoặc mua trái phiếu ở Mỹ đã cho lợi suất cao, một phần nhà đầu tư toàn cầu rút bớt khỏi các '
         'thị trường mới nổi để giảm rủi ro. Việt Nam không phải ngoại lệ. Nhóm cổ phiếu vốn hóa lớn, nơi nhà đầu tư nước ngoài nắm nhiều, thường chịu áp lực '
         'bán ròng rõ nhất trong những giai đoạn này.',
  'anh': 'global money flow',
  'cards': [('Lợi suất Mỹ cao', 'Giữ tiền ở Mỹ hấp dẫn', ''), ('Thị trường mới nổi', 'Bị bán bớt', ''), ('Chịu rõ nhất', 'Vốn hóa lớn, sở hữu ngoại cao', '')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Kênh định giá',
  'label': '',
  'cap': ('KÊNH 3', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, kênh thứ ba là định giá. Lãi suất là giá của thời gian. Khi lãi suất cao lên, một đồng lợi nhuận trong tương lai đáng giá ít hơn hôm '
         'nay, nên nhóm cổ phiếu được định giá dựa nhiều vào tăng trưởng xa thường giảm mạnh hơn. Doanh nghiệp có lợi nhuận đều, nợ thấp và trả cổ tức tiền '
         'mặt thường chống chịu tốt hơn trong giai đoạn lãi suất đi lên.',
  'anh': 'hourglass money',
  'moc': True,
  'cards': [('Lãi suất tăng', 'Lợi nhuận tương lai rẻ đi', ''),
            ('Chịu nhiều', 'Cổ phiếu tăng trưởng xa', ''),
            ('Chống chịu tốt', 'Lợi nhuận đều, nợ thấp', '')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Nhà đầu tư chuẩn bị gì',
  'label': '',
  'cap': ('CHUẨN BỊ', 'THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, nhà đầu tư chuẩn bị gì trước cuộc họp tháng mười hai. Một, kiểm tra tỷ lệ vay ký quỹ, vì lãi suất cao kéo dài làm chi phí vay đắt hơn. '
         'Hai, xem trong danh mục có bao nhiêu doanh nghiệp nợ đô la hoặc nhập khẩu nhiều. Ba, giữ một phần tiền mặt để không bị động nếu thị trường biến '
         'động. Bốn, không dự đoán quyết định của Fed, mà chuẩn bị cho cả hai kịch bản tăng và giữ nguyên.',
  'anh': 'planning desk',
  'items': [('Kiểm tra tỷ lệ vay ký quỹ', (239, 68, 68)),
            ('Doanh nghiệp nợ USD, nhập khẩu', (255, 196, 0)),
            ('Giữ một phần tiền mặt', (34, 197, 94)),
            ('Chuẩn bị cả hai kịch bản', (34, 197, 94))]},
 {'k': 'cards',
  'ch': 'Chương 6 – Nhìn lại năm 2022',
  'label': '',
  'cap': ('NHÌN LẠI', 'NĂM 2022'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, nhìn lại năm hai nghìn không trăm hai mươi hai để thấy tác động thật. Trong năm đó, Fed nâng lãi suất từ gần không phần trăm lên bốn '
         'phẩy hai mươi lăm đến bốn phẩy năm phần trăm, một trong những chu kỳ tăng nhanh nhất nhiều thập kỷ. Đồng đô la mạnh lên, tỷ giá trong nước chịu áp '
         'lực, lãi suất huy động trong nước tăng, và VN-Index giảm khoảng ba mươi ba phần trăm trong cả năm. Đợt tăng không phẩy hai mươi lăm điểm phần trăm '
         'năm hai nghìn không trăm hai mươi sáu nhỏ hơn rất nhiều, nhưng cơ chế lan truyền vẫn đi qua đúng những kênh đó.',
  'anh': '2022 calendar',
  'cards': [('Fed 2022', '≈ 0% → 4,25–4,5%', 'tăng nhanh'), ('VN-Index 2022', '≈ −33%', 'cả năm'), ('Năm 2026', '+0,25 điểm %', 'nhỏ hơn nhiều')]},
 {'k': 'end',
  'label': '',
  'cap': ('FED 3,75–4%', 'HỌP 8–9/12'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nguồn số liệu: thông báo của Cục Dự trữ Liên bang Mỹ ngày hai mươi chín tháng mười năm hai nghìn không trăm hai mươi sáu theo giờ Việt Nam. Nếu '
         'tháng mười hai Fed tăng thêm không phẩy hai mươi lăm điểm phần trăm, anh chị sẽ điều chỉnh danh mục ở chỗ nào trước tiên?'}]

S['Y3_1311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Vàng – tuần đầu 11/2026',
  'cap': ('VÀNG 4.079 USD', 'CHỨNG KHOÁN −4%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'gold bars',
  'say': 'Phiên ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, chỉ số S&P năm trăm giảm bốn phẩy ba mươi sáu phần trăm, Nasdaq giảm năm phẩy '
         'năm mươi hai phần trăm, còn giá vàng tăng không phẩy chín mươi chín phần trăm lên khoảng bốn nghìn một trăm mười ba đô la Mỹ một ounce. Hôm sau, chỉ '
         'số Nikkei của Nhật giảm năm phẩy chín mươi sáu phần trăm. Tới phiên sáu tháng mười một, vàng ở khoảng bốn nghìn không trăm bảy mươi chín đô la Mỹ. '
         'Khi chứng khoán thế giới rung lắc mạnh, vàng thường được nhắc tới như nơi trú ẩn. Video này em xem vàng thực sự đóng vai trò gì trong một danh mục '
         'được quản trị rủi ro.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Một tuần hai chiều',
  'label': '',
  'cap': ('MỘT TUẦN', 'HAI CHIỀU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, một tuần hai chiều. Giá vàng phiên hai tháng mười một khoảng ba nghìn chín trăm bảy mươi đô la Mỹ, phiên ba tháng mười một khoảng ba '
         'nghìn chín trăm bốn mươi đô la Mỹ, phiên bốn tháng mười một tăng ba phẩy ba mươi bảy phần trăm lên khoảng bốn nghìn không trăm bảy mươi ba đô la Mỹ, '
         'phiên năm tháng mười một khoảng bốn nghìn một trăm mười ba đô la Mỹ, và phiên sáu tháng mười một khoảng bốn nghìn không trăm bảy mươi chín đô la Mỹ. '
         'Trong cùng tuần, chứng khoán Mỹ có phiên tăng một phẩy năm mươi tám phần trăm và có phiên giảm bốn phẩy ba mươi sáu phần trăm. Vàng cũng biến động, '
         'nhưng thường không cùng chiều với cổ phiếu trong những ngày hoảng loạn.',
  'anh': 'gold price chart',
  'moc': True,
  'bars': [('2/11', 3969.6, (56, 189, 248), '3.970'),
           ('3/11', 3940.4, (56, 189, 248), '3.940'),
           ('4/11', 4073.0, (56, 189, 248), '4.073'),
           ('5/11', 4113.5, (34, 197, 94), '4.114'),
           ('6/11', 4079.5, (255, 196, 0), '4.080')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Vì sao vàng tăng khi cổ phiếu giảm',
  'label': '',
  'cap': ('VÌ SAO', 'NGƯỢC CHIỀU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, vì sao vàng thường đi ngược cổ phiếu trong lúc căng thẳng. Vàng không phụ thuộc vào lợi nhuận của một doanh nghiệp nào, cũng không thể '
         'vỡ nợ. Khi nhà đầu tư lo ngại rủi ro, một phần tiền rời cổ phiếu và tìm tới tài sản được xem là an toàn. Các ngân hàng trung ương nhiều nước cũng '
         'mua vàng để đa dạng dự trữ ngoài đồng đô la.',
  'anh': 'central bank vault',
  'cards': [('Không vỡ nợ', 'Không phụ thuộc lợi nhuận', ''),
            ('Lúc hoảng loạn', 'Tiền tìm nơi trú ẩn', ''),
            ('Ngân hàng trung ương', 'Mua để đa dạng dự trữ', '')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Mặt trái của vàng',
  'label': '',
  'cap': ('MẶT TRÁI', 'CỦA VÀNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, mặt trái của vàng. Vàng không trả cổ tức, không trả lãi. Khi lãi suất thực cao, giữ vàng có chi phí cơ hội lớn. Lịch sử cũng có những '
         'giai đoạn vàng giảm sâu và đi ngang rất lâu, ví dụ sau đỉnh năm một nghìn chín trăm tám mươi, phải hơn hai mươi năm sau giá vàng danh nghĩa mới vượt '
         'lại đỉnh cũ. Vì vậy vàng phù hợp làm phần phòng thủ, không phù hợp làm toàn bộ danh mục.',
  'anh': 'old gold coins',
  'moc': True,
  'cards': [('Không dòng tiền', 'Không cổ tức, không lãi', ''),
            ('Lãi suất thực cao', 'Chi phí cơ hội lớn', ''),
            ('Sau đỉnh 1980', '> 20 năm', 'mới vượt lại đỉnh danh nghĩa')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Vàng ở Việt Nam',
  'label': '',
  'cap': ('VÀNG', 'Ở VIỆT NAM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, vàng ở Việt Nam có điểm riêng. Giá vàng miếng trong nước nhiều lúc chênh khá xa giá thế giới quy đổi, và chênh lệch giữa giá mua với giá '
         'bán có thể lớn. Người mua vàng để phòng thủ cần tính cả hai khoản chênh này. Vàng nhẫn thường có chênh lệch thấp hơn vàng miếng, nhưng vẫn cần so '
         'sánh giá giữa các nơi bán trước khi mua.',
  'anh': 'gold shop',
  'cards': [('Chênh với thế giới', 'Có lúc rất lớn', ''), ('Chênh mua – bán', 'Cần tính trước', ''), ('Vàng nhẫn', 'Chênh thường thấp hơn', '')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Vàng trong danh mục',
  'label': '',
  'cap': ('VÀNG TRONG', 'DANH MỤC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, đặt vàng vào danh mục thế nào. Một, xác định vai trò: vàng là phần bảo hiểm, giúp danh mục bớt giảm khi cổ phiếu giảm mạnh. Hai, giữ tỷ '
         'trọng vừa phải, nhiều người chọn khoảng năm đến mười phần trăm. Ba, tái cân bằng định kỳ: khi vàng tăng mạnh vượt tỷ trọng thì bán bớt, khi giảm sâu '
         'thì mua bù. Bốn, không mua vàng bằng tiền vay hay tiền cần dùng gấp.',
  'anh': 'portfolio pie chart',
  'items': [('Vai trò: bảo hiểm danh mục', (34, 197, 94)),
            ('Tỷ trọng vừa phải, 5–10%', (255, 196, 0)),
            ('Tái cân bằng định kỳ', (34, 197, 94)),
            ('Không mua bằng tiền vay', (239, 68, 68))]},
 {'k': 'end',
  'label': '',
  'cap': ('VÀNG ≈ 4.079 USD', 'BẢO HIỂM HAY ĐẦU CƠ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nguồn số liệu: giá đóng cửa vàng và chỉ số chứng khoán thế giới phiên hai đến sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Trong danh '
         'mục của anh chị, vàng đang là phần bảo hiểm hay là một khoản đầu cơ?'}]

