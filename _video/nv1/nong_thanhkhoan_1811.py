# -*- coding: utf-8 -*-
# NV1B 18/11/2026 – VIDEO NÓNG kênh chính: tiền vào chứng khoán thấp nhất 21 tháng (CafeF 18/11/2026 00:03).
# Lý do chọn: tin nóng nhất 24h về túi tiền nhà đầu tư cá nhân (CafeF đêm 17/11, Vietstock "Đọc gì" 18/11: tự doanh + khối ngoại bán ròng gần 1.100 tỷ phiên 17/11).
#   Khác NONG1611A (margin kỷ lục – phía nợ vay) – đây là phía dòng tiền/thanh khoản + định giá + khối ngoại. Khác NONG1711A (lãi tiết kiệm SCB).
#   WiData hết credit tới 00:00 20/11 → nguồn báo, ghi tên báo + ngày cho từng số.
# Nguồn:
#  - CafeF 18/11/2026 (Mai Chi, theo Việt Nam hàng ngày; dữ liệu HOSE, VSDC): giá trị khớp lệnh bình quân HOSE tháng 10/2026 chỉ hơn 12.000 tỷ, thấp nhất kể từ tháng 1/2025;
#    VN-Index từ 1.829 điểm cuối tháng 1 về 1.726,72 điểm ngày 17/11 (giảm khoảng 5,6%), vẫn trên 1.700; khối ngoại bán ròng HOSE tháng 10 hơn 23.705 tỷ, từ đầu năm hơn 119.000 tỷ;
#    tháng 10 mở mới hơn 252.000 tài khoản, tổng khoảng 14,33 triệu; NHNN đề nghị ngân hàng giảm lãi, mua USD giao ngay từ 11/11;
#    thanh khoản giảm KHÔNG chứng minh tiền chạy sang vàng, nhà đất hay ngân hàng – có thể nhà đầu tư giữ lâu hơn, giao dịch ít hơn.
#  - Báo Đấu thầu 5/11/2026 (số liệu HOSE): tháng 10/2026 giá trị giao dịch bình quân hơn 15.602 tỷ/phiên, giảm 4,93% so với tháng 9; VN-Index 30/10 1.741,62; khối ngoại bán ròng hơn 23.705 tỷ.
#  - Báo Đầu tư 3/9/2025: tháng 8/2025 giá trị giao dịch bình quân riêng HOSE xấp xỉ 50.000 tỷ/phiên; khối ngoại bán ròng kỷ lục hơn 42.000 tỷ trong tháng.
#  - CafeF 4/11/2026: nâng hạng FTSE Russell ngày 21/9; bán ròng gần 30.000 tỷ trong khoảng 1,5 tháng sau đó; luỹ kế HOSE đến 3/11 gần 121.000 tỷ, gần kỷ lục năm 2025 (125.000 tỷ).
#  - CafeF 18/11/2026 dẫn báo cáo chiến lược tháng 11 của SHS: P/E VN-Index cuối tháng 10 10,8 lần, thấp hơn đáy tháng 4/2025, sát mức 10,3 lần ở đáy Covid tháng 4/2020;
#    lãi sau thuế quý 3/2026 của 1.124 doanh nghiệp khoảng 254.800 tỷ, tăng gần 43%.
#  - Dân trí 16/11/2026: lãi tiết kiệm online 12 tháng phổ biến 6–7% mỗi năm.
#  - VnEconomy 3/11/2022: tháng 10/2022 giá trị giao dịch bình quân HOSE hơn 11.449 tỷ/phiên, giảm 14,53%; VN-Index cuối tháng 10/2022 1.027,94.
#  - BSC 30/12/2022: VN-Index cuối 2022 1.007,09. Viettimes/VnExpress: VN-Index chốt năm 2023 1.129,93 (tăng hơn 12%).
#  - Vietstock 18/11/2026: tự doanh và khối ngoại bán ròng gần 1.100 tỷ phiên 17/11.
# V2 (whisper V1: 'một trăm hai mươi mốt nghìn tỷ' nghe ra 124.000 cả beam 1 và 5) → lời đọc nói tỷ lệ 121.000 ÷ 125.000 ≈ 97%, số đủ trên thẻ.
# SỐ TỰ TÍNH: 15.602 ÷ 50.000 = 31,2% → giảm khoảng 68,8% ("gần 70%"). 1.726,72 ÷ 1.829 = 94,4% → giảm 5,6%.
#   1.129,93 ÷ 1.027,94 = 1,099 → cao hơn khoảng 9,9% ("gần 10%"). 121.000 ÷ 125.000 = 96,8%.
#   Nhân vật (GIẢ ĐỊNH): tài khoản 400 triệu = 300 triệu vốn + 100 triệu vay ký quỹ; giảm 8% → mất 32 triệu = 10,7% vốn tự có ("gần 11%").
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261118_0815_nong'
KEY = 'NONG1811A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TP = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline night'
HN = 'ov:Hanoi skyline night||Hanoi skyline night'
SGD = 'ov:Ho Chi Minh City Stock Exchange||Ho Chi Minh City Stock Exchange'
BX = 'ov:Bitexco Financial Tower||Bitexco Financial Tower'
NHA = 'ov:Hanoi apartment buildings||Hanoi apartment buildings'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('TIỀN VÀO CHỨNG KHOÁN', 'THẤP NHẤT 21 THÁNG'), cols=CR, noti=dict(gio='07:30', ngay='Thứ Tư', items=[
        ('Tin tức', 'Chứng khoán', 'Tiền vào chứng khoán rơi xuống thấp nhất 21 tháng', R_),
        ('Vợ', 'Tin nhắn', 'Anh ơi, tài khoản chứng khoán nhà mình sao rồi?', X_)]),
      say=("Bảy giờ rưỡi sáng nay, anh Tùng, kỹ sư ở Hà Nội, vừa mở điện thoại đã thấy một tin. Tiền vào chứng khoán vừa rơi xuống mức thấp nhất hai mươi mốt tháng. "
           "Theo CafeF, giá trị khớp lệnh bình quân mỗi phiên trên sàn HOSE tháng mười chỉ hơn mười hai nghìn tỷ đồng, thấp nhất kể từ tháng một năm 2025. "
           "Một phút sau, vợ nhắn: anh ơi, tài khoản chứng khoán nhà mình sao rồi?")),
 dict(k='bignum', anh=SGD, cap=('50.000 TỶ MỖI PHIÊN', 'GIỜ CÒN 15.600 TỶ'), cols=CR, value=15602, fmt='{:,.0f}', unit=' tỷ', top='GIÁ TRỊ GIAO DỊCH MỖI PHIÊN, T10/2026', sub='Tháng 8/2025: xấp xỉ 50.000 tỷ mỗi phiên', col=RED,
      say=("Tính cả giao dịch thoả thuận, theo số liệu sàn HOSE, tháng mười mỗi phiên có khoảng mười lăm nghìn sáu trăm tỷ đồng sang tay. Tháng tám năm ngoái, con số đó xấp xỉ năm mươi nghìn tỷ. "
           "Giảm gần bảy mươi phần trăm. Tiền đã đi đâu? Ai đang bán? Và tài khoản của anh chị nên nhìn chuyện này thế nào?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Tháng 10 nói gì?', cap=('THÁNG 10 TRÊN SÀN HOSE', 'NHỮNG CON SỐ CHÍNH'), cols=CC, moc=True, giay=dict(tieu_de='SÀN HOSE THÁNG 10/2026', so='Theo Báo Đấu thầu 5/11 và CafeF 18/11/2026', dau='ĐÃ ĐỌC', dieu=[
        ('Giao dịch mỗi phiên: hơn 15.602 tỷ.', 'GIẢM 4,93%'),
        ('Riêng khớp lệnh: hơn 12.000 tỷ.', 'THẤP NHẤT 21 THÁNG'),
        ('Khối ngoại bán ròng hơn 23.705 tỷ.', 'BÁN MẠNH'),
        ('VN-Index ngày 17/11: 1.726,72 điểm.', 'VẪN TRÊN 1.700')]),
      say=("Anh Tùng ghi lại bốn con số. Một, giá trị giao dịch bình quân mỗi phiên tháng mười hơn mười lăm nghìn sáu trăm tỷ đồng, giảm gần năm phần trăm so với tháng chín. "
           "Hai, riêng khớp lệnh chỉ hơn mười hai nghìn tỷ. Ba, khối ngoại bán ròng hơn hai mươi ba nghìn bảy trăm tỷ đồng chỉ trong tháng mười. "
           "Bốn, VN-Index phiên hôm qua đóng cửa ở một nghìn bảy trăm hai mươi sáu điểm, vẫn trên mốc một nghìn bảy trăm.")),
 dict(k='chat', cap=('"TIỀN RÚT HẾT RỒI', 'BÁN ĐI ANH?"'), cols=CR, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='07:45', mau=X_, msgs=[
        ('Vợ', 'Báo nói tiền rút khỏi chứng khoán hết rồi'),
        ('Vợ', 'Hay anh bán đi cho nhẹ đầu?'),
        ('me', 'Để anh đọc kỹ đã em')]),
      say=("Vợ nhắn tiếp: báo nói tiền rút khỏi chứng khoán hết rồi, hay anh bán đi cho nhẹ đầu? Anh Tùng trả lời: để anh đọc kỹ đã. "
           "Và chi tiết đầu tiên anh đọc được làm anh bất ngờ. Chính bài báo viết: thanh khoản giảm không chứng minh tiền đã chạy sang vàng, nhà đất hay ngân hàng. Có thể nhà đầu tư chỉ đang giữ cổ phiếu lâu hơn, mua bán ít đi.")),
 dict(k='bignum', anh=HN, cap=('THÁNG 10 VẪN MỞ MỚI', 'HƠN 252.000 TÀI KHOẢN'), cols=CC, moc=True, value=252000, fmt='{:,.0f}', unit=' tài khoản', top='TÀI KHOẢN MỞ MỚI THÁNG 10/2026', sub='Tổng khoảng 14,33 triệu tài khoản, theo VSDC', col=GOLD,
      say=("Cú lật thứ hai. Cũng trong tháng mười, nhà đầu tư trong nước mở mới hơn hai trăm năm mươi hai nghìn tài khoản, nâng tổng số lên khoảng mười bốn phẩy ba triệu. "
           "Người vẫn đến, nhưng tiền chưa vào. Mở tài khoản rồi để đó, đứng ngoài quan sát. Vậy điều gì khiến tiền đứng yên?")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='cards', ch='Chương 2 – Vì sao tiền đứng ngoài?', anh=TP, cap=('3 LÝ DO', 'TIỀN ĐỨNG NGOÀI'), cols=CC, moc=True,
      cards=[('6 đến 7%', 'Lãi tiết kiệm 12 tháng', 'GỬI LÀ CÓ LÃI'), ('121.000 tỷ', 'Khối ngoại bán ròng đến 3/11', 'GẦN KỶ LỤC 2025'), ('30.000 tỷ', 'Bán ròng 1,5 tháng sau nâng hạng', 'NGƯỢC KỲ VỌNG')],
      say=("Báo chí nêu ba lý do. Một, lãi tiết kiệm kỳ hạn mười hai tháng phổ biến sáu đến bảy phần trăm mỗi năm. Gửi là có lãi, còn cổ phiếu thì có rủi ro giá. "
           "Hai, khối ngoại bán ròng trên sàn HOSE từ đầu năm tới ngày ba tháng mười một đã bằng khoảng chín mươi bảy phần trăm kỷ lục của cả năm ngoái. Kỷ lục đó là một trăm hai mươi lăm nghìn tỷ đồng. "
           "Ba, Việt Nam được FTSE Russell nâng hạng ngày hai mươi mốt tháng chín, nhưng chỉ khoảng một tháng rưỡi sau đó, khối ngoại bán ròng thêm gần ba mươi nghìn tỷ.")),
 dict(k='chat', cap=('"NÂNG HẠNG RỒI', 'SAO VẪN BÁN?"'), cols=CC, moc=True, chat=dict(ten='Anh Quân', tv='Đồng nghiệp', gio='09:10', mau=G_, msgs=[
        ('me', 'Nâng hạng rồi sao khối ngoại vẫn bán?'),
        ('Anh Quân', 'Tiền từ quỹ chỉ số vào theo lịch, từng đợt'),
        ('Anh Quân', 'Còn tiền chủ động thì đang chờ tỷ giá và lãi suất')]),
      say=("Anh Tùng hỏi anh Quân, đồng nghiệp hay đọc báo cáo phân tích: nâng hạng rồi, sao khối ngoại vẫn bán? Anh Quân trả lời: tiền của các quỹ chỉ số thường vào theo lịch, từng đợt, không phải ngay hôm sau. "
           "Còn dòng tiền chủ động thì đang chờ tỷ giá và lãi suất dịu lại. Phiên hôm qua, theo Vietstock, tự doanh và khối ngoại vẫn bán ròng gần một nghìn một trăm tỷ.")),
 dict(k='bignum', anh=BX, cap=('P/E VN-INDEX 10,8 LẦN', 'SÁT ĐÁY COVID 10,3'), cols=CC, moc=True, value=10.8, fmt='{:,.1f}', unit=' lần', top='P/E VN-INDEX CUỐI THÁNG 10/2026', sub='Đáy Covid tháng 4/2020: 10,3 lần (theo SHS)', col=GOLD,
      say=("Rồi anh Quân gửi thêm một con số, và đây là cú lật lớn nhất. Theo báo cáo của Chứng khoán SHS, cuối tháng mười, P/E của VN-Index chỉ khoảng mười phẩy tám lần. "
           "Mức này thấp hơn cả đáy tháng tư năm 2025, và sát mức mười phẩy ba lần ở đáy Covid tháng tư năm 2020. Tiền đang đứng ngoài, đúng lúc thị trường được định giá ở vùng thấp nhiều năm.")),
 dict(k='cards', anh=TP, cap=('LÃI DOANH NGHIỆP TĂNG', 'GIÁ CỔ PHIẾU ĐỨNG'), cols=CC, moc=True,
      cards=[('254.800 tỷ', 'Lãi quý 3 của 1.124 doanh nghiệp', 'TĂNG GẦN 43%'), ('1.829 điểm', 'VN-Index cuối tháng 1/2026', 'ĐIỂM ĐẦU NĂM'), ('1.726,72', 'VN-Index ngày 17/11', 'GIẢM 5,6%')],
      say=("Vì sao P/E thấp? Nguyên nhân chính nằm ở lợi nhuận. Theo SHS, lãi sau thuế quý ba của một nghìn một trăm hai mươi tư doanh nghiệp niêm yết khoảng hai trăm năm mươi tư nghìn tám trăm tỷ, tăng gần bốn mươi ba phần trăm. "
           "Trong khi đó, VN-Index từ khoảng một nghìn tám trăm hai mươi chín điểm cuối tháng một, nay về một nghìn bảy trăm hai mươi sáu điểm, giảm khoảng năm phẩy sáu phần trăm. Lãi đi lên, giá đi ngang và xuống, nên P/E co lại.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='call', ch='Chương 3 – Lần trước là tháng 10/2022', cap=('"NĂM 2022 CHÚ CŨNG', 'CHÁN, RỒI BÁN HẾT"'), cols=CC, moc=True, call=dict(ten='Chú Bình', phu='Hàng xóm, đầu tư từ năm 2007', mau=V_, loi=[
        'Cuối năm 2022 sàn vắng như chợ chiều', 'Chú chán quá, bán hết']),
      say=("Trưa đó anh Tùng gọi cho chú Bình, hàng xóm đầu tư chứng khoán từ năm 2007. Chú kể: cuối năm 2022, sàn vắng như chợ chiều. Ai cũng chán, ai cũng nói tiền đã rút đi hết. "
           "Chú cũng chán, và bán sạch danh mục khi chỉ số quanh mốc một nghìn điểm.")),
 dict(k='giay', cap=('THÁNG 10/2022', 'NHỮNG CON SỐ CỦA LẦN TRƯỚC'), cols=CC, moc=True, giay=dict(tieu_de='NHỮNG CON SỐ CỦA LẦN TRƯỚC', so='Theo VnEconomy 3/11/2022, BSC, Viettimes', dau='SO SÁNH', dieu=[
        ('T10/2022: hơn 11.449 tỷ mỗi phiên.', 'GIẢM 14,53%'),
        ('VN-Index cuối T10/2022: 1.027,94.', 'QUANH 1.000'),
        ('VN-Index cuối năm 2022: 1.007,09.', 'VẪN THẤP'),
        ('VN-Index cuối năm 2023: 1.129,93.', 'CAO HƠN GẦN 10%')]),
      say=("Những con số của lần trước. Tháng mười năm 2022, theo VnEconomy, giao dịch bình quân trên HOSE hơn mười một nghìn bốn trăm tỷ mỗi phiên. Con số đó giảm gần mười lăm phần trăm chỉ trong một tháng. VN-Index cuối tháng mười quanh mốc một nghìn điểm. "
           "Tháng sau đó chỉ số còn xuống sâu hơn nữa. Nhưng cuối năm 2023, VN-Index đóng cửa ở một nghìn một trăm hai mươi chín điểm. Mức đó cao hơn khoảng mười phần trăm so với cuối tháng mười năm 2022. Không phải một cú bật thần kỳ, nhưng người bán vì chán đã bán ở vùng thấp.")),
 dict(k='bars', anh=TP, cap=('TIỀN MỖI PHIÊN TRÊN HOSE', 'LẦN TRƯỚC VÀ BÂY GIỜ'), cols=CC, moc=True,
      bars=[('Tháng 10/2022', 11449, RED, '11.449 tỷ'), ('Tháng 8/2025', 50000, GREEN, '50.000 tỷ'), ('Tháng 10/2026', 15602, GOLD, '15.602 tỷ')],
      say=("Đặt ba mốc cạnh nhau. Tháng mười năm 2022, hơn mười một nghìn bốn trăm tỷ mỗi phiên. Tháng tám năm 2025, lúc sôi động nhất, xấp xỉ năm mươi nghìn tỷ. "
           "Tháng mười năm nay, khoảng mười lăm nghìn sáu trăm tỷ. Thấp, nhưng vẫn cao hơn đáy năm 2022.")),
 dict(k='checklist', anh=HN, cap=('GIỐNG 2, KHÁC 2', 'SO VỚI NĂM 2022'), cols=CC, moc=True,
      items=[('Giống: sàn vắng, ai cũng chán', RED), ('Giống: lãi suất là đối thủ', RED), ('Khác: lãi doanh nghiệp tăng', GREEN), ('Khác: đã được nâng hạng', GREEN)],
      say=("So với năm 2022, có hai điểm giống và hai điểm khác. Giống ở chỗ sàn vắng, tâm lý chán nản, và lãi suất tiết kiệm là đối thủ cạnh tranh tiền với cổ phiếu. "
           "Khác ở chỗ năm 2022 có khủng hoảng trái phiếu doanh nghiệp, còn lần này lợi nhuận quý ba vẫn tăng. Và thị trường đã được nâng hạng, dù dòng tiền ngoại chưa vào. Chưa có cú bật, không có nghĩa là không thể có thêm một đợt giảm.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='giay', ch='Chương 4 – Tài khoản của anh Tùng', cap=('TÀI KHOẢN 400 TRIỆU', 'TRONG ĐÓ 100 TRIỆU ĐI VAY'), cols=CR, moc=True, giay=dict(tieu_de='TÀI KHOẢN CỦA ANH TÙNG', so='Số giả định để minh hoạ', dau='GIẢ ĐỊNH', dieu=[
        ('Cổ phiếu đang nắm: 400 triệu.', '400 TRIỆU'),
        ('Vốn tự có 300 triệu, vay ký quỹ 100 triệu.', 'CÓ VAY'),
        ('Tài khoản giảm 8%: mất 32 triệu.', 'MẤT 32 TRIỆU'),
        ('So với vốn tự có: mất gần 11%.', 'NẶNG HƠN')]),
      say=("Anh Tùng mở tài khoản của mình. Em giả định để minh hoạ: anh đang nắm bốn trăm triệu đồng cổ phiếu, trong đó ba trăm triệu là vốn tự có, một trăm triệu vay ký quỹ của công ty chứng khoán. "
           "Tài khoản giảm tám phần trăm, tức mất ba mươi hai triệu. Nhưng so với ba trăm triệu vốn thật của anh, đó là gần mười một phần trăm. Khoản vay làm mọi cú giảm nặng hơn.")),
 dict(k='chat', cap=('"KHOẢN VAY 100 TRIỆU', 'MỚI LÀ CHỖ ĐÁNG LO"'), cols=CC, moc=True, chat=dict(ten='Chú Bình', tv='Đang hoạt động', gio='12:40', mau=V_, msgs=[
        ('Chú Bình', 'Thị trường vắng thì giá đứng lâu lắm'),
        ('Chú Bình', 'Tiền vay thì ngày nào cũng tính lãi'),
        ('me', 'Vâng, khoản vay mới là chỗ đáng lo')]),
      say=("Chú Bình nhắn thêm: thị trường vắng thì giá có thể đứng rất lâu, mà tiền vay thì ngày nào cũng tính lãi. "
           "Anh Tùng trả lời: vâng, khoản vay một trăm triệu mới là chỗ đáng lo, chứ không phải chuyện thanh khoản thấp.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='cards', ch='Chương 5 – Ba con đường', anh=NHA, cap=('3 CON ĐƯỜNG', 'CHO TÀI KHOẢN 400 TRIỆU'), cols=CC, moc=True,
      cards=[('Bán hết', 'Như chú Bình năm 2022', 'NHẸ ĐẦU, DỄ BÁN ĐÁY'), ('Giữ nguyên', 'Cả 100 triệu tiền vay', 'RỦI RO VẪN CÒN'), ('Trả bớt vay', 'Giữ phần vốn tự có', 'NGỦ NGON HƠN')],
      say=("Anh Tùng thấy trước mặt có ba con đường. Một, bán hết như chú Bình năm 2022, nhẹ đầu nhưng dễ bán đúng lúc chán nhất. Hai, giữ nguyên, cả khoản vay một trăm triệu, chờ thị trường. "
           "Ba, trả bớt khoản vay, chỉ giữ phần vốn tự có. Mỗi con đường có cái giá riêng, và chỉ người cầm tài khoản mới biết mình chịu được cái giá nào.")),
 dict(k='chat', cap=('"ANH TRẢ HẾT TIỀN VAY', 'GIỮ PHẦN VỐN CỦA MÌNH"'), cols=CC, moc=True, chat=dict(ten='Vợ', tv='Đang hoạt động', gio='20:15', mau=X_, msgs=[
        ('me', 'Tuần này anh trả hết 100 triệu tiền vay'),
        ('me', 'Phần vốn nhà mình thì giữ, không vay thêm'),
        ('Vợ', 'Vậy em yên tâm rồi')]),
      say=("Tối đó anh Tùng nhắn vợ kế hoạch. Tuần này anh sẽ bán bớt để trả hết một trăm triệu tiền vay. Phần vốn của nhà thì giữ, không vay thêm. "
           "Vợ trả lời: vậy em yên tâm rồi. Đó là lựa chọn của gia đình anh Tùng, không phải lời khuyên chung cho mọi người.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='checklist', ch='Chương 6 – Phép thử cho tài khoản', anh=HN, cap=('PHÉP THỬ', 'TIỀN CẦN DÙNG TRONG 12 THÁNG?'), cols=CC, moc=True,
      items=[('Không đồng nào cần dùng', GREEN), ('Dưới 20% cần dùng', GOLD), ('Trên 20%, hoặc đang vay', RED)],
      say=("Em gợi ý một phép thử tự soi. Trong số tiền đang nằm ở cổ phiếu, có bao nhiêu anh chị sẽ cần dùng trong mười hai tháng tới? "
           "Nếu không đồng nào, thị trường vắng chỉ là chuyện chờ đợi. Nếu dưới hai mươi phần trăm, nên tính trước nguồn khác. Nếu trên hai mươi phần trăm, hoặc đang vay, thì một thị trường đi ngang lâu là rủi ro thật. Đây là mốc tự soi, không phải lời khuyên.")),
 dict(k='checklist', anh=TP, cap=('3 ĐIỀU CẦN THEO DÕI', 'TỪ NAY TỚI CUỐI NĂM'), cols=CC, moc=True,
      items=[('Thanh khoản khớp lệnh mỗi phiên', GOLD), ('Khối ngoại còn bán ròng?', RED), ('Lãi tiết kiệm có giảm tiếp?', GOLD)],
      say=("Ba điều đáng theo dõi tới cuối năm. Giá trị khớp lệnh mỗi phiên có quay lại vùng cao hơn hay không. Khối ngoại có ngừng bán ròng khi các quỹ chỉ số bắt đầu giải ngân. "
           "Và lãi suất tiết kiệm có giảm tiếp sau khi Ngân hàng Nhà nước đề nghị các ngân hàng hạ lãi. Muốn hiểu P/E thấp có thật sự rẻ hay không, anh chị có thể đọc bài miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối ngày', cap=('"SÀN VẮNG KHÔNG ĐÁNG SỢ', 'VAY MỚI ĐÁNG SỢ"'), cols=CC, moc=True, chat=dict(ten='Chú Bình', tv='Đang hoạt động', gio='21:30', mau=V_, msgs=[
        ('Chú Bình', 'Đừng bán vì chán như chú năm đó nhé'),
        ('me', 'Dạ, cháu chỉ bán phần tiền vay'),
        ('me', 'Sàn vắng không đáng sợ, vay mới đáng sợ')]),
      say=("Chín giờ rưỡi tối, chú Bình nhắn: đừng bán vì chán như chú năm đó nhé. Anh Tùng trả lời: dạ, cháu chỉ bán phần tiền vay. "
           "Rồi anh gõ thêm một dòng: sàn vắng không đáng sợ, tiền vay mới đáng sợ.")),
 dict(k='end', cap=('TIỀN TRONG CỔ PHIẾU CỦA ANH CHỊ', 'CÓ CẦN DÙNG TRONG 12 THÁNG?'), cols=CC,
      say=("Còn anh chị, trong số tiền đang nằm ở cổ phiếu, có bao nhiêu phần trăm anh chị sẽ cần dùng trong mười hai tháng tới? Kể cho em và mọi người ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100, anh_mac_dinh='Ho Chi Minh City skyline night')
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Tiền Vào Chứng Khoán Thấp Nhất 21 Tháng: 50.000 Tỷ Còn 15.600 Tỷ Mỗi Phiên – Tiền Đi Đâu, Có Nên Sợ?'
MT = ("NÓNG: tiền vào chứng khoán rơi xuống mức thấp nhất 21 tháng – giá trị khớp lệnh bình quân trên HOSE tháng 10/2026 chỉ hơn 12.000 tỷ đồng mỗi phiên, thấp nhất từ tháng 1/2025. "
      "Tiền đi đâu, vì sao khối ngoại bán ròng dù đã nâng hạng, P/E VN-Index 10,8 lần sát đáy Covid nói gì, lần trước tháng 10/2022 ai thiệt, và phép thử cho tài khoản của anh chị.\n\n"
      "Nguồn số liệu:\n"
      "• CafeF 18/11/2026 (theo Việt Nam hàng ngày, dữ liệu HOSE, VSDC): khớp lệnh bình quân HOSE tháng 10/2026 hơn 12.000 tỷ, thấp nhất từ tháng 1/2025; VN-Index 1.829 điểm cuối tháng 1 → 1.726,72 điểm ngày 17/11; "
      "khối ngoại bán ròng HOSE tháng 10 hơn 23.705 tỷ; tháng 10 mở mới hơn 252.000 tài khoản, tổng khoảng 14,33 triệu; thanh khoản giảm không chứng minh tiền chuyển sang vàng, nhà đất hay ngân hàng\n"
      "• Báo Đấu thầu 5/11/2026 (số liệu HOSE): giá trị giao dịch bình quân tháng 10/2026 hơn 15.602 tỷ/phiên, giảm 4,93% so với tháng 9; VN-Index 30/10: 1.741,62\n"
      "• Báo Đầu tư 3/9/2025: tháng 8/2025 giá trị giao dịch bình quân riêng HOSE xấp xỉ 50.000 tỷ/phiên\n"
      "• CafeF 4/11/2026: nâng hạng FTSE Russell 21/9; bán ròng gần 30.000 tỷ trong khoảng 1,5 tháng sau đó; luỹ kế HOSE từ đầu năm đến 3/11 gần 121.000 tỷ, gần kỷ lục năm 2025 (125.000 tỷ)\n"
      "• CafeF 18/11/2026 dẫn báo cáo chiến lược tháng 11 của Chứng khoán SHS: P/E VN-Index cuối tháng 10 khoảng 10,8 lần, thấp hơn đáy tháng 4/2025, sát 10,3 lần ở đáy Covid tháng 4/2020; lãi sau thuế quý 3/2026 của 1.124 doanh nghiệp khoảng 254.800 tỷ, tăng gần 43%\n"
      "• Dân trí 16/11/2026: lãi tiết kiệm online kỳ hạn 12 tháng phổ biến 6–7%/năm\n"
      "• Vietstock 18/11/2026: tự doanh và khối ngoại bán ròng gần 1.100 tỷ phiên 17/11\n"
      "• VnEconomy 3/11/2022: tháng 10/2022 giá trị giao dịch bình quân HOSE hơn 11.449 tỷ/phiên, giảm 14,53%; VN-Index cuối tháng 10/2022: 1.027,94. BSC 30/12/2022: VN-Index cuối 2022: 1.007,09. Viettimes/VnExpress: VN-Index chốt năm 2023: 1.129,93\n"
      "• Tự tính: 15.602 ÷ 50.000 ≈ 31% → giảm gần 70%; 1.726,72 so với 1.829 → giảm khoảng 5,6%; 1.129,93 so với 1.027,94 → cao hơn khoảng 9,9%; 121.000 ÷ 125.000 ≈ 97%. "
      "Tài khoản anh Tùng là GIẢ ĐỊNH: 400 triệu cổ phiếu = 300 triệu vốn + 100 triệu vay ký quỹ; giảm 8% = 32 triệu ≈ 10,7% vốn tự có\n\n"
      "P/E thấp có rẻ không: https://chungkhoanhuynguyen.com/hoc/dinh-gia-p-e-thap-co-re-khong-mot-quy-loi-nhuan-co-the-lam-meo-p-e.html\n"
      "Margin – con dao hai lưỡi: https://chungkhoanhuynguyen.com/hoc/margin-con-dao-hai-luoi-giam-30-mat-60-von-khi-nao-bi-call.html\n"
      "Bài học 2021–2022: https://chungkhoanhuynguyen.com/hoc/bai-hoc-lich-su-2021-2022-vn-index-tu-khoang-1-529-xuong-khoang-874.html\n"
      "Cần trao đổi riêng về kế hoạch tài chính: Zalo 0365.188.286\n\n"
      "Nhân vật anh Tùng, vợ, anh Quân, chú Bình là hư cấu; số liệu là thật theo nguồn trên.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-18', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['tiền vào chứng khoán', 'thanh khoản thấp nhất 21 tháng', 'thanh khoản chứng khoán', 'khối ngoại bán ròng', 'VN-Index hôm nay', 'P/E VN-Index', 'nâng hạng FTSE', 'chứng khoán hôm nay', 'tin nóng tài chính', 'margin'],
    bia_hook=['TIỀN VÀO CK', 'ĐÁY 21 THÁNG'], badge='TIỀN ĐI ĐÂU?',
    bia_anh='Ho Chi Minh City skyline night||Ho Chi Minh City skyline night',
    bia_hook_b=['50.000 TỶ', 'CÒN 15.600 TỶ'], badge_b='MỖI PHIÊN TRÊN HOSE',
    bia_hook_c=['SÀN VẮNG', 'P/E 10,8???'], badge_c='SÁT ĐÁY COVID 10,3',
    reel_hook='TIỀN VÀO CHỨNG KHOÁN|THẤP NHẤT 21 THÁNG???',
    fb_post=("Tiền vào chứng khoán thấp nhất 21 tháng 😳\n\n👉 Tháng 8/2025: khoảng 50.000 tỷ mỗi phiên\n👉 Tháng 10/2026: khoảng 15.600 tỷ\n"
             "👉 Nhưng P/E VN-Index chỉ 10,8 lần – sát đáy Covid\n\nTiền trong cổ phiếu của anh chị có cần dùng trong 12 tháng tới?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 18/11: tiền vào chứng khoán thấp nhất 21 tháng (NV1B 18/11/2026).\n"
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
sys.path.insert(0, CW + '/_video')
try:
    import xung_ho
    for i, c in enumerate(S, 1):
        if xung_ho.le_phep(c['say']) != c['say']: print('XUNG_HO doi canh', i)
except Exception as e: print('xung_ho?', e)
