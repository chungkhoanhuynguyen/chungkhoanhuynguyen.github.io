# -*- coding: utf-8 -*-
# QL1 11/11/2026 – THỬ khuôn "Vì Sao Thật Tệ Khi…" trên kênh phụ @chungkhoanhuynguyen6 (Đầu Tư Tích Sản) – anh Huy 11/11 17:10:
# "các kênh phụ khác cũng thử 1 video xem có chuyển biến tốt hơn không". KHUÔN CHUẨN: chi_dao/kenh5_vi_sao_that_te_1011.
# Số thật (WiData, giá vàng miếng SJC bán ra, nghìn đồng/lượng, giá cuối tuần):
#   31/12/2024 84.220 · 31/12/2025 152.820 · 13/3/2026 184.820 (cao nhất các tuần 2026) · 3/4 174.520 · 31/5 159.020 · 29/8 148.720 · 11/11/2026 140.020.
#   Đỉnh 13/3 -> 11/11: −24,2%. 1 tỷ mua ở đỉnh = 5,41 lượng -> nay ~757 triệu (giá bán ra; bán lại theo giá mua vào còn thấp hơn).
#   Người mua cuối 2024 (84,22 tr) nay vẫn +66%.
#   Thế giới quy đổi (WiData 1224337): 31/12/2024 82.264 · 27/2/2026 168.971 · 13/3 165.592 · 11/11 126.624. USD/oz đỉnh cuối T2 5.277,9; 11/11 4.056,7.
#   2011: đỉnh ~49 tr (9/2011), cuối 2013 35,1 tr (doanhnhanplus), vượt 50 tr 7/2020 (VTV/VTC). DCA T1–T10/2026 ước tính giá bán = mua vào+2,5 tr: 1 tỷ -> ~876 tr.
#   SJC mua vào (1224205): 13/3 181.800 · 11/11 137.000. 5,41 lượng x 137 = 741 tr. Tiết kiệm 1 tỷ x 5,4% x 8/12 = +36 tr.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261111_1900_vt6'
KEY = 'VT6VANG'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('1 TỶ MUA VÀNG', 'CÒN 757 TRIỆU'), cols=CR, noti=dict(gio='08:05', ngay='Thứ Tư', items=[
        ('Giá vàng', 'Bảng giá hôm nay', 'Vàng miếng bán ra: 140,02 triệu/lượng', R_),
        ('Zalo', 'Chị Thu – hàng xóm', 'Em ơi, vàng nhà chị mua tháng 3 giờ lỗ bao nhiêu rồi?', V_)]),
      say=("Sáng mười một tháng mười một, bạn mở bảng giá vàng: một trăm bốn mươi triệu đồng một lượng. Đúng tám tháng trước, bạn rút một tỷ tiền tiết kiệm, xếp hàng từ năm giờ sáng để mua năm lượng rưỡi vàng miếng, giá gần một trăm tám mươi lăm triệu. "
           "Giờ năm lượng rưỡi ấy chỉ còn khoảng bảy trăm năm mươi bảy triệu. Bạn mất gần một phần tư số tiền. Và người rủ bạn đi xếp hàng hôm đó, giờ đang nhắn hỏi chính bạn: lỗ bao nhiêu rồi?")),
 dict(k='text', cap=('VÌ SAO THẬT TỆ KHI', 'MUA VÀNG LÚC CẢ XÓM XẾP HÀNG'), cols=CC, anh='ov:gold bars||gold bullion',
      say=("Vàng là tài sản giữ giá, ông bà mình nói vậy và không sai. Nhưng vì sao có người mua vàng mà vẫn mất gần hai trăm rưỡi triệu chỉ trong tám tháng? "
           "Câu chuyện hôm nay là giả định, nhưng mọi con số giá vàng đều là số thật năm 2026.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Cơn sốt', cap=('"VÀNG CHỈ CÓ LÊN', 'KHÔNG CÓ XUỐNG"'), cols=CC, moc=True, chat=dict(ten='Hội chị em khu phố', tv='38 thành viên', gio='21:40', mau=V_, msgs=[
        ('Chị Thu', 'Vàng lên 184 triệu rồi, đầu năm mới 158'),
        ('Chị Thu', 'Mai 5h chị đi xếp hàng, ai đi cùng không?'),
        ('Lan', 'Em đi! Gửi tiết kiệm lãi có 5%, vàng 2 tháng lên 17%'),
        ('me', 'Vàng chỉ có lên chứ không có xuống đúng không chị?')]),
      say=("Tháng ba năm 2026. Nhóm Zalo khu phố của bạn sôi lên. Chị Thu nhắn: vàng lên một trăm tám mươi tư triệu rồi, đầu năm mới một trăm năm mươi tám. Mai năm giờ chị đi xếp hàng, ai đi cùng không? "
           "Lan nhảy vào: em đi, gửi tiết kiệm lãi có năm phần trăm một năm, vàng hai tháng lên mười bảy phần trăm. Bạn gõ một câu mà chính bạn cũng muốn tin: vàng chỉ có lên chứ không có xuống đúng không chị?")),
 dict(k='cards', anh='ov:gold bars||gold bullion', cap=('GIÁ VÀNG MIẾNG BÁN RA', 'TRIỆU ĐỒNG/LƯỢNG'), cols=CC, moc=True,
      cards=[('84,2', 'Cuối năm 2024', ''), ('152,8', 'Cuối năm 2025', ''), ('184,8', 'Tuần 13/3/2026 – cao nhất', '')],
      say=("Nhìn lại, cũng dễ hiểu vì sao cả xóm tin. Cuối năm 2024, một lượng vàng miếng giá khoảng tám mươi tư triệu. Cuối năm 2025, một trăm năm mươi hai triệu. "
           "Đến tuần mười ba tháng ba năm 2026, một trăm tám mươi tư phẩy tám triệu. Chỉ hơn một năm, giá đã hơn gấp đôi. Ai đứng ngoài cũng thấy mình đang lỡ tàu.")),
 dict(k='giay', cap=('PHIẾU MUA HÀNG', '13/3/2026'), cols=CR, giay=dict(tieu_de='PHIẾU BÁN HÀNG – VÀNG MIẾNG', so='Ngày 13/3/2026 – Khách hàng: Bạn', dau='ĐÃ THU TIỀN', dieu=[
        ('Số lượng: 5,4 lượng vàng miếng.', ''),
        ('Đơn giá bán ra: 184.820.000 đồng/lượng.', 'ĐỈNH'),
        ('Tổng thanh toán: khoảng 1.000.000.000 đồng – rút từ sổ tiết kiệm trước hạn.', 'MẤT LÃI')]),
      say=("Năm giờ sáng hôm sau, bạn đứng thứ ba mươi bảy trong hàng. Chín giờ, bạn cầm tờ phiếu: năm phẩy bốn lượng, giá một trăm tám mươi tư triệu tám trăm hai mươi nghìn đồng một lượng. Tổng khoảng một tỷ, rút từ sổ tiết kiệm trước hạn, mất luôn tiền lãi. "
           "Bạn không biết, đó là tuần giá vàng cao nhất cả năm.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='noti', ch='Chương 2 – Trượt dốc', cap=('MỖI THÁNG', 'MẤT VÀI CHỤC TRIỆU'), cols=CR, moc=True, noti=dict(gio='18:20', ngay='Thứ Bảy', items=[
        ('Giá vàng', 'Bảng giá', 'Vàng miếng: 159,02 triệu/lượng (31/5)', R_),
        ('Giá vàng', 'Bảng giá', 'Vàng miếng: 148,72 triệu/lượng (29/8)', R_)]),
      say=("Rồi giá bắt đầu đi xuống, không phải một cú sập, mà từ từ, như nước rút. Cuối tháng năm, một trăm năm mươi chín triệu. Cuối tháng tám, một trăm bốn mươi tám triệu. "
           "Mỗi lần mở bảng giá, bạn tự trấn an: vàng mà, rồi sẽ lên lại. Nhóm Zalo khu phố từ năm chục tin nhắn mỗi tối, giờ im lặng hẳn.")),
 dict(k='call', cap=('"CON CẦN TIỀN', 'ĐÓNG HỌC PHÍ"'), cols=CR, call=dict(ten='Con trai – Minh', phu='Di động', mau=X_, loi=[
        'Mẹ ơi, học phí kỳ này 45 triệu, hạn cuối thứ Sáu', 'Mẹ bán bớt vàng được không mẹ?']),
      say=("Tháng chín, con trai bạn gọi: mẹ ơi, học phí kỳ này bốn mươi lăm triệu, hạn cuối thứ sáu. Mẹ bán bớt vàng được không mẹ? "
           "Bạn mang vàng ra tiệm. Giá mua vào của tiệm còn thấp hơn giá bán ra vài triệu một lượng. Bạn bán đúng một lượng, và lần đầu tiên thấy rõ cái giá của việc mua đúng đỉnh.")),
 dict(k='noti', cap=('2 GIỜ SÁNG', 'VẪN MỞ BẢNG GIÁ'), cols=CR, noti=dict(gio='02:14', ngay='Thứ Hai', items=[
        ('Giá vàng', 'Bảng giá', 'Vàng thế giới giảm thêm 1,2% trong đêm', R_),
        ('Tìm kiếm', 'Lịch sử', '"giá vàng bao giờ lên lại"', V_)]),
      say=("Những đêm sau đó, bạn ngủ không yên. Hai giờ sáng, bạn vẫn cầm điện thoại, mở bảng giá vàng thế giới, rồi gõ vào ô tìm kiếm: giá vàng bao giờ lên lại. "
           "Ai đã từng cầm một khoản lỗ lớn sẽ hiểu cảm giác này. Tiền chưa mất hẳn, vì vàng vẫn nằm trong két. Nhưng mỗi ngày nó lại mỏng đi một chút, và bạn không biết phải làm gì.")),
 dict(k='chat', cap=('"SAO EM KHÔNG', 'HỎI ANH TRƯỚC?"'), cols=CR, chat=dict(ten='Anh Tùng – chồng', tv='Đang hoạt động', gio='22:05', mau=X_, msgs=[
        ('Anh Tùng', 'Sổ tiết kiệm đâu rồi em? Ngân hàng nhắn tất toán trước hạn'),
        ('me', 'Em mua vàng rồi anh, tháng 3, cả xóm mua'),
        ('Anh Tùng', 'Một tỷ? Sao em không hỏi anh trước?')]),
      say=("Rồi đến cuộc nói chuyện bạn sợ nhất. Chồng bạn nhắn: sổ tiết kiệm đâu rồi em, sao ngân hàng báo tất toán trước hạn? Bạn đành kể thật: em mua vàng rồi anh, hồi tháng ba, cả xóm cùng mua. "
           "Anh nhắn lại đúng một câu: một tỷ? Sao em không hỏi anh trước? Khoản lỗ không chỉ nằm trên bảng giá. Nó nằm cả trong bữa cơm tối hôm đó.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='bignum', ch='Chương 3 – Con số thật', anh='ov:gold bars||gold bullion', cap=('TỪ ĐỈNH 13/3', 'ĐẾN 11/11/2026'), cols=CR, moc=True, value=-24.2, fmt='{:,.1f}', unit='%', top='GIÁ VÀNG MIẾNG BÁN RA', sub='184,82 xuống 140,02 triệu đồng/lượng', col=RED,
      say=("Đây là con số thật. Tuần cao nhất là ngày mười ba tháng ba, giá vàng miếng bán ra một trăm tám mươi tư phẩy tám triệu đồng một lượng. Đến ngày mười một tháng mười một, còn một trăm bốn mươi triệu. Tức là giảm hai mươi bốn phẩy hai phần trăm. "
           "Một tỷ mua ở đỉnh, tính theo giá bán ra hôm nay chỉ còn khoảng bảy trăm năm mươi bảy triệu. Nếu bán lại cho tiệm theo giá mua vào, còn thấp hơn nữa.")),
 dict(k='cards', anh='ov:gold bars||gold bullion', cap=('CÙNG LÀ VÀNG', 'MUA LÚC NÀO MỚI QUAN TRỌNG'), cols=CC, moc=True,
      cards=[('+66%', 'Mua cuối 2024 (84,2 triệu)', 'vẫn lãi lớn'), ('−8%', 'Mua cuối 2025 (152,8 triệu)', 'đang lỗ'), ('−24%', 'Mua đỉnh tháng 3/2026', 'lỗ nặng nhất')],
      say=("Nhưng khoan vội trách vàng. Người mua cuối năm 2024 với giá tám mươi tư triệu, hôm nay vẫn lãi khoảng sáu mươi sáu phần trăm. Người mua cuối năm 2025, đang lỗ khoảng tám phần trăm. "
           "Còn người mua đúng tuần đỉnh, lỗ hai mươi tư phần trăm. Cùng một tài sản, cùng một năm, kết quả khác nhau hoàn toàn chỉ vì thời điểm mua. Và thời điểm tệ nhất thường là lúc cả xóm cùng xếp hàng.")),
 dict(k='cards', ch='Chương 4 – Vàng lên xuống vì ai?', anh='ov:gold bullion||gold bars', cap=('VÀNG THẾ GIỚI', 'QUY ĐỔI – TRIỆU ĐỒNG/LƯỢNG'), cols=CC, moc=True,
      cards=[('82,3', 'Cuối năm 2024', ''), ('169,0', 'Cuối tháng 2/2026 – đỉnh', ''), ('126,6', 'Ngày 11/11/2026', '−25% từ đỉnh')],
      say=("Vậy vì sao giá vàng lên rồi lại xuống? Câu trả lời không nằm ở tiệm vàng đầu ngõ, mà ở thị trường thế giới. Giá vàng thế giới quy ra tiền Việt, cuối năm 2024 chỉ khoảng tám mươi hai triệu một lượng. "
           "Cuối tháng hai năm 2026, nó lên đỉnh khoảng một trăm sáu mươi chín triệu, tức khoảng năm nghìn hai trăm bảy mươi tám đô la một ounce. Đến hôm nay, mười một tháng mười một, còn khoảng một trăm hai mươi sáu triệu, giảm chừng một phần tư. "
           "Vàng trong nước đi theo đúng nhịp đó. Bạn và chị Thu, dù xếp hàng sớm đến đâu, cũng không quyết được giá vàng ngày mai.")),
 dict(k='cards', anh='ov:gold jewelry shop||gold bars', cap=('TIỀN CHÊNH', 'BẠN TRẢ MÀ KHÔNG THẤY'), cols=CR, moc=True,
      cards=[('~2 tr', 'Cuối 2024: SJC cao hơn thế giới', 'mỗi lượng'), ('~19 tr', 'Ngày 13/3/2026', 'mỗi lượng'), ('~3 tr', 'Chênh giá mua – bán tại tiệm', 'mỗi lượng')],
      say=("Còn một khoản nữa ít ai để ý. Cuối năm 2024, vàng miếng trong nước chỉ đắt hơn giá thế giới quy đổi khoảng hai triệu một lượng. Nhưng đúng ngày mười ba tháng ba, khi cả xóm xếp hàng, khoảng chênh đó lên tới khoảng mười chín triệu một lượng. "
           "Nghĩa là trong một tỷ bạn bỏ ra, khoảng một phần mười là tiền trả thêm cho cơn sốt, chứ không phải cho vàng. Chưa kể khi bán lại, tiệm mua vào thấp hơn giá bán ra khoảng ba triệu một lượng. "
           "Lúc đám đông càng hăng, cái giá phụ này càng đắt.")),
 dict(k='bignum', anh='ov:piggy bank coins||savings coins', cap=('NẾU ĐỂ YÊN', 'TRONG SỔ TIẾT KIỆM'), cols=CR, moc=True, value=295, fmt='{:,.0f}', unit=' triệu', top='CHÊNH LỆCH SAU 8 THÁNG', sub='Tiết kiệm ~1.036 tr · Vàng ~741 tr', col=RED,
      say=("Thử làm một phép so sánh. Nếu một tỷ đó cứ nằm yên trong sổ tiết kiệm mười hai tháng, lãi khoảng năm phẩy bốn phần trăm một năm, sau tám tháng bạn có khoảng một tỷ không trăm ba mươi sáu triệu. "
           "Còn năm phẩy bốn lượng vàng, nếu bán lại cho tiệm hôm nay theo giá mua vào khoảng một trăm ba mươi bảy triệu, bạn nhận về khoảng bảy trăm bốn mươi mốt triệu. Hai con đường, chênh nhau gần ba trăm triệu, chỉ vì một buổi sáng xếp hàng.")),
 dict(k='cards', ch='Chương 5 – Năm 2011 từng như thế', anh='ov:gold bars||gold bullion', cap=('CƠN SỐT VÀNG 2011', 'TRIỆU ĐỒNG/LƯỢNG'), cols=CC, moc=True,
      cards=[('~49', 'Tháng 9/2011 – đỉnh cơn sốt', ''), ('35,1', 'Cuối năm 2013', ''), ('>50', 'Tháng 7/2020', 'gần 9 năm sau')],
      say=("Chuyện này không mới. Tháng chín năm 2011, cả nước cũng sốt vàng. Vàng miếng lên gần năm mươi triệu một lượng, vàng thế giới lập kỷ lục hơn một nghìn chín trăm hai mươi đô la một ounce. "
           "Rồi giá rơi. Cuối năm 2013, vàng miếng còn khoảng ba mươi lăm triệu. Người mua đúng đỉnh năm 2011 phải chờ đến tháng bảy năm 2020, gần chín năm sau, giá mới vượt lại mốc năm mươi triệu. "
           "Chín năm. Đủ để một đứa trẻ vào lớp một rồi lên cấp hai. Vàng giữ giá về lâu dài là đúng, nhưng lâu dài có thể dài hơn rất nhiều so với điều bạn chờ được.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='checklist', ch='Chương 6 – Vì sao người cẩn thận vẫn mua đỉnh?', anh='ov:crowd queue||people waiting line', cap=('3 CÁI BẪY', 'KHI MUA THEO ĐÁM ĐÔNG'), cols=CC, moc=True,
      items=[('Thấy giá tăng nhanh nên nghĩ còn tăng tiếp – mua vì sợ lỡ', RED),
             ('Rút tiền tiết kiệm, dồn hết một lần, không chia nhỏ', RED),
             ('Không có kế hoạch nếu giá giảm 20%: bán, giữ hay mua thêm?', RED)],
      say=("Vì sao một người vốn cẩn thận, cả đời gửi tiết kiệm, lại mua đúng đỉnh? Mình thấy có ba cái bẫy. Một: thấy giá tăng nhanh nên tin nó còn tăng tiếp, mua vì sợ lỡ chứ không vì cần. "
           "Hai: rút hết tiết kiệm, dồn một lần, không chia nhỏ theo thời gian. Ba: không có kế hoạch cho tình huống giá giảm hai mươi phần trăm, nên đến lúc cần tiền thì phải bán đúng lúc thấp.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='cards', ch='Chương 7 – Tích sản đúng cách', anh='ov:calendar coins||coins stack', cap=('CÙNG 1 TỶ, CÙNG NĂM 2026', 'GIÁ TRỊ HÔM NAY'), cols=CC, moc=True,
      cards=[('~741 tr', 'Mua 1 lần ngày 13/3', 'lỗ ~26%'), ('~876 tr', 'Chia đều 10 tháng, T1–T10', 'lỗ ~12%'), ('~1.036 tr', 'Để trong sổ tiết kiệm', 'lãi ~4%')],
      say=("Giờ thử nhìn một người hàng xóm khác, chị Hạnh. Chị cũng có một tỷ, nhưng không xếp hàng. Chị chia đều, mỗi tháng mua một ít, từ tháng một đến tháng mười năm 2026. "
           "Em ước tính theo giá vàng miếng cuối mỗi tháng: đến hôm nay, số vàng của chị Hạnh bán lại được khoảng tám trăm bảy mươi sáu triệu. Chị vẫn lỗ khoảng mười hai phần trăm, vì cả năm nay vàng đi xuống. "
           "Nhưng lỗ chỉ bằng một nửa so với người mua một lần đúng đỉnh. Chia nhỏ không giúp bạn luôn có lãi. Nó giúp bạn không bao giờ dồn hết tiền vào đúng ngày tệ nhất.")),
 dict(k='checklist', anh='ov:gold coins||coins stack', cap=('4 NGUYÊN TẮC', 'TRƯỚC KHI MUA VÀNG TÍCH SẢN'), cols=CC, moc=True,
      items=[('Chia nhỏ, mua đều mỗi tháng – không dồn một lần', GREEN),
             ('Chỉ dùng tiền nhàn rỗi 3–5 năm, giữ riêng quỹ dự phòng', GREEN),
             ('Vàng là một phần, không phải toàn bộ tài sản', GREEN),
             ('Xếp hàng càng dài – càng nên chậm lại', GOLD)],
      say=("Nếu muốn tích sản bằng vàng, mình gợi ý bốn nguyên tắc. Một: chia nhỏ, mua đều mỗi tháng, đừng dồn một lần. Hai: chỉ dùng tiền nhàn rỗi ba đến năm năm, và luôn giữ riêng một quỹ dự phòng cho học phí, viện phí. "
           "Ba: vàng chỉ nên là một phần trong tài sản, bên cạnh tiết kiệm, cổ phiếu hay chứng chỉ quỹ. Và bốn: hàng người xếp càng dài, bạn càng nên chậm lại một nhịp.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối', cap=('"LẦN SAU', 'MÌNH MUA ĐỀU THÔI CHỊ"'), cols=CC, moc=True, chat=dict(ten='Chị Thu – hàng xóm', tv='Đang hoạt động', gio='21:10', mau=V_, msgs=[
        ('Chị Thu', 'Lỗ hơn 40 triệu một lượng rồi em ơi'),
        ('me', 'Em cũng thế. Lần sau mình mua đều mỗi tháng thôi chị'),
        ('Chị Thu', 'Ừ, không xếp hàng nữa')]),
      say=("Tối đó chị Thu nhắn riêng: lỗ hơn bốn mươi triệu một lượng rồi em ơi. Bạn trả lời: em cũng thế. Lần sau mình mua đều mỗi tháng thôi chị. "
           "Chị Thu gửi lại đúng một câu: ừ, không xếp hàng nữa.")),
 dict(k='end', cap=('BẠN ĐÃ TỪNG MUA', 'VÀNG LÚC ĐANG SỐT CHƯA?'), cols=CC,
      say=("Bạn hay người nhà đã từng mua vàng giữa cơn sốt chưa? Giờ đang lãi hay lỗ? Kể ở phần bình luận nhé, và gửi video này cho người đang định xếp hàng mua vàng.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vì Sao Thật Tệ Khi Mua Vàng Lúc Cả Xóm Xếp Hàng: 1 Tỷ Còn 757 Triệu Sau 8 Tháng'
MT = ("Tháng 3/2026, cả xóm xếp hàng mua vàng ở giá gần 185 triệu/lượng. Tám tháng sau, giá còn 140 triệu. Một tỷ mua đúng đỉnh chỉ còn khoảng 757 triệu. Vì sao người cẩn thận nhất cũng mua đúng đỉnh, và tích sản bằng vàng thế nào cho đúng?\n\n"
      "Câu chuyện giả định, giá vàng là số thật (vàng miếng bán ra, nghìn đồng/lượng, giá cuối tuần – tổng hợp WiData):\n"
      "• 31/12/2024: 84.220 · 31/12/2025: 152.820 · 13/3/2026: 184.820 (cao nhất các tuần năm 2026)\n"
      "• 31/5/2026: 159.020 · 29/8/2026: 148.720 · 11/11/2026: 140.020 (−24,2% từ đỉnh)\n"
      "• Vàng thế giới quy đổi: cuối 2024 ~82,3 tr · cuối 2/2026 ~169,0 tr · 11/11/2026 ~126,6 tr/lượng\n"
      "• SJC mua vào 11/11/2026: 137.000 · tiết kiệm 12 tháng ~5,4%/năm\n"
      "• Mua chia đều T1–T10/2026: ước tính theo giá cuối tháng (giá bán ≈ giá mua vào + 2,5 triệu)\n"
      "• Năm 2011: vàng miếng gần 50 tr (9/2011), cuối 2013 ~35,1 tr, vượt lại 50 tr tháng 7/2020\n\n"
      "Kênh chính: https://www.youtube.com/@chungkhoanhuynguyen\nTìm hiểu kênh tích sản minh bạch: https://chungkhoanhuynguyen.com\n\n"
      "Nhân vật là hư cấu. Chia sẻ góc nhìn, không phải tư vấn tài chính.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen6', seri='Vì sao thật tệ khi…', ngay='2026-11-13', gio_goi_y='20:00', gio='20:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['giá vàng', 'mua vàng', 'vàng miếng', 'giá vàng giảm', 'tích sản vàng', 'có nên mua vàng', 'vàng 2026', 'vì sao thật tệ khi'],
    bia_hook=['1 TỶ MUA VÀNG', 'CÒN 757 TRIỆU'], badge='VÌ SAO THẬT TỆ KHI…',
    bia_anh='ov:gold bars||gold bullion',
    bia_hook_b=['MUA ĐÚNG ĐỈNH', 'MẤT 24%'], badge_b='VÀNG 2026',
    bia_hook_c=['CẢ XÓM XẾP HÀNG', 'RỒI SAO?'], badge_c='VÌ SAO THẬT TỆ KHI…',
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh phụ @chungkhoanhuynguyen6 – thử khuôn 'Vì sao thật tệ khi' – vàng (QL1 11/11/2026).\n"
    "XH_BAN = True; NO_CTA = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), len(TIEU))
sys.path.insert(0, '/tmp/cw/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
