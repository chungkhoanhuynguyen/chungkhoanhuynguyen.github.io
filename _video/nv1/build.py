# -*- coding: utf-8 -*-
import json, pprint, sys, os
from gen import *
from hand import H
sys.path.insert(0, CW + '/_video'); import kiem_loi, xung_ho
LO = sys.argv[1]
def meta_hand(k, v, kenh, ngay, gio):
    link = "https://chungkhoanhuynguyen.com/hoc/%s.html" % slug(v['title'])
    M = dict(kenh=kenh, seri=v['seri'], ngay=ngay, gio_goi_y=gio, gio=gio, tieu_de=v['title'], title=v['title'], mo_ta=mo_ta(v['title'], v['nguon'], v['seri'], link),
             tags=v['tags'], bia_hook=v['hook'], badge=v['badge'], fb_post=fb(" – ".join(v['hook']), v['fb'], v['q'], link), chuong=[c['ch'] for c in v['S'] if c.get('ch')], seri_web=v['seri'], link_web=link)
    if v.get('nhac'): M['nhac'] = v['nhac']
    return M
def hand(k, kenh, ngay, gio, PX):
    v = H[k]; S0 = v['S']
    for c in S0:
        if c.get('chart') and c['chart'].get('circles') is None:
            sym = c['chart']['sym'][:-1]; wk = weekly(sym); PX[sym + 'W'] = wk; c['chart']['circles'] = circles(wk)
    return S0, meta_hand(k, v, kenh, ngay, gio)
def lo_chinh(PX):
    S, M = {}, {}
    plan = [('CH2311A', 'd', 'NAB', '2026-11-23', '07:00'), ('CH2311B', 'h', None, '2026-11-23', '17:30'), ('CH2311C', 'd', 'GAS', '2026-11-23', '20:00'),
            ('CH2411A', 'd', 'KLB', '2026-11-24', '07:00'), ('CH2411B', 'h', None, '2026-11-24', '17:30'), ('CH2411C', 'd', 'VJC', '2026-11-24', '20:00'),
            ('CH2511A', 'd', 'VAB', '2026-11-25', '07:00'), ('CH2511B', 'h', None, '2026-11-25', '17:30'), ('CH2511C', 'd', 'DPM', '2026-11-25', '20:00')]
    for k, t, s, ngay, gio in plan:
        S[k], M[k] = doc_bctc(k, s, ngay, gio, PX) if t == 'd' else hand(k, "@chungkhoanhuynguyen", ngay, gio, PX)
    return S, M
def lo_kp(PX):
    S, M = {}, {}
    for d in ('14', '15'):
        ng = '2026-11-%s' % d
    S['HI1411A'], M['HI1411A'] = hi('HI1411A', 'HVN', '2026-11-14', PX)
    S['HI1511A'], M['HI1511A'] = hi('HI1511A', 'KDH', '2026-11-15', PX)
    S['Y2_1411A'], M['Y2_1411A'] = y2('Y2_1411A', 'GMD', '2026-11-14', PX, 'lãi 9 tháng +80,7% | biên gộp co lại')
    S['Y2_1511A'], M['Y2_1511A'] = y2('Y2_1511A', 'VSC', '2026-11-15', PX, 'lỗ 9 tỷ | lãi vay +83,6%')
    S['TS1411A'], M['TS1411A'] = ts('TS1411A', 'VNM', '2026-11-14', PX, 'mua một lần thì sao?')
    S['TS1511A'], M['TS1511A'] = ts('TS1511A', 'DHG', '2026-11-15', PX, 'cổ phiếu ít biến động nói gì?')
    S['K2_1411A'], M['K2_1411A'] = k2('K2_1411A', ['BSR', 'PLX', 'GAS', 'PVT', 'PVD'], '2026-11-14', PX,
        "BSR, PLX, GAS, PVT, PVD: dầu khí quý 3/2026 – BSR lãi +888%, PVD −74,5%: vì sao chênh nhau xa?", "BSR +888%", "PVD −74,5%", "dầu khí", "BSR",
        "Giá dầu Brent ngày 6/11/2026 khoảng 97,76 USD một thùng, giảm khoảng 5,7% trong một tháng, nên kết quả quý 4 của nhóm này có thể khác quý 3.")
    S['K2_1511A'], M['K2_1511A'] = k2('K2_1511A', ['DHG', 'DCM', 'VNM', 'REE', 'NAB', 'LPB'], '2026-11-15', PX,
        "6 cổ phiếu beta thấp: DHG 0,22, VNM 0,42, NAB 0,48 – phòng thủ thật hay chỉ ít biến động?", "BETA 0,22", "PHÒNG THỦ THẬT?", "beta thấp", "VNM",
        "Beta thấp được đo trong quá khứ; một tin xấu riêng của doanh nghiệp vẫn có thể làm giá giảm mạnh, như lợi nhuận quý 3 của Dược Hậu Giang giảm khoảng 53% so với cùng kỳ.")
    for k, kenh in [('LST_1411A', 'LST'), ('LST_1511A', 'LST'), ('Y3_1411A', 'Y3 Vĩ Mô Chứng Khoán Dễ Hiểu (@chungkhoanhuynguyen7)'), ('Y3_1511A', 'Y3 Vĩ Mô Chứng Khoán Dễ Hiểu (@chungkhoanhuynguyen7)')]:
        S[k], M[k] = hand(k, kenh, '2026-11-%s' % k[-5:-3], '19:00', PX)
        if k.startswith('LST'): M[k]['nhac'] = 'lofi'
    return S, M
def qc(S):
    bad = 0
    for k, sc in S.items():
        L = kiem_loi.kiem([{'loi': xung_ho.le_phep(c['say'])} for c in sc], tin_nong=False)
        e = [l for l in L if l.startswith('LỖI')]; bad += len(e)
        print(k, dem(sc), 'LỖI=%d' % len(e), 'CB=%d' % (len(L) - len(e)), e[:3], [l for l in L if 'cụt' in l][:2])
        for c in sc: assert isinstance(c['cap'], (tuple, list))
    return bad
def ghi(dirp, S, M, PX, ghi_chu):
    os.makedirs(dirp, exist_ok=True)
    with open(dirp + '/video_dai.py', 'w', encoding='utf-8') as f:
        f.write("# -*- coding: utf-8 -*-\n# VIDEO DÀI – NV1 soạn 8/11/2026 (lô %s: %s). %s Nến tuần: px_tuan.json.\n" % (os.path.basename(dirp), ", ".join(S), ghi_chu))
        f.write("GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)\n\nS = {}\n\n")
        for k, sc in S.items(): f.write("S[%r] = %s\n\n" % (k, pprint.pformat(sc, width=160, sort_dicts=False)))
    json.dump(M, open(dirp + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(PX, open(dirp + '/px_tuan.json', 'w', encoding='utf-8'), ensure_ascii=False)
if __name__ == '__main__':
    P1, P2 = {}, {}
    S1, M1 = lo_chinh(P1); S2, M2 = lo_kp(P2)
    b = qc(S1) + qc(S2); print('TONG LOI', b)
    if '--ghi' in sys.argv:
        ghi(CW + '/_video/queue/' + LO, S1, M1, P1, "Đọc BCTC NAB/GAS/KLB/VJC/VAB/DPM + 3 video Quản trị rủi ro.")
        ghi(CW + '/_video/queue/' + LO + '_kp', S2, M2, P2, "Kênh phụ 14–15/11.")
        json.dump({'chinh': {k: M1[k]['tieu_de'] for k in M1}, 'kp': {k: M2[k]['tieu_de'] for k in M2}}, open('/tmp/sp/titles.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
