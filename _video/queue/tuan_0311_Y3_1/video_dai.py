# -*- coding: utf-8 -*-
# Đợt 1: ngày 3/11–5/11/2026 (8 video; 3/11 khung 12:00 bỏ vì kênh phụ đã có lô 20261103_1130).
# Kênh Y3 Vĩ Mô Chứng Khoán Dễ Hiểu (@chungkhoanhuynguyen7) – NV1 soạn 2/11/2026 theo claude/giao_viec/nv1_tuan_0311.md. fb_trang = TT.
# Khuôn dx2 như _video/queue/20261102_1631c/video_dai.py. SỐ VIẾT THÀNH CHỮ trong "say". circles = chỉ số tuần trong px_tuan.json (0 = tuần cũ nhất 27/10/2025, 51 = tuần 26/10/2026).
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['Y3_0311A'] = [{'k': 'hook',
  'ch': 'Mở đầu: Dầu tăng, ai hưởng lợi?',
  'moc': True,
  'label': 'GAS – PV GAS',
  'cap': ('DẦU 108,74', 'AI HƯỞNG LỢI?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'GASW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 57.43, 'Đáy tuần 27/10: 57,43', 0.6], [17, 127.79, 'Đỉnh tuần 2/3: 127,79', 1.6], [51, 77.7, '28/10: 77,70', 2.6]]},
  'anh': 'oil refinery',
  'say': 'Giá dầu Brent hôm nay là một trăm linh tám phẩy bảy mươi bốn đô la một thùng. Cao hơn khoảng sáu mươi bảy phần trăm so với một năm trước. Vậy khi dầu tăng như thế, khâu '
         'nào trong chuỗi năng lượng đang hưởng lợi, và khâu nào phải gánh chi phí? Trong video này mình đi qua ba mã: khí G A S, phân phối xăng dầu P L X, và vận tải dầu khí P V '
         'T. Và hãy ở lại đến cuối, vì có một doanh nghiệp vừa đi từ lỗ bảy trăm sáu mươi ba tỷ sang lãi hai nghìn tám trăm tỷ chỉ trong một quý.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Dầu đang ở đâu?',
  'moc': True,
  'label': 'Giá dầu thế giới 2/11/2026',
  'cap': ('GIÁ DẦU', 'HÔM NAY'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Brent (USD/thùng)', '108,74', '+67,1% sau 1 năm'),
            ('WTI (USD/thùng)', '99,81', '+63,7% sau 1 năm'),
            ('Đỉnh 1 năm Brent', '118,35', 'ngày 30/3/2026'),
            ('Đáy 1 năm Brent', '58,92', 'ngày 16/12/2025')],
  'anh': 'crude oil barrels',
  'say': 'Chương một. Dầu đang ở đâu? Theo dữ liệu thị trường thế giới cập nhật ngày hai tháng mười một, Brent đứng ở một trăm linh tám phẩy bảy mươi bốn đô la một thùng, còn dầu '
         'W T I là chín mươi chín phẩy tám mươi mốt đô la. Đỉnh một năm của Brent là một trăm mười tám phẩy ba mươi lăm đô la, hôm ba mươi tháng ba. Đáy một năm là năm mươi tám '
         'phẩy chín mươi hai đô la, hôm mười sáu tháng mười hai năm hai nghìn không trăm hai mươi lăm. Giá dầu gần gấp đôi so với đáy. Riêng phiên hai tháng mười một, Brent giảm '
         'bảy phẩy năm mươi bảy phần trăm.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Chuỗi giá trị dầu khí',
  'moc': True,
  'label': 'Dầu tăng tác động ra sao theo từng khâu (cơ chế chung)',
  'cap': ('CHUỖI', 'DẦU KHÍ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Khai thác, lọc dầu: bán sản phẩm theo giá dầu', [34, 197, 94]),
            ('Khí: giá bán thường gắn với giá dầu, có độ trễ', [34, 197, 94]),
            ('Phân phối xăng dầu: giá vốn và giá bán lệch nhịp', [255, 196, 0]),
            ('Vận tải dầu khí: phụ thuộc giá cước và nhu cầu chở', [56, 189, 248])],
  'anh': 'oil pipeline',
  'say': 'Chương hai. Chuỗi giá trị dầu khí hoạt động thế nào? Đây là cơ chế chung, không phải số liệu của riêng doanh nghiệp nào. Ở thượng nguồn, khai thác và lọc dầu bán sản '
         'phẩm theo giá dầu thế giới, nên giá lên thường là tin tốt. Ở khâu khí, giá bán nhiều hợp đồng có gắn với giá dầu, nhưng thường có độ trễ. Ở khâu phân phối xăng dầu, '
         'doanh nghiệp mua hàng theo giá này, bán ra theo giá khác, nên lợi nhuận phụ thuộc vào việc giá vốn và giá bán lệch nhịp nhau ra sao. Còn vận tải dầu khí kiếm tiền từ '
         'giá cước và khối lượng chở, không trực tiếp bán dầu. Giờ mình kiểm tra bằng số thật.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Khí: G A S',
  'moc': True,
  'label': 'GAS – Quý 2/2026',
  'cap': ('GAS', 'QUÝ 2/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST công ty mẹ', '5.860 tỷ', '+23,4% cùng kỳ'),
            ('Doanh thu thuần', '43.249 tỷ', '+43,8% cùng kỳ'),
            ('So với quý 1/2026', '+99,0%', '2.945 đến 5.860 tỷ'),
            ('P/E hiện tại', '14,8', 'ROE 18,5%')],
  'anh': 'natural gas pipeline',
  'say': 'Chương ba. Khâu khí, mã G A S. Lưu ý quan trọng: G A S chưa có báo cáo quý ba trong dữ liệu, nên mình dùng quý hai năm hai nghìn không trăm hai mươi sáu. Lợi nhuận sau '
         'thuế công ty mẹ quý hai là năm nghìn tám trăm sáu mươi tỷ đồng, tăng hai mươi ba phẩy bốn phần trăm so với cùng kỳ. Doanh thu thuần bốn mươi ba nghìn hai trăm bốn mươi '
         'chín tỷ, tăng bốn mươi ba phẩy tám phần trăm. So với quý một, lợi nhuận gần như gấp đôi, từ hai nghìn chín trăm bốn mươi lăm tỷ lên năm nghìn tám trăm sáu mươi tỷ. Về '
         'giá cổ phiếu, G A S đang ở bảy mươi bảy phẩy bảy mươi nghìn đồng, tăng ba mươi ba phẩy ba phần trăm sau một năm, nhưng giảm sáu phẩy chín phần trăm trong tháng qua, và '
         'thấp hơn đỉnh một trăm hai mươi lăm nghìn hôm bốn tháng ba. P trên E là mười bốn phẩy tám. Đây là mô tả quá khứ, không phải dự báo.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Phân phối xăng dầu: P L X',
  'moc': True,
  'label': 'PLX – LNST công ty mẹ theo quý (tỷ đồng)',
  'cap': ('PLX', 'LỖ RỒI LÃI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 611, [56, 189, 248], '611'), ('Q4/25', 565, [56, 189, 248], '565'), ('Q1/26', -763, [239, 68, 68], '−763'), ('Q2/26', 2800, [34, 197, 94], '2.800')],
  'anh': 'gas station fuel',
  'say': 'Chương bốn. Nếu dầu lên là tốt cho tất cả, thì tại sao khâu phân phối lại có quý lỗ? Mã P L X là ví dụ rõ nhất. Quý một năm hai nghìn không trăm hai mươi sáu, P L X lỗ '
         'bảy trăm sáu mươi ba tỷ đồng. Sang quý hai, lãi hai nghìn tám trăm tỷ, tăng một trăm lẻ bốn phẩy chín phần trăm so với cùng kỳ. Doanh thu thuần quý hai một trăm ba mươi '
         'sáu nghìn không trăm bốn mươi sáu tỷ, tăng bảy mươi bảy phẩy bảy phần trăm. Vì sao quý một lỗ, quý hai lãi? Dữ liệu của mình không nói nguyên nhân. Về cơ chế chung, khi '
         'giá dầu biến động mạnh, giá vốn hàng tồn kho và giá bán ra có thể lệch nhau theo từng quý. Phần giải trình cụ thể nằm trong báo cáo gốc của doanh nghiệp. P trên E của P '
         'L X là mười ba phẩy bốn mươi lăm.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Vận tải dầu khí: P V T',
  'moc': True,
  'label': 'PVT – Quý 3/2026',
  'cap': ('PVT', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST công ty mẹ', '375 tỷ', '+42,4% cùng kỳ'),
            ('Doanh thu thuần', '5.610 tỷ', '+26,9% cùng kỳ'),
            ('Lũy kế 9 tháng', '1.273 tỷ', '+64,6% cùng kỳ'),
            ('So với quý 2', '−35,2%', '579 đến 375 tỷ')],
  'anh': 'oil tanker ship',
  'say': 'Chương năm. Khâu vận tải, mã P V T, đã có báo cáo quý ba. Lợi nhuận sau thuế công ty mẹ là ba trăm bảy mươi lăm tỷ đồng, tăng bốn mươi hai phẩy bốn phần trăm so với '
         'cùng kỳ. Doanh thu năm nghìn sáu trăm mười tỷ, tăng hai mươi sáu phẩy chín phần trăm. Chín tháng đạt một nghìn hai trăm bảy mươi ba tỷ, tăng sáu mươi bốn phẩy sáu phần '
         'trăm. Nhưng so với quý hai, lợi nhuận quý ba giảm ba mươi lăm phẩy hai phần trăm, từ năm trăm bảy mươi chín tỷ xuống ba trăm bảy mươi lăm tỷ. Nguyên nhân nằm trong báo '
         'cáo gốc. P trên E của P V T là bảy phẩy mười bốn, P trên B một phẩy mười một, giá hai mươi hai phẩy tám mươi lăm nghìn đồng, tăng bốn mươi lăm phẩy ba phần trăm sau một '
         'năm. Thêm một điểm để so sánh: B S R, nhà máy lọc dầu, quý ba lãi tám nghìn chín trăm sáu mươi tám tỷ, biên lợi nhuận gộp mười sáu phẩy hai phần trăm so với hai phẩy '
         'chín phần trăm cùng kỳ.'},
 {'k': 'bars',
  'ch': 'Chương 6 – Tổng kết',
  'moc': True,
  'label': 'Tăng trưởng LNST so với cùng kỳ (%) – GAS và PLX là Q2, PVT là Q3',
  'cap': ('SO SÁNH', '3 KHÂU'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('GAS Q2', 23.4, [34, 197, 94], '+23,4%'), ('PLX Q2', 104.9, [34, 197, 94], '+104,9%'), ('PVT Q3', 42.4, [34, 197, 94], '+42,4%')],
  'anh': 'energy industry',
  'say': 'Chương sáu. Tổng kết lại. Cả ba doanh nghiệp đều có lợi nhuận tăng so với cùng kỳ ở kỳ báo cáo gần nhất: G A S tăng hai mươi ba phẩy bốn phần trăm ở quý hai, P L X tăng '
         'một trăm lẻ bốn phẩy chín phần trăm ở quý hai, P V T tăng bốn mươi hai phẩy bốn phần trăm ở quý ba. Nhưng hãy chú ý hai điều. Một là kỳ báo cáo không giống nhau, nên '
         'đừng so trực tiếp. Hai là mức dao động giữa các quý rất khác nhau: P L X từ lỗ sang lãi lớn, P V T quý ba thấp hơn quý hai.'},
 {'k': 'checklist',
  'label': 'Khi đọc doanh nghiệp dầu khí, hỏi 4 câu',
  'cap': ('CHECKLIST', 'DẦU KHÍ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Doanh nghiệp đứng ở khâu nào của chuỗi?', [56, 189, 248]),
            ('Kỳ báo cáo là quý nào, đã có quý 3 chưa?', [255, 196, 0]),
            ('Lợi nhuận quý này so với quý trước ra sao?', [34, 197, 94]),
            ('Báo cáo gốc giải trình biến động thế nào?', [239, 68, 68])],
  'anh': 'financial report analysis',
  'say': 'Vậy khi đọc một doanh nghiệp dầu khí, bạn có thể tự hỏi bốn câu. Doanh nghiệp này đứng ở khâu nào của chuỗi? Kỳ báo cáo đang xem là quý nào, đã có quý ba chưa? Lợi '
         'nhuận quý này so với quý trước ra sao, chứ không chỉ so với cùng kỳ? Và phần giải trình trong báo cáo gốc nói gì về biến động?'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CHIA SẺ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: dữ liệu thị trường thế giới cập nhật ngày hai tháng mười một năm hai nghìn không trăm hai mươi sáu, và báo cáo tài chính của các doanh nghiệp. Đây là chia sẻ '
         'kiến thức, không phải khuyến nghị mua bán. Theo bạn, trong chuỗi dầu khí, khâu nào có lợi nhuận dao động mạnh nhất? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0311C'] = [{'k': 'hook',
  'ch': 'Mở đầu: Lạm phát và biên lợi nhuận',
  'moc': True,
  'label': 'MSN – Masan',
  'cap': ('CPI +5,08%', 'AI GIỮ BIÊN?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'MSNW', 'tf': 'W', 'weeks': 52, 'circles': [[14, 85.5, 'Đỉnh tuần 2/2: 85,50', 0.6], [37, 61.7, 'Đáy tuần 20/7: 61,70', 1.6], [51, 74.2, '28/10: 74,20', 2.6]]},
  'anh': 'supermarket shelves',
  'say': 'Theo Cục Thống kê, chỉ số giá tiêu dùng tháng chín năm hai nghìn không trăm hai mươi sáu tăng năm phẩy không tám phần trăm so với cùng kỳ. Bình quân chín tháng tăng bốn '
         'phẩy năm mươi hai phần trăm. Khi chi phí đầu vào tăng, doanh nghiệp tiêu dùng nào vẫn giữ được biên lợi nhuận? Hôm nay mình soi ba cái tên: V N M, M S N và Q N S, nhắc '
         'thêm S A B. Và có một doanh nghiệp doanh thu tăng gần bảy mươi lăm phần trăm, nhưng biên lợi nhuận gộp lại thu hẹp. Chuyện gì đang xảy ra?'},
 {'k': 'cards',
  'ch': 'Chương 1 – Lạm phát đang ở mức nào?',
  'moc': True,
  'label': 'CPI tháng 9/2026 – Cục Thống kê',
  'cap': ('CPI', 'THÁNG 9/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('So cùng kỳ', '+5,08%', 'CPI tháng 9'),
            ('So tháng trước', '+0,62%', 'CPI tháng 9'),
            ('So tháng 12/2025', '+4,20%', 'CPI tháng 9'),
            ('Bình quân 9 tháng', '+4,52%', 'lạm phát cơ bản +4,26%')],
  'anh': 'market vendor Vietnam',
  'say': 'Chương một. Lạm phát đang ở mức nào? Theo Cục Thống kê, chỉ số giá tiêu dùng tháng chín tăng không phẩy sáu mươi hai phần trăm so với tháng trước, tăng năm phẩy không '
         'tám phần trăm so với cùng kỳ, và tăng bốn phẩy hai mươi phần trăm so với tháng mười hai năm hai nghìn không trăm hai mươi lăm. Bình quân chín tháng tăng bốn phẩy năm '
         'mươi hai phần trăm, còn lạm phát cơ bản bình quân tăng bốn phẩy hai mươi sáu phần trăm. Cũng theo Cục Thống kê, tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng '
         'chín tháng tăng mười ba phẩy bốn phần trăm. Tức là giá tăng, nhưng sức mua vẫn tăng. Đó là bối cảnh cho các doanh nghiệp tiêu dùng.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Giá đầu vào tăng thì biên đi đâu?',
  'moc': True,
  'label': 'Ba cách doanh nghiệp giữ biên (cơ chế chung)',
  'cap': ('GIỮ BIÊN', 'BẰNG CÁCH NÀO'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Tăng giá bán theo chi phí', [34, 197, 94]),
            ('Đổi cơ cấu sang sản phẩm biên cao', [255, 196, 0]),
            ('Tối ưu chi phí bán hàng, quản lý', [56, 189, 248]),
            ('Không làm được: biên thu hẹp', [239, 68, 68])],
  'anh': 'food factory',
  'say': 'Chương hai. Khi giá nguyên liệu tăng, biên lợi nhuận đi đâu? Đây là cơ chế chung. Doanh nghiệp có ba lựa chọn. Một là tăng giá bán, nhưng chỉ làm được nếu người mua '
         'chấp nhận. Hai là đổi cơ cấu sang sản phẩm có biên cao hơn. Ba là tiết kiệm chi phí bán hàng và quản lý. Nếu không làm được cả ba, biên gộp sẽ thu hẹp. Biên gộp là phần '
         'trăm lợi nhuận gộp trên doanh thu, nên nhìn vào nó là cách nhanh nhất để thấy áp lực chi phí đầu vào. Giờ xem số thật.'},
 {'k': 'cards',
  'ch': 'Chương 3 – M S N: doanh thu tăng vọt, biên gộp thu hẹp',
  'moc': True,
  'label': 'MSN – Quý 3/2026',
  'cap': ('MSN', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Doanh thu thuần', '36.981 tỷ', '+74,7% cùng kỳ'),
            ('LNST công ty mẹ', '3.671 tỷ', '+203,7% cùng kỳ'),
            ('Biên lợi nhuận gộp', '28,2%', 'cùng kỳ 30,4%'),
            ('Lũy kế 9 tháng', '8.042 tỷ', '+205,3%')],
  'anh': 'retail store Vietnam',
  'say': 'Chương ba. Mã M S N. Quý ba hai nghìn không trăm hai mươi sáu, doanh thu thuần ba mươi sáu nghìn chín trăm tám mươi mốt tỷ đồng, tăng bảy mươi tư phẩy bảy phần trăm. '
         'Lợi nhuận sau thuế công ty mẹ ba nghìn sáu trăm bảy mươi mốt tỷ, tăng hơn hai trăm phần trăm. Lũy kế chín tháng tám nghìn không trăm bốn mươi hai tỷ. Nhưng chú ý biên '
         'lợi nhuận gộp: hai mươi tám phẩy hai phần trăm, thấp hơn ba mươi phẩy bốn phần trăm cùng kỳ. Nghĩa là lợi nhuận tăng nhờ quy mô doanh thu lớn hơn rất nhiều, chứ không '
         'phải nhờ biên cao hơn. Vì sao doanh thu nhảy mạnh như vậy? Dữ liệu của mình không nói rõ, bạn cần xem phần giải trình trong báo cáo gốc. Cổ phiếu M S N ở bảy mươi bốn '
         'phẩy hai nghìn đồng, giảm sáu phẩy một phần trăm sau một năm, P trên E mười một phẩy hai mươi chín.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Q N S: biên gộp đi ngược chiều',
  'moc': True,
  'label': 'Biên lợi nhuận gộp quý 3/2026 so với cùng kỳ (%)',
  'cap': ('BIÊN GỘP', 'QNS VÀ MSN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('QNS Q3/25', 32.4, [56, 189, 248], '32,4%'),
           ('QNS Q3/26', 35.4, [34, 197, 94], '35,4%'),
           ('MSN Q3/25', 30.4, [56, 189, 248], '30,4%'),
           ('MSN Q3/26', 28.2, [239, 68, 68], '28,2%')],
  'anh': 'sugar cane',
  'say': 'Chương bốn. Câu chuyện của Q N S ngược lại. Quý ba, biên lợi nhuận gộp là ba mươi lăm phẩy bốn phần trăm, cao hơn ba mươi hai phẩy bốn phần trăm cùng kỳ. Doanh thu ba '
         'nghìn không trăm bảy mươi ba tỷ, tăng mười bốn phẩy năm phần trăm. Lợi nhuận bốn trăm năm mươi tỷ, tăng mười tám phẩy một phần trăm. Như vậy, trong môi trường giá đầu '
         'vào tăng, Q N S vẫn cải thiện biên gộp. Tuy nhiên lũy kế chín tháng, lợi nhuận một nghìn bốn trăm lẻ bảy tỷ chỉ tăng sáu phẩy bảy phần trăm, và quý ba thấp hơn quý hai '
         'là năm trăm sáu mươi sáu tỷ. Cổ phiếu có P trên E chín phẩy không tám, ROE mười chín phần trăm. Lý do biên cải thiện, dữ liệu không nói; đó là câu hỏi dành cho báo cáo '
         'gốc.'},
 {'k': 'cards',
  'ch': 'Chương 5 – V N M và S A B',
  'moc': True,
  'label': 'VNM – Quý 3/2026',
  'cap': ('VNM', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Doanh thu thuần', '18.465 tỷ', '+8,9% cùng kỳ'),
            ('LNST công ty mẹ', '2.964 tỷ', '+17,3% cùng kỳ'),
            ('Lũy kế 9 tháng', '8.560 tỷ', '+30,3%'),
            ('P/E | ROE', '10,43 | 31,1%', 'giá 58,20 nghìn')],
  'anh': 'dairy milk products',
  'say': 'Chương năm. V N M, doanh nghiệp sữa lớn nhất. Quý ba, doanh thu thuần mười tám nghìn bốn trăm sáu mươi lăm tỷ đồng, tăng tám phẩy chín phần trăm. Lợi nhuận hai nghìn '
         'chín trăm sáu mươi tư tỷ, tăng mười bảy phẩy ba phần trăm. Lợi nhuận tăng nhanh hơn doanh thu, nghĩa là mỗi đồng doanh thu để lại nhiều lợi nhuận hơn. Gói dữ liệu của '
         'mình không có biên gộp riêng của V N M nên mình không nói thêm. Lũy kế chín tháng tám nghìn năm trăm sáu mươi tỷ, tăng ba mươi phẩy ba phần trăm. R O E ba mươi mốt phẩy '
         'một phần trăm, P trên E mười phẩy bốn ba. Giá cổ phiếu năm mươi tám phẩy hai nghìn đồng, tăng bốn phẩy bảy phần trăm sau một năm. Nhắc thêm S A B: quý ba doanh thu sáu '
         'nghìn sáu trăm tám mươi tư tỷ tăng ba phẩy tám phần trăm, nhưng lợi nhuận một nghìn hai trăm ba mươi hai tỷ giảm chín phẩy bốn phần trăm.'},
 {'k': 'bars',
  'ch': 'Chương 6 – So sánh nhanh',
  'moc': True,
  'label': 'Tăng trưởng LNST quý 3/2026 so với cùng kỳ (%)',
  'cap': ('LỢI NHUẬN', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('MSN', 203.7, [34, 197, 94], '+203,7%'), ('QNS', 18.1, [34, 197, 94], '+18,1%'), ('VNM', 17.3, [34, 197, 94], '+17,3%'), ('SAB', -9.4, [239, 68, 68], '−9,4%')],
  'anh': 'consumer goods',
  'say': 'Chương sáu. Đặt cạnh nhau, ba doanh nghiệp đều có lợi nhuận quý ba tăng so với cùng kỳ, còn S A B giảm chín phẩy bốn phần trăm. Nhưng tăng lợi nhuận không đồng nghĩa '
         'giữ biên. M S N tăng lợi nhuận hơn hai trăm phần trăm trong khi biên gộp thu hẹp. Q N S vừa tăng lợi nhuận vừa cải thiện biên gộp. V N M tăng lợi nhuận nhanh hơn doanh '
         'thu. Bài học: một chỉ số không đủ, hãy nhìn doanh thu, biên gộp và lợi nhuận cùng lúc.'},
 {'k': 'checklist',
  'label': 'Đọc doanh nghiệp tiêu dùng trong lúc lạm phát',
  'cap': ('CHECKLIST', 'LẠM PHÁT'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Biên gộp quý này so với cùng kỳ', [255, 196, 0]),
            ('Doanh thu có tăng nhanh hơn lợi nhuận?', [56, 189, 248]),
            ('Lợi nhuận tăng nhờ quy mô hay nhờ biên?', [34, 197, 94]),
            ('Đọc phần giải trình của báo cáo gốc', [239, 68, 68])],
  'anh': 'financial analysis',
  'say': 'Vậy khi lạm phát cao, bạn có thể kiểm tra bốn điều. Biên gộp quý này so với cùng kỳ ra sao? Doanh thu có tăng nhanh hơn lợi nhuận hay chậm hơn? Lợi nhuận tăng nhờ quy '
         'mô hay nhờ biên cao hơn? Và phần giải trình trong báo cáo gốc nói gì? Làm đủ bốn bước này, bạn sẽ hiểu rõ hơn doanh nghiệp đang chịu áp lực chi phí đến đâu.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CHIA SẺ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: Cục Thống kê về chỉ số giá tiêu dùng và bán lẻ chín tháng, cùng báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của các doanh nghiệp. Đây là chia '
         'sẻ kiến thức, không phải khuyến nghị mua bán. Theo bạn, doanh nghiệp tiêu dùng nên ưu tiên giữ biên hay giữ thị phần? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0411A'] = [{'k': 'hook',
  'ch': 'Mở đầu: Lãi suất tăng, ai trả giá?',
  'moc': True,
  'label': 'HSG – Hoa Sen',
  'cap': ('LÃI SUẤT 6,38%', 'AI TRẢ GIÁ?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'HSGW', 'tf': 'W', 'weeks': 52, 'circles': [[3, 13.65, 'Đỉnh tuần 17/11: 13,65', 0.6], [38, 9.7, 'Đáy tuần 27/7: 9,70', 1.6], [51, 11.1, '28/10: 11,10', 2.6]]},
  'anh': 'steel factory',
  'say': 'Theo Ngân hàng Nhà nước, lãi suất tiền gửi bình quân giao dịch phát sinh mới là sáu phẩy ba mươi tám phần trăm một năm, tăng một phẩy mười lăm điểm phần trăm so với '
         'cuối năm hai nghìn không trăm hai mươi lăm. Khi lãi suất đi lên, doanh nghiệp vay nhiều phải trả giá thế nào? Hôm nay mình nhìn vào chi phí lãi vay của H S G, N K G và '
         'F R T, nhắc thêm H P G. Có một doanh nghiệp doanh thu tăng hai mươi bốn phần trăm nhưng lợi nhuận quý ba lại giảm gần bốn mươi phần trăm.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Lãi suất đang ở đâu?',
  'moc': True,
  'label': 'Lãi suất – Ngân hàng Nhà nước',
  'cap': ('LÃI SUẤT', 'TIỀN GỬI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Lãi suất tiền gửi mới', '6,38%/năm', 'số liệu ngày 20/9/2026'),
            ('Tăng so với cuối 2025', '+1,15', 'điểm phần trăm'),
            ('Lãi suất điều hành', 'Giữ nguyên', 'theo NHNN'),
            ('Yêu cầu với tổ chức tín dụng', 'Giảm lãi vay', 'theo NHNN')],
  'anh': 'bank counter Vietnam',
  'say': 'Chương một. Lãi suất đang ở đâu? Theo họp báo quý ba của Ngân hàng Nhà nước ngày bảy tháng mười, lãi suất tiền gửi bình quân giao dịch phát sinh mới là sáu phẩy ba mươi '
         'tám phần trăm một năm, theo số liệu ngày hai mươi tháng chín. Mức này cao hơn cuối năm hai nghìn không trăm hai mươi lăm là một phẩy mười lăm điểm phần trăm. Ngân hàng '
         'Nhà nước tiếp tục giữ nguyên lãi suất điều hành và yêu cầu các tổ chức tín dụng giảm lãi suất cho vay. Lãi suất tiền gửi tăng thường kéo chi phí vốn của ngân hàng lên, '
         'và chi phí đó có thể lan sang lãi suất cho vay. Đó là cơ chế chung, và mình sẽ kiểm tra qua số liệu doanh nghiệp.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Chi phí lãi vay ăn vào lợi nhuận thế nào?',
  'moc': True,
  'label': 'Chi phí lãi vay phụ thuộc hai yếu tố (cơ chế chung)',
  'cap': ('CHI PHÍ', 'LÃI VAY'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Chi phí lãi vay = dư nợ vay × lãi suất', [255, 196, 0]),
            ('Lãi suất tăng làm chi phí tăng', [239, 68, 68]),
            ('Vay thêm để mở rộng cũng làm tăng', [56, 189, 248]),
            ('Phải đọc báo cáo để tách hai yếu tố', [34, 197, 94])],
  'anh': 'loan contract',
  'say': 'Chương hai. Chi phí lãi vay ăn vào lợi nhuận thế nào? Cơ chế chung là: chi phí lãi vay bằng dư nợ vay nhân với lãi suất. Lãi suất tăng làm chi phí tăng. Nhưng doanh '
         'nghiệp vay thêm để mở rộng sản xuất hay tích trữ hàng cũng làm chi phí tăng. Vì vậy, khi thấy chi phí lãi vay tăng mạnh, chưa thể kết luận là do lãi suất. Dữ liệu của '
         'mình cho biết mức tăng chi phí lãi vay, nhưng không tách được phần do lãi suất và phần do vay thêm. Hãy nhớ điều này khi xem các con số tiếp theo.'},
 {'k': 'cards',
  'ch': 'Chương 3 – H S G: doanh thu tăng, lợi nhuận giảm',
  'moc': True,
  'label': 'HSG – Quý 3/2026',
  'cap': ('HSG', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Doanh thu thuần', '10.384 tỷ', '+24,3% cùng kỳ'),
            ('LNST công ty mẹ', '55 tỷ', '−37,4% cùng kỳ'),
            ('Chi phí lãi vay', '+195,8%', 'so với cùng kỳ'),
            ('So với quý 2', '−85,6%', '382 đến 55 tỷ')],
  'anh': 'steel coil',
  'say': 'Chương ba. Mã H S G, tập đoàn thép Hoa Sen. Quý ba, doanh thu thuần mười nghìn ba trăm tám mươi bốn tỷ đồng, tăng hai mươi bốn phẩy ba phần trăm. Nhưng lợi nhuận sau '
         'thuế công ty mẹ chỉ năm mươi lăm tỷ, giảm ba mươi bảy phẩy bốn phần trăm so với cùng kỳ. Nguyên nhân nổi bật trong dữ liệu là chi phí lãi vay tăng một trăm chín mươi '
         'lăm phẩy tám phần trăm. So với quý hai, lợi nhuận giảm tám mươi lăm phẩy sáu phần trăm, từ ba trăm tám mươi hai tỷ xuống năm mươi lăm tỷ. Lũy kế chín tháng năm trăm sáu '
         'mươi mốt tỷ, giảm một phẩy năm phần trăm. R O E chỉ năm phẩy bảy phần trăm, P trên B không phẩy bảy mươi bốn, cổ phiếu mười một phẩy một nghìn đồng, giảm mười bốn phẩy '
         'bốn phần trăm sau một năm. Phần giải trình chi tiết, bạn xem trong báo cáo gốc.'},
 {'k': 'bars',
  'ch': 'Chương 4 – N K G và F R T',
  'moc': True,
  'label': 'Chi phí lãi vay quý 3/2026 so với cùng kỳ (%)',
  'cap': ('LÃI VAY', 'TĂNG BAO NHIÊU'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('HSG', 195.8, [239, 68, 68], '+195,8%'), ('FRT', 157.4, [239, 68, 68], '+157,4%'), ('HPG', 118.4, [239, 68, 68], '+118,4%'), ('NKG', 83.0, [239, 68, 68], '+83,0%')],
  'anh': 'retail store electronics',
  'say': 'Chương bốn. Nhưng không phải doanh nghiệp nào có chi phí lãi vay tăng cũng giảm lợi nhuận. N K G quý ba có chi phí lãi vay tăng tám mươi ba phần trăm, nhưng lợi nhuận '
         'một trăm hai mươi sáu tỷ lại tăng một trăm năm mươi tư phẩy tám phần trăm, nhờ biên lợi nhuận gộp lên chín phần trăm so với bốn phẩy tám phần trăm cùng kỳ. F R T, chuỗi '
         'bán lẻ, chi phí lãi vay tăng một trăm năm mươi bảy phẩy bốn phần trăm, nhưng doanh thu mười bảy nghìn năm trăm ba mươi tỷ tăng ba mươi ba phẩy bảy phần trăm, lợi nhuận '
         'bốn trăm bốn mươi tỷ tăng hơn gấp đôi. Nhắc thêm H P G: chi phí lãi vay tăng một trăm mười tám phẩy bốn phần trăm, nhưng lợi nhuận tám nghìn hai trăm mười bảy tỷ vẫn '
         'tăng một trăm lẻ sáu phần trăm. Như vậy, chi phí lãi vay tăng là gánh nặng, nhưng kết quả cuối cùng còn tùy doanh nghiệp có đủ biên lợi nhuận để gánh hay không.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Định giá và giá cổ phiếu',
  'moc': True,
  'label': 'Chỉ số định giá hiện tại',
  'cap': ('ĐỊNH GIÁ', 'HIỆN TẠI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('HSG P/B | ROE', '0,74 | 5,7%', 'giá 11,10 nghìn'),
            ('NKG P/B | ROE', '0,75 | 3,2%', 'giá 12,15 nghìn'),
            ('FRT P/E | ROE', '23,38 | 25,4%', 'giá 147 nghìn'),
            ('HPG P/E | ROE', '6,46 | 19,9%', 'giá 20,75 nghìn')],
  'anh': 'stock market board',
  'say': 'Chương năm. Thị trường định giá ba doanh nghiệp này ra sao? H S G có P trên B không phẩy bảy mươi bốn, R O E năm phẩy bảy phần trăm. N K G có P trên B không phẩy bảy '
         'mươi lăm, R O E ba phẩy hai phần trăm. F R T có P trên E hai mươi ba phẩy ba mươi tám và R O E hai mươi lăm phẩy bốn phần trăm. Còn H P G có P trên E sáu phẩy bốn mươi '
         'sáu, R O E mười chín phẩy chín phần trăm. Con số cho thấy hai doanh nghiệp thép có R O E thấp đang được định giá dưới giá trị sổ sách, còn doanh nghiệp bán lẻ có R O E '
         'cao được định giá cao hơn. Đây chỉ là mô tả hiện tại, không phải dự báo.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cần hỏi gì khi lãi suất tăng?',
  'moc': True,
  'label': 'Đọc doanh nghiệp vay nhiều',
  'cap': ('CHECKLIST', 'VAY NHIỀU'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Chi phí lãi vay tăng bao nhiêu so với cùng kỳ?', [239, 68, 68]),
            ('Biên lợi nhuận gộp có đủ gánh không?', [255, 196, 0]),
            ('Doanh thu tăng nhanh hơn chi phí lãi vay?', [34, 197, 94]),
            ('Lợi nhuận quý so với quý trước ra sao?', [56, 189, 248])],
  'anh': 'financial report',
  'say': 'Chương sáu. Khi lãi suất tăng, bạn có thể hỏi bốn câu với doanh nghiệp vay nhiều. Chi phí lãi vay tăng bao nhiêu so với cùng kỳ? Biên lợi nhuận gộp có đủ gánh khoản đó '
         'không? Doanh thu có tăng nhanh hơn chi phí lãi vay không? Và lợi nhuận quý này so với quý trước biến động thế nào? Hoa Sen cho thấy khi biên mỏng thì chi phí lãi vay là '
         'yếu tố quyết định, còn N K G và F R T cho thấy khi biên cải thiện thì doanh nghiệp vẫn gánh được.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CHIA SẺ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: Ngân hàng Nhà nước cho lãi suất tiền gửi bình quân, cùng báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của các doanh nghiệp. Đây là chia sẻ kiến '
         'thức, không phải khuyến nghị mua bán. Theo bạn, chi phí lãi vay tăng là rủi ro lớn nhất của doanh nghiệp vay nhiều không? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0411B'] = [{'k': 'hook',
  'ch': 'Mở đầu: Tín dụng tăng, ngân hàng nào hưởng?',
  'moc': True,
  'label': 'ACB – Ngân hàng Á Châu',
  'cap': ('TÍN DỤNG +16,69%', 'AI HƯỞNG?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'ACBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[18, 18.7, 'Đáy tuần 9/3: 18,70', 0.6], [36, 23.85, 'Đỉnh tuần 13/7: 23,85', 1.6], [51, 21.35, '28/10: 21,35', 2.6]]},
  'anh': 'bank branch Vietnam',
  'say': 'Theo Ngân hàng Nhà nước, dư nợ tín dụng toàn hệ thống đến ngày ba mươi tháng chín tăng mười một phẩy năm mươi chín phần trăm so với cuối năm, và mười sáu phẩy sáu mươi '
         'chín phần trăm so với cùng kỳ năm trước. Tín dụng tăng nhanh như vậy, nhưng ngân hàng nào thật sự biến nó thành thu nhập lãi thuần, và ngân hàng nào chưa? Mình so sánh '
         'bốn cái tên: A C B, T P B, V I B và M S B, nhắc thêm O C B và L P B. Có một ngân hàng lợi nhuận tăng gần ba mươi phần trăm mà thu nhập lãi thuần lại giảm. Chuyện đó là '
         'sao?'},
 {'k': 'cards',
  'ch': 'Chương 1 – Tín dụng toàn hệ thống',
  'moc': True,
  'label': 'Tín dụng – Ngân hàng Nhà nước, đến 30/9/2026',
  'cap': ('TÍN DỤNG', 'TOÀN HỆ THỐNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Dư nợ tín dụng', '20,75 triệu tỷ', 'đến 30/9/2026'),
            ('So với cuối 2025', '+11,59%', 'theo NHNN'),
            ('So với cùng kỳ', '+16,69%', 'theo NHNN'),
            ('Mục tiêu cả năm', 'khoảng 15%', 'có điều chỉnh')],
  'anh': 'banking Vietnam',
  'say': 'Chương một. Bức tranh toàn hệ thống. Theo Ngân hàng Nhà nước, dư nợ tín dụng đến ngày ba mươi tháng chín khoảng hai mươi phẩy bảy mươi lăm triệu tỷ đồng. Tăng mười một '
         'phẩy năm mươi chín phần trăm so với cuối năm hai nghìn không trăm hai mươi lăm, và tăng mười sáu phẩy sáu mươi chín phần trăm so với cùng kỳ. Mục tiêu cả năm khoảng '
         'mười lăm phần trăm, có điều chỉnh, theo họp báo ngày hai tháng bảy. Cho vay nhiều hơn là điều kiện cần để ngân hàng có thu nhập lãi cao hơn. Nhưng điều kiện đủ còn phụ '
         'thuộc vào chênh lệch giữa lãi cho vay và chi phí vốn. Mình sẽ nhìn trực tiếp vào thu nhập lãi thuần.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Từ tín dụng đến thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần phụ thuộc gì? (cơ chế chung)',
  'cap': ('LÃI THUẦN', 'NGÂN HÀNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Dư nợ cho vay lớn hơn', [34, 197, 94]),
            ('Chênh lệch lãi cho vay trừ chi phí vốn (NIM)', [255, 196, 0]),
            ('Chi phí dự phòng ăn vào lợi nhuận sau cùng', [239, 68, 68]),
            ('Thu nhập ngoài lãi bù đắp', [56, 189, 248])],
  'anh': 'bank loan',
  'say': 'Chương hai. Từ tín dụng đến thu nhập lãi thuần cần mấy bước? Một là dư nợ cho vay lớn hơn. Hai là chênh lệch giữa lãi cho vay và chi phí vốn, gọi là N I M. Ba là chi '
         'phí dự phòng: ngân hàng cho vay nhiều nhưng nợ xấu tăng thì phải trích lập nhiều, ăn vào lợi nhuận cuối cùng. Bốn là thu nhập ngoài lãi, như lãi dịch vụ, có thể bù đắp. '
         'Lưu ý: gói dữ liệu của mình không có mức tăng trưởng tín dụng riêng của từng ngân hàng, nên mình dùng thu nhập lãi thuần làm thước đo.'},
 {'k': 'cards',
  'ch': 'Chương 3 – A C B: lãi thuần tăng, dự phòng cũng tăng',
  'moc': True,
  'label': 'ACB – Quý 3/2026',
  'cap': ('ACB', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Thu nhập lãi thuần', '8.195 tỷ', '+21,1% cùng kỳ'),
            ('LNST công ty mẹ', '4.699 tỷ', '+9,8% cùng kỳ'),
            ('Chi phí dự phòng', '+223,2%', 'so với cùng kỳ'),
            ('Nợ xấu', '1,19%', 'quý trước 1,03%')],
  'anh': 'bank building',
  'say': 'Chương ba. A C B. Quý ba hai nghìn không trăm hai mươi sáu, thu nhập lãi thuần tám nghìn một trăm chín mươi lăm tỷ đồng, tăng hai mươi mốt phẩy một phần trăm. Nhưng lợi '
         'nhuận sau thuế công ty mẹ bốn nghìn sáu trăm chín mươi chín tỷ chỉ tăng chín phẩy tám phần trăm. Khoảng cách này đến từ chi phí dự phòng, tăng hai trăm hai mươi ba phẩy '
         'hai phần trăm. Tỷ lệ nợ xấu một phẩy mười chín phần trăm, tăng so với một phẩy không ba phần trăm quý trước, còn bao phủ nợ xấu khoảng chín mươi mốt phần trăm. Lũy kế '
         'chín tháng mười ba nghìn ba trăm mười hai tỷ, tăng ba phẩy bảy phần trăm. P trên E bảy phẩy năm mươi bảy, R O E mười sáu phẩy năm phần trăm, giá hai mươi mốt phẩy ba '
         'mươi lăm nghìn đồng.'},
 {'k': 'cards',
  'ch': 'Chương 4 – T P B: thu nhập lãi thuần tăng mạnh nhất',
  'moc': True,
  'label': 'TPB – Quý 3/2026',
  'cap': ('TPB', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Thu nhập lãi thuần', '4.424 tỷ', '+36,6% cùng kỳ'),
            ('LNST công ty mẹ', '2.393 tỷ', '+57,4% cùng kỳ'),
            ('NIM', 'khoảng 2,58%', 'quý 3/2026'),
            ('P/E | ROE', '5,32 | 17,9%', 'giá 13 nghìn')],
  'anh': 'bank customer service',
  'say': 'Chương bốn. T P B là cái tên tăng thu nhập lãi thuần mạnh nhất trong nhóm. Quý ba, thu nhập lãi thuần bốn nghìn bốn trăm hai mươi bốn tỷ đồng, tăng ba mươi sáu phẩy sáu '
         'phần trăm. Lợi nhuận hai nghìn ba trăm chín mươi ba tỷ, tăng năm mươi bảy phẩy bốn phần trăm, và tăng ba mươi mốt phần trăm so với quý hai. N I M khoảng hai phẩy năm '
         'mươi tám phần trăm. P trên E chỉ năm phẩy ba mươi hai, R O E mười bảy phẩy chín phần trăm, giá mười ba nghìn đồng, giảm chín phẩy bốn phần trăm sau một năm.'},
 {'k': 'bars',
  'ch': 'Chương 5 – V I B, M S B và hai ngân hàng nhắc thêm',
  'moc': True,
  'label': 'Tăng trưởng thu nhập lãi thuần quý 3/2026 so với cùng kỳ (%)',
  'cap': ('LÃI THUẦN', '6 NGÂN HÀNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('TPB', 36.6, [34, 197, 94], '+36,6%'),
           ('MSB', 21.6, [34, 197, 94], '+21,6%'),
           ('ACB', 21.1, [34, 197, 94], '+21,1%'),
           ('VIB', 14.6, [56, 189, 248], '+14,6%'),
           ('OCB', 14.2, [56, 189, 248], '+14,2%'),
           ('LPB', -7.4, [239, 68, 68], '−7,4%')],
  'anh': 'bank teller',
  'say': 'Chương năm. V I B quý ba thu nhập lãi thuần bốn nghìn bảy trăm tám mươi mốt tỷ, tăng mười bốn phẩy sáu phần trăm, lãi dịch vụ tăng hơn gấp đôi lên chín trăm chín mươi '
         'tỷ. Nhưng nợ xấu ba phẩy hai phần trăm và bao phủ chỉ khoảng bốn mươi hai phần trăm, bộ đệm mỏng. M S B thu nhập lãi thuần ba nghìn bốn trăm hai mươi hai tỷ, tăng hai '
         'mươi mốt phẩy sáu phần trăm, lợi nhuận tăng hai mươi chín phẩy bốn phần trăm, nợ xấu hai phẩy bảy phần trăm. Nhắc thêm O C B: thu nhập lãi thuần tăng mười bốn phẩy hai '
         'phần trăm. Và L P B là trường hợp đặc biệt: thu nhập lãi thuần giảm bảy phẩy bốn phần trăm xuống ba nghìn chín trăm hai mươi ba tỷ, nhưng lợi nhuận vẫn tăng hai mươi '
         'tám phẩy chín phần trăm nhờ lãi dịch vụ ba nghìn ba trăm chín mươi lăm tỷ. Nhìn vào mốc so sánh thô là tín dụng toàn hệ thống tăng mười sáu phẩy sáu mươi chín phần '
         'trăm, T P B, M S B và A C B có thu nhập lãi thuần tăng cao hơn mức đó, còn V I B, O C B và L P B thấp hơn.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cách đọc ngân hàng',
  'moc': True,
  'label': 'Đọc ngân hàng khi tín dụng tăng',
  'cap': ('CHECKLIST', 'NGÂN HÀNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Thu nhập lãi thuần tăng bao nhiêu?', [34, 197, 94]),
            ('Chi phí dự phòng có tăng mạnh?', [239, 68, 68]),
            ('Nợ xấu và bao phủ nợ xấu', [255, 196, 0]),
            ('Lợi nhuận đến từ lãi hay từ dịch vụ?', [56, 189, 248])],
  'anh': 'bank analysis',
  'say': 'Chương sáu. Tóm lại, khi đọc một ngân hàng lúc tín dụng tăng, bạn có thể hỏi bốn câu. Thu nhập lãi thuần tăng bao nhiêu? Chi phí dự phòng có tăng mạnh không? Nợ xấu và '
         'mức bao phủ nợ xấu thế nào? Lợi nhuận đến từ hoạt động cho vay hay từ dịch vụ? T P B biến tín dụng thành thu nhập lãi thuần tốt nhất trong nhóm. A C B tăng thu nhập lãi '
         'nhưng dự phòng cũng tăng. L P B cho thấy lợi nhuận có thể tăng dù thu nhập lãi giảm.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CHIA SẺ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: Ngân hàng Nhà nước về dư nợ tín dụng đến ba mươi tháng chín, và báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của các ngân hàng. Đây là chia sẻ '
         'kiến thức, không phải khuyến nghị mua bán. Theo bạn, thu nhập lãi thuần hay lợi nhuận dịch vụ bền vững hơn? Hãy để lại bình luận. Xem thêm tại chungkhoanhuynguyen chấm '
         'com.'}]

S['Y3_0411C'] = [{'k': 'hook',
  'ch': 'Mở đầu: Đồng nội tệ mạnh lên',
  'moc': True,
  'label': 'DHG – Dược Hậu Giang',
  'cap': ('USD/VND 25.802', 'AI ĐƯỢC MẤT?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'DHGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 99.12, 'Đỉnh tuần 27/10: 99,12', 0.6], [37, 85.19, 'Đáy tuần 20/7: 85,19', 1.6], [51, 87.3, '28/10: 87,30', 2.6]]},
  'anh': 'pharmaceutical factory',
  'say': 'Tỷ giá đô la so với đồng Việt Nam trên thị trường hôm nay là hai mươi lăm nghìn tám trăm linh hai đồng. Giảm không phẩy bảy phần trăm trong tháng, và giảm một phẩy chín '
         'phần trăm sau một năm. Nghĩa là đồng nội tệ đang mạnh lên so với đô la. Vậy ai được lợi, ai bị thiệt? Doanh nghiệp xuất khẩu, doanh nghiệp nhập nguyên liệu, hay doanh '
         'nghiệp có lãi bằng đô la? Hôm nay mình xem T N G, V E A và D H G. Trong đó có một doanh nghiệp lợi nhuận lớn hơn cả doanh thu, và mình sẽ giải thích vì sao đừng vội suy '
         'diễn.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Tỷ giá đang ở đâu?',
  'moc': True,
  'label': 'USD/VND thị trường 2/11/2026',
  'cap': ('TỶ GIÁ', 'USD/VND'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Tỷ giá thị trường', '25.802', '2/11/2026'),
            ('Trong 1 tháng', '−0,7%', '3 tháng −1,8%'),
            ('Sau 1 năm', '−1,9%', '2 năm +2,1%'),
            ('Đỉnh 1 năm', '26.378', 'ngày 19/11/2025')],
  'anh': 'currency exchange',
  'say': 'Chương một. Tỷ giá đang ở đâu? Theo dữ liệu thị trường cập nhật ngày hai tháng mười một, tỷ giá đô la đồng là hai mươi lăm nghìn tám trăm linh hai. Giảm không phẩy bảy '
         'phần trăm trong một tháng, giảm một phẩy tám phần trăm trong ba tháng, và giảm một phẩy chín phần trăm sau một năm. Đỉnh một năm là hai mươi sáu nghìn ba trăm bảy mươi '
         'tám, hôm mười chín tháng mười một năm ngoái. Còn giá bán của ngân hàng là hai mươi lăm nghìn chín trăm tám mươi. Chỉ số đô la thế giới D X Y đứng ở một trăm lẻ một phẩy '
         'sáu mươi lăm. Mình không bàn nguyên nhân hay dự báo tỷ giá; mình chỉ hỏi: khi đồng nội tệ mạnh lên, cơ chế chung tác động tới doanh nghiệp ra sao?'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Cơ chế: ai được, ai mất?',
  'moc': True,
  'label': 'Đồng nội tệ mạnh lên (cơ chế chung)',
  'cap': ('NỘI TỆ', 'MẠNH LÊN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Xuất khẩu thu USD: quy ra đồng ít hơn', [239, 68, 68]),
            ('Nhập nguyên liệu bằng USD: chi phí giảm', [34, 197, 94]),
            ('Nợ vay USD: gánh nặng quy đồng nhẹ hơn', [34, 197, 94]),
            ('Tài sản, lãi bằng USD: quy ra đồng ít hơn', [239, 68, 68])],
  'anh': 'container port',
  'say': 'Chương hai. Cơ chế chung là thế này. Khi đồng nội tệ mạnh lên, một đô la đổi được ít đồng hơn. Doanh nghiệp xuất khẩu thu tiền bằng đô la nên quy ra đồng sẽ ít hơn. '
         'Doanh nghiệp nhập nguyên liệu bằng đô la thì chi phí quy ra đồng thấp hơn. Doanh nghiệp có nợ vay bằng đô la thấy gánh nặng quy ra đồng nhẹ hơn. Còn doanh nghiệp có tài '
         'sản hoặc lãi bằng đô la thì giá trị quy ra đồng giảm. Nhưng mỗi doanh nghiệp có tỷ lệ doanh thu xuất khẩu, tỷ lệ nguyên liệu nhập và tỷ lệ vay ngoại tệ khác nhau, mà '
         'gói dữ liệu của mình không có những tỷ lệ này. Vì vậy mình chỉ mô tả kết quả kinh doanh, không gán nguyên nhân cho tỷ giá.'},
 {'k': 'cards',
  'ch': 'Chương 3 – T N G: doanh nghiệp dệt may',
  'moc': True,
  'label': 'TNG – Quý 3/2026',
  'cap': ('TNG', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Doanh thu thuần', '3.229 tỷ', '+22,6% cùng kỳ'),
            ('LNST công ty mẹ', '152 tỷ', '+29,5% cùng kỳ'),
            ('Lũy kế 9 tháng', '362 tỷ', '+29,0%'),
            ('P/E | ROE', '4,86 | 23,7%', 'P/B 1,13')],
  'anh': 'garment factory',
  'say': 'Chương ba. T N G, doanh nghiệp may mặc, thuộc nhóm thường có doanh thu xuất khẩu. Quý ba hai nghìn không trăm hai mươi sáu, doanh thu thuần ba nghìn hai trăm hai mươi '
         'chín tỷ đồng, tăng hai mươi hai phẩy sáu phần trăm. Lợi nhuận sau thuế công ty mẹ một trăm năm mươi hai tỷ, tăng hai mươi chín phẩy năm phần trăm. Lũy kế chín tháng ba '
         'trăm sáu mươi hai tỷ, tăng hai mươi chín phần trăm. Như vậy, trong giai đoạn đồng nội tệ mạnh dần, lợi nhuận quý ba của T N G vẫn tăng. Dữ liệu không cho biết tỷ giá '
         'đóng góp bao nhiêu vào kết quả này. P trên E là bốn phẩy tám mươi sáu, R O E hai mươi ba phẩy bảy phần trăm.'},
 {'k': 'cards',
  'ch': 'Chương 4 – V E A: lợi nhuận lớn hơn doanh thu',
  'moc': True,
  'label': 'VEA – Quý 3/2026',
  'cap': ('VEA', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Doanh thu thuần', '1.256 tỷ', '+15,2% cùng kỳ'),
            ('LNST công ty mẹ', '1.893 tỷ', '+5,2% cùng kỳ'),
            ('Lũy kế 9 tháng', '5.849 tỷ', '+13,1%'),
            ('P/E | ROE', '6,38 | 28,6%', 'P/B 1,95')],
  'anh': 'automobile factory',
  'say': 'Chương bốn. Mã V E A có điểm khác lạ. Quý ba, doanh thu thuần chỉ một nghìn hai trăm năm mươi sáu tỷ đồng, nhưng lợi nhuận sau thuế công ty mẹ lại là một nghìn tám trăm '
         'chín mươi ba tỷ, lớn hơn cả doanh thu. Lợi nhuận tăng năm phẩy hai phần trăm, doanh thu tăng mười lăm phẩy hai phần trăm. Lý do là một phần lớn lợi nhuận đến từ thu '
         'nhập của các công ty liên doanh, không nằm trong doanh thu thuần. Mình chỉ dừng ở mức đó, không suy diễn thêm về tỷ giá hay các liên doanh cụ thể. Lũy kế chín tháng năm '
         'nghìn tám trăm bốn mươi chín tỷ, tăng mười ba phẩy một phần trăm. P trên E sáu phẩy ba mươi tám, R O E hai mươi tám phẩy sáu phần trăm.'},
 {'k': 'cards',
  'ch': 'Chương 5 – D H G và P O W',
  'moc': True,
  'label': 'DHG – Quý 3/2026',
  'cap': ('DHG', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Doanh thu thuần', '1.023 tỷ', '−10,7% cùng kỳ'),
            ('LNST công ty mẹ', '98 tỷ', '−53,0% cùng kỳ'),
            ('So với quý 2', '−67,0%', '299 đến 98 tỷ'),
            ('Lũy kế 9 tháng', '713 tỷ', '+0,0%')],
  'anh': 'pharmacy medicine',
  'say': 'Chương năm. D H G, dược phẩm. Về cơ chế chung, doanh nghiệp dược thường nhập một phần nguyên liệu, nên đồng nội tệ mạnh lên có thể giảm chi phí đó. Nhưng kết quả quý ba '
         'của D H G lại yếu. Doanh thu thuần một nghìn không trăm hai mươi ba tỷ đồng, giảm mười phẩy bảy phần trăm. Lợi nhuận chín mươi tám tỷ, giảm năm mươi ba phần trăm so với '
         'cùng kỳ và giảm sáu mươi bảy phần trăm so với quý hai. Lũy kế chín tháng bảy trăm mười ba tỷ, gần như đi ngang. Dữ liệu không nói nguyên nhân; báo cáo gốc sẽ có phần '
         'giải trình. Cổ phiếu tám mươi bảy phẩy ba nghìn đồng, giảm mười phẩy bốn phần trăm sau một năm, P trên E mười ba phẩy ba mươi ba. Nhắc thêm P O W, mới có quý hai: lợi '
         'nhuận ba nghìn ba trăm bảy mươi lăm tỷ, tăng bốn trăm sáu mươi phần trăm. Mình không gán nguyên nhân cho tỷ giá.'},
 {'k': 'bars',
  'ch': 'Chương 6 – So sánh và bài học',
  'moc': True,
  'label': 'Tăng trưởng LNST quý 3/2026 so với cùng kỳ (%)',
  'cap': ('LỢI NHUẬN', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('TNG', 29.5, [34, 197, 94], '+29,5%'), ('VEA', 5.2, [34, 197, 94], '+5,2%'), ('DHG', -53.0, [239, 68, 68], '−53,0%')],
  'anh': 'business growth',
  'say': 'Chương sáu. Đặt cạnh nhau, T N G tăng lợi nhuận hai mươi chín phẩy năm phần trăm, V E A tăng năm phẩy hai phần trăm, còn D H G giảm năm mươi ba phần trăm. Ba kết quả '
         'khác nhau trong cùng một môi trường tỷ giá. Điều đó cho thấy tỷ giá chỉ là một trong nhiều yếu tố. Muốn biết tỷ giá ảnh hưởng bao nhiêu, bạn cần xem tỷ lệ xuất khẩu, '
         'nhập khẩu và vay ngoại tệ trong báo cáo thuyết minh của từng doanh nghiệp.'},
 {'k': 'checklist',
  'label': 'Khi tỷ giá thay đổi, cần hỏi',
  'cap': ('CHECKLIST', 'TỶ GIÁ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Doanh thu xuất khẩu chiếm bao nhiêu?', [56, 189, 248]),
            ('Nguyên liệu nhập khẩu chiếm bao nhiêu?', [34, 197, 94]),
            ('Có nợ vay hoặc tài sản bằng USD không?', [255, 196, 0]),
            ('Lợi nhuận có đến từ nguồn ngoài doanh thu?', [239, 68, 68])],
  'anh': 'financial notes',
  'say': 'Vậy khi tỷ giá thay đổi, bạn có thể hỏi bốn câu. Doanh thu xuất khẩu chiếm bao nhiêu? Nguyên liệu nhập khẩu chiếm bao nhiêu? Doanh nghiệp có nợ vay hoặc tài sản bằng đô '
         'la không? Và lợi nhuận có đến từ những nguồn nằm ngoài doanh thu, như trường hợp V E A không? Bốn câu này giúp bạn tách tác động của tỷ giá khỏi những yếu tố khác.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CHIA SẺ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: dữ liệu thị trường tỷ giá cập nhật ngày hai tháng mười một năm hai nghìn không trăm hai mươi sáu, và báo cáo tài chính của các doanh nghiệp. Đây là chia sẻ kiến '
         'thức, không phải khuyến nghị mua bán. Theo bạn, đồng nội tệ mạnh lên có lợi nhiều hơn hại cho doanh nghiệp Việt không? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0511A'] = [{'k': 'hook',
  'ch': 'Chương 1 – Mở đầu: Fed giữ lãi suất',
  'moc': True,
  'label': 'BMP – Nhựa Bình Minh',
  'cap': ('FED GIỮ LÃI', 'KHỐI NGOẠI?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'BMPW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[7, 180.67, 'Đỉnh tuần 15/12: 180,67', 0.6], [20, 114.64, 'Đáy tuần 23/3: 114,64', 1.6], [51, 138.1, '28/10: 138,10', 2.6]]},
  'anh': 'Federal Reserve building Washington',
  'say': 'Ngày hai mươi chín tháng mười, Fed giữ nguyên lãi suất ở mức từ ba phẩy bảy mươi lăm đến bốn phần trăm. Biểu quyết mười trên hai, và hai thành viên còn muốn tăng thêm '
         'không phẩy hai mươi lăm điểm phần trăm. Vậy khi lãi suất Mỹ còn cao, những cổ phiếu có tỷ lệ sở hữu nước ngoài lớn chịu tác động thế nào? Hôm nay mình đi tìm câu trả '
         'lời bằng số liệu thật của hai doanh nghiệp đứng đầu bảng sở hữu nước ngoài, B M P và S A B. Ở lại đến cuối, vì có một chi tiết trong bảng sở hữu nước ngoài sẽ làm bạn '
         'nhìn lại cách mình hiểu về dòng vốn ngoại.'},
 {'k': 'cards',
  'label': 'Fed ngày 29/10/2026',
  'cap': ('FED ĐÃ LÀM', 'GÌ?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Lãi suất điều hành', '3,75–4,00%', 'giữ nguyên ngày 29/10'),
            ('Biểu quyết', '10–2', '2 người muốn tăng 0,25 điểm'),
            ('Lần chỉnh gần nhất', 'Tăng 0,25 điểm', 'ngày 17/9, từ 3,50–3,75%'),
            ('Họp tiếp theo', '8–9/12', 'công bố ngày 10/12')],
  'anh': 'Federal Reserve interest rate decision',
  'say': 'Trước hết là sự kiện. Fed giữ lãi suất ở mức ba phẩy bảy mươi lăm đến bốn phần trăm. Lần chỉnh gần nhất không phải giảm mà là tăng, tăng không phẩy hai mươi lăm điểm '
         'phần trăm vào ngày mười bảy tháng chín, từ mức ba phẩy năm đến ba phẩy bảy mươi lăm phần trăm. Cuộc họp tiếp theo diễn ra ngày tám và chín tháng mười hai. Đây là những '
         'gì đã xảy ra. Còn tiếp theo thế nào thì không ai biết trước, và video này không dự báo. Câu hỏi của chúng ta chỉ là: khi lãi suất Mỹ ở vùng cao như vậy, cơ chế nào có '
         'thể chạm tới dòng vốn ngoại?'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Cơ chế: lãi suất Mỹ chạm tới cổ phiếu Việt thế nào',
  'moc': True,
  'label': 'Cơ chế chung',
  'cap': 'CƠ CHẾ CHUNG',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Lãi suất Mỹ cao: tài sản an toàn bằng đô la hấp dẫn hơn', [56, 189, 248]),
            ('Đô la mạnh có thể tạo áp lực lên tỷ giá thị trường mới nổi', [255, 196, 0]),
            ('Chi phí vốn toàn cầu cao: đòi hỏi mức sinh lời cao hơn', [255, 196, 0]),
            ('Không có công thức chắc chắn: còn tùy từng doanh nghiệp', [56, 189, 248])],
  'anh': 'global finance dollar currency',
  'say': 'Cơ chế chung thế này. Một, khi lãi suất ở Mỹ cao, gửi tiền vào tài sản bằng đô la có lợi hơn, nên nhà đầu tư toàn cầu thường cân nhắc lại phần vốn đang để ở các thị '
         'trường mới nổi như Việt Nam. Hai, đô la mạnh lên có thể gây áp lực lên tỷ giá. Ba, chi phí vốn trên toàn cầu cao hơn thì mức sinh lời nhà đầu tư đòi hỏi cũng cao hơn. '
         'Đây là cơ chế chung, không phải số liệu riêng của doanh nghiệp nào. Và cần nói rõ: không có công thức nào khẳng định lãi suất Mỹ tăng thì khối ngoại chắc chắn bán.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Ai đang có tỷ lệ sở hữu nước ngoài cao nhất?',
  'moc': True,
  'label': 'Tỷ lệ sở hữu nước ngoài',
  'cap': 'SỞ HỮU NƯỚC NGOÀI',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('BMP', 82.0, [255, 196, 0], '82,0%'),
           ('SAB', 58.8, [255, 196, 0], '58,8%'),
           ('DHG', 54.0, [56, 189, 248], '54,0%'),
           ('VNM', 49.7, [56, 189, 248], '49,7%'),
           ('MWG', 49.0, [56, 189, 248], '49,0%'),
           ('REE', 48.9, [56, 189, 248], '48,9%')],
  'anh': 'foreign investors stock market',
  'say': 'Giờ đến bảng sở hữu nước ngoài trong dữ liệu. B M P đứng đầu với tám mươi hai phần trăm, S A B năm mươi tám phẩy tám phần trăm, D H G năm mươi tư phần trăm, V N M bốn '
         'mươi chín phẩy bảy, M W G bốn mươi chín và R E E bốn mươi tám phẩy chín phần trăm. Hôm nay mình soi kỹ hai cái tên đầu bảng. Bốn mã còn lại chỉ đứng trong bảng để so '
         'sánh. Và lưu ý quan trọng: đây là tỷ lệ đang nắm giữ, nó không cho biết khối ngoại đang mua hay đang bán.'},
 {'k': 'cards',
  'ch': 'Chương 4 – B M P: tỷ lệ nước ngoài cao nhất bảng',
  'moc': True,
  'label': 'BMP – Nhựa Bình Minh',
  'cap': 'BMP QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '319 tỷ', '−8,9% so với cùng kỳ'),
            ('Lũy kế 9 tháng', '990 tỷ', '+2,4%'),
            ('Doanh thu thuần', '1.463 tỷ', '−4,5%'),
            ('Biên lợi nhuận gộp', '40,3%', 'cùng kỳ 47,9%'),
            ('P/E · ROE', '8,99 · 41,1%', 'sở hữu nước ngoài 82%')],
  'anh': 'plastic pipes factory',
  'say': 'Bắt đầu với B M P, công ty có tỷ lệ sở hữu nước ngoài cao nhất bảng. Quý ba năm hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế công ty mẹ là ba trăm mười chín tỷ '
         'đồng, giảm tám phẩy chín phần trăm so với cùng kỳ. Doanh thu thuần một nghìn bốn trăm sáu mươi ba tỷ, giảm bốn phẩy năm phần trăm. Biên lợi nhuận gộp còn bốn mươi phẩy '
         'ba phần trăm, so với bốn mươi bảy phẩy chín phần trăm cùng kỳ. Nghĩa là phần thu hẹp nằm ở biên lợi nhuận, không chỉ ở doanh thu. Nguyên nhân cụ thể thì báo cáo gốc có '
         'phần giải trình. Tính chung chín tháng, lợi nhuận vẫn đạt chín trăm chín mươi tỷ, tăng hai phẩy bốn phần trăm.'},
 {'k': 'bars',
  'label': 'BMP – LNST theo quý (tỷ đồng)',
  'cap': 'BMP 8 QUÝ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q4/24', 231, [56, 189, 248], '231'),
           ('Q1/25', 287, [56, 189, 248], '287'),
           ('Q2/25', 330, [56, 189, 248], '330'),
           ('Q3/25', 351, [56, 189, 248], '351'),
           ('Q4/25', 261, [56, 189, 248], '261'),
           ('Q1/26', 304, [56, 189, 248], '304'),
           ('Q2/26', 367, [34, 197, 94], '367'),
           ('Q3/26', 319, [255, 196, 0], '319')],
  'anh': 'plastic pipe production',
  'say': 'Nhìn chuỗi tám quý, lợi nhuận B M P dao động từ hai trăm ba mươi mốt đến ba trăm sáu mươi bảy tỷ đồng, đỉnh là quý hai năm nay. Quý ba lùi về ba trăm mười chín tỷ, thấp '
         'hơn ba trăm năm mươi mốt tỷ của cùng kỳ. Đến ngày hai mươi tám tháng mười, cổ phiếu ở một trăm ba mươi tám phẩy một nghìn đồng, thấp hơn một năm trước mười phẩy sáu '
         'phần trăm. Đây là chi tiết đáng nghĩ: sở hữu nước ngoài tám mươi hai phần trăm, nhưng giá một năm vẫn giảm. P trên E tám phẩy chín mươi chín, ROE bốn mươi mốt phẩy một '
         'phần trăm chỉ là mô tả quá khứ.'},
 {'k': 'cards',
  'ch': 'Chương 5 – S A B: doanh thu nhích, lợi nhuận lùi',
  'moc': True,
  'label': 'SAB – Sabeco',
  'cap': 'SAB QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '1.232 tỷ', '−9,4% so với cùng kỳ'),
            ('Lũy kế 9 tháng', '3.584 tỷ', '+6,6%'),
            ('Doanh thu thuần', '6.684 tỷ', '+3,8%'),
            ('Giá 28/10', '42,90', '1 năm +5,2%'),
            ('P/E · ROE', '11,7 · 20,1%', 'sở hữu nước ngoài 58,8%')],
  'anh': 'beer brewery bottles',
  'say': 'Sang S A B, tỷ lệ sở hữu nước ngoài năm mươi tám phẩy tám phần trăm. Quý ba, lợi nhuận sau thuế công ty mẹ là một nghìn hai trăm ba mươi hai tỷ đồng, giảm chín phẩy bốn '
         'phần trăm so với cùng kỳ, trong khi doanh thu thuần tăng ba phẩy tám phần trăm lên sáu nghìn sáu trăm tám mươi bốn tỷ. Doanh thu nhích lên còn lợi nhuận lùi lại, điều '
         'này cho thấy chi phí hoặc biên lợi nhuận đã thay đổi, nhưng nguyên nhân cụ thể cần xem báo cáo gốc. Chín tháng đầu năm lợi nhuận vẫn đạt ba nghìn năm trăm tám mươi bốn '
         'tỷ, tăng sáu phẩy sáu phần trăm.'},
 {'k': 'bars',
  'ch': 'Chương 6 – Tổng kết: giá và lợi nhuận đi cùng nhau không?',
  'moc': True,
  'label': 'Giá cổ phiếu 1 năm (%)',
  'cap': 'GIÁ 1 NĂM',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('BMP', -10.6, [239, 68, 68], '−10,6%'),
           ('SAB', 5.2, [34, 197, 94], '+5,2%'),
           ('VNM', 4.7, [34, 197, 94], '+4,7%'),
           ('DHG', -10.4, [239, 68, 68], '−10,4%'),
           ('MWG', -7.1, [239, 68, 68], '−7,1%'),
           ('REE', -14.8, [239, 68, 68], '−14,8%')],
  'anh': 'stock price chart',
  'say': 'Nhìn cả bảng sáu mã, giá một năm đến ngày hai mươi tám tháng mười: B M P giảm mười phẩy sáu phần trăm, S A B tăng năm phẩy hai, V N M tăng bốn phẩy bảy, D H G giảm mười '
         'phẩy bốn, M W G giảm bảy phẩy một và R E E giảm mười bốn phẩy tám phần trăm. Trong khi đó lợi nhuận quý ba cũng khác nhau: V N M tăng mười bảy phẩy ba phần trăm, M W G '
         'tăng bảy mươi bốn phẩy bảy, còn D H G giảm năm mươi ba phần trăm. Tức là giá và lợi nhuận mỗi mã đi một hướng riêng. Tỷ lệ sở hữu nước ngoài cao không tự động nghĩa là '
         'giá giảm hay tăng khi lãi suất Mỹ thay đổi.'},
 {'k': 'checklist',
  'label': 'Nhìn gì khi lãi suất Mỹ cao',
  'cap': 'CẦN NHÌN GÌ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Lãi suất và tỷ giá: biến số nền, không phải kết luận', [56, 189, 248]),
            ('Lợi nhuận quý của chính doanh nghiệp', [34, 197, 94]),
            ('Biên lợi nhuận gộp: thu hẹp hay cải thiện', [255, 196, 0]),
            ('Giá 1 năm và P/E chỉ là mô tả quá khứ', [56, 189, 248])],
  'anh': 'investor analyzing financial report',
  'say': 'Tóm lại, khi lãi suất Mỹ ở vùng cao, bạn nên nhìn những gì? Một, xem lãi suất và tỷ giá như biến số nền, không phải kết luận. Hai, xem lợi nhuận quý của chính doanh '
         'nghiệp. Ba, xem biên lợi nhuận gộp đang thu hẹp hay cải thiện. Bốn, giá một năm và P trên E chỉ là mô tả quá khứ. Và nhớ rằng video này không khẳng định khối ngoại đã '
         'mua hay đã bán, vì dữ liệu ở đây không cho biết điều đó.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN: FED, CỤC', 'THỐNG KÊ, BCTC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu: Fed, báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của các doanh nghiệp và dữ liệu giá của kênh. Đây là chia sẻ kiến thức, không phải '
         'khuyến nghị mua bán. Câu hỏi cho bạn: theo bạn, tỷ lệ sở hữu nước ngoài cao là điểm mạnh hay điểm cần lưu ý? Hãy để lại bình luận. Xem thêm tại chungkhoanhuynguyen chấm '
         'com.'}]

S['Y3_0511B'] = [{'k': 'hook',
  'ch': 'Chương 1 – Mở đầu: lãi suất không rủi ro',
  'moc': True,
  'label': 'BID – BIDV',
  'cap': ('LỢI SUẤT MỸ', 'VS NGÂN HÀNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'BIDW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[12, 52.37, 'Đỉnh tuần 19/1: 52,37', 0.6], [38, 32.15, 'Đáy tuần 27/7: 32,15', 1.6], [51, 33.65, '28/10: 33,65', 2.6]]},
  'anh': 'US treasury bond securities',
  'say': 'Lợi suất trái phiếu Mỹ kỳ hạn mười năm là bốn phẩy chín hai chín phần trăm ngày ba mươi tháng mười, mức lãi gần như không rủi ro. Nếu so với mức lợi nhuận mà năm ngân '
         'hàng lớn tạo ra trên giá cổ phiếu, khoảng cách rộng hay hẹp? Đây là phép so sánh minh họa, không phải định giá đúng sai. Video đi sâu V C B, B I D và M B B, còn T C B '
         'và V P B nằm trong bảng. Ở lại đến cuối để xem ngân hàng nào có khoảng cách hẹp nhất.'},
 {'k': 'cards',
  'label': 'Lợi suất trái phiếu Mỹ 10 năm',
  'cap': 'LỢI SUẤT MỸ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Hiện tại', '4,929%', 'ngày 30/10/2026'),
            ('Đỉnh 1 năm', '5,311%', 'ngày 5/10/2026'),
            ('Thấp nhất 1 năm', '3,962%', 'ngày 27/2/2026'),
            ('Tháng 9/2026', '5,29%', 'cuối tháng')],
  'anh': 'bond market yield chart',
  'say': 'Trước hết là mốc so sánh. Lợi suất trái phiếu Mỹ mười năm hiện là bốn phẩy chín hai chín phần trăm. Đỉnh một năm là năm phẩy ba một một phần trăm ngày năm tháng mười, '
         'và thấp nhất một năm là ba phẩy chín sáu hai phần trăm ngày hai mươi bảy tháng hai. Chênh lệch giữa mức hiện tại và đáy một năm gần một điểm phần trăm, chính xác là '
         'không phẩy chín mươi bảy điểm. Cuối tháng chín lợi suất ở mức năm phẩy hai mươi chín phần trăm. Mình dùng mức bốn phẩy chín hai chín làm thước đo chính, và chỉ mô tả, '
         'không dự báo lợi suất sẽ đi đâu.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Cách tính: lợi suất lợi nhuận là gì?',
  'moc': True,
  'label': 'Lợi suất lợi nhuận',
  'cap': 'PHÉP SO SÁNH',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Lợi suất lợi nhuận = 1 chia P/E', [255, 196, 0]),
            ('Ví dụ P/E 10 thì lợi suất lợi nhuận là 10%', [56, 189, 248]),
            ('Phần bù = lợi suất lợi nhuận trừ 4,929%', [255, 196, 0]),
            ('Chỉ là phép tính minh họa, không định giá đúng sai', [239, 68, 68])],
  'anh': 'calculator financial analysis',
  'say': 'Phép so sánh hôm nay rất đơn giản. Lấy một chia cho P trên E. Ví dụ P trên E bằng mười thì mỗi một đồng giá cổ phiếu tương ứng mười phần trăm lợi nhuận một năm. Mình '
         'gọi là lợi suất lợi nhuận. Sau đó trừ đi lãi suất không rủi ro là bốn phẩy chín hai chín phần trăm, ra phần bù. Nhưng đây là phép tính minh họa của kênh từ P trên E '
         'trong gói dữ liệu, không phải kết luận cổ phiếu rẻ hay đắt.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Năm ngân hàng đặt cạnh lãi suất Mỹ',
  'moc': True,
  'label': 'Lợi suất lợi nhuận (1/PE) so với TP Mỹ',
  'cap': 'LỢI SUẤT LN',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('TP Mỹ 10 năm', 4.929, [56, 189, 248], '4,93%'),
           ('VCB', 8.86, [255, 196, 0], '8,86%'),
           ('BID', 12.42, [255, 196, 0], '12,42%'),
           ('MBB', 16.75, [255, 196, 0], '16,75%'),
           ('TCB', 12.47, [255, 196, 0], '12,47%'),
           ('VPB', 13.59, [255, 196, 0], '13,59%')],
  'anh': 'bank building skyline',
  'say': 'Áp vào số liệu. V C B có P trên E mười một phẩy hai mươi chín, lợi suất lợi nhuận khoảng tám phẩy tám mươi sáu phần trăm. B I D P trên E tám phẩy không năm, tương ứng '
         'mười hai phẩy bốn mươi hai phần trăm. M B B P trên E năm phẩy chín mươi bảy, tương ứng mười sáu phẩy bảy mươi lăm phần trăm. T C B P trên E tám phẩy không hai, tương '
         'ứng mười hai phẩy bốn mươi bảy phần trăm. V P B P trên E bảy phẩy ba mươi sáu, tương ứng mười ba phẩy năm mươi chín phần trăm. Cả năm đều cao hơn mốc bốn phẩy chín hai '
         'chín phần trăm của trái phiếu Mỹ.'},
 {'k': 'bars',
  'label': 'Phần bù so với TP Mỹ 4,929% (điểm %)',
  'cap': 'PHẦN BÙ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('VCB', 3.93, [255, 196, 0], '3,93'),
           ('BID', 7.49, [255, 196, 0], '7,49'),
           ('TCB', 7.54, [255, 196, 0], '7,54'),
           ('VPB', 8.66, [255, 196, 0], '8,66'),
           ('MBB', 11.82, [34, 197, 94], '11,82')],
  'anh': 'bank branch Vietnam',
  'say': 'Phần bù thì sao? V C B hẹp nhất, khoảng ba phẩy chín mươi ba điểm phần trăm. B I D khoảng bảy phẩy bốn mươi chín, T C B bảy phẩy năm mươi bốn, V P B tám phẩy sáu mươi '
         'sáu và M B B rộng nhất, khoảng mười một phẩy tám mươi hai điểm. Vậy rộng hay hẹp? Trung thực là: mình chỉ so được giữa các ngân hàng với nhau, vì không có chuỗi lịch sử '
         'để nói rộng hơn hay hẹp hơn bình thường. Nếu lợi suất Mỹ ở đáy một năm ba phẩy chín sáu hai phần trăm thì phần bù V C B là bốn phẩy chín điểm, còn ở đỉnh năm phẩy ba '
         'một một phần trăm là ba phẩy năm mươi lăm điểm.'},
 {'k': 'cards',
  'ch': 'Chương 4 – V C B: phần bù hẹp nhất',
  'moc': True,
  'label': 'VCB – Vietcombank',
  'cap': 'VCB QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '9.033 tỷ', '+0,1% so với cùng kỳ'),
            ('Lũy kế 9 tháng', '33.032 tỷ', '+24,4%'),
            ('Thu nhập lãi thuần', '20.386 tỷ', '+39,1%'),
            ('Nợ xấu · bao phủ', '0,71% · 243%', 'bộ đệm dự phòng dày'),
            ('P/E · ROE', '11,29 · 17,6%', 'giá 1 năm −3,4%')],
  'anh': 'Vietcombank headquarters',
  'say': 'V C B là ngân hàng có phần bù hẹp nhất. Quý ba, lợi nhuận sau thuế công ty mẹ chín nghìn không trăm ba mươi ba tỷ đồng, chỉ tăng không phẩy một phần trăm so với cùng '
         'kỳ, dù thu nhập lãi thuần tăng ba mươi chín phẩy một phần trăm. So với quý hai là mười bốn nghìn năm trăm bốn mươi hai tỷ, lợi nhuận giảm ba mươi bảy phẩy chín phần '
         'trăm, và chi phí dự phòng tăng sáu trăm chín mươi bảy phẩy ba phần trăm. Báo cáo gốc có phần giải trình cho biến động này. Tỷ lệ nợ xấu không phẩy bảy mươi mốt phần '
         'trăm, bao phủ nợ xấu khoảng hai trăm bốn mươi ba phần trăm.'},
 {'k': 'cards',
  'ch': 'Chương 5 – B I D, M B B và hai cái tên trong bảng',
  'moc': True,
  'label': 'BID – BIDV',
  'cap': 'BID QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '8.331 tỷ', '+39,9% so với cùng kỳ'),
            ('Lũy kế 9 tháng', '23.278 tỷ', '+25,5%'),
            ('Thu nhập lãi thuần', '17.056 tỷ', '+12,4%'),
            ('Chi phí dự phòng', '−25,0%', 'trích lập ít hơn'),
            ('P/E · ROE', '8,05 · 18,0%', 'giá 1 năm −2,0%')],
  'anh': 'BIDV bank building',
  'say': 'Tiếp theo là B I D. Quý ba lợi nhuận sau thuế công ty mẹ tám nghìn ba trăm ba mươi mốt tỷ đồng, tăng ba mươi chín phẩy chín phần trăm so với cùng kỳ, trong khi thu nhập '
         'lãi thuần tăng mười hai phẩy bốn phần trăm lên mười bảy nghìn không trăm năm mươi sáu tỷ. Lợi nhuận tăng nhanh hơn thu nhập lãi vì chi phí dự phòng giảm hai mươi lăm '
         'phần trăm, nghĩa là một phần lợi nhuận tăng nhờ trích lập ít hơn. P trên E tám phẩy không năm cho lợi suất lợi nhuận khoảng mười hai phẩy bốn mươi hai phần trăm, ROE '
         'mười tám phần trăm.'},
 {'k': 'cards',
  'label': 'MBB – MB Bank',
  'cap': 'MBB QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '8.039 tỷ', '+44,3% so với cùng kỳ'),
            ('Thu nhập lãi thuần', '17.836 tỷ', '+37,3%'),
            ('NIM', 'khoảng 3,72%', 'lãi dịch vụ +26,5%'),
            ('Lũy kế 9 tháng', '23.784 tỷ', '+32,0%'),
            ('P/E · ROE', '5,97 · 21,8%', 'giá 1 năm +2,5%')],
  'anh': 'MB Bank headquarters',
  'say': 'M B B là ngân hàng có phần bù rộng nhất. P trên E chỉ năm phẩy chín mươi bảy trong khi ROE hai mươi mốt phẩy tám phần trăm. Lợi nhuận quý ba tám nghìn không trăm ba '
         'mươi chín tỷ đồng, tăng bốn mươi bốn phẩy ba phần trăm so với cùng kỳ, và thu nhập lãi thuần tăng ba mươi bảy phẩy ba phần trăm lên mười bảy nghìn tám trăm ba mươi sáu '
         'tỷ. Chín tháng lợi nhuận đạt hai mươi ba nghìn bảy trăm tám mươi bốn tỷ, tăng ba mươi hai phần trăm. Giá một năm đến ngày hai mươi tám tháng mười cao hơn hai phẩy năm '
         'phần trăm.'},
 {'k': 'cards',
  'ch': 'Chương 6 – Giới hạn của phép so sánh',
  'moc': True,
  'label': 'Bối cảnh trong nước (NHNN)',
  'cap': 'TRONG NƯỚC',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Lãi suất tiền gửi bình quân', '6,38%/năm', '20/9; +1,15 điểm so với cuối 2025'),
            ('Tín dụng toàn hệ thống', '+11,59%', 'so với cuối 2025, đến 30/9'),
            ('Tín dụng so với cùng kỳ', '+16,69%', 'khoảng 20,75 triệu tỷ đồng'),
            ('Lãi suất điều hành', 'Giữ nguyên', 'theo NHNN')],
  'anh': 'Vietnam State Bank building',
  'say': 'Còn trong nước, theo Ngân hàng Nhà nước, lãi suất tiền gửi bình quân giao dịch mới là sáu phẩy ba mươi tám phần trăm một năm, số liệu ngày hai mươi tháng chín, tăng một '
         'phẩy mười lăm điểm phần trăm so với cuối năm hai nghìn không trăm hai mươi lăm. Ngân hàng Nhà nước giữ nguyên lãi suất điều hành. Dư nợ tín dụng đến cuối tháng chín '
         'tăng mười sáu phẩy sáu mươi chín phần trăm so với cùng kỳ. Chi phí vốn trong và ngoài nước đều là yếu tố nền của lợi nhuận ngân hàng.'},
 {'k': 'checklist',
  'label': 'Giới hạn của phép so sánh',
  'cap': 'GIỚI HẠN',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Trái phiếu Mỹ tính bằng đô la, ngân hàng Việt tính bằng đồng', [239, 68, 68]),
            ('P/E dựa trên lợi nhuận quá khứ, có thể có khoản bất thường', [255, 196, 0]),
            ('Chất lượng tài sản khác nhau: nợ xấu, bao phủ nợ xấu', [255, 196, 0]),
            ('Đây là minh họa, không phải định giá đúng/sai', [56, 189, 248])],
  'anh': 'analyst reviewing charts',
  'say': 'Cuối cùng là giới hạn. Một, trái phiếu Mỹ tính bằng đô la còn ngân hàng Việt tính bằng đồng, hai đồng tiền không so trực tiếp được. Hai, P trên E dựa trên lợi nhuận quá '
         'khứ, mà lợi nhuận có thể có biến động một lần, như quý hai của V C B. Ba, chất lượng tài sản mỗi ngân hàng khác nhau, nhìn nợ xấu và bao phủ nợ xấu. Bốn, đây là phép '
         'minh họa, không phải kết luận ngân hàng nào đúng giá hay sai giá.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN: BCTC,', 'FED, NHNN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu: báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu, dữ liệu lợi suất trái phiếu Mỹ của kênh, và Ngân hàng Nhà nước. Đây là chia sẻ kiến thức, '
         'không phải khuyến nghị mua bán. Câu hỏi cho bạn: khi so cổ phiếu với lãi suất không rủi ro, bạn thấy cần thêm yếu tố nào? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0511C'] = [{'k': 'hook',
  'ch': 'Chương 1 – Mở đầu: vàng giảm, ai lo?',
  'moc': True,
  'label': 'PNJ – vàng trang sức',
  'cap': ('VÀNG GIẢM', 'PNJ LỖ?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'PNJW', 'tf': 'W', 'weeks': 52, 'circles': [[13, 84.67, 'Đỉnh tuần 26/1: 84,67', 0.6], [51, 17.15, '28/10: 17,15', 1.6]]},
  'anh': 'gold jewelry shop',
  'say': 'Vàng thế giới đang ở ba nghìn chín trăm linh bốn phẩy tám đô la một ounce, thấp hơn đỉnh năm hai nghìn không trăm hai mươi sáu khoảng hai mươi sáu phẩy sáu phần trăm. '
         'Nhiều người nghĩ vàng giảm thì người bán vàng trang sức lợi hơn hoặc ít nhất đỡ lo. Nhưng nhìn tám quý gần nhất của P N J, bạn sẽ thấy câu chuyện không đơn giản như '
         'vậy. Hôm nay mình đào sâu chuỗi tám quý, từ lãi lớn sang lỗ, để trả lời: giá vàng tác động hai chiều lên doanh nghiệp ra sao, và vì sao giảm không phải lúc nào cũng '
         'tốt.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Giá vàng đã đi đâu?',
  'moc': True,
  'label': 'Giá vàng thế giới',
  'cap': 'VÀNG THẾ GIỚI',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Giá hiện tại', '3.904,8', 'đô la/ounce, 2/11/2026'),
            ('Đỉnh 1 năm', '5.318,4', 'ngày 29/1/2026'),
            ('Giảm từ đỉnh', '−26,6%', 'phép tính của kênh'),
            ('1 tháng', '−6,2%', '3 tháng −6,0%'),
            ('2 năm', '+42,0%', '1 năm −2,3%')],
  'anh': 'gold bars bullion',
  'say': 'Trước hết là giá vàng. Ngày hai tháng mười một, vàng thế giới ở ba nghìn chín trăm linh bốn phẩy tám đô la một ounce. Đỉnh một năm là năm nghìn ba trăm mười tám phẩy '
         'bốn đô la ngày hai mươi chín tháng một năm hai nghìn không trăm hai mươi sáu, nghĩa là hiện giảm khoảng hai mươi sáu phẩy sáu phần trăm từ đỉnh. Một tháng qua giảm sáu '
         'phẩy hai phần trăm, ba tháng giảm sáu phần trăm, một năm giảm hai phẩy ba phần trăm. Nhưng nhìn dài hơn, hai năm vàng vẫn cao hơn bốn mươi hai phần trăm. Đây chỉ là mô '
         'tả, mình không dự báo vàng đi đâu.'},
 {'k': 'bars',
  'label': 'Giá vàng cuối tháng (USD/ounce)',
  'cap': 'ĐƯỜNG GIÁ VÀNG',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('11/25', 4009.8, [56, 189, 248], '4.009,8'),
           ('01/26', 4496.1, [56, 189, 248], '4.496,1'),
           ('03/26', 5158.7, [255, 196, 0], '5.158,7'),
           ('05/26', 4710.9, [56, 189, 248], '4.710,9'),
           ('07/26', 4167.5, [56, 189, 248], '4.167,5'),
           ('09/26', 4476.6, [56, 189, 248], '4.476,6'),
           ('10/26', 4162.3, [56, 189, 248], '4.162,3'),
           ('2/11', 3904.8, [239, 68, 68], '3.904,8')],
  'anh': 'gold price chart',
  'say': 'Đường đi giá vàng cuối tháng: tháng mười một năm ngoái bốn nghìn không trăm linh chín phẩy tám đô la, tháng một bốn nghìn bốn trăm chín mươi sáu phẩy một, tháng ba năm '
         'nghìn một trăm năm mươi tám phẩy bảy, tháng năm bốn nghìn bảy trăm mười phẩy chín, tháng bảy bốn nghìn một trăm sáu mươi bảy phẩy năm, tháng mười bốn nghìn một trăm sáu '
         'mươi hai phẩy ba và hôm nay ba nghìn chín trăm linh bốn phẩy tám. Đỉnh thật sự là năm nghìn ba trăm mười tám phẩy bốn ngày hai mươi chín tháng một, nằm ngay trong quý '
         'một. Hãy nhớ mốc này, vì quý một cũng là quý P N J ghi nhận con số lớn nhất chuỗi.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Cơ chế: vàng tác động hai chiều',
  'moc': True,
  'label': 'Cơ chế hai chiều',
  'cap': 'HAI CHIỀU',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Vàng tăng: doanh thu danh nghĩa tăng, hàng tồn kho giá thấp có lợi', [34, 197, 94]),
            ('Vàng giảm: hàng đã mua giá cao có thể thu hẹp biên', [239, 68, 68]),
            ('Vàng giảm sâu: khách có thể mua nhiều hơn hoặc chờ thêm', [255, 196, 0]),
            ('Mua vàng nguyên liệu giá rẻ hơn cần ít vốn lưu động hơn', [56, 189, 248])],
  'anh': 'jewelry workshop craftsman',
  'say': 'Cơ chế chung có hai chiều. Khi vàng tăng, doanh thu tính theo giá tăng, và phần hàng mua từ trước ở giá thấp thường có lợi. Khi vàng giảm, hàng đã mua ở giá cao có thể '
         'làm biên lợi nhuận thu hẹp. Ngược lại, vàng rẻ hơn thì mua nguyên liệu cần ít tiền hơn, tức vốn lưu động nhẹ hơn, và khách hàng có thể mua nhiều hơn hoặc chờ giá giảm '
         'thêm. Đó là cơ chế chung. Còn việc chi tiết kết quả của P N J do yếu tố nào thì báo cáo gốc có phần giải trình, mình không đoán.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Chuỗi tám quý của P N J',
  'moc': True,
  'label': 'PNJ – LNST theo quý (tỷ đồng)',
  'cap': 'PNJ 8 QUÝ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q4/24', 731, [56, 189, 248], '731'),
           ('Q1/25', 678, [56, 189, 248], '678'),
           ('Q2/25', 437, [56, 189, 248], '437'),
           ('Q3/25', 496, [56, 189, 248], '496'),
           ('Q4/25', 1218, [34, 197, 94], '1.218'),
           ('Q1/26', 1467, [34, 197, 94], '1.467'),
           ('Q2/26', -739, [239, 68, 68], '−739'),
           ('Q3/26', -257, [239, 68, 68], '−257')],
  'anh': 'financial report profit loss',
  'say': 'Giờ đến chuỗi tám quý của P N J. Lợi nhuận sau thuế công ty mẹ đi từ bảy trăm ba mươi mốt tỷ quý bốn năm hai nghìn không trăm hai mươi bốn, sáu trăm bảy mươi tám, bốn '
         'trăm ba mươi bảy và bốn trăm chín mươi sáu tỷ quý ba năm ngoái. Rồi nhảy lên một nghìn hai trăm mười tám tỷ quý bốn và một nghìn bốn trăm sáu mươi bảy tỷ quý một năm '
         'nay, cao nhất chuỗi. Sau đó đảo chiều: quý hai lỗ bảy trăm ba mươi chín tỷ, quý ba lỗ hai trăm năm mươi bảy tỷ. Chín tháng, lợi nhuận còn bốn trăm bảy mươi hai tỷ, giảm '
         'bảy mươi phẩy bảy phần trăm so với cùng kỳ. Dữ liệu cho thấy chuỗi lãi lớn rồi lỗ liên tiếp hai quý.'},
 {'k': 'bars',
  'label': 'PNJ – doanh thu thuần theo quý (tỷ đồng)',
  'cap': 'DOANH THU',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q4/24', 8581, [56, 189, 248], '8.581'),
           ('Q1/25', 9635, [56, 189, 248], '9.635'),
           ('Q2/25', 7582, [56, 189, 248], '7.582'),
           ('Q3/25', 8136, [56, 189, 248], '8.136'),
           ('Q4/25', 9623, [56, 189, 248], '9.623'),
           ('Q1/26', 17245, [255, 196, 0], '17.245'),
           ('Q2/26', 8464, [56, 189, 248], '8.464'),
           ('Q3/26', 6995, [239, 68, 68], '6.995')],
  'anh': 'retail jewelry store counter',
  'say': 'Doanh thu kể một phần câu chuyện. Quý bốn năm ngoái chín nghìn sáu trăm hai mươi ba tỷ, rồi quý một năm nay bật lên mười bảy nghìn hai trăm bốn mươi lăm tỷ, gần gấp '
         'đôi, đúng quý vàng thế giới chạm đỉnh. Sau đó quý hai còn tám nghìn bốn trăm sáu mươi bốn tỷ và quý ba chỉ sáu nghìn chín trăm chín mươi lăm tỷ, giảm mười bốn phần trăm '
         'so với cùng kỳ, thấp nhất trong cả tám quý. Mình chỉ nêu sự trùng thời điểm, không khẳng định nguyên nhân. Điều đáng chú ý là doanh thu quý một cao đột biến nhưng lợi '
         'nhuận quý hai và quý ba lại đảo chiều thành lỗ.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Quý 3 lỗ và biên gộp thu hẹp',
  'moc': True,
  'label': 'PNJ quý 3/2026',
  'cap': 'PNJ QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '−257 tỷ', 'cùng kỳ: lãi 496 tỷ'),
            ('Doanh thu thuần', '6.995 tỷ', '−14,0% so với cùng kỳ'),
            ('Biên lợi nhuận gộp', '8,7%', 'cùng kỳ 19,8%'),
            ('Quý 2/2026', '−739 tỷ', 'lỗ lớn nhất chuỗi'),
            ('Lũy kế 9 tháng', '472 tỷ', '−70,7%')],
  'anh': 'jewelry gold necklace display',
  'say': 'Đi sâu quý ba. Lợi nhuận sau thuế công ty mẹ lỗ hai trăm năm mươi bảy tỷ đồng, trong khi cùng kỳ năm ngoái lãi bốn trăm chín mươi sáu tỷ. Biên lợi nhuận gộp chỉ còn tám '
         'phẩy bảy phần trăm, so với mười chín phẩy tám phần trăm cùng kỳ, nghĩa là mỗi một trăm đồng doanh thu chỉ còn khoảng tám phẩy bảy đồng lợi nhuận gộp. Đây là điểm mấu '
         'chốt. Doanh thu giảm mười bốn phần trăm đã đau, nhưng biên gộp thu hẹp hơn một nửa mới là phần nặng. Lý do cụ thể phải đọc phần giải trình của báo cáo gốc.'},
 {'k': 'cards',
  'label': 'PNJ – giá và định giá',
  'cap': 'PNJ GIÁ CP',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Giá 28/10', '17,15', 'nghìn đồng'),
            ('1 năm', '−72,6%', '3 tháng −47,6%'),
            ('1 tháng', '−44,1%', 'thấp nhất 1 năm 17,05'),
            ('Đỉnh 1 năm', '84,67', 'ngày 30/1/2026'),
            ('P/E · P/B', '3,25 · 0,6', 'ROE 12,7%')],
  'anh': 'stock market decline red',
  'say': 'Giá cổ phiếu phản ánh điều đó. Đến ngày hai mươi tám tháng mười, P N J ở mười bảy phẩy mười lăm nghìn đồng, giảm bảy mươi hai phẩy sáu phần trăm trong một năm và bốn '
         'mươi bốn phẩy một phần trăm chỉ trong một tháng. Đỉnh một năm là tám mươi bốn phẩy sáu mươi bảy nghìn đồng ngày ba mươi tháng một, chỉ sau một ngày vàng đạt đỉnh. P '
         'trên E ba phẩy hai mươi lăm và P trên B không phẩy sáu nhìn rất thấp, nhưng đó là con số tính trên lợi nhuận quá khứ, trong khi hai quý gần nhất đang lỗ. Vì vậy P trên '
         'E thấp không tự động có nghĩa là rẻ.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Giảm là tốt hay xấu cho dòng tiền?',
  'moc': True,
  'label': 'Vàng giảm có phải là tốt?',
  'cap': 'GIẢM = TỐT?',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Vàng giảm giúp mua nguyên liệu rẻ hơn, nhẹ vốn lưu động', [34, 197, 94]),
            ('Nhưng hàng tồn mua giá cao có thể kéo biên gộp xuống', [239, 68, 68]),
            ('Doanh thu giảm khi giá giảm, nên lợi nhuận hai đầu bị ép', [255, 196, 0]),
            ('Dòng tiền tốt chưa chắc đi cùng lợi nhuận tốt', [56, 189, 248])],
  'anh': 'cash flow business finance',
  'say': "Vậy 'vàng giảm là tốt cho dòng tiền' đúng đến đâu? Đúng một phần. Mua nguyên liệu rẻ hơn thì cần ít tiền hơn, nhẹ vốn lưu động, nên dòng tiền có thể dễ thở. Nhưng lợi "
         'nhuận kế toán lại tính trên giá vốn của hàng đã mua, và giá bán thì giảm theo thị trường. Hai thứ này lệch nhịp nên biên gộp có thể bị ép, như con số tám phẩy bảy phần '
         'trăm của P N J quý ba. Vì thế dòng tiền tốt chưa chắc đi cùng lợi nhuận tốt. Dữ liệu trong video không đủ để nói P N J cụ thể thuộc trường hợp nào, đó là việc của báo '
         'cáo gốc.'},
 {'k': 'checklist',
  'label': 'Theo dõi gì ở doanh nghiệp vàng',
  'cap': 'THEO DÕI',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Biên lợi nhuận gộp qua từng quý', [255, 196, 0]),
            ('Doanh thu: so với cùng kỳ và so với quý trước', [56, 189, 248]),
            ('Giải trình lãi/lỗ trong báo cáo gốc', [34, 197, 94]),
            ('Giá vàng chỉ là một biến số, không phải tất cả', [56, 189, 248])],
  'anh': 'investor reading report',
  'say': 'Tóm lại, khi nhìn doanh nghiệp bán vàng, bạn có thể theo dõi bốn thứ. Biên lợi nhuận gộp qua từng quý. Doanh thu so với cùng kỳ và so với quý trước. Phần giải trình lãi '
         'lỗ trong báo cáo gốc. Và nhớ rằng giá vàng chỉ là một biến số. Những doanh nghiệp khác như D G W hay S S I cũng có chuỗi riêng, nhưng hôm nay mình dành thời gian cho P '
         'N J.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN: BCTC,', 'DỮ LIỆU GIÁ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu: báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của P N J và dữ liệu giá vàng thế giới của kênh. Đây là chia sẻ kiến thức, không phải '
         'khuyến nghị mua bán. Câu hỏi cho bạn: theo bạn, doanh nghiệp vàng nên được đánh giá bằng lợi nhuận hay bằng dòng tiền? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

if __name__ == "__main__":
    for k, sc in S.items():
        n = sum(len(s["say"].split()) for s in sc)
        print(k, "số từ:", n, "· phút ≈", round(n / 170, 1))
