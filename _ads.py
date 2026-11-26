# Gắn mã Google AdSense (ca-pub-1473458130993450) vào <head> mọi trang .html. Chạy sau mọi bước sinh trang.
import os, re
ROOT = os.path.dirname(os.path.abspath(__file__))
PUB = "ca-pub-1473458130993450"
TAG = ('<meta name="google-adsense-account" content="%s">\n'
       '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=%s" crossorigin="anonymous"></script>\n') % (PUB, PUB)
n = 0
for d, ds, fs in os.walk(ROOT):
    ds[:] = [x for x in ds if not x.startswith(('.', '_')) and x != 'node_modules']
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf-8', errors='ignore').read()
        if PUB in s or '</head>' not in s: continue
        s = s.replace('</head>', TAG + '</head>', 1); open(p, 'w', encoding='utf-8').write(s); n += 1
open(os.path.join(ROOT, 'ads.txt'), 'w').write("google.com, pub-1473458130993450, DIRECT, f08c47fec0942fa0\n")
print("gan adsense", n, "trang")

# PostHog (đo khách, 17/11/2026): gắn /ph.js mọi trang + mở CSP cho PostHog EU.
PH = '<script src="/ph.js" defer></script>\n'
PA, PC = "https://eu-assets.i.posthog.com", "https://eu.i.posthog.com"
def csp_ph(s):
    """(25/11 QL1) Bản cũ chỉ vá khi thấy đúng chuỗi "script-src 'self'" và bỏ qua trang đã có posthog ở connect-src
    → 556/814 trang (mã CP, F0, bài học, mở tài khoản…) bị CSP chặn PostHog, không đo được khách. Giờ vá theo từng chỉ thị."""
    m = re.search(r'(<meta http-equiv="Content-Security-Policy" content=")([^"]*)(")', s)
    if not m: return s
    ds = [x.strip() for x in m.group(2).split(';') if x.strip()]
    d = {x.split()[0]: x.split()[1:] for x in ds}; order = [x.split()[0] for x in ds]
    sc = [v for v in d.get('script-src', ["'self'"]) if v != "'none'"]
    for v in ("'self'", PA):
        if v not in sc: sc.append(v)
    cn = [v for v in d.get('connect-src', ["'self'"]) if v != "'none'"]
    for v in ("'self'", PC, PA):
        if v not in cn: cn.append(v)
    for k, v in (('script-src', sc), ('connect-src', cn)):
        if k not in d: order.insert(1, k)
        d[k] = v
    out = '; '.join(k + (' ' + ' '.join(d[k]) if d[k] else '') for k in order)
    return s[:m.start(2)] + out + s[m.end(2):]
m = 0
for d, ds, fs in os.walk(ROOT):
    ds[:] = [x for x in ds if not x.startswith(('.', '_')) and x != 'node_modules']
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf-8', errors='ignore').read(); s0 = s
        if '/ph.js' not in s and '</head>' in s: s = s.replace('</head>', PH + '</head>', 1)
        s = csp_ph(s)
        if s != s0: open(p, 'w', encoding='utf-8').write(s); m += 1
print("gan posthog", m, "trang")

# Google Analytics 4 (26/11/2026, anh Huy duyệt "tạo GA"): tài sản chungkhoanhuynguyen.com, luồng web, mã G-SZC87T98J3.
# Gắn mọi trang (trừ trang nhận định riêng tư) + mở CSP. ph.js gọi gtag("event", …) cho zalo_1_1, zalo_nhom, mo_tk, soi_ma.
GA_ID = "G-SZC87T98J3"
GA = ('<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>\n'
      '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","%s");</script>\n') % (GA_ID, GA_ID)
GT = "https://www.googletagmanager.com"
GAC = ("https://*.google-analytics.com", "https://*.analytics.google.com", GT)
def csp_ga(s):
    m = re.search(r'(<meta http-equiv="Content-Security-Policy" content=")([^"]*)(")', s)
    if not m: return s
    ds = [x.strip() for x in m.group(2).split(';') if x.strip()]
    d = {x.split()[0]: x.split()[1:] for x in ds}; order = [x.split()[0] for x in ds]
    add = {'script-src': (GT, "'unsafe-inline'"), 'connect-src': GAC, 'img-src': ("https://*.google-analytics.com", GT)}
    for k, vs in add.items():
        cur = [v for v in d.get(k, ["'self'"]) if v != "'none'"]
        for v in vs:
            if v not in cur: cur.append(v)
        if k not in d: order.insert(1, k)
        d[k] = cur
    out = '; '.join(k + (' ' + ' '.join(d[k]) if d[k] else '') for k in order)
    return s[:m.start(2)] + out + s[m.end(2):]
g = 0
for d, ds, fs in os.walk(ROOT):
    ds[:] = [x for x in ds if not x.startswith(('.', '_')) and x not in ('node_modules', 'nhandinhthitruong')]
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf-8', errors='ignore').read(); s0 = s
        if GA_ID not in s and '<head' in s and '</head>' in s:
            s = re.sub(r'(<head[^>]*>)', lambda mm: mm.group(1) + '\n' + GA, s, count=1)
        s = csp_ga(s)
        if s != s0: open(p, 'w', encoding='utf-8').write(s); g += 1
print("gan GA4", g, "trang")

# (26/11 Phòng Web, soát điện thoại) Nút/link chạm <24px trên khổ điện thoại: chữ F0 ở thanh menu, mã CP trong bảng/đoạn
# "Mã cổ phiếu khác", chữ cái mục lục Từ điển F0, link chủ đề chân trang. Sửa gốc 1 chỗ: gắn 1 khối CSS chung mọi trang.
TAP = ('<style id="tap24">@media(max-width:760px){.nav a{display:inline-block;padding:6px 0;min-width:24px;text-align:center}'
       'td a[href^="/ma/"],p a[href^="/ma/"],li a[href^="/ma/"],.az a{display:inline-block;min-width:24px;min-height:24px;line-height:24px;text-align:center}'
       '.meta a[href^="#k"]{display:inline-block;min-width:24px;min-height:24px;line-height:24px;text-align:center}'
       '.kw a{display:inline-block;padding:5px 0}}</style>\n')
t = 0
for d, ds, fs in os.walk(ROOT):
    ds[:] = [x for x in ds if not x.startswith(('.', '_')) and x not in ('node_modules', 'nhandinhthitruong', 'thienkiemmon', 'thuthanhlacduong')]
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf-8', errors='ignore').read(); s0 = s
        if '</head>' not in s or TAP in s: continue
        s = re.sub(r'<style id="tap24">.*?</style>\n?', '', s, flags=re.S)
        s = s.replace('</head>', TAP + '</head>', 1)
        if s != s0: open(p, 'w', encoding='utf-8').write(s); t += 1
print("gan CSS cham 24px", t, "trang")

# A3 (26/11 Phòng Web): thanh "Nhắn Zalo" + "Soi mã miễn phí" cố định đáy màn hình điện thoại – /hnbar.js mọi trang nội dung.
BAR = '<script src="/hnbar.js" defer></script>\n'
nb = 0
for d, ds, fs in os.walk(ROOT):
    ds[:] = [x for x in ds if not x.startswith(('.', '_')) and x not in ('node_modules', 'nhandinhthitruong', 'thienkiemmon', 'thuthanhlacduong', 'game', 'loanthelanhchua')]
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf-8', errors='ignore').read()
        if '/hnbar.js' in s or '</head>' not in s: continue
        s = s.replace('</head>', BAR + '</head>', 1); open(p, 'w', encoding='utf-8').write(s); nb += 1
print("gan thanh nut day", nb, "trang")
