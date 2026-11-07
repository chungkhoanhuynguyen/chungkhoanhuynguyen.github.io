# -*- coding: utf-8 -*-
# VIDEO DÀI – NV1 soạn 8/11/2026 (lô 20261108_0045: CH2311A, CH2311B, CH2311C, CH2411A, CH2411B, CH2411C, CH2511A, CH2511B, CH2511C). Đọc BCTC NAB/GAS/KLB/VJC/VAB/DPM + 3 video Quản trị rủi ro. Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['CH2311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'NAB – đọc BCTC',
  'cap': ('LÃI QUÝ +23,0%', 'P/B 0,97'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nam A Bank, mã NAB, báo lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt một nghìn hai trăm sáu mươi chín tỷ, tăng hai '
         'mươi ba phần trăm so với cùng kỳ. Lũy kế chín tháng đạt ba nghìn bảy trăm tám mươi bảy tỷ, tăng hai mươi bốn phẩy năm phần trăm. Cổ phiếu đóng cửa '
         'ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu ở khoảng mười hai phẩy sáu mươi nghìn đồng, thấp hơn đỉnh năm mươi hai tuần khoảng năm '
         'phẩy sáu phần trăm. Con số quý này có đủ để kết luận doanh nghiệp đang khỏe lên hay yếu đi không? Trong video này, em đọc lần lượt lợi nhuận tám '
         'quý, thu nhập lãi thuần, dự phòng và nợ xấu, định giá, rủi ro cần theo dõi và cách quản trị vốn khi nắm giữ NAB. Số liệu lấy từ báo cáo tài chính '
         'quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'bank building',
  'chart': {'sym': 'NABW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[34, 13.5, 'Đỉnh tuần 6/7/26: 13,50', 0.6], [18, 10.08, 'Đáy tuần 16/3/26: 10,08', 1.6], [51, 12.6, 'Tuần 2/11/26: 12,60', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý một năm hai nghìn không trăm hai mươi sáu với khoảng một nghìn ba trăm linh tám tỷ, thấp nhất ở quý bốn năm '
         'hai nghìn không trăm hai mươi bốn với khoảng chín trăm sáu mươi bảy tỷ, và có năm quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý '
         'bốn năm hai nghìn không trăm hai mươi lăm đạt một nghìn một trăm bốn mươi tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt một nghìn ba trăm '
         'linh tám tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt một nghìn hai trăm mười tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt một '
         'nghìn hai trăm sáu mươi chín tỷ. Khi đọc chuỗi này, anh chị đừng chỉ so với cùng kỳ năm trước. Hãy so thêm với quý liền trước và với lũy kế chín '
         'tháng, vì một quý có thể đẹp lên nhờ khoản thu bất thường, nhờ trích lập dự phòng ít đi, hoặc nhờ nền so sánh thấp. Chuỗi tám quý cho thấy lợi nhuận '
         'đang đi lên đều, đi ngang hay dao động mạnh, và đó mới là thứ giúp ước lượng quý tiếp theo.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('Q4/24', 966.8, (56, 189, 248), '967'),
           ('Q1/25', 976.1, (56, 189, 248), '976'),
           ('Q2/25', 1034.7, (56, 189, 248), '1.035'),
           ('Q3/25', 1031.3, (56, 189, 248), '1.031'),
           ('Q4/25', 1140.1, (56, 189, 248), '1.140'),
           ('Q1/26', 1308.5, (56, 189, 248), '1.308'),
           ('Q2/26', 1209.8, (56, 189, 248), '1.210'),
           ('Q3/26', 1268.9, (34, 197, 94), '1.269')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'label': '',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, thu nhập lãi thuần, tức phần chênh lệch giữa lãi cho vay thu vào và lãi huy động trả ra. Đây là mảng cốt lõi của ngân hàng. Thu nhập lãi '
         'thuần đạt một nghìn bảy trăm bảy mươi tám tỷ, giảm mười ba phẩy năm phần trăm. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến '
         'quý ba năm hai nghìn không trăm hai mươi sáu, thu nhập lãi thuần cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng hai nghìn ba '
         'trăm hai mươi tám tỷ, thấp nhất ở quý ba năm hai nghìn không trăm hai mươi sáu với khoảng một nghìn bảy trăm bảy mươi tám tỷ, và có bốn quý tăng so '
         'với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt hai nghìn ba trăm hai mươi tám tỷ, quý một năm '
         'hai nghìn không trăm hai mươi sáu đạt hai nghìn không trăm năm mươi bốn tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt hai nghìn hai trăm hai '
         'mươi bảy tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt một nghìn bảy trăm bảy mươi tám tỷ. Lãi dịch vụ tăng năm trăm bảy mươi tám phẩy chín '
         'phần trăm, đạt một nghìn một trăm bảy mươi chín tỷ. Khi lợi nhuận tăng mà thu nhập lãi thuần giảm, phần tăng thêm đến từ nơi khác: dịch vụ, kinh '
         'doanh chứng khoán, thu hồi nợ đã xử lý, hoặc chi phí dự phòng thấp hơn. Những nguồn này thường kém đều hơn mảng cho vay, nên anh chị cần hỏi: quý '
         'sau nguồn đó có lặp lại không?',
  'anh': 'bank loan',
  'bars': [('Q4/24', 2011.6, (56, 189, 248), '2.012'),
           ('Q1/25', 2112.2, (56, 189, 248), '2.112'),
           ('Q2/25', 2122.1, (56, 189, 248), '2.122'),
           ('Q3/25', 2054.8, (56, 189, 248), '2.055'),
           ('Q4/25', 2327.6, (56, 189, 248), '2.328'),
           ('Q1/26', 2053.7, (56, 189, 248), '2.054'),
           ('Q2/26', 2227.4, (56, 189, 248), '2.227'),
           ('Q3/26', 1777.8, (34, 197, 94), '1.778')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Dự phòng và nợ xấu',
  'label': '',
  'cap': ('DỰ PHÒNG', 'VÀ NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, dự phòng và nợ xấu. Tỷ lệ nợ xấu một phẩy sáu mươi mốt phần trăm. Bao phủ nợ xấu chỉ khoảng sáu mươi bảy phần trăm, bộ đệm dự phòng mỏng. '
         'Tỷ lệ bao phủ nợ xấu là số dự phòng đã trích chia cho tổng nợ xấu. Bao phủ một trăm phần trăm nghĩa là nếu toàn bộ nợ xấu mất trắng, ngân hàng đã có '
         'sẵn tiền dự phòng để bù. Bao phủ càng thấp thì bộ đệm càng mỏng, và lợi nhuận tương lai càng dễ bị bào mòn khi phải trích lập thêm. Hai con số này '
         'anh chị tra được trong thuyết minh báo cáo tài chính, mục chất lượng nợ cho vay.',
  'moc': True,
  'anh': 'risk management',
  'cards': [('Tỷ lệ nợ xấu 1,61%', '', ''), ('Bao phủ nợ xấu chỉ khoảng 67%', '', '')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, định giá. Với giá khoảng mười hai phẩy sáu mươi nghìn đồng, NAB có P trên E khoảng năm phẩy năm mươi hai lần, P trên B khoảng không phẩy '
         'chín mươi bảy lần, ROE khoảng mười chín phẩy tám phần trăm. Trong hai mươi mã cùng nhóm ngân hàng có vốn hóa từ một nghìn năm trăm tỷ, P trên E '
         'trung vị khoảng bảy phẩy hai mươi lần, P trên B trung vị khoảng một phẩy mười chín lần, ROE trung vị khoảng mười bảy phẩy ba phần trăm. Với ngân '
         'hàng, P trên B nên đọc cùng ROE. Một ngân hàng có ROE cao xứng đáng được trả P trên B cao hơn, còn P trên B thấp kèm ROE thấp thì chưa chắc là rẻ. '
         'Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '5,52', 'lần'), ('P/B', '0,97', 'lần'), ('ROE', '19,8%', 'trên vốn chủ')]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá cách đỉnh bao xa. Đỉnh năm mươi hai tuần của NAB khoảng mười ba phẩy ba mươi lăm nghìn đồng, đáy khoảng mười phẩy không tám nghìn '
         'đồng. Giá hiện tại thấp hơn đỉnh khoảng năm phẩy sáu phần trăm. Người mua ở đỉnh cần cổ phiếu tăng khoảng sáu phần trăm mới hòa vốn. Đây là toán học '
         'của thua lỗ: giảm càng sâu thì phần tăng cần thiết để hồi lại càng lớn hơn phần đã mất. Hệ số beta của NAB khoảng không phẩy bốn mươi tám, nghĩa là '
         'trong giai đoạn đo, giá dao động ít hơn thị trường chung. Beta không nói cổ phiếu tốt hay xấu, nó chỉ nói mức rung lắc mà anh chị phải chịu được.',
  'moc': True,
  'value': -5.6,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 13,35 – NAY 12,60',
  'sub': 'cần +6% để về đỉnh',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Thu nhập lãi thuần, mảng cho vay cốt lõi giảm mười ba phẩy năm phần trăm. Bao phủ nợ xấu chỉ khoảng sáu mươi bảy '
         'phần trăm, bộ đệm dự phòng mỏng. Với cổ phiếu ngân hàng, rủi ro lớn nhất thường không nằm ở một quý lợi nhuận, mà ở chất lượng tài sản: nợ xấu, nợ '
         'tái cơ cấu và mức độ tập trung cho vay vào bất động sản. Ngoài ra, cổ phiếu ngân hàng hay biến động cùng nhau, nên anh chị cần cộng tỷ trọng cả nhóm '
         'ngân hàng trong danh mục.',
  'anh': 'warning sign',
  'items': [('Thu nhập lãi thuần (mảng cho vay cốt lõi', (239, 68, 68)),
            ('Bao phủ nợ xấu chỉ khoảng 67%', (239, 68, 68)),
            ('Tỷ trọng cả nhóm ngành', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Quản trị vốn',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, quản trị vốn khi nắm giữ NAB. Em đề xuất ba câu hỏi phải trả lời trước khi mua. Một, mã này chiếm tối đa bao nhiêu phần trăm danh mục? '
         'Với một mã đơn lẻ, nhiều nhà đầu tư cá nhân giới hạn trong khoảng mười đến hai mươi phần trăm. Hai, nếu giá quay về đáy năm mươi hai tuần khoảng '
         'mười phẩy không tám nghìn đồng, tức thấp hơn giá hiện tại khoảng hai mươi phần trăm, thì danh mục mất bao nhiêu? Với tỷ trọng mười phần trăm, mức '
         'giảm đó làm danh mục mất khoảng hai phần trăm. Ba, điều gì xảy ra thì luận điểm sai? Ví dụ lợi nhuận hai quý liên tiếp giảm, hoặc nợ xấu xấu đi. '
         'Viết sẵn ba câu trả lời này ra giấy, anh chị sẽ bớt bị cảm xúc kéo đi khi giá biến động. Không dùng vay ký quỹ cho mã mình chưa trả lời được câu hỏi '
         'thứ ba.',
  'moc': True,
  'anh': 'balance scale',
  'cards': [('Tỷ trọng tối đa', '10–20%', 'một mã'), ('Nếu về đáy 52 tuần', '−20,0%', 'giá cổ phiếu'), ('Điểm sai', 'viết trước', 'khi mua')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước tự đọc',
  'label': '',
  'cap': ('NĂM BƯỚC', 'TỰ ĐỌC BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, năm bước anh chị có thể tự làm với mọi báo cáo ngân hàng. Một, lợi nhuận tám quý, lũy kế. Hai, thu nhập lãi thuần. Ba, dự phòng, nợ xấu, '
         'bao phủ. Bốn, P trên B cạnh ROE. Năm, tỷ trọng và điểm sai. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm '
         'com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận 8 quý, lũy kế', (34, 197, 94)),
            ('Thu nhập lãi thuần', (34, 197, 94)),
            ('Dự phòng, nợ xấu, bao phủ', (34, 197, 94)),
            ('P/B cạnh ROE', (34, 197, 94)),
            ('Tỷ trọng và điểm sai', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI QUÝ +23,0%', 'ĐỦ KẾT LUẬN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với NAB, anh chị đặt trọng số nhiều hơn vào kết quả quý gần nhất, hay vào chuỗi tám quý và rủi ro phía trước?'}]

S['CH2311B'] = [{'k': 'hook',
  'label': '',
  'cap': ('VN-INDEX −20%?', 'VIẾT KẾ HOẠCH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'VN Index đóng cửa tuần ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu ở khoảng một nghìn bảy trăm hai mươi lăm điểm, thấp hơn đỉnh '
         'tuần ngày mười tám tháng năm năm hai nghìn không trăm hai mươi sáu khoảng mười phẩy bảy phần trăm. Trong ba năm qua, chỉ số từng giảm khoảng hai '
         'mươi phần trăm chỉ trong khoảng bốn tuần, từ vùng một nghìn ba trăm bốn mươi ba điểm đầu tháng ba/hai nghìn không trăm hai mươi lăm về vùng một '
         'nghìn không trăm bảy mươi bốn điểm đầu tháng tư/hai nghìn không trăm hai mươi lăm. Câu hỏi của video này không phải thị trường sẽ đi đâu, vì không '
         'ai biết chắc. Câu hỏi là: nếu chỉ số giảm thêm hai mươi phần trăm, danh mục của anh chị mất bao nhiêu, và anh chị sẽ làm gì. Em đi qua năm bước để '
         'viết kế hoạch đó từ hôm nay, khi đầu óc còn bình tĩnh.',
  'anh': 'stock market crash screen',
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
  'cap': ('VÌ SAO PHẢI', 'VIẾT TRƯỚC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Vì sao phải viết trước? Khi thị trường giảm mạnh, mỗi ngày đều có một lý do nghe rất hợp lý để bán hết, và cũng có một lý do nghe rất hợp lý để mua '
         'thêm. Người không có kế hoạch sẽ chọn theo cảm xúc của phiên hôm đó. Nghiên cứu về tâm lý nhà đầu tư cho thấy nỗi đau khi mất tiền lớn hơn niềm vui '
         'khi được cùng một số tiền, nên trong lúc giảm, não bộ thường chọn hành động để giảm đau ngay, chứ không chọn hành động đúng. Một kế hoạch viết sẵn '
         'trên giấy là cách mượn cái đầu bình tĩnh của hôm nay để dùng cho ngày khó khăn.',
  'anh': 'notebook planning desk',
  'ch': 'Bước 0 – Vì sao phải viết trước'},
 {'k': 'text',
  'label': '',
  'cap': ('BƯỚC 1', 'ĐO BETA DANH MỤC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bước một, ước lượng danh mục của mình nhạy với thị trường cỡ nào. Hệ số beta của từng mã cho biết giá mã đó thường dao động bao nhiêu so với chỉ số '
         'chung. Theo dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, Vinamilk có beta khoảng không phẩy bốn mươi hai, Dược '
         'Hậu Giang khoảng không phẩy hai mươi hai, Nam A Bank khoảng không phẩy bốn mươi tám, trong khi nhiều mã chứng khoán và bất động sản có beta trên '
         'một. Beta danh mục xấp xỉ bằng beta từng mã nhân tỷ trọng rồi cộng lại. Nếu beta danh mục khoảng một phẩy ba, một cú giảm hai mươi phần trăm của chỉ '
         'số có thể tương ứng mức giảm khoảng hai mươi sáu phần trăm của danh mục. Đây chỉ là ước lượng, vì beta đo trong quá khứ và có thể thay đổi.',
  'anh': 'measuring tape',
  'ch': 'Bước 1 – Đo độ nhạy của danh mục',
  'moc': True},
 {'k': 'checklist',
  'label': '',
  'cap': ('BƯỚC 2', 'BẢNG BA KỊCH BẢN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bước hai, lập bảng ba kịch bản: chỉ số giảm mười phần trăm, giảm hai mươi phần trăm và giảm ba mươi phần trăm. Với mỗi kịch bản, nhân với beta danh '
         'mục để ra mức giảm ước tính, rồi đổi ra số tiền. Ví dụ danh mục một tỷ đồng, beta khoảng một phẩy hai. Giảm mười phần trăm thì danh mục mất khoảng '
         'một trăm hai mươi triệu. Giảm hai mươi phần trăm thì mất khoảng hai trăm bốn mươi triệu. Giảm ba mươi phần trăm thì mất khoảng ba trăm sáu mươi '
         'triệu. Khi nhìn thấy con số bằng tiền, nhiều người nhận ra mức rủi ro hiện tại lớn hơn mức mình chịu được. Nếu con số ba trăm sáu mươi triệu khiến '
         'anh chị mất ngủ, thì tỷ trọng cổ phiếu hôm nay đang quá cao so với khả năng chịu đựng.',
  'anh': 'spreadsheet table',
  'ch': 'Bước 2 – Bảng ba kịch bản',
  'items': [('Giảm 10% → mất ≈ 120 triệu', (255, 196, 0)), ('Giảm 20% → mất ≈ 240 triệu', (239, 68, 68)), ('Giảm 30% → mất ≈ 360 triệu', (239, 68, 68))]},
 {'k': 'bignum',
  'label': '',
  'cap': ('VAY KÝ QUỸ', 'NHÂN ĐÔI CÚ GIẢM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nếu danh mục có dùng vay ký quỹ, bảng kịch bản phải tính lại hoàn toàn. Với tỷ lệ vay một đồng vốn tự có một đồng vay, danh mục giảm hai mươi lăm '
         'phần trăm thì vốn tự có mất khoảng năm mươi phần trăm. Ở các mức giảm sâu hơn, công ty chứng khoán có thể yêu cầu nộp thêm tiền hoặc bán giải chấp, '
         'và lệnh bán đó xảy ra đúng lúc giá thấp. Vì vậy, trong kế hoạch cho kịch bản giảm hai mươi phần trăm, dòng đầu tiên nên là: không có khoản vay nào '
         'bị bán giải chấp ở mức giảm đó. Nếu chưa bảo đảm được, việc đầu tiên là giảm vay, trước mọi quyết định chọn mã.',
  'anh': 'chain link broken',
  'ch': 'Vay ký quỹ nhân đôi cú giảm',
  'moc': True,
  'value': -50,
  'fmt': '{:,.0f}',
  'unit': '%',
  'top': 'DANH MỤC −25%, VAY 1:1',
  'sub': 'vốn tự có mất khoảng một nửa',
  'col': (239, 68, 68)},
 {'k': 'text',
  'label': '',
  'cap': ('BƯỚC 3', 'TIỀN MẶT LÀ VŨ KHÍ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bước ba, quyết định tỷ trọng tiền mặt trước. Tiền mặt trong danh mục có hai việc: giảm mức mất khi thị trường giảm, và cho anh chị lựa chọn mua ở '
         'giá thấp hơn mà không phải bán thứ khác. Một danh mục một trăm phần trăm cổ phiếu khi chỉ số giảm hai mươi phần trăm chỉ còn hai lựa chọn: chịu đựng '
         'hoặc bán. Một danh mục giữ hai mươi phần trăm tiền mặt có thêm lựa chọn thứ ba: giải ngân từng phần theo kế hoạch. Tỷ trọng tiền mặt bao nhiêu là '
         'tùy mỗi người, nhưng nó phải là con số anh chị chọn trước, không phải con số còn sót lại sau khi đã mua hết.',
  'anh': 'cash wallet',
  'ch': 'Bước 3 – Tiền mặt là lựa chọn'},
 {'k': 'checklist',
  'label': '',
  'cap': ('BƯỚC 4', 'VIẾT SẴN HÀNH ĐỘNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bước bốn, viết sẵn hành động cho từng mốc. Ví dụ, khi chỉ số giảm mười phần trăm từ đỉnh: rà lại từng mã, mã nào có kết quả kinh doanh xấu đi thì '
         'giảm tỷ trọng. Khi giảm hai mươi phần trăm: giải ngân một phần ba lượng tiền mặt dự phòng vào những mã đã chọn sẵn, với điều kiện lợi nhuận doanh '
         'nghiệp vẫn giữ được. Khi giảm ba mươi phần trăm: giải ngân thêm một phần ba, và tuyệt đối không vay. Con số cụ thể của anh chị có thể khác, điều '
         'quan trọng là mỗi mốc có một hành động rõ, và hành động đó dựa trên doanh nghiệp, không dựa trên tin đồn trong ngày.',
  'anh': 'checklist clipboard',
  'ch': 'Bước 4 – Hành động cho từng mốc',
  'moc': True,
  'items': [('−10%: rà từng mã, giảm mã xấu đi', (255, 196, 0)),
            ('−20%: giải ngân 1 phần tiền dự phòng', (34, 197, 94)),
            ('−30%: giải ngân thêm, không vay', (34, 197, 94))]},
 {'k': 'text',
  'label': '',
  'cap': ('BƯỚC 5', 'DANH SÁCH CHỜ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Bước năm, chuẩn bị danh sách chờ ngay từ hôm nay. Khi thị trường giảm mạnh, không ai đủ thời gian và bình tĩnh để đọc báo cáo tài chính của hai mươi '
         'doanh nghiệp. Danh sách chờ gồm ba đến năm mã anh chị đã đọc kỹ: chuỗi lợi nhuận tám quý, nợ vay, dòng tiền, định giá hiện tại và mức giá mà anh chị '
         'thấy hợp lý. Bảng định giá từng mã có trên trang chứng khoán Huy Nguyễn chấm com, anh chị có thể dùng để lập danh sách này. Khi giá về vùng đã định, '
         'việc còn lại chỉ là làm theo kế hoạch.',
  'anh': 'watchlist screen',
  'ch': 'Bước 5 – Danh sách chờ'},
 {'k': 'text',
  'label': '',
  'cap': ('BA NĂM QUA', 'ĐÃ CÓ BAO LẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nhìn lại ba năm qua để thấy kịch bản này không xa vời. Từ tuần ngày hai mươi ba tháng mười năm hai nghìn không trăm hai mươi ba ở khoảng một nghìn '
         'không trăm sáu mươi mốt điểm, VN Index đi lên đỉnh tuần ngày mười tám tháng năm năm hai nghìn không trăm hai mươi sáu khoảng một nghìn chín trăm ba '
         'mươi ba điểm. Nhưng trên đường đi, có ít nhất một lần chỉ số mất khoảng hai mươi phần trăm trong vài tuần, vào tháng ba và tháng tư/hai nghìn không '
         'trăm hai mươi lăm. Người có kế hoạch nhìn đợt giảm đó như một bước trong bảng đã viết. Người không có kế hoạch thường bán ở gần đáy, rồi đứng ngoài '
         'khi chỉ số hồi lại. Cùng một thị trường, kết quả khác nhau nằm ở chuẩn bị.',
  'anh': 'mountain road',
  'ch': 'Ba năm qua đã có bao lần'},
 {'k': 'checklist',
  'label': '',
  'cap': ('NHỮNG SAI LẦM', 'HAY GẶP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba sai lầm hay gặp khi viết kế hoạch. Một, viết quá chung chung, kiểu sẽ mua khi rẻ, mà không ghi rẻ là bao nhiêu. Hai, chỉ viết kế hoạch mua, quên '
         'kế hoạch cho những mã kết quả kinh doanh xấu đi. Ba, viết xong rồi để đó, không xem lại mỗi quý khi báo cáo tài chính mới ra. Một kế hoạch tốt chỉ '
         'cần một trang giấy, nhưng phải có số cụ thể và phải được cập nhật.',
  'anh': 'mistake eraser',
  'ch': 'Những sai lầm hay gặp',
  'items': [('Viết chung chung, không có số', (239, 68, 68)), ('Chỉ có kế hoạch mua', (239, 68, 68)), ('Không cập nhật mỗi quý', (239, 68, 68))]},
 {'k': 'checklist',
  'label': '',
  'cap': ('MỘT TRANG GIẤY', 'NĂM DÒNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, kế hoạch cho kịch bản thị trường giảm hai mươi phần trăm gồm năm dòng. Dòng một, beta và mức giảm ước tính của danh mục. Dòng hai, số tiền '
         'có thể mất ở ba kịch bản. Dòng ba, tỷ trọng tiền mặt và khoản vay. Dòng bốn, hành động cho từng mốc giảm. Dòng năm, danh sách chờ. Bộ tài liệu quản '
         'trị rủi ro, gồm bảng kế hoạch và bảng tỷ trọng, có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'one page plan',
  'ch': 'Tóm lại: một trang, năm dòng',
  'moc': True,
  'items': [('Beta danh mục', (34, 197, 94)),
            ('Số tiền ở 3 kịch bản', (34, 197, 94)),
            ('Tiền mặt và khoản vay', (255, 196, 0)),
            ('Hành động từng mốc', (255, 196, 0)),
            ('Danh sách chờ', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('VN-INDEX −20%?', 'ĐÃ CÓ KẾ HOẠCH?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu VN Index theo tuần từ tháng mười một/hai nghìn không trăm hai mươi ba đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu. Nếu '
         'ngày mai VN Index giảm hai mươi phần trăm, anh chị đã viết sẵn mình sẽ làm gì chưa?'}]

S['CH2311C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'GAS – đọc BCTC',
  'cap': ('LÃI QUÝ +79,5%', 'P/E 12,13'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'PV Gas, mã GAS, báo lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn nghìn năm trăm bảy mươi sáu tỷ, tăng bảy mươi '
         'chín phẩy năm phần trăm so với cùng kỳ. Lũy kế chín tháng đạt mười ba nghìn ba trăm tám mươi mốt tỷ, tăng ba mươi ba phẩy một phần trăm. Cổ phiếu '
         'đóng cửa ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu ở khoảng bảy mươi bốn phẩy mười nghìn đồng, thấp hơn đỉnh năm mươi hai tuần '
         'khoảng bốn mươi phẩy tám phần trăm. Con số quý này có đủ để kết luận doanh nghiệp đang khỏe lên hay yếu đi không? Trong video này, em đọc lần lượt '
         'lợi nhuận tám quý, doanh thu và biên lợi nhuận, chi phí lãi vay và dòng tiền, định giá, rủi ro cần theo dõi và cách quản trị vốn khi nắm giữ GAS. Số '
         'liệu lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu.',
  'moc': True,
  'anh': 'gas pipeline',
  'chart': {'sym': 'GASW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 127.79, 'Đỉnh tuần 2/3/26: 127,79', 0.6], [0, 58.4, 'Đáy tuần 3/11/25: 58,40', 1.6], [51, 74.1, 'Tuần 2/11/26: 74,10', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý hai năm hai nghìn không trăm hai mươi sáu với khoảng năm nghìn tám trăm sáu mươi tỷ, thấp nhất ở quý bốn '
         'năm hai nghìn không trăm hai mươi lăm với khoảng một nghìn ba trăm sáu mươi mốt tỷ, và có bốn quý tăng so với quý liền trước. Bốn quý gần nhất lần '
         'lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt một nghìn ba trăm sáu mươi mốt tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt hai '
         'nghìn chín trăm bốn mươi lăm tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt năm nghìn tám trăm sáu mươi tỷ, quý ba năm hai nghìn không trăm '
         'hai mươi sáu đạt bốn nghìn năm trăm bảy mươi sáu tỷ. Khi đọc chuỗi này, anh chị đừng chỉ so với cùng kỳ năm trước. Hãy so thêm với quý liền trước và '
         'với lũy kế chín tháng, vì một quý có thể đẹp lên nhờ khoản thu bất thường, nhờ trích lập dự phòng ít đi, hoặc nhờ nền so sánh thấp. Chuỗi tám quý '
         'cho thấy lợi nhuận đang đi lên đều, đi ngang hay dao động mạnh, và đó mới là thứ giúp ước lượng quý tiếp theo.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('Q4/24', 2044.1, (56, 189, 248), '2.044'),
           ('Q1/25', 2756.5, (56, 189, 248), '2.756'),
           ('Q2/25', 4747.6, (56, 189, 248), '4.748'),
           ('Q3/25', 2549.1, (56, 189, 248), '2.549'),
           ('Q4/25', 1361.1, (56, 189, 248), '1.361'),
           ('Q1/26', 2944.6, (56, 189, 248), '2.945'),
           ('Q2/26', 5860.1, (56, 189, 248), '5.860'),
           ('Q3/26', 4576.5, (34, 197, 94), '4.576')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Doanh thu tám quý',
  'label': '',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, doanh thu và biên lợi nhuận. Doanh thu thuần đạt ba mươi chín nghìn bảy trăm linh tám tỷ, tăng mười một phẩy ba phần trăm. Trong tám quý '
         'từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, doanh thu thuần cao nhất ở quý bốn năm hai nghìn '
         'không trăm hai mươi lăm với khoảng bốn mươi ba nghìn sáu trăm tám mươi ba tỷ, thấp nhất ở quý bốn năm hai nghìn không trăm hai mươi bốn với khoảng '
         'hai mươi bốn nghìn chín trăm bốn mươi lăm tỷ, và có năm quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai nghìn không '
         'trăm hai mươi lăm đạt bốn mươi ba nghìn sáu trăm tám mươi ba tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt ba mươi tám nghìn không trăm hai '
         'mươi tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt bốn mươi ba nghìn hai trăm bốn mươi chín tỷ, quý ba năm hai nghìn không trăm hai mươi sáu '
         'đạt ba mươi chín nghìn bảy trăm linh tám tỷ. Biên lợi nhuận gộp mười lăm phẩy bảy phần trăm, cùng kỳ mười một phẩy năm phần trăm, cải thiện. Doanh '
         'thu cho biết doanh nghiệp bán được bao nhiêu, còn biên lợi nhuận gộp cho biết mỗi một trăm đồng doanh thu còn lại bao nhiêu đồng sau giá vốn. Doanh '
         'thu tăng mà biên co lại thường là dấu hiệu giá bán chịu áp lực hoặc chi phí đầu vào tăng nhanh hơn. Biên mở rộng mà doanh thu đi ngang thì lợi nhuận '
         'vẫn có thể tăng, nhưng mức tăng đó phụ thuộc vào giá đầu vào, thứ doanh nghiệp không kiểm soát hoàn toàn.',
  'anh': 'gas pipeline',
  'bars': [('Q4/24', 24945.1, (56, 189, 248), '24.945'),
           ('Q1/25', 25675.4, (56, 189, 248), '25.675'),
           ('Q2/25', 30080.4, (56, 189, 248), '30.080'),
           ('Q3/25', 35690.1, (56, 189, 248), '35.690'),
           ('Q4/25', 43683.1, (56, 189, 248), '43.683'),
           ('Q1/26', 38019.6, (56, 189, 248), '38.020'),
           ('Q2/26', 43249.1, (56, 189, 248), '43.249'),
           ('Q3/26', 39708.4, (34, 197, 94), '39.708')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Lãi vay và dòng tiền',
  'label': '',
  'cap': ('LÃI VAY', 'VÀ DÒNG TIỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, chi phí lãi vay và dòng tiền. Bốn quý gần nhất, chi phí lãi vay cộng lại khoảng hai trăm ba mươi mốt tỷ. Cũng trong bốn quý đó, lợi nhuận '
         'sau thuế cộng lại khoảng mười bốn nghìn bảy trăm bốn mươi hai tỷ, còn dòng tiền thuần từ hoạt động kinh doanh cộng lại khoảng mười hai nghìn năm '
         'trăm sáu mươi hai tỷ. Dòng tiền kinh doanh thấp hơn lợi nhuận nghĩa là một phần lợi nhuận còn nằm ở khoản phải thu, hàng tồn kho hoặc khoản trả '
         'trước, chưa về thành tiền. Một vài quý như vậy là bình thường, nhưng kéo dài nhiều quý thì anh chị cần soi kỹ thuyết minh. Doanh nghiệp vay càng '
         'nhiều thì khi lãi suất tăng, phần lợi nhuận dành cho cổ đông càng bị chia sẻ cho chủ nợ.',
  'moc': True,
  'anh': 'cash flow',
  'cards': [('Lãi vay 4 quý', '≈ 231 tỷ', ''), ('LNST 4 quý', '≈ 14.742 tỷ', ''), ('Dòng tiền KD 4 quý', '≈ 12.562 tỷ', '')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, định giá. Với giá khoảng bảy mươi bốn phẩy mười nghìn đồng, GAS có P trên E khoảng mười hai phẩy mười ba lần, P trên B khoảng hai phẩy '
         'bốn mươi bốn lần, ROE khoảng hai mươi mốt phẩy một phần trăm. Trong mười bảy mã cùng nhóm điện, nước có vốn hóa từ một nghìn năm trăm tỷ, P trên E '
         'trung vị khoảng chín phẩy hai mươi bốn lần, P trên B trung vị khoảng một phẩy bốn mươi bốn lần, ROE trung vị khoảng mười bảy phẩy một phần trăm. P '
         'trên E chỉ có ý nghĩa khi lợi nhuận bốn quý gần nhất phản ánh đúng sức kiếm tiền bình thường. Nếu có quý đột biến hoặc quý lỗ, P trên E sẽ bị méo, '
         'khi đó anh chị nên tính lại với lợi nhuận đã loại phần bất thường. Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán '
         'Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '12,13', 'lần'), ('P/B', '2,44', 'lần'), ('ROE', '21,1%', 'trên vốn chủ')]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá cách đỉnh bao xa. Đỉnh năm mươi hai tuần của GAS khoảng một trăm hai mươi lăm phẩy không bảy nghìn đồng, đáy khoảng năm mươi chín '
         'phẩy không chín nghìn đồng. Giá hiện tại thấp hơn đỉnh khoảng bốn mươi phẩy tám phần trăm. Người mua ở đỉnh cần cổ phiếu tăng khoảng sáu mươi chín '
         'phần trăm mới hòa vốn. Đây là toán học của thua lỗ: giảm càng sâu thì phần tăng cần thiết để hồi lại càng lớn hơn phần đã mất. Hệ số beta của GAS '
         'khoảng không phẩy bảy mươi bảy, nghĩa là trong giai đoạn đo, giá dao động ít hơn thị trường chung. Beta không nói cổ phiếu tốt hay xấu, nó chỉ nói '
         'mức rung lắc mà anh chị phải chịu được.',
  'moc': True,
  'value': -40.8,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 125,07 – NAY 74,10',
  'sub': 'cần +69% để về đỉnh',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Báo cáo quý này không có dòng nào xấu rõ rệt, nhưng đó không phải lý do để bỏ qua phần rủi ro. Với doanh nghiệp sản '
         'xuất và dịch vụ, ba rủi ro cần theo dõi là giá đầu vào, nợ vay và sức mua của khách hàng. Một quý tăng trưởng không xóa được rủi ro chu kỳ, nên anh '
         'chị hãy hỏi: nếu giá đầu vào quay lại mức cũ, biên lợi nhuận còn bao nhiêu?',
  'anh': 'warning sign',
  'items': [('Tỷ trọng cả nhóm ngành', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Quản trị vốn',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, quản trị vốn khi nắm giữ GAS. Em đề xuất ba câu hỏi phải trả lời trước khi mua. Một, mã này chiếm tối đa bao nhiêu phần trăm danh mục? '
         'Với một mã đơn lẻ, nhiều nhà đầu tư cá nhân giới hạn trong khoảng mười đến hai mươi phần trăm. Hai, nếu giá quay về đáy năm mươi hai tuần khoảng năm '
         'mươi chín phẩy không chín nghìn đồng, tức thấp hơn giá hiện tại khoảng hai mươi phẩy ba phần trăm, thì danh mục mất bao nhiêu? Với tỷ trọng mười '
         'phần trăm, mức giảm đó làm danh mục mất khoảng hai phần trăm. Ba, điều gì xảy ra thì luận điểm sai? Ví dụ lợi nhuận hai quý liên tiếp giảm, hoặc '
         'biên lợi nhuận xấu đi. Viết sẵn ba câu trả lời này ra giấy, anh chị sẽ bớt bị cảm xúc kéo đi khi giá biến động. Không dùng vay ký quỹ cho mã mình '
         'chưa trả lời được câu hỏi thứ ba.',
  'moc': True,
  'anh': 'balance scale',
  'cards': [('Tỷ trọng tối đa', '10–20%', 'một mã'), ('Nếu về đáy 52 tuần', '−20,3%', 'giá cổ phiếu'), ('Điểm sai', 'viết trước', 'khi mua')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước tự đọc',
  'label': '',
  'cap': ('NĂM BƯỚC', 'TỰ ĐỌC BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, năm bước anh chị có thể tự làm với mọi báo cáo doanh nghiệp. Một, lợi nhuận tám quý, lũy kế. Hai, doanh thu và biên gộp. Ba, lãi vay và '
         'dòng tiền. Bốn, P trên E cạnh tăng trưởng. Năm, tỷ trọng và điểm sai. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy '
         'Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận 8 quý, lũy kế', (34, 197, 94)),
            ('Doanh thu và biên gộp', (34, 197, 94)),
            ('Lãi vay và dòng tiền', (34, 197, 94)),
            ('P/E cạnh tăng trưởng', (34, 197, 94)),
            ('Tỷ trọng và điểm sai', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI QUÝ +79,5%', 'ĐỦ KẾT LUẬN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với GAS, anh chị đặt trọng số nhiều hơn vào kết quả quý gần nhất, hay vào chuỗi tám quý và rủi ro phía trước?'}]

S['CH2411A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'KLB – đọc BCTC',
  'cap': ('LÃI QUÝ −12,8%', 'P/B 0,79'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Kienlongbank, mã KLB, báo lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn trăm hai mươi chín tỷ, giảm mười hai '
         'phẩy tám phần trăm so với cùng kỳ. Lũy kế chín tháng đạt một nghìn ba trăm sáu mươi tám tỷ, tăng mười một phẩy bốn phần trăm. Cổ phiếu đóng cửa ngày '
         'sáu tháng mười một năm hai nghìn không trăm hai mươi sáu ở khoảng mười phẩy ba mươi nghìn đồng, thấp hơn đỉnh năm mươi hai tuần khoảng hai mươi sáu '
         'phẩy năm phần trăm. Con số quý này có đủ để kết luận doanh nghiệp đang khỏe lên hay yếu đi không? Trong video này, em đọc lần lượt lợi nhuận tám '
         'quý, thu nhập lãi thuần, dự phòng và nợ xấu, định giá, rủi ro cần theo dõi và cách quản trị vốn khi nắm giữ KLB. Số liệu lấy từ báo cáo tài chính '
         'quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'bank building',
  'chart': {'sym': 'KLBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[11, 14.44, 'Đỉnh tuần 19/1/26: 14,44', 0.6], [19, 9.61, 'Đáy tuần 23/3/26: 9,61', 1.6], [51, 10.3, 'Tuần 2/11/26: 10,30', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng sáu trăm hai mươi tám tỷ, thấp nhất ở quý bốn năm hai '
         'nghìn không trăm hai mươi bốn với khoảng hai trăm tám mươi mốt tỷ, và có năm quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn '
         'năm hai nghìn không trăm hai mươi lăm đạt sáu trăm hai mươi tám tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt bốn trăm mười bảy tỷ, quý hai '
         'năm hai nghìn không trăm hai mươi sáu đạt năm trăm hai mươi ba tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn trăm hai mươi chín tỷ. Khi '
         'đọc chuỗi này, anh chị đừng chỉ so với cùng kỳ năm trước. Hãy so thêm với quý liền trước và với lũy kế chín tháng, vì một quý có thể đẹp lên nhờ '
         'khoản thu bất thường, nhờ trích lập dự phòng ít đi, hoặc nhờ nền so sánh thấp. Chuỗi tám quý cho thấy lợi nhuận đang đi lên đều, đi ngang hay dao '
         'động mạnh, và đó mới là thứ giúp ước lượng quý tiếp theo.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('Q4/24', 280.7, (56, 189, 248), '281'),
           ('Q1/25', 284.7, (56, 189, 248), '285'),
           ('Q2/25', 451.5, (56, 189, 248), '452'),
           ('Q3/25', 491.9, (56, 189, 248), '492'),
           ('Q4/25', 628.2, (56, 189, 248), '628'),
           ('Q1/26', 416.8, (56, 189, 248), '417'),
           ('Q2/26', 522.7, (56, 189, 248), '523'),
           ('Q3/26', 429.0, (34, 197, 94), '429')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'label': '',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, thu nhập lãi thuần, tức phần chênh lệch giữa lãi cho vay thu vào và lãi huy động trả ra. Đây là mảng cốt lõi của ngân hàng. Thu nhập lãi '
         'thuần đạt tám trăm bảy mươi bốn tỷ, giảm mười phẩy bảy phần trăm. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai '
         'nghìn không trăm hai mươi sáu, thu nhập lãi thuần cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng một nghìn không trăm năm mươi '
         'bảy tỷ, thấp nhất ở quý bốn năm hai nghìn không trăm hai mươi bốn với khoảng bảy trăm chín mươi bốn tỷ, và có năm quý tăng so với quý liền trước. '
         'Bốn quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt một nghìn không trăm năm mươi bảy tỷ, quý một năm hai nghìn không '
         'trăm hai mươi sáu đạt chín trăm hai mươi tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt một nghìn không trăm linh bảy tỷ, quý ba năm hai '
         'nghìn không trăm hai mươi sáu đạt tám trăm bảy mươi bốn tỷ. Khi lợi nhuận tăng mà thu nhập lãi thuần giảm, phần tăng thêm đến từ nơi khác: dịch vụ, '
         'kinh doanh chứng khoán, thu hồi nợ đã xử lý, hoặc chi phí dự phòng thấp hơn. Những nguồn này thường kém đều hơn mảng cho vay, nên anh chị cần hỏi: '
         'quý sau nguồn đó có lặp lại không?',
  'anh': 'bank loan',
  'bars': [('Q4/24', 793.7, (56, 189, 248), '794'),
           ('Q1/25', 849.1, (56, 189, 248), '849'),
           ('Q2/25', 883.9, (56, 189, 248), '884'),
           ('Q3/25', 977.9, (56, 189, 248), '978'),
           ('Q4/25', 1056.7, (56, 189, 248), '1.057'),
           ('Q1/26', 919.7, (56, 189, 248), '920'),
           ('Q2/26', 1006.9, (56, 189, 248), '1.007'),
           ('Q3/26', 873.6, (34, 197, 94), '874')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Dự phòng và nợ xấu',
  'label': '',
  'cap': ('DỰ PHÒNG', 'VÀ NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, dự phòng và nợ xấu. Bao phủ nợ xấu khoảng tám mươi mốt phần trăm. Tỷ lệ nợ xấu một phẩy chín mươi tám phần trăm, tăng so với quý trước, '
         'một phẩy tám mươi ba phần trăm. Tỷ lệ bao phủ nợ xấu là số dự phòng đã trích chia cho tổng nợ xấu. Bao phủ một trăm phần trăm nghĩa là nếu toàn bộ '
         'nợ xấu mất trắng, ngân hàng đã có sẵn tiền dự phòng để bù. Bao phủ càng thấp thì bộ đệm càng mỏng, và lợi nhuận tương lai càng dễ bị bào mòn khi '
         'phải trích lập thêm. Hai con số này anh chị tra được trong thuyết minh báo cáo tài chính, mục chất lượng nợ cho vay.',
  'moc': True,
  'anh': 'risk management',
  'cards': [('Bao phủ nợ xấu khoảng 81%', '', ''), ('Tỷ lệ nợ xấu 1,98%', '', '')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, định giá. Với giá khoảng mười phẩy ba mươi nghìn đồng, KLB có P trên E khoảng ba phẩy tám mươi sáu lần, P trên B khoảng không phẩy bảy '
         'mươi chín lần, ROE khoảng hai mươi hai phẩy bảy phần trăm. Trong hai mươi mã cùng nhóm ngân hàng có vốn hóa từ một nghìn năm trăm tỷ, P trên E trung '
         'vị khoảng bảy phẩy hai mươi lần, P trên B trung vị khoảng một phẩy mười chín lần, ROE trung vị khoảng mười bảy phẩy ba phần trăm. Với ngân hàng, P '
         'trên B nên đọc cùng ROE. Một ngân hàng có ROE cao xứng đáng được trả P trên B cao hơn, còn P trên B thấp kèm ROE thấp thì chưa chắc là rẻ. Bảng định '
         'giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '3,86', 'lần'), ('P/B', '0,79', 'lần'), ('ROE', '22,7%', 'trên vốn chủ')]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá cách đỉnh bao xa. Đỉnh năm mươi hai tuần của KLB khoảng mười bốn phẩy không hai nghìn đồng, đáy khoảng chín phẩy sáu mươi lăm nghìn '
         'đồng. Giá hiện tại thấp hơn đỉnh khoảng hai mươi sáu phẩy năm phần trăm. Người mua ở đỉnh cần cổ phiếu tăng khoảng ba mươi sáu phần trăm mới hòa '
         'vốn. Đây là toán học của thua lỗ: giảm càng sâu thì phần tăng cần thiết để hồi lại càng lớn hơn phần đã mất. Hệ số beta của KLB khoảng không phẩy '
         'năm mươi tám, nghĩa là trong giai đoạn đo, giá dao động ít hơn thị trường chung. Beta không nói cổ phiếu tốt hay xấu, nó chỉ nói mức rung lắc mà anh '
         'chị phải chịu được.',
  'moc': True,
  'value': -26.5,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 14,02 – NAY 10,30',
  'sub': 'cần +36% để về đỉnh',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Thu nhập lãi thuần, mảng cho vay cốt lõi giảm mười phẩy bảy phần trăm. Tỷ lệ nợ xấu một phẩy chín mươi tám phần '
         'trăm, tăng so với quý trước, một phẩy tám mươi ba phần trăm. Với cổ phiếu ngân hàng, rủi ro lớn nhất thường không nằm ở một quý lợi nhuận, mà ở chất '
         'lượng tài sản: nợ xấu, nợ tái cơ cấu và mức độ tập trung cho vay vào bất động sản. Ngoài ra, cổ phiếu ngân hàng hay biến động cùng nhau, nên anh chị '
         'cần cộng tỷ trọng cả nhóm ngân hàng trong danh mục.',
  'anh': 'warning sign',
  'items': [('Thu nhập lãi thuần (mảng cho vay cốt lõi', (239, 68, 68)), ('Tỷ lệ nợ xấu 1,98%', (239, 68, 68)), ('Tỷ trọng cả nhóm ngành', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Quản trị vốn',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, quản trị vốn khi nắm giữ KLB. Em đề xuất ba câu hỏi phải trả lời trước khi mua. Một, mã này chiếm tối đa bao nhiêu phần trăm danh mục? '
         'Với một mã đơn lẻ, nhiều nhà đầu tư cá nhân giới hạn trong khoảng mười đến hai mươi phần trăm. Hai, nếu giá quay về đáy năm mươi hai tuần khoảng '
         'chín phẩy sáu mươi lăm nghìn đồng, tức thấp hơn giá hiện tại khoảng sáu phẩy ba phần trăm, thì danh mục mất bao nhiêu? Với tỷ trọng mười phần trăm, '
         'mức giảm đó làm danh mục mất khoảng không phẩy sáu phần trăm. Ba, điều gì xảy ra thì luận điểm sai? Ví dụ lợi nhuận hai quý liên tiếp giảm, hoặc nợ '
         'xấu xấu đi. Viết sẵn ba câu trả lời này ra giấy, anh chị sẽ bớt bị cảm xúc kéo đi khi giá biến động. Không dùng vay ký quỹ cho mã mình chưa trả lời '
         'được câu hỏi thứ ba.',
  'moc': True,
  'anh': 'balance scale',
  'cards': [('Tỷ trọng tối đa', '10–20%', 'một mã'), ('Nếu về đáy 52 tuần', '−6,3%', 'giá cổ phiếu'), ('Điểm sai', 'viết trước', 'khi mua')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước tự đọc',
  'label': '',
  'cap': ('NĂM BƯỚC', 'TỰ ĐỌC BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, năm bước anh chị có thể tự làm với mọi báo cáo ngân hàng. Một, lợi nhuận tám quý, lũy kế. Hai, thu nhập lãi thuần. Ba, dự phòng, nợ xấu, '
         'bao phủ. Bốn, P trên B cạnh ROE. Năm, tỷ trọng và điểm sai. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm '
         'com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận 8 quý, lũy kế', (34, 197, 94)),
            ('Thu nhập lãi thuần', (34, 197, 94)),
            ('Dự phòng, nợ xấu, bao phủ', (34, 197, 94)),
            ('P/B cạnh ROE', (34, 197, 94)),
            ('Tỷ trọng và điểm sai', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI QUÝ −12,8%', 'ĐỦ KẾT LUẬN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với KLB, anh chị đặt trọng số nhiều hơn vào kết quả quý gần nhất, hay vào chuỗi tám quý và rủi ro phía trước?'}]

S['CH2411B'] = [{'k': 'text',
  'label': '',
  'cap': ('CẮT LỖ Ở ĐÂU?', '3 KIỂU ĐIỂM SAI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Lỗ mười phần trăm cần lãi khoảng mười một phần trăm để hòa vốn. Lỗ ba mươi phần trăm cần lãi khoảng bốn mươi ba phần trăm. Lỗ năm mươi phần trăm cần '
         'lãi một trăm phần trăm. Đó là lý do mọi người đều nói phải cắt lỗ. Nhưng cắt ở đâu mới là câu hỏi khó. Cắt quá sớm thì bị rung lắc bình thường đánh '
         'bật ra khỏi một cổ phiếu tốt. Cắt quá muộn thì một sai lầm nhỏ thành vết thương lớn. Trong video này, em trình bày ba kiểu điểm sai: theo giá, theo '
         'thời gian và theo luận điểm, cùng cách kết hợp chúng với tỷ trọng để mỗi lệnh sai chỉ là một vết xước.',
  'anh': 'stop sign road',
  'ch': 'Mở đầu',
  'moc': True},
 {'k': 'bars',
  'label': '',
  'cap': ('TOÁN HỌC', 'CỦA THUA LỖ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Trước hết là toán học. Phần lãi cần để hòa vốn bằng phần lỗ chia cho phần còn lại. Lỗ hai mươi phần trăm thì còn tám mươi phần trăm, cần lãi hai '
         'mươi chia tám mươi, tức hai mươi lăm phần trăm. Lỗ bốn mươi phần trăm thì còn sáu mươi phần trăm, cần lãi khoảng sáu mươi bảy phần trăm. Đường cong '
         'này dốc dần lên: càng lỗ sâu, quãng đường quay về càng xa, và thời gian chờ càng dài. Vì vậy mục tiêu của cắt lỗ không phải là đúng mọi lúc, mà là '
         'giữ cho mỗi lần sai nằm ở vùng đầu của đường cong, nơi việc gỡ lại còn khả thi. Một cổ phiếu tốt tăng mười lăm đến hai mươi phần trăm trong một năm '
         'đã là kết quả đẹp, nên một khoản lỗ năm mươi phần trăm có thể cần nhiều năm mới gỡ lại, kể cả khi anh chị chọn đúng mã ở lần sau.',
  'anh': 'steep curve graph',
  'ch': 'Toán học của thua lỗ',
  'bars': [('−10%', 11.1, (255, 196, 0), '+11%'),
           ('−20%', 25.0, (255, 196, 0), '+25%'),
           ('−30%', 42.9, (239, 68, 68), '+43%'),
           ('−40%', 66.7, (239, 68, 68), '+67%'),
           ('−50%', 100.0, (239, 68, 68), '+100%')]},
 {'k': 'text',
  'label': '',
  'cap': ('KIỂU 1', 'ĐIỂM SAI THEO GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Kiểu thứ nhất, điểm sai theo giá. Anh chị chọn trước một mức giá mà nếu cổ phiếu đóng cửa dưới mức đó, lý do mua ban đầu không còn đúng. Mức này nên '
         'đặt dựa trên cấu trúc giá, ví dụ dưới đáy gần nhất hoặc dưới vùng tích lũy, chứ không phải một con số tròn như bảy phần trăm cho mọi mã. Mã dao động '
         'mạnh cần khoảng cách rộng hơn, mã dao động ít có thể đặt gần hơn. Ưu điểm của kiểu này là rõ ràng, dễ làm theo. Nhược điểm là dễ bị kích hoạt bởi '
         'một phiên rung lắc rồi giá quay lại.',
  'anh': 'price chart support',
  'ch': 'Kiểu 1 – Điểm sai theo giá',
  'moc': True},
 {'k': 'text',
  'label': '',
  'cap': ('KIỂU 2', 'THEO THỜI GIAN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Kiểu thứ hai, điểm sai theo thời gian. Khi mua, anh chị dự kiến điều mình chờ sẽ xảy ra trong bao lâu, ví dụ kết quả kinh doanh hai quý tới. Nếu hết '
         'khoảng thời gian đó mà điều mình chờ không xảy ra, lệnh được xem là sai, kể cả khi giá chưa giảm nhiều. Kiểu này giải quyết một rủi ro hay bị bỏ '
         'quên: chi phí cơ hội. Một khoản tiền nằm im mười tám tháng trong một mã đi ngang là mười tám tháng không làm việc cho anh chị.',
  'anh': 'hourglass time',
  'ch': 'Kiểu 2 – Điểm sai theo thời gian'},
 {'k': 'text',
  'label': '',
  'cap': ('KIỂU 3', 'THEO LUẬN ĐIỂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Kiểu thứ ba, điểm sai theo luận điểm. Mỗi lệnh mua nên có một câu lý do, ví dụ: lợi nhuận ngân hàng tăng nhờ thu nhập lãi thuần tăng và nợ xấu giảm. '
         'Điểm sai theo luận điểm là điều kiện khiến câu đó không còn đúng: thu nhập lãi thuần giảm hai quý liên tiếp, hoặc nợ xấu tăng vượt một ngưỡng. Đây '
         'là kiểu điểm sai của người đầu tư theo doanh nghiệp, và nó buộc anh chị đọc báo cáo tài chính mỗi quý. Báo cáo tài chính đầy đủ từng mã có trên '
         'trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'financial report reading',
  'ch': 'Kiểu 3 – Điểm sai theo luận điểm',
  'moc': True},
 {'k': 'checklist',
  'label': '',
  'cap': ('KẾT HỢP', 'BA KIỂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Trong thực tế, ba kiểu nên đi cùng nhau. Điểm sai theo giá là lưới an toàn cuối cùng, chặn những cú giảm mà anh chị chưa kịp hiểu lý do. Điểm sai '
         'theo luận điểm là lý do chính để bán khi doanh nghiệp xấu đi. Điểm sai theo thời gian giúp dọn những vị thế không còn tạo ra giá trị. Viết cả ba vào '
         'cùng một dòng trong nhật ký giao dịch, ngay lúc đặt lệnh mua.',
  'anh': 'three layers shield',
  'ch': 'Kết hợp ba kiểu',
  'items': [('Giá: lưới an toàn cuối', (239, 68, 68)), ('Luận điểm: lý do chính để bán', (255, 196, 0)), ('Thời gian: dọn vị thế đứng yên', (255, 196, 0))]},
 {'k': 'cards',
  'label': '',
  'cap': ('TỶ TRỌNG', 'QUYẾT ĐỊNH VẾT THƯƠNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Điểm sai chỉ là một nửa. Nửa còn lại là tỷ trọng. Ví dụ, anh chị chấp nhận mỗi lệnh sai chỉ làm danh mục mất tối đa một phần trăm. Nếu điểm sai theo '
         'giá cách giá mua mười phần trăm, tỷ trọng tối đa cho mã đó là mười phần trăm danh mục. Nếu điểm sai cách hai mươi phần trăm, tỷ trọng tối đa còn năm '
         'phần trăm. Cách tính này đảo ngược thói quen phổ biến: chọn tỷ trọng theo mức độ thích một cổ phiếu. Ở đây, tỷ trọng được quyết định bởi khoảng cách '
         'tới điểm sai.',
  'anh': 'balance scale weights',
  'ch': 'Tỷ trọng quyết định vết thương',
  'moc': True,
  'cards': [('Rủi ro mỗi lệnh', '1%', 'danh mục'), ('Điểm sai −10%', 'tối đa 10%', 'tỷ trọng'), ('Điểm sai −20%', 'tối đa 5%', 'tỷ trọng')]},
 {'k': 'bignum',
  'label': '',
  'cap': ('MƯỜI LỆNH SAI', 'VẪN CÒN VỐN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Với quy tắc mỗi lệnh sai mất một phần trăm danh mục, mười lệnh sai liên tiếp làm danh mục giảm khoảng chín phẩy sáu phần trăm, vì mỗi lần mất một '
         'phần trăm của phần còn lại. Đó là một giai đoạn khó chịu, nhưng vẫn gỡ lại được. Ngược lại, nếu mỗi lệnh sai mất mười phần trăm danh mục, ba lệnh '
         'sai liên tiếp đã làm mất khoảng hai mươi bảy phần trăm, cần lãi khoảng ba mươi bảy phần trăm mới hòa. Người đầu tư lâu năm không phải người chưa bao '
         'giờ sai, mà là người mà mỗi lần sai đều nhỏ.',
  'anh': 'survival compass',
  'ch': 'Mười lệnh sai vẫn còn vốn',
  'value': -9.6,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': '10 LỆNH SAI, MỖI LỆNH −1%',
  'sub': 'danh mục vẫn còn hơn 90%',
  'col': (255, 196, 0)},
 {'k': 'cards',
  'label': '',
  'cap': ('VÍ DỤ', 'BẰNG SỐ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Một ví dụ cụ thể bằng số. Danh mục năm trăm triệu đồng, quy tắc mỗi lệnh sai mất tối đa một phần trăm, tức năm triệu đồng. Anh chị muốn mua một cổ '
         'phiếu giá năm mươi nghìn đồng, và điểm sai theo giá nằm ở bốn mươi lăm nghìn đồng, dưới đáy gần nhất. Khoảng cách tới điểm sai là năm nghìn đồng mỗi '
         'cổ phiếu, tức mười phần trăm. Số cổ phiếu tối đa bằng năm triệu chia cho năm nghìn, tức một nghìn cổ phiếu, tương đương năm mươi triệu đồng, đúng '
         'mười phần trăm danh mục. Nếu cổ phiếu chạm điểm sai, anh chị mất khoảng năm triệu đồng cộng phí giao dịch, và vẫn còn chín mươi chín phần trăm danh '
         'mục để làm lệnh tiếp theo. Nếu cổ phiếu đúng như kỳ vọng, phần lãi không bị giới hạn bởi quy tắc này.',
  'anh': 'calculator notebook',
  'ch': 'Ví dụ bằng số',
  'moc': True,
  'cards': [('Danh mục', '500 triệu', ''), ('Rủi ro 1 lệnh', '5 triệu', '1%'), ('Mua 50 – sai 45', '1.000 cổ phiếu', '≈ 10% danh mục')]},
 {'k': 'text',
  'label': '',
  'cap': ('VÌ SAO KHÓ', 'LÀM THEO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Vì sao biết mà vẫn khó làm? Vì cắt lỗ là thừa nhận mình sai, và não bộ con người rất ghét điều đó. Hiệu ứng tâm lý này có tên là ngại thua lỗ: người '
         'ta có xu hướng giữ mã đang lỗ quá lâu với hy vọng hòa vốn, và bán mã đang lãi quá sớm. Cách đối phó hiệu quả nhất là biến quyết định thành quy tắc '
         'trước khi tiền nằm trong cổ phiếu, và đặt lệnh dừng lỗ sẵn nếu có thể, để cảm xúc lúc giá giảm không phải là người quyết định.',
  'anh': 'brain decision',
  'ch': 'Vì sao khó làm theo'},
 {'k': 'checklist',
  'label': '',
  'cap': ('SAU KHI CẮT', 'LÀM GÌ TIẾP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Sau khi cắt lỗ, có ba việc nên làm. Một, ghi vào nhật ký: kiểu điểm sai nào đã kích hoạt, và luận điểm ban đầu sai ở đâu. Hai, không mua lại ngay '
         'trong cùng phiên chỉ vì giá hồi một chút; nếu muốn quay lại, hãy viết một luận điểm mới. Ba, sau mỗi hai mươi lệnh, xem lại tỷ lệ lệnh đúng và mức '
         'lãi lỗ trung bình. Con số đó cho biết vấn đề nằm ở chọn mã hay ở quản trị vị thế. Bộ tài liệu quản trị rủi ro, gồm bảng kế hoạch và bảng tỷ trọng, '
         'có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'journal notebook pen',
  'ch': 'Sau khi cắt lỗ làm gì',
  'moc': True,
  'items': [('Ghi nhật ký kiểu điểm sai', (34, 197, 94)), ('Không mua lại theo cảm xúc', (255, 196, 0)), ('Thống kê sau mỗi 20 lệnh', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('CẮT LỖ Ở ĐÂU?', 'VIẾT TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Lệnh mua gần nhất của anh chị có điểm sai được viết trước không, và đó là kiểu theo giá, theo thời gian hay theo luận điểm?'}]

S['CH2411C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'VJC – đọc BCTC',
  'cap': ('LÃI QUÝ +8,6%', 'P/E 47,00'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Vietjet, mã VJC, báo lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt ba trăm bốn mươi bảy tỷ, tăng tám phẩy sáu phần '
         'trăm so với cùng kỳ. Lũy kế chín tháng đạt một nghìn sáu trăm chín mươi bốn tỷ, tăng năm phẩy một phần trăm. Cổ phiếu đóng cửa ngày sáu tháng mười '
         'một năm hai nghìn không trăm hai mươi sáu ở khoảng một trăm ba mươi bốn phẩy bảy nghìn đồng, thấp hơn đỉnh năm mươi hai tuần khoảng hai mươi phẩy '
         'một phần trăm. Con số quý này có đủ để kết luận doanh nghiệp đang khỏe lên hay yếu đi không? Trong video này, em đọc lần lượt lợi nhuận tám quý, '
         'doanh thu và biên lợi nhuận, chi phí lãi vay và dòng tiền, định giá, rủi ro cần theo dõi và cách quản trị vốn khi nắm giữ VJC. Số liệu lấy từ báo '
         'cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'airplane runway',
  'chart': {'sym': 'VJCW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[3, 169.22, 'Đỉnh tuần 24/11/25: 169,22', 0.6],
                        [17, 111.92, 'Đáy tuần 9/3/26: 111,92', 1.6],
                        [51, 134.7, 'Tuần 2/11/26: 134,70', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý một năm hai nghìn không trăm hai mươi sáu với khoảng một nghìn không trăm mười bốn tỷ, thấp nhất ở quý bốn '
         'năm hai nghìn không trăm hai mươi bốn với khoảng một tỷ, và có năm quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai '
         'nghìn không trăm hai mươi lăm đạt năm trăm mười tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt một nghìn không trăm mười bốn tỷ, quý hai năm '
         'hai nghìn không trăm hai mươi sáu đạt ba trăm ba mươi bốn tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt ba trăm bốn mươi bảy tỷ. Khi đọc '
         'chuỗi này, anh chị đừng chỉ so với cùng kỳ năm trước. Hãy so thêm với quý liền trước và với lũy kế chín tháng, vì một quý có thể đẹp lên nhờ khoản '
         'thu bất thường, nhờ trích lập dự phòng ít đi, hoặc nhờ nền so sánh thấp. Chuỗi tám quý cho thấy lợi nhuận đang đi lên đều, đi ngang hay dao động '
         'mạnh, và đó mới là thứ giúp ước lượng quý tiếp theo.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('Q4/24', 0.8, (56, 189, 248), '1'),
           ('Q1/25', 640.5, (56, 189, 248), '640'),
           ('Q2/25', 652.4, (56, 189, 248), '652'),
           ('Q3/25', 319.3, (56, 189, 248), '319'),
           ('Q4/25', 510.4, (56, 189, 248), '510'),
           ('Q1/26', 1013.5, (56, 189, 248), '1.014'),
           ('Q2/26', 333.7, (56, 189, 248), '334'),
           ('Q3/26', 346.6, (34, 197, 94), '347')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Doanh thu tám quý',
  'label': '',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, doanh thu và biên lợi nhuận. Doanh thu thuần đạt hai mươi hai nghìn tám trăm bốn mươi chín tỷ, tăng ba mươi lăm phần trăm. Trong tám quý '
         'từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, doanh thu thuần cao nhất ở quý hai năm hai nghìn '
         'không trăm hai mươi sáu với khoảng ba mươi nghìn năm trăm mười bốn tỷ, thấp nhất ở quý ba năm hai nghìn không trăm hai mươi lăm với khoảng mười sáu '
         'nghìn chín trăm ba mươi mốt tỷ, và có hai quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm '
         'đạt hai mươi chín nghìn ba trăm hai mươi bốn tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt hai mươi mốt nghìn không trăm hai mươi mốt tỷ, '
         'quý hai năm hai nghìn không trăm hai mươi sáu đạt ba mươi nghìn năm trăm mười bốn tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt hai mươi hai '
         'nghìn tám trăm bốn mươi chín tỷ. Biên lợi nhuận gộp tám phẩy chín phần trăm, cùng kỳ mười hai phẩy bốn phần trăm, thu hẹp. Doanh thu cho biết doanh '
         'nghiệp bán được bao nhiêu, còn biên lợi nhuận gộp cho biết mỗi một trăm đồng doanh thu còn lại bao nhiêu đồng sau giá vốn. Doanh thu tăng mà biên co '
         'lại thường là dấu hiệu giá bán chịu áp lực hoặc chi phí đầu vào tăng nhanh hơn. Biên mở rộng mà doanh thu đi ngang thì lợi nhuận vẫn có thể tăng, '
         'nhưng mức tăng đó phụ thuộc vào giá đầu vào, thứ doanh nghiệp không kiểm soát hoàn toàn.',
  'anh': 'airplane runway',
  'bars': [('Q4/24', 19851.1, (56, 189, 248), '19.851'),
           ('Q1/25', 17952.2, (56, 189, 248), '17.952'),
           ('Q2/25', 17885.3, (56, 189, 248), '17.885'),
           ('Q3/25', 16931.4, (56, 189, 248), '16.931'),
           ('Q4/25', 29324.1, (56, 189, 248), '29.324'),
           ('Q1/26', 21021.3, (56, 189, 248), '21.021'),
           ('Q2/26', 30514.3, (56, 189, 248), '30.514'),
           ('Q3/26', 22849.4, (34, 197, 94), '22.849')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Lãi vay và dòng tiền',
  'label': '',
  'cap': ('LÃI VAY', 'VÀ DÒNG TIỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, chi phí lãi vay và dòng tiền. Bốn quý gần nhất, chi phí lãi vay cộng lại khoảng ba nghìn bảy trăm chín mươi sáu tỷ. Cũng trong bốn quý '
         'đó, lợi nhuận sau thuế cộng lại khoảng hai nghìn hai trăm linh bốn tỷ, còn dòng tiền thuần từ hoạt động kinh doanh cộng lại khoảng một nghìn sáu '
         'trăm năm mươi tám tỷ. Dòng tiền kinh doanh thấp hơn lợi nhuận nghĩa là một phần lợi nhuận còn nằm ở khoản phải thu, hàng tồn kho hoặc khoản trả '
         'trước, chưa về thành tiền. Một vài quý như vậy là bình thường, nhưng kéo dài nhiều quý thì anh chị cần soi kỹ thuyết minh. Doanh nghiệp vay càng '
         'nhiều thì khi lãi suất tăng, phần lợi nhuận dành cho cổ đông càng bị chia sẻ cho chủ nợ.',
  'moc': True,
  'anh': 'cash flow',
  'cards': [('Lãi vay 4 quý', '≈ 3.796 tỷ', ''), ('LNST 4 quý', '≈ 2.204 tỷ', ''), ('Dòng tiền KD 4 quý', '≈ 1.658 tỷ', '')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, định giá. Với giá khoảng một trăm ba mươi bốn phẩy bảy nghìn đồng, VJC có P trên E khoảng bốn mươi bảy lần, P trên B khoảng ba phẩy chín '
         'mươi lần, ROE khoảng tám phẩy sáu phần trăm. Trong mười sáu mã cùng nhóm vận tải, cảng có vốn hóa từ một nghìn năm trăm tỷ, P trên E trung vị khoảng '
         'chín phẩy bốn mươi lăm lần, P trên B trung vị khoảng hai phẩy hai mươi mốt lần, ROE trung vị khoảng mười tám phẩy một phần trăm. P trên E chỉ có ý '
         'nghĩa khi lợi nhuận bốn quý gần nhất phản ánh đúng sức kiếm tiền bình thường. Nếu có quý đột biến hoặc quý lỗ, P trên E sẽ bị méo, khi đó anh chị '
         'nên tính lại với lợi nhuận đã loại phần bất thường. Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm '
         'com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '47,00', 'lần'), ('P/B', '3,90', 'lần'), ('ROE', '8,6%', 'trên vốn chủ')]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá cách đỉnh bao xa. Đỉnh năm mươi hai tuần của VJC khoảng một trăm sáu mươi tám phẩy năm mươi ba nghìn đồng, đáy khoảng một trăm mười '
         'sáu phẩy bảy mươi bảy nghìn đồng. Giá hiện tại thấp hơn đỉnh khoảng hai mươi phẩy một phần trăm. Người mua ở đỉnh cần cổ phiếu tăng khoảng hai mươi '
         'lăm phần trăm mới hòa vốn. Đây là toán học của thua lỗ: giảm càng sâu thì phần tăng cần thiết để hồi lại càng lớn hơn phần đã mất. Hệ số beta của '
         'VJC khoảng không phẩy sáu mươi mốt, nghĩa là trong giai đoạn đo, giá dao động ít hơn thị trường chung. Beta không nói cổ phiếu tốt hay xấu, nó chỉ '
         'nói mức rung lắc mà anh chị phải chịu được.',
  'moc': True,
  'value': -20.1,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 168,53 – NAY 134,7',
  'sub': 'cần +25% để về đỉnh',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Biên lợi nhuận gộp tám phẩy chín phần trăm, cùng kỳ mười hai phẩy bốn phần trăm, thu hẹp. Với doanh nghiệp sản xuất '
         'và dịch vụ, ba rủi ro cần theo dõi là giá đầu vào, nợ vay và sức mua của khách hàng. Một quý tăng trưởng không xóa được rủi ro chu kỳ, nên anh chị '
         'hãy hỏi: nếu giá đầu vào quay lại mức cũ, biên lợi nhuận còn bao nhiêu?',
  'anh': 'warning sign',
  'items': [('Biên lợi nhuận gộp 8,9% (cùng kỳ 12,4%)', (239, 68, 68)), ('Tỷ trọng cả nhóm ngành', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Quản trị vốn',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, quản trị vốn khi nắm giữ VJC. Em đề xuất ba câu hỏi phải trả lời trước khi mua. Một, mã này chiếm tối đa bao nhiêu phần trăm danh mục? '
         'Với một mã đơn lẻ, nhiều nhà đầu tư cá nhân giới hạn trong khoảng mười đến hai mươi phần trăm. Hai, nếu giá quay về đáy năm mươi hai tuần khoảng một '
         'trăm mười sáu phẩy bảy mươi bảy nghìn đồng, tức thấp hơn giá hiện tại khoảng mười ba phẩy ba phần trăm, thì danh mục mất bao nhiêu? Với tỷ trọng '
         'mười phần trăm, mức giảm đó làm danh mục mất khoảng một phẩy ba phần trăm. Ba, điều gì xảy ra thì luận điểm sai? Ví dụ lợi nhuận hai quý liên tiếp '
         'giảm, hoặc biên lợi nhuận xấu đi. Viết sẵn ba câu trả lời này ra giấy, anh chị sẽ bớt bị cảm xúc kéo đi khi giá biến động. Không dùng vay ký quỹ cho '
         'mã mình chưa trả lời được câu hỏi thứ ba.',
  'moc': True,
  'anh': 'balance scale',
  'cards': [('Tỷ trọng tối đa', '10–20%', 'một mã'), ('Nếu về đáy 52 tuần', '−13,3%', 'giá cổ phiếu'), ('Điểm sai', 'viết trước', 'khi mua')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước tự đọc',
  'label': '',
  'cap': ('NĂM BƯỚC', 'TỰ ĐỌC BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, năm bước anh chị có thể tự làm với mọi báo cáo doanh nghiệp. Một, lợi nhuận tám quý, lũy kế. Hai, doanh thu và biên gộp. Ba, lãi vay và '
         'dòng tiền. Bốn, P trên E cạnh tăng trưởng. Năm, tỷ trọng và điểm sai. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy '
         'Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận 8 quý, lũy kế', (34, 197, 94)),
            ('Doanh thu và biên gộp', (34, 197, 94)),
            ('Lãi vay và dòng tiền', (34, 197, 94)),
            ('P/E cạnh tăng trưởng', (34, 197, 94)),
            ('Tỷ trọng và điểm sai', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI QUÝ +8,6%', 'ĐỦ KẾT LUẬN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với VJC, anh chị đặt trọng số nhiều hơn vào kết quả quý gần nhất, hay vào chuỗi tám quý và rủi ro phía trước?'}]

S['CH2511A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'VAB – đọc BCTC',
  'cap': ('LÃI QUÝ +10,1%', 'P/B 0,73'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'VietABank, mã VAB, báo lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt hai trăm chín mươi sáu tỷ, tăng mười phẩy một '
         'phần trăm so với cùng kỳ. Lũy kế chín tháng đạt chín trăm năm mươi sáu tỷ, tăng mười ba phẩy tám phần trăm. Cổ phiếu đóng cửa ngày sáu tháng mười '
         'một năm hai nghìn không trăm hai mươi sáu ở khoảng chín nghìn đồng, thấp hơn đỉnh năm mươi hai tuần khoảng mười sáu phẩy bốn phần trăm. Con số quý '
         'này có đủ để kết luận doanh nghiệp đang khỏe lên hay yếu đi không? Trong video này, em đọc lần lượt lợi nhuận tám quý, thu nhập lãi thuần, dự phòng '
         'và nợ xấu, định giá, rủi ro cần theo dõi và cách quản trị vốn khi nắm giữ VAB. Số liệu lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai '
         'mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'bank building',
  'chart': {'sym': 'VABW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[12, 10.82, 'Đỉnh tuần 26/1/26: 10,82', 0.6], [17, 8.59, 'Đáy tuần 9/3/26: 8,59', 1.6], [51, 9.0, 'Tuần 2/11/26: 9,00', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng bốn trăm tám mươi tỷ, thấp nhất ở quý bốn năm hai '
         'nghìn không trăm hai mươi bốn với khoảng hai trăm hai mươi tám tỷ, và có ba quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm '
         'hai nghìn không trăm hai mươi lăm đạt bốn trăm tám mươi tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt bốn trăm linh tám tỷ, quý hai năm hai '
         'nghìn không trăm hai mươi sáu đạt hai trăm năm mươi hai tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt hai trăm chín mươi sáu tỷ. Khi đọc '
         'chuỗi này, anh chị đừng chỉ so với cùng kỳ năm trước. Hãy so thêm với quý liền trước và với lũy kế chín tháng, vì một quý có thể đẹp lên nhờ khoản '
         'thu bất thường, nhờ trích lập dự phòng ít đi, hoặc nhờ nền so sánh thấp. Chuỗi tám quý cho thấy lợi nhuận đang đi lên đều, đi ngang hay dao động '
         'mạnh, và đó mới là thứ giúp ước lượng quý tiếp theo.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('Q4/24', 227.9, (56, 189, 248), '228'),
           ('Q1/25', 292.9, (56, 189, 248), '293'),
           ('Q2/25', 278.5, (56, 189, 248), '278'),
           ('Q3/25', 268.6, (56, 189, 248), '269'),
           ('Q4/25', 479.9, (56, 189, 248), '480'),
           ('Q1/26', 408.5, (56, 189, 248), '408'),
           ('Q2/26', 251.8, (56, 189, 248), '252'),
           ('Q3/26', 295.6, (34, 197, 94), '296')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'label': '',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, thu nhập lãi thuần, tức phần chênh lệch giữa lãi cho vay thu vào và lãi huy động trả ra. Đây là mảng cốt lõi của ngân hàng. Thu nhập lãi '
         'thuần đạt năm trăm ba mươi bốn tỷ, giảm mười sáu phẩy ba phần trăm. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm '
         'hai nghìn không trăm hai mươi sáu, thu nhập lãi thuần cao nhất ở quý bốn năm hai nghìn không trăm hai mươi lăm với khoảng một nghìn sáu trăm linh '
         'tám tỷ, thấp nhất ở quý ba năm hai nghìn không trăm hai mươi sáu với khoảng năm trăm ba mươi bốn tỷ, và có hai quý tăng so với quý liền trước. Bốn '
         'quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt một nghìn sáu trăm linh tám tỷ, quý một năm hai nghìn không trăm hai mươi '
         'sáu đạt sáu trăm bảy mươi sáu tỷ, quý hai năm hai nghìn không trăm hai mươi sáu đạt năm trăm bảy mươi bảy tỷ, quý ba năm hai nghìn không trăm hai '
         'mươi sáu đạt năm trăm ba mươi bốn tỷ. Lãi dịch vụ tăng hai mươi sáu phẩy ba phần trăm, đạt ba mươi ba tỷ. Khi lợi nhuận tăng mà thu nhập lãi thuần '
         'giảm, phần tăng thêm đến từ nơi khác: dịch vụ, kinh doanh chứng khoán, thu hồi nợ đã xử lý, hoặc chi phí dự phòng thấp hơn. Những nguồn này thường '
         'kém đều hơn mảng cho vay, nên anh chị cần hỏi: quý sau nguồn đó có lặp lại không?',
  'anh': 'bank loan',
  'bars': [('Q4/24', 813.6, (56, 189, 248), '814'),
           ('Q1/25', 612.5, (56, 189, 248), '612'),
           ('Q2/25', 542.4, (56, 189, 248), '542'),
           ('Q3/25', 638.7, (56, 189, 248), '639'),
           ('Q4/25', 1608.3, (56, 189, 248), '1.608'),
           ('Q1/26', 675.5, (56, 189, 248), '676'),
           ('Q2/26', 576.9, (56, 189, 248), '577'),
           ('Q3/26', 534.3, (34, 197, 94), '534')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Dự phòng và nợ xấu',
  'label': '',
  'cap': ('DỰ PHÒNG', 'VÀ NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, dự phòng và nợ xấu. NIM khoảng hai phẩy hai mươi lăm phần trăm. Chi phí dự phòng giảm tám mươi chín phẩy sáu phần trăm đạt một phần lợi '
         'nhuận tăng nhờ trích lập ít hơn. Tỷ lệ nợ xấu một phẩy ba mươi tám phần trăm, tăng so với quý trước, một phẩy hai mươi hai phần trăm. Bao phủ nợ xấu '
         'chỉ khoảng năm mươi lăm phần trăm, bộ đệm dự phòng mỏng. Tỷ lệ bao phủ nợ xấu là số dự phòng đã trích chia cho tổng nợ xấu. Bao phủ một trăm phần '
         'trăm nghĩa là nếu toàn bộ nợ xấu mất trắng, ngân hàng đã có sẵn tiền dự phòng để bù. Bao phủ càng thấp thì bộ đệm càng mỏng, và lợi nhuận tương lai '
         'càng dễ bị bào mòn khi phải trích lập thêm. Hai con số này anh chị tra được trong thuyết minh báo cáo tài chính, mục chất lượng nợ cho vay.',
  'moc': True,
  'anh': 'risk management',
  'cards': [('NIM khoảng 2,25%', '', ''), ('Chi phí dự phòng giảm −89,6%: một ', '', ''), ('Tỷ lệ nợ xấu 1,38%', '', '')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, định giá. Với giá khoảng chín nghìn đồng, VAB có P trên E khoảng năm phẩy sáu mươi lăm lần, P trên B khoảng không phẩy bảy mươi ba lần, '
         'ROE khoảng mười ba phẩy bảy phần trăm. Trong hai mươi mã cùng nhóm ngân hàng có vốn hóa từ một nghìn năm trăm tỷ, P trên E trung vị khoảng bảy phẩy '
         'hai mươi lần, P trên B trung vị khoảng một phẩy mười chín lần, ROE trung vị khoảng mười bảy phẩy ba phần trăm. Với ngân hàng, P trên B nên đọc cùng '
         'ROE. Một ngân hàng có ROE cao xứng đáng được trả P trên B cao hơn, còn P trên B thấp kèm ROE thấp thì chưa chắc là rẻ. Bảng định giá và báo cáo tài '
         'chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '5,65', 'lần'), ('P/B', '0,73', 'lần'), ('ROE', '13,7%', 'trên vốn chủ')]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá cách đỉnh bao xa. Đỉnh năm mươi hai tuần của VAB khoảng mười phẩy bảy mươi bảy nghìn đồng, đáy khoảng tám phẩy sáu mươi nghìn đồng. '
         'Giá hiện tại thấp hơn đỉnh khoảng mười sáu phẩy bốn phần trăm. Người mua ở đỉnh cần cổ phiếu tăng khoảng hai mươi phần trăm mới hòa vốn. Đây là toán '
         'học của thua lỗ: giảm càng sâu thì phần tăng cần thiết để hồi lại càng lớn hơn phần đã mất. Hệ số beta của VAB khoảng không phẩy năm mươi bảy, nghĩa '
         'là trong giai đoạn đo, giá dao động ít hơn thị trường chung. Beta không nói cổ phiếu tốt hay xấu, nó chỉ nói mức rung lắc mà anh chị phải chịu được.',
  'moc': True,
  'value': -16.4,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 10,77 – NAY 9,00',
  'sub': 'cần +20% để về đỉnh',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Thu nhập lãi thuần, mảng cho vay cốt lõi giảm mười sáu phẩy ba phần trăm. Chi phí dự phòng giảm tám mươi chín phẩy '
         'sáu phần trăm đạt một phần lợi nhuận tăng nhờ trích lập ít hơn. Tỷ lệ nợ xấu một phẩy ba mươi tám phần trăm, tăng so với quý trước, một phẩy hai '
         'mươi hai phần trăm. Với cổ phiếu ngân hàng, rủi ro lớn nhất thường không nằm ở một quý lợi nhuận, mà ở chất lượng tài sản: nợ xấu, nợ tái cơ cấu và '
         'mức độ tập trung cho vay vào bất động sản. Ngoài ra, cổ phiếu ngân hàng hay biến động cùng nhau, nên anh chị cần cộng tỷ trọng cả nhóm ngân hàng '
         'trong danh mục.',
  'anh': 'warning sign',
  'items': [('Thu nhập lãi thuần (mảng cho vay cốt lõi', (239, 68, 68)),
            ('Chi phí dự phòng giảm −89,6%: một phần l', (239, 68, 68)),
            ('Tỷ lệ nợ xấu 1,38%', (239, 68, 68)),
            ('Tỷ trọng cả nhóm ngành', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Quản trị vốn',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, quản trị vốn khi nắm giữ VAB. Em đề xuất ba câu hỏi phải trả lời trước khi mua. Một, mã này chiếm tối đa bao nhiêu phần trăm danh mục? '
         'Với một mã đơn lẻ, nhiều nhà đầu tư cá nhân giới hạn trong khoảng mười đến hai mươi phần trăm. Hai, nếu giá quay về đáy năm mươi hai tuần khoảng tám '
         'phẩy sáu mươi nghìn đồng, tức thấp hơn giá hiện tại khoảng bốn phẩy bốn phần trăm, thì danh mục mất bao nhiêu? Với tỷ trọng mười phần trăm, mức giảm '
         'đó làm danh mục mất khoảng không phẩy bốn phần trăm. Ba, điều gì xảy ra thì luận điểm sai? Ví dụ lợi nhuận hai quý liên tiếp giảm, hoặc nợ xấu xấu '
         'đi. Viết sẵn ba câu trả lời này ra giấy, anh chị sẽ bớt bị cảm xúc kéo đi khi giá biến động. Không dùng vay ký quỹ cho mã mình chưa trả lời được câu '
         'hỏi thứ ba.',
  'moc': True,
  'anh': 'balance scale',
  'cards': [('Tỷ trọng tối đa', '10–20%', 'một mã'), ('Nếu về đáy 52 tuần', '−4,4%', 'giá cổ phiếu'), ('Điểm sai', 'viết trước', 'khi mua')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước tự đọc',
  'label': '',
  'cap': ('NĂM BƯỚC', 'TỰ ĐỌC BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, năm bước anh chị có thể tự làm với mọi báo cáo ngân hàng. Một, lợi nhuận tám quý, lũy kế. Hai, thu nhập lãi thuần. Ba, dự phòng, nợ xấu, '
         'bao phủ. Bốn, P trên B cạnh ROE. Năm, tỷ trọng và điểm sai. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm '
         'com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận 8 quý, lũy kế', (34, 197, 94)),
            ('Thu nhập lãi thuần', (34, 197, 94)),
            ('Dự phòng, nợ xấu, bao phủ', (34, 197, 94)),
            ('P/B cạnh ROE', (34, 197, 94)),
            ('Tỷ trọng và điểm sai', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI QUÝ +10,1%', 'ĐỦ KẾT LUẬN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với VAB, anh chị đặt trọng số nhiều hơn vào kết quả quý gần nhất, hay vào chuỗi tám quý và rủi ro phía trước?'}]

S['CH2511B'] = [{'k': 'hook',
  'label': '',
  'cap': ('5 NGÂN HÀNG', 'LÀ 1 RỦI RO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nhiều nhà đầu tư nghĩ mình đã đa dạng hóa vì danh mục có năm mã. Nhưng nếu năm mã đó là Vietcombank, BIDV, VietinBank, Techcombank và MB, thì theo '
         'dữ liệu một trăm linh bốn tuần đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, giá của chúng đi cùng chiều với nhau khá chặt: hệ '
         'số tương quan trung bình khoảng không phẩy năm mươi tám, riêng cặp Vietcombank và BIDV khoảng không phẩy tám. Video này dùng số liệu thật để trả lời '
         'ba câu: đa dạng hóa thật khác đa dạng hóa giả thế nào, nó giúp được gì, và nó không giúp được gì.',
  'anh': 'bank buildings',
  'ch': 'Mở đầu',
  'moc': True,
  'chart': {'sym': 'VCBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 78.15, 'Đỉnh tuần 12/1/26: 78,15', 0.6], [36, 52.6, 'Đáy tuần 20/7/26: 52,60', 1.6], [51, 53.6, 'Tuần 2/11/26: 53,60', 2.6]]}},
 {'k': 'text',
  'label': '',
  'cap': ('TƯƠNG QUAN', 'LÀ GÌ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Hệ số tương quan đo mức độ hai cổ phiếu đi cùng chiều. Bằng một nghĩa là luôn tăng giảm cùng nhau. Bằng không nghĩa là không liên quan. Âm nghĩa là '
         'thường đi ngược chiều. Em tính tương quan trên lợi suất từng tuần, tức phần trăm tăng giảm mỗi tuần, của mười mã trong một trăm linh bốn tuần gần '
         'nhất. Con số này thay đổi theo thời gian, nên nó là bức ảnh của giai đoạn vừa qua, không phải quy luật cố định. Thông thường, khi thị trường bình '
         'yên, tương quan giữa các mã thấp hơn; khi thị trường hoảng loạn, tương quan tăng vọt, vì gần như ai cũng bán cùng lúc. Đó cũng là lúc nhà đầu tư cần '
         'đa dạng hóa nhất, nhưng lại nhận được ít tác dụng nhất.',
  'anh': 'two lines graph',
  'ch': 'Tương quan là gì'},
 {'k': 'bars',
  'label': '',
  'cap': ('NGÂN HÀNG 0,58', 'KHÁC NGÀNH 0,33'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Kết quả. Năm ngân hàng lớn có tương quan trung bình khoảng không phẩy năm mươi tám, thấp nhất khoảng không phẩy ba mươi tám và cao nhất khoảng không '
         'phẩy tám. Năm mã khác ngành gồm Vinamilk, PV Gas, FPT, Hòa Phát và Dược Hậu Giang có tương quan trung bình chỉ khoảng không phẩy ba mươi ba. Ví dụ, '
         'Vinamilk và Hòa Phát khoảng không phẩy bốn mươi sáu, Dược Hậu Giang và FPT khoảng không phẩy năm mươi bốn. Nói đơn giản, khi một ngân hàng có tuần '
         'giảm mạnh, khả năng các ngân hàng còn lại cũng giảm cao hơn hẳn so với khi một mã tiêu dùng giảm.',
  'anh': 'comparison bars',
  'ch': 'Ngân hàng 0,58 – khác ngành 0,33',
  'moc': True,
  'bars': [('VCB–BID', 0.8, (239, 68, 68), '0,80'),
           ('TCB–MBB', 0.55, (239, 68, 68), '0,55'),
           ('TB 5 NH', 0.58, (239, 68, 68), '0,58'),
           ('VNM–HPG', 0.46, (34, 197, 94), '0,46'),
           ('DHG–FPT', 0.54, (34, 197, 94), '0,54'),
           ('TB khác ngành', 0.33, (34, 197, 94), '0,33')]},
 {'k': 'cards',
  'label': '',
  'cap': ('ĐA DẠNG HÓA', 'GIÚP GÌ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đa dạng hóa giúp gì? Nó làm giảm rung lắc thường ngày do rủi ro riêng của từng doanh nghiệp: một quý lợi nhuận xấu, một khoản nợ xấu bất ngờ, một '
         'biến động giá đầu vào. Trong một trăm linh bốn tuần, mã dao động mạnh nhất trong nhóm là PV Gas, độ lệch chuẩn lợi suất tuần khoảng năm phẩy chín '
         'phần trăm và tuần xấu nhất giảm khoảng mười tám phẩy một phần trăm. Dược Hậu Giang dao động ít nhất, khoảng một phẩy tám phần trăm. Khi gộp nhiều mã '
         'ít tương quan, những cú giật riêng lẻ như vậy được pha loãng.',
  'anh': 'diversified baskets',
  'ch': 'Đa dạng hóa giúp gì',
  'cards': [('GAS: tuần xấu nhất', '−18,1%', 'dao động 5,9%/tuần'), ('DHG: dao động', '1,8%/tuần', 'ít nhất nhóm'), ('TCB: tuần xấu nhất', '−13,2%', '')]},
 {'k': 'cards',
  'label': '',
  'cap': ('ĐA DẠNG HÓA', 'KHÔNG GIÚP GÌ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Nhưng đa dạng hóa không giúp được gì? Em thử hai danh mục chia đều, mua từ tuần ngày hai mươi tám tháng mười năm hai nghìn không trăm hai mươi bốn. '
         'Danh mục năm ngân hàng có mức sụt sâu nhất khoảng hai mươi hai phẩy sáu phần trăm và tuần xấu nhất giảm khoảng tám phẩy một phần trăm. Danh mục trộn '
         'Vietcombank, Techcombank, Vinamilk, PV Gas và FPT có mức sụt sâu nhất khoảng hai mươi bảy phẩy một phần trăm và tuần xấu nhất giảm khoảng bảy phẩy '
         'sáu phần trăm. Nghĩa là khi cả thị trường giảm, như tháng tư/hai nghìn không trăm hai mươi lăm, gần như mọi cổ phiếu cùng giảm, và đa dạng hóa giữa '
         'các cổ phiếu không chặn được cú giảm chung.',
  'anh': 'storm umbrella',
  'ch': 'Đa dạng hóa không giúp gì',
  'moc': True,
  'cards': [('5 ngân hàng', 'sụt sâu nhất −22,6%', 'tuần xấu nhất −8,1%'), ('Danh mục trộn', 'sụt sâu nhất −27,1%', 'tuần xấu nhất −7,6%')]},
 {'k': 'text',
  'label': '',
  'cap': ('RỦI RO HỆ THỐNG', 'CẦN CÔNG CỤ KHÁC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đây là phân biệt quan trọng giữa rủi ro riêng và rủi ro hệ thống. Rủi ro riêng của từng doanh nghiệp giảm được bằng cách chia nhiều mã khác ngành. '
         'Rủi ro hệ thống, tức cả thị trường cùng giảm vì lãi suất, tỷ giá hay tâm lý chung, thì không giảm được bằng cách thêm mã. Muốn giảm rủi ro hệ thống, '
         'công cụ là tỷ trọng tiền mặt, tỷ trọng tài sản khác như tiền gửi hay trái phiếu, và không dùng đòn bẩy. Thêm một mã cổ phiếu thứ mười một không thay '
         'được một phần tiền mặt.',
  'anh': 'control panel',
  'ch': 'Rủi ro hệ thống cần công cụ khác'},
 {'k': 'checklist',
  'label': '',
  'cap': ('ĐA DẠNG HÓA GIẢ', 'BA DẤU HIỆU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Ba dấu hiệu của đa dạng hóa giả. Một, nhiều mã nhưng cùng một ngành, như năm ngân hàng hay năm mã bất động sản. Hai, nhiều ngành nhưng cùng một động '
         'lực, ví dụ ngân hàng, chứng khoán và bất động sản đều nhạy với lãi suất và tín dụng. Ba, nhiều mã nhưng một mã chiếm hơn một nửa danh mục, khi đó '
         'các mã còn lại chỉ là trang trí. Anh chị có thể tự kiểm tra bằng cách viết cạnh mỗi mã một động lực chính, rồi cộng tỷ trọng theo động lực.',
  'anh': 'magnifying glass list',
  'ch': 'Đa dạng hóa giả: ba dấu hiệu',
  'moc': True,
  'items': [('Nhiều mã, một ngành', (239, 68, 68)), ('Nhiều ngành, một động lực', (239, 68, 68)), ('Một mã chiếm hơn nửa', (239, 68, 68))]},
 {'k': 'checklist',
  'label': '',
  'cap': ('ĐỔI DANH MỤC', 'VÍ DỤ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Một ví dụ chuyển đổi. Danh mục ban đầu chia đều cho năm ngân hàng lớn, mỗi mã hai mươi phần trăm. Vì Vietcombank và BIDV có tương quan khoảng không '
         'phẩy tám, hai mã này gần như một vị thế bốn mươi phần trăm. Một cách sắp xếp lại có thể là: giữ hai ngân hàng với tổng tỷ trọng ba mươi phần trăm, '
         'thêm một mã tiêu dùng, một mã năng lượng và một mã công nghệ mỗi mã khoảng mười lăm phần trăm, và giữ hai mươi lăm phần trăm tiền mặt hoặc tiền gửi. '
         'Số mã vẫn là năm, nhưng số động lực rủi ro tăng từ một lên bốn, và có thêm một phần tiền mặt cho kịch bản cả thị trường cùng giảm. Đây chỉ là ví dụ '
         'minh họa cách nghĩ, tỷ trọng cụ thể phụ thuộc mục tiêu và khả năng chịu đựng của mỗi người.',
  'anh': 'rearrange blocks',
  'ch': 'Ví dụ đổi danh mục',
  'moc': True,
  'items': [('2 ngân hàng: 30%', (255, 196, 0)), ('Tiêu dùng, năng lượng, công nghệ: 45%', (34, 197, 94)), ('Tiền mặt, tiền gửi: 25%', (34, 197, 94))]},
 {'k': 'text',
  'label': '',
  'cap': ('BAO NHIÊU MÃ', 'LÀ VỪA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Vậy bao nhiêu mã là vừa? Với nhà đầu tư cá nhân, câu trả lời thường nằm ở số mã mình đọc được báo cáo tài chính mỗi quý, thường khoảng sáu đến mười '
         'mã, chia vào ba đến năm động lực khác nhau. Ít hơn thì rủi ro riêng quá lớn. Nhiều hơn thì không theo dõi kịp, và danh mục dần trở thành một quỹ chỉ '
         'số tự chế với chi phí cao hơn. Nếu không có thời gian đọc báo cáo, một quỹ chỉ số có thể là lựa chọn đa dạng hóa rẻ hơn.',
  'anh': 'chess board',
  'ch': 'Bao nhiêu mã là vừa'},
 {'k': 'checklist',
  'label': '',
  'cap': ('BẢNG TỶ TRỌNG', 'THEO ĐỘNG LỰC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Gợi ý một bảng tỷ trọng đơn giản. Cột một, tên mã. Cột hai, động lực chính: lãi suất và tín dụng, tiêu dùng, hàng hóa, đầu tư công, xuất khẩu. Cột '
         'ba, tỷ trọng. Cuối bảng, cộng tỷ trọng theo từng động lực, và đặt giới hạn, ví dụ không động lực nào quá bốn mươi phần trăm. Thêm một dòng tiền mặt '
         'với tỷ trọng tối thiểu anh chị đã chọn. Bộ tài liệu quản trị rủi ro, gồm bảng kế hoạch và bảng tỷ trọng, có miễn phí trên trang chứng khoán Huy '
         'Nguyễn chấm com.',
  'anh': 'spreadsheet planning',
  'ch': 'Bảng tỷ trọng theo động lực',
  'moc': True,
  'items': [('Mã – động lực – tỷ trọng', (34, 197, 94)),
            ('Cộng theo động lực', (34, 197, 94)),
            ('Không động lực nào quá 40%', (255, 196, 0)),
            ('Dòng tiền mặt tối thiểu', (255, 196, 0))]},
 {'k': 'text',
  'label': '',
  'cap': ('TÓM LẠI', 'BA CÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại ba câu. Một, năm mã cùng ngành thường là một rủi ro, không phải năm. Hai, đa dạng hóa giảm rủi ro riêng, nhưng không chặn được cú giảm chung '
         'của cả thị trường. Ba, công cụ cho cú giảm chung là tiền mặt, tỷ trọng và không đòn bẩy. Số liệu trong video tính từ giá đóng cửa theo tuần, có thể '
         'kiểm tra lại trên trang chứng khoán Huy Nguyễn chấm com.',
  'anh': 'summary notes',
  'ch': 'Tóm lại ba câu'},
 {'k': 'end',
  'label': '',
  'cap': ('5 NGÂN HÀNG', 'LÀ 1 RỦI RO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Danh mục của anh chị hiện có bao nhiêu nhóm rủi ro thật sự khác nhau, nếu tính theo động lực chứ không tính theo số mã?'}]

S['CH2511C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'label': 'DPM – đọc BCTC',
  'cap': ('LÃI QUÝ −82,9%', 'P/E 8,47'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Đạm Phú Mỹ, mã DPM, báo lợi nhuận sau thuế công ty mẹ quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn mươi tỷ, giảm tám mươi hai phẩy chín phần '
         'trăm so với cùng kỳ. Lũy kế chín tháng đạt một nghìn ba trăm bốn mươi tám tỷ, tăng năm mươi chín phẩy bảy phần trăm. Cổ phiếu đóng cửa ngày sáu '
         'tháng mười một năm hai nghìn không trăm hai mươi sáu ở khoảng mười chín phẩy sáu mươi lăm nghìn đồng, thấp hơn đỉnh năm mươi hai tuần khoảng ba mươi '
         'tám phẩy ba phần trăm. Con số quý này có đủ để kết luận doanh nghiệp đang khỏe lên hay yếu đi không? Trong video này, em đọc lần lượt lợi nhuận tám '
         'quý, doanh thu và biên lợi nhuận, chi phí lãi vay và dòng tiền, định giá, rủi ro cần theo dõi và cách quản trị vốn khi nắm giữ DPM. Số liệu lấy từ '
         'báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu.',
  'moc': True,
  'anh': 'fertilizer plant',
  'chart': {'sym': 'DPMW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[17, 33.52, 'Đỉnh tuần 9/3/26: 33,52', 0.6], [51, 19.05, 'Đáy tuần 2/11/26: 19,05', 1.6], [51, 19.65, 'Tuần 2/11/26: 19,65', 2.6]]}},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận tám quý',
  'label': '',
  'cap': ('LỢI NHUẬN', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương một, lợi nhuận tám quý. Trong tám quý từ quý bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, lợi '
         'nhuận sau thuế công ty mẹ cao nhất ở quý hai năm hai nghìn không trăm hai mươi sáu với khoảng chín trăm linh sáu tỷ, thấp nhất ở quý bốn năm hai '
         'nghìn không trăm hai mươi bốn với khoảng âm hai mươi tỷ, và có bốn quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai '
         'nghìn không trăm hai mươi lăm đạt hai trăm hai mươi chín tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt bốn trăm linh hai tỷ, quý hai năm hai '
         'nghìn không trăm hai mươi sáu đạt chín trăm linh sáu tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn mươi tỷ. Khi đọc chuỗi này, anh chị '
         'đừng chỉ so với cùng kỳ năm trước. Hãy so thêm với quý liền trước và với lũy kế chín tháng, vì một quý có thể đẹp lên nhờ khoản thu bất thường, nhờ '
         'trích lập dự phòng ít đi, hoặc nhờ nền so sánh thấp. Chuỗi tám quý cho thấy lợi nhuận đang đi lên đều, đi ngang hay dao động mạnh, và đó mới là thứ '
         'giúp ước lượng quý tiếp theo.',
  'moc': True,
  'anh': 'financial chart',
  'bars': [('Q4/24', -20.0, (239, 68, 68), '-20'),
           ('Q1/25', 204.9, (56, 189, 248), '205'),
           ('Q2/25', 402.9, (56, 189, 248), '403'),
           ('Q3/25', 236.4, (56, 189, 248), '236'),
           ('Q4/25', 229.0, (56, 189, 248), '229'),
           ('Q1/26', 401.8, (56, 189, 248), '402'),
           ('Q2/26', 905.9, (56, 189, 248), '906'),
           ('Q3/26', 40.4, (34, 197, 94), '40')]},
 {'k': 'bars',
  'ch': 'Chương 2 – Doanh thu tám quý',
  'label': '',
  'cap': ('DOANH THU', 'TÁM QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương hai, doanh thu và biên lợi nhuận. Doanh thu thuần đạt bốn nghìn một trăm hai mươi tám tỷ, tăng mười phẩy bảy phần trăm. Trong tám quý từ quý '
         'bốn năm hai nghìn không trăm hai mươi bốn đến quý ba năm hai nghìn không trăm hai mươi sáu, doanh thu thuần cao nhất ở quý hai năm hai nghìn không '
         'trăm hai mươi sáu với khoảng sáu nghìn chín trăm tám mươi sáu tỷ, thấp nhất ở quý bốn năm hai nghìn không trăm hai mươi bốn với khoảng ba nghìn một '
         'trăm sáu mươi bốn tỷ, và có bốn quý tăng so với quý liền trước. Bốn quý gần nhất lần lượt là quý bốn năm hai nghìn không trăm hai mươi lăm đạt ba '
         'nghìn bốn trăm mười bốn tỷ, quý một năm hai nghìn không trăm hai mươi sáu đạt năm nghìn sáu trăm hai mươi ba tỷ, quý hai năm hai nghìn không trăm '
         'hai mươi sáu đạt sáu nghìn chín trăm tám mươi sáu tỷ, quý ba năm hai nghìn không trăm hai mươi sáu đạt bốn nghìn một trăm hai mươi tám tỷ. Biên lợi '
         'nhuận gộp mười bốn phẩy một phần trăm, cùng kỳ mười chín phẩy ba phần trăm, thu hẹp. Doanh thu cho biết doanh nghiệp bán được bao nhiêu, còn biên '
         'lợi nhuận gộp cho biết mỗi một trăm đồng doanh thu còn lại bao nhiêu đồng sau giá vốn. Doanh thu tăng mà biên co lại thường là dấu hiệu giá bán chịu '
         'áp lực hoặc chi phí đầu vào tăng nhanh hơn. Biên mở rộng mà doanh thu đi ngang thì lợi nhuận vẫn có thể tăng, nhưng mức tăng đó phụ thuộc vào giá '
         'đầu vào, thứ doanh nghiệp không kiểm soát hoàn toàn.',
  'anh': 'fertilizer plant',
  'bars': [('Q4/24', 3164.0, (56, 189, 248), '3.164'),
           ('Q1/25', 4120.1, (56, 189, 248), '4.120'),
           ('Q2/25', 5301.1, (56, 189, 248), '5.301'),
           ('Q3/25', 3728.8, (56, 189, 248), '3.729'),
           ('Q4/25', 3414.4, (56, 189, 248), '3.414'),
           ('Q1/26', 5623.2, (56, 189, 248), '5.623'),
           ('Q2/26', 6985.8, (56, 189, 248), '6.986'),
           ('Q3/26', 4128.0, (34, 197, 94), '4.128')]},
 {'k': 'cards',
  'ch': 'Chương 3 – Lãi vay và dòng tiền',
  'label': '',
  'cap': ('LÃI VAY', 'VÀ DÒNG TIỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương ba, chi phí lãi vay và dòng tiền. Bốn quý gần nhất, chi phí lãi vay cộng lại khoảng một trăm tám mươi mốt tỷ. Chi phí lãi vay tăng bốn mươi '
         'tám phẩy ba phần trăm, ăn vào lợi nhuận. Cũng trong bốn quý đó, lợi nhuận sau thuế cộng lại khoảng một nghìn năm trăm bảy mươi bảy tỷ, còn dòng tiền '
         'thuần từ hoạt động kinh doanh cộng lại khoảng một nghìn chín trăm năm mươi ba tỷ. Dòng tiền kinh doanh cao hơn lợi nhuận là dấu hiệu lợi nhuận được '
         'thu về bằng tiền thật. Doanh nghiệp vay càng nhiều thì khi lãi suất tăng, phần lợi nhuận dành cho cổ đông càng bị chia sẻ cho chủ nợ.',
  'moc': True,
  'anh': 'cash flow',
  'cards': [('Lãi vay 4 quý', '≈ 181 tỷ', ''), ('LNST 4 quý', '≈ 1.577 tỷ', ''), ('Dòng tiền KD 4 quý', '≈ 1.953 tỷ', '')]},
 {'k': 'cards',
  'ch': 'Chương 4 – Định giá',
  'label': '',
  'cap': ('BA CON SỐ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bốn, định giá. Với giá khoảng mười chín phẩy sáu mươi lăm nghìn đồng, DPM có P trên E khoảng tám phẩy bốn mươi bảy lần, P trên B khoảng một '
         'phẩy mười tám lần, ROE khoảng mười ba phẩy bảy phần trăm. Trong hai mươi mã cùng nhóm hóa chất, phân bón có vốn hóa từ một nghìn năm trăm tỷ, P trên '
         'E trung vị khoảng tám phẩy năm mươi chín lần, P trên B trung vị khoảng một phẩy bốn mươi tám lần, ROE trung vị khoảng mười hai phẩy một phần trăm. P '
         'trên E chỉ có ý nghĩa khi lợi nhuận bốn quý gần nhất phản ánh đúng sức kiếm tiền bình thường. Nếu có quý đột biến hoặc quý lỗ, P trên E sẽ bị méo, '
         'khi đó anh chị nên tính lại với lợi nhuận đã loại phần bất thường. Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán '
         'Huy Nguyễn chấm com, mục tra cứu mã.',
  'anh': 'calculator',
  'cards': [('P/E', '8,47', 'lần'), ('P/B', '1,18', 'lần'), ('ROE', '13,7%', 'trên vốn chủ')]},
 {'k': 'bignum',
  'ch': 'Chương 5 – Cách đỉnh 52 tuần',
  'label': '',
  'cap': ('CÁCH ĐỈNH', '52 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương năm, giá cách đỉnh bao xa. Đỉnh năm mươi hai tuần của DPM khoảng ba mươi mốt phẩy tám mươi ba nghìn đồng, đáy khoảng mười chín phẩy hai mươi '
         'lăm nghìn đồng. Giá hiện tại thấp hơn đỉnh khoảng ba mươi tám phẩy ba phần trăm. Người mua ở đỉnh cần cổ phiếu tăng khoảng sáu mươi hai phần trăm '
         'mới hòa vốn. Đây là toán học của thua lỗ: giảm càng sâu thì phần tăng cần thiết để hồi lại càng lớn hơn phần đã mất. Hệ số beta của DPM khoảng không '
         'phẩy bốn mươi tám, nghĩa là trong giai đoạn đo, giá dao động ít hơn thị trường chung. Beta không nói cổ phiếu tốt hay xấu, nó chỉ nói mức rung lắc '
         'mà anh chị phải chịu được.',
  'moc': True,
  'value': -38.3,
  'fmt': '{:,.1f}',
  'unit': '%',
  'top': 'ĐỈNH 31,83 – NAY 19,65',
  'sub': 'cần +62% để về đỉnh',
  'col': (239, 68, 68)},
 {'k': 'checklist',
  'ch': 'Chương 6 – Rủi ro cần theo dõi',
  'label': '',
  'cap': ('RỦI RO', 'CẦN THEO DÕI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương sáu, rủi ro cần theo dõi. Lợi nhuận quý giảm tám mươi hai phẩy chín phần trăm so với cùng kỳ. So với quý trước, lợi nhuận giảm chín mươi lăm '
         'phẩy năm phần trăm. Biên lợi nhuận gộp mười bốn phẩy một phần trăm, cùng kỳ mười chín phẩy ba phần trăm, thu hẹp. Với doanh nghiệp sản xuất và dịch '
         'vụ, ba rủi ro cần theo dõi là giá đầu vào, nợ vay và sức mua của khách hàng. Một quý tăng trưởng không xóa được rủi ro chu kỳ, nên anh chị hãy hỏi: '
         'nếu giá đầu vào quay lại mức cũ, biên lợi nhuận còn bao nhiêu?',
  'anh': 'warning sign',
  'items': [('Lợi nhuận quý giảm −82,9% so với cùng kỳ', (239, 68, 68)),
            ('So với quý trước', (239, 68, 68)),
            ('Biên lợi nhuận gộp 14,1% (cùng kỳ 19,3%)', (239, 68, 68)),
            ('Tỷ trọng cả nhóm ngành', (255, 196, 0))]},
 {'k': 'cards',
  'ch': 'Chương 7 – Quản trị vốn',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'TRƯỚC KHI MUA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương bảy, quản trị vốn khi nắm giữ DPM. Em đề xuất ba câu hỏi phải trả lời trước khi mua. Một, mã này chiếm tối đa bao nhiêu phần trăm danh mục? '
         'Với một mã đơn lẻ, nhiều nhà đầu tư cá nhân giới hạn trong khoảng mười đến hai mươi phần trăm. Hai, nếu giá quay về đáy năm mươi hai tuần khoảng '
         'mười chín phẩy hai mươi lăm nghìn đồng, tức thấp hơn giá hiện tại khoảng hai phần trăm, thì danh mục mất bao nhiêu? Với tỷ trọng mười phần trăm, mức '
         'giảm đó làm danh mục mất khoảng không phẩy hai phần trăm. Ba, điều gì xảy ra thì luận điểm sai? Ví dụ lợi nhuận hai quý liên tiếp giảm, hoặc biên '
         'lợi nhuận xấu đi. Viết sẵn ba câu trả lời này ra giấy, anh chị sẽ bớt bị cảm xúc kéo đi khi giá biến động. Không dùng vay ký quỹ cho mã mình chưa '
         'trả lời được câu hỏi thứ ba.',
  'moc': True,
  'anh': 'balance scale',
  'cards': [('Tỷ trọng tối đa', '10–20%', 'một mã'), ('Nếu về đáy 52 tuần', '−2,0%', 'giá cổ phiếu'), ('Điểm sai', 'viết trước', 'khi mua')]},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bước tự đọc',
  'label': '',
  'cap': ('NĂM BƯỚC', 'TỰ ĐỌC BCTC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Chương tám, năm bước anh chị có thể tự làm với mọi báo cáo doanh nghiệp. Một, lợi nhuận tám quý, lũy kế. Hai, doanh thu và biên gộp. Ba, lãi vay và '
         'dòng tiền. Bốn, P trên E cạnh tăng trưởng. Năm, tỷ trọng và điểm sai. Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy '
         'Nguyễn chấm com.',
  'anh': 'checklist notebook',
  'items': [('Lợi nhuận 8 quý, lũy kế', (34, 197, 94)),
            ('Doanh thu và biên gộp', (34, 197, 94)),
            ('Lãi vay và dòng tiền', (34, 197, 94)),
            ('P/E cạnh tăng trưởng', (34, 197, 94)),
            ('Tỷ trọng và điểm sai', (34, 197, 94))]},
 {'k': 'end',
  'label': '',
  'cap': ('LÃI QUÝ −82,9%', 'ĐỦ KẾT LUẬN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày sáu tháng mười một năm hai nghìn '
         'không trăm hai mươi sáu. Với DPM, anh chị đặt trọng số nhiều hơn vào kết quả quý gần nhất, hay vào chuỗi tám quý và rủi ro phía trước?'}]

