# -*- coding: utf-8 -*-
# NV1 12/11/2026 00:39 – VIDEO DÀI kênh chính, "câu hỏi lớn": Việt Nam đang nợ bao nhiêu? (cặp với reel RV1211NO).
# Lý do chọn: data/view/xu_huong.md tuần 5–11/11: "Việt Nam đang nợ ai? Tiền đang đi đâu?" ~200 nghìn view (14 phút),
#   "2000 tỷ USD kéo VN vào khủng hoảng" ~72 nghìn → chủ đề nợ/tiền đang nóng; kênh mình 7 ngày chưa làm (đã làm: xuất khẩu, vàng, PNJ, IPO, lãi kỷ lục).
# Nguồn (WiData – Bộ Tài chính, NHNN, TCTK), đơn vị tỷ đồng; SỐ TỰ TÍNH ghi rõ:
#  - Nợ Chính phủ 2025: 4.072.002; nợ Chính phủ bảo lãnh 2025: 202.105 → nợ công (tự cộng) 4.274.107.
#  - GDP danh nghĩa 4 quý tới Q4/2025: 12.847.571 → nợ công/GDP 33,3%, nợ CP/GDP 31,7% (tự tính).
#  - 2018: nợ CP 2.767.229 + bảo lãnh 437.372 = 3.204.601; GDP 7.009.042 → 45,7% (tự tính). Nợ CP 2018→2025 +47%, GDP +83%.
#  - Nợ nước ngoài quốc gia 2025: 3.286.569 → 25,6% GDP (tự tính).
#  - Dân số 2025: 102.345 nghìn → nợ công/người 41,8 triệu; tín dụng/người 200 triệu (tự tính, chia đều).
#  - Tổng tín dụng 8/2026: 20.489.434 (≈ 793 tỷ USD theo tỷ giá NHTM bán 25.840 ngày 11/11/2026); 4,8 lần nợ công.
#  - Tín dụng/GDP (tự tính, tín dụng cuối kỳ / GDP 4 quý): 12/2016 97,6% · 12/2020 114,3% · 12/2022 123,9% · 12/2024 135,7% · 12/2025 144,7% · 8/2026 145,8% (GDP 4 quý tới Q3/2026 14.056.614).
#  - Tín dụng +17,4% so cùng kỳ (8/2026); tổng tiền gửi +13,6% (bảng đã điều chỉnh); GDP danh nghĩa 4 quý +12,9% (tự tính).
#  - Tín dụng "các hoạt động dịch vụ khác" (phần lớn kinh doanh BĐS + tiêu dùng/vay mua nhà) 8/2026: 9.238.445 = 45,1% tổng; +24,4% so 8/2025 (7.428.885).
#  - Chênh tín dụng − tổng tiền gửi: 8/2026 20.489.434 − 17.771.452 = 2.717.982; 8/2025 17.455.204 − 15.959.293 = 1.495.911 → gấp 1,8 lần (tự tính).
#  - Lãi suất huy động 12 tháng NHTM Nhà nước 11/11/2026: 5,4%; CPI 10/2026 +5,09% → lãi thực khoảng 0,3 điểm %.
#  - Thu nhập bình quân lao động Q3/2026: 9,18 triệu đồng/tháng.
#  - Tin: VietnamFinance 29/10/2026 "Loạt ngân hàng có thể 'cạn' room tín dụng sau quy định mới của NHNN"; VnEconomy 2/11/2026 "Tỷ lệ nợ công so với GDP của Mỹ cao nhất 80 năm".
#  - Lịch sử: 2007 tín dụng tăng 53,89% (NHNN); 2008 CPI bình quân 22,97% (TCTK).
#  - Khoản vay minh hoạ (tự tính, trả đều gốc+lãi 240 tháng): 1,2 tỷ: 8% → 10,04 triệu/tháng; 10% → 11,58 triệu; 11% → 12,39 triệu; chênh 8→10% 1,54 triệu/tháng, 18,5 triệu/năm; tổng trả 2,41 tỷ vs 2,78 tỷ (+371 triệu). Vay 1 tỷ ở 10% → 9,65 triệu.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261112_0039'
KEY = 'CH1411NO'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
NGAN = 'ov:bank loan contract signing||loan document'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('"NƯỚC MÌNH NỢ NGẬP ĐẦU', 'RÚT TIỀN ĐI CON"'), cols=CR, noti=dict(gio='23:10', ngay='Thứ Ba', items=[
        ('Zalo', 'Mẹ', 'Con xem cái này đi, nước mình nợ ngập đầu rồi', R_),
        ('Zalo', 'Mẹ', 'Mai mẹ ra rút hết sổ tiết kiệm mua vàng', R_),
        ('Tin nhắn', 'Ngân hàng', 'Lãi suất khoản vay của quý khách sẽ được điều chỉnh từ kỳ tới', V_)]),
      say=("Mười một giờ đêm, anh Tuấn vừa ru con ngủ thì điện thoại rung liên tục. Mẹ anh gửi một đường link, kèm hai dòng: con xem cái này đi, nước mình nợ ngập đầu rồi. Mai mẹ ra rút hết sổ tiết kiệm mua vàng. "
           "Ngay bên dưới là tin nhắn của ngân hàng nơi anh đang vay mua nhà: lãi suất khoản vay của quý khách sẽ được điều chỉnh từ kỳ tới. Hai tin nhắn, hai nỗi sợ, cùng một câu hỏi: Việt Nam đang nợ bao nhiêu, và khoản nợ đó có chạm vào túi mình không?")),
 dict(k='bignum', anh='ov:hanoi city skyline night||vietnam city skyline', cap=('NỢ CÔNG VIỆT NAM 2025', 'NHƯNG ĐÂY CHƯA PHẢI CHUYỆN LỚN'), cols=CC, value=33.3, fmt='{:,.1f}', unit='% GDP', top='NỢ CÔNG / GDP NĂM 2025', sub='Khoảng 4,27 triệu tỷ đồng', col=GOLD,
      say=("Em nói luôn kết quả để anh chị đỡ hồi hộp. Nợ công của Việt Nam năm 2025 vào khoảng ba mươi ba phần trăm GDP, thấp hơn rất nhiều so với những gì mẹ anh Tuấn đang lo. "
           "Nhưng trong lúc lục số liệu, anh Tuấn tìm ra một khoản nợ khác lớn gần gấp năm lần nợ công, lớn hơn cả GDP cả nước. Và khoản nợ đó nằm ngay trong tờ hợp đồng vay đang để trong ngăn kéo nhà anh.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Nhà nước nợ bao nhiêu?', cap=('"NỢ BAO NHIÊU', 'MÀ MẸ SỢ THẾ?"'), cols=CC, moc=True, chat=dict(ten='Mẹ', tv='Đang hoạt động', gio='23:25', mau=X_, msgs=[
        ('me', 'Mẹ ơi, nợ công mình khoảng 33% GDP thôi'),
        ('Mẹ', 'Thế là nhiều hay ít hả con?'),
        ('me', 'Nhiều nước giàu còn cao hơn mình mấy lần mẹ ạ'),
        ('Mẹ', 'Thế sao người ta bảo sắp vỡ nợ?')]),
      say=("Anh Tuấn nhắn lại cho mẹ: mẹ ơi, nợ công mình khoảng ba mươi ba phần trăm GDP thôi. Mẹ hỏi: thế là nhiều hay ít hả con? Anh trả lời: nhiều nước giàu còn cao hơn mình mấy lần mẹ ạ. "
           "Mẹ vẫn chưa yên: thế sao người ta bảo sắp vỡ nợ? Câu hỏi đó hợp lý, nên mình cùng xem con số thật.")),
 dict(k='cards', anh='ov:government building vietnam||hanoi city', cap=('NỢ CÔNG NĂM 2025', 'TỶ ĐỒNG'), cols=CC, moc=True,
      cards=[('4.072.002', 'Nợ Chính phủ vay trực tiếp', '31,7% GDP'), ('202.105', 'Nợ Chính phủ bảo lãnh', 'giảm hơn một nửa từ 2018'), ('41,8 triệu', 'Chia đều mỗi người dân', '102,3 triệu dân, tự tính')],
      say=("Theo số liệu Bộ Tài chính tổng hợp trên WiData, năm 2025, Chính phủ vay trực tiếp khoảng bốn triệu không trăm bảy mươi hai nghìn tỷ đồng. Thêm khoảng hai trăm lẻ hai nghìn tỷ nợ do Chính phủ đứng ra bảo lãnh. "
           "Cộng lại, nợ công khoảng bốn phẩy hai bảy triệu tỷ đồng. Chia đều cho hơn một trăm lẻ hai triệu dân, mỗi người khoảng bốn mươi mốt phẩy tám triệu đồng. Nghe thì giật mình, nhưng phải đặt cạnh quy mô nền kinh tế mới hiểu.")),
 dict(k='bars', anh='ov:hanoi city skyline||vietnam city', cap=('NỢ CÔNG / GDP', 'ĐANG GIẢM, KHÔNG PHẢI TĂNG'), cols=CC, moc=True,
      bars=[('2018', 45.7, GOLD, '45,7%'), ('2025', 33.3, GREEN, '33,3%')],
      say=("Và đây là cú lật đầu tiên. Năm 2018, nợ công bằng khoảng bốn mươi lăm phẩy bảy phần trăm GDP. Đến năm 2025 chỉ còn khoảng ba mươi ba phẩy ba phần trăm. "
           "Nợ Chính phủ vẫn tăng khoảng bốn mươi bảy phần trăm trong bảy năm. Nhưng GDP danh nghĩa tăng tới tám mươi ba phần trăm, nên gánh nợ so với sức kiếm tiền của đất nước nhẹ đi chứ không nặng lên. Đây là số em tự tính, nguồn có trong mô tả.")),
 dict(k='cards', anh='ov:world map finance||globe economy', cap=('NỢ NƯỚC NGOÀI QUỐC GIA', 'CẢ NHÀ NƯỚC VÀ TƯ NHÂN'), cols=CC, moc=True,
      cards=[('25,6% GDP', 'Nợ nước ngoài năm 2025', 'khoảng 3,29 triệu tỷ đồng'), ('80 NĂM', 'Mỹ: nợ công / GDP cao nhất', 'VnEconomy 2/11/2026')],
      say=("Còn nợ nước ngoài, tức tiền cả Nhà nước lẫn doanh nghiệp vay từ bên ngoài. Năm 2025, con số này khoảng ba phẩy hai chín triệu tỷ đồng, chừng hai mươi lăm phẩy sáu phần trăm GDP. "
           "Trong khi đó, báo VnEconomy ngày hai tháng mười một vừa đưa tin tỷ lệ nợ công so với GDP của Mỹ đã lên mức cao nhất tám mươi năm. Nên nếu chỉ nhìn nợ công, Việt Nam chưa phải nước đáng lo. Mẹ anh Tuấn có thể ngủ yên. Nhưng anh Tuấn thì không.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='bignum', ch='Chương 2 – Khoản nợ lớn hơn cả GDP', anh='ov:bank vault money||banknotes stack', cap=('TỔNG DƯ NỢ CHO VAY', 'THÁNG 8/2026'), cols=CR, moc=True, value=20.49, fmt='{:,.2f}', unit=' triệu tỷ', top='TÍN DỤNG TOÀN NỀN KINH TẾ', sub='Gấp 4,8 lần nợ công', col=RED,
      say=("Khoản nợ khiến anh Tuấn mất ngủ không nằm ở Chính phủ, mà nằm ở ngân hàng. Đó là tiền ngân hàng cho doanh nghiệp và người dân vay. Đến tháng tám năm 2026, tổng dư nợ cho vay của cả nền kinh tế là khoảng hai mươi phẩy bốn chín triệu tỷ đồng. "
           "Quy ra đô la theo tỷ giá hôm nay, khoảng bảy trăm chín mươi ba tỷ đô la, gấp khoảng bốn phẩy tám lần toàn bộ nợ công.")),
 dict(k='bars', anh='ov:bank vault money||banknotes stack', cap=('DƯ NỢ CHO VAY / GDP', 'TỰ TÍNH TỪ SỐ NHNN, TCTK'), cols=CR, moc=True,
      bars=[('2016', 97.6, GOLD, '97,6%'), ('2020', 114.3, GOLD, '114,3%'), ('2022', 123.9, RED, '123,9%'), ('2024', 135.7, RED, '135,7%'), ('2025', 144.7, RED, '144,7%'), ('8/2026', 145.8, RED, '145,8%')],
      say=("So với quy mô nền kinh tế, cuối năm 2016 dư nợ cho vay bằng khoảng chín mươi bảy phẩy sáu phần trăm GDP. Năm 2020 lên một trăm mười bốn phần trăm. Năm 2024 khoảng một trăm ba mươi sáu phần trăm. "
           "Và đến tháng tám năm nay là khoảng một trăm bốn mươi sáu phần trăm. Tức là cứ nền kinh tế làm ra một trăm đồng mỗi năm, thì đang có khoảng một trăm bốn mươi sáu đồng là tiền đi vay ngân hàng. Mười năm, dư nợ tăng gần gấp bốn, còn GDP danh nghĩa chỉ tăng khoảng hai phẩy năm lần.")),
 dict(k='cards', anh='ov:bank vault money||banknotes stack', cap=('TRONG 12 THÁNG QUA', 'TIỀN VAY CHẠY NHANH HƠN'), cols=CR, moc=True,
      cards=[('+17,4%', 'Dư nợ cho vay', 'so với tháng 8/2025'), ('+12,9%', 'GDP danh nghĩa 4 quý', 'em tự tính'), ('200 triệu', 'Chia đều mỗi người dân', 'gồm cả nợ doanh nghiệp')],
      say=("Trong mười hai tháng qua, dư nợ cho vay tăng khoảng mười bảy phẩy bốn phần trăm, trong khi GDP danh nghĩa chỉ tăng khoảng mười hai phẩy chín phần trăm. Nợ đang lớn nhanh hơn thu nhập. "
           "Nếu chia đều dư nợ đó cho mỗi người dân, kể cả em bé mới sinh, con số là khoảng hai trăm triệu đồng một người. Dĩ nhiên phần lớn là nợ của doanh nghiệp, nhưng nó cho anh chị thấy nền kinh tế đang chạy bằng tiền vay nhiều đến mức nào.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='giay', ch='Chương 3 – Tiền vay đi đâu?', cap=('HỢP ĐỒNG VAY', 'MUA NHÀ CỦA ANH TUẤN'), cols=CC, moc=True, giay=dict(tieu_de='HỢP ĐỒNG TÍN DỤNG', so='Khách hàng: Nguyễn Văn Tuấn – vay mua căn hộ', dau='ĐÃ KÝ', dieu=[
        ('Số tiền vay: 1.200.000.000 đồng, thời hạn 20 năm.', '1,2 TỶ'),
        ('Lãi suất 2 năm đầu: 8%/năm, cố định.', '8%'),
        ('Sau đó: lãi suất cơ sở cộng biên độ, điều chỉnh 3 tháng một lần.', 'THẢ NỔI')]),
      say=("Anh Tuấn mở ngăn kéo, lấy hợp đồng vay ra đọc lại. Vay một phẩy hai tỷ đồng, hai mươi năm, để mua căn hộ chung cư. Hai năm đầu lãi suất tám phần trăm cố định. "
           "Sau đó là dòng chữ nhỏ mà lúc ký anh không để ý: lãi suất cơ sở cộng biên độ, điều chỉnh ba tháng một lần. Anh chợt hiểu, mình chính là một phần trong con số hai mươi triệu tỷ kia.")),
 dict(k='cards', anh='ov:apartment buildings construction||apartment building', cap=('TIỀN VAY DỒN VÀO ĐÂU?', 'THÁNG 8/2026'), cols=CR, moc=True,
      cards=[('45%', 'Nhóm "dịch vụ khác" trong tổng dư nợ', 'khoảng 9,24 triệu tỷ'), ('+24,4%', 'Nhóm này tăng trong 1 năm', 'tổng dư nợ chỉ +17,4%')],
      say=("Vậy hai mươi triệu tỷ đó chảy vào đâu? Trong số liệu của Ngân hàng Nhà nước có một nhóm tên khô khan là các hoạt động dịch vụ khác. Phần lớn nhóm này là cho vay kinh doanh bất động sản và cho vay tiêu dùng, mà chủ yếu là vay mua nhà như anh Tuấn. "
           "Nhóm này chiếm khoảng bốn mươi lăm phần trăm tổng dư nợ, khoảng chín phẩy hai bốn triệu tỷ đồng. Nó tăng hai mươi bốn phẩy bốn phần trăm chỉ trong một năm, nhanh hơn hẳn mức tăng chung. Tiền vay đang dồn về nhà đất.")),
 dict(k='call', cap=('"ANH ĐANG ĐỨNG', 'Ở PHÍA RỦI RO"'), cols=CC, call=dict(ten='Bạn thân Hải', phu='Làm tín dụng 10 năm', mau=G_, loi=[
        'Ngân hàng cho vay nhanh hơn huy động', 'Thiếu vốn thì lãi suất khó mà giảm']),
      say=("Anh Tuấn gọi cho Hải, bạn thân làm tín dụng ở ngân hàng mười năm. Hải nói thẳng: vấn đề không nằm ở việc nước mình vỡ nợ. Vấn đề là ngân hàng đang cho vay nhanh hơn tốc độ họ huy động được tiền. "
           "Mà ngân hàng thiếu vốn thì phải trả lãi cao hơn để giữ tiền gửi, và người vay như ông sẽ là người trả phần chênh đó.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='noti', ch='Chương 4 – Ngân hàng lấy tiền đâu cho vay?', cap=('NGÂN HÀNG', 'SẮP HẾT ROOM?'), cols=CR, noti=dict(gio='00:15', ngay='Thứ Tư', items=[
        ('Tin tức', 'VietnamFinance 29/10', 'Loạt ngân hàng có thể cạn room tín dụng sau quy định mới', R_),
        ('Zalo', 'Hải', 'Ông xem số này: cho vay tăng 17,4%, tiền gửi chỉ 13,6%', X_)]),
      say=("Cúp máy, Hải gửi ngay cho anh Tuấn một bài báo. Cuối tháng mười, VietnamFinance đưa tin nhiều ngân hàng có thể cạn hạn mức tín dụng sau quy định mới của Ngân hàng Nhà nước. "
           "Kèm theo là một dòng tin nhắn: ông xem số này, cho vay tăng mười bảy phẩy bốn phần trăm, tiền gửi chỉ tăng mười ba phẩy sáu phần trăm.")),
 dict(k='cards', anh='ov:bank counter customers||bank interior', cap=('CHO VAY VƯỢT TIỀN GỬI', 'TỶ ĐỒNG – EM TỰ TÍNH'), cols=CR, moc=True,
      cards=[('1.495.911', 'Tháng 8/2025', 'dư nợ trừ tổng tiền gửi'), ('2.717.982', 'Tháng 8/2026', 'gấp 1,8 lần sau 1 năm'), ('+13,6%', 'Tổng tiền gửi tăng', 'dư nợ +17,4%')],
      say=("Hải nói đúng. Em lấy tổng dư nợ trừ đi tổng tiền gửi trong hệ thống ngân hàng. Tháng tám năm 2025, phần cho vay vượt tiền gửi khoảng một phẩy năm triệu tỷ đồng. Tháng tám năm 2026, con số này là khoảng hai phẩy bảy hai triệu tỷ, gấp một phẩy tám lần chỉ sau một năm. "
           "Khi tiền cho vay lớn nhanh hơn tiền gửi, ngân hàng phải đi tìm nguồn vốn khác, thường là đắt hơn.")),
 dict(k='giay', cap=('SỔ TIẾT KIỆM CỦA MẸ', 'LÃI THẬT CÒN BAO NHIÊU?'), cols=CC, moc=True, giay=dict(tieu_de='SỔ TIẾT KIỆM – KỲ HẠN 12 THÁNG', so='Phép tính anh Tuấn ghi bên lề', dau='ĐÃ TÍNH', dieu=[
        ('Lãi suất 12 tháng, nhóm ngân hàng Nhà nước: 5,4%/năm', '5,4%'),
        ('Lạm phát tháng 10/2026 so với cùng kỳ: 5,09%', '5,09%'),
        ('Lãi thật sau lạm phát: khoảng 0,3 điểm %', 'GẦN ĐỨNG YÊN')]),
      say=("Còn sổ tiết kiệm của mẹ anh Tuấn thì sao? Lãi suất mười hai tháng ở nhóm ngân hàng thương mại Nhà nước hôm nay là năm phẩy bốn phần trăm một năm. Lạm phát tháng mười so với cùng kỳ là năm phẩy không chín phần trăm. "
           "Trừ đi, lãi thật chỉ còn khoảng không phẩy ba điểm phần trăm. Gửi tiền không lỗ, nhưng gần như đứng yên. Và chính vì tiền gửi kém hấp dẫn, ngân hàng càng khó huy động, áp lực lại dồn sang phía người đi vay.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='cards', ch='Chương 5 – Lịch sử từng lặp lại', anh='ov:old banknotes inflation||money inflation', cap=('VIỆT NAM 2007 – 2008', 'KHI TIỀN VAY CHẠY QUÁ NHANH'), cols=CR, moc=True,
      cards=[('+53,89%', 'Tín dụng năm 2007', 'Ngân hàng Nhà nước'), ('22,97%', 'Lạm phát bình quân 2008', 'Tổng cục Thống kê')],
      say=("Chuyện tiền vay chạy nhanh hơn nền kinh tế, Việt Nam đã trải qua. Năm 2007, tín dụng tăng năm mươi ba phẩy tám chín phần trăm. Một năm sau, lạm phát bình quân năm 2008 lên hai mươi hai phẩy chín bảy phần trăm. "
           "Ngân hàng Nhà nước buộc phải siết mạnh, lãi suất cho vay có lúc vượt hai mươi phần trăm một năm. Những người vay lãi thả nổi để mua nhà, mua đất lúc đó là những người chịu trận đầu tiên.")),
 dict(k='text', cap=('BÂY GIỜ KHÔNG PHẢI 2008', 'NHƯNG BÀI HỌC VẪN CÒN'), cols=CC, anh='ov:stock chart monitor||candlestick chart',
      say=("Em nói công bằng: hôm nay không giống năm 2008. Tín dụng tăng mười bảy phần trăm chứ không phải năm mươi ba phần trăm, lạm phát khoảng năm phần trăm chứ không phải hai mươi ba. "
           "Nhưng bài học vẫn nguyên giá trị: khi tiền vay lớn nhanh hơn thu nhập nhiều năm liền, người trả giá thường không phải Nhà nước, mà là người vay với lãi suất thả nổi.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='bars', ch='Chương 6 – Bài toán trong căn hộ', anh=NGAN, cap=('VAY 1,2 TỶ, 20 NĂM', 'TRIỆU ĐỒNG MỖI THÁNG'), cols=CR, moc=True,
      bars=[('8%', 10.04, GOLD, '10,04'), ('10%', 11.58, RED, '11,58'), ('11%', 12.39, RED, '12,39')],
      say=("Anh Tuấn ngồi tính lại khoản vay của mình. Vay một phẩy hai tỷ, trả đều trong hai mươi năm. Lãi tám phần trăm, mỗi tháng trả khoảng mười phẩy không bốn triệu đồng. "
           "Nếu lãi lên mười phần trăm, con số thành mười một phẩy năm tám triệu mỗi tháng. Lên mười một phần trăm là mười hai phẩy ba chín triệu mỗi tháng.")),
 dict(k='cards', anh=NGAN, cap=('CHỈ 2 ĐIỂM % LÃI SUẤT', 'CÁI GIÁ CỦA DÒNG CHỮ NHỎ'), cols=CR, moc=True,
      cards=[('1,54 triệu', 'Trả thêm mỗi tháng', 'lãi từ 8% lên 10%'), ('371 triệu', 'Trả thêm sau 20 năm', 'em tự tính'), ('9,18 triệu', 'Thu nhập bình quân lao động', 'mỗi tháng, quý 3/2026')],
      say=("Chỉ hai điểm phần trăm lãi suất thôi, anh Tuấn trả thêm khoảng một phẩy năm tư triệu đồng mỗi tháng, gần mười tám phẩy năm triệu mỗi năm. Cộng cả hai mươi năm là thêm khoảng ba trăm bảy mươi mốt triệu đồng. "
           "Để dễ hình dung, thu nhập bình quân của người lao động quý ba năm nay là chín phẩy một tám triệu đồng mỗi tháng. Một phẩy năm tư triệu là gần một phần sáu số đó.")),
 dict(k='chat', cap=('PHƯƠNG ÁN KHÁC', 'HAI VỢ CHỒNG TỰ VẠCH RA'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='00:40', mau=G_, msgs=[
        ('me', 'Mình trả bớt 200 triệu gốc trước khi hết ưu đãi nhé'),
        ('me', 'Còn 1 tỷ thì lãi 10% cũng chỉ 9,65 triệu mỗi tháng'),
        ('Vợ', 'Ừ, nhưng phải giữ lại đủ 6 tháng tiền trả nợ đấy'),
        ('me', 'Và tổng trả nợ không quá 40% lương hai đứa')]),
      say=("Anh Tuấn không hoảng như mẹ. Anh nhắn cho vợ một phương án khác. Một: dồn khoản tiết kiệm trả bớt hai trăm triệu nợ gốc trước khi hết ưu đãi. Vay còn một tỷ, kể cả lãi mười phần trăm cũng chỉ trả khoảng chín phẩy sáu lăm triệu mỗi tháng, thấp hơn mức hiện tại. "
           "Hai: giữ tổng tiền trả nợ không quá bốn mươi phần trăm thu nhập cả nhà. Ba, vợ anh nhắc thêm: luôn để sẵn quỹ dự phòng đủ sáu tháng trả nợ, thay vì rút hết đi mua vàng theo lời đồn. Đây là cách anh Tuấn tự tính cho nhà mình, không phải lời khuyên chung cho mọi người.")),
 # ---------------- CHƯƠNG 7 ----------------
 dict(k='checklist', ch='Chương 7 – Nhà đầu tư đọc con số này thế nào?', anh='ov:stock chart monitor||candlestick chart', cap=('3 CÂU HỎI', 'KHI NGHE "VIỆT NAM NỢ NHIỀU"'), cols=CC, moc=True,
      items=[('Nợ của ai: Nhà nước, doanh nghiệp hay hộ gia đình?', GREEN),
             ('Doanh nghiệp mình nắm giữ vay nhiều không, lãi vay ăn mất bao nhiêu lợi nhuận?', GREEN),
             ('Cho vay chạy nhanh hơn tiền gửi: lãi suất 6–12 tháng tới sẽ đi đâu?', GOLD)],
      say=("Với nhà đầu tư chứng khoán, em gợi ý ba câu hỏi mỗi khi nghe ai đó nói Việt Nam nợ nhiều. Một: nợ của ai, Nhà nước, doanh nghiệp hay hộ gia đình? Mỗi loại có rủi ro rất khác nhau. "
           "Hai: doanh nghiệp mình đang nắm giữ vay nhiều không, và chi phí lãi vay đang ăn mất bao nhiêu phần lợi nhuận? Ba: khi cho vay chạy nhanh hơn tiền gửi, lãi suất sáu đến mười hai tháng tới sẽ đi về đâu? "
           "Anh chị có thể tra nợ vay, chi phí lãi vay và lợi nhuận từng quý của hơn bốn trăm mã miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn lúc 1 giờ sáng', cap=('"MẸ ĐỪNG RÚT TIỀN', 'NHÀ MÌNH CẦN XEM LẠI KHOẢN VAY"'), cols=CC, moc=True, chat=dict(ten='Mẹ', tv='Đang hoạt động', gio='01:05', mau=X_, msgs=[
        ('me', 'Mẹ đừng rút sổ tiết kiệm nhé, nước mình chưa vỡ nợ đâu'),
        ('me', 'Cái con lo là khoản vay nhà mình'),
        ('Mẹ', 'Vậy mẹ để sổ đó, khi nào con cần thì lấy trả bớt nợ')]),
      say=("Một giờ sáng, anh Tuấn nhắn cho mẹ: mẹ đừng rút sổ tiết kiệm nhé, nước mình chưa vỡ nợ đâu. Cái con lo là khoản vay nhà mình. "
           "Một lúc sau mẹ trả lời: vậy mẹ cứ để sổ đó, khi nào con cần thì lấy trả bớt nợ. Đôi khi câu hỏi đáng sợ nhất không phải đất nước nợ bao nhiêu, mà là gia đình mình nợ bao nhiêu.")),
 dict(k='end', cap=('NẾU LÃI VAY LÊN 11%', 'ANH CHỊ SẼ LÀM GÌ?'), cols=CC,
      say=("Còn anh chị, nếu lãi vay nhà mình lên mười một phần trăm, anh chị sẽ trả bớt nợ, bán bớt tài sản, hay cứ giữ nguyên? Kể cho em và mọi người ở phần bình luận nhé. "
           "Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Việt Nam Đang Nợ Bao Nhiêu? Nợ Công Chỉ 33% GDP, Nhưng Khoản Vay 146% GDP Mới Chạm Vào Túi Anh Chị'
MT = ("Nợ công Việt Nam năm 2025 chỉ khoảng 33% GDP và đang giảm. Nhưng tổng dư nợ cho vay của nền kinh tế đã khoảng 20,5 triệu tỷ đồng, bằng 146% GDP, gấp 4,8 lần nợ công, và tăng nhanh hơn cả thu nhập lẫn tiền gửi. "
      "Câu chuyện của một gia đình: người mẹ sợ nước vỡ nợ, người con đang vay 1,2 tỷ mua nhà với lãi suất thả nổi.\n\n"
      "Nguồn số liệu (Bộ Tài chính, NHNN, Tổng cục Thống kê – tổng hợp WiData):\n"
      "• Nợ Chính phủ 2025: 4.072.002 tỷ đồng; nợ Chính phủ bảo lãnh: 202.105 tỷ; GDP danh nghĩa 2025: 12.847.571 tỷ → nợ công 33,3% GDP (tự tính); 2018: 45,7% GDP (tự tính)\n"
      "• Nợ nước ngoài quốc gia 2025: 3.286.569 tỷ đồng (25,6% GDP, tự tính); dân số 2025: 102,3 triệu người\n"
      "• Tổng dư nợ tín dụng 8/2026: 20.489.434 tỷ đồng (+17,4% so cùng kỳ); khoảng 793 tỷ USD theo tỷ giá 25.840 (11/11/2026)\n"
      "• Dư nợ / GDP 4 quý (tự tính): 2016 97,6% · 2020 114,3% · 2022 123,9% · 2024 135,7% · 2025 144,7% · 8/2026 145,8%\n"
      "• Tín dụng 'các hoạt động dịch vụ khác' (phần lớn kinh doanh bất động sản và tiêu dùng) 8/2026: 9.238.445 tỷ (45% tổng dư nợ), +24,4% so 8/2025\n"
      "• Dư nợ trừ tổng tiền gửi (tự tính): 8/2025 1.495.911 tỷ → 8/2026 2.717.982 tỷ; tổng tiền gửi +13,6% so cùng kỳ\n"
      "• Lãi suất huy động 12 tháng NHTM Nhà nước 11/11/2026: 5,4%; CPI 10/2026: +5,09%; thu nhập bình quân lao động Q3/2026: 9,18 triệu đồng mỗi tháng\n"
      "• Năm 2007 tín dụng tăng 53,89% (NHNN); lạm phát bình quân 2008: 22,97% (TCTK)\n"
      "• Tin: VietnamFinance 29/10/2026 – nhiều ngân hàng có thể cạn room tín dụng; VnEconomy 2/11/2026 – nợ công/GDP của Mỹ cao nhất 80 năm\n"
      "• Khoản vay minh hoạ (tự tính, trả đều 240 tháng): 1,2 tỷ lãi 8% = 10,04 triệu mỗi tháng; 10% = 11,58 triệu; 11% = 12,39 triệu\n\n"
      "Tra nợ vay, chi phí lãi vay, lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật anh Tuấn, mẹ anh và bạn Hải là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-14', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['nợ công Việt Nam', 'Việt Nam nợ bao nhiêu', 'tín dụng', 'lãi suất vay mua nhà', 'kinh tế Việt Nam', 'nợ công', 'vĩ mô', 'lãi suất thả nổi', 'tín dụng bất động sản'],
    bia_hook=['NỢ 146% GDP', 'AI ĐANG VAY?'], badge='NỢ CÔNG CHỈ 33% GDP',
    bia_anh='ov:bank vault money||banknotes stack',
    bia_hook_b=['VAY 793 TỶ USD', 'ĐI ĐÂU HẾT?'], badge_b='CÂU HỎI LỚN',
    bia_hook_c=['NỢ CÔNG 33%', 'SAO VẪN LO?'], badge_c='THÁNG 8/2026',
    reel_hook='VIỆT NAM NỢ BAO NHIÊU|NỢ THẬT NẰM Ở ĐÂU???',
    fb_post=("Việt Nam đang nợ bao nhiêu? 💸\n\n👉 Nợ công chỉ khoảng 33% GDP và đang giảm\n👉 Nhưng dư nợ cho vay cả nền kinh tế đã 146% GDP, gấp 4,8 lần nợ công\n"
             "👉 Cho vay tăng 17,4%, tiền gửi chỉ 13,6%\n\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: Việt Nam đang nợ bao nhiêu (NV1 12/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
