# -*- coding: utf-8 -*-
# NV1 28/11/2026 – VIDEO DÀI kênh chính, đề 5 lo_video_dai_tui_tien_2711 "Việt Nam có thành Nhật Bản thứ hai?" theo hướng "già trước khi giàu" – chạm túi tiền: ai nuôi mình lúc già.
# Lý do chọn: xu_huong tuần tới 27/11: "IS VIETNAM AT RISK OF AGING LIKE JAPAN?" 61 nghìn; "VN vượt nửa châu Á" 174 nghìn; "GDP quý 4 vượt Thái Lan" 275 nghìn;
#   kênh mình "VN có thành Thái Lan thứ hai?" +76 (top 2 tuần). Không trùng 7 ngày (chưa có video dân số/lương hưu).
# Nguồn (đã mở 28/11/2026):
#  - Tuổi Trẻ 27/1/2026: VN bước vào thời kỳ dân số già từ 2034 (người 65+ đạt 14%); "siêu già" từ 2050; kết thúc dân số vàng khoảng 2036, sớm hơn 3 năm so với dự báo 2019;
#    2024 có khoảng 14,2 triệu người 60+; 20,9 triệu năm 2034; người trong tuổi lao động đạt đỉnh 2038, khoảng 69,5 triệu.
#  - VietNamNet 14/7/2026: GS Nguyễn Đình Cử – VN đã tận dụng được 20 năm dân số vàng, còn khoảng 10 năm; 2024 cứ 100 trẻ em có khoảng 60 người cao tuổi.
#  - VietNamNet 27/3/2025 (Bộ trưởng Y tế): mức sinh 2024 còn 1,91 con/phụ nữ; thu nhập bình quân đầu người khoảng 4.700 USD năm 2024.
#  - Việt Báo 6/11/2026 (theo VnExpress): mức sinh thay thế 2,1 con.
#  - VnExpress International 23/12/2024 (bài bình luận): Nhật thành xã hội già năm 1994, GDP bình quân đầu người khi đó 40.000 USD; Nhật mất 24 năm từ già hoá sang già, Việt Nam dự kiến 21 năm.
#  - VnEconomy 9/7/2024: 16,1 triệu người cao tuổi; 2,7 triệu người cao tuổi hưởng lương hưu và trợ cấp bảo hiểm xã hội hằng tháng; khoảng 65% chưa được hưởng trợ giúp xã hội.
#  - VnEconomy 10/2/2025: lương hưu bình quân 6,2 triệu đồng/tháng (thống kê đến 12/2024).
#  - VnExpress 16/1/2025: khoảng 50% người trên 60 tuổi vẫn làm việc (khảo sát quốc gia 2022, GS Giang Thanh Long); chi tiền túi khoảng 40% chi phí khám chữa bệnh (WHO).
#  - VietnamPlus 25/6/2026: trợ cấp hưu trí xã hội từ đủ 75 tuổi (thông thường), 70 đến dưới 75 với hộ nghèo, cận nghèo; dự thảo đề xuất giảm dần xuống 70; khoảng 2,5 triệu người nhận.
# Số tự tính: 2,7 ÷ 16,1 = 16,8% (khoảng 1 trong 6); 40.000 ÷ 4.700 = 8,5 lần; 2034 − 2026 = 8 năm;
#   ví dụ giả định Cường 35 tuổi: muốn tự có 6,2 triệu/tháng từ 60 đến 80 tuổi = 6,2 × 12 × 20 = 1.488 triệu (gần 1,5 tỷ, CHƯA tính lãi và trượt giá);
#   để dành từ 35 đến 60 tuổi = 300 tháng → 1.488 ÷ 300 = 4,96 triệu/tháng (gần 5 triệu). Nếu bắt đầu từ 45 tuổi: 180 tháng → 8,27 triệu/tháng.
# Lưu ý: số Nhật là GDP bình quân đầu người (VnExpress), số VN là thu nhập bình quân đầu người (VietNamNet) – nói "khoảng", ghi rõ trong mô tả. Không trộn 14,2 triệu (60+, Tuổi Trẻ) với 16,1 triệu (VnEconomy).
# Cường, Hùng (dàn cố định), bà Tư (mẹ Cường), ông Bảy (bố Hùng) là nhân vật hư cấu. Không hô mua bán, không dự đoán.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw')
sys.path.insert(0, CW + '/_video'); from phat_am import doc as phat_am_doc
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = CW + '/_video/queue/20261128_0200'
KEY = 'CH0212GG'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HCM = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline'
HN = 'ov:Hanoi skyline night||Hanoi skyline'
TAU = 'ov:Container ship||Ho Chi Minh City skyline'
CF_L = ([-28.25, 0.15, 5.2], [-27.15, 0.15, 5.2])
CAM_CF = {'from': [[-27.4, 1.5, 2.3], [-27.7, 0.8, 5.2], 42], 'to': [[-27.6, 1.42, 3.0], [-27.7, 0.8, 5.2], 38]}
CAM_VP = {'from': [[0.9, 1.5, 4.4], [0.3, 1.3, -1.0], 44], 'to': [[0.6, 1.45, 3.4], [0.2, 1.35, -1.2], 39]}

S = [
 dict(k='noti', ch='Mở đầu', cap=('6 NGƯỜI GIÀ', '1 CÓ LƯƠNG HƯU, TRỢ CẤP???'), cols=CR, noti=dict(gio='06:20', ngay='Thứ Bảy 28/11', items=[
        ('Tin tức', 'Tuổi Trẻ · 27/1/2026', 'Dự báo: Việt Nam bước vào thời kỳ dân số già từ năm 2034', R_),
        ('Zalo', 'Mẹ', 'Con ơi, chân mẹ đau, mai mẹ nghỉ chợ', V_)]),
      say=("Anh chị đã bao giờ tự hỏi: năm sáu mươi tuổi, tiền chợ mỗi tháng ai trả cho mình? "
           "Ở nước mình, cứ sáu người cao tuổi thì chỉ khoảng một người có lương hưu hoặc trợ cấp bảo hiểm xã hội hằng tháng. "
           "Và theo dự báo, chỉ khoảng tám năm nữa, Việt Nam đã thành một nước dân số già.")),
 dict(k='bignum', short=True, anh=HCM, cap=('NHẬT LÚC GIÀ: 40.000 ĐÔ', 'VIỆT NAM HÔM NAY: 4.700 ĐÔ'), cols=CR,
      value=8.5, fmt='{:,.1f}', unit=' LẦN', top='NHẬT 1994: GDP/NGƯỜI · VIỆT NAM 2024: THU NHẬP/NGƯỜI · ĐÔ DANH NGHĨA · EM TỰ TÍNH', sub='VnExpress 23/12/2024 · VietNamNet 27/3/2025', col=R_,
      say=("Năm một nghìn chín trăm chín mươi tư, khi Nhật Bản thành xã hội già, mỗi người Nhật làm ra khoảng bốn mươi nghìn đô một năm. "
           "Còn mỗi người Việt năm hai nghìn không trăm hai mươi tư mới khoảng bốn nghìn bảy trăm đô một năm. Hai con số đo hơi khác nhau, nhưng Nhật lúc già vẫn hơn ta hôm nay hơn tám lần. "
           "Người ta gọi đó là già trước khi giàu.")),
 dict(k='3d', set='cafevh', light='day', cam=CAM_CF, label='SÁNG THỨ BẢY · QUÁN NƯỚC',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'dienthoai', 'ngoi': True, 'expr': 'worried'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'}],
      cap=('"MẸ TÔI 63 TUỔI', 'VẪN PHẢI ĐI CHỢ BÁN RAU"'), cols=CC,
      say=("Em, Huy Nguyễn, kể chuyện anh Cường ba mươi lăm tuổi và anh Hùng, hai nhân vật hư cấu, số liệu là thật. "
           "Mẹ Cường, bà Tư, sáu mươi ba tuổi, bán rau ở chợ ba mươi năm, không có lương hưu. Sáng nay bà nhắn chân đau, mai nghỉ chợ. "
           "Bố Hùng, ông Bảy, về hưu từ nhà máy, tháng nào cũng có lương hưu. Cùng một lứa tuổi, hai tuổi già rất khác nhau.")),
 dict(k='checklist', anh=HN, cap=('BA CÂU HỎI', 'CỦA VIDEO NÀY'), cols=CC, moc=True,
      items=[('1. Ta già nhanh cỡ nào?', V_), ('2. Người già có lương hưu?', R_), ('3. Nhà mình để dành bao nhiêu?', V_)],
      say=("Ta đi qua ba câu hỏi. Việt Nam già nhanh cỡ nào? Bao nhiêu người già đang có lương hưu? Và nhà mình cần để dành bao nhiêu?")),
 # ---- Chương 1
 dict(k='giay', ch='Chương 1 – Ta già nhanh cỡ nào', cap=('2034: DÂN SỐ GIÀ', '2036: HẾT DÂN SỐ VÀNG'), cols=CR, moc=True, giay=dict(
        tieu_de='NHỮNG MỐC CỦA VIỆT NAM', so='Tuổi Trẻ 27/1/2026 · dự báo dân số', dau='DỰ BÁO', dieu=[
        ('Người từ 60 tuổi, năm 2024', '14,2 TRIỆU'),
        ('Người từ 60 tuổi, năm 2034', '20,9 TRIỆU'),
        ('Dân số già', 'NĂM 2034'),
        ('Hết thời kỳ dân số vàng', 'KHOẢNG 2036')]),
      say=("Câu thứ nhất, ta già nhanh cỡ nào. Theo dự báo được báo Tuổi Trẻ đăng đầu năm nay, năm hai nghìn không trăm hai mươi tư nước ta có khoảng mười bốn triệu hai trăm nghìn người từ sáu mươi tuổi trở lên. Mười năm sau, gần hai mươi mốt triệu. "
           "Đến năm hai nghìn không trăm ba mươi tư, cứ khoảng bảy người dân thì có một người đã ngoài sáu mươi lăm. Thế giới gọi đó là nước dân số già.")),
 dict(k='cards', anh=HCM, cap=('DÂN SỐ VÀNG LÀ GÌ?', 'CÒN KHOẢNG 10 NĂM'), cols=CC, moc=True,
      cards=[('2 NGƯỜI', 'Đang tuổi đi làm', 'Mới có 1 người phụ thuộc'), ('2007', 'Bắt đầu dân số vàng', 'Đã dùng gần 20 năm'), ('10 NĂM', 'Còn lại', 'Theo GS Nguyễn Đình Cử')],
      say=("Dân số vàng là lúc cứ ít nhất hai người đang tuổi đi làm mới có một người già hoặc trẻ nhỏ phải nuôi. Đó là quãng thuận lợi để một nước tăng trưởng. "
           "Việt Nam vào quãng ấy từ năm hai nghìn không trăm lẻ bảy. Theo giáo sư Nguyễn Đình Cử, ta đã dùng gần hai mươi năm và chỉ còn khoảng mười năm.")),
 dict(k='bignum', short=True, anh=HN, cap=('MỖI PHỤ NỮ', 'CÒN 1,91 CON'), cols=CR,
      value=1.91, fmt='{:,.2f}', unit=' CON', top='MỨC SINH NĂM 2024 · VIETNAMNET 27/3/2025', sub='Mức để dân số không giảm: 2,1 con (VnExpress)', col=R_,
      say=("Một lý do ta già nhanh: sinh ít đi. Năm hai nghìn không trăm hai mươi tư, mỗi phụ nữ trung bình chỉ còn gần hai con, thấp hơn mức hai phẩy một con, là mức để dân số không giảm. "
           "Ít con thì sau này ít người đi làm nuôi người già. Theo báo VietNamNet, năm hai nghìn không trăm hai mươi tư, cứ một trăm trẻ em đã có khoảng sáu mươi người cao tuổi. Tức là cứ năm đứa trẻ đã có ba người cao tuổi.")),
 dict(k='chat', cap=('"NHÀ TÔI 1 ĐỨA', 'SAU NÀY NÓ NUÔI 2 NGƯỜI?"'), cols=CC, moc=True, chat=dict(ten='Hùng', tv='Đang hoạt động', gio='19:15', mau=V_, msgs=[
        ('me', 'Nhà tôi chỉ một đứa con'),
        ('me', 'Sau này nó nuôi cả hai vợ chồng tôi à?'),
        ('Hùng', 'Nó còn nhà nó, con nó nữa ông ạ'),
        ('Hùng', 'Tự lo được phần nào thì lo trước đi')]),
      say=("Tối đó Cường nhắn Hùng: nhà Cường chỉ có một đứa con, sau này nó nuôi cả hai vợ chồng sao? "
           "Hùng đáp: nó còn nhà nó, con nó nữa. Tự lo được phần nào thì lo trước đi.")),
 # ---- Chương 2
 dict(k='giay', ch='Chương 2 – Bao nhiêu người già có lương hưu', short=True, cap=('6 NGƯỜI GIÀ', 'CHỈ 1 CÓ LƯƠNG HƯU, TRỢ CẤP'), cols=CR, moc=True, giay=dict(
        tieu_de='NGƯỜI CAO TUỔI VÀ LƯƠNG HƯU', so='VnEconomy 9/7/2024 · em tự tính', dau='KHOẢNG 1 TRONG 6', dieu=[
        ('Lương hưu, trợ cấp BHXH hằng tháng', '2,7 TRIỆU NGƯỜI'),
        ('Tỷ lệ trong người cao tuổi', 'KHOẢNG 17%'),
        ('Chưa có trợ giúp xã hội', 'KHOẢNG 65%'),
        ('Bà Tư', 'KHÔNG CÓ KHOẢN NÀO')]),
      say=("Câu thứ hai, bao nhiêu người già có lương hưu. Theo báo VnEconomy giữa năm hai nghìn không trăm hai mươi tư, chỉ hai triệu bảy trăm nghìn người cao tuổi có lương hưu hoặc trợ cấp bảo hiểm xã hội hằng tháng, khoảng mười bảy phần trăm. "
           "Cứ sáu người già, chỉ khoảng một người có khoản tiền đều đặn ấy. Cùng bài báo cho biết khoảng sáu mươi lăm phần trăm người cao tuổi chưa được hưởng trợ giúp xã hội của nhà nước. "
           "Bà Tư nằm trong số đông ấy.")),
 dict(k='bignum', short=True, anh=HCM, cap=('LƯƠNG HƯU BÌNH QUÂN', '6,2 TRIỆU MỖI THÁNG'), cols=CC,
      value=6.2, fmt='{:,.1f}', unit=' TRIỆU', top='LƯƠNG HƯU BÌNH QUÂN, THỐNG KÊ ĐẾN 12/2024 · VNECONOMY 10/2/2025', sub='Mỗi tháng · người đang hưởng', col=V_,
      say=("Còn người có lương hưu như ông Bảy thì nhận bao nhiêu? Lương hưu bình quân, thống kê đến cuối năm hai nghìn không trăm hai mươi tư, khoảng sáu triệu hai trăm nghìn đồng mỗi tháng. "
           "Không giàu, nhưng đủ tiền chợ, tiền điện, và quan trọng nhất là tháng nào cũng có.")),
 dict(k='noti', cap=('KHÔNG LƯƠNG HƯU', 'THÌ SỐNG BẰNG GÌ?'), cols=CR, moc=True, noti=dict(gio='20:40', ngay='Thứ Bảy 28/11', items=[
        ('Tin tức', 'VnExpress · 16/1/2025', 'Khoảng 50% người trên 60 tuổi vẫn đang làm việc', R_),
        ('Tin tức', 'VietnamPlus · 25/6/2026', 'Trợ cấp hưu trí xã hội: từ đủ 75 tuổi', V_),
        ('Tin tức', 'VnExpress · 16/1/2025', 'Cả nước: khoảng 40% tiền khám chữa bệnh tự trả', R_)]),
      say=("Không có lương hưu thì sống bằng gì? Theo khảo sát năm hai nghìn không trăm hai mươi hai mà báo VnExpress dẫn, khoảng một nửa người trên sáu mươi tuổi vẫn đang làm việc. "
           "Ai không có lương hưu, trường hợp thông thường, phải đủ bảy mươi lăm tuổi mới được nhà nước trợ cấp hưu trí xã hội hằng tháng. Đến tháng sáu năm nay, việc hạ xuống bảy mươi tuổi mới là dự thảo, tức bản đề xuất, chưa được thông qua. "
           "Và tính chung cả nước, khoảng bốn mươi phần trăm chi phí khám chữa bệnh vẫn là tiền tự bỏ túi.")),
 dict(k='call', cap=('"MẸ KHÔNG MUỐN', 'LÀM KHỔ CÁC CON"'), cols=CR, moc=True, call=dict(ten='Mẹ', phu='Đang gọi', mau=V_, loi=[
        'Mẹ không muốn làm khổ các con', 'Còn đi chợ được thì mẹ còn đi']),
      say=("Cường gọi cho mẹ, bảo mẹ nghỉ hẳn đi, con gửi tiền. Bà Tư chỉ nói: mẹ không muốn làm khổ các con, còn đi chợ được thì mẹ còn đi. "
           "Câu ấy có lẽ anh chị đã nghe ở nhà mình. Nó không phải chuyện riêng của bà Tư.")),
 # ---- Chương 3: Nhật
 dict(k='giay', ch='Chương 3 – Nhật Bản đi trước', cap=('NHẬT ĐI TRƯỚC', 'TA GIÀ NHANH HƠN'), cols=CC, moc=True, giay=dict(
        tieu_de='NHẬT BẢN ĐI TRƯỚC', so='VnExpress International 23/12/2024', dau='LẦN TRƯỚC', dieu=[
        ('Nhật thành xã hội già', 'NĂM 1994'),
        ('Nhật: từ bắt đầu già đến già', '24 NĂM'),
        ('Việt Nam dự kiến', '21 NĂM'),
        ('Mỗi người Nhật lúc ấy', '40.000 ĐÔ MỘT NĂM')]),
      say=("Nhật Bản là nước đi trước. Theo một bài phân tích trên VnExpress, từ lúc bắt đầu có nhiều người già cho đến lúc thành xã hội già, Nhật mất hai mươi tư năm. Việt Nam được dự kiến chỉ mất hai mươi mốt năm. "
           "Ta không chỉ đang tiến tới tuổi già với cái túi mỏng hơn, mà còn già nhanh hơn.")),
 dict(k='checklist', anh=HN, cap=('SO VỚI NHẬT', 'GIỐNG 2, KHÁC 1'), cols=CC, moc=True,
      items=[('Giống: sinh ít', R_), ('Giống: già rất nhanh', R_), ('Khác: túi mỏng hơn nhiều', R_), ('Còn trong tay: 10 năm vàng', G_)],
      say=("So với Nhật, có hai điểm giống: sinh ít, và già rất nhanh. Điểm khác: túi của ta mỏng hơn nhiều. "
           "Nhưng còn một thứ trong tay: khoảng mười năm dân số vàng. Mười năm đó là của cả nước, và cũng là của từng nhà.")),
 # ---- Chương 4
 dict(k='3d', ch='Chương 4 – Nhà mình cần để dành bao nhiêu', set='vanphong', light='day', cam=CAM_VP, label='SÁNG CHỦ NHẬT · VĂN PHÒNG',
      cast=[{'a': 'huy', 'p': [-0.7, 0, 0.5], 'act': 'chitay', 'side': -1, 'expr': 'smile'},
            {'a': 'cuong', 'p': [0.9, 0, 0.7], 'act': 'noi', 'side': -1, 'expr': 'worried'}],
      cap=('"TÔI LÀM TỰ DO', 'KHÔNG ĐÓNG BẢO HIỂM"'), cols=CC,
      say=("Sáng Chủ nhật Cường ghé văn phòng em. Anh làm tự do, chưa đóng bảo hiểm xã hội ngày nào. Anh hỏi: nếu Cường muốn già như ông Bảy chứ không như mẹ, thì phải để dành bao nhiêu? "
           "Em ngồi tính cùng anh, số em giả định cho dễ hình dung.")),
 dict(k='giay', short=True, cap=('TỰ LÀM LƯƠNG HƯU 6,2 TRIỆU', 'CẦN GẦN 1,5 TỶ'), cols=CC, moc=True, giay=dict(
        tieu_de='BẢNG TÍNH CỦA CƯỜNG (VÍ DỤ GIẢ ĐỊNH)', so='Chưa tính lãi và trượt giá · em tự tính', dau='VÍ DỤ', dieu=[
        ('Muốn có mỗi tháng', '6,2 TRIỆU'),
        ('Giả định từ 60 đến 80 tuổi', '240 THÁNG'),
        ('Tổng cần', 'GẦN 1,5 TỶ'),
        ('Để dành từ 35 đến 60 tuổi', 'GẦN 5 TRIỆU MỖI THÁNG')]),
      say=("Giả sử Cường muốn tự có một khoản bằng lương hưu bình quân, sáu triệu hai trăm nghìn mỗi tháng. Em tạm tính từ sáu mươi đến tám mươi tuổi, hai mươi năm, là hai trăm bốn mươi tháng. "
           "Cộng lại gần một tỷ rưỡi đồng. Chia cho ba trăm tháng từ nay đến năm sáu mươi tuổi, Cường phải để dành gần năm triệu mỗi tháng. "
           "Em chưa tính tiền lãi, cũng chưa tính giá cả tăng lên. Lãi giúp mình, còn giá tăng thì làm khoản cần lớn hơn.")),
 dict(k='bignum', short=True, anh=HCM, cap=('BẮT ĐẦU TỪ 45 TUỔI', 'PHẢI ĐỂ DÀNH 8,27 TRIỆU'), cols=CR,
      value=8.27, fmt='{:,.2f}', unit=' TRIỆU', top='MỖI THÁNG, NẾU BẮT ĐẦU ĐỂ DÀNH TỪ 45 TUỔI · EM TỰ TÍNH', sub='Gần 1,5 tỷ chia 180 tháng', col=R_,
      say=("Còn đây là cú lật. Nếu đợi đến bốn mươi lăm tuổi mới bắt đầu, chỉ còn một trăm tám mươi tháng. Mỗi tháng phải để dành hơn tám triệu. "
           "Chậm mười năm, mỗi tháng phải bỏ ra gấp hơn một rưỡi, từ gần năm triệu lên hơn tám triệu. Cái đắt nhất của chuyện để dành cho tuổi già không phải là tiền, mà là thời gian. "
           "Anh chị đã ngoài bốn mươi lăm cũng đừng nản. Bắt đầu hôm nay vẫn rẻ hơn bắt đầu năm sau.")),
 dict(k='cards', anh=HN, cap=('3 CÁCH LÀM LƯƠNG HƯU', 'CHO CHÍNH MÌNH'), cols=CC, moc=True,
      cards=[('CÁCH 1', 'Bảo hiểm xã hội tự nguyện', 'Đóng đủ số năm tối thiểu'), ('CÁCH 2', 'Góp đều mỗi tháng', 'Khoản cố định, để lâu năm'), ('CÁCH 3', 'Một nghề làm được lâu', 'Không cần sức nặng')],
      say=("Có ba cách để tự làm lương hưu cho mình. Một, đóng bảo hiểm xã hội tự nguyện, hỏi ở cơ quan bảo hiểm xã hội nơi mình ở. Đóng đủ số năm tối thiểu theo luật thì về già có một khoản hằng tháng. "
           "Hai, mỗi tháng góp đều một khoản cố định để lâu năm, gửi tiết kiệm hay cách khác thì anh chị chọn cái mình yên tâm. "
           "Ba, có một nghề làm được đến tuổi già mà không cần sức nặng như gánh rau ra chợ. Ba cách này làm cùng lúc được, càng nhiều cửa càng chắc.")),
 dict(k='chat', cap=('"MỖI THÁNG 5 TRIỆU', 'TRƯỚC KHI TIÊU"'), cols=CC, moc=True, chat=dict(ten='Vợ Cường', tv='Đang hoạt động', gio='21:00', mau=V_, msgs=[
        ('me', 'Từ tháng sau để riêng 5 triệu trước đã'),
        ('Vợ Cường', 'Còn tiền gửi mẹ thì sao anh?'),
        ('me', 'Vẫn gửi mẹ, bớt tiền ăn ngoài'),
        ('Vợ Cường', 'Thế thì được, cả nhà cùng làm')]),
      say=("Tối Chủ nhật Cường bàn với vợ: từ tháng sau, để riêng năm triệu ngay khi nhận lương, trước khi tiêu bất cứ thứ gì. Vợ hỏi còn tiền gửi mẹ thì sao. "
           "Cường bảo vẫn gửi mẹ đều, chỉ bớt tiền ăn ngoài. Lo cho bố mẹ hôm nay, và lo cho chính mình ngày mai, phải đi cùng nhau.")),
 dict(k='checklist', ch='Phép thử tuổi 60', cap=('NĂM 60 TUỔI', 'TIỀN CHỢ NHÀ MÌNH TỪ ĐÂU?'), cols=CC, moc=True,
      items=[('Có lương hưu, có để dành', G_), ('Chỉ có một trong hai', V_), ('Chưa có gì, trông vào con', R_)],
      say=("Em gửi anh chị một phép thử. Hình dung năm sáu mươi tuổi, tiền chợ mỗi tháng của nhà mình đến từ đâu? "
           "Nếu vừa có lương hưu, vừa có khoản để dành, anh chị đang đi đúng hướng. Nếu chỉ có một trong hai, nên bổ sung cái còn thiếu sớm. "
           "Nếu chưa có gì và đang trông vào con, thì hôm nay là ngày rẻ nhất để bắt đầu. Đây là mốc em tự đặt để soi, anh chị cân theo hoàn cảnh nhà mình.")),
 dict(k='giay', cap=('3 VIỆC LÀM NGAY', 'TRONG TUẦN NÀY'), cols=CC, moc=True, giay=dict(
        tieu_de='BA VIỆC TUẦN NÀY', so='Gợi ý của Huy Nguyễn', dau='LÀM NGAY', dieu=[
        ('Hỏi bố mẹ', 'CÓ LƯƠNG HƯU CHƯA?'),
        ('Hỏi cơ quan bảo hiểm xã hội', 'ĐÓNG TỰ NGUYỆN'),
        ('Mở sổ riêng, để vào trước', 'SỔ TUỔI GIÀ')]),
      say=("Và ba việc làm được ngay trong tuần này. Một, hỏi bố mẹ xem đang có lương hưu hay chưa, để biết nhà mình cần đỡ bao nhiêu. "
           "Hai, hỏi cơ quan bảo hiểm xã hội về đóng tự nguyện. Ba, mở một sổ tiết kiệm riêng, ghi tên là tuổi già, và mỗi tháng để vào trước rồi mới tiêu.")),
 # ---- Kết
 dict(k='3d', ch='Kết', set='cafevh', light='day', cam=CAM_CF, label='QUÁN NƯỚC · TUẦN SAU',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'noi', 'ngoi': True, 'expr': 'relief'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'}],
      cap=('GIÀ TRƯỚC KHI GIÀU', 'LÀ CHUYỆN CẢ NƯỚC'), cols=CC,
      say=("Tuần sau, Cường kể với Hùng rằng anh đã mở sổ để dành riêng cho tuổi già. Hùng cười bảo bố Hùng có lương hưu vì ngày xưa nhà máy bắt đóng, còn Cường giờ phải tự bắt mình. "
           "Già trước khi giàu là chuyện của cả nước. Nhưng già có tiền hay không, phần lớn là chuyện của từng nhà.")),
 dict(k='cards', anh=HCM, cap=('GÓP ĐỀU MỖI THÁNG', 'EM ĐỂ SẴN BẢNG TRÊN WEB'), cols=CC, moc=True,
      cards=[('Trên web', 'Bảng góp đều mỗi tháng', 'Số liệu cập nhật'), ('Miễn phí', 'Xem không cần đăng ký', 'Chứng khoán Huy Nguyễn'), ('Tính vẫn rối?', 'Zalo 0365.188.286', 'Em tính cùng anh chị')],
      say=("Bảng theo dõi góp đều mỗi tháng, em để sẵn trên web chứng khoán Huy Nguyễn chấm com, xem miễn phí. "
           "Nếu anh chị muốn tính xem nhà mình cần để dành bao nhiêu cho tuổi già, cứ nhắn Zalo cho em. Em tính cùng, anh chị tự quyết.")),
 dict(k='end', cap=('NĂM 60 TUỔI', 'TIỀN CHỢ NHÀ ANH CHỊ TỪ ĐÂU?'), cols=CC,
      say=("Còn anh chị, năm sáu mươi tuổi, tiền chợ nhà mình sẽ đến từ lương hưu, từ khoản để dành, hay từ con cái? Kể em nghe ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=50)
for c in S: c['say'] = lib.doc(phat_am_doc(c['say']))

TIEU = '6 Người Già, 1 Có Lương Hưu, Trợ Cấp: Ai Nuôi Mình Lúc Già?'
MT = ("Cứ 6 người cao tuổi ở Việt Nam, chỉ khoảng 1 người có lương hưu hoặc trợ cấp bảo hiểm xã hội hằng tháng. Năm 1994, Nhật Bản thành xã hội già khi mỗi người làm ra khoảng 40.000 USD một năm; Việt Nam năm 2024 khoảng 4.700 USD – và theo dự báo, năm 2034 đã thành nước dân số già. "
      "Ta già nhanh cỡ nào, bao nhiêu người già đang có lương hưu, và nếu tự làm lương hưu 6,2 triệu mỗi tháng thì nhà mình phải để dành bao nhiêu. "
      "Cường, Hùng, bà Tư, ông Bảy là nhân vật hư cấu; số liệu là thật.\n\n"
      "Nguồn số liệu:\n"
      "• Tuổi Trẻ 27/1/2026: Việt Nam bước vào thời kỳ dân số già từ 2034 (người từ 65 tuổi đạt 14%); kết thúc dân số vàng khoảng 2036; năm 2024 có khoảng 14,2 triệu người từ 60 tuổi, năm 2034 khoảng 20,9 triệu\n"
      "• VietNamNet 14/7/2026: dân số vàng từ 2007, đã tận dụng 20 năm, còn khoảng 10 năm (GS Nguyễn Đình Cử); 2024 cứ 100 trẻ em có khoảng 60 người cao tuổi\n"
      "• VietNamNet 27/3/2025: mức sinh 2024 còn 1,91 con/phụ nữ; thu nhập bình quân đầu người khoảng 4.700 USD năm 2024. Mức sinh thay thế 2,1 con (Việt Báo/VnExpress 6/11/2026)\n"
      "• VnExpress International 23/12/2024 (bài phân tích): Nhật Bản thành xã hội già năm 1994, GDP bình quân đầu người khi đó 40.000 USD; Nhật mất 24 năm từ già hoá đến xã hội già, Việt Nam dự kiến 21 năm\n"
      "• VnEconomy 9/7/2024: 16,1 triệu người cao tuổi; 2,7 triệu người cao tuổi hưởng lương hưu và trợ cấp bảo hiểm xã hội hằng tháng; khoảng 65% chưa được hưởng trợ giúp xã hội\n"
      "• VnEconomy 10/2/2025: lương hưu bình quân 6,2 triệu đồng/tháng (thống kê đến 12/2024)\n"
      "• VnExpress 16/1/2025: khoảng 50% người trên 60 tuổi vẫn làm việc (khảo sát quốc gia 2022); chi tiền túi khoảng 40% tổng chi phí khám chữa bệnh (WHO)\n"
      "• VietnamPlus 25/6/2026: trợ cấp hưu trí xã hội từ đủ 75 tuổi (thông thường), 70 đến dưới 75 với hộ nghèo, cận nghèo; dự thảo đề xuất giảm dần xuống 70 tuổi\n"
      "• Em tự tính: 40.000 ÷ 4.700 = 8,5 lần (số Nhật là GDP bình quân đầu người, số Việt Nam là thu nhập bình quân đầu người – hai thước đo gần nhau, không hoàn toàn giống); 2,7 ÷ 16,1 = 16,8%; ví dụ giả định: 6,2 triệu × 240 tháng = 1.488 triệu; để dành 300 tháng (35–60 tuổi) = 4,96 triệu/tháng; 180 tháng (45–60 tuổi) = 8,27 triệu/tháng; 8,27 ÷ 4,96 = 1,67 lần; chưa tính lãi và trượt giá.\n\n"
      "Bảng góp đều mỗi tháng: https://chungkhoanhuynguyen.com\n"
      "Cần tính kế hoạch để dành cho tuổi già: Zalo 0365.188.286")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Vĩ mô chạm túi tiền', ngay='2026-12-02', gio_goi_y='17:00', gio='17:00', nhac='lofi', can_duyet='anh Huy duyệt trước khi hẹn',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['già trước khi giàu', 'dân số già Việt Nam', 'Nhật Bản', 'lương hưu', 'bảo hiểm xã hội tự nguyện', 'dân số vàng', 'tiết kiệm hưu trí', 'tích sản', 'kinh tế Việt Nam', 'người cao tuổi'],
    bia_hook=['6 NGƯỜI GIÀ', '1 CÓ LƯƠNG HƯU'], badge='LƯƠNG HƯU HOẶC TRỢ CẤP', bia_anh='ov:Hanoi skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['NHẬT 40.000 ĐÔ', 'TA 4.700 ĐÔ???'], badge_b='GIÀ TRƯỚC KHI GIÀU',
    bia_hook_c=['CHẬM 10 NĂM', 'TIỀN GẤP RƯỠI'], badge_c='TỰ LÀM LƯƠNG HƯU',
    reel_hook='6 NGƯỜI GIÀ|CHỈ 1 CÓ LƯƠNG HƯU???',
    fb_post=("Nhật Bản già khi mỗi người làm ra 40.000 đô một năm. Việt Nam sắp già khi mới khoảng 4.700 đô.\n"
             "👉 2034 thành nước dân số già, khoảng 2036 hết dân số vàng\n👉 Cứ 6 người cao tuổi chỉ khoảng 1 người có lương hưu, trợ cấp BHXH hằng tháng\n👉 Tự làm lương hưu 6,2 triệu/tháng: để dành từ 35 tuổi gần 5 triệu/tháng, từ 45 tuổi hơn 8 triệu (gấp hơn 1,6 lần)\n"
             "Năm 60 tuổi, tiền chợ nhà mình từ đâu?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – Vĩ mô chạm túi tiền: GIÀ TRƯỚC KHI GIÀU (NV1 28/11/2026). 3 cảnh 3D.\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    exec(open(os.path.join(os.path.dirname(__file__), '_kiem_chung.py'), encoding='utf-8').read())
