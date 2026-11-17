# -*- coding: utf-8 -*-
# NV1 18/11/2026 – REEL "câu hỏi lớn" cặp với CH2411NX (hết ưu đãi lãi vay mua nhà, nợ nhóm 2 tăng 52,4%). Nguồn + cách tính: nv1/ql_no_tre_han.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261118_0040_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Nếu lãi vay lên 15%, nhà anh chị còn gánh được bằng thu nhập, hay phải rút tiết kiệm? Khoản vay của anh chị hết ưu đãi vào lúc nào?'
R = dict(key='RV1811NX', tieu_de='Hết ưu đãi, lãi vay mua nhà lên 14%: trả góp thêm 8,25 triệu mỗi tháng – nợ trễ hạn tại 28 ngân hàng tăng 52,4%',
 hook=['HẾT ƯU ĐÃI, LÃI VAY LÊN 14%', 'NHÀ MÌNH CÒN GÁNH NỔI???'], nhan='LÃI VAY · HỎI THẬT',
 short_caption=('Lãi thả nổi vay mua nhà quý 3/2026 ở mức 12–15% (SSI Research, Công Luận 6/11/2026). Nợ nhóm 2 tại 28 ngân hàng niêm yết 253.048 tỷ, +52,4%; nợ xấu 340.816 tỷ, +26,9%; bao phủ khoảng 80%, thấp nhất 5 năm '
                '(VietnamFinance 11/11/2026). Nợ xấu gộp toàn hệ thống 3,9% cuối 8/2026 (NHNN, Báo Đấu thầu 9/11/2026); 9/2012 NHNN giám sát 8,82% (VnEconomy 1/1/2013). '
                'Khoản vay 2 tỷ 20 năm là giả định, em tự tính. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH GÁNH ĐƯỢC KHÔNG?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City skyline night', 'Hanoi apartment buildings']),
 canh=[
  C('LÃI THẢ NỔI 12 ĐẾN 15%', 'Hết hai năm ưu đãi, nhiều người vay mua nhà vừa nhận thông báo lãi mới. Lãi thả nổi hiện đang ở mức 12 đến 15% mỗi năm.',
    the=dict(loai='lon', tieu='LÃI THẢ NỔI VAY MUA NHÀ QUÝ 3/2026', nguon='SSI Research, Công Luận 6/11/2026', dong=[['12 ĐẾN 15%', 120, 'do'], ['SAU KHI HẾT ƯU ĐÃI', 56, 'trang']])),
  C('THÊM HƠN 8 TRIỆU', 'Một khoản vay 2 tỷ, 20 năm, lãi từ 8,5% lên 14%. Sau hai năm, kỳ trả góp từ khoảng 21 triệu lên hơn 29 triệu, thêm hơn 8 triệu mỗi tháng, em tự tính.',
    the=dict(loai='cot', tieu='KỲ TRẢ GÓP MỖI THÁNG (TRIỆU ĐỒNG)', nguon='Em giả định khoản vay 2 tỷ, tự tính', hang=[['Lãi 8,5%', 21.08], ['Lãi 14%', 29.33]], noi=[1], dv='', max=35)),
  C('TRỄ 10 NGÀY LÀ NHÓM 2', 'Nhiều người nghĩ trả chậm vài ngày không sao. Nhưng theo quy định, trễ từ 10 ngày là khoản vay đã sang nợ nhóm 2, gọi là nợ cần chú ý.',
    the=dict(loai='lon', tieu='PHÂN LOẠI NỢ', nguon='Thông tư 31/2024/TT-NHNN', dong=[['TRỄ 10 NGÀY', 116, 'vang'], ['ĐÃ LÀ NỢ NHÓM 2', 58, 'trang']])),
  C('NỢ NHÓM 2 TĂNG 52,4%', 'Ở 28 ngân hàng niêm yết, nợ nhóm 2 đã lên khoảng 253.000 tỷ đồng. Con số này tăng 52,4% chỉ sau 9 tháng.',
    the=dict(loai='lon', tieu='NỢ NHÓM 2, 28 NGÂN HÀNG, 30/9/2026', nguon='SSI Research, VietnamFinance 11/11/2026', dong=[['TĂNG 52,4%', 120, 'do'], ['253.048 TỶ ĐỒNG', 58, 'trang']])),
  C('LÃI KỶ LỤC, DỰ PHÒNG MỎNG', 'Ngân hàng vẫn lãi 311.100 tỷ đồng trong 9 tháng. Nhưng tiền dự phòng chỉ còn bằng khoảng 80% nợ xấu, mức thấp nhất 5 năm.',
    the=dict(loai='lon', tieu='TỶ LỆ BAO PHỦ NỢ XẤU', nguon='VietnamFinance 11/11/2026; SHS, 24hmoney 10/11/2026', dong=[['80%', 130, 'do'], ['THẤP NHẤT 5 NĂM', 58, 'trang']])),
  C('2012: GẦN 8,8%', 'Lần trước, năm 2012, nợ xấu theo giám sát của Ngân hàng Nhà nước gần 8,8%. Hôm nay nợ xấu gộp là 3,9%. Hệ thống còn khỏe hơn, nhưng con số đang đi lên.',
    the=dict(loai='cot', tieu='NỢ XẤU (%)', nguon='VnEconomy 1/1/2013; NHNN, Báo Đấu thầu 9/11/2026', hang=[['NHNN 9/2012', 8.82], ['Gộp 8/2026', 3.9]], noi=[1], dv='%', max=10)),
  C('GẶP NGÂN HÀNG SỚM', 'Nếu lãi lên 15% mà thu nhập không gánh nổi, nên gặp ngân hàng ngay khi còn trả được. Kéo dài thời hạn hay trả bớt gốc đều dễ hơn khi chưa trễ ngày nào.',
    the=dict(loai='lon', tieu='LÀM TRƯỚC KHI TRỄ HẠN', nguon='Quan điểm cá nhân', dong=[['ĐI SỚM', 120, 'vang'], ['KHI CÒN Ở NHÓM 1', 58, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.path.insert(0, CW + '/_video'); import kiem_loi
print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
    if 'câu cụt' not in q: print(q)
for c in R['canh']: print(c['loi_doc'][:200])
