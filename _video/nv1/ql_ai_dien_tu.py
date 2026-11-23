# -*- coding: utf-8 -*-
# NV1 22/11/2026 – VIDEO DÀI kênh chính, "câu hỏi lớn về tiền": Mỹ mất 2.500 tỷ USD cổ phiếu công nghệ trong một phiên – còn Việt Nam xuất 149 tỷ USD hàng điện tử nhờ cơn sốt AI: nếu AI hạ nhiệt, túi ai đau?
#   Khuôn "so với lần trước" (năm 2023 điện thoại xuất khẩu giảm sau cơn sốt thời Covid; Nasdaq 2000–2002) + phép thử "thu nhập nhà mình dựa vào một ngành bao nhiêu %".
# Lý do chọn: data/view/xu_huong.md tuần tới 21/11 – "Vàng cắm đầu, AI bốc hơi 2.500 tỷ USD, USD trỗi dậy" ~63 nghìn view; "Nvidia… khi người hùng thành gánh nặng" ~67 nghìn (VTV24).
#   Chủ đề THẾ GIỚI/CÚ SẬP + TIỀN TÚI NGƯỜI THƯỜNG (việc làm khu công nghiệp). 7 ngày qua chưa làm AI/điện tử (CH1711XK 17/11 nói tổng xuất khẩu & FDI – khác góc, cách 15 ngày).
# Nguồn:
#  - Nhà Đầu Tư 12/11/2026: phiên 5/11 Nasdaq Composite −5,52%, S&P 500 −4,36%, chỉ số bán dẫn SOX giảm hơn 12%; Nasdaq 100 −6,4%, xóa khoảng 2.500 tỷ USD vốn hóa; câu hỏi khả năng hoàn vốn của cuộc đua AI nghìn tỷ USD.
#  - Nhà Đầu Tư 13/11/2026: Nvidia so với đỉnh đầu tháng 10 giảm khoảng 1/3; mất gần 1.000 tỷ USD vốn hóa trong tháng 11 (NYT).
#  - Doanh Nhân Việt Nam 18/11/2026: Nvidia quý III năm tài chính 2027 (kết thúc 25/10/2026) doanh thu 116 tỷ USD (+103%), lợi nhuận ròng 65 tỷ USD – cao nhất từ trước đến nay; dự báo quý IV khoảng 130 tỷ USD.
#  - WiData (số liệu hải quan): xuất khẩu máy vi tính, sản phẩm điện tử và linh kiện luỹ kế 10 tháng: 2023 46.523,6 triệu USD; 2024 59.022,5; 2025 87.392,3; 2026 149.407,5 (tháng 10/2026 riêng 25.748,3);
#    tổng xuất khẩu 10 tháng 2026 498.803,7 triệu USD (2025: 391.607,1); nhập khẩu máy vi tính, sản phẩm điện tử và linh kiện 10 tháng 2026 215.250,1 triệu USD.
#    Điện thoại và linh kiện xuất khẩu cả năm: 2022 58.006,0 → 2023 52.372,8 triệu USD.
#  - Tạp chí Kinh tế – Tài chính, đăng lại Trung tâm WTO (VCCI) 30/10/2026, số đến 15/10/2026: xuất khẩu nhóm 135,31 tỷ USD (+65,2%), đóng góp gần 56% mức tăng xuất khẩu cả nước; nhập khẩu nhóm 201,12 tỷ USD (+72,9%);
#    nhập siêu nhóm từ 34,41 lên 65,81 tỷ USD; cán cân thương mại cả nước từ xuất siêu 17,55 tỷ chuyển sang nhập siêu 17,66 tỷ USD.
#    (dùng ở cảnh bignum 39,6%) Nửa đầu tháng 10/2026: xuất khẩu nhóm 11,59 tỷ USD (+163,6%), chiếm 39,63% xuất khẩu cả nước trong kỳ.
#  - VnEconomy 10/7/2026: Hiệp hội Doanh nghiệp điện tử VN dự báo xuất khẩu điện tử 2026 có thể tăng 15–20% nhờ đầu tư AI, trung tâm dữ liệu; tỷ lệ nội địa hóa thấp ở nhiều phân khúc, giá trị giữ lại trong nước còn thấp, phụ thuộc linh kiện nhập.
#  - Thời báo Ngân hàng 1/11/2026: Hàn Quốc xuất khẩu tháng 10 +93,7% (cao nhất từ 1/1974), bán dẫn +259,4%, máy tính +496,6% chủ yếu nhờ máy chủ AI.
#  - Lịch sử Nasdaq Composite: đỉnh 5.048,62 (10/3/2000), đáy 1.114,11 (9/10/2002), giảm khoảng 78%.
# TỰ TÍNH: 149.407,5 / 87.392,3 = +71%; / 46.523,6 = 3,2 lần; 149.407,5 / 498.803,7 = 30%; phần tăng thêm: (149.407,5 − 87.392,3) / (498.803,7 − 391.607,1) = 62.015 / 107.197 = 58%.
#   Điện thoại 2023 so với 2022: 52.372,8 / 58.006,0 − 1 = −9,7%.
#   Nhà anh Tuấn (giả định): lương 14 triệu (cứng 10, tăng ca 4); quán cơm của vợ lãi 16 triệu/tháng, khoảng 10 triệu từ khách công nhân → thu nhập 30 triệu; phần dựa vào đơn hàng điện tử 4 + 10 = 14 / 30 ≈ 47%.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261122_0200'
KEY = 'CH0212AI'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
HA = 'ov:Hanoi apartment buildings||Hanoi skyline night'
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HX = 'ov:Ho Chi Minh City Stock Exchange||Ho Chi Minh City skyline night'
CT = 'ov:Container ship||Ho Chi Minh City skyline night'
BX = 'ov:Bitexco Financial Tower||Ho Chi Minh City skyline night'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('CHỨNG KHOÁN MỸ', 'BỐC HƠI 2.500 TỶ USD'), cols=CR, noti=dict(gio='05:50', ngay='Thứ Sáu', items=[
        ('Tin tức', 'Thế giới', 'Cổ phiếu công nghệ Mỹ bốc hơi 2.500 tỷ USD trong một phiên vì lo bong bóng AI', R_),
        ('Zalo', 'Tổ chuyền', 'Tháng 12 vẫn tăng ca 3 tối mỗi tuần nhé anh em', G_),
        ('Zalo', 'Vợ', 'TV bảo chứng khoán Mỹ sập, công ty anh có cắt ca không?', V_)]),
      say=("Năm giờ năm mươi sáng, anh Tuấn, tổ trưởng một chuyền lắp ráp bo mạch điện tử ở Bắc Giang, đọc ba tin liền nhau. "
           "Cổ phiếu công nghệ Mỹ mới bốc hơi khoảng hai nghìn năm trăm tỷ đô la chỉ trong một phiên, vì lo bong bóng trí tuệ nhân tạo, hay AI. "
           "Nhóm chuyền báo tháng mười hai vẫn tăng ca ba tối mỗi tuần. "
           "Và vợ anh, chủ quán cơm trước cổng khu công nghiệp, hỏi: tivi bảo chứng khoán Mỹ sập, công ty anh có cắt ca không?")),
 dict(k='bignum', anh=HA, cap=('GẦN NỬA THU NHẬP NHÀ', 'DỰA VÀO MỘT THỨ'), cols=CR, moc=True, value=47, fmt='{:,.0f}', unit='%', top='PHẦN THU NHẬP NHÀ ANH TUẤN DỰA VÀO ĐƠN HÀNG ĐIỆN TỬ (GIẢ ĐỊNH, EM TỰ TÍNH)',
      sub='Tiền tăng ca và khách công nhân của quán cơm', col=RED,
      say=("Câu hỏi đó không nhỏ. Em tính thử: gần một nửa thu nhập nhà anh Tuấn, gồm tiền tăng ca và phần lớn khách của quán cơm, đang dựa vào một thứ: đơn hàng điện tử còn nhiều hay không. "
           "Hôm nay em cùng anh chị trả lời: nếu cơn sốt AI hạ nhiệt, ở Việt Nam túi tiền của ai đau trước?")),
 dict(k='bignum', anh=CT, cap=('VIỆT NAM XUẤT ĐIỆN TỬ', '149 TỶ USD TRONG 10 THÁNG'), cols=CC, moc=True, value=149.4, fmt='{:,.1f}', unit=' TỶ USD', top='XUẤT KHẨU MÁY VI TÍNH, SẢN PHẨM ĐIỆN TỬ VÀ LINH KIỆN, 10 THÁNG 2026',
      sub='Tăng 71% so với cùng kỳ, gấp 3,2 lần năm 2023, chiếm 30% tổng xuất khẩu – hải quan qua WiData', col=GOLD,
      say=("Vì đơn hàng đang nhiều thật. Mười tháng năm nay, Việt Nam xuất khẩu máy vi tính, sản phẩm điện tử và linh kiện gần một trăm năm mươi tỷ đô la. "
           "Con số đó tăng bảy mươi mốt phần trăm so với cùng kỳ, gấp hơn ba lần mười tháng năm hai nghìn không trăm hai mươi ba. Nó chiếm khoảng ba mươi phần trăm tổng xuất khẩu cả nước.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='bignum', ch='Chương 1 – Cú lật: lãi kỷ lục, cổ phiếu đã giảm từ trước', anh=HX, cap=('LÃI KỶ LỤC 65 TỶ USD', 'MỘT QUÝ'), cols=CR, moc=True, value=65, fmt='{:,.0f}', unit=' TỶ USD', top='LỢI NHUẬN MỘT QUÝ CỦA HÃNG CHIP AI LỚN NHẤT, QUÝ KẾT THÚC 25/10/2026',
      sub='Doanh thu 116 tỷ USD, tăng 103% – Doanh Nhân Việt Nam 18/11/2026', col=GOLD,
      say=("Vậy AI có phải bong bóng? Đây là cú lật thứ nhất. Hai tuần sau phiên đó, hãng chip AI lớn nhất thế giới báo một quý lãi sáu mươi lăm tỷ đô la, cao nhất từ trước đến nay, doanh thu tăng gấp đôi. "
           "Nhưng trước khi báo con số đó, cổ phiếu của hãng đã giảm khoảng ba mươi ba phần trăm so với đỉnh đầu tháng mười.")),
 dict(k='text', anh=HX, cap=('THỊ TRƯỜNG KHÔNG HỎI HÔM NAY', 'MÀ HỎI NĂM SAU'), cols=CC,
      say=("Lãi hôm nay là thật. Nhưng giá cổ phiếu trả tiền cho tương lai. Nhà đầu tư đang hỏi: các tập đoàn chi hàng trăm tỷ đô la xây trung tâm dữ liệu, liệu có thu lại được tiền không.")),
 dict(k='cards', anh=HX, cap=('PHIÊN NGÀY 5/11', 'CHỈ TRONG MỘT NGÀY'), cols=CR, moc=True,
      cards=[('5,52%', 'Nasdaq Composite giảm', 'Phiên 5/11'), ('Hơn 12%', 'Chỉ số bán dẫn giảm', 'Cùng phiên'), ('2.500 tỷ USD', 'Nasdaq 100 bốc hơi', 'Giảm 6,4%')],
      say=("Phiên ngày năm tháng mười một là lúc nỗi lo bùng ra. Chỉ số Nasdaq tổng hợp giảm hơn năm phần trăm, chỉ số các hãng bán dẫn giảm hơn mười hai phần trăm. "
           "Riêng nhóm một trăm công ty lớn trên sàn này mất khoảng hai nghìn năm trăm tỷ đô la vốn hóa trong một ngày.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='giay', ch='Chương 2 – Vì sao hàng điện tử bán chạy?', cap=('MÁY CHỦ AI', 'KÉO CẢ CHÂU Á'), cols=CC, moc=True, giay=dict(tieu_de='TIN XUẤT KHẨU', so='Thời báo Ngân hàng 1/11, VnEconomy 10/7/2026', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Hàn Quốc tháng 10: xuất khẩu', '+93,7%'),
        ('Hàn Quốc: máy tính, nhờ máy chủ AI', '+496,6%'),
        ('Dự báo tháng 7: điện tử VN 2026', '+15 ĐẾN 20%'),
        ('10 tháng, số hải quan', '+71%')]),
      say=("Vì sao hàng điện tử bán chạy đến vậy? Nhìn sang Hàn Quốc: tháng mười, máy tính xuất khẩu của họ gấp gần sáu lần cùng kỳ, chủ yếu nhờ máy chủ phục vụ AI. "
           "Ở Việt Nam, hồi tháng bảy, hiệp hội ngành điện tử chỉ dự báo năm nay tăng mười lăm đến hai mươi phần trăm. Theo số hải quan, mới mười tháng đã tăng hơn bảy mươi phần trăm.")),
 dict(k='chat', cap=('"QUÁN EM ĐÔNG', 'CŨNG NHỜ CÁI AI ĐẤY À?"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='12:15', mau=V_, msgs=[
        ('Vợ', 'Sao dạo này công ty anh nhiều đơn thế?'),
        ('me', 'Sếp bảo bo mạch đi lắp máy chủ AI bên Mỹ'),
        ('Vợ', 'Thế quán em đông cũng nhờ cái AI đấy à?')]),
      say=("Trưa đó vợ anh Tuấn nhắn: sao dạo này công ty anh nhiều đơn thế? "
           "Anh trả lời: sếp bảo bo mạch chuyền anh đi lắp máy chủ AI bên Mỹ. "
           "Chị nhắn lại, nửa đùa nửa thật: thế quán em đông cũng nhờ cái AI đấy à?")),
 dict(k='bignum', anh=CT, cap=('NỬA ĐẦU THÁNG 10', 'GẦN 40% LÀ HÀNG ĐIỆN TỬ'), cols=CR, moc=True, value=39.6, fmt='{:,.1f}', unit='%', top='TỶ TRỌNG NHÓM ĐIỆN TỬ TRONG XUẤT KHẨU CẢ NƯỚC, NỬA ĐẦU THÁNG 10/2026',
      sub='11,59 tỷ USD, tăng 163,6% – Tạp chí Kinh tế – Tài chính, VCCI 30/10/2026', col=RED,
      say=("Có thời điểm còn dồn hơn nữa. Trong nửa đầu tháng mười, cứ mười đô la Việt Nam xuất khẩu thì gần bốn đô la là hàng điện tử. "
           "Một nhóm hàng kéo cả nền xuất khẩu là tin vui khi đơn nhiều. Nhưng nó cũng có nghĩa: nếu nhóm này chậm lại, cả bức tranh sẽ đổi màu rất nhanh.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='giay', ch='Chương 3 – Cú lật thứ hai: xuất nhiều, nhập còn nhiều hơn', cap=('ĐẾN GIỮA THÁNG 10', 'XUẤT 135 TỶ, NHẬP 201 TỶ'), cols=CR, moc=True, giay=dict(tieu_de='NHÓM ĐIỆN TỬ ĐẾN 15/10/2026', so='Tạp chí Kinh tế – Tài chính, VCCI 30/10/2026', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Xuất khẩu nhóm điện tử', '135,31 TỶ USD'),
        ('Nhập khẩu cùng nhóm', '201,12 TỶ USD'),
        ('Nhập nhiều hơn xuất', '65,81 TỶ USD'),
        ('Cán cân cả nước', 'NHẬP SIÊU 17,66 TỶ')]),
      say=("Cú lật thứ hai nằm ở tờ số liệu tính đến giữa tháng mười. Nhóm điện tử xuất đi khoảng một trăm ba mươi lăm tỷ đô la, nhưng cùng nhóm đó Việt Nam nhập về hơn hai trăm tỷ đô la. "
           "Có những linh kiện nhập về được dùng cho nhóm hàng khác như điện thoại, nên không thể nói nhóm này lỗ. Điểm chính là hàng xuất đi rất nhiều, nhưng phần giá trị ở lại Việt Nam không lớn như con số xuất khẩu. Cả nước cũng đã chuyển từ xuất siêu sang nhập siêu.")),
 dict(k='cards', anh=CT, cap=('TIỀN Ở LẠI VIỆT NAM', 'NẰM Ở ĐÂU?'), cols=CC, moc=True,
      cards=[('Nhập về', 'Chip, linh kiện giá trị cao', 'Lắp ráp rồi xuất đi'), ('Ở lại', 'Tiền công, thuê đất, dịch vụ', 'Quanh khu công nghiệp'), ('Còn thấp', 'Giá trị giữ lại trong nước', 'VnEconomy 10/7/2026')],
      say=("Hiệp hội ngành điện tử cũng thừa nhận tỷ lệ nội địa hóa còn thấp ở nhiều phân khúc, giá trị giữ lại trong nước chưa cao. "
           "Theo em, phần tiền ở lại Việt Nam nằm nhiều ở tiền công, tiền thuê đất, và dịch vụ quanh khu công nghiệp, như quán cơm của vợ anh Tuấn. Đó cũng là những phần nhạy nhất khi đơn hàng chậm lại.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='call', ch='Chương 4 – Lần trước: sau cơn sốt điện thoại', cap=('"NĂM 2023 XƯỞNG ANH', 'CẮT TĂNG CA MẤY THÁNG"'), cols=CR, moc=True, call=dict(ten='Anh Phong', phu='Đang gọi', mau=R_, loi=[
        'Năm 2023 xưởng điện thoại anh cắt tăng ca mấy tháng', 'Chỉ còn lương cứng, anh nhận thêm việc buổi tối']),
      say=("Tối đó, anh Phong, đồng nghiệp cũ của anh Tuấn, gọi điện. Anh Phong kể: năm hai nghìn không trăm hai mươi ba, xưởng điện thoại chỗ anh cắt tăng ca mấy tháng liền. "
           "Chỉ còn lương cứng, anh phải nhận thêm việc buổi tối cho đủ tiền nhà.")),
 dict(k='giay', cap=('LẦN TRƯỚC: ĐIỆN THOẠI', 'XUẤT KHẨU GIẢM 9,7%'), cols=CR, moc=True, giay=dict(tieu_de='NHÓM ĐIỆN THOẠI, LẦN TRƯỚC', so='Số liệu hải quan qua WiData', dau='ĐÃ XẢY RA', dieu=[
        ('Xuất khẩu điện thoại 2022', '58 TỶ USD'),
        ('Xuất khẩu điện thoại 2023', '52,4 TỶ USD'),
        ('Thay đổi', 'GIẢM 9,7%'),
        ('Bối cảnh, em nhận định', 'SAU CƠN SỐT COVID')]),
      say=("Câu chuyện của anh Phong phù hợp với xu hướng số liệu. Sau cơn sốt mua thiết bị thời Covid, xuất khẩu điện thoại, một nhóm hàng khác, năm hai nghìn không trăm hai mươi ba giảm gần mười phần trăm. Nó đi từ năm mươi tám tỷ xuống khoảng năm mươi hai tỷ đô la. "
           "Chỉ giảm chưa tới mười phần trăm, nhưng theo em, với người làm công, phần bị cắt đầu tiên thường là tăng ca.")),
 dict(k='bars', anh=CT, cap=('XUẤT KHẨU ĐIỆN TỬ 10 THÁNG', 'ĐI LÊN NHƯ THẾ NÀO'), cols=CC, moc=True, top='MÁY VI TÍNH, ĐIỆN TỬ, LINH KIỆN – 10 THÁNG (TỶ USD)',
      bars=[('2023', 46.5, G_, '46,5'), ('2024', 59.0, G_, '59'), ('2025', 87.4, V_, '87,4'), ('2026', 149.4, R_, '149,4')],
      say=("Còn nhóm máy tính, điện tử thì đi lên rất dốc. Mười tháng năm hai nghìn không trăm hai mươi ba khoảng bốn mươi sáu tỷ rưỡi, năm ngoái hơn tám mươi bảy tỷ, năm nay gần một trăm năm mươi tỷ đô la. "
           "Đi lên càng dốc, một nhịp chững lại càng dễ thấy trong bảng lương.")),
 dict(k='checklist', anh=HN, cap=('LẦN TRƯỚC VÀ LẦN NÀY', 'GIỐNG 2, KHÁC 2'), cols=CC, moc=True,
      items=[('Một làn sóng công nghệ kéo đơn hàng', R_), ('Đơn hàng có thể quay đầu khi hết sốt', R_), ('Hãng dẫn đầu vẫn lãi kỷ lục', G_), ('Hàng mới: máy chủ, không chỉ điện thoại', G_)],
      say=("Anh Tuấn so lần trước với lần này. Giống nhau hai điểm: đơn hàng tăng vọt nhờ một làn sóng công nghệ, và đơn hàng có thể quay đầu khi cơn sốt qua đi. "
           "Khác nhau cũng hai điểm. Hãng dẫn đầu vẫn lãi kỷ lục, và dự báo quý sau doanh thu khoảng một trăm ba mươi tỷ đô la. Hàng Việt Nam làm giờ là máy chủ, không chỉ điện thoại. "
           "Chưa chắc đơn hàng sẽ giảm. Nhưng chưa, không có nghĩa là không thể.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='giay', ch='Chương 5 – Phép tính nhà anh Tuấn', short=True, cap=('THU NHẬP 30 TRIỆU', '14 TRIỆU NHỜ ĐƠN ĐIỆN TỬ'), cols=CR, moc=True, giay=dict(tieu_de='SỔ THU NHẬP NHÀ ANH TUẤN', so='Em giả định, em tự tính', dau='TỰ TÍNH', dieu=[
        ('Lương cứng của anh Tuấn', '10 TRIỆU'),
        ('Tiền tăng ca', '4 TRIỆU'),
        ('Lãi quán, khách công nhân điện tử', '10 TRIỆU'),
        ('Lãi quán, từ khách khác', '6 TRIỆU')]),
      say=("Giờ là sổ thu nhập nhà anh Tuấn, em giả định. Lương cứng mười triệu, tăng ca thêm bốn triệu mỗi tháng. "
           "Quán cơm của vợ mỗi tháng lãi khoảng mười sáu triệu đồng, trong đó khoảng mười triệu đồng nhờ khách là công nhân các nhà máy điện tử quanh đó. "
           "Cả nhà khoảng ba mươi triệu đồng mỗi tháng.")),
 dict(k='bignum', anh=HA, cap=('14 TRÊN 30 TRIỆU', 'DỰA VÀO MỘT NGÀNH'), cols=CR, moc=True, value=47, fmt='{:,.0f}', unit='%', top='PHẦN THU NHẬP NHÀ ANH TUẤN DỰA VÀO ĐƠN HÀNG ĐIỆN TỬ (EM TỰ TÍNH)',
      sub='Tăng ca 4 triệu + khách công nhân 10 triệu, trên tổng 30 triệu', col=RED,
      say=("Tiền tăng ca và phần lãi từ khách công nhân cộng lại mười bốn triệu, gần một nửa thu nhập cả nhà. "
           "Nếu đơn chững lại như lần trước, tăng ca bị cắt trước, rồi quán cơm vắng sau. Lương cứng còn, nếu không bị giảm giờ hay cắt người.")),
 dict(k='chat', cap=('"HỒI ĐÓ AI VAY THEO', 'TIỀN TĂNG CA THÌ KHỔ"'), cols=CR, moc=True, chat=dict(ten='Anh Phong', tv='Đang hoạt động', gio='21:40', mau=R_, msgs=[
        ('Anh Phong', 'Hồi đó ai để riêng được tiền tăng ca thì đỡ'),
        ('Anh Phong', 'Ai trả góp xe, điện thoại bằng tiền tăng ca thì khổ'),
        ('me', 'Em đang trả góp cái xe 2 triệu mỗi tháng anh ạ')]),
      say=("Anh Phong nhắn thêm một câu từ kinh nghiệm: hồi đó, ai để riêng được tiền tăng ca thì đỡ. Ai trả góp xe, trả góp điện thoại bằng tiền tăng ca thì khổ. "
           "Anh Tuấn giật mình: chính anh đang trả góp cái xe máy hai triệu đồng mỗi tháng, và khoản đó đang lấy từ tiền tăng ca.")),
 dict(k='cards', anh=TP, cap=('3 CÁCH CỦA NHÀ ANH TUẤN', 'KHÔNG CÓ CÁCH NÀO MIỄN PHÍ'), cols=CC, moc=True,
      cards=[('Sổ riêng', 'Sống bằng lương cứng', 'Để riêng tiền tăng ca'), ('Thêm khách', 'Quán nhận cơm văn phòng', 'Thêm việc, thêm giờ'), ('Học nghề', 'Bảo trì máy, kiểm tra lỗi', 'Mất thời gian, học phí')],
      say=("Hai vợ chồng tính ba cách. Một: sống bằng lương cứng, để riêng toàn bộ tiền tăng ca, đổi lại chi tiêu chặt hơn. "
           "Hai: quán nhận thêm cơm văn phòng, bớt phụ thuộc vào ca của nhà máy, đổi lại thêm việc. "
           "Ba: anh Tuấn học thêm bảo trì máy hay kiểm tra lỗi, những việc vẫn cần khi đơn ít đi, đổi lại tốn thời gian và học phí. Không có cách nào miễn phí.")),
 dict(k='chat', cap=('"TIỀN TĂNG CA', 'MÌNH KHÔNG TIÊU NỮA"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:20', mau=V_, msgs=[
        ('me', 'Từ tháng này trả góp xe bằng lương cứng, tăng ca vào sổ riêng'),
        ('Vợ', 'Em nhận thêm 20 suất cơm văn phòng ở thị trấn'),
        ('me', 'Ra Tết anh đăng ký lớp bảo trì máy')]),
      say=("Tối đó hai vợ chồng chốt. Khoản trả góp xe chuyển sang trả bằng lương cứng, còn toàn bộ tiền tăng ca vào một sổ riêng, coi như không có. "
           "Vợ anh nhận thêm hai mươi suất cơm văn phòng ở thị trấn. Ra Tết, anh đăng ký một lớp bảo trì máy.")),
 dict(k='checklist', anh=TP, cap=('PHÉP THỬ CỦA ANH CHỊ', 'BAO NHIÊU % DỰA VÀO 1 NGÀNH?'), cols=CC, moc=True,
      items=[('Dưới 20%: khá an toàn', G_), ('Từ 20% đến 50%: có phương án dự phòng', V_), ('Trên 50%: quỹ dự phòng trước', R_)],
      say=("Phép thử cho anh chị. Cộng mọi khoản thu nhập nhà mình phụ thuộc vào cùng một ngành hay một nhóm khách hàng, rồi chia cho tổng thu nhập. "
           "Dưới hai mươi phần trăm, khá an toàn. Từ hai mươi đến năm mươi phần trăm, nên có phương án dự phòng. "
           "Trên năm mươi phần trăm, nên dựng quỹ dự phòng trước khi ngành đó chững lại. Đây là mốc em tự đặt để soi, không phải chuẩn chung.")),
 dict(k='checklist', ch='Chương 6 – Theo dõi gì tiếp theo?', anh=BX, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY ĐẾN TẾT'), cols=CC, moc=True,
      items=[('Xuất khẩu điện tử đầu mỗi tháng', V_), ('Xuất khẩu chip Hàn Quốc', V_), ('Kế hoạch chi tiền cho AI ở Mỹ', R_)],
      say=("Em gợi ý theo dõi ba điều. "
           "Một: số xuất khẩu điện tử công bố đầu mỗi tháng. "
           "Hai: xuất khẩu chip của Hàn Quốc, công bố ngay ngày đầu tháng. Em nghĩ đó là tín hiệu sớm đáng xem. "
           "Ba: kế hoạch chi tiền cho AI của các tập đoàn Mỹ trong các kỳ báo cáo tới. Số liệu vĩ mô hằng tháng, anh chị xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn của vợ', cap=('"ĐƠN NHIỀU THÌ CỨ LÀM', 'NHƯNG ĐỪNG TIÊU HẾT"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='23:05', mau=V_, msgs=[
        ('Vợ', 'Đơn nhiều thì cứ làm, nhưng đừng tiêu hết anh nhé'),
        ('Vợ', 'Hôm nào vắng khách mình vẫn có sổ'),
        ('me', 'Ừ, mai anh mở sổ')]),
      say=("Trước khi ngủ, vợ anh Tuấn nhắn: đơn nhiều thì cứ làm, nhưng đừng tiêu hết anh nhé. Hôm nào vắng khách, mình vẫn có sổ.")),
 dict(k='end', cap=('THU NHẬP NHÀ MÌNH', 'DỰA VÀO MỘT NGÀNH BAO NHIÊU %?'), cols=CC,
      say=("Còn anh chị thì sao: thu nhập nhà mình đang dựa vào một ngành bao nhiêu phần trăm, dưới hai mươi, hai mươi đến năm mươi, hay trên năm mươi? "
           "Ghi con số và kể cho em nghe ở phần bình luận nhé. Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=50)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Chứng Khoán Mỹ Bốc Hơi 2.500 Tỷ USD Vì AI: Tăng Ca Ra Sao?'
MT = ("Cổ phiếu công nghệ Mỹ (Nasdaq 100) bốc hơi khoảng 2.500 tỷ USD trong phiên 5/11 vì lo bong bóng AI – cùng lúc Việt Nam xuất khẩu 149,4 tỷ USD máy vi tính, điện tử, linh kiện trong 10 tháng, tăng 71%, gấp 3,2 lần năm 2023. "
      "Cú lật: hãng chip AI lớn nhất lãi kỷ lục 65 tỷ USD một quý, trong khi cổ phiếu đã giảm khoảng 1/3 từ đỉnh trước đó; nhóm điện tử Việt Nam xuất nhiều nhưng nhập còn nhiều hơn. Lần trước: năm 2023 xuất khẩu điện thoại giảm 9,7% sau cơn sốt thời Covid. "
      "Câu chuyện nhà anh Tuấn – tổ trưởng chuyền bo mạch ở Bắc Giang và quán cơm trước cổng khu công nghiệp.\n\n"
      "Nguồn số liệu:\n"
      "• Nhà Đầu Tư 12/11/2026: phiên 5/11 Nasdaq Composite −5,52%, chỉ số bán dẫn SOX giảm hơn 12%, Nasdaq 100 −6,4% xóa khoảng 2.500 tỷ USD vốn hóa. Nhà Đầu Tư 13/11/2026: cổ phiếu hãng chip AI lớn nhất giảm khoảng 1/3 so với đỉnh đầu tháng 10\n"
      "• Doanh Nhân Việt Nam 18/11/2026: hãng chip AI lớn nhất (Nvidia) quý III năm tài chính 2027 (kết thúc 25/10/2026) doanh thu 116 tỷ USD (+103%), lợi nhuận ròng 65 tỷ USD, cao nhất từ trước đến nay; dự báo quý IV khoảng 130 tỷ USD\n"
      "• WiData (số liệu hải quan): xuất khẩu máy vi tính, sản phẩm điện tử và linh kiện 10 tháng: 2023 46,5 tỷ USD; 2024 59,0 tỷ; 2025 87,4 tỷ; 2026 149,4 tỷ (tháng 10/2026: 25,7 tỷ); tổng xuất khẩu 10 tháng 2026 498,8 tỷ USD; xuất khẩu điện thoại và linh kiện 2022 58,0 tỷ, 2023 52,4 tỷ USD\n"
      "• Tạp chí Kinh tế – Tài chính / Trung tâm WTO VCCI 30/10/2026 (đến 15/10/2026): xuất khẩu nhóm điện tử 135,31 tỷ USD, nhập khẩu 201,12 tỷ USD, nhập siêu nhóm 65,81 tỷ USD; cán cân cả nước chuyển từ xuất siêu 17,55 tỷ sang nhập siêu 17,66 tỷ USD\n"
      "• VnEconomy 10/7/2026: Hiệp hội Doanh nghiệp điện tử Việt Nam dự báo xuất khẩu điện tử 2026 tăng 15–20% nhờ AI, trung tâm dữ liệu; tỷ lệ nội địa hóa thấp, giá trị giữ lại trong nước còn thấp\n"
      "• Thời báo Ngân hàng 1/11/2026: Hàn Quốc tháng 10 xuất khẩu +93,7%, bán dẫn +259,4%, máy tính +496,6% chủ yếu nhờ máy chủ AI\n"
      "• Em tự tính: 149,4 / 87,4 = +71%; 149,4 / 46,5 = 3,2 lần; 149,4 / 498,8 = 30%; phần tăng thêm (149,4 − 87,4) / (498,8 − 391,6) = 58%; điện thoại 52,4 / 58,0 − 1 = −9,7%. "
      "Nhà anh Tuấn (giả định): lương cứng 10 triệu + tăng ca 4 triệu, quán lãi 16 triệu (giả định 10 triệu từ khách là công nhân nhà máy điện tử): 14 / 30 ≈ 47%\n\n"
      "Số liệu vĩ mô hằng tháng: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật anh Tuấn, vợ anh Tuấn, anh Phong là hư cấu; số liệu là thật. Thu nhập nhà anh Tuấn là giả định để minh hoạ.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán cổ phiếu hay tư vấn đầu tư.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-12-02', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['bong bóng AI', 'trí tuệ nhân tạo', 'Nvidia', 'Nasdaq', 'xuất khẩu điện tử', 'khu công nghiệp', 'việc làm', 'xuất nhập khẩu', 'kinh tế Việt Nam', 'vĩ mô'],
    bia_hook=['TIỀN TĂNG CA', 'CÒN BAO LÂU?'], badge='CK MỸ MẤT 2.500 TỶ USD',
    bia_anh='Container ship||Ho Chi Minh City skyline night',
    bia_hook_b=['ĐIỆN TỬ', 'TĂNG 71%'], badge_b='XUẤT 149 TỶ USD NHỜ AI',
    bia_hook_c=['GẦN NỬA', 'THU NHẬP NHÀ'], badge_c='DỰA VÀO 1 NGÀNH',
    reel_hook='CHỨNG KHOÁN MỸ BỐC HƠI 2.500 TỶ USD|TIỀN TĂNG CA VIỆT NAM RA SAO???',
    fb_post=("Cổ phiếu công nghệ Mỹ mất 2.500 tỷ USD trong một phiên vì sợ bong bóng AI 💻 Còn Việt Nam vừa xuất 149 tỷ USD hàng điện tử trong 10 tháng, tăng 71%.\n\n👉 Hãng chip AI lớn nhất lãi kỷ lục 65 tỷ USD một quý – trước đó cổ phiếu đã giảm 1/3\n"
             "👉 Đến giữa tháng 10, nhóm điện tử xuất 135 tỷ nhưng nhập 201 tỷ USD\n👉 Lần trước 2023: xuất khẩu điện thoại giảm 9,7%, tăng ca bị cắt\n👉 Nhà anh chị dựa vào một ngành bao nhiêu %?\n\n"
             "🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: Mỹ mất 2.500 tỷ USD vì sợ AI, Việt Nam xuất 149 tỷ điện tử (NV1 22/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
CX = {'noti': ('tò mò', 'chuông thông báo'), 'chat': ('tâm sự', 'tiếng gõ phím'), 'call': ('trầm, lo', 'chuông gọi'), 'giay': ('căng', 'lật giấy'),
      'bignum': ('sốc', 'trống nhấn'), 'cards': ('suy nghĩ', 'nền phố'), 'bars': ('so sánh', 'nền phố'), 'checklist': ('quyết tâm', 'tick'), 'text': ('ngộ ra', 'nền nhẹ'), 'end': ('mở', 'nhạc kết')}
with open(LO + '/phan_canh.md', 'w', encoding='utf-8') as f:
    f.write('| # | loại | hình (thẻ form cũ) | cảm xúc | tiếng động |\n|---|---|---|---|---|\n')
    for i, c in enumerate(S, 1):
        cx = CX.get(c['k'], ('', '')); f.write('| %d | the/%s | %s | %s | %s |\n' % (i, c['k'], ' / '.join(c.get('cap', ('', ''))), cx[0], cx[1]))
if __name__ == '__main__':
    from collections import Counter
    cnt = Counter(c['k'] for c in S); dt = sum(cnt[k] for k in ('chat', 'noti', 'call', 'giay'))
    print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'dien thoai/giay %d/%d' % (dt, len(S)), 'tieu de', len(TIEU))
    for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
    for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
    sys.path.insert(0, CW + '/_video'); import kiem_loi, kiem_goi
    print('goi', kiem_goi.kiem(TIEU, META[KEY]['bia_hook']))
    for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
        if 'câu cụt' not in q: print(q)
    from xung_ho import le_phep
    for c in S:
        if le_phep(c['say']) != c['say']: print('XUNG_HO', c['say'][:80])
    for c in S:
        for x in c.get('cards', []):
            for y in x:
                if isinstance(y, str) and len(y) > 30: print('CARD DAI', y)
        for x in c.get('items', []):
            if len(x[0]) > 40: print('ITEM DAI', len(x[0]), x[0])
        for x in c.get('cap', ()):
            if len(x) > 30: print('CAP DAI', len(x), x)
