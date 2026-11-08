# -*- coding: utf-8 -*-
# VIDEO DÀI – NV1 soạn 8/11/2026 (lô 20261109_0040_kp: HI1611A, HI1711A, Y2_1611A, Y2_1711A, TS1611A, TS1711A, K2_1611A, K2_1711A, LST_1611A, LST_1711A, Y3_1611A, Y3_1711A). Kênh phụ 16–17/11. Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['HI1611A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'NLG – định giá nhanh',
  'cap': ('NLG P/E 18,0', 'ROE 4,2%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nam Long, mã NLG, đang giao dịch quanh hai mươi hai phẩy chín mươi lăm nghìn đồng, P trên E khoảng mười tám phẩy không bốn lần, P trên B khoảng '
         'không phẩy tám mươi tám lần, ROE khoảng bốn phẩy hai phần trăm. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt năm '
         'tỷ, giảm chín mươi sáu phẩy bảy phần trăm so với cùng kỳ. Rẻ thật, đắt thật, hay thị trường đang nhìn thấy điều gì khác? Video này em đặt ba con số '
         'định giá cạnh chuỗi lợi nhuận tám quý, cạnh mặt bằng của ngành và cạnh rủi ro, để anh chị tự trả lời. Số liệu từ báo cáo quý ba năm hai nghìn không '
         'trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'residential buildings Vietnam',
  'chart': {'sym': 'NLGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 39.0, 'Đỉnh tuần 3/11/25: 39,00', 0.6], [37, 19.15, 'Đáy tuần 27/7/26: 19,15', 1.6], [51, 22.95, 'Tuần 2/11/26: 22,95', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Ba con số định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, ba con số định giá nghĩa là gì với NLG. P trên E mười tám phẩy không bốn lần nghĩa là với lợi nhuận mỗi cổ phiếu bốn quý gần nhất khoảng '
         'một nghìn hai trăm bảy mươi hai đồng, người mua đang trả khoảng mười tám phẩy không bốn đồng giá cho mỗi đồng lợi nhuận. Nói cách khác, nếu lợi '
         'nhuận đứng yên, phải khoảng mười tám năm lợi nhuận mới bằng giá mua. P trên B không phẩy tám mươi tám lần nghĩa là giá đang gấp không phẩy tám mươi '
         'tám lần giá trị sổ sách mỗi cổ phiếu, khoảng hai mươi sáu nghìn một trăm tám mươi hai đồng. ROE bốn phẩy hai phần trăm cho biết mỗi một trăm đồng '
         'vốn chủ sở hữu tạo ra khoảng bốn phẩy hai đồng lợi nhuận một năm. Ba con số này liên kết với nhau: P trên E nhân ROE xấp xỉ bằng P trên B.',
  'moc': True,
  'anh': 'calculator',
  'cards': [('P/E', '18,04', 'lần'), ('P/B', '0,88', 'lần'), ('ROE', '4,2%', 'năm')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lợi nhuận tám quý, gốc của chữ E trong P trên E. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn '
         'không trăm hai mươi sáu, lợi nhuận sau thuế công ty mẹ cao nhất ở quý bốn năm hai nghìn không trăm hai mươi bốn với khoảng năm trăm linh hai tỷ, '
         'thấp nhất ở quý ba năm hai nghìn không trăm hai mươi sáu với khoảng năm tỷ, và có hai quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là '
         'quý bốn năm hai nghìn không trăm hai mươi lăm đạt ba trăm bốn mươi tám tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt sáu mươi tám tỷ, quý '
         'hai năm hai nghìn không trăm hai mươi sáu đạt năm mươi lăm tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt năm tỷ. Lũy kế chín tháng đạt một '
         'trăm hai mươi tám tỷ, giảm sáu mươi ba phẩy bảy phần trăm. Nếu lợi nhuận bốn quý gần nhất có một quý đột biến tăng hoặc một quý lỗ, P trên E hiện '
         'tại sẽ không phản ánh đúng sức kiếm tiền bình thường. Khi đó, cách an toàn hơn là tính P trên E trên lợi nhuận trung bình nhiều quý.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 502.4, (56, 189, 248), '502'),
           ('Q1/25', 108.4, (56, 189, 248), '108'),
           ('Q2/25', 99.3, (56, 189, 248), '99'),
           ('Q3/25', 146.0, (56, 189, 248), '146'),
           ('Q4/25', 347.7, (56, 189, 248), '348'),
           ('Q1/26', 68.2, (56, 189, 248), '68'),
           ('Q2/26', 55.2, (56, 189, 248), '55'),
           ('Q3/26', 4.8, (34, 197, 94), '5')]},
 {'k': 'cards',
  'ch': 'Chương 3 – So với ngành',
  'label': '',
  'cap': ('SO VỚI', 'CÙNG NGÀNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, so với ngành. NLG thuộc nhóm bất động sản. Trong hai mươi hai mã cùng nhóm có vốn hóa từ một nghìn năm trăm tỷ, P trên E trung vị khoảng '
         'mười sáu phẩy mười sáu lần, P trên B trung vị khoảng không phẩy chín mươi lăm lần, ROE trung vị khoảng sáu phẩy năm phần trăm. NLG có P trên E cao '
         'hơn mặt bằng nhóm và ROE thấp hơn mặt bằng nhóm. So với ngành giúp tránh một sai lầm phổ biến: thấy P trên E thấp hơn mã khác ngành rồi kết luận là '
         'rẻ. Mỗi ngành có chu kỳ, rủi ro và tốc độ tăng trưởng khác nhau, nên mặt bằng định giá cũng khác nhau. Bảng định giá và báo cáo tài chính đầy đủ của '
         'mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'moc': True,
  'anh': 'comparison chart',
  'cards': [('P/E NLG', '18,04', 'trung vị 16,16'), ('P/B NLG', '0,88', 'trung vị 0,95'), ('ROE NLG', '4,2%', 'trung vị 6,5%')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Điểm tốt và điểm cần soi',
  'label': '',
  'cap': ('ĐIỂM TỐT', 'ĐIỂM CẦN SOI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, điểm tốt và điểm cần soi. Điểm tốt: Biên lợi nhuận gộp bốn mươi sáu phẩy một phần trăm, cùng kỳ bốn mươi bốn phẩy một phần trăm, cải '
         'thiện. Điểm cần soi: Lợi nhuận quý giảm chín mươi sáu phẩy bảy phần trăm so với cùng kỳ. So với quý trước, lợi nhuận giảm chín mươi mốt phẩy ba phần '
         'trăm. Doanh thu giảm tám mươi hai phẩy năm phần trăm. Một định giá chỉ có ý nghĩa khi đặt cạnh câu hỏi: lợi nhuận năm tới cao hơn hay thấp hơn năm '
         'nay? Nếu lợi nhuận đi xuống, P trên E thấp hôm nay sẽ thành P trên E cao vào năm sau.',
  'anh': 'magnifying glass',
  'items': [('Biên lợi nhuận gộp 46,1% (cùng kỳ 44,1%)', (34, 197, 94)),
            ('Lợi nhuận quý giảm −96,7% so với cùng kỳ', (239, 68, 68)),
            ('So với quý trước', (239, 68, 68)),
            ('Doanh thu giảm −82,5%', (239, 68, 68))]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Giá và đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá trong năm mươi hai tuần. Đỉnh khoảng ba mươi bảy phẩy hai mươi ba nghìn đồng, đáy khoảng hai mươi nghìn đồng, giá hiện tại thấp hơn '
         'đỉnh khoảng ba mươi tám phẩy bốn phần trăm. Người mua ở đỉnh cần lãi khoảng sáu mươi hai phần trăm mới hòa vốn. Giá giảm có thể làm định giá rẻ đi, '
         'nhưng cũng có thể là thị trường đang đi trước một quý lợi nhuận xấu. Vì vậy, khi thấy một mã rẻ đi nhanh, anh chị hãy tìm lý do trước khi tìm điểm '
         'mua.',
  'value': -38.4,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 52 TUẦN 37,23',
  'sub': 'giá 22,95',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro và vị thế',
  'label': '',
  'cap': ('RỦI RO', 'VÀ VỊ THẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi và cách giữ vị thế. Beta của NLG khoảng không phẩy chín mươi hai. Tỷ lệ sở hữu nước ngoài khoảng ba mươi lăm phần '
         'trăm. Hai con số này cho biết cổ phiếu rung lắc thế nào và nhạy ra sao với dòng vốn ngoại. Em gợi ý ba nguyên tắc: không để một mã vượt hai mươi '
         'phần trăm danh mục; viết sẵn điều kiện khiến luận điểm sai trước khi mua; và với mã có lợi nhuận dao động mạnh, chia mua làm nhiều lần thay vì mua '
         'một lần. Anh chị có thể mở trang chứng khoán Huy Nguyễn chấm com để xem lại từng con số trong video này.',
  'moc': True,
  'anh': 'warning sign',
  'items': [('Tối đa 20% một mã', (255, 196, 0)), ('Viết điểm sai trước khi mua', (255, 196, 0)), ('Chia mua nhiều lần', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bốn sai lầm khi đọc định giá',
  'label': '',
  'cap': ('BỐN SAI LẦM', 'KHI ĐỌC ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, bốn sai lầm hay gặp khi đọc định giá. Một, so P trên E giữa hai ngành khác nhau, ví dụ so một hãng hàng không với một ngân hàng. Hai, '
         'dùng P trên E của một năm lợi nhuận đột biến để kết luận là rẻ. Ba, nhìn P trên B thấp mà quên hỏi tài sản trên sổ sách có thu hồi được giá trị đó '
         'không. Bốn, quên rằng ROE rất cao có thể đến từ vốn chủ sở hữu mỏng sau nhiều năm lỗ, hoặc từ nợ vay lớn. Với NLG, ROE khoảng bốn phẩy hai phần trăm '
         'cần được đặt cạnh câu hỏi: vốn chủ sở hữu hiện tại có đang thấp bất thường không? Câu trả lời nằm ở bảng cân đối kế toán, mục vốn chủ sở hữu, qua '
         'nhiều quý.',
  'anh': 'mistake warning',
  'items': [('So P/E khác ngành', (239, 68, 68)),
            ('P/E năm đột biến', (239, 68, 68)),
            ('P/B thấp, tài sản ảo', (239, 68, 68)),
            ('ROE cao vì vốn mỏng', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Tóm lại',
  'label': '',
  'cap': ('RẺ HAY ĐẮT', 'TÓM LẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, tóm lại. Rẻ hay đắt không nằm ở một con số. P trên E và P trên B chỉ là giá, còn ROE, chuỗi lợi nhuận và rủi ro mới là thứ anh chị đang '
         'mua. Bảng tóm tắt gồm: P trên E mười tám phẩy không bốn lần, P trên B không phẩy tám mươi tám lần, ROE bốn phẩy hai phần trăm, giá thấp hơn đỉnh năm '
         'mươi hai tuần khoảng ba mươi tám phẩy bốn phần trăm. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'notebook summary',
  'cards': [('P/E', '18,04', 'lần'), ('ROE', '4,2%', ''), ('Cách đỉnh', '−38,4%', '52 tuần')]},
 {'k': 'end',
  'label': '',
  'cap': ('NLG P/E 18,0', 'RẺ HAY ĐẮT?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Anh chị xếp NLG vào nhóm rẻ, hợp lý hay đắt, và vì sao?'}]

S['HI1711A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'DXG – định giá nhanh',
  'cap': ('DXG P/E 121,8', 'ROE 0,6%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đất Xanh, mã DXG, đang giao dịch quanh mười một nghìn đồng, P trên E khoảng một trăm hai mươi mốt phẩy bảy mươi sáu lần, P trên B khoảng không phẩy '
         'chín mươi bảy lần, ROE khoảng không phẩy sáu phần trăm. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt mười lăm tỷ, '
         'giảm tám mươi ba phẩy sáu phần trăm so với cùng kỳ. Rẻ thật, đắt thật, hay thị trường đang nhìn thấy điều gì khác? Video này em đặt ba con số định '
         'giá cạnh chuỗi lợi nhuận tám quý, cạnh mặt bằng của ngành và cạnh rủi ro, để anh chị tự trả lời. Số liệu từ báo cáo quý ba năm hai nghìn không trăm '
         'hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'apartment construction',
  'chart': {'sym': 'DXGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 17.85, 'Đỉnh tuần 3/11/25: 17,85', 0.6], [47, 9.3, 'Đáy tuần 5/10/26: 9,30', 1.6], [51, 11.0, 'Tuần 2/11/26: 11,00', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Ba con số định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, ba con số định giá nghĩa là gì với DXG. P trên E một trăm hai mươi mốt phẩy bảy mươi sáu lần nghĩa là với lợi nhuận mỗi cổ phiếu bốn quý '
         'gần nhất khoảng chín mươi đồng, người mua đang trả khoảng một trăm hai mươi mốt phẩy bảy mươi sáu đồng giá cho mỗi đồng lợi nhuận. Nói cách khác, '
         'nếu lợi nhuận đứng yên, phải khoảng một trăm hai mươi hai năm lợi nhuận mới bằng giá mua. P trên B không phẩy chín mươi bảy lần nghĩa là giá đang '
         'gấp không phẩy chín mươi bảy lần giá trị sổ sách mỗi cổ phiếu, khoảng mười một nghìn hai trăm chín mươi ba đồng. ROE không phẩy sáu phần trăm cho '
         'biết mỗi một trăm đồng vốn chủ sở hữu tạo ra khoảng không phẩy sáu đồng lợi nhuận một năm. Ba con số này liên kết với nhau: P trên E nhân ROE xấp xỉ '
         'bằng P trên B.',
  'moc': True,
  'anh': 'calculator',
  'cards': [('P/E', '121,76', 'lần'), ('P/B', '0,97', 'lần'), ('ROE', '0,6%', 'năm')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lợi nhuận tám quý, gốc của chữ E trong P trên E. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn '
         'không trăm hai mươi sáu, lợi nhuận sau thuế công ty mẹ cao nhất ở quý bốn năm hai nghìn không trăm hai mươi bốn với khoảng một trăm sáu mươi mốt tỷ, '
         'thấp nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng tám tỷ, và có bốn quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là '
         'quý bốn năm hai nghìn không trăm hai mươi lăm đạt tám tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt ba mươi tám tỷ, quý hai năm hai nghìn '
         'không trăm hai mươi sáu đạt năm mươi ba tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt mười lăm tỷ. Lũy kế chín tháng đạt một trăm linh sáu '
         'tỷ, giảm năm mươi hai phẩy ba phần trăm. Nếu lợi nhuận bốn quý gần nhất có một quý đột biến tăng hoặc một quý lỗ, P trên E hiện tại sẽ không phản '
         'ánh đúng sức kiếm tiền bình thường. Khi đó, cách an toàn hơn là tính P trên E trên lợi nhuận trung bình nhiều quý.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 161.0, (56, 189, 248), '161'),
           ('Q1/25', 48.4, (56, 189, 248), '48'),
           ('Q2/25', 81.4, (56, 189, 248), '81'),
           ('Q3/25', 92.8, (56, 189, 248), '93'),
           ('Q4/25', 8.3, (56, 189, 248), '8'),
           ('Q1/26', 37.9, (56, 189, 248), '38'),
           ('Q2/26', 53.1, (56, 189, 248), '53'),
           ('Q3/26', 15.2, (34, 197, 94), '15')]},
 {'k': 'cards',
  'ch': 'Chương 3 – So với ngành',
  'label': '',
  'cap': ('SO VỚI', 'CÙNG NGÀNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, so với ngành. DXG thuộc nhóm bất động sản. Trong hai mươi hai mã cùng nhóm có vốn hóa từ một nghìn năm trăm tỷ, P trên E trung vị khoảng '
         'mười sáu phẩy mười sáu lần, P trên B trung vị khoảng không phẩy chín mươi lăm lần, ROE trung vị khoảng sáu phẩy năm phần trăm. DXG có P trên E cao '
         'hơn mặt bằng nhóm và ROE thấp hơn mặt bằng nhóm. So với ngành giúp tránh một sai lầm phổ biến: thấy P trên E thấp hơn mã khác ngành rồi kết luận là '
         'rẻ. Mỗi ngành có chu kỳ, rủi ro và tốc độ tăng trưởng khác nhau, nên mặt bằng định giá cũng khác nhau. Bảng định giá và báo cáo tài chính đầy đủ của '
         'mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'moc': True,
  'anh': 'comparison chart',
  'cards': [('P/E DXG', '121,76', 'trung vị 16,16'), ('P/B DXG', '0,97', 'trung vị 0,95'), ('ROE DXG', '0,6%', 'trung vị 6,5%')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Điểm tốt và điểm cần soi',
  'label': '',
  'cap': ('ĐIỂM TỐT', 'ĐIỂM CẦN SOI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, điểm tốt và điểm cần soi. Quý này báo cáo không có điểm tốt nổi bật. Điểm cần soi: Lợi nhuận quý giảm tám mươi ba phẩy sáu phần trăm so '
         'với cùng kỳ. So với quý trước, lợi nhuận giảm bảy mươi mốt phẩy ba phần trăm. Doanh thu giảm ba mươi sáu phẩy một phần trăm. Một định giá chỉ có ý '
         'nghĩa khi đặt cạnh câu hỏi: lợi nhuận năm tới cao hơn hay thấp hơn năm nay? Nếu lợi nhuận đi xuống, P trên E thấp hôm nay sẽ thành P trên E cao vào '
         'năm sau.',
  'anh': 'magnifying glass',
  'items': [('Lợi nhuận quý giảm −83,6% so với cùng kỳ', (239, 68, 68)), ('So với quý trước', (239, 68, 68)), ('Doanh thu giảm −36,1%', (239, 68, 68))]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Giá và đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá trong năm mươi hai tuần. Đỉnh khoảng mười bảy phẩy ba mươi bảy nghìn đồng, đáy khoảng chín phẩy sáu mươi mốt nghìn đồng, giá hiện '
         'tại thấp hơn đỉnh khoảng ba mươi sáu phẩy bảy phần trăm. Người mua ở đỉnh cần lãi khoảng năm mươi tám phần trăm mới hòa vốn. Giá giảm có thể làm '
         'định giá rẻ đi, nhưng cũng có thể là thị trường đang đi trước một quý lợi nhuận xấu. Vì vậy, khi thấy một mã rẻ đi nhanh, anh chị hãy tìm lý do '
         'trước khi tìm điểm mua.',
  'value': -36.7,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 52 TUẦN 17,37',
  'sub': 'giá 11,00',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro và vị thế',
  'label': '',
  'cap': ('RỦI RO', 'VÀ VỊ THẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi và cách giữ vị thế. Beta của DXG khoảng không phẩy chín mươi. Tỷ lệ sở hữu nước ngoài khoảng mười bốn phẩy tám phần '
         'trăm. Hai con số này cho biết cổ phiếu rung lắc thế nào và nhạy ra sao với dòng vốn ngoại. Em gợi ý ba nguyên tắc: không để một mã vượt hai mươi '
         'phần trăm danh mục; viết sẵn điều kiện khiến luận điểm sai trước khi mua; và với mã có lợi nhuận dao động mạnh, chia mua làm nhiều lần thay vì mua '
         'một lần. Anh chị có thể mở trang chứng khoán Huy Nguyễn chấm com để xem lại từng con số trong video này.',
  'moc': True,
  'anh': 'warning sign',
  'items': [('Tối đa 20% một mã', (255, 196, 0)), ('Viết điểm sai trước khi mua', (255, 196, 0)), ('Chia mua nhiều lần', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bốn sai lầm khi đọc định giá',
  'label': '',
  'cap': ('BỐN SAI LẦM', 'KHI ĐỌC ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, bốn sai lầm hay gặp khi đọc định giá. Một, so P trên E giữa hai ngành khác nhau, ví dụ so một hãng hàng không với một ngân hàng. Hai, '
         'dùng P trên E của một năm lợi nhuận đột biến để kết luận là rẻ. Ba, nhìn P trên B thấp mà quên hỏi tài sản trên sổ sách có thu hồi được giá trị đó '
         'không. Bốn, quên rằng ROE rất cao có thể đến từ vốn chủ sở hữu mỏng sau nhiều năm lỗ, hoặc từ nợ vay lớn. Với DXG, ROE khoảng không phẩy sáu phần '
         'trăm cần được đặt cạnh câu hỏi: vốn chủ sở hữu hiện tại có đang thấp bất thường không? Câu trả lời nằm ở bảng cân đối kế toán, mục vốn chủ sở hữu, '
         'qua nhiều quý.',
  'anh': 'mistake warning',
  'items': [('So P/E khác ngành', (239, 68, 68)),
            ('P/E năm đột biến', (239, 68, 68)),
            ('P/B thấp, tài sản ảo', (239, 68, 68)),
            ('ROE cao vì vốn mỏng', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Tóm lại',
  'label': '',
  'cap': ('RẺ HAY ĐẮT', 'TÓM LẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, tóm lại. Rẻ hay đắt không nằm ở một con số. P trên E và P trên B chỉ là giá, còn ROE, chuỗi lợi nhuận và rủi ro mới là thứ anh chị đang '
         'mua. Bảng tóm tắt gồm: P trên E một trăm hai mươi mốt phẩy bảy mươi sáu lần, P trên B không phẩy chín mươi bảy lần, ROE không phẩy sáu phần trăm, '
         'giá thấp hơn đỉnh năm mươi hai tuần khoảng ba mươi sáu phẩy bảy phần trăm. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán '
         'Huy Nguyễn chấm com.',
  'anh': 'notebook summary',
  'cards': [('P/E', '121,76', 'lần'), ('ROE', '0,6%', ''), ('Cách đỉnh', '−36,7%', '52 tuần')]},
 {'k': 'end',
  'label': '',
  'cap': ('DXG P/E 121,8', 'RẺ HAY ĐẮT?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Anh chị xếp DXG vào nhóm rẻ, hợp lý hay đắt, và vì sao?'}]

S['Y2_1611A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'NT2 – soi BCTC',
  'cap': ('LÃI 9 THÁNG +57,0%', 'QUÝ 3 +95,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Điện lực Nhơn Trạch hai, mã NThai. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn trăm mười chín tỷ, tăng chín '
         'mươi lăm phẩy bốn phần trăm so với cùng kỳ. Lũy kế chín tháng đạt chín trăm linh sáu tỷ, tăng năm mươi bảy phần trăm. Quý này nhìn từ báo cáo kết '
         'quả kinh doanh thì đã rõ, nhưng báo cáo tài chính có ba phần, và phần ít người đọc nhất là bảng cân đối kế toán và lưu chuyển tiền tệ. Video này em '
         'soi cả ba phần: lợi nhuận đến từ đâu, tiền có về thật không, và doanh nghiệp đang dùng bao nhiêu nợ. Số liệu từ báo cáo quý ba năm hai nghìn không '
         'trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'gas power plant',
  'chart': {'sym': 'NT2W',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 28.22, 'Đỉnh tuần 2/3/26: 28,22', 0.6], [44, 19.36, 'Đáy tuần 14/9/26: 19,36', 1.6], [51, 22.2, 'Tuần 2/11/26: 22,20', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng năm trăm năm mươi ba tỷ, thấp nhất ở quý một năm hai '
         'nghìn không trăm hai mươi lăm với khoảng ba mươi bảy tỷ, và có bốn quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai '
         'nghìn không trăm hai mươi lăm đạt năm trăm năm mươi ba tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt một trăm tám mươi tỷ, quý hai năm hai '
         'nghìn không trăm hai mươi sáu đạt ba trăm linh tám tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn trăm mười chín tỷ. Chuỗi tám quý giúp '
         'tách phần lợi nhuận đều đặn khỏi những quý đột biến.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 74.6, (56, 189, 248), '75'),
           ('Q1/25', 37.0, (56, 189, 248), '37'),
           ('Q2/25', 326.2, (56, 189, 248), '326'),
           ('Q3/25', 214.2, (56, 189, 248), '214'),
           ('Q4/25', 552.8, (56, 189, 248), '553'),
           ('Q1/26', 180.0, (56, 189, 248), '180'),
           ('Q2/26', 307.8, (56, 189, 248), '308'),
           ('Q3/26', 418.6, (34, 197, 94), '419')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Biên lợi nhuận gộp',
  'label': '',
  'cap': ('BIÊN LỢI NHUẬN', 'GỘP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, biên lợi nhuận gộp. Theo báo cáo, biên gộp quý ba năm hai nghìn không trăm hai mươi sáu khoảng mười bảy phẩy năm phần trăm, quý trước '
         'khoảng mười hai phẩy bảy phần trăm, cùng kỳ năm trước khoảng mười phẩy sáu phần trăm. Bình quân tám quý khoảng mười hai phẩy bảy phần trăm. Doanh '
         'thu thuần đạt hai nghìn tám trăm linh bảy tỷ, tăng bốn mươi lăm phẩy sáu phần trăm. Biên gộp là tấm đệm đầu tiên của lợi nhuận. Khi biên co lại, '
         'doanh nghiệp phải bán nhiều hơn chỉ để giữ nguyên lợi nhuận, và mọi chi phí cố định như lãi vay, khấu hao, lương sẽ chiếm phần lớn hơn.',
  'moc': True,
  'anh': 'profit margin',
  'bars': [('Q4/24', 4.921800549358148, (56, 189, 248), '4,9'),
           ('Q1/25', 3.126095184691947, (56, 189, 248), '3,1'),
           ('Q2/25', 17.6091865660885, (56, 189, 248), '17,6'),
           ('Q3/25', 10.610932475884244, (56, 189, 248), '10,6'),
           ('Q4/25', 25.05947660586836, (56, 189, 248), '25,1'),
           ('Q1/26', 10.01519546898743, (56, 189, 248), '10,0'),
           ('Q2/26', 12.657107452646486, (56, 189, 248), '12,7'),
           ('Q3/26', 17.451553149045314, (34, 197, 94), '17,5')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Nợ vay',
  'label': '',
  'cap': ('NỢ VAY', 'VÀ LÃI VAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, nợ vay. Cuối quý ba năm hai nghìn không trăm hai mươi sáu, tổng vay ngắn hạn và dài hạn khoảng một nghìn bảy trăm chín mươi sáu tỷ, vốn '
         'chủ sở hữu khoảng năm nghìn bốn trăm hai mươi mốt tỷ, tức nợ vay bằng khoảng không phẩy ba mươi ba lần vốn chủ. Một năm trước, tỷ lệ này khoảng '
         'không phẩy hai mươi chín lần. Chi phí lãi vay quý này khoảng hai mươi bảy tỷ, cùng kỳ khoảng mười sáu tỷ. Tiền và tương đương tiền cuối kỳ khoảng '
         'mười hai tỷ. Nợ vay không xấu nếu tiền vay tạo ra lợi nhuận cao hơn lãi phải trả. Nhưng nợ làm lợi nhuận nhạy hơn: khi kinh doanh tốt, lãi tăng '
         'nhanh; khi kinh doanh xấu, lãi vay vẫn phải trả đủ.',
  'anh': 'bank loan',
  'cards': [('Nợ vay', '≈ 1.796 tỷ', ''), ('Nợ vay / vốn chủ', '0,33 lần', ''), ('Lãi vay quý', '≈ 27 tỷ', '')]},
 {'k': 'bars',
  'ch': 'Chương 4 – Dòng tiền kinh doanh',
  'label': '',
  'cap': ('DÒNG TIỀN', 'KINH DOANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, tiền có về thật không. Bốn quý gần nhất, lợi nhuận sau thuế cộng lại khoảng một nghìn bốn trăm năm mươi chín tỷ, dòng tiền thuần từ hoạt '
         'động kinh doanh cộng lại khoảng một nghìn hai trăm hai mươi bảy tỷ. Từng quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm âm '
         'ba mươi tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt tám trăm sáu mươi tỷ, quý hai năm hai nghìn không trăm hai mươi sáu âm hai mươi sáu '
         'tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn trăm hai mươi hai tỷ. Hàng tồn kho cuối kỳ khoảng ba trăm bốn mươi sáu tỷ, khoản phải thu '
         'ngắn hạn khoảng bốn nghìn hai trăm năm mươi lăm tỷ, so với một năm trước lần lượt khoảng ba trăm năm mươi mốt tỷ và ba nghìn một trăm ba mươi chín '
         'tỷ. Nếu phải thu và tồn kho tăng nhanh hơn doanh thu, lợi nhuận đang được ghi nhận trước khi tiền về. Điều đó chưa phải là sai, nhưng anh chị cần '
         'theo dõi xem các quý sau tiền có về theo không.',
  'moc': True,
  'anh': 'cash flow',
  'bars': [('Q4/24', 150.3, (34, 197, 94), '150'),
           ('Q1/25', -169.1, (239, 68, 68), '-169'),
           ('Q2/25', 500.8, (34, 197, 94), '501'),
           ('Q3/25', 701.2, (34, 197, 94), '701'),
           ('Q4/25', -29.6, (239, 68, 68), '-30'),
           ('Q1/26', 860.1, (34, 197, 94), '860'),
           ('Q2/26', -25.5, (239, 68, 68), '-26'),
           ('Q3/26', 421.6, (34, 197, 94), '422')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, điểm tốt và rủi ro cần theo dõi. Lợi nhuận quý tăng chín mươi lăm phẩy bốn phần trăm so với cùng kỳ. So với quý trước, lợi nhuận tăng ba '
         'mươi sáu phần trăm. Ngoài các dòng trên, rủi ro ngành cũng cần đặt cạnh: giá đầu vào, nhu cầu của khách hàng và lãi suất. Một doanh nghiệp tốt vẫn '
         'có thể có hai, ba quý xấu khi ngành đi xuống.',
  'anh': 'warning sign',
  'items': [('Lợi nhuận quý tăng +95,4% so với cùng kỳ', (34, 197, 94)), ('So với quý trước', (34, 197, 94))]},
 {'k': 'cards',
  'ch': 'Chương 6 – Định giá và vị thế',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'VÀ VỊ THẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, định giá và vị thế. Giá khoảng hai mươi hai phẩy hai mươi nghìn đồng, P trên E khoảng bốn phẩy ba mươi tám lần, P trên B khoảng một phẩy '
         'hai mươi bốn lần, ROE khoảng hai mươi chín phẩy bốn phần trăm, thấp hơn đỉnh năm mươi hai tuần khoảng mười chín phẩy chín phần trăm. Khi đã soi đủ '
         'ba phần báo cáo, anh chị hãy quyết định tỷ trọng trước khi quyết định mua: doanh nghiệp càng nhiều nợ hoặc dòng tiền càng thất thường thì tỷ trọng '
         'tối đa nên càng thấp. Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '4,38', 'lần'), ('P/B', '1,24', 'lần'), ('Cách đỉnh', '−19,9%', '52 tuần')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Đọc thuyết minh ở đâu',
  'label': '',
  'cap': ('ĐỌC THUYẾT MINH', 'Ở ĐÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, đọc thuyết minh ở đâu. Bốn con số trong video đều có trong báo cáo tài chính quý, nhưng lời giải thích nằm ở thuyết minh. Khoản vay: mục '
         'vay và nợ thuê tài chính, ghi rõ ngân hàng cho vay, lãi suất và kỳ hạn. Hàng tồn kho: mục hàng tồn kho, cho biết nguyên liệu, thành phẩm và dự phòng '
         'giảm giá. Phải thu: mục phải thu khách hàng, có bảng tuổi nợ và dự phòng phải thu khó đòi. Doanh thu và giá vốn: mục doanh thu theo mảng, cho biết '
         'mảng nào đang kéo lợi nhuận. Đọc thuyết minh mất thêm mười phút, nhưng giúp anh chị phân biệt một quý xấu tạm thời với một xu hướng xấu kéo dài.',
  'anh': 'document reading',
  'items': [('Vay và nợ thuê tài chính', (255, 196, 0)),
            ('Hàng tồn kho', (255, 196, 0)),
            ('Phải thu, tuổi nợ', (255, 196, 0)),
            ('Doanh thu theo mảng', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 7 – Bốn câu hỏi',
  'label': '',
  'cap': ('BỐN CÂU HỎI', 'KHI SOI BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, bốn câu hỏi khi soi bất kỳ báo cáo nào. Một, lợi nhuận đến từ hoạt động chính hay từ khoản bất thường? Hai, biên gộp đang mở rộng hay co '
         'lại? Ba, dòng tiền kinh doanh có theo kịp lợi nhuận không? Bốn, nợ vay so với vốn chủ đang tăng hay giảm? Bài viết kèm video và bảng số có trong thư '
         'viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận từ đâu?', (255, 196, 0)),
            ('Biên gộp mở hay co?', (255, 196, 0)),
            ('Tiền có về không?', (255, 196, 0)),
            ('Nợ tăng hay giảm?', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI 9 THÁNG +57,0%', 'QUÝ 3 +95,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Trong bốn câu hỏi vừa rồi, câu nào anh chị thấy NThai đang trả lời yếu nhất?'}]

S['Y2_1711A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'NKG – soi BCTC',
  'cap': ('LÃI QUÝ 3 +154,8%', 'DOANH THU +45,0%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Thép Nam Kim, mã NKG. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt một trăm hai mươi sáu tỷ, tăng một trăm năm '
         'mươi bốn phẩy tám phần trăm so với cùng kỳ. Lũy kế chín tháng đạt hai trăm năm mươi ba tỷ, tăng hai mươi hai phẩy ba phần trăm. Quý này nhìn từ báo '
         'cáo kết quả kinh doanh thì đã rõ, nhưng báo cáo tài chính có ba phần, và phần ít người đọc nhất là bảng cân đối kế toán và lưu chuyển tiền tệ. Video '
         'này em soi cả ba phần: lợi nhuận đến từ đâu, tiền có về thật không, và doanh nghiệp đang dùng bao nhiêu nợ. Số liệu từ báo cáo quý ba năm hai nghìn '
         'không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'steel coils',
  'chart': {'sym': 'NKGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[2, 16.05, 'Đỉnh tuần 17/11/25: 16,05', 0.6], [47, 9.0, 'Đáy tuần 5/10/26: 9,00', 1.6], [51, 12.15, 'Tuần 2/11/26: 12,15', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý ba năm hai nghìn không trăm hai mươi sáu với khoảng một trăm hai mươi sáu tỷ, thấp nhất ở quý bốn năm hai '
         'nghìn không trăm hai mươi lăm với khoảng âm chín tỷ, và có năm quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai nghìn '
         'không trăm hai mươi lăm lỗ chín tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt hai mươi hai tỷ, quý hai năm hai nghìn không trăm hai mươi sáu '
         'đạt một trăm linh bốn tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt một trăm hai mươi sáu tỷ. Chuỗi tám quý giúp tách phần lợi nhuận đều đặn '
         'khỏi những quý đột biến.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 18.4, (56, 189, 248), '18'),
           ('Q1/25', 65.4, (56, 189, 248), '65'),
           ('Q2/25', 91.6, (56, 189, 248), '92'),
           ('Q3/25', 49.5, (56, 189, 248), '50'),
           ('Q4/25', -9.4, (239, 68, 68), '-9'),
           ('Q1/26', 22.3, (56, 189, 248), '22'),
           ('Q2/26', 104.1, (56, 189, 248), '104'),
           ('Q3/26', 126.2, (34, 197, 94), '126')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Biên lợi nhuận gộp',
  'label': '',
  'cap': ('BIÊN LỢI NHUẬN', 'GỘP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, biên lợi nhuận gộp. Theo báo cáo, biên gộp quý ba năm hai nghìn không trăm hai mươi sáu khoảng chín phần trăm, quý trước khoảng mười '
         'phẩy năm phần trăm, cùng kỳ năm trước khoảng bốn phẩy tám phần trăm. Bình quân tám quý khoảng sáu phẩy hai phần trăm. Doanh thu thuần đạt năm nghìn '
         'bốn trăm bảy mươi hai tỷ, tăng bốn mươi lăm phần trăm. Biên gộp là tấm đệm đầu tiên của lợi nhuận. Khi biên co lại, doanh nghiệp phải bán nhiều hơn '
         'chỉ để giữ nguyên lợi nhuận, và mọi chi phí cố định như lãi vay, khấu hao, lương sẽ chiếm phần lớn hơn.',
  'moc': True,
  'anh': 'profit margin',
  'bars': [('Q4/24', 6.730661654471818, (56, 189, 248), '6,7'),
           ('Q1/25', 6.437495415760005, (56, 189, 248), '6,4'),
           ('Q2/25', 7.089405277668373, (56, 189, 248), '7,1'),
           ('Q3/25', 4.773263364342318, (56, 189, 248), '4,8'),
           ('Q4/25', 2.2891758329348, (56, 189, 248), '2,3'),
           ('Q1/26', 2.612375053657938, (56, 189, 248), '2,6'),
           ('Q2/26', 10.53202255312997, (56, 189, 248), '10,5'),
           ('Q3/26', 9.036915204678362, (34, 197, 94), '9,0')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Nợ vay',
  'label': '',
  'cap': ('NỢ VAY', 'VÀ LÃI VAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, nợ vay. Cuối quý ba năm hai nghìn không trăm hai mươi sáu, tổng vay ngắn hạn và dài hạn khoảng tám nghìn sáu trăm ba mươi lăm tỷ, vốn chủ '
         'sở hữu khoảng bảy nghìn bảy trăm bảy mươi chín tỷ, tức nợ vay bằng khoảng một phẩy mười một lần vốn chủ. Một năm trước, tỷ lệ này khoảng không phẩy '
         'chín mươi mốt lần. Chi phí lãi vay quý này khoảng một trăm tỷ, cùng kỳ khoảng năm mươi lăm tỷ. Tiền và tương đương tiền cuối kỳ khoảng năm trăm tám '
         'mươi hai tỷ. Nợ vay không xấu nếu tiền vay tạo ra lợi nhuận cao hơn lãi phải trả. Nhưng nợ làm lợi nhuận nhạy hơn: khi kinh doanh tốt, lãi tăng '
         'nhanh; khi kinh doanh xấu, lãi vay vẫn phải trả đủ.',
  'anh': 'bank loan',
  'cards': [('Nợ vay', '≈ 8.635 tỷ', ''), ('Nợ vay / vốn chủ', '1,11 lần', ''), ('Lãi vay quý', '≈ 100 tỷ', '')]},
 {'k': 'bars',
  'ch': 'Chương 4 – Dòng tiền kinh doanh',
  'label': '',
  'cap': ('DÒNG TIỀN', 'KINH DOANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, tiền có về thật không. Bốn quý gần nhất, lợi nhuận sau thuế cộng lại khoảng hai trăm bốn mươi ba tỷ, dòng tiền thuần từ hoạt động kinh '
         'doanh cộng lại khoảng một nghìn năm trăm bốn mươi hai tỷ. Từng quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt bảy trăm '
         'chín mươi bốn tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt bốn trăm bảy mươi bảy tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt hai '
         'trăm bốn mươi bốn tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt hai mươi sáu tỷ. Hàng tồn kho cuối kỳ khoảng sáu nghìn ba trăm năm mươi bốn '
         'tỷ, khoản phải thu ngắn hạn khoảng một nghìn bảy trăm linh tám tỷ, so với một năm trước lần lượt khoảng năm nghìn không trăm bốn mươi chín tỷ và một '
         'nghìn chín trăm bảy mươi sáu tỷ. Nếu phải thu và tồn kho tăng nhanh hơn doanh thu, lợi nhuận đang được ghi nhận trước khi tiền về. Điều đó chưa phải '
         'là sai, nhưng anh chị cần theo dõi xem các quý sau tiền có về theo không.',
  'moc': True,
  'anh': 'cash flow',
  'bars': [('Q4/24', 179.2, (34, 197, 94), '179'),
           ('Q1/25', 433.6, (34, 197, 94), '434'),
           ('Q2/25', -62.8, (239, 68, 68), '-63'),
           ('Q3/25', 161.8, (34, 197, 94), '162'),
           ('Q4/25', 794.4, (34, 197, 94), '794'),
           ('Q1/26', 476.8, (34, 197, 94), '477'),
           ('Q2/26', 244.3, (34, 197, 94), '244'),
           ('Q3/26', 26.3, (34, 197, 94), '26')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, điểm tốt và rủi ro cần theo dõi. Lợi nhuận quý tăng một trăm năm mươi bốn phẩy tám phần trăm so với cùng kỳ. Doanh thu tăng bốn mươi lăm '
         'phần trăm. Chi phí lãi vay tăng tám mươi ba phần trăm, ăn vào lợi nhuận. Ngoài các dòng trên, rủi ro ngành cũng cần đặt cạnh: giá đầu vào, nhu cầu '
         'của khách hàng và lãi suất. Một doanh nghiệp tốt vẫn có thể có hai, ba quý xấu khi ngành đi xuống.',
  'anh': 'warning sign',
  'items': [('Lợi nhuận quý tăng +154,8% so với cùng k', (34, 197, 94)),
            ('Doanh thu tăng +45,0%', (34, 197, 94)),
            ('Chi phí lãi vay tăng +83,0%', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 6 – Định giá và vị thế',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'VÀ VỊ THẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, định giá và vị thế. Giá khoảng mười hai phẩy mười lăm nghìn đồng, P trên E khoảng hai mươi bốn phẩy năm mươi chín lần, P trên B khoảng '
         'không phẩy bảy mươi bảy lần, ROE khoảng ba phẩy hai phần trăm, thấp hơn đỉnh năm mươi hai tuần khoảng hai mươi hai phẩy năm phần trăm. Khi đã soi đủ '
         'ba phần báo cáo, anh chị hãy quyết định tỷ trọng trước khi quyết định mua: doanh nghiệp càng nhiều nợ hoặc dòng tiền càng thất thường thì tỷ trọng '
         'tối đa nên càng thấp. Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '24,59', 'lần'), ('P/B', '0,77', 'lần'), ('Cách đỉnh', '−22,5%', '52 tuần')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Đọc thuyết minh ở đâu',
  'label': '',
  'cap': ('ĐỌC THUYẾT MINH', 'Ở ĐÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, đọc thuyết minh ở đâu. Bốn con số trong video đều có trong báo cáo tài chính quý, nhưng lời giải thích nằm ở thuyết minh. Khoản vay: mục '
         'vay và nợ thuê tài chính, ghi rõ ngân hàng cho vay, lãi suất và kỳ hạn. Hàng tồn kho: mục hàng tồn kho, cho biết nguyên liệu, thành phẩm và dự phòng '
         'giảm giá. Phải thu: mục phải thu khách hàng, có bảng tuổi nợ và dự phòng phải thu khó đòi. Doanh thu và giá vốn: mục doanh thu theo mảng, cho biết '
         'mảng nào đang kéo lợi nhuận. Đọc thuyết minh mất thêm mười phút, nhưng giúp anh chị phân biệt một quý xấu tạm thời với một xu hướng xấu kéo dài.',
  'anh': 'document reading',
  'items': [('Vay và nợ thuê tài chính', (255, 196, 0)),
            ('Hàng tồn kho', (255, 196, 0)),
            ('Phải thu, tuổi nợ', (255, 196, 0)),
            ('Doanh thu theo mảng', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 7 – Bốn câu hỏi',
  'label': '',
  'cap': ('BỐN CÂU HỎI', 'KHI SOI BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, bốn câu hỏi khi soi bất kỳ báo cáo nào. Một, lợi nhuận đến từ hoạt động chính hay từ khoản bất thường? Hai, biên gộp đang mở rộng hay co '
         'lại? Ba, dòng tiền kinh doanh có theo kịp lợi nhuận không? Bốn, nợ vay so với vốn chủ đang tăng hay giảm? Bài viết kèm video và bảng số có trong thư '
         'viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận từ đâu?', (255, 196, 0)),
            ('Biên gộp mở hay co?', (255, 196, 0)),
            ('Tiền có về không?', (255, 196, 0)),
            ('Nợ tăng hay giảm?', (255, 196, 0))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI QUÝ 3 +154,8%', 'DOANH THU +45,0%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Trong bốn câu hỏi vừa rồi, câu nào anh chị thấy NKG đang trả lời yếu nhất?'}]

S['TS1611A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'MBB – tích sản',
  'cap': ('GÓP ĐỀU MBB', 'LÃI 30,7%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nếu mỗi tháng anh chị góp đều ba triệu đồng vào cổ phiếu MBB của MB, bắt đầu từ ngày bảy tháng mười một năm hai nghìn không trăm hai mươi ba, thì '
         'sau ba mươi bảy tháng, tổng vốn một trăm mười một triệu đồng hôm nay có giá trị khoảng một trăm bốn mươi lăm triệu đồng, lãi khoảng ba mươi phẩy bảy '
         'phần trăm. Còn nếu bỏ hết một trăm mười một triệu một lần ngay tháng đầu, kết quả là khoảng hai trăm ba mươi bốn phẩy tám triệu, lãi khoảng một trăm '
         'mười một phẩy năm phần trăm. Video này em đi từng bước: giá vốn bình quân, những tháng âm, lợi nhuận doanh nghiệp và cách giữ kỷ luật. Phép tính '
         'dùng giá đóng cửa phiên đầu mỗi tháng, chưa tính cổ tức tiền mặt, phí và thuế.',
  'moc': True,
  'anh': 'bank building',
  'chart': {'sym': 'MBBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[14, 23.63, 'Đỉnh tuần 9/2/26: 23,63', 0.6], [37, 17.78, 'Đáy tuần 27/7/26: 17,78', 1.6], [51, 19.25, 'Tuần 2/11/26: 19,25', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Hai cách, hai kết quả',
  'label': '',
  'cap': ('HAI CÁCH', 'HAI KẾT QUẢ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, hai cách, hai kết quả. Giá MBB tháng đầu khoảng chín phẩy mười nghìn đồng, giá ngày sáu tháng mười một năm hai nghìn không trăm hai mươi '
         'sáu khoảng mười chín phẩy hai mươi lăm nghìn đồng. Góp đều cho kết quả một trăm bốn mươi lăm triệu, mua một lần cho kết quả hai trăm ba mươi bốn '
         'phẩy tám triệu. Mua một lần thắng khi giá đi lên đều từ đầu kỳ; góp đều thắng khi giá đi xuống rồi mới hồi. Điều quan trọng không phải cách nào '
         'thắng trong quá khứ, mà là cách nào anh chị làm được đều đặn mà không bỏ cuộc giữa chừng. Với người đi làm, góp đều còn có một lợi thế không nằm '
         'trong bảng tính: nó khớp với dòng tiền lương hằng tháng, nên không cần có sẵn một khoản lớn và không cần đoán thời điểm.',
  'moc': True,
  'anh': 'coins jar',
  'cards': [('Tổng vốn', '111 triệu', '37 tháng'), ('Góp đều', '145,0 triệu', '+30,7%'), ('Mua một lần', '234,8 triệu', '+111,5%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Giá trị danh mục theo thời gian',
  'label': '',
  'cap': ('GIÁ TRỊ', 'DANH MỤC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, giá vốn bình quân. Góp đều ba mươi bảy tháng cho giá vốn bình quân khoảng mười bốn phẩy bảy mươi ba nghìn đồng một cổ phiếu, so với giá '
         'hiện tại khoảng mười chín phẩy hai mươi lăm nghìn đồng. Góp cùng một số tiền mỗi tháng thì tháng giá thấp mua được nhiều cổ phiếu hơn, tháng giá cao '
         'mua được ít hơn, nên giá vốn bình quân thường thấp hơn giá trung bình các tháng. Trong ví dụ này, trung bình cộng giá của ba mươi bảy lần mua khoảng '
         'mười lăm phẩy tám mươi bốn nghìn đồng, còn giá vốn bình quân thực tế khoảng mười bốn phẩy bảy mươi ba nghìn đồng. Nhưng giá vốn thấp không tự biến '
         'thành lãi: nếu giá cuối kỳ vẫn dưới giá vốn bình quân, danh mục vẫn âm.',
  'anh': 'growth chart',
  'bars': [('07/24', 29.2, (34, 197, 94), '29'),
           ('11/24', 44.1, (34, 197, 94), '44'),
           ('03/25', 60.2, (34, 197, 94), '60'),
           ('07/25', 80.4, (34, 197, 94), '80'),
           ('11/25', 106.6, (34, 197, 94), '107'),
           ('03/26', 140.6, (34, 197, 94), '141'),
           ('07/26', 142.8, (34, 197, 94), '143'),
           ('11/26', 141.3, (34, 197, 94), '141')]},
 {'k': 'bignum',
  'ch': 'Chương 3 – Những tháng âm',
  'label': '',
  'cap': ('NHỮNG THÁNG', 'DANH MỤC ÂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, những tháng âm. Trong ba mươi bảy lần góp, có không tháng giá trị danh mục thấp hơn số vốn đã bỏ vào. Thời điểm xấu nhất là tháng mười '
         'một năm hai nghìn không trăm hai mươi ba, danh mục dương khoảng không phần trăm so với vốn. Thời điểm tốt nhất là tháng chín năm hai nghìn không '
         'trăm hai mươi lăm, lãi khoảng tám mươi phẩy ba phần trăm. Đây là phần mà bảng tính thường bỏ qua: người góp đều phải chịu được những tháng âm liên '
         'tiếp mà vẫn tiếp tục góp. Nếu dừng ở đúng tháng xấu nhất, kết quả sẽ khác hẳn con số cuối kỳ.',
  'moc': True,
  'value': 0,
  'fmt': '{:,.0f}',
  'unit': ' tháng',
  'top': 'TRÊN 37 LẦN GÓP',
  'sub': 'xấu nhất 0,0%',
  'col': (34, 197, 94)},
 {'k': 'bars',
  'ch': 'Chương 4 – Lợi nhuận doanh nghiệp',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, doanh nghiệp phía sau cổ phiếu. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai '
         'mươi sáu, lợi nhuận sau thuế công ty mẹ cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng tám nghìn bảy trăm sáu mươi ba tỷ, thấp '
         'nhất ở quý ba năm hai nghìn không trăm hai mươi lăm với khoảng năm nghìn năm trăm bảy mươi mốt tỷ, và có ba quý tăng so với quý liền trước. Bốn quý '
         'gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt tám nghìn bảy trăm sáu mươi ba tỷ, quý một năm hai nghìn không trăm hai mươi '
         'sáu đạt bảy nghìn năm trăm mười sáu tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt tám nghìn hai trăm hai mươi chín tỷ, quý ba năm hai nghìn '
         'không trăm hai mươi sáu đạt tám nghìn không trăm bốn mươi tỷ. Lũy kế chín tháng đạt hai mươi ba nghìn bảy trăm tám mươi bốn tỷ, tăng ba mươi hai '
         'phần trăm. Tích sản bằng cổ phiếu là góp vốn vào một doanh nghiệp, nên lợi nhuận doanh nghiệp tăng đều qua nhiều năm mới là động cơ thật của giá cổ '
         'phiếu. Góp đều chỉ giúp làm mượt giá mua.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 6284.2, (56, 189, 248), '6.284'),
           ('Q1/25', 6567.7, (56, 189, 248), '6.568'),
           ('Q2/25', 5877.6, (56, 189, 248), '5.878'),
           ('Q3/25', 5571.0, (56, 189, 248), '5.571'),
           ('Q4/25', 8762.6, (56, 189, 248), '8.763'),
           ('Q1/26', 7515.5, (56, 189, 248), '7.516'),
           ('Q2/26', 8229.1, (56, 189, 248), '8.229'),
           ('Q3/26', 8039.5, (34, 197, 94), '8.040')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá hôm nay',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'HÔM NAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, định giá hôm nay. MBB có P trên E khoảng năm phẩy chín mươi sáu lần, P trên B khoảng một phẩy hai mươi ba lần, ROE khoảng hai mươi mốt '
         'phẩy tám phần trăm, beta khoảng không phẩy bảy mươi sáu. Người tích sản không cần mua ở giá thấp nhất, nhưng nên tránh góp mạnh tay khi định giá đã '
         'cao hơn hẳn mặt bằng lịch sử. Một cách đơn giản là giữ số tiền góp cố định, không tăng tiền góp khi giá tăng nóng. Bảng định giá và báo cáo tài '
         'chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '5,96', 'lần'), ('ROE', '21,8%', ''), ('Beta', '0,76', '')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Quản trị rủi ro khi tích sản',
  'label': '',
  'cap': ('QUẢN TRỊ RỦI RO', 'KHI TÍCH SẢN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, quản trị rủi ro cho người tích sản. Một, không dồn toàn bộ tiền góp vào một mã: nên chia ít nhất ba đến năm mã khác ngành, hoặc kết hợp '
         'quỹ chỉ số. Hai, giữ quỹ dự phòng khoảng sáu tháng chi tiêu bằng tiền gửi trước khi góp, để không phải bán cổ phiếu đúng lúc giá thấp. Ba, mỗi năm '
         'xem lại tỷ trọng một lần: mã nào phình quá ba mươi phần trăm% danh mục thì giảm bớt về mức đã định. Bốn, không dùng vay ký quỹ cho danh mục tích '
         'sản, vì đòn bẩy biến những tháng âm bình thường thành lệnh bán bắt buộc.',
  'moc': True,
  'anh': 'umbrella rain',
  'items': [('Chia 3–5 mã khác ngành', (34, 197, 94)),
            ('Quỹ dự phòng 6 tháng', (34, 197, 94)),
            ('Tái cân bằng mỗi năm', (255, 196, 0)),
            ('Không vay ký quỹ', (239, 68, 68))]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Góp đều cho bền',
  'label': '',
  'cap': ('GÓP ĐỀU', 'CHO BỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, góp đều thế nào cho bền. Một, chọn một ngày cố định mỗi tháng, ví dụ ngày nhận lương, và đặt lệnh theo số tiền đã định, không chờ giá '
         'đẹp. Hai, ghi nhật ký mỗi lần góp: ngày, giá, số cổ phiếu, giá vốn bình quân mới. Ba, đặt quy tắc cho những tháng thị trường giảm mạnh từ trước, ví '
         'dụ vẫn góp đúng số tiền cũ, không dừng và cũng không vay thêm để mua. Bốn, mỗi quý đọc lại kết quả kinh doanh của doanh nghiệp, vì lý do để tiếp tục '
         'góp là doanh nghiệp vẫn tốt, không phải giá vẫn tăng. Những quy tắc nhỏ này giúp anh chị đi qua không tháng âm như trong ví dụ của MBB mà không phải '
         'quyết định lại từ đầu mỗi lần thị trường biến động.',
  'anh': 'calendar planner',
  'items': [('Ngày cố định mỗi tháng', (34, 197, 94)),
            ('Nhật ký giá vốn', (34, 197, 94)),
            ('Quy tắc tháng giảm mạnh', (255, 196, 0)),
            ('Đọc KQKD mỗi quý', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Tóm lại',
  'label': '',
  'cap': ('TÍCH SẢN', 'TÓM LẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, tóm lại. Góp đều ba mươi bảy tháng vào MBB cho kết quả lãi khoảng ba mươi phẩy bảy phần trăm, mua một lần cho kết quả lãi khoảng một '
         'trăm mười một phẩy năm phần trăm. Quá khứ không bảo đảm tương lai, nhưng con số giúp anh chị biết trước mình sẽ phải chịu đựng những gì. Bài viết '
         'kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'notebook summary',
  'cards': [('Góp đều', '+30,7%', ''), ('Một lần', '+111,5%', ''), ('Tháng âm', '0', '/37')]},
 {'k': 'end',
  'label': '',
  'cap': ('GÓP ĐỀU MBB', 'LÃI 30,7%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu dùng giá đóng cửa đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu và báo cáo tài chính quý ba năm hai nghìn không trăm hai '
         'mươi sáu. Nếu bắt đầu góp đều từ hôm nay, anh chị chọn một mã, hay chia đều cho nhiều mã?'}]

S['TS1711A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'HPG – tích sản',
  'cap': ('GÓP ĐỀU HPG', 'LÃI 0,8%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nếu mỗi tháng anh chị góp đều ba triệu đồng vào cổ phiếu HPG của Hòa Phát, bắt đầu từ ngày bảy tháng mười một năm hai nghìn không trăm hai mươi ba, '
         'thì sau ba mươi bảy tháng, tổng vốn một trăm mười một triệu đồng hôm nay có giá trị khoảng một trăm mười một phẩy chín triệu đồng, lãi khoảng không '
         'phẩy tám phần trăm. Còn nếu bỏ hết một trăm mười một triệu một lần ngay tháng đầu, kết quả là khoảng một trăm ba mươi bốn phẩy chín triệu, lãi '
         'khoảng hai mươi mốt phẩy năm phần trăm. Video này em đi từng bước: giá vốn bình quân, những tháng âm, lợi nhuận doanh nghiệp và cách giữ kỷ luật. '
         'Phép tính dùng giá đóng cửa phiên đầu mỗi tháng, chưa tính cổ tức tiền mặt, phí và thuế.',
  'moc': True,
  'anh': 'steel mill',
  'chart': {'sym': 'HPGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[15, 26.51, 'Đỉnh tuần 23/2/26: 26,51', 0.6], [46, 19.6, 'Đáy tuần 28/9/26: 19,60', 1.6], [51, 21.2, 'Tuần 2/11/26: 21,20', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Hai cách, hai kết quả',
  'label': '',
  'cap': ('HAI CÁCH', 'HAI KẾT QUẢ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, hai cách, hai kết quả. Giá HPG tháng đầu khoảng mười bảy phẩy bốn mươi lăm nghìn đồng, giá ngày sáu tháng mười một năm hai nghìn không '
         'trăm hai mươi sáu khoảng hai mươi mốt phẩy hai mươi nghìn đồng. Góp đều cho kết quả một trăm mười một phẩy chín triệu, mua một lần cho kết quả một '
         'trăm ba mươi bốn phẩy chín triệu. Mua một lần thắng khi giá đi lên đều từ đầu kỳ; góp đều thắng khi giá đi xuống rồi mới hồi. Điều quan trọng không '
         'phải cách nào thắng trong quá khứ, mà là cách nào anh chị làm được đều đặn mà không bỏ cuộc giữa chừng. Với người đi làm, góp đều còn có một lợi thế '
         'không nằm trong bảng tính: nó khớp với dòng tiền lương hằng tháng, nên không cần có sẵn một khoản lớn và không cần đoán thời điểm.',
  'moc': True,
  'anh': 'coins jar',
  'cards': [('Tổng vốn', '111 triệu', '37 tháng'), ('Góp đều', '111,9 triệu', '+0,8%'), ('Mua một lần', '134,9 triệu', '+21,5%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Giá trị danh mục theo thời gian',
  'label': '',
  'cap': ('GIÁ TRỊ', 'DANH MỤC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, giá vốn bình quân. Góp đều ba mươi bảy tháng cho giá vốn bình quân khoảng hai mươi mốt phẩy không bốn nghìn đồng một cổ phiếu, so với '
         'giá hiện tại khoảng hai mươi mốt phẩy hai mươi nghìn đồng. Góp cùng một số tiền mỗi tháng thì tháng giá thấp mua được nhiều cổ phiếu hơn, tháng giá '
         'cao mua được ít hơn, nên giá vốn bình quân thường thấp hơn giá trung bình các tháng. Trong ví dụ này, trung bình cộng giá của ba mươi bảy lần mua '
         'khoảng hai mươi mốt phẩy hai mươi sáu nghìn đồng, còn giá vốn bình quân thực tế khoảng hai mươi mốt phẩy không bốn nghìn đồng. Nhưng giá vốn thấp '
         'không tự biến thành lãi: nếu giá cuối kỳ vẫn dưới giá vốn bình quân, danh mục vẫn âm.',
  'anh': 'growth chart',
  'bars': [('07/24', 29.2, (34, 197, 94), '29'),
           ('11/24', 39.5, (34, 197, 94), '40'),
           ('03/25', 54.2, (34, 197, 94), '54'),
           ('07/25', 64.9, (34, 197, 94), '65'),
           ('11/25', 86.3, (34, 197, 94), '86'),
           ('03/26', 107.1, (34, 197, 94), '107'),
           ('07/26', 110.4, (34, 197, 94), '110'),
           ('11/26', 107.6, (239, 68, 68), '108')]},
 {'k': 'bignum',
  'ch': 'Chương 3 – Những tháng âm',
  'label': '',
  'cap': ('NHỮNG THÁNG', 'DANH MỤC ÂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, những tháng âm. Trong ba mươi bảy lần góp, có năm tháng giá trị danh mục thấp hơn số vốn đã bỏ vào. Thời điểm xấu nhất là tháng mười năm '
         'hai nghìn không trăm hai mươi sáu, danh mục âm khoảng bốn phẩy tám phần trăm so với vốn. Thời điểm tốt nhất là tháng chín năm hai nghìn không trăm '
         'hai mươi lăm, lãi khoảng hai mươi sáu phẩy một phần trăm. Đây là phần mà bảng tính thường bỏ qua: người góp đều phải chịu được những tháng âm liên '
         'tiếp mà vẫn tiếp tục góp. Nếu dừng ở đúng tháng xấu nhất, kết quả sẽ khác hẳn con số cuối kỳ.',
  'moc': True,
  'value': 5,
  'fmt': '{:,.0f}',
  'unit': ' tháng',
  'top': 'TRÊN 37 LẦN GÓP',
  'sub': 'xấu nhất -4,8%',
  'col': (239, 68, 68)},
 {'k': 'bars',
  'ch': 'Chương 4 – Lợi nhuận doanh nghiệp',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, doanh nghiệp phía sau cổ phiếu. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai '
         'mươi sáu, lợi nhuận sau thuế công ty mẹ cao nhất ở quý một năm hai nghìn không trăm hai mươi sáu với khoảng tám nghìn chín trăm chín mươi bốn tỷ, '
         'thấp nhất ở quý bốn năm hai nghìn không trăm hai mươi bốn với khoảng hai nghìn tám trăm linh chín tỷ, và có bốn quý tăng so với quý liền trước. Bốn '
         'quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt ba nghìn tám trăm sáu mươi bốn tỷ, quý một năm hai nghìn không trăm hai '
         'mươi sáu đạt tám nghìn chín trăm chín mươi bốn tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt sáu nghìn ba trăm bảy mươi mốt tỷ, quý ba năm '
         'hai nghìn không trăm hai mươi sáu đạt tám nghìn hai trăm mười bảy tỷ. Lũy kế chín tháng đạt hai mươi ba nghìn năm trăm tám mươi hai tỷ, tăng một '
         'trăm linh ba phẩy năm phần trăm. Tích sản bằng cổ phiếu là góp vốn vào một doanh nghiệp, nên lợi nhuận doanh nghiệp tăng đều qua nhiều năm mới là '
         'động cơ thật của giá cổ phiếu. Góp đều chỉ giúp làm mượt giá mua.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 2808.6, (56, 189, 248), '2.809'),
           ('Q1/25', 3344.3, (56, 189, 248), '3.344'),
           ('Q2/25', 4256.5, (56, 189, 248), '4.256'),
           ('Q3/25', 3988.3, (56, 189, 248), '3.988'),
           ('Q4/25', 3864.1, (56, 189, 248), '3.864'),
           ('Q1/26', 8994.0, (56, 189, 248), '8.994'),
           ('Q2/26', 6371.0, (56, 189, 248), '6.371'),
           ('Q3/26', 8217.3, (34, 197, 94), '8.217')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá hôm nay',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'HÔM NAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, định giá hôm nay. HPG có P trên E khoảng sáu phẩy năm mươi hai lần, P trên B khoảng một phẩy hai mươi lần, ROE khoảng mười chín phẩy '
         'chín phần trăm, beta khoảng không phẩy sáu mươi hai. Người tích sản không cần mua ở giá thấp nhất, nhưng nên tránh góp mạnh tay khi định giá đã cao '
         'hơn hẳn mặt bằng lịch sử. Một cách đơn giản là giữ số tiền góp cố định, không tăng tiền góp khi giá tăng nóng. Bảng định giá và báo cáo tài chính '
         'đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '6,52', 'lần'), ('ROE', '19,9%', ''), ('Beta', '0,62', '')]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Quản trị rủi ro khi tích sản',
  'label': '',
  'cap': ('QUẢN TRỊ RỦI RO', 'KHI TÍCH SẢN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, quản trị rủi ro cho người tích sản. Một, không dồn toàn bộ tiền góp vào một mã: nên chia ít nhất ba đến năm mã khác ngành, hoặc kết hợp '
         'quỹ chỉ số. Hai, giữ quỹ dự phòng khoảng sáu tháng chi tiêu bằng tiền gửi trước khi góp, để không phải bán cổ phiếu đúng lúc giá thấp. Ba, mỗi năm '
         'xem lại tỷ trọng một lần: mã nào phình quá ba mươi phần trăm% danh mục thì giảm bớt về mức đã định. Bốn, không dùng vay ký quỹ cho danh mục tích '
         'sản, vì đòn bẩy biến những tháng âm bình thường thành lệnh bán bắt buộc.',
  'moc': True,
  'anh': 'umbrella rain',
  'items': [('Chia 3–5 mã khác ngành', (34, 197, 94)),
            ('Quỹ dự phòng 6 tháng', (34, 197, 94)),
            ('Tái cân bằng mỗi năm', (255, 196, 0)),
            ('Không vay ký quỹ', (239, 68, 68))]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Góp đều cho bền',
  'label': '',
  'cap': ('GÓP ĐỀU', 'CHO BỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, góp đều thế nào cho bền. Một, chọn một ngày cố định mỗi tháng, ví dụ ngày nhận lương, và đặt lệnh theo số tiền đã định, không chờ giá '
         'đẹp. Hai, ghi nhật ký mỗi lần góp: ngày, giá, số cổ phiếu, giá vốn bình quân mới. Ba, đặt quy tắc cho những tháng thị trường giảm mạnh từ trước, ví '
         'dụ vẫn góp đúng số tiền cũ, không dừng và cũng không vay thêm để mua. Bốn, mỗi quý đọc lại kết quả kinh doanh của doanh nghiệp, vì lý do để tiếp tục '
         'góp là doanh nghiệp vẫn tốt, không phải giá vẫn tăng. Những quy tắc nhỏ này giúp anh chị đi qua năm tháng âm như trong ví dụ của HPG mà không phải '
         'quyết định lại từ đầu mỗi lần thị trường biến động.',
  'anh': 'calendar planner',
  'items': [('Ngày cố định mỗi tháng', (34, 197, 94)),
            ('Nhật ký giá vốn', (34, 197, 94)),
            ('Quy tắc tháng giảm mạnh', (255, 196, 0)),
            ('Đọc KQKD mỗi quý', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Tóm lại',
  'label': '',
  'cap': ('TÍCH SẢN', 'TÓM LẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, tóm lại. Góp đều ba mươi bảy tháng vào HPG cho kết quả lãi khoảng không phẩy tám phần trăm, mua một lần cho kết quả lãi khoảng hai mươi '
         'mốt phẩy năm phần trăm. Quá khứ không bảo đảm tương lai, nhưng con số giúp anh chị biết trước mình sẽ phải chịu đựng những gì. Bài viết kèm video và '
         'bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'notebook summary',
  'cards': [('Góp đều', '+0,8%', ''), ('Một lần', '+21,5%', ''), ('Tháng âm', '5', '/37')]},
 {'k': 'end',
  'label': '',
  'cap': ('GÓP ĐỀU HPG', 'LÃI 0,8%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu dùng giá đóng cửa đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu và báo cáo tài chính quý ba năm hai nghìn không trăm hai '
         'mươi sáu. Nếu bắt đầu góp đều từ hôm nay, anh chị chọn một mã, hay chia đều cho nhiều mã?'}]

S['K2_1611A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'ngân hàng có vốn nhà nước – so sánh nhóm',
  'cap': ('VCB +0,1%', 'CTG +28,2%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Video này đặt ba mã ngân hàng có vốn nhà nước cạnh nhau: Vietcombank VCB, BIDV BID, VietinBank CTG. Cùng một nhóm, cùng một quý, nhưng kết quả và '
         'định giá rất khác nhau. Nhóm này còn gánh vai trò hỗ trợ hệ thống, ví dụ Vietcombank nhận chuyển giao bắt buộc CBBank từ tháng mười/hai nghìn không '
         'trăm hai mươi bốn, nên lợi nhuận và cổ tức có thể khác các ngân hàng tư nhân. Em đi qua bốn lớp: lợi nhuận quý ba so với cùng kỳ, lợi nhuận lũy kế '
         'chín tháng, định giá, và rủi ro. Số liệu từ báo cáo quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai '
         'nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'stock market screen',
  'chart': {'sym': 'CTGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 42.84, 'Đỉnh tuần 12/1/26: 42,84', 0.6], [36, 28.4, 'Đáy tuần 20/7/26: 28,40', 1.6], [51, 31.85, 'Tuần 2/11/26: 31,85', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận quý 3 so với cùng kỳ',
  'label': '',
  'cap': ('LÃI QUÝ 3', 'SO CÙNG KỲ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận quý ba so với cùng kỳ. VCB: chín nghìn không trăm ba mươi ba tỷ, tăng không phẩy một phần trăm so với cùng kỳ. BID: tám nghìn '
         'ba trăm ba mươi mốt tỷ, tăng ba mươi chín phẩy chín phần trăm so với cùng kỳ. CTG: mười nghìn tám trăm ba mươi lăm tỷ, tăng hai mươi tám phẩy hai '
         'phần trăm so với cùng kỳ. Cùng một bối cảnh thị trường mà lợi nhuận đi các hướng khác nhau, nghĩa là yếu tố riêng của từng doanh nghiệp quan trọng '
         'không kém yếu tố ngành.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('VCB', 0.1, (34, 197, 94), '+0,1%'), ('BID', 39.9, (34, 197, 94), '+39,9%'), ('CTG', 28.2, (34, 197, 94), '+28,2%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Lũy kế chín tháng',
  'label': '',
  'cap': ('LŨY KẾ', 'CHÍN THÁNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lũy kế chín tháng, để bớt nhiễu của một quý. VCB: ba mươi ba nghìn không trăm ba mươi hai tỷ, tăng hai mươi bốn phẩy bốn phần trăm. BID: '
         'hai mươi ba nghìn hai trăm bảy mươi tám tỷ, tăng hai mươi lăm phẩy năm phần trăm. CTG: ba mươi mốt nghìn bốn trăm chín mươi hai tỷ, tăng ba mươi ba '
         'phẩy tám phần trăm. Khi quý ba và lũy kế chín tháng đi ngược nhau, anh chị nên tìm xem quý ba có khoản bất thường hay nền so sánh đặc biệt không.',
  'anh': 'calendar',
  'cards': [('VCB', '33.032 tỷ', '+24,4%'), ('BID', '23.278 tỷ', '+25,5%'), ('CTG', '31.492 tỷ', '+33,8%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Định giá cả nhóm',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, định giá cả nhóm. VCB có P trên E khoảng mười phẩy bảy mươi lăm lần, P trên B khoảng một phẩy bảy mươi bảy lần, ROE khoảng mười bảy phẩy '
         'sáu phần trăm. BID có P trên E khoảng bảy phẩy mười tám lần, P trên B khoảng một phẩy hai mươi sáu lần, ROE khoảng mười tám phẩy năm phần trăm. CTG '
         'có P trên E khoảng năm phẩy tám mươi mốt lần, P trên B khoảng một phẩy hai mươi lần, ROE khoảng hai mươi hai phẩy năm phần trăm. P trên E thấp nhất '
         'nhóm chưa chắc là rẻ nhất, vì lợi nhuận bốn quý gần nhất có thể đang ở đỉnh chu kỳ. Mã có ROE cao thường được thị trường trả P trên B cao hơn. Bảng '
         'định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'moc': True,
  'anh': 'calculator',
  'cards': [('VCB', 'P/E 10,8', 'ROE 17,6%'), ('BID', 'P/E 7,2', 'ROE 18,5%'), ('CTG', 'P/E 5,8', 'ROE 22,5%')]},
 {'k': 'bars',
  'ch': 'Chương 4 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, giá cách đỉnh năm mươi hai tuần và hệ số beta. VCB thấp hơn đỉnh khoảng hai mươi tám phẩy chín phần trăm, beta không phẩy bảy mươi lăm. '
         'BID thấp hơn đỉnh khoảng ba mươi bảy phẩy hai phần trăm, beta không phẩy chín mươi. CTG thấp hơn đỉnh khoảng hai mươi hai phẩy một phần trăm, beta '
         'không phẩy tám mươi bảy. Mã cách đỉnh càng xa thì người mua ở đỉnh càng cần lãi nhiều mới hòa vốn. Beta dưới một nghĩa là giá thường dao động ít hơn '
         'thị trường chung, nhưng không bảo vệ khỏi rủi ro riêng của doanh nghiệp.',
  'anh': 'mountain peak',
  'bars': [('VCB', -28.9, (239, 68, 68), '−28,9%'), ('BID', -37.2, (239, 68, 68), '−37,2%'), ('CTG', -22.1, (239, 68, 68), '−22,1%')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, rủi ro cần theo dõi. Với VCB, so với quý trước, lợi nhuận giảm ba mươi bảy phẩy chín phần trăm. Với BID, chi phí dự phòng giảm hai mươi '
         'lăm phần trăm đạt một phần lợi nhuận tăng nhờ trích lập ít hơn. Nhóm này còn gánh vai trò hỗ trợ hệ thống, ví dụ Vietcombank nhận chuyển giao bắt '
         'buộc CBBank từ tháng mười/hai nghìn không trăm hai mươi bốn, nên lợi nhuận và cổ tức có thể khác các ngân hàng tư nhân. Vì các mã cùng nhóm thường '
         'biến động cùng chiều khi yếu tố ngành thay đổi, anh chị nên cộng tỷ trọng cả nhóm trong danh mục, và đặt giới hạn cho cả nhóm, không chỉ cho từng '
         'mã.',
  'moc': True,
  'anh': 'warning sign',
  'items': [('VCB: So với quý trước', (239, 68, 68)), ('BID: Chi phí dự phòng giảm −25,0%: ', (239, 68, 68)), ('Giới hạn tỷ trọng cả nhóm', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Từng mã một nét chính',
  'label': '',
  'cap': ('TỪNG MÃ', 'MỘT NÉT CHÍNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, từng mã một nét chính. VCB: Thu nhập lãi thuần, mảng cho vay cốt lõi tăng ba mươi chín phẩy một phần trăm. BID: Lợi nhuận quý tăng ba '
         'mươi chín phẩy chín phần trăm so với cùng kỳ. CTG: Lợi nhuận quý tăng hai mươi tám phẩy hai phần trăm so với cùng kỳ. Những nét chính này chỉ là '
         'điểm bắt đầu; mỗi mã cần được đọc riêng chuỗi tám quý và thuyết minh trước khi đưa vào danh mục.',
  'anh': 'stock list',
  'items': [('VCB: Thu nhập lãi thuần (mảng cho', (34, 197, 94)),
            ('BID: Lợi nhuận quý tăng +39,9% so', (34, 197, 94)),
            ('CTG: Lợi nhuận quý tăng +28,2% so', (34, 197, 94))]},
 {'k': 'bignum',
  'ch': 'Chương 7 – Tỷ trọng cả nhóm',
  'label': '',
  'cap': ('TỶ TRỌNG', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, tỷ trọng cả nhóm, ví dụ bằng số. Bình quân ba mã trong video đang thấp hơn đỉnh năm mươi hai tuần khoảng hai mươi chín phẩy bốn phần '
         'trăm. Giả sử một danh mục đặt bốn mươi phần trăm vào nhóm ngân hàng có vốn nhà nước, chia đều cho các mã, và mua đúng vùng đỉnh. Khi đó riêng nhóm '
         'này đã kéo cả danh mục giảm khoảng mười một phẩy tám phần trăm. Nếu chỉ đặt hai mươi phần trăm, mức kéo giảm còn khoảng năm phẩy chín phần trăm. '
         'Cùng một nhóm cổ phiếu, cùng một diễn biến giá, nhưng kết quả của danh mục khác nhau gấp đôi chỉ vì quyết định tỷ trọng. Đó là lý do quản trị rủi ro '
         'bắt đầu từ tỷ trọng, trước cả việc chọn mã.',
  'moc': True,
  'value': -11.8,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': '40% DANH MỤC VÀO NHÓM',
  'sub': '20% thì còn −5,9%',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước so sánh nhóm',
  'label': '',
  'cap': ('NĂM BƯỚC', 'SO SÁNH NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, cách tự so sánh một nhóm ngành. Một, xếp lợi nhuận quý và lũy kế cạnh nhau. Hai, đặt P trên E, P trên B cạnh ROE. Ba, xem giá cách đỉnh '
         'và beta để biết mức rung lắc. Bốn, ghi rủi ro riêng của từng mã. Năm, quyết định tỷ trọng cho cả nhóm trước, rồi mới chia cho từng mã. Bài viết kèm '
         'video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'items': [('Lãi quý và lũy kế', (34, 197, 94)),
            ('P/E, P/B cạnh ROE', (34, 197, 94)),
            ('Cách đỉnh, beta', (255, 196, 0)),
            ('Rủi ro riêng từng mã', (239, 68, 68)),
            ('Tỷ trọng cả nhóm', (255, 196, 0))]},
 {'k': 'text',
  'ch': 'Chương bổ sung – Lũy kế 9 tháng',
  'label': '',
  'cap': ('LŨY KẾ 9 THÁNG', 'NÓI GÌ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Trước khi kết luận, em đặt thêm các con số lũy kế cạnh nhau, vì một quý có thể bị méo bởi khoản bất thường. Mã VCB. Lợi nhuận sau thuế công ty mẹ '
         'quý ba năm hai nghìn không trăm hai mươi sáu đạt chín nghìn không trăm ba mươi ba tỷ, tăng không phẩy một phần trăm so với cùng kỳ. Lũy kế chín '
         'tháng đạt ba mươi ba nghìn không trăm ba mươi hai tỷ, tăng hai mươi bốn phẩy bốn phần trăm. Thu nhập lãi thuần đạt hai mươi nghìn ba trăm tám mươi '
         'sáu tỷ, tăng ba mươi chín phẩy một phần trăm. Mã BID. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt tám nghìn ba '
         'trăm ba mươi mốt tỷ, tăng ba mươi chín phẩy chín phần trăm so với cùng kỳ. Lũy kế chín tháng đạt hai mươi ba nghìn hai trăm bảy mươi tám tỷ, tăng '
         'hai mươi lăm phẩy năm phần trăm. Thu nhập lãi thuần đạt mười bảy nghìn không trăm năm mươi sáu tỷ, tăng mười hai phẩy bốn phần trăm. Mã CTG. Lợi '
         'nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt mười nghìn tám trăm ba mươi lăm tỷ, tăng hai mươi tám phẩy hai phần trăm '
         'so với cùng kỳ. Lũy kế chín tháng đạt ba mươi mốt nghìn bốn trăm chín mươi hai tỷ, tăng ba mươi ba phẩy tám phần trăm. Thu nhập lãi thuần đạt hai '
         'mươi mốt nghìn tám trăm mười sáu tỷ, tăng hai mươi bảy phần trăm. Nhìn cả chín tháng, anh chị sẽ thấy mã nào tăng trưởng đều, mã nào chỉ có một quý '
         'đột biến. Trong nhóm ngân hàng có vốn nhà nước, một quý đẹp chưa đủ để kết luận; ba quý liên tiếp cùng chiều mới là tín hiệu đáng tin hơn. Ví von '
         'đời thường: một trận thắng đậm chưa nói lên phong độ, cả mùa giải mới nói lên phong độ.',
  'anh': 'financial report'},
 {'k': 'end',
  'label': '',
  'cap': ('VCB +0,1%', 'CTG +28,2%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Trong nhóm này, anh chị theo dõi mã nào, và vì sao?'}]

S['K2_1711A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'thép – so sánh nhóm',
  'cap': ('NKG +154,8%', 'HSG −37,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Video này đặt ba mã thép cạnh nhau: Hòa Phát HPG, Hoa Sen HSG, Thép Nam Kim NKG. Cùng một nhóm, cùng một quý, nhưng kết quả và định giá rất khác '
         'nhau. Giá thép phụ thuộc giá quặng sắt, than cốc và thép nhập khẩu; từ năm hai nghìn không trăm hai mươi lăm Việt Nam áp thuế chống bán phá giá thép '
         'cán nóng nhập từ Trung Quốc và Ấn Độ. Em đi qua bốn lớp: lợi nhuận quý ba so với cùng kỳ, lợi nhuận lũy kế chín tháng, định giá, và rủi ro. Số liệu '
         'từ báo cáo quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'stock market screen',
  'chart': {'sym': 'HPGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[15, 26.51, 'Đỉnh tuần 23/2/26: 26,51', 0.6], [46, 19.6, 'Đáy tuần 28/9/26: 19,60', 1.6], [51, 21.2, 'Tuần 2/11/26: 21,20', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận quý 3 so với cùng kỳ',
  'label': '',
  'cap': ('LÃI QUÝ 3', 'SO CÙNG KỲ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận quý ba so với cùng kỳ. HPG: tám nghìn hai trăm mười bảy tỷ, tăng một trăm linh sáu phần trăm so với cùng kỳ. HSG: năm mươi lăm '
         'tỷ, giảm ba mươi bảy phẩy bốn phần trăm so với cùng kỳ. NKG: một trăm hai mươi sáu tỷ, tăng một trăm năm mươi bốn phẩy tám phần trăm so với cùng kỳ. '
         'Cùng một bối cảnh thị trường mà lợi nhuận đi các hướng khác nhau, nghĩa là yếu tố riêng của từng doanh nghiệp quan trọng không kém yếu tố ngành.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('HPG', 106.0, (34, 197, 94), '+106,0%'), ('HSG', -37.4, (239, 68, 68), '−37,4%'), ('NKG', 154.8, (34, 197, 94), '+154,8%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Lũy kế chín tháng',
  'label': '',
  'cap': ('LŨY KẾ', 'CHÍN THÁNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lũy kế chín tháng, để bớt nhiễu của một quý. HPG: hai mươi ba nghìn năm trăm tám mươi hai tỷ, tăng một trăm linh ba phẩy năm phần trăm. '
         'HSG: năm trăm sáu mươi mốt tỷ, giảm một phẩy năm phần trăm. NKG: hai trăm năm mươi ba tỷ, tăng hai mươi hai phẩy ba phần trăm. Khi quý ba và lũy kế '
         'chín tháng đi ngược nhau, anh chị nên tìm xem quý ba có khoản bất thường hay nền so sánh đặc biệt không.',
  'anh': 'calendar',
  'cards': [('HPG', '23.582 tỷ', '+103,5%'), ('HSG', '561 tỷ', '−1,5%'), ('NKG', '253 tỷ', '+22,3%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Định giá cả nhóm',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, định giá cả nhóm. HPG có P trên E khoảng sáu phẩy năm mươi hai lần, P trên B khoảng một phẩy hai mươi lần, ROE khoảng mười chín phẩy chín '
         'phần trăm. HSG có P trên E khoảng mười bốn phẩy mười hai lần, P trên B khoảng không phẩy bảy mươi bốn lần, ROE khoảng năm phẩy bốn phần trăm. NKG có '
         'P trên E khoảng hai mươi bốn phẩy năm mươi chín lần, P trên B khoảng không phẩy bảy mươi bảy lần, ROE khoảng ba phẩy hai phần trăm. P trên E thấp '
         'nhất nhóm chưa chắc là rẻ nhất, vì lợi nhuận bốn quý gần nhất có thể đang ở đỉnh chu kỳ. Mã có ROE cao thường được thị trường trả P trên B cao hơn. '
         'Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'moc': True,
  'anh': 'calculator',
  'cards': [('HPG', 'P/E 6,5', 'ROE 19,9%'), ('HSG', 'P/E 14,1', 'ROE 5,4%'), ('NKG', 'P/E 24,6', 'ROE 3,2%')]},
 {'k': 'bars',
  'ch': 'Chương 4 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, giá cách đỉnh năm mươi hai tuần và hệ số beta. HPG thấp hơn đỉnh khoảng mười chín phẩy hai phần trăm, beta không phẩy sáu mươi hai. HSG '
         'thấp hơn đỉnh khoảng mười tám phẩy một phần trăm, beta không phẩy bảy mươi. NKG thấp hơn đỉnh khoảng hai mươi hai phẩy năm phần trăm, beta không '
         'phẩy bảy mươi lăm. Mã cách đỉnh càng xa thì người mua ở đỉnh càng cần lãi nhiều mới hòa vốn. Beta dưới một nghĩa là giá thường dao động ít hơn thị '
         'trường chung, nhưng không bảo vệ khỏi rủi ro riêng của doanh nghiệp.',
  'anh': 'mountain peak',
  'bars': [('HPG', -19.2, (239, 68, 68), '−19,2%'), ('HSG', -18.1, (239, 68, 68), '−18,1%'), ('NKG', -22.5, (239, 68, 68), '−22,5%')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, rủi ro cần theo dõi. Với HPG, chi phí lãi vay tăng một trăm mười tám phẩy bốn phần trăm, ăn vào lợi nhuận. Với HSG, lợi nhuận quý giảm '
         'ba mươi bảy phẩy bốn phần trăm so với cùng kỳ. Với NKG, chi phí lãi vay tăng tám mươi ba phần trăm, ăn vào lợi nhuận. Giá thép phụ thuộc giá quặng '
         'sắt, than cốc và thép nhập khẩu; từ năm hai nghìn không trăm hai mươi lăm Việt Nam áp thuế chống bán phá giá thép cán nóng nhập từ Trung Quốc và Ấn '
         'Độ. Vì các mã cùng nhóm thường biến động cùng chiều khi yếu tố ngành thay đổi, anh chị nên cộng tỷ trọng cả nhóm trong danh mục, và đặt giới hạn cho '
         'cả nhóm, không chỉ cho từng mã.',
  'moc': True,
  'anh': 'warning sign',
  'items': [('HPG: Chi phí lãi vay tăng +118,4%', (239, 68, 68)),
            ('HSG: Lợi nhuận quý giảm −37,4% so v', (239, 68, 68)),
            ('NKG: Chi phí lãi vay tăng +83,0%', (239, 68, 68)),
            ('Giới hạn tỷ trọng cả nhóm', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Từng mã một nét chính',
  'label': '',
  'cap': ('TỪNG MÃ', 'MỘT NÉT CHÍNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, từng mã một nét chính. HPG: Lợi nhuận quý tăng một trăm linh sáu phần trăm so với cùng kỳ. HSG: Doanh thu tăng hai mươi bốn phẩy ba phần '
         'trăm. NKG: Lợi nhuận quý tăng một trăm năm mươi bốn phẩy tám phần trăm so với cùng kỳ. Những nét chính này chỉ là điểm bắt đầu; mỗi mã cần được đọc '
         'riêng chuỗi tám quý và thuyết minh trước khi đưa vào danh mục.',
  'anh': 'stock list',
  'items': [('HPG: Lợi nhuận quý tăng +106,0% s', (34, 197, 94)),
            ('HSG: Doanh thu tăng +24,3%', (34, 197, 94)),
            ('NKG: Lợi nhuận quý tăng +154,8% s', (34, 197, 94))]},
 {'k': 'bignum',
  'ch': 'Chương 7 – Tỷ trọng cả nhóm',
  'label': '',
  'cap': ('TỶ TRỌNG', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, tỷ trọng cả nhóm, ví dụ bằng số. Bình quân ba mã trong video đang thấp hơn đỉnh năm mươi hai tuần khoảng hai mươi phần trăm. Giả sử một '
         'danh mục đặt bốn mươi phần trăm vào nhóm thép, chia đều cho các mã, và mua đúng vùng đỉnh. Khi đó riêng nhóm này đã kéo cả danh mục giảm khoảng tám '
         'phần trăm. Nếu chỉ đặt hai mươi phần trăm, mức kéo giảm còn khoảng bốn phần trăm. Cùng một nhóm cổ phiếu, cùng một diễn biến giá, nhưng kết quả của '
         'danh mục khác nhau gấp đôi chỉ vì quyết định tỷ trọng. Đó là lý do quản trị rủi ro bắt đầu từ tỷ trọng, trước cả việc chọn mã.',
  'moc': True,
  'value': -8.0,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': '40% DANH MỤC VÀO NHÓM',
  'sub': '20% thì còn −4,0%',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước so sánh nhóm',
  'label': '',
  'cap': ('NĂM BƯỚC', 'SO SÁNH NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, cách tự so sánh một nhóm ngành. Một, xếp lợi nhuận quý và lũy kế cạnh nhau. Hai, đặt P trên E, P trên B cạnh ROE. Ba, xem giá cách đỉnh '
         'và beta để biết mức rung lắc. Bốn, ghi rủi ro riêng của từng mã. Năm, quyết định tỷ trọng cho cả nhóm trước, rồi mới chia cho từng mã. Bài viết kèm '
         'video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'items': [('Lãi quý và lũy kế', (34, 197, 94)),
            ('P/E, P/B cạnh ROE', (34, 197, 94)),
            ('Cách đỉnh, beta', (255, 196, 0)),
            ('Rủi ro riêng từng mã', (239, 68, 68)),
            ('Tỷ trọng cả nhóm', (255, 196, 0))]},
 {'k': 'text',
  'ch': 'Chương bổ sung – Lũy kế 9 tháng',
  'label': '',
  'cap': ('LŨY KẾ 9 THÁNG', 'NÓI GÌ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Trước khi kết luận, em đặt thêm các con số lũy kế cạnh nhau, vì một quý có thể bị méo bởi khoản bất thường. Mã HPG. Lợi nhuận sau thuế công ty mẹ '
         'quý ba năm hai nghìn không trăm hai mươi sáu đạt tám nghìn hai trăm mười bảy tỷ, tăng một trăm linh sáu phần trăm so với cùng kỳ. Lũy kế chín tháng '
         'đạt hai mươi ba nghìn năm trăm tám mươi hai tỷ, tăng một trăm linh ba phẩy năm phần trăm. Doanh thu thuần đạt sáu mươi hai nghìn hai trăm mười bốn '
         'tỷ, tăng bảy mươi phẩy chín phần trăm. Mã HSG. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt năm mươi lăm tỷ, giảm '
         'ba mươi bảy phẩy bốn phần trăm so với cùng kỳ. Lũy kế chín tháng đạt năm trăm sáu mươi mốt tỷ, giảm một phẩy năm phần trăm. Doanh thu thuần đạt mười '
         'nghìn ba trăm tám mươi bốn tỷ, tăng hai mươi bốn phẩy ba phần trăm. Mã NKG. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi '
         'sáu đạt một trăm hai mươi sáu tỷ, tăng một trăm năm mươi bốn phẩy tám phần trăm so với cùng kỳ. Lũy kế chín tháng đạt hai trăm năm mươi ba tỷ, tăng '
         'hai mươi hai phẩy ba phần trăm. Doanh thu thuần đạt năm nghìn bốn trăm bảy mươi hai tỷ, tăng bốn mươi lăm phần trăm. Nhìn cả chín tháng, anh chị sẽ '
         'thấy mã nào tăng trưởng đều, mã nào chỉ có một quý đột biến. Trong nhóm thép, một quý đẹp chưa đủ để kết luận; ba quý liên tiếp cùng chiều mới là '
         'tín hiệu đáng tin hơn. Ví von đời thường: một trận thắng đậm chưa nói lên phong độ, cả mùa giải mới nói lên phong độ.',
  'anh': 'financial report'},
 {'k': 'end',
  'label': '',
  'cap': ('NKG +154,8%', 'HSG −37,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Trong nhóm này, anh chị theo dõi mã nào, và vì sao?'}]

S['LST_1611A'] = [{'k': 'hook',
  'label': '',
  'cap': ('1,9 TỶ EURO', 'KHÔNG TỒN TẠI?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ngày ngày mười tám tháng sáu năm hai nghìn không trăm hai mươi, công ty thanh toán Wirecard của Đức thông báo kiểm toán viên EY không ký báo cáo tài '
         'chính năm hai nghìn không trăm mười chín, vì không xác minh được khoảng một phẩy chín tỷ euro tiền gửi. Bốn ngày sau, chính Wirecard thừa nhận số '
         'tiền đó nhiều khả năng không hề tồn tại. Ngày ngày hai mươi lăm tháng sáu năm hai nghìn không trăm hai mươi, công ty nộp đơn phá sản. Chỉ bảy ngày, '
         'một thành viên của chỉ số DAX, nhóm ba mươi công ty lớn nhất nước Đức, sụp đổ. Xem hết video, anh chị sẽ biết những dấu hiệu nào đã lộ ra từ nhiều '
         'năm trước, và cách áp dụng chúng khi đọc báo cáo doanh nghiệp Việt Nam.',
  'anh': 'Frankfurt stock exchange',
  'ch': 'Mở đầu',
  'moc': True},
 {'k': 'text',
  'label': '',
  'cap': ('NGÔI SAO', 'CÔNG NGHỆ ĐỨC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Wirecard được thành lập năm một nghìn chín trăm chín mươi chín ở Aschheim, gần Munich, làm dịch vụ xử lý thanh toán thẻ cho các cửa hàng trực tuyến. '
         'Đến tháng chín/hai nghìn không trăm mười tám, Wirecard được đưa vào chỉ số DAX, thay chỗ ngân hàng Commerzbank. Ở thời điểm đỉnh, vốn hóa công ty '
         'khoảng hai mươi bốn tỷ euro, lớn hơn cả Deutsche Bank. Báo chí Đức gọi đây là ngôi sao công nghệ hiếm hoi của châu Âu. Người mua cổ phiếu khi đó tin '
         'vào một câu chuyện rất đẹp: thanh toán số sẽ thay tiền mặt, và Wirecard đứng ở trung tâm của làn sóng đó.',
  'anh': 'Munich skyline',
  'ch': 'Chương 1 – Ngôi sao'},
 {'k': 'text',
  'label': '',
  'cap': ('NHỮNG CẢNH BÁO', 'ĐẦU TIÊN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Cảnh báo không xuất hiện năm hai nghìn không trăm hai mươi. Từ năm hai nghìn không trăm mười lăm, tờ Financial Times đã đặt câu hỏi về kế toán của '
         'Wirecard. Đầu năm hai nghìn không trăm mười chín, tờ báo đăng loạt bài về nghi vấn ghi khống doanh thu ở văn phòng Singapore. Phản ứng của thị '
         'trường lúc đó rất đáng chú ý: cơ quan giám sát tài chính Đức BaFin cấm bán khống cổ phiếu Wirecard trong hai tháng, và lại điều tra chính các nhà '
         'báo. Câu móc giữ cho phần sau: khi cơ quan quản lý đứng về phía công ty, nhà đầu tư nhỏ còn biết tin vào ai?',
  'anh': 'newspaper printing',
  'ch': 'Chương 2 – Cảnh báo'},
 {'k': 'text',
  'label': '',
  'cap': ('BÊN THỨ BA', 'GIỮ TIỀN HỘ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Điểm mấu chốt nằm ở mô hình kinh doanh. Một phần lớn lợi nhuận của Wirecard đến từ các đối tác bên thứ ba ở châu Á, những công ty xử lý giao dịch '
         'thay Wirecard ở các nước mà Wirecard không có giấy phép. Tiền thu được từ các đối tác này được báo cáo là nằm trong tài khoản ủy thác, cuối cùng là '
         'ở hai ngân hàng tại Philippines. Khi kiểm toán hỏi xác nhận, hai ngân hàng này nói các giấy tờ là giả. Ví von đời thường: một cửa hàng báo lãi rất '
         'lớn, nhưng tiền lãi luôn nằm ở nhà người quen giữ hộ, và không ai được xem két.',
  'anh': 'bank vault',
  'ch': 'Chương 3 – Tiền ở đâu'},
 {'k': 'text',
  'label': '',
  'cap': ('KPMG', 'KHÔNG XÁC MINH ĐƯỢC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tháng mười/hai nghìn không trăm mười chín, dưới áp lực, Wirecard thuê KPMG làm kiểm toán đặc biệt. Ngày ngày hai mươi tám tháng tư năm hai nghìn '
         'không trăm hai mươi, KPMG công bố báo cáo: họ không thể xác minh lợi nhuận từ các đối tác bên thứ ba giai đoạn hai nghìn không trăm mười sáu đến hai '
         'nghìn không trăm mười tám, vì không nhận được đủ chứng từ. Cổ phiếu giảm mạnh trong ngày, nhưng nhiều người vẫn tin đây chỉ là chuyện thủ tục. Bài '
         'học thứ nhất: khi một kiểm toán độc lập nói không xác minh được, đó không phải là chuyện thủ tục. Đó là cảnh báo lớn nhất mà một nhà đầu tư nhỏ có '
         'thể đọc được.',
  'anh': 'audit documents',
  'ch': 'Chương 4 – KPMG'},
 {'k': 'text',
  'label': '',
  'cap': ('BẢY NGÀY', 'SỤP ĐỔ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Rồi đến bảy ngày cuối. Ngày ngày mười tám tháng sáu năm hai nghìn không trăm hai mươi, EY không ký báo cáo năm hai nghìn không trăm mười chín, cổ '
         'phiếu giảm hơn sáu mươi phần trăm trong một phiên. Ngày ngày mười chín tháng sáu, tổng giám đốc Markus Braun từ chức. Ngày ngày hai mươi hai tháng '
         'sáu, Wirecard thông báo một phẩy chín tỷ euro nhiều khả năng không tồn tại, Braun bị bắt cùng ngày ở Munich. Giám đốc vận hành Jan Marsalek bỏ trốn '
         'và tới nay vẫn bị truy nã. Ngày ngày hai mươi lăm tháng sáu năm hai nghìn không trăm hai mươi, Wirecard nộp đơn phá sản, trở thành thành viên DAX '
         'đầu tiên vỡ nợ. Cổ phiếu từng có giá trên một trăm chín mươi euro chỉ còn vài euro.',
  'anh': 'police car night',
  'ch': 'Chương 5 – Bảy ngày'},
 {'k': 'text',
  'label': '',
  'cap': ('LỢI NHUẬN', 'KHÔNG THÀNH TIỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đâu là dấu hiệu có thể thấy trên báo cáo? Thứ nhất, lợi nhuận tăng đều nhưng dòng tiền từ hoạt động kinh doanh không đi theo, phần lớn tiền nằm ở '
         'các khoản phải thu và tài khoản ủy thác. Thứ hai, lợi nhuận phụ thuộc vào đối tác mà nhà đầu tư không thể kiểm tra. Thứ ba, công ty phản ứng với câu '
         'hỏi bằng cách tấn công người hỏi, thay vì đưa chứng từ. Câu đúc kết: lợi nhuận là ý kiến, tiền mặt là sự thật.',
  'anh': 'cash flow chart',
  'ch': 'Chương 6 – Dấu hiệu'},
 {'k': 'text',
  'label': '',
  'cap': ('ÁP DỤNG', 'Ở VIỆT NAM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Áp dụng cho cổ phiếu Việt Nam thế nào? Bước một, đặt lợi nhuận sau thuế bốn quý cạnh lưu chuyển tiền thuần từ hoạt động kinh doanh bốn quý. Nếu lợi '
         'nhuận dương liên tục mà dòng tiền kinh doanh âm nhiều năm, phải đọc thuyết minh xem tiền đang nằm ở đâu. Bước hai, xem các khoản phải thu và trả '
         'trước cho người bán có tăng nhanh hơn doanh thu không. Bước ba, đọc trang ý kiến kiểm toán: chấp nhận toàn phần, ngoại trừ, hay từ chối đưa ý kiến. '
         'Bước bốn, xem công ty có đổi kiểm toán liên tục không.',
  'anh': 'Ho Chi Minh City skyline',
  'ch': 'Chương 7 – Áp dụng'},
 {'k': 'text',
  'label': '',
  'cap': ('Ý KIẾN', 'KIỂM TOÁN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ý kiến kiểm toán là trang ngắn nhất nhưng quan trọng nhất của báo cáo năm. Chấp nhận toàn phần là bình thường. Ý kiến ngoại trừ nghĩa là có khoản '
         'mục kiểm toán viên không đồng ý hoặc không đủ bằng chứng, và nhà đầu tư cần đọc rõ khoản đó là bao nhiêu so với vốn chủ sở hữu. Từ chối đưa ý kiến '
         'là mức cảnh báo cao nhất. Ở Việt Nam, cổ phiếu có thể bị đưa vào diện cảnh báo hay kiểm soát nếu báo cáo năm có ý kiến từ chối hoặc trái ngược. Chỉ '
         'năm phút đọc trang này có thể tránh được những năm tháng mắc kẹt.',
  'anh': 'accountant desk',
  'ch': 'Chương 8 – Kiểm toán'},
 {'k': 'text',
  'label': '',
  'cap': ('BẪY HAY GẶP', 'BA NIỀM TIN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba niềm tin đã giữ nhà đầu tư ở lại Wirecard. Một, công ty lớn, nằm trong chỉ số hàng đầu thì không thể gian lận. Hai, cơ quan quản lý đã vào cuộc '
         'thì chắc là an toàn. Ba, giá giảm vì bị bán khống, không phải vì công ty có vấn đề. Cả ba đều sai. Chỉ số chỉ phản ánh vốn hóa, cơ quan quản lý cũng '
         'có thể sai, và giá giảm đôi khi là thị trường đang nói một điều mà báo cáo chưa nói.',
  'anh': 'question marks',
  'ch': 'Chương 9 – Bẫy niềm tin'},
 {'k': 'text',
  'label': '',
  'cap': ('CHECKLIST', 'NĂM DÒNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Checklist năm dòng sau câu chuyện Wirecard. Một, lợi nhuận bốn quý so với dòng tiền kinh doanh bốn quý. Hai, phải thu tăng nhanh hơn doanh thu hay '
         'không. Ba, ý kiến kiểm toán năm gần nhất. Bốn, lợi nhuận có phụ thuộc đối tác khó kiểm chứng không. Năm, công ty trả lời câu hỏi khó bằng số liệu '
         'hay bằng lời. Bảng kiểm tra chất lượng lợi nhuận có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'ch': 'Chương 10 – Checklist'},
 {'k': 'end',
  'label': '',
  'cap': ('1,9 TỶ EURO', 'BÀI HỌC NÀO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Câu chuyện Wirecard theo thông cáo của công ty, báo cáo KPMG và báo chí tài chính hai nghìn không trăm mười chín, hai nghìn không trăm hai mươi. Cần '
         'trao đổi riêng về danh mục: Zalo ba trăm sáu mươi lăm.một trăm tám mươi tám nghìn hai trăm tám mươi sáu. Khi đọc báo cáo một doanh nghiệp Việt Nam, '
         'anh chị đã bao giờ so lợi nhuận với dòng tiền kinh doanh và đọc kỹ ý kiến kiểm toán chưa?'}]

S['LST_1711A'] = [{'k': 'hook',
  'label': '',
  'cap': ('NỢ 300 TỶ USD?', '3 LẰN RANH ĐỎ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Giữa năm hai nghìn không trăm hai mươi mốt, tập đoàn bất động sản Evergrande của Trung Quốc có tổng nợ phải trả khoảng một nghìn chín trăm bảy mươi '
         'tỷ nhân dân tệ, tức là hơn ba trăm tỷ đô la Mỹ, lớn hơn quy mô cả nền kinh tế của nhiều quốc gia. Chỉ vài tháng sau, Evergrande không trả được lãi '
         'trái phiếu đô la Mỹ và bị xếp hạng vỡ nợ. Điều thú vị là cú sụp không bắt đầu bằng một vụ bê bối, mà bằng ba con số đơn giản mà cơ quan quản lý '
         'Trung Quốc đặt ra năm hai nghìn không trăm hai mươi. Xem hết video, anh chị sẽ biết ba con số đó là gì, và tự đo được nó cho các doanh nghiệp bất '
         'động sản Việt Nam.',
  'anh': 'China city skyscrapers',
  'ch': 'Mở đầu',
  'moc': True},
 {'k': 'text',
  'label': '',
  'cap': ('TỪ QUẢNG CHÂU', 'ĐẾN 280 THÀNH PHỐ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Evergrande được ông Hứa Gia Ấn thành lập năm một nghìn chín trăm chín mươi sáu ở Quảng Châu, niêm yết trên sàn Hồng Kông năm hai nghìn không trăm '
         'linh chín. Mô hình rất nhanh: vay tiền mua đất, bán nhà khi chưa xây xong để thu tiền trước, rồi dùng tiền đó mua thêm đất. Đỉnh cao, tập đoàn có '
         'hơn một nghìn ba trăm dự án ở hơn hai trăm tám mươi thành phố, và mở rộng sang cả xe điện, nước khoáng, đội bóng đá. Ví von đời thường: một người '
         'đạp xe càng lúc càng nhanh, vì nếu chậm lại thì xe đổ.',
  'anh': 'construction cranes China',
  'ch': 'Chương 1 – Mô hình'},
 {'k': 'text',
  'label': '',
  'cap': ('TIỀN KHÁCH', 'LÀ NỢ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Điểm then chốt mà nhiều người bỏ qua: tiền khách trả trước khi mua nhà hình thành trong tương lai là một khoản nợ của doanh nghiệp, vì công ty có '
         'nghĩa vụ giao nhà. Khi thị trường tốt, khoản này giống như một nguồn vốn miễn phí. Khi thị trường xấu, khách ngừng mua, dòng tiền vào biến mất, '
         'nhưng nghĩa vụ xây nhà và trả nợ vẫn còn nguyên. Câu móc giữ cho phần sau: chuyện gì xảy ra khi cơ quan quản lý quyết định đếm lại tất cả các khoản '
         'nợ này?',
  'anh': 'unfinished apartment buildings',
  'ch': 'Chương 2 – Tiền trả trước'},
 {'k': 'text',
  'label': '',
  'cap': ('BA LẰN RANH', 'ĐỎ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tháng tám/hai nghìn không trăm hai mươi, cơ quan quản lý Trung Quốc đặt ra ba lằn ranh đỏ cho doanh nghiệp bất động sản. Một, nợ phải trả trừ tiền '
         'khách trả trước, chia cho tổng tài sản trừ tiền khách trả trước, không quá bảy mươi phần trăm. Hai, nợ vay ròng, tức nợ vay trừ tiền mặt, không quá '
         'một trăm phần trăm vốn chủ sở hữu. Ba, tiền mặt phải lớn hơn nợ vay ngắn hạn. Doanh nghiệp vượt cả ba lằn ranh sẽ không được tăng nợ vay. Evergrande '
         'vượt qua cả ba lằn ranh. Cánh cửa vốn đóng lại, và chiếc xe đạp bắt đầu chậm.',
  'anh': 'red line warning',
  'ch': 'Chương 3 – Ba lằn ranh'},
 {'k': 'text',
  'label': '',
  'cap': ('VỠ NỢ', '2021'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Năm hai nghìn không trăm hai mươi mốt diễn ra rất nhanh. Tháng chín, Evergrande lỡ hạn trả lãi trái phiếu đô la Mỹ. Nhà cung cấp và người mua nhà '
         'biểu tình trước trụ sở ở Thâm Quyến. Ngày ngày chín tháng mười hai năm hai nghìn không trăm hai mươi mốt, tổ chức xếp hạng Fitch hạ Evergrande xuống '
         'mức vỡ nợ có giới hạn. Tháng bảy/hai nghìn không trăm hai mươi ba, công ty công bố khoản lỗ cộng dồn hai năm hai nghìn không trăm hai mươi mốt và '
         'hai nghìn không trăm hai mươi hai khoảng năm trăm tám mươi hai tỷ nhân dân tệ. Ngày ngày hai mươi chín tháng một năm hai nghìn không trăm hai mươi '
         'bốn, tòa án Hồng Kông ra lệnh thanh lý tập đoàn. Tháng ba/hai nghìn không trăm hai mươi bốn, cơ quan quản lý chứng khoán Trung Quốc kết luận đơn vị '
         'chính của tập đoàn đã khai khống doanh thu khoảng năm trăm sáu mươi bốn tỷ nhân dân tệ trong hai năm hai nghìn không trăm mười chín và hai nghìn '
         'không trăm hai mươi.',
  'anh': 'courthouse',
  'ch': 'Chương 4 – Vỡ nợ'},
 {'k': 'text',
  'label': '',
  'cap': ('CỔ ĐÔNG', 'MẤT GẦN HẾT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Người chịu thiệt nhiều nhất là cổ đông và người mua nhà. Cổ phiếu Evergrande mất hơn chín mươi chín phần trăm giá trị so với đỉnh năm hai nghìn '
         'không trăm mười bảy, bị ngừng giao dịch từ đầu năm hai nghìn không trăm hai mươi bốn và bị hủy niêm yết năm hai nghìn không trăm hai mươi lăm. Hàng '
         'trăm nghìn người đã trả tiền nhưng chưa nhận nhà. Câu đúc kết: trong cấu trúc vốn, cổ đông đứng cuối hàng. Khi doanh nghiệp vỡ nợ, chủ nợ còn thương '
         'lượng được, còn cổ đông thường chỉ còn lại tờ chứng nhận.',
  'anh': 'empty construction site',
  'ch': 'Chương 5 – Cổ đông'},
 {'k': 'text',
  'label': '',
  'cap': ('ĐO BA LẰN RANH', 'Ở VIỆT NAM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Áp dụng cho Việt Nam. Ba lằn ranh là quy định của Trung Quốc, không phải quy định ở Việt Nam, nhưng là thước đo tham khảo rất tốt. Em tính từ báo '
         'cáo tài chính quý ba/hai nghìn không trăm hai mươi sáu, số liệu ngày ba mươi tháng chín năm hai nghìn không trăm hai mươi sáu. NLG: lằn ranh một '
         'khoảng ba mươi ba phẩy bốn phần trăm, lằn ranh hai khoảng tám phần trăm, lằn ranh ba khoảng hai phẩy hai mươi bốn lần. KDH: lằn ranh một khoảng năm '
         'mươi mốt phẩy bốn phần trăm, lằn ranh hai khoảng năm mươi bảy phần trăm, lằn ranh ba khoảng ba phẩy bảy mươi lăm lần. DXG: lằn ranh một khoảng ba '
         'mươi bốn phẩy hai phần trăm, lằn ranh hai khoảng hai mươi phần trăm, lằn ranh ba khoảng không phẩy sáu mươi bốn lần. Ba doanh nghiệp này đều nằm '
         'trong vùng an toàn theo cả ba thước đo.',
  'anh': 'Ho Chi Minh City apartments',
  'ch': 'Chương 6 – Áp dụng'},
 {'k': 'text',
  'label': '',
  'cap': ('HAI MÃ', 'SÁT LẰN RANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Hai mã khác cho kết quả khác. PDR: lằn ranh một khoảng sáu mươi mốt phẩy một phần trăm, lằn ranh hai khoảng một trăm linh hai phần trăm, lằn ranh ba '
         'khoảng không phẩy ba mươi sáu lần. NVL: lằn ranh một khoảng bảy mươi mốt phẩy tám phần trăm, lằn ranh hai khoảng một trăm linh bốn phần trăm, lằn '
         'ranh ba khoảng không phẩy mười ba lần. Nợ vay ròng của hai doanh nghiệp này đều vượt một trăm phần trăm vốn chủ sở hữu, và tiền mặt thấp hơn nhiều '
         'so với nợ vay ngắn hạn. Điều này không có nghĩa doanh nghiệp sẽ vỡ nợ, vì còn phụ thuộc vào kế hoạch bán hàng, tái cấu trúc nợ và chính sách. Nhưng '
         'nó cho biết biên an toàn mỏng hơn, và nhà đầu tư cần đọc kỹ thuyết minh vay nợ, lịch đáo hạn trái phiếu.',
  'anh': 'financial documents',
  'ch': 'Chương 6 – Áp dụng'},
 {'k': 'text',
  'label': '',
  'cap': ('BẪY HAY GẶP', 'BA CÂU CHUYỆN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba câu chuyện từng giữ nhà đầu tư ở lại Evergrande. Một, quá lớn để sụp đổ. Hai, nhà nước sẽ cứu. Ba, quỹ đất rất lớn, bán đất là trả được nợ. Thực '
         'tế, quỹ đất chỉ có giá khi có người mua, và trong khủng hoảng, ai cũng muốn bán cùng lúc. Câu đúc kết: tài sản trên báo cáo được ghi theo giá gốc, '
         'còn nợ thì được ghi theo đúng số phải trả.',
  'anh': 'land plot aerial',
  'ch': 'Chương 7 – Bẫy hay gặp'},
 {'k': 'text',
  'label': '',
  'cap': ('CHECKLIST', 'BẤT ĐỘNG SẢN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Checklist năm dòng khi đọc một doanh nghiệp bất động sản. Một, tính ba lằn ranh từ bảng cân đối quý mới nhất. Hai, lịch đáo hạn trái phiếu và vay '
         'ngân hàng trong mười hai tháng tới. Ba, dòng tiền kinh doanh có dương không, hay chỉ sống bằng tiền khách trả trước. Bốn, người mua trả tiền trước '
         'đang tăng hay giảm, phản ánh bán hàng mới. Năm, ý kiến kiểm toán. Bảng tính ba lằn ranh có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'ch': 'Chương 8 – Checklist'},
 {'k': 'end',
  'label': '',
  'cap': ('NỢ 300 TỶ USD', 'BÀI HỌC NÀO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Câu chuyện Evergrande theo báo cáo công ty, Fitch, tòa án Hồng Kông và cơ quan quản lý chứng khoán Trung Quốc; số liệu Việt Nam từ báo cáo quý '
         'ba/hai nghìn không trăm hai mươi sáu. Cần trao đổi riêng về danh mục: Zalo ba trăm sáu mươi lăm.một trăm tám mươi tám nghìn hai trăm tám mươi sáu. '
         'Với mã bất động sản anh chị đang theo dõi, anh chị đã thử tính ba lằn ranh từ báo cáo quý gần nhất chưa?'}]

S['Y3_1611A'] = [{'k': 'hook',
  'label': '',
  'cap': ('FED ĐỔI 7 LẦN', 'VN-INDEX RA SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Từ tháng chín/hai nghìn không trăm hai mươi bốn tới tháng mười/hai nghìn không trăm hai mươi sáu, Cục Dự trữ Liên bang Mỹ đã đổi lãi suất bảy lần: '
         'sáu lần giảm và một lần tăng trở lại. Mỗi lần như vậy, mạng xã hội lại đầy những bài viết về dòng tiền ngoại sắp chảy vào hay chảy ra. Em lấy đúng '
         'bảy ngày đó, đo VN Index hai mươi phiên sau. Kết quả: năm lần chỉ số cao hơn, hai lần thấp hơn. Nghe có vẻ như Fed không quan trọng? Xem hết video, '
         'anh chị sẽ thấy Fed tác động theo một đường vòng, và đường vòng đó mới là thứ đáng theo dõi.',
  'anh': 'Federal Reserve building',
  'ch': 'Mở đầu',
  'moc': True,
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'text',
  'label': '',
  'cap': ('LÃI SUẤT FED', 'LÀ GÌ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Lãi suất Fed là mức lãi các ngân hàng Mỹ cho nhau vay qua đêm, do Fed định hướng. Nó giống như giá gốc của đồng đô la Mỹ. Khi Fed tăng lãi suất, cầm '
         'đô la Mỹ gửi ngân hàng Mỹ được trả lãi cao hơn, tiền toàn cầu có xu hướng quay về Mỹ. Khi Fed giảm, tiền dễ đi tìm nơi có lợi suất cao hơn, trong đó '
         'có thị trường mới nổi như Việt Nam. Đầu tháng mười một/hai nghìn không trăm hai mươi ba, lãi suất Fed ở mức năm phẩy hai mươi lăm đến năm phẩy năm '
         'phần trăm, cao nhất trong khoảng hai mươi năm.',
  'anh': 'US dollar bills',
  'ch': 'Chương 1 – Khái niệm'},
 {'k': 'text',
  'label': '',
  'cap': ('BA LẦN GIẢM', 'NĂM 2024'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba lần đổi đầu tiên, năm hai nghìn không trăm hai mươi bốn. Tháng chín/hai nghìn không trăm hai mươi bốn, Fed giảm năm mươi điểm cơ bản về bốn phẩy '
         'bảy mươi lăm đến năm phần trăm, VN Index khoảng một nghìn hai trăm bảy mươi mốt điểm, hai mươi phiên sau một phẩy hai phần trăm. Tháng mười một/hai '
         'nghìn không trăm hai mươi bốn, Fed giảm hai mươi lăm điểm cơ bản về bốn phẩy năm mươi đến bốn phẩy bảy mươi lăm phần trăm, VN Index khoảng một nghìn '
         'hai trăm năm mươi ba điểm, hai mươi phiên sau một phẩy bốn phần trăm. Tháng mười hai/hai nghìn không trăm hai mươi bốn, Fed giảm hai mươi lăm điểm '
         'cơ bản về bốn phẩy hai mươi lăm đến bốn phẩy năm mươi phần trăm, VN Index khoảng một nghìn hai trăm năm mươi lăm điểm, hai mươi phiên sau âm không '
         'phẩy bốn phần trăm. Điều bất ngờ: Fed giảm mạnh không phẩy năm điểm phần trăm ngay lần đầu, nhưng VN Index cuối năm hai nghìn không trăm hai mươi '
         'bốn vẫn quanh một nghìn hai trăm năm mươi điểm, gần như đi ngang. Lý do nằm ở chỗ đô la Mỹ lại mạnh lên, chỉ số DXY lên đỉnh khoảng một trăm mười '
         'ngày mười ba tháng một năm hai nghìn không trăm hai mươi lăm, và tỷ giá đô la Mỹ/VND tăng.',
  'anh': 'stock board Vietnam',
  'ch': 'Chương 2 – Năm 2024'},
 {'k': 'text',
  'label': '',
  'cap': ('BA LẦN GIẢM', 'NĂM 2025'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba lần giảm tiếp theo, năm hai nghìn không trăm hai mươi lăm. Tháng chín/hai nghìn không trăm hai mươi lăm, Fed giảm hai mươi lăm điểm cơ bản về bốn '
         'đến bốn phẩy hai mươi lăm phần trăm, VN Index khoảng một nghìn sáu trăm sáu mươi lăm điểm, hai mươi phiên sau sáu phẩy một phần trăm. Tháng mười/hai '
         'nghìn không trăm hai mươi lăm, Fed giảm hai mươi lăm điểm cơ bản về ba phẩy bảy mươi lăm đến bốn phần trăm, VN Index khoảng một nghìn sáu trăm bảy '
         'mươi điểm, hai mươi phiên sau không phẩy chín phần trăm. Tháng mười hai/hai nghìn không trăm hai mươi lăm, Fed giảm hai mươi lăm điểm cơ bản về ba '
         'phẩy năm mươi đến ba phẩy bảy mươi lăm phần trăm, VN Index khoảng một nghìn sáu trăm chín mươi chín điểm, hai mươi phiên sau mười phẩy năm phần '
         'trăm. Lần này, VN Index đã ở vùng một nghìn sáu trăm sáu mươi lăm đến một nghìn bảy trăm điểm, cao hơn khoảng ba mươi phần trăm so với một năm '
         'trước. Phần tăng lớn nhất lại diễn ra trong những tháng Fed đứng yên, từ tháng tư đến tháng tám/hai nghìn không trăm hai mươi lăm. Câu móc: nếu Fed '
         'không đổi lãi suất mà thị trường vẫn tăng, thì động lực thật nằm ở đâu?',
  'anh': 'Ho Chi Minh City finance',
  'ch': 'Chương 3 – Năm 2025'},
 {'k': 'text',
  'label': '',
  'cap': ('LẦN TĂNG', 'THÁNG 9/2026'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Lần thứ bảy là một lần tăng. Tháng chín/hai nghìn không trăm hai mươi sáu, Fed tăng hai mươi lăm điểm cơ bản về ba phẩy bảy mươi lăm đến bốn phần '
         'trăm, VN Index khoảng một nghìn tám trăm hai mươi ba điểm, hai mươi phiên sau âm sáu phẩy tám phần trăm. Đến kỳ họp ngày hai mươi tám và ngày hai '
         'mươi chín tháng mười năm hai nghìn không trăm hai mươi sáu, Fed giữ nguyên lãi suất ở ba phẩy bảy mươi lăm đến bốn phần trăm, nhưng có hai thành '
         'viên muốn tăng thêm. VN Index đóng cửa ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu khoảng một nghìn bảy trăm hai mươi lăm điểm, '
         'thấp hơn đỉnh khoảng một nghìn chín trăm hai mươi tám điểm. Kỳ họp tiếp theo vào ngày tám và ngày chín tháng mười hai năm hai nghìn không trăm hai '
         'mươi sáu, kèm dự báo kinh tế mới.',
  'anh': 'FOMC meeting',
  'ch': 'Chương 4 – Lần tăng'},
 {'k': 'text',
  'label': '',
  'cap': ('ĐƯỜNG VÒNG 1', 'LỢI SUẤT MỸ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đường vòng thứ nhất là lợi suất trái phiếu Chính phủ Mỹ mười năm, con số các nhà đầu tư lớn dùng để so sánh mọi tài sản. Ba năm trước khoảng bốn '
         'phẩy sáu mươi sáu phần trăm, thấp nhất khoảng ba phẩy sáu mươi hai phần trăm ngày mười sáu tháng chín năm hai nghìn không trăm hai mươi bốn, cao '
         'nhất khoảng năm phẩy ba mươi mốt phần trăm ngày năm tháng mười năm hai nghìn không trăm hai mươi sáu, và ngày sáu tháng mười một năm hai nghìn không '
         'trăm hai mươi sáu khoảng bốn phẩy tám mươi sáu phần trăm. Điểm đáng chú ý: Fed giảm lãi suất sáu lần, nhưng lợi suất mười năm hiện cao hơn ba năm '
         'trước. Lãi suất ngắn hạn do Fed quyết, lãi suất dài hạn do thị trường quyết, và hai thứ này không phải lúc nào cũng đi cùng nhau.',
  'anh': 'US Treasury building',
  'ch': 'Chương 5 – Lợi suất Mỹ'},
 {'k': 'text',
  'label': '',
  'cap': ('ĐƯỜNG VÒNG 2', 'TỶ GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đường vòng thứ hai, và quan trọng nhất với Việt Nam, là tỷ giá. Đầu tháng mười một/hai nghìn không trăm hai mươi ba, đô la Mỹ/VND khoảng hai mươi '
         'bốn nghìn năm trăm hai mươi đồng. Tỷ giá lên đỉnh khoảng hai mươi sáu nghìn bốn trăm hai mươi lăm đồng và ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu về khoảng hai mươi lăm nghìn năm trăm tám mươi đồng. Khi tỷ giá chịu áp lực, Ngân hàng Nhà nước khó hạ lãi suất trong nước, '
         'và đó là thứ ảnh hưởng trực tiếp tới chi phí vốn của doanh nghiệp và sức mua cổ phiếu. Ví von: Fed là thời tiết ở thượng nguồn, còn tỷ giá và lãi '
         'suất trong nước là mực nước ở ngay trước nhà mình.',
  'anh': 'river dam',
  'ch': 'Chương 6 – Tỷ giá'},
 {'k': 'text',
  'label': '',
  'cap': ('ĐƯỜNG VÒNG 3', 'LỢI NHUẬN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đường vòng thứ ba là lợi nhuận doanh nghiệp. Năm hai nghìn không trăm hai mươi lăm, lợi nhuận nhiều ngân hàng và doanh nghiệp lớn tăng hai con số, '
         'và đó là lý do VN Index tăng mạnh cả trong những tháng Fed đứng yên. Câu đúc kết: lãi suất quyết định người ta trả bao nhiêu cho một đồng lợi nhuận, '
         'còn doanh nghiệp quyết định có bao nhiêu đồng lợi nhuận để trả.',
  'anh': 'factory workers Vietnam',
  'ch': 'Chương 7 – Lợi nhuận'},
 {'k': 'text',
  'label': '',
  'cap': ('BẪY HAY GẶP', 'BA KIỂU ĐỌC TIN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba kiểu đọc tin Fed dễ dẫn tới quyết định sai. Một, Fed giảm lãi suất là mua, Fed tăng là bán, như một công tắc. Bảng bảy lần ở trên cho thấy điều '
         'này không đúng. Hai, phản ứng ngay trong đêm Fed họp, khi thị trường Việt Nam còn đóng cửa và tin đã được phản ánh vào giá thế giới. Ba, bỏ qua câu '
         'chữ của Fed về các kỳ tiếp theo, trong khi thị trường thường phản ứng với dự báo nhiều hơn quyết định.',
  'anh': 'newspaper headlines',
  'ch': 'Chương 8 – Bẫy hay gặp'},
 {'k': 'text',
  'label': '',
  'cap': ('CHECKLIST', 'SAU MỖI KỲ HỌP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Checklist sau mỗi kỳ họp Fed. Một, quyết định và tỷ lệ biểu quyết, có ai phản đối không. Hai, lợi suất Mỹ mười năm phản ứng thế nào trong tuần đó. '
         'Ba, chỉ số DXY và tỷ giá đô la Mỹ/đồng. Bốn, lãi suất tiền gửi trong nước có thay đổi không. Năm, quay lại với lợi nhuận quý của các mã mình nắm '
         'giữ. Bảng theo dõi vĩ mô cập nhật hằng ngày có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'ch': 'Chương 9 – Checklist'},
 {'k': 'end',
  'label': '',
  'cap': ('FED ĐỔI LÃI SUẤT', 'ANH CHỊ LÀM GÌ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu Fed, VN Index, lợi suất Mỹ và tỷ giá tới ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Cần trao đổi riêng về danh mục: Zalo '
         'ba trăm sáu mươi lăm.một trăm tám mươi tám nghìn hai trăm tám mươi sáu. Anh chị có điều chỉnh danh mục theo từng lần Fed họp không, hay theo dõi tỷ '
         'giá và lợi nhuận doanh nghiệp là chính?'}]

S['Y3_1711A'] = [{'k': 'hook',
  'label': '',
  'cap': ('KOSPI +102%?', 'CÓ LÚC −44,5%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba năm qua, chỉ số KOSPI của Hàn Quốc tăng khoảng một trăm linh hai phần trăm, từ khoảng hai nghìn năm trăm linh hai điểm lên khoảng năm nghìn không '
         'trăm sáu mươi điểm ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Con số này nghe rất hấp dẫn. Nhưng nếu ai mua ở đỉnh khoảng chín '
         'nghìn một trăm mười lăm điểm ngày hai mươi hai tháng sáu năm hai nghìn không trăm hai mươi sáu, tới ngày sáu tháng mười một năm hai nghìn không trăm '
         'hai mươi sáu họ đang lỗ khoảng bốn mươi bốn phẩy năm phần trăm. Cùng ba năm đó, VN Index tăng khoảng sáu mươi hai phẩy bảy phần trăm, ít hơn, nhưng '
         'mức sụt sâu nhất tính theo giá đóng cửa chỉ khoảng mười tám phẩy một phần trăm. Video này đặt tám tài sản cạnh nhau, đo cả phần thưởng lẫn cái giá '
         'phải trả. Xem hết video, anh chị sẽ có một câu hỏi rất khác khi chọn tài sản.',
  'anh': 'Seoul skyline',
  'ch': 'Mở đầu',
  'moc': True,
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'text',
  'label': '',
  'cap': ('HAI CON SỐ', 'PHẢI ĐI CÙNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Mỗi tài sản em đo hai con số. Con số thứ nhất là lợi nhuận ba năm, từ đầu tháng mười một/hai nghìn không trăm hai mươi ba tới ngày sáu tháng mười '
         'một năm hai nghìn không trăm hai mươi sáu. Con số thứ hai là mức sụt sâu nhất từ đỉnh, tức là nếu không may mua ở đỉnh, anh chị đã từng lỗ trên giấy '
         'bao nhiêu. Con số thứ nhất là thứ người ta khoe. Con số thứ hai là thứ quyết định người ta có giữ nổi hay không. Ví von đời thường: một con đường '
         'đẹp chưa chắc đã dễ đi, phải hỏi thêm nó có bao nhiêu đoạn đèo.',
  'anh': 'mountain road',
  'ch': 'Chương 1 – Hai con số'},
 {'k': 'text',
  'label': '',
  'cap': ('MỸ', 'S&P 500 VÀ NASDAQ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nhóm Mỹ trước. S&P năm trăm tăng khoảng sáu mươi tám phẩy năm phần trăm, sụt sâu nhất khoảng mười tám phẩy chín phần trăm, đoạn sụt đó từ ngày mười '
         'chín tháng hai năm hai nghìn không trăm hai mươi lăm tới ngày tám tháng tư năm hai nghìn không trăm hai mươi lăm. Nasdaq tăng khoảng tám mươi phẩy '
         'hai phần trăm, sụt sâu nhất khoảng hai mươi bốn phẩy ba phần trăm. Nasdaq tăng nhiều hơn nhưng cũng giảm sâu hơn, vì chứa nhiều cổ phiếu công nghệ '
         'có định giá cao. Cả hai cú sụt lớn nhất đều rơi vào cùng một giai đoạn đầu tháng tư/hai nghìn không trăm hai mươi lăm.',
  'anh': 'Wall Street',
  'ch': 'Chương 2 – Mỹ'},
 {'k': 'text',
  'label': '',
  'cap': ('CHÂU Á', 'NHẬT VÀ HÀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nhóm châu Á. Nikkei hai trăm hai mươi lăm tăng khoảng bảy mươi lăm phẩy sáu phần trăm, sụt sâu nhất khoảng hai mươi sáu phẩy ba phần trăm. KOSPI '
         'tăng khoảng một trăm linh hai phẩy hai phần trăm, sụt sâu nhất khoảng bốn mươi bốn phẩy năm phần trăm. KOSPI có một hành trình đặc biệt: từ khoảng '
         'hai nghìn năm trăm linh hai điểm lên đỉnh khoảng chín nghìn một trăm mười lăm điểm ngày hai mươi hai tháng sáu năm hai nghìn không trăm hai mươi '
         'sáu, tức là hơn gấp ba, rồi giảm khoảng bốn mươi bốn phẩy năm phần trăm chỉ trong khoảng bốn tháng. Câu móc: thị trường tăng nhanh nhất cũng thường '
         'là thị trường giảm nhanh nhất.',
  'anh': 'Tokyo stock exchange',
  'ch': 'Chương 3 – Châu Á'},
 {'k': 'text',
  'label': '',
  'cap': ('HÀNG HÓA', 'VÀNG VÀ DẦU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nhóm hàng hóa. vàng tăng khoảng một trăm linh năm phẩy một phần trăm, sụt sâu nhất khoảng hai mươi sáu phẩy bảy phần trăm, từ đỉnh khoảng năm nghìn '
         'ba trăm mười tám đô la Mỹ một ounce ngày hai mươi chín tháng một năm hai nghìn không trăm hai mươi sáu. dầu Brent tăng khoảng mười bốn phẩy tám phần '
         'trăm, sụt sâu nhất khoảng ba mươi chín phẩy năm phần trăm. Dầu Brent là ví dụ rõ nhất cho việc lợi nhuận ba năm không kể hết câu chuyện: điểm đầu và '
         'điểm cuối không cách nhau nhiều, nhưng ở giữa có những đoạn giảm gần bốn mươi phần trăm. Độ biến động năm của dầu khoảng ba mươi chín phẩy tám phần '
         'trăm, cao gấp đôi vàng.',
  'anh': 'gold bars',
  'ch': 'Chương 4 – Hàng hóa'},
 {'k': 'text',
  'label': '',
  'cap': ('BITCOIN', 'PHẦN THƯỞNG VÀ CÁI GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bitcoin tăng khoảng một trăm mười bốn phẩy hai phần trăm, sụt sâu nhất khoảng năm mươi ba phẩy một phần trăm. Bitcoin lên đỉnh khoảng một trăm hai '
         'mươi bốn nghìn bảy trăm năm mươi ba đô la Mỹ ngày sáu tháng mười năm hai nghìn không trăm hai mươi lăm, rồi về khoảng năm mươi tám nghìn năm trăm '
         'năm mươi chín đô la Mỹ ngày ba mươi tháng sáu năm hai nghìn không trăm hai mươi sáu. Độ biến động năm khoảng ba mươi chín phần trăm. Nghĩa là mỗi '
         'đồng lợi nhuận của Bitcoin đi kèm những đoạn đường mà rất ít người giữ nổi, nhất là khi dùng tiền vay.',
  'anh': 'bitcoin coin',
  'ch': 'Chương 5 – Bitcoin'},
 {'k': 'text',
  'label': '',
  'cap': ('VN-INDEX', 'Ở ĐÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'VN Index tăng khoảng sáu mươi hai phẩy bảy phần trăm, sụt sâu nhất khoảng mười tám phẩy một phần trăm, đoạn sụt đó từ ngày mười bảy tháng ba năm hai '
         'nghìn không trăm hai mươi lăm tới ngày chín tháng tư năm hai nghìn không trăm hai mươi lăm. Độ biến động năm khoảng mười tám phẩy hai phần trăm, '
         'thấp hơn Nasdaq, Nikkei, KOSPI và Bitcoin. Điều bất ngờ với nhiều người: trong ba năm này, VN Index không phải là thị trường nhiều sóng gió nhất, '
         'nếu đo bằng giá đóng cửa. Nhưng từng mã riêng lẻ thì khác hẳn, nhiều cổ phiếu Việt Nam có mức sụt trên năm mươi phần trăm trong cùng giai đoạn.',
  'anh': 'Ho Chi Minh City skyline',
  'ch': 'Chương 6 – VN-Index'},
 {'k': 'text',
  'label': '',
  'cap': ('TỶ LỆ', 'THƯỞNG TRÊN ĐAU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Một cách so sánh đơn giản: lấy lợi nhuận ba năm chia cho mức sụt sâu nhất. Con số càng cao, mỗi đơn vị đau đớn mang lại càng nhiều phần thưởng. Tỷ '
         'lệ của VN Index khoảng ba phẩy bốn mươi sáu. Tỷ lệ của S&P năm trăm khoảng ba phẩy sáu mươi hai. Tỷ lệ của Nasdaq khoảng ba phẩy ba mươi. Tỷ lệ của '
         'Nikkei hai trăm hai mươi lăm khoảng hai phẩy tám mươi tám. Tỷ lệ của KOSPI khoảng hai phẩy ba mươi. Tỷ lệ của vàng khoảng ba phẩy chín mươi bốn. Tỷ '
         'lệ của Bitcoin khoảng hai phẩy mười lăm. Không có tài sản nào thắng ở mọi thước đo. Câu đúc kết: lợi nhuận cao nhất chỉ có ý nghĩa nếu anh chị còn ở '
         'đó vào ngày cuối.',
  'anh': 'balance scale',
  'ch': 'Chương 7 – Thưởng trên đau'},
 {'k': 'text',
  'label': '',
  'cap': ('PHÂN BỔ', 'KHÔNG DỒN MỘT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bài học cho phân bổ tài sản. Thứ nhất, các cú sụt không xảy ra cùng lúc: vàng sụt mạnh nhất năm hai nghìn không trăm hai mươi sáu, KOSPI cũng năm '
         'hai nghìn không trăm hai mươi sáu, còn S&P năm trăm và VN Index sụt mạnh nhất tháng tư/hai nghìn không trăm hai mươi lăm. Đặt các tài sản có nhịp '
         'khác nhau cạnh nhau giúp danh mục bớt chao đảo. Thứ hai, tỷ trọng tài sản nhiều biến động như Bitcoin nên nhỏ, để cú sụt năm mươi phần trăm chỉ làm '
         'danh mục mất vài phần trăm. Thứ ba, với nhà đầu tư Việt Nam, rủi ro tỷ giá cũng là một phần của lợi nhuận khi nắm tài sản nước ngoài.',
  'anh': 'portfolio pie chart',
  'ch': 'Chương 8 – Phân bổ'},
 {'k': 'text',
  'label': '',
  'cap': ('BẪY HAY GẶP', 'BA KIỂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba bẫy khi nhìn bảng lợi nhuận ba năm. Một, chọn tài sản tăng nhiều nhất ba năm qua và nghĩ ba năm tới sẽ lặp lại, như mua KOSPI ở vùng đỉnh năm hai '
         'nghìn không trăm hai mươi sáu. Hai, quên mức sụt từ đỉnh, nên đặt tỷ trọng quá lớn. Ba, so sánh mà bỏ quên tỷ giá và chi phí giao dịch khi đầu tư ra '
         'nước ngoài.',
  'anh': 'rear view mirror',
  'ch': 'Chương 9 – Bẫy hay gặp'},
 {'k': 'text',
  'label': '',
  'cap': ('CHECKLIST', 'TRƯỚC KHI CHỌN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Checklist trước khi thêm một tài sản vào danh mục. Một, lợi nhuận ba năm. Hai, mức sụt sâu nhất từ đỉnh. Ba, độ biến động năm. Bốn, tài sản này sụt '
         'vào lúc nào, có trùng với các tài sản mình đang có không. Năm, nếu nó sụt đúng bằng mức sâu nhất trong quá khứ, danh mục của mình mất bao nhiêu phần '
         'trăm. Bảng giá thế giới và hàng hóa cập nhật hằng ngày có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'ch': 'Chương 10 – Checklist'},
 {'k': 'end',
  'label': '',
  'cap': ('TĂNG NHIỀU NHẤT?', 'HAY GIỮ ĐƯỢC LÂU?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu giá đóng cửa ngày tám tài sản từ tháng mười một/hai nghìn không trăm hai mươi ba đến ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu, quá khứ không bảo đảm cho tương lai. Cần trao đổi riêng về danh mục: Zalo ba trăm sáu mươi lăm.một trăm tám mươi tám nghìn hai trăm tám '
         'mươi sáu. Nếu được chọn lại ba năm trước, anh chị chọn tài sản tăng nhiều nhất hay tài sản mình đủ bình tĩnh để giữ suốt ba năm?'}]

