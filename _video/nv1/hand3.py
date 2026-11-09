# -*- coding: utf-8 -*-
# NV1 10/11/2026 – kịch bản viết tay lô 20261110_0036: CH2911B (giữ tiền mặt 70/30), CH3011B (bẫy cổ tức cao),
# LST_1811A (LTCM 1998), Y3_1811A (S&P 500 và VN-Index). Số liệu tính từ data/c/*.bin, data/wm.bin, data/fund.bin, data/kqkd.bin (tới 9/11/2026).
import datetime as _D, statistics as _st
from lib import *
from hand import T as _T, END as _END
def T(cap, say, *a, **kw): return _T(cap, say.replace('%%', '%'), *a, **kw)
def END(cap, say): return _END(cap, say.replace('%%', '%'))
H3 = {}
CH = lambda s: {'sym': s + 'W', 'tf': 'W', 'weeks': 52, 'circles': None}
def p1(x): return vn(x, 1)
def p2(x): return vn(x, 2)
def fd(d): return "%d/%d/%s" % (int(d[8:]), int(d[5:7]), d[:4])

# ---------- tính: danh mục 100% / 70-30 / 50-50 theo VN-Index, tiền mặt 5%/năm, cân lại mỗi quý ----------
_c = [(x[0], x[4] / 100) for x in daily('VNINDEX')]
def _sim(eq):
    E, C, pk, mdd, vals = eq, 1 - eq, 1, 0, []
    for i in range(1, len(_c)):
        E *= _c[i][1] / _c[i - 1][1]; C *= 1 + 0.05 / 252
        if _c[i][0][5:7] != _c[i - 1][0][5:7] and _c[i][0][5:7] in ('01', '04', '07', '10'): t = E + C; E, C = t * eq, t * (1 - eq)
        t = E + C; pk = max(pk, t); mdd = max(mdd, 1 - t / pk); vals.append((_c[i][0], t))
    seg = [x for x in vals if '2025-03-25' <= x[0] <= '2025-04-15']
    return dict(ret=(E + C - 1) * 100, mdd=mdd * 100, apr=(1 - min(x[1] for x in seg) / seg[0][1]) * 100, end=E + C)
P = {e: _sim(e) for e in (1, .7, .5)}
A, B, C5 = P[1], P[.7], P[.5]
_pk = max(_c, key=lambda x: x[1])

H3['CH2911B'] = dict(
 title="Quản trị vốn | Giữ 30%% tiền mặt: lãi 3 năm %s%% thay vì %s%%, nhưng cú sụt 4/2025 chỉ còn %s%% – đổi lấy giấc ngủ có đáng?" % (p1(B['ret']), p1(A['ret']), p1(B['apr'])),
 hook=["GIỮ TIỀN MẶT", "MẤT LÃI %s%%?" % p1(A['ret'] - B['ret'])], badge="QUẢN TRỊ VỐN", seri="Quản trị vốn", nhac=None,
 nguon="Nguồn: VN-Index đóng cửa ngày (HOSE) 27/10/2023–9/11/2026; giả định tiền mặt sinh lãi 5%/năm, cân lại tỷ trọng đầu mỗi quý; tính toán của Chứng Khoán Huy Nguyễn.",
 tags=["quản trị vốn", "tỷ trọng tiền mặt", "phân bổ tài sản", "VN-Index", "rủi ro danh mục", "cân bằng danh mục"],
 fb=["100%% theo VN-Index: 3 năm +%s%%, cú sụt sâu nhất %s%%" % (p1(A['ret']), p1(A['mdd'])),
     "70%% cổ phiếu + 30%% tiền mặt: +%s%%, sụt sâu nhất %s%%; 50/50: +%s%%, sụt %s%%" % (p1(B['ret']), p1(B['mdd']), p1(C5['ret']), p1(C5['mdd'])),
     "Đầu tháng 4/2025: danh mục 1 tỷ đồng 100%% cổ phiếu sụt khoảng %s triệu, 70/30 sụt khoảng %s triệu" % (vn(A['apr'] * 10, 0), vn(B['apr'] * 10, 0))],
 q="Danh mục của anh chị hiện đang giữ bao nhiêu phần trăm tiền mặt, và con số đó được chọn từ trước hay tùy cảm giác từng tuần?",
 S=[
 T(("GIỮ TIỀN MẶT", "MẤT LÃI %s%%?" % p1(A['ret'] - B['ret'])),
   f"Ba năm qua, từ cuối tháng 10/2023 tới ngày 9/11/2026, VN-Index đi từ khoảng 1.060 điểm lên khoảng 1.714 điểm. Một người để toàn bộ tiền theo chỉ số có lãi khoảng {p1(A['ret'])}%. Một người khác luôn giữ 30% tiền mặt chỉ lãi khoảng {p1(B['ret'])}%. Nghe thì người giữ tiền mặt thua. Nhưng đầu tháng 4/2025, danh mục của người thứ nhất sụt khoảng {p1(A['apr'])}% chỉ trong vài phiên, còn người thứ hai sụt khoảng {p1(B['apr'])}%. Câu hỏi của video hôm nay: giữ tiền mặt là một khoản phí, hay là một hợp đồng bảo hiểm? Xem hết video, anh chị sẽ có một cách chọn tỷ lệ tiền mặt phù hợp với chính mình.",
   "cash and stock chart", "Mở đầu", moc=True, k='hook', chart=CH('VNINDEX')),
 T(("CÁCH EM", "LÀM PHÉP THỬ"),
   "Em làm một phép thử đơn giản để ai cũng kiểm tra lại được. Ba danh mục, cùng bắt đầu ngày 27/10/2023. Danh mục thứ nhất: 100% đi theo VN-Index. Danh mục thứ hai: 70% theo VN-Index, 30% tiền mặt. Danh mục thứ ba: một nửa cổ phiếu, một nửa tiền mặt. Phần tiền mặt được giả định sinh lãi 5% một năm, gần mức tiền gửi kỳ hạn dài. Đầu mỗi quý, danh mục được đưa về đúng tỷ lệ ban đầu: cổ phiếu tăng nhiều thì bán bớt, cổ phiếu giảm thì mua thêm. Đây không phải gợi ý một con số cố định, mà là cách để nhìn thấy cái giá và cái lợi của tiền mặt bằng số liệu thật.",
   "spreadsheet calculator", "Chương 1 – Phép thử"),
 T(("BA NĂM", "BA KẾT QUẢ"),
   f"Kết quả sau ba năm. Danh mục 100% cổ phiếu tăng khoảng {p1(A['ret'])}%. Danh mục 70 cổ phiếu, 30 tiền mặt tăng khoảng {p1(B['ret'])}%. Danh mục 50 trên 50 tăng khoảng {p1(C5['ret'])}%. Nếu bắt đầu với 1 tỷ đồng, ba con số này tương đương khoảng {vn(A['end'] * 1000, 0)} triệu, {vn(B['end'] * 1000, 0)} triệu và {vn(C5['end'] * 1000, 0)} triệu đồng. Trong một giai đoạn thị trường đi lên, càng nhiều tiền mặt thì lãi càng ít. Đó là cái giá thật, không cần né tránh. Nếu chỉ nhìn bảng này, ai cũng sẽ chọn 100% cổ phiếu.",
   "money growth chart", "Chương 2 – Kết quả"),
 T(("CÚ SỤT", "SÂU NHẤT"),
   f"Nhưng bảng kết quả cuối kỳ giấu đi đoạn đường ở giữa. Cú sụt sâu nhất từ đỉnh của danh mục 100% cổ phiếu là khoảng {p1(A['mdd'])}%. Với danh mục 70 trên 30, cú sụt sâu nhất chỉ khoảng {p1(B['mdd'])}%. Với danh mục 50 trên 50, khoảng {p1(C5['mdd'])}%. Đầu tháng 4/2025, khi thị trường thế giới chao đảo vì thuế quan, danh mục 1 tỷ đồng toàn cổ phiếu mất tạm thời khoảng {vn(A['apr'] * 10, 0)} triệu đồng. Danh mục giữ 30% tiền mặt mất khoảng {vn(B['apr'] * 10, 0)} triệu. Khoảng chênh đó chính là thứ quyết định một người có bình tĩnh hay không.",
   "stock market crash screen", "Chương 3 – Cú sụt"),
 T(("ĐIỀU BẤT NGỜ", "TIỀN MẶT LÀ ĐẠN"),
   "Điều bất ngờ nằm ở việc cân lại tỷ trọng. Đầu quý 2/2025, ngay sau cú giảm, danh mục 70 trên 30 có cổ phiếu chiếm ít hơn 70%. Quy tắc buộc người đó lấy tiền mặt mua thêm cổ phiếu, đúng lúc mọi người đang sợ. Ngược lại, khi VN-Index lên vùng khoảng 1.928 điểm ngày 18/5/2026, quy tắc buộc người đó bán bớt. Tiền mặt không chỉ là chỗ trốn. Nó là viên đạn để dùng khi giá rẻ, và là chỗ cất lãi khi giá đắt. Người giữ 100% cổ phiếu không có viên đạn nào trong tay lúc thị trường giảm.",
   "chess strategy board", "Chương 4 – Tiền mặt là đạn"),
 T(("CẢM XÚC", "MỚI LÀ CHI PHÍ LỚN"),
   "Trên giấy, danh mục 100% cổ phiếu thắng. Ngoài đời, rất nhiều người không giữ được nó tới cuối. Khi tài khoản 1 tỷ mất gần 180 triệu trong vài phiên, câu hỏi trong đầu không còn là lợi nhuận ba năm, mà là còn mất bao nhiêu nữa. Nhiều người bán ra đúng vùng đáy, rồi đứng ngoài nhìn thị trường hồi lại. Khi đó, kết quả thật của họ còn tệ hơn cả danh mục 50 trên 50. Ví von đời thường: chiếc xe chạy nhanh nhất không có ích nếu người lái sợ quá mà bỏ cuộc giữa đường.",
   "worried investor", "Chương 5 – Cảm xúc"),
 T(("CHỌN TỶ LỆ", "THEO 3 CÂU HỎI"),
   "Vậy chọn tỷ lệ tiền mặt thế nào? Em gợi ý ba câu hỏi. Một, khoản tiền này bao lâu nữa anh chị cần dùng. Dưới hai năm thì tiền mặt nên nhiều hơn, vì không có thời gian chờ thị trường hồi. Hai, anh chị chịu được mức sụt bao nhiêu mà không mất ngủ. Nếu con số là 10%, danh mục toàn cổ phiếu từng sụt khoảng 18% trong ba năm qua là quá sức. Ba, thu nhập hằng tháng có ổn định không. Thu nhập càng bấp bênh, tiền mặt dự phòng càng phải dày.",
   "family budget planning", "Chương 6 – Chọn tỷ lệ"),
 T(("QUỸ DỰ PHÒNG", "KHÁC TIỀN CHỜ MUA"),
   "Một điểm hay bị nhầm. Quỹ dự phòng gia đình, thường từ ba đến sáu tháng chi tiêu, không nằm trong phép tính tiền mặt của danh mục. Đó là tiền để sống khi có việc đột xuất, không phải tiền để chờ mua cổ phiếu. Nếu gộp chung, đến lúc thị trường giảm mà nhà lại cần tiền, anh chị sẽ phải bán cổ phiếu đúng lúc giá thấp. Em hay chia làm hai túi: túi dự phòng không bao giờ đụng tới, và túi tiền mặt của danh mục, dùng theo quy tắc cân lại mỗi quý.",
   "two piggy banks", "Chương 7 – Hai túi tiền"),
 T(("BẪY HAY GẶP", "BA KIỂU"),
   "Ba kiểu bẫy hay gặp. Một, giữ tiền mặt nhưng không có quy tắc dùng, nên thị trường giảm thì sợ không dám mua, thị trường tăng thì sốt ruột mua đuổi ở giá cao. Hai, dùng vay ký quỹ trong khi vẫn tự nhủ mình đang giữ tiền mặt; thực tế tỷ lệ cổ phiếu đã vượt 100%. Ba, đổi tỷ lệ theo tin tức mỗi tuần, hôm nay 20%, tuần sau 0%. Cả ba kiểu đều biến tiền mặt từ tấm đệm thành một khoản đặt cược mới.",
   "trap warning sign", "Chương 8 – Bẫy hay gặp"),
 T(("CHECKLIST", "NĂM DÒNG"),
   "Checklist năm dòng anh chị tự làm được trong tối nay. Một, tách quỹ dự phòng gia đình ra khỏi tài khoản chứng khoán. Hai, viết ra mức sụt tối đa mình chịu được, tính bằng tiền chứ không chỉ bằng phần trăm. Ba, chọn tỷ lệ tiền mặt của danh mục và ghi ngày cân lại, ví dụ ngày làm việc đầu tiên mỗi quý. Bốn, không dùng vay ký quỹ trong lúc vẫn tính là đang giữ tiền mặt. Năm, mỗi năm xem lại tỷ lệ một lần, khi hoàn cảnh gia đình thay đổi.",
   "checklist clipboard", "Chương 9 – Checklist"),
 END(("GIỮ TIỀN MẶT", "LÀ PHÍ HAY BẢO HIỂM?"),
   "Số liệu VN-Index từ 27/10/2023 đến 9/11/2026, phép thử giả định, quá khứ không bảo đảm cho tương lai. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Danh mục của anh chị hiện đang giữ bao nhiêu phần trăm tiền mặt, và con số đó được chọn từ trước hay tùy cảm giác từng tuần?")])
H3['CH2911B']['hook'] = ["GIỮ TIỀN MẶT", "MẤT LÃI %s%%?" % p1(A['ret'] - B['ret'])]

# ---------- CH3011B: bẫy cổ tức cao ----------
def _f(s): return fund(s)
def _q(s): return KQ[s]['info']
Y = {s: dict(dy=_f(s)['dy'], h52=_f(s)['h52'], l52=_f(s)['l52'], c=close(s), pe=_f(s)['pe']) for s in ['PNJ', 'DHG', 'DPM', 'VNM', 'LPB']}
for s, v in Y.items(): v['tu_dinh'] = (1 - v['c'] / v['h52']) * 100; v['cash'] = v['dy'] / 100 * v['c'] * 1000
H3['CH3011B'] = dict(
 title="Định giá | Cổ tức 10%%/năm là món hời? PNJ %s%%, DHG %s%%, DPM %s%%: khi tỷ suất cao vì giá rơi và lợi nhuận giảm" % (p2(Y['PNJ']['dy']), p2(Y['DHG']['dy']), p2(Y['DPM']['dy'])),
 hook=["CỔ TỨC 10%?", "GIÁ ĐÃ −%s%%" % p1(Y['PNJ']['tu_dinh'])], badge="ĐỊNH GIÁ", seri="Định giá", nhac=None,
 nguon="Nguồn: tỷ suất cổ tức, giá, đỉnh/đáy 52 tuần theo dữ liệu thị trường ngày 9/11/2026; kết quả kinh doanh quý 3/2026 từ báo cáo tài chính các doanh nghiệp; tổng hợp của Chứng Khoán Huy Nguyễn.",
 tags=["tỷ suất cổ tức", "bẫy cổ tức", "cổ phiếu cổ tức cao", "PNJ", "DHG", "VNM", "định giá cổ phiếu"],
 fb=["PNJ: tỷ suất cổ tức %s%% nhưng giá %s nghìn, thấp hơn đỉnh 52 tuần khoảng %s%%; quý 3/2026 lỗ khoảng 257 tỷ" % (p2(Y['PNJ']['dy']), p1(Y['PNJ']['c']), p1(Y['PNJ']['tu_dinh'])),
     "DHG %s%%: lãi quý 3 −53,0%%; DPM %s%%: lãi quý 3 −82,9%%" % (p2(Y['DHG']['dy']), p2(Y['DPM']['dy'])),
     "VNM %s%% (lãi quý 3 +17,3%%), LPB %s%% (+28,9%%): cùng cổ tức cao nhưng câu chuyện khác" % (p2(Y['VNM']['dy']), p2(Y['LPB']['dy']))],
 q="Khi thấy một mã có tỷ suất cổ tức trên 10%, anh chị kiểm tra điều gì đầu tiên: giá đã giảm bao nhiêu, hay lợi nhuận quý gần nhất?",
 S=[
 T(("CỔ TỨC 10%?", "GIÁ ĐÃ −%s%%" % p1(Y['PNJ']['tu_dinh'])),
   f"Ngày 9/11/2026, bảng dữ liệu cho thấy cổ phiếu PNJ có tỷ suất cổ tức khoảng {p2(Y['PNJ']['dy'])}%, cao gấp đôi lãi tiền gửi. Nhìn con số đó, nhiều người nghĩ ngay: mua vào, mỗi năm nhận hơn 10%, còn gì bằng. Nhưng cùng ngày, giá PNJ chỉ còn khoảng {p1(Y['PNJ']['c'])} nghìn đồng, thấp hơn đỉnh 52 tuần khoảng {p1(Y['PNJ']['tu_dinh'])}%. Và quý 3/2026, công ty lỗ khoảng 257 tỷ đồng. Tỷ suất cổ tức cao lên không phải vì doanh nghiệp trả nhiều hơn, mà vì giá rơi. Xem hết video, anh chị sẽ biết cách phân biệt cổ tức cao thật và cổ tức cao do bẫy.",
   "jewelry store", "Mở đầu", moc=True, k='hook', chart=CH('PNJ')),
 T(("TỶ SUẤT CỔ TỨC", "TÍNH THẾ NÀO?"),
   f"Tỷ suất cổ tức bằng cổ tức tiền mặt mỗi cổ phiếu chia cho giá cổ phiếu. Với PNJ, {p2(Y['PNJ']['dy'])}% nhân với giá khoảng {p1(Y['PNJ']['c'])} nghìn đồng cho ra khoảng {vn(Y['PNJ']['cash'], 0)} đồng mỗi cổ phiếu. Đó là cổ tức đã trả trong quá khứ. Điểm mấu chốt nằm ở chữ quá khứ. Phần tử số là tiền doanh nghiệp đã trả khi còn lãi tốt. Phần mẫu số là giá hôm nay, khi thị trường đã biết lợi nhuận giảm. Mẫu số co lại thì tỷ số phình ra. Con số đẹp đó chưa nói gì về khoản cổ tức năm tới.",
   "calculator coins", "Chương 1 – Công thức"),
 T(("PNJ", "LỢI NHUẬN ĐI ĐÂU?"),
   f"Kết quả kinh doanh của PNJ quý 3/2026: doanh thu thuần khoảng 6.995 tỷ đồng, giảm khoảng 14,0% so với cùng kỳ; lợi nhuận sau thuế công ty mẹ chuyển từ lãi sang lỗ khoảng 257 tỷ đồng. Lũy kế chín tháng, lợi nhuận còn khoảng 472 tỷ, giảm khoảng 70,7%. Hệ số P trên E khoảng {p2(Y['PNJ']['pe'])} lần trông rất rẻ, nhưng nó vẫn tính cả những quý lãi tốt của năm trước. Khi lợi nhuận giảm mạnh như vậy, khả năng duy trì mức cổ tức cũ là một câu hỏi lớn, và câu trả lời chỉ có khi hội đồng quản trị công bố.",
   "gold jewelry display", "Chương 2 – PNJ"),
 T(("DHG VÀ DPM", "CÙNG MỘT KIỂU"),
   f"PNJ không phải trường hợp duy nhất. Dược Hậu Giang có tỷ suất cổ tức khoảng {p2(Y['DHG']['dy'])}%, nhưng lợi nhuận quý 3/2026 chỉ khoảng 98 tỷ đồng, giảm khoảng 53,0%. Đạm Phú Mỹ có tỷ suất khoảng {p2(Y['DPM']['dy'])}%, lợi nhuận quý 3 chỉ khoảng 40 tỷ, giảm khoảng 82,9%; giá khoảng {p1(Y['DPM']['c'])} nghìn, sát đáy 52 tuần. Ba mã, ba ngành khác nhau, chung một điểm: tỷ suất cổ tức cao xuất hiện cùng lúc với lợi nhuận đi xuống. Đó là kiểu mà giới đầu tư gọi là bẫy cổ tức.",
   "pharmacy medicine", "Chương 3 – Cùng một kiểu"),
 T(("VNM VÀ LPB", "CÂU CHUYỆN KHÁC"),
   f"Nhưng cổ tức cao không phải lúc nào cũng là bẫy. Vinamilk có tỷ suất khoảng {p2(Y['VNM']['dy'])}%, và lợi nhuận quý 3/2026 khoảng 2.964 tỷ đồng, tăng khoảng 17,3%. LPBank có tỷ suất khoảng {p2(Y['LPB']['dy'])}%, lợi nhuận quý 3 khoảng 3.562 tỷ, tăng khoảng 28,9%. Ở hai mã này, lợi nhuận vẫn đi lên, nên nguồn trả cổ tức còn nguyên. Giá thấp hơn đỉnh 52 tuần là chuyện của tâm lý thị trường, còn khả năng trả cổ tức là chuyện của báo cáo tài chính. Hai chuyện này phải xem tách bạch.",
   "dairy milk factory", "Chương 4 – Cổ tức cao thật"),
 T(("BA CÂU HỎI", "TRƯỚC KHI TIN"),
   "Vậy trước khi tin một tỷ suất cổ tức cao, em hỏi ba câu. Một, lợi nhuận bốn quý gần nhất đang tăng hay giảm. Hai, tỷ lệ chi trả: cổ tức chiếm bao nhiêu phần trăm lợi nhuận. Nếu đã trả gần hết lợi nhuận, hoặc trả nhiều hơn lợi nhuận, mức cổ tức đó rất khó giữ. Ba, dòng tiền kinh doanh có đủ không, hay doanh nghiệp phải vay để trả cổ tức. Ví von đời thường: một người cho bạn bè vay tiền đều đặn, nhưng lương vừa bị cắt một nửa, thì năm sau khó mà cho vay như cũ.",
   "magnifying glass report", "Chương 5 – Ba câu hỏi"),
 T(("CỔ TỨC", "KHÔNG LÀM GIÀU THÊM"),
   "Một điều nhiều người mới chưa để ý. Ngày giao dịch không hưởng quyền, giá cổ phiếu được điều chỉnh giảm đúng bằng phần cổ tức tiền mặt. Tài sản của anh chị chỉ chuyển từ túi cổ phiếu sang túi tiền mặt, chưa tính thuế thu nhập 5% trên cổ tức. Cổ tức chỉ làm anh chị giàu thêm khi doanh nghiệp tiếp tục tạo ra lợi nhuận để bù vào phần đã chia. Nên câu hỏi gốc vẫn là lợi nhuận, không phải con số tỷ suất.",
   "cash envelope", "Chương 6 – Cổ tức và giá"),
 T(("BẢNG SO SÁNH", "5 MÃ CỔ TỨC CAO"),
   f"Đặt năm mã cạnh nhau cho dễ nhớ. PNJ: tỷ suất khoảng {p2(Y['PNJ']['dy'])}%, quý 3 lỗ. DHG: khoảng {p2(Y['DHG']['dy'])}%, lãi quý 3 giảm khoảng 53%. DPM: khoảng {p2(Y['DPM']['dy'])}%, lãi giảm khoảng 83%. VNM: khoảng {p2(Y['VNM']['dy'])}%, lãi tăng khoảng 17%. LPB: khoảng {p2(Y['LPB']['dy'])}%, lãi tăng khoảng 29%. Cùng nhóm tỷ suất từ 7 đến 12%, nhưng hai nhóm câu chuyện ngược nhau hoàn toàn. Nếu chỉ lọc theo tỷ suất cổ tức, anh chị sẽ nhận cả năm mã vào cùng một giỏ.",
   "comparison table", "Chương 7 – So sánh"),
 T(("BẪY HAY GẶP", "BA KIỂU"),
   "Ba kiểu bẫy hay gặp. Một, lọc cổ phiếu chỉ theo tỷ suất cổ tức, không mở báo cáo quý. Hai, nhầm cổ tức bằng cổ phiếu với cổ tức tiền mặt; cổ phiếu thưởng không đưa tiền vào túi anh chị. Ba, mua ngay trước ngày chốt quyền để ăn cổ tức, quên mất giá sẽ được điều chỉnh giảm tương ứng, và còn bị trừ thuế. Cả ba kiểu đều có chung một gốc: nhìn con số đầu ra mà không nhìn nguồn tạo ra nó.",
   "trap warning sign", "Chương 8 – Bẫy hay gặp"),
 T(("CHECKLIST", "NĂM DÒNG"),
   "Checklist năm dòng cho cổ phiếu cổ tức cao. Một, giá hiện tại thấp hơn đỉnh 52 tuần bao nhiêu phần trăm. Hai, lợi nhuận quý gần nhất và lũy kế chín tháng tăng hay giảm. Ba, tỷ lệ chi trả cổ tức so với lợi nhuận. Bốn, lưu chuyển tiền thuần từ hoạt động kinh doanh có dương không. Năm, nghị quyết đại hội cổ đông gần nhất đặt kế hoạch cổ tức bao nhiêu. Nếu ba trên năm dòng xấu, con số tỷ suất cổ tức nên được xem là cảnh báo chứ không phải lời mời.",
   "checklist clipboard", "Chương 9 – Checklist"),
 END(("CỔ TỨC CAO", "THẬT HAY BẪY?"),
   "Số liệu tỷ suất cổ tức và giá ngày 9/11/2026, kết quả kinh doanh quý 3/2026, chỉ dùng làm ví dụ minh họa. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Khi thấy một mã có tỷ suất cổ tức trên 10%, anh chị kiểm tra điều gì đầu tiên: giá đã giảm bao nhiêu, hay lợi nhuận quý gần nhất?")])

# ---------- LST_1811A: LTCM 1998 ----------
H3['LST_1811A'] = dict(
 title="LTCM 1998: quỹ có 2 nhà kinh tế đoạt Nobel mất 4,6 tỷ USD trong chưa đầy 4 tháng – đòn bẩy 25 lần đã làm gì?",
 hook=["2 NOBEL VẪN CHÁY?", "MẤT 4,6 TỶ USD"], badge="BÀI HỌC LỊCH SỬ", seri="Lịch sử & bài học thị trường", nhac='lofi',
 nguon="Nguồn: báo cáo Nhóm Công tác về Thị trường Tài chính của Tổng thống Mỹ (4/1999); Cục Dự trữ Liên bang New York; Roger Lowenstein, 'When Genius Failed' (2000).",
 tags=["lịch sử thị trường", "LTCM", "đòn bẩy", "quản trị rủi ro", "khủng hoảng 1998", "ký quỹ"],
 fb=["Đầu 1998: vốn khoảng 4,7 tỷ USD, vay hơn 120 tỷ USD – đòn bẩy khoảng 25 lần", "17/8/1998: Nga phá giá đồng rúp, ngừng trả nợ – các khoản đặt cược 'chắc ăn' cùng lúc đi ngược", "23/9/1998: 14 ngân hàng góp khoảng 3,6 tỷ USD để tiếp quản quỹ"],
 q="Nếu thị trường giảm thêm 20% ngày mai, tài khoản của anh chị có bị buộc phải bán không, hay anh chị vẫn được tự quyết định?",
 S=[
 T(("2 NOBEL VẪN CHÁY?", "MẤT 4,6 TỶ USD"),
   "Năm 1997, hai nhà kinh tế Myron Scholes và Robert Merton nhận giải Nobel kinh tế cho công trình định giá quyền chọn. Cả hai đều là thành viên của một quỹ đầu tư ở Mỹ tên là Long-Term Capital Management, gọi tắt là LTCM. Chỉ một năm sau, trong chưa đầy bốn tháng của năm 1998, quỹ này mất khoảng 4,6 tỷ USD, và Cục Dự trữ Liên bang New York phải đứng ra gọi các ngân hàng lớn tới giải cứu. Những bộ óc giỏi nhất phố Wall đã thua vì điều gì? Xem hết video, anh chị sẽ thấy bài học đó áp dụng ngay cho tài khoản vay ký quỹ ở Việt Nam.",
   "Wall Street New York", "Mở đầu", moc=True, k='hook'),
 T(("ĐỘI HÌNH", "TOÀN NGÔI SAO"),
   "LTCM được thành lập năm 1994 bởi John Meriwether, người từng đứng đầu bộ phận kinh doanh trái phiếu của ngân hàng Salomon Brothers. Đội ngũ gồm các nhà giao dịch giỏi nhất, giáo sư đại học và hai người sau này đoạt Nobel. Mức đầu tư tối thiểu là 10 triệu USD. Những năm đầu, kết quả rất đẹp: sau phí, nhà đầu tư nhận khoảng 21% năm 1994, khoảng 43% năm 1995 và khoảng 41% năm 1996. Ai cũng muốn góp tiền, và các ngân hàng lớn sẵn sàng cho quỹ vay với điều kiện rất ưu đãi.",
   "Manhattan office tower", "Chương 1 – Đội hình"),
 T(("NHẶT TIỀN LẺ", "TRƯỚC XE LU"),
   "Cách LTCM kiếm tiền nghe rất an toàn. Họ tìm hai loại trái phiếu gần giống nhau nhưng giá chênh lệch một chút, mua cái rẻ, bán khống cái đắt, rồi chờ hai giá về gần nhau. Mỗi lần chỉ lời một phần rất nhỏ. Để phần nhỏ đó thành lợi nhuận lớn, quỹ phải vay thật nhiều. Đầu năm 1998, LTCM có khoảng 4,7 tỷ USD vốn, nhưng vay hơn 120 tỷ USD, tức là đòn bẩy khoảng 25 lần. Giới đầu tư gọi kiểu chiến lược này là nhặt tiền lẻ trước một chiếc xe lu: thường ngày nhặt được đều đều, đến một ngày xe lu chạy tới.",
   "steamroller road", "Chương 2 – Cách kiếm tiền"),
 T(("MÔ HÌNH NÓI", "GẦN NHƯ KHÔNG THỂ"),
   "Các mô hình của LTCM dựa trên dữ liệu lịch sử. Theo mô hình, khả năng quỹ mất phần lớn vốn trong một năm là cực kỳ nhỏ. Vấn đề là mô hình giả định các khoản đặt cược không cùng lúc đi ngược. Khi thị trường bình thường, giả định đó đúng. Khi thị trường hoảng loạn, mọi người cùng bán thứ rủi ro và cùng mua thứ an toàn nhất, nên tất cả các khoản chênh lệch giãn ra một lượt. Mô hình không sai trong những ngày bình thường. Nó sai đúng vào ngày duy nhất mà nó cần phải đúng.",
   "computer code screen", "Chương 3 – Mô hình"),
 T(("17/8/1998", "NGA VỠ NỢ"),
   "Ngày 17/8/1998, nước Nga phá giá đồng rúp và tuyên bố ngừng trả một phần nợ trong nước. Nhà đầu tư toàn cầu hoảng sợ, đổ tiền vào trái phiếu chính phủ Mỹ, thứ được coi là an toàn nhất. Trái phiếu an toàn tăng giá, trái phiếu kém an toàn hơn giảm giá, khoảng chênh lệch mà LTCM đặt cược sẽ thu hẹp lại giãn ra mạnh. Chỉ riêng tháng 8/1998, quỹ mất gần một nửa vốn. Với đòn bẩy 25 lần, mỗi 1% đi ngược trên tài sản trở thành khoảng 25% trên vốn.",
   "Moscow Red Square", "Chương 4 – Cú sốc Nga"),
 T(("KHÔNG AI", "MUA LẠI"),
   "Khi lỗ, LTCM cần bán bớt để giảm nợ. Nhưng cả thị trường biết quỹ đang kẹt, và các khoản đầu tư của quỹ quá lớn so với thanh khoản. Không ai muốn mua ở giá hợp lý, một số bên còn bán trước để tránh bị kéo theo. Bán không được, giá càng xuống, lỗ càng sâu. Đây là điều mà mọi người dùng đòn bẩy cần nhớ: thanh khoản có mặt khi mình không cần, và biến mất đúng lúc mình cần nhất. Đến tháng 9/1998, vốn của quỹ chỉ còn một phần nhỏ so với đầu năm.",
   "empty trading floor", "Chương 5 – Thanh khoản biến mất"),
 T(("23/9/1998", "14 NGÂN HÀNG"),
   "Nếu LTCM sụp đổ hỗn loạn, các ngân hàng cho quỹ vay sẽ phải bán tháo tài sản thế chấp cùng lúc, và thị trường trái phiếu có thể đóng băng. Ngày 23/9/1998, Cục Dự trữ Liên bang New York mời các ngân hàng lớn tới họp. Mười bốn tổ chức góp khoảng 3,6 tỷ USD để tiếp quản khoảng 90% quỹ. Các nhà sáng lập gần như mất trắng phần vốn của mình. Sau đó, Fed giảm lãi suất ba lần trong mùa thu năm 1998 để trấn an thị trường. Đầu năm 2000, quỹ được giải thể.",
   "Federal Reserve Bank New York", "Chương 6 – Giải cứu"),
 T(("ÁP DỤNG", "Ở VIỆT NAM"),
   "Câu chuyện LTCM giống một tài khoản vay ký quỹ phóng to. Ở Việt Nam, khi anh chị vay để mua cổ phiếu, công ty chứng khoán đặt ngưỡng tỷ lệ ký quỹ. Thị trường giảm mạnh, tài khoản chạm ngưỡng, và lệnh bán giải chấp được đặt bất kể anh chị tin cổ phiếu đó tốt đến đâu. Khi rất nhiều tài khoản cùng chạm ngưỡng, lệnh bán dồn dập làm giá giảm sàn, tạo thêm tài khoản chạm ngưỡng mới. Đó chính là vòng xoáy mà LTCM gặp phải, chỉ khác ở quy mô.",
   "Ho Chi Minh City stock exchange", "Chương 7 – Liên hệ Việt Nam"),
 T(("BẪY HAY GẶP", "BA NIỀM TIN"),
   "Ba niềm tin đã đưa LTCM tới bờ vực. Một, người giỏi thì không thể thua lớn. Hai, chuyện chưa từng xảy ra trong dữ liệu thì sẽ không xảy ra. Ba, khi cần là bán được. Nhà đầu tư cá nhân cũng hay có ba niềm tin này: mình đã thắng nhiều lần nên lần này cũng thắng, cổ phiếu này chưa bao giờ giảm quá 30%, và mã này thanh khoản tốt nên lúc nào cũng thoát được. Một mùa thị trường xấu đủ để lật cả ba.",
   "chess pieces falling", "Chương 8 – Bẫy hay gặp"),
 T(("CHECKLIST", "NĂM DÒNG"),
   "Checklist năm dòng sau câu chuyện LTCM. Một, tính tổng dư nợ vay so với vốn tự có; nếu vượt 50% thì đã là đòn bẩy cao với người mới. Hai, tính xem thị trường giảm bao nhiêu phần trăm thì tài khoản chạm ngưỡng bị bán. Ba, đừng dồn vay vào một mã hoặc một ngành, vì khi hoảng loạn chúng giảm cùng lúc. Bốn, kiểm tra giá trị giao dịch bình quân của mã mình nắm. Năm, luôn để sẵn một phần tiền mặt hoặc kế hoạch giảm nợ, viết ra trước khi thị trường xấu.",
   "checklist clipboard", "Chương 9 – Checklist"),
 END(("ĐÒN BẨY", "AI ĐANG QUYẾT ĐỊNH?"),
   "Câu chuyện LTCM theo báo cáo của Nhóm Công tác về Thị trường Tài chính của Tổng thống Mỹ năm 1999 và các tài liệu công khai. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Nếu thị trường giảm thêm 20% ngày mai, tài khoản của anh chị có bị buộc phải bán không, hay anh chị vẫn được tự quyết định?")])

# ---------- Y3_1811A: S&P 500 và VN-Index theo tuần ----------
_W = {s[0]: s for s in hncodec.load(CW + '/data/wm.bin')['s']}
def _ds(n): return _D.date(1970, 1, 1) + _D.timedelta(days=n)
def _wk(pairs):
    o = {}
    for d, v in pairs: o[(d - _D.timedelta(days=d.weekday())).isoformat()] = v
    return o
_sp = _wk([(_ds(a), b) for a, b in zip(_W['spx'][5], _W['spx'][6])])
_vw = _wk([(_D.date.fromisoformat(x[0]), x[4] / 100) for x in daily('VNINDEX')])
_ks = sorted(set(_sp) & set(_vw))
R = [(_ks[i], (_sp[_ks[i]] / _sp[_ks[i - 1]] - 1) * 100, (_vw[_ks[i]] / _vw[_ks[i - 1]] - 1) * 100) for i in range(1, len(_ks))]
CORR = _st.correlation([r[1] for r in R], [r[2] for r in R])
BIG = [r for r in R if r[1] <= -3]; UP = [r for r in R if r[1] >= 3]; WORST = sorted(R, key=lambda r: r[2])[:5]
nup = sum(r[2] > 0 for r in UP); ndn = sum(r[2] < 0 for r in BIG); nquiet = sum(r[1] > -2.1 for r in WORST)
def _r(r): return "tuần bắt đầu %s, S&P 500 %s%%, VN-Index %s%%" % (fd(r[0]), ("giảm " if r[1] < 0 else "tăng ") + p2(abs(r[1])), ("giảm " if r[2] < 0 else "tăng ") + p2(abs(r[2])))
H3['Y3_1811A'] = dict(
 title="Mỹ hắt hơi, VN-Index cảm cúm? %d tuần dữ liệu: tương quan chỉ %s – %d/5 tuần VN-Index giảm sâu nhất, S&P 500 giảm chưa tới 2,1%%" % (len(R), p2(CORR), nquiet),
 hook=["MỸ HẮT HƠI,", "VN CẢM CÚM? %s" % p2(CORR)], badge="VĨ MÔ", seri="Vĩ mô dễ hiểu", nhac=None,
 nguon="Nguồn: S&P 500 và VN-Index đóng cửa, gom theo tuần, 11/2023–9/11/2026; tính toán của Chứng Khoán Huy Nguyễn.",
 tags=["S&P 500", "VN-Index", "chứng khoán Mỹ", "tương quan thị trường", "vĩ mô", "phố Wall"],
 fb=["%d tuần: tương quan lợi nhuận tuần giữa S&P 500 và VN-Index khoảng %s" % (len(R), p2(CORR)),
     "%d tuần S&P 500 giảm từ 3%% trở lên: VN-Index giảm cùng tuần %d lần" % (len(BIG), ndn),
     "%d/5 tuần VN-Index giảm sâu nhất, S&P 500 chỉ giảm chưa tới 2,1%% – rủi ro lớn nằm ở trong nước" % nquiet],
 q="Sáng nào thấy chứng khoán Mỹ đỏ, anh chị có thay đổi kế hoạch giao dịch trong ngày không?",
 S=[
 T(("MỸ HẮT HƠI,", "VN CẢM CÚM? %s" % p2(CORR)),
   f"Sáng nào chứng khoán Mỹ giảm mạnh, trên mạng lại có câu quen thuộc: Mỹ hắt hơi thì Việt Nam cảm cúm. Em lấy {len(R)} tuần dữ liệu, từ tháng 11/2023 tới tuần này, so S&P 500 và VN-Index theo từng tuần. Hệ số tương quan chỉ khoảng {p2(CORR)}. Còn bất ngờ hơn: trong năm tuần VN-Index giảm sâu nhất, có {nquiet} tuần S&P 500 chỉ giảm chưa tới 2,1%. Vậy anh chị nên lo phố Wall tới mức nào? Xem hết video, anh chị sẽ biết khi nào tin Mỹ đáng để ý, và khi nào nên nhìn vào chính thị trường trong nước.",
   "Wall Street New York", "Mở đầu", moc=True, k='hook', chart=CH('VNINDEX')),
 T(("TƯƠNG QUAN", "LÀ GÌ?"),
   f"Tương quan đo mức hai chuỗi số đi cùng chiều. Bằng 1 là luôn đi cùng nhau, bằng 0 là không liên quan, bằng âm 1 là luôn ngược nhau. Con số khoảng {p2(CORR)} nghĩa là có liên quan, nhưng lỏng. Nói theo thống kê, chỉ khoảng {vn(CORR * CORR * 100, 0)}% biến động tuần của VN-Index đi cùng biến động của S&P 500; phần lớn còn lại đến từ chỗ khác. Ví von đời thường: hai người hàng xóm có khi cùng mở cửa sổ lúc trời nóng, nhưng phần lớn thời gian mỗi nhà có lịch sinh hoạt riêng.",
   "two lines chart", "Chương 1 – Tương quan"),
 T(("KHI MỸ GIẢM", "TỪ 3% TRỞ LÊN"),
   f"Trong {len(R)} tuần, S&P 500 có {len(BIG)} tuần giảm từ 3% trở lên. VN-Index giảm cùng tuần {ndn} lần. Lần nặng nhất là {_r(BIG[-1])}, đúng tuần thế giới chao đảo vì thuế quan đầu tháng 4/2025. Nhưng cũng có {_r(BIG[2])}. Nghĩa là cú giảm của Mỹ đủ lớn thì thường kéo theo Việt Nam, nhưng không phải lúc nào cũng vậy, và mức giảm ở Việt Nam có khi nhẹ hơn, có khi nặng hơn.",
   "stock market crash screen", "Chương 2 – Khi Mỹ giảm mạnh"),
 T(("KHI MỸ TĂNG", "TỪ 3% TRỞ LÊN"),
   f"Chiều ngược lại thì sao? S&P 500 có {len(UP)} tuần tăng từ 3% trở lên. Trong những tuần đó, VN-Index tăng {nup} lần, giảm {len(UP) - nup} lần. Mức tăng của VN-Index thường nhỏ hơn mức tăng của Mỹ. Ví dụ tuần bắt đầu 7/4/2025, khi Mỹ tạm hoãn thuế quan, S&P 500 tăng khoảng 5,7%, VN-Index chỉ tăng khoảng 1%. Nghĩa là tin tốt từ Mỹ có giúp, nhưng không tự động kéo VN-Index lên cùng biên độ.",
   "rising stock chart", "Chương 3 – Khi Mỹ tăng mạnh"),
 T(("NĂM TUẦN", "TỆ NHẤT CỦA VN"),
   f"Bây giờ đảo câu hỏi: những tuần VN-Index giảm sâu nhất, Mỹ làm gì? Tuần tệ nhất, {_r(WORST[0])}. Tuần thứ hai, {_r(WORST[1])}. Ba tuần còn lại: {_r(WORST[2])}; {_r(WORST[3])}; và {_r(WORST[4])}. Có {nquiet} trên 5 tuần, S&P 500 gần như đứng yên hoặc chỉ giảm nhẹ. Lý do của những tuần đó phải tìm ở trong nước: dòng tiền, tỷ giá, vay ký quỹ, tin riêng của các nhóm ngành.",
   "Ho Chi Minh City skyline", "Chương 4 – Tuần tệ nhất"),
 T(("RỦI RO", "NẰM TRONG NƯỚC"),
   "Điều này thay đổi cách theo dõi tin tức. Nhiều người dậy sớm xem phố Wall, rồi bỏ qua các con số trong nước như tỷ giá USD trên VND, lãi suất liên ngân hàng, dư nợ vay ký quỹ toàn thị trường hay giao dịch của khối ngoại. Theo dữ liệu ba năm qua, chính các yếu tố này mới thường đứng sau những tuần giảm sâu nhất của VN-Index. Phố Wall đáng xem, nhưng nên xếp sau các chỉ số trong nước khi đánh giá rủi ro cho danh mục.",
   "Vietnamese dong banknotes", "Chương 5 – Rủi ro trong nước"),
 T(("KÊNH TRUYỀN", "TỪ MỸ SANG VN"),
   "Khi nào thì tin Mỹ thật sự đáng để ý? Tin từ Mỹ truyền sang Việt Nam qua ba kênh chính. Một, lãi suất của Fed và đồng USD: USD mạnh làm áp lực tỷ giá trong nước tăng, Ngân hàng Nhà nước có thể phải giữ lãi suất cao hơn. Hai, khối ngoại: khi nhà đầu tư toàn cầu hoảng sợ, họ rút tiền khỏi các thị trường cận biên và mới nổi. Ba, xuất khẩu: Mỹ là thị trường xuất khẩu lớn nhất của Việt Nam, nên tin thuế quan tác động thẳng vào doanh nghiệp. Cú sốc đi qua cả ba kênh, như tháng 4/2025, thường mạnh nhất.",
   "container port ships", "Chương 6 – Ba kênh truyền"),
 T(("BẪY HAY GẶP", "BA KIỂU"),
   "Ba kiểu bẫy hay gặp. Một, bán vội lúc mở cửa chỉ vì đêm qua Mỹ đỏ, trong khi dữ liệu cho thấy VN-Index không luôn đi theo. Hai, mua đuổi vì Mỹ lập đỉnh mới, quên rằng chênh lệch biên độ giữa hai thị trường rất lớn. Ba, chỉ theo dõi tin quốc tế mà bỏ qua tỷ giá và vay ký quỹ trong nước, chính là những thứ đứng sau các tuần tệ nhất. Cả ba kiểu đều xuất phát từ một câu nói nghe hợp lý nhưng chưa được kiểm tra bằng số liệu.",
   "trap warning sign", "Chương 7 – Bẫy hay gặp"),
 T(("CHECKLIST", "SÁNG THỨ HAI"),
   "Checklist sáng thứ Hai cho người bận rộn. Một, xem S&P 500 tuần trước giảm hay tăng bao nhiêu; dưới 3% thì đừng vội đổi kế hoạch. Hai, xem tỷ giá USD trên VND và chỉ số đồng USD. Ba, xem khối ngoại mua hay bán ròng tuần trước. Bốn, xem lãi suất liên ngân hàng có tăng vọt không. Năm, kiểm tra tỷ lệ vay ký quỹ của chính tài khoản mình. Năm dòng này mất khoảng mười phút, nhưng giúp anh chị phân biệt tiếng ồn với rủi ro thật.",
   "checklist clipboard", "Chương 8 – Checklist"),
 T(("BẢNG GHI NHỚ", "BA CON SỐ"),
   f"Ba con số để ghi nhớ. Một, tương quan tuần khoảng {p2(CORR)}: có liên quan nhưng lỏng. Hai, {ndn} trên {len(BIG)} tuần Mỹ giảm mạnh, VN-Index giảm theo: cú sốc lớn của Mỹ vẫn cần được tôn trọng. Ba, {nquiet} trên 5 tuần tệ nhất của VN-Index, Mỹ gần như bình yên: rủi ro lớn nhất thường nằm ở nhà mình. Số liệu ba năm là một mẫu ngắn, chưa có các giai đoạn như năm 2008 hay 2022, nên đây là cách nhìn, không phải quy luật.",
   "notebook pen", "Chương 9 – Ghi nhớ"),
 END(("MỸ HẮT HƠI,", "ANH CHỊ LÀM GÌ?"),
   "Số liệu S&P 500 và VN-Index theo tuần tới ngày 9/11/2026, quá khứ không bảo đảm cho tương lai. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Sáng nào thấy chứng khoán Mỹ đỏ, anh chị có thay đổi kế hoạch giao dịch trong ngày không?")])
