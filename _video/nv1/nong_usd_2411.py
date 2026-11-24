# -*- coding: utf-8 -*-
# NV1B 24/11/2026 – VIDEO NÓNG kênh chính: giá USD ngân hàng vượt 26.000 đồng, tỷ giá trung tâm lên kỷ lục 25.668 (23/11/2026)
#   – cú lật: giá USD ở ngân hàng vẫn RẺ HƠN đầu năm; đầu năm ngân hàng bán đúng mức trần, nay còn cách trần hơn 900 đồng; năm 2022 NHNN phải bán 22 tỷ USD, nay đang tìm mua vào.
# KEY NONG2411A. Khác NONG2211A (OMO hút ròng, phiên mua USD đầu tiên) – góc này: giá USD người dân mua, so đầu năm, so 2022, ai có khoản chi bằng USD.
# Nguồn:
#  - VnExpress 23/11/2026 13:08 "Tỷ giá trung tâm lập kỷ lục mới": trung tâm 25.668 (+9), cao nhất từ trước đến nay; Vietcombank sáng 23/11 25.620–26.030 (+50);
#    USD ngân hàng tăng hơn 300 đồng trong 2 tuần, vượt 26.000 sau gần 3,5 tháng giảm liên tục; giá USD ngân hàng thấp hơn khoảng 1,3% so đầu năm;
#    NHNN từ giữa tháng 11 quay lại mua USD giao ngay 25.500; DXY 103,7; Techcombank: tỷ giá ổn định đến cuối năm quanh 25.600, kiều hối + FDI cuối năm bổ sung nguồn cung.
#  - Dân trí 23/11/2026 14:24: giá bán cao nhất 26.030; sàn 24.385, trần 26.951 (biên độ 5%); 93% khả năng Fed tăng 0,25 điểm % tại họp 8–9/12 (lên 4–4,25%).
#  - Thị trường Tài chính Tiền tệ 23/11/2026: trần 26.951; Vietcombank 9h 25.610–26.020; bán thấp nhất 26.000, cao nhất 26.037.
#  - Thời báo Tài chính VN 24/11/2026 07:56: USD tự do quanh 26.250–26.290; DXY 104,32 – cao nhất từ 4/2025.
#  - Thương hiệu & Công luận 2/1/2026: trung tâm 25.121; Vietcombank 26.047–26.377.
#  - The Leader 17/10/2022: NHNN nới biên độ từ ±3% lên ±5% từ 17/10/2022.
#  - VnExpress 24/10/2022: Vietcombank 24.575–24.885; USD ngân hàng tăng hơn 8,5% so đầu năm 2022; Sở Giao dịch NHNN bán 24.870.
#  - VietTimes 14/11/2022 (ACBS ước tính, tính đến 11/2022): NHNN bán khoảng 22 tỷ USD dự trữ năm 2022 (≈21% dự trữ cuối 2021), còn khoảng 87 tỷ USD.
# SỐ TỰ TÍNH: 25.121 × 1,05 = 26.377 → đầu năm Vietcombank bán đúng mức trần. 26.951 − 26.030 = 921 đồng cách trần. 25.668 − 25.121 = 547 đồng (+2,2%).
#   26.030/26.377 = 0,987 → rẻ hơn khoảng 1,3% (khớp VnExpress). Khoản học phí 10.000 USD là GIẢ ĐỊNH: đầu năm 263,77 triệu; 23/11 260,3 triệu; rẻ hơn 3,47 triệu.
#   Nếu giá bán lên tới trần 26.951: 269,51 triệu → thêm 9,21 triệu. (Bỏ kịch bản +8,5% vì vượt trần hiện tại – thám tử 24/11.)
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261124_0815_nong'
KEY = 'NONG2411A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
BX = 'ov:Bitexco Financial Tower||Bitexco Financial Tower'
NT = 'ov:Nhat Tan Bridge||Nhat Tan Bridge'
CON = 'ov:Container ship||Container ship'
SGD = 'ov:Ho Chi Minh City Stock Exchange||Ho Chi Minh City Stock Exchange'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', short=True, cap=('TỶ GIÁ LÊN KỶ LỤC', 'GIÁ ĐÔ NGÂN HÀNG VƯỢT 26.000'), cols=CR, noti=dict(gio='07:30', ngay='Thứ Ba', items=[
        ('Tin tức', 'Tỷ giá', 'Tỷ giá trung tâm lên kỷ lục, giá USD ngân hàng vượt 26.000 đồng', R_),
        ('Minh', 'Tin nhắn', 'Mẹ ơi, tháng 1 con đóng 10.000 đô học phí nha mẹ', X_)]),
      say=("Bảy giờ rưỡi sáng nay, chị Hạnh ở Hà Nội mở điện thoại và thấy một tin từ hôm qua. Giá đô la Mỹ bán ra ở ngân hàng đã vượt hai mươi sáu nghìn đồng, và giá mốc của Nhà nước, gọi là tỷ giá trung tâm, lên mức cao nhất từ trước đến nay. "
           "Ngay dưới là tin nhắn của con trai chị, Minh, đang du học: mẹ ơi, tháng một con đóng mười nghìn đô học phí nha mẹ. "
           "Kể cả nhà anh chị không có ai du học, giá đô vẫn chạm tới giá hàng nhập mà nhà mình mua mỗi ngày.")),
 dict(k='bignum', anh=TP, cap=('TỶ GIÁ TRUNG TÂM', 'CAO NHẤT TỪ TRƯỚC ĐẾN NAY'), cols=CR, value=25668, fmt='{:,.0f}', unit=' đồng', top='TỶ GIÁ TRUNG TÂM NGÀY 23/11/2026', sub='Cao nhất từ trước đến nay (VnExpress 23/11/2026)', col=RED,
      say=("Tỷ giá trung tâm là giá mốc mà Ngân hàng Nhà nước công bố mỗi sáng. Chị không mua đô theo giá này, nhưng ngân hàng phải dựa vào nó. Ngân hàng chỉ được bán đô cao hơn giá mốc tối đa năm phần trăm, giống như một cái trần. "
           "Hôm qua, giá mốc này là hai mươi lăm nghìn sáu trăm sáu mươi tám đồng, cao nhất từ trước đến nay. Nghe chữ kỷ lục, chị Hạnh giật mình. Nhưng khi mở cuốn sổ đổi tiền, chị thấy một chuyện ngược hẳn.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Kỷ lục mà lại rẻ hơn?', short=True, cap=('10.000 ĐÔ HỌC PHÍ', 'RẺ HƠN ĐẦU NĂM GẦN 3,5 TRIỆU'), cols=CC, moc=True, giay=dict(tieu_de='SỔ ĐỔI TIỀN CỦA CHỊ HẠNH', so='Giá bán Vietcombank. Em giả định khoản 10.000 USD', dau='GIẢ ĐỊNH', dieu=[
        ('Đầu năm (sáng 2/1): 26.377 đồng.', 'GIÁ BÁN'),
        ('10.000 đô lúc đó: 263,77 triệu.', 'ĐẦU NĂM'),
        ('Sáng 23/11: 26.030 đồng.', 'GIÁ BÁN'),
        ('10.000 đô bây giờ: 260,3 triệu.', 'RẺ HƠN')]),
      say=("Em giả định chị cần mười nghìn đô cho học phí. Theo giá một ngân hàng lớn niêm yết sáng hai tháng một, mười nghìn đô tốn gần hai trăm sáu mươi tư triệu đồng. "
           "Theo giá sáng hai mươi ba tháng mười một, chỉ còn khoảng hai trăm sáu mươi triệu. Tức là đổi bây giờ còn rẻ hơn đầu năm gần ba triệu rưỡi đồng.")),
 dict(k='chat', cap=('"KỶ LỤC MÀ SAO', 'ĐỔI LẠI RẺ HƠN HẢ ANH?"'), cols=CR, moc=True, chat=dict(ten='Anh Tâm', tv='Đang hoạt động', gio='08:00', mau=V_, msgs=[
        ('me', 'Báo nói tỷ giá kỷ lục mà sao em đổi lại rẻ hơn đầu năm hả anh?'),
        ('Anh Tâm', 'Kỷ lục là giá mốc, còn em mua theo giá ngân hàng'),
        ('Anh Tâm', 'Đầu năm ngân hàng bán đúng trần rồi')]),
      say=("Chị nhắn hỏi anh trai, anh Tâm, người làm nhập khẩu hàng chục năm: báo nói kỷ lục mà sao em đổi lại rẻ hơn? "
           "Anh Tâm trả lời: cái lên kỷ lục là giá mốc của Ngân hàng Nhà nước. Còn em mua theo giá ngân hàng bán ra. Mà đầu năm nay, ngân hàng đã bán đúng bằng trần rồi.")),
 dict(k='cards', anh=BX, cap=('ĐẦU NĂM BÁN ĐÚNG TRẦN', 'NAY CÒN CÁCH TRẦN 921 ĐỒNG'), cols=CC, moc=True,
      cards=[('26.377 đồng', 'Giá bán đầu năm', 'ĐÚNG TRẦN'), ('26.951 đồng', 'Trần hôm 23/11', 'GIÁ MỐC + 5%'), ('26.030 đồng', 'Giá bán sáng 23/11', 'CÁCH TRẦN 921')],
      say=("Đây là cú lật đầu tiên. Đầu năm, giá ngân hàng bán ra đúng bằng giá mốc cộng năm phần trăm, tức là đã chạm trần, không được bán cao hơn nữa. "
           "Bây giờ giá mốc cao hơn, nên trần cũng cao hơn, gần hai mươi bảy nghìn đồng, và giá ngân hàng bán vẫn cách trần hơn chín trăm đồng. "
           "Với túi tiền của chị, điều này nghĩa là: giá chị trả vẫn thấp hơn đầu năm. Nhưng cách trần chín trăm đồng cũng có nghĩa là giá vẫn còn chỗ để lên thêm.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='noti', ch='Chương 2 – Vì sao đô tăng lại?', cap=('2 TUẦN TĂNG HƠN 300 ĐỒNG', 'SAU GẦN 3,5 THÁNG GIẢM'), cols=CR, moc=True, noti=dict(gio='09:00', ngay='Thứ Ba', items=[
        ('Tin tức', 'Tỷ giá', 'USD ngân hàng tăng hơn 300 đồng trong 2 tuần', R_),
        ('Tin tức', 'Thế giới', 'Chỉ số đồng USD lên cao nhất từ tháng 4/2025', V_)]),
      say=("Dù vậy, chiều đi lên là có thật. Theo VnExpress, chỉ trong hai tuần, giá đô ở ngân hàng tăng hơn ba trăm đồng, vượt mốc hai mươi sáu nghìn sau gần ba tháng rưỡi giảm liên tục. "
           "Theo các báo, phần lớn lực đẩy đến từ nước Mỹ.")),
 dict(k='bignum', anh=NT, cap=('THỊ TRƯỜNG ĐẶT 93%', 'FED TĂNG LÃI THÁNG 12'), cols=CR, moc=True, value=93, fmt='{:,.0f}', unit='%', top='KHẢ NĂNG FED TĂNG LÃI SUẤT HỌP 8–9/12', sub='Theo kỳ vọng của thị trường (Dân trí 23/11/2026)', col=RED,
      say=("Fed là ngân hàng trung ương của Mỹ, nơi quyết định lãi suất của đồng đô. Theo Dân trí, thị trường đang đặt khoảng chín mươi ba phần trăm khả năng Fed tăng lãi suất trong cuộc họp ngày tám và chín tháng mười hai. "
           "Khi mọi người chờ lãi đô tăng, tiền khắp thế giới kéo về đồng đô. Ai cũng muốn cầm đô thì đô thành hàng được săn, nên ở nước mình giá đô cũng nhích lên.")),
 dict(k='cards', anh=TP, cap=('3 GIÁ ĐÔ', 'CÙNG MỘT TỜ ĐÔ'), cols=CC, moc=True,
      cards=[('25.668 đồng', 'Giá mốc NHNN 23/11', 'KỶ LỤC'), ('26.030 đồng', 'Ngân hàng bán ra 23/11', 'VƯỢT 26.000'), ('26.290 đồng', 'Điểm thu đổi tự do 24/11', 'CAO HƠN NGÂN HÀNG')],
      say=("Cùng một tờ đô, có ba mức giá. Giá mốc của Ngân hàng Nhà nước. Giá ngân hàng bán ra. Và giá ở các điểm thu đổi bên ngoài, sáng nay quanh hai mươi sáu nghìn ba trăm đồng, cao hơn giá ngân hàng hôm qua. "
           "Với người cần đô thật sự để đóng học phí, như chị Hạnh, giá đáng nhìn nhất là giá ngân hàng bán ra.")),
 dict(k='chat', cap=('"VẬY CÓ GIỐNG', 'NĂM 2022 KHÔNG ANH?"'), cols=CR, moc=True, chat=dict(ten='Anh Tâm', tv='Đang hoạt động', gio='12:00', mau=V_, msgs=[
        ('me', 'Vậy có giống năm 2022 không anh?'),
        ('Anh Tâm', 'Năm đó anh nhớ mãi, để tối anh gọi kể'),
        ('Anh Tâm', 'Nhưng có một chỗ khác hẳn')]),
      say=("Chị hỏi anh Tâm: vậy có giống năm hai nghìn không trăm hai mươi hai không? Anh trả lời rằng năm đó anh nhớ mãi, tối nay anh sẽ gọi kể. Nhưng có một chỗ khác hẳn.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước là năm 2022', cap=('"NĂM ĐÓ ANH ĐỔI ĐÔ', 'MÀ GIÁ LÊN TỪNG TUẦN"'), cols=CC, moc=True, call=dict(ten='Anh Tâm', phu='Anh trai', mau=V_, loi=[
        'Năm đó giá đô lên từng tuần', 'Ngân hàng bán kịch trần']),
      say=("Tối nay anh Tâm gọi điện. Anh kể: mùa thu năm đó, giá đô lên gần như từng tuần. Lô hàng nhập của anh phải trả bằng đô, mà ngân hàng thì bán kịch trần. "
           "Tháng mười năm đó, Ngân hàng Nhà nước phải nâng cái trần lên: ngân hàng được bán cao hơn giá mốc năm phần trăm, thay vì ba phần trăm như trước. Trần bị nâng vì giá đã đội tới nóc.")),
 dict(k='giay', cap=('NĂM 2022', 'NHỮNG CON SỐ CỦA LẦN TRƯỚC'), cols=CC, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='The Leader 17/10/2022, VnExpress 24/10/2022, VietTimes 14/11/2022', dau='2022', dieu=[
        ('17/10/2022: trần từ 3% lên 5%.', 'NÂNG TRẦN'),
        ('24/10/2022: ngân hàng bán 24.885.', 'KỊCH TRẦN'),
        ('Đô ngân hàng tăng hơn 8,5%.', 'SO ĐẦU NĂM'),
        ('NHNN bán khoảng 22 tỷ USD.', 'ACBS ƯỚC TÍNH')]),
      say=("Những con số của lần trước. Theo VnExpress, cuối tháng mười năm đó, giá đô ngân hàng lên kịch trần, cao hơn đầu năm hơn tám phẩy năm phần trăm. "
           "Nhà nước có một quỹ dự trữ ngoại tệ, giống như một cái két đô để dành. Báo VietTimes dẫn ước tính của một công ty chứng khoán: năm đó, Ngân hàng Nhà nước đã lấy ra bán khoảng hai mươi hai tỷ đô la Mỹ để hạ nhiệt giá.")),
 dict(k='bignum', anh=BX, cap=('NĂM ĐÓ NHNN BÁN ĐÔ RA', 'NAY ĐẶT LỆNH MUA VÀO'), cols=CC, moc=True, value=25500, fmt='{:,.0f}', unit=' đồng', top='GIÁ NHNN ĐẶT MUA USD TỪ GIỮA THÁNG 11/2026', sub='Năm 2022: bán khoảng 22 tỷ USD dự trữ (ACBS ước tính)', col=GREEN,
      say=("Và đây là cú lật thứ hai. Năm đó, Ngân hàng Nhà nước phải tung đô ra bán. Còn từ giữa tháng mười một năm nay, theo VnExpress, Ngân hàng Nhà nước lại đặt lệnh mua đô vào, ở giá hai mươi lăm nghìn năm trăm đồng. "
           "Mua được bao nhiêu thì chưa chắc, vì ngân hàng bán đô ra ngoài đang được giá cao hơn mức này. Nhưng người phải bán đô ra để giữ giá, và người muốn gom thêm đô vào, là hai tình thế rất khác nhau.")),
 dict(k='cards', anh=TP, cap=('3 CON SỐ', 'SO VỚI ĐẦU NĂM'), cols=CC, moc=True,
      cards=[('Tăng 8,5%', 'Đô ngân hàng bán 10/2022', 'LẦN TRƯỚC'), ('Giảm 1,3%', 'Đô ngân hàng bán 11/2026', 'GIÁ CHỊ TRẢ'), ('Tăng 2,2%', 'Giá mốc NHNN 2026', 'KHÔNG PHẢI GIÁ MUA')],
      say=("Đặt cạnh nhau cho dễ thấy. Lần trước, giá đô ngân hàng bán ra tăng hơn tám phẩy năm phần trăm so với đầu năm. Năm nay, cũng giá đó lại đang thấp hơn đầu năm khoảng một phẩy ba phần trăm. "
           "Chỉ có giá mốc là nhích lên khoảng hai phẩy hai phần trăm.")),
 dict(k='checklist', anh=HN, cap=('GIỐNG 2, KHÁC 2', 'SO VỚI LẦN TRƯỚC'), cols=CC, moc=True,
      items=[('Giống: đô đi lên nhiều tuần', GOLD), ('Giống: nhà trả bằng đô lo nhất', GOLD), ('Khác: còn cách trần 921 đồng', GREEN), ('Khác: NHNN đặt mua ở 25.500', GREEN)],
      say=("So với lần trước, có hai điểm giống. Giá đô đi lên liền mấy tuần, và người lo nhất vẫn là nhà phải trả bằng đô. "
           "Có hai điểm khác. Giá ngân hàng bán ra còn cách trần hơn chín trăm đồng, không phải kịch trần. Và Ngân hàng Nhà nước đang đặt lệnh mua đô vào, chứ không phải tung đô ra bán. Khác lần trước, nhưng giá đô vẫn có thể tăng tiếp.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='giay', ch='Chương 4 – Nếu giá đô lên tới trần', short=True, cap=('NẾU GIÁ ĐÔ LÊN TỚI TRẦN', '10.000 ĐÔ ĐẮT THÊM 9,2 TRIỆU'), cols=CR, moc=True, giay=dict(tieu_de='PHÉP TÍNH CỦA CHỊ HẠNH', so='Em giả định, theo giá bán 26.030 sáng 23/11', dau='GIẢ ĐỊNH', dieu=[
        ('Theo giá 23/11: 260,3 triệu.', 'BÂY GIỜ'),
        ('Nếu lên tới trần 26.951: 269,5 triệu.', 'NẾU TỚI TRẦN'),
        ('Đắt thêm khoảng 9,2 triệu đồng.', 'CHÊNH'),
        ('Nếu giá đứng yên: không đổi gì.', 'KỊCH BẢN GIỮ')]),
      say=("Chị Hạnh tự làm một phép tính. Em giả định trong thời gian tới, giá đô ngân hàng lên tới trần hiện nay. Mười nghìn đô học phí sẽ đắt thêm khoảng chín triệu hai trăm nghìn đồng. "
           "Muốn đắt như lần trước, giá mốc phải tăng tiếp, hoặc trần phải nâng thêm. Lần trước, chuyện đó mất gần mười tháng. Đây là kịch bản để soi rủi ro, không phải dự báo.")),
 dict(k='cards', anh=CON, cap=('AI CẢM NHẬN RÕ NHẤT', 'KHI ĐÔ TĂNG'), cols=CC, moc=True,
      cards=[('Học phí', 'Nhà có con du học', 'TRẢ BẰNG ĐÔ'), ('Hàng nhập', 'Doanh nghiệp nhập khẩu', 'CHI PHÍ TĂNG'), ('Tiền gửi về', 'Nhà có người thân ở nước ngoài', 'ĐỔI ĐƯỢC NHIỀU HƠN')],
      say=("Không phải ai cũng chịu tác động như nhau. Nhà có con du học, hay doanh nghiệp nhập hàng, phải trả bằng đô, nên đô tăng là chi phí tăng. "
           "Ngược lại, nhà có người thân ở nước ngoài gửi tiền về thì đổi được nhiều tiền Việt hơn. "
           "Còn nếu nhà mình chỉ gửi tiết kiệm bằng tiền đồng và không có khoản nào phải trả bằng đô, thì tác động chủ yếu là gián tiếp, qua giá những món hàng nhập khẩu.")),
 dict(k='noti', anh=SGD, cap=('DỰ BÁO CỦA MỘT NGÂN HÀNG', 'TỶ GIÁ ỔN ĐỊNH ĐẾN CUỐI NĂM'), cols=CC, moc=True, noti=dict(gio='15:00', ngay='Thứ Ba', items=[
        ('VnExpress 23/11', 'Dự báo', 'Techcombank: tỷ giá ổn định đến cuối năm', G_),
        ('VnExpress 23/11', 'Nguồn đô', 'Cuối năm: tiền kiều bào gửi về, vốn nước ngoài bổ sung nguồn đô', V_)]),
      say=("Cũng có góc nhìn bớt lo hơn. Theo nhóm phân tích của Techcombank, tỷ giá sẽ ổn định đến cuối năm. Lý do là cuối năm, tiền kiều bào gửi về và vốn nước ngoài vào mở nhà máy sẽ bổ sung nguồn đô. "
           "Nhưng đó là dự báo, và học phí của Minh đóng vào tháng một. Không ai biết chắc.")),
 dict(k='cards', ch='Chương 5 – Ba con đường của chị Hạnh', anh=HN, cap=('3 CON ĐƯỜNG', 'CHO KHOẢN HỌC PHÍ THÁNG 1'), cols=CC, moc=True,
      cards=[('Đổi hết ngay', 'Chốt một mức giá', 'THIỆT NẾU GIÁ GIẢM'), ('Đổi dần', 'Chia vài đợt tới tháng 1', 'GIÁ TRUNG BÌNH'), ('Chờ sát ngày', 'Đợi giá giảm lại', 'THIỆT NẾU GIÁ TĂNG')],
      say=("Chị Hạnh thấy có ba con đường. Một, đổi hết ngay để chốt một mức giá. Không phải lo giá lên, nhưng nếu giá giảm lại thì thiệt. "
           "Hai, đổi dần thành vài đợt từ nay tới tháng một, để được giá trung bình. "
           "Ba, chờ sát ngày đóng tiền. Cách này được nếu giá giảm, nhưng thiệt nếu giá tăng. Mua đô ở ngân hàng để đóng học phí cần giấy tờ chứng minh mục đích. Mỗi nhà mỗi hoàn cảnh, video không khuyến nghị mua hay giữ ngoại tệ.")),
 dict(k='chat', cap=('"MẸ ĐỔI TRƯỚC MỘT NỬA', 'NỬA CÒN LẠI ĐỔI DẦN"'), cols=CC, moc=True, chat=dict(ten='Minh', tv='Đang hoạt động', gio='21:00', mau=X_, msgs=[
        ('me', 'Mẹ đổi trước một nửa ở ngân hàng nhé con'),
        ('me', 'Nửa còn lại mẹ đổi dần trước tháng 1'),
        ('Minh', 'Dạ, con cảm ơn mẹ')]),
      say=("Tối nay, chị Hạnh nhắn cho con. Mẹ đổi trước một nửa ở ngân hàng. Nửa còn lại mẹ sẽ đổi dần trước tháng một. Minh trả lời: dạ, con cảm ơn mẹ. Đó là lựa chọn riêng của gia đình chị.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='checklist', ch='Chương 6 – Phép thử cho túi tiền nhà mình', anh=TP, cap=('PHÉP THỬ: 12 THÁNG TỚI', 'NHÀ MÌNH CÓ KHOẢN NÀO TRẢ BẰNG ĐÔ?'), cols=CC, moc=True,
      items=[('Không có khoản nào: ít ảnh hưởng', GREEN), ('Có, tiền đủ và dư 10%: khá vững', GOLD), ('Có, tiền vừa sát: tính sớm', RED)],
      say=("Em gợi ý một phép thử tự soi. Trong mười hai tháng tới, nhà mình có khoản nào phải trả bằng đô không, như học phí, hàng nhập, hay khoản vay ngoại tệ? "
           "Nếu không có, giá đô ít ảnh hưởng trực tiếp tới nhà mình. Nếu có, và tiền đã đủ, còn dư thêm khoảng mười phần trăm, đây là mốc em tự chọn để phòng giá lên, thì khá vững. Nếu tiền chỉ vừa sát, đó là lúc nên tính sớm. Đây là mốc tự soi, không phải lời khuyên.")),
 dict(k='checklist', anh=SGD, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI TẾT'), cols=CC, moc=True,
      items=[('Fed họp ngày 8 và 9/12', GOLD), ('Giá bán còn cách trần bao xa', GOLD), ('NHNN mua được bao nhiêu đô', GOLD)],
      say=("Ba điều đáng theo dõi từ nay tới Tết. Cuộc họp của Fed ngày tám và chín tháng mười hai. Giá đô ngân hàng bán ra còn cách trần bao xa. Và Ngân hàng Nhà nước mua vào được bao nhiêu đô. "
           "Muốn hiểu tỷ giá tác động thế nào tới cổ phiếu và túi tiền gia đình, anh chị có thể đọc bài miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"CHỮ KỶ LỤC NGHE SỢ', 'NHƯNG PHẢI NHÌN GIÁ MÌNH TRẢ"'), cols=CC, moc=True, chat=dict(ten='Anh Tâm', tv='Đang hoạt động', gio='22:00', mau=V_, msgs=[
        ('Anh Tâm', 'Chữ kỷ lục nghe thì sợ'),
        ('Anh Tâm', 'Nhưng phải nhìn cái giá mình thật sự trả'),
        ('me', 'Dạ, em hiểu rồi anh')]),
      say=("Mười giờ tối, anh Tâm nhắn thêm một dòng. Chữ kỷ lục nghe thì sợ, nhưng phải nhìn cái giá mình thật sự trả. Chị Hạnh trả lời: dạ, em hiểu rồi anh.")),
 dict(k='end', cap=('12 THÁNG TỚI', 'NHÀ ANH CHỊ CÓ KHOẢN NÀO TRẢ BẰNG ĐÔ?'), cols=CC,
      say=("Còn anh chị, trong mười hai tháng tới, nhà mình có khoản nào phải trả bằng đô không: không có, có và đã đủ tiền, hay có mà tiền còn sát?")),
]
import ql_post; S = ql_post.tach(S, max_tu=50, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Tỷ Giá Kỷ Lục 25.668: Sao Đổi Đô Lại Rẻ Hơn Đầu Năm?'
WEB = 'https://chungkhoanhuynguyen.com/hoc/vi-sao-that-te-khi-om-do-la-luc-ai-cung-so-1-ty-doi-o-gia-28-080-con.html'
MT = ("NÓNG: ngày 23/11/2026, tỷ giá trung tâm lên 25.668 đồng/USD – cao nhất từ trước đến nay; giá USD bán ra ở ngân hàng vượt 26.000 đồng sau 2 tuần tăng hơn 300 đồng. "
      "Nhưng giá USD ngân hàng vẫn thấp hơn đầu năm khoảng 1,3%: đầu năm ngân hàng bán đúng mức trần, nay còn cách trần hơn 900 đồng. Năm 2022 NHNN phải bán khoảng 22 tỷ USD dự trữ (ACBS ước tính); nay NHNN đặt lệnh mua USD vào ở 25.500. "
      "Vì sao đô tăng lại, ai cảm nhận rõ nhất, và phép thử cho túi tiền gia đình.\n\n"
      "Nguồn số liệu:\n"
      "• VnExpress 23/11/2026: tỷ giá trung tâm 25.668 (+9), cao nhất từ trước đến nay; Vietcombank 25.620–26.030; USD ngân hàng tăng hơn 300 đồng trong 2 tuần, vượt 26.000 sau gần 3,5 tháng giảm; thấp hơn khoảng 1,3% so đầu năm; NHNN từ giữa tháng 11 mua USD giao ngay 25.500; Techcombank: tỷ giá ổn định đến cuối năm quanh 25.600, kiều hối và FDI cuối năm bổ sung nguồn cung\n"
      "• Dân trí 23/11/2026: trần 26.951, sàn 24.385 (biên độ 5%); khoảng 93% khả năng Fed tăng 0,25 điểm % tại họp 8–9/12 (lên 4–4,25%)\n"
      "• Thị trường Tài chính Tiền tệ 23/11/2026: trần 26.951; giá bán USD các ngân hàng 26.000–26.037\n"
      "• Thời báo Tài chính Việt Nam 24/11/2026: USD tự do quanh 26.250–26.290; chỉ số DXY 104,32 – cao nhất từ tháng 4/2025\n"
      "• Thương hiệu & Công luận, bản tin 4h30 ngày 2/1/2026: tỷ giá trung tâm 25.121; Vietcombank 26.047–26.377\n"
      "• The Leader 17/10/2022: NHNN nới biên độ tỷ giá từ ±3% lên ±5%; VnExpress 24/10/2022: Vietcombank 24.575–24.885, USD ngân hàng tăng hơn 8,5% so đầu năm; VietTimes 14/11/2022 (ACBS ước tính, tính đến 11/2022): NHNN bán khoảng 22 tỷ USD dự trữ năm 2022\n"
      "• Tự tính: 25.121 × 1,05 = 26.377 (đầu năm bán đúng trần); 26.951 − 26.030 = 921 đồng; 25.668/25.121 ≈ +2,2%; 26.030/26.377 ≈ −1,3% (khớp VnExpress); 26.290 − 26.030 = 260 đồng. Khoản học phí 10.000 USD là GIẢ ĐỊNH: đầu năm 263,77 triệu, 23/11 260,3 triệu (rẻ hơn 3,47 triệu); nếu giá bán lên tới trần 26.951: 269,51 triệu, thêm khoảng 9,2 triệu\n\n"
      "Bài liên quan về giữ đô la: " + WEB + "\n"
      "Cần trao đổi riêng về kế hoạch tài chính: Zalo 0365.188.286\n\n"
      "Nhân vật chị Hạnh, anh Tâm, Minh là hư cấu; số liệu là thật theo nguồn trên.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-24', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['giá USD hôm nay', 'tỷ giá USD', 'tỷ giá hôm nay', 'tỷ giá trung tâm', 'giá đô la', 'tỷ giá Vietcombank', 'Fed tăng lãi suất', 'du học phí', 'tin nóng tài chính', 'tỷ giá 2026'],
    bia_hook=['10.000 ĐÔ', 'RẺ HƠN 3,5 TR'], badge='SO VỚI ĐẦU NĂM',
    bia_anh='Ho Chi Minh City skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['2022 BÁN ĐÔ', 'NAY MUA VÀO'], badge_b='NGÂN HÀNG NHÀ NƯỚC',
    bia_hook_c=['HỌC PHÍ ĐÔ', '+9,2 TRIỆU?'], badge_c='NẾU GIÁ LÊN TỚI TRẦN',
    reel_hook='TỶ GIÁ LÊN KỶ LỤC|MÀ ĐỔI ĐÔ RẺ HƠN ĐẦU NĂM???',
    fb_post=("Tỷ giá trung tâm lên kỷ lục 25.668, giá USD ngân hàng vượt 26.000 💵\n\n👉 Nhưng giá USD ngân hàng vẫn thấp hơn đầu năm khoảng 1,3%\n👉 Đầu năm ngân hàng bán đúng trần, nay còn cách trần hơn 900 đồng\n"
             "👉 Năm 2022 NHNN bán khoảng 22 tỷ USD, nay đặt lệnh mua vào ở 25.500\n\n12 tháng tới, nhà anh chị có khoản nào phải trả bằng đô?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 24/11: giá USD ngân hàng vượt 26.000, tỷ giá trung tâm kỷ lục mà giá đô vẫn rẻ hơn đầu năm (NV1B 24/11/2026).\n"
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
sys.path.insert(0, CW + '/_video'); import kiem_loi, kiem_goi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'):
    for l in kiem_goi.kiem(TIEU, META[KEY][b]): print('kiem_goi', b, l)
try:
    import xung_ho
    for i, c in enumerate(S, 1):
        if xung_ho.le_phep(c['say']) != c['say']: print('XUNG_HO doi canh', i)
except Exception as e: print('xung_ho?', e)
