# -*- coding: utf-8 -*-
# QL1 10/11/2026 – kênh phụ @chungkhoanhuynguyen5, thử định dạng "Vì Sao Thật Tệ Khi…" (kể chuyện nhân vật hư cấu, số liệu thật).
# Mốc lịch sử: VN-Index đóng cửa đỉnh 1.528,57 (4/1/2022) -> 911,9 (16/11/2022). Còn lại là phép tính minh hoạ.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261110_1800_vt'
KEY = 'VT5MARGIN'; CC = (WHITE, GOLD); CR = (WHITE, RED)
v = lambda x, d=0: lib.vn(x, d)
VON, VAY, LS = 500, 500, 13.0          # triệu đồng, lãi vay %/năm
TONG = VON + VAY
def tk(giam):                          # thị trường giảm giam% -> (tài sản, vốn còn, % vốn mất, tỷ lệ ký quỹ)
    ts = TONG * (1 - giam / 100); con = ts - VAY; return ts, con, (1 - con / VON) * 100, con / ts * 100
LAI_THANG = VAY * LS / 100 / 12
D0, D1 = 1528.57, 911.9; GIAM22 = (1 - D1 / D0) * 100
def can_hoa(m): return (1 / (1 - m / 100) - 1) * 100
S = [
 dict(k='hook', ch='Mở đầu', label='Vì sao thật tệ khi…', cap=('THỊ TRƯỜNG GIẢM 23%', 'TÀI KHOẢN MẤT 46%'), cols=CR, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say="Thị trường giảm 23%. Nhưng tài khoản của bạn mất 46%. Và đó mới chỉ là ngày đầu tiên của cơn ác mộng."),
 dict(k='bignum', cap=('9 GIỜ TỐI', 'MỘT TIN NHẮN'), cols=CR, value=35, fmt='{:,.0f}', unit='%', top='TỶ LỆ KÝ QUỸ CÒN', sub='yêu cầu nộp thêm tiền trước 10 giờ sáng mai', col=RED,
      say=("Chín giờ tối thứ Năm, điện thoại của bạn rung lên. Một tin nhắn từ công ty chứng khoán: tỷ lệ ký quỹ của quý khách đã xuống dưới mức duy trì. "
           "Đề nghị nộp thêm tiền trước mười giờ sáng mai. Nếu không, hệ thống sẽ tự bán.")),
 dict(k='text', cap=('VÌ SAO THẬT TỆ KHI', 'VAY MARGIN ĐU ĐỈNH'), cols=CC, anh='Ho Chi Minh City skyline',
      say=("Khoan đã. Bạn đâu phải người liều. Bạn là nhân viên văn phòng, 29 tuổi, có 500 triệu đồng dành dụm suốt sáu năm để cưới vợ. "
           "Vậy làm sao một người cẩn thận như bạn lại rơi vào đúng tình huống này? Hôm nay mình sẽ cùng bạn sống lại câu chuyện đó: vì sao thật tệ khi vay margin đu đỉnh. "
           "Câu chuyện là giả định, nhưng từng con số đều tính được, và rất nhiều người ngoài đời đã đi đúng con đường này.")),
 dict(k='text', ch='Chương 1 – Bữa tiệc mà ai cũng được mời', cap=('AI CŨNG ĐANG LÃI', 'TRỪ MÌNH'), cols=CC, moc=True, anh='coffee shop Vietnam',
      say=("Mọi chuyện bắt đầu ở quán cà phê. Thằng bạn thân thời đại học khoe vừa lãi 30% trong hai tháng. Chị kế toán trong công ty mua được xe mới. "
           "Nhóm chat chứng khoán mỗi tối đều có người đăng ảnh tài khoản xanh lè. "
           "Còn bạn để 500 triệu trong sổ tiết kiệm, mỗi tháng nhận khoảng ba triệu tiền lãi. Ngồi giữa những câu chuyện đó, bạn bắt đầu thấy mình là đứa chậm chân nhất bàn. "
           "Đây là cảm giác nguy hiểm nhất trong đầu tư. Không phải sợ mất tiền, mà là sợ bị bỏ lại.")),
 dict(k='cards', ch='Chương 2 – Nút bấm "mua tối đa"', cap=('500 TRIỆU', 'THÀNH SỨC MUA 1 TỶ'), cols=CC, moc=True,
      cards=[('%s triệu' % v(VON), 'tiền thật của bạn', ''), ('%s triệu' % v(VAY), 'tiền vay công ty chứng khoán', ''), ('%s triệu' % v(TONG), 'giá trị cổ phiếu đứng tên', '')],
      say=("Bạn mở tài khoản, chuyển 500 triệu vào. Rồi bạn để ý một dòng chữ trên ứng dụng: sức mua 1 tỷ đồng. "
           "Công ty chứng khoán sẵn sàng cho bạn vay thêm đúng bằng số tiền bạn có. Đó chính là margin, hay giao dịch ký quỹ. "
           "Chỉ cần bấm nút mua tối đa, 500 triệu của bạn biến thành một tỷ đồng cổ phiếu. "
           "Nghe thì giống được tặng thêm một đôi chân. Nhưng thật ra, đó là một cái thang mượn. Người ta cho bạn mượn thang để leo cao hơn, chứ không cho bạn mượn dù để nhảy xuống.")),
 dict(k='bignum', ch='Chương 3 – Tuần trăng mật', cap=('THỊ TRƯỜNG +10%', 'VỐN CỦA TUẤN'), cols=CC, moc=True, value=20, fmt='+{:,.0f}', unit='%', top='LÃI 100 TRIỆU', sub='trong vòng một tháng', col=GREEN,
      say=("Tháng đầu tiên, mọi thứ đẹp như mơ. Cổ phiếu tăng 10%. Một tỷ thành một tỷ một trăm triệu. "
           "Nhưng tiền vay vẫn là 500 triệu, nên toàn bộ 100 triệu tiền lãi thuộc về bạn. Vốn của bạn tăng 20%, gấp đôi thị trường. "
           "Bạn bắt đầu nghĩ mình có năng khiếu. Bạn tính nhẩm: cứ đà này, cuối năm có thể mua được nhà. "
           "Đòn bẩy làm lợi nhuận gấp đôi. Và cảm giác tự tin còn tăng nhanh hơn thế.")),
 dict(k='bignum', ch='Chương 4 – Khoản nợ không bao giờ ngủ', cap=('LÃI VAY MARGIN', 'MỖI THÁNG'), cols=CC, moc=True, value=round(LAI_THANG, 1), fmt='{:,.1f}', unit=' triệu', top='VAY 500 TRIỆU · LÃI ~13%/NĂM', sub='chạy cả thứ Bảy, Chủ nhật, ngày lễ', col=GOLD, anh2='Saigon night',
      say=("Có một thứ bạn không để ý. Khoản vay 500 triệu có lãi, khoảng 13%% một năm, tùy công ty và tùy gói vay. "
           "Tính ra khoảng %s triệu đồng mỗi tháng, gần bằng tiền thuê một căn hộ nhỏ ở thành phố. "
           "Và khoản lãi này không nghỉ cuối tuần, không nghỉ Tết. Thị trường đi ngang ba tháng, bạn vẫn mất khoảng %s triệu. "
           "Nghĩa là cổ phiếu không chỉ cần tăng. Nó phải tăng đủ nhanh để thắng cả tiền lãi đang chạy mỗi ngày. "
           "Sổ tiết kiệm trả tiền cho bạn khi bạn ngủ. Còn margin thì lấy tiền của bạn khi bạn ngủ.") % (v(LAI_THANG, 1), v(LAI_THANG * 3, 0))),
 dict(k='text', ch='Chương 5 – Mua thêm ở đỉnh', cap=('CỔ PHIẾU ĐANG LÊN', 'SAO LẠI ĐỨNG NGOÀI?'), cols=CC, moc=True, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say=("Thị trường tiếp tục tăng thêm một chút. Nhóm chat bắt đầu nói về những mức điểm chưa từng có. "
           "Bạn chốt lời một mã, rồi lại dùng toàn bộ sức mua mới để mua mã đang được nhắc nhiều nhất. "
           "Bạn không đọc báo cáo tài chính của nó. Bạn chỉ biết nó vừa tăng ba phiên liền và ai cũng đang nói về nó. "
           "Chính khoảnh khắc này mới là đu đỉnh. Không phải vì giá cao, mà vì lý do mua chỉ còn là: người khác đang mua.")),
 dict(k='bars', ch='Chương 6 – Khi thị trường quay đầu', cap=('THỊ TRƯỜNG GIẢM', 'VỐN CỦA TUẤN MẤT'), cols=CR, moc=True,
      bars=[('Giảm %d%%' % g, round(tk(g)[2]), RED if g >= 20 else GOLD, '−' + v(tk(g)[2]) + '%') for g in (10, 20, 23, 30)],
      say=("Rồi thị trường quay đầu, chậm rãi lúc đầu. Giảm 10%%, tài khoản bạn mất %s%%. Giảm 20%%, bạn mất %s%% số vốn. "
           "Đòn bẩy làm lợi nhuận gấp đôi lúc lên, thì cũng làm thua lỗ gấp đôi lúc xuống. Toán học không có thiên vị. "
           "Bạn tự nhủ, chỉ là điều chỉnh thôi. Bạn không bán, vì bán bây giờ là chốt lỗ, mà chốt lỗ thì đau.") % (v(tk(10)[2]), v(tk(20)[2]))),
 dict(k='cards', ch='Chương 7 – Cuộc gọi lúc 9 giờ tối', cap=('THỊ TRƯỜNG −23%', 'CHẠM VẠCH CALL MARGIN'), cols=CR, moc=True,
      cards=[('%s triệu' % v(tk(23)[0]), 'giá trị cổ phiếu còn lại', ''), ('%s triệu' % v(VAY), 'nợ vẫn y nguyên', ''), ('%s%%' % v(tk(23)[3]), 'tỷ lệ ký quỹ, chạm mức duy trì', '')],
      say=("Đến khi thị trường giảm 23%%, một tỷ đồng cổ phiếu chỉ còn %s triệu. Nhưng khoản nợ thì vẫn y nguyên 500 triệu. "
           "Phần thật sự là của bạn chỉ còn %s triệu, tức khoảng %s%% tổng tài sản. Ở nhiều công ty chứng khoán, đây là quanh mức tỷ lệ duy trì. "
           "Đó là lúc tin nhắn chín giờ tối xuất hiện. Người ta gọi đó là call margin. "
           "Công ty chứng khoán không quan tâm cổ phiếu của bạn tốt hay xấu, sau này có lên lại hay không. Họ chỉ quan tâm một điều: tiền cho vay phải được an toàn.") % (v(tk(23)[0]), v(tk(23)[1]), v(tk(23)[3]))),
 dict(k='checklist', ch='Chương 8 – Ba lựa chọn, không cái nào dễ chịu', cap=('ĐÊM ĐÓ BẠN CÓ', '3 LỰA CHỌN'), cols=CR, moc=True,
      items=[('Nộp thêm tiền: tiền ở đâu ra?', GOLD), ('Tự bán bớt: chốt lỗ ngay', GOLD), ('Không làm gì: bị bán giải chấp', RED)],
      say=("Đêm đó, bạn có ba lựa chọn. Một, nộp thêm tiền. Nhưng toàn bộ tiền tiết kiệm đã nằm trong tài khoản rồi. Muốn nộp thêm, bạn phải vay bố mẹ, vay người quen, hoặc quẹt thẻ tín dụng. "
           "Hai, tự bán bớt cổ phiếu để giảm nợ, tức là biến khoản lỗ trên giấy thành khoản lỗ thật. "
           "Ba, không làm gì cả, và sáng mai hệ thống sẽ tự bán thay bạn, ở bất kỳ mức giá nào khớp được. "
           "Và bạn chọn cách mà rất nhiều người chọn. Bạn gọi về nhà, nói dối là cần tiền đặt cọc thuê nhà, vay thêm 100 triệu.")),
 dict(k='text', ch='Chương 9 – Vòng xoáy giải chấp', cap=('TẤT CẢ CÙNG BỊ CALL', 'TẤT CẢ CÙNG PHẢI BÁN'), cols=CR, moc=True, anh='storm clouds',
      say=("Vấn đề là bạn không đứng một mình. Hàng nghìn tài khoản khác cũng vay margin, cũng nhận tin nhắn đó cùng một đêm. "
           "Sáng hôm sau, ai không nộp được tiền sẽ bị bán. Lệnh bán dồn dập đẩy giá giảm thêm. Giá giảm thêm lại làm thêm nhiều tài khoản chạm vạch. "
           "Giống như một hàng người đứng trên băng mỏng. Người đầu tiên ngã xuống làm cả mảng băng nứt theo. "
           "Đó là lý do những cú giảm có margin thường nhanh và sâu hơn những gì báo cáo tài chính của doanh nghiệp có thể giải thích.")),
 dict(k='bars', ch='Chương 10 – Toán học không thương lượng', cap=('ĐÃ MẤT', 'CẦN TĂNG BAO NHIÊU ĐỂ VỀ BỜ'), cols=CR, moc=True,
      bars=[('Mất %d%%' % m, round(can_hoa(m)), GOLD if m < 50 else RED, '+' + v(can_hoa(m)) + '%') for m in (20, 46, 60, 80)],
      say=("Một tuần sau, thị trường giảm 30%%. Vốn của bạn, tính cả 100 triệu vay của gia đình, đã mất khoảng một nửa. "
           "Đây là phần toán học mà ít ai nói cho bạn biết. Mất 20%%, cần tăng 25%% để về bờ. Mất 46%%, cần tăng %s%%. "
           "Mất 60%%, cần tăng %s%%. Và mất 80%%, cần tăng tới %s%%. "
           "Thua lỗ càng sâu, con đường về càng dài, theo cấp số không công bằng chút nào.") % (v(can_hoa(46)), v(can_hoa(60)), v(can_hoa(80)))),
 dict(k='bignum', ch='Chương 11 – Chuyện này đã xảy ra thật', cap=('VN-INDEX NĂM 2022', 'TỪ ĐỈNH XUỐNG ĐÁY'), cols=CR, moc=True, value=round(-GIAM22, 1), fmt='{:,.1f}', unit='%', top='%s → %s ĐIỂM' % (v(D0, 0), v(D1, 0)), sub='đóng cửa 4/1/2022 → 16/11/2022', col=RED,
      say=("Bạn có thể nghĩ đây chỉ là chuyện tưởng tượng. Nhưng năm 2022, VN-Index đóng cửa ở đỉnh khoảng %s điểm vào ngày 4 tháng 1. "
           "Đến giữa tháng 11, chỉ số đóng cửa quanh %s điểm, giảm khoảng %s%%. Nhiều cổ phiếu đầu cơ còn giảm 70, 80%%. "
           "Với người không vay, đó là một năm buồn. Với người dùng margin tối đa ở vùng đỉnh, đó là năm tài khoản về gần bằng 0.") % (v(D0, 0), v(D1, 0), v(GIAM22, 0))),
 dict(k='text', ch='Chương 12 – Điều thật sự tệ', cap=('MẤT TIỀN CHƯA PHẢI', 'ĐIỀU TỆ NHẤT'), cols=CC, moc=True, anh='Saigon night',
      say=("Nhưng điều thật sự tệ khi vay margin đu đỉnh không chỉ là mất tiền. "
           "Đó là quỹ cưới sáu năm biến mất trong vài tháng. Là khoản nợ với gia đình mà bạn phải nói dối để vay. Là những đêm không ngủ nhìn bảng giá nước ngoài. "
           "Và tệ nhất, là sau cú đó, nhiều người không bao giờ quay lại thị trường nữa. Họ bỏ lỡ luôn những năm thị trường hồi phục, chỉ vì một lần đi quá nhanh.")),
 dict(k='checklist', ch='Chương 13 – Nếu vẫn muốn dùng margin', cap=('4 NGUYÊN TẮC', 'TRƯỚC KHI VAY'), cols=CC, moc=True,
      items=[('Không dùng tiền sắp cần đến', GREEN), ('Vay ít, không bao giờ mua tối đa', GREEN), ('Tự đặt điểm dừng trước vạch call', GREEN), ('Tính lãi vay vào kỳ vọng lợi nhuận', GOLD)],
      say=("Margin không phải ác quỷ. Nó là một công cụ, như con dao trong bếp. Vấn đề là ai cầm và cầm lúc nào. "
           "Nếu bạn vẫn muốn dùng, có bốn nguyên tắc. Một, không bao giờ dùng tiền sắp cần đến, như tiền cưới, tiền nhà, tiền học. "
           "Hai, vay ít, đừng bao giờ bấm mua tối đa. Ba, tự đặt điểm dừng lỗ của mình trước khi công ty chứng khoán đặt hộ. "
           "Bốn, cộng tiền lãi vay vào bài toán. Nếu kỳ vọng lợi nhuận không thắng nổi 13% một năm, khoản vay đó không đáng.")),
 dict(k='text', cap=('BIẾT MÌNH ĐANG MUA GÌ', 'TRƯỚC KHI VAY TIỀN MUA'), cols=CC, anh='File:Sở GDCK TPHCM (HOSE).JPG',
      say=("Và quan trọng hơn hết, đừng vay tiền để mua thứ mình không hiểu. Trong câu chuyện này, bạn chưa từng mở báo cáo tài chính của mã mình mua. "
           "Nếu muốn xem nhanh P/E, biên lợi nhuận và kết quả kinh doanh của hơn 400 mã trước khi xuống tiền, bạn có thể tra miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 dict(k='end', cap=('BẠN ĐÃ TỪNG', 'BỊ CALL MARGIN CHƯA?'), cols=CC,
      say=("Câu chuyện hôm nay là giả định. Nhưng nếu bạn đã từng nhận tin nhắn chín giờ tối đó, bạn sẽ biết nó thật đến mức nào. "
           "Bạn đã từng bị call margin chưa, và bài học lớn nhất của bạn là gì? Bình luận cho mình biết nhé. "
           "Video tiếp theo: vì sao thật tệ khi vào nhóm phím hàng.")),
]
import ql_post; S = ql_post.tach(S)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vì Sao Thật Tệ Khi Vay Margin Đu Đỉnh | Thị Trường Giảm 23%, Tài Khoản Mất 46%'
MT = ("Bạn 29 tuổi, có 500 triệu tiền cưới vợ. Một nút bấm \"mua tối đa\" biến nó thành 1 tỷ đồng cổ phiếu. Thị trường giảm 23%, tài khoản mất 46%, và tin nhắn call margin đến lúc 9 giờ tối. "
      "Câu chuyện giả định, nhưng mọi con số đều tính được: đòn bẩy margin, lãi vay, tỷ lệ ký quỹ, vòng xoáy giải chấp, VN-Index năm 2022.\n\n"
      "P/E, biên lợi nhuận, kết quả kinh doanh 400+ mã cập nhật mỗi phiên: https://chungkhoanhuynguyen.com\n"
      "Kênh chính: https://www.youtube.com/@chungkhoanhuynguyen\n\n"
      "Tình huống là giả định, ví dụ minh hoạ với lãi vay giả định ~13%/năm và tỷ lệ ký quỹ ban đầu 50%. VN-Index: giá đóng cửa 4/1/2022 và 16/11/2022.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen5', seri='Vì sao thật tệ khi…', ngay='2026-11-12', gio_goi_y='20:00', gio='20:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['margin là gì', 'call margin', 'vay margin', 'đu đỉnh', 'giải chấp', 'F0 chứng khoán', 'đòn bẩy tài chính', 'vì sao thật tệ khi'],
    bia_hook=['GIẢM 23%', 'MẤT 46%'], badge='VÌ SAO THẬT TỆ KHI…',
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh phụ @chungkhoanhuynguyen5 – QL1 10/11/2026, định dạng 'Vì sao thật tệ khi…'.\n"
    "XH_BAN = True; NO_CTA = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
print('so chu', lib.dem(S), 'canh', len(S), [round(x) for x in tk(23)], round(LAI_THANG, 2), round(GIAM22, 1), TIEU, len(TIEU))
