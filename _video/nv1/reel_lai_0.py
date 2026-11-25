# -*- coding: utf-8 -*-
# NV1 26/11/2026 – REEL dọc đi cặp CH0112NH "Mua nhà lãi suất 0%". 100% thẻ đồ hoạ the_so ("anh": []), mở bài hỏi thẳng anh chị (LUẬT SỐNG A1, A3).
# Nguồn: CafeBiz 25/11/2026 (theo Nhịp sống thị trường); CafeF 18/11/2026 (CBRE Hà Nội quý 3/2026); TheLEADER 23/11/2026. Tự tính: 3,7−3,4=0,3; 2,7×15%÷12≈34 triệu; 2,7÷3,7=73%.
import os, sys, json
CW = os.environ.get('CW', '/tmp/cw'); sys.path.insert(0, CW + '/_video')
LO = CW + '/_video/queue/20261126_0100_reel'
def c(chu_to, loi, the): return dict(chu_to=chu_to, loi=loi, loi_doc=loi, anh=[], the=the)
NG = 'CafeBiz 25/11/2026'
CANH = [
 c('GÓP 1 TỶ, MẤT 700 TRIỆU', "Anh chị có dám ký mua nhà, khi người bán hứa hai năm đầu chưa phải trả đồng lãi nào không? Báo vừa đăng chuyện một người ở Hà Nội đã ký như thế. Anh góp một tỷ đồng. Gần hai năm sau, nếu bán, một tỷ ấy mất hơn bảy trăm triệu.",
   dict(loai='lon', tieu='MUA NHÀ GÓI LÃI SUẤT 0%', nguon='Phép tính của người mua · ' + NG, dong=[['GÓP 1 TỶ', 84, 'trang'], ['MẤT HƠN 700 TRIỆU', 104, 'do'], ['NẾU BÁN BÂY GIỜ', 56, 'vang']])),
 c('CĂN NHÀ CÓ 2 GIÁ', "Đầu năm hai nghìn không trăm hai mươi lăm, anh mua căn hộ giá ba tỷ bảy trăm triệu, theo gói lãi suất bằng không. Cũng căn đó, nếu trả thẳng thì chỉ ba tỷ bốn trăm triệu. Ba trăm triệu chênh ấy chính là tiền lãi, chỉ là nó đổi tên.",
   dict(loai='cot', tieu='GIÁ CÙNG MỘT CĂN HỘ (TỶ ĐỒNG)', nguon=NG, hang=[['Gói lãi 0%', 3.7], ['Trả thẳng', 3.4]], noi=[1], dv='')),
 c('NỢ VẪN NGUYÊN 2,7 TỶ', "Anh trả trước một tỷ, còn nợ hai tỷ bảy trăm triệu. Suốt hai năm ưu đãi, anh chưa trả đồng nào trong số tiền vay, nên khoản nợ vẫn còn nguyên.",
   dict(loai='chuoi', tieu='HAI NĂM ĐẦU DỄ THỞ', nguon=NG, buoc=['TRẢ TRƯỚC 1 TỶ', 'NỢ 2,7 TỶ, LÃI 0% HAI NĂM', 'HẾT ƯU ĐÃI: NỢ CÒN NGUYÊN'], mau=['tim', 'tim', 'vang'])),
 c('34 TRIỆU TIỀN LÃI MỖI THÁNG', "Đầu năm tới, ưu đãi hết. Anh tự giả định lãi suất lúc đó là mười lăm phần trăm mỗi năm. Em tính giúp: riêng tiền lãi đã khoảng ba mươi tư triệu đồng mỗi tháng.",
   dict(loai='dem', tieu='TIỀN LÃI KHI HẾT ƯU ĐÃI', nguon='Em tự tính: 2,7 tỷ × 15% ÷ 12 · giả định của người mua, ' + NG, n=34, to='34 TRIỆU MỖI THÁNG', phu='NẾU LÃI 15% MỖI NĂM')),
 c('NHÀ CÒN HƠN 3 TỶ', "Muốn bán thì căn nhà giờ chỉ còn khoảng hơn ba tỷ. Trả ngân hàng hai tỷ bảy trăm triệu, cộng phí trả nợ sớm, anh cầm về chưa tới ba trăm triệu.",
   dict(loai='lon', tieu='NẾU BÁN NGAY BÂY GIỜ', nguon='Phép tính của người mua · ' + NG, dong=[['NHÀ CÒN HƠN 3 TỶ', 84, 'vang'], ['NỢ NGUYÊN 2,7 TỶ', 96, 'do'], ['CẦM VỀ CHƯA TỚI 300 TRIỆU', 50, 'trang']])),
 c('GIÁ CĂN HỘ CŨ QUAY ĐẦU', "Và giá đang quay đầu thật. Ở Hà Nội, giá rao căn hộ cũ quý ba thấp hơn năm trước khoảng tám phần trăm. Đây là lần đầu, sau hai năm tăng hơn hai mươi lăm phần trăm mỗi năm.",
   dict(loai='cot', tieu='GIÁ RAO CĂN HỘ CŨ HÀ NỘI (%)', nguon='CBRE qua CafeF 18/11/2026 · TheLEADER 23/11/2026', hang=[['2 năm trước, mỗi năm', 25], ['Quý 3/2026 so năm trước', -8]], noi=[1], dv='%')),
 c('CÁI BẪY LÀ VAY 73%', "Gói không lãi tự nó không đắt. Cái nguy hiểm là hai năm đầu chưa phải trả gì, nên anh dám vay tới bảy mươi ba phần trăm giá nhà. Giá vừa quay đầu là tiền của anh mất trước, còn khoản nợ vẫn nguyên.",
   dict(loai='lon', tieu='TIỀN VAY TRÊN GIÁ NHÀ', nguon='Em tự tính: 2,7 ÷ 3,7 · ' + NG, dong=[['VAY 73% GIÁ NHÀ', 100, 'do'], ['GIÁ GIẢM', 60, 'trang'], ['NỢ KHÔNG GIẢM', 60, 'vang']])),
 c('3 DÒNG TRƯỚC KHI KÝ', "Trước khi ký một gói không lãi, em tự tính ba dòng. Giá trả thẳng là bao nhiêu? Hết ưu đãi, mỗi tháng trả mấy triệu? Và nếu thu nhập giảm ba mươi phần trăm, nhà mình còn trả nổi không?",
   dict(loai='chuoi', tieu='PHÉP THỬ CỦA HUY NGUYỄN', nguon='Mốc tự soi', buoc=['GIÁ TRẢ THẲNG?', 'HẾT ƯU ĐÃI TRẢ MẤY TRIỆU?', 'THU NHẬP GIẢM 30% CÒN TRẢ NỔI?'], mau=['tim', 'tim', 'vang'])),
]
Q = "Nếu là người mua, anh chị A: ký ngay để giữ ưu đãi, hay B: hỏi giá trả thẳng trước?"
W = "Bảng tính ba dòng này, em viết từng bước trên chứng khoán Huy Nguyễn chấm com."
R = dict(key='RV2611NH', tieu_de='Mua nhà lãi suất 0%: góp 1 tỷ, gần 2 năm sau bán là mất hơn 700 triệu – tiền đi đâu?',
    hook=['GÓP 1 TỶ MUA NHÀ', 'MẤT 700 TRIỆU???'], nhan='NHÀ ĐẤT · TÚI TIỀN',
    short_caption=("Theo CafeBiz 25/11/2026 (dẫn Nhịp sống thị trường): căn hộ ở Hà Nội mua đầu 2025 giá 3,7 tỷ theo gói lãi 0% trong 2 năm, trả trước 1 tỷ; giá trả thẳng 3,4 tỷ; "
                   "căn nay còn khoảng hơn 3 tỷ; người mua tự tính lỗ hơn 700 triệu trên 1 tỷ vốn nếu bán; mức lãi 15% là giả định của người mua. "
                   "CBRE (CafeF 18/11/2026): giá chào căn hộ thứ cấp Hà Nội quý 3/2026 giảm 8% so với cùng kỳ; TheLEADER 23/11/2026: hai năm trước đó tăng hơn 25% mỗi năm. "
                   "Em tự tính: 3,7 − 3,4 = 0,3 tỷ; 2,7 tỷ × 15% ÷ 12 ≈ 34 triệu; 2,7 ÷ 3,7 = 73%."),
    tags=[], toc=1.1, nhac='lofi', music_db=-2, hieu_ung=1,
    cau_hoi=dict(chu_to='KÝ NGAY HAY HỎI GIÁ?', loi=Q, loi_doc=Q, anh=[], the=dict(loai='lon', tieu='GÓI MUA NHÀ LÃI 0%', dong=[['A: KÝ NGAY', 100, 'vang'], ['HAY', 56, 'trang'], ['B: HỎI GIÁ TRẢ THẲNG?', 76, 'do']])),
    canh=CANH,
    keo_web=dict(chu_to='BẢNG TÍNH 3 DÒNG', loi="Bảng tính ba dòng này, em viết từng bước trên chungkhoanhuynguyen.com.", loi_doc=W, anh=[],
                 the=dict(loai='lon', tieu='CHUNGKHOANHUYNGUYEN.COM', dong=[[' ', 120, 'trang'], [' ', 120, 'trang'], ['BẢNG TÍNH 3 DÒNG', 50, 'vang'], ['XEM MIỄN PHÍ', 50, 'trang']])))
os.makedirs(LO, exist_ok=True)
json.dump([R], open(LO + '/reel.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if __name__ == '__main__':
    import kiem_loi
    print('tu', sum(len(x['loi'].split()) for x in CANH), 'hook', [len(h) for h in R['hook']])
    print(kiem_loi.kiem(CANH, R['cau_hoi'], True))
