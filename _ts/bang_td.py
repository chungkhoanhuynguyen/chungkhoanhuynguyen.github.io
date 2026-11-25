# -*- coding: utf-8 -*-
"""Cập nhật 'Bảng theo dõi' (#grid) và dòng giá MSR ở 'Tiêu điểm' trên index.html theo giá mới nhất.
Chạy sau update.py trong workflow Cap nhat bang."""
import re, os, sys, datetime as D
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, R)
import hncodec
rec = hncodec.load(os.path.join(R, 'data/c/recent.bin'))['b']
live = hncodec.load(os.path.join(R, 'data/c/live.bin'))
def series(s, den=None):
    x = hncodec.load(os.path.join(R, 'data/c/%s.bin' % s)); m = {}
    if x:
        d = D.date.fromisoformat(x['d0'])
        for g, c in zip(x['g'], x['c']): d += D.timedelta(days=g); m[str(d)] = c / 100
    else:  # mã UPCoM không có tệp lịch sử: lấy trực tiếp
        import chart
        for b in chart.bars(s): m[b[0]] = b[4] / 100
    for r in rec.get(s, []): m[r[0]] = r[4] / 100
    y = live['b'].get(s)
    if y and y[3] and live.get('d'): m[live['d']] = y[3] / 100
    k = sorted(x for x in m if den is None or x <= den)
    return [(a, m[a]) for a in k]
def vf(x): return ('+' if x >= 0 else '−') + f"{abs(x):.1f}".replace('.', ',') + '%'
def nf(x): return f"{x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
def card(s, den=None):
    ss = series(s, den); last_d, last = ss[-1]
    y1 = str(D.date.fromisoformat(last_d) - D.timedelta(days=365))
    yr = [p for p in ss if p[0] >= y1]; base = [p for p in ss if p[0] <= y1]
    b0 = base[-1][1] if base else yr[0][1]
    ch = (last / b0 - 1) * 100; pk = max(c for _, c in yr); fp = (last / pk - 1) * 100
    v = [c for _, c in yr]; lo, hi = min(v), max(v); n = len(v)
    pts = ' '.join('%.1f,%.1f' % (i * 240 / (n - 1), 53.6 - (c - lo) / (hi - lo or 1) * 51.2) for i, c in enumerate(v))
    return last_d, last, ch, fp, pts
if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'thu':
    for s, d in (('FPT', '2026-10-23'), ('MSR', '2026-10-26'), ('HCM', '2026-10-23')):
        a = card(s, d); print(s, a[:4])
    sys.exit()
P = os.path.join(R, 'index.html'); t = open(P, encoding='utf-8').read()
def fix(m):
    a = m.group(0); s = m.group(1)
    d, last, ch, fp, pts = card(s)
    a = re.sub(r'data-y="[^"]*" data-h="[^"]*"', 'data-y="%.2f" data-h="%.2f"' % (ch, fp), a)
    a = re.sub(r'class="spark (up|dn)"', 'class="spark %s"' % ('up' if ch >= 0 else 'dn'), a)
    a = re.sub(r'points="[^"]*"', 'points="%s"' % pts, a)
    cy = pts.split()[-1].split(',')[1]
    a = re.sub(r'<circle cx="[^"]*" cy="[^"]*"', '<circle cx="240.0" cy="%s"' % cy, a)
    a = re.sub(r'<dt>Giá \d\d/\d\d</dt><dd>[^<]*</dd>', '<dt>Giá %s</dt><dd>%s</dd>' % ('/'.join(d.split('-')[2:0:-1]), nf(last)), a)
    a = re.sub(r'(<dt>1 năm</dt><dd class=")(pos|neg)(">)[^<]*', lambda mm: mm.group(1) + ('pos' if ch >= 0 else 'neg') + mm.group(3) + vf(ch), a)
    a = re.sub(r'(<dt>Từ đỉnh</dt><dd class=")(pos|neg)(">)[^<]*', lambda mm: mm.group(1) + ('pos' if fp >= 0 else 'neg') + mm.group(3) + vf(fp), a)
    return a
t, n = re.subn(r'<article class="tk" [^>]*data-s="([A-Z0-9]+)">.*?</article>', fix, t, flags=re.S)
mm = re.search(r'<h2>Tiêu điểm: ([A-Z0-9]+)</h2>', t)
if mm:
    d, last, ch, fp, _ = card(mm.group(1))
    t = re.sub(r'Giá cổ phiếu 1 năm: [+−][\d,]+% · đóng cửa [\d.,]+ ngày \d\d/\d\d/\d{4}\.',
               'Giá cổ phiếu 1 năm: %s · đóng cửa %s ngày %s.' % (vf(ch), nf(last), '/'.join(reversed(d.split('-')))), t)

# (25/11 QL1: thẻ "Lệnh thật tiêu điểm" ghi tay "Hiện 54,0, giảm 50% từ đỉnh" bị đứng giá – anh Huy: không để số sai trên web)
def fix_lt(m):
    a = m.group(0); s = m.group(1)
    ss = series(s); d, last = ss[-1]; pk = max(c for _, c in ss); dd = (1 - last / pk) * 100
    return re.sub(r'([Hh]iện) [\d.,]+, giảm (?:hơn )?\d+% từ đỉnh',
                  lambda mm: '%s %s (%s), giảm %d%% từ đỉnh' % (mm.group(1), nf(last), '/'.join(d.split('-')[2:0:-1]), int(dd)), a)
t, n2 = re.subn(r'<article class="lt-c"><div class="lt-h"><b>([A-Z0-9]+)</b>.*?</article>', fix_lt, t, flags=re.S)
open(P, 'w', encoding='utf-8').write(t)
print('bang theo doi', n, 'the', '| lenh tieu diem', n2)
