# -*- coding: utf-8 -*-
# NV1 14/11/2026 00:40 – VIDEO DÀI kênh chính, "câu hỏi lớn": Việt Nam có thành Thái Lan thứ hai? (cặp với reel RV1411TL).
# Lý do chọn: data/view/xu_huong.md tuần tới 13/11: "Tăng trưởng trên 10% suốt 5 năm: VN thành Hàn Quốc hay Thái Lan thứ hai?" ~95 nghìn view,
#   "Kinh tế VN vs Thái Lan: vì sao Thái Lan vẫn giàu hơn?" ~57 nghìn; kênh mình 7 ngày chưa làm (đã làm: nợ công, GDP-lương, xuất khẩu, lãi suất, đô la).
# Nguồn và SỐ TỰ TÍNH:
#  - Tiền Phong 9/7/2026 ("Vì sao Thái Lan tăng trưởng 13,3%, sau gần 40 năm chưa lọt nhóm thu nhập cao?", số Ngân hàng Thế giới):
#    Thái Lan GDP +13,3% năm 1988, trên 10% liên tục 1987–1990; 1997 −2,8%; 1998 −7,6%; 2020 −6,1%; nay khoảng 2%/năm;
#    thả nổi baht 2/7/1997; GNI bình quân đầu người 2025: Thái Lan khoảng 7.690 USD, Việt Nam 4.970 USD; ngưỡng thu nhập cao 14.375 USD;
#    Việt Nam vào nhóm thu nhập trung bình cao năm 2025, mục tiêu thu nhập cao năm 2045; Hàn Quốc tăng 7–10%/năm 1970–1996, vào OECD 1996.
#  - 7.690 / 4.970 = 1,547 → Thái Lan cao hơn khoảng 55% (tự tính).
#  - RBA (Ngân hàng Trung ương Úc) RDP 9805, 1998: baht mất khoảng một nửa giá trị so với USD tới đáy tháng 1/1998; giá cổ phiếu Thái giảm hơn 60% từ đỉnh đầu năm 1994.
#  - IMF WEO 10/2026 (TNGlobal 13/10/2026): tăng trưởng 2026 Việt Nam 8,4%, Malaysia 5,2%, Indonesia 5,1%, Thái Lan 2,1% (2027: Thái 2,1%, VN 7,5%).
#  - Nợ hộ gia đình Thái Lan quý 4/2025: 86,7% GDP, 12,72 nghìn tỷ baht, tăng chủ yếu do vay tiêu dùng cá nhân (SCB EIC, The Nation 15/4/2026); quý 1/2026: 85,9% (The Nation 15/7/2026).
#  - The Nation 28/9/2025: Thái Lan có hơn 20% dân số từ 60 tuổi từ năm 2023, dự báo 28% năm 2033; gần một nửa người cao tuổi không có tiết kiệm.
#  - Cục Thống kê – UNFPA, Dự báo dân số 2024–2074 (Tuổi Trẻ 27/1/2026): 14,2 triệu người từ 60 tuổi năm 2024, 20,9 triệu năm 2034; Việt Nam thành dân số già năm 2034; dân số vàng kết thúc khoảng 2036.
#  - WiData/TCTK: GDP thực Việt Nam 2025 +8,02% (281279); quý 3/2026 +9,95% (80042).
#  - PHÉP TÍNH (em tự tính, giả định ngưỡng 14.375 USD đứng yên, thu nhập bình quân tính bằng USD tăng đều): số năm = ln(14.375/4.970)/ln(1+g):
#    g=7% → 15,7 năm (khoảng 2041); g=5% → 21,8 năm (khoảng 2047); g=2% → 53,6 năm; Thái Lan từ 7.690 USD với g=2% → 31,6 năm (khoảng 2057);
#    để kịp 2045 (20 năm) cần g ≈ 5,5% mỗi năm.
#  - Bảng lương anh Somchai là GIẢ ĐỊNH minh hoạ: lương 25.000 baht, trả góp xe 8.000, thẻ tín dụng 4.500 → trả nợ 12.500 = 50% lương.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261114_0040'
KEY = 'CH1811TL'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
# v2: 'ov:Bangkok skyline' ra ảnh Singapore (Esplanade) và Hong Kong (IFC) – dùng đích danh file Commons đã soát là Bangkok
BK1 = 'File:Bangkok_Skyline_from_Movenpick_Hotel,_Asok,_Bangkok_at_night.jpg'
BK2 = 'File:Bangkok_-_City_skyline_at_sunset.JPG'
BK3 = BK2   # v3: Bangkok_Panorama có biển AIA (logo DN) ở cảnh tiêu cực – bỏ
BK4 = 'File:Twilight_over_the_modern_city_skyline_in_Ratchadamri_district,_Bangkok,_Thailand,_July_2019_-_Flickr_-_sergei.gussev.jpg'
BK5 = 'File:Bangkok,_Thailand,_Benjakitti_Park,_2024.jpg'
NHA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
SGD = 'ov:Ho Chi Minh City Stock Exchange||Bitexco Financial Tower'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('THÁI LAN TỪNG TĂNG 13,3%', 'GIỜ KẸT Ở 2%'), cols=CR, noti=dict(gio='21:15', ngay='Thứ Ba', items=[
        ('Tin tức', 'IMF tháng 10', 'Năm 2026: Việt Nam tăng 8,4%, Thái Lan 2,1%', G_),
        ('Zalo', 'Somchai', 'Hồi bố tôi còn trẻ, Thái Lan cũng tăng 13% một năm đấy', V_),
        ('Zalo', 'Somchai', 'Rồi cả nhà tôi mất gần hết trong một năm', R_)]),
      say=("Năm 1988, Thái Lan tăng trưởng mười ba phẩy ba phần trăm. Gần bốn mươi năm sau, họ vẫn chưa thành nước giàu. "
           "Tối nay anh Hưng, kỹ sư một nhà máy Nhật ở Bình Dương, đọc tin: năm nay Việt Nam được dự báo tăng tám phẩy bốn phần trăm, Thái Lan chỉ hai phẩy một phần trăm. "
           "Anh gửi tin cho Somchai, người bạn Thái học cùng khóa đào tạo. Somchai trả lời: hồi bố anh ấy còn trẻ, Thái Lan cũng tăng như vậy. Rồi cả nhà mất gần hết chỉ trong một năm.")),
 dict(k='bignum', anh=BK1, cap=('NHANH HƠN CẢ VIỆT NAM', 'RỒI KẸT GẦN 40 NĂM'), cols=CR, value=13.3, fmt='{:,.1f}', unit='%', top='THÁI LAN NĂM 1988', sub='Nay còn khoảng 2% mỗi năm', col=RED,
      say=("Mười ba phẩy ba phần trăm. Nhanh hơn cả Việt Nam bây giờ. Vậy mà đến hôm nay, Thái Lan vẫn đứng ngoài cửa nhóm nước thu nhập cao, tăng trưởng chỉ còn khoảng hai phần trăm, "
           "các gia đình Thái gánh khoản nợ gần chín mươi phần trăm GDP. Việt Nam sẽ thành Hàn Quốc, hay thành Thái Lan thứ hai? Và chuyện đó liên quan gì tới túi tiền nhà mình?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='cards', ch='Chương 1 – Con hổ từng chạy nhanh nhất châu Á', anh=BK2, cap=('THÁI LAN THỜI HOÀNG KIM', 'TIỀN PHONG, SỐ NGÂN HÀNG THẾ GIỚI'), cols=CC, moc=True,
      cards=[('+13,3%', 'GDP Thái Lan năm 1988', 'Cao nhất thời hoàng kim'), ('Trên 10%', 'Liên tục từ 1987 tới 1990', 'Bốn năm hai chữ số'), ('7.690 USD', 'Thu nhập mỗi người năm 2025', 'Vẫn chưa thành nước giàu')],
      say=("Cuối những năm tám mươi, Thái Lan là ngôi sao của châu Á. Theo số Ngân hàng Thế giới mà báo Tiền Phong tổng hợp, từ năm 1987 đến năm 1990, kinh tế Thái tăng trên mười phần trăm liên tục. Đỉnh là mười ba phẩy ba phần trăm vào năm 1988. "
           "Nhà máy Nhật đổ vào Bangkok, giống nhà máy nước ngoài đổ vào Bắc Ninh, Bình Dương bây giờ. "
           "Thế nhưng năm 2025, thu nhập bình quân mỗi người Thái mới khoảng bảy nghìn sáu trăm chín mươi đô la. Ngưỡng nước giàu là mười bốn nghìn ba trăm bảy mươi lăm đô la. Họ mới đi được hơn nửa đường.")),
 dict(k='bars', anh=HN, cap=('THU NHẬP MỖI NGƯỜI 2025', 'THÁI LAN HƠN 55%'), cols=CC, moc=True,
      bars=[('Việt Nam', 4970, GOLD, '4.970 USD'), ('Thái Lan', 7690, GREEN, '7.690 USD'), ('Ngưỡng nước giàu', 14375, RED, '14.375 USD')],
      say=("Còn Việt Nam? Năm 2025, thu nhập bình quân mỗi người Việt khoảng bốn nghìn chín trăm bảy mươi đô la, vừa bước vào nhóm thu nhập trung bình cao. "
           "Thái Lan vẫn cao hơn khoảng năm mươi lăm phần trăm, em tự tính. Việt Nam đang đứng gần chỗ Thái Lan từng đứng, và đang chạy nhanh như Thái Lan thời hoàng kim.")),
 dict(k='chat', cap=('"LƯƠNG TÔI GẤP RƯỠI ÔNG', 'MÀ THÁNG NÀO CŨNG HẾT"'), cols=CC, moc=True, chat=dict(ten='Somchai', tv='Đang hoạt động', gio='21:30', mau=X_, msgs=[
        ('me', 'Nghe nói lương bên ông cao hơn bên tôi nhiều'),
        ('Somchai', 'Gấp rưỡi ông đấy, nhưng tháng nào cũng hết sạch'),
        ('Somchai', 'Xe trả góp, thẻ tín dụng, rồi gửi về cho bố mẹ')]),
      say=("Anh Hưng hỏi đùa: nghe nói lương bên đó cao hơn nhiều. Somchai trả lời: gấp rưỡi đấy, nhưng tháng nào cũng hết sạch. Xe trả góp, thẻ tín dụng, rồi gửi về cho bố mẹ. "
           "Một đất nước giàu hơn, lương cao hơn, sao người trẻ lại kẹt như vậy? Để hiểu, phải quay lại năm 1997.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='giay', ch='Chương 2 – Ngày 2 tháng 7 năm 1997', cap=('NGÀY BAHT BỊ THẢ NỔI', 'MẤT MỘT NỬA GIÁ TRỊ'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA CÚ SẬP 1997', so='Tổng hợp: Ngân hàng Trung ương Úc 1998, Tiền Phong 2026', dau='ĐÃ XẢY RA', dieu=[
        ('2/7/1997: Thái Lan thả nổi đồng baht', '2/7/1997'),
        ('Tới tháng 1/1998: baht mất khoảng một nửa', 'MẤT 1/2'),
        ('Cổ phiếu giảm hơn 60% từ đỉnh đầu 1994', 'HƠN 60%'),
        ('GDP năm 1998 so với năm trước', 'GIẢM 7,6%')]),
      say=("Ngày hai tháng bảy năm 1997, Thái Lan buộc phải thả nổi đồng baht. Theo nghiên cứu của Ngân hàng Trung ương Úc năm 1998, chỉ sau vài tháng, đồng baht mất khoảng một nửa giá trị so với đô la. "
           "Giá cổ phiếu Thái đã giảm hơn sáu mươi phần trăm so với đỉnh đầu năm 1994. Kinh tế giảm hai phẩy tám phần trăm trong năm 1997, rồi giảm tiếp bảy phẩy sáu phần trăm trong năm 1998.")),
 dict(k='call', cap=('"BỐ TÔI MẤT VIỆC', 'NỢ ĐÔ LA THÌ TĂNG GẤP ĐÔI"'), cols=CR, moc=True, call=dict(ten='Somchai', phu='Gọi video từ Bangkok', mau=R_, loi=[
        'Bố tôi làm cho một công ty xây dựng', 'Công ty vay đô la, baht mất giá là sập']),
      say=("Somchai gọi video, giọng chậm hẳn lại. Bố anh ấy hồi đó làm cho một công ty xây dựng ở Bangkok, công ty vay đô la để xây chung cư. Baht mất một nửa giá trị, món nợ tính ra tiền baht gần như tăng gấp đôi. "
           "Công ty đóng cửa, bố anh ấy mất việc, căn nhà trả góp cũng không giữ được. Cả nhà làm lại từ đầu.")),
 dict(k='text', cap=('TĂNG NHANH BẰNG TIỀN VAY', 'THÌ NGÃ CŨNG RẤT ĐAU'), cols=CR, anh=BK2,
      say=("Anh chị thấy đấy, khi kinh tế tăng quá nóng bằng tiền đi vay, nhất là vay ngoại tệ ngắn hạn đổ vào bất động sản, chỉ cần dòng tiền quay đầu một lần là mọi thứ sụp rất nhanh. "
           "Nhưng cú sập chưa phải phần đáng sợ nhất. Đáng sợ nhất là chuyện xảy ra trong hai mươi lăm năm sau đó.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='bars', ch='Chương 3 – Kẹt ở hai phần trăm', anh=BK4, cap=('DỰ BÁO TĂNG TRƯỞNG 2026', 'IMF THÁNG 10/2026'), cols=CR, moc=True,
      bars=[('Việt Nam', 8.4, GREEN, '8,4%'), ('Malaysia', 5.2, GOLD, '5,2%'), ('Thái Lan', 2.1, RED, '2,1%')],
      say=("Thái Lan hồi phục sau khủng hoảng, nhưng không chạy nhanh lại được nữa. Báo cáo tháng mười năm nay của Quỹ Tiền tệ Quốc tế dự báo: Việt Nam tăng tám phẩy bốn phần trăm, "
           "Malaysia năm phẩy hai phần trăm, còn Thái Lan chỉ hai phẩy một phần trăm, thuộc nhóm chậm nhất Đông Nam Á. Báo chí khu vực gọi Thái Lan là người bệnh của châu Á.")),
 dict(k='bignum', anh=BK5, cap=('NỢ CỦA CÁC GIA ĐÌNH THÁI', 'BẰNG 86,7% GDP'), cols=CR, moc=True, value=86.7, fmt='{:,.1f}', unit='%', top='NỢ HỘ GIA ĐÌNH / GDP', sub='Thái Lan quý 4/2025, SCB EIC', col=RED,
      say=("Và đây là cú lật thứ hai. Cuối năm 2025, tổng nợ của các hộ gia đình Thái Lan bằng tám mươi sáu phẩy bảy phần trăm GDP cả năm, theo trung tâm nghiên cứu kinh tế SCB E I C. "
           "Đáng lo hơn, phần nợ tăng thêm chủ yếu là vay tiêu dùng, tức là vay để trang trải chi tiêu hằng ngày, không phải để làm ăn.")),
 dict(k='giay', cap=('BẢNG LƯƠNG CỦA SOMCHAI', 'MỘT NỬA ĐÃ LÀ TRẢ NỢ'), cols=CR, moc=True, giay=dict(tieu_de='BẢNG LƯƠNG THÁNG 10 – SOMCHAI', so='Em giả định để minh hoạ, đơn vị baht', dau='ĐÃ TRỪ', dieu=[
        ('Lương thực nhận: 25.000 baht', '25.000'),
        ('Trả góp xe bán tải: 8.000 baht', '8.000'),
        ('Thẻ tín dụng: 4.500 baht', '4.500'),
        ('Trả nợ chiếm bao nhiêu phần lương', '50%')]),
      say=("Somchai chụp bảng lương gửi anh Hưng, số này em giả định để minh hoạ. Lương thực nhận hai mươi lăm nghìn baht. "
           "Trả góp xe bán tải tám nghìn. Thẻ tín dụng bốn nghìn rưỡi. Đúng một nửa tiền lương đã đi trả nợ trước khi kịp mua bất cứ thứ gì. Phần còn lại lo ăn ở, và gửi về cho bố mẹ đã già.")),
 dict(k='cards', anh=BK1, cap=('GIÀ TRƯỚC KHI GIÀU', 'THE NATION 9/2025'), cols=CR, moc=True,
      cards=[('Hơn 20%', 'Dân số từ 60 tuổi, năm 2023', 'Đã thành xã hội già'), ('28%', 'Dự báo cho năm 2033', 'Già đi rất nhanh'), ('Gần 1/2', 'Người già không có tiết kiệm', 'Con cái phải gánh')],
      say=("Vì sao phải gửi tiền về cho bố mẹ? Vì Thái Lan đã già trước khi kịp giàu. Từ năm 2023, hơn hai mươi phần trăm dân số Thái từ sáu mươi tuổi trở lên, và được dự báo lên hai mươi tám phần trăm vào năm 2033. "
           "Báo The Nation dẫn ý kiến chuyên gia: gần một nửa người cao tuổi Thái không có tiền tiết kiệm. Người trẻ vừa trả nợ của mình, vừa gánh tuổi già của cha mẹ.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='giay', ch='Chương 4 – Việt Nam có đang đi lại con đường đó?', cap=('ĐỒNG HỒ DÂN SỐ VIỆT NAM', 'CÒN KHOẢNG 10 NĂM'), cols=CR, moc=True, giay=dict(tieu_de='DỰ BÁO DÂN SỐ VIỆT NAM 2024–2074', so='Cục Thống kê – Quỹ Dân số Liên hợp quốc', dau='DỰ BÁO', dieu=[
        ('Người từ 60 tuổi năm 2024: 14,2 triệu', '14,2 TR'),
        ('Năm Việt Nam thành nước dân số già', '2034'),
        ('Dân số vàng kết thúc, sớm hơn 3 năm', '2036')]),
      say=("Giờ quay về Việt Nam. Theo báo cáo dự báo dân số do Cục Thống kê làm cùng Quỹ Dân số Liên hợp quốc, năm 2024 cả nước có khoảng mười bốn phẩy hai triệu người từ sáu mươi tuổi trở lên. "
           "Tới năm 2034, Việt Nam chính thức thành nước có dân số già. Thời kỳ dân số vàng, lúc người đi làm đông hơn hẳn người phụ thuộc, dự kiến kết thúc khoảng năm 2036, sớm hơn ba năm so với dự báo cũ.")),
 dict(k='checklist', anh=TP, cap=('VIỆT NAM GIỐNG THÁI LAN', 'Ở 3 ĐIỂM'), cols=CR, moc=True,
      items=[('Tăng nhanh nhờ nhà máy FDI', GOLD),
             ('Xuất khẩu là động cơ chính', GOLD),
             ('Dân số vàng sắp hết', RED)],
      say=("Đặt hai nước cạnh nhau, có ba điểm giống đến giật mình. Một: tăng trưởng nhanh nhờ nhà máy nước ngoài. Hai: xuất khẩu là động cơ chính. "
           "Ba: cửa sổ dân số vàng đang khép lại. Khác biệt là Việt Nam còn khoảng mười năm, và mười năm đó dùng thế nào sẽ quyết định mình thành ai.")),
 dict(k='bars', anh=TP, cap=('BAO NHIÊU NĂM TỚI NGƯỠNG GIÀU?', 'EM TỰ TÍNH'), cols=CC, moc=True,
      bars=[('Tăng 7% mỗi năm', 15.7, GREEN, '16 năm'), ('Tăng 5% mỗi năm', 21.8, GOLD, '22 năm'), ('Tăng 2% như Thái', 53.6, RED, '54 năm')],
      say=("Em làm một phép tính. Từ bốn nghìn chín trăm bảy mươi đô la, nếu thu nhập bình quân tính bằng đô la tăng đều bảy phần trăm mỗi năm, Việt Nam cần khoảng mười sáu năm để chạm ngưỡng nước giàu. Tức là quanh năm 2041. "
           "Nếu chỉ tăng năm phần trăm, cần khoảng hai mươi hai năm, lỡ mục tiêu năm 2045. Nếu chậm lại hai phần trăm như Thái Lan bây giờ, cần hơn năm mươi năm. "
           "Em giả định ngưỡng đứng yên, cách tính có trong mô tả.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='cards', ch='Chương 5 – Con đường của Hàn Quốc', anh=SGD, cap=('PHƯƠNG ÁN KHÁC', 'HÀN QUỐC 1970 TỚI 1996'), cols=CC, moc=True,
      cards=[('7 đến 10%', 'Mỗi năm, từ 1970 tới 1996', 'Gần 30 năm liền'), ('1996', 'Hàn Quốc vào khối OECD', 'Bước qua ngưỡng giàu'), ('2045', 'Mục tiêu của Việt Nam', 'Còn 19 năm')],
      say=("Có một con đường khác. Hàn Quốc tăng trưởng bảy đến mười phần trăm gần như mỗi năm, từ năm 1970 đến năm 1996. Cũng trong năm 1996, họ được nhận vào khối các nước phát triển OECD. "
           "Khác biệt không nằm ở tốc độ một vài năm, mà ở chỗ họ giữ được tốc độ đó gần ba mươi năm, đi từ lắp ráp lên làm công nghệ.")),
 dict(k='text', cap=('TRỞ THÀNH NƯỚC NÀO', 'NẰM Ở 10 NĂM TỚI'), cols=CC, anh=TP,
      say=("Nhưng với mỗi gia đình, câu hỏi nhỏ hơn và gần hơn. Nhà nào vay để tiêu, nhà đó đi theo đường của Somchai. "
           "Nhà nào dùng những năm thu nhập tăng nhanh để học thêm, để dành và tránh nợ tiêu dùng, nhà đó đi đường thứ hai, dù đất nước đi đường nào.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='chat', ch='Chương 6 – Kế hoạch của nhà anh Hưng', cap=('KẾ HOẠCH CỦA NHÀ HƯNG', 'TRƯỚC KHI DÂN SỐ VÀNG HẾT'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:40', mau=G_, msgs=[
        ('me', 'Thôi, anh chưa đổi xe trả góp nữa'),
        ('Vợ', 'Ừ, tiền trả nợ đừng quá 1/3 lương'),
        ('me', 'Phần lương tăng thêm, mình để dành cho lúc bố mẹ già'),
        ('Vợ', 'Còn anh đi học tiếng Nhật cho lên tổ trưởng')]),
      say=("Anh Hưng nhắn cho vợ: thôi, anh chưa đổi xe trả góp nữa. Vợ anh đáp: ừ, tiền trả nợ đừng quá ba mươi ba phần trăm tiền lương. "
           "Anh nhắn tiếp: phần lương tăng thêm, mình để riêng cho lúc bố mẹ già. Vợ anh thêm: còn anh đi học tiếng Nhật cho lên tổ trưởng. Thu nhập tăng nhanh nhất vẫn đến từ tay nghề.")),
 dict(k='checklist', anh=NHA, cap=('PHÉP THỬ CỦA ANH CHỊ', 'TRẢ NỢ CHIẾM BAO NHIÊU LƯƠNG?'), cols=CC, moc=True,
      items=[('Dưới 30%: còn thở được', GREEN),
             ('30 đến 50%: bắt đầu căng', GOLD),
             ('Trên 50%: như Somchai', RED)],
      say=("Và đây là phép thử anh chị tự làm được tối nay. Cộng mọi khoản trả nợ mỗi tháng, trả góp nhà, xe, điện thoại, thẻ tín dụng, rồi chia cho tổng thu nhập. "
           "Dưới ba mươi phần trăm thì còn thở được. Từ ba mươi đến năm mươi phần trăm là bắt đầu căng. Trên năm mươi phần trăm, nhà mình đang sống giống Somchai. Đây là mốc em đặt để tự soi, không phải quy định.")),
 dict(k='checklist', ch='Chương 7 – Nhà đầu tư nên theo dõi gì?', anh=SGD, cap=('3 CON SỐ CẦN THEO DÕI', 'ĐỂ BIẾT VIỆT NAM ĐI ĐƯỜNG NÀO'), cols=CC, moc=True,
      items=[('Tăng trưởng có giữ trên 5,5%?', GREEN),
             ('Nợ vay tiêu dùng tăng nhanh?', GOLD),
             ('Doanh nghiệp Việt có lớn lên?', GREEN)],
      say=("Với anh chị có thêm khoản đầu tư, em gợi ý theo dõi ba điều. Một: thu nhập có giữ được mức tăng trên năm phẩy năm phần trăm qua nhiều năm không, đó là tốc độ cần để kịp năm 2045. "
           "Hai: nợ vay tiêu dùng có tăng nhanh hơn thu nhập không. Ba: lợi nhuận doanh nghiệp Việt có lớn lên cùng nền kinh tế không. Lợi nhuận từng quý của hơn bốn trăm mã có miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn từ Bangkok', cap=('"ĐỪNG GIÀ', 'TRƯỚC KHI GIÀU NHƯ BỌN TÔI"'), cols=CC, moc=True, chat=dict(ten='Somchai', tv='Đang hoạt động', gio='23:30', mau=X_, msgs=[
        ('Somchai', 'Nước ông đang chạy nhanh như nước tôi ngày xưa'),
        ('Somchai', 'Đừng già trước khi giàu như bọn tôi nhé'),
        ('me', 'Cảm ơn ông. Tôi bắt đầu từ nhà mình trước')]),
      say=("Gần nửa đêm, Somchai nhắn thêm: nước Việt Nam đang chạy nhanh như Thái Lan ngày xưa, đừng già trước khi giàu nhé. Anh Hưng trả lời: cảm ơn, mình bắt đầu từ nhà mình trước. "
           "Tăng trưởng tám đến chín phần trăm là cơ hội của cả một thế hệ. Nhưng Thái Lan cho thấy, cơ hội đó có hạn dùng.")),
 dict(k='end', cap=('HÀN QUỐC HAY THÁI LAN', 'THỨ HAI?'), cols=CC,
      say=("Còn anh chị nghĩ sao: Việt Nam sẽ thành Hàn Quốc, hay thành Thái Lan thứ hai? Và khoản trả nợ mỗi tháng của nhà mình đang chiếm bao nhiêu phần thu nhập? Kể cho em và mọi người ở phần bình luận nhé. "
           "Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Việt Nam Có Thành Thái Lan Thứ Hai? Từng Tăng 13,3% Một Năm, Giờ Kẹt Ở 2% Và Nợ 86,7% GDP'
MT = ("Năm 1988 Thái Lan tăng trưởng 13,3%, nhanh hơn cả Việt Nam bây giờ. Gần 40 năm sau, họ vẫn chưa thành nước giàu: tăng trưởng còn khoảng 2%, nợ hộ gia đình bằng 86,7% GDP, hơn 20% dân số đã từ 60 tuổi. "
      "Việt Nam đang tăng 8–10% và có 3 điểm giống Thái Lan. Câu chuyện của anh Hưng và người bạn Thái Somchai, cùng phép thử cho chính gia đình anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• Tiền Phong 9/7/2026 (số Ngân hàng Thế giới): Thái Lan GDP +13,3% năm 1988, trên 10% liên tục 1987–1990; 1997 −2,8%; 1998 −7,6%; thả nổi baht 2/7/1997; GNI bình quân đầu người 2025: Thái Lan khoảng 7.690 USD, Việt Nam 4.970 USD; ngưỡng thu nhập cao 14.375 USD; Hàn Quốc tăng 7–10%/năm giai đoạn 1970–1996, vào OECD 1996\n"
      "• Ngân hàng Trung ương Úc (RBA), RDP 9805 (1998): baht mất khoảng một nửa giá trị so với USD tới đáy tháng 1/1998; cổ phiếu Thái giảm hơn 60% từ đỉnh đầu 1994\n"
      "• IMF, Triển vọng kinh tế thế giới 10/2026 (TNGlobal 13/10/2026): tăng trưởng 2026 Việt Nam 8,4%, Malaysia 5,2%, Thái Lan 2,1%\n"
      "• SCB EIC (The Nation 15/4/2026): nợ hộ gia đình Thái Lan quý 4/2025 là 12,72 nghìn tỷ baht, 86,7% GDP, tăng chủ yếu do vay tiêu dùng cá nhân\n"
      "• The Nation 28/9/2025: hơn 20% dân số Thái từ 60 tuổi (từ 2023), dự báo 28% năm 2033; gần một nửa người cao tuổi không có tiết kiệm\n"
      "• Cục Thống kê – UNFPA, Dự báo dân số 2024–2074 (Tuổi Trẻ 27/1/2026): 14,2 triệu người từ 60 tuổi năm 2024; Việt Nam thành dân số già năm 2034; dân số vàng kết thúc khoảng 2036\n"
      "• Tổng cục Thống kê (WiData): GDP Việt Nam 2025 +8,02%; quý 3/2026 +9,95%\n"
      "• Tự tính: 7.690/4.970 = 1,55 (Thái Lan cao hơn khoảng 55%). Số năm tới ngưỡng = ln(14.375/4.970)/ln(1+g), giả định ngưỡng đứng yên: g=7% → khoảng 16 năm; g=5% → 22 năm; g=2% → 54 năm; kịp 2045 cần g khoảng 5,5%\n"
      "• Bảng lương của Somchai là giả định minh hoạ (25.000 baht, trả góp 8.000 + thẻ 4.500 = 50% lương)\n\n"
      "Tra lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật anh Hưng, vợ anh và Somchai là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-18', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['Việt Nam và Thái Lan', 'bẫy thu nhập trung bình', 'kinh tế Thái Lan', 'khủng hoảng 1997', 'nợ hộ gia đình', 'già hóa dân số', 'GDP Việt Nam', 'kinh tế Việt Nam', 'vĩ mô'],
    bia_hook=['THÁI LAN 13,3%', 'GIỜ CÒN 2%???'], badge='VIỆT NAM CÓ THEO?',
    bia_anh='Ho Chi Minh City skyline night||Hanoi skyline night',
    bia_hook_b=['NỢ 86,7% GDP', 'GIÀ TRƯỚC GIÀU'], badge_b='THÁI LAN · SCB EIC',
    bia_hook_c=['HÀN QUỐC', 'HAY THÁI LAN?'], badge_c='CÂU HỎI LỚN',
    reel_hook='THÁI LAN TỪNG TĂNG 13%|VIỆT NAM CÓ ĐI VẾT XE ĐỔ???',
    fb_post=("Việt Nam có thành Thái Lan thứ hai? 🇹🇭\n\n👉 Thái Lan năm 1988 tăng 13,3%, nay chỉ khoảng 2%\n👉 Nợ hộ gia đình Thái: 86,7% GDP\n"
             "👉 Việt Nam thành dân số già năm 2034, dân số vàng hết khoảng 2036\n\nKhoản trả nợ mỗi tháng nhà anh chị chiếm bao nhiêu phần thu nhập?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: Việt Nam có thành Thái Lan thứ hai (NV1 14/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
# bảng phân cảnh (xuong_phim_chuan_1311): mỗi cảnh – loại, mô tả, cảm xúc, tiếng động
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
