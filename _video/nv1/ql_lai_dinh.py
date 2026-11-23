# -*- coding: utf-8 -*-
# NV1 24/11/2026 – VIDEO DÀI kênh chính, "câu hỏi lớn về tiền": LÃI TIẾT KIỆM ĐÃ QUA ĐỈNH? – gửi dài hay ngắn, người vay được gì.
# Lý do chọn: data/view/xu_huong.md tuần tới 23/11: "Lãi Suất Chạm Đỉnh: Tiền Gửi Sắp Đảo Chiều, Người Vay Được Lợi?" ~80 nghìn view,
#   "Vì Sao Người Dân Ồ Ạt Rút Tiền Vàng, Chứng Khoán Đổ Vào Ngân Hàng Gửi Lãi?" ~82 nghìn, "Thanh Tra Ngân Hàng Tháng 11" ~79 nghìn.
#   Anh Huy 23/11: video dài nhiều view nhất là vĩ mô – tiền tệ (video_dai_can_doi_2311). Khác góc CH2811TP (trái phiếu 9% vs tiết kiệm).
# Nguồn (đã đọc toàn văn 24/11/2026; WiData hết credit tới 27/11):
#  - VCCI/Bnews 10/11/2026 (họp báo Chính phủ 4/11): NHNN yêu cầu giảm 0,5–1%/năm lãi huy động tiền gửi MỚI kỳ hạn từ 6 tháng; giảm 1,5–2%/năm lãi cho vay.
#    Lãi niêm yết NHTM nhà nước giảm khoảng 0,5%/năm, cổ phần 0,5–0,7%/năm. Khoản vay mới cuối tháng 10 giảm khoảng 0,2–0,5% so với đầu tháng 10.
#    Một ngân hàng số cộng 2,2 điểm, lãi thực nhận có thể tới 9,1%/năm (6 tháng niêm yết 6,9%, đến 30/11).
#  - Thị trường Tài chính Tiền tệ 1/11/2026: giảm phổ biến 0,5 điểm; phần lớn ngân hàng niêm yết 12 tháng dưới 7%; cao nhất từ 12 tháng trở lên chỉ khoảng 7%.
#  - Việt Báo 17/11/2026 (bảng online): 12 tháng Agribank, BIDV, VietinBank 6,8%; Vietcombank 5,4%. Dẫn NHNN: đến 26/10/2026 dư nợ hơn 20,81 triệu tỷ (+11,94% so cuối 2025),
#    huy động gần 19,73 triệu tỷ (+11,7%).
#  - Tạp chí Công Thương 8/10/2026 (NHNN): lãi tiền gửi bình quân giao dịch mới 6,38%/năm ngày 20/9/2026, tăng 1,15 điểm so cuối 2025.
#  - Lần trước: TT Tài chính Tiền tệ 1/12/2022: cao nhất 10,5% (13 tháng), 12 tháng có nơi 10%; TT Tài chính Tiền tệ 1/1/2023: các ngân hàng thống nhất tối đa 9,5%
#    (hưởng ứng Hiệp hội Ngân hàng); VnEconomy 12/12/2023: Vietcombank 12 tháng 4,8%, BIDV/Agribank/VietinBank 5,3%, cao nhất thị trường 12 tháng 5,7%.
#  - VN-Index: nến tuần, dữ liệu chungkhoanhuynguyen.com (tuần 11/12/2023 đóng 1.102,3; đỉnh tuần 18/5/2026 1.933,11; tuần 23/11/2026 1.697,14).
#  - Số tự tính (giả định nhân vật): 600 triệu × 10% = 60 triệu; × 5,7% = 34,2 triệu; chênh 25,8 triệu (43%).
#    Vay 1,5 tỷ, lãi giảm 1 điểm: 15 triệu/năm = 1,25 triệu/tháng. 20,81 − 19,73 = 1,08 triệu tỷ. 1.697,14 / 1.933,11 − 1 = −12,2%.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw')
sys.path.insert(0, CW + '/_video'); from phat_am import doc as phat_am_doc
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = CW + '/_video/queue/20261124_0100'
KEY = 'CH0812LS'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HCM = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline'
HN = 'ov:Hanoi skyline night||Hanoi skyline'
HO = 'ov:Ho Chi Minh City Stock Exchange||Ho Chi Minh City skyline night'
CF_L = ([-28.25, 0.15, 5.2], [-27.15, 0.15, 5.2])
CAM_CF = {'from': [[-27.4, 1.5, 2.3], [-27.7, 0.8, 5.2], 42], 'to': [[-27.6, 1.42, 3.0], [-27.7, 0.8, 5.2], 38]}
CAM_VP = {'from': [[0.9, 1.5, 4.4], [0.3, 1.3, -1.0], 44], 'to': [[0.6, 1.45, 3.4], [0.2, 1.35, -1.2], 39]}
SOFA_T = [0.35, 0, -1.85]; SOFA_P = [1.65, 0, -1.85]
CAM_PK = {'from': [[1.0, 1.3, 2.6], [1.0, 0.9, -1.8], 38], 'to': [[1.0, 1.25, 2.0], [1.0, 0.9, -1.8], 33]}
# nến tuần VN-Index: chỉ số theo thứ tự thời gian (cũ -> mới)
WK = lib.weekly('VNINDEX', 160)[::-1]
iw = lambda d: [r[0] for r in WK].index(d)
W26 = lib.weekly('VNINDEX', 26)[::-1]; iw26 = lambda d: [r[0] for r in W26].index(d)
S = [
 # ---------------- MỞ ĐẦU: tin hôm nay + túi tiền nhân vật + cú lật lần trước ----------------
 dict(k='noti', ch='Mở đầu', cap=('LÃI TIẾT KIỆM', 'ĐÃ QUA ĐỈNH?'), cols=CC, noti=dict(gio='07:10', ngay='Thứ Ba', items=[
        ('Tin tức', 'Họp báo Chính phủ 4/11', 'NHNN yêu cầu giảm 0,5 đến 1%/năm lãi tiền gửi mới, giảm 1,5 đến 2%/năm lãi cho vay', R_),
        ('Ngân hàng', 'Thông báo', 'Sổ tiết kiệm 600.000.000đ đến hạn ngày 15/12. Vui lòng chọn kỳ hạn mới', V_),
        ('Zalo', 'Chồng', 'Lãi sắp giảm thì gửi luôn 12 tháng đi em', X_)]),
      say=("Bảy giờ sáng, Trang, kế toán một công ty may, nhận cùng lúc ba tin. Ngân hàng báo sổ tiết kiệm sáu trăm triệu đồng sắp đến hạn. "
           "Báo đưa tin Ngân hàng Nhà nước yêu cầu giảm lãi tiền gửi mới từ nửa điểm đến một điểm phần trăm. Còn chồng chị nhắn: lãi sắp giảm thì gửi luôn mười hai tháng đi em. "
           "Nghe thì đơn giản. Nhưng lần trước lãi tiết kiệm quay đầu, chỉ trong khoảng một năm, có nơi trả mười phần trăm cho kỳ mười hai tháng, một năm sau nơi trả cao nhất chỉ còn năm phẩy bảy phần trăm. "
           "")),
 dict(k='bars', short=True, anh=HCM, cap=('CÙNG 600 TRIỆU, LẦN TRƯỚC', 'LÃI 60 TRIỆU HAY 34,2 TRIỆU'), cols=CR, top='TIỀN LÃI 1 NĂM CỦA 600 TRIỆU, KỲ 12 THÁNG (TRIỆU ĐỒNG, EM TỰ TÍNH)',
      bars=[('Gửi 12/2022, 10%', 60, G_, '60 triệu'), ('Gửi 12/2023, 5,7%', 34.2, R_, '34,2 triệu')],
      say=("Đặt sáu trăm triệu của Trang vào lần trước. Gửi mười hai tháng đúng lúc lãi cao, một năm nhận sáu mươi triệu đồng. "
           "Chậm đúng một năm, nơi trả cao nhất lúc đó chỉ cho ba mươi tư triệu hai trăm nghìn đồng. Mất hơn bốn mươi phần trăm tiền lãi, chỉ vì chọn kỳ hạn vào lúc nào. "
           "Hôm nay câu chuyện có lặp lại không? Cuối video có một phép thử mười giây để anh chị tự biết nên gửi kỳ dài hay ngắn.")),
 dict(k='3d', set='phongkhach', light='day', cam=CAM_PK, label='TỐI ĐÓ · NHÀ TRANG VÀ HÙNG',
      cast=[{'a': 'trang', 'p': SOFA_T, 'act': 'dienthoai', 'ngoi': True, 'expr': 'worried'},
            {'a': 'hung', 'p': SOFA_P, 'act': 'noi', 'ngoi': True, 'expr': 'grin'}],
      cap=('"LÃI GIẢM THÌ NHÀ MÌNH', 'ĐƯỢC HAY MẤT?"'), cols=CC,
      say=("Tối đó, Trang hỏi Hùng, chồng chị, tài xế xe tải: lãi giảm thì nhà mình được hay mất? "
           "Hùng cười: được chứ, nhà mình đang vay một tỷ rưỡi mua nhà, lãi thả nổi, tức ngân hàng điều chỉnh theo từng kỳ, lãi vay giảm thì mỗi tháng trả bớt. "
           "Trang lắc đầu: nhưng sáu trăm triệu tiết kiệm của em thì lãi cũng giảm. Một nhà, hai túi tiền, đi theo hai hướng ngược nhau.")),
 # ---------------- CHƯƠNG 1: vì sao lãi từng lên ----------------
 dict(k='giay', ch='Chương 1 – Vì sao lãi tiết kiệm từng lên?', cap=('LÃI TIỀN GỬI BÌNH QUÂN', 'LÊN 6,38%'), cols=CC, moc=True, giay=dict(
        tieu_de='LÃI TIỀN GỬI GIAO DỊCH MỚI', so='NHNN – Tạp chí Công Thương 8/10/2026', dau='ĐÃ CÔNG BỐ', dieu=[
        ('Bình quân ngày 20/9/2026', '6,38% MỘT NĂM'),
        ('So với cuối năm 2025', 'TĂNG 1,15 ĐIỂM'),
        ('Lãi điều hành của NHNN', 'GIỮ NGUYÊN')]),
      say=("Muốn biết lãi sẽ đi đâu, phải hiểu vì sao nó từng lên. Theo Ngân hàng Nhà nước, ngày hai mươi tháng chín, lãi tiền gửi bình quân cho các khoản gửi mới là khoảng sáu phẩy bốn phần trăm. "
           "Con số đó cao hơn cuối năm ngoái hơn một điểm phần trăm, trong khi lãi điều hành, tức lãi suất Ngân hàng Nhà nước dùng để định hướng thị trường, vẫn giữ nguyên.")),
 dict(k='cards', anh=HN, cap=('NGÂN HÀNG CHO VAY NHANH', 'HƠN TIỀN GỬI VÀO'), cols=CR, moc=True, cards=[
        ('20,81 triệu tỷ', 'Dư nợ cho vay đến 26/10', 'Tăng 11,94% từ đầu năm'),
        ('19,73 triệu tỷ', 'Vốn huy động cùng ngày', 'Tăng 11,7% từ đầu năm')],
      say=("Lý do nằm ở hai đường chạy. Đến cuối tháng mười, cho vay tăng gần mười hai phần trăm từ đầu năm, tiền huy động vào tăng chậm hơn một chút. "
           "Theo báo VnBusiness, tín dụng tăng nhanh hơn huy động là lý do chính khiến các ngân hàng phải nâng lãi để hút tiền gửi.")),
 dict(k='chat', cap=('"BÊN KIA CỘNG THÊM', 'LÃI 9,1% ĐẤY"'), cols=CC, moc=True, chat=dict(ten='Cường', tv='Đang hoạt động', gio='21:15', mau=V_, msgs=[
        ('Cường', 'Tôi vừa gửi online, được cộng thêm, thực nhận 9,1%'),
        ('Cường', 'Bảo vợ ông chuyển sang đi'),
        ('me', 'Kỳ hạn bao lâu? Ưu đãi đến bao giờ?'), ('me', 'Sổ vợ tôi 15/12 mới đến hạn')]),
      say=("Đúng lúc đó Cường, người quen của Hùng, nhắn rằng anh vừa gửi online, được cộng thêm lãi, thực nhận chín phẩy một phần trăm, và rủ vợ Hùng chuyển sang. "
           "Hùng hỏi lại hai câu: kỳ hạn bao lâu, và ưu đãi đến bao giờ? Vì sổ của Trang phải đến ngày mười lăm tháng mười hai mới đến hạn.")),
 dict(k='giay', cap=('9,1% ĐÃ GỒM 2,2 ĐIỂM CỘNG', 'NIÊM YẾT CHỈ 6,9%'), cols=CR, moc=True, giay=dict(
        tieu_de='MỨC 9,1% NẰM Ở ĐÂU?', so='VCCI 10/11/2026 · TT Tài chính Tiền tệ 1/11/2026', dau='ĐỌC KỸ', dieu=[
        ('Lãi niêm yết kỳ 6 tháng', '6,9%'),
        ('Cộng thêm khi gửi online', '2,2 ĐIỂM'),
        ('Thời hạn ưu đãi', 'ĐẾN 30/11'),
        ('Phần lớn 12 tháng niêm yết', 'DƯỚI 7%')]),
      say=("Hai câu hỏi đó trúng chỗ. Theo báo VCCI, mức chín phẩy một phần trăm là lãi niêm yết sáu phẩy chín phần trăm cộng thêm hai phẩy hai điểm, chỉ khi gửi online, và ưu đãi chỉ kéo dài đến cuối tháng mười một. "
           "Ưu đãi hết trước khi sổ của Trang đến hạn, nên con số đó không phải của chị. Còn lãi niêm yết, tức mức ngân hàng công bố chính thức trên biểu lãi, thì khác. "
           "Đầu tháng mười một, phần lớn ngân hàng niêm yết kỳ mười hai tháng dưới bảy phần trăm.")),
 # ---------------- CHƯƠNG 2: cú lật ----------------
 dict(k='noti', ch='Chương 2 – Cú quay đầu đã bắt đầu', cap=('NHNN YÊU CẦU', 'GIẢM 0,5 ĐẾN 1%'), cols=CR, moc=True, noti=dict(gio='16:30', ngay='Thứ Tư 4/11', items=[
        ('Tin tức', 'Họp báo Chính phủ', 'Lãi tiền gửi mới kỳ hạn từ 6 tháng: giảm 0,5 đến 1%/năm', R_),
        ('Tin tức', 'Họp báo Chính phủ', 'Lãi cho vay: giảm 1,5 đến 2%/năm', G_),
        ('Tin tức', 'Thị trường', 'Lãi niêm yết đã giảm khoảng 0,5 đến 0,7%/năm', V_)]),
      say=("Quay lại tin sáng hôm đó, giờ nói rõ hơn. Tại họp báo Chính phủ ngày bốn tháng mười một, Ngân hàng Nhà nước cho biết đã yêu cầu giảm lãi tiền gửi mới, áp dụng cho kỳ hạn từ sáu tháng. "
           "Lãi cho vay phải giảm mạnh hơn. Đó là cú quay đầu.")),
 dict(k='bignum', anh=HCM, cap=('LÃI VAY YÊU CẦU GIẢM', '1,5 ĐẾN 2 ĐIỂM'), cols=CC, moc=True, value=2, fmt='{:,.0f}', unit=' ĐIỂM %', top='MỨC GIẢM LÃI CHO VAY NHNN YÊU CẦU (TỐI ĐA)',
      sub='Khoản vay mới cuối tháng 10 (trước họp báo) giảm 0,2 đến 0,5% – VCCI 10/11/2026', col=GOLD,
      say=("Đây là chỗ nhiều người bỏ qua. Lãi cho vay được yêu cầu giảm từ một phẩy năm đến hai điểm phần trăm. "
           "Còn số đo được trước buổi họp báo, đến cuối tháng mười, khoản vay mới chỉ giảm khoảng từ không phẩy hai đến không phẩy năm điểm phần trăm. Người vay còn phải chờ.")),
 dict(k='giay', short=True, cap=('VAY 1,5 TỶ, LÃI GIẢM 1 ĐIỂM', 'BỚT 1,25 TRIỆU MỖI THÁNG'), cols=CC, moc=True, giay=dict(
        tieu_de='PHÉP TÍNH CỦA HÙNG', so='Em giả định, em tự tính', dau='TỰ TÍNH', dieu=[
        ('Dư nợ vay mua nhà', '1,5 TỶ'),
        ('Giả định lãi giảm', '1 ĐIỂM %'),
        ('Tiền lãi bớt mỗi năm', '15 TRIỆU'),
        ('Bớt mỗi tháng', '1,25 TRIỆU')]),
      say=("Hùng lấy giấy tính. Em giả định kỳ điều chỉnh tới, lãi khoản vay một tỷ rưỡi của anh giảm một điểm phần trăm. "
           "Mỗi năm anh bớt mười lăm triệu đồng tiền lãi, tức khoảng một triệu hai trăm năm mươi nghìn đồng mỗi tháng. "
           "Nhưng giảm bao nhiêu, và từ kỳ nào, nằm trong hợp đồng của anh, không nằm trên tin tức.")),
 dict(k='3d', set='vanphong', light='day', cam=CAM_VP, label='HÙNG HỎI HUY NGUYỄN',
      cast=[{'a': 'huy', 'p': [-0.7, 0, 0.5], 'act': 'chitay', 'side': -1, 'expr': 'smile'},
            {'a': 'hung', 'p': [0.9, 0, 0.7], 'act': 'noi', 'side': -1, 'expr': 'worried'}],
      cap=('KHOẢN VAY CŨ', 'ĐIỀU CHỈNH THEO HỢP ĐỒNG'), cols=CC,
      say=("Hùng hỏi em: yêu cầu giảm lãi vay rồi, sao ngân hàng chưa báo gì? Em trả lời: "
           "khoản vay cũ thả nổi thường chỉ điều chỉnh theo kỳ ghi trong hợp đồng, có nơi ba tháng, có nơi sáu tháng một lần. "
           "Anh nên mở hợp đồng ra xem ngày điều chỉnh và công thức tính lãi, trước khi mừng.")),
 # ---------------- CHƯƠNG 3: lần trước ----------------
 dict(k='call', ch='Chương 3 – Lần trước lãi quay đầu', cap=('"CUỐI NĂM 2022', 'BÁC GỬI 1 THÁNG MỘT"'), cols=CR, moc=True, call=dict(ten='Bác Sáu', phu='Hàng xóm', mau=R_, loi=[
        'Cuối năm 2022 bác gửi 1 tháng một', 'Năm sau lãi tụt, bác tiếc mãi']),
      say=("Trang gọi cho bác Sáu, hàng xóm đã nghỉ hưu, người gửi tiết kiệm mấy chục năm. Bác kể: cuối năm hai nghìn không trăm hai mươi hai, lãi lên rất cao, nhưng bác sợ còn lên nữa nên chỉ gửi từng tháng một, đến hạn lại tái tục, tức gửi lại kỳ mới theo lãi lúc đó. "
           "Sang năm sau lãi tụt dần, mỗi lần tái tục lại thấp hơn lần trước. Bác Sáu là nhân vật hư cấu, nhưng những con số bác nhắc là thật.")),
 dict(k='giay', cap=('NHỮNG CON SỐ', 'CỦA LẦN TRƯỚC'), cols=CR, moc=True, giay=dict(
        tieu_de='LÃI TIẾT KIỆM 2022 ĐẾN 2023', so='TT Tài chính Tiền tệ 1/12/2022, 1/1/2023 · VnEconomy 12/12/2023', dau='LẦN TRƯỚC', dieu=[
        ('12 tháng, có nơi trả, đầu 12/2022', '10%'),
        ('Trần các ngân hàng thống nhất 1/2023', '9,5%'),
        ('12 tháng, cao nhất thị trường, 12/2023', '5,7%'),
        ('Vietcombank 12 tháng, 12/2023', '4,8%')]),
      say=("Những con số của lần trước. Đầu tháng mười hai năm đó, có nơi trả mười phần trăm cho kỳ mười hai tháng. Sang tháng một năm sau, các ngân hàng thống nhất trần chín phẩy năm phần trăm. "
           "Đến tháng mười hai năm sau, nơi trả cao nhất cho kỳ mười hai tháng chỉ còn năm phẩy bảy phần trăm, Vietcombank còn bốn phẩy tám phần trăm. "
           "Đó chính là hai con số sáu mươi triệu và ba mươi tư triệu ở đầu phim.")),
 dict(k='hook', cap=('12/2023: VIETCOMBANK 4,8%', 'VN-INDEX QUANH 1.100'), cols=CC, label='VN-Index – nến tuần, 160 tuần gần nhất',
      chart=dict(sym='VNIW', weeks=160, mas=[(20, (255, 196, 0))], circles=[
          [iw('2023-12-11'), 1102.3, '12/2023: Vietcombank 12 tháng còn 4,8%', 2.0],
          [iw('2026-05-18'), 1933.11, 'Đỉnh tuần 18/5/2026: 1.933', 5.0],
          [iw('2026-11-23'), 1697.14, 'Tuần 23/11/2026: 1.697', 8.0]]),
      say=("Còn chứng khoán thì sao? Đây là nến tuần của VN-Index ba năm qua. Tháng mười hai năm đó, khi Vietcombank trả bốn phẩy tám phần trăm cho kỳ mười hai tháng, chỉ số ở quanh mốc một nghìn một trăm điểm. "
           "Từ đó chỉ số đi lên, chạm đỉnh tuần vào tháng năm năm nay. Tuần này, chỉ số thấp hơn đỉnh khoảng mười hai phần trăm.")),
 dict(k='hook', cap=('LÃI TIẾT KIỆM CHỈ LÀ', 'MỘT LỰC KÉO'), cols=CC, label='VN-Index – 26 tuần gần nhất',
      chart=dict(sym='VNIW', weeks=26, mas=[(10, (56, 189, 248))], hlines=[[1697.14, 'Tuần 23/11/2026: 1.697', (255, 196, 0), 1.5]],
                 circles=[[iw26('2026-07-20'), 1686.11, 'Tuần 20/7: 1.686', 3.0], [iw26('2026-08-31'), 1853.08, 'Tuần 31/8: 1.853', 5.0]]),
      say=("Nửa năm gần đây, chỉ số lên xuống trong một vùng khá hẹp. Lãi tiết kiệm chỉ là một lực kéo, bên cạnh lợi nhuận doanh nghiệp, tỷ giá và dòng tiền nước ngoài. "
           "Em không nói nên mua hay bán.")),
 dict(k='checklist', anh=HCM, cap=('LẦN TRƯỚC VÀ HÔM NAY', 'GIỐNG 2, KHÁC 2'), cols=CC, moc=True, items=[
        ('Giống: lãi lên cao rồi bị kéo xuống', R_), ('Giống: có thống nhất, yêu cầu hạ lãi', R_),
        ('Khác: đỉnh niêm yết quanh 7%', G_), ('Khác: có ưu đãi cộng thêm có hạn', V_)],
      say=("Đặt lần trước cạnh hôm nay. Giống nhau hai điểm: lãi lên cao rồi bị kéo xuống, và đều có thống nhất hay yêu cầu hạ lãi. "
           "Khác nhau hai điểm: đỉnh niêm yết hôm nay thấp hơn nhiều, quanh bảy phần trăm chứ không phải mười phần trăm. Và hôm nay có những ưu đãi cộng thêm, có hạn, có điều kiện. "
           "Giống, không có nghĩa là lặp lại y hệt.")),
 # ---------------- CHƯƠNG 4: Trang chọn gì ----------------
 dict(k='giay', ch='Chương 4 – Sáu trăm triệu của Trang', cap=('SỔ 600 TRIỆU', 'CẦN DÙNG BAO NHIÊU?'), cols=CC, moc=True, giay=dict(
        tieu_de='SỔ TÀI SẢN NHÀ TRANG', so='Em giả định', dau='GIẢ ĐỊNH', dieu=[
        ('Sổ tiết kiệm đến hạn 15/12', '600 TRIỆU'),
        ('Học phí con, sửa xe trong 12 tháng', '150 TRIỆU'),
        ('Quỹ dự phòng giữ riêng', '100 TRIỆU'),
        ('Phần chưa cần đến trong 12 tháng', '350 TRIỆU')]),
      say=("Trang mở sổ ra tính, em giả định như sau. Sáu trăm triệu, trong mười hai tháng tới có khoảng một trăm năm mươi triệu sẽ phải tiêu cho học phí con và sửa xe. "
           "Một trăm triệu giữ làm quỹ dự phòng. Còn ba trăm năm mươi triệu, Trang chắc chắn chưa cần đến trong một năm.")),
 dict(k='cards', anh=HN, cap=('3 CÁCH ĐẶT', 'SÁU TRĂM TRIỆU'), cols=CC, moc=True, cards=[
        ('Kỳ ngắn', 'Tiền sắp tiêu, dự phòng', 'Lãi thấp, rút dễ'),
        ('Kỳ 12 tháng', 'Tiền chưa cần trong năm', 'Giữ mức lãi hiện tại'),
        ('Chia bậc thang', 'Nhiều sổ, nhiều ngày đến hạn', 'Không đoán đúng đỉnh')],
      say=("Có ba cách đặt. Một, tiền sắp tiêu và tiền dự phòng để kỳ ngắn, lãi thấp nhưng rút dễ. "
           "Hai, tiền chắc chắn chưa cần trong năm thì kỳ mười hai tháng, giữ mức lãi của hôm nay nếu lãi tiếp tục giảm. "
           "Ba, chia thành nhiều sổ đến hạn vào các tháng khác nhau, gọi là bậc thang, để không phải đoán đúng đỉnh.")),
 dict(k='chat', cap=('"RÚT TRƯỚC HẠN', 'CHỈ ĐƯỢC LÃI KHÔNG KỲ HẠN"'), cols=CR, moc=True, chat=dict(ten='Hùng', tv='Đang hoạt động', gio='22:05', mau=X_, msgs=[
        ('Hùng', 'Sao không gửi hết 12 tháng cho lãi cao?'),
        ('me', 'Nhỡ giữa năm cần tiền, rút trước hạn thường chỉ được lãi không kỳ hạn'),
        ('me', 'Em chỉ khóa phần chưa dùng đến thôi')]),
      say=("Hùng vẫn hỏi: sao không gửi hết mười hai tháng cho lãi cao? Trang trả lời rằng nếu giữa năm cần tiền, rút trước hạn thì phần đó thường chỉ được lãi không kỳ hạn, gần như không có gì. "
           "Chị chỉ khóa phần tiền chưa dùng đến.")),
 dict(k='cards', anh=HCM, cap=('KẾ HOẠCH CỦA TRANG', 'GIỮ TIỀN, KHÔNG ĐOÁN ĐỈNH'), cols=CC, moc=True, cards=[
        ('350 triệu', 'Kỳ 12 tháng, nơi niêm yết rõ', 'Không chạy theo quảng cáo'),
        ('150 triệu', 'Chia 3 sổ kỳ ngắn', 'Đến hạn đúng tháng cần tiêu'),
        ('100 triệu', 'Quỹ dự phòng', 'Rút được ngay')],
      say=("Kế hoạch cuối cùng của Trang: ba trăm năm mươi triệu gửi mười hai tháng ở nơi niêm yết rõ ràng, đọc kỹ điều kiện nếu có ưu đãi. "
           "Một trăm năm mươi triệu chia ba sổ kỳ ngắn, đến hạn đúng tháng cần tiêu, đó chính là bậc thang. Một trăm triệu để dự phòng. "
           "Còn Hùng hẹn mở hợp đồng vay để xem ngày điều chỉnh lãi. Mỗi người trong nhà soi đúng túi tiền của mình.")),
 dict(k='checklist', anh=HN, cap=('PHÉP THỬ CỦA ANH CHỊ', 'TIỀN CẦN DÙNG TRONG 12 THÁNG'), cols=CC, moc=True, items=[
        ('Dưới 30%: phần lớn có thể khóa dài', G_),
        ('30 đến 60%: chia bậc thang', V_),
        ('Trên 60%: ưu tiên kỳ ngắn, dễ rút', R_)],
      say=("Em gợi ý một phép thử, đây là mốc tự soi, không phải lời khuyên chung. Anh chị tính xem trong tiền tiết kiệm, bao nhiêu phần trăm sẽ cần dùng trong mười hai tháng tới. "
           "Dưới ba mươi phần trăm, phần lớn có thể khóa kỳ dài. Từ ba mươi đến sáu mươi phần trăm, chia bậc thang. Trang cần hai trăm năm mươi trên sáu trăm triệu, khoảng bốn mươi hai phần trăm, nên chị chia bậc thang. Trên sáu mươi phần trăm, ưu tiên kỳ ngắn, dễ rút, đừng chạy theo ưu đãi dài hạn.")),
 dict(k='checklist', anh=HO, cap=('3 ĐIỀU NÊN THEO DÕI', 'TỪ NAY ĐẾN TẾT'), cols=CC, moc=True, items=[
        ('3 ngân hàng lớn: 12 tháng dưới 6,5%?', V_),
        ('Có đợt ưu đãi mới trước Tết?', V_),
        ('Ngày điều chỉnh lãi khoản vay của mình', R_)],
      say=("Ba điều nên theo dõi từ nay đến Tết. Một, ba ngân hàng lớn đang niêm yết sáu phẩy tám phần trăm cho kỳ mười hai tháng, mức đó có xuống dưới sáu phẩy năm phần trăm hay chưa. "
           "Hai, đợt ưu đãi cộng thêm đã hết ngày ba mươi tháng mười một, ngân hàng có tung đợt mới trước Tết hay không. Ba, ngày điều chỉnh lãi trong hợp đồng vay của chính mình. "
           "Biểu lãi suất và số liệu vĩ mô hằng tháng, em để miễn phí trên web chứng khoán Huy Nguyễn chấm com.")),
 dict(k='3d', ch='Kết', set='cafevh', light='day', cam=CAM_CF, label='SÁNG HÔM SAU · QUÁN NƯỚC',
      cast=[{'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'},
            {'a': 'cuong', 'p': CF_L[0], 'act': 'dienthoai', 'ngoi': True, 'expr': 'relief'}],
      cap=('"LÃI CAO NHẤT CHƯA CHẮC', 'LÀ LÃI CỦA MÌNH"'), cols=CC,
      say=("Sáng hôm sau, Cường đọc lại điều kiện ưu đãi của mình rồi gãi đầu: hóa ra mức chín phẩy một phần trăm chỉ có đến cuối tháng. "
           "Hùng cười, kể rằng vợ anh hay nói: lãi cao nhất trên quảng cáo chưa chắc là lãi của mình. Lãi của mình là số tiền thực nhận, tính cả những lần phải rút giữa chừng.")),
 dict(k='end', cap=('GỬI NHƯ TRANG', 'HAY NHƯ HÙNG?'), cols=CC,
      say=("Còn anh chị chọn như Trang, chia bậc thang theo số tiền cần dùng, hay như Hùng, gửi hết mười hai tháng cho lãi cao? "
           "Anh chị gõ chữ Trang hoặc chữ Hùng vào phần bình luận, kèm phần trăm tiền nhà mình cần dùng trong năm tới nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=50)
for c in S: c['say'] = lib.doc(phat_am_doc(c['say']))
TIEU = 'Lãi Tiết Kiệm Qua Đỉnh? Lần Trước 10% Còn 5,7% Sau 1 Năm'
MT = ("Ngân hàng Nhà nước yêu cầu giảm 0,5–1%/năm lãi tiền gửi mới kỳ hạn từ 6 tháng (họp báo Chính phủ 4/11/2026). Lãi tiết kiệm đã qua đỉnh? "
      "Lần trước lãi quay đầu: tháng 12/2022 có nơi trả 10% cho kỳ 12 tháng, một năm sau nơi trả cao nhất chỉ còn 5,7%. Câu chuyện nhà Trang – Hùng: một nhà, hai túi tiền, sổ tiết kiệm 600 triệu và khoản vay mua nhà 1,5 tỷ.\n\n"
      "Nguồn số liệu:\n"
      "• VCCI/Bnews 10/11/2026 (họp báo Chính phủ 4/11): NHNN yêu cầu giảm 0,5–1%/năm lãi huy động tiền gửi mới kỳ hạn từ 6 tháng, giảm 1,5–2%/năm lãi cho vay; lãi niêm yết NHTM nhà nước giảm khoảng 0,5%, cổ phần 0,5–0,7%; khoản vay mới cuối tháng 10 giảm khoảng 0,2–0,5%; một ngân hàng số cộng 2,2 điểm, thực nhận tới 9,1% (6 tháng niêm yết 6,9%, đến 30/11)\n"
      "• Thị trường Tài chính Tiền tệ 1/11/2026: phần lớn ngân hàng niêm yết 12 tháng dưới 7%\n"
      "• VnBusiness 10/11/2026: tín dụng tăng nhanh hơn huy động là lý do chính khiến ngân hàng nâng lãi huy động\n"
      "• Việt Báo 17/11/2026: 12 tháng Agribank, BIDV, VietinBank 6,8%, Vietcombank 5,4%; số liệu NHNN: đến 26/10/2026 dư nợ hơn 20,81 triệu tỷ (+11,94%), huy động gần 19,73 triệu tỷ (+11,7%)\n"
      "• Tạp chí Công Thương 8/10/2026 (NHNN): lãi tiền gửi bình quân giao dịch mới 6,38%/năm ngày 20/9/2026, +1,15 điểm so cuối 2025\n"
      "• Thị trường Tài chính Tiền tệ 1/12/2022 (cao nhất 10,5% kỳ 13 tháng; 12 tháng có nơi 10%) và 1/1/2023 (các ngân hàng thống nhất tối đa 9,5%); VnEconomy 12/12/2023 (Vietcombank 12 tháng 4,8%, BIDV – Agribank – VietinBank 5,3%, cao nhất thị trường 12 tháng 5,7%)\n"
      "• VN-Index: nến tuần – dữ liệu chungkhoanhuynguyen.com\n"
      "• Em tự tính (giả định nhân vật): 600 triệu × 10% = 60 triệu; × 5,7% = 34,2 triệu (có nơi trả 10% tháng 12/2022 so với mức cao nhất thị trường tháng 12/2023); chênh 25,8 triệu (43%). Trang cần 250/600 ≈ 42%. Vay 1,5 tỷ, lãi giảm 1 điểm = 15 triệu/năm ≈ 1,25 triệu/tháng. 20,81 − 19,73 = 1,08 triệu tỷ. VN-Index: tuần 11/12/2023 đóng 1.102,3; đỉnh tuần 18/5/2026 1.933,11; tuần 23/11/2026 1.697,14 (≈ −12,2% so đỉnh)\n\n"
      "Biểu lãi suất, số liệu vĩ mô hằng tháng: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng: Zalo 0365.188.286\n\n"
      "Nhân vật Trang, Hùng, Cường, bác Sáu là hư cấu; số liệu là thật. Phép thử là mốc tự soi, không phải lời khuyên đầu tư hay gửi tiền cụ thể.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Câu hỏi lớn về tiền', ngay='2026-12-08', gio_goi_y='12:00', gio='12:00', nhac='lofi', can_duyet='anh Huy duyệt trước khi hẹn',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['lãi suất tiết kiệm', 'lãi suất ngân hàng', 'lãi suất huy động', 'gửi tiết kiệm', 'lãi suất cho vay', 'Ngân hàng Nhà nước', 'lãi suất 2026', 'vay mua nhà', 'VN-Index', 'kinh tế Việt Nam'],
    bia_hook=['60 TRIỆU', 'HAY 34,2 TRIỆU?'], badge='CÙNG SỔ 600 TRIỆU',
    bia_anh='ov:Ho Chi Minh City skyline night||Hanoi skyline night',
    bia_hook_b=['LÃI TIẾT KIỆM', 'QUA ĐỈNH?'], badge_b='NHNN YÊU CẦU GIẢM LÃI',
    bia_hook_c=['GỬI DÀI', 'HAY GỬI NGẮN?'], badge_c='PHÉP THỬ 10 GIÂY',
    reel_hook='LÃI TIẾT KIỆM|ĐÃ QUA ĐỈNH???',
    fb_post=("Lãi tiết kiệm đã qua đỉnh? NHNN vừa yêu cầu giảm 0,5–1%/năm lãi tiền gửi mới.\n"
             "👉 Lần trước: tháng 12/2022 có nơi trả 10% kỳ 12 tháng, 1 năm sau cao nhất chỉ còn 5,7%\n👉 Cùng 600 triệu: lãi 60 triệu hay 34,2 triệu – chỉ vì chọn kỳ hạn lúc nào\n👉 Người vay: yêu cầu giảm 1,5–2%, thực tế mới 0,2–0,5%\n"
             "Anh chị đang gửi kỳ dài hay kỳ ngắn?\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – Câu hỏi lớn về tiền: LÃI TIẾT KIỆM QUA ĐỈNH? (NV1 24/11/2026). Có cảnh 3D + 2 nến VN-Index.\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'VNIW': lib.weekly('VNINDEX', 160)}, open(LO + '/px_tuan.json', 'w'), ensure_ascii=False)
if __name__ == '__main__':
    from collections import Counter
    cnt = Counter(c['k'] for c in S)
    print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'tieu de', len(TIEU))
    for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
    for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
    import kiem_loi, kiem_goi
    print('goi', kiem_goi.kiem(TIEU, META[KEY]['bia_hook']))
    for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
        if 'câu cụt' not in q: print(q)
    from xung_ho import le_phep
    for c in S:
        if le_phep(c['say']) != c['say']: print('XUNG_HO', c['say'][:80])
    for c in S:
        for x in c.get('cap', ()):
            if len(x) > 32: print('CAP DAI', len(x), x)
