# -*- coding: utf-8 -*-
# NV1 20/11/2026 01:00 – VIDEO DÀI kênh chính, "câu hỏi lớn về tiền": thuế thu nhập cá nhân năm nay dự kiến hụt gần 34.000 tỷ – ai được lợi nhiều nhất?
#   Khuôn "manh mối – suy luận" (3 chi tiết đầu phim, cuối phim ghép lại) + "so với lần trước" (mức giảm trừ 11 triệu đứng yên từ 7/2020).
# Lý do chọn: data/view/xu_huong.md tuần tới 19/11 – "Người giàu coi thuế là đặc ân" ~70 nghìn (tuần trước) / CEO Nvidia "đóng 8 tỷ USD thuế là đặc quyền";
#   chủ đề TIỀN TÚI NGƯỜI THƯỜNG (phiếu lương) + con số lớn (34.000 tỷ). 7 ngày qua chưa làm thuế/ngân sách. Không trùng CH2011VON (vốn 38,5 triệu tỷ), CH1611GDP (lương).
#   Cú lật: giảm thuế tính theo SỐ TIỀN thì người thu nhập cao được nhiều nhất (110 triệu bớt 5,95 triệu/tháng), tính theo % thì người thu nhập vừa (27 triệu bớt 73%),
#   còn người có thu nhập quanh mức bình quân (9,18 triệu) vốn không nộp thuế nên không được gì; và lần trước mức giảm trừ đứng yên 5,5 năm trong lúc thu nhập +58,6%.
# Nguồn:
#  - VnExpress 23/10/2026 (Bộ Tài chính, công khai dự toán): thu thuế TNCN 2026 ước 203.200 tỷ, thấp hơn dự toán 33.800 tỷ (14,3%), thấp hơn năm ngoái 13,6%;
#    nguyên nhân: nâng giảm trừ gia cảnh, biểu lũy tiến 7 xuống 5 bậc, kỳ kê khai tháng sang quý. Từ 1/1/2026: bậc thấp nhất 5% đến 10 triệu/tháng, cao nhất 35% trên 100 triệu;
#    giảm trừ bản thân 11 lên 15,5 triệu/tháng, người phụ thuộc 4,4 lên 6,2 triệu.
#  - Nhân Dân 29/11/2025 (Bộ Tài chính trình): khung 5 bậc – đến 10 triệu 5%; trên 10 đến 30 triệu 10%; trên 30 đến 60 triệu 20%; trên 60 đến 100 triệu 30%; trên 100 triệu 35%.
#  - Biểu 7 bậc cũ (Luật Thuế TNCN 2007, sửa đổi 2012, Điều 22): đến 5 triệu 5%; 5–10 10%; 10–18 15%; 18–32 20%; 32–52 25%; 52–80 30%; trên 80 triệu 35%.
#  - VCCI 26/2/2026: Quốc hội thông qua 10/12/2025; nâng giảm trừ ước giúp người lao động đỡ hơn 8.700 tỷ đồng tiền thuế.
#  - Nghị quyết 954/2020/UBTVQH14: giảm trừ 11 triệu (bản thân), 4,4 triệu (người phụ thuộc) từ 1/7/2020.
#  - Doanh Nhân Việt Nam 9/11/2026: Nghị quyết 43/2026/QH16 (24/8/2026) + Nghị định 398 (hiệu lực 29/10/2026): hộ, cá nhân kinh doanh doanh thu không quá 10 tỷ/năm giảm 30% số thuế TNCN phải nộp, kỳ 2026 và 2027.
#  - WiData (Cục Thống kê): thu nhập bình quân tháng của lao động Q3/2020 5.789,5 nghìn đồng, Q3/2026 9.184,9 nghìn đồng (+58,6%, tự tính);
#    CPI bình quân năm 2021 1,89%; 2022 3,15%; 2023 3,25%; 2024 3,63%; 2025 3,31% → giá cả 2021–2025 cộng dồn khoảng +16% (tự tính: nhân 5 hệ số = 1,162).
#  - Báo Pháp luật 22/10/2026 (CBS): CEO Nvidia Jensen Huang nói khoản thuế khoảng 8 tỷ USD trong 5 năm (đề xuất thuế tài sản California) là một đặc quyền.
# TỰ TÍNH (thu nhập sau bảo hiểm, đã gồm giảm trừ):
#  - Anh Minh 27 triệu, 1 con: cũ 27 − 11 − 4,4 = 11,6 → 5×5% + 5×10% + 1,6×15% = 0,99 triệu; mới 27 − 15,5 − 6,2 = 5,3 → 5,3×5% = 0,265 triệu; bớt 0,725 triệu/tháng (73%), 8,7 triệu/năm.
#  - Chị Lan 110 triệu, không người phụ thuộc: cũ 99 → 0,25+0,5+1,2+2,8+5+8,4+6,65 = 24,8 triệu; mới 94,5 → 0,5+2+6+10,35 = 18,85 triệu; bớt 5,95 triệu/tháng (24%).
#  - Thu nhập 9,18 triệu (bình quân): dưới 11 triệu lẫn 15,5 triệu → 0 đồng cả hai năm.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261120_0100'
KEY = 'CH2711TN'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
HA = 'ov:Hanoi apartment buildings||Hanoi skyline night'
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
BX = 'ov:Bitexco Financial Tower||Ho Chi Minh City skyline night'
NT = 'ov:Nhat Tan Bridge||Hanoi skyline night'
BT = 'ov:Ben Thanh Market||Ho Chi Minh City skyline night'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('THUẾ THU NHẬP NĂM NAY', 'DỰ KIẾN HỤT 33.800 TỶ'), cols=CC, noti=dict(gio='07:10', ngay='Thứ Sáu', items=[
        ('Tin tức', 'Ngân sách', 'Thu thuế thu nhập cá nhân năm nay dự kiến hụt gần 34.000 tỷ đồng', V_),
        ('Email', 'Phòng nhân sự', 'Phiếu lương tháng 11: thuế thu nhập 265.000 đồng', G_),
        ('Zalo', 'Chị Lan', 'Năm nay chị được giảm gần 6 triệu tiền thuế mỗi tháng', X_)]),
      say=("Bảy giờ sáng thứ Sáu ở Hà Nội, điện thoại anh Minh, một kế toán, sáng lên ba lần. "
           "Tin thứ nhất: thu thuế thu nhập cá nhân năm nay dự kiến hụt gần ba mươi tư nghìn tỷ đồng. "
           "Tin thứ hai: phiếu lương tháng mười một, dòng thuế thu nhập của anh chỉ còn hai trăm sáu mươi lăm nghìn đồng. "
           "Tin thứ ba, từ chị gái anh, chị Lan: năm nay chị được giảm gần sáu triệu tiền thuế mỗi tháng. "
           "Anh Minh tự hỏi: cùng một lần giảm thuế, sao chị mình được nhiều gấp tám lần mình?")),
 dict(k='bignum', anh=HN, cap=('THUẾ THU NHẬP CÁ NHÂN', 'THẤP HƠN DỰ TOÁN 33.800 TỶ'), cols=CC, value=33800, fmt='{:,.0f}', unit=' TỶ ĐỒNG', top='THU THUẾ THU NHẬP CÁ NHÂN 2026 THẤP HƠN DỰ TOÁN',
      sub='cả năm ước 203.200 tỷ, thấp hơn năm ngoái 13,6% – Bộ Tài chính, VnExpress 23/10', col=GOLD,
      say=("Con số này nằm trong báo cáo dự toán ngân sách của Bộ Tài chính. Cả năm nay, thuế thu nhập cá nhân ước thu khoảng hai trăm linh ba nghìn tỷ đồng. "
           "Thấp hơn dự toán ba mươi ba nghìn tám trăm tỷ. "
           "Bộ Tài chính nêu nguyên nhân: mức giảm trừ được nâng, biểu thuế đổi mới, và kỳ kê khai chuyển sang theo quý cũng làm chậm tiến độ thu. Vậy phần tiền thuế được giảm nằm lại trong túi ai?")),
 dict(k='checklist', anh=HA, cap=('3 CHI TIẾT', 'TRẢ LỜI CUỐI PHIM'), cols=CC,
      items=[('1. Phiếu lương: 990 nghìn còn 265', V_), ('2. Tờ giấy cũ: giảm trừ 11 triệu, 2020', X_), ('3. Mẹ hỏi: giảm thuế mẹ được gì?', G_)],
      say=("Ba chi tiết nhỏ trong nhà anh Minh sẽ trả lời câu hỏi đó ở cuối phim, anh chị nhớ giúp em. "
           "Một: trên phiếu lương của anh Minh, tiền thuế mỗi tháng từ chín trăm chín mươi nghìn xuống còn hai trăm sáu mươi lăm nghìn. "
           "Hai: trên tủ lạnh nhà anh vẫn dán một tờ giấy cũ ghi mức giảm trừ mười một triệu, từ tháng bảy năm hai nghìn hai mươi. "
           "Ba: mẹ anh, công nhân may đã nghỉ hưu, gọi điện hỏi: giảm thuế thì mẹ được gì?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Luật thuế đổi những gì?', cap=('BIỂU THUẾ 7 BẬC', 'CÒN 5 BẬC'), cols=CC, moc=True, giay=dict(tieu_de='THUẾ THU NHẬP TỪ TIỀN LƯƠNG 2026', so='VnExpress 23/10/2026, Nhân Dân', dau='ĐANG ÁP DỤNG', dieu=[
        ('Giảm trừ cho bản thân', '15,5 TRIỆU'),
        ('Mỗi người phụ thuộc', '6,2 TRIỆU'),
        ('Bậc thấp nhất, đến 10 triệu', '5%'),
        ('Bậc cao nhất, trên 100 triệu', '35%')]),
      say=("Theo Bộ Tài chính, từ kỳ tính thuế năm hai nghìn không trăm hai mươi sáu, cách tính thuế từ tiền lương đã đổi. "
           "Mức giảm trừ cho bản thân tăng từ mười một lên mười lăm phẩy năm triệu đồng mỗi tháng. Mỗi người phụ thuộc tăng từ bốn phẩy bốn lên sáu phẩy hai triệu. "
           "Biểu thuế lũy tiến rút từ bảy bậc xuống năm bậc.")),
 dict(k='cards', anh=HN, cap=('BẬC THUẾ RỘNG RA', 'THUẾ SUẤT GIẢM XUỐNG'), cols=CC, moc=True,
      cards=[('10%', 'Phần từ 10 đến 30 triệu', 'Trước đây có phần chịu 15%'), ('20%', 'Phần từ 30 đến 60 triệu', 'Trước đây có phần chịu 25%'), ('35%', 'Phần trên 100 triệu', 'Trước đây từ 80 triệu')],
      say=("Các bậc ở giữa cũng rộng ra. Phần thu nhập tính thuế từ mười đến ba mươi triệu chịu mười phần trăm. "
           "Từ ba mươi đến sáu mươi triệu chịu hai mươi phần trăm. Mức cao nhất ba mươi lăm phần trăm nay chỉ áp cho phần trên một trăm triệu, thay vì trên tám mươi triệu như trước. "
           "Ai đang nộp thuế từ tiền lương cũng được giảm, nhưng rất khác nhau.")),
 dict(k='giay', cap=('THU NHẬP 27 TRIỆU, 1 CON', 'THUẾ 990 NGHÌN CÒN 265'), cols=CC, moc=True, giay=dict(tieu_de='PHIẾU LƯƠNG CỦA ANH MINH', so='Em giả định, em tự tính', dau='TỰ TÍNH', dieu=[
        ('Thu nhập sau bảo hiểm', '27 TRIỆU'),
        ('Thuế mỗi tháng, năm ngoái', '990.000Đ'),
        ('Thuế mỗi tháng, năm nay', '265.000Đ'),
        ('Bớt mỗi năm', '8,7 TRIỆU')]),
      say=("Phiếu lương của anh Minh là em giả định, còn phép tính theo đúng biểu thuế. Anh có thu nhập sau bảo hiểm hai mươi bảy triệu đồng mỗi tháng, nuôi một con nhỏ. "
           "Năm ngoái mỗi tháng anh nộp chín trăm chín mươi nghìn đồng. Năm nay chỉ còn hai trăm sáu mươi lăm nghìn. "
           "Anh Minh bớt bảy trăm hai mươi lăm nghìn đồng mỗi tháng, tức khoảng tám triệu bảy trăm nghìn một năm.")),
 dict(k='chat', cap=('"CHỊ ĐƯỢC GIẢM', 'GẦN 6 TRIỆU MỘT THÁNG"'), cols=CC, moc=True, chat=dict(ten='Chị Lan', tv='Đang hoạt động', gio='12:20', mau=X_, msgs=[
        ('Chị Lan', 'Thuế của chị từ 24,8 triệu xuống còn 18,85 triệu'),
        ('me', 'Em chỉ bớt có 725 nghìn thôi chị ạ'),
        ('Chị Lan', 'Thế là chị được nhiều gấp 8 lần em à?')]),
      say=("Trưa đó chị Lan, quản lý một công ty, nhắn lại cho em trai. Thu nhập sau bảo hiểm của chị là một trăm mười triệu đồng, chưa có người phụ thuộc. "
           "Theo biểu cũ, mỗi tháng chị nộp hai mươi tư phẩy tám triệu. Theo biểu mới còn mười tám triệu tám trăm năm mươi nghìn. "
           "Chị bớt gần sáu triệu đồng mỗi tháng, gấp hơn tám lần em trai.")),
 dict(k='bars', anh=HN, cap=('CÙNG MỘT LẦN GIẢM THUẾ', 'MỖI NGƯỜI MỘT KHÁC'), cols=CC, moc=True, top='TIỀN THUẾ BỚT MỖI THÁNG (TRIỆU ĐỒNG, EM TỰ TÍNH)',
      bars=[('Thu nhập 27 tr', 0.725, V_, '0,725'), ('Thu nhập 110 tr', 5.95, G_, '5,95')],
      say=("Đặt hai chị em cạnh nhau. Người thu nhập hai mươi bảy triệu bớt bảy trăm hai mươi lăm nghìn mỗi tháng. "
           "Người thu nhập một trăm mười triệu bớt gần sáu triệu. Cùng một luật, khoảng cách gấp hơn tám lần.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='bignum', ch='Chương 2 – Cú lật: tính theo phần trăm', anh=HA, cap=('THUẾ CỦA ANH MINH', 'GIẢM 73%'), cols=CC, moc=True, value=73, fmt='{:,.0f}', unit='%', top='TIỀN THUẾ MỖI THÁNG GIẢM BAO NHIÊU PHẦN TRĂM',
      sub='27 triệu: giảm 73% · 110 triệu: giảm 24% · 11 đến 15,5 triệu: hết phải nộp – em tự tính', col=GREEN,
      say=("Nhưng có một cú lật, nếu đổi sang tính theo phần trăm. "
           "Tiền thuế của anh Minh giảm bảy mươi ba phần trăm, gần ba phần tư. Tiền thuế của chị Lan chỉ giảm hai mươi tư phần trăm. Còn người thu nhập từ mười một đến mười lăm phẩy năm triệu, không người phụ thuộc, năm nay hết phải nộp. "
           "Tính theo số tiền, người thu nhập cao được nhiều hơn. Tính theo phần trăm, người thu nhập vừa được nhiều hơn. Biểu thuế lũy tiến vận hành đúng như vậy.")),
 dict(k='noti', cap=('Ở MỸ, CEO NVIDIA NÓI', 'ĐÓNG THUẾ LÀ ĐẶC QUYỀN'), cols=CC, moc=True, noti=dict(gio='20:30', ngay='Thứ Sáu', items=[
        ('Tin tức', 'Thế giới', 'CEO Nvidia: thuế tài sản khoảng 8 tỷ USD trong 5 năm là một đặc quyền', V_),
        ('Zalo', 'Chị Lan', 'Ông ấy còn nói đóng nhiều là đặc quyền đấy', X_)]),
      say=("Tối đó, chị Lan gửi cho em trai một tin thế giới. Ở Mỹ, ông Jensen Huang, giám đốc điều hành Nvidia, gọi khoản thuế tài sản khoảng tám tỷ đô la mà bang California đề xuất là một đặc quyền. "
           "Chị Lan nhắn: chị vẫn đóng gần mười chín triệu mỗi tháng, chỉ là ít hơn trước.")),
 dict(k='call', cap=('"GIẢM THUẾ THÌ', 'MẸ ĐƯỢC GÌ HẢ CON?"'), cols=CR, moc=True, call=dict(ten='Mẹ', phu='Đang gọi', mau=V_, loi=[
        'Giảm thuế thì mẹ có được gì không con?']),
      say=("Cuối tuần, mẹ anh Minh gọi điện. Bà nghe tivi nói giảm thuế, hỏi con: thế mẹ có được gì không. "
           "Anh Minh chưa trả lời ngay, vì câu hỏi của mẹ không đơn giản như bà nghĩ.")),
 dict(k='cards', anh=BT, cap=('THU NHẬP BÌNH QUÂN', '9,18 TRIỆU MỘT THÁNG'), cols=CR, moc=True,
      cards=[('9,18 triệu', 'Thu nhập bình quân lao động', 'Quý 3/2026'), ('15,5 triệu', 'Mức giảm trừ bản thân', 'Chưa tính bảo hiểm'), ('30%', 'Hộ kinh doanh được giảm', 'Doanh thu dưới 10 tỷ')],
      say=("Theo Cục Thống kê, thu nhập bình quân của người lao động quý ba năm nay khoảng chín triệu một trăm tám mươi nghìn đồng mỗi tháng. "
           "Con số đó thấp hơn nhiều so với mức giảm trừ mười lăm phẩy năm triệu. Em sẽ quay lại con số này ở cuối phim. "
           "Riêng hộ kinh doanh có doanh thu không quá mười tỷ đồng một năm thì được giảm ba mươi phần trăm số thuế thu nhập phải nộp, cho năm nay và năm sau.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='giay', ch='Chương 3 – Lần trước: tháng 7 năm 2020', cap=('GIẢM TRỪ 11 TRIỆU', 'ĐỨNG YÊN 5 NĂM RƯỠI'), cols=CR, moc=True, giay=dict(tieu_de='TỜ GIẤY TRÊN TỦ LẠNH', so='Nghị quyết 954/2020, Cục Thống kê', dau='ĐÃ XẢY RA', dieu=[
        ('Nâng từ 9 lên, từ 7/2020', '11 TRIỆU'),
        ('Giữ nguyên đến hết năm', '2025'),
        ('Thu nhập bình quân quý 3/2020', '5,79 TRIỆU'),
        ('Thu nhập bình quân quý 3/2025', '8,36 TRIỆU')]),
      say=("Giờ đến tờ giấy cũ trên tủ lạnh. Lần nâng giảm trừ trước là tháng bảy năm hai nghìn hai mươi, từ chín lên mười một triệu đồng. "
           "Sau đó, con số mười một triệu đứng yên đến hết năm hai nghìn hai mươi lăm. "
           "Theo luật lúc đó, mức giảm trừ chỉ được xem lại khi giá cả tăng trên hai mươi phần trăm so với lần điều chỉnh trước. "
           "Trong khi đó, thu nhập bình quân của người lao động đi từ năm triệu tám trăm nghìn lên tám triệu ba trăm sáu mươi nghìn đồng.")),
 dict(k='bars', anh=HN, cap=('5 NĂM GIẢM TRỪ ĐỨNG YÊN', 'THU NHẬP TĂNG 44,4%'), cols=CC, moc=True, top='TỪ 2020 ĐẾN 2025 TĂNG BAO NHIÊU (%, EM TỰ TÍNH)',
      bars=[('Mức giảm trừ', 0, R_, '0'), ('Giá cả', 16.2, V_, '16,2'), ('Thu nhập bình quân', 44.4, G_, '44,4')],
      say=("Em tự tính từ số Cục Thống kê. Trong giai đoạn đó, mức giảm trừ tăng không phần trăm. "
           "Giá cả cộng dồn tăng khoảng mười sáu phần trăm, chưa chạm ngưỡng hai mươi. "
           "Còn thu nhập bình quân tăng bốn mươi bốn phẩy bốn phần trăm. "
           "Nghĩa là nhiều người lên lương từng bước rơi vào diện nộp thuế, hoặc nộp ở bậc cao hơn. "
           "Và mức mới mười lăm phẩy năm triệu vẫn chưa đuổi kịp mức tăng thu nhập của chính giai đoạn ấy.")),
 dict(k='checklist', anh=HA, cap=('2020 VÀ HÔM NAY', 'GIỐNG 2, KHÁC 2'), cols=CC, moc=True,
      items=[('Giảm trừ chỉ xem lại khi giá tăng 20%', R_), ('Lương tăng thì thuế tự tăng theo', R_), ('Lần này bậc thuế cũng rộng ra', G_), ('Hộ kinh doanh được giảm thêm 30%', G_)],
      say=("Anh Minh so lại hai lần. Giống nhau ở hai điểm: mức giảm trừ vẫn là một con số cố định, và cứ lên lương thì tiền thuế lại tự tăng theo. "
           "Khác nhau ở hai điểm: lần này chính các bậc thuế cũng rộng ra, và hộ kinh doanh nhỏ được giảm thêm ba mươi phần trăm. "
           "Còn mức mười lăm phẩy năm triệu sẽ được nâng tiếp vào năm nào, hiện chưa có lịch.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='cards', ch='Chương 4 – Tiền đỡ thuế đi đâu?', anh=HN, cap=('725 NGHÌN MỖI THÁNG', 'BA CÁCH DÙNG'), cols=CC, moc=True,
      cards=[('725.000đ', 'Để chung tài khoản lương', 'Dễ tan vào chi tiêu'), ('8,7 triệu', 'Để riêng cả năm', 'Thêm vào quỹ dự phòng'), ('Trả nợ', 'Trả bớt khoản vay lãi cao', 'Đỡ tiền lãi mỗi tháng')],
      say=("Hai vợ chồng anh Minh tính xem bảy trăm hai mươi lăm nghìn mỗi tháng nên đi đâu. "
           "Cách thứ nhất: để nguyên trong tài khoản lương, khoản này dễ tan vào tiền chợ. "
           "Cách thứ hai: chuyển riêng ngay ngày nhận lương, cả năm được khoảng tám triệu bảy, thêm vào quỹ dự phòng. "
           "Cách thứ ba: trả bớt một khoản vay lãi cao, nếu nhà đang có.")),
 dict(k='chat', cap=('"TIỀN ĐỠ THUẾ', 'CHUYỂN RIÊNG NGAY NGÀY LƯƠNG"'), cols=CC, moc=True, chat=dict(ten='Hằng', tv='Đang hoạt động', gio='21:45', mau=G_, msgs=[
        ('Hằng', 'Phần thuế giảm của anh để riêng sang tài khoản khác nhé'),
        ('me', 'Ừ, đặt lệnh tự chuyển ngày 5 hằng tháng'),
        ('Hằng', 'Em cũng để riêng phần thuế thu nhập được giảm 30%')]),
      say=("Chị Hằng, vợ anh, bán hàng online theo hộ kinh doanh, nhắn: phần thuế giảm của anh thì chuyển riêng sang tài khoản khác nhé. "
           "Anh Minh đặt lệnh tự chuyển vào ngày năm hằng tháng. "
           "Chị Hằng cũng để riêng phần thuế thu nhập được giảm ba mươi phần trăm.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Huy Nguyễn ghép ba chi tiết', anh=HA, cap=('3 CHI TIẾT ĐẦU PHIM', 'GHÉP LẠI THÀNH LỜI GIẢI'), cols=CC, moc=True,
      items=[('1. Giảm 73%, nhưng chỉ 725 nghìn', V_), ('2. Tờ giấy 2020: có thể đứng yên lâu', X_), ('3. Mẹ hỏi: giảm thuế mẹ được gì?', G_)],
      say=("Giờ quay lại ba chi tiết đầu phim. Chi tiết thứ nhất, phiếu lương từ chín trăm chín mươi nghìn còn hai trăm sáu mươi lăm nghìn. Giảm bảy mươi ba phần trăm nghe rất lớn, nhưng tính ra chỉ bảy trăm hai mươi lăm nghìn mỗi tháng. "
           "Chi tiết thứ hai, tờ giấy ghi mức mười một triệu từ năm hai nghìn hai mươi. Mức mười lăm phẩy năm triệu hôm nay cũng có thể đứng yên nhiều năm, trong khi lương cứ tăng. Phần lợi hôm nay sẽ mỏng dần qua từng lần lên lương.")),
 dict(k='checklist', anh=HN, cap=('CHI TIẾT THỨ BA', 'CÂU HỎI CỦA MẸ'), cols=CC, moc=True,
      items=[('Lương hưu: không chịu thuế thu nhập', G_), ('Đi làm dưới 11 triệu: vốn không nộp', G_), ('Bình quân 9,18 triệu: dưới mức đó', R_)],
      say=("Chi tiết thứ ba, câu hỏi của mẹ. Lương hưu của bà không chịu thuế thu nhập. Người đi làm có thu nhập dưới mười một triệu vốn đã không nộp. Thu nhập bình quân cả nước, chín triệu một trăm tám mươi nghìn, cũng nằm dưới mức đó. Với họ, lần giảm thuế này không đổi gì.")),
 dict(k='checklist', anh=HN, cap=('AI ĐƯỢC NHIỀU NHẤT?', '3 ĐÁP ÁN'), cols=CC, moc=True,
      items=[('Theo tiền: thu nhập cao được nhiều nhất', V_), ('Theo phần trăm: thu nhập vừa được nhiều', X_), ('Dưới 11 triệu: không đổi gì', R_)],
      say=("Ghép ba chi tiết lại, câu hỏi ai được nhiều nhất có ba đáp án. Tính theo số tiền, người thu nhập cao được nhiều nhất. Tính theo phần trăm, người thu nhập vừa được nhiều. Người dưới mười một triệu không được gì. Và với ai đang được, phần đó sẽ mỏng dần.")),
 dict(k='checklist', anh=TP, cap=('PHÉP THỬ CỦA ANH CHỊ', 'TỰ TÍNH LẠI TIỀN THUẾ'), cols=CC, moc=True,
      items=[('Thu nhập sau bảo hiểm, trừ 15,5 triệu', X_), ('Trừ tiếp 6,2 triệu mỗi người phụ thuộc', X_), ('Còn dương thì so với phiếu lương', G_)],
      say=("Phép thử cho anh chị tối nay: lấy thu nhập sau bảo hiểm mỗi tháng, trừ mười lăm phẩy năm triệu cho bản thân, trừ tiếp sáu phẩy hai triệu cho mỗi người phụ thuộc. "
           "Nếu kết quả âm, anh chị không nộp thuế thu nhập từ tiền lương. Nếu còn dương, hãy so dòng thuế trên phiếu lương năm nay với năm ngoái, rồi xem phần chênh đó đang nằm ở tiết kiệm, ở khoản trả nợ, hay đã tan vào chi tiêu. "
           "Đây là mốc em đặt để tự soi.")),
 dict(k='checklist', ch='Chương 6 – Theo dõi gì tiếp theo?', anh=BX, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY ĐẾN QUYẾT TOÁN'), cols=CC, moc=True,
      items=[('Quyết toán thuế năm 2026', V_), ('Đăng ký đủ người phụ thuộc', V_), ('Số thu ngân sách cuối năm', R_)],
      say=("Em gợi ý theo dõi ba điều. "
           "Một: quyết toán thuế năm hai nghìn không trăm hai mươi sáu, năm đầu áp biểu năm bậc. Ai có từ hai nguồn lương trở lên nên tự kiểm lại. "
           "Hai: đăng ký đủ người phụ thuộc, mỗi người được trừ sáu phẩy hai triệu mỗi tháng. "
           "Ba: số thu ngân sách cuối năm, xem khoản hụt thuế thu nhập thực tế là bao nhiêu. Số liệu ngân sách hằng tháng, anh chị xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn của mẹ', cap=('"CON ĐƯỢC GIẢM THÌ GIỮ LẠI', 'ĐỪNG TIÊU NHƯ TIỀN THƯỞNG"'), cols=CC, moc=True, chat=dict(ten='Mẹ', tv='Đang hoạt động', gio='22:30', mau=V_, msgs=[
        ('Mẹ', 'Mẹ không được giảm, nhưng con được thì giữ lại'),
        ('Mẹ', 'Đừng tiêu như tiền thưởng'),
        ('me', 'Dạ, con chuyển riêng rồi mẹ ạ')]),
      say=("Gần khuya, mẹ anh Minh nhắn: mẹ không được giảm gì, nhưng con được thì giữ lại, đừng tiêu như tiền thưởng. "
           "Phần thuế được giảm nhờ luật mới không biến mất. Nó nằm lại trong túi những người đang nộp thuế. Còn nằm được bao lâu, là do từng nhà.")),
 dict(k='end', cap=('THUẾ GIẢM, PHẦN CỦA NHÀ MÌNH', 'ĐANG NẰM Ở ĐÂU?'), cols=CC,
      say=("Còn anh chị thì sao: phần thuế thu nhập nhà mình được giảm năm nay đang nằm ở đâu, tiết kiệm, trả nợ, hay đã tan vào chi tiêu? "
           "Kể cho em và mọi người ở phần bình luận nhé. Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu hỏi lớn tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Thu Thuế Thu Nhập Hụt 34.000 Tỷ: Ai Lợi Nhất? Thu Nhập 110 Triệu Bớt 6 Triệu, 9 Triệu Bớt 0 Đồng'
MT = ("Thu thuế thu nhập cá nhân năm 2026 dự kiến thấp hơn dự toán 33.800 tỷ đồng chủ yếu vì luật mới: giảm trừ bản thân 15,5 triệu, người phụ thuộc 6,2 triệu, biểu thuế 7 bậc còn 5 bậc. "
      "Cùng một lần giảm thuế: thu nhập 110 triệu bớt 5,95 triệu mỗi tháng, thu nhập 27 triệu bớt 725 nghìn (giảm 73%), còn người thu nhập dưới 11 triệu vốn không nộp nên không được gì (thu nhập bình quân cả nước 9,18 triệu). "
      "Lần trước mức giảm trừ 11 triệu đứng yên từ 7/2020 đến hết 2025 trong khi thu nhập bình quân tăng 44,4% – phần đỡ thuế năm nay sẽ mỏng dần. Câu chuyện nhà anh Minh, chị Hằng ở Hà Nội.\n\n"
      "Nguồn số liệu:\n"
      "• VnExpress 23/10/2026 (Bộ Tài chính, công khai dự toán ngân sách): thu thuế thu nhập cá nhân 2026 ước 203.200 tỷ đồng, thấp hơn dự toán 33.800 tỷ (14,3%), thấp hơn năm 2025 13,6%; từ 1/1/2026 biểu lũy tiến 5 bậc, thấp nhất 5% đến 10 triệu/tháng, cao nhất 35% trên 100 triệu; giảm trừ bản thân 11 lên 15,5 triệu/tháng, người phụ thuộc 4,4 lên 6,2 triệu; kỳ kê khai chuyển từ tháng sang quý\n"
      "• Nhân Dân 29/11/2025: khung 5 bậc – đến 10 triệu 5%; trên 10 đến 30 triệu 10%; trên 30 đến 60 triệu 20%; trên 60 đến 100 triệu 30%; trên 100 triệu 35%\n"
      "• Biểu 7 bậc cũ (Luật Thuế thu nhập cá nhân 2007, sửa đổi 2012, Điều 22): đến 5 triệu 5%; 5–10 triệu 10%; 10–18 triệu 15%; 18–32 triệu 20%; 32–52 triệu 25%; 52–80 triệu 30%; trên 80 triệu 35%\n"
      "• VCCI 26/2/2026: Luật Thuế thu nhập cá nhân sửa đổi thông qua 10/12/2025; nâng giảm trừ ước giúp người lao động đỡ hơn 8.700 tỷ đồng\n"
      "• Nghị quyết 954/2020/UBTVQH14: nâng giảm trừ bản thân từ 9 lên 11 triệu, người phụ thuộc từ 3,6 lên 4,4 triệu, từ 1/7/2020; Luật Thuế thu nhập cá nhân sửa đổi 2012 (Điều 19): mức giảm trừ được điều chỉnh khi CPI biến động trên 20% so với lần điều chỉnh gần nhất\n"
      "• Doanh Nhân Việt Nam 9/11/2026: Nghị quyết 43/2026/QH16 và Nghị định 398 (hiệu lực 29/10/2026) – hộ, cá nhân kinh doanh doanh thu không quá 10 tỷ đồng/năm được giảm 30% số thuế thu nhập cá nhân phải nộp, kỳ tính thuế 2026 và 2027\n"
      "• WiData (Cục Thống kê): thu nhập bình quân tháng của người lao động quý 3/2020 khoảng 5,79 triệu đồng, quý 3/2025 khoảng 8,36 triệu, quý 3/2026 khoảng 9,18 triệu; CPI bình quân năm 2021 1,89%, 2022 3,15%, 2023 3,25%, 2024 3,63%, 2025 3,31%\n"
      "• Báo Pháp luật 22/10/2026 (CBS): CEO Nvidia Jensen Huang nói khoản thuế khoảng 8 tỷ USD trong 5 năm theo đề xuất thuế tài sản của California là một đặc quyền, người kiếm nhiều tiền hơn nên đóng thuế nhiều hơn\n"
      "• Em tự tính (thu nhập sau bảo hiểm): 27 triệu, 1 người phụ thuộc – năm 2025: 27 − 11 − 4,4 = 11,6 triệu tính thuế, thuế 0,99 triệu/tháng; năm 2026: 27 − 15,5 − 6,2 = 5,3 triệu, thuế 0,265 triệu; bớt 0,725 triệu/tháng (73%), khoảng 8,7 triệu/năm. "
      "110 triệu, không người phụ thuộc – năm 2025: 99 triệu tính thuế, thuế 24,8 triệu; năm 2026: 94,5 triệu, thuế 18,85 triệu; bớt 5,95 triệu/tháng (24%). "
      "Thu nhập bình quân quý 3/2020 đến quý 3/2025: 8,36 / 5,79 ≈ +44,4%; giảm trừ mới 15,5 / 11 ≈ +40,9%; giá cả 2021–2025 cộng dồn khoảng +16,2% (nhân 5 hệ số CPI bình quân). Thu nhập sau bảo hiểm từ 11 đến 15,5 triệu, không người phụ thuộc: năm 2025 có nộp, năm 2026 không phải nộp\n\n"
      "Số liệu ngân sách, vĩ mô từng tháng: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật anh Minh, chị Hằng, chị Lan và mẹ là hư cấu; số liệu là thật. Ví dụ tính thuế chỉ để minh hoạ, chưa gồm các khoản giảm trừ khác (từ thiện, bảo hiểm hưu trí tự nguyện…).\n"
      "Chia sẻ góc nhìn, không phải tư vấn thuế, khuyến nghị mua bán hay tư vấn đầu tư.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn', ngay='2026-11-27', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['thuế thu nhập cá nhân', 'thuế TNCN 2026', 'giảm trừ gia cảnh', 'biểu thuế 5 bậc', 'cách tính thuế thu nhập', 'phiếu lương', 'ngân sách nhà nước', 'tài chính cá nhân', 'kinh tế Việt Nam', 'vĩ mô'],
    bia_hook=['HỤT 34.000 TỶ', 'AI LỢI NHẤT???'], badge='THUẾ THU NHẬP CÁ NHÂN',
    bia_anh='Hanoi skyline night||Hanoi skyline night',
    bia_hook_b=['THUẾ 990 NGHÌN', 'CÒN 265 NGHÌN'], badge_b='PHIẾU LƯƠNG 27 TRIỆU',
    bia_hook_c=['KIẾM 110 TRIỆU', 'BỚT 6 TRIỆU???'], badge_c='THU NHẬP 9,18TR: 0Đ',
    reel_hook='THUẾ THU NHẬP HỤT 34.000 TỶ|AI ĐƯỢC LỢI NHIỀU NHẤT???',
    fb_post=("Thuế thu nhập cá nhân năm nay dự kiến thấp hơn dự toán 33.800 tỷ đồng 💸\n\n👉 Giảm trừ bản thân 15,5 triệu, người phụ thuộc 6,2 triệu; biểu thuế 7 bậc còn 5 bậc\n"
             "👉 Thu nhập 27 triệu, 1 con: thuế 990 nghìn còn 265 nghìn mỗi tháng\n👉 Thu nhập 110 triệu: bớt gần 6 triệu mỗi tháng\n👉 Thu nhập bình quân 9,18 triệu: vốn không nộp, không được gì\n\n"
             "Phần đỡ thuế nhà anh chị đang nằm ở đâu?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – câu hỏi lớn: thuế thu nhập cá nhân giảm 34.000 tỷ, ai được nhiều nhất (NV1 20/11/2026).\n"
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
