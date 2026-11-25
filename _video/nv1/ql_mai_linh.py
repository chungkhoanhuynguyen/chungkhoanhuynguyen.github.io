# -*- coding: utf-8 -*-
# QL1 (Fable 5.2) 25/11/2026 22:00 – VIDEO DÀI kênh chính theo CÔNG THỨC MỚI anh Huy giao 25/11 21:32:
#   tin nóng hot → kể chuyện → lái sang nội dung đang ra view của kênh (nợ, ngân hàng siết tài sản) → kết dẫn khéo về tư vấn.
# Tin: Tập đoàn Mai Linh bị LPBank thông báo thu giữ tài sản, lao động đăng ký 5.500 còn 120 (báo đăng 24–25/11/2026, "đọc nhiều" trên Tiền Phong, 24h).
# Lý do chọn: thương hiệu ai cũng biết (drama/fame) + số sốc; nối thẳng sang nhóm đang ra view: "Việt Nam nợ bao nhiêu" (+91), Short nợ xấu/đất siết nợ, "vay 3 tỷ mua đất" (994).
# Nguồn (đã mở bài gốc 25/11/2026):
#  - VnExpress 24/11/2026 "Taxi Mai Linh nợ quá hạn, ngân hàng thu giữ bất động sản": LPBank thu giữ QSDĐ 707 m2 tại Hội An (tài sản bảo đảm của Mai Linh Hội An) để thu nợ của CTCP Tập đoàn Mai Linh;
#    22/9 thông báo thu hồi toàn bộ khoản nợ; 2/10 yêu cầu tự nguyện bàn giao, hai doanh nghiệp không bàn giao; lao động đăng ký 120 người, giảm 98% so với 5.500 (bố cáo giữa tháng 11); thành lập 1993, ông Hồ Huy sáng lập.
#  - CafeF 25/11/2026: ngày thu giữ dự kiến 11/12/2026; thời đỉnh cao "hàng chục nghìn tài xế", doanh thu "hàng nghìn tỷ đồng mỗi năm".
#  - Znews 24/11/2026: doanh thu năm 2016 là 3.700 tỷ; 2008 bắt đầu khó khăn tài chính; cuối 2024 ký hợp đồng mua và thuê 3.999 xe điện qua Green SM;
#    đầu tháng 5/2026 Nam A Bank thông báo thu giữ ô tô điện VF 5 Plus của Mai Linh Lào Cai.
#  - Tài chính Doanh nghiệp / Stockbiz (9/2024): cuối 2023 lỗ lũy kế 1.306 tỷ, lớn hơn vốn góp của chủ sở hữu; nợ 10 tháng bảo hiểm của người lao động (4,5 tỷ).
#  - Công Luận 29/1/2026: doanh thu thuần 2024 đạt 1.343 tỷ, giảm 15%. Người Lao Động 28/1/2026: đến 31/12/2025 nợ thuế, tiền phạt, chậm nộp hơn 6,38 tỷ (thông báo ngày 15/1/2026).
#  - Nợ xấu (đã dùng ở Short SN2511NOXAU): Báo Đấu thầu – nhà máy nước Cần Giờ Agribank đấu giá 103,55 tỷ (10/2025) còn 52,1 tỷ (10/2026);
#    Báo Đầu tư 9/2026 – HDBank thu giữ 26 thửa đất của Địa ốc Hoàng Quân, dư nợ khoảng 895 tỷ; SHS qua Việt Báo – nợ xấu 27 ngân hàng niêm yết 2,12%, bao phủ 74%.
# Số tự tính: 5.500 → 120 = −97,8%; 3.700 → 1.343 = −63,7% (còn 36,3%); 103,55 → 52,1 = −49,7%.
# Không nêu số dư nợ của Mai Linh tại LPBank (báo không công bố). Nhân vật Cường, Hùng thuộc dàn nhân vật cố định.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw')
sys.path.insert(0, CW + '/_video'); from phat_am import doc as phat_am_doc
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = CW + '/_video/queue/20261125_2200'
KEY = 'CH0112ML'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HCM = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline'
HN = 'ov:Hanoi skyline night||Hanoi skyline'
CF_L = ([-28.25, 0.15, 5.2], [-27.15, 0.15, 5.2])
CAM_CF = {'from': [[-27.4, 1.5, 2.3], [-27.7, 0.8, 5.2], 42], 'to': [[-27.6, 1.42, 3.0], [-27.7, 0.8, 5.2], 38]}
CAM_VP = {'from': [[0.9, 1.5, 4.4], [0.3, 1.3, -1.0], 44], 'to': [[0.6, 1.45, 3.4], [0.2, 1.35, -1.2], 39]}

S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('5.500 NGƯỜI', 'NỬA NĂM SAU CÒN 120'), cols=CR, noti=dict(gio='19:16', ngay='Thứ Ba 24/11', items=[
        ('Tin tức', 'VnExpress · 24/11/2026', 'Taxi Mai Linh nợ quá hạn, ngân hàng thu giữ bất động sản', R_),
        ('Tin tức', 'CafeF · 25/11/2026', 'Tập đoàn Mai Linh chỉ còn 120 nhân sự', R_),
        ('Zalo', 'Cường', 'Ông nhớ cái taxi xanh hồi mình đón vợ đẻ không? Đọc tin đi!', V_)]),
      say=("Năm nghìn năm trăm người. Nửa năm sau, trên giấy tờ chỉ còn một trăm hai mươi. "
           "Đó là số lao động đăng ký của Tập đoàn Mai Linh, hãng taxi màu xanh lá mà gần như nhà nào cũng từng vẫy một lần. "
           "Anh chị có bao giờ tự hỏi, một thương hiệu ba mươi ba tuổi, từng thu về hàng nghìn tỷ mỗi năm, thì hụt hơi từ chỗ nào không? "
           "Em kể anh chị nghe chuyện này. Vì thứ làm Mai Linh khó thở cũng đang nằm trong nhiều cổ phiếu, và trong không ít gia đình mình.")),
 dict(k='bignum', short=True, anh=HCM, cap=('LAO ĐỘNG ĐĂNG KÝ', 'GIẢM 98%'), cols=CR,
      value=98, fmt='{:,.0f}', unit='%', top='TỪ 5.500 NGƯỜI (THÁNG 5) CÒN 120 NGƯỜI (THÁNG 11)', sub='VnExpress 24/11/2026 · CafeF 25/11/2026', col=R_,
      say=("Con số này nằm trong hồ sơ đăng ký doanh nghiệp. Tháng năm, năm nghìn năm trăm người. Giữa tháng mười một, một trăm hai mươi người. Giảm chín mươi tám phần trăm. "
           "Cùng lúc đó, một ngân hàng gửi thông báo thu giữ tài sản thế chấp của tập đoàn.")),
 dict(k='3d', set='cafevh', light='day', cam=CAM_CF, label='TỐI THỨ BA · QUÁN NƯỚC',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'dienthoai', 'ngoi': True, 'expr': 'worried'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'worried'}],
      cap=('"HÃNG TO THẾ', 'MÀ CŨNG BỊ SIẾT NỢ À?"'), cols=CC,
      say=("Tối thứ Ba, Cường chìa điện thoại cho Hùng xem tin. Hùng lái xe container hơn mười năm, hồi mới vào nghề từng mơ được khoác áo xanh chạy taxi. "
           "Anh đọc xong, im một lúc rồi hỏi: hãng to thế mà cũng bị siết nợ à? "
           "Cường thì lo chuyện khác. Anh đang cầm cổ phiếu của một công ty, mua chỉ vì thấy thương hiệu quen. Hai người hỏi em ba câu. Chuyện gì vừa xảy ra? Vì sao ra nông nỗi? Và làm sao biết công ty Cường đang cầm có giống thế không?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Chuyện gì vừa xảy ra', cap=('NGÂN HÀNG THÔNG BÁO', 'THU GIỮ TÀI SẢN THẾ CHẤP'), cols=CR, moc=True, giay=dict(
        tieu_de='THÔNG BÁO THU GIỮ TÀI SẢN', so='VnExpress 24/11/2026 · CafeF 25/11/2026', dau='NỢ QUÁ HẠN', dieu=[
        ('22/9: ngân hàng đòi lại', 'TOÀN BỘ KHOẢN NỢ'),
        ('2/10: yêu cầu tự bàn giao tài sản', 'KHÔNG BÀN GIAO'),
        ('Tài sản: khu đất tại Hội An', '707 M²'),
        ('Ngày thu giữ dự kiến', '11/12/2026')]),
      say=("Câu thứ nhất, chuyện gì vừa xảy ra. Mai Linh vay tiền ngân hàng và đem một khu đất hơn bảy trăm mét vuông ở Hội An ra thế chấp. Thế chấp nghĩa là: người vay không trả được thì ngân hàng được lấy miếng đất đó. "
           "Ngày hai mươi hai tháng chín, ngân hàng thông báo đòi lại toàn bộ khoản nợ. Ngày mùng hai tháng mười, ngân hàng yêu cầu tự bàn giao khu đất. Theo báo VnExpress, phía doanh nghiệp không bàn giao. "
           "Và ngày thu giữ dự kiến là mười một tháng mười hai tới.")),
 dict(k='giay', cap=('KHÔNG PHẢI TỜ THÔNG BÁO ĐẦU TIÊN', 'TRONG NĂM NAY'), cols=CR, moc=True, giay=dict(
        tieu_de='NHỮNG TỜ THÔNG BÁO NỐI NHAU', so='Người Lao Động 28/1/2026 · Znews 24/11/2026', dau='NĂM 2026', dieu=[
        ('Tháng 1: cơ quan thuế báo nợ thuế', 'HƠN 6,38 TỶ'),
        ('Tháng 5: một ngân hàng khác thu giữ', 'XE ĐIỆN Ở LÀO CAI'),
        ('Tháng 9: ngân hàng đòi', 'TOÀN BỘ KHOẢN NỢ'),
        ('Tháng 12: dự kiến thu giữ', 'ĐẤT Ở HỘI AN')]),
      say=("Nhưng điều em muốn anh chị để ý là: đây không phải tờ thông báo đầu tiên. "
           "Tháng một năm nay, cơ quan thuế báo tập đoàn nợ thuế hơn sáu tỷ đồng. Tháng năm, một ngân hàng khác thông báo thu giữ xe điện của công ty con ở Lào Cai. Tháng chín, đến lượt khoản vay có khu đất Hội An. "
           "Một doanh nghiệp hiếm khi gục trong một ngày. Nó hụt hơi dần, qua từng tờ thông báo.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Từ chiếc taxi xanh tới nghìn tỷ', anh=HCM, cap=('33 NĂM', 'MỘT MÀU XANH LÁ'), cols=CC, moc=True,
      cards=[('Năm 1993', 'Ra đời', 'Ông Hồ Huy sáng lập'), ('Thời đỉnh cao', 'Hàng chục nghìn tài xế', 'Theo CafeF'), ('Năm 2016', 'Doanh thu 3.700 tỷ', 'Theo Znews')],
      say=("Câu thứ hai, vì sao ra nông nỗi. Phải quay lại từ đầu. Năm một nghìn chín trăm chín mươi ba, ông Hồ Huy lập công ty. "
           "Ba mươi năm sau đó, màu xanh lá ấy có mặt ở khắp nơi, từ sân bay tới cổng bệnh viện. Thời đỉnh cao, hãng có hàng chục nghìn tài xế. "
           "Riêng năm hai nghìn không trăm mười sáu, doanh thu khoảng ba nghìn bảy trăm tỷ đồng. Doanh thu là tổng tiền khách trả cho hãng trong một năm, chưa trừ đồng chi phí nào.")),
 dict(k='bars', short=True, anh=HN, cap=('DOANH THU 3.700 TỶ', 'TÁM NĂM SAU CÒN 1.343 TỶ'), cols=CR, top='DOANH THU MỘT NĂM (TỶ ĐỒNG)',
      bars=[('Năm 2016', 3700, V_, '3.700'), ('Năm 2024', 1343, R_, '1.343')],
      say=("Rồi xe công nghệ xuất hiện. Khách không cần ra đường vẫy nữa, chỉ cần bấm điện thoại, biết trước giá, biết trước xe. "
           "Tám năm sau, doanh thu của Mai Linh còn khoảng một nghìn ba trăm bốn mươi ba tỷ đồng, tức là chỉ còn khoảng ba mươi sáu phần trăm. "
           "Khách ít đi, nhưng xe vẫn phải trả góp, lương vẫn phải trả, lãi ngân hàng vẫn chạy từng ngày.")),
 dict(k='chat', cap=('"THƯƠNG HIỆU TO THẾ', 'CƠ MÀ?"'), cols=CC, moc=True, chat=dict(ten='Cường', tv='Đang hoạt động', gio='21:05', mau=V_, msgs=[
        ('Cường', 'Nhưng thương hiệu to thế cơ mà?'),
        ('Cường', 'Ai chả biết cái xe xanh đó'),
        ('me', 'Ai cũng biết, nhưng còn mấy người gọi?'),
        ('me', 'Thương hiệu không đi trả nợ thay được')]),
      say=("Cường vẫn chưa tin. Anh nhắn: nhưng thương hiệu to thế cơ mà, ai chẳng biết cái xe xanh đó. "
           "Hùng trả lời một câu em rất thích: ai cũng biết, nhưng còn mấy người gọi? Thương hiệu không đi trả nợ thay được.")),
 dict(k='bignum', anh=HCM, cap=('CÚ XOAY CUỐI NĂM 2024', 'GẦN 4.000 XE ĐIỆN'), cols=CC,
      value=3999, fmt='{:,.0f}', unit=' XE', top='HỢP ĐỒNG MUA VÀ THUÊ XE ĐIỆN, KÝ CUỐI NĂM 2024', sub='Theo Znews 24/11/2026', col=V_,
      say=("Mai Linh không ngồi yên. Cuối năm hai nghìn không trăm hai mươi tư, hãng ký hợp đồng mua và thuê gần bốn nghìn xe điện để làm mới đội xe. "
           "Nhưng xe mới cũng là nợ mới. Vài tháng sau, chính những chiếc xe điện ở Lào Cai lại nằm trong thông báo thu giữ của ngân hàng. "
           "Đổi xe thì nhanh. Kéo khách quay lại mới là việc khó.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='giay', ch='Chương 3 – Dòng chữ ít ai đọc', cap=('DẤU HIỆU ĐÃ NẰM TRONG BÁO CÁO', 'TỪ CUỐI NĂM 2023'), cols=CR, moc=True, giay=dict(
        tieu_de='BÁO CÁO TÀI CHÍNH CUỐI NĂM 2023', so='Tài chính Doanh nghiệp, Stockbiz · tháng 9/2024', dau='ĐÈN ĐỎ', dieu=[
        ('Lỗ cộng dồn qua nhiều năm', '1.306 TỶ'),
        ('So với số tiền chủ đã góp', 'LỖ LỚN HƠN'),
        ('Chậm đóng bảo hiểm cho người lao động', '10 THÁNG'),
        ('Doanh thu 2024 so với năm trước', 'GIẢM 15%')]),
      say=("Và đây là phần em muốn anh chị xem kỹ nhất. Dấu hiệu không đợi đến tháng mười một năm nay. Nó nằm sẵn trong báo cáo tài chính từ cuối năm hai nghìn không trăm hai mươi ba. "
           "Dòng thứ nhất: lỗ lũy kế hơn một nghìn ba trăm tỷ đồng. Lỗ lũy kế nghĩa là cộng hết lãi lỗ các năm lại, công ty vẫn đang âm chừng đó tiền. "
           "Dòng thứ hai mới đáng sợ: khoản lỗ cộng dồn ấy lớn hơn cả số tiền các chủ đã góp vào.")),
 dict(k='checklist', cap=('LỖ LỚN HƠN TIỀN CHỦ GÓP', 'NGHĨA LÀ GÌ?'), cols=CC, moc=True,
      items=[('Góp 10 đồng mở quán', V_), ('Mấy năm cộng lại lỗ hơn 10 đồng', R_), ('Quán còn mở là nhờ tiền đi vay', R_)],
      say=("Em ví dụ cho dễ hình dung. Anh chị góp mười đồng mở một cái quán. Mấy năm cộng lại, quán lỗ hơn mười đồng. "
           "Nghĩa là tiền của chủ đã hết sạch. Cái quán vẫn sáng đèn là nhờ tiền đi vay, và tiền chưa trả cho người khác. "
           "Lúc đó chỉ cần một chủ nợ đòi gấp, là cả dây cùng căng. Cùng thời điểm ấy, báo chí cũng ghi nhận tập đoàn chậm đóng bảo hiểm cho người lao động tới mười tháng.")),
 # ---------------- CHƯƠNG 4: lái sang nội dung đang ra view ----------------
 dict(k='cards', ch='Chương 4 – Không chỉ một hãng taxi', anh=HN, cap=('NGÂN HÀNG ĐANG SIẾT NỢ', 'Ở NHIỀU NƠI'), cols=CR, moc=True,
      cards=[('Nhà máy nước Cần Giờ', '103,55 tỷ còn 52,1 tỷ', 'Giá đấu giá sau 1 năm'), ('Một công ty địa ốc', 'Bị thu giữ 26 thửa đất', 'Dư nợ khoảng 895 tỷ'), ('27 ngân hàng niêm yết', 'Nợ xấu 2,12%', 'Dự phòng che 74%')],
      say=("Chuyện này không riêng một hãng taxi. Năm nay, anh chị sẽ gặp chữ thu giữ tài sản ngày một nhiều. "
           "Một nhà máy nước ở Cần Giờ bị ngân hàng đem đấu giá. Một năm trước giá khởi điểm hơn một trăm linh ba tỷ, nay hạ còn khoảng năm mươi hai tỷ, mất gần một nửa. "
           "Một công ty địa ốc bị thu giữ hai mươi sáu thửa đất. Còn nợ xấu, tức những khoản vay khó đòi, ở hai mươi bảy ngân hàng niêm yết đã lên khoảng hai phẩy một phần trăm.")),
 dict(k='bignum', short=True, anh=HCM, cap=('TÀI SẢN THẾ CHẤP ĐEM BÁN', 'CÓ KHI CÒN MỘT NỬA'), cols=CR,
      value=52.1, fmt='{:,.1f}', unit=' TỶ', top='GIÁ KHỞI ĐIỂM TỪ 103,55 TỶ (10/2025) HẠ CÒN', sub='Nhà máy nước Cần Giờ · theo Báo Đấu thầu', col=R_,
      say=("Điều này nghĩa là gì với túi tiền anh chị? Có hai nghĩa. "
           "Một, nếu nhà mình đang vay: tài sản thế chấp trên giấy là một trăm, lúc phải bán gấp có khi chỉ còn năm mươi. Đừng tính nợ theo giá lúc đẹp trời. "
           "Hai, nếu anh chị cầm cổ phiếu: doanh nghiệp nào vay nhiều, khách ít dần, thì sớm muộn cũng nhận những tờ thông báo như thế.")),
 dict(k='3d', set='vanphong', light='day', cam=CAM_VP, label='SÁNG THỨ TƯ · VĂN PHÒNG',
      cast=[{'a': 'huy', 'p': [-0.7, 0, 0.5], 'act': 'chitay', 'side': -1, 'expr': 'smile'},
            {'a': 'cuong', 'p': [0.9, 0, 0.7], 'act': 'dienthoai', 'side': -1, 'expr': 'worried'}],
      cap=('"THẾ MÃ TÔI ĐANG CẦM', 'THÌ XEM Ở ĐÂU?"'), cols=CC,
      say=("Sáng thứ Tư, Cường ghé văn phòng em, Huy Nguyễn. Anh hỏi thẳng: thế cái mã anh đang cầm thì xem ở đâu, anh có biết đọc báo cáo đâu. "
           "Em bảo anh không cần đọc cả trăm trang. Chỉ cần tìm đúng ba dòng. Mất năm phút, mà tránh được phần lớn những cú như thế này.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Ba dòng phải xem', cap=('3 DÒNG PHẢI XEM', 'TRƯỚC KHI XUỐNG TIỀN'), cols=CC, moc=True,
      items=[('Lỗ cộng dồn có lớn hơn tiền chủ góp?', R_), ('Tiền lãi vay có ăn hết tiền lãi làm ra?', V_), ('Tiền thật thu về từ bán hàng: âm hay dương?', V_)],
      say=("Dòng thứ nhất, lỗ lũy kế. Nếu lỗ cộng dồn lớn hơn tiền chủ góp, giống cái quán em vừa kể, thì dừng lại đã. "
           "Dòng thứ hai, chi phí lãi vay. Làm ra mười đồng lãi mà trả ngân hàng hết tám chín đồng, thì công ty đang làm thuê cho chủ nợ. "
           "Dòng thứ ba, dòng tiền từ hoạt động kinh doanh. Nói đơn giản là tiền thật chảy vào két từ việc bán hàng. Báo lãi mà dòng này âm nhiều năm, thì lãi đó mới nằm trên giấy.")),
 dict(k='chat', cap=('"LỖ CỘNG DỒN', 'BA NĂM LIỀN ÔNG Ạ"'), cols=CR, moc=True, chat=dict(ten='Cường', tv='Đang hoạt động', gio='22:40', mau=V_, msgs=[
        ('Cường', 'Tôi mở báo cáo cái mã tôi cầm rồi'),
        ('Cường', 'Lỗ cộng dồn ba năm liền ông ạ'),
        ('Cường', 'Thế mà tôi mua vì thấy quảng cáo nhiều'),
        ('me', 'Giờ biết vẫn hơn là không biết')]),
      say=("Tối đó Cường nhắn cho Hùng. Anh đã mở báo cáo của cái mã mình cầm. Lỗ cộng dồn ba năm liền. Thế mà anh mua chỉ vì thấy quảng cáo nhiều. "
           "Hùng trả lời: giờ biết vẫn hơn là không biết. "
           "Em không nói mã của Cường tốt hay xấu. Em chỉ muốn anh ấy quyết định khi đã nhìn thấy ba dòng đó, chứ không phải khi mới nhìn thấy cái biển hiệu.")),
 dict(k='checklist', ch='Phép thử cho nhà mình', cap=('NỢ CỦA NHÀ MÌNH', '3 CÂU TỰ HỎI'), cols=CC, moc=True,
      items=[('Thu nhập giảm một nửa, còn trả nổi 6 tháng?', V_), ('Tiền trả nợ có quá 30% thu nhập?', V_), ('Tài sản thế chấp bán gấp còn bao nhiêu?', R_)],
      say=("Còn với nhà mình, em có một phép thử ba câu. Một, nếu thu nhập giảm một nửa, nhà mình còn trả nợ được sáu tháng không? "
           "Hai, tiền trả nợ mỗi tháng có vượt quá ba mươi phần trăm thu nhập không? "
           "Ba, tài sản đang thế chấp, nếu phải bán gấp thì còn được bao nhiêu? Đây là mốc em tự soi cho mình, anh chị tham khảo rồi cân theo hoàn cảnh nhà mình.")),
 # ---------------- KẾT ----------------
 dict(k='3d', ch='Kết', set='cafevh', light='day', cam=CAM_CF, label='CUỐI TUẦN · QUÁN NƯỚC',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'noi', 'ngoi': True, 'expr': 'relief'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'}],
      cap=('"THƯƠNG HIỆU ĐỂ NGƯỜI TA NHỚ', 'DÒNG TIỀN MỚI ĐỂ MÌNH SỐNG"'), cols=CC,
      say=("Cuối tuần, hai người lại ngồi quán nước. Ngoài đường vẫn có một chiếc taxi xanh chạy qua. Hùng nhìn theo, rồi nói một câu em muốn anh chị mang theo: "
           "thương hiệu để người ta nhớ, còn dòng tiền mới để mình sống.")),
 dict(k='cards', anh=HCM, cap=('BA DÒNG ĐÓ', 'EM ĐÃ CHẤM SẴN'), cols=CC, moc=True,
      cards=[('Trên web', 'Đánh giá báo cáo tài chính', 'Xem miễn phí'), ('Từng quý', 'Điểm tốt, điểm cần lưu ý', 'Chữ dễ hiểu'), ('Đọc vẫn rối?', 'Nhắn em tên mã', 'Em xem cùng anh chị')],
      say=("Ba dòng vừa rồi, em đã chấm sẵn cho các doanh nghiệp trên sàn, ở mục đánh giá báo cáo tài chính trên web chứng khoán Huy Nguyễn chấm com. Anh chị vào xem miễn phí. "
           "Còn nếu anh chị đang cầm một mã mà đọc vẫn thấy rối, cứ nhắn Zalo cho em tên mã. Em xem cùng anh chị đúng ba dòng đó, rồi anh chị tự quyết.")),
 dict(k='end', cap=('ANH CHỊ TỪNG MUA CỔ PHIẾU', 'CHỈ VÌ THƯƠNG HIỆU QUEN?'), cols=CC,
      say=("Còn anh chị, đã bao giờ mua một cổ phiếu chỉ vì thương hiệu quen chưa? Và chuyến taxi xanh anh chị nhớ nhất là chuyến nào? Kể em nghe ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=50)
for c in S: c['say'] = lib.doc(phat_am_doc(c['say']))
TIEU = 'Mai Linh 5.500 Người Còn 120: Thương Hiệu Lớn Gục Vì Đâu?'
MT = ("Số lao động đăng ký của Tập đoàn Mai Linh giảm từ 5.500 xuống 120 người sau khoảng nửa năm, ngân hàng thông báo thu giữ khu đất thế chấp 707 m² tại Hội An. "
      "Một thương hiệu 33 năm, doanh thu từng 3.700 tỷ, hụt hơi từ đâu? Dấu hiệu đã nằm trong báo cáo tài chính từ cuối 2023: lỗ cộng dồn 1.306 tỷ, lớn hơn cả vốn chủ góp. "
      "Chuyện Cường – Hùng và 3 dòng phải xem trước khi mua một cổ phiếu chỉ vì thương hiệu quen.\n\n"
      "Nguồn số liệu:\n"
      "• VnExpress 24/11/2026: LPBank thông báo thu giữ quyền sử dụng đất 707 m² tại Hội An để thu hồi nợ vay của CTCP Tập đoàn Mai Linh; 22/9 thông báo thu hồi toàn bộ khoản nợ; 2/10 yêu cầu tự nguyện bàn giao; lao động đăng ký 120 người, giảm 98% so với 5.500; thành lập năm 1993\n"
      "• CafeF 25/11/2026: thời gian thu giữ dự kiến 11/12/2026; thời đỉnh cao có hàng chục nghìn tài xế\n"
      "• Znews 24/11/2026: doanh thu năm 2016 khoảng 3.700 tỷ đồng; cuối 2024 ký hợp đồng mua và thuê 3.999 xe điện; đầu tháng 5/2026 Nam A Bank thông báo thu giữ ô tô điện của Mai Linh Lào Cai\n"
      "• Tài chính Doanh nghiệp, Stockbiz (9/2024): cuối 2023 lỗ lũy kế 1.306 tỷ đồng, lớn hơn vốn góp của chủ sở hữu; nợ 10 tháng bảo hiểm của người lao động\n"
      "• Công Luận 29/1/2026: doanh thu thuần 2024 đạt 1.343 tỷ đồng, giảm 15%. Người Lao Động 28/1/2026: nợ thuế, tiền phạt, tiền chậm nộp hơn 6,38 tỷ đồng tính đến 31/12/2025\n"
      "• Báo Đấu thầu: nhà máy nước Cần Giờ giá khởi điểm 103,55 tỷ (10/2025) còn 52,1 tỷ (10/2026). Báo Đầu tư 9/2026: HDBank thu giữ 26 thửa đất của Địa ốc Hoàng Quân, dư nợ khoảng 895 tỷ. SHS qua Việt Báo: nợ xấu 27 ngân hàng niêm yết 2,12%, tỷ lệ bao phủ 74%\n"
      "• Em tự tính: 5.500 → 120 = −97,8%; 3.700 → 1.343 tỷ = −63,7%; 103,55 → 52,1 tỷ = −49,7%\n\n"
      "Đánh giá báo cáo tài chính từng doanh nghiệp, xem miễn phí: https://chungkhoanhuynguyen.com/#bctc\n"
      "Cần trao đổi riêng về mã đang cầm: Zalo 0365.188.286\n\n"
      "Ba dòng và phép thử trong video là mốc tự soi, không phải lời khuyên mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng kể chuyện', ngay='2026-12-01', gio_goi_y='12:00', gio='12:00', nhac='lofi', can_duyet='anh Huy duyệt trước khi hẹn',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['Mai Linh', 'taxi Mai Linh', 'Mai Linh bị thu giữ tài sản', 'nợ xấu', 'ngân hàng siết nợ', 'lỗ lũy kế', 'đọc báo cáo tài chính', 'cách chọn cổ phiếu', 'đầu tư chứng khoán', 'kinh tế Việt Nam'],
    bia_hook=['TAXI XANH', 'BỊ SIẾT NỢ'], badge='GIẢM 98% NHÂN SỰ', bia_anh='ov:Ho Chi Minh City skyline night||Hanoi skyline night',
    bia_hook_b=['LỖ 1.306 TỶ', 'VƯỢT VỐN GÓP'], badge_b='DÒNG CHỮ ÍT AI ĐỌC',
    bia_hook_c=['THƯƠNG HIỆU', 'KHÔNG TRẢ NỢ'], badge_c='3 DÒNG PHẢI XEM',
    reel_hook='5.500 NGƯỜI CÒN 120|THƯƠNG HIỆU LỚN GỤC VÌ ĐÂU???',
    fb_post=("5.500 người, nửa năm sau còn 120 – chuyện gì đã xảy ra với hãng taxi xanh?\n"
             "👉 Doanh thu từng 3.700 tỷ, 8 năm sau còn 1.343 tỷ\n👉 Cuối 2023 lỗ cộng dồn 1.306 tỷ, lớn hơn cả tiền chủ góp\n👉 Ngân hàng dự kiến thu giữ đất thế chấp ngày 11/12\n"
             "3 dòng phải xem trước khi mua cổ phiếu chỉ vì thương hiệu quen.\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – Tin nóng kể chuyện: MAI LINH (QL1 Fable 5.2, 25/11/2026). Công thức: tin nóng → kể chuyện → nợ/ngân hàng siết tài sản → 3 dòng BCTC → dẫn về tư vấn. 3 cảnh 3D.\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    from collections import Counter
    cnt = Counter(c['k'] for c in S)
    print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'tieu de', len(TIEU))
    for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
    for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
    import kiem_loi, kiem_goi
    print('goi', kiem_goi.kiem(TIEU, META[KEY]['bia_hook']))
    for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
        if 'câu cụt' not in q: print(q)
    from xung_ho import le_phep
    for c in S:
        if le_phep(c['say']) != c['say']: print('XUNG_HO', c['say'][:80])
    for c in S:
        for x in c.get('cap', ()):
            if len(x) > 32: print('CAP DAI', len(x), x)
