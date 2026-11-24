# -*- coding: utf-8 -*-
"""Cập nhật tự động mục #tichsan trên bao-cao-2026.html theo giá mới nhất.
Chạy sau update.py (workflow Cap nhat bang). Danh mục và lệnh từ 28/10/2026 ghi trong data/ts_cfg.json;
mỗi lần có lệnh tích sản mới chỉ cần thêm 1 dòng vào "lenh" (mua/bán theo % tài khoản tại giá đóng cửa ngày đó)."""
import json, re, sys, datetime as D, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import hncodec
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(R, 'data/ts_cfg.json'), encoding='utf-8'))
P = os.path.join(R, 'bao-cao-2026.html')

def hist(s):
    x = hncodec.load(os.path.join(R, 'data/c/%s.bin' % s)); d = D.date.fromisoformat(x['d0']); out = {}
    for g, c in zip(x['g'], x['c']):
        d += D.timedelta(days=g); out[str(d)] = c / 100
    return out
rec = hncodec.load(os.path.join(R, 'data/c/recent.bin'))['b']
live = hncodec.load(os.path.join(R, 'data/c/live.bin'))
syms = sorted({s for s in cfg['dau'] } | {l['ma'] for l in cfg['lenh']})
gia = {}
for s in syms:
    m = hist(s)
    for r in rec.get(s, []): m[r[0]] = r[4] / 100
    x = live['b'].get(s)
    if x and x[3] and live.get('d'): m[live['d']] = x[3] / 100
    gia[s] = m
mwh = hncodec.load(os.path.join(R, 'data/mwh.bin'))
vni = dict(zip(mwh['dates'], mwh['vn']))
B = cfg['ngay_goc']
ngay = sorted(d for d in vni if d >= B)
if live.get('d') and live['d'] > ngay[-1] and all(live['d'] in gia[s] for s in cfg['dau']):
    ngay.append(live['d']); vni[live['d']] = vni[ngay[-2]]  # chỉ số chưa có thì giữ phiên trước
def px(s, d):
    m = gia[s]; k = max(x for x in m if x <= d); return m[k]
# đơn vị cổ phiếu, tài khoản = 1 tại ngày gốc
tw = sum(cfg['dau'].values()); u = {s: w / tw / px(s, B) for s, w in cfg['dau'].items()}; tien = 0.0
nav = {}
lenh = sorted(cfg['lenh'], key=lambda l: l['ngay'])
for d in ngay:
    v = tien + sum(n * px(s, d) for s, n in u.items())
    for l in [l for l in lenh if l['ngay'] == d]:
        s = l['ma']; p = px(s, d)
        if l['loai'] == 'ban_het': tien += u.pop(s, 0) * p
        elif l['loai'] == 'ban': q = l['pt'] / 100 * v; u[s] -= q / p; tien += q
        elif l['loai'] == 'mua':
            q = min(tien, l['pt'] / 100 * v) if not l.get('dung_het') else tien
            u[s] = u.get(s, 0) + q / p; tien -= q
    nav[d] = v
L0 = cfg['nav_goc']; V0 = cfg['vni_goc_ti_le']
last = ngay[-1]
tk = {d: L0 * nav[d] for d in ngay}; vn = {d: V0 * vni[d] / vni[B] for d in ngay}
w_now = {s: n * px(s, last) / nav[last] for s, n in u.items()}
t = open(P, encoding='utf-8').read()
# 1) biểu đồ: giữ điểm gốc đến ngày gốc, thêm điểm mỗi 7 ngày + điểm mới nhất
m = re.search(r'__CH\["c2"\]=\{d:(\[\[.*?\]\]),', t)
pts = [p for p in json.loads(m.group(1)) if p[0] <= B]
dB = D.date.fromisoformat(B); add = []; k = 1
while True:
    want = str(dB + D.timedelta(days=7 * k))
    if want >= last: break
    c = [d for d in ngay if d <= want][-1]
    if c > B and (not add or add[-1][0] != c): add.append([c, round(tk[c], 5), round(vn[c], 5)])
    k += 1
if last > B: add.append([last, round(tk[last], 5), round(vn[last], 5)])
newd = json.dumps(pts + add, separators=(',', ':'))
t = t[:m.start(1)] + newd + t[m.end(1):]
allp = pts + add
# 2) KPI
tot = allp[-1][1] - 1; vt = allp[-1][2] - 1
yrs = (D.date.fromisoformat(last) - D.date(2017, 12, 29)).days / 365.25
cagr = (allp[-1][1]) ** (1 / yrs) - 1
pk = 0; dd = 0
for p in allp: pk = max(pk, p[1]); dd = min(dd, p[1] / pk - 1)
dd = min(dd, cfg['sut_goc'] / 100)
nf = lambda x: f"{x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
vf = lambda x, n=1: ('+' if x >= 0 else '−') + f"{abs(x)*100:,.{n}f}".replace(',', 'X').replace('.', ',').replace('X', '.') + '%'
sec = t.find('id="tichsan"'); end = t.find('Danh mục đang cầm', sec)
blk = t[sec:end]
def kpi(blk, lab, val):
    # thay số đứng ngay trước nhãn KPI
    return re.sub(r'(>)([+−\-]?[\d.,]+%)(<[^>]*>\s*(?:<[^>]*>\s*)*' + re.escape(lab) + ')', lambda mm: mm.group(1) + val + mm.group(3), blk, count=1)
y0 = [p for p in allp if p[0] <= '2025-12-31'][-1]
blk2 = blk
blk2 = kpi(blk2, 'Tài khoản tích sản từ 01/2018', vf(tot))
blk2 = kpi(blk2, 'VN-Index cùng kỳ', vf(vt))
blk2 = kpi(blk2, 'Lãi kép bình quân mỗi năm', vf(cagr).lstrip('+'))
blk2 = kpi(blk2, 'Sụt sâu nhất của tài khoản', vf(dd))
y26 = allp[-1][1] / y0[1] - 1; v26 = allp[-1][2] / y0[2] - 1
blk2, n26 = re.subn(r'(<td class="sym">2026</td><td class="n )(pos|neg)(">)[^<]*(</td><td class="n )(pos|neg)(">)[^<]*(</td>)',
              lambda mm: mm.group(1) + ('pos' if y26 >= 0 else 'neg') + mm.group(3) + vf(y26) + mm.group(4) + ('pos' if v26 >= 0 else 'neg') + mm.group(6) + vf(v26) + mm.group(7), blk2, count=1)
assert n26 == 1, 'khong thay dong 2026'
ds = '/'.join(reversed(last.split('-')))
blk2 = re.sub(r'Lãi/lỗ năm 2026 tính đến \d\d/\d\d/\d{4}', 'Lãi/lỗ năm 2026 tính đến ' + ds, blk2)
blk2, nn = re.subn(r'đủ lâu: [+−][\d.,]+% từ 01/2018, lãi kép bình quân [\d,]+% mỗi năm', 'đủ lâu: ' + vf(tot) + ' từ 01/2018, lãi kép bình quân ' + vf(cagr).lstrip('+') + ' mỗi năm', blk2)
assert nn == 1, 'khong thay cau nhuoc diem'
for lab in ('Tài khoản tích sản từ 01/2018', 'VN-Index cùng kỳ', 'Lãi kép bình quân mỗi năm', 'Sụt sâu nhất của tài khoản'):
    assert lab in blk2, lab
t = t[:sec] + blk2 + t[end:]
# 3) lãi/lỗ mã đang cầm (bản tĩnh, JS trên trang vẫn tính lại theo giá trong phiên)
for s in u:
    mm = re.search(r'(<td class="sym">%s</td><td class="n">)(\d+)%%(</td><td data-gv="([\d.]+)" class="n )(pos|neg)(">)[^<]*' % s, t)
    if not mm: continue
    p = px(s, last) / float(mm.group(4)) * 0.9985 - 1
    t = t[:mm.start()] + mm.group(1) + str(round(w_now[s] * 100)) + '%' + mm.group(3) + ('pos' if p >= 0 else 'neg') + mm.group(6) + vf(p) + t[mm.end():]
# 4) đầu cơ V306TMVN: tự tính từ sổ lệnh room (data/dc_lenh.json do lượt lọc hằng ngày ở kho riêng chép sang)
import base64
KE = 'hn-bc-208'
def xr(b): return bytes(b[i] ^ ord(KE[i % len(KE)]) ^ ((i * 7) & 255) for i in range(len(b)))
try: DC = json.load(open(os.path.join(R, 'data/dc_lenh.json'), encoding='utf-8'))
except Exception: DC = {'mo': [], 'xong': []}
lenh_dc = [dict(p, mo=True) for p in DC.get('mo', [])] + [dict(p, mo=False) for p in DC.get('xong', [])]
lenh_dc = [p for p in lenh_dc if p.get('ngay_mua') and p['ngay_mua'] > B]
def phien_sau(d):
    c = [x for x in ngay if x > d]; return c[0] if c else None
def gia_mo(s, d):
    r = [x for x in rec.get(s, []) if x[0] == d]
    return r[0][1] / 100 if r else None
for p in lenh_dc:
    if p['ma'] not in gia:
        m = hist(p['ma']) if os.path.exists(os.path.join(R, 'data/c/%s.bin' % p['ma'])) else {}
        for r in rec.get(p['ma'], []): m[r[0]] = r[4] / 100
        gia[p['ma']] = m
    if not p['mo']:
        p['ngay_ban'] = phien_sau(p['ngay_ban_bao'])
        if p['ngay_ban']:
            p['gia_ban'] = gia_mo(p['ma'], p['ngay_ban']) or p.get('hien') or px(p['ma'], p['ngay_bao'])
m1 = re.search(r'__CH\["c1"\]=\{d:(\[\[.*?\]\]),off:(\[.*?\]\]),', t)
p1 = [p for p in json.loads(m1.group(1)) if p[0] <= B]; f1 = p1[-1]
cash = 1.0; pos = {}; navd = {}
for d in ngay:
    for p in lenh_dc:
        if p.get('ngay_ban') == d and id(p) in pos:
            n = pos.pop(id(p)); cash += n * p['gia_ban']
    v = cash + sum(n * px(p['ma'], d) for p in lenh_dc for k, n in pos.items() if k == id(p))
    for p in lenh_dc:
        if p['ngay_mua'] == d and id(p) not in pos:
            q = min(cash, 0.25 * v); pos[id(p)] = q / p['gia']; cash -= q
    navd[d] = (v, bool(pos))
a1 = [[p[0], round(f1[1] * navd[p[0]][0], 5), round(f1[2] * vni[p[0]] / vni[B], 5)] for p in add]
off = [[x[0], min(x[1], B)] for x in json.loads(m1.group(2)) if x[0] <= B]
for d in ngay[1:]:
    if not navd[d][1]:
        if off and off[-1][1] >= [x for x in ngay if x < d][-1]: off[-1][1] = d
        else: off.append([d, d])
t = t[:m1.start(1)] + json.dumps(p1 + a1, separators=(',', ':')) + t[m1.end(1):m1.start(2)] + json.dumps(off) + t[m1.end(2):]
s1 = t.find('id="luotsong"'); e1 = t.find('id="tichsan"')
b1 = t[s1:e1]; z = (p1 + a1)[-1]
ye = [p for p in p1 + a1 if p[0] < z[0][:4] + '-01-01'][-1]
yrs1 = (D.date.fromisoformat(last) - D.date(2015, 12, 31)).days / 365.25
dong = [p for p in lenh_dc if not p['mo'] and p.get('gia_ban')]
lai = [p for p in dong if p['gia_ban'] > p['gia']]
g = cfg['dau_co_goc']
b1 = kpi(b1, 'Tài khoản V306TMVN từ 01/2016', vf(z[1] - 1))
b1 = kpi(b1, 'VN-Index cùng kỳ', vf(z[2] - 1))
b1 = kpi(b1, 'Lãi kép bình quân mỗi năm', vf(z[1] ** (1 / yrs1) - 1).lstrip('+'))
b1, nk = re.subn(r'<b>\d+</b><span>Lệnh đã đóng, \d+ lệnh lãi</span>', '<b>%d</b><span>Lệnh đã đóng, %d lệnh lãi</span>' % (g['dong'] + len(dong), g['lai'] + len(lai)), b1)
assert nk == 1, 'khong thay KPI lenh dong'
n26 = sum(1 for p in lenh_dc if p['ngay_mua'][:4] == '2026'); l26 = sum(1 for p in lai if p['ngay_mua'][:4] == '2026')
b1, n1 = re.subn(r'(<td class="sym">2026</td><td class="n )(pos|neg)(">)[^<]*(</td><td class="n )(pos|neg)(">)[^<]*(</td><td class="n">)\d+(</td><td class="n">)\d+(</td>)',
                 lambda mm: mm.group(1) + ('pos' if z[1] >= ye[1] else 'neg') + mm.group(3) + vf(z[1] / ye[1] - 1) + mm.group(4) + ('pos' if z[2] >= ye[2] else 'neg') + mm.group(6) + vf(z[2] / ye[2] - 1) + mm.group(7) + str(g['lenh_2026'] + n26) + mm.group(8) + str(g['lai_2026'] + l26) + mm.group(9), b1, count=1)
assert n1 == 1, 'khong thay dong 2026 dau co'
b1 = re.sub(r'năm 2026 tính đến nay [+−][\d,]+%', 'năm 2026 tính đến nay ' + vf(z[1] / ye[1] - 1), b1)
b1 = re.sub(r'Năm 2026 tính đến \d\d/\d\d/\d{4}', 'Năm 2026 tính đến ' + ds, b1)
# sổ lệnh PRO (mã hoá): thêm lệnh đã đóng sau ngày gốc, đánh dấu data-auto để chạy lại không trùng
mm = re.search(r'<tbody data-e="([^"]+)"', b1)
if mm:
    body = xr(base64.b64decode(mm.group(1))).decode()
    body = re.sub(r'<tr data-auto="1".*?</tr>', '', body, flags=re.S)
    dmy = lambda d: '/'.join(reversed(d.split('-')))
    LY = {'cat': ('loss', 'Cắt lỗ'), 'bao_ve': (None, 'Chốt lời'), 'het_gio': (None, 'Hết thời gian nắm giữ')}
    rows = ''
    for p in sorted(dong, key=lambda p: p['ngay_mua'], reverse=True):
        k = p['gia_ban'] / p['gia'] - 1; cl, tx = LY.get(p.get('ly_do'), (None, 'Hết thời gian nắm giữ'))
        cl = cl or ('win' if k > 0 else 'loss'); np_ = len([x for x in ngay if p['ngay_mua'] <= x <= p['ngay_ban']]) - 1
        rows += ('<tr data-auto="1" data-y="%s"><td class="sym">%s</td><td>%s</td><td class="n">%s</td><td>%s</td><td class="n">%s</td><td class="n">%d</td><td class="n %s">%s</td><td><span class="tag %s">%s</span></td></tr>'
                 % (p['ngay_mua'][:4], p['ma'], dmy(p['ngay_mua']), nf(p['gia']), dmy(p['ngay_ban']), nf(p['gia_ban']), np_, 'pos' if k > 0 else 'neg', vf(k), cl, tx))
    body = rows + body
    b1 = b1[:mm.start(1)] + base64.b64encode(xr(body.encode())).decode() + b1[mm.end(1):]
t = t[:s1] + b1 + t[e1:]
t = re.sub(r'(cắt lỗ từ 01/01/2016 đến )\d\d/\d\d/\d{4}', lambda mm: mm.group(1) + ds, t, count=1)
open(P, 'w', encoding='utf-8').write(t)
print('dau co', z[0], vf(z[1]-1), 'lenh moi', len(lenh_dc), 'dong', len(dong))
print('tich san', last, 'tk', vf(tot), 'cagr', vf(cagr), 'vni', vf(vt), 'dd', vf(dd), '2026', vf(y26), vf(v26),
      {s: round(w * 100, 1) for s, w in w_now.items()}, 'tien', round(tien / nav[last] * 100, 1))
