# -*- coding: utf-8 -*-
# QL1 10/11/2026 – kênh @chungkhoanhuynguyen5, tập 2 "Vì Sao Thật Tệ Khi Vào Nhóm Phím Hàng". Kể nhập vai "bạn" (anh Huy cho phép 10/11).
# Vụ thật: CMS – CA Hà Nội khởi tố 7 bị can 15/8/2024 (VietnamBiz/ANTĐ 30/8/2024); Fnory.com – CA Thanh Hoá 12/2/2025, >200 tỷ, 9 bị can (Tuổi Trẻ);
# mạo danh KIS – UBCKNN cảnh báo 23/2/2024 (ANTĐ); sàn "chứng khoán ảo" – CA TP.HCM công bố 9/11/2026, 14 người nước ngoài, 112 điện thoại (Thanh Niên).
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
LO = '/tmp/cw/_video/queue/20261110_1900_vt'
KEY = 'VT5PHIMHANG'; CC = (WHITE, GOLD); CR = (WHITE, RED)
A = lambda n: 'repo:_video/anh_ai/phimhang/%02d.jpg' % n
v = lambda x, d=0: lib.vn(x, d)
S = [
 # ---------------- MỞ ĐẦU (0:00–0:45) ----------------
 dict(k='hook', ch='Mở đầu', label='Vì sao thật tệ khi…', cap=('6 GIỜ SÁNG', 'TRONG NHÀ VỆ SINH'), cols=CR, anh=A(1),
      say=("Sáu giờ sáng, trong nhà vệ sinh của một công ty kho vận ở Bình Dương, có một người đàn ông ngồi im đã hai mươi phút. "
           "Không phải vì đau bụng. Mà vì nhóm Zalo VIP Kim Cương vừa báo: chín giờ mười lăm, vào lệnh.")),
 dict(k='text', cap=('NGƯỜI ĐÀN ÔNG ĐÓ', 'CHÍNH LÀ BẠN'), cols=CC, anh=A(2),
      say=("Màn hình điện thoại toàn ảnh tài khoản xanh lè. Người này lãi 40 triệu, người kia vừa mua được xe. Ai cũng cảm ơn thầy. "
           "Người đàn ông đó chính là bạn. Và ba tháng nữa, bạn sẽ mất 470 triệu đồng, mất luôn cả niềm tin của vợ. Tất cả chỉ vì một nhóm chat hai nghìn thành viên, mà gần như không ai trong đó là người thật.")),
 dict(k='text', cap=('VÌ SAO THẬT TỆ KHI', 'VÀO NHÓM PHÍM HÀNG'), cols=CC, anh=A(3),
      say=("Hôm nay mình sẽ cùng bạn sống lại từng ngày của câu chuyện đó: vì sao thật tệ khi vào nhóm phím hàng. "
           "Câu chuyện là giả định, nhưng mọi thủ đoạn trong video đều lấy từ những vụ án có thật đã bị công an khởi tố, và mình sẽ nêu rõ từng vụ ở cuối video.")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='text', ch='Chương 1 – Người đàn ông chậm chân nhất', cap=('31 TUỔI, LƯƠNG 14 TRIỆU', 'VỢ BẦU THÁNG THỨ SÁU'), cols=CC, moc=True, anh=A(4),
      say=("Bạn 31 tuổi, làm giám sát kho, lương 14 triệu một tháng. Vợ bạn tên Hà, đang bầu tháng thứ sáu. "
           "Hai vợ chồng thuê một căn phòng 20 mét vuông, cuối tháng nào cũng ngồi tính tiền điện, tiền sữa bầu, tiền gửi về quê. "
           "Trong ngân hàng, bạn có 300 triệu, gom góp suốt bảy năm. Mẹ vợ hứa cho thêm 200 triệu, để sang năm hai đứa trả trước một căn chung cư nhỏ.")),
 dict(k='text', cap=('500 TRIỆU', 'VÀ MỘT GIẤC MƠ CĂN HỘ'), cols=CC, anh=A(4),
      say=("Năm trăm triệu. Với bạn, đó là cả một gia tài. Nhưng mỗi lần lên mạng xem giá chung cư, bạn lại thấy nó bé dần. "
           "Căn hộ hai phòng ngủ ở rìa thành phố, năm ngoái hỏi giá còn vừa, năm nay đã nhảy lên một bậc khác. "
           "Lãi tiết kiệm mỗi tháng được hơn hai triệu, chưa bằng một tháng tiền sữa với bỉm cho đứa con sắp chào đời. "
           "Bạn bắt đầu có cảm giác: cứ để tiền nằm im thế này, mình đang thua.")),
 dict(k='text', cap=('AI CŨNG ĐANG LÃI', 'TRỪ MÌNH'), cols=CC, anh=A(5),
      say=("Rồi bữa cơm trưa ở căng tin công ty, thằng Tùng bên phòng kế toán chìa điện thoại ra khoe. "
           "Mày xem, tháng này tao ăn ba mươi phần trăm. Vào nhóm của thầy Phong đi, thầy phím mã nào là mã đấy bay. "
           "Bạn nhìn cái màn hình đỏ xanh nhảy múa, nghe chữ thầy, chữ phím, chữ bay, mà thấy mình như người tối cổ. "
           "Tối hôm đó, lần đầu tiên trong đời, bạn gõ lên Facebook ba chữ: học chứng khoán.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='text', ch='Chương 2 – Lời mời ngọt như đường phèn', cap=('CHUYÊN GIA 15 NĂM', 'TẶNG 3 MÃ MIỄN PHÍ'), cols=CC, moc=True, anh=A(6),
      say=("Thuật toán của mạng xã hội làm việc nhanh hơn bạn tưởng. Sáng hôm sau, mỗi lần mở điện thoại là một quảng cáo. "
           "Một người đàn ông mặc vest đứng trước bảng điện tử. Chữ vàng rực rỡ: chuyên gia mười lăm năm kinh nghiệm, tỷ lệ thắng 92 phần trăm, tặng miễn phí ba mã cổ phiếu tuần này. "
           "Bạn bấm vào. Ba mươi giây sau có tin nhắn. Người nhắn tự giới thiệu là Thư, trợ lý của thầy Phong.")),
 dict(k='text', cap=('"ANH ƠI EM LÀ THƯ"', 'TRỢ LÝ CỦA THẦY'), cols=CC, anh=A(7),
      say=("Ảnh đại diện của Thư là một cô gái tóc dài, áo sơ mi trắng, ngồi trước laptop trong một văn phòng kính. "
           "Anh ơi, em là Thư bên đội ngũ của thầy Phong. Anh đầu tư lâu chưa ạ? Dạ không sao đâu anh, người mới lại càng dễ thành công, vì chưa bị nhiễm thói quen xấu. "
           "Em mời anh vào nhóm miễn phí của thầy nhé. Tuần này thầy chỉ nhận thêm năm mươi người thôi ạ. "
           "Bạn chưa từng được ai gọi là người dễ thành công. Bạn bấm vào đường link.")),
 dict(k='bignum', cap=('NHÓM ZALO MIỄN PHÍ', 'THÀNH VIÊN'), cols=CC, value=2148, fmt='{:,.0f}', unit='', top='CỘNG ĐỒNG ĐẦU TƯ THÔNG MINH', sub='ảnh lãi, lời cảm ơn, và một ông thầy', col=GOLD,
      say=("Nhóm có tên Cộng Đồng Đầu Tư Thông Minh, hai nghìn một trăm bốn mươi tám thành viên. "
           "Vừa vào, bạn đã choáng. Chị Lan Anh khoe tài khoản lãi 38 phần trăm. Anh Hùng gửi ảnh chuyển khoản tạ ơn thầy. "
           "Một cô giáo về hưu kể đã trả hết nợ cho con nhờ làm theo thầy. Mỗi tối tám giờ, thầy Phong lên sóng phân tích thị trường, giọng chậm rãi, chắc nịch, toàn thuật ngữ bạn chưa nghe bao giờ.")),
 dict(k='text', cap=('2.148 THÀNH VIÊN', 'MẤY NGƯỜI LÀ NGƯỜI THẬT?'), cols=CR, anh=A(8),
      say=("Có một điều bạn không biết. Trong hai nghìn người đó, phần lớn những tài khoản đang khen thầy là chân gỗ, tức là người của chính nhóm, hoặc tài khoản ảo. "
           "Năm 2024, Ủy ban Chứng khoán Nhà nước đã cảnh báo một vụ như vậy. Các đối tượng mạo danh nhân viên một công ty chứng khoán, lập nhóm Zalo với cái tên rất học thuật. "
           "Rồi cho các tài khoản chân gỗ liên tục ca ngợi một người và khoe lãi, để những người mới như bạn tự tin xuống tiền.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='text', ch='Chương 3 – Ba mã miễn phí và cái bẫy đầu tiên', cap=('MÃ ĐẦU TIÊN', 'TĂNG 12% TRONG 5 PHIÊN'), cols=CC, moc=True, anh=A(9),
      say=("Tuần đầu, thầy cho miễn phí đúng ba mã như đã hứa. Bạn rụt rè mua thử 50 triệu một mã. Năm phiên sau, mã đó tăng mười hai phần trăm. "
           "Bạn lãi sáu triệu, gần bằng nửa tháng lương. Bạn ngồi trong kho, nhìn con số xanh đó mà tim đập thình thịch. "
           "Mã thứ hai đi ngang. Mã thứ ba giảm nhẹ, nhưng thầy đã dặn trước là sẽ cắt lỗ, nên bạn còn thấy thầy đúng là chuyên nghiệp.")),
 dict(k='text', cap=('VÌ SAO MÃ CỦA THẦY', 'LẠI TĂNG?'), cols=CR, anh=A(10),
      say=("Bạn nghĩ thầy giỏi. Nhưng hãy nghĩ theo cách khác. Nếu nhóm đã gom sẵn một mã nhỏ từ trước, rồi hô cho hai nghìn người cùng mua trong một buổi sáng, thì mã đó tăng là chuyện đương nhiên. "
           "Hãy nhìn vụ thao túng cổ phiếu CMS mà công an Hà Nội khởi tố năm 2024. Các đối tượng lập nhóm Zalo và Telegram, hô hào thành viên mua đúng mã mà họ đã gom. "
           "Có những ngày nhận định giá của admin khớp đúng với giá thị trường trong phiên. Không phải vì họ đoán giỏi, mà vì chính họ đang kéo giá.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='cards', ch='Chương 4 – Phòng VIP Kim Cương', cap=('MUỐN NHẬN', 'HÀNG CỦA TAY TO?'), cols=CC, moc=True,
      cards=[('15 triệu', 'phí phòng VIP mỗi tháng', ''), ('5 suất', 'còn lại, hết hạn tối nay', ''), ('x2', 'mục tiêu mã "có tay to đứng sau"', '')],
      say=("Đến tuần thứ ba, Thư nhắn riêng. Anh ơi, nhóm miễn phí chỉ là để mọi người làm quen thôi. Hàng thật của thầy nằm ở phòng VIP Kim Cương. "
           "Ở đó có mã có tay to đứng sau, mục tiêu gấp đôi trong một tháng. Phí 15 triệu một tháng anh nhé. "
           "Tháng này chỉ còn năm suất, hết hạn lúc mười hai giờ đêm nay. Em giữ cho anh một suất được không ạ?")),
 dict(k='text', cap=('15 TRIỆU', 'HAY MỘT CĂN HỘ?'), cols=CC, anh=A(11),
      say=("Mười lăm triệu. Hơn một tháng lương. Bạn đứng ngoài ban công phòng trọ, nhìn vào trong thấy Hà đang ngồi gấp quần áo sơ sinh mua ở chợ. "
           "Bạn nhẩm tính: nếu đúng mục tiêu gấp đôi, 500 triệu thành một tỷ, mười lăm triệu tiền phí có là gì. "
           "Bạn chuyển khoản lúc mười một giờ năm mươi tám phút đêm. Thư gửi lại một sticker trái tim và một câu: chúc mừng anh đã bước vào thế giới của người chiến thắng.")),
 dict(k='checklist', cap=('LUẬT CỦA', 'PHÒNG VIP'), cols=CR, anh=A(12),
      items=[('Chỉ mua khi có lệnh của thầy', GOLD), ('Không được bán khi chưa có lệnh', RED), ('Không bàn mã ra ngoài', GOLD), ('Ai nói tiêu cực sẽ bị mời ra', RED)],
      say=("Phòng VIP có luật riêng, được ghim ngay đầu nhóm. Một, chỉ mua khi có lệnh của thầy. Hai, không được bán khi chưa có lệnh, vì bán sớm là phá hàng của anh em. "
           "Ba, không bàn mã ra ngoài. Bốn, ai nói tiêu cực sẽ bị mời ra khỏi nhóm. "
           "Bạn đọc xong thấy rất chuyên nghiệp, có kỷ luật như quân đội. Bạn không để ý rằng cả bốn điều luật đều phục vụ một mục đích: giữ bạn ngồi yên trong khi người khác bán.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='text', ch='Chương 5 – Mã X và ba phiên tím', cap=('"ALL IN MÃ X"', '"MỤC TIÊU GẤP ĐÔI"'), cols=CR, moc=True, anh=A(13),
      say=("Thứ Hai, tám giờ bốn mươi lăm sáng. Thầy Phong nhắn vào phòng VIP một tin duy nhất, in đậm. "
           "Mã X. Hàng có thông tin. Vùng mua quanh giá tham chiếu. Tỷ trọng tối đa. Mục tiêu gấp đôi. "
           "Mã X là một cổ phiếu nhỏ bạn chưa từng nghe tên. Mình gọi tạm là mã X, vì kịch bản này đã lặp lại với rất nhiều mã khác nhau. "
           "Bạn bán hết các mã đang có, dồn toàn bộ 500 triệu vào mã X. Kể cả 200 triệu mẹ vợ vừa chuyển cho.")),
 dict(k='bars', cap=('MÃ X', '3 PHIÊN TĂNG TRẦN'), cols=CC, moc=True,
      bars=[('Mua', 100, BLUE, '100'), ('Phiên 1', 107, GREEN, '+7%'), ('Phiên 2', 114, GREEN, '+14%'), ('Phiên 3', 123, GREEN, '+23%')],
      say=("Và mã X tăng trần. Một phiên. Hai phiên. Ba phiên liên tiếp. Màu tím phủ kín bảng điện. "
           "Tài khoản của bạn từ 500 triệu lên hơn 610 triệu. Phòng VIP vỡ òa. Chị Lan Anh gửi ảnh ăn mừng. Anh Hùng viết: cả đời chưa thấy ai phím chuẩn như thầy. "
           "Bạn chụp màn hình gửi cho thằng Tùng. Tối đó, lần đầu tiên sau nhiều tháng, bạn dẫn Hà đi ăn lẩu, gọi thêm đĩa bò Mỹ mà không nhìn giá.")),
 dict(k='text', cap=('BẠN MUỐN CHỐT LỜI', 'THẦY BẢO: GIỮ CHẶT'), cols=CR, anh=A(14),
      say=("Sáng phiên thứ tư, bạn bỗng muốn chốt lời. 110 triệu, gần tám tháng lương. Bạn nhắn hỏi. Thư trả lời gần như ngay lập tức. "
           "Anh ơi, thầy chưa có lệnh. Hàng này mục tiêu gấp đôi, giờ mới đi được một phần năm chặng đường. Bán bây giờ là bán non, mấy anh bán sớm tháng trước giờ tiếc lắm. "
           "Bạn nhìn lại luật thứ hai của phòng VIP. Bạn đặt điện thoại xuống. Bạn giữ.")),
 # ---------------- CHƯƠNG 6 ----------------
 dict(k='text', ch='Chương 6 – Phiên thứ tư', cap=('9 GIỜ 15', 'LỆNH BÁN Ở KHẮP NƠI'), cols=CR, moc=True, anh=A(15),
      say=("Chín giờ mười lăm. Mã X mở cửa vẫn xanh. Rồi đến chín giờ ba mươi, có những lệnh bán khối lượng rất lớn xuất hiện ở bên bán, mỗi lệnh vài trăm nghìn cổ phiếu. "
           "Giá bắt đầu trượt. Từ xanh về tham chiếu. Từ tham chiếu xuống đỏ. Đến mười giờ, mã X nằm sàn, trắng bên mua. "
           "Không ai mua nữa. Hàng triệu cổ phiếu treo bán ở giá sàn mà không khớp được một cổ nào.")),
 dict(k='text', cap=('"RŨ HÀNG ĐẤY"', '"TAY TO ĐANG GOM LẠI"'), cols=CR, anh=A(16),
      say=("Bạn nhắn vào nhóm, tay run. Thầy Phong trả lời sau đúng mười phút. Bình tĩnh. Đây là rũ hàng. Tay to đang ép giá để gom lại ở vùng thấp. Ai giữ chặt sẽ được thưởng. "
           "Chị Lan Anh viết: em vừa mua thêm, cơ hội trời cho. Anh Hùng viết: ai bán bây giờ là dại. "
           "Một tài khoản lạ viết: hình như nhóm xả hàng rồi mọi người ơi. Ba phút sau, tài khoản đó bị mời ra khỏi nhóm.")),
 dict(k='bars', cap=('MÃ X', 'SAU 5 PHIÊN GIẢM SÀN'), cols=CR, moc=True,
      bars=[('Đỉnh', 123, GOLD, '123'), ('Sàn 1', 114, RED, '−7%'), ('Sàn 2', 106, RED, '−14%'), ('Sàn 3', 99, RED, '−20%'), ('Sàn 5', 85, RED, '−31%')],
      say=("Mã X giảm sàn năm phiên liên tiếp. Từ đỉnh 123, giá về quanh 85, mất khoảng 31 phần trăm. Tính từ giá bạn mua, bạn lỗ khoảng 15 phần trăm, mà mỗi ngày bán không được. "
           "Đến ngày thứ sáu, khi bạn bán được những cổ phiếu đầu tiên, tài khoản 610 triệu chỉ còn khoảng 380 triệu, và vẫn đang tiếp tục rơi. "
           "Đây chính là kịch bản trong vụ CMS: nhóm gom hàng, hô hào cho đám đông mua, đẩy giá lên, rồi bán ra một lượng rất lớn ở đỉnh.")),
 dict(k='cards', cap=('VỤ CMS', 'HÀ NỘI, KHỞI TỐ 15/8/2024'), cols=CR, moc=True, anh=A(17),
      cards=[('7 bị can', 'thao túng giá cổ phiếu CMS', ''), ('> 10 tỷ', 'thu lợi bất chính, theo xác minh ban đầu', ''), ('Zalo, Telegram', 'hô hào, xoá thành viên nói ngược', '')],
      say=("Theo cơ quan công an, từ tháng 5 đến tháng 10 năm 2023, nhóm này dùng nhiều tài khoản để gom cổ phiếu CMS. Họ lập các nhóm Zalo, Telegram hô hào thành viên giao dịch. "
           "Người cầm đầu còn chỉ đạo xoá những thành viên đăng thông tin tiêu cực, gây cản trở việc đẩy giá. "
           "Đến tháng 9 năm 2023, khi giá lên đỉnh, nhóm bán ra lượng lớn, thu lợi bất chính hơn mười tỷ đồng. "
           "Ngày 15 tháng 8 năm 2024, công an Hà Nội khởi tố bảy bị can. Còn những người đã mua theo lời hô hào thì chịu thua lỗ.")),
 # ---------------- CHƯƠNG 7 ----------------
 dict(k='text', ch='Chương 7 – Nhóm biến mất', cap=('"NHÓM NÀY ĐÃ', 'BỊ GIẢI TÁN"'), cols=CR, moc=True, anh=A(18),
      say=("Sáng thứ Hai tuần sau, bạn mở Zalo. Phòng VIP Kim Cương không còn nữa. Chỉ có một dòng chữ xám: nhóm này đã bị giải tán. "
           "Bạn nhắn cho Thư. Tin nhắn gửi đi, nhưng không bao giờ hiện chữ đã xem. Trang Facebook của thầy Phong vẫn còn, nhưng đã đổi tên, đổi ảnh bìa, và đang chạy quảng cáo cho một nhóm mới: Cộng Đồng Nhà Đầu Tư Thịnh Vượng. "
           "Ảnh lãi trong quảng cáo mới, bạn nhận ra, chính là ảnh chị Lan Anh từng khoe.")),
 dict(k='text', cap=('BẠN CHƯA NÓI', 'VỚI VỢ'), cols=CC, anh=A(19),
      say=("Bạn không dám nói với Hà. Tối nào về nhà cũng cười, cũng hỏi con đạp có mạnh không, rồi nằm quay mặt vào tường, mở bảng giá xem đi xem lại. "
           "Bạn tự nhủ: chỉ cần gỡ lại được 200 triệu của mẹ vợ là được. Phần của mình thì từ từ tính. "
           "Và đúng lúc bạn đang tuyệt vọng nhất, điện thoại sáng lên. Một số lạ. Giọng con gái, ngọt và rất quen. Anh ơi, em là Thư đây.")),
 # ---------------- CHƯƠNG 8 ----------------
 dict(k='text', ch='Chương 8 – Phòng gỡ lỗ', cap=('"EM SẼ GIÚP ANH', 'GỠ LẠI"'), cols=CR, moc=True, anh=A(20),
      say=("Thư khóc. Thư bảo thầy Phong là người xấu, Thư cũng bị lừa, bị nợ lương, và đã nghỉ việc. Thư thấy có lỗi với anh nhất. "
           "Giờ Thư làm cho một sàn đầu tư quốc tế, có giấy phép ở nước ngoài, giao dịch đòn bẩy, hai chiều lên xuống đều kiếm được tiền. "
           "Bên em có phòng gỡ lỗ riêng cho người từng bị lừa, anh ạ. Chuyên gia bên này là người nước ngoài, làm thật. Em chỉ muốn chuộc lỗi thôi. "
           "Bạn biết là có gì đó không ổn. Nhưng người đang chết đuối thì với cả vào cọng rơm.")),
 dict(k='bignum', cap=('TÀI KHOẢN TRÊN SÀN', 'SAU 2 TUẦN'), cols=CC, value=61, fmt='+{:,.0f}', unit='%', top='NẠP 100 TRIỆU', sub='con số chỉ nằm trên màn hình', col=GREEN, anh2=A(21),
      say=("Bạn tải một ứng dụng qua đường link Thư gửi, không có trên kho ứng dụng. Bạn chuyển 100 triệu qua một mã QR, vào một tài khoản cá nhân mang tên lạ. "
           "Hai tuần sau, màn hình báo bạn lãi 61 phần trăm. 100 triệu thành 161 triệu. Bạn rút thử ba triệu, được ngay. Bạn sướng run người. "
           "Bạn nạp thêm 150 triệu, trong đó 90 triệu là tiền vay từ hai ứng dụng cho vay trên điện thoại. Tài khoản trên màn hình nhảy lên hơn nửa tỷ.")),
 dict(k='cards', cap=('MUỐN RÚT TIỀN?', 'NỘP THÊM PHÍ'), cols=CR, moc=True, anh=A(22),
      cards=[('20%', '"thuế thu nhập" phải nộp trước khi rút', ''), ('"Sai lệnh"', 'tài khoản bị đóng băng', ''), ('50 triệu', '"phí xác minh" để mở khoá', '')],
      say=("Rồi bạn bấm rút toàn bộ. Màn hình báo: để rút, quý khách cần nộp trước hai mươi phần trăm thuế thu nhập. Bạn gom nốt tiền tiết kiệm, nộp thêm 85 triệu. "
           "Hôm sau tài khoản bị đóng băng vì quý khách đặt sai lệnh, vi phạm quy định sàn. Muốn mở khoá, nộp 50 triệu phí xác minh. "
           "Bạn gọi cho Thư. Số máy không liên lạc được. Bạn mở lại ứng dụng. Ứng dụng không vào được nữa.")),
 dict(k='cards', cap=('SÀN ẢO', 'CÓ THẬT Ở NGOÀI ĐỜI'), cols=CR, moc=True, anh=A(23),
      cards=[('> 200 tỷ', 'sàn Fnory.com, Thanh Hoá, 2/2025', ''), ('112 điện thoại', 'sàn "chứng khoán ảo", TP.HCM, 11/2026', ''), ('Lãi ảo', 'rồi khoá lệnh, chiếm đoạt', '')],
      say=("Đây cũng không phải chuyện tưởng tượng. Tháng 2 năm 2025, công an Thanh Hoá bắt tạm giam chín bị can trong vụ sàn Fnory, chiếm đoạt hơn 200 tỷ đồng. "
           "Nhân viên đóng vai chuyên gia tài chính, đưa khách vào nhóm kín, hô lệnh mua bán cho đến khi khách mất hết tiền. "
           "Mới đây, công an TP.HCM công bố phát hiện 14 người nước ngoài trong một căn nhà kín cổng cao tường, với 29 máy tính và 112 điện thoại. Họ bị nghi lập sàn chứng khoán ảo. "
           "Theo cơ quan công an, họ cho màn hình hiện lợi nhuận tăng vọt để nạn nhân nạp thêm, rồi khoá lệnh và chiếm đoạt toàn bộ.")),
 # ---------------- CHƯƠNG 9 ----------------
 dict(k='text', ch='Chương 9 – Ba thông báo lúc nửa đêm', cap=('THÔNG BÁO', 'THỨ NHẤT'), cols=CR, moc=True, anh=A(24),
      say=("Mười một giờ đêm, Hà đã ngủ. Bạn ngồi ngoài ban công, điện thoại sáng lên ba thông báo liền nhau. "
           "Thông báo thứ nhất, từ ứng dụng cho vay: khoản vay của quý khách đã quá hạn bảy ngày. Chúng tôi sẽ liên hệ những người trong danh bạ của quý khách. "
           "Trong danh bạ đó có sếp của bạn, có bố mẹ bạn, và có mẹ vợ.")),
 dict(k='text', cap=('THÔNG BÁO', 'THỨ HAI VÀ THỨ BA'), cols=CR, anh=A(25),
      say=("Thông báo thứ hai, từ thằng Tùng: mày ơi, tao cũng mất hết rồi, nhóm của thầy Phong là lừa đảo. Thì ra ảnh lãi ba mươi phần trăm hôm nào cũng chỉ là ảnh lãi trên giấy. "
           "Thông báo thứ ba, từ mẹ vợ: con ơi, mẹ hỏi chút, tiền mẹ chuyển hai đứa để mua nhà, con gửi tiết kiệm ở ngân hàng nào, mẹ muốn chuyển thêm cho đủ kỳ hạn. "
           "Bạn nhìn ba tin nhắn rất lâu. Rồi bạn bước vào phòng, nhìn Hà đang ngủ, tay đặt lên bụng.")),
 dict(k='bignum', cap=('SAU BA THÁNG', 'BẠN ĐÃ MẤT'), cols=CR, value=470, fmt='{:,.0f}', unit=' triệu', top='PHÍ VIP + LỖ MÃ X + NẠP SÀN ẢO', sub='trong đó 90 triệu là tiền vay', col=RED,
      say=("Cộng lại sau ba tháng: mười lăm triệu tiền phí phòng VIP. Khoảng một trăm hai mươi triệu lỗ ở mã X. Ba trăm ba mươi lăm triệu nạp vào sàn ảo, trừ đi ba triệu rút được hôm đầu. "
           "Tổng cộng khoảng bốn trăm bảy mươi triệu đồng. Năm trăm triệu tiền mua nhà giờ chỉ còn khoảng một trăm ba mươi lăm triệu, cộng thêm 90 triệu nợ ứng dụng cho vay, đang lãi chồng lãi. "
           "Và điều tệ nhất: tất cả những người bạn gặp trên hành trình đó, thầy Phong, chị Lan Anh, anh Hùng, Thư, đều có thể chưa từng tồn tại.")),
 # ---------------- CHƯƠNG 10 ----------------
 dict(k='text', ch='Chương 10 – Vì sao người cẩn thận vẫn sập bẫy', cap=('KHÔNG PHẢI VÌ NGU', 'MÀ VÌ BỊ DẪN TỪNG BƯỚC'), cols=CC, moc=True, anh=A(26),
      say=("Bạn không ngu. Bạn là người tính toán từng đồng tiền điện. Nhưng nhóm phím hàng không lừa bạn bằng một cú lớn. Họ dẫn bạn từng bước nhỏ, bước nào cũng có vẻ hợp lý. "
           "Miễn phí trước, để bạn hết đề phòng. Cho bạn thắng nhỏ, để bạn tin. Tạo đám đông giả, để bạn thấy mình không cô đơn. Thu phí, để bạn tiếc tiền mà ở lại. "
           "Đặt luật cấm bán, để bạn ngồi yên khi họ bán. Và cuối cùng, phòng gỡ lỗ, để lấy nốt những đồng cuối cùng của người đang tuyệt vọng.")),
 dict(k='checklist', cap=('6 DẤU HIỆU', 'NHÓM PHÍM HÀNG LỪA ĐẢO'), cols=CR, moc=True,
      items=[('Hứa tỷ lệ thắng, hứa lãi gấp đôi', RED), ('Ảnh lãi, lời cảm ơn dày đặc', RED), ('Thúc giục: còn 5 suất, hết hạn tối nay', RED), ('Cấm bán khi chưa có lệnh, xoá người nói ngược', RED), ('Chuyển tiền vào tài khoản cá nhân, app ngoài kho', RED), ('"Phòng gỡ lỗ" sau khi bạn vừa mất tiền', RED)],
      say=("Nếu chỉ nhớ một phần của video này, hãy nhớ sáu dấu hiệu. Một, hứa tỷ lệ thắng, hứa lãi gấp đôi. Không ai làm được điều đó đều đặn. "
           "Hai, ảnh lãi và lời cảm ơn dày đặc. Ba, thúc giục: chỉ còn năm suất, hết hạn tối nay. "
           "Bốn, cấm bán khi chưa có lệnh, và xoá người nói ngược. Năm, bảo bạn chuyển tiền vào tài khoản cá nhân hoặc tải ứng dụng ngoài kho chính thức. "
           "Sáu, ai đó tìm đến đúng lúc bạn vừa mất tiền, hứa giúp bạn gỡ lại. Gặp một dấu hiệu, hãy dừng lại. Gặp hai dấu hiệu, hãy rời đi.")),
 dict(k='text', cap=('TIỀN CỦA BẠN', 'CHỈ NÊN ĐI MỘT ĐƯỜNG'), cols=CC, anh=A(27),
      say=("Và một điều nữa: khi đầu tư chứng khoán thật, tiền của bạn chỉ đi từ ngân hàng của bạn vào tài khoản đứng tên chính bạn ở một công ty chứng khoán được cấp phép. "
           "Không có trợ lý nào cần bạn chuyển tiền vào tài khoản cá nhân. Không có sàn hợp pháp nào bắt nộp thuế trước mới cho rút tiền. "
           "Trước khi mua bất kỳ mã nào ai đó hô, hãy tự mở báo cáo tài chính của nó ra xem doanh nghiệp đó có thật sự làm ra lợi nhuận không. "
           "Nếu cần một chỗ tra nhanh P/E, lợi nhuận, biên lãi của hơn 400 mã, bạn có thể xem miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='text', ch='Kết – Thứ nhóm phím hàng không bao giờ phím', cap=('THỨ HỌ', 'KHÔNG BAO GIỜ PHÍM'), cols=CC, moc=True, anh=A(28),
      say=("Sáng hôm sau, bạn ngồi xuống cạnh Hà, đưa cho vợ xem toàn bộ tin nhắn, toàn bộ sao kê. Hà im lặng rất lâu. Rồi Hà hỏi một câu: thế anh còn nợ ai nữa không? "
           "Bạn mất bảy năm để gom 300 triệu, và ba tháng để mất gần năm trăm triệu. Nhưng bạn vẫn còn một người ngồi cạnh, và một đứa con sắp chào đời. "
           "Nhóm phím hàng phím cho bạn đủ thứ: mã tăng trần, mục tiêu gấp đôi, tay to đứng sau. "
           "Chỉ có một thứ họ không bao giờ phím: lúc nào thì chính họ bán.")),
 dict(k='end', cap=('BẠN ĐÃ TỪNG', 'VÀO NHÓM PHÍM HÀNG CHƯA?'), cols=CC,
      say=("Bạn đã từng được mời vào nhóm phím hàng chưa? Họ dùng câu gì để mời bạn? Kể cho mọi người cùng biết ở phần bình luận nhé, biết đâu bình luận của bạn cứu được tiền của một người khác. "
           "Tập sau: vì sao thật tệ khi gửi tiết kiệm cả đời.")),
]

# ---- hình từng cảnh: điện thoại (chat/noti) cho phần nhóm chat, ảnh thật Commons cho bối cảnh ----
R_, V_, X_ = (239, 68, 68), (255, 196, 0), (56, 189, 248)
NHOM = 'Cộng Đồng Đầu Tư Thông Minh'; VIP = 'Phòng VIP Kim Cương'
OV = {
 1: dict(k='noti', noti=dict(gio='06:02', ngay='Thứ Hai', items=[
        ('Nhóm chat', VIP, 'Thầy Phong: 9 giờ 15 vào lệnh. Anh em chuẩn bị tiền, tỷ trọng tối đa.', V_),
        ('Nhóm chat', VIP, 'Lan Anh: Em sẵn sàng rồi thầy ơi!!!', V_)])),
 2: dict(k='chat', chat=dict(ten=VIP, tv='312 thành viên', gio='06:05', msgs=[
        ('Lan Anh', 'Tháng này em lãi 40 triệu, cảm ơn thầy ạ', 'lai', '+40.150.000'),
        ('Hùng', 'Vừa đặt cọc xe mới nhờ thầy. Tạ ơn thầy'),
        ('Cô Mai', 'Cô về hưu rồi, nhờ thầy mà trả hết nợ cho con'),
        ('Thầy Phong', 'Kỷ luật là chiến thắng. 9h15 vào lệnh.')])),
 3: dict(anh='Ho Chi Minh City skyline'),
 4: dict(anh='Ho Chi Minh City apartments'), 5: dict(anh='Com tam'), 6: dict(anh='smartphone'),
 7: dict(k='chat', chat=dict(ten='Thư – Trợ lý thầy Phong', tv='Đang hoạt động', gio='22:41', mau=(255, 120, 160), msgs=[
        ('Thư', 'Anh ơi, em là Thư bên đội ngũ của thầy Phong ạ'),
        ('Thư', 'Anh đầu tư lâu chưa ạ?'), ('me', 'Anh mới tìm hiểu thôi em'),
        ('Thư', 'Dạ không sao đâu anh, người mới lại càng dễ thành công'),
        ('Thư', 'Em mời anh vào nhóm miễn phí nhé. Tuần này thầy chỉ nhận thêm 50 người thôi ạ')])),
 8: dict(k='chat', chat=dict(ten=NHOM, tv='2.148 thành viên', gio='20:03', msgs=[
        ('Lan Anh', 'Tài khoản em lãi 38% rồi, em cảm ơn thầy', 'lai', '+38,2%'),
        ('Hùng', 'Cả đời chưa thấy ai phím chuẩn như thầy'),
        ('Minh Châu', 'Thầy cho em xin vào phòng VIP với ạ'),
        ('*', 'Thư đã thêm bạn vào nhóm'), ('me', 'Chào mọi người, em mới vào ạ'),
        ('Lan Anh', 'Chào em, làm theo thầy là thắng nhé')])),
 9: dict(anh='warehouse'), 10: dict(anh='marionette'),
 11: dict(k='chat', chat=dict(ten='Thư – Trợ lý thầy Phong', tv='Đang hoạt động', gio='23:58', mau=(255, 120, 160), msgs=[
        ('Thư', 'Anh ơi chỉ còn 2 suất thôi, 12 giờ là em đóng danh sách ạ'),
        ('me', 'Anh chuyển rồi em nhé'),
        ('*', 'Bạn đã chuyển 15.000.000 đ'),
        ('Thư', 'Chúc mừng anh đã bước vào thế giới của người chiến thắng ♥')])),
 12: dict(anh='marionette'),
 13: dict(k='chat', chat=dict(ten=VIP, tv='312 thành viên', gio='08:45', msgs=[
        ('Thầy Phong', 'MÃ X. Hàng có thông tin. Vùng mua quanh tham chiếu. Tỷ trọng tối đa. Mục tiêu x2.'),
        ('Hùng', 'Đã vào full thầy ơi'), ('Lan Anh', 'Em bán hết mã cũ để vào X rồi ạ'),
        ('me', 'Em vào 500 triệu rồi thầy')])),
 14: dict(k='chat', chat=dict(ten='Thư – Trợ lý thầy Phong', tv='Đang hoạt động', gio='09:02', mau=(255, 120, 160), msgs=[
        ('me', 'Em ơi anh muốn chốt lời được không, lãi 110 triệu rồi'),
        ('Thư', 'Anh ơi thầy chưa có lệnh ạ'),
        ('Thư', 'Mục tiêu x2, giờ mới đi được 1/5 chặng thôi anh. Bán bây giờ là bán non đó ạ')])),
 15: dict(anh='File:Sở GDCK TPHCM (HOSE).JPG'),
 16: dict(k='chat', chat=dict(ten=VIP, tv='312 thành viên', gio='10:14', msgs=[
        ('me', 'Thầy ơi mã X nằm sàn rồi, sao bán không được ạ?'),
        ('Thầy Phong', 'Bình tĩnh. Đây là rũ hàng. Tay to ép giá để gom lại. Ai giữ chặt sẽ được thưởng.'),
        ('Lan Anh', 'Em vừa mua thêm, cơ hội trời cho'), ('Hùng', 'Ai bán bây giờ là dại'),
        ('Minh Tuấn', 'Hình như nhóm xả hàng rồi mọi người ơi'),
        ('*', 'Thư đã mời Minh Tuấn ra khỏi nhóm')])),
 17: dict(anh='Hanoi skyline'),
 18: dict(k='chat', chat=dict(ten=VIP, tv='Nhóm không còn hoạt động', gio='07:30', mau=(120, 128, 146), msgs=[
        ('Thầy Phong', 'Kỷ luật là chiến thắng.'),
        ('*', 'Nhóm này đã bị giải tán'),
        ('*', 'Bạn không thể gửi tin nhắn vào nhóm này')])),
 19: dict(anh='Ho Chi Minh City apartments'),
 20: dict(k='chat', chat=dict(ten='Số lạ', tv='Cuộc gọi thoại · 14 phút', gio='22:17', mau=(255, 120, 160), msgs=[
        ('Thư', 'Anh ơi em xin lỗi, em cũng bị thầy Phong lừa'),
        ('Thư', 'Giờ em làm cho sàn quốc tế, có phòng gỡ lỗ riêng cho người từng bị lừa'),
        ('Thư', 'Em chỉ muốn chuộc lỗi thôi anh'), ('me', 'Thật không em?')])),
 22: dict(k='noti', noti=dict(gio='14:26', ngay='Thứ Sáu', items=[
        ('Sàn đầu tư', 'Yêu cầu rút tiền đang chờ', 'Quý khách cần nộp trước 20% thuế thu nhập để hoàn tất rút tiền.', R_),
        ('Sàn đầu tư', 'Tài khoản bị đóng băng', 'Phát hiện lệnh sai quy định. Nộp phí xác minh 50.000.000 đ để mở khoá.', R_),
        ('Điện thoại', 'Thư', 'Thuê bao quý khách vừa gọi tạm thời không liên lạc được.', (120, 128, 146))])),
 23: dict(anh='Ho Chi Minh City skyline'),
 24: dict(k='noti', noti=dict(gio='23:04', ngay='Thứ Năm', items=[
        ('Vay nhanh', 'Khoản vay quá hạn 7 ngày', 'Chúng tôi sẽ liên hệ những người trong danh bạ của quý khách.', R_)])),
 25: dict(k='noti', noti=dict(gio='23:05', ngay='Thứ Năm', co_san=1, items=[
        ('Vay nhanh', 'Khoản vay quá hạn 7 ngày', 'Chúng tôi sẽ liên hệ những người trong danh bạ của quý khách.', R_),
        ('Tin nhắn', 'Tùng', 'Mày ơi, tao cũng mất hết rồi. Nhóm của thầy Phong là lừa đảo.', X_),
        ('Tin nhắn', 'Mẹ vợ', 'Con ơi, tiền mẹ chuyển hai đứa mua nhà, con gửi tiết kiệm ngân hàng nào?', (34, 197, 94))])),
 26: dict(anh='staircase'), 27: dict(anh='File:Sở GDCK TPHCM (HOSE).JPG'), 28: dict(anh='Saigon river'),
}
for c in S:
    for key_ in ('anh', 'anh2'):
        a_ = c.get(key_, '')
        if isinstance(a_, str) and a_.startswith('repo:'):
            n_ = int(a_[-6:-4]); o_ = OV.get(n_, {})
            if key_ == 'anh2': c[key_] = o_.get('anh', 'Saigon night'); continue
            if 'k' in o_ and c['k'] in ('text', 'hook'): c.update(o_); c.pop('anh', None)
            elif 'k' in o_: c['anh'] = 'Saigon night'
            else: c['anh'] = o_.get('anh', 'Saigon night')
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Vì Sao Thật Tệ Khi Vào Nhóm Phím Hàng | 3 Phiên Tăng Trần, Rồi Nhóm Biến Mất'
MT = ("Bạn 31 tuổi, có 500 triệu tiền mua nhà. Một quảng cáo \"chuyên gia 15 năm, tặng 3 mã miễn phí\" dẫn bạn vào nhóm Zalo 2.148 thành viên, phòng VIP 15 triệu/tháng, mã X ba phiên tăng trần… rồi năm phiên giảm sàn, nhóm giải tán, và \"phòng gỡ lỗ\" trên một sàn ảo.\n\n"
      "Câu chuyện giả định, nhưng từng thủ đoạn lấy từ các vụ án có thật:\n"
      "• Thao túng cổ phiếu CMS qua nhóm Zalo/Telegram – Công an Hà Nội khởi tố 7 bị can ngày 15/8/2024 (VietnamBiz/An ninh Thủ đô 30/8/2024)\n"
      "• Sàn Fnory.com, hơn 200 tỷ đồng, 9 bị can – Công an Thanh Hoá (Tuổi Trẻ 12/2/2025)\n"
      "• Mạo danh công ty chứng khoán lập nhóm Zalo, tài khoản chân gỗ khoe lãi – UBCKNN cảnh báo (An ninh Thủ đô 23/2/2024)\n"
      "• Nghi lập sàn chứng khoán ảo, 14 người nước ngoài, 112 điện thoại – Công an TP.HCM (Thanh Niên 9/11/2026)\n\n"
      "6 dấu hiệu nhóm phím hàng lừa đảo ở chương 10.\n\n"
      "Tra P/E, lợi nhuận, biên lãi 400+ mã miễn phí: https://chungkhoanhuynguyen.com\nKênh chính: https://www.youtube.com/@chungkhoanhuynguyen\n\n"
      "Mã X là tên giả định, không ám chỉ cổ phiếu nào. Nhân vật là hư cấu. Ảnh minh hoạ tạo bằng AI.\nChia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen5', seri='Vì sao thật tệ khi…', ngay='2026-11-14', gio_goi_y='20:00', gio='20:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['nhóm phím hàng', 'lừa đảo chứng khoán', 'nhóm zalo chứng khoán', 'phím hàng', 'thao túng cổ phiếu', 'sàn ảo', 'F0 chứng khoán', 'vì sao thật tệ khi'],
    bia_hook=['3 PHIÊN TRẦN', 'RỒI NHÓM BIẾN MẤT'], badge='VÌ SAO THẬT TỆ KHI…',
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh phụ @chungkhoanhuynguyen5 – tập 2 'Vì sao thật tệ khi vào nhóm phím hàng' (QL1 10/11/2026).\n"
    "XH_BAN = True; NO_CTA = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
print('so chu', lib.dem(S), 'canh', len(S), 'anh', sorted({c.get('anh') or c.get('anh2') for c in S if (c.get('anh') or c.get('anh2') or '').startswith('repo:')}).__len__(), len(TIEU))
