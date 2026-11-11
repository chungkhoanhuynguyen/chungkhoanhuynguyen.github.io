# -*- coding: utf-8 -*-
# QL1 11/11/2026 – VIDEO DÀI kênh chính, khuôn kể chuyện: "Lãi tăng 888% mà cổ phiếu vẫn giảm – vì sao?" (BSR, POW, PGV đối chiếu MSR).
# Nguồn (WiData 11/11/2026):
#  - BCTC hợp nhất, LNST cổ đông công ty mẹ (tỷ đồng): BSR Q3/25 908 · Q4/25 3.062 · Q1/26 8.265 · Q2/26 7.666 · Q3/26 8.968;
#    MSR Q3/25 5 · Q4/25 222 · Q1/26 537 · Q2/26 1.666 · Q3/26 2.148; POW Q3/26 1.860 (+129,8%), 9T 6.434 (605,7% KH); PGV Q3/26 1.221 (+638%).
#  - Tin KQKD (ai_news 30/10, 2/11/2026): BSR 9T 24.899 tỷ (+1.057%), 1.151,7% kế hoạch năm, 106,1% dự phóng CTCK 2026 (23.460 tỷ).
#  - Giá đã điều chỉnh 22/5 → 11/11/2026: BSR 29.370 → 25.300 (−13,9%); MSR 37.620 → 58.700 (+56%); POW 13.600 → 12.700; PGV 20.770 → 20.700.
#  - P/E theo phiên 11/11/2026: BSR 4,5; POW 5,6; PGV 4,2; MSR 14,2.
#  - Dòng vốn kinh doanh 11/11/2026 (VNDirect Research): LN quý 3 DN HOSE +52%, đóng góp đột biến từ VIC, VHM, BSR; dự báo quý 4 chỉ tăng khoảng 6%.
#  - MarketTimes 10/11/2026 (MetalMiner): APT Rotterdam 278,22 USD/kg tháng 10/2026, gấp 3,74 lần giá xuất xưởng Trung Quốc 74,43 USD/kg; 9/2021–6/2025 bình quân 1,24 lần;
#    Trung Quốc cấp phép xuất khẩu từ 2/2025; Elmet (Mỹ) thành cổ đông MSR tháng 10; Sojitz (Nhật) ký MOU 9/11 dự kiến mua 5% MSR.
import os, sys, json
sys.path.insert(0, os.path.dirname(__file__)); import lib
from lib import GOLD, RED, GREEN, BLUE, WHITE
CW = os.environ.get('CW', '/tmp/cw')
LO = CW + '/_video/queue/20261111_1700'
KEY = 'CH1511LKL'; CC = (WHITE, GOLD); CR = (WHITE, RED)
R_, V_, X_, G_ = (239, 68, 68), (255, 196, 0), (56, 189, 248), (34, 197, 94)
TU = 'Anh Tú'; QUAN = 'Quân'
S = [
 # ---------------- MỞ ĐẦU ----------------
 dict(k='noti', ch='Mở đầu', cap=('LÃI TĂNG 888%', 'CỔ PHIẾU VẪN GIẢM'), cols=CR, noti=dict(gio='21:30', ngay='Thứ Sáu', items=[
        ('Tin tức', 'Kết quả kinh doanh', 'BSR: lợi nhuận quý 3/2026 đạt 8.968 tỷ, tăng 888% so với cùng kỳ', G_),
        ('Chứng khoán', 'Ứng dụng giao dịch', 'Danh mục: BSR −13,9%. Lãi/lỗ: −55.000.000đ', R_)]),
      say=("Tối ba mươi tháng mười, điện thoại anh Tú rung hai lần liền. Tin thứ nhất: Lọc hóa dầu Bình Sơn báo lãi quý ba gần chín nghìn tỷ đồng, tăng tám trăm tám mươi tám phần trăm so với cùng kỳ. "
           "Tin thứ hai, từ chính ứng dụng chứng khoán của anh: cổ phiếu BSR trong danh mục đang lỗ gần mười bốn phần trăm. Công ty lãi kỷ lục, mà người cầm cổ phiếu lại đang mất tiền. Chuyện này là sao?")),
 dict(k='bignum', anh='ov:oil refinery||oil refinery', cap=('BSR: LÃI 9 THÁNG 2026', 'GẤP 11,5 LẦN KẾ HOẠCH NĂM'), cols=CC, value=24899, fmt='{:,.0f}', unit=' tỷ', top='LỢI NHUẬN 9 THÁNG – TĂNG 1.057%', sub='Cùng lúc giá cổ phiếu giảm gần 14% từ cuối tháng 5', col=GOLD,
      say=("Con số không hề nhỏ. Chín tháng đầu năm 2026, BSR lãi hai mươi bốn nghìn tám trăm chín mươi chín tỷ đồng, gấp mười một lần rưỡi kế hoạch cả năm mà chính công ty đặt ra. "
           "Vậy mà từ cuối tháng năm đến nay, cổ phiếu từ khoảng hai mươi chín nghìn bốn trăm đồng còn hai mươi lăm nghìn ba trăm. "
           "Hôm nay em kể câu chuyện của anh Tú để trả lời một câu hỏi mà rất nhiều nhà đầu tư đang thắc mắc: vì sao có những công ty lãi kỷ lục mà cổ phiếu không tăng, còn có công ty lại tăng hơn năm mươi phần trăm?")),
 # ---------------- CHƯƠNG 1 ----------------
 dict(k='chat', ch='Chương 1 – Hai người bạn, hai lựa chọn', cap=('"LÃI GẤP 20 LẦN', 'MÀ P/E CÓ 4"'), cols=CC, moc=True, chat=dict(ten=QUAN, tv='Đang hoạt động', gio='20:10', mau=X_, msgs=[
        ('me', 'BSR quý 1 lãi hơn 8.200 tỷ, gấp 20 lần cùng kỳ mày ạ'),
        ('me', 'P/E có hơn 4, rẻ như cho, tao vào 400 triệu'),
        ('Quân', 'Tao thì đang để ý MSR, giá vonfram đang sốt'),
        ('me', 'MSR P/E cao hơn nhiều, mua đắt làm gì')]),
      say=("Quay lại cuối tháng năm. Anh Tú, kỹ sư cơ khí ba mươi tư tuổi, nhắn cho Quân, bạn thân thời đại học. BSR quý một lãi hơn tám nghìn hai trăm tỷ, gấp hai mươi lần cùng kỳ mày ạ. P trên E có hơn bốn, rẻ như cho, tao vào bốn trăm triệu. "
           "Quân trả lời: tao thì đang để ý MSR, Masan High-Tech Materials, giá vonfram đang sốt. Anh Tú gạt đi: MSR P trên E cao hơn nhiều, mua đắt làm gì.")),
 dict(k='cards', anh='ov:stock market screen||stock trading', cap=('CUỐI THÁNG 5/2026', 'HAI LỰA CHỌN'), cols=CC, moc=True,
      cards=[('BSR', '400 triệu – giá khoảng 29.400', 'lãi tăng gấp 20 lần'), ('MSR', '200 triệu – giá khoảng 37.600', 'lãi mới bắt đầu tăng'), ('T5/2026', 'Cùng một ngày mua', 'hai lựa chọn')],
      say=("Cùng một tuần, hai người bạn đưa ra hai lựa chọn. Anh Tú dồn bốn trăm triệu vào BSR, giá khoảng hai mươi chín nghìn bốn trăm đồng, một công ty mà lợi nhuận vừa tăng gấp hai mươi lần. "
           "Quân bỏ hai trăm triệu vào MSR, giá khoảng ba mươi bảy nghìn sáu trăm. Lợi nhuận của MSR lúc đó mới bắt đầu nhích lên sau nhiều năm thua lỗ. Theo logic thông thường, anh Tú đã chọn đúng: rẻ hơn, lãi nhiều hơn.")),
 # ---------------- CHƯƠNG 2 ----------------
 dict(k='noti', ch='Chương 2 – Sáu tháng sau', cap=('SÁU THÁNG SAU', 'AI ĐÚNG?'), cols=CR, moc=True, noti=dict(gio='15:00', ngay='Thứ Tư', items=[
        ('Chứng khoán', 'Ứng dụng giao dịch', 'BSR 25.300 (−13,9%). MSR 58.700 (+56%)', V_),
        ('Zalo', QUAN, 'MSR lãi hơn trăm triệu rồi mày ơi', G_)]),
      say=("Sáu tháng sau, phiên mười một tháng mười một. BSR đóng cửa hai mươi lăm nghìn ba trăm đồng, giảm gần mười bốn phần trăm. Bốn trăm triệu của anh Tú còn khoảng ba trăm bốn mươi lăm triệu. "
           "MSR đóng cửa năm mươi tám nghìn bảy trăm, tăng năm mươi sáu phần trăm. Hai trăm triệu của Quân thành hơn ba trăm mười triệu. Quân nhắn đúng một câu: MSR lãi hơn trăm triệu rồi mày ơi.")),
 dict(k='cards', anh='ov:power plant||oil refinery', cap=('LÃI QUÝ 3/2026 KỶ LỤC', 'GIÁ CỔ PHIẾU THÌ KHÔNG'), cols=CR, moc=True,
      cards=[('BSR +888%', 'lãi quý 3: 8.968 tỷ', 'giá 6 tháng −14%'), ('POW +130%', 'lãi quý 3: 1.860 tỷ', 'giá 6 tháng −7%'), ('PGV +638%', 'lãi quý 3: 1.221 tỷ', 'giá 6 tháng đi ngang')],
      say=("Và BSR không phải trường hợp duy nhất. Điện lực Dầu khí, mã POW, quý ba lãi một nghìn tám trăm sáu mươi tỷ, tăng một trăm ba mươi phần trăm, chín tháng đã vượt sáu lần kế hoạch năm. Cổ phiếu sáu tháng giảm khoảng bảy phần trăm. "
           "Phát điện ba, mã PGV, lãi quý ba tăng sáu trăm ba mươi tám phần trăm. Cổ phiếu đi ngang. Ba công ty lãi kỷ lục, P trên E chỉ bốn đến sáu lần, mà dòng tiền không mặn mà.")),
 dict(k='call', cap=('"THỊ TRƯỜNG', 'KHÔNG MUA QUÁ KHỨ"'), cols=CC, call=dict(ten='Chị Ngân', phu='Chuyên viên phân tích, bạn của Quân', mau=G_, loi=[
        'Thị trường không trả tiền cho lợi nhuận đã qua',
        'Nó trả tiền cho lợi nhuận của những năm tới']),
      say=("Không hiểu nổi, anh Tú nhờ Quân gọi cho chị Ngân, một chuyên viên phân tích. Chị Ngân nghe xong, nói một câu mà anh Tú nhớ mãi: thị trường không trả tiền cho lợi nhuận đã qua. Nó trả tiền cho lợi nhuận của những năm tới. "
           "Câu hỏi không phải là quý này lãi bao nhiêu. Câu hỏi là năm sau, năm sau nữa, công ty còn lãi được như vậy không.")),
 # ---------------- CHƯƠNG 3 ----------------
 dict(k='cards', ch='Chương 3 – P/E thấp có phải là rẻ?', anh='ov:oil refinery||oil tanker', cap=('LỢI NHUẬN BSR', 'TỪNG QUÝ'), cols=CC, moc=True,
      cards=[('908 tỷ', 'Quý 3/2025', ''), ('3.062 tỷ', 'Quý 4/2025', ''), ('8.968 tỷ', 'Quý 3/2026', 'Q1: 8.265 · Q2: 7.666')],
      say=("Chị Ngân mở báo cáo tài chính của BSR. Quý ba năm ngoái, lãi chín trăm lẻ tám tỷ. Quý bốn, ba nghìn không trăm sáu mươi hai tỷ. Ba quý năm nay, lần lượt tám nghìn hai trăm sáu mươi lăm, bảy nghìn sáu trăm sáu mươi sáu và tám nghìn chín trăm sáu mươi tám tỷ. "
           "Chị chỉ vào một dòng: kế hoạch năm của chính công ty chỉ khoảng hai nghìn một trăm tỷ. Tức là ban lãnh đạo cũng không coi mức lãi này là bình thường.")),
 dict(k='text', cap=('LÃI ĐẾN TỪ ĐÂU?', 'CHÊNH LỆCH GIÁ, KHÔNG PHẢI SẢN LƯỢNG'), cols=CC, anh='ov:oil refinery night||oil refinery',
      say=("Nhà máy lọc dầu kiếm tiền từ chênh lệch giữa giá xăng dầu thành phẩm và giá dầu thô. Khi chênh lệch này nới rộng, lợi nhuận tăng vọt dù sản lượng gần như không đổi. Khi nó thu hẹp lại, lợi nhuận cũng rơi nhanh như lúc tăng. "
           "Nhà máy không bán được gấp mười lần xăng dầu. Nó chỉ đang hưởng một giai đoạn biên lợi nhuận rất cao, do thị trường thế giới quyết định, không phải do riêng công ty tạo ra.")),
 dict(k='bignum', anh='ov:oil refinery night||oil refinery', cap=('P/E THẤP Ở ĐỈNH LỢI NHUẬN', 'CÓ THỂ LÀ CÁI BẪY'), cols=CR, value=4.5, fmt='{:,.1f}', unit=' lần', top='P/E CỦA BSR NGÀY 11/11/2026', sub='Tính trên lợi nhuận 4 quý gần nhất – quý cao nhất trong lịch sử', col=RED,
      say=("Đây là chỗ anh Tú hiểu sai. P trên E của BSR chỉ khoảng bốn phẩy năm lần, nhưng con số này được tính trên bốn quý lãi cao nhất lịch sử công ty. "
           "Nếu lợi nhuận năm sau chỉ còn một nửa, P trên E thật sẽ là chín lần. Nếu chỉ còn một phần tư, nó là mười tám lần. Với doanh nghiệp chu kỳ, P trên E thấp nhất thường xuất hiện đúng lúc lợi nhuận ở đỉnh, và đó lại thường là lúc rủi ro nhất để mua.")),
 dict(k='checklist', anh='ov:stock market screen||stock trading', cap=('THỊ TRƯỜNG ĐANG NGHĨ GÌ?', 'THEO VNDIRECT RESEARCH'), cols=CC,
      items=[('Quý 3/2026: lợi nhuận DN trên HOSE tăng 52%', GREEN), ('Phần đột biến chủ yếu từ VIC, VHM và BSR', GOLD), ('Dự báo quý 4: chỉ tăng khoảng 6%', RED)],
      say=("Không chỉ chị Ngân nghĩ vậy. Theo báo cáo chiến lược tháng mười một của VNDirect Research, lợi nhuận doanh nghiệp trên HOSE quý ba tăng năm mươi hai phần trăm, chủ yếu nhờ đóng góp đột biến từ VIC, VHM và BSR. "
           "Nhưng đà tăng được dự báo chậm lại rõ trong quý bốn, chỉ khoảng sáu phần trăm so với cùng kỳ. Thị trường đã nhìn thấy điều đó từ trước, và giá cổ phiếu phản ánh trước.")),
 # ---------------- CHƯƠNG 4 ----------------
 dict(k='bignum', ch='Chương 4 – Vì sao MSR khác?', anh='ov:tungsten||metal ore mining', cap=('GIÁ VONFRAM PHƯƠNG TÂY', 'GẤP 3,74 LẦN TRUNG QUỐC'), cols=CC, moc=True, value=278.22, fmt='{:,.2f}', unit=' USD/kg', top='GIÁ APT TẠI ROTTERDAM, THÁNG 10/2026', sub='Trung Quốc chỉ 74,43 USD/kg. Trước 6/2025 chênh bình quân 1,24 lần', col=GOLD,
      say=("Vậy tại sao MSR khác? Lợi nhuận MSR cũng tăng nhờ giá hàng hóa, nhưng là một loại giá rất đặc biệt. Theo MetalMiner, tháng mười năm 2026, giá vonfram trung gian tại Rotterdam, Hà Lan, là hai trăm bảy mươi tám đô la một ký, gấp ba phẩy bảy tư lần giá xuất xưởng ở Trung Quốc. "
           "Từ năm 2021 đến giữa năm 2025, chênh lệch này bình quân chỉ một phẩy hai tư lần. Thay đổi lớn đến từ tháng hai năm 2025, khi Trung Quốc bắt đầu cấp phép xuất khẩu, khiến phương Tây thiếu nguồn cung đạt chuẩn.")),
 dict(k='checklist', anh='ov:metal ore mining||mining', cap=('ĐIỀU THỊ TRƯỜNG THẤY Ở MSR', 'MÀ KHÔNG THẤY Ở NHÓM KIA'), cols=CC,
      items=[('Lợi thế đến từ thay đổi cấu trúc nguồn cung, không chỉ một chu kỳ giá', GREEN),
             ('Đối tác lớn tìm đến: Elmet (Mỹ) thành cổ đông, Sojitz (Nhật) ký ghi nhớ mua 5%', GREEN),
             ('Lợi nhuận vẫn đang tăng qua từng quý: 537 – 1.666 – 2.148 tỷ', GOLD)],
      say=("Đó là khác biệt cốt lõi. Biên lợi nhuận của MSR đến từ một thay đổi về cấu trúc nguồn cung thế giới, không chỉ là một nhịp lên xuống của giá. Và có những người sẵn sàng trả tiền để đặt cược vào điều đó: tháng mười, Elmet của Mỹ trở thành cổ đông MSR. "
           "Ngày chín tháng mười một, Sojitz của Nhật ký biên bản ghi nhớ, dự kiến mua năm phần trăm MSR. Trong khi lợi nhuận MSR vẫn đang leo dốc qua từng quý: năm trăm ba mươi bảy, một nghìn sáu trăm sáu mươi sáu, rồi hai nghìn một trăm bốn mươi tám tỷ đồng.")),
 dict(k='text', cap=('CHU KỲ VẪN LÀ CHU KỲ', 'KỂ CẢ VỚI MSR'), cols=CC, anh='ov:metal ore mining||mining',
      say=("Em nói công bằng: MSR cũng là doanh nghiệp hàng hóa. Nếu nguồn cung ngoài Trung Quốc tăng lên, hoặc chính sách xuất khẩu thay đổi, chênh lệch giá có thể thu hẹp, và cổ phiếu sẽ phản ứng rất mạnh. "
           "P trên E của MSR hiện khoảng mười bốn lần, đã phản ánh nhiều kỳ vọng. Bài học ở đây không phải là MSR tốt, BSR xấu. Bài học là: phải hiểu lợi nhuận đến từ đâu, và kéo dài được bao lâu.")),
 # ---------------- CHƯƠNG 5 ----------------
 dict(k='checklist', ch='Chương 5 – Ba câu hỏi trước khi mua theo lợi nhuận', anh='ov:stock market screen||stock trading', cap=('3 CÂU HỎI', 'TRƯỚC KHI MUA VÌ LÃI KỶ LỤC'), cols=CC, moc=True,
      items=[('Lãi tăng nhờ giá bán của thị trường, hay nhờ năng lực riêng của công ty?', GREEN),
             ('Điều tạo ra mức lãi này có thể kéo dài mấy năm? Ai có thể làm theo?', GREEN),
             ('P/E thấp vì cổ phiếu rẻ, hay vì lợi nhuận đang ở đỉnh?', GOLD)],
      say=("Sau cuộc gọi đó, anh Tú viết ra ba câu hỏi, dán ngay cạnh màn hình. Một: lãi tăng nhờ giá bán của thị trường, hay nhờ năng lực riêng của công ty? "
           "Hai: điều tạo ra mức lãi này có thể kéo dài mấy năm, và ai có thể làm theo? Ba: P trên E thấp vì cổ phiếu thật sự rẻ, hay vì lợi nhuận đang ở đỉnh? "
           "Anh chị có thể tra lợi nhuận từng quý, P trên E và kế hoạch năm của BSR, POW, PGV hay MSR miễn phí trên chứng khoán Huy Nguyễn chấm com.")),
 # ---------------- KẾT ----------------
 dict(k='chat', ch='Kết – Tin nhắn cuối', cap=('"LẦN SAU', 'TAO HỎI 3 CÂU TRƯỚC"'), cols=CC, moc=True, chat=dict(ten=QUAN, tv='Đang hoạt động', gio='22:05', mau=X_, msgs=[
        ('me', 'Tao không tiếc vì mua BSR'),
        ('me', 'Tao tiếc vì mua mà không hỏi lãi đó kéo dài bao lâu'),
        ('Quân', 'Tao cũng may thôi, lần sau cả hai cùng hỏi 3 câu')]),
      say=("Tối hôm đó, anh Tú nhắn cho Quân: tao không tiếc vì mua BSR. Tao tiếc vì mua mà không hỏi lãi đó kéo dài bao lâu. "
           "Quân trả lời: tao cũng một phần là may thôi. Lần sau cả hai cùng hỏi ba câu đó trước.")),
 dict(k='end', cap=('ANH CHỊ ĐÃ TỪNG MUA', 'VÌ "LÃI KỶ LỤC" CHƯA?'), cols=CC,
      say=("Còn anh chị, đã từng mua một cổ phiếu chỉ vì tin lãi kỷ lục chưa? Kết quả ra sao? Kể cho em và mọi người ở phần bình luận nhé. "
           "Nếu thấy video hữu ích, anh chị đăng ký kênh để xem những câu chuyện tiếp theo.")),
]
import ql_post; S = ql_post.tach(S, max_tu=100)
for c in S: c['say'] = lib.doc(c['say'])
TIEU = 'Lãi Tăng 888% Mà Cổ Phiếu Vẫn Giảm 14%: Vì Sao BSR, POW Lãi Kỷ Lục Còn MSR Mới Là Cổ Phiếu Tăng?'
MT = ("BSR lãi quý 3/2026 gần 9.000 tỷ (+888%), 9 tháng gấp 11,5 lần kế hoạch năm, P/E chỉ 4,5 – nhưng cổ phiếu giảm gần 14% trong 6 tháng. Cùng lúc MSR tăng 56%. "
      "Vì sao? Câu chuyện hai người bạn, hai lựa chọn, và bài học về P/E thấp ở đỉnh lợi nhuận.\n\n"
      "Nguồn số liệu:\n"
      "• BCTC hợp nhất, LNST cổ đông công ty mẹ: BSR Q3/25 908 · Q4/25 3.062 · Q1/26 8.265 · Q2/26 7.666 · Q3/26 8.968 tỷ; MSR Q1–Q3/26 537 · 1.666 · 2.148 tỷ; POW Q3/26 1.860 tỷ; PGV Q3/26 1.221 tỷ\n"
      "• BSR 9T/2026 24.899 tỷ (+1.057%), 1.151,7% kế hoạch năm; POW 9T 6.434 tỷ, 605,7% kế hoạch\n"
      "• Giá điều chỉnh 22/5 → 11/11/2026: BSR 29.370 → 25.300; MSR 37.620 → 58.700; POW 13.600 → 12.700; PGV 20.770 → 20.700. P/E 11/11: BSR 4,5; POW 5,6; PGV 4,2; MSR 14,2\n"
      "• VNDirect Research, chiến lược tháng 11/2026 (Dòng vốn kinh doanh 11/11/2026): LN DN HOSE Q3 +52%, dự báo Q4 +6%\n"
      "• MetalMiner qua MarketTimes 10/11/2026: APT Rotterdam 278,22 USD/kg (10/2026), gấp 3,74 lần Trung Quốc; Elmet, Sojitz và MSR\n\n"
      "BSR: https://chungkhoanhuynguyen.com/ma/BSR.html · MSR: https://chungkhoanhuynguyen.com/ma/MSR.html\n"
      "POW: https://chungkhoanhuynguyen.com/ma/POW.html · PGV: https://chungkhoanhuynguyen.com/ma/PGV.html\n"
      "Soi P/E, lợi nhuận từng quý 400+ mã: https://chungkhoanhuynguyen.com\n"
      "Cần trao đổi riêng về danh mục: Zalo 0365.188.286\n\n"
      "Nhân vật anh Tú, Quân, chị Ngân là hư cấu; số liệu là thật. Video không đánh giá triển vọng hay khuyến nghị bất kỳ cổ phiếu nào.\n"
      "Chia sẻ góc nhìn, không phải khuyến nghị mua bán.")
META = {KEY: dict(kenh='@chungkhoanhuynguyen', seri='Chuyện gì đã xảy ra?', ngay='2026-11-15', gio_goi_y='12:00', gio='12:00', nhac='lofi',
    tieu_de=TIEU, title=TIEU, mo_ta=MT,
    tags=['BSR', 'cổ phiếu BSR', 'MSR', 'POW', 'PGV', 'lãi kỷ lục', 'P/E thấp', 'cổ phiếu chu kỳ', 'vonfram', 'kết quả kinh doanh quý 3 2026', 'đọc báo cáo tài chính'],
    bia_hook=['LÃI +888%', 'GIÁ VẪN GIẢM?'], badge='VÌ SAO LÃI KỶ LỤC MÀ CỔ PHIẾU KHÔNG TĂNG?',
    bia_anh='ov:oil refinery night||oil refinery',
    bia_hook_b=['P/E 4,5', 'RẺ HAY BẪY?'], badge_b='BSR – POW – PGV – MSR',
    bia_hook_c=['BSR −14%', 'MSR +56%'], badge_c='CÙNG LÃI KỶ LỤC, VÌ SAO KHÁC?',
    fb_post=("Lãi quý 3 tăng 888%, P/E chỉ 4,5 – mà cổ phiếu vẫn giảm 14% 😳\n\n👉 BSR lãi 9 tháng gấp 11,5 lần kế hoạch năm\n👉 POW, PGV cũng lãi kỷ lục, giá đi ngang hoặc giảm\n"
             "👉 Cùng lúc MSR +56%\n\nThị trường không trả tiền cho lợi nhuận đã qua. 3 câu hỏi trước khi mua vì 'lãi kỷ lục'.\n\n🎬 Xem đầy đủ: {LINK}"),
    chuong=[c['ch'] for c in S if c.get('ch')])}
os.makedirs(LO, exist_ok=True)
open(LO + '/video_dai.py', 'w', encoding='utf-8').write(
    "# VIDEO DÀI kênh chính – kể chuyện 'Lãi tăng 888 phần trăm mà cổ phiếu vẫn giảm' (QL1 11/11/2026).\n"
    "CHI_CTA_CUOI = True\nGOLD=%r; RED=%r; GREEN=%r; BLUE=%r; WHITE=%r\nS = {}\n" % (GOLD, RED, GREEN, BLUE, WHITE) + "S[%r] = %r\n" % (KEY, S) + "META = %r\n" % META)
json.dump(META, open(LO + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({}, open(LO + '/px_tuan.json', 'w'))
from collections import Counter
print('so chu', lib.dem(S), 'canh', len(S), dict(Counter(c['k'] for c in S)), len(TIEU))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
