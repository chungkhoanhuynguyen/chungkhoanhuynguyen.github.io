# -*- coding: utf-8 -*-
# NV1B 23/11/2026 – VIDEO NÓNG kênh chính: giá cà phê Tây Nguyên mất hơn 11.000 đồng/kg trong 1 tuần, thấp nhất gần 3 năm – xuất khẩu kỷ lục mà nhà vườn hụt tiền.
# KEY NONG2311B (NONG2311A đã dùng cho lô 20261120_nong_td). Lý do chọn: tin 24–48h chạm túi nông hộ Tây Nguyên; chưa làm cà phê trong 7 ngày
#   (CH2911SR sầu riêng là nông sản khác, góc "một khách hàng"; đây là góc "bán nhiều mà thu ít – giá theo cung cầu thế giới").
# Nguồn:
#  - Bnews/TTXVN 22/11/2026 16:11 + VietnamPlus 22/11/2026: kết thúc tuần, cà phê Tây Nguyên 71.200–72.000 đ/kg, giảm 11.000–11.200 đ/kg so cuối tuần trước (trên 13%),
#    thấp nhất gần 3 năm; robusta London kỳ hạn 1/2027 còn 2.978 USD/tấn, có lúc 2.972, mất mốc 3.000, thấp nhất khoảng hai năm rưỡi.
#    Nguyên nhân: vụ mới VN ra thị trường khối lượng lớn; real Brazil yếu → nông dân Brazil bán nhiều; USDA: Colombia 2026-27 +5,9% lên 13,4 triệu bao;
#    ICO niên vụ 2025/26: sản lượng 183,6 triệu bao (+4,4%), tiêu thụ 180,6 triệu bao (−0,9%), dư khoảng 3 triệu bao.
#    VICOFA/ICO tại VICO 2026: VN chiếm 14,2% xuất khẩu cà phê hoà tan toàn cầu, vượt Brazil 11,2%; chế biến sâu niên vụ 2025-26 ~142.600 tấn, ~1,5 tỷ USD, giá trị +14%;
#    nhà máy hoà tan đủ đơn hàng chạy hết công suất đến hết quý I/2027 (Phó Chủ tịch VICOFA).
#  - Thương Trường 23/11/2026 07:01: sáng 23/11 Đắk Lắk và Gia Lai quanh 71.800 đ/kg; chi phí nhân công và vật tư cao, biên lợi nhuận người trồng thu hẹp.
#  - WiData ai_news 21/11/2026: Đắk Lắk 20/11/2026 73.800 đ/kg, đáy 1 năm, −22% so tháng trước, −36,8% so cùng kỳ, thấp hơn 45,5% so đỉnh 10 năm.
#  - Báo Văn hoá + Báo Lâm Đồng 23/11/2025: Đắk Lắk 112.500 đ/kg sáng 23/11/2025.
#  - CafeF 20/10/2026 (VICOFA 19/10): niên vụ 2025-2026 xuất khẩu 1,8 triệu tấn, 8,5 tỷ USD – cao nhất từ trước tới nay; lượng +21%, kim ngạch +1%.
#  - CafeF 15/10/2026 (Bộ NN&MT): 9 tháng 2026 xuất khẩu ~1,4 triệu tấn, 6,5 tỷ USD; lượng +15,4%, kim ngạch −7,3%; giá bình quân ~4.537 USD/tấn, giảm gần 20%.
#  - Doanh nghiệp Hội nhập 27/3/2025: Đắk Lắk 135.500 đ/kg – kỷ lục mới (khớp WiData: thấp hơn 45,5% đỉnh 10 năm → đỉnh ≈ 135.400).
#  - VOH 12/12/2019: Tây Nguyên 32.600–33.200 đ/kg; niên vụ 2018-2019 xuất khẩu ~1,7 triệu tấn, gần 3 tỷ USD; nhiều vườn đã chặt bỏ chuyển cây khác.
#  - Nông nghiệp & Môi trường 18/3/2020: Tây Nguyên 29.700–30.200 đ/kg.
# SỐ TỰ TÍNH: 71.800/112.500 = 0,638 → giảm khoảng 36%; chênh 40.700 đ/kg. 71.800/135.500 = 0,53 → bằng khoảng 53% đỉnh. 71.800/30.000 ≈ 2,4 lần đáy 3/2020.
#   Dư 3/183,6 = 1,6% → "chưa tới hai phần trăm". Vườn anh Tư GIẢ ĐỊNH 4 tấn nhân: năm ngoái 4.000×112.500 = 450 triệu; nay 4.000×71.800 = 287,2 triệu; hụt 162,8 triệu.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261123_0815_nong'
KEY = 'NONG2311B'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
CF = 'ov:Coffee beans drying||Coffee beans drying'
CB = 'ov:Coffee beans drying||Coffee beans drying'
BMT = 'ov:Buon Ma Thuot||Buon Ma Thuot'
CON = 'ov:Container ship||Container ship'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', short=True, cap=('CÀ PHÊ MẤT 11.000 ĐỒNG/KG', 'CHỈ TRONG 1 TUẦN'), cols=CR, noti=dict(gio='06:10', ngay='Thứ Hai', items=[
        ('Tin tức', 'Nông sản', 'Cà phê Tây Nguyên mất hơn 11.000 đồng/kg trong tuần', R_),
        ('Linh', 'Tin nhắn', 'Bố ơi giá cà phê sao rồi? Nhà mình bán chưa?', X_)]),
      say=("Sáu giờ sáng nay, anh Tư ở Buôn Ma Thuột vừa ra sân phơi thì điện thoại hiện một tin. Theo Thông tấn xã Việt Nam, chỉ trong tuần qua, giá cà phê nhân Tây Nguyên đã mất hơn mười một nghìn đồng mỗi ký, xuống thấp nhất gần ba năm. "
           " Ngay sau đó là tin nhắn của con gái anh, Linh, đang làm ở Sài Gòn: bố ơi, giá cà phê sao rồi, nhà mình bán chưa?")),
 dict(k='bignum', anh=CF, short=True, cap=('CÀ PHÊ ĐẮK LẮK', 'CÒN 71.800 ĐỒNG/KG'), cols=CR, value=71800, fmt='{:,.0f}', unit=' đ/kg', top='CÀ PHÊ NHÂN ĐẮK LẮK SÁNG 23/11/2026', sub='Cùng ngày năm ngoái: 112.500 đồng/kg', col=RED,
      say=("Sáng nay, giá ở Đắk Lắk quanh bảy mươi mốt nghìn tám trăm đồng mỗi ký. Cùng ngày này năm ngoái là một trăm mười hai nghìn năm trăm đồng. Tức là giảm khoảng ba mươi sáu phần trăm. "
           "Nhưng chuyện lạ nằm ở chỗ khác. Chính niên vụ vừa rồi, cà phê Việt Nam vừa xuất khẩu nhiều tiền nhất từ trước đến nay. Vậy tiền đi đâu?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Một tuần mất 11.000 đồng', cap=('BẢNG GIÁ SÁNG NAY', 'THẤP NHẤT GẦN 3 NĂM'), cols=CR, moc=True, giay=dict(tieu_de='BẢNG GIÁ CÀ PHÊ SÁNG NAY', so='Theo Thương Trường 23/11, TTXVN 22/11/2026', dau='GIÁ', dieu=[
        ('Đắk Lắk: 71.800 đồng/kg.', 'GIẢM'),
        ('Gia Lai: 71.800 đồng/kg.', 'GIẢM'),
        ('Một tuần: mất hơn 11.000 đồng/kg.', 'TRÊN 13%'),
        ('Robusta London: dưới 3.000 USD/tấn.', 'MẤT MỐC 3.000')]),
      say=("Anh Tư mở bảng giá sáng nay. Đắk Lắk và Gia Lai cùng một mức giá. Chỉ một tuần, giá mất hơn mười ba phần trăm. "
           "Trên sàn London, nơi định giá loại cà phê vối Việt Nam trồng nhiều nhất, giá đã thủng mốc ba nghìn đô la Mỹ mỗi tấn.")),
 dict(k='giay', short=True, cap=('VƯỜN 4 TẤN NHÂN (GIẢ ĐỊNH)', 'HỤT HƠN 160 TRIỆU'), cols=CR, moc=True, giay=dict(tieu_de='SỔ BÁN CÀ PHÊ CỦA ANH TƯ', so='Em giả định để minh hoạ', dau='GIẢ ĐỊNH', dieu=[
        ('Vườn thu khoảng 4 tấn nhân.', 'MỖI VỤ'),
        ('Theo giá 23/11/2025: 450 triệu.', 'NĂM NGOÁI'),
        ('Giá sáng nay 71.800: 287,2 triệu.', 'NAY'),
        ('Chênh lệch: 162,8 triệu đồng.', 'HỤT')]),
      say=("Anh Tư lấy cuốn sổ ra tính. Em giả định vườn anh thu khoảng bốn tấn nhân mỗi vụ. Với giá cùng kỳ năm ngoái, bốn tấn bán được bốn trăm năm mươi triệu đồng. "
           "Với giá sáng nay, chỉ còn khoảng hai trăm tám mươi bảy triệu đồng. Cùng một vườn, cùng một công chăm, mà hụt hơn một trăm sáu mươi triệu đồng.")),
 dict(k='chat', cap=('"XUẤT KHẨU KỶ LỤC', 'MÀ SAO GIÁ RỚT HẢ BỐ?"'), cols=CR, moc=True, chat=dict(ten='Linh', tv='Đang hoạt động', gio='06:30', mau=X_, msgs=[
        ('Linh', 'Con đọc báo nói cà phê xuất khẩu kỷ lục mà bố'),
        ('Linh', 'Sao giá ở vườn lại rớt hả bố?'),
        ('me', 'Bố cũng không hiểu, con tìm giúp bố')]),
      say=("Linh nhắn tiếp. Con đọc báo nói cà phê xuất khẩu kỷ lục mà bố, sao giá ở vườn lại rớt? Anh Tư trả lời rằng anh cũng không hiểu, nhờ con tìm giúp. "
           "Và câu trả lời nằm ngay trong những con số kỷ lục đó.")),
 dict(k='bignum', anh=CON, cap=('XUẤT KHẨU KỶ LỤC', '8,5 TỶ USD'), cols=CC, moc=True, value=8.5, fmt='{:,.1f}', unit=' tỷ USD', top='XUẤT KHẨU CÀ PHÊ NIÊN VỤ 2025-2026', sub='Cao nhất từ trước tới nay (VICOFA, CafeF 20/10/2026)', col=GOLD,
      say=("Theo Hiệp hội Cà phê Ca cao Việt Nam, cà phê Việt Nam vừa xuất khẩu được tám phẩy năm tỷ đô la Mỹ trong niên vụ vừa rồi, cao nhất từ trước tới nay. "
           "Con số này nghe rất đẹp. Nhưng đây là cú lật đầu tiên: lượng hàng bán ra tăng hai mươi mốt phần trăm, còn tiền thu về chỉ tăng khoảng một phần trăm.")),
 dict(k='cards', anh=CB, cap=('BÁN NHIỀU HƠN 21%', 'THU VỀ CHỈ HƠN 1%'), cols=CC, moc=True,
      cards=[('1,8 triệu tấn', 'Lượng xuất niên vụ 2025-26', 'TĂNG 21%'), ('8,5 tỷ USD', 'Tiền thu về cả niên vụ', 'CHỈ TĂNG 1%'), ('4.537 USD/tấn', 'Giá bình quân 9 tháng 2026', 'GIẢM GẦN 20%')],
      say=("Nói cách khác, Việt Nam bán nhiều hơn hẳn, nhưng mỗi tấn bán rẻ hơn. Theo Bộ Nông nghiệp và Môi trường, chín tháng đầu năm nay, giá xuất khẩu bình quân chỉ còn hơn bốn nghìn năm trăm đô la Mỹ mỗi tấn, giảm gần hai mươi phần trăm. "
           "Kỷ lục là kỷ lục về tiền của cả ngành, nhưng có được là nhờ bán nhiều hơn. Còn giá mỗi tấn, thứ quyết định tiền trong túi nhà vườn, đã đi xuống từ trước khi vụ mới bắt đầu.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='noti', ch='Chương 2 – Vì sao giá rơi nhanh như vậy?', cap=('VỤ MỚI VỀ Ồ ẠT', 'BRAZIL CŨNG ĐẨY MẠNH BÁN'), cols=CR, moc=True, noti=dict(gio='07:00', ngay='Thứ Hai', items=[
        ('Tin tức', 'Nông sản', 'Vụ mới Việt Nam ra thị trường khối lượng lớn', R_),
        ('Tin tức', 'Thế giới', 'Đồng real yếu, nông dân Brazil đẩy mạnh bán', V_)]),
      say=("Linh gửi cho bố hai dòng tin. Theo Thông tấn xã Việt Nam, vụ mới của Việt Nam đang ra thị trường với khối lượng lớn, nhà rang xay có thêm nhiều lựa chọn. "
           "Cùng lúc, đồng tiền của Brazil yếu đi, khiến nông dân Brazil đẩy mạnh bán ra. Hai nước xuất khẩu cà phê hàng đầu thế giới cùng bán mạnh trong một thời điểm.")),
 dict(k='bignum', anh=CF, cap=('THẾ GIỚI CHỈ DƯ', 'CHƯA TỚI 2% LƯỢNG CÀ PHÊ'), cols=CC, moc=True, value=3, fmt='{:,.0f}', unit=' triệu bao', top='CÀ PHÊ THẾ GIỚI DƯ RA NIÊN VỤ 2025/26', sub='Sản xuất 183,6 triệu bao, tiêu thụ 180,6 triệu bao (ICO)', col=GOLD,
      say=("Rồi đến cú lật thứ hai. Theo Tổ chức Cà phê Quốc tế, niên vụ này thế giới làm ra hơn một trăm tám mươi ba triệu bao cà phê, nhưng chỉ dùng chưa tới một trăm tám mươi mốt triệu bao. "
           "Phần dư ra khoảng ba triệu bao, chưa tới hai phần trăm. Dư không nhiều, nhưng cùng lúc vụ mới về và Brazil bán mạnh, giá đã chịu sức ép lớn. Với nông sản, dư một chút cũng đủ khiến người mua dễ trả giá thấp hơn.")),
 dict(k='cards', anh=CB, cap=('CUNG TĂNG, CẦU GIẢM', 'CÙNG MỘT LÚC'), cols=CC, moc=True,
      cards=[('183,6 triệu bao', 'Sản lượng thế giới 2025/26', 'TĂNG 4,4%'), ('180,6 triệu bao', 'Tiêu thụ thế giới 2025/26', 'GIẢM 0,9%'), ('13,4 triệu bao', 'Colombia vụ 2026-27 (USDA)', 'TĂNG 5,9%')],
      say=("Sản lượng thế giới tăng hơn bốn phần trăm, trong khi lượng tiêu thụ lại giảm nhẹ. "
           "Và năm tới chưa chắc đã bớt hàng. Bộ Nông nghiệp Mỹ dự báo Colombia, một nước trồng cà phê lớn khác, sẽ tăng sản lượng gần sáu phần trăm.")),
 dict(k='chat', cap=('"HẠT THÔ RỚT GIÁ', 'NHƯNG CÓ CHỖ VẪN BÁN ĐƯỢC"'), cols=CC, moc=True, chat=dict(ten='Linh', tv='Đang hoạt động', gio='07:20', mau=X_, msgs=[
        ('Linh', 'Vụ mới về cùng lúc Brazil bán mạnh, nên giá bị ép đó bố'),
        ('Linh', 'Nhưng con thấy có một chỗ vẫn bán được'),
        ('me', 'Chỗ nào con?')]),
      say=("Linh nhắn: dư không nhiều, nhưng vụ mới về cùng lúc Brazil bán mạnh, nên giá bị ép đó bố. Nhưng con thấy có một chỗ cà phê Việt Nam vẫn bán được. Anh Tư hỏi lại: chỗ nào con?")),
 dict(k='bignum', anh=TP, cap=('CÀ PHÊ HOÀ TAN VIỆT NAM', 'VƯỢT CẢ BRAZIL'), cols=CC, moc=True, value=14.2, fmt='{:,.1f}', unit='%', top='THỊ PHẦN XUẤT KHẨU CÀ PHÊ HOÀ TAN THẾ GIỚI', sub='Brazil 11,2% (ICO, tại VICO 2026 – VietnamPlus 22/11/2026)', col=GREEN,
      say=("Đó là cú lật thứ ba. Theo Tổ chức Cà phê Quốc tế, Việt Nam đang chiếm mười bốn phẩy hai phần trăm xuất khẩu cà phê hoà tan toàn cầu, vượt cả Brazil. "
           "Niên vụ vừa rồi, cà phê chế biến sâu thu về khoảng một phẩy năm tỷ đô la Mỹ, giá trị tăng khoảng mười bốn phần trăm. Phó chủ tịch Hiệp hội Cà phê Ca cao Việt Nam cho biết các nhà máy hoà tan đã có đủ đơn hàng để chạy hết công suất đến hết quý một năm sau. "
           "Hạt thô bán theo giá trên sàn London, còn hàng chế biến có đơn hàng ổn định hơn. Nhưng hạt anh Tư bán ra vẫn đi theo giá trên sàn London.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước là năm 2019', cap=('"NĂM 2019 CHÚ CHẶT 1 HÉC TA', 'LÚC ĐÓ AI BIẾT TRƯỚC"'), cols=CC, moc=True, call=dict(ten='Chú Sáu', phu='Hàng xóm', mau=V_, loi=[
        'Năm 2019 giá còn hơn 30 nghìn', 'Chú chặt một héc ta, lúc đó ai biết trước']),
      say=("Trưa nay, anh Tư gọi cho chú Sáu, hàng xóm đã trồng cà phê hơn ba mươi năm. Chú kể: cuối năm hai nghìn không trăm mười chín, giá chỉ còn hơn ba mươi nghìn đồng mỗi ký. "
           "Chú nản, chặt một héc ta để trồng cây khác. Mấy năm sau giá lên, nhưng lúc chặt thì không ai biết trước. Chú tiếc, còn có nhà chuyển cây khác vẫn sống ổn.")),
 dict(k='giay', cap=('NĂM 2019–2020', 'NHỮNG CON SỐ CỦA LẦN TRƯỚC'), cols=CC, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='VOH 12/12/2019, Nông nghiệp 18/3/2020, DN Hội nhập 27/3/2025', dau='SO SÁNH', dieu=[
        ('12/2019: 32.600 đến 33.200 đồng/kg.', 'MỐC CŨ'),
        ('3/2020: 29.700 đến 30.200 đồng/kg.', 'MỐC CŨ'),
        ('Niên vụ 2018-19: gần 3 tỷ USD.', 'XUẤT KHẨU'),
        ('3/2025: 135.500 đồng/kg.', 'KỶ LỤC')]),
      say=("Những con số của lần trước. Theo báo VOH, tháng mười hai năm hai nghìn không trăm mười chín, giá cà phê Tây Nguyên chỉ hơn ba mươi hai nghìn đồng mỗi ký. Đến tháng ba năm hai nghìn không trăm hai mươi, giá còn quanh ba mươi nghìn đồng. "
           "Theo VOH, thời đó nhiều vườn bị chặt bỏ để chuyển sang cây khác. Rồi đến tháng ba năm hai nghìn không trăm hai mươi lăm, giá ở Đắk Lắk lập kỷ lục một trăm ba mươi lăm nghìn năm trăm đồng mỗi ký.")),
 dict(k='bars', anh=CF, cap=('3 MỐC GIÁ', 'MỖI KÝ CÀ PHÊ'), cols=CC, moc=True,
      bars=[('Tháng 3/2020', 30, RED, '30.000'), ('Đỉnh 3/2025', 135.5, GOLD, '135.500'), ('Sáng 23/11/2026', 71.8, GREEN, '71.800')],
      say=("Đặt ba mốc cạnh nhau. Giá sáng nay vẫn cao gấp hơn hai lần mức tháng ba năm hai nghìn không trăm hai mươi. "
           "Nhưng chỉ bằng khoảng năm mươi ba phần trăm đỉnh tháng ba năm ngoái. Người trồng đau không phải vì giá đã về mốc cũ, mà vì giá rơi quá nhanh từ một đỉnh rất cao.")),
 dict(k='checklist', anh=BMT, cap=('GIỐNG 2, KHÁC 2', 'SO VỚI NĂM 2019'), cols=CC, moc=True,
      items=[('Giống: giá rơi đúng mùa thu hoạch', GOLD), ('Giống: giá mỗi tấn đi xuống', GOLD), ('Khác: giá vẫn gấp 2 lần mốc cũ', GREEN), ('Khác: chi phí nay cao', RED)],
      say=("So với lần trước, có hai điểm giống và hai điểm khác. Giống ở chỗ giá rơi đúng mùa thu hoạch, và giá bán mỗi tấn đều đi xuống. Hồi đó, theo VOH, kim ngạch còn giảm hơn mười bốn phần trăm. Năm nay tiền vẫn giữ được, nhưng là nhờ bán nhiều hơn. "
           "Khác ở chỗ giá hôm nay vẫn cao gấp hơn hai lần mốc cũ. Nhưng theo báo Thương Trường, chi phí nhân công và vật tư hiện nay cao, nên biên lợi nhuận của người trồng bị thu hẹp.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='cards', ch='Chương 4 – Ba con đường của anh Tư', anh=CB, cap=('3 CON ĐƯỜNG', 'KHI GIÁ RƠI ĐÚNG MÙA THU HOẠCH'), cols=CC, moc=True,
      cards=[('Bán hết', 'Có tiền ngay', 'CHỐT Ở GIÁ THẤP'), ('Bán dần', 'Chia nhiều đợt theo tháng', 'NHIỀU MỨC GIÁ'), ('Giữ hết', 'Chờ giá hồi', 'PHỤ THUỘC GIÁ HỒI')],
      say=("Anh Tư thấy có ba con đường. Một, bán hết ngay để có tiền trả nợ và chi tiêu. Không phải lo giá rơi thêm, nhưng cũng chốt luôn ở mức thấp. "
           "Hai, bán dần thành nhiều đợt, để không đặt cược cả vụ vào một ngày giá. "
           "Ba, giữ hết chờ giá hồi. Không ai biết chắc giá hồi khi nào, và áp lực lớn hơn nếu nhà đang có khoản vay. Mỗi nhà mỗi hoàn cảnh, video không khuyến nghị bán hay giữ.")),
 dict(k='chat', cap=('"BỐ BÁN TRƯỚC 1 TẤN RƯỠI', 'TRẢ TIỀN PHÂN"'), cols=CC, moc=True, chat=dict(ten='Linh', tv='Đang hoạt động', gio='20:00', mau=X_, msgs=[
        ('me', 'Bố bán trước một tấn rưỡi để trả tiền phân'),
        ('me', 'Phần còn lại bố tính dần, chưa chặt cây'),
        ('Linh', 'Dạ, sáng nào con cũng gửi bố bảng giá')]),
      say=("Tối nay anh Tư nhắn con gái kế hoạch. Anh bán trước một tấn rưỡi để trả tiền phân. Phần còn lại anh sẽ tính dần, và chưa chặt cây. "
           "Linh trả lời rằng sáng nào cũng sẽ gửi bố bảng giá. Đó là lựa chọn riêng của gia đình anh.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Phép thử cho túi tiền nhà mình', anh=BMT, cap=('PHÉP THỬ: GIÁ ĐỨNG YÊN 12 THÁNG', 'NHÀ MÌNH Ở NHÓM NÀO?'), cols=CC, moc=True,
      items=[('Vẫn dư: khá vững', GREEN), ('Vừa đủ: xem lại chi tiêu', GOLD), ('Không đủ trả nợ: tính sớm', RED)],
      say=("Em gợi ý một phép thử tự soi, cho nhà nào có thu nhập dựa nhiều vào một loại nông sản. Giả sử giá đứng yên ở mức hôm nay thêm mười hai tháng. "
           "Nếu thu vẫn đủ chi và còn dư, nhà mình khá vững. Nếu vừa đủ, là lúc xem lại chi tiêu và lịch bán. Nếu không đủ trả nợ, đó là lúc cần tính sớm với bên cho vay, trước khi khoản vay trễ hạn. Đây là mốc tự soi, không phải lời khuyên.")),
 dict(k='checklist', anh=TP, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI TẾT'), cols=CC, moc=True,
      items=[('Robusta London quanh 3.000 USD', GOLD), ('Tiến độ thu hoạch vụ mới', GOLD), ('Xuất khẩu tháng 11 và 12', GOLD)],
      say=("Ba điều đáng theo dõi từ nay tới Tết. Giá cà phê vối trên sàn London có giữ được quanh mốc ba nghìn đô la Mỹ mỗi tấn hay không. Tiến độ thu hoạch vụ mới ở Tây Nguyên. "
           "Và số xuất khẩu hai tháng cuối năm: nếu lượng tăng mà tiền không tăng, nghĩa là giá bán mỗi tấn vẫn đang thấp. Muốn hiểu giá hàng hoá tác động thế nào tới cổ phiếu và túi tiền gia đình, anh chị có thể đọc bài miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"CHUYỆN CỦA CHÚ THÔI', 'NHÀ NÀO TÍNH THEO NHÀ ĐÓ"'), cols=CC, moc=True, chat=dict(ten='Chú Sáu', tv='Đang hoạt động', gio='21:00', mau=V_, msgs=[
        ('Chú Sáu', 'Năm 2019 chú chặt một héc ta'),
        ('Chú Sáu', 'Chú kể chuyện của chú thôi, nhà nào tính theo nhà đó'),
        ('me', 'Dạ, cháu tính kỹ rồi chú')]),
      say=("Chín giờ tối, chú Sáu nhắn thêm một dòng. Năm hai nghìn không trăm mười chín chú chặt một héc ta. Chú chỉ kể chuyện của chú thôi, nhà nào tính theo nhà đó. "
           "Anh Tư trả lời: dạ, cháu tính kỹ rồi chú.")),
 dict(k='end', cap=('GIÁ ĐỨNG YÊN 12 THÁNG', 'NHÀ ANH CHỊ Ở NHÓM NÀO?'), cols=CC,
      say=("Kỷ lục xuất khẩu là kỷ lục của cả ngành, còn tiền trong túi nhà vườn đi theo giá từng ký. Còn anh chị, nếu giá nông sản hay thu nhập chính của nhà mình đứng yên ở mức hôm nay thêm mười hai tháng, nhà mình ở nhóm nào: vẫn dư, vừa đủ, hay không đủ?")),
]
import ql_post; S = ql_post.tach(S, max_tu=50, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Giá Cà Phê Hôm Nay Mất 11.000 Đồng/Kg: Kỷ Lục Mà Vẫn Hụt?'
MT = ("NÓNG: giá cà phê Tây Nguyên tuần qua mất hơn 11.000 đồng/kg, còn 71.200–72.000 đồng/kg – thấp nhất gần 3 năm (TTXVN 22/11/2026). Sáng 23/11, Đắk Lắk quanh 71.800 đồng/kg, cùng ngày năm ngoái 112.500. "
      "Lạ là niên vụ vừa rồi cà phê Việt Nam xuất khẩu kỷ lục 8,5 tỷ USD. Vì sao bán nhiều mà nhà vườn hụt tiền, thế giới dư bao nhiêu, lần trước năm 2019 ra sao, và phép thử cho túi tiền gia đình.\n\n"
      "Nguồn số liệu:\n"
      "• Bnews/TTXVN và VietnamPlus 22/11/2026: Tây Nguyên 71.200–72.000 đ/kg, giảm 11.000–11.200 đ/kg trong tuần (trên 13%), thấp nhất gần 3 năm; robusta London kỳ hạn 1/2027 2.978 USD/tấn, mất mốc 3.000; vụ mới VN ra thị trường khối lượng lớn; real Brazil yếu; USDA: Colombia 2026-27 +5,9% lên 13,4 triệu bao; ICO 2025/26: sản lượng 183,6 triệu bao (+4,4%), tiêu thụ 180,6 triệu bao (−0,9%); VN chiếm 14,2% xuất khẩu cà phê hoà tan toàn cầu (Brazil 11,2%); chế biến sâu ~1,5 tỷ USD (+14%); nhà máy hoà tan đủ đơn chạy hết công suất đến hết quý I/2027 (Phó Chủ tịch VICOFA)\n"
      "• Thương Trường 23/11/2026: Đắk Lắk, Gia Lai quanh 71.800 đ/kg; chi phí nhân công, vật tư cao, biên lợi nhuận thu hẹp\n"
      "• Báo Văn hoá, Báo Lâm Đồng 23/11/2025: Đắk Lắk 112.500 đ/kg\n"
      "• CafeF 20/10/2026 (VICOFA): niên vụ 2025-2026 xuất khẩu 1,8 triệu tấn, 8,5 tỷ USD – cao nhất từ trước tới nay; lượng +21%, kim ngạch +1%; chế biến sâu ~142.600 tấn, ~1,5 tỷ USD\n"
      "• CafeF 15/10/2026 (Bộ NN&MT): 9 tháng 2026 giá xuất khẩu bình quân ~4.537 USD/tấn, giảm gần 20%\n"
      "• Doanh nghiệp Hội nhập 27/3/2025: Đắk Lắk 135.500 đ/kg (kỷ lục); VOH 12/12/2019: 32.600–33.200 đ/kg, niên vụ 2018-19 xuất khẩu gần 3 tỷ USD, kim ngạch giảm hơn 14%, nhiều vườn chặt bỏ chuyển cây khác; Nông nghiệp & Môi trường 18/3/2020: 29.700–30.200 đ/kg\n"
      "• Tự tính: 71.800/112.500 → giảm khoảng 36%; 71.800/135.500 ≈ 53% đỉnh; dư 3/183,6 triệu bao ≈ 1,6%. Vườn anh Tư 4 tấn nhân là GIẢ ĐỊNH: 4.000 kg × 112.500 = 450 triệu; × 71.800 = 287,2 triệu; hụt 162,8 triệu\n\n"
      "Giá hàng hoá và túi tiền gia đình: https://chungkhoanhuynguyen.com/hoc/\n"
      "Cần trao đổi riêng về kế hoạch tài chính: Zalo 0365.188.286\n\n"
      "Nhân vật anh Tư, Linh, chú Sáu là hư cấu; số liệu là thật theo nguồn trên.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-23', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['giá cà phê hôm nay', 'giá cà phê', 'cà phê Tây Nguyên', 'giá cà phê Đắk Lắk', 'xuất khẩu cà phê', 'robusta', 'nông sản', 'giá nông sản', 'tin nóng tài chính', 'cà phê 2026'],
    bia_hook=['1 NĂM: 112.500', 'CÒN 71.800'], badge='CÀ PHÊ/KG SO NĂM NGOÁI',
    bia_anh='Coffee beans drying||Coffee beans drying',
    bia_hook_b=['MỘT TUẦN', 'MẤT 11.000'], badge_b='THẤP NHẤT GẦN 3 NĂM',
    bia_hook_c=['KỶ LỤC 8,5 TỶ', 'VẪN HỤT TIỀN?'], badge_c='XUẤT KHẨU CÀ PHÊ',
    reel_hook='CÀ PHÊ MẤT 11.000 ĐỒNG/KG|XUẤT KHẨU KỶ LỤC MÀ HỤT TIỀN???',
    fb_post=("Giá cà phê mất hơn 11.000 đồng/kg chỉ trong 1 tuần ☕\n\n👉 Đắk Lắk sáng nay quanh 71.800 đồng/kg, cùng ngày năm ngoái 112.500\n👉 Niên vụ vừa rồi xuất khẩu kỷ lục 8,5 tỷ USD\n"
             "👉 Nhưng bán nhiều hơn 21%, tiền thu về chỉ hơn 1%\n\nNếu giá đứng yên 12 tháng, nhà anh chị ở nhóm nào?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 23/11: giá cà phê mất hơn 11.000 đồng/kg trong 1 tuần, xuất khẩu kỷ lục mà nhà vườn hụt tiền (NV1B 23/11/2026).\n"
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
print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dien thoai/giay %d/%d' % (dt, len(S)), 'tieu de', len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
try:
    import xung_ho
    for i, c in enumerate(S, 1):
        if xung_ho.le_phep(c['say']) != c['say']: print('XUNG_HO doi canh', i)
except Exception as e: print('xung_ho?', e)
