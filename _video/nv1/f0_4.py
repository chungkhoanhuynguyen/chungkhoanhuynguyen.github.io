# -*- coding: utf-8 -*-
# NV1 16/11/2026: 2 bài F0 chuẩn bai_seo_hay_hon_0811, nối 2 chiều với CH2011VON (lãi suất thực) và CH2111FED (chỉ số DXY). Dùng: python3 f0_4.py [--ghi]
import json, sys, re
P = '/tmp/cw/_f0/bai.json'
L = lambda s, t: '<a href="/f0/%s.html">%s</a>' % (s, t)
B = []
B.append(dict(slug="lai-suat-thuc-la-gi", kw="lãi suất thực là gì", grp=8, date="2026-11-16",
 title="Lãi suất thực là gì? Gửi 5,4% mà giá cả tăng 5,09% thì còn gì",
 desc="Lãi suất thực = lãi suất gửi trừ lạm phát. Tháng 11/2026: lãi 12 tháng 5,4%, CPI tháng 10 +5,09%, lãi thật chỉ khoảng 0,3%. Cách tự tính cho sổ của mình.",
 body=[
 ["p", "Một cuốn sổ tiết kiệm 800 triệu, kỳ hạn 12 tháng, lãi <b>5,4%</b> – mức các ngân hàng thương mại Nhà nước đang trả (WiData, 13/11/2026). Một năm nhận <b>43,2 triệu</b> tiền lãi. Nghe ổn. Nhưng giá cả tháng 10/2026 tăng <b>5,09%</b> so với cùng kỳ. Tám trăm triệu bị giá cả ăn mất khoảng <b>40,7 triệu</b> sức mua. Sau một năm, người gửi thật sự giàu thêm khoảng <b>2,5 triệu</b>."],
 ["p", "Con số 2,5 triệu đó, hay khoảng 0,3% trên 800 triệu, chính là <b>lãi suất thực</b>."],
 ["h2", "Lãi suất thực là gì?"],
 ["p", "Lãi suất thực là phần tiền lãi còn lại sau khi trừ đi mức tăng giá cả. Cách tính gần đúng mà ai cũng làm được:"],
 ["p", "<b>Lãi suất thực ≈ lãi suất danh nghĩa − lạm phát</b>. Ví dụ: 5,4% − 5,09% = <b>0,31 điểm phần trăm</b>."],
 ["p", "Lãi suất danh nghĩa là con số in trên sổ. Lạm phát là mức tăng giá cả (CPI) so với cùng kỳ năm trước, Cục Thống kê công bố hằng tháng. Lãi thật dương nghĩa là tiền của anh chị đang mua được nhiều hàng hơn; lãi thật âm nghĩa là tiền đang nghèo đi, dù số dư trên sổ vẫn tăng."],
 ["h2", "Ba thời điểm, ba mức lãi thật"],
 ["table", [["Thời điểm", "Lãi gửi", "Lạm phát", "Lãi thật (tự tính)"],
   ["Năm 2011", "Trần 14% (Thông tư 02/2011)", "CPI bình quân 18,6%", "Khoảng −4,6 điểm"],
   ["Tháng 10/2026", "5,4% (12 tháng, NHTM Nhà nước)", "CPI so cùng kỳ 5,09%", "Khoảng +0,3 điểm"],
   ["Giả định sổ 7%", "7%", "5,09%", "Khoảng +1,9 điểm"]]],
 ["p", "Năm 2011 lãi gửi lên tới 14% nhưng vẫn thua giá cả hơn 4 điểm phần trăm (lạm phát 2011 theo Vietnamnet 23/6/2025). Năm 2026 lãi gửi thấp hơn nhiều nhưng lãi thật vẫn dương nhẹ. Con số in trên sổ không nói lên tất cả."],
 ["h2", "Vì sao lãi thật lại quan trọng lúc này?"],
 ["p", "Việt Nam cần khoảng <b>38,5 triệu tỷ đồng</b> vốn đầu tư giai đoạn 2026–2030 (VnBusiness 22/10/2026), và hơn 50% vốn của nền kinh tế đi qua ngân hàng – tức là từ tiền gửi của người dân. Tới tháng 8/2026, tín dụng tăng 17,38% so với cùng kỳ, còn tiền gửi chỉ tăng 13,65% (WiData). Khi cho vay chạy nhanh hơn tiền gửi, ngân hàng thiếu nguồn: hoặc phải trả lãi cao hơn, hoặc bớt cho vay. Người gửi tiền nên theo dõi lãi thật để biết mình đang được trả công bao nhiêu cho phần vốn đóng góp đó."],
 ["p", "Cùng logic với " + L("luong-thuc-te-la-gi", "lương thực tế") + ": lương tăng 8% mà giá cả tăng 5% thì sức mua chỉ tăng khoảng 3%."],
 ["h2", "Bẫy hay gặp"],
 ["ul", ["<b>Chỉ nhìn con số trên sổ.</b> Năm 2011, sổ lãi 14% trông rất hấp dẫn, nhưng giá cả bình quân tăng 18,6%.",
   "<b>So lãi suất với tháng trước thay vì với giá cả.</b> Lãi giảm từ 6% xuống 5,4% chưa chắc tệ hơn nếu lạm phát cũng giảm mạnh hơn.",
   "<b>Chạy theo lãi cao bằng mọi giá.</b> Sản phẩm trả lãi cao hơn tiết kiệm (trái phiếu doanh nghiệp, hợp đồng bảo hiểm liên kết) thường đi kèm rủi ro khác; xem " + L("tich-san-co-phieu-hay-gui-tiet-kiem", "tích sản cổ phiếu hay gửi tiết kiệm") + "."]],
 ["h2", "Checklist tự tính lãi thật cho nhà mình"],
 ["ul", ["Ghi lãi suất từng khoản tiền gửi, tính lãi suất bình quân theo số tiền.",
   "Lấy CPI so cùng kỳ tháng gần nhất (tháng 10/2026: 5,09%).",
   "Lãi thật = lãi bình quân − CPI. Âm: tiền đang nghèo đi; 0 đến 2 điểm: giữ được giá; trên 2 điểm: đang được trả công (mốc em tự đặt để tự soi, không phải quy định).",
   "Luôn giữ 6 tháng chi tiêu ở khoản dễ rút, dù lãi thật thấp.",
   "Xem lại mỗi năm một lần, hoặc khi CPI đổi hướng; đọc thêm " + L("lam-phat-va-chung-khoan", "lạm phát và chứng khoán") + "."]],
 ["p", "<small>Nguồn: WiData (lãi suất huy động 12 tháng NHTM Nhà nước 13/11/2026, CPI tháng 10/2026, tín dụng và tiền gửi tháng 8/2026); VnBusiness 22/10/2026; Vietnamnet 23/6/2025; Thông tư 02/2011/TT-NHNN. Sổ 800 triệu là ví dụ giả định. Bài chia sẻ kiến thức, không phải khuyến nghị.</small>"]],
 faq=[["Lãi suất thực là gì?", "Là lãi suất danh nghĩa trừ đi lạm phát, cho biết sau một năm tiền gửi mua được thêm bao nhiêu hàng hoá. Tháng 11/2026: 5,4% − 5,09% ≈ 0,3 điểm phần trăm."],
      ["Lãi suất thực âm thì sao?", "Tiền gửi vẫn tăng về số dư nhưng mua được ít hàng hơn. Năm 2011, lãi gửi trần 14% còn CPI bình quân 18,6%, lãi thật khoảng −4,6 điểm."],
      ["Lấy lạm phát ở đâu để tính?", "Dùng CPI so cùng kỳ do Cục Thống kê công bố đầu mỗi tháng; với khoản gửi 12 tháng, nhiều người dùng CPI bình quân từ đầu năm để ổn định hơn."]],
 rel=["luong-thuc-te-la-gi", "tich-san-co-phieu-hay-gui-tiet-kiem", "lam-phat-va-chung-khoan"]))
B.append(dict(slug="chi-so-dxy-la-gi", kw="chỉ số DXY là gì", grp=8, date="2026-11-16",
 title="Chỉ số DXY là gì? Đô la mạnh nhất từ 4/2025, túi người Việt bị gì",
 desc="DXY đo sức mạnh đồng USD so với 6 đồng tiền lớn. Ngày 14/11/2026 DXY lên 103,41, tỷ giá Vietcombank tăng 130 đồng/tuần. Cách đọc DXY cho người mới.",
 body=[
 ["p", "Tuần 9–13/11/2026, chỉ số DXY tăng <b>1,09%</b> lên <b>103,41 điểm</b>, cao nhất kể từ tháng 4/2025. Cùng tuần, giá bán USD ở Vietcombank tăng <b>130 đồng</b> lên 25.910 đồng, BIDV tăng 145 đồng lên 25.920 đồng (Hà Nội Mới 14/11/2026). Một con số bên Mỹ, chạm thẳng vào bảng tỷ giá ở Việt Nam chỉ trong vài ngày."],
 ["h2", "Chỉ số DXY là gì?"],
 ["p", "DXY (US Dollar Index) đo giá trị đồng đô la Mỹ so với một rổ 6 đồng tiền lớn: euro, yen Nhật, bảng Anh, đô la Canada, krona Thuỵ Điển và franc Thuỵ Sĩ, trong đó euro chiếm tỷ trọng lớn nhất. DXY tăng nghĩa là USD mạnh lên so với các đồng tiền này; giảm là USD yếu đi."],
 ["h2", "DXY khác tỷ giá USD/VND thế nào?"],
 ["p", "DXY không có đồng Việt Nam trong rổ. Tỷ giá USD/VND do Ngân hàng Nhà nước điều hành quanh <b>tỷ giá trung tâm</b>, ngân hàng thương mại được yết giá trong biên độ ±5% (tuần 9–13/11/2026: từ 24.355 đến 26.919 đồng). Vì vậy DXY tăng 1% không có nghĩa tỷ giá trong nước tăng đúng 1%. Tuần đó DXY tăng 1,09%, còn giá bán USD ở Vietcombank tăng khoảng 0,5% (130 đồng trên 25.780 đồng, em tự tính)."],
 ["p", "Cách hiểu đơn giản: DXY là “nhiệt kế” cho sức mạnh của USD trên toàn thế giới. Khi nhiệt kế lên cao, đồng Việt Nam chịu áp lực, nhưng mức độ phụ thuộc vào dự trữ ngoại hối, cán cân thương mại và cách Ngân hàng Nhà nước điều hành. Người mới chỉ cần nhớ: theo dõi DXY để biết <b>hướng gió</b>, còn theo dõi giá bán USD ở ngân hàng để biết <b>túi mình</b> bị chạm tới đâu."],
 ["h2", "Vì sao DXY đang tăng?"],
 ["p", "Nguyên nhân chính là kỳ vọng Fed tăng lãi suất. Lãi suất Fed đang ở 3,75–4% (Vietnam+ 11/11/2026), Fed đã tăng lãi suất tháng 9, và công cụ CME FedWatch cho khả năng tăng tiếp ở cuộc họp 8–9/12 trên 80%. Lợi suất trái phiếu Mỹ 2 năm lên 4,725% (CafeF 12/11/2026). Gửi tiền bằng USD có lãi cao hơn thì dòng tiền toàn cầu có xu hướng chảy về USD."],
 ["h2", "DXY tăng chạm vào túi người Việt qua 3 đường"],
 ["table", [["Kênh", "Chuyện gì xảy ra", "Ai chịu trước"],
   ["Tỷ giá", "Giá mua USD trong nước tăng (tuần 9–13/11: tỷ giá trung tâm 25.637, +22 đồng)", "Người du học, nhập hàng, có khoản vay USD"],
   ["Lãi suất", "Ngân hàng Nhà nước khó giảm lãi suất tiếp khi Mỹ tăng", "Người vay mua nhà lãi thả nổi"],
   ["Chứng khoán", "Khối ngoại có thể rút vốn khỏi thị trường mới nổi", "Người dùng vay ký quỹ"]]],
 ["p", "Năm 2022 là ví dụ rõ nhất: Fed tăng lãi suất 7 lần, Ngân hàng Nhà nước tăng lãi suất điều hành 2 lần (tháng 9 và 10/2022), VN-Index từ 1.498,28 điểm cuối 2021 xuống 1.007,09 điểm cuối 2022, giảm 32,8% (BSC 30/12/2022, em tự tính). Xem thêm " + L("fed-tang-giam-lai-suat-tac-dong", "Fed tăng giảm lãi suất tác động thế nào") + "."],
 ["h2", "Bẫy hay gặp"],
 ["ul", ["<b>Nghĩ DXY tăng là VN-Index chắc chắn giảm.</b> DXY chỉ là một kênh; nhiều tuần VN-Index giảm mạnh mà Mỹ gần như đứng yên (xem " + L("chung-khoan-my-giam-vn-index-co-giam-theo", "chứng khoán Mỹ giảm, VN-Index có giảm theo") + ").",
   "<b>Đổ tiền mua USD tự do để \"đón sóng\".</b> Chênh lệch mua bán và rủi ro pháp lý có thể ăn hết phần lợi.",
   "<b>Quên khoản vay của chính mình.</b> Người vay ký quỹ hoặc vay nhà lãi thả nổi chịu tác động sớm hơn người chỉ cầm tiền mặt."]],
 ["h2", "Checklist theo dõi khi DXY tăng"],
 ["ul", ["Xem DXY và giá bán USD ở 2–3 ngân hàng lớn mỗi tuần.",
   "Ghi lịch họp Fed (gần nhất 8–9/12/2026) và mức tăng thực tế: 0,25 hay 0,5 điểm.",
   "Kiểm tra lãi suất khoản vay nhà kỳ tới; tính trước nếu tăng 1 điểm phần trăm (vay 2 tỷ: thêm 20 triệu mỗi năm).",
   "Nếu dùng vay ký quỹ: tự hỏi nếu cổ phiếu giảm 20% có bị bán giải chấp không; đọc " + L("ban-giai-chap-la-gi", "bán giải chấp là gì") + "."]],
 ["p", "<small>Nguồn: Hà Nội Mới 14/11/2026; Vietnam+ 11/11/2026; CafeF 12/11/2026; BSC Daily Review 30/12/2022. Bài chia sẻ kiến thức, không phải khuyến nghị.</small>"]],
 faq=[["Chỉ số DXY là gì?", "Là chỉ số đo giá trị đồng USD so với 6 đồng tiền lớn (euro, yen, bảng Anh, đô la Canada, krona Thuỵ Điển, franc Thuỵ Sĩ). Ngày 14/11/2026 DXY ở 103,41 điểm."],
      ["DXY tăng thì tỷ giá Việt Nam có tăng?", "Thường có áp lực tăng. Tuần 9–13/11/2026, DXY tăng 1,09% và giá bán USD ở Vietcombank tăng 130 đồng lên 25.910 đồng."],
      ["DXY tăng có làm chứng khoán Việt Nam giảm?", "Có thể qua kênh khối ngoại và lãi suất, nhưng không chắc chắn. Năm 2022 Fed tăng 7 lần và VN-Index giảm 32,8%; nhiều giai đoạn khác tác động nhẹ hơn."]],
 rel=["fed-tang-giam-lai-suat-tac-dong", "chung-khoan-my-giam-vn-index-co-giam-theo", "ban-giai-chap-la-gi"]))
if __name__ == '__main__':
    D = json.load(open(P, encoding='utf-8')); have = {x['slug'] for x in D}
    for b in B:
        txt = " ".join(re.sub('<[^>]+>', '', json.dumps(b['body'], ensure_ascii=False)).split()) + " ".join(a + b2 for a, b2 in b['faq'])
        print(b['slug'], b['slug'] in have, len(b['title']), len(b['desc']), len(txt.split()), [r for r in b['rel'] if r not in have])
    if '--ghi' in sys.argv:
        D += [b for b in B if b['slug'] not in have]
        json.dump(D, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
