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
            if c['k'] in ('checklist', 'bars', 'cards', 'bignum', 'chat', 'noti', 'call', 'giay'):   # giữ hình số liệu / điện thoại, tránh ảnh lạc đề
                d = {k: v for k, v in c.items() if k not in ('ch', 'say', 'moc')}; d['say'] = p
                for kk, ds in (('chat', 'msgs'), ('noti', 'items'), ('call', 'loi')):   # cảnh điện thoại nối tiếp: tin đã hiện đủ, không phát lại
                    if kk in d: d[kk] = dict(d[kk], co_san=len(d[kk].get(ds, [])))
                out.append(d)
            else:
                out.append(dict(k='text', cap=c.get('cap', ('', '')), cols=c.get('cols'), anh=c.get('anh2') or anh_mac_dinh, say=p))
    return out
