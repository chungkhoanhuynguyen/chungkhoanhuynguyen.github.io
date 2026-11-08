# -*- coding: utf-8 -*-
import json, unicodedata, re, datetime, itertools, os
from lib import *
LOAI = {'STB', 'SHB', 'EIB', 'VIC', 'PNJ', 'DGC', 'VEA'}
def ascii_(t): t = unicodedata.normalize('NFD', t.replace('đ', 'd').replace('Đ', 'D')); return ''.join(c for c in t if unicodedata.category(c) != 'Mn')
def cl(s):
    r = RECENT.get(s); return r[-1][4] / 100 if r else None
G = {}
for s, sec in SEC.items():
    f = fund(s)
    if s in LOAI or not f or f.get('mc', 0) < 1500: continue
    G.setdefault(sec, []).append(s)
SECS = [k for k, v in G.items() if len(v) >= 5]
M = {  # key: (tiêu đề, sub, hướng, đơn vị, hàm, nhãn hook, link f0, câu giải thích, câu hỏi, chủ đề)
 'PE': ("P/E thấp nhất nhóm", "P/E (lần), thấp nhất", 'asc', 'lần', lambda f, s: f['pe'] if f['pe'] > 0 else None, "P/E", "pe-la-gi", "P/E thấp chưa chắc là rẻ: cần xem thêm tốc độ tăng lợi nhuận và việc lợi nhuận có đột biến hay không.", "Khi xem nhóm này, anh chị ưu tiên P/E hay tốc độ tăng lợi nhuận?", "Chỉ số theo ngành – P/E"),
 'PB': ("P/B thấp nhất nhóm", "P/B (lần), thấp nhất", 'asc', 'lần', lambda f, s: f['pb'] if f['pb'] > 0 else None, "P/B", "pb-la-gi", "P/B thấp chưa chắc rẻ nếu ROE thấp; cần xem thêm chất lượng tài sản và khả năng sinh lời.", "Khi xem định giá, anh chị nhìn P/B hay ROE trước?", "Chỉ số theo ngành – P/B"),
 'ROE': ("ROE cao nhất nhóm", "ROE (%), cao nhất", 'desc', '%', lambda f, s: f['roe'], "ROE", "roe-eps-la-gi", "ROE cao có thể đến từ đòn bẩy vay nợ, nên xem ROE nhiều năm cùng mức nợ.", "Anh chị tin ROE một năm hay ROE trung bình nhiều năm hơn?", "Chỉ số theo ngành – ROE"),
 'BETA': ("BETA thấp nhất nhóm", "Hệ số beta, thấp nhất", 'asc', 'hệ số', lambda f, s: f['beta'] if f.get('v10', 0) > 50000 and f['beta'] > 0.05 else None, "BETA", "beta-danh-muc-la-gi", "QUẢN TRỊ RỦI RO: beta dưới 1 nghĩa là giá thường dao động ít hơn thị trường chung. Beta thấp giúp danh mục bớt rung lắc, nhưng không bảo vệ khỏi rủi ro riêng của doanh nghiệp.", "Danh mục của anh chị đang nghiêng về mã beta cao hay beta thấp?", "Quản trị rủi ro – Hệ số beta"),
 'DD': ("cách đỉnh 52 tuần xa nhất nhóm", "Thấp hơn đỉnh 52 tuần (%)", 'desc', '%', lambda f, s: round((f['h52'] - cl(s)) / f['h52'] * 100, 1) if cl(s) and f.get('h52') else None, "", "ke-hoach-khi-vn-index-giam-20-phan-tram", "QUẢN TRỊ VỐN: mã cách đỉnh 52 tuần càng xa thì người mua ở đỉnh càng cần lãi nhiều mới hòa vốn (lỗ 40% cần lãi khoảng 67%). Trước khi bắt đáy, hãy đặt sẵn tỷ trọng tối đa và điểm sai của lệnh.", "Với mã đã giảm sâu từ đỉnh, anh chị đặt tỷ trọng tối đa bao nhiêu phần trăm danh mục?", "Quản trị vốn – Khoảng cách tới đỉnh 52 tuần"),
 'FO': ("SỞ HỮU NN cao nhất nhóm", "Sở hữu nước ngoài (%), cao nhất", 'desc', '%', lambda f, s: f['fo'] if f['fo'] > 0 else None, "SỞ HỮU NN", "khoi-ngoai-mua-rong-ban-rong-la-gi", "Tỷ lệ sở hữu nước ngoài cao cho thấy mã được nhà đầu tư tổ chức quan tâm, nhưng cũng nhạy hơn khi khối ngoại bán ròng.", "Anh chị có theo dõi giao dịch khối ngoại ở mã mình nắm giữ không?", "Chỉ số theo ngành – Sở hữu nước ngoài"),
 'GAN': ("gần đáy 52 tuần nhất nhóm", "Cao hơn đáy 52 tuần (%)", 'asc', '%', lambda f, s: round((cl(s) - f['l52']) / f['l52'] * 100, 1) if cl(s) and f.get('l52') and cl(s) >= f['l52'] else None, "", "dung-lo-dong-trung-binh-gia-xuong", "QUẢN TRỊ RỦI RO: giá gần đáy 52 tuần chưa chắc là đáy. Đừng bình quân giá xuống khi chưa biết vì sao giá giảm; hãy đọc lại kết quả kinh doanh trước.", "Khi một mã về gần đáy 52 tuần, anh chị đọc lại báo cáo hay mua thêm trước?", "Quản trị rủi ro – Gần đáy 52 tuần"),
}
def fmt(v, k): return vn(v, 1) if k in ('ROE', 'DD', 'FO', 'GAN') else vn(v, 2)
def post(page, date, time, idx, sec, k):
    t, sub, dirn, dv, fn, lab, f0, ex, q, chude = M[k]
    rows = [(s, fn(fund(s), s)) for s in G[sec]]; rows = [r for r in rows if r[1] is not None]
    rows.sort(key=lambda r: r[1], reverse=(dirn == 'desc')); rows = rows[:8]
    if len(rows) < 5: return None
    a, z = rows[0], rows[-1]; sl = sec.upper()
    if k == 'DD': h1 = "%s −%s%%" % (a[0], fmt(a[1], k)); h2 = "%s −%s%%" % (z[0], fmt(z[1], k)); dau = "XA ĐỈNH " + sl
    elif k == 'GAN': h1 = "%s +%s%% TỪ ĐÁY" % (a[0], fmt(a[1], k)); h2 = "%s +%s%%" % (z[0], fmt(z[1], k)); dau = "GẦN ĐÁY " + sl
    else: h1 = "%s %s %s%s" % (a[0], lab, fmt(a[1], k), '%' if dv == '%' else ''); h2 = "%s %s%s" % (z[0], fmt(z[1], k), '%' if dv == '%' else ''); dau = "%s %s" % (lab, sl)
    if len(h1) > 18: h1 = "%s %s%s" % (a[0], fmt(a[1], k), '%' if dv == '%' else '')
    nhom = sec.lower()
    if k == 'DD': line1 = "%s đang thấp hơn đỉnh 52 tuần khoảng %s%% – xa nhất nhóm %s (dữ liệu %s)" % (a[0], fmt(a[1], k), nhom, NGAY)
    elif k == 'GAN': line1 = "%s chỉ cao hơn đáy 52 tuần khoảng %s%% – gần đáy nhất nhóm %s (dữ liệu %s)" % (a[0], fmt(a[1], k), nhom, NGAY)
    else: line1 = "%s %s %s%s – %s nhóm %s (dữ liệu %s)" % (a[0], lab, fmt(a[1], k), '%' if dv == '%' else '', t.split(' nhóm')[0].replace(lab + ' ', '').strip(), nhom, NGAY)
    lb = {'DD': 'Cách đỉnh 52 tuần', 'GAN': 'Cao hơn đáy 52 tuần'}.get(k, lab)
    lst = " · ".join("%s %s%s%s" % (s, fmt(v, k), '%' if dv == '%' else '', "" if k == 'ROE' else " (ROE %s%%)" % vn(fund(s)['roe'], 1)) for s, v in rows)
    tagsec = "#CoPhieu" + ascii_(sec).title().replace(',', '').replace(' ', '')
    cap = "%s\n\n%s: %s\nMỗi doanh nghiệp có mô hình và chu kỳ khác nhau nên không nên so cứng.\n\n%s\n\n%s\n\n%s. Bản phân tích đầy đủ: trang Nguyễn Huy Anh.\n\nThông tin tham khảo, không phải khuyến nghị. #ChungKhoan %s #%s #%s%s" % (
        line1, lb, lst, ex, q, chude, tagsec, a[0], z[0], " #QuanTriRuiRo" if k in ('DD', 'BETA', 'GAN') else "")
    return {"page": page, "date": date, "time": time, "key": "%s%s_%s_%s_%d" % (page, os.environ.get("KP", "37"), ascii_(sec).upper().replace(',', '').replace(' ', '')[:6], k, idx), "type": "rank",
            "title": "%s: %s" % (sl, t), "sub": sub, "rows": [[s, v] for s, v in rows], "hook1": h1, "hook2": h2, "dau": dau, "tag": sl.replace(', ', ' – '), "don_vi": dv,
            "caption": cap, "binh_luan_ghim": "Tìm hiểu: chungkhoanhuynguyen.com/f0/%s.html · Dữ liệu: chungkhoanhuynguyen.com · Nhóm Zalo cộng đồng: zalo.me/g/jbnbiq994" % f0}
NGAY = "6/11/2026"
TIMES = {'TC': ['08:00', '12:00', '17:30', '20:30'], 'TT': ['07:00', '11:00', '16:00', '20:00'], 'ST': ['09:30', '13:30', '18:30', '21:30']}
OTHER = ['PE', 'PB', 'ROE', 'BETA', 'FO', 'GAN']
out = []
OFF = int(os.environ.get('OFF', '7')); d0 = datetime.date.fromisoformat(os.environ.get('D0', '2026-12-30')); n = 0
for di in range(7):
    d = (d0 + datetime.timedelta(days=di)).isoformat(); day = []; used = set()
    for pi, page in enumerate(['TC', 'TT', 'ST']):
        for si in range(4):
            k = 'DD' if si == 1 else OTHER[((di + OFF) * 5 + pi * 3 + si) % len(OTHER)]
            for j in range(len(SECS)):
                sec = SECS[((di + OFF) * 7 + pi * 4 + si * 3 + j) % len(SECS)]
                if (sec, k) in used or sec in {p['tag'] for p in day if p['page'] == page}: continue
                p = post(page, d, TIMES[page][si], di + 1, sec, k)
                if p: used.add((sec, k)); p['tag'] = p['tag']; day.append(p); break
    out.append(day); n += len(day)
os.makedirs('/tmp/sp/tp', exist_ok=True)
for i, day in enumerate(out):
    js = {"ghi_chu": "Trang phụ TC/TT/ST ngày %s (4 bài/trang; slot 2 mỗi trang là QUẢN TRỊ VỐN – cách đỉnh 52 tuần; thêm chỉ số mới GẦN ĐÁY 52 TUẦN = quản trị rủi ro). Số liệu fund.bin, giá recent.bin %s, nhóm ngành sec.bin, vốn hóa ≥1.500 tỷ; loại %s. Xưng anh chị; link ở bình luận ghim. Đủ hook1, hook2 (≤18 ký tự), dau, tag, don_vi." % (day[0]['date'], NGAY, ", ".join(sorted(LOAI))), "posts": day}
    json.dump(js, open('/tmp/sp/tp/trang_phu_%d.json' % (i + 1), 'w', encoding='utf-8'), ensure_ascii=False)
print(n, SECS)
for p in out[0]: print(p['page'], p['time'], p['key'], p['hook1'], '|', p['hook2'], len(p['hook1']), len(p['hook2']))
print(out[3][5]['caption'])
