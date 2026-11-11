# -*- coding: utf-8 -*-
# NV1B 11/11/2026 – VIDEO NÓNG kênh chính: "IPO thành công, cổ phiếu lao dốc" (Nhà Đầu Tư 11/11/2026 07:00).
# Nguồn:
#  - Nhà Đầu Tư 11/11/2026 "IPO thành công, cổ phiếu lao dốc: Niềm tin nhà đầu tư bị bào mòn": UBCKNN (bà Lê Thị Việt Nga) – cuối 2025 → 10/2026: 10 DN IPO, 60.900 tỷ;
#    2021–2024: 16 DN, ~6.500 tỷ. LPS IPO 141,8 triệu cp giá 30.000, phân phối 100%, ~1.005 NĐT; niêm yết HOSE 18/8. DVV IPO 54.800, phiên đầu 2/11 có lúc 45.000,
#    sau đó 2 phiên giảm sàn. HPA giảm ~30% so với giá IPO sau điều chỉnh cổ tức. DMX IPO 80.000, 13.315 tỷ, 93%, 90% thuộc 30 tổ chức.
#  - vnbusiness 26/8/2026: TCX giá IPO 46.800, huy động >10.800 tỷ; VPX 375 triệu cp giá 33.900, ~12.713 tỷ.
#  - Giá đóng cửa 10/11/2026 (dữ liệu web): LPS 15.800; DVV 47.000; TCX 28.850; VPX 23.300; DMX 75.300.
#  - Tinnhanhchungkhoan 11/11: HIO (Helio Energy) chào sàn HOSE 16/11, giá tham chiếu 9.900.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261111_0815_nong'
KEY = 'NONG1111A'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HA = 'Chị Hà'; NHOM = 'Hội săn IPO'
S = [
 # ---------------- MỞ ĐẦU: cảnh đắt nhất ----------------
 dict(k='noti', ch='Mở đầu', cap=('300 TRIỆU', 'CÒN 158 TRIỆU'), cols=CR, noti=dict(gio='14:46', ngay='Thứ Ba', items=[
        ('Chứng khoán', 'Ứng dụng giao dịch', 'LPS đóng cửa 15.800đ. Lãi/lỗ: −142.000.000đ (−47,3%)', R_),
        ('Zalo', NHOM, 'Hôm nay có mã mới chào sàn, ai đăng ký thêm không?', V_)]),
      say=("Chiều mười tháng mười một, phiên vừa đóng cửa, chị Hà mở ứng dụng chứng khoán. Ba trăm triệu chị mua cổ phiếu LPS trong đợt IPO tháng sáu, giá ba mươi nghìn đồng, giờ chỉ còn một trăm năm mươi tám triệu. "
           "Cùng lúc, nhóm Zalo săn IPO lại rung: có mã mới sắp chào sàn, ai đăng ký thêm không?")),
 dict(k='bignum', cap=('10 THƯƠNG VỤ IPO', 'CUỐI 2025 → 10/2026'), cols=CC, value=60900, fmt='{:,.0f}', unit=' tỷ', top='TIỀN NHÀ ĐẦU TƯ ĐÃ BỎ VÀO', sub='Gấp ~9 lần cả giai đoạn 2021–2024', col=GOLD,
      say=("Chị Hà không phải người duy nhất. Theo Ủy ban Chứng khoán Nhà nước, từ cuối năm 2025 đến tháng mười năm nay, mười doanh nghiệp IPO đã huy động sáu mươi nghìn chín trăm tỷ đồng. "
           "Con số này gấp khoảng chín lần cả bốn năm 2021 đến 2024 cộng lại. Báo Nhà Đầu Tư sáng nay đặt một câu hỏi rất thẳng: IPO thành công, sao cổ phiếu lại lao dốc? "
           "Sáu mươi nghìn tỷ đó đã đi đâu, ai hưởng lợi, và ai đang ôm lỗ?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Suất mua 30.000 đồng', cap=('"MUA GIÁ GỐC', 'LÊN SÀN LÀ LÃI"'), cols=CC, moc=True, chat=dict(ten=NHOM, tv='214 thành viên', gio='20:15', mau=X_, msgs=[
        ('Long', 'IPO giá 30.000, phân phối kín 100% rồi các bác ơi'),
        ('Long', 'Mua giá gốc, lên sàn là có lãi, như gửi tiết kiệm mà lãi hơn'),
        ('me', 'Em có 300 triệu, mua hết vào có ổn không anh?'),
        ('Long', 'Giá IPO là giá thấp nhất rồi em, sợ gì')]),
      say=("Quay lại tháng sáu. Trong nhóm săn IPO, anh Long, người lập nhóm, nhắn: giá ba mươi nghìn, phân phối kín một trăm phần trăm rồi các bác ơi. Mua giá gốc, lên sàn là có lãi. "
           "Chị Hà hỏi: em có ba trăm triệu, mua hết vào có ổn không anh? Anh Long trả lời một câu mà nhiều người tin: giá IPO là giá thấp nhất rồi em, sợ gì.")),
 dict(k='giay', cap=('BẢN CÁO BẠCH', 'CÓ GHI ĐIỀU NÀY'), cols=CR, giay=dict(tieu_de='ĐỢT CHÀO BÁN LẦN ĐẦU RA CÔNG CHÚNG', so='Số liệu theo báo Nhà Đầu Tư 11/11/2026', dau='ĐÃ KÝ', dieu=[
        ('Số lượng chào bán: 141,8 triệu cổ phiếu.', ''),
        ('Giá chào bán: 30.000 đồng/cổ phiếu – tổng 4.256 tỷ đồng.', 'DO BÊN BÁN ĐẶT'),
        ('Giá sau khi niêm yết: do thị trường quyết định.', 'KHÔNG CAM KẾT')]),
      say=("Nhưng giá IPO không phải giá sàn của tương lai. Đó là giá do bên bán đặt ra. Đợt chào bán của LPS gồm một trăm bốn mươi mốt phẩy tám triệu cổ phiếu. Công ty thu về khoảng bốn nghìn hai trăm năm mươi sáu tỷ đồng, từ khoảng một nghìn không trăm linh năm nhà đầu tư. "
           "Còn giá sau khi lên sàn, không ai cam kết. Tờ giấy ấy chị Hà đã ký, nhưng chưa đọc kỹ dòng cuối.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='noti', ch='Chương 2 – Ngày lên sàn', cap=('NGÀY 18/8', 'KHÔNG CÓ PHÁO HOA'), cols=CR, moc=True, noti=dict(gio='09:20', ngay='Thứ Ba', items=[
        ('Chứng khoán', 'Ứng dụng giao dịch', 'LPS chính thức giao dịch trên HOSE. Giá tham chiếu 30.000đ', X_),
        ('Chứng khoán', 'Ứng dụng giao dịch', 'Cảnh báo: LPS giảm 5 phiên liên tiếp', R_)]),
      say=("Ngày mười tám tháng tám, LPS lên sàn HOSE với giá tham chiếu ba mươi nghìn đồng. Chị Hà chờ một phiên tăng trần. Nó không đến. "
           "Đến cuối tháng chín, cổ phiếu còn khoảng mười chín nghìn chín trăm đồng, thấp hơn giá IPO khoảng ba mươi tám phần trăm. Và đến phiên mười tháng mười một, còn mười lăm nghìn tám trăm đồng, mất gần một nửa.")),
 dict(k='cards', cap=('KHÔNG CHỈ MỘT MÃ', 'GIÁ IPO → ĐÓNG CỬA 10/11'), cols=CR, moc=True,
      cards=[('LPS −47%', '30.000 → 15.800', ''), ('TCX −38%', '46.800 → 28.850', ''), ('VPX −31%', '33.900 → 23.300', '')],
      say=("Và đây không phải chuyện riêng của một mã. Cổ phiếu TCX, giá IPO bốn mươi sáu nghìn tám trăm, phiên mười tháng mười một đóng cửa hai mươi tám nghìn tám trăm năm mươi đồng. "
           "VPX, giá IPO ba mươi ba nghìn chín trăm, còn hai mươi ba nghìn ba trăm. Một mã thương hiệu mạnh như DMX, IPO tám mươi nghìn, cũng đang giao dịch quanh bảy mươi lăm nghìn ba trăm đồng.")),
 dict(k='chat', cap=('"MÃ MỚI THÌ KHÁC"', ''), cols=CR, chat=dict(ten=NHOM, tv='214 thành viên', gio='15:05', mau=X_, msgs=[
        ('Long', 'DVV phiên đầu 2/11 có lúc 45.000, IPO 54.800 các bác ạ'),
        ('Thảo', 'Lại giảm sàn rồi, hai phiên liền'),
        ('me', 'Anh Long ơi, sao lần nào lên sàn cũng thấp hơn giá mình mua?'),
        ('Long', '...')]),
      say=("Đầu tháng mười một, cả nhóm lại nín thở với DVV, doanh nghiệp đứng sau các chương trình truyền hình giải trí đình đám. Giá IPO năm mươi tư nghìn tám trăm. Phiên đầu tiên có lúc chỉ còn bốn mươi lăm nghìn, rồi hai phiên tiếp theo giảm sàn. "
           "Chị Hà gõ: anh Long ơi, sao lần nào lên sàn cũng thấp hơn giá mình mua? Lần này, anh Long chỉ gửi ba dấu chấm.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='text', ch='Chương 3 – Tiền đi đâu, ai hưởng lợi?', cap=('TIỀN ĐI ĐÂU?', 'AI HƯỞNG LỢI?'), cols=CC, moc=True, anh='ov:signing contract pen||business meeting',
      say=("Giờ em trả lời câu hỏi chính. Sáu mươi nghìn chín trăm tỷ đó đi đâu? Phần lớn về doanh nghiệp phát hành, để tăng vốn, cho vay ký quỹ, trả nợ, mở rộng sản xuất. "
           "Với doanh nghiệp, giá chào bán càng cao thì càng thu nhiều tiền mà phát hành ít cổ phiếu hơn. Đó là người hưởng lợi đầu tiên, và hoàn toàn hợp pháp.")),
 dict(k='checklist', cap=('AI ĐƯỢC – AI MẤT', 'SAU MỘT ĐỢT IPO GIÁ CAO'), cols=CC,
      items=[('Doanh nghiệp: nhận đủ tiền ngay ngày chào bán', GREEN), ('Cổ đông cũ: ít bị pha loãng, định giá công ty cao', GREEN), ('Người mua IPO: gánh rủi ro nếu giá đã "đi trước" tương lai', RED)],
      say=("Còn người mua IPO thì sao? Báo Nhà Đầu Tư viết: nếu giá IPO đã phản ánh phần lớn, thậm chí vượt trước kỳ vọng tăng trưởng, thì dư địa tăng giá sau khi lên sàn không còn nhiều. "
           "Nói cách khác, doanh nghiệp nhận đủ tiền ngay hôm chào bán. Rủi ro định giá thì chuyển sang người cầm cổ phiếu, những người như chị Hà.")),
 dict(k='call', cap=('"CHỊ CÓ NÊN', 'BÁN KHÔNG EM?"'), cols=CR, call=dict(ten='Em trai Tuấn', phu='Kế toán trưởng', mau=G_, loi=[
        'Chị đừng hỏi bán hay giữ vội',
        'Chị hỏi xem lúc mua, mình trả bao nhiêu lần lợi nhuận đã']),
      say=("Tối đó chị Hà gọi cho Tuấn, em trai làm kế toán trưởng. Chị có nên bán không em? Tuấn bảo: chị đừng hỏi bán hay giữ vội. Chị hỏi xem lúc mua, mình đã trả bao nhiêu lần lợi nhuận của công ty đã. "
           "Chị Hà im lặng. Chị chưa từng mở bản cáo bạch ra xem trang lợi nhuận.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='checklist', ch='Chương 4 – Trước suất IPO tiếp theo', cap=('3 CÂU HỎI', 'TRƯỚC KHI ĐĂNG KÝ IPO'), cols=CC, moc=True,
      items=[('Giá chào bán gấp bao nhiêu lần lợi nhuận? So với doanh nghiệp cùng ngành đang niêm yết?', GREEN),
             ('Tiền huy động dùng để làm gì: mở rộng, hay trả nợ, hay cổ đông lớn bán bớt?', GREEN),
             ('Nếu giá lên sàn thấp hơn 30%, mình chịu được không?', GOLD)],
      say=("Ngày mười sáu tháng mười một, lại có một mã mới chào sàn HOSE. Trước khi đăng ký bất kỳ suất IPO nào, em gợi ý anh chị hỏi ba câu. "
           "Một, giá chào bán gấp bao nhiêu lần lợi nhuận, so với doanh nghiệp cùng ngành đang niêm yết thì đắt hay rẻ? "
           "Hai, tiền huy động dùng làm gì, mở rộng kinh doanh, trả nợ, hay cổ đông lớn bán bớt? "
           "Ba, nếu giá lên sàn thấp hơn ba mươi phần trăm, mình có chịu được không?")),
 dict(k='text', cap=('IPO KHÔNG PHẢI VÉ SỐ', 'CÓ GIẢI CHẮC CHẮN'), cols=CC, anh='ov:balance scale||stock market',
      say=("Em không nói IPO là xấu. Có những thương vụ IPO tạo ra giá trị lớn cho cổ đông về lâu dài. Nhưng một đợt phân phối kín không có nghĩa là giá đã hợp lý. "
           "Như báo Nhà Đầu Tư nhận định, nếu nhà đầu tư thấy mua sau khi lên sàn có giá tốt hơn và ít rủi ro hơn, sức hấp dẫn của IPO sẽ khó giữ được. "
           "Muốn so nhanh P trên E và lợi nhuận từng quý của LPS, TCX, VPX với cả ngành, anh chị có thể tra miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối', cap=('"LẦN SAU', 'EM ĐỌC TRƯỚC ĐÃ"'), cols=CC, moc=True, chat=dict(ten=NHOM, tv='214 thành viên', gio='21:40', mau=X_, msgs=[
        ('Long', 'Mã mới 16/11, ai đăng ký thêm báo anh nhé'),
        ('me', 'Lần này em đọc bản cáo bạch trước đã anh'),
        ('Thảo', 'Chị gửi em trang lợi nhuận với, em cũng đọc')]),
      say=("Tối hôm đó, anh Long lại nhắn: mã mới mười sáu tháng mười một, ai đăng ký thêm báo anh nhé. Lần này chị Hà trả lời: lần này em đọc bản cáo bạch trước đã anh. "
           "Một phút sau, Thảo nhắn riêng: chị gửi em trang lợi nhuận với, em cũng đọc.")),
 dict(k='end', cap=('ANH CHỊ ĐÃ TỪNG MUA IPO', 'RỒI THẤY GIÁ THẤP HƠN?'), cols=CC,
      say=("Còn anh chị, đã từng mua cổ phiếu IPO rồi thấy giá lên sàn thấp hơn giá mình trả chưa? Lúc đó anh chị bán hay giữ, và vì sao?")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Cổ Phiếu IPO Lao Dốc: Mua 30.000 Còn 15.800 – 60.900 Tỷ Tiền Nhà Đầu Tư Đi Đâu, Ai Hưởng Lợi?'
MT = ("NÓNG 11/11/2026: 10 thương vụ IPO từ cuối 2025 đến 10/2026 huy động 60.900 tỷ đồng, gấp ~9 lần cả 2021–2024. Nhưng nhiều cổ phiếu vừa lên sàn đã thấp hơn giá chào bán: LPS từ 30.000 còn 15.800 đồng (−47%). "
      "Tiền đi đâu, ai hưởng lợi, ai ôm lỗ? Câu chuyện kể qua mắt một nhà đầu tư dồn 300 triệu vào một suất IPO.\n\n"
      "Nguồn số liệu:\n"
      "• UBCKNN: 10 DN IPO, 60.900 tỷ (cuối 2025 – 10/2026); 2021–2024: 16 DN, ~6.500 tỷ (báo Nhà Đầu Tư 11/11/2026)\n"
      "• LPS: IPO 141,8 triệu cp giá 30.000, phân phối 100%, ~1.005 nhà đầu tư; niêm yết HOSE 18/8/2026 (Nhà Đầu Tư 11/11/2026); ~19.900 ngày 29/9 (MarketTimes 29/9/2026)\n"
      "• DVV: IPO 54.800; phiên đầu 2/11 có lúc 45.000, hai phiên sau giảm sàn (Nhà Đầu Tư 11/11/2026)\n"
      "• TCX: giá IPO 46.800; VPX: giá IPO 33.900; DMX: giá IPO 80.000 (vnbusiness 26/8/2026)\n"
      "• Giá đóng cửa 10/11/2026: LPS 15.800; TCX 28.850; VPX 23.300; DMX 75.300\n"
      "• Mã mới chào sàn HOSE 16/11/2026 (tinnhanhchungkhoan 11/11/2026)\n\n"
      "Hồ sơ LPS (lợi nhuận 8 quý, P/E, P/B): https://chungkhoanhuynguyen.com/ma/LPS.html\n"
      "TCX: https://chungkhoanhuynguyen.com/ma/TCX.html · VPX: https://chungkhoanhuynguyen.com/ma/VPX.html\n"
      "Soi P/E, lợi nhuận từng quý, dòng tiền 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật chị Hà, anh Long, Thảo, Tuấn là hư cấu; số liệu là thật. Video không đánh giá trách nhiệm của bất kỳ doanh nghiệp hay đơn vị tư vấn nào.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng trong ngày', ngay='2026-11-11', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['cổ phiếu IPO', 'IPO 2026', 'LPS', 'cổ phiếu LPS', 'TCX', 'VPX', 'DVV', 'IPO lao dốc', 'có nên mua IPO', 'chứng khoán hôm nay', 'tin nóng chứng khoán'],
    bia_hook=['MUA 30.000', 'CÒN 15.800'], badge='NÓNG: CỔ PHIẾU IPO LAO DỐC',
    bia_anh='ov:stock market crash red screen||stock market',
    bia_hook_b=['60.900 TỶ', 'ĐI ĐÂU?'], badge_b='IPO: AI HƯỞNG LỢI?',
    bia_hook_c=['IPO KÍN 100%', 'VẪN −47%'], badge_c='NÓNG 11/11',
    fb_post=("10 thương vụ IPO hút 60.900 tỷ đồng – gấp ~9 lần cả 4 năm trước cộng lại. Nhưng lên sàn thì sao? 😳\n\n"
             "👉 LPS: IPO 30.000 → 15.800 (−47%)\n👉 TCX: 46.800 → 28.850\n👉 VPX: 33.900 → 23.300\n\n"
             "Tiền đi đâu, ai hưởng lợi, ai ôm lỗ – và 3 câu hỏi trước suất IPO tiếp theo.\n\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – NÓNG 11/11: cổ phiếu IPO lao dốc (NV1B 11/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
