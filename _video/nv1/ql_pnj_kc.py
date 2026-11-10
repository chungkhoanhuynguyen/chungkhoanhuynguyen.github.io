# -*- coding: utf-8 -*-
# QL1 11/11/2026 – KÊNH CHÍNH, video dài kể chuyện (khuôn chuẩn kenh5 áp sang kênh chính, xưng em/anh chị – anh Huy chốt 11/11 04:26).
# Chủ đề nóng: PNJ mất ~77% trong 4 tháng (63.000 ngày 30/6 → 14.700 ngày 10/11/2026, WiData eod_adjust).
# Nguồn:
#  - BCTC PNJ (WiData fs_nonfin): Q1/2026 LNST cty mẹ 1.467 tỷ (Q1/2025: 678 tỷ); Q2/2026 −739 tỷ; Q3/2026 −257 tỷ; tồn kho 30/9 ~18.855 tỷ.
#  - Công an Thanh Hoá triệt phá đường dây buôn lậu kim cương xuyên quốc gia (thông báo 2/7/2026, 22 bị can, 1.100 viên – Vietnambiz 2/7);
#    GĐ PNJ-LAB bị bắt; kết luận ban đầu 20/8: kim cương buôn lậu bán cho khách cá nhân, không đưa vào hệ thống bán lẻ PNJ (CafeF 21/8).
#  - Làn sóng bán lại tháng 7: gần 6.000 tỷ, gần bằng cả năm 2025 (~7.000 tỷ); tiền + tiền gửi từ ~3.700 tỷ (30/6) còn 770 tỷ (30/9) gồm khoản vay 700 tỷ từ Chủ tịch (CafeF, Vietnambiz 21/10).
#  - Chính sách thu đổi trang sức kim cương 75–90% hoá đơn, kim cương rời có thể 95–98% (Nhà Đầu Tư 29/10); nghĩa vụ tích luỹ ~21.000 tỷ, "lời hứa không có thời hạn" (TGĐ Phan Quốc Công, VietnamFinance 21/10);
#    thanh toán thu đổi trong 120 ngày (SGGP 21/10); dự phòng 7.071 tỷ; kế hoạch 2026 lỗ 6.271 tỷ; huy động ~8.000 tỷ, phát hành riêng lẻ tối đa 550 triệu cp so với 511,7 triệu đang lưu hành (VnEconomy 22/10).
#  - Q2/2026 dự phòng 865,5 tỷ liên quan mua lại kim cương (CafeF 30/7); 2 tháng 7–8 biên gộp ~10% so với 18,5% (ĐTCK 28/9); đóng 25–30 cửa hàng.
#  - SJC bán ra: 184 triệu (27/2/2026) → 140,9 triệu (10/11/2026) (WiData).
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261111_0500'
KEY = 'CH1311PNJ'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, H_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (255, 120, 160), (34, 197, 94)
LAN = 'Chị Lan'; MINH = 'Minh – em trai'; CH = 'Cửa hàng trang sức'
S = [
 # ---------------- MỞ ĐẦU: cảnh đắt nhất ----------------
 dict(k='noti', ch='Mở đầu', cap=('MỘT ĐÊM THÁNG 7', 'HAI THÔNG BÁO'), cols=CR, noti=dict(gio='21:14', ngay='Thứ Năm', items=[
        ('Tin tức', 'Báo điện tử', 'Triệt phá đường dây buôn lậu kim cương xuyên quốc gia, giám đốc một đơn vị kiểm định bị bắt', R_),
        ('Zalo', 'Hội bạn thân', 'Lan ơi nhẫn kim cương của bà mua ở đâu? Mai đi bán lại không?', V_)]),
      say=("Một tối đầu tháng bảy, chị Lan đang dọn bát thì điện thoại sáng lên hai lần. Tin thứ nhất từ báo điện tử: triệt phá đường dây buôn lậu kim cương xuyên quốc gia, giám đốc một đơn vị kiểm định bị bắt. "
           "Tin thứ hai từ nhóm bạn thân: Lan ơi, nhẫn kim cương của bà mua ở đâu? Mai có đi bán lại không?")),
 dict(k='text', cap=('CHIẾC NHẪN 300 TRIỆU', 'CÒN ĐÁNG BAO NHIÊU?'), cols=CR, anh='ov:diamond ring box||diamond ring',
      say=("Chị Lan nhìn chiếc nhẫn trên tay. Ba trăm triệu, tiền thưởng Tết hai năm của hai vợ chồng. Người bán hứa: bất cứ lúc nào cần, cửa hàng mua lại chín mươi phần trăm. "
           "Đêm đó, không chỉ chị Lan mất ngủ. Hàng nghìn người cầm hoá đơn kim cương cũng đang tự hỏi cùng một câu.")),
 dict(k='bignum', cap=('CỔ PHIẾU PNJ', '30/6 → 10/11/2026'), cols=CR, value=-76.7, fmt='{:,.1f}', unit='%', top='TỪ 63.000 XUỐNG 14.700 ĐỒNG', sub='Quý 1/2026 vừa lãi 1.467 tỷ', col=RED,
      say=("Và sáng hôm sau, câu hỏi đó đổ vào sàn chứng khoán. Cổ phiếu PNJ, doanh nghiệp trang sức lớn nhất Việt Nam, từ sáu mươi ba nghìn đồng cuối tháng sáu, đến ngày mười tháng mười một chỉ còn mười bốn nghìn bảy trăm đồng, mất gần bảy mươi bảy phần trăm. "
           "Trong khi chỉ một quý trước đó, công ty vừa báo lãi một nghìn bốn trăm sáu mươi bảy tỷ đồng, gấp đôi cùng kỳ.")),
 dict(k='text', cap=('CHUYỆN GÌ ĐÃ XẢY RA', 'VỚI PNJ?'), cols=CC, anh='ov:jewelry store window||jewelry shop',
      say=("Hôm nay em sẽ cùng anh chị đi lại bốn tháng đó, qua mắt của hai người: chị Lan, một khách hàng cầm hoá đơn kim cương, và Minh, em trai chị, một nhà đầu tư cầm cổ phiếu PNJ vì nghĩ đó là cổ phiếu an toàn. "
           "Hai nhân vật là giả định, nhưng mọi con số đều lấy từ báo cáo tài chính và các bài báo, em để nguồn ở phần mô tả. "
           "Và cuối video, em sẽ chỉ ra một khoản nợ không nằm trên bảng cân đối kế toán, thứ đã làm một doanh nghiệp bốn mươi năm lao đao chỉ trong vài tuần.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='giay', ch='Chương 1 – Lời hứa trên hoá đơn', cap=('LỜI HỨA', 'MUA LẠI 90%'), cols=CC, moc=True, giay=dict(tieu_de='CHÍNH SÁCH THU ĐỔI', so='Trang sức gắn kim cương – áp dụng trước tháng 7/2026', dau='CAM KẾT', dieu=[
        ('Trang sức kim cương: thu đổi 75–90% giá trị hoá đơn gốc.', '75–90%'),
        ('Kim cương rời: có thể tới 95–98% giá trị.', 'GẦN NHƯ NGUYÊN GIÁ'),
        ('Thời hạn áp dụng: không ghi thời hạn.', 'KHÔNG HẾT HẠN')]),
      say=("Muốn hiểu chuyện này, phải bắt đầu từ một tờ giấy rất nhỏ đi kèm hoá đơn. Theo báo Nhà Đầu Tư, PNJ có chính sách thu đổi trang sức gắn kim cương ở mức bảy mươi lăm đến chín mươi phần trăm giá trị hoá đơn gốc, kim cương rời có loại tới chín mươi lăm đến chín mươi tám phần trăm. "
           "Với người mua, đây là lý do để yên tâm xuống tiền. Kim cương không chỉ là trang sức, mà gần như một cuốn sổ tiết kiệm đeo trên tay.")),
 dict(k='chat', cap=('"CHỊ CỨ YÊN TÂM', 'BÊN EM MUA LẠI"'), cols=CC, chat=dict(ten=CH, tv='Nhân viên tư vấn', gio='15:30', mau=X_, msgs=[
        ('Cửa hàng', 'Viên này 5 ly 4, nước D, chị đeo rất sang ạ'),
        ('me', 'Ba trăm triệu cũng nhiều, lỡ sau này cần tiền thì sao em?'),
        ('Cửa hàng', 'Chị cứ yên tâm, bên em mua lại 90% theo hoá đơn'),
        ('Cửa hàng', 'Mua kim cương ở đây như gửi tiết kiệm mà còn được đeo chị ạ')]),
      say=("Hai năm trước, chị Lan đứng trước quầy, phân vân. Ba trăm triệu cũng nhiều, lỡ sau này cần tiền thì sao em? Cô nhân viên cười: chị cứ yên tâm, bên em mua lại chín mươi phần trăm theo hoá đơn. "
           "Mua kim cương ở đây như gửi tiết kiệm mà còn được đeo. Chị Lan ký thẻ. Và chị không phải người duy nhất nghe câu đó.")),
 dict(k='text', cap=('MỘT LỜI HỨA', 'NHÂN VỚI HÀNG TRĂM NGHÌN KHÁCH'), cols=CC, anh='ov:jewelry display case||jewelry shop',
      say=("Bây giờ anh chị thử nhìn từ phía doanh nghiệp. Mỗi chiếc nhẫn bán ra là một khoản doanh thu đẹp trên báo cáo. Nhưng đi kèm nó là một lời hứa: bất cứ lúc nào khách muốn, công ty phải bỏ tiền mặt ra mua lại. "
           "Trong điều kiện bình thường, mọi chuyện rất ổn. Theo lời Tổng giám đốc PNJ tại đại hội cổ đông bất thường, khách bán lại rải rác theo nhu cầu cá nhân, thường trong ba đến năm năm đầu. "
           "Vấn đề là lời hứa đó cộng dồn qua từng năm. Đến cuối quý ba năm 2026, tổng giá trị sản phẩm còn nằm trong diện thu đổi lên tới khoảng hai mươi mốt nghìn tỷ đồng. Và lời hứa này, theo chính ông, không có thời hạn.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='chat', ch='Chương 2 – Người em trai cầm cổ phiếu', cap=('"CỔ PHIẾU QUỐC DÂN', 'ÔM LÀ ĂN"'), cols=CC, moc=True, chat=dict(ten=MINH, tv='Đang hoạt động', gio='11:45', mau=G_, msgs=[
        ('Minh', 'Chị ơi PNJ báo lãi quý 1 gần 1.500 tỷ, gấp đôi năm ngoái!'),
        ('Minh', 'Vàng lên, kim cương bán chạy. Em tăng tỷ trọng lên 40% danh mục rồi'),
        ('me', 'Em bỏ nhiều thế, có rủi ro gì không?'),
        ('Minh', 'Cổ phiếu quốc dân chị ơi, 40 năm chưa sao, ôm là ăn')]),
      say=("Cùng lúc đó, Minh, em trai chị Lan, đang rất vui. Tháng tư, anh nhắn chị: PNJ báo lãi quý một gần một nghìn năm trăm tỷ, gấp đôi năm ngoái. Vàng lên, kim cương bán chạy. Em tăng tỷ trọng lên bốn mươi phần trăm danh mục rồi. "
           "Chị Lan hỏi: em bỏ nhiều thế, có rủi ro gì không? Minh trả lời rất tự tin: cổ phiếu quốc dân chị ơi, bốn mươi năm chưa sao, ôm là ăn.")),
 dict(k='cards', cap=('LỢI NHUẬN PNJ', 'THEO QUÝ'), cols=CC, moc=True,
      cards=[('+678 tỷ', 'Quý 1/2025', ''), ('+1.467 tỷ', 'Quý 1/2026 – gấp đôi cùng kỳ', ''), ('Giá cổ phiếu', 'quanh 80.000 đồng đầu năm', '')],
      say=("Minh có lý do để tự tin. Theo báo cáo tài chính, quý một năm 2026, PNJ lãi một nghìn bốn trăm sáu mươi bảy tỷ đồng, gấp hơn hai lần mức sáu trăm bảy mươi tám tỷ cùng kỳ. "
           "Giá vàng lúc đó đang lên đỉnh, người người đi mua vàng, mua trang sức. Cổ phiếu quanh tám mươi nghìn đồng. "
           "Mọi con số trên báo cáo đều đẹp. Chỉ có một thứ không nằm trong những con số đó: hai mươi mốt nghìn tỷ tiền lời hứa.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='noti', ch='Chương 3 – Ngày 2 tháng 7', cap=('MỘT VỤ ÁN', 'KHÔNG Ở TRONG CỬA HÀNG'), cols=CR, moc=True, noti=dict(gio='07:02', ngay='Thứ Sáu', items=[
        ('Tin tức', 'Báo điện tử', 'Khởi tố 22 bị can, thu giữ 1.100 viên kim cương trong đường dây buôn lậu xuyên quốc gia', R_),
        ('Tin tức', 'Báo điện tử', 'Giám đốc công ty kiểm định trực thuộc doanh nghiệp trang sức lớn bị bắt', R_),
        ('Chứng khoán', 'Ứng dụng giao dịch', 'PNJ: giá sàn, dư bán lớn', R_)]),
      say=("Ngày hai tháng bảy, Công an tỉnh Thanh Hoá thông báo triệt phá một đường dây buôn lậu kim cương xuyên quốc gia, khởi tố hai mươi hai bị can, thu giữ một nghìn một trăm viên kim cương. "
           "Trong số người bị bắt có giám đốc công ty kiểm định trực thuộc PNJ. Sáng hôm sau, cổ phiếu PNJ nằm sàn.")),
 dict(k='text', cap=('CÔNG AN KẾT LUẬN', 'KHÔNG VÀO HỆ THỐNG BÁN LẺ'), cols=CC, anh='ov:magnifying glass diamond||diamond',
      say=("Em cần nói rõ điểm này cho công bằng. Ngày hai mươi tháng tám, theo kết quả điều tra ban đầu Công an tỉnh Thanh Hoá công bố, toàn bộ số kim cương buôn lậu được bán cho khách hàng cá nhân, không đưa vào hệ thống bán lẻ của PNJ. "
           "PNJ cũng khẳng định đây là trách nhiệm cá nhân, và công ty có đầy đủ hồ sơ nhập khẩu hợp lệ. "
           "Nhưng anh chị để ý: kết luận đó đến sau bảy tuần. Còn nỗi sợ thì chỉ cần một đêm.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='chat', ch='Chương 4 – Hàng người trước cửa hàng', cap=('"BÁN LẠI ĐI', 'TRƯỚC KHI HỌ ĐỔI CHÍNH SÁCH"'), cols=CR, moc=True, chat=dict(ten='Hội bạn thân', tv='9 thành viên', gio='06:50', msgs=[
        ('Thu', 'Tôi ra cửa hàng từ 6 giờ, đã có hàng người rồi'),
        ('Hằng', 'Bán lại đi các bà, trước khi họ đổi chính sách'),
        ('me', 'Nhưng nhẫn của tôi đâu có vấn đề gì'),
        ('Thu', 'Bà không bán thì người khác bán. Hết tiền là họ không mua nữa đâu')]),
      say=("Sáng thứ hai, nhóm bạn chị Lan sôi lên từ sáu giờ. Thu nhắn: tôi ra cửa hàng từ sáu giờ, đã có hàng người rồi. Hằng: bán lại đi các bà, trước khi họ đổi chính sách. "
           "Chị Lan gõ: nhưng nhẫn của tôi đâu có vấn đề gì. Thu trả lời một câu mà chị nhớ mãi: bà không bán thì người khác bán. Hết tiền là họ không mua nữa đâu.")),
 dict(k='text', cap=('KHÔNG AI SỢ KIM CƯƠNG GIẢ', 'HỌ SỢ NGƯỜI KHÁC BÁN TRƯỚC'), cols=CR, anh='ov:crowd queue store||people waiting line',
      say=("Câu nói của Thu chính là cơ chế của mọi cuộc tháo chạy. Người ta không bán vì chắc chắn kim cương của mình có vấn đề. Người ta bán vì sợ người khác bán trước, và đến lượt mình thì cửa hàng hết tiền. "
           "Ngân hàng gặp nó và gọi là rút tiền hàng loạt. Quỹ đầu tư gặp nó và gọi là làn sóng rút vốn. Và tháng bảy năm 2026, một doanh nghiệp trang sức gặp nó lần đầu tiên.")),
 dict(k='cards', cap=('THÁNG 7/2026', 'KHÁCH BÁN LẠI BAO NHIÊU?'), cols=CR, moc=True,
      cards=[('~6.000 tỷ', 'giá trị thu mua lại riêng tháng 7', ''), ('~7.000 tỷ', 'cả năm 2025', ''), ('3.700 → 770 tỷ', 'tiền và tiền gửi, 30/6 → 30/9', '')],
      say=("Con số thật đáng sợ hơn mọi tưởng tượng. Theo ban điều hành PNJ tại đại hội bất thường, riêng tháng bảy, giá trị hàng khách bán lại lên tới gần sáu nghìn tỷ đồng, gần bằng cả năm 2025. "
           "Tiền và tiền gửi của công ty từ khoảng ba nghìn bảy trăm tỷ cuối tháng sáu, còn bảy trăm bảy mươi tỷ cuối tháng chín. "
           "Và bảy trăm bảy mươi tỷ đó đã bao gồm khoản vay cá nhân bảy trăm tỷ đồng từ chính Chủ tịch hội đồng quản trị, giải ngân trong tháng chín để giữ thanh khoản.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='call', ch='Chương 5 – Cuộc gọi của chị Lan', cap=('"CHỊ ĐỢI', '120 NGÀY Ạ"'), cols=CR, moc=True, call=dict(ten=CH, phu='Tổng đài chăm sóc khách hàng', mau=R_, loi=[
        'Dạ theo chính sách mới, bên em ghi nhận yêu cầu thu đổi của chị',
        'Tiền sẽ được thanh toán trong vòng 120 ngày, theo hạn mức ạ']),
      say=("Cuối cùng, chị Lan cũng gọi. Giọng nhân viên lịch sự nhưng mệt mỏi: dạ theo chính sách mới, bên em ghi nhận yêu cầu thu đổi của chị. Tiền sẽ được thanh toán trong vòng một trăm hai mươi ngày, theo hạn mức ạ. "
           "Chị Lan hỏi lại: thế không trả ngay được hả em? Đầu dây bên kia im lặng mấy giây.")),
 dict(k='text', cap=('KHÔNG ĐỦ TIỀN MẶT', 'ĐỂ GIỮ LỜI HỨA NGAY'), cols=CR, anh='ov:empty cash register||jewelry shop',
      say=("Câu trả lời thật nằm ở đại hội cổ đông ngày hai mươi mốt tháng mười. Khi cổ đông hỏi bao giờ rút ngắn được thời gian thanh toán, Tổng giám đốc PNJ trả lời, theo báo Sài Gòn Giải Phóng: với khả năng dòng tiền hiện nay, việc mua lại kim cương ngay bằng tiền mặt chưa khả thi. "
           "Cuối tháng bảy, khi mất thanh khoản, công ty đã phải điều chỉnh chính sách thu đổi. Dòng hàng bán lại giảm, nhưng doanh thu cũng giảm theo, vì niềm tin của người mua đã thay đổi.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='noti', ch='Chương 6 – Danh mục của Minh', cap=('MỖI SÁNG', 'MỘT THÔNG BÁO ĐỎ'), cols=CR, moc=True, noti=dict(gio='09:16', ngay='Thứ Hai', items=[
        ('Chứng khoán', 'Ứng dụng giao dịch', 'PNJ giảm sàn. Danh mục của bạn: −18% trong tuần', R_),
        ('Zalo', 'Chị Lan', 'Minh ơi em còn giữ cổ phiếu đó không?', V_)]),
      say=("Còn Minh, mỗi sáng là một thông báo đỏ. PNJ giảm sàn. Danh mục của bạn giảm mười tám phần trăm trong tuần. Chị Lan nhắn: Minh ơi, em còn giữ cổ phiếu đó không? "
           "Minh không trả lời. Bốn mươi phần trăm danh mục của anh đang nằm ở đó.")),
 dict(k='chat', cap=('"BÁN BÂY GIỜ', 'LÀ CHỐT LỖ"'), cols=CR, chat=dict(ten=MINH, tv='Đang hoạt động', gio='23:10', mau=G_, msgs=[
        ('Minh', 'Em chưa bán chị ạ. Công an kết luận rồi, đâu phải lỗi công ty'),
        ('Minh', 'Bán bây giờ là chốt lỗ. Doanh nghiệp 40 năm không sập được'),
        ('me', 'Chị chỉ thấy cửa hàng không có tiền trả chị thôi'),
        ('Minh', '...')]),
      say=("Mười một giờ đêm, Minh trả lời: em chưa bán chị ạ. Công an kết luận rồi, đâu phải lỗi công ty. Bán bây giờ là chốt lỗ. Doanh nghiệp bốn mươi năm không sập được. "
           "Chị Lan gõ một câu rất đơn giản: chị chỉ thấy cửa hàng không có tiền trả chị thôi. Minh gõ, xoá, rồi chỉ gửi ba dấu chấm.")),
 dict(k='text', cap=('MINH ĐÚNG MỘT NỬA', 'VÀ SAI NỬA QUAN TRỌNG'), cols=CC, anh='ov:stock market screen red||stock market',
      say=("Minh đúng một nửa. Vụ án không làm kim cương trong cửa hàng thành giả. Nhưng anh sai ở nửa quan trọng hơn. "
           "Thứ đe doạ doanh nghiệp không phải vụ án. Mà là tiền mặt không đủ cho một lời hứa hai mươi mốt nghìn tỷ, đúng vào lúc mọi người cùng muốn đòi lời hứa đó một lúc.")),
 # ---------------- CHƯƠNG 7 ----------------
 dict(k='cards', ch='Chương 7 – Những con số sau cơn bão', cap=('TỪ LÃI KỶ LỤC', 'ĐẾN KẾ HOẠCH LỖ'), cols=CR, moc=True,
      cards=[('+1.467 tỷ', 'Quý 1/2026', ''), ('−739 tỷ', 'Quý 2/2026', ''), ('−257 tỷ', 'Quý 3/2026', '')],
      say=("Và đây là những gì hiện lên trên báo cáo tài chính. Quý một năm 2026, lãi một nghìn bốn trăm sáu mươi bảy tỷ. Quý hai, lỗ bảy trăm ba mươi chín tỷ, trong đó có khoản dự phòng tám trăm sáu mươi lăm tỷ liên quan đến làn sóng mua lại kim cương. "
           "Quý ba, lỗ thêm hai trăm năm mươi bảy tỷ. Hai tháng bảy và tám, biên lợi nhuận gộp chỉ còn khoảng mười phần trăm, so với khoảng mười tám phẩy năm phần trăm cùng kỳ.")),
 dict(k='giay', cap=('NGHỊ QUYẾT', 'ĐẠI HỘI BẤT THƯỜNG 21/10'), cols=CR, giay=dict(tieu_de='KẾ HOẠCH ĐIỀU CHỈNH NĂM 2026', so='Theo VnEconomy, CafeF 21–22/10/2026', dau='THÔNG QUA', dieu=[
        ('Kế hoạch lợi nhuận sau thuế 2026: lỗ 6.271 tỷ đồng.', 'GỒM DỰ PHÒNG 7.071 TỶ'),
        ('Huy động khoảng 8.000 tỷ đồng để tái thiết dòng tiền.', ''),
        ('Phát hành riêng lẻ tối đa 550 triệu cổ phiếu (đang lưu hành 511,7 triệu).', 'GẤP ĐÔI SỐ CỔ PHIẾU'),
        ('Đóng 25–30 cửa hàng trong năm 2026.', '')]),
      say=("Ngày hai mươi mốt tháng mười, đại hội cổ đông bất thường thông qua kế hoạch năm 2026 mới: lỗ sáu nghìn hai trăm bảy mươi mốt tỷ đồng, đã gồm khoản dự phòng bảy nghìn không trăm bảy mươi mốt tỷ cho nghĩa vụ mua lại trong tương lai. "
           "Công ty cần huy động khoảng tám nghìn tỷ, qua phương án phát hành riêng lẻ tối đa năm trăm năm mươi triệu cổ phiếu, trong khi số đang lưu hành là năm trăm mười một phẩy bảy triệu. "
           "Nghĩa là nếu phát hành hết, số cổ phiếu có thể tăng gấp đôi. Với cổ đông cũ như Minh, mỗi cổ phiếu sẽ chỉ còn sở hữu khoảng một nửa công ty so với trước.")),
 # ---------------- CHƯƠNG 8 ----------------
 dict(k='checklist', ch='Chương 8 – Khoản nợ không nằm trên bảng cân đối', cap=('3 CÂU HỎI', 'TRƯỚC KHI GỌI LÀ "AN TOÀN"'), cols=CC, moc=True,
      items=[('Doanh nghiệp đang hứa trả tiền cho ai, bao nhiêu, khi nào?', GREEN), ('Nếu tất cả cùng đòi một lúc, tiền mặt đủ mấy phần?', GREEN), ('Một cổ phiếu chiếm bao nhiêu % danh mục của mình?', GOLD)],
      say=("Đây là phần em muốn anh chị nhớ nhất. Bảng cân đối kế toán cho biết doanh nghiệp đang nợ ai. Nhưng có những lời hứa không nằm trên đó, hoặc chỉ hiện ra khi đã quá muộn: cam kết mua lại, bảo lãnh, chính sách đổi trả. "
           "Trước khi gọi một cổ phiếu là an toàn, hãy hỏi ba câu. Một, doanh nghiệp đang hứa trả tiền cho ai, bao nhiêu, và khi nào? Câu trả lời thường nằm ở thuyết minh báo cáo tài chính hoặc báo cáo thường niên. "
           "Hai, nếu tất cả cùng đòi một lúc, tiền mặt đủ được mấy phần? Ngay trước biến cố, cuối tháng sáu, PNJ có khoảng ba nghìn bảy trăm tỷ tiền mặt, so với lời hứa hai mươi mốt nghìn tỷ. "
           "Ba, một cổ phiếu đang chiếm bao nhiêu phần trăm danh mục của mình? Bốn mươi năm lịch sử không bảo vệ được bốn mươi phần trăm danh mục của Minh.")),
 dict(k='text', cap=('CỔ PHIẾU QUỐC DÂN', 'KHÔNG CÓ NGHĨA LÀ KHÔNG RỦI RO'), cols=CC, anh='ov:balance scale||Ho Chi Minh City skyline',
      say=("Em không nói PNJ sẽ phục hồi hay không. Đó là câu hỏi của tương lai, phụ thuộc vào việc huy động vốn, xử lý hàng tồn kho và lấy lại niềm tin khách hàng. Video này cũng không phải khuyến nghị mua hay bán. "
           "Điều em muốn nói là: một doanh nghiệp tốt vẫn có thể gặp khủng hoảng khi một rủi ro ẩn gặp đúng một cú sốc niềm tin. "
           "Nếu anh chị muốn soi nhanh P trên E, lợi nhuận từng quý và dòng tiền của hơn bốn trăm mã trước khi xuống tiền, có thể tra miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Chiếc nhẫn và bài học', cap=('"LẦN SAU', 'EM HỎI CHỊ ĐÃ"'), cols=CC, moc=True, chat=dict(ten=MINH, tv='Đang hoạt động', gio='20:05', mau=G_, msgs=[
        ('Minh', 'Chị ơi, em bán bớt rồi. Lỗ hơn một nửa phần đó'),
        ('me', 'Chị vẫn đeo cái nhẫn. Không bán nữa, coi như kỷ niệm'),
        ('Minh', 'Lần sau thấy ai bảo "ôm là ăn", em hỏi chị đã'),
        ('me', 'Hỏi cái báo cáo tài chính ấy, đừng hỏi chị')]),
      say=("Bốn tháng sau, Minh nhắn: chị ơi, em bán bớt rồi, lỗ hơn một nửa phần đó. Chị Lan trả lời: chị vẫn đeo cái nhẫn, không bán nữa, coi như kỷ niệm. "
           "Minh gửi thêm: lần sau thấy ai bảo ôm là ăn, em hỏi chị đã. Chị Lan cười: hỏi cái báo cáo tài chính ấy, đừng hỏi chị.")),
 dict(k='end', cap=('ANH CHỊ ĐÃ TỪNG CẦM', 'MỘT "CỔ PHIẾU AN TOÀN" NHƯ VẬY?'), cols=CC,
      say=("Anh chị đã từng cầm một cổ phiếu mà ai cũng bảo là an toàn, rồi một sáng thức dậy thấy nó nằm sàn chưa? Bài học lớn nhất của anh chị là gì? "
           "Kể cho em và mọi người ở phần bình luận nhé. Nếu thấy video hữu ích, anh chị đăng ký kênh để xem tập sau: em sẽ mổ xẻ một lời hứa khác, lời hứa lãi suất cao của trái phiếu doanh nghiệp.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'PNJ Mất 77% Trong 4 Tháng: Lời Hứa Mua Lại Kim Cương 21.000 Tỷ Và Bài Học Cho Nhà Đầu Tư'
MT = ("Quý 1/2026 PNJ lãi 1.467 tỷ, gấp đôi cùng kỳ. Bốn tháng sau, cổ phiếu từ 63.000 xuống 14.700 đồng (−77%), công ty lên kế hoạch lỗ 6.271 tỷ năm 2026. "
      "Chuyện gì đã xảy ra? Câu chuyện kể qua mắt một khách hàng cầm hoá đơn kim cương và một nhà đầu tư cầm cổ phiếu \"quốc dân\".\n\n"
      "Nguồn số liệu:\n"
      "• BCTC PNJ: LNST công ty mẹ Q1/2026 +1.467 tỷ, Q2/2026 −739 tỷ, Q3/2026 −257 tỷ\n"
      "• Công an tỉnh Thanh Hoá triệt phá đường dây buôn lậu kim cương xuyên quốc gia (2/7/2026); kết luận ban đầu 20/8: kim cương buôn lậu không đưa vào hệ thống bán lẻ PNJ (CafeF 21/8/2026)\n"
      "• Làn sóng bán lại tháng 7 gần 6.000 tỷ; tiền và tiền gửi 3.700 tỷ → 770 tỷ, gồm khoản vay 700 tỷ từ Chủ tịch HĐQT (CafeF, Vietnambiz 21/10/2026)\n"
      "• Chính sách thu đổi 75–90% hoá đơn, kim cương rời tới 95–98% (Nhà Đầu Tư 29/10/2026); nghĩa vụ tích luỹ ~21.000 tỷ (VietnamFinance 21/10/2026)\n"
      "• Kế hoạch 2026 lỗ 6.271 tỷ gồm dự phòng 7.071 tỷ; phát hành riêng lẻ tối đa 550 triệu cổ phiếu (VnEconomy 22/10/2026)\n"
      "• Giá cổ phiếu: đóng cửa 30/6/2026 và 10/11/2026\n\n"
      "Soi P/E, lợi nhuận từng quý, dòng tiền 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật chị Lan, Minh là hư cấu. Video không nhằm kết luận về trách nhiệm pháp lý của bất kỳ cá nhân, tổ chức nào; thông tin vụ án theo công bố của cơ quan điều tra và báo chí.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Chuyện gì đã xảy ra?', ngay='2026-11-13', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['PNJ', 'cổ phiếu PNJ', 'PNJ lỗ', 'thu đổi kim cương', 'PNJ kim cương', 'chuyện gì đã xảy ra với PNJ', 'rủi ro ẩn', 'đọc báo cáo tài chính', 'cổ phiếu quốc dân'],
    bia_hook=['MẤT 77%', 'TRONG 4 THÁNG'], badge='CHUYỆN GÌ ĐÃ XẢY RA VỚI PNJ?',
    bia_anh='ov:diamond ring||diamond',
    bia_hook_b=['LÃI 1.467 TỶ', 'RỒI LỖ 6.271 TỶ'], badge_b='PNJ: VÌ SAO?',
    bia_hook_c=['LỜI HỨA', '21.000 TỶ'], badge_c='KHOẢN NỢ KHÔNG AI THẤY',
    fb_post=("Quý 1/2026 lãi 1.467 tỷ, gấp đôi cùng kỳ. 4 tháng sau cổ phiếu −77%, kế hoạch lỗ 6.271 tỷ 😳\n\n"
             "👉 Tháng 7: khách bán lại kim cương gần 6.000 tỷ, bằng cả năm 2025\n👉 Tiền mặt 3.700 tỷ → 770 tỷ (đã gồm 700 tỷ vay từ Chủ tịch)\n"
             "👉 Lời hứa mua lại tích luỹ ~21.000 tỷ, \"không có thời hạn\"\n\nBài học: có những khoản nợ không nằm trên bảng cân đối.\n\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – kể chuyện 'Chuyện gì đã xảy ra với PNJ' (QL1 11/11/2026).\n"
    "GOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), len(TIEU))
