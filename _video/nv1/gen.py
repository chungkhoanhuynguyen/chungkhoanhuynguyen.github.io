# -*- coding: utf-8 -*-
# NV1 – sinh kịch bản video dài theo số liệu thật (Đọc BCTC kênh chính, HI, Y2, TS, K2). Viết số bằng chữ số, doc() đổi sang chữ.
import statistics as st
from lib import *
TEN = {'NAB': 'Nam A Bank', 'KLB': 'Kienlongbank', 'VAB': 'VietABank', 'GAS': 'PV Gas', 'VJC': 'Vietjet', 'DPM': 'Đạm Phú Mỹ', 'HVN': 'Vietnam Airlines',
       'KDH': 'Nhà Khang Điền', 'GMD': 'Gemadept', 'VSC': 'Viconship', 'VNM': 'Vinamilk', 'DHG': 'Dược Hậu Giang', 'PVD': 'PV Drilling', 'BSR': 'Lọc hóa dầu Bình Sơn',
       'PLX': 'Petrolimex', 'PVT': 'PVTrans', 'QNS': 'Đường Quảng Ngãi', 'VEA': 'VEAM', 'SSB': 'SeABank', 'DCM': 'Đạm Cà Mau', 'REE': 'REE', 'PVP': 'Vận tải dầu khí Thái Bình Dương', 'LPB': 'LPBank', 'BMP': 'Nhựa Bình Minh'}
ANH = {'bank': 'bank building', 'GAS': 'gas pipeline', 'VJC': 'airplane runway', 'HVN': 'airplane runway', 'DPM': 'fertilizer plant', 'KDH': 'residential buildings Vietnam',
       'GMD': 'container port', 'VSC': 'container port', 'VNM': 'dairy farm', 'DHG': 'pharmaceutical factory', 'PVD': 'oil drilling rig'}
NGAY_DL = "6/11/2026"
WEB = ["Bảng định giá và báo cáo tài chính đầy đủ của mã này có trên trang chứng khoán Huy Nguyễn chấm com, mục tra cứu mã.",
       "Anh chị có thể mở trang chứng khoán Huy Nguyễn chấm com để xem lại từng con số trong video này.",
       "Bài viết kèm video và bảng số có trong thư viện bài học trên chứng khoán Huy Nguyễn chấm com."]
def S_(k, ch, cap, say, **kw):
    d = {'k': k, 'ch': ch, 'label': kw.pop('label', ''), 'cap': tuple(cap), 'cols': CC, 'say': doc(say)}; d.update(kw); return d
def info(s):
    x = KQ[s]; f = fund(s); c = close(s); h = x['h'][-8:]
    lines = x['info']; dd = (f['h52'] - c) / f['h52'] * 100 if f.get('h52') else 0
    sec = SEC.get(s, ''); peers = [p for p in FD if SEC.get(p) == sec and fund(p).get('mc', 0) >= 1500 and fund(p).get('pe', 0) > 0]
    med = lambda k: st.median([fund(p)[k] for p in peers]) if len(peers) >= 3 else None
    return dict(s=s, ten=TEN.get(s, s), x=x, f=f, c=c, h=h, dd=dd, can=dd / (100 - dd) * 100, sec=sec, npeer=len(peers), mpe=med('pe'), mpb=med('pb'), mroe=med('roe'), bank=x['form'] == 'bank')
def gia(c): return vn(c, 2 if c < 100 else 1)
def bars(h, i, last_col=GREEN): return [(a[0], a[i], (last_col if j == len(h) - 1 else (RED if a[i] < 0 else BLUE)), vn(a[i], 0)) for j, a in enumerate(h)]
def chuoi(h, i, ten):
    v = [a[i] for a in h]; up = sum(1 for j in range(1, len(v)) if v[j] > v[j - 1])
    hi = max(range(len(v)), key=lambda j: v[j]); lo = min(range(len(v)), key=lambda j: v[j])
    t = "Trong tám quý từ %s đến %s, %s cao nhất ở %s với khoảng %s tỷ, thấp nhất ở %s với khoảng %s tỷ, và có %d quý tăng so với quý liền trước. " % (h[0][0], h[-1][0], ten, h[hi][0], vn(v[hi], 0), h[lo][0], vn(v[lo], 0), up)
    t += "Bốn quý gần nhất lần lượt là " + ", ".join("%s %s %s tỷ" % (a[0], "lỗ" if a[i] < 0 else "đạt", vn(abs(a[i]), 0)) for a in h[-4:]) + ". "
    return t
def hook_chart(s, wk): return {'sym': s + 'W', 'tf': 'W', 'weeks': 52, 'circles': circles(wk)}
def risk_lines(I):
    b = [l for l in I['x']['bad']]
    return b[:3]

# ================= ĐỌC BCTC 5 PHÚT (kênh chính) =================
def doc_bctc(key, s, ngay, gio, PX):
    I = info(s); x = I['x']; f = I['f']; c = I['c']; wk = weekly(s); PX[s + 'W'] = wk
    q = x['info'][0]; m = re.search(r"([\d.]+) tỷ \(([+−][\d,]+)%", q); lnq = m.group(1) + " tỷ" if m else ""; g = m.group(2) if m else ""
    lk = x['info'][1]; m2 = re.search(r"\(([+−][\d,]+%|gấp [\d,]+ lần)\)", lk); glk = m2.group(1) if m2 else ""
    ten = I['ten']; bank = I['bank']
    h1 = ("LÃI QUÝ %s%%" % g) if g else "QUÝ 3 LỖ"; h2 = "P/B %s" % vn(f['pb'], 2) if bank else "P/E %s" % vn(f['pe'], 2)
    title = "Đọc BCTC 5 phút | %s: lãi quý %s%%, lũy kế 9 tháng %s – %s" % (s, g, glk, h2.replace("P/B", "P/B").replace("P/E", "P/E")) if g else "Đọc BCTC 5 phút | %s: quý 3 lỗ, lũy kế 9 tháng %s – %s" % (s, glk, h2)
    link = "https://chungkhoanhuynguyen.com/hoc/%s.html" % slug(title)
    sc = []
    say = ("%s, mã %s, báo %s. %s Cổ phiếu đóng cửa ngày %s ở khoảng %s nghìn đồng, thấp hơn đỉnh 52 tuần khoảng %s%%. "
           "Con số quý này có đủ để kết luận doanh nghiệp đang khỏe lên hay yếu đi không? Trong video này, em đọc lần lượt lợi nhuận tám quý, %s, %s, định giá, rủi ro cần theo dõi và cách quản trị vốn khi nắm giữ %s. "
           "Số liệu lấy từ báo cáo tài chính Q3/2026 và dữ liệu tổng hợp ngày %s.") % (
        ten, s, noi(q)[0].lower() + noi(q)[1:].rstrip("."), noi(lk), NGAY_DL, gia(c), vn(I['dd'], 1), "thu nhập lãi thuần" if bank else "doanh thu và biên lợi nhuận",
        "dự phòng và nợ xấu" if bank else "chi phí lãi vay và dòng tiền", s, NGAY_DL)
    sc.append(S_('hook', 'Mở đầu', (h1, h2), say, moc=True, label="%s – đọc BCTC" % s, anh=ANH.get(s, ANH['bank'] if bank else 'factory'), chart=hook_chart(s, wk)))
    say = "Chương một, lợi nhuận tám quý. " + chuoi(I['h'], 1, "lợi nhuận sau thuế công ty mẹ") + \
          "Khi đọc chuỗi này, anh chị đừng chỉ so với cùng kỳ năm trước. Hãy so thêm với quý liền trước và với lũy kế chín tháng, vì một quý có thể đẹp lên nhờ khoản thu bất thường, nhờ trích lập dự phòng ít đi, hoặc nhờ nền so sánh thấp. Chuỗi tám quý cho thấy lợi nhuận đang đi lên đều, đi ngang hay dao động mạnh, và đó mới là thứ giúp ước lượng quý tiếp theo."
    sc.append(S_('bars', 'Chương 1 – Lợi nhuận tám quý', ('LỢI NHUẬN', 'TÁM QUÝ'), say, moc=True, anh='financial chart', bars=bars(I['h'], 1)))
    third = x['info'][2] if len(x['info']) > 2 else ""
    if bank:
        dv = [l for l in x['good'] + x['bad'] if 'dịch vụ' in l]
        say = ("Chương hai, thu nhập lãi thuần, tức phần chênh lệch giữa lãi cho vay thu vào và lãi huy động trả ra. Đây là mảng cốt lõi của ngân hàng. %s " % noi(third)) + chuoi(I['h'], 2, "thu nhập lãi thuần") + \
              ("%s " % noi(dv[0]) if dv else "") + \
              "Khi lợi nhuận tăng mà thu nhập lãi thuần giảm, phần tăng thêm đến từ nơi khác: dịch vụ, kinh doanh chứng khoán, thu hồi nợ đã xử lý, hoặc chi phí dự phòng thấp hơn. Những nguồn này thường kém đều hơn mảng cho vay, nên anh chị cần hỏi: quý sau nguồn đó có lặp lại không?"
        sc.append(S_('bars', 'Chương 2 – Thu nhập lãi thuần', ('THU NHẬP', 'LÃI THUẦN'), say, anh='bank loan', bars=bars(I['h'], 2)))
        nx = [l for l in x['info'] + x['good'] + x['bad'] if any(k in l for k in ('nợ xấu', 'dự phòng', 'Bao phủ', 'NIM'))]
        say = "Chương ba, dự phòng và nợ xấu. " + " ".join(noi(l) for l in nx[:4]) + \
              " Tỷ lệ bao phủ nợ xấu là số dự phòng đã trích chia cho tổng nợ xấu. Bao phủ một trăm phần trăm nghĩa là nếu toàn bộ nợ xấu mất trắng, ngân hàng đã có sẵn tiền dự phòng để bù. Bao phủ càng thấp thì bộ đệm càng mỏng, và lợi nhuận tương lai càng dễ bị bào mòn khi phải trích lập thêm. Hai con số này anh chị tra được trong thuyết minh báo cáo tài chính, mục chất lượng nợ cho vay."
        sc.append(S_('cards', 'Chương 3 – Dự phòng và nợ xấu', ('DỰ PHÒNG', 'VÀ NỢ XẤU'), say, moc=True, anh='risk management',
                     cards=[(l.split(', ')[0][:34], '', '') for l in nx[:3]] or [('Nợ xấu', 'xem thuyết minh', '')]))
    else:
        bg = [l for l in x['good'] + x['bad'] if 'Biên' in l]; lv = [l for l in x['good'] + x['bad'] if 'lãi vay' in l]
        say = "Chương hai, doanh thu và biên lợi nhuận. %s " % noi(third) + chuoi(I['h'], 2, "doanh thu thuần") + ("%s " % noi(bg[0]) if bg else "") + \
              "Doanh thu cho biết doanh nghiệp bán được bao nhiêu, còn biên lợi nhuận gộp cho biết mỗi một trăm đồng doanh thu còn lại bao nhiêu đồng sau giá vốn. Doanh thu tăng mà biên co lại thường là dấu hiệu giá bán chịu áp lực hoặc chi phí đầu vào tăng nhanh hơn. Biên mở rộng mà doanh thu đi ngang thì lợi nhuận vẫn có thể tăng, nhưng mức tăng đó phụ thuộc vào giá đầu vào, thứ doanh nghiệp không kiểm soát hoàn toàn."
        sc.append(S_('bars', 'Chương 2 – Doanh thu tám quý', ('DOANH THU', 'TÁM QUÝ'), say, anh=ANH.get(s, 'factory'), bars=bars(I['h'], 2)))
        lvv = bq(s, 'is', 'Trong đó: Chi phí lãi vay') or []; cfo = bq(s, 'cf', 'Lưu chuyển tiền thuần từ hoạt động kinh doanh') or []
        lv4 = sum(lvv[:4]) if lvv else 0; cf4 = sum(cfo[:4]) if cfo else 0; ln4 = sum(a[1] for a in I['h'][-4:])
        say = ("Chương ba, chi phí lãi vay và dòng tiền. Bốn quý gần nhất, chi phí lãi vay cộng lại khoảng %s tỷ. %s"
               "Cũng trong bốn quý đó, lợi nhuận sau thuế cộng lại khoảng %s tỷ, còn dòng tiền thuần từ hoạt động kinh doanh cộng lại khoảng %s tỷ. ") % (
            vn(lv4, 0), (noi(lv[0]) + " ") if lv else "", vn(ln4, 0), ("âm " if cf4 < 0 else "") + vn(abs(cf4), 0))
        say += ("Dòng tiền kinh doanh cao hơn lợi nhuận là dấu hiệu lợi nhuận được thu về bằng tiền thật. " if cf4 >= ln4 else
                "Dòng tiền kinh doanh thấp hơn lợi nhuận nghĩa là một phần lợi nhuận còn nằm ở khoản phải thu, hàng tồn kho hoặc khoản trả trước, chưa về thành tiền. Một vài quý như vậy là bình thường, nhưng kéo dài nhiều quý thì anh chị cần soi kỹ thuyết minh. ")
        say += "Doanh nghiệp vay càng nhiều thì khi lãi suất tăng, phần lợi nhuận dành cho cổ đông càng bị chia sẻ cho chủ nợ."
        sc.append(S_('cards', 'Chương 3 – Lãi vay và dòng tiền', ('LÃI VAY', 'VÀ DÒNG TIỀN'), say, moc=True, anh='cash flow',
                     cards=[('Lãi vay 4 quý', '≈ %s tỷ' % vn(lv4, 0), ''), ('LNST 4 quý', '≈ %s tỷ' % vn(ln4, 0), ''), ('Dòng tiền KD 4 quý', '≈ %s tỷ' % vn(cf4, 0), '')]))
    pe, pb, roe = f['pe'], f['pb'], f['roe']
    say = "Chương bốn, định giá. Với giá khoảng %s nghìn đồng, %s có P/E khoảng %s lần, P/B khoảng %s lần, ROE khoảng %s%%. " % (gia(c), s, vn(pe, 2), vn(pb, 2), vn(roe, 1))
    if I['mpe']:
        say += "Trong %d mã cùng nhóm %s có vốn hóa từ 1.500 tỷ, P/E trung vị khoảng %s lần, P/B trung vị khoảng %s lần, ROE trung vị khoảng %s%%. " % (I['npeer'], I['sec'].lower(), vn(I['mpe'], 2), vn(I['mpb'], 2), vn(I['mroe'], 1))
    say += ("Với ngân hàng, P/B nên đọc cùng ROE. Một ngân hàng có ROE cao xứng đáng được trả P/B cao hơn, còn P/B thấp kèm ROE thấp thì chưa chắc là rẻ. " if bank else
            "P/E chỉ có ý nghĩa khi lợi nhuận bốn quý gần nhất phản ánh đúng sức kiếm tiền bình thường. Nếu có quý đột biến hoặc quý lỗ, P/E sẽ bị méo, khi đó anh chị nên tính lại với lợi nhuận đã loại phần bất thường. ") + WEB[0]
    sc.append(S_('cards', 'Chương 4 – Định giá', ('BA CON SỐ', 'ĐỊNH GIÁ'), say, anh='calculator',
                 cards=[('P/E', vn(pe, 2), 'lần'), ('P/B', vn(pb, 2), 'lần'), ('ROE', vn(roe, 1) + '%', 'trên vốn chủ')]))
    say = ("Chương năm, giá cách đỉnh bao xa. Đỉnh 52 tuần của %s khoảng %s nghìn đồng, đáy khoảng %s nghìn đồng. Giá hiện tại thấp hơn đỉnh khoảng %s%%. "
           "Người mua ở đỉnh cần cổ phiếu tăng khoảng %s%% mới hòa vốn. Đây là toán học của thua lỗ: giảm càng sâu thì phần tăng cần thiết để hồi lại càng lớn hơn phần đã mất. "
           "Hệ số beta của %s khoảng %s, nghĩa là trong giai đoạn đo, giá dao động %s thị trường chung. Beta không nói cổ phiếu tốt hay xấu, nó chỉ nói mức rung lắc mà anh chị phải chịu được.") % (
        s, vn(f['h52'], 2), vn(f['l52'], 2), vn(I['dd'], 1), vn(I['can'], 0), s, vn(f['beta'], 2), "ít hơn" if f['beta'] < 1 else "mạnh hơn")
    sc.append(S_('bignum', 'Chương 5 – Cách đỉnh 52 tuần', ('CÁCH ĐỈNH', '52 TUẦN'), say, moc=True, value=-round(I['dd'], 1), fmt='{:,.1f}', unit='%',
                 top='ĐỈNH %s – NAY %s' % (vn(f['h52'], 2), gia(c)), sub='cần +%s%% để về đỉnh' % vn(I['can'], 0), col=RED))
    rl = risk_lines(I)
    say = "Chương sáu, rủi ro cần theo dõi. " + (" ".join(noi(l) for l in rl) if rl else "Báo cáo quý này không có dòng nào xấu rõ rệt, nhưng đó không phải lý do để bỏ qua phần rủi ro. ") + \
          (" Với cổ phiếu ngân hàng, rủi ro lớn nhất thường không nằm ở một quý lợi nhuận, mà ở chất lượng tài sản: nợ xấu, nợ tái cơ cấu và mức độ tập trung cho vay vào bất động sản. Ngoài ra, cổ phiếu ngân hàng hay biến động cùng nhau, nên anh chị cần cộng tỷ trọng cả nhóm ngân hàng trong danh mục." if bank else
           " Với doanh nghiệp sản xuất và dịch vụ, ba rủi ro cần theo dõi là giá đầu vào, nợ vay và sức mua của khách hàng. Một quý tăng trưởng không xóa được rủi ro chu kỳ, nên anh chị hãy hỏi: nếu giá đầu vào quay lại mức cũ, biên lợi nhuận còn bao nhiêu?")
    sc.append(S_('checklist', 'Chương 6 – Rủi ro cần theo dõi', ('RỦI RO', 'CẦN THEO DÕI'), say, anh='warning sign',
                 items=[(l.split(', ')[0][:40], RED) for l in rl[:3]] + [('Tỷ trọng cả nhóm ngành', GOLD)]))
    say = ("Chương bảy, quản trị vốn khi nắm giữ %s. Em đề xuất ba câu hỏi phải trả lời trước khi mua. Một, mã này chiếm tối đa bao nhiêu phần trăm danh mục? Với một mã đơn lẻ, nhiều nhà đầu tư cá nhân giới hạn trong khoảng 10 đến 20%%. "
           "Hai, nếu giá quay về đáy 52 tuần khoảng %s nghìn đồng, tức thấp hơn giá hiện tại khoảng %s%%, thì danh mục mất bao nhiêu? Với tỷ trọng 10%%, mức giảm đó làm danh mục mất khoảng %s%%. "
           "Ba, điều gì xảy ra thì luận điểm sai? Ví dụ lợi nhuận hai quý liên tiếp giảm, hoặc %s xấu đi. Viết sẵn ba câu trả lời này ra giấy, anh chị sẽ bớt bị cảm xúc kéo đi khi giá biến động. Không dùng vay ký quỹ cho mã mình chưa trả lời được câu hỏi thứ ba.") % (
        s, vn(f['l52'], 2), vn(max(0, (c - f['l52']) / c * 100), 1), vn(max(0, (c - f['l52']) / c * 10), 1), "nợ xấu" if bank else "biên lợi nhuận")
    sc.append(S_('cards', 'Chương 7 – Quản trị vốn', ('QUẢN TRỊ VỐN', 'TRƯỚC KHI MUA'), say, moc=True, anh='balance scale',
                 cards=[('Tỷ trọng tối đa', '10–20%', 'một mã'), ('Nếu về đáy 52 tuần', '−%s%%' % vn(max(0, (c - f['l52']) / c * 100), 1), 'giá cổ phiếu'), ('Điểm sai', 'viết trước', 'khi mua')]))
    steps = (['Lợi nhuận 8 quý, lũy kế', 'Thu nhập lãi thuần', 'Dự phòng, nợ xấu, bao phủ', 'P/B cạnh ROE', 'Tỷ trọng và điểm sai'] if bank else
             ['Lợi nhuận 8 quý, lũy kế', 'Doanh thu và biên gộp', 'Lãi vay và dòng tiền', 'P/E cạnh tăng trưởng', 'Tỷ trọng và điểm sai'])
    say = "Chương tám, năm bước anh chị có thể tự làm với mọi báo cáo %s. Một, %s. Hai, %s. Ba, %s. Bốn, %s. Năm, %s. %s" % (
        "ngân hàng" if bank else "doanh nghiệp", *[(t[0].lower() + t[1:]) if t[1:2].islower() else t for t in steps], WEB[2])
    sc.append(S_('checklist', 'Chương 8 – Năm bước tự đọc', ('NĂM BƯỚC', 'TỰ ĐỌC BCTC'), say, anh='checklist notebook', items=[(t, GREEN) for t in steps]))
    say = "Số liệu trong video lấy từ báo cáo tài chính Q3/2026 và dữ liệu tổng hợp ngày %s. Với %s, anh chị đặt trọng số nhiều hơn vào kết quả quý gần nhất, hay vào chuỗi tám quý và rủi ro phía trước?" % (NGAY_DL, s)
    sc.append(S_('end', None, (h1, 'ĐỦ KẾT LUẬN?'), say)); sc[-1].pop('ch')
    chuong = [c['ch'] for c in sc if c.get('ch')]
    M = dict(kenh="@chungkhoanhuynguyen", seri="Đọc BCTC", ngay=ngay, gio_goi_y=gio, gio=gio, tieu_de=title, title=title,
             mo_ta=mo_ta(title, "Số liệu từ báo cáo tài chính và dữ liệu tổng hợp đến ngày %s; bài học là cách đọc dùng được nhiều năm." % NGAY_DL, "Đọc BCTC", link),
             tags=[s, ten, "đọc báo cáo tài chính", "BCTC quý 3 2026", "quản trị rủi ro", "cổ phiếu ngân hàng" if bank else "phân tích doanh nghiệp"],
             bia_hook=[h1, h2], badge="ĐỌC BCTC %s" % s,
             fb_post=fb("%s – %s" % (h1, h2), [x['info'][0], x['info'][1], third] + rl[:1], "Theo anh chị, kết quả này đã phản ánh vào giá %s chưa?" % s, link, "📊"),
             chuong=chuong, seri_web="Đọc BCTC", link_web=link)
    return sc, M

# ================= HI – định giá rẻ hay đắt =================
def hi(key, s, ngay, PX):
    I = info(s); x = I['x']; f = I['f']; c = I['c']; wk = weekly(s); PX[s + 'W'] = wk; ten = I['ten']
    q = x['info'][0]; m = re.search(r"\(([+−][\d,]+)%", q); g = m.group(1) if m else None
    title = "%s: P/E %s, P/B %s, ROE %s%% – %s: rẻ hay đắt?" % (s, vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), ("lãi quý 3 %s%%" % g) if g else "quý 3 lỗ")
    link = "https://chungkhoanhuynguyen.com/hoc/%s.html" % slug(title); h1 = "%s P/E %s" % (s, vn(f['pe'], 1)); h2 = "ROE %s%%" % vn(f['roe'], 1)
    sc = []; eps = f['eps']; bv = f['bvps']
    say = ("%s, mã %s, đang giao dịch quanh %s nghìn đồng, P/E khoảng %s lần, P/B khoảng %s lần, ROE khoảng %s%%. %s Rẻ thật, đắt thật, hay thị trường đang nhìn thấy điều gì khác? "
           "Video này em đặt ba con số định giá cạnh chuỗi lợi nhuận tám quý, cạnh mặt bằng của ngành và cạnh rủi ro, để anh chị tự trả lời. Số liệu từ báo cáo Q3/2026 và dữ liệu tổng hợp ngày %s.") % (
        ten, s, gia(c), vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), noi(q), NGAY_DL)
    sc.append(S_('hook', 'Mở đầu', (h1, h2), say, moc=True, label="%s – định giá nhanh" % s, anh=ANH.get(s, 'factory'), chart=hook_chart(s, wk)))
    say = ("Chương một, ba con số định giá nghĩa là gì với %s. P/E %s lần nghĩa là với lợi nhuận mỗi cổ phiếu bốn quý gần nhất khoảng %s đồng, người mua đang trả khoảng %s đồng giá cho mỗi đồng lợi nhuận. "
           "Nói cách khác, nếu lợi nhuận đứng yên, phải khoảng %s năm lợi nhuận mới bằng giá mua. P/B %s lần nghĩa là giá đang gấp %s lần giá trị sổ sách mỗi cổ phiếu, khoảng %s đồng. "
           "ROE %s%% cho biết mỗi một trăm đồng vốn chủ sở hữu tạo ra khoảng %s đồng lợi nhuận một năm. Ba con số này liên kết với nhau: P/E nhân ROE xấp xỉ bằng P/B.") % (
        s, vn(f['pe'], 2), vn(eps, 0), vn(f['pe'], 2), vn(f['pe'], 0), vn(f['pb'], 2), vn(f['pb'], 2), vn(bv, 0), vn(f['roe'], 1), vn(f['roe'], 1))
    sc.append(S_('cards', 'Chương 1 – Ba con số định giá', ('BA CON SỐ', 'ĐỊNH GIÁ'), say, moc=True, anh='calculator',
                 cards=[('P/E', vn(f['pe'], 2), 'lần'), ('P/B', vn(f['pb'], 2), 'lần'), ('ROE', vn(f['roe'], 1) + '%', 'năm')]))
    say = "Chương hai, lợi nhuận tám quý, gốc của chữ E trong P/E. " + chuoi(I['h'], 1, "lợi nhuận sau thuế công ty mẹ") + noi(x['info'][1]) + \
          " Nếu lợi nhuận bốn quý gần nhất có một quý đột biến tăng hoặc một quý lỗ, P/E hiện tại sẽ không phản ánh đúng sức kiếm tiền bình thường. Khi đó, cách an toàn hơn là tính P/E trên lợi nhuận trung bình nhiều quý."
    sc.append(S_('bars', 'Chương 2 – Lợi nhuận tám quý', ('LỢI NHUẬN', 'TÁM QUÝ'), say, anh='financial chart', bars=bars(I['h'], 1)))
    say = "Chương ba, so với ngành. "
    if I['mpe']:
        say += ("%s thuộc nhóm %s. Trong %d mã cùng nhóm có vốn hóa từ 1.500 tỷ, P/E trung vị khoảng %s lần, P/B trung vị khoảng %s lần, ROE trung vị khoảng %s%%. "
                "%s có P/E %s mặt bằng nhóm và ROE %s mặt bằng nhóm. ") % (s, I['sec'].lower(), I['npeer'], vn(I['mpe'], 2), vn(I['mpb'], 2), vn(I['mroe'], 1), s,
                "cao hơn" if f['pe'] > I['mpe'] else "thấp hơn", "cao hơn" if f['roe'] > I['mroe'] else "thấp hơn")
    say += "So với ngành giúp tránh một sai lầm phổ biến: thấy P/E thấp hơn mã khác ngành rồi kết luận là rẻ. Mỗi ngành có chu kỳ, rủi ro và tốc độ tăng trưởng khác nhau, nên mặt bằng định giá cũng khác nhau. " + WEB[0]
    sc.append(S_('cards', 'Chương 3 – So với ngành', ('SO VỚI', 'CÙNG NGÀNH'), say, moc=True, anh='comparison chart',
                 cards=[('P/E %s' % s, vn(f['pe'], 2), 'trung vị %s' % vn(I['mpe'] or 0, 2)), ('P/B %s' % s, vn(f['pb'], 2), 'trung vị %s' % vn(I['mpb'] or 0, 2)), ('ROE %s' % s, vn(f['roe'], 1) + '%', 'trung vị %s%%' % vn(I['mroe'] or 0, 1))]))
    g4 = [l for l in x['good']][:2]; b4 = x['bad'][:3]
    say = "Chương bốn, điểm tốt và điểm cần soi. " + ("Điểm tốt: " + " ".join(noi(l) for l in g4) + " " if g4 else "Quý này báo cáo không có điểm tốt nổi bật. ") + \
          ("Điểm cần soi: " + " ".join(noi(l) for l in b4) if b4 else "Báo cáo không có dòng xấu rõ rệt.") + \
          " Một định giá chỉ có ý nghĩa khi đặt cạnh câu hỏi: lợi nhuận năm tới cao hơn hay thấp hơn năm nay? Nếu lợi nhuận đi xuống, P/E thấp hôm nay sẽ thành P/E cao vào năm sau."
    sc.append(S_('checklist', 'Chương 4 – Điểm tốt và điểm cần soi', ('ĐIỂM TỐT', 'ĐIỂM CẦN SOI'), say, anh='magnifying glass',
                 items=[(l.split(', ')[0][:40], GREEN) for l in g4] + [(l.split(', ')[0][:40], RED) for l in b4]))
    sc.append(S_('bignum', 'Chương 5 – Giá và đỉnh 52 tuần', ('CÁCH ĐỈNH', '52 TUẦN'),
                 ("Chương năm, giá trong 52 tuần. Đỉnh khoảng %s nghìn đồng, đáy khoảng %s nghìn đồng, giá hiện tại thấp hơn đỉnh khoảng %s%%. Người mua ở đỉnh cần lãi khoảng %s%% mới hòa vốn. "
                  "Giá giảm có thể làm định giá rẻ đi, nhưng cũng có thể là thị trường đang đi trước một quý lợi nhuận xấu. Vì vậy, khi thấy một mã rẻ đi nhanh, anh chị hãy tìm lý do trước khi tìm điểm mua.") % (
                     vn(f['h52'], 2), vn(f['l52'], 2), vn(I['dd'], 1), vn(I['can'], 0)), value=-round(I['dd'], 1), fmt='{:,.1f}', unit='%', top='ĐỈNH 52 TUẦN %s' % vn(f['h52'], 2), sub='giá %s' % gia(c), col=RED))
    say = ("Chương sáu, rủi ro cần theo dõi và cách giữ vị thế. Beta của %s khoảng %s. Tỷ lệ sở hữu nước ngoài khoảng %s%%. Hai con số này cho biết cổ phiếu rung lắc thế nào và nhạy ra sao với dòng vốn ngoại. "
           "Em gợi ý ba nguyên tắc: không để một mã vượt 20%% danh mục; viết sẵn điều kiện khiến luận điểm sai trước khi mua; và với mã có lợi nhuận dao động mạnh, chia mua làm nhiều lần thay vì mua một lần. %s") % (
        s, vn(f['beta'], 2), vn(f['fo'], 1), WEB[1])
    sc.append(S_('checklist', 'Chương 6 – Rủi ro và vị thế', ('RỦI RO', 'VÀ VỊ THẾ'), say, moc=True, anh='warning sign',
                 items=[('Tối đa 20% một mã', GOLD), ('Viết điểm sai trước khi mua', GOLD), ('Chia mua nhiều lần', GOLD)]))
    say = "Chương bảy, tóm lại. Rẻ hay đắt không nằm ở một con số. P/E và P/B chỉ là giá, còn ROE, chuỗi lợi nhuận và rủi ro mới là thứ anh chị đang mua. Bảng tóm tắt gồm: P/E %s lần, P/B %s lần, ROE %s%%, giá thấp hơn đỉnh 52 tuần khoảng %s%%. %s" % (
        vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), vn(I['dd'], 1), WEB[2])
    sc.append(S_('cards', 'Chương 7 – Tóm lại', ('RẺ HAY ĐẮT', 'TÓM LẠI'), say, anh='notebook summary',
                 cards=[('P/E', vn(f['pe'], 2), 'lần'), ('ROE', vn(f['roe'], 1) + '%', ''), ('Cách đỉnh', '−' + vn(I['dd'], 1) + '%', '52 tuần')]))
    say = ("Chương tám, bốn sai lầm hay gặp khi đọc định giá. Một, so P/E giữa hai ngành khác nhau, ví dụ so một hãng hàng không với một ngân hàng. Hai, dùng P/E của một năm lợi nhuận đột biến để kết luận là rẻ. "
           "Ba, nhìn P/B thấp mà quên hỏi tài sản trên sổ sách có thu hồi được giá trị đó không. Bốn, quên rằng ROE rất cao có thể đến từ vốn chủ sở hữu mỏng sau nhiều năm lỗ, hoặc từ nợ vay lớn. "
           "Với %s, ROE khoảng %s%% cần được đặt cạnh câu hỏi: vốn chủ sở hữu hiện tại có đang thấp bất thường không? Câu trả lời nằm ở bảng cân đối kế toán, mục vốn chủ sở hữu, qua nhiều quý.") % (s, vn(f['roe'], 1))
    sc.insert(-1, S_('checklist', 'Chương 8 – Bốn sai lầm khi đọc định giá', ('BỐN SAI LẦM', 'KHI ĐỌC ĐỊNH GIÁ'), say, anh='mistake warning',
                 items=[('So P/E khác ngành', RED), ('P/E năm đột biến', RED), ('P/B thấp, tài sản ảo', RED), ('ROE cao vì vốn mỏng', RED)]))
    sc.append(S_('end', None, (h1, 'RẺ HAY ĐẮT?'), "Số liệu từ báo cáo tài chính Q3/2026 và dữ liệu tổng hợp ngày %s. Anh chị xếp %s vào nhóm rẻ, hợp lý hay đắt, và vì sao?" % (NGAY_DL, s))); sc[-1].pop('ch')
    M = dict(kenh="Huy Invest (@chungkhoanhuynguyen3)", seri="Huy Invest – Đầu tư thông minh", ngay=ngay, gio_goi_y="19:00", gio="19:00", tieu_de=title, title=title,
             mo_ta=mo_ta(title, "Số liệu từ báo cáo tài chính và dữ liệu tổng hợp đến ngày %s; bài học là cách đọc dùng được nhiều năm." % NGAY_DL, "Huy Invest – Đầu tư thông minh", link),
             tags=["định giá cổ phiếu", s, ten, "P/E", "P/B", "Huy Invest"], bia_hook=[h1, h2], badge="RẺ HAY ĐẮT",
             fb_post=fb("%s – %s" % (h1, h2), [x['info'][0], "P/E %s, P/B %s, ROE %s%%" % (vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1))] + ["Rủi ro: " + x['bad'][0]] * bool(x['bad']), "Anh chị xếp %s vào nhóm rẻ, hợp lý hay đắt?" % s, link),
             chuong=[c['ch'] for c in sc if c.get('ch')], seri_web="Huy Invest – Đầu tư thông minh", link_web=link)
    return sc, M

# ================= Y2 – soi BCTC sâu (bảng cân đối) =================
def y2(key, s, ngay, PX, goc):
    I = info(s); x = I['x']; f = I['f']; c = I['c']; wk = weekly(s); PX[s + 'W'] = wk; ten = I['ten']
    title = "Soi BCTC %s quý 3/2026: %s" % (ten, goc); link = "https://chungkhoanhuynguyen.com/hoc/%s.html" % slug(title)
    tt = lambda n: bq(s, 'bs', n) or [0] * 8
    ts, vay_n, vay_d, vcsh, htk, pt = tt('TỔNG CỘNG TÀI SẢN'), tt('Vay và nợ ngắn hạn'), tt('Vay và nợ dài hạn'), tt('Vốn chủ sở hữu'), tt('Hàng tồn kho'), tt('Các khoản phải thu ngắn hạn')
    tien = tt('Tiền và các khoản tương đương tiền'); vay = [a + b for a, b in zip(vay_n, vay_d)]
    lv = bq(s, 'is', 'Trong đó: Chi phí lãi vay') or [0] * 8; cfo = bq(s, 'cf', 'Lưu chuyển tiền thuần từ hoạt động kinh doanh') or [0] * 8
    gp = bq(s, 'is', 'Lợi nhuận gộp') or [0] * 8; dt = bq(s, 'is', 'Doanh thu thuần') or [1] * 8
    bien = [g / d * 100 if d else 0 for g, d in zip(gp, dt)]
    h1, h2 = goc.split('|')[0].strip().upper()[:18], goc.split('|')[1].strip().upper()[:18] if '|' in goc else ''
    title = title.replace('|', '–'); link = "https://chungkhoanhuynguyen.com/hoc/%s.html" % slug(title)
    sc = []
    say = ("%s, mã %s. %s %s Quý này nhìn từ báo cáo kết quả kinh doanh thì đã rõ, nhưng báo cáo tài chính có ba phần, và phần ít người đọc nhất là bảng cân đối kế toán và lưu chuyển tiền tệ. "
           "Video này em soi cả ba phần: lợi nhuận đến từ đâu, tiền có về thật không, và doanh nghiệp đang dùng bao nhiêu nợ. Số liệu từ báo cáo Q3/2026 và dữ liệu tổng hợp ngày %s.") % (ten, s, noi(x['info'][0]), noi(x['info'][1]), NGAY_DL)
    sc.append(S_('hook', 'Mở đầu', (h1, h2), say, moc=True, label="%s – soi BCTC" % s, anh=ANH.get(s, 'factory'), chart=hook_chart(s, wk)))
    say = "Chương một, lợi nhuận tám quý. " + chuoi(I['h'], 1, "lợi nhuận sau thuế công ty mẹ") + "Chuỗi tám quý giúp tách phần lợi nhuận đều đặn khỏi những quý đột biến."
    sc.append(S_('bars', 'Chương 1 – Lợi nhuận tám quý', ('LỢI NHUẬN', 'TÁM QUÝ'), say, anh='financial chart', bars=bars(I['h'], 1)))
    say = ("Chương hai, biên lợi nhuận gộp. Theo báo cáo, biên gộp Q3/2026 khoảng %s%%, quý trước khoảng %s%%, cùng kỳ năm trước khoảng %s%%. Bình quân tám quý khoảng %s%%. %s "
           "Biên gộp là tấm đệm đầu tiên của lợi nhuận. Khi biên co lại, doanh nghiệp phải bán nhiều hơn chỉ để giữ nguyên lợi nhuận, và mọi chi phí cố định như lãi vay, khấu hao, lương sẽ chiếm phần lớn hơn.") % (
        vn(bien[0], 1), vn(bien[1], 1), vn(bien[4], 1), vn(sum(bien) / 8, 1), noi(x['info'][2]) if len(x['info']) > 2 else "")
    bb = [(q, b, (GREEN if j == 7 else BLUE), vn(b, 1)) for j, (q, b) in enumerate(zip([a[0] for a in I['h']], bien[::-1]))]
    sc.append(S_('bars', 'Chương 2 – Biên lợi nhuận gộp', ('BIÊN LỢI NHUẬN', 'GỘP'), say, moc=True, anh='profit margin', bars=bb))
    say = ("Chương ba, nợ vay. Cuối Q3/2026, tổng vay ngắn hạn và dài hạn khoảng %s tỷ, vốn chủ sở hữu khoảng %s tỷ, tức nợ vay bằng khoảng %s lần vốn chủ. Một năm trước, tỷ lệ này khoảng %s lần. "
           "Chi phí lãi vay quý này khoảng %s tỷ, cùng kỳ khoảng %s tỷ. Tiền và tương đương tiền cuối kỳ khoảng %s tỷ. "
           "Nợ vay không xấu nếu tiền vay tạo ra lợi nhuận cao hơn lãi phải trả. Nhưng nợ làm lợi nhuận nhạy hơn: khi kinh doanh tốt, lãi tăng nhanh; khi kinh doanh xấu, lãi vay vẫn phải trả đủ.") % (
        vn(vay[0], 0), vn(vcsh[0], 0), vn(vay[0] / vcsh[0], 2) if vcsh[0] else '0', vn(vay[4] / vcsh[4], 2) if vcsh[4] else '0', vn(lv[0], 0), vn(lv[4], 0), vn(tien[0], 0))
    sc.append(S_('cards', 'Chương 3 – Nợ vay', ('NỢ VAY', 'VÀ LÃI VAY'), say, anh='bank loan',
                 cards=[('Nợ vay', '≈ %s tỷ' % vn(vay[0], 0), ''), ('Nợ vay / vốn chủ', '%s lần' % (vn(vay[0] / vcsh[0], 2) if vcsh[0] else '0'), ''), ('Lãi vay quý', '≈ %s tỷ' % vn(lv[0], 0), '')]))
    cf4 = sum(cfo[:4]); ln4 = sum(a[1] for a in I['h'][-4:])
    say = ("Chương bốn, tiền có về thật không. Bốn quý gần nhất, lợi nhuận sau thuế cộng lại khoảng %s tỷ, dòng tiền thuần từ hoạt động kinh doanh cộng lại khoảng %s tỷ. Từng quý gần nhất lần lượt là %s. "
           "Hàng tồn kho cuối kỳ khoảng %s tỷ, khoản phải thu ngắn hạn khoảng %s tỷ, so với một năm trước lần lượt khoảng %s tỷ và %s tỷ. "
           "Nếu phải thu và tồn kho tăng nhanh hơn doanh thu, lợi nhuận đang được ghi nhận trước khi tiền về. Điều đó chưa phải là sai, nhưng anh chị cần theo dõi xem các quý sau tiền có về theo không.") % (
        vn(ln4, 0), ("âm " if cf4 < 0 else "") + vn(abs(cf4), 0), ", ".join("%s %s %s tỷ" % (q, "âm" if v < 0 else "đạt", vn(abs(v), 0)) for q, v in zip([a[0] for a in I['h'][-4:]], cfo[:4][::-1])),
        vn(htk[0], 0), vn(pt[0], 0), vn(htk[4], 0), vn(pt[4], 0))
    sc.append(S_('bars', 'Chương 4 – Dòng tiền kinh doanh', ('DÒNG TIỀN', 'KINH DOANH'), say, moc=True, anh='cash flow',
                 bars=[(q, v, (GREEN if v >= 0 else RED), vn(v, 0)) for q, v in zip([a[0] for a in I['h']], cfo[::-1])]))
    b4 = x['bad'][:3]; g4 = x['good'][:2]
    say = "Chương năm, điểm tốt và rủi ro cần theo dõi. " + (" ".join(noi(l) for l in g4) + " " if g4 else "") + (" ".join(noi(l) for l in b4) if b4 else "") + \
          " Ngoài các dòng trên, rủi ro ngành cũng cần đặt cạnh: giá đầu vào, nhu cầu của khách hàng và lãi suất. Một doanh nghiệp tốt vẫn có thể có hai, ba quý xấu khi ngành đi xuống."
    sc.append(S_('checklist', 'Chương 5 – Rủi ro cần theo dõi', ('RỦI RO', 'CẦN THEO DÕI'), say, anh='warning sign',
                 items=[(l.split(', ')[0][:40], GREEN) for l in g4] + [(l.split(', ')[0][:40], RED) for l in b4]))
    say = ("Chương sáu, định giá và vị thế. Giá khoảng %s nghìn đồng, P/E khoảng %s lần, P/B khoảng %s lần, ROE khoảng %s%%, thấp hơn đỉnh 52 tuần khoảng %s%%. "
           "Khi đã soi đủ ba phần báo cáo, anh chị hãy quyết định tỷ trọng trước khi quyết định mua: doanh nghiệp càng nhiều nợ hoặc dòng tiền càng thất thường thì tỷ trọng tối đa nên càng thấp. %s") % (
        gia(c), vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), vn(I['dd'], 1), WEB[0])
    sc.append(S_('cards', 'Chương 6 – Định giá và vị thế', ('ĐỊNH GIÁ', 'VÀ VỊ THẾ'), say, anh='calculator',
                 cards=[('P/E', vn(f['pe'], 2), 'lần'), ('P/B', vn(f['pb'], 2), 'lần'), ('Cách đỉnh', '−' + vn(I['dd'], 1) + '%', '52 tuần')]))
    say = "Chương bảy, bốn câu hỏi khi soi bất kỳ báo cáo nào. Một, lợi nhuận đến từ hoạt động chính hay từ khoản bất thường? Hai, biên gộp đang mở rộng hay co lại? Ba, dòng tiền kinh doanh có theo kịp lợi nhuận không? Bốn, nợ vay so với vốn chủ đang tăng hay giảm? %s" % WEB[2]
    sc.append(S_('checklist', 'Chương 7 – Bốn câu hỏi', ('BỐN CÂU HỎI', 'KHI SOI BCTC'), say, anh='checklist notebook',
                 items=[('Lợi nhuận từ đâu?', GOLD), ('Biên gộp mở hay co?', GOLD), ('Tiền có về không?', GOLD), ('Nợ tăng hay giảm?', GOLD)]))
    say = ("Chương tám, đọc thuyết minh ở đâu. Bốn con số trong video đều có trong báo cáo tài chính quý, nhưng lời giải thích nằm ở thuyết minh. Khoản vay: mục vay và nợ thuê tài chính, ghi rõ ngân hàng cho vay, lãi suất và kỳ hạn. "
           "Hàng tồn kho: mục hàng tồn kho, cho biết nguyên liệu, thành phẩm và dự phòng giảm giá. Phải thu: mục phải thu khách hàng, có bảng tuổi nợ và dự phòng phải thu khó đòi. Doanh thu và giá vốn: mục doanh thu theo mảng, cho biết mảng nào đang kéo lợi nhuận. "
           "Đọc thuyết minh mất thêm mười phút, nhưng giúp anh chị phân biệt một quý xấu tạm thời với một xu hướng xấu kéo dài.")
    sc.insert(-1, S_('checklist', 'Chương 8 – Đọc thuyết minh ở đâu', ('ĐỌC THUYẾT MINH', 'Ở ĐÂU'), say, anh='document reading',
                 items=[('Vay và nợ thuê tài chính', GOLD), ('Hàng tồn kho', GOLD), ('Phải thu, tuổi nợ', GOLD), ('Doanh thu theo mảng', GOLD)]))
    sc.append(S_('end', None, (h1, h2 or 'SOI KỸ CHƯA?'), "Số liệu từ báo cáo tài chính Q3/2026 và dữ liệu tổng hợp ngày %s. Trong bốn câu hỏi vừa rồi, câu nào anh chị thấy %s đang trả lời yếu nhất?" % (NGAY_DL, s))); sc[-1].pop('ch')
    M = dict(kenh="Y2 Soi Báo Cáo Tài Chính (@chungkhoanhuynguyen8)", seri="Soi báo cáo tài chính", ngay=ngay, gio_goi_y="19:00", gio="19:00", tieu_de=title, title=title,
             mo_ta=mo_ta(title, "Số liệu từ báo cáo tài chính và dữ liệu tổng hợp đến ngày %s; bài học là cách đọc dùng được nhiều năm." % NGAY_DL, "Soi báo cáo tài chính", link),
             tags=["soi báo cáo tài chính", s, ten, "BCTC quý 3 2026", "dòng tiền", "nợ vay"], bia_hook=[h1, h2], badge="SOI BCTC %s" % s,
             fb_post=fb("%s – %s" % (h1, h2), [x['info'][0], "Nợ vay ≈ %s tỷ, lãi vay quý ≈ %s tỷ" % (vn(vay[0], 0), vn(lv[0], 0)), "Dòng tiền KD 4 quý ≈ %s tỷ so với LNST ≈ %s tỷ" % (vn(cf4, 0), vn(ln4, 0))],
                        "Theo anh chị, phần nào trong báo cáo %s đáng lo nhất?" % s, link, "🔎"),
             chuong=[c['ch'] for c in sc if c.get('ch')], seri_web="Soi báo cáo tài chính", link_web=link)
    return sc, M

# ================= TS – góp đều =================
def dca(s, thang=3_000_000, nam=3):
    D = daily(s); last = D[-1]; import datetime as dt
    start = (dt.date.fromisoformat(last[0]) - dt.timedelta(days=365 * nam)).isoformat()
    mon = {}
    for r in D:
        if r[0] >= start and r[0][:7] not in mon: mon[r[0][:7]] = r
    rows = sorted(mon.values()); cp = 0; von = 0; path = []
    for r in rows:
        p = r[4] * 10; cp += thang / p; von += thang; path.append((r[0], von, cp * p))
    val = cp * last[4] * 10; avg = von / cp / 1000
    lump = von / (rows[0][4] * 10) * last[4] * 10
    am = sum(1 for a in path if a[2] < a[1]); worst = min(path, key=lambda a: a[2] / a[1] - 1)
    best = max(path, key=lambda a: a[2] / a[1] - 1)
    mean = sum(r[4] for r in rows) / len(rows) / 100
    return dict(mean=mean, n=len(rows), von=von, val=val, avg=avg, last=last[4] / 100, first=rows[0][4] / 100, d0=rows[0][0], d1=last[0], lump=lump, am=am,
                worst=(worst[0], (worst[2] / worst[1] - 1) * 100), best=(best[0], (best[2] / best[1] - 1) * 100), path=path)
def ngay_vn(d): return "%d/%d/%s" % (int(d[8:]), int(d[5:7]), d[:4])
def ts(key, s, ngay, PX, goc):
    I = info(s); x = I['x']; f = I['f']; wk = weekly(s); PX[s + 'W'] = wk; ten = I['ten']; R = dca(s)
    tr = lambda v: vn(v / 1e6, 1)
    title = "%s góp đều %d tháng: vốn %s triệu thành %s triệu – %s" % (ten, R['n'], vn(R['von'] / 1e6, 0), tr(R['val']), goc)
    link = "https://chungkhoanhuynguyen.com/hoc/%s.html" % slug(title); lai = (R['val'] / R['von'] - 1) * 100; lump = (R['lump'] / R['von'] - 1) * 100
    h1 = "GÓP ĐỀU %s" % s; h2 = ("LÃI %s%%" if lai >= 0 else "LỖ %s%%") % vn(abs(lai), 1)
    sc = []
    say = ("Nếu mỗi tháng anh chị góp đều 3 triệu đồng vào cổ phiếu %s của %s, bắt đầu từ ngày %s, thì sau %d tháng, tổng vốn %s triệu đồng hôm nay có giá trị khoảng %s triệu đồng, %s khoảng %s%%. "
           "Còn nếu bỏ hết %s triệu một lần ngay tháng đầu, kết quả là khoảng %s triệu, %s khoảng %s%%. Video này em đi từng bước: giá vốn bình quân, những tháng âm, lợi nhuận doanh nghiệp và cách giữ kỷ luật. "
           "Phép tính dùng giá đóng cửa phiên đầu mỗi tháng, chưa tính cổ tức tiền mặt, phí và thuế.") % (
        s, ten, ngay_vn(R['d0']), R['n'], vn(R['von'] / 1e6, 0), tr(R['val']), "lãi" if lai >= 0 else "lỗ", vn(abs(lai), 1), vn(R['von'] / 1e6, 0), tr(R['lump']), "lãi" if lump >= 0 else "lỗ", vn(abs(lump), 1))
    sc.append(S_('hook', 'Mở đầu', (h1, h2), say, moc=True, label="%s – tích sản" % s, anh=ANH.get(s, 'piggy bank savings'), chart=hook_chart(s, wk)))
    say = ("Chương một, hai cách, hai kết quả. Giá %s tháng đầu khoảng %s nghìn đồng, giá ngày %s khoảng %s nghìn đồng. Góp đều cho kết quả %s triệu, mua một lần cho kết quả %s triệu. "
           "%s Điều quan trọng không phải cách nào thắng trong quá khứ, mà là cách nào anh chị làm được đều đặn mà không bỏ cuộc giữa chừng.") % (
        s, vn(R['first'], 2), ngay_vn(R['d1']), vn(R['last'], 2), tr(R['val']), tr(R['lump']),
        "Mua một lần thắng khi giá đi lên đều từ đầu kỳ; góp đều thắng khi giá đi xuống rồi mới hồi." if R['lump'] > R['val'] else "Góp đều thắng ở đây vì giá có giai đoạn đi xuống, giúp mua được nhiều cổ phiếu hơn ở vùng giá thấp.")
    say += " Với người đi làm, góp đều còn có một lợi thế không nằm trong bảng tính: nó khớp với dòng tiền lương hằng tháng, nên không cần có sẵn một khoản lớn và không cần đoán thời điểm."
    sc.append(S_('cards', 'Chương 1 – Hai cách, hai kết quả', ('HAI CÁCH', 'HAI KẾT QUẢ'), say, moc=True, anh='coins jar',
                 cards=[('Tổng vốn', '%s triệu' % vn(R['von'] / 1e6, 0), '%d tháng' % R['n']), ('Góp đều', '%s triệu' % tr(R['val']), pct(lai)), ('Mua một lần', '%s triệu' % tr(R['lump']), pct(lump))]))
    say = ("Chương hai, giá vốn bình quân. Góp đều %d tháng cho giá vốn bình quân khoảng %s nghìn đồng một cổ phiếu, so với giá hiện tại khoảng %s nghìn đồng. "
           "Góp cùng một số tiền mỗi tháng thì tháng giá thấp mua được nhiều cổ phiếu hơn, tháng giá cao mua được ít hơn, nên giá vốn bình quân thường thấp hơn giá trung bình các tháng. "
           "Trong ví dụ này, trung bình cộng giá của %d lần mua khoảng %s nghìn đồng, còn giá vốn bình quân thực tế khoảng %s nghìn đồng. "
           "Nhưng giá vốn thấp không tự biến thành lãi: nếu giá cuối kỳ vẫn dưới giá vốn bình quân, danh mục vẫn âm.") % (R['n'], vn(R['avg'], 2), vn(R['last'], 2), R['n'], vn(R['mean'], 2), vn(R['avg'], 2))
    pts = R['path'][::max(1, len(R['path']) // 8)][-8:]
    sc.append(S_('bars', 'Chương 2 – Giá trị danh mục theo thời gian', ('GIÁ TRỊ', 'DANH MỤC'), say, anh='growth chart',
                 bars=[("%s/%s" % (a[0][5:7], a[0][2:4]), round(a[2] / 1e6, 1), (GREEN if a[2] >= a[1] else RED), vn(a[2] / 1e6, 0)) for a in pts]))
    say = ("Chương ba, những tháng âm. Trong %d lần góp, có %d tháng giá trị danh mục thấp hơn số vốn đã bỏ vào. Thời điểm xấu nhất là tháng %s, danh mục %s khoảng %s%% so với vốn. Thời điểm tốt nhất là tháng %s, %s khoảng %s%%. "
           "Đây là phần mà bảng tính thường bỏ qua: người góp đều phải chịu được những tháng âm liên tiếp mà vẫn tiếp tục góp. Nếu dừng ở đúng tháng xấu nhất, kết quả sẽ khác hẳn con số cuối kỳ.") % (
        R['n'], R['am'], ngay_vn(R['worst'][0])[2:] if False else R['worst'][0][5:7] + "/" + R['worst'][0][:4], "âm" if R['worst'][1] < 0 else "dương", vn(abs(R['worst'][1]), 1),
        R['best'][0][5:7] + "/" + R['best'][0][:4], "lãi" if R['best'][1] >= 0 else "lỗ", vn(abs(R['best'][1]), 1))
    say = say.replace("tháng %s/%s" % (R['worst'][0][5:7], R['worst'][0][:4]), "tháng %d năm %s" % (int(R['worst'][0][5:7]), R['worst'][0][:4])).replace("tháng %s/%s" % (R['best'][0][5:7], R['best'][0][:4]), "tháng %d năm %s" % (int(R['best'][0][5:7]), R['best'][0][:4]))
    sc.append(S_('bignum', 'Chương 3 – Những tháng âm', ('NHỮNG THÁNG', 'DANH MỤC ÂM'), say, moc=True, value=R['am'], fmt='{:,.0f}', unit=' tháng', top='TRÊN %d LẦN GÓP' % R['n'], sub='xấu nhất %s%%' % vn(R['worst'][1], 1), col=RED if R['am'] else GREEN))
    say = "Chương bốn, doanh nghiệp phía sau cổ phiếu. " + chuoi(I['h'], 1, "lợi nhuận sau thuế công ty mẹ") + noi(x['info'][1]) + \
          " Tích sản bằng cổ phiếu là góp vốn vào một doanh nghiệp, nên lợi nhuận doanh nghiệp tăng đều qua nhiều năm mới là động cơ thật của giá cổ phiếu. Góp đều chỉ giúp làm mượt giá mua."
    sc.append(S_('bars', 'Chương 4 – Lợi nhuận doanh nghiệp', ('LỢI NHUẬN', 'TÁM QUÝ'), say, anh='financial chart', bars=bars(I['h'], 1)))
    say = ("Chương năm, định giá hôm nay. %s có P/E khoảng %s lần, P/B khoảng %s lần, ROE khoảng %s%%, beta khoảng %s. "
           "Người tích sản không cần mua ở giá thấp nhất, nhưng nên tránh góp mạnh tay khi định giá đã cao hơn hẳn mặt bằng lịch sử. Một cách đơn giản là giữ số tiền góp cố định, không tăng tiền góp khi giá tăng nóng. %s") % (
        s, vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), vn(f['beta'], 2), WEB[0])
    sc.append(S_('cards', 'Chương 5 – Định giá hôm nay', ('ĐỊNH GIÁ', 'HÔM NAY'), say, anh='calculator', cards=[('P/E', vn(f['pe'], 2), 'lần'), ('ROE', vn(f['roe'], 1) + '%', ''), ('Beta', vn(f['beta'], 2), '')]))
    say = ("Chương sáu, quản trị rủi ro cho người tích sản. Một, không dồn toàn bộ tiền góp vào một mã: nên chia ít nhất ba đến năm mã khác ngành, hoặc kết hợp quỹ chỉ số. "
           "Hai, giữ quỹ dự phòng khoảng sáu tháng chi tiêu bằng tiền gửi trước khi góp, để không phải bán cổ phiếu đúng lúc giá thấp. Ba, mỗi năm xem lại tỷ trọng một lần: mã nào phình quá 30%% danh mục thì giảm bớt về mức đã định. "
           "Bốn, không dùng vay ký quỹ cho danh mục tích sản, vì đòn bẩy biến những tháng âm bình thường thành lệnh bán bắt buộc.")
    sc.append(S_('checklist', 'Chương 6 – Quản trị rủi ro khi tích sản', ('QUẢN TRỊ RỦI RO', 'KHI TÍCH SẢN'), say, moc=True, anh='umbrella rain',
                 items=[('Chia 3–5 mã khác ngành', GREEN), ('Quỹ dự phòng 6 tháng', GREEN), ('Tái cân bằng mỗi năm', GOLD), ('Không vay ký quỹ', RED)]))
    say = "Chương bảy, tóm lại. Góp đều %d tháng vào %s cho kết quả %s khoảng %s%%, mua một lần cho kết quả %s khoảng %s%%. Quá khứ không bảo đảm tương lai, nhưng con số giúp anh chị biết trước mình sẽ phải chịu đựng những gì. %s" % (
        R['n'], s, "lãi" if lai >= 0 else "lỗ", vn(abs(lai), 1), "lãi" if lump >= 0 else "lỗ", vn(abs(lump), 1), WEB[2])
    sc.append(S_('cards', 'Chương 7 – Tóm lại', ('TÍCH SẢN', 'TÓM LẠI'), say, anh='notebook summary', cards=[('Góp đều', pct(lai), ''), ('Một lần', pct(lump), ''), ('Tháng âm', str(R['am']), '/%d' % R['n'])]))
    say = ("Chương tám, góp đều thế nào cho bền. Một, chọn một ngày cố định mỗi tháng, ví dụ ngày nhận lương, và đặt lệnh theo số tiền đã định, không chờ giá đẹp. Hai, ghi nhật ký mỗi lần góp: ngày, giá, số cổ phiếu, giá vốn bình quân mới. "
           "Ba, đặt quy tắc cho những tháng thị trường giảm mạnh từ trước, ví dụ vẫn góp đúng số tiền cũ, không dừng và cũng không vay thêm để mua. Bốn, mỗi quý đọc lại kết quả kinh doanh của doanh nghiệp, vì lý do để tiếp tục góp là doanh nghiệp vẫn tốt, không phải giá vẫn tăng. "
           "Những quy tắc nhỏ này giúp anh chị đi qua %d tháng âm như trong ví dụ của %s mà không phải quyết định lại từ đầu mỗi lần thị trường biến động.") % (R['am'], s)
    sc.insert(-1, S_('checklist', 'Chương 8 – Góp đều cho bền', ('GÓP ĐỀU', 'CHO BỀN'), say, anh='calendar planner',
                 items=[('Ngày cố định mỗi tháng', GREEN), ('Nhật ký giá vốn', GREEN), ('Quy tắc tháng giảm mạnh', GOLD), ('Đọc KQKD mỗi quý', GOLD)]))
    sc.append(S_('end', None, (h1, h2), "Số liệu dùng giá đóng cửa đến ngày %s và báo cáo tài chính Q3/2026. Nếu bắt đầu góp đều từ hôm nay, anh chị chọn một mã, hay chia đều cho nhiều mã?" % ngay_vn(R['d1']))); sc[-1].pop('ch')
    M = dict(kenh="Đầu Tư Tích Sản (@chungkhoanhuynguyen6)", seri="Đầu tư tích sản", ngay=ngay, gio_goi_y="19:00", gio="19:00", tieu_de=title, title=title,
             mo_ta=mo_ta(title, "Tính bằng giá đóng cửa phiên đầu mỗi tháng từ %s đến %s, chưa gồm cổ tức tiền mặt, phí, thuế; số liệu tài chính đến ngày %s." % (ngay_vn(R['d0']), ngay_vn(R['d1']), NGAY_DL), "Đầu tư tích sản", link),
             tags=["tích sản", "đầu tư định kỳ", s, ten, "góp đều", "quản trị rủi ro"], bia_hook=[h1, h2], badge="TÍCH SẢN",
             fb_post=fb("%s %d THÁNG – %s" % (h1, R['n'], h2), ["Góp 3 triệu/tháng: vốn %s triệu → %s triệu" % (vn(R['von'] / 1e6, 0), tr(R['val'])), "Mua một lần: %s triệu (%s)" % (tr(R['lump']), pct(lump)), "%d/%d tháng danh mục âm, xấu nhất %s" % (R['am'], R['n'], pct(R['worst'][1]))],
                        "Anh chị chọn góp đều hay mua một lần, và vì sao?" % (), link, "💰"),
             chuong=[c['ch'] for c in sc if c.get('ch')], seri_web="Đầu tư tích sản", link_web=link)
    return sc, M

# ================= K2 – so sánh nhóm =================
def k2(key, syms, ngay, PX, title, h1, h2, nhom, chart_sym, goc_rr):
    link = "https://chungkhoanhuynguyen.com/hoc/%s.html" % slug(title); wk = weekly(chart_sym); PX[chart_sym + 'W'] = wk
    I = {s: info(s) for s in syms}; sc = []
    g = {}
    for s in syms:
        m = re.search(r"\(([+−][\d,]+)%", KQ[s]['info'][0]); g[s] = float(m.group(1).replace('−', '-').replace(',', '.')) if m else None
    say = ("Video này đặt %d mã %s cạnh nhau: %s. Cùng một nhóm, cùng một quý, nhưng kết quả và định giá rất khác nhau. %s "
           "Em đi qua bốn lớp: lợi nhuận quý 3 so với cùng kỳ, lợi nhuận lũy kế chín tháng, định giá, và rủi ro. Số liệu từ báo cáo Q3/2026 và dữ liệu tổng hợp ngày %s.") % (
        len(syms), nhom, ", ".join("%s %s" % (I[s]['ten'], s) for s in syms), goc_rr, NGAY_DL)
    sc.append(S_('hook', 'Mở đầu', (h1, h2), say, moc=True, label="%s – so sánh nhóm" % nhom, anh='oil refinery' if 'dầu' in nhom else 'stock market screen', chart=hook_chart(chart_sym, wk)))
    say = "Chương một, lợi nhuận quý 3 so với cùng kỳ. " + " ".join("%s: %s" % (s, noi(KQ[s]['info'][0]).split('đạt ', 1)[-1]) for s in syms) + \
          " Cùng một bối cảnh thị trường mà lợi nhuận đi các hướng khác nhau, nghĩa là yếu tố riêng của từng doanh nghiệp quan trọng không kém yếu tố ngành."
    sc.append(S_('bars', 'Chương 1 – Lợi nhuận quý 3 so với cùng kỳ', ('LÃI QUÝ 3', 'SO CÙNG KỲ'), say, moc=True, anh='financial chart',
                 bars=[(s, g[s] if g[s] is not None else -100, (GREEN if (g[s] or -1) >= 0 else RED), pct(g[s]) if g[s] is not None else 'lỗ') for s in syms]))
    say = "Chương hai, lũy kế chín tháng, để bớt nhiễu của một quý. " + " ".join("%s: %s" % (s, noi(KQ[s]['info'][1]).split('đạt ', 1)[-1]) for s in syms) + \
          " Khi quý 3 và lũy kế chín tháng đi ngược nhau, anh chị nên tìm xem quý 3 có khoản bất thường hay nền so sánh đặc biệt không."
    sc.append(S_('cards', 'Chương 2 – Lũy kế chín tháng', ('LŨY KẾ', 'CHÍN THÁNG'), say, anh='calendar', cards=[(s, KQ[s]['info'][1].split(': ')[1].split(' (')[0], re.sub(r'.*\((.*)\).*', r'\1', KQ[s]['info'][1])) for s in syms[:4]]))
    say = "Chương ba, định giá cả nhóm. " + " ".join("%s có P/E khoảng %s lần, P/B khoảng %s lần, ROE khoảng %s%%." % (s, vn(I[s]['f']['pe'], 2), vn(I[s]['f']['pb'], 2), vn(I[s]['f']['roe'], 1)) for s in syms) + \
          " P/E thấp nhất nhóm chưa chắc là rẻ nhất, vì lợi nhuận bốn quý gần nhất có thể đang ở đỉnh chu kỳ. Mã có ROE cao thường được thị trường trả P/B cao hơn. " + WEB[0]
    sc.append(S_('cards', 'Chương 3 – Định giá cả nhóm', ('ĐỊNH GIÁ', 'CẢ NHÓM'), say, moc=True, anh='calculator', cards=[(s, 'P/E ' + vn(I[s]['f']['pe'], 1), 'ROE ' + vn(I[s]['f']['roe'], 1) + '%') for s in syms[:4]]))
    say = "Chương bốn, giá cách đỉnh 52 tuần và hệ số beta. " + " ".join("%s thấp hơn đỉnh khoảng %s%%, beta %s." % (s, vn(I[s]['dd'], 1), vn(I[s]['f']['beta'], 2)) for s in syms) + \
          " Mã cách đỉnh càng xa thì người mua ở đỉnh càng cần lãi nhiều mới hòa vốn. Beta dưới một nghĩa là giá thường dao động ít hơn thị trường chung, nhưng không bảo vệ khỏi rủi ro riêng của doanh nghiệp."
    sc.append(S_('bars', 'Chương 4 – Cách đỉnh 52 tuần', ('CÁCH ĐỈNH', '52 TUẦN'), say, anh='mountain peak', bars=[(s, -round(I[s]['dd'], 1), RED, '−' + vn(I[s]['dd'], 1) + '%') for s in syms]))
    rr = [(s, KQ[s]['bad'][0]) for s in syms if KQ[s]['bad']]
    say = "Chương năm, rủi ro cần theo dõi. " + " ".join("Với %s, %s" % (s, noi(b)[0].lower() + noi(b)[1:]) for s, b in rr[:4]) + " " + goc_rr + \
          " Vì các mã cùng nhóm thường biến động cùng chiều khi yếu tố ngành thay đổi, anh chị nên cộng tỷ trọng cả nhóm trong danh mục, và đặt giới hạn cho cả nhóm, không chỉ cho từng mã."
    sc.append(S_('checklist', 'Chương 5 – Rủi ro cần theo dõi', ('RỦI RO', 'CẦN THEO DÕI'), say, moc=True, anh='warning sign', items=[("%s: %s" % (s, b.split(', ')[0][:30]), RED) for s, b in rr[:4]] + [('Giới hạn tỷ trọng cả nhóm', GOLD)]))
    say = "Chương sáu, từng mã một nét chính. " + " ".join("%s: %s" % (s, noi((KQ[s]['good'] or KQ[s]['info'][2:3] or KQ[s]['info'][:1])[0])) for s in syms) + \
          " Những nét chính này chỉ là điểm bắt đầu; mỗi mã cần được đọc riêng chuỗi tám quý và thuyết minh trước khi đưa vào danh mục."
    sc.append(S_('checklist', 'Chương 6 – Từng mã một nét chính', ('TỪNG MÃ', 'MỘT NÉT CHÍNH'), say, anh='stock list', items=[(s + ': ' + (KQ[s]['good'] or KQ[s]['info'][2:3] or KQ[s]['info'][:1])[0].split(', ')[0][:28], GREEN) for s in syms[:5]]))
    adv = sum(I[x]['dd'] for x in syms) / len(syms)
    say = ("Chương bảy, tỷ trọng cả nhóm, ví dụ bằng số. Bình quân %d mã trong video đang thấp hơn đỉnh 52 tuần khoảng %s%%. Giả sử một danh mục đặt 40%% vào nhóm %s, chia đều cho các mã, và mua đúng vùng đỉnh. "
           "Khi đó riêng nhóm này đã kéo cả danh mục giảm khoảng %s%%. Nếu chỉ đặt 20%%, mức kéo giảm còn khoảng %s%%. Cùng một nhóm cổ phiếu, cùng một diễn biến giá, nhưng kết quả của danh mục khác nhau gấp đôi chỉ vì quyết định tỷ trọng. "
           "Đó là lý do quản trị rủi ro bắt đầu từ tỷ trọng, trước cả việc chọn mã.") % (len(syms), vn(adv, 1), nhom, vn(adv * 0.4, 1), vn(adv * 0.2, 1))
    sc.append(S_('bignum', 'Chương 7 – Tỷ trọng cả nhóm', ('TỶ TRỌNG', 'CẢ NHÓM'), say, moc=True, value=-round(adv * 0.4, 1), fmt='{:,.1f}', unit='%', top='40% DANH MỤC VÀO NHÓM', sub='20%% thì còn −%s%%' % vn(adv * 0.2, 1), col=RED))
    say = "Chương tám, cách tự so sánh một nhóm ngành. Một, xếp lợi nhuận quý và lũy kế cạnh nhau. Hai, đặt P/E, P/B cạnh ROE. Ba, xem giá cách đỉnh và beta để biết mức rung lắc. Bốn, ghi rủi ro riêng của từng mã. Năm, quyết định tỷ trọng cho cả nhóm trước, rồi mới chia cho từng mã. " + WEB[2]
    sc.append(S_('checklist', 'Chương 8 – Năm bước so sánh nhóm', ('NĂM BƯỚC', 'SO SÁNH NHÓM'), say, anh='checklist notebook',
                 items=[('Lãi quý và lũy kế', GREEN), ('P/E, P/B cạnh ROE', GREEN), ('Cách đỉnh, beta', GOLD), ('Rủi ro riêng từng mã', RED), ('Tỷ trọng cả nhóm', GOLD)]))
    sc.append(S_('end', None, (h1, h2), "Số liệu từ báo cáo tài chính Q3/2026 và dữ liệu tổng hợp ngày %s. Trong nhóm này, anh chị theo dõi mã nào, và vì sao?" % NGAY_DL)); sc[-1].pop('ch')
    M = dict(kenh="Kênh 2 (@chungkhoanhuynguyen2) – Cổ Phiếu Mỗi Ngày", seri="Cổ phiếu mỗi ngày", ngay=ngay, gio_goi_y="19:00", gio="19:00", tieu_de=title, title=title,
             mo_ta=mo_ta(title, "Số liệu từ báo cáo tài chính và dữ liệu tổng hợp đến ngày %s; bài học là cách đọc dùng được nhiều năm." % NGAY_DL, "Cổ phiếu mỗi ngày", link),
             tags=["cổ phiếu %s" % nhom] + syms[:5] + ["so sánh cổ phiếu"], bia_hook=[h1, h2], badge=nhom.upper()[:16],
             fb_post=fb("%s – %s" % (h1, h2), ["%s: lãi quý 3 %s, P/E %s" % (s, pct(g[s]) if g[s] is not None else 'lỗ', vn(I[s]['f']['pe'], 2)) for s in syms[:5]], "Trong nhóm này, anh chị theo dõi mã nào?", link, "📊"),
             chuong=[c['ch'] for c in sc if c.get('ch')], seri_web="Cổ phiếu mỗi ngày", link_web=link)
    return sc, M
