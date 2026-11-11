# -*- coding: utf-8 -*-
# NV1 12/11/2026 – REEL "câu hỏi lớn" cặp với CH1411NO: Việt Nam đang nợ bao nhiêu? (số liệu như nv1/ql_no_vn.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261112_0039_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
N = 'NHNN, Bộ Tài chính, TCTK – tổng hợp WiData'
R = dict(key='RV1211NO', tieu_de='Việt Nam đang nợ bao nhiêu? Nợ công chỉ 33% GDP, nhưng dư nợ cho vay đã 146% GDP',
 hook=['NỢ CÔNG CHỈ 33% GDP', 'NỢ THẬT NẰM Ở ĐÂU???'], nhan='VĨ MÔ · HỎI THẬT',
 short_caption=('Nợ công Việt Nam năm 2025 chỉ khoảng 33% GDP và đang giảm. Nhưng dư nợ cho vay của cả nền kinh tế đã khoảng 20,5 triệu tỷ đồng, bằng 146% GDP, '
                'tăng 17,4% trong khi tiền gửi chỉ tăng 13,6%. Người vay lãi thả nổi mới là người cần để ý. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='LÃI LÊN 11% THÌ SAO?', loi='Nếu lãi vay nhà mình lên 11%, anh chị sẽ trả bớt nợ, bán bớt tài sản hay cứ giữ nguyên?',
              loi_doc=lib.doc('Nếu lãi vay nhà mình lên 11%, anh chị sẽ trả bớt nợ, bán bớt tài sản hay cứ giữ nguyên?'), anh=['ov:apartment building night||apartment building']),
 canh=[
  C('VIỆT NAM NỢ BAO NHIÊU?', 'Ngày 2/11/2026, VnEconomy vừa đưa tin nợ công của Mỹ so với GDP lên mức cao nhất 80 năm. Còn Việt Nam đang nợ bao nhiêu? Em kiểm tra bằng số liệu thật, và kết quả bất ngờ.',
    anh=['ov:newspaper finance headline||newspaper'], chat=1),
  C('NỢ CÔNG CHỈ 33% GDP', 'Năm 2025, nợ công khoảng 4,27 triệu tỷ đồng, chỉ khoảng 33% GDP. Năm 2018 con số này còn là 45,7%. Gánh nợ của Nhà nước đang nhẹ đi.',
    the=dict(loai='cot', tieu='NỢ CÔNG / GDP', nguon='Bộ Tài chính, TCTK – em tự tính', hang=[['2018', 45.7], ['2025', 33.3]], noi=[1], dv='%', max=50)),
  C('NHƯNG CÓ KHOẢN NỢ KHÁC', 'Khoản nợ đáng để ý nằm ở ngân hàng. Tháng 8/2026, dư nợ cho vay cả nền kinh tế khoảng 20,5 triệu tỷ đồng, gấp 4,8 lần nợ công.',
    the=dict(loai='lon', tieu='DƯ NỢ CHO VAY THÁNG 8/2026', nguon=N, dong=[['20,49 TRIỆU TỶ', 76, 'do'], ['GẤP 4,8 LẦN NỢ CÔNG', 52, 'trang']])),
  C('146% GDP', 'So với nền kinh tế, năm 2016 dư nợ bằng khoảng 98% GDP. Tháng 8/2026 đã khoảng 146%. Mười năm, dư nợ tăng gần gấp 4, GDP chỉ gấp 2,5.',
    the=dict(loai='cot', tieu='DƯ NỢ CHO VAY / GDP (%)', nguon='NHNN, TCTK – em tự tính', hang=[['2016', 97.6], ['2020', 114.3], ['2024', 135.7], ['8/2026', 145.8]], noi=[3], dv='%', max=160)),
  C('DỒN VỀ NHÀ ĐẤT', 'Khoảng 45% dư nợ nằm ở nhóm phần lớn là cho vay bất động sản và tiêu dùng, chủ yếu vay mua nhà. Nhóm này tăng 24,4% trong một năm.',
    the=dict(loai='lon', tieu='NHÓM BẤT ĐỘNG SẢN, TIÊU DÙNG', nguon=N, dong=[['45% TỔNG DƯ NỢ', 64, 'vang'], ['+24,4% TRONG 1 NĂM', 58, 'do']])),
  C('CHO VAY NHANH HƠN GỬI', 'Cho vay tăng 17,4%, tiền gửi chỉ tăng 13,6%. Ngân hàng thiếu vốn thì phải trả lãi cao hơn, và người vay lãi thả nổi gánh phần chênh đó.',
    the=dict(loai='cot', tieu='TĂNG TRONG 12 THÁNG (%)', nguon=N, hang=[['Cho vay', 17.4], ['Tiền gửi', 13.6]], noi=[0], dv='%', max=20)),
  C('VAY 1,2 TỶ MUA NHÀ', 'Vay 1,2 tỷ trong 20 năm: lãi 8% trả khoảng 10,04 triệu mỗi tháng. Lên 10% là 11,58 triệu mỗi tháng, thêm khoảng 371 triệu sau 20 năm.',
    the=dict(loai='cot', tieu='TRẢ MỖI THÁNG (TRIỆU ĐỒNG)', nguon='Em tự tính: trả đều gốc và lãi 240 tháng', hang=[['Lãi 8%', 10.04], ['Lãi 10%', 11.58], ['Lãi 11%', 12.39]], noi=[2], dv='', max=14)),
  C('ĐỪNG SỢ SAI CHỖ', 'Nước mình chưa đến mức vỡ nợ. Điều đáng lo là khoản vay của chính gia đình mình khi lãi suất đổi chiều.',
    anh=['ov:family apartment living room||family home'], chat=1),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
    if 'câu cụt' not in q: print(q)
