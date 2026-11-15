# -*- coding: utf-8 -*-
# NV1 16/11/2026 – REEL "câu hỏi lớn" cặp với CH2111FED: Mỹ quay lại tăng lãi suất – năm 2022 có lặp lại? (nguồn như nv1/ql_fed_2022.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261116_0130_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Nếu cổ phiếu giảm 20% và lãi vay tăng 1 điểm cùng lúc, nhà anh chị vẫn ngủ ngon, phải cắt chi tiêu, hay phải bán gấp?'
R = dict(key='RV1611FED', tieu_de='Mỹ quay lại tăng lãi suất: năm 2022 Fed tăng 7 lần, VN-Index mất 32,8% – lần này thì sao?',
 hook=['MỸ QUAY LẠI TĂNG LÃI SUẤT', 'NĂM 2022 CÓ LẶP LẠI???'], nhan='THẾ GIỚI · HỎI THẬT',
 short_caption=('Khả năng Fed tăng lãi suất tháng 12 trên 80% (CME FedWatch, Vietnam+ 11/11/2026); giá xăng Mỹ +37%, PPI tháng 10 +6,5%; DXY 103,41 cao nhất từ 4/2025 (Hà Nội Mới 14/11). '
                'Năm 2022 Fed tăng 7 lần, VN-Index từ 1.498,28 xuống 1.007,09 điểm (−32,8%). Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH CHỊU NỔI?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City Stock Exchange', 'Ho Chi Minh City skyline night']),
 canh=[
  C('KHẢ NĂNG TRÊN 80%', 'Tuần này, công cụ dự báo của sàn CME vừa cho thấy khả năng Ngân hàng Trung ương Mỹ tăng lãi suất trong cuộc họp ngày 8 và 9 tháng 12 là trên 80%.',
    the=dict(loai='lon', tieu='FED TĂNG LÃI SUẤT THÁNG 12?', nguon='CME FedWatch, Vietnam+ 11/11/2026', dong=[['TRÊN 80%', 130, 'do'], ['KHẢ NĂNG TĂNG', 60, 'trang']])),
  C('XĂNG MỸ +37%', 'Lý do là lạm phát Mỹ chưa chịu hạ. Giá xăng tăng 37% so với năm ngoái, giá sản xuất tăng 6,5%, cao nhất kể từ tháng 11 năm 2022.',
    the=dict(loai='cot', tieu='NƯỚC MỸ, THÁNG 10/2026 (%)', nguon='Vietnam+ 11/11 và 14/11/2026', hang=[['Giá xăng', 37], ['Giá sản xuất', 6.5]], noi=[0], dv='%', max=40)),
  C('NVIDIA GIẢM 6 TUẦN', 'Cổ phiếu trí tuệ nhân tạo chao đảo. Giám đốc điều hành Nvidia từ chức, cổ phiếu có lúc giảm 13% trong phiên, giảm 6 tuần liền, chuỗi dài nhất từ năm 2012.',
    the=dict(loai='lon', tieu='NVIDIA', nguon='Vietnam+ 14/11/2026', dong=[['6 TUẦN', 130, 'do'], ['GIẢM LIÊN TIẾP', 60, 'trang']])),
  C('ĐÔ LA MẠNH NHẤT', 'Đồng đô la mạnh lên. Chỉ số DXY lên 103,41 điểm, cao nhất từ tháng 4 năm 2025. Giá bán đô la ở một ngân hàng lớn tăng 130 đồng chỉ trong một tuần.',
    the=dict(loai='lon', tieu='CHỈ SỐ ĐÔ LA DXY', nguon='Hà Nội Mới 14/11/2026', dong=[['103,41', 130, 'vang'], ['CAO NHẤT TỪ 4/2025', 56, 'trang']])),
  C('MỸ TĂNG, VIỆT NAM GIẢM', 'Trong khi Mỹ tăng lãi suất, Ngân hàng Nhà nước lại đang thanh tra việc giảm lãi suất trong tháng 11. Hai hướng ngược nhau, áp lực dồn vào tỷ giá.',
    the=dict(loai='lon', tieu='HAI HƯỚNG NGƯỢC NHAU', nguon='Người Quan Sát 13/11/2026', dong=[['MỸ TĂNG', 100, 'do'], ['VIỆT NAM MUỐN GIẢM', 60, 'trang']])),
  C('2022: VN-INDEX MẤT 32,8%', 'Lần trước, năm 2022, Fed tăng lãi suất 7 lần. VN-Index đi từ 1.498 điểm xuống 1.007 điểm, mất 32,8%, em tự tính.',
    the=dict(loai='cot', tieu='VN-INDEX CUỐI NĂM (ĐIỂM)', nguon='BSC 30/12/2022; em tự tính', hang=[['Cuối 2021', 1498], ['Cuối 2022', 1007]], noi=[1], dv='', max=1600)),
  C('LẦN NÀY KHÁC Ở ĐÂU', 'Nhưng năm 2022 lạm phát Mỹ trên 9%, Fed tăng hơn 4 điểm. Lần này thị trường tính tổng khoảng 1 điểm. Người đau nhất năm 2022 là người cầm cổ phiếu bằng tiền vay.',
    the=dict(loai='lon', tieu='LẦN NÀY THỊ TRƯỜNG TÍNH', nguon='CafeF 12/11/2026', dong=[['KHOẢNG 1 ĐIỂM', 104, 'vang'], ['NĂM 2022 LÀ HƠN 4 ĐIỂM', 54, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
    if 'câu cụt' not in q: print(q)
