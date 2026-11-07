# -*- coding: utf-8 -*-
import json, re, datetime
from lib import *
LOAI = {'STB', 'SHB', 'EIB', 'VIC', 'PNJ', 'DGC', 'VEA', 'FPT'}
def g(line):
    m = re.search(r"\(([+−][\d.,]+)%", line); 
    if m: return float(m.group(1).replace('−', '-').replace('.', '').replace(',', '.'))
    m = re.search(r"gấp ([\d,]+) lần", line)
    return (float(m.group(1).replace(',', '.')) - 1) * 100 if m else None
R = []
for s, x in KQ.items():
    if s in LOAI or not fund(s): continue
    q, lk = g(x['info'][0]), g(x['info'][1])
    if q is None or lk is None: continue
    R.append((abs(q - lk), s, q, lk))
R.sort(reverse=True); R = R[:35]
T = ['07:30', '10:30', '13:30', '17:00', '20:30']; d0 = datetime.date(2026, 11, 30); posts = []
for i, (_, s, q, lk) in enumerate(R):
    x = KQ[s]; f = fund(s); d = d0 + datetime.timedelta(days=i // 5)
    cung = (q >= 0) == (lk >= 0)
    h1 = "%s %s QUÝ 3 %s%%" % ("📈" if q >= 0 else "📉", s, ("+" if q >= 0 else "−") + vn(abs(q), 1))
    h2 = "🧮 9 THÁNG %s%%" % (("+" if lk >= 0 else "−") + vn(abs(lk), 1))
    rr = "; ".join(x['bad'][:2]); gg = "; ".join(x['good'][:2])
    cap = "%s\n%s\n\n%s – quý 3 và lũy kế 9 tháng đang kể %s.\n\n👉 %s\n\n👉 %s\n\n%s%s🛡️ QUẢN TRỊ RỦI RO: một quý chưa đủ để kết luận. Khi quý 3 và 9 tháng lệch nhau xa, hãy tìm khoản bất thường, nền so sánh hoặc chi phí dự phòng trước khi tăng tỷ trọng. Beta %s cho biết mức rung lắc so với thị trường.\n\nĐịnh giá (%s): P/E %s, P/B %s, ROE %s%%\n\nVới %s, anh chị tin con số quý 3 hay con số 9 tháng hơn?\n\n%s\n%s\nSố liệu: BCTC hợp nhất Q3/2026, dữ liệu tổng hợp 6/11/2026.\n#ChungKhoan #%s #QuanTriRuiRo" % (
        h1, h2, s, "cùng một câu chuyện" if cung else "hai câu chuyện ngược nhau", x['info'][0], x['info'][1],
        ("✅ Điểm tích cực: %s.\n\n" % gg) if gg else "", ("⚠️ Rủi ro cần theo dõi: %s.\n\n" % rr) if rr else "", vn(f['beta'], 2), "6/11/2026",
        vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), s, CS_AN[0], CS_AN[1], s)
    posts.append({"trang": "Nguyễn Huy Anh (trang chính)", "date": d.isoformat(), "time": T[i % 5], "key": "FB_%s_%d_%s" % (d.strftime('%m%d'), i % 5 + 1, s), "ma": s,
                  "hook1": h1, "hook2": h2, "anh_goi_y": "chụp trang chungkhoanhuynguyen.com/ma/%s.html (giữ thanh menu HUY NGUYỄN CHỨNG KHOÁN)" % s, "caption": cap})
note = "35 caption FB trang chính 30/11–6/12/2026 (5 bài/ngày). Chủ đề tuần: CHẤT LƯỢNG LỢI NHUẬN – quý 3 lệch xa lũy kế 9 tháng + beta (quản trị rủi ro). Hook IN HOA 2 dòng, câu hỏi mở, Zalo 1 câu. Loại %s. Ảnh: chụp trang mã trên web." % ", ".join(sorted(LOAI))
for j in range(3):
    json.dump({"ghi_chu": note, "posts": posts[j * 12:(j + 1) * 12]}, open('/tmp/sp/tp/fb_chinh_%d.json' % (j + 1), 'w', encoding='utf-8'), ensure_ascii=False)
print(len(posts), [p['ma'] for p in posts]); print(posts[0]['caption'])
# nhóm FB: 8 bài, link web dạng chữ, không Zalo
NH = []
pick = ['NAB', 'GAS', 'KLB', 'VJC', 'VAB', 'DPM', 'GMD', 'HVN']
for i, s in enumerate(pick):
    x = KQ[s]; f = fund(s); c = close(s); dd = (f['h52'] - c) / f['h52'] * 100
    txt = "%s – đọc nhanh báo cáo quý 3/2026\n\n• %s\n• %s\n• %s\n%s\nĐịnh giá ngày 6/11/2026: P/E %s, P/B %s, ROE %s%%, beta %s. Giá đóng cửa khoảng %s, thấp hơn đỉnh 52 tuần khoảng %s%%.\n\nQuản trị rủi ro: trước khi mua, hãy viết sẵn tỷ trọng tối đa và điều kiện khiến lý do mua không còn đúng.\n\nAnh chị đang theo dõi %s vì lợi nhuận, vì định giá hay vì mức giảm từ đỉnh?\n\nBảng số đầy đủ: chungkhoanhuynguyen.com/ma/%s.html" % (
        s, x['info'][0], x['info'][1], x['info'][2] if len(x['info']) > 2 else "", ("• Cần theo dõi: %s\n" % x['bad'][0]) if x['bad'] else "", vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), vn(f['beta'], 2), vn(c, 2), vn(dd, 1), s, s)
    NH.append({"stt": i + 1, "ma": s, "noi_dung": txt, "anh_goi_y": "chụp trang chungkhoanhuynguyen.com/ma/%s.html" % s})
json.dump({"ghi_chu": "8 bài đăng nhóm FB (NV4), số liệu kqkd.bin/fund.bin/recent.bin 6/11/2026, link web dạng chữ, KHÔNG link Zalo, không hô mua bán. Mỗi nhóm dùng bài khác nhau.", "bai": NH}, open('/tmp/sp/tp/nhom_fb.json', 'w', encoding='utf-8'), ensure_ascii=False)
print(NH[0]['noi_dung'])
