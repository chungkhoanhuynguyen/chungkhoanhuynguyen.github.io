# -*- coding: utf-8 -*-
# Đợt 2: ngày 6/11–9/11/2026 (12 video).
# Kênh Y3 Vĩ Mô Chứng Khoán Dễ Hiểu (@chungkhoanhuynguyen7) – NV1 soạn 2/11/2026 theo claude/giao_viec/nv1_tuan_0311.md. fb_trang = TT.
# Khuôn dx2 như _video/queue/20261102_1631c/video_dai.py. SỐ VIẾT THÀNH CHỮ trong "say". circles = chỉ số tuần trong px_tuan.json (0 = tuần cũ nhất 27/10/2025, 51 = tuần 26/10/2026).
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['Y3_0611A'] = [{'k': 'hook',
  'ch': 'Chương 1 – Mở đầu: tăng trưởng chạm tới đâu?',
  'moc': True,
  'label': 'HPG – Hòa Phát',
  'cap': ('XÂY DỰNG BỨT', 'THÉP, GIẤY?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'HPGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[16, 26.51, 'Đỉnh tuần 23/2: 26,51', 0.6], [47, 19.6, 'Đáy tuần 28/9: 19,60', 1.6], [51, 20.75, '28/10: 20,75', 2.6]]},
  'anh': 'steel mill furnace',
  'say': 'Quý ba năm hai nghìn không trăm hai mươi sáu, GDP tăng chín phẩy chín mươi lăm phần trăm, công nghiệp và xây dựng tăng mười hai phẩy năm phần trăm, theo Cục Thống kê. '
         'Vốn đầu tư toàn xã hội chín tháng tăng mười lăm phẩy một phần trăm. Vậy tăng trưởng xây dựng chạm tới thép, bao bì giấy và xây lắp hạ tầng ra sao? Mình soi H P G, D H C '
         'và C T R, còn N K G và H S G nhắc ngắn. Có một mã lợi nhuận tăng hơn gấp đôi nhưng chi phí lãi vay còn tăng nhanh hơn, bạn đoán thử là mã nào, đáp án nằm ở cuối video.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Bức tranh vĩ mô: đầu tư và xây dựng',
  'moc': True,
  'label': 'Số liệu vĩ mô (Cục Thống kê)',
  'cap': 'VĨ MÔ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('GDP quý 3/2026', '+9,95%', '9 tháng +9,01%'),
            ('Công nghiệp – xây dựng', '+12,50%', 'quý 3; 9 tháng +11,21%'),
            ('Vốn đầu tư toàn xã hội', '3.109,6 nghìn tỷ', '9 tháng, +15,1%'),
            ('Sản xuất công nghiệp (IIP)', '+14,8%', 'quý 3; 9 tháng +12,3%'),
            ('Bán lẻ và dịch vụ', '+13,4%', '9 tháng')],
  'anh': 'construction site cranes Vietnam',
  'say': 'Số liệu của Cục Thống kê. GDP quý ba ước tăng chín phẩy chín mươi lăm phần trăm, chín tháng tăng chín phẩy không một phần trăm. Công nghiệp và xây dựng tăng mười hai '
         'phẩy năm phần trăm trong quý ba. Vốn đầu tư toàn xã hội chín tháng theo giá hiện hành đạt ba nghìn một trăm linh chín phẩy sáu nghìn tỷ đồng, tăng mười lăm phẩy một '
         'phần trăm. Chỉ số sản xuất công nghiệp quý ba tăng mười bốn phẩy tám phần trăm. Tổng mức bán lẻ chín tháng tăng mười ba phẩy bốn phần trăm. Đây đều là số ước tính của '
         'cơ quan thống kê.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Cơ chế: tăng trưởng đi vào lợi nhuận thế nào?',
  'moc': True,
  'label': 'Từ công trường tới lợi nhuận',
  'cap': 'CƠ CHẾ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Thép: nhu cầu từ xây dựng, hạ tầng, sản xuất', [34, 197, 94]),
            ('Xây lắp hạ tầng: doanh thu phụ thuộc hợp đồng và tiến độ', [255, 196, 0]),
            ('Bao bì giấy: liên hệ gián tiếp qua sản xuất, tiêu dùng, xuất khẩu', [56, 189, 248]),
            ('Chi phí lãi vay: lãi suất cao ăn vào lợi nhuận', [239, 68, 68])],
  'anh': 'infrastructure road building Vietnam',
  'say': 'Cơ chế chung. Khi đầu tư và xây dựng tăng, nhu cầu thép tăng vì thép là vật liệu đầu vào. Doanh nghiệp xây lắp hạ tầng có thêm hợp đồng, nhưng doanh thu còn tùy tiến '
         'độ. Bao bì giấy liên hệ gián tiếp hơn, qua sản xuất công nghiệp, bán lẻ và xuất khẩu. Chi phí lãi vay là mảnh ghép thứ tư: theo Ngân hàng Nhà nước, lãi suất tiền gửi '
         'bình quân sáu phẩy ba mươi tám phần trăm, tăng một phẩy mười lăm điểm so với cuối năm hai nghìn không trăm hai mươi lăm.'},
 {'k': 'cards',
  'ch': 'Chương 4 – H P G: thép hưởng lợi rõ nhất',
  'moc': True,
  'label': 'HPG – Hòa Phát',
  'cap': 'HPG QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '8.217 tỷ', '+106,0% so với cùng kỳ'),
            ('Doanh thu thuần', '62.214 tỷ', '+70,9%'),
            ('Biên lợi nhuận gộp', '19,2%', 'cùng kỳ 16,7%'),
            ('Chi phí lãi vay', '+118,4%', 'ăn vào lợi nhuận'),
            ('P/E · ROE', '6,46 · 19,9%', 'giá 1 năm −13,3%')],
  'anh': 'Hoa Phat steel plant',
  'say': 'Bắt đầu với H P G. Quý ba, lợi nhuận sau thuế công ty mẹ tám nghìn hai trăm mười bảy tỷ đồng, tăng một trăm linh sáu phần trăm so với cùng kỳ. Doanh thu thuần sáu mươi '
         'hai nghìn hai trăm mười bốn tỷ, tăng bảy mươi phẩy chín phần trăm, biên lợi nhuận gộp cải thiện lên mười chín phẩy hai phần trăm từ mười sáu phẩy bảy. Chín tháng lợi '
         'nhuận đạt hai mươi ba nghìn năm trăm tám mươi hai tỷ, tăng một trăm linh ba phẩy năm phần trăm. Tuy vậy chi phí lãi vay tăng một trăm mười tám phẩy bốn phần trăm, ăn '
         'vào lợi nhuận. Giá cổ phiếu một năm vẫn giảm mười ba phẩy ba phần trăm, ở hai mươi phẩy bảy mươi lăm nghìn đồng.'},
 {'k': 'bars',
  'label': 'HPG – LNST theo quý (tỷ đồng)',
  'cap': 'HPG 8 QUÝ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q4/24', 2809, [56, 189, 248], '2.809'),
           ('Q1/25', 3344, [56, 189, 248], '3.344'),
           ('Q2/25', 4256, [56, 189, 248], '4.256'),
           ('Q3/25', 3988, [56, 189, 248], '3.988'),
           ('Q4/25', 3864, [56, 189, 248], '3.864'),
           ('Q1/26', 8994, [34, 197, 94], '8.994'),
           ('Q2/26', 6371, [56, 189, 248], '6.371'),
           ('Q3/26', 8217, [255, 196, 0], '8.217')],
  'anh': 'blast furnace steel production',
  'say': 'Chuỗi tám quý của H P G cho thấy bước nhảy. Năm quý đầu chuỗi, lợi nhuận quanh hai nghìn tám trăm linh chín đến bốn nghìn hai trăm năm mươi sáu tỷ. Quý một năm nay vọt '
         'lên tám nghìn chín trăm chín mươi bốn tỷ, quý hai còn sáu nghìn ba trăm bảy mươi mốt tỷ, quý ba trở lại tám nghìn hai trăm mười bảy tỷ. Lợi nhuận tăng, nhưng nợ vay và '
         'lãi vay cũng tăng, cần đọc cả hai.'},
 {'k': 'cards',
  'ch': 'Chương 5 – D H C và C T R: bao bì giấy, xây lắp hạ tầng',
  'moc': True,
  'label': 'DHC – bao bì giấy',
  'cap': 'DHC QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '149 tỷ', '+49,7% so với cùng kỳ'),
            ('Doanh thu thuần', '1.093 tỷ', '+17,3%'),
            ('Biên lợi nhuận gộp', '20,8%', 'cùng kỳ 15,7%'),
            ('Lũy kế 9 tháng', '464 tỷ', '+79,7%'),
            ('Giá 1 năm', '+28,2%', 'P/E 6,53 · ROE 25,4%')],
  'anh': 'paper packaging factory',
  'say': 'Sang D H C, doanh nghiệp bao bì giấy. Quý ba lợi nhuận một trăm bốn mươi chín tỷ đồng, tăng bốn mươi chín phẩy bảy phần trăm, doanh thu tăng mười bảy phẩy ba phần trăm '
         'lên một nghìn không trăm chín mươi ba tỷ, còn biên lợi nhuận gộp cải thiện lên hai mươi phẩy tám phần trăm từ mười lăm phẩy bảy. Chín tháng lợi nhuận bốn trăm sáu mươi '
         'bốn tỷ, tăng bảy mươi chín phẩy bảy phần trăm. Lý do cụ thể báo cáo gốc có phần giải trình. Điều đáng nhấn mạnh: D H C là mã duy nhất trong ba mã mà giá một năm tăng, '
         'cao hơn hai mươi tám phẩy hai phần trăm.'},
 {'k': 'cards',
  'label': 'CTR – xây lắp hạ tầng',
  'cap': 'CTR QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '183 tỷ', '+8,6% so với cùng kỳ'),
            ('Doanh thu thuần', '4.227 tỷ', '+6,6%'),
            ('Lũy kế 9 tháng', '505 tỷ', '+15,9%'),
            ('Chi phí lãi vay', '+93,1%', 'ăn vào lợi nhuận'),
            ('P/E · ROE', '12,91 · 30,6%', 'giá 1 năm −15,2%')],
  'anh': 'telecom tower construction',
  'say': 'Còn C T R, doanh nghiệp xây lắp hạ tầng. Quý ba lợi nhuận một trăm tám mươi ba tỷ đồng, tăng tám phẩy sáu phần trăm, doanh thu tăng sáu phẩy sáu phần trăm lên bốn nghìn '
         'hai trăm hai mươi bảy tỷ. Chín tháng lợi nhuận năm trăm linh năm tỷ, tăng mười lăm phẩy chín phần trăm. Đây là mức tăng khiêm tốn hơn nhiều so với con số tăng trưởng '
         'xây dựng của cả nền kinh tế, và chi phí lãi vay tăng tới chín mươi ba phẩy một phần trăm. Giá một năm giảm mười lăm phẩy hai phần trăm. Tức là tăng trưởng xây dựng '
         'chung chưa chắc chuyển thẳng thành lợi nhuận tương ứng cho từng doanh nghiệp.'},
 {'k': 'bars',
  'ch': 'Chương 6 – So sánh: chi phí lãi vay và giá cổ phiếu',
  'moc': True,
  'label': 'LNST quý 3/2026 so với cùng kỳ (%)',
  'cap': 'LNST QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('NKG', 154.8, [34, 197, 94], '+154,8%'),
           ('HPG', 106.0, [34, 197, 94], '+106,0%'),
           ('DHC', 49.7, [34, 197, 94], '+49,7%'),
           ('CTR', 8.6, [34, 197, 94], '+8,6%'),
           ('HSG', -37.4, [239, 68, 68], '−37,4%')],
  'anh': 'steel coil warehouse',
  'say': 'Đặt cạnh nhau. Lợi nhuận quý ba so với cùng kỳ: N K G tăng một trăm năm mươi bốn phẩy tám phần trăm, H P G tăng một trăm linh sáu, D H C tăng bốn mươi chín phẩy bảy, C '
         'T R tăng tám phẩy sáu và H S G giảm ba mươi bảy phẩy bốn phần trăm. N K G có doanh thu tăng bốn mươi lăm phần trăm và biên gộp lên chín phần trăm từ bốn phẩy tám. Còn H '
         'S G doanh thu tăng hai mươi bốn phẩy ba phần trăm nhưng lợi nhuận giảm, so với quý hai giảm tám mươi lăm phẩy sáu phần trăm. Cùng là thép, nhưng kết quả rất khác nhau.'},
 {'k': 'bars',
  'label': 'Chi phí lãi vay quý 3 (% so với cùng kỳ)',
  'cap': 'LÃI VAY',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('HSG', 195.8, [239, 68, 68], '+195,8%'), ('HPG', 118.4, [239, 68, 68], '+118,4%'), ('CTR', 93.1, [239, 68, 68], '+93,1%'), ('NKG', 83.0, [239, 68, 68], '+83,0%')],
  'anh': 'bank loan interest',
  'say': 'Và đây là đáp án câu đố đầu video: mã có lợi nhuận tăng hơn gấp đôi mà lãi vay tăng nhanh hơn chính là H P G, lợi nhuận tăng một trăm linh sáu phần trăm còn chi phí lãi '
         'vay tăng một trăm mười tám phẩy bốn. Ở H S G lãi vay tăng một trăm chín mươi lăm phẩy tám phần trăm, ở C T R chín mươi ba phẩy một và N K G tám mươi ba. Đây chỉ là con '
         'số trong báo cáo, không phải phân tích nguyên nhân. Giá một năm đến ngày hai mươi tám tháng mười: H P G giảm mười ba phẩy ba phần trăm, C T R giảm mười lăm phẩy hai, N '
         'K G giảm mười bảy phẩy năm, H S G giảm mười bốn phẩy bốn, chỉ D H C tăng hai mươi tám phẩy hai.'},
 {'k': 'checklist',
  'label': 'Nhìn gì khi GDP và xây dựng tăng',
  'cap': 'CẦN NHÌN GÌ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Doanh thu và biên gộp của chính doanh nghiệp', [255, 196, 0]),
            ('Chi phí lãi vay tăng nhanh hơn hay chậm hơn lợi nhuận', [239, 68, 68]),
            ('Mức liên hệ trực tiếp hay gián tiếp với xây dựng', [56, 189, 248]),
            ('Số vĩ mô là ước tính, báo cáo gốc mới là chi tiết', [56, 189, 248])],
  'anh': 'analyst checklist report',
  'say': 'Tóm lại, khi GDP và xây dựng tăng, bạn nên nhìn bốn thứ. Doanh thu và biên gộp của chính doanh nghiệp. Chi phí lãi vay đang tăng nhanh hơn hay chậm hơn lợi nhuận. Mức '
         'liên hệ của doanh nghiệp với xây dựng là trực tiếp như thép và xây lắp, hay gián tiếp như bao bì. Và nhớ rằng số vĩ mô là ước tính của Cục Thống kê, còn báo cáo gốc mới '
         'có chi tiết.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN: CỤC', 'THỐNG KÊ, BCTC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu: Cục Thống kê, Ngân hàng Nhà nước và báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu. Đây là chia sẻ kiến thức, không phải khuyến nghị mua '
         'bán. Câu hỏi cho bạn: theo bạn, lợi nhuận tăng gấp đôi mà giá cổ phiếu vẫn giảm là do đâu? Hãy để lại bình luận. Xem thêm tại chungkhoanhuynguyen chấm com.'}]

S['Y3_0611B'] = [{'k': 'hook',
  'ch': 'Chương 1 – Mở đầu: thương mại bùng nổ',
  'moc': True,
  'label': 'GMD – Gemadept',
  'cap': ('XUẤT NHẬP', 'KHẨU TĂNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'GMDW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[7, 36.86, 'Đáy tuần 15/12: 36,86', 0.6], [17, 57.99, 'Đỉnh tuần 2/3: 57,99', 1.6], [51, 54.0, '28/10: 54,00', 2.6]]},
  'anh': 'container port ship crane',
  'say': 'Theo Cục Thống kê, chín tháng đầu năm hai nghìn không trăm hai mươi sáu xuất khẩu tăng hai mươi bốn phẩy năm phần trăm, nhập khẩu tăng ba mươi sáu phẩy bảy phần trăm, '
         'tổng kim ngạch tám trăm tám mươi tám phẩy không hai tỷ đô la. Hàng hóa qua nhiều hơn thì cảng biển và logistics hưởng lợi đến đâu? Mình soi G M D, H A H và V S C. Lưu '
         'ý: G M D và V S C mới có báo cáo quý hai, còn H A H đã có quý ba. Ở lại đến cuối, vì có một mã lợi nhuận nhảy gấp đôi nhưng lại phụ thuộc vào khoản không đến từ hoạt '
         'động cốt lõi.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Thương mại 9 tháng nói gì?',
  'moc': True,
  'label': 'Thương mại 9 tháng (Cục Thống kê)',
  'cap': 'THƯƠNG MẠI',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Tổng kim ngạch', '888,02 tỷ USD', '+30,4%'),
            ('Xuất khẩu', '+24,5%', '9 tháng 2026'),
            ('Nhập khẩu', '+36,7%', 'nhanh hơn xuất khẩu'),
            ('Nhập siêu', '19,42 tỷ USD', '9 tháng'),
            ('FDI giải ngân', '21,07 tỷ USD', '+12,1%')],
  'anh': 'container terminal cargo',
  'say': 'Số liệu của Cục Thống kê cho chín tháng. Tổng kim ngạch hàng hóa đạt tám trăm tám mươi tám phẩy không hai tỷ đô la, tăng ba mươi phẩy bốn phần trăm. Xuất khẩu tăng hai '
         'mươi bốn phẩy năm phần trăm, nhập khẩu tăng ba mươi sáu phẩy bảy phần trăm, nhanh hơn xuất khẩu, nên nhập siêu mười chín phẩy bốn mươi hai tỷ đô la. Vốn FDI thực hiện '
         'chín tháng đạt hai mươi mốt phẩy không bảy tỷ đô la, tăng mười hai phẩy một phần trăm.'},
 {'k': 'bars',
  'label': 'Tăng trưởng 9 tháng 2026 (%)',
  'cap': 'TĂNG TRƯỞNG',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Nhập khẩu', 36.7, [255, 196, 0], '+36,7%'),
           ('Tổng kim ngạch', 30.4, [255, 196, 0], '+30,4%'),
           ('Xuất khẩu', 24.5, [255, 196, 0], '+24,5%'),
           ('Bán lẻ', 13.4, [56, 189, 248], '+13,4%'),
           ('IIP', 12.3, [56, 189, 248], '+12,3%'),
           ('FDI giải ngân', 12.1, [56, 189, 248], '+12,1%'),
           ('GDP', 9.01, [56, 189, 248], '+9,01%')],
  'anh': 'cargo ship sea',
  'say': 'Đặt cạnh các chỉ tiêu khác. Nhập khẩu tăng ba mươi sáu phẩy bảy phần trăm, tổng kim ngạch ba mươi phẩy bốn, xuất khẩu hai mươi bốn phẩy năm. Bán lẻ tăng mười ba phẩy '
         'bốn phần trăm, sản xuất công nghiệp mười hai phẩy ba, FDI giải ngân mười hai phẩy một và GDP chín tháng tăng chín phẩy không một phần trăm. Kim ngạch thương mại tăng '
         'nhanh hơn rất nhiều so với GDP. Điều này cho thấy lượng hàng hóa quay vòng quanh nền kinh tế đang tăng nhanh, nhưng đó là giá trị tính bằng đô la, chưa phải sản lượng '
         'container qua cảng.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Cơ chế: hàng qua cảng thành lợi nhuận ra sao?',
  'moc': True,
  'label': 'Từ thương mại tới lợi nhuận cảng',
  'cap': 'CƠ CHẾ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Hàng qua cảng nhiều hơn: sản lượng container tăng', [34, 197, 94]),
            ('Giá dịch vụ và công suất quyết định phần được hưởng', [255, 196, 0]),
            ('Nhiên liệu: Brent 108,74 USD/thùng, 1 năm +67,1%', [239, 68, 68]),
            ('Số liệu kim ngạch là giá trị, không phải sản lượng', [56, 189, 248])],
  'anh': 'port logistics trucks',
  'say': 'Cơ chế chung. Hàng hóa qua cảng nhiều hơn thì sản lượng container có thể tăng, và doanh nghiệp cảng có thêm doanh thu. Nhưng phần được hưởng còn tùy giá dịch vụ, công '
         'suất và chi phí. Với vận tải, nhiên liệu là chi phí lớn: giá dầu Brent ngày hai tháng mười một là một trăm linh tám phẩy bảy mươi bốn đô la một thùng, cao hơn một năm '
         'trước sáu mươi bảy phẩy một phần trăm. Và cần nhớ, kim ngạch của Cục Thống kê là giá trị tính bằng đô la, không phải số container.'},
 {'k': 'cards',
  'ch': 'Chương 4 – G M D: lợi nhuận gấp đôi, nhưng từ đâu?',
  'moc': True,
  'label': 'GMD – Gemadept (quý 2/2026)',
  'cap': 'GMD QUÝ 2',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 2/2026', '1.124 tỷ', '+152,5% so với cùng kỳ'),
            ('Doanh thu thuần', '1.762 tỷ', '+17,9%'),
            ('Biên lợi nhuận gộp', '52,5%', 'cùng kỳ 48,3%'),
            ('Lũy kế 6 tháng', '1.658 tỷ', '+95,5%'),
            ('P/E · ROE', '13,34 · 17,3%', 'giá 1 năm +25,3%')],
  'anh': 'Gemadept port Vietnam',
  'say': 'Bắt đầu với G M D, số liệu quý hai năm hai nghìn không trăm hai mươi sáu. Lợi nhuận sau thuế công ty mẹ một nghìn một trăm hai mươi bốn tỷ đồng, tăng một trăm năm mươi '
         'hai phẩy năm phần trăm so với cùng kỳ, trong khi doanh thu chỉ tăng mười bảy phẩy chín phần trăm lên một nghìn bảy trăm sáu mươi hai tỷ. Dữ liệu ghi rõ lãi phụ thuộc '
         'nhiều vào doanh thu tài chính, không đến từ hoạt động cốt lõi. Biên gộp cải thiện lên năm mươi hai phẩy năm phần trăm từ bốn mươi tám phẩy ba. Vậy tăng trưởng thương '
         'mại chỉ giải thích được một phần, phần còn lại cần xem phần giải trình của báo cáo gốc.'},
 {'k': 'bars',
  'label': 'GMD – LNST theo quý (tỷ đồng)',
  'cap': 'GMD 8 QUÝ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/24', 335, [56, 189, 248], '335'),
           ('Q4/24', 231, [56, 189, 248], '231'),
           ('Q1/25', 403, [56, 189, 248], '403'),
           ('Q2/25', 445, [56, 189, 248], '445'),
           ('Q3/25', 315, [56, 189, 248], '315'),
           ('Q4/25', 592, [56, 189, 248], '592'),
           ('Q1/26', 534, [56, 189, 248], '534'),
           ('Q2/26', 1124, [255, 196, 0], '1.124')],
  'anh': 'Gemadept container port',
  'say': 'Chuỗi tám quý của G M D, từ quý ba năm hai nghìn không trăm hai mươi bốn đến quý hai năm hai nghìn không trăm hai mươi sáu: lợi nhuận đi từ ba trăm ba mươi lăm tỷ lên '
         'năm trăm chín mươi hai tỷ quý bốn năm ngoái và năm trăm ba mươi bốn tỷ quý một. Quý hai vọt lên một nghìn một trăm hai mươi bốn tỷ, tăng một trăm mười phẩy bốn phần '
         'trăm so với quý trước. Đến ngày hai mươi tám tháng mười, cổ phiếu ở năm mươi bốn nghìn đồng, hơn một năm trước hai mươi lăm phẩy ba phần trăm, P trên E mười ba phẩy ba '
         'mươi bốn, chỉ là mô tả quá khứ.'},
 {'k': 'cards',
  'ch': 'Chương 5 – H A H và V S C: vận tải và cảng',
  'moc': True,
  'label': 'HAH – Hải An (quý 3/2026)',
  'cap': 'HAH QUÝ 3',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3/2026', '329 tỷ', '+8,0% so với cùng kỳ'),
            ('Doanh thu thuần', '1.419 tỷ', '+5,3%'),
            ('Lũy kế 9 tháng', '1.001 tỷ', '+11,3%'),
            ('Giá 1 năm', '−12,1%', '3 tháng +15,1%'),
            ('P/E · ROE', '7,28 · 22,5%', 'giá 28/10: 50,60')],
  'anh': 'container ship Hai An',
  'say': 'Đến H A H, đã có số liệu quý ba. Lợi nhuận sau thuế công ty mẹ ba trăm hai mươi chín tỷ đồng, tăng tám phần trăm so với cùng kỳ, doanh thu thuần tăng năm phẩy ba phần '
         'trăm lên một nghìn bốn trăm mười chín tỷ. Chín tháng lợi nhuận đạt một nghìn không trăm linh một tỷ, tăng mười một phẩy ba phần trăm. Đây là mức tăng khiêm tốn so với '
         'kim ngạch thương mại tăng hơn ba mươi phần trăm. Giá cổ phiếu một năm giảm mười hai phẩy một phần trăm, nhưng ba tháng gần nhất tăng mười lăm phẩy một phần trăm, ở năm '
         'mươi phẩy sáu nghìn đồng.'},
 {'k': 'cards',
  'label': 'VSC – Viconship (quý 2/2026)',
  'cap': 'VSC QUÝ 2',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 2/2026', '186 tỷ', '+59,8% so với cùng kỳ'),
            ('So với quý 1', '13,9 lần', 'quý 1/2026: 13 tỷ'),
            ('Biên lợi nhuận gộp', '43,6%', 'cùng kỳ 31,4%'),
            ('Chi phí lãi vay', '+188,3%', 'ăn vào lợi nhuận'),
            ('Giá 1 năm', '−41,8%', 'P/E 14,4 · ROE 5,5%')],
  'anh': 'Viconship port Hai Phong',
  'say': 'V S C ghi nhận quý hai lợi nhuận một trăm tám mươi sáu tỷ đồng, tăng năm mươi chín phẩy tám phần trăm so với cùng kỳ và gấp mười ba phẩy chín lần quý một, vì quý một '
         'chỉ có mười ba tỷ. Biên gộp cải thiện lên bốn mươi ba phẩy sáu phần trăm từ ba mươi mốt phẩy bốn, nhưng chi phí lãi vay tăng một trăm tám mươi tám phẩy ba phần trăm, '
         'sáu tháng lợi nhuận chỉ tăng một phẩy một phần trăm. Giá cổ phiếu một năm giảm tới bốn mươi mốt phẩy tám phần trăm, ở mười bốn phẩy năm nghìn đồng. Nghĩa là một quý tốt '
         'chưa chắc đủ để đảo ngược xu hướng giá.'},
 {'k': 'bars',
  'ch': 'Chương 6 – So sánh ba mã cảng và vận tải',
  'moc': True,
  'label': 'LNST quý gần nhất so với cùng kỳ (%)',
  'cap': 'SO CÙNG KỲ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('GMD (Q2)', 152.5, [34, 197, 94], '+152,5%'), ('VSC (Q2)', 59.8, [34, 197, 94], '+59,8%'), ('HAH (Q3)', 8.0, [34, 197, 94], '+8,0%')],
  'anh': 'seaport container yard',
  'say': 'Đặt ba mã cạnh nhau. Lợi nhuận quý gần nhất so với cùng kỳ: G M D quý hai tăng một trăm năm mươi hai phẩy năm phần trăm, V S C quý hai tăng năm mươi chín phẩy tám và H '
         'A H quý ba tăng tám. Các mã có kỳ khác nhau nên không so trực tiếp được. Còn giá một năm: G M D tăng hai mươi lăm phẩy ba phần trăm, H A H giảm mười hai phẩy một và V S '
         'C giảm bốn mươi mốt phẩy tám. Thương mại tăng mạnh nhưng thị trường chưa trả giá đồng nhất.'},
 {'k': 'checklist',
  'label': 'Nhìn gì khi thương mại tăng',
  'cap': 'CẦN NHÌN GÌ',
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Lãi có đến từ hoạt động cốt lõi hay doanh thu tài chính', [255, 196, 0]),
            ('Doanh thu và biên gộp qua nhiều quý, không chỉ một quý', [34, 197, 94]),
            ('Chi phí lãi vay và nhiên liệu', [239, 68, 68]),
            ('Kim ngạch là giá trị, không phải sản lượng container', [56, 189, 248])],
  'anh': 'investor reading chart',
  'say': 'Tóm lại. Một, xem lãi đến từ hoạt động cốt lõi hay từ doanh thu tài chính. Hai, nhìn doanh thu và biên gộp qua nhiều quý. Ba, nhìn chi phí lãi vay và nhiên liệu. Bốn, '
         'nhớ rằng kim ngạch thương mại là giá trị bằng đô la, chưa phải sản lượng container. Kết luận của video này là: thương mại tăng mạnh là điều kiện thuận lợi, nhưng phần '
         'lợi nhuận mỗi doanh nghiệp hưởng khác nhau, và dữ liệu hiện có cho thấy sự khác biệt đó rất lớn.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN: CỤC', 'THỐNG KÊ, BCTC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu: Cục Thống kê, báo cáo tài chính quý hai năm hai nghìn không trăm hai mươi sáu của G M D và V S C, quý ba của H A H, dữ liệu giá của kênh. Đây là chia sẻ '
         'kiến thức, không phải khuyến nghị mua bán. Câu hỏi cho bạn: theo bạn, nên đánh giá doanh nghiệp cảng bằng lợi nhuận hay bằng sản lượng? Hãy để lại bình luận. Xem thêm '
         'tại chungkhoanhuynguyen chấm com.'}]

S['Y3_0611C'] = [{'k': 'hook',
  'ch': 'Chương 1 – Vốn ngoại chảy vào, khu công nghiệp kiếm tiền ra sao',
  'moc': True,
  'label': 'KBC – Kinh Bắc',
  'cap': ('VỐN NGOẠI VÀO', 'KCN GHI LÃI?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'KBCW', 'tf': 'W', 'weeks': 52, 'circles': [[14, 38.2, 'Đỉnh tuần 2/2: 38,20', 0.6], [48, 24.15, 'Đáy tuần 5/10: 24,15', 1.6], [51, 27.0, '28/10: 27,00', 2.6]]},
  'anh': 'industrial park Vietnam factory',
  'say': 'Vốn ngoại chảy vào nhà máy, vậy khu công nghiệp có kiếm tiền đều đặn không? Theo Cục Thống kê, vốn đầu tư nước ngoài thực hiện chín tháng đầu năm hai nghìn không trăm '
         'hai mươi sáu đạt hai mươi mốt phẩy không bảy tỷ đô la, tăng mười hai phẩy một phần trăm. Nghe như một dòng tiền chảy đều đặn. Nhưng nhìn vào lợi nhuận của ba doanh '
         'nghiệp khu công nghiệp là K B C, S Z C và I D C, bạn sẽ thấy một bức tranh rất khác: lợi nhuận đi theo từng đợt, không đi theo từng tháng. Hôm nay mình đi từng bước để '
         'hiểu vì sao. Ở lại đến cuối nhé, vì có một con số quý ba của K B C sẽ làm bạn phải dừng lại suy nghĩ.'},
 {'k': 'cards',
  'label': 'Vốn ngoại và đầu tư 9 tháng 2026',
  'cap': ('SỐ VĨ MÔ', '9 THÁNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('FDI giải ngân', '21,07 tỷ USD', 'tăng 12,1%'),
            ('Vốn đầu tư toàn xã hội', '3.109,6 nghìn tỷ đồng', 'tăng 15,1%'),
            ('Xuất nhập khẩu', '888,02 tỷ USD', 'tăng 30,4%'),
            ('GDP quý 3', 'tăng 9,95%', '9 tháng tăng 9,01%')],
  'anh': 'foreign investment factory Vietnam',
  'say': 'Trước hết là nền. Theo Cục Thống kê, vốn nước ngoài giải ngân chín tháng là hai mươi mốt phẩy không bảy tỷ đô la, tăng mười hai phẩy một phần trăm. Vốn đầu tư toàn xã '
         'hội theo giá hiện hành là ba nghìn một trăm linh chín phẩy sáu nghìn tỷ đồng, tăng mười lăm phẩy một phần trăm. Tổng kim ngạch xuất nhập khẩu hàng hóa là tám trăm tám '
         'mươi tám phẩy không hai tỷ đô la, tăng ba mươi phẩy bốn phần trăm. Kinh tế quý ba tăng chín phẩy chín mươi lăm phần trăm. Câu hỏi tiếp theo: tiền đó biến thành lợi '
         'nhuận khu công nghiệp bằng cách nào?'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Vì sao lợi nhuận khu công nghiệp đi theo đợt',
  'moc': True,
  'label': 'Cơ chế ghi nhận lợi nhuận khu công nghiệp',
  'cap': ('CƠ CHẾ', 'THEO ĐỢT'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Bán hoặc cho thuê đất đã có hạ tầng', [255, 196, 0]),
            ('Một hợp đồng đất thường rất lớn', [56, 189, 248]),
            ('Bàn giao đất xong mới ghi doanh thu', [34, 197, 94]),
            ('Quý không có đợt bàn giao thì doanh thu mỏng', [239, 68, 68])],
  'anh': 'industrial land aerial',
  'say': 'Chương hai. Vì sao lợi nhuận khu công nghiệp đi theo đợt chứ không đều? Đây là cơ chế chung, không phải số liệu riêng của doanh nghiệp nào. Doanh nghiệp khu công nghiệp '
         'làm hạ tầng rồi bán hoặc cho thuê lại quyền sử dụng đất cho nhà đầu tư. Một hợp đồng đất thường rất lớn. Khi hợp đồng đó được bàn giao và ghi nhận doanh thu, lợi nhuận '
         'cả quý có thể nhảy lên. Quý nào không có đợt bàn giao nào, doanh thu mỏng đi, dù nhà đầu tư ngoại vẫn đang xây nhà máy ở nơi khác. Nói cách khác, vốn giải ngân là dòng '
         'chảy, còn lợi nhuận khu công nghiệp giống những cú chạm. Muốn đọc đúng phải nhìn nhiều quý liền.'},
 {'k': 'cards',
  'ch': 'Chương 3 – K B C quý ba: bật mạnh nhưng lũy kế vẫn thấp',
  'moc': True,
  'label': 'KBC – Quý 3/2026',
  'cap': ('KBC', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '911 tỷ', 'tăng 196,6% so với cùng kỳ'),
            ('Doanh thu thuần', '3.187 tỷ', 'tăng 136,6%'),
            ('Lũy kế 9 tháng', '1.143 tỷ', 'giảm 23,6%'),
            ('Biên lợi nhuận gộp', '54,0%', 'cùng kỳ 58,2%'),
            ('Chi phí lãi vay', 'tăng 69,0%', 'ăn vào lợi nhuận')],
  'anh': 'industrial zone Bac Ninh',
  'say': 'Chương ba, mã chính hôm nay là K B C. Quý ba hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế công ty mẹ là chín trăm mười một tỷ đồng, tăng một trăm chín mươi sáu '
         'phẩy sáu phần trăm so với cùng kỳ. Doanh thu thuần ba nghìn một trăm tám mươi bảy tỷ, tăng một trăm ba mươi sáu phẩy sáu phần trăm. So với quý hai, lợi nhuận tăng gấp '
         'một trăm hai mươi bảy phẩy một lần, vì quý hai chỉ có bảy tỷ. Nhưng lũy kế chín tháng là một nghìn một trăm bốn mươi ba tỷ, vẫn giảm hai mươi ba phẩy sáu phần trăm so '
         'với cùng kỳ. Biên lợi nhuận gộp năm mươi tư phần trăm, thấp hơn năm mươi tám phẩy hai phần trăm cùng kỳ, và chi phí lãi vay tăng sáu mươi chín phần trăm.'},
 {'k': 'bars',
  'label': 'KBC – LNST từng quý (tỷ đồng)',
  'cap': ('KBC', 'RĂNG CƯA'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 307, [56, 189, 248], '307'),
           ('Q4/25', 608, [56, 189, 248], '608'),
           ('Q1/26', 224, [56, 189, 248], '224'),
           ('Q2/26', 7, [239, 68, 68], '7'),
           ('Q3/26', 911, [34, 197, 94], '911')],
  'anh': 'construction site industrial park',
  'say': 'Bây giờ nhìn năm quý gần nhất của K B C. Quý ba năm ngoái ba trăm linh bảy tỷ. Quý bốn sáu trăm linh tám tỷ. Quý một năm nay hai trăm hai mươi bốn tỷ. Quý hai chỉ còn '
         'bảy tỷ. Rồi quý ba vọt lên chín trăm mười một tỷ. Đường này là răng cưa, đúng hình ảnh lợi nhuận đi theo đợt. Còn nguyên nhân cụ thể của từng quý, báo cáo gốc của công '
         'ty có phần giải trình, mình không đoán thay ở đây.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Cùng dòng vốn ngoại, ba kết quả khác nhau',
  'moc': True,
  'label': 'LNST quý 3/2026 so với cùng kỳ (%)',
  'cap': ('3 KCN', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('KBC', 196.6, [34, 197, 94], '+196,6%'), ('SZC', 3.8, [34, 197, 94], '+3,8%'), ('IDC', -41.5, [239, 68, 68], '−41,5%')],
  'anh': 'industrial park aerial Vietnam',
  'say': 'Chương bốn. Nếu vốn ngoại là cơn gió chung, ba doanh nghiệp có cùng nhịp không? Dữ liệu cho thấy là không. Quý ba, lợi nhuận K B C tăng một trăm chín mươi sáu phẩy sáu '
         'phần trăm. S Z C tăng ba phẩy tám phần trăm. I D C giảm bốn mươi mốt phẩy năm phần trăm. Cùng một dòng vốn ngoại, ba kết quả ở ba hướng. Điều này khớp với cơ chế đợt '
         'bàn giao: mỗi doanh nghiệp có quỹ đất, tiến độ và thời điểm ghi nhận riêng.'},
 {'k': 'cards',
  'label': 'SZC và IDC – Quý 3/2026',
  'cap': ('SZC', 'IDC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('SZC – LNST quý 3', '22 tỷ', 'tăng 3,8%'),
            ('SZC – Lũy kế 9 tháng', '58 tỷ', 'giảm 76,2%'),
            ('IDC – LNST quý 3', '493 tỷ', 'giảm 41,5%'),
            ('IDC – Doanh thu', '2.076 tỷ', 'giảm 27,7%'),
            ('IDC – Lũy kế 9 tháng', '1.373 tỷ', 'giảm 7,4%')],
  'anh': 'logistics warehouse industrial',
  'say': 'Nhìn kỹ hơn. S Z C quý ba lãi hai mươi hai tỷ đồng, doanh thu một trăm mười hai tỷ, tăng hai mươi chín phẩy sáu phần trăm. Nhưng lũy kế chín tháng chỉ năm mươi tám tỷ, '
         'giảm bảy mươi sáu phẩy hai phần trăm. I D C quý ba lãi bốn trăm chín mươi ba tỷ, giảm bốn mươi mốt phẩy năm phần trăm, doanh thu hai nghìn không trăm bảy mươi sáu tỷ, '
         'giảm hai mươi bảy phẩy bảy phần trăm. Quý ba năm ngoái I D C là tám trăm bốn mươi hai tỷ, mức cao nhất trong tám quý của bảng, nên so với cùng kỳ khá nặng.'},
 {'k': 'bars',
  'ch': 'Chương 5 – Giá cổ phiếu và định giá nhìn lại',
  'moc': True,
  'label': 'Biến động giá đến 28/10/2026 (%)',
  'cap': ('GIÁ', 'ĐẾN 28/10'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('KBC 1 năm', -22.2, [239, 68, 68], '−22,2%'),
           ('SZC 1 năm', -30.0, [239, 68, 68], '−30,0%'),
           ('KBC 1 tháng', 4.7, [34, 197, 94], '+4,7%'),
           ('SZC 1 tháng', 16.2, [34, 197, 94], '+16,2%')],
  'anh': 'stock market board Vietnam',
  'say': 'Chương năm: giá cổ phiếu nói gì? Đến ngày hai mươi tám tháng mười, K B C đóng cửa ở mức hai mươi bảy, giảm hai mươi hai phẩy hai phần trăm sau một năm, nhưng tăng bốn '
         'phẩy bảy phần trăm trong một tháng. S Z C ở mức hai mươi phẩy một, giảm ba mươi phần trăm sau một năm, nhưng tăng mười sáu phẩy hai phần trăm trong một tháng. Giá và '
         'lợi nhuận quý không phải lúc nào cũng đi cùng nhịp, và đây chỉ là mô tả quá khứ, không phải dự báo.'},
 {'k': 'cards',
  'label': 'Định giá hiện tại theo dữ liệu',
  'cap': ('P/E', 'P/B – ROE'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('KBC', 'P/E 13,98', 'P/B 0,94, ROE 6,5%'), ('SZC', 'P/E 21,66', 'P/B 1,14, ROE 5,1%'), ('IDC', 'P/E 7,83', 'P/B 1,97, ROE 20,9%')],
  'anh': 'calculator financial report',
  'say': 'Về định giá theo dữ liệu. K B C có P trên E mười ba phẩy chín tám, P trên B không phẩy chín bốn, R O E sáu phẩy năm phần trăm. S Z C có P trên E hai mươi mốt phẩy sáu '
         'sáu, P trên B một phẩy một bốn, R O E năm phẩy một phần trăm. I D C có P trên E bảy phẩy tám ba, P trên B một phẩy chín bảy, R O E hai mươi phẩy chín phần trăm. Mình '
         'chỉ mô tả, không kết luận rẻ hay đắt.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cách đọc lợi nhuận khu công nghiệp',
  'moc': True,
  'label': 'Checklist đọc doanh nghiệp khu công nghiệp',
  'cap': ('CHECKLIST', 'ĐỌC KCN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Nhìn nhiều quý liền, không nhìn một quý', [255, 196, 0]),
            ('Phân biệt vốn giải ngân với doanh thu bàn giao đất', [56, 189, 248]),
            ('So lũy kế 9 tháng, không chỉ quý', [34, 197, 94]),
            ('Xem biên gộp và chi phí lãi vay', [239, 68, 68]),
            ('Đọc phần giải trình trong báo cáo gốc', [255, 255, 255])],
  'anh': 'investor reading financial report',
  'say': 'Chương cuối, gom lại thành năm việc nên làm khi đọc lợi nhuận khu công nghiệp. Một, nhìn nhiều quý liền, đừng nhìn một quý. Hai, phân biệt vốn giải ngân với doanh thu '
         'bàn giao đất. Ba, so thêm lũy kế chín tháng, vì K B C quý ba tăng gần hai trăm phần trăm nhưng chín tháng vẫn giảm hai mươi ba phẩy sáu phần trăm. Bốn, xem biên lợi '
         'nhuận gộp và chi phí lãi vay. Năm, đọc phần giải trình trong báo cáo gốc. Câu trả lời cho câu hỏi hôm nay: vốn ngoại tăng là tín hiệu tốt cho nhu cầu, nhưng lợi nhuận '
         'khu công nghiệp được quyết định bởi thời điểm bàn giao đất.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CỤC THỐNG KÊ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu vĩ mô: Cục Thống kê, số liệu chín tháng hai nghìn không trăm hai mươi sáu. Số liệu doanh nghiệp: báo cáo tài chính quý ba hai nghìn không trăm hai mươi '
         'sáu. Đây là chia sẻ kiến thức, không phải khuyến nghị mua bán. Bạn nghĩ lợi nhuận khu công nghiệp nên đọc theo quý hay theo năm? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0711A'] = [{'k': 'hook',
  'ch': 'Chương 1 – Nhà máy chạy nhiều, điện có thành lợi nhuận',
  'moc': True,
  'label': 'POW – PV Power',
  'cap': ('NHÀ MÁY CHẠY', 'ĐIỆN LÃI?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'POWW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 11.12, 'Đáy tuần 27/10: 11,12', 0.6], [17, 16.85, 'Đỉnh tuần 2/3: 16,85', 1.6], [51, 12.55, '28/10: 12,55', 2.6]]},
  'anh': 'power plant electricity transmission',
  'say': 'Nhà máy chạy nhiều hơn thì cần điện nhiều hơn. Nghe hợp lý, nhưng điện có thực sự thành lợi nhuận đều đặn không? Theo Cục Thống kê, chỉ số sản xuất công nghiệp quý ba '
         'hai nghìn không trăm hai mươi sáu tăng mười bốn phẩy tám phần trăm so với cùng kỳ, chín tháng tăng mười hai phẩy ba phần trăm. Hôm nay mình nhìn ba cái tên ngành điện '
         'là P O W, N T hai và R E E, để hỏi ai đang thể hiện nhu cầu điện trong con số lợi nhuận, và vì sao doanh thu điện còn phụ thuộc thủy văn, giá khí. Có một con số của P O '
         'W quý hai mà mình nghĩ nhiều người ít để ý. Mình sẽ nói ở chương ba.'},
 {'k': 'cards',
  'label': 'Sản xuất công nghiệp 2026',
  'cap': ('SẢN XUẤT', 'CÔNG NGHIỆP'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('IIP quý 3', 'tăng 14,8%', 'so với cùng kỳ'),
            ('IIP 9 tháng', 'tăng 12,3%', 'Cục Thống kê'),
            ('Chế biến, chế tạo 9 tháng', 'tăng 12,9%', 'Cục Thống kê'),
            ('CN và xây dựng quý 3', 'tăng 12,50%', 'GDP quý 3 tăng 9,95%')],
  'anh': 'factory production line',
  'say': 'Bắt đầu từ nhu cầu. Theo Cục Thống kê, chỉ số sản xuất công nghiệp quý ba tăng mười bốn phẩy tám phần trăm, chín tháng tăng mười hai phẩy ba phần trăm, riêng chế biến '
         'chế tạo chín tháng tăng mười hai phẩy chín phần trăm. Kinh tế quý ba tăng chín phẩy chín mươi lăm phần trăm, trong đó công nghiệp và xây dựng tăng mười hai phẩy năm '
         'phần trăm. Nhà máy chạy nhiều hơn thường dùng nhiều điện hơn, đó là logic chung. Nhưng giữa chuyện dùng nhiều điện và chuyện doanh nghiệp phát điện lãi nhiều còn một '
         'đoạn đường khá dài.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Vì sao doanh thu điện không chỉ theo nhu cầu',
  'moc': True,
  'label': 'Doanh thu điện còn phụ thuộc gì',
  'cap': ('DOANH THU', 'ĐIỆN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Thủy điện: nước về hồ, thủy văn từng năm', [56, 189, 248]),
            ('Nhiệt điện khí: giá khí đầu vào', [239, 68, 68]),
            ('Mức huy động của hệ thống điều độ', [255, 196, 0]),
            ('Giá bán: hợp đồng và thị trường', [34, 197, 94])],
  'anh': 'hydropower dam Vietnam',
  'say': 'Chương hai. Vì sao doanh thu điện không chỉ phụ thuộc nhu cầu? Đây là cơ chế chung của ngành, không phải kết luận cho từng công ty. Thứ nhất, thủy điện phụ thuộc lượng '
         'nước về hồ, tức là thủy văn từng năm. Mưa nhiều thì sản lượng cao, hạn thì thấp. Thứ hai, nhiệt điện khí phụ thuộc giá khí đầu vào, mà giá khí thường gắn với giá dầu '
         'thế giới. Giá dầu Brent ngày hai tháng mười một là một trăm lẻ tám phẩy bảy bốn đô la một thùng, tăng sáu mươi bảy phẩy một phần trăm sau một năm, nhưng mình không '
         'khẳng định tác động lên từng nhà máy. Thứ ba, nhà máy được huy động bao nhiêu còn tùy hệ thống điều độ chung. Thứ tư, giá bán theo hợp đồng và theo thị trường có thể '
         'khác nhau.'},
 {'k': 'cards',
  'ch': 'Chương 3 – P O W: quý hai bứt phá, quý ba chưa có',
  'moc': True,
  'label': 'POW – Quý 2/2026',
  'cap': ('POW', 'QUÝ 2/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 2', '3.375 tỷ', 'tăng 460,3%'),
            ('Doanh thu thuần', '20.306 tỷ', 'tăng 116,1%'),
            ('Biên lợi nhuận gộp', '22,6%', 'cùng kỳ 12,4%'),
            ('Lũy kế 6 tháng', '4.575 tỷ', 'tăng 336,7%')],
  'anh': 'gas power plant Vietnam',
  'say': 'Chương ba, mã chính là P O W. Lưu ý quan trọng: trong dữ liệu mình có, P O W mới có báo cáo đến quý hai hai nghìn không trăm hai mươi sáu. Quý hai, lợi nhuận sau thuế '
         'công ty mẹ là ba nghìn ba trăm bảy mươi lăm tỷ đồng, tăng bốn trăm sáu mươi phẩy ba phần trăm so với cùng kỳ. Doanh thu hai mươi nghìn ba trăm linh sáu tỷ, tăng một '
         'trăm mười sáu phẩy một phần trăm. Biên lợi nhuận gộp hai mươi hai phẩy sáu phần trăm, so với mười hai phẩy bốn phần trăm cùng kỳ. Sáu tháng đầu năm lợi nhuận là bốn '
         'nghìn năm trăm bảy mươi lăm tỷ, tăng ba trăm ba mươi sáu phẩy bảy phần trăm. Vì sao quý hai tăng mạnh như vậy, báo cáo gốc có phần giải trình, mình không đoán thay.'},
 {'k': 'bars',
  'label': 'POW – LNST từng quý (tỷ đồng)',
  'cap': ('POW', '4 QUÝ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 809, [56, 189, 248], '809'), ('Q4/25', 570, [56, 189, 248], '570'), ('Q1/26', 1200, [34, 197, 94], '1.200'), ('Q2/26', 3375, [34, 197, 94], '3.375')],
  'anh': 'electricity pylons sunset',
  'say': 'Nhìn bốn quý gần nhất của P O W: quý ba năm ngoái tám trăm linh chín tỷ, quý bốn năm trăm bảy mươi tỷ, quý một năm nay một nghìn hai trăm tỷ, quý hai ba nghìn ba trăm '
         'bảy mươi lăm tỷ. Hai quý gần nhất tăng rất nhanh. Nhưng quý ba của P O W chưa có trong dữ liệu, nên mình chưa thể nói nhu cầu điện quý ba đã đi vào lợi nhuận P O W hay '
         'chưa. Đó là chỗ cần chờ báo cáo. Về con số quá khứ, P trên E là sáu phẩy hai chín, P trên B không phẩy chín mốt, R O E mười lăm phẩy ba phần trăm. Giá đến ngày hai mươi '
         'tám tháng mười là mười hai phẩy năm lăm, tăng chín phẩy sáu phần trăm sau một năm.'},
 {'k': 'bars',
  'ch': 'Chương 4 – N T hai và R E E đã có quý ba',
  'moc': True,
  'label': 'NT2 và REE – quý 3 và 9 tháng (%)',
  'cap': ('NT2 VÀ REE', 'TĂNG TRƯỞNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('NT2 LNST Q3', 95.4, [34, 197, 94], '+95,4%'),
           ('REE LNST Q3', 16.9, [34, 197, 94], '+16,9%'),
           ('NT2 DT Q3', 45.6, [56, 189, 248], '+45,6%'),
           ('REE DT Q3', 28.1, [56, 189, 248], '+28,1%'),
           ('NT2 LNST 9T', 57.0, [34, 197, 94], '+57,0%'),
           ('REE LNST 9T', 11.8, [34, 197, 94], '+11,8%')],
  'anh': 'thermal power plant',
  'say': 'Chương bốn: hai cái tên đã có quý ba. N T hai quý ba lãi bốn trăm mười chín tỷ, tăng chín mươi lăm phẩy bốn phần trăm. Doanh thu hai nghìn tám trăm linh bảy tỷ, tăng '
         'bốn mươi lăm phẩy sáu phần trăm. Biên lợi nhuận gộp mười bảy phẩy năm phần trăm so với mười phẩy sáu phần trăm cùng kỳ. Chín tháng N T hai lãi chín trăm linh sáu tỷ, '
         'tăng năm mươi bảy phần trăm. R E E quý ba lãi bảy trăm tám mươi tám tỷ, tăng mười sáu phẩy chín phần trăm, doanh thu ba nghìn hai trăm bảy mươi tỷ, tăng hai mươi tám '
         'phẩy một phần trăm. Nhưng biên lợi nhuận gộp ba mươi ba phẩy ba phần trăm, thấp hơn ba mươi sáu phẩy năm phần trăm cùng kỳ. Chín tháng R E E tăng mười một phẩy tám phần '
         'trăm.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Giá cổ phiếu và định giá nhìn lại',
  'moc': True,
  'label': 'Giá và định giá đến 28/10/2026',
  'cap': ('GIÁ VÀ', 'ĐỊNH GIÁ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('POW', 'P/E 6,29', 'giá 1 năm tăng 9,6%'),
            ('NT2', 'P/E 4,44, ROE 29,4%', 'giá 1 năm tăng 3,2%, 1 tháng tăng 15,7%'),
            ('REE', 'P/E 10,28, ROE 10,9%', 'giá 1 năm giảm 14,8%')],
  'anh': 'stock chart screen',
  'say': 'Chương năm. N T hai có P trên E bốn phẩy bốn bốn, R O E hai mươi chín phẩy bốn phần trăm, giá hai mươi ba phẩy không năm, tăng ba phẩy hai phần trăm sau một năm và mười '
         'lăm phẩy bảy phần trăm trong một tháng. R E E có P trên E mười phẩy hai tám, R O E mười phẩy chín phần trăm, giá bốn mươi sáu phẩy ba, giảm mười bốn phẩy tám phần trăm '
         'sau một năm. P trên E thấp ở doanh nghiệp điện có thể phản ánh lợi nhuận đang ở mức cao theo chu kỳ, nên mình không kết luận rẻ hay đắt. Đây là mô tả quá khứ, không '
         'phải dự báo.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cách đọc nhu cầu điện trong báo cáo',
  'moc': True,
  'label': 'Checklist đọc doanh nghiệp điện',
  'cap': ('CHECKLIST', 'ĐỌC NGÀNH ĐIỆN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Nhớ POW mới có đến quý 2/2026', [255, 196, 0]),
            ('Xem loại nhà máy: thủy điện hay nhiệt điện khí', [56, 189, 248]),
            ('So biên lợi nhuận gộp cùng kỳ', [34, 197, 94]),
            ('Đọc giải trình trong báo cáo gốc', [255, 255, 255])],
  'anh': 'investor reading report',
  'say': 'Chương cuối, bốn việc nên làm. Một, nhớ rằng P O W mới có đến quý hai, đừng suy ra quý ba. Hai, xem nhà máy thuộc loại nào, thủy điện hay nhiệt điện khí, vì chúng chịu '
         'tác động khác nhau. Ba, so biên lợi nhuận gộp với cùng kỳ, như N T hai cải thiện từ mười phẩy sáu lên mười bảy phẩy năm phần trăm còn R E E thu hẹp. Bốn, đọc phần giải '
         'trình trong báo cáo gốc. Trả lời câu hỏi hôm nay: nhu cầu điện tăng là nền thuận lợi, nhưng ai hưởng lợi nhiều hay ít còn phụ thuộc loại nhà máy, thủy văn và giá khí.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CỤC THỐNG KÊ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu vĩ mô: Cục Thống kê, quý ba và chín tháng hai nghìn không trăm hai mươi sáu. Số liệu doanh nghiệp: báo cáo tài chính, P O W đến quý hai, các mã còn lại '
         'đến quý ba. Đây là chia sẻ kiến thức, không phải khuyến nghị mua bán. Bạn nghĩ yếu tố nào quyết định lợi nhuận ngành điện nhiều nhất, thủy văn hay giá khí? Hãy để lại '
         'bình luận. Xem thêm tại chungkhoanhuynguyen chấm com.'}]

S['Y3_0711B'] = [{'k': 'hook',
  'ch': 'Chương 1 – Tiêu dùng tăng, lợi nhuận bán lẻ tăng bao nhiêu',
  'moc': True,
  'label': 'MWG – Thế Giới Di Động',
  'cap': ('TIÊU DÙNG TĂNG', 'LÃI BÁN LẺ?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'MWGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[14, 91.73, 'Đỉnh tuần 2/2: 91,73', 0.6], [38, 60.73, 'Đáy tuần 27/7: 60,73', 1.6], [51, 76.0, '28/10: 76,00', 2.6]]},
  'anh': 'electronics retail store Vietnam',
  'say': 'Người dân chi tiêu nhiều hơn, vậy doanh nghiệp bán lẻ lãi tăng bao nhiêu? Theo Cục Thống kê, tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng chín tháng hai '
         'nghìn không trăm hai mươi sáu tăng mười ba phẩy bốn phần trăm. Hôm nay mình nhìn M W G, D G W và nhắc ngắn F R T, để hỏi tiêu dùng tăng thì biến thành lợi nhuận như thế '
         'nào. Có một điều thú vị: doanh thu của M W G tăng ba mươi hai phần trăm, nhưng lợi nhuận tăng gấp hơn hai lần con số đó. Vì sao lại như vậy, và F R T có một con số cảnh '
         'báo ở chi phí lãi vay. Mình sẽ đi từng bước.'},
 {'k': 'cards',
  'label': 'Tiêu dùng 9 tháng 2026',
  'cap': ('TIÊU DÙNG', '9 THÁNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Bán lẻ và dịch vụ tiêu dùng', 'tăng 13,4%', 'Cục Thống kê'),
            ('Bán lẻ hàng hóa', 'tăng 12,8%', 'Cục Thống kê'),
            ('Lưu trú, ăn uống', 'tăng 16,7%', 'Cục Thống kê'),
            ('CPI bình quân 9 tháng', 'tăng 4,52%', 'Cục Thống kê')],
  'anh': 'shopping mall Vietnam',
  'say': 'Trước hết là nền vĩ mô. Theo Cục Thống kê, tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng chín tháng tăng mười ba phẩy bốn phần trăm. Riêng bán lẻ hàng hóa '
         'tăng mười hai phẩy tám phần trăm. Lưu trú và ăn uống tăng mười sáu phẩy bảy phần trăm. Còn chỉ số giá tiêu dùng bình quân chín tháng tăng bốn phẩy năm hai phần trăm, '
         'nên một phần mức tăng là do giá. Dù vậy sức mua nhìn chung vẫn tăng. Câu hỏi của chương này: sức mua tăng thì doanh nghiệp bán lẻ giữ lại được bao nhiêu?'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Từ doanh thu bán lẻ đến lợi nhuận',
  'moc': True,
  'label': 'Từ doanh thu đến lợi nhuận bán lẻ',
  'cap': ('DOANH THU', 'ĐẾN LỢI NHUẬN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Chi phí cố định: mặt bằng, nhân sự', [56, 189, 248]),
            ('Doanh thu tăng, chi phí cố định pha loãng', [34, 197, 94]),
            ('Biên lợi nhuận gộp quyết định phần giữ lại', [255, 196, 0]),
            ('Vay vốn: lãi vay ăn vào lợi nhuận', [239, 68, 68])],
  'anh': 'retail store interior',
  'say': 'Chương hai. Vì sao doanh thu tăng ba mươi mà lợi nhuận có thể tăng bảy mươi? Đây là cơ chế chung của bán lẻ, không phải kết luận riêng cho công ty nào. Cửa hàng có chi '
         'phí cố định như mặt bằng, nhân sự. Khi doanh thu tăng, chi phí cố định được chia cho nhiều đồng doanh thu hơn, lợi nhuận tăng nhanh hơn doanh thu. Thứ hai là biên lợi '
         'nhuận gộp, tức phần giữ lại sau giá vốn. Thứ ba là vay vốn: bán lẻ cần hàng tồn kho nên thường vay, và khi lãi vay tăng nhanh thì ăn vào phần lợi nhuận. Ba yếu tố này '
         'sẽ lần lượt xuất hiện trong dữ liệu.'},
 {'k': 'cards',
  'ch': 'Chương 3 – M W G: lợi nhuận tăng nhanh hơn doanh thu',
  'moc': True,
  'label': 'MWG – Quý 3/2026',
  'cap': ('MWG', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '3.094 tỷ', 'tăng 74,7%'),
            ('Doanh thu thuần', '52.614 tỷ', 'tăng 32,0%'),
            ('Biên lợi nhuận gộp', '21,7%', 'cùng kỳ 18,8%'),
            ('Lũy kế 9 tháng', '9.111 tỷ', 'tăng 83,5%')],
  'anh': 'smartphone store',
  'say': 'Chương ba, mã chính là M W G. Quý ba hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế công ty mẹ là ba nghìn không trăm chín mươi bốn tỷ đồng, tăng bảy mươi bốn '
         'phẩy bảy phần trăm so với cùng kỳ. Doanh thu thuần năm mươi hai nghìn sáu trăm mười bốn tỷ, tăng ba mươi hai phần trăm. Biên lợi nhuận gộp hai mươi mốt phẩy bảy phần '
         'trăm, so với mười tám phẩy tám phần trăm cùng kỳ. Lũy kế chín tháng chín nghìn một trăm mười một tỷ, tăng tám mươi ba phẩy năm phần trăm. Đúng như cơ chế: doanh thu '
         'tăng, biên gộp cải thiện, lợi nhuận tăng nhanh hơn doanh thu. Nhưng có một chi tiết: lợi nhuận quý ba thấp hơn quý hai là ba nghìn ba trăm linh hai tỷ.'},
 {'k': 'bars',
  'label': 'MWG – LNST từng quý (tỷ đồng)',
  'cap': ('MWG', '6 QUÝ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q2/25', 1648, [56, 189, 248], '1.648'),
           ('Q3/25', 1771, [56, 189, 248], '1.771'),
           ('Q4/25', 2069, [56, 189, 248], '2.069'),
           ('Q1/26', 2714, [56, 189, 248], '2.714'),
           ('Q2/26', 3302, [34, 197, 94], '3.302'),
           ('Q3/26', 3094, [255, 196, 0], '3.094')],
  'anh': 'electronics store customers',
  'say': 'Nhìn sáu quý của M W G. Quý hai năm ngoái một nghìn sáu trăm bốn mươi tám tỷ. Quý ba một nghìn bảy trăm bảy mươi mốt tỷ. Quý bốn hai nghìn không trăm sáu mươi chín tỷ. '
         'Quý một năm nay hai nghìn bảy trăm mười bốn tỷ. Quý hai ba nghìn ba trăm linh hai tỷ. Quý ba ba nghìn không trăm chín mươi bốn tỷ. Năm quý liền đi lên, rồi quý ba lùi '
         'nhẹ so với quý hai. Giá đến ngày hai mươi tám tháng mười là bảy mươi sáu, giảm bảy phẩy một phần trăm sau một năm nhưng tăng mười lăm phẩy tám phần trăm trong ba tháng. '
         'P trên E chín phẩy bảy bảy, R O E hai mươi chín phẩy năm phần trăm.'},
 {'k': 'bars',
  'ch': 'Chương 4 – D G W và F R T: lãi vay là phần đáng chú ý',
  'moc': True,
  'label': 'Doanh thu, LNST và lãi vay quý 3/2026 (%)',
  'cap': ('DGW – FRT', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('DGW LNST', 65.9, [34, 197, 94], '+65,9%'),
           ('DGW lãi vay', 42.2, [239, 68, 68], '+42,2%'),
           ('FRT LNST', 101.3, [34, 197, 94], '+101,3%'),
           ('FRT lãi vay', 157.4, [239, 68, 68], '+157,4%')],
  'anh': 'warehouse distribution logistics',
  'say': 'Chương bốn. D G W quý ba lãi hai trăm bảy mươi sáu tỷ, tăng sáu mươi lăm phẩy chín phần trăm. Doanh thu mười một nghìn không trăm hai mươi hai tỷ, tăng bốn mươi chín '
         'phẩy một phần trăm. Chín tháng lãi bảy trăm tám mươi sáu tỷ, tăng một trăm linh hai phẩy năm phần trăm. Chi phí lãi vay của D G W tăng bốn mươi hai phẩy hai phần trăm. '
         'Nhắc ngắn F R T: lợi nhuận quý ba bốn trăm bốn mươi tỷ, tăng một trăm linh một phẩy ba phần trăm, nhưng chi phí lãi vay tăng một trăm năm mươi bảy phẩy bốn phần trăm, '
         'nhanh hơn lợi nhuận. Lãi vay tăng nhanh hơn lãi thường là điểm cần xem ở báo cáo gốc.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Giá cổ phiếu và định giá nhìn lại',
  'moc': True,
  'label': 'Giá và định giá đến 28/10/2026',
  'cap': ('GIÁ VÀ', 'ĐỊNH GIÁ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('MWG', 'P/E 9,77', 'giá 1 năm giảm 7,1%'), ('DGW', 'P/E 9,58, ROE 26,9%', 'giá 1 năm tăng 10,7%'), ('FRT', 'P/E 23,38', 'giá 1 năm tăng 4,3%')],
  'anh': 'stock exchange display',
  'say': 'Chương năm. D G W có P trên E chín phẩy năm tám, R O E hai mươi sáu phẩy chín phần trăm, giá bốn mươi hai phẩy ba lăm, tăng mười phẩy bảy phần trăm sau một năm. F R T '
         'có P trên E hai mươi ba phẩy ba tám và giá một trăm bốn mươi bảy, tăng bốn phẩy ba phần trăm sau một năm. Mỗi doanh nghiệp có mức P trên E khác nhau dù cùng hưởng sức '
         'mua. Mình chỉ mô tả dữ liệu quá khứ, không dự báo giá.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cách đọc lợi nhuận bán lẻ',
  'moc': True,
  'label': 'Checklist đọc doanh nghiệp bán lẻ',
  'cap': ('CHECKLIST', 'ĐỌC BÁN LẺ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('So tốc độ tăng lợi nhuận với doanh thu', [255, 196, 0]),
            ('Xem biên lợi nhuận gộp cùng kỳ', [56, 189, 248]),
            ('Xem chi phí lãi vay', [239, 68, 68]),
            ('Nhìn nhiều quý, không chỉ một quý', [34, 197, 94])],
  'anh': 'investor reading report',
  'say': 'Chương cuối, bốn việc nên làm. Một, so tốc độ tăng lợi nhuận với doanh thu, như M W G có lợi nhuận tăng bảy mươi bốn phẩy bảy phần trăm trong khi doanh thu tăng ba mươi '
         'hai phần trăm. Hai, xem biên lợi nhuận gộp cùng kỳ. Ba, xem chi phí lãi vay, đặc biệt F R T tăng một trăm năm mươi bảy phẩy bốn phần trăm. Bốn, nhìn nhiều quý, vì M W G '
         'quý ba lùi nhẹ so với quý hai. Trả lời câu hỏi hôm nay: tiêu dùng tăng giúp doanh thu, nhưng phần lợi nhuận giữ lại còn phụ thuộc biên gộp và chi phí vay.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CỤC THỐNG KÊ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu vĩ mô: Cục Thống kê, chín tháng hai nghìn không trăm hai mươi sáu. Số liệu doanh nghiệp: báo cáo tài chính quý ba hai nghìn không trăm hai mươi sáu. Đây '
         'là chia sẻ kiến thức, không phải khuyến nghị mua bán. Bạn nghĩ lãi vay hay biên gộp quan trọng hơn khi đọc doanh nghiệp bán lẻ? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0711C'] = [{'k': 'hook',
  'ch': 'Chương 1 – Du lịch tăng, vì sao hãng bay chưa lãi theo',
  'moc': True,
  'label': 'VJC – Vietjet',
  'cap': ('DU LỊCH TĂNG', 'HÃNG BAY?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'VJCW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[4, 169.22, 'Đỉnh tuần 24/11: 169,22', 0.6], [18, 111.92, 'Đáy tuần 9/3: 111,92', 1.6], [51, 131.5, '28/10: 131,50', 2.6]]},
  'anh': 'airplane airport Vietnam',
  'say': 'Du lịch đang tăng mạnh, vậy hãng bay phải lãi đậm chứ? Theo Cục Thống kê, chín tháng hai nghìn không trăm hai mươi sáu, doanh thu lưu trú và ăn uống tăng mười sáu phẩy '
         'bảy phần trăm, lữ hành tăng mười bảy phẩy chín phần trăm. Nhưng báo cáo mới nhất mà mình có của hai hãng bay V J C và H V N, là quý hai, lại cho thấy lợi nhuận không '
         'tăng theo. H V N thậm chí lỗ bảy trăm chín mươi hai tỷ đồng. Vì sao cầu du lịch tăng mà lợi nhuận hãng bay không tăng theo? Hôm nay mình giải thích bằng nhiên liệu, tỷ '
         'giá và cơ chế chung.'},
 {'k': 'cards',
  'label': 'Du lịch 9 tháng 2026',
  'cap': ('DU LỊCH', '9 THÁNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Lưu trú, ăn uống', 'tăng 16,7%', 'Cục Thống kê'),
            ('Lữ hành', 'tăng 17,9%', 'Cục Thống kê'),
            ('Bán lẻ và dịch vụ tiêu dùng', 'tăng 13,4%', 'Cục Thống kê'),
            ('Dịch vụ khác', 'tăng 13,4%', 'Cục Thống kê')],
  'anh': 'tourists Vietnam beach hotel',
  'say': 'Bắt đầu từ cầu. Theo Cục Thống kê, chín tháng doanh thu lưu trú và ăn uống tăng mười sáu phẩy bảy phần trăm, lữ hành tăng mười bảy phẩy chín phần trăm, cao hơn mức tăng '
         'mười ba phẩy bốn phần trăm của toàn bộ bán lẻ và dịch vụ tiêu dùng. Nhìn vào đó, ngành du lịch rõ ràng đang có nhu cầu. Câu hỏi: cầu du lịch tăng thì doanh thu hãng bay '
         'có tăng không, và doanh thu tăng thì lợi nhuận có tăng không? Hai câu này có hai câu trả lời khác nhau.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Doanh thu tăng nhưng lợi nhuận quý 2 giảm',
  'moc': True,
  'label': 'VJC và HVN – Quý 2/2026',
  'cap': ('VJC – HVN', 'QUÝ 2/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('VJC – Doanh thu', '30.514 tỷ', 'tăng 70,6%'),
            ('VJC – LNST quý 2', '334 tỷ', 'giảm 48,8%'),
            ('HVN – Doanh thu', '38.303 tỷ', 'tăng 36,8%'),
            ('HVN – LNST quý 2', 'lỗ 792 tỷ', 'quý 1 lãi 4.388 tỷ'),
            ('Biên gộp VJC', '5,6%', 'cùng kỳ 13,5%'),
            ('Biên gộp HVN', '4,2%', 'cùng kỳ 17,6%')],
  'anh': 'airline aircraft maintenance',
  'say': 'Chương hai, nhìn thẳng vào dữ liệu. Lưu ý: cả hai hãng chỉ có đến quý hai hai nghìn không trăm hai mươi sáu. V J C quý hai doanh thu ba mươi nghìn năm trăm mười bốn tỷ, '
         'tăng bảy mươi phẩy sáu phần trăm, nhưng lợi nhuận chỉ ba trăm ba mươi bốn tỷ, giảm bốn mươi tám phẩy tám phần trăm so với cùng kỳ. Biên lợi nhuận gộp năm phẩy sáu phần '
         'trăm, so với mười ba phẩy năm phần trăm cùng kỳ. H V N doanh thu ba mươi tám nghìn ba trăm linh ba tỷ, tăng ba mươi sáu phẩy tám phần trăm, nhưng quý hai lỗ bảy trăm '
         'chín mươi hai tỷ, trong khi quý một lãi bốn nghìn ba trăm tám mươi tám tỷ. Biên gộp bốn phẩy hai phần trăm, so với mười bảy phẩy sáu phần trăm.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Cơ chế chung: nhiên liệu và tỷ giá',
  'moc': True,
  'label': 'Vì sao doanh thu tăng mà lãi không tăng',
  'cap': ('CƠ CHẾ', 'HÃNG BAY'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Nhiên liệu là khoản chi lớn của hãng bay', [239, 68, 68]),
            ('Giá dầu tăng thì giá vốn tăng', [239, 68, 68]),
            ('Máy bay thuê, vay bằng đô la: nhạy tỷ giá', [56, 189, 248]),
            ('Doanh thu tăng chưa chắc biên gộp tăng', [255, 196, 0])],
  'anh': 'jet fuel airplane refuel',
  'say': 'Chương ba, cơ chế chung. Mình nhấn mạnh: đây là cơ chế của ngành, không phải kết luận nguyên nhân cho V J C hay H V N, vì nguyên nhân cụ thể nằm trong phần giải trình '
         'báo cáo gốc. Thứ nhất, nhiên liệu là một khoản chi rất lớn của hãng bay, nên giá dầu tăng thì giá vốn thường tăng. Thứ hai, nhiều chi phí như thuê hoặc vay mua máy bay '
         'tính bằng đô la, nên tỷ giá ảnh hưởng chi phí quy ra đồng. Thứ ba, doanh thu tăng không có nghĩa biên lợi nhuận tăng: bán nhiều vé hơn nhưng chi phí mỗi chuyến bay cũng '
         'tăng thì phần giữ lại có thể mỏng đi. Dữ liệu biên gộp ở chương trước đúng với hình dạng đó.'},
 {'k': 'bars',
  'label': 'Giá dầu Brent cuối kỳ (USD/thùng)',
  'cap': ('DẦU BRENT', '2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Cuối 1/26', 60.7, [56, 189, 248], '60,70'),
           ('Cuối 3/26', 92.69, [255, 196, 0], '92,69'),
           ('Cuối 4/26', 109.27, [239, 68, 68], '109,27'),
           ('Cuối 6/26', 93.09, [255, 196, 0], '93,09'),
           ('Cuối 8/26', 79.45, [56, 189, 248], '79,45'),
           ('Cuối 10/26', 102.25, [239, 68, 68], '102,25'),
           ('2/11/26', 108.74, [239, 68, 68], '108,74')],
  'anh': 'oil refinery',
  'say': 'Thử nhìn đường giá dầu Brent trong năm. Cuối tháng một sáu mươi phẩy bảy đô la một thùng. Cuối tháng ba chín mươi hai phẩy sáu chín. Cuối tháng tư một trăm linh chín '
         'phẩy hai bảy. Cuối tháng sáu chín mươi ba phẩy không chín. Cuối tháng tám bảy mươi chín phẩy bốn lăm. Cuối tháng mười một trăm linh hai phẩy hai lăm. Và ngày hai tháng '
         'mười một là một trăm lẻ tám phẩy bảy bốn, tăng sáu mươi bảy phẩy một phần trăm sau một năm. Đỉnh một năm là một trăm mười tám phẩy ba lăm ngày ba mươi tháng ba. Đây là '
         'bối cảnh giá nhiên liệu thế giới, mình không gán một con số nào là nguyên nhân lợi nhuận quý hai.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Tỷ giá, giá cổ phiếu và định giá',
  'moc': True,
  'label': 'Giá và định giá đến 28/10/2026',
  'cap': ('GIÁ VÀ', 'ĐỊNH GIÁ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('VJC', 'P/E 46,49, ROE 8,7%', 'giá 1 năm giảm 8,8%'), ('HVN', 'P/E 14,2', 'giá 1 năm giảm 37,0%'), ('USD/VND', '25.802', '1 năm giảm 1,9%')],
  'anh': 'stock market Vietnam',
  'say': 'Chương bốn. Về tỷ giá, ngày hai tháng mười một tỷ giá đô la so với đồng ở mức hai mươi lăm nghìn tám trăm linh hai, giảm một phẩy chín phần trăm sau một năm. Mình chỉ '
         'nêu số, không khẳng định tác động đến báo cáo quý hai. Về giá, đến ngày hai mươi tám tháng mười, V J C ở mức một trăm ba mươi mốt phẩy năm, giảm tám phẩy tám phần trăm '
         'sau một năm, P trên E bốn mươi sáu phẩy bốn chín, R O E tám phẩy bảy phần trăm. H V N ở mức hai mươi phẩy tám lăm, giảm ba mươi bảy phần trăm sau một năm, P trên E mười '
         'bốn phẩy hai. Quý hai chưa phải quý ba, nên các hệ số này sẽ thay đổi khi báo cáo mới ra.'},
 {'k': 'bars',
  'label': 'HVN và VJC – LNST từng quý (tỷ đồng)',
  'cap': ('HVN – VJC', 'LNST QUÝ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('HVN Q3/25', 617, [56, 189, 248], '617'),
           ('HVN Q4/25', 330, [56, 189, 248], '330'),
           ('HVN Q1/26', 4388, [34, 197, 94], '4.388'),
           ('HVN Q2/26', -792, [239, 68, 68], '−792'),
           ('VJC Q1/26', 1014, [34, 197, 94], '1.014'),
           ('VJC Q2/26', 334, [255, 196, 0], '334')],
  'anh': 'airport terminal Vietnam',
  'say': 'Nhìn lại lợi nhuận từng quý. H V N quý ba năm ngoái sáu trăm mười bảy tỷ, quý bốn ba trăm ba mươi tỷ, quý một năm nay bốn nghìn ba trăm tám mươi tám tỷ, quý hai âm bảy '
         'trăm chín mươi hai tỷ. V J C quý một một nghìn không trăm mười bốn tỷ, quý hai ba trăm ba mươi bốn tỷ, giảm sáu mươi bảy phẩy một phần trăm so với quý một. Lợi nhuận '
         'hãng bay biến động mạnh giữa các quý. Sáu tháng đầu năm V J C vẫn tăng bốn phẩy hai phần trăm, còn H V N giảm bốn mươi hai phẩy năm phần trăm.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Cách đọc cầu du lịch và hãng bay',
  'moc': True,
  'label': 'Checklist đọc hãng bay',
  'cap': ('CHECKLIST', 'ĐỌC HÃNG BAY'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Cầu du lịch tăng không đồng nghĩa lãi hãng bay tăng', [255, 196, 0]),
            ('Xem biên lợi nhuận gộp, không chỉ doanh thu', [56, 189, 248]),
            ('Nhớ VJC, HVN mới có đến quý 2', [239, 68, 68]),
            ('Đọc giải trình báo cáo gốc về nhiên liệu, tỷ giá', [34, 197, 94])],
  'anh': 'investor analyzing airline report',
  'say': 'Chương cuối, bốn việc nên làm. Một, đừng suy từ cầu du lịch sang lợi nhuận hãng bay, hai thứ này cách nhau bởi chi phí. Hai, xem biên lợi nhuận gộp chứ không chỉ doanh '
         'thu. Ba, nhớ rằng dữ liệu hãng bay mới đến quý hai, quý ba có thể khác. Bốn, đọc phần giải trình về nhiên liệu và tỷ giá trong báo cáo gốc. Trả lời câu hỏi hôm nay: cầu '
         'du lịch tăng mười sáu đến mười tám phần trăm là tín hiệu tốt cho doanh thu, nhưng lợi nhuận hãng bay còn phụ thuộc nhiều vào chi phí nhiên liệu, tỷ giá và cách vận '
         'hành.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'CỤC THỐNG KÊ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu vĩ mô: Cục Thống kê, chín tháng hai nghìn không trăm hai mươi sáu. Số liệu hãng bay: báo cáo tài chính quý hai hai nghìn không trăm hai mươi sáu. Giá dầu: '
         'dữ liệu thị trường ngày hai tháng mười một. Đây là chia sẻ kiến thức, không phải khuyến nghị mua bán. Bạn nghĩ nhiên liệu hay tỷ giá ảnh hưởng hãng bay nhiều hơn? Hãy '
         'để lại bình luận. Xem thêm tại chungkhoanhuynguyen chấm com.'}]

S['Y3_0811A'] = [{'k': 'hook',
  'ch': 'Chương 1 – Nasdaq giảm, cổ phiếu công nghệ Việt lệch pha',
  'moc': True,
  'label': 'FPT – FPT Corporation',
  'cap': ('NASDAQ GIẢM', 'FPT LỆCH PHA'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'FPTW', 'tf': 'W', 'weeks': 52, 'circles': [[12, 97.48, 'Đỉnh tuần 19/1: 97,48', 0.6], [51, 54.0, '28/10: 54,00', 1.6]]},
  'anh': 'software company technology office',
  'say': 'Lợi nhuận tăng nhưng giá cổ phiếu giảm hơn bốn mươi phần trăm, vì sao? Trong một tháng, chỉ số Nasdaq của Mỹ giảm năm phẩy ba phần trăm, và phiên ba mươi tháng mười chỉ '
         'số S và P năm trăm giảm một phẩy tám hai phần trăm. Ở Việt Nam, giá F P T giảm bốn mươi phẩy năm phần trăm sau một năm, về năm mươi tư, mức thấp nhất một năm vào ngày '
         'hai mươi tám tháng mười. Thế nhưng lợi nhuận chín tháng của F P T lại tăng mười ba phẩy ba phần trăm. Hôm nay mình đặt câu hỏi, chứ chưa đưa ra câu trả lời, vì sao giá '
         'và lợi nhuận lệch nhau, và chỉ nhìn vào dữ liệu cùng P trên E.'},
 {'k': 'cards',
  'label': 'Thế giới: chứng khoán Mỹ',
  'cap': ('CHỨNG KHOÁN', 'MỸ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Nasdaq 1 tháng', 'giảm 5,3%', '25.437 điểm'),
            ('S&P 500 phiên 30/10', 'giảm 1,82%', '7.580,07 điểm'),
            ('Nasdaq phiên 30/10', 'giảm 2,86%', '25.437 điểm'),
            ('Nasdaq 1 năm', 'tăng 7,9%', 'đỉnh 27.599,79')],
  'anh': 'Nasdaq stock exchange New York',
  'say': 'Trước hết là bối cảnh thế giới. Chỉ số Nasdaq đóng cửa ngày ba mươi tháng mười ở hai mươi lăm nghìn bốn trăm ba mươi bảy điểm, giảm năm phẩy ba phần trăm trong một '
         'tháng, nhưng vẫn tăng bảy phẩy chín phần trăm sau một năm. Riêng phiên ba mươi tháng mười, Nasdaq giảm hai phẩy tám sáu phần trăm, S và P năm trăm giảm một phẩy tám hai '
         'phần trăm, còn Dow Jones giảm một phẩy không chín phần trăm. Kênh tự tính tương quan lợi suất tháng của VN-Index với Nasdaq khoảng không phẩy năm, từ tháng mười một hai '
         'nghìn không trăm hai mươi ba đến tháng mười năm nay. Đó là tương quan, không phải quan hệ nguyên nhân.'},
 {'k': 'cards',
  'ch': 'Chương 2 – F P T: giá giảm sâu, lợi nhuận vẫn tăng',
  'moc': True,
  'label': 'FPT – Quý 3/2026',
  'cap': ('FPT', 'QUÝ 3/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '2.723 tỷ', 'tăng 11,8%'),
            ('Lũy kế 9 tháng', '7.778 tỷ', 'tăng 13,3%'),
            ('Giá 28/10', '54,00', 'mức thấp nhất 1 năm'),
            ('Giá 1 năm', 'giảm 40,5%', 'đỉnh 95,14 ngày 29/1/2026')],
  'anh': 'technology company Vietnam office',
  'say': 'Chương hai, mã chính F P T. Quý ba hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế công ty mẹ là hai nghìn bảy trăm hai mươi ba tỷ đồng, tăng mười một phẩy tám '
         'phần trăm so với cùng kỳ. Lũy kế chín tháng bảy nghìn bảy trăm bảy mươi tám tỷ, tăng mười ba phẩy ba phần trăm. Còn giá cổ phiếu ngày hai mươi tám tháng mười là năm '
         'mươi tư, giảm bốn mươi phẩy năm phần trăm sau một năm, giảm mười lăm phẩy hai phần trăm trong một tháng. Đỉnh một năm là chín mươi lăm phẩy một bốn ngày hai mươi chín '
         'tháng một. Giá giảm sâu trong khi lợi nhuận vẫn tăng, đó là điều khiến câu hỏi trở nên đáng chú ý.'},
 {'k': 'bars',
  'label': 'FPT – LNST từng quý (tỷ đồng)',
  'cap': ('FPT', '5 QUÝ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 2435, [56, 189, 248], '2.435'),
           ('Q4/25', 2510, [56, 189, 248], '2.510'),
           ('Q1/26', 2487, [56, 189, 248], '2.487'),
           ('Q2/26', 2568, [56, 189, 248], '2.568'),
           ('Q3/26', 2723, [34, 197, 94], '2.723')],
  'anh': 'data center servers',
  'say': 'Nhìn năm quý gần nhất của F P T. Quý ba năm ngoái hai nghìn bốn trăm ba mươi lăm tỷ. Quý bốn hai nghìn năm trăm mười tỷ. Quý một năm nay hai nghìn bốn trăm tám mươi bảy '
         'tỷ. Quý hai hai nghìn năm trăm sáu mươi tám tỷ. Quý ba hai nghìn bảy trăm hai mươi ba tỷ. Lợi nhuận đi tương đối đều quanh mức hai nghìn năm trăm tỷ rồi nhích lên. '
         'Trong khi đó giá đi xuống. Về định giá, P trên E hiện là chín phẩy sáu sáu, P trên B hai phẩy ba hai, R O E hai mươi bốn phẩy ba phần trăm. Mình chỉ nêu số, không nói '
         'giá đúng hay sai.'},
 {'k': 'cards',
  'ch': 'Chương 3 – C M G: cũng giảm giá, nhưng lợi nhuận yếu hơn',
  'moc': True,
  'label': 'CMG – Quý 2/2026',
  'cap': ('CMG', 'QUÝ 2/2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 2', '75 tỷ', 'giảm 20,3%'),
            ('Lũy kế 6 tháng', '169 tỷ', 'giảm 2,7%'),
            ('Doanh thu quý 2', '2.323 tỷ', 'tăng 5,1%'),
            ('Chi phí lãi vay', 'tăng 48,3%', 'ăn vào lợi nhuận'),
            ('Giá 1 năm', 'giảm 47,2%', '19,05, thấp nhất 1 năm')],
  'anh': 'IT services company',
  'say': 'Chương ba, nhìn C M G. Lưu ý: C M G mới có báo cáo đến quý hai hai nghìn không trăm hai mươi sáu. Quý hai, lợi nhuận sau thuế công ty mẹ là bảy mươi lăm tỷ đồng, giảm '
         'hai mươi phẩy ba phần trăm so với cùng kỳ. Doanh thu hai nghìn ba trăm hai mươi ba tỷ, tăng năm phẩy một phần trăm. Chi phí lãi vay tăng bốn mươi tám phẩy ba phần trăm. '
         'Lũy kế sáu tháng một trăm sáu mươi chín tỷ, giảm hai phẩy bảy phần trăm. Giá ngày hai mươi tám tháng mười là mười chín phẩy không năm, giảm bốn mươi bảy phẩy hai phần '
         'trăm sau một năm, cũng là mức thấp nhất một năm. Ở C M G, lợi nhuận yếu đi cùng với giá giảm.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Hai câu chuyện khác nhau trong cùng một ngành',
  'moc': True,
  'label': 'FPT và CMG – giá và lợi nhuận (%)',
  'cap': ('FPT VÀ CMG', 'GIÁ – LỢI NHUẬN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('FPT giá 1 năm', -40.5, [239, 68, 68], '−40,5%'),
           ('FPT LNST 9T', 13.3, [34, 197, 94], '+13,3%'),
           ('CMG giá 1 năm', -47.2, [239, 68, 68], '−47,2%'),
           ('CMG LNST 6T', -2.7, [239, 68, 68], '−2,7%'),
           ('CMG LNST Q2', -20.3, [239, 68, 68], '−20,3%')],
  'anh': 'stock chart decline',
  'say': 'Chương bốn, đặt hai mã cạnh nhau. F P T giá giảm bốn mươi phẩy năm phần trăm, lợi nhuận chín tháng tăng mười ba phẩy ba phần trăm: giá và lợi nhuận đi hai hướng. C M G '
         'giá giảm bốn mươi bảy phẩy hai phần trăm, lợi nhuận quý hai giảm hai mươi phẩy ba phần trăm, lũy kế sáu tháng giảm hai phẩy bảy phần trăm: hai đại lượng cùng đi xuống. '
         'Vậy vì sao giá và lợi nhuận lệch nhau ở F P T? Mình không khẳng định nguyên nhân. Gói dữ liệu không chứa lời giải thích, nên câu hỏi vẫn để mở.'},
 {'k': 'cards',
  'ch': 'Chương 5 – P trên E, P trên B và R O E nhìn lại',
  'moc': True,
  'label': 'Định giá theo dữ liệu',
  'cap': ('P/E', 'P/B – ROE'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('FPT', 'P/E 9,66', 'P/B 2,32, ROE 24,3%'), ('CMG', 'P/E 10,94', 'P/B 1,29, ROE 9,9%')],
  'anh': 'financial analyst desk',
  'say': 'Chương năm. F P T có P trên E chín phẩy sáu sáu, P trên B hai phẩy ba hai, R O E hai mươi bốn phẩy ba phần trăm. C M G có P trên E mười phẩy chín bốn, P trên B một phẩy '
         'hai chín, R O E chín phẩy chín phần trăm. P trên E của hai mã khá gần nhau, nhưng R O E khác nhau rõ: hai mươi bốn phẩy ba so với chín phẩy chín phần trăm. Đây chỉ là '
         'dữ liệu quá khứ, mình không kết luận cổ phiếu nào đắt hay rẻ.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cách đọc khi giá và lợi nhuận lệch nhau',
  'moc': True,
  'label': 'Checklist khi giá lệch lợi nhuận',
  'cap': ('CHECKLIST', 'GIÁ LỆCH LÃI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Đặt câu hỏi trước, đừng vội kết luận nguyên nhân', [255, 196, 0]),
            ('So P/E với lợi nhuận bốn quý gần nhất', [56, 189, 248]),
            ('Phân biệt dữ liệu quý 3 với quý 2', [239, 68, 68]),
            ('Đọc báo cáo gốc và giải trình', [34, 197, 94])],
  'anh': 'investor reading report',
  'say': 'Chương cuối, bốn việc nên làm khi giá và lợi nhuận lệch nhau. Một, đặt câu hỏi trước, đừng vội gán nguyên nhân. Hai, nhìn P trên E cùng với lợi nhuận bốn quý gần nhất. '
         'Ba, phân biệt dữ liệu quý ba với quý hai: F P T có quý ba, C M G mới có quý hai. Bốn, đọc báo cáo gốc và phần giải trình. Trả lời câu hỏi hôm nay: dữ liệu cho thấy F P '
         'T giá giảm bốn mươi phẩy năm phần trăm trong khi lợi nhuận chín tháng tăng mười ba phẩy ba phần trăm, và mình chưa có đủ thông tin để nói vì sao. Chúng ta tiếp tục theo '
         'dõi khi có báo cáo mới.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN', 'SỐ LIỆU THẾ GIỚI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn số liệu: chỉ số Mỹ phiên ba mươi tháng mười, báo cáo tài chính của doanh nghiệp, F P T đến quý ba, C M G đến quý hai hai nghìn không trăm hai mươi sáu. Đây là '
         'chia sẻ kiến thức, không phải khuyến nghị mua bán. Bạn nghĩ khi giá giảm mà lợi nhuận vẫn tăng, nhà đầu tư nên hỏi điều gì đầu tiên? Hãy để lại bình luận. Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0811B'] = [{'k': 'hook',
  'ch': 'Chương 1 – Rủi ro toàn cầu và chứng khoán',
  'moc': True,
  'label': 'SSI – Chứng khoán SSI',
  'cap': ('KHẨU VỊ', 'RỦI RO'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'SSIW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[17, 27.98, 'Đỉnh tuần 2/3: 27,98', 0.6], [38, 17.34, 'Đáy tuần 27/7: 17,34', 1.6], [51, 19.75, '28/10: 19,75', 2.6]]},
  'anh': 'Bitcoin coin chart',
  'say': 'Theo số liệu ngày hai tháng mười một, Bitcoin đang quanh bảy mươi bảy nghìn tám trăm năm mươi lăm đô la. Một tháng giảm tám phẩy hai phần trăm, một năm giảm hai mươi '
         'chín phẩy sáu phần trăm, so với mức cao nhất trong một năm là một trăm mười nghìn sáu trăm bốn mươi đô la, ghi nhận ngày hai tháng mười một năm hai nghìn không trăm hai '
         'mươi lăm. Nasdaq cũng giảm năm phẩy ba phần trăm trong một tháng. Khi hai thước đo khẩu vị rủi ro cùng yếu đi, một câu hỏi xuất hiện. Liệu điều đó có chạm tới lợi nhuận '
         'các công ty chứng khoán không? Chào bạn, đây là kênh Vĩ Mô Chứng Khoán Dễ Hiểu. Hôm nay mình đi từ khẩu vị rủi ro toàn cầu đến báo cáo quý ba của sáu công ty: S S I, V '
         'N D, H C M, V C I, F T S và T C X.'},
 {'k': 'cards',
  'label': 'THẾ GIỚI – KHẨU VỊ RỦI RO',
  'cap': ('RỦI RO', 'TOÀN CẦU'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Bitcoin', '77.855 USD', '−8,2% / 1 tháng'),
            ('Bitcoin 1 năm', '−29,6%', 'Đỉnh 1 năm 110.640 USD'),
            ('Nasdaq', '25.437 điểm', '−5,3% / 1 tháng'),
            ('S&P 500', '7.580 điểm', '−0,9% / 1 tháng')],
  'anh': 'stock market trading screen',
  'say': 'Khẩu vị rủi ro là mức độ nhà đầu tư sẵn lòng cầm những tài sản biến động mạnh. Bitcoin và Nasdaq phản ánh khá rõ. Bitcoin giảm tám phẩy hai phần trăm một tháng, Nasdaq '
         'giảm năm phẩy ba, còn S và P năm trăm giảm nhẹ hơn, không phẩy chín phần trăm. Bức tranh là phân hóa, chưa phải sụp đổ. Mình nhấn mạnh: đây là số liệu quá khứ, kênh '
         'không dự báo giá hay lợi nhuận.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Công ty chứng khoán kiếm tiền từ đâu',
  'moc': True,
  'label': '3 NGUỒN THU CHÍNH',
  'cap': ('CƠ CHẾ', 'CHUNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Phí giao dịch: theo thanh khoản', [56, 189, 248]),
            ('Cho vay ký quỹ: lãi trên dư nợ', [34, 197, 94]),
            ('Tự doanh: lãi lỗ theo giá thị trường', [255, 196, 0]),
            ('Mỗi nguồn phản ứng một nhịp khác', [239, 68, 68])],
  'anh': 'stock exchange trading floor',
  'say': 'Chương hai. Công ty chứng khoán kiếm tiền từ đâu? Đây là cơ chế chung, không phải nguyên nhân riêng của công ty nào. Nguồn thứ nhất là phí giao dịch: thanh khoản lớn '
         'thì phí nhiều, thanh khoản mỏng thì phí giảm. Nguồn thứ hai là cho vay ký quỹ: nhà đầu tư vay mua cổ phiếu, công ty thu lãi trên dư nợ. Nguồn thứ ba là tự doanh: công '
         'ty đầu tư bằng vốn của mình, nên lãi lỗ theo giá thị trường. Ba nguồn này phản ứng khác nhau, nên kết quả sáu công ty không giống nhau.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Bức tranh quý 3 của sáu công ty',
  'moc': True,
  'label': 'LNST QUÝ 3/2026 SO CÙNG KỲ',
  'cap': ('LỢI NHUẬN', 'QUÝ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('SSI', -23.7, [239, 68, 68], '−23,7%'),
           ('VND', -64.5, [239, 68, 68], '−64,5%'),
           ('HCM', -32.5, [239, 68, 68], '−32,5%'),
           ('VCI', -12.6, [239, 68, 68], '−12,6%'),
           ('FTS', -35.0, [239, 68, 68], '−35,0%'),
           ('TCX', 7.9, [34, 197, 94], '+7,9%')],
  'anh': 'securities company office Vietnam',
  'say': 'Chương ba. Lợi nhuận sau thuế công ty mẹ quý ba so với cùng kỳ. S S I giảm hai mươi ba phẩy bảy phần trăm. V N D giảm sáu mươi bốn phẩy năm. H C M giảm ba mươi hai phẩy '
         'năm. V C I giảm mười hai phẩy sáu. F T S giảm ba mươi lăm phẩy không. Chỉ T C X tăng bảy phẩy chín phần trăm. Nhưng hãy chú ý nền so sánh: quý ba năm hai nghìn không '
         'trăm hai mươi lăm, V N D lãi chín trăm hai mươi chín tỷ và S S I lãi một nghìn bốn trăm bảy mươi lăm tỷ, đều là mức cao nhất trong chuỗi tám quý. Một phần mức giảm đến '
         'từ nền cùng kỳ cao.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Ba mã chính: SSI, VND, HCM',
  'moc': True,
  'label': 'SSI – LỢI NHUẬN & GIÁ',
  'cap': ('SSI', 'QUÝ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '1.125 tỷ', '−23,7% cùng kỳ'),
            ('Lũy kế 9 tháng', '3.634 tỷ', '+14,2%'),
            ('Phí giao dịch', '−62,1%', 'doanh thu quý 3'),
            ('Giá 1 năm', '−24,3%', 'P/E 13,01 đến 28/10')],
  'anh': 'Ho Chi Minh City skyline',
  'say': 'Chương bốn. Ba mã chính, bắt đầu với S S I. Lợi nhuận quý ba là một nghìn một trăm hai mươi lăm tỷ, giảm hai mươi ba phẩy bảy phần trăm, nhưng cộng chín tháng vẫn đạt '
         'ba nghìn sáu trăm ba mươi bốn tỷ, tăng mười bốn phẩy hai phần trăm. Quý yếu nằm trong một năm chưa hề xấu. Dữ liệu ghi doanh thu phí giao dịch giảm sáu mươi hai phẩy '
         'một phần trăm và lợi nhuận phụ thuộc nhiều vào tự doanh, nên lợi nhuận từng quý nhấp nhô mạnh. Giá một năm giảm hai mươi bốn phẩy ba phần trăm đến ngày hai mươi tám '
         'tháng mười, P trên E mười ba phẩy không một, chỉ là mô tả quá khứ.'},
 {'k': 'bars',
  'label': 'VND – LNST 5 QUÝ GẦN NHẤT (TỶ ĐỒNG)',
  'cap': ('VND', 'CHUỖI QUÝ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 929, [56, 189, 248], '929'),
           ('Q4/25', 342, [56, 189, 248], '342'),
           ('Q1/26', 545, [56, 189, 248], '545'),
           ('Q2/26', 883, [255, 196, 0], '883'),
           ('Q3/26', 329, [239, 68, 68], '329')],
  'anh': 'stock price board Vietnam',
  'say': 'Tiếp theo là V N D, công ty nhạy nhất trong sáu công ty. Quý ba năm ngoái chín trăm hai mươi chín tỷ, rồi ba trăm bốn mươi hai, năm trăm bốn mươi lăm, tám trăm tám mươi '
         'ba, và quý ba năm nay còn ba trăm hai mươi chín tỷ. Giảm sáu mươi bốn phẩy năm phần trăm so với cùng kỳ và sáu mươi hai phẩy bảy phần trăm so với quý trước. Dữ liệu ghi '
         'doanh thu phí giao dịch giảm bảy mươi phẩy bốn phần trăm, lãi tự doanh giảm hơn một nửa. Hai nguồn này cùng phụ thuộc thị trường, nên khi cùng yếu, lợi nhuận mỏng đi '
         'rất nhanh. P trên B không phẩy chín mươi bốn, giá một năm giảm ba mươi ba phẩy ba phần trăm.'},
 {'k': 'cards',
  'label': 'HCM – LỢI NHUẬN & GIÁ',
  'cap': ('HCM', 'QUÝ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '297 tỷ', '−32,5% cùng kỳ'), ('Quý 3/2025', '440 tỷ', 'nền so sánh cao'), ('Lũy kế 9 tháng', '861 tỷ', '+0,2%'), ('Giá 1 năm', '+15,2%', 'đến 28/10')],
  'anh': 'securities trading office',
  'say': 'H C M có câu chuyện khác. Lợi nhuận quý ba là hai trăm chín mươi bảy tỷ, giảm ba mươi hai phẩy năm phần trăm vì quý ba năm ngoái là bốn trăm bốn mươi tỷ. Nhưng so với '
         'hai trăm bảy mươi ba tỷ của quý hai, quý này nhỉnh hơn. Chín tháng là tám trăm sáu mươi mốt tỷ, gần như đi ngang, tăng không phẩy hai phần trăm. Phí giao dịch giảm bảy '
         'mươi phẩy không phần trăm, tự doanh giảm hơn một nửa. Vậy mà giá cổ phiếu một năm vẫn tăng mười lăm phẩy hai phần trăm. Giá và lợi nhuận một quý không luôn đi cùng '
         'nhịp.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Cho vay ký quỹ có giữ nhịp không',
  'moc': True,
  'label': 'VCI & TCX – KÝ QUỸ TĂNG',
  'cap': ('CHO VAY', 'KÝ QUỸ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('VCI – ký quỹ', '472 tỷ', '+50,5% quý 3'),
            ('VCI – phí giao dịch', '−49,9%', 'LNST −12,6%'),
            ('TCX – ký quỹ', '1.561 tỷ', '+53,8% quý 3'),
            ('TCX – phí giao dịch', '−37,3%', 'LNST +7,9%')],
  'anh': 'stock market investors',
  'say': 'Chương năm. Cho vay ký quỹ có giữ nhịp không? Nhìn V C I và T C X: phí giao dịch giảm bốn mươi chín phẩy chín phần trăm ở V C I và ba mươi bảy phẩy ba ở T C X, nhưng '
         'lãi cho vay ký quỹ tăng năm mươi phẩy năm phần trăm lên bốn trăm bảy mươi hai tỷ ở V C I và năm mươi ba phẩy tám phần trăm lên một nghìn năm trăm sáu mươi mốt tỷ ở T C '
         'X. Kết quả: T C X tăng lợi nhuận bảy phẩy chín phần trăm, còn V C I giảm nhẹ hơn nhóm. F T S thì ngược lại, lợi nhuận ba mươi sáu tỷ, giảm ba mươi lăm phẩy không phần '
         'trăm, phí giao dịch giảm bảy mươi lăm phẩy chín. Đây là mô tả số liệu, không khẳng định nguyên nhân từng công ty.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cách đọc báo cáo công ty chứng khoán',
  'moc': True,
  'label': '4 BƯỚC ĐỌC BÁO CÁO',
  'cap': ('CÁCH', 'ĐỌC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('1. Nhìn cơ cấu: phí – ký quỹ – tự doanh', [255, 196, 0]),
            ('2. So cùng kỳ và cả quý trước', [56, 189, 248]),
            ('3. Kiểm tra nền so sánh quý 3/2025', [34, 197, 94]),
            ('4. Đọc giải trình ở báo cáo gốc', [239, 68, 68])],
  'anh': 'financial report analysis',
  'say': 'Chương sáu. Đọc báo cáo công ty chứng khoán thế nào? Bốn bước. Một, nhìn cơ cấu thu nhập: phí giao dịch, ký quỹ, tự doanh. Hai, so cả cùng kỳ lẫn quý trước. Ba, kiểm '
         'tra nền so sánh, như quý ba năm hai nghìn không trăm hai mươi lăm cao bất thường. Bốn, đọc giải trình ở báo cáo gốc trước khi tin bất kỳ lời giải thích nào, kể cả của '
         'mình. Khẩu vị rủi ro là biến số cần theo dõi, nhưng nó đi vào lợi nhuận qua từng nguồn thu.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN &', 'LƯU Ý'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu, dữ liệu thị trường của kênh đến ngày hai tháng mười một, giá cổ phiếu đến ngày hai mươi tám tháng '
         'mười. Đây là chia sẻ kiến thức, không phải khuyến nghị mua bán. Câu hỏi cho bạn: bạn quan tâm nguồn thu nào nhất của công ty chứng khoán? Xem thêm tại '
         'chungkhoanhuynguyen chấm com.'}]

S['Y3_0811C'] = [{'k': 'hook',
  'ch': 'Chương 1 – Lãi suất và tín dụng chạm bất động sản',
  'moc': True,
  'label': 'NLG – Nam Long',
  'cap': ('LÃI SUẤT', 'BẤT ĐỘNG SẢN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'NLGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 39.39, 'Đỉnh tuần 27/10: 39,39', 0.6], [38, 19.15, 'Đáy tuần 27/7: 19,15', 1.6], [51, 23.0, '28/10: 23,00', 2.6]]},
  'anh': 'apartment construction Vietnam',
  'say': 'Theo Ngân hàng Nhà nước, lãi suất tiền gửi bình quân phát sinh mới là sáu phẩy ba mươi tám phần trăm một năm, số liệu ngày hai mươi tháng chín, cao hơn cuối năm hai '
         'nghìn không trăm hai mươi lăm tới một phẩy mười lăm điểm. Đồng thời tín dụng đến ngày ba mươi tháng chín tăng mười sáu phẩy sáu mươi chín phần trăm so với cùng kỳ. Bất '
         'động sản nhạy cảm nhất với hai con số này, vì người mua nhà vay, chủ đầu tư vay, và lợi nhuận chỉ ghi nhận khi bàn giao. Chào bạn, đây là kênh Vĩ Mô Chứng Khoán Dễ '
         'Hiểu. Hôm nay mình xem N L G, K D H, D X G và V H M. Câu hỏi: vì sao doanh thu và lợi nhuận lệch nhau giữa các quý?'},
 {'k': 'cards',
  'label': 'LÃI SUẤT & TÍN DỤNG – NHNN',
  'cap': ('LÃI SUẤT', '& TÍN DỤNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Lãi suất tiền gửi mới', '6,38%/năm', '20/9/2026, NHNN'),
            ('So với cuối 2025', '+1,15 điểm', 'NHNN'),
            ('Tín dụng so cùng kỳ', '+16,69%', 'đến 30/9/2026'),
            ('Tín dụng so cuối 2025', '+11,59%', 'dư nợ 20,75 triệu tỷ')],
  'anh': 'bank building Vietnam',
  'say': 'Theo Ngân hàng Nhà nước, dư nợ tín dụng khoảng hai mươi phẩy bảy mươi lăm triệu tỷ đồng, tăng mười một phẩy năm mươi chín phần trăm so với cuối năm. Ngân hàng Nhà nước '
         'giữ nguyên lãi suất điều hành và yêu cầu các tổ chức tín dụng giảm lãi suất cho vay. Tiền gửi đắt hơn nhưng tín dụng vẫn mở rộng. Với bất động sản, mặt bằng lãi huy '
         'động cao thường kéo chi phí vốn lên. Đó là cơ chế chung, lãi vay thực tế mỗi doanh nghiệp còn tùy từng khoản nợ.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Vì sao bất động sản nhạy lãi suất',
  'moc': True,
  'label': 'BA KÊNH TÁC ĐỘNG',
  'cap': ('BA KÊNH', 'TÁC ĐỘNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Người mua vay: lãi cao, sức mua chậm', [56, 189, 248]),
            ('Chủ đầu tư vay: chi phí lãi vay', [239, 68, 68]),
            ('Doanh thu ghi nhận khi bàn giao', [255, 196, 0]),
            ('Tiền thu sớm, lợi nhuận về muộn', [34, 197, 94])],
  'anh': 'housing project aerial',
  'say': 'Chương hai. Vì sao bất động sản nhạy lãi suất? Đây là cơ chế chung. Kênh một là người mua nhà, thường vay ngân hàng, lãi cao thì sức mua chậm lại. Kênh hai là chủ đầu '
         'tư, vay làm dự án, nên chi phí lãi vay chạy vào báo cáo. Kênh ba, quan trọng nhất cho cách đọc, là thời điểm ghi nhận: doanh thu căn hộ, nhà phố thường ghi nhận khi bàn '
         'giao, không phải khi đặt cọc. Quý ít bàn giao thì doanh thu mỏng dù tiền thu từ khách đã về trước. Đừng chỉ nhìn một quý.'},
 {'k': 'bars',
  'ch': 'Chương 3 – VHM, ví dụ chuỗi bàn giao',
  'moc': True,
  'label': 'VHM – LNST CÁC QUÝ (TỶ ĐỒNG)',
  'cap': ('VHM', 'CHUỖI QUÝ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 4184, [56, 189, 248], '4.184'),
           ('Q4/25', 27514, [255, 196, 0], '27.514'),
           ('Q1/26', 25552, [255, 196, 0], '25.552'),
           ('Q2/26', 22683, [255, 196, 0], '22.683'),
           ('Q3/26', 23146, [34, 197, 94], '23.146')],
  'anh': 'large residential township',
  'say': 'Chương ba. V H M là ví dụ chuỗi bàn giao lớn. Lợi nhuận quý ba năm ngoái bốn nghìn một trăm tám mươi bốn tỷ, rồi từ quý bốn năm hai nghìn không trăm hai mươi lăm nhảy '
         'lên hai mươi bảy nghìn năm trăm mười bốn, hai mươi lăm nghìn năm trăm năm mươi hai, hai mươi hai nghìn sáu trăm tám mươi ba và hai mươi ba nghìn một trăm bốn mươi sáu '
         'tỷ ở quý ba năm hai nghìn không trăm hai mươi sáu. Doanh thu quý này tám mươi lăm nghìn ba trăm sáu mươi bốn tỷ, tăng bốn trăm mười chín phẩy chín phần trăm, biên gộp '
         'sáu mươi phẩy ba phần trăm so với mười lăm phẩy không cùng kỳ. Chi phí lãi vay tăng sáu mươi bảy phẩy chín phần trăm, ăn vào lợi nhuận, nhưng doanh thu tăng nhanh hơn '
         'nhiều. Giá một năm tăng hai mươi ba phẩy ba phần trăm, P trên E năm phẩy hai mươi ba, theo dữ liệu quá khứ. Đó là mặt sáng của bàn giao.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Ba mã chính: NLG, KDH, DXG',
  'moc': True,
  'label': 'NLG – QUÝ 3/2026',
  'cap': ('NLG', 'QUÝ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '5 tỷ', '−96,7% cùng kỳ'), ('Doanh thu thuần', '328 tỷ', '−82,5%'), ('Biên gộp', '46,1%', 'cùng kỳ 44,1%'), ('Lũy kế 9 tháng', '128 tỷ', '−63,7%')],
  'anh': 'townhouse project',
  'say': 'Chương bốn. N L G trước. Doanh thu quý ba chỉ ba trăm hai mươi tám tỷ, giảm tám mươi hai phẩy năm phần trăm, lợi nhuận còn năm tỷ, giảm chín mươi sáu phẩy bảy. Doanh '
         'thu các quý gần nhất là một nghìn bảy trăm linh bốn, một nghìn hai trăm bảy mươi chín, bốn trăm mười lăm rồi ba trăm hai mươi tám tỷ, một đường đi xuống rõ rệt. Biên '
         'gộp lại cải thiện, bốn mươi sáu phẩy một phần trăm so với bốn mươi bốn phẩy một, nên điểm cần chú ý là quy mô bàn giao. Dữ liệu nhắc lợi nhuận khác mười tỷ chiếm hai '
         'mươi sáu phần trăm lợi nhuận trước thuế, cần xem có phải khoản một lần. Giá một năm giảm ba mươi sáu phẩy không phần trăm.'},
 {'k': 'bars',
  'label': 'KDH – DOANH THU THUẦN (TỶ ĐỒNG)',
  'cap': ('KDH', 'DOANH THU'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 1098, [56, 189, 248], '1.098'),
           ('Q4/25', 1794, [56, 189, 248], '1.794'),
           ('Q1/26', 281, [255, 196, 0], '281'),
           ('Q2/26', 161, [255, 196, 0], '161'),
           ('Q3/26', 41, [239, 68, 68], '41')],
  'anh': 'villa residential area',
  'say': 'K D H lệch rất rõ. Doanh thu quý ba chỉ bốn mươi mốt tỷ, giảm chín mươi sáu phẩy hai phần trăm, biên gộp mười bốn phẩy chín phần trăm so với bảy mươi phẩy sáu. Vậy mà '
         'lợi nhuận vẫn một trăm bảy mươi sáu tỷ, giảm hai mươi lăm phẩy năm phần trăm, và chín tháng đạt một nghìn hai trăm linh chín tỷ, tăng một trăm mười bảy phẩy một phần '
         'trăm. Lợi nhuận lớn hơn doanh thu nghĩa là còn nguồn khác ngoài bán hàng. Mình không đoán nguồn nào, bạn xem giải trình ở báo cáo gốc. Giá một năm giảm năm mươi ba phẩy '
         'hai phần trăm.'},
 {'k': 'cards',
  'label': 'DXG – QUÝ 3/2026',
  'cap': ('DXG', 'QUÝ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '15 tỷ', '−83,6% cùng kỳ'), ('Doanh thu thuần', '683 tỷ', '−36,1%'), ('Biên gộp', '48,1%', 'cùng kỳ 56,0%'), ('Giá 1 năm', '−45,8%', 'đến 28/10')],
  'anh': 'apartment building Vietnam',
  'say': 'D X G. Lợi nhuận quý ba chỉ mười lăm tỷ, giảm tám mươi ba phẩy sáu phần trăm, doanh thu sáu trăm tám mươi ba tỷ giảm ba mươi sáu phẩy một, biên gộp thu hẹp từ năm mươi '
         'sáu phẩy không xuống bốn mươi tám phẩy một phần trăm. Chín tháng một trăm linh sáu tỷ, giảm năm mươi hai phẩy ba. ROE chỉ không phẩy sáu phần trăm, P trên E sáu mươi '
         'sáu phẩy sáu mươi lăm. P trên E cao ở đây vì lợi nhuận thấp, nó mô tả hiện tại, không nói về tương lai. Giá giảm bốn mươi lăm phẩy tám phần trăm trong một năm. Câu hỏi '
         'nên đặt: dự án nào sắp bàn giao?'},
 {'k': 'bars',
  'ch': 'Chương 5 – Thị trường đã phản ứng thế nào',
  'moc': True,
  'label': 'GIÁ CỔ PHIẾU 1 NĂM (ĐẾN 28/10)',
  'cap': ('GIÁ', '1 NĂM'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('NLG', -36.0, [239, 68, 68], '−36,0%'), ('KDH', -53.2, [239, 68, 68], '−53,2%'), ('DXG', -45.8, [239, 68, 68], '−45,8%'), ('VHM', 23.3, [34, 197, 94], '+23,3%')],
  'anh': 'stock chart real estate',
  'say': 'Chương năm. Thị trường phản ứng thế nào? Giá một năm đến ngày hai mươi tám tháng mười: N L G giảm ba mươi sáu phẩy không phần trăm, K D H giảm năm mươi ba phẩy hai, D X '
         'G giảm bốn mươi lăm phẩy tám, còn V H M tăng hai mươi ba phẩy ba. Ba mã nhỏ đều giảm mạnh, trong khi V H M vẫn tăng. Có thể thị trường đang phân biệt doanh nghiệp bàn '
         'giao đều với bàn giao thưa, nhưng đó là cách đọc quá khứ, không phải dự báo.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Câu hỏi nên đặt khi đọc báo cáo bất động sản',
  'moc': True,
  'label': '4 CÂU HỎI NÊN ĐẶT',
  'cap': ('4 CÂU', 'HỎI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Bàn giao quý này so với quý trước?', [56, 189, 248]),
            ('Biên gộp thu hẹp hay cải thiện?', [255, 196, 0]),
            ('Chi phí lãi vay tăng bao nhiêu?', [239, 68, 68]),
            ('Lợi nhuận có đến từ nguồn ngoài bán hàng?', [34, 197, 94])],
  'anh': 'financial analyst reading report',
  'say': 'Chương sáu. Bốn câu hỏi khi đọc báo cáo bất động sản. Một, bàn giao quý này so với quý trước? Hai, biên gộp thu hẹp hay cải thiện, như N L G cải thiện còn D X G thu '
         'hẹp? Ba, chi phí lãi vay tăng bao nhiêu, như V H M tăng sáu mươi bảy phẩy chín phần trăm? Bốn, lợi nhuận có đến từ nguồn ngoài bán hàng không, như K D H? Bốn câu này '
         'không cho bạn dự báo, nhưng giúp đọc đúng điều doanh nghiệp đã báo cáo.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN &', 'LƯU Ý'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: Ngân hàng Nhà nước, báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu, giá cổ phiếu đến ngày hai mươi tám tháng mười. Đây là chia sẻ kiến thức, '
         'không phải khuyến nghị mua bán. Câu hỏi cho bạn: bạn nhìn doanh thu bàn giao hay chi phí lãi vay trước? Xem thêm tại chungkhoanhuynguyen chấm com.'}]

S['Y3_0911A'] = [{'k': 'hook',
  'ch': 'Chương 1 – Dầu tăng, phân bón được gì',
  'moc': True,
  'label': 'DCM – Đạm Cà Mau',
  'cap': ('DẦU TĂNG', 'PHÂN BÓN?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'DCMW', 'tf': 'W', 'weeks': 52, 'circles': [[18, 50.01, 'Đỉnh tuần 9/3: 50,01', 0.6], [37, 28.5, 'Đáy tuần 20/7: 28,50', 1.6], [51, 34.8, '28/10: 34,80', 2.6]]},
  'anh': 'fertilizer plant',
  'say': 'Dầu Brent đang ở một trăm linh tám phẩy bảy mươi bốn đô la một thùng, tăng sáu mươi bảy phẩy một phần trăm so với một năm trước, theo dữ liệu ngày hai tháng mười một. '
         'Mức đáy một năm là năm mươi tám phẩy chín mươi hai đô la, ngày mười sáu tháng mười hai năm hai nghìn không trăm hai mươi lăm. Giá năng lượng cao thường được hiểu là tin '
         'tốt cho phân bón vì giá bán có thể tăng. Nhưng năng lượng cũng là chi phí đầu vào. Vậy phân đạm và hóa chất hưởng lợi, hay bị bóp biên? Chào bạn, đây là kênh Vĩ Mô '
         'Chứng Khoán Dễ Hiểu. Hôm nay mình đặt câu hỏi này lên ba doanh nghiệp: D C M, D P M và D G C, qua lợi nhuận, biên lợi nhuận gộp và chi phí lãi vay. Mình không dùng giá '
         'urê, vì dữ liệu của kênh không có. Cái gì không có số, mình không nói.'},
 {'k': 'cards',
  'label': 'GIÁ DẦU THẾ GIỚI',
  'cap': ('GIÁ', 'DẦU'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Brent', '108,74 USD', '2/11/2026'), ('Brent 1 tháng', '+6,3%', '3 tháng +37,0%'), ('Brent 1 năm', '+67,1%', 'Đáy 58,92 USD'), ('WTI', '99,81 USD', '+63,7% / 1 năm')],
  'anh': 'oil refinery',
  'say': 'Trước hết là con số. Brent đang một trăm linh tám phẩy bảy mươi bốn đô la, tăng sáu phẩy ba phần trăm trong một tháng và ba mươi bảy phẩy không phần trăm trong ba '
         'tháng. Đỉnh một năm là một trăm mười tám phẩy ba mươi lăm đô la, ngày ba mươi tháng ba. Đường đi khá dốc: cuối tháng một năm nay còn sáu mươi phẩy bảy đô la, tháng bốn '
         'lên một trăm linh chín phẩy hai mươi bảy, tháng bảy về bảy mươi mốt phẩy chín mươi chín, rồi quay lại một trăm linh tám phẩy bảy mươi bốn. Dầu WTI là chín mươi chín '
         'phẩy tám mươi mốt đô la, tăng sáu mươi ba phẩy bảy phần trăm một năm. Giá năng lượng đã ở vùng cao, nhưng lợi nhuận doanh nghiệp còn phụ thuộc nhiều yếu tố khác.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Cơ chế: hưởng lợi hay bóp biên',
  'moc': True,
  'label': 'BIÊN GỘP LÀ THƯỚC ĐO',
  'cap': ('CƠ CHẾ', 'CHUNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Khí, dầu là chi phí đầu vào', [239, 68, 68]),
            ('Giá bán có thể tăng theo', [34, 197, 94]),
            ('Biên gộp: giá bán trừ chi phí', [255, 196, 0]),
            ('Chi phí lãi vay ăn vào lợi nhuận cuối', [56, 189, 248])],
  'anh': 'natural gas pipeline',
  'say': 'Chương hai. Mình nói trước, đây là cơ chế chung, không gán cho công ty nào. Phân đạm dùng khí làm nguyên liệu. Khi năng lượng đắt lên, chi phí đầu vào tăng. Nếu giá bán '
         'tăng nhanh hơn chi phí, biên gộp rộng ra. Nếu giá bán tăng chậm hơn, biên bị bóp. Vì vậy thước đo đúng là biên lợi nhuận gộp, không chỉ doanh thu. Dưới biên gộp còn chi '
         'phí lãi vay, ăn vào lợi nhuận sau cùng. Thêm nữa, chi phí và giá bán không luôn đổi cùng lúc. Giờ ta đọc ba doanh nghiệp.'},
 {'k': 'cards',
  'ch': 'Chương 3 – DCM: doanh thu gần gấp đôi, biên thu hẹp',
  'moc': True,
  'label': 'DCM – QUÝ 3/2026',
  'cap': ('DCM', 'QUÝ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '430 tỷ', '+31,1% cùng kỳ'),
            ('Doanh thu', '5.742 tỷ', '+92,1%'),
            ('Biên gộp', '19,1%', 'cùng kỳ 22,0%'),
            ('Lũy kế 9 tháng', '2.282 tỷ', '+49,6%'),
            ('ROE', '24,2%', 'P/E 6,49')],
  'anh': 'urea fertilizer factory',
  'say': 'Chương ba, D C M. Doanh thu thuần quý ba là năm nghìn bảy trăm bốn mươi hai tỷ, gần gấp đôi cùng kỳ, tăng chín mươi hai phẩy một phần trăm. Lợi nhuận bốn trăm ba mươi '
         'tỷ, tăng ba mươi mốt phẩy một phần trăm. Lợi nhuận tăng chậm hơn doanh thu nhiều, vì biên gộp thu hẹp còn mười chín phẩy một phần trăm từ hai mươi hai phẩy không. Mỗi '
         'đồng doanh thu giữ lại ít hơn. Chín tháng đạt hai nghìn hai trăm tám mươi hai tỷ, tăng bốn mươi chín phẩy sáu phần trăm, ROE hai mươi bốn phẩy hai phần trăm.'},
 {'k': 'bars',
  'label': 'DCM – LNST CÁC QUÝ (TỶ ĐỒNG)',
  'cap': ('DCM', 'CHUỖI QUÝ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('Q3/25', 328, [56, 189, 248], '328'),
           ('Q4/25', 435, [56, 189, 248], '435'),
           ('Q1/26', 788, [56, 189, 248], '788'),
           ('Q2/26', 1065, [255, 196, 0], '1.065'),
           ('Q3/26', 430, [34, 197, 94], '430')],
  'anh': 'fertilizer warehouse',
  'say': 'Chuỗi lợi nhuận D C M: ba trăm hai mươi tám tỷ, bốn trăm ba mươi lăm, bảy trăm tám mươi tám, đỉnh một nghìn không trăm sáu mươi lăm tỷ ở quý hai, rồi bốn trăm ba mươi '
         'tỷ ở quý ba. So với quý trước giảm năm mươi chín phẩy sáu phần trăm. Quý ba vẫn cao hơn cùng kỳ, nhưng thấp hơn nhiều quý hai. Giá cổ phiếu một năm tăng năm phẩy tám '
         'phần trăm. Một mã, hai lát cắt: so cùng kỳ thì tốt, so quý trước thì yếu. Hãy đọc cả hai.'},
 {'k': 'cards',
  'ch': 'Chương 4 – DPM: từ 906 tỷ xuống 40 tỷ',
  'moc': True,
  'label': 'DPM – QUÝ 2 VÀ QUÝ 3',
  'cap': ('DPM', 'QUÝ 2 VÀ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 2', '906 tỷ', 'quý 2/2026'),
            ('LNST quý 3', '40 tỷ', '−82,9% cùng kỳ'),
            ('Biên gộp', '14,1%', 'cùng kỳ 19,3%'),
            ('Chi phí lãi vay', '+48,3%', 'ăn vào lợi nhuận')],
  'anh': 'fertilizer production plant',
  'say': 'Chương bốn, D P M. Quý hai lợi nhuận chín trăm linh sáu tỷ, quý ba chỉ bốn mươi tỷ, giảm chín mươi lăm phẩy năm phần trăm so với quý trước và tám mươi hai phẩy chín '
         'phần trăm so với cùng kỳ. Doanh thu vẫn tăng mười phẩy bảy phần trăm lên bốn nghìn một trăm hai mươi tám tỷ, nghĩa là phần bị bào mòn là phần giữ lại. Biên gộp rơi từ '
         'mười chín phẩy ba xuống mười bốn phẩy một phần trăm, và chi phí lãi vay tăng bốn mươi tám phẩy ba phần trăm. Hai yếu tố cùng ăn vào lợi nhuận. Chín tháng vẫn là một '
         'nghìn ba trăm bốn mươi tám tỷ, tăng năm mươi chín phẩy bảy phần trăm. Nguyên nhân của biên, báo cáo gốc có giải trình.'},
 {'k': 'cards',
  'ch': 'Chương 5 – DGC: dầu cao nhưng biên thấp',
  'moc': True,
  'label': 'DGC – QUÝ 3/2026',
  'cap': ('DGC', 'QUÝ 3'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('LNST quý 3', '478 tỷ', '−36,4% cùng kỳ'), ('Doanh thu', '2.469 tỷ', '−12,3%'), ('Biên gộp', '20,5%', 'cùng kỳ 31,1%'), ('Lũy kế 9 tháng', '1.267 tỷ', '−47,3%')],
  'anh': 'chemical plant',
  'say': 'Chương năm, D G C, trường hợp ngược với kỳ vọng dầu cao thì hóa chất có lợi. Doanh thu quý ba giảm mười hai phẩy ba phần trăm còn hai nghìn bốn trăm sáu mươi chín tỷ, '
         'biên gộp từ ba mươi mốt phẩy một xuống hai mươi phẩy năm phần trăm, lợi nhuận bốn trăm bảy mươi tám tỷ giảm ba mươi sáu phẩy bốn. Chín tháng một nghìn hai trăm sáu mươi '
         'bảy tỷ, giảm bốn mươi bảy phẩy ba. Nhìn chuỗi quý, lợi nhuận chạm ba trăm tám mươi tỷ ở quý hai rồi lên bốn trăm bảy mươi tám tỷ ở quý ba. Giá một năm giảm năm mươi lăm '
         'phẩy chín phần trăm. Giá năng lượng cao không tự động thành biên cao, còn nhiều yếu tố mà gói dữ liệu không nêu, và mình không đoán.'},
 {'k': 'bars',
  'ch': 'Chương 6 – So sánh biên gộp và câu hỏi nên đặt',
  'moc': True,
  'label': 'BIÊN GỘP QUÝ 3 SO CÙNG KỲ (%)',
  'cap': ('BIÊN GỘP', '3 MÃ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('DCM Q3/25', 22.0, [56, 189, 248], '22,0%'),
           ('DCM Q3/26', 19.1, [255, 196, 0], '19,1%'),
           ('DPM Q3/25', 19.3, [56, 189, 248], '19,3%'),
           ('DPM Q3/26', 14.1, [255, 196, 0], '14,1%'),
           ('DGC Q3/25', 31.1, [56, 189, 248], '31,1%'),
           ('DGC Q3/26', 20.5, [255, 196, 0], '20,5%')],
  'anh': 'industrial chemical plant',
  'say': 'Đặt cạnh nhau, cả ba đều có biên gộp quý ba thấp hơn cùng kỳ: D C M từ hai mươi hai phẩy không xuống mười chín phẩy một, D P M từ mười chín phẩy ba xuống mười bốn phẩy '
         'một, D G C từ ba mươi mốt phẩy một xuống hai mươi phẩy năm. Ba doanh nghiệp, ba câu chuyện: D C M doanh thu tăng mạnh nhưng biên thu hẹp, D P M thêm lãi vay tăng, D G C '
         'doanh thu cũng yếu. Vì vậy hưởng lợi hay bị bóp biên không có một đáp án chung cho cả ngành.'},
 {'k': 'checklist',
  'label': 'CÂU HỎI NÊN ĐẶT',
  'cap': ('CÂU HỎI', 'NÊN ĐẶT'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Biên gộp so cùng kỳ thay đổi ra sao?', [255, 196, 0]),
            ('Doanh thu tăng có kéo theo lợi nhuận?', [56, 189, 248]),
            ('Chi phí lãi vay tăng bao nhiêu?', [239, 68, 68]),
            ('So quý trước thì quý này thế nào?', [34, 197, 94])],
  'anh': 'analyst checking financial statements',
  'say': 'Vậy khi giá dầu tăng, bạn nên hỏi gì khi đọc báo cáo phân bón và hóa chất? Một, biên gộp so cùng kỳ thay đổi thế nào. Hai, doanh thu tăng có kéo theo lợi nhuận không, '
         'như D C M tăng doanh thu chín mươi hai phẩy một phần trăm nhưng lợi nhuận tăng ba mươi mốt phẩy một. Ba, chi phí lãi vay tăng bao nhiêu. Bốn, so với quý trước thì sao, '
         'vì D P M cho thấy một quý có thể đổi chiều rất nhanh. Những câu hỏi này giúp đọc đúng điều doanh nghiệp đã báo cáo, không dự báo.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN &', 'LƯU Ý'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: dữ liệu thị trường của kênh đến ngày hai tháng mười một cho giá dầu, báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và giá cổ phiếu đến ngày hai '
         'mươi tám tháng mười. Đây là chia sẻ kiến thức, không phải khuyến nghị mua bán. Câu hỏi cho bạn: bạn nghĩ biên gộp hay doanh thu quan trọng hơn khi đọc báo cáo ngành '
         'này? Xem thêm tại chungkhoanhuynguyen chấm com.'}]

S['Y3_0911B'] = [{'k': 'hook',
  'ch': 'Chương 1 – VN-Index có đi theo thế giới',
  'moc': True,
  'label': 'VN-Index',
  'cap': ('VN-INDEX', 'THEO THẾ GIỚI?'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[2, 1578.42, 'Đáy tuần 10/11: 1.578,42', 0.6], [28, 1933.11, 'Đỉnh tuần 18/5: 1.933,11', 1.6], [51, 1766.65, '28/10: 1.766,65', 2.6]]},
  'anh': 'Ho Chi Minh City stock exchange',
  'say': 'Tháng qua, KOSPI của Hàn Quốc giảm mười sáu phẩy ba phần trăm. Nikkei của Nhật giảm bảy phẩy bảy. Nasdaq giảm năm phẩy ba. Vậy VN-Index thì sao? Từ một nghìn bảy trăm '
         'tám mươi lăm phẩy một điểm ngày hai mươi lăm tháng chín xuống một nghìn bảy trăm sáu mươi sáu phẩy sáu mươi lăm điểm ngày hai mươi tám tháng mười, giảm khoảng một phần '
         'trăm. Câu hỏi hôm nay: VN-Index có đi theo thế giới không? Chào bạn, đây là kênh Vĩ Mô Chứng Khoán Dễ Hiểu. Mình dùng một phép tính của kênh: tương quan lợi suất theo '
         'tháng giữa VN-Index và tám thước đo thế giới, từ tháng mười một năm hai nghìn không trăm hai mươi ba đến tháng mười năm hai nghìn không trăm hai mươi sáu. Nói trước hai '
         'giới hạn: tương quan không phải nhân quả, và mẫu chỉ khoảng ba năm.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Tám hệ số tương quan',
  'moc': True,
  'label': 'TƯƠNG QUAN THÁNG VỚI VN-INDEX',
  'cap': ('TƯƠNG', 'QUAN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('S&P 500', 0.59, [34, 197, 94], '0,59'),
           ('Nasdaq', 0.5, [34, 197, 94], '0,50'),
           ('Nikkei', 0.48, [34, 197, 94], '0,48'),
           ('KOSPI', 0.42, [34, 197, 94], '0,42'),
           ('Vàng', 0.19, [56, 189, 248], '0,19'),
           ('Bitcoin', 0.13, [56, 189, 248], '0,13'),
           ('DXY', -0.17, [239, 68, 68], '−0,17'),
           ('Brent', -0.23, [239, 68, 68], '−0,23')],
  'anh': 'stock market correlation chart',
  'say': 'Chương hai. Tương quan chạy từ âm một đến một. Dương là cùng chiều, âm là ngược chiều, gần không là ít liên hệ. Kết quả: S và P năm trăm không phẩy năm mươi chín, '
         'Nasdaq không phẩy năm mươi, Nikkei không phẩy bốn mươi tám, KOSPI không phẩy bốn mươi hai. Vàng chỉ không phẩy mười chín, Bitcoin không phẩy mười ba. Chỉ số đô la DXY '
         'âm không phẩy mười bảy, giá dầu Brent âm không phẩy hai mươi ba. Đọc đơn giản: cổ phiếu Mỹ và châu Á cùng chiều rõ nhất, vàng và Bitcoin ít liên hệ, đô la mạnh hay dầu '
         'cao đi ngược nhẹ. Đây là phép tính của kênh trên mẫu từ ba mươi lăm đến ba mươi sáu tháng. Ví dụ, hệ số không phẩy năm chín không có nghĩa là mỗi khi S và P tăng một '
         'phần trăm thì VN-Index tăng không phẩy năm chín phần trăm. Nó chỉ nói hai chuỗi lợi suất tháng có xu hướng cùng chiều.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Tháng qua: thế giới giảm, VN-Index đứng yên',
  'moc': True,
  'label': 'BIẾN ĐỘNG 1 THÁNG (%)',
  'cap': ('1 THÁNG', 'QUA'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('KOSPI', -16.3, [239, 68, 68], '−16,3%'),
           ('Nikkei', -7.7, [239, 68, 68], '−7,7%'),
           ('Nasdaq', -5.3, [239, 68, 68], '−5,3%'),
           ('S&P 500', -0.9, [239, 68, 68], '−0,9%'),
           ('VN-Index', -1.0, [255, 196, 0], '−1,0%')],
  'anh': 'stock market decline',
  'say': 'Chương ba. Nhìn tháng vừa qua: KOSPI giảm mười sáu phẩy ba phần trăm, Nikkei giảm bảy phẩy bảy, Nasdaq giảm năm phẩy ba, S và P năm trăm giảm không phẩy chín. VN-Index '
         'giảm khoảng một phần trăm so với cuối tháng chín. Hai mốc thời gian không trùng hoàn toàn, vì VN-Index tính đến ngày hai mươi tám tháng mười, còn các chỉ số thế giới '
         'tính đến phiên ngày ba mươi tháng mười hoặc ngày hai tháng mười một. Dù vậy, độ lệch lớn: thế giới giảm sâu, VN-Index gần như đứng yên.'},
 {'k': 'cards',
  'label': 'BÊN NGOÀI NHÓM CỔ PHIẾU',
  'cap': ('VÀNG, USD', 'DẦU, BTC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Vàng', '3.904,8 USD', '−6,2% / 1 tháng'),
            ('Bitcoin', '77.855 USD', '−8,2% / 1 tháng'),
            ('DXY', '101,65', '−0,3% / 1 tháng'),
            ('Brent', '108,74 USD', '+6,3% / 1 tháng')],
  'anh': 'gold bars',
  'say': 'Còn các tài sản khác? Vàng ba nghìn chín trăm linh bốn phẩy tám đô la một ounce, giảm sáu phẩy hai phần trăm trong tháng. Bitcoin giảm tám phẩy hai. Chỉ số đô la DXY '
         'một trăm linh một phẩy sáu mươi lăm, giảm không phẩy ba. Dầu Brent một trăm linh tám phẩy bảy mươi bốn đô la, tăng sáu phẩy ba. Những tài sản này có tương quan thấp '
         'hoặc âm với VN-Index trong mẫu, nên chúng biến động mạnh chưa có nghĩa VN-Index phải đi theo. Điều đáng chú ý là nhóm cổ phiếu quốc tế mới có tương quan dương rõ.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Vì sao không nên diễn giải quá đà',
  'moc': True,
  'label': '4 GIỚI HẠN CẦN NHỚ',
  'cap': ('4 GIỚI', 'HẠN'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Tương quan cao nhất chỉ 0,59', [255, 196, 0]),
            ('Tương quan không phải nhân quả', [239, 68, 68]),
            ('Mẫu chỉ khoảng 3 năm', [56, 189, 248]),
            ('Một tháng có thể là ngoại lệ', [34, 197, 94])],
  'anh': 'analyst studying market data',
  'say': 'Chương bốn. Mình nhấn mạnh bốn giới hạn. Một, hệ số cao nhất cũng chỉ không phẩy năm mươi chín, nghĩa là còn nhiều biến động VN-Index không đi cùng thế giới. Hai, tương '
         'quan không phải nhân quả, hai chuỗi đi cùng nhau chưa chắc cái này gây ra cái kia. Ba, mẫu chỉ khoảng ba năm, một giai đoạn ngắn. Bốn, một tháng có thể là ngoại lệ so '
         'với quy luật chung. Vì thế câu trả lời trung thực là: có liên hệ, nhưng chưa đủ để nói VN-Index đi theo thế giới.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Yếu tố trong nước',
  'moc': True,
  'label': 'VĨ MÔ & DOANH NGHIỆP TRONG NƯỚC',
  'cap': ('YẾU TỐ', 'TRONG NƯỚC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('GDP quý 3/2026', '+9,95%', 'Cục Thống kê'),
            ('Tín dụng', '+16,69%', 'so cùng kỳ, NHNN'),
            ('Bán lẻ + dịch vụ 9 tháng', '+13,4%', 'Cục Thống kê'),
            ('VHM – LNST quý 3', '23.146 tỷ', '+453,2% cùng kỳ')],
  'anh': 'Vietnam economy factory',
  'say': 'Chương năm. Vậy điều gì đứng phía trong nước? Theo Cục Thống kê, GDP quý ba ước tăng chín phẩy chín mươi lăm phần trăm, và tổng mức bán lẻ cùng doanh thu dịch vụ tiêu '
         'dùng chín tháng tăng mười ba phẩy bốn phần trăm. Theo Ngân hàng Nhà nước, tín dụng đến ngày ba mươi tháng chín tăng mười sáu phẩy sáu mươi chín phần trăm so với cùng '
         'kỳ. Về doanh nghiệp, V H M là ví dụ phụ: lợi nhuận quý ba đạt hai mươi ba nghìn một trăm bốn mươi sáu tỷ, tăng bốn trăm năm mươi ba phẩy hai phần trăm. Mình không khẳng '
         'định các yếu tố này quyết định VN-Index, chỉ nói rằng chúng là biến số cần đặt bên cạnh tin thế giới.'},
 {'k': 'cards',
  'label': 'VN-INDEX NĂM 2026',
  'cap': ('VN-INDEX', 'NĂM 2026'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Đóng cửa 28/10', '1.766,65', 'điểm'), ('Từ đầu năm', '−1,0%', 'đến 28/10'), ('Đỉnh tuần', '1.933,11', 'tuần 18/5/2026'), ('Đáy tuần', '1.647,81', '20/3/2026')],
  'anh': 'stock index chart',
  'say': 'Cuối cùng, VN-Index trong năm. Đóng cửa ngày hai mươi tám tháng mười là một nghìn bảy trăm sáu mươi sáu phẩy sáu mươi lăm điểm, từ đầu năm giảm một phẩy không phần '
         'trăm. Đỉnh tuần là một nghìn chín trăm ba mươi ba phẩy mười một điểm, tuần ngày mười tám tháng năm. Đáy tuần là một nghìn sáu trăm bốn mươi bảy phẩy tám mươi mốt điểm, '
         'đóng cửa tuần ngày hai mươi tháng ba. Nghĩa là chỉ số đã dao động khá rộng trong năm, và hiện nằm ở khoảng giữa. Đó chỉ là mô tả quá khứ. Để so sánh, KOSPI có đỉnh một '
         'năm là chín nghìn một trăm mười bốn phẩy năm mươi lăm điểm ngày hai mươi hai tháng sáu và hiện ở năm nghìn tám trăm năm mươi chín phẩy không tám điểm. Biên độ của '
         'VN-Index trong năm êm hơn.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cách theo dõi hợp lý',
  'moc': True,
  'label': 'CÁCH THEO DÕI',
  'cap': ('CÁCH', 'THEO DÕI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('Xem tương quan, đừng coi là quy luật', [255, 196, 0]),
            ('Tách tin thế giới và tin trong nước', [56, 189, 248]),
            ('Đối chiếu cùng mốc thời gian', [34, 197, 94]),
            ('Quay về báo cáo tài chính', [239, 68, 68])],
  'anh': 'investor reading charts',
  'say': 'Chương sáu. Cách theo dõi hợp lý gồm bốn việc. Dùng tương quan như một gợi ý, đừng coi là quy luật. Tách tin thế giới khỏi tin doanh nghiệp trong nước. Đối chiếu cùng '
         'mốc thời gian khi so sánh. Và cuối cùng, quay về báo cáo tài chính, vì chỉ số chỉ là tổng hợp của hàng trăm doanh nghiệp. Nếu ai đó nói chắc chắn VN-Index sẽ đi theo '
         'thế giới, hãy nhớ con số không phẩy năm chín và mẫu ba năm.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN &', 'LƯU Ý'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: phép tính tương quan của kênh từ dữ liệu thị trường, Cục Thống kê, Ngân hàng Nhà nước, giá đến ngày hai mươi tám tháng mười và hai tháng mười một. Đây là chia sẻ '
         'kiến thức, không phải khuyến nghị mua bán. Câu hỏi cho bạn: bạn thấy VN-Index đang đi theo thế giới hay theo yếu tố trong nước? Xem thêm tại chungkhoanhuynguyen chấm '
         'com.'}]

S['Y3_0911C'] = [{'k': 'hook',
  'ch': 'Chương 1 – Bản đồ tám biến số',
  'moc': True,
  'label': 'VCB – Vietcombank',
  'cap': ('BẢN ĐỒ', 'VĨ MÔ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'chart': {'sym': 'VCBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[11, 78.15, 'Đỉnh tuần 12/1: 78,15', 0.6], [37, 52.6, 'Đáy tuần 20/7: 52,60', 1.6], [51, 57.5, '28/10: 57,50', 2.6]]},
  'anh': 'Vietnam economy skyline',
  'say': 'Vĩ mô nghe xa vời, cho đến khi bạn nối nó với một dòng trong báo cáo tài chính. Đây là kênh Vĩ Mô Chứng Khoán Dễ Hiểu, và video hôm nay là tổng kết: tám biến số vĩ mô, '
         'mỗi biến số nối với một ngành và một doanh nghiệp thật. Dầu. Lãi suất tiền gửi và tín dụng. Lạm phát. Tỷ giá. Fed và lợi suất Mỹ. Vàng. Xuất nhập khẩu và đầu tư nước '
         'ngoài. Bán lẻ và du lịch. Với mỗi biến số mình chỉ điểm một con số và một câu hỏi nên đặt, không phân tích sâu lại các mã đã nói ở video khác. Cuối cùng là quy trình '
         'năm bước để bạn tự làm. Câu hỏi xuyên suốt: biến số này đi vào lợi nhuận qua cửa nào?'},
 {'k': 'cards',
  'ch': 'Chương 2 – Giá cả và chi phí',
  'moc': True,
  'label': 'DẦU & LẠM PHÁT',
  'cap': ('DẦU &', 'LẠM PHÁT'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Brent', '108,74 USD', '+67,1% / 1 năm'),
            ('BSR – lọc dầu', 'LNST quý 3 +888,2%', 'so cùng kỳ'),
            ('CPI tháng 9/2026', '+5,08%', 'so cùng kỳ, Cục Thống kê'),
            ('HPG – thép', 'LNST quý 3 +106,0%', 'so cùng kỳ')],
  'anh': 'oil refinery Vietnam',
  'say': 'Chương hai. Biến số một: dầu. Brent một trăm linh tám phẩy bảy mươi bốn đô la, tăng sáu mươi bảy phẩy một phần trăm một năm. Ngành nối ở đầu nguồn là lọc dầu, ví dụ B S '
         'R, lợi nhuận quý ba tăng tám trăm tám mươi tám phẩy hai phần trăm. Câu hỏi nên đặt: biên đến từ giá bán hay từ chi phí? Biến số hai: lạm phát. Theo Cục Thống kê, CPI '
         'tháng chín tăng năm phẩy không tám phần trăm so với cùng kỳ. Ngành thép, ví dụ H P G, lợi nhuận quý ba tăng một trăm linh sáu phẩy không phần trăm. Câu hỏi: doanh '
         'nghiệp có chuyển được chi phí đầu vào sang giá bán không, và biên gộp nói gì?'},
 {'k': 'cards',
  'ch': 'Chương 3 – Tiền và lãi suất',
  'moc': True,
  'label': 'LÃI SUẤT & TÍN DỤNG',
  'cap': ('LÃI SUẤT', '& TÍN DỤNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Lãi suất tiền gửi mới', '6,38%/năm', 'NHNN, 20/9/2026'), ('Tín dụng', '+16,69%', 'so cùng kỳ, NHNN'), ('VCB – ngân hàng', 'Thu nhập lãi thuần +39,1%', 'quý 3/2026')],
  'anh': 'bank counter Vietnam',
  'say': 'Biến số ba: lãi suất tiền gửi và tín dụng. Theo Ngân hàng Nhà nước, lãi suất tiền gửi mới là sáu phẩy ba mươi tám phần trăm một năm, tín dụng tăng mười sáu phẩy sáu '
         'mươi chín phần trăm so với cùng kỳ. Ngành nối trực tiếp là ngân hàng, ví dụ V C B, thu nhập lãi thuần quý ba tăng ba mươi chín phẩy một phần trăm. Câu hỏi nên đặt: '
         'chênh lệch giữa lãi cho vay và lãi huy động ra sao, và chi phí dự phòng có ăn vào lợi nhuận không? Với ngân hàng, thu nhập lãi thuần và chi phí dự phòng luôn đi cùng '
         'nhau.'},
 {'k': 'cards',
  'label': 'TỶ GIÁ',
  'cap': ('TỶ', 'GIÁ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('USD/VND', '25.802', '−1,9% / 1 năm'), ('Cao nhất 1 năm', '26.378', '19/11/2025'), ('POW – điện', 'LNST quý 2 +460,3%', 'quý 2, chưa có quý 3')],
  'anh': 'power plant Vietnam',
  'say': 'Biến số bốn: tỷ giá. Đô la ở mức hai mươi lăm nghìn tám trăm linh hai đồng, giảm một phẩy chín phần trăm một năm, đỉnh một năm là hai mươi sáu nghìn ba trăm bảy mươi '
         'tám đồng, ngày mười chín tháng mười một năm hai nghìn không trăm hai mươi lăm. Doanh nghiệp có nợ hoặc nhiên liệu tính bằng ngoại tệ, như ngành điện, có thể nhạy với tỷ '
         'giá. Lấy P O W làm ví dụ, lợi nhuận quý hai tăng bốn trăm sáu mươi phẩy ba phần trăm, lưu ý là quý hai vì chưa có quý ba. Gói dữ liệu không cho biết doanh nghiệp này có '
         'bao nhiêu nợ ngoại tệ, và đó chính là câu hỏi nên đặt: thuyết minh báo cáo nói gì?'},
 {'k': 'cards',
  'ch': 'Chương 4 – Dòng vốn toàn cầu',
  'moc': True,
  'label': 'FED, LỢI SUẤT MỸ, VÀNG',
  'cap': ('FED &', 'VÀNG'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Lãi suất Fed', '3,75–4,00%', 'giữ nguyên 29/10'),
            ('Lợi suất Mỹ 10 năm', '4,929%', '30/10/2026'),
            ('Vàng', '3.904,8 USD', '−6,2% / 1 tháng'),
            ('SSI – chứng khoán', 'LNST quý 3 −23,7%', 'so cùng kỳ')],
  'anh': 'Federal Reserve building',
  'say': 'Biến số năm và sáu: Fed, lợi suất Mỹ và vàng. Fed giữ lãi suất ba phẩy bảy mươi lăm đến bốn phẩy không không phần trăm ngày hai mươi chín tháng mười, sau lần tăng hai '
         'mươi lăm điểm cơ bản ngày mười bảy tháng chín. Lợi suất trái phiếu Mỹ mười năm là bốn phẩy chín hai chín phần trăm. Vàng ba nghìn chín trăm linh bốn phẩy tám đô la một '
         'ounce, giảm sáu phẩy hai phần trăm trong tháng. Ba thước đo này cùng kể một câu chuyện về dòng vốn và khẩu vị rủi ro. Ngành nối là công ty chứng khoán, ví dụ S S I, lợi '
         'nhuận quý ba giảm hai mươi ba phẩy bảy phần trăm. Câu hỏi: nguồn thu nào, phí giao dịch, ký quỹ hay tự doanh, đang chịu tác động?'},
 {'k': 'cards',
  'ch': 'Chương 5 – Kinh tế thực: thương mại và tiêu dùng',
  'moc': True,
  'label': 'XUẤT NHẬP KHẨU & FDI',
  'cap': ('XUẤT NHẬP', 'KHẨU & FDI'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Xuất nhập khẩu 9 tháng', '888,02 tỷ USD', '+30,4%, Cục Thống kê'),
            ('FDI giải ngân 9 tháng', '21,07 tỷ USD', '+12,1%'),
            ('GMD – cảng biển', 'LNST quý 2 +152,5%', 'quý 2, chưa có quý 3')],
  'anh': 'container port Vietnam',
  'say': 'Chương năm. Biến số bảy: xuất nhập khẩu và đầu tư nước ngoài. Theo Cục Thống kê, kim ngạch hàng hóa chín tháng là tám trăm tám mươi tám phẩy không hai tỷ đô la, tăng ba '
         'mươi phẩy bốn phần trăm, vốn đầu tư nước ngoài giải ngân hai mươi mốt phẩy không bảy tỷ đô la, tăng mười hai phẩy một. Ngành nối là cảng biển và logistics, ví dụ G M D, '
         'lợi nhuận quý hai tăng một trăm năm mươi hai phẩy năm phần trăm. Câu hỏi nên đặt: lãi đến từ hoạt động cảng hay từ doanh thu tài chính? Dữ liệu ghi lãi phụ thuộc nhiều '
         'vào doanh thu tài chính.'},
 {'k': 'cards',
  'label': 'BÁN LẺ & DU LỊCH',
  'cap': ('BÁN LẺ &', 'DU LỊCH'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'cards': [('Bán lẻ + dịch vụ 9 tháng', '+13,4%', 'Cục Thống kê'), ('Lữ hành 9 tháng', '+17,9%', 'Cục Thống kê'), ('MWG – bán lẻ', 'LNST quý 3 +74,7%', 'so cùng kỳ')],
  'anh': 'electronics retail store',
  'say': 'Biến số tám: bán lẻ và du lịch. Theo Cục Thống kê, tổng mức bán lẻ hàng hóa và doanh thu dịch vụ tiêu dùng chín tháng tăng mười ba phẩy bốn phần trăm, lữ hành tăng mười '
         'bảy phẩy chín. Ngành nối là bán lẻ, ví dụ M W G, lợi nhuận quý ba tăng bảy mươi bốn phẩy bảy phần trăm. Câu hỏi nên đặt: doanh thu tăng nhờ mở rộng hay nhờ sức mua, và '
         'biên gộp ra sao?'},
 {'k': 'bars',
  'ch': 'Chương 6 – Cùng vĩ mô, mỗi nơi một kết quả',
  'moc': True,
  'label': 'TĂNG TRƯỞNG LNST SO CÙNG KỲ',
  'cap': ('MỖI NƠI', 'MỘT KẾT QUẢ'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'bars': [('BSR Q3', 888.2, [34, 197, 94], '+888,2%'),
           ('POW Q2', 460.3, [34, 197, 94], '+460,3%'),
           ('GMD Q2', 152.5, [34, 197, 94], '+152,5%'),
           ('HPG Q3', 106.0, [34, 197, 94], '+106,0%'),
           ('MWG Q3', 74.7, [34, 197, 94], '+74,7%'),
           ('VCB Q3', 0.1, [56, 189, 248], '+0,1%'),
           ('SSI Q3', -23.7, [239, 68, 68], '−23,7%')],
  'anh': 'financial charts analysis',
  'say': 'Đặt các con số cạnh nhau, B S R tăng tám trăm tám mươi tám phẩy hai phần trăm, P O W bốn trăm sáu mươi phẩy ba, G M D một trăm năm mươi hai phẩy năm, H P G một trăm '
         'linh sáu phẩy không, M W G bảy mươi bốn phẩy bảy, V C B chỉ không phẩy một, còn S S I giảm hai mươi ba phẩy bảy. Lưu ý P O W và G M D là quý hai. Cùng một môi trường vĩ '
         'mô, kết quả mỗi nơi một khác. Biến số vĩ mô chỉ là điểm xuất phát, phần còn lại do mô hình kinh doanh, chi phí và nợ vay quyết định.'},
 {'k': 'checklist',
  'label': 'QUY TRÌNH 5 BƯỚC',
  'cap': ('QUY TRÌNH', '5 BƯỚC'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'items': [('1. Chọn biến số, ghi nguồn chính thống', [255, 196, 0]),
            ('2. Xác định ngành nhạy với biến số', [56, 189, 248]),
            ('3. Mở báo cáo: doanh thu, biên gộp, lãi vay, LNST', [34, 197, 94]),
            ('4. So cùng kỳ và quý trước, ghi rõ mốc quý', [239, 68, 68]),
            ('5. Hỏi: cơ chế hay nhất thời? Đọc giải trình gốc', [255, 196, 0])],
  'anh': 'person analyzing financial statements',
  'say': 'Cuối cùng là quy trình năm bước. Một, chọn một biến số và ghi nguồn chính thống. Hai, xác định ngành nhạy với biến số đó. Ba, mở báo cáo, nhìn doanh thu, biên gộp, chi '
         'phí lãi vay và lợi nhuận sau thuế. Bốn, so cả cùng kỳ lẫn quý trước, và ghi rõ mốc quý. Năm, tự hỏi đây là cơ chế hay chỉ nhất thời, rồi đọc giải trình ở báo cáo gốc. '
         'Làm đủ năm bước, bạn đã nối được vĩ mô với báo cáo tài chính.'},
 {'k': 'end',
  'label': '',
  'cap': ('NGUỒN &', 'LƯU Ý'),
  'cols': ([255, 255, 255], [255, 196, 0]),
  'say': 'Nguồn: Cục Thống kê, Ngân hàng Nhà nước, Fed, dữ liệu thị trường của kênh, báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu, riêng P O W và G M D là quý '
         'hai. Đây là chia sẻ kiến thức, không phải khuyến nghị mua bán. Câu hỏi cho bạn: trong tám biến số, bạn muốn kênh đào sâu biến số nào? Xem thêm tại chungkhoanhuynguyen '
         'chấm com.'}]

if __name__ == "__main__":
    for k, sc in S.items():
        n = sum(len(s["say"].split()) for s in sc)
        print(k, "số từ:", n, "· phút ≈", round(n / 170, 1))
