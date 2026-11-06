# -*- coding: utf-8 -*-
# VIDEO DÀI – NV1 soạn 7/11/2026 (lô 20261107_0100_kp: HI1011A, K2_1011A, LST_1011A, TS1011A, Y2_1011A, Y3_1011A, HI1111A, K2_1111A, LST_1111A, TS1111A, Y2_1111A, Y3_1111A). Nến tuần: px_tuan.json. Kênh phụ HI, K2, LST, TS, Y2, Y3 ngày 10–11/11.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['HI1011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'DHC – định giá nhanh',
  'cap': ('DHC: P/E 6,43', 'ROE 25,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'paper packaging factory',
  'say': 'Đông Hải Bến Tre, mã DHC, đang có P trên E khoảng sáu phẩy bốn ba lần, P trên B khoảng một phẩy năm bảy lần, ROE khoảng hai mươi lăm phẩy bốn phần '
         'trăm và tỷ suất cổ tức khoảng năm phẩy không hai phần trăm. Một doanh nghiệp giấy bao bì có hiệu quả vốn cao hơn nhiều ngân hàng, nhưng thị trường '
         'chỉ trả khoảng sáu lần lợi nhuận. Rẻ thật, hay có lý do? Video này em đặt ba con số định giá cạnh chuỗi lợi nhuận tám quý, biên gộp và rủi ro, để '
         'anh chị tự trả lời. Số liệu từ báo cáo quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không '
         'trăm hai mươi sáu.',
  'chart': {'sym': 'DHCW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[47, 39.85, 'Đỉnh tuần 5/10/26: 39,85', 0.6], [4, 27.6, 'Đáy tuần 1/12/25: 27,60', 1.6], [51, 36.45, 'Tuần 2/11/26: 36,45', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Doanh nghiệp kiếm tiền thế nào',
  'moc': True,
  'label': 'DHC – mô hình kinh doanh',
  'cap': ('DHC', 'KIẾM TIỀN THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'cardboard boxes',
  'say': 'Chương một, DHC kiếm tiền thế nào. Doanh nghiệp sản xuất giấy cuộn công nghiệp và bao bì carton. Lợi nhuận phụ thuộc vào ba biến số: giá giấy phế '
         'liệu đầu vào, giá bán giấy và bao bì đầu ra, và sản lượng đơn hàng từ các doanh nghiệp xuất khẩu. Khi xuất khẩu tăng, nhu cầu thùng carton tăng '
         'theo. Khi giá giấy phế liệu giảm mà giá bán giữ được, biên lợi nhuận mở rộng. Đây là ngành có tính chu kỳ, nên P trên E phải đọc cùng vị trí trong '
         'chu kỳ.',
  'cards': [('Sản phẩm', 'Giấy cuộn, carton', ''), ('Đầu vào', 'Giấy phế liệu', 'giá biến động'), ('Nhu cầu', 'Theo xuất khẩu', 'có chu kỳ')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'moc': True,
  'label': 'LNST công ty mẹ DHC (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit chart',
  'say': 'Chương hai, lợi nhuận. quý ba năm hai nghìn không trăm hai mươi sáu DHC lãi sau thuế khoảng một trăm bốn mươi chín tỷ đồng, tăng bốn mươi chín phẩy '
         'bảy phần trăm so với cùng kỳ. Lũy kế chín tháng khoảng bốn trăm sáu mươi tư tỷ, tăng bảy mươi chín phẩy bảy phần trăm. Chuỗi tám quý đi lên khá đều, '
         'từ khoảng bốn mươi chín tỷ ở quý bốn năm hai nghìn không trăm hai mươi tư lên khoảng một trăm bảy mươi tám tỷ ở quý hai năm hai nghìn không trăm hai '
         'mươi sáu, rồi lùi nhẹ ở quý ba. Doanh thu quý ba khoảng một nghìn không trăm chín mươi ba tỷ, tăng mười bảy phẩy ba phần trăm. Lợi nhuận tăng nhanh '
         'hơn doanh thu nhiều lần, vậy phần chênh đến từ biên.',
  'bars': [('Q4/24', 49.0, (56, 189, 248), '49'),
           ('Q1/25', 75.7, (56, 189, 248), '76'),
           ('Q2/25', 83.0, (56, 189, 248), '83'),
           ('Q3/25', 99.6, (56, 189, 248), '100'),
           ('Q4/25', 134.8, (56, 189, 248), '135'),
           ('Q1/26', 137.3, (56, 189, 248), '137'),
           ('Q2/26', 177.8, (56, 189, 248), '178'),
           ('Q3/26', 149.1, (34, 197, 94), '149')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Biên lợi nhuận gộp',
  'moc': True,
  'label': 'DHC – biên gộp cải thiện',
  'cap': ('BIÊN GỘP', '20,8%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'margin',
  'say': 'Chương ba, biên gộp. quý ba năm hai nghìn không trăm hai mươi sáu biên lợi nhuận gộp của DHC khoảng hai mươi phẩy tám phần trăm, cùng kỳ chỉ khoảng '
         'mười lăm phẩy bảy phần trăm, cải thiện hơn năm điểm phần trăm. Với doanh thu khoảng một nghìn không trăm chín mươi ba tỷ, năm điểm phần trăm biên '
         'tương đương khoảng năm mươi lăm tỷ lợi nhuận gộp tăng thêm. Đây chính là lý do lợi nhuận tăng gần năm mươi phần trăm trong khi doanh thu chỉ tăng '
         'mười bảy phần trăm. Câu hỏi quan trọng nhất cho định giá là: biên hai mươi phần trăm có bền không, hay chỉ là đỉnh chu kỳ khi giá đầu vào đang thuận '
         'lợi?',
  'cards': [('Biên gộp Q3/2026', '20,8%', 'cùng kỳ 15,7%'), ('Doanh thu', '+17,3%', '1.093 tỷ'), ('Lợi nhuận', '+49,7%', '149 tỷ')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Ba con số định giá',
  'moc': True,
  'label': 'DHC – định giá ngày 6/11/2026',
  'cap': ('P/E 6,43', 'P/B 1,57'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation',
  'say': 'Chương bốn, đọc ba con số định giá. P trên E sáu phẩy bốn ba lần nghĩa là nếu lợi nhuận giữ nguyên, doanh nghiệp cần khoảng sáu năm rưỡi để kiếm lại '
         'bằng giá trị thị trường. P trên B một phẩy năm bảy lần với ROE hai mươi lăm phẩy bốn phần trăm là mức không đắt, vì mỗi đồng vốn chủ đang sinh lời '
         'hơn hai mươi lăm xu mỗi năm. Vốn hóa khoảng ba nghìn tám trăm năm mươi hai tỷ đồng, thuộc nhóm nhỏ, giá trị giao dịch khoảng hai mươi tỷ đồng mỗi '
         'ngày. Nhưng anh chị nhớ: P trên E tính trên lợi nhuận bốn quý gần nhất, đang ở vùng cao nhất trong chuỗi. Nếu biên quay về mười lăm phần trăm, lợi '
         'nhuận giảm và P trên E thực tế sẽ cao hơn.',
  'cards': [('P/E', '6,43 lần', '4 quý gần nhất'), ('P/B · ROE', '1,57 · 25,4%', '6/11/2026'), ('Cổ tức', '5,02%', 'theo giá hiện tại')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'DHC – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk',
  'say': 'Chương năm, rủi ro cần theo dõi. Một, giá giấy phế liệu: tăng trở lại sẽ bóp biên. Hai, đơn hàng xuất khẩu: nhu cầu carton đi theo xuất khẩu, chậm '
         'lại thì sản lượng giảm. Ba, thanh khoản: vốn hóa nhỏ, khoảng hai mươi tỷ một ngày, nên tỷ trọng không nên lớn. Bốn, P trên E thấp ở đỉnh chu kỳ là '
         'cái bẫy kinh điển của cổ phiếu chu kỳ: P trên E thấp nhất thường xuất hiện khi lợi nhuận cao nhất.',
  'items': [('Giá giấy phế liệu', (255, 196, 0)),
            ('Đơn hàng xuất khẩu', (255, 196, 0)),
            ('Thanh khoản ≈ 20 tỷ/ngày', (239, 68, 68)),
            ('P/E thấp ở đỉnh chu kỳ', (239, 68, 68))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('P/E 6', 'RẺ HAY ĐỈNH CHU KỲ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Với một doanh nghiệp chu kỳ có P trên E khoảng sáu và biên vừa tăng mạnh, anh chị sẽ dựa vào con số nào để biết mình đang ở '
         'đầu hay cuối chu kỳ?'}]

S['K2_1011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': '9 ngân hàng – bộ đệm dự phòng',
  'cap': ('ĐỆM 243%', 'HAY CHỈ 42%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'bank vault',
  'say': 'Cùng là ngân hàng niêm yết, cùng báo lãi quý ba. Nhưng một bên để sẵn khoảng hai trăm bốn mươi ba đồng dự phòng cho mỗi một trăm đồng nợ xấu, bên '
         'kia chỉ khoảng bốn mươi hai đồng. Khi nợ xấu tăng, hai ngân hàng này phản ứng hoàn toàn khác nhau. Video này em đặt chín ngân hàng cạnh nhau theo ba '
         'con số: tỷ lệ bao phủ nợ xấu, tỷ lệ nợ xấu và P trên B, để anh chị thấy thị trường đang trả giá cho rủi ro thế nào. Số liệu từ báo cáo tài chính quý '
         'ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'VCBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 78.15, 'Đỉnh tuần 12/1/26: 78,15', 0.6], [36, 52.6, 'Đáy tuần 20/7/26: 52,60', 1.6], [51, 53.6, 'Tuần 2/11/26: 53,60', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Bao phủ nợ xấu',
  'moc': True,
  'label': 'Tỷ lệ bao phủ nợ xấu cuối Q3/2026 (%)',
  'cap': ('BỘ ĐỆM', 'DỰ PHÒNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'safety buffer chart',
  'say': 'Chương một, tỷ lệ bao phủ nợ xấu, tức quỹ dự phòng chia cho nợ xấu. VCB khoảng hai trăm bốn mươi ba phần trăm, CTG khoảng một trăm sáu mươi phần '
         'trăm, TCB khoảng một trăm linh bảy phần trăm. Nhóm giữa có ACB khoảng chín mươi mốt phần trăm và MBB khoảng tám mươi lăm phần trăm. Nhóm mỏng có VPB '
         'khoảng năm mươi tư phần trăm, MSB khoảng bốn mươi bảy phần trăm, HDB khoảng bốn mươi sáu phần trăm và VIB khoảng bốn mươi hai phần trăm. Bộ đệm trên '
         'một trăm phần trăm nghĩa là ngân hàng đã dự phòng nhiều hơn toàn bộ nợ xấu hiện có. Bộ đệm dưới năm mươi phần trăm nghĩa là nếu nợ xấu không thu hồi '
         'được, ngân hàng còn phải trích lập thêm hơn một nửa, và khoản đó đi thẳng vào lợi nhuận.',
  'bars': [('VCB', 243, (34, 197, 94), '243%'),
           ('CTG', 160, (34, 197, 94), '160%'),
           ('TCB', 107, (34, 197, 94), '107%'),
           ('ACB', 91, (255, 196, 0), '91%'),
           ('MBB', 85, (255, 196, 0), '85%'),
           ('VPB', 54, (239, 68, 68), '54%'),
           ('MSB', 47, (239, 68, 68), '47%'),
           ('HDB', 46, (239, 68, 68), '46%'),
           ('VIB', 42, (239, 68, 68), '42%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Tỷ lệ nợ xấu',
  'moc': True,
  'label': 'Tỷ lệ nợ xấu cuối Q3/2026 (%)',
  'cap': ('TỶ LỆ', 'NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'npl chart',
  'say': 'Chương hai, tỷ lệ nợ xấu. VCB khoảng không phẩy bảy một phần trăm, ACB khoảng một phẩy một chín phần trăm, CTG khoảng một phẩy hai không phần trăm, '
         'TCB khoảng một phẩy hai bảy phần trăm, MBB khoảng một phẩy sáu bảy phần trăm. Nhóm còn lại cao hơn: MSB khoảng hai phẩy bảy không phần trăm, VPB '
         'khoảng ba phẩy một hai phần trăm, VIB khoảng ba phẩy hai không phần trăm, HDB khoảng ba phẩy bốn hai phần trăm. Anh chị thấy một quy luật: ngân hàng '
         'có nợ xấu thấp thường cũng là ngân hàng có bộ đệm dày. Ngân hàng có nợ xấu cao lại có bộ đệm mỏng. Rủi ro dồn về một phía, chứ không bù trừ cho '
         'nhau. Trong quý ba, nợ xấu tăng so với quý trước ở TCB, MBB, MSB, VIB và HDB.',
  'bars': [('VCB', 0.71, (34, 197, 94), '0,71%'),
           ('ACB', 1.19, (34, 197, 94), '1,19%'),
           ('CTG', 1.2, (34, 197, 94), '1,20%'),
           ('TCB', 1.27, (34, 197, 94), '1,27%'),
           ('MBB', 1.67, (255, 196, 0), '1,67%'),
           ('MSB', 2.7, (239, 68, 68), '2,70%'),
           ('VPB', 3.12, (239, 68, 68), '3,12%'),
           ('VIB', 3.2, (239, 68, 68), '3,20%'),
           ('HDB', 3.42, (239, 68, 68), '3,42%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Thị trường trả giá thế nào',
  'moc': True,
  'label': 'P/B ngày 6/11/2026 so với bộ đệm',
  'cap': ('P/B', 'SO VỚI RỦI RO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation bank',
  'say': 'Chương ba, thị trường có trả giá cho rủi ro không? VCB bộ đệm dày nhất, P trên B cao nhất nhóm, khoảng một phẩy bảy chín lần. Nhưng HDB có bộ đệm '
         'khoảng bốn mươi sáu phần trăm vẫn có P trên B khoảng một phẩy sáu ba lần, nhờ ROE khoảng hai mươi ba phẩy ba phần trăm. MSB bộ đệm bốn mươi bảy phần '
         'trăm có P trên B khoảng một phẩy ba một lần, cao hơn CTG khoảng một phẩy một chín lần dù CTG có bộ đệm một trăm sáu mươi phần trăm. VIB bộ đệm thấp '
         'nhất, P trên B khoảng một phẩy không sáu lần. Như vậy, thị trường chủ yếu trả giá theo ROE và câu chuyện tăng trưởng, còn bộ đệm chỉ được phản ánh '
         'một phần. Đây chính là chỗ nhà đầu tư cá nhân cần tự điều chỉnh.',
  'cards': [('VCB', 'P/B 1,79', 'đệm ≈ 243%'), ('HDB · MSB', 'P/B 1,63 · 1,31', 'đệm ≈ 46% · 47%'), ('CTG · VIB', 'P/B 1,19 · 1,06', 'đệm ≈ 160% · 42%')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Cách đọc cho nhà đầu tư',
  'moc': True,
  'label': 'Ba câu hỏi khi chọn cổ phiếu ngân hàng',
  'cap': ('BA CÂU HỎI', 'TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'questions',
  'say': 'Chương bốn, ba câu hỏi em dùng khi so ngân hàng. Một, nợ xấu đang tăng hay giảm qua hai đến bốn quý? Hai, bộ đệm dưới sáu mươi phần trăm thì lợi '
         'nhuận năm tới chịu rủi ro trích lập, anh chị nên chiết khấu P trên B tương ứng. Ba, lợi nhuận tăng nhờ cho vay hay nhờ giảm trích lập? Ngân hàng bộ '
         'đệm mỏng mà vẫn giảm trích lập là tín hiệu cần thận trọng. Và nếu đang cầm nhiều mã ngân hàng, anh chị nên tổng hợp tỷ trọng cả nhóm, vì đó là một '
         'ngành.',
  'items': [('Xu hướng nợ xấu 2–4 quý', (255, 196, 0)),
            ('Đệm < 60% → chiết khấu P/B', (239, 68, 68)),
            ('Lãi nhờ cho vay hay nhờ trích lập ít', (255, 196, 0)),
            ('Tổng tỷ trọng cả nhóm ngân hàng', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LÃI GIỐNG NHAU', 'ĐỆM KHÁC NHAU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Giữa một ngân hàng ROE cao nhưng bộ đệm dưới năm mươi phần trăm, và một ngân hàng ROE thấp hơn nhưng bộ đệm trên một trăm năm '
         'mươi phần trăm, anh chị sẵn sàng trả P trên B cao hơn cho bên nào?'}]

S['LST_1011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Enron 2001',
  'cap': ('90 USD XUỐNG', 'DƯỚI 1 USD?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'Enron headquarters Houston',
  'say': 'Năm hai nghìn, cổ phiếu Enron giao dịch quanh chín mươi đô la Mỹ, công ty được tạp chí Fortune bình chọn là công ty sáng tạo nhất nước Mỹ sáu năm '
         'liền. Chưa đầy hai năm sau, cổ phiếu xuống dưới một đô la, và Enron nộp đơn phá sản ngày hai tháng mười hai năm hai nghìn không trăm linh một, vụ '
         'phá sản lớn nhất nước Mỹ lúc đó. Một công ty báo lãi đều đặn sụp đổ thế nào? Video này em kể lại câu chuyện Enron theo bốn phần: cỗ máy lợi nhuận '
         'trên giấy, những khoản nợ giấu ngoài bảng, sáu tuần sụp đổ, và bài học đọc báo cáo tài chính cho nhà đầu tư Việt Nam hôm nay. Biểu đồ phía sau là '
         'VN-Index, chỉ để minh họa.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Cỗ máy lợi nhuận trên giấy',
  'moc': True,
  'label': 'Enron 1985–2000',
  'cap': ('LỢI NHUẬN', 'TRÊN GIẤY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'energy trading floor',
  'say': 'Chương một, cỗ máy lợi nhuận trên giấy. Enron ra đời năm một nghìn chín trăm tám mươi lăm từ việc sáp nhập hai công ty đường ống khí đốt. Đến cuối '
         'thập niên chín mươi, Enron biến mình thành sàn giao dịch năng lượng, mua bán hợp đồng điện, khí, thậm chí cả băng thông internet. Họ dùng phương '
         'pháp kế toán theo giá thị trường: khi ký một hợp đồng nhiều năm, Enron ghi nhận ngay lợi nhuận ước tính của cả hợp đồng vào năm ký. Lợi nhuận trên '
         'báo cáo vì thế tăng rất nhanh, trong khi tiền mặt thực thu lại chậm hơn nhiều. Khoảng cách giữa lợi nhuận và dòng tiền là dấu hiệu đầu tiên mà ít '
         'người để ý.',
  'cards': [('1985', 'Sáp nhập', 'hai công ty đường ống'),
            ('Cuối 1990s', 'Sàn giao dịch năng lượng', 'điện, khí, băng thông'),
            ('Kế toán', 'Theo giá thị trường', 'ghi lãi trước, thu tiền sau')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Nợ giấu ngoài bảng',
  'moc': True,
  'label': 'Các công ty mục đích đặc biệt',
  'cap': ('NỢ GIẤU', 'NGOÀI BẢNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'hidden debt',
  'say': 'Chương hai, những khoản nợ giấu ngoài bảng cân đối. Để giữ lợi nhuận đẹp và nợ thấp, Enron lập hàng trăm công ty mục đích đặc biệt. Các khoản nợ và '
         'tài sản thua lỗ được chuyển sang những công ty này, nên không xuất hiện trên báo cáo của Enron. Nhiều công ty trong số đó lại được bảo đảm bằng '
         'chính cổ phiếu Enron. Khi giá cổ phiếu còn cao, mọi thứ có vẻ ổn. Khi giá giảm, tài sản bảo đảm co lại, các khoản nợ ẩn lộ ra cùng lúc. Đây là vòng '
         'xoáy mà các nhà phân tích bên ngoài gần như không thể thấy nếu chỉ đọc số tổng.',
  'cards': [('Công ty mục đích đặc biệt', 'Hàng trăm', 'giữ nợ ngoài bảng'),
            ('Bảo đảm bằng', 'Cổ phiếu Enron', 'vòng xoáy khi giá giảm'),
            ('Người ngoài', 'Khó thấy', 'nếu chỉ đọc số tổng')]},
 {'k': 'checklist',
  'ch': 'Chương 3 – Sáu tuần sụp đổ',
  'moc': True,
  'label': 'Enron năm 2001',
  'cap': ('SÁU TUẦN', 'SỤP ĐỔ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'newspaper collapse',
  'say': 'Chương ba, sáu tuần sụp đổ. Tháng tám năm hai nghìn không trăm linh một, tổng giám đốc Jeffrey Skilling từ chức sau khoảng sáu tháng tại vị. Ngày '
         'mười sáu tháng mười năm hai nghìn không trăm linh một, Enron công bố lỗ quý ba khoảng sáu trăm mười tám triệu đô la Mỹ và giảm vốn chủ sở hữu khoảng '
         'một phẩy hai tỷ đô la. Đầu tháng mười một, công ty điều chỉnh lại lợi nhuận của các năm từ một nghìn chín trăm chín mươi bảy. Thương vụ bán mình cho '
         'đối thủ Dynegy đổ vỡ cuối tháng mười một, cổ phiếu rơi xuống dưới một đô la. Ngày hai tháng mười hai năm hai nghìn không trăm linh một, Enron nộp '
         'đơn phá sản. Công ty kiểm toán Arthur Andersen sau đó cũng sụp đổ theo.',
  'items': [('8/2001: CEO từ chức', (255, 196, 0)),
            ('16/10/2001: lỗ quý ba ≈ 618 triệu USD', (239, 68, 68)),
            ('11/2001: điều chỉnh lợi nhuận từ 1997', (239, 68, 68)),
            ('2/12/2001: nộp đơn phá sản', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 4 – Ai chịu thiệt nhất',
  'moc': True,
  'label': 'Người lao động và cổ đông',
  'cap': ('AI CHỊU', 'THIỆT NHẤT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'employees leaving office',
  'say': 'Chương bốn, ai chịu thiệt nhất. Không phải các nhà đầu tư chuyên nghiệp, mà là nhân viên Enron. Rất nhiều người để phần lớn quỹ hưu trí của mình '
         'trong chính cổ phiếu Enron, vì tin vào công ty nơi mình làm việc. Khi Enron phá sản, họ mất việc và mất luôn khoản tiết kiệm cả đời cùng một lúc. '
         'Đây là bài học về rủi ro tập trung ở dạng khắc nghiệt nhất: thu nhập và tài sản cùng phụ thuộc vào một doanh nghiệp. Sau vụ Enron, nước Mỹ ban hành '
         'Đạo luật Sarbanes-Oxley năm hai nghìn không trăm linh hai, siết chặt trách nhiệm của lãnh đạo và kiểm toán.',
  'cards': [('Quỹ hưu trí', 'Dồn vào cổ phiếu Enron', 'tập trung'),
            ('Mất cùng lúc', 'Việc làm và tiết kiệm', ''),
            ('2002', 'Đạo luật Sarbanes-Oxley', 'siết kiểm toán')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Bài học cho hôm nay',
  'moc': True,
  'label': 'Bốn bài học từ Enron',
  'cap': ('BỐN BÀI HỌC', 'TỪ ENRON'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'lessons',
  'say': 'Chương năm, bốn bài học cho nhà đầu tư Việt Nam hôm nay. Một, so lợi nhuận với dòng tiền kinh doanh nhiều năm: lãi đều mà dòng tiền âm kéo dài là cờ '
         'đỏ. Hai, đọc thuyết minh về bên liên quan, bảo lãnh và cam kết ngoài bảng. Ba, cẩn trọng với mô hình kinh doanh mà anh chị không giải thích được '
         'trong hai câu. Bốn, không để thu nhập và tài sản cùng phụ thuộc vào một công ty, kể cả công ty mình tin nhất. Enron không sụp vì một ngày xấu, mà vì '
         'nhiều năm con số không khớp với thực tế.',
  'items': [('Lợi nhuận so với dòng tiền', (239, 68, 68)),
            ('Bên liên quan, bảo lãnh ngoài bảng', (255, 196, 0)),
            ('Mô hình phải giải thích được', (255, 196, 0)),
            ('Không dồn mọi thứ vào một công ty', (239, 68, 68))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LÃI ĐẸP', 'CHƯA CHẮC THẬT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Khi đọc báo cáo tài chính một doanh nghiệp, anh chị đã bao giờ so lợi nhuận với dòng tiền kinh doanh của năm năm liền chưa, '
         'và kết quả có khiến anh chị bất ngờ không?'}]

S['TS1011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'REE – góp đều 38 tháng',
  'cap': ('GÓP ĐỀU 3 NĂM', 'VẪN HÒA VỐN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'savings jar coins',
  'say': 'Góp đều ba triệu đồng mỗi tháng vào cổ phiếu REE trong ba mươi tám tháng, từ tháng mười năm hai nghìn không trăm hai mươi ba đến tháng mười một năm '
         'hai nghìn không trăm hai mươi sáu, tổng vốn một trăm mười bốn triệu. Kết quả hôm nay: khoảng một trăm mười ba phẩy tám triệu, gần như hòa vốn. Trong '
         'khi đó, nếu mua một lần ngay từ đầu, cùng một trăm mười bốn triệu sẽ thành khoảng một trăm năm mươi lăm phẩy bốn triệu. Góp đều không phải lúc nào '
         'cũng thắng? Video này em dùng giá đóng cửa thật để giải thích vì sao, và người tích sản nên rút ra điều gì. Số liệu chưa tính cổ tức tiền mặt. Kết '
         'quả quá khứ, không phải cam kết lợi nhuận.',
  'chart': {'sym': 'REEW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[20, 64.52, 'Đỉnh tuần 30/3/26: 64,52', 0.6], [36, 42.5, 'Đáy tuần 20/7/26: 42,50', 1.6], [51, 47.1, 'Tuần 2/11/26: 47,10', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Hai cách, hai kết quả',
  'moc': True,
  'label': 'Giá trị 114 triệu đồng vốn vào REE (triệu đồng, 11/2026)',
  'cap': ('GÓP ĐỀU', 'HAY MỘT LẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'comparison bars',
  'say': 'Chương một, hai cách, hai kết quả. Cách thứ nhất, góp đều ba triệu vào phiên đầu tiên mỗi tháng, ba mươi tám tháng, tổng vốn một trăm mười bốn '
         'triệu, giá trị hôm nay khoảng một trăm mười ba phẩy tám triệu, lỗ khoảng không phẩy hai phần trăm. Cách thứ hai, bỏ cả một trăm mười bốn triệu vào '
         'phiên ngày hai mươi bảy tháng mười năm hai nghìn không trăm hai mươi ba ở giá đóng cửa khoảng ba mươi tư phẩy năm năm nghìn đồng, hôm nay giá khoảng '
         'bốn mươi bảy phẩy một nghìn, giá trị khoảng một trăm năm mươi lăm phẩy bốn triệu, lãi khoảng ba mươi sáu phần trăm. Cùng một mã, cùng số vốn, chênh '
         'nhau khoảng bốn mươi mốt phẩy sáu triệu đồng. Nhưng anh chị nhớ, người đi làm hiếm khi có sẵn một trăm mười bốn triệu ngay từ đầu.',
  'bars': [('Góp đều 38 tháng', 113.8, (255, 196, 0), '113,8'),
           ('Mua một lần 10/2023', 155.4, (34, 197, 94), '155,4'),
           ('Vốn bỏ ra', 114.0, (56, 189, 248), '114')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Vì sao góp đều hòa vốn',
  'moc': True,
  'label': 'Giá vốn bình quân so với giá hiện tại',
  'cap': ('GIÁ VỐN', '≈ GIÁ HIỆN TẠI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'average cost',
  'say': 'Chương hai, vì sao góp đều lại hòa vốn. Giá REE đi lên phần lớn trong giai đoạn hai nghìn không trăm hai mươi tư đến đầu hai nghìn không trăm hai '
         'mươi sáu, đỉnh khoảng sáu mươi hai phẩy ba năm nghìn đồng ngày hai mươi sáu tháng ba năm hai nghìn không trăm hai mươi sáu, sau đó giảm về khoảng '
         'bốn mươi bảy phẩy một nghìn. Người góp đều mua nhiều kỳ ở vùng giá cao năm hai nghìn không trăm hai mươi lăm và đầu hai nghìn không trăm hai mươi '
         'sáu, nên giá vốn bình quân lên khoảng bốn mươi bảy phẩy một bảy nghìn, gần bằng giá hôm nay. Góp đều làm giá vốn đi theo giá trung bình của cả giai '
         'đoạn. Nếu cổ phiếu tăng ở đầu kỳ rồi giảm ở cuối kỳ, kết quả của góp đều sẽ kém mua một lần.',
  'cards': [('Giá đầu kỳ', '34,55', '27/10/2023'), ('Giá vốn bình quân', '≈ 47,17', 'góp đều 38 tháng'), ('Giá hiện tại', '≈ 47,10', 'tuần 2/11/2026')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Doanh nghiệp vẫn lãi đều',
  'moc': True,
  'label': 'LNST công ty mẹ REE (tỷ đồng)',
  'cap': ('DOANH NGHIỆP', 'VẪN LÃI ĐỀU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit bars',
  'say': 'Chương ba, doanh nghiệp vẫn làm ăn ổn. quý ba năm hai nghìn không trăm hai mươi sáu REE lãi sau thuế khoảng bảy trăm tám mươi tám tỷ đồng, tăng mười '
         'sáu phẩy chín phần trăm so với cùng kỳ, lũy kế chín tháng khoảng hai nghìn một trăm ba mươi tư tỷ, tăng mười một phẩy tám phần trăm. Lợi nhuận tăng '
         'đều, nhưng không nhanh. Trong khi đó giá cổ phiếu đã có lúc tăng mạnh hơn lợi nhuận, rồi điều chỉnh lại. Bài học ở đây: khi tích sản, giá có thể đi '
         'trước hoặc đi sau lợi nhuận nhiều năm. Người góp đều cần đo kết quả bằng chu kỳ năm đến mười năm, không phải ba năm.',
  'bars': [('Q4/24', 678.3, (56, 189, 248), '678'),
           ('Q1/25', 611.4, (56, 189, 248), '611'),
           ('Q2/25', 622.9, (56, 189, 248), '623'),
           ('Q3/25', 674.2, (56, 189, 248), '674'),
           ('Q4/25', 620.0, (56, 189, 248), '620'),
           ('Q1/26', 714.2, (56, 189, 248), '714'),
           ('Q2/26', 631.3, (56, 189, 248), '631'),
           ('Q3/26', 788.0, (34, 197, 94), '788')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Người tích sản nên làm gì',
  'moc': True,
  'label': 'Ba điều chỉnh cho người góp đều',
  'cap': ('NGƯỜI TÍCH SẢN', 'NÊN LÀM GÌ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'plan',
  'say': 'Chương bốn, người tích sản nên làm gì. Một, góp đều nhiều mã hoặc quỹ chỉ số, đừng chỉ một mã, để không phụ thuộc vào thời điểm một cổ phiếu tăng '
         'hay giảm. Hai, khi giá vượt xa lợi nhuận, cân nhắc giảm tốc độ mua mã đó và chuyển phần góp sang mã khác đang rẻ hơn. Ba, ghi lại giá vốn và tỷ '
         'trọng mỗi quý, để biết danh mục đang lệch về đâu. Góp đều là kỷ luật tốt, nhưng góp đều mà không nhìn định giá thì chỉ là mua theo lịch.',
  'items': [('Góp đều nhiều mã hoặc quỹ chỉ số', (34, 197, 94)),
            ('Giá vượt xa lợi nhuận → giảm tốc mua', (255, 196, 0)),
            ('Ghi giá vốn, tỷ trọng mỗi quý', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('GÓP ĐỀU 3 NĂM', 'HÒA VỐN – SAI Ở ĐÂU?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Nếu anh chị là người góp đều REE ba năm qua, anh chị sẽ tiếp tục, dừng lại, hay chuyển một phần sang mã khác, và vì sao?'}]

S['Y2_1011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Soi BCTC PVT – Q3/2026',
  'cap': ('LÃI +42,4%', 'NHƯNG −35% QUÝ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'oil tanker ship',
  'say': 'PVTrans, mã PVT, báo lãi quý ba năm hai nghìn không trăm hai mươi sáu tăng bốn mươi hai phẩy bốn phần trăm so với cùng kỳ, lũy kế chín tháng tăng '
         'sáu mươi tư phẩy sáu phần trăm. Nhưng nếu so với quý hai, lợi nhuận lại giảm ba mươi lăm phẩy hai phần trăm. Cùng một quý, một phép so sánh cho thấy '
         'tăng mạnh, phép so sánh kia cho thấy giảm mạnh. Video này em soi báo cáo tài chính PVT theo năm dòng: doanh thu, lợi nhuận, so sánh cùng kỳ và quý '
         'trước, định giá, và rủi ro. Số liệu từ báo cáo quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai '
         'nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'PVTW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[17, 29.73, 'Đỉnh tuần 9/3/26: 29,73', 0.6], [0, 15.32, 'Đáy tuần 3/11/25: 15,32', 1.6], [51, 20.55, 'Tuần 2/11/26: 20,55', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Doanh thu',
  'moc': True,
  'label': 'Doanh thu thuần PVT (tỷ đồng)',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'shipping',
  'say': 'Dòng thứ nhất, doanh thu. quý ba năm hai nghìn không trăm hai mươi sáu PVT đạt khoảng năm nghìn sáu trăm mười tỷ đồng doanh thu thuần, tăng hai mươi '
         'sáu phẩy chín phần trăm so với cùng kỳ. Chuỗi tám quý tăng từ khoảng ba nghìn hai trăm sáu mươi tám tỷ ở quý bốn năm hai nghìn không trăm hai mươi '
         'tư lên trên năm nghìn năm trăm tỷ trong hai quý gần nhất. PVT vận tải dầu thô, xăng dầu và khí bằng đội tàu, nên doanh thu phụ thuộc vào số tàu, giá '
         'cước và hiệu suất khai thác. Doanh thu tăng đều cho thấy đội tàu đang được dùng nhiều hơn hoặc giá cước tốt hơn.',
  'bars': [('Q4/24', 3267.6, (56, 189, 248), '3.268'),
           ('Q1/25', 2789.5, (56, 189, 248), '2.790'),
           ('Q2/25', 4312.6, (56, 189, 248), '4.313'),
           ('Q3/25', 4419.4, (56, 189, 248), '4.419'),
           ('Q4/25', 4444.1, (56, 189, 248), '4.444'),
           ('Q1/26', 4177.1, (56, 189, 248), '4.177'),
           ('Q2/26', 5577.3, (56, 189, 248), '5.577'),
           ('Q3/26', 5610.1, (34, 197, 94), '5.610')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận',
  'moc': True,
  'label': 'LNST công ty mẹ PVT (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit',
  'say': 'Dòng thứ hai, lợi nhuận. quý ba năm hai nghìn không trăm hai mươi sáu PVT lãi sau thuế công ty mẹ khoảng ba trăm bảy mươi lăm tỷ đồng, tăng bốn mươi '
         'hai phẩy bốn phần trăm so với cùng kỳ. Lũy kế chín tháng khoảng một nghìn hai trăm bảy mươi ba tỷ, tăng sáu mươi tư phẩy sáu phần trăm. Anh chị nhìn '
         'cột quý hai năm hai nghìn không trăm hai mươi sáu: khoảng năm trăm bảy mươi chín tỷ, cao vượt trội so với các quý khác. Quý hai có thể có khoản thu '
         'nhập không thường xuyên, như thanh lý tàu hoặc hoàn nhập. Vì vậy, khi quý ba trở về khoảng ba trăm bảy mươi lăm tỷ, so với quý trước sẽ giảm ba mươi '
         'lăm phẩy hai phần trăm, nhưng so với mặt bằng các quý trước đó vẫn cao hơn.',
  'bars': [('Q4/24', 209.1, (56, 189, 248), '209'),
           ('Q1/25', 215.1, (56, 189, 248), '215'),
           ('Q2/25', 294.8, (56, 189, 248), '295'),
           ('Q3/25', 263.4, (56, 189, 248), '263'),
           ('Q4/25', 265.9, (56, 189, 248), '266'),
           ('Q1/26', 319.0, (56, 189, 248), '319'),
           ('Q2/26', 578.7, (56, 189, 248), '579'),
           ('Q3/26', 375.1, (34, 197, 94), '375')]},
 {'k': 'cards',
  'ch': 'Chương 3 – So cùng kỳ hay so quý trước',
  'moc': True,
  'label': 'Hai phép so sánh, hai câu chuyện',
  'cap': ('SO CÙNG KỲ', 'HAY QUÝ TRƯỚC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'compare',
  'say': 'Dòng thứ ba, chọn phép so sánh đúng. So cùng kỳ năm trước loại bỏ yếu tố mùa vụ, phù hợp với hầu hết doanh nghiệp. So với quý trước cho thấy đà ngắn '
         'hạn, nhưng dễ bị méo bởi một quý có khoản bất thường. Với PVT, cách đọc công bằng là nhìn mặt bằng: bốn quý gần nhất có tổng lợi nhuận khoảng một '
         'nghìn năm trăm ba mươi chín tỷ, trong khi bốn quý trước đó khoảng chín trăm tám mươi hai tỷ. Mặt bằng đã cao hơn rõ, dù quý ba thấp hơn quý hai.',
  'cards': [('So cùng kỳ', '+42,4%', 'Q3/2026'),
            ('So quý trước', '−35,2%', 'quý 2 có thể bất thường'),
            ('4 quý gần nhất', '≈ 1.539 tỷ', '4 quý trước ≈ 982 tỷ')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'moc': True,
  'label': 'PVT – định giá ngày 6/11/2026',
  'cap': ('P/E 6,92', 'P/B 1,08'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation',
  'say': 'Dòng thứ tư, định giá. PVT có P trên E khoảng sáu phẩy chín hai lần, P trên B khoảng một phẩy không tám lần, ROE khoảng mười hai phẩy chín phần '
         'trăm, vốn hóa khoảng mười nghìn sáu trăm bốn mươi chín tỷ đồng. Giá đóng cửa tuần gần nhất khoảng hai mươi phẩy năm năm nghìn đồng, so với đỉnh tuần '
         'khoảng hai mươi chín phẩy bảy ba nghìn tháng ba năm hai nghìn không trăm hai mươi sáu. Vận tải biển là ngành thâm dụng vốn, phải liên tục đầu tư tàu '
         'mới, nên ROE khoảng mười ba phần trăm là mức trung bình và P trên B quanh một lần phản ánh điều đó.',
  'cards': [('P/E', '6,92 lần', '6/11/2026'), ('P/B · ROE', '1,08 · 12,9%', ''), ('Giá', '20,55', 'đỉnh tuần 3/2026: 29,73')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'PVT – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk',
  'say': 'Dòng thứ năm, rủi ro. Một, giá cước vận tải dầu có chu kỳ, có thể giảm nhanh khi cung tàu toàn cầu tăng. Hai, đầu tư tàu mới cần vốn lớn và vay nợ, '
         'chi phí lãi vay sẽ tăng. Ba, lợi nhuận bất thường: cần tách khoản thanh lý tàu ra khỏi lợi nhuận cốt lõi. Bốn, giá dầu biến động mạnh như tuần đầu '
         'tháng mười một tác động đến tâm lý cả nhóm dầu khí, kể cả doanh nghiệp vận tải.',
  'items': [('Chu kỳ giá cước', (255, 196, 0)),
            ('Vốn đầu tư tàu, lãi vay', (255, 196, 0)),
            ('Tách lợi nhuận bất thường', (239, 68, 68)),
            ('Tâm lý nhóm dầu khí', (255, 196, 0))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('TĂNG 42%', 'HAY GIẢM 35%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Khi một quý vừa tăng mạnh so với cùng kỳ vừa giảm mạnh so với quý trước, anh chị thường tin phép so sánh nào hơn, và vì sao?'}]

S['Y3_1011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Châu Á bán tháo 6/11/2026',
  'cap': ('NIKKEI −5,96%', 'VN-INDEX −0,88%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'stock market crash asia screens',
  'say': 'Ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, Nasdaq giảm năm phẩy năm hai phần trăm, S và P năm trăm giảm bốn phẩy ba sáu phần '
         'trăm. Sáng hôm sau, Nikkei hai trăm hai mươi lăm của Nhật giảm năm phẩy chín sáu phần trăm, KOSPI của Hàn Quốc giảm sáu phẩy không hai phần trăm. '
         'Cùng ngày sáu tháng mười một, VN-Index chỉ giảm khoảng không phẩy tám tám phần trăm, đóng cửa khoảng một nghìn bảy trăm hai mươi lăm điểm. Vì sao '
         'thị trường Việt Nam ít bị cuốn theo, và điều đó an toàn hay chỉ là chậm hơn? Video này em đặt các con số cạnh nhau, giải thích kênh lây lan giữa các '
         'thị trường, và những gì nhà đầu tư Việt Nam nên chuẩn bị. Số liệu đóng cửa các phiên từ ngày ba mươi tháng mười đến ngày sáu tháng mười một năm hai '
         'nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Một tuần biến động',
  'moc': True,
  'label': 'Mức giảm một phiên, tuần đầu tháng 11/2026 (%)',
  'cap': ('MỘT PHIÊN', 'GIẢM BAO NHIÊU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'red screens',
  'say': 'Chương một, một tuần biến động. Ngày ba tháng mười một, KOSPI giảm ba phẩy năm chín phần trăm. Ngày năm tháng mười một, KOSPI giảm tiếp năm phẩy hai '
         'tám phần trăm, Nikkei giảm một phẩy bảy chín phần trăm. Đêm ngày năm tháng mười một giờ Mỹ, Nasdaq giảm năm phẩy năm hai phần trăm, S và P năm trăm '
         'giảm bốn phẩy ba sáu phần trăm. Ngày sáu tháng mười một, Nikkei giảm năm phẩy chín sáu phần trăm về khoảng năm mươi bảy nghìn bốn trăm ba mươi lăm '
         'điểm, KOSPI giảm sáu phẩy không hai phần trăm. Đêm ngày sáu tháng mười một, Mỹ hồi lại: S và P năm trăm tăng không phẩy bốn chín phần trăm, Nasdaq '
         'tăng một phẩy ba chín phần trăm. Trong khi đó, VN-Index phiên ngày sáu tháng mười một giảm khoảng không phẩy tám tám phần trăm, và cả tuần từ một '
         'nghìn bảy trăm bốn mươi mốt phẩy sáu hai điểm cuối tháng mười xuống khoảng một nghìn bảy trăm hai mươi lăm điểm.',
  'bars': [('KOSPI 6/11', 6.02, (239, 68, 68), '−6,02%'),
           ('Nikkei 6/11', 5.96, (239, 68, 68), '−5,96%'),
           ('Nasdaq 5/11', 5.52, (239, 68, 68), '−5,52%'),
           ('S&P 500 5/11', 4.36, (239, 68, 68), '−4,36%'),
           ('VN-Index 6/11', 0.88, (56, 189, 248), '−0,88%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Vì sao Việt Nam ít bị cuốn theo',
  'moc': True,
  'label': 'Ba khác biệt của thị trường Việt Nam',
  'cap': ('VÌ SAO', 'ÍT BỊ CUỐN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'vietnam stock exchange',
  'say': 'Chương hai, vì sao VN-Index giảm ít hơn nhiều. Lý do thứ nhất là cơ cấu: Nikkei và KOSPI có tỷ trọng lớn cổ phiếu công nghệ, bán dẫn, xuất khẩu, '
         'liên thông trực tiếp với Nasdaq. VN-Index nặng về ngân hàng, bất động sản, tiêu dùng nội địa. Lý do thứ hai là nhà đầu tư: thị trường Việt Nam chủ '
         'yếu là nhà đầu tư cá nhân trong nước, dòng vốn ngoại chiếm tỷ trọng nhỏ hơn. Lý do thứ ba là biên độ giá: sàn HOSE giới hạn bảy phần trăm mỗi phiên, '
         'nên cú sốc thường được chia ra nhiều phiên chứ không dồn vào một ngày.',
  'cards': [('Cơ cấu', 'Ngân hàng, BĐS, nội địa', 'ít công nghệ'),
            ('Nhà đầu tư', 'Cá nhân trong nước', 'vốn ngoại nhỏ hơn'),
            ('Biên độ', 'HOSE ±7%', 'sốc chia nhiều phiên')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Kênh lây lan',
  'moc': True,
  'label': 'Ba kênh cú sốc toàn cầu đi vào Việt Nam',
  'cap': ('KÊNH', 'LÂY LAN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'global network',
  'say': 'Chương ba, nhưng giảm ít hơn không có nghĩa là miễn nhiễm. Cú sốc toàn cầu đi vào Việt Nam qua ba kênh. Kênh một, dòng vốn ngoại: khi quỹ toàn cầu '
         'cần tiền mặt, họ bán ở các thị trường mới nổi, gồm cả Việt Nam. Kênh hai, tỷ giá: nếu đồng đô la mạnh lên, áp lực tỷ giá tăng. Hiện tỷ giá đô la '
         'Mỹ/VND khoảng hai mươi lăm nghìn bảy trăm tám mươi đồng, giảm khoảng một phẩy năm phần trăm trong một tháng, nên kênh này đang yên. Kênh ba, tâm lý: '
         'nhà đầu tư trong nước đọc tin quốc tế và phản ứng với độ trễ một, hai phiên.',
  'cards': [('Dòng vốn ngoại', 'Bán ở thị trường mới nổi', ''), ('Tỷ giá', '≈ 25.780', '−1,5% trong 1 tháng'), ('Tâm lý', 'Phản ứng trễ', '1–2 phiên')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Nhà đầu tư nên chuẩn bị gì',
  'moc': True,
  'label': 'Bốn việc khi thế giới biến động mạnh',
  'cap': ('CHUẨN BỊ', 'THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'checklist',
  'say': 'Chương bốn, nhà đầu tư nên chuẩn bị gì. Một, kiểm tra tỷ lệ margin: nếu thị trường trong nước giảm theo trễ vài phiên, tài khoản dùng đòn bẩy sẽ '
         'chịu áp lực đầu tiên. Hai, xem lại tỷ trọng nhóm cổ phiếu xuất khẩu và có sở hữu nước ngoài cao, vì đây là nhóm nhạy nhất với dòng vốn ngoại. Ba, '
         'giữ một phần tiền mặt để không phải bán ở giá xấu. Bốn, đừng phản ứng với một phiên: thị trường Mỹ đã hồi ngay phiên ngày sáu tháng mười một, biến '
         'động mạnh thường đi theo cả hai chiều.',
  'items': [('Kiểm tra tỷ lệ margin', (239, 68, 68)),
            ('Tỷ trọng nhóm xuất khẩu, vốn ngoại', (255, 196, 0)),
            ('Giữ một phần tiền mặt', (34, 197, 94)),
            ('Không phản ứng với một phiên', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('THẾ GIỚI −6%', 'VIỆT NAM −0,9%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Theo anh chị, việc VN-Index giảm ít hơn nhiều so với Nhật và Hàn là dấu hiệu thị trường vững, hay chỉ là phản ứng chậm hơn '
         'vài phiên?'}]

S['HI1111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'NT2 – định giá nhanh',
  'cap': ('NT2: P/E 4,46', 'ROE 29,4%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'gas power plant',
  'say': 'Điện lực Dầu khí Nhơn Trạch hai, mã NThai, đang có P trên E khoảng bốn phẩy bốn sáu lần, thấp nhất trong nhóm điện lớn. ROE khoảng hai mươi chín '
         'phẩy bốn phần trăm, lợi nhuận quý ba tăng chín mươi lăm phẩy bốn phần trăm. Trả khoảng bốn năm rưỡi lợi nhuận cho một nhà máy điện có hiệu quả vốn '
         'gần ba mươi phần trăm, nghe như món hời. Nhưng nhà máy điện khí có những đặc điểm khiến P trên E thấp là chuyện bình thường. Video này em đọc ba con '
         'số định giá của NThai cạnh chuỗi lợi nhuận và rủi ro riêng của ngành. Số liệu quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày '
         'sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'NT2W',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 28.22, 'Đỉnh tuần 2/3/26: 28,22', 0.6], [44, 19.36, 'Đáy tuần 14/9/26: 19,36', 1.6], [51, 22.2, 'Tuần 2/11/26: 22,20', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Nhà máy điện khí kiếm tiền thế nào',
  'moc': True,
  'label': 'NT2 – mô hình kinh doanh',
  'cap': ('NT2', 'KIẾM TIỀN THẾ NÀO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'power grid',
  'say': 'Chương một, NThai kiếm tiền thế nào. NThai vận hành một nhà máy điện chạy bằng khí, bán điện cho hệ thống điện quốc gia. Doanh thu phụ thuộc vào sản '
         'lượng huy động, tức hệ thống gọi bao nhiêu điện từ nhà máy, và giá bán trên thị trường điện. Chi phí lớn nhất là nhiên liệu khí. Khi thủy điện thiếu '
         'nước, nhiệt điện khí được huy động nhiều hơn. Khi nước về nhiều, sản lượng khí giảm. Vì vậy lợi nhuận của NThai dao động theo thời tiết và theo năm, '
         'không đi thẳng.',
  'cards': [('Bán điện', 'Hệ thống quốc gia', 'sản lượng huy động'),
            ('Chi phí chính', 'Khí nhiên liệu', ''),
            ('Biến số', 'Thủy văn', 'nước nhiều → huy động ít')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận tám quý',
  'moc': True,
  'label': 'LNST công ty mẹ NT2 (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit',
  'say': 'Chương hai, lợi nhuận. quý ba năm hai nghìn không trăm hai mươi sáu NThai lãi sau thuế khoảng bốn trăm mười chín tỷ đồng, tăng chín mươi lăm phẩy '
         'bốn phần trăm so với cùng kỳ và tăng ba mươi sáu phẩy không phần trăm so với quý trước. Lũy kế chín tháng khoảng chín trăm linh sáu tỷ, tăng năm '
         'mươi bảy phẩy không phần trăm. Doanh thu quý khoảng hai nghìn tám trăm linh bảy tỷ, tăng bốn mươi lăm phẩy sáu phần trăm, biên gộp khoảng mười bảy '
         'phẩy năm phần trăm, cùng kỳ mười phẩy sáu phần trăm. Nhưng anh chị nhìn chuỗi: quý một năm hai nghìn không trăm hai mươi lăm chỉ khoảng ba mươi bảy '
         'tỷ, quý bốn năm hai nghìn không trăm hai mươi lăm lại khoảng năm trăm năm mươi ba tỷ. Biên độ lên xuống rất lớn giữa các quý, đúng với đặc thù ngành '
         'điện.',
  'bars': [('Q4/24', 74.6, (56, 189, 248), '75'),
           ('Q1/25', 37.0, (56, 189, 248), '37'),
           ('Q2/25', 326.2, (56, 189, 248), '326'),
           ('Q3/25', 214.2, (56, 189, 248), '214'),
           ('Q4/25', 552.8, (56, 189, 248), '553'),
           ('Q1/26', 180.0, (56, 189, 248), '180'),
           ('Q2/26', 307.8, (56, 189, 248), '308'),
           ('Q3/26', 418.6, (34, 197, 94), '419')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Vì sao P/E thấp',
  'moc': True,
  'label': 'NT2 – định giá ngày 6/11/2026',
  'cap': ('P/E 4,46', 'VÌ SAO THẤP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation',
  'say': 'Chương ba, vì sao P trên E thấp. P trên E khoảng bốn phẩy bốn sáu lần, P trên B khoảng một phẩy hai bảy lần, ROE khoảng hai mươi chín phẩy bốn phần '
         'trăm, cổ tức khoảng ba phẩy một phần trăm, vốn hóa khoảng sáu nghìn năm trăm linh sáu tỷ đồng. P trên E thấp có ba lý do. Một, lợi nhuận bốn quý gần '
         'nhất đang ở vùng cao của chu kỳ, nên P trên E tính trên lợi nhuận đó trông rẻ. Hai, nhà máy đã vận hành nhiều năm, khấu hao giảm làm lợi nhuận tăng, '
         'nhưng sẽ cần chi phí bảo dưỡng lớn định kỳ. Ba, nhà máy điện có vòng đời và hợp đồng mua bán điện có thời hạn, nên thị trường không trả giá như cho '
         'doanh nghiệp tăng trưởng mãi.',
  'cards': [('P/E', '4,46 lần', '4 quý gần nhất'), ('P/B · ROE', '1,27 · 29,4%', ''), ('Cổ tức', '≈ 3,1%', 'theo giá hiện tại')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'NT2 – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk',
  'say': 'Chương bốn, rủi ro cần theo dõi. Một, thủy văn: năm nhiều nước, sản lượng khí giảm, lợi nhuận đi xuống. Hai, giá khí đầu vào và cơ chế chuyển chi '
         'phí sang giá điện. Ba, lịch đại tu nhà máy: quý đại tu thường lãi thấp. Bốn, thanh khoản và tỷ trọng: giá cổ phiếu đã giảm từ đỉnh tuần khoảng hai '
         'mươi tám phẩy hai hai nghìn tháng ba năm hai nghìn không trăm hai mươi sáu về khoảng hai mươi hai phẩy hai nghìn, nên dù P trên E thấp, giá vẫn có '
         'thể biến động mạnh. Với cổ phiếu chu kỳ, nên đọc P trên E trung bình nhiều năm thay vì một năm.',
  'items': [('Thủy văn năm tới', (255, 196, 0)),
            ('Giá khí và cơ chế giá điện', (255, 196, 0)),
            ('Lịch đại tu', (255, 196, 0)),
            ('Đọc P/E trung bình nhiều năm', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('P/E 4,46', 'RẺ HAY ĐÚNG GIÁ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Với doanh nghiệp điện có lợi nhuận lên xuống theo thời tiết, anh chị dùng P trên E của một năm hay của trung bình ba đến năm '
         'năm để định giá?'}]

S['K2_1111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': '5 mã cổ tức cao',
  'cap': ('CỔ TỨC 11%', 'LẤY TỪ ĐÂU?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'dividend money',
  'say': 'Năm cổ phiếu đang có tỷ suất cổ tức từ khoảng bảy phẩy năm phần trăm đến mười một phần trăm theo giá hiện tại: TNG, BMP, VNM, QNS và SSI. Cao hơn '
         'lãi tiết kiệm mười hai tháng phổ biến. Nhưng tiền cổ tức phải đến từ lợi nhuận, và có mã đang trả gần bằng, thậm chí hơn lợi nhuận kiếm được. Video '
         'này em đặt năm mã cạnh nhau theo ba con số: tỷ suất cổ tức, tỷ lệ chi trả ước tính, và chuỗi lợi nhuận, để anh chị phân biệt cổ tức bền và cổ tức dễ '
         'bị cắt. Dữ liệu ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'VNMW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[11, 73.11, 'Đỉnh tuần 19/1/26: 73,11', 0.6], [0, 54.52, 'Đáy tuần 3/11/25: 54,52', 1.6], [51, 57.8, 'Tuần 2/11/26: 57,80', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Tỷ suất cổ tức',
  'moc': True,
  'label': 'Tỷ suất cổ tức theo giá 6/11/2026 (%)',
  'cap': ('TỶ SUẤT', 'CỔ TỨC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'dividend bars',
  'say': 'Chương một, tỷ suất cổ tức, tức cổ tức tiền mặt năm gần nhất chia cho giá hiện tại. TNG khoảng mười một phẩy không một phần trăm, BMP khoảng mười '
         'phẩy bảy tám phần trăm, VNM khoảng tám phẩy một tám phần trăm, QNS khoảng tám phẩy một năm phần trăm, SSI khoảng bảy phẩy bốn bảy phần trăm. Anh chị '
         'lưu ý hai điều. Một, tỷ suất tăng khi giá giảm, nên tỷ suất cao đôi khi chỉ vì giá đã giảm mạnh. Hai, con số này dựa trên mức chi trả quá khứ, không '
         'phải cam kết cho năm sau.',
  'bars': [('TNG', 11.01, (34, 197, 94), '11,01%'),
           ('BMP', 10.78, (34, 197, 94), '10,78%'),
           ('VNM', 8.18, (34, 197, 94), '8,18%'),
           ('QNS', 8.15, (34, 197, 94), '8,15%'),
           ('SSI', 7.47, (34, 197, 94), '7,47%')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Tỷ lệ chi trả ước tính',
  'moc': True,
  'label': 'Tỷ lệ chi trả ước tính = tỷ suất cổ tức × P/E (%)',
  'cap': ('TRẢ BAO NHIÊU', '% LỢI NHUẬN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'payout ratio',
  'say': 'Chương hai, tỷ lệ chi trả ước tính, tính bằng tỷ suất cổ tức nhân với P trên E. Đây là con số gần đúng, cho biết doanh nghiệp đang trả bao nhiêu '
         'phần trăm lợi nhuận thành cổ tức. TNG khoảng năm mươi lăm phần trăm, QNS khoảng bảy mươi ba phần trăm, VNM khoảng tám mươi sáu phần trăm, BMP khoảng '
         'chín mươi bảy phần trăm, SSI khoảng một trăm linh ba phần trăm. Tỷ lệ dưới bảy mươi phần trăm để lại dư địa: lợi nhuận giảm một chút vẫn trả được. '
         'Tỷ lệ gần hoặc trên một trăm phần trăm nghĩa là doanh nghiệp trả gần hết, hoặc hơn, số lợi nhuận một năm. Mức đó chỉ bền khi lợi nhuận ổn định hoặc '
         'doanh nghiệp có tiền tích lũy lớn.',
  'bars': [('TNG', 55, (34, 197, 94), '≈ 55%'),
           ('QNS', 73, (255, 196, 0), '≈ 73%'),
           ('VNM', 86, (255, 196, 0), '≈ 86%'),
           ('BMP', 97, (239, 68, 68), '≈ 97%'),
           ('SSI', 103, (239, 68, 68), '≈ 103%')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Lợi nhuận có đỡ được không',
  'moc': True,
  'label': 'LNST quý 3/2026 so với cùng kỳ',
  'cap': ('LỢI NHUẬN', 'ĐỠ CỔ TỨC?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'earnings',
  'say': 'Chương ba, lợi nhuận có đỡ được cổ tức không. quý ba năm hai nghìn không trăm hai mươi sáu, TNG lãi khoảng một trăm năm mươi hai tỷ, tăng hai mươi '
         'chín phẩy năm phần trăm. QNS lãi khoảng bốn trăm năm mươi tỷ, tăng mười tám phẩy một phần trăm. VNM lãi khoảng hai nghìn chín trăm sáu mươi tư tỷ, '
         'tăng mười bảy phẩy ba phần trăm. Trong khi đó BMP lãi khoảng ba trăm mười chín tỷ, giảm tám phẩy chín phần trăm, và SSI lãi khoảng một nghìn một '
         'trăm hai mươi lăm tỷ, giảm hai mươi ba phẩy bảy phần trăm. Hai mã có tỷ lệ chi trả cao nhất lại đúng là hai mã lợi nhuận quý ba giảm. Nếu xu hướng '
         'đó kéo dài, cổ tức năm sau có thể thấp hơn, và tỷ suất mười phần trăm hôm nay sẽ không lặp lại.',
  'cards': [('TNG · QNS · VNM', '+29,5% · +18,1% · +17,3%', 'lợi nhuận đỡ được'), ('BMP', '−8,9%', 'chi trả ≈ 97%'), ('SSI', '−23,7%', 'chi trả ≈ 103%')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Bẫy cổ tức',
  'moc': True,
  'label': 'Bốn dấu hiệu bẫy cổ tức',
  'cap': ('BẪY', 'CỔ TỨC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'trap warning',
  'say': 'Chương bốn, bốn dấu hiệu của bẫy cổ tức. Một, tỷ suất cao vì giá giảm mạnh, không phải vì cổ tức tăng. Hai, tỷ lệ chi trả trên chín mươi phần trăm '
         'trong khi lợi nhuận đang giảm. Ba, dòng tiền kinh doanh thấp hơn tiền chi cổ tức nhiều năm, doanh nghiệp phải vay hoặc bán tài sản để trả. Bốn, '
         'ngành có chu kỳ mạnh như chứng khoán, nơi lợi nhuận năm tốt không lặp lại năm sau. Cổ tức cao là điểm cộng, nhưng chỉ khi nó đến từ lợi nhuận bền và '
         'dòng tiền thật.',
  'items': [('Tỷ suất cao do giá giảm', (239, 68, 68)),
            ('Chi trả > 90%, lợi nhuận giảm', (239, 68, 68)),
            ('Dòng tiền < cổ tức nhiều năm', (255, 196, 0)),
            ('Ngành chu kỳ mạnh', (255, 196, 0))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('CỔ TỨC 11%', 'BỀN HAY BẪY?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Khi chọn cổ phiếu cổ tức, anh chị nhìn tỷ suất cổ tức trước, hay nhìn tỷ lệ chi trả và lợi nhuận trước?'}]

S['LST_1111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Thứ Tư Đen 16/9/1992',
  'cap': ('1 NGÀY', 'LÃI 1 TỶ USD?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'Bank of England London',
  'say': 'Ngày mười sáu tháng chín năm một nghìn chín trăm chín mươi hai, chính phủ Anh nâng lãi suất từ mười phần trăm lên mười hai phần trăm chỉ trong một '
         'buổi sáng, rồi tuyên bố sẽ nâng lên mười lăm phần trăm. Đến tối, họ bỏ cuộc và rút đồng bảng khỏi cơ chế tỷ giá châu Âu. Người ta gọi ngày đó là Thứ '
         'Tư Đen. Phía bên kia, quỹ của George Soros được cho là lãi khoảng một tỷ đô la Mỹ. Một chính phủ thua một quỹ đầu tư như thế nào? Video này em kể '
         'lại sự kiện theo bốn phần và rút ra bài học về chống lại thị trường bằng nguồn lực có hạn. Biểu đồ phía sau là VN-Index, chỉ để minh họa.',
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933,11', 0.6],
                        [1, 1578.42, 'Đáy tuần 10/11/25: 1.578,42', 1.6],
                        [51, 1725.36, 'Tuần 2/11/26: 1.725,36', 2.6]]}},
 {'k': 'cards',
  'ch': 'Chương 1 – Lời cam kết cứng',
  'moc': True,
  'label': 'Anh tham gia cơ chế tỷ giá châu Âu, 10/1990',
  'cap': ('LỜI CAM KẾT', 'CỨNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'pound sterling',
  'say': 'Chương một, lời cam kết cứng. Tháng mười năm một nghìn chín trăm chín mươi, Anh tham gia cơ chế tỷ giá hối đoái châu Âu, cam kết giữ đồng bảng quanh '
         'mức khoảng hai phẩy chín năm mác Đức, với biên độ dao động cho phép khoảng sáu phần trăm. Vấn đề là kinh tế Anh và Đức đi theo hai hướng khác nhau. '
         'Đức sau thống nhất giữ lãi suất cao để chống lạm phát. Anh đang suy thoái, cần lãi suất thấp. Muốn giữ tỷ giá, Anh buộc phải giữ lãi suất cao trong '
         'lúc nền kinh tế cần điều ngược lại. Một cam kết đi ngược nhu cầu thực tế là điểm yếu mà thị trường nhìn thấy.',
  'cards': [('10/1990', 'Anh vào cơ chế tỷ giá', ''), ('Mức neo', '≈ 2,95 mác Đức', 'biên độ ≈ 6%'), ('Mâu thuẫn', 'Anh suy thoái', 'Đức lãi suất cao')]},
 {'k': 'checklist',
  'ch': 'Chương 2 – Một ngày thứ Tư',
  'moc': True,
  'label': 'Diễn biến ngày 16/9/1992',
  'cap': ('MỘT NGÀY', 'THỨ TƯ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'trading desk',
  'say': 'Chương hai, diễn biến một ngày. Các quỹ đầu tư bán khống đồng bảng với quy mô lớn, quỹ Quantum của Soros được cho là bán khoảng mười tỷ đô la. Ngân '
         'hàng Trung ương Anh mua đồng bảng để đỡ giá, nhưng không đủ. Buổi sáng, lãi suất được nâng từ mười phần trăm lên mười hai phần trăm. Đồng bảng vẫn '
         'không lên. Buổi chiều, chính phủ công bố sẽ nâng tiếp lên mười lăm phần trăm. Thị trường không tin. Buổi tối, Anh rút khỏi cơ chế tỷ giá, đồng bảng '
         'thả nổi và giảm mạnh so với mác Đức trong những tuần sau.',
  'items': [('Quỹ bán khống bảng Anh quy mô lớn', (255, 196, 0)),
            ('Sáng: lãi suất 10% → 12%', (239, 68, 68)),
            ('Chiều: công bố lên 15%', (239, 68, 68)),
            ('Tối: rút khỏi cơ chế tỷ giá', (239, 68, 68))]},
 {'k': 'cards',
  'ch': 'Chương 3 – Ai thắng ai thua',
  'moc': True,
  'label': 'Cái giá của việc đỡ tỷ giá',
  'cap': ('AI THẮNG', 'AI THUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'winners losers',
  'say': 'Chương ba, ai thắng ai thua. Quỹ của Soros lãi khoảng một tỷ đô la trong vài ngày. Bộ Tài chính Anh sau này ước tính chi phí của việc đỡ tỷ giá '
         'khoảng ba phẩy ba tỷ bảng. Nhưng câu chuyện có một khúc quanh: sau khi thả nổi tỷ giá, Anh hạ được lãi suất, nền kinh tế hồi phục trong những năm '
         'sau. Thứ Tư Đen là thất bại chính trị lớn, nhưng về kinh tế lại giải phóng nước Anh khỏi một cam kết không phù hợp. Người thua nhiều nhất là những '
         'ai đặt cược rằng cam kết sẽ được giữ bằng mọi giá.',
  'cards': [('Quỹ Quantum', '≈ 1 tỷ USD', 'lãi trong vài ngày'),
            ('Bộ Tài chính Anh', '≈ 3,3 tỷ bảng', 'chi phí ước tính'),
            ('Sau đó', 'Lãi suất giảm', 'kinh tế hồi phục')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Bài học cho nhà đầu tư',
  'moc': True,
  'label': 'Bốn bài học từ Thứ Tư Đen',
  'cap': ('BỐN BÀI HỌC', '1992'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'lessons',
  'say': 'Chương bốn, bốn bài học cho nhà đầu tư cá nhân. Một, đừng chống lại xu hướng bằng nguồn lực có hạn: một chính phủ còn thua, một tài khoản cá nhân '
         'càng không nên bình quân giá xuống vô hạn. Hai, cam kết cứng là điểm yếu: nói rằng mình sẽ giữ mã này bằng mọi giá cũng giống như cam kết giữ tỷ '
         'giá. Ba, khi nền tảng thay đổi, chấp nhận sai sớm thường rẻ hơn sai muộn. Bốn, Soros thắng nhờ đặt cược có giới hạn rủi ro rõ ràng: nếu sai, đồng '
         'bảng khó tăng mạnh, nên khoản lỗ tối đa nhỏ hơn nhiều khoản lãi tiềm năng.',
  'items': [('Không chống xu hướng bằng nguồn lực có hạn', (239, 68, 68)),
            ('Cam kết cứng là điểm yếu', (255, 196, 0)),
            ('Sai sớm rẻ hơn sai muộn', (255, 196, 0)),
            ('Cược có giới hạn rủi ro rõ ràng', (34, 197, 94))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('CHÍNH PHỦ CÒN THUA', 'KHI CHỐNG THỊ TRƯỜNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Anh chị đã bao giờ giữ một mã cổ phiếu bằng mọi giá, mua thêm khi giá giảm, và nếu được làm lại, anh chị sẽ đặt giới hạn ở '
         'đâu?'}]

S['TS1111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'GAS – góp đều 38 tháng',
  'cap': ('TỪNG LÃI 92%', 'GIỜ CÒN 10%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'gas pipeline',
  'say': 'Góp đều ba triệu đồng mỗi tháng vào cổ phiếu GAS từ tháng mười năm hai nghìn không trăm hai mươi ba. Ngày bốn tháng ba năm hai nghìn không trăm hai '
         'mươi sáu, danh mục từng lãi khoảng chín mươi hai phần trăm. Hôm nay, sau ba mươi tám tháng và một trăm mười bốn triệu tiền vốn, giá trị khoảng một '
         'trăm hai mươi lăm phẩy bốn triệu, lãi khoảng mười phần trăm. Phần lớn khoản lãi trên giấy đã biến mất trong bốn tháng. Người tích sản nên làm gì khi '
         'một mã tăng quá nhanh? Video này em dùng giá đóng cửa thật để trả lời, chưa tính cổ tức tiền mặt. Kết quả quá khứ, không phải cam kết lợi nhuận.',
  'chart': {'sym': 'GASW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 127.79, 'Đỉnh tuần 2/3/26: 127,79', 0.6], [0, 58.4, 'Đáy tuần 3/11/25: 58,40', 1.6], [51, 74.1, 'Tuần 2/11/26: 74,10', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Hành trình 38 tháng',
  'moc': True,
  'label': 'Lãi/lỗ trên vốn góp đều GAS tại các mốc (%)',
  'cap': ('HÀNH TRÌNH', '38 THÁNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'rollercoaster',
  'say': 'Chương một, hành trình ba mươi tám tháng. Ngày chín tháng bốn năm hai nghìn không trăm hai mươi lăm, danh mục góp đều GAS có lúc lỗ khoảng hai mươi '
         'bảy phẩy bảy phần trăm, mức thấp nhất. Gần một năm sau, ngày bốn tháng ba năm hai nghìn không trăm hai mươi sáu, giá GAS lên khoảng một trăm hai '
         'mươi lăm nghìn đồng, danh mục lãi khoảng chín mươi hai phần trăm. Đến tháng bảy năm hai nghìn không trăm hai mươi sáu, giá giảm về khoảng sáu mươi '
         'hai phẩy sáu nghìn, giảm năm mươi phần trăm từ đỉnh. Hôm nay giá khoảng bảy mươi tư phẩy một nghìn, danh mục lãi khoảng mười phần trăm. Người kiên '
         'nhẫn đã đi qua cả hai cực: lỗ gần hai mươi tám phần trăm và lãi chín mươi hai phần trăm, chỉ cách nhau mười một tháng.',
  'bars': [('9/4/2025', 27.7, (239, 68, 68), '−27,7%'), ('4/3/2026', 92.0, (34, 197, 94), '+92,0%'), ('6/11/2026', 10.0, (255, 196, 0), '+10,0%')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Doanh nghiệp làm ăn thế nào',
  'moc': True,
  'label': 'GAS – lợi nhuận Q3/2026',
  'cap': ('DOANH NGHIỆP', 'VẪN LÃI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit',
  'say': 'Chương hai, doanh nghiệp vẫn làm ăn tốt. quý ba năm hai nghìn không trăm hai mươi sáu GAS lãi sau thuế khoảng bốn nghìn năm trăm bảy mươi sáu tỷ '
         'đồng, tăng bảy mươi chín phẩy năm phần trăm so với cùng kỳ. Lũy kế chín tháng khoảng mười ba nghìn ba trăm tám mươi mốt tỷ, tăng ba mươi ba phẩy một '
         'phần trăm. Biên gộp khoảng mười lăm phẩy bảy phần trăm, cùng kỳ mười một phẩy năm phần trăm. ROE khoảng hai mươi mốt phẩy một phần trăm. Như vậy cú '
         'giảm năm mươi phần trăm của giá không đến từ việc doanh nghiệp đi xuống, mà từ việc giá đã tăng quá nhanh so với lợi nhuận đầu năm hai nghìn không '
         'trăm hai mươi sáu, rồi quay về. Giá cổ phiếu có thể lệch khỏi giá trị doanh nghiệp rất xa trong vài tháng.',
  'cards': [('LNST Q3/2026', '4.576 tỷ', '+79,5%'), ('9 tháng', '13.381 tỷ', '+33,1%'), ('ROE', '21,1%', 'P/E 12,21')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Tỷ trọng phình to',
  'moc': True,
  'label': 'Khi một mã tăng 92%, danh mục thay đổi thế nào',
  'cap': ('TỶ TRỌNG', 'PHÌNH TO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'portfolio pie',
  'say': 'Chương ba, vấn đề tỷ trọng. Giả sử anh chị tích sản ba mã với tỷ trọng ngang nhau. Khi GAS lãi chín mươi hai phần trăm còn hai mã kia đi ngang, GAS '
         'tự động chiếm gần một nửa danh mục. Không ai quyết định điều đó, nó tự xảy ra. Đến khi GAS giảm năm mươi phần trăm, cả danh mục chịu thiệt lớn hơn '
         'nhiều so với kế hoạch ban đầu. Đây là lúc nguyên tắc tái cân bằng phát huy tác dụng: khi một mã vượt tỷ trọng mục tiêu, bán bớt phần vượt để đưa về '
         'mức cũ, dồn sang mã còn thấp.',
  'cards': [('Ban đầu', '3 mã × 33%', ''), ('GAS +92%', '≈ 49% danh mục', 'tự phình'), ('Tái cân bằng', 'Bán phần vượt', 'về 33%')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Quy tắc cho người tích sản',
  'moc': True,
  'label': 'Ba quy tắc khi một mã tăng quá nhanh',
  'cap': ('KHI MÃ', 'TĂNG QUÁ NHANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'rules',
  'say': 'Chương bốn, ba quy tắc cho người tích sản. Một, đặt tỷ trọng mục tiêu cho mỗi mã từ đầu, ví dụ không quá hai mươi đến ba mươi phần trăm. Hai, mỗi '
         'quý kiểm tra một lần, mã nào vượt mục tiêu quá năm điểm phần trăm thì cân bằng lại. Ba, khi lãi trên giấy vượt xa tốc độ tăng lợi nhuận của doanh '
         'nghiệp, chốt lời từng phần là cách khóa thành quả mà vẫn giữ vị thế. Tích sản không có nghĩa là không bao giờ bán, mà là bán có quy tắc.',
  'items': [('Tỷ trọng mục tiêu ≤ 20–30%/mã', (34, 197, 94)),
            ('Kiểm tra mỗi quý, lệch > 5 điểm → cân bằng', (255, 196, 0)),
            ('Lãi vượt xa lợi nhuận → chốt từng phần', (255, 196, 0))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LÃI 92%', 'KHÔNG CHỐT – CÒN 10%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Nếu danh mục tích sản của anh chị có một mã lãi chín mươi hai phần trăm sau hai năm, anh chị sẽ giữ nguyên, chốt một phần, '
         'hay cân bằng lại về tỷ trọng ban đầu?'}]

S['Y2_1111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Soi BCTC PLX – Q3/2026',
  'cap': ('Q1 LỖ 763 TỶ', 'Q2 LÃI 2.800 TỶ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'petrol station',
  'say': 'Petrolimex, mã PLX, quý một năm hai nghìn không trăm hai mươi sáu lỗ khoảng bảy trăm sáu mươi ba tỷ đồng. Chỉ một quý sau, quý hai năm hai nghìn '
         'không trăm hai mươi sáu lãi khoảng hai nghìn tám trăm tỷ. quý ba năm hai nghìn không trăm hai mươi sáu lãi khoảng một nghìn hai trăm bốn mươi mốt '
         'tỷ, tăng một trăm linh ba phẩy hai phần trăm so với cùng kỳ nhưng giảm năm mươi lăm phẩy bảy phần trăm so với quý hai. Lợi nhuận một doanh nghiệp '
         'phân phối xăng dầu sao lại lên xuống mạnh như vậy? Câu trả lời nằm ở hàng tồn kho và giá dầu. Video này em soi báo cáo PLX theo năm dòng: doanh thu, '
         'lợi nhuận, tồn kho, định giá và rủi ro. Số liệu quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai '
         'nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'PLXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 67.96, 'Đỉnh tuần 2/3/26: 67,96', 0.6], [36, 30.8, 'Đáy tuần 20/7/26: 30,80', 1.6], [51, 33.35, 'Tuần 2/11/26: 33,35', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Doanh thu',
  'moc': True,
  'label': 'Doanh thu thuần PLX (tỷ đồng)',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'fuel',
  'say': 'Dòng thứ nhất, doanh thu. quý ba năm hai nghìn không trăm hai mươi sáu PLX đạt khoảng một trăm ba mươi tám nghìn bốn trăm tám mươi hai tỷ đồng doanh '
         'thu thuần, tăng sáu mươi lăm phẩy sáu phần trăm so với cùng kỳ. Anh chị nhìn bước nhảy từ khoảng chín mươi tám nghìn sáu trăm chín mươi tám tỷ ở quý '
         'một năm hai nghìn không trăm hai mươi sáu lên trên một trăm ba mươi sáu nghìn tỷ ở hai quý sau. Doanh thu xăng dầu chủ yếu đi theo giá bán, mà giá '
         'bán đi theo giá dầu thế giới. Khi giá dầu tăng mạnh trong năm hai nghìn không trăm hai mươi sáu, doanh thu tăng theo, dù sản lượng bán ra không nhất '
         'thiết tăng tương ứng.',
  'bars': [('Q4/24', 71027.4, (56, 189, 248), '71.027'),
           ('Q1/25', 67861.0, (56, 189, 248), '67.861'),
           ('Q2/25', 76539.0, (56, 189, 248), '76.539'),
           ('Q3/25', 83631.4, (56, 189, 248), '83.631'),
           ('Q4/25', 81843.1, (56, 189, 248), '81.843'),
           ('Q1/26', 98697.9, (56, 189, 248), '98.698'),
           ('Q2/26', 136046.3, (56, 189, 248), '136.046'),
           ('Q3/26', 138481.8, (34, 197, 94), '138.482')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Lợi nhuận',
  'moc': True,
  'label': 'LNST công ty mẹ PLX (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'LÊN XUỐNG MẠNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'profit swing',
  'say': 'Dòng thứ hai, lợi nhuận. Chuỗi tám quý của PLX lên xuống rất mạnh: quý một năm hai nghìn không trăm hai mươi lăm khoảng một trăm ba mươi ba tỷ, quý '
         'hai năm hai nghìn không trăm hai mươi lăm khoảng một nghìn ba trăm sáu mươi sáu tỷ, quý một năm hai nghìn không trăm hai mươi sáu lỗ khoảng bảy trăm '
         'sáu mươi ba tỷ, quý hai năm hai nghìn không trăm hai mươi sáu lãi khoảng hai nghìn tám trăm tỷ, quý ba năm hai nghìn không trăm hai mươi sáu khoảng '
         'một nghìn hai trăm bốn mươi mốt tỷ. Lũy kế chín tháng năm hai nghìn không trăm hai mươi sáu khoảng ba nghìn hai trăm bảy mươi tám tỷ, tăng năm mươi '
         'lăm phẩy ba phần trăm. Với doanh thu hơn một trăm ba mươi nghìn tỷ mỗi quý, lợi nhuận chỉ khoảng một phần trăm doanh thu. Biên rất mỏng, nên một '
         'thay đổi nhỏ trong giá vốn cũng làm lợi nhuận đảo chiều.',
  'bars': [('Q4/24', 545.3, (34, 197, 94), '545'),
           ('Q1/25', 133.4, (34, 197, 94), '133'),
           ('Q2/25', 1366.4, (34, 197, 94), '1.366'),
           ('Q3/25', 610.7, (34, 197, 94), '611'),
           ('Q4/25', 564.7, (34, 197, 94), '565'),
           ('Q1/26', 763.0, (239, 68, 68), '-763'),
           ('Q2/26', 2799.7, (34, 197, 94), '2.800'),
           ('Q3/26', 1240.9, (34, 197, 94), '1.241')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Tồn kho và giá dầu',
  'moc': True,
  'label': 'Lãi, lỗ tồn kho',
  'cap': ('TỒN KHO', 'VÀ GIÁ DẦU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'oil barrels',
  'say': 'Dòng thứ ba, tồn kho. Doanh nghiệp xăng dầu luôn giữ một lượng hàng tồn lớn. Khi giá dầu tăng, hàng mua giá cũ được bán theo giá mới, tạo ra lãi tồn '
         'kho. Khi giá dầu giảm nhanh, hàng mua giá cao phải bán theo giá thấp, tạo ra lỗ tồn kho. Đây là lý do một quý lỗ rồi quý sau lãi lớn. Phần lãi lỗ '
         'này không phản ánh hiệu quả kinh doanh cốt lõi. Đầu tháng mười một năm hai nghìn không trăm hai mươi sáu, giá dầu Brent có hai phiên giảm khoảng '
         'mười phẩy chín bốn phần trăm và tám phẩy sáu bảy phần trăm, nên anh chị cần chú ý tác động lên quý bốn.',
  'cards': [('Dầu tăng', 'Lãi tồn kho', 'hàng giá cũ bán giá mới'),
            ('Dầu giảm nhanh', 'Lỗ tồn kho', 'hàng giá cao bán giá thấp'),
            ('Đầu 11/2026', 'Brent −10,94%, −8,67%', 'hai phiên')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'moc': True,
  'label': 'PLX – định giá ngày 6/11/2026',
  'cap': ('P/E 11,14', 'P/B 1,53'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'valuation',
  'say': 'Dòng thứ tư, định giá. PLX có P trên E khoảng mười một phẩy một bốn lần, P trên B khoảng một phẩy năm ba lần, ROE khoảng mười ba phẩy không phần '
         'trăm, cổ tức khoảng ba phẩy sáu bảy phần trăm, vốn hóa khoảng bốn mươi hai nghìn tám trăm mười chín tỷ đồng. Giá đóng cửa tuần gần nhất khoảng ba '
         'mươi ba phẩy ba năm nghìn đồng, thấp hơn nhiều so với đỉnh tuần khoảng sáu mươi bảy phẩy chín sáu nghìn tháng ba năm hai nghìn không trăm hai mươi '
         'sáu. Với doanh nghiệp có lãi lỗ tồn kho lớn, P trên E bốn quý gần nhất dễ bị méo. Cách đọc hợp lý hơn là ước lượng lợi nhuận cốt lõi bình quân nhiều '
         'năm.',
  'cards': [('P/E', '11,14 lần', '6/11/2026'), ('P/B · ROE', '1,53 · 13,0%', ''), ('Giá', '33,35', 'đỉnh tuần 3/2026: 67,96')]},
 {'k': 'checklist',
  'ch': 'Chương 5 – Rủi ro cần theo dõi',
  'moc': True,
  'label': 'PLX – rủi ro cần theo dõi',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'risk',
  'say': 'Dòng thứ năm, rủi ro. Một, giá dầu giảm nhanh đầu tháng mười một có thể tạo lỗ tồn kho trong quý bốn. Hai, cơ chế điều hành giá xăng dầu trong nước '
         'quyết định chiết khấu và biên của nhà phân phối. Ba, biên lợi nhuận khoảng một phần trăm doanh thu, rất nhạy với chi phí. Bốn, giá cổ phiếu đã giảm '
         'hơn năm mươi phần trăm từ đỉnh tháng ba, biến động mạnh hơn nhiều người nghĩ về một doanh nghiệp phân phối lớn.',
  'items': [('Lỗ tồn kho quý 4', (239, 68, 68)),
            ('Cơ chế điều hành giá', (255, 196, 0)),
            ('Biên ≈ 1% doanh thu', (255, 196, 0)),
            ('Giá cổ phiếu biến động mạnh', (239, 68, 68))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LỖ 763 TỶ', 'RỒI LÃI 2.800 TỶ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Với doanh nghiệp có lãi lỗ tồn kho lớn như PLX, anh chị sẽ dùng lợi nhuận của quý nào, hay trung bình bao nhiêu năm, để định '
         'giá?'}]

S['Y3_1111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Dầu Brent đầu tháng 11/2026',
  'cap': ('DẦU −20%', 'TRONG 3 PHIÊN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'oil price crash',
  'say': 'Ngày hai tháng mười một năm hai nghìn không trăm hai mươi sáu, giá dầu Brent giảm mười phẩy chín bốn phần trăm. Ngày bốn tháng mười một giảm tiếp '
         'tám phẩy sáu bảy phần trăm, xuống khoảng chín mươi tư phẩy sáu hai đô la Mỹ một thùng. Tính từ trước phiên ngày hai tháng mười một, dầu mất gần hai '
         'mươi phần trăm chỉ trong ba phiên. Với Việt Nam, dầu giảm là tin tốt cho hàng không, vận tải và lạm phát, nhưng là tin xấu cho một số doanh nghiệp '
         'dầu khí. Video này em đi qua dữ liệu giá dầu, phản ứng của cổ phiếu BSR, PVD, PLX, GAS, và những gì nhà đầu tư nên đọc trong báo cáo quý bốn. Số '
         'liệu đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'chart': {'sym': 'BSRW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[17, 39.16, 'Đỉnh tuần 9/3/26: 39,16', 0.6], [5, 13.35, 'Đáy tuần 8/12/25: 13,35', 1.6], [51, 26.25, 'Tuần 2/11/26: 26,25', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Năm phiên của giá dầu',
  'moc': True,
  'label': 'Brent các phiên đầu tháng 11/2026 (USD/thùng)',
  'cap': ('BRENT', '5 PHIÊN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'oil chart',
  'say': 'Chương một, năm phiên của giá dầu. Brent đóng cửa phiên ngày hai tháng mười một khoảng một trăm linh bốn phẩy bảy bảy đô la, giảm mười phẩy chín bốn '
         'phần trăm. Phiên ngày ba tháng mười một khoảng một trăm linh ba phẩy sáu không đô la. Phiên ngày bốn tháng mười một khoảng chín mươi tư phẩy sáu hai '
         'đô la, giảm tám phẩy sáu bảy phần trăm. Phiên ngày năm tháng mười một hồi lên khoảng chín mươi tám phẩy hai chín đô la, tăng ba phẩy tám tám phần '
         'trăm. Phiên ngày sáu tháng mười một khoảng chín mươi tám phẩy hai bốn đô la. Tính chung một tháng, Brent giảm khoảng sáu phẩy bốn phần trăm. Biến '
         'động hơn tám phần trăm trong một phiên là mức hiếm với một mặt hàng lớn như dầu, cho thấy thị trường đang rất nhạy với tin tức.',
  'bars': [('2/11', 104.77, (239, 68, 68), '104,77'),
           ('3/11', 103.6, (239, 68, 68), '103,60'),
           ('4/11', 94.62, (239, 68, 68), '94,62'),
           ('5/11', 98.29, (34, 197, 94), '98,29'),
           ('6/11', 98.24, (56, 189, 248), '98,24')]},
 {'k': 'cards',
  'ch': 'Chương 2 – Ai được, ai mất',
  'moc': True,
  'label': 'Dầu giảm: tác động theo ngành',
  'cap': ('AI ĐƯỢC', 'AI MẤT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'airplane and refinery',
  'say': 'Chương hai, ai được, ai mất. Nhóm được lợi là doanh nghiệp dùng nhiên liệu làm chi phí lớn: hàng không như VJC và HVN, vận tải, và doanh nghiệp nhựa '
         'dùng hạt nhựa từ dầu như BMP. Lạm phát chung cũng dịu đi. Nhóm chịu bất lợi là doanh nghiệp dầu khí: lọc dầu BSR, khoan PVD, dịch vụ PVS, khí GAS, '
         'và PLX với rủi ro lỗ tồn kho. Tuy vậy mỗi doanh nghiệp chịu tác động khác nhau, vì lọc dầu phụ thuộc chênh lệch giá sản phẩm với dầu thô chứ không '
         'chỉ giá dầu.',
  'cards': [('Được lợi', 'VJC, HVN, vận tải, BMP', 'chi phí nhiên liệu giảm'),
            ('Bất lợi', 'BSR, PVD, PVS, GAS, PLX', 'giá bán, tồn kho'),
            ('Vĩ mô', 'Lạm phát dịu', 'tốt cho lãi suất')]},
 {'k': 'bars',
  'ch': 'Chương 3 – Cổ phiếu phản ứng thế nào',
  'moc': True,
  'label': 'Giá đóng cửa 30/10 → 6/11/2026 (thay đổi %)',
  'cap': ('CỔ PHIẾU', 'PHẢN ỨNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'stock reaction',
  'say': 'Chương ba, cổ phiếu phản ứng thế nào trong tuần. Từ phiên ngày ba mươi tháng mười đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu: '
         'BSR từ khoảng hai mươi bảy phẩy sáu xuống hai mươi sáu phẩy hai năm nghìn đồng, giảm khoảng bốn phẩy chín phần trăm. PVD từ mười bảy phẩy chín năm '
         'xuống mười bảy phẩy một, giảm khoảng bốn phẩy bảy phần trăm. GAS từ bảy mươi tám phẩy không xuống bảy mươi tư phẩy một, giảm năm phẩy không phần '
         'trăm. PLX từ ba mươi tư phẩy không xuống ba mươi ba phẩy ba năm, giảm khoảng một phẩy chín phần trăm. Ở chiều ngược lại, HVN từ hai mươi phẩy bảy '
         'năm lên hai mươi mốt phẩy tám năm, tăng khoảng năm phẩy ba phần trăm, VJC từ một trăm ba mươi mốt phẩy sáu lên một trăm ba mươi tư phẩy bảy, tăng '
         'khoảng hai phẩy bốn phần trăm. Cổ phiếu Việt Nam phản ứng đúng hướng nhưng nhẹ hơn nhiều so với mức giảm của dầu.',
  'bars': [('HVN', 5.3, (34, 197, 94), '+5,3%'),
           ('VJC', 2.4, (34, 197, 94), '+2,4%'),
           ('PLX', 1.9, (239, 68, 68), '−1,9%'),
           ('PVD', 4.7, (239, 68, 68), '−4,7%'),
           ('BSR', 4.9, (239, 68, 68), '−4,9%'),
           ('GAS', 5.0, (239, 68, 68), '−5,0%')]},
 {'k': 'checklist',
  'ch': 'Chương 4 – Đọc gì trong báo cáo quý 4',
  'moc': True,
  'label': 'Bốn điểm cần đọc trong BCTC quý 4/2026',
  'cap': ('ĐỌC GÌ', 'QUÝ 4'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': 'report checklist',
  'say': 'Chương bốn, đọc gì trong báo cáo quý bốn. Một, PLX: có lỗ tồn kho không, và bao nhiêu. Hai, BSR: biên lọc dầu, tức chênh lệch giá xăng dầu thành '
         'phẩm với dầu thô, quan trọng hơn giá dầu tuyệt đối. Ba, hàng không: chi phí nhiên liệu trên mỗi ghế có giảm thật không, vì tỷ giá và hợp đồng phòng '
         'ngừa cũng ảnh hưởng. Bốn, với chính danh mục của anh chị, nếu nhóm dầu khí đang chiếm tỷ trọng lớn, hãy kiểm tra mức chịu đựng khi giá dầu biến động '
         'mười phần trăm một phiên.',
  'items': [('PLX: lãi lỗ tồn kho', (255, 196, 0)),
            ('BSR: biên lọc dầu', (255, 196, 0)),
            ('Hàng không: chi phí nhiên liệu/ghế', (34, 197, 94)),
            ('Tỷ trọng nhóm dầu khí của mình', (239, 68, 68))]},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('DẦU −20%', 'CỔ PHIẾU −5%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'anh': '',
  'say': 'Cảm ơn anh chị đã xem. Theo anh chị, cổ phiếu dầu khí Việt Nam đã phản ánh đủ cú giảm gần hai mươi phần trăm của giá dầu chưa, hay thị trường đang '
         'chờ báo cáo quý bốn?'}]

META = {'HI1011A': {'title': 'DHC: P/E 6,43, P/B 1,57, ROE 25,4% – Bao bì: rẻ hay đỉnh chu kỳ?', 'bia': ('DHC P/E 6,43', 'ROE 25,4%'), 'badge': 'P/E 6,43'},
 'K2_1011A': {'title': '9 ngân hàng: bộ đệm nợ xấu từ 243% đến 42% – thị trường có trả giá cho rủi ro?', 'bia': ('ĐỆM 243%', 'HAY 42%?'), 'badge': '9 NH'},
 'LST_1011A': {'title': 'Enron 2001: từ 90 USD xuống dưới 1 USD – lợi nhuận đẹp che giấu điều gì?', 'bia': ('90 USD', 'XUỐNG < 1 USD'), 'badge': '2001'},
 'TS1011A': {'title': 'REE góp đều 38 tháng gần hòa vốn, mua một lần lãi 36%: vì sao?', 'bia': ('GÓP ĐỀU 3 NĂM', 'HÒA VỐN?'), 'badge': '−0,2%'},
 'Y2_1011A': {'title': 'Soi BCTC PVTrans quý 3/2026: lãi +42,4% cùng kỳ nhưng −35,2% so với quý 2', 'bia': ('LÃI +42,4%', 'QUÝ −35%?'), 'badge': 'PVT'},
 'Y3_1011A': {'title': 'Nikkei −5,96%, KOSPI −6,02%, Nasdaq −5,52%: vì sao VN-Index chỉ −0,88%?', 'bia': ('NIKKEI −5,96%', 'VN −0,88%'), 'badge': '−6%'},
 'HI1111A': {'title': 'NT2: P/E 4,46, P/B 1,27, ROE 29,4% – Điện khí: rẻ hay đúng giá?', 'bia': ('NT2 P/E 4,46', 'ROE 29,4%'), 'badge': 'P/E 4,46'},
 'K2_1111A': {'title': 'TNG, BMP, VNM, QNS, SSI: cổ tức 7,5–11% – mã nào trả gần hết lợi nhuận?', 'bia': ('CỔ TỨC 11%', 'BỀN HAY BẪY?'), 'badge': '5 mã'},
 'LST_1111A': {'title': 'Thứ Tư Đen 1992: nước Anh nâng lãi suất 2 lần trong 1 ngày vẫn thua thị trường', 'bia': ('1 NGÀY', 'LÃI 1 TỶ USD'), 'badge': '1992'},
 'TS1111A': {'title': 'GAS góp đều 38 tháng: từng lãi 92%, giờ còn 10% – bài học tái cân bằng', 'bia': ('TỪNG LÃI 92%', 'CÒN 10%'), 'badge': '+10%'},
 'Y2_1111A': {'title': 'Soi BCTC Petrolimex quý 3/2026: Q1 lỗ 763 tỷ, Q2 lãi 2.800 tỷ – vì sao?', 'bia': ('Q1 LỖ 763 TỶ', 'Q2 LÃI 2.800'), 'badge': 'PLX'},
 'Y3_1111A': {'title': 'Dầu Brent giảm gần 20% trong 3 phiên: BSR, PVD, GAS, PLX và hàng không phản ứng ra sao?',
              'bia': ('DẦU −20%', '3 PHIÊN'),
              'badge': '−20%'}}
