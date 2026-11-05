# -*- coding: utf-8 -*-
# VIDEO DÀI KÊNH CHÍNH – NV1 soạn 06/11/2026 (lô 20261106_0100: CH1111A, CH1111B, CH1111C, CH1211A, CH1211B, CH1211C). Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['CH1111A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'MBB – Đọc BCTC 5 phút',
  'cap': ('LÃI QUÝ 3 +44,3%', 'NỢ XẤU VẪN TĂNG?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'MBBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[14, 23.63, 'Đỉnh tuần 9/2/26: 23,63', 0.6], [37, 17.78, 'Đáy tuần 27/7/26: 17,78', 1.6], [51, 19.5, 'Đóng tuần 2/11/26: 19,50', 2.6]]},
  'anh': 'bank building vietnam',
  'say': 'Một ngân hàng báo lợi nhuận quý ba tăng bốn mươi bốn phẩy ba phần trăm so với cùng kỳ, đạt tám nghìn không trăm ba mươi chín tỷ đồng chỉ trong ba tháng. Nghe như một '
         'tin vui tuyệt đối. Nhưng cũng trong báo cáo đó, tỷ lệ nợ xấu lại nhích từ một phẩy bốn mươi lăm phần trăm lên một phẩy sáu mươi bảy phần trăm. Vậy lợi nhuận tăng mạnh '
         'và nợ xấu tăng cùng lúc thì nên đọc là tốt hay xấu? Trong video này mình mổ xẻ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của Ngân hàng Quân đội, mã '
         'MBB, theo khung năm bước mà bạn dùng được cho bất kỳ ngân hàng nào: lợi nhuận, thu nhập lãi thuần, lãi dịch vụ, nợ xấu cùng bao phủ, và cuối cùng là định giá. Xem hết, '
         'bạn sẽ biết con số nào đáng tin nhất, con số nào cần đọc kỹ hơn, và vì sao một quý lãi đẹp chưa phải là câu trả lời. Video thuộc seri Đọc BCTC năm phút. Số liệu là ví '
         'dụ minh họa tại ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, còn cách đọc thì dùng được nhiều năm. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Bước 1: Lợi nhuận sau thuế qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ MBB theo quý (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 5571.0, (56, 189, 248), '5.571'),
           ('Q4/25', 8763.0, (56, 189, 248), '8.763'),
           ('Q1/26', 7516.0, (56, 189, 248), '7.516'),
           ('Q2/26', 8229.0, (56, 189, 248), '8.229'),
           ('Q3/26', 8039.0, (34, 197, 94), '8.039')],
  'anh': 'financial report charts',
  'say': 'Bước một là nhìn lợi nhuận sau thuế của công ty mẹ qua nhiều quý, không chỉ một quý. Quý ba năm hai nghìn không trăm hai mươi sáu, MBB lãi tám nghìn không trăm ba mươi '
         'chín tỷ đồng, cao hơn bốn mươi bốn phẩy ba phần trăm so với năm nghìn năm trăm bảy mươi mốt tỷ của quý ba năm hai nghìn không trăm hai mươi lăm. Lũy kế chín tháng đạt '
         'hai mươi ba nghìn bảy trăm tám mươi bốn tỷ, tăng ba mươi hai phẩy không phần trăm. Nhìn riêng con số này thì rất đẹp. Nhưng hãy để ý hai điều. Thứ nhất, quý ba năm '
         'ngoái là một nền khá thấp, nên mức tăng nhìn lớn hơn thực tế. Thứ hai, so với quý hai năm hai nghìn không trăm hai mươi sáu là tám nghìn hai trăm hai mươi chín tỷ thì '
         'quý ba giảm khoảng hai phẩy ba phần trăm. Nghĩa là đà tăng so cùng kỳ rất mạnh, nhưng lợi nhuận hằng quý gần đây đi ngang quanh mức tám nghìn tỷ. Bài học đầu tiên: luôn '
         'đặt ba phép so sánh cạnh nhau, so với cùng kỳ, so với quý trước, và so với mức trung bình bốn quý. Một phép so sánh đơn lẻ rất dễ dẫn bạn đến kết luận vội.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Bước 2: Thu nhập lãi thuần, động cơ của ngân hàng',
  'moc': True,
  'label': 'Thu nhập lãi thuần MBB theo quý (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 12991.0, (56, 189, 248), '12.991'),
           ('Q4/25', 14555.0, (56, 189, 248), '14.555'),
           ('Q1/26', 14913.0, (56, 189, 248), '14.913'),
           ('Q2/26', 16894.0, (56, 189, 248), '16.894'),
           ('Q3/26', 17836.0, (34, 197, 94), '17.836')],
  'anh': 'bank loans money counting',
  'say': 'Bước hai là thu nhập lãi thuần, tức tiền lãi ngân hàng thu từ cho vay trừ đi tiền lãi phải trả cho người gửi tiết kiệm. Hãy hình dung một tiệm tạp hóa: mua hàng giá rẻ, '
         'bán lại giá cao hơn, phần chênh lệch là lời. Ngân hàng cũng vậy, nhưng hàng hóa là tiền. Quý ba, MBB có mười bảy nghìn tám trăm ba mươi sáu tỷ thu nhập lãi thuần, tăng '
         'ba mươi bảy phẩy ba phần trăm so với mười hai nghìn chín trăm chín mươi mốt tỷ cùng kỳ. Điều đáng chú ý là con số này tăng liên tục qua năm quý liền, từ mười hai nghìn '
         'chín trăm chín mươi mốt lên mười bốn nghìn năm trăm năm mươi lăm, mười bốn nghìn chín trăm mười ba, mười sáu nghìn tám trăm chín mươi bốn rồi mười bảy nghìn tám trăm ba '
         'mươi sáu. Đây là dấu hiệu của hoạt động cốt lõi đang mở rộng thật, không phải do một khoản thu bất thường. Với ngân hàng, nếu lợi nhuận lên xuống thất thường nhưng thu '
         'nhập lãi thuần tăng đều, thì thường hoạt động cốt lõi vẫn khỏe. Ngược lại, nếu lợi nhuận đẹp mà thu nhập lãi thuần đi ngang, bạn cần tìm xem phần tăng đến từ đâu.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Bước 3: Lãi dịch vụ và cấu trúc thu nhập',
  'moc': True,
  'label': 'Quý 3/2026 theo dữ liệu tổng hợp',
  'cap': ('CẤU TRÚC', 'THU NHẬP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Thu nhập lãi thuần', '17.836 tỷ', 'tăng 37,3%'), ('Lãi dịch vụ', '1.678 tỷ', 'tăng 26,5%'), ('LNST công ty mẹ', '8.039 tỷ', 'tăng 44,3%')],
  'anh': 'bank customer service',
  'say': 'Bước ba là xem ngân hàng kiếm tiền từ đâu ngoài cho vay. Lãi dịch vụ gồm phí thanh toán, phí bảo lãnh, phí bảo hiểm bán qua ngân hàng. Quý ba, MBB thu một nghìn sáu '
         'trăm bảy mươi tám tỷ từ dịch vụ, tăng hai mươi sáu phẩy năm phần trăm, nhưng chỉ bằng khoảng chín phẩy bốn phần trăm so với thu nhập lãi thuần. Nói cách khác, ngân hàng '
         'này vẫn sống chủ yếu bằng chênh lệch lãi suất. Điều đó không xấu, nhưng nó có nghĩa là kết quả phụ thuộc nhiều vào chu kỳ tín dụng và lãi suất. Một chi tiết thú vị: lợi '
         'nhuận sau thuế tăng bốn mươi bốn phẩy ba phần trăm, nhanh hơn thu nhập lãi thuần ba mươi bảy phẩy ba phần trăm. Khi lợi nhuận tăng nhanh hơn thu nhập, thường là chi phí '
         'hoạt động hoặc chi phí dự phòng tăng chậm hơn thu nhập. Bạn nên mở báo cáo xem hai dòng đó để hiểu mức tăng này bền hay chỉ đến từ việc trích lập ít đi trong một quý.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Bước 4: Nợ xấu và bao phủ nợ xấu',
  'moc': True,
  'label': 'MBB quý 3/2026, so với hai ngân hàng khác trong dữ liệu',
  'cap': ('NỢ XẤU &', 'BAO PHỦ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('MBB', 'nợ xấu 1,67%', 'bao phủ khoảng 85%'), ('TCB', 'nợ xấu 1,27%', 'bao phủ khoảng 107%'), ('ACB', 'nợ xấu 1,19%', 'bao phủ khoảng 91%')],
  'anh': 'bank risk analysis',
  'say': 'Bước bốn là phần quan trọng nhất với một ngân hàng: chất lượng tài sản. Tỷ lệ nợ xấu của MBB quý ba là một phẩy sáu mươi bảy phần trăm, tăng không phẩy hai mươi hai '
         'điểm phần trăm so với một phẩy bốn mươi lăm phần trăm của quý trước. Bao phủ nợ xấu khoảng tám mươi lăm phần trăm, nghĩa là mỗi một đồng nợ xấu có khoảng tám mươi lăm '
         'xu dự phòng. Dưới một trăm phần trăm không có nghĩa là nguy hiểm ngay, vì khoản vay thường còn tài sản đảm bảo, nhưng đệm bảo vệ mỏng hơn. Để có cảm giác so sánh, trong '
         'cùng bộ dữ liệu, Techcombank có nợ xấu một phẩy hai mươi bảy phần trăm và bao phủ khoảng một trăm linh bảy phần trăm, ACB có nợ xấu một phẩy mười chín phần trăm và bao '
         'phủ khoảng chín mươi mốt phần trăm. Mỗi ngân hàng có mô hình khác nhau nên không so cứng, nhưng bạn thấy rõ hai con số này phải đọc cùng nhau. Nợ xấu tăng trong khi bao '
         'phủ không dày thêm là tín hiệu cần theo dõi ở các quý sau.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Bước 5: Hiệu quả và định giá',
  'moc': True,
  'label': 'Dữ liệu tổng hợp 5/11/2026',
  'cap': ('ROE, ROA', 'P/E, P/B'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE', '21,8%', '4 quý gần nhất'), ('ROA', '2,0%', 'tài sản gấp ~11 lần vốn'), ('P/E · P/B', '5,96 · 1,23', 'lần')],
  'anh': 'calculator stock valuation',
  'say': 'Bước năm là hiệu quả sinh lời và định giá. Theo dữ liệu tổng hợp ngày ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, ROE của MBB khoảng hai mươi mốt '
         'phẩy tám phần trăm, ROA khoảng hai phẩy không phần trăm, P/E năm phẩy chín mươi sáu lần và P/B một phẩy hai mươi ba lần. Lấy ROE chia ROA ra khoảng mười phẩy chín, '
         'nghĩa là tổng tài sản lớn gấp gần mười một lần vốn chủ sở hữu. Đó là đòn bẩy đặc trưng của ngân hàng: vay của dân để cho vay lại, nên chỉ cần một phần nhỏ tài sản gặp '
         'rủi ro cũng ảnh hưởng đáng kể tới vốn. Vì vậy với ngân hàng, người ta thường nhìn P/B cùng ROE chứ không chỉ P/E. P/B một phẩy hai mươi ba đi cùng ROE hai mươi mốt phẩy '
         'tám phần trăm là một cách mô tả thị trường đang định giá lợi nhuận ra sao, không phải lời khuyên mua hay bán. Điều cần nhớ: định giá thấp có thể phản ánh nỗi lo về nợ '
         'xấu, nên đừng đọc P/B tách khỏi bước bốn.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Ba câu hỏi nên đặt thêm',
  'moc': True,
  'label': 'Khi đã đọc xong năm bước',
  'cap': ('3 CÂU HỎI', 'THÊM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Nợ xấu tăng ở nhóm khách hàng hay ngành nào?', (56, 189, 248)),
            ('Dự phòng có được bồi đắp để bao phủ nợ xấu không?', (34, 197, 94)),
            ('Lợi nhuận quý có khoản bất thường nào không?', (255, 196, 0)),
            ('Tăng trưởng tín dụng có vượt mức vốn cho phép?', (239, 68, 68))],
  'anh': 'analyst reading report',
  'say': 'Sau khi đọc năm bước, người đọc kỹ sẽ đặt thêm ba câu hỏi. Câu một: nợ xấu tăng ở đâu? Nếu tăng ở một nhóm ngành hay một vài khoản lớn, rủi ro khác hẳn với việc tăng '
         'dàn trải. Bạn tìm câu trả lời trong thuyết minh báo cáo tài chính. Câu hai: dự phòng có được bồi đắp không? Nếu nợ xấu tăng mà chi phí dự phòng giảm, lợi nhuận có thể '
         'đang được hỗ trợ bởi việc trích ít hơn, và đó là điều cần thận trọng. Câu ba: có khoản thu nhập bất thường nào không, ví dụ thoái vốn, thu hồi nợ đã xóa, hay lãi từ đầu '
         'tư? Những khoản này đẹp nhưng không lặp lại. Thêm một câu nữa dành cho người học sâu hơn: tăng trưởng tín dụng có quá nhanh so với vốn của ngân hàng không, vì mở rộng '
         'nhanh luôn đi kèm rủi ro chất lượng. Bốn câu hỏi này giúp bạn không dừng ở tiêu đề báo chí.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những cái bẫy khi đọc báo cáo ngân hàng',
  'moc': True,
  'label': 'Bốn điều dễ nhầm',
  'cap': ('4 CÁI BẪY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Chỉ so với cùng kỳ năm trước, bỏ quên quý liền kề', (239, 68, 68)),
            ('Nhìn lợi nhuận mà bỏ qua chi phí dự phòng', (239, 68, 68)),
            ('Coi P/E thấp là rẻ mà không xem nợ xấu', (239, 68, 68)),
            ('Lấy một quý đại diện cho cả năm', (239, 68, 68))],
  'anh': 'warning sign caution',
  'say': 'Bốn cái bẫy thường gặp khi đọc báo cáo ngân hàng. Bẫy một: chỉ so với cùng kỳ năm trước. Nếu cùng kỳ là nền thấp, mức tăng nhìn rất lớn, như trường hợp bốn mươi bốn '
         'phẩy ba phần trăm ở trên. Bạn phải xem thêm quý liền kề. Bẫy hai: nhìn lợi nhuận mà bỏ qua chi phí dự phòng. Dự phòng là khoản ngân hàng tự trích để phòng nợ xấu, giảm '
         'trích thì lợi nhuận tăng, nhưng đệm an toàn mỏng đi. Bẫy ba: thấy P/E chỉ gần sáu lần là kết luận rẻ. P/E thấp ở ngân hàng đôi khi phản ánh kỳ vọng lợi nhuận sẽ giảm '
         'hoặc lo ngại chất lượng tài sản. Bẫy bốn: lấy một quý đại diện cho cả năm. Ngân hàng có tính mùa vụ, có khoản thu bất thường rơi vào quý này mà không rơi vào quý khác. '
         'Cách tránh cả bốn bẫy là nhìn chuỗi tám đến mười hai quý thay vì một điểm.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Khung 5 bước đọc ngân hàng',
  'cap': ('5 BƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Lợi nhuận: ba phép so sánh', (56, 189, 248)),
            ('2. Thu nhập lãi thuần: động cơ cốt lõi', (56, 189, 248)),
            ('3. Lãi dịch vụ: nguồn thu thứ hai', (56, 189, 248)),
            ('4. Nợ xấu + bao phủ: chất lượng tài sản', (34, 197, 94)),
            ('5. ROE + P/B: hiệu quả và giá', (255, 196, 0))],
  'anh': 'checklist notebook pen',
  'say': 'Tổng kết lại. Mười năm nữa các con số của MBB sẽ khác, nhưng khung năm bước này vẫn dùng được. Một, lợi nhuận với ba phép so sánh. Hai, thu nhập lãi thuần, động cơ cốt '
         'lõi. Ba, lãi dịch vụ, nguồn thu thứ hai. Bốn, nợ xấu đi cùng bao phủ, chất lượng tài sản. Năm, ROE cùng P/B, hiệu quả và giá thị trường đang trả. Trong ví dụ này, bức '
         'tranh cân bằng như sau: lợi nhuận và thu nhập lãi thuần tăng mạnh, lãi dịch vụ tăng khá, nhưng nợ xấu nhích lên và bao phủ chưa dày. Cả hai mặt đều có thật, và việc của '
         'bạn là theo dõi xem quý sau mặt nào thay đổi. Hãy thử làm bài tập: mở báo cáo của một ngân hàng bạn quan tâm, điền năm dòng này ra giấy, mất khoảng mười lăm phút. Làm '
         'vài lần, bạn sẽ đọc nhanh hơn rất nhiều. Nếu thấy hữu ích, hãy lưu video để xem lại mỗi mùa báo cáo.'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐỌC BCTC 5 PHÚT', 'MBB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu lấy từ báo cáo tài chính hợp nhất quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày ngày năm tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu, mang tính minh họa cách đọc. Biểu đồ chỉ là hình nền. Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem tiếp '
         'seri Đọc BCTC năm phút.'}]

S['CH1111B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VNM – hình nền minh họa',
  'cap': ('LÃI 100 TỶ NHƯNG', 'TIỀN ÂM 40 TỶ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNMW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 54.52, 'Đáy tuần 3/11/25: 54,52', 0.6], [11, 73.11, 'Đỉnh tuần 19/1/26: 73,11', 1.6], [51, 57.5, '5/11/26: 57,50', 2.6]]},
  'anh': 'cash flow money coins',
  'say': 'Hãy tưởng tượng một công ty báo cáo lãi sau thuế một trăm tỷ đồng trong năm, lợi nhuận tăng đều ba năm liền. Nhưng khi mở báo cáo lưu chuyển tiền tệ, dòng tiền kinh '
         'doanh lại âm bốn mươi tỷ. Công ty lãi trên giấy, nhưng trong két sắt không có thêm đồng nào, thậm chí còn phải đi vay để trả lương. Chuyện này có thật, và nó là lý do '
         'nhiều doanh nghiệp báo lãi vẫn rơi vào khủng hoảng thanh khoản. Trong video này mình giải thích vì sao lợi nhuận và tiền mặt có thể lệch nhau, cách đọc báo cáo lưu '
         'chuyển tiền tệ trong năm phút, và bốn dấu hiệu cảnh báo bạn có thể tự kiểm tra. Xem hết, bạn sẽ biết cách nhìn vào một báo cáo và hỏi đúng câu: lãi này đã biến thành '
         'tiền chưa? Video thuộc seri Nền tảng đầu tư. Các con số trong bài là số giả định để tính, còn nguyên tắc thì đúng ở mọi thị trường và mọi thời kỳ. Biểu đồ phía sau chỉ '
         'là hình nền.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Lãi kế toán không phải là tiền thật',
  'moc': True,
  'label': 'Ví dụ giả định: một năm của công ty A',
  'cap': ('LÃI ≠ TIỀN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Doanh thu ghi nhận', '1.000 tỷ', 'đã xuất hóa đơn'), ('Tiền thực thu', '600 tỷ', 'khách đã trả'), ('Khoản phải thu', '+400 tỷ', 'khách còn nợ')],
  'anh': 'invoice accounting desk',
  'say': 'Kế toán ghi nhận doanh thu khi hàng đã giao và hóa đơn đã xuất, không đợi khách trả tiền. Giả sử công ty A bán được một nghìn tỷ hàng trong năm, nhưng khách mới trả sáu '
         'trăm tỷ, còn bốn trăm tỷ nằm ở khoản phải thu. Trên báo cáo kết quả kinh doanh, toàn bộ một nghìn tỷ vẫn là doanh thu và công ty vẫn có lãi. Nhưng chủ nợ, nhân viên và '
         'nhà cung cấp không nhận được lãi, họ nhận tiền. Đó là khác biệt gốc rễ: lợi nhuận đo hiệu quả theo nguyên tắc kế toán dồn tích, còn dòng tiền đo tiền thật vào ra tài '
         'khoản. Cả hai đều quan trọng, nhưng nếu phải chọn một thứ để kiểm tra độ thật của lợi nhuận, thì dòng tiền kinh doanh là phép thử đơn giản nhất. Một công ty có thể sống '
         'nhiều năm với lợi nhuận thấp nếu tiền về đều, nhưng không sống nổi một năm nếu tiền cạn.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Ba dòng tiền trong một báo cáo',
  'moc': True,
  'label': 'Báo cáo lưu chuyển tiền tệ',
  'cap': ('3 DÒNG TIỀN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Kinh doanh: tiền từ hoạt động chính', (34, 197, 94)),
            ('Đầu tư: mua tài sản, xây nhà máy, góp vốn', (56, 189, 248)),
            ('Tài chính: vay nợ, trả nợ, phát hành, cổ tức', (255, 196, 0)),
            ('Cộng ba dòng = thay đổi tiền trong năm', (255, 255, 255))],
  'anh': 'financial statement cash',
  'say': 'Báo cáo lưu chuyển tiền tệ chia dòng tiền thành ba nhóm. Một, dòng tiền từ hoạt động kinh doanh: tiền thu từ khách trừ tiền trả nhà cung cấp, lương và thuế. Đây là dòng '
         'quan trọng nhất vì nó cho biết hoạt động chính có tự nuôi được mình không. Hai, dòng tiền từ hoạt động đầu tư: mua sắm máy móc, xây nhà máy, mua cổ phần công ty khác. '
         'Dòng này thường âm ở công ty đang mở rộng, và âm không có nghĩa là xấu. Ba, dòng tiền từ hoạt động tài chính: đi vay, trả nợ gốc, phát hành cổ phiếu, trả cổ tức. Cộng '
         'ba dòng lại bạn có mức thay đổi tiền trong năm. Một công ty khỏe thường có dòng kinh doanh dương, dòng đầu tư âm vì đang mở rộng, và dòng tài chính linh hoạt. Công ty '
         'yếu thì ngược lại: kinh doanh âm, phải bù bằng đi vay ở dòng tài chính.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Từ lợi nhuận sang tiền: phép cầu nối',
  'moc': True,
  'label': 'Ví dụ giả định, đơn vị tỷ đồng',
  'cap': ('CẦU NỐI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lợi nhuận sau thuế: +100', (34, 197, 94)),
            ('Cộng khấu hao, không mất tiền: +20', (34, 197, 94)),
            ('Phải thu tăng, khách chưa trả: −120', (239, 68, 68)),
            ('Hàng tồn kho tăng, tiền nằm trong kho: −60', (239, 68, 68)),
            ('Phải trả tăng, chưa trả nhà cung cấp: +20', (34, 197, 94)),
            ('Dòng tiền kinh doanh: −40', (255, 196, 0))],
  'anh': 'bridge construction steel',
  'say': 'Phép cầu nối giúp bạn thấy lợi nhuận biến thành tiền, hoặc không, ở đâu. Bắt đầu từ lợi nhuận sau thuế một trăm tỷ. Cộng lại khấu hao hai mươi tỷ, vì đó là chi phí ghi '
         'sổ nhưng không mất tiền thật. Trừ đi khoản phải thu tăng một trăm hai mươi tỷ, vì doanh thu đã ghi nhưng tiền chưa về. Trừ đi hàng tồn kho tăng sáu mươi tỷ, vì tiền đã '
         'bỏ ra mua hàng nhưng chưa bán. Cộng khoản phải trả tăng hai mươi tỷ, vì công ty giữ lại tiền chưa trả nhà cung cấp. Cộng trừ tất cả, dòng tiền kinh doanh là âm bốn mươi '
         'tỷ. Phép tính này cho thấy lợi nhuận một trăm tỷ đã bị hút vào phải thu và hàng tồn kho. Khi bạn thấy dòng tiền kinh doanh thấp hơn lợi nhuận nhiều, hãy tìm xem khoản '
         'nào trong bảng cân đối đã tăng mạnh. Câu trả lời thường nằm đúng ở hai dòng đó.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Hai thước đo kiểm tra nhanh',
  'moc': True,
  'label': 'Công thức và ngưỡng tham khảo',
  'cap': ('2 THƯỚC ĐO',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('CFO ÷ LNST', '≥ 0,8–1,0', 'tiền thật theo kịp lãi'),
            ('Dòng tiền tự do', 'CFO − chi đầu tư', 'tiền còn lại cho cổ đông'),
            ('Ví dụ A', '−40 ÷ 100', '= −0,4: cảnh báo')],
  'anh': 'calculator financial ratios',
  'say': 'Có hai thước đo nhanh bạn nên thuộc. Thước đo thứ nhất là tỷ lệ dòng tiền kinh doanh trên lợi nhuận sau thuế. Nếu tỷ lệ này quanh một, nghĩa là mỗi đồng lãi có một đồng '
         'tiền về, lợi nhuận đáng tin. Nếu thấp dưới không phẩy tám trong nhiều năm liền, hãy hỏi vì sao. Với công ty A, tỷ lệ là âm không phẩy bốn, một tín hiệu cần xem xét kỹ. '
         'Thước đo thứ hai là dòng tiền tự do, bằng dòng tiền kinh doanh trừ chi tiêu mua sắm tài sản cố định. Đó là phần tiền còn lại sau khi duy trì và mở rộng hoạt động, có '
         'thể dùng để trả nợ, chia cổ tức hoặc tích lũy. Doanh nghiệp có dòng tiền tự do dương ổn định qua nhiều năm thường có nền tảng bền. Hai ngưỡng này chỉ để tham khảo, vì '
         'mỗi ngành khác nhau và một năm đơn lẻ có thể bị méo bởi một khoản thu chi lớn.'},
 {'k': 'cards',
  'ch': 'Chương 5 – So sánh hai công ty cùng ngành',
  'moc': True,
  'label': 'Ví dụ giả định, đơn vị tỷ đồng',
  'cap': ('A HAY B?',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Công ty A', 'lãi 100', 'dòng tiền −40'), ('Công ty B', 'lãi 60', 'dòng tiền +70'), ('Câu hỏi', 'tiền về hay nợ?', 'đọc phải thu, tồn kho')],
  'anh': 'two businesses comparison',
  'say': 'Hãy so sánh hai công ty giả định trong cùng ngành. Công ty A báo lãi một trăm tỷ nhưng dòng tiền kinh doanh âm bốn mươi tỷ. Công ty B báo lãi chỉ sáu mươi tỷ nhưng dòng '
         'tiền kinh doanh dương bảy mươi tỷ. Nhìn riêng báo cáo kết quả kinh doanh, A có vẻ mạnh hơn. Nhìn qua tiền thật, B vững hơn: tiền về nhiều hơn lãi, nghĩa là khách trả '
         'đúng hạn, hàng bán được, và công ty không cần vay để nuôi hoạt động. Điều này không có nghĩa A chắc chắn tệ. Có thể A đang tăng trưởng nhanh nên tạm thời phải ứng tiền '
         'cho khách, và nếu khoản phải thu thu được trong quý sau thì mọi thứ ổn. Nhưng bạn cần biết đó là giả thuyết cần kiểm tra, chứ không phải sự thật hiển nhiên. Cách kiểm '
         'tra: xem khoản phải thu đã thu được trong các quý kế tiếp chưa, và dòng tiền có trở lại dương không.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Bốn dấu hiệu cảnh báo',
  'moc': True,
  'label': 'Tự kiểm tra trong 5 phút',
  'cap': ('4 CỜ ĐỎ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lãi tăng nhiều năm nhưng dòng tiền kinh doanh âm kéo dài', (239, 68, 68)),
            ('Phải thu tăng nhanh hơn doanh thu', (239, 68, 68)),
            ('Vay mới để trả nợ cũ hoặc trả cổ tức', (239, 68, 68)),
            ('Chi đầu tư lớn mà không có nguồn tiền từ hoạt động chính', (239, 68, 68))],
  'anh': 'warning red flag',
  'say': 'Bốn cờ đỏ bạn có thể tự kiểm tra trong năm phút. Một, lãi tăng nhiều năm nhưng dòng tiền kinh doanh âm kéo dài. Một năm âm có thể do thời vụ, ba năm âm thì cần lý do '
         'rất thuyết phục. Hai, khoản phải thu tăng nhanh hơn doanh thu. Nếu doanh thu tăng mười phần trăm mà phải thu tăng bốn mươi phần trăm, doanh nghiệp có thể đang nới tín '
         'dụng để đẩy doanh số. Ba, đi vay mới để trả nợ cũ hoặc trả cổ tức. Đó là dấu hiệu hoạt động chính không tự đủ tiền. Bốn, chi đầu tư lớn mà không có nguồn tiền từ hoạt '
         'động chính, tức mở rộng bằng nợ. Mở rộng bằng nợ không sai, nhưng khi lãi suất tăng hoặc doanh thu chậm lại, gánh nặng lãi vay sẽ làm lợi nhuận mỏng đi rất nhanh. Cờ đỏ '
         'không phải bản án, nó chỉ là lý do để đọc kỹ thuyết minh trước khi tin con số lợi nhuận.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những ngoại lệ cần nhớ',
  'moc': True,
  'label': 'Không phải lúc nào dòng tiền âm cũng xấu',
  'cap': ('NGOẠI LỆ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Công ty đang tăng trưởng nhanh cần ứng vốn lưu động', (56, 189, 248)),
            ('Ngành xây dựng, bất động sản ghi nhận theo tiến độ', (56, 189, 248)),
            ('Ngân hàng, bảo hiểm: dòng tiền kinh doanh đọc khác', (56, 189, 248)),
            ('Nhìn chuỗi ít nhất 3 năm, không chỉ một năm', (255, 196, 0))],
  'anh': 'construction site progress',
  'say': 'Cần thận trọng vì quy tắc dòng tiền có ngoại lệ. Công ty đang tăng trưởng nhanh thường phải ứng thêm vốn lưu động cho khách và hàng tồn kho, nên dòng tiền kinh doanh có '
         'thể âm tạm thời dù hoạt động lành mạnh. Ngành xây dựng và bất động sản ghi nhận doanh thu theo tiến độ hoặc bàn giao, thời điểm thu tiền và ghi nhận lệch nhau nhiều '
         'năm, nên một năm đơn lẻ rất dễ gây hiểu lầm. Với ngân hàng và bảo hiểm, cấu trúc bảng khác hẳn, dòng tiền kinh doanh gồm cả tiền gửi và cho vay, nên không dùng ngưỡng '
         'trên được. Vì vậy quy tắc vàng là nhìn chuỗi ít nhất ba năm và đặt dòng tiền cạnh ngành nghề. Khi một con số làm bạn lo, đừng kết luận ngay, hãy đọc thuyết minh để biết '
         'lý do cụ thể. Người đọc báo cáo giỏi không phải người thuộc nhiều ngưỡng, mà là người biết hỏi đúng câu.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Ba câu hỏi cho mọi báo cáo',
  'cap': ('3 CÂU HỎI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lãi này đã thành tiền chưa?', (255, 196, 0)),
            ('Tiền đến từ hoạt động chính hay từ đi vay?', (255, 196, 0)),
            ('Sau khi đầu tư, còn tiền tự do không?', (255, 196, 0))],
  'anh': 'notebook pen thinking',
  'say': 'Tổng kết lại bằng ba câu hỏi bạn có thể dùng cho mọi báo cáo tài chính trong mười năm tới. Câu một: lãi này đã thành tiền chưa? Hãy so dòng tiền kinh doanh với lợi '
         'nhuận, và tìm phải thu, tồn kho ở đâu. Câu hai: tiền đến từ hoạt động chính hay từ đi vay? Nếu hoạt động chính không tạo ra tiền, mọi thứ khác chỉ là kéo dài thời gian. '
         'Câu ba: sau khi trừ chi đầu tư, còn bao nhiêu tiền tự do? Đó mới là phần thực sự thuộc về cổ đông. Có một bài tập nhỏ: chọn một doanh nghiệp bạn quan tâm, mở báo cáo '
         'lưu chuyển tiền tệ của ba năm gần nhất, và trả lời ba câu hỏi này bằng số. Mất khoảng mười lăm phút nhưng bạn sẽ hiểu doanh nghiệp đó hơn nhiều người chỉ nhìn giá. Lợi '
         'nhuận có thể được trình bày khéo, còn tiền trong tài khoản thì khó giả. Hãy lưu video này để xem lại mỗi mùa báo cáo.'},
 {'k': 'end',
  'label': '',
  'cap': ('DÒNG TIỀN THẬT', 'HAY LÃI GIẤY?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các ví dụ trong video là số giả định để minh họa, không phải số liệu của doanh nghiệp cụ thể. Biểu đồ chỉ là hình nền. Nội dung chia sẻ kiến thức, không phải khuyến '
         'nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Nền tảng đầu tư.'}]

S['CH1111C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – hình nền minh họa',
  'cap': ('VN-INDEX MẤT 80%', 'TRONG 2 NĂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, 'Đóng tuần 2/11/26: 1.741', 2.6]]},
  'anh': 'vietnam stock exchange 2007',
  'say': 'Tháng ba năm hai nghìn không trăm linh bảy, VN-Index chạm khoảng một nghìn một trăm bảy mươi điểm, và nhiều người tin rằng chứng khoán là cách làm giàu chắc chắn nhất '
         'đất nước. Chưa đầy hai năm sau, tháng hai năm hai nghìn không trăm linh chín, chỉ số rơi về khoảng hai trăm ba mươi lăm điểm. Mất gần tám mươi phần trăm giá trị. Câu '
         'hỏi không phải là vì sao thị trường giảm, mà là vì sao gần như không ai bán ở vùng đỉnh. Trong video này mình kể lại giai đoạn hai nghìn không trăm linh sáu đến hai '
         'nghìn không trăm linh chín theo ba lớp: điều gì đã đẩy thị trường lên, điều gì làm nó sụp, và những phép tính vì sao thua lỗ lớn lại khó gỡ đến vậy. Xem hết, bạn sẽ có '
         'một danh sách dấu hiệu bong bóng áp dụng được ở bất kỳ thời kỳ nào, và một phép tính làm bạn nghĩ lại về cắt lỗ. Video thuộc seri Bài học lịch sử. Các mốc điểm số là số '
         'làm tròn theo thông tin công khai, có thể chênh nhẹ. Biểu đồ phía sau chỉ là hình nền minh họa, không phải giai đoạn hai nghìn không trăm linh bảy.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Ba mốc cần nhớ',
  'moc': True,
  'label': 'Số làm tròn theo thông tin công khai',
  'cap': ('3 MỐC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Cuối năm 2006', '~751 điểm', 'sau năm tăng rất mạnh'), ('Đỉnh 12/3/2007', '~1.170 điểm', 'kỷ lục lúc đó'), ('Đáy tháng 2/2009', '~235 điểm', 'mất gần 80% từ đỉnh')],
  'anh': 'old stock exchange screen',
  'say': 'Hãy bắt đầu với ba mốc. Cuối năm hai nghìn không trăm linh sáu, VN-Index quanh bảy trăm năm mươi mốt điểm, sau một năm tăng rất mạnh khi thị trường còn rất non trẻ. '
         'Ngày mười hai tháng ba năm hai nghìn không trăm linh bảy, chỉ số đạt đỉnh khoảng một nghìn một trăm bảy mươi điểm. Và đến tháng hai năm hai nghìn không trăm linh chín, '
         'đáy khoảng hai trăm ba mươi lăm điểm. Từ đỉnh xuống đáy, giảm khoảng tám mươi phần trăm. Để dễ hình dung: một người đặt một tỷ đồng ở vùng đỉnh sẽ chỉ còn khoảng hai '
         'trăm triệu ở vùng đáy nếu giữ nguyên danh mục theo chỉ số. Tất nhiên từng cổ phiếu khác nhau, có mã giảm nhiều hơn, có mã giảm ít hơn. Nhưng điều đáng nói là tốc độ: '
         'khoảng hai năm. Trong lịch sử các thị trường, đỉnh bong bóng thường được nhận ra rõ ràng chỉ khi nhìn lại, còn lúc đang diễn ra, ai cũng có lý do nghe rất hợp lý để tin '
         'rằng lần này sẽ khác.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Vì sao thị trường lên',
  'moc': True,
  'label': 'Các lực đẩy giai đoạn 2006–2007',
  'cap': ('LỰC ĐẨY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Thị trường còn mới, nhiều doanh nghiệp lên sàn', (56, 189, 248)),
            ('Hàng triệu tài khoản mở trong thời gian ngắn', (56, 189, 248)),
            ('Tiền nước ngoài đổ vào kỳ vọng tăng trưởng', (56, 189, 248)),
            ('Câu chuyện: ai vào cũng lãi', (255, 196, 0))],
  'anh': 'crowd trading hall',
  'say': 'Vì sao thị trường lên nhanh như vậy? Có nhiều lực cùng tác động. Một, thị trường còn rất mới: nhiều doanh nghiệp lần đầu niêm yết, nhà đầu tư chưa có nhiều so sánh. '
         'Hai, số tài khoản chứng khoán tăng cực nhanh, kéo theo một lớp nhà đầu tư lần đầu tham gia, trong khi kinh nghiệm chu kỳ gần như chưa có. Ba, dòng vốn nước ngoài và kỳ '
         'vọng tăng trưởng kinh tế cao đã tạo ra một câu chuyện hấp dẫn. Bốn, và quan trọng nhất về tâm lý, là câu chuyện ai vào cũng lãi. Khi lợi nhuận đến dễ dàng, người ta dần '
         'quên rủi ro. Nhiều người vay tiền, cầm cố tài sản để mua thêm, vì giá luôn tăng trong ký ức gần nhất của họ. Một nguyên tắc cũ của thị trường: khi người bán rau cũng '
         'hỏi mua mã nào, thì rủi ro thường đã lớn hơn cơ hội.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Ba năm, ba bức tranh',
  'moc': True,
  'label': 'VN-Index cuối năm (điểm, số làm tròn)',
  'cap': ('3 NĂM',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Cuối 2006', 751.0, (56, 189, 248), '751'), ('Cuối 2007', 927.0, (34, 197, 94), '927'), ('Cuối 2008', 316.0, (239, 68, 68), '316')],
  'anh': 'line chart decline',
  'say': 'Nhìn theo cuối năm, bức tranh như sau. Cuối năm hai nghìn không trăm linh sáu khoảng bảy trăm năm mươi mốt điểm. Cuối năm hai nghìn không trăm linh bảy khoảng chín trăm '
         'hai mươi bảy điểm, tăng hơn hai mươi ba phần trăm so với cuối năm trước, thậm chí còn có đợt đỉnh cao hơn nhiều trong năm. Cuối năm hai nghìn không trăm linh tám khoảng '
         'ba trăm mười sáu điểm, giảm khoảng sáu mươi sáu phần trăm chỉ trong một năm. Nếu chỉ nhìn số cuối năm, bạn sẽ không thấy hết những cú rơi nửa chừng. Điều quan trọng là '
         'năm hai nghìn không trăm linh bảy vẫn kết thúc ở mức dương, nên nhiều người tưởng đó chỉ là một đợt điều chỉnh bình thường. Họ chờ hồi phục, mua thêm khi giá giảm, và '
         'rồi năm hai nghìn không trăm linh tám giáng cú thứ hai. Bài học về thời gian: những cú giảm lớn thường diễn ra theo nhiều đợt, mỗi đợt tạo ra một nhóm người tin rằng '
         'đây là đáy. Nhận ra đáy sớm hiếm khi dễ như người ta kể lại.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Vì sao thị trường sụp',
  'moc': True,
  'label': 'Các lực kéo xuống giai đoạn 2008',
  'cap': ('LỰC KÉO',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lạm phát cao, chính sách tiền tệ thắt chặt', (239, 68, 68)),
            ('Lãi suất huy động và cho vay tăng mạnh', (239, 68, 68)),
            ('Khủng hoảng tài chính toàn cầu cuối năm 2008', (239, 68, 68)),
            ('Nhà đầu tư vay mượn buộc phải bán', (239, 68, 68))],
  'anh': 'financial crisis newspaper',
  'say': 'Vậy điều gì làm thị trường sụp? Năm hai nghìn không trăm linh tám, lạm phát trong nước tăng rất cao, buộc cơ quan quản lý thắt chặt tiền tệ và đẩy lãi suất lên nhiều. '
         'Khi lãi suất gửi ngân hàng tăng mạnh, tiền rời khỏi cổ phiếu để về gửi tiết kiệm, vì lãi suất an toàn bỗng hấp dẫn hơn rủi ro. Cuối năm hai nghìn không trăm linh tám, '
         'khủng hoảng tài chính toàn cầu càng khiến dòng vốn ngoại rút ra và tâm lý lo sợ lan rộng. Còn ở bên trong thị trường, những người đã vay mượn để đầu tư buộc phải bán '
         'khi giá giảm, và việc bán ép đẩy giá giảm thêm, kéo thêm người bị ép bán. Đây là vòng xoáy mà ở các video khác mình đã phân tích bằng toán học. Điều cần nhớ: không có '
         'một nguyên nhân duy nhất. Thường là nhiều yếu tố vĩ mô xấu cùng lúc rơi vào một thị trường đang định giá quá lạc quan.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Toán học của việc gỡ vốn',
  'moc': True,
  'label': 'Mức giảm và mức tăng cần để hòa vốn',
  'cap': ('GỠ VỐN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Mất 20%', 'cần +25%', 'để về điểm cũ'), ('Mất 50%', 'cần +100%', 'phải gấp đôi'), ('Mất 80%', 'cần +400%', 'phải gấp năm lần')],
  'anh': 'math calculation board',
  'say': 'Bây giờ đến phép tính quan trọng nhất của video này. Khi mất hai mươi phần trăm, bạn cần tăng hai mươi lăm phần trăm để hòa vốn. Khi mất năm mươi phần trăm, bạn cần '
         'tăng một trăm phần trăm, tức phải gấp đôi. Và khi mất tám mươi phần trăm, bạn cần tăng bốn trăm phần trăm, tức phải gấp năm lần số còn lại. Phép tính không đối xứng: '
         'mất càng sâu, đường quay về càng dài theo cấp số nhân. Từ đáy khoảng hai trăm ba mươi lăm điểm, VN-Index phải tăng gần bốn trăm phần trăm mới trở lại đỉnh một nghìn một '
         'trăm bảy mươi, và thực tế phải mất nhiều năm. Đây là lý do tôi luôn nói cắt lỗ và quản trị vốn không phải là chuyện nhát gan, mà là toán học. Giữ cho khoản lỗ nhỏ luôn '
         'rẻ hơn cố gỡ một khoản lỗ lớn. Và đây cũng là lý do mức đòn bẩy cao đặc biệt nguy hiểm: nó biến một cú giảm bình thường thành một khoản lỗ sâu, rất khó quay lại.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Dấu hiệu bong bóng áp dụng mọi thời kỳ',
  'moc': True,
  'label': 'Danh sách tự kiểm tra',
  'cap': ('DẤU HIỆU',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Giá tăng nhanh hơn lợi nhuận rất nhiều', (239, 68, 68)),
            ('Người mới đổ xô, ai cũng bàn chuyện cổ phiếu', (239, 68, 68)),
            ('Nhiều người vay mượn để mua', (239, 68, 68)),
            ('Lập luận “lần này khác” được chấp nhận rộng rãi', (239, 68, 68))],
  'anh': 'bubble warning crowd',
  'say': 'Những dấu hiệu bong bóng này không chỉ đúng với giai đoạn hai nghìn không trăm linh bảy. Một, giá tăng nhanh hơn lợi nhuận rất nhiều: P/E của cả thị trường bị đẩy cao '
         'dựa trên kỳ vọng. Hai, người mới đổ xô: tài khoản mở mới tăng đột biến, chuyện chứng khoán xuất hiện ở mọi bàn cà phê. Ba, nhiều người vay mượn để mua, khiến thị trường '
         'dễ gãy khi giá đảo chiều. Bốn, câu chuyện lần này khác: người ta bắt đầu giải thích rằng các quy luật cũ không còn áp dụng. Cần nói rõ, các dấu hiệu này không dự báo '
         'được thời điểm. Một thị trường có thể nóng thêm nhiều tháng, thậm chí nhiều năm. Nhưng chúng đủ để bạn tự hỏi: mình đang đầu tư vì phân tích, hay vì sợ bị bỏ lại? Biết '
         'mình đang ở trạng thái nào đã là một lợi thế lớn so với đám đông.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Điều đã thay đổi, điều chưa đổi',
  'moc': True,
  'label': 'Thị trường ngày nay so với thời đó',
  'cap': ('ĐỔI & KHÔNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Đã đổi: thị trường lớn hơn, nhiều công cụ và thông tin hơn', (56, 189, 248)),
            ('Đã đổi: quy định minh bạch hơn', (56, 189, 248)),
            ('Chưa đổi: tâm lý tham lam và sợ hãi', (255, 196, 0)),
            ('Chưa đổi: đòn bẩy vẫn là nguyên nhân bán tháo', (255, 196, 0))],
  'anh': 'modern trading screens',
  'say': 'Thị trường ngày nay khác khá nhiều so với năm hai nghìn không trăm linh bảy. Quy mô lớn hơn nhiều, có nhiều công cụ và thông tin hơn, quy định công bố thông tin chặt '
         'chẽ hơn, và nhà đầu tư tổ chức đóng vai trò lớn hơn. Nhưng bản chất con người thì không đổi. Nỗi sợ bỏ lỡ khi giá tăng và nỗi sợ mất mát khi giá giảm vẫn là hai động cơ '
         'lớn nhất. Đòn bẩy vẫn là nguyên nhân quen thuộc của những phiên bán tháo. Kênh này đã có video phân tích ba cú giảm lớn hai nghìn không trăm mười tám, hai nghìn không '
         'trăm hai mươi và hai nghìn không trăm hai mươi hai, và bạn sẽ thấy các kịch bản có những điểm chung rất đáng ngạc nhiên. Mỗi lần công nghệ và tên gọi khác đi, nhưng mô '
         'thức tâm lý lặp lại. Vì vậy học lịch sử không phải để dự báo ngày mai, mà để nhận ra mô thức khi nó xuất hiện lần nữa, và không phải trả học phí bằng chính tài khoản '
         'của mình.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm bài học mang theo mười năm',
  'moc': True,
  'label': 'Rút ra từ giai đoạn 2006–2009',
  'cap': ('5 BÀI HỌC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Đỉnh chỉ rõ ràng khi nhìn lại', (255, 196, 0)),
            ('2. Mất càng sâu, gỡ càng khó', (255, 196, 0)),
            ('3. Đòn bẩy biến điều chỉnh thành thảm họa', (255, 196, 0)),
            ('4. Giữ tiền mặt hợp lý để có lựa chọn', (255, 196, 0)),
            ('5. Đầu tư theo kế hoạch, không theo đám đông', (255, 196, 0))],
  'anh': 'compass lesson wisdom',
  'say': 'Năm bài học để mang theo. Một, đỉnh chỉ rõ ràng khi nhìn lại, nên đừng cố bán đúng đỉnh mà hãy có kế hoạch từ trước. Hai, mất càng sâu gỡ càng khó, vì thế giữ khoản lỗ '
         'nhỏ. Ba, đòn bẩy biến một đợt điều chỉnh thành thảm họa, nên dùng đòn bẩy bao nhiêu thì tính trước nó chịu được cú giảm bao nhiêu. Bốn, giữ phần tiền mặt hợp lý, vì khi '
         'thị trường rẻ thật, người có tiền mới có lựa chọn. Năm, đầu tư theo kế hoạch thay vì theo đám đông: viết ra lý do mua, mức rủi ro chấp nhận được và điều kiện thoát '
         'trước khi vào lệnh. Mười năm nữa sẽ có một chu kỳ khác với những cái tên khác, nhưng năm bài học này vẫn đúng. Nếu thấy hữu ích, hãy lưu video và xem lại vào lúc thị '
         'trường đang rất vui hoặc rất buồn, vì đó là lúc bạn cần nó nhất.'},
 {'k': 'end',
  'label': '',
  'cap': ('BÀI HỌC LỊCH SỬ', '2006–2009'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các mốc điểm số trong video là số làm tròn theo thông tin công khai, có thể chênh nhẹ so với số chính thức. Biểu đồ chỉ là hình nền. Nội dung chia sẻ kiến thức, không '
         'phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Bài học lịch sử.'}]

S['CH1211A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'HPG – Đọc BCTC 5 phút',
  'cap': ('LỢI NHUẬN +106%', 'LÃI VAY +118%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'HPGW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[15, 26.51, 'Đỉnh tuần 23/2/26: 26,51', 0.6], [46, 19.6, 'Đáy tuần 28/9/26: 19,60', 1.6], [51, 21.5, 'Đóng tuần 2/11/26: 21,50', 2.6]]},
  'anh': 'steel mill furnace',
  'say': 'Một doanh nghiệp thép báo lợi nhuận quý ba tăng một trăm linh sáu phần trăm so với cùng kỳ, gấp đôi chỉ trong một năm. Nhưng cũng trong báo cáo đó, chi phí lãi vay tăng '
         'một trăm mười tám phẩy bốn phần trăm, còn nhanh hơn cả lợi nhuận. Vậy doanh nghiệp đang làm ăn tốt lên, hay đang gánh nợ nặng hơn? Trong video này mình đọc báo cáo tài '
         'chính quý ba năm hai nghìn không trăm hai mươi sáu của Tập đoàn Hòa Phát, mã HPG, theo năm bước dành cho doanh nghiệp sản xuất: doanh thu, biên lợi nhuận gộp, chi phí '
         'tài chính, lợi nhuận ròng, và cuối cùng là định giá trong bối cảnh ngành thép có tính chu kỳ. Xem hết, bạn sẽ biết cách phân biệt lợi nhuận tăng nhờ bán nhiều hơn với '
         'lợi nhuận tăng nhờ biên lợi nhuận cải thiện, và vì sao lãi vay là dòng đáng theo dõi. Video thuộc seri Đọc BCTC năm phút. Số liệu là ví dụ minh họa tại ngày năm tháng '
         'mười một năm hai nghìn không trăm hai mươi sáu. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Bước 1: Doanh thu thuần',
  'moc': True,
  'label': 'Doanh thu thuần HPG theo quý (tỷ đồng)',
  'cap': ('DOANH THU', 'THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 36407.0, (56, 189, 248), '36.407'),
           ('Q4/25', 46177.0, (56, 189, 248), '46.177'),
           ('Q1/26', 52901.0, (56, 189, 248), '52.901'),
           ('Q2/26', 55159.0, (56, 189, 248), '55.159'),
           ('Q3/26', 62214.0, (34, 197, 94), '62.214')],
  'anh': 'steel coils factory',
  'say': 'Bước một là doanh thu thuần. Quý ba năm hai nghìn không trăm hai mươi sáu, Hòa Phát ghi nhận sáu mươi hai nghìn hai trăm mười bốn tỷ đồng, tăng bảy mươi phẩy chín phần '
         'trăm so với ba mươi sáu nghìn bốn trăm linh bảy tỷ cùng kỳ. Nhìn chuỗi năm quý, doanh thu tăng gần như liên tục: ba mươi sáu nghìn bốn trăm linh bảy, bốn mươi sáu nghìn '
         'một trăm bảy mươi bảy, năm mươi hai nghìn chín trăm linh một, năm mươi lăm nghìn một trăm năm mươi chín rồi sáu mươi hai nghìn hai trăm mười bốn. Mức tăng này đến từ '
         'đâu? Với doanh nghiệp sản xuất, doanh thu bằng sản lượng nhân với giá bán. Nếu cả hai cùng tăng, đó là tín hiệu rất tốt. Nếu chỉ giá tăng, bạn cần thận trọng vì giá '
         'hàng hóa có thể đảo chiều. Nếu chỉ sản lượng tăng nhờ nhà máy mới, đó là tăng trưởng có nền tảng hơn. Báo cáo thường có thuyết minh về sản lượng và giá bình quân, đó là '
         'nơi bạn tìm câu trả lời. Một nguyên tắc chung: khi doanh thu tăng nhanh bất thường, hãy luôn hỏi động lực nằm ở lượng hay ở giá, vì câu trả lời quyết định mức độ bền '
         'của đà tăng.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Bước 2: Biên lợi nhuận gộp',
  'moc': True,
  'label': 'Quý 3 năm 2026 so với cùng kỳ',
  'cap': ('BIÊN LỢI', 'NHUẬN GỘP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Quý 3/2025', '16,7%', 'biên lợi nhuận gộp'), ('Quý 3/2026', '19,2%', 'tăng 2,5 điểm phần trăm'), ('Ý nghĩa', 'mỗi 100 đồng bán', 'giữ thêm 2,5 đồng')],
  'anh': 'steel price chart',
  'say': 'Bước hai là biên lợi nhuận gộp, tức phần trăm doanh thu còn lại sau khi trừ giá vốn hàng bán. Quý ba năm hai nghìn không trăm hai mươi sáu, biên gộp của Hòa Phát là '
         'mười chín phẩy hai phần trăm, so với mười sáu phẩy bảy phần trăm cùng kỳ, cải thiện hai phẩy năm điểm phần trăm. Điều này nghĩa là mỗi một trăm đồng hàng bán ra, công '
         'ty giữ lại thêm khoảng hai đồng rưỡi so với năm trước. Trong ngành thép, biên gộp phụ thuộc vào chênh lệch giữa giá thép thành phẩm và giá nguyên liệu như quặng sắt và '
         'than. Khi chênh lệch này mở rộng, biên cải thiện. Khi thu hẹp, biên mỏng đi rất nhanh. Vì vậy với ngành chu kỳ, biên lợi nhuận quan trọng hơn bản thân doanh thu: doanh '
         'thu tăng nhưng biên giảm thì lợi nhuận chưa chắc tăng. Ở quý này, cả doanh thu và biên cùng tăng, và đó là lý do lợi nhuận bứt lên.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Bước 3: Chi phí lãi vay',
  'moc': True,
  'label': 'Điểm cần đọc kỹ trong báo cáo',
  'cap': ('LÃI VAY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Lợi nhuận sau thuế', '+106,0%', 'so với cùng kỳ'), ('Doanh thu', '+70,9%', 'so với cùng kỳ'), ('Chi phí lãi vay', '+118,4%', 'tăng nhanh nhất')],
  'anh': 'bank loan interest',
  'say': 'Bước ba là chi phí tài chính, mà chủ yếu là lãi vay. Theo dữ liệu tổng hợp, chi phí lãi vay quý ba của Hòa Phát tăng một trăm mười tám phẩy bốn phần trăm so với cùng '
         'kỳ, nhanh hơn cả doanh thu bảy mươi phẩy chín phần trăm và lợi nhuận một trăm linh sáu phẩy không phần trăm. Điều này thường xảy ra khi doanh nghiệp vay thêm để đầu tư '
         'các dự án lớn, hoặc khi chi phí vốn cao hơn. Lãi vay tăng không tự nó là xấu, vì đầu tư mở rộng cần vốn. Câu hỏi là dòng tiền từ hoạt động chính có đủ gánh lãi và gốc '
         'không, và khoản vay đang được dùng để làm gì. Nếu lãi vay tăng nhanh hơn lợi nhuận kéo dài nhiều quý, phần lợi nhuận sẽ bị bào mòn khi chu kỳ ngành đảo chiều. Hãy xem '
         'thêm tổng nợ vay, nợ vay trên vốn chủ và hệ số bao phủ lãi vay. Đây là ba con số trả lời câu hỏi doanh nghiệp có đang đi đường dài một cách an toàn không.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Bước 4: Lợi nhuận ròng',
  'moc': True,
  'label': 'LNST công ty mẹ HPG theo quý (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'RÒNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 3988.0, (56, 189, 248), '3.988'),
           ('Q4/25', 3864.0, (56, 189, 248), '3.864'),
           ('Q1/26', 8994.0, (56, 189, 248), '8.994'),
           ('Q2/26', 6371.0, (56, 189, 248), '6.371'),
           ('Q3/26', 8217.0, (34, 197, 94), '8.217')],
  'anh': 'profit chart growth',
  'say': 'Bước bốn là lợi nhuận ròng. Quý ba năm hai nghìn không trăm hai mươi sáu, lợi nhuận sau thuế của công ty mẹ là tám nghìn hai trăm mười bảy tỷ, tăng một trăm linh sáu '
         'phẩy không phần trăm so với ba nghìn chín trăm tám mươi tám tỷ cùng kỳ. Lũy kế chín tháng đạt hai mươi ba nghìn năm trăm tám mươi hai tỷ, tăng một trăm linh ba phẩy năm '
         'phần trăm. Nhìn chuỗi, có hai điểm đáng chú ý. Một, lợi nhuận bứt phá từ quý một năm hai nghìn không trăm hai mươi sáu lên tám nghìn chín trăm chín mươi bốn tỷ rồi dao '
         'động từ sáu nghìn ba trăm bảy mươi mốt đến tám nghìn hai trăm mười bảy tỷ, nghĩa là mặt bằng lợi nhuận đã cao hơn hẳn năm ngoái. Hai, biên lợi nhuận ròng, tính bằng lợi '
         'nhuận chia doanh thu, tăng từ khoảng mười một phẩy không phần trăm lên mười ba phẩy hai phần trăm. Đây là phép tính bạn nên tự làm vì nó gộp ảnh hưởng của giá vốn, chi '
         'phí bán hàng, lãi vay và thuế vào một con số. Khi biên ròng tăng dù lãi vay tăng mạnh, nghĩa là biên gộp đủ rộng để gánh chi phí tài chính. Nhưng ngành chu kỳ thì biên '
         'có thể co lại rất nhanh.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Bước 5: Định giá và chu kỳ',
  'moc': True,
  'label': 'Dữ liệu tổng hợp 5/11/2026',
  'cap': ('ĐỊNH GIÁ', 'NGÀNH CHU KỲ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('P/E · P/B', '6,68 · 1,23', 'lần'), ('ROE · ROA', '19,9% · 10,4%', '4 quý gần nhất'), ('Tỷ suất cổ tức', '2,09%', 'theo dữ liệu tổng hợp')],
  'anh': 'stock valuation chart',
  'say': 'Bước năm là định giá, và với ngành thép phải nhớ yếu tố chu kỳ. Theo dữ liệu tổng hợp ngày ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, P/E của Hòa '
         'Phát khoảng sáu phẩy sáu mươi tám lần, P/B một phẩy hai mươi ba lần, ROE mười chín phẩy chín phần trăm và ROA mười phẩy bốn phần trăm. Chênh lệch nhỏ giữa ROE và ROA, '
         'chỉ khoảng một phẩy chín lần, cho thấy đòn bẩy tài chính thấp hơn nhiều so với một ngân hàng. Điều nhiều người mới hay nhầm: P/E thấp ở ngành chu kỳ không phải lúc nào '
         'cũng là rẻ. Khi lợi nhuận đang ở vùng đỉnh chu kỳ, P/E tính trên lợi nhuận đỉnh trông rất thấp, rồi lợi nhuận giảm khiến P/E thực tế cao lên. Vì vậy với doanh nghiệp '
         'chu kỳ, người ta thường nhìn lợi nhuận trung bình qua nhiều năm, hoặc P/B kết hợp ROE. Các con số này chỉ mô tả cách thị trường đang định giá, không phải khuyến nghị '
         'mua hay bán.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Ba câu hỏi nên đặt thêm',
  'moc': True,
  'label': 'Sau khi đọc xong năm bước',
  'cap': ('3 CÂU HỎI', 'THÊM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Doanh thu tăng nhờ sản lượng hay giá bán?', (56, 189, 248)),
            ('Biên gộp có duy trì khi giá nguyên liệu biến động?', (56, 189, 248)),
            ('Dòng tiền kinh doanh có đủ gánh lãi vay và đầu tư?', (255, 196, 0))],
  'anh': 'analyst questions',
  'say': 'Sau năm bước, có ba câu hỏi nâng cao. Câu một: doanh thu tăng nhờ sản lượng hay giá bán? Đọc thuyết minh để biết sản lượng bán và giá bình quân. Nếu sản lượng tăng nhờ '
         'nhà máy mới, đà tăng có nền tảng. Nếu chỉ giá tăng, hãy cảnh giác với đảo chiều. Câu hai: biên gộp có duy trì khi giá nguyên liệu biến động? Hãy xem biên qua ít nhất '
         'tám quý, và đặt nó cạnh giá thép, giá quặng trong cùng thời kỳ. Câu ba: dòng tiền kinh doanh có đủ để gánh lãi vay và chi đầu tư không? Nếu không, doanh nghiệp phải vay '
         'thêm, và lãi vay tăng như dữ liệu quý này sẽ càng nặng. Ba câu hỏi này đưa bạn từ việc đọc con số sang việc hiểu câu chuyện kinh doanh phía sau, và câu chuyện mới là '
         'thứ quyết định lợi nhuận quý sau.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những cái bẫy với doanh nghiệp chu kỳ',
  'moc': True,
  'label': 'Bốn điều dễ nhầm',
  'cap': ('4 CÁI BẪY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lấy lợi nhuận đỉnh chu kỳ làm mức bình thường', (239, 68, 68)),
            ('Thấy P/E thấp là kết luận rẻ', (239, 68, 68)),
            ('Bỏ qua nợ vay khi lợi nhuận đang đẹp', (239, 68, 68)),
            ('Chỉ so cùng kỳ năm ngoái đang là nền thấp', (239, 68, 68))],
  'anh': 'warning sign road',
  'say': 'Bốn cái bẫy khi đọc doanh nghiệp chu kỳ. Bẫy một: lấy lợi nhuận đỉnh làm mức bình thường. Khi lợi nhuận gấp đôi, rất dễ nghĩ đó là mức mới vĩnh viễn, trong khi ngành '
         'chu kỳ thường quay về mức trung bình sau vài năm. Bẫy hai: P/E thấp là rẻ. Như đã nói, P/E thấp có thể chỉ do lợi nhuận đang ở đỉnh. Bẫy ba: bỏ qua nợ vay khi lợi nhuận '
         'đang đẹp. Lúc dễ trả nợ thì không ai lo, đến khi chu kỳ xấu mới thấy gánh nặng. Bẫy bốn: so cùng kỳ năm ngoái khi đó là nền thấp, khiến mức tăng trông ấn tượng hơn. '
         'Trong ví dụ này, quý ba năm hai nghìn không trăm hai mươi lăm lợi nhuận chỉ khoảng ba nghìn chín trăm tám mươi tám tỷ, nên mức tăng một trăm linh sáu phần trăm một phần '
         'do nền thấp. Cách tránh cả bốn bẫy là nhìn chuỗi dài hơn, chia lợi nhuận cho nhiều năm, và luôn đặt lãi vay cạnh dòng tiền.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Khung 5 bước đọc doanh nghiệp sản xuất',
  'cap': ('5 BƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Doanh thu: lượng hay giá', (56, 189, 248)),
            ('2. Biên gộp: chênh lệch giá bán và vốn', (56, 189, 248)),
            ('3. Chi phí lãi vay: gánh nặng tài chính', (239, 68, 68)),
            ('4. Lợi nhuận ròng và biên ròng', (34, 197, 94)),
            ('5. P/E, P/B, ROE trong chu kỳ', (255, 196, 0))],
  'anh': 'checklist notebook',
  'say': 'Tổng kết lại bằng năm bước. Một, doanh thu: tăng nhờ lượng hay nhờ giá. Hai, biên gộp: chênh lệch giữa giá bán và giá vốn. Ba, chi phí lãi vay: gánh nặng tài chính và '
         'dòng tiền để gánh. Bốn, lợi nhuận ròng cùng biên ròng. Năm, P/E, P/B và ROE đặt trong bối cảnh chu kỳ. Trong ví dụ Hòa Phát, bức tranh quý ba năm hai nghìn không trăm '
         'hai mươi sáu là doanh thu và biên cùng cải thiện nên lợi nhuận bứt lên, đồng thời chi phí lãi vay tăng nhanh hơn doanh thu. Hai mặt đó cùng có thật. Mười năm nữa các '
         'con số sẽ khác, nhưng khung năm bước vẫn đọc được cho nhiều doanh nghiệp sản xuất khác. Hãy thử áp dụng cho một cổ phiếu cùng ngành bạn quan tâm: so sánh tám quý, đặt '
         'cạnh nhau năm dòng này. Nếu thấy hữu ích, lưu video để xem lại mỗi mùa báo cáo.'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐỌC BCTC 5 PHÚT', 'HPG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu lấy từ báo cáo tài chính hợp nhất quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày ngày năm tháng mười một năm hai nghìn không trăm hai '
         'mươi sáu, mang tính minh họa cách đọc. Biểu đồ chỉ là hình nền. Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem tiếp '
         'seri Đọc BCTC năm phút.'}]

S['CH1211B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'TCB – hình nền minh họa',
  'cap': ('ROE 20% NHƯNG', 'KHÔNG NHƯ NHAU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'TCBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 24.94, 'Đỉnh tuần 12/1/26: 24,94', 0.6], [21, 18.51, 'Đáy tuần 6/4/26: 18,51', 1.6], [51, 21.95, 'Đóng tuần 2/11/26: 21,95', 2.6]]},
  'anh': 'three business types',
  'say': 'Ba doanh nghiệp cùng có ROE khoảng hai mươi phần trăm. Nếu chỉ nhìn một chỉ số, họ giống hệt nhau. Nhưng một doanh nghiệp đạt ROE đó nhờ biên lợi nhuận cao, một nhờ bán '
         'hàng quay vòng thật nhanh, và một nhờ vay rất nhiều. Ba con đường, ba mức rủi ro rất khác. Công cụ giúp bạn tách ROE thành các mảnh là phân tích DuPont, một phép tính '
         'đơn giản có từ hơn một trăm năm nay và vẫn dùng đến ngày nay. Trong video này mình giải thích ROE là gì, cách tách thành ba phần, dùng số liệu thật của một ngân hàng, '
         'một doanh nghiệp thép và một doanh nghiệp sữa để thấy ROE đến từ đâu. Xem hết, bạn sẽ biết cách nhìn một ROE cao và hỏi đúng câu: cao nhờ cái gì, và có bền không? Video '
         'thuộc seri Nền tảng đầu tư. Số liệu ví dụ lấy từ dữ liệu tổng hợp ngày ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu. Biểu đồ phía sau chỉ là hình nền.'},
 {'k': 'checklist',
  'ch': 'Chương 1 – ROE là gì',
  'moc': True,
  'label': 'Lợi nhuận trên vốn chủ sở hữu',
  'cap': ('ROE LÀ GÌ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('ROE = Lợi nhuận sau thuế ÷ Vốn chủ sở hữu', (255, 196, 0)),
            ('Cho biết mỗi đồng vốn cổ đông tạo bao nhiêu lãi', (56, 189, 248)),
            ('Nên dùng số 4 quý gần nhất, không lấy một quý', (56, 189, 248)),
            ('ROE cao chưa chắc doanh nghiệp tốt', (239, 68, 68))],
  'anh': 'equity shareholder capital',
  'say': 'ROE là lợi nhuận sau thuế chia cho vốn chủ sở hữu, thường tính theo bốn quý gần nhất để tránh biến động một quý. Nếu vốn chủ của bạn là một trăm đồng và công ty lãi hai '
         'mươi đồng một năm thì ROE là hai mươi phần trăm. Con số này cho biết mỗi đồng vốn của cổ đông được sử dụng sinh lời ra sao, nên Warren Buffett và nhiều nhà đầu tư giá '
         'trị coi ROE là một trong những thước đo chất lượng quan trọng. Nhưng chính vì thế nó dễ bị hiểu sai. ROE cao chưa chắc doanh nghiệp tốt, vì ROE có thể cao do vốn chủ '
         'quá nhỏ, do vay quá nhiều, hoặc do lợi nhuận bất thường. Muốn đọc đúng ROE, bạn cần biết nó được tạo ra từ những mảnh nào. Đó chính là lúc phân tích DuPont xuất hiện, '
         'và nó dễ hơn bạn nghĩ.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Tách ROE thành ba phần',
  'moc': True,
  'label': 'Công thức DuPont',
  'cap': ('3 PHẦN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Biên lợi nhuận ròng', 'Lãi ÷ Doanh thu', 'mỗi đồng bán ra giữ lại bao nhiêu'),
            ('Vòng quay tài sản', 'Doanh thu ÷ Tài sản', 'tài sản quay nhanh hay chậm'),
            ('Đòn bẩy tài chính', 'Tài sản ÷ Vốn chủ', 'dùng bao nhiêu nợ')],
  'anh': 'three gears machine',
  'say': 'DuPont tách ROE thành tích của ba phần. Phần một là biên lợi nhuận ròng, bằng lợi nhuận chia doanh thu: mỗi đồng bán ra giữ lại được bao nhiêu. Phần hai là vòng quay '
         'tài sản, bằng doanh thu chia tổng tài sản: tài sản được dùng để tạo doanh thu nhanh hay chậm. Phần ba là đòn bẩy tài chính, bằng tổng tài sản chia vốn chủ: doanh nghiệp '
         'dùng bao nhiêu vốn vay so với vốn của mình. Nhân ba phần này lại, các mẫu số và tử số triệt tiêu nhau và bạn có đúng ROE. Điểm hay là mỗi phần phản ánh một chiến lược '
         'kinh doanh khác nhau. Biên cao thường là doanh nghiệp bán sản phẩm khác biệt. Vòng quay cao là bán lẻ, bán nhanh biên mỏng. Đòn bẩy cao là ngân hàng và những ngành dùng '
         'nhiều nợ. Cùng một ROE nhưng thành phần khác nhau thì rủi ro khác nhau.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Ba doanh nghiệp, ba con đường',
  'moc': True,
  'label': 'Dữ liệu tổng hợp 5/11/2026, 4 quý gần nhất',
  'cap': ('3 CON ĐƯỜNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Doanh nghiệp sữa (VNM)', 'ROE 31,1%', 'ROA 20,4% → đòn bẩy ~1,5 lần'),
            ('Doanh nghiệp thép (HPG)', 'ROE 19,9%', 'ROA 10,4% → đòn bẩy ~1,9 lần'),
            ('Ngân hàng (MBB)', 'ROE 21,8%', 'ROA 2,0% → đòn bẩy ~10,9 lần')],
  'anh': 'dairy steel bank',
  'say': 'Hãy xem ba ví dụ thật. Doanh nghiệp sữa Vinamilk có ROE khoảng ba mươi mốt phẩy một phần trăm và ROA hai mươi phẩy bốn phần trăm. Lấy ROE chia ROA ra khoảng một phẩy '
         'năm lần, nghĩa là đòn bẩy rất thấp, ROE cao đến từ khả năng sinh lời trên tài sản. Hòa Phát có ROE mười chín phẩy chín phần trăm và ROA mười phẩy bốn phần trăm, đòn bẩy '
         'khoảng một phẩy chín lần. Còn ngân hàng Quân đội có ROE hai mươi mốt phẩy tám phần trăm nhưng ROA chỉ hai phẩy không phần trăm, đòn bẩy khoảng mười phẩy chín lần. Ba '
         'doanh nghiệp có ROE từ hai mươi đến ba mươi mốt phần trăm, nhưng kết cấu hoàn toàn khác. Với ngân hàng, đòn bẩy cao là đặc điểm ngành, bình thường, nhưng nghĩa là một '
         'khoản tổn thất nhỏ trên tài sản cũng ảnh hưởng nhiều đến vốn. Với doanh nghiệp sản xuất, đòn bẩy một phẩy năm đến một phẩy chín lần cho thấy phần lớn tài sản được tài '
         'trợ bằng vốn của cổ đông. Ba con số, ba câu chuyện rủi ro.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Ví dụ tính tay',
  'moc': True,
  'label': 'Số giả định để thấy phép nhân',
  'cap': ('TÍNH TAY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Biên ròng', '10%', 'lãi 10 trên doanh thu 100'), ('Vòng quay', '1,0 lần', 'doanh thu 100 trên tài sản 100'), ('Đòn bẩy', '2,0 lần', 'tài sản 100 trên vốn 50')],
  'anh': 'calculator pen paper',
  'say': 'Hãy tự tính một ví dụ giả định. Một công ty có doanh thu một trăm, lợi nhuận ròng mười, tổng tài sản một trăm, vốn chủ sở hữu năm mươi. Biên ròng là mười chia một trăm, '
         'bằng mười phần trăm. Vòng quay tài sản là một trăm chia một trăm, bằng một phẩy không lần. Đòn bẩy là một trăm chia năm mươi, bằng hai phẩy không lần. Nhân ba phần: '
         'mười phần trăm nhân một phẩy không nhân hai phẩy không bằng hai mươi phần trăm. Kiểm tra trực tiếp: lợi nhuận mười chia vốn chủ năm mươi cũng bằng hai mươi phần trăm. '
         'Bây giờ giả sử công ty đạt ROE hai mươi phần trăm theo cách khác: biên ròng chỉ năm phần trăm nhưng vòng quay hai phẩy không lần và đòn bẩy hai phẩy không lần. Kết quả '
         'vẫn hai mươi phần trăm, nhưng đó là một doanh nghiệp bán nhanh, lãi mỏng. Hoặc biên mười phần trăm, vòng quay không phẩy năm lần, đòn bẩy bốn phẩy không lần cho cùng '
         'kết quả, nhưng rủi ro khác hẳn vì phải vay gấp đôi. Phép tính nhỏ này cho bạn thấy vì sao không nên chỉ nhìn một con số tổng.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – ROE tăng: tốt hay xấu',
  'moc': True,
  'label': 'Ba nguồn làm ROE tăng',
  'cap': ('ROE TĂNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Biên lợi nhuận cải thiện: thường là tín hiệu tốt', (34, 197, 94)),
            ('Vòng quay tài sản nhanh hơn: thường tốt', (34, 197, 94)),
            ('Vay nhiều hơn để đẩy đòn bẩy: cần thận trọng', (239, 68, 68)),
            ('Vốn chủ giảm vì lỗ hoặc mua lại: xem lại nguyên nhân', (239, 68, 68))],
  'anh': 'growth arrow chart',
  'say': 'Khi thấy ROE tăng, hãy hỏi tăng do phần nào trong ba phần. Nếu biên lợi nhuận cải thiện, thường là do bán được giá tốt hơn hoặc kiểm soát chi phí tốt hơn, đó là tín '
         'hiệu tích cực nhất. Nếu vòng quay tài sản nhanh hơn, doanh nghiệp đang tận dụng tài sản hiệu quả hơn, cũng thường là tốt. Nhưng nếu ROE tăng chủ yếu do đòn bẩy, tức vay '
         'nhiều hơn so với vốn, thì cần thận trọng: lợi nhuận được khuếch đại khi thuận lợi, nhưng khoản lỗ cũng khuếch đại như thế khi bất lợi. Một trường hợp khác là vốn chủ '
         'giảm vì doanh nghiệp lỗ hoặc mua lại cổ phiếu, khiến mẫu số nhỏ lại và ROE trông đẹp hơn mà thực chất không có gì cải thiện. Vì vậy, một ROE tăng luôn cần một lần kiểm '
         'tra thành phần.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Bốn cái bẫy khi dùng ROE',
  'moc': True,
  'label': 'Những điều dễ nhầm',
  'cap': ('4 CÁI BẪY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('So ROE giữa các ngành khác bản chất', (239, 68, 68)),
            ('Lấy ROE của một quý hoặc một năm bất thường', (239, 68, 68)),
            ('Bỏ qua lợi nhuận bất thường trong tử số', (239, 68, 68)),
            ('Không đọc cùng nợ vay và dòng tiền', (239, 68, 68))],
  'anh': 'warning cautious',
  'say': 'Bốn cái bẫy thường gặp khi dùng ROE. Bẫy một: so ROE giữa các ngành khác bản chất. Ngân hàng, bán lẻ, thép, công nghệ có kết cấu vốn khác hẳn, nên so ROE chéo ngành dễ '
         'dẫn đến kết luận sai. Bẫy hai: lấy ROE của một quý hoặc một năm bất thường, trong khi doanh nghiệp chu kỳ có ROE lên xuống mạnh. Bẫy ba: bỏ qua lợi nhuận bất thường '
         'trong tử số, ví dụ lãi thanh lý tài sản hay hoàn nhập dự phòng, những khoản không lặp lại. Bẫy bốn: không đọc cùng nợ vay và dòng tiền. Một doanh nghiệp ROE cao mà dòng '
         'tiền kinh doanh âm hoặc nợ vay tăng vọt cần được xem kỹ hơn nhiều. Cách tránh: nhìn ROE ít nhất năm năm, tách DuPont, và đối chiếu với dòng tiền. Chỉ khi các phần nhất '
         'quán với nhau, ROE mới thật sự là tấm gương phản ánh chất lượng doanh nghiệp.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – ROE và định giá: cặp đôi P/B',
  'moc': True,
  'label': 'Vì sao P/B cần đi cùng ROE',
  'cap': ('ROE VÀ P/B',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('P/B cao thường đi kèm kỳ vọng ROE cao và bền', (56, 189, 248)),
            ('P/B thấp đi cùng ROE thấp: thường hợp lý', (56, 189, 248)),
            ('ROE giảm dần: P/B có thể co lại', (239, 68, 68)),
            ('Luôn kiểm tra ROE có duy trì được không', (255, 196, 0))],
  'anh': 'valuation balance scale',
  'say': 'ROE và P/B là một cặp đi cùng nhau. Về lý thuyết, doanh nghiệp tạo ra ROE cao và bền xứng đáng được thị trường trả P/B cao hơn, vì mỗi đồng vốn sổ sách sinh ra nhiều '
         'lợi nhuận. Ngược lại, doanh nghiệp ROE thấp thường có P/B thấp, và điều đó thường là hợp lý chứ không phải rẻ. Nguy hiểm là nhìn P/B thấp rồi kết luận có cơ hội, trong '
         'khi ROE đang trượt dốc. Ví dụ, nếu ROE giảm từ hai mươi xuống mười phần trăm, P/B tương ứng hợp lý cũng co lại. Vì vậy, câu hỏi hay hơn là: ROE hiện tại có duy trì được '
         'không, và nó đến từ phần nào trong ba phần DuPont. Nếu từ biên và vòng quay bền vững, đó là chất lượng. Nếu từ đòn bẩy hoặc từ một khoản bất thường, mức định giá cao có '
         'thể kém bền. Đây chỉ là khung tư duy, không phải khuyến nghị.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Quy trình ba bước với mọi ROE',
  'cap': ('3 BƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Tách DuPont: biên × vòng quay × đòn bẩy', (255, 196, 0)),
            ('2. Xem 5 năm, không chỉ 1 quý', (255, 196, 0)),
            ('3. Đối chiếu dòng tiền, nợ vay và ngành', (255, 196, 0))],
  'anh': 'checklist progress',
  'say': 'Tổng kết lại với quy trình ba bước cho mọi ROE trong mười năm tới. Bước một, tách DuPont thành biên lợi nhuận, vòng quay tài sản và đòn bẩy, để biết ROE đến từ đâu. '
         'Bước hai, nhìn ít nhất năm năm thay vì một quý, vì ROE bền mới có giá trị. Bước ba, đối chiếu với dòng tiền kinh doanh, nợ vay và đặc điểm ngành, vì mỗi ngành có kết '
         'cấu vốn khác nhau. Bài tập cho bạn: chọn hai doanh nghiệp cùng ngành mà bạn quan tâm, lấy ROE và ROA của họ, chia để ra đòn bẩy, rồi viết một câu mô tả vì sao ROE của '
         'hai doanh nghiệp khác nhau. Nếu làm được trong mười phút, bạn đã đọc ROE tốt hơn rất nhiều người chỉ nhìn một con số. Hãy lưu video để xem lại khi bạn đọc báo cáo mùa '
         'tới, và nhớ rằng ROE là điểm khởi đầu của câu hỏi chứ không phải đáp án cuối cùng.'},
 {'k': 'end',
  'label': '',
  'cap': ('ROE VÀ DUPONT', 'TÁCH TRƯỚC KHI TIN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu ví dụ lấy từ dữ liệu tổng hợp ngày ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, bốn quý gần nhất, mang tính minh họa cách đọc. Các ví dụ tính '
         'tay là số giả định. Biểu đồ chỉ là hình nền. Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Nền tảng đầu tư.'}]

S['CH1211C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – hình nền minh họa',
  'cap': ('LỖ VÌ CHỌN SAI?', 'HAY VÌ TÂM LÝ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, 'Đóng tuần 2/11/26: 1.741', 2.6]]},
  'anh': 'investor stress screen',
  'say': 'Hai người cùng mua một cổ phiếu, cùng giá, cùng ngày. Một năm sau, một người lãi, một người lỗ, dù cổ phiếu đó không đổi. Vì sao? Vì người lãi đã làm theo kế hoạch, còn '
         'người lỗ mua thêm lúc giá hưng phấn rồi bán lúc hoảng sợ. Đây là điều mà các nghiên cứu về tài chính hành vi nói đi nói lại suốt nhiều thập kỷ: kết quả đầu tư kém '
         'thường không nằm ở việc chọn sai cổ phiếu, mà ở cách con người phản ứng với giá. Trong video này mình trình bày năm thiên kiến tâm lý phổ biến nhất khi đầu tư, mỗi cái '
         'kèm một ví dụ đời thường và một cách đối phó cụ thể. Xem hết, bạn sẽ nhận ra mình đang mắc ít nhất hai trong năm thiên kiến này, và biết cách thiết kế quy trình để '
         'chúng ít làm hại tài khoản hơn. Video thuộc seri Nền tảng đầu tư. Các ví dụ là số giả định. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'checklist',
  'ch': 'Chương 1 – Thiên kiến 1: sợ bỏ lỡ (FOMO)',
  'moc': True,
  'label': 'Khi mọi người cùng mua',
  'cap': ('FOMO',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Giá tăng nhanh, cảm giác “không vào là mất”', (239, 68, 68)),
            ('Mua đuổi ở vùng giá đã cao', (239, 68, 68)),
            ('Không có lý do mua ngoài “ai cũng mua”', (239, 68, 68)),
            ('Đối phó: viết lý do mua trước khi đặt lệnh', (34, 197, 94))],
  'anh': 'crowd rushing market',
  'say': 'Thiên kiến đầu tiên là sợ bỏ lỡ, thường gọi là FOMO. Khi một cổ phiếu tăng liên tiếp nhiều phiên, bạn thấy bạn bè khoe lãi, và cảm giác không vào là mất xuất hiện. Hậu '
         'quả điển hình là mua đuổi ở vùng giá đã cao, đúng lúc những người mua sớm bắt đầu chốt lời. Nguy hiểm ở chỗ FOMO không phải lý do đầu tư, chỉ là cảm xúc. Ví dụ giả '
         'định: cổ phiếu tăng ba mươi phần trăm trong hai tuần, bạn mua ở mức cao nhất vì sợ lỡ, rồi giá điều chỉnh mười lăm phần trăm. Bạn lỗ mà chưa hề có lý do kinh doanh nào '
         'cho quyết định đó. Cách đối phó đơn giản và hiệu quả: trước khi đặt lệnh, viết ra một câu lý do mua dựa trên doanh nghiệp, một mức giá bạn thấy hợp lý, và một mức bạn '
         'chấp nhận thoát. Nếu không viết được, đó là FOMO chứ không phải đầu tư. Thị trường luôn có cơ hội mới, còn vốn bị mất thì không quay lại dễ dàng.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Thiên kiến 2: ác cảm thua lỗ',
  'moc': True,
  'label': 'Nỗi đau mất mát lớn hơn niềm vui được lợi',
  'cap': ('ÁC CẢM LỖ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Lãi 10 triệu', 'vui 1 phần', 'cảm giác được'), ('Lỗ 10 triệu', 'đau ~2 phần', 'theo nghiên cứu hành vi'), ('Hệ quả', 'giữ mã lỗ', 'bán sớm mã lãi')],
  'anh': 'worried investor red numbers',
  'say': 'Thiên kiến thứ hai là ác cảm thua lỗ, do hai nhà tâm lý học Daniel Kahneman và Amos Tversky mô tả. Nghiên cứu của họ cho thấy nỗi đau khi mất một khoản tiền thường lớn '
         'hơn niềm vui khi được một khoản tương đương, khoảng hai lần. Hệ quả trên thị trường là hiệu ứng nổi tiếng: nhà đầu tư có xu hướng bán sớm cổ phiếu đang lãi để khóa niềm '
         'vui, và giữ lì cổ phiếu đang lỗ vì không muốn thừa nhận thua. Kết quả là danh mục dần chứa toàn mã lỗ lâu năm và rất ít mã thắng. Ví dụ giả định: bạn có hai mã, một mã '
         'lãi mười phần trăm và một mã lỗ hai mươi phần trăm. Bạn bán mã lãi để thấy mình thắng, giữ mã lỗ chờ hòa vốn. Cuối cùng mã lãi tiếp tục tăng mà bạn đã ra, mã lỗ tiếp '
         'tục giảm. Cách đối phó: đặt trước quy tắc cắt lỗ và quy tắc chốt lời bằng con số, rồi tuân theo, thay vì để cảm xúc quyết định mỗi lần.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Thiên kiến 3: neo giá',
  'moc': True,
  'label': 'Bị trói vào giá mua của chính mình',
  'cap': ('NEO GIÁ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('“Chờ về giá vốn rồi bán”', (239, 68, 68)),
            ('Giá mua của bạn không ảnh hưởng giá thị trường', (239, 68, 68)),
            ('Câu hỏi đúng: hôm nay có mua mã này không?', (34, 197, 94)),
            ('Đối phó: đánh giá lại như người chưa sở hữu', (34, 197, 94))],
  'anh': 'anchor ship sea',
  'say': 'Thiên kiến thứ ba là neo giá. Bạn mua một cổ phiếu ở giá bốn mươi nghìn, giá giảm còn ba mươi nghìn, và bạn tự nhủ sẽ chờ về bốn mươi nghìn rồi bán. Giá mua trở thành '
         'cái neo trong đầu, dù thị trường hoàn toàn không biết bạn mua giá nào. Cổ phiếu không quan tâm bạn lỗ hay lãi. Câu hỏi đúng không phải bao giờ về giá vốn, mà là: nếu '
         'hôm nay tôi chưa sở hữu cổ phiếu này, với thông tin hiện tại, tôi có mua nó ở giá này không? Nếu câu trả lời là không, việc giữ lại chỉ vì chờ hòa vốn là một quyết định '
         'bị neo. Ngược lại, nếu câu trả lời là có, thì giữ là quyết định hợp lý dù giá đang thấp hơn giá mua. Cách đối phó: định kỳ đánh giá lại từng mã như thể bạn là người '
         'mới, không nhìn giá vốn, chỉ nhìn doanh nghiệp, giá hiện tại và rủi ro.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Thiên kiến 4: tự tin thái quá',
  'moc': True,
  'label': 'Cảm giác mình hiểu hơn thực tế',
  'cap': ('TỰ TIN QUÁ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Vài lần thắng liên tiếp, tin mình giỏi', (239, 68, 68)),
            ('Tăng tỷ trọng và đòn bẩy sau chuỗi thắng', (239, 68, 68)),
            ('Giao dịch quá nhiều, phí và sai lầm tăng', (239, 68, 68)),
            ('Đối phó: ghi nhật ký, đo kết quả dài hạn', (34, 197, 94))],
  'anh': 'overconfident gambler',
  'say': 'Thiên kiến thứ tư là tự tin thái quá. Sau vài lần thắng liên tiếp, đặc biệt trong thị trường tăng, nhà đầu tư dễ tin rằng kết quả đến từ năng lực, trong khi phần lớn là '
         'do thị trường thuận lợi. Họ tăng tỷ trọng, dùng đòn bẩy cao hơn, giao dịch nhiều hơn. Khi thị trường đảo chiều, tài khoản chịu thiệt hại lớn nhất đúng lúc vị thế lớn '
         'nhất. Một ví dụ giả định: bạn thắng sáu lần liên tục mỗi lần tám phần trăm, rồi dồn gần hết vốn vào lệnh thứ bảy và lỗ hai mươi lăm phần trăm, xóa gần hết thành quả sáu '
         'lần. Giao dịch nhiều cũng có chi phí: phí, thuế và nhất là cơ hội mắc thêm sai lầm. Cách đối phó tốt nhất là ghi nhật ký đầu tư, ghi lý do mua và kết quả, rồi định kỳ '
         'đo kết quả theo năm thay vì theo lệnh. Con số dài hạn thường khiêm tốn hơn cảm giác, và đó là thông tin rất có giá trị.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Thiên kiến 5: hiệu ứng bầy đàn và xác nhận',
  'moc': True,
  'label': 'Chỉ nghe điều mình muốn nghe',
  'cap': ('BẦY ĐÀN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Theo đám đông vì “nhiều người cùng nghĩ”', (239, 68, 68)),
            ('Chỉ đọc tin ủng hộ quyết định đã có', (239, 68, 68)),
            ('Bỏ qua thông tin trái chiều', (239, 68, 68)),
            ('Đối phó: chủ động tìm lập luận phản biện', (34, 197, 94))],
  'anh': 'sheep herd',
  'say': 'Thiên kiến thứ năm gồm hai mặt gắn với nhau: hiệu ứng bầy đàn và thiên kiến xác nhận. Bầy đàn là đi theo đám đông vì nhiều người cùng nghĩ như vậy nên chắc đúng. Thiên '
         'kiến xác nhận là chỉ tìm và tin những thông tin ủng hộ điều mình đã quyết, trong khi bỏ qua những dữ kiện trái chiều. Khi cả hai cùng xuất hiện, bạn có một vòng lặp '
         'nguy hiểm: mua theo đám đông, rồi chỉ đọc bài viết khen cổ phiếu đó, rồi tin chắc mình đúng. Cách đối phó thực tế là chủ động tìm lập luận phản biện. Trước khi mua, hãy '
         'thử viết ba lý do mình có thể sai, rồi tìm thông tin về ba lý do đó. Nếu không phản biện được, bạn đã có thêm một lớp bảo vệ. Nếu thấy lập luận phản biện mạnh, có lẽ '
         'nên giảm tỷ trọng hoặc đợi thêm. Một ý kiến chỉ có giá trị khi nó chịu được câu hỏi ngược.'},
 {'k': 'cards',
  'ch': 'Chương 6 – Một ví dụ cộng dồn',
  'moc': True,
  'label': 'Số giả định, vốn 100 triệu',
  'cap': ('CỘNG DỒN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Kế hoạch', '+8%/năm', 'đều đặn, có quy tắc'), ('Hành vi', '−3%/năm', 'mua đuổi, bán hoảng'), ('Chênh lệch', '~11 điểm/năm', 'sau 10 năm rất lớn')],
  'anh': 'two paths diverging',
  'say': 'Hãy xem tác động cộng dồn bằng một ví dụ giả định. Hai nhà đầu tư cùng vốn một trăm triệu, cùng thị trường. Người thứ nhất làm theo kế hoạch, thu về tám phần trăm mỗi '
         'năm. Người thứ hai mắc các thiên kiến vừa kể, mua đuổi lúc nóng, bán hoảng lúc lạnh, và thu về trung bình âm ba phần trăm mỗi năm. Chênh lệch mỗi năm khoảng mười một '
         'điểm phần trăm. Sau mười năm, số tiền của người thứ nhất khoảng hai trăm mười sáu triệu, của người thứ hai khoảng bảy mươi bốn triệu. Chênh lệch hơn gấp hai lần chỉ vì '
         'cách hành xử. Con số tám phần trăm và âm ba phần trăm là giả định để minh họa, không phải dự báo, nhưng nguyên lý thì có thật: sai lầm hành vi nhỏ lặp lại mỗi năm cộng '
         'dồn thành khác biệt rất lớn do lãi kép, và lãi kép hoạt động theo cả hai chiều.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Thiết kế quy trình để thắng thiên kiến',
  'moc': True,
  'label': 'Tin vào hệ thống hơn cảm xúc',
  'cap': ('QUY TRÌNH',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Viết lý do mua và mức thoát trước khi vào lệnh', (255, 196, 0)),
            ('Đặt quy tắc tỷ trọng tối đa cho một mã', (255, 196, 0)),
            ('Góp đều định kỳ thay vì canh thời điểm', (255, 196, 0)),
            ('Giới hạn số lần xem giá mỗi ngày', (255, 196, 0))],
  'anh': 'checklist system process',
  'say': 'Ý chí rất hao mòn, nên tốt hơn là thiết kế quy trình khiến thiên kiến ít có cơ hội. Một, viết lý do mua và mức thoát trước khi vào lệnh, để quyết định được đưa ra lúc '
         'bình tĩnh. Hai, đặt giới hạn tỷ trọng tối đa cho một mã, ví dụ không quá một phần năm danh mục, để một sai lầm không phá hỏng cả tài khoản. Ba, góp đều định kỳ thay vì '
         'cố canh thời điểm, vì mua đều giúp bạn không phải quyết định đúng đáy, đúng đỉnh. Bốn, giới hạn số lần mở bảng giá mỗi ngày, vì xem giá liên tục làm cảm xúc mạnh lên mà '
         'thông tin không tăng. Những quy tắc này đơn giản, thậm chí hơi nhàm, nhưng nhàm là điều bạn cần: kết quả tốt của đầu tư thường đến từ sự đều đặn nhàm chán hơn là từ '
         'những quyết định xuất sắc.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Năm thiên kiến, năm câu hỏi',
  'cap': ('5 CÂU HỎI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('FOMO: mình mua vì lý do hay vì sợ lỡ?', (255, 196, 0)),
            ('Ác cảm lỗ: mình giữ vì tin hay vì không muốn thua?', (255, 196, 0)),
            ('Neo giá: nếu chưa có mã này, mình có mua không?', (255, 196, 0)),
            ('Tự tin quá: kết quả dài hạn của mình là bao nhiêu?', (255, 196, 0)),
            ('Bầy đàn: ai phản biện được lý do của mình?', (255, 196, 0))],
  'anh': 'five questions notebook',
  'say': 'Tổng kết với năm câu hỏi bạn có thể hỏi chính mình trước mỗi quyết định trong mười năm tới. FOMO: mình mua vì lý do hay vì sợ bỏ lỡ? Ác cảm thua lỗ: mình giữ vì tin vào '
         'doanh nghiệp hay vì không muốn thừa nhận thua? Neo giá: nếu hôm nay chưa sở hữu mã này, mình có mua không? Tự tin thái quá: kết quả dài hạn thật sự của mình là bao '
         'nhiêu? Bầy đàn: ai có thể phản biện lý do của mình? Bài tập cho bạn tuần này: chọn một vị thế đang lỗ và một vị thế đang lãi trong danh mục, rồi trả lời năm câu hỏi này '
         'bằng văn bản. Bạn sẽ thấy rất nhiều quyết định được lái bởi cảm xúc chứ không phải phân tích. Nhận ra là bước đầu tiên, và thiết kế quy trình là bước thứ hai. Hãy lưu '
         'video này để xem lại vào những lúc thị trường rất vui hoặc rất buồn.'},
 {'k': 'end',
  'label': '',
  'cap': ('TÂM LÝ ĐẦU TƯ', 'NHẬN RA TRƯỚC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các ví dụ về số tiền và tỷ suất trong video là số giả định để minh họa, không phải dự báo. Biểu đồ chỉ là hình nền. Nội dung chia sẻ kiến thức, không phải khuyến nghị '
         'mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Nền tảng đầu tư.'}]

