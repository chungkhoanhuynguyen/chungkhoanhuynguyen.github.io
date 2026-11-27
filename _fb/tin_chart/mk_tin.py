import sys, io, json, datetime as dt
import os; ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'../..')); sys.path.insert(0,ROOT); import hncodec as h
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from PIL import Image, ImageDraw, ImageFont
FD=ROOT+'/_video/engine/fonts/BeVietnamPro-'
for w in ('Bold','SemiBold','Black','Medium'): fm.fontManager.addfont(FD+w+'.ttf')
plt.rcParams['font.family']='Be Vietnam Pro'
F=lambda w,s: ImageFont.truetype(FD+w+'.ttf',s)
W,H=1080,1350; BG=(11,18,34); Y=(255,204,0)
def wrap(d,t,f,mw):
    out=[];
    for para in t.split('\n'):
        cur=''
        for wd in para.split():
            tt=(cur+' '+wd).strip()
            if d.textlength(tt,font=f)<=mw: cur=tt
            else: out.append(cur); cur=wd
        out.append(cur)
    return out
def card(fig_png, nhan, hook1, hook2, tin, nguon, out):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    f=F('Bold',26); tw=d.textlength(nhan,font=f); d.rounded_rectangle((W/2-tw/2-18,40,W/2+tw/2+18,84),12,fill=(200,40,40)); d.text((W/2,62),nhan,font=f,fill='white',anchor='mm')
    y=110
    for t,c in ((hook1,Y),(hook2,'white')):
        s=86; f=F('Black',s)
        while d.textlength(t,font=f)>W-80: s-=2; f=F('Black',s)
        d.text((W/2,y+s/2),t,font=f,fill=c,anchor='mm',stroke_width=3,stroke_fill=(0,0,0)); y+=s+14
    y+=14; f=F('Bold',34); lines=wrap(d,tin,f,W-140); bh=len(lines)*46+70
    d.rounded_rectangle((40,y,W-40,y+bh),18,fill='white'); d.rectangle((40,y,52,y+bh),fill=(200,40,40))
    yy=y+22
    for l in lines: d.text((76,yy),l,font=f,fill=(15,15,15)); yy+=46
    d.text((76,yy+2),nguon,font=F('Medium',22),fill=(110,110,110)); y+=bh+24
    ch=Image.open(fig_png).convert('RGB'); avail=H-y-70; r=min((W-80)/ch.width,avail/ch.height); ch=ch.resize((int(ch.width*r),int(ch.height*r)),Image.LANCZOS)
    d.rounded_rectangle((40,y,W-40,y+ch.height+20),18,fill='white'); im.paste(ch,(int(W/2-ch.width/2),y+10))
    d.text((W-44,H-36),'chungkhoanhuynguyen.com',font=F('SemiBold',24),fill=(170,170,190),anchor='rm')
    im.save(out,quality=93)
def bars(labels,vals,cols,txt,title,fn,unit,gap=''):
    fig,ax=plt.subplots(figsize=(10,6.2),dpi=110)
    b=ax.bar(labels,vals,color=cols,width=0.55)
    for r,t in zip(b,txt): ax.text(r.get_x()+r.get_width()/2,r.get_height()*1.01,t,ha='center',va='bottom',fontsize=24,fontweight='bold')
    ax.set_ylim(min(vals)*0.8,max(vals)*1.12); ax.set_title(title,fontsize=20,fontweight='bold',loc='left',pad=14)
    ax.tick_params(axis='x',labelsize=19); ax.tick_params(axis='y',labelsize=14); ax.set_ylabel(unit,fontsize=14)
    for s in ('top','right'): ax.spines[s].set_visible(False)
    ax.grid(axis='y',alpha=.25)
    if gap: ax.text(0.5,(vals[0]+vals[1])/2,gap,ha='center',va='center',fontsize=26,fontweight='bold',color='white',bbox=dict(boxstyle='round,pad=0.4',fc='#c43c32',ec='none'))
    fig.tight_layout(); fig.savefig(fn); plt.close(fig)

# Dùng: python3 _fb/tin_chart/mk_tin.py cfg.json  (mỗi phần tử 1 ảnh)
# {"ra":"out.jpg","nhan":"ĐIỀU TRA · 27/11/2026","hook1":"…","hook2":"…???","tin":"tóm tắt tin như tiêu đề báo","nguon":"Nguồn: … ngày …",
#  "chart":{"kieu":"cot","nhan":["A","B"],"so":[134.2,112.1],"chu":["134,2 tr","112,1 tr"],"mau":["#c9a227","#8a8f99"],"tieu_de":"…","don_vi":"…","chenh":"CHÊNH 22,1 TRIỆU"}
#   hoặc {"kieu":"duong","ngay":["2026-09-01",…],"so":[…],"tieu_de":"…","ghi":"26/11: 1.629,68\n−57,77 điểm"}}
def duong(c,fn):
    import matplotlib.dates as md
    x=[dt.date.fromisoformat(s) for s in c['ngay']]; v=c['so']
    fig,ax=plt.subplots(figsize=(10,6.2),dpi=110); ax.plot(x,v,color='#3b4cc0',lw=3); ax.fill_between(x,v,min(v)*0.98,color='#3b4cc0',alpha=.08)
    ax.scatter([x[-1]],[v[-1]],s=140,color='#c43c32',zorder=5)
    if c.get('ghi'): ax.annotate(c['ghi'],(x[-1],v[-1]),xytext=(-330,-10),textcoords='offset points',fontsize=20,fontweight='bold',color='#c43c32',arrowprops=dict(arrowstyle='->',color='#c43c32',lw=2))
    ax.set_title(c.get('tieu_de',''),fontsize=20,fontweight='bold',loc='left',pad=14); ax.xaxis.set_major_formatter(md.DateFormatter('%d/%m')); ax.tick_params(labelsize=14)
    for s in ('top','right'): ax.spines[s].set_visible(False)
    ax.grid(alpha=.25); fig.tight_layout(); fig.savefig(fn); plt.close(fig)
if __name__=='__main__':
    import tempfile
    for a in json.load(open(sys.argv[1],encoding='utf-8')):
        c=a['chart']; fn=tempfile.mktemp(suffix='.png')
        if c['kieu']=='cot': bars(c['nhan'],c['so'],c.get('mau',['#c9a227','#8a8f99']),c['chu'],c.get('tieu_de',''),fn,c.get('don_vi',''),c.get('chenh',''))
        else: duong(c,fn)
        card(fn,a['nhan'],a['hook1'],a['hook2'],a['tin'],a['nguon'],a['ra']); print('ok',a['ra'])
