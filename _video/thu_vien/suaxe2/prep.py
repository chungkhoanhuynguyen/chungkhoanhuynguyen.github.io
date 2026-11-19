import json, os, sys, shutil
from PIL import Image, ImageFilter, ImageEnhance
src, dst = sys.argv[1], sys.argv[2]
for n in sorted(os.listdir(src)):
    d=os.path.join(src,n); g=[f for f in os.listdir(d) if f.endswith('.gltf')]
    if not g: print('no gltf',n); continue
    J=json.load(open(os.path.join(d,g[0]))); od=os.path.join(dst,n); os.makedirs(od,exist_ok=True)
    keep=set()
    for m in J.get('materials',[]):
        p=m.get('pbrMetallicRoughness',{})
        for k in ['normalTexture','occlusionTexture','emissiveTexture']: m.pop(k,None)
        p.pop('metallicRoughnessTexture',None)
        if 'baseColorTexture' in p: keep.add(p['baseColorTexture']['index'])
    # remap textures/images
    tex=J.get('textures',[]); imgs=J.get('images',[]); newT=[]; newI=[]; tmap={}; imap={}
    for ti in sorted(keep):
        t=tex[ti]; si=t['source']
        if si not in imap:
            im=imgs[si]; fn=im['uri']; I=Image.open(os.path.join(d,fn)).convert('RGB'); I.thumbnail((512,512)); I=I.filter(ImageFilter.MedianFilter(5)); I=ImageEnhance.Color(I).enhance(1.2); base=os.path.basename(fn).rsplit('.',1)[0]+'.jpg'
            I.save(os.path.join(od,base),quality=82); imap[si]=len(newI); newI.append({'uri':base,'mimeType':'image/jpeg'})
        tmap[ti]=len(newT); nt=dict(t); nt['source']=imap[si]; newT.append(nt)
    for m in J.get('materials',[]):
        p=m.get('pbrMetallicRoughness',{})
        if 'baseColorTexture' in p: p['baseColorTexture']={'index':tmap[p['baseColorTexture']['index']]}
    J['textures']=newT; J['images']=newI
    if not newT: J.pop('textures'); J.pop('images',None); J.pop('samplers',None)
    for b in J['buffers']: shutil.copy(os.path.join(d,b['uri']),os.path.join(od,os.path.basename(b['uri']))); b['uri']=os.path.basename(b['uri'])
    json.dump(J,open(os.path.join(od,n+'.gltf'),'w'))
    print(n, sum(os.path.getsize(os.path.join(od,f)) for f in os.listdir(od))//1024,'KB')
