# -*- coding: utf-8 -*-
# NV1 27/11/2026 – REEL đôi với CH0512TG (tỷ giá lập đỉnh lịch sử). Nguồn + cách tính: xem đầu _video/nv1/ql_ty_gia.py.
import json, os
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261127_0100_reel'
def c(chu_to, loi, the, loi_doc=None): return dict(chu_to=chu_to, loi=loi, loi_doc=loi_doc or loi, anh=[], the=the)
R = dict(key='RV2711TG', tieu_de='Tỷ giá lập đỉnh lịch sử – vậy mà ôm 10.000 đô từ đầu năm, giờ bán lại vẫn lỗ gần 7,5 triệu?',
  hook=['TỶ GIÁ LẬP ĐỈNH', 'ÔM ĐÔ VẪN LỖ???'], nhan='TỶ GIÁ · TÚI TIỀN',
  short_caption=("MarketTimes 25/11/2026: tỷ giá trung tâm 25.679 đồng/USD, cao nhất từng ghi nhận; Vietcombank bán 25.970, giảm 20 đồng. "
     "WiData: giá ngân hàng bán USD 26.377 (31/12/2025), 26.010 (26/11/2026); giá mua 25.630 (26/11); tự do bán 25.880 (16/11), 26.560 (26/11); "
     "2022: 24.879 (31/10/2022), giá mua 23.290 (31/3/2023). Em tự tính: 10.000 USD mua 263,77 triệu, bán 256,3 triệu, lỗ 7,47 triệu; chênh mua bán 380 đồng; 2022 lỗ 15,89 triệu."),
  tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
  canh=[
   c('ĐỈNH LỊCH SỬ MÀ RẺ ĐI?', 'Anh chị có định đổi tiền tiết kiệm sang đô la vì tỷ giá vừa lập đỉnh lịch sử không? Sáng thứ Tư, tỷ giá trung tâm lên hai mươi lăm nghìn sáu trăm bảy mươi chín đồng, cao nhất từ trước tới nay. Nhưng cùng buổi sáng, giá đô ở một ngân hàng lớn lại giảm hai mươi đồng.',
     dict(loai='lon', tieu='SÁNG 25/11/2026', nguon='MarketTimes 25/11/2026', dong=[['TỶ GIÁ TRUNG TÂM 25.679', 66, 'vang'], ['CAO NHẤT LỊCH SỬ', 80, 'do'], ['NGÂN HÀNG BÁN: GIẢM 20 ĐỒNG', 50, 'trang']])),
   c('CÁI CỌC VÀ SỢI DÂY', 'Tỷ giá trung tâm giống cái cọc giữa sân. Ngân hàng được bán đô lệch khỏi cọc tối đa năm phần trăm. Cái lập đỉnh là cái cọc, còn anh chị trả theo giá ngân hàng.',
     dict(loai='chuoi', tieu='ĐỈNH LỊCH SỬ LÀ GIÁ NÀO?', nguon='Ngân hàng Nhà nước · biên độ 5%', buoc=['CỌC: TỶ GIÁ TRUNG TÂM', 'DÂY: LỆCH TỐI ĐA 5%', 'ANH CHỊ TRẢ GIÁ NGÂN HÀNG'], mau=['tim', 'tim', 'vang'])),
   c('GIÁ ĐÔ THẤP HƠN ĐẦU NĂM', 'Theo số liệu WiData, ngày cuối năm ngoái ngân hàng bán đô hai mươi sáu nghìn ba trăm bảy mươi bảy đồng. Hôm thứ Năm chỉ còn hai mươi sáu nghìn không trăm mười đồng.',
     dict(loai='cot', tieu='GIÁ NGÂN HÀNG BÁN 1 ĐÔ (ĐỒNG)', nguon='WiData', hang=[['31/12/2025', 26377], ['26/11/2026', 26010]], noi=[1], dv='')),
   c('ÔM 10.000 ĐÔ: LỖ 7,47 TRIỆU', 'Ai mua mười nghìn đô ngày cuối năm ngoái thì trả gần hai trăm sáu mươi bốn triệu. Hôm thứ Năm bán lại cho ngân hàng, cầm về hai trăm năm mươi sáu triệu ba trăm nghìn. Người đó lỗ gần bảy triệu rưỡi.',
     dict(loai='lon', tieu='MUA 10.000 ĐÔ NGÀY 31/12/2025', nguon='Em tự tính từ giá ngân hàng mua, bán · WiData', dong=[['MUA: 263,77 TRIỆU', 70, 'trang'], ['BÁN: 256,3 TRIỆU', 70, 'vang'], ['LỖ 7,47 TRIỆU', 100, 'do']])),
   c('ĐÔ CŨNG CÓ 2 GIÁ', 'Vì đô la cũng có hai giá như vàng. Hôm thứ Năm, giá ngân hàng bán và giá ngân hàng mua lại cách nhau ba trăm tám mươi đồng. Mua xong bán ngay là mất khoảng một phẩy năm phần trăm.',
     dict(loai='lon', tieu='CHÊNH MUA BÁN NGÀY 26/11', nguon='Em tự tính: 26.010 − 25.630 · WiData', dong=[['380 ĐỒNG MỖI ĐÔ', 96, 'do'], ['10.000 ĐÔ: MẤT 3,8 TRIỆU', 56, 'vang'], ['NGAY KHI VỪA MUA', 50, 'trang']])),
   c('CHỢ ĐEN VỌT 680 ĐỒNG', 'Còn giá đô tự do, chỗ người ta quen gọi là chợ đen, mười ngày qua vọt thêm sáu trăm tám mươi đồng, cao hơn giá ngân hàng tới năm trăm năm mươi đồng mỗi đô.',
     dict(loai='cot', tieu='GIÁ ĐÔ TỰ DO BÁN RA (ĐỒNG)', nguon='WiData', hang=[['16/11/2026', 25880], ['26/11/2026', 26560]], noi=[1], dv='')),
   c('NĂM 2022 ĐỔI SÁT ĐỈNH', 'Năm hai nghìn không trăm hai mươi hai, ai đổi mười nghìn đô cuối tháng mười, sát đỉnh của năm, thì tháng ba năm sau bán lại lỗ gần mười sáu triệu.',
     dict(loai='lon', tieu='LẦN TRƯỚC: NĂM 2022', nguon='Em tự tính từ WiData: 24.879 (31/10/2022), mua lại 23.290 (31/3/2023)', dong=[['10.000 ĐÔ', 70, 'trang'], ['LỖ 15,89 TRIỆU', 96, 'do'], ['SAU 5 THÁNG', 56, 'vang']])),
   c('ĐỔI THEO LỊCH CHI TIÊU', 'Em không đoán tỷ giá. Em tự soi ba dòng: mười hai tháng tới nhà mình phải trả bao nhiêu tiền bằng đô? Đô đang giữ có vượt số đó không? Phần vượt ra chính là phần đặt cược.',
     dict(loai='chuoi', tieu='PHÉP THỬ CỦA HUY NGUYỄN', nguon='Mốc tự soi', buoc=['12 THÁNG TỚI TRẢ BAO NHIÊU ĐÔ?', 'ĐÔ ĐANG GIỮ CÓ VƯỢT?', 'PHẦN VƯỢT LÀ ĐẶT CƯỢC'], mau=['tim', 'tim', 'vang'])),
  ],
  cau_hoi=dict(chu_to='ĐÔ ĐỂ CHI HAY ĐỂ CHỜ?', loi='Số đô nhà anh chị đang giữ là A: để trả một khoản có ngày cụ thể, hay B: để chờ tỷ giá lên?',
     loi_doc='Số đô nhà anh chị đang giữ là A: để trả một khoản có ngày cụ thể, hay B: để chờ tỷ giá lên?', anh=[],
     the=dict(loai='lon', tieu='ĐÔ LA TRONG NHÀ', dong=[['A: ĐỂ CHI TIÊU', 90, 'vang'], ['HAY', 56, 'trang'], ['B: ĐỂ CHỜ GIÁ LÊN?', 76, 'do']])),
  keo_web=dict(chu_to='GIÁ ĐÔ MỖI NGÀY', loi='Giá đô và chỉ số sức mạnh đồng đô, em cập nhật mỗi ngày trên chungkhoanhuynguyen.com.',
     loi_doc='Giá đô và chỉ số sức mạnh đồng đô, em cập nhật mỗi ngày trên chứng khoán Huy Nguyễn chấm com.', anh=[],
     the=dict(loai='lon', tieu='CHUNGKHOANHUYNGUYEN.COM', dong=[[' ', 120, 'trang'], [' ', 120, 'trang'], ['GIÁ ĐÔ MỖI NGÀY', 50, 'vang'], ['XEM MIỄN PHÍ', 50, 'trang']])))
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    import sys; sys.path.insert(0, CW + '/_video')
    print('tu', sum(len(x['loi'].split()) for x in R['canh']) + len(R['cau_hoi']['loi'].split()) + len(R['keo_web']['loi'].split()), 'hook', [len(h) for h in R['hook']])
    import kiem_loi
    for q in kiem_loi.kiem(R['canh'] + [R['cau_hoi']], None, True): print(q)
