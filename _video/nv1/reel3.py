# -*- coding: utf-8 -*-
# NV1 10/11/2026: 2 reel "Chuyện mã hôm nay" (phiên 9/11/2026) – PNJ, nhóm chứng khoán. Số liệu data/c, kqkd, fund.
import json, sys
from lib import *
def C(chu, loi, anh=None, the=None, **kw):
    d = {'chu_to': chu, 'loi': loi, 'loi_doc': doc(loi)}
    if anh: d['anh'] = anh
    if the: d['the'] = the
    d.update(kw); return d
def Q(chu, loi): return {'chu_to': chu, 'loi': loi, 'loi_doc': doc(loi)}
CAP = " Quan điểm cá nhân, không phải khuyến nghị đầu tư."
f = fund('PNJ')
R1 = dict(key='CM1011A', tieu_de="PNJ rơi 83% từ đỉnh 52 tuần, quý 3 lỗ 257 tỷ: cổ tức 10% là quà hay bẫy?", hook=["PNJ RƠI 83%", "CỔ TỨC 10% LÀ QUÀ?"],
  nhan="CHUYỆN MÃ HÔM NAY", short_caption="PNJ phiên 9/11 giảm 5,65% còn 14.200 đồng, thấp hơn đỉnh 52 tuần khoảng 83%. Quý 3 lỗ 257 tỷ, tỷ suất cổ tức nhìn lên hơn 10%. Rẻ thật hay bẫy cổ tức?" + CAP,
  tags=[], keo_web=None, toc=1.12, nhac='lofi', music_db=-2, hieu_ung=1,
  cau_hoi=Q("ANH CHỊ NGHĨ SAO?", "Theo anh chị, tỷ suất cổ tức hơn 10% của PNJ là món quà hay cái bẫy? Bình luận cho em biết nhé."),
  canh=[
   C("PNJ RƠI 83%", "Đầu năm, PNJ còn giao dịch quanh 80 nghìn đồng. Phiên 9/11, PNJ giảm 5,65%, đóng cửa 14.200 đồng, đúng đáy 52 tuần. Vàng thì sáng, mà cổ phiếu tiệm vàng lại tối thui. Anh chị có biết chuyện gì đang xảy ra với PNJ không?", anh=["jewelry store", "gold jewelry display"], chat=1),
   C("QUÝ 3 LỖ 257 TỶ", "Câu trả lời nằm trong báo cáo quý 3. Doanh thu thuần 6.995 tỷ, giảm 14%. Lợi nhuận sau thuế công ty mẹ chuyển từ lãi sang lỗ 257 tỷ đồng. Lũy kế chín tháng chỉ còn 472 tỷ, giảm 70,7%.",
     the={'loai': 'cot', 'tieu': 'PNJ QUÝ 3/2026 SO VỚI CÙNG KỲ', 'nguon': 'BCTC quý 3/2026', 'hang': [['Doanh thu', -14.0], ['LN 9 tháng', -70.7]], 'noi': [1], 'dv': '%', 'max': 80}),
   C("P/E 4,56 MÀ RẺ?", "Nhìn bảng chỉ số, P trên E chỉ 4,56 lần, P trên B 0,58 lần, nghe như hàng giảm giá. Nhưng P trên E vẫn đang tính những quý lãi đẹp của năm trước. Lợi nhuận đã lao dốc thì con số rẻ ấy có thể chỉ là ảo giác.",
     the={'loai': 'lon', 'tieu': 'CHỈ SỐ NGÀY 9/11', 'nguon': 'Dữ liệu thị trường', 'dong': [['P/E 4,56', 76, 'vang'], ['P/B 0,58', 76, 'trang'], ['QUÝ 3 LỖ 257 TỶ', 60, 'do']]}),
   C("CỔ TỨC 10% LÀ QUÀ?", "Tỷ suất cổ tức nhìn lên 10,54%, gấp đôi lãi tiết kiệm. Nhưng tỷ suất cao lên chủ yếu vì giá rơi, chứ không phải vì công ty trả nhiều hơn. Cổ tức năm sau còn được như cũ hay không phải chờ hội đồng quản trị công bố.", anh=["cash envelope", "calculator coins"]),
   C("NHÀ ĐẦU TƯ NHỎ LẺ", "Với nhà đầu tư nhỏ lẻ, bài học là giá giảm sâu chưa phải lý do để mua. Trước khi bắt đáy, anh chị cần thấy lợi nhuận quý sau quay lại tăng, và dòng tiền kinh doanh dương trở lại.",
     the={'loai': 'lon', 'tieu': 'TRƯỚC KHI BẮT ĐÁY', 'nguon': '', 'dong': [['LÃI QUÝ SAU TĂNG?', 62, 'vang'], ['DÒNG TIỀN DƯƠNG?', 62, 'trang'], ['CỔ TỨC CÒN GIỮ?', 62, 'tim2']]}),
  ])
L = {s: KQ[s]['info'][0] for s in ['SSI', 'VND', 'HCM', 'VCI', 'VIX']}
R2 = dict(key='CM1011B', tieu_de="VND tăng 14,6% trong 3 phiên rồi quay đầu: 5 công ty chứng khoán lớn đều báo lãi quý 3 giảm", hook=["VND +14,6% 3 PHIÊN", "RỒI QUAY ĐẦU?"],
  nhan="CHUYỆN MÃ HÔM NAY", short_caption="VND tăng 14,6% trong 3 phiên, phiên 9/11 quay đầu giảm 3,34%. SSI, VND, HCM, VCI, VIX đều báo lãi quý 3 giảm so với cùng kỳ. Sóng chứng khoán đang chạy bằng gì?" + CAP,
  tags=[], keo_web=None, toc=1.12, nhac='lofi', music_db=-2, hieu_ung=1,
  cau_hoi=Q("ANH CHỊ CÓ ĐU?", "Ba phiên VND tăng vừa rồi, anh chị đứng ngoài hay đã nhảy vào? Bình luận cho em biết nhé."),
  canh=[
   C("VND +14,6% 3 PHIÊN", "Ba phiên từ 4 đến 6/11, VND tăng một mạch từ 13.050 lên 14.950 đồng, tức 14,6%. Sang phiên 9/11, cổ phiếu quay đầu giảm 3,34%, còn 14.450 đồng. Lên bằng thang máy, xuống cũng chẳng cần cầu thang.", anh=["stock trading screen", "stock market chart"], chat=1),
   C("CẢ NHÓM ĐỎ", "Không chỉ VND. Phiên 9/11, SSI giảm 2,45%, VIX giảm 2,62%, VN-Index mất 0,64% còn khoảng 1.714 điểm. Nhóm chứng khoán vốn nhạy với thị trường, nên thường đi trước khi tâm lý đổi chiều.", anh=["red stock board"]),
   C("5 ANH EM CÙNG LÙI", "Điều đáng chú ý nằm ở báo cáo quý 3. Cả năm công ty chứng khoán lớn đều báo lãi giảm so với cùng kỳ. SSI giảm 23,7%. VCI giảm 12,6%. HCM giảm 32,5%. VND giảm 64,5%. VIX giảm tới 92,9%.",
     the={'loai': 'cot', 'tieu': 'LÃI QUÝ 3/2026 SO VỚI CÙNG KỲ', 'nguon': 'BCTC quý 3/2026', 'hang': [['SSI', -23.7], ['VCI', -12.6], ['HCM', -32.5], ['VND', -64.5], ['VIX', -92.9]], 'noi': [4], 'dv': '%', 'max': 100}),
   C("GIÁ TĂNG, LÃI GIẢM", "Giá tăng trong khi lãi giảm nghĩa là thị trường đang trả tiền cho kỳ vọng, chẳng hạn kỳ vọng thanh khoản quay lại. Kỳ vọng đúng thì không sao. Kỳ vọng hụt thì mức giảm có thể nhanh như lúc tăng.", anh=["balance scale"]),
   C("NHÀ ĐẦU TƯ NHỎ LẺ", "Với nhà đầu tư nhỏ lẻ, ba phiên tăng mạnh là lúc dễ mua đuổi nhất. Trước khi vào lệnh, anh chị hỏi ba câu: lợi nhuận quý gần nhất ra sao, mình mua vì số liệu hay vì sợ lỡ, và nếu giá giảm 10% thì mình làm gì.",
     the={'loai': 'lon', 'tieu': 'TRƯỚC KHI MUA ĐUỔI', 'nguon': '', 'dong': [['LÃI QUÝ GẦN NHẤT?', 60, 'vang'], ['MUA VÌ SỐ HAY VÌ SỢ?', 54, 'trang'], ['GIẢM 10% LÀM GÌ?', 60, 'do']]}),
  ])
json.dump([R1, R2], open(sys.argv[1], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print([L, f['dy'], f['h52'], close('VNINDEX'), daily('VNINDEX')[-2][4]])
