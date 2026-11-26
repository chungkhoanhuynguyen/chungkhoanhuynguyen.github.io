# Soát giao diện điện thoại 390px cho MỌI trang .html: tràn ngang (phần tử lòi ra ngoài, không nằm trong khung cuộn), lỗi JS, chữ <12px, nút bấm <24px. Kết quả /tmp/scan_mob.json. Chạy: python3 _kiem/soat_dien_thoai.py
import glob, json, asyncio
from playwright.async_api import async_playwright
files=[f for f in glob.glob('/tmp/cw/**/*.html',recursive=True) if '/_' not in f.replace('/tmp/cw','') and '/.git/' not in f and '/node_modules/' not in f]
JS='''()=>{const W=document.documentElement.clientWidth;const sw=document.documentElement.scrollWidth;let bad=[];
if(sw>W+2){for(const e of document.querySelectorAll('body *')){const r=e.getBoundingClientRect();if(r.width>0&&r.right>W+2){let p=e.parentElement,inScroll=false;while(p){const s=getComputedStyle(p);if(/(auto|scroll|hidden)/.test(s.overflowX)){inScroll=true;break}p=p.parentElement}if(!inScroll){bad.push((e.tagName+'.'+(e.className||'')).toString().slice(0,50)+':'+Math.round(r.right));if(bad.length>3)break}}}}
const small=[...document.querySelectorAll('p,li,td,span,a')].filter(e=>e.offsetParent&&e.textContent.trim().length>20&&parseFloat(getComputedStyle(e).fontSize)<12).length;
const tap=[...document.querySelectorAll('a,button')].filter(e=>{const r=e.getBoundingClientRect();return e.offsetParent&&r.width>0&&r.height>0&&r.height<24&&r.width<24}).length;
return {sw,W,bad,small,tap}}'''
async def main():
    out=[]
    async with async_playwright() as p:
        b=await p.chromium.launch()
        ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=1,is_mobile=True,has_touch=True)
        await ctx.route('**/*',lambda r: r.abort() if r.request.url.startswith('http') else r.continue_())
        sem=asyncio.Semaphore(8)
        async def one(f):
            async with sem:
                pg=await ctx.new_page(); errs=[]
                pg.on('pageerror',lambda e: errs.append(str(e)[:80]))
                try:
                    await pg.goto('file://'+f,wait_until='domcontentloaded',timeout=15000); await pg.wait_for_timeout(600)
                    r=await pg.evaluate(JS); r['f']=f.replace('/tmp/cw/',''); r['err']=errs[:2]; out.append(r)
                except Exception as e: out.append({'f':f.replace('/tmp/cw/',''),'fail':str(e)[:60]})
                await pg.close()
        await asyncio.gather(*[one(f) for f in files])
    json.dump(out,open('/tmp/scan_mob.json','w'),ensure_ascii=False)
asyncio.run(main())
