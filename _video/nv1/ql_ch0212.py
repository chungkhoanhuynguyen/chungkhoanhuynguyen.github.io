# -*- coding: utf-8 -*-
# QL1 10/11/2026 – video dài chuẩn mới #2: chuỗi "Doanh nghiệp kiếm tiền thế nào" – Vinamilk. Số liệu: WiData (ratio_nonfin_ttm, ratio_daily, eod_root_put, co_events), data/kqkd.bin.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib, hncodec
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261110_1100'; os.makedirs(LO, exist_ok=True)
KEY = 'CH0212A'; CC = (WHITE, GOLD)
wk = lib.weekly('VNM'); cir = lib.circles(wk); gia = lib.close('VNM') * 1000
G0, PE0 = 69090, 16.272          # giá gốc chưa điều chỉnh & P/E ngày 10/11/2023 (WiData)
PE1 = 10.43                      # fund.bin hiện tại
EPS0 = G0 / PE0; EPS1 = gia / PE1; tang_eps = (EPS1 / EPS0 - 1) * 100; doi_gia = (gia / G0 - 1) * 100
CT = 900 + 950 + 1500 + 500 + 2000 + 2500 + 350 + 1850   # cổ tức tiền mặt có GDKHQ 11/2023–10/11/2026
tong = (gia + CT) / G0 * 100 - 100
it = [x for x in hncodec.load('/tmp/cw/data/kqkd.bin')['items'] if x['s'] == 'VNM'][0]['h']
v = lambda x, d=0: lib.vn(x, d)

S = [
 dict(k='hook', ch='Mở đầu', label='Vinamilk', cap=('LÃI TĂNG %d%%' % round(tang_eps), 'GIÁ GIẢM %d%%?' % round(-doi_gia)), cols=CC, anh='milk carton supermarket shelf',
      chart=dict(sym='VNMW', tf='W', weeks=52, circles=[cir[0], cir[2]]),
      say=("Ngày 10 tháng 11 năm 2023, cổ phiếu Vinamilk có giá %s đồng. Ba năm sau, lợi nhuận trên mỗi cổ phiếu tăng khoảng %s%%, công ty vẫn chia cổ tức tiền mặt đều đặn.") % (v(G0), v(tang_eps))),
 dict(k='bignum', cap=('GIÁ VINAMILK', 'SAU 3 NĂM'), cols=CC, value=round(doi_gia, 1), fmt='{:,.1f}', unit='%', top='%s → %s ĐỒNG' % (v(G0), v(gia)), sub='lợi nhuận mỗi cổ phiếu +%s%%' % v(tang_eps), col=RED,
      say=("Vậy mà hôm nay, giá cổ phiếu chỉ khoảng %s đồng, thấp hơn %s%%. Doanh nghiệp làm ăn tốt hơn, cổ phiếu lại rẻ đi.") % (v(gia), v(-doi_gia))),
 dict(k='text', cap=('LÃI HAY LỖ', 'SAU 3 NĂM?'), cols=CC, anh='dairy cows farm',
      say=("Người giữ Vinamilk suốt ba năm qua rốt cuộc lãi hay lỗ? "
           "Trong video này, em sẽ mổ xẻ cỗ máy kiếm tiền của Vinamilk bằng số liệu thật, xem mười nghìn đồng doanh thu đi đâu và còn lại bao nhiêu. "
           "Cuối video là câu trả lời, và một bài học mà nhiều người phải trả giá bằng tiền thật mới hiểu.")),
 dict(k='cards', ch='Chương 1 – Mười nghìn đồng doanh thu đi đâu?', cap=('10.000 ĐỒNG', 'ĐI ĐÂU?'), cols=CC, moc=True, anh='dairy cows farm',
      cards=[('Lãi gộp', '4.200 đ', ''), ('Bán hàng', '2.110 đ', ''), ('Lãi ròng', '1.620 đ', '')],
      say=("Hãy tưởng tượng anh chị mua sữa Vinamilk và trả mười nghìn đồng. Theo báo cáo tài chính mười hai tháng gần nhất, khoảng 5.800 đồng là giá vốn, gồm sữa nguyên liệu, bao bì, nhà máy. "
           "Phần còn lại, khoảng 4.200 đồng, là lãi gộp. "
           "Từ lãi gộp đó, khoảng 2.110 đồng dành cho chi phí bán hàng, khoảng 290 đồng cho chi phí quản lý. "
           "Cuối cùng, sau thuế, Vinamilk giữ lại khoảng 1.620 đồng trên mỗi mười nghìn đồng doanh thu. "
           "Một doanh nghiệp giữ lại được hơn 16% doanh thu thành lợi nhuận ròng là rất hiếm ở Việt Nam. Nhưng con số đáng chú ý nhất lại là con số thứ hai.")),
 dict(k='text', ch='Chương 2 – Cái giá để làm vua sữa', cap=('CHI PHÍ BÁN HÀNG', 'GẤP 7 LẦN QUẢN LÝ'), cols=CC, anh='supermarket aisle',
      say=("Chi phí bán hàng của Vinamilk lớn gấp khoảng bảy lần chi phí quản lý. Đó là tiền quảng cáo, khuyến mãi, chiết khấu cho đại lý và chi phí để hộp sữa có mặt ở hàng trăm nghìn điểm bán. "
           "Mỗi mười nghìn đồng doanh thu, hơn hai nghìn đồng phải chi ra chỉ để giữ chỗ trên kệ và trong đầu người mua. "
           "Đó là cái giá để làm vua sữa. Nó cũng giải thích vì sao doanh nghiệp nhỏ rất khó cạnh tranh: họ không đủ tiền để trả cái giá này. "
           "Câu hỏi tiếp theo là: cỗ máy này mấy năm gần đây chạy nhanh lên hay chậm lại?")),
 dict(k='bars', ch='Chương 3 – Cỗ máy chạy nhanh hơn', cap=('LỢI NHUẬN', '12 QUÝ GẦN NHẤT'), anh2='milk factory', cols=CC, moc=True,
      bars=[(q, p, GREEN if i >= 8 else BLUE, v(p)) for i, (q, p, r) in enumerate(it)],
      say=("Đây là lợi nhuận sau thuế công ty mẹ của Vinamilk trong mười hai quý, từ cuối năm 2023 đến quý 3 năm 2026. "
           "Ba quý gần nhất của năm 2026 đều cao hơn cùng kỳ. Quý 3 năm nay đạt khoảng %s tỷ đồng, tăng khoảng 17,3%%. "
           "Lũy kế chín tháng đạt khoảng 8.560 tỷ, tăng khoảng 30,3%%. Doanh thu thuần quý 3 khoảng 18.465 tỷ, tăng khoảng 8,9%%. "
           "Biên lợi nhuận ròng mười hai tháng cũng nhích từ khoảng 14,1%% năm ngoái lên khoảng 16,2%%. "
           "Nói đơn giản, cỗ máy đang chạy tốt hơn. Vậy thì giá cổ phiếu phải tăng chứ? Đây là chỗ thị trường làm nhiều người bối rối.") % v(it[-1][1])),
 dict(k='cards', ch='Chương 4 – Lãi tăng, giá giảm: chuyện gì đã xảy ra?', cap=('LÃI TĂNG', 'GIÁ VẪN GIẢM'), cols=CC, moc=True, anh='price tag discount',
      cards=[('EPS', '+%s%%' % v(tang_eps), ''), ('Giá', '%s%%' % v(doi_gia), ''), ('P/E', '%s → %s' % (v(PE0, 1), v(PE1, 1)), '')],
      say=("Hãy đặt ba con số cạnh nhau. Lợi nhuận trên mỗi cổ phiếu tăng từ khoảng %s đồng lên khoảng %s đồng, tức là tăng khoảng %s%%. "
           "Nhưng giá cổ phiếu đi từ %s đồng xuống khoảng %s đồng. "
           "Thứ thay đổi chính là hệ số P trên E, tức là thị trường sẵn sàng trả bao nhiêu đồng cho một đồng lợi nhuận. "
           "Ba năm trước là khoảng 16,3 lần, bây giờ chỉ khoảng 10,4 lần. "
           "Nói cách khác, Vinamilk kiếm được nhiều hơn, nhưng người mua chỉ chịu trả ít hơn cho mỗi đồng lợi nhuận đó.") % (v(EPS0), v(EPS1), v(tang_eps), v(G0), v(gia))),
 dict(k='text', ch='Chương 4 – Lãi tăng, giá giảm: chuyện gì đã xảy ra?', cap=('VÌ SAO NGƯỜI MUA', 'TRẢ ÍT HƠN?'), cols=CC, anh='stock market screen',
      say=("Vì sao người mua trả ít hơn? Thị trường thường trả giá cao cho doanh nghiệp tăng trưởng nhanh. "
           "Ba năm trước, nhiều người vẫn kỳ vọng Vinamilk tăng trưởng mạnh trở lại. Thực tế, doanh thu mười hai tháng chỉ tăng khoảng 14% sau hai năm, chậm hơn nhiều doanh nghiệp khác. "
           "Khi kỳ vọng giảm, hệ số P trên E co lại, và phần co lại đó ăn mất toàn bộ phần tăng của lợi nhuận. "
           "Bài học ở đây là: anh chị không chỉ mua một doanh nghiệp, anh chị còn mua cả kỳ vọng của thị trường về doanh nghiệp đó. Mua lúc kỳ vọng quá cao, doanh nghiệp tốt mấy cũng khó cứu.")),
 dict(k='bignum', ch='Chương 5 – Người giữ ba năm lãi hay lỗ?', cap=('GIỮ 3 NĂM', 'TÍNH CẢ CỔ TỨC'), anh2='piggy bank coins', cols=CC, moc=True,
      value=round(tong, 1), fmt='{:,.1f}', unit='%', top='GIÁ %s%% + CỔ TỨC %s Đ' % (v(doi_gia, 1), v(CT)), sub='trước thuế và phí, chưa tái đầu tư', col=RED if tong < 0 else GREEN,
      say=("Giờ trả lời câu hỏi mở đầu. Giả sử một người mua Vinamilk ngày 10 tháng 11 năm 2023 với giá %s đồng. Giữ đến hôm nay, người đó mất khoảng %s%% vì giá giảm. "
           "Nhưng trong ba năm đó, họ nhận được tổng cộng khoảng %s đồng cổ tức tiền mặt trên mỗi cổ phiếu. "
           "Cộng lại, kết quả là khoảng %s%%, gần như hòa vốn sau ba năm, chưa tính thuế và phí. "
           "Cổ tức đã cứu khoản đầu tư khỏi lỗ, nhưng không biến nó thành khoản lãi. "
           "Trong cùng ba năm, nếu để tiền gửi tiết kiệm, anh chị đã có lãi chắc chắn. Đó là cái giá của việc mua đúng doanh nghiệp nhưng ở mức giá kỳ vọng quá cao.") % (v(G0), v(-doi_gia, 1), v(CT), v(tong, 1))),
 dict(k='text', ch='Chương 6 – Bức tranh bây giờ khác gì?', cap=('BÂY GIỜ', 'KHÁC 3 NĂM TRƯỚC?'), cols=CC, anh='calendar planning',
      say=("Vậy bây giờ thì sao? Em không đưa ra khuyến nghị mua bán, nhưng em có thể đặt hai bức tranh cạnh nhau để anh chị tự đánh giá. "
           "Ba năm trước, P trên E khoảng 16,3 lần và lợi nhuận đi ngang. Bây giờ, P trên E khoảng 10,4 lần và lợi nhuận chín tháng tăng khoảng 30%%. "
           "Vinamilk đã trả 1.850 đồng cổ tức vào tháng 6. Công ty sắp trả thêm 2.500 đồng đợt 1 năm 2026, ngày giao dịch không hưởng quyền là 11 tháng 11. "
           "Cộng lại khoảng 4.350 đồng, tương đương khoảng %s%% so với giá hiện tại. "
           "Nhưng anh chị nhớ: cổ tức cao một phần là do giá thấp, và câu hỏi thật sự vẫn là tăng trưởng của năm 2027 có giữ được không.") % v(4350 / gia * 100, 1)),
 dict(k='checklist', ch='Chương 7 – Ba câu hỏi trước khi mua cổ phiếu tốt', cap=('3 CÂU HỎI', 'TRƯỚC KHI MUA'), cols=CC, anh='checklist notebook',
      items=[('Lợi nhuận có tăng thật không?', GREEN), ('Đang trả bao nhiêu lần lợi nhuận?', GOLD), ('Tính cả cổ tức thì lãi bao nhiêu?', GOLD)],
      say=("Rút gọn lại, trước khi mua một cổ phiếu tốt, anh chị hãy hỏi ba câu. "
           "Một, lợi nhuận có thật sự tăng không, nhìn ít nhất tám đến mười hai quý chứ không phải một quý. "
           "Hai, mình đang trả bao nhiêu lần lợi nhuận, và mức đó cao hay thấp so với chính quá khứ của doanh nghiệp. "
           "Ba, khi tính hiệu quả, hãy cộng cả cổ tức, rồi so với lãi tiết kiệm trong cùng thời gian. "
           "Lịch sử P trên E và cổ tức của Vinamilk cùng hơn bốn trăm mã khác được em cập nhật mỗi phiên trên chứng khoán Huy Nguyễn chấm com, anh chị có thể tự kiểm tra.")),
 dict(k='end', cap=('DOANH NGHIỆP TỐT', 'CHƯA CHẮC LÃI'), cols=CC,
      say=("Vinamilk là một ví dụ rõ ràng: doanh nghiệp tốt, lợi nhuận tăng, cổ tức đều, nhưng người mua ở giá kỳ vọng cao vẫn gần như đứng yên ba năm. "
           "Còn anh chị, khi chọn cổ phiếu, anh chị nhìn lợi nhuận trước hay nhìn giá trước? Anh chị bình luận cho em biết nhé.")),
]
import ql_post; S = ql_post.tach(S)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vinamilk Bán 10.000 Đồng Sữa Lãi Bao Nhiêu? Lãi Tăng %d%% Mà Cổ Phiếu GIẢM %d%% – Vì Sao?' % (round(tang_eps), round(-doi_gia))
MT = ("Mổ xẻ cỗ máy kiếm tiền của Vinamilk bằng báo cáo tài chính 12 tháng đến quý 3/2026: 10.000 đồng doanh thu đi đâu, vì sao chi phí bán hàng lớn gấp 7 lần chi phí quản lý, "
      "và vì sao lợi nhuận mỗi cổ phiếu tăng mà giá cổ phiếu giảm sau 3 năm. Tính cả cổ tức tiền mặt, người giữ 3 năm lãi hay lỗ?\n\n"
      "Bảng P/E, cổ tức, lợi nhuận 400+ mã cập nhật mỗi phiên: https://chungkhoanhuynguyen.com\n📂 Thư viện bài học: https://chungkhoanhuynguyen.com/hoc/\n\n"
      "Nguồn số liệu: BCTC Vinamilk, giá đóng cửa chưa điều chỉnh 10/11/2023 và giá hiện tại, lịch sử cổ tức tiền mặt (GDKHQ 11/2023–10/11/2026).\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\nChia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Doanh nghiệp kiếm tiền thế nào', ngay='2026-12-02', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['Vinamilk', 'VNM', 'doanh nghiệp kiếm tiền như thế nào', 'P/E là gì', 'cổ tức Vinamilk', 'đầu tư giá trị', 'đọc báo cáo tài chính', 'cổ phiếu tốt'],
    bia_hook=['LÃI TĂNG %d%%' % round(tang_eps), 'GIÁ GIẢM %d%%?' % round(-doi_gia)], badge='DOANH NGHIỆP KIẾM TIỀN THẾ NÀO',
    fb_post=("Ba năm trước mua Vinamilk giá %s đồng. Ba năm sau, lợi nhuận mỗi cổ phiếu tăng ~%s%%… mà giá còn ~%s đồng 🤯\n\n"
             "👉 Mỗi 10.000đ doanh thu: ~4.200đ lãi gộp, ~2.110đ chi cho bán hàng, còn ~1.620đ lợi nhuận ròng\n"
             "👉 Lợi nhuận 9 tháng 2026 +30,3%%, nhưng P/E co từ ~16,3 lần xuống ~10,4 lần\n"
             "👉 Tính cả %sđ cổ tức tiền mặt, người giữ 3 năm vẫn chỉ quanh hòa vốn (~%s%%)\n\n"
             "Doanh nghiệp tốt chưa chắc là khoản đầu tư tốt, nếu mua ở giá kỳ vọng quá cao.\n\n"
             "🎬 Xem đầy đủ: {LINK}\nGửi cho người bạn đang ôm cổ phiếu \"tốt\" mà mãi không lên 😅") % (v(G0), v(tang_eps), v(gia), v(CT), v(tong, 1)),
    chuong=[c['ch'] for c in S if c.get('ch')])}
src = open(LO + '/video_dai.py', encoding='utf-8').read() if os.path.exists(LO + '/video_dai.py') else ''
g = {}; exec(src, g) if src else None
SS = g.get('S', {}); MM = g.get('META', {}); SS[KEY] = S; MM[KEY] = META[KEY]
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI – QL1 soạn 10/11/2026 theo chuẩn video_dai_ke_chuyen_1011 + chien_luoc_nut_bac_1011.\n"
    "GOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "".join("S[%r] = %r\n" % (k, x) for k, x in SS.items()) + "META = %r\n" % MM)
json.dump(MM, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
px = json.load(open(LO + '/px_tuan.json')) if os.path.exists(LO + '/px_tuan.json') else {}
px['VNMW'] = wk; json.dump(px, open(LO + '/px_tuan.json', 'w'), ensure_ascii=False)
print('so chu', lib.dem(S), 'eps', round(EPS0), round(EPS1), round(tang_eps, 1), 'gia', gia, round(doi_gia, 1), 'tong', round(tong, 1), TIEU, len(TIEU))
