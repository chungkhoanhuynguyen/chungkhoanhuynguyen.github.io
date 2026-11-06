# -*- coding: utf-8 -*-
# VIDEO DÀI KÊNH CHÍNH – NV1 soạn 06/11/2026 (lô 20261106_0650: CH1511A, CH1511B, CH1511C, CH1611A, CH1611B, CH1611C). Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['CH1511A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VPB – Đọc BCTC 5 phút',
  'cap': ('NỢ XẤU 3,12%', 'VẪN LÃI +44,9%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VPBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[48, 24.95, 'Đỉnh tuần 12/10/26: 24,95', 0.6], [19, 18.63, 'Đáy tuần 23/3/26: 18,63', 1.6], [51, 21.9, 'Tuần 2/11/26: 21,90', 2.6]]},
  'anh': 'bank building vietnam',
  'say': 'Một ngân hàng có tỷ lệ nợ xấu ba phẩy mười hai phần trăm, cao hơn hẳn mức trung bình quen thuộc. Mà lợi nhuận chín tháng vẫn tăng bốn mươi bốn phẩy '
         'chín phần trăm. Nghe có vẻ vô lý, đúng không anh chị? Hầu hết mọi người nhìn thấy nợ xấu cao là loại ngay. Nhưng nợ xấu chỉ là một nửa câu chuyện. '
         'Nửa còn lại nằm ở chỗ ngân hàng kiếm tiền bằng cách nào, và đệm dự phòng dày hay mỏng. Video này em đọc báo cáo tài chính quý ba năm hai nghìn không '
         'trăm hai mươi sáu của VPBank. Mã VPB, theo năm bước: lợi nhuận, thu nhập lãi thuần, nợ xấu, bao phủ và định giá. Xem hết, anh chị sẽ biết vì sao '
         'cùng một con số nợ xấu mà cách đọc có thể khác nhau hoàn toàn. Số liệu tính đến ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, còn '
         'cách đọc thì dùng được nhiều năm. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ VPB (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q2/25', 4862.0, (56, 189, 248), '4.862'),
           ('Q3/25', 7276.0, (56, 189, 248), '7.276'),
           ('Q4/25', 7957.0, (56, 189, 248), '7.957'),
           ('Q1/26', 6199.0, (56, 189, 248), '6.199'),
           ('Q2/26', 8385.0, (56, 189, 248), '8.385'),
           ('Q3/26', 8644.0, (34, 197, 94), '8.644')],
  'anh': 'financial charts',
  'say': 'Bước một là nhìn lợi nhuận qua nhiều quý. Quý ba năm hai nghìn không trăm hai mươi sáu VPB lãi sau thuế tám nghìn sáu trăm bốn mươi bốn tỷ đồng. '
         'Tăng mười tám phẩy tám phần trăm so với cùng kỳ, và là quý cao nhất trong sáu quý trên biểu đồ. Cộng cả chín tháng là hai mươi ba nghìn hai trăm hai '
         'mươi bảy tỷ, tăng tới bốn mươi bốn phẩy chín phần trăm. Tại sao chín tháng tăng nhanh hơn một quý? Vì chín tháng đầu năm ngoái là nền thấp: riêng '
         'quý hai năm hai nghìn không trăm hai mươi lăm chỉ có bốn nghìn tám trăm sáu mươi hai tỷ. Đây là hiệu ứng nền so sánh. Khi quý cùng kỳ năm trước '
         'thấp, mức tăng trông rất đẹp. Khi quý cùng kỳ đã cao, như quý ba năm hai nghìn không trăm hai mươi lăm với bảy nghìn hai trăm bảy mươi sáu tỷ. Mức '
         'tăng nhìn khiêm tốn hơn dù lợi nhuận tuyệt đối vẫn lớn hơn. Quy tắc đầu tiên: luôn hỏi con số tăng trưởng đang được so với nền cao hay nền thấp.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần, động cơ chính',
  'moc': True,
  'label': 'Thu nhập lãi thuần VPB (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q2/25', 13479.0, (56, 189, 248), '13.479'),
           ('Q3/25', 15061.0, (56, 189, 248), '15.061'),
           ('Q4/25', 16767.0, (56, 189, 248), '16.767'),
           ('Q1/26', 16961.0, (56, 189, 248), '16.961'),
           ('Q2/26', 17974.0, (56, 189, 248), '17.974'),
           ('Q3/26', 18158.0, (34, 197, 94), '18.158')],
  'anh': 'financial charts',
  'say': 'Bước hai là thu nhập lãi thuần, khoản tiền lãi cho vay trừ đi lãi phải trả cho người gửi. Quý ba con số này là mười tám nghìn một trăm năm mươi tám '
         'tỷ đồng. Tăng hai mươi phẩy sáu phần trăm so với cùng kỳ, và tăng đều sáu quý liền, không có quý nào thụt lùi. Biên lãi ròng, gọi tắt là NIM, khoảng '
         'bốn phẩy năm mươi sáu phần trăm. Con số này cao hơn nhiều so với các ngân hàng cho vay chủ yếu doanh nghiệp lớn, vì VPBank có mảng cho vay tiêu '
         'dùng, nơi lãi suất cho vay cao hơn. Lãi từ dịch vụ cũng tăng hai mươi chín phẩy một phần trăm, đạt ba nghìn không trăm tám mươi chín tỷ. Nhìn chung '
         'phần lõi của ngân hàng đang chạy rất tốt. Nhưng lãi suất cho vay cao luôn đi kèm một cái giá, và cái giá đó nằm ở chương tiếp theo.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Vì sao biên lãi cao đi kèm nợ xấu cao',
  'moc': True,
  'label': 'Tiền lãi cao – rủi ro cao',
  'cap': ('LÃI CAO', 'RỦI RO CAO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('NIM khoảng', '4,56%', 'biên lãi ròng'), ('Nợ xấu', '3,12%', 'quý trước 3,28%'), ('Bao phủ nợ xấu', '~54%', 'đệm dự phòng')],
  'anh': 'insurance shield money',
  'say': 'Hãy nghĩ như thế này. Một người cho người quen vay có thế chấp sổ đỏ thì lấy lãi thấp, nhưng gần như không sợ mất tiền. Một người cho vay tiêu dùng, '
         'không tài sản đảm bảo, phải lấy lãi cao hơn vì biết sẽ có một phần khách không trả được. Biên lãi cao và nợ xấu cao thường đi cùng nhau, như hai mặt '
         'của một đồng xu. Vì vậy so sánh nợ xấu của VPBank với một ngân hàng chuyên cho vay doanh nghiệp lớn có tài sản bảo đảm là so sánh khập khiễng. Câu '
         'hỏi đúng không phải là nợ xấu cao hay thấp, mà là phần lãi ngân hàng kiếm thêm có đủ bù cho phần tiền mất đi hay không.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Nợ xấu và bao phủ',
  'moc': True,
  'label': 'Ba ngân hàng, ba mức bao phủ nợ xấu (%)',
  'cap': ('BAO PHỦ', 'NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('HDB', 46.0, (56, 189, 248), '46%'), ('VPB', 54.0, (56, 189, 248), '54%'), ('TPB', 57.0, (34, 197, 94), '57%')],
  'anh': 'bank vault',
  'say': 'Bước bốn là nợ xấu và bao phủ. Tỷ lệ nợ xấu của VPBank quý ba là ba phẩy mười hai phần trăm, giảm so với ba phẩy hai mươi tám phần trăm của quý '
         'trước. Chiều giảm này là tín hiệu tích cực, vì cho thấy tình hình đang được kiểm soát tốt hơn. Nhưng điểm cần chú ý là bao phủ nợ xấu chỉ khoảng năm '
         'mươi bốn phần trăm. Bao phủ cho biết ngân hàng đã trích sẵn bao nhiêu đồng dự phòng cho mỗi một trăm đồng nợ xấu. Mức năm mươi bốn phần trăm nghĩa '
         'là chưa đủ một nửa nợ xấu được che bằng tiền dự phòng. Con số này vẫn nhỉnh hơn một số ngân hàng khác trên biểu đồ, nhưng vẫn là đệm mỏng. Nếu nợ '
         'xấu nhích lên trở lại, ngân hàng sẽ phải trích thêm, và lợi nhuận là thứ bị ăn vào đầu tiên.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Ghép các mảnh lại',
  'moc': True,
  'label': 'Nợ xấu cao có nhất thiết là xấu?',
  'cap': ('GHÉP LẠI', 'CẢ BỨC TRANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Thu nhập lãi thuần tăng đều 6 quý liền', (34, 197, 94)),
            ('Nợ xấu giảm từ 3,28% xuống 3,12%', (34, 197, 94)),
            ('Lãi dịch vụ tăng 29,1%, thêm nguồn thu ngoài lãi', (34, 197, 94)),
            ('Bao phủ chỉ khoảng 54%, đệm còn mỏng', (239, 68, 68)),
            ('Cần theo dõi: quý sau nợ xấu có tiếp tục giảm không', (255, 196, 0))],
  'anh': 'scales balance',
  'say': 'Ghép các mảnh lại, em thấy ba điểm sáng và một điểm cần theo dõi. Điểm sáng thứ nhất, thu nhập lãi thuần tăng đều sáu quý liền. Điểm sáng thứ hai, '
         'nợ xấu quay đầu giảm. Điểm sáng thứ ba, lãi dịch vụ tăng gần ba mươi phần trăm, nghĩa là ngân hàng không chỉ sống bằng cho vay. Điểm cần theo dõi là '
         'bao phủ mới ở mức năm mươi bốn phần trăm. Vì vậy câu trả lời cho câu hỏi ở đầu video là: nợ xấu ba phẩy mười hai phần trăm mà lợi nhuận vẫn tăng '
         'mạnh là có thể giải thích được. Nhờ biên lãi cao và nền so sánh thấp. Nhưng nó chỉ bền khi nợ xấu tiếp tục đi xuống. Nếu quý sau con số này quay đầu '
         'tăng, bức tranh sẽ đổi ngay.'},
 {'k': 'cards',
  'ch': 'Chương 6 – Hiệu quả và định giá',
  'moc': True,
  'label': 'Hiệu quả và định giá VPB',
  'cap': ('ĐỊNH GIÁ', 'VPB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE', '17,0%', '4 quý gần nhất'), ('P/E', '7,1 lần', 'giá 21,9 nghìn'), ('P/B', '1,18 lần', 'vốn hóa 221.500 tỷ')],
  'anh': 'finance',
  'say': 'Bước năm là hiệu quả và định giá. ROE, tức lợi nhuận trên vốn chủ sở hữu, khoảng mười bảy phẩy không phần trăm. ROA khoảng hai phẩy ba phần trăm. '
         'Với giá khoảng hai mươi mốt phẩy chín nghìn đồng một cổ phiếu ở tuần hai tháng mười một năm hai nghìn không trăm hai mươi sáu. P/E khoảng bảy phẩy '
         'một lần và P/B khoảng một phẩy mười tám lần. Em lưu ý ngay một điều: P/E bảy phẩy một lần nghe rất thấp, nhưng nó không tự động có nghĩa là rẻ. Với '
         'ngân hàng có bao phủ nợ xấu mỏng, thị trường thường đòi hỏi mức chiết khấu cao hơn, tức là chấp nhận trả P/E thấp hơn. Cổ tức tiền mặt quy ra khoảng '
         'một phẩy bảy mươi chín phần trăm mỗi năm theo dữ liệu tổng hợp. Giá cổ phiếu cũng không đi thẳng: trong năm mươi hai tuần, đỉnh tuần là hai mươi bốn '
         'phẩy chín mươi lăm nghìn và đáy tuần là mười tám phẩy sáu mươi ba nghìn.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những cái bẫy khi đọc',
  'moc': True,
  'label': 'Ba cái bẫy khi đọc ngân hàng',
  'cap': ('BA CÁI BẪY', 'THƯỜNG GẶP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Bẫy 1: chỉ nhìn tăng trưởng, quên nền so sánh', (239, 68, 68)),
            ('Bẫy 2: so nợ xấu giữa hai mô hình kinh doanh khác nhau', (239, 68, 68)),
            ('Bẫy 3: thấy P/E thấp là kết luận rẻ', (239, 68, 68)),
            ('Cách tránh: đọc cả chuỗi 5 đến 6 quý', (34, 197, 94)),
            ('Đặt dự phòng cạnh nợ xấu và bao phủ', (34, 197, 94))],
  'anh': 'scales balance',
  'say': 'Qua ví dụ VPBank, em rút ra ba cái bẫy phổ biến. Bẫy thứ nhất là chỉ nhìn phần trăm tăng trưởng mà quên hỏi nền so sánh. Bẫy thứ hai là so nợ xấu '
         'giữa hai ngân hàng có mô hình kinh doanh khác nhau, như so cho vay tiêu dùng với cho vay doanh nghiệp lớn. Bẫy thứ ba là thấy P/E thấp là kết luận '
         'rẻ, trong khi P/E thấp đôi khi chỉ phản ánh rủi ro mà thị trường đang tính vào giá. Cách tránh khá đơn giản: đọc cả chuỗi năm đến sáu quý thay vì '
         'một quý, và luôn đặt chi phí dự phòng cạnh nợ xấu và bao phủ. Ba thứ này nằm cạnh nhau mới kể được câu chuyện đầy đủ.'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐỌC CẢ CHUỖI', 'ĐỪNG ĐỌC 1 QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, nợ xấu chỉ là một con số trong bức tranh, và phải được đọc cùng biên lãi, bao phủ và xu hướng nhiều quý. Cảm ơn anh chị đã xem. Theo anh '
         'chị, với một ngân hàng cho vay tiêu dùng, mức nợ xấu bao nhiêu thì bắt đầu đáng lo? Anh chị để lại ý kiến bên dưới giúp em nhé. Hẹn gặp anh chị ở '
         'video tiếp theo trong seri Đọc BCTC năm phút.'}]

S['CH1511B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'P/E thấp có rẻ không?',
  'cap': ('P/E THẤP 4,81', 'CÓ PHẢI RẺ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'TPBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[15, 15.78, 'Đỉnh tuần 23/2/26: 15,78', 0.6], [47, 11.25, 'Đáy tuần 5/10/26: 11,25', 1.6], [51, 12.8, 'Tuần 2/11/26: 12,80', 2.6]]},
  'anh': 'calculator finance',
  'say': 'Hai cổ phiếu ngân hàng, một cái P/E bốn phẩy tám mươi mốt lần, một cái P/E tám phẩy mười một lần. Cái nào rẻ hơn? Gần như ai cũng trả lời cái P/E '
         'thấp hơn. Nhưng nếu em nói rằng chỉ cần một quý lợi nhuận bất thường, P/E thấp có thể thành P/E cao chỉ sau vài tháng, anh chị còn tin con số đó '
         'không? Trong video này em chỉ ra P/E được tính thế nào, vì sao nó dễ bị bóp méo bởi đúng một quý, và ba câu hỏi cần đặt ra trước khi tin vào P/E. '
         'Xem hết, anh chị sẽ có một cách đọc P/E an toàn hơn. Số liệu lấy từ báo cáo quý ba năm hai nghìn không trăm hai mươi sáu, tính đến ngày năm tháng '
         'mười một năm hai nghìn không trăm hai mươi sáu.'},
 {'k': 'cards',
  'ch': 'Chương 1 – P/E là gì',
  'moc': True,
  'label': 'P/E tính thế nào',
  'cap': ('P/E', 'LÀ GÌ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Vốn hóa TPB', '40.674 tỷ', 'giá nhân số cổ phiếu'), ('LNST 4 quý', '8.453 tỷ', 'Q4/25 đến Q3/26'), ('P/E', '4,81 lần', '40.674 chia 8.453')],
  'anh': 'finance',
  'say': 'Trước hết, P/E là gì. P/E là giá thị trường chia cho lợi nhuận. Hiểu đơn giản: P/E bằng năm nghĩa là nếu lợi nhuận giữ nguyên, về lý thuyết cần '
         'khoảng năm năm lợi nhuận để bằng số tiền bỏ ra. Lấy Ngân hàng Tiên Phong làm ví dụ. Vốn hóa khoảng bốn mươi nghìn sáu trăm bảy mươi bốn tỷ đồng. Lợi '
         'nhuận bốn quý gần nhất cộng lại là tám nghìn bốn trăm năm mươi ba tỷ. Chia ra được bốn phẩy tám mươi mốt lần. Điểm then chốt: mẫu số là tổng bốn quý '
         'gần nhất. Mẫu số có thể bị kéo lên hoặc kéo xuống bởi một quý bất thường. Và khi mẫu số phình lên vì một quý lợi nhuận đẹp, P/E trông thấp đi, dù '
         'giá chưa hề thay đổi.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Một quý làm méo P/E',
  'moc': True,
  'label': 'LNST TPB theo quý (tỷ đồng)',
  'cap': ('MỘT QUÝ', 'LÀM MÉO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q4/25', 2565.0, (56, 189, 248), '2.565'),
           ('Q1/26', 1666.0, (56, 189, 248), '1.666'),
           ('Q2/26', 1828.0, (56, 189, 248), '1.828'),
           ('Q3/26', 2394.0, (34, 197, 94), '2.394')],
  'anh': 'financial charts',
  'say': 'Nhìn bốn quý tạo nên P/E bốn phẩy tám mươi mốt của TPB: quý bốn năm hai nghìn không trăm hai mươi lăm là hai nghìn năm trăm sáu mươi lăm tỷ. Quý một '
         'năm hai nghìn không trăm hai mươi sáu chỉ một nghìn sáu trăm sáu mươi sáu tỷ. Quý hai là một nghìn tám trăm hai mươi tám tỷ, quý ba là hai nghìn ba '
         'trăm chín mươi bốn tỷ. Hai quý cao là quý bốn và quý ba, hai quý còn lại thấp hơn rõ rệt. Thử một phép tính đơn giản: giả sử hai quý cao chỉ bằng '
         'mức trung bình của hai quý thấp, khoảng một nghìn bảy trăm bốn mươi bảy tỷ. Khi đó tổng bốn quý chỉ còn khoảng sáu nghìn chín trăm tám mươi tám tỷ, '
         'và P/E lên thành khoảng năm phẩy tám mươi hai lần. Tức là chỉ vì hai quý lợi nhuận đẹp mà P/E thấp hơn gần một đơn vị. Em nhấn mạnh đây là phép thử '
         'giả định để minh họa, không phải dự báo. Nó cho thấy P/E thấp chỉ đáng tin khi lợi nhuận bốn quý đó lặp lại được.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Chiều ngược lại',
  'moc': True,
  'label': 'LNST ACB theo quý (tỷ đồng)',
  'cap': ('NGƯỢC LẠI', 'CŨNG ĐÚNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q4/25', 2785.0, (56, 189, 248), '2.785'),
           ('Q1/26', 4320.0, (56, 189, 248), '4.320'),
           ('Q2/26', 4293.0, (56, 189, 248), '4.293'),
           ('Q3/26', 4699.0, (34, 197, 94), '4.699')],
  'anh': 'financial charts',
  'say': 'Cái bẫy chạy cả hai chiều. Với ACB, bốn quý gần nhất gồm một quý rất thấp là quý bốn năm hai nghìn không trăm hai mươi lăm với hai nghìn bảy trăm '
         'tám mươi lăm tỷ. Và ba quý quanh bốn nghìn ba trăm đến bốn nghìn bảy trăm tỷ. Tổng là mười sáu nghìn không trăm chín mươi bảy tỷ, vốn hóa khoảng một '
         'trăm mười tám nghìn chín trăm chín mươi mốt tỷ, nên P/E là bảy phẩy ba mươi chín lần. Nếu quý bốn ấy chỉ bình thường, khoảng bốn nghìn ba trăm tỷ. '
         'Tổng sẽ là khoảng mười bảy nghìn sáu trăm mười hai tỷ và P/E chỉ còn khoảng sáu phẩy bảy mươi sáu lần. Nghĩa là P/E của ACB đang hơi cao so với sức '
         'lợi nhuận thường lệ vì một quý lõm kéo mẫu số xuống. Vậy cùng là P/E, có cái bị làm đẹp, có cái bị làm xấu. Bởi thế một con số P/E đứng riêng lẻ gần '
         'như không nói lên điều gì.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Bảng so sánh',
  'moc': True,
  'label': 'P/E sáu ngân hàng lớn (lần)',
  'cap': ('P/E', 'SÁU NGÂN HÀNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('TPB', 4.81, (56, 189, 248), '4,81'),
           ('MBB', 5.96, (56, 189, 248), '5,96'),
           ('VPB', 7.1, (56, 189, 248), '7,10'),
           ('ACB', 7.39, (56, 189, 248), '7,39'),
           ('HDB', 7.48, (56, 189, 248), '7,48'),
           ('TCB', 8.11, (34, 197, 94), '8,11')],
  'anh': 'financial charts',
  'say': 'Đặt sáu ngân hàng cạnh nhau: TPB bốn phẩy tám mươi mốt lần, MBB năm phẩy chín mươi sáu lần, VPB bảy phẩy một lần. ACB bảy phẩy ba mươi chín lần, HDB '
         'bảy phẩy bốn mươi tám lần và TCB tám phẩy mười một lần. Chênh nhau chưa tới hai lần giữa thấp nhất và cao nhất. Nhưng khác biệt thật nằm ở những thứ '
         'P/E không cho thấy. HDB có ROE hai mươi ba phẩy ba phần trăm nhưng bao phủ nợ xấu chỉ bốn mươi sáu phần trăm. TCB có ROE chỉ mười lăm phẩy bốn phần '
         'trăm nhưng cổ tức tiền mặt quy ra khoảng năm phẩy mười ba phần trăm mỗi năm. MBB có ROE hai mươi mốt phẩy tám phần trăm và cổ tức khoảng bốn phẩy '
         'mười sáu phần trăm. P/E giống nhau không có nghĩa chất lượng giống nhau. Đây là lý do em nói P/E là điểm khởi đầu cho câu hỏi, chứ không phải câu '
         'trả lời.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Ba câu hỏi trước khi tin P/E',
  'moc': True,
  'label': 'Ba câu hỏi trước khi tin P/E',
  'cap': ('BA CÂU HỎI', 'VỀ P/E'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Câu 1: bốn quý đó có quý nào bất thường không', (255, 196, 0)),
            ('Câu 2: ROE và tăng trưởng đi kèm ra sao', (255, 196, 0)),
            ('Câu 3: chất lượng tài sản, nợ xấu và bao phủ', (255, 196, 0)),
            ('P/E thấp + quý bất thường = chưa chắc rẻ', (239, 68, 68)),
            ('P/E vừa + chuỗi đều + đệm dày = đáng xem kỹ', (34, 197, 94))],
  'anh': 'scales balance',
  'say': 'Vậy trước khi tin vào một con số P/E, em đề xuất ba câu hỏi. Câu một: trong bốn quý tính P/E có quý nào bất thường không, cao vọt hoặc thấp lõm. Câu '
         'hai: ROE và tốc độ tăng trưởng đi kèm ra sao, vì P/E thấp mà lợi nhuận đang đi xuống thì khác hẳn P/E thấp mà lợi nhuận đang đi lên. Câu ba: chất '
         'lượng tài sản, tức là nợ xấu và bao phủ. Một ngân hàng đệm mỏng thường bị thị trường định giá thấp hơn, và có lý do chính đáng. Nếu cả ba câu hỏi '
         'đều ổn, P/E mới có giá trị tham khảo. Nếu một trong ba câu có vấn đề, P/E thấp chỉ là một dấu hiệu cần đọc thêm, chưa phải cơ hội.'},
 {'k': 'end',
  'label': '',
  'cap': ('P/E LÀ CÂU HỎI', 'CHƯA PHẢI ĐÁP ÁN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, P/E là điểm bắt đầu để đặt câu hỏi, không phải đáp án. Cảm ơn anh chị đã xem. Lâu nay anh chị thường nhìn P/E hay P/B trước khi xem một cổ '
         'phiếu ngân hàng? Anh chị để lại ý kiến bên dưới giúp em nhé. Hẹn gặp anh chị ở video tiếp theo.'}]

S['CH1511C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Bài học lịch sử | Tháng 4/2025',
  'cap': ('RỚT 18,5%', 'TRONG 2 TUẦN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 90,
            'circles': [[65, 1933.11, 'Đỉnh tuần 18/5/26: 1933,11', 0.6],
                        [8, 1073.61, 'Đáy tuần 7/4/25: 1073,61', 1.6],
                        [89, 1740.73, 'Tuần 2/11/26: 1740,73', 2.6]]},
  'anh': 'stock market crash',
  'say': 'Chỉ trong hai tuần. VN-Index rớt mười tám phẩy năm phần trăm từ giá đóng cửa tuần hai mươi bốn tháng ba năm hai nghìn không trăm hai mươi lăm xuống '
         'đáy tuần bảy tháng tư năm hai nghìn không trăm hai mươi lăm. Tức là từ khoảng một nghìn ba trăm mười bảy điểm xuống còn một nghìn không trăm bảy '
         'mươi ba điểm. Nhiều người khi đó nghĩ là hết, thị trường sẽ về vùng thấp hơn nữa. Vậy tám mươi hai tuần sau chuyện gì đã xảy ra? Video này nằm trong '
         'seri Bài học lịch sử. Em dùng số liệu thật của chỉ số để kể lại một đợt giảm điểm sâu, rồi rút ra ba bài học về tâm lý và kỷ luật đầu tư. Xem hết, '
         'anh chị sẽ biết vì sao đợt giảm mạnh thường khó đoán, và điều gì thực sự quyết định kết quả của người đi qua nó. Đây là nội dung lịch sử, không dự '
         'đoán tương lai. Số liệu tính đến ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Điều gì đã xảy ra',
  'moc': True,
  'label': 'VN-Index giá đóng cửa tuần (điểm)',
  'cap': ('RỚT NHANH', 'TRONG 2 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('24/3', 1317.0, (56, 189, 248), '1.317'),
           ('31/3', 1211.0, (56, 189, 248), '1.211'),
           ('7/4 đáy', 1074.0, (56, 189, 248), '1.074'),
           ('7/4 đóng', 1222.0, (34, 197, 94), '1.222')],
  'anh': 'financial charts',
  'say': 'Hãy xem diễn biến. Tuần bắt đầu ngày hai mươi bốn tháng ba năm hai nghìn không trăm hai mươi lăm, VN-Index đóng cửa ở khoảng một nghìn ba trăm mười '
         'bảy điểm. Tuần kế tiếp, ba mươi mốt tháng ba, đóng cửa một nghìn hai trăm mười một điểm, giảm tám phẩy một phần trăm. Sang tuần bảy tháng tư, chỉ số '
         'có lúc chạm một nghìn không trăm bảy mươi bốn điểm. Giảm mười tám phẩy năm phần trăm so với giá đóng cửa tuần hai mươi bốn tháng ba. Bối cảnh khi đó '
         'là thông báo về mức thuế đối ứng của Mỹ ở đầu tháng bốn, tạo ra lo ngại rất lớn với các nền kinh tế xuất khẩu như Việt Nam. Điều đáng chú ý ở thanh '
         'cuối: cũng ngay trong tuần đó, chỉ số đóng cửa ở một nghìn hai trăm hai mươi hai điểm. Nghĩa là bật lại mười ba phẩy chín phần trăm từ đáy. Giảm sâu '
         'và bật mạnh xảy ra gần như cùng một tuần.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Nhìn lại 82 tuần',
  'moc': True,
  'label': 'Từ đáy đến nay',
  'cap': ('SAU ĐỢT RỚT', '82 TUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Đáy tuần 7/4/25', '1.073,61', 'điểm'), ('Tuần 2/11/26', '1.740,73', 'giá đóng cửa'), ('Chênh lệch', '+62,1%', 'so với đáy')],
  'anh': 'trending chart',
  'say': 'Nhìn lại tám mươi hai tuần sau đó. Từ đáy một nghìn không trăm bảy mươi ba phẩy sáu mươi mốt điểm. Tuần đầu tháng mười một năm hai nghìn không trăm '
         'hai mươi sáu chỉ số đóng cửa ở một nghìn bảy trăm bốn mươi phẩy bảy mươi ba điểm. Cao hơn sáu mươi hai phẩy một phần trăm so với đáy. Còn so với giá '
         'đóng cửa tuần hai mươi bốn tháng ba năm hai nghìn không trăm hai mươi lăm. Tức trước khi rớt, chỉ số cao hơn ba mươi hai phẩy một phần trăm. Chỉ số '
         'cũng từng lên tới đỉnh tuần một nghìn chín trăm ba mươi ba điểm vào tuần ngày mười tám tháng năm năm hai nghìn không trăm hai mươi sáu. Em nhắc lại '
         'để tránh hiểu nhầm: đây là kết quả sau khi đã biết đáp án. Vào lúc đang rớt, không ai biết đáy nằm ở đâu, và ngay cả sau đáy tuần bảy tháng tư. Chỉ '
         'số vẫn có tuần quay lại thử vùng thấp ở tuần hai mươi mốt tháng tư với mức một nghìn một trăm ba mươi bảy điểm.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Hồi phục không thẳng',
  'moc': True,
  'label': 'VN-Index đóng cửa tuần, sau đáy (điểm)',
  'cap': ('HỒI PHỤC', 'KHÔNG THẲNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('7/4', 1222.0, (56, 189, 248), '1.222'),
           ('14/4', 1219.0, (56, 189, 248), '1.219'),
           ('21/4', 1229.0, (56, 189, 248), '1.229'),
           ('28/4', 1226.0, (56, 189, 248), '1.226'),
           ('5/5', 1267.0, (56, 189, 248), '1.267'),
           ('26/5', 1333.0, (34, 197, 94), '1.333')],
  'anh': 'financial charts',
  'say': 'Đừng tưởng sau đáy là một đường lên thẳng. Các tuần sau đó, giá đóng cửa quanh một nghìn hai trăm mười chín đến một nghìn hai trăm hai mươi chín '
         'điểm trong ba tuần liền. Rồi mới lên một nghìn hai trăm sáu mươi bảy ở tuần năm tháng năm. Phải đến tuần hai mươi sáu tháng năm, tức khoảng bảy tuần '
         'sau, chỉ số mới đóng cửa ở một nghìn ba trăm ba mươi ba điểm. Vượt giá đóng cửa tuần hai mươi bốn tháng ba trước khi rớt. Trong bảy tuần đó có đủ '
         'tin tức tốt xấu lẫn lộn, có lúc ai cũng tưởng đợt giảm quay lại. Người giữ được tâm lý trong giai đoạn đi ngang nhàm chán này chịu nhiều áp lực '
         'không kém lúc chỉ số rớt.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Ba bài học',
  'moc': True,
  'label': 'Ba bài học tâm lý',
  'cap': ('BA BÀI HỌC', 'TỪ THÁNG 4'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Đáy chỉ nhìn thấy khi đã qua rồi', (255, 196, 0)),
            ('2. Rớt nhanh thường đi cùng bật nhanh', (255, 196, 0)),
            ('3. Tiền không cần dùng mới giữ được bình tĩnh', (34, 197, 94)),
            ('Tránh: dồn toàn bộ vốn vào một thời điểm', (239, 68, 68)),
            ('Tránh: vay ký quỹ sát mức bị bán giải chấp', (239, 68, 68))],
  'anh': 'scales balance',
  'say': 'Từ đó em rút ra ba bài học. Bài học một: đáy chỉ nhìn thấy khi đã qua. Tuần bảy tháng tư không có biển báo nào ghi đây là đáy, và các tuần sau còn '
         'quay lại thử. Bài học hai: rớt nhanh thường đi cùng bật nhanh, nên quyết định bán vì hoảng loạn ở đúng đáy là sai lầm đắt giá nhất. Bài học ba: '
         'người giữ được bình tĩnh thường là người dùng tiền nhàn rỗi, không cần rút ra trong ngắn hạn. Ngược lại, những ai vay ký quỹ sát mức bị bán giải '
         'chấp thường không có quyền lựa chọn, vì tài khoản bị bán thay họ. Em không nói nên mua đáy hay nên bán, mà nói về cách chuẩn bị trước, khi thị '
         'trường còn yên.'},
 {'k': 'end',
  'label': '',
  'cap': ('KỶ LUẬT', 'THẮNG DỰ ĐOÁN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, thị trường sẽ còn những tuần rớt mạnh như tháng bốn năm hai nghìn không trăm hai mươi lăm. Điều quyết định kết quả là kỷ luật chuẩn bị từ '
         'trước chứ không phải khả năng đoán đáy. Cảm ơn anh chị đã xem. Lần đó anh chị đã làm gì khi chỉ số rớt sâu? Anh chị để lại ý kiến bên dưới giúp em '
         'nhé. Hẹn gặp anh chị ở video tiếp theo trong seri Bài học lịch sử.'}]

S['CH1611A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'TPB – Đọc BCTC 5 phút',
  'cap': ('LÃI +57,4%', 'NỢ XẤU CŨNG TĂNG?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'TPBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[15, 15.78, 'Đỉnh tuần 23/2/26: 15,78', 0.6], [47, 11.25, 'Đáy tuần 5/10/26: 11,25', 1.6], [51, 12.8, 'Tuần 2/11/26: 12,80', 2.6]]},
  'anh': 'bank building vietnam',
  'say': 'Lợi nhuận quý ba của một ngân hàng tăng năm mươi bảy phẩy bốn phần trăm so với cùng kỳ. Tin tốt tuyệt đối, đúng không anh chị? Nhưng cũng trong báo '
         'cáo đó, tỷ lệ nợ xấu lại nhích từ một phẩy tám mươi sáu phần trăm lên hai phẩy mười phần trăm. Hai con số này nằm cạnh nhau và kể hai câu chuyện '
         'trái ngược. Vậy nên tin vào con số nào? Trong video này em đọc báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của Ngân hàng Tiên '
         'Phong. Mã TPB, theo năm bước: lợi nhuận, thu nhập lãi thuần, nợ xấu và bao phủ, định giá, rồi những điều cần theo dõi. Xem hết, anh chị sẽ biết cách '
         'phân biệt một quý bứt phá nhờ hoạt động cốt lõi với một quý đẹp nhờ yếu tố khác. Số liệu tính đến ngày năm tháng mười một năm hai nghìn không trăm '
         'hai mươi sáu.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ TPB (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q2/25', 1630.0, (56, 189, 248), '1.630'),
           ('Q3/25', 1521.0, (56, 189, 248), '1.521'),
           ('Q4/25', 2565.0, (56, 189, 248), '2.565'),
           ('Q1/26', 1666.0, (56, 189, 248), '1.666'),
           ('Q2/26', 1828.0, (56, 189, 248), '1.828'),
           ('Q3/26', 2394.0, (34, 197, 94), '2.394')],
  'anh': 'financial charts',
  'say': 'Bước một, lợi nhuận qua các quý. Quý ba năm hai nghìn không trăm hai mươi sáu TPB lãi sau thuế hai nghìn ba trăm chín mươi bốn tỷ đồng. Tăng năm '
         'mươi bảy phẩy bốn phần trăm so với cùng kỳ và tăng ba mươi mốt phần trăm so với quý trước. Nhưng hãy nhìn thanh thứ ba trên biểu đồ: quý bốn năm hai '
         'nghìn không trăm hai mươi lăm đã có lúc lên hai nghìn năm trăm sáu mươi lăm tỷ. Rồi quý sau tụt xuống một nghìn sáu trăm sáu mươi sáu tỷ. Lợi nhuận '
         'của ngân hàng này có những quý nhảy vọt, rồi lại lùi. Điều đó cho thấy nó không đi theo đường thẳng mà dao động theo từng quý. Cộng chín tháng, lợi '
         'nhuận đạt năm nghìn tám trăm tám mươi bảy tỷ, tăng hai mươi mốt phẩy bảy phần trăm. Con số hai mươi mốt phẩy bảy phần trăm của chín tháng phản ánh '
         'sức khỏe dài hạn tốt hơn con số năm mươi bảy phẩy bốn phần trăm của một quý. Vì một quý thường bị méo bởi nền so sánh. Quý ba năm hai nghìn không '
         'trăm hai mươi lăm chỉ có một nghìn năm trăm hai mươi mốt tỷ, là nền khá thấp.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần TPB (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q2/25', 3151.0, (56, 189, 248), '3.151'),
           ('Q3/25', 3238.0, (56, 189, 248), '3.238'),
           ('Q4/25', 3599.0, (56, 189, 248), '3.599'),
           ('Q1/26', 3460.0, (56, 189, 248), '3.460'),
           ('Q2/26', 3634.0, (56, 189, 248), '3.634'),
           ('Q3/26', 4424.0, (34, 197, 94), '4.424')],
  'anh': 'financial charts',
  'say': 'Bước hai, thu nhập lãi thuần, động cơ chính của ngân hàng. Quý ba là bốn nghìn bốn trăm hai mươi bốn tỷ đồng, tăng ba mươi sáu phẩy sáu phần trăm so '
         'với cùng kỳ, và tăng mạnh nhất trong sáu quý. Đây là tin tốt thật sự, vì nó đến từ hoạt động cho vay, không phải từ khoản thu bất thường. Biên lãi '
         'ròng, NIM, khoảng hai phẩy năm mươi tám phần trăm, thấp hơn nhiều so với các ngân hàng cho vay tiêu dùng. Biên thấp nghĩa là ngân hàng kiếm lãi mỏng '
         'hơn trên mỗi đồng cho vay, nên tăng trưởng phải đến từ quy mô. Vì vậy mức tăng ba mươi sáu phẩy sáu phần trăm có giá trị: nó cho thấy dư nợ đang mở '
         'rộng đáng kể. Bây giờ là câu hỏi quan trọng: tăng trưởng nhanh như vậy có phải trả giá bằng chất lượng tín dụng hay không.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Nợ xấu nhích lên',
  'moc': True,
  'label': 'Nợ xấu và bao phủ TPB',
  'cap': ('NỢ XẤU', 'NHÍCH LÊN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Nợ xấu', '2,10%', 'quý trước 1,86%'), ('Bao phủ', '~57%', 'đệm dự phòng'), ('Biến động', '+0,24', 'điểm phần trăm')],
  'anh': 'insurance shield money',
  'say': 'Bước ba là nợ xấu. Tỷ lệ nợ xấu của TPB quý ba là hai phẩy mười phần trăm, tăng so với một phẩy tám mươi sáu phần trăm của quý trước. Tức là nhích '
         'thêm khoảng không phẩy hai mươi bốn điểm phần trăm. Bao phủ nợ xấu khoảng năm mươi bảy phần trăm, nghĩa là mỗi một trăm đồng nợ xấu mới có khoảng '
         'năm mươi bảy đồng dự phòng. Em nói thẳng: một quý nhích lên chưa phải là xu hướng. Nhưng khi cho vay tăng nhanh, nợ xấu thường tăng với độ trễ, vì '
         'khoản vay mới cần thời gian mới lộ rủi ro. Vì vậy khi thấy lợi nhuận và dư nợ cùng tăng vọt, anh chị nên để mắt tới nợ xấu ở hai đến ba quý sau, chứ '
         'không chỉ quý này. Một con số tăng không làm bức tranh xấu đi, nhưng nó là lý do để đọc kỹ hơn.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Quý đẹp nhờ đâu',
  'moc': True,
  'label': 'Phân biệt hai kiểu quý đẹp',
  'cap': ('QUÝ ĐẸP', 'NHỜ ĐÂU?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Kiểu 1: thu nhập lãi lõi tăng, dư nợ mở rộng', (34, 197, 94)),
            ('Kiểu 2: hoàn nhập dự phòng hoặc thu nhập bất thường', (239, 68, 68)),
            ('TPB quý 3: thu nhập lãi thuần tăng 36,6%', (34, 197, 94)),
            ('Nhưng nợ xấu nhích lên, bao phủ chỉ ~57%', (239, 68, 68)),
            ('Cần xem: 2 quý tới nợ xấu đi hướng nào', (255, 196, 0))],
  'anh': 'scales balance',
  'say': 'Bước bốn là phân biệt hai kiểu quý đẹp. Kiểu thứ nhất là quý đẹp nhờ hoạt động lõi: thu nhập lãi thuần tăng, dư nợ mở rộng. Kiểu thứ hai là quý đẹp '
         'nhờ yếu tố không lặp lại, như hoàn nhập dự phòng hay thu nhập bất thường. Với TPB, thu nhập lãi thuần tăng tới ba mươi sáu phẩy sáu phần trăm, nên '
         'phần lớn mức tăng đến từ hoạt động lõi. Đó là điểm cộng. Nhưng em chưa có đủ dữ liệu để khẳng định toàn bộ mức tăng năm mươi bảy phẩy bốn phần trăm '
         'là bền, vì còn phụ thuộc vào chi phí dự phòng từng quý. Cách kiểm tra đơn giản anh chị có thể tự làm: lấy lợi nhuận trừ đi phần đóng góp của thu '
         'nhập lãi thuần. Nếu phần còn lại biến động thất thường thì quý đó có yếu tố nhất thời.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Hiệu quả và định giá',
  'moc': True,
  'label': 'Hiệu quả và định giá TPB',
  'cap': ('ĐỊNH GIÁ', 'TPB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE', '17,9%', '4 quý gần nhất'), ('P/E', '4,81 lần', 'giá 12,8 nghìn'), ('P/B', '0,87 lần', 'dưới giá trị sổ sách')],
  'anh': 'finance',
  'say': 'Bước năm, hiệu quả và định giá. ROE khoảng mười bảy phẩy chín phần trăm, ROA khoảng một phẩy sáu phần trăm. Với giá khoảng mười hai phẩy tám nghìn '
         'đồng một cổ phiếu, P/E khoảng bốn phẩy tám mươi mốt lần và P/B khoảng không phẩy tám mươi bảy lần. Tức là giá thị trường thấp hơn giá trị sổ sách. '
         'Nhìn sơ qua thì rất hấp dẫn. Nhưng đừng vội. P/E tính trên lợi nhuận bốn quý gần nhất. Mà quý bốn năm hai nghìn không trăm hai mươi lăm và quý ba '
         'năm hai nghìn không trăm hai mươi sáu đều là hai quý lợi nhuận cao. Nếu hai quý này không lặp lại, P/E thực tế sẽ cao hơn con số bốn phẩy tám mươi '
         'mốt. Đây chính là lý do em luôn nói P/E thấp không đồng nghĩa với rẻ. Giá cổ phiếu năm mươi hai tuần cũng dao động mạnh: đỉnh tuần mười lăm phẩy bảy '
         'mươi tám nghìn hồi tháng hai và đáy tuần mười một phẩy hai mươi lăm nghìn hồi tháng mười.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Những điểm cần theo dõi',
  'moc': True,
  'label': 'Ba việc cần theo dõi ở TPB',
  'cap': ('THEO DÕI', 'TPB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Nợ xấu quý sau: tiếp tục nhích hay quay đầu', (255, 196, 0)),
            ('Bao phủ có được nâng từ mức ~57% không', (255, 196, 0)),
            ('Lợi nhuận quý sau có giữ được mức 2.000 tỷ không', (255, 196, 0)),
            ('Thu nhập lãi thuần có tăng đều không', (34, 197, 94)),
            ('Không có cổ tức tiền mặt theo dữ liệu tổng hợp', (56, 189, 248))],
  'anh': 'scales balance',
  'say': 'Cuối cùng là danh sách ba việc cần theo dõi ở các quý sau. Thứ nhất, nợ xấu: tiếp tục nhích lên hay quay đầu giảm. Thứ hai, bao phủ nợ xấu có được '
         'nâng lên từ mức năm mươi bảy phần trăm hay không. Thứ ba, lợi nhuận quý sau có duy trì được quanh mốc hai nghìn tỷ hay lại lùi như sau quý bốn năm '
         'ngoái. Thêm một chi tiết nhỏ: theo dữ liệu tổng hợp, tỷ suất cổ tức tiền mặt của TPB hiện bằng không. Nên người sở hữu chủ yếu trông vào giá và sự '
         'tăng trưởng của lợi nhuận. Em không đưa ra kết luận mua bán, mà chỉ muốn anh chị có sẵn một danh sách để so sánh với báo cáo quý tiếp theo.'},
 {'k': 'end',
  'label': '',
  'cap': ('NHÌN CẢ HAI MẶT', 'LÃI VÀ NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, lợi nhuận tăng mạnh là tin tốt, nhưng chỉ đáng tin khi nợ xấu và bao phủ đi cùng hướng. Cảm ơn anh chị đã xem. Khi một ngân hàng lãi tăng '
         'vọt mà nợ xấu nhích lên, anh chị sẽ tin con số nào hơn? Anh chị để lại ý kiến bên dưới giúp em nhé. Hẹn gặp anh chị ở video tiếp theo trong seri Đọc '
         'BCTC năm phút.'}]

S['CH1611B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'HDB – Đọc BCTC 5 phút',
  'cap': ('LÃI QUÝ GIẢM 30,7%', 'LÕI VẪN +19,6%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'HDBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[48, 23.45, 'Đỉnh tuần 12/10/26: 23,45', 0.6], [1, 17.23, 'Đáy tuần 10/11/25: 17,23', 1.6], [51, 22.45, 'Tuần 2/11/26: 22,45', 2.6]]},
  'anh': 'bank building vietnam',
  'say': 'Lợi nhuận quý ba của một ngân hàng giảm tới ba mươi phẩy bảy phần trăm so với quý trước. Nghe như tin xấu, đúng không anh chị? Nhưng thu nhập lãi '
         'thuần, phần cốt lõi nhất của ngân hàng, vẫn tăng mười chín phẩy sáu phần trăm so với cùng kỳ. Vậy lợi nhuận đã đi đâu? Trong video này em đọc báo '
         'cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu của HDBank. Mã HDB, và chỉ ra vì sao hai con số trái chiều này có thể cùng đúng. Em đi '
         'theo năm bước: lợi nhuận, thu nhập lãi thuần, chi phí dự phòng, nợ xấu và bao phủ, rồi định giá. Xem hết, anh chị sẽ biết khi nào lợi nhuận giảm là '
         'bình thường, và khi nào là dấu hiệu cần dè chừng. Số liệu tính đến ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ HDB (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q2/25', 3515.0, (56, 189, 248), '3.515'),
           ('Q3/25', 3647.0, (56, 189, 248), '3.647'),
           ('Q4/25', 5128.0, (56, 189, 248), '5.128'),
           ('Q1/26', 4767.0, (56, 189, 248), '4.767'),
           ('Q2/26', 5555.0, (56, 189, 248), '5.555'),
           ('Q3/26', 3852.0, (34, 197, 94), '3.852')],
  'anh': 'financial charts',
  'say': 'Bước một, lợi nhuận qua các quý. Quý ba năm hai nghìn không trăm hai mươi sáu HDB lãi sau thuế ba nghìn tám trăm năm mươi hai tỷ đồng. So với cùng '
         'kỳ năm trước là ba nghìn sáu trăm bốn mươi bảy tỷ thì tăng năm phẩy sáu phần trăm, một mức tăng nhỏ. Nhưng so với quý hai năm hai nghìn không trăm '
         'hai mươi sáu là năm nghìn năm trăm năm mươi lăm tỷ thì giảm tới ba mươi phẩy bảy phần trăm. Thanh cuối cùng trên biểu đồ thấp hẳn so với ba thanh '
         'liền trước. Đó là lý do con số giảm ba mươi phẩy bảy phần trăm nghe đáng lo. Tuy nhiên, nhìn cả chín tháng đầu năm thì lợi nhuận vẫn đạt mười bốn '
         'nghìn một trăm bảy mươi bốn tỷ, tăng hai mươi bốn phẩy bốn phần trăm so với cùng kỳ. Nghĩa là bức tranh cả năm vẫn đẹp, chỉ có riêng quý ba bị chững '
         'lại. Bài học đầu tiên: đừng bao giờ phán xét một ngân hàng qua một quý, dù quý đó tăng hay giảm.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần HDB (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 7763.0, (56, 189, 248), '7.763'),
           ('Q4/25', 9756.0, (56, 189, 248), '9.756'),
           ('Q1/26', 8483.0, (56, 189, 248), '8.483'),
           ('Q2/26', 9737.0, (56, 189, 248), '9.737'),
           ('Q3/26', 9288.0, (34, 197, 94), '9.288')],
  'anh': 'financial charts',
  'say': 'Bước hai, thu nhập lãi thuần, quý ba là chín nghìn hai trăm tám mươi tám tỷ đồng. Tăng mười chín phẩy sáu phần trăm so với cùng kỳ bảy nghìn bảy '
         'trăm sáu mươi ba tỷ. Biên lãi ròng khoảng ba phẩy bốn mươi bảy phần trăm. Lãi từ dịch vụ còn tăng mạnh hơn, bốn mươi mốt phẩy ba phần trăm, đạt một '
         'nghìn sáu trăm bảy mươi bảy tỷ. Như vậy hoạt động kinh doanh cốt lõi của HDBank vẫn đang tăng khá tốt. Em lưu ý một chi tiết: so với quý hai thì thu '
         'nhập lãi thuần có giảm nhẹ. Từ chín nghìn bảy trăm ba mươi bảy tỷ xuống chín nghìn hai trăm tám mươi tám tỷ. Nhưng mức giảm này nhỏ hơn rất nhiều so '
         'với mức giảm ba mươi phẩy bảy phần trăm của lợi nhuận. Vậy phần chênh lệch lớn đó không nằm ở thu nhập lãi. Nó phải nằm ở khoản chi phí nào đó đã '
         'tăng mạnh, và đây là lúc nói đến chi phí dự phòng.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Chi phí dự phòng',
  'moc': True,
  'label': 'Chi phí dự phòng tăng mạnh',
  'cap': ('DỰ PHÒNG', 'TĂNG MẠNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Chi phí dự phòng', '+47,4%', 'so với cùng kỳ'), ('Thu nhập lãi thuần', '+19,6%', 'cùng kỳ'), ('Lợi nhuận quý', '+5,6%', 'cùng kỳ')],
  'anh': 'insurance shield money',
  'say': 'Chi phí dự phòng là khoản tiền ngân hàng trích ra từ lợi nhuận để phòng khi khách hàng không trả được nợ. Trích nhiều thì lợi nhuận kế toán thấp đi, '
         'dù hoạt động cho vay vẫn tốt. Theo báo cáo, chi phí dự phòng của HDB quý ba tăng bốn mươi bảy phẩy bốn phần trăm, nhanh gấp hơn hai lần thu nhập lãi '
         'thuần. Đó chính là lý do thu nhập lãi tăng mười chín phẩy sáu phần trăm mà lợi nhuận chỉ tăng năm phẩy sáu phần trăm. Phần chênh lệch đã bị dự phòng '
         'ăn mất. Câu hỏi quan trọng là vì sao ngân hàng trích nhiều như vậy. Có hai khả năng: hoặc ngân hàng thận trọng, chủ động làm dày đệm trước, hoặc rủi '
         'ro tín dụng thực sự đang tăng. Muốn phân biệt, anh chị phải nhìn sang nợ xấu.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Nợ xấu và bao phủ',
  'moc': True,
  'label': 'Bao phủ nợ xấu (%)',
  'cap': ('BAO PHỦ', 'NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('HDB', 46.0, (56, 189, 248), '46%'), ('VPB', 54.0, (56, 189, 248), '54%'), ('TPB', 57.0, (34, 197, 94), '57%')],
  'anh': 'bank vault',
  'say': 'Bước bốn là nợ xấu và bao phủ. Tỷ lệ nợ xấu của HDB quý ba là ba phẩy bốn mươi hai phần trăm. Tăng khá mạnh so với hai phẩy bảy mươi chín phần trăm '
         'của quý trước, khoảng không phẩy sáu mươi ba điểm phần trăm trong đúng một quý. Bao phủ nợ xấu chỉ khoảng bốn mươi sáu phần trăm, thấp hơn cả VPBank '
         'và TPB trên biểu đồ. Như vậy cách đọc đầu tiên, rằng ngân hàng thận trọng làm dày đệm, chỉ đúng một phần. Ngân hàng đã trích dự phòng nhiều hơn, '
         'nhưng nợ xấu cũng tăng nhanh hơn và đệm vẫn mỏng nhất trong ba cái tên. Thông điệp: chi phí dự phòng tăng đi cùng nợ xấu tăng là tín hiệu rủi ro '
         'đang nhích lên thật, chứ không chỉ là sự thận trọng. Nhưng một quý chưa tạo nên xu hướng, nên cần theo dõi thêm.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Hiệu quả và định giá',
  'moc': True,
  'label': 'Hiệu quả và định giá HDB',
  'cap': ('ĐỊNH GIÁ', 'HDB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE', '23,3%', 'cao nhất nhóm'), ('P/E', '7,48 lần', 'giá 22,45 nghìn'), ('P/B', '1,61 lần', 'cao hơn các mã khác')],
  'anh': 'finance',
  'say': 'Bước năm, hiệu quả và định giá. ROE của HDB khoảng hai mươi ba phẩy ba phần trăm, thuộc nhóm cao nhất trong các ngân hàng em so sánh. Với giá khoảng '
         'hai mươi hai phẩy bốn mươi lăm nghìn đồng, P/E khoảng bảy phẩy bốn mươi tám lần và P/B khoảng một phẩy sáu mươi mốt lần. P/B cao hơn VPB và TPB, '
         'nhưng đi kèm ROE cao hơn. Đây là quy luật chung: thị trường thường chấp nhận trả P/B cao cho ngân hàng có ROE cao. Câu hỏi là mức ROE hai mươi ba '
         'phẩy ba phần trăm có bền không khi nợ xấu đang nhích lên và dự phòng phải trích nhiều hơn. Nếu phải trích nhiều hơn, lợi nhuận giảm và ROE sẽ giảm '
         'theo. Giá cổ phiếu trong năm mươi hai tuần có đỉnh tuần hai mươi ba phẩy bốn mươi lăm nghìn hồi tháng mười và đáy tuần mười bảy phẩy hai mươi ba '
         'nghìn hồi tháng mười một năm ngoái.'},
 {'k': 'end',
  'label': '',
  'cap': ('GIẢM 30,7%', 'CHƯA PHẢI HẾT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, lợi nhuận giảm so với quý trước chưa chắc là xấu, nhưng khi đi cùng nợ xấu tăng và bao phủ mỏng thì cần theo dõi sát. Cảm ơn anh chị đã '
         'xem. Theo anh chị, một quý lợi nhuận giảm mạnh nên đọc là nhiễu hay là tín hiệu? Anh chị để lại ý kiến bên dưới giúp em nhé. Hẹn gặp anh chị ở video '
         'tiếp theo trong seri Đọc BCTC năm phút.'}]

S['CH1611C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'So sánh 6 ngân hàng',
  'cap': ('ROE 23,3%', 'MÀ P/B 1,61?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'HDBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[48, 23.45, 'Đỉnh tuần 12/10/26: 23,45', 0.6], [1, 17.23, 'Đáy tuần 10/11/25: 17,23', 1.6], [51, 22.45, 'Tuần 2/11/26: 22,45', 2.6]]},
  'anh': 'bank building vietnam',
  'say': 'Có ngân hàng ROE hai mươi ba phẩy ba phần trăm, có ngân hàng chỉ mười lăm phẩy bốn phần trăm. Nhưng P/B của hai bên lại khá giống nhau, một bên một '
         'phẩy sáu mươi mốt lần, một bên một phẩy hai mươi bốn lần. Nhìn qua tưởng thị trường định giá sai, đúng không anh chị? Thực ra P/B và ROE đi cùng '
         'nhau theo một quy luật mà ít người để ý. Video này em đặt sáu ngân hàng lớn cạnh nhau: HDB, MBB, TPB, VPB, ACB và TCB, theo ba trục ROE, P/B và cổ '
         'tức. Xem hết, anh chị sẽ biết cách đọc bảng so sánh ngân hàng mà không bị đánh lừa bởi một con số đơn lẻ. Số liệu tính đến ngày năm tháng mười một '
         'năm hai nghìn không trăm hai mươi sáu, còn cách đọc dùng được lâu dài.'},
 {'k': 'bars',
  'ch': 'Chương 1 – ROE',
  'moc': True,
  'label': 'ROE sáu ngân hàng (%)',
  'cap': ('ROE', 'AI CAO NHẤT?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('TCB', 15.4, (56, 189, 248), '15,4%'),
           ('ACB', 16.5, (56, 189, 248), '16,5%'),
           ('VPB', 17.0, (56, 189, 248), '17,0%'),
           ('TPB', 17.9, (56, 189, 248), '17,9%'),
           ('MBB', 21.8, (56, 189, 248), '21,8%'),
           ('HDB', 23.3, (34, 197, 94), '23,3%')],
  'anh': 'financial charts',
  'say': 'Bắt đầu với ROE, tức lợi nhuận trên vốn chủ sở hữu, thước đo ngân hàng sinh lời trên số vốn của chủ sở hữu giỏi đến đâu. Xếp từ thấp lên cao: TCB '
         'mười lăm phẩy bốn phần trăm, ACB mười sáu phẩy năm phần trăm, VPB mười bảy phần trăm. TPB mười bảy phẩy chín phần trăm, MBB hai mươi mốt phẩy tám '
         'phần trăm và HDB hai mươi ba phẩy ba phần trăm. Khoảng cách giữa cao nhất và thấp nhất tới gần tám điểm phần trăm. Với ngân hàng, ROE cao nghĩa là '
         'mỗi đồng vốn tạo ra nhiều lợi nhuận hơn. Nhưng ROE cũng có thể cao nhờ đòn bẩy, tức vay mượn nhiều hơn so với vốn, nên cần đọc cùng chất lượng tài '
         'sản. Ở đây em chỉ dùng ROE làm trục thứ nhất, chưa kết luận gì.'},
 {'k': 'bars',
  'ch': 'Chương 2 – P/B',
  'moc': True,
  'label': 'P/B sáu ngân hàng (lần)',
  'cap': ('P/B', 'AI ĐẮT NHẤT?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('TPB', 0.87, (56, 189, 248), '0,87'),
           ('ACB', 1.14, (56, 189, 248), '1,14'),
           ('VPB', 1.18, (56, 189, 248), '1,18'),
           ('MBB', 1.23, (56, 189, 248), '1,23'),
           ('TCB', 1.24, (56, 189, 248), '1,24'),
           ('HDB', 1.61, (34, 197, 94), '1,61')],
  'anh': 'financial charts',
  'say': 'Trục thứ hai là P/B, giá thị trường chia cho giá trị sổ sách. TPB thấp nhất với không phẩy tám mươi bảy lần, tức giá thấp hơn sổ sách. Tiếp theo là '
         'ACB một phẩy mười bốn, VPB một phẩy mười tám, MBB một phẩy hai mươi ba. TCB một phẩy hai mươi bốn và HDB cao nhất với một phẩy sáu mươi mốt lần. Bốn '
         'ngân hàng nằm gọn trong khoảng một phẩy mười bốn đến một phẩy hai mươi bốn. Điều thú vị là TCB và MBB có P/B gần như bằng nhau, một phẩy hai mươi '
         'bốn và một phẩy hai mươi ba. Trong khi ROE của MBB là hai mươi mốt phẩy tám phần trăm, cao hơn TCB mười lăm phẩy bốn phần trăm khá nhiều. Nói cách '
         'khác, với cùng mức giá trả trên sổ sách, MBB đang tạo ra nhiều lợi nhuận hơn trên mỗi đồng vốn. Nhưng TCB có những thứ khác để bù, như cổ tức, và '
         'quy mô vốn hóa lớn nhất nhóm.'},
 {'k': 'bars',
  'ch': 'Chương 3 – Cổ tức',
  'moc': True,
  'label': 'Tỷ suất cổ tức tiền mặt (%/năm)',
  'cap': ('CỔ TỨC', 'TIỀN MẶT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('HDB', 0.0, (56, 189, 248), '0%'),
           ('TPB', 0.0, (56, 189, 248), '0%'),
           ('VPB', 1.79, (56, 189, 248), '1,79%'),
           ('ACB', 3.02, (56, 189, 248), '3,02%'),
           ('MBB', 4.16, (56, 189, 248), '4,16%'),
           ('TCB', 5.13, (34, 197, 94), '5,13%')],
  'anh': 'financial charts',
  'say': 'Trục thứ ba là cổ tức tiền mặt theo dữ liệu tổng hợp. HDB và TPB bằng không. VPB khoảng một phẩy bảy mươi chín phần trăm, ACB khoảng ba phẩy không '
         'hai phần trăm. MBB khoảng bốn phẩy mười sáu phần trăm và TCB khoảng năm phẩy mười ba phần trăm mỗi năm. Cổ tức không phải là tiêu chí duy nhất, vì '
         'ngân hàng giữ lại lợi nhuận để tăng vốn cũng có thể tạo giá trị về sau, như chia cổ phiếu. Nhưng nếu anh chị ưu tiên dòng tiền đều, nhóm cổ tức cao '
         'sẽ khác nhóm bằng không. Và cổ tức của quá khứ không bảo đảm cho tương lai, mức chi trả thay đổi theo từng năm tùy quyết định của đại hội cổ đông.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Đọc chung ba trục',
  'moc': True,
  'label': 'Không có ngân hàng nào hoàn hảo',
  'cap': ('ĐỌC CHUNG', 'BA TRỤC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('HDB: ROE cao nhất, P/B cao nhất, cổ tức 0%', (255, 196, 0)),
            ('MBB: ROE cao, P/B vừa, cổ tức khá', (34, 197, 94)),
            ('TCB: ROE thấp nhất, cổ tức cao nhất', (255, 196, 0)),
            ('TPB: P/B dưới 1 nhưng cổ tức 0%', (255, 196, 0)),
            ('Mỗi mã đánh đổi một thứ', (56, 189, 248))],
  'anh': 'scales balance',
  'say': 'Ghép ba trục lại, mỗi ngân hàng đánh đổi một thứ. HDB có ROE và P/B cao nhất, cổ tức bằng không. MBB nằm giữa, ROE cao, P/B vừa phải, cổ tức khá. '
         'TCB có ROE thấp nhất nhưng cổ tức cao nhất. TPB có P/B dưới một nhưng cổ tức bằng không. Không có ngân hàng nào hơn hẳn ở cả ba trục. Vì vậy câu hỏi '
         'đúng không phải là mã nào tốt nhất, mà là mục tiêu của anh chị là gì: dòng tiền, tăng trưởng, hay định giá thấp. Mỗi mục tiêu sẽ chọn trục ưu tiên '
         'khác nhau. Em chỉ đưa số liệu để anh chị tự đối chiếu, không đưa ra khuyến nghị mua bán.'},
 {'k': 'end',
  'label': '',
  'cap': ('KHÔNG CÓ MÃ', 'HOÀN HẢO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, so sánh ngân hàng cần nhìn cùng lúc ROE, P/B, cổ tức và chất lượng tài sản, đừng để một con số quyết định. Cảm ơn anh chị đã xem. Trong ba '
         'trục ROE, P/B và cổ tức, anh chị ưu tiên trục nào khi xem một cổ phiếu ngân hàng? Anh chị để lại ý kiến bên dưới giúp em nhé. Hẹn gặp anh chị ở '
         'video tiếp theo.'}]

