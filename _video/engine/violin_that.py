# 20 mẫu nhạc violin THẬT: dùng mẫu thu âm dàn dây VSCO 2 Community Edition (CC0, Versilian Studios)
# Chạy trên GitHub Actions: python violin_that.py <thư_mục_VSCO> <out>
import sys, os, re, glob, json, subprocess, numpy as np, soundfile as sf
V, OUT = sys.argv[1], sys.argv[2]; os.makedirs(OUT, exist_ok=True); SR = 44100
NOTE = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
def midi(name):
    m = re.search(r'(?<![A-Za-z])([A-G])(#|b|s)?(-?\d)(?!\d)', name)
    if not m: return None
    n = NOTE[m.group(1)] + {'#':1,'s':1,'b':-1}.get(m.group(2) or '', 0)
    return 12*(int(m.group(3))+1)+n
wavs = [w for w in glob.glob(os.path.join(V, '**', '*.wav'), recursive=True)]
log = {}
def bank(inst_kw, art_kw, excl=()):
    B = {}
    for w in wavs:
        p = w.lower()
        if not any(k in p for k in inst_kw) or not any(k in p for k in art_kw) or any(k in p for k in excl): continue
        m = midi(os.path.basename(w))
        if m is None: continue
        B.setdefault(m, []).append(w)
    log['/'.join(inst_kw)+':'+'/'.join(art_kw)] = sorted(B)
    return B
VLN = ('violin', 'vln')
SUS = bank(VLN, ('sus', 'legato', 'arco', 'vib'), ('spic', 'pizz', 'trem', 'stac', 'harm'))
SPIC = bank(VLN, ('spic', 'stac', 'short'))
PIZZ = bank(VLN, ('pizz',))
TREM = bank(VLN, ('trem',))
CEL = bank(('cello', 'vc', 'celli'), ('sus', 'legato', 'arco', 'vib'), ('spic', 'pizz', 'trem'))
BASS = bank(('bass', 'contrabass', 'cb'), ('sus', 'arco', 'legato'), ('pizz', 'spic', 'trem', 'drum'))
DRUM = [w for w in wavs if any(k in w.lower() for k in ('timpani', 'bass drum', 'bassdrum', 'gran cassa'))]
json.dump({k: [min(v), max(v), len(v)] if v else [] for k, v in log.items()} | {'drum': len(DRUM), 'wav_tong': len(wavs)}, open(os.path.join(OUT, 'kho_mau.json'), 'w'), indent=1)
if not SUS: SUS = SPIC or PIZZ
if not CEL: CEL = SUS
_c = {}
def load(w):
    if w not in _c:
        x, sr = sf.read(w, always_2d=True); x = x.mean(1)
        if sr != SR: x = np.interp(np.arange(0, len(x), sr/SR), np.arange(len(x)), x)
        _c[w] = x / (np.abs(x).max() + 1e-9)
    return _c[w]
def note(B, m, dur, rng, rel=0.15):
    if not B: return np.zeros(int(SR*dur))
    k = min(B, key=lambda q: abs(q-m)); x = load(B[k][rng.integers(len(B[k]))])
    r = 2 ** ((m-k)/12)
    if abs(r-1) > 1e-3: x = np.interp(np.arange(0, len(x)-1, r), np.arange(len(x)), x)
    n = int(SR*dur)
    if len(x) < n: x = np.pad(x, (0, n-len(x)))
    x = x[:n].copy(); fr = min(int(SR*rel), n); x[-fr:] *= np.linspace(1, 0, fr)
    return x
def place(buf, x, t0, g):
    i = int(t0*SR); j = min(len(buf), i+len(x)); buf[i:j] += g*x[:j-i]
SC = {'min':[0,2,3,5,7,8,10],'harm':[0,2,3,5,7,8,11],'phryg':[0,1,3,5,7,8,10]}
PROG = [[0,5,3,4],[0,3,5,4],[0,5,6,4],[0,6,3,4],[0,4,5,3]]
MOT=[[0,2,4,2],[0,4,2,5],[4,2,0,-1],[0,1,2,4]]
def make(i,name,root,bpm,mode,style,prog,L=64):
    rng=np.random.default_rng(i); sc=SC[mode]; beat=60/bpm; bar=4*beat; buf=np.zeros(int(SR*(L+4))); nb=int(L/bar)
    mot=MOT[i%4]
    def deg(d,o=0): return root+sc[d%7]+12*(d//7)+o
    for b in range(nb):
        f=b/nb; t0=b*bar; d=prog[b%4]; r=deg(d)
        sec=0 if f<.18 else 1 if f<.45 else 2 if f<.58 else 3 if f<.9 else 4
        env=[.35,.55,.8,1.0,.4][sec]*(0.8+0.4*f if sec in(1,2) else 1)
        place(buf,note(CEL,r-12,bar*1.05,rng,.4),t0,.5*env)
        if BASS and sec>=1: place(buf,note(BASS,r-24,bar*1.05,rng,.4),t0,.35*env)
        if sec==0:
            place(buf,note(SUS,deg(d+4,12),bar*1.1,rng,.5),t0,.3)
            if b%2: 
                for k in range(4): place(buf,note(PIZZ or SPIC or SUS,deg(d+[0,2,4,2][k],12),.5,rng,.2),t0+k*beat,.3)
        elif sec==1:
            n=16 if (f>.3) else 8
            for k in range(n): place(buf,note(SPIC or SUS,deg(d+[0,4,7,4][k%4],12),bar/n*1.6,rng,.06),t0+k*bar/n,.3*env)
            for q,m in enumerate(mot): place(buf,note(SUS,deg(d+m,12),beat*1.1,rng,.2),t0+q*beat,.4*env)
            if DRUM and b%2==0: place(buf,load(DRUM[0])[:int(SR*1.2)],t0,.35*env)
        elif sec==2:
            place(buf,note(TREM or SUS,deg(d+4,12),bar*1.05,rng,.3),t0,.45*env)
            place(buf,note(SUS,deg(d+7,12),bar*1.05,rng,.3),t0,.3*env)
            if DRUM:
                m=2**int((f-.45)/.13*3+1)
                for k in range(int(m*2)): place(buf,load(DRUM[k%len(DRUM)])[:int(SR*.5)],t0+k*bar/(m*2),.3+.04*k/ m)
        elif sec==3:
            for k in range(16): place(buf,note(SPIC or SUS,deg(d+[0,4,7,4][k%4],12),beat/4*1.6,rng,.06),t0+k*beat/4,.3)
            for q,m in enumerate(mot): place(buf,note(SUS,deg(d+m+7,12),beat*1.3,rng,.15),t0+q*beat,.6)
            place(buf,note(SUS,deg(d+4,24),bar*1.1,rng,.3),t0,.3)
            if DRUM:
                for k in range(4): place(buf,load(DRUM[(k*3)%len(DRUM)])[:int(SR*1.2)],t0+k*beat,.55 if k%2==0 else .35)
        else:
            place(buf,note(SUS,deg(0,12),bar*1.2,rng,.5),t0,.5)
        if sec==3 and b==int(nb*.58): buf[int(t0*SR):int((t0+beat*.5)*SR)]*=.2
    for d_,g in ((0.029,0.3),(0.043,0.25),(0.067,0.2),(0.101,0.15),(0.151,0.1),(.23,.08)):
        k=int(d_*SR); buf[k:]+=g*buf[:-k]
    buf=buf[:int(SR*L)]; fo=int(SR*3); buf[-fo:]*=np.linspace(1,0,fo); buf/=np.abs(buf).max()*1.12
    st=np.stack([buf,np.roll(buf,200)],1); w=os.path.join(OUT,f'{i:02d}_{name}.wav'); sf.write(w,st,SR)
    subprocess.run(['ffmpeg','-v','error','-y','-i',w,'-b:a','192k',w[:-4]+'.mp3']); os.remove(w)
L=[('cao_trao_rao_riet',50,76,'min','x',0),('cao_trao_harmonic',52,84,'harm','x',2),('cao_trao_phrygian',47,72,'phryg','x',3),('cao_trao_bi_trang',45,66,'min','x',1),('cao_trao_nhanh',53,96,'min','x',0),('cao_trao_harmonic_nhanh',48,92,'harm','x',4),('cao_trao_tham',43,60,'min','x',1),('cao_trao_phrygian_nhanh',52,88,'phryg','x',2),('cao_trao_hung',50,80,'min','x',4),('cao_trao_ky_binh',46,100,'harm','x',3),('cao_trao_bi_an',57,70,'min','x',1),('cao_trao_dong_dao',55,104,'harm','x',0),('cao_trao_dan_dap',53,110,'min','x',3),('cao_trao_bao',50,90,'harm','x',2),('cao_trao_phrygian_cham',52,64,'phryg','x',4),('cao_trao_sau_lang',41,58,'min','x',1),('cao_trao_dinh_diem',47,86,'harm','x',2),('cao_trao_hoi_hop',52,94,'phryg','x',0),('cao_trao_tin_nong',48,98,'min','x',4),('cao_trao_thoi_su',45,82,'min','x',1)]
for i,a in enumerate(L,1): make(i,a[0],a[1]+12,a[2],a[3],a[4],PROG[a[5]])
fs = sorted(glob.glob(os.path.join(OUT, '[0-9]*.mp3')))
subprocess.run(['ffmpeg','-v','error','-y'] + sum([['-i', f] for f in fs], []) + ['-filter_complex', ''.join(f'[{k}:a]atrim=26:40,afade=t=out:st=13:d=1[a{k}];' for k in range(len(fs))) + ''.join(f'[a{k}]' for k in range(len(fs))) + f'concat=n={len(fs)}:v=0:a=1', '-b:a', '160k', os.path.join(OUT, '00_nghe_thu_20_mau.mp3')])
