import json,os,sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
from lay_gia import lay
rows={}
for l in open('ohlc.txt'):
    s,d,o,h,lo,c,v=l.split(); rows.setdefault(s,[]).append(dict(time='2026-'+d,open=int(o)/1000,high=int(h)/1000,low=int(lo)/1000,close=int(c)/1000,volume=int(v)))
for s in rows: rows[s].sort(key=lambda x:x['time'])
# QL1 21/11: mặc định lấy giá từ DỮ LIỆU WEB (0 token); ohlc.txt chỉ dùng khi muốn ghi đè
class _R(dict):
    def __missing__(self,k):
        v=[dict(x,volume=x['volume']*100) for x in lay(k,125)]; self[k]=v; return v
rows=_R(rows)
cfg=json.load(open('cfg.json',encoding='utf-8'))
tpl=open('tpl.html',encoding='utf-8').read()
for s,c in cfg.items():
    b=rows[s.rstrip('2')]; ch=round(b[-1]['close']-b[-2]['close'],2)
    d=dict(ma=s.rstrip('2'),bars=b,gia=b[-1]['close'],ch=ch,pct=ch/b[-2]['close']*100,**c)
    open(s+'.html','w',encoding='utf-8').write(tpl.replace('/*DATA*/',json.dumps(d,ensure_ascii=False)))
