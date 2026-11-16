# Ghép các phần trong _src/lanhchua thành loanthelanhchua/index.html
import glob,os
d=os.path.dirname(os.path.abspath(__file__))
out=''.join(open(f,encoding='utf8').read() for f in sorted(glob.glob(os.path.join(d,'[0-9][0-9]_*'))))
dst=os.path.join(d,'..','..','loanthelanhchua','index.html')
open(dst,'w',encoding='utf8').write(out[:-1])
print('built',len(out)//1024,'KB ->',os.path.normpath(dst))
