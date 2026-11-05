# -*- coding: utf-8 -*-
# VIDEO DÀI KÊNH CHÍNH – NV1 soạn 06/11/2026 (lô 20261106_0215: CH1311A, CH1311B, CH1311C, CH1411A, CH1411B, CH1411C). Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['CH1311A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'ACB – Đọc BCTC 5 phút',
  'cap': ('LÃI THUẦN +21,1%', 'LÃI RÒNG +9,8%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'ACBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[35, 23.85, 'Đỉnh tuần 13/7/26: 23,85', 0.6], [17, 18.7, 'Đáy tuần 9/3/26: 18,70', 1.6], [51, 20.55, 'Tuần 2/11/26: 20,55', 2.6]]},
  'anh': 'bank building vietnam',
  'say': 'Cùng một ngân hàng, cùng một quý. Thu nhập lãi thuần tăng hai mươi mốt phẩy một phần trăm, nhưng lợi nhuận sau thuế chỉ tăng chín phẩy tám phần trăm. Phần '
         'tăng trưởng đẹp nhất của ngân hàng đã đi đâu mất hơn một nửa trên đường từ doanh thu xuống tới lợi nhuận? Câu trả lời nằm ở một dòng trong báo cáo mà nhiều '
         'người lướt qua: chi phí dự phòng, tăng tới hai trăm hai mươi ba phẩy hai phần trăm so với cùng kỳ. Trong video này mình mổ xẻ báo cáo tài chính quý ba năm hai '
         'nghìn không trăm hai mươi sáu của Ngân hàng Á Châu, mã ACB, từng bước một: lợi nhuận, thu nhập lãi thuần, chi phí dự phòng, nợ xấu cùng bao phủ, rồi định giá. '
         'Xem hết, bạn sẽ biết vì sao lợi nhuận tăng chậm hơn thu nhập lõi chưa chắc là tin xấu, và khi nào nó là tin xấu. Video thuộc seri Đọc BCTC năm phút. Số liệu '
         'là ví dụ minh họa tại ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, còn cách đọc dùng được nhiều năm. Biểu đồ phía sau chỉ là hình nền minh '
         'họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Bước 1: Lợi nhuận sau thuế qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ ACB theo quý (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 4281.0, (56, 189, 248), '4.281'),
           ('Q4/25', 2785.0, (239, 68, 68), '2.785'),
           ('Q1/26', 4320.0, (56, 189, 248), '4.320'),
           ('Q2/26', 4293.0, (56, 189, 248), '4.293'),
           ('Q3/26', 4699.0, (34, 197, 94), '4.699')],
  'anh': 'financial report charts',
  'say': 'Bước một là nhìn lợi nhuận sau thuế của công ty mẹ qua nhiều quý chứ không chỉ một quý. Quý ba năm hai nghìn không trăm hai mươi sáu ACB lãi bốn nghìn sáu '
         'trăm chín mươi chín tỷ đồng, cao hơn chín phẩy tám phần trăm so với bốn nghìn hai trăm tám mươi mốt tỷ của quý ba năm ngoái. Lũy kế chín tháng đạt mười ba '
         'nghìn ba trăm mười hai tỷ, tăng ba phẩy bảy phần trăm. Bây giờ nhìn thanh thứ hai trên biểu đồ: quý bốn năm hai nghìn không trăm hai mươi lăm chỉ có hai nghìn '
         'bảy trăm tám mươi lăm tỷ, thấp hơn hẳn bốn quý còn lại. Một quý lõm như vậy là lời nhắc rằng lợi nhuận ngân hàng không đi theo đường thẳng, nó phụ thuộc vào '
         'việc ngân hàng trích dự phòng nhiều hay ít trong từng quý. Quý ba năm nay là quý cao nhất trong năm quý, nhưng mức tăng ba phẩy bảy phần trăm sau chín tháng '
         'cho thấy bức tranh cả năm chậm hơn con số chín phẩy tám phần trăm của một quý. Quy tắc đầu tiên: đừng bao giờ kết luận từ một con số quý duy nhất.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Bước 2: Thu nhập lãi thuần, động cơ chính',
  'moc': True,
  'label': 'Thu nhập lãi thuần ACB theo quý (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 6770.0, (56, 189, 248), '6.770'),
           ('Q4/25', 7093.0, (56, 189, 248), '7.093'),
           ('Q1/26', 6989.0, (56, 189, 248), '6.989'),
           ('Q2/26', 7785.0, (56, 189, 248), '7.785'),
           ('Q3/26', 8195.0, (34, 197, 94), '8.195')],
  'anh': 'bank loans interest',
  'say': 'Bước hai là thu nhập lãi thuần, tức là tiền lãi ngân hàng thu từ cho vay trừ đi tiền lãi phải trả cho người gửi. Đây là động cơ chính của một ngân hàng thương '
         'mại. Quý ba năm hai nghìn không trăm hai mươi sáu con số này là tám nghìn một trăm chín mươi lăm tỷ đồng, tăng hai mươi mốt phẩy một phần trăm so với sáu '
         'nghìn bảy trăm bảy mươi tỷ cùng kỳ, và là mức cao nhất trong năm quý trên biểu đồ. Đọc điều này thế nào? Hoạt động cho vay cốt lõi của ngân hàng đang khỏe: dư '
         'nợ tăng và chênh lệch giữa lãi cho vay với lãi huy động duy trì tốt. Nếu chỉ nhìn thu nhập lãi thuần, bạn sẽ nghĩ lợi nhuận phải tăng khoảng hai mươi phần '
         'trăm. Nhưng lợi nhuận chỉ tăng chín phẩy tám phần trăm. Độ chênh khoảng mười một điểm phần trăm đó chính là câu hỏi của cả video: phần thu nhập tăng thêm đã '
         'bị khoản nào ăn mất, và ăn mất vì lý do tốt hay vì lý do xấu?'},
 {'k': 'cards',
  'ch': 'Chương 3 – Bước 3: Chi phí dự phòng là gì',
  'moc': True,
  'label': 'Chi phí dự phòng, nói đơn giản',
  'cap': ('DỰ PHÒNG', 'LÀ GÌ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Chi phí dự phòng', '+223,2%', 'so với cùng kỳ'), ('Thu nhập lãi thuần', '+21,1%', 'động cơ chính'), ('Lợi nhuận sau thuế', '+9,8%', 'phần còn lại')],
  'anh': 'insurance shield money',
  'say': 'Chi phí dự phòng giống như tiền mua bảo hiểm cho những khoản vay có thể không thu hồi được. Khi ngân hàng cho rằng một số khoản vay có nguy cơ xấu đi, kế toán '
         'buộc họ trích một khoản tiền từ lợi nhuận để đặt sang một bên, và khoản này được tính là chi phí ngay trong quý đó. Ở ACB, chi phí dự phòng quý ba tăng hai '
         'trăm hai mươi ba phẩy hai phần trăm so với cùng kỳ, nghĩa là hơn gấp ba lần. Ba con số trên màn hình kể cả câu chuyện: động cơ lãi tăng hai mươi mốt phẩy một '
         'phần trăm, chi phí dự phòng tăng vọt, nên lợi nhuận chỉ còn tăng chín phẩy tám phần trăm. Tin tốt là ngân hàng không giấu rủi ro, họ trích trước. Tin cần cân '
         'nhắc là sở dĩ họ phải trích nhiều là vì họ thấy rủi ro đang lớn hơn. Nên câu hỏi tiếp theo hiển nhiên là nợ xấu có thật sự tăng không.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Bước 4: Nợ xấu và bao phủ nợ xấu',
  'moc': True,
  'label': 'Chất lượng tài sản ACB quý 3/2026',
  'cap': ('NỢ XẤU', 'VÀ BAO PHỦ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Tỷ lệ nợ xấu', '1,19%', 'quý trước 1,03%'), ('Mức tăng', '+0,16 điểm', 'trong một quý'), ('Bao phủ nợ xấu', 'khoảng 91%', 'dự phòng / nợ xấu')],
  'anh': 'bank risk loans',
  'say': 'Bước bốn là nợ xấu và bao phủ nợ xấu. Tỷ lệ nợ xấu của ACB quý ba là một phẩy mười chín phần trăm, tăng so với một phẩy không ba phần trăm của quý trước, tức '
         'nhích thêm khoảng không phẩy mười sáu điểm phần trăm trong ba tháng. Về độ lớn, một phẩy mười chín phần trăm vẫn là mức thấp so với nhiều ngân hàng trên thị '
         'trường, nhưng về xu hướng thì đang đi lên, và điều đó khớp với việc chi phí dự phòng tăng mạnh. Bao phủ nợ xấu khoảng chín mươi mốt phần trăm nghĩa là cứ một '
         'trăm đồng nợ xấu thì ngân hàng đã dự phòng khoảng chín mươi mốt đồng. Dưới một trăm phần trăm không có nghĩa là nguy hiểm, vì nhiều khoản nợ xấu có tài sản '
         'đảm bảo, nhưng nó cho biết bộ đệm đang mỏng hơn mức an toàn tuyệt đối. Hãy ghi nhớ cặp đôi này: nợ xấu cho bạn biết rủi ro đã lộ ra bao nhiêu, bao phủ cho bạn '
         'biết ngân hàng đã chuẩn bị đến đâu.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Ghép các mảnh lại: lợi nhuận tăng chậm là tốt hay xấu',
  'moc': True,
  'label': 'Hai cách đọc cùng một con số',
  'cap': ('TỐT HAY', 'XẤU?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Cách đọc 1: ngân hàng thận trọng, trích dự phòng sớm', (34, 197, 94)),
            ('Cách đọc 2: rủi ro tín dụng đang nhích lên thật', (239, 68, 68)),
            ('Dấu hiệu ủng hộ cách 1: nợ xấu vẫn ở mức thấp, 1,19%', (34, 197, 94)),
            ('Dấu hiệu ủng hộ cách 2: nợ xấu còn nhích thêm ở quý sau?', (239, 68, 68)),
            ('Cần theo dõi: quý sau dự phòng giảm hay tăng thêm', (255, 196, 0))],
  'anh': 'scales balance',
  'say': 'Giờ ghép các mảnh lại. Lợi nhuận tăng chậm hơn thu nhập lõi có hai cách đọc hợp lý. Cách thứ nhất: ngân hàng thận trọng, thấy rủi ro thì trích dự phòng sớm, '
         'giống một người lái xe đạp phanh trước khi vào cua. Dấu hiệu ủng hộ cách này là nợ xấu vẫn ở mức thấp. Cách thứ hai: rủi ro tín dụng thật sự đang nhích lên và '
         'dự phòng chỉ phản ánh điều đó. Dấu hiệu ủng hộ cách này là nợ xấu tăng và bao phủ dưới một trăm phần trăm. Cả hai dấu hiệu hôm nay đều có mặt, nên chưa thể '
         'kết luận. Người đọc báo cáo giỏi không vội chọn phe, mà ghi ra thứ cần theo dõi: quý sau chi phí dự phòng giảm xuống hay tiếp tục tăng, tỷ lệ nợ xấu quay đầu '
         'hay nhích thêm. Một quý cho bạn câu hỏi, hai ba quý mới cho bạn câu trả lời.'},
 {'k': 'cards',
  'ch': 'Chương 6 – Bước 5: Hiệu quả và định giá',
  'moc': True,
  'label': 'Chỉ số ACB tại ngày 5/11/2026',
  'cap': ('ROE VÀ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE 4 quý', '16,5%', 'sinh lời trên vốn chủ'), ('P/E', '7,39 lần', 'giá / lợi nhuận mỗi cổ phiếu'), ('P/B', '1,14 lần', 'giá / giá trị sổ sách')],
  'anh': 'stock valuation calculator',
  'say': 'Bước năm là hiệu quả và định giá. ROE bốn quý gần nhất của ACB khoảng mười sáu phẩy năm phần trăm, nghĩa là mỗi một trăm đồng vốn chủ sinh ra khoảng mười sáu '
         'phẩy năm đồng lợi nhuận trong năm. P/E là bảy phẩy ba mươi chín lần, tức giá thị trường bằng gần bảy lần rưỡi lợi nhuận mỗi cổ phiếu trong bốn quý gần nhất. '
         'P/B là một phẩy mười bốn lần, tức giá chỉ cao hơn giá trị sổ sách khoảng mười bốn phần trăm. Nhưng đừng đọc ba con số này như một bảng điểm. P/E thấp hay P/B '
         'thấp chỉ có ý nghĩa khi đặt cạnh chất lượng lợi nhuận. Nếu quý sau dự phòng tiếp tục tăng, lợi nhuận bốn quý có thể thấp đi và P/E hôm nay sẽ trông rẻ hơn '
         'thực tế. Ngược lại, nếu dự phòng hạ nhiệt, ROE có thể cải thiện. Định giá luôn là câu hỏi về tương lai, còn báo cáo chỉ cho bạn dữ liệu quá khứ để đặt câu hỏi '
         'cho tốt.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những cái bẫy khi đọc báo cáo ngân hàng',
  'moc': True,
  'label': 'Bẫy thường gặp',
  'cap': ('3 CÁI BẪY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Chỉ nhìn tăng trưởng lợi nhuận một quý', (239, 68, 68)),
            ('Quên so với quý liền trước và cùng kỳ năm trước', (239, 68, 68)),
            ('Bỏ qua chi phí dự phòng và nợ xấu', (239, 68, 68)),
            ('Thấy P/B thấp là kết luận rẻ ngay', (239, 68, 68)),
            ('Cách làm đúng: đọc cả chuỗi 5 quý', (34, 197, 94))],
  'anh': 'warning sign red',
  'say': 'Ba cái bẫy lớn khi đọc báo cáo ngân hàng. Bẫy thứ nhất: chỉ nhìn tăng trưởng lợi nhuận của một quý. Một quý tăng chín phẩy tám phần trăm hay bốn mươi bốn phần '
         'trăm đều có thể là hiệu ứng của nền so sánh, và quý bốn năm hai nghìn không trăm hai mươi lăm thấp của ACB là ví dụ sống động. Bẫy thứ hai: bỏ qua chi phí dự '
         'phòng. Hai ngân hàng cùng tăng lợi nhuận hai mươi phần trăm nhưng một bên nhờ trích dự phòng ít đi, một bên tăng thu nhập lõi, chất lượng hoàn toàn khác nhau. '
         'Bẫy thứ ba: thấy P/B thấp rồi kết luận là rẻ. P/B thấp có thể là cơ hội, cũng có thể là mức giá hợp lý cho một ngân hàng có ROE thấp hoặc chất lượng tài sản '
         'đang xấu đi. Cách phòng bẫy chung: luôn đọc cả chuỗi năm quý và đặt ít nhất ba câu hỏi trước khi có bất kỳ kết luận nào.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài tập tự làm và tài liệu đi kèm',
  'moc': True,
  'label': 'Làm thử với một ngân hàng khác',
  'cap': ('BÀI TẬP', 'TỰ LÀM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Bước 1: lấy 5 quý lợi nhuận của một ngân hàng', (255, 196, 0)),
            ('Bước 2: so tăng trưởng thu nhập lãi thuần với lợi nhuận', (255, 196, 0)),
            ('Bước 3: tìm chi phí dự phòng, nợ xấu, bao phủ', (255, 196, 0)),
            ('Bước 4: ghi 2 câu hỏi cần theo dõi quý sau', (255, 196, 0)),
            ('Bảng số 400 mã: chungkhoanhuynguyen.com', (56, 189, 248))],
  'anh': 'student notebook homework',
  'say': 'Để dùng được kiến thức này, bạn hãy làm bài tập nhỏ sau. Chọn một ngân hàng bất kỳ, lấy lợi nhuận năm quý gần nhất. So sánh tốc độ tăng của thu nhập lãi thuần '
         'với tốc độ tăng của lợi nhuận sau thuế. Nếu hai con số lệch nhau nhiều, hãy tìm chi phí dự phòng để giải thích. Sau đó xem tỷ lệ nợ xấu và bao phủ nợ xấu, rồi '
         'viết ra hai câu hỏi cần theo dõi ở quý sau. Mất khoảng mười lăm phút, và sau vài lần bạn sẽ đọc báo cáo nhanh hơn nhiều. Toàn bộ số liệu trong video, kèm bảng '
         'báo cáo tài chính của hơn bốn trăm mã, đều có sẵn miễn phí tại chứng khoán Huy Nguyễn chấm com, kèm bài viết đi cùng video này để bạn đối chiếu. Số liệu ví dụ '
         'mang tính chia sẻ kiến thức, không phải khuyến nghị mua bán.'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐỌC CẢ CHUỖI', 'ĐỪNG ĐỌC 1 QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, lợi nhuận sau thuế chỉ là điểm cuối của một hành trình dài. Muốn hiểu một ngân hàng, hãy đi từ thu nhập lãi thuần, qua chi phí dự phòng, nợ xấu và '
         'bao phủ, rồi mới tới ROE và định giá. Cảm ơn bạn đã xem. Hẹn gặp bạn ở video tiếp theo trong seri Đọc BCTC năm phút.'}]

S['CH1311B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – hình nền minh họa',
  'cap': ('NỬA SAU CHIẾM', '60% KẾT QUẢ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, 'Tuần 2/11/26: 1.741', 2.6]]},
  'anh': 'compound interest growth',
  'say': 'Giả sử mỗi tháng bạn góp đều ba triệu đồng trong mười năm. Tổng tiền bạn bỏ ra là ba trăm sáu mươi triệu. Với mức sinh lời giả định tám phần trăm mỗi năm, tài '
         'khoản của bạn sau mười năm sẽ khoảng năm trăm bốn mươi chín triệu đồng. Nhưng con số thú vị nhất không phải là năm trăm bốn mươi chín. Mà là khi nhìn lại, năm '
         'năm đầu chỉ tạo ra khoảng bốn mươi phần trăm kết quả, còn năm năm sau tạo ra tới sáu mươi phần trăm. Cùng số tiền góp, cùng mức sinh lời, tại sao nửa sau lại '
         'nặng gấp rưỡi nửa đầu? Đó là lãi kép, và cũng là lý do rất nhiều người bỏ cuộc đúng vào lúc nó sắp phát huy tác dụng. Trong video này mình giải thích lãi kép '
         'bằng số cụ thể, giới thiệu quy tắc bảy mươi hai để nhẩm nhanh, và chỉ ra ba kẻ thù khiến người ta mất lãi kép. Xem hết, bạn sẽ biết vì sao kỷ luật quan trọng '
         'hơn việc tìm ra thời điểm hoàn hảo. Toàn bộ là số giả định để minh họa, không phải cam kết lợi nhuận. Biểu đồ phía sau chỉ là hình nền.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Ba con số của ví dụ',
  'moc': True,
  'label': 'Góp 3 triệu/tháng trong 10 năm, giả định 8%/năm',
  'cap': ('3 CON SỐ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Vốn bạn góp', '360 triệu', '3 triệu x 120 tháng'),
            ('Giá trị cuối kỳ', '~549 triệu', 'giả định 8%/năm'),
            ('Phần do lãi sinh ra', '~189 triệu', 'chênh lệch')],
  'anh': 'saving money jar',
  'say': 'Hãy bắt đầu từ ba con số của ví dụ. Mỗi tháng góp ba triệu, trong mười năm là một trăm hai mươi tháng, tổng vốn bạn bỏ ra là ba trăm sáu mươi triệu đồng. Giả '
         'định tài khoản sinh lời tám phần trăm mỗi năm, lãi được tính gộp theo tháng và tái đầu tư liên tục. Sau mười năm giá trị khoảng năm trăm bốn mươi chín triệu '
         'đồng. Phần chênh lệch khoảng một trăm tám mươi chín triệu là tiền do lãi sinh ra, hay còn gọi là tiền đẻ ra tiền. Cần nhấn mạnh ngay: tám phần trăm mỗi năm ở '
         'đây là con số giả định để dễ tính. Thị trường thật không bao giờ cho bạn đúng tám phần trăm đều đặn mỗi năm, có năm lãi hơn hai mươi phần trăm, có năm lỗ. Mục '
         'đích của ví dụ không phải để hứa hẹn kết quả, mà để bạn thấy cơ chế vận hành của lãi kép khi thời gian đủ dài.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Đường cong cong lên',
  'moc': True,
  'label': 'Giá trị tài khoản theo số năm góp (triệu đồng, giả định 8%/năm)',
  'cap': ('THEO NĂM',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('3 năm', 122.0, (56, 189, 248), '122'),
           ('5 năm', 220.0, (56, 189, 248), '220'),
           ('10 năm', 549.0, (34, 197, 94), '549'),
           ('15 năm', 1038.0, (34, 197, 94), '1.038'),
           ('20 năm', 1767.0, (255, 196, 0), '1.767')],
  'anh': 'growth chart rising',
  'say': 'Nhìn biểu đồ năm cột. Sau ba năm, bạn có khoảng một trăm hai mươi hai triệu, trong đó vốn góp là một trăm linh tám triệu. Sau năm năm, khoảng hai trăm hai '
         'mươi triệu, vốn góp một trăm tám mươi triệu. Sau mười năm là năm trăm bốn mươi chín triệu, vốn góp ba trăm sáu mươi triệu. Sau mười lăm năm hơn một nghìn '
         'không trăm ba mươi tám triệu, tức là hơn một tỷ đồng, vốn góp chỉ năm trăm bốn mươi triệu. Và sau hai mươi năm khoảng một nghìn bảy trăm sáu mươi bảy triệu '
         'trong khi vốn góp bảy trăm hai mươi triệu. Để ý một điều: khoảng cách giữa các cột không đều nhau. Từ năm thứ mười đến năm thứ mười lăm tài khoản tăng thêm '
         'gần bốn trăm chín mươi triệu, trong khi năm năm đầu chỉ tăng hai trăm hai mươi triệu. Mỗi năm, số tiền được cộng thêm lớn hơn năm trước, vì lãi giờ được tính '
         'cả trên phần lãi đã có. Đó là lý do đồ thị lãi kép trông phẳng lúc đầu rồi cong vút lên về sau.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Khi lãi vượt vốn góp',
  'moc': True,
  'label': 'Điểm chuyển giao của ví dụ 3 triệu/tháng',
  'cap': ('LÃI > VỐN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Năm thứ 16', 'lãi > vốn góp', '1.162 triệu so với 576 triệu góp'),
            ('Sau 20 năm', 'vốn góp 720 triệu', 'giá trị ~1.767 triệu'),
            ('Phần lãi 20 năm', '~1.047 triệu', 'gấp ~1,5 lần vốn góp')],
  'anh': 'turning point',
  'say': 'Có một cột mốc tâm lý rất quan trọng: thời điểm tiền lãi vượt tổng số tiền bạn đã góp. Với ví dụ ba triệu mỗi tháng và tám phần trăm mỗi năm, mốc này đến vào '
         'khoảng năm thứ mười sáu: tài khoản khoảng một nghìn một trăm sáu mươi hai triệu, trong khi vốn góp mới năm trăm bảy mươi sáu triệu. Sau hai mươi năm, vốn góp '
         'là bảy trăm hai mươi triệu nhưng phần lãi sinh ra đã lên tới khoảng một nghìn không trăm bốn mươi bảy triệu, gấp rưỡi vốn. Nghĩa là trong mười sáu năm đầu, '
         'bạn cảm giác công sức của mình mới là phần chính, nhưng sau đó chính tài khoản mới là bên làm việc. Vấn đề là chỉ một số ít người đủ kiên nhẫn tới đoạn ấy. '
         'Phần lớn người đầu tư đổi ý, dừng góp, hoặc rút ra sau vài năm, đúng lúc đường cong chuẩn bị dốc lên. Vì thế kỷ luật mới là lợi thế thật sự, còn mức sinh lời '
         'chỉ là gia vị.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Quy tắc 72 để nhẩm nhanh',
  'moc': True,
  'label': 'Bao nhiêu năm để tiền nhân đôi',
  'cap': ('QUY TẮC 72',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lấy 72 chia cho lãi suất mỗi năm (%)', (255, 255, 255)),
            ('Sinh lời 6%/năm: khoảng 12 năm nhân đôi', (56, 189, 248)),
            ('Sinh lời 8%/năm: khoảng 9 năm nhân đôi', (34, 197, 94)),
            ('Sinh lời 10%/năm: khoảng 7,2 năm nhân đôi', (34, 197, 94)),
            ('Sinh lời 12%/năm: khoảng 6 năm nhân đôi', (255, 196, 0))],
  'anh': 'calculator math',
  'say': 'Để nhẩm nhanh không cần máy tính, hãy nhớ quy tắc bảy mươi hai. Lấy bảy mươi hai chia cho mức sinh lời mỗi năm tính bằng phần trăm, kết quả là số năm xấp xỉ '
         'để một khoản tiền tăng gấp đôi. Sinh lời sáu phần trăm mỗi năm thì khoảng mười hai năm nhân đôi. Sinh lời tám phần trăm thì khoảng chín năm. Sinh lời mười '
         'phần trăm thì bảy phẩy hai năm. Sinh lời mười hai phần trăm thì sáu năm. Quy tắc này cũng dùng ngược được: nếu bạn muốn tiền nhân đôi trong sáu năm thì cần '
         'mức sinh lời khoảng mười hai phần trăm mỗi năm, và một mục tiêu như vậy thường đi kèm rủi ro cao hơn rất nhiều. Một công dụng khác là đo lạm phát: nếu lạm '
         'phát bốn phần trăm mỗi năm thì sức mua của tiền mặt giảm một nửa sau khoảng mười tám năm. Quy tắc bảy mươi hai chỉ là phép xấp xỉ, nhưng đủ chính xác để bạn '
         'tự kiểm tra những lời hứa quá đẹp.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Kẻ thù số 1: bỏ giữa chừng',
  'moc': True,
  'label': 'Góp 5 năm rồi dừng so với góp đủ 10 năm',
  'cap': ('BỎ GIỮA', 'CHỪNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Góp đủ 10 năm', '~549 triệu', 'vốn góp 360 triệu'),
            ('Góp 5 năm rồi để yên 5 năm', '~324 triệu', 'vốn góp 180 triệu'),
            ('Chênh lệch', '~225 triệu', '5 năm kỷ luật còn lại')],
  'anh': 'quit stop sign',
  'say': 'Kẻ thù thứ nhất của lãi kép là bỏ giữa chừng. Giả sử hai người cùng bắt đầu, cùng góp ba triệu mỗi tháng, cùng mức sinh lời giả định tám phần trăm. Người thứ '
         'nhất góp đủ mười năm, được khoảng năm trăm bốn mươi chín triệu. Người thứ hai góp năm năm rồi dừng, nhưng vẫn để nguyên tiền thêm năm năm cho lãi tiếp tục '
         'chạy. Kết quả khoảng ba trăm hai mươi bốn triệu. Chênh lệch khoảng hai trăm hai mươi lăm triệu đồng, trong khi số tiền người thứ nhất góp thêm chỉ là một trăm '
         'tám mươi triệu. Nghĩa là năm năm kỷ luật còn lại không chỉ cộng thêm một trăm tám mươi triệu vốn mà còn sinh ra thêm khoảng bốn mươi lăm triệu tiền lãi so với '
         'số vốn đó. Phần lớn những người dừng giữa chừng không dừng vì hết tiền, mà vì thị trường giảm, họ hoảng, hoặc nghe một cách làm mới nghe có vẻ nhanh hơn rồi '
         'đổi ý.'},
 {'k': 'cards',
  'ch': 'Chương 6 – Kẻ thù số 2: bắt đầu muộn',
  'moc': True,
  'label': 'Cùng góp 3 triệu/tháng, khác ở điểm xuất phát',
  'cap': ('BẮT ĐẦU', 'SỚM HƠN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Góp 10 năm', '~549 triệu', 'vốn góp 360 triệu'),
            ('Góp 15 năm', '~1.038 triệu', 'vốn góp 540 triệu'),
            ('Chênh lệch', '~489 triệu', 'chỉ thêm 180 triệu vốn')],
  'anh': 'sunrise early start',
  'say': 'Kẻ thù thứ hai là bắt đầu muộn. Hãy so sánh góp mười năm với góp mười lăm năm, cùng ba triệu mỗi tháng, cùng mức sinh lời giả định. Góp mười năm được khoảng '
         'năm trăm bốn mươi chín triệu. Góp mười lăm năm được khoảng một nghìn không trăm ba mươi tám triệu. Vốn bạn phải bỏ thêm chỉ là một trăm tám mươi triệu, nhưng '
         'giá trị cuối kỳ hơn nhau gần bốn trăm chín mươi triệu. Đó là phần thưởng của thời gian, thứ không thể mua bù bằng cách góp nhiều hơn về sau. Nhiều người nói '
         'đợi có thêm tiền rồi mới bắt đầu, nhưng ví dụ này cho thấy bắt đầu với số tiền nhỏ ngay hôm nay thường tốt hơn bắt đầu với số tiền lớn sau vài năm. Tất nhiên '
         'điều đó chỉ đúng khi bạn đã có quỹ dự phòng và không dùng tiền cần chi tiêu trong mười hai tháng tới để đầu tư.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Kẻ thù số 3 và những điều ví dụ không nói',
  'moc': True,
  'label': 'Sự thật khó chịu về lãi kép trong đời thực',
  'cap': ('LƯU Ý',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lợi suất thật không đều: có năm âm', (239, 68, 68)),
            ('Thị trường giảm 30% cần tăng 43% để hòa vốn', (239, 68, 68)),
            ('Phí, thuế và lạm phát làm lợi suất thật thấp hơn', (239, 68, 68)),
            ('Rút tiền sớm phá vỡ đường cong', (239, 68, 68)),
            ('Giữ nguyên quy tắc góp đều là phần bạn kiểm soát được', (34, 197, 94))],
  'anh': 'rollercoaster volatility',
  'say': 'Kẻ thù thứ ba là sự thật khó chịu mà ví dụ lý tưởng không nói: lợi suất thật không đều. Thị trường có năm giảm ba mươi phần trăm, và sau một năm giảm ba mươi '
         'phần trăm cần tăng khoảng bốn mươi ba phần trăm mới trở về hòa vốn. Ngoài ra phí giao dịch, thuế và lạm phát luôn làm lợi suất thực tế thấp hơn con số ghi '
         'trên giấy. Vì thế đừng dùng con số tám phần trăm mỗi năm làm kế hoạch chắc chắn. Hãy dùng nó như thước đo, rồi thử thêm kịch bản năm phần trăm để xem kế hoạch '
         'của mình có còn chịu được không. Với năm phần trăm mỗi năm, góp ba triệu trong mười năm vẫn ra khoảng bốn trăm sáu mươi sáu triệu, tức là vẫn hơn vốn góp đáng '
         'kể. Điều bạn kiểm soát được không phải mức sinh lời, mà là số tiền góp, thời gian góp và việc có bỏ cuộc hay không. Chỉ riêng ba thứ đó đã quyết định phần lớn '
         'kết quả.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Kế hoạch tích sản kỷ luật cho người mới',
  'moc': True,
  'label': 'Bốn bước đơn giản',
  'cap': ('4 BƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Bước 1: quỹ dự phòng 3–6 tháng chi tiêu trước', (255, 196, 0)),
            ('Bước 2: chọn số tiền góp nhỏ, đều, tự động hằng tháng', (255, 196, 0)),
            ('Bước 3: viết sẵn quy tắc không bán khi thị trường giảm', (255, 196, 0)),
            ('Bước 4: xem lại mỗi quý, không xem mỗi ngày', (255, 196, 0)),
            ('Máy tính tích sản và bảng số thật: chungkhoanhuynguyen.com', (56, 189, 248))],
  'anh': 'monthly planner calendar',
  'say': 'Cuối cùng, một kế hoạch tích sản kỷ luật có bốn bước. Một, có quỹ dự phòng ba đến sáu tháng chi tiêu trước khi đầu tư, để không bị buộc bán ở đáy. Hai, chọn '
         'số tiền nhỏ, đều, tự động mỗi tháng, đủ nhỏ để bạn không bỏ cuộc. Ba, viết sẵn quy tắc không bán vì hoảng khi thị trường giảm, vì lúc giảm là lúc bạn mua được '
         'nhiều đơn vị hơn với cùng số tiền. Bốn, xem lại mỗi quý thay vì mỗi ngày. Bạn có thể thử tính với số tiền của riêng mình bằng máy tính tích sản, và đối chiếu '
         'với bảng tích sản cổ phiếu ngân hàng bằng số liệu thật tại chứng khoán Huy Nguyễn chấm com. Hãy nhớ kết quả trong quá khứ không phải cam kết lợi nhuận trong '
         'tương lai, và nội dung này chỉ chia sẻ kiến thức, không phải khuyến nghị mua bán.'},
 {'k': 'end',
  'label': '',
  'cap': ('PHƯƠNG PHÁP TỐT', 'ĐỪNG BỎ CUỘC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, lãi kép không phải phép màu, nó là phần thưởng cho sự kiên nhẫn. Phương pháp không sợ sai, chỉ sợ theo giữa chừng rồi đổi ý. Cảm ơn bạn đã xem, hẹn '
         'gặp bạn ở video tiếp theo.'}]

S['CH1311C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – hình nền minh họa',
  'cap': ('MẤT 43% TRONG', '10 THÁNG?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, 'Tuần 2/11/26: 1.741', 2.6]]},
  'anh': 'vietnam stock market crash 2022',
  'say': 'Ngày mười tháng một năm hai nghìn không trăm hai mươi hai, VN-Index đóng cửa ở khoảng một nghìn năm trăm hai mươi chín điểm, mức cao nhất lịch sử vào thời '
         'điểm đó. Chỉ khoảng mười tháng sau, ngày mười lăm tháng mười một, chỉ số này chạm khoảng tám trăm bảy mươi bốn điểm, tức là mất gần bốn mươi ba phần trăm giá '
         'trị. Mấy tháng trước đó, hầu như ai bước vào thị trường cũng có lãi, và có người tin rằng chứng khoán chỉ biết đi lên. Vậy chuyện gì đã xảy ra, và vì sao một '
         'thị trường đang cực kỳ thuận lợi lại đảo chiều nhanh đến thế? Trong video này mình kể lại giai đoạn hai nghìn không trăm hai mươi mốt đến hai nghìn không trăm '
         'hai mươi hai theo bốn bước: cơn sốt đi lên, những cú hích làm đảo chiều, cách đòn bẩy biến một đợt giảm thành cơn hoảng loạn, và những bài học còn nguyên giá '
         'trị sau mười năm nữa. Xem hết, bạn sẽ biết dấu hiệu nào đáng cảnh giác khi ai cũng thấy dễ kiếm tiền. Các mốc điểm số là số làm tròn theo thông tin công khai. '
         'Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Những mốc cần nhớ',
  'moc': True,
  'label': 'VN-Index các mốc (điểm, số làm tròn)',
  'cap': ('6 MỐC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Đáy 3/2020', 659.0, (56, 189, 248), '659'),
           ('Cuối 2020', 1104.0, (56, 189, 248), '1.104'),
           ('Cuối 2021', 1498.0, (34, 197, 94), '1.498'),
           ('Đỉnh 1/2022', 1529.0, (255, 196, 0), '1.529'),
           ('Đáy 11/2022', 874.0, (239, 68, 68), '874'),
           ('Cuối 2022', 1007.0, (239, 68, 68), '1.007')],
  'anh': 'stock chart history',
  'say': 'Hãy bắt đầu bằng sáu mốc. Tháng ba năm hai nghìn không trăm hai mươi, khi đại dịch bùng phát, VN-Index chạm đáy khoảng sáu trăm năm mươi chín điểm. Cuối năm '
         'hai nghìn không trăm hai mươi chỉ số ở khoảng một nghìn một trăm linh bốn điểm. Cuối năm hai nghìn không trăm hai mươi mốt khoảng một nghìn bốn trăm chín mươi '
         'tám điểm, tăng gần ba mươi sáu phần trăm trong năm. Đỉnh vào ngày mười tháng một năm hai nghìn không trăm hai mươi hai khoảng một nghìn năm trăm hai mươi chín '
         'điểm. Đáy vào ngày mười lăm tháng mười một năm hai nghìn không trăm hai mươi hai khoảng tám trăm bảy mươi bốn điểm. Và cuối năm hai nghìn không trăm hai mươi '
         'hai chỉ số đóng cửa khoảng một nghìn không trăm linh bảy điểm, nghĩa là cả năm giảm gần ba mươi ba phần trăm. Tính từ đáy năm hai nghìn không trăm hai mươi '
         'đến đỉnh năm hai nghìn không trăm hai mươi hai, chỉ số tăng hơn gấp đôi, khoảng một trăm ba mươi hai phần trăm, trong chưa đầy hai năm. Tính từ đỉnh đến đáy '
         'hai nghìn không trăm hai mươi hai, mất khoảng bốn mươi ba phần trăm. Hai chuyển động cực đoan này chỉ cách nhau chừng mười tháng, và đó chính là lý do giai '
         'đoạn này đáng học nhất với người đầu tư hiện nay.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Cơn sốt đi lên: vì sao ai cũng thấy dễ',
  'moc': True,
  'label': 'Các lực đẩy giai đoạn 2020–2021',
  'cap': ('CƠN SỐT',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lãi suất thấp, tiền rẻ, gửi tiết kiệm lãi ít', (56, 189, 248)),
            ('Hơn 1,5 triệu tài khoản mới trong năm 2021 (theo VSD)', (56, 189, 248)),
            ('Giao dịch online, vay ký quỹ (margin) dễ dàng', (56, 189, 248)),
            ('Mạng xã hội lan truyền câu chuyện ai vào cũng lãi', (255, 196, 0)),
            ('Nhiều người lần đầu vào thị trường, chưa từng gặp chu kỳ giảm', (239, 68, 68))],
  'anh': 'crowd investors screen',
  'say': 'Vì sao giai đoạn này giống một cơn sốt? Thứ nhất, lãi suất thấp và tiền rẻ, gửi tiết kiệm cho lãi ít nên nhiều người tìm kênh khác. Thứ hai, theo Trung tâm '
         'Lưu ký Chứng khoán Việt Nam, năm hai nghìn không trăm hai mươi mốt có hơn một phẩy năm triệu tài khoản chứng khoán mở mới, mức kỷ lục tại thời điểm đó. Thứ '
         'ba, giao dịch trực tuyến và vay ký quỹ trở nên cực kỳ dễ, chỉ vài thao tác trên điện thoại. Thứ tư, mạng xã hội lan truyền câu chuyện ai vào cũng lãi. Điều '
         'nguy hiểm nhất là yếu tố cuối: rất nhiều người lần đầu bước vào thị trường đúng thời điểm chỉ số chỉ biết đi lên, nên họ mặc định đó là bình thường. Khi tất '
         'cả bằng chứng bạn từng thấy đều là lãi, bạn rất khó tưởng tượng một đợt giảm bốn mươi phần trăm, và bạn cũng không chuẩn bị gì cho nó.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Những cú hích làm đảo chiều năm 2022',
  'moc': True,
  'label': 'Các lực kéo xuống, theo thông tin công khai',
  'cap': ('CÚ HÍCH',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Fed tăng lãi suất từ gần 0% lên 4,25–4,50% trong năm 2022', (239, 68, 68)),
            ('Lãi suất trong nước tăng, tiền rẻ không còn', (239, 68, 68)),
            ('Thị trường trái phiếu doanh nghiệp bất động sản căng thẳng', (239, 68, 68)),
            ('Niềm tin suy giảm, thanh khoản thu hẹp', (239, 68, 68)),
            ('Bán giải chấp (margin call) khuếch đại đợt giảm', (239, 68, 68))],
  'anh': 'interest rate hike',
  'say': 'Vậy điều gì đảo chiều thị trường? Không có một nguyên nhân duy nhất, mà là nhiều lực cùng lúc. Một là Cục Dự trữ Liên bang Mỹ tăng lãi suất rất nhanh, từ gần '
         'không phần trăm đầu năm hai nghìn không trăm hai mươi hai lên mức bốn phẩy hai mươi lăm đến bốn phẩy năm mươi phần trăm vào cuối năm, và dòng tiền toàn cầu '
         'chảy ngược khỏi các thị trường mới nổi. Hai là lãi suất trong nước cũng tăng, có ngân hàng niêm yết lãi huy động kỳ hạn mười hai tháng trên chín phần trăm mỗi '
         'năm, nên gửi tiết kiệm lại hấp dẫn trở lại. Ba là thị trường trái phiếu doanh nghiệp, đặc biệt nhóm bất động sản, bắt đầu căng thẳng sau những vụ việc cuối '
         'quý một và quý bốn năm hai nghìn không trăm hai mươi hai. Bốn là niềm tin suy giảm khiến thanh khoản thu hẹp. Mình không nêu từng vụ việc cụ thể, vì điều quan '
         'trọng với nhà đầu tư là cơ chế: khi tiền rẻ biến mất và niềm tin bị lung lay, thị trường định giá lại rất nhanh.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Đòn bẩy biến giảm thành hoảng loạn',
  'moc': True,
  'label': 'Cơ chế bán giải chấp, ví dụ giả định',
  'cap': ('ĐÒN BẨY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Có 100 triệu, vay thêm 100', 'tài sản 200 triệu', 'tỷ lệ vay 50%'),
            ('Giá giảm 25%', 'tài sản còn 150', 'vẫn nợ 100'),
            ('Vốn thật của bạn', 'chỉ còn 50 triệu', 'mất 50% vốn')],
  'anh': 'margin call warning',
  'say': 'Đòn bẩy là chất xúc tác biến một đợt giảm thành cơn hoảng loạn. Hãy xem ví dụ giả định. Bạn có một trăm triệu đồng và vay thêm một trăm triệu để mua cổ phiếu, '
         'tổng tài sản là hai trăm triệu. Nếu giá giảm hai mươi lăm phần trăm, tài sản chỉ còn một trăm năm mươi triệu, nhưng bạn vẫn nợ một trăm triệu. Vốn thật của '
         'bạn còn năm mươi triệu, tức mất năm mươi phần trăm. Khi tài sản giảm tới ngưỡng công ty chứng khoán quy định, họ buộc phải bán cổ phiếu của bạn để thu hồi nợ, '
         'bất kể giá lúc đó là bao nhiêu. Hàng nghìn tài khoản cùng bị bán giải chấp trong một ngày khiến giá giảm thêm, rồi lại kích hoạt thêm những lệnh bán giải chấp '
         'khác. Vòng xoáy đó giải thích vì sao có những phiên thị trường giảm thẳng đứng chẳng cần thêm tin xấu nào. Người không dùng đòn bẩy có thể chờ, người dùng đòn '
         'bẩy thì không có quyền chờ.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Toán học của việc hồi phục',
  'moc': True,
  'label': 'Muốn về lại đỉnh cần tăng bao nhiêu',
  'cap': ('HÒA VỐN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Giảm 43%', 'cần tăng ~75%', 'để về đỉnh cũ'),
            ('Từ đáy tháng 11/2022', '+15%', 'đến cuối năm 2022 (~1.007)'),
            ('Đến cuối năm 2023', '~1.130', 'tăng ~29% so với đáy')],
  'anh': 'recovery climb mountain',
  'say': 'Có một bài học toán học rất tàn nhẫn: giảm bốn mươi ba phần trăm cần tăng khoảng bảy mươi lăm phần trăm mới về lại điểm xuất phát. Với VN-Index, từ đáy khoảng '
         'tám trăm bảy mươi bốn điểm muốn quay về đỉnh một nghìn năm trăm hai mươi chín điểm cần tăng hơn bảy mươi bốn phần trăm, và chuyện đó tất nhiên không thể xảy '
         'ra trong một vài tháng. Thực tế, từ đáy tháng mười một năm hai nghìn không trăm hai mươi hai đến cuối năm chỉ số hồi khoảng mười lăm phần trăm lên một nghìn '
         'không trăm linh bảy điểm, và đến cuối năm hai nghìn không trăm hai mươi ba khoảng một nghìn một trăm ba mươi điểm, tức hồi khoảng hai mươi chín phần trăm so '
         'với đáy. Nghĩa là những người mua gần đỉnh tháng một năm hai nghìn không trăm hai mươi hai phải chờ rất lâu mới hòa vốn, nếu họ đủ kiên nhẫn chờ. Còn những '
         'người dùng đòn bẩy và bị bán giải chấp gần đáy thì không còn cơ hội chờ. Đó là lý do mình luôn nhấn mạnh quản trị rủi ro, hơn cả việc chọn đúng cổ phiếu.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Dấu hiệu cảnh giác khi thị trường quá hưng phấn',
  'moc': True,
  'label': 'Những dấu hiệu lặp lại qua các chu kỳ',
  'cap': ('DẤU HIỆU',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Ai quanh bạn cũng nói về cổ phiếu, kể cả người chưa từng đầu tư', (239, 68, 68)),
            ('Mua đuổi vì sợ lỡ, không còn hỏi giá trị thật', (239, 68, 68)),
            ('Mức vay ký quỹ tăng nhanh cùng lúc giá tăng', (239, 68, 68)),
            ('Tin xấu bị coi nhẹ, tin tốt bị thổi phồng', (239, 68, 68)),
            ('Bạn bắt đầu tính chuyện vay để mua thêm', (239, 68, 68))],
  'anh': 'fireworks bubble',
  'say': 'Vậy có dấu hiệu nào giúp nhận ra giai đoạn quá hưng phấn không? Không có công thức báo trước ngày đảo chiều, nhưng có những dấu hiệu lặp lại qua các chu kỳ. '
         'Một, người quanh bạn, kể cả người chưa từng đầu tư, đều nói về cổ phiếu và khoe lãi. Hai, bạn và mọi người mua đuổi vì sợ lỡ, không còn hỏi giá trị thật của '
         'doanh nghiệp. Ba, mức vay ký quỹ tăng nhanh cùng lúc với giá. Bốn, tin xấu bị coi nhẹ, trong khi tin tốt bị thổi phồng. Năm, chính bạn bắt đầu tính chuyện vay '
         'thêm để mua thêm. Khi bạn thấy từ ba dấu hiệu trở lên, đó chưa phải lúc bán sạch, nhưng là lúc nên kiểm tra tỷ trọng đòn bẩy, giữ tiền mặt dự phòng và nhìn '
         'lại lý do mình đang nắm giữ từng cổ phiếu.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Kế hoạch phòng thủ cho người đầu tư',
  'moc': True,
  'label': 'Việc bạn làm được trước khi cơn giảm tới',
  'cap': ('PHÒNG THỦ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Không vay quá mức bạn chịu được khi giá giảm 40%', (255, 196, 0)),
            ('Giữ tiền mặt hoặc tài sản an toàn theo kế hoạch', (255, 196, 0)),
            ('Chia nhỏ vốn, góp đều thay vì dồn một lần', (255, 196, 0)),
            ('Có sẵn tiêu chí mua, bán và tỷ trọng tối đa mỗi mã', (255, 196, 0)),
            ('Chỉ đầu tư tiền nhàn rỗi, không dùng tiền sinh hoạt', (255, 196, 0))],
  'anh': 'umbrella protection storm',
  'say': 'Phần quan trọng nhất là chuẩn bị. Một, không vay nhiều hơn mức bạn còn chịu được khi giá giảm bốn mươi phần trăm. Ví dụ giả định ở trên cho thấy chỉ cần giảm '
         'hai mươi lăm phần trăm đã mất nửa vốn. Hai, giữ tiền mặt hoặc tài sản an toàn theo kế hoạch, để có thứ mà mua khi thị trường rẻ chứ không phải bán khi thị '
         'trường rẻ. Ba, chia nhỏ vốn và góp đều thay vì dồn tất cả một lần ở vùng giá cao. Bốn, có sẵn tiêu chí mua, bán và tỷ trọng tối đa cho mỗi mã, viết ra giấy từ '
         'lúc bình tĩnh. Năm, chỉ dùng tiền nhàn rỗi, không dùng tiền sinh hoạt hay tiền đã hứa cho việc khác. Không điều nào trong đây giúp bạn dự đoán thị trường, '
         'nhưng tất cả giúp bạn còn đứng trong cuộc chơi khi thị trường quay đầu.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Ba câu để nhớ',
  'cap': ('3 BÀI HỌC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Thị trường tăng làm người ta quên rủi ro, giảm làm người ta quên giá trị', (255, 255, 255)),
            ('Đòn bẩy lấy đi quyền được chờ của bạn', (239, 68, 68)),
            ('Sống sót qua đợt giảm quan trọng hơn thắng nhanh trong đợt tăng', (34, 197, 94)),
            ('Tài liệu số liệu và công cụ miễn phí: chungkhoanhuynguyen.com', (56, 189, 248))],
  'anh': 'old book wisdom library',
  'say': 'Nếu chỉ được mang theo ba câu từ giai đoạn này, mình chọn ba câu sau. Thứ nhất: thị trường tăng làm người ta quên rủi ro, thị trường giảm làm người ta quên '
         'giá trị. Thứ hai: đòn bẩy lấy đi quyền được chờ của bạn. Thứ ba: sống sót qua đợt giảm quan trọng hơn thắng nhanh trong đợt tăng. Nếu bạn còn trong thị trường '
         'sau mỗi chu kỳ, thời gian và lãi kép sẽ làm phần còn lại. Số liệu các mốc và biểu đồ chỉ số, cùng bảng báo cáo tài chính và công cụ phân tích miễn phí, bạn có '
         'thể xem tại chứng khoán Huy Nguyễn chấm com. Nội dung chia sẻ kiến thức lịch sử, không phải dự báo hay khuyến nghị mua bán chứng khoán.'},
 {'k': 'end',
  'label': '',
  'cap': ('SỐNG SÓT', 'TRƯỚC KHI THẮNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Cảm ơn bạn đã xem. Lịch sử không lặp lại y nguyên, nhưng con người thì lặp lại cách phản ứng. Hẹn gặp bạn ở video tiếp theo trong seri Bài học lịch sử.'}]

S['CH1411A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'TCB – Đọc BCTC 5 phút',
  'cap': ('LÃI +23,7% NHỜ', 'TRÍCH LẬP ÍT HƠN?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'TCBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[10, 24.94, 'Đỉnh tuần 12/1/26: 24,94', 0.6], [21, 18.51, 'Đáy tuần 6/4/26: 18,51', 1.6], [51, 21.95, 'Tuần 2/11/26: 21,95', 2.6]]},
  'anh': 'bank tower vietnam',
  'say': 'Quý ba năm hai nghìn không trăm hai mươi sáu, Ngân hàng Kỹ Thương, mã TCB, báo lãi sau thuế bảy nghìn chín trăm bốn mươi ba tỷ đồng, tăng hai mươi ba phẩy bảy '
         'phần trăm so với cùng kỳ. Một con số rất đẹp. Nhưng thu nhập lãi thuần, động cơ chính của ngân hàng, chỉ tăng mười bảy phẩy chín phần trăm. Vậy phần lợi nhuận '
         'tăng nhanh hơn thu nhập đến từ đâu? Trong báo cáo có hai dòng đáng chú ý: lãi từ dịch vụ tăng tới năm mươi chín phẩy năm phần trăm, và chi phí dự phòng lại '
         'giảm ba mươi tám phẩy tám phần trăm. Chi phí dự phòng giảm thì lợi nhuận được cộng điểm, nhưng cũng là lúc tỷ lệ nợ xấu nhích từ một phẩy không tám phần trăm '
         'lên một phẩy hai mươi bảy phần trăm. Trong video này mình đọc báo cáo của TCB theo khung năm bước giống video ACB trước đó, và đặt hai ngân hàng cạnh nhau để '
         'bạn thấy cùng một con số lợi nhuận có thể có chất lượng rất khác nhau. Xem hết, bạn sẽ biết cách tách phần lợi nhuận đến từ kinh doanh với phần đến từ trích '
         'lập. Số liệu là ví dụ tại ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Bước 1: Lợi nhuận sau thuế qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ TCB theo quý (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 6419.0, (56, 189, 248), '6.419'),
           ('Q4/25', 6676.0, (56, 189, 248), '6.676'),
           ('Q1/26', 6671.0, (56, 189, 248), '6.671'),
           ('Q2/26', 7350.0, (56, 189, 248), '7.350'),
           ('Q3/26', 7943.0, (34, 197, 94), '7.943')],
  'anh': 'financial report charts',
  'say': 'Bước một là nhìn lợi nhuận qua nhiều quý. TCB quý ba năm hai nghìn không trăm hai mươi sáu lãi bảy nghìn chín trăm bốn mươi ba tỷ đồng, so với sáu nghìn bốn '
         'trăm mười chín tỷ cùng kỳ năm trước, tăng hai mươi ba phẩy bảy phần trăm. Lũy kế chín tháng đạt hai mươi mốt nghìn chín trăm sáu mươi bốn tỷ, tăng mười tám '
         'phẩy không phần trăm. Điều đáng chú ý trên biểu đồ là đường đi rất đều: sáu nghìn bốn trăm mười chín, sáu nghìn sáu trăm bảy mươi sáu, sáu nghìn sáu trăm bảy '
         'mươi mốt, bảy nghìn ba trăm năm mươi rồi bảy nghìn chín trăm bốn mươi ba tỷ. Không có quý nào lõm xuống, mỗi quý gần như cao hơn quý trước. Với ngân hàng, một '
         'chuỗi tăng đều như vậy là dấu hiệu tốt, vì nó cho thấy lợi nhuận không phụ thuộc vào một khoản thu bất thường nào của một quý. Nhưng đều đặn chưa đủ, ta còn '
         'phải xem phần tăng đó đến từ đâu, và đó là bước hai.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Bước 2: Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần TCB theo quý (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 9925.0, (56, 189, 248), '9.925'),
           ('Q4/25', 10788.0, (56, 189, 248), '10.788'),
           ('Q1/26', 9522.0, (56, 189, 248), '9.522'),
           ('Q2/26', 10763.0, (56, 189, 248), '10.763'),
           ('Q3/26', 11700.0, (34, 197, 94), '11.700')],
  'anh': 'bank loans interest',
  'say': 'Bước hai là thu nhập lãi thuần, chênh lệch giữa tiền lãi thu được và tiền lãi phải trả. Quý ba năm hai nghìn không trăm hai mươi sáu TCB đạt mười một nghìn '
         'bảy trăm tỷ đồng, tăng mười bảy phẩy chín phần trăm so với chín nghìn chín trăm hai mươi lăm tỷ cùng kỳ, và là mức cao nhất trong năm quý. Để ý quý một năm '
         'hai nghìn không trăm hai mươi sáu có một nhịp giảm xuống chín nghìn năm trăm hai mươi hai tỷ, tức là thu nhập lãi cũng có biến động theo mùa, không phải luôn '
         'tăng. Bây giờ đặt hai con số cạnh nhau: thu nhập lãi thuần tăng mười bảy phẩy chín phần trăm còn lợi nhuận tăng hai mươi ba phẩy bảy phần trăm. Lợi nhuận tăng '
         'nhanh hơn thu nhập lõi khoảng năm phẩy tám điểm phần trăm. Phần dư ra này có nghĩa là các dòng khác trong báo cáo đã đóng góp thêm hoặc chi phí đã bớt đi. Hai '
         'dòng ấy là lãi dịch vụ và chi phí dự phòng.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Bước 3: Ba nguồn tăng trưởng',
  'moc': True,
  'label': 'Tăng trưởng so với cùng kỳ quý 3/2026',
  'cap': ('3 NGUỒN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Thu nhập lãi thuần', '+17,9%', '11.700 tỷ'), ('Lãi dịch vụ', '+59,5%', '3.615 tỷ'), ('Chi phí dự phòng', '-38,8%', 'trích lập ít hơn')],
  'anh': 'three pillars building',
  'say': 'Ba con số trên màn hình kể gần hết câu chuyện. Thu nhập lãi thuần tăng mười bảy phẩy chín phần trăm, đây là phần nền tảng. Lãi từ dịch vụ tăng năm mươi chín '
         'phẩy năm phần trăm lên ba nghìn sáu trăm mười lăm tỷ đồng, một mức tăng rất mạnh, cho thấy ngân hàng không chỉ sống bằng chênh lệch lãi suất mà còn có nguồn '
         'thu từ phí, bảo hiểm, thanh toán và các dịch vụ khác. Nguồn thu từ phí thường được xem là chất lượng cao vì ít chịu tác động trực tiếp của rủi ro tín dụng. '
         'Con số thứ ba là chi phí dự phòng giảm ba mươi tám phẩy tám phần trăm. Đây là chi phí, nên khi giảm thì lợi nhuận tăng, nhưng khác với hai nguồn đầu, nó không '
         'phải là hoạt động kinh doanh mới mà là quyết định trích lập ít hơn. Cùng là lợi nhuận tăng, nhưng bạn nên tách phần tăng nhờ kinh doanh với phần tăng nhờ '
         'trích lập.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Bước 4: Nợ xấu và bao phủ',
  'moc': True,
  'label': 'Chất lượng tài sản TCB quý 3/2026',
  'cap': ('NỢ XẤU', 'VÀ BAO PHỦ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Tỷ lệ nợ xấu', '1,27%', 'quý trước 1,08%'), ('Mức tăng', '+0,19 điểm', 'trong một quý'), ('Bao phủ nợ xấu', 'khoảng 107%', 'dự phòng / nợ xấu')],
  'anh': 'bank risk loans',
  'say': 'Bước bốn là nợ xấu và bao phủ nợ xấu. Tỷ lệ nợ xấu của TCB quý ba là một phẩy hai mươi bảy phần trăm, tăng từ một phẩy không tám phần trăm của quý trước, tức '
         'nhích thêm khoảng không phẩy mười chín điểm phần trăm. Mức này vẫn thấp, nhưng xu hướng là đi lên. Bao phủ nợ xấu khoảng một trăm linh bảy phần trăm, nghĩa là '
         'cứ một trăm đồng nợ xấu thì ngân hàng đã dự phòng khoảng một trăm linh bảy đồng, nhiều hơn số nợ xấu hiện có. Đây là điểm tựa an toàn. Tuy nhiên bạn hãy nhìn '
         'sự ngược chiều: nợ xấu tăng nhưng chi phí dự phòng giảm ba mươi tám phẩy tám phần trăm. Điều đó có thể hợp lý nếu ngân hàng đã trích lập dày từ những quý '
         'trước và có tài sản đảm bảo tốt, nhưng cũng đáng để theo dõi: nếu nợ xấu tiếp tục tăng ở quý sau, chi phí dự phòng sẽ phải tăng trở lại và lợi nhuận sẽ chịu '
         'áp lực.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Đặt hai ngân hàng cạnh nhau',
  'moc': True,
  'label': 'TCB và ACB, quý 3/2026, so với cùng kỳ',
  'cap': ('TCB VS ACB',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Lợi nhuận sau thuế', 'TCB +23,7%', 'ACB +9,8%'),
            ('Chi phí dự phòng', 'TCB -38,8%', 'ACB +223,2%'),
            ('Nợ xấu / bao phủ', 'TCB 1,27% / 107%', 'ACB 1,19% / 91%')],
  'anh': 'comparison two sides',
  'say': 'Giờ đặt TCB cạnh ACB, ngân hàng ở video trước. Lợi nhuận quý ba: TCB tăng hai mươi ba phẩy bảy phần trăm, ACB tăng chín phẩy tám phần trăm. Nhìn riêng điểm '
         'này, TCB hơn hẳn. Nhưng nhìn chi phí dự phòng, TCB giảm ba mươi tám phẩy tám phần trăm còn ACB tăng hai trăm hai mươi ba phẩy hai phần trăm. Hai ngân hàng đi '
         'theo hai chiến lược trích lập rất khác nhau trong cùng một quý. Nợ xấu của TCB là một phẩy hai mươi bảy phần trăm với bao phủ một trăm linh bảy phần trăm, nợ '
         'xấu của ACB là một phẩy mười chín phần trăm với bao phủ chín mươi mốt phần trăm. Nghĩa là ACB trích dự phòng mạnh dù nợ xấu thấp hơn, còn TCB trích ít hơn '
         'nhưng bộ đệm hiện còn dày hơn. Mình không kết luận bên nào tốt hơn, vì chỉ một quý thì chưa đủ. Điểm cần nhớ là cùng một con số lợi nhuận tăng trưởng có thể '
         'được tạo ra bằng những cách rất khác nhau, và bạn chỉ thấy điều này khi đọc xuống tới dòng chi phí dự phòng.'},
 {'k': 'cards',
  'ch': 'Chương 6 – Bước 5: Hiệu quả và định giá',
  'moc': True,
  'label': 'Chỉ số TCB tại ngày 5/11/2026',
  'cap': ('ROE VÀ', 'ĐỊNH GIÁ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE 4 quý', '15,4%', 'ROA 2,3%'), ('P/E', '8,11 lần', 'giá / lợi nhuận mỗi cổ phiếu'), ('P/B', '1,24 lần', 'giá / giá trị sổ sách')],
  'anh': 'stock valuation calculator',
  'say': 'Bước năm là hiệu quả và định giá. ROE bốn quý gần nhất của TCB khoảng mười lăm phẩy bốn phần trăm và ROA khoảng hai phẩy ba phần trăm, mức ROA này thuộc nhóm '
         'cao trong ngành, cho thấy hiệu quả sử dụng tài sản tốt. P/E là tám phẩy mười một lần, P/B là một phẩy hai mươi bốn lần. Nếu so với ACB có P/E bảy phẩy ba mươi '
         'chín lần và P/B một phẩy mười bốn lần, TCB đắt hơn một chút trên cả hai thước đo. Điều này có hợp lý không? Câu trả lời phụ thuộc vào chất lượng lợi nhuận và '
         'khả năng duy trì tăng trưởng. Một ngân hàng có lãi dịch vụ tăng mạnh và ROA cao có thể xứng mức định giá cao hơn, nhưng nếu lợi nhuận phụ thuộc nhiều vào việc '
         'trích lập ít đi thì mức giá đó cần được kiểm chứng ở các quý tới. Định giá là câu hỏi về tương lai, còn báo cáo chỉ cung cấp dữ liệu quá khứ để bạn đặt câu '
         'hỏi cho đúng.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Ba câu hỏi về chất lượng lợi nhuận',
  'moc': True,
  'label': 'Hỏi trước khi kết luận',
  'cap': ('3 CÂU HỎI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lợi nhuận tăng nhờ doanh thu hay nhờ chi phí giảm?', (255, 196, 0)),
            ('Phần tăng có lặp lại được ở quý sau không?', (255, 196, 0)),
            ('Rủi ro nào chưa hiện trong báo cáo, như nợ xấu nhích lên?', (255, 196, 0)),
            ('Trích lập ít đi: do nợ xấu giảm hay do chọn trích ít?', (239, 68, 68)),
            ('Luôn so cả chuỗi 5 quý, không chỉ 1 quý', (34, 197, 94))],
  'anh': 'magnifier question mark',
  'say': 'Từ hai video về ACB và TCB, mình rút ra ba câu hỏi về chất lượng lợi nhuận. Một: lợi nhuận tăng nhờ doanh thu tăng hay nhờ chi phí giảm? Doanh thu tăng như '
         'thu nhập lãi và lãi dịch vụ thường bền hơn. Hai: phần tăng đó có lặp lại được ở quý sau không? Một khoản trích lập giảm trong một quý chưa chắc lặp lại. Ba: '
         'rủi ro nào chưa hiện trong báo cáo? Ví dụ nợ xấu nhích lên nhưng chi phí dự phòng giảm, bạn cần hiểu vì sao hai điều này đi ngược chiều. Trích lập ít đi có '
         'thể do ngân hàng đã trích dày từ trước, nhưng cũng có thể đơn giản là họ chọn trích ít trong quý đó. Hãy luôn so cả chuỗi năm quý, và ghi ra điều cần theo dõi '
         'ở quý sau, thay vì ghép ngay một kết luận từ một quý duy nhất.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài tập tự làm và tài liệu đi kèm',
  'moc': True,
  'label': 'Làm thử với ngân hàng bạn quan tâm',
  'cap': ('BÀI TẬP', 'TỰ LÀM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lấy lợi nhuận và thu nhập lãi thuần 5 quý', (255, 196, 0)),
            ('Tính chênh lệch tốc độ tăng của hai dòng này', (255, 196, 0)),
            ('Tìm chi phí dự phòng, nợ xấu, bao phủ để giải thích', (255, 196, 0)),
            ('Viết 2 điều cần theo dõi ở quý sau', (255, 196, 0)),
            ('Bảng số 400 mã: chungkhoanhuynguyen.com', (56, 189, 248))],
  'anh': 'student notebook homework',
  'say': 'Bài tập cho bạn: chọn một ngân hàng, lấy lợi nhuận và thu nhập lãi thuần của năm quý gần nhất. Tính chênh lệch tốc độ tăng của hai dòng này. Nếu lợi nhuận '
         'tăng nhanh hơn nhiều, hãy tìm xem phần chênh đến từ lãi dịch vụ hay từ chi phí dự phòng giảm. Sau đó xem nợ xấu và bao phủ nợ xấu có đi cùng chiều với chi phí '
         'dự phòng hay không, rồi viết ra hai điều cần theo dõi ở quý sau. Toàn bộ số liệu trong video này, cùng bảng báo cáo tài chính hơn bốn trăm mã, có sẵn miễn phí '
         'tại chứng khoán Huy Nguyễn chấm com, kèm bài viết đi cùng để bạn đối chiếu. Số liệu minh họa mang tính chia sẻ kiến thức, không phải khuyến nghị mua bán chứng '
         'khoán.'},
 {'k': 'end',
  'label': '',
  'cap': ('TÁCH LỢI NHUẬN', 'THEO NGUỒN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, lợi nhuận tăng hai mươi ba phẩy bảy phần trăm hay chín phẩy tám phần trăm chỉ là phần nổi. Phần chìm là thu nhập lõi, lãi dịch vụ và chi phí dự '
         'phòng. Cảm ơn bạn đã xem, hẹn gặp bạn ở video tiếp theo.'}]

S['CH1411B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – hình nền minh họa',
  'cap': ('CÙNG P/B 0,87', 'ROE GẤP ĐÔI?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, 'Tuần 2/11/26: 1.741', 2.6]]},
  'anh': 'bank stock valuation table',
  'say': 'Hai ngân hàng cùng được định giá ở mức P/B không phẩy tám mươi bảy lần, tức giá thấp hơn giá trị sổ sách mười ba phần trăm. Nhìn qua có vẻ như hai ngân hàng '
         'đang rẻ y hệt nhau. Nhưng ROE bốn quý gần nhất của một bên là mười bảy phẩy chín phần trăm, còn bên kia chỉ tám phẩy chín phần trăm, chênh nhau gấp đôi. Vậy '
         'hai con số P/B giống hệt nhau có thật sự cùng nghĩa không? Câu trả lời là không, và đây là hiểu lầm phổ biến nhất khi nhìn định giá ngân hàng: nghĩ rằng P/B '
         'càng thấp càng rẻ. Trong video này mình giải thích P/B thật sự đo cái gì, vì sao phải đọc nó cùng ROE, dùng số liệu thật của mười hai ngân hàng tại ngày năm '
         'tháng mười một năm hai nghìn không trăm hai mươi sáu, và đưa ra một khung ba câu hỏi để bạn không bị đánh lừa bởi một con số. Xem hết, bạn sẽ biết khi nào P/B '
         'thấp là cơ hội để tìm hiểu thêm, và khi nào đó chỉ là mức giá hợp lý cho khả năng sinh lời thấp. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'cards',
  'ch': 'Chương 1 – P/B đo cái gì',
  'moc': True,
  'label': 'P/B, nói đơn giản',
  'cap': ('P/B LÀ GÌ?',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Giá thị trường', '1 cổ phiếu', 'ví dụ 20.000 đồng'), ('Giá trị sổ sách', '1 cổ phiếu', 'ví dụ 17.000 đồng'), ('P/B', '20.000 / 17.000', 'khoảng 1,18 lần')],
  'anh': 'balance sheet books',
  'say': 'Trước hết, P/B là giá thị trường của một cổ phiếu chia cho giá trị sổ sách của cổ phiếu đó. Giá trị sổ sách là phần vốn chủ sở hữu chia cho số cổ phiếu đang '
         'lưu hành. Ví dụ giả định: giá thị trường hai mươi nghìn đồng, giá trị sổ sách mười bảy nghìn đồng thì P/B khoảng một phẩy mười tám lần. P/B dưới một có nghĩa '
         'giá thấp hơn sổ sách. Với ngân hàng, P/B được dùng nhiều vì tài sản chủ yếu là các khoản cho vay và chứng khoán, giá trị sổ sách khá sát bản chất hoạt động. '
         'Nhưng P/B chỉ nói cho bạn biết bạn đang trả bao nhiêu cho một đồng vốn chủ sở hữu. Nó không nói đồng vốn đó có làm ra nhiều tiền hay không. Phần trả lời câu '
         'hỏi đó thuộc về ROE, và hai con số chỉ có nghĩa khi đứng cạnh nhau.'},
 {'k': 'bars',
  'ch': 'Chương 2 – ROE là phần còn thiếu',
  'moc': True,
  'label': 'P/B và ROE của hai cặp ngân hàng (số liệu 5/11/2026)',
  'cap': ('CÙNG P/B', 'KHÁC ROE'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('TPB ROE', 17.9, (34, 197, 94), '17,9%'),
           ('BAB ROE', 8.9, (239, 68, 68), '8,9%'),
           ('KLB ROE', 22.7, (34, 197, 94), '22,7%'),
           ('PGB ROE', 9.2, (239, 68, 68), '9,2%')],
  'anh': 'two bank branches',
  'say': 'ROE là lợi nhuận bốn quý gần nhất chia cho vốn chủ sở hữu, nó cho biết mỗi một trăm đồng vốn tạo ra bao nhiêu đồng lợi nhuận. Hãy nhìn hai cặp ngân hàng. Cặp '
         'thứ nhất: TPB và BAB cùng P/B không phẩy tám mươi bảy lần. ROE của TPB là mười bảy phẩy chín phần trăm, ROE của BAB là tám phẩy chín phần trăm. Cặp thứ hai: '
         'KLB có P/B không phẩy tám mươi lần với ROE hai mươi hai phẩy bảy phần trăm, còn PGB có P/B không phẩy bảy mươi mốt lần với ROE chín phẩy hai phần trăm. Điều '
         'thú vị là PGB có P/B thấp hơn KLB, nhìn qua rẻ hơn, nhưng KLB sinh lời trên vốn gần gấp hai lần rưỡi. Nếu bạn chỉ sắp xếp theo P/B từ thấp lên cao, bạn sẽ xếp '
         'PGB lên trên và nghĩ đó là cơ hội tốt hơn, trong khi cùng một đồng vốn ở KLB đang làm ra nhiều lợi nhuận hơn hẳn. Mức giá thấp hơn không đáng giá nếu thứ bạn '
         'mua kém hiệu quả hơn.'},
 {'k': 'checklist',
  'ch': 'Chương 3 – Vì sao P/B thấp chưa chắc rẻ',
  'moc': True,
  'label': 'Những lý do thị trường trả giá thấp',
  'cap': ('VÌ SAO P/B', 'THẤP?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('ROE thấp: vốn tạo ra ít lợi nhuận', (239, 68, 68)),
            ('Chất lượng tài sản đáng ngại: nợ xấu cao, bao phủ mỏng', (239, 68, 68)),
            ('Thị trường nghi ngờ khả năng duy trì lợi nhuận', (239, 68, 68)),
            ('Cổ phiếu ít thanh khoản, ít người theo dõi', (239, 68, 68)),
            ('Hoặc có thể thị trường đang định giá thấp một doanh nghiệp tốt', (34, 197, 94))],
  'anh': 'discount sale tag',
  'say': 'Vậy vì sao nhiều ngân hàng giao dịch dưới sổ sách? Có năm lý do thường gặp. Một, ROE thấp: nếu mỗi một trăm đồng vốn chỉ làm ra chín đồng lợi nhuận, thị '
         'trường không có lý do trả hơn mức sổ sách. Hai, chất lượng tài sản đáng ngại: nợ xấu cao hoặc bao phủ nợ xấu mỏng nên giá trị sổ sách có thể bị đánh giá cao '
         'hơn giá trị thực. Ba, thị trường nghi ngờ lợi nhuận hiện tại không duy trì được. Bốn, cổ phiếu ít thanh khoản, ít người theo dõi nên bị chiết khấu. Năm, cũng '
         'có trường hợp thị trường đang định giá thấp một doanh nghiệp tốt, và đó mới là cơ hội. Vấn đề là chỉ nhìn P/B, bạn không phân biệt được trường hợp nào là '
         'trường hợp nào. Vì vậy P/B thấp chỉ nên là lời mời bạn đào sâu hơn, chứ chưa phải kết luận.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Ngược lại: P/B cao có thể hợp lý',
  'moc': True,
  'label': 'Ví dụ ROE cao đi cùng P/B cao (5/11/2026)',
  'cap': ('P/B CAO', 'CHƯA ĐẮT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('LPB', 'P/B 2,33', 'ROE 26,3%'), ('VCB', 'P/B 1,81', 'ROE 17,6%'), ('HDB', 'P/B 1,61', 'ROE 23,3%')],
  'anh': 'premium quality',
  'say': 'Chiều ngược lại cũng đúng. Có những ngân hàng giao dịch ở P/B cao hơn nhiều so với sổ sách nhưng vẫn có lý do. LPB có P/B hai phẩy ba mươi ba lần với ROE hai '
         'mươi sáu phẩy ba phần trăm, cao nhất trong mười hai ngân hàng mình xem. VCB có P/B một phẩy tám mươi mốt lần với ROE mười bảy phẩy sáu phần trăm, mức giá cao '
         'thường đi cùng vị thế đầu ngành và chất lượng tài sản. HDB có P/B một phẩy sáu mươi mốt lần với ROE hai mươi ba phẩy ba phần trăm. Khi ROE cao và duy trì được '
         'nhiều năm, thị trường sẵn sàng trả cao hơn giá trị sổ sách, vì mỗi đồng vốn đó sinh ra nhiều lợi nhuận. Nhưng cũng đừng đảo chiều thành P/B cao thì tốt. Cái '
         'bạn cần kiểm tra là mức giá cao đã phản ánh sẵn bao nhiêu kỳ vọng, và ROE cao đó có bền hay chỉ là một giai đoạn đẹp. Ví dụ mình đưa ra chỉ để mô tả số liệu, '
         'không phải khuyến nghị mua bán.'},
 {'k': 'bars',
  'ch': 'Chương 5 – Ghép P/B với ROE trên một bảng',
  'moc': True,
  'label': 'ROE (%) của các ngân hàng, cùng P/B tại 5/11/2026',
  'cap': ('P/B VÀ ROE',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('KLB 0,80x', 22.7, (34, 197, 94), '22,7%'),
           ('CTG 1,17x', 22.5, (34, 197, 94), '22,5%'),
           ('ACB 1,14x', 16.5, (56, 189, 248), '16,5%'),
           ('OCB 0,88x', 13.0, (56, 189, 248), '13,0%'),
           ('PGB 0,71x', 9.2, (239, 68, 68), '9,2%')],
  'anh': 'scatter plot chart',
  'say': 'Cách đơn giản để ghép hai con số là đặt chúng cạnh nhau như trên biểu đồ, mỗi cột là ROE và nhãn bên dưới là P/B. KLB có ROE hai mươi hai phẩy bảy phần trăm ở '
         'P/B không phẩy tám mươi lần. CTG có ROE hai mươi hai phẩy năm phần trăm ở P/B một phẩy mười bảy lần. ACB có ROE mười sáu phẩy năm phần trăm ở P/B một phẩy '
         'mười bốn lần. OCB có ROE mười ba phẩy không phần trăm ở P/B không phẩy tám mươi tám lần. PGB có ROE chín phẩy hai phần trăm ở P/B không phẩy bảy mươi mốt lần. '
         'Quan sát thấy rằng nhìn chung ROE cao đi cùng P/B cao hơn, nhưng không đều: KLB có ROE gần bằng CTG mà P/B thấp hơn khá nhiều, có thể do quy mô, thanh khoản '
         'hoặc khác biệt chất lượng tài sản mà thị trường đang tính tới. Những chỗ lệch nhau như vậy không phải tín hiệu mua hay bán, mà là chỗ nên đặt câu hỏi: thị '
         'trường biết điều gì mà bảng số này chưa cho thấy?'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Khung ba câu hỏi đọc P/B',
  'moc': True,
  'label': 'Trước khi kết luận về định giá ngân hàng',
  'cap': ('3 CÂU HỎI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. ROE bao nhiêu và có ổn định nhiều năm không?', (255, 196, 0)),
            ('2. Nợ xấu và bao phủ nợ xấu thế nào?', (255, 196, 0)),
            ('3. Vốn có tăng thêm làm loãng cổ phiếu không?', (255, 196, 0)),
            ('Không đủ dữ liệu cho 3 câu: chưa kết luận', (239, 68, 68)),
            ('P/B thấp + ROE cao + tài sản tốt = đáng đào sâu', (34, 197, 94))],
  'anh': 'checklist clipboard',
  'say': 'Khung ba câu hỏi của mình khi đọc P/B của một ngân hàng. Câu một: ROE là bao nhiêu và có ổn định nhiều năm không? Một quý ROE cao có thể do yếu tố bất thường. '
         'Câu hai: nợ xấu và bao phủ nợ xấu thế nào? Đây là nơi giá trị sổ sách có thể bị thổi phồng nếu tài sản xấu chưa được trích lập đủ. Câu ba: ngân hàng có tăng '
         'vốn làm loãng cổ phiếu không? Phát hành thêm cổ phiếu làm tăng vốn nhưng cũng làm lợi nhuận mỗi cổ phiếu mỏng đi. Nếu cả ba câu đều có câu trả lời tích cực mà '
         'P/B vẫn thấp, đó là tổ hợp đáng đào sâu thêm. Nếu bạn không đủ dữ liệu để trả lời, thì đừng kết luận. Không có con số thần kỳ nào thay thế được việc tự đặt '
         'câu hỏi và kiểm tra.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những cái bẫy khi đọc định giá',
  'moc': True,
  'label': 'Bẫy thường gặp',
  'cap': ('3 CÁI BẪY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Sắp xếp theo P/B từ thấp lên cao rồi chọn', (239, 68, 68)),
            ('Bỏ qua ROA và đòn bẩy của ngân hàng', (239, 68, 68)),
            ('So P/B ngân hàng với công ty sản xuất', (239, 68, 68)),
            ('Dùng số liệu một quý để định giá cả năm', (239, 68, 68)),
            ('Cách đúng: so cùng ngành, cùng thời điểm, nhiều chỉ số', (34, 197, 94))],
  'anh': 'warning sign red',
  'say': 'Ba cái bẫy thường gặp. Bẫy một: sắp xếp danh sách theo P/B từ thấp lên cao rồi chọn những mã đứng đầu. Làm vậy bạn gần như chắc chắn chọn trúng những ngân '
         'hàng ROE thấp nhất, như ví dụ PGB và BAB. Bẫy hai: bỏ qua ROA và đòn bẩy. Ngân hàng vốn dùng đòn bẩy cao nên ROE có thể cao nhờ vay nhiều hơn, vì vậy hãy xem '
         'thêm ROA. Trong các ví dụ, KLB, TPB và ACB có ROA một phẩy tám phần trăm, một phẩy sáu phần trăm và một phẩy sáu phần trăm, còn BAB chỉ không phẩy sáu phần '
         'trăm. Bẫy ba: so P/B của ngân hàng với công ty sản xuất. Bảng cân đối của hai loại hình này khác bản chất nên so sánh chéo ngành rất dễ sai. Cách làm đúng là '
         'so cùng ngành, cùng thời điểm và dùng nhiều chỉ số, rồi coi kết quả là cơ sở để hỏi thêm chứ chưa phải câu trả lời cuối cùng.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài tập và tài liệu đi kèm',
  'moc': True,
  'label': 'Làm thử với bảng của riêng bạn',
  'cap': ('BÀI TẬP', 'TỰ LÀM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lấy P/B và ROE của 8–10 ngân hàng', (255, 196, 0)),
            ('Đánh dấu ngân hàng P/B thấp nhưng ROE cũng thấp', (255, 196, 0)),
            ('Đánh dấu ngân hàng P/B thấp mà ROE cao, đào sâu thêm', (255, 196, 0)),
            ('Kiểm tra nợ xấu và bao phủ của nhóm thứ hai', (255, 196, 0)),
            ('Bảng định giá: chungkhoanhuynguyen.com', (56, 189, 248))],
  'anh': 'student notebook homework',
  'say': 'Bài tập cho bạn: lập bảng gồm tám đến mười ngân hàng với P/B và ROE. Đánh dấu những ngân hàng P/B thấp nhưng ROE cũng thấp, đó là nhóm giá thấp có lý do. Đánh '
         'dấu những ngân hàng P/B thấp mà ROE cao, đó là nhóm đáng đào sâu thêm. Với nhóm thứ hai, tiếp tục kiểm tra nợ xấu và bao phủ nợ xấu. Bảng định giá cập nhật '
         'hằng ngày cho hơn bốn trăm mã, kèm bài viết giải thích đi cùng video này, có sẵn miễn phí tại chứng khoán Huy Nguyễn chấm com. Số liệu P/B và ROE trong video '
         'lấy từ dữ liệu tổng hợp ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu và có thể khác thông báo chính thức. Nội dung chia sẻ kiến thức, không '
         'phải khuyến nghị mua bán chứng khoán.'},
 {'k': 'end',
  'label': '',
  'cap': ('P/B THẤP', 'CHƯA CHẮC RẺ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, P/B cho bạn biết mình trả bao nhiêu, ROE cho bạn biết mình nhận lại bao nhiêu. Chỉ khi đọc cả hai, cùng chất lượng tài sản, bạn mới có bức tranh đầy '
         'đủ. Cảm ơn bạn đã xem, hẹn gặp bạn ở video tiếp theo.'}]

S['CH1411C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – hình nền minh họa',
  'cap': ('LỖ 50% PHẢI', 'LÃI 100% MỚI HÒA?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, 'Tuần 2/11/26: 1.741', 2.6]]},
  'anh': 'risk management stop loss',
  'say': 'Bạn có một trăm triệu đồng và danh mục giảm năm mươi phần trăm, còn năm mươi triệu. Muốn về lại một trăm triệu, bạn không cần lãi năm mươi phần trăm mà phải '
         'lãi một trăm phần trăm. Nếu danh mục giảm bảy mươi phần trăm, bạn cần lãi tới hai trăm ba mươi ba phần trăm. Còn giảm chín mươi phần trăm, bạn cần lãi chín '
         'trăm phần trăm mới về điểm xuất phát. Đây không phải mẹo tâm lý, mà là phép tính, và nó giải thích vì sao những người chơi lâu năm hay nhắc: trước khi nghĩ '
         'lãi bao nhiêu, hãy nghĩ lỗ tối đa bao nhiêu. Trong video này mình giải thích toán học đứng sau việc cắt lỗ và chia tỷ trọng, bằng những ví dụ giả định mà bạn '
         'có thể tự tính lại, rồi đưa ra một kế hoạch mẫu cho người mới. Xem hết, bạn sẽ biết vì sao một người thắng chưa tới nửa số lần vẫn có thể có lãi, và vì sao '
         'một người thắng nhiều lần vẫn có thể mất sạch. Biểu đồ phía sau chỉ là hình nền minh họa. Nội dung chia sẻ kiến thức, không phải khuyến nghị.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Bảng toán học của việc hòa vốn',
  'moc': True,
  'label': 'Mức lãi cần có để hòa vốn sau khi lỗ (%)',
  'cap': ('LỖ RỒI', 'LÃI BAO NHIÊU?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Lỗ 10%', 11.1, (56, 189, 248), '11,1%'),
           ('Lỗ 20%', 25.0, (56, 189, 248), '25%'),
           ('Lỗ 30%', 42.9, (255, 196, 0), '42,9%'),
           ('Lỗ 50%', 100.0, (239, 68, 68), '100%'),
           ('Lỗ 70%', 233.0, (239, 68, 68), '233%')],
  'anh': 'math formula chalkboard',
  'say': 'Công thức rất đơn giản: lãi cần có bằng mức lỗ chia cho một trừ mức lỗ. Lỗ mười phần trăm cần lãi mười một phẩy một phần trăm để hòa. Lỗ hai mươi phần trăm '
         'cần lãi hai mươi lăm phần trăm. Lỗ ba mươi phần trăm cần lãi bốn mươi hai phẩy chín phần trăm. Lỗ năm mươi phần trăm cần lãi một trăm phần trăm. Lỗ bảy mươi '
         'phần trăm cần lãi tới hai trăm ba mươi ba phần trăm. Quan sát biểu đồ: phần đầu tăng chậm, từ mười phần trăm đến hai mươi phần trăm lỗ chỉ thêm khoảng mười '
         'bốn điểm cần lãi, nhưng từ ba mươi phần trăm đến năm mươi phần trăm lỗ thì lãi cần có tăng hơn gấp đôi, và qua mốc năm mươi phần trăm đường cong dựng đứng. '
         'Đây là lý do mất hai mươi phần trăm là chuyện có thể sửa, còn mất năm mươi phần trăm là chuyện cực kỳ khó sửa. Thị trường Việt Nam từng cho ví dụ rất rõ: năm '
         'hai nghìn không trăm hai mươi hai, VN-Index giảm khoảng bốn mươi ba phần trăm từ đỉnh xuống đáy, và muốn về lại đỉnh phải tăng khoảng bảy mươi lăm phần trăm. '
         'Nếu bạn đồng thời dùng đòn bẩy, mức lỗ của bạn còn lớn hơn mức giảm của chỉ số.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Thắng ít vẫn có thể lãi',
  'moc': True,
  'label': '10 lệnh giả định, lãi và lỗ mỗi lệnh khác nhau',
  'cap': ('THẮNG ÍT', 'VẪN LÃI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('5 thắng +15%, 5 thua -8%', 'tổng ~ +32,6%', 'tỷ lệ thắng chỉ 50%'),
            ('4 thắng +20%, 6 thua -8%', 'tổng ~ +25,7%', 'tỷ lệ thắng chỉ 40%'),
            ('5 thắng +15%, 5 thua -15%', 'tổng ~ -10,8%', 'thắng 50% vẫn lỗ')],
  'anh': 'scales profit loss',
  'say': 'Nhiều người nghĩ muốn có lãi phải thắng thật nhiều lần. Phép tính cho thấy điều quan trọng hơn là lỗ nhỏ hơn lãi bao nhiêu. Ví dụ giả định thứ nhất: mười '
         'lệnh, năm lệnh thắng mỗi lệnh lãi mười lăm phần trăm, năm lệnh thua mỗi lệnh lỗ tám phần trăm. Tính nhân liên tiếp, vốn tăng khoảng ba mươi hai phẩy sáu phần '
         'trăm, dù tỷ lệ thắng chỉ năm mươi phần trăm. Ví dụ thứ hai: bốn lệnh thắng lãi hai mươi phần trăm, sáu lệnh thua lỗ tám phần trăm, vốn vẫn tăng khoảng hai '
         'mươi lăm phẩy bảy phần trăm dù tỷ lệ thắng chỉ bốn mươi phần trăm. Nhưng ví dụ thứ ba: năm lệnh thắng lãi mười lăm phần trăm, năm lệnh thua lỗ mười lăm phần '
         'trăm, vốn giảm khoảng mười phẩy tám phần trăm. Đây chính là điều mà người chơi dài hạn hiểu rất sớm: bạn không cần đúng nhiều lần, bạn cần để những lần sai có '
         'giá nhỏ. Chiến lược cắt lỗ chính là cách để biến lần sai thành khoản phí nhỏ có thể kiểm soát.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Tính khối lượng theo mức rủi ro',
  'moc': True,
  'label': 'Ví dụ giả định: vốn 500 triệu, rủi ro tối đa 1% mỗi lệnh',
  'cap': ('TÍNH', 'KHỐI LƯỢNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Rủi ro tối đa mỗi lệnh', '5 triệu', '1% của 500 triệu'),
            ('Mua giá 20.000, cắt lỗ -8%', 'lỗ 1.600 đ/cp', '5 triệu / 1.600'),
            ('Khối lượng tối đa', '3.125 cổ phiếu', 'giá trị 62,5 triệu = 12,5% vốn')],
  'anh': 'calculator position size',
  'say': 'Giờ tới phần thực hành: tính khối lượng dựa trên mức rủi ro. Giả sử vốn năm trăm triệu, bạn quy định mỗi lệnh chỉ chấp nhận mất tối đa một phần trăm vốn, tức '
         'năm triệu. Bạn dự định mua ở giá hai mươi nghìn đồng và nếu giá giảm tám phần trăm, tức về mười tám nghìn bốn trăm, thì thoát. Mỗi cổ phiếu lỗ một nghìn sáu '
         'trăm đồng. Khối lượng tối đa là năm triệu chia cho một nghìn sáu trăm, khoảng ba nghìn một trăm hai mươi lăm cổ phiếu, tương đương giá trị sáu mươi hai phẩy '
         'năm triệu, chiếm mười hai phẩy năm phần trăm vốn. Chú ý thứ tự: bạn không chọn số tiền muốn mua rồi mới tính lỗ, mà chọn mức lỗ tối đa chấp nhận được rồi suy '
         'ra khối lượng. Cách tính ngược này khiến bạn mua ít hơn khi mức cắt lỗ xa, và mua nhiều hơn khi mức cắt lỗ gần, tức là rủi ro trên mỗi lệnh luôn được giữ ổn '
         'định. Đây là ví dụ giả định, không phải khuyến nghị về mã hay giá.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Tỷ trọng: bảo hiểm tốt nhất cho sai lầm',
  'moc': True,
  'label': 'Một mã chiếm bao nhiêu danh mục, cùng giảm 50%',
  'cap': ('TỶ TRỌNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Chiếm 40% danh mục', 'mã giảm 50%', 'danh mục mất 20%'),
            ('Chiếm 20% danh mục', 'mã giảm 50%', 'danh mục mất 10%'),
            ('Chiếm 10% danh mục', 'mã giảm 50%', 'danh mục mất 5%')],
  'anh': 'portfolio pie chart',
  'say': 'Cắt lỗ là công cụ, tỷ trọng là lớp bảo hiểm thứ hai. Giả sử một mã giảm năm mươi phần trăm. Nếu mã đó chiếm bốn mươi phần trăm danh mục, danh mục mất hai mươi '
         'phần trăm. Nếu chiếm hai mươi phần trăm, danh mục mất mười phần trăm. Nếu chỉ chiếm mười phần trăm, danh mục mất năm phần trăm. Cùng một sai lầm, nhưng kết '
         'cục khác nhau gấp bốn lần. Điều này có ý nghĩa đặc biệt khi bạn sai mà không kịp cắt lỗ, vì giá rơi qua mức thoát trong một phiên hoặc vì doanh nghiệp công bố '
         'tin xấu bất ngờ. Giới hạn tỷ trọng tối đa của một mã, ví dụ không quá mười đến mười lăm phần trăm danh mục, giúp bạn sống sót qua loại sai lầm mà không công '
         'cụ cắt lỗ nào xử lý hết. Thêm vào đó, không phải mọi mã trong danh mục đều có tương quan, nên chia ngành và chia nhịp mua giúp tránh việc nhiều vị thế cùng '
         'gặp vấn đề một lúc.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Ba cách đặt điểm thoát',
  'moc': True,
  'label': 'Mỗi cách có ưu và nhược',
  'cap': ('3 CÁCH',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Theo phần trăm: dễ làm, nhưng không xét đặc tính từng mã', (56, 189, 248)),
            ('Theo kỹ thuật: thoát khi thủng vùng hỗ trợ đã xác định', (56, 189, 248)),
            ('Theo luận điểm: thoát khi lý do mua không còn đúng', (56, 189, 248)),
            ('Theo thời gian: thoát nếu sau N tháng chưa như kế hoạch', (255, 196, 0)),
            ('Quan trọng nhất: viết ra TRƯỚC khi mua', (34, 197, 94))],
  'anh': 'three roads signpost',
  'say': 'Có ba cách thường dùng để đặt điểm thoát. Cách một là theo phần trăm, ví dụ lỗ tám phần trăm thì thoát. Ưu điểm là dễ làm, nhược điểm là không xét đặc tính '
         'từng mã: một cổ phiếu biến động mạnh có thể bị quét ra khỏi lệnh chỉ vì dao động bình thường. Cách hai là theo kỹ thuật, thoát khi giá thủng một vùng hỗ trợ '
         'đã xác định. Cách này gần với diễn biến thị trường hơn, nhưng đòi hỏi bạn biết xác định vùng hỗ trợ. Cách ba là theo luận điểm: nếu lý do bạn mua, ví dụ lợi '
         'nhuận tăng trưởng, không còn đúng thì thoát, kể cả khi giá chưa giảm nhiều. Bạn có thể thêm cách thứ tư, theo thời gian: nếu sau vài tháng chưa diễn ra như kế '
         'hoạch thì xem lại. Điểm chung quan trọng nhất của mọi cách là bạn phải viết ra trước khi mua, khi đầu óc còn bình tĩnh, chứ không phải nghĩ lúc đang lỗ.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Những sai lầm kinh điển khi cắt lỗ',
  'moc': True,
  'label': 'Cắt lỗ sai cách còn tệ hơn không có kế hoạch',
  'cap': ('4 SAI LẦM',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Dời mức cắt lỗ xa hơn khi giá sắp chạm', (239, 68, 68)),
            ('Bình quân giá xuống vô điều kiện để hạ giá vốn', (239, 68, 68)),
            ('Đặt cắt lỗ quá sát, bị quét ra bởi dao động thường ngày', (239, 68, 68)),
            ('Cắt lỗ xong lại mua đuổi ngay vì tức', (239, 68, 68)),
            ('Cách đúng: dùng quy tắc đã viết, ghi nhật ký mỗi lệnh', (34, 197, 94))],
  'anh': 'broken rules mistakes',
  'say': 'Bốn sai lầm kinh điển khi cắt lỗ. Một, dời mức cắt lỗ xa hơn mỗi khi giá sắp chạm, tức là biến một quy tắc thành một lời hứa vô nghĩa. Hai, bình quân giá '
         'xuống vô điều kiện để hạ giá vốn. Mua thêm khi luận điểm còn đúng là một chuyện, mua thêm chỉ vì không chấp nhận lỗ là chuyện khác, và thường biến một khoản '
         'lỗ vừa phải thành khoản lỗ lớn. Ba, đặt cắt lỗ quá sát nên bị quét ra bởi dao động bình thường rồi giá quay lại, khiến bạn mất phí và mất cơ hội. Bốn, cắt lỗ '
         'xong lại mua đuổi ngay vì tức, tức là cảm xúc đang điều khiển lệnh tiếp theo. Cách khắc phục chung là có quy tắc bằng văn bản và nhật ký cho từng lệnh, để sau '
         'mỗi tháng bạn xem lại và điều chỉnh bằng dữ liệu thay vì bằng cảm xúc.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Kế hoạch mẫu cho người mới',
  'moc': True,
  'label': 'Bản nháp để bạn chỉnh theo hoàn cảnh của mình',
  'cap': ('KẾ HOẠCH', 'MẪU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Rủi ro tối đa mỗi lệnh: 1–2% tổng vốn', (255, 196, 0)),
            ('Một mã tối đa 10–15% danh mục', (255, 196, 0)),
            ('Tổng lỗ tối đa trong tháng: ví dụ 5%, chạm thì nghỉ xem lại', (255, 196, 0)),
            ('Viết lý do mua, điểm thoát, tỷ trọng trước khi đặt lệnh', (255, 196, 0)),
            ('Không dùng đòn bẩy cho đến khi có nhật ký 12 tháng', (255, 196, 0))],
  'anh': 'plan notebook pen',
  'say': 'Kế hoạch mẫu cho người mới, bạn hãy chỉnh theo hoàn cảnh của mình. Một, rủi ro tối đa mỗi lệnh từ một đến hai phần trăm tổng vốn. Hai, một mã tối đa mười đến '
         'mười lăm phần trăm danh mục. Ba, giới hạn tổng lỗ trong tháng, ví dụ năm phần trăm, nếu chạm mức này thì dừng giao dịch mới để xem lại thay vì cố gỡ. Bốn, '
         'trước khi đặt lệnh viết ra lý do mua, điểm thoát và tỷ trọng. Năm, chưa dùng đòn bẩy cho đến khi có ít nhất mười hai tháng nhật ký giao dịch cho thấy bạn tuân '
         'thủ được quy tắc. Những con số trên chỉ là ví dụ để bạn bắt đầu; người có vốn lớn hơn, thời gian dài hơn, hay chấp nhận rủi ro khác có thể chọn mức khác. Điều '
         'quan trọng là bạn có mức của riêng mình, và bạn tuân thủ nó ngay cả khi thị trường đang rất hấp dẫn.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài tập tự làm và tài liệu đi kèm',
  'moc': True,
  'label': 'Tính thử với danh mục của bạn',
  'cap': ('BÀI TẬP', 'TỰ LÀM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Tính lỗ tối đa mỗi lệnh bằng 1% vốn của bạn', (255, 196, 0)),
            ('Tính khối lượng tối đa theo mức cắt lỗ dự kiến', (255, 196, 0)),
            ('Kiểm tra mã nào đang chiếm hơn 15% danh mục', (255, 196, 0)),
            ('Viết 3 dòng quy tắc, dán ở nơi nhìn thấy', (255, 196, 0)),
            ('Công cụ và bảng số: chungkhoanhuynguyen.com', (56, 189, 248))],
  'anh': 'student notebook homework',
  'say': 'Bài tập cho bạn mất khoảng mười phút. Lấy tổng vốn của bạn, tính một phần trăm làm mức lỗ tối đa mỗi lệnh. Với một mã bạn đang quan tâm và mức cắt lỗ dự kiến, '
         'tính khối lượng tối đa theo cách ở chương ba. Sau đó nhìn danh mục hiện tại, xem mã nào đang chiếm hơn mười lăm phần trăm. Cuối cùng viết ba dòng quy tắc ngắn '
         'của riêng bạn và đặt ở nơi dễ thấy. Bài viết kèm video, công cụ tính và bảng số liệu cho hơn bốn trăm mã được cập nhật miễn phí tại chứng khoán Huy Nguyễn '
         'chấm com. Toàn bộ ví dụ trong video là số giả định để minh họa phép tính, không phải khuyến nghị mua, bán hay cắt lỗ bất kỳ mã nào. Mỗi người có mục tiêu và '
         'khả năng chịu rủi ro khác nhau.'},
 {'k': 'end',
  'label': '',
  'cap': ('LỖ NHỎ', 'SỐNG LÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, nghệ thuật không nằm ở việc tránh mọi cú lỗ, mà ở việc không để cú lỗ nào đủ lớn để loại bạn khỏi cuộc chơi. Cảm ơn bạn đã xem, hẹn gặp bạn ở video '
         'tiếp theo trong seri Quản trị vốn.'}]

