# -*- coding: utf-8 -*-
# NV1 9/11/2026 – 3 bài F0 chuẩn mới (bai_seo_hay_hon_0811) + rút gọn 7 tiêu đề/mô tả. Chạy: CW=/tmp/cw python3 f0_2.py
import json
from hand2 import *
P = CW + '/_f0/bai.json'; L = json.load(open(P, encoding='utf-8')); S = {b['slug'] for b in L}
A = lambda s, t: '<a href="/f0/%s.html">%s</a>' % (s, t)
TEN = dict(DHG='Dược Hậu Giang', VCB='Vietcombank', HPG='Hòa Phát', SSI='Chứng khoán SSI', DIG='DIC Corp', NVL='Novaland')
NEW = []
# ---- 1. Độ biến động ----
NEW.append(dict(slug="do-bien-dong-co-phieu-la-gi", kw="độ biến động cổ phiếu là gì", grp=5,
 title="Độ biến động cổ phiếu là gì? Chia vốn theo rủi ro, ví dụ 6 mã",
 desc="Cùng 100 triệu, NVL dao động mạnh gấp %s lần DHG. Cách đo độ biến động, đặt điểm sai và chia tiền để mỗi mã sai chỉ mất 1%% danh mục." % p1(ratio),
 body=[["p", "Anh Tuấn, một nhân viên văn phòng ở Hà Nội, chia 600 triệu đều cho sáu mã, mỗi mã 100 triệu, và nghĩ như vậy là đã đa dạng hóa. Một tuần thị trường xấu, cả danh mục giảm, nhưng gần một nửa khoản mất đến từ hai mã bất động sản. Anh không chọn sai mã. Anh chỉ chia đều <b>tiền</b>, trong khi rủi ro của sáu mã không hề đều nhau. Theo giá đóng cửa điều chỉnh từ 10/2023 đến 6/11/2026, độ biến động năm của Novaland (NVL) khoảng %s%%, của Dược Hậu Giang (DHG) chỉ khoảng %s%%. Cùng 100 triệu, vị thế NVL dao động mạnh gấp khoảng %s lần." % (p1(V['NVL']), p1(V['DHG']), p1(ratio))],
  ["h2", "Độ biến động đo cái gì?"],
  ["p", "<b>Độ biến động</b> (volatility) đo mức giá một mã thường nhảy lên xuống. Cách tính: lấy phần trăm thay đổi giá mỗi phiên, tính độ lệch chuẩn của chuỗi đó, rồi nhân với căn bậc hai của 250 (số phiên một năm) để quy ra năm. Độ biến động năm 20% nghĩa là trong một năm bình thường, giá lệch khoảng 20% so với xu hướng là chuyện hay gặp. Nó không cho biết giá sẽ lên hay xuống, chỉ cho biết đường đi gập ghềnh cỡ nào. Khái niệm gần với nó là " + A("he-so-beta-la-gi", "hệ số beta") + ": beta đo mức đi theo thị trường, còn độ biến động đo tổng mức dao động, gồm cả phần riêng của doanh nghiệp."],
  ["h2", "Sáu mã thật dao động khác nhau thế nào?"],
  ["p", "Số liệu tính từ giá đóng cửa điều chỉnh trên HOSE, 27/10/2023–6/11/2026 (754 phiên). Cột cuối là số tiền nên đặt vào mỗi mã nếu danh mục 1 tỷ đồng và mỗi vị thế chỉ được làm mất tối đa 10 triệu (1%) khi chạm điểm sai:"],
  ["ul", ["<b>%s (%s)</b>: độ biến động năm %s%% · dao động 1 tháng khoảng %s%% · điểm sai khoảng %s%% · vị thế khoảng <b>%s triệu</b>" % (s, TEN[s], p1(V[s]), p1(VM[s]), p1(STOP[s]), vn(POS[s], 0)) for s in SY]],
  ["h2", "Tính từng bước như thế nào?"],
  ["ol", ["Chọn mức rủi ro mỗi lệnh: ví dụ 1% của 1 tỷ = 10 triệu (xem " + A("quy-tac-rui-ro-1-phan-tram", "quy tắc rủi ro 1%") + ").",
          "Quy độ biến động năm ra dao động một tháng: chia cho căn bậc hai của 12 (khoảng 3,46). Với DHG: %s%% ÷ 3,46 ≈ %s%%." % (p1(V['DHG']), p1(VM['DHG'])),
          "Đặt điểm sai bằng khoảng 2 lần dao động một tháng: DHG ≈ %s%%, NVL ≈ %s%%." % (p1(STOP['DHG']), p1(STOP['NVL'])),
          "Chia rủi ro cho khoảng cách điểm sai: DHG = 10 triệu ÷ %s%% ≈ %s triệu; NVL = 10 triệu ÷ %s%% ≈ %s triệu." % (p1(STOP['DHG']), vn(POS['DHG'], 0), p1(STOP['NVL']), vn(POS['NVL'], 0)),
          "So với trần tỷ trọng (ví dụ 20% danh mục = 200 triệu) và lấy số nhỏ hơn."]],
  ["p", "Kết quả: nếu cả DHG và NVL cùng chạm điểm sai, mỗi mã làm danh mục mất đúng khoảng 10 triệu. Đó là <b>chia đều rủi ro</b>, khác hẳn chia đều tiền. Cách đặt điểm sai chi tiết hơn có trong bài " + A("diem-sai-cua-lenh-mua-la-gi", "điểm sai của lệnh mua") + "."],
  ["h2", "Mã ít dao động có an toàn tuyệt đối không?"],
  ["p", "Không. Độ biến động đo quá khứ bình thường, không đo được cú sốc riêng. Lợi nhuận sau thuế công ty mẹ quý 3/2026 của DHG giảm khoảng 53%% so với cùng kỳ, dù DHG là mã ít dao động nhất trong sáu mã. Vietcombank có độ biến động năm khoảng %s%%, nhưng từ đỉnh khoảng 75,4 nghìn đồng (14/1/2026) vẫn về khoảng 53,5 nghìn (3/11/2026), giảm khoảng 29%%. Ít dao động hằng ngày chỉ có nghĩa là giảm từ từ, không có nghĩa là không giảm sâu. Vì vậy luôn cần trần tỷ trọng." % p1(V['VCB'])],
  ["h2", "Bẫy hay gặp"],
  ["ul", ["<b>Tính đúng vị thế nhưng không đặt điểm sai.</b> Bảng chia tiền chỉ có nghĩa khi điểm sai được thực hiện. Người mua DIG từ 27,41 nghìn (2/4/2024) mà không có điểm sai đã chứng kiến giá về khoảng 9,02 nghìn (5/10/2026).",
          "<b>Dùng vay ký quỹ.</b> Vay 1:1 làm mọi mức mất trong bảng nhân đôi trên vốn tự có (xem " + A("margin-la-gi", "margin là gì") + ").",
          "<b>Dời điểm sai ra xa khi giá tới gần.</b> NVL từng giảm khoảng 55,7% từ đỉnh khoảng 16,9 nghìn (6/12/2023) về khoảng 7,48 nghìn (9/4/2025). Mỗi lần dời điểm sai là một lần tăng rủi ro sau khi lệnh đã vào."]],
  ["h2", "Checklist anh chị tự làm được"],
  ["ul", ["Chọn mức rủi ro mỗi lệnh (0,5–2% danh mục) và ghi ra giấy.", "Tính độ biến động năm của mã (hoặc dùng mức dao động trung bình mỗi phiên × 16 làm ước lượng nhanh).", "Đổi ra khoảng cách điểm sai.", "Chia rủi ro cho khoảng cách để ra số tiền.", "Đối chiếu trần tỷ trọng 15–20%, lấy số nhỏ hơn.", "Cập nhật lại mỗi quý, cùng lúc đọc báo cáo tài chính."]],
  ["p", "Các con số trên chỉ minh họa cách tính, không phải khuyến nghị mua bán. Video giải thích cùng chủ đề sẽ có trên kênh YouTube Chứng Khoán Huy Nguyễn (series Quản trị vốn)."]],
 faq=[["Độ biến động bao nhiêu là cao?", "Với cổ phiếu Việt Nam, dưới khoảng 20%%/năm là thấp, 25–35%% là trung bình, trên 35%% là cao. VN-Index giai đoạn 10/2023–11/2026 khoảng %s%%." % p1(AS['vni']['vol'])],
      ["Tính độ biến động bằng Excel thế nào?", "Cột A là giá đóng cửa, cột B = A2/A1−1, rồi dùng STDEV.P cho cột B và nhân với SQRT(250)."],
      ["Có nên chỉ mua mã ít biến động?", "Không nhất thiết. Mã ít biến động vẫn có cú sốc riêng; điều quan trọng là mỗi vị thế được chia theo rủi ro và có trần tỷ trọng."]],
 rel=["quy-tac-rui-ro-1-phan-tram", "cach-tinh-khoi-luong-mua-theo-diem-cat-lo", "he-so-beta-la-gi", "diem-sai-cua-lenh-mua-la-gi"]))
# ---- 2. Ba lằn ranh đỏ ----
def rl(s): a, b, c = RL[s]; return a, b, c
NEW.append(dict(slug="ba-lan-ranh-do-bat-dong-san-la-gi", kw="ba lằn ranh đỏ bất động sản là gì", grp=5,
 title="Ba lằn ranh đỏ là gì? Đo nợ 5 doanh nghiệp bất động sản Việt Nam",
 desc="Ba lằn ranh đỏ làm Evergrande vỡ nợ: nợ/tài sản, nợ vay ròng/vốn, tiền/nợ ngắn hạn. Cách tính từ BCTC Q3/2026 với NLG, KDH, DXG, PDR, NVL.",
 body=[["p", "Giữa năm 2021, Evergrande, tập đoàn bất động sản lớn của Trung Quốc, có tổng nợ phải trả khoảng 1.970 tỷ nhân dân tệ, hơn 300 tỷ USD. Cú sụp không bắt đầu bằng một vụ bê bối, mà bằng ba con số cơ quan quản lý Trung Quốc đặt ra từ tháng 8/2020, thường gọi là <b>ba lằn ranh đỏ</b>. Evergrande vượt cả ba, bị chặn tăng nợ vay, rồi lỡ hạn trả lãi trái phiếu năm 2021. Ba lằn ranh không phải quy định ở Việt Nam, nhưng là một thước đo rất gọn để anh chị tự kiểm tra sức khỏe nợ của doanh nghiệp bất động sản trên sàn."],
  ["h2", "Ba lằn ranh gồm những gì?"],
  ["ol", ["<b>Lằn ranh 1</b>: (Nợ phải trả − Người mua trả tiền trước) ÷ (Tổng tài sản − Người mua trả tiền trước) không quá 70%.",
          "<b>Lằn ranh 2</b>: Nợ vay ròng (vay ngắn hạn + vay dài hạn − tiền) ÷ Vốn chủ sở hữu không quá 100%.",
          "<b>Lằn ranh 3</b>: Tiền và tương đương tiền ÷ Vay ngắn hạn lớn hơn 1 lần."]],
  ["p", "Vì sao trừ tiền khách trả trước? Đó là tiền khách đặt mua nhà hình thành trong tương lai, ghi vào nợ vì doanh nghiệp còn nghĩa vụ giao nhà, nhưng không phải nợ vay phải trả lãi. Xem thêm " + A("no-vay-tren-von-chu-so-huu", "nợ vay trên vốn chủ sở hữu") + " và " + A("vay-ngan-han-va-dai-han-la-gi", "vay ngắn hạn và dài hạn") + "."],
  ["h2", "Tính thử từng bước với NLG"],
  ["p", "Số liệu bảng cân đối kế toán hợp nhất Nam Long (NLG) ngày 30/9/2026, đơn vị tỷ đồng. Lằn ranh 1 ra khoảng %s%%. Lằn ranh 2: vay ngắn hạn cộng vay dài hạn trừ tiền, chia vốn chủ sở hữu, ra khoảng %s%%. Lằn ranh 3: tiền chia vay ngắn hạn, khoảng %s lần. Cả ba đều nằm trong vùng an toàn." % (p1(rl('NLG')[0]), vn(rl('NLG')[1], 0), p2(rl('NLG')[2]))],
  ["h2", "Năm doanh nghiệp so với nhau ra sao?"],
  ["p", "Số liệu BCTC quý 3/2026 (30/9/2026), tính của Chứng Khoán Huy Nguyễn:"],
  ["ul", ["<b>%s</b>: lằn ranh 1 ≈ %s%% · lằn ranh 2 ≈ %s%% · lằn ranh 3 ≈ %s lần" % (s, p1(rl(s)[0]), vn(rl(s)[1], 0), p2(rl(s)[2])) for s in ['NLG', 'KDH', 'DXG', 'PDR', 'NVL']]],
  ["p", "NLG, KDH, DXG nằm trong cả ba ngưỡng tham khảo. PDR và NVL có nợ vay ròng vượt 100% vốn chủ sở hữu và tiền mặt thấp hơn nhiều so với nợ vay ngắn hạn. Điều này <b>không</b> có nghĩa doanh nghiệp sẽ vỡ nợ, vì còn phụ thuộc kế hoạch bán hàng, tái cấu trúc nợ và chính sách; nó chỉ cho biết biên an toàn mỏng hơn và cần đọc kỹ thuyết minh vay, lịch đáo hạn trái phiếu."],
  ["h2", "Evergrande đã đi đến đâu?"],
  ["p", "Ngày 9/12/2021, Fitch hạ Evergrande xuống mức vỡ nợ có giới hạn. Tháng 7/2023, công ty công bố lỗ cộng dồn 2021–2022 khoảng 582 tỷ nhân dân tệ. Ngày 29/1/2024, tòa án Hồng Kông ra lệnh thanh lý. Tháng 3/2024, cơ quan quản lý chứng khoán Trung Quốc kết luận đơn vị chính của tập đoàn khai khống doanh thu khoảng 564 tỷ nhân dân tệ trong 2019–2020. Cổ phiếu mất hơn 99% so với đỉnh năm 2017 và bị hủy niêm yết năm 2025. Cổ đông đứng cuối hàng khi doanh nghiệp vỡ nợ."],
  ["h2", "Bẫy hay gặp"],
  ["ul", ["<b>Nhìn tổng tài sản lớn rồi yên tâm.</b> Quỹ đất ghi theo giá gốc, chỉ thành tiền khi có người mua; nợ thì ghi đúng số phải trả.", "<b>Chỉ xem nợ vay, bỏ qua lịch đáo hạn.</b> Lằn ranh 3 của PDR ≈ %s lần, NVL ≈ %s lần: tiền mặt không đủ trả vay ngắn hạn nếu không đảo nợ được." % (p2(rl('PDR')[2]), p2(rl('NVL')[2])), "<b>Tin rằng quá lớn để sụp.</b> Evergrande từng có hơn 1.300 dự án ở hơn 280 thành phố."]],
  ["h2", "Checklist anh chị tự làm được"],
  ["ul", ["Mở bảng cân đối quý mới nhất, lấy 6 dòng: nợ phải trả, người mua trả tiền trước, tổng tài sản, vay ngắn hạn, vay dài hạn, tiền.", "Tính ba lằn ranh như trên.", "So với quý cùng kỳ năm trước: đang tốt lên hay xấu đi?", "Đọc thuyết minh vay: khoản nào đáo hạn trong 12 tháng.", "Xem dòng tiền kinh doanh (" + A("dong-tien-kinh-doanh-la-gi", "CFO") + ") có dương không.", "Đọc ý kiến kiểm toán (" + A("kiem-toan-ngoai-tru-la-gi", "ngoại trừ") + " hay chấp nhận toàn phần)."]],
  ["p", "Bài viết chỉ minh họa cách đọc số liệu, không phải khuyến nghị mua bán. Video kể lại câu chuyện Evergrande có trên kênh YouTube phụ Lịch sử & bài học thị trường."]],
 faq=[["Ba lằn ranh đỏ có áp dụng ở Việt Nam không?", "Không. Đây là quy định của Trung Quốc từ 8/2020; ở Việt Nam chỉ nên dùng như thước đo tham khảo."],
      ["Người mua trả tiền trước nằm ở đâu trong BCTC?", "Ở phần nợ ngắn hạn (và dài hạn nếu có) của bảng cân đối kế toán, dòng 'Người mua trả tiền trước'."],
      ["Vượt lằn ranh có nghĩa là sắp vỡ nợ?", "Không chắc chắn. Nó báo biên an toàn mỏng; cần đọc thêm lịch đáo hạn, dòng tiền và khả năng bán hàng."]],
 rel=["doc-bctc-cong-ty-bat-dong-san", "no-vay-tren-von-chu-so-huu", "vay-ngan-han-va-dai-han-la-gi", "dong-tien-kinh-doanh-la-gi"]))
# ---- 3. Phiên giảm mạnh ----
n20 = sum(1 for w in W10 if w['f20'] > 0)
NEW.append(dict(slug="phien-giam-manh-nhat-vn-index-nen-lam-gi", kw="thị trường giảm mạnh nên làm gì", grp=7,
 title="VN-Index giảm mạnh nên làm gì? 10 phiên giảm sâu nhất 3 năm qua",
 desc="10 phiên VN-Index giảm sâu nhất 10/2023–11/2026: 5, 20, 60 phiên sau ra sao, vì sao thống kê đẹp vẫn không phải lời khuyên, và checklist 5 dòng.",
 body=[["p", "Ngày %s, VN-Index giảm %s%% chỉ trong một phiên, về khoảng %s điểm. Nhiều nhà đầu tư bán tháo ngay chiều hôm đó. Hai phiên sau, chỉ số giảm thêm. Nhưng sáu mươi phiên sau, VN-Index cao hơn mức đóng cửa ngày giảm khoảng %s%%. Em lấy mười phiên giảm mạnh nhất trong 754 phiên từ 27/10/2023 tới 6/11/2026 để xem điều gì thường xảy ra sau đó." % (fd(W10[0]['d']), p2(abs(W10[0]['r'])), vn(W10[0]['c'], 0), p1(W10[0]['f60']))],
  ["h2", "Mười phiên giảm sâu nhất là những phiên nào?"],
  ["ul", ["<b>%s</b>: %s%% · đóng cửa ≈ %s · 5 phiên sau %s · 20 phiên sau %s · 60 phiên sau %s" % (fd(w['d']), p2(w['r']), vn(w['c'], 0), pct(w['f5']), pct(w['f20']), pct(w['f60'])) for w in W10]],
  ["p", "Nguồn: VN-Index đóng cửa ngày, HOSE; tính của Chứng Khoán Huy Nguyễn. Kết quả: 5 phiên sau có %d/10 lần chỉ số còn thấp hơn; 20 phiên sau %d/10 lần cao hơn; 60 phiên sau %d/10 lần cao hơn." % (n5, n20, n60)],
  ["h2", "Vì sao con số đẹp này không phải lời khuyên?"],
  ["p", "Ba năm này là giai đoạn VN-Index đi lên, từ khoảng 1.061 lên khoảng 1.725 điểm, có lúc khoảng 1.928 điểm. Trong thị trường đi lên, cú giảm dễ được lấp lại. Năm 2022 không có trong mẫu: khi đó VN-Index giảm từ vùng khoảng 1.500 về dưới 900 điểm, và nhiều phiên giảm mạnh được nối tiếp bằng những phiên giảm khác trong nhiều tháng (xem " + A("quan-tri-rui-ro-khi-thi-truong-giam-manh", "quản trị rủi ro khi thị trường giảm mạnh") + "). Mười quan sát là quá ít để kết luận chắc chắn. Thống kê ba năm giống dự báo thời tiết mùa khô: rất đúng, cho tới khi mùa mưa đến. Vì vậy, điều đáng học từ bảng trên không phải là cứ giảm là mua, mà là quyết định trong phiên giảm mạnh nên được viết sẵn từ lúc bình tĩnh, và không để mình rơi vào thế buộc phải bán."],
  ["h2", "Điều gì phân biệt cú giảm sẽ hồi và cú giảm kéo dài?"],
  ["ol", ["Lợi nhuận doanh nghiệp đang tăng hay giảm. Năm 2025–2026, lợi nhuận nhiều ngân hàng tăng hai con số (ví dụ CTG lũy kế 9 tháng 2026 tăng khoảng 33,8%).", "Lãi suất trong nước đang đi lên hay đi xuống.", "Cú giảm đến từ bên ngoài (thuế quan tháng 4/2025, chứng khoán Mỹ giảm) hay từ vấn đề nội tại (nợ, thanh khoản ngân hàng, trái phiếu doanh nghiệp)."]],
  ["h2", "Bẫy hay gặp"],
  ["ul", ["<b>Bán toàn bộ vì sợ</b>, rồi mua lại ở giá cao hơn: ai bán ngày %s rồi mua lại 20 phiên sau phải trả cao hơn khoảng %s%%." % (fd(W10[9]['d']), p1(W10[9]['f20'])),
          "<b>Dồn toàn bộ tiền mặt ngay phiên đầu</b>: sau phiên %s, chỉ số còn giảm thêm khoảng %s%% trong 5 phiên." % (fd(W10[4]['d']), p1(abs(W10[4]['f5']))),
          "<b>Dùng margin cao</b>: tài khoản sát ngưỡng bị bán giải chấp trước khi kịp thấy cú hồi (xem " + A("ban-giai-chap-la-gi", "bán giải chấp là gì") + ")."]],
  ["h2", "Checklist anh chị tự làm được"],
  ["ul", ["Tỷ lệ vay ký quỹ có an toàn nếu chỉ số giảm thêm 10%?", "Tiền mặt dự phòng chia làm 3 phần, mỗi phần gắn với một mốc giảm.", "Danh sách chờ 3–5 mã đã đọc kỹ lợi nhuận 8 quý.", "Cú giảm do bên ngoài hay nội tại?", "Không đặt lệnh trong 30 phút đầu sau khi đọc tin xấu."]],
  ["p", "Quá khứ không bảo đảm cho tương lai; bài viết không phải khuyến nghị mua bán. Video cùng chủ đề có trong series Bài học lịch sử trên kênh YouTube Chứng Khoán Huy Nguyễn."]],
 faq=[["Thị trường giảm mạnh có nên bán hết không?", "Quyết định nên dựa trên kế hoạch viết trước và kết quả kinh doanh từng mã, không dựa trên cảm xúc của phiên giảm."],
      ["Phiên giảm mạnh nhất của VN-Index 3 năm qua là ngày nào?", "Theo giá đóng cửa 10/2023–11/2026, là ngày %s, giảm khoảng %s%%." % (fd(W10[0]['d']), p2(abs(W10[0]['r'])))],
      ["Sau phiên giảm mạnh bao lâu thì thị trường hồi?", "Không có quy luật cố định. Trong mẫu 3 năm, 60 phiên sau %d/10 lần chỉ số cao hơn, nhưng năm 2022 cho kết quả khác hẳn." % n60]],
 rel=["quan-tri-rui-ro-khi-thi-truong-giam-manh", "ke-hoach-khi-vn-index-giam-20-phan-tram", "co-nen-mua-co-phieu-khi-thi-truong-giam", "tam-ly-fomo-va-hoang-loan"]))
FIX = {'rut-tien-hang-loat-ngan-hang-la-gi': ("Rút tiền hàng loạt là gì? Từ 1907 đến Silicon Valley Bank 2023", None),
       'stress-test-danh-muc-la-gi': ("Stress test danh mục: thị trường giảm 20–30%, còn bao nhiêu?", None),
       'da-dang-hoa-gia-la-gi': ("Đa dạng hóa giả là gì? 5 ngân hàng không phải 5 rủi ro", None),
       'ty-trong-vang-bitcoin-trong-danh-muc': ("Nên để bao nhiêu % vàng, Bitcoin trong danh mục?", None),
       'ty-trong-theo-dong-luc-rui-ro': ("Phân bổ tỷ trọng theo động lực rủi ro: bảng 4 cột", None),
       'diem-sai-cua-lenh-mua-la-gi': ("Điểm sai của lệnh mua là gì? 3 kiểu cho nhà đầu tư", None),
       'beta-danh-muc-la-gi': ("Beta danh mục là gì? Ước lượng mức giảm khi VN-Index giảm", None)}
n = 0
for b in L:
    if b['slug'] in FIX:
        b['title'] = FIX[b['slug']][0]
        if len(b['desc']) > 155: b['desc'] = b['desc'][:152].rsplit(' ', 1)[0].rstrip(',.;:–') + '.'
        n += 1
for x in NEW:
    assert x['slug'] not in S, x['slug']
    assert len(x['title']) <= 65 and len(x['desc']) <= 155, (x['slug'], len(x['title']), len(x['desc']))
    L.append(x)
    w = sum(len(str(c).split()) if isinstance(c, str) else sum(len(y.split()) for y in c) for _, c in x['body']) + sum(len((a + ' ' + q).split()) for a, q in x['faq'])
    print(x['slug'], len(x['title']), len(x['desc']), 'chữ', w)
print('sua', n, [(s, len(b['title']), len(b['desc'])) for b in L for s in FIX if b['slug'] == s])
json.dump(L, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
