# -*- coding: utf-8 -*-
# NV1B 25/11/2026 – VIDEO NÓNG kênh chính: El Nino rất mạnh + hạn mặn miền Tây mùa khô 2026–2027 + giá gạo (tin hội thảo gạo xanh Cần Thơ 24/11/2026)
#   – cú lật 1: giá gạo xuất khẩu lên cao nhất gần 2 năm, nhưng giá gạo trong nước tháng 10 lại GIẢM (−0,92%).
#   – cú lật 2: mùa khô 2019–2020 mặn còn rộng hơn 2016, mà lúa thiệt hại chỉ bằng 14% – nhờ dự báo sớm, xuống giống sớm.
#   – cú lật 3: lần gạo tăng thật (Ấn Độ cấm 7/2023) thì bàn ăn trong nước đắt lên rõ vào năm 2024 (gạo +15,93%).
# KEY NONG2511A. Khác NONG2311B (cà phê), CH2911SR (sầu riêng).
# Nguồn:
#  - BNEWS/TTXVN 24/11/2026 20:50 "Điểm tin kinh tế VN nổi bật": hội thảo "Gạo xanh Việt Nam" (Cần Thơ, 24/11), Phó Viện trưởng Viện Chiến lược, Chính sách nông nghiệp và môi trường:
#    "El Nino có khả năng xuất hiện vào cuối năm 2026 và đầu năm 2027"; sản lượng gạo Ấn Độ có thể giảm khoảng 4,6%, Thái Lan 1,9%, Brazil khoảng 3%.
#  - VietnamPlus 15/10/2026: Trung tâm Dự báo KTTV quốc gia – xác suất 96% El Nino giữ cường độ rất mạnh từ 11/2026 đến 1/2027; mưa hạ lưu Mê Công tháng 1/2027 thấp hơn TBNN 30–60%.
#  - Nhân Dân 8/11/2026: khoảng 350.000 ha lúa đông xuân có nguy cơ hạn mặn.
#  - Tiền Phong 5/10/2026 (Viện Khoa học thủy lợi miền Nam, ranh mặn 4 g/l): tháng 12/2026 vào 30–40 km; tháng 1–2/2027 50–65 km, tương đương 2016; nửa đầu tháng 3 55–70 km, cao hơn 2016;
#    khuyến cáo xuống giống đông xuân sớm, hoàn thành trong tháng 12/2026, chậm nhất nửa đầu tháng 1/2027; trữ nước sớm.
#  - Business Recorder 5/11/2026 + VietnamPlus 7/11/2026: gạo 5% tấm VN 480–490 USD/tấn, cao nhất từ 12/2024; Thái 490–495 cao nhất từ 1/2025.
#  - Reuters qua Hua Hin Localplus 22/11/2026: tuần tới 22/11 VN 475–485; Thái 505–510; Ấn Độ gạo trắng 395–400 USD/tấn.
#  - VietnamPlus 4/11/2026 (Bộ NN&MT): xuất khẩu gạo 10 tháng 6,8 triệu tấn (−4,6%), 3,31 tỷ USD (−9,7%), giá bình quân ~484 USD/tấn (−5,4%). (VietnamPlus 7/11: riêng tháng 10 475.000 tấn, +37,2%.)
#  - Báo Văn Hóa 12/11/2026: lúa tươi tại ruộng ĐBSCL 11/11: IR50404 6.200–6.300; OM5451 6.400–6.600; Đài Thơm 8 7.100–7.200 đồng/kg.
#  - Cục Thống kê (PDF CPI tháng 10/2026): lương thực −0,57% so tháng trước, +0,22% so cùng kỳ; gạo −0,92% "khi nguồn cung trong nước dồi dào"; gạo tẻ thường 14.600–16.500 đồng/kg.
#  - VietNamNet 22/6/2020: 2019–2020 lúa thiệt hại 58.400 ha = 14% diện tích bị ảnh hưởng 2015–2016 (405.000 ha); ~96.000 hộ khó khăn (2016: 210.000 hộ);
#    nhiễm mặn 4 g/l 1,68 triệu ha – hơn 2016 (SGGP 20/6/2020); bài học: dự báo tốt, đông xuân xuống giống sớm 10–20 ngày để né mặn.
#  - Bộ Công Thương 21/7/2023: Ấn Độ cấm xuất khẩu gạo trắng non-basmati từ 20/7/2023. VnExpress 5/12/2023: gạo VN 5% tấm 663 USD/tấn (4/12/2023), cao nhất nếu không tính 2008.
#  - Cục Thống kê – Tổng quan CPI năm 2024: bình quân 2024 gạo +15,93%, lương thực +12,19%, CPI chung +3,63%.
# SỐ TỰ TÍNH: 480/663 ≈ 0,72 → thấp hơn đỉnh khoảng 28%. Sổ chi tiêu GIẢ ĐỊNH: nhà 4 người 30 kg gạo/tháng × 16.500 = 495.000 đ;
#   nếu tăng như năm 2024 (+15,93%) → thêm 78.854 đ ≈ gần 80.000 đ/tháng. 58.400/405.000 = 14,4%.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261125_0830_nong'
KEY = 'NONG2511A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
LUA = 'File:Cau-can-tho-tuonglamphotos.jpg'
MEK = 'File:Can_Tho_City_-_Stadt_aus_Sicht_vom_Boot.jpg'
CON = 'ov:Container ship||Container ship'
GAO = 'File:White_rice_at_a_restaurant.jpg'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', short=True, cap=('GẠO BÁN RA NƯỚC NGOÀI ĐẮT LÊN', 'GẠO NGOÀI CHỢ LẠI RẺ ĐI'), cols=CR, noti=dict(gio='07:30', ngay='Thứ Tư', items=[
        ('Tin tức', 'Nông nghiệp', 'El Nino: sản lượng gạo Ấn Độ có thể giảm 4,6%, Thái Lan 1,9%', R_),
        ('Ba', 'Tin nhắn', 'Năm nay báo mặn vào sâu, ba tính xuống giống sớm nha con', X_)]),
      say=("Đầu tháng mười một, gạo Việt bán ra nước ngoài lên mức giá cao nhất gần hai năm. Vậy mà tháng mười, gạo ngoài chợ lại rẻ đi. "
           "Sáng nay, chị Ngọc ở thành phố Hồ Chí Minh đọc tin từ một hội thảo về gạo ở Cần Thơ hôm qua. Hiện tượng El Nino có khả năng kéo dài qua cuối năm nay và đầu năm sau. Sản lượng gạo của Ấn Độ có thể giảm khoảng bốn phẩy sáu phần trăm. "
           "Ngay dưới là tin nhắn của ba chị, đang trồng lúa ở Vĩnh Long: năm nay báo mặn vào sâu, ba tính xuống giống sớm nha con. Xuống giống là gieo lúa, gieo sớm để kịp gặt trước khi nước mặn lên. "
           "Chị Ngọc tự hỏi: có nên mua trữ gạo không?")),
 dict(k='bignum', anh=MEK, cap=('96% KHẢ NĂNG', 'EL NINO RẤT MẠNH TỚI THÁNG 1'), cols=CR, value=96, fmt='{:,.0f}', unit='%', top='KHẢ NĂNG EL NINO GIỮ MỨC RẤT MẠNH', sub='Từ tháng 11/2026 đến tháng 1/2027 (Trung tâm Dự báo KTTV quốc gia)', col=RED,
      say=("El Nino là khi nước biển ở giữa Thái Bình Dương nóng lên bất thường. Với miền Nam nước ta, nó thường kéo theo ít mưa, mùa khô dài, và nước mặn từ biển lấn sâu vào sông. "
           "Trung tâm Dự báo khí tượng thủy văn quốc gia đánh giá: khả năng El Nino giữ mức rất mạnh từ tháng mười một đến tháng một năm sau là chín mươi sáu phần trăm. "
           "Nghĩa là mùa khô tới nhiều khả năng ít mưa hơn bình thường. Câu hỏi là: nồi cơm nhà mình và ruộng lúa của ba chị sẽ ra sao?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Nước mặn sẽ vào tới đâu?', short=True, cap=('MẶN VÀO SÂU 50 ĐẾN 65 KM', 'THÁNG 1 VÀ 2 NĂM SAU'), cols=CR, moc=True, giay=dict(tieu_de='DỰ BÁO MẶN MÙA KHÔ TỚI', so='Ranh mặn 4 g/l. Viện Khoa học thủy lợi miền Nam (Tiền Phong 5/10)', dau='DỰ BÁO', dieu=[
        ('Tháng 12/2026: vào 30 đến 40 km.', 'THÁNG 12'),
        ('Tháng 1 và 2/2027: 50 đến 65 km.', 'NGANG 2016'),
        ('Nửa đầu tháng 3/2027: 55 đến 70 km.', 'THÁNG 3'),
        ('350.000 ha lúa đông xuân có nguy cơ.', 'NHÂN DÂN 8/11')]),
      say=("Nước mặn ở đây là nước biển chảy ngược vào sông, tới những đoạn sông người ta vẫn lấy nước tưới ruộng. "
           "Theo dự báo của Viện Khoa học thủy lợi miền Nam, tháng một và tháng hai năm sau, mặn có thể vào sâu năm mươi đến sáu mươi lăm cây số. Mức đó ngang với mùa hạn mặn năm 2016. "
           "Báo Nhân Dân cho biết khoảng ba trăm năm mươi nghìn héc ta lúa đông xuân, vụ lúa lớn nhất năm, gieo cuối năm và gặt đầu năm sau, có nguy cơ bị hạn mặn. Nếu mất mùa lớn, đó là chuyện của cả người trồng lẫn người ăn.")),
 dict(k='chat', cap=('"VẬY GẠO SẮP LÊN GIÁ?', 'EM MUA TRỮ VÀI BAO NHA?"'), cols=CR, moc=True, chat=dict(ten='Anh Khoa', tv='Đang hoạt động', gio='08:00', mau=V_, msgs=[
        ('me', 'Vậy gạo sắp lên giá hả anh? Em mua trữ vài bao nha?'),
        ('Anh Khoa', 'Giá gạo bán ra nước ngoài thì đang lên'),
        ('Anh Khoa', 'Nhưng tháng 10 giá gạo ngoài chợ lại giảm')]),
      say=("Chị Ngọc nhắn cho chồng, anh Khoa, người làm kho vận cho một công ty nông sản: vậy gạo sắp lên giá hả anh, em mua trữ vài bao nha? "
           "Anh Khoa trả lời: giá gạo bán ra nước ngoài thì đang lên. Nhưng tháng mười, giá gạo ngoài chợ lại giảm.")),
 dict(k='cards', anh=CON, cap=('GẠO VIỆT XUẤT KHẨU', 'CAO NHẤT TỪ THÁNG 12/2024'), cols=CC, moc=True,
      cards=[('490 USD', 'Gạo Việt 5/11: 480 đến 490', 'CAO NHẤT TỪ 12/2024'), ('510 USD', 'Gạo Thái tuần qua: 505 đến 510', 'CAO HƠN GẠO VIỆT'), ('400 USD', 'Ấn Độ tuần qua: 395 đến 400', 'RẺ NHẤT 3 NƯỚC')],
      say=("Đây là giá một tấn gạo trắng loại phổ biến, bán sỉ ra nước ngoài, chưa phải giá chị trả ngoài chợ. Đầu tháng mười một, gạo Việt lên gần năm trăm đô la một tấn, cao nhất gần hai năm. Quy ra tiền Việt, khoảng mười hai đến mười ba nghìn đồng một ký, trong khi ngoài chợ chị mua mười lăm đến mười sáu nghìn đồng. "
           "Giá bán ra nước ngoài là một tín hiệu nên theo dõi, dù không phải lúc nào cũng kéo giá chợ theo ngay. Riêng Ấn Độ vẫn bán quanh bốn trăm đô, rẻ nhất trong ba nước.")),
 dict(k='bignum', anh=GAO, cap=('GIÁ GẠO NGOÀI CHỢ', 'THÁNG 10 LẠI GIẢM 0,92%'), cols=CC, value=0.92, fmt='{:,.2f}', unit='%', top='GIÁ GẠO THÁNG 10/2026 GIẢM SO VỚI THÁNG 9', sub='Gạo tẻ thường 14.600 đến 16.500 đồng/kg (Cục Thống kê)', col=GREEN,
      say=("Đây là cú lật đầu tiên. Theo Cục Thống kê, tháng mười, giá gạo trong nước giảm gần một phần trăm so với tháng trước, vì nguồn cung trong nước dồi dào. "
           "Gạo tẻ thường ngoài chợ khoảng mười bốn nghìn sáu trăm đến mười sáu nghìn năm trăm đồng mỗi ký. Số của tháng mười một thì đầu tháng sau mới có. "
           "Với túi tiền nhà chị Ngọc, điều này nghĩa là: tính đến tháng mười, giá ngoài cảng đã nóng lên, nhưng chưa vào tới chợ.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Vì sao giá ngoài chợ chưa lên?', anh=CON, cap=('XUẤT KHẨU GẠO 10 THÁNG', 'ÍT HƠN VÀ RẺ HƠN NĂM NGOÁI'), cols=CC, moc=True,
      cards=[('6,8 triệu tấn', 'Gạo bán ra 10 tháng', 'ÍT HƠN NĂM NGOÁI'), ('484 USD', 'Giá bình quân 10 tháng', 'RẺ HƠN NĂM NGOÁI'), ('475.000 tấn', 'Riêng tháng 10', 'TĂNG 37,2% CÙNG KỲ')],
      say=("Anh Khoa gửi chị số của Bộ Nông nghiệp và Môi trường. Tính chung mười tháng, gạo Việt bán ra nước ngoài vừa ít hơn, vừa rẻ hơn năm ngoái. "
           "Tức là gần cả năm nay, gạo ở trong nước không thiếu. Chỉ riêng tháng mười, lượng bán ra tăng khoảng ba mươi bảy phần trăm so với cùng tháng năm ngoái. Khách nước ngoài bắt đầu mua mạnh trở lại, và đó là tín hiệu chị nên để mắt.")),
 dict(k='giay', short=True, cap=('LÚA TẠI RUỘNG', 'MỖI KÝ 6.200 ĐẾN 7.200 ĐỒNG'), cols=CC, moc=True, giay=dict(tieu_de='GIÁ LÚA TƯƠI TẠI RUỘNG', so='Miền Tây, ngày 11/11/2026 (Báo Văn Hóa)', dau='GIÁ LÚA', dieu=[
        ('Lúa thường: 6.200 đến 6.600 đồng/kg.', 'THƯỜNG'),
        ('Lúa thơm: 7.100 đến 7.200 đồng/kg.', 'THƠM'),
        ('Lúa tươi còn phải phơi, xay xát.', 'XAY XÁT'),
        ('Ruộng hỏng thì giá lên khó bù.', 'RỦI RO')]),
      say=("Còn ở ruộng của ba chị, ngày mười một tháng mười một, mỗi ký lúa tươi loại thường được khoảng sáu nghìn hai trăm đến sáu nghìn sáu trăm đồng. "
           "Lúa tươi còn phải phơi, xay xát, đóng bao, nên giá lúa thấp hơn giá gạo nhiều là bình thường. "
           "Với ba chị, chuyện lớn không phải giá lên bao nhiêu. Nếu mặn làm hỏng ruộng, giá có lên cũng khó bù phần lúa mất.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước mặn như thế nào?', cap=('"NĂM 2016 XÓM BA THẤT LẮM', 'NĂM 2020 NGHE BÁO TRƯỚC"'), cols=CC, moc=True, call=dict(ten='Ba', phu='Vĩnh Long', mau=V_, loi=[
        'Năm 2016 xóm ba thất nhiều lắm', 'Năm 2020 nghe báo trước, gieo sớm']),
      say=("Tối đó, ba chị Ngọc gọi điện. Ông nhớ năm 2016, xóm ông thất mùa nhiều lắm. "
           "Bốn năm sau, vào mùa khô năm 2020, ông nghe báo trước nên gieo sớm. Ông muốn con gái hiểu: lần đó mặn không nhẹ hơn, nhưng xóm ông đỡ hơn.")),
 dict(k='giay', cap=('2016 VÀ 2020', 'NHỮNG CON SỐ CỦA LẦN TRƯỚC'), cols=CC, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='VietNamNet 22/6/2020, SGGP 20/6/2020', dau='LẦN TRƯỚC', dieu=[
        ('2016: 405.000 ha lúa bị ảnh hưởng.', 'NĂM 2016'),
        ('2020: vùng nhiễm mặn rộng hơn 2016.', 'NĂM 2020'),
        ('2020: 58.400 ha lúa thiệt hại.', 'NĂM 2020'),
        ('Hộ khó khăn: 210.000 còn 96.000.', 'SỐ HỘ')]),
      say=("Đây là con số của lần trước. Mùa mặn năm 2016, hơn bốn trăm nghìn héc ta lúa bị ảnh hưởng. "
           "Mùa khô năm 2020, vùng nhiễm mặn còn rộng hơn. Vậy mà diện tích lúa thiệt hại chỉ khoảng năm mươi tám nghìn héc ta.")),
 dict(k='bignum', anh=LUA, cap=('2020 MẶN RỘNG HƠN', 'THIỆT HẠI CHỈ BẰNG 14%'), cols=CC, value=14, fmt='{:,.0f}', unit='%', top='LÚA THIỆT HẠI 2020 SO VỚI DIỆN TÍCH BỊ ẢNH HƯỞNG 2016', sub='58.400 ha so với 405.000 ha (VietNamNet 22/6/2020)', col=GREEN,
      say=("Đây là cú lật thứ hai. Lúa thiệt hại năm 2020 chỉ bằng khoảng mười bốn phần trăm diện tích lúa bị ảnh hưởng năm 2016. "
           "Theo bài tổng kết trên VietNamNet, vụ đông xuân năm đó được gieo sớm hơn mười đến hai mươi ngày để né lúc mặn lên cao. "
           "Nghĩa là El Nino mạnh không tự động thành mất mùa. Ruộng đỡ thiệt thì gạo có thể đỡ thiếu, và tiền chợ của nhà mình cũng có thể đỡ áp lực.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='noti', ch='Chương 4 – Lần gạo tăng giá thật', cap=('THÁNG 7/2023', 'ẤN ĐỘ CẤM XUẤT KHẨU GẠO TRẮNG'), cols=CR, moc=True, noti=dict(gio='20:00', ngay='20/7/2023', items=[
        ('Tin tức', 'Thế giới', 'Ấn Độ cấm xuất khẩu gạo trắng thường từ hôm nay', R_)]),
      say=("Vậy giá gạo đã bao giờ tăng thật chưa? Rồi. Ngày hai mươi tháng bảy năm 2023, Ấn Độ cấm xuất khẩu gạo trắng thường. "
           "Lần đó, cú hích đến từ một lệnh cấm của nước bán gạo lớn, không chỉ từ thời tiết.")),
 dict(k='bignum', anh=CON, cap=('ĐỈNH 663 USD MỘT TẤN', 'THÁNG 12/2023'), cols=CR, value=663, fmt='{:,.0f}', unit=' USD', top='GIÁ GẠO VIỆT XUẤT KHẨU NGÀY 4/12/2023', sub='Cao nhất nếu không tính năm 2008 (VnExpress 5/12/2023)', col=RED,
      say=("Đến ngày bốn tháng mười hai năm đó, giá gạo Việt bán ra lên sáu trăm sáu mươi ba đô la một tấn. Theo VnExpress, đó là mức cao nhất nếu không tính năm 2008. "
           "Tuần qua, giá bán ra quanh bốn trăm tám mươi đô, vẫn thấp hơn đỉnh đó khoảng hai mươi tám phần trăm.")),
 dict(k='giay', short=True, cap=('NĂM 2024: GẠO ĐẮT HƠN 15,93%', 'BÌNH QUÂN CẢ NĂM'), cols=CR, moc=True, giay=dict(tieu_de='GIÁ TRÊN BÀN ĂN NĂM 2024', so='Cục Thống kê, bình quân năm 2024 so với 2023', dau='NĂM 2024', dieu=[
        ('Giá gạo: tăng 15,93%.', 'GẠO'),
        ('Giá cả nói chung: tăng 3,63%.', 'CPI'),
        ('Gạo tăng gấp hơn 4 lần giá chung.', 'TỰ TÍNH')]),
      say=("Và đây là cú lật thứ ba. Tính bình quân cả năm 2024, sau lệnh cấm đó, giá gạo trong nước cao hơn năm trước gần mười sáu phần trăm. Mức đó gấp hơn bốn lần mức tăng của giá cả nói chung. "
           "Năm đó, riêng giá gạo tăng nhanh hơn nhiều so với giá cả nói chung.")),
 dict(k='bars', anh=CON, cap=('GIÁ GẠO VIỆT MỘT TẤN', 'ĐỈNH CŨ VÀ TUẦN QUA'), cols=CC, moc=True,
      bars=[('Đỉnh 12/2023', 663, RED, '663 USD'), ('Tuần qua', 480, GOLD, 'khoảng 480 USD')],
      say=("Đặt cạnh nhau: đỉnh cũ sáu trăm sáu mươi ba đô, tuần qua chưa tới năm trăm. "
           "Giá đã lên so với mấy tháng trước, nhưng còn cách đỉnh cũ khá xa.")),
 dict(k='checklist', anh=MEK, cap=('GIỐNG 2, KHÁC 2', 'SO VỚI CÁC LẦN TRƯỚC'), cols=CC, moc=True,
      items=[('Giống 2016: mùa khô có El Nino', GOLD), ('Giống 2016: mặn có thể vào sâu', GOLD), ('Khác 2023: Ấn Độ vẫn bán gạo', GREEN), ('Khác 2023: chợ tháng 10 giảm', GREEN)],
      say=("So với lần mặn năm 2016, có hai điểm giống: mùa khô đi cùng El Nino, và mặn có thể vào sâu tương tự. "
           "So với lần gạo đắt năm 2023, có hai điểm khác: Ấn Độ hiện vẫn bán gạo ra ngoài với giá rẻ nhất, và giá gạo trong nước tháng mười còn giảm. "
           "Chưa tăng, không có nghĩa là không thể tăng. Nếu sản lượng của Ấn Độ và Thái Lan giảm như dự báo, giá có thể đi lên tiếp.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='giay', ch='Chương 5 – Nồi cơm nhà mình', short=True, cap=('NẾU GẠO TĂNG NHƯ NĂM 2024', 'NHÀ 4 NGƯỜI THÊM GẦN 80 NGHÌN'), cols=CC, moc=True, giay=dict(tieu_de='SỔ CHI TIÊU CỦA CHỊ NGỌC', so='Em giả định 4 người, 30 kg mỗi tháng, giá mức cao 16.500', dau='GIẢ ĐỊNH', dieu=[
        ('30 kg × 16.500 đồng = 495.000 đồng.', 'BÂY GIỜ'),
        ('Nếu tăng 15,93% như năm 2024:', 'KỊCH BẢN'),
        ('Mỗi tháng thêm khoảng 79.000 đồng.', 'THÊM'),
        ('Trữ nhiều bao: dễ ẩm, dễ mọt.', 'RỦI RO')]),
      say=("Chị Ngọc lấy sổ chi tiêu ra tính. Em giả định nhà chị bốn người, ăn khoảng ba mươi ký gạo mỗi tháng. Lấy giá mức cao mười sáu nghìn năm trăm đồng, tiền gạo gần năm trăm nghìn đồng mỗi tháng. "
           "Nếu giá gạo tăng mạnh như năm 2024, mỗi tháng nhà chị trả thêm gần tám mươi nghìn đồng. "
           "Với người chỉ mua gạo để ăn, đây là khoản nên biết, nhưng chưa phải chuyện lớn.")),
 dict(k='chat', cap=('"VẬY KHÔNG CẦN VỘI TRỮ GẠO', 'MÀ NÊN LO CHO RUỘNG CỦA BA"'), cols=CC, moc=True, chat=dict(ten='Anh Khoa', tv='Đang hoạt động', gio='21:00', mau=V_, msgs=[
        ('me', 'Vậy em khỏi vội trữ gạo hả anh?'),
        ('Anh Khoa', 'Trữ nhiều dễ ẩm mốc, phần tăng nếu có cũng nhỏ'),
        ('Anh Khoa', 'Chỗ cần lo là ruộng của ba với nước ngọt')]),
      say=("Anh Khoa nhắn lại: trữ nhiều gạo trong nhà phố dễ ẩm, dễ mọt, mà phần tăng nếu có cũng nhỏ. Chỗ cần lo thật là ruộng của ba và nước ngọt ở quê. "
           "Với người ở thành phố, đó là vài chục nghìn đồng. Với người trồng lúa, đó có thể là cả một vụ.")),
 dict(k='cards', anh=LUA, cap=('KHUYẾN CÁO CHO MÙA KHÔ TỚI', 'VIỆN KHOA HỌC THỦY LỢI MIỀN NAM'), cols=CC, moc=True,
      cards=[('Tháng 12', 'Xong xuống giống đông xuân', 'CHẬM NHẤT NỬA ĐẦU THÁNG 1'), ('Ngay khi có thể', 'Tích thêm nước ngọt', 'TRỮ NƯỚC SỚM'), ('Thường xuyên', 'Cập nhật dự báo mặn', 'THEO DÕI')],
      say=("Theo khuyến cáo được báo Tiền Phong đăng, vụ đông xuân nên xuống giống xong trong tháng mười hai, chậm nhất là nửa đầu tháng một. Nước ngọt cần trữ sớm, tích thêm ngay khi có thể. Và thường xuyên cập nhật dự báo mặn. "
           "Lịch cụ thể từng xã sẽ khác nhau, nên ba chị vẫn phải theo lịch thời vụ của địa phương.")),
 dict(k='chat', cap=('"CON GỬI BA TIỀN MUA BỒN', 'THAY VÌ MUA TRỮ GẠO"'), cols=CC, moc=True, chat=dict(ten='Ba', tv='Vĩnh Long', gio='21:30', mau=X_, msgs=[
        ('me', 'Con không trữ gạo nữa, con gửi ba một triệu góp mua bồn nước nha'),
        ('Ba', 'Ừ, ba xuống giống theo lịch của xã'),
        ('Ba', 'Không vay thêm để làm rộng vụ này')]),
      say=("Chị Ngọc quyết định không mua trữ gạo. Khoảng một triệu đồng chị định mua mấy bao gạo, chị gửi về để ba góp mua thêm bồn chứa nước ngọt. "
           "Ba chị nói sẽ xuống giống theo đúng lịch của xã, và vụ này không vay thêm tiền để làm rộng ruộng.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='checklist', ch='Chương 6 – Phép thử cho túi tiền nhà mình', anh=TP, cap=('PHÉP THỬ: NHÀ MÌNH ĐỨNG', 'Ở PHÍA NÀO CỦA BAO GẠO?'), cols=CC, moc=True,
      items=[('Chỉ mua gạo ăn: ảnh hưởng nhỏ', GREEN), ('Người thân làm ruộng miền Tây', GOLD), ('Làm ăn, vay vốn dựa vào nông sản', RED)],
      say=("Em gợi ý một phép thử tự soi: nhà mình đứng ở phía nào của bao gạo? "
           "Nếu nhà mình chỉ mua gạo để ăn, ảnh hưởng thường nhỏ, thường không cần vội mua trữ. Nếu có người thân làm ruộng hay vườn ở miền Tây, hãy hỏi lịch xuống giống và chuyện nước ngọt ngay từ bây giờ. "
           "Còn nếu nhà mình làm ăn hay đang vay vốn dựa vào nông sản miền Tây, nên tính trước một kịch bản xấu như mùa mặn năm 2016. Đây là mốc tự soi, không phải lời khuyên.")),
 dict(k='checklist', anh=HN, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI TẾT'), cols=CC, moc=True,
      items=[('Bản tin mặn của địa phương', GOLD), ('Giá gạo Việt và Thái mỗi tuần', GOLD), ('Mỹ cập nhật El Nino ngày 10/12', GOLD)],
      say=("Ba điều đáng theo dõi từ nay tới Tết. Bản tin mặn của địa phương. Giá gạo Việt và gạo Thái bán ra mỗi tuần. Và bản cập nhật El Nino tiếp theo của cơ quan khí tượng Mỹ, dự kiến ngày mười tháng mười hai. "
           "Muốn hiểu giá cả tác động thế nào tới tiền tiết kiệm của gia đình, anh chị có thể đọc bài miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', cap=('"GIÁ GẠO THÌ CHỜ ĐƯỢC', 'LỊCH XUỐNG GIỐNG THÌ KHÔNG"'), cols=CC, chat=dict(ten='Ba', tv='Vĩnh Long', gio='22:00', mau=X_, msgs=[
        ('Ba', 'Giá gạo thì chờ được con'),
        ('Ba', 'Lịch xuống giống thì không chờ được')]),
      say=("Trước khi ngủ, ba chị Ngọc nhắn thêm một câu: giá gạo thì chờ được con, lịch xuống giống thì không chờ được. "
           "Lần trước, người gieo sớm thường đỡ thiệt hơn.")),
 dict(k='end', cap=('NHÀ ANH CHỊ ĐỨNG', 'Ở PHÍA NÀO CỦA BAO GẠO?'), cols=CC,
      say=("Còn anh chị, nhà mình đứng ở phía nào của bao gạo: chỉ mua gạo để ăn, có người thân làm ruộng miền Tây, hay đang làm ăn dựa vào nông sản?")),
]
import ql_post; S = ql_post.tach(S, max_tu=50, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Giá Gạo Xuất Khẩu Đỉnh Gần 2 Năm, Chợ Lại Giảm: Có Nên Trữ?'
WEB = 'https://chungkhoanhuynguyen.com/hoc/gui-tiet-kiem-an-toan-chua-chac-lai-thuc-lam-phat-va-suc-mua-sau-10.html'
MT = ("NÓNG: ngày 24/11/2026 tại hội thảo gạo xanh ở Cần Thơ, Viện Chiến lược, Chính sách nông nghiệp và môi trường cho biết El Nino có khả năng kéo dài cuối 2026 – đầu 2027; sản lượng gạo Ấn Độ có thể giảm khoảng 4,6%, Thái Lan 1,9%. "
      "Nước mặn mùa khô tới có thể vào sâu ngang năm 2016. Giá gạo Việt xuất khẩu đầu tháng 11 lên cao nhất từ 12/2024 – nhưng giá gạo trong nước tháng 10 lại giảm 0,92%. Mùa khô 2020 vùng nhiễm mặn rộng hơn 2016, mà lúa thiệt hại chỉ bằng 14% diện tích bị ảnh hưởng năm 2016: vì sao? Và phép thử cho túi tiền gia đình.\n\n"
      "Nguồn số liệu:\n"
      "• BNEWS/TTXVN 24/11/2026: hội thảo \"Gạo xanh Việt Nam\" tại Cần Thơ – El Nino có khả năng xuất hiện cuối 2026, đầu 2027; sản lượng gạo Ấn Độ có thể giảm khoảng 4,6%, Thái Lan 1,9%, Brazil khoảng 3%\n"
      "• VietnamPlus 15/10/2026: Trung tâm Dự báo KTTV quốc gia – xác suất 96% El Nino giữ cường độ rất mạnh từ 11/2026 đến 1/2027\n"
      "• Tiền Phong 5/10/2026 (Viện Khoa học thủy lợi miền Nam): mặn 4 g/l tháng 12/2026 vào 30–40 km; tháng 1–2/2027 50–65 km, tương đương 2016; nửa đầu tháng 3/2027 55–70 km; khuyến cáo xuống giống đông xuân xong trong tháng 12/2026, chậm nhất nửa đầu tháng 1/2027, trữ nước sớm\n"
      "• Nhân Dân 8/11/2026: khoảng 350.000 ha lúa đông xuân có nguy cơ hạn mặn\n"
      "• Business Recorder 5/11/2026, VietnamPlus 7/11/2026: gạo 5% tấm Việt Nam 480–490 USD/tấn, cao nhất từ 12/2024; Reuters (tuần tới 22/11/2026): Việt Nam 475–485, Thái Lan 505–510, Ấn Độ gạo trắng 395–400 USD/tấn\n"
      "• VietnamPlus 4/11 và 7/11/2026 (Bộ NN&MT): xuất khẩu gạo 10 tháng 6,8 triệu tấn (−4,6%), giá bình quân khoảng 484 USD/tấn (−5,4%); riêng tháng 10 475.000 tấn (+37,2% so cùng kỳ)\n"
      "• Báo Văn Hóa 12/11/2026: lúa tươi tại ruộng ngày 11/11 – IR50404 6.200–6.300, OM5451 6.400–6.600, Đài Thơm 8 7.100–7.200 đồng/kg\n"
      "• Cục Thống kê, CPI tháng 10/2026: giá gạo giảm 0,92% so tháng trước do nguồn cung trong nước dồi dào; gạo tẻ thường 14.600–16.500 đồng/kg\n"
      "• FOX10 News 12/11/2026 (NOAA): bản cập nhật El Nino kế tiếp ngày 10/12/2026\n"
      "• VietNamNet 22/6/2020, SGGP 20/6/2020: mùa khô 2019–2020 lúa thiệt hại 58.400 ha, bằng 14% diện tích bị ảnh hưởng 2015–2016 (405.000 ha); 2016: 210.000 hộ khó khăn, 2020: khoảng 96.000 hộ; diện tích nhiễm mặn 2020 rộng hơn 2016; đông xuân xuống giống sớm 10–20 ngày để né mặn\n"
      "• Bộ Công Thương 21/7/2023: Ấn Độ cấm xuất khẩu gạo trắng non-basmati từ 20/7/2023; VnExpress 5/12/2023: gạo Việt 5% tấm 663 USD/tấn ngày 4/12/2023\n"
      "• Cục Thống kê, CPI năm 2024: giá gạo bình quân +15,93%, lương thực +12,19%, CPI chung +3,63%\n"
      "• Tự tính: 480/663 ≈ 0,72 (thấp hơn đỉnh khoảng 28%); 58.400/405.000 ≈ 14%; 15,93/3,63 ≈ 4,4 lần. Quy đổi giá xuất khẩu: 480–490 USD × 26.030 đồng/USD (giá bán Vietcombank 23/11, VnExpress) ≈ 12.500–12.750 đồng/kg. Sổ chi tiêu là GIẢ ĐỊNH: 30 kg × 16.500 = 495.000 đồng/tháng; nếu tăng 15,93% → thêm khoảng 79.000 đồng/tháng\n\n"
      "Bài liên quan về giá cả và tiền tiết kiệm: " + WEB + "\n"
      "Cần trao đổi riêng về kế hoạch tài chính: Zalo 0365.188.286\n\n"
      "Nhân vật chị Ngọc, anh Khoa, ba chị Ngọc là hư cấu; số liệu là thật theo nguồn trên.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-25', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['El Nino', 'El Nino 2026', 'hạn mặn miền Tây', 'xâm nhập mặn', 'giá gạo hôm nay', 'giá gạo xuất khẩu', 'giá lúa hôm nay', 'giá gạo tăng', 'tin nóng tài chính', 'lạm phát'],
    bia_hook=['GẠO SẮP TĂNG?', 'CHỢ VẪN GIẢM'], badge='EL NINO RẤT MẠNH',
    bia_anh='Rice field Mekong Delta||Rice paddy Vietnam',
    bia_hook_b=['2020 MẶN HƠN', 'MÀ ÍT HỎNG HƠN'], badge_b='BÀI HỌC LẦN TRƯỚC',
    bia_hook_c=['GẠO +15,93%', 'LẶP LẠI?'], badge_c='BÌNH QUÂN NĂM 2024',
    reel_hook='EL NINO RẤT MẠNH|SAO GIÁ GẠO CHỢ LẠI GIẢM???',
    fb_post=("El Nino rất mạnh, nước mặn có thể vào sâu ngang năm 2016 🌾\n\n👉 Gạo Việt xuất khẩu lên cao nhất gần 2 năm\n👉 Nhưng giá gạo trong nước tháng 10 lại giảm 0,92%\n"
             "👉 Mùa khô 2020 mặn rộng hơn 2016 mà lúa thiệt hại chỉ bằng 14% diện tích bị ảnh hưởng năm 2016\n\nNhà anh chị đứng ở phía nào của bao gạo?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 25/11: El Nino rất mạnh, mặn có thể như 2016, gạo xuất khẩu lên đỉnh gần 2 năm mà giá chợ giảm (NV1B 25/11/2026).\n"
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
sys.path.insert(0, CW + '/_video'); import kiem_loi, kiem_goi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'):
    for l in kiem_goi.kiem(TIEU, META[KEY][b]): print('kiem_goi', b, l)
try:
    import xung_ho
    for i, c in enumerate(S, 1):
        if xung_ho.le_phep(c['say']) != c['say']: print('XUNG_HO doi canh', i)
except Exception as e: print('xung_ho?', e)
