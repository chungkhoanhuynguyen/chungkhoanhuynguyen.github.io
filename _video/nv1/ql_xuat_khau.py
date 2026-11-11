# -*- coding: utf-8 -*-
# QL1 11/11/2026 – VIDEO DÀI kênh chính, khuôn kể chuyện + chủ đề vĩ mô "câu hỏi lớn" (anh Huy 11/11: reel chủ đề nóng, làm luôn video dài cùng nội dung).
# Cặp với reel RV1111A (lô 20261111_1730_reel).
# Nguồn (WiData, số Cục Hải quan / NHNN):
#  - Xuất khẩu tháng (triệu USD) 1–10/2026 cộng 498.804; 1–10/2025 cộng 391.607 => +27,4%.
#  - Xuất khẩu khu vực FDI = nhập khẩu FDI + cán cân FDI = 404.038 (81%); trong nước = 94.766 (19%) – số tự tính.
#  - Cán cân 10T/2026: FDI +25.052; trong nước −36.867; tổng −11.816 (10T/2025: +19.492).
#  - Xuất sang Hoa Kỳ 10T/2026: 159.498 (32% tổng xuất khẩu).
#  - FDI xuất = 92730+255713: 2017 71% · 2023 72,5% · 2025 77,7% · 10T/26 81%; 10T/25 FDI 303,9 tỷ, DN Việt 87,7 tỷ -> +33% / +8%. FDI nhập 10T/26 378,99 tỷ.
#  - Mặt hàng 10T/26 (bảng 86 ytd): điện tử 149,4 · máy móc 63,3 · điện thoại 57,6 · gỗ 15,0 tỷ USD.
#  - Cán cân thanh toán NHNN, 4 quý Q3/2025–Q2/2026: chi thu nhập đầu tư (lãi, lợi nhuận trả ra nước ngoài) 17.861; FDI vào 23.070.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261111_1800'
KEY = 'CH1711XK'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('XUẤT KHẨU KỶ LỤC', 'TIỀN VỀ TÚI AI?'), cols=CC, noti=dict(gio='06:40', ngay='Thứ Hai', items=[
        ('Tin tức', 'Kinh tế', 'Xuất khẩu 10 tháng đạt 498,8 tỷ USD, tăng hơn 27%', G_),
        ('Zalo', 'Tổ trưởng chuyền 3', 'Tháng này chuyền mình không tăng ca nhé mọi người', R_)]),
      say=("Sáu giờ bốn mươi sáng, chị Mai đứng chờ xe đưa đón ở cổng khu công nghiệp. Điện thoại hiện hai thông báo liền nhau. Tin thứ nhất: xuất khẩu mười tháng đạt gần năm trăm tỷ đô la, tăng hơn hai mươi bảy phần trăm. "
           "Tin thứ hai, từ tổ trưởng: tháng này chuyền mình không tăng ca nhé mọi người. Chị Mai nhìn hai dòng chữ, tự hỏi: đất nước xuất khẩu kỷ lục, sao túi mình vẫn thế?")),
 dict(k='bignum', anh='ov:container port aerial||container port', cap=('10 THÁNG NĂM 2026', 'TĂNG 27,4% SO VỚI CÙNG KỲ'), cols=CC, value=498.8, fmt='{:,.1f}', unit=' tỷ USD', top='XUẤT KHẨU CỦA VIỆT NAM', sub='Khoảng 50 tỷ USD mỗi tháng', col=GOLD,
      say=("Con số trên báo là thật. Theo số liệu hải quan, mười tháng năm 2026, Việt Nam xuất khẩu bốn trăm chín mươi tám phẩy tám tỷ đô la, tăng hai mươi bảy phẩy bốn phần trăm so với cùng kỳ, trung bình gần năm mươi tỷ đô la mỗi tháng. "
           "Nhưng hôm nay em muốn cùng anh chị trả lời câu hỏi của chị Mai: gần năm trăm tỷ đô la đó, cuối cùng về túi ai?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Hai người trong cùng một con số', cap=('"ĐƠN HÀNG', 'VẪN CHƯA VỀ"'), cols=CR, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='21:15', mau=X_, msgs=[
        ('Vợ', 'Báo nói xuất khẩu tăng 27% mà anh'),
        ('me', 'Xưởng mình đơn hàng gỗ vẫn chưa về em ạ'),
        ('me', 'Tháng này lại phải vay thêm để mua gỗ nhập'),
        ('Vợ', 'Vậy ai xuất khẩu nhiều thế?')]),
      say=("Cách đó hơn một nghìn cây số, ở Bình Dương, anh Hùng chủ một xưởng gỗ nhỏ chuyên làm hàng xuất khẩu. Tối đó vợ anh nhắn: báo nói xuất khẩu tăng hai mươi bảy phần trăm mà anh. "
           "Anh Hùng trả lời: xưởng mình đơn hàng vẫn chưa về em ạ, tháng này lại phải vay thêm để mua gỗ nhập. Vợ anh hỏi lại một câu rất đơn giản: vậy ai xuất khẩu nhiều thế?")),
 dict(k='cards', anh='ov:factory workers||factory assembly line', cap=('XUẤT KHẨU 10T/2026', 'CỦA AI?'), cols=CC, moc=True,
      cards=[('81%', 'Doanh nghiệp vốn nước ngoài (FDI)', 'khoảng 404 tỷ USD'), ('19%', 'Doanh nghiệp Việt', 'khoảng 95 tỷ USD'), ('5 : 1', 'Cứ 5 đô la xuất khẩu', 'chỉ 1 đô của DN Việt')],
      say=("Câu trả lời nằm ở bảng số liệu theo khu vực. Em tách xuất khẩu mười tháng ra hai phần. Khoảng tám mươi mốt phần trăm, tức hơn bốn trăm tỷ đô la, là hàng của doanh nghiệp có vốn nước ngoài, những nhà máy như nơi chị Mai đang làm. "
           "Doanh nghiệp Việt, như xưởng của anh Hùng, chỉ chiếm khoảng mười chín phần trăm. Tức là cứ năm đô la xuất khẩu, chỉ khoảng một đô la là của doanh nghiệp trong nước.")),
 dict(k='cards', anh='ov:factory assembly line electronics||factory workers', cap=('10 THÁNG 2026', 'SO VỚI CÙNG KỲ 2025'), cols=CC, moc=True,
      cards=[('+33%', 'Xuất khẩu khu vực FDI', '~304 lên ~404 tỷ USD'), ('+8%', 'Xuất khẩu doanh nghiệp Việt', '~88 lên ~95 tỷ USD', (196, 120, 20))],
      say=("Và đây là chi tiết khiến em giật mình. So với mười tháng năm ngoái, xuất khẩu của khu vực FDI tăng khoảng ba mươi ba phần trăm, từ khoảng ba trăm lẻ bốn lên khoảng bốn trăm lẻ bốn tỷ đô la. "
           "Còn xuất khẩu của doanh nghiệp Việt chỉ tăng khoảng tám phần trăm, từ tám mươi tám lên chín mươi lăm tỷ. Nói cách khác, gần như toàn bộ phần tăng trưởng kỷ lục năm nay đến từ các nhà máy vốn nước ngoài.")),
 dict(k='cards', anh='ov:container port aerial||container port', cap=('PHẦN CỦA DOANH NGHIỆP VIỆT', 'TRONG TỔNG XUẤT KHẨU'), cols=CR, moc=True,
      cards=[('29%', 'Năm 2017', '~62 / 215 tỷ USD'), ('27,5%', 'Năm 2023', '~98 / 355 tỷ USD'), ('22%', 'Năm 2025', '~106 / 475 tỷ USD'), ('19%', '10 tháng 2026', '~95 / 499 tỷ USD')],
      say=("Nếu nhìn xa hơn, xu hướng còn rõ. Năm 2017, doanh nghiệp Việt chiếm khoảng hai mươi chín phần trăm xuất khẩu. Năm 2023, hai mươi bảy phẩy năm phần trăm. Năm 2025 còn khoảng hai mươi hai phần trăm, và mười tháng năm nay chỉ còn mười chín phần trăm. "
           "Doanh nghiệp Việt vẫn lớn lên về số tuyệt đối, nhưng chiếc bánh FDI lớn nhanh hơn rất nhiều. Đây là số em tự tính từ số liệu hải quan theo khu vực, anh chị xem nguồn ở phần mô tả.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Người dư, người thiếu', anh='ov:cargo ship containers port||container port', cap=('CÁN CÂN THƯƠNG MẠI', '10 THÁNG 2026'), cols=CR, moc=True,
      cards=[('+25,1 tỷ USD', 'Khu vực FDI: bán ra nhiều hơn mua vào', ''), ('−36,9 tỷ USD', 'Doanh nghiệp Việt: mua vào nhiều hơn bán ra', ''), ('−11,8 tỷ USD', 'Cả nước (cùng kỳ 2025: +19,5 tỷ)', '')],
      say=("Chưa hết. Khu vực FDI bán ra nhiều hơn mua vào hai mươi lăm phẩy một tỷ đô la. Doanh nghiệp Việt thì ngược lại: mua vào nhiều hơn bán ra ba mươi sáu phẩy chín tỷ đô la. "
           "Cộng lại, mười tháng năm nay cả nước nhập siêu mười một phẩy tám tỷ đô la, trong khi cùng kỳ năm ngoái còn xuất siêu mười chín phẩy năm tỷ. Xuất khẩu tăng kỷ lục, mà cán cân lại đảo chiều.")),
 dict(k='text', cap=('MÌNH NHẬP NHỮNG GÌ?', 'MÁY MÓC, NGUYÊN LIỆU, XĂNG DẦU'), cols=CC, anh='ov:cargo ship containers port||container port',
      say=("Doanh nghiệp trong nước nhập về máy móc, nguyên liệu, xăng dầu và cả hàng tiêu dùng. Như xưởng anh Hùng, gỗ tốt phải nhập, keo và sơn cũng nhập. "
           "Điều quan trọng: doanh nghiệp Việt phải mua đô la ngay trong nước để thanh toán. Còn doanh nghiệp FDI thường giữ ngoại tệ ở nước ngoài. Vì vậy phần nhập siêu của khu vực trong nước mới là áp lực thật lên tỷ giá, lên giá hàng hóa mà chị Mai mua mỗi ngày.")),
 dict(k='cards', ch='Chương 3 – Mình xuất khẩu cái gì?', anh='ov:circuit board electronics||electronics factory', cap=('XUẤT KHẨU 10T/2026', 'TỶ USD – THEO MẶT HÀNG'), cols=CC, moc=True,
      cards=[('149,4', 'Máy tính, điện tử, linh kiện', ''), ('63,3', 'Máy móc, thiết bị, phụ tùng', ''), ('57,6', 'Điện thoại và linh kiện', ''), ('15,0', 'Gỗ và sản phẩm gỗ', 'như xưởng anh Hùng', (196, 120, 20))],
      say=("Vậy năm trăm tỷ đô la đó là những mặt hàng gì? Đứng đầu là máy tính, sản phẩm điện tử và linh kiện, một trăm bốn mươi chín phẩy bốn tỷ đô la. Tiếp theo là máy móc, thiết bị, sáu mươi ba phẩy ba tỷ. Rồi điện thoại và linh kiện, năm mươi bảy phẩy sáu tỷ. "
           "Ba nhóm này cộng lại khoảng hai trăm bảy mươi tỷ, hơn một nửa tổng xuất khẩu, và phần lớn do các tập đoàn nước ngoài làm ra. Còn gỗ và sản phẩm gỗ, ngành của anh Hùng, cả nước xuất mười lăm tỷ đô la, chưa bằng một phần mười nhóm điện tử.")),
 dict(k='bignum', anh='ov:cargo ship containers port||container port', cap=('MỖI 100 ĐÔ FDI XUẤT ĐI', 'CÓ 94 ĐÔ ĐẦU VÀO NHẬP VỀ'), cols=CR, moc=True, value=94, fmt='{:,.0f}', unit=' USD', top='NHẬP KHẨU / XUẤT KHẨU KHU VỰC FDI 10T/2026', sub='Nhập ~379 tỷ USD · xuất ~404 tỷ USD', col=RED,
      say=("Vì sao điện tử xuất nhiều mà giá trị ở lại ít? Câu trả lời nằm ở chiều nhập. Mười tháng năm nay, khu vực FDI nhập về khoảng ba trăm bảy mươi chín tỷ đô la linh kiện, nguyên liệu, máy móc. "
           "Tức là cứ một trăm đô la hàng FDI xuất đi, có khoảng chín mươi bốn đô la là đầu vào nhập từ nước ngoài. Phần chênh còn lại mới gồm tiền công, tiền điện, tiền thuê đất, và cả lợi nhuận của chủ đầu tư.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='bignum', ch='Chương 4 – Lợi nhuận đi đâu?', anh='ov:industrial park aerial||factory', cap=('LÃI CHUYỂN RA NƯỚC NGOÀI', '4 QUÝ GẦN NHẤT'), cols=CR, moc=True, value=17.9, fmt='{:,.1f}', unit=' tỷ USD', top='LÃI VÀ LỢI NHUẬN TRẢ RA NƯỚC NGOÀI', sub='Bằng gần 80% vốn FDI chảy vào cùng kỳ (23,1 tỷ USD)', col=RED,
      say=("Vậy còn lợi nhuận? Theo cán cân thanh toán của Ngân hàng Nhà nước, trong bốn quý gần nhất, từ quý ba năm 2025 đến quý hai năm 2026, khoảng mười bảy phẩy chín tỷ đô la lãi và lợi nhuận đã được trả ra nước ngoài. "
           "Cùng thời gian đó, vốn FDI chảy vào là hai mươi ba phẩy một tỷ đô la. Nghĩa là cứ một đô la vốn mới vào, có gần tám mươi xu lợi nhuận đi ra.")),
 dict(k='call', cap=('"CHỊ NHÌN', 'PHIẾU LƯƠNG ĐI"'), cols=CC, call=dict(ten='Em trai Long', phu='Kỹ sư sản xuất', mau=G_, loi=[
        'Một chiếc điện thoại xuất đi vài trăm đô', 'Phần ở lại Việt Nam chủ yếu là tiền công lắp ráp']),
      say=("Tối đó chị Mai gọi cho Long, em trai làm kỹ sư sản xuất. Long giải thích bằng chính công việc của chị: một chiếc điện thoại xuất đi có giá vài trăm đô la. Linh kiện chủ yếu nhập từ nước ngoài, thiết kế và thương hiệu của nước ngoài. "
           "Phần ở lại Việt Nam chủ yếu là tiền công lắp ráp, tiền thuê đất, điện, nước và vận chuyển. Chị cứ nhìn phiếu lương của mình là thấy mình đang đứng ở khâu nào.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='bignum', ch='Chương 5 – Một phần ba giỏ hàng đi Mỹ', anh='ov:cargo ship||container ship', cap=('XUẤT SANG HOA KỲ', '10 THÁNG 2026'), cols=CC, moc=True, value=159.5, fmt='{:,.1f}', unit=' tỷ USD', top='KHOẢNG 32% TỔNG XUẤT KHẨU', sub='Mỹ mua chủ yếu hàng gia công và điện tử', col=GOLD,
      say=("Còn một con số nữa. Mười tháng năm 2026, Việt Nam xuất sang Hoa Kỳ một trăm năm mươi chín phẩy năm tỷ đô la, khoảng ba mươi hai phần trăm tổng xuất khẩu. "
           "Mỹ mua chủ yếu hàng tiêu dùng đã gia công và hàng điện tử. Nghĩa là nếu Mỹ thay đổi chính sách thuế, một phần ba giỏ hàng xuất khẩu chịu ảnh hưởng, và người chịu đầu tiên là những chuyền sản xuất như của chị Mai.")),
 dict(k='checklist', anh='ov:factory workers||industrial park', cap=('FDI MANG LẠI GÌ', 'CHO NGƯỜI VIỆT?'), cols=CC,
      items=[('Hàng triệu việc làm, thu nhập ổn định', GREEN), ('Kéo theo khu công nghiệp, cảng, điện, logistics', GREEN), ('Nhưng phần giá trị cao nhất: thiết kế, linh kiện, thương hiệu, phần lớn ở nước ngoài', RED)],
      say=("Em nói công bằng: FDI không xấu. Họ tạo ra hàng triệu việc làm, kéo theo khu công nghiệp, cảng biển, điện và logistics. Không có FDI thì cũng không có con số năm trăm tỷ đô la. "
           "Nhưng phần giá trị cao nhất của chuỗi, thiết kế, linh kiện lõi và thương hiệu, phần lớn vẫn ở nước ngoài. Doanh nghiệp Việt còn đứng ở khâu thấp nhất, và đó là bài toán lớn nhất của mười năm tới.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 6 – Nhà đầu tư đọc con số này thế nào?', anh='ov:stock market screen||stock trading', cap=('3 CÂU HỎI', 'KHI NGHE "XUẤT KHẨU KỶ LỤC"'), cols=CC, moc=True,
      items=[('Kỷ lục của ai: khu vực FDI hay doanh nghiệp Việt?', GREEN),
             ('Doanh nghiệp mình đầu tư hưởng lợi từ FDI, hay đang cạnh tranh với FDI?', GREEN),
             ('Nhập siêu khu vực trong nước tăng: tỷ giá, chi phí đầu vào sẽ ra sao?', GOLD)],
      say=("Với nhà đầu tư chứng khoán, em gợi ý ba câu hỏi mỗi khi nghe tin xuất khẩu kỷ lục. Một: kỷ lục của ai, khu vực FDI hay doanh nghiệp Việt? "
           "Hai: doanh nghiệp mình đang đầu tư hưởng lợi từ dòng vốn FDI, như khu công nghiệp, cảng, logistics, hay đang phải cạnh tranh với FDI? Ba: nhập siêu của khu vực trong nước tăng thì tỷ giá và chi phí đầu vào của doanh nghiệp mình sẽ ra sao? "
           "Anh chị có thể tra lợi nhuận từng quý và P trên E của hơn bốn trăm mã miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối', cap=('"MÌNH Ở KHÂU NÀO', 'THÌ LÀM CHO GIỎI KHÂU ĐÓ"'), cols=CC, moc=True, chat=dict(ten='Long', tv='Đang hoạt động', gio='22:30', mau=X_, msgs=[
        ('me', 'Vậy chị cứ làm công nhân mãi à?'),
        ('Long', 'Không chị ơi. Biết mình ở khâu nào rồi tính bước tiếp'),
        ('Long', 'Học thêm tay nghề, đi lên quản lý chuyền, hoặc tự làm nhà cung cấp')]),
      say=("Trước khi ngủ, chị Mai nhắn: vậy chị cứ làm công nhân mãi à? Long trả lời: không chị ơi. Biết mình đang ở khâu nào thì mới tính được bước tiếp. "
           "Học thêm tay nghề, lên quản lý chuyền, hay một ngày tự làm nhà cung cấp cho chính nhà máy đó. Đất nước cũng vậy thôi.")),
 dict(k='end', cap=('THEO ANH CHỊ, VIỆT NAM', 'CẦN GÌ ĐỂ GIÀNH PHẦN LỚN HƠN?'), cols=CC,
      say=("Còn anh chị, theo anh chị doanh nghiệp Việt cần gì để giành lại phần lớn hơn trong năm trăm tỷ đô la xuất khẩu đó? Kể cho em và mọi người ở phần bình luận nhé. "
           "Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Xuất Khẩu Kỷ Lục 500 Tỷ USD Nhưng 81% Của FDI: Tiền Về Túi Ai, Người Việt Được Gì?'
MT = ("10 tháng 2026 Việt Nam xuất khẩu 498,8 tỷ USD (+27,4%). Nhưng khoảng 81% thuộc doanh nghiệp vốn nước ngoài; FDI xuất siêu 25,1 tỷ USD trong khi doanh nghiệp Việt nhập siêu 36,9 tỷ USD, cả nước nhập siêu 11,8 tỷ USD. "
      "Tiền về túi ai? Câu chuyện của một nữ công nhân khu công nghiệp và một chủ xưởng gỗ.\n\n"
      "Nguồn số liệu (Cục Hải quan, NHNN – tổng hợp WiData):\n"
      "• Xuất khẩu 1–10/2026: 498,8 tỷ USD; 1–10/2025: 391,6 tỷ USD\n"
      "• Xuất khẩu theo khu vực = nhập khẩu + cán cân của từng khu vực (số tự tính): FDI ~404 tỷ (81%), trong nước ~95 tỷ (19%)\n"
      "• Cán cân 10T/2026: FDI +25,1; trong nước −36,9; tổng −11,8 tỷ USD (10T/2025: +19,5)\n"
      "• Xuất sang Hoa Kỳ 10T/2026: 159,5 tỷ USD (~32%)\n"
      "• Xuất khẩu theo khu vực 10T/2025 → 10T/2026 (tự tính): FDI ~304 → ~404 tỷ (+33%); DN Việt ~88 → ~95 tỷ (+8%). Tỷ trọng DN Việt: 2017 ~29% · 2023 ~27,5% · 2025 ~22% · 10T/2026 ~19%\n"
      "• Mặt hàng 10T/2026: máy tính, điện tử, linh kiện 149,4 · máy móc thiết bị 63,3 · điện thoại 57,6 · gỗ 15,0 tỷ USD; nhập khẩu khu vực FDI ~379 tỷ USD\n"
      "• Cán cân thanh toán Q3/2025–Q2/2026: chi thu nhập đầu tư ra nước ngoài 17,9 tỷ USD; FDI vào 23,1 tỷ USD\n\n"
      "Soi P/E, lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật chị Mai, anh Hùng, Long là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-17', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['xuất khẩu Việt Nam', 'FDI', 'xuất khẩu 2026', 'nhập siêu', 'kinh tế Việt Nam', 'tỷ giá', 'vĩ mô', 'doanh nghiệp FDI', 'xuất khẩu sang Mỹ'],
    bia_hook=['500 TỶ USD', 'VỀ TÚI AI?'], badge='XUẤT KHẨU KỶ LỤC – 81% CỦA FDI',
    bia_anh='ov:container port aerial||container port',
    bia_hook_b=['81% CỦA FDI', 'MÌNH ĐƯỢC GÌ?'], badge_b='CÂU HỎI LỚN',
    bia_hook_c=['XUẤT KỶ LỤC', 'VẪN NHẬP SIÊU?'], badge_c='10 THÁNG 2026',
    reel_hook='XUẤT KHẨU 500 TỶ USD|TIỀN VỀ TÚI AI???',
    fb_post=("Xuất khẩu 10 tháng gần 500 tỷ USD, tăng 27% 🚢 Nhưng tiền về túi ai?\n\n👉 81% là của doanh nghiệp FDI\n👉 FDI xuất siêu 25 tỷ USD, DN Việt nhập siêu 37 tỷ USD\n"
             "👉 4 quý qua: 17,9 tỷ USD lợi nhuận chuyển ra nước ngoài\n\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: xuất khẩu 500 tỷ USD, tiền về túi ai (QL1 11/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
