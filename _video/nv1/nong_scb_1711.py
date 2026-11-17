# -*- coding: utf-8 -*-
# NV1B 17/11/2026 – VIDEO NÓNG kênh chính: SCB đưa lãi suất tiết kiệm về 0% từ 16/11/2026.
# Lý do chọn: tin tiền-trong-túi nóng nhất 24h (Dân trí, CafeF, CafeBiz, Kenh14, Vietstock, Người Quan Sát 16/11; Vietstock "Đọc gì" 17/11 nhắc lại);
#   xu_huong.md: "Lãi suất tăng, tiền gửi dịch chuyển" ~67 nghìn view. Khác NONG1311A (lãi vay giảm) – đây là phía tiền gửi + an toàn tiền gửi.
#   WiData hết credit tới 00:00 20/11 → nguồn báo, ghi tên báo + ngày.
# Nguồn:
#  - Dân trí 16/11/2026: từ 16/11 SCB online 0%/năm kỳ hạn 31 ngày, 1, 3, 6, 12, 36 tháng cả 3 cách lĩnh lãi; tiết kiệm thường (cá nhân gửi mới) 0% kỳ hạn 1–36 tháng;
#    12 tháng 3,7% và 13 tháng 8,7% (lãi cuối kỳ, biểu công bố trước đó); online trước đó 0,1–0,7%; lần điều chỉnh mạnh thứ hai trong 1 tháng;
#    kiểm soát đặc biệt từ 2022 sau biến cố liên quan Vạn Thịnh Phát; hạn mức chuyển nhanh tối đa 20 triệu/ngày;
#    ~240 điểm giao dịch (50 CN + 190 PGD) trước kiểm soát đặc biệt → 3/11 còn 8 điểm tại 6 tỉnh, thành;
#    lãi online phổ biến: 3 tháng 4,2–4,75%; 6 tháng 4,15–6,9%; 12 tháng 6–7%.
#  - Người Quan Sát 16/11/2026: 12 và 13 tháng theo biểu 26/10, SCB chưa công bố biểu thay thế; VPBank online <10 tỷ: 6–11 tháng 6,6%; VPBank là ngân hàng thứ 5 giảm lãi huy động hơn 1 lần từ 18/10.
#  - MotTheGioi 16/11/2026: lãi cao nhất SCB trước 2024 8,5–9,5%; 2024 đến trước 10/2026 3,9%; cuối 10/2026 0,7%; từ 16/11 0% (trừ 12–13 tháng); "trường hợp cá biệt", không phải xu hướng chung; 13 tháng 8,7% thường kèm điều kiện.
#  - Vietstock 17/11/2026: lãi tiết kiệm giảm 0,5–2%/năm, huy động qua trái phiếu ngân hàng 8–10%/năm.
#  - VnEconomy 8/10/2022: tin tiêu cực về SCB lan trên mạng 7/10/2022, một số người rút trước hạn; NHNN: quyền lợi người gửi tiền được bảo đảm; rút trước hạn mất lãi.
#  - RFA 15/10/2022 dẫn SCB: ngày 12/10/2022 khách gửi lại gần 6.000 tỷ trong 1 ngày, ngày trước đó hơn 1.600 tỷ.
#  - VietnamPlus 20/7/2026, Báo Đầu tư, Thị trường Tài chính Tiền tệ: Thông tư 05/2026/TT-NHNN – hạn mức chi trả bảo hiểm tiền gửi 350 triệu (cũ 125 triệu, gấp 2,8 lần) từ 13/7/2026, tổng gốc + lãi của 1 người tại 1 tổ chức.
#  - CafeF 22/8/2026: 30/6/2026 NHNN trình Thủ tướng phương án xử lý tài sản thu hồi nợ của SCB.
# SỐ TỰ TÍNH: 200 triệu × 6,6% × 6/12 = 6,6 triệu; × 0,7% × 6/12 = 0,7 triệu; × 3,7% × 12/12 = 7,4 triệu; × 0% = 0.
#   200 triệu ÷ 20 triệu/ngày = 10 ngày chuyển nhanh. 240 ÷ 8 = 30 (cứ 30 điểm cũ còn 1). 350 ÷ 125 = 2,8.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261117_0900_nong'
KEY = 'NONG1711A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
BT = 'ov:Ben Thanh Market||Ben Thanh Market'
NHA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('LÃI SUẤT TIẾT KIỆM 0%', 'TỪ NGÀY 16/11'), cols=CR, noti=dict(gio='07:40', ngay='Thứ Hai', items=[
        ('Tin tức', 'Ngân hàng', 'SCB đưa lãi suất tiết kiệm online về 0% cho các kỳ hạn từ 31 ngày đến 36 tháng', R_),
        ('Con gái', 'Tin nhắn', 'Mẹ ơi, sổ 200 triệu của mẹ ở SCB tuần này đáo hạn đúng không?', X_)]),
      say=("Bảy giờ bốn mươi sáng thứ Hai, cô Hạnh, giáo viên đã nghỉ hưu, đọc được một tin hiếm thấy. Từ ngày mười sáu tháng mười một, ngân hàng SCB đưa lãi suất tiết kiệm online về không phần trăm, cho các kỳ hạn từ ba mươi mốt ngày đến ba mươi sáu tháng. "
           "Một phút sau, con gái nhắn: mẹ ơi, sổ hai trăm triệu của mẹ ở SCB tuần này đáo hạn đúng không?")),
 dict(k='bignum', anh=TP, cap=('GỬI 200 TRIỆU 6 THÁNG', 'NHẬN 0 ĐỒNG TIỀN LÃI'), cols=CR, value=0, fmt='{:,.0f}', unit=' đồng', top='LÃI 200 TRIỆU GỬI 6 THÁNG', sub='Biểu lãi suất SCB từ 16/11/2026', col=RED,
      say=("Nếu cô gửi lại hai trăm triệu, kỳ hạn sáu tháng, theo biểu mới, tiền lãi là không đồng. "
           "Ngân hàng nhận tiền mà không trả lãi, chuyện đó nghĩa là gì? Tiền của người gửi có còn an toàn không? Và nếu là anh chị, anh chị sẽ làm gì với cuốn sổ sắp đáo hạn?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Biểu lãi suất mới nói gì?', cap=('BIỂU LÃI SUẤT MỚI', 'CHỈ CÒN 2 KỲ HẠN CÓ LÃI'), cols=CR, moc=True, giay=dict(tieu_de='BIỂU LÃI SUẤT SCB TỪ 16/11', so='Theo Dân trí và Người Quan Sát, 16/11/2026', dau='ĐÃ ĐỌC', dieu=[
        ('Tiết kiệm online 31 ngày đến 36 tháng: 0%.', '0%'),
        ('Tại quầy, khách gửi mới, 1 đến 11 tháng: 0%.', '0%'),
        ('Kỳ hạn 12 tháng: 3,7% mỗi năm.', '3,7%'),
        ('Kỳ hạn 13 tháng: 8,7% mỗi năm, lãi cuối kỳ.', 'CÓ ĐIỀU KIỆN?')]),
      say=("Con gái gửi sang bảng tóm tắt theo báo Dân trí và Người Quan Sát. Một, tiết kiệm online, từ ba mươi mốt ngày đến ba mươi sáu tháng, đều không phần trăm. Hai, tại quầy, khách cá nhân gửi mới, kỳ hạn dưới mười hai tháng cũng không phần trăm. "
           "Ba, chỉ còn kỳ hạn mười hai tháng là ba phẩy bảy phần trăm mỗi năm. Bốn, kỳ hạn mười ba tháng ghi tám phẩy bảy phần trăm, lãi cuối kỳ. Mức cao bất thường này, theo báo, thường kèm điều kiện, và ngân hàng chưa công bố biểu thay thế cho hai kỳ hạn này.")),
 dict(k='bars', anh=TP, cap=('TỪ 9,5% VỀ 0%', 'TRONG HƠN 2 NĂM'), cols=CR, moc=True,
      bars=[('Trước 2024', 9.5, GREEN, '9,5%'), ('2024 đến T9/2026', 3.9, GOLD, '3,9%'), ('Cuối T10/2026', 0.7, RED, '0,7%'), ('Từ 16/11/2026', 0.05, RED, '0%')],
      say=("Nhìn lại lãi suất cao nhất SCB từng trả, theo báo MotTheGioi. Trước năm 2024, có lúc lên tới chín phẩy năm phần trăm. Từ năm 2024 đến trước tháng mười năm nay, còn ba phẩy chín phần trăm. "
           "Cuối tháng mười còn không phẩy bảy. Và từ hôm qua, về không. Đây là lần điều chỉnh mạnh thứ hai chỉ trong khoảng một tháng.")),
 dict(k='cards', anh=BT, cap=('CÙNG 200 TRIỆU, 6 THÁNG', 'NƠI 0 ĐỒNG, NƠI 6,6 TRIỆU'), cols=CC, moc=True,
      cards=[('0 đồng', 'SCB, 6 tháng, biểu mới', 'KHÔNG CÓ LÃI'), ('700 nghìn', 'SCB, biểu cuối tháng 10', 'LÃI 0,7%'), ('6,6 triệu', 'Ngân hàng khác, 6,6% mỗi năm', 'MỨC NIÊM YẾT ONLINE')],
      say=("Em tính thử với hai trăm triệu, kỳ hạn sáu tháng. Theo biểu mới của SCB, lãi là không đồng. Theo biểu cuối tháng mười, khoảng bảy trăm nghìn đồng. "
           "Còn ở một ngân hàng tư nhân lớn đang niêm yết sáu phẩy sáu phần trăm mỗi năm cho kỳ hạn này, cùng số tiền đó cho khoảng sáu phẩy sáu triệu đồng.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='chat', ch='Chương 2 – Vì sao ngân hàng không trả lãi?', cap=('"NGÂN HÀNG KHÔNG TRẢ LÃI', 'LÀ HẾT TIỀN À?"'), cols=CR, moc=True, chat=dict(ten='Anh Toàn', tv='Đang hoạt động', gio='08:15', mau=G_, msgs=[
        ('me', 'Ngân hàng không trả lãi là hết tiền à cháu?'),
        ('Anh Toàn', 'Không hẳn cô ạ. Ngân hàng này đang được cơ cấu lại'),
        ('Anh Toàn', 'Họ không cần hút thêm tiền gửi mới')]),
      say=("Cô Hạnh nhắn cho anh Toàn, hàng xóm làm kế toán. Ngân hàng không trả lãi, có phải là hết tiền không? Anh Toàn trả lời: chưa thể nói vậy. "
           "Ngân hàng này đang trong quá trình cơ cấu lại. Ngân hàng không công bố lý do chính thức, nhưng trả lãi bằng không thì gần như là nói rằng họ không cần hút thêm tiền gửi mới.")),
 dict(k='giay', cap=('KIỂM SOÁT ĐẶC BIỆT', 'TỪ THÁNG 10/2022'), cols=CC, moc=True, giay=dict(tieu_de='NHỮNG ĐIỀU ĐÃ CÔNG BỐ', so='Theo Dân trí 16/11/2026 và CafeF 22/8/2026', dau='ĐÃ ĐỌC', dieu=[
        ('Kiểm soát đặc biệt từ năm 2022.', 'TỪ 2022'),
        ('Từ 240 điểm giao dịch, nay còn 8.', 'CÒN 8 ĐIỂM'),
        ('Chuyển tiền nhanh tối đa 20 triệu mỗi ngày.', '20 TRIỆU'),
        ('30/6/2026: trình phương án xử lý tài sản.', 'ĐANG XỬ LÝ')]),
      say=("Anh Toàn gửi những điều đã được công bố. Một, SCB được Ngân hàng Nhà nước đặt vào diện kiểm soát đặc biệt từ năm 2022, sau biến cố liên quan tập đoàn Vạn Thịnh Phát. "
           "Hai, trước đó ngân hàng có khoảng hai trăm bốn mươi điểm giao dịch, đến ngày ba tháng mười một chỉ còn tám điểm, ở sáu tỉnh, thành. "
           "Ba, hạn mức chuyển tiền nhanh trên ứng dụng giảm còn tối đa hai mươi triệu đồng mỗi ngày. Bốn, theo CafeF, ngày ba mươi tháng sáu năm nay, Ngân hàng Nhà nước đã trình Thủ tướng phương án xử lý tài sản thu hồi nợ của SCB.")),
 dict(k='bignum', anh=HN, cap=('CỨ 30 ĐIỂM GIAO DỊCH', 'NAY CÒN 1'), cols=CR, moc=True, value=8, fmt='{:,.0f}', unit=' điểm', top='ĐIỂM GIAO DỊCH CÒN LẠI', sub='Từ khoảng 240 điểm trước năm 2022', col=RED,
      say=("Em chia hai trăm bốn mươi cho tám, ra ba mươi. Cứ ba mươi điểm giao dịch ngày trước, nay còn một. "
           "Ngân hàng đang thu nhỏ lại, giảm chi phí, xử lý nợ xấu. Trong bối cảnh đó, lãi suất bằng không là một cách để dòng tiền gửi mới tự đi nơi khác.")),
 dict(k='cards', anh=TP, cap=('CẢ NGÀNH CŨNG GIẢM', 'NHƯNG KHÔNG VỀ 0'), cols=CC, moc=True,
      cards=[('4,15 đến 6,9%', 'Lãi online 6 tháng phổ biến', 'NGÂN HÀNG KHÁC'), ('6 đến 7%', 'Lãi online 12 tháng phổ biến', 'NGÂN HÀNG KHÁC'), ('8 đến 10%', 'Trái phiếu ngân hàng', 'VẪN HUY ĐỘNG')],
      say=("Có phải cả ngành đang về không? Không. Theo Dân trí, lãi tiết kiệm online kỳ hạn sáu tháng ở các ngân hàng khác phổ biến từ bốn phẩy mười lăm đến sáu phẩy chín phần trăm. Kỳ hạn mười hai tháng từ sáu đến bảy phần trăm. "
           "Đúng là lãi đang giảm dần. Nhưng theo Vietstock, ngân hàng vẫn huy động qua trái phiếu ở mức tám đến mười phần trăm. Trường hợp SCB là cá biệt, không phải xu hướng chung.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước là tháng 10/2022', cap=('"ĐÊM ĐÓ BÁC XẾP HÀNG', 'RÚT HẾT, MẤT SẠCH LÃI"'), cols=CC, moc=True, call=dict(ten='Bác Tư', phu='Hàng xóm, gửi tiết kiệm 20 năm', mau=V_, loi=[
        'Tháng 10/2022 bác rút trước hạn', 'Mất gần hết tiền lãi']),
      say=("Trưa đó cô Hạnh gọi cho bác Tư, hàng xóm gửi tiết kiệm hơn hai mươi năm. Bác kể: chiều tối mùng bảy tháng mười năm 2022, tin đồn về ngân hàng này lan trên mạng. "
           "Bác cũng xếp hàng, rút trước hạn cả cuốn sổ. Tiền gốc còn nguyên, nhưng gần như mất sạch tiền lãi của kỳ hạn.")),
 dict(k='giay', cap=('THÁNG 10/2022', 'NHỮNG CON SỐ CỦA LẦN TRƯỚC'), cols=CC, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='Theo VnEconomy 8/10/2022 và báo chí ngày 15/10/2022', dau='SO SÁNH', dieu=[
        ('7/10/2022: tin đồn lan, người dân rút tiền.', 'RÚT ỒN ÀO'),
        ('Ngân hàng Nhà nước: quyền lợi người gửi được bảo đảm.', 'CAM KẾT'),
        ('12/10/2022: gửi lại gần 6.000 tỷ trong 1 ngày.', 'GỬI LẠI'),
        ('Người rút trước hạn: mất lãi kỳ hạn.', 'THIỆT THẬT')]),
      say=("Những con số của lần trước. Ngày tám tháng mười năm 2022, theo VnEconomy, Ngân hàng Nhà nước khẳng định quyền lợi người gửi tiền được bảo đảm. Cơ quan này cũng khuyên người dân cân nhắc, vì rút trước hạn sẽ mất lãi. "
           "Ngày mười hai tháng mười, SCB cho biết khách gửi lại gần sáu nghìn tỷ đồng chỉ trong một ngày, so với hơn một nghìn sáu trăm tỷ của ngày trước đó. Người thiệt thật là người hoảng loạn rút trước hạn.")),
 dict(k='checklist', anh=TP, cap=('GIỐNG 2, KHÁC 2', 'SO VỚI NĂM 2022'), cols=CC, moc=True,
      items=[('Giống: cùng một ngân hàng', RED), ('Giống: tin lan rất nhanh', RED), ('Khác: không ai bị giữ tiền', GREEN), ('Khác: bảo hiểm tiền gửi 350 triệu', GREEN)],
      say=("So với năm 2022, có hai điểm giống và hai điểm khác. Giống ở chỗ cùng một ngân hàng, và tin tức lan rất nhanh. "
           "Khác ở chỗ lần này không có chuyện ngân hàng giữ tiền, chỉ là không trả lãi cho tiền gửi mới. Và lưới an toàn đã dày hơn nhiều, như em kể ngay sau đây. Chưa có biến cố, không có nghĩa là không cần để ý.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='bignum', ch='Chương 4 – Lưới an toàn 350 triệu', anh=HN, cap=('BẢO HIỂM TIỀN GỬI', 'TỐI ĐA 350 TRIỆU'), cols=CC, moc=True, value=350, fmt='{:,.0f}', unit=' triệu', top='HẠN MỨC CHI TRẢ TỪ 13/7/2026', sub='Thông tư 05/2026, gấp 2,8 lần mức cũ 125 triệu', col=GOLD,
      say=("Từ ngày mười ba tháng bảy năm nay, theo quy định mới của Ngân hàng Nhà nước, hạn mức chi trả bảo hiểm tiền gửi tăng lên tối đa ba trăm năm mươi triệu đồng. Mức này gấp hai phẩy tám lần mức cũ một trăm hai mươi lăm triệu. "
           "Con số này tính trên tổng tiền gốc và lãi của một người, tại một ngân hàng.")),
 dict(k='chat', cap=('"SỔ 200 TRIỆU CỦA MẸ', 'NẰM TRONG HẠN MỨC"'), cols=CC, moc=True, chat=dict(ten='Con gái', tv='Đang hoạt động', gio='12:30', mau=G_, msgs=[
        ('Con gái', 'Sổ 200 triệu của mẹ nằm trong hạn mức 350 triệu'),
        ('me', 'Vậy mẹ có cần rút ngay không?'),
        ('Con gái', 'Đợi đúng ngày đáo hạn đã mẹ, rút trước là mất lãi')]),
      say=("Con gái nhắn: sổ hai trăm triệu của mẹ nằm trong hạn mức ba trăm năm mươi triệu. Cô hỏi lại: vậy có cần rút ngay không? "
           "Con gái trả lời đúng bài học của bác Tư: đợi đúng ngày đáo hạn, rút trước là mất lãi của kỳ đang gửi.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='cards', ch='Chương 5 – Ba con đường cho cuốn sổ', anh=NHA, cap=('3 CON ĐƯỜNG', 'CHO 200 TRIỆU'), cols=CC, moc=True,
      cards=[('0 đồng', 'Gửi lại 6 tháng tại SCB', 'KHÔNG CÓ LÃI'), ('7,4 triệu', 'Kỳ hạn 12 tháng, lãi 3,7%', 'SAU 1 NĂM'), ('6,6 triệu', 'Nơi khác 6 tháng, lãi 6,6%', 'SAU 6 THÁNG')],
      say=("Đến ngày đáo hạn, cô Hạnh có ba con đường. Một, gửi lại sáu tháng tại SCB, lãi không đồng. Hai, chuyển sang kỳ hạn mười hai tháng, lãi ba phẩy bảy phần trăm, sau một năm được khoảng bảy phẩy bốn triệu đồng. "
           "Ba, rút ra gửi nơi khác, với mức sáu phẩy sáu phần trăm thì sáu tháng được khoảng sáu phẩy sáu triệu đồng.")),
 dict(k='giay', cap=('RÚT 200 TRIỆU', 'CHUYỂN NHANH MẤT 10 NGÀY'), cols=CR, moc=True, giay=dict(tieu_de='GHI CHÚ TRƯỚC NGÀY ĐÁO HẠN', so='Cô Hạnh tự ghi, số liệu theo báo 16/11/2026', dau='CẦN NHỚ', dieu=[
        ('Chuyển nhanh tối đa 20 triệu mỗi ngày.', '10 NGÀY'),
        ('Rút tại quầy: chỉ còn 8 điểm giao dịch.', 'HỎI TRƯỚC'),
        ('Mang căn cước, hỏi rõ thủ tục.', 'GIẤY TỜ'),
        ('Lãi 13 tháng 8,7%: hỏi điều kiện.', 'ĐỌC KỸ')]),
      say=("Nhưng con đường thứ ba có vài điều phải biết. Hạn mức chuyển tiền nhanh là hai mươi triệu đồng mỗi ngày, hai trăm triệu sẽ mất khoảng mười ngày nếu chuyển qua ứng dụng. "
           "Rút tại quầy thì cả nước chỉ còn tám điểm giao dịch, nên gọi hỏi trước. Còn mức tám phẩy bảy phần trăm của kỳ hạn mười ba tháng, cô ghi rõ: phải hỏi điều kiện, không chạy theo con số bất thường.")),
 dict(k='chat', cap=('"MẸ CHIA RA 2 NƠI', 'MỖI NƠI DƯỚI 350 TRIỆU"'), cols=CC, moc=True, chat=dict(ten='Con gái', tv='Đang hoạt động', gio='20:10', mau=G_, msgs=[
        ('me', 'Đáo hạn mẹ rút, gửi sang chỗ có lãi'),
        ('me', 'Tiền hưu sau này mẹ chia ra 2 nơi'),
        ('Con gái', 'Mỗi nơi dưới 350 triệu là mẹ ngủ ngon')]),
      say=("Tối đó cô Hạnh nhắn cho con gái kế hoạch của mình. Đến ngày đáo hạn, cô sẽ rút và gửi sang nơi có lãi. Tiền dành dụm sau này, cô chia ra hai ngân hàng. "
           "Con gái trả lời: mỗi nơi dưới ba trăm năm mươi triệu là mẹ ngủ ngon. Đó là lựa chọn của cô Hạnh, không phải lời khuyên chung cho mọi người.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='checklist', ch='Chương 6 – Phép thử cho sổ tiết kiệm', anh=HN, cap=('PHÉP THỬ', 'SỔ CỦA ANH CHỊ Ở ĐÂU?'), cols=CC, moc=True,
      items=[('Gốc và lãi 1 nơi dưới 350 triệu?', GREEN), ('Có sổ đáo hạn trong 30 ngày?', GOLD), ('Lãi đang nhận dưới 4%?', GOLD), ('Mức lãi cao bất thường?', RED)],
      say=("Em gợi ý một phép thử tự soi. Một, tổng gốc và lãi của anh chị ở mỗi ngân hàng có dưới ba trăm năm mươi triệu đồng không. Hai, có cuốn sổ nào đáo hạn trong ba mươi ngày tới. "
           "Ba, mức lãi đang nhận có thấp hơn bốn phần trăm, trong khi mặt bằng kỳ hạn mười hai tháng đang khoảng sáu đến bảy phần trăm. Bốn, có mức lãi nào cao bất thường so với nơi khác. Đây là mốc tự soi, không phải lời khuyên.")),
 dict(k='checklist', anh=TP, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI CUỐI NĂM'), cols=CC, moc=True,
      items=[('Biểu mới cho kỳ hạn 12, 13 tháng', GOLD), ('Phương án cơ cấu lại SCB', GOLD), ('Lãi suất nơi khác giảm tiếp?', RED)],
      say=("Ba điều đáng theo dõi tới cuối năm. SCB công bố biểu mới cho kỳ hạn mười hai và mười ba tháng ra sao. Phương án cơ cấu lại ngân hàng này được quyết thế nào. "
           "Và lãi suất tiết kiệm ở các ngân hàng khác có giảm tiếp hay không. Muốn hiểu vì sao gửi tiết kiệm chưa chắc đã giữ được sức mua, anh chị có thể đọc bài miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"TIỀN GỬI KHÔNG MẤT', 'CHỈ LÀ ĐỨNG YÊN"'), cols=CC, moc=True, chat=dict(ten='Bác Tư', tv='Đang hoạt động', gio='21:30', mau=V_, msgs=[
        ('Bác Tư', 'Cô đừng xếp hàng như bác năm đó nhé'),
        ('me', 'Dạ, em đợi đáo hạn rồi tính'),
        ('me', 'Tiền gửi không mất, chỉ là đứng yên')]),
      say=("Chín giờ rưỡi tối, bác Tư nhắn: cô đừng xếp hàng như bác năm đó nhé. Cô Hạnh trả lời: dạ, em đợi đáo hạn rồi tính. "
           "Rồi cô gõ thêm một dòng: tiền gửi không mất, chỉ là đứng yên. Mà tiền đứng yên thì vẫn bị giá cả ăn mòn.")),
 dict(k='end', cap=('TIỀN GỬI 1 NƠI CỦA ANH CHỊ', 'DƯỚI HAY TRÊN 350 TRIỆU?'), cols=CC,
      say=("Còn anh chị, tiền tiết kiệm của anh chị ở một ngân hàng đang dưới hay trên ba trăm năm mươi triệu đồng? Kể cho em và mọi người ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Lãi Suất Tiết Kiệm 0% Ở SCB: Gửi 200 Triệu 6 Tháng Nhận 0 Đồng – Tiền Gửi Có Còn An Toàn?'
MT = ("NÓNG: từ 16/11/2026, SCB đưa lãi suất tiết kiệm online về 0%/năm cho các kỳ hạn từ 31 ngày đến 36 tháng; tại quầy, khách cá nhân gửi mới kỳ hạn dưới 12 tháng cũng 0%. "
      "Vì sao một ngân hàng không trả lãi, tiền gửi có còn an toàn, lần trước tháng 10/2022 ai thiệt, bảo hiểm tiền gửi 350 triệu bảo vệ đến đâu, và phép thử cho cuốn sổ của anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• Dân trí 16/11/2026: biểu lãi SCB từ 16/11 – online 0%/năm kỳ hạn 31 ngày, 1, 3, 6, 12, 36 tháng (3 cách lĩnh lãi); tiết kiệm thường khách cá nhân gửi mới 0%; kỳ hạn 12 tháng 3,7%/năm, 13 tháng 8,7%/năm (lãi cuối kỳ, biểu trước đó); "
      "lần điều chỉnh mạnh thứ hai trong 1 tháng; kiểm soát đặc biệt từ 2022; chuyển tiền nhanh tối đa 20 triệu/ngày; khoảng 240 điểm giao dịch trước đây, ngày 3/11 còn 8 điểm tại 6 tỉnh, thành; "
      "lãi online phổ biến ở ngân hàng khác: 6 tháng 4,15–6,9%, 12 tháng 6–7%\n"
      "• Người Quan Sát 16/11/2026: kỳ hạn 12 và 13 tháng theo biểu 26/10, SCB chưa công bố biểu thay thế; VPBank online dưới 10 tỷ kỳ hạn 6–11 tháng 6,6%/năm; VPBank là ngân hàng thứ 5 giảm lãi huy động hơn một lần từ 18/10\n"
      "• MotTheGioi 16/11/2026: lãi cao nhất SCB trước 2024 8,5–9,5%; 2024 đến trước 10/2026 3,9%; cuối 10/2026 0,7%; từ 16/11 0% (trừ 12–13 tháng); trường hợp cá biệt, không phải xu hướng chung\n"
      "• Vietstock 17/11/2026: lãi tiết kiệm giảm 0,5–2%/năm, huy động qua trái phiếu ngân hàng 8–10%/năm\n"
      "• CafeF 22/8/2026: ngày 30/6/2026 NHNN trình Thủ tướng phương án xử lý tài sản thu hồi nợ của SCB\n"
      "• VnEconomy 8/10/2022: NHNN khẳng định quyền lợi người gửi tiền SCB được bảo đảm, rút trước hạn sẽ mất lãi; báo chí 15/10/2022 dẫn SCB: ngày 12/10/2022 khách gửi lại gần 6.000 tỷ đồng trong 1 ngày (ngày trước hơn 1.600 tỷ)\n"
      "• VietnamPlus 20/7/2026, Báo Đầu tư: Thông tư 05/2026/TT-NHNN – hạn mức chi trả bảo hiểm tiền gửi tối đa 350 triệu đồng (cũ 125 triệu) từ 13/7/2026, tính trên tổng gốc và lãi của một người tại một tổ chức\n"
      "• Tự tính: 200 triệu, 6 tháng – lãi 0% = 0 đồng; 0,7% ≈ 700 nghìn; 6,6% ≈ 6,6 triệu; kỳ hạn 12 tháng 3,7% ≈ 7,4 triệu sau 1 năm; 200 triệu ÷ 20 triệu/ngày = 10 ngày; 240 ÷ 8 = 30; 350 ÷ 125 = 2,8 lần\n\n"
      "Gửi tiết kiệm an toàn chưa chắc lãi thực – lạm phát và sức mua: https://chungkhoanhuynguyen.com/hoc/gui-tiet-kiem-an-toan-chua-chac-lai-thuc-lam-phat-va-suc-mua-sau-10.html\n"
      "Lãi suất giảm ở 46 ngân hàng – ai được giảm: https://chungkhoanhuynguyen.com/hoc/lai-suat-giam-o-46-ngan-hang-ai-duoc-giam-2-vi-sao-khoan-vay-mua-nha.html\n"
      "Cần trao đổi riêng về kế hoạch tài chính: Zalo 0365.188.286\n\n"
      "Nhân vật cô Hạnh, con gái, anh Toàn, bác Tư là hư cấu; số liệu là thật theo nguồn trên. Lãi suất có thể thay đổi, anh chị kiểm tra trực tiếp với ngân hàng.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-17', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['lãi suất tiết kiệm', 'lãi suất 0%', 'SCB', 'lãi suất ngân hàng hôm nay', 'gửi tiết kiệm', 'bảo hiểm tiền gửi', '350 triệu', 'tiền gửi an toàn', 'tin nóng tài chính', 'lãi suất tháng 11'],
    bia_hook=['LÃI SUẤT 0%', 'TỪ 16/11'], badge='NÓNG: TIỀN GỬI CÓ AN TOÀN?',
    bia_anh='Ho Chi Minh City skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['GỬI 200 TRIỆU', 'LÃI 0 ĐỒNG'], badge_b='NƠI KHÁC: 6,6 TRIỆU',
    bia_hook_c=['TỪ 9,5%', 'VỀ 0%???'], badge_c='BẢO HIỂM TỐI ĐA 350 TR',
    reel_hook='LÃI SUẤT TIẾT KIỆM 0%|TIỀN GỬI CÒN AN TOÀN???',
    fb_post=("Một ngân hàng đưa lãi suất tiết kiệm về 0% 😳\n\n👉 Gửi 200 triệu 6 tháng: 0 đồng tiền lãi\n👉 Nơi khác cùng kỳ hạn: khoảng 6,6 triệu\n"
             "👉 Bảo hiểm tiền gửi nay tối đa 350 triệu mỗi người, mỗi ngân hàng\n\nTiền gửi của anh chị ở 1 nơi đang dưới hay trên 350 triệu?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 17/11: SCB lãi suất tiết kiệm 0%% từ 16/11 (NV1B 17/11/2026).\n"
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
