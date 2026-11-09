# -*- coding: utf-8 -*-
# NV1 lô 20261110_0040: kênh chính 29–30/11 + kênh phụ 18/11. Dùng: CW=/tmp/cw python3 build3.py <lô> [--ghi]
import json, sys, os
import gen
gen.NGAY_DL = "9/11/2026"
gen.TEN.update({'VHM': 'Vinhomes', 'GMD': 'Gemadept', 'REE': 'Cơ điện lạnh REE', 'PLX': 'Petrolimex', 'PVD': 'PV Drilling', 'PVT': 'PV Trans',
                'VCB': 'Vietcombank', 'DCM': 'Đạm Cà Mau', 'DPM': 'Đạm Phú Mỹ', 'DHC': 'Giấy Đông Hải Bến Tre', 'BMP': 'Nhựa Bình Minh'})
gen.ANH.update({'VHM': 'residential towers Vietnam', 'GMD': 'container port', 'REE': 'office building air conditioning', 'PLX': 'gas station', 'PVD': 'offshore drilling rig',
                'PVT': 'oil tanker ship', 'KBC': 'industrial park', 'IDC': 'industrial park factory', 'SZC': 'industrial zone aerial'})
from gen import *
import build as B
from hand3 import H3
import hand; hand.H.update(H3)
LO = sys.argv[1]
from build2 import them_k2
def lo_chinh(PX):
    S, M = {}, {}
    plan = [('CH2911A', 'd', 'VHM', '2026-11-29', '07:00'), ('CH2911B', 'h', None, '2026-11-29', '17:30'), ('CH2911C', 'd', 'GMD', '2026-11-29', '20:00'),
            ('CH3011A', 'd', 'REE', '2026-11-30', '07:00'), ('CH3011B', 'h', None, '2026-11-30', '17:30'), ('CH3011C', 'd', 'PLX', '2026-11-30', '20:00')]
    for k, t, s, ngay, gio in plan:
        S[k], M[k] = doc_bctc(k, s, ngay, gio, PX) if t == 'd' else B.hand(k, "@chungkhoanhuynguyen", ngay, gio, PX)
    return S, M
def lo_kp(PX):
    S, M = {}, {}
    S['HI1811A'], M['HI1811A'] = hi('HI1811A', 'PVD', '2026-11-18', PX)
    S['Y2_1811A'], M['Y2_1811A'] = y2('Y2_1811A', 'PVT', '2026-11-18', PX, 'lãi quý 3 +42,4% | 9 tháng +64,6%')
    S['TS1811A'], M['TS1811A'] = ts('TS1811A', 'VCB', '2026-11-18', PX, 'ngân hàng lớn nhất có hợp góp đều?')
    G = ['DCM', 'DPM', 'DHC', 'BMP']
    S['K2_1811A'], M['K2_1811A'] = k2('K2_1811A', G, '2026-11-18', PX,
        "DCM, DPM, DHC, BMP: phân bón – hóa chất – nhựa quý 3/2026 – DCM lãi +31,1%, DPM −82,9%: cùng làm urê sao chênh xa?", "DCM +31,1%", "DPM −82,9%", "phân bón, hóa chất", "DCM",
        "Đạm Cà Mau và Đạm Phú Mỹ cùng sản xuất urê từ khí thiên nhiên, nên giá khí đầu vào, giá urê thế giới và lịch bảo dưỡng nhà máy có thể làm lợi nhuận từng quý chênh nhau rất xa.")
    them_k2(S['K2_1811A'], G, 'phân bón, hóa chất')
    for k, kenh in [('LST_1811A', 'LST'), ('Y3_1811A', 'Y3 Vĩ Mô Chứng Khoán Dễ Hiểu (@chungkhoanhuynguyen7)')]:
        S[k], M[k] = B.hand(k, kenh, '2026-11-18', '19:00', PX)
        if k.startswith('LST'): M[k]['nhac'] = 'lofi'
    return S, M
if __name__ == '__main__':
    P1, P2 = {}, {}
    S1, M1 = lo_chinh(P1); S2, M2 = lo_kp(P2)
    b = B.qc(S1) + B.qc(S2); print('TONG LOI', b)
    for M in (M1, M2):
        for k, v in M.items(): print(k, v['tieu_de'][:120], v['bia_hook'], len(v.get('fb_post', '')))
    if '--ghi' in sys.argv:
        B.ghi(CW + '/_video/queue/' + LO, S1, M1, P1, "Đọc BCTC VHM/GMD/REE/PLX + Quản trị vốn (tiền mặt 70/30) + Định giá (bẫy cổ tức).")
        B.ghi(CW + '/_video/queue/' + LO + '_kp', S2, M2, P2, "Kênh phụ 18/11.")
        json.dump({'chinh': {k: M1[k]['tieu_de'] for k in M1}, 'kp': {k: M2[k]['tieu_de'] for k in M2}}, open('/tmp/sp/titles.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
