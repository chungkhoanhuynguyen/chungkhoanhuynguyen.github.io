# -*- coding: utf-8 -*-
# NV1 24/11/2026 – REEL cặp với CH0812LS (lô 20261124_0100): lãi tiết kiệm qua đỉnh? Nguồn: xem đầu _video/nv1/ql_lai_dinh.py.
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261124_0100_reel'
sys.path.insert(0, CW + '/_video'); from phat_am import doc as pa
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(pa(loi))); d.update(k); return d
Q = 'Anh chị đang gửi kỳ dài hay kỳ ngắn, và trong năm tới cần dùng bao nhiêu phần trăm số tiền đó?'
R = dict(key='RV2411LS', tieu_de='Lãi tiết kiệm đã qua đỉnh? Lần trước có nơi trả 10%, một năm sau cao nhất chỉ 5,7% – cùng 600 triệu, lãi 60 triệu hay 34,2 triệu',
 hook=['LÃI TIẾT KIỆM', 'ĐÃ QUA ĐỈNH???'], nhan='LÃI SUẤT · TÚI TIỀN',
 short_caption=('NHNN yêu cầu giảm 0,5–1%/năm lãi tiền gửi mới kỳ hạn từ 6 tháng, giảm 1,5–2%/năm lãi cho vay (họp báo Chính phủ 4/11/2026, VCCI 10/11/2026). '
                'Phần lớn ngân hàng niêm yết 12 tháng dưới 7% (TT Tài chính Tiền tệ 1/11/2026). Lần trước: 12/2022 có nơi trả 10% kỳ 12 tháng (TT Tài chính Tiền tệ 1/12/2022); '
                '12/2023 cao nhất thị trường 12 tháng 5,7%, Vietcombank 4,8% (VnEconomy 12/12/2023). 600 triệu × 10% = 60 triệu; × 5,7% = 34,2 triệu (tự tính). '
                'Khoản vay mới cuối tháng 10 giảm 0,2–0,5% (VCCI 10/11/2026).'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='KỲ DÀI HAY KỲ NGẮN?', loi=Q, loi_doc=lib.doc(pa(Q)), anh=['Ho Chi Minh City skyline night', 'Hanoi skyline night']),
 canh=[
  C('NHNN YÊU CẦU GIẢM LÃI', 'Ngân hàng Nhà nước vừa yêu cầu giảm lãi tiền gửi mới từ nửa điểm đến một điểm phần trăm, áp dụng cho kỳ hạn từ 6 tháng. Lãi cho vay phải giảm mạnh hơn.',
    the=dict(loai='lon', tieu='HỌP BÁO CHÍNH PHỦ 4/11/2026', nguon='VCCI 10/11/2026', dong=[['GIẢM 0,5 ĐẾN 1%', 96, 'vang'], ['LÃI TIỀN GỬI MỚI, TỪ 6 THÁNG', 50, 'trang']])),
  C('NIÊM YẾT DƯỚI 7%', 'Đầu tháng 11, phần lớn ngân hàng niêm yết kỳ 12 tháng dưới 7%. Mức 9,1% từng được quảng cáo là lãi niêm yết cộng thêm ưu đãi, có hạn và có điều kiện.',
    the=dict(loai='lon', tieu='LÃI NIÊM YẾT KỲ 12 THÁNG', nguon='TT Tài chính Tiền tệ 1/11/2026', dong=[['DƯỚI 7%', 120, 'vang'], ['Ở PHẦN LỚN NGÂN HÀNG', 52, 'trang']])),
  C('LẦN TRƯỚC: 10% CÒN 5,7%', 'Lần trước lãi quay đầu, tháng 12 năm 2022 có nơi trả 10% cho kỳ 12 tháng. Một năm sau, nơi trả cao nhất chỉ còn 5,7%, Vietcombank còn 4,8%.',
    the=dict(loai='cot', tieu='LÃI 12 THÁNG (%)', nguon='TT Tài chính Tiền tệ 1/12/2022, VnEconomy 12/12/2023', hang=[['Có nơi 12/2022', 10], ['Cao nhất 12/2023', 5.7], ['Vietcombank 12/2023', 4.8]], noi=[1], dv='%')),
  C('CÙNG 600 TRIỆU', 'Cùng 600 triệu, gửi 12 tháng ở mức 10% thì một năm nhận 60 triệu tiền lãi. Chậm một năm, ở mức cao nhất 5,7%, chỉ còn 34 triệu 200 nghìn đồng.',
    the=dict(loai='cot', tieu='TIỀN LÃI 1 NĂM CỦA 600 TRIỆU (TỰ TÍNH)', nguon='Em tự tính từ số liệu trên', hang=[['Mức 10%', 60], ['Mức 5,7%', 34.2]], noi=[1], dv=' triệu')),
  C('NGƯỜI VAY CÒN PHẢI CHỜ', 'Còn người vay, số đo được trước họp báo cho thấy khoản vay mới cuối tháng 10 chỉ giảm khoảng 0,2 đến 0,5 điểm phần trăm. Khoản vay cũ thả nổi thường điều chỉnh theo kỳ ghi trong hợp đồng.',
    the=dict(loai='lon', tieu='LÃI VAY MỚI CUỐI THÁNG 10', nguon='VCCI 10/11/2026', dong=[['GIẢM 0,2 ĐẾN 0,5%', 88, 'vang'], ['YÊU CẦU: GIẢM 1,5 ĐẾN 2%', 52, 'trang']])),
  C('PHÉP THỬ 10 GIÂY', 'Phép thử của em: tiền cần dùng trong 12 tháng dưới 30% thì phần lớn có thể khóa kỳ dài, từ 30 đến 60% thì chia nhiều sổ, trên 60% thì ưu tiên kỳ ngắn. Đây là mốc tự soi, không phải lời khuyên chung.',
    the=dict(loai='lon', tieu='TIỀN CẦN DÙNG TRONG 12 THÁNG', nguon='Mốc tự soi của Huy Nguyễn', dong=[['DƯỚI 30% / TRÊN 60%', 84, 'vang'], ['KỲ DÀI / KỲ NGẮN', 56, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    import kiem_loi
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
