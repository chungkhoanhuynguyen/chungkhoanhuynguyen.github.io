# -*- coding: utf-8 -*-
# QL1 10/11/2026 – kênh @5, VIẾT LẠI tập margin theo khuôn tập phím hàng (anh Huy: margin bản 1 "nghe 3 phút chán tắt", phím hàng "nghe đến hết").
# Khuôn: nhân vật phụ có tên + lời thoại, ≥1/3 cảnh điện thoại, mỗi chương 1 cú lật, thẻ số chen sau khi đã cài truyện, phần "chuyện có thật".
# Sự kiện thật: VN-Index đóng cửa 1.528,57 (4/1/2022) -> 911,9 (15/11/2022, gần 300 mã giảm sàn, Tiền Phong);
# lãnh đạo HBC, HDC bị bán giải chấp cuối 10/2022 (Tuổi Trẻ 27/10/2022). Phần còn lại là phép tính minh hoạ.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261110_1800_vt'
KEY = 'VT5MARGIN2'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, H_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (255, 120, 160)
v = lambda x, d=0: lib.vn(x, d)
VON, VAY, LS = 500, 500, 13.0
TONG = VON + VAY
def tk(g):
    ts = TONG * (1 - g / 100); con = ts - VAY; return ts, con, (1 - con / VON) * 100, con / ts * 100
LAI_THANG = VAY * LS / 100 / 12
D0, D1 = 1528.57, 911.9; GIAM22 = (1 - D1 / D0) * 100
def can_hoa(m): return (1 / (1 - m / 100) - 1) * 100
CTCK = 'Công ty chứng khoán'; LINH = 'Linh ♥'; NHOM = 'Hội bạn đại học'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('HAI TIN NHẮN', 'CÙNG MỘT LÚC'), cols=CR, noti=dict(gio='21:00', ngay='Thứ Năm', items=[
        ('Tin nhắn', LINH, 'Mai anh nhớ qua đón em đi xem nhẫn cưới nhé. Em chọn được mẫu rồi!', H_),
        ('Tin nhắn', CTCK, 'Tỷ lệ ký quỹ của Quý khách đã xuống dưới mức duy trì. Đề nghị nộp bổ sung trước 10:00 ngày mai, nếu không hệ thống sẽ bán giải chấp.', R_)]),
      say=("Chín giờ tối thứ Năm, điện thoại bạn rung hai lần liền. Tin thứ nhất từ người yêu: mai anh nhớ qua đón em đi xem nhẫn cưới nhé. "
           "Tin thứ hai từ công ty chứng khoán: tỷ lệ ký quỹ của quý khách đã xuống dưới mức duy trì. Nộp tiền trước mười giờ sáng mai, nếu không hệ thống sẽ tự bán.")),
 dict(k='text', cap=('500 TRIỆU TIỀN CƯỚI', 'CÒN LẠI BAO NHIÊU?'), cols=CC, anh='Ho Chi Minh City skyline',
      say=("Bạn mở ứng dụng. Năm trăm triệu tiền cưới, dành dụm suốt sáu năm, giờ chỉ còn hai trăm bảy mươi triệu. Và mười giờ sáng mai, có thể còn ít hơn nữa. "
           "Ba tháng trước, bạn chưa từng vay ai một đồng. Vậy chuyện gì đã xảy ra? "
           "Hôm nay mình sẽ cùng bạn sống lại từng ngày của câu chuyện đó: vì sao thật tệ khi vay margin đu đỉnh. "
           "Câu chuyện là giả định, nhưng mọi con số đều tính được, và ở cuối video mình sẽ cho bạn xem chuyện này đã xảy ra thật với cả những ông chủ doanh nghiệp.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='text', ch='Chương 1 – Đứa chậm chân nhất bàn nhậu', cap=('29 TUỔI, 500 TRIỆU', 'VÀ MỘT ĐÁM CƯỚI'), cols=CC, moc=True, anh='Ho Chi Minh City apartments',
      say=("Bạn 29 tuổi, làm kỹ sư phần mềm, lương hai mươi hai triệu. Bạn và Linh yêu nhau bốn năm, đã hẹn tháng Ba năm sau cưới. "
           "Năm trăm triệu trong sổ tiết kiệm là tiền làm đám cưới, đặt cọc một căn hộ nhỏ, và một chút để dành khi Linh sinh con. "
           "Bạn là kiểu người cẩn thận. Đi chợ cũng ghi chi tiêu vào điện thoại. Chưa bao giờ mua trả góp. Chưa bao giờ vay.")),
 dict(k='chat', cap=('AI CŨNG ĐANG LÃI', 'TRỪ MÌNH'), cols=CC, chat=dict(ten=NHOM, tv='18 thành viên', gio='22:47', msgs=[
        ('Khoa', 'Tháng này tao lãi 30% anh em ạ', 'lai', '+30,4%'),
        ('Tuấn Béo', 'Khoa dạo này ăn gì mà đỏ thế'),
        ('Khoa', 'Margin full. Tiền mình 1 đồng, công ty cho vay thêm 1 đồng. Lãi nhân đôi'),
        ('Khoa', 'Ai còn gửi tiết kiệm 6%/năm là lạc hậu rồi nhé'),
        ('me', 'Mình vẫn để tiết kiệm…'),
        ('Khoa', 'Thôi xong, ông cụ non của nhóm')]),
      say=("Rồi một tối, nhóm chat hội bạn đại học bỗng sôi lên. Khoa, đứa ngày xưa toàn chép bài của bạn, khoe tháng này lãi ba mươi phần trăm. "
           "Bí quyết của nó là margin full: tiền mình một đồng, công ty chứng khoán cho vay thêm một đồng, lãi nhân đôi. "
           "Bạn gõ một câu: mình vẫn để tiết kiệm. Khoa trả lời ngay: thôi xong, ông cụ non của nhóm. Cả nhóm thả một loạt mặt cười.")),
 dict(k='text', cap=('SỢ MẤT TIỀN', 'HAY SỢ BỊ BỎ LẠI?'), cols=CC, anh='Saigon river',
      say=("Bạn tắt điện thoại, nhưng câu ông cụ non cứ lởn vởn trong đầu. Lãi tiết kiệm một tháng của bạn được khoảng hai triệu rưỡi. Khoa một tháng lãi gần trăm triệu. "
           "Đêm đó bạn không sợ mất tiền. Bạn sợ một thứ khác: sợ mình là đứa duy nhất đứng ngoài bữa tiệc. "
           "Và đó chính là cảm giác nguy hiểm nhất trong đầu tư.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='chat', ch='Chương 2 – Cuộc gọi lúc 10 giờ sáng', cap=('"SỨC MUA CỦA ANH', 'ĐANG LÀ 1 TỶ"'), cols=CC, moc=True, chat=dict(ten='Vy – Chuyên viên tư vấn', tv='Công ty chứng khoán', gio='10:02', mau=X_, msgs=[
        ('Vy', 'Em chào anh, tài khoản anh vừa mở xong rồi ạ'),
        ('Vy', 'Anh nộp 500 triệu thì sức mua của anh đang là 1 tỷ đó anh'),
        ('me', 'Vay thêm thì lãi bao nhiêu em?'),
        ('Vy', 'Dạ khoảng 13%/năm, tính theo ngày, dùng ngày nào tính ngày đó thôi ạ'),
        ('Vy', 'Thị trường đang đẹp lắm anh, nhiều khách bên em dùng hết sức mua')]),
      say=("Tuần sau, bạn mở tài khoản chứng khoán, chuyển vào năm trăm triệu. Mười giờ sáng, một chuyên viên tư vấn tên Vy nhắn tin. "
           "Anh ơi, sức mua của anh đang là một tỷ đồng đó ạ. Lãi vay khoảng mười ba phần trăm mỗi năm, dùng ngày nào tính ngày đó thôi. "
           "Thị trường đang đẹp lắm anh. Nhiều khách bên em dùng hết sức mua.")),
 dict(k='cards', cap=('500 TRIỆU', 'THÀNH SỨC MUA 1 TỶ'), cols=CC, moc=True,
      cards=[('%s triệu' % v(VON), 'tiền thật của bạn', ''), ('%s triệu' % v(VAY), 'tiền vay công ty chứng khoán', ''), ('%s triệu' % v(TONG), 'cổ phiếu đứng tên bạn', '')],
      say=("Bạn nhìn nút mua tối đa rất lâu. Rồi bạn bấm. Năm trăm triệu của bạn, cộng năm trăm triệu tiền vay, thành một tỷ đồng cổ phiếu. "
           "Nghe giống như được tặng thêm một đôi chân. Nhưng thật ra, đó là một cái thang đi mượn. "
           "Người ta cho bạn mượn thang để leo cao hơn. Họ không cho bạn mượn dù để nhảy xuống.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='bignum', ch='Chương 3 – Tuần trăng mật', cap=('THỊ TRƯỜNG +10%', 'VỐN CỦA BẠN'), cols=CC, moc=True, value=20, fmt='+{:,.0f}', unit='%', top='LÃI 100 TRIỆU', sub='trong vòng một tháng', col=GREEN,
      say=("Tháng đầu tiên, mọi thứ đẹp như mơ. Cổ phiếu tăng mười phần trăm. Một tỷ thành một tỷ một trăm triệu. "
           "Khoản vay vẫn là năm trăm triệu, nên toàn bộ một trăm triệu tiền lãi là của bạn. Vốn của bạn tăng hai mươi phần trăm, gấp đôi thị trường.")),
 dict(k='chat', cap=('"ÔNG CỤ NON"', 'ĐÃ VÀO BỮA TIỆC'), cols=CC, chat=dict(ten=NHOM, tv='18 thành viên', gio='21:30', msgs=[
        ('me', 'Tháng đầu chơi margin, ăn 100 củ anh em', 'lai', '+20,0%'),
        ('Khoa', 'Đấy, tao nói mà. Chào mừng đến với thế giới người lớn'),
        ('Tuấn Béo', 'Ông cụ non lột xác rồi'),
        ('*', 'Linh đã gửi một tin nhắn riêng')]),
      say=("Lần này, chính bạn là người chụp màn hình gửi vào nhóm. Tháng đầu chơi margin, ăn một trăm củ anh em. "
           "Khoa trả lời: đấy, tao nói mà, chào mừng đến với thế giới người lớn. "
           "Bạn cười một mình trong phòng. Lần đầu tiên sau nhiều năm, bạn thấy mình không còn chậm chân.")),
 dict(k='chat', cap=('"MÌNH ĐẶT NHÀ HÀNG', 'XỊN HƠN NHÉ"'), cols=CC, chat=dict(ten=LINH, tv='Đang hoạt động', gio='21:41', mau=H_, msgs=[
        ('Linh', 'Anh ơi bên nhà hàng gửi báo giá rồi, gói thường hay gói cao cấp hả anh?'),
        ('me', 'Gói cao cấp đi em. Tháng này anh đầu tư được 100 triệu'),
        ('Linh', 'Thật á? Anh giỏi thế'),
        ('Linh', 'Mà anh có chắc không, đừng dùng tiền cưới nha anh')]),
      say=("Tối đó Linh hỏi: nhà hàng gửi báo giá rồi, gói thường hay gói cao cấp hả anh. Bạn trả lời không cần nghĩ: gói cao cấp đi em, tháng này anh đầu tư được một trăm triệu. "
           "Linh nhắn lại: anh giỏi thế. Rồi thêm một câu nữa, mà lúc đó bạn đọc lướt qua: mà anh có chắc không, đừng dùng tiền cưới nha anh.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='noti', ch='Chương 4 – Khoản nợ không bao giờ ngủ', cap=('KHOẢN NỢ', 'KHÔNG BAO GIỜ NGỦ'), cols=CC, moc=True, noti=dict(gio='08:00', ngay='Ngày 1', items=[
        ('Tin nhắn', CTCK, 'Lãi vay ký quỹ tháng này của Quý khách: %s đồng. Vui lòng đảm bảo số dư.' % v(LAI_THANG * 1e6), V_)]),
      say=("Đầu tháng, một tin nhắn nhỏ mà bạn gần như không để ý: lãi vay ký quỹ tháng này khoảng %s triệu đồng. "
           "Gần bằng tiền thuê một căn hộ nhỏ. Và khoản lãi này không nghỉ thứ Bảy, không nghỉ Chủ nhật, không nghỉ Tết. "
           "Sổ tiết kiệm trả tiền cho bạn khi bạn ngủ. Còn margin thì lấy tiền của bạn khi bạn ngủ.") % v(LAI_THANG, 1)),
 dict(k='bignum', cap=('ĐI NGANG 3 THÁNG', 'VẪN MẤT'), cols=CC, value=round(LAI_THANG * 3), fmt='{:,.0f}', unit=' triệu', top='LÃI VAY ~13%/NĂM TRÊN 500 TRIỆU', sub='cổ phiếu phải tăng nhanh hơn tiền lãi', col=GOLD,
      say=("Nếu thị trường chỉ đi ngang ba tháng, bạn vẫn mất khoảng %s triệu tiền lãi. "
           "Nghĩa là với margin, cổ phiếu không chỉ cần tăng. Nó phải tăng đủ nhanh để thắng cả khoản nợ đang chạy từng ngày.") % v(LAI_THANG * 3)),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='chat', ch='Chương 5 – Mã nóng nhất nhóm', cap=('"MÃ NÀY SẮP CÓ TIN"', '"VÀO ĐI"'), cols=CR, moc=True, chat=dict(ten='Khoa', tv='Đang hoạt động', gio='14:58', mau=(120, 230, 140), msgs=[
        ('Khoa', 'Mày đang cầm mã gì? Ngân hàng à? Rùa lắm'),
        ('Khoa', 'Bán đi, qua mã bất động sản này. Sắp có tin, tuần sau x2'),
        ('me', 'Nhưng nó vừa tăng 3 phiên rồi mà'),
        ('Khoa', 'Thế mới là sóng. Đứng ngoài thì đừng tiếc')]),
      say=("Rồi Khoa nhắn riêng. Mày đang cầm mã ngân hàng à, rùa lắm. Bán đi, qua mã bất động sản này, sắp có tin, tuần sau gấp đôi. "
           "Bạn hỏi: nhưng nó vừa tăng ba phiên rồi mà. Khoa trả lời: thế mới là sóng, đứng ngoài thì đừng tiếc. "
           "Bạn không mở báo cáo tài chính của mã đó. Bạn chỉ biết nó đang tăng, và ai cũng đang nói về nó.")),
 dict(k='text', cap=('ĐÂY MỚI LÀ', 'ĐU ĐỈNH'), cols=CR, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say=("Bạn bán mã ngân hàng đang lãi, dùng toàn bộ sức mua mới, mua mã bất động sản Khoa chỉ. Lại một tỷ đồng, lại tối đa margin. "
           "Chính khoảnh khắc này mới là đu đỉnh. Không phải vì giá đã cao. Mà vì lý do mua duy nhất còn lại là: người khác đang mua.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='bars', ch='Chương 6 – Khi thị trường quay đầu', cap=('THỊ TRƯỜNG GIẢM', 'VỐN CỦA BẠN MẤT'), cols=CR, moc=True,
      bars=[('Giảm %d%%' % g, round(tk(g)[2]), RED if g >= 20 else GOLD, '−' + v(tk(g)[2]) + '%') for g in (10, 20, 23)],
      say=("Hai tuần sau, thị trường bắt đầu quay đầu. Chậm rãi lúc đầu. Mã của bạn giảm mười phần trăm, tài khoản mất hai mươi phần trăm. "
           "Giảm hai mươi phần trăm, bạn mất bốn mươi phần trăm số vốn. "
           "Đòn bẩy làm lợi nhuận gấp đôi lúc lên, thì cũng làm thua lỗ gấp đôi lúc xuống. Toán học không thiên vị ai.")),
 dict(k='chat', cap=('"ĐIỀU CHỈNH THÔI"', '"HOLD CHẶT"'), cols=CR, chat=dict(ten=NHOM, tv='18 thành viên', gio='15:10', msgs=[
        ('me', 'Mã của Khoa giảm 20% rồi anh em ơi'),
        ('Khoa', 'Điều chỉnh thôi. Hold chặt, tuần sau có tin'),
        ('Tuấn Béo', 'Khoa ơi tao cũng đang kẹp mã đấy'),
        ('Khoa', 'Bình tĩnh. Ai bán bây giờ là dại')]),
      say=("Bạn nhắn vào nhóm: mã của Khoa giảm hai mươi phần trăm rồi anh em ơi. Khoa trả lời: điều chỉnh thôi, hold chặt, tuần sau có tin. "
           "Bạn tự nhủ, bán bây giờ là chốt lỗ, mà chốt lỗ thì đau. Bạn giữ. Và chờ cái tin tuần sau, cái tin không bao giờ đến.")),
 # ---------------- CHƯƠNG 7 ----------------
 dict(k='cards', ch='Chương 7 – Tin nhắn lúc 9 giờ tối', cap=('THỊ TRƯỜNG −23%', 'CHẠM VẠCH CALL MARGIN'), cols=CR, moc=True,
      cards=[('%s triệu' % v(tk(23)[0]), 'giá trị cổ phiếu còn lại', ''), ('%s triệu' % v(VAY), 'nợ vẫn y nguyên', ''), ('%s%%' % v(tk(23)[3]), 'tỷ lệ ký quỹ, chạm mức duy trì', '')],
      say=("Và rồi mã giảm hai mươi ba phần trăm. Một tỷ cổ phiếu chỉ còn %s triệu. Nhưng khoản nợ thì vẫn y nguyên năm trăm triệu. "
           "Phần thật sự là của bạn còn %s triệu, khoảng %s%% tổng tài sản, quanh mức tỷ lệ duy trì ở nhiều công ty chứng khoán. "
           "Đó là lúc hai tin nhắn đến cùng một lúc. Tin của Linh về chiếc nhẫn cưới. Và tin của công ty chứng khoán. Người ta gọi đó là call margin.") % (v(tk(23)[0]), v(tk(23)[1]), v(tk(23)[3]))),
 dict(k='text', cap=('HỌ KHÔNG QUAN TÂM', 'CỔ PHIẾU TỐT HAY XẤU'), cols=CR, anh='Ho Chi Minh City skyline',
      say=("Công ty chứng khoán không quan tâm cổ phiếu của bạn tốt hay xấu, sau này có lên lại hay không. "
           "Họ chỉ quan tâm một điều: khoản tiền cho vay phải an toàn. Và khi cần, họ sẽ bán cổ phiếu của bạn ở bất kỳ giá nào khớp được, để thu hồi phần của họ trước.")),
 # ---------------- CHƯƠNG 8 ----------------
 dict(k='checklist', ch='Chương 8 – Đêm không ngủ', cap=('ĐÊM ĐÓ BẠN CÓ', '3 LỰA CHỌN'), cols=CR, moc=True,
      items=[('Nộp thêm tiền: tiền ở đâu ra?', GOLD), ('Tự bán bớt: chốt lỗ ngay', GOLD), ('Không làm gì: bị bán giải chấp', RED)],
      say=("Đêm đó bạn có ba lựa chọn. Một, nộp thêm tiền, nhưng toàn bộ tiền tiết kiệm đã nằm trong tài khoản rồi. "
           "Hai, tự bán bớt để giảm nợ, tức là biến khoản lỗ trên giấy thành khoản lỗ thật. "
           "Ba, không làm gì, và sáng mai hệ thống sẽ bán thay bạn.")),
 dict(k='chat', cap=('"MẸ ƠI, CON CẦN', '100 TRIỆU"'), cols=CR, chat=dict(ten='Mẹ', tv='Đang hoạt động', gio='23:12', mau=(34, 197, 94), msgs=[
        ('me', 'Mẹ ơi mẹ ngủ chưa'),
        ('me', 'Con cần 100 triệu đặt cọc nhà, tuần sau con trả mẹ'),
        ('Mẹ', 'Sao gấp thế con? Có chuyện gì không?'),
        ('me', 'Không có gì đâu mẹ, chủ nhà đòi cọc sớm thôi'),
        ('Mẹ', 'Ừ để sáng mẹ ra ngân hàng rút sổ cho')]),
      say=("Mười một giờ đêm, bạn làm điều mà rất nhiều người đã làm. Bạn nhắn cho mẹ. Mẹ ơi, con cần một trăm triệu đặt cọc nhà, tuần sau con trả. "
           "Mẹ hỏi: sao gấp thế con, có chuyện gì không. Bạn nói dối: không có gì đâu mẹ, chủ nhà đòi cọc sớm thôi. "
           "Mẹ trả lời: ừ, để sáng mẹ ra ngân hàng rút sổ cho. Đó là sổ tiết kiệm mẹ gửi để dưỡng già.")),
 # ---------------- CHƯƠNG 9B: GỠ ----------------
 dict(k='chat', ch='Chương 9 – Gỡ bằng mọi giá', cap=('"BẮT ĐÁY ĐI"', '"GIỜ RẺ LẮM RỒI"'), cols=CR, moc=True, chat=dict(ten='Khoa', tv='Đang hoạt động', gio='20:40', mau=(120, 230, 140), msgs=[
        ('Khoa', 'Giờ giá rẻ lắm rồi, bắt đáy đi mày'),
        ('Khoa', 'Trung bình giá xuống, hồi 10% là về bờ'),
        ('me', 'Tao hết tiền rồi'),
        ('Khoa', 'Hỏi bên công ty xem, mã này giờ được vay tỷ lệ cao hơn đấy')]),
      say=("Tối hôm sau, Khoa lại nhắn. Giờ giá rẻ lắm rồi, bắt đáy đi mày, trung bình giá xuống, hồi mười phần trăm là về bờ. "
           "Bạn trả lời: tao hết tiền rồi. Khoa gửi một câu mà sau này bạn nhớ mãi: hỏi bên công ty xem, giờ được vay tỷ lệ cao hơn đấy. "
           "Người đang thua luôn muốn gỡ thật nhanh. Và cách nhanh nhất để gỡ, cũng là cách nhanh nhất để mất nốt.")),
 dict(k='chat', cap=('TIỀN CỦA MẸ', 'ĐI ĐÂU?'), cols=CR, chat=dict(ten='Vy – Chuyên viên tư vấn', tv='Công ty chứng khoán', gio='09:05', mau=X_, msgs=[
        ('me', 'Em ơi tài khoản anh còn vay thêm được không?'),
        ('Vy', 'Dạ anh vừa nộp thêm 100 triệu nên sức mua đang khoảng 150 triệu ạ'),
        ('me', 'Mua hết vào mã đang cầm cho anh'),
        ('Vy', 'Dạ em lưu ý anh tỷ lệ ký quỹ sẽ sát mức duy trì đó ạ'),
        ('me', 'Không sao, hồi lên là ổn')]),
      say=("Sáng hôm sau nữa, thay vì để một trăm triệu của mẹ nằm yên làm tấm đệm, bạn hỏi Vy: tài khoản anh còn vay thêm được không. "
           "Vy trả lời sức mua còn khoảng một trăm năm mươi triệu, và lưu ý tỷ lệ ký quỹ sẽ sát mức duy trì. "
           "Bạn gõ: không sao, hồi lên là ổn. Tấm đệm cuối cùng của bạn, bạn tự tay rút đi.")),
 # ---------------- CHƯƠNG 9 ----------------
 dict(k='noti', ch='Chương 10 – 9 giờ 15 sáng thứ Sáu', cap=('LỆNH BÁN', 'KHÔNG PHẢI CỦA BẠN'), cols=CR, moc=True, noti=dict(gio='09:17', ngay='Thứ Sáu', items=[
        ('Tin nhắn', CTCK, 'Lệnh bán giải chấp của Quý khách đã khớp một phần tại giá sàn.', R_),
        ('Nhóm chat', NHOM, 'Khoa: Tao bị bán giải chấp rồi anh em ạ', V_),
        ('Nhóm chat', NHOM, 'Tuấn Béo: Tao cũng vậy. Sàn trắng bên mua', V_)]),
      say=("Một trăm triệu của mẹ giờ đã thành cổ phiếu. Sáng thứ Sáu, thị trường mở cửa đỏ rực. Mã của bạn giảm sàn ngay từ chín giờ mười lăm. "
           "Tỷ lệ ký quỹ lại thủng vạch. Lần này bạn không còn ai để vay. Chín giờ mười bảy, tin nhắn: lệnh bán giải chấp đã khớp một phần tại giá sàn. "
           "Ngay sau đó, nhóm chat hội bạn hiện lên: Khoa, tao bị bán giải chấp rồi anh em ạ.")),
 dict(k='text', cap=('TẤT CẢ CÙNG BỊ CALL', 'TẤT CẢ CÙNG PHẢI BÁN'), cols=CR, anh='storm clouds',
      say=("Vấn đề là bạn không đứng một mình. Hàng nghìn tài khoản cũng vay margin, cũng nhận tin nhắn đó cùng một đêm. "
           "Ai không nộp được tiền sẽ bị bán. Lệnh bán dồn dập đẩy giá giảm thêm. Giá giảm thêm lại làm thêm nhiều tài khoản chạm vạch. "
           "Giống một hàng người đứng trên băng mỏng: người đầu tiên ngã xuống làm cả mảng băng nứt theo. Người ta gọi đó là vòng xoáy giải chấp.")),
 dict(k='bars', cap=('ĐÃ MẤT', 'CẦN TĂNG BAO NHIÊU ĐỂ VỀ BỜ'), cols=CR, moc=True,
      bars=[('Mất %d%%' % m, round(can_hoa(m)), GOLD if m < 50 else RED, '+' + v(can_hoa(m)) + '%') for m in (20, 46, 60, 80)],
      say=("Đến chiều thứ Sáu, tính cả một trăm triệu của mẹ, bạn đã mất hơn một nửa số tiền. Và đây là phần toán học ít ai nói cho bạn biết. "
           "Mất hai mươi phần trăm, cần tăng hai mươi lăm phần trăm để về bờ. Mất bốn mươi sáu phần trăm, cần tăng %s phần trăm. "
           "Mất sáu mươi phần trăm, cần tăng %s phần trăm. Thua càng sâu, đường về càng xa.") % (v(can_hoa(46)), v(can_hoa(60)))),
 # ---------------- CHƯƠNG 10 ----------------
 dict(k='bignum', ch='Chương 11 – Chuyện này đã xảy ra thật', cap=('VN-INDEX NĂM 2022', 'TỪ ĐỈNH XUỐNG ĐÁY'), cols=CR, moc=True, value=round(-GIAM22, 1), fmt='{:,.1f}', unit='%', top='TỪ %s XUỐNG %s ĐIỂM' % (v(D0, 0), v(D1, 0)), sub='đóng cửa 4/1/2022 và 15/11/2022', col=RED, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say=("Bạn có thể nghĩ đây chỉ là chuyện tưởng tượng. Ngày 4 tháng 1 năm 2022, VN-Index đóng cửa ở đỉnh khoảng %s điểm. "
           "Ngày 15 tháng 11 năm 2022, chỉ số đóng cửa ở %s điểm, giảm khoảng %s%%. Riêng phiên hôm đó, theo báo Tiền Phong, gần ba trăm mã giảm sàn, vì lực bán giải chấp xuất hiện ngay từ đầu phiên.") % (v(D0, 0), v(D1, 1), v(GIAM22, 0))),
 dict(k='cards', cap=('KHÔNG CHỈ NHÀ ĐẦU TƯ NHỎ', 'CẢ LÃNH ĐẠO DOANH NGHIỆP'), cols=CR, moc=True, anh='Ho Chi Minh City skyline',
      cards=[('HBC', 'Phó tổng giám đốc bị bán giải chấp, 10/2022', ''), ('HDC', 'thành viên HĐQT bị bán giải chấp, 10/2022', ''), ('~300 mã', 'giảm sàn phiên 15/11/2022', '')],
      say=("Và không chỉ nhà đầu tư nhỏ. Cuối tháng 10 năm 2022, theo báo Tuổi Trẻ, một phó tổng giám đốc của Xây dựng Hòa Bình bị bán giải chấp cổ phiếu. Một thành viên hội đồng quản trị của Hodeco cũng vậy. "
           "Những người hiểu doanh nghiệp của mình hơn ai hết, vẫn không thoát được khi đã vay quá tay đúng lúc thị trường quay đầu.")),
 # ---------------- CHƯƠNG 11 ----------------
 dict(k='chat', ch='Chương 12 – Điều thật sự tệ', cap=('"ANH NÓI THẬT ĐI"', '"TIỀN CƯỚI ĐÂU?"'), cols=CR, moc=True, chat=dict(ten=LINH, tv='Đang hoạt động', gio='22:03', mau=H_, msgs=[
        ('Linh', 'Mẹ anh gọi cho em, hỏi tiền cọc nhà là sao'),
        ('Linh', 'Anh nói thật đi. Tiền cưới đâu?'),
        ('me', 'Anh xin lỗi'),
        ('*', 'Linh đang nhập…'),
        ('Linh', 'Em đã nhắn anh rồi mà. Đừng dùng tiền cưới.')]),
      say=("Tối Chủ nhật, Linh nhắn: mẹ anh gọi cho em, hỏi tiền cọc nhà là sao. Anh nói thật đi, tiền cưới đâu. "
           "Bạn gõ đúng ba chữ: anh xin lỗi. Dòng chữ Linh đang nhập hiện lên, tắt đi, rồi lại hiện lên rất lâu. "
           "Cuối cùng chỉ có một câu: em đã nhắn anh rồi mà. Đừng dùng tiền cưới.")),
 dict(k='text', cap=('MẤT TIỀN', 'CHƯA PHẢI ĐIỀU TỆ NHẤT'), cols=CC, anh='Saigon river',
      say=("Điều thật sự tệ khi vay margin đu đỉnh không chỉ là mất tiền. Đó là sáu năm dành dụm biến mất trong ba tháng. "
           "Là khoản nợ với mẹ mà bạn phải nói dối để vay. Là một tin nhắn của người mình thương mà bạn từng đọc lướt qua. "
           "Và tệ nhất, sau cú đó, rất nhiều người không bao giờ quay lại thị trường nữa, bỏ lỡ luôn những năm thị trường hồi phục.")),
 # ---------------- CHƯƠNG 12 ----------------
 dict(k='checklist', ch='Chương 13 – Nếu vẫn muốn dùng margin', cap=('4 NGUYÊN TẮC', 'TRƯỚC KHI VAY'), cols=CC, moc=True,
      items=[('Không dùng tiền sắp cần đến', GREEN), ('Vay ít, không bao giờ mua tối đa', GREEN), ('Tự đặt điểm dừng trước vạch call', GREEN), ('Tính lãi vay vào kỳ vọng lợi nhuận', GOLD)],
      say=("Margin không phải ác quỷ. Nó là con dao trong bếp: vấn đề là ai cầm, và cầm lúc nào. Nếu vẫn muốn dùng, hãy nhớ bốn nguyên tắc. "
           "Một, không bao giờ dùng tiền sắp cần đến: tiền cưới, tiền nhà, tiền học. Hai, vay ít, đừng bao giờ bấm mua tối đa. "
           "Ba, tự đặt điểm dừng lỗ của mình, trước khi công ty chứng khoán đặt hộ. Bốn, cộng tiền lãi vay vào bài toán: nếu kỳ vọng không thắng nổi mười ba phần trăm mỗi năm, khoản vay đó không đáng.")),
 dict(k='text', cap=('ĐỪNG VAY TIỀN', 'MUA THỨ MÌNH KHÔNG HIỂU'), cols=CC, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say=("Và quan trọng nhất, đừng vay tiền để mua thứ mình không hiểu. Trong câu chuyện này, bạn chưa từng mở báo cáo tài chính của mã Khoa chỉ. "
           "Nếu muốn xem nhanh P/E, lợi nhuận và biên lãi của hơn 400 mã trước khi xuống tiền, bạn có thể tra miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='text', ch='Kết – Cái thang đi mượn', cap=('CÁI THANG', 'ĐI MƯỢN'), cols=CC, moc=True, anh='Ho Chi Minh City skyline',
      say=("Ba tháng sau, bạn vẫn đi làm, vẫn trả góp cho mẹ từng tháng. Linh chưa nói chia tay, nhưng đám cưới đã lùi sang một năm không có ngày. "
           "Còn Khoa đã rời nhóm chat từ lâu. "
           "Công ty chứng khoán cho bạn mượn một cái thang. Khi thang gãy, người ngã là bạn. Còn cái thang, họ đã thu về đúng giờ.")),
 dict(k='end', cap=('BẠN ĐÃ TỪNG', 'BỊ CALL MARGIN CHƯA?'), cols=CC,
      say=("Bạn đã từng nhận tin nhắn chín giờ tối đó chưa? Bài học lớn nhất của bạn là gì? Kể cho mọi người ở phần bình luận nhé, biết đâu có người đang cần nghe đúng câu chuyện của bạn. "
           "Tập sau: vì sao thật tệ khi gửi tiết kiệm cả đời.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vì Sao Thật Tệ Khi Vay Margin Đu Đỉnh | 9 Giờ Tối, 2 Tin Nhắn Đến Cùng Lúc'
MT = ("9 giờ tối, hai tin nhắn đến cùng lúc: người yêu hẹn đi xem nhẫn cưới, công ty chứng khoán báo call margin. 500 triệu tiền cưới, một nút \"mua tối đa\", một mã nóng bạn thân chỉ… và ba tháng sau.\n\n"
      "Câu chuyện giả định, nhưng mọi con số đều tính được: đòn bẩy margin, lãi vay ~13%/năm, tỷ lệ ký quỹ, vòng xoáy giải chấp. Và chuyện này đã xảy ra thật:\n"
      "• VN-Index đóng cửa 1.528,57 điểm (4/1/2022) → 911,9 điểm (15/11/2022), gần 300 mã giảm sàn phiên 15/11 (Tiền Phong)\n"
      "• Lãnh đạo HBC, HDC bị bán giải chấp cổ phiếu cuối 10/2022 (Tuổi Trẻ 27/10/2022)\n\n"
      "4 nguyên tắc trước khi vay margin ở chương 13.\n\n"
      "Tra P/E, lợi nhuận, biên lãi 400+ mã miễn phí: https://chungkhoanhuynguyen.com\nKênh chính: https://www.youtube.com/@chungkhoanhuynguyen\n\n"
      "Nhân vật là hư cấu. Ví dụ minh hoạ với lãi vay giả định ~13%/năm, tỷ lệ ký quỹ ban đầu 50%.\nChia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen5', seri='Vì sao thật tệ khi…', ngay='2026-11-15', gio_goi_y='20:00', gio='20:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['margin là gì', 'call margin', 'vay margin', 'đu đỉnh', 'giải chấp', 'F0 chứng khoán', 'đòn bẩy tài chính', 'vì sao thật tệ khi'],
    bia_hook=['2 TIN NHẮN', 'LÚC 9 GIỜ TỐI'], badge='VÌ SAO THẬT TỆ KHI…',
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh phụ @chungkhoanhuynguyen5 – tập margin VIẾT LẠI (QL1 10/11/2026) theo khuôn tập phím hàng.\n"
    "XH_BAN = True; NO_CTA = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), round(LAI_THANG, 2), round(GIAM22, 1), len(TIEU))
