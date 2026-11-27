# -*- coding: utf-8 -*-
# Reel dọc RV2811MM – đi kèm CH0112MM (NV1 28/11/2026). Nguồn: xem ql_my_mua_gi.py.
import json, os
CW = os.environ.get('CW', '/tmp/cw'); LO = CW + '/_video/queue/20261128_0100_reel'
def c(chu, loi, the): return dict(chu_to=chu, loi=loi, loi_doc=loi, anh=[], the=the)
CANH = [
 c("BÁN 159 TỶ, MUA 19 TỶ", "Nhà anh chị có ai làm ở xưởng may, xưởng giày không? Mười tháng năm nay, Việt Nam vừa bán sang Mỹ hơn một trăm năm mươi chín tỷ đô hàng hoá, nhưng chỉ mua lại của Mỹ hơn mười chín tỷ.",
   dict(loai='cot', tieu='VIỆT NAM VÀ MỸ, 10 THÁNG 2026 (TỶ USD)', nguon='Báo Đầu tư 4/11/2026 · WiData', hang=[['Bán sang Mỹ', 159.4], ['Mua của Mỹ', 19.27]], noi=[0], dv='')),
 c("MỸ ĐỀ XUẤT THUẾ TỚI 35%", "Bán ra gấp hơn tám lần mua vào. Ngày hai mươi lăm tháng mười một, Mỹ đề xuất xem xét thuế tới ba mươi lăm phần trăm với hàng Việt Nam, hai mươi phần trăm nếu có thoả thuận.",
   dict(loai='lon', tieu='ĐỀ XUẤT CỦA MỸ 25/11/2026', nguon='Thông cáo Văn phòng Đại diện Thương mại Mỹ 25/11/2026', dong=[['THUẾ TỚI 35%', 100, 'do'], ['CÓ THỎA THUẬN: 20%', 60, 'vang'], ['GÓP Ý ĐẾN 5/1/2027', 50, 'trang']])),
 c("MỸ BÁN GÌ CHO TA?", "Hàng Mỹ vào Việt Nam nhiều nhất là linh kiện điện tử, gần sáu tỷ đô. Đứng sau là bông và máy móc. Phần lớn là đồ để sản xuất tiếp, không phải táo nho trong siêu thị.",
   dict(loai='cot', tieu='HÀNG MỸ VÀO VIỆT NAM, 10 THÁNG (TỶ USD)', nguon='WiData', hang=[['Điện tử', 5.88], ['Bông', 1.52], ['Máy móc', 1.48]], noi=[0], dv='')),
 c("90 MÁY BAY VẪN CHƯA ĐỦ", "Các hãng bay Việt đã ký mua chín mươi máy bay Boeing, hơn ba mươi tỷ đô, giao trong nhiều năm. Cả hợp đồng ấy chỉ bằng khoảng hai mươi hai phần trăm con số chênh của riêng mười tháng.",
   dict(loai='lon', tieu='HỢP ĐỒNG 2/2026, GIAO NHIỀU NĂM', nguon='Reuters 19/2/2026 · em tự tính 30,6 chia 140,13', dong=[['90 MÁY BAY: 30,6 TỶ USD', 60, 'trang'], ['CHÊNH 10 THÁNG: 140 TỶ', 60, 'vang'], ['CHỈ BẰNG 22%', 100, 'do']])),
 c("AI ĐANG BÁN SANG MỸ?", "Tính chung cả nước chín tháng, doanh nghiệp vốn nước ngoài chiếm gần tám mươi mốt phần trăm xuất khẩu. Hàng đi Mỹ nhiều nhất là điện tử, máy móc. Sổ sách là của họ, nhưng người đứng máy là người Việt.",
   dict(loai='lon', tieu='XUẤT KHẨU CẢ NƯỚC 9 THÁNG 2026', nguon='Cục Thống kê, họp báo 7/10/2026', dong=[['80,7%', 130, 'do'], ['KHU VỰC VỐN NƯỚC NGOÀI', 56, 'vang'], ['KỂ CẢ DẦU THÔ', 50, 'trang']])),
 c("DỆT MAY, GIÀY BỊ NÊU TÊN", "Dệt may bán sang Mỹ hơn mười lăm tỷ đô, giày dép gần tám tỷ, cả hai có tên trong đề xuất. Đơn hàng chậm lại thì tăng ca thường bị cắt trước.",
   dict(loai='cot', tieu='BÁN SANG MỸ, 10 THÁNG (TỶ USD)', nguon='WiData', hang=[['Dệt may', 15.36], ['Giày dép', 7.92], ['Gỗ', 7.58]], noi=[0, 1], dv='')),
 c("THU NHẬP QUA CỬA MỸ?", "Em tự soi một phép thử: thu nhập nhà mình bao nhiêu phần trăm đi qua đơn hàng Mỹ? Trên ba mươi phần trăm thì để dành đủ sáu tháng chi tiêu, hoãn khoản vay chưa cần.",
   dict(loai='chuoi', tieu='PHÉP THỬ MỘT CÁNH CỬA', nguon='Mốc tự soi', buoc=['DƯỚI 30%: THEO DÕI TIN', '30 ĐẾN 60%: ĐỂ DÀNH, HOÃN VAY', 'TRÊN 60%: KHÔNG VAY MỚI'], mau=['tim', 'vang', 'do'])),
]
R = [dict(key='RV2811MM', tieu_de='Bán sang Mỹ 159 tỷ đô, mua lại 19 tỷ – Mỹ muốn Việt Nam mua gì, và thuế 35% chạm túi ai?',
  hook=['BÁN 159 TỶ, MUA 19 TỶ', 'MỸ MUỐN TA MUA GÌ???'], nhan='VIỆT NAM – MỸ · TÚI TIỀN',
  short_caption=("Báo Đầu tư 4/11/2026: 10 tháng 2026 xuất sang Mỹ 159,40 tỷ USD (+26,2%). WiData: nhập từ Mỹ 19,27 tỷ USD; điện tử 5,88; bông 1,52; máy móc 1,48; dệt may sang Mỹ 15,36; giày dép 7,92; gỗ 7,58 tỷ USD. "
                 "USTR 25/11/2026: xem xét thuế tới 35%, 20% nếu có thoả thuận. Reuters 19/2/2026: 90 máy bay Boeing, 8,1 + 22,5 = 30,6 tỷ USD. Cục Thống kê: 9 tháng khu vực vốn nước ngoài chiếm 80,7% xuất khẩu. Em tự tính: chênh 140,13 tỷ; 30,6/140,13 = 22%."),
  tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1, canh=CANH,
  cau_hoi=c("NHÀ CÓ AI LÀM XƯỞNG HÀNG ĐI MỸ?", "Nhà anh chị có ai đang làm cho xưởng hàng đi Mỹ không? Kể em nghe ở phần bình luận nhé.",
            dict(loai='lon', tieu='CÂU HỎI CHO ANH CHỊ', dong=[['NHÀ CÓ AI LÀM', 76, 'vang'], ['XƯỞNG HÀNG ĐI MỸ?', 76, 'do']])),
  keo_web=dict(chu_to='TỶ GIÁ, VĨ MÔ MỖI NGÀY', loi='Tỷ giá, lãi suất và số liệu thế giới, em cập nhật mỗi ngày trên chungkhoanhuynguyen.com.',
            loi_doc='Tỷ giá, lãi suất và số liệu thế giới, em cập nhật mỗi ngày trên chứng khoán Huy Nguyễn chấm com.', anh=[],
            the=dict(loai='lon', tieu='CHUNGKHOANHUYNGUYEN.COM', dong=[[' ', 120, 'trang'], [' ', 120, 'trang'], ['VĨ MÔ MỖI NGÀY', 50, 'vang'], ['XEM MIỄN PHÍ', 50, 'trang']])))]
os.makedirs(LO, exist_ok=True)
json.dump(R, open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    import sys; sys.path.insert(0, CW + '/_video'); import kiem_loi
    n = sum(len(x['loi'].split()) for x in CANH) + len(R[0]['cau_hoi']['loi'].split()) + len(R[0]['keo_web']['loi'].split())
    print('so tu', n, 'hook', [len(h) for h in R[0]['hook']])
    for q in kiem_loi.kiem([{"loi": x['loi']} for x in CANH + [R[0]['cau_hoi']]], None, False): print(q)
