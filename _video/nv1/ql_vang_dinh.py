# -*- coding: utf-8 -*-
# NV1 17/11/2026 00:40 – VIDEO DÀI kênh chính, "câu hỏi lớn": Vàng mất 30% từ đỉnh – người mua 191 triệu giờ bán lại 134,5; lần trước (2011) phải chờ 9 năm?
# Lý do chọn: data/view/xu_huong.md tuần tới 16/11: "TS Bùi Ngọc Sơn: Vàng bị ồ ạt bán tháo, đáy mới ở đâu…" ~70,6 nghìn view; "TS Nguyễn Trí Hiếu: Vàng cắm đầu…" ~49,4 nghìn;
#   giá vàng hằng ngày (Ngọc Hạnh) 90–116 nghìn; tin 16/11: vàng thấp nhất năm 2026. Kênh mình: Short "1 tỷ mua vàng, 8 tháng còn 757 triệu" @6 +568 (top 3 tuần) – công thức số tiền + mất mát.
#   7 ngày kênh chính chưa làm vàng (đã làm: GDP 16/11, xuất khẩu 17/11, Thái Lan 18/11, nhà đất 19/11, vốn 20/11, Fed 21/11). WiData hết credit tới 20/11 → số từ báo, ghi đủ tên báo + ngày.
# Nguồn:
#  - MarketTimes 16/11/2026 09:23: vàng thế giới mở cửa 16/11 3.875,65 USD/ounce; tuần qua giảm khoảng 4,5% (khoảng 186 USD), tuần giảm sâu nhất từ đầu 6/2026;
#    SJC mua 134,5 – bán 137,5 triệu đồng/lượng; nhẫn SJC 133,3 – 137,3; mức thấp nhất từ đầu năm 2026.
#  - 1thegioi 16/11/2026: SJC bán ra giảm 53,8 triệu/lượng (28,1%) so với đỉnh cuối tháng 1; nhẫn giảm 54,9 triệu (28,6%); đáy năm thế giới 3.852 USD;
#    Phó Chủ tịch Fed Philip Jefferson 14/11: lạm phát là yếu tố quan trọng nhất – kỳ vọng cắt lãi suất nguội; USD và lợi suất trái phiếu Mỹ mạnh lên.
#  - Znews 28/5/2026: vàng miếng lập đỉnh lịch sử 191,3 triệu đồng/lượng cuối tháng 1/2026.
#  - Stockbiz (cập nhật 6/7/2026): đỉnh thế giới 5.594,82 USD/ounce ngày 29/1/2026.
#  - Tinnhanhchungkhoan 2/6/2016: SJC đỉnh 49 triệu cuối tháng 8/2011, cú đổ dốc sau đó về khoảng 33 triệu; VietNamNet 18/4/2025: SJC 33,3 triệu ngày 11/4/2016.
#  - USAGOLD (Gold price history): 1980 đỉnh 850 USD, 1999 khoảng 250 USD (−70%, 19 năm); 2011 đỉnh 1.920 USD (9/2011), cuối 2015 khoảng 1.050 USD (−45%); vượt 2.000 USD năm 2020.
#  - Hà Nội Mới 14/11/2026: Vietcombank bán USD 25.910 đồng. Lãi tiết kiệm 12 tháng NHTM nhà nước 5,4% (WiData 16/11, xem ql_von_385.py).
# Số tự tính:
#  - Thế giới: 1 − 3.875,65/5.594,82 = 30,7%. Người mua đỉnh SJC 191,3 bán lại 134,5: mất 56,8 triệu/lượng = 29,7%.
#  - Giá thế giới quy đổi: 3.875,65 × (37,5/31,1035) × 25.910 = 121,1 triệu/lượng → SJC bán 137,5 cao hơn khoảng 16,4 triệu (khoảng 12%), chưa tính thuế phí.
#  - 2011: SJC 49 → 33 triệu = −32,7% (nói "khoảng một phần ba" → đọc "khoảng ba mươi ba phần trăm"); thế giới 1.920 → 1.050 = −45%.
#  - GIẢ ĐỊNH minh hoạ (chị Thu): 29/1 mua 2 lượng giá 190 triệu = 380 triệu; 16/11 bán lại 134,5 × 2 = 269 triệu → lỗ 111 triệu (29,2%).
#    Nếu gửi tiết kiệm 380 triệu lãi 5,4%/năm từ 29/1 tới 16/11 (293 ngày): 380 × 5,4% × 293/365 = khoảng 16,5 triệu tiền lãi.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261117_0040'
KEY = 'CH2211VANG'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
HA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
WM = 'Blue Marble||World map'
BT = 'ov:Ben Thanh Market||Ben Thanh Market'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('MUA 190 TRIỆU MỘT LƯỢNG', 'GIỜ TIỆM MUA LẠI 134,5'), cols=CR, noti=dict(gio='07:40', ngay='Thứ Hai', items=[
        ('Tin tức', 'Giá vàng sáng nay', 'Vàng miếng xuống thấp nhất từ đầu năm 2026', R_),
        ('Zalo', 'Mẹ', 'Con ơi, vàng xuống nữa rồi, con có bán không?', V_),
        ('Ghi chú', 'Sổ tài sản', '29/1: mua 2 lượng, 380 triệu', X_)]),
      say=("Một trăm chín mươi triệu đồng một lượng. Đó là giá chị Thu, kế toán ở Hà Nội, mua hai lượng vàng miếng vào ngày hai mươi chín tháng một năm nay, đúng những ngày cả nước đổ đi mua vàng. "
           "Sáng nay, mười sáu tháng mười một, chị mở điện thoại: giá vàng miếng xuống thấp nhất từ đầu năm. Tiệm chỉ mua lại một trăm ba mươi tư phẩy năm triệu đồng một lượng. "
           "Mẹ chị nhắn: con ơi, vàng xuống nữa rồi, con có bán không?")),
 dict(k='bignum', anh=HN, cap=('MỖI LƯỢNG MẤT 56,8 TRIỆU', 'NẾU MUA ĐÚNG ĐỈNH'), cols=CR, value=56.8, fmt='{:,.1f}', unit=' TRIỆU', top='MUA ĐỈNH 191,3 – BÁN LẠI 134,5', sub='mỗi lượng vàng miếng – em tự tính', col=RED,
      say=("Năm mươi sáu phẩy tám triệu đồng. Đó là số tiền mất trên mỗi lượng, nếu ai mua đúng đỉnh một trăm chín mươi mốt phẩy ba triệu hồi cuối tháng một rồi bán lại hôm nay. "
           "Gần ba mươi phần trăm, em tự tính. Câu hỏi lớn của video này: vàng đã chạm đáy chưa, lần trước chuyện này kéo dài bao lâu, và tiền trong túi mình nên làm gì?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Mười tháng của chị Thu', cap=('SỔ TÀI SẢN CỦA CHỊ THU', '380 TRIỆU CÒN 269 TRIỆU'), cols=CR, moc=True, giay=dict(tieu_de='SỔ TÀI SẢN – CHỊ THU', so='Em giả định để minh hoạ', dau='TỰ KÊ', dieu=[
        ('29/1: mua 2 lượng, mỗi lượng 190 triệu', '380 TR'),
        ('16/11: tiệm mua lại 134,5 triệu một lượng', '269 TR'),
        ('Số tiền mất nếu bán hôm nay', '111 TR'),
        ('Nếu gửi tiết kiệm 5,4% mỗi năm', '+16,5 TR')]),
      say=("Chị Thu mở cuốn sổ tài sản, số này em giả định để minh hoạ. Hai lượng vàng mua hết ba trăm tám mươi triệu đồng, gần như toàn bộ tiền tiết kiệm sáu năm đi làm. "
           "Bán hôm nay, chị nhận về hai trăm sáu mươi chín triệu. Mất một trăm mười một triệu. "
           "Nếu ngày đó chị để ba trăm tám mươi triệu trong sổ tiết kiệm lãi năm phẩy bốn phần trăm mỗi năm, tới hôm nay chị đã có thêm khoảng mười sáu phẩy năm triệu tiền lãi.")),
 dict(k='chat', cap=('"LÚC ĐÓ CẢ CƠ QUAN', 'AI CŨNG MUA VÀNG MÀ"'), cols=CR, moc=True, chat=dict(ten='Chồng', tv='Đang hoạt động', gio='07:55', mau=G_, msgs=[
        ('Chồng', 'Lúc đó cả cơ quan em ai cũng mua mà'),
        ('me', 'Ừ, em sợ để tiền trong sổ bị mất giá'),
        ('Chồng', 'Giờ bán thì mất hơn trăm triệu, giữ thì không biết đến bao giờ')]),
      say=("Chồng chị nhắn: lúc đó cả cơ quan em ai cũng mua mà. Chị trả lời rằng chị sợ để tiền trong sổ bị mất giá. "
           "Anh nhắn tiếp: giờ bán thì mất hơn trăm triệu, giữ thì không biết đến bao giờ. Đó cũng là câu hỏi của rất nhiều gia đình đã mua vàng trong năm nay.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Vì sao vàng rơi?', anh=WM, cap=('VÀNG THẾ GIỚI', 'MẤT 30,7% TỪ ĐỈNH'), cols=CR, moc=True,
      cards=[('5.594 USD', 'Đỉnh ngày 29/1/2026', 'Mức cao nhất lịch sử'), ('3.875 USD', 'Sáng 16/11/2026', 'Thấp nhất năm nay'), ('30,7%', 'Em tự tính', 'Mất gần một phần ba')],
      say=("Không chỉ ở Việt Nam. Trên thị trường thế giới, vàng lập đỉnh lịch sử năm nghìn năm trăm chín mươi tư đô la một ounce vào ngày hai mươi chín tháng một. "
           "Sáng nay, giá còn khoảng ba nghìn tám trăm bảy mươi lăm đô la, thấp nhất năm. Tức là mất ba mươi phẩy bảy phần trăm, em tự tính. "
           "Riêng tuần vừa rồi, vàng giảm khoảng bốn phẩy năm phần trăm, tuần giảm sâu nhất kể từ đầu tháng sáu.")),
 dict(k='noti', cap=('MỸ CHƯA CHỊU HẠ LÃI SUẤT', 'VÀNG KHÔNG SINH LÃI'), cols=CR, moc=True, noti=dict(gio='08:10', ngay='Thứ Hai', items=[
        ('Tin tức', 'Fed', 'Phó Chủ tịch Fed: lạm phát vẫn là yếu tố quan trọng nhất', R_),
        ('Tin tức', 'Đô la Mỹ', 'Đồng đô la và lợi suất trái phiếu Mỹ tiếp tục tăng', V_),
        ('Tin tức', 'Kỳ vọng', 'Hy vọng Fed sớm giảm lãi suất nguội lạnh', X_)]),
      say=("Lý do nằm ở nước Mỹ. Ngày mười bốn tháng mười một, Phó Chủ tịch Ngân hàng Trung ương Mỹ nói lạm phát vẫn là yếu tố quan trọng nhất khi quyết định lãi suất. "
           "Hy vọng lãi suất sớm giảm nguội đi, đồng đô la và lợi suất trái phiếu Mỹ tiếp tục tăng. "
           "Khi gửi đô la hay mua trái phiếu được trả lãi cao, thì vàng, một thứ không sinh ra đồng lãi nào, kém hấp dẫn hẳn đi.")),
 dict(k='bignum', anh=HN, cap=('VÀNG MIẾNG SJC', 'CAO HƠN THẾ GIỚI 16,4 TRIỆU'), cols=CR, moc=True, value=16.4, fmt='{:,.1f}', unit=' TRIỆU', top='CHÊNH VỚI GIÁ THẾ GIỚI QUY ĐỔI', sub='mỗi lượng, sáng 16/11 – em tự tính', col=RED,
      say=("Và đây là cú lật mà nhiều người không để ý. Quy đổi theo giá bán đô la ở ngân hàng, giá vàng thế giới sáng nay chỉ khoảng một trăm hai mươi mốt triệu đồng một lượng. "
           "Vàng miếng trong nước bán ra một trăm ba mươi bảy phẩy năm triệu. Cao hơn khoảng mười sáu phẩy bốn triệu đồng mỗi lượng, em tự tính, chưa kể thuế phí. "
           "Nghĩa là ngay cả khi giá thế giới đứng yên, phần chênh này vẫn có thể co lại, và người cầm vàng miếng chịu thêm một lần thiệt.")),
 dict(k='giay', cap=('MUA VÀO VÀ BÁN RA', 'CHÊNH NGAY 3 TRIỆU'), cols=CR, moc=True, giay=dict(tieu_de='BẢNG GIÁ SÁNG 16/11/2026', so='MarketTimes 16/11/2026, đơn vị triệu đồng/lượng', dau='NIÊM YẾT', dieu=[
        ('Vàng miếng: tiệm mua vào', '134,5'),
        ('Vàng miếng: tiệm bán ra', '137,5'),
        ('Nhẫn trơn: tiệm mua vào', '133,3'),
        ('Nhẫn trơn: tiệm bán ra', '137,3')]),
      say=("Chị Thu chụp bảng giá sáng nay. Vàng miếng tiệm mua vào một trăm ba mươi tư phẩy năm, bán ra một trăm ba mươi bảy phẩy năm. "
           "Nhẫn trơn mua vào một trăm ba mươi ba phẩy ba, bán ra một trăm ba mươi bảy phẩy ba. "
           "Tức là ai mua hôm nay rồi bán ngay, đã mất từ ba triệu đến bốn triệu đồng mỗi lượng. Vàng phải tăng ít nhất chừng đó mới hoà vốn.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước: năm 2011', cap=('MẸ MUA ĐỈNH 49 TRIỆU', 'CHỜ GẦN 9 NĂM'), cols=CR, moc=True, call=dict(ten='Mẹ', phu='Gọi thoại', mau=V_, loi=[
        'Năm 2011 mẹ cũng mua đúng đỉnh 49 triệu',
        'Mấy năm sau xuống còn 33 triệu']),
      say=("Mẹ chị Thu gọi điện. Bà kể năm hai nghìn không trăm mười một, bà cũng mua vàng đúng đỉnh, khoảng bốn mươi chín triệu đồng một lượng. "
           "Mấy năm sau, giá chỉ còn khoảng ba mươi ba triệu. Bà không bán, cứ cất trong tủ, chờ. Và bà phải chờ rất lâu.")),
 dict(k='giay', cap=('LẦN TRƯỚC: NĂM 2011', 'CHỜ GẦN 9 NĂM'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='Tinnhanhchungkhoan 2/6/2016, VietNamNet, USAGOLD', dau='ĐÃ XẢY RA', dieu=[
        ('Cuối 8/2011: vàng miếng lập đỉnh', '49 TR'),
        ('Năm 2016: vàng miếng còn khoảng', '33 TR'),
        ('Thế giới: 1.920 USD năm 2011 còn 1.050', 'MẤT 45%'),
        ('Năm vượt lại đỉnh cũ', '2020')]),
      say=("Đây là những con số của lần trước. Cuối tháng tám năm hai nghìn không trăm mười một, vàng miếng lập đỉnh bốn mươi chín triệu đồng. Năm hai nghìn không trăm mười sáu, giá còn khoảng ba mươi ba triệu, mất khoảng ba mươi ba phần trăm, em tự tính. "
           "Trên thế giới, vàng đi từ một nghìn chín trăm hai mươi đô la một ounce. Tới cuối năm hai nghìn không trăm mười lăm, giá chỉ còn khoảng một nghìn không trăm năm mươi đô la, mất bốn mươi lăm phần trăm. "
           "Phải tới năm hai nghìn không trăm hai mươi, giá mới vượt lại đỉnh cũ. Người mua đỉnh đã phải chờ gần chín năm.")),
 dict(k='bars', anh=WM, cap=('ĐỈNH VÀNG VÀ CÚ RƠI', 'NĂM 1980, 2011 VÀ 2026'), cols=CR, moc=True,
      bars=[('Năm 1980', 70, R_, 'Mất 70%'), ('Năm 2011', 45, V_, 'Mất 45%'), ('Năm 2026', 30.7, X_, 'Đã mất 30,7%')],
      say=("Em lùi xa hơn nữa. Tháng một năm một nghìn chín trăm tám mươi, vàng thế giới lên tám trăm năm mươi đô la một ounce. Sau đó giá rơi dần. Tới năm một nghìn chín trăm chín mươi chín, vàng chỉ còn khoảng hai trăm năm mươi đô la, mất bảy mươi phần trăm sau mười chín năm. "
           "Năm hai nghìn không trăm mười một mất bốn mươi lăm phần trăm. Còn lần này, mới mười tháng, đã mất ba mươi phẩy bảy phần trăm.")),
 dict(k='checklist', anh=HN, cap=('LẦN NÀY VÀ NĂM 2011', 'GIỐNG 2, KHÁC 2'), cols=CR, moc=True,
      items=[('Giống: người dân xếp hàng ở đỉnh', R_), ('Giống: Mỹ đổi hướng lãi suất', R_), ('Khác: lần này rơi nhanh hơn', V_), ('Khác: giá trong nước chênh lớn', V_)],
      say=("Đặt hai lần cạnh nhau, có hai điểm giống. Một: đỉnh giá đều đến lúc người dân xếp hàng mua vì sợ tiền mất giá. Hai: vàng quay đầu khi nước Mỹ không còn hạ lãi suất. "
           "Và hai điểm khác. Lần này giá rơi nhanh hơn nhiều, mười tháng đã mất khoảng ba mươi mốt phần trăm. Và giá trong nước đang cao hơn thế giới khoảng mười hai phần trăm. "
           "Lịch sử chưa lặp lại, nhưng chưa, không có nghĩa là không thể.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='chat', ch='Chương 4 – Bán, giữ hay mua thêm?', cap=('"HAY MÌNH MUA THÊM', 'CHO GIÁ TRUNG BÌNH THẤP?"'), cols=CR, moc=True, chat=dict(ten='Chồng', tv='Đang hoạt động', gio='12:15', mau=G_, msgs=[
        ('Chồng', 'Hay vay thêm mua 2 lượng nữa cho giá trung bình thấp?'),
        ('me', 'Nếu giá xuống tiếp như năm 2011 thì sao?'),
        ('Chồng', 'Thì vừa lỗ vàng vừa trả lãi vay...')]),
      say=("Buổi trưa, chồng chị Thu nhắn: hay vay thêm mua hai lượng nữa, cho giá trung bình thấp xuống? Chị hỏi lại: nếu giá xuống tiếp như năm hai nghìn không trăm mười một thì sao? "
           "Anh im lặng một lúc rồi nhắn: thì vừa lỗ vàng, vừa trả lãi vay. Vay tiền để mua thêm một thứ không sinh lãi, là cách biến khoản lỗ có thể chờ được thành khoản lỗ không chờ được.")),
 dict(k='cards', anh=HA, cap=('BA CON ĐƯỜNG', 'CỦA NHÀ CHỊ THU'), cols=CC, moc=True,
      cards=[('Giữ 2 lượng', 'Không vay, chờ được nhiều năm', 'Chấp nhận chờ lâu'), ('Bán 1 lượng', 'Lấy 134,5 triệu làm quỹ dự phòng', 'Bớt áp lực'), ('Vay mua thêm', 'Lỗ vàng cộng tiền lãi', 'Rủi ro nhất')],
      say=("Hai vợ chồng ngồi viết ra ba con đường. Một: giữ nguyên hai lượng, không vay, chấp nhận có thể phải chờ nhiều năm như mẹ. "
           "Hai: bán một lượng, lấy một trăm ba mươi tư phẩy năm triệu làm quỹ dự phòng, phần còn lại cứ để đó. "
           "Ba: vay mua thêm. Con đường này chỉ đẹp khi giá tăng lại ngay, còn nếu giá đi như năm hai nghìn không trăm mười một, đây là con đường đau nhất.")),
 dict(k='chat', cap=('KẾ HOẠCH NHÀ CHỊ THU', 'KHÔNG VAY, CÓ QUỸ DỰ PHÒNG'), cols=CC, moc=True, chat=dict(ten='Chồng', tv='Đang hoạt động', gio='21:30', mau=G_, msgs=[
        ('me', 'Không vay nữa anh ạ'),
        ('Chồng', 'Ừ, giữ vàng, nhưng phải có 6 tháng chi tiêu bằng tiền mặt'),
        ('me', 'Từ giờ vàng không quá 1/5 tài sản nhà mình')]),
      say=("Tối đó, chị Thu chốt với chồng: không vay nữa. Anh đồng ý giữ vàng, nhưng nhà phải có đủ sáu tháng chi tiêu bằng tiền mặt trong sổ tiết kiệm. "
           "Chị thêm một quy tắc cho riêng nhà mình: từ giờ, vàng không chiếm quá hai mươi phần trăm tổng tài sản. "
           "Không phải vì vàng xấu, mà vì không nên để một thứ quyết định cả năm tài chính của gia đình.")),
 dict(k='checklist', anh=HA, cap=('PHÉP THỬ CỦA ANH CHỊ', 'VÀNG CHIẾM BAO NHIÊU TÀI SẢN?'), cols=CC, moc=True,
      items=[('Dưới 20%: ngủ ngon', G_), ('20 đến 50%: cần quỹ dự phòng', V_), ('Trên 50% hoặc có vay: nguy hiểm', R_)],
      say=("Và đây là phép thử anh chị tự làm được tối nay. Cộng giá trị số vàng nhà mình theo giá tiệm mua vào, rồi chia cho tổng tài sản. "
           "Dưới hai mươi phần trăm, giá lên xuống anh chị vẫn ngủ ngon. Từ hai mươi đến năm mươi phần trăm, cần một quỹ dự phòng đủ dày để không phải bán lúc giá thấp. "
           "Trên năm mươi phần trăm, hoặc vàng mua bằng tiền vay, đó là lúc nguy hiểm. Đây là mốc em đặt để tự soi, không phải quy định.")),
 dict(k='checklist', ch='Chương 5 – Theo dõi gì để biết sớm?', anh=TP, cap=('3 ĐIỀU CẦN THEO DÕI', 'TRƯỚC KHI QUYẾT ĐỊNH'), cols=CC, moc=True,
      items=[('Fed họp ngày 8 và 9/12', V_), ('Chênh giá trong nước và thế giới', R_), ('Chênh giá mua vào và bán ra', V_)],
      say=("Muốn biết sớm vàng đi tiếp thế nào, em gợi ý theo dõi ba điều. Một: cuộc họp của Ngân hàng Trung ương Mỹ ngày tám và chín tháng mười hai, giữ, tăng hay giảm lãi suất. "
           "Hai: khoảng chênh giữa giá vàng miếng và giá thế giới quy đổi, đang khoảng mười sáu triệu, co lại hay nới ra. Ba: khoảng chênh giá mua vào và bán ra ở tiệm. "
           "Khi tiệm nới rộng khoảng này, thường là lúc họ cũng không chắc giá sẽ đi đâu. "
           "Còn với phần tiền anh chị đặt vào cổ phiếu, lợi nhuận từng quý của hơn bốn trăm doanh nghiệp có miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn của mẹ', cap=('"VÀNG KHÔNG CÓ LỖI', 'LỖI LÀ MUA LÚC AI CŨNG MUA"'), cols=CC, moc=True, chat=dict(ten='Mẹ', tv='Đang hoạt động', gio='22:10', mau=V_, msgs=[
        ('Mẹ', 'Vàng không có lỗi đâu con'),
        ('Mẹ', 'Lỗi là mua lúc ai cũng mua, bằng tiền mình cần dùng'),
        ('me', 'Vâng, con giữ, nhưng không vay nữa')]),
      say=("Gần khuya, mẹ nhắn thêm: vàng không có lỗi đâu con, lỗi là mua lúc ai cũng mua, bằng tiền mình sắp cần dùng. Chị Thu trả lời rằng chị sẽ giữ, nhưng không vay thêm đồng nào. "
           "Năm hai nghìn không trăm mười một, người mất nhiều nhất không phải người mua vàng, mà là người phải bán vàng đúng lúc giá thấp nhất.")),
 dict(k='end', cap=('VÀNG MẤT 30%', 'ANH CHỊ BÁN HAY GIỮ?'), cols=CC,
      say=("Còn anh chị thì sao: vàng đang chiếm bao nhiêu phần tài sản của nhà mình, dưới hai mươi phần trăm, từ hai mươi đến năm mươi phần trăm, hay trên năm mươi phần trăm? Và anh chị đang giữ, bán, hay chờ mua thêm? "
           "Kể cho em và mọi người ở phần bình luận nhé. Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vàng Mất 30% Từ Đỉnh: Mua 191 Triệu, Giờ Tiệm Mua Lại 134,5 – Lần Trước Phải Chờ 9 Năm?'
MT = ("Vàng miếng xuống thấp nhất năm 2026: tiệm mua vào 134,5 triệu/lượng, trong khi đỉnh cuối tháng 1 là 191,3 triệu. Vàng thế giới mất 30,7% từ đỉnh 5.594 USD. "
      "Lần trước, năm 2011, vàng miếng từ 49 triệu về khoảng 33 triệu và phải tới năm 2020 mới vượt lại đỉnh cũ. Lần này giống và khác ở đâu? Câu chuyện của chị Thu, người mẹ từng mua đỉnh 2011, và phép thử cho chính gia đình anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• MarketTimes 16/11/2026: vàng thế giới mở cửa 16/11 3.875,65 USD/ounce, tuần qua giảm khoảng 4,5% (tuần giảm sâu nhất từ đầu 6/2026); SJC mua 134,5 – bán 137,5 triệu/lượng; nhẫn SJC 133,3 – 137,3; thấp nhất từ đầu năm 2026\n"
      "• 1thegioi 16/11/2026: SJC bán ra giảm 53,8 triệu (28,1%) so với đỉnh cuối tháng 1; Phó Chủ tịch Fed Philip Jefferson 14/11: lạm phát vẫn là yếu tố quan trọng nhất; USD và lợi suất trái phiếu Mỹ tăng\n"
      "• Znews 28/5/2026: vàng miếng lập đỉnh lịch sử 191,3 triệu đồng/lượng cuối tháng 1/2026\n"
      "• Stockbiz 7/2026: đỉnh vàng thế giới 5.594,82 USD/ounce ngày 29/1/2026\n"
      "• Tinnhanhchungkhoan 2/6/2016: SJC đỉnh 49 triệu cuối 8/2011, sau đó về khoảng 33 triệu; VietNamNet: SJC 33,3 triệu ngày 11/4/2016\n"
      "• USAGOLD: vàng 850 USD (1/1980) → khoảng 250 USD (1999), −70%; 1.920 USD (9/2011) → khoảng 1.050 USD (cuối 2015), −45%; vượt 2.000 USD năm 2020\n"
      "• Hà Nội Mới 14/11/2026: Vietcombank bán USD 25.910 đồng; lãi tiết kiệm 12 tháng NHTM nhà nước 5,4%\n"
      "• Em tự tính: thế giới 1 − 3.875,65/5.594,82 = 30,7%; mua đỉnh 191,3, bán lại 134,5 → mất 56,8 triệu/lượng (29,7%); giá thế giới quy đổi 3.875,65 × 37,5/31,1035 × 25.910 ≈ 121,1 triệu/lượng → SJC bán ra cao hơn khoảng 16,4 triệu (chưa tính thuế phí)\n"
      "• Sổ tài sản chị Thu là giả định minh hoạ: 2 lượng × 190 triệu = 380 triệu; bán lại 2 × 134,5 = 269 triệu → mất 111 triệu; gửi tiết kiệm 5,4%/năm trong 293 ngày ≈ 16,5 triệu tiền lãi\n\n"
      "Tra lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật chị Thu và gia đình là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-22', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['giá vàng', 'giá vàng hôm nay', 'vàng SJC', 'vàng giảm', 'vàng nhẫn', 'mua vàng', 'Fed', 'lãi suất', 'tài chính cá nhân', 'vĩ mô'],
    bia_hook=['VÀNG MẤT 30%', 'CHỜ 9 NĂM???'], badge='LẦN TRƯỚC LÀ NĂM 2011',
    bia_anh='Hanoi skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['MUA 191 TRIỆU', 'BÁN 134,5'], badge_b='MỖI LƯỢNG VÀNG MIẾNG',
    bia_hook_c=['THẤP NHẤT', 'NĂM 2026???'], badge_c='TUẦN QUA GIẢM 4,5%',
    reel_hook='VÀNG MẤT 30% TỪ ĐỈNH|LẦN TRƯỚC CHỜ 9 NĂM???',
    fb_post=("Vàng mất 30% từ đỉnh 🟡\n\n👉 Đỉnh cuối tháng 1: 191,3 triệu/lượng – sáng 16/11 tiệm mua lại 134,5 triệu\n👉 Giá trong nước vẫn cao hơn thế giới khoảng 16 triệu/lượng\n"
             "👉 Năm 2011 vàng miếng từ 49 triệu về 33 triệu, tới 2020 mới vượt đỉnh\n\nVàng chiếm bao nhiêu phần tài sản nhà anh chị?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: vàng mất 30 phần trăm từ đỉnh, lần trước chờ 9 năm (NV1 17/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
CX = {'noti': ('tò mò', 'chuông thông báo'), 'chat': ('tâm sự', 'tiếng gõ phím'), 'call': ('trầm, lo', 'chuông gọi'), 'giay': ('căng', 'lật giấy'),
      'bignum': ('sốc', 'trống nhấn'), 'cards': ('suy nghĩ', 'nền phố'), 'bars': ('so sánh', 'nền phố'), 'checklist': ('quyết tâm', 'tick'), 'text': ('ngộ ra', 'nền nhẹ'), 'end': ('mở', 'nhạc kết')}
with open(LO + '/phan_canh.md', 'w', encoding='utf-8') as f:
    f.write('| # | loại | hình (thẻ form cũ) | cảm xúc | tiếng động |\n|---|---|---|---|---|\n')
    for i, c in enumerate(S, 1):
        cx = CX.get(c['k'], ('', '')); f.write('| %d | the/%s | %s | %s | %s |\n' % (i, c['k'], ' / '.join(c.get('cap', ('', ''))), cx[0], cx[1]))
from collections import Counter
cnt = Counter(c['k'] for c in S); dt = sum(cnt[k] for k in ('chat', 'noti', 'call', 'giay'))
print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dien thoai/giay %d/%d' % (dt, len(S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
