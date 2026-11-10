# -*- coding: utf-8 -*-
# QL1 10/11/2026 – video dài #3 chuỗi "Doanh nghiệp kiếm tiền thế nào" – Thế Giới Di Động. Số liệu: WiData (ratio_nonfin_ttm, ratio_daily, eod_root_put), BCTC Q3/2026 (Thời báo Tài chính 10/2026), VnExpress (BHX lần đầu có lãi).
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261110_1100'
KEY = 'CH0312A'; CC = (WHITE, GOLD)
wk = lib.weekly('MWG'); cir = lib.circles(wk); gia = lib.close('MWG') * 1000
G0, PE0, PE1 = 39400, 343.72, 9.54
EPS0 = G0 / PE0; EPS1 = gia / PE1; boi = EPS1 / EPS0; doi_gia = (gia / G0 - 1) * 100
v = lambda x, d=0: lib.vn(x, d)
NM = [('Q3/2023', 0.59), ('Q3/2024', 2.27), ('Q3/2025', 3.94), ('Q3/2026', 6.16)]
S = [
 dict(k='hook', ch='Mở đầu', label='Thế Giới Di Động', cap=('60 ĐỒNG', 'THÀNH 616 ĐỒNG'), cols=CC, anh='electronics store Vietnam',
      chart=dict(sym='MWGW', tf='W', weeks=52, circles=[cir[0], cir[2]]),
      say="Ba năm trước, cứ mười nghìn đồng anh chị trả ở Thế Giới Di Động hay Điện Máy Xanh, công ty chỉ giữ lại được khoảng 60 đồng lợi nhuận. Bây giờ con số đó là khoảng 616 đồng, gấp hơn mười lần."),
 dict(k='bignum', cap=('GIÁ CỔ PHIẾU MWG', 'SAU 3 NĂM'), cols=CC, value=round(doi_gia, 1), fmt='+{:,.1f}', unit='%', top='%s → %s ĐỒNG' % (v(G0), v(gia)), sub='Vinamilk cùng kỳ: −16,9%', col=GREEN,
      say=("Cổ phiếu cũng đi theo. Ngày 10 tháng 11 năm 2023, MWG giá %s đồng. Hôm nay giá khoảng %s đồng, tăng khoảng %s%%. "
           "Trong khi đó, như em phân tích ở video trước, Vinamilk cùng ba năm lại giảm gần 17%%.") % (v(G0), v(gia), v(doi_gia, 1))),
 dict(k='text', cap=('CÙNG BA NĂM', 'VÌ SAO NGƯỢC NHAU?'), cols=CC, anh='supermarket aisle',
      say=("Cùng là doanh nghiệp bán lẻ hàng tiêu dùng, cùng ba năm. Một bên tăng gần gấp đôi, một bên lại giảm. "
           "Trong video này, em sẽ mổ xẻ xem Thế Giới Di Động đã làm gì để giữ lại nhiều tiền hơn trên mỗi đồng bán ra. "
           "Sau đó là rủi ro nằm ở đâu, và bài học lớn nhất khi đặt cạnh câu chuyện Vinamilk.")),
 dict(k='bars', ch='Chương 1 – Mười nghìn đồng còn lại bao nhiêu?', cap=('GIỮ LẠI TRÊN', '10.000 ĐỒNG DOANH THU'), cols=CC, moc=True,
      bars=[(q, round(p * 100), GREEN if i == 3 else BLUE, v(p * 100) + ' đ') for i, (q, p) in enumerate(NM)],
      say=("Đây là biên lợi nhuận ròng mười hai tháng của Thế Giới Di Động, đổi ra số đồng giữ lại trên mỗi mười nghìn đồng doanh thu. "
           "Quý 3 năm 2023 chỉ khoảng 59 đồng. Một năm sau lên khoảng 227 đồng, rồi 394 đồng, và quý 3 năm nay khoảng 616 đồng. "
           "Ngành bán lẻ điện máy vốn lãi mỏng, nên từ 0,6% lên 6,2% là một cú lội ngược dòng rất hiếm. Vậy tiền tăng thêm đến từ đâu?")),
 dict(k='cards', ch='Chương 2 – Cắt chi phí bán hàng', cap=('CHI PHÍ BÁN HÀNG', 'TRÊN DOANH THU'), cols=CC, moc=True, anh='electronics store Vietnam',
      cards=[('18,2%', 'chi phí bán hàng 12 tháng đến Q3/2023', ''), ('12,5%', 'chi phí bán hàng 12 tháng đến Q3/2026', ''), ('21,4%', 'biên lãi gộp hiện nay', '')],
      say=("Nguồn lớn nhất là chi phí bán hàng. Mười hai tháng đến quý 3 năm 2023, chi phí bán hàng ăn mất khoảng 18,2% doanh thu. "
           "Ba năm sau chỉ còn khoảng 12,5%. Trong khi biên lãi gộp gần như giữ nguyên quanh 20 đến 21%. "
           "Nói đơn giản, giá bán và giá vốn không đổi nhiều, nhưng tiền thuê mặt bằng, nhân sự, vận hành trên mỗi đồng doanh thu giảm mạnh. "
           "Theo giải trình của công ty trong báo cáo quý 3, đó là nhờ doanh thu tăng và vận hành tinh gọn, kiểm soát chi phí ở các chuỗi.")),
 dict(k='bignum', ch='Chương 3 – Bách Hóa Xanh: từ gánh nặng thành động cơ', cap=('BÁCH HÓA XANH', 'DOANH THU 9 THÁNG'), cols=CC, moc=True,
      value=45900, fmt='{:,.0f}', unit=' tỷ', top='9 THÁNG 2026', sub='+34% · 3.904 cửa hàng', col=GOLD, anh2='supermarket aisle',
      say=("Câu chuyện thứ hai là Bách Hóa Xanh. Chuỗi này từng là gánh nặng. Theo VnExpress, sau tám năm hoạt động, khoản lỗ lũy kế vượt 8.700 tỷ đồng. Phải đến quý 2 năm 2024, Bách Hóa Xanh mới có lãi lần đầu, khoảng 7 tỷ đồng. "
           "Chín tháng năm 2026, doanh thu Bách Hóa Xanh khoảng 45.900 tỷ đồng, tăng khoảng 34%. Số cửa hàng lên 3.904, so với khoảng 1.701 cửa hàng giữa năm 2024. "
           "Một chuỗi từng đốt tiền giờ thành động cơ tăng trưởng. Đây là ví dụ điển hình của chiến lược chịu lỗ để lấy quy mô, rồi thu hoạch khi đủ lớn.")),
 dict(k='cards', ch='Chương 4 – Kết quả quý 3 và điểm cần cẩn thận', cap=('QUÝ 3/2026', 'KỶ LỤC'), cols=CC, moc=True, anh='shopping mall Vietnam',
      cards=[('52.600 tỷ', 'doanh thu quý 3, +32%', ''), ('3.521 tỷ', 'lãi sau thuế quý 3, +97%', ''), ('≈ 38%', 'doanh thu Điện Máy Xanh từ mua trả chậm', '')],
      say=("Quý 3 năm 2026, doanh thu hợp nhất khoảng 52.600 tỷ đồng, tăng 32%. Lãi sau thuế khoảng 3.521 tỷ, tăng 97%. "
           "Chín tháng lãi khoảng 9.634 tỷ đồng, đã vượt kế hoạch cả năm 9.200 tỷ. "
           "Nhưng có một con số anh chị nên để ý: doanh thu mua trả chậm tăng khoảng 50% và chiếm khoảng 38% doanh thu nhóm Điện Máy Xanh. "
           "Bán trả chậm giúp đẩy doanh số, nhưng nó phụ thuộc vào sức khỏe tín dụng tiêu dùng. Nếu lãi suất tăng hay người vay gặp khó, phần doanh số này có thể chậm lại.")),
 dict(k='cards', ch='Chương 5 – Mua lúc lãi gần bằng 0', cap=('BÀI HỌC', 'GIÁ ĐI THEO LỢI NHUẬN'), cols=CC, moc=True, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      cards=[('%s lần' % v(PE0, 0), 'P/E ngày 10/11/2023', ''), ('%s lần' % v(PE1, 1), 'P/E hiện tại', ''), ('×%s' % v(boi, 0), 'lợi nhuận mỗi cổ phiếu', '')],
      say=("Giờ là phần thú vị nhất. Ngày 10 tháng 11 năm 2023, P trên E của MWG lên tới khoảng %s lần. Nhìn con số đó, nhiều người sẽ nói quá đắt. "
           "Nhưng P trên E cao vì lợi nhuận lúc đó gần như bằng 0, không phải vì giá cao. "
           "Ba năm sau, lợi nhuận mỗi cổ phiếu tăng gấp khoảng %s lần. Vì vậy dù giá gần gấp đôi, P trên E chỉ còn khoảng %s lần. "
           "Đặt cạnh Vinamilk: ba năm trước Vinamilk có P trên E khoảng 16 lần. Lợi nhuận ổn định nhưng tăng chậm, và giá đi xuống. "
           "Một bên mua lúc kỳ vọng thấp nhất và lợi nhuận phục hồi mạnh, một bên mua lúc kỳ vọng cao và tăng trưởng chậm.") % (v(PE0, 0), v(boi, 0), v(PE1, 1))),
 dict(k='text', ch='Chương 5 – Mua lúc lãi gần bằng 0', cap=('ĐỪNG HIỂU SAI', 'BÀI HỌC NÀY'), cols=CC, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say=("Nhưng đừng hiểu sai: không phải cứ mua cổ phiếu có lợi nhuận gần bằng 0 là sẽ thắng. Rất nhiều doanh nghiệp lãi gần bằng 0 rồi lỗ luôn. "
           "Điều khác biệt ở Thế Giới Di Động là có dấu hiệu cụ thể: chi phí bán hàng giảm dần từng quý, Bách Hóa Xanh lỗ ít dần rồi có lãi, doanh thu trên cửa hàng hiện hữu tăng. "
           "Người thắng không phải người đoán đáy, mà là người theo dõi những con số đó đổi chiều.")),
 dict(k='checklist', ch='Chương 6 – Ba dấu hiệu doanh nghiệp đang hồi phục thật', cap=('3 DẤU HIỆU', 'HỒI PHỤC THẬT'), cols=CC, anh='Ho Chi Minh City skyline',
      items=[('Chi phí trên doanh thu giảm đều', GREEN), ('Mảng lỗ lỗ ít dần, rồi có lãi', GREEN), ('Doanh thu cửa hàng cũ tăng', GOLD)],
      say=("Rút gọn lại, khi một doanh nghiệp đang lãi mỏng, em nhìn ba dấu hiệu. "
           "Một, chi phí trên mỗi đồng doanh thu có giảm đều qua nhiều quý không. "
           "Hai, mảng đang lỗ có lỗ ít dần rồi chuyển sang lãi không. "
           "Ba, doanh thu của chính các cửa hàng cũ có tăng không, chứ không chỉ tăng nhờ mở thêm. "
           "Biên lợi nhuận và chi phí bán hàng của các doanh nghiệp bán lẻ được em cập nhật trên chứng khoán Huy Nguyễn chấm com, anh chị có thể tự theo dõi.")),
 dict(k='end', cap=('MUA KỲ VỌNG', 'HAY MUA SỐ LIỆU?'), cols=CC,
      say=("Thế Giới Di Động và Vinamilk là hai mặt của cùng một bài học: giá cổ phiếu đi theo lợi nhuận và kỳ vọng, chứ không theo độ nổi tiếng của thương hiệu. "
           "Còn anh chị, khi chọn cổ phiếu, anh chị thích mua doanh nghiệp ổn định hay doanh nghiệp đang hồi phục? Anh chị bình luận cho em biết nhé.")),
]
import ql_post; S = ql_post.tach(S)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Thế Giới Di Động Bán 10.000 Đồng Lãi Bao Nhiêu? Từ 60 Đồng Lên 616 Đồng – Cổ Phiếu TĂNG %d%%' % round(doi_gia)
MT = ("Mổ xẻ cỗ máy kiếm tiền của Thế Giới Di Động (MWG) bằng số liệu 3 năm: biên lợi nhuận ròng từ 0,6% lên 6,2%, chi phí bán hàng giảm từ 18,2% xuống 12,5% doanh thu, Bách Hóa Xanh từ lỗ lũy kế thành động cơ tăng trưởng, "
      "kết quả quý 3/2026 và rủi ro mua trả chậm. Đặt cạnh Vinamilk để rút bài học về giá, lợi nhuận và kỳ vọng.\n\n"
      "Biên lợi nhuận, chi phí bán hàng, P/E 400+ mã cập nhật mỗi phiên: https://chungkhoanhuynguyen.com\n📂 Thư viện bài học: https://chungkhoanhuynguyen.com/hoc/\n\n"
      "Nguồn số liệu: BCTC MWG (12 tháng đến quý 3 các năm 2023–2026), kết quả quý 3/2026 (Thời báo Tài chính Việt Nam), VnExpress (Bách Hóa Xanh lần đầu có lãi), giá đóng cửa chưa điều chỉnh 10/11/2023 và giá hiện tại.\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\nChia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Doanh nghiệp kiếm tiền thế nào', ngay='2026-12-03', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['Thế Giới Di Động', 'MWG', 'Bách Hóa Xanh', 'doanh nghiệp kiếm tiền như thế nào', 'biên lợi nhuận', 'P/E là gì', 'cổ phiếu bán lẻ', 'đọc báo cáo tài chính'],
    bia_hook=['60 ĐỒNG', 'THÀNH 616 ĐỒNG'], badge='DOANH NGHIỆP KIẾM TIỀN THẾ NÀO',
    fb_post=("Ba năm trước, cứ 10.000đ bán ra Thế Giới Di Động chỉ giữ lại ~60đ lợi nhuận. Bây giờ: ~616đ, gấp 10 lần 🤯\n\n"
             "👉 Chi phí bán hàng từ 18,2%% xuống 12,5%% doanh thu\n👉 Bách Hóa Xanh từ lỗ lũy kế hơn 8.700 tỷ thành động cơ: 9 tháng 2026 doanh thu 45.900 tỷ (+34%%)\n"
             "👉 Quý 3/2026 lãi 3.521 tỷ (+97%%)\n👉 Cổ phiếu: %s → %s đồng sau 3 năm (+%s%%), trong khi Vinamilk −17%%\n\n"
             "Điểm cần để ý: ~38%% doanh thu Điện Máy Xanh đến từ mua trả chậm.\n\n🎬 Xem đầy đủ: {LINK}\nGửi cho người bạn đang phân vân giữa cổ phiếu 'ổn định' và cổ phiếu 'hồi phục' 😄") % (v(G0), v(gia), v(doi_gia, 1)),
    chuong=[c['ch'] for c in S if c.get('ch')])}
src = open(LO + '/video_dai.py', encoding='utf-8').read() if os.path.exists(LO + '/video_dai.py') else ''
g = {}; exec(src, g) if src else None
SS = g.get('S', {}); MM = g.get('META', {}); SS[KEY] = S; MM[KEY] = META[KEY]
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI – QL1 soạn 10/11/2026 theo chuẩn video_dai_ke_chuyen_1011 + chien_luoc_nut_bac_1011.\n"
    "GOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "".join("S[%r] = %r\n" % (k, x) for k, x in SS.items()) + "META = %r\n" % MM)
json.dump(MM, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
px = json.load(open(LO + '/px_tuan.json')) if os.path.exists(LO + '/px_tuan.json') else {}
px['MWGW'] = wk; json.dump(px, open(LO + '/px_tuan.json', 'w'), ensure_ascii=False)
print('so chu', lib.dem(S), 'eps', round(EPS0), round(EPS1), round(boi, 1), 'gia', gia, round(doi_gia, 1), TIEU, len(TIEU))
