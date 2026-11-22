# -*- coding: utf-8 -*-
# NV1 23/11/2026 – REEL câu hỏi lớn, cặp với CH0412PQ (lô 20261123_0100). Nguồn: xem đầu _video/nv1/ql_apec_phu_quoc.py.
#  Nhà Đầu Tư 20/11/2026 (19/11 nhận chủ nhà APEC 2027; 21 dự án 137.138 tỷ; mục tiêu xong trước 30/6/2027); Báo Cần Thơ 13/11/2026 (Bộ Tài chính: giải ngân 7.548 tỷ, 76,02%);
#  MarketTimes 19/11/2026 (Savills: thêm ~11.000 phòng cao cấp 2027–2030, 4–5 sao gần gấp đôi; công suất trên 80%); VietNamNet 24/12/2018 (Vân Đồn 7,2 → 23 triệu/m2; 15/6/2018 luật đặc khu chưa thông qua);
#  VnBusiness 13/2/2019 (Phú Quốc giảm trung bình 30–40% so với đầu 2018). Em tự tính: vay 1,4 tỷ lãi 10% = 140 triệu/năm, 11,7 triệu/tháng.
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__)); import lib
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261123_0100_reel'
sys.path.insert(0, CW + '/_video'); from phat_am import doc as pa
def C(chu, loi, **k):
    d = dict(chu_to=chu, loi=loi, loi_doc=lib.doc(pa(loi))); d.update(k); return d
Q = 'Nếu có một tỷ dành dụm, anh chị có vay thêm để mua đất đảo trước APEC không? Có, không, hay chờ sau sự kiện mới tính?'
R = dict(key='RV2311PQ', tieu_de='APEC 2027 về Phú Quốc: 137.000 tỷ đổ vào đảo – đất sốt lại hay lặp lại năm 2018, khi một năm sau giảm 30–40%?',
 hook=['APEC 2027 VỀ PHÚ QUỐC', 'ĐẤT SỐT LẠI HAY LẶP LẠI 2018???'], nhan='ĐẤT ĐẢO · TÚI TIỀN',
 short_caption=('Việt Nam chính thức nhận vai trò chủ nhà APEC 2027 (19/11), tuần lễ cấp cao ở Phú Quốc: 21 dự án, tổng mức đầu tư sơ bộ 137.138 tỷ đồng, mục tiêu xong trước 30/6/2027 (Nhà Đầu Tư 20/11/2026). '
                'Giải ngân đầu tư công đến 29/10 hơn 7.548 tỷ, 76,02% kế hoạch năm (Bộ Tài chính – Báo Cần Thơ 13/11). Savills: thêm khoảng 11.000 phòng cao cấp 2027–2030, nguồn cung 4–5 sao gần gấp đôi (MarketTimes 19/11). '
                'Lần trước: sốt đất đặc khu 2018, Vân Đồn 7,2 lên 23 triệu/m2; 15/6/2018 luật đặc khu chưa được thông qua (VietNamNet 24/12/2018); đầu 2019 đất Phú Quốc giảm trung bình 30–40% (VnBusiness 13/2/2019). '
                'Em tự tính: vay 1,4 tỷ lãi 10% là khoảng 11,7 triệu tiền lãi mỗi tháng. Quan điểm cá nhân, không phải khuyến nghị đầu tư.'),
 tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
 cau_hoi=dict(chu_to='VAY MUA ĐẤT ĐẢO?', loi=Q, loi_doc=lib.doc(pa(Q)), anh=['Phu Quoc beach', 'Ho Chi Minh City skyline night']),
 canh=[
  C('APEC 2027 VỀ PHÚ QUỐC', 'Việt Nam vừa chính thức nhận vai trò chủ nhà APEC 2027, tuần lễ cấp cao tổ chức ở Phú Quốc. Hai mươi mốt dự án phục vụ sự kiện có tổng vốn sơ bộ hơn 137 nghìn tỷ đồng.',
    the=dict(loai='lon', tieu='21 DỰ ÁN PHỤC VỤ APEC 2027 TẠI PHÚ QUỐC', nguon='Nhà Đầu Tư 20/11/2026', dong=[['137.138 TỶ', 112, 'vang'], ['TỔNG MỨC ĐẦU TƯ SƠ BỘ', 56, 'trang']])),
  C('TIỀN ĐÃ CHI THẬT', 'Khác những cơn sốt trước, tiền đã chi thật. Đến cuối tháng 10, vốn đầu tư công cho các dự án này đã giải ngân hơn 7 nghìn 500 tỷ đồng, khoảng ba phần tư kế hoạch năm.',
    the=dict(loai='lon', tieu='GIẢI NGÂN ĐẦU TƯ CÔNG ĐẾN 29/10/2026', nguon='Bộ Tài chính, Báo Cần Thơ 13/11/2026', dong=[['7.548 TỶ', 120, 'vang'], ['76% KẾ HOẠCH NĂM', 56, 'trang']])),
  C('THÊM 11.000 PHÒNG CAO CẤP', 'Nhưng con số tiếp theo là một cú lật. Một công ty tư vấn bất động sản quốc tế dự báo Phú Quốc thêm khoảng 11 nghìn phòng khách sạn cao cấp đến năm 2030. Nguồn cung bốn đến năm sao gần gấp đôi. Sau APEC, ai lấp đầy?',
    the=dict(loai='lon', tieu='PHÒNG CAO CẤP DỰ KIẾN THÊM 2027 – 2030', nguon='Savills, MarketTimes 19/11/2026', dong=[['11.000 PHÒNG', 112, 'do'], ['4 – 5 SAO GẦN GẤP ĐÔI', 56, 'trang']])),
  C('LẦN TRƯỚC: SỐT ĐẶC KHU 2018', 'Lần trước xảy ra vào năm 2018. Tin luật đặc khu sắp thông qua làm đất sốt. Ở Vân Đồn, nửa năm giá đất trung bình gấp hơn ba lần cùng kỳ.',
    the=dict(loai='cot', tieu='GIÁ ĐẤT TRUNG BÌNH VÂN ĐỒN (TRIỆU ĐỒNG/M2)', nguon='VietNamNet 24/12/2018', hang=[['Cùng kỳ 2017', 7.2], ['6 tháng đầu 2018', 23]], noi=[1], dv='', max=26)),
  C('LUẬT CHƯA THÔNG QUA, GIÁ GIẢM', 'Rồi ngày 15 tháng 6 năm đó, luật đặc khu chưa được thông qua. Đến đầu năm sau, giá đất phần lớn khu vực ở Phú Quốc giảm trung bình từ 30 đến 40% so với đầu năm 2018.',
    the=dict(loai='lon', tieu='ĐẤT PHÚ QUỐC 2/2019 SO VỚI ĐẦU 2018', nguon='VnBusiness 13/2/2019', dong=[['GIẢM 30 – 40%', 104, 'do'], ['CÓ NƠI KHOẢNG MỘT NỬA', 56, 'trang']])),
  C('VAY 1,4 TỶ, LÃI GẦN 12 TRIỆU', 'Em giả định một lô đất 2 tỷ 400 triệu, vay 1 tỷ 400 triệu với lãi suất 10%. Mỗi tháng trả gần 12 triệu đồng tiền lãi, trong khi lô đất không cho thuê thì mang về không đồng.',
    the=dict(loai='cot', tieu='MỖI THÁNG (TRIỆU ĐỒNG, EM GIẢ ĐỊNH)', nguon='Em tự tính', hang=[['Tiền lãi phải trả', 11.7], ['Lô đất mang về', 0]], noi=[0], dv='', max=14)),
  C('TÀI SẢN MANG VỀ BAO NHIÊU?', 'Phép thử của em: đừng tính giá bán lại. Hỏi tài sản đó mỗi tháng mang về bao nhiêu so với tiền lãi. Dưới một nửa, mọi thứ phụ thuộc vào người mua sau.',
    the=dict(loai='lon', tieu='THU MỖI THÁNG SO VỚI TIỀN LÃI', nguon='Mốc em tự đặt, không phải chuẩn chung', dong=[['DƯỚI 50%', 112, 'vang'], ['PHỤ THUỘC NGƯỜI MUA SAU', 52, 'trang']])),
 ])
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    import kiem_loi
    print(R['key'], 'so chu', sum(len(c['loi_doc'].split()) for c in R['canh']) + len(R['cau_hoi']['loi_doc'].split()))
    for q in kiem_loi.kiem(R['canh'], R['cau_hoi'], True): print(q)
    for c in R['canh']: print(c['loi_doc'][:300])
