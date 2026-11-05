# -*- coding: utf-8 -*-
# VIDEO DÀI KÊNH CHÍNH – NV1 soạn 05/11/2026 (lô 20261105_2359: CH0811A–CH1011C). Nến tuần: px_tuan.json.
GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)

S = {}

S['CH0811A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VNM – minh họa quyền & thưởng',
  'cap': ('CHIA THƯỞNG 20%', '= LÃI 20%? SAI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNMW', 'tf': 'W', 'weeks': 52, 'circles': [[0, 54.52, 'Đáy tuần 3/11/25: 54,52', 0.6], [11, 73.11, 'Đỉnh tuần 19/1/26: 73,11', 1.6], [51, 57.5, '5/11/26: 57,50', 2.6]]},
  'anh': 'stock certificate dividend',
  'say': 'Bạn có một nghìn cổ phiếu, giá ba mươi nghìn đồng, tức là ba mươi triệu. Công ty thông báo thưởng hai mươi phần trăm bằng cổ phiếu. Bạn mừng vì nhận thêm hai trăm cổ phiếu. Nhưng sáng hôm '
         'sau, giá trên bảng điện chỉ còn khoảng hai mươi lăm nghìn đồng, giảm gần mười bảy phần trăm mà không ai bán gì cả. Vậy tài sản của bạn đã tăng, giảm, hay đứng yên? Con số ở cuối ví dụ này '
         'làm rất nhiều người mới ngạc nhiên. Trong video này mình giải thích từng sự kiện, từ ngày giao dịch không hưởng quyền, cổ phiếu thưởng, chia tách đến quyền mua và pha loãng, bằng số tính '
         'tay để bạn tự kiểm lại. Xem đến hết, bạn sẽ biết sự kiện nào làm tài sản thật sự thay đổi và sự kiện nào chỉ là đổi cách đếm. Video thuộc seri Nền tảng đầu tư, nội dung được chọn để mười '
         'năm nữa xem lại vẫn đúng. Các cổ phiếu trên biểu đồ chỉ là hình nền minh họa, ví dụ số trong bài là số giả định.'},
 {'k': 'checklist',
  'ch': 'Chương 1 – Ngày giao dịch không hưởng quyền',
  'moc': True,
  'label': 'Ba mốc ngày của một sự kiện quyền',
  'cap': ('3 MỐC NGÀY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Ngày giao dịch không hưởng quyền', (56, 189, 248)),
            ('Ngày đăng ký cuối cùng', (56, 189, 248)),
            ('Ngày thực hiện, tiền hoặc cổ phiếu về tài khoản', (34, 197, 94)),
            ('Giá tham chiếu được điều chỉnh ngay đầu ngày không hưởng quyền', (255, 196, 0))],
  'anh': 'stock exchange trading board',
  'say': 'Mỗi sự kiện chia cổ tức, thưởng cổ phiếu hay phát hành quyền mua đều có ba mốc ngày. Mốc quan trọng nhất là ngày giao dịch không hưởng quyền. Từ ngày này trở đi, ai mua cổ phiếu sẽ không '
         'còn được hưởng quyền nữa, vì danh sách cổ đông đã chốt trước đó hai ngày làm việc. Vì vậy sàn giao dịch điều chỉnh giá tham chiếu giảm xuống đúng bằng giá trị của quyền được chia. Đây là '
         'điểm đầu tiên cần nhớ: giá giảm vào ngày đó là điều chỉnh kỹ thuật, không phải tin xấu. Ví dụ cổ tức tiền mặt một nghìn đồng mỗi cổ phiếu, giá đóng cửa hôm trước ba mươi nghìn, thì giá '
         'tham chiếu hôm sau là hai mươi chín nghìn. Bạn mất một nghìn trên giá nhưng nhận một nghìn tiền mặt, tổng tài sản không đổi. Mốc thứ ba là ngày thực hiện, khi tiền hoặc cổ phiếu thật sự về '
         'tài khoản, thường cách ngày chốt vài tuần.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Cổ phiếu thưởng: chia bánh thành nhiều miếng',
  'moc': True,
  'label': 'Ví dụ giả định: 1.000 cổ phiếu, giá 30.000 đồng, thưởng 20%',
  'cap': ('THƯỞNG 20%',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Trước', '1.000 cổ phiếu', 'giá 30.000 đ = 30 triệu'), ('Sau', '1.200 cổ phiếu', 'giá về 25.000 đ'), ('Giá trị', '30 triệu', 'không đổi, chỉ đổi cách đếm')],
  'anh': 'cake slices sharing',
  'say': 'Cổ phiếu thưởng giống như bạn có một chiếc bánh cắt thành mười miếng, giờ nhà bếp cắt lại thành mười hai miếng nhưng chiếc bánh vẫn chỉ một. Công ty không đưa thêm tiền vào, mà chuyển một '
         'phần lợi nhuận giữ lại thành vốn điều lệ. Số cổ phiếu của bạn tăng từ một nghìn lên một nghìn hai trăm, còn giá tham chiếu chia cho một phẩy hai, từ ba mươi nghìn xuống hai mươi lăm nghìn. '
         'Nhân lại, một nghìn hai trăm nhân hai mươi lăm nghìn vẫn là ba mươi triệu. Điều thay đổi thật sự nằm ở chỗ khác: lợi nhuận trên mỗi cổ phiếu, tức EPS, bị chia nhỏ ra, và cổ tức tiền mặt '
         'trong tương lai sẽ chia cho nhiều cổ phiếu hơn. Cổ phiếu thưởng chỉ tốt khi doanh nghiệp tiếp tục tăng lợi nhuận đủ nhanh để bù phần chia nhỏ này. Nếu không, thưởng chỉ là cảm giác nhiều '
         'hơn chứ không phải giàu hơn.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Chia tách cổ phiếu: đổi tờ tiền lớn thành tiền lẻ',
  'moc': True,
  'label': 'Ví dụ giả định: chia tách 1 thành 2',
  'cap': ('CHIA TÁCH',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Trước', '100 cổ phiếu', 'giá 100.000 đ = 10 triệu'), ('Sau', '200 cổ phiếu', 'giá 50.000 đ'), ('Khác thưởng', 'không đụng lợi nhuận giữ lại', 'chỉ đổi mệnh giá')],
  'anh': 'coins and banknotes change',
  'say': 'Chia tách cổ phiếu còn đơn giản hơn nữa. Bạn đổi một tờ một trăm nghìn lấy hai tờ năm mươi nghìn. Số cổ phiếu tăng gấp đôi, giá giảm một nửa, tài sản không đổi. Về mặt kế toán, chia tách '
         'đổi mệnh giá, còn thưởng cổ phiếu chuyển lợi nhuận giữ lại sang vốn. Tại sao công ty làm vậy? Vì giá quá cao khiến nhà đầu tư nhỏ khó mua đủ lô, thanh khoản giảm. Chia nhỏ giá giúp nhiều '
         'người tham gia hơn. Nhưng hãy nhớ nguyên tắc chung: những sự kiện chỉ thay đổi số lượng và giá mà không có tiền mới vào hay ra thì không làm bạn giàu lên. Nếu một bài đăng nói chia tách là '
         'tin vui khiến giá sẽ nhân đôi, hãy tính lại bằng phép nhân đơn giản trong video này. Thị trường có thể phản ứng theo tâm lý, nhưng giá trị gốc thì chưa đổi.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Quyền mua: được quyền, không phải được tiền',
  'moc': True,
  'label': 'Ví dụ giả định: quyền mua 10:2 ở giá 20.000, thị giá 30.000',
  'cap': ('QUYỀN MUA',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Quyền', 'cứ 10 cổ phiếu', 'mua thêm 2 ở giá 20.000 đ'), ('Giá lý thuyết sau', '28.333 đ', '(10×30.000 + 2×20.000) / 12'), ('Giá trị 1 quyền', 'khoảng 1.667 đ', '30.000 − 28.333')],
  'anh': 'person signing share purchase form',
  'say': 'Quyền mua khác hẳn hai loại trên, vì lần này có tiền thật chảy vào công ty. Giả sử cứ mười cổ phiếu được quyền mua hai cổ phiếu mới ở giá hai mươi nghìn, trong khi thị giá là ba mươi '
         'nghìn. Sau khi phát hành, giá lý thuyết là trung bình có trọng số: mười nhân ba mươi nghìn cộng hai nhân hai mươi nghìn, chia cho mười hai, ra khoảng hai mươi tám nghìn ba trăm. Mỗi quyền '
         'mua vì vậy có giá trị khoảng một nghìn sáu trăm sáu mươi bảy đồng. Có hai lựa chọn hợp lý. Một là nộp tiền mua thêm để giữ nguyên tỷ lệ sở hữu. Hai là bán quyền trên thị trường nếu được '
         'phép, để bù phần giá bị giảm. Điều không nên làm là để quyền hết hạn mà không làm gì, vì bạn sẽ mất phần giá trị đó và bị pha loãng tỷ lệ sở hữu. Quyền mua là một quyền chọn, không phải '
         'món quà.'},
 {'k': 'bars',
  'ch': 'Chương 5 – Pha loãng: miếng bánh của bạn nhỏ đi bao nhiêu',
  'moc': True,
  'label': 'Tỷ lệ sở hữu của cổ đông giữ 1.000 cổ phiếu khi công ty phát hành thêm (giả định)',
  'cap': ('PHA LOÃNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Trước: 1.000/10 triệu', 0.01, (56, 189, 248), '0,010%'), ('Phát thêm 20%, không mua', 0.0083, (239, 68, 68), '0,0083%'), ('Phát thêm 20%, mua đủ', 0.01, (34, 197, 94), '0,010%')],
  'anh': 'pie chart ownership',
  'say': 'Pha loãng là hệ quả chung của mọi lần công ty phát hành thêm cổ phiếu mà bạn không tham gia. Hãy xem một cổ đông giữ một nghìn trên tổng mười triệu cổ phiếu, tức không phẩy không mười phần '
         'trăm công ty. Nếu công ty phát hành thêm hai mươi phần trăm, tổng số lên mười hai triệu. Nếu bạn không mua thêm, tỷ lệ sở hữu của bạn còn khoảng không phẩy không không tám ba phần trăm, '
         'tức giảm khoảng mười bảy phần trăm. Nếu bạn mua đủ phần quyền của mình thì tỷ lệ giữ nguyên. Pha loãng không phải lúc nào cũng xấu. Nếu số tiền thu về được dùng để đầu tư nhà máy cho lợi '
         'nhuận tăng nhanh hơn mức pha loãng, cổ đông vẫn có lợi. Câu hỏi cần đặt luôn là tiền mới được dùng vào đâu và lợi nhuận trên mỗi cổ phiếu sẽ thay đổi thế nào.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Cổ tức bằng cổ phiếu và thuế',
  'moc': True,
  'label': 'Những điều hay bị bỏ qua',
  'cap': ('CHI TIẾT HAY SÓT',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Cổ tức bằng cổ phiếu giống thưởng: không có tiền về', (56, 189, 248)),
            ('Cổ tức tiền mặt chịu thuế thu nhập cá nhân', (239, 68, 68)),
            ('Lẻ cổ phiếu thường được làm tròn xuống', (239, 68, 68)),
            ('Luôn đọc thông báo chính thức của công ty và sở giao dịch', (34, 197, 94))],
  'anh': 'accountant tax documents',
  'say': 'Có vài chi tiết nhỏ nhưng làm người mới mất tiền oan. Cổ tức bằng cổ phiếu có bản chất giống cổ phiếu thưởng: bạn nhận thêm cổ phiếu, không nhận được tiền, và giá tham chiếu giảm tương '
         'ứng. Cổ tức bằng tiền mặt thì bị khấu trừ thuế thu nhập cá nhân theo quy định hiện hành, nên số tiền thực nhận thấp hơn con số công bố. Phần lẻ cổ phiếu khi chia thường được làm tròn '
         'xuống. Ví dụ bạn có một trăm cổ phiếu, tỷ lệ thưởng mười lăm phần trăm sẽ cho mười lăm cổ phiếu, nhưng nếu có mười ba cổ phiếu thì phần lẻ có thể bị bỏ. Mức thuế và quy định có thể thay '
         'đổi theo thời gian, vì vậy hãy luôn đọc thông báo chính thức của công ty và sở giao dịch trước khi tính toán. Video này chỉ giải thích nguyên lý, không thay thế tư vấn thuế.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Bảng ghi nhớ nhanh',
  'moc': True,
  'label': 'Bốn sự kiện, bốn câu hỏi',
  'cap': ('BẢNG GHI NHỚ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Cổ tức tiền: tiền ra khỏi công ty vào tay bạn', (34, 197, 94)),
            ('Thưởng và chia tách: số lượng tăng, giá giảm, giá trị đứng yên', (56, 189, 248)),
            ('Quyền mua: cần tiền thật, có thể bán quyền', (255, 196, 0)),
            ('Phát hành riêng lẻ: hỏi giá và mục đích dùng vốn', (239, 68, 68))],
  'anh': 'notebook checklist pen',
  'say': 'Hãy ghi nhớ bằng một bảng đơn giản. Cổ tức tiền mặt là tiền chuyển từ công ty sang túi bạn, giá giảm đúng bằng số tiền chia. Cổ phiếu thưởng và chia tách chỉ đổi cách đếm, số lượng tăng, '
         'giá giảm, giá trị đứng yên. Quyền mua cần bạn bỏ tiền thật và có thể bán quyền để bù. Phát hành riêng lẻ cho một nhóm nhà đầu tư là trường hợp phải chú ý nhất, vì giá phát hành thường thấp '
         'hơn thị giá và làm pha loãng cổ đông hiện hữu. Khi gặp một sự kiện lạ, hãy hỏi bốn câu: tiền có ra hay vào công ty không, số cổ phiếu tăng bao nhiêu, giá tham chiếu điều chỉnh thế nào, và '
         'tỷ lệ sở hữu của mình thay đổi ra sao. Chỉ cần trả lời được bốn câu này, bạn sẽ không còn bị những dòng tin giật gân về thưởng hay chia tách làm hoang mang.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Năm câu hỏi tự kiểm tra',
  'moc': True,
  'label': 'Trước khi phản ứng với một sự kiện quyền',
  'cap': ('5 CÂU HỎI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Tiền thật có chảy ra hoặc vào công ty không?', (56, 189, 248)),
            ('Giá tham chiếu được điều chỉnh bao nhiêu?', (56, 189, 248)),
            ('Mình có phải nộp tiền để giữ tỷ lệ sở hữu không?', (255, 196, 0)),
            ('EPS sau sự kiện thay đổi thế nào?', (255, 196, 0)),
            ('Giá trị tài sản của mình có thật sự đổi không?', (34, 197, 94))],
  'anh': 'investor thinking at desk',
  'say': 'Năm câu hỏi này đủ dùng cho mọi sự kiện quyền trong nhiều năm tới. Một, tiền thật có chảy ra hoặc vào công ty không. Hai, giá tham chiếu được điều chỉnh bao nhiêu để so sánh đúng giá trước '
         'và sau. Ba, bạn có phải nộp tiền để giữ nguyên tỷ lệ sở hữu không. Bốn, lợi nhuận trên mỗi cổ phiếu sau sự kiện thay đổi thế nào, vì EPS bị chia nhỏ là điều nhiều người quên. Năm, giá trị '
         'tài sản của bạn có thật sự đổi hay chỉ đổi cách đếm. Cách làm này nghe đơn giản nhưng giúp bạn tránh hai sai lầm phổ biến. Sai lầm thứ nhất là vui mừng vì nhận thêm cổ phiếu rồi hoảng khi '
         'thấy giá giảm. Sai lầm thứ hai là bán vội vì nghĩ giá giảm là tin xấu. Thị trường lên xuống thế nào, nguyên lý tính toán vẫn đứng yên.'},
 {'k': 'end',
  'label': '',
  'cap': ('NỀN TẢNG ĐẦU TƯ', 'TÍNH TRƯỚC KHI LO'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu giá trong biểu đồ lấy từ dữ liệu tổng hợp đến ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu, chỉ làm hình minh họa. Các ví dụ tính toán là số giả định. Nội dung '
         'chia sẻ kiến thức, không phải khuyến nghị mua bán chứng khoán. Nếu thấy hữu ích, hãy đăng ký kênh để xem tiếp seri Nền tảng đầu tư.'}]

S['CH0811B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'GMD – minh họa tăng trưởng và định giá',
  'cap': ('P/E 12 CÓ ĐẮT?', 'TUỲ TĂNG TRƯỞNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'GMDW', 'tf': 'W', 'weeks': 52, 'circles': [[6, 36.86, 'Đáy tuần 15/12/25: 36,86', 0.6], [16, 57.99, 'Đỉnh tuần 2/3/26: 57,99', 1.6], [51, 52.6, '5/11/26: 52,60', 2.6]]},
  'anh': 'container ship at port',
  'say': 'Hai doanh nghiệp cùng có P/E là mười hai. Một doanh nghiệp tăng lợi nhuận năm phần trăm mỗi năm, doanh nghiệp kia tăng hai mươi lăm phần trăm. Bạn nghĩ hai mức giá này có đắt như nhau '
         'không? Hầu hết người mới chỉ nhìn P/E rồi kết luận, trong khi con số chia cho tốc độ tăng trưởng mới cho câu trả lời, và hai kết quả ở đây chênh nhau năm lần. Trong video này mình giải '
         'thích chỉ số PEG, cách dựng ba kịch bản lợi nhuận, biên an toàn là gì, vì sao ngoại suy từ một quý đẹp là cái bẫy lớn nhất, và vai trò của lãi suất trong mọi phép định giá. Xem đến hết bạn '
         'sẽ hiểu vì sao không có con số kỳ diệu nào, chỉ có cách nghĩ đúng. Doanh nghiệp vận tải biển và cảng trên biểu đồ chỉ là ví dụ minh họa với số liệu quý ba năm hai nghìn không trăm hai mươi '
         'sáu. Các mức định giá tính trong bài là giả định, không phải khuyến nghị.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Từ P/E đến PEG',
  'moc': True,
  'label': 'Ví dụ giả định: cùng P/E 12, tăng trưởng khác nhau',
  'cap': ('PEG = P/E ÷ TĂNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Công ty A', 'P/E 12, tăng 5%', 'PEG 2,4'), ('Công ty B', 'P/E 12, tăng 15%', 'PEG 0,8'), ('Công ty C', 'P/E 12, tăng 25%', 'PEG 0,5')],
  'anh': 'calculator and charts',
  'say': 'P/E cho biết bạn trả bao nhiêu đồng cho mỗi đồng lợi nhuận hiện tại. Nhưng nếu lợi nhuận đang tăng nhanh, năm sau mỗi đồng giá bạn trả sẽ đổi được nhiều lợi nhuận hơn. PEG là cách ghép hai '
         'điều đó lại: lấy P/E chia cho tốc độ tăng trưởng lợi nhuận hằng năm tính theo phần trăm. Với cùng P/E mười hai, công ty tăng năm phần trăm có PEG hai phẩy bốn, công ty tăng mười lăm phần '
         'trăm có PEG không phẩy tám, công ty tăng hai mươi lăm phần trăm có PEG không phẩy năm. Quy ước thường gặp là PEG quanh một được xem là cân bằng, thấp hơn thì giá có vẻ rẻ so với tăng '
         'trưởng, cao hơn thì ngược lại. Nhưng đây chỉ là quy ước để so sánh nhanh, không phải luật. Nó chỉ có ý nghĩa khi tốc độ tăng trưởng bạn dùng là con số đáng tin, và đó chính là phần khó '
         'nhất của cả bài.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Nhìn lợi nhuận 5 quý của một doanh nghiệp cảng biển',
  'moc': True,
  'label': 'LNST công ty mẹ GMD theo quý (tỷ đồng)',
  'cap': ('LỢI NHUẬN 5 QUÝ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 315.2, (56, 189, 248), '315'),
           ('Q4/25', 592.2, (56, 189, 248), '592'),
           ('Q1/26', 534.2, (56, 189, 248), '534'),
           ('Q2/26', 1124.2, (255, 196, 0), '1.124'),
           ('Q3/26', 443.9, (56, 189, 248), '444')],
  'anh': 'port crane container terminal',
  'say': 'Đây là lợi nhuận sau thuế năm quý gần nhất của một doanh nghiệp cảng biển và logistics. Quý ba năm hai nghìn không trăm hai mươi lăm là ba trăm mười lăm tỷ, quý hai năm nay vọt lên một '
         'nghìn một trăm hai mươi bốn tỷ, rồi quý ba còn bốn trăm bốn mươi bốn tỷ. Chín tháng đầu năm lợi nhuận tăng tám mươi phẩy bảy phần trăm so với cùng kỳ, nhưng quý ba chỉ tăng bốn mươi phẩy '
         'tám phần trăm và giảm hơn một nửa so với quý trước. Nếu bạn lấy con số tám mươi phần trăm rồi chia cho P/E để ra PEG cực thấp, bạn sẽ kết luận rất đẹp nhưng rất dễ sai. Một quý có lợi '
         'nhuận cao bất thường kéo cả bức tranh lên. Với dữ liệu kiểu này, người đọc cẩn thận sẽ hỏi quý đột biến đến từ hoạt động kinh doanh chính hay từ khoản thu nhập một lần.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Ba kịch bản EPS thay cho một con số',
  'moc': True,
  'label': 'Ví dụ giả định để luyện cách nghĩ, không phải dự báo',
  'cap': ('3 KỊCH BẢN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Thận trọng', 'EPS tăng 5%/năm', 'xem như trần của cơ bản'), ('Cơ sở', 'EPS tăng 12%/năm', 'bằng mức trung bình nhiều năm'), ('Lạc quan', 'EPS tăng 20%/năm', 'chỉ khi có lý do cụ thể')],
  'anh': 'whiteboard planning scenarios',
  'say': 'Thay vì chọn một con số tăng trưởng duy nhất, người làm định giá nghiêm túc dựng ba kịch bản. Kịch bản thận trọng giả định lợi nhuận tăng rất chậm hoặc đi ngang. Kịch bản cơ sở lấy mức '
         'tăng trưởng trung bình nhiều năm của doanh nghiệp, đã bao gồm cả năm tốt lẫn năm xấu. Kịch bản lạc quan chỉ dùng khi bạn nêu được lý do cụ thể, ví dụ công suất mới sắp đi vào vận hành. Với '
         'mỗi kịch bản, bạn tính EPS sau ba năm, nhân với một mức P/E hợp lý rồi so với giá hiện tại. Ví dụ EPS hiện tại sáu nghìn đồng, tăng mười hai phần trăm mỗi năm thì sau ba năm khoảng tám '
         'nghìn bốn trăm đồng. Bạn thu được một khoảng giá trị chứ không phải một điểm, và khoảng đó mới là thứ trung thực. Nếu giá hiện tại nằm trên cả ba kịch bản, đó là tín hiệu để thận trọng.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Biên an toàn',
  'moc': True,
  'label': 'Khoảng đệm cho sai số của chính bạn',
  'cap': ('BIÊN AN TOÀN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Giá trị ước tính luôn có sai số, đệm 20–30% là thói quen phổ biến', (56, 189, 248)),
            ('Biên an toàn lớn hơn khi ngành biến động mạnh', (255, 196, 0)),
            ('Biên an toàn không đảm bảo thắng, chỉ giảm tổn thương khi sai', (239, 68, 68))],
  'anh': 'safety net construction',
  'say': 'Biên an toàn là ý tưởng mượn từ ngành xây cầu. Kỹ sư thiết kế cầu chịu được mười tấn nhưng chỉ cho xe sáu tấn chạy qua. Trong đầu tư, nếu bạn ước tính giá trị hợp lý của một cổ phiếu là '
         'một trăm nghìn và chỉ muốn mua ở mức thấp hơn đáng kể, khoảng cách đó chính là chiếc đệm cho sai số của bạn. Nhiều người dùng đệm hai mươi đến ba mươi phần trăm, ngành càng biến động mạnh '
         'thì đệm nên càng dày. Biên an toàn không đảm bảo bạn lãi. Nó chỉ làm cho cú sai của bạn bớt đau, và quan trọng hơn, nó bắt bạn thừa nhận rằng mọi dự báo đều có thể sai. Người có biên an '
         'toàn thường kiên nhẫn chờ giá phù hợp, còn người không có thường mua vì sợ bỏ lỡ. Hai thói quen này dẫn đến hai kết quả rất khác nhau sau nhiều năm.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Ba sai lầm khi ngoại suy',
  'moc': True,
  'label': 'Những cách tăng trưởng đẹp trên giấy thành bẫy',
  'cap': ('3 SAI LẦM',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lấy một quý đột biến nhân lên cả năm', (239, 68, 68)),
            ('Cho rằng tăng trưởng cao kéo dài mãi', (239, 68, 68)),
            ('Bỏ qua biên lợi nhuận đang thu hẹp', (239, 68, 68)),
            ('Dùng tăng trưởng cũ cho doanh nghiệp đã lớn', (56, 189, 248))],
  'anh': 'cliff edge warning sign',
  'say': 'Sai lầm đầu tiên là lấy một quý đẹp nhân bốn. Trong ví dụ doanh nghiệp cảng biển, quý hai lập đỉnh nhưng quý ba đã giảm hơn sáu mươi phần trăm so với quý trước. Sai lầm thứ hai là tin rằng '
         'tăng trưởng cao sẽ kéo dài mãi. Doanh nghiệp càng lớn thì càng khó tăng nhanh, vì mức nền đã cao. Sai lầm thứ ba là bỏ qua biên lợi nhuận. Cũng ở doanh nghiệp này, biên lợi nhuận gộp quý '
         'ba là ba mươi mốt phẩy tám phần trăm, thấp hơn mức bốn mươi hai phẩy bảy phần trăm cùng kỳ, nghĩa là mỗi đồng doanh thu giữ lại được ít lợi nhuận hơn dù doanh thu vẫn tăng. Khi thấy cả ba '
         'dấu hiệu này, hãy hạ giả định tăng trưởng xuống trước khi tính PEG. Tăng trưởng bền vững thường thấp hơn tăng trưởng mà quý gần nhất cho thấy.'},
 {'k': 'cards',
  'ch': 'Chương 6 – Tăng trưởng bền vững đến từ đâu',
  'moc': True,
  'label': 'Ba nguồn tăng trưởng lợi nhuận',
  'cap': ('NGUỒN TĂNG', 'TRƯỞNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Bán nhiều hơn', 'sản lượng, thị phần', 'phụ thuộc cầu & công suất'),
            ('Lãi cao hơn', 'giá bán, biên', 'dễ bị cạnh tranh bào mòn'),
            ('Dùng vốn tốt hơn', 'ROE, vòng quay', 'bền khi lợi thế cạnh tranh có thật')],
  'anh': 'factory expansion construction',
  'say': 'Tăng trưởng lợi nhuận chỉ đến từ ba nguồn. Một là bán nhiều hơn, nhờ thêm khách hàng hoặc thêm công suất. Hai là lãi nhiều hơn trên mỗi đồng doanh thu, nhờ tăng giá hoặc giảm chi phí. Ba '
         'là dùng vốn hiệu quả hơn, tức ROE tăng. Nguồn thứ hai thường kém bền nhất vì đối thủ cạnh tranh sẽ kéo biên về mức trung bình. Nguồn thứ nhất bền hơn nếu ngành còn dư địa. Nguồn thứ ba bền '
         'khi doanh nghiệp có lợi thế khó sao chép như vị trí cảng, thương hiệu hay hệ thống phân phối. Cũng có một công thức gần đúng: tăng trưởng bền vững bằng ROE nhân với tỷ lệ lợi nhuận giữ '
         'lại. Doanh nghiệp có ROE hai mươi phần trăm và giữ lại sáu mươi phần trăm lợi nhuận về lý thuyết tăng khoảng mười hai phần trăm mỗi năm mà không cần vay thêm. Đây là cách kiểm tra xem con '
         'số tăng trưởng bạn dùng có nằm trong giới hạn hợp lý không.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Lãi suất: sợi dây ngầm của mọi định giá',
  'moc': True,
  'label': 'Vì sao cùng lợi nhuận mà giá hợp lý đổi',
  'cap': ('LÃI SUẤT & P/E',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lãi suất thấp: dòng tiền tương lai đáng giá hơn', (34, 197, 94)),
            ('Lãi suất cao: dòng tiền tương lai bị chiết khấu nặng', (239, 68, 68)),
            ('Cổ phiếu tăng trưởng nhạy với lãi suất hơn cổ phiếu ổn định', (56, 189, 248))],
  'anh': 'central bank building',
  'say': 'Mọi phép định giá đều ngầm có một con số khác là lãi suất. Lý do là tiền nhận được trong tương lai kém giá trị hơn tiền nhận hôm nay, vì bạn có thể gửi tiền hôm nay để sinh lãi. Khi lãi '
         'suất thấp, lợi nhuận tương lai được chiết khấu nhẹ nên mức P/E hợp lý thường cao hơn. Khi lãi suất tăng, mức P/E hợp lý co lại dù lợi nhuận chưa đổi. Cổ phiếu mà phần lớn giá trị nằm ở lợi '
         'nhuận rất xa trong tương lai chịu ảnh hưởng mạnh hơn cổ phiếu có lợi nhuận ổn định hiện tại. Đó là lý do bạn thấy cổ phiếu tăng trưởng giảm mạnh khi lãi suất đi lên, ngay cả khi doanh '
         'nghiệp vẫn kinh doanh tốt. Vì vậy, một PEG đẹp trong môi trường lãi suất thấp có thể chỉ còn trung bình khi lãi suất tăng, và bạn nên xem lại giả định mỗi khi môi trường lãi suất thay đổi '
         'rõ rệt.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Quy trình 5 bước',
  'cap': ('QUY TRÌNH 5 BƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Lấy P/E và tăng trưởng từ nhiều quý, không phải một quý', (56, 189, 248)),
            ('2. Loại khoản bất thường khỏi lợi nhuận', (56, 189, 248)),
            ('3. Dựng ba kịch bản EPS', (255, 196, 0)),
            ('4. Đặt biên an toàn cho sai số', (255, 196, 0)),
            ('5. Xem lại khi lãi suất thay đổi', (34, 197, 94))],
  'anh': 'investor notebook planning',
  'say': 'Tóm lại, không có con số kỳ diệu nào cho định giá. PEG là công cụ so sánh nhanh nhưng chỉ đúng khi tốc độ tăng trưởng đáng tin. Quy trình năm bước giúp bạn dùng nó đúng cách. Một, lấy P/E '
         'và tăng trưởng từ nhiều quý chứ không phải một quý. Hai, loại các khoản bất thường ra khỏi lợi nhuận. Ba, dựng ba kịch bản thay vì một điểm. Bốn, đặt biên an toàn cho sai số của chính bạn. '
         'Năm, xem lại khi lãi suất thay đổi. Điều quan trọng nhất là thái độ: định giá là cách nghĩ về một khoảng giá trị, không phải máy tính cho đáp án. Nếu mười năm nữa bạn xem lại video này, số '
         'liệu ví dụ chắc chắn đã khác, nhưng bốn câu hỏi về nguồn tăng trưởng, độ bền, biên an toàn và lãi suất vẫn đúng như hôm nay.'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐỊNH GIÁ', 'LÀ MỘT KHOẢNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu của doanh nghiệp trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày năm tháng mười một. Các mức định giá là giả định minh '
         'họa, không phải khuyến nghị mua bán. Nếu thấy hữu ích, hãy đăng ký kênh để xem thêm seri Định giá.'}]

S['CH0811C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – ba cú giảm lớn',
  'cap': ('3 LẦN RỚT SÂU', '25–43%: SAU ĐÓ?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, '5/11/26: 1.741', 2.6]]},
  'anh': 'stock market crash newspaper',
  'say': 'Ba lần trong tám năm, VN-Index mất từ một phần tư đến hơn bốn mươi phần trăm giá trị. Mỗi lần, đám đông đều nói lần này khác. Vậy điều gì thật sự lặp lại mỗi lần chỉ số rơi sâu, và điều gì '
         'khác nhau? Năm hai nghìn không trăm mười tám, chỉ số từ một nghìn hai trăm lẻ bốn xuống khoảng tám trăm chín mươi. Năm hai nghìn không trăm hai mươi, dịch bệnh kéo chỉ số xuống sáu trăm '
         'năm mươi chín điểm. Năm hai nghìn không trăm hai mươi hai, từ một nghìn năm trăm hai mươi tám xuống dưới chín trăm điểm. Xem hết video, bạn sẽ biết ba điểm chung của ba cú giảm, vì sao đòn '
         'bẩy luôn là nhân vật chính, và ba việc nên làm trước cú giảm tiếp theo. Đây là bài học lịch sử, không phải dự báo, và biểu đồ phía sau là nến tuần VN-Index một năm gần nhất.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Năm 2018: đỉnh tháng Tư, nhiều dòng tiền đuổi theo',
  'moc': True,
  'label': 'VN-Index 2018 (làm tròn)',
  'cap': ('NĂM 2018',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Đỉnh', '1.204 điểm', 'phiên 9/4/2018'), ('Cuối năm', 'khoảng 893 điểm', 'giảm khoảng 26%'), ('Bối cảnh', 'định giá cao', 'căng thẳng thương mại toàn cầu')],
  'anh': 'financial chart red decline',
  'say': 'Đầu năm hai nghìn không trăm mười tám, thị trường Việt Nam là một trong những nơi tăng mạnh nhất thế giới. Chỉ số chạm đỉnh một nghìn hai trăm lẻ bốn điểm vào ngày chín tháng Tư. Định giá '
         'nhiều cổ phiếu đã cao, dòng tiền mới đổ vào rất nhanh, trong đó có không ít tiền vay. Sau đó, căng thẳng thương mại giữa các nền kinh tế lớn làm thị trường toàn cầu rung lắc, và chỉ số '
         'Việt Nam giảm dần rồi kết thúc năm quanh tám trăm chín mươi ba điểm, tức mất khoảng hai mươi sáu phần trăm từ đỉnh. Điểm đáng nhớ là cú giảm không đến trong một ngày, mà kéo dài gần chín '
         'tháng, đủ lâu để làm nhiều người mất kiên nhẫn và bán ở vùng thấp. Cú giảm chậm và dai thường làm hao tâm lý nhiều hơn cú sập nhanh.'},
 {'k': 'cards',
  'ch': 'Chương 2 – Năm 2020: cú sốc đến từ bên ngoài',
  'moc': True,
  'label': 'VN-Index đầu 2020 (làm tròn)',
  'cap': ('NĂM 2020',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Từ', 'khoảng 1.000 điểm', 'đầu năm 2020'), ('Đáy', '659 điểm', 'phiên 24/3/2020'), ('Cuối năm', 'vượt 1.100 điểm', 'hồi phục nhanh')],
  'anh': 'empty street pandemic lockdown',
  'say': 'Năm hai nghìn không trăm hai mươi là cú giảm khác loại. Không có bong bóng định giá nào, mà là cú sốc từ bên ngoài: đại dịch làm cả thế giới đóng cửa. Chỉ số từ vùng một nghìn điểm đầu năm '
         'xuống sáu trăm năm mươi chín điểm vào cuối tháng Ba, giảm khoảng một phần ba trong vài tuần. Nhưng sau đó chỉ số hồi phục rất nhanh nhờ lãi suất thấp và dòng tiền mới vào thị trường, cuối '
         'năm vượt một nghìn một trăm điểm. Bài học là cú sốc từ bên ngoài có thể đến bất cứ lúc nào, nhưng cũng có thể qua nhanh nếu nền tảng doanh nghiệp không hỏng. Người bán ở đáy vì sợ đã chốt '
         'khoản lỗ lớn đúng vào lúc thị trường sắp đảo chiều, và đây là hình mẫu lặp đi lặp lại ở mọi cú giảm.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Năm 2022: đỉnh lịch sử rồi xuống dưới 900',
  'moc': True,
  'label': 'VN-Index 2022 (làm tròn)',
  'cap': ('NĂM 2022',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Đỉnh', 'khoảng 1.528 điểm', 'đầu tháng 1/2022'), ('Đáy', 'dưới 900 điểm', 'khoảng tháng 11/2022'), ('Giảm', 'hơn 40%', 'đòn bẩy & lãi suất tăng')],
  'anh': 'city skyline downturn grey',
  'say': 'Đầu năm hai nghìn không trăm hai mươi hai, chỉ số ở quanh vùng một nghìn năm trăm hai mươi tám điểm, mức cao kỷ lục lúc bấy giờ, sau hai năm tăng rất nóng với hàng triệu tài khoản mới mở. '
         'Rồi lãi suất toàn cầu tăng, thị trường trái phiếu doanh nghiệp và bất động sản trong nước gặp khó, dòng tiền rút ra. Đến khoảng tháng Mười Một, chỉ số xuống dưới chín trăm điểm, mất hơn '
         'bốn mươi phần trăm. Đây là cú giảm có nhiều yếu tố giống năm hai nghìn không trăm bảy và hai nghìn không trăm tám: tăng nóng, đòn bẩy cao, rồi dòng tiền quay đầu. Điểm khác là lần này thị '
         'trường có nhiều nhà đầu tư cá nhân trẻ lần đầu trải nghiệm một chu kỳ giảm sâu, và rất nhiều người học được bài học về vay ký quỹ theo cách đắt giá.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Ba cú giảm cạnh nhau',
  'moc': True,
  'label': 'Mức giảm từ đỉnh đến đáy (%, làm tròn)',
  'cap': ('SO SÁNH 3 LẦN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('2018', 26, (56, 189, 248), '~26%'), ('2020', 34, (255, 196, 0), '~34%'), ('2022', 43, (239, 68, 68), '>40%')],
  'anh': 'bar chart comparison finance',
  'say': 'Đặt ba cú giảm cạnh nhau, bạn thấy mức giảm khoảng hai mươi sáu, ba mươi bốn và hơn bốn mươi phần trăm. Đây là các con số làm tròn từ giá đóng cửa của chỉ số, đủ để thấy một quy luật: cứ '
         'vài năm, thị trường lại có một lần giảm từ một phần tư đến gần một nửa. Với bạn, điều này có hai ý nghĩa. Thứ nhất, nếu bạn đầu tư cổ phiếu đủ lâu, gần như chắc chắn bạn sẽ trải qua ít '
         'nhất một lần. Thứ hai, bạn nên quyết định cách mình phản ứng từ lúc bình tĩnh, không phải đợi đến lúc tài khoản đỏ. Hãy thử hỏi: nếu tài khoản của bạn mất bốn mươi phần trăm, bạn còn ngủ '
         'được không? Nếu câu trả lời là không, tỷ trọng cổ phiếu của bạn đang quá cao so với khả năng chịu đựng của bản thân, và đó là điều chỉnh bạn có thể làm ngay hôm nay.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Ba điểm chung',
  'moc': True,
  'label': 'Điều lặp lại',
  'cap': ('3 ĐIỂM CHUNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Tăng nóng trước đó, dòng tiền mới đổ vào nhanh', (56, 189, 248)), ('Đòn bẩy làm cú giảm thành dây chuyền bán tháo', (239, 68, 68)), ('Đáy luôn đi kèm tâm lý tuyệt vọng', (255, 196, 0))],
  'anh': 'crowd of traders worried',
  'say': 'Ba cú giảm khác nhau về nguyên nhân nhưng có ba điểm chung. Một là trước mỗi cú giảm đều có giai đoạn tăng nóng, khi dòng tiền mới đổ vào nhanh và mọi người đều thấy dễ kiếm tiền. Hai là '
         'đòn bẩy biến cú giảm thành dây chuyền: giá giảm làm tài khoản vay chạm ngưỡng cảnh báo, bị bán giải chấp, bán ra làm giá giảm tiếp. Ba là đáy thường đi kèm tâm lý tuyệt vọng, khi người ta '
         'nói thị trường sẽ không bao giờ hồi phục và khối lượng bán dồn dập cuối cùng. Ngược lại, những giai đoạn mọi người đều chắc chắn thị trường sẽ tăng mãi thường gần đỉnh hơn. Tất nhiên không '
         'thể dùng quy luật tâm lý này để bắt đúng đáy hay đỉnh, nhưng nó nhắc rằng đám đông thường cảm nhận rõ nhất ở đúng thời điểm sai nhất.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Điểm khác nhau',
  'moc': True,
  'label': 'Mỗi lần một nguyên nhân',
  'cap': ('3 NGUYÊN', 'NHÂN KHÁC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('2018: định giá cao + căng thẳng thương mại', (56, 189, 248)),
            ('2020: cú sốc dịch bệnh, phục hồi nhờ lãi suất thấp', (255, 196, 0)),
            ('2022: lãi suất tăng + trái phiếu & bất động sản gặp khó', (239, 68, 68))],
  'anh': 'world map economy',
  'say': 'Điểm khác nhau là nguyên nhân kích hoạt và tốc độ hồi phục. Năm hai nghìn không trăm mười tám là định giá cao gặp căng thẳng thương mại. Năm hai nghìn không trăm hai mươi là cú sốc dịch '
         'bệnh nhưng được đỡ bởi lãi suất thấp và hỗ trợ chính sách, nên hồi phục chữ V. Năm hai nghìn không trăm hai mươi hai là lãi suất tăng cộng với vấn đề trái phiếu doanh nghiệp và bất động '
         'sản, nên hồi phục chậm hơn và cần cải tổ nền tảng. Nhìn như vậy, câu nói lần này khác thực ra đúng một nửa. Nguyên nhân luôn khác, nhưng cơ chế khuếch đại bằng đòn bẩy và tâm lý thì giống '
         'nhau. Vì thế thay vì đoán nguyên nhân của cú giảm tiếp theo, hãy chuẩn bị cho cơ chế khuếch đại, thứ bạn kiểm soát được bằng chính cách dùng vốn của mình.'},
 {'k': 'bars',
  'ch': 'Chương 7 – Ba năm gần đây: bốn lần giảm trên 10%',
  'moc': True,
  'label': 'Mức giảm từ đỉnh đến đáy các nhịp giảm trên 10% của VN-Index, giá đóng cửa (%)',
  'cap': ('4 NHỊP GẦN ĐÂY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('17/3→9/4/2025', 18.1, (239, 68, 68), '18,1%'),
           ('16/10→10/11/2025', 10.5, (56, 189, 248), '10,5%'),
           ('13/1→23/3/2026', 16.4, (239, 68, 68), '16,4%'),
           ('18/5→22/7/2026', 13.5, (56, 189, 248), '13,5%')],
  'anh': 'stock chart volatility screen',
  'say': 'Dữ liệu ba năm gần đây của VN-Index cho thấy cú giảm trên mười phần trăm không phải chuyện hiếm. Có bốn nhịp. Từ ngày mười bảy tháng Ba đến ngày chín tháng Tư năm hai nghìn không trăm hai '
         'mươi lăm, chỉ số giảm mười tám phẩy một phần trăm. Từ mười sáu tháng Mười đến mười tháng Mười Một năm đó, giảm mười phẩy năm phần trăm. Từ mười ba tháng Một đến hai mươi ba tháng Ba năm '
         'hai nghìn không trăm hai mươi sáu, giảm mười sáu phẩy bốn phần trăm. Và từ mười tám tháng Năm đến hai mươi hai tháng Bảy năm nay, giảm mười ba phẩy năm phần trăm. Cùng khoảng thời gian đó '
         'chỉ số vẫn có những đỉnh mới, đến phiên năm tháng Mười Một đang ở một nghìn bảy trăm bốn mươi điểm. Nói cách khác, trong một thị trường nhìn chung đi lên, mỗi năm vẫn có một hai nhịp giảm '
         'đủ sâu để thử lòng người.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Ba việc nên làm trước cú giảm tiếp theo',
  'moc': True,
  'label': 'Làm khi thị trường còn yên',
  'cap': ('3 VIỆC TRƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Biết mình chịu được mức giảm nào, đặt tỷ trọng cổ phiếu theo đó', (255, 196, 0)),
            ('Không dùng vốn vay quá sức, giữ khoảng đệm tiền mặt', (255, 196, 0)),
            ('Viết sẵn kế hoạch: khi giảm 20%, 30% tôi sẽ làm gì', (34, 197, 94))],
  'anh': 'person writing plan notebook',
  'say': 'Ba việc nên làm khi thị trường còn yên. Một, xác định mức giảm bạn chịu được và đặt tỷ trọng cổ phiếu theo mức đó, đừng theo cảm giác lúc thị trường đang lên. Hai, tránh dùng vốn vay quá '
         'sức, và giữ một khoản tiền mặt đệm để không buộc phải bán lúc giá thấp. Ba, viết sẵn kế hoạch bằng giấy: nếu chỉ số giảm hai mươi phần trăm tôi sẽ làm gì, nếu giảm ba mươi phần trăm tôi sẽ '
         'làm gì. Kế hoạch này không cần thông minh, chỉ cần có. Khi cú giảm đến, bạn sẽ không phải quyết định giữa lúc sợ hãi nhất. Lịch sử không cho biết chính xác khi nào thị trường giảm, nhưng '
         'cho biết người sống sót và tiếp tục đi tiếp thường là người có kế hoạch trước, ít vay, và không dồn mọi thứ vào một thời điểm.'},
 {'k': 'end',
  'label': '',
  'cap': ('BÀI HỌC LỊCH SỬ', 'CHUẨN BỊ TRƯỚC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu VN-Index các năm hai nghìn không trăm mười tám, hai nghìn không trăm hai mươi và hai nghìn không trăm hai mươi hai là số làm tròn từ giá đóng cửa. Bốn nhịp giảm gần đây tính từ dữ '
         'liệu giá đến ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu. Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán. Hãy đăng ký kênh để xem thêm seri Bài học lịch sử.'}]

S['CH0911A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'HAH – minh họa lãi và tiền',
  'cap': ('LÃI ĐẸP NHƯNG', 'KHÁCH NỢ 90 NGÀY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'HAHW', 'tf': 'W', 'weeks': 52, 'circles': [[16, 68.88, 'Đỉnh tuần 2/3/26: 68,88', 0.6], [44, 42.9, 'Đáy tuần 14/9/26: 42,90', 1.6], [51, 48.75, '5/11/26: 48,75', 2.6]]},
  'anh': 'container yard logistics',
  'say': 'Một doanh nghiệp báo lãi đều ba năm liền, doanh thu năm nào cũng tăng. Nhưng nếu thời gian khách hàng trả tiền kéo từ bốn mươi lăm ngày lên chín mươi mốt ngày, thì phần lãi đó đang nằm '
         'trong sổ nợ chứ chưa nằm trong két. Hai khoản mục dễ bị lướt qua nhất trong bảng cân đối kế toán là hàng tồn kho và khoản phải thu, và chúng thường là nơi cảnh báo đầu tiên xuất hiện, '
         'trước cả khi lợi nhuận giảm. Trong video này mình chỉ cách tính số ngày thu tiền, số ngày tồn kho, chu kỳ chuyển đổi tiền mặt, sáu dấu hiệu cảnh báo và quy trình năm bước kiểm tra. Xem hết '
         'bạn sẽ tự tính được chỉ với một cây bút và ba con số trong báo cáo. Các ví dụ tính toán là số giả định để minh họa, riêng doanh nghiệp vận tải container chỉ được dùng làm ví dụ về kết quả '
         'kinh doanh quý ba năm hai nghìn không trăm hai mươi sáu.'},
 {'k': 'checklist',
  'ch': 'Chương 1 – Hai khoản mục ngủ yên trong bảng cân đối',
  'moc': True,
  'label': 'Vì sao cần nhìn hai khoản này',
  'cap': ('2 KHOẢN CẦN SOI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Khoản phải thu: hàng đã giao nhưng chưa thu được tiền', (56, 189, 248)),
            ('Hàng tồn kho: hàng đã mua hoặc làm ra nhưng chưa bán', (56, 189, 248)),
            ('Cả hai chiếm vốn lưu động và có thể kẹt lâu', (239, 68, 68)),
            ('Lợi nhuận kế toán đã ghi, nhưng tiền chưa vào', (255, 196, 0))],
  'anh': 'warehouse inventory shelves',
  'say': 'Khi một doanh nghiệp bán hàng nhưng khách chưa trả tiền, kế toán vẫn ghi doanh thu và lợi nhuận, đồng thời ghi một khoản phải thu. Khi doanh nghiệp mua hàng hay sản xuất nhưng chưa bán '
         'được, tiền đã ra khỏi két và nằm lại thành hàng tồn kho. Cả hai khoản này đều chiếm vốn lưu động. Nếu chúng phình to nhanh hơn doanh thu, doanh nghiệp cần vay thêm hoặc dùng tiền mặt để '
         'duy trì hoạt động, dù trên giấy vẫn lãi. Hãy hình dung một cửa hàng bán chịu cho mọi khách quen. Sổ sách đẹp, nhưng cuối tháng không còn tiền trả lương. Không có gì sai về kế toán, vấn đề '
         'nằm ở thời gian chờ tiền. Vì thế người đọc báo cáo cần so tốc độ tăng của hai khoản này với tốc độ tăng của doanh thu, chứ không chỉ nhìn bản thân chúng lớn hay nhỏ.'},
 {'k': 'cards',
  'ch': 'Chương 2 – DSO: số ngày thu tiền',
  'moc': True,
  'label': 'Ví dụ giả định: doanh thu năm 1.200 tỷ, khoản phải thu cuối năm 300 tỷ',
  'cap': ('DSO',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Công thức', 'Phải thu ÷ Doanh thu × 365', 'đo số ngày chờ tiền'), ('Tính', '300 ÷ 1.200 × 365', '≈ 91 ngày'), ('Đọc', 'so với kỳ hạn bán chịu', 'và với chính mình các năm trước')],
  'anh': 'accountant calculator invoices',
  'say': 'DSO là số ngày bình quân doanh nghiệp phải chờ để thu tiền sau khi bán. Công thức là khoản phải thu chia doanh thu rồi nhân ba trăm sáu mươi lăm. Với ví dụ giả định doanh thu một nghìn hai '
         'trăm tỷ, phải thu ba trăm tỷ, DSO là khoảng chín mươi mốt ngày, tức gần ba tháng. Con số này tự nó không tốt hay xấu. Phải so với kỳ hạn bán chịu thông thường của ngành, và quan trọng hơn '
         'là so với chính doanh nghiệp qua các năm. Nếu năm trước DSO là bốn mươi lăm ngày và năm nay chín mươi mốt ngày, thì doanh nghiệp đang nới lỏng bán chịu để giữ doanh thu, hoặc khách hàng '
         'đang gặp khó trả tiền. Cả hai đều là tín hiệu nên tìm hiểu thêm trong thuyết minh báo cáo.'},
 {'k': 'cards',
  'ch': 'Chương 3 – DIO và DPO: kho và nhà cung cấp',
  'moc': True,
  'label': 'Ví dụ giả định: giá vốn 900 tỷ, tồn kho 200 tỷ, phải trả 100 tỷ',
  'cap': ('DIO & DPO',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('DIO', '200 ÷ 900 × 365', '≈ 81 ngày tồn kho'),
            ('DPO', '100 ÷ 900 × 365', '≈ 41 ngày chịu nhà cung cấp'),
            ('Ghi nhớ', 'dùng giá vốn, không phải doanh thu', 'vì tồn kho tính theo giá vốn')],
  'anh': 'forklift warehouse',
  'say': 'DIO là số ngày hàng nằm trong kho trước khi bán. Công thức là tồn kho chia giá vốn hàng bán rồi nhân ba trăm sáu mươi lăm. Dùng giá vốn vì tồn kho được ghi theo giá vốn. Với tồn kho hai '
         'trăm tỷ và giá vốn chín trăm tỷ, DIO là khoảng tám mươi mốt ngày. DPO là số ngày doanh nghiệp được chịu tiền nhà cung cấp, tính bằng khoản phải trả chia giá vốn rồi nhân ba trăm sáu mươi '
         'lăm, ví dụ này ra khoảng bốn mươi mốt ngày. DPO càng dài càng có lợi cho doanh nghiệp, vì dùng tiền của nhà cung cấp để xoay vòng. Nhưng nếu DPO tăng mạnh bất thường, đôi khi là dấu hiệu '
         'doanh nghiệp đang thiếu tiền nên kéo dài thời gian trả. Ba chỉ số này nên luôn đọc cùng nhau chứ không đọc riêng lẻ.'},
 {'k': 'bars',
  'ch': 'Chương 4 – Chu kỳ chuyển đổi tiền mặt',
  'moc': True,
  'label': 'Ví dụ giả định: số ngày',
  'cap': ('CHU KỲ TIỀN MẶT',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('DSO thu tiền', 91, (56, 189, 248), '91'),
           ('DIO tồn kho', 81, (56, 189, 248), '81'),
           ('DPO trả nhà cung cấp', 41, (34, 197, 94), '−41'),
           ('Chu kỳ tiền mặt', 132, (239, 68, 68), '132 ngày')],
  'anh': 'cash flow cycle diagram',
  'say': 'Ghép ba chỉ số lại ta có chu kỳ chuyển đổi tiền mặt: DSO cộng DIO trừ DPO. Với ví dụ giả định, chín mươi mốt cộng tám mươi mốt trừ bốn mươi mốt là một trăm ba mươi hai ngày. Nghĩa là từ '
         'lúc doanh nghiệp bỏ tiền mua hàng, đến lúc thu lại tiền từ khách, mất khoảng bốn tháng rưỡi, trong thời gian đó phần vốn này không sinh ra tiền cho cổ đông. Chu kỳ càng dài, doanh nghiệp '
         'càng cần vốn lưu động, càng dễ phải vay, và càng dễ gặp khó khi lãi suất tăng. Chu kỳ ngắn hoặc âm là đặc điểm của một số mô hình bán lẻ, nơi khách trả ngay còn nhà cung cấp cho chịu lâu. '
         'Cách dùng tốt nhất không phải là học thuộc con số chuẩn, mà là theo dõi chu kỳ của chính doanh nghiệp qua nhiều quý để thấy nó đang dài ra hay ngắn đi.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Sáu dấu hiệu cảnh báo',
  'moc': True,
  'label': 'Khi nào nên đọc kỹ hơn',
  'cap': ('6 DẤU HIỆU',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Phải thu tăng nhanh hơn doanh thu trong 3 quý liền', (239, 68, 68)),
            ('Tồn kho tăng nhanh hơn giá vốn', (239, 68, 68)),
            ('DSO dài ra mà không có giải thích', (239, 68, 68)),
            ('Dự phòng phải thu khó đòi tăng đột biến', (239, 68, 68)),
            ('Phải thu từ một vài bên liên quan chiếm tỷ trọng lớn', (239, 68, 68)),
            ('Dòng tiền kinh doanh thấp hơn nhiều so với lợi nhuận', (255, 196, 0))],
  'anh': 'warning alert red flag',
  'say': 'Sáu dấu hiệu nên đọc kỹ hơn. Một, phải thu tăng nhanh hơn doanh thu ba quý liền. Hai, tồn kho tăng nhanh hơn giá vốn, nghĩa là hàng đang chất đống. Ba, DSO dài ra mà không có lời giải '
         'thích. Bốn, dự phòng phải thu khó đòi tăng đột biến, cho thấy chính doanh nghiệp cũng lo. Năm, khoản phải thu tập trung vào một vài bên có liên quan. Sáu, dòng tiền từ hoạt động kinh doanh '
         'thấp hơn nhiều so với lợi nhuận trong nhiều quý. Xuất hiện một dấu hiệu chưa chắc có vấn đề, vì có thể do mùa vụ hoặc chuẩn bị bán hàng. Nhưng khi xuất hiện từ ba dấu hiệu trở lên cùng '
         'lúc, bạn nên dành thời gian đọc thuyết minh báo cáo và nghe giải trình của ban lãnh đạo trước khi tin vào con số lợi nhuận.'},
 {'k': 'bars',
  'ch': 'Chương 6 – Một ví dụ kết quả kinh doanh thật: doanh nghiệp vận tải container',
  'moc': True,
  'label': 'Doanh thu thuần HAH theo quý (tỷ đồng)',
  'cap': ('DOANH THU 5 QUÝ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 1347.7, (56, 189, 248), '1.348'),
           ('Q4/25', 1299.6, (56, 189, 248), '1.300'),
           ('Q1/26', 1265.0, (56, 189, 248), '1.265'),
           ('Q2/26', 1533.6, (255, 196, 0), '1.534'),
           ('Q3/26', 1419.3, (56, 189, 248), '1.419')],
  'anh': 'container ship cargo vessel',
  'say': 'Để thấy cách đọc kết quả kinh doanh làm nền cho phân tích tiếp theo, hãy xem một doanh nghiệp vận tải container niêm yết. Doanh thu thuần quý ba năm hai nghìn không trăm hai mươi sáu là '
         'một nghìn bốn trăm mười chín tỷ, tăng năm phẩy ba phần trăm so với cùng kỳ. Lợi nhuận sau thuế ba trăm hai mươi chín tỷ, tăng tám phần trăm. Lũy kế chín tháng lợi nhuận tăng mười một phẩy '
         'ba phần trăm. Đây là bức tranh tăng trưởng vừa phải và khá đều qua năm quý. Với bức tranh như vậy, bước tiếp theo của người phân tích là mở bảng cân đối, tính DSO và DIO của các năm, rồi '
         'hỏi liệu tăng trưởng này có đang đi kèm tiền thu về tương ứng hay không. Video này không đánh giá cổ phiếu cụ thể, mà chỉ cho thấy khởi điểm của một quy trình kiểm tra.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Quy trình 5 bước kiểm tra',
  'moc': True,
  'label': 'Làm trong 10 phút với báo cáo miễn phí',
  'cap': ('QUY TRÌNH 5 BƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Lấy doanh thu, giá vốn, phải thu, tồn kho, phải trả', (56, 189, 248)),
            ('2. Tính DSO, DIO, DPO cho 3 năm hoặc 8 quý', (56, 189, 248)),
            ('3. So xu hướng với doanh thu và lợi nhuận', (255, 196, 0)),
            ('4. Đọc thuyết minh: phải thu của ai, tồn kho loại gì', (255, 196, 0)),
            ('5. Đối chiếu dòng tiền kinh doanh', (34, 197, 94))],
  'anh': 'analyst desk laptop spreadsheet',
  'say': 'Quy trình năm bước. Bước một, lấy năm con số từ báo cáo: doanh thu, giá vốn, khoản phải thu, hàng tồn kho và khoản phải trả. Bước hai, tính DSO, DIO và DPO cho ít nhất ba năm hoặc tám quý '
         'để thấy xu hướng. Bước ba, so xu hướng đó với tăng trưởng doanh thu và lợi nhuận. Bước bốn, đọc thuyết minh để biết khoản phải thu là của khách hàng nào, tồn kho gồm những loại gì, thành '
         'phẩm hay nguyên liệu hay bất động sản dở dang. Bước năm, đối chiếu với dòng tiền từ hoạt động kinh doanh. Cả quy trình thường không quá mười phút nếu bạn đã quen. Lưu ý quan trọng là mỗi '
         'ngành có chu kỳ tiền mặt khác nhau, nên đừng so một doanh nghiệp bán lẻ với một doanh nghiệp xây dựng. Hãy so doanh nghiệp với chính nó và với đối thủ cùng ngành.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Ba ý ghi nhớ',
  'cap': ('3 Ý GHI NHỚ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lợi nhuận là ý kiến, tiền thu về mới là sự thật', (255, 196, 0)),
            ('Xu hướng của DSO và DIO quan trọng hơn mức tuyệt đối', (56, 189, 248)),
            ('Một dấu hiệu là câu hỏi, ba dấu hiệu là cảnh báo', (239, 68, 68))],
  'anh': 'old library books timeless',
  'say': 'Ba ý mang theo mười năm. Một, lợi nhuận là kết quả của quy tắc ghi sổ, còn tiền thu về là thực tế. Hai, xu hướng của DSO và DIO quan trọng hơn mức tuyệt đối, vì mỗi ngành mỗi khác, nhưng '
         'sự xấu đi dần dần thì giống nhau ở mọi nơi. Ba, một dấu hiệu chỉ là câu hỏi cần tìm hiểu, ba dấu hiệu cùng lúc mới là cảnh báo. Khi bạn đã quen đọc hai khoản mục này, bạn sẽ thấy báo cáo '
         'tài chính bớt khô khan, vì mỗi dòng đều kể một phần câu chuyện của doanh nghiệp. Hãy thử làm ngay với một doanh nghiệp bạn quan tâm, tính DSO của hai năm gần nhất và so sánh. Chỉ cần làm '
         'một lần là bạn đã hơn rất nhiều người chỉ nhìn lợi nhuận. Đây là kỹ năng không bao giờ hết hạn.'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐỌC BCTC', 'TIỀN MỚI LÀ THẬT'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các ví dụ tính toán DSO, DIO và DPO là số giả định để minh họa. Số liệu kết quả kinh doanh của doanh nghiệp vận tải container lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai '
         'mươi sáu. Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Đọc BCTC.'}]

S['CH0911B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'MBB – ví dụ điền nhật ký',
  'cap': ('KHÔNG GHI LẠI', '= LẶP SAI LẦM?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'MBBW', 'tf': 'W', 'weeks': 52, 'circles': [[14, 23.63, 'Đỉnh tuần 9/2/26: 23,63', 0.6], [37, 17.78, 'Đáy tuần 27/7/26: 17,78', 1.6], [51, 19.5, '5/11/26: 19,50', 2.6]]},
  'anh': 'investor journal notebook',
  'say': 'Sáu tháng trước bạn mua một cổ phiếu vì điều gì? Nếu bạn không nhớ chính xác lý do, bạn đang giống phần lớn nhà đầu tư cá nhân. Trí nhớ có xu hướng viết lại quá khứ: khi thắng, ta nhớ mình '
         'đã phân tích kỹ, khi thua, ta đổ cho thị trường. Nhật ký đầu tư chặn đúng thói quen đó bằng một trang giấy điền trong ba phút trước mỗi lệnh. Trong video này mình giới thiệu mẫu nhật ký '
         'tám mục, vì sao phải ghi cả cảm xúc, cách xem lại mỗi quý, quy trình ba lớp để ra quyết định, và một ví dụ điền mẫu thật bằng số liệu quý ba của một ngân hàng lớn. Xem hết bạn sẽ có ngay '
         'một mẫu để dùng từ hôm nay. Lưu ý, ví dụ điền mẫu chỉ để minh họa cách ghi, không phải khuyến nghị mua hay bán bất kỳ cổ phiếu nào.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Vì sao trí nhớ không đủ',
  'moc': True,
  'label': 'Ba thiên kiến quen thuộc',
  'cap': ('VÌ SAO CẦN GHI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Thiên kiến nhìn lại', '"tôi biết từ đầu"', 'sau khi biết kết quả'),
            ('Tự quy kết', 'thắng do giỏi', 'thua do thị trường'),
            ('Thiên kiến xác nhận', 'chỉ nhớ tin ủng hộ', 'quên tin trái chiều')],
  'anh': 'person forgetting memory',
  'say': 'Có ba thiên kiến khiến trí nhớ không đáng tin khi nhớ lại quyết định đầu tư. Thiên kiến nhìn lại là cảm giác tôi đã biết từ đầu sau khi đã biết kết quả. Tự quy kết là khi thắng thì cho '
         'rằng mình giỏi, khi thua thì cho rằng do thị trường hay do tin xấu. Thiên kiến xác nhận là chỉ nhớ những thông tin ủng hộ quyết định của mình và quên những cảnh báo trái chiều. Cả ba đều '
         'khiến bạn không học được gì từ chính mình, vì dữ liệu về quá khứ đã bị chỉnh sửa bởi trí nhớ. Nhật ký là cách duy nhất để lưu bản gốc: lý do lúc bạn quyết định, trước khi có kết quả. Về '
         'sau, đọc lại bạn có thể thấy rõ mình hay sai ở đâu, quá tự tin ở nhóm nào, hoặc hay hoảng loạn trong hoàn cảnh nào.'},
 {'k': 'checklist',
  'ch': 'Chương 2 – Mẫu nhật ký 8 mục',
  'moc': True,
  'label': 'Điền trước khi vào lệnh',
  'cap': ('8 MỤC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Mã và ngày', (56, 189, 248)),
            ('2. Luận điểm trong một câu', (56, 189, 248)),
            ('3. Số liệu nền: P/E, P/B, ROE, tăng trưởng', (56, 189, 248)),
            ('4. Điều gì khiến mình sai', (239, 68, 68)),
            ('5. Quy mô vị thế, % danh mục', (255, 196, 0)),
            ('6. Điều kiện thoát, lãi và lỗ', (255, 196, 0)),
            ('7. Cảm xúc lúc quyết định', (255, 196, 0)),
            ('8. Ngày xem lại', (34, 197, 94))],
  'anh': 'checklist clipboard pen',
  'say': 'Mẫu gồm tám mục, mỗi mục chỉ một hai dòng. Mục một là mã và ngày. Mục hai là luận điểm trong đúng một câu, nếu không viết được một câu thì bạn chưa hiểu rõ vì sao mình mua. Mục ba là số '
         'liệu nền như P/E, P/B, ROE và tốc độ tăng trưởng, để sau này có cái so sánh. Mục bốn là điều gì sẽ khiến mình sai, đây là mục quan trọng nhất và hay bị bỏ qua nhất. Mục năm là quy mô vị '
         'thế, chiếm bao nhiêu phần trăm danh mục. Mục sáu là điều kiện thoát, gồm cả khi lãi và khi lỗ. Mục bảy là cảm xúc lúc quyết định, bình tĩnh, hào hứng hay sợ bỏ lỡ. Mục tám là ngày xem lại, '
         'thường sau ba đến sáu tháng. Tổng cộng chưa tới ba phút, nhưng đủ để tách quyết định có lý do khỏi quyết định theo đám đông.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Ví dụ điền mẫu với số liệu thật',
  'moc': True,
  'label': 'Ngân hàng MBB, số liệu quý 3/2026 và dữ liệu 5/11/2026 (chỉ minh họa cách ghi)',
  'cap': ('VÍ DỤ ĐIỀN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Số liệu nền', 'P/E 5,96 · P/B 1,23', 'ROE 21,8%'), ('Kết quả quý 3', 'LNST 8.039 tỷ (+44,3%)', 'thu nhập lãi thuần +37,3%'), ('Điểm cần soi', 'nợ xấu 1,67%', 'tăng từ 1,45% quý trước')],
  'anh': 'bank office building',
  'say': 'Giờ điền thử một mẫu với số liệu thật của một ngân hàng thương mại lớn, chỉ để minh họa cách ghi. Mục số liệu nền: P/E năm phẩy chín mươi sáu, P/B một phẩy hai mươi ba, ROE hai mươi mốt '
         'phẩy tám phần trăm. Kết quả quý ba: lợi nhuận sau thuế tám nghìn không trăm ba mươi chín tỷ, tăng bốn mươi bốn phẩy ba phần trăm, thu nhập lãi thuần tăng ba mươi bảy phẩy ba phần trăm. Mục '
         'điều gì khiến mình sai: tỷ lệ nợ xấu đã lên một phẩy sáu mươi bảy phần trăm từ một phẩy bốn mươi lăm quý trước, và bao phủ nợ xấu chỉ khoảng tám mươi lăm phần trăm. Nếu xu hướng nợ xấu '
         'tiếp tục tăng, luận điểm tăng trưởng sẽ yếu đi. Hãy chú ý cách viết: mỗi mục đều có một con số hoặc một điều kiện kiểm chứng được, thay vì những câu chung chung như doanh nghiệp tốt.'},
 {'k': 'checklist',
  'ch': 'Chương 4 – Ghi cả cảm xúc',
  'moc': True,
  'label': 'Cảm xúc là dữ liệu',
  'cap': ('GHI CẢM XÚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Hào hứng quá: dễ mua đuổi', (239, 68, 68)),
            ('Sợ bỏ lỡ: dấu hiệu của FOMO', (239, 68, 68)),
            ('Bình tĩnh: quyết định theo kế hoạch', (34, 197, 94)),
            ('Đánh giá lại sau 3–6 tháng, so sánh cảm xúc và kết quả', (56, 189, 248))],
  'anh': 'calm meditation desk',
  'say': 'Nhiều người ngại ghi cảm xúc vì thấy không liên quan đến phân tích. Thực ra đây là dữ liệu giá trị nhất. Sau vài tháng, bạn sẽ thấy các lệnh ghi hào hứng quá hay sợ bỏ lỡ thường có kết quả '
         'kém hơn các lệnh ghi bình tĩnh theo kế hoạch. Không phải lúc nào cũng vậy, nhưng nếu xu hướng đó có thật với bạn, bạn đã tìm ra một quy tắc cá nhân vô giá: khi cảm thấy hào hứng quá mức, '
         'hãy chờ một ngày trước khi đặt lệnh. Ngược lại, nếu các lệnh lúc sợ hãi lại hiệu quả hơn, bạn cũng học được điều gì đó về bản thân. Điểm mấu chốt là nhật ký biến cảm giác mơ hồ thành thống '
         'kê cá nhân, thứ mà không sách vở nào dạy thay bạn được.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Xem lại mỗi quý',
  'moc': True,
  'label': 'Ba câu hỏi khi đọc lại',
  'cap': ('XEM LẠI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Luận điểm của mình đúng, sai hay chưa rõ?', (56, 189, 248)),
            ('Điều mình lo có xảy ra không?', (56, 189, 248)),
            ('Mình thoát theo kế hoạch hay theo cảm xúc?', (255, 196, 0)),
            ('Ghi một bài học vào đầu nhật ký', (34, 197, 94))],
  'anh': 'quarterly review meeting',
  'say': 'Nhật ký chỉ có tác dụng khi xem lại. Mỗi quý hãy dành khoảng nửa tiếng đọc lại các mục đã ghi và trả lời ba câu hỏi. Luận điểm của mình đúng, sai hay chưa rõ. Điều mình lo ngại ở mục bốn '
         'có xảy ra không. Mình thoát theo kế hoạch ở mục sáu hay theo cảm xúc. Sau đó ghi một bài học lên đầu nhật ký, ví dụ tôi hay mua đuổi khi thấy tin tốt liên tiếp, hoặc tôi hay bán sớm khi '
         'lãi nhỏ. Trải qua vài quý, những bài học này sẽ thành bộ quy tắc riêng của bạn, phù hợp với tính cách và hoàn cảnh của bạn hơn bất kỳ phương pháp nào mượn từ người khác. Điều đáng quý là '
         'mọi quy tắc đều được rút ra từ dữ liệu của chính bạn.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Quy trình 3 lớp ra quyết định',
  'moc': True,
  'label': 'Từ ý tưởng đến lệnh',
  'cap': ('3 LỚP SÀNG LỌC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lớp 1 – Sàng lọc: ngành, quy mô, thanh khoản, nợ', (56, 189, 248)),
            ('Lớp 2 – Phân tích: lợi nhuận, dòng tiền, định giá', (255, 196, 0)),
            ('Lớp 3 – Thực thi: quy mô vị thế, điều kiện thoát', (34, 197, 94))],
  'anh': 'funnel process workflow',
  'say': 'Nhật ký sẽ hiệu quả hơn nếu đi cùng một quy trình ba lớp. Lớp một là sàng lọc: loại những doanh nghiệp quá nhỏ, thanh khoản kém, nợ quá cao hoặc ngành bạn không hiểu. Lớp hai là phân tích: '
         'đọc kết quả kinh doanh, dòng tiền, định giá so với lịch sử và so với đối thủ. Lớp ba là thực thi: quyết định bạn sẽ dùng bao nhiêu phần trăm danh mục, mua một lần hay chia nhiều lần, và '
         'điều kiện nào thì thoát. Một ý tưởng chỉ được đặt lệnh khi qua đủ ba lớp. Ưu điểm của quy trình này là bạn không phải nghĩ lại từ đầu mỗi lần, và khi thị trường biến động mạnh, bạn có '
         'khung để bám vào thay vì quyết định theo cảm giác. Quy trình đơn giản được dùng đều đặn luôn tốt hơn quy trình phức tạp bị bỏ giữa chừng.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những sai lầm khi ghi nhật ký',
  'moc': True,
  'label': 'Tránh để bỏ cuộc',
  'cap': ('4 SAI LẦM',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Ghi sau khi có kết quả', (239, 68, 68)), ('Chỉ ghi lệnh thắng', (239, 68, 68)), ('Viết quá dài nên bỏ dở', (239, 68, 68)), ('Không bao giờ đọc lại', (239, 68, 68))],
  'anh': 'abandoned notebook',
  'say': 'Bốn sai lầm khiến nhiều người bỏ nhật ký sau một tháng. Một, ghi sau khi đã có kết quả, khi đó nhật ký chỉ phản ánh trí nhớ đã bị chỉnh sửa. Hai, chỉ ghi các lệnh thắng, làm nhật ký thành '
         'album kỷ niệm thay vì công cụ học tập. Ba, viết quá dài khiến việc ghi thành gánh nặng, nên nhớ mỗi mục chỉ một hai dòng. Bốn, không bao giờ đọc lại, đây là sai lầm phổ biến nhất. Cách '
         'khắc phục đơn giản là đặt lịch nhắc xem lại ngay khi ghi, và chọn công cụ nhẹ như một tệp ghi chú trên điện thoại. Không cần phần mềm cầu kỳ. Quan trọng là nhật ký phải đơn giản đến mức '
         'bạn không có lý do để lười, và phải được ghi trước khi lệnh được đặt.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Ba ý ghi nhớ',
  'cap': ('3 Ý GHI NHỚ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Ghi lý do trước khi biết kết quả', (255, 196, 0)), ('Ghi cả điều có thể khiến mình sai', (239, 68, 68)), ('Đọc lại mỗi quý, rút ra quy tắc của riêng mình', (34, 197, 94))],
  'anh': 'journal pen sunrise',
  'say': 'Ba ý để mang theo. Một, ghi lý do trước khi biết kết quả, vì đó là bản gốc duy nhất không bị trí nhớ chỉnh sửa. Hai, ghi cả điều có thể khiến mình sai, vì đó là lớp bảo hiểm đầu tiên của '
         'bạn. Ba, đọc lại mỗi quý và rút ra quy tắc của riêng mình. Thị trường mười năm nữa sẽ khác, cổ phiếu bạn sở hữu cũng khác, nhưng thói quen nhìn lại chính mình để cải thiện sẽ vẫn là lợi '
         'thế lớn nhất của một nhà đầu tư cá nhân. Hãy thử ngay hôm nay: mở một tệp ghi chú, chép tám mục trong video và điền cho lệnh tiếp theo của bạn. Nếu bạn không có lệnh nào sắp tới, hãy điền '
         'cho một cổ phiếu bạn đang giữ, xem luận điểm hiện tại còn đúng không.'},
 {'k': 'end',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'GHI TRƯỚC, HỌC SAU'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu ngân hàng trong ví dụ lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày năm tháng mười một. Ví dụ điền mẫu chỉ để minh họa cách ghi, '
         'không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Quản trị vốn.'}]

S['CH0911C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – nến tuần một năm',
  'cap': ('7 ĐIỀU ĐỦ DÙNG', '10 NĂM KHÔNG ĐỔI'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, '5/11/26: 1.741', 2.6]]},
  'anh': 'mountain path journey long term',
  'say': 'Biểu đồ phía sau cho thấy chỉ số một năm qua có lúc xuống một nghìn năm trăm bảy mươi tám rồi lên một nghìn chín trăm ba mươi ba, chênh nhau hơn hai mươi hai phần trăm trong chưa đầy sáu '
         'tháng. Nếu bạn phải đoán hướng đi từng tuần, bạn sẽ mệt mỏi và thường sai. Nhưng nếu có bảy nguyên tắc đúng ở mọi thời điểm, bạn không cần đoán. Đây là video tổng kết seri Nền tảng đầu tư '
         'cho người mới, rút gọn mọi thứ thành bảy ý: sở hữu doanh nghiệp, đọc báo cáo trước giá, giá đi cùng giá trị, bảo toàn vốn, phân bổ vừa đủ, thời gian và lãi kép, và quản trị cảm xúc. Xem '
         'hết bạn sẽ có một lộ trình học ba tháng để bắt đầu. Nội dung không hứa hẹn lợi nhuận và được chọn để mười năm nữa xem lại vẫn dùng được.'},
 {'k': 'checklist',
  'ch': 'Nguyên tắc 1 và 2 – Sở hữu doanh nghiệp, đọc báo cáo trước giá',
  'moc': True,
  'label': 'Hai nền móng',
  'cap': ('NGUYÊN TẮC 1–2',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Mua cổ phiếu là sở hữu một phần doanh nghiệp thật', (56, 189, 248)), ('2. Đọc báo cáo kết quả, bảng cân đối, dòng tiền trước khi nhìn giá', (56, 189, 248))],
  'anh': 'business owner shop',
  'say': 'Nguyên tắc một: cổ phiếu là mảnh sở hữu của một doanh nghiệp thật với nhà máy, nhân viên, khách hàng. Khi bạn nghĩ mình là chủ doanh nghiệp, bạn tự nhiên quan tâm doanh nghiệp kiếm tiền '
         'thế nào chứ không chỉ giá nhảy ra sao. Nguyên tắc hai: đọc báo cáo trước khi nhìn giá. Ba báo cáo cơ bản là kết quả kinh doanh cho biết doanh nghiệp có lãi không, bảng cân đối cho biết '
         'doanh nghiệp mạnh hay yếu, và lưu chuyển tiền tệ cho biết lợi nhuận có thành tiền thật không. Bạn không cần đọc hết hàng trăm trang. Chỉ cần nắm doanh thu, lợi nhuận, nợ vay, tồn kho, '
         'khoản phải thu và dòng tiền kinh doanh, là đã lọc được rất nhiều doanh nghiệp chưa đủ chất lượng. Hai nguyên tắc đầu tiên này đưa bạn từ người đoán giá thành người phân tích doanh nghiệp.'},
 {'k': 'checklist',
  'ch': 'Nguyên tắc 3 và 4 – Giá đi cùng giá trị, bảo toàn vốn',
  'moc': True,
  'label': 'Hai nguyên tắc về rủi ro',
  'cap': ('NGUYÊN TẮC 3–4',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('3. Một doanh nghiệp tốt vẫn có thể là cổ phiếu đắt', (56, 189, 248)), ('4. Lỗ 50% cần lãi 100% mới hòa vốn, hãy tránh lỗ lớn', (239, 68, 68))],
  'anh': 'scale balance value',
  'say': 'Nguyên tắc ba: giá phải đi cùng giá trị. Một doanh nghiệp tốt mua ở giá quá cao vẫn có thể cho kết quả tồi trong nhiều năm. Các chỉ số P/E, P/B, ROE và tăng trưởng giúp bạn đặt giá vào bối '
         'cảnh, dù không có con số nào đúng tuyệt đối. Nguyên tắc bốn: bảo toàn vốn. Toán học của khoản lỗ không đối xứng: lỗ năm mươi phần trăm cần lãi một trăm phần trăm mới hòa vốn. Vì vậy ưu '
         'tiên số một không phải là kiếm thật nhiều trong năm nay, mà là không để mất những khoản lớn. Quy tắc thực tế là giới hạn rủi ro mỗi lệnh ở mức nhỏ so với tổng vốn, đặt điều kiện thoát từ '
         'trước và không dùng vốn vay vượt quá khả năng chịu đựng. Người còn vốn thì luôn còn cơ hội cho chu kỳ tiếp theo.'},
 {'k': 'checklist',
  'ch': 'Nguyên tắc 5 và 6 – Phân bổ vừa đủ, thời gian và lãi kép',
  'moc': True,
  'label': 'Hai nguyên tắc về thời gian',
  'cap': ('NGUYÊN TẮC 5–6',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('5. Không dồn hết vào một mã hay một ngành', (56, 189, 248)), ('6. Góp đều và giữ đủ lâu: lãi kép cần thời gian', (34, 197, 94))],
  'anh': 'growing plant coins',
  'say': 'Nguyên tắc năm: phân bổ vừa đủ. Không dồn tất cả vào một mã hay một ngành, nhưng cũng không chia nhỏ tới mức không theo dõi nổi. Với nhà đầu tư cá nhân, số mã vừa phải mà bạn hiểu rõ còn '
         'quan trọng hơn danh mục đẹp trên giấy. Nguyên tắc sáu: thời gian và lãi kép. Một trăm triệu với tỷ suất giả định mười phần trăm mỗi năm sau mười năm khoảng hai trăm năm mươi chín triệu, '
         'sau hai mươi năm khoảng sáu trăm bảy mươi ba triệu, phần lớn tăng thêm đến từ những năm sau. Đây là phép tính giả định, không phải cam kết, nhưng nó cho thấy kỷ luật góp đều và không bỏ '
         'cuộc giữa chừng quan trọng thế nào. Nhiều người mất lãi kép không vì chọn sai mã mà vì dừng lại đúng lúc thị trường giảm.'},
 {'k': 'checklist',
  'ch': 'Nguyên tắc 7 – Quản trị cảm xúc',
  'moc': True,
  'label': 'Kẻ thù lớn nhất thường là chính mình',
  'cap': ('NGUYÊN TẮC 7',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('7. Hệ thống tốt hơn cảm xúc', (255, 196, 0)), ('Viết kế hoạch trước, ghi nhật ký, xem lại định kỳ', (56, 189, 248)), ('Hào hứng quá hoặc sợ quá: đợi một ngày', (239, 68, 68))],
  'anh': 'calm person meditating',
  'say': 'Nguyên tắc cuối cùng và khó nhất là quản trị cảm xúc. Kiến thức tài chính ai cũng học được, nhưng khi tài khoản đỏ năm mươi phần trăm hoặc cổ phiếu quen thuộc tăng gấp đôi, không phải ai '
         'cũng giữ được kế hoạch. Cách thực tế không phải là cố gắng không có cảm xúc, mà là xây hệ thống để cảm xúc ít can thiệp. Viết kế hoạch trước khi vào lệnh, ghi nhật ký đầu tư, đặt quy tắc '
         'chờ một ngày khi quá hào hứng hoặc quá sợ, và xem lại định kỳ. Những quy tắc đơn giản này nghe tầm thường nhưng là khác biệt giữa người kiên trì mười năm và người bỏ cuộc sau hai cú giảm. '
         'Hãy nhớ rằng thị trường không trả công cho người thông minh nhất, mà thường trả công cho người nhất quán nhất.'},
 {'k': 'bars',
  'ch': 'Lãi kép nhìn bằng số',
  'moc': True,
  'label': 'Ví dụ giả định: 100 triệu đồng, tỷ suất không đổi (triệu đồng)',
  'cap': ('100 TRIỆU', 'SAU 10 NĂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('5%/năm', 162.9, (56, 189, 248), '163'), ('8%/năm', 215.9, (255, 196, 0), '216'), ('10%/năm', 259.4, (34, 197, 94), '259')],
  'anh': 'compound growth chart money',
  'say': 'Hãy nhìn lại lãi kép bằng số. Một trăm triệu đồng sau mười năm với tỷ suất giả định năm phần trăm mỗi năm thành khoảng một trăm sáu mươi ba triệu. Với tám phần trăm là khoảng hai trăm mười '
         'sáu triệu. Với mười phần trăm là khoảng hai trăm năm mươi chín triệu. Chênh lệch tỷ suất chỉ vài phần trăm nhưng sau mười năm chênh nhau gần một trăm triệu. Đây là lý do tối ưu chi phí, '
         'tránh những sai lầm lớn và duy trì lâu dài quan trọng không kém việc chọn mã. Tuy nhiên hãy nhớ đây là con số giả định, thị trường không trả đều đặn như vậy, có năm lãi, có năm lỗ. Điều '
         'đáng học không phải là con số, mà là cấu trúc: thời gian là hệ số nhân, và mọi lần dừng lại đều làm mất phần nhân của những năm sau.'},
 {'k': 'checklist',
  'ch': 'Lộ trình học 3 tháng',
  'moc': True,
  'label': 'Từng bước cho người mới',
  'cap': ('LỘ TRÌNH 3 THÁNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Tháng 1: cổ phiếu là gì, đọc kết quả kinh doanh, bảng cân đối', (56, 189, 248)),
            ('Tháng 2: dòng tiền, P/E, P/B, ROE, đọc một ngành', (255, 196, 0)),
            ('Tháng 3: quản trị vốn, nhật ký, thực hành với số vốn nhỏ', (34, 197, 94))],
  'anh': 'student studying planner',
  'say': 'Nếu bạn mới bắt đầu, đây là lộ trình học ba tháng. Tháng thứ nhất: hiểu cổ phiếu là gì, học đọc báo cáo kết quả kinh doanh và bảng cân đối, mỗi tuần đọc một doanh nghiệp. Tháng thứ hai: '
         'học dòng tiền, các chỉ số định giá P/E, P/B, ROE, và chọn một ngành để hiểu sâu, ví dụ ngân hàng. Tháng thứ ba: học quản trị vốn, lập nhật ký đầu tư, và nếu muốn thực hành, chỉ dùng một số '
         'vốn nhỏ mà bạn sẵn sàng mất để rút kinh nghiệm. Trong suốt ba tháng, hãy dùng các video của kênh theo từng seri, kết hợp dữ liệu miễn phí trên trang web. Mục tiêu của ba tháng này không '
         'phải là kiếm tiền, mà là xây nền tảng đúng để các quyết định sau đó dựa trên hiểu biết thay vì tin đồn.'},
 {'k': 'checklist',
  'ch': 'Bảy nguyên tắc trên một trang',
  'moc': True,
  'label': 'Chụp màn hình để giữ lại',
  'cap': ('BẢY NGUYÊN TẮC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Sở hữu doanh nghiệp · Đọc báo cáo trước giá', (56, 189, 248)),
            ('Giá đi cùng giá trị · Bảo toàn vốn', (56, 189, 248)),
            ('Phân bổ vừa đủ · Thời gian và lãi kép', (255, 196, 0)),
            ('Quản trị cảm xúc bằng hệ thống', (34, 197, 94))],
  'anh': 'summary whiteboard marker',
  'say': 'Để kết thúc, bảy nguyên tắc trên một trang. Sở hữu doanh nghiệp. Đọc báo cáo trước giá. Giá đi cùng giá trị. Bảo toàn vốn. Phân bổ vừa đủ. Thời gian và lãi kép. Quản trị cảm xúc bằng hệ '
         'thống. Bạn có thể chụp màn hình khung này để giữ lại. Mỗi nguyên tắc có một video riêng trong seri, hãy xem lại khi cần. Không nguyên tắc nào cho biết ngày mai thị trường tăng hay giảm, và '
         'đó là chủ ý: chúng tập trung vào những thứ bạn kiểm soát được, như cách chọn doanh nghiệp, cách dùng vốn và cách phản ứng. Mười năm nữa, giá cổ phiếu, lãi suất, và cả các chỉ số trong '
         'video này sẽ khác, nhưng bảy nguyên tắc vẫn dùng được. Cảm ơn bạn đã xem hết, hãy để lại bình luận nguyên tắc nào bạn thấy khó nhất để làm theo.'},
 {'k': 'end',
  'label': '',
  'cap': ('NỀN TẢNG ĐẦU TƯ', 'BẢY NGUYÊN TẮC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các ví dụ lãi kép là số giả định, không phải cam kết lợi nhuận. Biểu đồ chỉ số lấy từ dữ liệu tổng hợp đến ngày năm tháng mười một năm hai nghìn không trăm hai mươi sáu. Nội dung chia sẻ '
         'kiến thức, không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm.'}]

S['CH1011A'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VCB – Đọc BCTC 5 phút',
  'cap': ('LÃI QUÝ 3: +0,1%', 'LÃI LÕI: +39,1%'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VCBW', 'tf': 'W', 'weeks': 52, 'circles': [[10, 78.15, 'Đỉnh tuần 12/1/26: 78,15', 0.6], [36, 52.6, 'Đáy tuần 20/7/26: 52,60', 1.6], [51, 54.2, '5/11/26: 54,20', 2.6]]},
  'anh': 'bank headquarters building Vietnam',
  'say': 'Quý ba năm hai nghìn không trăm hai mươi sáu, một ngân hàng lớn nhất nhì thị trường báo lợi nhuận sau thuế tăng chỉ không phẩy một phần trăm so với cùng kỳ, nhìn qua tưởng như đứng yên. '
         'Nhưng cũng trong báo cáo đó, thu nhập lãi thuần, tức phần kiếm tiền cốt lõi của ngân hàng, tăng ba mươi chín phẩy một phần trăm. Vậy lợi nhuận đứng yên mà mảng cốt lõi tăng gần bốn mươi '
         'phần trăm, tiền đã đi đâu? Câu trả lời nằm ở một dòng nhỏ mà người mới ít khi đọc là chi phí dự phòng. Trong khoảng chín phút tới, mình đọc báo cáo này theo năm bước, từ thu nhập lãi, nợ '
         'xấu, bao phủ nợ xấu, chi phí dự phòng đến định giá bằng P/B và ROE. Đây là tập đầu của seri Đọc BCTC năm phút, dùng ngân hàng Vietcombank làm ví dụ minh họa với số liệu quý ba, không phải '
         'khuyến nghị.'},
 {'k': 'bars',
  'ch': 'Chương 1 – Bước 1: Thu nhập lãi thuần, động cơ chính',
  'moc': True,
  'label': 'Thu nhập lãi thuần VCB theo quý (tỷ đồng)',
  'cap': ('THU NHẬP', 'LÃI THUẦN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 14657.2, (56, 189, 248), '14.657'),
           ('Q4/25', 16266.8, (56, 189, 248), '16.267'),
           ('Q1/26', 17651.1, (56, 189, 248), '17.651'),
           ('Q2/26', 19141.8, (56, 189, 248), '19.142'),
           ('Q3/26', 20386.0, (34, 197, 94), '20.386')],
  'anh': 'bank counter customers',
  'say': 'Một ngân hàng kiếm tiền chủ yếu từ chênh lệch giữa lãi cho vay và lãi huy động, gọi là thu nhập lãi thuần. Đây là dòng đầu tiên cần đọc. Của ngân hàng trong ví dụ, năm quý gần nhất tăng '
         'đều: mười bốn nghìn sáu trăm năm mươi bảy tỷ quý ba năm ngoái, mười sáu nghìn hai trăm sáu mươi bảy tỷ, mười bảy nghìn sáu trăm năm mươi mốt tỷ, mười chín nghìn một trăm bốn mươi hai tỷ, '
         'và hai mươi nghìn ba trăm tám mươi sáu tỷ ở quý ba năm nay, tăng ba mươi chín phẩy một phần trăm so với cùng kỳ. Một chuỗi tăng đều như vậy cho thấy mảng cho vay và huy động đang vận hành '
         'tốt, tín dụng tăng hoặc chênh lệch lãi suất được cải thiện. Khi thu nhập lãi thuần tăng liên tục nhiều quý, đó là nền tảng của lợi nhuận bền vững hơn nhiều so với lãi bất thường từ các '
         'khoản một lần.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Bước 2: Lợi nhuận sau thuế theo quý',
  'moc': True,
  'label': 'LNST công ty mẹ VCB theo quý (tỷ đồng)',
  'cap': ('LỢI NHUẬN', 'SAU THUẾ'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Q3/25', 9020.5, (56, 189, 248), '9.021'),
           ('Q4/25', 8629.0, (56, 189, 248), '8.629'),
           ('Q1/26', 9456.6, (56, 189, 248), '9.457'),
           ('Q2/26', 14542.3, (255, 196, 0), '14.542'),
           ('Q3/26', 9033.3, (56, 189, 248), '9.033')],
  'anh': 'financial report table',
  'say': 'Bây giờ nhìn dòng dưới cùng. Lợi nhuận sau thuế quý ba năm nay là chín nghìn không trăm ba mươi ba tỷ, gần như bằng quý ba năm ngoái, chỉ tăng không phẩy một phần trăm. So với quý trước, '
         'lợi nhuận giảm ba mươi bảy phẩy chín phần trăm, nhưng đừng hoảng. Quý hai năm nay có lợi nhuận cao bất thường là mười bốn nghìn năm trăm bốn mươi hai tỷ, nên so với nó thì quý ba trông '
         'thấp. Nếu bạn cộng lũy kế chín tháng, lợi nhuận là ba mươi ba nghìn không trăm ba mươi hai tỷ, tăng hai mươi bốn phẩy bốn phần trăm so với cùng kỳ. Bài học đọc ở đây: đừng kết luận từ một '
         'quý và đừng chỉ so với quý liền kề. Hãy đặt quý đó trong chuỗi nhiều quý và kiểm tra có khoản bất thường nào không.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Bước 3: Chi phí dự phòng, nơi lợi nhuận bị giữ lại',
  'moc': True,
  'label': 'Quý 3/2026 theo dữ liệu tổng hợp',
  'cap': ('DỰ PHÒNG',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Thu nhập lãi thuần', '+39,1%', 'so với cùng kỳ'), ('Lợi nhuận sau thuế', '+0,1%', 'so với cùng kỳ'), ('Chi phí dự phòng', '+697,3%', 'trích lập tăng rất mạnh')],
  'anh': 'safe vault bank money',
  'say': 'Đây là câu trả lời cho câu hỏi ở đầu video. Khi thu nhập lãi thuần tăng ba mươi chín phẩy một phần trăm mà lợi nhuận gần như đứng yên, phần chênh nằm ở chi phí dự phòng, khoản ngân hàng '
         'trích ra để phòng nợ có thể không thu hồi được. Theo dữ liệu tổng hợp, chi phí dự phòng quý ba tăng sáu trăm chín mươi bảy phẩy ba phần trăm so với cùng kỳ. Hiểu thế nào? Có hai cách đọc. '
         'Cách thứ nhất là ngân hàng đang trích lập thận trọng hơn, tạo thêm đệm cho tương lai, điều này tốt về chất lượng nhưng làm lợi nhuận kỳ này thấp. Cách thứ hai là chất lượng tài sản có dấu '
         'hiệu xấu đi nên buộc phải trích nhiều. Muốn biết cách nào đúng, bước tiếp theo là nhìn tỷ lệ nợ xấu và bao phủ nợ xấu.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Bước 4: Nợ xấu và bao phủ nợ xấu',
  'moc': True,
  'label': 'Vietcombank quý 3/2026',
  'cap': ('NỢ XẤU & BAO PHỦ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Tỷ lệ nợ xấu', '0,71%', 'thấp'), ('Bao phủ nợ xấu', 'khoảng 243%', 'dự phòng gấp hơn 2 lần nợ xấu'), ('Hàm ý', 'đệm dày', 'dự phòng có thể là thận trọng')],
  'anh': 'shield protection safety',
  'say': 'Tỷ lệ nợ xấu của ngân hàng trong ví dụ là không phẩy bảy mươi mốt phần trăm, thuộc nhóm thấp. Bao phủ nợ xấu, tức quỹ dự phòng chia cho nợ xấu, là khoảng hai trăm bốn mươi ba phần trăm. '
         'Nghĩa là cứ một đồng nợ xấu thì đã có hơn hai đồng dự phòng. Kết hợp hai con số này với chi phí dự phòng tăng mạnh ở bước ba, cách đọc thiên về thận trọng nhiều hơn là lo ngại: chất lượng '
         'tài sản đang tốt, và ngân hàng tiếp tục làm dày thêm đệm. Tất nhiên, đây là bức tranh tại một quý. Người phân tích sẽ theo dõi tiếp xem nợ xấu có tăng không, nhóm nợ cần chú ý có phình ra '
         'không, và chi phí dự phòng quý sau thế nào. So sánh với các ngân hàng khác cùng kỳ cũng cho thấy tỷ lệ bao phủ khác nhau rất xa, nên con số cần đọc trong bối cảnh từng ngân hàng.'},
 {'k': 'cards',
  'ch': 'Chương 5 – Bước 5: Định giá bằng P/B và ROE',
  'moc': True,
  'label': 'Dữ liệu tổng hợp 5/11/2026',
  'cap': ('P/B VÀ ROE',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('P/E', '10,99', 'giá / lợi nhuận một cổ phiếu'), ('P/B', '1,81', 'giá / giá trị sổ sách'), ('ROE', '17,6%', 'lợi nhuận / vốn chủ')],
  'anh': 'valuation scale chart',
  'say': 'Cuối cùng là định giá. Theo dữ liệu tổng hợp ngày năm tháng Mười Một, ngân hàng trong ví dụ có P/E mười phẩy chín mươi chín, P/B một phẩy tám mươi mốt và ROE mười bảy phẩy sáu phần trăm. '
         'Với ngân hàng, P/B và ROE đi cùng nhau: ROE càng cao và càng bền thì mức P/B hợp lý càng cao. Bạn có thể so P/B một phẩy tám mươi mốt này với P/B của các ngân hàng cùng quy mô, với chính '
         'nó trong vài năm trước, và đặt cạnh ROE để xem mức giá đang phản ánh điều gì. Biểu đồ nến tuần phía sau cho thấy giá từng ở vùng bảy mươi tám nghìn đồng vào tuần mười hai tháng Một, và '
         'xuống vùng năm mươi hai nghìn sáu trăm vào tuần hai mươi tháng Bảy, tức biên độ lớn trong một năm, dù lợi nhuận cốt lõi tăng đều. Giá và giá trị có thể lệch nhau rất lâu.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Ba câu hỏi nên đặt thêm',
  'moc': True,
  'label': 'Khi đã đọc xong năm bước',
  'cap': ('3 CÂU HỎI THÊM',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lợi nhuận bất thường quý trước đến từ đâu?', (56, 189, 248)),
            ('Dự phòng tăng là thận trọng hay chất lượng tài sản xấu đi?', (239, 68, 68)),
            ('Tín dụng tăng bao nhiêu, và có đang chạy theo tăng trưởng?', (255, 196, 0))],
  'anh': 'analyst question mark thinking',
  'say': 'Đọc xong năm bước, vẫn còn ba câu hỏi để đào sâu. Thứ nhất, khoản lợi nhuận cao bất thường ở quý hai đến từ đâu, từ hoàn nhập dự phòng, từ thu hồi nợ, hay từ một giao dịch một lần, vì điều '
         'này quyết định lợi nhuận quý hai có lặp lại không. Thứ hai, việc trích dự phòng quý ba tăng vọt là thận trọng chủ động hay là phản ứng với chất lượng tài sản xấu đi, bạn xem trong thuyết '
         'minh về nợ nhóm hai và nợ cần chú ý. Thứ ba, tín dụng đang tăng bao nhiêu phần trăm, và tăng trưởng nhanh có đi kèm chất lượng tín dụng chặt hay không. Báo cáo tài chính cho bạn dữ liệu, '
         'còn buổi họp với cổ đông và bản cáo bạch cho bạn lời giải thích. Người đọc kỹ thường dành mười phút đọc phần giải trình của ban lãnh đạo.'},
 {'k': 'checklist',
  'ch': 'Chương 7 – Những cái bẫy khi đọc báo cáo ngân hàng',
  'moc': True,
  'label': 'Bốn điều dễ nhầm',
  'cap': ('4 CÁI BẪY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Chỉ nhìn lợi nhuận quý, bỏ qua thu nhập lãi thuần', (239, 68, 68)),
            ('So với quý trước khi quý trước có khoản bất thường', (239, 68, 68)),
            ('Thấy nợ xấu thấp là yên tâm, bỏ qua nhóm nợ cần chú ý', (239, 68, 68)),
            ('Dùng P/E để so ngân hàng khác mô hình', (239, 68, 68))],
  'anh': 'trap danger sign',
  'say': 'Bốn cái bẫy phổ biến. Một là chỉ nhìn lợi nhuận quý mà bỏ qua thu nhập lãi thuần, nên không phân biệt được lợi nhuận tăng nhờ kinh doanh cốt lõi hay nhờ khoản một lần. Hai là so với quý '
         'trước khi quý trước có khoản bất thường, như ví dụ quý hai ở trên. Ba là thấy tỷ lệ nợ xấu thấp là yên tâm, trong khi nợ nhóm hai và nợ cần chú ý mới là nơi nợ xấu tương lai xuất hiện '
         'trước. Bốn là dùng P/E để so sánh các ngân hàng có mô hình rất khác nhau, trong khi P/B kết hợp ROE phản ánh tốt hơn chất lượng vốn. Tránh bốn cái bẫy này bạn đã đọc báo cáo ngân hàng tốt '
         'hơn nhiều người xem tin tức. Đừng quên mỗi ngân hàng một đặc thù, đừng áp khuôn.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Khung 5 bước đọc ngân hàng',
  'cap': ('5 BƯỚC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('1. Thu nhập lãi thuần: động cơ cốt lõi', (56, 189, 248)),
            ('2. Lợi nhuận: nhìn chuỗi, loại khoản bất thường', (56, 189, 248)),
            ('3. Chi phí dự phòng: lợi nhuận bị giữ lại hay bị ăn mòn', (255, 196, 0)),
            ('4. Nợ xấu và bao phủ: độ dày của đệm', (255, 196, 0)),
            ('5. P/B và ROE: giá so với chất lượng', (34, 197, 94))],
  'anh': 'notebook five steps',
  'say': 'Khung năm bước đọc ngân hàng: thu nhập lãi thuần cho biết động cơ cốt lõi, lợi nhuận cho thấy kết quả sau cùng nhưng cần nhìn chuỗi và loại khoản bất thường, chi phí dự phòng cho biết lợi '
         'nhuận bị giữ lại hay bị ăn mòn, nợ xấu và bao phủ cho biết độ dày của đệm, P/B cùng ROE đặt giá cạnh chất lượng. Số liệu quý ba năm hai nghìn không trăm hai mươi sáu mười năm nữa sẽ không '
         'còn, nhưng khung này vẫn dùng được cho bất kỳ ngân hàng nào ở bất kỳ quý nào. Hãy thử áp dụng cho một ngân hàng khác trong danh mục quan tâm của bạn, mất khoảng năm phút nếu có sẵn số '
         'liệu. Dữ liệu từng mã có miễn phí trên trang web của kênh. Kết quả luôn có hai nửa: con số và câu hỏi tại sao, và nửa thứ hai mới là phần có giá trị.'},
 {'k': 'end',
  'label': '',
  'cap': ('ĐỌC BCTC 5 PHÚT', 'VCB'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Số liệu của ngân hàng trong video lấy từ báo cáo tài chính quý ba năm hai nghìn không trăm hai mươi sáu và dữ liệu tổng hợp ngày năm tháng mười một. Video dùng ngân hàng làm ví dụ minh '
         'họa, không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Đọc BCTC năm phút.'}]

S['CH1011B'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – nến tuần một năm',
  'cap': ('GỬI TIẾT KIỆM', 'AN TOÀN? CHƯA CHẮC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, '5/11/26: 1.741', 2.6]]},
  'anh': 'savings bank deposit piggy',
  'say': 'Gửi một trăm triệu vào ngân hàng với lãi năm phần trăm một năm, mười năm sau bạn có một trăm sáu mươi ba triệu. Nghe rất an toàn. Nhưng nếu giá cả tăng sáu phần trăm mỗi năm, số tiền một '
         'trăm sáu mươi ba triệu đó chỉ mua được lượng hàng tương đương chín mươi mốt triệu hôm nay. Bạn không mất một đồng nào trên sổ tiết kiệm, nhưng mất gần một phần mười sức mua. Đó là rủi ro '
         'không có tên trên sổ. Trong video này mình so sánh hai loại rủi ro: rủi ro biến động của cổ phiếu và rủi ro mất sức mua của tiền gửi, bằng số tính tay. Xem hết bạn sẽ biết khi nào tiết '
         'kiệm là lựa chọn đúng, khi nào chỉ riêng nó là chưa đủ, và vì sao câu trả lời không bao giờ là chọn một bỏ một. Các con số lãi suất và lạm phát trong bài là giả định để tính, không phải số '
         'liệu hiện hành, và video không khuyên bạn chuyển tiền.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Hai loại rủi ro',
  'moc': True,
  'label': 'Rủi ro nhìn thấy và rủi ro không nhìn thấy',
  'cap': ('2 LOẠI RỦI RO',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Cổ phiếu', 'biến động mạnh', 'giá có thể giảm 20–40%'),
            ('Tiền gửi', 'số dư không giảm', 'nhưng sức mua có thể giảm'),
            ('Kết luận', 'không có lựa chọn không rủi ro', 'chỉ là loại rủi ro khác nhau')],
  'anh': 'two roads decision fork',
  'say': 'Phần lớn chúng ta sợ rủi ro nhìn thấy: cổ phiếu có thể giảm hai mươi, ba mươi phần trăm và tài khoản đỏ rực. Chúng ta ít sợ rủi ro không nhìn thấy: tiền gửi ngân hàng số dư không bao giờ '
         'giảm, nhưng nếu giá cả tăng nhanh hơn lãi suất, sức mua của số tiền đó giảm dần mà bạn không thấy con số đỏ nào. Cả hai đều là rủi ro thật, chỉ khác hình thức. Rủi ro của cổ phiếu là biến '
         'động và có thể lỗ vốn nếu bán lúc giá thấp. Rủi ro của tiền gửi là lãi thực âm hoặc rất thấp trong thời gian dài. Câu hỏi đúng không phải là cái nào an toàn, mà là tôi cần tiền vào lúc '
         'nào, và tôi chịu được loại rủi ro nào ít khó chịu hơn với mục tiêu của mình.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Sức mua thật của 100 triệu sau 10 năm',
  'moc': True,
  'label': 'Gửi lãi 5%/năm, lạm phát giả định thay đổi (triệu đồng tính theo giá hôm nay)',
  'cap': ('SỨC MUA', 'SAU 10 NĂM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Lạm phát 3%', 121.2, (34, 197, 94), '121'), ('Lạm phát 4%', 110.0, (56, 189, 248), '110'), ('Lạm phát 6%', 91.0, (239, 68, 68), '91')],
  'anh': 'shopping cart groceries prices',
  'say': 'Đây là phép tính giả định. Một trăm triệu gửi lãi năm phần trăm mỗi năm, sau mười năm thành một trăm sáu mươi ba triệu trên sổ. Nhưng hãy chia cho mức tăng giá chung. Nếu lạm phát ba phần '
         'trăm mỗi năm, sức mua thật là khoảng một trăm hai mươi mốt triệu hôm nay. Nếu lạm phát bốn phần trăm, là khoảng một trăm mười triệu. Nếu lạm phát sáu phần trăm, chỉ còn khoảng chín mươi '
         'mốt triệu. Như vậy chênh lệch giữa lãi suất và lạm phát, gọi là lãi suất thực, mới là thứ quyết định bạn giàu lên hay không, chứ không phải con số danh nghĩa trên sổ. Tất nhiên, lãi suất '
         'và lạm phát thay đổi theo thời gian và không bao giờ cố định mười năm như ví dụ này, nhưng nguyên lý thì luôn đúng.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Tiết kiệm làm tốt việc gì',
  'moc': True,
  'label': 'Đừng bỏ nó đi',
  'cap': ('VAI TRÒ', 'TIẾT KIỆM'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Quỹ khẩn cấp', '3–6 tháng chi tiêu', 'tiền phải có ngay khi cần'),
            ('Mục tiêu ngắn hạn', 'dưới 2–3 năm', 'không nên chịu biến động'),
            ('Đệm tâm lý', 'giúp bạn không bán cổ phiếu vì cần tiền', 'giữ kỷ luật')],
  'anh': 'emergency fund umbrella',
  'say': 'Phần này quan trọng để tránh hiểu lầm. Video không nói tiết kiệm là tệ. Tiết kiệm làm rất tốt ba việc. Thứ nhất là quỹ khẩn cấp, thường được khuyên bằng ba đến sáu tháng chi tiêu, để khi '
         'mất việc hay ốm đau bạn không phải bán tài sản đầu tư vào lúc xấu nhất. Thứ hai là các mục tiêu ngắn hạn, như học phí hay mua nhà trong hai ba năm tới, nơi bạn cần chắc chắn số tiền có đủ '
         'chứ không cần tối đa hóa lợi nhuận. Thứ ba là đệm tâm lý: biết mình có đủ tiền mặt giúp bạn bình tĩnh giữ cổ phiếu khi thị trường giảm, thay vì bán vì sợ. Nói cách khác, tiết kiệm và cổ '
         'phiếu không phải đối thủ. Chúng làm hai việc khác nhau trong cùng một kế hoạch tài chính.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Dữ liệu thật: chỉ số đi lên nhưng không đi thẳng',
  'moc': True,
  'label': 'VN-Index theo dữ liệu giá đóng cửa',
  'cap': ('VN-INDEX 3 NĂM',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('27/10/2023', '1.060 điểm', 'đầu chuỗi dữ liệu'), ('5/11/2026', '1.741 điểm', 'tăng khoảng 64%'), ('Trên đường đi', '4 nhịp giảm trên 10%', 'từ 10,5% đến 18,1%')],
  'anh': 'stock market upward trend chart',
  'say': 'Giờ nhìn dữ liệu thật của cổ phiếu. Chỉ số VN-Index đóng cửa ở khoảng một nghìn không trăm sáu mươi điểm vào cuối tháng Mười năm hai nghìn không trăm hai mươi ba và ở một nghìn bảy trăm '
         'bốn mươi mốt điểm vào ngày năm tháng Mười Một năm nay, tăng khoảng sáu mươi bốn phần trăm trong ba năm. Nhưng trên đường đi có bốn nhịp giảm trên mười phần trăm, nhịp sâu nhất khoảng mười '
         'tám phần trăm. Người cầm cổ phiếu phải chịu những nhịp đó. Cũng xin nhấn mạnh: đây là kết quả quá khứ của một chỉ số, không phải cam kết, và từng cổ phiếu riêng lẻ có thể khác xa. Điều dữ '
         'liệu cho thấy là cổ phiếu có thể sinh lời cao hơn lạm phát trong dài hạn, nhưng đi kèm biến động mà tiết kiệm không có.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Thời gian quyết định loại rủi ro',
  'moc': True,
  'label': 'Càng dài hạn, rủi ro càng đổi chỗ',
  'cap': ('THEO THỜI GIAN',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Dưới 3 năm: ưu tiên chắc chắn, biến động là rủi ro chính', (56, 189, 248)),
            ('3–7 năm: kết hợp, tăng dần phần biến động', (255, 196, 0)),
            ('Trên 10 năm: mất sức mua dần là rủi ro lớn hơn', (34, 197, 94))],
  'anh': 'timeline calendar years',
  'say': 'Một cách nghĩ hữu ích là xem thời gian bạn cần tiền. Với tiền cần dùng trong dưới ba năm, rủi ro chính là biến động, vì bạn có thể phải bán đúng lúc giá thấp, nên ưu tiên chắc chắn là hợp '
         'lý. Với tiền cần sau ba đến bảy năm, nhiều người kết hợp cả hai, tăng dần phần chịu biến động. Với tiền để dài hạn, mười năm hay hơn, rủi ro mất sức mua dần có thể lớn hơn rủi ro biến '
         'động, vì bạn có đủ thời gian để đi qua các nhịp giảm. Dĩ nhiên, đây là khung suy nghĩ chung, không phải lời khuyên cá nhân. Hoàn cảnh mỗi người khác nhau về thu nhập, nghĩa vụ tài chính, '
         'tâm lý, và bạn nên tính toán cho riêng mình hoặc trao đổi với người tư vấn có chuyên môn.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Năm câu hỏi trước khi chuyển tiền từ nơi này sang nơi khác',
  'moc': True,
  'label': 'Đừng quyết định theo cảm xúc',
  'cap': ('5 CÂU HỎI',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Tiền này tôi cần dùng khi nào?', (56, 189, 248)),
            ('Tôi có đủ quỹ khẩn cấp chưa?', (56, 189, 248)),
            ('Nếu tài khoản giảm 30%, tôi có bán không?', (239, 68, 68)),
            ('Tôi hiểu thứ mình mua không?', (255, 196, 0)),
            ('Tôi có kế hoạch góp đều thay vì dồn một lần?', (34, 197, 94))],
  'anh': 'checklist decision notebook',
  'say': 'Năm câu hỏi giúp bạn quyết định tỉnh táo. Tiền này tôi cần dùng khi nào. Tôi đã có quỹ khẩn cấp đủ chưa. Nếu tài khoản giảm ba mươi phần trăm, tôi có bán hay không, vì nếu câu trả lời là '
         'có thì tỷ trọng của bạn đang quá cao. Tôi có hiểu thứ mình đang mua không. Và tôi có kế hoạch góp đều từng tháng thay vì dồn một lần vào thời điểm tâm lý hào hứng nhất không. Ba câu đầu '
         'bảo vệ bạn khỏi rủi ro biến động, hai câu sau bảo vệ bạn khỏi rủi ro hành vi. Nhiều người chuyển hết tiền tiết kiệm sang cổ phiếu khi thị trường nóng rồi chuyển ngược lại khi thị trường '
         'lạnh, hậu quả là mua cao bán thấp. Một quy trình đều đặn luôn thắng một quyết định bốc đồng.'},
 {'k': 'cards',
  'ch': 'Chương 7 – Góp đều: cách làm dịu biến động',
  'moc': True,
  'label': 'Ví dụ giả định: góp 5 triệu mỗi tháng',
  'cap': ('GÓP ĐỀU',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Mỗi tháng', '5 triệu', 'không cần đoán thời điểm'),
            ('Giá thấp', 'mua được nhiều hơn', 'giá trung bình được kéo xuống'),
            ('Kỷ luật', 'quan trọng hơn thời điểm', 'không bỏ cuộc giữa chừng')],
  'anh': 'monthly savings calendar coins',
  'say': 'Góp đều là cách nhiều người dùng để vừa đi vào cổ phiếu vừa giảm nỗi sợ chọn sai thời điểm. Mỗi tháng bạn bỏ một khoản cố định, ví dụ năm triệu đồng. Khi giá cao, khoản tiền đó mua được ít '
         'cổ phiếu hơn. Khi giá thấp, mua được nhiều hơn. Theo thời gian, giá vốn trung bình của bạn thường thấp hơn giá trung bình của thị trường. Điểm hay hơn cả là phương pháp này loại bỏ gánh '
         'nặng đoán đáy đoán đỉnh. Nhưng nó chỉ hiệu quả nếu bạn không bỏ cuộc khi thị trường giảm, vì chính các tháng giá thấp là lúc góp đều phát huy tác dụng. Đây cũng là nội dung mà nhiều tài '
         'liệu trên kênh gọi là tích sản, với nguyên tắc phương pháp không sợ sai, chỉ sợ theo giữa chừng rồi đổi ý.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Ba ý ghi nhớ',
  'cap': ('3 Ý GHI NHỚ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Lãi thực = lãi suất − lạm phát, không phải con số trên sổ', (255, 196, 0)),
            ('Tiết kiệm và cổ phiếu làm hai việc khác nhau', (56, 189, 248)),
            ('Thời gian cần tiền quyết định mức biến động chịu được', (34, 197, 94))],
  'anh': 'sunrise long road horizon',
  'say': 'Ba ý mang theo mười năm. Một, nhìn lãi thực chứ không nhìn lãi danh nghĩa, vì lãi suất trừ lạm phát mới cho biết sức mua thay đổi thế nào. Hai, tiết kiệm và cổ phiếu làm hai việc khác nhau '
         'trong cùng một kế hoạch, một cho sự chắc chắn, một cho tăng trưởng dài hạn có biến động. Ba, thời gian bạn cần tiền quyết định mức biến động bạn có thể chịu được. Con số lãi suất, lạm phát '
         'và chỉ số năm nay mười năm nữa sẽ khác hẳn, nhưng cách nghĩ này không đổi. Hãy bắt đầu bằng việc đơn giản: tính xem lãi suất bạn đang nhận trừ đi mức tăng giá chung hiện tại còn bao nhiêu, '
         'rồi tự hỏi số tiền nào trong tài sản của bạn thật sự cần chắc chắn và số tiền nào có thể để dài hạn. Chỉ riêng việc đặt câu hỏi đó đã là bước đi đúng.'},
 {'k': 'end',
  'label': '',
  'cap': ('NỀN TẢNG ĐẦU TƯ', 'LÃI THỰC MỚI QUAN TRỌNG'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các mức lãi suất và lạm phát trong video là giả định để tính, không phải số liệu hiện hành. Số liệu VN-Index lấy từ dữ liệu tổng hợp đến ngày năm tháng mười một năm hai nghìn không trăm '
         'hai mươi sáu, là kết quả quá khứ, không phải cam kết lợi nhuận. Nội dung chia sẻ kiến thức, không phải tư vấn đầu tư. Hãy đăng ký kênh để xem thêm.'}]

S['CH1011C'] = [{'k': 'hook',
  'ch': 'Mở đầu',
  'moc': True,
  'label': 'VN-Index – nến tuần một năm',
  'cap': ('DANH MỤC -25%', 'VỐN CÒN 50%?'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'chart': {'sym': 'VNINDEXW',
            'tf': 'W',
            'weeks': 52,
            'circles': [[1, 1578.42, 'Đáy tuần 10/11/25: 1.578', 0.6], [27, 1933.11, 'Đỉnh tuần 18/5/26: 1.933', 1.6], [51, 1740.73, '5/11/26: 1.741', 2.6]]},
  'anh': 'margin loan leverage risk',
  'say': 'Bạn có một trăm triệu tiền mình và vay thêm một trăm triệu để mua cổ phiếu, tổng tài sản hai trăm triệu. Danh mục giảm hai mươi lăm phần trăm. Bạn nghĩ mình mất hai mươi lăm phần trăm? '
         'Không. Tài sản còn một trăm năm mươi triệu, nợ vẫn một trăm triệu, vốn của bạn chỉ còn năm mươi triệu, tức mất đúng một nửa. Chỉ cần giảm thêm vài phần trăm nữa là chạm ngưỡng bị bán giải '
         'chấp. Trong video này mình tính tay toán học của đòn bẩy, từ vay một đổi một đến vay hai đổi một, lãi vay ăn mòn thế nào, cơ chế gọi bổ sung ký quỹ và bán giải chấp, rồi năm quy tắc dùng '
         'đòn bẩy nếu bạn vẫn muốn dùng. Xem hết bạn sẽ hiểu vì sao đòn bẩy là nhân vật chính của mọi cú sập lịch sử. Các tỷ lệ ngưỡng trong bài là giả định, thực tế mỗi công ty chứng khoán quy định '
         'khác nhau.'},
 {'k': 'cards',
  'ch': 'Chương 1 – Đòn bẩy là gì',
  'moc': True,
  'label': 'Ví dụ giả định: vốn 100 triệu, vay 100 triệu',
  'cap': ('ĐÒN BẨY 1:1',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Tài sản', '200 triệu', 'vốn 100 + vay 100'), ('Nợ', '100 triệu', 'luôn phải trả'), ('Vốn của bạn', '100 triệu', 'tài sản trừ nợ')],
  'anh': 'balance scale debt equity',
  'say': 'Đòn bẩy là dùng tiền vay để mua nhiều hơn số vốn của mình. Với một trăm triệu vốn và một trăm triệu vay, bạn kiểm soát hai trăm triệu cổ phiếu. Nếu danh mục tăng hai mươi phần trăm, tài '
         'sản lên hai trăm bốn mươi triệu, trừ nợ một trăm triệu còn một trăm bốn mươi triệu, bạn lãi bốn mươi phần trăm trên vốn của mình, gấp đôi mức tăng. Nghe hấp dẫn. Nhưng đòn bẩy là con dao '
         'hai lưỡi cân xứng: khi danh mục giảm hai mươi phần trăm, tài sản còn một trăm sáu mươi triệu, trừ nợ còn sáu mươi triệu, bạn lỗ bốn mươi phần trăm. Và nợ thì không giảm khi giá giảm, nên '
         'mỗi đồng lỗ đều đến từ vốn của bạn. Đòn bẩy không tạo ra lợi thế, nó chỉ nhân đôi kết quả theo cả hai hướng.'},
 {'k': 'bars',
  'ch': 'Chương 2 – Vốn còn lại khi danh mục giảm 20%',
  'moc': True,
  'label': 'Ví dụ giả định, vốn ban đầu 100 triệu (triệu đồng)',
  'cap': ('GIẢM 20%:', 'VỐN CÒN'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'bars': [('Không vay', 80, (34, 197, 94), '80'), ('Vay 1 đổi 1', 60, (255, 196, 0), '60'), ('Vay 2 đổi 1', 40, (239, 68, 68), '40')],
  'anh': 'red arrow downward chart',
  'say': 'Đây là so sánh trực quan. Cùng vốn một trăm triệu, cùng danh mục giảm hai mươi phần trăm. Không vay, bạn còn tám mươi triệu. Vay một đổi một, nghĩa là vay thêm bằng vốn của mình, bạn còn '
         'sáu mươi triệu. Vay hai đổi một, tức tổng tài sản ba trăm triệu, nợ hai trăm triệu, giảm hai mươi phần trăm còn hai trăm bốn mươi triệu, trừ nợ chỉ còn bốn mươi triệu, bạn mất sáu mươi '
         'phần trăm vốn. Điều cần nhớ là để hòa vốn lại từ mức bốn mươi triệu về một trăm triệu, bạn cần lãi một trăm năm mươi phần trăm. Cùng cú giảm hai mươi phần trăm của thị trường, kết quả của '
         'ba người khác nhau hoàn toàn chỉ vì cách dùng vốn. Mà cú giảm hai mươi phần trăm, như bài học lịch sử đã cho thấy, là chuyện xảy ra vài năm một lần.'},
 {'k': 'cards',
  'ch': 'Chương 3 – Gọi bổ sung ký quỹ và bán giải chấp',
  'moc': True,
  'label': 'Ví dụ giả định: ngưỡng cảnh báo 30%, ngưỡng giải chấp 20% vốn/tài sản',
  'cap': ('NGƯỠNG GIẢ ĐỊNH',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Ban đầu', 'vốn 50% tài sản', 'vay 1 đổi 1'), ('Cảnh báo', 'tài sản giảm ≈ 28,6%', 'vốn còn 30% tài sản'), ('Giải chấp', 'tài sản giảm 37,5%', 'vốn còn 20% tài sản')],
  'anh': 'warning alert margin call',
  'say': 'Công ty chứng khoán yêu cầu bạn duy trì tỷ lệ vốn của bạn so với tài sản không thấp hơn một ngưỡng. Với ví dụ vay một đổi một, ban đầu vốn chiếm năm mươi phần trăm. Nếu ngưỡng cảnh báo là '
         'ba mươi phần trăm, tài sản chỉ cần giảm khoảng hai mươi tám phẩy sáu phần trăm là bạn nhận yêu cầu nộp thêm tiền. Nếu ngưỡng giải chấp là hai mươi phần trăm, tài sản giảm ba mươi bảy phẩy '
         'năm phần trăm là hệ thống tự bán cổ phiếu của bạn, bất kể giá lúc đó có hợp lý hay không. Quan trọng nhất, lệnh bán giải chấp xảy ra khi giá thấp, tức là biến khoản lỗ tạm thời thành khoản '
         'lỗ thật. Và khi hàng nghìn tài khoản cùng bị giải chấp, họ cùng bán, giá giảm thêm, kéo thêm tài khoản khác chạm ngưỡng. Đó là cơ chế dây chuyền đã nhấn chìm nhiều cú sập.'},
 {'k': 'cards',
  'ch': 'Chương 4 – Lãi vay: khoản chi phí không ngủ',
  'moc': True,
  'label': 'Ví dụ giả định: lãi vay 12%/năm, vay 100 triệu',
  'cap': ('CHI PHÍ LÃI VAY',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Mỗi năm', '12 triệu', '12% của 100 triệu vay'), ('Mỗi tháng', '1 triệu', 'trả dù lãi hay lỗ'), ('Hòa vốn', 'danh mục phải lãi 6%', 'chỉ để trả lãi vay (trên 200 triệu)')],
  'anh': 'interest rate percent calculator',
  'say': 'Ngoài rủi ro giảm giá, tiền vay có lãi. Với lãi vay giả định mười hai phần trăm mỗi năm cho khoản vay một trăm triệu, bạn phải trả mười hai triệu mỗi năm, khoảng một triệu mỗi tháng, bất '
         'kể danh mục lãi hay lỗ. Tính trên tổng tài sản hai trăm triệu, danh mục phải lãi ít nhất sáu phần trăm mỗi năm chỉ để trả lãi vay mà chưa có đồng lãi nào cho bạn. Nếu thị trường đi ngang '
         'một năm, người không vay hòa vốn, còn người vay đã mất mười hai phần trăm trên vốn của mình. Lãi vay là nguyên nhân khiến đòn bẩy phù hợp nhất với các cơ hội ngắn hạn có xác suất cao, và '
         'rất tệ với cổ phiếu mà bạn định giữ nhiều năm, vì chi phí cộng dồn mỗi ngày trong khi phần thưởng chưa chắc đến.'},
 {'k': 'checklist',
  'ch': 'Chương 5 – Vì sao đòn bẩy giết chết nhiều tài khoản',
  'moc': True,
  'label': 'Ba cơ chế hại',
  'cap': ('3 CƠ CHẾ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Toán học không đối xứng: lỗ nhanh hơn, hồi phục chậm hơn', (239, 68, 68)),
            ('Mất quyền chọn: bị bán dù giá hợp lý', (239, 68, 68)),
            ('Tâm lý: nhìn vốn teo lại, quyết định méo mó', (239, 68, 68))],
  'anh': 'chess pieces strategy loss',
  'say': 'Có ba cơ chế khiến đòn bẩy giết nhiều tài khoản hơn là thị trường giảm. Thứ nhất là toán học không đối xứng: lỗ nhiều thì cần lãi nhiều hơn để hòa vốn, và đòn bẩy làm bước lỗ nhanh hơn. '
         'Thứ hai là mất quyền chọn. Người không vay có thể chờ cổ phiếu hồi phục, người vay bị buộc bán khi chạm ngưỡng, mất cơ hội cho thị trường đảo chiều. Thứ ba là tâm lý: khi thấy vốn teo lại '
         'với tốc độ gấp đôi, quyết định của bạn bị méo mó, dễ bán hoảng loạn hoặc vay thêm để gỡ, càng làm tình hình xấu hơn. Chính vì vậy, những nhà đầu tư kỳ cựu thường coi sống sót qua các cú '
         'giảm là quan trọng hơn tối đa hóa lợi nhuận mỗi năm. Họ chịu lãi ít hơn một chút để còn ở lại ván chơi tiếp theo.'},
 {'k': 'checklist',
  'ch': 'Chương 6 – Năm quy tắc nếu vẫn muốn dùng đòn bẩy',
  'moc': True,
  'label': 'Giảm sát thương',
  'cap': ('5 QUY TẮC',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Chỉ dùng vốn mà bạn thật sự không cần trong dài hạn, và thu nhập ổn định để trả lãi', (255, 196, 0)),
            ('Đòn bẩy thấp: tài sản tối đa 1,5 lần vốn', (255, 196, 0)),
            ('Đặt điều kiện thoát từ trước, xa ngưỡng giải chấp', (56, 189, 248)),
            ('Không vay để gỡ một khoản lỗ', (239, 68, 68)),
            ('Tránh vay cho cổ phiếu biến động mạnh hay thanh khoản kém', (239, 68, 68))],
  'anh': 'safety helmet construction',
  'say': 'Nếu vẫn muốn dùng đòn bẩy, đây là năm quy tắc giảm sát thương. Một, dùng đòn bẩy chỉ khi thu nhập ổn định đủ trả lãi mà không cần bán cổ phiếu, và không bao giờ dùng tiền cần cho sinh hoạt '
         'hay tiền cho mục tiêu ngắn hạn. Hai, giữ đòn bẩy thấp, ví dụ tổng tài sản không quá một phẩy năm lần vốn. Ba, đặt điều kiện thoát từ trước và ở mức cách xa ngưỡng giải chấp. Bốn, không bao '
         'giờ vay thêm để gỡ một khoản lỗ, đây là con đường nhanh nhất đến mất toàn bộ. Năm, tránh vay cho cổ phiếu biến động mạnh hoặc thanh khoản kém, vì khi cần bán sẽ không bán được hoặc phải '
         'bán giá rất thấp. Những quy tắc này không đảm bảo an toàn, chỉ làm giảm xác suất bạn bị loại khỏi cuộc chơi bởi một cú giảm mà bạn không dự đoán được.'},
 {'k': 'cards',
  'ch': 'Chương 7 – Một cách nghĩ khác: kiếm tiền từ thời gian, không từ đòn bẩy',
  'moc': True,
  'label': 'Ví dụ giả định: vốn 100 triệu, lãi kép 10%/năm',
  'cap': ('THỜI GIAN', 'THAY ĐÒN BẨY'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'cards': [('Sau 10 năm', 'khoảng 259 triệu', 'không vay, tỷ suất giả định'), ('Sau 20 năm', 'khoảng 673 triệu', 'nếu duy trì kỷ luật'), ('Rủi ro', 'không bị giải chấp', 'có thể ngủ ngon')],
  'anh': 'patient gardener growth',
  'say': 'Nhiều người dùng đòn bẩy vì muốn đi nhanh. Nhưng có con đường khác là dùng thời gian thay cho đòn bẩy. Một trăm triệu với tỷ suất giả định mười phần trăm mỗi năm thành khoảng hai trăm năm '
         'mươi chín triệu sau mười năm và sáu trăm bảy mươi ba triệu sau hai mươi năm, mà không phải trả lãi vay và không phải lo bị giải chấp. Tất nhiên đây là phép tính giả định, thị trường không '
         'trả đều như vậy, nhưng điểm chính là phần thưởng của sự kiên nhẫn là có thật, còn phần thưởng của đòn bẩy bị chặn bởi rủi ro bị loại khỏi cuộc chơi. Người sống sót qua các chu kỳ là người '
         'hưởng trọn lãi kép. Nếu phải chọn một điều để nhớ, hãy chọn câu này: thà đi chậm mà đi được đường dài, còn hơn đi nhanh rồi dừng ở chu kỳ giảm đầu tiên.'},
 {'k': 'checklist',
  'ch': 'Chương 8 – Bài học mang theo mười năm',
  'moc': True,
  'label': 'Ba ý ghi nhớ',
  'cap': ('3 Ý GHI NHỚ',),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'items': [('Đòn bẩy nhân đôi kết quả theo cả hai hướng, và nợ không giảm', (239, 68, 68)),
            ('Bán giải chấp biến lỗ tạm thời thành lỗ thật', (239, 68, 68)),
            ('Ưu tiên số một: ở lại cuộc chơi đủ lâu', (34, 197, 94))],
  'anh': 'long journey road ahead',
  'say': 'Ba ý mang theo mười năm. Một, đòn bẩy nhân đôi kết quả theo cả hai hướng, và khoản nợ thì không giảm theo giá. Hai, bán giải chấp biến khoản lỗ tạm thời thành khoản lỗ thật, vào đúng lúc '
         'giá thấp nhất. Ba, ưu tiên số một của nhà đầu tư cá nhân là ở lại cuộc chơi đủ lâu để lãi kép làm việc. Thị trường mười năm nữa sẽ có những cú giảm mới, những công ty mới, những tài khoản '
         'mới bị giải chấp. Người học được bài học này từ sách vở và video thay vì từ chính tài khoản của mình sẽ rẻ hơn rất nhiều. Hãy thử tự tính bằng giấy: với vốn của bạn, nếu thị trường giảm ba '
         'mươi phần trăm, vốn còn bao nhiêu với mức đòn bẩy bạn đang dùng. Con số đó trả lời mọi thứ.'},
 {'k': 'end',
  'label': '',
  'cap': ('QUẢN TRỊ VỐN', 'SỐNG SÓT TRƯỚC'),
  'cols': ((255, 255, 255), (255, 196, 0)),
  'say': 'Các ví dụ vay, ngưỡng ký quỹ và lãi vay là số giả định để tính, thực tế mỗi công ty chứng khoán quy định khác nhau. Biểu đồ chỉ số lấy từ dữ liệu tổng hợp đến ngày năm tháng mười một năm '
         'hai nghìn không trăm hai mươi sáu. Nội dung chia sẻ kiến thức, không phải khuyến nghị mua bán chứng khoán. Hãy đăng ký kênh để xem thêm seri Quản trị vốn.'}]

