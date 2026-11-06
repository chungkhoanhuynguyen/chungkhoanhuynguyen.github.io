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
def make(i, name, root, bpm, mode, style, prog, L=32):
    rng = np.random.default_rng(i); sc = SC[mode]; beat = 60/bpm; bar = 4*beat; buf = np.zeros(int(SR*(L+3))); nb = int(L/bar)
    for b in range(nb):
        deg = prog[b % 4]; t0 = b*bar; r = root + sc[deg % 7]; third = root + sc[(deg+2) % 7]; fifth = root + sc[(deg+4) % 7]
        place(buf, note(CEL, r-12, bar*1.05, rng, 0.4), t0, 0.5)
        if BASS: place(buf, note(BASS, r-24, bar*1.05, rng, 0.4), t0, 0.35)
        for m in (third, fifth): place(buf, note(SUS, m, bar*1.05, rng, 0.4), t0, 0.22)
        if style == 'ostinato':
            for k in range(16): place(buf, note(SPIC or SUS, r+12+[0,7,12,7][k % 4], beat/4*1.6, rng, 0.06), t0+k*beat/4, 0.32)
        elif style == 'tremolo':
            place(buf, note(TREM or SUS, r+12, bar*1.05, rng, 0.3), t0, 0.45)
        elif style == 'march':
            for k in range(8): place(buf, note(SPIC or SUS, r+(12 if k % 2 else 0), beat/2*1.4, rng, 0.06), t0+k*beat/2, 0.35)
        elif style == 'pizz':
            for k in range(8): place(buf, note(PIZZ or SPIC or SUS, r+12+int(rng.choice([0,3,7,12])), 0.6, rng, 0.2), t0+k*beat/2, 0.4)
        if (style != 'lament' and b >= 1) or style == 'lament':
            ns = rng.choice([0,2,4,5,7], size=2 if bpm > 110 else 4); d = bar/len(ns)
            for q, n in enumerate(ns):
                m = root+12+sc[(deg+int(n)) % 7]+(12 if b >= nb//2 else 0)
                place(buf, note(SUS, m, d*1.15, rng, 0.25), t0+q*d, 0.45)
        if DRUM and (style in ('march', 'epic')) and b % (1 if style == 'march' else 2) == 0:
            x = load(DRUM[0]); place(buf, x[:int(SR*1.5)], t0, 0.6)
    buf *= np.linspace(0.8, 1.1, len(buf))
    for d, g in ((0.029,0.3),(0.043,0.25),(0.067,0.2),(0.101,0.15),(0.151,0.1)):
        k = int(d*SR); buf[k:] += g*buf[:-k]
    buf = buf[:int(SR*L)]; fo = int(SR*1.5); buf[-fo:] *= np.linspace(1, 0, fo); buf /= np.abs(buf).max()*1.12
    st = np.stack([buf, np.roll(buf, 200)], 1); w = os.path.join(OUT, f'{i:02d}_{name}.wav'); sf.write(w, st, SR)
    subprocess.run(['ffmpeg','-v','error','-y','-i',w,'-b:a','192k',w[:-4]+'.mp3']); os.remove(w)
L = [('ostinato_rao_riet',50,140,'min','ostinato',0),('ostinato_harmonic',52,150,'harm','ostinato',2),('tremolo_cang_thang',45,90,'min','tremolo',1),('tremolo_phrygian',47,84,'phryg','tremolo',3),('hanh_quan_violin',50,112,'min','march',0),('hanh_quan_trong',48,100,'harm','march',4),('bi_trang_lament',45,66,'min','lament',1),('bi_trang_harmonic',43,60,'harm','lament',2),('hung_trang_epic',50,96,'min','epic',0),('epic_phrygian',52,92,'phryg','epic',3),('pizzicato_bi_an',57,108,'min','pizz',1),('pizzicato_trinh_tham',55,120,'harm','pizz',4),('ostinato_cuc_nhanh',53,168,'min','ostinato',3),('tremolo_bao_to',50,100,'harm','tremolo',0),('hanh_quan_phrygian',52,120,'phryg','march',1),('lament_sau_lang',41,56,'min','lament',4),('epic_cao_trao',47,104,'harm','epic',2),('pizz_hoi_hop',52,132,'phryg','pizz',0),('ostinato_tin_nong',48,128,'min','ostinato',4),('epic_thoi_su',45,88,'min','epic',1)]
for i, a in enumerate(L, 1): make(i, a[0], a[1]+12, a[2], a[3], a[4], PROG[a[5]])
fs = sorted(glob.glob(os.path.join(OUT, '[0-9]*.mp3')))
subprocess.run(['ffmpeg','-v','error','-y'] + sum([['-i', f] for f in fs], []) + ['-filter_complex', ''.join(f'[{k}:a]atrim=0:9,afade=t=out:st=8:d=1[a{k}];' for k in range(len(fs))) + ''.join(f'[a{k}]' for k in range(len(fs))) + f'concat=n={len(fs)}:v=0:a=1', '-b:a', '160k', os.path.join(OUT, '00_nghe_thu_20_mau.mp3')])
