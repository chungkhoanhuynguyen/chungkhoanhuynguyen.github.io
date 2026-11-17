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
m = 0
for d, ds, fs in os.walk(ROOT):
    ds[:] = [x for x in ds if not x.startswith(('.', '_')) and x != 'node_modules']
    for f in fs:
        if not f.endswith('.html'): continue
        p = os.path.join(d, f); s = open(p, encoding='utf-8', errors='ignore').read(); s0 = s
        if '/ph.js' not in s and '</head>' in s: s = s.replace('</head>', PH + '</head>', 1)
        if 'Content-Security-Policy' in s and 'eu.i.posthog.com' not in s:
            s = s.replace("script-src 'self'", "script-src 'self' https://eu-assets.i.posthog.com", 1).replace("connect-src 'self'", "connect-src 'self' https://eu.i.posthog.com https://eu-assets.i.posthog.com", 1)
        if s != s0: open(p, 'w', encoding='utf-8').write(s); m += 1
print("gan posthog", m, "trang")
