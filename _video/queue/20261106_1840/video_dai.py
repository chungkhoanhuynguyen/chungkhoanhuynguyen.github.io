# -*- coding: utf-8 -*-
# VIDEO DÀI KÊNH CHÍNH – NV1 soạn 06/11/2026 (lô 20261106_1840: CH1711A, CH1711B, CH1711C, CH1811A, CH1811B, CH1811C). Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['CH1711A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VIB – Đọc BCTC 5 phút',
  'cap': ('BAO PHỦ NỢ XẤU', 'CHỈ 42%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VIBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[0, 16.54, 'Đỉnh tuần 3/11/25: 16,54', 0.6], [37, 12.83, 'Đáy tuần 27/7/26: 12,83', 1.6], [51, 13.9, 'Tuần 2/11/26: 13,90', 2.6]]},
  'anh': 'bank building vietnam',
  'say': 'Một ngân hàng lãi quý ba tăng mười tám phẩy năm phần trăm, nhưng bộ đệm dự phòng chỉ phủ khoảng bốn mươi hai phần trăm nợ xấu. Anh chị sẽ tin con số nào '
         'trước, lãi tăng hay đệm mỏng? Rất nhiều người chỉ nhìn con số lợi nhuận rồi kết luận. Video này em đọc báo cáo tài chính quý ba năm hai nghìn không trăm hai '
         'mươi sáu của VIB, mã VIB, theo năm bước: lợi nhuận, thu nhập lãi thuần cùng lãi dịch vụ, chi phí dự phòng, nợ xấu cùng bao phủ, và định giá. Xem hết, anh chị '
         'sẽ biết vì sao lãi tăng đẹp vẫn chưa đủ để kết luận. Số liệu tính đến ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, còn cách đọc thì dùng '
         'được nhiều năm. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ VIB (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q2/25', 2076.5, (56, 189, 248), '2.077'),
           ('Q3/25', 1624.5, (56, 189, 248), '1.625'),
           ('Q4/25', 1648.0, (56, 189, 248), '1.648'),
           ('Q1/26', 2241.2, (56, 189, 248), '2.241'),
           ('Q2/26', 1905.4, (56, 189, 248), '1.905'),
           ('Q3/26', 1924.9, (34, 197, 94), '1.925')],
  'anh': 'financial charts',
  'say': 'Bước một, lợi nhuận qua các quý. Quý ba năm hai nghìn không trăm hai mươi sáu VIB lãi sau thuế khoảng một nghìn chín trăm hai mươi lăm tỷ đồng, tăng mười tám '
         'phẩy năm phần trăm so với cùng kỳ năm trước là một nghìn sáu trăm hai mươi lăm tỷ. Nhưng so với quý hai, mức tăng chỉ khoảng một phần trăm. Nghĩa là lợi nhuận '
         'đi ngang trong ba quý liền quanh mức một nghìn chín trăm đến hai nghìn hai trăm năm mươi tỷ, chưa có một cú bứt phá thật sự. Lũy kế chín tháng đạt sáu nghìn '
         'không trăm bảy mươi mốt tỷ, tăng bảy phẩy bảy phần trăm, thấp hơn nhiều so với mức tăng của quý ba. Vì sao quý ba tăng mười tám phẩy năm phần trăm mà chín '
         'tháng chỉ bảy phẩy bảy phần trăm? Vì quý ba năm ngoái là một nền thấp. Đây là hiệu ứng nền so sánh, và là lý do em luôn đặt cả chuỗi nhiều quý cạnh nhau thay '
         'vì chỉ nhìn một con số.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần VIB (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 4172.7, (56, 189, 248), '4.173'),
           ('Q4/25', 4213.6, (56, 189, 248), '4.214'),
           ('Q1/26', 4038.6, (56, 189, 248), '4.039'),
           ('Q2/26', 4368.0, (56, 189, 248), '4.368'),
           ('Q3/26', 4780.8, (34, 197, 94), '4.781')],
  'anh': 'financial charts',
  'say': 'Bước hai, thu nhập lãi thuần, phần cốt lõi của một ngân hàng. Quý ba đạt khoảng bốn nghìn bảy trăm tám mươi mốt tỷ, tăng mười bốn phẩy sáu phần trăm so với '
         'cùng kỳ và tăng gần chín phẩy năm phần trăm so với quý hai. Đây là mức cao nhất trong mười hai quý gần nhất. Biên lãi ròng, tức NIM, khoảng hai phẩy tám mươi '
         'ba phần trăm. Thu nhập lãi tăng nhanh hơn mức tăng lợi nhuận chín tháng, cho thấy hoạt động cho vay vẫn đang mở rộng đều. Điểm đáng chú ý nữa là lãi dịch vụ. '
         'Khoản này đạt khoảng chín trăm chín mươi tỷ, tăng một trăm phẩy sáu phần trăm, gấp đôi cùng kỳ. Nguồn thu ngoài lãi tăng mạnh là tín hiệu tốt, nhưng nguyên '
         'nhân cụ thể cần đọc ở phần thuyết minh của báo cáo.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Chi phí dự phòng',
  'moc': True,
  'label': 'Thu nhập tăng, nhưng dự phòng tăng nhanh hơn',
  'cap': ('DỰ PHÒNG', 'TĂNG NHANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Chi phí dự phòng', '+64,0%', 'so với cùng kỳ'), ('Thu nhập lãi thuần', '+14,6%', 'so với cùng kỳ'), ('Lãi dịch vụ', '+100,6%', 'khoảng 990 tỷ')],
  'anh': 'insurance shield money',
  'say': 'Bước ba, chi phí dự phòng. Đây là khoản tiền ngân hàng trích ra từ lợi nhuận để phòng khi khách hàng không trả được nợ. Quý ba, chi phí dự phòng của VIB tăng '
         'sáu mươi bốn phần trăm so với cùng kỳ. Con số này nhanh hơn rất nhiều so với mức tăng mười bốn phẩy sáu phần trăm của thu nhập lãi thuần. Nói đơn giản, cứ mỗi '
         'đồng thu nhập lãi tăng thêm, ngân hàng phải trích phần lớn hơn để dự phòng. Điều này không nhất thiết là xấu. Trích nhiều có thể là thận trọng. Nhưng nó giải '
         'thích vì sao lợi nhuận chỉ tăng đều chứ không bứt phá, dù thu nhập lãi và lãi dịch vụ đều tăng mạnh.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Nợ xấu và bao phủ',
  'moc': True,
  'label': 'Bao phủ nợ xấu (%) – Q3/2026',
  'cap': ('BAO PHỦ', 'NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('VIB', 42.0, (239, 68, 68), '42%'),
           ('HDB', 46.0, (56, 189, 248), '46%'),
           ('MSB', 47.0, (56, 189, 248), '47%'),
           ('VPB', 54.0, (56, 189, 248), '54%'),
           ('TPB', 57.0, (56, 189, 248), '57%'),
           ('OCB', 58.0, (56, 189, 248), '58%'),
           ('LPB', 63.0, (34, 197, 94), '63%')],
  'anh': 'bank vault',
  'say': 'Bước bốn, nợ xấu và bao phủ. Tỷ lệ nợ xấu của VIB quý ba là ba phẩy hai mươi phần trăm, tăng từ hai phẩy chín mươi ba phần trăm của quý trước, tức tăng khoảng '
         'không phẩy hai mươi bảy điểm phần trăm trong đúng một quý. Bao phủ nợ xấu, tức số tiền dự phòng so với số nợ xấu, chỉ khoảng bốn mươi hai phần trăm. Hiểu đơn '
         'giản, cứ một trăm đồng nợ xấu thì ngân hàng mới có khoảng bốn mươi hai đồng dự phòng. Biểu đồ bên cạnh so sánh VIB với sáu ngân hàng khác trong dữ liệu của '
         'em. VIB nằm thấp nhất nhóm, trong khi cao nhất là khoảng sáu mươi ba phần trăm. Bao phủ thấp không có nghĩa sắp có chuyện, nhưng bộ đệm mỏng nghĩa là nếu nợ '
         'xấu tiếp tục tăng, ngân hàng sẽ phải trích thêm, và lợi nhuận các quý sau sẽ chịu áp lực.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Hiệu quả và định giá',
  'moc': True,
  'label': 'Hiệu quả và định giá VIB',
  'cap': ('ĐỊNH GIÁ', 'VIB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE', '16,2%', 'mức khá'), ('P/E', '6,81 lần', 'dữ liệu 5/11/2026'), ('P/B', '1,06 lần', 'gần giá trị sổ sách')],
  'anh': 'finance',
  'say': 'Bước năm, hiệu quả và định giá. ROE của VIB khoảng mười sáu phẩy hai phần trăm, ở mức khá. P/E khoảng sáu phẩy tám mươi mốt lần và P/B khoảng một phẩy không '
         'sáu lần theo dữ liệu tổng hợp ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu. Nhìn qua thì rẻ: P/B chỉ hơn một lần giá trị sổ sách. Nhưng em '
         'nhắc lại điều này nhiều lần trong seri. Định giá thấp luôn đi cùng một câu hỏi: thị trường đang trả giá thấp vì bỏ sót, hay vì họ nhìn thấy điều mà con số lợi '
         'nhuận chưa thể hiện? Với VIB, hai điều thị trường có thể đang cân nhắc là nợ xấu đang tăng và bao phủ đứng thấp nhất nhóm. Đây là đánh đổi, không phải câu trả '
         'lời. Mỗi nhà đầu tư tự cân theo khẩu vị rủi ro của mình.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Ghép các mảnh lại',
  'moc': True,
  'label': 'Lãi tăng đẹp – nhưng đã đủ chưa?',
  'cap': ('GHÉP LẠI', 'CẢ BỨC TRANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Thu nhập lãi thuần tăng 14,6%', (34, 197, 94)),
            ('Lãi dịch vụ tăng gấp đôi', (34, 197, 94)),
            ('Định giá P/B chỉ khoảng 1,06 lần', (34, 197, 94)),
            ('Chi phí dự phòng tăng 64%', (239, 68, 68)),
            ('Nợ xấu nhích lên 3,20%', (239, 68, 68)),
            ('Bao phủ khoảng 42%, thấp nhất nhóm', (239, 68, 68))],
  'anh': 'scales balance',
  'say': 'Ghép các mảnh lại. Bốn điểm tích cực: thu nhập lãi thuần tăng mười bốn phẩy sáu phần trăm, lãi dịch vụ tăng gấp đôi, lợi nhuận quý tăng mười tám phẩy năm phần '
         'trăm, định giá không cao. Ba điểm cần theo dõi: chi phí dự phòng tăng sáu mươi bốn phần trăm, nợ xấu nhích lên ba phẩy hai mươi phần trăm, và bao phủ chỉ '
         'khoảng bốn mươi hai phần trăm. Câu trả lời trung thực là bức tranh có sáng và có tối. Cách dùng bài học này cho bất kỳ ngân hàng nào: đừng đọc lợi nhuận một '
         'mình, hãy đọc cùng ba người bạn đồng hành là chi phí dự phòng, nợ xấu và bao phủ. Và đừng đọc một quý, hãy đọc cả chuỗi. Quý sau, nếu nợ xấu quay đầu giảm và '
         'bao phủ dày lên, bức tranh sẽ khác đi rất nhiều.'},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('ĐỌC CẢ CHUỖI', 'ĐỪNG ĐỌC 1 QUÝ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, lãi tăng đẹp chưa phải là hết câu chuyện. Hãy đọc lợi nhuận cùng chi phí dự phòng, nợ xấu và bao phủ, và đọc cả chuỗi nhiều quý. Cảm ơn anh chị đã '
         'xem. Theo anh chị, với một ngân hàng lãi tăng nhưng bao phủ mỏng, điều gì quan trọng hơn: tốc độ tăng lợi nhuận hay độ dày của bộ đệm? Anh chị để lại ý kiến '
         'bên dưới giúp em nhé.'}]

S['CH1711B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Cổ tức – sự thật sau ngày chốt quyền',
  'cap': ('NHẬN CỔ TỨC', 'LÀ LÃI HAY LỖ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1933,11', 0.6], [1, 1578.42, 'Đáy tuần 10/11/25: 1578,42', 1.6], [51, 1720.66, 'Tuần 2/11/26: 1720,66', 2.6]]},
  'anh': 'dividend money',
  'say': 'Anh chị nhận về một triệu đồng cổ tức, tài khoản hiện lên chữ lãi. Nhưng cùng ngày hôm đó, giá cổ phiếu lại bị trừ đi đúng một triệu. Vậy rốt cuộc anh chị có '
         'lời thêm đồng nào không? Rất nhiều người mới đầu tư tin rằng cổ tức là tiền biếu thêm. Video này em đi qua bốn bước: chuyện gì xảy ra với giá vào ngày giao '
         'dịch không hưởng quyền, cổ tức bằng cổ phiếu khác gì cổ tức tiền mặt, vì sao cổ tức cao chưa chắc tốt, và bốn câu hỏi để đọc cổ tức. Xem hết, anh chị sẽ hiểu '
         'vì sao nhận cổ tức không phải là lãi thêm, nhưng cũng không phải là lỗ. Mọi con số trong video là ví dụ giả định để dễ hình dung. Biểu đồ phía sau chỉ là hình '
         'nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Ngày giao dịch không hưởng quyền',
  'moc': True,
  'label': 'Ví dụ giả định: cổ tức tiền mặt 1.000 đồng/cổ phiếu',
  'cap': ('GIÁ ĐIỀU CHỈNH', 'NGÀY GDKHQ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Trước GDKHQ', 20000.0, (56, 189, 248), '20.000'), ('Sau GDKHQ', 19000.0, (239, 68, 68), '19.000'), ('Cổ tức nhận', 1000.0, (34, 197, 94), '1.000')],
  'anh': 'coins stack',
  'say': 'Bước một, ngày giao dịch không hưởng quyền. Giả sử anh chị giữ một trăm cổ phiếu giá hai mươi nghìn đồng, tổng tài sản hai triệu đồng. Doanh nghiệp công bố '
         'trả cổ tức tiền mặt một nghìn đồng mỗi cổ phiếu. Đến ngày giao dịch không hưởng quyền, giá tham chiếu được điều chỉnh giảm đúng bằng mức cổ tức, từ hai mươi '
         'nghìn xuống mười chín nghìn đồng. Lý do rất hợp lý: doanh nghiệp sắp đưa ra ngoài một khoản tiền, nên giá trị còn lại trong doanh nghiệp phải thấp đi tương '
         'ứng. Vài tuần sau, anh chị nhận một trăm nghìn đồng cổ tức. Cộng lại: một triệu chín trăm nghìn trong cổ phiếu, cộng một trăm nghìn tiền mặt, vẫn là hai triệu '
         'đồng. Chưa có đồng lời nào xuất hiện thêm, chỉ là tiền chuyển từ túi này sang túi kia.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Cổ tức bằng cổ phiếu',
  'moc': True,
  'label': 'Ví dụ giả định: trả cổ tức 10% bằng cổ phiếu',
  'cap': ('CỔ TỨC CỔ PHIẾU', 'CHIA NHỎ MIẾNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Trước', '100 cp', 'giá 20.000 đồng'), ('Sau', '110 cp', 'giá khoảng 18.182 đồng'), ('Tổng tài sản', '~2 triệu', 'gần như không đổi')],
  'anh': 'pizza slices',
  'say': 'Bước hai, cổ tức bằng cổ phiếu. Doanh nghiệp trả cổ tức mười phần trăm bằng cổ phiếu, nghĩa là cứ mười cổ phiếu được tặng thêm một. Anh chị có một trăm cổ '
         'phiếu thì sau đó có một trăm mười cổ phiếu. Nghe như được tặng, nhưng doanh nghiệp vẫn là doanh nghiệp đó, chỉ chia thành nhiều phần hơn. Giá được điều chỉnh '
         'từ hai mươi nghìn xuống khoảng mười tám nghìn một trăm tám mươi hai đồng. Một trăm mười cổ phiếu nhân với mức giá đó vẫn xấp xỉ hai triệu đồng. Giống như một '
         'chiếc bánh cắt thành mười một miếng thay vì mười miếng: số miếng nhiều hơn nhưng tổng chiếc bánh không đổi. Giá trị chỉ thật sự tăng khi doanh nghiệp kiếm '
         'được nhiều tiền hơn trong những năm sau.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Cổ tức cao chưa chắc tốt',
  'moc': True,
  'label': 'Ví dụ giả định: tổng lợi suất 1 năm',
  'cap': ('CỔ TỨC CAO', 'CHƯA CHẮC TỐT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Cổ phiếu A', '-3%', 'cổ tức 5%, giá giảm 8%'), ('Cổ phiếu B', '+7%', 'cổ tức 1%, giá tăng 6%'), ('Công thức', 'Giá + cổ tức', 'đọc cả hai vế')],
  'anh': 'stock chart declining',
  'say': 'Bước ba, vì sao cổ tức cao chưa chắc tốt. Xét hai cổ phiếu giả định. Cổ phiếu A trả cổ tức năm phần trăm một năm nhưng giá giảm tám phần trăm. Tổng cộng anh '
         'chị mất ba phần trăm. Cổ phiếu B chỉ trả cổ tức một phần trăm, nhưng giá tăng sáu phần trăm, tổng lợi suất là bảy phần trăm. Tổng lợi suất luôn bằng phần '
         'chênh lệch giá cộng với cổ tức, không thể chỉ nhìn một vế. Có một cái bẫy nữa là tỷ suất cổ tức tính trên giá hiện tại. Khi giá giảm mạnh, tỷ suất tự nhiên '
         'trông cao lên, dù doanh nghiệp không hề trả thêm đồng nào. Một mức cổ tức rất cao đôi khi chỉ là dấu hiệu giá đang bị bán tháo vì thị trường lo ngại điều gì '
         'đó.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Bốn câu hỏi đọc cổ tức',
  'moc': True,
  'label': 'Bốn câu hỏi trước khi tin vào cổ tức',
  'cap': ('BỐN CÂU HỎI', 'VỀ CỔ TỨC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Cổ tức trả từ lợi nhuận thật?', (34, 197, 94)),
            ('Dòng tiền kinh doanh có đủ?', (34, 197, 94)),
            ('Nợ có đang tăng nhanh?', (239, 68, 68)),
            ('Lịch sử trả đều nhiều năm?', (34, 197, 94)),
            ('Cổ tức năm trước không bảo đảm năm sau', (255, 196, 0))],
  'anh': 'checklist',
  'say': 'Bước bốn, bốn câu hỏi trước khi tin vào cổ tức. Câu một, cổ tức có được trả từ lợi nhuận thật không, hay doanh nghiệp phải vay để trả. Tỷ lệ chi trả cổ tức '
         'quá cao so với lợi nhuận là dấu hiệu cần để ý. Câu hai, dòng tiền kinh doanh có đủ không. Lợi nhuận kế toán có thể đẹp nhưng tiền thật chưa về. Câu ba, nợ có '
         'đang tăng không, vì doanh nghiệp nợ nhiều thường phải ưu tiên trả nợ trước cổ đông. Câu bốn, lịch sử trả cổ tức có đều nhiều năm không, hay chỉ một năm đột '
         'biến. Và nhớ rằng cổ tức năm trước không bảo đảm cho năm sau. Trả lời được cả bốn câu, anh chị đã đọc cổ tức giỏi hơn đa số người chỉ nhìn một con số tỷ '
         'suất.'},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('CỔ TỨC', 'KHÔNG PHẢI QUÀ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, cổ tức là tiền chuyển từ giá cổ phiếu sang tài khoản tiền mặt của anh chị, không phải khoản lãi thêm. Giá trị thật đến từ việc doanh nghiệp kiếm được '
         'nhiều tiền hơn theo thời gian. Cảm ơn anh chị đã xem. Theo anh chị, lúc nhận cổ tức, anh chị thường làm gì với số tiền đó: tiêu, hay mua thêm cổ phiếu? Anh '
         'chị để lại ý kiến bên dưới giúp em nhé.'}]

S['CH1711C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Bài học lịch sử – VN-Index 3 năm',
  'cap': ('GIẢM >10%', '4 LẦN RỒI – SAO?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[27, 1933.11, 'Đỉnh tuần 18/5/26: 1933,11', 0.6], [1, 1578.42, 'Đáy tuần 10/11/25: 1578,42', 1.6], [51, 1720.66, 'Tuần 2/11/26: 1720,66', 2.6]]},
  'anh': 'stock exchange screen',
  'say': 'Trong chưa đầy ba năm, chỉ số VN-Index đã bốn lần giảm trên mười phần trăm từ đỉnh gần nhất. Vậy mà từ cuối tháng mười năm hai nghìn không trăm hai mươi ba '
         'đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, chỉ số vẫn tăng khoảng sáu mươi hai phần trăm. Nghe như hai chuyện không thể cùng đúng, '
         'đúng không anh chị? Video này em đi qua số liệu thật của VN-Index theo giá đóng cửa: bốn lần giảm đó sâu bao nhiêu, mất bao lâu, ba lần đã hồi như thế nào, và '
         'lần thứ tư đang ở đâu. Xem hết, anh chị sẽ rút ra bốn bài học về cách sống chung với những nhịp giảm. Đây là bài học lịch sử, không phải dự báo. Quá khứ không '
         'bảo đảm tương lai. Biểu đồ phía sau là VN-Index theo tuần.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Bốn lần giảm trên 10%',
  'moc': True,
  'label': 'Mức giảm từ đỉnh đến đáy (%) – giá đóng cửa',
  'cap': ('BỐN LẦN', 'GIẢM SÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('3/2025', 18.1, (239, 68, 68), '-18,1%'),
           ('10/2025', 10.5, (239, 68, 68), '-10,5%'),
           ('1/2026', 16.4, (239, 68, 68), '-16,4%'),
           ('5/2026', 13.5, (239, 68, 68), '-13,5%')],
  'anh': 'stock crash chart',
  'say': 'Bước một, bốn lần giảm. Lần một, từ đỉnh ngày mười bảy tháng ba năm hai nghìn không trăm hai mươi lăm khoảng một nghìn ba trăm ba mươi sáu điểm xuống một '
         'nghìn không trăm chín mươi bốn điểm ngày chín tháng bốn năm hai nghìn không trăm hai mươi lăm, giảm mười tám phẩy một phần trăm chỉ trong hai mươi ba ngày. '
         'Lần hai, từ một nghìn bảy trăm sáu mươi bảy điểm ngày mười sáu tháng mười năm hai nghìn không trăm hai mươi lăm xuống một nghìn năm trăm tám mươi mốt điểm '
         'ngày mười tháng mười một năm hai nghìn không trăm hai mươi lăm, giảm mười phẩy năm phần trăm. Lần ba, từ một nghìn chín trăm linh ba điểm ngày mười ba tháng '
         'một năm hai nghìn không trăm hai mươi sáu xuống một nghìn năm trăm chín mươi mốt điểm ngày hai mươi ba tháng ba năm hai nghìn không trăm hai mươi sáu, giảm '
         'mười sáu phẩy bốn phần trăm, kéo dài sáu mươi chín ngày. Lần bốn, từ một nghìn chín trăm hai mươi tám điểm ngày mười tám tháng năm năm hai nghìn không trăm '
         'hai mươi sáu xuống một nghìn sáu trăm sáu mươi chín điểm ngày hai mươi hai tháng bảy năm hai nghìn không trăm hai mươi sáu, giảm mười ba phẩy năm phần trăm. '
         'Để ý một điều: giảm nhanh nhất là lần một, nhưng kéo dài nhất là lần ba. Không có hai nhịp giảm nào giống hệt nhau, cả về độ sâu lẫn thời gian. Đó là lý do '
         'mọi kịch bản đoán trước đều khó chính xác.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Hồi phục mất bao lâu',
  'moc': True,
  'label': 'Số ngày từ đáy đến khi lấy lại đỉnh cũ',
  'cap': ('HỒI PHỤC', 'MẤT BAO LÂU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Lần 1', 48.0, (56, 189, 248), '48 ngày'), ('Lần 2', 43.0, (56, 189, 248), '43 ngày'), ('Lần 3', 45.0, (34, 197, 94), '45 ngày')],
  'anh': 'calendar clock',
  'say': 'Bước hai, hồi phục mất bao lâu. Sau lần một, chỉ số lấy lại đỉnh cũ ngày hai mươi bảy tháng năm năm hai nghìn không trăm hai mươi lăm, tức bốn mươi tám ngày '
         'kể từ đáy. Sau lần hai, mất bốn mươi ba ngày. Sau lần ba, mất bốn mươi lăm ngày, vào ngày bảy tháng năm năm hai nghìn không trăm hai mươi sáu. Cả ba lần đều '
         'quanh con số bốn mươi lăm ngày từ đáy, tức khoảng sáu đến bảy tuần. Nhưng em phải nói rõ: đây là quan sát trong một giai đoạn tăng trưởng, không phải quy '
         'luật. Lần bốn, đến ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu, chỉ số vẫn thấp hơn đỉnh ngày mười tám tháng năm năm hai nghìn không trăm '
         'hai mươi sáu khoảng mười phẩy bảy phần trăm, chưa lấy lại. Nghĩa là không ai biết lần giảm này kết thúc ở đâu. Nếu anh chị chỉ nhớ ba lần đã hồi mà quên lần '
         'bốn chưa hồi, anh chị đang chọn lọc ký ức theo hướng dễ chịu.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Bức tranh ba năm',
  'moc': True,
  'label': 'VN-Index từ 27/10/2023 đến 6/11/2026',
  'cap': ('BỨC TRANH', 'BA NĂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Điểm xuất phát', '1.061', '27/10/2023'), ('Đỉnh trong giai đoạn', '1.928', '18/5/2026'), ('Ngày 6/11/2026', '1.721', '+62% so với xuất phát')],
  'anh': 'growth chart',
  'say': 'Bước ba, nhìn bức tranh lớn. Ngày ngày hai mươi bảy tháng mười năm hai nghìn không trăm hai mươi ba VN-Index đóng cửa khoảng một nghìn không trăm sáu mươi mốt '
         'điểm. Ngày ngày sáu tháng mười một năm hai nghìn không trăm hai mươi sáu là khoảng một nghìn bảy trăm hai mươi mốt điểm, tăng khoảng sáu mươi hai phần trăm. '
         'Đỉnh cao nhất trong giai đoạn là một nghìn chín trăm hai mươi tám điểm ngày mười tám tháng năm năm hai nghìn không trăm hai mươi sáu, tức đã tăng khoảng tám '
         'mươi hai phần trăm từ điểm xuất phát. Trên đường đi, chỉ số trải qua bốn nhịp giảm trên mười phần trăm. Nhìn riêng từng nhịp thì rất đáng sợ, nhìn cả đoạn '
         'đường thì chúng chỉ là những vết lõm. Nhưng cũng đừng vội kết luận lúc nào cũng vậy. Chỉ số đại diện cả thị trường, còn từng cổ phiếu, từng danh mục có thể '
         'diễn biến rất khác.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Bốn bài học',
  'moc': True,
  'label': 'Bốn bài học sống chung với nhịp giảm',
  'cap': ('BỐN BÀI HỌC', 'LỊCH SỬ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Giảm 10% xảy ra khá thường xuyên', (255, 196, 0)),
            ('Không bán vì hoảng loạn ở đáy', (34, 197, 94)),
            ('Có kế hoạch cắt lỗ và tỷ trọng từ trước', (34, 197, 94)),
            ('Dùng tiền nhàn rỗi, không vay mượn', (34, 197, 94)),
            ('Góp đều đặn thay vì đoán đỉnh đáy', (34, 197, 94))],
  'anh': 'shield discipline',
  'say': 'Bước bốn, bốn bài học. Một, giảm mười phần trăm không phải chuyện lạ, nó xảy ra bốn lần trong chưa đầy ba năm. Nếu danh mục của anh chị không chịu nổi mức '
         'giảm đó, vấn đề là tỷ trọng và đòn bẩy, không phải thị trường. Hai, đừng bán vì hoảng loạn ở đáy. Ba lần hồi nhanh đều đến khi nhiều người đã bán. Ba, nhưng '
         'cũng đừng ôm hy vọng vô điều kiện, vì lần bốn vẫn chưa hồi, cần có kế hoạch cắt lỗ và tỷ trọng rõ ràng từ trước. Bốn, dùng tiền nhàn rỗi và góp đều đặn. Người '
         'góp đều mỗi tháng không cần đoán đỉnh đáy, họ mua cả lúc giá cao lẫn lúc giá thấp. Kỷ luật quan trọng hơn dự báo.'},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('GIẢM RỒI SAO?', 'CÓ KẾ HOẠCH CHƯA'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, những nhịp giảm trên mười phần trăm là một phần bình thường của thị trường. Điều quyết định kết quả là kế hoạch của anh chị trước khi nhịp giảm đến. '
         'Cảm ơn anh chị đã xem. Theo anh chị, trong bốn nhịp giảm vừa qua, anh chị đã hành động thế nào: bán, giữ hay mua thêm? Anh chị để lại ý kiến bên dưới giúp em '
         'nhé.'}]

S['CH1811A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'LPB – Đọc BCTC 5 phút',
  'cap': ('LÃI QUÝ +28,9%', 'LÕI LẠI GIẢM?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'LPBW', 'tf': 'W', 'weeks': 52, 'circles': [[51, 36.0, 'Tuần 2/11/26: 36,00', 1.0]]},
  'anh': 'bank building vietnam',
  'say': 'Một ngân hàng lãi quý ba tăng gần hai mươi chín phần trăm, nhưng thu nhập lãi thuần, phần cốt lõi nhất, lại giảm bảy phẩy bốn phần trăm. Hai con số ngược '
         'chiều nhau trong cùng một bản báo cáo. Vậy lợi nhuận tăng đến từ đâu, và có lặp lại được không? Video này em đọc báo cáo tài chính quý ba năm hai nghìn không '
         'trăm hai mươi sáu của LPB, mã LPB, theo năm bước: lợi nhuận, thu nhập lãi thuần, nguồn thu ngoài lãi, chi phí dự phòng cùng nợ xấu, và định giá. Xem hết, anh '
         'chị sẽ biết cách tách lợi nhuận lặp lại được khỏi lợi nhuận có thể chỉ xuất hiện một lần. Số liệu tính đến ngày năm tháng mười một năm hai nghìn không trăm '
         'hai mươi sáu, còn cách đọc thì dùng được nhiều năm. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ LPB (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q2/25', 2395.9, (56, 189, 248), '2.396'),
           ('Q3/25', 2762.0, (56, 189, 248), '2.762'),
           ('Q4/25', 3730.6, (56, 189, 248), '3.731'),
           ('Q1/26', 2279.2, (56, 189, 248), '2.279'),
           ('Q2/26', 2520.7, (56, 189, 248), '2.521'),
           ('Q3/26', 3561.5, (34, 197, 94), '3.562')],
  'anh': 'financial charts',
  'say': 'Bước một, lợi nhuận qua các quý. Quý ba năm hai nghìn không trăm hai mươi sáu LPB lãi sau thuế khoảng ba nghìn năm trăm sáu mươi hai tỷ đồng, tăng hai mươi '
         'tám phẩy chín phần trăm so với cùng kỳ năm trước là hai nghìn bảy trăm sáu mươi hai tỷ. So với quý hai là hai nghìn năm trăm hai mươi mốt tỷ thì tăng tới bốn '
         'mươi mốt phẩy ba phần trăm. Nhìn biểu đồ, quý ba là quý cao thứ hai trong sáu quý, chỉ sau quý bốn năm hai nghìn không trăm hai mươi lăm. Nhưng lũy kế chín '
         'tháng đạt tám nghìn ba trăm sáu mươi mốt tỷ, tăng chỉ tám phẩy bảy phần trăm. Nghĩa là các quý trước đó yếu hơn nhiều. Một quý bứt lên giữa những quý đi ngang '
         'là mẫu hình cần hỏi ngay một câu: khoản tăng này đến từ hoạt động kinh doanh thường xuyên, hay từ một khoản đặc biệt?'},
 {'k': 'bars',
  'ch': 'Chương 2 – Thu nhập lãi thuần',
  'moc': True,
  'label': 'Thu nhập lãi thuần LPB (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 4235.0, (56, 189, 248), '4.235'),
           ('Q4/25', 4781.4, (56, 189, 248), '4.781'),
           ('Q1/26', 3878.2, (56, 189, 248), '3.878'),
           ('Q2/26', 3888.3, (56, 189, 248), '3.888'),
           ('Q3/26', 3922.7, (239, 68, 68), '3.923')],
  'anh': 'financial charts',
  'say': 'Bước hai, thu nhập lãi thuần, động cơ chính của ngân hàng. Quý ba đạt khoảng ba nghìn chín trăm hai mươi ba tỷ, giảm bảy phẩy bốn phần trăm so với cùng kỳ là '
         'bốn nghìn hai trăm ba mươi lăm tỷ. So với hai quý liền trước thì gần như đi ngang, quanh ba nghìn chín trăm tỷ. Nhìn biểu đồ, thu nhập lãi thuần đã đi lùi so '
         'với đỉnh quý bốn năm hai nghìn không trăm hai mươi lăm là bốn nghìn bảy trăm tám mươi mốt tỷ, và từ đó đứng quanh mức thấp hơn. Đây là điểm mấu chốt. Lợi '
         'nhuận quý ba tăng hai mươi tám phẩy chín phần trăm trong khi thu nhập cốt lõi giảm, nghĩa là phần tăng đến từ nơi khác. Một ngân hàng lợi nhuận bền vững '
         'thường cần thu nhập lãi thuần tăng cùng chiều. Khi hai thứ ngược nhau, nhà đầu tư cần tìm ra phần chênh lệch nằm ở đâu.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Nguồn thu ngoài lãi và dự phòng',
  'moc': True,
  'label': 'Phần chênh lệch nằm ở đâu',
  'cap': ('NGOÀI LÃI', 'VÀ DỰ PHÒNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Lãi dịch vụ', '+297,9%', 'so với cùng kỳ'), ('Chi phí dự phòng', '+338,7%', 'so với cùng kỳ'), ('Thu nhập lãi thuần', '-7,4%', 'so với cùng kỳ')],
  'anh': 'insurance shield money',
  'say': 'Bước ba, nguồn thu ngoài lãi và chi phí dự phòng. Theo dữ liệu tổng hợp, mục lãi dịch vụ của LPB quý ba tăng hai trăm chín mươi bảy phẩy chín phần trăm. Đây '
         'là mức tăng rất lớn, và em lưu ý đó là con số cần đối chiếu với thuyết minh báo cáo để biết thành phần cụ thể. Cùng lúc, chi phí dự phòng tăng ba trăm ba mươi '
         'tám phẩy bảy phần trăm so với cùng kỳ. Ngân hàng vừa ghi nhận thu nhập ngoài lãi tăng vọt, vừa trích dự phòng tăng gấp hơn bốn lần. Một cách giải thích có thể '
         'là ngân hàng dùng phần thu thêm để làm dày bộ đệm, nhưng đó chỉ là suy đoán, em chưa có dữ liệu để khẳng định. Cách đọc đúng là xem phần lợi nhuận tăng thêm '
         'có phải khoản một lần không. Khoản một lần không sai, nhưng khi dự phóng các quý sau, anh chị không nên mặc định nó lặp lại.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Nợ xấu và bao phủ',
  'moc': True,
  'label': 'Bao phủ nợ xấu (%) – Q3/2026',
  'cap': ('BAO PHỦ', 'NỢ XẤU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('VIB', 42.0, (56, 189, 248), '42%'),
           ('HDB', 46.0, (56, 189, 248), '46%'),
           ('MSB', 47.0, (56, 189, 248), '47%'),
           ('VPB', 54.0, (56, 189, 248), '54%'),
           ('TPB', 57.0, (56, 189, 248), '57%'),
           ('OCB', 58.0, (56, 189, 248), '58%'),
           ('LPB', 63.0, (34, 197, 94), '63%')],
  'anh': 'bank vault',
  'say': 'Bước bốn, nợ xấu và bao phủ. Tỷ lệ nợ xấu của LPB quý ba là một phẩy tám mươi bảy phần trăm, thấp hơn đa số ngân hàng trong dữ liệu của em. Bao phủ nợ xấu '
         'khoảng sáu mươi ba phần trăm, cao nhất trong bảy ngân hàng em so sánh. Đây là điểm cộng thật sự. Nợ xấu thấp và bộ đệm tương đối dày cho thấy chất lượng tài '
         'sản ở mức tốt. Khoản dự phòng tăng mạnh ở bước ba cũng không mâu thuẫn với bức tranh này. Nhưng nhớ rằng bao phủ cao không bù được cho việc thu nhập cốt lõi '
         'không tăng. Hai thứ đo hai khía cạnh khác nhau: một là sức khỏe tài sản, một là sức kiếm tiền thường xuyên.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Hiệu quả và định giá',
  'moc': True,
  'label': 'Hiệu quả và định giá LPB',
  'cap': ('ĐỊNH GIÁ', 'LPB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('ROE', '26,3%', 'nhóm cao nhất'), ('P/E', '9,0 lần', 'dữ liệu 5/11/2026'), ('P/B', '2,34 lần', 'cao hơn nhiều mã khác')],
  'anh': 'finance',
  'say': 'Bước năm, hiệu quả và định giá. ROE của LPB khoảng hai mươi sáu phẩy ba phần trăm, thuộc nhóm cao nhất trong các ngân hàng em theo dõi. P/E khoảng chín lần và '
         'P/B khoảng hai phẩy ba mươi bốn lần theo dữ liệu tổng hợp ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu. P/B cao hơn nhiều ngân hàng khác, '
         'nhưng ROE cao cũng giải thích một phần. Quy tắc quen thuộc: P/B và ROE đi cùng nhau. Tuy vậy, ROE tính trên lợi nhuận bốn quý gần nhất, mà lợi nhuận quý ba có '
         'thể chứa khoản đặc biệt. Nên nếu muốn thận trọng, anh chị có thể tự tính lại ROE khi loại bỏ phần tăng bất thường, rồi so lại với P/B. Đó là cách đọc có chiều '
         'sâu hơn là chỉ nhìn ROE bề mặt.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Ghép các mảnh lại',
  'moc': True,
  'label': 'Lợi nhuận tăng 28,9% – bền hay một lần?',
  'cap': ('GHÉP LẠI', 'CẢ BỨC TRANH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lợi nhuận quý tăng 28,9%', (34, 197, 94)),
            ('Nợ xấu chỉ 1,87%', (34, 197, 94)),
            ('Bao phủ 63%, cao nhất nhóm', (34, 197, 94)),
            ('Thu nhập lãi thuần giảm 7,4%', (239, 68, 68)),
            ('Tăng trưởng nhờ nguồn thu ngoài lãi', (239, 68, 68)),
            ('P/B 2,34 lần cao hơn mặt bằng', (255, 196, 0))],
  'anh': 'scales balance',
  'say': 'Ghép các mảnh lại. Điểm tích cực: lợi nhuận quý tăng hai mươi tám phẩy chín phần trăm, nợ xấu một phẩy tám mươi bảy phần trăm thấp, bao phủ sáu mươi ba phần '
         'trăm cao nhất nhóm, ROE cao. Điểm cần theo dõi: thu nhập lãi thuần giảm bảy phẩy bốn phần trăm, lợi nhuận tăng nhờ nguồn thu ngoài lãi, và P/B cao hơn mặt '
         'bằng. Kết luận trung thực: LPB có chất lượng tài sản tốt, nhưng lợi nhuận quý ba có thể chưa phản ánh sức kiếm tiền thường xuyên. Bài học cho mọi ngân hàng '
         'khác: khi lợi nhuận và thu nhập lãi thuần đi ngược chiều, hãy đào sâu thuyết minh trước khi kết luận.'},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('LÃI TĂNG', 'CHƯA CHẮC BỀN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, lợi nhuận tăng mạnh chưa chắc bền. Hãy tách phần lõi lặp lại được khỏi phần có thể chỉ xuất hiện một lần. Cảm ơn anh chị đã xem. Theo anh chị, với '
         'ngân hàng lãi tăng nhờ thu ngoài lãi nhưng thu nhập cốt lõi đi ngang, anh chị tin vào lợi nhuận hay tin vào thu nhập cốt lõi hơn? Anh chị để lại ý kiến bên '
         'dưới giúp em nhé.'}]

S['CH1811B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'BSR – Đọc BCTC 5 phút',
  'cap': ('P/E CHỈ 4,75', 'RẺ HAY BẪY?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'BSRW', 'tf': 'W', 'weeks': 52, 'circles': [[51, 26.9, 'Tuần 2/11/26: 26,90', 1.0]]},
  'anh': 'oil refinery',
  'say': 'Một cổ phiếu có P/E chỉ khoảng bốn phẩy bảy mươi lăm, ROE hơn bốn mươi phần trăm, lợi nhuận quý ba tăng gần mười lần so với cùng kỳ. Rẻ đến mức khó tin, đúng '
         'không anh chị? Chính những cổ phiếu như vậy là nơi nhà đầu tư dễ mắc sai lầm nhất. Video này em đọc báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi '
         'sáu của BSR, mã BSR, một doanh nghiệp lọc dầu, theo bốn bước: lợi nhuận qua các quý, nguồn gốc của mức tăng, ba cách tính P/E, và cách đọc cổ phiếu chu kỳ. '
         'Xem hết, anh chị sẽ hiểu vì sao với cổ phiếu chu kỳ, P/E thấp nhất thường xuất hiện đúng lúc lợi nhuận cao nhất. Số liệu tính đến ngày năm tháng mười một năm '
         'hai nghìn không trăm hai mươi sáu. Biểu đồ phía sau chỉ là hình nền minh họa.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Lợi nhuận qua các quý',
  'moc': True,
  'label': 'LNST công ty mẹ BSR (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q1/25', 398.7, (56, 189, 248), '399'),
           ('Q2/25', 845.7, (56, 189, 248), '846'),
           ('Q3/25', 907.5, (56, 189, 248), '908'),
           ('Q4/25', 3061.7, (56, 189, 248), '3.062'),
           ('Q1/26', 8264.7, (56, 189, 248), '8.265'),
           ('Q2/26', 7666.1, (56, 189, 248), '7.666'),
           ('Q3/26', 8968.0, (34, 197, 94), '8.968')],
  'anh': 'financial charts',
  'say': 'Bước một, lợi nhuận qua các quý. Quý ba năm hai nghìn không trăm hai mươi sáu BSR lãi sau thuế khoảng tám nghìn chín trăm sáu mươi tám tỷ đồng, gấp khoảng '
         'chín phẩy chín lần cùng kỳ là chín trăm linh tám tỷ. Lũy kế chín tháng đạt hai mươi bốn nghìn tám trăm chín mươi chín tỷ, gấp khoảng mười một phẩy sáu lần '
         'cùng kỳ. Nhưng hãy nhìn cả chuỗi. Nửa đầu năm hai nghìn không trăm hai mươi lăm, lợi nhuận mỗi quý chỉ vài trăm tỷ. Từ quý bốn năm hai nghìn không trăm hai '
         'mươi lăm mới nhảy lên hơn ba nghìn tỷ, rồi hơn tám nghìn tỷ. Ba quý gần nhất đều ở quanh mức tám nghìn tỷ. Một doanh nghiệp mà lợi nhuận một quý bằng cả năm '
         'trước cộng lại là một doanh nghiệp đang ở giữa một chu kỳ rất đặc biệt, và câu hỏi quan trọng nhất là chu kỳ đó kéo dài bao lâu.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Mức tăng đến từ đâu',
  'moc': True,
  'label': 'Doanh thu tăng, nhưng biên lợi nhuận mới là chìa khóa',
  'cap': ('DOANH THU', 'VÀ BIÊN GỘP'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Doanh thu thuần', '+68,8%', 'so với cùng kỳ'), ('Lợi nhuận quý', '~9,9 lần', 'so với cùng kỳ'), ('Biên gộp', '16,2%', 'cùng kỳ 2,9%')],
  'anh': 'crude oil',
  'say': 'Bước hai, mức tăng đến từ đâu. Doanh thu thuần quý ba đạt khoảng năm mươi chín nghìn năm trăm tám mươi mốt tỷ, tăng sáu mươi tám phẩy tám phần trăm. Trong khi '
         'đó lợi nhuận tăng gần mười lần. Hai con số lệch nhau rất xa, nghĩa là phần lớn mức tăng không đến từ bán được nhiều hơn mà đến từ biên lợi nhuận. Biên lợi '
         'nhuận gộp quý ba khoảng mười sáu phẩy hai phần trăm, trong khi cùng kỳ chỉ hai phẩy chín phần trăm. Với doanh nghiệp lọc dầu, lợi nhuận phụ thuộc vào chênh '
         'lệch giữa giá sản phẩm bán ra và giá dầu thô mua vào. Chênh lệch này biến động mạnh theo thị trường năng lượng thế giới, và doanh nghiệp gần như không điều '
         'khiển được. Em không đi vào nguyên nhân cụ thể của mức tăng biên, vì báo cáo không nói rõ hết. Điều cần nhớ là: biên mười sáu phẩy hai phần trăm đã cao gấp '
         'hơn năm lần mức một năm trước, và biên như vậy hiếm khi đứng yên mãi.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Ba cách tính P/E',
  'moc': True,
  'label': 'Cùng một cổ phiếu, ba con số P/E',
  'cap': ('BA CÁCH TÍNH', 'P/E'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('4 quý gần nhất', '4,75 lần', 'con số trên bảng giá'),
            ('Trung bình 12 quý', '~12,1 lần', 'nếu lợi nhuận về mức TB'),
            ('Quý 3 nhân 4', '~3,7 lần', 'nếu lặp lại mãi')],
  'anh': 'calculator',
  'say': 'Bước ba, ba cách tính P/E. Vốn hóa BSR khoảng một trăm ba mươi hai nghìn bảy trăm tỷ đồng. Cách một, chia cho lợi nhuận bốn quý gần nhất, tổng khoảng hai mươi '
         'bảy nghìn chín trăm sáu mươi tỷ, ra P/E khoảng bốn phẩy bảy mươi lăm lần. Đây chính là con số thường thấy trên các bảng giá. Cách hai, giả sử lợi nhuận quay '
         'về mức trung bình của mười hai quý gần nhất, khoảng hai nghìn bảy trăm năm mươi hai tỷ mỗi quý, tức khoảng mười một nghìn tỷ mỗi năm. Khi đó P/E khoảng mười '
         'hai phẩy một lần, gấp hơn hai lần rưỡi. Cách ba, giả sử quý ba lặp lại bốn lần, ba mươi lăm nghìn tám trăm bảy mươi hai tỷ, P/E chỉ khoảng ba phẩy bảy lần. Em '
         'nhấn mạnh đây là phép tính minh họa, không phải dự báo. Điều nó cho thấy là con số P/E bốn phẩy bảy mươi lăm nằm giữa hai kịch bản rất xa nhau, và thị trường '
         'đang đặt cược vào kịch bản nào chính là câu hỏi cốt lõi.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Cách đọc cổ phiếu chu kỳ',
  'moc': True,
  'label': 'Bốn nguyên tắc đọc cổ phiếu chu kỳ',
  'cap': ('CỔ PHIẾU', 'CHU KỲ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Tính P/E cả với lợi nhuận trung bình nhiều quý', (34, 197, 94)),
            ('Tìm nguyên nhân của mức tăng biên', (34, 197, 94)),
            ('Xem ROE nhiều năm, không chỉ năm nay', (34, 197, 94)),
            ('Đặt kịch bản biên quay về mức cũ', (255, 196, 0)),
            ('P/E thấp ở đỉnh chu kỳ: thận trọng', (239, 68, 68))],
  'anh': 'cycle chart',
  'say': 'Bước bốn, cách đọc cổ phiếu chu kỳ. Một, đừng tin P/E của một quý lợi nhuận đỉnh, hãy tính cả với lợi nhuận trung bình nhiều quý. Hai, tìm nguyên nhân của mức '
         'tăng biên: nếu là yếu tố bên ngoài, giá thế giới, thì khó kéo dài hơn lợi thế nội tại. Ba, nhìn ROE nhiều năm. ROE khoảng bốn mươi phẩy năm phần trăm hôm nay '
         'là kết quả của một chu kỳ đặc biệt, so sánh với những năm lợi nhuận thấp mới thấy bức tranh đầy đủ. Bốn, đặt kịch bản xấu trước: nếu biên quay về mức cũ, lợi '
         'nhuận còn bao nhiêu, và giá đang phản ánh điều đó chưa. Nhớ quy tắc cũ của thị trường: ở cổ phiếu chu kỳ, P/E thấp thường là lời cảnh báo chứ không phải lời '
         'mời.'},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('P/E THẤP', 'CHƯA CHẮC RẺ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, với cổ phiếu chu kỳ, hãy hỏi lợi nhuận này bền bao lâu trước khi hỏi P/E bao nhiêu. Cảm ơn anh chị đã xem. Theo anh chị, nên tin P/E bốn quý gần nhất '
         'hay tính lại theo lợi nhuận trung bình nhiều năm? Anh chị để lại ý kiến bên dưới giúp em nhé.'}]

S['CH1811C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'Quy trình đọc một cổ phiếu',
  'cap': ('10 GIÂY ĐỂ MUA', '10 PHÚT ĐỂ ĐỌC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'ACBW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[35, 23.85, 'Đỉnh tuần 13/7/26: 23,85', 0.6], [17, 18.7, 'Đáy tuần 9/3/26: 18,70', 1.6], [51, 20.3, 'Tuần 2/11/26: 20,30', 2.6]]},
  'anh': 'person reading phone',
  'say': 'Mua một cổ phiếu mất mười giây, chỉ cần vài cú chạm trên điện thoại. Nhưng để hiểu mình đang mua gì, cần bao lâu? Phần lớn người mới dành cho việc đó chưa đến '
         'mười phút, thậm chí không có. Video này em chia sẻ một quy trình sáu bước, vừa đủ mười phút, để đọc một cổ phiếu trước khi quyết định: doanh nghiệp kiếm tiền '
         'thế nào, chuỗi lợi nhuận, chất lượng lợi nhuận, rủi ro riêng của ngành, định giá, và kịch bản sai. Xem hết, anh chị sẽ có một danh sách có thể dùng cho bất kỳ '
         'cổ phiếu nào, bất kỳ năm nào. Ví dụ trong video lấy từ số liệu quý ba năm hai nghìn không trăm hai mươi sáu và chỉ để minh họa cách làm. Biểu đồ phía sau chỉ '
         'là hình nền minh họa.'},
 {'k': 'cards',
  'ch': 'Bước 1 và 2 – Kiếm tiền thế nào, chuỗi lợi nhuận',
  'moc': True,
  'label': 'Hai bước đầu: 3 phút',
  'cap': ('HAI BƯỚC ĐẦU', 'BA PHÚT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Bước 1', 'Kiếm tiền thế nào', 'viết được 1 câu'), ('Bước 2', 'Chuỗi 8 đến 12 quý', 'không đọc 1 quý'), ('Thời gian', '3 phút', 'xem trên bảng số')],
  'anh': 'notebook writing',
  'say': 'Bước một, một phút: doanh nghiệp kiếm tiền bằng cách nào. Hãy tự trả lời bằng một câu, ví dụ ngân hàng kiếm tiền từ chênh lệch giữa lãi cho vay và lãi huy '
         'động. Nếu anh chị không viết nổi một câu, anh chị chưa nên mua. Bước hai, hai phút: nhìn chuỗi lợi nhuận tám đến mười hai quý, không chỉ một quý. Một quý tăng '
         'mạnh chỉ có ý nghĩa khi đặt trong chuỗi. Hãy tự hỏi: lợi nhuận đang tăng đều, đi ngang, hay chỉ vừa nhảy lên từ một nền rất thấp? Hai bước này nghe đơn giản, '
         'nhưng đã loại được rất nhiều quyết định mua theo tin đồn.'},
 {'k': 'cards',
  'ch': 'Bước 3 – Chất lượng lợi nhuận',
  'moc': True,
  'label': 'Lợi nhuận tăng có đồng nghĩa lõi tăng?',
  'cap': ('CHẤT LƯỢNG', 'LỢI NHUẬN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Thu nhập lãi thuần', '+21,1%', 'ACB, Q3/2026'), ('Lợi nhuận sau thuế', '+9,8%', 'ACB, Q3/2026'), ('Chi phí dự phòng', '+223,2%', 'ACB, Q3/2026')],
  'anh': 'financial charts',
  'say': 'Bước ba, hai phút: chất lượng lợi nhuận. Ví dụ từ quý ba năm hai nghìn không trăm hai mươi sáu, ACB có thu nhập lãi thuần tăng hai mươi mốt phẩy một phần '
         'trăm, nhưng lợi nhuận sau thuế chỉ tăng chín phẩy tám phần trăm vì chi phí dự phòng tăng tới hai trăm hai mươi ba phẩy hai phần trăm. Hai con số khác nhau kể '
         'hai câu chuyện khác nhau. Với bất kỳ cổ phiếu nào, hãy so lợi nhuận với doanh thu hoặc thu nhập lõi, và so lợi nhuận với dòng tiền kinh doanh. Lợi nhuận tăng '
         'nhanh hơn doanh thu rất nhiều, hoặc lợi nhuận dương mà dòng tiền âm kéo dài, là hai dấu hiệu cần đọc kỹ thuyết minh trước khi tiếp tục.'},
 {'k': 'checklist',
  'ch': 'Bước 4 – Rủi ro riêng của ngành',
  'moc': True,
  'label': 'Mỗi ngành có một con số cần soi',
  'cap': ('RỦI RO', 'RIÊNG NGÀNH'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Ngân hàng: nợ xấu, bao phủ nợ xấu', (34, 197, 94)),
            ('Thép, dầu khí: biên gộp, giá hàng hóa', (34, 197, 94)),
            ('Bán lẻ, sản xuất: tồn kho, khoản phải thu', (34, 197, 94)),
            ('Bất động sản: nợ vay, tiền ứng trước', (34, 197, 94)),
            ('Chứng khoán: tỷ trọng lãi từ tự doanh', (34, 197, 94))],
  'anh': 'industry factory',
  'say': 'Bước bốn, hai phút: rủi ro riêng của ngành. Mỗi ngành có một con số mà nhà đầu tư lâu năm luôn soi trước. Ngân hàng: nợ xấu và bao phủ nợ xấu. Doanh nghiệp '
         'chu kỳ như thép, dầu khí: biên lợi nhuận gộp và giá hàng hóa. Bán lẻ và sản xuất: hàng tồn kho và khoản phải thu. Bất động sản: nợ vay và tiền khách hàng ứng '
         'trước. Chứng khoán: lợi nhuận từ tự doanh có đang chiếm quá lớn không. Anh chị không cần biết hết, chỉ cần biết con số quan trọng nhất của ngành mình đang '
         'xem.'},
 {'k': 'bars',
  'ch': 'Bước 5 – Định giá có điều kiện',
  'moc': True,
  'label': 'P/B của sáu ngân hàng (lần) – ROE đi kèm',
  'cap': ('P/B ĐI THEO', 'ROE'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('OCB', 0.9, (56, 189, 248), '0,90'),
           ('VIB', 1.06, (56, 189, 248), '1,06'),
           ('ACB', 1.15, (56, 189, 248), '1,15'),
           ('MBB', 1.25, (56, 189, 248), '1,25'),
           ('HDB', 1.63, (56, 189, 248), '1,63'),
           ('LPB', 2.34, (34, 197, 94), '2,34')],
  'anh': 'finance',
  'say': 'Bước năm, hai phút: định giá, nhưng có điều kiện. Đừng nhìn P/E hay P/B một mình, hãy đặt cạnh ROE và so trong cùng ngành. Biểu đồ cho thấy P/B của sáu ngân '
         'hàng, theo dữ liệu ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu. OCB có P/B khoảng không phẩy chín mươi với ROE khoảng mười ba phần trăm. VIB '
         'P/B một phẩy không sáu, ROE mười sáu phẩy hai phần trăm. ACB P/B một phẩy mười lăm, ROE mười sáu phẩy năm phần trăm. MBB P/B một phẩy hai mươi lăm, ROE hai '
         'mươi mốt phẩy tám phần trăm. HDB P/B một phẩy sáu mươi ba, ROE hai mươi ba phẩy ba phần trăm. LPB P/B hai phẩy ba mươi bốn, ROE hai mươi sáu phẩy ba phần '
         'trăm. Nhìn chung, ROE càng cao thì thị trường càng trả P/B cao. Vậy P/B thấp không tự động là rẻ, nó thường phản ánh ROE thấp. Rẻ thật sự chỉ khi P/B thấp mà '
         'ROE vẫn cao và bền.'},
 {'k': 'checklist',
  'ch': 'Bước 6 – Kịch bản sai',
  'moc': True,
  'label': 'Viết trước: tôi sai nếu...',
  'cap': ('TÔI SAI NẾU', '...'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Tôi sẽ sai nếu nợ xấu tăng 2 quý liền', (255, 196, 0)),
            ('Tôi sẽ sai nếu biên gộp quay về mức cũ', (255, 196, 0)),
            ('Có mức cắt lỗ và tỷ trọng định sẵn', (34, 197, 94)),
            ('Ghi lại quyết định vào nhật ký', (34, 197, 94))],
  'anh': 'checklist',
  'say': 'Bước sáu, một phút: viết kịch bản sai. Trước khi mua, hãy viết một câu bắt đầu bằng chữ: tôi sẽ sai nếu. Ví dụ: tôi sẽ sai nếu nợ xấu tiếp tục tăng hai quý '
         'liền, hoặc tôi sẽ sai nếu biên lợi nhuận quay về mức cũ. Câu này làm hai việc. Một, nó buộc anh chị hiểu điều gì thật sự quan trọng với doanh nghiệp. Hai, nó '
         'cho anh chị lý do rõ ràng để thay đổi quyết định, thay vì ở lại chỉ vì không muốn nhận mình đã sai. Kèm theo đó là mức cắt lỗ và tỷ trọng đã định sẵn.'},
 {'k': 'end',
  'ch': '',
  'moc': True,
  'label': '',
  'cap': ('SÁU BƯỚC', 'MƯỜI PHÚT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Tóm lại, sáu bước, mười phút: kiếm tiền thế nào, chuỗi lợi nhuận, chất lượng lợi nhuận, rủi ro riêng của ngành, định giá có điều kiện, và kịch bản sai. Cảm ơn '
         'anh chị đã xem. Theo anh chị, bước nào trong sáu bước này anh chị hay bỏ qua nhất? Anh chị để lại ý kiến bên dưới giúp em nhé.'}]

