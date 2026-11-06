import numpy as np, wave, subprocess, os
SR=44100
def f(m): return 440*2**((m-69)/12)
def violin(freq, dur, vib=5.5, vd=0.004, att=0.06, rel=0.12, bright=1.0):
    t=np.arange(int(SR*dur))/SR
    ph=2*np.pi*np.cumsum(freq*(1+vd*np.sin(2*np.pi*vib*t)*np.clip(t/0.25,0,1)))/SR
    x=sum((1/k**(1.15/bright))*np.sin(k*ph) for k in range(1,14))
    x+=0.02*np.random.randn(len(t))*np.clip(1-t/dur,0,1)  # tiếng vĩ
    env=np.minimum(1,t/att)*np.minimum(1,(dur-t)/rel).clip(0,1)
    return x*env
def cello(freq,dur,**k): return violin(freq,dur,vib=4.5,vd=0.003,bright=0.8,**k)
def place(buf,x,t0,g=1.0):
    i=int(t0*SR); j=min(len(buf),i+len(x)); buf[i:j]+=g*x[:j-i]
def drum(dur):
    t=np.arange(int(SR*dur))/SR; return np.sin(2*np.pi*55*t*np.exp(-t*3))*np.exp(-t*7)
SC={'min':[0,2,3,5,7,8,10],'harm':[0,2,3,5,7,8,11],'phryg':[0,1,3,5,7,8,10]}
PROG=[[0,5,3,4],[0,3,5,4],[0,5,6,4],[0,6,3,4],[0,4,5,3]]
def make(i,name,root,bpm,mode,style,prog,L=32):
    rng=np.random.default_rng(i); sc=SC[mode]; beat=60/bpm; buf=np.zeros(int(SR*(L+2))); bar=4*beat
    nb=int(L/bar)
    for b in range(nb):
        deg=prog[b%4]; t0=b*bar; r=root+sc[deg%7]
        chord=[r-24, r-12, r-12+sc[(deg+2)%7]-sc[deg%7]+(12 if sc[(deg+2)%7]<sc[deg%7] else 0)]
        # nền cello/viola giữ hợp âm
        for m in chord: place(buf,cello(f(m),bar*1.02,att=0.3,rel=0.4),t0,0.18)
        if style=='ostinato':   # spiccato 16th dồn dập
            for k in range(16): place(buf,violin(f(r+[0,7,12,7][k%4]),beat/4*0.9,att=0.008,rel=0.03,vd=0.0),t0+k*beat/4,0.22)
        elif style=='tremolo':
            for k in range(32): place(buf,violin(f(r+12),beat/8,att=0.004,rel=0.02,vd=0),t0+k*beat/8,0.15)
        elif style=='march':
            for k in range(8): place(buf,violin(f(r+(12 if k%2 else 0)),beat/2*0.7,att=0.01,rel=0.05,vd=0),t0+k*beat/2,0.22)
            for k in range(4): place(buf,drum(0.5),t0+k*beat,0.5 if k%2==0 else 0.3)
        elif style=='pizz':
            for k in range(8): place(buf,violin(f(r+rng.choice([0,3,7,12])),0.12,att=0.002,rel=0.1,vd=0),t0+k*beat/2,0.3)
        # giai điệu violin chính (legato, lên cao dần)
        if style in ('ostinato','tremolo','march','lament','epic','pizz'):
            if b>=(1 if style!='lament' else 0):
                notes=rng.choice([0,2,4,5,7],size=2 if bpm>110 else 4); dur=bar/len(notes)
                for q,n in enumerate(notes):
                    m=root+12+sc[(deg+int(n))%7]+(12 if b>=nb//2 else 0)
                    place(buf,violin(f(m),dur*1.05,att=0.05),t0+q*dur,0.28)
        if style=='epic' and b%2==0: place(buf,drum(1.2),t0,0.7)
    # đẩy cao trào: tăng âm lượng nửa sau
    env=np.linspace(0.75,1.15,len(buf)); buf*=env
    # reverb đơn giản
    for d,g in ((0.031,0.35),(0.047,0.28),(0.071,0.22),(0.113,0.15)):
        k=int(d*SR); buf[k:]+=g*buf[:-k]
    buf=buf[:int(SR*L)]; fo=int(SR*1.5); buf[-fo:]*=np.linspace(1,0,fo)
    buf/=np.abs(buf).max()*1.12
    st=np.stack([buf,np.roll(buf,180)],1)
    w=f"{i:02d}_{name}.wav"
    with wave.open(w,'wb') as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((st*32767).astype('<i2').tobytes())
    subprocess.run(['ffmpeg','-v','error','-y','-i',w,'-b:a','160k',w[:-4]+'.mp3']); os.remove(w)
L=[('ostinato_rao_riet',50,140,'min','ostinato',0),('ostinato_harmonic',52,150,'harm','ostinato',2),
('tremolo_cang_thang',45,90,'min','tremolo',1),('tremolo_phrygian',47,84,'phryg','tremolo',3),
('hanh_quan_violin',50,112,'min','march',0),('hanh_quan_trong',48,100,'harm','march',4),
('bi_trang_lament',45,66,'min','lament',1),('bi_trang_harmonic',43,60,'harm','lament',2),
('hung_trang_epic',50,96,'min','epic',0),('epic_phrygian',52,92,'phryg','epic',3),
('pizzicato_bi_an',57,108,'min','pizz',1),('pizzicato_trinh_tham',55,120,'harm','pizz',4),
('ostinato_cuc_nhanh',53,168,'min','ostinato',3),('tremolo_bao_to',50,100,'harm','tremolo',0),
('hanh_quan_phrygian',52,120,'phryg','march',1),('lament_sau_lang',41,56,'min','lament',4),
('epic_cao_trao',47,104,'harm','epic',2),('pizz_hoi_hop',52,132,'phryg','pizz',0),
('ostinato_tin_nong',48,128,'min','ostinato',4),('epic_thoi_su',45,88,'min','epic',1)]
for i,(n,r,b,m,s,p) in enumerate(L,1): make(i,n,r,b,m,s,PROG[p])
