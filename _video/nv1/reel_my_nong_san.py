# -*- coding: utf-8 -*-
# NV1 19/11/2026 – REEL câu hỏi lớn, cặp với CH2511MY (lô 20261119_0120). Nguồn: xem đầu _video/nv1/ql_my_nong_san.py.
#  Tuổi Trẻ 8/11/2026 (đoàn lớn nhất, 43 doanh nghiệp); Thuế & Hải quan Online 13/11/2026 (10T: xuất sang Mỹ 159,4 tỷ, nhập 19,3 tỷ; tự tính 8,26 lần);
#  Investing.com 27/8/2026 (thâm hụt Mỹ với VN nửa đầu 2026 114,03 tỷ, đứng đầu); Znews 2/8/2026 (61,8% thịt gà nhập từ Mỹ, chủ yếu đùi góc tư);
#  VnBusiness 9/9/2026 (giá nhập bình quân 26.500 đ/kg; giá gà hơi tháng 8 miền Nam: trắng 25.000, lông màu 46.000); VnExpress 11/11/2026 (bò Mỹ 8 tháng gấp 3).
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261119_0120_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Thu nhập nhà anh chị đi qua cửa nào: cửa bán hàng sang Mỹ, cửa đụng hàng Mỹ, hay không qua cửa nào?'
R = dict(key='RV1911MY', tieu_de='Vì sao Mỹ cử đoàn nông nghiệp lớn nhất lịch sử sang Việt Nam? Bán sang Mỹ 159,4 tỷ USD, mua lại 19,3 tỷ',
 hook=['MỸ CỬ ĐOÀN NÔNG NGHIỆP LỚN NHẤT', 'SANG VIỆT NAM ĐỂ LÀM GÌ???'], nhan='VIỆT – MỸ · HỎI THẬT',
 short_caption=('Đoàn xúc tiến nông nghiệp lớn nhất từ trước đến nay của Mỹ, 43 doanh nghiệp, TP.HCM 9–12/11/2026 (Tuổi Trẻ 8/11/2026). 10 tháng 2026: xuất khẩu sang Mỹ 159,4 tỷ USD, nhập từ Mỹ 19,3 tỷ '
                '(Thuế & Hải quan Online 13/11/2026; em tự tính: hơn 8 lần). Thâm hụt hàng hoá của Mỹ với Việt Nam nửa đầu 2026: 114,03 tỷ USD, lớn nhất (Cục Thống kê Mỹ, Investing.com 27/8/2026). '
                '61,8% thịt gà nhập khẩu đến từ Mỹ, chủ yếu đùi góc tư (Hiệp hội Gia cầm, Znews 2/8/2026); giá nhập bình quân khoảng 26.500 đồng/kg; giá gà hơi tháng 8 miền Nam: gà trắng 25.000, lông màu 46.000 (VnBusiness 9/9/2026). '
                'Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH Ở CỬA NÀO?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City skyline night', 'Bitexco Financial Tower']),
 canh=[
  C('ĐOÀN LỚN NHẤT LỊCH SỬ', 'Từ ngày 9 đến 12/11, Bộ Nông nghiệp Mỹ vừa đưa 43 doanh nghiệp sang Thành phố Hồ Chí Minh. Đây là đoàn xúc tiến nông nghiệp lớn nhất từ trước đến nay. Đoàn này sang để bán hàng.',
    the=dict(loai='lon', tieu='ĐOÀN XÚC TIẾN NÔNG NGHIỆP MỸ', nguon='Tuổi Trẻ 8/11/2026', dong=[['43 DOANH NGHIỆP', 112, 'vang'], ['TP.HCM, 9 ĐẾN 12/11', 56, 'trang']])),
  C('BÁN 159,4, MUA 19,3', 'Lý do nằm ở sổ sách. Mười tháng năm nay, Việt Nam bán sang Mỹ 159,4 tỷ đô la, nhưng chỉ mua lại 19,3 tỷ. Em tự tính: bán hơn 8 đồng mới mua về 1 đồng.',
    the=dict(loai='cot', tieu='VIỆT NAM VÀ MỸ, 10 THÁNG 2026 (TỶ USD)', nguon='Thuế & Hải quan Online 13/11/2026', hang=[['Bán sang Mỹ', 159.4], ['Mua từ Mỹ', 19.3]], noi=[0], dv='', max=170)),
  C('VƯỢT CẢ TRUNG QUỐC', 'Theo số của chính nước Mỹ, nửa đầu năm nay Mỹ thâm hụt với Việt Nam hơn 114 tỷ đô la. Việt Nam đứng đầu danh sách, vượt cả Trung Quốc.',
    the=dict(loai='lon', tieu='MỸ THÂM HỤT HÀNG HOÁ, NỬA ĐẦU 2026', nguon='Cục Thống kê Mỹ, Investing.com 27/8/2026', dong=[['114 TỶ USD', 120, 'do'], ['LỚN NHẤT, VƯỢT TRUNG QUỐC', 52, 'trang']])),
  C('6 PHẦN 10 GÀ NHẬP TỪ MỸ', 'Muốn cân bằng, Việt Nam phải mua thêm hàng Mỹ. Trong thịt gà nhập khẩu, khoảng 62% đã đến từ Mỹ, chủ yếu là đùi gà góc tư đông lạnh.',
    the=dict(loai='lon', tieu='THỊT GÀ NHẬP KHẨU, NỬA ĐẦU 2026', nguon='Hiệp hội Gia cầm Việt Nam, Znews 2/8/2026', dong=[['61,8% TỪ MỸ', 116, 'do'], ['CHỦ YẾU ĐÙI GÓC TƯ', 56, 'trang']])),
  C('26.500 ĐỒNG MỘT KÝ', 'Giá nhập bình quân của thịt gia cầm chỉ khoảng 26.500 đồng một ký. Người nuôi gà trắng công nghiệp trong nước đang chịu áp lực trực tiếp.',
    the=dict(loai='lon', tieu='GIÁ NHẬP BÌNH QUÂN, 7 THÁNG 2026', nguon='Cục Hải quan, VnBusiness 9/9/2026', dong=[['26.500 Đ/KG', 116, 'do'], ['THỊT GIA CẦM NHẬP KHẨU', 54, 'trang']])),
  C('NGƯỜI ĐI CHỢ CÓ LỢI', 'Nhưng người đi chợ thì có lợi. Thịt bò Mỹ nhập về tám tháng đầu năm gấp ba lần cùng kỳ. Táo Mỹ bán lẻ rẻ hơn năm ngoái khoảng 5 đến 10%.',
    the=dict(loai='lon', tieu='THỊT BÒ MỸ NHẬP, 8 THÁNG 2026', nguon='VnExpress 11/11/2026', dong=[['GẤP 3 LẦN', 120, 'vang'], ['SO VỚI CÙNG KỲ', 58, 'trang']])),
  C('GÀ TA KHÔNG ĐỤNG HÀNG', 'Và không phải cả ngành đều thua. Hồi tháng tám, gà lông màu miền Nam được khoảng 46.000 đồng một ký, gần gấp đôi gà trắng. Gà nguyên con đông lạnh chỉ chiếm khoảng 2% thịt gà nhập.',
    the=dict(loai='cot', tieu='GIÁ GÀ HƠI MIỀN NAM, THÁNG 8 (NGHÌN Đ/KG)', nguon='Bộ NN&MT, VnBusiness 9/9/2026', hang=[['Gà trắng', 25], ['Gà lông màu', 46]], noi=[1], dv='', max=50)),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.path.insert(0, CW + '/_video'); import kiem_loi
print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
for c in R['canh']: print(c['loi_doc'][:220])
