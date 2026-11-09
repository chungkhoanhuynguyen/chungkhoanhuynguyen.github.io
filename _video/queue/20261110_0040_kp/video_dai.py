# -*- coding: utf-8 -*-
# VIDEO DÀI – NV1 soạn 8/11/2026 (lô 20261110_0040_kp: HI1811A, Y2_1811A, TS1811A, K2_1811A, LST_1811A, Y3_1811A). Kênh phụ 18/11. Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['HI1811A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'PVD – định giá nhanh',
  'cap': ('PVD P/E 17,5', 'ROE 5,2%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'PV Drilling, mã PVD, đang giao dịch quanh mười bảy phẩy hai mươi nghìn đồng, P trên E khoảng mười bảy phẩy năm mươi ba lần, P trên B khoảng không '
         'phẩy chín mươi hai lần, ROE khoảng năm phẩy hai phần trăm. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt bảy mươi '
         'mốt tỷ, giảm bảy mươi bốn phẩy năm phần trăm so với cùng kỳ. Rẻ thật, đắt thật, hay thị trường đang nhìn thấy điều gì khác? Video này em đặt ba con '
         'số định giá cạnh chuỗi lợi nhuận tám quý, cạnh mặt bằng của ngành và cạnh rủi ro, để anh chị tự trả lời. Số liệu từ báo cáo quý ba năm hai nghìn '
         'không trăm hai mươi sáu và dữ liệu tổng hợp ngày chín tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'offshore drilling rig',
  'chart': {'sym': 'PVDW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[15, 27.26, 'Đỉnh tuần 2/3/26: 27,26', 0.6], [5, 14.11, 'Đáy tuần 15/12/25: 14,11', 1.6], [51, 17.2, 'Tuần 9/11/26: 17,20', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Ba con số định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, ba con số định giá nghĩa là gì với PVD. P trên E mười bảy phẩy năm mươi ba lần nghĩa là với lợi nhuận mỗi cổ phiếu bốn quý gần nhất '
         'khoảng chín trăm bảy mươi sáu đồng, người mua đang trả khoảng mười bảy phẩy năm mươi ba đồng giá cho mỗi đồng lợi nhuận. Nói cách khác, nếu lợi '
         'nhuận đứng yên, phải khoảng mười tám năm lợi nhuận mới bằng giá mua. P trên B không phẩy chín mươi hai lần nghĩa là giá đang gấp không phẩy chín '
         'mươi hai lần giá trị sổ sách mỗi cổ phiếu, khoảng mười tám nghìn năm trăm hai mươi sáu đồng. ROE năm phẩy hai phần trăm cho biết mỗi một trăm đồng '
         'vốn chủ sở hữu tạo ra khoảng năm phẩy hai đồng lợi nhuận một năm. Ba con số này liên kết với nhau: P trên E nhân ROE xấp xỉ bằng P trên B.',
  'moc': True,
  'anh': 'calculator',
  'cards': [('P/E', '17,53', 'lần'), ('P/B', '0,92', 'lần'), ('ROE', '5,2%', 'năm')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lợi nhuận tám quý, gốc của chữ E trong P trên E. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn '
         'không trăm hai mươi sáu, lợi nhuận sau thuế công ty mẹ cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng ba trăm sáu mươi lăm tỷ, '
         'thấp nhất ở quý ba năm hai nghìn không trăm hai mươi sáu với khoảng bảy mươi mốt tỷ, và có ba quý tăng so với quý liền trước. Bốn quý gần nhất lần '
         'lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt ba trăm sáu mươi lăm tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt ba trăm linh '
         'sáu tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt một trăm sáu mươi ba tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt bảy mươi mốt tỷ. '
         'Lũy kế chín tháng đạt năm trăm bốn mươi tỷ, giảm mười chín phẩy bốn phần trăm. Nếu lợi nhuận bốn quý gần nhất có một quý đột biến tăng hoặc một quý '
         'lỗ, P trên E hiện tại sẽ không phản ánh đúng sức kiếm tiền bình thường. Khi đó, cách an toàn hơn là tính P trên E trên lợi nhuận trung bình nhiều '
         'quý.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 219.6, (56, 189, 248), '220'),
           ('Q1/25', 152.9, (56, 189, 248), '153'),
           ('Q2/25', 239.7, (56, 189, 248), '240'),
           ('Q3/25', 278.2, (56, 189, 248), '278'),
           ('Q4/25', 364.8, (56, 189, 248), '365'),
           ('Q1/26', 306.2, (56, 189, 248), '306'),
           ('Q2/26', 163.3, (56, 189, 248), '163'),
           ('Q3/26', 70.9, (34, 197, 94), '71')]},
 {'k': 'cards',
  'ch': 'Chương 3 – So với ngành',
  'label': '',
  'cap': ('SO VỚI', 'CÙNG NGÀNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, so với ngành. So với ngành giúp tránh một sai lầm phổ biến: thấy P trên E thấp hơn mã khác ngành rồi kết luận là rẻ. Mỗi ngành có chu kỳ, '
         'rủi ro và tốc độ tăng trưởng khác nhau, nên mặt bằng định giá cũng khác nhau. Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang '
         'chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'moc': True,
  'anh': 'comparison chart',
  'cards': [('P/E PVD', '17,53', 'trung vị 0,00'), ('P/B PVD', '0,92', 'trung vị 0,00'), ('ROE PVD', '5,2%', 'trung vị 0,0%')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Điểm tốt và điểm cần soi',
  'label': '',
  'cap': ('ĐIỂM TỐT', 'ĐIỂM CẦN SOI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, điểm tốt và điểm cần soi. Điểm tốt: Doanh thu tăng hai mươi lăm phần trăm. Điểm cần soi: Lợi nhuận quý giảm bảy mươi bốn phẩy năm phần '
         'trăm so với cùng kỳ. So với quý trước, lợi nhuận giảm năm mươi sáu phẩy sáu phần trăm. Biên lợi nhuận gộp mười hai phẩy tám phần trăm, cùng kỳ hai '
         'mươi ba phẩy bảy phần trăm, thu hẹp. Một định giá chỉ có ý nghĩa khi đặt cạnh câu hỏi: lợi nhuận năm tới cao hơn hay thấp hơn năm nay? Nếu lợi nhuận '
         'đi xuống, P trên E thấp hôm nay sẽ thành P trên E cao vào năm sau.',
  'anh': 'magnifying glass',
  'items': [('Doanh thu tăng +25,0%', (34, 197, 94)),
            ('Lợi nhuận quý giảm −74,5% so với cùng kỳ', (239, 68, 68)),
            ('So với quý trước', (239, 68, 68)),
            ('Biên lợi nhuận gộp 12,8% (cùng kỳ 23,7%)', (239, 68, 68))]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Giá và đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá trong năm mươi hai tuần. Đỉnh khoảng hai mươi sáu phẩy chín mươi sáu nghìn đồng, đáy khoảng mười bốn phẩy mười bốn nghìn đồng, giá '
         'hiện tại thấp hơn đỉnh khoảng ba mươi sáu phẩy hai phần trăm. Người mua ở đỉnh cần lãi khoảng năm mươi bảy phần trăm mới hòa vốn. Giá giảm có thể '
         'làm định giá rẻ đi, nhưng cũng có thể là thị trường đang đi trước một quý lợi nhuận xấu. Vì vậy, khi thấy một mã rẻ đi nhanh, anh chị hãy tìm lý do '
         'trước khi tìm điểm mua.',
  'value': -36.2,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 52 TUẦN 26,96',
  'sub': 'giá 17,20',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro và vị thế',
  'label': '',
  'cap': ('RỦI RO', 'VÀ VỊ THẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi và cách giữ vị thế. Beta của PVD khoảng không phẩy bảy mươi bốn. Tỷ lệ sở hữu nước ngoài khoảng tám phẩy hai phần '
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
         'không. Bốn, quên rằng ROE rất cao có thể đến từ vốn chủ sở hữu mỏng sau nhiều năm lỗ, hoặc từ nợ vay lớn. Với PVD, ROE khoảng năm phẩy hai phần trăm '
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
         'mua. Bảng tóm tắt gồm: P trên E mười bảy phẩy năm mươi ba lần, P trên B không phẩy chín mươi hai lần, ROE năm phẩy hai phần trăm, giá thấp hơn đỉnh '
         'năm mươi hai tuần khoảng ba mươi sáu phẩy hai phần trăm. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm '
         'com.',
  'anh': 'notebook summary',
  'cards': [('P/E', '17,53', 'lần'), ('ROE', '5,2%', ''), ('Cách đỉnh', '−36,2%', '52 tuần')]},
 {'k': 'end',
  'label': '',
  'cap': ('PVD P/E 17,5', 'RẺ HAY ĐẮT?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày chín tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Anh chị xếp PVD vào nhóm rẻ, hợp lý hay đắt, và vì sao?'}]

S['Y2_1811A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'PVT – soi BCTC',
  'cap': ('LÃI QUÝ 3 +42,4%', '9 THÁNG +64,6%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'PV Trans, mã PVT. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt ba trăm bảy mươi lăm tỷ, tăng bốn mươi hai phẩy bốn '
         'phần trăm so với cùng kỳ. Lũy kế chín tháng đạt một nghìn hai trăm bảy mươi ba tỷ, tăng sáu mươi bốn phẩy sáu phần trăm. Quý này nhìn từ báo cáo kết '
         'quả kinh doanh thì đã rõ, nhưng báo cáo tài chính có ba phần, và phần ít người đọc nhất là bảng cân đối kế toán và lưu chuyển tiền tệ. Video này em '
         'soi cả ba phần: lợi nhuận đến từ đâu, tiền có về thật không, và doanh nghiệp đang dùng bao nhiêu nợ. Số liệu từ báo cáo quý ba năm hai nghìn không '
         'trăm hai mươi sáu và dữ liệu tổng hợp ngày chín tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'oil tanker ship',
  'chart': {'sym': 'PVTW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 29.73, 'Đỉnh tuần 9/3/26: 29,73', 0.6], [0, 15.64, 'Đáy tuần 10/11/25: 15,64', 1.6], [51, 20.6, 'Tuần 9/11/26: 20,60', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý hai năm hai nghìn không trăm hai mươi sáu với khoảng năm trăm bảy mươi chín tỷ, thấp nhất ở quý bốn năm hai '
         'nghìn không trăm hai mươi bốn với khoảng hai trăm linh chín tỷ, và có năm quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm '
         'hai nghìn không trăm hai mươi lăm đạt hai trăm sáu mươi sáu tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt ba trăm mười chín tỷ, quý hai năm '
         'hai nghìn không trăm hai mươi sáu đạt năm trăm bảy mươi chín tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt ba trăm bảy mươi lăm tỷ. Chuỗi tám '
         'quý giúp tách phần lợi nhuận đều đặn khỏi những quý đột biến.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 209.1, (56, 189, 248), '209'),
           ('Q1/25', 215.1, (56, 189, 248), '215'),
           ('Q2/25', 294.8, (56, 189, 248), '295'),
           ('Q3/25', 263.4, (56, 189, 248), '263'),
           ('Q4/25', 265.9, (56, 189, 248), '266'),
           ('Q1/26', 319.0, (56, 189, 248), '319'),
           ('Q2/26', 578.7, (56, 189, 248), '579'),
           ('Q3/26', 375.1, (34, 197, 94), '375')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Biên lợi nhuận gộp',
  'label': '',
  'cap': ('BIÊN LỢI NHUẬN', 'GỘP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, biên lợi nhuận gộp. Theo báo cáo, biên gộp quý ba năm hai nghìn không trăm hai mươi sáu khoảng mười bốn phẩy một phần trăm, quý trước '
         'khoảng mười bảy phẩy tám phần trăm, cùng kỳ năm trước khoảng mười ba phẩy hai phần trăm. Bình quân tám quý khoảng mười lăm phẩy năm phần trăm. Doanh '
         'thu thuần đạt năm nghìn sáu trăm mười tỷ, tăng hai mươi sáu phẩy chín phần trăm. Biên gộp là tấm đệm đầu tiên của lợi nhuận. Khi biên co lại, doanh '
         'nghiệp phải bán nhiều hơn chỉ để giữ nguyên lợi nhuận, và mọi chi phí cố định như lãi vay, khấu hao, lương sẽ chiếm phần lớn hơn.',
  'moc': True,
  'anh': 'profit margin',
  'bars': [('Q4/24', 17.612314848818706, (56, 189, 248), '17,6'),
           ('Q1/25', 17.677003047141067, (56, 189, 248), '17,7'),
           ('Q2/25', 13.822288178824838, (56, 189, 248), '13,8'),
           ('Q3/25', 13.216726252432458, (56, 189, 248), '13,2'),
           ('Q4/25', 15.199927994419566, (56, 189, 248), '15,2'),
           ('Q1/26', 14.675253166072155, (56, 189, 248), '14,7'),
           ('Q2/26', 17.750524447313214, (56, 189, 248), '17,8'),
           ('Q3/26', 14.149480401418868, (34, 197, 94), '14,1')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Nợ vay',
  'label': '',
  'cap': ('NỢ VAY', 'VÀ LÃI VAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, nợ vay. Cuối quý ba năm hai nghìn không trăm hai mươi sáu, tổng vay ngắn hạn và dài hạn khoảng sáu nghìn chín trăm sáu mươi bốn tỷ, vốn '
         'chủ sở hữu khoảng mười hai nghìn tám trăm sáu mươi ba tỷ, tức nợ vay bằng khoảng không phẩy năm mươi bốn lần vốn chủ. Một năm trước, tỷ lệ này '
         'khoảng không phẩy năm mươi bảy lần. Chi phí lãi vay quý này khoảng một trăm mười bảy tỷ, cùng kỳ khoảng một trăm linh bảy tỷ. Tiền và tương đương '
         'tiền cuối kỳ khoảng hai nghìn không trăm sáu mươi tỷ. Nợ vay không xấu nếu tiền vay tạo ra lợi nhuận cao hơn lãi phải trả. Nhưng nợ làm lợi nhuận '
         'nhạy hơn: khi kinh doanh tốt, lãi tăng nhanh; khi kinh doanh xấu, lãi vay vẫn phải trả đủ.',
  'anh': 'bank loan',
  'cards': [('Nợ vay', '≈ 6.964 tỷ', ''), ('Nợ vay / vốn chủ', '0,54 lần', ''), ('Lãi vay quý', '≈ 117 tỷ', '')]},
 {'k': 'bars',
  'ch': 'Chương 4 – Dòng tiền kinh doanh',
  'label': '',
  'cap': ('DÒNG TIỀN', 'KINH DOANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, tiền có về thật không. Bốn quý gần nhất, lợi nhuận sau thuế cộng lại khoảng một nghìn năm trăm ba mươi chín tỷ, dòng tiền thuần từ hoạt '
         'động kinh doanh cộng lại khoảng ba nghìn sáu trăm sáu mươi hai tỷ. Từng quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt '
         'chín trăm hai mươi sáu tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt sáu trăm bảy mươi sáu tỷ, quý hai năm hai nghìn không trăm hai mươi sáu '
         'đạt một nghìn một trăm mười hai tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt chín trăm bốn mươi bảy tỷ. Hàng tồn kho cuối kỳ khoảng bốn trăm '
         'ba mươi tỷ, khoản phải thu ngắn hạn khoảng hai nghìn ba trăm mười sáu tỷ, so với một năm trước lần lượt khoảng ba trăm linh bốn tỷ và hai nghìn một '
         'trăm hai mươi lăm tỷ. Nếu phải thu và tồn kho tăng nhanh hơn doanh thu, lợi nhuận đang được ghi nhận trước khi tiền về. Điều đó chưa phải là sai, '
         'nhưng anh chị cần theo dõi xem các quý sau tiền có về theo không.',
  'moc': True,
  'anh': 'cash flow',
  'bars': [('Q4/24', 758.3, (34, 197, 94), '758'),
           ('Q1/25', 505.7, (34, 197, 94), '506'),
           ('Q2/25', 617.2, (34, 197, 94), '617'),
           ('Q3/25', 1112.4, (34, 197, 94), '1.112'),
           ('Q4/25', 925.9, (34, 197, 94), '926'),
           ('Q1/26', 676.4, (34, 197, 94), '676'),
           ('Q2/26', 1112.2, (34, 197, 94), '1.112'),
           ('Q3/26', 947.2, (34, 197, 94), '947')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, điểm tốt và rủi ro cần theo dõi. Lợi nhuận quý tăng bốn mươi hai phẩy bốn phần trăm so với cùng kỳ. Doanh thu tăng hai mươi sáu phẩy '
         'chín phần trăm. So với quý trước, lợi nhuận giảm ba mươi lăm phẩy hai phần trăm. Ngoài các dòng trên, rủi ro ngành cũng cần đặt cạnh: giá đầu vào, '
         'nhu cầu của khách hàng và lãi suất. Một doanh nghiệp tốt vẫn có thể có hai, ba quý xấu khi ngành đi xuống.',
  'anh': 'warning sign',
  'items': [('Lợi nhuận quý tăng +42,4% so với cùng kỳ', (34, 197, 94)), ('Doanh thu tăng +26,9%', (34, 197, 94)), ('So với quý trước', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 6 – Định giá và vị thế',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'VÀ VỊ THẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, định giá và vị thế. Giá khoảng hai mươi phẩy sáu mươi nghìn đồng, P trên E khoảng sáu phẩy chín mươi lần, P trên B khoảng một phẩy không '
         'tám lần, ROE khoảng mười hai phẩy chín phần trăm, thấp hơn đỉnh năm mươi hai tuần khoảng hai mươi sáu phẩy hai phần trăm. Khi đã soi đủ ba phần báo '
         'cáo, anh chị hãy quyết định tỷ trọng trước khi quyết định mua: doanh nghiệp càng nhiều nợ hoặc dòng tiền càng thất thường thì tỷ trọng tối đa nên '
         'càng thấp. Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '6,90', 'lần'), ('P/B', '1,08', 'lần'), ('Cách đỉnh', '−26,2%', '52 tuần')]},
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
  'cap': ('LÃI QUÝ 3 +42,4%', '9 THÁNG +64,6%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày chín tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Trong bốn câu hỏi vừa rồi, câu nào anh chị thấy PVT đang trả lời yếu nhất?'}]

S['TS1811A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'VCB – tích sản',
  'cap': ('GÓP ĐỀU VCB', 'LỖ 10,1%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nếu mỗi tháng anh chị góp đều ba triệu đồng vào cổ phiếu VCB của Vietcombank, bắt đầu từ ngày mười tháng mười một năm hai nghìn không trăm hai mươi '
         'ba, thì sau ba mươi bảy tháng, tổng vốn một trăm mười một triệu đồng hôm nay có giá trị khoảng chín mươi chín phẩy bảy triệu đồng, lỗ khoảng mười '
         'phẩy một phần trăm. Còn nếu bỏ hết một trăm mười một triệu một lần ngay tháng đầu, kết quả là khoảng một trăm linh năm triệu, lỗ khoảng năm phẩy bốn '
         'phần trăm. Video này em đi từng bước: giá vốn bình quân, những tháng âm, lợi nhuận doanh nghiệp và cách giữ kỷ luật. Phép tính dùng giá đóng cửa '
         'phiên đầu mỗi tháng, chưa tính cổ tức tiền mặt, phí và thuế.',
  'moc': True,
  'anh': 'piggy bank savings',
  'chart': {'sym': 'VCBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[9, 78.15, 'Đỉnh tuần 12/1/26: 78,15', 0.6], [35, 52.6, 'Đáy tuần 20/7/26: 52,60', 1.6], [51, 53.6, 'Tuần 9/11/26: 53,60', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Hai cách, hai kết quả',
  'label': '',
  'cap': ('HAI CÁCH', 'HAI KẾT QUẢ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, hai cách, hai kết quả. Giá VCB tháng đầu khoảng năm mươi sáu phẩy sáu mươi bốn nghìn đồng, giá ngày chín tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu khoảng năm mươi ba phẩy sáu mươi nghìn đồng. Góp đều cho kết quả chín mươi chín phẩy bảy triệu, mua một lần cho kết quả một '
         'trăm linh năm triệu. Mua một lần thắng khi giá đi lên đều từ đầu kỳ; góp đều thắng khi giá đi xuống rồi mới hồi. Điều quan trọng không phải cách nào '
         'thắng trong quá khứ, mà là cách nào anh chị làm được đều đặn mà không bỏ cuộc giữa chừng. Với người đi làm, góp đều còn có một lợi thế không nằm '
         'trong bảng tính: nó khớp với dòng tiền lương hằng tháng, nên không cần có sẵn một khoản lớn và không cần đoán thời điểm.',
  'moc': True,
  'anh': 'coins jar',
  'cards': [('Tổng vốn', '111 triệu', '37 tháng'), ('Góp đều', '99,7 triệu', '−10,1%'), ('Mua một lần', '105,0 triệu', '−5,4%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Giá trị danh mục theo thời gian',
  'label': '',
  'cap': ('GIÁ TRỊ', 'DANH MỤC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, giá vốn bình quân. Góp đều ba mươi bảy tháng cho giá vốn bình quân khoảng năm mươi chín phẩy sáu mươi lăm nghìn đồng một cổ phiếu, so '
         'với giá hiện tại khoảng năm mươi ba phẩy sáu mươi nghìn đồng. Góp cùng một số tiền mỗi tháng thì tháng giá thấp mua được nhiều cổ phiếu hơn, tháng '
         'giá cao mua được ít hơn, nên giá vốn bình quân thường thấp hơn giá trung bình các tháng. Trong ví dụ này, trung bình cộng giá của ba mươi bảy lần '
         'mua khoảng năm mươi chín phẩy tám mươi hai nghìn đồng, còn giá vốn bình quân thực tế khoảng năm mươi chín phẩy sáu mươi lăm nghìn đồng. Nhưng giá '
         'vốn thấp không tự biến thành lãi: nếu giá cuối kỳ vẫn dưới giá vốn bình quân, danh mục vẫn âm.',
  'anh': 'growth chart',
  'bars': [('07/24', 26.1, (239, 68, 68), '26'),
           ('11/24', 40.6, (34, 197, 94), '41'),
           ('03/25', 52.6, (34, 197, 94), '53'),
           ('07/25', 60.9, (239, 68, 68), '61'),
           ('11/25', 74.0, (239, 68, 68), '74'),
           ('03/26', 90.7, (34, 197, 94), '91'),
           ('07/26', 103.2, (34, 197, 94), '103'),
           ('11/26', 99.7, (239, 68, 68), '100')]},
 {'k': 'bignum',
  'ch': 'Chương 3 – Những tháng âm',
  'label': '',
  'cap': ('NHỮNG THÁNG', 'DANH MỤC ÂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, những tháng âm. Trong ba mươi bảy lần góp, có mười lăm tháng giá trị danh mục thấp hơn số vốn đã bỏ vào. Thời điểm xấu nhất là tháng mười '
         'một năm hai nghìn không trăm hai mươi sáu, danh mục âm khoảng mười phẩy một phần trăm so với vốn. Thời điểm tốt nhất là tháng hai năm hai nghìn '
         'không trăm hai mươi sáu, lãi khoảng mười tám phẩy bảy phần trăm. Đây là phần mà bảng tính thường bỏ qua: người góp đều phải chịu được những tháng âm '
         'liên tiếp mà vẫn tiếp tục góp. Nếu dừng ở đúng tháng xấu nhất, kết quả sẽ khác hẳn con số cuối kỳ.',
  'moc': True,
  'value': 15,
  'fmt': '{:,.0f}',
  'unit': ' tháng',
  'top': 'TRÊN 37 LẦN GÓP',
  'sub': 'xấu nhất -10,1%',
  'col': (239, 68, 68)},
 {'k': 'bars',
  'ch': 'Chương 4 – Lợi nhuận doanh nghiệp',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, doanh nghiệp phía sau cổ phiếu. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai '
         'mươi sáu, lợi nhuận sau thuế công ty mẹ cao nhất ở quý hai năm hai nghìn không trăm hai mươi sáu với khoảng mười bốn nghìn năm trăm bốn mươi hai tỷ, '
         'thấp nhất ở quý bốn năm hai nghìn không trăm hai mươi bốn với khoảng tám nghìn năm trăm sáu mươi lăm tỷ, và có năm quý tăng so với quý liền trước. '
         'Bốn quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt tám nghìn sáu trăm hai mươi chín tỷ, quý một năm hai nghìn không trăm '
         'hai mươi sáu đạt chín nghìn bốn trăm năm mươi bảy tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt mười bốn nghìn năm trăm bốn mươi hai tỷ, quý '
         'ba năm hai nghìn không trăm hai mươi sáu đạt chín nghìn không trăm ba mươi ba tỷ. Lũy kế chín tháng đạt ba mươi ba nghìn không trăm ba mươi hai tỷ, '
         'tăng hai mươi bốn phẩy bốn phần trăm. Tích sản bằng cổ phiếu là góp vốn vào một doanh nghiệp, nên lợi nhuận doanh nghiệp tăng đều qua nhiều năm mới '
         'là động cơ thật của giá cổ phiếu. Góp đều chỉ giúp làm mượt giá mua.',
  'anh': 'financial chart',
  'bars': [('Q4/24', 8565.4, (56, 189, 248), '8.565'),
           ('Q1/25', 8696.2, (56, 189, 248), '8.696'),
           ('Q2/25', 8831.9, (56, 189, 248), '8.832'),
           ('Q3/25', 9020.5, (56, 189, 248), '9.020'),
           ('Q4/25', 8629.0, (56, 189, 248), '8.629'),
           ('Q1/26', 9456.6, (56, 189, 248), '9.457'),
           ('Q2/26', 14542.3, (56, 189, 248), '14.542'),
           ('Q3/26', 9033.3, (34, 197, 94), '9.033')]},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá hôm nay',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'HÔM NAY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, định giá hôm nay. VCB có P trên E khoảng mười phẩy bảy mươi lăm lần, P trên B khoảng một phẩy bảy mươi bảy lần, ROE khoảng mười bảy phẩy '
         'sáu phần trăm, beta khoảng không phẩy bảy mươi lăm. Người tích sản không cần mua ở giá thấp nhất, nhưng nên tránh góp mạnh tay khi định giá đã cao '
         'hơn hẳn mặt bằng lịch sử. Một cách đơn giản là giữ số tiền góp cố định, không tăng tiền góp khi giá tăng nóng. Bảng định giá và báo cáo tài chính '
         'đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '10,75', 'lần'), ('ROE', '17,6%', ''), ('Beta', '0,75', '')]},
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
         'góp là doanh nghiệp vẫn tốt, không phải giá vẫn tăng. Những quy tắc nhỏ này giúp anh chị đi qua mười lăm tháng âm như trong ví dụ của VCB mà không '
         'phải quyết định lại từ đầu mỗi lần thị trường biến động.',
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
  'say': 'Chương bảy, tóm lại. Góp đều ba mươi bảy tháng vào VCB cho kết quả lỗ khoảng mười phẩy một phần trăm, mua một lần cho kết quả lỗ khoảng năm phẩy bốn '
         'phần trăm. Quá khứ không bảo đảm tương lai, nhưng con số giúp anh chị biết trước mình sẽ phải chịu đựng những gì. Bài viết kèm video và bảng số có '
         'trong thư viện bài học trên chứng khoán Huy Nguyễn chấm com.',
  'anh': 'notebook summary',
  'cards': [('Góp đều', '−10,1%', ''), ('Một lần', '−5,4%', ''), ('Tháng âm', '15', '/37')]},
 {'k': 'end',
  'label': '',
  'cap': ('GÓP ĐỀU VCB', 'LỖ 10,1%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu dùng giá đóng cửa đến ngày chín tháng mười một năm hai nghìn không trăm hai mươi sáu và báo cáo tài chính quý ba năm hai nghìn không trăm '
         'hai mươi sáu. Nếu bắt đầu góp đều từ hôm nay, anh chị chọn một mã, hay chia đều cho nhiều mã?'}]

S['K2_1811A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'phân bón, hóa chất – so sánh nhóm',
  'cap': ('DCM +31,1%', 'DPM −82,9%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Video này đặt bốn mã phân bón, hóa chất cạnh nhau: Đạm Cà Mau DCM, Đạm Phú Mỹ DPM, Giấy Đông Hải Bến Tre DHC, Nhựa Bình Minh BMP. Cùng một nhóm, '
         'cùng một quý, nhưng kết quả và định giá rất khác nhau. Đạm Cà Mau và Đạm Phú Mỹ cùng sản xuất urê từ khí thiên nhiên, nên giá khí đầu vào, giá urê '
         'thế giới và lịch bảo dưỡng nhà máy có thể làm lợi nhuận từng quý chênh nhau rất xa. Em đi qua bốn lớp: lợi nhuận quý ba so với cùng kỳ, lợi nhuận '
         'lũy kế chín tháng, định giá, và rủi ro. Số liệu từ báo cáo quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày chín tháng mười một '
         'năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'stock market screen',
  'chart': {'sym': 'DCMW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 50.01, 'Đỉnh tuần 9/3/26: 50,01', 0.6], [35, 28.5, 'Đáy tuần 20/7/26: 28,50', 1.6], [51, 30.9, 'Tuần 9/11/26: 30,90', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận quý 3 so với cùng kỳ',
  'label': '',
  'cap': ('LÃI QUÝ 3', 'SO CÙNG KỲ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận quý ba so với cùng kỳ. DCM: bốn trăm ba mươi tỷ, tăng ba mươi mốt phẩy một phần trăm so với cùng kỳ. DPM: bốn mươi tỷ, giảm '
         'tám mươi hai phẩy chín phần trăm so với cùng kỳ. DHC: một trăm bốn mươi chín tỷ, tăng bốn mươi chín phẩy bảy phần trăm so với cùng kỳ. BMP: ba trăm '
         'mười chín tỷ, giảm tám phẩy chín phần trăm so với cùng kỳ. Cùng một bối cảnh thị trường mà lợi nhuận đi các hướng khác nhau, nghĩa là yếu tố riêng '
         'của từng doanh nghiệp quan trọng không kém yếu tố ngành.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('DCM', 31.1, (34, 197, 94), '+31,1%'),
           ('DPM', -82.9, (239, 68, 68), '−82,9%'),
           ('DHC', 49.7, (34, 197, 94), '+49,7%'),
           ('BMP', -8.9, (239, 68, 68), '−8,9%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Lũy kế chín tháng',
  'label': '',
  'cap': ('LŨY KẾ', 'CHÍN THÁNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, lũy kế chín tháng, để bớt nhiễu của một quý. DCM: hai nghìn hai trăm tám mươi hai tỷ, tăng bốn mươi chín phẩy sáu phần trăm. DPM: một '
         'nghìn ba trăm bốn mươi tám tỷ, tăng năm mươi chín phẩy bảy phần trăm. DHC: bốn trăm sáu mươi bốn tỷ, tăng bảy mươi chín phẩy bảy phần trăm. BMP: '
         'chín trăm chín mươi tỷ, tăng hai phẩy bốn phần trăm. Khi quý ba và lũy kế chín tháng đi ngược nhau, anh chị nên tìm xem quý ba có khoản bất thường '
         'hay nền so sánh đặc biệt không.',
  'anh': 'calendar',
  'cards': [('DCM', '2.282 tỷ', '+49,6%'), ('DPM', '1.348 tỷ', '+59,7%'), ('DHC', '464 tỷ', '+79,7%'), ('BMP', '990 tỷ', '+2,4%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Định giá cả nhóm',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, định giá cả nhóm. DCM có P trên E khoảng sáu phẩy hai mươi sáu lần, P trên B khoảng một phẩy bốn mươi ba lần, ROE khoảng hai mươi bốn '
         'phẩy hai phần trăm. DPM có P trên E khoảng tám phẩy bốn mươi bảy lần, P trên B khoảng một phẩy mười tám lần, ROE khoảng mười ba phẩy bảy phần trăm. '
         'DHC có P trên E khoảng sáu phẩy bốn mươi bảy lần, P trên B khoảng một phẩy năm mươi bảy lần, ROE khoảng hai mươi lăm phẩy bốn phần trăm. BMP có P '
         'trên E khoảng tám phẩy chín mươi hai lần, P trên B khoảng ba phẩy năm mươi hai lần, ROE khoảng bốn mươi mốt phẩy một phần trăm. P trên E thấp nhất '
         'nhóm chưa chắc là rẻ nhất, vì lợi nhuận bốn quý gần nhất có thể đang ở đỉnh chu kỳ. Mã có ROE cao thường được thị trường trả P trên B cao hơn. Bảng '
         'định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'moc': True,
  'anh': 'calculator',
  'cards': [('DCM', 'P/E 6,3', 'ROE 24,2%'), ('DPM', 'P/E 8,5', 'ROE 13,7%'), ('DHC', 'P/E 6,5', 'ROE 25,4%'), ('BMP', 'P/E 8,9', 'ROE 41,1%')]},
 {'k': 'bars',
  'ch': 'Chương 4 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, giá cách đỉnh năm mươi hai tuần và hệ số beta. DCM thấp hơn đỉnh khoảng ba mươi bốn phẩy chín phần trăm, beta không phẩy ba mươi tám. '
         'DPM thấp hơn đỉnh khoảng ba mươi chín phẩy bốn phần trăm, beta không phẩy bốn mươi bảy. DHC thấp hơn đỉnh khoảng bảy phẩy tám phần trăm, beta không '
         'phẩy sáu mươi sáu. BMP thấp hơn đỉnh khoảng hai mươi hai phẩy tám phần trăm, beta không phẩy năm mươi hai. Mã cách đỉnh càng xa thì người mua ở đỉnh '
         'càng cần lãi nhiều mới hòa vốn. Beta dưới một nghĩa là giá thường dao động ít hơn thị trường chung, nhưng không bảo vệ khỏi rủi ro riêng của doanh '
         'nghiệp.',
  'anh': 'mountain peak',
  'bars': [('DCM', -34.9, (239, 68, 68), '−34,9%'),
           ('DPM', -39.4, (239, 68, 68), '−39,4%'),
           ('DHC', -7.8, (239, 68, 68), '−7,8%'),
           ('BMP', -22.8, (239, 68, 68), '−22,8%')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, rủi ro cần theo dõi. Với DCM, so với quý trước, lợi nhuận giảm năm mươi chín phẩy sáu phần trăm. Với DPM, lợi nhuận quý giảm tám mươi '
         'hai phẩy chín phần trăm so với cùng kỳ. Với BMP, biên lợi nhuận gộp bốn mươi phẩy ba phần trăm, cùng kỳ bốn mươi bảy phẩy chín phần trăm, thu hẹp. '
         'Đạm Cà Mau và Đạm Phú Mỹ cùng sản xuất urê từ khí thiên nhiên, nên giá khí đầu vào, giá urê thế giới và lịch bảo dưỡng nhà máy có thể làm lợi nhuận '
         'từng quý chênh nhau rất xa. Vì các mã cùng nhóm thường biến động cùng chiều khi yếu tố ngành thay đổi, anh chị nên cộng tỷ trọng cả nhóm trong danh '
         'mục, và đặt giới hạn cho cả nhóm, không chỉ cho từng mã.',
  'moc': True,
  'anh': 'warning sign',
  'items': [('DCM: So với quý trước', (239, 68, 68)),
            ('DPM: Lợi nhuận quý giảm −82,9% so v', (239, 68, 68)),
            ('BMP: Biên lợi nhuận gộp 40,3% (cùng', (239, 68, 68)),
            ('Giới hạn tỷ trọng cả nhóm', (255, 196, 0))]},
 {'k': 'checklist',
  'ch': 'Chương 6 – Từng mã một nét chính',
  'label': '',
  'cap': ('TỪNG MÃ', 'MỘT NÉT CHÍNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, từng mã một nét chính. DCM: Lợi nhuận quý tăng ba mươi mốt phẩy một phần trăm so với cùng kỳ. DPM: Doanh thu thuần đạt bốn nghìn một '
         'trăm hai mươi tám tỷ, tăng mười phẩy bảy phần trăm. DHC: Lợi nhuận quý tăng bốn mươi chín phẩy bảy phần trăm so với cùng kỳ. BMP: Doanh thu thuần '
         'đạt một nghìn bốn trăm sáu mươi ba tỷ, giảm bốn phẩy năm phần trăm. Những nét chính này chỉ là điểm bắt đầu; mỗi mã cần được đọc riêng chuỗi tám quý '
         'và thuyết minh trước khi đưa vào danh mục.',
  'anh': 'stock list',
  'items': [('DCM: Lợi nhuận quý tăng +31,1% so', (34, 197, 94)),
            ('DPM: Doanh thu thuần: 4.128 tỷ (+', (34, 197, 94)),
            ('DHC: Lợi nhuận quý tăng +49,7% so', (34, 197, 94)),
            ('BMP: Doanh thu thuần: 1.463 tỷ (−', (34, 197, 94))]},
 {'k': 'bignum',
  'ch': 'Chương 7 – Tỷ trọng cả nhóm',
  'label': '',
  'cap': ('TỶ TRỌNG', 'CẢ NHÓM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, tỷ trọng cả nhóm, ví dụ bằng số. Bình quân bốn mã trong video đang thấp hơn đỉnh năm mươi hai tuần khoảng hai mươi sáu phẩy hai phần '
         'trăm. Giả sử một danh mục đặt bốn mươi phần trăm vào nhóm phân bón, hóa chất, chia đều cho các mã, và mua đúng vùng đỉnh. Khi đó riêng nhóm này đã '
         'kéo cả danh mục giảm khoảng mười phẩy năm phần trăm. Nếu chỉ đặt hai mươi phần trăm, mức kéo giảm còn khoảng năm phẩy hai phần trăm. Cùng một nhóm '
         'cổ phiếu, cùng một diễn biến giá, nhưng kết quả của danh mục khác nhau gấp đôi chỉ vì quyết định tỷ trọng. Đó là lý do quản trị rủi ro bắt đầu từ tỷ '
         'trọng, trước cả việc chọn mã.',
  'moc': True,
  'value': -10.5,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': '40% DANH MỤC VÀO NHÓM',
  'sub': '20% thì còn −5,2%',
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
  'say': 'Trước khi kết luận, em đặt thêm các con số lũy kế cạnh nhau, vì một quý có thể bị méo bởi khoản bất thường. Mã DCM. Lợi nhuận sau thuế công ty mẹ '
         'quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn trăm ba mươi tỷ, tăng ba mươi mốt phẩy một phần trăm so với cùng kỳ. Lũy kế chín tháng đạt hai '
         'nghìn hai trăm tám mươi hai tỷ, tăng bốn mươi chín phẩy sáu phần trăm. Doanh thu thuần đạt năm nghìn bảy trăm bốn mươi hai tỷ, tăng chín mươi hai '
         'phẩy một phần trăm. Mã DPM. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn mươi tỷ, giảm tám mươi hai phẩy chín '
         'phần trăm so với cùng kỳ. Lũy kế chín tháng đạt một nghìn ba trăm bốn mươi tám tỷ, tăng năm mươi chín phẩy bảy phần trăm. Doanh thu thuần đạt bốn '
         'nghìn một trăm hai mươi tám tỷ, tăng mười phẩy bảy phần trăm. Mã DHC. Lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt '
         'một trăm bốn mươi chín tỷ, tăng bốn mươi chín phẩy bảy phần trăm so với cùng kỳ. Lũy kế chín tháng đạt bốn trăm sáu mươi bốn tỷ, tăng bảy mươi chín '
         'phẩy bảy phần trăm. Doanh thu thuần đạt một nghìn không trăm chín mươi ba tỷ, tăng mười bảy phẩy ba phần trăm. Mã BMP. Lợi nhuận sau thuế công ty mẹ '
         'quý ba năm hai nghìn không trăm hai mươi sáu đạt ba trăm mười chín tỷ, giảm tám phẩy chín phần trăm so với cùng kỳ. Lũy kế chín tháng đạt chín trăm '
         'chín mươi tỷ, tăng hai phẩy bốn phần trăm. Doanh thu thuần đạt một nghìn bốn trăm sáu mươi ba tỷ, giảm bốn phẩy năm phần trăm. Nhìn cả chín tháng, '
         'anh chị sẽ thấy mã nào tăng trưởng đều, mã nào chỉ có một quý đột biến. Trong nhóm phân bón, hóa chất, một quý đẹp chưa đủ để kết luận; ba quý liên '
         'tiếp cùng chiều mới là tín hiệu đáng tin hơn. Ví von đời thường: một trận thắng đậm chưa nói lên phong độ, cả mùa giải mới nói lên phong độ.',
  'anh': 'financial report'},
 {'k': 'end',
  'label': '',
  'cap': ('DCM +31,1%', 'DPM −82,9%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày chín tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu. Trong nhóm này, anh chị theo dõi mã nào, và vì sao?'}]

S['LST_1811A'] = [{'k': 'hook',
  'label': '',
  'cap': ('2 NOBEL VẪN CHÁY?', 'MẤT 4,6 TỶ USD'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Năm một nghìn chín trăm chín mươi bảy, hai nhà kinh tế Myron Scholes và Robert Merton nhận giải Nobel kinh tế cho công trình định giá quyền chọn. Cả '
         'hai đều là thành viên của một quỹ đầu tư ở Mỹ tên là Long-Term Capital Management, gọi tắt là LTCM. Chỉ một năm sau, trong chưa đầy bốn tháng của '
         'năm một nghìn chín trăm chín mươi tám, quỹ này mất khoảng bốn phẩy sáu tỷ đô la Mỹ, và Cục Dự trữ Liên bang New York phải đứng ra gọi các ngân hàng '
         'lớn tới giải cứu. Những bộ óc giỏi nhất phố Wall đã thua vì điều gì? Xem hết video, anh chị sẽ thấy bài học đó áp dụng ngay cho tài khoản vay ký quỹ '
         'ở Việt Nam.',
  'anh': 'Wall Street New York',
  'ch': 'Mở đầu',
  'moc': True},
 {'k': 'text',
  'label': '',
  'cap': ('ĐỘI HÌNH', 'TOÀN NGÔI SAO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'LTCM được thành lập năm một nghìn chín trăm chín mươi bốn bởi John Meriwether, người từng đứng đầu bộ phận kinh doanh trái phiếu của ngân hàng '
         'Salomon Brothers. Đội ngũ gồm các nhà giao dịch giỏi nhất, giáo sư đại học và hai người sau này đoạt Nobel. Mức đầu tư tối thiểu là mười triệu đô la '
         'Mỹ. Những năm đầu, kết quả rất đẹp: sau phí, nhà đầu tư nhận khoảng hai mươi mốt phần trăm năm một nghìn chín trăm chín mươi bốn, khoảng bốn mươi ba '
         'phần trăm năm một nghìn chín trăm chín mươi lăm và khoảng bốn mươi mốt phần trăm năm một nghìn chín trăm chín mươi sáu. Ai cũng muốn góp tiền, và '
         'các ngân hàng lớn sẵn sàng cho quỹ vay với điều kiện rất ưu đãi.',
  'anh': 'Manhattan office tower',
  'ch': 'Chương 1 – Đội hình'},
 {'k': 'text',
  'label': '',
  'cap': ('NHẶT TIỀN LẺ', 'TRƯỚC XE LU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Cách LTCM kiếm tiền nghe rất an toàn. Họ tìm hai loại trái phiếu gần giống nhau nhưng giá chênh lệch một chút, mua cái rẻ, bán khống cái đắt, rồi '
         'chờ hai giá về gần nhau. Mỗi lần chỉ lời một phần rất nhỏ. Để phần nhỏ đó thành lợi nhuận lớn, quỹ phải vay thật nhiều. Đầu năm một nghìn chín trăm '
         'chín mươi tám, LTCM có khoảng bốn phẩy bảy tỷ đô la Mỹ vốn, nhưng vay hơn một trăm hai mươi tỷ đô la Mỹ, tức là đòn bẩy khoảng hai mươi lăm lần. '
         'Giới đầu tư gọi kiểu chiến lược này là nhặt tiền lẻ trước một chiếc xe lu: thường ngày nhặt được đều đều, đến một ngày xe lu chạy tới.',
  'anh': 'steamroller road',
  'ch': 'Chương 2 – Cách kiếm tiền'},
 {'k': 'text',
  'label': '',
  'cap': ('MÔ HÌNH NÓI', 'GẦN NHƯ KHÔNG THỂ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các mô hình của LTCM dựa trên dữ liệu lịch sử. Theo mô hình, khả năng quỹ mất phần lớn vốn trong một năm là cực kỳ nhỏ. Vấn đề là mô hình giả định '
         'các khoản đặt cược không cùng lúc đi ngược. Khi thị trường bình thường, giả định đó đúng. Khi thị trường hoảng loạn, mọi người cùng bán thứ rủi ro '
         'và cùng mua thứ an toàn nhất, nên tất cả các khoản chênh lệch giãn ra một lượt. Mô hình không sai trong những ngày bình thường. Nó sai đúng vào ngày '
         'duy nhất mà nó cần phải đúng.',
  'anh': 'computer code screen',
  'ch': 'Chương 3 – Mô hình'},
 {'k': 'text',
  'label': '',
  'cap': ('17/8/1998', 'NGA VỠ NỢ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ngày ngày mười bảy tháng tám năm một nghìn chín trăm chín mươi tám, nước Nga phá giá đồng rúp và tuyên bố ngừng trả một phần nợ trong nước. Nhà đầu '
         'tư toàn cầu hoảng sợ, đổ tiền vào trái phiếu chính phủ Mỹ, thứ được coi là an toàn nhất. Trái phiếu an toàn tăng giá, trái phiếu kém an toàn hơn '
         'giảm giá, khoảng chênh lệch mà LTCM đặt cược sẽ thu hẹp lại giãn ra mạnh. Chỉ riêng tháng tám/một nghìn chín trăm chín mươi tám, quỹ mất gần một nửa '
         'vốn. Với đòn bẩy hai mươi lăm lần, mỗi một phần trăm đi ngược trên tài sản trở thành khoảng hai mươi lăm phần trăm trên vốn.',
  'anh': 'Moscow Red Square',
  'ch': 'Chương 4 – Cú sốc Nga'},
 {'k': 'text',
  'label': '',
  'cap': ('KHÔNG AI', 'MUA LẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Khi lỗ, LTCM cần bán bớt để giảm nợ. Nhưng cả thị trường biết quỹ đang kẹt, và các khoản đầu tư của quỹ quá lớn so với thanh khoản. Không ai muốn '
         'mua ở giá hợp lý, một số bên còn bán trước để tránh bị kéo theo. Bán không được, giá càng xuống, lỗ càng sâu. Đây là điều mà mọi người dùng đòn bẩy '
         'cần nhớ: thanh khoản có mặt khi mình không cần, và biến mất đúng lúc mình cần nhất. Đến tháng chín/một nghìn chín trăm chín mươi tám, vốn của quỹ '
         'chỉ còn một phần nhỏ so với đầu năm.',
  'anh': 'empty trading floor',
  'ch': 'Chương 5 – Thanh khoản biến mất'},
 {'k': 'text',
  'label': '',
  'cap': ('23/9/1998', '14 NGÂN HÀNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nếu LTCM sụp đổ hỗn loạn, các ngân hàng cho quỹ vay sẽ phải bán tháo tài sản thế chấp cùng lúc, và thị trường trái phiếu có thể đóng băng. Ngày ngày '
         'hai mươi ba tháng chín năm một nghìn chín trăm chín mươi tám, Cục Dự trữ Liên bang New York mời các ngân hàng lớn tới họp. Mười bốn tổ chức góp '
         'khoảng ba phẩy sáu tỷ đô la Mỹ để tiếp quản khoảng chín mươi phần trăm quỹ. Các nhà sáng lập gần như mất trắng phần vốn của mình. Sau đó, Fed giảm '
         'lãi suất ba lần trong mùa thu năm một nghìn chín trăm chín mươi tám để trấn an thị trường. Đầu năm hai nghìn, quỹ được giải thể.',
  'anh': 'Federal Reserve Bank New York',
  'ch': 'Chương 6 – Giải cứu'},
 {'k': 'text',
  'label': '',
  'cap': ('ÁP DỤNG', 'Ở VIỆT NAM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Câu chuyện LTCM giống một tài khoản vay ký quỹ phóng to. Ở Việt Nam, khi anh chị vay để mua cổ phiếu, công ty chứng khoán đặt ngưỡng tỷ lệ ký quỹ. '
         'Thị trường giảm mạnh, tài khoản chạm ngưỡng, và lệnh bán giải chấp được đặt bất kể anh chị tin cổ phiếu đó tốt đến đâu. Khi rất nhiều tài khoản cùng '
         'chạm ngưỡng, lệnh bán dồn dập làm giá giảm sàn, tạo thêm tài khoản chạm ngưỡng mới. Đó chính là vòng xoáy mà LTCM gặp phải, chỉ khác ở quy mô.',
  'anh': 'Ho Chi Minh City stock exchange',
  'ch': 'Chương 7 – Liên hệ Việt Nam'},
 {'k': 'text',
  'label': '',
  'cap': ('BẪY HAY GẶP', 'BA NIỀM TIN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba niềm tin đã đưa LTCM tới bờ vực. Một, người giỏi thì không thể thua lớn. Hai, chuyện chưa từng xảy ra trong dữ liệu thì sẽ không xảy ra. Ba, khi '
         'cần là bán được. Nhà đầu tư cá nhân cũng hay có ba niềm tin này: mình đã thắng nhiều lần nên lần này cũng thắng, cổ phiếu này chưa bao giờ giảm quá '
         'ba mươi phần trăm, và mã này thanh khoản tốt nên lúc nào cũng thoát được. Một mùa thị trường xấu đủ để lật cả ba.',
  'anh': 'chess pieces falling',
  'ch': 'Chương 8 – Bẫy hay gặp'},
 {'k': 'text',
  'label': '',
  'cap': ('CHECKLIST', 'NĂM DÒNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Checklist năm dòng sau câu chuyện LTCM. Một, tính tổng dư nợ vay so với vốn tự có; nếu vượt năm mươi phần trăm thì đã là đòn bẩy cao với người mới. '
         'Hai, tính xem thị trường giảm bao nhiêu phần trăm thì tài khoản chạm ngưỡng bị bán. Ba, đừng dồn vay vào một mã hoặc một ngành, vì khi hoảng loạn '
         'chúng giảm cùng lúc. Bốn, kiểm tra giá trị giao dịch bình quân của mã mình nắm. Năm, luôn để sẵn một phần tiền mặt hoặc kế hoạch giảm nợ, viết ra '
         'trước khi thị trường xấu.',
  'anh': 'checklist clipboard',
  'ch': 'Chương 9 – Checklist'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐÒN BẨY', 'AI ĐANG QUYẾT ĐỊNH?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Câu chuyện LTCM theo báo cáo của Nhóm Công tác về Thị trường Tài chính của Tổng thống Mỹ năm một nghìn chín trăm chín mươi chín và các tài liệu công '
         'khai. Cần trao đổi riêng về danh mục: Zalo ba trăm sáu mươi lăm.một trăm tám mươi tám nghìn hai trăm tám mươi sáu. Nếu thị trường giảm thêm hai mươi '
         'phần trăm ngày mai, tài khoản của anh chị có bị buộc phải bán không, hay anh chị vẫn được tự quyết định?'}]

S['Y3_1811A'] = [{'k': 'hook',
  'label': '',
  'cap': ('MỸ HẮT HƠI,', 'VN CẢM CÚM? 0,37'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Sáng nào chứng khoán Mỹ giảm mạnh, trên mạng lại có câu quen thuộc: Mỹ hắt hơi thì Việt Nam cảm cúm. Em lấy một trăm năm mươi lăm tuần dữ liệu, từ '
         'tháng mười một/hai nghìn không trăm hai mươi ba tới tuần này, so S&P năm trăm và VN Index theo từng tuần. Hệ số tương quan chỉ khoảng không phẩy ba '
         'mươi bảy. Còn bất ngờ hơn: trong năm tuần VN Index giảm sâu nhất, có ba tuần S&P năm trăm chỉ giảm chưa tới hai phẩy một phần trăm. Vậy anh chị nên '
         'lo phố Wall tới mức nào? Xem hết video, anh chị sẽ biết khi nào tin Mỹ đáng để ý, và khi nào nên nhìn vào chính thị trường trong nước.',
  'anh': 'Wall Street New York',
  'ch': 'Mở đầu',
  'moc': True,
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[26, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [0, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1714.32, 'Tuần 9/11/26: 1.714,32', 2.6]]}},
 {'k': 'text',
  'label': '',
  'cap': ('TƯƠNG QUAN', 'LÀ GÌ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tương quan đo mức hai chuỗi số đi cùng chiều. Bằng một là luôn đi cùng nhau, bằng không là không liên quan, bằng âm một là luôn ngược nhau. Con số '
         'khoảng không phẩy ba mươi bảy nghĩa là có liên quan, nhưng lỏng. Nói theo thống kê, chỉ khoảng mười bốn phần trăm biến động tuần của VN Index đi '
         'cùng biến động của S&P năm trăm; phần lớn còn lại đến từ chỗ khác. Ví von đời thường: hai người hàng xóm có khi cùng mở cửa sổ lúc trời nóng, nhưng '
         'phần lớn thời gian mỗi nhà có lịch sinh hoạt riêng.',
  'anh': 'two lines chart',
  'ch': 'Chương 1 – Tương quan'},
 {'k': 'text',
  'label': '',
  'cap': ('KHI MỸ GIẢM', 'TỪ 3% TRỞ LÊN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Trong một trăm năm mươi lăm tuần, S&P năm trăm có bốn tuần giảm từ ba phần trăm trở lên. VN Index giảm cùng tuần ba lần. Lần nặng nhất là tuần bắt '
         'đầu ngày ba mươi mốt tháng ba năm hai nghìn không trăm hai mươi lăm, S&P năm trăm giảm chín phẩy không tám phần trăm, VN Index giảm tám phẩy mười '
         'một phần trăm, đúng tuần thế giới chao đảo vì thuế quan đầu tháng tư/hai nghìn không trăm hai mươi lăm. Nhưng cũng có tuần bắt đầu ngày ba tháng ba '
         'năm hai nghìn không trăm hai mươi lăm, S&P năm trăm giảm ba phẩy mười phần trăm, VN Index tăng một phẩy năm mươi chín phần trăm. Nghĩa là cú giảm '
         'của Mỹ đủ lớn thì thường kéo theo Việt Nam, nhưng không phải lúc nào cũng vậy, và mức giảm ở Việt Nam có khi nhẹ hơn, có khi nặng hơn.',
  'anh': 'stock market crash screen',
  'ch': 'Chương 2 – Khi Mỹ giảm mạnh'},
 {'k': 'text',
  'label': '',
  'cap': ('KHI MỸ TĂNG', 'TỪ 3% TRỞ LÊN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chiều ngược lại thì sao? S&P năm trăm có mười hai tuần tăng từ ba phần trăm trở lên. Trong những tuần đó, VN Index tăng mười lần, giảm hai lần. Mức '
         'tăng của VN Index thường nhỏ hơn mức tăng của Mỹ. Ví dụ tuần bắt đầu ngày bảy tháng tư năm hai nghìn không trăm hai mươi lăm, khi Mỹ tạm hoãn thuế '
         'quan, S&P năm trăm tăng khoảng năm phẩy bảy phần trăm, VN Index chỉ tăng khoảng một phần trăm. Nghĩa là tin tốt từ Mỹ có giúp, nhưng không tự động '
         'kéo VN Index lên cùng biên độ.',
  'anh': 'rising stock chart',
  'ch': 'Chương 3 – Khi Mỹ tăng mạnh'},
 {'k': 'text',
  'label': '',
  'cap': ('NĂM TUẦN', 'TỆ NHẤT CỦA VN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bây giờ đảo câu hỏi: những tuần VN Index giảm sâu nhất, Mỹ làm gì? Tuần tệ nhất, tuần bắt đầu ngày ba mươi mốt tháng ba năm hai nghìn không trăm hai '
         'mươi lăm, S&P năm trăm giảm chín phẩy không tám phần trăm, VN Index giảm tám phẩy mười một phần trăm. Tuần thứ hai, tuần bắt đầu ngày mười lăm tháng '
         'tư năm hai nghìn không trăm hai mươi bốn, S&P năm trăm giảm ba phẩy không năm phần trăm, VN Index giảm bảy phẩy chín mươi bảy phần trăm. Ba tuần còn '
         'lại: tuần bắt đầu ngày hai tháng ba năm hai nghìn không trăm hai mươi sáu, S&P năm trăm giảm hai phẩy không hai phần trăm, VN Index giảm năm phẩy '
         'chín mươi tám phần trăm; tuần bắt đầu ngày hai mươi tháng bảy năm hai nghìn không trăm hai mươi sáu, S&P năm trăm giảm không phẩy sáu mươi mốt phần '
         'trăm, VN Index giảm năm phẩy sáu mươi bảy phần trăm; và tuần bắt đầu ngày tám tháng mười hai năm hai nghìn không trăm hai mươi lăm, S&P năm trăm '
         'giảm không phẩy sáu mươi ba phần trăm, VN Index giảm năm phẩy bốn mươi hai phần trăm. Có ba trên năm tuần, S&P năm trăm gần như đứng yên hoặc chỉ '
         'giảm nhẹ. Lý do của những tuần đó phải tìm ở trong nước: dòng tiền, tỷ giá, vay ký quỹ, tin riêng của các nhóm ngành.',
  'anh': 'Ho Chi Minh City skyline',
  'ch': 'Chương 4 – Tuần tệ nhất'},
 {'k': 'text',
  'label': '',
  'cap': ('RỦI RO', 'NẰM TRONG NƯỚC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Điều này thay đổi cách theo dõi tin tức. Nhiều người dậy sớm xem phố Wall, rồi bỏ qua các con số trong nước như tỷ giá đô la Mỹ trên đồng, lãi suất '
         'liên ngân hàng, dư nợ vay ký quỹ toàn thị trường hay giao dịch của khối ngoại. Theo dữ liệu ba năm qua, chính các yếu tố này mới thường đứng sau '
         'những tuần giảm sâu nhất của VN Index. Phố Wall đáng xem, nhưng nên xếp sau các chỉ số trong nước khi đánh giá rủi ro cho danh mục.',
  'anh': 'Vietnamese dong banknotes',
  'ch': 'Chương 5 – Rủi ro trong nước'},
 {'k': 'text',
  'label': '',
  'cap': ('KÊNH TRUYỀN', 'TỪ MỸ SANG VN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Khi nào thì tin Mỹ thật sự đáng để ý? Tin từ Mỹ truyền sang Việt Nam qua ba kênh chính. Một, lãi suất của Fed và đồng đô la Mỹ: đô la Mỹ mạnh làm áp '
         'lực tỷ giá trong nước tăng, Ngân hàng Nhà nước có thể phải giữ lãi suất cao hơn. Hai, khối ngoại: khi nhà đầu tư toàn cầu hoảng sợ, họ rút tiền khỏi '
         'các thị trường cận biên và mới nổi. Ba, xuất khẩu: Mỹ là thị trường xuất khẩu lớn nhất của Việt Nam, nên tin thuế quan tác động thẳng vào doanh '
         'nghiệp. Cú sốc đi qua cả ba kênh, như tháng tư/hai nghìn không trăm hai mươi lăm, thường mạnh nhất.',
  'anh': 'container port ships',
  'ch': 'Chương 6 – Ba kênh truyền'},
 {'k': 'text',
  'label': '',
  'cap': ('BẪY HAY GẶP', 'BA KIỂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba kiểu bẫy hay gặp. Một, bán vội lúc mở cửa chỉ vì đêm qua Mỹ đỏ, trong khi dữ liệu cho thấy VN Index không luôn đi theo. Hai, mua đuổi vì Mỹ lập '
         'đỉnh mới, quên rằng chênh lệch biên độ giữa hai thị trường rất lớn. Ba, chỉ theo dõi tin quốc tế mà bỏ qua tỷ giá và vay ký quỹ trong nước, chính là '
         'những thứ đứng sau các tuần tệ nhất. Cả ba kiểu đều xuất phát từ một câu nói nghe hợp lý nhưng chưa được kiểm tra bằng số liệu.',
  'anh': 'trap warning sign',
  'ch': 'Chương 7 – Bẫy hay gặp'},
 {'k': 'text',
  'label': '',
  'cap': ('CHECKLIST', 'SÁNG THỨ HAI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Checklist sáng thứ Hai cho người bận rộn. Một, xem S&P năm trăm tuần trước giảm hay tăng bao nhiêu; dưới ba phần trăm thì đừng vội đổi kế hoạch. '
         'Hai, xem tỷ giá đô la Mỹ trên VND và chỉ số đồng đô la Mỹ. Ba, xem khối ngoại mua hay bán ròng tuần trước. Bốn, xem lãi suất liên ngân hàng có tăng '
         'vọt không. Năm, kiểm tra tỷ lệ vay ký quỹ của chính tài khoản mình. Năm dòng này mất khoảng mười phút, nhưng giúp anh chị phân biệt tiếng ồn với rủi '
         'ro thật.',
  'anh': 'checklist clipboard',
  'ch': 'Chương 8 – Checklist'},
 {'k': 'text',
  'label': '',
  'cap': ('BẢNG GHI NHỚ', 'BA CON SỐ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba con số để ghi nhớ. Một, tương quan tuần khoảng không phẩy ba mươi bảy: có liên quan nhưng lỏng. Hai, ba trên bốn tuần Mỹ giảm mạnh, VN Index giảm '
         'theo: cú sốc lớn của Mỹ vẫn cần được tôn trọng. Ba, ba trên năm tuần tệ nhất của VN Index, Mỹ gần như bình yên: rủi ro lớn nhất thường nằm ở nhà '
         'mình. Số liệu ba năm là một mẫu ngắn, chưa có các giai đoạn như năm hai nghìn không trăm linh tám hay hai nghìn không trăm hai mươi hai, nên đây là '
         'cách nhìn, không phải quy luật.',
  'anh': 'notebook pen',
  'ch': 'Chương 9 – Ghi nhớ'},
 {'k': 'end',
  'label': '',
  'cap': ('MỸ HẮT HƠI,', 'ANH CHỊ LÀM GÌ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu S&P năm trăm và VN Index theo tuần tới ngày chín tháng mười một năm hai nghìn không trăm hai mươi sáu, quá khứ không bảo đảm cho tương lai. '
         'Cần trao đổi riêng về danh mục: Zalo ba trăm sáu mươi lăm.một trăm tám mươi tám nghìn hai trăm tám mươi sáu. Sáng nào thấy chứng khoán Mỹ đỏ, anh '
         'chị có thay đổi kế hoạch giao dịch trong ngày không?'}]

