import sys; sys.path.insert(0,"/tmp/cw")
import datetime as dt, hncodec, numpy as np
sys.path.insert(0,'/tmp/cw')
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from PIL import Image, ImageDraw, ImageFont, ImageFilter
F='/tmp/cw/_video/engine/fonts/'
for f in ['BeVietnamPro-SemiBold.ttf','BeVietnamPro-ExtraBold.ttf']: fm.fontManager.addfont(F+f)
plt.rcParams['font.family']='Be Vietnam Pro'
def fnt(w,s): return ImageFont.truetype(F+{'b':'BeVietnamPro-Black.ttf','x':'BeVietnamPro-ExtraBold.ttf','s':'BeVietnamPro-SemiBold.ttf'}[w],s)
VANG=(242,207,116); TIM1=(31,20,51); TIM2=(79,43,112)
def series(s):
    d=hncodec.load(f'/tmp/cw/data/c/{s}.bin'); t=dt.date.fromisoformat(d['d0']); ds=[]
    for g in d['g']: t+=dt.timedelta(days=g); ds.append(t)
    px=dict(zip(ds,[x/100 for x in d['c']]))
    for r in hncodec.load('/tmp/cw/data/c/recent.bin')['b'][s]: px[dt.date.fromisoformat(r[0])]=r[4]/100
    k=sorted(px); return k,[px[x] for x in k]
def nen():
    im=Image.new('RGB',(1080,1080)); a=np.linspace(0,1,1080)[:,None]
    arr=(np.array(TIM1)[None,None,:]*(1-a[...,None])+np.array(TIM2)[None,None,:]*a[...,None]).repeat(1080,1).astype('uint8')
    return Image.fromarray(arr)
def khung(chart, l1, l2, nhan, dong_nho, out):
    im=nen(); d=ImageDraw.Draw(im)
    d.text((60,52),"HUY NGUYỄN",font=fnt('b',34),fill='white'); d.text((60+d.textlength("HUY NGUYỄN",font=fnt("b",34))+16,60),"CHỨNG KHOÁN",font=fnt('s',26),fill=(200,180,230))
    d.rectangle([60,100,180,106],fill=VANG)
    w=d.textlength(nhan,font=fnt('x',30)); d.rounded_rectangle([1020-w-36,48,1020,98],25,fill=VANG); d.text((1020-w-18,55),nhan,font=fnt('x',30),fill=TIM1)
    y=135
    for t,c,s in ((l1,'white',74),(l2,VANG,74)):
        f=fnt('b',s)
        while d.textlength(t,font=f)>960: s-=4; f=fnt('b',s)
        d.text((60,y),t,font=f,fill=c); y+=s+14
    ch=Image.open(chart).convert('RGB'); ch=ch.resize((960,int(ch.height*960/ch.width)))
    m=Image.new('L',ch.size,0); ImageDraw.Draw(m).rounded_rectangle([0,0,ch.width-1,ch.height-1],22,fill=255)
    im.paste(ch,(60,y+16),m); y2=y+16+ch.height+18
    for t in dong_nho: d.text((60,y2),t,font=fnt('s',30),fill=(235,228,245)); y2+=44
    t="chungkhoanhuynguyen.com"; w=d.textlength(t,font=fnt('s',24)); d.text((1020-w,1035),t,font=fnt('s',24),fill=(200,180,230))
    im.save(out,quality=92); print(out,y2)
def ve_line(s, tu, mocs, path, ylab='nghìn đồng'):
    k,v=series(s); i0=next(i for i,x in enumerate(k) if x>=tu); k,v=k[i0:],v[i0:]
    fig,ax=plt.subplots(figsize=(9.6,5.8),dpi=110); fig.patch.set_facecolor('white')
    ax.plot(k,v,color='#4f2b70',lw=2.6); ax.fill_between(k,v,min(v)*0.9,color='#4f2b70',alpha=.08)
    for (dd,txt,c,dy) in mocs:
        j=min(range(len(k)),key=lambda i:abs((k[i]-dd).days)); ax.scatter([k[j]],[v[j]],s=70,color=c,zorder=5)
        ax.annotate(txt,(k[j],v[j]),xytext=(0,dy),textcoords='offset points',ha='center',fontsize=13,fontweight='bold',color='white',
            bbox=dict(boxstyle='round,pad=0.35',fc='#1f1433',ec='none'),arrowprops=dict(arrowstyle='-',color='#1f1433',ls='--',lw=1.2))
    ax.spines[['top','right']].set_visible(False); ax.grid(axis='y',alpha=.25); ax.set_ylabel(ylab,fontsize=11); ax.tick_params(labelsize=11)
    ax.set_ylim(min(v)*0.85,max(v)*1.18); fig.tight_layout(); fig.savefig(path); plt.close(fig); return k,v
