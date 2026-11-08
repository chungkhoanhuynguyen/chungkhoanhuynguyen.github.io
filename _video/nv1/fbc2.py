# -*- coding: utf-8 -*-
# NV1 9/11/2026 – 35 caption FB trang chính 7–13/12/2026. Chủ đề tuần: ĐỘ BIẾN ĐỘNG & CHIA VỐN THEO RỦI RO.
import json, re, datetime, math, statistics as st
from lib import *
LOAI = {'STB', 'SHB', 'EIB', 'VIC', 'PNJ', 'DGC', 'VEA', 'FPT'}
def g(line):
    m = re.search(r"\(([+−][\d.,]+)%", line)
    return float(m.group(1).replace('−', '-').replace('.', '').replace(',', '.')) if m else None
OLD = []
for s, x in KQ.items():
    if s in LOAI or not fund(s): continue
    q, lk = g(x['info'][0]), g(x['info'][1])
    if q is not None and lk is not None: OLD.append((abs(q - lk), s))
OLD = {s for _, s in sorted(OLD, reverse=True)[:35]}
C = []
for s, x in KQ.items():
    f = fund(s)
    if s in LOAI or s in OLD or not f or f.get('mc', 0) < 1500 or not f.get('pe') or f['pe'] <= 0: continue
    try: c = [r[4] for r in daily(s)]
    except Exception: continue
    if len(c) < 500: continue
    r = [c[i] / c[i - 1] - 1 for i in range(1, len(c)) if c[i - 1]]
    v = st.pstdev(r) * math.sqrt(250) * 100; C.append((f['mc'], s, v))
C.sort(reverse=True); C = C[:35]; C.sort(key=lambda t: t[2])
T = ['07:30', '10:30', '13:30', '17:00', '20:30']; d0 = datetime.date(2026, 12, 7); posts = []
for i, (_, s, v) in enumerate(C):
    x = KQ[s]; f = fund(s); d = d0 + datetime.timedelta(days=i // 5)
    vm = v / math.sqrt(12); stop = 2 * vm; pos = 10 / (stop / 100)
    h1 = "📊 %s DAO ĐỘNG %s%%" % (s, vn(v, 1)); h2 = "🛡️ VỊ THẾ 1%%: %s TR" % vn(pos, 0)
    cap = ("%s\n%s\n\nCùng 100 triệu nhưng rủi ro không bằng nhau. Độ biến động năm của %s khoảng %s%% (giá đóng cửa điều chỉnh 10/2023–6/11/2026), tức dao động khoảng %s%% trong một tháng bình thường.\n\n"
           "🛡️ QUẢN TRỊ VỐN: với danh mục 1 tỷ và mỗi lệnh chỉ chấp nhận mất 1%% (10 triệu), nếu đặt điểm sai khoảng %s%% (2 lần dao động tháng) thì vị thế %s vào khoảng %s triệu, có trần 20%% danh mục.\n\n"
           "👉 %s\n👉 %s\n\nĐịnh giá ngày 6/11/2026: P/E %s, P/B %s, ROE %s%%, beta %s.\n\nAnh chị đang chia vốn đều theo tiền, hay đã chia theo mức dao động của từng mã?\n\n%s\n%s #ChungKhoan #QuanTriVon #%s") % (
        h1, h2, s, vn(v, 1), vn(vm, 1), vn(stop, 1), s, vn(pos, 0), x['info'][0], x['info'][1], vn(f['pe'], 2), vn(f['pb'], 2), vn(f['roe'], 1), vn(f['beta'], 2), CS_AN[0], CS_AN[1], s)
    posts.append({"trang": "Nguyễn Huy Anh (trang chính)", "date": d.isoformat(), "time": T[i % 5], "key": "FB_%s_%d_%s" % (d.strftime('%m%d'), i % 5 + 1, s), "ma": s,
                  "hook1": h1, "hook2": h2, "anh_goi_y": "chụp trang chungkhoanhuynguyen.com/ma/%s.html (giữ thanh menu HUY NGUYỄN CHỨNG KHOÁN)" % s, "caption": cap})
note = "35 caption FB trang chính 7–13/12/2026 (5 bài/ngày, từ mã ít dao động tới nhiều dao động). Chủ đề tuần: ĐỘ BIẾN ĐỘNG & CHIA VỐN THEO RỦI RO (khớp video CH2711B, bài F0 do-bien-dong-co-phieu-la-gi). 35 vốn hóa lớn nhất có P/E>0, không trùng mã tuần trước; loại %s." % ", ".join(sorted(LOAI))
for j in range(3):
    json.dump({"ghi_chu": note, "posts": posts[j * 12:(j + 1) * 12]}, open('/tmp/sp/tp/fb_chinh_%d.json' % (j + 1), 'w', encoding='utf-8'), ensure_ascii=False)
print(len(posts), [(p['ma'], p['hook1'], p['hook2']) for p in posts][:6]); print(posts[-1]['caption'])
