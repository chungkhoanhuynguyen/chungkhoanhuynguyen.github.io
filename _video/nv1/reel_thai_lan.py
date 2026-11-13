# -*- coding: utf-8 -*-
# NV1 14/11/2026 – REEL "câu hỏi lớn" cặp với CH1811TL: Việt Nam có thành Thái Lan thứ hai? (nguồn như nv1/ql_thai_lan.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261114_0040_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Theo anh chị, Việt Nam sẽ thành Hàn Quốc hay thành Thái Lan thứ hai? Và khoản trả nợ mỗi tháng nhà mình chiếm bao nhiêu phần thu nhập?'
R = dict(key='RV1411TL', tieu_de='Thái Lan từng tăng 13,3% một năm, giờ kẹt ở 2%: Việt Nam có thành Thái Lan thứ hai?',
 hook=['THÁI LAN TỪNG TĂNG 13,3%', 'VIỆT NAM CÓ ĐI VẾT XE ĐỔ???'], nhan='VĨ MÔ · HỎI THẬT',
 short_caption=('Năm 1988 Thái Lan tăng trưởng 13,3%. Nay IMF dự báo Thái Lan chỉ tăng 2,1% năm 2026, nợ hộ gia đình bằng 86,7% GDP (SCB EIC), hơn 20% dân số từ 60 tuổi. '
                'Việt Nam được dự báo tăng 8,4% và sẽ thành dân số già năm 2034 (Cục Thống kê – UNFPA). Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='HÀN QUỐC HAY THÁI LAN?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City skyline night', 'Hanoi skyline night']),
 canh=[
  C('THÁI LAN TỪNG TĂNG 13,3%', 'Tháng mười vừa rồi, IMF dự báo Việt Nam tăng 8,4%, Thái Lan chỉ 2,1%. Nhưng năm 1988, chính Thái Lan từng tăng 13,3%, nhanh hơn cả mình bây giờ.',
    the=dict(loai='lon', tieu='GDP THÁI LAN NĂM 1988', nguon='Tiền Phong, số Ngân hàng Thế giới', dong=[['+13,3%', 140, 'vang'], ['NHANH HƠN VIỆT NAM BÂY GIỜ', 54, 'trang']])),
  C('GIỜ CHỈ CÒN 2,1%', 'Gần 40 năm sau, Thái Lan thuộc nhóm tăng chậm nhất Đông Nam Á. Việt Nam 8,4%, Malaysia 5,2%, Thái Lan 2,1%.',
    the=dict(loai='cot', tieu='DỰ BÁO TĂNG TRƯỞNG 2026 (%)', nguon='IMF, Triển vọng kinh tế thế giới 10/2026', hang=[['Việt Nam', 8.4], ['Malaysia', 5.2], ['Thái Lan', 2.1]], noi=[2], dv='%', max=10)),
  C('CÚ SẬP 1997', 'Ngày 2 tháng 7 năm 1997, Thái Lan thả nổi đồng baht. Baht mất khoảng một nửa giá trị, kinh tế năm 1998 giảm 7,6%.',
    the=dict(loai='lon', tieu='SAU NGÀY 2/7/1997', nguon='Ngân hàng Trung ương Úc 1998, Tiền Phong', dong=[['BAHT MẤT MỘT NỬA', 84, 'do'], ['GDP 1998 GIẢM 7,6%', 62, 'trang']])),
  C('NỢ BẰNG 86,7% GDP', 'Cuối năm 2025, nợ của các hộ gia đình Thái bằng 86,7% GDP, phần tăng thêm chủ yếu là vay để tiêu dùng.',
    the=dict(loai='lon', tieu='NỢ HỘ GIA ĐÌNH THÁI LAN', nguon='SCB EIC, The Nation 15/4/2026', dong=[['86,7% GDP', 130, 'do'], ['CHỦ YẾU VAY ĐỂ TIÊU DÙNG', 54, 'trang']])),
  C('GIÀ TRƯỚC KHI GIÀU', 'Hơn 20% dân số Thái đã từ 60 tuổi. Thu nhập mỗi người khoảng 7.690 đô la, vẫn chưa tới ngưỡng nước giàu 14.375 đô la.',
    the=dict(loai='cot', tieu='THU NHẬP MỖI NGƯỜI 2025 (USD)', nguon='Ngân hàng Thế giới, Tiền Phong 9/7/2026', hang=[['Việt Nam', 4970], ['Thái Lan', 7690], ['Ngưỡng giàu', 14375]], noi=[1], dv='', max=15000)),
  C('VIỆT NAM CÒN 10 NĂM', 'Còn Việt Nam sẽ thành nước dân số già năm 2034, dân số vàng kết thúc khoảng năm 2036. Mình còn khoảng 10 năm.',
    the=dict(loai='lon', tieu='ĐỒNG HỒ DÂN SỐ VIỆT NAM', nguon='Cục Thống kê – UNFPA, dự báo 2024–2074', dong=[['2034: DÂN SỐ GIÀ', 80, 'vang'], ['2036: HẾT DÂN SỐ VÀNG', 62, 'trang']])),
  C('CẦN TĂNG 5,5% MỖI NĂM', 'Em tự tính: muốn chạm ngưỡng nước giàu vào năm 2045, thu nhập tính bằng đô la phải tăng khoảng 5,5% mỗi năm, đều đặn suốt 20 năm.',
    the=dict(loai='lon', tieu='MUỐN GIÀU KỊP NĂM 2045', nguon='Em tự tính từ 4.970 lên 14.375 USD', dong=[['5,5% MỖI NĂM', 110, 'vang'], ['ĐỀU ĐẶN SUỐT 20 NĂM', 58, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
    if 'câu cụt' not in q: print(q)
