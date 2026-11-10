# -*- coding: utf-8 -*-
# Hậu xử lý kịch bản video dài (QL1 10/11): không cảnh nào đứng yên quá ~30s; chương không lặp; cảnh nối dùng ảnh + Ken Burns.
import re
def tach(S, max_tu=95, anh_mac_dinh='Ho Chi Minh City skyline'):
    out = []; seen = set()
    for c in S:
        c = dict(c)
        if c.get('ch') in seen: c.pop('ch')
        elif c.get('ch'): seen.add(c['ch'])
        cau = re.split(r'(?<=[.?!])\s+', c['say'].strip()); parts = []; cur = []
        for s in cau:
            if cur and len(' '.join(cur + [s]).split()) > max_tu: parts.append(' '.join(cur)); cur = []
            cur.append(s)
        if cur: parts.append(' '.join(cur))
        if c['k'] == 'end' or len(parts) == 1: out.append(c); continue
        c['say'] = parts[0]; out.append(c)
        for p in parts[1:]:
            out.append(dict(k='text', cap=c.get('cap', ('', '')), cols=c.get('cols'), anh=c.get('anh2') or c.get('anh') or anh_mac_dinh, say=p))
    return out
