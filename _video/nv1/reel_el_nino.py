# -*- coding: utf-8 -*-
# NV1 22/11/2026 – REEL câu hỏi lớn, cặp với CH3011EN (lô 20261122_0100). Nguồn: xem đầu _video/nv1/ql_el_nino.py.
#  Nhà Đầu Tư 9/11/2026 (El Nino 96% rất mạnh 11/2026–1/2027; mưa thiếu 20–40%); PetroTimes 7/11/2026 (nước về hồ khoảng 80%; nhu cầu điện 2027 +10%);
#  CafeF 31/10/2026 (giá điện bình quân −2% từ 1/11, 2.204 → 2.160 đ/kWh, phương án đến hết 31/3/2027); Báo Đầu tư 11/8/2023 (WB: mất điện 5–6/2023 thiệt hại 1,4 tỷ USD);
#  VietNamNet 22/6/2020 (2020 mặn gắt hơn, lúa thiệt hại 58.400 ha; 2016 405.000 ha bị ảnh hưởng; dự báo sớm, xuống giống sớm 10–20 ngày). Em tự tính: xưởng giả định 9 triệu tiền điện → bớt 180 nghìn; doanh thu 180 triệu × 10% = 18 triệu.
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261122_0100_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Thu nhập nhà anh chị đang dính mấy thứ trong ba thứ: điện ổn định, nước ngọt, mùa màng thuận? Không, một, hai hay ba?'
R = dict(key='RV2211EN', tieu_de='El Nino rất mạnh 96%: giá điện vừa giảm 2% nhưng mùa khô 2027 điện, nước, gạo nhà mình ra sao?',
 hook=['EL NINO RẤT MẠNH 96%', 'ĐIỆN, NƯỚC, GẠO NHÀ MÌNH???'], nhan='THỜI TIẾT · TÚI TIỀN',
 short_caption=('El Nino có khả năng 96% duy trì cường độ rất mạnh tới tháng 1/2027; kịch bản rủi ro rất cao: mưa thiếu 20–40% (Trung tâm Dự báo KTTV quốc gia, Bộ NN&MT – Nhà Đầu Tư 9/11/2026). '
                'Nước về hồ thủy điện khoảng 80% trung bình nhiều năm, nhu cầu điện 2027 dự báo +10% (Hội nghị Bộ Công Thương 7/11 – PetroTimes). Giá điện bình quân giảm 2% từ 1/11/2026 (CafeF 31/10). '
                'Mùa hè 2023 mất điện thiệt hại khoảng 1,4 tỷ USD (Ngân hàng Thế giới – Báo Đầu tư 11/8/2023). Hạn mặn 2020 gắt hơn 2016 nhưng lúa thiệt hại 58.400 ha so với 405.000 ha bị ảnh hưởng năm 2016 (VietNamNet 22/6/2020). '
                'Em tự tính cho xưởng giả định: bớt 180 nghìn tiền điện mỗi tháng, mất tới 10% doanh thu là 18 triệu. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH DÍNH MẤY THỨ?', loi=Q, loi_doc=lib.doc(Q), anh=['Hoa Binh Dam', 'Hanoi skyline night']),
 canh=[
  C('EL NINO 96% RẤT MẠNH', 'Trung tâm Dự báo khí tượng thủy văn quốc gia vừa cho biết El Nino có khả năng 96% duy trì cường độ rất mạnh tới tháng 1 năm sau. Kịch bản rủi ro rất cao là mưa thiếu từ 20 đến 40%.',
    the=dict(loai='lon', tieu='KHẢ NĂNG EL NINO RẤT MẠNH ĐẾN 1/2027', nguon='Nhà Đầu Tư 9/11/2026', dong=[['96%', 130, 'do'], ['MƯA CÓ THỂ THIẾU 20 – 40%', 56, 'trang']])),
  C('GIÁ ĐIỆN VỪA GIẢM 2%', 'Cùng lúc đó, giá điện bình quân vừa giảm 2% từ ngày 1 tháng 11. Nghe như tin tốt. Nhưng phương án giảm chỉ được yêu cầu đến hết tháng 3, trước cao điểm nắng nóng.',
    the=dict(loai='cot', tieu='GIÁ ĐIỆN BÌNH QUÂN (ĐỒNG/KWH)', nguon='CafeF 31/10/2026', hang=[['Từ 5/2025', 2204], ['Từ 1/11/2026', 2160]], noi=[1], dv='', max=2400)),
  C('NƯỚC VỀ HỒ CHỈ 80%', 'Chuyện đáng lo hơn là nước. Nước về các hồ thủy điện chỉ còn khoảng 80% trung bình nhiều năm, trong khi nhu cầu điện năm sau dự báo tăng khoảng 10%.',
    the=dict(loai='lon', tieu='NƯỚC VỀ HỒ THỦY ĐIỆN SO VỚI TRUNG BÌNH', nguon='Hội nghị Bộ Công Thương 7/11/2026', dong=[['80%', 130, 'do'], ['NHU CẦU ĐIỆN 2027 TĂNG 10%', 54, 'trang']])),
  C('HÈ 2023 MẤT 1,4 TỶ USD', 'Lần trước, mùa hè năm 2023, miền Bắc cắt điện luân phiên. Ngân hàng Thế giới ước tính thiệt hại khoảng 1 tỷ 400 triệu đô la.',
    the=dict(loai='lon', tieu='MẤT ĐIỆN THÁNG 5 VÀ 6 NĂM 2023', nguon='Ngân hàng Thế giới, Báo Đầu tư 11/8/2023', dong=[['1,4 TỶ USD', 118, 'do'], ['KHOẢNG 0,3% GDP', 56, 'trang']])),
  C('BỚT 180 NGHÌN, MẤT 18 TRIỆU', 'Với một xưởng may giả định trả 9 triệu tiền điện mỗi tháng, giảm 2% là bớt 180 nghìn. Nhưng nếu một tháng thiếu điện làm mất tới 10% doanh thu, xưởng mất 18 triệu, gấp 100 lần.',
    the=dict(loai='cot', tieu='XƯỞNG MAY GIẢ ĐỊNH (NGHÌN ĐỒNG)', nguon='Em tự tính', hang=[['Bớt tiền điện', 180], ['Mất 10% doanh thu', 18000]], noi=[1], dv='', max=20000)),
  C('MẶN GẮT HƠN, THIỆT HẠI ÍT HƠN', 'Nhưng chuẩn bị sớm thì khác. Năm 2020, miền Tây mặn còn gắt hơn năm 2016, vậy mà lúa thiệt hại 58 nghìn 400 héc ta, so với hơn 400 nghìn héc ta bị ảnh hưởng năm 2016. Lần đó có dự báo sớm và xuống giống sớm.',
    the=dict(loai='cot', tieu='LÚA MIỀN TÂY (NGHÌN HA)', nguon='VietNamNet 22/6/2020', hang=[['2016 bị ảnh hưởng', 405], ['2020 thiệt hại', 58.4]], noi=[1], dv='', max=450)),
  C('NHÀ MÌNH DÍNH MẤY THỨ?', 'Phép thử của em: đếm xem thu nhập nhà mình dựa vào mấy thứ do thời tiết quyết định. Từ 2 thứ trở lên, nên có quỹ dự phòng trước tháng 4.',
    the=dict(loai='lon', tieu='ĐIỆN ỔN ĐỊNH · NƯỚC NGỌT · MÙA MÀNG', nguon='Mốc em tự đặt, không phải chuẩn chung', dong=[['0 · 1 · 2 · 3', 110, 'vang'], ['TỪ 2 THỨ: QUỸ TRƯỚC THÁNG 4', 50, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    sys.path.insert(0, CW + '/_video'); import kiem_loi
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
    for c in R['canh']: print(c['loi_doc'][:260])
