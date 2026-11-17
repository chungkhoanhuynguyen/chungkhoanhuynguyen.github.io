# Bìa reel dọc 1080x1920 (17/11, anh Huy chốt): ảnh/biểu đồ nửa trên, dòng 1 chữ trắng to, dòng 2 nền vàng, nhãn đỏ. Dùng: from bia_reel_doc import cover, chart (chạy từ thư mục gốc repo).
import sys, os, datetime as D
sys.path.insert(0,'/tmp/cw'); import hncodec
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FD='/tmp/cw/_video/anim3d/public/fonts/'; BLK=FD+'BeVietnamPro-Black.ttf'; BOLD=FD+'BeVietnamPro-ExtraBold.ttf'
P='/tmp/cw/_video/anim3d/public/'
W,H=1080,1920
def chart(sym, out, d0='2025-11-01'):
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    d=hncodec.load(f'data/c/{sym}.bin'); t=D.date.fromisoformat(d['d0']); ds=[]
    for g in d['g']: t+=D.timedelta(days=g); ds.append(t)
    S=[(a,o,h,l,c) for a,o,h,l,c in zip(ds,d['o'],d['h'],d['l'],d['c']) if a>=D.date.fromisoformat(d0)]
    try:
        for x in hncodec.load('data/c/recent.bin')['b'][sym]:
            dd=D.date.fromisoformat(x[0])
            if dd>ds[-1]: S.append((dd,*x[1:5]))
    except KeyError: pass
    f,ax=plt.subplots(figsize=(10.8,9.6),dpi=100); f.patch.set_facecolor('#1a0d36'); ax.set_facecolor('#1a0d36'); ax.axis('off')
    for i,(a,o,h,l,c) in enumerate(S):
        col='#22c55e' if c>=o else '#ef4444'; ax.plot([i,i],[l,h],color=col,lw=1.2); ax.add_patch(plt.Rectangle((i-0.35,min(o,c)),0.7,max(abs(c-o),1),color=col))
    ax.set_xlim(-2,len(S)+2); f.subplots_adjust(0,0,1,1); f.savefig(out,facecolor='#1a0d36'); plt.close(f)
def cover(img, l1, l2, badge, out):
    im=Image.new('RGB',(W,H),(26,13,54)); d=ImageDraw.Draw(im)
    for y in range(H): a=y/H; d.line([(0,y),(W,y)],fill=(int(26+30*a),int(13+8*a),int(54+40*a)))
    ph=Image.open(img).convert('RGB'); r=max(W/ph.width,1300/ph.height); ph=ph.resize((int(ph.width*r)+1,int(ph.height*r)+1))
    ph=ph.crop(((ph.width-W)//2,(ph.height-1300)//2,(ph.width-W)//2+W,(ph.height-1300)//2+1300))
    m=Image.new('L',(W,1300)); md=ImageDraw.Draw(m)
    for y in range(1300): md.line([(0,y),(W,y)],fill=int(255*min(1,(1300-y)/380)))
    im.paste(ph,(0,120),m)
    d=ImageDraw.Draw(im)
    # logo
    fl=ImageFont.truetype(BLK,46); d.text((W//2,70),'HUY NGUYỄN',font=fl,fill=(255,204,0),anchor='mm')
    def fit(txt,maxw,size):
        while size>60:
            f=ImageFont.truetype(BLK,size)
            if d.textlength(txt,font=f)<=maxw: return f
            size-=4
        return ImageFont.truetype(BLK,size)
    y=1330
    f1=fit(l1,1000,170); d.text((W//2,y),l1,font=f1,fill='white',anchor='mm',stroke_width=8,stroke_fill=(20,8,40)); y+=f1.size+40
    f2=fit(l2,960,130); tw=d.textlength(l2,font=f2); bx=[W//2-tw/2-30,y-f2.size*0.62,W//2+tw/2+30,y+f2.size*0.62]
    d.rounded_rectangle(bx,18,fill=(255,204,0)); d.text((W//2,y),l2,font=f2,fill=(26,13,54),anchor='mm'); y+=f2.size+70
    if badge:
        fb=fit(badge,820,92); tw=d.textlength(badge,font=fb); bx=[W//2-tw/2-40,y-fb.size*0.7,W//2+tw/2+40,y+fb.size*0.7]
        d.rounded_rectangle(bx,60,fill=(226,46,46)); d.text((W//2,y),badge,font=fb,fill='white',anchor='mm')
    im.convert('RGB').save(out,quality=88)
