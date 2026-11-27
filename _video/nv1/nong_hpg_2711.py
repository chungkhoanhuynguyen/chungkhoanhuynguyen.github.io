# -*- coding: utf-8 -*-
# NV1B 27/11/2026 – VIDEO NÓNG kênh chính: cổ phiếu Hòa Phát (HPG) đóng cửa 19.600 đồng ngày 26/11/2026 – thấp nhất kể từ tháng 6/2025 – dù lãi 9 tháng tăng 104%.
#   – cú lật 1: lãi gấp đôi mà giá rơi; P/E chỉ khoảng 6 lần (thấp hơn trung vị 5 năm 13,2).
#   – cú lật 2 (lần trước): quý 1/2022 lãi cổ đông công ty mẹ 8.217 tỷ – đúng bằng quý 3/2026 (8.217 tỷ); tháng 3/2022 P/E cũng khoảng 6,4 – rồi giá mất khoảng 69%, quý 3 và 4/2022 lỗ.
#   – bài học: thị trường trả tiền cho lãi của những năm tới; P/E thấp dựa trên lãi đỉnh chưa chắc là rẻ. Trung lập: không hô mua/bán.
# KEY NONG2711A. Không trùng 7 ngày: NONG2011A nhân sự NH, NONG2211A NHNN, NONG2311B cà phê, NONG2411A tỷ giá, NONG2511A gạo, NONG2611A NOXH;
#   CH2711TQ (QL1, đăng 26/11) nói về đề xuất thuế 35% + tháng 4/2025 → video này chỉ nhắc thuế 1 câu, góc khác (một cổ phiếu lãi tăng vẫn rơi).
# Nguồn:
#  - MarketTimes 26/11/2026 "Cổ phiếu Hòa Phát rơi xuống mức thấp nhất 18 tháng": HPG −2,2% còn 19.600 đ, thấp nhất kể từ 11/6/2025 (19.418, giá điều chỉnh); KL >24 triệu cp;
#    quý 3/2026 doanh thu 62.669 tỷ (+70%), LNST 8.265 tỷ (+106%); 9 tháng doanh thu 171.539 tỷ (+54%), LNST 23.746 tỷ (+104%), vượt 8% kế hoạch lợi nhuận năm; thép 97% doanh thu; "nhà sản xuất thép lớn nhất Đông Nam Á với công suất 16 triệu tấn/năm".
#  - WiData eod_adjust (giá đã điều chỉnh): đóng cửa cao nhất 12 tháng (26/11/2025–26/11/2026) 26.250 → 19.600 = −25,3%; 7/3/2022 26.150 (cao nhất 2022) → 10/11/2022 8.190 = −68,7%; 10/1/2023 13.390.
#  - WiData fs_nonfin (hợp nhất, LNST cổ đông công ty mẹ): Q1/2022 8.216,96 tỷ; Q2/2022 4.032 tỷ; Q3/2022 −1.774 tỷ; Q4/2022 −1.992 tỷ; Q3/2026 8.217,34 tỷ; Q3/2025 3.988 tỷ.
#  - WiData ratio_daily: P/E HPG 26/11/2026 6,03; trung vị 5 năm 13,2; P/E 7/3/2022 6,40 (2–10/3/2022: 5,9–6,4). ACV P/E 10,3.
#  - WiData ai_news 26/11/2026: VN-Index −57,77 điểm (−3,42%) còn 1.629,68; VIC kéo giảm 23,82 điểm; 291 mã giảm/47 tăng; khối ngoại bán ròng từ đầu tháng 10.674 tỷ.
#  - WiData index_ratio_daily 26/11/2026: P/E VN-Index 10,3; trừ nhóm Vingroup 8,8. index_eod 2026: cao nhất 1.927,94.
#  - WiData eod_adjust VIC 12 tháng: thấp nhất 121.600, hiện 230.000 (+89%). foreign_trading_agg HPG 30 phiên (15/10–26/11): khối ngoại mua ròng 197,6 tỷ (tính cả thỏa thuận).
#  - Nhà Đầu Tư 26/11/2026: ACV có lúc 35.200 đ, thấp nhất hơn 6 năm; LNST quý 3/2026 2.083 tỷ (−35,1%).
#  - Báo Cần Thơ (TTXVN) 26/11/2026: USTR đề xuất thuế bổ sung tối đa 35% với hàng Việt Nam, chưa có hiệu lực; điều trần từ 25/1/2027, quyết định muộn nhất 11/3/2027.
# SỐ TỰ TÍNH: 19.600/26.250 − 1 = −25,3%; 8.190/26.150 − 1 = −68,7%; 230.000/121.600 = 1,89; 4.032/8.217 − 1 = −50,9%.
#   Giả định nhân vật anh Khoa: 5.000 cổ phiếu mua 24.000 đ = 120 triệu; nay 19.600 → 98 triệu; tạm lỗ 22 triệu (−18,3%); tiền nhàn rỗi, không vay.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261127_0900_nong'
KEY = 'NONG2711A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
SGD = 'ov:Ho Chi Minh City Stock Exchange||Ho Chi Minh City skyline night'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', short=True, cap=('LÃI GẤP ĐÔI', 'MÀ GIÁ THẤP NHẤT 18 THÁNG?'), cols=CR, noti=dict(gio='15:05', ngay='Thứ Năm 26/11', items=[
        ('Tin tức', 'Chứng khoán', 'VN-Index giảm gần 58 điểm, còn 1.629,68 điểm', R_),
        ('Tin tức', 'Doanh nghiệp', 'Cổ phiếu Hòa Phát rơi xuống mức thấp nhất 18 tháng', R_),
        ('Zalo', 'Vợ', 'Báo nói công ty lãi gấp đôi, sao cổ phiếu anh cứ rơi?', V_)]),
      say=("Anh chị có đang cầm một cổ phiếu mà công ty báo lãi rất tốt, nhưng giá thì cứ đi xuống không? "
           "Kết thúc phiên chiều hôm qua, ngày hai mươi sáu tháng mười một, cổ phiếu Hòa Phát đóng cửa ở mức thấp nhất mười tám tháng. Trong khi đó, nhà sản xuất thép lớn nhất Đông Nam Á này đã báo lãi chín tháng tăng gấp đôi. "
           "Anh Khoa, kỹ sư ở Bắc Ninh, đọc tin xong thì nhận tin nhắn của vợ: báo nói công ty lãi gấp đôi, sao cổ phiếu anh cứ rơi?")),
 dict(k='bignum', anh=SGD, cap=('19.600 ĐỒNG', 'THẤP NHẤT TỪ THÁNG 6/2025'), cols=CR, value=19600, fmt='{:,.0f}', unit=' Đ', top='GIÁ ĐÓNG CỬA CỔ PHIẾU HÒA PHÁT 26/11', sub='Thấp nhất kể từ tháng 6/2025 (MarketTimes 26/11/2026)', col=RED,
      say=("Giá cuối ngày hôm qua là mười chín nghìn sáu trăm đồng mỗi cổ phiếu. Đó là mức thấp nhất kể từ tháng sáu năm ngoái. "
           "So với lúc cao nhất trong mười hai tháng qua, cổ phiếu này đã giảm khoảng hai mươi lăm phần trăm. "
           "Nói dễ hiểu, ai bỏ một trăm triệu đồng ở đỉnh, giờ còn khoảng bảy mươi lăm triệu.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Lãi gấp đôi là thật', short=True, cap=('LÃI 9 THÁNG 23.746 TỶ', 'TĂNG 104%'), cols=CC, moc=True, giay=dict(tieu_de='KẾT QUẢ 9 THÁNG 2026', so='MarketTimes 26/11/2026', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Doanh thu 9 tháng: 171.539 tỷ.', 'TĂNG 54%'),
        ('Lãi sau thuế 9 tháng: 23.746 tỷ.', 'TĂNG 104%'),
        ('Riêng quý 3: lãi 8.265 tỷ.', 'TĂNG 106%'),
        ('Lãi đã vượt 8% kế hoạch cả năm.', 'VƯỢT')]),
      say=("Anh Khoa mở lại kết quả kinh doanh. Chín tháng đầu năm, Hòa Phát lãi sau khi đóng thuế hơn hai mươi ba nghìn bảy trăm tỷ đồng, gấp đôi chín tháng năm ngoái. "
           "Riêng quý ba lãi hơn tám nghìn hai trăm tỷ đồng, cũng gấp đôi. Mới chín tháng mà lãi đã vượt kế hoạch cả năm. "
           "Vậy là công ty không hề làm ăn kém đi. Chuyện lạ nằm ở giá.")),
 dict(k='bignum', anh=TP, cap=('P/E CHỈ KHOẢNG 6 LẦN', '5 NĂM QUA THƯỜNG KHOẢNG 13'), cols=CC, value=6, fmt='{:,.0f}', unit=' LẦN', top='P/E CỔ PHIẾU HÒA PHÁT NGÀY 26/11', sub='Bỏ khoảng 6 đồng mua 1 đồng lãi mỗi năm (WiData, P/E 6,03)', col=GOLD,
      say=("Có một con số người ta hay dùng để xem cổ phiếu đắt hay rẻ, gọi là P/E. Hiểu đơn giản, P/E sáu lần nghĩa là anh chị bỏ ra khoảng sáu đồng để mua một đồng lãi mỗi năm của công ty. "
           "Hôm qua, P/E của Hòa Phát chỉ khoảng sáu lần. Năm năm qua, mức ở giữa là khoảng mười ba lần. "
           "Nhìn con số này, ai cũng dễ nghĩ: rẻ quá rồi.")),
 dict(k='chat', cap=('"RẺ THẾ', 'HAY MUA THÊM ANH?"'), cols=CR, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='19:40', mau=V_, msgs=[
        ('Vợ', 'Lãi gấp đôi mà rẻ thế, hay mua thêm anh?'),
        ('me', 'Anh cũng định thế, nhưng chưa hiểu vì sao giá rơi'),
        ('Vợ', 'Không hiểu thì khoan đã')]),
      say=("Tối đó, vợ anh Khoa nhắn: lãi gấp đôi mà rẻ thế, hay mua thêm anh? "
           "Anh Khoa trả lời rằng anh cũng định thế, nhưng anh chưa hiểu vì sao giá lại rơi. "
           "Chị chỉ nhắn lại một câu: không hiểu thì khoan đã. Và đó là một câu rất đáng giá.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Không chỉ một mình Hòa Phát', anh=SGD, cap=('PHIÊN 26/11', 'CẢ SÀN CÙNG GIẢM'), cols=CR, moc=True,
      cards=[('57,77 điểm', 'VN-Index giảm trong 1 phiên', 'CÒN 1.629,68 ĐIỂM'), ('291 mã', 'Giảm giá, chỉ 47 mã tăng', 'ĐỎ GẦN KÍN SÀN'), ('35%', 'Mức thuế Mỹ đề xuất tối đa', 'CHƯA CÓ HIỆU LỰC')],
      say=("Trước hết, hôm qua không chỉ một mình Hòa Phát giảm. Chỉ số VN-Index, con số đo chung cả sàn chứng khoán, mất gần năm mươi tám điểm, khoảng ba phần trăm rưỡi. Cùng ngày có tin Mỹ đề xuất mức thuế tối đa ba mươi lăm phần trăm với hàng Việt Nam. "
           "Mức thuế này mới là đề xuất, chưa có hiệu lực. Toàn thị trường có hai trăm chín mươi mốt cổ phiếu giảm, chỉ bốn mươi bảy cổ phiếu tăng. "
           "Nghĩa là gió ngược thổi vào gần như mọi cổ phiếu.")),
 dict(k='cards', anh=TP, cap=('CÙNG RƠI', 'NHƯNG KHÁC NHAU'), cols=CC, moc=True,
      cards=[('106%', 'Hòa Phát: lãi quý 3 tăng', 'GIÁ THẤP NHẤT 18 THÁNG'), ('35,1%', 'ACV: lãi quý 3 giảm', 'CÓ LÚC THẤP NHẤT HƠN 6 NĂM'), ('89%', 'VIC: cao hơn đáy 12 tháng', 'GẦN GẤP ĐÔI ĐÁY NĂM')],
      say=("Nhưng nhìn kỹ thì mỗi cổ phiếu rơi một kiểu. Tổng công ty Cảng hàng không, mã ACV, lãi quý ba giảm khoảng ba mươi lăm phần trăm, và giá có lúc về mức thấp nhất hơn sáu năm. "
           "Hòa Phát thì ngược lại, lãi tăng mà giá vẫn thấp nhất mười tám tháng. "
           "Còn cổ phiếu Vingroup hôm qua một mình kéo chỉ số giảm gần hai mươi tư điểm. Dù vậy, giá của nó vẫn cao gần gấp đôi lúc thấp nhất năm qua. Nghĩa là Vingroup đã tăng rất mạnh từ trước, còn Hòa Phát thì rơi dù lãi tốt.")),
 dict(k='chat', short=True, cap=('"THỊ TRƯỜNG KHÔNG TRẢ TIỀN', 'CHO LÃI QUÝ VỪA RỒI"'), cols=CC, moc=True, chat=dict(ten='Anh Long (bạn cũ)', tv='Đang hoạt động', gio='21:10', mau=X_, msgs=[
        ('me', 'Lãi gấp đôi, P/E 6, sao giá vẫn rơi?'),
        ('Anh Long (bạn cũ)', 'Giá cổ phiếu nhìn lãi những năm tới, không nhìn quý vừa rồi'),
        ('Anh Long (bạn cũ)', 'Thép lên xuống theo chu kỳ, nhớ năm 2022 không?')]),
      say=("Anh Khoa hỏi anh Long, người bạn cũ làm kế toán: lãi gấp đôi, P/E sáu lần, sao giá vẫn rơi? "
           "Anh Long trả lời: giá cổ phiếu nhìn vào lãi của những năm tới, không nhìn lại quý vừa rồi. Thép là ngành lên xuống theo chu kỳ. "
           "Rồi anh hỏi lại: ông còn nhớ năm hai nghìn không trăm hai mươi hai không?")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước: năm 2022', cap=('"NĂM 2022 CHÚ CŨNG THẤY', 'P/E 6 LÀ RẺ"'), cols=CR, moc=True, call=dict(ten='Chú Thành', phu='Đang gọi', mau=V_, loi=[
        'Năm 2022 chú cũng thấy P/E 6 là rẻ', 'Lãi năm trước rất cao, chú mua vào tháng 3']),
      say=("Anh Khoa gọi cho chú Thành, người dạy anh mua cổ phiếu đầu tiên. Chú kể: năm hai nghìn không trăm hai mươi hai, chú cũng thấy P/E sáu lần là rẻ. "
           "Lãi năm hai nghìn không trăm hai mươi mốt của công ty rất cao, nên chú mua vào tháng ba. Chú nói chú không tiếc vì mua, chú tiếc vì đã tin rằng con số đó sẽ đứng yên.")),
 dict(k='giay', short=True, cap=('NĂM 2022: P/E 6,4', 'RỒI GIÁ MẤT 69%'), cols=CR, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ NĂM 2022', so='WiData: giá đã điều chỉnh, lãi cổ đông công ty mẹ', dau='ĐÃ XẢY RA', dieu=[
        ('Quý 1/2022: lãi 8.217 tỷ.', 'VÙNG CAO'),
        ('7/3/2022: giá 26.150 đ, P/E 6,4.', 'ĐỈNH'),
        ('Quý 3 và quý 4/2022: lỗ.', 'LỖ'),
        ('10/11/2022: giá còn 8.190 đ.', 'GIẢM 69%')]),
      say=("Em tìm lại số liệu. Quý một năm hai nghìn không trăm hai mươi hai, phần lãi thuộc về cổ đông Hòa Phát là khoảng tám nghìn hai trăm mười bảy tỷ đồng. "
           "Tháng ba năm đó, giá lên đỉnh của năm, khoảng hai mươi sáu nghìn đồng. P/E khi ấy cũng chỉ khoảng sáu lần. "
           "Rồi quý ba và quý bốn, công ty lỗ. Đến tháng mười một, giá còn khoảng tám nghìn hai trăm đồng, mất gần bảy mươi phần trăm.")),
 dict(k='bignum', anh=TP, cap=('CÙNG 8.217 TỶ LÃI 1 QUÝ', 'QUÝ 1/2022 VÀ QUÝ 3/2026'), cols=CR, value=8217, fmt='{:,.0f}', unit=' TỶ', top='LÃI MỘT QUÝ THUỘC CỔ ĐÔNG HÒA PHÁT', sub='Phần của người cầm cổ phiếu Hòa Phát, khác số 8.265 tỷ lãi tổng', col=RED,
      say=("Và đây là chỗ khiến anh Khoa giật mình. Quý ba năm nay, chỉ tính phần lãi thực sự thuộc về người cầm cổ phiếu Hòa Phát, con số cũng là khoảng tám nghìn hai trăm mười bảy tỷ đồng. "
           "Gần như đúng bằng quý một năm hai nghìn không trăm hai mươi hai. Cùng một mức lãi, cùng một P/E khoảng sáu lần. "
           "Lần trước, đó không phải là đáy. Đó là lúc lãi đang ở vùng cao, ngay trước khi đi xuống.")),
 dict(k='bars', anh=SGD, cap=('GIÁ ĐI TRƯỚC LÃI', 'NĂM 2022'), cols=CR, moc=True, top='GIÁ CỔ PHIẾU HÒA PHÁT (ĐỒNG, ĐÃ ĐIỀU CHỈNH)',
      bars=[('7/3/2022', 26150, GOLD, '26.150'), ('10/11/2022', 8190, RED, '8.190'), ('26/11/2026', 19600, X_, '19.600')],
      say=("Điều đáng nhớ là năm đó, giá đi trước lãi. Quý hai năm hai nghìn không trăm hai mươi hai, lãi vẫn dương nhưng đã giảm khoảng năm mươi mốt phần trăm so với quý một, trong khi giá đã rơi từ trước đó. "
           "Người chỉ nhìn lãi quý vừa công bố để mua thường chậm hơn người nhìn trước một bước.")),
 dict(k='checklist', anh=HN, cap=('2022 VÀ HÔM NAY', 'GIỐNG 2, KHÁC 2'), cols=CC, moc=True,
      items=[('Giống: lãi quý khoảng 8.217 tỷ', GOLD), ('Giống: P/E quanh 6 lần', GOLD), ('Khác: chưa thấy lãi chững lại', G_), ('Khác: nước ngoài đang mua vào', G_)],
      say=("Nhưng hôm nay có giống hệt năm đó không? Em thấy giống hai điểm: lãi một quý khoảng tám nghìn hai trăm tỷ đồng, và P/E quanh sáu lần. "
           "Khác ở chỗ: năm hai nghìn không trăm hai mươi hai, lãi giảm ngay quý kế tiếp; năm nay chưa thấy dấu hiệu đó, nhưng lãi quý bốn mới là phép thử. "
           "Khác thứ hai: ba mươi phiên giao dịch qua, nhà đầu tư nước ngoài mua vào cổ phiếu này nhiều hơn bán ra, chênh gần hai trăm tỷ đồng, tính cả giao dịch thỏa thuận. Trong khi đó, trên cả thị trường họ đang bán ra nhiều hơn mua vào. "
           "Chưa lặp lại, không có nghĩa là không thể lặp lại.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='giay', ch='Chương 4 – Tài khoản của anh Khoa', short=True, cap=('MUA 120 TRIỆU', 'CÒN 98 TRIỆU'), cols=CR, moc=True, giay=dict(tieu_de='TÀI KHOẢN CỦA ANH KHOA', so='Em giả định: tiền nhàn rỗi, không vay', dau='GIẢ ĐỊNH', dieu=[
        ('5.000 cổ phiếu, giá mua 24.000 đ.', 'MUA'),
        ('Vốn bỏ ra: 120 triệu đồng.', 'VỐN'),
        ('Giá hôm qua: 19.600 đ.', 'NAY'),
        ('Còn 98 triệu, tạm lỗ 22 triệu.', 'LỖ 18%')]),
      say=("Anh Khoa mở tài khoản. Đây là con số em giả định. Anh có năm nghìn cổ phiếu, mua giá hai mươi tư nghìn đồng. Anh đã bỏ ra một trăm hai mươi triệu đồng. "
           "Theo giá hôm qua, tài khoản còn chín mươi tám triệu đồng. Anh đang tạm lỗ hai mươi hai triệu. "
           "May là đây là tiền nhàn rỗi, anh không vay đồng nào.")),
 dict(k='chat', cap=('"TIỀN NÀY CÓ CẦN', 'TRONG 12 THÁNG KHÔNG?"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:15', mau=V_, msgs=[
        ('Vợ', 'Tiền này nhà mình có cần trong 12 tháng không anh?'),
        ('me', 'Không, tiền học của con đã để riêng rồi'),
        ('Vợ', 'Vậy đừng vay để mua thêm nhé')]),
      say=("Vợ anh hỏi: tiền này nhà mình có cần dùng trong mười hai tháng tới không anh? "
           "Anh Khoa trả lời là không, vì tiền học của con đã để riêng. Chị nhắn: vậy đừng vay để mua thêm nhé. "
           "Hai câu hỏi đó quyết định nhiều hơn mọi lời đoán giá.")),
 dict(k='cards', anh=TP, cap=('3 CÁCH', 'KHÔNG PHẢI ĐOÁN GIÁ'), cols=CC, moc=True,
      cards=[('Quý 4', 'Xem lãi quý 4 khi công bố', 'ĐẶT MỐC XEM LẠI'), ('12 tháng', 'Tiền cần dùng không để ở cổ phiếu', 'TÁCH TIỀN CẦN DÙNG'), ('0 đồng', 'Không vay thêm để mua bù', 'KHÔNG VAY ĐỂ MUA')],
      say=("Anh Khoa ghi ra ba cách, không cách nào là đoán giá. Một, đặt mốc xem lại khi công ty công bố lãi quý bốn, xem lãi còn tăng hay đã bắt đầu chững. "
           "Hai, tiền nào cần dùng trong mười hai tháng thì không để ở cổ phiếu. Ba, không vay tiền để mua thêm ở giá thấp cho giá vốn giảm xuống, vì năm hai nghìn không trăm hai mươi hai cho thấy giá có thể giảm sâu hơn nhiều người nghĩ. "
           "Quyết giữ hay bán, cách nào cũng có rủi ro riêng.")),
 dict(k='chat', cap=('"ANH KHÔNG ĐOÁN ĐÁY', 'ANH CHỈ ĐẶT MỐC"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='22:40', mau=V_, msgs=[
        ('me', 'Anh không đoán đáy nữa, anh chỉ đặt mốc'),
        ('me', 'Lãi quý 4 còn tăng thì giữ, chững lại thì tính tiếp'),
        ('Vợ', 'Vậy là được. Ngủ thôi')]),
      say=("Anh Khoa nhắn vợ: anh không đoán đáy nữa, anh chỉ đặt mốc. Lãi quý bốn còn tăng thì giữ, chững lại thì tính tiếp. "
           "Chị trả lời: vậy là được, ngủ thôi. Đây là cách riêng của nhà anh Khoa, không phải lời khuyên mua hay bán.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Phép thử cho cổ phiếu đang rơi', anh=SGD, cap=('PHÉP THỬ 3 CÂU', 'KHI CỔ PHIẾU ĐANG RƠI'), cols=CC, moc=True,
      items=[('Lãi quý gần nhất tăng hay giảm?', GOLD), ('P/E thấp nhờ lãi đang ở đỉnh?', GOLD), ('Tiền cần trong 12 tháng hay đang vay?', RED)],
      say=("Em gợi ý một phép thử ba câu cho bất kỳ cổ phiếu nào anh chị đang cầm mà giá đang rơi. Một, lãi quý gần nhất của công ty tăng hay giảm so với cùng kỳ? "
           "Hai, P/E thấp là vì giá rẻ thật, hay vì lãi đang ở đỉnh của một chu kỳ? Ba, số tiền này anh chị có cần trong mười hai tháng tới, hay đang có tiền vay trong đó? "
           "Câu ba mà trả lời là có, thì đó là việc cần xử lý trước tiên.")),
 dict(k='checklist', anh=HN, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY ĐẾN THÁNG 3/2027'), cols=CC, moc=True,
      items=[('Lãi quý 4 của doanh nghiệp', GOLD), ('Mỹ nghe trình bày về thuế từ 25/1', GOLD), ('Nhà đầu tư nước ngoài mua hay bán', GOLD)],
      say=("Ba điều đáng theo dõi. Lãi quý bốn của các doanh nghiệp, thường được công bố vào tháng một. Buổi Mỹ nghe các bên trình bày về mức thuế bắt đầu từ ngày hai mươi lăm tháng một, quyết định chậm nhất ngày mười một tháng ba năm sau. "
           "Và việc nhà đầu tư nước ngoài mua vào hay bán ra. Trang mã Hòa Phát trên chứng khoán Huy Nguyễn chấm com có số liệu lãi từng quý để anh chị tự xem.")),
 # ---------------- KẾT ----------------
 dict(k='chat', cap=('"LẦN NÀY CHÚ NHÌN LÃI', 'NĂM SAU, KHÔNG NHÌN GIÁ HÔM NAY"'), cols=CC, chat=dict(ten='Chú Thành', tv='Đang hoạt động', gio='23:00', mau=V_, msgs=[
        ('me', 'Cháu đặt mốc quý 4 rồi chú ạ'),
        ('Chú Thành', 'Tốt. Đừng nhìn giá hôm nay mà đoán'),
        ('Chú Thành', 'Nhìn xem lãi năm sau đi về đâu')]),
      say=("Trước khi ngủ, anh Khoa nhắn chú Thành: cháu đặt mốc quý bốn rồi chú ạ. Chú trả lời: tốt, đừng nhìn giá hôm nay mà đoán, hãy nhìn xem lãi năm sau đi về đâu. "
           "Năm hai nghìn không trăm hai mươi hai, chú học điều đó bằng tiền thật.")),
 dict(k='end', cap=('CỔ PHIẾU ANH CHỊ ĐANG CẦM', 'LÃI QUÝ GẦN NHẤT TĂNG HAY GIẢM?'), cols=CC,
      say=("Còn anh chị, cổ phiếu anh chị đang cầm có lãi quý gần nhất tăng hay giảm, và giá của nó đang đi cùng chiều hay ngược chiều với lãi?")),
]
import ql_post; S = ql_post.tach(S, max_tu=50, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = "Cổ Phiếu Hòa Phát Thấp Nhất 18 Tháng Dù Lãi Gấp Đôi: Đã Rẻ?"
WEB = 'https://chungkhoanhuynguyen.com/ma/HPG.html'
MT = ("NÓNG: phiên 26/11/2026, cổ phiếu Hòa Phát (HPG) đóng cửa 19.600 đồng – thấp nhất kể từ tháng 6/2025 – dù lãi sau thuế 9 tháng tăng 104%, quý 3 tăng 106%. P/E chỉ khoảng 6 lần. "
      "Vì sao lãi gấp đôi mà giá vẫn rơi? Năm 2022 cổ phiếu này cũng có lãi một quý khoảng 8.217 tỷ và P/E khoảng 6 – rồi giá mất khoảng 69%. Giống 2, khác 2, và phép thử 3 câu cho cổ phiếu đang rơi. Video không khuyến nghị mua hay bán.\n\n"
      "Nguồn số liệu:\n"
      "• MarketTimes 26/11/2026: HPG giảm 2,2% còn 19.600 đồng/cp, thấp nhất kể từ 11/6/2025; quý 3/2026 doanh thu 62.669 tỷ (+70%), lãi sau thuế 8.265 tỷ (+106%); 9 tháng doanh thu 171.539 tỷ (+54%), lãi sau thuế 23.746 tỷ (+104%), vượt 8% kế hoạch lợi nhuận năm\n"
      "• WiData (giá đã điều chỉnh): giá đóng cửa cao nhất 12 tháng 26.250 đồng; 7/3/2022 26.150 đồng (cao nhất năm 2022); 10/11/2022 8.190 đồng\n"
      "• WiData (BCTC hợp nhất, lãi sau thuế của cổ đông công ty mẹ): quý 1/2022 8.217 tỷ; quý 2/2022 4.032 tỷ; quý 3/2022 lỗ 1.774 tỷ; quý 4/2022 lỗ 1.992 tỷ; quý 3/2026 8.217 tỷ\n"
      "• WiData P/E: HPG 26/11/2026 6,03 lần (trung vị 5 năm 13,2); 7/3/2022 6,4 lần\n"
      "• WiData 26/11/2026: VN-Index giảm 57,77 điểm (−3,42%) còn 1.629,68; 291 mã giảm, 47 mã tăng; VIC kéo giảm 23,82 điểm; khối ngoại bán ròng từ đầu tháng 10.674 tỷ; VIC 230.000 đồng, cao hơn giá đóng cửa thấp nhất 12 tháng (121.600) khoảng 89%; khối ngoại mua ròng HPG 197,6 tỷ trong 30 phiên 15/10–26/11 (gồm thỏa thuận)\n"
      "• Nhà Đầu Tư 26/11/2026: ACV có lúc 35.200 đồng, thấp nhất hơn 6 năm; lãi sau thuế quý 3/2026 giảm 35,1%\n"
      "• Báo Cần Thơ (TTXVN) 26/11/2026: Mỹ đề xuất thuế bổ sung tối đa 35% với hàng Việt Nam, chưa có hiệu lực; điều trần từ 25/1/2027, quyết định muộn nhất 11/3/2027\n"
      "• Tự tính: 19.600/26.250 − 1 ≈ −25%; 8.190/26.150 − 1 ≈ −69%; quý 2/2022 so quý 1/2022 ≈ −51%. Tài khoản anh Khoa là GIẢ ĐỊNH: 5.000 cp × 24.000 đồng = 120 triệu; theo giá 19.600 còn 98 triệu (tạm lỗ 22 triệu, ≈ −18%)\n\n"
      "Số liệu lãi từng quý của Hòa Phát: " + WEB + "\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật anh Khoa, vợ anh, anh Long, chú Thành là hư cấu; số liệu là thật theo nguồn trên.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-27', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['cổ phiếu Hòa Phát', 'HPG', 'cổ phiếu HPG', 'P/E', 'VN-Index hôm nay', 'chứng khoán hôm nay', 'cổ phiếu thép', 'Hòa Phát lãi quý 3', 'chu kỳ thép', 'tin nóng tài chính'],
    bia_hook=['LÃI GẤP ĐÔI', 'GIÁ VẪN RƠI???'], badge='THẤP NHẤT 18 THÁNG',
    bia_anh='Ho Chi Minh City Stock Exchange||Ho Chi Minh City skyline night',
    bia_hook_b=['CÙNG LÃI 8.217', '2022 MẤT 69%'], badge_b='LÃI 1 QUÝ, 2022 VÀ NAY',
    bia_hook_c=['P/E 6 LẦN', 'RẺ HAY BẪY CŨ?'], badge_c='NĂM 2022 CŨNG P/E 6',
    reel_hook='LÃI GẤP ĐÔI|SAO GIÁ VẪN RƠI???',
    fb_post=("Hòa Phát lãi 9 tháng tăng 104%, mà cổ phiếu thấp nhất 18 tháng 📉\n\n👉 P/E chỉ khoảng 6 lần\n👉 Năm 2022: lãi một quý cũng khoảng 8.217 tỷ, P/E cũng khoảng 6 – rồi giá mất khoảng 69%\n"
             "👉 Giá cổ phiếu nhìn lãi những năm tới, không nhìn quý vừa rồi\n\nPhép thử 3 câu khi cổ phiếu đang rơi: lãi quý gần nhất? P/E thấp nhờ lãi đỉnh? tiền cần trong 12 tháng hay đang vay?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 27/11: cổ phiếu Hòa Phát thấp nhất 18 tháng dù lãi gấp đôi; P/E 6 – lần trước 2022 (NV1B 27/11/2026).\n"
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
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, True):
    if 'câu cụt' not in q and ('cảnh 1' in q): print('TIN_NONG', q)
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'):
    for l in kiem_goi.kiem(TIEU, META[KEY][b]): print('kiem_goi', b, l)
try:
    import xung_ho
    for i, c in enumerate(S, 1):
        if xung_ho.le_phep(c['say']) != c['say']: print('XUNG_HO doi canh', i)
except Exception as e: print('xung_ho?', e)
