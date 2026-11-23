# -*- coding: utf-8 -*-
# NV1 23/11/2026 – VIDEO DÀI kênh chính, TẬP THỬ loạt "Vì sao…" theo bản đồ (claude/chi_dao/series_vi_sao_ban_do_2311.md): CẢNG CÁI MÉP.
# Hình: bản đồ vệ tinh bay zoom (ban_do.py 'map'), thước so sánh ('scale'), mặt cắt luồng ('section'), 3D dàn nhân vật (r3d: huy, hung, cuong, trang),
#       nến tuần GMD có chú thích (2 cảnh), thẻ điện thoại/giấy.
# Nguồn (đã đọc toàn văn 23/11/2026):
#  - Báo SGGP 9/2/2024: luồng Cái Mép – Thị Vải nạo vét xong, sâu 15,5 m (sâu nhất cả nước), tàu 160.000–200.000 DWT chạy không phụ thuộc thủy triều, vốn ngân sách hơn 1.414 tỷ.
#  - Hà Nội Mới 13/3/2025: OOCL Bauhinia 166.000 DWT, 16.828 TEU, dài 366,99 m, rộng 51 m cập Tân Cảng Cái Mép – Thị Vải.
#  - Gemadept 12/6/2024 (CPPI 2023 – World Bank/S&P): Cái Mép thứ 7 thế giới. SGGP 22/10/2025: CPPI 2024 giữ thứ 7, trên Singapore, Hồng Kông.
#  - bbw.vn 11/6/2026: CPPI 2025 (công bố 10/6/2026) Cái Mép 122 điểm, thứ 11, giảm 10 điểm, lùi 4 bậc; Hải Phòng 122 điểm, thứ 13, lần đầu vào top 20.
#  - SGGP/VPA 22/10/2025: 9 tháng 2025 tàu mẹ qua Cái Mép – Thị Vải 5,6 triệu TEU, +18%.
#  - Báo Xây dựng 11/1/2026 (Cảng vụ TP.HCM): năm 2025 container hơn 12,4 triệu TEU (+12,91%); cụm cảng gần hết công suất; tàu trễ lịch chờ cầu 3 giờ – 3 ngày;
#    chỉ Gemalink, TCIT có cầu riêng cho sà lan; 75–80% hàng gom/rút bằng đường thủy; hơn 40 tuyến quốc tế mỗi tuần.
#  - Người Quan Sát 1/11/2026: 22 tuyến đi Mỹ, 2 tuyến đi châu Âu, 10 tuyến nội Á; đường 991B ~9 km, 4 làn, gần 4.000 tỷ, dự kiến thông xe 12/2026.
#  - Số tự tính: 16.828 TEU x 6,1 m (1 TEU dài 20 feet) = khoảng 102 km; 15,5 m : 3,1 m/tầng = khoảng 5 tầng nhà. Landmark 81 cao 461 m (số công bố của chủ đầu tư).
#  - Giá GMD: dữ liệu giá ngày của web (đã điều chỉnh), gộp nến tuần.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw')
sys.path.insert(0, CW + '/_video'); from phat_am import doc as phat_am_doc
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = CW + '/_video/queue/20261123_2230'
KEY = 'CH0612CM'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
CANG = 'ov:container ship||container port aerial'
# 3D: vị trí đặt người + máy quay (theo lô 20261121_nong_vimo bản v2 đã dựng được)
CF_L = ([-28.25, 0.15, 5.2], [-27.15, 0.15, 5.2])
CAM_CF = {'from': [[-27.4, 1.5, 2.3], [-27.7, 0.8, 5.2], 42], 'to': [[-27.6, 1.42, 3.0], [-27.7, 0.8, 5.2], 38]}
CAM_VP = {'from': [[0.9, 1.5, 4.4], [0.3, 1.3, -1.0], 44], 'to': [[0.6, 1.45, 3.4], [0.2, 1.35, -1.2], 39]}
SOFA_T = [0.35, 0, -1.85]; SOFA_P = [1.65, 0, -1.85]
CAM_PK = {'from': [[1.0, 1.3, 2.6], [1.0, 0.9, -1.8], 38], 'to': [[1.0, 1.25, 2.0], [1.0, 0.9, -1.8], 33]}
CM = (10.535, 107.03)   # cụm cảng Cái Mép – Thị Vải
S = [
 # ---------------- MỞ ĐẦU: niềm tin ai cũng tin -> cú lật trong 15 giây ----------------
 dict(k='map', ch='Mở đầu', cap=('VÌ SAO TÀU MẸ', 'GHÉ THẲNG CÁI MÉP?'), cols=CC,
      map=dict(kf=[(12.5, 109.5, 5.0, 0.0), (11.0, 107.3, 7.8, 0.5), (10.5, 107.02, 12.4, 1.0)],
               nhan=[(1.29, 103.85, 'Singapore', 0.03), (22.3, 114.17, 'Hồng Kông', 0.06), (16.5, 112.0, 'QĐ. Hoàng Sa (Việt Nam)', 0.08, 'chu'),
                     (8.8, 114.5, 'QĐ. Trường Sa (Việt Nam)', 0.1, 'chu'), (CM[0], CM[1], 'Cụm cảng Cái Mép – Thị Vải', 0.75, 'cang')],
               duong=[([(1.29, 103.85), (4.5, 105.6), (8.5, 107.2), (10.38, 107.02)], R_, 0.05, 0.4, '')]),
      say=("Nhiều người vẫn nghĩ: tàu container cỡ lớn chạy thẳng sang Mỹ không bao giờ ghé Việt Nam, hàng của mình phải đi tàu nhỏ sang Singapore rồi mới lên tàu lớn. "
           "Nhưng có một cụm cảng nằm giữa rừng ngập mặn, cách trung tâm thành phố rất xa, hai kỳ liền đứng thứ 7 thế giới về hiệu quả, xếp trên cả Singapore. "
           "Năm ngoái, nó đón hơn 12 triệu đơn vị container. Vì sao lại là nơi này?")),
 dict(k='3d', set='cafevh', light='day', cam=CAM_CF, label='QUÁN NƯỚC GẦN CẢNG · 5 GIỜ SÁNG',
      cast=[{'a': 'hung', 'p': CF_L[1], 'act': 'dienthoai', 'ngoi': True, 'expr': 'worried'},
            {'a': 'cuong', 'p': CF_L[0], 'act': 'noi', 'ngoi': True, 'expr': 'grin'}],
      cap=('"CẢNG LỚN PHẢI Ở', 'THÀNH PHỐ LỚN CHỨ?"'), cols=CC,
      say=("Năm giờ sáng, ở quán nước gần cảng, Hùng Xa Lộ, tài xế container mười hai năm, vừa nhận tin nhắn: tàu đến trễ, xe anh phải chờ thêm. "
           "Cường Sociu ngồi cạnh cười: cảng lớn thì phải ở thành phố lớn chứ, ai lại xây giữa rừng đước thế này? "
           "Hùng không cãi. Anh chỉ biết mỗi đêm có những con tàu dài hơn ba sân bóng cập bến ở đây. Câu chuyện hôm nay đi tìm câu trả lời cho Cường.")),
 # ---------------- CHƯƠNG 1: vì sao không phải trong thành phố ----------------
 dict(k='map', ch='Chương 1 – Cảng lớn không nằm trong thành phố', cap=('SÔNG TRONG THÀNH PHỐ', 'KHÔNG ĐỦ SÂU CHO TÀU MẸ'), cols=CR,
      map=dict(kf=[(10.6, 106.88, 9.8, 0.0), (10.58, 106.9, 10.3, 1.0)],
               nhan=[(10.758, 106.79, 'Cảng trên sông Sài Gòn', 0.05),
                     (10.45, 106.84, 'Rừng ngập mặn Cần Giờ', 0.4, 'chu'), (CM[0], CM[1], 'Cái Mép – Thị Vải', 0.6, 'cang'), (10.346, 107.084, 'Vũng Tàu', 0.7)]),
      say=("Muốn hiểu, anh chị nhìn bản đồ. Cảng truyền thống của Sài Gòn nằm sâu trên sông, tàu phải đi một quãng dài, vòng vèo, luồng không đủ sâu cho những con tàu lớn nhất. "
           "Còn cách đó không xa, sông Thị Vải đổ thẳng ra vịnh Gành Rái, nước sâu, gần biển. "
           "Lợi thế ấy có từ tự nhiên. Nhưng tự nhiên chỉ cho một nửa câu trả lời.")),
 dict(k='cards', anh=CANG, cap=('NHIỀU NGƯỜI TỪNG NGHĨ', 'KHÔNG THỂ'), cols=CR, moc=True, cards=[
        ('Có sẵn đối thủ', 'Singapore, Hồng Kông', 'Đã là nơi chuyển tàu'),
        ('Hãng tàu kén', 'Chỉ ghé nơi đủ hàng', 'Tàu to, chạy vắng là lỗ'),
        ('Xây trước', 'Cảng có, tàu chưa về', 'Có thời gian vắng tàu')],
      say=("Hồi đầu, nhiều người cho rằng không thể. Singapore và Hồng Kông đã là nơi chuyển tàu của cả khu vực. "
           "Hãng tàu lớn chỉ ghé nơi có đủ hàng, vì một con tàu khổng lồ chạy vắng là lỗ. "
           "Và đã có một thời gian, các bến ở đây xây xong mà tàu chưa về nhiều. Vậy điều gì đã đổi?")),
 dict(k='section', cap=('LUỒNG CÁI MÉP – THỊ VẢI', 'SÂU 15,5 MÉT'), cols=CC,
      section=dict(sau=15.5, tang=3.1, nhan_sau='SÂU 15,5 M', nhan_nha='BẰNG KHOẢNG 5 TẦNG NHÀ', tau=[('Tàu mẹ 160.000 – 200.000 tấn (minh họa)', 14.0, 1.0, V_)],
                   ghi=['Không phụ thuộc thủy triều · Báo SGGP 9/2/2024']),
      say=("Nửa còn lại là con người làm. Đầu năm 2024, luồng Cái Mép – Thị Vải được nạo vét xong, sâu 15,5 mét, sâu nhất cả nước, bằng khoảng 5 tầng nhà chồng lên nhau. "
           "Tàu mẹ từ 160.000 đến 200.000 tấn ra vào an toàn, không phải chờ nước lên.")),
 dict(k='giay', cap=('HƠN 1.414 TỶ NGÂN SÁCH', 'ĐỂ ĐÀO SÂU MỘT CON SÔNG'), cols=CC, moc=True, giay=dict(tieu_de='LUỒNG CÁI MÉP – THỊ VẢI', so='Báo SGGP 9/2/2024', dau='ĐÃ XONG', dieu=[
        ('Độ sâu sau nạo vét', '15,5 MÉT'),
        ('Cỡ tàu chạy không chờ thủy triều', '160.000 – 200.000 TẤN'),
        ('Vốn ngân sách', 'HƠN 1.414 TỶ')]),
      say=("Số tiền bỏ ra là hơn 1.414 tỷ đồng vốn ngân sách, để đào sâu một con sông. Nghe thì lớn, nhưng anh chị sẽ thấy nó đổi lại được gì.")),
 # ---------------- CHƯƠNG 2: Việt Nam làm được thế nào ----------------
 dict(k='noti', ch='Chương 2 – Con tàu dài gần bằng Landmark 81', cap=('16.828 CONTAINER', 'TRÊN MỘT CON TÀU'), cols=CC, noti=dict(gio='06:15', ngay='Thứ Năm 13/3/2025', items=[
        ('Tin tức', 'Hàng hải · 13/3/2025', 'Tân Cảng Cái Mép – Thị Vải đón tàu OOCL Bauhinia 166.000 tấn, 16.828 TEU', V_),
        ('Zalo', 'Đội xe · 13/3/2025', 'Sáng nay tàu lớn vào, anh em xe đầu kéo trực sớm nhé', G_)]),
      say=("Ngày 13 tháng 3 năm ngoái, Hùng nhận tin đội xe gọi trực sớm. Cảng Tân Cảng Cái Mép – Thị Vải đón tàu OOCL Bauhinia, nặng 166.000 tấn, chở được 16.828 container loại 20 feet.")),
 dict(k='scale', cap=('DÀI 366,99 MÉT', 'GẦN BẰNG LANDMARK 81 NẰM NGANG'), cols=CC,
      scale=dict(don_vi='m', muc=[('Tàu OOCL Bauhinia', 367, 'tau', V_, 'dài 366,99 m'), ('Landmark 81', 461, 'thap', X_, 'cao 461 m'), ('3 sân bóng đá xếp nối', 315, 'thanh', G_, 'khoảng 105 m mỗi sân')]),
      say=("Con tàu dài gần 367 mét. Nếu dựng đứng, nó chỉ thấp hơn tòa Landmark 81 khoảng một trăm mét. "
           "Đặt nằm ngang, nó dài hơn ba sân bóng đá nối nhau.")),
 dict(k='bignum', anh=CANG, cap=('XẾP NỐI 16.828 CONTAINER', 'DÀI KHOẢNG 102 KM'), cols=CC, value=102, fmt='{:,.0f}', unit=' KM', top='16.828 TEU X 6,1 MÉT MỖI CONTAINER',
      sub='Em tự tính, 1 TEU dài 20 feet = 6,1 m', col=GOLD,
      say=("Còn số container trên tàu, nếu xếp nối đuôi nhau, dài khoảng 102 km, em tự tính theo chiều dài 6,1 mét mỗi container. "
           "Một chuyến tàu như thế, trước đây phải chia ra nhiều chuyến tàu nhỏ.")),
 dict(k='map', cap=('22 TUYẾN ĐI MỸ', '2 TUYẾN ĐI CHÂU ÂU'), cols=CC,
      map=dict(kf=[(28.0, 123.0, 3.35, 0.0), (28.0, 123.0, 3.2, 1.0)],
               nhan=[(CM[0], CM[1], 'Cái Mép', 0.02, 'cang'), (34.0, 241.8, 'Bờ Tây nước Mỹ', 0.35), (51.9, 4.1, 'Châu Âu', 0.6)],
               duong=[([(10.4, 107.05), (18.0, 130.0), (25.0, 160.0), (33.0, 200.0), (34.0, 241.8)], V_, 0.08, 0.45, '22 tuyến đi Mỹ'),
                      ([(10.4, 107.05), (1.2, 104.0), (6.0, 80.0), (12.5, 45.0), (30.0, 32.5), (36.0, 15.0), (36.0, -6.0), (44.0, -9.5), (51.9, 4.1)], X_, 0.4, 0.85, '')],
               dim=0.2),
      say=("Đến cuối năm nay, theo báo Người Quan Sát, từ Cái Mép có 22 tuyến tàu đi Mỹ, 2 tuyến đi châu Âu và 10 tuyến nội Á. "
           "Với các tuyến này, hàng của mình lên tàu lớn ngay tại cửa nhà, không phải vòng sang cảng nước khác để chuyển tàu.")),
 dict(k='3d', set='vanphong', light='day', cam=CAM_VP, label='VÌ SAO ĐI THẲNG LẠI QUAN TRỌNG?',
      cast=[{'a': 'huy', 'p': [-0.7, 0, 0.5], 'act': 'chitay', 'side': -1, 'expr': 'smile'},
            {'a': 'trang', 'p': [0.9, 0, 0.7], 'act': 'noi', 'side': -1, 'expr': 'worried'}],
      cap=('BỚT MỘT LẦN CHUYỂN TÀU', 'LÀ BỚT CHỜ, BỚT PHÍ'), cols=CC,
      say=("Trang Trâu hỏi em: đi thẳng hay chuyển tàu thì khác gì nhau, miễn hàng tới nơi là được? "
           "Em trả lời: mỗi lần chuyển tàu ở cảng khác là thêm một lần bốc xếp, thêm ngày chờ, thêm phí, và thêm rủi ro lỡ chuyến. "
           "Với lô cà phê, đồ gỗ hay quần áo đi Mỹ, vài ngày chậm có khi là mất đơn hàng sau.")),
 dict(k='bignum', anh=CANG, cap=('NĂM NGOÁI: HƠN 12,4 TRIỆU TEU', 'TĂNG 12,91%'), cols=CC, value=12.4, fmt='{:,.1f}', unit=' TRIỆU TEU', top='CONTAINER QUA CÁI MÉP – THỊ VẢI NĂM 2025',
      sub='Cảng vụ TP.HCM – Báo Xây dựng 11/1/2026', col=GOLD,
      say=("Kết quả nằm trong con số. Theo Cảng vụ Hàng hải Thành phố Hồ Chí Minh, năm ngoái cụm cảng Cái Mép – Thị Vải đón hơn 12,4 triệu TEU container, tăng gần 13 phần trăm.")),
 dict(k='noti', cap=('THỨ 7 THẾ GIỚI', 'TRÊN CẢ SINGAPORE'), cols=CC, noti=dict(gio='08:30', ngay='Bảng xếp hạng CPPI', items=[
        ('Tin tức', 'Gemadept · 12/6/2024', 'World Bank: Cái Mép thứ 7 trong các cảng container hiệu quả nhất thế giới (CPPI 2023)', V_),
        ('Tin tức', 'SGGP · 22/10/2025', 'CPPI 2024: Cái Mép giữ vị trí thứ 7, trên Singapore, Hồng Kông', G_)]),
      say=("Ngân hàng Thế giới có một chỉ số đo hiệu quả cảng container. Hai kỳ liền, chỉ số này xếp Cái Mép thứ 7 thế giới. Cái Mép đứng trên cả Singapore và Hồng Kông, hai nơi mà trước đây hàng Việt phải đi nhờ.")),
 # ---------------- CHƯƠNG 3: cú lật ----------------
 dict(k='noti', ch='Chương 3 – Từ hạng 7 xuống hạng 11', cap=('TỪ HẠNG 7', 'XUỐNG HẠNG 11'), cols=CR, noti=dict(gio='21:40', ngay='Thứ Năm 11/6/2026', items=[
        ('Tin tức', 'bbw.vn · 11/6/2026', 'CPPI mới: Cái Mép 122 điểm, xếp thứ 11, giảm 10 điểm, lùi 4 bậc', R_),
        ('Tin tức', 'bbw.vn · 11/6/2026', 'Hải Phòng lần đầu vào top 20, xếp thứ 13', G_)]),
      say=("Nhưng câu chuyện không dừng ở đó. Tháng 6 năm nay, bảng xếp hạng mới được công bố. Cái Mép giảm 10 điểm, lùi 4 bậc, xuống thứ 11. "
           "Cùng lúc, Hải Phòng tăng từ 87 lên 122 điểm, lần đầu vào top 20, xếp thứ 13.")),
 dict(k='map', cap=('CÁI MÉP LÙI 4 BẬC', 'HẢI PHÒNG VÀO TOP 20'), cols=CC,
      map=dict(kf=[(15.3, 107.6, 5.9, 0.0), (15.3, 107.6, 6.1, 1.0)],
               nhan=[(CM[0], CM[1], 'Cái Mép: thứ 7 xuống thứ 11', 0.05, 'cang'), (20.84, 106.69, 'Hải Phòng: thứ 13', 0.3, 'cang'),
                     (16.5, 112.0, 'QĐ. Hoàng Sa (Việt Nam)', 0.05, 'chu'), (8.6, 114.5, 'QĐ. Trường Sa (Việt Nam)', 0.05, 'chu')], dim=0.15),
      say=("Hai cảng biển lớn nhất hai đầu đất nước cùng nằm trong nhóm tốt nhất thế giới là tin vui. Nhưng vì sao Cái Mép tụt hạng, khi lượng hàng vẫn tăng?")),
 dict(k='bignum', anh=CANG, cap=('RIÊNG TÀU MẸ 9 THÁNG 2025', 'TĂNG 18%'), cols=CC, value=5.6, fmt='{:,.1f}', unit=' TRIỆU TEU', top='HÀNG QUA TÀU MẸ Ở CÁI MÉP – THỊ VẢI',
      sub='9 tháng 2025, +18% – Báo SGGP 22/10/2025', col=GOLD,
      say=("Hàng thì vẫn đổ về. Chỉ riêng hàng đi tàu mẹ, chín tháng năm ngoái đạt 5,6 triệu TEU, tăng 18 phần trăm. "
           "Hàng tăng nhanh như thế, còn cầu bến thì không thể xây kịp trong một năm.")),
 dict(k='giay', cap=('GẦN NHƯ HẾT CÔNG SUẤT', 'TÀU CHỜ CẦU TỚI 3 NGÀY'), cols=CR, moc=True, giay=dict(tieu_de='BÀI TOÁN CÔNG SUẤT CÁI MÉP – THỊ VẢI', so='Báo Xây dựng 11/1/2026', dau='ĐIỂM NGHẼN', dieu=[
        ('Các cảng lớn gần đạt công suất thiết kế', 'GẦN HẾT CHỖ'),
        ('Tàu trễ lịch phải chờ cầu bến', '3 GIỜ – 3 NGÀY'),
        ('Hàng gom, rút bằng đường thủy', '75 – 80%'),
        ('Cảng có cầu riêng cho sà lan', 'CHỈ 2 CẢNG')]),
      say=("Em nghĩ câu trả lời nằm ở chữ đông. Theo báo Xây dựng, cụm cảng gần như hết công suất. Tàu đến trễ lịch phải chờ cầu bến từ 3 giờ đến 3 ngày. "
           "Phần lớn hàng được gom về bằng sà lan, nhưng chỉ hai cảng có cầu riêng cho sà lan.")),
 dict(k='3d', set='phongkhach', light='day', cam=CAM_PK, label='TỐI ĐÓ · NHÀ HÙNG XA LỘ',
      cast=[{'a': 'hung', 'p': SOFA_T, 'act': 'noi', 'ngoi': True, 'expr': 'worried'},
            {'a': 'cuong', 'p': SOFA_P, 'act': 'dienthoai', 'ngoi': True, 'expr': 'stern'}],
      cap=('"XE CHỜ CẢ NGÀY', 'THÌ AI TRẢ TIỀN?"'), cols=CR,
      say=("Tối đó Cường ghé nhà Hùng. Hùng kể: hôm nào tàu trễ, xe anh nằm chờ ở cảng cả ngày, mà tiền chuyến thì vẫn thế. "
           "Cường hỏi lại: vậy cảng đông như thế, sao không làm thêm đường cho xe chạy? Hùng chỉ ra cửa sổ: đang làm đấy, nhưng chưa xong. Cái giá của một cảng quá đông không nằm trên bảng xếp hạng. Nó nằm trong tiền dầu xe chạy không, trong ngày công tài xế ngồi chờ, và trong lô hàng của chủ xưởng lỡ chuyến tàu tuần này.")),
 dict(k='map', cap=('ĐƯỜNG 991B: 9 KM, GẦN 4.000 TỶ', 'DỰ KIẾN THÔNG XE THÁNG 12/2026'), cols=CC,
      map=dict(kf=[(10.57, 107.07, 10.6, 0.0), (10.56, 107.06, 11.2, 1.0)],
               nhan=[(CM[0], CM[1], 'Cụm cảng Cái Mép – Thị Vải', 0.05, 'cang'), (10.6, 107.12, 'Hướng Quốc lộ 51', 0.3), (10.43, 107.0, 'Luồng ra biển', 0.45, 'chu')]),
      say=("Theo báo Người Quan Sát, đường 991B nối cụm cảng ra Quốc lộ 51 dài khoảng 9 km, 4 làn xe, vốn gần 4.000 tỷ đồng. Đường dự kiến thông xe toàn tuyến trong tháng 12 này. "
           "Nhưng đường này vẫn cách cao tốc Biên Hòa – Vũng Tàu hơn 8 km.")),
 dict(k='cards', anh=CANG, cap=('ĐIỀU GÌ TẠO NÊN', 'SỰ KHÁC BIỆT?'), cols=CC, moc=True, cards=[
        ('Nước sâu', 'Tự nhiên cho sẵn', 'Sông Thị Vải gần biển'),
        ('Đào luồng', 'Nhà nước bỏ 1.414 tỷ', 'Sâu 15,5 mét'),
        ('Doanh nghiệp', 'Xây cảng, mở tuyến', '22 tuyến đi Mỹ')],
      say=("Vậy điều gì tạo nên sự khác biệt? Em nghĩ có ba lớp. Lớp một là nước sâu, tự nhiên cho sẵn. Lớp hai là đào luồng, nhà nước bỏ tiền. "
           "Lớp ba là doanh nghiệp dám xây cảng giữa rừng đước và kéo các hãng tàu lớn về. Thiếu lớp nào, tàu mẹ cũng không ghé. Và muốn giữ hạng, cả ba lớp phải chạy cùng tốc độ với lượng hàng.")),
 # ---------------- CHƯƠNG 4: nối doanh nghiệp, nến có chú thích ----------------
 dict(k='hook', ch='Chương 4 – Doanh nghiệp sống nhờ câu chuyện cảng', cap=('GIÁ CỔ PHIẾU GMD', 'PHẢN ỨNG VỚI TIN CẢNG'), cols=CC, label='GMD – Gemadept (cảng Gemalink), giá điều chỉnh',
      chart=dict(sym='GMDW', weeks=108, mas=[(20, (255, 196, 0))], circles=[[19, 38.62, '13/3/2025: đón tàu 16.828 TEU', 2.0], [23, 26.46, '4/2025: Mỹ công bố thuế đối ứng', 4.5], [83, 50.67, '6/2026: CPPI tụt hạng 11', 7.0]]),
      say=("Một doanh nghiệp sống nhờ câu chuyện này là Gemadept, mã GMD, doanh nghiệp đứng sau cảng Gemalink ở Cái Mép. Biểu đồ nến tuần hai năm qua, giá đã điều chỉnh. "
           "Tuần đón tàu 16.828 container, giá không tăng. Đầu tháng 4 năm ngoái, khi Mỹ công bố thuế đối ứng, giá giảm mạnh cùng cả thị trường, vì hàng đi Mỹ càng nhiều thì thuế Mỹ càng là rủi ro. "
           "Tháng 6 năm nay, tin tụt hạng không làm giá đổi chiều.")),
 dict(k='hook', cap=('TIN TỐT CHƯA CHẮC LÊN GIÁ', 'TIN XẤU CHƯA CHẮC XUỐNG'), cols=CC, label='GMD – 26 tuần gần nhất, giá điều chỉnh',
      chart=dict(sym='GMDW', weeks=26, mas=[(10, (56, 189, 248))], hlines=[[51.9, 'Tuần 23/11/2026: 51,9', (255, 196, 0), 1.5]], circles=[[23, 55.0, 'Tuần 9/11: 55,0', 3.0]]),
      say=("Hai mươi sáu tuần gần nhất, giá dao động trong vùng 45 đến 58 nghìn đồng. Bài học em rút ra: giá cổ phiếu phản ứng với cả thế giới, không chỉ với tin cảng. "
           "Em không nói nên mua hay bán, chỉ muốn anh chị thấy: câu chuyện hay và giá cổ phiếu là hai việc khác nhau.")),
 dict(k='checklist', cap=('3 ĐIỀU NÊN THEO DÕI', 'Ở CÁI MÉP NĂM 2027'), cols=CC, moc=True, items=[
        ('Đường 991B có thông xe đúng tháng 12?', V_),
        ('Cảng nào mở thêm cầu bến cho sà lan?', V_),
        ('Số tuyến đi Mỹ có còn tăng?', R_)],
      say=("Nếu anh chị muốn tự theo dõi câu chuyện này, em gợi ý ba điều. Một, đường 991B có thông xe đúng hẹn không. "
           "Hai, cảng nào mở thêm cầu bến, nhất là cầu cho sà lan. Ba, số tuyến đi Mỹ có còn tăng khi thuế quan thay đổi. "
           "Bảng giá và báo cáo tài chính các doanh nghiệp cảng em để miễn phí trên web chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='3d', ch='Kết', set='cafevh', light='day', cam=CAM_CF, label='SÁNG HÔM SAU · QUÁN NƯỚC GẦN CẢNG',
      cast=[{'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'},
            {'a': 'cuong', 'p': CF_L[0], 'act': 'dienthoai', 'ngoi': True, 'expr': 'relief'}],
      cap=('"HÓA RA KHÔNG PHẢI', 'CỨ THÀNH PHỐ LỚN"'), cols=CC,
      say=("Sáng hôm sau, Cường đọc lại bảng xếp hạng rồi nói: hóa ra cảng lớn không cần nằm trong thành phố lớn, mà cần nước sâu, cần người dám đào, và cần đường cho xe chạy. "
           "Hùng cười: còn đường thì để anh chờ thêm một tháng nữa. Em nghĩ câu chuyện Cái Mép giống một bài học đầu tư: lợi thế tự nhiên chỉ là điểm xuất phát, thứ giữ được vị trí là đầu tư đều đặn và đúng chỗ nghẽn.")),
 dict(k='end', cap=('CÁI MÉP SẼ LẤY LẠI', 'HẠNG 7 HAY KHÔNG?'), cols=CC,
      say=("Còn anh chị, anh chị nghĩ sau khi đường 991B thông xe, Cái Mép có lấy lại được hạng 7 thế giới không, hay Hải Phòng sẽ vượt lên? "
           "Kể cho em nghe ở phần bình luận nhé. Tập sau, em kể tiếp vì sao một vùng đất khác của Việt Nam thay đổi cả nền kinh tế.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(phat_am_doc(c['say']))
TIEU = 'Vì Sao Cảng Thứ 7 Thế Giới Lại Nằm Giữa Rừng Đước?'
MT = ("Vì sao cụm cảng Cái Mép – Thị Vải, nằm giữa rừng ngập mặn, đón được tàu mẹ 166.000 tấn đi thẳng Mỹ, châu Âu và hai kỳ liền đứng thứ 7 thế giới về hiệu quả? "
      "Và vì sao năm nay tụt xuống thứ 11? Kể bằng bản đồ vệ tinh, số liệu thật và câu chuyện tài xế container Hùng Xa Lộ.\n\n"
      "Nguồn số liệu:\n"
      "• Luồng Cái Mép – Thị Vải sâu 15,5 m, tàu 160.000–200.000 tấn không phụ thuộc thủy triều, vốn ngân sách hơn 1.414 tỷ – Báo SGGP 9/2/2024\n"
      "• Tàu OOCL Bauhinia 166.000 tấn, 16.828 TEU, dài 366,99 m cập Tân Cảng Cái Mép – Thị Vải 13/3/2025 – Báo Hà Nội Mới\n"
      "• CPPI 2023 thứ 7 – Gemadept 12/6/2024; CPPI 2024 giữ thứ 7 – SGGP 22/10/2025; CPPI 2025: thứ 11 (122 điểm, −10), Hải Phòng thứ 13 – bbw.vn 11/6/2026\n"
      "• Năm 2025: hơn 12,4 triệu TEU (+12,91%); gần hết công suất; tàu chờ cầu 3 giờ – 3 ngày; 75–80% hàng gom bằng đường thủy – Báo Xây dựng 11/1/2026 (Cảng vụ TP.HCM)\n"
      "• 22 tuyến đi Mỹ, 2 tuyến châu Âu, 10 tuyến nội Á; đường 991B ~9 km, gần 4.000 tỷ, dự kiến thông xe 12/2026 – Người Quan Sát 1/11/2026\n"
      "• Số tự tính: 16.828 TEU × 6,1 m ≈ 102 km; 15,5 m ÷ 3,1 m/tầng ≈ 5 tầng nhà\n"
      "• Giá GMD: nến tuần, giá điều chỉnh – dữ liệu chungkhoanhuynguyen.com\n"
      "• Ảnh vệ tinh: Sentinel-2 cloudless – s2maps.eu by EOX IT Services GmbH (CC BY 4.0, dữ liệu Copernicus Sentinel 2016)\n\n"
      "Bảng giá, báo cáo tài chính doanh nghiệp cảng biển: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật Hùng Xa Lộ, Cường Sociu, Trang Trâu là hư cấu; số liệu là thật.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Vì sao… (bản đồ)', ngay='2026-12-06', gio_goi_y='12:00', gio='12:00', nhac='lofi', can_duyet='anh Huy duyệt trước khi hẹn',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['Cái Mép', 'cảng Cái Mép Thị Vải', 'cảng biển Việt Nam', 'tàu mẹ', 'logistics', 'CPPI', 'Gemalink', 'GMD', 'kinh tế Việt Nam', 'vì sao'],
    bia_hook=['TÀU 367 MÉT', 'VÀO TẬN RỪNG ĐƯỚC'], badge='TÀU 16.828 CONTAINER',
    bia_anh='ov:container ship||container port aerial',
    bia_hook_b=['TỪ HẠNG 7', 'XUỐNG HẠNG 11?'], badge_b='CẢNG CÁI MÉP',
    bia_hook_c=['22 TUYẾN', 'ĐI MỸ TỪ ĐÂY'], badge_c='CẢNG CÁI MÉP',
    reel_hook='CẢNG GIỮA RỪNG ĐƯỚC|XẾP TRÊN CẢ SINGAPORE???',
    fb_post=("Vì sao một cụm cảng giữa rừng đước lại đón tàu 16.828 container và từng xếp thứ 7 thế giới, trên cả Singapore? 🚢\n\n"
             "👉 Luồng sâu 15,5 m – bằng 5 tầng nhà\n👉 22 tuyến tàu đi Mỹ\n👉 Nhưng năm nay tụt xuống thứ 11: tàu chờ cầu tới 3 ngày\n\n"
             "Đường 991B thông xe tháng 12 – Cái Mép có lấy lại hạng 7?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – loạt 'Vì sao…' theo bản đồ, tập thử: CẢNG CÁI MÉP (NV1 23/11/2026). Có cảnh map/scale/section (ban_do.py) + 3D (r3d).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'GMDW': lib.weekly('GMD', 108)}, open(LO + '/px_tuan.json', 'w'), ensure_ascii=False)
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
