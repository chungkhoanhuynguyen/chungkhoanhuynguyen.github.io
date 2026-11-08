# -*- coding: utf-8 -*-
# NV1 9/11/2026 – kịch bản viết tay lô 20261109: CH2611B, CH2711B, CH2811B (kênh chính), LST_1611A/1711A, Y3_1611A/1711A.
# Số liệu tính trực tiếp từ data/c/*.bin, data/wm.bin, data/mac.bin, data/bctc/*.bin (dữ liệu tới 6/11/2026).
import datetime as _D, statistics as _st, math as _m
from lib import *
from hand import T as _T, END as _END
def T(cap, say, *a, **kw): return _T(cap, say.replace('%%', '%'), *a, **kw)
def END(cap, say): return _END(cap, say.replace('%%', '%'))
H2 = {}
WEBL = "Bảng tính kèm video có miễn phí trên trang chứng khoán Huy Nguyễn chấm com, mục bài học."
CH = lambda s: {'sym': s + 'W', 'tf': 'W', 'weeks': 52, 'circles': None}
def _c(s): return [(x[0], x[4] / 100) for x in daily(s)]
def p1(x): return vn(x, 1)
def p2(x): return vn(x, 2)

# ---------------- CH2611B: mua trung bình giá xuống ----------------
def _avg(s, pk, n=4):
    cc = _c(s); i0 = [k for k, x in enumerate(cc) if x[0] == pk][0]; buys = [cc[i0]]; nxt = cc[i0][1] * 0.8
    for d, p in cc[i0:]:
        if p <= nxt and len(buys) < n: buys.append((d, p)); nxt = p * 0.8
    sh = sum(100 / p for _, p in buys); inv = 100 * len(buys); last = cc[-1][1]
    return dict(b=buys, avg=inv / sh, val=sh * last, inv=inv, last=last, single=100 * last / buys[0][1], hi_after=max((p, d) for d, p in cc if d >= buys[-1][0]), low=min((p, d) for d, p in cc if d >= pk))
A = _avg('DIG', '2024-04-02'); B = _avg('HPG', '2024-06-12')
def fd(d): return "%d/%d/%s" % (int(d[8:]), int(d[5:7]), d[:4])
_b = A['b']
H2['CH2611B'] = dict(
 title="Quản trị vốn | Mua trung bình giá xuống: 4 lần mua DIG, vốn 400 triệu còn %s triệu – khi nào bình quân giá thành bẫy?" % vn(A['val'], 0),
 hook=["MUA THÊM KHI LỖ?", "DIG −%s%%" % p1((1 - A['low'][0] / _b[0][1]) * 100)], badge="QUẢN TRỊ VỐN", seri="Quản trị vốn", nhac=None,
 nguon="Nguồn: giá đóng cửa điều chỉnh DIG, HPG trên HOSE 10/2023–6/11/2026; ví dụ mô phỏng mỗi lần mua 100 triệu đồng khi giá thấp hơn lần mua trước 20%.",
 tags=["mua trung bình giá xuống", "bình quân giá", "quản trị vốn", "DIG", "HPG", "cắt lỗ", "quản trị rủi ro"],
 fb=["DIG: mua 4 lần, mỗi lần 100 triệu (%s), giá vốn bình quân %s nghìn – ngày 6/11/2026 còn khoảng %s triệu" % (", ".join("%s: %s" % (fd(d), p2(p)) for d, p in _b), p2(A['avg']), vn(A['val'], 0)),
     "Có lúc danh mục DIG lãi: ngày %s giá %s nghìn, cao hơn giá vốn bình quân" % (fd(A['hi_after'][1]), p2(A['hi_after'][0])),
     "HPG cùng cách mua: 2 lần, 200 triệu thành khoảng %s triệu – khác nhau ở lợi nhuận doanh nghiệp, không ở giá" % vn(B['val'], 0)],
 q="Lần gần nhất anh chị mua thêm một mã đang lỗ, anh chị có viết ra lý do mua thêm dựa trên số liệu kinh doanh không?",
 S=[
 T(("MUA THÊM KHI LỖ?", "DIG −%s%%" % p1((1 - A['low'][0] / _b[0][1]) * 100)),
   "Ngày %s, cổ phiếu DIG đóng cửa ở khoảng %s nghìn đồng, giá đã điều chỉnh. Ngày %s, DIG chỉ còn khoảng %s nghìn đồng, tức là giảm khoảng %s%%. Bây giờ, anh chị thử hình dung một nhà đầu tư rất kiên nhẫn: cứ mỗi lần giá thấp hơn lần mua trước 20%%, người đó lại mua thêm 100 triệu đồng để kéo giá vốn xuống. Bốn lần mua, 400 triệu đồng. Ngày 6/11/2026, số tiền đó còn khoảng %s triệu đồng. Nếu chỉ mua một lần rồi để yên, người đó mất khoảng %s triệu. Mua trung bình giá xuống làm phần trăm lỗ nhỏ lại, nhưng số tiền mất lại lớn hơn gấp mấy lần. Xem hết video, anh chị sẽ biết khi nào mua thêm là có kế hoạch, và khi nào nó chỉ là cách để không phải thừa nhận mình sai." % (
       fd(_b[0][0]), p2(_b[0][1]), fd(A['low'][1]), p2(A['low'][0]), p1((1 - A['low'][0] / _b[0][1]) * 100), vn(A['val'], 0), vn(100 - A['single'], 0)),
   "Vietnam real estate construction", "Mở đầu", moc=True, k='hook', chart=CH('DIG')),
 T(("BỐN LẦN MUA", "CỦA DIG"),
   "Em đi lại từng lần mua. Lần một, ngày %s, giá khoảng %s nghìn đồng. Lần hai, ngày %s, giá khoảng %s nghìn, vừa thấp hơn lần trước 20%%. Lần ba, ngày %s, giá khoảng %s nghìn. Lần bốn, ngày %s, giá khoảng %s nghìn đồng, đúng giai đoạn thị trường giảm mạnh đầu tháng 4/2025. Sau bốn lần, giá vốn bình quân còn khoảng %s nghìn đồng, thấp hơn giá mua lần đầu khoảng %s%%. Trên giấy, mọi thứ trông rất hợp lý: giá vốn đã thấp hơn nhiều, chỉ cần giá hồi một chút là hòa vốn. Đây chính là suy nghĩ làm cho cách mua này hấp dẫn đến vậy." % (
       fd(_b[0][0]), p2(_b[0][1]), fd(_b[1][0]), p2(_b[1][1]), fd(_b[2][0]), p2(_b[2][1]), fd(_b[3][0]), p2(_b[3][1]), p2(A['avg']), p1((1 - A['avg'] / _b[0][1]) * 100)),
   "stock market chart screen", "Chương 1 – Bốn lần mua"),
 T(("CÓ LÚC ĐÃ LÃI", "RỒI MẤT HẾT"),
   "Điều bất ngờ nằm ở đây. Sau lần mua thứ tư, DIG có một nhịp hồi rất mạnh. Ngày %s, giá lên khoảng %s nghìn đồng, cao hơn giá vốn bình quân khoảng %s%%. Ở thời điểm đó, danh mục 400 triệu đang lãi. Người mua trung bình giá xuống sẽ thấy mình đúng, và rất có thể sẽ kể cho bạn bè nghe rằng kiên nhẫn là chiến thắng. Nhưng không có kế hoạch bán, khoản lãi đó chỉ nằm trên màn hình. Giá sau đó giảm tiếp về khoảng %s nghìn ngày %s. Câu móc cho phần tiếp theo: vấn đề không nằm ở việc mua thêm, mà nằm ở chỗ quyết định mua thêm được dựa vào điều gì." % (
       fd(A['hi_after'][1]), p2(A['hi_after'][0]), p1((A['hi_after'][0] / A['avg'] - 1) * 100), p2(A['low'][0]), fd(A['low'][1])),
   "roller coaster", "Chương 2 – Bất ngờ"),
 T(("PHẦN TRĂM", "VÀ SỐ TIỀN"),
   "Nhiều người nhìn vào phần trăm lỗ để tự an ủi. Với bốn lần mua, phần trăm lỗ ngày 6/11/2026 là khoảng %s%%, nhỏ hơn mức khoảng %s%% nếu chỉ mua một lần. Nhưng tiền không trả bằng phần trăm. Mua một lần, khoản mất là khoảng %s triệu đồng. Mua bốn lần, khoản mất là khoảng %s triệu đồng. Thêm nữa, 300 triệu bỏ vào ba lần sau đã bị khóa trong một mã suốt nhiều tháng, không thể dùng cho cơ hội khác. Ví von đời thường: đổ thêm xăng vào một chiếc xe đang hỏng máy không làm xe chạy nhanh hơn, chỉ làm bình xăng mất nhiều tiền hơn." % (
       p1((1 - A['val'] / A['inv']) * 100), p1(100 - A['single']), vn(100 - A['single'], 0), vn(A['inv'] - A['val'], 0)),
   "money calculator", "Chương 3 – Phần trăm và tiền"),
 T(("CÙNG CÁCH MUA", "HPG KHÁC HẲN"),
   "Bây giờ áp đúng quy tắc đó cho HPG. Mua lần một ngày %s, giá khoảng %s nghìn đồng. Giá chỉ một lần thấp hơn 20%%, ngày %s, khoảng %s nghìn, nên chỉ có hai lần mua, tổng 200 triệu. Ngày 6/11/2026, HPG đóng cửa khoảng %s nghìn, số tiền đó thành khoảng %s triệu đồng. Cùng một quy tắc, một bên mất gần một nửa, một bên có lãi. Sự khác nhau không đến từ biểu đồ giá, mà đến từ thứ nằm sau giá: lợi nhuận doanh nghiệp. Lợi nhuận sau thuế công ty mẹ quý 3/2026 của HPG khoảng 8.217 tỷ đồng, tăng khoảng 106%% so với cùng kỳ." % (
       fd(B['b'][0][0]), p2(B['b'][0][1]), fd(B['b'][1][0]), p2(B['b'][1][1]), p2(B['last']), vn(B['val'], 0)),
   "steel mill", "Chương 4 – So sánh"),
 T(("ĐIỀU KIỆN 1", "LỢI NHUẬN CÒN ĐÓ"),
   "Vậy khi nào mua thêm một mã đang lỗ là có cơ sở? Điều kiện thứ nhất: lý do mua ban đầu vẫn còn nguyên. Nếu anh chị mua vì lợi nhuận tăng trưởng, thì trước lần mua thêm phải mở báo cáo quý mới nhất và kiểm tra lợi nhuận còn tăng hay không. Giá giảm mà lợi nhuận vẫn tăng thì mã đó đang rẻ đi. Giá giảm và lợi nhuận cũng giảm thì mã đó có thể không rẻ đi chút nào, vì cái mẫu số của P trên E cũng đang co lại. Câu đúc kết: giá giảm chưa phải là lý do, lợi nhuận mới là lý do." ,
   "financial report", "Chương 5 – Điều kiện mua thêm"),
 T(("ĐIỀU KIỆN 2", "TRẦN TỶ TRỌNG"),
   "Điều kiện thứ hai: đặt trần tỷ trọng trước khi mua lần đầu. Ví dụ, một mã không được vượt 15% danh mục, kể cả khi mua thêm. Nếu danh mục 1 tỷ đồng, trần là 150 triệu. Với trần này, người mua DIG trong ví dụ chỉ được mua tối đa một lần rưỡi, không phải bốn lần. Trần tỷ trọng giống dây an toàn trên ô tô: lúc bình thường thấy vướng víu, lúc va chạm mới thấy nó giữ mình lại. Không có trần, mỗi lần giá giảm lại sinh ra một lý do mới để mua thêm, và một mã nhỏ dần dần chiếm cả danh mục." ,
   "seat belt car", "Chương 5 – Điều kiện mua thêm"),
 T(("ĐIỀU KIỆN 3", "ĐIỂM DỪNG VIẾT SẴN"),
   "Điều kiện thứ ba: viết sẵn điểm dừng cho cả vị thế. Ví dụ: nếu lợi nhuận hai quý liên tiếp giảm so với cùng kỳ, hoặc tổng vị thế lỗ quá 10% số vốn dành cho nó, thì dừng mua và giảm dần. Điểm dừng phải viết trước, vì khi đang lỗ, não người rất giỏi tìm lý do để chờ thêm. Các nghiên cứu tài chính hành vi gọi đây là hiệu ứng chốt lời sớm, gồng lỗ lâu: người ta bán mã đang lãi quá sớm và giữ mã đang lỗ quá lâu. Mua trung bình giá xuống không kế hoạch chính là phiên bản mạnh hơn của gồng lỗ." ,
   "stop sign", "Chương 5 – Điều kiện mua thêm"),
 T(("MUA THÊM", "KHI ĐÚNG"),
   "Có một cách ngược lại mà ít người dùng: mua thêm khi mình đúng, tức là khi giá đã đi lên và lợi nhuận quý mới xác nhận luận điểm. Cách này làm giá vốn bình quân cao lên, nên nhìn không sướng mắt. Nhưng nó có một ưu điểm lớn: tiền chỉ được đổ thêm vào những vị thế đang được thị trường và báo cáo tài chính cùng xác nhận. Một người thợ câu giỏi không thả thêm mồi vào chỗ không có cá, mà thả vào chỗ phao đang động." ,
   "fishing float lake", "Chương 6 – Mua thêm khi đúng"),
 T(("BẪY HAY GẶP", "BA CÂU NÓI"),
   "Ba câu nói thường báo hiệu mua trung bình giá xuống đã thành bẫy. Câu một: giá này rẻ quá rồi, không thể giảm thêm. Ví dụ DIG cho thấy giá đã giảm 50%% vẫn có thể giảm thêm. Câu hai: mua thêm để về bờ nhanh hơn. Mục tiêu đã chuyển từ đầu tư sang gỡ lỗ. Câu ba: chưa bán thì chưa lỗ. Khoản lỗ đã nằm trong tài khoản, việc chưa bán chỉ làm nó chưa được ghi sổ. Nếu anh chị nghe chính mình nói một trong ba câu này, đó là lúc dừng lại, mở báo cáo tài chính trước khi mở bảng giá." ,
   "trap warning", "Chương 7 – Bẫy hay gặp"),
 T(("CHECKLIST", "TRƯỚC LỆNH MUA THÊM"),
   "Checklist năm dòng trước mỗi lệnh mua thêm. Một, lý do mua ban đầu là gì, còn đúng không. Hai, lợi nhuận quý mới nhất so với cùng kỳ tăng hay giảm. Ba, sau lệnh này mã đó chiếm bao nhiêu phần trăm danh mục, có vượt trần không. Bốn, điểm dừng của cả vị thế ở đâu. Năm, nếu không có mã này trong danh mục, hôm nay mình có mua nó không. Câu thứ năm là câu khó nhất và cũng trung thực nhất. " + WEBL,
   "checklist notebook", "Chương 8 – Checklist"),
 END(("MUA THÊM KHI LỖ?", "CÓ KẾ HOẠCH CHƯA?"),
   "Số liệu giá đóng cửa đã điều chỉnh của DIG và HPG từ tháng 10/2023 đến ngày 6/11/2026, ví dụ chỉ để minh họa, không phải khuyến nghị. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Lần gần nhất anh chị mua thêm một mã đang lỗ, anh chị có viết ra lý do mua thêm dựa trên số liệu kinh doanh không?")])

# ---------------- CH2711B: chia vốn theo biến động ----------------
SY = ['DHG', 'VCB', 'HPG', 'SSI', 'DIG', 'NVL']
def _vol(s):
    c = [x[1] for x in _c(s)]; r = [c[i] / c[i - 1] - 1 for i in range(1, len(c))]
    return _st.pstdev(r) * _m.sqrt(250) * 100
V = {s: _vol(s) for s in SY}; VM = {s: V[s] / _m.sqrt(12) for s in SY}; STOP = {s: 2 * VM[s] for s in SY}; POS = {s: 10 / (STOP[s] / 100) for s in SY}
ratio = V['NVL'] / V['DHG']
H2['CH2711B'] = dict(
 title="Quản trị vốn | Cùng 100 triệu nhưng rủi ro gấp %s lần: chia tiền theo biến động DHG, VCB, HPG, SSI, DIG, NVL" % p1(ratio),
 hook=["CÙNG 100 TRIỆU?", "RỦI RO GẤP %s" % p1(ratio)], badge="QUẢN TRỊ VỐN", seri="Quản trị vốn", nhac=None,
 nguon="Nguồn: độ biến động năm tính từ lợi suất ngày, giá đóng cửa điều chỉnh HOSE 10/2023–6/11/2026; ví dụ danh mục 1 tỷ đồng, rủi ro 1% mỗi vị thế.",
 tags=["quản trị vốn", "độ biến động", "tỷ trọng danh mục", "position sizing", "quy tắc 1%", "quản trị rủi ro"],
 fb=["Độ biến động năm 3 năm qua: " + ", ".join("%s %s%%" % (s, p1(V[s])) for s in SY),
     "Cùng chấp nhận mất 10 triệu (1%% của 1 tỷ): vị thế DHG khoảng %s triệu, NVL khoảng %s triệu" % (vn(POS['DHG'], 0), vn(POS['NVL'], 0)),
     "Chia đều tiền không phải chia đều rủi ro"],
 q="Danh mục của anh chị đang chia đều tiền cho các mã, hay đã chia theo mức dao động của từng mã?",
 S=[
 T(("CÙNG 100 TRIỆU?", "RỦI RO GẤP %s" % p1(ratio)),
   "Phần lớn nhà đầu tư chia vốn theo một cách rất tự nhiên: mỗi mã 100 triệu cho đều. Nhưng theo dữ liệu ba năm qua tới ngày 6/11/2026, độ biến động năm của NVL khoảng %s%%, còn của DHG chỉ khoảng %s%%. Nghĩa là cùng 100 triệu, vị thế NVL dao động mạnh gấp khoảng %s lần vị thế DHG. Chia đều tiền không có nghĩa là chia đều rủi ro. Video này em đi qua sáu mã thật, từ ít dao động đến nhiều dao động, và một cách tính đơn giản để mỗi vị thế, nếu sai, chỉ làm danh mục mất cùng một số tiền. Xem hết video, anh chị sẽ có một bảng tỷ trọng tự làm được trong năm phút." % (p1(V['NVL']), p1(V['DHG']), p1(ratio)),
   "stock exchange board", "Mở đầu", moc=True, k='hook', chart=CH('NVL')),
 T(("ĐỘ BIẾN ĐỘNG", "LÀ GÌ"),
   "Độ biến động đo xem giá một mã thường nhảy lên xuống mạnh cỡ nào. Cách tính: lấy phần trăm thay đổi giá mỗi ngày, đo độ lệch chuẩn của chuỗi đó, rồi quy ra năm. Anh chị không cần nhớ công thức, chỉ cần hiểu ý nghĩa. Độ biến động năm 20%% nghĩa là trong một năm bình thường, giá đi lệch khoảng 20%% so với xu hướng là chuyện hay xảy ra. Độ biến động 40%% nghĩa là lệch 40%% vẫn là chuyện bình thường. Nó giống như thời tiết: Đà Lạt và sa mạc đều có nhiệt độ trung bình, nhưng chênh lệch ngày đêm thì khác hẳn." ,
   "weather thermometer", "Chương 1 – Khái niệm"),
 T(("SÁU MÃ", "SÁU MỨC DAO ĐỘNG"),
   "Đây là độ biến động năm tính từ giá đóng cửa đã điều chỉnh, tháng 10/2023 đến ngày 6/11/2026. Dược Hậu Giang khoảng %s%%. Vietcombank khoảng %s%%. Hòa Phát khoảng %s%%. Chứng khoán SSI khoảng %s%%. DIC Corp, mã DIG, khoảng %s%%. Novaland khoảng %s%%. Điều thú vị là thứ tự này khá khớp với cảm nhận của nhà đầu tư: dược phẩm và ngân hàng lớn đi chậm, chứng khoán và bất động sản đi nhanh. Nhưng ít ai biến cảm nhận đó thành con số để chia tiền." % tuple(p1(V[s]) for s in SY),
   "pharmacy", "Chương 2 – Sáu mã"),
 T(("BƯỚC 1", "RỦI RO MỖI LỆNH"),
   "Bước một, quyết định mỗi vị thế được phép làm danh mục mất tối đa bao nhiêu nếu sai. Nhiều người dùng mốc 1%%. Với danh mục 1 tỷ đồng, đó là 10 triệu. Con số này nghe nhỏ, nhưng nó có lý do: thua mười lệnh liên tiếp, danh mục vẫn còn khoảng 90%%. Anh chị có thể chọn 0,5%% hay 2%% tùy khẩu vị, miễn là chọn trước và dùng chung cho mọi mã. Đây là phần không đổi. Phần thay đổi là khoảng cách tới điểm sai của từng mã." ,
   "calculator desk", "Chương 3 – Ba bước"),
 T(("BƯỚC 2", "ĐIỂM SAI THEO NHỊP"),
   "Bước hai, đặt điểm sai theo nhịp dao động của chính mã đó, thay vì một con số chung như 7%% cho mọi mã. Một cách đơn giản: lấy độ biến động năm chia cho căn bậc hai của 12 để ra mức dao động khoảng một tháng, rồi nhân hai. Với DHG, dao động một tháng khoảng %s%%, điểm sai khoảng %s%%. Với VCB, khoảng %s%%. Với HPG, khoảng %s%%. Với SSI, khoảng %s%%. Với DIG, khoảng %s%%. Với NVL, khoảng %s%%. Đặt điểm sai 7%% cho NVL giống như đo nhiệt độ sa mạc bằng thang của Đà Lạt: chỉ một ngày nắng đã báo động." % (
       p1(VM['DHG']), p1(STOP['DHG']), p1(STOP['VCB']), p1(STOP['HPG']), p1(STOP['SSI']), p1(STOP['DIG']), p1(STOP['NVL'])),
   "desert heat", "Chương 3 – Ba bước"),
 T(("BƯỚC 3", "CHIA TIỀN"),
   "Bước ba, chia tiền: số tiền vị thế bằng mức rủi ro chia cho khoảng cách điểm sai. Với 10 triệu rủi ro: DHG được khoảng %s triệu. VCB khoảng %s triệu. HPG khoảng %s triệu. SSI khoảng %s triệu. DIG khoảng %s triệu. NVL khoảng %s triệu. Nhìn bảng này, anh chị thấy vị thế mã ít dao động lớn gấp mấy lần mã nhiều dao động, nhưng nếu cả hai cùng chạm điểm sai, danh mục mất đúng 10 triệu như nhau. Đó mới là chia đều rủi ro." % tuple(vn(POS[s], 0) for s in SY),
   "pie chart portfolio", "Chương 3 – Ba bước"),
 T(("BẤT NGỜ", "MÃ ÍT DAO ĐỘNG"),
   "Đến đây có một điều bất ngờ. Nhiều người nghĩ mã ít dao động thì an toàn, nên dồn hết vào đó. Nhưng độ biến động chỉ đo quá khứ bình thường, không đo được cú sốc riêng của doanh nghiệp. Lợi nhuận quý 3/2026 của Dược Hậu Giang giảm khoảng 53%% so với cùng kỳ, dù đây là mã ít dao động nhất trong sáu mã. Vì vậy, bảng chia tiền theo biến động luôn cần thêm một trần: không mã nào vượt 20%% danh mục, dù nó dao động ít đến đâu." ,
   "medicine production", "Chương 4 – Giới hạn"),
 T(("VCB CŨNG", "CÓ LÚC −29%"),
   "Một ví dụ khác cho thấy vì sao cần trần. Vietcombank, mã ngân hàng lớn nhất, có độ biến động năm chỉ khoảng %s%%. Nhưng từ đỉnh khoảng 75,4 nghìn đồng ngày 14/1/2026, giá về khoảng 53,5 nghìn ngày 3/11/2026, giảm khoảng 29%%. Ít dao động hằng ngày không có nghĩa là không thể giảm sâu, nó chỉ có nghĩa là giảm từ từ. Câu móc cho phần sau: vậy dùng bảng này thế nào khi thị trường đổi tính?" % p1(V['VCB']),
   "Vietcombank headquarters", "Chương 4 – Giới hạn"),
 T(("CẬP NHẬT", "MỖI QUÝ"),
   "Độ biến động không đứng yên. Khi thị trường hoảng loạn, như đầu tháng 4/2025, mọi mã đều dao động mạnh hơn, và bảng chia tiền tự động bảo anh chị giảm quy mô vị thế. Khi thị trường yên ả, bảng cho phép vị thế lớn hơn. Em gợi ý cập nhật bảng mỗi quý, cùng lúc với mùa báo cáo tài chính, để hai việc đi cùng nhau: đọc lợi nhuận và đo nhịp dao động. Người lái xe giỏi không giữ một tốc độ cho mọi con đường." ,
   "highway night traffic", "Chương 5 – Cập nhật"),
 T(("BẪY HAY GẶP", "BA CHỖ SAI"),
   "Ba chỗ sai hay gặp. Một, tính đúng vị thế nhưng không đặt điểm sai, thế là bảng chỉ là trang trí. Hai, dùng vay ký quỹ, làm mọi con số trong bảng nhân lên theo tỷ lệ vay. Ba, dời điểm sai ra xa khi giá tới gần, vì tiếc. Dời điểm sai đồng nghĩa với tăng rủi ro sau khi lệnh đã vào, và phá hỏng toàn bộ phép chia ở bước ba." ,
   "broken rule", "Chương 6 – Bẫy hay gặp"),
 T(("CHECKLIST", "NĂM PHÚT"),
   "Checklist năm phút cho mỗi mã mới. Một, chọn mức rủi ro mỗi lệnh, ví dụ 1%% danh mục. Hai, tính độ biến động năm của mã. Ba, quy ra khoảng cách điểm sai. Bốn, chia rủi ro cho khoảng cách để ra số tiền. Năm, so với trần 20%% và lấy số nhỏ hơn. " + WEBL,
   "notebook pen", "Chương 7 – Checklist"),
 END(("CHIA ĐỀU TIỀN?", "HAY CHIA RỦI RO?"),
   "Số liệu giá đóng cửa đã điều chỉnh sáu mã DHG, VCB, HPG, SSI, DIG, NVL từ tháng 10/2023 đến ngày 6/11/2026, ví dụ minh họa, không phải khuyến nghị. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Danh mục của anh chị đang chia đều tiền cho các mã, hay đã chia theo mức dao động của từng mã?")])

# ---------------- CH2811B: 10 phiên giảm mạnh nhất VN-Index ----------------
_v = _c('VNINDEX'); _r = sorted([(_v[i][1] / _v[i - 1][1] - 1, i) for i in range(1, len(_v))])[:10]
W10 = [dict(d=_v[i][0], r=x * 100, c=_v[i][1], f5=(_v[min(i + 5, len(_v) - 1)][1] / _v[i][1] - 1) * 100, f20=(_v[min(i + 20, len(_v) - 1)][1] / _v[i][1] - 1) * 100,
            f60=(_v[min(i + 60, len(_v) - 1)][1] / _v[i][1] - 1) * 100) for x, i in _r]
n60 = sum(1 for w in W10 if w['f60'] > 0); n5 = sum(1 for w in W10 if w['f5'] < 0)
def _w(w): return "ngày %s giảm %s%%, đóng cửa khoảng %s điểm" % (fd(w['d']), p2(abs(w['r'])), vn(w['c'], 0))
H2['CH2811B'] = dict(
 title="Bài học lịch sử | 10 phiên giảm mạnh nhất của VN-Index 3 năm qua: 60 phiên sau %d/10 lần cao hơn – nhưng đừng vội kết luận" % n60,
 hook=["BÁN KHI SẬP?", "%d/10 LẦN HỒI" % n60], badge="BÀI HỌC LỊCH SỬ", seri="Bài học lịch sử", nhac=None,
 nguon="Nguồn: VN-Index đóng cửa ngày, HOSE, 27/10/2023–6/11/2026 (754 phiên); tính toán của Chứng Khoán Huy Nguyễn.",
 tags=["VN-Index", "bài học lịch sử", "phiên giảm mạnh", "bán tháo", "tâm lý đầu tư", "quản trị rủi ro"],
 fb=["3 phiên giảm sâu nhất: " + "; ".join("%s %s%%" % (fd(w['d']), p2(w['r'])) for w in W10[:3]),
     "60 phiên sau: %d/10 lần VN-Index cao hơn ngày giảm; 5 phiên sau vẫn có %d lần thấp hơn" % (n60, n5),
     "Mẫu chỉ 3 năm, không có 2022 – kế hoạch vẫn quan trọng hơn thống kê"],
 q="Trong phiên giảm mạnh gần nhất, anh chị đã làm theo kế hoạch viết sẵn hay theo cảm xúc của phiên hôm đó?",
 S=[
 T(("BÁN KHI SẬP?", "%d/10 LẦN HỒI" % n60),
   "Trong 754 phiên giao dịch từ cuối tháng 10/2023 tới ngày 6/11/2026, VN-Index có mười phiên giảm mạnh nhất. Phiên nặng nhất là %s. Câu hỏi mà ai cũng tự hỏi trong những phiên như thế: bán ngay để giữ tiền, hay ngồi yên? Em lấy đúng mười phiên đó và đo xem 5 phiên, 20 phiên và 60 phiên sau, chỉ số ở đâu. Kết quả: 60 phiên sau, %d trên 10 lần VN-Index cao hơn mức đóng cửa của ngày giảm. Nhưng xem hết video, anh chị sẽ thấy vì sao con số đẹp này không phải là lời khuyên cứ giảm là mua." % (_w(W10[0]), n60),
   "stock market crash screen", "Mở đầu", moc=True, k='hook', chart=CH('VNINDEX')),
 T(("CỤM THÁNG 4", "NĂM 2025"),
   "Ba trong mười phiên nằm sát nhau đầu tháng 4/2025. Phiên thứ nhất, %s. Phiên thứ hai, %s. Phiên thứ ba, %s. Đó là giai đoạn thị trường thế giới chao đảo vì thuế quan, S&P 500 giảm khoảng 18,9%% từ đỉnh ngày 19/2/2025 tới ngày 8/4/2025. Người bán ở phiên đầu tiên nghĩ mình đã thoát, nhưng hai phiên sau giá còn thấp hơn. Người bán ở phiên cuối lại bán đúng vùng thấp nhất của cả giai đoạn. Cùng một cú sập, cùng một quyết định bán, kết quả khác nhau hoàn toàn chỉ vì chênh nhau vài ngày." % (_w(W10[0]), _w(W10[2]), _w(W10[9])),
   "trade war containers", "Chương 1 – Tháng 4/2025"),
 T(("NĂM PHIÊN SAU", "VẪN CÓ THỂ THẤP HƠN"),
   "Nhìn khung ngắn trước. Năm phiên sau ngày giảm mạnh, có %d trên 10 lần chỉ số còn thấp hơn. Ví dụ phiên %s, năm phiên sau chỉ số còn thấp hơn khoảng %s%%. Nghĩa là trong ngắn hạn, cú giảm thường chưa kết thúc ngay. Ai mua dồn hết tiền ngay trong phiên giảm sẽ phải chịu thêm vài phiên đỏ, và cảm giác đó rất khó chịu. Câu đúc kết: phiên giảm mạnh hiếm khi là phiên cuối cùng, nhưng cũng hiếm khi là ngày tận thế." % (n5, fd(W10[4]['d']), p1(abs(W10[4]['f5']))),
   "red stock board", "Chương 2 – Năm phiên sau"),
 T(("SÁU MƯƠI PHIÊN", "BỨC TRANH KHÁC"),
   "Khung dài hơn thì khác. Hai mươi phiên sau, các mức thay đổi dao động từ khoảng %s%% đến khoảng %s%%. Sáu mươi phiên sau, tức là khoảng ba tháng, mức cao nhất là khoảng %s%%, sau phiên %s. Ba tháng sau phiên giảm %s, chỉ số cao hơn khoảng %s%%. Nếu nhìn bảng này, người bán tháo trong phiên giảm mạnh thường bán ở vùng giá mà ba tháng sau nhìn lại thấy tiếc." % (
       p1(min(w['f20'] for w in W10)), p1(max(w['f20'] for w in W10)), p1(max(w['f60'] for w in W10)), fd(max(W10, key=lambda w: w['f60'])['d']), fd(W10[1]['d']), p1(W10[1]['f60'])),
   "calendar three months", "Chương 3 – Sáu mươi phiên"),
 T(("ĐỪNG VỘI", "KẾT LUẬN"),
   "Đến đây là phần quan trọng nhất. Ba năm này là một giai đoạn VN-Index tăng, từ khoảng 1.061 điểm lên khoảng 1.725 điểm, có lúc lên khoảng 1.928 điểm. Trong một thị trường đi lên, mọi cú giảm đều dễ được lấp lại. Năm 2022 không nằm trong mẫu dữ liệu này. Khi đó, VN-Index giảm từ vùng khoảng 1.500 điểm về dưới 900 điểm, và rất nhiều phiên giảm mạnh được tiếp nối bằng những phiên giảm khác trong nhiều tháng. Thống kê ba năm giống như dự báo thời tiết của mùa khô: rất đúng, cho tới khi mùa mưa đến." ,
   "storm clouds", "Chương 4 – Giới hạn của thống kê"),
 T(("ĐIỀU GÌ", "PHÂN BIỆT"),
   "Vậy điều gì phân biệt một phiên giảm sẽ hồi và một phiên giảm mở đầu cho chuỗi giảm dài? Không có chỉ báo nào chắc chắn. Nhưng có ba câu hỏi đáng kiểm tra. Một, lợi nhuận doanh nghiệp đang tăng hay đang giảm. Năm 2025 và 2026, lợi nhuận nhiều ngân hàng vẫn tăng hai con số. Năm 2022, lãi suất tăng mạnh và lợi nhuận bất động sản sụt. Hai, lãi suất đang đi lên hay đi xuống. Ba, cú giảm do sự kiện bên ngoài, hay do vấn đề nội tại như nợ, thanh khoản, hệ thống ngân hàng." ,
   "magnifying glass report", "Chương 5 – Ba câu hỏi"),
 T(("KẾ HOẠCH", "THẮNG CẢM XÚC"),
   "Bài học không phải là cứ giảm là mua. Bài học là quyết định trong phiên giảm mạnh nên được viết từ trước. Ví dụ: chia tiền mặt dự phòng làm ba phần; phần một dùng khi chỉ số giảm 10%% từ đỉnh, phần hai khi giảm 20%%, phần ba chỉ dùng khi báo cáo quý mới xác nhận lợi nhuận vẫn ổn. Cách này không cần đoán đáy. Nó chỉ cần anh chị không bị buộc phải bán, nhờ tỷ trọng hợp lý và không vay ký quỹ quá tay." ,
   "strategy chess", "Chương 6 – Kế hoạch"),
 T(("NGƯỜI BÁN", "VÌ BỊ ÉP"),
   "Có một nhóm người không có quyền chọn: những người dùng vay ký quỹ cao. Khi chỉ số giảm 6%% trong một phiên, nhiều mã giảm sàn, tài khoản vay sát ngưỡng sẽ bị bán giải chấp, bất kể ba tháng sau giá có hồi hay không. Thống kê 60 phiên chẳng có ý nghĩa gì với họ, vì họ không còn ở đó để nhìn thấy cú hồi. Câu đúc kết: thị trường thưởng cho người kiên nhẫn, nhưng chỉ khi người đó còn đủ tiền để kiên nhẫn." ,
   "empty chair", "Chương 7 – Bán vì bị ép"),
 T(("BẪY HAY GẶP", "BA KIỂU"),
   "Ba kiểu bẫy trong phiên giảm mạnh. Một, bán toàn bộ vì sợ, rồi mua lại ở giá cao hơn vài tuần sau. Hai, mua dồn toàn bộ tiền mặt ngay phiên đầu, rồi hết tiền khi giá giảm thêm. Ba, đọc tin trên mạng xã hội và đổi kế hoạch theo câu chuyện mới nhất. Cả ba đều có chung một gốc: quyết định được đưa ra trong lúc bảng điện toàn màu đỏ." ,
   "social media phone", "Chương 8 – Bẫy hay gặp"),
 T(("CHECKLIST", "PHIÊN GIẢM MẠNH"),
   "Checklist cho phiên giảm mạnh tiếp theo. Một, tỷ lệ vay ký quỹ hiện tại là bao nhiêu, có an toàn nếu giảm thêm 10%% không. Hai, tiền mặt dự phòng có sẵn chưa, chia mấy phần. Ba, danh sách chờ gồm những mã nào, lợi nhuận quý gần nhất ra sao. Bốn, cú giảm do bên ngoài hay do nội tại. Năm, không đặt lệnh nào trong 30 phút đầu tiên sau khi đọc tin xấu. " + WEBL,
   "checklist clipboard", "Chương 9 – Checklist"),
 END(("BÁN KHI SẬP?", "HAY THEO KẾ HOẠCH?"),
   "Số liệu VN-Index đóng cửa ngày từ 27/10/2023 đến 6/11/2026, quá khứ không bảo đảm cho tương lai. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Trong phiên giảm mạnh gần nhất, anh chị đã làm theo kế hoạch viết sẵn hay theo cảm xúc của phiên hôm đó?")])

# ---------------- LST_1611A: Wirecard 2020 ----------------
H2['LST_1611A'] = dict(
 title="Wirecard 2020: 1,9 tỷ euro không tồn tại – công ty trong DAX phá sản sau 7 ngày",
 hook=["1,9 TỶ EURO", "KHÔNG TỒN TẠI?"], badge="BÀI HỌC LỊCH SỬ", seri="Lịch sử & bài học thị trường", nhac='lofi',
 nguon="Nguồn: thông cáo Wirecard AG 18/6, 22/6 và 25/6/2020; báo cáo kiểm toán đặc biệt KPMG (28/4/2020); BaFin; loạt bài Financial Times 2019–2020.",
 tags=["lịch sử thị trường", "Wirecard", "gian lận kế toán", "kiểm toán", "đọc báo cáo tài chính", "DAX"],
 fb=["9/2018: Wirecard vào chỉ số DAX, thay Commerzbank; vốn hóa đỉnh khoảng 24 tỷ euro", "18/6/2020: kiểm toán EY không ký báo cáo năm 2019 – 1,9 tỷ euro tiền gửi không xác minh được", "25/6/2020: nộp đơn phá sản – thành viên DAX đầu tiên vỡ nợ"],
 q="Khi đọc báo cáo một doanh nghiệp Việt Nam, anh chị đã bao giờ so lợi nhuận với dòng tiền kinh doanh và đọc kỹ ý kiến kiểm toán chưa?",
 S=[
 T(("1,9 TỶ EURO", "KHÔNG TỒN TẠI?"), "Ngày 18/6/2020, công ty thanh toán Wirecard của Đức thông báo kiểm toán viên EY không ký báo cáo tài chính năm 2019, vì không xác minh được khoảng 1,9 tỷ euro tiền gửi. Bốn ngày sau, chính Wirecard thừa nhận số tiền đó nhiều khả năng không hề tồn tại. Ngày 25/6/2020, công ty nộp đơn phá sản. Chỉ bảy ngày, một thành viên của chỉ số DAX, nhóm 30 công ty lớn nhất nước Đức, sụp đổ. Xem hết video, anh chị sẽ biết những dấu hiệu nào đã lộ ra từ nhiều năm trước, và cách áp dụng chúng khi đọc báo cáo doanh nghiệp Việt Nam.", "Frankfurt stock exchange", "Mở đầu", moc=True, k='hook'),
 T(("NGÔI SAO", "CÔNG NGHỆ ĐỨC"), "Wirecard được thành lập năm 1999 ở Aschheim, gần Munich, làm dịch vụ xử lý thanh toán thẻ cho các cửa hàng trực tuyến. Đến tháng 9/2018, Wirecard được đưa vào chỉ số DAX, thay chỗ ngân hàng Commerzbank. Ở thời điểm đỉnh, vốn hóa công ty khoảng 24 tỷ euro, lớn hơn cả Deutsche Bank. Báo chí Đức gọi đây là ngôi sao công nghệ hiếm hoi của châu Âu. Người mua cổ phiếu khi đó tin vào một câu chuyện rất đẹp: thanh toán số sẽ thay tiền mặt, và Wirecard đứng ở trung tâm của làn sóng đó.", "Munich skyline", "Chương 1 – Ngôi sao"),
 T(("NHỮNG CẢNH BÁO", "ĐẦU TIÊN"), "Cảnh báo không xuất hiện năm 2020. Từ năm 2015, tờ Financial Times đã đặt câu hỏi về kế toán của Wirecard. Đầu năm 2019, tờ báo đăng loạt bài về nghi vấn ghi khống doanh thu ở văn phòng Singapore. Phản ứng của thị trường lúc đó rất đáng chú ý: cơ quan giám sát tài chính Đức BaFin cấm bán khống cổ phiếu Wirecard trong hai tháng, và lại điều tra chính các nhà báo. Câu móc giữ cho phần sau: khi cơ quan quản lý đứng về phía công ty, nhà đầu tư nhỏ còn biết tin vào ai?", "newspaper printing", "Chương 2 – Cảnh báo"),
 T(("BÊN THỨ BA", "GIỮ TIỀN HỘ"), "Điểm mấu chốt nằm ở mô hình kinh doanh. Một phần lớn lợi nhuận của Wirecard đến từ các đối tác bên thứ ba ở châu Á, những công ty xử lý giao dịch thay Wirecard ở các nước mà Wirecard không có giấy phép. Tiền thu được từ các đối tác này được báo cáo là nằm trong tài khoản ủy thác, cuối cùng là ở hai ngân hàng tại Philippines. Khi kiểm toán hỏi xác nhận, hai ngân hàng này nói các giấy tờ là giả. Ví von đời thường: một cửa hàng báo lãi rất lớn, nhưng tiền lãi luôn nằm ở nhà người quen giữ hộ, và không ai được xem két.", "bank vault", "Chương 3 – Tiền ở đâu"),
 T(("KPMG", "KHÔNG XÁC MINH ĐƯỢC"), "Tháng 10/2019, dưới áp lực, Wirecard thuê KPMG làm kiểm toán đặc biệt. Ngày 28/4/2020, KPMG công bố báo cáo: họ không thể xác minh lợi nhuận từ các đối tác bên thứ ba giai đoạn 2016 đến 2018, vì không nhận được đủ chứng từ. Cổ phiếu giảm mạnh trong ngày, nhưng nhiều người vẫn tin đây chỉ là chuyện thủ tục. Bài học thứ nhất: khi một kiểm toán độc lập nói không xác minh được, đó không phải là chuyện thủ tục. Đó là cảnh báo lớn nhất mà một nhà đầu tư nhỏ có thể đọc được.", "audit documents", "Chương 4 – KPMG"),
 T(("BẢY NGÀY", "SỤP ĐỔ"), "Rồi đến bảy ngày cuối. Ngày 18/6/2020, EY không ký báo cáo năm 2019, cổ phiếu giảm hơn 60%% trong một phiên. Ngày 19/6, tổng giám đốc Markus Braun từ chức. Ngày 22/6, Wirecard thông báo 1,9 tỷ euro nhiều khả năng không tồn tại, Braun bị bắt cùng ngày ở Munich. Giám đốc vận hành Jan Marsalek bỏ trốn và tới nay vẫn bị truy nã. Ngày 25/6/2020, Wirecard nộp đơn phá sản, trở thành thành viên DAX đầu tiên vỡ nợ. Cổ phiếu từng có giá trên 190 euro chỉ còn vài euro.", "police car night", "Chương 5 – Bảy ngày"),
 T(("LỢI NHUẬN", "KHÔNG THÀNH TIỀN"), "Đâu là dấu hiệu có thể thấy trên báo cáo? Thứ nhất, lợi nhuận tăng đều nhưng dòng tiền từ hoạt động kinh doanh không đi theo, phần lớn tiền nằm ở các khoản phải thu và tài khoản ủy thác. Thứ hai, lợi nhuận phụ thuộc vào đối tác mà nhà đầu tư không thể kiểm tra. Thứ ba, công ty phản ứng với câu hỏi bằng cách tấn công người hỏi, thay vì đưa chứng từ. Câu đúc kết: lợi nhuận là ý kiến, tiền mặt là sự thật.", "cash flow chart", "Chương 6 – Dấu hiệu"),
 T(("ÁP DỤNG", "Ở VIỆT NAM"), "Áp dụng cho cổ phiếu Việt Nam thế nào? Bước một, đặt lợi nhuận sau thuế bốn quý cạnh lưu chuyển tiền thuần từ hoạt động kinh doanh bốn quý. Nếu lợi nhuận dương liên tục mà dòng tiền kinh doanh âm nhiều năm, phải đọc thuyết minh xem tiền đang nằm ở đâu. Bước hai, xem các khoản phải thu và trả trước cho người bán có tăng nhanh hơn doanh thu không. Bước ba, đọc trang ý kiến kiểm toán: chấp nhận toàn phần, ngoại trừ, hay từ chối đưa ý kiến. Bước bốn, xem công ty có đổi kiểm toán liên tục không.", "Ho Chi Minh City skyline", "Chương 7 – Áp dụng"),
 T(("Ý KIẾN", "KIỂM TOÁN"), "Ý kiến kiểm toán là trang ngắn nhất nhưng quan trọng nhất của báo cáo năm. Chấp nhận toàn phần là bình thường. Ý kiến ngoại trừ nghĩa là có khoản mục kiểm toán viên không đồng ý hoặc không đủ bằng chứng, và nhà đầu tư cần đọc rõ khoản đó là bao nhiêu so với vốn chủ sở hữu. Từ chối đưa ý kiến là mức cảnh báo cao nhất. Ở Việt Nam, cổ phiếu có thể bị đưa vào diện cảnh báo hay kiểm soát nếu báo cáo năm có ý kiến từ chối hoặc trái ngược. Chỉ năm phút đọc trang này có thể tránh được những năm tháng mắc kẹt.", "accountant desk", "Chương 8 – Kiểm toán"),
 T(("BẪY HAY GẶP", "BA NIỀM TIN"), "Ba niềm tin đã giữ nhà đầu tư ở lại Wirecard. Một, công ty lớn, nằm trong chỉ số hàng đầu thì không thể gian lận. Hai, cơ quan quản lý đã vào cuộc thì chắc là an toàn. Ba, giá giảm vì bị bán khống, không phải vì công ty có vấn đề. Cả ba đều sai. Chỉ số chỉ phản ánh vốn hóa, cơ quan quản lý cũng có thể sai, và giá giảm đôi khi là thị trường đang nói một điều mà báo cáo chưa nói.", "question marks", "Chương 9 – Bẫy niềm tin"),
 T(("CHECKLIST", "NĂM DÒNG"), "Checklist năm dòng sau câu chuyện Wirecard. Một, lợi nhuận bốn quý so với dòng tiền kinh doanh bốn quý. Hai, phải thu tăng nhanh hơn doanh thu hay không. Ba, ý kiến kiểm toán năm gần nhất. Bốn, lợi nhuận có phụ thuộc đối tác khó kiểm chứng không. Năm, công ty trả lời câu hỏi khó bằng số liệu hay bằng lời. Bảng kiểm tra chất lượng lợi nhuận có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.", "checklist notebook", "Chương 10 – Checklist"),
 END(("1,9 TỶ EURO", "BÀI HỌC NÀO?"), "Câu chuyện Wirecard theo thông cáo của công ty, báo cáo KPMG và báo chí tài chính 2019–2020. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Khi đọc báo cáo một doanh nghiệp Việt Nam, anh chị đã bao giờ so lợi nhuận với dòng tiền kinh doanh và đọc kỹ ý kiến kiểm toán chưa?")])

# ---------------- LST_1711A: Evergrande ----------------
RL = {}
for s in ['NLG', 'KDH', 'DXG', 'PDR', 'NVL']:
    g = lambda n: (bq(s, 'bs', n) or [0])[0] or 0
    vn_, vd, v, ts, tien, np_, tr = g('Vay và nợ ngắn hạn'), g('Vay và nợ dài hạn'), g('Vốn chủ sở hữu'), g('TỔNG CỘNG TÀI SẢN'), g('Tiền và các khoản tương đương tiền'), g('Nợ phải trả'), g('Người mua trả tiền trước')
    RL[s] = ((np_ - tr) / (ts - tr) * 100, (vn_ + vd - tien) / v * 100, tien / vn_ if vn_ else 99)
def _rl(s): a, b, c = RL[s]; return "%s: lằn ranh một khoảng %s%%, lằn ranh hai khoảng %s%%, lằn ranh ba khoảng %s lần" % (s, p1(a), vn(b, 0), p2(c))
H2['LST_1711A'] = dict(
 title="Evergrande 2021: nợ hơn 300 tỷ USD – tập đoàn bất động sản Trung Quốc vỡ nợ sau 'ba lằn ranh đỏ'",
 hook=["NỢ 300 TỶ USD?", "3 LẰN RANH ĐỎ"], badge="BÀI HỌC LỊCH SỬ", seri="Lịch sử & bài học thị trường", nhac='lofi',
 nguon="Nguồn: báo cáo tài chính China Evergrande Group (6/2021, 7/2023); Fitch Ratings (9/12/2021); Tòa án Tối cao Hồng Kông (29/1/2024); CSRC (18/3/2024); BCTC Q3/2026 NLG, KDH, DXG, PDR, NVL.",
 tags=["lịch sử thị trường", "Evergrande", "bất động sản Trung Quốc", "ba lằn ranh đỏ", "nợ vay", "cổ phiếu bất động sản"],
 fb=["Giữa 2021: tổng nợ phải trả khoảng 1.970 tỷ nhân dân tệ, hơn 300 tỷ USD", "8/2020: 'ba lằn ranh đỏ' – nợ/tài sản (trừ tiền trả trước) <70%, nợ ròng/vốn <100%, tiền/nợ ngắn hạn >1", "1/2024 tòa Hồng Kông ra lệnh thanh lý"],
 q="Với mã bất động sản anh chị đang theo dõi, anh chị đã thử tính ba lằn ranh từ báo cáo quý gần nhất chưa?",
 S=[
 T(("NỢ 300 TỶ USD?", "3 LẰN RANH ĐỎ"), "Giữa năm 2021, tập đoàn bất động sản Evergrande của Trung Quốc có tổng nợ phải trả khoảng 1.970 tỷ nhân dân tệ, tức là hơn 300 tỷ USD, lớn hơn quy mô cả nền kinh tế của nhiều quốc gia. Chỉ vài tháng sau, Evergrande không trả được lãi trái phiếu USD và bị xếp hạng vỡ nợ. Điều thú vị là cú sụp không bắt đầu bằng một vụ bê bối, mà bằng ba con số đơn giản mà cơ quan quản lý Trung Quốc đặt ra năm 2020. Xem hết video, anh chị sẽ biết ba con số đó là gì, và tự đo được nó cho các doanh nghiệp bất động sản Việt Nam.", "China city skyscrapers", "Mở đầu", moc=True, k='hook'),
 T(("TỪ QUẢNG CHÂU", "ĐẾN 280 THÀNH PHỐ"), "Evergrande được ông Hứa Gia Ấn thành lập năm 1996 ở Quảng Châu, niêm yết trên sàn Hồng Kông năm 2009. Mô hình rất nhanh: vay tiền mua đất, bán nhà khi chưa xây xong để thu tiền trước, rồi dùng tiền đó mua thêm đất. Đỉnh cao, tập đoàn có hơn 1.300 dự án ở hơn 280 thành phố, và mở rộng sang cả xe điện, nước khoáng, đội bóng đá. Ví von đời thường: một người đạp xe càng lúc càng nhanh, vì nếu chậm lại thì xe đổ.", "construction cranes China", "Chương 1 – Mô hình"),
 T(("TIỀN KHÁCH", "LÀ NỢ"), "Điểm then chốt mà nhiều người bỏ qua: tiền khách trả trước khi mua nhà hình thành trong tương lai là một khoản nợ của doanh nghiệp, vì công ty có nghĩa vụ giao nhà. Khi thị trường tốt, khoản này giống như một nguồn vốn miễn phí. Khi thị trường xấu, khách ngừng mua, dòng tiền vào biến mất, nhưng nghĩa vụ xây nhà và trả nợ vẫn còn nguyên. Câu móc giữ cho phần sau: chuyện gì xảy ra khi cơ quan quản lý quyết định đếm lại tất cả các khoản nợ này?", "unfinished apartment buildings", "Chương 2 – Tiền trả trước"),
 T(("BA LẰN RANH", "ĐỎ"), "Tháng 8/2020, cơ quan quản lý Trung Quốc đặt ra ba lằn ranh đỏ cho doanh nghiệp bất động sản. Một, nợ phải trả trừ tiền khách trả trước, chia cho tổng tài sản trừ tiền khách trả trước, không quá 70%%. Hai, nợ vay ròng, tức nợ vay trừ tiền mặt, không quá 100%% vốn chủ sở hữu. Ba, tiền mặt phải lớn hơn nợ vay ngắn hạn. Doanh nghiệp vượt cả ba lằn ranh sẽ không được tăng nợ vay. Evergrande vượt qua cả ba lằn ranh. Cánh cửa vốn đóng lại, và chiếc xe đạp bắt đầu chậm.", "red line warning", "Chương 3 – Ba lằn ranh"),
 T(("VỠ NỢ", "2021"), "Năm 2021 diễn ra rất nhanh. Tháng 9, Evergrande lỡ hạn trả lãi trái phiếu USD. Nhà cung cấp và người mua nhà biểu tình trước trụ sở ở Thâm Quyến. Ngày 9/12/2021, tổ chức xếp hạng Fitch hạ Evergrande xuống mức vỡ nợ có giới hạn. Tháng 7/2023, công ty công bố khoản lỗ cộng dồn hai năm 2021 và 2022 khoảng 582 tỷ nhân dân tệ. Ngày 29/1/2024, tòa án Hồng Kông ra lệnh thanh lý tập đoàn. Tháng 3/2024, cơ quan quản lý chứng khoán Trung Quốc kết luận đơn vị chính của tập đoàn đã khai khống doanh thu khoảng 564 tỷ nhân dân tệ trong hai năm 2019 và 2020.", "courthouse", "Chương 4 – Vỡ nợ"),
 T(("CỔ ĐÔNG", "MẤT GẦN HẾT"), "Người chịu thiệt nhiều nhất là cổ đông và người mua nhà. Cổ phiếu Evergrande mất hơn 99%% giá trị so với đỉnh năm 2017, bị ngừng giao dịch từ đầu năm 2024 và bị hủy niêm yết năm 2025. Hàng trăm nghìn người đã trả tiền nhưng chưa nhận nhà. Câu đúc kết: trong cấu trúc vốn, cổ đông đứng cuối hàng. Khi doanh nghiệp vỡ nợ, chủ nợ còn thương lượng được, còn cổ đông thường chỉ còn lại tờ chứng nhận.", "empty construction site", "Chương 5 – Cổ đông"),
 T(("ĐO BA LẰN RANH", "Ở VIỆT NAM"), "Áp dụng cho Việt Nam. Ba lằn ranh là quy định của Trung Quốc, không phải quy định ở Việt Nam, nhưng là thước đo tham khảo rất tốt. Em tính từ báo cáo tài chính quý 3/2026, số liệu ngày 30/9/2026. " + _rl('NLG') + ". " + _rl('KDH') + ". " + _rl('DXG') + ". Ba doanh nghiệp này đều nằm trong vùng an toàn theo cả ba thước đo.", "Ho Chi Minh City apartments", "Chương 6 – Áp dụng"),
 T(("HAI MÃ", "SÁT LẰN RANH"), "Hai mã khác cho kết quả khác. " + _rl('PDR') + ". " + _rl('NVL') + ". Nợ vay ròng của hai doanh nghiệp này đều vượt 100%% vốn chủ sở hữu, và tiền mặt thấp hơn nhiều so với nợ vay ngắn hạn. Điều này không có nghĩa doanh nghiệp sẽ vỡ nợ, vì còn phụ thuộc vào kế hoạch bán hàng, tái cấu trúc nợ và chính sách. Nhưng nó cho biết biên an toàn mỏng hơn, và nhà đầu tư cần đọc kỹ thuyết minh vay nợ, lịch đáo hạn trái phiếu.", "financial documents", "Chương 6 – Áp dụng"),
 T(("BẪY HAY GẶP", "BA CÂU CHUYỆN"), "Ba câu chuyện từng giữ nhà đầu tư ở lại Evergrande. Một, quá lớn để sụp đổ. Hai, nhà nước sẽ cứu. Ba, quỹ đất rất lớn, bán đất là trả được nợ. Thực tế, quỹ đất chỉ có giá khi có người mua, và trong khủng hoảng, ai cũng muốn bán cùng lúc. Câu đúc kết: tài sản trên báo cáo được ghi theo giá gốc, còn nợ thì được ghi theo đúng số phải trả.", "land plot aerial", "Chương 7 – Bẫy hay gặp"),
 T(("CHECKLIST", "BẤT ĐỘNG SẢN"), "Checklist năm dòng khi đọc một doanh nghiệp bất động sản. Một, tính ba lằn ranh từ bảng cân đối quý mới nhất. Hai, lịch đáo hạn trái phiếu và vay ngân hàng trong 12 tháng tới. Ba, dòng tiền kinh doanh có dương không, hay chỉ sống bằng tiền khách trả trước. Bốn, người mua trả tiền trước đang tăng hay giảm, phản ánh bán hàng mới. Năm, ý kiến kiểm toán. Bảng tính ba lằn ranh có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.", "checklist notebook", "Chương 8 – Checklist"),
 END(("NỢ 300 TỶ USD", "BÀI HỌC NÀO?"), "Câu chuyện Evergrande theo báo cáo công ty, Fitch, tòa án Hồng Kông và cơ quan quản lý chứng khoán Trung Quốc; số liệu Việt Nam từ báo cáo quý 3/2026. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Với mã bất động sản anh chị đang theo dõi, anh chị đã thử tính ba lằn ranh từ báo cáo quý gần nhất chưa?")])

# ---------------- Y3_1611A: 7 lần Fed đổi lãi suất ----------------
_M = hncodec.load(CW + '/data/mac.bin')['fed']['hist']
_vd = [x[0] for x in _v]
def _ds(n): return (_D.date(1970, 1, 1) + _D.timedelta(days=n)).isoformat()
FED = []
for i in range(1, len(_M)):
    d = _ds(_M[i][0]); k = [j for j, x in enumerate(_vd) if x >= d][0]
    FED.append(dict(d=d, lo=_M[i][1], hi=_M[i][2], act='giảm' if _M[i][2] < _M[i - 1][2] else 'tăng', bps=abs(_M[i][2] - _M[i - 1][2]) * 100, c=_v[k][1], f20=(_v[min(k + 20, len(_v) - 1)][1] / _v[k][1] - 1) * 100))
nup = sum(1 for f in FED if f['f20'] > 0)
def _f(f): return "Tháng %d/%s, Fed %s %s điểm cơ bản về %s đến %s%%, VN-Index khoảng %s điểm, 20 phiên sau %s%%" % (int(f['d'][5:7]), f['d'][:4], f['act'], vn(f['bps'], 0), p2(f['lo']), p2(f['hi']), vn(f['c'], 0), pct(f['f20'], 1))
H2['Y3_1611A'] = dict(
 title="7 lần Fed đổi lãi suất 2024–2026: VN-Index 20 phiên sau phản ứng thế nào? %d lần cao hơn, %d lần thấp hơn" % (nup, len(FED) - nup),
 hook=["FED ĐỔI 7 LẦN", "VN-INDEX RA SAO?"], badge="VĨ MÔ DỄ HIỂU", seri="Vĩ mô dễ hiểu", nhac=None,
 nguon="Nguồn: Cục Dự trữ Liên bang Mỹ (các kỳ họp FOMC 9/2024–10/2026); VN-Index đóng cửa ngày HOSE; lợi suất TPCP Mỹ 10 năm, DXY, USD/VND theo dữ liệu thị trường tới 6/11/2026.",
 tags=["Fed", "lãi suất Fed", "VN-Index", "vĩ mô", "tỷ giá", "lợi suất trái phiếu Mỹ"],
 fb=["9/2024–12/2025: Fed giảm 6 lần, từ 5,25–5,5% về 3,5–3,75%; 9/2026 tăng lại 0,25 điểm % về 3,75–4%", "20 phiên sau mỗi lần Fed đổi lãi suất: VN-Index %d lần cao hơn, %d lần thấp hơn" % (nup, len(FED) - nup), "Kỳ họp tới 8–9/12/2026"],
 q="Anh chị có điều chỉnh danh mục theo từng lần Fed họp không, hay theo dõi tỷ giá và lợi nhuận doanh nghiệp là chính?",
 S=[
 T(("FED ĐỔI 7 LẦN", "VN-INDEX RA SAO?"), "Từ tháng 9/2024 tới tháng 10/2026, Cục Dự trữ Liên bang Mỹ đã đổi lãi suất bảy lần: sáu lần giảm và một lần tăng trở lại. Mỗi lần như vậy, mạng xã hội lại đầy những bài viết về dòng tiền ngoại sắp chảy vào hay chảy ra. Em lấy đúng bảy ngày đó, đo VN-Index 20 phiên sau. Kết quả: %d lần chỉ số cao hơn, %d lần thấp hơn. Nghe có vẻ như Fed không quan trọng? Xem hết video, anh chị sẽ thấy Fed tác động theo một đường vòng, và đường vòng đó mới là thứ đáng theo dõi." % (nup, len(FED) - nup), "Federal Reserve building", "Mở đầu", moc=True, k='hook', chart=CH('VNINDEX')),
 T(("LÃI SUẤT FED", "LÀ GÌ"), "Lãi suất Fed là mức lãi các ngân hàng Mỹ cho nhau vay qua đêm, do Fed định hướng. Nó giống như giá gốc của đồng USD. Khi Fed tăng lãi suất, cầm USD gửi ngân hàng Mỹ được trả lãi cao hơn, tiền toàn cầu có xu hướng quay về Mỹ. Khi Fed giảm, tiền dễ đi tìm nơi có lợi suất cao hơn, trong đó có thị trường mới nổi như Việt Nam. Đầu tháng 11/2023, lãi suất Fed ở mức 5,25 đến 5,5%%, cao nhất trong khoảng hai mươi năm.", "US dollar bills", "Chương 1 – Khái niệm"),
 T(("BA LẦN GIẢM", "NĂM 2024"), "Ba lần đổi đầu tiên, năm 2024. " + ". ".join(_f(f) for f in FED[:3]) + ". Điều bất ngờ: Fed giảm mạnh 0,5 điểm phần trăm ngay lần đầu, nhưng VN-Index cuối năm 2024 vẫn quanh 1.250 điểm, gần như đi ngang. Lý do nằm ở chỗ USD lại mạnh lên, chỉ số DXY lên đỉnh khoảng 110 ngày 13/1/2025, và tỷ giá USD/VND tăng.", "stock board Vietnam", "Chương 2 – Năm 2024"),
 T(("BA LẦN GIẢM", "NĂM 2025"), "Ba lần giảm tiếp theo, năm 2025. " + ". ".join(_f(f) for f in FED[3:6]) + ". Lần này, VN-Index đã ở vùng 1.665 đến 1.700 điểm, cao hơn khoảng 30%% so với một năm trước. Phần tăng lớn nhất lại diễn ra trong những tháng Fed đứng yên, từ tháng 4 đến tháng 8/2025. Câu móc: nếu Fed không đổi lãi suất mà thị trường vẫn tăng, thì động lực thật nằm ở đâu?", "Ho Chi Minh City finance", "Chương 3 – Năm 2025"),
 T(("LẦN TĂNG", "THÁNG 9/2026"), "Lần thứ bảy là một lần tăng. " + _f(FED[6]) + ". Đến kỳ họp ngày 28 và 29/10/2026, Fed giữ nguyên lãi suất ở 3,75 đến 4%%, nhưng có hai thành viên muốn tăng thêm. VN-Index đóng cửa ngày 6/11/2026 khoảng 1.725 điểm, thấp hơn đỉnh khoảng 1.928 điểm. Kỳ họp tiếp theo vào ngày 8 và 9/12/2026, kèm dự báo kinh tế mới.", "FOMC meeting", "Chương 4 – Lần tăng"),
 T(("ĐƯỜNG VÒNG 1", "LỢI SUẤT MỸ"), "Đường vòng thứ nhất là lợi suất trái phiếu Chính phủ Mỹ 10 năm, con số các nhà đầu tư lớn dùng để so sánh mọi tài sản. Ba năm trước khoảng 4,66%%, thấp nhất khoảng 3,62%% ngày 16/9/2024, cao nhất khoảng 5,31%% ngày 5/10/2026, và ngày 6/11/2026 khoảng 4,86%%. Điểm đáng chú ý: Fed giảm lãi suất sáu lần, nhưng lợi suất 10 năm hiện cao hơn ba năm trước. Lãi suất ngắn hạn do Fed quyết, lãi suất dài hạn do thị trường quyết, và hai thứ này không phải lúc nào cũng đi cùng nhau.", "US Treasury building", "Chương 5 – Lợi suất Mỹ"),
 T(("ĐƯỜNG VÒNG 2", "TỶ GIÁ"), "Đường vòng thứ hai, và quan trọng nhất với Việt Nam, là tỷ giá. Đầu tháng 11/2023, USD/VND khoảng 24.520 đồng. Tỷ giá lên đỉnh khoảng 26.425 đồng và ngày 6/11/2026 về khoảng 25.580 đồng. Khi tỷ giá chịu áp lực, Ngân hàng Nhà nước khó hạ lãi suất trong nước, và đó là thứ ảnh hưởng trực tiếp tới chi phí vốn của doanh nghiệp và sức mua cổ phiếu. Ví von: Fed là thời tiết ở thượng nguồn, còn tỷ giá và lãi suất trong nước là mực nước ở ngay trước nhà mình.", "river dam", "Chương 6 – Tỷ giá"),
 T(("ĐƯỜNG VÒNG 3", "LỢI NHUẬN"), "Đường vòng thứ ba là lợi nhuận doanh nghiệp. Năm 2025, lợi nhuận nhiều ngân hàng và doanh nghiệp lớn tăng hai con số, và đó là lý do VN-Index tăng mạnh cả trong những tháng Fed đứng yên. Câu đúc kết: lãi suất quyết định người ta trả bao nhiêu cho một đồng lợi nhuận, còn doanh nghiệp quyết định có bao nhiêu đồng lợi nhuận để trả.", "factory workers Vietnam", "Chương 7 – Lợi nhuận"),
 T(("BẪY HAY GẶP", "BA KIỂU ĐỌC TIN"), "Ba kiểu đọc tin Fed dễ dẫn tới quyết định sai. Một, Fed giảm lãi suất là mua, Fed tăng là bán, như một công tắc. Bảng bảy lần ở trên cho thấy điều này không đúng. Hai, phản ứng ngay trong đêm Fed họp, khi thị trường Việt Nam còn đóng cửa và tin đã được phản ánh vào giá thế giới. Ba, bỏ qua câu chữ của Fed về các kỳ tiếp theo, trong khi thị trường thường phản ứng với dự báo nhiều hơn quyết định.", "newspaper headlines", "Chương 8 – Bẫy hay gặp"),
 T(("CHECKLIST", "SAU MỖI KỲ HỌP"), "Checklist sau mỗi kỳ họp Fed. Một, quyết định và tỷ lệ biểu quyết, có ai phản đối không. Hai, lợi suất Mỹ 10 năm phản ứng thế nào trong tuần đó. Ba, chỉ số DXY và tỷ giá USD/VND. Bốn, lãi suất tiền gửi trong nước có thay đổi không. Năm, quay lại với lợi nhuận quý của các mã mình nắm giữ. Bảng theo dõi vĩ mô cập nhật hằng ngày có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.", "checklist notebook", "Chương 9 – Checklist"),
 END(("FED ĐỔI LÃI SUẤT", "ANH CHỊ LÀM GÌ?"), "Số liệu Fed, VN-Index, lợi suất Mỹ và tỷ giá tới ngày 6/11/2026. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Anh chị có điều chỉnh danh mục theo từng lần Fed họp không, hay theo dõi tỷ giá và lợi nhuận doanh nghiệp là chính?")])

# ---------------- Y3_1711A: 3 năm, 8 tài sản ----------------
_W = {s[0]: s for s in hncodec.load(CW + '/data/wm.bin')['s']}
def _st3(dts, v):
    pk = v[0]; mdd = 0; a = b = None; pkd = dts[0]
    for t, x in zip(dts, v):
        if x > pk: pk = x; pkd = t
        if (pk - x) / pk > mdd: mdd = (pk - x) / pk; a = (pkd, pk); b = (t, x)
    r = [v[i] / v[i - 1] - 1 for i in range(1, len(v))]
    return dict(ret=(v[-1] / v[0] - 1) * 100, mdd=mdd * 100, a=a, b=b, vol=_st.pstdev(r) * _m.sqrt(250) * 100, v0=v[0], v1=v[-1])
AS = {}
for k in ['spx', 'ixic', 'n225', 'kospi', 'gold', 'btc', 'brent']:
    s = _W[k]; dts = [_ds(x) for x in s[5]]; AS[k] = _st3(dts, s[6])
AS['vni'] = _st3([x[0] for x in _v], [x[1] for x in _v])
NM = dict(spx='S&P 500', ixic='Nasdaq', n225='Nikkei 225', kospi='KOSPI', gold='vàng', btc='Bitcoin', brent='dầu Brent', vni='VN-Index')
def _a(k): x = AS[k]; return "%s tăng khoảng %s%%, sụt sâu nhất khoảng %s%%" % (NM[k], p1(x['ret']), p1(x['mdd']))
K = AS['kospi']
H2['Y3_1711A'] = dict(
 title="3 năm, 8 tài sản: KOSPI +%s%% nhưng có lúc −%s%%, VN-Index +%s%% sụt sâu nhất %s%% – lợi nhuận nào đáng giá hơn?" % (vn(K['ret'], 0), p1(K['mdd']), p1(AS['vni']['ret']), p1(AS['vni']['mdd'])),
 hook=["KOSPI +%s%%?" % vn(K['ret'], 0), "CÓ LÚC −%s%%" % p1(K['mdd'])], badge="VĨ MÔ DỄ HIỂU", seri="Vĩ mô dễ hiểu", nhac=None,
 nguon="Nguồn: giá đóng cửa ngày S&P 500, Nasdaq, Nikkei 225, KOSPI, vàng, Bitcoin, dầu Brent, VN-Index 11/2023–6/11/2026; tính toán lợi nhuận, mức sụt từ đỉnh và độ biến động năm của Chứng Khoán Huy Nguyễn.",
 tags=["vĩ mô", "phân bổ tài sản", "KOSPI", "VN-Index", "vàng", "Bitcoin", "độ biến động"],
 fb=[_a('kospi'), _a('vni'), _a('btc')],
 q="Nếu được chọn lại ba năm trước, anh chị chọn tài sản tăng nhiều nhất hay tài sản mình đủ bình tĩnh để giữ suốt ba năm?",
 S=[
 T(("KOSPI +%s%%?" % vn(K['ret'], 0), "CÓ LÚC −%s%%" % p1(K['mdd'])), "Ba năm qua, chỉ số KOSPI của Hàn Quốc tăng khoảng %s%%, từ khoảng %s điểm lên khoảng %s điểm ngày 6/11/2026. Con số này nghe rất hấp dẫn. Nhưng nếu ai mua ở đỉnh khoảng %s điểm ngày %s, tới ngày 6/11/2026 họ đang lỗ khoảng %s%%. Cùng ba năm đó, VN-Index tăng khoảng %s%%, ít hơn, nhưng mức sụt sâu nhất tính theo giá đóng cửa chỉ khoảng %s%%. Video này đặt tám tài sản cạnh nhau, đo cả phần thưởng lẫn cái giá phải trả. Xem hết video, anh chị sẽ có một câu hỏi rất khác khi chọn tài sản." % (
       vn(K['ret'], 0), vn(K['v0'], 0), vn(K['v1'], 0), vn(K['a'][1], 0), fd(K['a'][0]), p1(K['mdd']), p1(AS['vni']['ret']), p1(AS['vni']['mdd'])), "Seoul skyline", "Mở đầu", moc=True, k='hook', chart=CH('VNINDEX')),
 T(("HAI CON SỐ", "PHẢI ĐI CÙNG"), "Mỗi tài sản em đo hai con số. Con số thứ nhất là lợi nhuận ba năm, từ đầu tháng 11/2023 tới ngày 6/11/2026. Con số thứ hai là mức sụt sâu nhất từ đỉnh, tức là nếu không may mua ở đỉnh, anh chị đã từng lỗ trên giấy bao nhiêu. Con số thứ nhất là thứ người ta khoe. Con số thứ hai là thứ quyết định người ta có giữ nổi hay không. Ví von đời thường: một con đường đẹp chưa chắc đã dễ đi, phải hỏi thêm nó có bao nhiêu đoạn đèo.", "mountain road", "Chương 1 – Hai con số"),
 T(("MỸ", "S&P 500 VÀ NASDAQ"), "Nhóm Mỹ trước. " + _a('spx') + ", đoạn sụt đó từ ngày %s tới ngày %s. " % (fd(AS['spx']['a'][0]), fd(AS['spx']['b'][0])) + _a('ixic') + ". Nasdaq tăng nhiều hơn nhưng cũng giảm sâu hơn, vì chứa nhiều cổ phiếu công nghệ có định giá cao. Cả hai cú sụt lớn nhất đều rơi vào cùng một giai đoạn đầu tháng 4/2025.", "Wall Street", "Chương 2 – Mỹ"),
 T(("CHÂU Á", "NHẬT VÀ HÀN"), "Nhóm châu Á. " + _a('n225') + ". " + _a('kospi') + ". KOSPI có một hành trình đặc biệt: từ khoảng %s điểm lên đỉnh khoảng %s điểm ngày %s, tức là hơn gấp ba, rồi giảm khoảng %s%% chỉ trong khoảng bốn tháng. Câu móc: thị trường tăng nhanh nhất cũng thường là thị trường giảm nhanh nhất." % (vn(K['v0'], 0), vn(K['a'][1], 0), fd(K['a'][0]), p1(K['mdd'])), "Tokyo stock exchange", "Chương 3 – Châu Á"),
 T(("HÀNG HÓA", "VÀNG VÀ DẦU"), "Nhóm hàng hóa. " + _a('gold') + ", từ đỉnh khoảng %s USD một ounce ngày %s. " % (vn(AS['gold']['a'][1], 0), fd(AS['gold']['a'][0])) + _a('brent') + ". Dầu Brent là ví dụ rõ nhất cho việc lợi nhuận ba năm không kể hết câu chuyện: điểm đầu và điểm cuối không cách nhau nhiều, nhưng ở giữa có những đoạn giảm gần 40%%. Độ biến động năm của dầu khoảng %s%%, cao gấp đôi vàng." % p1(AS['brent']['vol']), "gold bars", "Chương 4 – Hàng hóa"),
 T(("BITCOIN", "PHẦN THƯỞNG VÀ CÁI GIÁ"), _a('btc') + ". Bitcoin lên đỉnh khoảng %s USD ngày %s, rồi về khoảng %s USD ngày %s. Độ biến động năm khoảng %s%%. Nghĩa là mỗi đồng lợi nhuận của Bitcoin đi kèm những đoạn đường mà rất ít người giữ nổi, nhất là khi dùng tiền vay." % (vn(AS['btc']['a'][1], 0), fd(AS['btc']['a'][0]), vn(AS['btc']['b'][1], 0), fd(AS['btc']['b'][0]), p1(AS['btc']['vol'])), "bitcoin coin", "Chương 5 – Bitcoin"),
 T(("VN-INDEX", "Ở ĐÂU"), _a('vni') + ", đoạn sụt đó từ ngày %s tới ngày %s. Độ biến động năm khoảng %s%%, thấp hơn Nasdaq, Nikkei, KOSPI và Bitcoin. Điều bất ngờ với nhiều người: trong ba năm này, VN-Index không phải là thị trường nhiều sóng gió nhất, nếu đo bằng giá đóng cửa. Nhưng từng mã riêng lẻ thì khác hẳn, nhiều cổ phiếu Việt Nam có mức sụt trên 50%% trong cùng giai đoạn." % (fd(AS['vni']['a'][0]), fd(AS['vni']['b'][0]), p1(AS['vni']['vol'])), "Ho Chi Minh City skyline", "Chương 6 – VN-Index"),
 T(("TỶ LỆ", "THƯỞNG TRÊN ĐAU"), "Một cách so sánh đơn giản: lấy lợi nhuận ba năm chia cho mức sụt sâu nhất. Con số càng cao, mỗi đơn vị đau đớn mang lại càng nhiều phần thưởng. " + ". ".join("Tỷ lệ của %s khoảng %s" % (NM[k], p2(AS[k]['ret'] / AS[k]['mdd'])) for k in ['vni', 'spx', 'ixic', 'n225', 'kospi', 'gold', 'btc']) + ". Không có tài sản nào thắng ở mọi thước đo. Câu đúc kết: lợi nhuận cao nhất chỉ có ý nghĩa nếu anh chị còn ở đó vào ngày cuối.", "balance scale", "Chương 7 – Thưởng trên đau"),
 T(("PHÂN BỔ", "KHÔNG DỒN MỘT"), "Bài học cho phân bổ tài sản. Thứ nhất, các cú sụt không xảy ra cùng lúc: vàng sụt mạnh nhất năm 2026, KOSPI cũng năm 2026, còn S&P 500 và VN-Index sụt mạnh nhất tháng 4/2025. Đặt các tài sản có nhịp khác nhau cạnh nhau giúp danh mục bớt chao đảo. Thứ hai, tỷ trọng tài sản nhiều biến động như Bitcoin nên nhỏ, để cú sụt 50%% chỉ làm danh mục mất vài phần trăm. Thứ ba, với nhà đầu tư Việt Nam, rủi ro tỷ giá cũng là một phần của lợi nhuận khi nắm tài sản nước ngoài.", "portfolio pie chart", "Chương 8 – Phân bổ"),
 T(("BẪY HAY GẶP", "BA KIỂU"), "Ba bẫy khi nhìn bảng lợi nhuận ba năm. Một, chọn tài sản tăng nhiều nhất ba năm qua và nghĩ ba năm tới sẽ lặp lại, như mua KOSPI ở vùng đỉnh năm 2026. Hai, quên mức sụt từ đỉnh, nên đặt tỷ trọng quá lớn. Ba, so sánh mà bỏ quên tỷ giá và chi phí giao dịch khi đầu tư ra nước ngoài.", "rear view mirror", "Chương 9 – Bẫy hay gặp"),
 T(("CHECKLIST", "TRƯỚC KHI CHỌN"), "Checklist trước khi thêm một tài sản vào danh mục. Một, lợi nhuận ba năm. Hai, mức sụt sâu nhất từ đỉnh. Ba, độ biến động năm. Bốn, tài sản này sụt vào lúc nào, có trùng với các tài sản mình đang có không. Năm, nếu nó sụt đúng bằng mức sâu nhất trong quá khứ, danh mục của mình mất bao nhiêu phần trăm. Bảng giá thế giới và hàng hóa cập nhật hằng ngày có miễn phí trên trang chứng khoán Huy Nguyễn chấm com.", "checklist notebook", "Chương 10 – Checklist"),
 END(("TĂNG NHIỀU NHẤT?", "HAY GIỮ ĐƯỢC LÂU?"), "Số liệu giá đóng cửa ngày tám tài sản từ tháng 11/2023 đến 6/11/2026, quá khứ không bảo đảm cho tương lai. Cần trao đổi riêng về danh mục: Zalo 0365.188.286. Nếu được chọn lại ba năm trước, anh chị chọn tài sản tăng nhiều nhất hay tài sản mình đủ bình tĩnh để giữ suốt ba năm?")])
