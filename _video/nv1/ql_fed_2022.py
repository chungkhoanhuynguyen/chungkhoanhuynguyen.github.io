# -*- coding: utf-8 -*-
# NV1 16/11/2026 01:30 – VIDEO DÀI kênh chính, "câu hỏi lớn": Mỹ quay lại tăng lãi suất, cổ phiếu AI lao dốc – lần trước năm 2022 VN-Index mất 33%, lần này túi anh chị bị gì?
# Lý do chọn: data/view/xu_huong.md tuần tới 15/11: "CÚ SỐC SAU BẦU CỬ MỸ, CỔ PHIẾU AI LAO DỐC, DẦU GIẢM 13%" ~81 nghìn view; "USD SURGES, US interest rates SOAR" ~70 nghìn;
#   "Sau bầu cử, lạm phát Mỹ kéo dài, Fed có thể tăng lãi suất cuối năm?" ~42 nghìn; "Jensen Huang… Nvidia" ~111 nghìn. Kênh mình: THẾ GIỚI/CÚ SẬP thắng (Iran 647, VN-Index 2022 883 view).
#   7 ngày chưa làm Fed/thế giới (đã làm: nợ công 14/11, GDP 16/11, xuất khẩu 17/11, Thái Lan 18/11, nhà đất 19/11, vốn 38,5 triệu tỷ 20/11). WiData hết credit tới 20/11 → số lấy từ báo, ghi đủ tên báo + ngày.
# Nguồn:
#  - Vietnam+ 11/11/2026: lãi suất Fed 3,75–4,00% (Chủ tịch Fed Dallas Lorie Logan); CPI Mỹ tháng 10 +0,4% so tháng trước (tháng 9 +0,6%), lõi +0,3% tháng thứ ba liền.
#  - Vietnam+ 11/11/2026 (bài "Mỹ: Lạm phát tháng 10 cao hơn dự báo"): giá xăng Mỹ +37% so cùng kỳ; CME FedWatch: xác suất tăng lãi suất tháng 12 trên 80%; họp 8–9/12.
#  - CafeF 12/11/2026: Fed đã tăng lãi suất tháng 9; Deutsche Bank dự báo 3 lần tăng 0,25 điểm nữa, tổng 1 điểm tính cả tháng 9; 0,5 điểm sẽ là bước lớn nhất từ 2022;
#    lợi suất trái phiếu Mỹ 2 năm +0,18 điểm lên 4,725%; Pimco: "chưa phải lặp lại 2022, khi lạm phát Mỹ trên 9%".
#  - MoneyF 14/11/2026: thị trường dự báo tăng 0,25 điểm ở 3 cuộc họp 12/2026, 1/2027, 3/2027.
#  - Vietnam+ 14/11/2026: PPI Mỹ tháng 10 +6,5% so cùng kỳ, cao nhất từ 11/2022; Nvidia: CEO Jensen Huang từ chức, phiên 12/11 có lúc giảm 13%, đóng cửa −4,3%;
#    tuần giảm thứ sáu liên tiếp, chuỗi dài nhất từ 10/2012; S&P 500 và Nasdaq chấm dứt 4 tuần giảm liên tiếp (tuần 9–13/11 S&P 500 +2,51%).
#  - Hà Nội Mới 14/11/2026: DXY 103,41 điểm, +1,09% trong tuần, cao nhất từ 4/2025; tỷ giá trung tâm 25.637 (+22 đồng); Vietcombank bán 25.910 (+130 đồng).
#  - Người Quan Sát 13/11/2026: NHNN yêu cầu thanh tra việc giảm lãi suất tại các ngân hàng ngay trong tháng 11.
#  - Lịch sử 2022: Fed tăng 7 lần, từ 0–0,25% lên 4,25–4,5%; VN-Index đóng cửa 31/12/2021 1.498,28, 30/12/2022 1.007,09 (BSC Daily Review 30/12/2022) → −32,8% (tự tính);
#    NHNN tăng lãi suất điều hành 2 lần (22/9/2022 và 25/10/2022), mỗi lần 1 điểm %.
#  - GIẢ ĐỊNH minh hoạ (nhà anh Khoa): cổ phiếu 400 triệu, trong đó vay ký quỹ 150 triệu → vốn thật 250 triệu. Giảm 20% → 320 triệu, trả 150 còn 170 → mất 80/250 = 32% vốn.
#    Vay mua nhà 2 tỷ lãi thả nổi: tăng 1 điểm % → 20 triệu mỗi năm ≈ 1,67 triệu mỗi tháng.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261116_0130'
KEY = 'CH2111FED'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
WM = 'Blue Marble||World map'     # cảnh số nước Mỹ: không dùng ảnh thành phố nước ngoài theo từ khoá (PPC v1.6–1.7)
SGD = 'ov:Ho Chi Minh City Stock Exchange||Bitexco Financial Tower'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('MỸ SẮP TĂNG LÃI SUẤT', 'LẦN TRƯỚC VN-INDEX MẤT 32,8%'), cols=CR, noti=dict(gio='21:10', ngay='Thứ Sáu', items=[
        ('Tin tức', 'Vietnam+', 'Khả năng Fed tăng lãi suất tháng 12 trên 80%', V_),
        ('Zalo', 'Linh (Mỹ)', 'Cổ phiếu chip bên này giảm 6 tuần liền rồi', R_),
        ('Ngân hàng', 'Nhắc nợ', 'Khoản vay nhà kỳ tới áp lãi suất thả nổi', X_)]),
      say=("Hơn tám mươi phần trăm. Đó là khả năng Ngân hàng Trung ương Mỹ tăng lãi suất trong cuộc họp tháng mười hai, theo công cụ dự báo của sàn giao dịch CME, được báo chí trong nước dẫn tuần này. "
           "Tối nay anh Khoa, kỹ sư phần mềm ở Thành phố Hồ Chí Minh, đọc tin đó thì nhận tin nhắn của Linh, người học cùng đại học đang làm ở Mỹ. Linh viết: cổ phiếu chip bên này giảm sáu tuần liền rồi. "
           "Cùng lúc, ngân hàng nhắc khoản vay mua nhà của anh sắp sang kỳ lãi suất thả nổi.")),
 dict(k='bignum', anh=SGD, cap=('NĂM 2022 MỸ TĂNG LÃI SUẤT', 'VN-INDEX MẤT 32,8%'), cols=CR, value=32.8, fmt='{:,.1f}', unit='%', top='VN-INDEX NĂM 2022 GIẢM', sub='1.498 xuống 1.007 điểm – em tự tính', col=RED,
      say=("Anh Khoa nhớ rất rõ lần gần nhất Mỹ tăng lãi suất mạnh. Đó là năm 2022. Cả năm đó, chỉ số VN-Index giảm từ một nghìn bốn trăm chín mươi tám điểm xuống còn một nghìn không trăm linh bảy điểm, mất ba mươi hai phẩy tám phần trăm. "
           "Bây giờ Mỹ lại bắt đầu tăng. Câu hỏi là: năm 2022 có lặp lại không, và lần này túi của anh chị bị chạm vào chỗ nào?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Chuyện gì đang xảy ra ở Mỹ?', cap=('"XĂNG BÊN NÀY ĐẮT HƠN', 'NĂM NGOÁI HƠN 1/3"'), cols=CR, moc=True, chat=dict(ten='Linh (Mỹ)', tv='Đang hoạt động', gio='21:25', mau=R_, msgs=[
        ('Linh (Mỹ)', 'Xăng bên này đắt hơn năm ngoái 37% đấy'),
        ('Linh (Mỹ)', 'Mọi thứ cứ lên giá từng tháng'),
        ('me', 'Vậy nên Fed lại phải tăng lãi suất à?'),
        ('Linh (Mỹ)', 'Ừ, tháng 9 tăng rồi, tháng 12 chắc tăng tiếp')]),
      say=("Linh kể: xăng bên đó đắt hơn năm ngoái ba mươi bảy phần trăm, mọi thứ cứ lên giá từng tháng một. Anh Khoa hỏi: vậy nên Ngân hàng Trung ương Mỹ, tức là Fed, lại phải tăng lãi suất sao. "
           "Linh trả lời: tháng chín tăng rồi, tháng mười hai chắc tăng tiếp.")),
 dict(k='giay', cap=('LẠM PHÁT MỸ', 'CHƯA CHỊU HẠ'), cols=CR, moc=True, giay=dict(tieu_de='NƯỚC MỸ, THÁNG 10/2026', so='Vietnam+ 11/11 và 14/11/2026, CafeF 12/11', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Giá xăng so với cùng kỳ', 'TĂNG 37%'),
        ('Giá sản xuất, cao nhất từ 11/2022', 'TĂNG 6,5%'),
        ('Lãi suất Fed hiện nay', '3,75 ĐẾN 4%'),
        ('Khả năng tăng tiếp tháng 12', 'TRÊN 80%')]),
      say=("Số liệu chính thức nói đúng như vậy. Giá cả tiêu dùng của Mỹ tháng mười tăng không phẩy bốn phần trăm chỉ trong một tháng. Giá sản xuất tăng sáu phẩy năm phần trăm so với cùng kỳ, cao nhất kể từ tháng mười một năm 2022. "
           "Lãi suất Fed đang ở mức ba phẩy bảy lăm đến bốn phần trăm, và thị trường bắt đầu tính tới ba lần tăng nữa: tháng mười hai năm nay, tháng một và tháng ba năm sau.")),
 dict(k='cards', anh=WM, cap=('CỔ PHIẾU AI CHAO ĐẢO', 'NVIDIA GIẢM 6 TUẦN LIỀN'), cols=CR, moc=True,
      cards=[('6 tuần', 'Nvidia giảm liên tiếp', 'Dài nhất từ 10/2012'), ('13%', 'Có lúc giảm trong phiên 12/11', 'Ngày CEO từ chức'), ('4 tuần', 'S&P 500 giảm liên tiếp', 'Tuần qua mới hồi lại')],
      say=("Cùng lúc đó, nhóm cổ phiếu trí tuệ nhân tạo, thứ kéo chứng khoán Mỹ đi lên mấy năm qua, chao đảo. Ngày mười hai tháng mười một, giám đốc điều hành Nvidia, ông Jensen Huang, từ chức. "
           "Cổ phiếu Nvidia có lúc giảm mười ba phần trăm trong phiên, và đã giảm sáu tuần liên tiếp, chuỗi dài nhất kể từ năm 2012. Chỉ số S&P năm trăm cũng giảm bốn tuần liền, tuần vừa rồi mới hồi lại.")),
 dict(k='bignum', anh=WM, cap=('ĐỒNG ĐÔ LA MẠNH NHẤT', 'TỪ THÁNG 4/2025'), cols=CR, moc=True, value=103.41, fmt='{:,.2f}', unit='', top='CHỈ SỐ ĐÔ LA DXY', sub='cao nhất từ 4/2025 – Hà Nội Mới 14/11/2026', col=RED,
      say=("Và khi lãi suất Mỹ sắp tăng, đồng đô la mạnh lên. Chỉ số đo sức mạnh đồng đô la vừa lên một trăm linh ba phẩy bốn mốt điểm, tăng hơn một phần trăm chỉ trong một tuần. Đây là mức cao nhất kể từ tháng tư năm 2025. "
           "Đây là chỗ câu chuyện bên Mỹ bắt đầu chạm vào Việt Nam.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Đô la mạnh lên, Việt Nam chịu gì?', anh=TP, cap=('TỶ GIÁ TĂNG', 'NGAY TRONG MỘT TUẦN'), cols=CR, moc=True,
      cards=[('25.637', 'Tỷ giá trung tâm', 'Tăng 22 đồng trong tuần'), ('25.910', 'Giá bán đô la ở Vietcombank', 'Tăng 130 đồng'), ('4,725%', 'Lợi suất trái phiếu Mỹ 2 năm', 'Một ngày tăng 0,18 điểm')],
      say=("Ngay trong tuần qua, tỷ giá trung tâm lên hai mươi lăm nghìn sáu trăm ba mươi bảy đồng một đô la. Giá bán đô la ở một ngân hàng lớn lên hai mươi lăm nghìn chín trăm mười đồng, tăng một trăm ba mươi đồng. "
           "Ở Mỹ, lãi suất trái phiếu hai năm vọt lên bốn phẩy bảy hai lăm phần trăm. Khi gửi tiền ở Mỹ lãi ngày càng cao, đồng tiền của thế giới có xu hướng chảy về Mỹ.")),
 dict(k='text', anh=HN, cap=('MỸ TĂNG LÃI SUẤT', 'VIỆT NAM LẠI MUỐN GIẢM'), cols=CR, moc=True,
      say=("Và đây là cú lật. Trong khi Mỹ tăng lãi suất, Việt Nam lại đang muốn giảm. Ngân hàng Nhà nước vừa yêu cầu thanh tra việc giảm lãi suất tại các ngân hàng ngay trong tháng mười một. "
           "Hai nước đi hai hướng ngược nhau. Lãi suất tiền đồng thấp đi, lãi suất đô la cao lên, thì giữ đô la trở nên hấp dẫn hơn. Áp lực dồn vào tỷ giá, và vào cả thị trường chứng khoán.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Năm 2022 đã xảy ra chuyện gì?', cap=('"NĂM 2022 ANH BỊ BÁN', 'GIẢI CHẤP 3 LẦN"'), cols=CR, moc=True, call=dict(ten='Anh Tùng', phu='Gọi thoại', mau=V_, loi=[
        'Lúc đầu ai cũng bảo Mỹ xa lắm', 'Đến tháng 11 thì cả phòng bán sạch']),
      say=("Anh Khoa gọi cho anh Tùng, đồng nghiệp cũ từng chơi chứng khoán từ năm 2020. Anh Tùng kể: năm 2022, lúc đầu ai cũng bảo chuyện lãi suất Mỹ xa lắm, không liên quan. "
           "Rồi anh bị công ty chứng khoán bán giải chấp ba lần vì vay ký quỹ. Đến tháng mười một năm đó, cả nhóm đầu tư của anh gần như bán sạch, đúng lúc thị trường xuống sâu nhất.")),
 dict(k='giay', cap=('NĂM 2022', 'NHỮNG CON SỐ CỦA CÚ RƠI'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ NĂM 2022', so='Fed, Ngân hàng Nhà nước, BSC 30/12/2022', dau='ĐÃ XẢY RA', dieu=[
        ('Fed tăng lãi suất trong năm', '7 LẦN'),
        ('Lãi suất Fed cuối năm', '4,25 ĐẾN 4,5%'),
        ('Ngân hàng Nhà nước tăng lãi suất', '2 LẦN'),
        ('VN-Index cả năm', 'GIẢM 32,8%')]),
      say=("Những gì anh Tùng kể có trong số liệu. Năm 2022, Fed tăng lãi suất bảy lần, từ gần bằng không lên bốn phẩy hai lăm đến bốn phẩy năm phần trăm. "
           "Để giữ tỷ giá, Ngân hàng Nhà nước Việt Nam tăng lãi suất điều hành hai lần trong tháng chín và tháng mười, mỗi lần một điểm phần trăm. "
           "Chỉ số VN-Index kết thúc năm ở một nghìn không trăm linh bảy điểm, mất ba mươi hai phẩy tám phần trăm.")),
 dict(k='checklist', anh=TP, cap=('BÂY GIỜ VÀ NĂM 2022', 'GIỐNG 2, KHÁC 2'), cols=CR, moc=True,
      items=[('Mỹ tăng vì lạm phát: giống', RED),
             ('Đô la mạnh lên: giống', RED),
             ('Lạm phát Mỹ 2022 trên 9%', GREEN),
             ('Lần này tính thêm khoảng 1 điểm', GREEN)],
      say=("Nhưng đặt hai thời điểm cạnh nhau cho công bằng. Giống thứ nhất: Mỹ tăng lãi suất vì lạm phát không chịu hạ. Giống thứ hai: đồng đô la mạnh lên, tỷ giá chịu áp lực. "
           "Khác thứ nhất: năm 2022, lạm phát Mỹ vượt chín phần trăm. Một chuyên gia của quỹ Pimco nói lần này chưa phải lặp lại năm 2022. "
           "Khác thứ hai: năm 2022 Fed tăng hơn bốn điểm phần trăm, còn lần này thị trường đang tính tổng cộng khoảng một điểm, tính cả lần tháng chín. Chưa phải cơn bão, nhưng chưa, không có nghĩa là không thể.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='giay', ch='Chương 4 – Túi của anh Khoa', cap=('CỔ PHIẾU 400 TRIỆU', 'TRONG ĐÓ 150 TRIỆU ĐI VAY'), cols=CR, moc=True, giay=dict(tieu_de='TÀI KHOẢN VÀ KHOẢN VAY NHÀ ANH KHOA', so='Em giả định để minh hoạ', dau='TỰ KÊ', dieu=[
        ('Cổ phiếu đang giữ', '400 TR'),
        ('Trong đó vay ký quỹ', '150 TR'),
        ('Vốn thật bỏ ra', '250 TR'),
        ('Vay mua nhà, lãi thả nổi', '2 TỶ')]),
      say=("Anh Khoa mở tài khoản ra xem. Số này em giả định để minh hoạ: anh đang giữ bốn trăm triệu cổ phiếu, trong đó một trăm năm mươi triệu là tiền vay ký quỹ của công ty chứng khoán. Vốn thật của anh là hai trăm năm mươi triệu. "
           "Ngoài ra, nhà anh còn khoản vay mua nhà hai tỷ, sắp sang kỳ lãi suất thả nổi.")),
 dict(k='chat', cap=('NẾU THỊ TRƯỜNG GIẢM 20%', 'VỐN NHÀ KHOA MẤT 32%'), cols=CR, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:20', mau=G_, msgs=[
        ('Vợ', 'Nếu như năm 2022 thì nhà mình mất bao nhiêu?'),
        ('me', 'Giảm 20% thì 400 còn 320 triệu'),
        ('me', 'Trả 150 nợ còn 170, mất 32% vốn'),
        ('Vợ', 'Lãi nhà tăng 1 điểm là thêm 20 triệu một năm')]),
      say=("Vợ anh hỏi: nếu như năm 2022 thì nhà mình mất bao nhiêu. Anh tính: chỉ cần giảm hai mươi phần trăm, bốn trăm triệu còn ba trăm hai mươi triệu. "
           "Trả một trăm năm mươi triệu nợ, còn một trăm bảy mươi triệu. Vốn thật hai trăm năm mươi triệu mất ba mươi hai phần trăm, dù thị trường chỉ giảm hai mươi phần trăm. "
           "Vợ anh nhắc thêm: lãi vay nhà mà tăng một điểm phần trăm thì mỗi năm trả thêm hai mươi triệu, khoảng một triệu bảy trăm nghìn mỗi tháng.")),
 dict(k='cards', anh=SGD, cap=('PHƯƠNG ÁN KHÁC', 'ĐỂ KHÔNG BỊ BÁN GIẢI CHẤP'), cols=CC, moc=True,
      cards=[('150 triệu', 'Khoản vay ký quỹ', 'Trả bớt trước tiên'), ('6 tháng', 'Quỹ dự phòng chi tiêu', 'Kể cả tiền trả góp nhà'), ('1 điểm', 'Lãi vay nhà có thể tăng', 'Tính trước vào ngân sách')],
      say=("Có một con đường khác, không cần bán hết hay đoán đúng thị trường. Việc đầu tiên là trả bớt khoản vay ký quỹ một trăm năm mươi triệu, vì đòn bẩy làm khoản lỗ to gần gấp rưỡi. "
           "Việc thứ hai là quỹ dự phòng đủ sáu tháng chi tiêu, tính cả tiền trả góp nhà. Việc thứ ba là cộng sẵn vào ngân sách khả năng lãi vay nhà tăng thêm một điểm phần trăm.")),
 dict(k='chat', cap=('KẾ HOẠCH NHÀ ANH KHOA', 'BỚT VAY, GIỮ TIỀN DỰ PHÒNG'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:45', mau=G_, msgs=[
        ('me', 'Mai anh bán bớt, trả hết phần vay ký quỹ'),
        ('Vợ', 'Ừ, phần còn lại là tiền thật của mình'),
        ('me', 'Để riêng 6 tháng chi tiêu và tiền góp nhà'),
        ('Vợ', 'Tháng 12 Fed họp xong mình ngồi tính lại')]),
      say=("Hai vợ chồng thống nhất: anh Khoa bán bớt để trả hết phần vay ký quỹ, phần còn lại là tiền thật của mình, giảm thì đau nhưng không bị bán giải chấp. "
           "Để riêng sáu tháng chi tiêu và tiền góp nhà. Và sau cuộc họp của Fed tháng mười hai, hai vợ chồng ngồi tính lại một lần nữa.")),
 dict(k='checklist', anh=TP, cap=('PHÉP THỬ CỦA ANH CHỊ', 'GIẢM 20% VÀ LÃI TĂNG 1 ĐIỂM'), cols=CC, moc=True,
      items=[('Vẫn ngủ ngon: đang ổn', GREEN),
             ('Phải cắt chi tiêu: nên bớt vay', GOLD),
             ('Phải bán gấp: đang quá đòn bẩy', RED)],
      say=("Và đây là phép thử anh chị làm được ngay tối nay. Giả sử cổ phiếu nhà mình giảm hai mươi phần trăm, và lãi vay tăng thêm một điểm phần trăm, cùng một lúc. "
           "Nếu nhà mình vẫn ngủ ngon, mọi thứ đang ổn. Nếu phải cắt chi tiêu, nên bớt vay dần. Còn nếu phải bán gấp, nhà mình đang dùng đòn bẩy quá sức. "
           "Đây là mốc em đặt để tự soi, không phải quy định.")),
 dict(k='checklist', ch='Chương 5 – Theo dõi gì để biết sớm?', anh=SGD, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY ĐẾN THÁNG 3/2027'), cols=CC, moc=True,
      items=[('Fed họp ngày 8 và 9/12', GOLD),
             ('Giá bán đô la ở ngân hàng', RED),
             ('Lãi suất vay trong nước', GOLD)],
      say=("Muốn biết sớm năm 2022 có lặp lại không, em gợi ý theo dõi ba điều. Một: cuộc họp của Fed ngày tám và chín tháng mười hai, tăng không phẩy hai lăm hay không phẩy năm điểm phần trăm. "
           "Hai: giá bán đô la ở các ngân hàng lớn có tiếp tục leo lên không. Ba: lãi suất cho vay trong nước có đảo chiều tăng không. "
           "Riêng lợi nhuận từng quý của các doanh nghiệp trên sàn, kể cả nhóm hay bị ảnh hưởng khi tỷ giá tăng, anh chị xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn từ Mỹ', cap=('"BÊN NÀY HẮT HƠI', 'BÊN ĐÓ ĐỪNG ĐỂ BỊ CẢM"'), cols=CC, moc=True, chat=dict(ten='Linh (Mỹ)', tv='Đang hoạt động', gio='23:30', mau=R_, msgs=[
        ('Linh (Mỹ)', 'Bên này hắt hơi thì bên đó đừng để bị cảm nhé'),
        ('me', 'Ừ, mình vừa trả bớt nợ rồi'),
        ('Linh (Mỹ)', 'Vậy là yên tâm hơn năm 2022 rồi')]),
      say=("Gần nửa đêm, Linh nhắn: nước Mỹ hắt hơi thì bên đó đừng để bị cảm nhé. Anh Khoa trả lời rằng anh vừa quyết định trả bớt nợ. "
           "Không ai biết chắc thị trường sẽ đi đâu, nhưng người bị tổn thương nhất năm 2022 không phải người cầm cổ phiếu, mà là người cầm cổ phiếu bằng tiền vay.")),
 dict(k='end', cap=('MỸ TĂNG LÃI SUẤT', 'NĂM 2022 CÓ LẶP LẠI?'), cols=CC,
      say=("Còn anh chị thì sao: nếu cổ phiếu giảm hai mươi phần trăm và lãi vay tăng một điểm, nhà mình vẫn ngủ ngon, phải cắt chi tiêu, hay phải bán gấp? Kể cho em và mọi người ở phần bình luận nhé. "
           "Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Mỹ Quay Lại Tăng Lãi Suất: Lần Trước Năm 2022, VN-Index Mất 32,8% – Lần Này Túi Anh Chị Bị Gì?'
MT = ("Khả năng Fed tăng lãi suất tháng 12 trên 80%, giá xăng Mỹ tăng 37%, Nvidia giảm 6 tuần liền sau khi CEO từ chức, chỉ số đô la DXY cao nhất từ 4/2025. "
      "Năm 2022, Fed tăng lãi suất 7 lần và VN-Index mất 32,8%. Lần này giống và khác ở đâu? Câu chuyện của anh Khoa, người bạn Linh ở Mỹ, và phép thử cho chính gia đình anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• Vietnam+ 11/11/2026: lãi suất Fed 3,75–4,00%; CPI Mỹ tháng 10 +0,4% so tháng trước, lõi +0,3%; giá xăng +37% so cùng kỳ; CME FedWatch: xác suất tăng lãi suất tháng 12 trên 80%, họp 8–9/12\n"
      "• CafeF 12/11/2026: Fed đã tăng lãi suất tháng 9; dự báo 3 lần tăng 0,25 điểm nữa, tổng khoảng 1 điểm tính cả tháng 9; lợi suất trái phiếu Mỹ 2 năm 4,725%; Pimco: chưa phải lặp lại 2022, khi lạm phát Mỹ trên 9%\n"
      "• MoneyF 14/11/2026: thị trường dự báo tăng 0,25 điểm ở 3 cuộc họp 12/2026, 1/2027, 3/2027\n"
      "• Vietnam+ 14/11/2026: PPI Mỹ tháng 10 +6,5% so cùng kỳ, cao nhất từ 11/2022; CEO Nvidia từ chức, cổ phiếu có lúc −13% phiên 12/11, giảm 6 tuần liên tiếp (dài nhất từ 10/2012); S&P 500 dừng chuỗi 4 tuần giảm\n"
      "• Hà Nội Mới 14/11/2026: DXY 103,41 điểm, cao nhất từ 4/2025; tỷ giá trung tâm 25.637 đồng (+22); Vietcombank bán 25.910 đồng (+130)\n"
      "• Người Quan Sát 13/11/2026: NHNN yêu cầu thanh tra việc giảm lãi suất tại các ngân hàng trong tháng 11\n"
      "• Năm 2022: Fed tăng lãi suất 7 lần lên 4,25–4,5%; NHNN tăng lãi suất điều hành 2 lần (9 và 10/2022), mỗi lần 1 điểm; VN-Index 31/12/2021: 1.498,28 điểm, 30/12/2022: 1.007,09 điểm (BSC Daily Review 30/12/2022) → −32,8% (tự tính)\n"
      "• Tài khoản và khoản vay nhà anh Khoa là giả định minh hoạ: 400 triệu cổ phiếu, vay ký quỹ 150 triệu, vốn thật 250 triệu; giảm 20% còn 320, trả nợ còn 170 → mất 80/250 = 32% vốn; vay nhà 2 tỷ, lãi tăng 1 điểm = 20 triệu/năm (khoảng 1,7 triệu/tháng)\n\n"
      "Tra lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật anh Khoa, anh Tùng và Linh là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-21', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['Fed tăng lãi suất', 'lãi suất Mỹ', 'Nvidia', 'cổ phiếu AI', 'tỷ giá', 'DXY', 'VN-Index 2022', 'chứng khoán Việt Nam', 'kinh tế thế giới', 'vĩ mô'],
    bia_hook=['FED TĂNG LÃI', 'NHƯ 2022???'], badge='NĂM 2022 VN-INDEX GIẢM',
    bia_anh='Ho Chi Minh City Stock Exchange||Ho Chi Minh City skyline night',
    bia_hook_b=['VN-INDEX 2022', 'MẤT 32,8%'], badge_b='KHI MỸ TĂNG LÃI SUẤT',
    bia_hook_c=['KHẢ NĂNG TĂNG', 'TRÊN 80%???'], badge_c='HỌP NGÀY 8 VÀ 9/12',
    reel_hook='MỸ QUAY LẠI TĂNG LÃI SUẤT|NĂM 2022 CÓ LẶP LẠI???',
    fb_post=("Mỹ quay lại tăng lãi suất 🇺🇸\n\n👉 Khả năng Fed tăng tiếp tháng 12: trên 80%\n👉 Nvidia giảm 6 tuần liền, đô la mạnh nhất từ 4/2025\n"
             "👉 Năm 2022, Fed tăng 7 lần và VN-Index mất 32,8%\n\nNếu cổ phiếu giảm 20% và lãi vay tăng 1 điểm, nhà anh chị có phải bán gấp không?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: Mỹ quay lại tăng lãi suất, năm 2022 có lặp lại (NV1 16/11/2026).\n"
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
