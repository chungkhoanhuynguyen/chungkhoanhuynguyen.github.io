# -*- coding: utf-8 -*-
# NV1 20/11/2026 01:20 – VIDEO DÀI kênh chính, "câu hỏi lớn về tiền": sầu riêng xuất khẩu kỷ lục 3,45 tỷ USD, 96% vào Trung Quốc,
#   diện tích 200.000 ha gần gấp đôi quy hoạch – tiền tỷ đô về túi ai, nhà vườn có đi vết xe hồ tiêu?
#   Khuôn "manh mối – suy luận" (3 chi tiết đầu phim) + "so với lần trước" (hồ tiêu: giá xuất khẩu 12/2016 → 4/2020 mất 73,6%).
# Lý do chọn: data/view/xu_huong.md tuần tới 19/11 – "Tại sao hoa quả Trung Quốc rẻ như cho mà vẫn phải nhập của Việt Nam?" (XB Giải Thích) ~182 nghìn view,
#   cao nhất nhóm kinh tế Việt Nam; chủ đề TIỀN TÚI NGƯỜI THƯỜNG (nhà vườn) + THẾ GIỚI (Trung Quốc, Thái, Philippines). Khác CH2511MY (25/11: hàng Mỹ vào VN, gà):
#   đây là hàng VN bán ra, một mặt hàng, một khách hàng. Cách ≥4 ngày, có CH2711TN (thuế) ở giữa.
# Nguồn:
#  - Vietnambiz 3/11/2026 + 5/11/2026 (Cục Hải quan): xuất khẩu sầu riêng 9T/2026 3,45 tỷ USD (+25%); sang Trung Quốc gần 3,3 tỷ (+27,6%), gần 96% (cùng kỳ 93,6%);
#    tháng 9 729 triệu USD (−23,8% so tháng 8, −25% cùng kỳ); Hàn Quốc +129%; Hiệp hội Rau quả (ông Đặng Phúc Nguyên, Tổng thư ký – chỉ nêu chức danh):
#    TQ chuộng sầu riêng tươi; nếu TQ siết kiểm soát chất lượng hoặc giảm nhập, hàng ùn ứ ở kho miền Tây, Tây Nguyên, áp lực bán tháo; thị trường khác chưa đủ sức hấp thụ.
#  - Vietnambiz 29/9/2026: 8T/2026 sầu riêng 2,72 tỷ USD (+55%), 44,3% xuất khẩu rau quả; giá xuất khẩu bình quân sầu riêng tươi 8T giảm 3,3% còn 3.269 USD/tấn.
#  - Trung tâm WTO (VCCI) / VnEconomy 15/10/2026: quy hoạch ban đầu 65.000–75.000 ha đến 2030, điều chỉnh 100.000–110.000 ha; thực tế 2026 khoảng 200.000 ha; nguy cơ dư thừa, áp lực giảm giá.
#  - Người Đưa Tin 25/10/2026: khoảng 200.000 ha, sản lượng dự kiến 2,08 triệu tấn năm 2026.
#  - Doanh Nhân Việt Nam 9/11/2026 (giasaurieng.net): Tây Nguyên RI6 đẹp lựa 52.000–54.000 đ/kg, RI6 xô 25.000–30.000; Thái đẹp lựa 72.000–74.000, Thái xô 32.000–35.000.
#  - Vietnambiz 25/9/2026 (Cục Xuất nhập khẩu, Bộ Công Thương): Philippines khoảng 15.000 ha, dự kiến 150 nghìn tấn niên vụ 2026/2027, chưa đến 1% thị phần TQ.
#  - WiData (Cục Hải quan): xuất khẩu rau quả 10T/2026 8.292 triệu USD (+17,3% so 10T/2025 7.066), trong đó sang TQ 5.420 triệu (65%); nhập khẩu rau quả 10T/2026 2.824 triệu USD;
#    rau quả sang TQ tháng 2/2025 132,7 triệu USD so 2/2024 195,9 triệu (−32%, tự tính).
#  - WiData (Cục Hải quan): giá xuất khẩu bình quân hạt tiêu 12/2016 7,63 USD/kg; 4/2020 2,01 USD/kg (−73,6%, tự tính); 10/2026 6,58 USD/kg.
# GIẢ ĐỊNH minh hoạ (nhà anh Phong, Đắk Lắk): vườn khoảng 30 tấn/vụ, gần nửa hàng xô; 15 tấn × chênh 25.000 đ/kg = 375 triệu đồng.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261120_0200'
KEY = 'CH2911SR'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
SR = 'ov:Durian fruit||Durian fruit'
TR = 'ov:Durian tree||Durian fruit'
CT = 'ov:Container ship||Container ship'
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
TI = 'ov:Black pepper plant||Black pepper'
BX = 'ov:Bitexco Financial Tower||Ho Chi Minh City skyline night'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('SẦU RIÊNG XUẤT KHẨU', '3,45 TỶ USD, 9 THÁNG'), cols=CC, noti=dict(gio='05:40', ngay='Chủ Nhật', items=[
        ('Tin tức', 'Nông sản', 'Xuất khẩu sầu riêng 9 tháng đạt 3,45 tỷ USD, gần 96% sang Trung Quốc', V_),
        ('Zalo', 'Thương lái', 'RI6 xô hôm nay 25 nghìn, anh bán không?', R_),
        ('Zalo', 'Linh', 'Báo nói sầu riêng kỷ lục, sao bố bảo lo hả bố?', X_)]),
      say=("Sáu giờ kém hai mươi sáng Chủ nhật, ở một vườn sầu riêng tại Đắk Lắk, điện thoại anh Phong sáng lên. "
           "Tin thứ nhất: xuất khẩu sầu riêng chín tháng đạt gần ba phẩy năm tỷ đô la, gần chín mươi sáu phần trăm sang Trung Quốc. "
           "Tin thứ hai, từ thương lái: hàng xô hôm nay hai mươi lăm nghìn một ký, anh bán không. "
           "Tin thứ ba, từ con gái anh, Linh, đang học ở Sài Gòn: báo nói sầu riêng kỷ lục, sao bố lại bảo lo?")),
 dict(k='bignum', anh=SR, cap=('96% SẦU RIÊNG', 'BÁN CHO MỘT KHÁCH HÀNG'), cols=CC, value=96, fmt='{:,.0f}', unit='%', top='TỶ TRỌNG TRUNG QUỐC TRONG XUẤT KHẨU SẦU RIÊNG, 9 THÁNG 2026',
      sub='gần 3,3 tỷ trên 3,45 tỷ USD, cùng kỳ năm ngoái 93,6% – Cục Hải quan, Vietnambiz 5/11', col=GOLD,
      say=("Câu trả lời bắt đầu từ con số này. Trong mỗi trăm đồng tiền sầu riêng bán ra nước ngoài, gần chín mươi sáu đồng đến từ một khách hàng: Trung Quốc. "
           "Năm ngoái tỷ lệ đó là chín mươi ba phẩy sáu phần trăm. Kỷ lục đi kèm một tỷ trọng còn cao hơn.")),
 dict(k='checklist', anh=TR, cap=('3 CHI TIẾT', 'TRẢ LỜI CUỐI PHIM'), cols=CC,
      items=[('1. Cùng một cây: 54 nghìn và 25 nghìn', V_), ('2. Gốc tiêu khô của ông nội', R_), ('3. Thùng hàng ghi Hàn Quốc', X_)],
      say=("Ba chi tiết nhỏ trong vườn nhà anh Phong sẽ trả lời câu hỏi của Linh ở cuối phim, anh chị nhớ giúp em. "
           "Một: cùng một cây, trái đẹp được năm mươi tư nghìn một ký, trái xô chỉ hai mươi lăm nghìn. "
           "Hai: ở góc vườn vẫn còn mấy gốc tiêu khô ông nội trồng từ mười năm trước. "
           "Ba: ở kho đóng gói đầu xã, có một chồng thùng sầu riêng ghi nơi đến là Hàn Quốc.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Tiền kỷ lục đến từ đâu?', cap=('200.000 HA SẦU RIÊNG', 'GẦN GẤP ĐÔI QUY HOẠCH'), cols=CC, moc=True, giay=dict(tieu_de='SẦU RIÊNG VIỆT NAM 2026', so='Trung tâm WTO 15/10, Người Đưa Tin 25/10', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Quy hoạch đến 2030, đã nâng', 'TỐI ĐA 110.000 HA'),
        ('Diện tích thực tế năm 2026', '200.000 HA'),
        ('Sản lượng dự kiến năm 2026', '2,08 TRIỆU TẤN'),
        ('Xuất khẩu 9 tháng', '3,45 TỶ USD')]),
      say=("Quy hoạch ban đầu cho cây sầu riêng đến năm hai nghìn không trăm ba mươi chỉ khoảng sáu mươi lăm đến bảy mươi lăm nghìn héc ta. Sau đó được nâng lên một trăm mười nghìn. "
           "Nhưng đến năm nay, diện tích thực tế đã khoảng hai trăm nghìn héc ta, gần gấp đôi mức đã nâng. Sản lượng dự kiến hơn hai triệu tấn.")),
 dict(k='cards', anh=CT, cap=('KỶ LỤC 9 THÁNG', 'NHƯNG THÁNG 9 GIẢM 25%'), cols=CC, moc=True,
      cards=[('3,45 tỷ USD', 'Xuất khẩu 9 tháng', 'Gần 96% sang Trung Quốc'), ('729 triệu USD', 'Riêng tháng 9', 'Giảm 25% so cùng kỳ'), ('3.269 USD', 'Mỗi tấn sầu riêng tươi', '8 tháng, giảm 3,3%')],
      say=("Cú lật đầu tiên nằm ngay trong số liệu hải quan. Riêng tháng chín, xuất khẩu sầu riêng khoảng bảy trăm hai mươi chín triệu đô la, thấp hơn cùng kỳ năm ngoái hai mươi lăm phần trăm. "
           "Còn tính đến tháng tám, giá xuất khẩu bình quân mỗi tấn sầu riêng tươi giảm ba phẩy ba phần trăm, còn khoảng ba nghìn hai trăm bảy mươi đô la. "
           "Kỷ lục là của chín tháng, nhưng tháng gần nhất đã thấp hơn cùng kỳ. Và tiền về nhiều là nhờ bán nhiều hàng, không phải vì mỗi ký đắt hơn.")),
 dict(k='giay', cap=('CÙNG MỘT TRÁI SẦU RIÊNG', 'ĐẸP 54 NGHÌN, XÔ 25 NGHÌN'), cols=CR, moc=True, giay=dict(tieu_de='BẢNG GIÁ TÂY NGUYÊN 9/11', so='Doanh Nhân Việt Nam 9/11/2026', dau='GIÁ THU MUA', dieu=[
        ('RI6 đẹp lựa', '52 ĐẾN 54 NGHÌN'),
        ('RI6 hàng xô', '25 ĐẾN 30 NGHÌN'),
        ('Thái đẹp lựa', '72 ĐẾN 74 NGHÌN'),
        ('Thái hàng xô', '32 ĐẾN 35 NGHÌN')]),
      say=("Còn ở vườn, giá thu mua Tây Nguyên đầu tháng mười một như thế này. "
           "Sầu riêng RI sáu đẹp lựa khoảng năm mươi hai đến năm mươi tư nghìn đồng một ký. Hàng xô chỉ hai mươi lăm đến ba mươi nghìn. "
           "Cùng một cây, trái đạt chuẩn và trái không đạt chuẩn chênh nhau gần gấp đôi.")),
 dict(k='chat', cap=('NỬA VƯỜN HÀNG XÔ', 'KÉM 375 TRIỆU?'), cols=CR, moc=True, chat=dict(ten='Linh', tv='Đang hoạt động', gio='12:10', mau=X_, msgs=[
        ('Linh', 'Vườn mình được bao nhiêu tấn hả bố?'),
        ('me', 'Khoảng 30 tấn, mà nửa vườn ra hàng xô'),
        ('Linh', '15 tấn kém 25 nghìn một ký là bao nhiêu?')]),
      say=("Trưa đó Linh hỏi bố vườn mình được bao nhiêu. Anh Phong đáp: khoảng ba mươi tấn, mà gần nửa vườn ra hàng xô. Con số này là em giả định. "
           "Linh tự tính, lấy giữa khung giá: mười lăm tấn hàng xô, mỗi ký kém hàng đẹp khoảng hai mươi lăm nghìn, là khoảng ba trăm bảy mươi lăm triệu đồng.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='bignum', ch='Chương 2 – Người mua có nhiều lựa chọn', anh=CT, cap=('VIỆT NAM CŨNG NHẬP', '2,82 TỶ USD RAU QUẢ'), cols=CC, moc=True, value=2.82, fmt='{:,.2f}', unit=' TỶ USD', top='NHẬP KHẨU RAU QUẢ CỦA VIỆT NAM, 10 THÁNG 2026',
      sub='xuất khẩu rau quả 10 tháng 8,29 tỷ USD – Cục Hải quan, WiData', col=RED,
      say=("Có một cú lật mà nhiều người không để ý. Trong lúc bán sầu riêng ra, Việt Nam cũng nhập rau quả về. "
           "Mười tháng năm nay, nhập khẩu rau quả hơn hai phẩy tám tỷ đô la. Xuất khẩu rau quả gần tám phẩy ba tỷ đô la, trong đó khoảng sáu mươi lăm phần trăm sang Trung Quốc. "
           "Việt Nam cũng mua trái cây từ nhiều nước. Người mua nào cũng chọn nơi bán, Trung Quốc cũng vậy.")),
 dict(k='cards', anh=SR, cap=('ĐỐI THỦ ĐANG TRỒNG THÊM', 'KHÁCH CÓ NHIỀU LỰA CHỌN'), cols=CR, moc=True,
      cards=[('15.000 ha', 'Philippines đang trồng', 'Dự kiến 150 nghìn tấn'), ('Dưới 1%', 'Thị phần Philippines ở TQ', 'Dư địa còn lớn'), ('12 ngày', 'Malaysia thử chở đường biển', 'Giữ được độ tươi')],
      say=("Và khách hàng lớn ấy đang có thêm người bán. Philippines có khoảng mười lăm nghìn héc ta sầu riêng, dự kiến một trăm năm mươi nghìn tấn niên vụ tới, thị phần ở Trung Quốc hiện còn rất nhỏ. "
           "Malaysia vừa thử chở sầu riêng bằng đường biển mười hai ngày mà vẫn giữ được độ tươi. "
           "Thái Lan vẫn là người bán lâu năm.")),
 dict(k='noti', cap=('HIỆP HỘI RAU QUẢ CẢNH BÁO', 'NẾU TRUNG QUỐC SIẾT LẠI'), cols=CR, moc=True, noti=dict(gio='19:30', ngay='Chủ Nhật', items=[
        ('Tin tức', 'Nông sản', 'Hiệp hội Rau quả: nếu Trung Quốc siết kiểm soát, hàng có thể ùn ứ', R_),
        ('Zalo', 'Kho đóng gói', 'Tuần này kho kiểm mẫu kỹ hơn, anh chuẩn bị giấy tờ vùng trồng', V_)]),
      say=("Tối đó, anh Phong đọc một cảnh báo của Tổng thư ký Hiệp hội Rau quả Việt Nam. Theo ông, sầu riêng nhanh chín, khó để lâu nếu không cấp đông sâu. "
           "Nếu Trung Quốc siết kiểm soát chất lượng hoặc giảm nhập, hàng không thông quan kịp sẽ ùn ở kho miền Tây và Tây Nguyên, kéo theo áp lực bán tháo. "
           "Và các thị trường khác chưa đủ sức hấp thụ lượng sầu riêng tươi đó.")),
 dict(k='bars', anh=CT, cap=('THÁNG 2/2025', 'THẤP HƠN CÙNG KỲ 32%'), cols=CR, moc=True, top='RAU QUẢ BÁN SANG TRUNG QUỐC, THÁNG 2 (TRIỆU USD)',
      bars=[('Tháng 2/2024', 195.9, V_, '195,9'), ('Tháng 2/2025', 132.7, R_, '132,7')],
      say=("Đã từng có tháng hụt mạnh. Theo số hải quan, tháng hai năm hai nghìn hai mươi lăm, rau quả bán sang Trung Quốc chỉ còn khoảng một trăm ba mươi ba triệu đô la. Con số đó thấp hơn khoảng ba mươi hai phần trăm so với cùng tháng năm trước. "
           "Đây là rau quả nói chung, so quanh dịp Tết nên chỉ để tham khảo, nhưng nó cho thấy một cửa ra duy nhất có thể hẹp lại nhanh thế nào.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước: cây hồ tiêu', cap=('"HỒI TIÊU ĐƯỢC GIÁ', 'CẢ XÃ ĐUA NHAU TRỒNG"'), cols=CR, moc=True, call=dict(ten='Bố', phu='Đang gọi', mau=V_, loi=[
        'Hồi tiêu được giá, cả xã đua nhau trồng', 'Giá rơi, nhiều nhà bỏ vườn']),
      say=("Đêm đó bố anh Phong gọi điện, kể lại chuyện cây hồ tiêu. "
           "Ông kể: hồi tiêu được giá, cả xã đua nhau trồng. Vài năm sau giá rơi, nhiều nhà bỏ vườn. Mấy gốc tiêu khô ở góc vườn là của thời ấy.")),
 dict(k='giay', cap=('GIÁ TIÊU XUẤT KHẨU', 'MẤT 73,6% TRONG HƠN 3 NĂM'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA CÂY TIÊU', so='Cục Hải quan, WiData', dau='ĐÃ XẢY RA', dieu=[
        ('Giá xuất khẩu bình quân 12/2016', '7,63 USD/KG'),
        ('Giá xuất khẩu bình quân 4/2020', '2,01 USD/KG'),
        ('So với 12/2016, em tự tính', 'MẤT 73,6%'),
        ('Giá tháng 10/2026', '6,58 USD/KG')]),
      say=("Số hải quan cho thấy rõ. Tháng mười hai năm hai nghìn mười sáu, giá xuất khẩu bình quân hạt tiêu khoảng hơn bảy phẩy sáu đô la một ký. "
           "Đến tháng tư năm hai nghìn hai mươi, chỉ còn khoảng hai đô la. Em tự tính: mất bảy mươi ba phẩy sáu phần trăm. "
           "Phải đến năm hai nghìn hai mươi tư giá mới hồi lại, giờ quanh sáu phẩy sáu đô la. Mất hơn bốn năm mới hồi được phần lớn.")),
 dict(k='checklist', anh=TR, cap=('TIÊU NGÀY ẤY, SẦU RIÊNG NAY', 'GIỐNG 2, KHÁC 2'), cols=CC, moc=True,
      items=[('Giá tốt kéo cả vùng trồng theo', R_), ('Nhà vườn dồn vốn vào một cây', R_), ('Sầu riêng có cấp đông, thị trường mới', G_), ('Mã số vùng trồng, truy xuất nguồn gốc', G_)],
      say=("Anh Phong so lại. Giống nhau ở hai điểm: giá tốt kéo cả vùng trồng theo, và nhà vườn dồn vốn vào một cây. "
           "Khác nhau ở hai điểm: sầu riêng đã có đường cấp đông và vài thị trường mới, và giờ có mã số vùng trồng để truy xuất nguồn gốc. "
           "Giá xuất khẩu bình quân đã bắt đầu giảm nhẹ. Chưa ai biết nó sẽ dừng ở đâu.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='cards', ch='Chương 4 – Nhà anh Phong chọn đường nào?', anh=TR, cap=('BA CON ĐƯỜNG', 'CỦA VƯỜN SẦU RIÊNG'), cols=CC, moc=True,
      cards=[('Mở thêm', 'Vay trồng thêm 1 ha', 'Cược giá còn cao'), ('Nâng chuẩn', 'Tăng tỷ lệ trái đẹp', 'Không thêm diện tích'), ('Cửa khác', 'Cấp đông, thị trường khác', 'Hàn Quốc tăng 129%')],
      say=("Anh Phong tính ba con đường. Một: vay tiền trồng thêm một héc ta, cược rằng giá còn cao. "
           "Hai: không thêm diện tích, dồn tiền chăm vườn để tăng tỷ lệ trái đẹp lựa. "
           "Ba: tìm cửa khác, như cấp đông hay thị trường ngoài Trung Quốc. Chín tháng qua, sầu riêng bán sang Hàn Quốc tăng một trăm hai mươi chín phần trăm, từ một nền còn nhỏ.")),
 dict(k='chat', cap=('KẾ HOẠCH NHÀ ANH PHONG', 'KHÔNG VAY TRỒNG THÊM'), cols=CC, moc=True, chat=dict(ten='Nga', tv='Đang hoạt động', gio='21:30', mau=G_, msgs=[
        ('me', 'Năm nay mình không vay trồng thêm'),
        ('Nga', 'Tiền bán vụ này trả nợ phân trước đã anh'),
        ('me', 'Gửi thử 3 tấn hàng xô vào kho cấp đông')]),
      say=("Hai vợ chồng chốt kế hoạch. Anh Phong nhắn: năm nay mình không vay trồng thêm. "
           "Chị Nga đáp: tiền bán vụ này trả hết nợ phân bón trước. "
           "Anh gửi thử ba tấn hàng xô vào kho cấp đông. Không ai biết chắc giá sầu riêng năm sau, nên hai vợ chồng chọn bớt rủi ro trước khi nghĩ đến lời thêm.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Huy Nguyễn ghép ba chi tiết', anh=SR, cap=('3 CHI TIẾT ĐẦU PHIM', 'GHÉP LẠI THÀNH LỜI GIẢI'), cols=CC, moc=True,
      items=[('1. 54 và 25 nghìn: chuẩn quyết định giá', V_), ('2. Gốc tiêu khô: giá rơi lúc đang nợ', R_), ('3. Thùng Hàn Quốc: một cửa ra nhỏ', X_)],
      say=("Giờ quay lại ba chi tiết đầu phim. Chi tiết thứ nhất, cùng một cây mà năm mươi tư nghìn và hai mươi lăm nghìn. Khi người mua có nhiều lựa chọn, thứ quyết định giá là trái có đạt chuẩn hay không, không phải là kỷ lục xuất khẩu. "
           "Chi tiết thứ hai, mấy gốc tiêu khô. Giá tiêu từng mất gần ba phần tư. Đêm đó ông nội còn kể thêm một điều: những nhà mất hẳn vườn thường là nhà đang gánh nợ. Giá thì nhà vườn không quyết được, còn nợ thì quyết được.")),
 dict(k='checklist', anh=CT, cap=('LỜI GIẢI CHO CÂU HỎI CỦA LINH', 'KỶ LỤC MÀ VẪN LO'), cols=CC, moc=True,
      items=[('Bán được nhiều, nhưng giá mỗi ký giảm', R_), ('96% vào một khách hàng', R_), ('Lo đúng chỗ: chuẩn, nợ, cửa ra', G_)],
      say=("Chi tiết thứ ba, chồng thùng ghi Hàn Quốc. Đó là một cửa ra nhỏ, nhưng có thật. "
           "Ghép ba chi tiết lại, đó là câu trả lời cho Linh. Kỷ lục mà vẫn lo, vì tiền về nhiều nhờ bán nhiều hàng, trong khi giá mỗi ký lại giảm. Và gần như tất cả đi qua một cửa. "
           "Lo đúng chỗ là lo ba thứ: trái có đạt chuẩn không, nhà có đang vay không, và đã có cửa ra nào khác chưa.")),
 dict(k='checklist', anh=TP, cap=('PHÉP THỬ CỦA ANH CHỊ', 'MỘT MÓN HÀNG, MỘT KHÁCH HÀNG?'), cols=CC, moc=True,
      items=[('Thu nhập nhà mình từ mấy nguồn?', X_), ('Nguồn lớn nhất chiếm bao nhiêu?', X_), ('Trên 50% và đang vay: soi kỹ', R_)],
      say=("Phép thử cho anh chị, kể cả khi không trồng sầu riêng: thu nhập cả nhà mình đến từ mấy nguồn, và nguồn lớn nhất chiếm bao nhiêu phần trăm? "
           "Nếu một nguồn chiếm hơn một nửa, lại đang có khoản vay đi kèm, thì nhà mình cũng đang giống vườn sầu riêng: một món hàng, một khách hàng. "
           "Mốc này em đặt ra để tự soi, không phải quy tắc.")),
 dict(k='checklist', ch='Chương 6 – Theo dõi gì để biết sớm?', anh=BX, cap=('3 ĐIỀU CẦN THEO DÕI', 'TRƯỚC VỤ SAU'), cols=CC, moc=True,
      items=[('Xuất khẩu sầu riêng mỗi tháng', V_), ('Giá RI6 hàng xô ở Tây Nguyên', R_), ('Mã số vùng trồng, kiểm tra ở cửa khẩu', V_)],
      say=("Em gợi ý theo dõi ba điều. "
           "Một: số xuất khẩu sầu riêng hằng tháng, nhất là phần sang Trung Quốc. "
           "Hai: giá RI sáu hàng xô ở Tây Nguyên, vì hàng xô luôn bị ép giá trước. "
           "Ba: việc cấp mã số vùng trồng và kiểm tra ở cửa khẩu. Số liệu xuất nhập khẩu từng tháng, anh chị xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn của ông nội', cap=('"ĐỪNG TRỒNG THEO GIÁ', 'TRỒNG THEO SỨC MÌNH"'), cols=CC, moc=True, chat=dict(ten='Bố', tv='Đang hoạt động', gio='23:00', mau=V_, msgs=[
        ('Bố', 'Đừng trồng theo giá, trồng theo sức mình con ạ'),
        ('Bố', 'Không nợ thì giá rơi vẫn còn vườn'),
        ('me', 'Dạ, năm nay con không vay thêm')]),
      say=("Gần nửa đêm, bố anh Phong nhắn: đừng trồng theo giá, trồng theo sức mình, không nợ thì giá rơi vẫn còn vườn. "
           "Kỷ lục gần ba phẩy năm tỷ đô la là thật. Nhưng với từng nhà vườn, câu hỏi không phải cả nước bán được bao nhiêu, mà là nhà mình đứng ở đâu khi người mua đổi ý.")),
 dict(k='end', cap=('GIÁ RI6 HÀNG XÔ Ở VƯỜN', 'HÔM NAY BAO NHIÊU?'), cols=CC,
      say=("Còn anh chị thì sao: nếu nhà mình trồng sầu riêng, giá RI sáu hàng xô ở vườn hôm nay là bao nhiêu, và năm nay có vay trồng thêm không? "
           "Kể cho em và mọi người ở phần bình luận nhé. Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Sầu Riêng Xuất Khẩu Kỷ Lục 3,45 Tỷ USD Mà Nhà Vườn Vẫn Lo? 96% Bán Cho Một Khách – Có Thành Hồ Tiêu?'
MT = ("Sầu riêng xuất khẩu 9 tháng 2026 đạt 3,45 tỷ USD, gần 96% sang Trung Quốc; diện tích khoảng 200.000 ha, gần gấp đôi quy hoạch đã nâng. "
      "Kim ngạch tăng nhờ bán nhiều hơn, còn giá xuất khẩu bình quân sầu riêng tươi lại giảm; ở Tây Nguyên RI6 đẹp lựa 52–54 nghìn, hàng xô 25–30 nghìn. "
      "Việt Nam cũng nhập 2,82 tỷ USD rau quả trong 10 tháng; Philippines, Malaysia đang chen vào thị trường Trung Quốc. Lần trước, giá tiêu xuất khẩu từ 12/2016 đến 4/2020 mất 73,6%. "
      "Câu chuyện nhà anh Phong ở Đắk Lắk và phép thử 'một món hàng, một khách hàng'.\n\n"
      "Nguồn số liệu:\n"
      "• Vietnambiz 3/11/2026 và 5/11/2026 (Cục Hải quan): xuất khẩu sầu riêng 9 tháng 2026 đạt 3,45 tỷ USD (+25%); sang Trung Quốc gần 3,3 tỷ USD (+27,6%), gần 96% (cùng kỳ 93,6%); tháng 9 hơn 729 triệu USD, giảm 23,8% so tháng 8 và giảm 25% so cùng kỳ năm 2025; sang Hàn Quốc +129%; "
      "Hiệp hội Rau quả Việt Nam: Trung Quốc chuộng sầu riêng tươi; sầu riêng nhanh chín, khó bảo quản dài ngày nếu không cấp đông sâu; nếu siết kiểm soát chất lượng hoặc giảm nhập, hàng ùn ứ tại kho miền Tây, Tây Nguyên, áp lực bán tháo; các thị trường khác chưa đủ sức hấp thụ\n"
      "• Vietnambiz 29/9/2026 (Cục Hải quan): 8 tháng 2026 sầu riêng 2,72 tỷ USD (+55%), chiếm 44,3% xuất khẩu rau quả; giá xuất khẩu bình quân sầu riêng tươi giảm 3,3% còn 3.269 USD/tấn\n"
      "• Trung tâm WTO và Hội nhập (VCCI), VnEconomy 15/10/2026: quy hoạch ban đầu 65.000–75.000 ha đến 2030, điều chỉnh lên 100.000–110.000 ha; thực tế năm 2026 khoảng 200.000 ha\n"
      "• Người Đưa Tin 25/10/2026: khoảng 200.000 ha, sản lượng dự kiến 2,08 triệu tấn năm 2026\n"
      "• Doanh Nhân Việt Nam 9/11/2026: giá thu mua Tây Nguyên – RI6 đẹp lựa 52.000–54.000 đ/kg, RI6 xô 25.000–30.000; Thái đẹp lựa 72.000–74.000, Thái xô 32.000–35.000\n"
      "• Vietnambiz 25/9/2026 (Cục Xuất nhập khẩu, Bộ Công Thương): Philippines khoảng 15.000 ha, dự kiến 150 nghìn tấn niên vụ 2026/2027, chưa đến 1% thị phần Trung Quốc; Người Đưa Tin 22/9/2026: Malaysia thử vận chuyển sầu riêng đường biển 12 ngày đến Trung Quốc\n"
      "• WiData (Cục Hải quan): xuất khẩu rau quả 10 tháng 2026 khoảng 8,29 tỷ USD (10 tháng 2025: 7,07 tỷ), sang Trung Quốc khoảng 5,42 tỷ (65%); nhập khẩu rau quả 10 tháng 2026 khoảng 2,82 tỷ USD; "
      "rau quả sang Trung Quốc tháng 2/2025 132,7 triệu USD, tháng 2/2024 195,9 triệu USD\n"
      "• WiData (Cục Hải quan): giá xuất khẩu bình quân hạt tiêu 12/2016 7,63 USD/kg; 4/2020 2,01 USD/kg; 9/2024 6,46 USD/kg; 10/2026 6,58 USD/kg\n"
      "• Em tự tính: 2,01 / 7,63 − 1 ≈ −73,6%; 132,7 / 195,9 − 1 ≈ −32%; 5,42 / 8,29 ≈ 65%. Vườn anh Phong là giả định minh hoạ: 30 tấn, nửa hàng xô 15 tấn × chênh 25.000 đ/kg = 375 triệu đồng\n\n"
      "Số liệu xuất nhập khẩu, vĩ mô từng tháng: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật anh Phong, chị Nga, Linh và ông nội là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán hay tư vấn đầu tư.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-29', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['sầu riêng', 'xuất khẩu sầu riêng', 'giá sầu riêng', 'sầu riêng Trung Quốc', 'xuất khẩu rau quả', 'nông sản Việt Nam', 'hồ tiêu', 'kinh tế Việt Nam', 'vĩ mô', 'tài chính cá nhân'],
    bia_hook=['3,45 TỶ USD', 'MÀ VẪN LO?'], badge='SẦU RIÊNG 9 THÁNG 2026',
    bia_anh='Durian fruit||Durian fruit',
    bia_hook_b=['ĐẸP 54 NGHÌN', 'XÔ 25 NGHÌN'], badge_b='GIÁ TÂY NGUYÊN 9/11',
    bia_hook_c=['96% BÁN CHO', 'MỘT KHÁCH'], badge_c='CÓ THÀNH HỒ TIÊU?',
    reel_hook='SẦU RIÊNG XUẤT KHẨU KỶ LỤC|SAO NHÀ VƯỜN VẪN LO???',
    fb_post=("Sầu riêng xuất khẩu 9 tháng đạt 3,45 tỷ USD – kỷ lục, nhưng... 🍈\n\n👉 Gần 96% bán sang Trung Quốc\n👉 Diện tích khoảng 200.000 ha, gần gấp đôi quy hoạch\n"
             "👉 Tây Nguyên: RI6 đẹp 52–54 nghìn, hàng xô 25–30 nghìn\n👉 Giá tiêu xuất khẩu từng mất 73,6% (12/2016 – 4/2020)\n\nThu nhập nhà anh chị có mấy cửa ra?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: sầu riêng xuất khẩu kỷ lục, gần hết sang Trung Quốc, bài học hồ tiêu (NV1 20/11/2026).\n"
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
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
from xung_ho import le_phep
for c in S:
    if le_phep(c['say']) != c['say']: print('XUNG_HO', c['say'][:80])
for c in S:
    for x in c.get('cards', []):
        for y in x:
            if len(y) > 30: print('CARD DAI', y)
    for x in c.get('items', []):
        if len(x[0]) > 40: print('ITEM DAI', len(x[0]), x[0])
    for x in c.get('cap', ()):
        if len(x) > 30: print('CAP DAI', len(x), x)
