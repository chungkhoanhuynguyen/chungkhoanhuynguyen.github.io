# -*- coding: utf-8 -*-
# QL1 11/11/2026 – THỬ khuôn "Vì Sao Thật Tệ Khi…" trên kênh phụ @chungkhoanhuynguyen6 (Đầu Tư Tích Sản) – anh Huy 11/11 17:10:
# "các kênh phụ khác cũng thử 1 video xem có chuyển biến tốt hơn không". KHUÔN CHUẨN: chi_dao/kenh5_vi_sao_that_te_1011.
# Số thật (WiData, giá vàng miếng SJC bán ra, nghìn đồng/lượng, giá cuối tuần):
#   31/12/2024 84.220 · 31/12/2025 152.820 · 13/3/2026 184.820 (cao nhất các tuần 2026) · 3/4 174.520 · 31/5 159.020 · 29/8 148.720 · 11/11/2026 140.020.
#   Đỉnh 13/3 -> 11/11: −24,2%. 1 tỷ mua ở đỉnh = 5,41 lượng -> nay ~757 triệu (giá bán ra; bán lại theo giá mua vào còn thấp hơn).
#   Người mua cuối 2024 (84,22 tr) nay vẫn +66%.
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
           "Giờ năm lượng rưỡi ấy chỉ còn khoảng bảy trăm năm mươi bảy triệu. Mất gần một phần tư. Và người rủ bạn đi xếp hàng hôm đó, giờ đang nhắn hỏi chính bạn: lỗ bao nhiêu rồi?")),
 dict(k='text', cap=('VÌ SAO THẬT TỆ KHI', 'MUA VÀNG LÚC CẢ XÓM XẾP HÀNG'), cols=CC, anh='ov:gold bars||gold bullion',
      say=("Vàng là tài sản giữ giá, ông bà mình nói vậy và không sai. Nhưng vì sao có người mua vàng mà vẫn mất hai trăm triệu chỉ trong tám tháng? "
           "Câu chuyện hôm nay là giả định, nhưng mọi con số giá vàng đều là số thật năm 2026.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Cơn sốt', cap=('"VÀNG CHỈ CÓ LÊN', 'KHÔNG CÓ XUỐNG"'), cols=CC, moc=True, chat=dict(ten='Hội chị em khu phố', tv='38 thành viên', gio='21:40', mau=V_, msgs=[
        ('Chị Thu', 'Vàng lên 184 triệu rồi, đầu năm mới 158'),
        ('Chị Thu', 'Mai 5h chị đi xếp hàng, ai đi cùng không?'),
        ('Lan', 'Em đi! Gửi tiết kiệm lãi có 5%, vàng 2 tháng lên 17%'),
        ('me', 'Vàng chỉ có lên chứ không có xuống đúng không chị?')]),
      say=("Tháng ba năm 2026. Nhóm Zalo khu phố của bạn sôi lên. Chị Thu nhắn: vàng lên một trăm tám mươi tư triệu rồi, đầu năm mới một trăm năm mươi tám. Mai năm giờ chị đi xếp hàng, ai đi cùng không? "
           "Lan nhảy vào: em đi, gửi tiết kiệm lãi có năm phần trăm một năm, vàng hai tháng lên mười bảy phần trăm. Bạn gõ một câu mà chính bạn cũng muốn tin: vàng chỉ có lên chứ không có xuống đúng không chị?")),
 dict(k='cards', cap=('GIÁ VÀNG MIẾNG BÁN RA', 'TRIỆU ĐỒNG/LƯỢNG'), cols=CC, moc=True,
      cards=[('84,2', 'Cuối năm 2024', ''), ('152,8', 'Cuối năm 2025', ''), ('184,8', 'Tuần 13/3/2026 – cao nhất', '')],
      say=("Nhìn lại, cũng dễ hiểu vì sao cả xóm tin. Cuối năm 2024, một lượng vàng miếng giá khoảng tám mươi tư triệu. Cuối năm 2025, một trăm năm mươi hai triệu. "
           "Đến tuần mười ba tháng ba năm 2026, một trăm tám mươi tư phẩy tám triệu. Hơn một năm, giá gần gấp đôi rưỡi. Ai đứng ngoài cũng thấy mình đang lỡ tàu.")),
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
           "Bạn ra tiệm. Giá mua vào của tiệm còn thấp hơn giá bán ra vài triệu một lượng. Bạn bán đúng một lượng, và lần đầu tiên thấy rõ cái giá của việc mua đúng đỉnh.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='bignum', ch='Chương 3 – Con số thật', cap=('TỪ ĐỈNH 13/3', 'ĐẾN 11/11/2026'), cols=CR, moc=True, value=-24.2, fmt='{:,.1f}', unit='%', top='GIÁ VÀNG MIẾNG BÁN RA', sub='184,82 xuống 140,02 triệu đồng/lượng', col=RED,
      say=("Đây là con số thật. Từ tuần cao nhất ngày mười ba tháng ba, đến ngày mười một tháng mười một năm 2026, giá vàng miếng bán ra giảm từ một trăm tám mươi tư phẩy tám xuống một trăm bốn mươi triệu đồng một lượng, tức giảm hai mươi bốn phẩy hai phần trăm. "
           "Một tỷ mua ở đỉnh, tính theo giá bán ra hôm nay chỉ còn khoảng bảy trăm năm mươi bảy triệu. Nếu bán lại cho tiệm theo giá mua vào, còn thấp hơn nữa.")),
 dict(k='cards', cap=('CÙNG LÀ VÀNG', 'MUA LÚC NÀO MỚI QUAN TRỌNG'), cols=CC, moc=True,
      cards=[('+66%', 'Mua cuối 2024 (84,2 triệu)', 'vẫn lãi lớn'), ('−8%', 'Mua cuối 2025 (152,8 triệu)', 'đang lỗ'), ('−24%', 'Mua đỉnh tháng 3/2026', 'lỗ nặng nhất')],
      say=("Nhưng khoan trách vàng. Người mua cuối năm 2024 với giá tám mươi tư triệu, hôm nay vẫn lãi khoảng sáu mươi sáu phần trăm. Người mua cuối năm 2025, đang lỗ khoảng tám phần trăm. "
           "Còn người mua đúng tuần đỉnh, lỗ hai mươi tư phần trăm. Cùng một tài sản, cùng một năm, kết quả khác nhau hoàn toàn chỉ vì thời điểm mua. Và thời điểm tệ nhất thường là lúc cả xóm cùng xếp hàng.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='checklist', ch='Chương 4 – Vì sao người cẩn thận vẫn mua đỉnh?', cap=('3 CÁI BẪY', 'KHI MUA THEO ĐÁM ĐÔNG'), cols=CC, moc=True,
      items=[('Thấy giá tăng nhanh nên nghĩ còn tăng tiếp – mua vì sợ lỡ', RED),
             ('Rút tiền tiết kiệm, dồn hết một lần, không chia nhỏ', RED),
             ('Không có kế hoạch nếu giá giảm 20%: bán, giữ hay mua thêm?', RED)],
      say=("Vì sao một người vốn cẩn thận, cả đời gửi tiết kiệm, lại mua đúng đỉnh? Có ba cái bẫy. Một: thấy giá tăng nhanh nên tin nó còn tăng tiếp, mua vì sợ lỡ chứ không vì cần. "
           "Hai: rút hết tiết kiệm, dồn một lần, không chia nhỏ theo thời gian. Ba: không có kế hoạch cho tình huống giá giảm hai mươi phần trăm, nên đến lúc cần tiền thì phải bán đúng lúc thấp.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Tích sản đúng cách', cap=('4 NGUYÊN TẮC', 'TRƯỚC KHI MUA VÀNG TÍCH SẢN'), cols=CC, moc=True,
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
      "• 31/5/2026: 159.020 · 29/8/2026: 148.720 · 11/11/2026: 140.020 (−24,2% từ đỉnh)\n\n"
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
