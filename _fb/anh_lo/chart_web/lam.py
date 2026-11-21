import json,sys,subprocess
rows={}
for l in open('ohlc.txt'):
    s,d,o,h,lo,c,v=l.split(); rows.setdefault(s,[]).append(dict(time='2026-'+d,open=int(o)/1000,high=int(h)/1000,low=int(lo)/1000,close=int(c)/1000,volume=int(v)))
for s in rows: rows[s].sort(key=lambda x:x['time'])
cfg={"PNJ":dict(ten="CTCP Vàng bạc Đá quý Phú Nhuận",meme="Vàng chưa kịp đeo"),
     "FPT":dict(ten="CTCP FPT",meme="Ăn chắc mặc bền?")}
tpl=open('tpl.html',encoding='utf-8').read()
for s,c in cfg.items():
    b=rows[s]; ch=b[-1]['close']-b[-2]['close']
    d=dict(ma=s,ten=c['ten'],meme=c['meme'],bars=b,gia=b[-1]['close'],ch=ch,pct=ch/b[-2]['close']*100)
    open(s+'.html','w',encoding='utf-8').write(tpl.replace('/*DATA*/',json.dumps(d,ensure_ascii=False)))
