# -*- coding: utf-8 -*-
# NV1 20/11/2026 – REEL câu hỏi lớn, cặp với CH2711TN (lô 20261120_0100). Nguồn: xem đầu _video/nv1/ql_thue_tncn.py.
#  VnExpress 23/10/2026 (thu TNCN 2026 ước 203.200 tỷ, thấp hơn dự toán 33.800 tỷ; giảm trừ 15,5/6,2 triệu; 5 bậc, 5% đến 10 triệu, 35% trên 100 triệu);
#  Nhân Dân 29/11/2025 (khung 5 bậc); biểu 7 bậc cũ Luật 2007 sửa 2012; Nghị quyết 954/2020 (11 triệu từ 7/2020); WiData/Cục Thống kê (thu nhập bình quân Q3/2020 5,79; Q3/2025 8,36; Q3/2026 9,18 triệu).
#  Em tự tính: 27 triệu 1 con: 990 nghìn còn 265 nghìn; 110 triệu: 24,8 còn 18,85 triệu (bớt 5,95).
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261120_0100_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q = 'Phần thuế thu nhập nhà anh chị được giảm năm nay đang nằm ở đâu: tiết kiệm, trả nợ, hay đã tan vào chi tiêu?'
R = dict(key='RV2011TN', tieu_de='Thu thuế thu nhập cá nhân hụt 34.000 tỷ: ai được lợi nhất? Lương 110 triệu bớt 6 triệu, 27 triệu bớt 725 nghìn',
 hook=['THUẾ THU NHẬP HỤT 34.000 TỶ', 'AI ĐƯỢC LỢI NHIỀU NHẤT???'], nhan='THUẾ · HỎI THẬT',
 short_caption=('Thu thuế thu nhập cá nhân 2026 ước 203.200 tỷ, thấp hơn dự toán 33.800 tỷ; giảm trừ bản thân 11 lên 15,5 triệu, người phụ thuộc 4,4 lên 6,2 triệu; biểu 7 bậc còn 5 bậc (VnExpress 23/10/2026, Nhân Dân 29/11/2025). '
                'Em tự tính theo biểu thuế, thu nhập sau bảo hiểm: 27 triệu, 1 con – thuế 990 nghìn còn 265 nghìn/tháng; 110 triệu – 24,8 triệu còn 18,85 triệu. '
                'Giảm trừ 11 triệu giữ từ 7/2020 đến hết 2025 (Nghị quyết 954/2020); thu nhập bình quân quý 3/2020 5,79 triệu, quý 3/2025 8,36 triệu, quý 3/2026 9,18 triệu (Cục Thống kê). '
                'Quan điểm cá nhân, không phải tư vấn thuế hay khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='PHẦN ĐỠ THUẾ ĐI ĐÂU?', loi=Q, loi_doc=lib.doc(Q), anh=['Hanoi skyline night', 'Ho Chi Minh City skyline night']),
 canh=[
  C('THU THẤP HƠN 33.800 TỶ', 'Thu thuế thu nhập cá nhân năm nay vừa được Bộ Tài chính dự báo thấp hơn kế hoạch hơn 33 nghìn tỷ đồng. Nguyên nhân được nêu đầu tiên là luật thuế mới đang áp dụng.',
    the=dict(loai='lon', tieu='THUẾ THU NHẬP CÁ NHÂN 2026', nguon='Bộ Tài chính, VnExpress 23/10/2026', dong=[['33.800 TỶ', 118, 'vang'], ['THẤP HƠN DỰ TOÁN', 56, 'trang']])),
  C('GIẢM TRỪ 15,5 TRIỆU', 'Mức giảm trừ cho bản thân tăng từ 11 lên 15,5 triệu đồng mỗi tháng. Mỗi người phụ thuộc tăng từ 4,4 lên 6,2 triệu. Còn biểu thuế thì rút từ 7 bậc xuống 5 bậc.',
    the=dict(loai='cot', tieu='GIẢM TRỪ BẢN THÂN (TRIỆU Đ/THÁNG)', nguon='VnExpress 23/10/2026', hang=[['Năm 2025', 11], ['Năm 2026', 15.5]], noi=[1], dv='', max=18)),
  C('27 TRIỆU, MỘT CON', 'Một người thu nhập sau bảo hiểm 27 triệu, nuôi một con. Năm ngoái nộp 990 nghìn mỗi tháng. Năm nay chỉ còn 265 nghìn. Em tự tính theo biểu thuế.',
    the=dict(loai='cot', tieu='THUẾ MỖI THÁNG, THU NHẬP 27 TRIỆU (NGHÌN Đ)', nguon='Em tự tính theo biểu thuế', hang=[['Năm 2025', 990], ['Năm 2026', 265]], noi=[1], dv='', max=1100)),
  C('110 TRIỆU BỚT GẦN 6 TRIỆU', 'Người thu nhập 110 triệu thì bớt gần 6 triệu mỗi tháng, gấp hơn tám lần. Tính theo tiền, người thu nhập cao được nhiều nhất.',
    the=dict(loai='lon', tieu='THU NHẬP 110 TRIỆU, KHÔNG NGƯỜI PHỤ THUỘC', nguon='Em tự tính theo biểu thuế', dong=[['BỚT 5,95 TRIỆU', 104, 'vang'], ['24,8 TRIỆU CÒN 18,85 TRIỆU', 52, 'trang']])),
  C('NHƯNG THEO PHẦN TRĂM', 'Nhưng tính theo phần trăm thì ngược lại. Thuế của người 27 triệu giảm khoảng 73%. Thuế của người 110 triệu chỉ giảm khoảng 24%.',
    the=dict(loai='cot', tieu='TIỀN THUẾ GIẢM BAO NHIÊU (%)', nguon='Em tự tính theo biểu thuế', hang=[['Thu nhập 27 tr', 73], ['Thu nhập 110 tr', 24]], noi=[0], dv='%', max=80)),
  C('BÌNH QUÂN 9,18 TRIỆU', 'Còn người có thu nhập dưới 11 triệu vốn không nộp thuế thu nhập. Thu nhập bình quân cả nước quý ba năm nay chỉ khoảng chín triệu một trăm tám mươi nghìn đồng. Với họ, lần giảm này không đổi gì.',
    the=dict(loai='lon', tieu='THU NHẬP BÌNH QUÂN THÁNG, QUÝ 3/2026', nguon='Cục Thống kê, WiData', dong=[['9,18 TRIỆU', 118, 'do'], ['DƯỚI MỨC GIẢM TRỪ', 56, 'trang']])),
  C('LẦN TRƯỚC ĐỨNG YÊN 5 NĂM', 'Và phần lợi này sẽ mỏng dần. Lần trước, mức 11 triệu giữ nguyên từ giữa năm 2020 đến hết năm 2025, trong khi thu nhập bình quân tăng khoảng 44%.',
    the=dict(loai='cot', tieu='TĂNG TỪ QUÝ 3/2020 ĐẾN QUÝ 3/2025 (%)', nguon='Nghị quyết 954/2020, Cục Thống kê', hang=[['Mức giảm trừ', 0], ['Thu nhập bình quân', 44.4]], noi=[1], dv='%', max=50)),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.path.insert(0, CW + '/_video'); import kiem_loi
print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
for c in R['canh']: print(c['loi_doc'][:220])
