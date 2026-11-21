# Anh "so lo" kieu man hinh app chung khoan cho FB chinh (QL1 21/11)
import sys, json
from PIL import Image, ImageDraw, ImageFont
IF="/usr/share/fonts/opentype/inter/"
def F(w,s): return ImageFont.truetype(IF+{"r":"Inter-Regular.otf","s":"Inter-SemiBold.otf","b":"Inter-Bold.otf","x":"Inter-ExtraBold.otf"}[w],s)
SERIF=lambda s: ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",s)
W,H=1080,1350
BG=(24,26,31); RED=(242,54,69); GRN=(8,196,120); ORG=(245,166,35); BLU=(41,121,255); GRY=(140,146,160)
def vnd(x): return f"{x:,.0f}"
def ve(c, out):
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    up=c["thaydoi"]>=0; MC=GRN if up else RED
    # header
    d.rounded_rectangle((30,40,110,120),40,fill=(55,58,66)); d.text((70,80),"‹",font=F("b",60),fill="white",anchor="mm")
    d.text((140,52),c["ten"],font=F("s",36),fill="white"); d.text((140,98),c["ma"]+" ("+c["san"]+")",font=F("r",30),fill=(200,204,212))
    d.line((0,150,W,150),fill=(45,48,55),width=2)
    d.text((40,170),f'{c["gia"]/1000:.2f}',font=F("x",110),fill=MC)
    s=f'{"▲" if up else "▼"} {c["thaydoi"]/1000:+.2f} ({c["thaydoi"]/(c["gia"]-c["thaydoi"])*100:+.2f}%)'
    tw=d.textlength(f'{c["gia"]/1000:.2f}',font=F("x",110))
    d.rounded_rectangle((60+tw,205,60+tw+d.textlength(s,font=F("s",38))+30,265),8,fill=(70,30,35) if not up else (20,60,45))
    d.text((75+tw,212),s,font=F("s",38),fill=MC)
    # card
    y0=320; d.rounded_rectangle((20,y0,W-20,y0+250),14,fill="white")
    pc=c["pct"]; PC=RED if pc<0 else GRN
    cols=[(50,c["ma"]),(300,f'{c["vao"]/1000:.2f}'),(520,f'{c["gia"]/1000:.2f}'),(680,vnd(c["sl"]))]
    for x,t in cols: d.text((x,y0+28),t,font=F("b",40),fill=RED if t==c["ma"] else (30,30,30))
    d.text((W-50,y0+28),f'{pc:+.2f}%',font=F("b",40),fill=PC,anchor="ra")
    for x,t in [(300,c["nhan_vao"]),(520,"Giá hiện tại"),(680,"Số lượng")]: d.text((x,y0+80),t,font=F("r",22),fill=GRY)
    d.rounded_rectangle((40,y0+120,W-40,y0+235),12,fill=(244,246,250))
    for i,(lb,v,colr) in enumerate([(c["l1"],vnd(c["v1"]),(30,30,30)),(c["l2"],vnd(c["v2"]),(30,30,30)),(c["l3"],("+" if c["v3"]>0 else "")+vnd(c["v3"]),PC)]):
        cx=40+(W-80)*(2*i+1)/6
        d.text((cx,y0+148),lb,font=F("r",26),fill=(90,95,105),anchor="mm"); d.text((cx,y0+198),v,font=F("b",34),fill=colr,anchor="mm")
    # chart
    cl=c["close"]; n=len(cl); cx0,cx1,cy0,cy1=40,W-130,760,1200
    o=[cl[0]]+cl[:-1]; hi=[max(a,b)*1.004 for a,b in zip(o,cl)]; lo=[min(a,b)*0.996 for a,b in zip(o,cl)]
    def ma(k): return [sum(cl[max(0,i-k+1):i+1])/len(cl[max(0,i-k+1):i+1]) for i in range(n)]
    m10,m50=ma(10),ma(50)
    vmax=max(max(hi),max(m50))*1.03; vmin=min(lo)*0.9
    Y=lambda v: cy1-(v-vmin)/(vmax-vmin)*(cy1-cy0); X=lambda i: cx0+(i+0.5)*(cx1-cx0)/n
    wm=F("x",230); d.text(((cx0+cx1)/2,(cy0+cy1)/2),c["ma"],font=wm,fill=(34,37,44),anchor="mm")
    for k in range(5):
        v=vmin+(vmax-vmin)*k/4; d.line((cx0,Y(v),cx1,Y(v)),fill=(40,43,50),width=1)
        d.text((W-20,Y(v)),f"{v/1000:.0f}",font=F("r",24),fill=GRY,anchor="rm")
    bw=max(2,(cx1-cx0)/n*0.6)
    for i in range(n):
        col=GRN if cl[i]>=o[i] else RED
        d.line((X(i),Y(hi[i]),X(i),Y(lo[i])),fill=col,width=2)
        d.rectangle((X(i)-bw/2,Y(max(o[i],cl[i])),X(i)+bw/2,max(Y(min(o[i],cl[i])),Y(max(o[i],cl[i]))+2)),fill=col)
    d.line([(X(i),Y(m50[i])) for i in range(n)],fill=BLU,width=4); d.line([(X(i),Y(m10[i])) for i in range(n)],fill=ORG,width=3)
    yl=Y(cl[-1]); 
    for xx in range(int(X(n-1)),cx1+10,14): d.line((xx,yl,xx+7,yl),fill=MC,width=2)
    d.rounded_rectangle((cx1+8,yl-22,W-8,yl+22),6,fill=MC); d.text(((cx1+8+W-8)/2,yl),f'{cl[-1]/1000:.2f}',font=F("b",26),fill="white",anchor="mm")
    d.text((cx0,cy0-25),f'MA10 {m10[-1]/1000:.2f}',font=F("s",26),fill=ORG); d.text((cx0+190,cy0-25),f'MA50 {m50[-1]/1000:.2f}',font=F("s",26),fill=BLU)
    for i,lb in c["moc"]: d.text((X(i),cy1+18),lb,font=F("r",24),fill=GRY,anchor="ma")
    # meme bubble
    f=SERIF(64); t=c["meme"]; tw=d.textlength(t,font=f)
    bx=(W-tw)/2-30; d.rounded_rectangle((bx,595,bx+tw+60,685),18,fill="white"); d.text((W/2,640),t,font=f,fill="black",anchor="mm")
    d.text((W/2,1290),c["chu_thich"],font=F("r",22),fill=(120,125,138),anchor="mm")
    d.text((W-30,H-20),"Chứng Khoán Huy Nguyễn",font=F("s",22),fill=(90,95,108),anchor="rd")
    im.save(out,quality=92)
if __name__=="__main__":
    for c in json.load(open(sys.argv[1],encoding="utf-8")): ve(c,c["ma"]+"_lo.jpg")
