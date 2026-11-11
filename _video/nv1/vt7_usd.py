# -*- coding: utf-8 -*-
# NV1 12/11/2026 – THỬ khuôn "Vì Sao Thật Tệ Khi…" trên kênh phụ @chungkhoanhuynguyen7 (Y3 Vĩ Mô Chứng Khoán Dễ Hiểu).
# Chỉ đạo tang_view_1111: mỗi kênh phụ thử 1 tập, QL1 đo 7 ngày. Chủ đề riêng kênh vĩ mô: tỷ giá / đô la tự do (nỗi sợ mất giá tiền đồng).
# Số thật (WiData): USD tự do bán ra, giá cuối tháng: 30/6/2025 26.480 · 31/10/2025 27.850 · 31/12/2025 26.820 · 30/1/2026 26.500 ·
#   31/3/2026 28.080 · 30/4 26.800 · 30/6 26.720 · 31/7 26.280 · 31/8 25.980 · 30/9 25.950 · 30/10 26.210 · 11/11/2026 25.890.
#   USD NHTM bán ra: 31/3/2026 26.357 · 11/11/2026 25.840. Chênh tự do − NH ngày 31/3: 1.723 đồng (6,5%, tự tính).
#   Tự tính: 1 tỷ / 28.080 = 35.612 USD; × 25.890 = 922,0 triệu (−78 triệu, −7,8%). Tiết kiệm VND 5,4%/năm × 225 ngày (31/3 → 11/11) = +33,3 triệu.
#   Đợt sốt trước: 31/10/2025 27.850 → 30/1/2026 26.500 (−4,8%).
# Tin: VnEconomy 10/8/2026 "Siết rửa tiền qua USDT, thu hẹp chênh lệch giá vàng: USD tự do lao dốc dưới 26.000 đồng";
#   VnEconomy 2/11/2026 "VND vào nhóm 3 đồng tiền châu Á tăng giá mạnh nhất so với USD"; VietnamFinance 2/11/2026 "USD liên tục lao dốc…".
# Pháp lý: Nghị định 88/2019/NĐ-CP – mua bán ngoại tệ tại tổ chức không được phép có thể bị phạt tiền và tịch thu ngoại tệ.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261112_0039_vt7'
KEY = 'VT7USD'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TIEN = 'ov:us dollar banknotes||dollar bills'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('1 TỶ ĐỔI ĐÔ LA', 'CÒN 922 TRIỆU'), cols=CR, noti=dict(gio='07:30', ngay='Thứ Tư', items=[
        ('Tỷ giá', 'Bảng giá hôm nay', 'USD tự do bán ra: 25.890 đồng', R_),
        ('Zalo', 'Anh Khoa', 'Đô xuống nữa rồi, em bán chưa?', V_)]),
      say=("Sáng mười một tháng mười một, bạn mở bảng tỷ giá: đô la tự do còn hai mươi lăm nghìn tám trăm chín mươi đồng. Bảy tháng trước, bạn mang một tỷ đồng tiền tiết kiệm ra tiệm vàng, đổi hết sang đô la ở giá hai mươi tám nghìn không trăm tám mươi. "
           "Giờ số đô la ấy, kể cả bán được đúng giá bán ra hôm nay, chỉ còn khoảng chín trăm hai mươi hai triệu. Và người rủ bạn đổi tiền hôm đó vừa nhắn: đô xuống nữa rồi, em bán chưa?")),
 dict(k='text', cap=('VÌ SAO THẬT TỆ KHI', 'ÔM ĐÔ LA LÚC AI CŨNG SỢ'), cols=CC, anh=TIEN,
      say=("Giữ đô la để phòng tiền đồng mất giá, nghe rất an toàn. Nhưng vì sao có người làm đúng như vậy mà mất gần tám mươi triệu chỉ trong bảy tháng, chưa kể phần lãi tiết kiệm bỏ lỡ? "
           "Câu chuyện hôm nay là giả định, nhưng mọi con số tỷ giá đều là số thật năm 2026.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Cơn sốt đô la', cap=('"TIỀN ĐỒNG SẮP MẤT GIÁ', 'ĐỔI HẾT ĐI EM"'), cols=CC, moc=True, chat=dict(ten='Anh Khoa', tv='Đang hoạt động', gio='21:10', mau=V_, msgs=[
        ('Anh Khoa', 'Đô tự do lên 28 nghìn rồi em'),
        ('Anh Khoa', 'Ngân hàng không bán cho mình đâu, ra tiệm quen anh'),
        ('me', 'Em có 1 tỷ gửi tiết kiệm, đổi hết luôn hả anh?'),
        ('Anh Khoa', 'Để tiền đồng là mất giá đấy, đổi sớm còn kịp')]),
      say=("Cuối tháng ba năm 2026, anh Khoa, anh rể của bạn, nhắn liên tục: đô tự do lên hai mươi tám nghìn rồi em. Ngân hàng không bán cho mình đâu, ra tiệm quen anh. "
           "Bạn hỏi: em có một tỷ gửi tiết kiệm, đổi hết luôn hả anh? Anh Khoa trả lời chắc nịch: để tiền đồng là mất giá đấy, đổi sớm còn kịp.")),
 dict(k='bignum', anh=TIEN, cap=('ĐÔ LA TỰ DO BÁN RA', 'CUỐI THÁNG 3/2026'), cols=CR, moc=True, value=28080, fmt='{:,.0f}', unit=' đồng', top='GIÁ 1 USD Ở THỊ TRƯỜNG TỰ DO', sub='Cao nhất các tháng gần đây', col=RED,
      say=("Con số anh Khoa nói là thật. Theo số liệu tổng hợp trên WiData, ngày ba mươi mốt tháng ba năm 2026, giá đô la tự do bán ra là hai mươi tám nghìn không trăm tám mươi đồng. Đó là mức cao nhất trong các tháng gần đây. "
           "Cả khu phố bàn chuyện tiền đồng mất giá. Không khí y như lúc cả xóm xếp hàng mua vàng. Mà đúng là vậy: giữa tháng ba năm đó, vàng miếng cũng lên đỉnh gần một trăm tám mươi lăm triệu đồng một lượng. "
           "Khi vàng sốt, người ta cần đô la tiền mặt, và giá đô ngoài chợ bị kéo lên theo.")),
 dict(k='cards', anh='ov:bank exchange rate board||currency exchange', cap=('CÙNG NGÀY 31/3/2026', 'GIÁ BÁN 1 USD'), cols=CR, moc=True,
      cards=[('26.357', 'Ngân hàng bán ra', 'đồng'), ('28.080', 'Thị trường tự do', 'đồng'), ('1.723', 'Bạn trả thêm mỗi đô', 'đắt hơn 6,5%')],
      say=("Nhưng có một chi tiết bạn bỏ qua. Cùng ngày hôm đó, giá ngân hàng bán ra chỉ hai mươi sáu nghìn ba trăm năm mươi bảy đồng. Tức là mỗi đô la ở tiệm, bạn đã trả thêm một nghìn bảy trăm hai mươi ba đồng, đắt hơn khoảng sáu phẩy năm phần trăm. "
           "Bạn chưa kịp lời đồng nào, đã thua ngay sáu phẩy năm phần trăm từ lúc cầm tờ đô la lên tay.")),
 dict(k='giay', cap=('TỜ GIẤY VIẾT TAY', 'Ở TIỆM QUEN'), cols=CR, moc=True, giay=dict(tieu_de='GIẤY GHI NHẬN ĐỔI TIỀN', so='Ngày 31/3/2026 – không hoá đơn, không con dấu', dau='ĐÃ GIAO', dieu=[
        ('Khách đưa: 1.000.000.000 đồng.', '1 TỶ'),
        ('Tỷ giá: 28.080 đồng một đô la.', '28.080'),
        ('Khách nhận: 35.612 đô la tiền mặt.', '35.612 USD')]),
      say=("Bạn đưa một tỷ đồng, nhận về ba mươi lăm nghìn sáu trăm mười hai đô la tiền mặt, kèm một tờ giấy viết tay. Không hoá đơn, không con dấu. "
           "Bạn cất xấp đô la vào két, thấy lòng nhẹ hẳn. Từ hôm nay, tiền đồng có mất giá thế nào cũng không còn liên quan đến mình nữa. Bạn nghĩ vậy.")),
 dict(k='chat', cap=('"GIỮ DÀI HẠN MÀ', 'LO GÌ ANH"'), cols=CC, chat=dict(ten='Chồng', tv='Đang hoạt động', gio='20:45', mau=X_, msgs=[
        ('Chồng', 'Đô ngoài tiệm còn 26.800 rồi em ơi'),
        ('me', 'Giữ dài hạn mà, lo gì anh'),
        ('Chồng', 'Thế còn tiền lãi sổ tiết kiệm em rút ra?'),
        ('me', 'Thôi, coi như phí bảo hiểm')]),
      say=("Cuối tháng tư, chồng bạn nhắn: đô ngoài tiệm còn hai mươi sáu nghìn tám trăm rồi em ơi. Bạn trả lời: giữ dài hạn mà, lo gì anh. "
           "Chồng hỏi tiếp: thế còn tiền lãi sổ tiết kiệm em rút ra? Bạn gõ một câu cho xong chuyện: thôi, coi như phí bảo hiểm. Bạn chưa biết, khoản phí bảo hiểm ấy sẽ đắt hơn bạn tưởng rất nhiều.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='bars', ch='Chương 2 – Cú quay đầu', anh=TIEN, cap=('ĐÔ LA TỰ DO BÁN RA', 'GIÁ CUỐI THÁNG, ĐỒNG'), cols=CR, moc=True,
      bars=[('3/2026', 28080, RED, '28.080'), ('4/2026', 26800, GOLD, '26.800'), ('7/2026', 26280, GOLD, '26.280'), ('8/2026', 25980, GREEN, '25.980'), ('11/11', 25890, GREEN, '25.890')],
      say=("Rồi đô la quay đầu. Cuối tháng tư, giá tự do còn hai mươi sáu nghìn tám trăm. Cuối tháng bảy, hai mươi sáu nghìn hai trăm tám mươi. Cuối tháng tám, xuống dưới hai mươi sáu nghìn. "
           "Đến ngày mười một tháng mười một, chỉ còn hai mươi lăm nghìn tám trăm chín mươi đồng. Từ đỉnh tháng ba, giảm khoảng bảy phẩy tám phần trăm.")),
 dict(k='noti', cap=('2 GIỜ SÁNG', 'MỞ BẢNG TỶ GIÁ'), cols=CR, noti=dict(gio='02:10', ngay='Thứ Bảy', items=[
        ('Tỷ giá', 'Cuối tháng 8/2026', 'USD tự do bán ra: 25.980 đồng', R_),
        ('Ghi chú', 'Máy tính', '35.612 × 25.980 = 925 triệu', R_)]),
      say=("Một đêm cuối tháng tám, hai giờ sáng, bạn không ngủ được. Bạn mở bảng tỷ giá: hai mươi lăm nghìn chín trăm tám mươi đồng. Bạn bấm máy tính: ba mươi lăm nghìn sáu trăm mười hai nhân hai mươi lăm nghìn chín trăm tám mươi, ra khoảng chín trăm hai mươi lăm triệu. "
           "Lần đầu tiên bạn nhìn thấy con số bảy mươi lăm triệu tiền lỗ, chỉ vì sợ tiền đồng mất giá.")),
 dict(k='noti', cap=('TIN TỨC', 'MÀ BẠN KHÔNG ĐỌC'), cols=CC, noti=dict(gio='12:00', ngay='Thứ Hai', items=[
        ('Tin tức', 'VnEconomy 10/8/2026', 'USD tự do lao dốc dưới 26.000 đồng', R_),
        ('Tin tức', 'VnEconomy 2/11/2026', 'VND vào nhóm 3 đồng tiền châu Á tăng giá mạnh nhất so với USD', G_)]),
      say=("Trong lúc bạn yên tâm giữ đô, báo chí vẫn đưa tin đều đặn. Tháng tám, VnEconomy viết: đô la tự do lao dốc xuống dưới hai mươi sáu nghìn đồng. "
           "Ngày hai tháng mười một, cũng VnEconomy: tiền đồng vào nhóm ba đồng tiền châu Á tăng giá mạnh nhất so với đô la. Thứ bạn sợ mất giá, lại là thứ tăng giá.")),
 dict(k='cards', anh='ov:bank exchange rate board||currency exchange', cap=('VÌ SAO TIỀN ĐỒNG', 'LẠI KHỎE LÊN?'), cols=CC, moc=True,
      cards=[('25.840', 'Ngân hàng bán ra 11/11/2026', 'đồng một đô la'), ('50', 'Chênh tự do với ngân hàng', 'đồng, từ 1.723 hồi tháng 3')],
      say=("Vì sao tiền đồng lại khỏe lên? Theo VnEconomy, một phần là do cơ quan chức năng siết các đường dây chuyển tiền qua tiền ảo. Chênh lệch giá vàng trong nước với thế giới cũng thu hẹp, nên nhu cầu đô la tiền mặt ngoài chợ giảm hẳn. "
           "Hôm nay, giá đô ngân hàng bán ra là hai mươi lăm nghìn tám trăm bốn mươi đồng, giá tự do chỉ cao hơn năm mươi đồng. Khoản chênh một nghìn bảy trăm đồng mà bạn trả hồi tháng ba gần như đã biến mất.")),
 dict(k='cards', anh=TIEN, cap=('1 TỶ ĐỔI ĐÔ NGÀY 31/3', 'ĐẾN NGÀY 11/11/2026'), cols=CR, moc=True,
      cards=[('922 triệu', 'Giá trị nếu bán đúng 25.890', 'mất khoảng 78 triệu'), ('+33 triệu', 'Nếu cứ để gửi tiết kiệm 5,4%', '225 ngày, tự tính'), ('111 triệu', 'Chênh giữa hai lựa chọn', 'tự tính')],
      say=("Làm phép tính. Ba mươi lăm nghìn sáu trăm mười hai đô la, nhân với hai mươi lăm nghìn tám trăm chín mươi, còn khoảng chín trăm hai mươi hai triệu đồng. Mà đó là giá bán ra, tiệm mua lại của bạn còn thấp hơn. "
           "Nếu bạn cứ để một tỷ trong sổ tiết kiệm lãi năm phẩy bốn phần trăm, sau hai trăm hai mươi lăm ngày bạn có thêm khoảng ba mươi ba triệu. Khoảng cách giữa hai lựa chọn là khoảng một trăm mười một triệu đồng.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='checklist', ch='Chương 3 – Vì sao người cẩn thận lại mua đúng đỉnh?', anh='ov:crowd queue shop||people waiting in line', cap=('3 CÁI BẪY', 'CỦA ĐÔ LA TỰ DO'), cols=CC, moc=True,
      items=[('Mua khi chênh với ngân hàng đang lớn nhất', RED), ('Tiền gửi đô la ở Việt Nam lãi 0%', RED), ('Không hoá đơn, không bảo vệ khi tranh chấp', RED)],
      say=("Vì sao một người cẩn thận như bạn lại mua đúng đỉnh? Bẫy thứ nhất: bạn mua đúng lúc chênh lệch giữa giá tự do và giá ngân hàng lớn nhất. Chênh lệch đó thường nới rộng khi người ta đổ xô mua đô, nhất là lúc giá vàng trong nước cao hơn thế giới nhiều. "
           "Bẫy thứ hai: giữ đô la ở Việt Nam gần như không sinh lời, vì lãi suất tiền gửi đô la tại ngân hàng là không phần trăm. Bẫy thứ ba: tờ giấy viết tay không bảo vệ bạn nếu có tranh chấp.")),
 dict(k='call', cap=('"ANH CŨNG KẸT', 'Ở GIÁ 28 NGHÌN"'), cols=CR, call=dict(ten='Anh Khoa', phu='Anh rể', mau=V_, loi=[
        'Anh cũng kẹt 20 nghìn đô ở giá 28 nghìn', 'Tưởng đô chỉ có lên']),
      say=("Bạn gọi cho anh Khoa. Đầu dây bên kia im một lúc rồi anh nói nhỏ: anh cũng kẹt hai mươi nghìn đô ở giá hai mươi tám nghìn. Anh tưởng đô chỉ có lên, ai ngờ tiền đồng lại khỏe thế. "
           "Không ai lừa ai cả. Hai người chỉ cùng làm theo nỗi sợ của cả khu phố.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='cards', ch='Chương 4 – Lịch sử từng lặp lại', anh=TIEN, cap=('ĐỢT SỐT TRƯỚC', 'ĐÔ LA TỰ DO BÁN RA'), cols=CR, moc=True,
      cards=[('27.850', 'Cuối tháng 10/2025', 'đồng'), ('26.500', 'Cuối tháng 1/2026', 'giảm khoảng 4,8%')],
      say=("Đây không phải lần đầu. Cuối tháng mười năm 2025, đô la tự do cũng sốt lên hai mươi bảy nghìn tám trăm năm mươi đồng. Ba tháng sau, cuối tháng một năm 2026, giá về hai mươi sáu nghìn rưỡi, giảm khoảng bốn phẩy tám phần trăm. "
           "Chỉ trong một năm, đô la tự do sốt hai lần, và cả hai lần, người mua lúc đang sốt đều phải chịu lỗ.")),
 dict(k='giay', cap=('ĐIỀU BẠN CHƯA BIẾT', 'VỀ ĐỔI TIỀN Ở TIỆM'), cols=CR, moc=True, giay=dict(tieu_de='NGHỊ ĐỊNH 88/2019/NĐ-CP', so='Xử phạt vi phạm hành chính trong lĩnh vực tiền tệ, ngân hàng', dau='QUY ĐỊNH', dieu=[
        ('Mua bán ngoại tệ tại nơi không được phép: có thể bị phạt tiền.', 'PHẠT TIỀN'),
        ('Số ngoại tệ vi phạm: có thể bị tịch thu.', 'TỊCH THU')]),
      say=("Và còn một rủi ro bạn chưa từng nghĩ tới. Theo Nghị định tám mươi tám năm 2019 của Chính phủ, mua bán ngoại tệ tại nơi không được phép có thể bị phạt tiền. Số ngoại tệ đó cũng có thể bị tịch thu. "
           "Nghĩa là xấp đô la trong két không chỉ mất giá, mà còn có thể mất trắng nếu không may bị kiểm tra.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Nếu thật sự cần đô la', anh='ov:bank counter customers||bank interior', cap=('LÀM LẠI TỪ ĐẦU', 'BẠN SẼ LÀM GÌ?'), cols=CC, moc=True,
      items=[('Chỉ đổi khi có nhu cầu thật: du học, chữa bệnh, trả nợ ngoại tệ', GREEN), ('Mua ở ngân hàng, theo giấy tờ hợp lệ', GREEN), ('Chia nhỏ nhiều lần, không dồn một lúc', GREEN), ('Còn lại: để tiền đồng sinh lời', GOLD)],
      say=("Nếu được làm lại, bạn sẽ làm khác. Chỉ đổi đô la khi có nhu cầu thật, như cho con đi du học, chữa bệnh hay trả khoản nợ bằng ngoại tệ. Khi đó, mua ở ngân hàng với giấy tờ hợp lệ, giá rẻ hơn và được pháp luật bảo vệ. "
           "Nếu nhu cầu còn xa, chia nhỏ ra mua nhiều lần thay vì dồn một lúc đúng đỉnh. Phần tiền không có nhu cầu đô la, để nó sinh lời bằng tiền đồng. "
           "Ví dụ, nếu năm sau con bạn đi du học và cần hai mươi nghìn đô, bạn có thể chia ra bốn quý, mỗi quý đổi năm nghìn đô ở ngân hàng. Giá lên hay xuống, bạn cũng chỉ mua được giá trung bình, chứ không bao giờ dồn hết vào đúng đỉnh.")),
 dict(k='text', cap=('NỖI SỢ', 'LÀ THỨ ĐẮT NHẤT'), cols=CC, anh='ov:man thinking window||man looking out window',
      say=("Bài học lớn nhất không nằm ở tỷ giá. Nó nằm ở việc bạn ra quyết định lúc cả khu phố đang sợ. Khi ai cũng muốn mua một thứ, người bán luôn là người có lợi. "
           "Giữ tiền đồng không phải lúc nào cũng đúng, giữ đô la cũng vậy. Thứ đắt nhất là quyết định vội vàng vì sợ.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối', cap=('"LẦN SAU', 'HỎI GIÁ NGÂN HÀNG TRƯỚC"'), cols=CC, moc=True, chat=dict(ten='Anh Khoa', tv='Đang hoạt động', gio='22:15', mau=V_, msgs=[
        ('me', 'Em giữ lại số đô đó, đợi nhà có việc cần thì dùng'),
        ('me', 'Lần sau mình hỏi giá ngân hàng trước anh nhé'),
        ('Anh Khoa', 'Ừ, và không đổi theo hội nữa')]),
      say=("Tối đó bạn nhắn anh Khoa: em giữ lại số đô đó, đợi nhà có việc cần thì dùng. Lần sau mình hỏi giá ngân hàng trước anh nhé. "
           "Anh Khoa gửi lại một dòng: ừ, và không đổi theo hội nữa.")),
 dict(k='end', cap=('BẠN TỪNG ĐỔI ĐÔ LA', 'LÚC ĐANG SỐT CHƯA?'), cols=CC,
      say=("Bạn hay người nhà đã từng đổi đô la lúc đang sốt chưa? Giờ đang lãi hay lỗ? Kể ở phần bình luận nhé, và gửi video này cho người đang định ôm đô la vì sợ.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vì Sao Thật Tệ Khi Ôm Đô La Lúc Ai Cũng Sợ: 1 Tỷ Đổi Ở Giá 28.080 Còn 922 Triệu Sau 7 Tháng'
MT = ("Cuối tháng 3/2026, đô la tự do lên 28.080 đồng, cả khu phố rủ nhau đổi tiền vì sợ tiền đồng mất giá. Bảy tháng sau, giá còn 25.890. Một tỷ đổi đúng đỉnh chỉ còn khoảng 922 triệu, trong khi để gửi tiết kiệm còn lãi thêm khoảng 33 triệu. Vì sao người cẩn thận lại mua đúng đỉnh?\n\n"
      "Câu chuyện giả định, tỷ giá là số thật (đồng/USD, giá cuối tháng – tổng hợp WiData):\n"
      "• USD tự do bán ra: 31/10/2025 27.850 · 30/1/2026 26.500 · 31/3/2026 28.080 · 30/4 26.800 · 31/7 26.280 · 31/8 25.980 · 11/11/2026 25.890\n"
      "• USD ngân hàng thương mại bán ra: 31/3/2026 26.357 · 11/11/2026 25.840\n"
      "• Tự tính: 1 tỷ / 28.080 = 35.612 USD; × 25.890 = 922 triệu (−7,8%); tiết kiệm 5,4%/năm trong 225 ngày = +33,3 triệu\n"
      "• Tin: VnEconomy 10/8/2026 (USD tự do lao dốc dưới 26.000 đồng); VnEconomy 2/11/2026 (VND vào nhóm 3 đồng tiền châu Á tăng giá mạnh nhất so với USD)\n"
      "• Nghị định 88/2019/NĐ-CP về xử phạt vi phạm hành chính lĩnh vực tiền tệ, ngân hàng\n\n"
      "Kênh chính: https://www.youtube.com/@chungkhoanhuynguyen\nTìm hiểu thêm: https://chungkhoanhuynguyen.com\n\n"
      "Nhân vật là hư cấu. Chia sẻ góc nhìn, không phải tư vấn tài chính.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen7', seri='Vì sao thật tệ khi…', ngay='2026-11-15', gio_goi_y='20:00', gio='20:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['tỷ giá', 'đô la tự do', 'giá USD hôm nay', 'USD giảm', 'có nên giữ đô la', 'tiền đồng mất giá', 'tỷ giá 2026', 'vì sao thật tệ khi'],
    bia_hook=['1 TỶ ĐỔI ĐÔ LA', 'CÒN 922 TRIỆU'], badge='VÌ SAO THẬT TỆ KHI…',
    bia_anh=TIEN,
    bia_hook_b=['ĐỔI ĐÚNG ĐỈNH', 'MẤT 78 TRIỆU'], badge_b='ĐÔ LA 2026',
    bia_hook_c=['SỢ MẤT GIÁ', 'RỒI SAO?'], badge_c='VÌ SAO THẬT TỆ KHI…',
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh phụ @chungkhoanhuynguyen7 – thử khuôn 'Vì sao thật tệ khi' – đô la tự do (NV1 12/11/2026).\n"
    "XH_BAN = True; NO_CTA = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q and 'bạn' not in q: print(q)
