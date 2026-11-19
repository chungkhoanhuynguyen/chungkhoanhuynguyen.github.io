# -*- coding: utf-8 -*-
# wsp_qc.py OUTDIR KEY – bước QC bắt buộc trên GitHub Actions (QL1 19/11: "whisper thành bước bắt buộc QC Actions trước 22/11").
# Nghe lại KEY.mp4 bằng faster-whisper (small, int8, CPU, miễn phí) → OUTDIR/KEY_wsp.txt; so mọi CON SỐ trong KEY.srt với lời whisper nghe được.
# Số có trên phụ đề mà whisper không nghe ra (vd 109,8 → 119,8; 341.000 → 350.000; "ngày chín" → 1979) → ghi "CẢNH BÁO whisper" vào KEY_qc.txt
# để người soát nghe lại đoạn đó (whisper hay nghe sai tên riêng – chỉ xét số). Bằng chứng giá trị: PPC v1.9–v2.3 (5 lần bắt được số nghe lệch).
import os, re, sys, subprocess
import numpy as np

def so(t):
    t = t.replace('\u00a0', ' ')
    out = set()
    # quy về đơn vị: "18 triệu 850 nghìn" = 18.850.000; "990 nghìn" = 990.000; "6 triệu" = 6.000.000 (whisper hay viết 990.000, srt viết 990 nghìn)
    for m in re.finditer(r'(\d+(?:,\d+)?)\s*(tỷ|triệu|nghìn)(?:\s+(\d+)\s*(nghìn|triệu))?', t):
        hs = {'tỷ': 1e9, 'triệu': 1e6, 'nghìn': 1e3}
        v = float(m.group(1).replace(',', '.')) * hs[m.group(2)]
        if m.group(3): v += float(m.group(3)) * hs[m.group(4)]
        out.add(round(v))
    for m in re.finditer(r'(\d+)\s*triệu\s+(\d{1,3})\.000\b', t):     # whisper: "8 triệu 700.000"
        out.add(int(m.group(1)) * 1000000 + int(m.group(2)) * 1000)
    for m in re.finditer(r'\d[\d.,]*\d|\d', t):
        x = m.group(0).rstrip('.,')
        x = re.sub(r'\.(?=\d{3}\b)', '', x)          # 33.800 -> 33800
        x = x.replace(',', '.')                       # 15,5 -> 15.5
        try:
            v = float(x)
        except ValueError:
            continue
        out.add(v)
    return out

def srt_dong(p):
    dong = []
    for blk in open(p, encoding='utf-8').read().strip().split('\n\n'):
        ls = blk.strip().split('\n')
        if len(ls) >= 3 and '-->' in ls[1]:
            dong.append((ls[1].split(' --> ')[0][:8], ' '.join(ls[2:])))
    return dong

def nghe(mp4, out):
    from faster_whisper import WhisperModel
    a = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', mp4, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'],
                                     capture_output=True).stdout, np.int16).astype(np.float32) / 32768
    m = WhisperModel('small', device='cpu', compute_type='int8')
    seg, _ = m.transcribe(a, language='vi', beam_size=1)
    txt = []
    with open(out, 'w', encoding='utf-8') as o:
        for x in seg:
            o.write('%.1f %s\n' % (x.start, x.text.strip())); txt.append(x.text)
    return ' '.join(txt)

if __name__ == '__main__':
    d, k = sys.argv[1], sys.argv[2]
    mp4, srt = os.path.join(d, k + '.mp4'), os.path.join(d, k + '.srt')
    if not (os.path.exists(mp4) and os.path.exists(srt)):
        print('thieu mp4/srt', k); sys.exit(0)
    wf = os.path.join(d, k + '_wsp.txt')
    if os.environ.get('REUSE') and os.path.exists(wf):
        nghe_duoc = so(' '.join(l.split(' ', 1)[1] for l in open(wf, encoding='utf-8') if ' ' in l))
    else:
        nghe_duoc = so(nghe(mp4, wf))
    lech = []
    for t, line in srt_dong(srt):
        so_dong = so(line)
        lon = {x for x in so_dong if x >= 1000 and x == int(x)}
        for v in sorted(so_dong):
            if v in nghe_duoc or (v < 10 and float(v).is_integer()):   # bỏ số nhỏ 0–9 (hay bị viết bằng chữ)
                continue
            if v < 1000 and any(x in nghe_duoc for x in lon):            # 990 trong "990 nghìn" đã khớp dạng 990.000
                continue
            if v >= 1000 and v not in lon:
                pass
            lech.append('%s %s | %s' % (t, ('{:,.0f}'.format(v).replace(',', '.') if v >= 1000 else ('%g' % v).replace('.', ',')), line[:90]))
    with open(os.path.join(d, k + '_qc.txt'), 'a', encoding='utf-8') as q:
        if lech:
            q.write('\nCẢNH BÁO whisper: %d số trên phụ đề không nghe ra – nghe lại từng đoạn:\n' % len(lech))
            for x in lech[:40]: q.write('  ' + x + '\n')
        else:
            q.write('\nWHISPER: khớp mọi con số trên phụ đề.\n')
    print('whisper lech', len(lech))
