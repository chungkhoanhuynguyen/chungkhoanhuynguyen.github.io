# -*- coding: utf-8 -*-
# NV1 21/11/2026 – REEL câu hỏi lớn, cặp với CH2611HT (lô 20261121_0100). Nguồn: xem đầu _video/nv1/ql_duong_sat.py.
#  Báo Đầu tư/MarketTimes 20/11/2026 (tổ công tác vốn; 1.713.548 tỷ; ngân sách hạn chế, ODA khó); Hà Nội Mới 10/11/2026 (giải ngân 10 tháng 74,1%, còn 247.300 tỷ);
#  VnEconomy 16/8/2025 (Đông Sơn rao 3 tỷ, mua 5,5 tỷ); VnEconomy 19/1/2025 + VietNamNet 22/12/2024 (Metro 1: 17.387 → 43.700 tỷ, dự kiến 2018, chạy 22/12/2024).
#  Em tự tính: 16,7 triệu/người; vay 1,2 tỷ lãi 10% = 10 triệu/tháng, 9 năm 1,08 tỷ.
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261121_0100_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Trên con đường sắt 67 tỷ đô la này, nhà anh chị đang đứng ở chỗ nào: người có đất, người đi tàu, hay người đang vay tiền chờ giá?'
R = dict(key='RV2111HT', tieu_de='Đường sắt tốc độ cao 67 tỷ USD: ai trả tiền, tiền về túi ai? Vay mua đất theo tin, chờ 9 năm lãi 1,08 tỷ',
 hook=['ĐƯỜNG SẮT 67 TỶ USD', 'AI TRẢ TIỀN, AI ĐƯỢC TIỀN???'], nhan='HẠ TẦNG · HỎI THẬT',
 short_caption=('Đường sắt tốc độ cao Bắc – Nam sơ bộ 1.713.548 tỷ đồng (khoảng 67 tỷ USD); Bộ Tài chính lập tổ công tác tìm nguồn vốn vì ngân sách hạn chế, vốn vay ưu đãi khó hơn (Báo Đầu tư 20/11/2026). '
                'Đầu tư công 10 tháng mới giải ngân 74,1%, còn 247.300 tỷ (Bộ Tài chính, Hà Nội Mới 10/11/2026). Đông Sơn, Thanh Hóa: lô 100 m2 rao 3 tỷ, sau hơn 1 năm mua 5,5 tỷ (VnEconomy 16/8/2025). '
                'Metro số 1: vốn 17.387 tỷ (2007) lên 43.700 tỷ, dự kiến chạy 2018, chạy thật 22/12/2024 (VnEconomy, VietNamNet). Em tự tính: chia đều 16,7 triệu/người; vay 1,2 tỷ lãi 10% là 10 triệu/tháng, 9 năm 1,08 tỷ. '
                'Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH ĐỨNG Ở ĐÂU?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City Metro Line 1', 'Hanoi skyline night']),
 canh=[
  C('TÌM NGUỒN VỐN 67 TỶ USD', 'Bộ Tài chính vừa lập tổ công tác tìm nguồn vốn cho đường sắt tốc độ cao Bắc Nam. Tổng vốn sơ bộ khoảng 67 tỷ đô la, vì ngân sách còn hạn chế và vốn vay ưu đãi ngày càng khó.',
    the=dict(loai='lon', tieu='ĐƯỜNG SẮT TỐC ĐỘ CAO BẮC – NAM', nguon='Báo Đầu tư 20/11/2026', dong=[['67 TỶ USD', 118, 'vang'], ['1.713.548 TỶ ĐỒNG', 56, 'trang']])),
  C('CHIA ĐỀU 16,7 TRIỆU', 'Để dễ hình dung, nếu chia đều cho hơn 102 triệu dân, mỗi người khoảng 16 triệu 700 nghìn đồng. Tiền sẽ chi trong nhiều năm, nhưng rốt cuộc là thuế hôm nay, hoặc nợ trả dần bằng thuế mai sau.',
    the=dict(loai='lon', tieu='NẾU CHIA ĐỀU MỖI NGƯỜI DÂN', nguon='Em tự tính, dân số 2025 Cục Thống kê', dong=[['16,7 TRIỆU', 118, 'vang'], ['ĐỂ HÌNH DUNG, KHÔNG PHẢI NỘP', 50, 'trang']])),
  C('CÓ TIỀN CHƯA CHẮC TIÊU ĐƯỢC', 'Nhưng có tiền chưa chắc đã tiêu được. Hết tháng 10, đầu tư công cả nước mới giải ngân khoảng 74%, còn 247 nghìn tỷ chưa chi. Một nút thắt lớn là mặt bằng.',
    the=dict(loai='cot', tieu='ĐẦU TƯ CÔNG 2026, HẾT THÁNG 10 (%)', nguon='Bộ Tài chính, Hà Nội Mới 10/11/2026', hang=[['Đã giải ngân', 74.1], ['Còn lại', 25.9]], noi=[1], dv='%', max=100)),
  C('RAO 3 TỶ, MUA 5,5 TỶ', 'Trong khi đó, giá đất chạy trước đường ray. Ở Đông Sơn, Thanh Hóa, nơi có ga theo quy hoạch, một lô đất 100 mét vuông từng rao khoảng 3 tỷ, hơn một năm sau được mua năm tỷ rưỡi.',
    the=dict(loai='cot', tieu='LÔ ĐẤT 100 M2 Ở ĐÔNG SƠN (TỶ Đ)', nguon='VnEconomy 16/8/2025', hang=[['Hơn 1 năm trước', 3], ['Tháng 8/2025', 5.5]], noi=[1], dv='', max=6)),
  C('METRO SỐ 1 GẤP 2,5 LẦN', 'Lần trước, Metro số 1 ở Thành phố Hồ Chí Minh được duyệt khoảng 17 nghìn tỷ, dự kiến chạy năm 2018. Tàu chạy thật cuối năm 2024, vốn khoảng 43 nghìn 700 tỷ.',
    the=dict(loai='cot', tieu='VỐN METRO SỐ 1 (NGHÌN TỶ Đ)', nguon='VnEconomy 19/1/2025, VietNamNet 22/12/2024', hang=[['Năm 2007', 17.4], ['Sau điều chỉnh', 43.7]], noi=[1], dv='', max=50)),
  C('VAY 1,2 TỶ, LÃI 10 TRIỆU', 'Giả sử một người vay 1 tỷ 200 triệu mua đất theo tin, lãi suất 10%. Mỗi tháng trả 10 triệu tiền lãi. Chờ 9 năm đến lúc tàu dự kiến chạy, tiền lãi là 1 tỷ 80 triệu.',
    the=dict(loai='lon', tieu='VAY 1,2 TỶ, LÃI SUẤT 10% (GIẢ ĐỊNH)', nguon='Em tự tính', dong=[['1,08 TỶ', 118, 'do'], ['TIỀN LÃI TRONG 9 NĂM', 56, 'trang']])),
  C('AI ĐƯỢC TRƯỚC?', 'Theo em, tiền đến trước với người có đất bị thu hồi, rồi nhà thầu, công nhân, vật liệu. Người vay tiền mua đất theo tin đứng cuối hàng, vì họ phải trả lãi cho thời gian chờ.',
    the=dict(loai='lon', tieu='TIỀN ĐI VÀO TÚI AI TRƯỚC', nguon='Nhận định của Huy Nguyễn', dong=[['NGƯỜI CÓ ĐẤT', 96, 'vang'], ['RỒI NHÀ THẦU, CÔNG NHÂN', 52, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    sys.path.insert(0, CW + '/_video'); import kiem_loi
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
    for c in R['canh']: print(c['loi_doc'][:260])
