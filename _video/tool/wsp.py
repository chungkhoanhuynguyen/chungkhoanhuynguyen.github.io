# wsp.py VIDEO OUT.txt – nghe lại giọng bằng faster-whisper (small, CPU int8, miễn phí) để đối chiếu số/xưng hô với .srt (NV1 17/11).
# Cài: pip install faster-whisper --break-system-packages. Đưa mảng numpy vào (bản av trong máy lỗi 'metadata_errors' khi đưa đường dẫn).
# Đã dùng: CH1811TL V5 (xác nhận "nhà mình"), CH2211VANG V1 (khớp mọi con số), giọng LTC6 "Bài năm". 7 phút audio ≈ 6–8 phút máy.
import sys, subprocess, numpy as np
from faster_whisper import WhisperModel
f, out = sys.argv[1], sys.argv[2]
a = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', f, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout, np.int16).astype(np.float32) / 32768
m = WhisperModel('small', device='cpu', compute_type='int8')
s, _ = m.transcribe(a, language='vi', beam_size=1)
with open(out, 'w') as o:
    for x in s: o.write('%.1f %s\n' % (x.start, x.text.strip())); o.flush()
