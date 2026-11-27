"""Ảnh FB kiểu 'VIC metro' (anh Huy 27/11): đầu tối (tên, giá to, %), hook 2 dòng (dòng 2 nền vàng),
biểu đồ trắng có nhãn viên thuốc đen + dây dẫn, vùng tô mờ, đường đứt đoạn, chữ web góc phải dưới.
Dùng: python3 _fb/tin_chart/mk_chart.py cfg.json   (mảng cấu hình, xem mẫu out/*.json)
cfg: ra, ten, sym, gia (chuỗi), doi (chuỗi), mau_doi ('xanh'|'do'), st [[nhãn,giá trị]...], hook1, hook2,
 loai: 'nen' (ohlc: lay_gia mã + den_ngay) | 'duong' (series: [{ten,mau,diem:[[ngày,giá]...]}]),
 diem [{t,g,chu,dx,dy}], muc [{g,chu}], vung [{tren,duoi,chu,mau}], don_vi, nguon (chữ nhỏ dưới chart)."""
import sys, os, json, datetime as dt
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')); sys.path.insert(0, ROOT); sys.path.insert(0, ROOT + '/_fb/anh_lo')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, matplotlib.dates as md
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle
FD = ROOT + '/_video/engine/fonts/BeVietnamPro-'
for w in ('Medium', 'SemiBold', 'Bold', 'ExtraBold', 'Black'): fm.fontManager.addfont(FD + w + '.ttf')
plt.rcParams['font.family'] = 'Be Vietnam Pro'
UP, DN, INK = '#1f8a57', '#c43c32', '#1d1726'
D = lambda s: dt.date.fromisoformat(s)

def ve(c):
    fig = plt.figure(figsize=(10.8, 10.8), dpi=100)
    # đầu tối
    fig.patches.append(Rectangle((0, .865), 1, .135, transform=fig.transFigure, color='#0b1222', zorder=0))
    fig.text(.025, .963, c['ten'], fontsize=31, fontweight='bold', color='white', va='center')
    fig.text(.025, .925, c.get('sym', ''), fontsize=19, color='#9aa3b5', va='center')
    col = '#22c55e' if c.get('mau_doi', 'xanh') == 'xanh' else '#f05252'
    fig.text(.975, .958, c['gia'], fontsize=46, fontweight='black', color=col, ha='right', va='center')
    fig.text(.975, .918, c['doi'], fontsize=22, fontweight='bold', color=col, ha='right', va='center')
    x = .025; R = fig.canvas.get_renderer()
    for a, b in c.get('st', []):
        t = fig.text(x, .885, a, fontsize=16, color='#9aa3b5', va='center'); x += t.get_window_extent(R).width / 1080 + .008
        t = fig.text(x, .885, b, fontsize=16, fontweight='bold', color='white', va='center'); x += t.get_window_extent(R).width / 1080 + .028
    # hook
    fig.text(.5, .812, c['hook1'], fontsize=c.get('co1', 34), fontweight='black', color=INK, ha='center', va='center')
    fig.text(.5, .757, c['hook2'], fontsize=c.get('co2', 34), fontweight='black', color=INK, ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.25', fc='#ffd23f', ec='none'))
    fig.add_artist(plt.Line2D([0, 1], [.718, .718], color=INK, lw=3))
    ax = fig.add_axes([.02, .095, .89, .605]); ax.yaxis.tick_right(); ax.tick_params(labelsize=15, colors='#5f5a69', length=0)
    for s in ('top', 'left', 'bottom', 'right'): ax.spines[s].set_visible(False)
    ax.grid(color='#f1eef4', lw=1)
    if c['loai'] == 'nen':
        from lay_gia import lay
        b = [r for r in lay(c['ma'], c.get('n', 125)) if r['time'] <= c['den_ngay']]
        xs = [D(r['time']) for r in b]; w = .6
        for xx, r in zip(xs, b):
            u = r['close'] >= r['open']; cl = UP if u else DN
            ax.vlines(xx, r['low'], r['high'], color=cl, lw=1.2)
            ax.add_patch(Rectangle((md.date2num(xx) - w / 2, min(r['open'], r['close'])), w, max(abs(r['close'] - r['open']), .4), color=cl))
        cs = [r['close'] for r in b]
        for n, cl in ((20, '#d08a1e'), (50, '#6a2d86')):
            m = [None if i < n - 1 else sum(cs[i - n + 1:i + 1]) / n for i in range(len(cs))]
            ax.plot([xx for xx, v in zip(xs, m) if v], [v for v in m if v], color=cl, lw=2.6)
        lo, hi = min(r['low'] for r in b), max(r['high'] for r in b)
        ax2 = ax.twinx(); ax2.bar(xs, [r['volume'] for r in b], color=[(UP if r['close'] >= r['open'] else DN) for r in b], alpha=.3, width=.7)
        ax2.set_ylim(0, max(r['volume'] for r in b) * 5.5); ax2.set_yticks([]); ax2.yaxis.set_visible(False)
        for sp in ax2.spines.values(): sp.set_visible(False)
        ax.yaxis.tick_right(); ax.set_zorder(ax2.get_zorder() + 1); ax.patch.set_visible(False)
        ax.axhline(cs[-1], color='#6a2d86', lw=1, ls=':', alpha=.6)
    else:
        lo, hi = 1e18, -1e18
        for s in c['series']:
            xs = [D(p[0]) for p in s['diem']]; ys = [p[1] for p in s['diem']]
            ax.plot(xs, ys, color=s.get('mau', '#3b4cc0'), lw=s.get('lw', 3.2), label=s.get('ten'))
            ax.scatter([xs[-1]], [ys[-1]], s=60, color=s.get('mau', '#3b4cc0'), zorder=5)
            lo, hi = min(lo, min(ys)), max(hi, max(ys))
        if any(s.get('ten') for s in c['series']): ax.legend(loc='upper left', fontsize=15, frameon=False)
    for m in c.get('muc', []): lo, hi = min(lo, m['g']), max(hi, m['g'])
    pad = (hi - lo) * c.get('dem', .18); ax.set_ylim(lo - pad, hi + pad)
    for v in c.get('vung', []):
        ax.axhspan(v['duoi'], v['tren'], color=v.get('mau', '#c43c32'), alpha=.10, lw=0)
        ax.text(.02 if v.get('trai') else .97, v['tren'], v['chu'], transform=ax.get_yaxis_transform(), ha='left' if v.get('trai') else 'right', va='bottom', fontsize=15, fontweight='semibold', color=v.get('mau_chu', '#7a2620'))
    for m in c.get('muc', []):
        ax.axhline(m['g'], color='#8a8496', lw=1.2, ls=(0, (5, 4)))
        ax.text(.99, m['g'], ' ' + m['chu'] + ' ', transform=ax.get_yaxis_transform(), ha='right', va='center', fontsize=14, color='white', bbox=dict(boxstyle='square,pad=0.2', fc='#5f5a69', ec='none'))
    if c.get('truc_nam'): ax.xaxis.set_major_locator(md.YearLocator()); ax.xaxis.set_major_formatter(md.DateFormatter('%Y'))  # chuỗi nhiều năm (27/11)
    else: ax.xaxis.set_major_locator(md.MonthLocator()); ax.xaxis.set_major_formatter(md.DateFormatter('T%-m'))
    if c.get('y_cham'): ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: '{:,.0f}'.format(v).replace(',', '.')))
    ax.tick_params(axis='x', labelsize=17, colors=INK)
    for d in c.get('diem', []):
        xx = D(d['t']); ax.scatter([xx], [d['g']], s=90, facecolor='white', edgecolor=INK, lw=2.4, zorder=8)
        ax.annotate(d['chu'], (xx, d['g']), xytext=(d.get('dx', 30), d.get('dy', 0)), textcoords='offset points',
                    fontsize=15, fontweight='semibold', color='white', va='center', ha='left' if d.get('dx', 30) >= 0 else 'right', zorder=9,
                    bbox=dict(boxstyle='round,pad=0.45,rounding_size=0.9', fc=INK, ec='none'),
                    arrowprops=dict(arrowstyle='-', color=INK, lw=1.3, shrinkA=0, shrinkB=5))
    if c.get('don_vi'): fig.text(.92, .705, c['don_vi'], fontsize=13, color='#8a8496', ha='right')
    if c.get('nguon'): fig.text(.025, .018, c['nguon'], fontsize=13, color='#8a8496')
    fig.text(.975, .02, 'chungkhoanhuynguyen.com', fontsize=17, fontweight='semibold', color='#8a8496', ha='right')
    fig.savefig(c['ra'], dpi=100, facecolor='white'); plt.close(fig)

if __name__ == '__main__':
    for c in json.load(open(sys.argv[1], encoding='utf-8')): ve(c); print('ok', c['ra'])
