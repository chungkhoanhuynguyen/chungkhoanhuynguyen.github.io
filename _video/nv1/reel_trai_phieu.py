# -*- coding: utf-8 -*-
# NV1 21/11/2026 – REEL cặp với CH2811TP (lô 20261121_0200). Nguồn: xem đầu _video/nv1/ql_trai_phieu.py.
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261121_0200_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Anh chị đã bao giờ được mời một sản phẩm lãi cao hơn tiết kiệm ngay tại quầy, và anh chị hỏi câu gì trước khi quyết định?'
R = dict(key='RV2111TP', tieu_de='Lãi tiết kiệm giảm, được mời "lãi 9%, cũng như gửi tiết kiệm": 4 chữ phải hỏi trước khi ký',
 hook=['LÃI TIẾT KIỆM GIẢM', 'MỜI LÃI 9% CÓ NÊN KÝ???'], nhan='TIỀN GỬI · HỎI THẬT',
 short_caption=('Lãi huy động giảm 0,5–1 điểm % từ giữa tháng 10, lãi 6 tháng bình quân tháng 10 khoảng 4,47% (VCBS, VietnamFinance 17/11/2026); trái phiếu ngân hàng vẫn 9–10,5%/năm. '
                'Bảo hiểm tiền gửi tối đa 350 triệu/người/ngân hàng, gồm gốc và lãi, từ 13/7/2026 (Thông tư 05/2026); trái phiếu không phải tiền gửi nên không được bảo hiểm tiền gửi. '
                'Vụ án khởi tố năm 2022: hơn 30.081 tỷ của 35.824 người mua trái phiếu bị chiếm đoạt (VnEconomy 28/9/2024). Trái phiếu ngân hàng phát hành là sản phẩm hợp pháp; video chỉ phân biệt với tiền gửi. '
                'Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='ANH CHỊ ĐÃ ĐƯỢC MỜI?', loi=Q, loi_doc=lib.doc(Q), anh=['Ho Chi Minh City skyline night', 'Hanoi skyline night']),
 canh=[
  C('LÃI TIẾT KIỆM VỪA GIẢM', 'Lãi tiết kiệm vừa giảm thêm nửa điểm đến một điểm phần trăm từ giữa tháng 10. Lãi 6 tháng bình quân thị trường chỉ còn khoảng bốn phẩy năm phần trăm.',
    the=dict(loai='lon', tieu='LÃI 6 THÁNG BÌNH QUÂN, THÁNG 10/2026', nguon='VCBS, VietnamFinance 17/11/2026', dong=[['4,47%', 118, 'vang'], ['GIẢM 0,5 ĐẾN 1 ĐIỂM', 56, 'trang']])),
  C('LỜI MỜI LÃI 9%', 'Cùng lúc, nhiều người cầm sổ đáo hạn ra quầy được mời một sản phẩm lãi 9%, gần gấp đôi, kèm câu: cũng như gửi tiết kiệm thôi.',
    the=dict(loai='cot', tieu='LÃI MỖI NĂM (%)', nguon='VCBS; trái phiếu ngân hàng 9–10,5%, VietnamFinance', hang=[['Tiết kiệm 6 tháng', 4.47], ['Lời mời ở quầy', 9]], noi=[1], dv='%', max=10)),
  C('800 TRIỆU CHÊNH 32 TRIỆU', 'Với 800 triệu, lãi 5% được 40 triệu một năm, lãi 9% được 72 triệu. Chênh 32 triệu một năm, nghe rất hấp dẫn. Câu hỏi là phần chênh đó đổi lấy điều gì.',
    the=dict(loai='cot', tieu='800 TRIỆU, TIỀN LÃI MỖI NĂM (TRIỆU Đ)', nguon='Em giả định, em tự tính', hang=[['Lãi 5%', 40], ['Lãi 9%', 72]], noi=[1], dv='', max=80)),
  C('ĐỌC DÒNG CHỮ NHỎ', 'Nhưng hãy đọc dòng chữ nhỏ. Nếu ghi loại sản phẩm là trái phiếu, thì đó không phải tiền gửi. Trái phiếu không được bảo hiểm tiền gửi, rủi ro thuộc về tổ chức phát hành.',
    the=dict(loai='lon', tieu='TRÁI PHIẾU KHÁC TIẾT KIỆM', nguon='Luật Bảo hiểm tiền gửi; div.gov.vn', dong=[['KHÔNG PHẢI', 96, 'do'], ['TIỀN GỬI', 96, 'do']])),
  C('BẢO HIỂM 350 TRIỆU', 'Còn tiền gửi tiết kiệm được bảo hiểm tối đa 350 triệu đồng cho mỗi người tại mỗi ngân hàng, tính cả gốc và lãi.',
    the=dict(loai='lon', tieu='HẠN MỨC BẢO HIỂM TIỀN GỬI TỪ 13/7/2026', nguon='Thông tư 05/2026/TT-NHNN', dong=[['350 TRIỆU', 118, 'vang'], ['MỖI NGƯỜI, MỖI NGÂN HÀNG', 52, 'trang']])),
  C('LẦN TRƯỚC: 35.824 NGƯỜI', 'Trong vụ án khởi tố năm 2022, hơn 30 nghìn tỷ đồng của gần 36 nghìn người mua trái phiếu đã bị chiếm đoạt. Khi ấy, nhiều người được giới thiệu đó là một hình thức tiết kiệm.',
    the=dict(loai='lon', tieu='VỤ ÁN KHỞI TỐ NĂM 2022', nguon='VnEconomy 28/9/2024; kết luận điều tra', dong=[['30.081 TỶ', 110, 'do'], ['CỦA 35.824 NGƯỜI MUA TRÁI PHIẾU', 46, 'trang']])),
  C('HỎI 4 CHỮ', 'Trái phiếu do ngân hàng phát hành hôm nay là sản phẩm hợp pháp. Nhưng trước khi ký, hãy hỏi đúng bốn chữ: có phải tiền gửi không?',
    the=dict(loai='lon', tieu='TRƯỚC KHI KÝ, HỎI', nguon='Gợi ý của Huy Nguyễn', dong=[['CÓ PHẢI', 104, 'vang'], ['TIỀN GỬI KHÔNG?', 80, 'vang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    sys.path.insert(0, CW + '/_video'); import kiem_loi
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
