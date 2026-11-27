# -*- coding: utf-8 -*-
# NV1 28/11/2026 00:36 – VIDEO DÀI kênh chính, cụm "VIỆT NAM – MỸ" (kho cum_my_viet_2711: đề "Mỹ muốn Việt Nam mua gì – máy bay, nông sản, LNG"; công thức huong_noi_dung_2711: 2 con số thật đối lập "Bán 159 tỷ – Mua 19 tỷ???").
# Lý do chọn: CH2511MY "Mỹ cử đoàn nông nghiệp… bán 8 đồng mới mua 1" top kênh tuần (+126 tuần, 215 view 27/11); USTR đề xuất thuế tới 35% (25/11) đang nóng;
#   khác góc CH2711TQ (QL1 – thuế 35% & VN-Index 4/2025): video này hỏi MUA GÌ để cân, mua thêm đã thử chưa, ai bán, và túi tiền người làm xưởng.
# Nguồn (đã mở 27–28/11/2026):
#  - WiData bảng 64 (NK chi tiết mặt hàng theo quốc gia), luỹ kế 10 tháng 2026, nhập từ Hoa Kỳ: tổng 19.273,88 triệu USD; máy vi tính, điện tử, linh kiện 5.877,24;
#    bông 1.524,47; máy móc thiết bị 1.478,64; chất dẻo 965,44; thức ăn gia súc 747,81; rau quả 746,52; đậu tương 456,35.
#  - WiData bảng 87 (XK chi tiết), luỹ kế 10 tháng 2026, sang Hoa Kỳ: máy vi tính, điện tử, linh kiện 53.486,68; máy móc 26.251,53; dệt may 15.358,83;
#    điện thoại 10.167,38; giày dép 7.923,45; gỗ và sản phẩm gỗ 7.577,61.
#  - Báo Đầu tư qua VCCI 4/11/2026: 10 tháng 2026 xuất khẩu sang Mỹ 159,40 tỷ USD, tăng 26,2% (QL1 đã mở 25/11, ghi trong ql_thue35.py).
#  - USTR thông cáo 25/11/2026 (QL1 đã mở): Việt Nam – xem xét thuế tới 35%, 20% nếu đạt thoả thuận; nêu dệt may, da giày, đóng tàu, xi măng, ICT; góp ý đến 5/1/2027; điều trần từ 25/1/2027.
#  - VCCI 9/6/2025: đoàn Việt Nam sang Mỹ (2–6/6/2025) ký 20 biên bản ghi nhớ nhập nông sản Mỹ, tổng tới 3 tỷ USD.
#  - Reuters 19/2/2026 (qua AOL): 3 hãng bay Việt ký mua 90 máy bay Boeing; Vietnam Airlines 50 chiếc 737-8, 8,1 tỷ USD, giao 2030–2032; Sun PhuQuoc Airways 40 chiếc 787-9, 22,5 tỷ USD.
#  - VnExpress 29/4/2025: Thủ tướng – Việt Nam cần mua thêm hàng Mỹ, gồm khí hoá lỏng LNG, máy bay, thuốc.
#  - VietnamPlus 7/11/2026: đoàn xúc tiến nông nghiệp lớn nhất của Mỹ (43 doanh nghiệp, 37 tổ chức) tới TP.HCM 9–12/11/2026; nông sản Mỹ vào Việt Nam năm 2025 gần 5,6 tỷ USD, +38%.
#  - Nhân Dân 10/6/2026 (đã mở 28/11): Mỹ là thị trường xuất khẩu lớn nhất của Việt Nam.
#  - Bán tăng 26,2%: 159,40 ÷ 1,262 = 126,31 → tăng ≈ 33,1 tỷ, lớn hơn cả tổng mua của Mỹ 19,27 tỷ → con số chênh lớn lên.
#  - Quasa 14/10/2026 (họp báo Cục Thống kê 7/10/2026): 9 tháng 2026 khu vực có vốn nước ngoài (kể cả dầu thô) xuất khẩu 350,41 tỷ USD, chiếm 80,7% xuất khẩu cả nước.
# Số tự tính: 159,40 − 19,27 = 140,13 tỷ USD; 159,40 ÷ 19,27 = 8,27 lần; 8,1 + 22,5 = 30,6 tỷ USD (90 máy bay); 30,6 ÷ 140,13 = 21,8%;
#   dệt may 15,36 ÷ bông 1,52 = 10,1 lần; dệt may + giày dép + gỗ = 15,36 + 7,92 + 7,58 = 30,86 tỷ USD.
#   Bảng thu nhập nhà Cường là VÍ DỤ GIẢ ĐỊNH: Hạnh lương 8,5 triệu + tăng ca 2,5 triệu; Cường 13 triệu → 24 triệu/tháng; mất tăng ca = 2,5 triệu/tháng = 30 triệu/năm;
#   phần đi qua đơn hàng Mỹ: 11 ÷ 24 = 45,8%.
# Không nêu mức thuế Mỹ đang áp hiện hành (nguồn 2026 vênh nhau: 12,5% Mục 301 từ 24/7, 19%/20% trước đó). Không nêu số lao động ngành (chưa có nguồn mở được).
# Cường, Hùng (dàn cố định), chị Hạnh là nhân vật hư cấu. Không dự đoán, không hô mua bán.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw')
sys.path.insert(0, CW + '/_video'); from phat_am import doc as phat_am_doc
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = CW + '/_video/queue/20261128_0100'
KEY = 'CH0112MM'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HCM = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline'
HN = 'ov:Hanoi skyline night||Hanoi skyline'
TAU = 'ov:Container ship||Ho Chi Minh City skyline'
CF_L = ([-28.25, 0.15, 5.2], [-27.15, 0.15, 5.2])
CAM_CF = {'from': [[-27.4, 1.5, 2.3], [-27.7, 0.8, 5.2], 42], 'to': [[-27.6, 1.42, 3.0], [-27.7, 0.8, 5.2], 38]}
CAM_VP = {'from': [[0.9, 1.5, 4.4], [0.3, 1.3, -1.0], 44], 'to': [[0.6, 1.45, 3.4], [0.2, 1.35, -1.2], 39]}

S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('BÁN 159 TỶ ĐÔ', 'MUA LẠI 19 TỶ???'), cols=CR, noti=dict(gio='07:10', ngay='Thứ Năm 26/11', items=[
        ('Tin tức', 'Thông cáo của Mỹ · 25/11/2026', 'Việt Nam: xem xét mức thuế tới 35%', R_),
        ('Zalo', 'Hạnh', 'Anh đọc tin thuế chưa? Chuyền em đang lo', V_)]),
      say=("Nhà anh chị có ai đang làm ở xưởng may, xưởng giày hay xưởng gỗ không? Nếu có, con số hôm nay liên quan thẳng đến lương tháng của người đó. "
           "Mười tháng đầu năm nay, Việt Nam bán sang Mỹ hơn một trăm năm mươi chín tỷ đô la hàng hoá. Còn mua lại của Mỹ, chỉ hơn mười chín tỷ. "
           "Và ngày hai mươi lăm tháng mười một, Mỹ đề xuất xem xét mức thuế tới ba mươi lăm phần trăm với hàng Việt Nam. "
           "Thuế này người Mỹ phải trả thêm khi mua hàng Việt. Hàng đắt lên thì họ dễ đặt ít đi, mà đơn ít thì xưởng cắt ca.")),
 dict(k='bignum', short=True, anh=TAU, cap=('BÁN RA GẤP 8 LẦN', 'MUA VÀO'), cols=CR,
      value=8.27, fmt='{:,.2f}', unit=' LẦN', top='VIỆT NAM VÀ MỸ, 10 THÁNG NĂM 2026 · EM TỰ TÍNH', sub='Bán 159,40 tỷ USD · mua 19,27 tỷ USD', col=R_,
      say=("Bán ra gấp hơn tám lần mua vào. Bán nhiều hơn mua hơn một trăm bốn mươi tỷ đô, trong video này em gọi đó là con số chênh. "
           "Người Mỹ nhìn con số chênh và hỏi: sao Việt Nam không mua hàng Mỹ nhiều hơn? Câu trả lời lại nằm trong lương tháng của rất nhiều gia đình Việt.")),
 dict(k='3d', set='cafevh', light='day', cam=CAM_CF, label='TỐI THỨ NĂM · QUÁN NƯỚC',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'dienthoai', 'ngoi': True, 'expr': 'worried'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'}],
      cap=('"MUA THÊM HÀNG MỸ', 'LÀ XONG CHỨ GÌ?"'), cols=CC,
      say=("Em, Huy Nguyễn, kể chuyện anh Cường, chị Hạnh vợ anh làm tổ trưởng một chuyền may ở Bình Dương, và anh Hùng lái xe container. Ba người hư cấu, số liệu là thật. "
           "Tối đó Cường đưa Hùng xem tin nhắn của vợ, rồi bảo: cứ mua thêm hàng Mỹ là xong chứ gì. Hùng chỉ cười: ông biết Mỹ bán gì cho mình chưa?")),
 dict(k='checklist', anh=TAU, cap=('BA CÂU HỎI', 'CỦA VIDEO NÀY'), cols=CC, moc=True,
      items=[('1. Mỹ bán gì cho Việt Nam?', V_), ('2. Mua thêm, đã thử chưa?', V_), ('3. Ai đang bán sang Mỹ?', R_)],
      say=("Vậy ta đi qua ba câu hỏi. Mỹ bán gì cho Việt Nam? Mua thêm, đã thử chưa? Và ai thật sự đang bán sang Mỹ?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Mỹ bán gì cho Việt Nam', cap=('HÀNG MỸ VÀO VIỆT NAM', '10 THÁNG: 19,27 TỶ ĐÔ'), cols=CC, moc=True, giay=dict(
        tieu_de='HÀNG MỸ VÀO VIỆT NAM, 10 THÁNG 2026', so='WiData · nhập khẩu theo mặt hàng và nước', dau='TỔNG 19,27 TỶ USD', dieu=[
        ('Linh kiện, máy tính, điện tử', '5,88 TỶ USD'),
        ('Bông các loại', '1,52 TỶ USD'),
        ('Máy móc, thiết bị', '1,48 TỶ USD'),
        ('Hạt nhựa nguyên liệu', '0,97 TỶ USD')]),
      say=("Câu thứ nhất, Mỹ bán gì cho ta. Mười tháng năm nay, nhiều nhất là linh kiện và hàng điện tử, gần sáu tỷ đô. "
           "Thứ hai là bông, hơn một tỷ rưỡi đô. Rồi đến máy móc thiết bị, và hạt nhựa nguyên liệu. Riêng bốn món này đã khoảng một nửa hàng Mỹ vào Việt Nam, phần lớn là đồ để sản xuất tiếp, không phải hàng bày trong siêu thị.")),
 dict(k='cards', anh=HCM, cap=('HÀNG MỸ', 'TRÊN MÂM CƠM NHÀ MÌNH'), cols=CC, moc=True,
      cards=[('748 TRIỆU USD', 'Thức ăn chăn nuôi', 'Dùng cho lợn, gà'), ('747 TRIỆU USD', 'Rau quả', 'Ví dụ: táo, nho'), ('456 TRIỆU USD', 'Đậu tương', 'Ép dầu, làm thức ăn')],
      say=("Phần đi vào bữa cơm thì nhỏ hơn nhiều: thức ăn chăn nuôi, rau quả, đậu tương, mỗi thứ chưa tới một tỷ đô trong mười tháng. "
           "Quả táo, chùm nho Mỹ ngoài chợ là cái người mua nhìn thấy, nhưng không phải phần lớn của câu chuyện.")),
 dict(k='chat', cap=('"BÔNG MỸ VÀO XƯỞNG', 'ÁO RA LẠI ĐI MỸ"'), cols=CC, moc=True, chat=dict(ten='Hạnh', tv='Đang hoạt động', gio='22:05', mau=V_, msgs=[
        ('Hạnh', 'Vải bên em nhiều lô dệt từ bông Mỹ'),
        ('Hạnh', 'May xong lại đóng thùng gửi sang Mỹ'),
        ('me', 'Vậy bông đi một vòng rồi về nhà nó à?'),
        ('Hạnh', 'Ừ, nhưng về dưới dạng cái áo')]),
      say=("Cường nhắn hỏi vợ. Chị Hạnh kể vải ở xưởng nhiều lô dệt từ bông Mỹ, may xong lại đóng thùng gửi sang Mỹ. "
           "Bông đi một vòng rồi về nhà nó, nhưng về dưới dạng cái áo.")),
 dict(k='bignum', short=True, anh=TAU, cap=('DỆT MAY BÁN SANG MỸ', 'GẤP 10 LẦN MUA BÔNG MỸ'), cols=CC,
      value=15.36, fmt='{:,.2f}', unit=' TỶ USD', top='HÀNG DỆT MAY BÁN SANG MỸ, 10 THÁNG 2026 · WIDATA', sub='Mua bông Mỹ cùng kỳ: 1,52 tỷ USD', col=V_,
      say=("Mười tháng năm nay, hàng dệt may Việt Nam bán sang Mỹ hơn mười lăm tỷ đô, gấp khoảng mười lần tiền mua bông Mỹ. "
           "Phần tiền hơn ra ấy gồm vải và phụ liệu mua từ nơi khác, và cả tiền công, điện nước, lương của những người như chị Hạnh. "
           "Giả sử mua bông Mỹ gấp đôi, thêm hơn một tỷ rưỡi đô, cũng chỉ khoảng một phẩy một phần trăm con số chênh.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='checklist', ch='Chương 2 – Mua thêm, đã thử chưa?', anh=HN, cap=('VIỆT NAM TỪNG NÓI', 'SẼ MUA THÊM GÌ?'), cols=CC, moc=True,
      items=[('Máy bay', V_), ('Khí hoá lỏng LNG', V_), ('Thuốc chữa bệnh', V_)],
      say=("Câu thứ hai, mua thêm đã thử chưa. Rồi. Từ tháng tư năm hai nghìn không trăm hai mươi lăm, Thủ tướng đã nói Việt Nam cần mua thêm hàng Mỹ, gồm máy bay, thuốc, và khí hoá lỏng. Khí hoá lỏng là loại khí đốt dùng nhiều để chạy nhà máy điện. "
           "Đó là những món đắt tiền mà Mỹ bán được.")),
 dict(k='giay', short=True, cap=('ĐÃ KÝ: 90 MÁY BAY', 'VÀ 3 TỶ ĐÔ NÔNG SẢN'), cols=CC, moc=True, giay=dict(
        tieu_de='NHỮNG LẦN KÝ MUA HÀNG MỸ', so='VCCI 9/6/2025 · Reuters 19/2/2026', dau='ĐÃ KÝ', dieu=[
        ('6/2025: 20 biên bản nông sản', 'TỚI 3 TỶ USD'),
        ('2/2026: Vietnam Airlines, 50 chiếc', '8,1 TỶ USD'),
        ('2/2026: Sun PhuQuoc Airways, 40 chiếc', '22,5 TỶ USD'),
        ('Vietnam Airlines nhận máy bay', '2030 ĐẾN 2032')]),
      say=("Tháng sáu năm ngoái, doanh nghiệp Việt sang Mỹ ký hai mươi biên bản ghi nhớ mua nông sản, tức là thoả thuận ý định mua, chưa phải hợp đồng giao hàng, tổng tới ba tỷ đô. "
           "Tháng hai năm nay, theo hãng tin Reuters, các hãng bay Việt ký mua chín mươi máy bay Boeing: Vietnam Airlines năm mươi chiếc, Sun PhuQuoc Airways bốn mươi chiếc, cộng lại hơn ba mươi tỷ đô. "
           "Nhưng có một dòng nhỏ: lô của Vietnam Airlines phải từ năm hai nghìn không trăm ba mươi mới bắt đầu giao. Máy bay về đến đâu mới tính là hàng nhập đến đó.")),
 dict(k='bignum', short=True, anh=HN, cap=('90 MÁY BAY', 'BẰNG 22% CON SỐ CHÊNH'), cols=CR,
      value=22, fmt='{:,.0f}', unit='%', top='HỢP ĐỒNG 30,6 TỶ USD, GIAO NHIỀU NĂM · CHÊNH 10 THÁNG 140,13 TỶ USD', sub='Em tự tính: 30,6 chia 140,13', col=R_,
      say=("Em đặt hai con số cạnh nhau. Giá trị hợp đồng chín mươi máy bay, giao trong nhiều năm, chỉ bằng khoảng hai mươi hai phần trăm con số chênh của riêng mười tháng năm nay. "
           "Mà con số chênh thì năm nào cũng có, còn máy bay thì không năm nào cũng mua.")),
 dict(k='bars', anh=TAU, cap=('ĐÃ KÝ MUA THÊM', 'BÁN SANG MỸ VẪN TĂNG 26,2%'), cols=CR, top='10 THÁNG 2026 (TỶ USD) · BÁO ĐẦU TƯ, WIDATA',
      bars=[('Bán sang Mỹ', 159.4, R_, '159,4'), ('Mua của Mỹ', 19.27, G_, '19,27')],
      say=("Ký mua thêm rồi, nhưng theo Báo Đầu tư, mười tháng năm nay hàng bán sang Mỹ vẫn tăng hơn hai mươi sáu phần trăm so với mười tháng năm ngoái. "
           "Con số chênh không tự nhỏ đi. Muốn hiểu vì sao, phải trả lời câu thứ ba: ai đang bán?")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='cards', ch='Chương 3 – Ai đang bán sang Mỹ?', anh=TAU, cap=('BA MÓN BÁN SANG MỸ', 'NHIỀU NHẤT'), cols=CC, moc=True,
      cards=[('53,49 TỶ USD', 'Máy tính, điện tử', 'Linh kiện'), ('26,25 TỶ USD', 'Máy móc, thiết bị', 'Phụ tùng'), ('15,36 TỶ USD', 'Dệt may', 'Quần áo, vải')],
      say=("Đứng đầu danh sách hàng bán sang Mỹ không phải quần áo, mà là máy tính, hàng điện tử và linh kiện, hơn năm mươi ba tỷ đô. "
           "Thứ hai là máy móc thiết bị, hơn hai mươi sáu tỷ. Dệt may mới đứng thứ ba.")),
 dict(k='bignum', short=True, anh=HCM, cap=('CẢ NƯỚC: VỐN NƯỚC NGOÀI', 'GIỮ 80,7% XUẤT KHẨU'), cols=CR,
      value=80.7, fmt='{:,.1f}', unit='%', top='XUẤT KHẨU CẢ NƯỚC 9 THÁNG 2026, KỂ CẢ DẦU THÔ · CỤC THỐNG KÊ', sub='Khu vực có vốn nước ngoài: 350,41 tỷ USD', col=R_,
      say=("Và đây là cú lật. Tính chung xuất khẩu cả nước chín tháng năm nay, theo Cục Thống kê, các doanh nghiệp có vốn nước ngoài chiếm gần tám mươi mốt phần trăm. "
           "Cứ mười đồng hàng Việt Nam bán ra nước ngoài, khoảng tám đồng do nhà máy của chủ nước ngoài làm ra. "
           "Hàng đi Mỹ nhiều nhất lại là điện tử, máy móc, đúng nhóm các tập đoàn nước ngoài làm nhiều. Nên rất có thể phần lớn con số chênh với Mỹ cũng đến từ họ. Tiền lãi phần lớn về túi chủ nhà máy, còn phần ở lại Việt Nam có tiền lương của người đứng máy.")),
 dict(k='chat', cap=('"VẬY THUẾ ĐÁNH VÀO', 'NHÀ MÁY NƯỚC NGOÀI À?"'), cols=CC, moc=True, chat=dict(ten='Hùng', tv='Đang hoạt động', gio='06:50', mau=V_, msgs=[
        ('me', 'Vậy thuế đánh chủ yếu vào nhà máy nước ngoài à?'),
        ('Hùng', 'Sổ sách là của họ'),
        ('Hùng', 'Nhưng người đứng máy là người Việt'),
        ('Hùng', 'Đơn hàng giảm thì ai bị cắt ca trước?')]),
      say=("Sáng hôm sau Cường nhắn hỏi Hùng: vậy thuế có đánh chủ yếu vào nhà máy nước ngoài không? Hùng trả lời một câu làm Cường im lặng: sổ sách là của họ, nhưng người đứng máy là người Việt. "
           "Đơn hàng giảm thì ai bị cắt ca trước?")),
 dict(k='noti', cap=('5 NHÓM NGÀNH BỊ NÊU TÊN', 'TRONG ĐỀ XUẤT CỦA MỸ'), cols=CR, moc=True, noti=dict(gio='07:15', ngay='Thứ Sáu 27/11', items=[
        ('Tin tức', 'Thông cáo của Mỹ · 25/11/2026', 'Nêu tên: dệt may, da giày, đóng tàu, xi măng, điện tử', R_),
        ('Tin tức', 'Thông cáo của Mỹ · 25/11/2026', 'Có thoả thuận: 20%. Góp ý đến 5/1/2027', V_)]),
      say=("Cường đọc kỹ thông cáo của cơ quan thương mại Mỹ. Năm nhóm ngành của Việt Nam bị nêu tên: dệt may, da giày, đóng tàu, xi măng, và điện tử công nghệ thông tin. "
           "Mức ba mươi lăm phần trăm mới là đề xuất, cao nhất có thể xem xét. Nếu hai nước đạt thoả thuận, mức được nêu là hai mươi phần trăm. Mỹ cho doanh nghiệp và các bên gửi ý kiến đến ngày năm tháng một năm sau.")),
 dict(k='checklist', short=True, anh=TAU, cap=('3 NGÀNH CẦN NHIỀU NHÂN CÔNG', 'TRONG HÀNG ĐI MỸ'), cols=CR, moc=True,
      items=[('Dệt may 15,36 tỷ: bị nêu tên', R_), ('Giày dép 7,92 tỷ: bị nêu tên', R_), ('Gỗ 7,58 tỷ: không bị nêu tên', V_)],
      say=("Còn đây là ba ngành cần nhiều nhân công trong hàng đi Mỹ. Dệt may hơn mười lăm tỷ đô và giày dép gần tám tỷ, cả hai đều có tên trong đề xuất. Gỗ và đồ gỗ hơn bảy tỷ rưỡi, không bị nêu tên. "
           "Nhà máy điện tử của tập đoàn lớn thường dễ chuyển dây chuyền sang nước khác hơn. Còn người đứng chuyền may, chuyền giày thì khó chuyển theo.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='call', ch='Chương 4 – Túi tiền nhà Cường', cap=('"THÁNG 12 VẪN ĐỦ ĐƠN', 'THÁNG 2 CHƯA CHỐT"'), cols=CR, moc=True, call=dict(ten='Hạnh', phu='Đang gọi', mau=V_, loi=[
        'Tháng 12 vẫn đủ đơn, tăng ca đều', 'Tháng 2 khách Mỹ chưa chốt']),
      say=("Trưa hôm đó chị Hạnh gọi về, kể rõ hơn. Tháng mười hai xưởng vẫn đủ đơn, vẫn tăng ca đều. Nhưng đơn tháng hai, khách Mỹ chưa chốt, họ bảo chờ xem thuế. "
           "Chưa ai mất việc cả. Nhưng khi đơn hàng chậm lại, tăng ca thường bị cắt trước.")),
 dict(k='giay', short=True, cap=('NHÀ CƯỜNG: 24 TRIỆU MỖI THÁNG', '11 TRIỆU NHỜ ĐƠN HÀNG MỸ'), cols=CR, moc=True, giay=dict(
        tieu_de='THU NHẬP NHÀ CƯỜNG (VÍ DỤ GIẢ ĐỊNH)', so='Mỗi tháng · em tự tính', dau='VÍ DỤ', dieu=[
        ('Lương chị Hạnh', '8,5 TRIỆU'),
        ('Tăng ca chị Hạnh', '2,5 TRIỆU'),
        ('Lương Cường, làm kho siêu thị', '13 TRIỆU'),
        ('Mất tăng ca: 2,5 nhân 12', 'HỤT 30 TRIỆU MỘT NĂM')]),
      say=("Em ngồi tính cùng Cường, số em giả định cho dễ hình dung. Chị Hạnh lương tám triệu rưỡi, cộng tăng ca hai triệu rưỡi, là mười một triệu mỗi tháng, em giả định toàn bộ nhờ đơn hàng Mỹ. "
           "Cường làm kho cho một siêu thị, mười ba triệu. Cả nhà hai mươi bốn triệu mỗi tháng, gần một nửa đi qua đơn hàng Mỹ. "
           "Chỉ cần mất tăng ca, mỗi năm hụt ba mươi triệu.")),
 dict(k='chat', cap=('"KHOAN VAY MUA XE', 'CHỜ CHỐT ĐƠN THÁNG 2"'), cols=CC, moc=True, chat=dict(ten='Hạnh', tv='Đang hoạt động', gio='21:30', mau=V_, msgs=[
        ('me', 'Định vay trả góp mua xe máy mới cho em đấy'),
        ('Hạnh', 'Khoan, chờ xưởng chốt đơn tháng 2 đã'),
        ('Hạnh', 'Tiền tăng ca tháng này để riêng ra'),
        ('me', 'Ừ, coi như tiền đó chưa phải của nhà')]),
      say=("Tối đó Cường định vay trả góp mua xe máy mới cho vợ. Chị Hạnh bảo khoan, chờ xưởng chốt đơn tháng hai đã, tiền tăng ca tháng này để riêng ra. "
           "Cường gật đầu: coi như khoản đó chưa phải của nhà, cho đến khi biết đơn hàng sau Tết.")),
 dict(k='cards', anh=HCM, cap=('3 VIỆC LÀM ĐƯỢC NGAY', 'KHÔNG CẦN ĐOÁN THUẾ'), cols=CC, moc=True,
      cards=[('6 THÁNG', 'Chi tiêu để dành sẵn', 'Trước khi tiêu tiền tăng ca'), ('0 KHOẢN', 'Vay mới chưa cần', 'Chờ đơn hàng chốt'), ('1 KỸ NĂNG', 'Học thêm nghề phụ', 'Không chỉ một xưởng')],
      say=("Không ai biết con số thuế cuối cùng là bao nhiêu, em cũng không đoán. Nhưng có ba việc nhà Cường làm được ngay. "
           "Một, tiền tăng ca tháng nào cất riêng tháng đó, cho đến khi để dành đủ sáu tháng chi tiêu. Hai, hoãn những khoản vay chưa thật cần cho đến khi đơn hàng chốt. "
           "Ba, người trong nhà học thêm một nghề phụ, để thu nhập không chỉ đi qua một cánh cửa.")),
 dict(k='3d', set='vanphong', light='day', cam=CAM_VP, label='SÁNG THỨ BẢY · VĂN PHÒNG',
      cast=[{'a': 'huy', 'p': [-0.7, 0, 0.5], 'act': 'chitay', 'side': -1, 'expr': 'smile'},
            {'a': 'cuong', 'p': [0.9, 0, 0.7], 'act': 'noi', 'side': -1, 'expr': 'worried'}],
      cap=('"VẤN ĐỀ KHÔNG PHẢI MỸ', 'MÀ LÀ MỘT CÁNH CỬA"'), cols=CC,
      say=("Sáng thứ Bảy, Cường ghé văn phòng em. Anh hỏi: vậy nhà anh có nên lo không? "
           "Em bảo: chuyện không nằm ở chỗ Mỹ tốt hay xấu. Theo báo Nhân Dân, Mỹ vẫn là thị trường xuất khẩu lớn nhất của Việt Nam. Chuyện nằm ở chỗ thu nhập nhà mình đi qua bao nhiêu cánh cửa.")),
 dict(k='checklist', ch='Phép thử một cánh cửa', cap=('THU NHẬP NHÀ MÌNH', 'ĐI QUA CỬA MỸ BAO NHIÊU?'), cols=CC, moc=True,
      items=[('Dưới 30%: chỉ cần theo dõi tin', G_), ('30 đến 60%: để dành, hoãn vay', V_), ('Trên 60%: không vay mới lúc này', R_)],
      say=("Em gửi anh chị một phép thử. Cộng tất cả thu nhập nhà mình mỗi tháng, rồi tính xem bao nhiêu phần trăm đến từ xưởng hay doanh nghiệp bán hàng sang Mỹ. "
           "Dưới ba mươi phần trăm, anh chị chỉ cần theo dõi tin. Từ ba mươi đến sáu mươi phần trăm, như nhà Cường, nên để dành đủ sáu tháng chi tiêu và hoãn khoản vay chưa cần. "
           "Trên sáu mươi phần trăm, đừng mở khoản vay mới nào cho đến khi con số thuế rõ ràng. Đây là mốc em tự đặt để soi, anh chị cân theo hoàn cảnh nhà mình.")),
 dict(k='cards', anh=HN, cap=('3 MỐC CẦN THEO DÕI', 'TỪ NAY ĐẾN TẾT'), cols=CC, moc=True,
      cards=[('5/1/2027', 'Hạn gửi góp ý', 'Cho đề xuất thuế'), ('25/1/2027', 'Mỹ họp nghe các bên', 'Trước khi chốt thuế'), ('MỖI THÁNG', 'Số bán sang Mỹ', 'Hải quan công bố')],
      say=("Và ba mốc nên đánh dấu trên lịch. Ngày năm tháng một, hạn gửi góp ý cho đề xuất. Ngày hai mươi lăm tháng một, Mỹ bắt đầu họp nghe các bên trình bày trước khi chốt thuế. "
           "Và mỗi đầu tháng, số hàng bán sang Mỹ do cơ quan hải quan công bố. Nó cho anh chị biết hàng thật đang đi ra sao, chắc hơn mọi lời đồn.")),
 # ---------------- KẾT ----------------
 dict(k='3d', ch='Kết', set='cafevh', light='day', cam=CAM_CF, label='QUÁN NƯỚC · CUỐI TUẦN',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'noi', 'ngoi': True, 'expr': 'relief'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'}],
      cap=('MUA THÊM HÀNG MỸ', 'KHÔNG CÂN ĐƯỢC TÚI NHÀ MÌNH'), cols=CC,
      say=("Cuối tuần, Cường bảo Hùng rằng hoá ra mua thêm hàng Mỹ là việc của cả nước. Còn việc của nhà Cường là đừng để mọi khoản thu đi qua một cánh cửa. "
           "Con số chênh hơn một trăm bốn mươi tỷ đô, không ai trong chúng ta cân được. Nhưng túi tiền nhà mình thì cân được.")),
 dict(k='cards', anh=HCM, cap=('SỐ LIỆU VĨ MÔ, TỶ GIÁ', 'EM ĐỂ SẴN TRÊN WEB'), cols=CC, moc=True,
      cards=[('Trên web', 'Thế giới và hàng hoá', 'Cập nhật mỗi ngày'), ('Miễn phí', 'Xem không cần đăng ký', 'Tỷ giá, lãi suất'), ('Tính vẫn rối?', 'Zalo 0365.188.286', 'Em tính cùng anh chị')],
      say=("Tỷ giá, lãi suất và số liệu thế giới em cập nhật mỗi ngày trên web chứng khoán Huy Nguyễn chấm com, xem miễn phí. "
           "Nếu nhà anh chị có người làm cho xưởng hàng xuất khẩu và muốn tính lại kế hoạch chi tiêu, vay mượn, cứ nhắn Zalo cho em. Em tính cùng, anh chị tự quyết.")),
 dict(k='end', cap=('NHÀ ANH CHỊ CÓ AI', 'LÀM XƯỞNG HÀNG ĐI MỸ?'), cols=CC,
      say=("Còn nhà anh chị, có bao nhiêu người đang làm cho xưởng hàng đi Mỹ? Không ai thì gõ số không, một người gõ số một, từ hai người trở lên gõ số hai. Em đọc hết.")),
]
import ql_post; S = ql_post.tach(S, max_tu=50)
for c in S: c['say'] = lib.doc(phat_am_doc(c['say']))
TIEU = 'Bán 159 Tỷ Đô, Mua Lại 19 Tỷ: Mỹ Muốn Việt Nam Mua Gì?'
MT = ("10 tháng 2026, Việt Nam bán sang Mỹ 159,40 tỷ USD hàng hoá nhưng chỉ mua lại 19,27 tỷ – gấp hơn 8 lần. Ngày 25/11, Mỹ đề xuất xem xét thuế tới 35% với hàng Việt Nam. "
      "Mỹ bán gì cho ta, mua thêm (90 máy bay, 3 tỷ USD nông sản) đã đủ cân chưa, ai thật sự đang bán sang Mỹ – và phép thử 'một cánh cửa' cho thu nhập nhà mình. "
      "Cường, Hùng, chị Hạnh là nhân vật hư cấu; số liệu là thật.\n\n"
      "Nguồn số liệu:\n"
      "• WiData (nhập khẩu theo mặt hàng và nước, luỹ kế 10 tháng 2026): nhập từ Hoa Kỳ 19,27 tỷ USD; máy vi tính, điện tử, linh kiện 5,88 tỷ; bông 1,52 tỷ; máy móc thiết bị 1,48 tỷ; chất dẻo nguyên liệu 0,97 tỷ; thức ăn gia súc 748 triệu; rau quả 747 triệu; đậu tương 456 triệu USD\n"
      "• WiData (xuất khẩu theo mặt hàng và nước, luỹ kế 10 tháng 2026), sang Hoa Kỳ: máy vi tính, điện tử, linh kiện 53,49 tỷ USD; máy móc thiết bị 26,25 tỷ; dệt may 15,36 tỷ; giày dép 7,92 tỷ; gỗ và sản phẩm gỗ 7,58 tỷ\n"
      "• Báo Đầu tư (VCCI) 4/11/2026: 10 tháng 2026 xuất khẩu sang Mỹ 159,40 tỷ USD, tăng 26,2%\n"
      "• Văn phòng Đại diện Thương mại Mỹ (USTR), thông cáo 25/11/2026: Việt Nam – xem xét thuế tới 35%, 20% nếu đạt thoả thuận; nêu dệt may, da giày, đóng tàu, xi măng, điện tử – công nghệ thông tin; góp ý đến 5/1/2027, điều trần từ 25/1/2027\n"
      "• VCCI 9/6/2025: doanh nghiệp Việt ký 20 biên bản ghi nhớ nhập nông sản Mỹ, tổng tới 3 tỷ USD\n"
      "• Reuters 19/2/2026: 3 hãng bay Việt ký mua 90 máy bay Boeing; Vietnam Airlines 50 chiếc 737-8 trị giá 8,1 tỷ USD, giao 2030–2032; Sun PhuQuoc Airways 40 chiếc 787-9 trị giá 22,5 tỷ USD\n"
      "• VnExpress 29/4/2025: Thủ tướng – Việt Nam cần mua thêm hàng Mỹ, gồm khí hoá lỏng LNG, máy bay, thuốc\n"
      "• Nhân Dân 10/6/2026: Mỹ là thị trường xuất khẩu lớn nhất của Việt Nam\n"
      "• Cục Thống kê (họp báo 7/10/2026, Quasa 14/10/2026): 9 tháng 2026 khu vực có vốn đầu tư nước ngoài (kể cả dầu thô) xuất khẩu 350,41 tỷ USD, chiếm 80,7% xuất khẩu cả nước\n"
      "• Em tự tính: 159,40 − 19,27 = 140,13 tỷ USD; 159,40 ÷ 19,27 = 8,27 lần; 8,1 + 22,5 = 30,6 tỷ USD; 30,6 ÷ 140,13 = 22%; 15,36 ÷ 1,52 = 10,1 lần; 15,36 + 7,92 + 7,58 = 30,86 tỷ USD. Mua bông Mỹ gấp đôi: thêm 1,52 tỷ = 1,1% của 140,13 tỷ. Thu nhập nhà Cường là ví dụ giả định (24 triệu/tháng; 8,5 + 2,5 = 11 triệu giả định toàn bộ nhờ đơn hàng Mỹ, 11 ÷ 24 ≈ 46%; mất tăng ca 2,5 × 12 = 30 triệu/năm).\n\n"
      "Số liệu vĩ mô, tỷ giá, lãi suất cập nhật mỗi ngày: https://chungkhoanhuynguyen.com/the-gioi-hang-hoa.html\n"
      "Cần tính lại kế hoạch chi tiêu khi thu nhập phụ thuộc đơn hàng xuất khẩu: Zalo 0365.188.286")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Vĩ mô chạm túi tiền', ngay='2026-12-01', gio_goi_y='17:00', gio='17:00', nhac='lofi', can_duyet='anh Huy duyệt trước khi hẹn',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['thuế Mỹ 35%', 'Việt Nam Mỹ', 'xuất khẩu sang Mỹ', 'thặng dư thương mại', 'Mỹ muốn Việt Nam mua gì', 'máy bay Boeing', 'dệt may', 'đơn hàng xuất khẩu', 'kinh tế Việt Nam', 'thuế đối ứng'],
    bia_hook=['BÁN 159 TỶ', 'MUA 19 TỶ???'], badge='MỸ MUỐN TA MUA GÌ?', bia_anh='ov:Container ship||Ho Chi Minh City skyline night',
    bia_hook_b=['90 MÁY BAY', 'VẪN CHƯA ĐỦ'], badge_b='BẰNG 22% CON SỐ CHÊNH',
    bia_hook_c=['THUẾ TỚI 35%', 'CHẠM TÚI AI?'], badge_c='DỆT MAY, GIÀY, GỖ',
    reel_hook='BÁN 159 TỶ, MUA 19 TỶ|MỸ MUỐN TA MUA GÌ???',
    fb_post=("Bán sang Mỹ 159 tỷ đô, mua lại 19 tỷ – Mỹ muốn Việt Nam mua gì?\n"
             "👉 Hàng Mỹ vào Việt Nam nhiều nhất là linh kiện, bông, máy móc – không phải táo, nho\n👉 90 máy bay Boeing đã ký chỉ bằng 22% khoảng chênh 10 tháng\n👉 Khu vực vốn nước ngoài chiếm 80,7% xuất khẩu – nhưng người đứng chuyền là người Việt\n"
             "Phép thử: thu nhập nhà mình đi qua cửa Mỹ bao nhiêu phần trăm?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – Vĩ mô chạm túi tiền: MỸ MUỐN VIỆT NAM MUA GÌ (NV1 28/11/2026). Bán 159 – mua 19; mua thêm đã thử; ai đang bán; túi tiền người làm xưởng. 3 cảnh 3D.\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    exec(open(os.path.join(os.path.dirname(__file__), '_kiem_chung.py'), encoding='utf-8').read())
