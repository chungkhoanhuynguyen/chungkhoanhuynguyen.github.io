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
