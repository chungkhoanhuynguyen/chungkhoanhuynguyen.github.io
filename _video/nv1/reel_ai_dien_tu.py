# -*- coding: utf-8 -*-
# NV1 22/11/2026 – REEL câu hỏi lớn, cặp với CH0212AI (lô 20261122_0200). Nguồn: xem đầu _video/nv1/ql_ai_dien_tu.py.
#  Nhà Đầu Tư 12/11/2026 (phiên 5/11 Nasdaq 100 −6,4%, xóa ~2.500 tỷ USD); Doanh Nhân VN 18/11/2026 (hãng chip AI lớn nhất lãi quý 65 tỷ USD); Nhà Đầu Tư 13/11 (cổ phiếu giảm ~1/3 từ đỉnh đầu tháng 10);
#  WiData hải quan (điện tử 10 tháng: 2023 46,5; 2026 149,4 tỷ USD; điện thoại 2022 58,0 → 2023 52,4); VCCI/TC Kinh tế – Tài chính 30/10/2026 (đến 15/10: xuất 135,31, nhập 201,12 tỷ USD). Giả định nhà anh Tuấn: 14/30 triệu = 47%.
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261122_0200_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Thu nhập nhà anh chị đang dựa vào một ngành bao nhiêu phần trăm: dưới 20, từ 20 đến 50, hay trên 50?'
R = dict(key='RV2211AI', tieu_de='Chứng khoán Mỹ bốc hơi 2.500 tỷ USD vì sợ AI – Việt Nam xuất 149 tỷ USD điện tử: tiền tăng ca của ai lung lay?',
 hook=['MỸ BỐC HƠI 2.500 TỶ USD', 'TIỀN TĂNG CA RA SAO???'], nhan='AI · VIỆC LÀM',
 short_caption=('Phiên 5/11, nhóm Nasdaq 100 giảm 6,4%, xóa khoảng 2.500 tỷ USD vốn hóa vì lo bong bóng AI (Nhà Đầu Tư 12/11/2026). Hãng chip AI lớn nhất lãi quý 65 tỷ USD, cao nhất từ trước đến nay (Doanh Nhân Việt Nam 18/11), trong khi cổ phiếu đã giảm khoảng 1/3 từ đỉnh đầu tháng 10 (Nhà Đầu Tư 13/11). '
                'Việt Nam xuất khẩu máy vi tính, điện tử, linh kiện 10 tháng 149,4 tỷ USD, tăng 71%, gấp 3,2 lần 2023 (hải quan qua WiData). Đến 15/10 nhóm này xuất 135,31 tỷ, nhập 201,12 tỷ USD (VCCI 30/10). Năm 2023 xuất khẩu điện thoại giảm 9,7%. '
                'Thu nhập nhà anh Tuấn là giả định. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='DỰA VÀO 1 NGÀNH BAO NHIÊU %?', loi=Q, loi_doc=lib.doc(Q), anh=['Container ship', 'Hanoi skyline night']),
 canh=[
  C('BỐC HƠI 2.500 TỶ USD', 'Phiên ngày 5 tháng 11, nhóm 100 cổ phiếu công nghệ lớn ở Mỹ mất khoảng 2 nghìn 500 tỷ đô la vốn hóa chỉ trong một ngày, vì lo bong bóng AI.',
    the=dict(loai='lon', tieu='NASDAQ 100, PHIÊN 5/11/2026', nguon='Nhà Đầu Tư 12/11/2026', dong=[['2.500 TỶ USD', 112, 'do'], ['GIẢM 6,4% TRONG MỘT PHIÊN', 56, 'trang']])),
  C('LÃI KỶ LỤC 65 TỶ USD', 'Lạ ở chỗ, hãng chip AI lớn nhất vừa báo một quý lãi 65 tỷ đô la, cao nhất từ trước đến nay. Vậy mà trước đó, cổ phiếu của hãng đã giảm khoảng 33% từ đỉnh.',
    the=dict(loai='lon', tieu='LỢI NHUẬN MỘT QUÝ, HÃNG CHIP AI LỚN NHẤT', nguon='Doanh Nhân Việt Nam 18/11/2026', dong=[['65 TỶ USD', 124, 'vang'], ['CỔ PHIẾU ĐÃ GIẢM KHOẢNG 1/3', 54, 'trang']])),
  C('VIỆT NAM XUẤT 149 TỶ USD', 'Còn Việt Nam thì đang hưởng cơn sốt. Mười tháng năm nay, hàng máy tính, điện tử, linh kiện xuất khẩu gần 150 tỷ đô la, gấp hơn 3 lần cùng kỳ năm 2023.',
    the=dict(loai='cot', tieu='XUẤT KHẨU ĐIỆN TỬ 10 THÁNG (TỶ USD)', nguon='Số liệu hải quan qua WiData', hang=[['2023', 46.5], ['2025', 87.4], ['2026', 149.4]], noi=[2], dv='', max=160)),
  C('XUẤT 135 TỶ, NHẬP 201 TỶ', 'Nhưng tính đến giữa tháng 10, cùng nhóm hàng đó Việt Nam nhập về hơn 201 tỷ đô la, nhiều hơn phần xuất đi. Giá trị ở lại trong nước chưa lớn như con số xuất khẩu.',
    the=dict(loai='cot', tieu='NHÓM ĐIỆN TỬ ĐẾN 15/10/2026 (TỶ USD)', nguon='VCCI, Kinh tế – Tài chính 30/10/2026', hang=[['Xuất khẩu', 135.3], ['Nhập khẩu', 201.1]], noi=[1], dv='', max=220)),
  C('LẦN TRƯỚC: ĐIỆN THOẠI GIẢM', 'Lần trước, sau cơn sốt thời Covid, xuất khẩu điện thoại năm 2023 giảm gần 10%. Với người làm công, theo em, phần bị cắt đầu tiên thường là tăng ca.',
    the=dict(loai='cot', tieu='XUẤT KHẨU ĐIỆN THOẠI (TỶ USD)', nguon='Số liệu hải quan qua WiData', hang=[['2022', 58.0], ['2023', 52.4]], noi=[1], dv='', max=65)),
  C('GẦN NỬA THU NHẬP NHÀ', 'Một gia đình giả định: chồng tăng ca 4 triệu, vợ bán cơm cho công nhân lãi 10 triệu, trên tổng 30 triệu. Gần một nửa thu nhập dựa vào đơn hàng điện tử.',
    the=dict(loai='lon', tieu='NHÀ ANH TUẤN (GIẢ ĐỊNH)', nguon='Em tự tính: 14 / 30 triệu', dong=[['47%', 130, 'do'], ['DỰA VÀO MỘT NGÀNH', 56, 'trang']])),
  C('SỐNG BẰNG LƯƠNG CỨNG', 'Phép thử của em: thu nhập dựa vào một ngành trên 50% thì nên có quỹ dự phòng trước. Theo em, tiền tăng ca không nên dùng để trả góp.',
    the=dict(loai='lon', tieu='PHÉP THỬ: BAO NHIÊU % DỰA VÀO MỘT NGÀNH', nguon='Mốc em tự đặt, không phải chuẩn chung', dong=[['20% · 50%', 110, 'vang'], ['TRÊN 50%: QUỸ DỰ PHÒNG TRƯỚC', 50, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    sys.path.insert(0, CW + '/_video'); import kiem_loi
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
    for c in R['canh']: print(c['loi_doc'][:260])
