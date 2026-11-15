# -*- coding: utf-8 -*-
# NV1 16/11/2026 – REEL "câu hỏi lớn" cặp với CH2011VON: cần 38,5 triệu tỷ cho 5 năm – tiền ở đâu ra? (nguồn như nv1/ql_von_385.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261116_0040_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Lãi thật của tiền nhà anh chị đang âm, đang hòa, hay đang được trả công? Anh chị đang để tiền ở kênh nào?'
R = dict(key='RV1611VON', tieu_de='Cần 38,5 triệu tỷ cho 5 năm: hơn nửa đi qua ngân hàng, mà lãi thật sổ tiết kiệm chỉ 0,3%',
 hook=['CẦN 38,5 TRIỆU TỶ', 'TIỀN Ở ĐÂU RA???'], nhan='VĨ MÔ · HỎI THẬT',
 short_caption=('Nhu cầu vốn đầu tư 2026–2030 khoảng 38,5 triệu tỷ đồng (VnBusiness 22/10/2026; chất vấn tại Quốc hội 12/11/2026). Đầu tư công trung hạn 8,22 triệu tỷ, khoảng 1/5. '
                'Hơn 50% vốn nền kinh tế đi qua ngân hàng; lãi gửi 12 tháng 5,4%, CPI 10/2026 +5,09% (WiData). Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='LÃI THẬT NHÀ MÌNH?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City skyline night', 'Hanoi skyline night']),
 canh=[
  C('CẦN 38,5 TRIỆU TỶ', 'Tại phiên chất vấn Thủ tướng hôm 12 tháng 11, Quốc hội vừa nêu một con số lớn. Việt Nam cần khoảng 38,5 triệu tỷ đồng vốn đầu tư từ năm 2026 đến năm 2030 để tăng trưởng hai con số.',
    the=dict(loai='lon', tieu='VỐN CẦN CHO 2026 ĐẾN 2030', nguon='VnBusiness 22/10, VietnamFinance 12/11/2026', dong=[['38,5', 140, 'do'], ['TRIỆU TỶ ĐỒNG', 60, 'trang']])),
  C('MỖI NĂM 55% GDP', 'Chia đều ra, mỗi năm khoảng 7,7 triệu tỷ, bằng 55% giá trị cả nền kinh tế làm ra trong một năm. Em tự tính.',
    the=dict(loai='lon', tieu='MỖI NĂM CẦN KHOẢNG', nguon='Em tự tính, GDP 4 quý tới quý 3/2026', dong=[['7,7 TRIỆU TỶ', 104, 'vang'], ['BẰNG 55% GDP', 60, 'trang']])),
  C('ĐẦU TƯ CÔNG CHỈ 1/5', 'Đầu tư công đã duyệt khoảng 8,22 triệu tỷ, chỉ bằng một phần năm. Gần 30 triệu tỷ còn lại phải huy động từ nơi khác.',
    the=dict(loai='cot', tieu='VỐN 2026 ĐẾN 2030 (TRIỆU TỶ)', nguon='VietnamFinance 12/11/2026', hang=[['Tổng nhu cầu', 38.5], ['Đầu tư công', 8.22]], noi=[1], dv='', max=40)),
  C('HƠN 50% QUA NGÂN HÀNG', 'Mà hơn một nửa vốn của nền kinh tế đang đi qua ngân hàng. Tức là phần lớn đến từ chính sổ tiết kiệm của người dân, được cho vay lại.',
    the=dict(loai='cot', tieu='NGUỒN VỐN NỀN KINH TẾ (%)', nguon='TS Cấn Văn Lực, VnBusiness 22/10/2026', hang=[['Ngân hàng', 50], ['Cổ phiếu, trái phiếu', 15]], noi=[0], dv='%', max=60)),
  C('80% LÀ TIỀN GỬI NGẮN HẠN', 'Khoảng 80% tiền gửi có kỳ hạn dưới 12 tháng, nhưng lại đang nuôi những dự án cần vốn mười, hai mươi năm.',
    the=dict(loai='lon', tieu='TIỀN GỬI NGÂN HÀNG', nguon='VnBusiness 22/10/2026', dong=[['80%', 140, 'do'], ['KỲ HẠN DƯỚI 12 THÁNG', 56, 'trang']])),
  C('LÃI THẬT CHỈ 0,3%', 'Lãi gửi 12 tháng ở ngân hàng lớn là 5,4%, còn giá cả tháng 10 tăng 5,09%. Người gửi tiền góp vốn cho cả nước, nhưng lãi thật chỉ còn khoảng 0,3%.',
    the=dict(loai='cot', tieu='LÃI GỬI VÀ GIÁ CẢ (%)', nguon='WiData: lãi 12 tháng 13/11, CPI 10/2026', hang=[['Lãi gửi 12 tháng', 5.4], ['Giá cả tăng', 5.09]], noi=[1], dv='%', max=6)),
  C('TÍN DỤNG 146% GDP', 'Tổng tín dụng đã bằng khoảng 146% GDP, em tự tính, từ 134% cuối năm 2024. Năm 2007 tín dụng tăng 53%, một năm sau lạm phát gần 20%.',
    the=dict(loai='lon', tieu='TÍN DỤNG SO VỚI GDP', nguon='Em tự tính từ WiData; Vietnamnet 6/2025', dong=[['146%', 140, 'do'], ['CUỐI 2024 LÀ 134%', 56, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
    if 'câu cụt' not in q: print(q)
