# -*- coding: utf-8 -*-
# QL1 (Fable 5.2) 25/11/2026 23:30 – VIDEO DÀI kênh chính, anh Huy giao 22:46 "tin mới, làm nhanh tay; 2025 cũng bị áp thuế kiểu này 1 lần rồi".
# Công thức: tin nóng (Mỹ đề xuất thuế tới 35% với hàng Việt Nam) → kể chuyện tháng 4/2025 → nghĩa là gì với danh mục → 3 câu tự soi → dẫn về tư vấn.
# Nguồn (đã mở 25/11/2026):
#  - USTR, thông cáo 25/11/2026 "USTR Makes Determinations and Proposes Actions in 14 Section 301 Investigations": 14 nền kinh tế; Việt Nam: xem xét thuế tới 35% trên hàng hoá Việt Nam,
#    20% nếu đạt Thoả thuận Thương mại Đối ứng; nêu dệt may, da giày, đóng tàu, xi măng, ICT; góp ý đến 5/1/2027; điều trần từ 25/1/2027; không nêu ngày hiệu lực.
#  - Dân trí 25/11/2026 (2 bài): điều tra 8 tháng theo Điều 301 về dư thừa năng lực sản xuất; thuế mới một phần thay các khoản thuế toàn cầu bị Toà án Tối cao Mỹ bác hồi tháng 2; MSCI thế giới giảm 0,5% sau tin.
#  - Báo Đầu tư qua VCCI 4/11/2026: 10 tháng 2026 xuất khẩu sang Mỹ 159,40 tỷ USD, +26,2%. Tạp chí Kinh tế Tài chính 14/11/2026: Mỹ chiếm gần 32% xuất khẩu cả nước.
#  - 2025: Nhà Đầu tư 3/4/2025, Báo Văn hoá 3/4/2025 (thuế 46%; VN-Index −87,99 điểm, −6,68%, còn 1.229,84; vốn hoá mất 370.000 tỷ); Thị trường Tài chính Tiền tệ 3/4/2025 (517 mã giảm, 280 mã sàn);
#    VnExpress 9/4/2025 (VN-Index 1.094 điểm, 4 phiên mất 223 điểm, vốn hoá mất hơn 933.000 tỷ ≈ 36 tỷ USD); mức 20% công bố sau đàm phán 2/7/2025.
#  - Nhân Dân, Tin nhanh Chứng khoán 25/11/2026: VN-Index đóng cửa 1.687,45 (−9,69 điểm) – TRƯỚC khi có tin (tin ra tối 25/11 giờ Việt Nam).
#  - BEA qua Kalkine, Zerohedge 25/11/2026: GDP Mỹ quý 3 ước tính lần hai 4,3% (lần đầu 3,4%, dự báo 3,5%); PCE lõi tháng 10 +3,3% so cùng kỳ (dự báo 3,2%). Fed họp 8–9/12 (CafeF 17/11/2026).
# Số tự tính: 1.317,83 → 1.094,30 = −223,5 điểm (−17%); 1.094,30 → 1.687,45 = +54,2%.
# Mức của các nước khác KHÔNG nêu chi tiết: nguồn vênh nhau (FXStreet: Trung Quốc tới 40%, nhóm ASEAN tới 25%; thông cáo USTR: Trung Quốc tới 20%, nhóm ASEAN tới 18%).
# Nhân vật Cường, Hùng hư cấu (dàn cố định). Không dự đoán thị trường.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw')
sys.path.insert(0, CW + '/_video'); from phat_am import doc as phat_am_doc
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = CW + '/_video/queue/20261125_2330'
KEY = 'CH2711TQ'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
HCM = 'ov:Ho Chi Minh City skyline night||Ho Chi Minh City skyline'
HN = 'ov:Hanoi skyline night||Hanoi skyline'
CF_L = ([-28.25, 0.15, 5.2], [-27.15, 0.15, 5.2])
CAM_CF = {'from': [[-27.4, 1.5, 2.3], [-27.7, 0.8, 5.2], 42], 'to': [[-27.6, 1.42, 3.0], [-27.7, 0.8, 5.2], 38]}
CAM_VP = {'from': [[0.9, 1.5, 4.4], [0.3, 1.3, -1.0], 44], 'to': [[0.6, 1.45, 3.4], [0.2, 1.35, -1.2], 39]}

S = [
 dict(k='noti', ch='Mở đầu', cap=('MỸ ĐỀ XUẤT THUẾ TỚI 35%', 'VỚI HÀNG VIỆT NAM'), cols=CR, noti=dict(gio='21:40', ngay='Thứ Tư 25/11', items=[
        ('Tin tức', 'Dân trí · 25/11/2026', 'Tổng thống Mỹ đề xuất áp thuế mới, chứng khoán bị bán tháo', R_),
        ('Tin tức', 'Thông cáo của Mỹ · 25/11/2026', 'Việt Nam: xem xét mức thuế tới 35%', R_),
        ('Zalo', 'Cường', 'Lại thuế! Mai tôi bán hết được không ông?', V_)]),
      say=("Ba mươi lăm phần trăm. Đó là mức thuế mà Mỹ vừa đề xuất xem xét với hàng Việt Nam, công bố đêm hai mươi lăm tháng mười một. "
           "Nếu anh chị đang cầm cổ phiếu, chắc tối nay anh chị cũng thấy nóng ruột. Nhưng khoan đã. Chuyện này, thị trường Việt Nam đã gặp một lần rồi, tháng tư năm hai nghìn không trăm hai mươi lăm. "
           "Hôm nay em kể lại lần đó: ai bán, bán ở đâu, và sau đó chuyện gì xảy ra. Rồi em cùng anh chị soi danh mục bằng ba câu hỏi.")),
 dict(k='bignum', short=True, anh=HCM, cap=('MỨC TRẦN ĐỀ XUẤT', 'TỚI 35%'), cols=CR,
      value=35, fmt='{:,.0f}', unit='%', top='MỸ ĐỀ XUẤT XEM XÉT THUẾ VỚI HÀNG VIỆT NAM', sub='Thông cáo Văn phòng Đại diện Thương mại Mỹ · 25/11/2026', col=R_,
      say=("Trước hết, tin chính xác là gì. Văn phòng Đại diện Thương mại Mỹ kết luận cuộc điều tra kéo dài tám tháng với mười bốn nền kinh tế. "
           "Với Việt Nam, họ đề xuất xem xét mức thuế tới ba mươi lăm phần trăm. Chữ quan trọng là: đề xuất, và tới.")),
 dict(k='3d', set='cafevh', light='day', cam=CAM_CF, label='10 GIỜ ĐÊM · QUÁN NƯỚC',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'dienthoai', 'ngoi': True, 'expr': 'worried'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'}],
      cap=('"MAI BÁN HẾT', 'ĐƯỢC KHÔNG ÔNG?"'), cols=CC,
      say=("Mười giờ đêm, Cường gọi Hùng ra quán nước. Anh giơ điện thoại: mai bán hết được không ông? "
           "Hùng lái xe container chở hàng xuất khẩu ra cảng hơn mười năm. Anh chỉ hỏi lại: ông còn nhớ tháng tư năm ngoái không? Hôm đó ông cũng hỏi đúng câu này.")),
 # ---- Chương 1
 dict(k='giay', ch='Chương 1 – Tin chính xác là gì', cap=('CÓ THỎA THUẬN: 20%', 'KHÔNG CÓ: TỚI 35%'), cols=CR, moc=True, giay=dict(
        tieu_de='ĐỀ XUẤT VỚI HÀNG VIỆT NAM', so='Văn phòng Đại diện Thương mại Mỹ · 25/11/2026', dau='MỚI LÀ ĐỀ XUẤT', dieu=[
        ('Mức trần xem xét', 'TỚI 35%'),
        ('Nếu đạt thỏa thuận thương mại', '20%'),
        ('Hạn gửi góp ý', '5/1/2027'),
        ('Bắt đầu điều trần', '25/1/2027')]),
      say=("Đọc kỹ thông cáo thì có bốn dòng cần nhớ. Một, mức trần xem xét là tới ba mươi lăm phần trăm. "
           "Hai, nếu hai nước đạt được thỏa thuận thương mại, mức được nêu là hai mươi phần trăm. "
           "Ba, Mỹ nhận góp ý đến ngày năm tháng một. Bốn, phiên điều trần bắt đầu từ ngày hai mươi lăm tháng một năm sau. Thông cáo không nêu ngày thuế có hiệu lực.")),
 dict(k='checklist', cap=('5 NHÓM NGÀNH', 'BỊ NÊU TÊN'), cols=CC, moc=True,
      items=[('Dệt may và da giày', V_), ('Đóng tàu và xi măng', V_), ('Điện tử, công nghệ thông tin', R_)],
      say=("Thông cáo cũng nêu tên năm nhóm ngành của Việt Nam: dệt may, da giày, đóng tàu, xi măng, và điện tử công nghệ thông tin. "
           "Theo báo Dân trí, đợt thuế này phần nào dùng để thay cho các khoản thuế toàn cầu đã bị Tòa án Tối cao Mỹ bác hồi tháng hai.")),
 dict(k='bignum', anh=HN, cap=('MỸ MUA GẦN 32%', 'HÀNG XUẤT KHẨU CỦA VIỆT NAM'), cols=CC,
      value=159.4, fmt='{:,.1f}', unit=' TỶ USD', top='XUẤT KHẨU SANG MỸ, 10 THÁNG NĂM 2026', sub='Báo Đầu tư 4/11/2026 · Cục Hải quan', col=V_,
      say=("Vì sao con số này làm cả thị trường giật mình? Mười tháng đầu năm nay, Việt Nam bán sang Mỹ hơn một trăm năm mươi chín tỷ đô la. Gần ba mươi hai phần trăm tổng xuất khẩu. "
           "Nghĩa là cứ ba đồng hàng mình bán ra nước ngoài, thì gần một đồng là bán cho Mỹ.")),
 # ---- Chương 2
 dict(k='call', ch='Chương 2 – Tháng 4 năm 2025', cap=('"HÔM ĐÓ CẢNG', 'ĐÔNG NHƯ TẾT"'), cols=CR, moc=True, call=dict(ten='Hùng', phu='Đang kể', mau=V_, loi=[
        'Sáng 3/4/2025: Mỹ công bố thuế 46%', 'Bảng điện đỏ từ lúc mở cửa']),
      say=("Hùng kể lại. Sáng mùng ba tháng tư năm hai nghìn không trăm hai mươi lăm, Mỹ công bố thuế bốn mươi sáu phần trăm với hàng Việt Nam. "
           "Hùng nhớ hôm đó chủ hàng gọi dồn dập, ai cũng muốn đẩy hàng ra cảng thật nhanh. Còn Cường thì ngồi nhìn bảng điện đỏ rực từ lúc mở cửa.")),
 dict(k='giay', cap=('PHIÊN 3/4/2025', 'VN-INDEX MẤT GẦN 88 ĐIỂM'), cols=CR, moc=True, giay=dict(
        tieu_de='PHIÊN 3/4/2025', so='Nhà Đầu tư, Báo Văn hóa, Thị trường Tài chính Tiền tệ · 3/4/2025', dau='KỶ LỤC GIẢM ĐIỂM', dieu=[
        ('VN-Index giảm', '87,99 ĐIỂM'),
        ('Tương đương', '6,68%'),
        ('Số mã giảm kịch sàn', '280 MÃ'),
        ('Vốn hóa mất trong một phiên', '370.000 TỶ')]),
      say=("Những con số của phiên hôm đó. Chỉ số VN-Index mất gần tám mươi tám điểm, tương đương sáu phẩy sáu tám phần trăm. Đó là phiên giảm nhiều điểm nhất trong lịch sử tính đến lúc ấy. "
           "Hai trăm tám mươi mã giảm kịch sàn. Giá trị cả sàn bốc hơi khoảng ba trăm bảy mươi nghìn tỷ đồng chỉ trong một ngày.")),
 dict(k='bars', short=True, anh=HCM, cap=('4 PHIÊN', 'MẤT 223 ĐIỂM'), cols=CR, top='VN-INDEX (ĐIỂM)',
      bars=[('2/4/2025', 1317.83, V_, '1.317,83'), ('3/4/2025', 1229.84, R_, '1.229,84'), ('9/4/2025', 1094.3, R_, '1.094,30')],
      say=("Và chưa dừng ở đó. Đến ngày mùng chín tháng tư, sau bốn phiên, VN-Index còn một nghìn không trăm chín mươi tư điểm, mất tổng cộng hai trăm hai mươi ba điểm. "
           "Theo VnExpress, giá trị cả sàn mất hơn chín trăm ba mươi ba nghìn tỷ đồng. Cường bán gần hết đúng trong mấy phiên đó.")),
 dict(k='chat', cap=('"TÔI BÁN ĐÚNG', 'NGÀY MÙNG 9"'), cols=CR, moc=True, chat=dict(ten='Cường', tv='Đang hoạt động', gio='22:25', mau=V_, msgs=[
        ('Cường', 'Tôi bán đúng ngày mùng 9 ông ạ'),
        ('Cường', 'Sợ quá, nghĩ còn rơi nữa'),
        ('me', 'Rồi sau đó thuế có là 46% không?'),
        ('Cường', 'Không. Tháng 7 công bố còn 20%')]),
      say=("Cường thú thật: anh bán đúng ngày mùng chín, vì sợ còn rơi nữa. Hùng hỏi: rồi sau đó thuế có là bốn mươi sáu phần trăm không? "
           "Không. Sau ba tháng đàm phán, mức công bố tháng bảy năm đó là hai mươi phần trăm.")),
 dict(k='bars', anh=HN, cap=('TỪ ĐÁY 9/4/2025', 'ĐẾN 25/11/2026'), cols=CC, top='VN-INDEX (ĐIỂM)',
      bars=[('9/4/2025', 1094.3, R_, '1.094,30'), ('25/11/2026', 1687.45, G_, '1.687,45')],
      say=("Còn đây là hai con số em muốn anh chị nhìn. Ngày mùng chín tháng tư năm ngoái: một nghìn không trăm chín mươi tư điểm. Đóng cửa ngày hai mươi lăm tháng mười một năm nay: một nghìn sáu trăm tám mươi bảy điểm. "
           "Em nói rõ: lần trước như thế không có nghĩa lần này cũng thế. Em không đoán thị trường. Nhưng nó cho thấy một điều: con số thuế đầu tiên chưa chắc là con số cuối cùng.")),
 # ---- Chương 3
 dict(k='checklist', ch='Chương 3 – Lần này giống và khác', cap=('GIỐNG VÀ KHÁC', 'LẦN TRƯỚC'), cols=CC, moc=True,
      items=[('Giống: mới là đề xuất, còn đàm phán', V_), ('Khác: lần này có lịch góp ý, điều trần', V_), ('Khác: đô la mạnh, lãi suất Mỹ còn cao', R_)],
      say=("Lần này giống ở chỗ: đây vẫn là con số đề xuất, và cửa đàm phán còn mở, với mức hai mươi phần trăm được nêu sẵn nếu có thỏa thuận. "
           "Khác thứ nhất: năm ngoái thuế định áp chỉ sau một tuần. Lần này có lịch góp ý và điều trần kéo sang cuối tháng một. "
           "Khác thứ hai, và cái này bất lợi hơn: bối cảnh tiền tệ.")),
 dict(k='cards', anh=HCM, cap=('KINH TẾ MỸ NÓNG HƠN DỰ BÁO', 'LÃI SUẤT KHÓ GIẢM'), cols=CR, moc=True,
      cards=[('Tăng trưởng Mỹ quý 3', '4,3%', 'Dự báo chỉ 3,5%'), ('Lạm phát lõi tháng 10', '3,3%', 'Dự báo 3,2%'), ('Fed họp', 'Ngày 8 và 9/12', 'Quyết định lãi suất')],
      say=("Cùng ngày, Mỹ công bố kinh tế quý ba tăng bốn phẩy ba phần trăm, cao hơn hẳn mức dự báo ba phẩy năm. Lạm phát lõi, tức giá cả không tính thực phẩm và năng lượng, tăng ba phẩy ba phần trăm, cũng cao hơn dự báo. "
           "Kinh tế nóng, giá còn cao, thì ngân hàng trung ương Mỹ khó hạ lãi suất. Đô la mạnh thì tỷ giá trong nước chịu sức ép, và khối ngoại dễ rút tiền. Fed họp ngày tám và chín tháng mười hai.")),
 dict(k='3d', set='vanphong', light='day', cam=CAM_VP, label='SÁNG HÔM SAU · VĂN PHÒNG',
      cast=[{'a': 'huy', 'p': [-0.7, 0, 0.5], 'act': 'chitay', 'side': -1, 'expr': 'smile'},
            {'a': 'cuong', 'p': [0.9, 0, 0.7], 'act': 'dienthoai', 'side': -1, 'expr': 'worried'}],
      cap=('"ĐỪNG HỎI THỊ TRƯỜNG', 'HÃY HỎI DANH MỤC"'), cols=CC,
      say=("Sáng hôm sau Cường ghé văn phòng em, Huy Nguyễn. Anh hỏi: thế bán hay giữ? "
           "Em bảo em không trả lời thay anh được, và cũng không ai biết thị trường mai thế nào. Nhưng có ba câu anh tự trả lời được ngay, và nó quan trọng hơn chuyện đoán chỉ số.")),
 # ---- Chương 4
 dict(k='checklist', ch='Chương 4 – Ba câu soi danh mục', cap=('3 CÂU SOI DANH MỤC', 'KHI CÓ TIN THUẾ'), cols=CC, moc=True,
      items=[('Công ty bán bao nhiêu phần sang Mỹ?', R_), ('Công ty vay nhiều hay ít?', V_), ('Anh chị có đang vay tiền để mua không?', R_)],
      say=("Câu một: công ty mình cầm bán bao nhiêu phần hàng sang Mỹ? Bán chủ yếu trong nước thì chịu ảnh hưởng trực tiếp ít hơn nhiều so với doanh nghiệp sống nhờ đơn hàng Mỹ. "
           "Câu hai: công ty vay nhiều hay ít? Khi đơn hàng chậm lại, doanh nghiệp nợ nhiều là doanh nghiệp hụt hơi trước. "
           "Câu ba, anh chị có đang vay tiền để mua cổ phiếu không? Tháng tư năm ngoái, nhiều người mất nặng không phải vì chọn sai cổ phiếu, mà vì dùng tiền vay nên bị buộc bán đúng lúc giá thấp nhất.")),
 dict(k='chat', cap=('"LẦN NÀY TÔI', 'SOI TRƯỚC ĐÃ"'), cols=CC, moc=True, chat=dict(ten='Cường', tv='Đang hoạt động', gio='20:10', mau=V_, msgs=[
        ('Cường', 'Tôi soi xong 3 câu rồi'),
        ('Cường', '2 mã bán trong nước là chính, không vay'),
        ('Cường', '1 mã dệt may, bán sang Mỹ nhiều'),
        ('me', 'Thế là ông biết phải nghĩ về mã nào rồi')]),
      say=("Tối hôm đó Cường nhắn cho Hùng. Anh soi xong rồi. Hai mã bán trong nước là chính, không vay nợ nhiều. Một mã dệt may bán sang Mỹ nhiều. "
           "Hùng trả lời: thế là ông biết phải nghĩ kỹ về mã nào rồi. Năm ngoái Cường bán tất cả trong một buổi sáng. Năm nay anh biết mình đang lo vì cái gì.")),
 # ---- Kết
 dict(k='3d', ch='Kết', set='cafevh', light='day', cam=CAM_CF, label='CUỐI TUẦN · QUÁN NƯỚC',
      cast=[{'a': 'cuong', 'p': CF_L[0], 'act': 'noi', 'ngoi': True, 'expr': 'relief'},
            {'a': 'hung', 'p': CF_L[1], 'act': 'noi', 'ngoi': True, 'expr': 'smile'}],
      cap=('"TIN XẤU KHÔNG LÀM MÌNH LỖ', 'HOẢNG MỚI LÀM MÌNH LỖ"'), cols=CC,
      say=("Cuối tuần, hai người lại ngồi quán nước. Hùng nói một câu em muốn anh chị mang theo: "
           "tin xấu chưa chắc làm mình lỗ, quyết định lúc hoảng mới dễ làm mình lỗ.")),
 dict(k='cards', anh=HCM, cap=('BA CÂU ĐÓ', 'EM SOI CÙNG ANH CHỊ'), cols=CC, moc=True,
      cards=[('Trên web', 'Đánh giá báo cáo tài chính', 'Xem miễn phí'), ('Mỗi ngày', 'Tin thuế, lãi suất Fed', 'Em cập nhật'), ('Đang rối?', 'Nhắn em tên mã', 'Em xem cùng anh chị')],
      say=("Câu một và câu hai, nợ vay và sức khỏe từng doanh nghiệp, em đã chấm sẵn ở mục đánh giá báo cáo tài chính trên web chứng khoán Huy Nguyễn chấm com. Anh chị vào xem miễn phí. "
           "Còn nếu tối nay anh chị đang rối, không biết mã mình cầm dính thuế nhiều hay ít, cứ nhắn Zalo cho em tên mã. Em xem cùng anh chị ba câu đó, rồi anh chị tự quyết.")),
 dict(k='end', cap=('THÁNG 4 NĂM NGOÁI', 'ANH CHỊ ĐÃ LÀM GÌ?'), cols=CC,
      say=("Còn anh chị, tháng tư năm ngoái anh chị đã bán, đã giữ, hay đã mua thêm? Và lần này anh chị định làm gì khác? Kể em nghe ở phần bình luận nhé.")),
]
import ql_post; S = ql_post.tach(S, max_tu=50)
for c in S: c['say'] = lib.doc(phat_am_doc(c['say']))
TIEU = 'Mỹ Đề Xuất Thuế 35% Với Hàng Việt: Lần Trước Ra Sao?'
MT = ("Đêm 25/11/2026, Văn phòng Đại diện Thương mại Mỹ đề xuất xem xét thuế tới 35% với hàng Việt Nam (20% nếu đạt thỏa thuận). Chưa có hiệu lực: góp ý đến 5/1/2027, điều trần từ 25/1/2027. "
      "Tháng 4/2025 thị trường đã gặp tin kiểu này: thuế 46%, VN-Index mất 223 điểm sau 4 phiên, rồi mức công bố tháng 7/2025 là 20%. "
      "Chuyện Cường – Hùng và 3 câu soi danh mục khi có tin thuế.\n\n"
      "Nguồn số liệu:\n"
      "• Văn phòng Đại diện Thương mại Mỹ (USTR), thông cáo 25/11/2026: kết luận điều tra Điều 301 với 14 nền kinh tế; Việt Nam: xem xét thuế tới 35%, 20% nếu đạt thỏa thuận thương mại đối ứng; nêu dệt may, da giày, đóng tàu, xi măng, điện tử – công nghệ thông tin; góp ý đến 5/1/2027, điều trần từ 25/1/2027\n"
      "• Dân trí 25/11/2026: điều tra kéo dài 8 tháng; thuế mới một phần thay các khoản thuế toàn cầu bị Tòa án Tối cao Mỹ bác hồi tháng 2\n"
      "• Báo Đầu tư 4/11/2026: xuất khẩu sang Mỹ 10 tháng 2026 đạt 159,40 tỷ USD; Tạp chí Kinh tế Tài chính 14/11/2026: Mỹ chiếm gần 32% xuất khẩu cả nước\n"
      "• Nhà Đầu tư, Báo Văn hóa, Thị trường Tài chính Tiền tệ 3/4/2025: thuế 46%; VN-Index giảm 87,99 điểm (6,68%) còn 1.229,84; 280 mã giảm sàn; vốn hóa mất 370.000 tỷ đồng\n"
      "• VnExpress 9/4/2025: VN-Index 1.094 điểm, 4 phiên mất 223 điểm, vốn hóa mất hơn 933.000 tỷ đồng\n"
      "• Nhân Dân 25/11/2026: VN-Index đóng cửa 1.687,45 điểm (trước khi có tin)\n"
      "• Cơ quan Phân tích Kinh tế Mỹ (BEA) 25/11/2026: GDP quý 3 ước tính lần hai 4,3% (dự báo 3,5%); PCE lõi tháng 10 tăng 3,3% so cùng kỳ (dự báo 3,2%). Fed họp 8–9/12/2026\n\n"
      "Đánh giá báo cáo tài chính từng doanh nghiệp, xem miễn phí: https://chungkhoanhuynguyen.com/#bctc\n"
      "Cần trao đổi riêng về mã đang cầm: Zalo 0365.188.286\n\n"
      "Nhân vật Cường, Hùng là hư cấu; số liệu là thật. Video không dự đoán thị trường, ba câu hỏi là mốc tự soi, không phải lời khuyên mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Tin nóng kể chuyện', ngay='2026-11-26', gio_goi_y='12:00', gio='12:00', nhac='lofi', can_duyet='anh Huy duyệt trước khi hẹn',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['thuế Mỹ 35%', 'Mỹ áp thuế Việt Nam', 'thuế quan Trump', 'thuế đối ứng', 'VN-Index', 'chứng khoán hôm nay', 'chứng khoán Việt Nam', 'Điều 301', 'xuất khẩu sang Mỹ', 'kinh tế Việt Nam'],
    bia_hook=['BÁN HAY GIỮ', 'ĐÊM NAY?'], badge='TIN NÓNG 25/11', bia_anh='ov:Ho Chi Minh City skyline night||Hanoi skyline night',
    bia_hook_b=['4 PHIÊN', 'MẤT 223 ĐIỂM'], badge_b='THÁNG 4/2025',
    bia_hook_c=['ĐỪNG HOẢNG', 'SOI 3 CÂU'], badge_c='THUẾ MỸ TỚI 35%',
    reel_hook='THUẾ MỸ 35%|LẦN TRƯỚC RA SAO???',
    fb_post=("Mỹ đề xuất thuế tới 35% với hàng Việt Nam – bán hay giữ?\n"
             "👉 Mới là đề xuất: góp ý đến 5/1/2027, điều trần từ 25/1/2027; có thỏa thuận thì mức nêu là 20%\n👉 Tháng 4/2025: tin thuế 46%, VN-Index mất 223 điểm sau 4 phiên\n👉 Tháng 7/2025: mức công bố là 20%\n"
             "3 câu soi danh mục khi có tin thuế.\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – Tin nóng kể chuyện: MỸ ĐỀ XUẤT THUẾ 35 phần trăm (QL1 Fable 5.2, 25/11/2026). Công thức: tin nóng → kể chuyện 2025 → túi tiền/danh mục → 3 câu soi danh mục → dẫn về tư vấn. 3 cảnh 3D.\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
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
