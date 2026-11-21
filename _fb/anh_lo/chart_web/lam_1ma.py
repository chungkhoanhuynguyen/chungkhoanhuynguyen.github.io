import json,os,sys
sys.path.insert(0,'_fb/anh_lo')
from lay_gia import lay
rows={}
for l in open('/dev/null'):
    s,d,o,h,lo,c,v=l.split(); rows.setdefault(s,[]).append(dict(time='2026-'+d,open=int(o)/1000,high=int(h)/1000,low=int(lo)/1000,close=int(c)/1000,volume=int(v)))
for s in rows: rows[s].sort(key=lambda x:x['time'])
# QL1 21/11: mặc định lấy giá từ DỮ LIỆU WEB (0 token); ohlc.txt chỉ dùng khi muốn ghi đè
class _R(dict):
    def __missing__(self,k):
        v=[dict(x,volume=x['volume']*100) for x in lay(k,125)]; self[k]=v; return v
rows=_R(rows)
cfg=json.load(open('_fb/anh_lo/chart_web/cfg_vic.json',encoding='utf-8'))
tpl=open('_fb/anh_lo/chart_web/tpl.html',encoding='utf-8').read()
for s,c in cfg.items():
    b=rows[s.rstrip('2')]; ch=round(b[-1]['close']-b[-2]['close'],2)
    d=dict(ma=s.rstrip('2'),bars=b,gia=b[-1]['close'],ch=ch,pct=ch/b[-2]['close']*100,**c)
    open('_fb/anh_lo/chart_web/'+s+'.html','w',encoding='utf-8').write(tpl.replace('/*DATA*/',json.dumps(d,ensure_ascii=False)))
