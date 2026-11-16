# -*- coding: utf-8 -*-
# NV1 17/11/2026 – 2 REEL "câu hỏi lớn" cặp với CH2211VANG (vàng mất 30% từ đỉnh) và CH2311DN (182.000 doanh nghiệp rút lui). Nguồn + cách tính: nv1/ql_vang_dinh.py, nv1/ql_doanh_nghiep.py
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261117_0040_reel'
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(loi)); d.update(k); return d
Q1 = 'Vàng đang chiếm bao nhiêu phần tài sản nhà anh chị: dưới 20%, từ 20 đến 50%, hay trên 50%? Anh chị đang giữ, bán, hay chờ mua thêm?'
R1 = dict(key='RV1711VANG', tieu_de='Vàng mất 30% từ đỉnh: mua 191,3 triệu, giờ tiệm mua lại 134,5 – lần trước năm 2011 phải chờ 9 năm?',
 hook=['VÀNG MẤT 30% TỪ ĐỈNH', 'LẦN TRƯỚC CHỜ 9 NĂM???'], nhan='VÀNG · HỎI THẬT',
 short_caption=('Vàng miếng SJC: đỉnh 191,3 triệu/lượng cuối tháng 1/2026 (Znews 28/5/2026); sáng 16/11 mua vào 134,5 – bán ra 137,5 (MarketTimes 16/11/2026). '
                'Thế giới 5.594,82 USD (29/1) còn 3.875,65 USD (16/11), −30,7% (tự tính). Năm 2011 SJC 49 triệu về khoảng 33 triệu, tới năm 2020 mới vượt đỉnh. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH CẦM BAO NHIÊU?', loi=Q1, loi_doc=lib.doc(Q1), anh=['Hanoi skyline night', 'Ho Chi Minh City skyline night']),
 canh=[
  C('THẤP NHẤT NĂM 2026', 'Sáng nay, giá vàng miếng vừa xuống thấp nhất từ đầu năm 2026. Tiệm chỉ mua lại 134,5 triệu đồng một lượng.',
    the=dict(loai='lon', tieu='VÀNG MIẾNG SÁNG 16/11', nguon='MarketTimes 16/11/2026', dong=[['134,5 TRIỆU', 120, 'do'], ['GIÁ TIỆM MUA VÀO MỖI LƯỢNG', 54, 'trang']])),
  C('ĐỈNH 191,3 TRIỆU', 'Cuối tháng 1, cũng loại vàng đó lập đỉnh 191,3 triệu đồng một lượng. Ai mua đúng đỉnh rồi bán hôm nay mất 56,8 triệu mỗi lượng, em tự tính.',
    the=dict(loai='cot', tieu='VÀNG MIẾNG (TRIỆU ĐỒNG/LƯỢNG)', nguon='Znews 28/5, MarketTimes 16/11/2026', hang=[['Đỉnh tháng 1', 191.3], ['Tiệm mua lại', 134.5]], noi=[1], dv='', max=200)),
  C('THẾ GIỚI MẤT 30,7%', 'Không chỉ trong nước. Vàng thế giới từ đỉnh 5.594 đô la một ounce còn khoảng 3.875 đô la, mất 30,7%, em tự tính.',
    the=dict(loai='lon', tieu='VÀNG THẾ GIỚI TỪ 29/1 TỚI 16/11', nguon='Stockbiz, MarketTimes; em tự tính', dong=[['MẤT 30,7%', 130, 'do'], ['5.594 CÒN 3.875 USD', 56, 'trang']])),
  C('VÌ SAO RƠI?', 'Lý do là nước Mỹ chưa chịu hạ lãi suất. Đồng đô la và lợi suất trái phiếu Mỹ tăng, nên vàng, thứ không sinh lãi, kém hấp dẫn đi.',
    the=dict(loai='lon', tieu='PHÓ CHỦ TỊCH FED NGÀY 14/11', nguon='1thegioi 16/11/2026', dong=[['LẠM PHÁT', 110, 'vang'], ['VẪN LÀ ĐIỀU QUAN TRỌNG NHẤT', 50, 'trang']])),
  C('CAO HƠN THẾ GIỚI 16,4 TRIỆU', 'Cú lật là giá vàng miếng vẫn cao hơn giá thế giới quy đổi khoảng 16,4 triệu đồng mỗi lượng, em tự tính. Phần chênh này có thể co lại.',
    the=dict(loai='cot', tieu='MỖI LƯỢNG SÁNG 16/11 (TRIỆU ĐỒNG)', nguon='MarketTimes, Hà Nội Mới; em tự tính', hang=[['Giá thế giới', 121.1], ['Vàng miếng', 137.5]], noi=[1], dv='', max=150)),
  C('2011: CHỜ 9 NĂM', 'Lần trước, năm 2011, vàng miếng lập đỉnh 49 triệu rồi về khoảng 33 triệu. Phải tới năm 2020, giá mới vượt lại đỉnh cũ.',
    the=dict(loai='cot', tieu='VÀNG MIẾNG (TRIỆU ĐỒNG/LƯỢNG)', nguon='Tinnhanhchungkhoan 2/6/2016', hang=[['Đỉnh 8/2011', 49], ['Năm 2016', 33]], noi=[1], dv='', max=60)),
  C('ĐỪNG VAY MUA THÊM', 'Người mất nhiều nhất năm 2011 là người phải bán vàng đúng lúc giá thấp. Vay tiền mua thêm thứ không sinh lãi là cách biến khoản lỗ chờ được thành khoản lỗ không chờ được.',
    the=dict(loai='lon', tieu='BÀI HỌC NĂM 2011', nguon='Quan điểm cá nhân', dong=[['KHÔNG VAY', 120, 'vang'], ['ĐỂ KHÔNG PHẢI BÁN ĐÁY', 56, 'trang']])),
 ])
Q2 = 'Quỹ dự phòng của nhà anh chị đủ sống dưới 3 tháng, từ 3 đến 6 tháng, hay trên 6 tháng? Năm nay chỗ anh chị làm có thấy đơn hàng ít đi không?'
R2 = dict(key='RV1711DN', tieu_de='182.000 doanh nghiệp rút lui trong 10 tháng, gần 600 mỗi ngày – kinh tế đang bệnh hay đang dọn sổ?',
 hook=['182.000 DOANH NGHIỆP RÚT LUI', 'KINH TẾ ĐANG BỆNH???'], nhan='KINH TẾ · HỎI THẬT',
 short_caption=('10 tháng 2026: tạm ngừng 92,0 nghìn, chờ giải thể 33,7 nghìn, giải thể 56,3 nghìn (+109,8%) – tổng 182,0 nghìn (tự cộng); thành lập mới và quay lại hơn 243,6 nghìn '
                '(Cục Thống kê, Thị trường Tài chính Tiền tệ 3/11/2026). Giải thể bán buôn, bán lẻ, sửa chữa ô tô xe máy 21.673 (Nhà đầu tư/VCCI 9/11/2026). Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='NHÀ MÌNH ĐỦ MẤY THÁNG?', loi=Q2, loi_doc=lib.doc(Q2), anh=['Ho Chi Minh City skyline night', 'Hanoi skyline night']),
 canh=[
  C('182.000 DOANH NGHIỆP', 'Cục Thống kê vừa công bố: 10 tháng đầu năm nay, cộng lại có 182.000 doanh nghiệp rút lui khỏi thị trường. Gần 600 công ty mỗi ngày, em tự tính.',
    the=dict(loai='lon', tieu='RÚT LUI 10 THÁNG 2026', nguon='Cục Thống kê, báo Thị trường Tài chính Tiền tệ 3/11/2026', dong=[['182.000', 130, 'do'], ['GẦN 600 MỖI NGÀY', 60, 'trang']])),
  C('GIẢI THỂ GẤP ĐÔI', 'Trong đó 56.300 doanh nghiệp đã giải thể hẳn, tăng 109,8% so với cùng kỳ. Nghe rất đáng sợ.',
    the=dict(loai='lon', tieu='HOÀN TẤT GIẢI THỂ 10 THÁNG', nguon='Cục Thống kê, 3/11/2026', dong=[['56.300', 130, 'do'], ['TĂNG 109,8%', 60, 'trang']])),
  C('NHƯNG CHỜ GIẢI THỂ GIẢM', 'Nhưng số tạm ngừng lại giảm 12,7%, số chờ giải thể giảm 42,3%. Nếu kinh tế tệ đi đều, lẽ ra cả ba nhóm phải cùng tăng.',
    the=dict(loai='cot', tieu='SO VỚI CÙNG KỲ (%)', nguon='Cục Thống kê, 3/11/2026', hang=[['Tạm ngừng', -12.7], ['Chờ giải thể', -42.3], ['Đã giải thể', 109.8]], noi=[2], dv='%')),
  C('DỌN HỒ SƠ CŨ', 'Cơ quan quản lý giải thích: một phần là rà soát dữ liệu, xử lý hồ sơ tồn đọng. Nhiều công ty đã ngừng từ những năm trước, nay mới làm xong thủ tục.',
    the=dict(loai='lon', tieu='VÌ SAO GIẢI THỂ TĂNG VỌT?', nguon='Nhà đầu tư, VCCI 9/11/2026', dong=[['DỌN SỔ', 120, 'vang'], ['LÀM SẠCH MÃ SỐ THUẾ 2026', 52, 'trang']])),
  C('VÀO VẪN NHIỀU HƠN RA', 'Cũng trong 10 tháng, hơn 243.600 doanh nghiệp thành lập mới và quay lại. Số vào vẫn nhiều hơn số ra khoảng 61.600, em tự tính.',
    the=dict(loai='cot', tieu='10 THÁNG 2026 (NGHÌN DOANH NGHIỆP)', nguon='Cục Thống kê; em tự tính', hang=[['Vào thị trường', 243.6], ['Rút lui', 182.0]], noi=[0], dv='', max=260)),
  C('CỬA HÀNG NHỎ ĐAU NHẤT', 'Nhưng chỗ đau là thật. Riêng bán buôn, bán lẻ và sửa chữa xe đã có 21.673 doanh nghiệp giải thể. Áp lực dồn vào doanh nghiệp nhỏ: thiếu đơn hàng, sức mua yếu, lãi vay cao.',
    the=dict(loai='lon', tieu='GIẢI THỂ NHIỀU NHẤT', nguon='Nhà đầu tư, VCCI 9/11/2026', dong=[['21.673', 120, 'do'], ['BÁN BUÔN, BÁN LẺ, XE CỘ', 54, 'trang']])),
  C('CÔNG TY TO HƠN, ÍT NGƯỜI HƠN', 'Còn công ty mới thì to hơn nhưng tuyển ít người hơn. Vốn bình quân tăng 34,8%, nhưng lao động đăng ký giảm 17,4%.',
    the=dict(loai='cot', tieu='DOANH NGHIỆP MỚI, SO CÙNG KỲ (%)', nguon='Cục Thống kê, 3/11/2026', hang=[['Vốn mỗi công ty', 34.8], ['Lao động', -17.4]], noi=[1], dv='%')),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R1, R2], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sys.path.insert(0, CW + '/_video'); import kiem_loi
for R in (R1, R2):
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True):
        if 'câu cụt' not in q: print(q)
