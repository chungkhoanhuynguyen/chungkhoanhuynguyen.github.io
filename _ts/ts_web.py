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
# 4) đầu cơ V306TMVN: đang đứng ngoài giữ tiền (cfg "dau_co_tien_mat") -> tài khoản đi ngang, VN-Index cập nhật
if cfg.get('dau_co_tien_mat'):
    m1 = re.search(r'__CH\["c1"\]=\{d:(\[\[.*?\]\]),off:(\[.*?\]\]),', t)
    p1 = [p for p in json.loads(m1.group(1)) if p[0] <= B]; f1 = p1[-1]
    a1 = [[p[0], f1[1], round(f1[2] * vni[p[0]] / vni[B], 5)] for p in add]
    off = json.loads(m1.group(2)); off[-1][1] = last
    t = t[:m1.start(1)] + json.dumps(p1 + a1, separators=(',', ':')) + t[m1.end(1):m1.start(2)] + json.dumps(off) + t[m1.end(2):]
    s1 = t.find('id="luotsong"'); e1 = t.find('id="tichsan"')
    b1 = t[s1:e1]; z = (p1 + a1)[-1]
    y1 = (z[0][:4] + '-01-01'); ye = [p for p in p1 + a1 if p[0] < y1][-1]
    yrs1 = (D.date.fromisoformat(last) - D.date(2015, 12, 31)).days / 365.25
    b1 = kpi(b1, 'VN-Index cùng kỳ', vf(z[2] - 1))
    b1 = kpi(b1, 'Lãi kép bình quân mỗi năm', vf(z[1] ** (1 / yrs1) - 1).lstrip('+'))
    b1, n1 = re.subn(r'(<td class="sym">2026</td><td class="n [a-z]+">[^<]*</td><td class="n )(pos|neg)(">)[^<]*(</td>)',
                     lambda mm: mm.group(1) + ('pos' if z[2] / ye[2] >= 1 else 'neg') + mm.group(3) + vf(z[2] / ye[2] - 1) + mm.group(4), b1, count=1)
    assert n1 == 1, 'khong thay dong 2026 dau co'
    b1 = re.sub(r'Năm 2026 tính đến \d\d/\d\d/\d{4}', 'Năm 2026 tính đến ' + ds, b1)
    t = t[:s1] + b1 + t[e1:]
    t = re.sub(r'(cắt lỗ từ 01/01/2016 đến )\d\d/\d\d/\d{4}', lambda mm: mm.group(1) + ds, t, count=1)
open(P, 'w', encoding='utf-8').write(t)
print('tich san', last, 'tk', vf(tot), 'cagr', vf(cagr), 'vni', vf(vt), 'dd', vf(dd), '2026', vf(y26), vf(v26),
      {s: round(w * 100, 1) for s, w in w_now.items()}, 'tien', round(tien / nav[last] * 100, 1))
