# -*- coding: utf-8 -*-
# NV1 15/11/2026 – REEL "câu hỏi lớn" cặp với CH1911ND: 87% tài sản ở nhà đất – có đi vết xe Trung Quốc? (nguồn như nv1/ql_nha_dat.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261115_0040_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Nhà anh chị đang để bao nhiêu phần tài sản trong nhà đất? Và anh chị nghĩ nhà đất Việt Nam có đi vết xe của Trung Quốc không?'
R = dict(key='RV1511ND', tieu_de='87% tài sản người Việt nằm ở nhà đất: Trung Quốc 70% mà doanh số bán nhà đã mất 60%',
 hook=['87% TÀI SẢN LÀ NHÀ ĐẤT', 'CÓ ĐI VẾT XE TRUNG QUỐC???'], nhan='VĨ MÔ · HỎI THẬT',
 short_caption=('Khoảng 87% tài sản gia đình Việt nằm ở bất động sản (Vietnambiz 13/11/2026). Trung Quốc khoảng 70%; doanh số bán nhà 9 tháng 2026 chỉ còn 40% so với cùng kỳ 2021 (Cục Thống kê Trung Quốc). '
                'Tín dụng bất động sản Việt Nam 5,21 triệu tỷ, vay kinh doanh nhà đất +19,59% trong 8 tháng (NHNN). Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH BAO NHIÊU %?', loi=Q, loi_doc=lib.doc(Q), anh=['Hanoi apartment buildings', 'Hanoi skyline night']),
 canh=[
  C('87% LÀ NHÀ ĐẤT', 'Báo Vietnambiz vừa đưa tin một khảo sát tại diễn đàn đầu tư hôm 13 tháng 11. Khoảng 87% tài sản của các gia đình Việt Nam đang nằm trong nhà đất.',
    the=dict(loai='lon', tieu='TÀI SẢN GIA ĐÌNH VIỆT', nguon='Vietnambiz 13/11/2026, khảo sát VIG', dong=[['87%', 140, 'do'], ['NẰM Ở NHÀ ĐẤT', 60, 'trang']])),
  C('TRUNG QUỐC KHOẢNG 70%', 'Người Trung Quốc từng nổi tiếng mê nhà đất nhất thế giới, khoảng 70% tài sản của gia đình thành thị là nhà ở. Người Việt còn dồn nhiều hơn họ. Vậy bên đó đã xảy ra chuyện gì?',
    the=dict(loai='cot', tieu='PHẦN TÀI SẢN Ở NHÀ ĐẤT (%)', nguon='Vietnambiz 11/2026, The Real Deal 7/2026', hang=[['Việt Nam', 87], ['Trung Quốc', 70]], noi=[0], dv='%', max=100)),
  C('DOANH SỐ MẤT 60%', 'Năm 2021, Trung Quốc bán nhà đất kỷ lục. Chín tháng đầu năm nay, doanh số bán nhà chỉ còn khoảng 40% so với cùng kỳ năm 2021, tức là mất 60%.',
    the=dict(loai='lon', tieu='DOANH SỐ BÁN NHÀ TRUNG QUỐC', nguon='Cục Thống kê Trung Quốc, qua WiData', dong=[['MẤT 60%', 130, 'do'], ['9 THÁNG 2026 SO VỚI 2021', 54, 'trang']])),
  C('GIÁ GIẢM 20 ĐẾN 40%', 'Giá nhà giảm 20 đến 40% từ đỉnh, tuỳ cách đo. Evergrande, tập đoàn lớn nhất nhì ngành, bị toà ra lệnh thanh lý với khoảng 300 tỷ đô la nợ.',
    the=dict(loai='lon', tieu='GIÁ NHÀ TRUNG QUỐC TỪ ĐỈNH 2021', nguon='Người Quan Sát 12/2025, The Real Deal 7/2026', dong=[['GIẢM 20 ĐẾN 40%', 92, 'do'], ['EVERGRANDE NỢ 300 TỶ USD', 54, 'trang']])),
  C('VAY KINH DOANH NHÀ +19,59%', 'Còn Việt Nam, tới cuối tháng 8, vay để kinh doanh nhà đất tăng 19,59%, còn vay mua nhà để ở chỉ tăng 1,02%.',
    the=dict(loai='cot', tieu='TÍN DỤNG BẤT ĐỘNG SẢN, 8 THÁNG 2026 (%)', nguon='Ngân hàng Nhà nước, 31/8/2026', hang=[['Kinh doanh nhà đất', 19.59], ['Mua nhà để ở', 1.02]], noi=[0], dv='%', max=25)),
  C('CĂN 6 TỶ = 27 NĂM LƯƠNG', 'Thu nhập bình quân một người lao động khoảng 9,2 triệu mỗi tháng. Em tự tính, một căn hộ 6 tỷ ở Hà Nội bằng khoảng 27 năm lương của cả hai vợ chồng, nếu không tiêu một đồng nào.',
    the=dict(loai='lon', tieu='CĂN HỘ 6 TỶ Ở HÀ NỘI BẰNG', nguon='Em tự tính, thu nhập lao động quý 3/2026', dong=[['27 NĂM', 130, 'vang'], ['LƯƠNG HAI VỢ CHỒNG', 58, 'trang']])),
  C('GIAO DỊCH CHẬM LẠI', 'Quý 3, cả nước có khoảng 92 nghìn giao dịch nhà đất, chỉ bằng 92% quý trước. Chưa phải cú sập như Trung Quốc, nhưng thị trường đã chậm lại.',
    the=dict(loai='lon', tieu='GIAO DỊCH NHÀ ĐẤT QUÝ 3/2026', nguon='Bộ Xây dựng, VietnamFinance 13/10/2026', dong=[['92%', 130, 'vang'], ['SO VỚI QUÝ TRƯỚC', 58, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
sys.path.insert(0, CW + '/_video'); import kiem_loi
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
    if 'câu cụt' not in q: print(q)
