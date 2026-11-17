# -*- coding: utf-8 -*-
# NV1 18/11/2026 – 2 REEL MỚI cho TikTok phụ @anhnh977 (kho tiktok_anhnh977_noi_dung_1711), nối tiếp chủ đề nhiều view nhất "GDP tăng 9,95% sao kiếm tiền khó" (791 view).
# (Không xem được trang TikTok trong phiên tự động – không dùng trình duyệt; lấy top chủ đề từ số QL1 ghi 17/11.)
# TT1811NHA "Vì sao giá nhà tăng nhanh hơn lương?":
#  - Savills, VnBusiness 15/10/2026: Hà Nội quý 3/2026 sơ cấp 107 triệu/m²; căn hộ hạng C: nguồn cung sơ cấp giảm 27% mỗi năm từ 2022, giá sơ cấp tăng 17% mỗi năm; căn bán được giảm 48% so cùng kỳ.
#  - Savills (VietnamFinance 16/10/2026): 70% số căn bán được ở Hà Nội quý 3 có giá trên 6 tỷ.
#  - TCTK (WiData 280708): thu nhập bình quân lao động Q3/2026 9.184.891 đ, +9,85% so cùng kỳ. Tự tính: 6 tỷ / (9,185 tr × 12 × 2) = 27,2 năm.
#  - CBRE (Doanh nhân Pháp luật 16/10/2026): giá sơ cấp TB toàn Hà Nội quý 3/2026 khoảng 86 triệu/m², giảm 6% so cùng kỳ; thứ cấp khoảng 60 triệu/m², giảm 8%; nguồn cung mới giảm 40%.
#  - SSI Research (Công Luận 6/11/2026): lãi thả nổi vay mua nhà 12–15%.
# TT1811TK "Gửi 1 tỷ, lãi thật còn bao nhiêu?":
#  - Lãi huy động 12 tháng NHTM Nhà nước 5,4% (WiData 202886, 12/11/2026); CPI 10/2026 +5,09% so cùng kỳ (TCTK, WiData 75701); thu nhập lao động +9,85% (TCTK).
#  - Tự tính: 1 tỷ × 5,4% = 54 triệu; giá cả 1 tỷ × 5,09% = 50,9 triệu; lãi thật 1 tỷ × (1,054/1,0509 − 1) = 2,95 triệu (khoảng 3 triệu).
#  - Bảo hiểm tiền gửi tối đa 350 triệu/người/tổ chức từ 13/7/2026 (VietnamPlus, Báo Đầu tư).
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261118_0100_reel_tt'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q1 = 'Với thu nhập hiện tại, nhà anh chị cần bao nhiêu năm để mua được căn nhà mình muốn? Anh chị nghĩ giá nhà năm tới sẽ đi đâu?'
R1 = dict(key='TT1811NHA', tieu_de='Căn hộ 6 tỷ bằng 27 năm lương hai vợ chồng: vì sao giá nhà tăng nhanh hơn lương?',
 hook=['CĂN HỘ 6 TỶ = 27 NĂM LƯƠNG', 'NHÀ TĂNG NHANH HƠN LƯƠNG???'], nhan='NHÀ ĐẤT · HỎI THẬT',
 short_caption=('Căn hộ hạng C Hà Nội: nguồn cung giảm 27% mỗi năm từ 2022, giá tăng 17% mỗi năm (Savills, VnBusiness 15/10/2026); thu nhập lao động +9,85% (TCTK). '
                '6 tỷ = 27 năm lương 2 người (tự tính). Quý 3/2026 giá sơ cấp toàn Hà Nội giảm 6% so cùng kỳ (CBRE, 16/10/2026). Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH CẦN MẤY NĂM?', loi=Q1, loi_doc=lib.doc(Q1), anh=['Hanoi apartment buildings', 'Hanoi skyline night']),
 canh=[
  C('27 NĂM LƯƠNG', 'Cục Thống kê vừa công bố thu nhập bình quân của người lao động khoảng 9,2 triệu mỗi tháng. Với mức đó, một căn hộ 6 tỷ ở Hà Nội bằng khoảng 27 năm lương của cả hai vợ chồng, nếu không tiêu một đồng nào.',
    the=dict(loai='lon', tieu='CĂN HỘ 6 TỶ BẰNG', nguon='TCTK quý 3/2026; em tự tính', dong=[['27 NĂM', 130, 'do'], ['LƯƠNG HAI NGƯỜI, KHÔNG TIÊU GÌ', 50, 'trang']])),
  C('NHÀ +17%, LƯƠNG +9,85%', 'Từ năm 2022, giá căn hộ bình dân ở Hà Nội tăng khoảng 17% mỗi năm. Còn thu nhập của người lao động năm nay tăng 9,85%.',
    the=dict(loai='cot', tieu='TĂNG MỖI NĂM (%)', nguon='Savills 15/10/2026; TCTK quý 3/2026', hang=[['Căn hộ hạng C', 17], ['Thu nhập lao động', 9.85]], noi=[0], dv='%', max=20)),
  C('NHÀ RẺ NGÀY CÀNG ÍT', 'Lý do đầu tiên là nhà giá rẻ ngày càng ít. Nguồn cung căn hộ bình dân mới giảm khoảng 27% mỗi năm kể từ năm 2022.',
    the=dict(loai='lon', tieu='CĂN HỘ HẠNG C MỞ BÁN MỚI', nguon='Savills, VnBusiness 15/10/2026', dong=[['GIẢM 27%', 124, 'do'], ['MỖI NĂM TỪ 2022', 58, 'trang']])),
  C('70% TRÊN 6 TỶ', 'Lý do thứ hai là dự án mới đa số là hàng đắt. Quý 3 năm nay, 70% số căn bán được ở Hà Nội có giá trên 6 tỷ đồng.',
    the=dict(loai='lon', tieu='CĂN BÁN ĐƯỢC Ở HÀ NỘI QUÝ 3/2026', nguon='Savills, VietnamFinance 16/10/2026', dong=[['70%', 130, 'vang'], ['CÓ GIÁ TRÊN 6 TỶ', 58, 'trang']])),
  C('NĂM NAY GIÁ ĐÃ GIẢM', 'Nhưng có một cú lật. Quý 3 năm nay, giá chào bán bình quân toàn Hà Nội giảm 6% so với cùng kỳ, giá căn hộ cũ giảm 8%.',
    the=dict(loai='cot', tieu='GIÁ CĂN HỘ HÀ NỘI, SO CÙNG KỲ (%)', nguon='CBRE, Doanh nhân Pháp luật 16/10/2026', hang=[['Bán mới', -6], ['Căn hộ cũ', -8]], noi=[1], dv='%')),
  C('LÃI VAY 12 ĐẾN 15%', 'Lý do là lãi vay mua nhà đã lên 12 đến 15%. Người mua chậm lại, số căn bán được giảm gần một nửa so với cùng kỳ.',
    the=dict(loai='lon', tieu='LÃI THẢ NỔI VAY MUA NHÀ', nguon='SSI Research, Công Luận 6/11/2026', dong=[['12 ĐẾN 15%', 120, 'do'], ['CĂN BÁN ĐƯỢC GIẢM 48%', 56, 'trang']])),
  C('NHÀ ĐỂ Ở, LƯƠNG ĐỂ TRẢ', 'Nhà để ở thì nên mua bằng khả năng trả nợ của chính mình, không phải bằng kỳ vọng giá sẽ tăng. Tiền trả góp nên dưới 40% thu nhập.',
    the=dict(loai='lon', tieu='MỐC AN TOÀN KHI VAY MUA NHÀ', nguon='Báo Đấu thầu 17/11/2026', dong=[['DƯỚI 40%', 124, 'vang'], ['THU NHẬP CHO TRẢ GÓP', 56, 'trang']])),
 ])
Q2 = 'Tiền gửi tiết kiệm của anh chị đang thắng giá cả bao nhiêu? Anh chị để bao nhiêu phần tài sản trong tiết kiệm?'
R2 = dict(key='TT1811TK', tieu_de='Gửi 1 tỷ, lãi 54 triệu – nhưng giá cả ăn mất 50,9 triệu: lãi thật chỉ còn khoảng 3 triệu?',
 hook=['GỬI 1 TỶ, LÃI 54 TRIỆU', 'LÃI THẬT CÒN BAO NHIÊU???'], nhan='TIẾT KIỆM · HỎI THẬT',
 short_caption=('Lãi tiết kiệm 12 tháng NHTM Nhà nước 5,4% (12/11/2026); CPI 10/2026 +5,09% so cùng kỳ (Cục Thống kê). Tự tính: 1 tỷ × (1,054/1,0509 − 1) ≈ 2,95 triệu lãi thật. '
                'Bảo hiểm tiền gửi tối đa 350 triệu từ 13/7/2026. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='TIỀN GỬI CÓ THẮNG GIÁ?', loi=Q2, loi_doc=lib.doc(Q2), anh=['Ho Chi Minh City skyline night', 'Hanoi skyline night']),
 canh=[
  C('GIÁ CẢ TĂNG 5,09%', 'Cục Thống kê vừa công bố: tháng 10 năm nay, giá cả tăng 5,09% so với cùng kỳ. Với 1 tỷ đồng tiền gửi, đó là khoảng 50,9 triệu sức mua bị mất đi.',
    the=dict(loai='lon', tieu='CHỈ SỐ GIÁ TIÊU DÙNG 10/2026', nguon='Cục Thống kê', dong=[['+5,09%', 130, 'do'], ['SO VỚI CÙNG KỲ', 58, 'trang']])),
  C('GỬI 1 TỶ, LÃI 54 TRIỆU', 'Còn gửi 1 tỷ kỳ hạn 12 tháng ở ngân hàng thương mại nhà nước, lãi khoảng 5,4%. Một năm anh chị nhận về 54 triệu đồng.',
    the=dict(loai='lon', tieu='LÃI TIẾT KIỆM 12 THÁNG', nguon='NHTM Nhà nước, 12/11/2026', dong=[['54 TRIỆU', 130, 'vang'], ['TIỀN LÃI MỘT NĂM CỦA 1 TỶ', 52, 'trang']])),
  C('LÃI THẬT KHOẢNG 3 TRIỆU', 'Trừ phần giá cả đi, tiền lãi thật của 1 tỷ chỉ còn khoảng 3 triệu đồng một năm. Em tự tính.',
    the=dict(loai='cot', tieu='TIỀN LÃI CỦA 1 TỶ MỘT NĂM (TRIỆU)', nguon='Em tự tính', hang=[['Lãi nhận về', 54], ['Lãi thật', 2.95]], noi=[1], dv='', max=60)),
  C('LƯƠNG VẪN THẮNG GIÁ', 'Trong khi đó, thu nhập của người lao động năm nay tăng 9,85%. Lương vẫn thắng giá cả, còn tiền gửi thì gần như chỉ hòa.',
    the=dict(loai='cot', tieu='TĂNG MỘT NĂM (%)', nguon='Cục Thống kê; lãi 12 tháng 12/11/2026', hang=[['Thu nhập', 9.85], ['Lãi gửi', 5.4], ['Giá cả', 5.09]], noi=[1], dv='%', max=12)),
  C('KHÔNG PHẢI MẤT TIỀN', 'Điều này không có nghĩa gửi tiết kiệm là mất tiền. Tiết kiệm là để giữ giá trị và để có tiền khi cần, chứ không phải để giàu nhanh.',
    the=dict(loai='lon', tieu='TIỀN GỬI ĐỂ LÀM GÌ?', nguon='Quan điểm cá nhân', dong=[['GIỮ GIÁ TRỊ', 116, 'vang'], ['KHÔNG PHẢI ĐỂ GIÀU NHANH', 54, 'trang']])),
  C('350 TRIỆU MỖI NƠI', 'Nếu gửi nhiều, anh chị nên nhớ mức bảo hiểm tiền gửi hiện là 350 triệu đồng mỗi người ở mỗi ngân hàng, áp dụng từ tháng 7 năm nay.',
    the=dict(loai='lon', tieu='BẢO HIỂM TIỀN GỬI TỐI ĐA', nguon='VietnamPlus, Báo Đầu tư; từ 13/7/2026', dong=[['350 TRIỆU', 124, 'vang'], ['MỖI NGƯỜI, MỖI NGÂN HÀNG', 54, 'trang']])),
  C('PHẦN MUỐN TĂNG', 'Còn phần tiền muốn tăng nhanh hơn giá cả, anh chị cần kênh khác, và phải chấp nhận rủi ro đi kèm. Đừng dồn tất cả vào một chỗ.',
    the=dict(loai='lon', tieu='CHIA TIỀN THEO MỤC ĐÍCH', nguon='Quan điểm cá nhân', dong=[['CHIA ĐỂ GIỮ', 116, 'vang'], ['KHÔNG DỒN MỘT CHỖ', 56, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R1, R2], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.path.insert(0, CW + '/_video'); import kiem_loi
for R in (R1, R2):
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()), [len(h) for h in R['hook']])
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
        if 'câu cụt' not in q: print(q)
