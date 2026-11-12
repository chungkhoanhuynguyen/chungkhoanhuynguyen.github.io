# -*- coding: utf-8 -*-
# NV1 13/11/2026 – REEL "câu hỏi lớn" cặp với CH1611GDP: GDP tăng gần 10%, lương thật tăng bao nhiêu? (số liệu như nv1/ql_gdp_luong.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261113_0037_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
N = 'Tổng cục Thống kê – tổng hợp WiData'
Q = 'Nếu lấy lương tháng này chia lương cùng tháng năm ngoái, lương của anh chị tăng bao nhiêu phần trăm, có theo kịp giá cả không?'
R = dict(key='RV1311GDP', tieu_de='GDP tăng gần 10% nhưng lương thật chỉ tăng 4,5%: phần còn lại đi đâu?',
 hook=['GDP TĂNG GẦN 10%', 'LƯƠNG THẬT TĂNG MẤY???'], nhan='VĨ MÔ · HỎI THẬT',
 short_caption=('GDP quý 3/2026 tăng 9,95%. Thu nhập bình quân người lao động tăng 9,85%, từ 8,36 lên 9,18 triệu mỗi tháng, nhưng trừ giá cả chỉ còn khoảng 4,5%. '
                'Xăng dầu tăng 15,6%, tiền nhà điện nước tăng 6,5% so cùng kỳ. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='LƯƠNG ANH CHỊ TĂNG MẤY %?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City skyline night', 'Hanoi skyline night']),
 canh=[
  C('GDP TĂNG 9,95%', 'GDP quý 3 năm 2026 vừa tăng 9,95%, cao nhất nhiều năm. Nhưng lương của người đi làm thật sự tăng bao nhiêu? Em kiểm tra bằng số liệu thật.',
    the=dict(loai='lon', tieu='GDP QUÝ 3/2026 SO CÙNG KỲ', nguon=N, dong=[['+9,95%', 90, 'vang'], ['CAO NHẤT NHIỀU NĂM', 52, 'trang']])),
  C('LƯƠNG TĂNG 9,85%', 'Thu nhập bình quân người lao động quý 3 là 9,18 triệu mỗi tháng, năm ngoái là 8,36 triệu. Tăng 9,85%, nghe cũng gần bằng GDP.',
    the=dict(loai='cot', tieu='THU NHẬP MỖI THÁNG (TRIỆU ĐỒNG)', nguon=N, hang=[['Q3/2024', 7.63], ['Q3/2025', 8.36], ['Q3/2026', 9.18]], noi=[2], dv='', max=10)),
  C('TRỪ GIÁ CẢ CÒN 4,5%', 'Nhưng giá cả cũng tăng khoảng 5,1%. Trừ đi, thu nhập thật chỉ tăng khoảng 4,5%, chưa bằng một nửa tốc độ GDP.',
    the=dict(loai='cot', tieu='TĂNG TRONG 12 THÁNG (%)', nguon='TCTK – em tự tính thu nhập thật', hang=[['GDP thực', 9.95], ['Thu nhập thật', 4.5]], noi=[1], dv='%', max=12)),
  C('XĂNG TĂNG 15,6%', 'Tệ hơn, thứ người đi làm trả mỗi ngày lại tăng nhanh nhất. Nhóm xăng dầu, đi lại tăng 15,6%. Tiền nhà, điện nước tăng 6,5%.',
    the=dict(loai='cot', tieu='GIÁ THÁNG 10/2026 SO CÙNG KỲ (%)', nguon='TCTK – em tự tính từ chỉ số giá', hang=[['Xăng, đi lại', 15.6], ['Nhà, điện nước', 6.5], ['Hàng ăn', 3.6]], noi=[0], dv='%', max=18)),
  C('TĂNG 820K, CÒN 390K', 'Một công nhân lương tăng 820 nghìn mỗi tháng. Với rổ chi tiêu em giả định, giá cả ăn mất khoảng 432 nghìn, còn lại chừng 390 nghìn.',
    the=dict(loai='lon', tieu='PHẦN LƯƠNG TĂNG CÒN LẠI', nguon='Em tự tính, rổ chi tiêu giả định', dong=[['CÒN 390 NGHÌN', 70, 'do'], ['TRÊN 820 NGHÌN TĂNG THÊM', 46, 'trang']])),
  C('CHIẾC BÁNH LỚN NHANH HƠN', 'Trong 12 tháng, GDP danh nghĩa lớn thêm 12,9%, thu nhập lao động chỉ 9,85%. Phần bánh lớn hơn nằm ở lợi nhuận, thuế và tài sản.',
    the=dict(loai='cot', tieu='TĂNG TRONG 12 THÁNG (%)', nguon='TCTK – em tự tính', hang=[['GDP danh nghĩa', 12.9], ['Thu nhập lao động', 9.85]], noi=[1], dv='%', max=15)),
  C('PHÉP THỬ CỦA ANH CHỊ', 'Lương tăng dưới 5,1% là đang nghèo đi. Từ 5,1 đến 9,85% là giàu lên chậm hơn bình quân. Trên 9,85% mới theo kịp cả nước.',
    the=dict(loai='lon', tieu='LƯƠNG NĂM NAY TĂNG', nguon='So với CPI 5,08% và thu nhập bình quân +9,85%', dong=[['DƯỚI 5,1%: NGHÈO ĐI', 50, 'do'], ['TRÊN 9,85%: THEO KỊP', 50, 'vang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
    if 'câu cụt' not in q: print(q)
