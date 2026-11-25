import asyncio, os, sys, json
from playwright.async_api import async_playwright

FPS = 30
OUT = os.environ.get('OUT','fr')
BASE = os.environ.get('BASE','http://localhost:8765/')
STRIDE = int(os.environ.get('STRIDE','1'))
CHROME = os.environ.get('CHROME','/usr/bin/google-chrome')
VT = r"""
(()=>{const rP=performance.now.bind(performance),rD=Date.now,rRAF=window.requestAnimationFrame.bind(window),rST=window.setTimeout.bind(window),rCT=window.clearTimeout.bind(window);
let V=false,vt=0,dOff=0,id=1e7;let q=[],raf=[];
performance.now=()=>V?vt:rP();Date.now=()=>V?dOff+vt:rD();
window.requestAnimationFrame=cb=>{if(V){raf.push(cb);return ++id}return rRAF(cb)};
window.setTimeout=(f,ms,...a)=>{if(V){const i=++id;q.push({t:vt+(+ms||0),f,a,i});return i}return rST(f,ms,...a)};
window.clearTimeout=i=>{if(V||i>1e7){q=q.filter(o=>o.i!==i)}rCT(i)};
window.__vtOn=()=>{vt=rP();dOff=rD()-vt;V=true};
window.__step=(n,dt)=>{for(let k=0;k<n;k++){vt+=dt;for(let g=0;g<50;g++){const due=q.filter(o=>o.t<=vt);if(!due.length)break;q=q.filter(o=>o.t>vt);due.sort((a,b)=>a.t-b.t).forEach(o=>{try{typeof o.f==='function'?o.f(...o.a):0}catch(e){console.log('T',e)}})}const c=raf;raf=[];c.forEach(f=>{try{f(vt)}catch(e){console.log('R',e)}})}};
localStorage.setItem('tkm_seen_guide','1');
})();
"""
OVL = r"""
(()=>{const st=document.createElement('style');st.textContent=`
@font-face{font-family:PF;src:url(pf/playfair-display-latin-900-normal.woff2)}@font-face{font-family:PF;src:url(pf/playfair-display-vietnamese-900-normal.woff2);unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}
@font-face{font-family:NS;src:url(pf/noto-serif-latin-900-normal.woff2)}@font-face{font-family:NS;src:url(pf/noto-serif-vietnamese-900-normal.woff2);unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB}
.lab .nm,.lab .tt,.lab .hp,.glab,#hbb,#cpbar,#inv,.ui,#chat,#wchat,#quest,#hint,#pkbar,#mm,#cpbar,#skills,#bars,#atkb,#tl,#menu,#fab,#joy,#srvan,#tutb,#tribb,#hud,#topbar,#npcp,#invw,.fab,#rank,#bagb{visibility:hidden!important}
#pv{position:fixed;inset:0;z-index:99999;pointer-events:none;font-family:PF,serif;color:#fff}
#pv .bar{position:absolute;left:0;right:0;height:0;background:#000}#pv .t{position:absolute;left:0;right:0;text-align:center;text-shadow:0 0 22px rgba(255,150,40,.9),0 3px 6px #000}
#pv .big{font-size:84px;letter-spacing:4px;background:linear-gradient(#fff6d0,#ffd36b 45%,#b8701c);-webkit-background-clip:text;color:transparent;filter:drop-shadow(0 0 14px rgba(255,140,30,.8)) drop-shadow(0 4px 3px #000)}
#pv .sub{font:900 30px NS,serif;letter-spacing:2px}
#pv .cap{font:900 52px NS,serif;letter-spacing:2px;color:#fff;text-shadow:0 0 18px #ff3a1a,0 0 4px #000,0 4px 6px #000}
#pv .cap2{font:900 30px NS,serif;color:#ffe08a;text-shadow:0 0 10px #000,0 2px 4px #000}
#pv .flash{position:absolute;inset:0;background:#fff;opacity:0}#pv .dk{position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,0,0,.35),rgba(0,0,0,.95));opacity:0}#pv .lab2{position:absolute;left:0;right:0;top:12%;text-align:center;font:900 22px NS,serif;letter-spacing:6px;color:#ffd36b;text-shadow:0 0 8px #000}`;document.head.appendChild(st);
const d=document.createElement('div');d.id='pv';d.innerHTML='<div class="dk"></div><div class="lab2" id="l2"></div><div class="flash"></div><div class="bar" id="b1" style="top:0"></div><div class="bar" id="b2" style="bottom:0"></div><div class="t" id="t1"></div><div class="t" id="t2"></div>';document.body.appendChild(d);
window.__ov=(o)=>{const t1=document.getElementById('t1'),t2=document.getElementById('t2');
 t1.className='t '+(o.c1||'cap');t2.className='t '+(o.c2||'cap2');t1.textContent=o.a||'';t2.textContent=o.b||'';
 t1.style.top=(o.y1||70)+'%';t2.style.top=(o.y2||82)+'%';
 const a=o.al==null?1:o.al;t1.style.opacity=a;t2.style.opacity=o.al2==null?a:o.al2;
 const sc=o.sc||1;t1.style.transform='scale('+sc+')';
 document.querySelector('#pv .flash').style.opacity=o.fl||0;document.querySelector('#pv .dk').style.opacity=o.dk||0;const l2=document.getElementById('l2');l2.textContent=o.lab||'';l2.style.opacity=o.lal==null?1:o.lal;
 document.getElementById('b1').style.height=document.getElementById('b2').style.height=(o.bars==null?60:o.bars)+'px'};
})();
"""

def ease(x): return max(0,min(1,x))

async def main():
    which = sys.argv[1:] or ['s0','s1','s2','s3','s4','s5','s6','s7','s8']
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME, args=['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
        pg = await (await b.new_context(viewport={'width':1280,'height':720})).new_page()
        pg.on('pageerror', lambda e: print('ERR', e))
        await pg.add_init_script(VT)
        await pg.goto(BASE+'index.html?noktx&noacct&noadapt&bfnow', wait_until='commit')
        await pg.wait_for_function("()=>document.getElementById('cgo')&&!document.getElementById('cgo').disabled", timeout=400000)
        await pg.evaluate("()=>{const c=document.getElementById('cn');c.value='Huyền Kiếm';c.dataset.ed='1';document.getElementById('cgo').click()}")
        await pg.wait_for_function("()=>window.__demo && window.__demo.hero", timeout=400000)
        await pg.wait_for_timeout(6000)
        await pg.evaluate(OVL)
        await pg.evaluate("""()=>{const D=__demo;D.TU.realm=2;D.TU.tang=10;
          D.TU.tong='kim';for(let i=0;i<14;i++)D.INV.bag.push(D.mkItem(5+(i%2)));D.wearBest();D.closeInv&&D.closeInv();
          D.hero.mp=99999;D.hero.max=D.hero.hp=999999;document.getElementById('npcp')&&(document.getElementById('npcp').style.display='none');
          document.getElementById('invw')&&(document.getElementById('invw').style.display='none');__vtOn();window.scrFlash=function(){}}""")
        await pg.evaluate("()=>{const st=document.createElement('style');st.textContent='#bfhud,#bfbtn,#hbb,#bfb{display:none!important}';document.head.appendChild(st)}")
        await pg.wait_for_timeout(1500)
        frame = [0]
        async def shoot(scene, n, per):
            os.makedirs(f'{OUT}/{scene}', exist_ok=True)
            for i in range(n):
                js = per(i, n)
                await pg.evaluate("js=>{try{(new Function(js))()}catch(e){console.log(e)};__step(1,1000/30)}", js)
                if i % STRIDE == 0:
                    for _try in range(4):
                        try:
                            await pg.screenshot(path=f'{OUT}/{scene}/{i:04d}.jpg', type='jpeg', quality=92, timeout=90000); break
                        except Exception as ex:
                            print('retry shot', i, ex, flush=True); await asyncio.sleep(3)
            print(scene, 'done', flush=True)
        async def ev(js):
            await pg.evaluate("js=>{(new Function(js))()}", js)

        def ov(**k): return '__ov(' + json.dumps(k, ensure_ascii=False) + ');'

        def hide_on(): return "document.querySelectorAll('#bfhud,#bfbtn,#hbb').forEach(e=>e.style.display='none');"
        # S0 (4s) intro tối
        if 's0' in which:
            await ev("const h=__demo.heroPos();h.set(-60,h.y,250);__step(20,33)")
            def s0(i,n):
                t=i/n
                if i<60: a=('Ngày Huyền Giới đại loạn…'); al=ease(i/15)*ease((58-i)/10)
                else: a=('…ai mạnh, kẻ đó sống.'); al=ease((i-62)/12)
                return f"__demo.setView({2.2+t*.5},{0.15+t*.1},{30-t*12});"+ov(a=a,c1='sub',y1=46,al=al,dk=0.82-0.2*t,bars=90,fl=0.9 if i>=n-4 else 0)
            await shoot('s0',120,s0)
        # S1 (4s) tên game
        if 's1' in which:
            await ev("const h=__demo.heroPos();h.set(40,h.y,262);__step(20,33)")
            def s1(i,n):
                t=i/n
                return f"__demo.setView({-0.6+t*1.2},{0.45-t*0.15},{60-t*28});"+ov(a='HUYỀN KIẾM TIÊN ĐỒ',b='Game tu tiên 3D · chơi ngay trên điện thoại',c1='big',c2='sub',y1=36,y2=56,al=ease((i-8)/18),al2=ease((i-40)/18),sc=1.15-.15*ease(i/30),bars=70)
            await shoot('s1',120,s1)
        # S2 (5s) tông môn
        if 's2' in which:
            await ev("const h=__demo.heroPos();h.set(0,h.y,-6);__step(10,33)")
            sects=['Thiên Kiếm Tông · Kim','Thanh Mộc Cốc · Mộc','Huyền Thủy Cung · Thủy','Xích Diễm Môn · Hỏa','Hậu Thổ Tông · Thổ','Huyết Ma Tông · Ma đạo']
            def s2(i,n):
                k=min(5,i//22)
                return f"__demo.setView({3.14+i*.01},0.38,{26-i*.04});"+ov(a='6 TÔNG MÔN · NGŨ HÀNH TƯƠNG KHẮC',b=sects[k],al=ease(i/10),al2=ease((i%22)/6),bars=60,lab='CHỌN ĐƯỜNG TU',lal=ease(i/10))
            await shoot('s2',150,s2)
        # S3 (8s) tuyệt học
        if 's3' in which:
            cuts=[('glong','GIÁNG LONG THẬP CHƯỞNG',2.0,'BÍ KÍP · CHƯỞNG PHÁP'),('ldvq','LÔI ĐÌNH VẠN QUÂN',3.0,'BÍ KÍP · LÔI HỆ'),('hlpt','HỎA LONG PHẦN THIÊN',4.4,'BÍ KÍP · HỎA HỆ'),('vkqt','VẠN KIẾM QUY TÔNG',5.6,'BÍ KÍP · KIẾM ĐẠO')]
            await ev("const D=__demo,h=D.heroPos();h.set(6,h.y,22);__step(10,33)")
            def s3(i,n):
                c=i//60; k=i%60; sid,name,yaw,lab=cuts[c]
                js=f"__demo.setView({1.45+k*0.004+0.1*(c%2)},{0.36+0.04*(c%2)},{14-k*0.03});"
                if k in (1,30): js+=f"__demo.hero.face={0 if k==1 else 1.2};__demo.hero.mp=99999;__demo.castCP('{sid}',true);"
                return js+ov(a=name,c1='cap',y1=74,al=ease((k-4)/6),sc=1.25-0.25*ease((k-4)/8),fl=max(0,1-k/5)*0.5,bars=60,lab=lab,lal=ease((k-4)/6))
            await shoot('s3',240,s3)
        # S4 (5s) cảnh giới + hào quang
        if 's4' in which:
            await ev("const D=__demo,h=D.heroPos();h.set(30,h.y,215);for(const sl of ['weapon','robe','pants','boots','belt','neck','ring','fabao'])D.INV.bag.push(D.mkItem(6,sl));D.wearBest();D.closeInv&&D.closeInv();__step(10,33)")
            rl=['Phàm Nhân','Luyện Khí','Trúc Cơ','Kết Đan','Nguyên Anh','Hóa Thần']
            def s4(i,n):
                k=min(5,i//25)
                return f"__demo.setView({3.14+0.9-i*.012},0.22,{9-i*.01});"+ov(a='CẢNH GIỚI TU VI',b=' → '.join(rl[:k+1]),al=ease(i/10),bars=60,lab='ĐỒ CÀNG XỊN · HÀO QUANG CÀNG RỰC',lal=ease((i-20)/10))
            await shoot('s4',150,s4)
        # S5 (8s) độ kiếp
        if 's5' in which:
            await ev("const D=__demo,h=D.heroPos();h.set(30,h.y,215);D.TU.tong='kim';D.TU.realm=1;D.TU.tang=10;D.TU.xp=D.needXp()*2;D.hero.max=D.hero.hp=1e7;__step(5,33);D.tribGo()")
            def s5(i,n):
                return f"__demo.setView({2.9+i*.002},{0.05+i*.0006},{26-i*.03});"+ov(a='ĐỘ KIẾP',b='Qua lôi kiếp phi thăng — xịt là tan xác, rơi sạch đồ',al=ease((i-20)/12),sc=1.2-0.2*ease((i-20)/12),bars=60)
            await shoot('s5',240,s5)
        # S6 (6s) PK rơi sạch đồ
        if 's6' in which:
            await ev("""const D=__demo,h=D.heroPos();h.set(60,h.y,200);D.TU.realm=2;__step(5,33);let e=D.allEnts().filter(b=>b.team==='bot'&&!b.dead).sort((a,b)=>a.c.g.position.distanceTo(h)-b.c.g.position.distanceTo(h))[0];if(e){e.c.g.position.set(h.x,h.y,h.z+5);e.target=null;e.st=null;e.hostile=0}window.__pkv=e;""")
            def s6(i,n):
                js=f"__demo.setView({3.14+0.7-i*0.004},0.3,{15-i*0.02});"
                if i==8: js+="__demo.hero.mp=99999;__demo.castCP('tnpt',true);"
                if i==50: js+="""const D=__demo,e=window.__pkv;if(e){const p=e.c.g.position.clone();e.hp=1;D.hit(D.hero,e,99999999,true);for(let q=0;q<12;q++){const a=q/12*6.28;D.dropItem(p.clone().add(new THREE.Vector3(Math.cos(a)*2.4,0,Math.sin(a)*2.4)),D.mkItem(2+q%5))}}"""
                al=ease((i-52)/8)
                return js+ov(a='PK DỨT KHOÁT',b='Hạ gục đối thủ — đối thủ RƠI SẠCH ĐỒ, kể cả đồ đang mặc',al=al,sc=1.3-0.3*al,fl=(0.8 if 50<=i<=52 else 0),bars=60)
            await shoot('s6',180,s6)
        # S7 (10s) chiến trường tiên ma: đông người, nổ skill liên tục
        if 's7' in which:
            await ev("""const D=__demo;D.TU.realm=2;D.TU.tong='kim';D.bfJoin('tien');const B=D.BF;B.sol.forEach(o=>{o.z=B.Z+(o.sd==='tien'?1:-1)*(2+Math.random()*16);o.x=B.X+(Math.random()-.5)*30;o.tg=null});const h=D.heroPos();h.set(B.X,B.Y,B.Z+8);D.hero.max=D.hero.hp=1e8;D.hero.mp=1e6;__step(10,33);"""+hide_on())
            ids=['glong','ldvq','hlpt','vkqt','bptg','hamc','htdc','tnpt','lmtk','chtv','htdp','cabc']
            def s7(i,n):
                js=hide_on()+"const D=__demo,B=D.BF;D.hero.hp=D.hero.max;D.hero.mp=1e6;"
                js+=f"D.setView({3.14+0.5-i*.004},{0.7-i*.0008},{28-i*.04});"
                if i%9==0:
                    sid=ids[(i//9)%len(ids)]
                    js+=f"{{const al=B.sol.filter(o=>!o.dead);const o=al[Math.floor(Math.random()*al.length)];if(o)D.castAt('{sid}',o.x,o.z)}}"
                if i%25==5:
                    js+=f"D.hero.face=Math.PI;D.castCP('{ids[(i//25)%len(ids)]}',false);"
                return js+ov(a='CHIẾN TRƯỜNG TIÊN MA',b='20:00 mỗi tối · hàng trăm tu sĩ · bản đồ 3 đường · phá Linh Tinh địch',al=ease((i-6)/12),bars=60,lab='TIÊN ☯ MA',lal=ease((i-6)/12))
            await shoot('s7',300,s7)
        # S8 (4s) kết
        if 's8' in which:
            await ev("const h=__demo.heroPos();h.set(40,h.y,262);__step(5,33)")
            def s8(i,n):
                return f"__demo.setView({1.2+i*.004},0.5,70);"+ov(a='HUYỀN KIẾM TIÊN ĐỒ',b='Chơi miễn phí: chungkhoanhuynguyen.com/thienkiemmon',c1='big',c2='sub',y1=34,y2=56,al=ease(i/15),bars=90,lab='TOP 10 PHONG THẦN BẢNG · DANH HIỆU RIÊNG',lal=ease((i-15)/15))
            await shoot('s8',120,s8)
        await b.close()

asyncio.run(main())
