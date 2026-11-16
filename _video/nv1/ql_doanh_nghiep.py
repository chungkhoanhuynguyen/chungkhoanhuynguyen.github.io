# -*- coding: utf-8 -*-
# NV1 17/11/2026 01:30 – VIDEO DÀI kênh chính, "câu hỏi lớn": 182.000 doanh nghiệp rút lui trong 10 tháng – mỗi ngày gần 600 công ty; kinh tế có đang "bệnh"? việc làm, thu nhập của anh chị ra sao?
# Lý do chọn: data/view/xu_huong.md tuần tới 16/11: "182.000 Doanh Nghiệp Rời Cuộc Chơi: Kinh Tế Việt Đang Có Điều Gì Bất Thường?" (VỰA TIN) ~131 nghìn view – top 4 tuần;
#   "KINH TẾ 2026: NỢ XẤU PHÌNH TO, NGƯỜI DÂN CẠN TIỀN" ~46 nghìn. Chủ đề NỖI SỢ + TIỀN TÚI NGƯỜI THƯỜNG (việc làm). Kênh mình 7 ngày chưa làm doanh nghiệp/việc làm.
#   Không chép đối thủ: góc riêng = "cú lật" con số (vào vẫn nhiều hơn ra; giải thể gấp đôi phần lớn là dọn hồ sơ tồn đọng) + áp lực thật dồn vào doanh nghiệp nhỏ và người làm ở đó.
# Nguồn (WiData hết credit tới 20/11 → số từ báo, ghi đủ tên báo + ngày):
#  - Thị trường Tài chính Tiền tệ 3/11/2026 (Cục Thống kê công bố 3/11): 10 tháng 2026 thành lập mới gần 162,3 nghìn (−0,4%); vốn đăng ký 2.138,8 nghìn tỷ (+34,3%);
#    lao động đăng ký 799,4 nghìn (−17,4%); vốn bình quân 13,2 tỷ/DN (+34,8%); quay lại hoạt động gần 81,4 nghìn (−12,5%); mới + quay lại hơn 243,6 nghìn (−4,8%);
#    tạm ngừng có thời hạn gần 92,0 nghìn (−12,7%); ngừng chờ giải thể hơn 33,7 nghìn (−42,3%); hoàn tất giải thể gần 56,3 nghìn (+109,8%);
#    bình quân mỗi tháng 24,4 nghìn vào, 18,2 nghìn rút lui. Tháng 10: thành lập mới gần 12,6 nghìn (−29,9% so cùng kỳ).
#  - Nhà đầu tư, đăng lại VCCI 9/11/2026 ("Phía sau làn sóng doanh nghiệp rời cuộc chơi"): giải thể 10 tháng theo ngành – bán buôn, bán lẻ, sửa chữa ô tô xe máy 21.673 (+120,1%);
#    chế biến chế tạo 6.085 (+107,1%); xây dựng 4.159 (+113,7%); kinh doanh BĐS 3.192 (+109,6%). Giám đốc Sở Tài chính Đà Nẵng: tạm ngừng chưa đồng nghĩa rời thị trường vĩnh viễn;
#    số giải thể chịu ảnh hưởng rà soát dữ liệu, xử lý hồ sơ tồn đọng, chiến dịch "Làm sạch mã số thuế" 2026. Phó Viện trưởng Viện Nghiên cứu phát triển TP.HCM: mức tăng giải thể
#    không hoàn toàn phản ánh sức khoẻ thực tế; áp lực thật: thiếu đơn hàng, sức mua yếu, chi phí logistics, lãi suất cao – tập trung ở doanh nghiệp nhỏ và vừa. (Không nêu tên người, chỉ chức danh.)
#  - VCCI 7/1/2025: cả năm 2024 tạm ngừng gần 100,1 nghìn; chờ giải thể gần 76,2 nghìn; hoàn tất giải thể hơn 21,6 nghìn; bình quân 16,5 nghìn DN rút lui mỗi tháng.
# Số tự tính: rút lui 10 tháng 2026 = 92,0 + 33,7 + 56,3 = 182,0 nghìn; 182.000/304 ngày ≈ 599 mỗi ngày ("gần 600");
#   vào (243,6) − ra (182,0) = 61,6 nghìn; giải thể 10 tháng 2025 ≈ 56,3/2,098 ≈ 26,8 nghìn; 2024 rút lui cả năm 100,1 + 76,2 + 21,6 = 197,9 nghìn.
#  - GIẢ ĐỊNH minh hoạ (anh Tuấn, kế toán dịch vụ): đầu năm 15 khách, nay 11; phí 2 triệu/khách/tháng → thu nhập dịch vụ 30 triệu còn 22 triệu (mất 8 triệu mỗi tháng).
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261117_0130'
KEY = 'CH2311DN'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
HA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
MT1 = 'ov:Ho Chi Minh City Metro Line 1||Ho Chi Minh City skyline night'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('KHÁCH HÀNG THỨ 4', 'GIẢI THỂ TRONG NĂM'), cols=CR, noti=dict(gio='08:05', ngay='Thứ Hai', items=[
        ('Email', 'Công ty Minh Phát', 'Thông báo giải thể, chấm dứt hợp đồng kế toán từ tháng 12', R_),
        ('Tin tức', 'Cục Thống kê', '10 tháng: gần 56.300 doanh nghiệp giải thể, gấp đôi cùng kỳ', V_),
        ('Zalo', 'Vợ', 'Đại lý xe chỗ em lại cắt thêm 2 người', X_)]),
      say=("Tám giờ sáng thứ Hai, anh Tuấn, kế toán dịch vụ ở Thành phố Hồ Chí Minh, nhận một email: công ty Minh Phát thông báo giải thể, chấm dứt hợp đồng kế toán từ tháng mười hai. "
           "Đây là khách hàng thứ tư của anh đóng cửa trong năm nay. Cùng lúc, vợ anh nhắn: đại lý xe máy chỗ em vừa cắt thêm hai người. "
           "Còn trên báo, một con số làm anh giật mình.")),
 dict(k='bignum', anh=TP, cap=('182.000 DOANH NGHIỆP', 'RÚT LUI TRONG 10 THÁNG'), cols=CR, value=182000, fmt='{:,.0f}', unit='', top='DOANH NGHIỆP RÚT LUI 10 THÁNG 2026', sub='gần 600 mỗi ngày – em tự tính từ số Cục Thống kê', col=RED,
      say=("Một trăm tám mươi hai nghìn. Đó là số doanh nghiệp rút lui khỏi thị trường trong mười tháng đầu năm nay, em cộng từ số liệu Cục Thống kê. "
           "Tính ra mỗi ngày gần sáu trăm công ty. Kinh tế tăng trưởng cao, vậy sao doanh nghiệp lại rời đi nhiều như thế? "
           "Và chuyện đó chạm vào việc làm, vào phiếu lương của anh chị như thế nào?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Con số 182.000 gồm những gì?', cap=('182.000 GỒM 3 NHÓM', 'KHÔNG PHẢI AI CŨNG ĐÓNG CỬA'), cols=CR, moc=True, giay=dict(tieu_de='DOANH NGHIỆP RÚT LUI 10 THÁNG 2026', so='Cục Thống kê, báo Thị trường Tài chính Tiền tệ 3/11/2026', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Tạm ngừng kinh doanh có thời hạn', '92.000'),
        ('Ngừng hoạt động, chờ giải thể', '33.700'),
        ('Hoàn tất giải thể', '56.300'),
        ('Cộng lại, em tự tính', '182.000')]),
      say=("Anh Tuấn là dân kế toán, nên anh mở bảng số gốc ra đọc kỹ. Một trăm tám mươi hai nghìn gồm ba nhóm. "
           "Chín mươi hai nghìn doanh nghiệp tạm ngừng kinh doanh có thời hạn. Ba mươi ba nghìn bảy trăm doanh nghiệp ngừng hoạt động, đang chờ làm thủ tục giải thể. "
           "Và năm mươi sáu nghìn ba trăm doanh nghiệp đã hoàn tất giải thể, tức là đóng cửa hẳn.")),
 dict(k='cards', anh=HN, cap=('NHÓM GIẢI THỂ', 'TĂNG GẤP ĐÔI'), cols=CR, moc=True,
      cards=[('92.000', 'Tạm ngừng, so cùng kỳ', 'Giảm 12,7%'), ('33.700', 'Chờ giải thể, so cùng kỳ', 'Giảm 42,3%'), ('56.300', 'Đã giải thể, so cùng kỳ', 'Tăng 109,8%')],
      say=("Nhưng điều lạ nằm ở cột so sánh. Số tạm ngừng giảm mười hai phẩy bảy phần trăm so với cùng kỳ. Số chờ giải thể giảm tới bốn mươi hai phẩy ba phần trăm. "
           "Chỉ riêng số đã giải thể tăng một trăm lẻ chín phẩy tám phần trăm, tức là gấp đôi. "
           "Nếu kinh tế đang tệ đi đều, lẽ ra cả ba nhóm phải cùng tăng. Vậy chuyện gì đang xảy ra?")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='noti', ch='Chương 2 – Cú lật: dọn sổ hay đổ vỡ?', cap=('NHIỀU CÔNG TY ĐÃ CHẾT TỪ LÂU', 'GIỜ MỚI LÀM GIẤY KHAI TỬ'), cols=CC, moc=True, noti=dict(gio='09:30', ngay='Thứ Hai', items=[
        ('Tin tức', 'Sở Tài chính', 'Tạm ngừng chưa đồng nghĩa rời thị trường vĩnh viễn', G_),
        ('Tin tức', 'Bộ Tài chính', 'Năm 2026: chiến dịch làm sạch mã số thuế', V_),
        ('Tin tức', 'Viện nghiên cứu', 'Nhiều doanh nghiệp ngừng hoạt động từ lâu, nay mới giải thể', X_)]),
      say=("Câu trả lời nằm trong lời giải thích của chính các cơ quan quản lý. Giám đốc Sở Tài chính Đà Nẵng cho biết số giải thể tăng mạnh có nguyên nhân từ việc rà soát dữ liệu và xử lý hồ sơ tồn đọng. Việc này gắn với chiến dịch làm sạch mã số thuế của Bộ Tài chính năm nay. "
           "Nhiều công ty đã ngừng hoạt động từ những năm trước, giờ mới hoàn tất thủ tục. "
           "Nói cách khác, có những doanh nghiệp đã chết từ lâu, năm nay mới làm giấy khai tử.")),
 dict(k='bignum', anh=TP, cap=('VÀO VẪN NHIỀU HƠN RA', 'HƠN 61.600 DOANH NGHIỆP'), cols=CC, moc=True, value=243600, fmt='{:,.0f}', unit='', top='MỚI THÀNH LẬP VÀ QUAY LẠI', sub='so với 182.000 rút lui – chênh 61.600, em tự tính', col=GREEN,
      say=("Và đây là cú lật thứ hai mà ít người nhắc tới. Cũng trong mười tháng đó, gần một trăm sáu mươi hai nghìn doanh nghiệp thành lập mới, thêm hơn tám mươi mốt nghìn doanh nghiệp quay lại hoạt động. "
           "Cộng lại hơn hai trăm bốn mươi ba nghìn. Tức là số vào thị trường vẫn nhiều hơn số rút lui khoảng sáu mươi mốt nghìn, em tự tính. "
           "Con số một trăm tám mươi hai nghìn là thật, nhưng nó chỉ là một nửa bức tranh.")),
 dict(k='chat', cap=('"VẬY LÀ KHÔNG SAO À ANH?"', '"CHƯA CHẮC"'), cols=CR, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='12:10', mau=G_, msgs=[
        ('Vợ', 'Vậy là kinh tế vẫn ổn hả anh?'),
        ('me', 'Tổng thì chưa đáng sợ, nhưng chưa chắc ổn với nhà mình'),
        ('Vợ', 'Sao vậy?'),
        ('me', 'Công ty nhỏ như khách của anh với đại lý chỗ em mới là chỗ đau')]),
      say=("Anh Tuấn gửi bảng số cho vợ. Chị hỏi: vậy là kinh tế vẫn ổn hả anh? Anh trả lời rằng nhìn tổng thì chưa đáng sợ, nhưng chưa chắc ổn với nhà mình. "
           "Vì những công ty nhỏ như khách hàng của anh, và đại lý xe máy chỗ vợ anh làm, mới là chỗ đang đau thật.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='bars', ch='Chương 3 – Ai đang đau thật?', anh=TP, cap=('GIẢI THỂ NHIỀU NHẤT', 'BÁN BUÔN, BÁN LẺ, XE CỘ'), cols=CR, moc=True,
      bars=[('Bán buôn, bán lẻ', 21673, R_, '21.673'), ('Chế biến, chế tạo', 6085, V_, '6.085'), ('Xây dựng', 4159, X_, '4.159')],
      say=("Nhìn theo ngành, nhóm giải thể nhiều nhất là bán buôn, bán lẻ và sửa chữa ô tô, xe máy. Có tới hai mươi mốt nghìn sáu trăm bảy mươi ba doanh nghiệp, tăng một trăm hai mươi phẩy một phần trăm. "
           "Tiếp theo là chế biến, chế tạo, khoảng sáu nghìn doanh nghiệp, và xây dựng, hơn bốn nghìn doanh nghiệp. "
           "Đây đều là những ngành dùng nhiều lao động, nhiều cửa hàng nhỏ, nhiều xưởng nhỏ.")),
 dict(k='giay', cap=('ÁP LỰC THẬT', 'DỒN VÀO DOANH NGHIỆP NHỎ'), cols=CR, moc=True, giay=dict(tieu_de='ÁP LỰC THẬT, THEO VIỆN NGHIÊN CỨU', so='Nhà đầu tư, đăng lại VCCI 9/11/2026', dau='GHI NHẬN', dieu=[
        ('Thiếu đơn hàng', 'ĐẦU RA'),
        ('Sức mua của người dân yếu', 'TIÊU DÙNG'),
        ('Chi phí vận chuyển tăng', 'CHI PHÍ'),
        ('Lãi suất vay còn cao', 'VỐN')]),
      say=("Phó Viện trưởng Viện Nghiên cứu phát triển Thành phố Hồ Chí Minh cho rằng mức tăng giải thể không hoàn toàn phản ánh sức khoẻ thật của doanh nghiệp. "
           "Áp lực thật nằm ở chỗ khác: thiếu đơn hàng, sức mua yếu, chi phí vận chuyển tăng và lãi suất vay còn cao. "
           "Và áp lực đó tập trung chủ yếu ở doanh nghiệp nhỏ và vừa.")),
 dict(k='cards', anh=HN, cap=('CÔNG TY TO LÊN', 'NHƯNG ÍT TUYỂN NGƯỜI HƠN'), cols=CR, moc=True,
      cards=[('13,2 tỷ', 'Vốn bình quân mỗi công ty mới', 'Tăng 34,8%'), ('799.400', 'Lao động đăng ký mới', 'Giảm 17,4%'), ('12.600', 'Công ty mới tháng 10', 'Giảm 29,9%')],
      say=("Còn một chi tiết nữa. Mỗi doanh nghiệp mới thành lập năm nay đăng ký vốn bình quân mười ba phẩy hai tỷ đồng, tăng ba mươi tư phẩy tám phần trăm. "
           "Nhưng số lao động đăng ký chỉ bảy trăm chín mươi chín nghìn bốn trăm người, giảm mười bảy phẩy bốn phần trăm. Riêng tháng mười, số công ty mới giảm gần ba mươi phần trăm so với cùng kỳ. "
           "Công ty mới to hơn, nhiều tiền hơn, nhưng tuyển ít người hơn.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='call', ch='Chương 4 – Lần trước: năm 2024', cap=('"NĂM 2024 ANH NHẬN', '20 BỘ HỒ SƠ GIẢI THỂ"'), cols=CR, moc=True, call=dict(ten='Anh Hải', phu='Gọi thoại', mau=V_, loi=[
        'Hồ sơ chờ giải thể từ năm 2024 vẫn còn đầy tủ',
        'Năm nay thủ tục nhanh hơn nên mới dồn một lúc']),
      say=("Anh Tuấn gọi cho anh Hải, đồng nghiệp làm dịch vụ giải thể doanh nghiệp. Anh Hải kể: hồ sơ chờ giải thể từ năm hai nghìn không trăm hai mươi tư vẫn còn đầy tủ. "
           "Năm nay thủ tục được đẩy nhanh, nên số giải thể mới dồn lên một lúc. Nhưng anh Hải cũng nói thêm: khách mới tìm đến năm nay phần lớn là cửa hàng nhỏ, không phải công ty ma.")),
 dict(k='giay', cap=('LẦN TRƯỚC: NĂM 2024', '76.200 CÔNG TY XẾP HÀNG CHỜ'), cols=CR, moc=True, giay=dict(tieu_de='DOANH NGHIỆP RÚT LUI CẢ NĂM 2024', so='Cục Thống kê, VCCI 7/1/2025', dau='ĐÃ XẢY RA', dieu=[
        ('Tạm ngừng kinh doanh có thời hạn', '100.100'),
        ('Ngừng hoạt động, chờ giải thể', '76.200'),
        ('Hoàn tất giải thể', '21.600'),
        ('Bình quân rút lui mỗi tháng', '16.500')]),
      say=("Số liệu năm hai nghìn không trăm hai mươi tư cho thấy đúng như vậy. Cả năm đó có khoảng một trăm nghìn doanh nghiệp tạm ngừng và bảy mươi sáu nghìn hai trăm doanh nghiệp ngừng hoạt động chờ giải thể. Nhưng chỉ hai mươi mốt nghìn sáu trăm doanh nghiệp hoàn tất giải thể. "
           "Bình quân, mỗi tháng có mười sáu nghìn năm trăm doanh nghiệp rút lui. Năm nay con số đó là mười tám nghìn hai trăm, cao hơn, nhưng không phải gấp đôi.")),
 dict(k='checklist', anh=TP, cap=('NĂM NAY VÀ NĂM 2024', 'GIỐNG 2, KHÁC 2'), cols=CR, moc=True,
      items=[('Giống: cửa hàng nhỏ đau nhất', R_), ('Giống: lãi vay, sức mua là gánh', R_), ('Khác: hồ sơ cũ được dọn', G_), ('Khác: công ty mới to hơn', V_)],
      say=("Đặt hai năm cạnh nhau, có hai điểm giống. Một: doanh nghiệp nhỏ, cửa hàng nhỏ vẫn chịu đòn nặng nhất. Hai: lãi vay và sức mua yếu vẫn là gánh nặng chính. "
           "Và hai điểm khác. Năm nay hồ sơ tồn đọng được dọn nhanh, nên số giải thể nhìn đáng sợ hơn thực tế. Và tiền đang dồn vào ít công ty hơn, to hơn. "
           "Nhìn chung, nền kinh tế chưa bệnh nặng. Nhưng chưa, không có nghĩa là không thể, nhất là với từng gia đình làm ở doanh nghiệp nhỏ.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='giay', ch='Chương 5 – Phiếu thu nhập của anh Tuấn', cap=('15 KHÁCH CÒN 11', 'MẤT 8 TRIỆU MỖI THÁNG'), cols=CR, moc=True, giay=dict(tieu_de='THU NHẬP DỊCH VỤ – ANH TUẤN', so='Em giả định để minh hoạ', dau='TỰ KÊ', dieu=[
        ('Đầu năm: 15 khách, 2 triệu mỗi khách', '30 TR'),
        ('Tháng 12: còn 11 khách', '22 TR'),
        ('Thu nhập mất mỗi tháng', '8 TR'),
        ('Quỹ dự phòng của nhà anh', '2 THÁNG')]),
      say=("Anh Tuấn mở sổ thu nhập, số này em giả định để minh hoạ. Đầu năm anh làm sổ sách cho mười lăm công ty nhỏ, mỗi công ty trả hai triệu đồng mỗi tháng, tổng ba mươi triệu. "
           "Từ tháng mười hai, chỉ còn mười một khách, thu nhập còn hai mươi hai triệu. Mất tám triệu đồng mỗi tháng. "
           "Điều làm anh lo nhất là dòng cuối: tiền dự phòng của cả nhà chỉ đủ sống hai tháng.")),
 dict(k='cards', anh=HA, cap=('BA CÁCH CỦA ANH TUẤN', 'KHI KHÁCH NHỎ BIẾN MẤT'), cols=CC, moc=True,
      cards=[('Giữ nguyên', 'Chờ khách nhỏ quay lại', 'Thu nhập giảm dần'), ('Học thêm', 'Phần mềm, hoá đơn điện tử', 'Nhận khách lớn hơn'), ('Thêm 1 nguồn', 'Vợ học bán hàng trên mạng', 'Không phụ thuộc 1 chỗ')],
      say=("Hai vợ chồng ngồi viết ra ba cách. Một: giữ nguyên, chờ khách nhỏ quay lại. Cách này dễ, nhưng thu nhập có thể giảm dần. "
           "Hai: anh học thêm phần mềm kế toán và hoá đơn điện tử để nhận những công ty mới, to hơn, đang cần sổ sách bài bản. "
           "Ba: vợ anh tìm thêm một nguồn thu, để nhà mình không phụ thuộc vào một chỗ làm duy nhất.")),
 dict(k='chat', cap=('KẾ HOẠCH NHÀ ANH TUẤN', 'QUỸ DỰ PHÒNG 6 THÁNG'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:15', mau=G_, msgs=[
        ('me', 'Tháng này anh đăng ký lớp hoá đơn điện tử'),
        ('Vợ', 'Còn em cắt bớt chi tiêu, để dành đủ 6 tháng'),
        ('me', 'Chưa đổi xe, chưa vay gì thêm nhé')]),
      say=("Tối đó anh Tuấn nhắn vợ: tháng này anh đăng ký lớp hoá đơn điện tử. Vợ anh đáp: còn em cắt bớt chi tiêu, để dành cho đủ sáu tháng sinh hoạt. "
           "Anh nhắn thêm: nhà mình chưa đổi xe, chưa vay gì thêm. Khi doanh nghiệp nhỏ chao đảo, người làm công cần một tấm đệm trước khi cần một cơ hội.")),
 dict(k='checklist', anh=HA, cap=('PHÉP THỬ CỦA ANH CHỊ', 'TIỀN DỰ PHÒNG ĐỦ MẤY THÁNG?'), cols=CC, moc=True,
      items=[('Dưới 3 tháng: rất mỏng', R_), ('3 đến 6 tháng: tạm ổn', V_), ('Trên 6 tháng: vững', G_)],
      say=("Và đây là phép thử anh chị tự làm được tối nay. Lấy số tiền mặt và tiết kiệm có thể rút ngay, chia cho chi tiêu một tháng của cả nhà. "
           "Dưới ba tháng là tấm đệm rất mỏng, chỉ một lần mất việc là phải vay. Từ ba đến sáu tháng là tạm ổn. Trên sáu tháng, anh chị vững hơn phần lớn các gia đình. "
           "Đây là mốc em đặt để tự soi, không phải quy định.")),
 dict(k='checklist', ch='Chương 6 – Theo dõi gì để biết sớm?', anh=TP, cap=('3 CON SỐ CẦN THEO DÕI', 'MỖI ĐẦU THÁNG'), cols=CC, moc=True,
      items=[('Số công ty mới so cùng kỳ', V_), ('Số tạm ngừng có tăng lại?', R_), ('Lao động đăng ký mới', V_)],
      say=("Muốn biết sớm kinh tế đang khoẻ lên hay yếu đi, em gợi ý theo dõi ba con số Cục Thống kê công bố đầu mỗi tháng. "
           "Một: số công ty thành lập mới so với cùng kỳ, tháng mười đang giảm gần ba mươi phần trăm. Hai: số tạm ngừng kinh doanh có tăng trở lại không, vì đó mới là nhóm phản ánh khó khăn mới. "
           "Ba: số lao động đăng ký mới. Còn sức khoẻ thật của các doanh nghiệp lớn trên sàn, lợi nhuận từng quý của hơn bốn trăm mã có miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn của khách hàng cũ', cap=('"CẢM ƠN ANH NHỮNG NĂM QUA', 'KHI NÀO MỞ LẠI EM GỌI"'), cols=CC, moc=True, chat=dict(ten='Chị Mai (Minh Phát)', tv='Đang hoạt động', gio='23:00', mau=V_, msgs=[
        ('Chị Mai (Minh Phát)', 'Cảm ơn anh những năm qua đã giữ sổ sách cho em'),
        ('Chị Mai (Minh Phát)', 'Khi nào mở lại, em gọi anh đầu tiên'),
        ('me', 'Chúc chị sớm làm lại. Tôi vẫn ở đây')]),
      say=("Gần nửa đêm, chị Mai, chủ công ty Minh Phát, nhắn: cảm ơn anh suốt những năm qua đã giữ sổ sách cho em, khi nào mở lại, em gọi anh đầu tiên. "
           "Anh Tuấn chúc chị sớm làm lại. Con số một trăm tám mươi hai nghìn ấy còn hơn một con số. Đằng sau mỗi doanh nghiệp rút lui là những người mất một nguồn thu nhập, và cũng là những người có thể quay lại.")),
 dict(k='end', cap=('182.000 DOANH NGHIỆP RÚT LUI', 'NHÀ MÌNH ĐỦ MẤY THÁNG?'), cols=CC,
      say=("Còn anh chị thì sao: quỹ dự phòng của nhà mình đủ sống dưới ba tháng, từ ba đến sáu tháng, hay trên sáu tháng? Và chỗ anh chị làm, năm nay có thấy khách hàng, đơn hàng ít đi không? "
           "Kể cho em và mọi người ở phần bình luận nhé. Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = '182.000 Doanh Nghiệp Rút Lui Trong 10 Tháng: Gần 600 Công Ty Mỗi Ngày – Việc Làm Anh Chị Ra Sao?'
MT = ("10 tháng năm 2026: 182.000 doanh nghiệp rút lui khỏi thị trường, gần 600 mỗi ngày; số giải thể tăng 109,8%. Nhưng cũng trong 10 tháng, hơn 243.600 doanh nghiệp thành lập mới và quay lại. "
      "Con số đáng sợ nói thật điều gì, ai đang đau thật, và phép thử quỹ dự phòng cho chính gia đình anh chị. Câu chuyện của anh Tuấn, kế toán dịch vụ có khách hàng thứ tư giải thể trong năm.\n\n"
      "Nguồn số liệu:\n"
      "• Cục Thống kê, báo Thị trường Tài chính Tiền tệ 3/11/2026: 10 tháng 2026 thành lập mới gần 162,3 nghìn (−0,4%), vốn bình quân 13,2 tỷ (+34,8%), lao động đăng ký 799,4 nghìn (−17,4%); quay lại gần 81,4 nghìn; mới + quay lại hơn 243,6 nghìn; "
      "tạm ngừng gần 92,0 nghìn (−12,7%); chờ giải thể hơn 33,7 nghìn (−42,3%); hoàn tất giải thể gần 56,3 nghìn (+109,8%); bình quân 18,2 nghìn rút lui mỗi tháng; tháng 10 thành lập mới gần 12,6 nghìn (−29,9% so cùng kỳ)\n"
      "• Nhà đầu tư / VCCI 9/11/2026: giải thể theo ngành – bán buôn, bán lẻ, sửa chữa ô tô xe máy 21.673 (+120,1%); chế biến chế tạo 6.085 (+107,1%); xây dựng 4.159 (+113,7%); "
      "ý kiến Giám đốc Sở Tài chính Đà Nẵng (rà soát dữ liệu, hồ sơ tồn đọng, chiến dịch làm sạch mã số thuế 2026) và Phó Viện trưởng Viện Nghiên cứu phát triển TP.HCM (thiếu đơn hàng, sức mua yếu, chi phí logistics, lãi suất cao; tập trung ở doanh nghiệp nhỏ và vừa)\n"
      "• VCCI 7/1/2025: năm 2024 tạm ngừng gần 100,1 nghìn, chờ giải thể gần 76,2 nghìn, giải thể hơn 21,6 nghìn; bình quân 16,5 nghìn rút lui mỗi tháng\n"
      "• Em tự tính: 92,0 + 33,7 + 56,3 = 182,0 nghìn; 182.000 / 304 ngày ≈ 599 mỗi ngày; vào 243,6 − ra 182,0 = 61,6 nghìn\n"
      "• Thu nhập anh Tuấn là giả định minh hoạ: 15 khách × 2 triệu = 30 triệu/tháng; còn 11 khách = 22 triệu → mất 8 triệu mỗi tháng\n\n"
      "Tra lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật anh Tuấn, anh Hải, chị Mai và công ty Minh Phát là hư cấu; số liệu là thật.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-23', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['doanh nghiệp giải thể', 'doanh nghiệp rút lui', 'kinh tế Việt Nam', 'việc làm', 'thất nghiệp', 'Cục Thống kê', 'tài chính cá nhân', 'quỹ dự phòng', 'vĩ mô', 'kinh tế 2026'],
    bia_hook=['182.000 CÔNG TY', 'RÚT LUI???'], badge='10 THÁNG ĐẦU NĂM 2026',
    bia_anh='Ho Chi Minh City skyline night||Hanoi skyline night',
    bia_hook_b=['MỖI NGÀY', 'GẦN 600 CÔNG TY'], badge_b='RÚT KHỎI THỊ TRƯỜNG',
    bia_hook_c=['GIẢI THỂ', 'GẤP ĐÔI???'], badge_c='VÀO VẪN NHIỀU HƠN RA',
    reel_hook='182.000 DOANH NGHIỆP RÚT LUI|KINH TẾ ĐANG BỆNH???',
    fb_post=("182.000 doanh nghiệp rút lui trong 10 tháng 🏢\n\n👉 Gần 600 công ty mỗi ngày, số giải thể gấp đôi cùng kỳ\n👉 Nhưng hơn 243.600 doanh nghiệp thành lập mới và quay lại\n"
             "👉 Đau thật nhất: cửa hàng nhỏ, bán buôn bán lẻ, xe cộ\n\nQuỹ dự phòng nhà anh chị đủ sống mấy tháng?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: 182.000 doanh nghiệp rút lui trong 10 tháng (NV1 17/11/2026).\n"
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
