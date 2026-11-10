# -*- coding: utf-8 -*-
# QL1 10/11/2026 – video dài chuẩn mới (kể chuyện, đề tài đại chúng nối về chứng khoán). Số liệu: WiData (TTM Q3/2026), data/fund.bin, data/c/*.bin.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261110_1100'; os.makedirs(LO, exist_ok=True)
KEY = 'CH0112A'
wk = lib.weekly('VCB'); cir = lib.circles(wk); gia = lib.close('VCB')
dinh = cir[0][1]; giam = (gia / dinh - 1) * 100
CC = (WHITE, GOLD)

S = [
 dict(k='hook', ch='Mở đầu', label='Vietcombank', cap=('TRẢ 6,8%', 'VẪN LÃI 41.000 TỶ?'), cols=CC, anh='bank building Hanoi',
      chart=dict(sym='VCBW', tf='W', weeks=52, circles=[cir[0], cir[2]]),
      say=("Anh chị gửi một tỷ đồng vào ngân hàng mười hai tháng. Lãi suất niêm yết gần đây khoảng 6,8%, cuối năm anh chị nhận về sáu mươi tám triệu. "
           "Nghe như ngân hàng đang trả cho mình rất hậu.")),
 dict(k='bignum', cap=('VIETCOMBANK', 'LÃI 12 THÁNG'), cols=CC, value=41, fmt='{:,.0f}', unit=' nghìn tỷ', top='LỢI NHUẬN 4 QUÝ GẦN NHẤT', sub='trả lãi cao mà vẫn lãi lớn?', col=GOLD,
      say=("Nhưng cũng trong mười hai tháng gần nhất, riêng Vietcombank lãi khoảng 41 nghìn tỷ đồng. "
           "Trả lãi cao như vậy mà vẫn lãi lớn như vậy, thì tiền đó đến từ đâu?")),
 dict(k='text', cap=('BÍ MẬT NẰM', 'TRONG ĐIỆN THOẠI'), cols=CC, anh='mobile banking app smartphone',
      say=("Câu trả lời nằm ngay trong cái ứng dụng ngân hàng trên điện thoại của anh chị. "
           "Xem hết video này, anh chị sẽ biết ngân hàng kiếm tiền từ mình bằng cách nào, và con số nào cho thấy ngân hàng nào giỏi hơn. "
           "Cuối video là cách để đứng cùng phía với ngân hàng, thay vì chỉ là người gửi tiền.")),
 dict(k='bignum', ch='Chương 1 – Cỗ máy 430 nghìn tỷ', cap=('7 NGÂN HÀNG LỚN', 'THU LÃI THUẦN'), anh2='banknotes Vietnam', cols=CC, moc=True,
      value=430, fmt='{:,.0f}', unit=' nghìn tỷ', top='12 THÁNG ĐẾN QUÝ 3/2026', sub='≈ 1.178 tỷ mỗi ngày', col=GOLD,
      say=("Bắt đầu bằng một con số cho dễ hình dung. Em cộng bảy ngân hàng lớn là Vietcombank, BIDV, VietinBank, MB, Techcombank, ACB và VPBank. "
           "Tính mười hai tháng đến hết quý 3 năm nay, bảy ngân hàng này thu lãi nhiều hơn trả lãi khoảng 430 nghìn tỷ đồng. Phần chênh lệch đó gọi là thu nhập lãi thuần. "
           "Chia ra mỗi ngày, kể cả thứ Bảy, Chủ nhật, là khoảng 1.178 tỷ đồng. "
           "Và nguyên liệu chính của cỗ máy này là khoảng 9,1 triệu tỷ đồng tiền gửi của khách hàng, tức là tiền của những người như anh chị và em.")),
 dict(k='text', ch='Chương 2 – Tiệm mua tiền rẻ, bán tiền đắt', cap=('MUA TIỀN RẺ', 'BÁN TIỀN ĐẮT'), cols=CC, anh='rice shop Vietnam market',
      say=("Hãy nghĩ ngân hàng giống một tiệm gạo. Tiệm gạo nhập gạo giá thấp, bán ra giá cao hơn, phần chênh là tiền lời. "
           "Ngân hàng cũng vậy, chỉ có điều món hàng là tiền. Ngân hàng mua tiền của người gửi, rồi bán tiền đó cho người vay. "
           "Vậy ngân hàng mua tiền của anh chị với giá bao nhiêu? Nhiều người sẽ trả lời là 6 đến 7% một năm. Đó là con số dán trên bảng lãi suất. "
           "Nhưng đây là chỗ thú vị nhất, và cũng là chỗ phần lớn người gửi tiền không để ý.")),
 dict(k='cards', ch='Chương 3 – Con số ngân hàng không dán lên bảng', cap=('GIÁ VỐN THẬT', 'CỦA VIETCOMBANK'), cols=CC, moc=True, anh='Ho Chi Minh City skyline',
      cards=[('5,48%', 'thu lãi trên tài sản', ''), ('2,84%', 'giá vốn bình quân', ''), ('2,93%', 'biên lãi thuần NIM', '')],
      say=("Theo báo cáo tài chính mười hai tháng gần nhất của Vietcombank, mỗi một trăm đồng tài sản sinh lãi mang về khoảng 5,48 đồng tiền lãi một năm. "
           "Trong khi đó, chi phí vốn bình quân, tức là giá trung bình ngân hàng phải trả cho mỗi một trăm đồng vốn huy động, chỉ khoảng 2,84 đồng. "
           "Nhưng có một điều lạ ở đây. Lãi tiết kiệm mười hai tháng niêm yết gần đây là 6,8%, vậy sao giá vốn bình quân chỉ có 2,84%? "
           "Thậm chí nếu toàn bộ tiền huy động đều phải trả 6,8%, thì với mức thu 5,48%, ngân hàng sẽ lỗ. "
           "Vậy là có một nguồn tiền rất rẻ đang kéo giá vốn xuống. Và nguồn tiền đó, nhiều khả năng đang nằm trong tài khoản của chính anh chị.")),
 dict(k='bignum', ch='Chương 4 – Bí mật trong tài khoản thanh toán', cap=('TIỀN KHÔNG KỲ HẠN', 'CỦA VIETCOMBANK'), anh2='credit card payment', cols=CC, moc=True,
      value=32.2, fmt='{:,.1f}', unit='%', top='TỶ LỆ CASA QUÝ 3/2026', sub='≈ 573 nghìn tỷ lãi gần bằng 0', col=GREEN,
      say=("Bí mật thứ nhất có tên là CASA, tức là tiền gửi không kỳ hạn, chính là số dư trong tài khoản thanh toán mà anh chị dùng để nhận lương, chuyển khoản, quẹt mã QR. "
           "Ở Vietcombank, loại tiền này chiếm khoảng 32,2% tổng tiền gửi, tương đương khoảng 573 nghìn tỷ đồng. "
           "Lãi suất không kỳ hạn thường chỉ khoảng 0,1% một năm. Nghĩa là cứ mười đồng anh chị để trong tài khoản thanh toán, ngân hàng gần như được dùng miễn phí. "
           "Số tiền anh chị để đó chờ tiêu, cộng với hàng triệu người khác, trở thành nguồn vốn rẻ nhất mà ngân hàng có. "
           "Đây là lý do các ngân hàng đua nhau miễn phí chuyển khoản, tặng tài khoản số đẹp: họ không làm từ thiện, họ đang mua tiền rẻ.")),
 dict(k='bars', ch='Chương 4 – Bí mật trong tài khoản thanh toán', cap=('AI GIỮ ĐƯỢC', 'TIỀN RẺ NHẤT?'), anh2='bank teller', cols=CC,
      bars=[('MBB', 34.0, GREEN, '34,0%'), ('TCB', 32.5, GREEN, '32,5%'), ('VCB', 32.2, GREEN, '32,2%'), ('CTG', 23.1, BLUE, '23,1%'),
            ('BID', 20.1, BLUE, '20,1%'), ('ACB', 19.9, BLUE, '19,9%'), ('VPB', 12.9, RED, '12,9%')],
      say=("So bảy ngân hàng, MB dẫn đầu với tỷ lệ tiền không kỳ hạn khoảng 34%, Techcombank khoảng 32,5%, Vietcombank 32,2%. "
           "Nhóm giữa là VietinBank, BIDV và ACB, quanh 20 đến 23%. VPBank thấp nhất, khoảng 12,9%. "
           "Con số này không chỉ là chuyện thống kê. Ngân hàng nào giữ được nhiều tiền rẻ, ngân hàng đó có lợi thế về giá vốn, "
           "giống như tiệm gạo nhập được hàng rẻ hơn đối thủ. Và lợi thế đó thường bền, vì người ta ít khi đổi ngân hàng nhận lương.")),
 dict(k='bars', ch='Chương 5 – Ai bán tiền đắt nhất?', cap=('BIÊN LÃI THUẦN', 'NIM 12 THÁNG'), anh2='shopping mall Vietnam', cols=CC, moc=True,
      bars=[('VPB', 5.15, GOLD, '5,15%'), ('MBB', 4.16, GOLD, '4,16%'), ('TCB', 3.67, BLUE, '3,67%'), ('ACB', 2.99, BLUE, '2,99%'),
            ('VCB', 2.93, BLUE, '2,93%'), ('CTG', 2.84, BLUE, '2,84%'), ('BID', 2.16, BLUE, '2,16%')],
      say=("Vế còn lại là bán tiền. Thước đo quan trọng nhất ở đây là biên lãi thuần, viết tắt là NIM, tức là mỗi một trăm đồng tài sản sinh lãi để lại bao nhiêu đồng chênh lệch. "
           "Và đây là một bất ngờ. VPBank, ngân hàng có tiền rẻ ít nhất, lại có biên lãi cao nhất, khoảng 5,15%. MB khoảng 4,16%. "
           "Còn Vietcombank, ngân hàng có giá vốn rẻ nhất, biên lãi chỉ khoảng 2,93%, và BIDV thấp nhất, khoảng 2,16%. "
           "Vốn đắt mà vẫn lời nhiều hơn, VPBank làm thế nào? Câu trả lời nằm ở việc họ bán tiền cho ai.")),
 dict(k='cards', ch='Chương 6 – Lãi cao luôn có giá của nó', cap=('NỢ XẤU', 'TRÊN DƯ NỢ'), cols=CC, moc=True, anh='Ho Chi Minh City skyline',
      cards=[('3,1%', 'nợ xấu / cho vay VPB', ''), ('0,7%', 'nợ xấu / cho vay VCB', ''), ('10,07%', 'thu lãi trên tài sản VPB', '')],
      say=("VPBank thu lãi trên tài sản khoảng 10,07% một năm, gần gấp đôi Vietcombank, vì họ cho vay nhiều ở mảng tiêu dùng và khách hàng cá nhân, nơi lãi suất cao. "
           "Nhưng lãi cao luôn có giá của nó. Tính theo số dư quý 3 năm 2026, nợ xấu của VPBank khoảng 37,8 nghìn tỷ, bằng khoảng 3,1% dư nợ cho vay. "
           "Vietcombank cho vay nhiều hơn VPBank, nhưng nợ xấu chỉ khoảng 12,8 nghìn tỷ, tương đương khoảng 0,7% dư nợ. "
           "Một bên chọn bán tiền đắt cho khách rủi ro hơn, một bên chọn bán rẻ cho khách an toàn hơn. Không có cách nào đúng tuyệt đối. "
           "Và anh chị để ý: đây cũng chính là bài toán của người đầu tư. Lợi nhuận cao hơn gần như luôn đi kèm rủi ro cao hơn. Ai hứa với anh chị lãi cao mà không có rủi ro, người đó đang không nói hết sự thật.")),
 dict(k='text', ch='Chương 7 – Đổi phía: từ người gửi thành người chủ', cap=('KHÔNG THẮNG ĐƯỢC', 'THÌ LÀM CHỦ?'), cols=CC, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say=("Đến đây, câu hỏi tự nhiên sẽ là: nếu ngân hàng kiếm tiền trên tiền của mình, thì có cách nào để mình hưởng phần chênh lệch đó không? "
           "Có một cách, và nó nằm trên sàn chứng khoán. Khi anh chị gửi tiết kiệm, anh chị là người bán tiền cho ngân hàng. "
           "Khi anh chị mua cổ phiếu ngân hàng, anh chị trở thành một trong những người chủ của tiệm gạo đó, và được chia phần lời theo tỷ lệ cổ phần. "
           "Nghe hấp dẫn, nhưng em sẽ cho anh chị thấy cả hai mặt bằng số, chứ không chỉ mặt đẹp.")),
 dict(k='cards', ch='Chương 7 – Đổi phía: từ người gửi thành người chủ', cap=('100 ĐỒNG GIÁ', 'KIẾM ĐƯỢC BAO NHIÊU?'), cols=CC, moc=True,
      cards=[('9,3 đồng', 'VCB lãi / 100đ giá', ''), ('16,7 đồng', 'MB lãi / 100đ giá', ''), ('6,8 đồng', 'gửi tiết kiệm', '')],
      say=("Lấy hệ số giá trên lợi nhuận, P trên E. Vietcombank có P trên E khoảng 10,75 lần, nghĩa là cứ một trăm đồng anh chị trả cho cổ phiếu, "
           "ngân hàng tạo ra khoảng 9,3 đồng lợi nhuận một năm. Nhưng phần chia bằng tiền mặt chỉ khoảng 1,7 đồng, phần còn lại ngân hàng giữ lại để lớn tiếp. "
           "MB có P trên E khoảng 5,97 lần, tức là khoảng 16,7 đồng lợi nhuận trên một trăm đồng giá, và chia tiền mặt khoảng 4,2 đồng. "
           "Còn gửi tiết kiệm, anh chị nhận khoảng 6,8 đồng, chắc chắn, không mất gốc. "
           "Nhìn bảng này, nhiều người sẽ nghĩ ngay rằng mua cổ phiếu ngân hàng lời hơn. Nhưng em xin anh chị đợi một chút. Còn một con số nữa mà bảng lãi suất không bao giờ có.")),
 dict(k='bignum', ch='Chương 8 – Cái giá của việc làm chủ', cap=('VIETCOMBANK', 'CÁCH ĐỈNH 52 TUẦN'), anh2='File:Sở GDCK TPHCM (HOSE).JPG', cols=CC, moc=True,
      value=round(giam, 1), fmt='{:,.1f}', unit='%', top='ĐỈNH %s – NAY %s' % (lib.vn(dinh, 2), lib.vn(gia, 2)), sub='tiết kiệm: gốc không đổi', col=RED,
      say=("Đó là biến động giá. Trong năm mươi hai tuần qua, cổ phiếu Vietcombank có lúc lên khoảng %s nghìn đồng. Nay giá chỉ khoảng %s nghìn đồng, thấp hơn đỉnh khoảng %s phần trăm. "
           "Một người mua ở đỉnh với một tỷ đồng, nếu bán hôm nay sẽ còn khoảng %s triệu. Trong khi đó, ngân hàng vẫn đang làm ăn có lãi. "
           "Đây là điều quan trọng nhất của cả video. Doanh nghiệp tốt chưa chắc là khoản đầu tư tốt nếu mua sai giá. Giá cổ phiếu còn có thể đi ngược với lợi nhuận trong một thời gian dài. "
           "Làm chủ thì được chia lời, nhưng cũng phải chịu được những năm giá đi xuống.") % (lib.vn(dinh, 2), lib.vn(gia, 2), lib.vn(-giam, 1), lib.vn(1000 * gia / dinh, 0))),
 dict(k='checklist', ch='Chương 9 – Bốn câu hỏi trước khi để tiền', cap=('4 CÂU HỎI', 'TRƯỚC KHI ĐỂ TIỀN'), cols=CC, anh='Ho Chi Minh City skyline',
      items=[('Đã có quỹ dự phòng 6 tháng chưa?', GREEN), ('Tiền này bao lâu nữa mới cần?', GREEN), ('CASA, NIM, nợ xấu ngân hàng ra sao?', GOLD), ('Giá đã cao hơn lợi nhuận bao nhiêu?', GOLD)],
      say=("Vậy anh chị nên để tiền ở đâu? Em không trả lời thay anh chị được, nhưng em gợi ý bốn câu hỏi. "
           "Một, anh chị đã có quỹ dự phòng đủ sáu tháng chi tiêu ở dạng tiết kiệm chưa? Phần tiền này nên an toàn trước tiên. "
           "Hai, số tiền còn lại bao lâu nữa anh chị mới cần dùng? Tiền cần dùng trong một hai năm tới không nên chịu rủi ro giảm ba mươi phần trăm. "
           "Ba, nếu nhìn cổ phiếu ngân hàng, hãy xem ba con số vừa học: tỷ lệ tiền không kỳ hạn, biên lãi thuần và nợ xấu trên dư nợ. "
           "Bốn, giá anh chị đang trả cao gấp bao nhiêu lần giá trị sổ sách và lợi nhuận? Mức đó có hợp lý với khả năng sinh lời của ngân hàng không? "
           "Bảng số của các ngân hàng trong video được em cập nhật mỗi phiên trên chứng khoán Huy Nguyễn chấm com. Anh chị có thể tự đối chiếu.")),
 dict(k='end', cap=('GỬI TIỀN', 'HAY LÀM CHỦ?'), cols=CC,
      say=("Tóm lại, ngân hàng kiếm tiền từ chênh lệch giữa giá mua tiền và giá bán tiền, và tiền rẻ nhất lại đến từ số dư mà chúng ta để quên trong tài khoản. "
           "Người gửi tiền được sự chắc chắn, người làm chủ được phần chênh lệch nhưng phải chịu biến động. "
           "Còn anh chị, đang để phần lớn tiền ở phía người gửi hay phía người làm chủ, và vì sao? Anh chị bình luận cho em biết nhé.")),
]
import ql_post; S = ql_post.tach(S)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Ngân Hàng Trả 6,8% Mà Vẫn LÃI 41.000 TỶ: Bí Mật Nằm Trong Tài Khoản Của Chính Mình'
link = 'https://chungkhoanhuynguyen.com/hoc/'
MT = ("Ngân hàng trả lãi tiết kiệm khoảng 6,8% mà vẫn lãi hàng chục nghìn tỷ mỗi năm. Video giải thích bằng số liệu báo cáo tài chính 12 tháng đến quý 3/2026 của 7 ngân hàng lớn: "
      "thu nhập lãi thuần, chi phí vốn, tỷ lệ tiền không kỳ hạn (CASA), biên lãi thuần (NIM), nợ xấu – và so sánh gửi tiết kiệm với làm chủ ngân hàng qua cổ phiếu.\n\n"
      "Chương:\n00:00 Mở đầu\n{CHUONG}\n\n"
      "Bảng số liệu ngân hàng cập nhật mỗi phiên: https://chungkhoanhuynguyen.com\n📂 Thư viện bài học: https://chungkhoanhuynguyen.com/hoc/\n\n"
      "Nguồn số liệu: báo cáo tài chính các ngân hàng (TTM quý 3/2026), lãi suất niêm yết 12 tháng Vietcombank (30/10/2026).\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\nChia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tiền của mình đi đâu', ngay='2026-12-01', gio_goi_y='19:30', gio='19:30', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['ngân hàng kiếm tiền như thế nào', 'lãi suất tiết kiệm', 'CASA', 'NIM ngân hàng', 'cổ phiếu ngân hàng', 'Vietcombank', 'gửi tiết kiệm hay mua cổ phiếu', 'tài chính cá nhân'],
    bia_hook=['TRẢ 6,8%', 'VẪN LÃI 41.000 TỶ?'], badge='BÍ MẬT NGÂN HÀNG',
    fb_post=("Gửi 1 tỷ, ngân hàng trả mình 68 triệu/năm. Cũng 12 tháng đó, riêng Vietcombank lãi khoảng 41.000 tỷ. Tiền đó từ đâu ra? 🤔\n\n"
             "👉 Lãi thu trên tài sản của VCB chỉ ~5,48%/năm, thấp hơn cả lãi tiết kiệm 6,8%\n"
             "👉 Nhưng giá vốn bình quân chỉ ~2,84% – vì ~32% tiền gửi là tiền không kỳ hạn, lãi gần 0\n"
             "👉 Tức là số dư trong tài khoản thanh toán của chúng ta là nguồn tiền rẻ nhất của ngân hàng\n"
             "👉 Ngân hàng lãi biên cao nhất (VPBank 5,15%) cũng là nơi nợ xấu cao hơn hẳn (~3,1% dư nợ)\n\n"
             "Gửi tiền để được chắc chắn, hay làm chủ ngân hàng để được chia phần chênh lệch? Video đầy đủ có cả hai mặt bằng số.\n\n"
             "🎬 Xem đầy đủ: {LINK}\nGửi cho người bạn đang để cả đống tiền trong tài khoản thanh toán 😄"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
for k in ('hook',): pass
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI – QL1 soạn 10/11/2026 theo chuẩn video_dai_ke_chuyen_1011 + chien_luoc_nut_bac_1011.\n"
    "GOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\nS[%r] = %r\nMETA = %r\n" % (GOLD, RED, GREEN, BLUE, WHITE, KEY, S, META))
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({'VCBW': wk}, open(LO + '/px_tuan.json', 'w'), ensure_ascii=False)
print('so chu', lib.dem(S), 'gia', gia, 'dinh', dinh, 'giam', round(giam, 1))
