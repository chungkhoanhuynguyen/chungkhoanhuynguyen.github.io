# -*- coding: utf-8 -*-
# Video BCTC quý – 1 mã/video cho kênh phụ Y2. Xoay vòng VN30 + ngân hàng, mỗi mã 1 lần/quý.
# Ngân hàng: chỉ nêu "vùng giá mua ≤ X" (data/bank_mua.json do kho riêng đẩy sang). Cảnh cuối: quan điểm cá nhân + câu hỏi mở.
import os, sys, json, datetime
CW = os.environ.get('CW', os.path.abspath(os.path.dirname(__file__) + '/../..')); os.environ['CW'] = CW
sys.path.insert(0, CW + '/_video/nv1')
import gen, re
from gen import *
_doc = gen.doc
def _r1(m): return ('%.1f' % (float(m.group(1) + '.' + m.group(2)) + 1e-9)).replace('.', ',')
gen.doc = lambda t: _doc(re.sub(r"(?<![\d.,])(\d+),(\d{2,})(?!\d)", _r1, t))  # lời đọc làm tròn 1 số lẻ, thẻ giữ số chính xác
VN30 = "ACB BCM BID BVH CTG FPT GAS GVR HDB HPG LPB MBB MSN MWG PLX SAB SHB SSB SSI STB TCB TPB VCB VHM VIB VIC VJC VNM VPB VRE".split()
KENH = "Y2 Soi Báo Cáo Tài Chính (@chungkhoanhuynguyen8)"
SO = CW + '/_video/bctc/da_lam.json'
def bank_mua():
    try: return json.load(open(CW + '/data/bank_mua.json', encoding='utf-8'))
    except Exception: return {}
def ds_ma():
    q = max(x['q'] for x in KQ.values() if x.get('q'))
    banks = sorted(s for s, x in KQ.items() if x.get('form') == 'bank' and x.get('q') == q and fund(s).get('mc', 0) >= 3000)
    L = [s for s in VN30 if s in KQ and KQ[s].get('q') == q] + [b for b in banks if b not in VN30]
    return q, L
CG = CW + '/data/can_gia.json'
def chon(n=1):
    """Lấy n mã chưa làm trong quý. Ngân hàng chưa có giá mua: xin giá (can_gia.json) và để lần sau; xin 2 lần không có thì làm không kèm giá."""
    q, L = ds_ma(); so = json.load(open(SO)) if os.path.exists(SO) else {}
    da = so.get(q, []); BM = bank_mua().get('m', {})
    try: cg = json.load(open(CG))
    except Exception: cg = {'s': [], 'lan': {}}
    L = sorted([s for s in L if s not in da], key=lambda s: -(fund(s).get('mc', 0) or 0))
    out = []
    for s in L:
        if len(out) >= n: break
        if KQ[s]['form'] == 'bank' and s not in BM and cg['lan'].get(s, 0) < 2:
            if s not in cg['s']: cg['s'].append(s)
            cg['lan'][s] = cg['lan'].get(s, 0) + 1; continue
        out.append(s)
    cg['s'] = [s for s in cg['s'] if s not in out and s not in BM]
    json.dump(cg, open(CG, 'w'), ensure_ascii=False)
    return q, out, so
def g2(v): return vn(v, 2).rstrip('0').rstrip(',')
def mot(key, s, ngay, gio, PX):
    x = KQ[s]; gen.NGAY_DL = x.get('date') or datetime.date.today().strftime('%d/%m/%Y')
    sc, M = gen.doc_bctc(key, s, ngay, gio, PX)
    bank = x['form'] == 'bank'; ten = gen.TEN.get(s, s); c = close(s)
    end = sc.pop()
    X = bank_mua().get('m', {}).get(s)
    if bank and X:
        say = ("Phần định giá. Theo quan điểm đầu tư cá nhân của Chứng Khoán Huy Nguyễn, với kết quả kinh doanh %s và mặt bằng P/B hiện tại, vùng giá mua hợp lý của %s là từ %s nghìn đồng trở xuống. "
               "Giá đóng cửa gần nhất khoảng %s nghìn đồng, %s. Đây là vùng giá để tích lũy dài hạn, không phải điểm mua ngắn hạn, và vùng giá có thể được điều chỉnh khi có báo cáo quý mới.") % (
            x['q'], s, g2(X), gen.gia(c), "đang nằm trong vùng này" if c <= X else "cao hơn vùng này khoảng %s%%" % vn((c / X - 1) * 100, 1))
        sc.append(S_('bignum', 'Định giá – vùng giá mua', ('VÙNG GIÁ MUA', s), say, moc=True, value=X, fmt='{:,.2f}', unit='',
                     top='%s – VÙNG GIÁ MUA ≤' % s, sub='giá hiện tại %s' % gen.gia(c), col=GREEN))
        M['bia_hook'] = [s + " MUA ≤ " + g2(X), M['bia_hook'][0]]
        M['title'] = M['tieu_de'] = ("%s %s: %s | vùng giá mua ≤ %s" % (s, x['q'], M['bia_hook'][1].lower(), g2(X)))[:100]
    q_end = ("Đó là phần đọc báo cáo tài chính %s của %s. Định giá trong video theo quan điểm đầu tư cá nhân của Chứng Khoán Huy Nguyễn. "
             "Nếu anh chị không đồng tình, hãy bình luận cho em biết anh chị định giá %s ở mức nào và vì sao. Em sẽ đọc hết và trả lời từng bình luận.") % (x['q'], ten, s)
    end['say'] = doc(q_end); end['cap'] = (end['cap'][0], 'ANH CHỊ NGHĨ SAO?'); sc.append(end)
    M.update(kenh=KENH, seri="Soi BCTC quý", seri_web="Đọc BCTC")
    if not bank: M['title'] = M['tieu_de'] = M['title'].replace("Đọc BCTC 5 phút | ", "")[:100]
    return sc, M
if __name__ == '__main__':
    n = int(os.environ.get('SO_MA', '1')); now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(hours=7)
    q, L, so = chon(n)
    if not L: print('HET MA QUY', q); sys.exit(0)
    import pprint
    sys.path.insert(0, CW + '/_video'); import kiem_loi, xung_ho
    lo = now.strftime('%Y%m%d') + '_bctc'; d = CW + '/_video/queue/' + lo; S, M, PX = {}, {}, {}
    for i, s in enumerate(L):
        ngay = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%d'); k = 'BC%s%s' % (now.strftime('%d%m'), s)
        S[k], M[k] = mot(k, s, ngay, '19:00', PX)
        e = [l for l in kiem_loi.kiem([{'loi': xung_ho.le_phep(c['say'])} for c in S[k]], tin_nong=False) if l.startswith('LỖI')]
        print(k, M[k]['title'], 'LOI', e[:3])
    os.makedirs(d, exist_ok=True)
    with open(d + '/video_dai.py', 'w', encoding='utf-8') as f:
        f.write("# -*- coding: utf-8 -*-\n# VIDEO BCTC QUÝ %s – tự sinh %s: %s\n" % (q, now.strftime('%d/%m/%Y'), ", ".join(L)))
        f.write("GOLD = (255, 196, 0); RED = (239, 68, 68); GREEN = (34, 197, 94); BLUE = (56, 189, 248); WHITE = (255, 255, 255)\n\nS = {}\n\n")
        for k, sc in S.items(): f.write("S[%r] = %s\n\n" % (k, pprint.pformat(sc, width=160, sort_dicts=False)))
    json.dump(M, open(d + '/meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(PX, open(d + '/px_tuan.json', 'w', encoding='utf-8'), ensure_ascii=False)
    so.setdefault(q, []).extend(L); json.dump(so, open(SO, 'w'), ensure_ascii=False, indent=0)
    open(os.environ.get('GITHUB_OUTPUT', '/dev/null'), 'a').write('lo=%s\n' % lo)
