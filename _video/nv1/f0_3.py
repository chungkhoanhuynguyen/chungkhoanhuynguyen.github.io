# -*- coding: utf-8 -*-
# NV1 10/11/2026: 3 bài F0 chuẩn bai_seo_hay_hon_0811 (S&P 500 vs VN-Index, đáy 52 tuần, LTCM 1998). Dùng: python3 f0_3.py [--ghi]
import json, sys, re
P = '/tmp/cw/_f0/bai.json'
L = lambda s, t: '<a href="/f0/%s.html">%s</a>' % (s, t)
B = []
B.append(dict(slug="chung-khoan-my-giam-vn-index-co-giam-theo", kw="chứng khoán Mỹ giảm VN-Index có giảm theo không", grp=8,
 title="Chứng khoán Mỹ giảm, VN-Index có giảm theo? Số liệu 155 tuần",
 desc="155 tuần dữ liệu: tương quan S&P 500 và VN-Index chỉ 0,37. 3/5 tuần VN-Index giảm sâu nhất, Mỹ gần như đứng yên. Cách đọc tin Mỹ cho người mới.",
 body=[
 ["p", "Tuần bắt đầu ngày 31/3/2025, S&P 500 giảm <b>9,08%</b>, VN-Index giảm <b>8,11%</b>. Từ đó, mỗi sáng thấy phố Wall đỏ, nhiều nhà đầu tư Việt lại lo \"Mỹ hắt hơi, Việt Nam cảm cúm\". Nhưng tuần bắt đầu 20/7/2026, VN-Index giảm 5,67% trong khi S&P 500 chỉ giảm 0,61%. Vậy chứng khoán Mỹ quan trọng tới mức nào? Em lấy 155 tuần dữ liệu, từ tháng 11/2023 tới ngày 9/11/2026, để trả lời bằng số."],
 ["h2", "Tương quan 0,37 nghĩa là gì?"],
 ["p", "Hệ số tương quan đo mức hai chuỗi số đi cùng chiều: bằng 1 là luôn đi cùng nhau, bằng 0 là không liên quan. Em gom giá đóng cửa S&P 500 và VN-Index theo tuần, tính phần trăm thay đổi mỗi tuần rồi tính tương quan. Kết quả: <b>khoảng 0,37</b>."],
 ["p", "Bình phương con số này (0,37 × 0,37 ≈ 0,14) cho biết về mặt thống kê, chỉ khoảng <b>14%</b> biến động tuần của VN-Index đi cùng S&P 500. Phần còn lại đến từ yếu tố khác: dòng tiền trong nước, tỷ giá, vay ký quỹ, tin riêng của từng nhóm ngành."],
 ["h2", "Khi Mỹ giảm mạnh, VN-Index làm gì?"],
 ["p", "Trong 155 tuần, S&P 500 có 4 tuần giảm từ 3% trở lên. VN-Index giảm cùng tuần 3 lần:"],
 ["table", [["Tuần bắt đầu", "S&P 500", "VN-Index", "Ghi chú"],
   ["15/4/2024", "−3,05%", "−7,97%", "VN giảm mạnh hơn Mỹ"], ["2/9/2024", "−4,25%", "−0,77%", "VN giảm nhẹ"],
   ["3/3/2025", "−3,10%", "+1,59%", "VN đi ngược"], ["31/3/2025", "−9,08%", "−8,11%", "Cú sốc thuế quan"]]],
 ["p", "Chiều ngược lại, 12 tuần S&P 500 tăng từ 3% trở lên thì VN-Index tăng 10 lần, nhưng biên độ thường nhỏ hơn. Ví dụ tuần bắt đầu 7/4/2025, S&P 500 tăng khoảng 5,7%, VN-Index chỉ tăng khoảng 1%."],
 ["h2", "Năm tuần tệ nhất của VN-Index, Mỹ ở đâu?"],
 ["p", "Đảo câu hỏi lại mới thấy điều bất ngờ. Năm tuần VN-Index giảm sâu nhất trong mẫu:"],
 ["ol", ["Tuần 31/3/2025: VN-Index −8,11%, S&P 500 −9,08%.", "Tuần 15/4/2024: VN-Index −7,97%, S&P 500 −3,05%.", "Tuần 2/3/2026: VN-Index −5,98%, S&P 500 −2,02%.",
   "Tuần 20/7/2026: VN-Index −5,67%, S&P 500 −0,61%.", "Tuần 8/12/2025: VN-Index −5,42%, S&P 500 −0,63%."]],
 ["p", "Có <b>3/5 tuần</b> S&P 500 chỉ giảm chưa tới 2,1%. Nghĩa là rủi ro lớn nhất của VN-Index thường nằm ở trong nước. Người chỉ canh phố Wall mỗi sáng có thể bỏ sót đúng những tín hiệu quan trọng nhất."],
 ["h2", "Tin Mỹ truyền sang Việt Nam qua đường nào?"],
 ["ul", ["<b>Lãi suất Fed và đồng USD:</b> USD mạnh làm áp lực tỷ giá tăng, lãi suất trong nước khó giảm (xem " + L("fed-tang-giam-lai-suat-tac-dong", "Fed tăng giảm lãi suất tác động thế nào") + ").",
   "<b>Khối ngoại:</b> khi nhà đầu tư toàn cầu sợ hãi, họ rút tiền khỏi thị trường mới nổi và cận biên (" + L("khoi-ngoai-mua-rong-ban-rong-la-gi", "khối ngoại mua ròng, bán ròng") + ").",
   "<b>Xuất khẩu:</b> Mỹ là thị trường xuất khẩu lớn nhất của Việt Nam, tin thuế quan tác động thẳng vào doanh nghiệp dệt may, thủy sản, gỗ, khu công nghiệp."]],
 ["p", "Cú sốc đi qua cả ba kênh cùng lúc, như đầu tháng 4/2025, thường làm VN-Index giảm mạnh nhất. Cú giảm của Mỹ chỉ do định giá công nghệ cao thì tác động sang Việt Nam thường nhẹ hơn."],
 ["h2", "Bẫy hay gặp"],
 ["ul", ["<b>Bán vội lúc mở cửa vì đêm qua Mỹ đỏ.</b> Tuần 3/3/2025, S&P 500 giảm 3,10% nhưng VN-Index tăng 1,59%. Người bán sớm vừa mất hàng vừa mua lại giá cao hơn.",
   "<b>Mua đuổi vì Mỹ lập đỉnh.</b> Mỹ tăng 5,7% không kéo VN-Index tăng 5,7%. Biên độ hai thị trường rất khác nhau.",
   "<b>Bỏ qua chỉ số trong nước.</b> Tỷ giá, lãi suất liên ngân hàng, dư nợ ký quỹ mới đứng sau phần lớn các tuần tệ nhất của VN-Index (" + L("ty-gia-tang-anh-huong-co-phieu", "tỷ giá tăng ảnh hưởng cổ phiếu") + ")."]],
 ["h2", "Checklist sáng thứ Hai"],
 ["ul", ["S&P 500 tuần trước giảm/tăng bao nhiêu? Dưới 3% thì chưa cần đổi kế hoạch.", "Tỷ giá USD/VND và chỉ số DXY tăng hay giảm.", "Khối ngoại tuần trước mua hay bán ròng.",
   "Lãi suất liên ngân hàng có tăng vọt không.", "Tỷ lệ vay ký quỹ của chính tài khoản mình còn an toàn nếu giảm thêm 10%."]],
 ["p", "Số liệu ba năm là mẫu ngắn, chưa có các giai đoạn như 2008 hay 2022, nên đây là cách nhìn chứ không phải quy luật. Cần trao đổi riêng về danh mục: Zalo 0365.188.286."]],
 faq=[["Chứng khoán Mỹ giảm thì VN-Index có giảm không?", "Không phải lúc nào cũng vậy. Trong 155 tuần từ 11/2023 đến 11/2026, 4 tuần S&P 500 giảm từ 3% trở lên thì VN-Index giảm cùng tuần 3 lần. Tương quan theo tuần chỉ khoảng 0,37."],
      ["Nên xem chỉ số Mỹ nào?", "S&P 500 đại diện rộng nhất cho thị trường Mỹ. Nasdaq nghiêng về công nghệ. Kèm chỉ số USD (DXY) và lợi suất trái phiếu Mỹ 10 năm để thấy tác động lên tỷ giá."],
      ["Yếu tố trong nước nào ảnh hưởng VN-Index nhiều nhất?", "Tỷ giá USD/VND, lãi suất liên ngân hàng, dư nợ vay ký quỹ, giao dịch khối ngoại và lợi nhuận doanh nghiệp. Ba trong năm tuần giảm sâu nhất của VN-Index ba năm qua xảy ra khi Mỹ gần như đứng yên."]],
 rel=["fed-tang-giam-lai-suat-tac-dong", "ty-gia-tang-anh-huong-co-phieu", "khoi-ngoai-mua-rong-ban-rong-la-gi", "tuong-quan-co-phieu-trong-danh-muc"]))

B.append(dict(slug="co-phieu-cham-day-52-tuan-co-nen-mua", kw="cổ phiếu chạm đáy 52 tuần có nên mua", grp=4,
 title="Cổ phiếu chạm đáy 52 tuần có nên mua? 10 mã, 2 câu chuyện",
 desc="Ngày 9/11/2026, 10/69 mã lớn sát đáy 52 tuần: PNJ lỗ quý 3, BID lãi +39,9%. Đáy 52 tuần là gì, phân biệt rẻ thật và bẫy giá bằng 4 bước.",
 body=[
 ["p", "Ngày 9/11/2026, cổ phiếu PNJ đóng cửa <b>14.200 đồng</b>, đúng mức thấp nhất 52 tuần, trong khi đỉnh 52 tuần là khoảng 84.670 đồng. Cùng ngày, BIDV (BID) cũng chỉ cách đáy 52 tuần khoảng 1%. Hai mã cùng nằm ở \"đáy\", nhưng một mã quý 3 lỗ 257 tỷ, mã kia lãi tăng 39,9%. Đáy 52 tuần là tín hiệu rẻ hay lời cảnh báo? Câu trả lời nằm ở chỗ khác ngoài giá."],
 ["h2", "Đáy 52 tuần là gì?"],
 ["p", "<b>Đáy 52 tuần</b> là giá thấp nhất của cổ phiếu trong khoảng một năm gần nhất; <b>đỉnh 52 tuần</b> là giá cao nhất. Hai con số này có trên hầu hết bảng giá và trang thông tin mã. Chúng cho biết giá hiện tại đang ở đâu trong biên độ một năm, nhưng không cho biết vì sao giá ở đó."],
 ["p", "Cách tính khoảng cách tới đỉnh: (1 − giá hiện tại / đỉnh 52 tuần) × 100. Với PNJ: (1 − 14,2 / 84,67) × 100 ≈ <b>83,2%</b>. Nghĩa là người mua ở đỉnh đang lỗ khoảng 83%, và cần giá tăng gần 500% mới hòa vốn."],
 ["h2", "10 mã sát đáy, hai câu chuyện"],
 ["p", "Trong 69 mã lớn có đủ báo cáo quý 3/2026 trên dữ liệu của web, có 10 mã đóng cửa ngày 9/11/2026 cách đáy 52 tuần dưới 3%. Đặt giá cạnh lợi nhuận quý 3 so với cùng kỳ:"],
 ["table", [["Mã", "Giá 9/11 (nghìn đ)", "Thấp hơn đỉnh 52 tuần", "LNST quý 3/2026", "Câu chuyện"],
   ["PNJ", "14,2", "83,2%", "Lỗ 257 tỷ", "Lợi nhuận giảm"], ["DPM", "19,3", "39,4%", "−82,9%", "Lợi nhuận giảm"], ["EIB", "16,25", "32,9%", "−67,6%", "Lợi nhuận giảm"],
   ["BID", "32,05", "37,0%", "+39,9%", "Lợi nhuận tăng"], ["LPB", "34,9", "37,7%", "+28,9%", "Lợi nhuận tăng"], ["CTR", "63,9", "32,6%", "+8,6%", "Lợi nhuận tăng"]]],
 ["p", "Nhóm trên: giá giảm đi cùng lợi nhuận giảm, thị trường đang phản ánh kết quả kinh doanh xấu đi. Nhóm dưới: giá giảm trong khi lợi nhuận vẫn tăng, khoảng cách giữa giá và kết quả kinh doanh rộng ra. Chỉ nhóm dưới mới đáng được xem kỹ hơn, và \"xem kỹ\" vẫn chưa có nghĩa là mua."],
 ["h2", "Vì sao P/E thấp ở đáy có thể đánh lừa?"],
 ["p", "PNJ có P/E khoảng 4,56 lần, nghe rất rẻ. Nhưng P/E dùng lợi nhuận 4 quý gần nhất, vẫn gồm những quý lãi tốt trước đó. Khi quý mới nhất đã lỗ, lợi nhuận 4 quý tới có thể thấp hơn nhiều, và P/E thật sẽ cao hơn con số đang thấy. Ngược lại, EIB có P/E khoảng 158 lần vì lợi nhuận giảm mạnh, con số này cũng không nói được nhiều. Ở vùng đáy, đọc P/E phải kèm xu hướng lợi nhuận."],
 ["h2", "Còn đỉnh 52 tuần thì sao?"],
 ["p", "Chiều ngược lại cũng cần bình tĩnh. Cùng ngày 9/11/2026, chỉ 1/69 mã sát đỉnh 52 tuần là MSB, giá 16.300 đồng so với đỉnh 16.450 đồng, lợi nhuận quý 3 tăng 29,4%. Giá ở đỉnh không tự động là đắt, giá ở đáy không tự động là rẻ. Thứ quyết định vẫn là giá đang trả cho bao nhiêu lợi nhuận và lợi nhuận đó đang đi về đâu."],
 ["h2", "Bẫy hay gặp"],
 ["ul", ["<b>\"Giảm 80% rồi, còn giảm được bao nhiêu nữa?\"</b> Mã đã giảm 80% vẫn có thể giảm thêm 50%. PNJ từ khoảng 35 nghìn giữa tháng 8 xuống 14,2 nghìn ngày 9/11, giảm thêm khoảng 60% chỉ trong ba tháng.",
   "<b>Tin vào tỷ suất cổ tức cao.</b> Tỷ suất cổ tức PNJ nhìn lên 10,54% chủ yếu vì giá rơi (xem " + L("bay-co-tuc-cao-la-gi", "bẫy cổ tức cao") + ").",
   "<b>Bắt đáy bằng toàn bộ tiền.</b> Đáy 52 tuần hôm nay có thể là giá cao của tuần sau. Chia nhỏ tiền và đặt trần tỷ trọng trước (" + L("bat-day-co-phieu-la-gi", "bắt đáy cổ phiếu là gì") + ")."]],
 ["h2", "Checklist 5 bước trước khi mua mã sát đáy"],
 ["ol", ["Tính khoảng cách giá hiện tại so với đỉnh 52 tuần.", "Mở báo cáo quý gần nhất: lợi nhuận và doanh thu tăng hay giảm so với cùng kỳ.",
   "Xem lũy kế 9 tháng để tránh kết luận từ một quý bất thường.", "Kiểm tra dòng tiền kinh doanh và nợ vay có xấu đi không.", "Đặt trần tỷ trọng tối đa cho mã đó và chia ít nhất 2–3 lần mua."]],
 ["p", "Giá ở đáy 52 tuần chỉ là điểm bắt đầu để đặt câu hỏi, không phải câu trả lời. Cần trao đổi riêng về danh mục: Zalo 0365.188.286."]],
 faq=[["Đáy 52 tuần là gì?", "Là giá thấp nhất của cổ phiếu trong khoảng một năm gần nhất. Nó cho biết giá đang ở đâu trong biên độ một năm, nhưng không giải thích vì sao."],
      ["Cổ phiếu chạm đáy 52 tuần có phải là rẻ?", "Chưa chắc. Nếu lợi nhuận giảm cùng giá, như PNJ lỗ quý 3/2026, giá thấp đang phản ánh kinh doanh xấu đi. Nếu lợi nhuận vẫn tăng, như BID, LPB, mã đó đáng được phân tích kỹ hơn."],
      ["Xem đỉnh, đáy 52 tuần ở đâu?", "Trên bảng giá của công ty chứng khoán và trang tra cứu mã của chungkhoanhuynguyen.com, kèm P/E, P/B và kết quả kinh doanh 8 quý."]],
 rel=["bat-day-co-phieu-la-gi", "bay-co-tuc-cao-la-gi", "ty-suat-co-tuc-la-gi", "tam-ly-fomo-va-hoang-loan"]))

B.append(dict(slug="ltcm-1998-bai-hoc-don-bay", kw="LTCM là gì bài học đòn bẩy", grp=5,
 title="LTCM 1998: quỹ có 2 Nobel mất 4,6 tỷ USD – bài học đòn bẩy",
 desc="LTCM vay hơn 120 tỷ USD trên 4,7 tỷ vốn, mất 4,6 tỷ USD trong chưa đầy 4 tháng năm 1998. Bài học đòn bẩy, thanh khoản cho người dùng margin ở Việt Nam.",
 body=[
 ["p", "Năm 1997, Myron Scholes và Robert Merton nhận giải Nobel kinh tế. Cả hai là thành viên quỹ Long-Term Capital Management (LTCM) ở Mỹ. Chỉ một năm sau, trong chưa đầy bốn tháng của năm 1998, quỹ mất khoảng <b>4,6 tỷ USD</b> và phải được 14 ngân hàng giải cứu. Nếu những người giỏi nhất còn thua vì đòn bẩy, nhà đầu tư dùng margin ở Việt Nam học được gì?"],
 ["h2", "LTCM kiếm tiền thế nào?"],
 ["p", "LTCM được John Meriwether, cựu lãnh đạo mảng trái phiếu của Salomon Brothers, thành lập năm 1994. Quỹ tìm hai loại trái phiếu gần giống nhau nhưng giá chênh nhau một chút, mua cái rẻ, bán khống cái đắt, chờ hai giá về gần nhau. Mỗi lần chỉ lời rất ít, nên quỹ vay rất nhiều để phóng to lợi nhuận. Sau phí, nhà đầu tư nhận khoảng 21% năm 1994, 43% năm 1995 và 41% năm 1996."],
 ["h2", "Đòn bẩy 25 lần trông như thế nào?"],
 ["p", "Đầu năm 1998, LTCM có khoảng 4,7 tỷ USD vốn nhưng vay hơn 120 tỷ USD. Tính từng bước:"],
 ["ol", ["Tổng tài sản ≈ 4,7 + 120 ≈ 125 tỷ USD.", "Đòn bẩy ≈ 125 / 4,7 ≈ <b>26 lần</b>, thường được làm tròn là khoảng 25 lần.",
   "Tài sản giảm 1% ≈ mất 1,25 tỷ USD ≈ <b>27% vốn</b>.", "Tài sản giảm 4% là gần như mất trắng vốn."]],
 ["p", "Ngày 17/8/1998, Nga phá giá đồng rúp và ngừng trả một phần nợ. Nhà đầu tư toàn cầu đổ vào trái phiếu Mỹ an toàn nhất, mọi khoản chênh lệch LTCM đặt cược cùng lúc giãn ra. Riêng tháng 8/1998, quỹ mất gần một nửa vốn. Ngày 23/9/1998, Fed New York đứng ra tổ chức để 14 tổ chức tài chính góp khoảng 3,6 tỷ USD, tiếp quản khoảng 90% quỹ."],
 ["h2", "So sánh với tài khoản margin ở Việt Nam"],
 ["table", [["", "LTCM 1998", "Tài khoản vay 1:1", "Tài khoản không vay"],
   ["Vốn tự có", "4,7 tỷ USD", "500 triệu", "500 triệu"], ["Tổng tài sản", "≈125 tỷ USD", "1 tỷ", "500 triệu"],
   ["Đòn bẩy", "≈26 lần", "2 lần", "1 lần"], ["Cổ phiếu giảm 20% thì vốn mất", "Mất trắng nhiều lần", "40%", "20%"]]],
 ["p", "Tài khoản vay 1:1 không đáng sợ như LTCM, nhưng nguyên lý giống hệt: đòn bẩy nhân cả lãi lẫn lỗ. Khi tài khoản chạm tỷ lệ ký quỹ duy trì, công ty chứng khoán " + L("ban-giai-chap-la-gi", "bán giải chấp") + " bất kể anh chị tin cổ phiếu tốt đến đâu."],
 ["p", "Sau cuộc giải cứu, Fed giảm lãi suất ba lần trong mùa thu năm 1998 để trấn an thị trường. Các nhà sáng lập gần như mất trắng phần vốn của mình, và quỹ được giải thể vào đầu năm 2000. Câu chuyện được kể lại chi tiết trong cuốn sách When Genius Failed của Roger Lowenstein, xuất bản năm 2000."],
 ["h2", "Thanh khoản biến mất đúng lúc cần"],
 ["p", "Khi lỗ, LTCM cần bán bớt để giảm nợ, nhưng vị thế quá lớn và cả thị trường biết quỹ đang kẹt. Không ai muốn mua ở giá hợp lý, giá càng xuống. Ở Việt Nam, những phiên nhiều mã giảm sàn, lệnh bán giải chấp xếp hàng mà không khớp cũng là cảnh tương tự (xem " + L("rui-ro-thanh-khoan-co-phieu", "rủi ro thanh khoản cổ phiếu") + ")."],
 ["h2", "Bẫy hay gặp"],
 ["ul", ["<b>\"Mình đã thắng nhiều lần.\"</b> LTCM thắng ba năm liền trước khi mất gần hết trong bốn tháng. Chuỗi thắng làm người ta tăng vay đúng lúc rủi ro tích tụ.",
   "<b>\"Chưa từng giảm sâu như vậy.\"</b> Mô hình của LTCM dựa trên dữ liệu lịch sử, nhưng thị trường hoảng loạn tạo ra điều chưa có trong dữ liệu.",
   "<b>\"Cần là bán được.\"</b> Thanh khoản có mặt khi không cần, biến mất khi cần nhất, nhất là với mã nhỏ."]],
 ["h2", "Checklist cho người dùng margin"],
 ["ul", ["Dư nợ vay không vượt 50% vốn tự có nếu mới đầu tư.", "Tính trước VN-Index hoặc mã mình nắm giảm bao nhiêu thì chạm " + L("call-margin-la-gi", "call margin") + ".",
   "Không dồn vay vào một mã hoặc một ngành.", "Kiểm tra giá trị giao dịch bình quân của mã: bán hết trong một phiên được không.", "Viết sẵn kế hoạch giảm nợ trước khi thị trường xấu."]],
 ["p", "Câu chuyện LTCM theo báo cáo của Nhóm Công tác về Thị trường Tài chính của Tổng thống Mỹ (4/1999) và các tài liệu công khai. Cần trao đổi riêng về danh mục: Zalo 0365.188.286."]],
 faq=[["LTCM là gì?", "Long-Term Capital Management, quỹ đầu tư ở Mỹ thành lập năm 1994, có hai thành viên đoạt Nobel kinh tế 1997. Năm 1998 quỹ mất khoảng 4,6 tỷ USD và được 14 ngân hàng tiếp quản."],
      ["Vì sao LTCM sụp đổ?", "Đòn bẩy khoảng 25 lần, các khoản đặt cược cùng lúc đi ngược sau khi Nga vỡ nợ tháng 8/1998, và thanh khoản biến mất khi quỹ cần bán."],
      ["Bài học LTCM cho nhà đầu tư cá nhân là gì?", "Kiểm soát đòn bẩy, tính trước ngưỡng bị bán giải chấp, không dồn vay vào một mã và luôn có kế hoạch giảm nợ."]],
 rel=["margin-la-gi", "call-margin-la-gi", "ban-giai-chap-la-gi", "rui-ro-thanh-khoan-co-phieu"]))

if __name__ == '__main__':
    D = json.load(open(P, encoding='utf-8')); have = {x['slug'] for x in D}
    for b in B:
        txt = " ".join(re.sub('<[^>]+>', '', json.dumps(b['body'], ensure_ascii=False)).split()) + " ".join(a + b2 for a, b2 in b['faq'])
        print(b['slug'], b['slug'] in have, len(b['title']), len(b['desc']), len(txt.split()), [r for r in b['rel'] if r not in have])
    if '--ghi' in sys.argv:
        D += [b for b in B if b['slug'] not in have]
        json.dump(D, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
