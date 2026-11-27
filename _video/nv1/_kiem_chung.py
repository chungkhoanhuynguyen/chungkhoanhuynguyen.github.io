# Kiểm chung kịch bản video dài NV1 (exec trong __main__ của ql_*.py)
from collections import Counter
cnt = Counter(c['k'] for c in S)
print('so chu', lib.dem(S), 'canh', len(S), dict(cnt), 'tieu de', len(TIEU))
for b in ('badge', 'badge_b', 'badge_c'): print(b, len(META[KEY][b]))
for b in ('bia_hook', 'bia_hook_b', 'bia_hook_c'): print(b, [len(x) for x in META[KEY][b]])
import kiem_loi, kiem_goi
print('goi', kiem_goi.kiem(TIEU, META[KEY]['bia_hook']))
for q in kiem_loi.kiem([{"loi": c['say']} for c in S], None, False):
    if 'câu cụt' not in q: print(q)
from xung_ho import le_phep
for c in S:
    if le_phep(c['say']) != c['say']: print('XUNG_HO', c['say'][:80])
for c in S:
    for x in c.get('cap', ()):
        if len(x) > 32: print('CAP DAI', len(x), x)
    for x in c.get('items', ()):
        if len(x[0]) > 32: print('ITEM DAI', len(x[0]), x[0])
    for cd in c.get('cards', ()):
        for x in cd:
            if len(x) > 30: print('CARD DAI', len(x), x)
    for x in c.get('bars', ()):
        if len(x[0]) > 16: print('BAR DAI', len(x[0]), x[0])
if os.environ.get('SO'):
    import so_chu
    for c in S:
        t = so_chu.doi(c['say'])
        import re
        for ln in re.split(r'(?<=[.?!])\s+', t):
            if re.search(r'\d', ln): print('SO|', ln)
if os.environ.get('KB'):
    with open(os.environ['KB'], 'w', encoding='utf-8') as f:
        f.write('TIÊU ĐỀ: ' + TIEU + '\n3 BÌA: %s / %s / %s\n\n' % (META[KEY]['bia_hook'], META[KEY]['bia_hook_b'], META[KEY]['bia_hook_c']))
        for i, c in enumerate(S):
            tm = {k: v for k, v in c.items() if k in ('cap', 'noti', 'giay', 'cards', 'bars', 'items', 'chat', 'call', 'top', 'sub', 'value', 'unit', 'label')}
            f.write('--- CẢNH %d [%s] %s\nCHỮ TRÊN MÀN: %s\nLỜI ĐỌC: %s\n\n' % (i + 1, c['k'], c.get('ch', ''), json.dumps(tm, ensure_ascii=False), c['say']))
        f.write('MÔ TẢ + NGUỒN:\n' + MT + '\n\nGHI CHÚ NGUỒN ĐẦU SCRIPT:\n' + ''.join(l for l in open(__file__, encoding='utf-8').readlines()[:30]))
