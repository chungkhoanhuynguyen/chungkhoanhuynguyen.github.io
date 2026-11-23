# -*- coding: utf-8 -*-
# NV1 23/11/2026 – REEL cặp với CH0612CM (lô 20261123_2230): cảng Cái Mép. Nguồn: xem đầu _video/nv1/ql_cai_mep.py.
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261123_2230_reel'
sys.path.insert(0, CW + '/_video'); from phat_am import doc as pa
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(pa(loi))); d.update(k); return d
Q = 'Theo anh chị, khi đường mới thông xe, Cái Mép có lấy lại hạng 7 thế giới, hay Hải Phòng sẽ vượt lên?'
# V2 24/11: thêm cảnh Hải Phòng + người chịu thiệt (57s lên ~70s); ảnh câu hỏi cuối đổi sang cảng Việt Nam (V1 rơi cảng Koper, Slovenia)
R = dict(key='RV2311CM', tieu_de='Cảng giữa rừng đước đón tàu 16.828 container, từng xếp thứ 7 thế giới trên cả Singapore – vì sao năm nay tụt xuống thứ 11?',
 hook=['CẢNG GIỮA RỪNG ĐƯỚC', 'XẾP TRÊN CẢ SINGAPORE???'], nhan='CẢNG BIỂN · TÚI TIỀN',
 short_caption=('Luồng Cái Mép – Thị Vải sâu 15,5 m, tàu 160.000–200.000 tấn ra vào không phụ thuộc thủy triều, vốn ngân sách hơn 1.414 tỷ (SGGP 9/2/2024). '
                'Tàu OOCL Bauhinia 166.000 tấn, 16.828 TEU, dài 366,99 m cập Tân Cảng Cái Mép – Thị Vải 13/3/2025 (Hà Nội Mới). '
                'CPPI của World Bank: Cái Mép thứ 7 hai kỳ liền (Gemadept 12/6/2024, SGGP 22/10/2025); kỳ công bố 10/6/2026 xuống thứ 11, Hải Phòng thứ 13 (bbw.vn 11/6/2026). '
                'Năm 2025 hơn 12,4 triệu TEU, +12,91%; gần hết công suất, tàu chờ cầu 3 giờ – 3 ngày (Báo Xây dựng 11/1/2026). Đường 991B dự kiến thông xe 12/2026 (Người Quan Sát 1/11/2026).'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='CÁI MÉP LẤY LẠI HẠNG 7?', loi=Q, loi_doc=lib.doc(pa(Q)), anh=['container port Vietnam', 'Ho Chi Minh City skyline']),
 canh=[
  C('TÀU 16.828 CONTAINER', 'Cảng giữa rừng đước ở Cái Mép từng đứng thứ 7 thế giới, vừa tụt xuống thứ 11. Ngày 13 tháng 3 năm ngoái, nơi đây đón tàu OOCL Bauhinia, chở được 16.828 container, dài gần 367 mét.',
    the=dict(loai='lon', tieu='TÀU OOCL BAUHINIA · 13/3/2025', nguon='Báo Hà Nội Mới 13/3/2025', dong=[['16.828 TEU', 112, 'vang'], ['DÀI 366,99 MÉT', 56, 'trang']])),
  C('LUỒNG SÂU 15,5 MÉT', 'Bí mật của cảng nằm ở dưới nước. Luồng Cái Mép – Thị Vải được nạo vét sâu 15,5 mét, sâu nhất cả nước, bằng khoảng 5 tầng nhà. Tàu mẹ trọng tải 200.000 tấn vào không phải chờ nước lên.',
    the=dict(loai='lon', tieu='LUỒNG CÁI MÉP – THỊ VẢI', nguon='Báo SGGP 9/2/2024', dong=[['15,5 MÉT', 120, 'vang'], ['BẰNG KHOẢNG 5 TẦNG NHÀ', 56, 'trang']])),
  C('THỨ 7 THẾ GIỚI', 'Kết quả: hai kỳ liền, chỉ số hiệu quả cảng container của Ngân hàng Thế giới xếp Cái Mép thứ 7 thế giới. Kỳ gần nhất, Cái Mép đứng trên cả Singapore và Hồng Kông.',
    the=dict(loai='lon', tieu='CHỈ SỐ HIỆU QUẢ CẢNG CONTAINER (CPPI)', nguon='Gemadept 12/6/2024, SGGP 22/10/2025', dong=[['THỨ 7', 120, 'vang'], ['KỲ 2024 TRÊN SINGAPORE', 52, 'trang']])),
  C('NĂM NAY TỤT XUỐNG THỨ 11', 'Nhưng tháng 6 năm nay, Cái Mép lùi 4 bậc, xuống thứ 11. Cảng gần như hết công suất, tàu trễ lịch phải chờ cầu bến từ 3 giờ đến 3 ngày.',
    the=dict(loai='cot', tieu='HẠNG CPPI CỦA CÁI MÉP (CÀNG THẤP CÀNG TỐT)', nguon='bbw.vn 11/6/2026, Báo Xây dựng 11/1/2026', hang=[['Hai kỳ trước', 7], ['Kỳ 6/2026', 11]], noi=[1], dv='', max=13)),
  C('HẢI PHÒNG THỨ 13', 'Cùng kỳ đó, Hải Phòng lần đầu vào top 20, xếp thứ 13. Còn ở Cái Mép, chỉ hai cảng có cầu riêng cho sà lan. Người chịu thiệt khi cảng quá đông là tài xế nằm chờ cả ngày và chủ hàng lỡ chuyến tàu.',
    the=dict(loai='lon', tieu='CPPI KỲ CÔNG BỐ 6/2026', nguon='bbw.vn 11/6/2026, Báo Xây dựng 11/1/2026', dong=[['HẢI PHÒNG THỨ 13', 96, 'vang'], ['LẦN ĐẦU VÀO TOP 20', 56, 'trang']])),
  C('ĐƯỜNG MỚI THÁNG 12', 'Năm ngoái cụm cảng đón hơn 12,4 triệu TEU. Đường 991B nối cảng ra quốc lộ, vốn gần 4.000 tỷ, dự kiến thông xe tháng 12 này.',
    the=dict(loai='lon', tieu='CONTAINER QUA CÁI MÉP – THỊ VẢI NĂM 2025', nguon='Cảng vụ TP.HCM, Báo Xây dựng 11/1/2026', dong=[['12,4 TRIỆU TEU', 104, 'vang'], ['TĂNG GẦN 13%', 56, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    import kiem_loi
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
