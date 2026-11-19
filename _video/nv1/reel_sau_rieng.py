# -*- coding: utf-8 -*-
# NV1 20/11/2026 – REEL câu hỏi lớn, cặp với CH2911SR (lô 20261120_0200). Nguồn: xem đầu _video/nv1/ql_sau_rieng.py.
#  Vietnambiz 3/11 + 5/11/2026 (9T 3,45 tỷ USD; gần 96% sang TQ; tháng 9 729 triệu, −25% cùng kỳ); Trung tâm WTO 15/10/2026 (quy hoạch 100–110 nghìn ha, thực tế ~200.000 ha);
#  Doanh Nhân VN 9/11/2026 (Tây Nguyên RI6 đẹp 52–54 nghìn, xô 25–30 nghìn); Vietnambiz 25/9/2026 (Philippines 15.000 ha); WiData (giá tiêu xuất khẩu 12/2016 7,63 → 4/2020 2,01 USD/kg).
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261120_0200_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Nếu nhà anh chị trồng sầu riêng, giá hàng xô ở vườn hôm nay là bao nhiêu, và năm nay có vay trồng thêm không?'
R = dict(key='RV2011SR', tieu_de='Sầu riêng xuất khẩu kỷ lục 3,45 tỷ USD mà nhà vườn vẫn lo? 96% bán cho một khách, có thành hồ tiêu?',
 hook=['SẦU RIÊNG XUẤT KHẨU KỶ LỤC', 'SAO NHÀ VƯỜN VẪN LO???'], nhan='SẦU RIÊNG · HỎI THẬT',
 short_caption=('Xuất khẩu sầu riêng 9 tháng 2026 đạt 3,45 tỷ USD, gần 96% sang Trung Quốc; tháng 9 khoảng 729 triệu USD, giảm 25% so cùng kỳ (Cục Hải quan, Vietnambiz 3/11 và 5/11/2026). '
                'Diện tích khoảng 200.000 ha, quy hoạch đã nâng 100.000–110.000 ha (Trung tâm WTO, VCCI 15/10/2026). Tây Nguyên 9/11: RI6 đẹp lựa 52–54 nghìn, hàng xô 25–30 nghìn đồng/kg (Doanh Nhân Việt Nam). '
                'Philippines khoảng 15.000 ha (Bộ Công Thương, Vietnambiz 25/9/2026). Giá xuất khẩu bình quân hạt tiêu 12/2016 7,63 USD/kg, 4/2020 2,01 USD/kg (Cục Hải quan, WiData; em tự tính −73,6%). '
                'Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='GIÁ HÀNG XÔ HÔM NAY?', loi=Q, loi_doc=lib.doc(Q), anh=['Durian fruit', 'Ho Chi Minh City skyline night']),
 canh=[
  C('3,45 TỶ USD, 9 THÁNG', 'Sầu riêng vừa lập kỷ lục xuất khẩu: chín tháng năm nay đạt gần 3,5 tỷ đô la. Nhưng gần 96% số tiền đó đến từ một khách hàng là Trung Quốc.',
    the=dict(loai='lon', tieu='XUẤT KHẨU SẦU RIÊNG, 9 THÁNG 2026', nguon='Cục Hải quan, Vietnambiz 5/11/2026', dong=[['3,45 TỶ USD', 116, 'vang'], ['GẦN 96% SANG TRUNG QUỐC', 54, 'trang']])),
  C('THÁNG 9 ĐÃ GIẢM 25%', 'Và tháng gần nhất đã chững lại. Riêng tháng chín, xuất khẩu sầu riêng khoảng 729 triệu đô la, thấp hơn cùng kỳ năm ngoái 25%.',
    the=dict(loai='lon', tieu='XUẤT KHẨU SẦU RIÊNG THÁNG 9/2026', nguon='Cục Hải quan, Vietnambiz 3/11/2026', dong=[['729 TRIỆU USD', 112, 'do'], ['THẤP HƠN CÙNG KỲ 25%', 56, 'trang']])),
  C('200.000 HA', 'Cả nước hiện có khoảng 200 nghìn héc ta sầu riêng. Mức quy hoạch đến năm 2030, dù đã nâng, chỉ khoảng 100 đến 110 nghìn héc ta.',
    the=dict(loai='cot', tieu='DIỆN TÍCH SẦU RIÊNG (NGHÌN HA)', nguon='Trung tâm WTO, VCCI 15/10/2026', hang=[['Quy hoạch 2030', 110], ['Thực tế 2026', 200]], noi=[1], dv='', max=220)),
  C('ĐẸP 54, XÔ 25 NGHÌN', 'Ở Tây Nguyên đầu tháng mười một, sầu riêng RI sáu đẹp lựa khoảng 52 đến 54 nghìn đồng một ký. Hàng xô chỉ 25 đến 30 nghìn.',
    the=dict(loai='cot', tieu='GIÁ RI6 TÂY NGUYÊN 9/11 (NGHÌN Đ/KG)', nguon='Doanh Nhân Việt Nam 9/11/2026', hang=[['Đẹp lựa', 54], ['Hàng xô', 25]], noi=[1], dv='', max=60)),
  C('ĐỐI THỦ TRỒNG THÊM', 'Trong khi đó Philippines đang có khoảng 15 nghìn héc ta sầu riêng. Malaysia thử chở sầu riêng sang Trung Quốc bằng đường biển. Người mua đang có thêm lựa chọn.',
    the=dict(loai='lon', tieu='PHILIPPINES TRỒNG SẦU RIÊNG', nguon='Bộ Công Thương, Vietnambiz 25/9/2026', dong=[['15.000 HA', 116, 'do'], ['DỰ KIẾN 150 NGHÌN TẤN', 54, 'trang']])),
  C('LẦN TRƯỚC: HỒ TIÊU', 'Lần trước là cây hồ tiêu. Giá xuất khẩu bình quân hạt tiêu từ hơn 7,6 đô la một ký cuối năm 2016 rơi còn khoảng 2 đô la vào tháng tư năm 2020. Em tự tính: mất gần 74%.',
    the=dict(loai='cot', tieu='GIÁ XUẤT KHẨU HẠT TIÊU (USD/KG)', nguon='Cục Hải quan, WiData', hang=[['12/2016', 7.63], ['4/2020', 2.01]], noi=[1], dv='', max=8)),
  C('GIÁ THÌ KHÔNG QUYẾT ĐƯỢC', 'Nhà vườn không quyết được giá. Nhưng nhà vườn quyết được ba việc: trái có đạt chuẩn không, có vay trồng thêm không, và có cửa bán thứ hai chưa.',
    the=dict(loai='lon', tieu='BA VIỆC NHÀ VƯỜN QUYẾT ĐƯỢC', nguon='Huy Nguyễn tổng hợp', dong=[['CHUẨN · NỢ · CỬA RA', 84, 'vang'], ['GIÁ THÌ KHÔNG QUYẾT ĐƯỢC', 52, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.path.insert(0, CW + '/_video'); import kiem_loi
print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
for c in R['canh']: print(c['loi_doc'][:240])
