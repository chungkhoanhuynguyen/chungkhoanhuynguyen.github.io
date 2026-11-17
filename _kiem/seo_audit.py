import os,re,sys,collections,glob
root=sys.argv[1]
H=[p for p in glob.glob(root+'/**/*.html',recursive=True) if '/_video/' not in p and '/node_modules/' not in p and '/.git/' not in p]
print('html',len(H))
for f in ['robots.txt','sitemap.xml','CNAME','404.html','ads.txt','manifest.json']:
    p=os.path.join(root,f); print(f, os.path.exists(p), os.path.getsize(p) if os.path.exists(p) else '')
if os.path.exists(root+'/robots.txt'): print(open(root+'/robots.txt').read()[:400])
sm=set()
for s in glob.glob(root+'/sitemap*.xml'):
    sm|=set(re.findall(r'<loc>(.*?)</loc>',open(s,encoding='utf8',errors='ignore').read()))
print('sitemap urls',len(sm))
miss=collections.Counter(); titles=collections.defaultdict(list); descs=collections.defaultdict(list); ex=collections.defaultdict(list)
big=[];notin=[]
for p in H:
    t=open(p,encoding='utf8',errors='ignore').read(); rel=os.path.relpath(p,root)
    def chk(name,ok):
        if not ok: miss[name]+=1; ex[name].append(rel)
    m=re.search(r'<title>(.*?)</title>',t,re.S); ti=m.group(1).strip() if m else ''
    chk('title',bool(ti)); 
    if ti: titles[ti].append(rel); chk('title<=65',len(ti)<=65)
    m=re.search(r'<meta[^>]+name=["\']description["\'][^>]*content=["\'](.*?)["\']',t,re.S|re.I); d=m.group(1).strip() if m else ''
    chk('meta_desc',bool(d))
    if d: descs[d].append(rel); chk('desc 70-165',70<=len(d)<=165)
    chk('canonical','rel="canonical"' in t or "rel='canonical'" in t)
    chk('viewport','name="viewport"' in t)
    chk('lang=vi',bool(re.search(r'<html[^>]+lang=["\']vi',t)))
    chk('og:image','og:image' in t)
    chk('json-ld','application/ld+json' in t)
    h1=len(re.findall(r'<h1[\s>]',t)); chk('h1==1',h1==1)
    imgs=re.findall(r'<img\b[^>]*>',t); na=[i for i in imgs if 'alt=' not in i]; chk('img alt',not na)
    chk('noindex-free','noindex' not in t)
    if len(t)>400000: big.append((rel,len(t)//1000))
    url_guess=rel.replace('index.html','')
    if sm and not any(u.rstrip('/').endswith(url_guess.rstrip('/').replace('.html','')) or u.endswith(rel) for u in sm): notin.append(rel)
for k,v in miss.most_common(): print(f'{k}: {v} trang thiếu/sai | vd:', ex[k][:4])
dt=[(k,len(v)) for k,v in titles.items() if len(v)>1]; print('title trùng',len(dt),dt[:5])
dd=[(k[:50],len(v)) for k,v in descs.items() if len(v)>1]; print('desc trùng',len(dd),dd[:5])
print('html >400KB',big[:10])
print('không có trong sitemap',len(notin),notin[:12])
