function hud(){if(!G)return;const pl=P0(),sm=SMALL(),net=income()-wages(),F=sm?fk:fmt;$('#cDay').textContent=(sm?'📅':'📅 Ngày ')+G.day;
 $('#cGold').innerHTML=`💰${sm?'':' '}${F(G.gold)} <small style="color:${net>=0?'#9f9':'#f88'}">${net>=0?'+':''}${F(net)}${sm?'':'/ngày'}</small>`+(G.lsOn?` · 💎${sm?fk(G.ls)+'h':' '+fmtLS(G.ls)}`:'');
 if(G.lsOn){$('#cArmy').innerHTML=sm?`☯ ${F(tot(pl.t))}/${F(rank(pl)[1])}`:`☯ ${cgN()} · tu vi <b>${fmt(tot(pl.t))}</b>/${fmt(rank(pl)[1])}`;$('#cArmy').title=`${cgN()} · Bộ ${fmt(pl.t.inf)} · Cung ${fmt(pl.t.arc)} · Kỵ ${fmt(pl.t.cav)}`}else $('#cArmy').innerHTML=sm?`⚔ ${F(tot(pl.t))}/${F(rank(pl)[1])}`:tt(pl.t)+` <small>/ ${fmt(rank(pl)[1])}</small>`;
 const r=rank(pl);$('#cRank').innerHTML=sm?`${r[2]} ${fiefs(pl)}🏰 ⭐${fk(pl.ren||0)}`:`${badge(pl)} ${fiefs(pl)} thành · ⭐${fmt(pl.ren||0)}`;const bf=$('#bFac');if(bf)bf.textContent=sm?'📜':'📜 Thế cục'}

/* ================= ĐIỀU KHIỂN ================= */
const PT=new Map();let pinch=null;
const cam=()=>mode=='battle'?BC:MC;
function setZoom(z,sx=W/2,sy=H/2){const c=cam(),lo=mode=='battle'?B.zf*.8:Math.max(W/CWB().w,H/CWB().h),hi=mode=='battle'?3:1.6;const wx=c.x+(sx-W/2)/c.z,wy=c.y+(sy-H/2)/c.z;c.z=cl(z,lo,hi);c.x=wx-(sx-W/2)/c.z;c.y=wy-(sy-H/2)/c.z;if(mode!='battle')c.follow=0}
C.addEventListener('pointerdown',e=>{try{C.setPointerCapture(e.pointerId)}catch(_){}PT.set(e.pointerId,{x:e.clientX,y:e.clientY,sx:e.clientX,sy:e.clientY,mv:0});
 if(PT.size==2){const [a,b]=[...PT.values()];pinch={d:Math.hypot(a.x-b.x,a.y-b.y)||1,z:cam().z};a.mv=b.mv=1}});
C.addEventListener('pointermove',e=>{const p=PT.get(e.pointerId);if(!p||paused&&mode!='battle')return;const dx=e.clientX-p.x,dy=e.clientY-p.y;p.x=e.clientX;p.y=e.clientY;
 if(PT.size==2&&pinch){const [a,b]=[...PT.values()];setZoom(pinch.z*Math.hypot(a.x-b.x,a.y-b.y)/pinch.d,(a.x+b.x)/2,(a.y+b.y)/2);return}
 if(Math.hypot(p.x-p.sx,p.y-p.sy)>9)p.mv=1;if(p.mv){const c=cam();c.x-=dx/c.z;c.y-=dy/c.z;if(mode=='map')c.follow=0}});
const pu=e=>{const p=PT.get(e.pointerId);PT.delete(e.pointerId);if(PT.size<2)pinch=null;if(p&&!p.mv&&!PT.size&&e.type=='pointerup')tap(p.x,p.y)};
C.addEventListener('pointerup',pu);C.addEventListener('pointercancel',pu);
C.addEventListener('wheel',e=>{e.preventDefault();setZoom(cam().z*(e.deltaY<0?1.15:.87),e.clientX,e.clientY)},{passive:false});
function tap(sx,sy){if(mode!='map'||paused||!G)return;const pl=P0(),m=mmRect();MC.follow=1;
 if(sx>=m.x&&sy>=m.y&&sx<=m.x+m.w&&sy<=m.y+m.h){const wb=CWB(),mx=wb.x0+(sx-m.x)/m.w*wb.w,my=wb.y0+(sy-m.y)/m.h*wb.h;if(!OPEN(contOf(mx,my))){toast('🔒 '+LOCKT(contOf(mx,my)),'#d9c2ff');return}pl.goS=pl.goP=null;pl.tx=mx;pl.ty=my;G.mk={x:pl.tx,y:pl.ty,t:2};return}
 const z=MC.z,q={x:MC.x+(sx-W/2)/z,y:MC.y+(sy-H/2)/z},rs=Math.max(1,.45/z);{const n=dhN();if(n&&z>=.42&&Math.abs(q.x-pl.x)<95&&q.y<pl.y-60&&q.y>pl.y-72-n*15-14){dhTog();return}}pl.goF=null;if(G.ac){G.ac=0;acBtn();toast('🤖 Đã tắt tự chinh phạt — bạn tự điều khiển','#fc8')}
 if(WRLD(q.y)!=WRLD(pl.y)){toast('🌀 Muốn sang thế giới khác phải đi qua Thông đạo','#9ff0ff');return}
 if(!OPEN(contOf(q.x,q.y))){toast('🔒 '+LOCKT(contOf(q.x,q.y)),'#d9c2ff');return}
 const fg=G.fights.find(f=>Math.hypot(f.x-q.x,f.y-q.y)<45*rs);if(fg){pl.goS=pl.goP=null;pl.goF=fg;if(dist(pl,fg)<40)joinFight(fg);return}
 pl.goV=null;const vg=V.find(v=>Math.hypot(v.x-q.x,v.y-q.y)<30*rs&&!S.some(s=>Math.hypot(s.x-q.x,s.y-12-q.y)<30*rs));if(vg){pl.goS=pl.goP=null;pl.goV=vg;if(dist(pl,vg)<24)villageMenu(vg);return}
 const s=S.find(s=>Math.hypot(s.x-q.x,s.y-12-q.y)<40*rs);if(s){pl.goS=s;pl.goP=null;if(dist(pl,s)<24)townMenu(s);return}
 const p=G.L.find(p=>!p.dead&&p.kind!='pl'&&Math.hypot(p.x-q.x,p.y-10-q.y)<24*rs);if(p){if(p.kind=='exile'){exileMenu(p);return}if(p.kind=='king'||(p.fac>=0&&p.fac!=pl.fac&&!atWar(pl.fac,p.fac))){partyMenu(p);return}if(false){stopPl();menu(`${badge(p)} ${pname(p)}`,`<p>Phe <b style="color:${facC(p.fac)}">${facN(p.fac)}</b> · ${RACE[raceOf(p)].n} · ${fmt(tot(p.t))} quân</p><p>🕊 Đang hòa bình với phe này.</p>`,[...(isMyKing()?[[`⚔ Tuyên chiến với ${facN(p.fac)}`,()=>{dWar(p.fac);close()}]]:[]),['🚶 Đi theo',()=>{close();pl.goP=p}],['Đóng',close]]);return}pl.goP=p;pl.goS=null;return}
 pl.goS=pl.goP=null;pl.tx=cl(q.x,10,WW-10);pl.ty=cl(q.y,10,WH-10);G.mk={x:pl.tx,y:pl.ty,t:1.5}}
$('#zMap').onclick=()=>{if(!G)return;G.mm=G.mm=='fac'?'rel':'fac';terr();toast(G.mm=='fac'?'🗺 Bản đồ: màu theo từng phe':'🗺 Bản đồ: 🟩 phe ta · 🟥 kẻ thù · ⬜ hòa bình','#ffd77a')};
const QN=['🎨 ĐẸP','⚙ NHẸ','⚡ SIÊU MƯỢT'];function qBtn(){const e=$('#zQ');if(e)e.textContent=['🎨','⚙','⚡'][QL]}
function setQ(n){QL=n;DSR=1;LOWQ=QL>=1;ULQ=QL==2;try{localStorage.setItem('ltlc-q',''+QL)}catch(e){}rs();BKC.clear();qBtn()}
$('#zQ').onclick=()=>{setQ((QL+1)%3);toast(['🎨 Đồ họa ĐẸP: nhiều chi tiết, tốn máy hơn','⚙ Đồ họa NHẸ: mượt hơn, ít chi tiết','⚡ SIÊU MƯỢT: hình mờ hơn, đoàn quân thành chấm, ít lính trong trận — hợp máy yếu'][QL],'#9cf')};qBtn();
$('#zFs').onclick=()=>{try{const d=document.documentElement;if(!document.fullscreenElement){(d.requestFullscreen||d.webkitRequestFullscreen).call(d).then(()=>{try{screen.orientation.lock('landscape')}catch(e){}}).catch(()=>{})}else document.exitFullscreen()}catch(e){}};
$('#zKg').onclick=()=>{if(paused)return;const k=myKing();if(!k){toast(isMyKing()?'Bạn là Vua — xem tướng ở 📜 Thế cục → Tướng':'Vua của bạn hiện không còn','#ccc');return}menu(`👑 ${pname(k)}`,`<p>${badge(k)} · ${fmt(tot(k.t))} quân · cách bạn ${Math.round(dist(k,P0())/100)} dặm</p><p>${k.inF?'⚔ Đang giao chiến!':k.goS?(k.goS.fac==k.fac?'🏰 Đang về '+k.goS.name:'⚔ Đang đi vây '+k.goS.name):'🚶 Đang tuần tra'}</p><p style="font-size:12px;color:#cdb">Đi theo Vua: khi Vua giao chiến hay vây thành, bạn ở gần sẽ cùng nhập trận và chia chiến công.</p>`,[['💬 Trò chuyện với Vua',()=>chat(k)],['🚶 Đi theo Vua',followKing],['📍 Xem Vua trên bản đồ',()=>goSee(k.x,k.y,.7)],['Đóng',close]])};
$('#zTp').onclick=()=>{if(!paused&&G)tpMenu()};
$('#zTs').onclick=()=>{if(!G)return;G.ts=({1:2,2:4,4:1})[G.ts||2];tsBtn();toast(`⏩ Tốc độ thời gian ×${G.ts}`,'#9cf')};
function tsBtn(){const cg=$('#zCg');if(cg)cg.style.display=G&&G.lsOn&&mode!='title'?'':'none';const l=$('#zTl');if(l)l.style.display=G&&G.lk&&mode!='title'?'':'none';const e=$('#zTs');if(!e)return;const on=G&&G.xian&&mode!='title';e.style.display=on?'':'none';if(on)e.textContent='⏩'+(G.ts||2)}
$('#cGold').onclick=$('#cArmy').onclick=()=>{if(!paused&&G&&G.lsOn)cgMenu()};$('#zCg').onclick=()=>{if(!paused&&G)cgMenu()};
$('#cRank').onclick=()=>{if(!paused&&G)dhMenu()};
$('#zMore').onclick=()=>{document.body.classList.toggle('more')};
$('#zSv').onclick=()=>{if(!paused&&G)slMenu()};
$('#zTl').onclick=()=>{if(!paused&&G)thienLo()};
$('#zAc').onclick=()=>{if(!paused&&G)acToggle()};
$('#zCo').onclick=()=>{showArrows(6);toast('🧭 Mũi tên chỉ hướng các nước gần nhất (6 giây)','#ffd77a')};
$('#zMu').onclick=()=>{muted=!muted;$('#zMu').textContent=muted?'🔇':'🔊'};
$('#zIn').onclick=()=>setZoom(cam().z*1.4);$('#zOut').onclick=()=>setZoom(cam().z/1.4);
$('#zMe').onclick=()=>{if(mode=='battle'&&B){BC.z=B.zf;BC.x=B.FW/2;BC.y=B.FH/2}else{MC.follow=1;MC.z=Math.max(MC.z,.7)}};
function titleMenu(){mode='title';G=null;B=null;$('#top').style.display='none';$('#zb').style.display='none';rlog();MC.z=Math.max(W/WW,H/WH)*1.05;MC.x=WW/2;MC.y=WH/2;MC.follow=0;
 S.forEach(s=>s.fac=s.f0);G={F:F0};terrNow();G=null;
 let has=0;try{has=!!localStorage.getItem(KEY)&&(!WMAP||localStorage.getItem('ltlc-map')=='2')}catch(e){}
 const btn=[];if(has)btn.push([WMAP?'▶ Chơi tiếp ván đã lưu':'▶ Chơi tiếp ván đã lưu (bản đồ cũ)',()=>{if(load()){close();startMap()}}]);
 btn.push(['💾 Mục lưu (5 ô) · 📤 Xuất / 📥 Nhập save',()=>slMenu()]);
 if(!WMAP){btn.push([`Đồ họa: <b>${QN[QL]}</b> — bấm để đổi`,()=>{setQ((QL+1)%3);close();titleMenu()}],['🌍 VÁN MỚI — Nhân tộc là bản đồ Trái Đất (201 quốc gia)<br><small>Ván cũ vẫn giữ tới khi ván mới được lưu</small>',()=>{try{sessionStorage.setItem('ltlc-newmap','1')}catch(e){}location.reload()}]);
  menu('⚔ Loạn Thế Lãnh Chúa','<p>Bản cập nhật mới: <b>lục địa Nhân tộc giờ là bản đồ Trái Đất thật</b> với 201 quốc gia và hơn 340 thành trì.</p><p>Ván đang chơi của bạn vẫn dùng bản đồ cũ.</p>',btn);return}
 btn.push([`Đồ họa: <b>${QN[QL]}</b> — bấm để đổi (máy giật chọn ⚡)`,()=>{setQ((QL+1)%3);close();titleMenu()}]);
 RACE.slice(0,4).forEach((r,c)=>btn.push([c==0&&WMAP?`${RIC[c]} ${r.n} — <b>bản đồ Trái Đất</b>: 201 quốc gia, ${S.filter(s=>!s.race).length} thành<br><small style="color:#9f9">★ Khuyên dùng cho người mới</small>`:`${RIC[c]} ${r.n} — châu lục ${['phía Tây Bắc','phía Đông Bắc','phía Tây Nam','phía Đông Nam','tận cùng phía Đông'][c]}`,()=>pickKing(c)]));
 menu('⚔ Loạn Thế Lãnh Chúa',`<p>Bạn khởi đầu là Hiệp sĩ ở châu lục quê nhà. Chinh phục để mở dần thế giới: <b>4 châu lục</b> → <b>Vùng Đất Chết</b> → <b>Thời đại Thần linh</b> (4 lục địa thần) → chiếm 2/4 lục địa Thần linh để mở <b>🌀 Cửu Thiên Huyền Giới</b> (thế giới tu tiên, cực mạnh) qua Cổng truyền tống.</p><p style="color:#ffd77a">Chọn tộc người:</p>`,btn)}
function pickKing(c,reg){if(c==0&&WMAP&&reg==null){menu('🌍 Nhân tộc — Trái Đất · chọn châu lục',`<p>${F0.filter(f=>!f.race).length} quốc gia, ${S.filter(s=>!s.race).length} thành trì theo bản đồ thế giới thật. Chọn châu lục rồi chọn nước để phụng sự.</p>`,[...WREG.map((n,r)=>[`${['🌏','🏰','🌍','🗽','🌎','🏝'][r]} ${n} — ${F0.filter(f=>f.wm===r).length} nước`,()=>{close();pickKing(0,r)}]),['◀ Quay lại',()=>{close();titleMenu()}]]);return}
 if(c==0&&WMAP){const L=F0.map((f,i)=>[f,i]).filter(([f])=>f.wm===reg).map(([f,i])=>[f,i,S.filter(s=>s.f0==i).length]).sort((a,b)=>b[2]-a[2]||a[0].n.localeCompare(b[0].n,'vi'));
  menu(`🌍 ${WREG[reg]} — chọn nước để phụng sự`,'<p>Nước lớn nhiều thành dễ chơi hơn.</p>',[...L.map(([f,i,n])=>[`<span style="color:${f.c}">■</span> ${f.n} — ${n} thành`,()=>{close();newGame(i);startMap();save()}]),['◀ Quay lại',()=>{close();pickKing(0)}]]);return}
 const btn=F0.map((f,i)=>[f,i]).filter(([f])=>f.race==c).map(([f,i])=>[`<span style="color:${f.c}">■</span> ${CC[f.cn].n} — phụng sự ${f.n}`,()=>{close();newGame(i);startMap();save()}]);
 btn.push(['◀ Quay lại',()=>{close();titleMenu()}]);menu(`${RIC[c]} ${RACE[c].n} — chọn vua để phụng sự`,`<p>${['Cân bằng mọi mặt.','Máu trâu, đánh mạnh nhưng chậm, tầm bắn ngắn.','Cung thủ bắn rất xa, nhanh nhẹn nhưng mỏng máu.','Cực nhanh và hung hãn, cận chiến mạnh, bắn kém.','Đạo quân xương bất tử: thành trì 10.000–20.000 quân, cực hiếu chiến, thù địch với mọi tộc.'][c]}</p>`,btn)}
function startMap(){mode='map';acBtn();showArrows(8);if(G&&!G.seenGuide){G.seenGuide=1;G.lbl=1;setTimeout(()=>{if(!paused)menu('⚔ Chào mừng, hiệp sĩ!',INTRO,[['▶ Bắt đầu chơi!',()=>{close();setTimeout(qMenu,600)}],['📖 Xem hướng dẫn đầy đủ',()=>{close();panel('hd')}]])},3500)}if(G&&!G.granted){G.granted=1;setTimeout(()=>grantVillage(1),1200)}$('#top').style.display='flex';$('#zb').style.display='flex';lblSet(G&&G.lbl==1&&G.day<6,1);qTick();G.lastRank=rank(P0())[0]}
let last=performance.now(),ht=0;
function step(now){const dt=Math.min(.05,(now-last)/1000);last=now;const t=now/1000;
 if(!document.hidden&&!paused){if(mode=='map'){const n=G&&G.xian?(G.ts||2):1;for(let i=0;i<n;i++)upMap(dt)}else if(mode=='battle'&&B)upBattle(dt*B.spd)}
 if(mode=='battle'&&B)drawBattle(t);else drawMap(t);if((ht-=dt)<0){ht=ULQ?.8:.3;hud()}}
const JQ=[];function runJobs(lim){const a=performance.now();while(JQ.length&&G){const f=JQ.shift();try{f()}catch(e){console.error(e)}if(performance.now()-a>lim)break}}
let LAGON=(()=>{try{return localStorage.getItem('ltlc-lag')!='0'}catch(e){return true}})(),LF={n:0,t0:0,last:0,mx:0,mxT:0,fps:0};
function lagTick(now){const g=LF.last?now-LF.last:0;LF.last=now;LF.n++;if(g>LF.mx||now-LF.mxT>5000){LF.mx=g;LF.mxT=now}if(now-LF.t0>=1000){LF.fps=Math.round(LF.n*1000/(now-LF.t0));LF.n=0;LF.t0=now;if(MOB&&G&&!paused&&!document.hidden){const tg=ULQ?24:29;if(LF.fps<tg*.75){LF.lo=(LF.lo||0)+1;LF.hi=0}else if(LF.fps>=tg){LF.hi=(LF.hi||0)+1;LF.lo=0}else LF.lo=LF.hi=0;if(LF.lo>=2&&DSR>.55){DSR=+(DSR-.1).toFixed(2);LF.lo=0;rs()}else if(LF.hi>=8&&DSR<1){DSR=Math.min(1,+(DSR+.1).toFixed(2));LF.hi=0;rs()}}tsBtn();const e=$('#lag');if(!e)return;const show=LAGON&&G&&mode!='title';e.style.display=show?'block':'none';if(!show)return;const tp=$('#top');e.style.top=((tp&&tp.offsetHeight?tp.getBoundingClientRect().bottom:40)+4)+'px';const mx=Math.round(LF.mx);e.innerHTML=SMALL()?`📶${LF.fps} ${mx>250?'🔴':mx>100?'🟡':'🟢'}`:`📶 ${LF.fps} hình/giây · giật lớn nhất ${mx}ms ${mx>250?'🔴':mx>100?'🟡':'🟢'}${DSR<1?` · nét ${Math.round(DSR*100)}%`:''}`}}
let lfr=0;function loop(now){const cap=paused&&mode!='battle'?(ULQ?250:120):!MOB?0:ULQ?40:(LOWQ||mode=='map')?32:0;if(now-lfr<cap){requestAnimationFrame(loop);return}lfr=now;lagTick(now);try{if(JQ.length)runJobs(JQ.length>120?60:JQ.length>40?14:6);else if(TD&&G&&now-tdT>400){tdT=now;terrNow()}if(mode=='map')ensureCont();step(now)}catch(e){console.error(e)}requestAnimationFrame(loop)}
setTimeout(()=>{bake();$('#load').remove();titleMenu();requestAnimationFrame(loop)},30);
window.__T={qCur,qMenu,qHints,lblSet,GUIDE_D,slMenu,slSwitch,slExport,curSlot,slMeta,dhUpdate,cgMenu,cgUp,lsInit,fmtLS,tangGo,thienLo,tangCheck,held,genTangWorld,rank,wmAt:(x,y)=>WMAP?wmAt(x,y):-1,save:()=>save(),acToggle,acTick,JQ,runJobs,slim,newDay:()=>newDay(),drawMap:t=>drawMap(t),drawBattle:t=>drawBattle(t),setQ,QL:()=>QL,crown,rebel,contsHeld,vassalDay,chat,exileMenu,partyMenu,calcCH,diplo,hireGen,myGens,V,villageMenu,grantVillage,income,startFight,joinFight,encounter,toast,G:()=>G,S,B:()=>B,newGame,startMap,startBattle,endBattle,upMap,upBattle,quick,townMenu,setOrder,close,panel,getMode:()=>mode,MC,BC,rank,fiefs,indep};
