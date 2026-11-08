# -*- coding: utf-8 -*-
# NV1 lô 20261109_0040: kênh chính 26–28/11 + kênh phụ 16–17/11. Dùng: CW=/tmp/cw python3 build2.py <lô> [--ghi]
import json, sys, os
import gen
gen.TEN.update({'SAB': 'Sabeco', 'HAH': 'Vận tải Hải An', 'MSN': 'Masan', 'POW': 'PV Power', 'NLG': 'Nam Long', 'DXG': 'Đất Xanh', 'NT2': 'Điện lực Nhơn Trạch 2', 'NKG': 'Thép Nam Kim',
                'MBB': 'MB', 'HPG': 'Hòa Phát', 'HSG': 'Hoa Sen', 'VCB': 'Vietcombank', 'BID': 'BIDV', 'CTG': 'VietinBank'})
gen.ANH.update({'SAB': 'beer brewery', 'BMP': 'plastic pipes factory', 'HAH': 'container ship', 'DCM': 'fertilizer plant', 'MSN': 'supermarket shelves', 'POW': 'gas power plant',
                'NLG': 'residential buildings Vietnam', 'DXG': 'apartment construction', 'NT2': 'gas power plant', 'NKG': 'steel coils', 'MBB': 'bank building', 'HPG': 'steel mill', 'HSG': 'steel roofing sheets'})
from gen import *
import build as B
from hand2 import H2
import hand; hand.H.update(H2)
LO = sys.argv[1]
def them_k2(sc, syms, nhom):
    def L(s): return [noi(x) for x in KQ[s]['info'][:3]]
    say = ("Trước khi kết luận, em đặt thêm các con số lũy kế cạnh nhau, vì một quý có thể bị méo bởi khoản bất thường. " +
           " ".join("Mã %s. %s" % (s, " ".join(L(s))) for s in syms) +
           " Nhìn cả chín tháng, anh chị sẽ thấy mã nào tăng trưởng đều, mã nào chỉ có một quý đột biến. Trong nhóm {NHOM}, một quý đẹp chưa đủ để kết luận; ba quý liên tiếp cùng chiều mới là tín hiệu đáng tin hơn. "
           "Ví von đời thường: một trận thắng đậm chưa nói lên phong độ, cả mùa giải mới nói lên phong độ.").replace("{NHOM}", nhom)
    sc.insert(len(sc) - 1, S_('text', 'Chương bổ sung – Lũy kế 9 tháng', ('LŨY KẾ 9 THÁNG', 'NÓI GÌ?'), say, anh='financial report'))
def lo_chinh(PX):
    S, M = {}, {}
    plan = [('CH2611A', 'd', 'SAB', '2026-11-26', '07:00'), ('CH2611B', 'h', None, '2026-11-26', '17:30'), ('CH2611C', 'd', 'BMP', '2026-11-26', '20:00'),
            ('CH2711A', 'd', 'HAH', '2026-11-27', '07:00'), ('CH2711B', 'h', None, '2026-11-27', '17:30'), ('CH2711C', 'd', 'DCM', '2026-11-27', '20:00'),
            ('CH2811A', 'd', 'MSN', '2026-11-28', '07:00'), ('CH2811B', 'h', None, '2026-11-28', '17:30'), ('CH2811C', 'd', 'POW', '2026-11-28', '20:00')]
    for k, t, s, ngay, gio in plan:
        S[k], M[k] = doc_bctc(k, s, ngay, gio, PX) if t == 'd' else B.hand(k, "@chungkhoanhuynguyen", ngay, gio, PX)
    return S, M
def lo_kp(PX):
    S, M = {}, {}
    S['HI1611A'], M['HI1611A'] = hi('HI1611A', 'NLG', '2026-11-16', PX)
    S['HI1711A'], M['HI1711A'] = hi('HI1711A', 'DXG', '2026-11-17', PX)
    S['Y2_1611A'], M['Y2_1611A'] = y2('Y2_1611A', 'NT2', '2026-11-16', PX, 'lãi 9 tháng +57,0% | quý 3 +95,4%')
    S['Y2_1711A'], M['Y2_1711A'] = y2('Y2_1711A', 'NKG', '2026-11-17', PX, 'lãi quý 3 +154,8% | doanh thu +45,0%')
    S['TS1611A'], M['TS1611A'] = ts('TS1611A', 'MBB', '2026-11-16', PX, 'mua một lần có hơn không?')
    S['TS1711A'], M['TS1711A'] = ts('TS1711A', 'HPG', '2026-11-17', PX, 'góp đều có giúp ngủ ngon hơn?')
    S['K2_1611A'], M['K2_1611A'] = k2('K2_1611A', ['VCB', 'BID', 'CTG'], '2026-11-16', PX,
        "VCB, BID, CTG: ngân hàng vốn nhà nước quý 3/2026 – CTG lãi +28,2%, VCB chỉ +0,1%: vì sao P/E chênh gần gấp đôi?", "VCB +0,1%", "CTG +28,2%", "ngân hàng có vốn nhà nước", "CTG",
        "Nhóm này còn gánh vai trò hỗ trợ hệ thống, ví dụ Vietcombank nhận chuyển giao bắt buộc CBBank từ tháng 10/2024, nên lợi nhuận và cổ tức có thể khác các ngân hàng tư nhân.")
    S['K2_1711A'], M['K2_1711A'] = k2('K2_1711A', ['HPG', 'HSG', 'NKG'], '2026-11-17', PX,
        "HPG, HSG, NKG: thép quý 3/2026 – NKG lãi +154,8%, HSG −37,4%: cùng ngành sao chênh xa vậy?", "NKG +154,8%", "HSG −37,4%", "thép", "HPG",
        "Giá thép phụ thuộc giá quặng sắt, than cốc và thép nhập khẩu; từ năm 2025 Việt Nam áp thuế chống bán phá giá thép cán nóng nhập từ Trung Quốc và Ấn Độ.")
    them_k2(S['K2_1611A'], ['VCB', 'BID', 'CTG'], 'ngân hàng có vốn nhà nước'); them_k2(S['K2_1711A'], ['HPG', 'HSG', 'NKG'], 'thép')
    for k, kenh in [('LST_1611A', 'LST'), ('LST_1711A', 'LST'), ('Y3_1611A', 'Y3 Vĩ Mô Chứng Khoán Dễ Hiểu (@chungkhoanhuynguyen7)'), ('Y3_1711A', 'Y3 Vĩ Mô Chứng Khoán Dễ Hiểu (@chungkhoanhuynguyen7)')]:
        S[k], M[k] = B.hand(k, kenh, '2026-11-%s' % k[-5:-3], '19:00', PX)
        if k.startswith('LST'): M[k]['nhac'] = 'lofi'
    return S, M
if __name__ == '__main__':
    P1, P2 = {}, {}
    S1, M1 = lo_chinh(P1); S2, M2 = lo_kp(P2)
    b = B.qc(S1) + B.qc(S2); print('TONG LOI', b)
    for M in (M1, M2):
        for k, v in M.items(): print(k, v['tieu_de'][:110], v['bia_hook'], len(v.get('fb_post', '')))
    if '--ghi' in sys.argv:
        B.ghi(CW + '/_video/queue/' + LO, S1, M1, P1, "Đọc BCTC SAB/BMP/HAH/DCM/MSN/POW + 3 video Quản trị vốn/Bài học lịch sử.")
        B.ghi(CW + '/_video/queue/' + LO + '_kp', S2, M2, P2, "Kênh phụ 16–17/11.")
        json.dump({'chinh': {k: M1[k]['tieu_de'] for k in M1}, 'kp': {k: M2[k]['tieu_de'] for k in M2}}, open('/tmp/sp/titles.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
