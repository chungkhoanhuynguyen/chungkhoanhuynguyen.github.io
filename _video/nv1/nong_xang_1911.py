# -*- coding: utf-8 -*-
# NV1B 19/11/2026 – VIDEO NÓNG kênh chính: giá xăng giảm hơn 1/3 từ đỉnh, nhưng giá cả chung vẫn tăng 5% (kỳ điều hành xăng dầu 19/11).
# Lý do chọn: tin "tiền trong túi" của 24h – kỳ điều hành giá xăng chiều 19/11 (Ngôi Sao 18/11 dự báo), thuế TTĐB xăng 0% (Báo Hải Phòng 18/11),
#   kỳ vọng lạm phát của các ngân hàng (NHNN khảo sát, Người Quan Sát 18/11). Fed/USD và vàng đã có CH2111FED, CH2211VANG → tránh.
#   Không trùng 7 ngày: NONG1611A margin, NONG1711A SCB, NONG1811A thanh khoản; CH2011VON (vốn – lãi thật) khác góc (đây là giá xăng – rổ hàng – chi tiêu).
#   WiData hết credit tới 00:00 20/11 → nguồn báo, ghi tên báo + ngày cho từng số.
# Nguồn:
#  - Ngôi Sao 18/11/2026: kỳ điều hành 15:00 ngày 12/11: E5 RON92 19.399 đ/lít (giảm 1.499), E10 RON95-III 19.845 (giảm 1.311), diesel 26.822;
#    từ đầu tháng 11: E5 giảm 6.628 đ/lít, E10 giảm gần 5.900; đỉnh E5 30.114 (tháng 3), giảm 10.715 (khoảng 35,6%); E10 đỉnh 31.420 ngày 24/3, giảm 11.575;
#    diesel đỉnh 44.788 ngày 3/4; kỳ điều hành tiếp theo 19/11. Brent 17/11: 93,14 USD/thùng.
#  - VietnamPlus 31/10/2026: NQ 45/2026/NQ-CP thuế TTĐB xăng 0% từ 1/11/2026 đến hết 31/3/2027; E5 còn 24.223 (giảm 1.804), E10 24.159 (giảm 1.575).
#  - Báo Hải Phòng 18/11/2026: NQ 45/2026/NQ-CP ngày 31/10/2026; thuế 0% không có nghĩa miễn mọi thuế, phí khác.
#  - Báo Đầu tư 4/11/2026 (Thứ trưởng Bộ Tài chính, họp báo Chính phủ tháng 10): giảm thu gần 7.000 tỷ; giá điện bình quân giảm 2% từ 1/11/2026;
#    CPI bình quân 10 tháng +4,57%; mục tiêu khoảng 4,5%; hai biện pháp làm CPI bình quân năm giảm khoảng 0,08 điểm %; quyền số tổng 9,34%.
#  - Nhân Dân 3/11/2026 (Cục Thống kê): CPI tháng 10 +0,20% so tháng trước, +5,09% so cùng kỳ; bình quân 10 tháng +4,57%; lạm phát cơ bản tháng 10 +4,04% so cùng kỳ, bình quân 10 tháng +4,24%;
#    xăng tăng 6,86% trong tháng 10.
#  - Người Quan Sát 18/11/2026: khảo sát NHNN (Vụ Dự báo thống kê, 1–9/11): các TCTD kỳ vọng CPI tháng 11 +0,34% so tháng 10; bình quân 2026 +4,49%; 2027 +4,23%.
#  - VnEconomy 7/3/2026: giá dầu tăng do xung đột Mỹ – Israel – Iran, Iran phong toả eo biển Hormuz. Doanh nghiệp Hội nhập 30/3/2026: Brent vượt 115 USD.
#  - VnExpress 12/12/2022: RON95 21.200 đ/lít, thấp hơn gần 36% so với đỉnh 32.870 tháng 6/2022. Tuổi Trẻ 29/12/2022 (Tổng cục Thống kê): CPI 2022 bình quân +3,15%; tháng 12/2022 +4,55% so cùng kỳ; 34 lần điều chỉnh giá xăng.
#  - Báo Quốc tế 19/11/2026: đồng USD cao nhất 19 tháng ngày 18/11.
# SỐ TỰ TÍNH: 30.114 − 19.399 = 10.715 (35,6%). 32.870 − 21.200 = 11.670 → 35,5%. 31.420 − 19.845 = 11.575 → 36,8%.
#   Nhân vật (GIẢ ĐỊNH): anh Thắng giao hàng đổ 65 lít mỗi tháng (2,5 lít × 26 ngày). Tháng 3: 65 × 30.114 = 1.957.410 ("gần 2 triệu"); nay 65 × 19.399 = 1.260.935 ("khoảng 1,26 triệu");
#   chênh 696.475 ("gần 700 nghìn"). Tiền chợ 6 triệu mỗi tháng × 5,09% = 305.400 ("hơn 300 nghìn").
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261119_0815_nong'
KEY = 'NONG1911A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
CHO = 'ov:Ben Thanh Market||Ben Thanh Market'
MET = 'ov:Ho Chi Minh City Metro Line 1||Ho Chi Minh City Metro Line 1'
NHA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('XĂNG E5 TỪ 30.114 ĐỒNG', 'CÒN 19.399 ĐỒNG'), cols=CC, noti=dict(gio='07:30', ngay='Thứ Năm', items=[
        ('Tin tức', 'Giá xăng', 'Chiều nay giá xăng điều chỉnh kỳ mới', V_),
        ('Vợ', 'Tin nhắn', 'Xăng rẻ vậy sao đi chợ vẫn đắt anh?', X_)]),
      say=("Bảy giờ rưỡi sáng nay, anh Thắng, người chạy giao hàng ở Thành phố Hồ Chí Minh, đổ đầy bình xăng. Một lít xăng E5 giờ chỉ còn hơn mười chín nghìn ba trăm đồng. "
           "Tháng ba năm nay, cùng lít xăng đó có lúc lên tới hơn ba mươi nghìn. Chiều nay giá xăng lại điều chỉnh kỳ mới. "
           "Nhưng tin nhắn của vợ anh mới là câu hỏi đáng nghĩ: xăng rẻ vậy, sao đi chợ vẫn đắt hả anh?")),
 dict(k='bignum', anh=TP, cap=('XĂNG E5 RẺ ĐI', 'GẦN 36% TỪ ĐỈNH'), cols=CC, value=10715, fmt='{:,.0f}', unit=' đồng', top='XĂNG E5 RẺ HƠN MỖI LÍT, SO VỚI ĐỈNH THÁNG 3', sub='Từ 30.114 còn 19.399 đồng (kỳ 12/11/2026)', col=GOLD,
      say=("Theo báo Ngôi Sao, từ đỉnh tháng ba đến kỳ điều hành tuần trước, mỗi lít xăng E5 đã rẻ đi mười nghìn bảy trăm mười lăm đồng, tức gần ba mươi sáu phần trăm. "
           "Vậy mà theo Cục Thống kê, giá cả nói chung tháng mười vẫn cao hơn năm ngoái năm phần trăm. Tiền xăng rẻ đi đâu? Ai thật sự được lợi? Và lúc nào xăng có thể đắt lại?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Giá xăng năm 2026', cap=('GIÁ XĂNG E5 NĂM 2026', 'TỪ ĐỈNH VỀ ĐẾN HÔM NAY'), cols=CC, moc=True, giay=dict(tieu_de='GIÁ XĂNG E5 MỖI LÍT', so='Theo VietnamPlus 31/10, Ngôi Sao 18/11/2026', dau='ĐÃ ĐỌC', dieu=[
        ('Tháng 3/2026, lúc cao nhất: 30.114 đồng.', 'ĐỈNH'),
        ('Trước ngày 1/11: khoảng 26.000 đồng.', 'VẪN CAO'),
        ('Ngày 1/11, thuế về 0%: 24.223 đồng.', 'GIẢM 1.804'),
        ('Kỳ 12/11: 19.399 đồng.', 'GIẢM 6.628')]),
      say=("Anh Thắng ghi lại đường đi của lít xăng. Tháng ba, khi xung đột quanh Iran làm eo biển Hormuz bị phong toả, xăng E5 lên hơn ba mươi nghìn đồng. "
           "Cuối tháng mười vẫn còn khoảng hai mươi sáu nghìn. Ngày một tháng mười một, thuế tiêu thụ đặc biệt với xăng về không phần trăm, giá giảm một nghìn tám trăm linh bốn đồng. "
           "Rồi đến kỳ điều hành tuần trước, chỉ còn mười chín nghìn ba trăm chín mươi chín đồng. Chỉ trong nửa tháng, mỗi lít rẻ đi hơn sáu nghìn sáu trăm đồng.")),
 dict(k='chat', cap=('"XĂNG GIẢM RỒI', 'SAO RAU THỊT CHƯA GIẢM?"'), cols=CR, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='08:05', mau=X_, msgs=[
        ('Vợ', 'Xăng giảm cả tháng nay rồi'),
        ('Vợ', 'Mà rau, thịt, tiền gửi xe vẫn y nguyên'),
        ('me', 'Để anh tìm hiểu xem sao')]),
      say=("Chị Mai, vợ anh, bán cơm văn phòng. Chị nhắn tiếp: xăng giảm cả tháng nay rồi, mà rau, thịt, tiền gửi xe vẫn y nguyên. "
           "Anh Thắng trả lời: để anh tìm hiểu xem sao. Và con số đầu tiên anh tìm được làm anh bất ngờ.")),
 dict(k='bignum', anh=CHO, cap=('GIÁ CẢ THÁNG 10', 'VẪN CAO HƠN NĂM NGOÁI 5,09%'), cols=CR, moc=True, value=5.09, fmt='{:,.2f}', unit='%', top='CPI THÁNG 10/2026 SO VỚI CÙNG KỲ', sub='Theo Cục Thống kê, công bố 3/11/2026', col=RED,
      say=("Theo Cục Thống kê, chỉ số giá tiêu dùng tháng mười cao hơn cùng kỳ năm ngoái khoảng năm phẩy một phần trăm. "
           "Tính bình quân mười tháng, giá cả tăng gần bốn phẩy sáu phần trăm, đã vượt mức mục tiêu khoảng bốn phẩy năm phần trăm cho cả năm. Xăng rẻ đi, nhưng mặt bằng giá chưa hề lùi.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Vì sao xăng rẻ mà chợ không rẻ?', anh=CHO, cap=('BỎ XĂNG RA', 'GIÁ CẢ VẪN TĂNG HƠN 4%'), cols=CC, moc=True,
      cards=[('4,24%', 'Lạm phát cơ bản 10 tháng', 'BỎ XĂNG, RAU THỊT TƯƠI'), ('4,57%', 'CPI bình quân 10 tháng', 'VƯỢT MỤC TIÊU 4,5%'), ('0,34%', 'Ngân hàng dự báo CPI tháng 11', 'VẪN TĂNG')],
      say=("Có một con số giúp anh Thắng hiểu ra. Đó là lạm phát cơ bản, tức là giá cả sau khi đã bỏ xăng dầu, lương thực và thực phẩm tươi sống ra. Bình quân mười tháng, con số này vẫn tăng hơn bốn phẩy hai phần trăm. "
           "Nghĩa là những thứ không dính tới xăng vẫn đang lên giá đều đặn. Ngân hàng Nhà nước vừa công bố khảo sát hôm qua. Các ngân hàng vẫn dự báo giá cả tháng mười một tăng thêm khoảng không phẩy ba phần trăm so với tháng mười, dù xăng và điện đều giảm.")),
 dict(k='noti', cap=('THUẾ XĂNG VỀ 0%', 'CHỈ ĐẾN HẾT 31/3/2027'), cols=CC, moc=True, noti=dict(gio='09:20', ngay='Thứ Năm', items=[
        ('Tin tức', 'Chính sách', 'Thuế tiêu thụ đặc biệt với xăng 0% đến hết 31/3/2027', V_),
        ('Tin tức', 'Chính sách', 'Giá điện bình quân giảm 2% từ ngày 1/11', G_)]),
      say=("Anh Thắng đọc tiếp tin chính sách. Theo Nghị quyết bốn mươi lăm của Chính phủ, thuế tiêu thụ đặc biệt với xăng về không phần trăm từ ngày một tháng mười một. Nhưng mức thuế này chỉ áp dụng đến hết ngày ba mươi mốt tháng ba năm 2027. "
           "Ngân sách giảm thu gần bảy nghìn tỷ đồng. Cùng ngày, giá điện bình quân cũng giảm hai phần trăm.")),
 dict(k='bignum', anh=TP, cap=('2 BIỆN PHÁP', 'KÉO CPI CẢ NĂM XUỐNG 0,08 ĐIỂM'), cols=CC, moc=True, value=0.08, fmt='{:,.2f}', unit=' điểm %', top='TÁC ĐỘNG LÊN CPI BÌNH QUÂN NĂM 2026', sub='Ước tính của Bộ Tài chính (Báo Đầu tư 4/11/2026)', col=GOLD,
      say=("Và đây là cú lật. Theo ước tính của Bộ Tài chính, cả hai biện pháp, xăng và điện, chỉ kéo chỉ số giá bình quân năm nay xuống chưa đến không phẩy một điểm phần trăm. "
           "Vì sao ít vậy? Vì trong rổ hàng tính giá, điện và xăng dầu cộng lại chỉ chiếm hơn chín phần trăm. Hơn chín mươi phần trăm còn lại là ăn uống, nhà ở, học hành, thuốc men, và những thứ đó không giảm theo xăng.")),
 dict(k='chat', cap=('"GIÁ LÊN THÌ NHANH', 'GIÁ XUỐNG THÌ CHẬM"'), cols=CC, moc=True, chat=dict(ten='Chị Mai', tv='Đang hoạt động', gio='11:15', mau=X_, msgs=[
        ('Chị Mai', 'Tháng ba xăng lên, rau thịt lên theo liền'),
        ('Chị Mai', 'Giờ xăng xuống, chưa mối nào hạ giá cho em'),
        ('me', 'Vậy suất cơm em có hạ không?')]),
      say=("Chị Mai kể thêm từ phía người bán. Tháng ba, xăng vừa lên là mối rau, mối thịt báo tăng giá ngay. Giờ xăng xuống cả tháng, chưa mối nào hạ giá cho chị. "
           "Anh Thắng hỏi lại: vậy suất cơm của em có hạ không? Chị trả lời rằng chị cũng chưa hạ, vì tiền chợ chưa giảm đồng nào.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước là năm 2022', cap=('"NĂM 2022 XĂNG CŨNG', 'GIẢM MỘT MẠCH"'), cols=CC, moc=True, call=dict(ten='Bố', phu='Chạy xe ôm 20 năm', mau=V_, loi=[
        'Năm 2022 xăng gần 33 nghìn', 'Cuối năm còn hơn 21 nghìn']),
      say=("Trưa đó anh Thắng gọi cho bố, người chạy xe ôm hơn hai mươi năm. Bố kể: năm 2022 cũng y như vậy. Giữa năm xăng gần ba mươi ba nghìn một lít, ai cũng than. "
           "Cuối năm giảm một mạch xuống hơn hai mươi mốt nghìn. Nhưng bát phở đầu ngõ thì không quay về giá cũ.")),
 dict(k='giay', cap=('NĂM 2022', 'NHỮNG CON SỐ CỦA LẦN TRƯỚC'), cols=CC, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='Theo VnExpress 12/12/2022, Tuổi Trẻ 29/12/2022', dau='SO SÁNH', dieu=[
        ('Xăng RON95 tháng 6/2022: 32.870 đồng.', 'ĐỈNH'),
        ('Ngày 12/12/2022: 21.200 đồng.', 'RẺ GẦN 36%'),
        ('CPI tháng 12/2022 so cùng kỳ: 4,55%.', 'VẪN TĂNG'),
        ('CPI bình quân năm 2022: 3,15%.', 'THẤP HƠN')]),
      say=("Những con số của lần trước. Tháng sáu năm 2022, theo VnExpress, xăng RON95 lên đỉnh ba mươi hai nghìn tám trăm bảy mươi đồng. Đến giữa tháng mười hai, chỉ còn hai mươi mốt nghìn hai trăm, rẻ đi gần ba mươi sáu phần trăm. "
           "Thế nhưng theo Tổng cục Thống kê, giá cả tháng mười hai năm 2022 vẫn cao hơn cùng kỳ khoảng bốn phẩy sáu phần trăm. Cao hơn hẳn mức bình quân chỉ hơn ba phần trăm của cả năm. Xăng xuống nửa năm trời, giá cả chung vẫn đi lên.")),
 dict(k='bars', anh=TP, cap=('XĂNG RON95 RẺ ĐI TỪ ĐỈNH', 'LẦN TRƯỚC VÀ LẦN NÀY'), cols=CC, moc=True,
      bars=[('Năm 2022', 35.5, GOLD, '35,5%'), ('Năm 2026', 36.8, GREEN, '36,8%')],
      say=("Đặt hai lần cạnh nhau, giống đến bất ngờ. Năm 2022, xăng RON95 rẻ đi khoảng ba mươi lăm phẩy năm phần trăm từ đỉnh. "
           "Năm nay, xăng RON95 loại E10 lên đỉnh ba mươi mốt nghìn bốn trăm hai mươi đồng ngày hai mươi tư tháng ba. Kỳ tuần trước còn mười chín nghìn tám trăm bốn mươi lăm đồng, rẻ đi khoảng ba mươi sáu phẩy tám phần trăm.")),
 dict(k='checklist', anh=HN, cap=('GIỐNG 2, KHÁC 2', 'SO VỚI NĂM 2022'), cols=CC, moc=True,
      items=[('Giống: xăng rẻ đi hơn 35%', GOLD), ('Giống: giá cả chung vẫn tăng', RED), ('Khác: nhờ thuế 0% có hạn', RED), ('Khác: đô la cao nhất 19 tháng', RED)],
      say=("So với năm 2022, có hai điểm giống và hai điểm khác. Giống ở chỗ xăng rẻ đi hơn ba mươi lăm phần trăm từ đỉnh, và giá cả chung vẫn tăng. "
           "Khác ở chỗ lần này giá xăng còn được đỡ bởi thuế tiêu thụ đặc biệt về không, mà mức thuế đó có ngày hết hạn. Và theo Báo Quốc tế, đồng đô la vừa lên cao nhất mười chín tháng, trong khi dầu mua bằng đô la. "
           "Giá dầu Brent hôm mười bảy tháng mười một vẫn quanh chín mươi ba đô la một thùng. Xăng rẻ hôm nay không có nghĩa là sẽ rẻ mãi.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='giay', ch='Chương 4 – Sổ chi tiêu nhà anh Thắng', cap=('TIỀN XĂNG RẺ ĐI GẦN 700 NGHÌN', 'TIỀN CHỢ ĐẮT THÊM HƠN 300 NGHÌN'), cols=CR, moc=True, giay=dict(tieu_de='SỔ CHI TIÊU MỖI THÁNG', so='Số giả định để minh hoạ', dau='GIẢ ĐỊNH', dieu=[
        ('Đổ 65 lít xăng E5 mỗi tháng.', '65 LÍT'),
        ('Tháng 3: gần 2 triệu tiền xăng.', 'GẦN 2 TRIỆU'),
        ('Bây giờ: khoảng 1,26 triệu.', 'BỚT GẦN 700 NGHÌN'),
        ('Tiền chợ 6 triệu, tăng 5,09%.', 'THÊM HƠN 300 NGHÌN')]),
      say=("Tối đó anh Thắng mở sổ chi tiêu. Em giả định để minh hoạ: anh chạy giao hàng, mỗi tháng đổ khoảng sáu mươi lăm lít xăng E5. "
           "Tháng ba, tiền xăng gần hai triệu đồng. Bây giờ còn khoảng một triệu hai trăm sáu mươi nghìn, bớt gần bảy trăm nghìn đồng mỗi tháng. "
           "Nhưng tiền chợ của nhà anh khoảng sáu triệu mỗi tháng, nếu đắt hơn năm ngoái năm phần trăm, là thêm hơn ba trăm nghìn. Phần lợi từ xăng đã bị chợ lấy lại gần một nửa.")),
 dict(k='chat', cap=('"THÁNG NÀY DƯ TIỀN', 'SAO KHÔNG THẤY ĐÂU?"'), cols=CR, moc=True, chat=dict(ten='Chị Mai', tv='Đang hoạt động', gio='21:00', mau=X_, msgs=[
        ('Chị Mai', 'Tháng này đáng lẽ dư tiền xăng'),
        ('Chị Mai', 'Mà cuối tháng em không thấy đồng nào'),
        ('me', 'Tại nó tan vào chi tiêu hết rồi')]),
      say=("Chị Mai nhắn: tháng này đáng lẽ nhà mình dư tiền xăng, mà cuối tháng em không thấy đồng nào. "
           "Anh Thắng trả lời: tại nó tan vào chi tiêu hằng ngày hết rồi. Tiền rẻ ra từng lít một, ít ai để ý, nên cũng ít ai giữ lại được.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='cards', ch='Chương 5 – Ba cách dùng tiền xăng rẻ', anh=NHA, cap=('3 CÁCH DÙNG', 'TIỀN XĂNG RẺ ĐI MỖI THÁNG'), cols=CC, moc=True,
      cards=[('Tiêu luôn', 'Để tan vào chi tiêu', 'KHÔNG THẤY ĐÂU'), ('Để riêng một nửa', 'Khoảng 350 nghìn mỗi tháng', 'CÓ QUỸ NHỎ'), ('Để riêng hết', 'Khoảng 700 nghìn mỗi tháng', 'SẴN SÀNG THÁNG 4/2027')],
      say=("Anh Thắng thấy có ba cách. Một, cứ để tiền xăng rẻ tan vào chi tiêu như tháng này. Hai, mỗi tháng để riêng một nửa, khoảng ba trăm năm mươi nghìn. "
           "Ba, để riêng toàn bộ phần chênh, khoảng bảy trăm nghìn, làm quỹ cho ngày thuế xăng hết hạn hoặc giá dầu quay lại. Không cách nào đúng cho mọi nhà, tuỳ thu nhập và nợ của từng người.")),
 dict(k='chat', cap=('"MỖI LẦN ĐỔ XĂNG', 'ANH CHUYỂN PHẦN CHÊNH"'), cols=CC, moc=True, chat=dict(ten='Chị Mai', tv='Đang hoạt động', gio='21:30', mau=X_, msgs=[
        ('me', 'Mỗi lần đổ xăng anh chuyển phần chênh sang tài khoản riêng'),
        ('me', 'Để dành cho lúc xăng đắt lại'),
        ('Chị Mai', 'Vậy em cũng để riêng tiền điện giảm')]),
      say=("Anh Thắng nhắn vợ kế hoạch. Mỗi lần đổ xăng, anh sẽ chuyển phần chênh so với giá tháng ba sang một tài khoản riêng, để dành cho lúc xăng đắt lại. "
           "Chị Mai trả lời rằng chị cũng sẽ để riêng phần tiền điện được giảm. Đó là lựa chọn của gia đình anh Thắng, không phải lời khuyên chung cho mọi người.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='checklist', ch='Chương 6 – Phép thử cho chi tiêu', anh=HN, cap=('PHÉP THỬ', 'TIỀN XĂNG RẺ ĐI ĐÂU?'), cols=CC, moc=True,
      items=[('Để riêng được toàn bộ', GREEN), ('Để riêng được một nửa', GOLD), ('Tan hết vào chi tiêu', RED)],
      say=("Em gợi ý một phép thử tự soi. Anh chị tính xem mỗi tháng nhà mình đổ bao nhiêu lít xăng, nhân với số tiền rẻ hơn mỗi lít. Rồi hỏi: phần tiền đó đang ở đâu? "
           "Nếu để riêng được toàn bộ, nhà mình đã có quỹ cho lúc xăng đắt lại. Nếu được một nửa, vẫn ổn. Nếu tan hết vào chi tiêu, thì ngày xăng tăng lại, ngân sách sẽ hụt ngay. Đây là mốc tự soi, không phải lời khuyên.")),
 dict(k='checklist', anh=TP, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI THÁNG 4/2027'), cols=CC, moc=True,
      items=[('Giá xăng mỗi thứ Năm', GOLD), ('CPI tháng 11, đầu tháng 12', GOLD), ('Thuế xăng hết hạn 31/3/2027', RED)],
      say=("Ba điều đáng theo dõi. Giá xăng điều chỉnh vào chiều thứ Năm hằng tuần, theo giá dầu và đồng đô la. Chỉ số giá tháng mười một, Cục Thống kê công bố đầu tháng mười hai, xem xăng và điện giảm có kéo được giá cả xuống không. "
           "Và ngày ba mươi mốt tháng ba năm 2027, khi thuế xăng về không phần trăm hết hạn. Muốn hiểu lạm phát ăn vào tiền tiết kiệm thế nào, anh chị có thể đọc bài miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"XĂNG RẺ LÀ TẠM THỜI', 'TIỀN ĐỂ RIÊNG MỚI LÀ CỦA MÌNH"'), cols=CC, moc=True, chat=dict(ten='Bố', tv='Đang hoạt động', gio='22:00', mau=V_, msgs=[
        ('Bố', 'Xăng lên xuống cả đời bố rồi'),
        ('Bố', 'Lúc rẻ thì phải biết để dành'),
        ('me', 'Dạ, xăng rẻ là tạm thời, tiền để riêng mới là của mình')]),
      say=("Mười giờ tối, bố nhắn: xăng lên xuống cả đời bố rồi, lúc rẻ thì phải biết để dành. "
           "Anh Thắng trả lời: dạ, xăng rẻ là tạm thời, tiền để riêng mới là của mình.")),
 dict(k='end', cap=('TIỀN XĂNG RẺ MỖI THÁNG', 'NHÀ ANH CHỊ ĐỂ Ở ĐÂU?'), cols=CC,
      say=("Còn anh chị, mỗi tháng nhà mình tiết kiệm được bao nhiêu từ xăng rẻ, và phần tiền đó đang ở đâu? Kể cho em và mọi người ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Giá Xăng Hôm Nay Rẻ Gần 36% Từ Đỉnh: 30.114 Còn 19.399 Đồng – Sao Đi Chợ Vẫn Đắt Hơn 5%?'
MT = ("NÓNG: giá xăng E5 từ đỉnh 30.114 đồng/lít tháng 3/2026 xuống 19.399 đồng kỳ 12/11 – rẻ đi gần 36%. Thuế tiêu thụ đặc biệt với xăng về 0% từ 1/11 đến hết 31/3/2027, giá điện giảm 2%. "
      "Vậy mà giá cả tháng 10 vẫn cao hơn năm ngoái 5,09%. Vì sao xăng rẻ mà chợ không rẻ, lần trước năm 2022 ra sao, và phép thử cho chi tiêu nhà anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• Ngôi Sao 18/11/2026: kỳ điều hành 15:00 ngày 12/11: E5 RON92 19.399 đ/lít, E10 RON95-III 19.845 đ/lít; từ đầu tháng 11 E5 giảm 6.628 đ/lít; đỉnh E5 30.114 (tháng 3/2026); đỉnh E10 31.420 (24/3/2026); Brent 17/11: 93,14 USD/thùng\n"
      "• VietnamPlus 31/10/2026: Nghị quyết 45/2026/NQ-CP – thuế TTĐB xăng 0% từ 1/11/2026 đến hết 31/3/2027; E5 còn 24.223 đ/lít (giảm 1.804)\n"
      "• Báo Đầu tư 4/11/2026 (họp báo Chính phủ): giảm thu gần 7.000 tỷ; giá điện bình quân giảm 2% từ 1/11; hai biện pháp làm CPI bình quân năm giảm khoảng 0,08 điểm %; quyền số điện và xăng dầu tổng 9,34%; mục tiêu CPI khoảng 4,5%\n"
      "• Nhân Dân 3/11/2026 (Cục Thống kê): CPI tháng 10/2026 +5,09% so cùng kỳ; bình quân 10 tháng +4,57%; lạm phát cơ bản bình quân 10 tháng +4,24%\n"
      "• Người Quan Sát 18/11/2026 (khảo sát kỳ vọng lạm phát của NHNN, 1–9/11): các tổ chức tín dụng kỳ vọng CPI tháng 11 +0,34% so tháng 10; bình quân 2026 +4,49%\n"
      "• VnEconomy 7/3/2026: giá dầu tăng do xung đột Mỹ – Israel – Iran, eo biển Hormuz bị phong toả\n"
      "• Báo Quốc tế 19/11/2026: đồng USD cao nhất 19 tháng (18/11)\n"
      "• VnExpress 12/12/2022: RON95 21.200 đ/lít, thấp hơn gần 36% so với đỉnh 32.870 tháng 6/2022. Tuổi Trẻ 29/12/2022 (Tổng cục Thống kê): CPI tháng 12/2022 +4,55% so cùng kỳ; bình quân 2022 +3,15%\n"
      "• Tự tính: 30.114 − 19.399 = 10.715 đ (35,6%); 32.870 → 21.200 = rẻ 35,5%; 31.420 → 19.845 = rẻ 36,8%. "
      "Sổ chi tiêu anh Thắng là GIẢ ĐỊNH: 65 lít/tháng; tháng 3: 65 × 30.114 ≈ 1,96 triệu; nay 65 × 19.399 ≈ 1,26 triệu; chênh ≈ 696 nghìn; tiền chợ 6 triệu × 5,09% ≈ 305 nghìn\n\n"
      "Lạm phát và tiền tiết kiệm: https://chungkhoanhuynguyen.com/hoc/\n"
      "Cần trao đổi riêng về kế hoạch tài chính: Zalo 0365.188.286\n\n"
      "Nhân vật anh Thắng, chị Mai, bố là hư cấu; số liệu là thật theo nguồn trên.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-19', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['giá xăng hôm nay', 'giá xăng', 'giá xăng E5', 'thuế tiêu thụ đặc biệt xăng', 'lạm phát', 'CPI tháng 10', 'giá cả', 'chi tiêu gia đình', 'tin nóng tài chính', 'giá dầu'],
    bia_hook=['XĂNG RẺ 36%', 'CHỢ VẪN ĐẮT?'], badge='GIÁ XĂNG HÔM NAY',
    bia_anh='Ho Chi Minh City skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['30.114 ĐỒNG', 'CÒN 19.399'], badge_b='XĂNG E5 MỖI LÍT',
    bia_hook_c=['TIỀN XĂNG RẺ', 'ĐI ĐÂU HẾT???'], badge_c='GIÁ CẢ VẪN TĂNG 5,09%',
    reel_hook='XĂNG RẺ GẦN 36%|SAO CHỢ VẪN ĐẮT???',
    fb_post=("Xăng E5 rẻ gần 36% từ đỉnh ⛽\n\n👉 Tháng 3/2026: 30.114 đồng/lít\n👉 Kỳ 12/11: 19.399 đồng/lít\n"
             "👉 Nhưng giá cả tháng 10 vẫn cao hơn năm ngoái 5,09%\n\nTiền xăng rẻ mỗi tháng nhà anh chị để ở đâu?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 19/11: giá xăng rẻ gần 36 phần trăm từ đỉnh, giá cả vẫn tăng (NV1B 19/11/2026).\n"
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
sys.path.insert(0, CW + '/_video')
try:
    import xung_ho
    for i, c in enumerate(S, 1):
        if xung_ho.le_phep(c['say']) != c['say']: print('XUNG_HO doi canh', i)
except Exception as e: print('xung_ho?', e)
