function mkP(o){return Object.assign({id:G.L.length,name:'',fac:0,kind:'lord',x:0,y:0,t:Z3(),tx:0,ty:0,goS:null,goP:null,to:-1,th:rnd(0,2),dead:0,safe:2,face:1,mv:0},o)}
let PSC=1;function pushP(o){let slot=-1;const N=G.L.length;for(let k=0;k<Math.min(N,400);k++){const i=1+(PSC+k)%Math.max(1,N-1),p=G.L[i];if(p&&p.kind=='rf'&&p.dead==-1&&p.id>0){slot=i;PSC=i+1;break}}if(slot<0)PSC=(PSC+400)%Math.max(1,N);const p=mkP(o);if(slot>0){p.id=slot;G.L[slot]=p}else{p.id=G.L.length;G.L.push(p)}p.tx=p.x;p.ty=p.y;if(G.xian&&p.kind=='rf'&&G.L[0]&&p.fac==G.L[0].fac){const o=G.L[p.to];if(o&&!o.dead&&o.fac==p.fac)rfTp(p,o,1600)}return p}
function rfTp(p,o,lim){if(dist(o,p)<=lim&&contOf(o.x,o.y)==contOf(p.x,p.y))return;const a=Math.random()*6.283,r=rnd(1800,2600);p.x=cl(o.x+Math.cos(a)*r,60,WW-60);p.y=cl(o.y+Math.sin(a)*r*.7,60,WH-60);if(contOf(p.x,p.y)!=contOf(o.x,o.y)){p.x=o.x-r*.8;p.y=o.y}p.tx=p.x;p.ty=p.y;p.tp=1}
function landPt(){for(let i=0;i<800;i++){const x=rnd(200,WW-200),y=rnd(200,WH-200);if(OPEN(contOf(x,y))&&okLand(x,y)&&(!G.L[0]||Math.hypot(G.L[0].x-x,G.L[0].y-y)>500)&&S.every(s=>dist(s,{x,y})>150))return{x,y}}return{x:WW/2,y:WH/2}}
function setupFac(fi2,k){const f=G.F[fi2];let gi=ri(0,40);const RC=RACE[f.race||0],gn=()=>f.wm!=null?wmName(f):f.race?RC.giv[(gi++)%RC.giv.length]+' '+f.sur:f.sur+' '+RC.giv[(gi++)%RC.giv.length];
 const DK=f.race==4,DV=f.race>=5&&f.race<9,DX=f.race>=9;S.filter(s=>s.f0==k).forEach(s=>{s.fac=fi2;s.pool=[300,200,100][s.type];s.gar=mix((DX?[ri(7000,9000),ri(4500,5500),ri(2800,3500)][s.type]:[1800,1000,600][s.type])*PW(f.race));
  let o;if(s.type==0){o=pushP({kind:'king',name:gn(),fac:fi2,x:s.x+rnd(-20,20),y:s.y+25,t:mix((DX?ri(20000,30000):ri(1200,1800))*PW(f.race))});f.king=o.id}
  else o=pushP({kind:'lord',name:gn(),fac:fi2,x:s.x+rnd(-20,20),y:s.y+25,t:mix((DX?ri(2000,4000):ri(250,500))*PW(f.race))});s.own=o.id;
  {const xt=mix(DX?ri(10000,20000):ri(120,260));if(s.type==0)pushP({kind:'lord',name:gn(),fac:fi2,x:s.x+rnd(-30,30),y:s.y+rnd(20,45),t:xt});else add(o.t,xt)}});
 V.forEach(v=>{if(S[v.p].f0==k){v.own=S[v.p].own;v.pool=20;v.burn=0}})}
const AGR=p=>G.tang&&p.kind=='lord'&&G.L[0]&&p.fac==G.L[0].fac?1.15:!G.F[p.fac]?2.6:G.F[p.fac].race>=5?1.2:G.F[p.fac].race==4?1.05:G.F[p.fac].race?1.8:2.6;
function initWar(list){for(const i of list){const f=G.F[i],ci=S.find(s=>s.fac==i&&s.type==0);if(!ci)continue;
 const o=S.filter(s=>s.type==0&&s.race==f.race&&G.F[s.fac]&&G.F[s.fac].cn!=f.cn).sort((x,y)=>dist(x,ci)-dist(y,ci))[0];if(o)G.war[i][o.fac]=G.war[o.fac][i]=1}}
function extraWar(list){for(const i of list){const ci=S.find(s=>s.fac==i&&s.type==0);if(!ci)continue;const o=S.filter(s=>s.type==0&&s.race==G.F[i].race&&s.fac!=i&&!G.war[i][s.fac]).sort((x,y)=>dist(x,ci)-dist(y,ci)).slice(0,2);for(const s of o)G.war[i][s.fac]=G.war[s.fac][i]=1}}
function sanitize(){const fx=t=>{if(!t)return;for(const k of KS){if(!(t[k]>=0))t[k]=0;t[k]=Math.round(t[k])}};
 for(const p of G.L){if(p.dead)continue;fx(p.t);const n=tot(p.t);if(n<=3000&&p.kind!='pl')continue;const M=LKM(),lim=p.kind=='pl'?rank(p)[1]*1.5:p.kind=='rf'||p.kind=='bandit'||p.kind=='exile'?(p.kind=='rf'?20000:3000)*M:(G.F[p.fac]&&G.F[p.fac].race>=9)?Math.max(rank(p)[1]*1.5,3000*M):p.inv?20000*M:Math.max(rank(p)[1]*2,3000*M);if(n>lim){const k=lim/n;KS.forEach(q=>p.t[q]=Math.floor(p.t[q]*k))}}
 for(const s of S){if(!s.gar)continue;fx(s.gar);const lim=Math.max((s.race>=9?15000:6000)*PW(s.race),G.divine&&s.fac==P0().fac?myGarT(s)*1.3:0),n=tot(s.gar);if(n>lim){const k=lim/n;KS.forEach(q=>s.gar[q]=Math.floor(s.gar[q]*k))}if(!(s.pool>=0))s.pool=0}}
function slim(){const pl=P0();let m=0;for(let i=0;i<G.F.length;i++){const f=G.F[i];if(f.dead||i==pl.fac)continue;const ss=S.filter(s=>s.fac==i);if(!ss.length)continue;const own=new Set(ss.map(s=>s.own));
 const fr=G.L.filter(q=>!q.dead&&q.fac==i&&q.kind=='lord'&&!own.has(q.id)&&!q.inF&&!q.inv&&!q.vuong&&dist(q,pl)>700).sort((a,b)=>tot(b.t)-tot(a.t)),keep=Math.ceil(ss.length/2)+1;if(fr.length<=keep)continue;
 const k=G.L[f.king],to=k&&!k.dead&&k.fac==i?k:null;for(const q of fr.slice(keep)){if(to)add(to.t,q.t);q.dead=-1;q.t=Z3();q.goS=q.goP=null;m++}}if(m){sanitize();G.ngen=myGens().length}return m}
function invade(){const pl=P0(),cand=G.F.map((f,i)=>i).filter(i=>!G.F[i].dead&&i!=pl.fac&&OPEN(G.F[i].race||0)&&(G.F[i].race||0)!=ACT&&S.some(s=>s.fac==i)&&S.some(s=>s.race==ACT&&atWar(i,s.fac)));if(!cand.length)return;
 const dk=cand.filter(i=>G.F[i].race==4),cp=dk.length&&Math.random()<.5?dk:cand,a=cp[ri(0,cp.length-1)],ra=G.F[a].race||0;
 const tg0=S.filter(s=>s.race==ACT&&atWar(a,s.fac));if(!tg0.length)return;const mine=tg0.filter(s=>s.fac==pl.fac),pool=mine.length&&Math.random()<.5?mine:tg0,tg=pool[ri(0,pool.length-1)];
 const cx=OX[ACT]+CWc[ACT]/2,cy=OY[ACT]+CHc[ACT]/2,ang=Math.atan2(tg.y-cy,tg.x-cx);let x=tg.x,y=tg.y;for(let i=0;i<120&&hW(x,y)>=.36;i++){x+=Math.cos(ang)*60;y+=Math.sin(ang)*60}
 x=cl(x,50,WW-50);y=cl(y,50,WH-50);const RC=RACE[ra],n=(ra>=9?ri(6000,12000):ri(2500,6000))*PW(ra);
 const nm=ra?RC.giv[ri(0,RC.giv.length-1)]+' '+G.F[a].sur:G.F[a].sur+' '+RC.giv[ri(0,RC.giv.length-1)];
 const p=pushP({kind:'lord',name:nm,fac:a,x,y,t:mix(n),inv:1,ren:3000});p.goS=tg;p.safe=3;
 const ic=ra>=9?'🌀':ra>=5?'⚡':ra==4?'💀':'⛵';toast(`${ic} ${facN(a)} (${RACE[ra].n}) vượt biển với ${fmt(n)} quân, nhắm vào ${tg.name}!`,ra==4?'#c58cff':'#ffb070',tg.fac==pl.fac);addLog(`${ic} ${facN(a)} (${RACE[ra].n}) đưa ${fmt(n)} quân vượt biển đánh ${tg.name}.`,'#ffb070')}
function xWar(){const pl=P0(),al=G.F.map((f,i)=>i).filter(i=>!G.F[i].dead&&G.F[i].race!=4&&OPEN(G.F[i].race||0)&&S.some(s=>s.fac==i));if(al.length<2)return;
 const a=al[ri(0,al.length-1)],bl=al.filter(i=>(G.F[i].race||0)!=(G.F[a].race||0)),b=bl[ri(0,bl.length-1)];if(b==null)return;const w=G.war[a][b]?(Math.random()<.3?0:1):1;if(w==G.war[a][b])return;G.war[a][b]=G.war[b][a]=w;terr();
 const msg=w?`⚔ ${facN(a)} (${RACE[G.F[a].race||0].n}) tuyên chiến với ${facN(b)} (${RACE[G.F[b].race||0].n}) bên kia biển!`:`🕊 ${facN(a)} và ${facN(b)} giảng hòa.`;if(a==pl.fac||b==pl.fac)toast(msg,w?'#ff6a5a':'#7dff8a');addLog(msg,'#ffb070')}
function splitDark(){if(G.split)return;G.split=1;const pl=P0();
 for(const s of S.slice()){if(s.race!=4)continue;const fi=s.fac,f=G.F[fi];if(!f||f.race!=4)continue;const mine=S.filter(q=>q.fac==fi);if(mine.length<2)continue;
  const keep=mine.find(q=>q.type==0)||mine[0];if(s===keep||(fi==pl.fac&&s.own===0))continue;
  const ni=G.F.length;G.F.push({sur:s.name,n:'Quân đoàn '+s.name,cn:s.cn,race:4,c:`hsl(${ri(0,359)},${ri(45,70)}%,${ri(36,56)}%)`,king:-1,dead:0,emp:0});
  G.war.forEach(r=>r.push(1));G.war.push(G.F.map((x,j)=>j==ni?0:1));
  let king=G.L[s.own];if(!king||king.dead||king.fac!=fi||king.kind=='pl')king=null;const near=G.L.filter(q=>!q.dead&&q.fac==fi&&q.kind=='lord'&&q!==king&&dist(q,s)<140);
  if(!king)king=near.shift()||pushP({kind:'lord',name:RACE[4].giv[ri(0,17)]+' '+s.name,fac:ni,x:s.x,y:s.y+25,t:Z3()});
  king.kind='king';king.fac=ni;if(tot(king.t)<1200)add(king.t,mix(ri(1200,1800)-tot(king.t)));G.F[ni].king=king.id;s.own=king.id;s.fac=ni;near.forEach(q=>q.fac=ni);
  V.forEach(v=>{if(v.p==s.id&&v.own!==0)v.own=king.id})}
 for(const f of G.F)if(f.race==4&&f.king>=0){const k=G.L[f.king];if(k&&k.kind!='king'&&k.kind!='pl')k.kind='king'}terr();calcMV(1)}
const LOCKT=c=>c<4?'Chiếm 3/4 thành châu lục của bạn để mở 4 châu lục':c==4?'Chiếm 3/4 thành của 2 châu lục để mở Vùng Đất Chết':c<9?'Chiếm 1/2 Vùng Đất Chết để mở Thời đại Thần linh':'Chiếm 3/4 thành của 2/4 lục địa Thần linh để mở 🌀 Cửu Thiên Huyền Giới';
const held=c=>{const ss=S.filter(s=>s.race==c);return ss.length?ss.filter(s=>s.fac==P0().fac).length/ss.length:0};
function progress(){if(!G.open)G.open=[0,1,2,3,4];
 if(G.open.length==1&&held(G.open[0])>=.75){G.open=[0,1,2,3];terr();toast('🗺 BẢN ĐỒ MỞ RỘNG!<br>Bạn đã chinh phục 3/4 châu lục quê nhà — 4 châu lục Nhân tộc · Người Lùn · Elf · Người Sói đã mở.','#7fe3ff',1);addLog('🗺 Mở bản đồ 4 châu lục.','#7fe3ff')}
 if(!G.open.includes(4)&&[0,1,2,3].filter(c=>held(c)>=.75).length>=2){G.open.push(4);terr();toast('💀 VÙNG ĐẤT CHẾT hiện ra ở phía Đông!<br>Bạn đã làm chủ 2 châu lục.','#c58cff',1);addLog('💀 Mở Vùng Đất Chết.','#c58cff')}
 if(!G.divine&&G.open.includes(4)&&held(4)>=.5)unlockDivine();
 if(G.divine&&!G.xian&&[5,6,7,8].filter(c=>held(c)>=.75).length>=2)unlockXian();
 if(G.xian&&!G.lsOn)lsInit();
 if(G.xian&&!G.lk&&[9,10,11].some(c=>held(c)>=.75))unlockLK();
 tangCheck()}
function unlockLK(){G.lk=1;const m=t=>{if(t)KS.forEach(k=>t[k]=Math.round(t[k]*5))};for(const p of G.L)if(!p.dead)m(p.t);for(const s of S){m(s.gar);s.pool=Math.round((s.pool||0)*5)}for(const v of V)v.pool=Math.round((v.pool||0)*5);SFX.fan();
 toast('✨ THỜI ĐẠI LINH KHÍ KHÔI PHỤC!<br>Linh khí tràn ngập mọi châu lục — toàn bộ quân đội, thành trì, nguồn lính và thu nhập tăng <b>×5</b><br>Chức vị chuyển sang cảnh giới tu tiên: Luyện Khí → Trúc Cơ → Kim Đan → Nguyên Anh → Hóa Thần → Luyện Hư → Đại Thừa → Tiên Vương → Tiên Đế → Chuẩn Đế<br><small>Chiếm 2/3 thành của 2 lục địa Cửu Thiên để ⚡ PHI THĂNG lên 23 Tầng Trời… trên cùng nghe nói là Tiên Giới</small>','#bfffd8',1);addLog('✨ Thời đại Linh khí khôi phục — toàn quân ×5.','#bfffd8');save()}
function unlockXian(){G.xian=1;unlockWorld2();G.portals=null;mkPortals();const n0=G.F.length;addConts();for(let i=n0;i<G.F.length;i++)for(let j=0;j<G.F.length;j++){if(i==j)continue;const fj=G.F[j];const w=j==P0().fac?1:fj.race>=9?(fj.race!=G.F[i].race?1:G.war[i][j]||0):Math.random()<.3?1:0;G.war[i][j]=G.war[j][i]=w}
 terr();SFX.fan();toast('🌀 CỔNG TRUYỀN TỐNG CỬU THIÊN HUYỀN GIỚI ĐÃ MỞ!<br>3 lục địa tu tiên: ☁️ Thiên Nguyên Giới · ☀️ Huyền Hoang Vực · 🌑 Cửu U Tiên Vực<br>Tông môn & Thánh địa cai quản phàm nhân — chiếm 3/4 thành 1 lục địa tu tiên để mở ✨ Thời đại Linh khí khôi phục!<br><small>Thông đạo 🌀 xuất hiện khắp lãnh địa các vị thần — bước vào để sang thế giới khác</small>','#9ff0ff',1);addLog('🌀 Mở Cổng truyền tống Cửu Thiên Huyền Giới.','#9ff0ff');save()}
function mkPortals(){if(G.portals)return;G.portals=[];const add=(c,n)=>{let k=0;for(let tr=0;tr<3000&&k<n;tr++){const x=OX[c]+300+Math.random()*(CWc[c]-600),y=OY[c]+300+Math.random()*(CHc[c]-600);if(!okLand(x,y)||S.some(s=>Math.hypot(s.x-x,s.y-y)<160)||G.portals.some(q=>Math.hypot(q.x-x,q.y-y)<1200))continue;G.portals.push({x,y,w:c>=9?1:0});k++}};
 for(let c=5;c<9;c++)add(c,4);for(let c=9;c<12;c++)add(c,3)}
function usePortal(q){const pl=P0(),ds=G.portals.filter(o=>o.w!=q.w),d=ds[ri(0,ds.length-1)];if(!d)return;stopPl();pl.x=d.x+rnd(-40,40);pl.y=d.y+70;pl.tx=pl.x;pl.ty=pl.y;pl.safe=6;MC.follow=1;
 for(const g of myGens())if(G.call){g.x=pl.x+rnd(-90,90);g.y=pl.y+rnd(-60,60);g.tx=g.x;g.ty=g.y;g.goS=g.goP=null}SFX.fan();toast(d.w?'🌀 Bước qua Thông đạo — bạn đã tới CỬU THIÊN HUYỀN GIỚI!':'🌀 Bước qua Thông đạo — bạn trở về lãnh địa các vị thần','#9ff0ff',1)}
function tpCost(s){const pl=P0(),d=dist(pl,s)+(WRLD(s.y)!=WRLD(pl.y)?20000:0),m=s.land?1.5:1;return{g:Math.round((300+d*.25)*m),d:Math.max(1,Math.ceil(d/4000*(s.land?1.25:1)))}}
function landNear(s,zf){for(let r=260;r<700;r+=40)for(let a=0;a<6.28;a+=.5){const x=s.x+Math.cos(a)*r,y=s.y+Math.sin(a)*r*.8;if(!okLand(x,y)||(zf&&!zf(x,y)))continue;if(S.some(o=>Math.abs(o.x-x)<220&&Math.abs(o.y-y)<220))continue;return{x,y}}return{x:s.x+60,y:s.y+60}}
function tpZones(){const Z=[];for(let c=0;c<13;c++){if(!OPEN(c))continue;if(c==0&&WMAP){CC.forEach((cc,k)=>{if(cc.race!==0)return;Z.push({c,k,n:`${['🌏','🏰','🌍','🗽','🌎','🏝'][WREG.indexOf(cc.n)]||'🧑'} ${cc.n}`,cx:cc.x,cy:cc.y,f:s=>s.race==0&&s.cn==k})})}else Z.push({c,n:`${RIC[c]} ${RACE[c].n}`,cx:OX[c]+CWc[c]/2,cy:OY[c]+CHc[c]/2,f:s=>s.race==c})}return Z}
function tpMenu(){const pl=P0(),bo=[],bl=[];for(const z of tpZones()){const all=S.filter(z.f);if(!all.length)continue;const ss=all.filter(s=>s.fac==pl.fac);let s,txt;
  if(ss.length){s=ss.find(x=>x.own===0&&x.type==0)||ss.find(x=>x.own===0)||ss.find(x=>x.type==0)||ss[0];txt=`→ ${s.name} · ${ss.length} thành của bạn`}
  else{const t=all.map(x=>[x,(x.x-z.cx)**2+(x.y-z.cy)**2+(atWar(pl.fac,x.fac)?4e6:0)]).sort((a,b)=>a[1]-b[1])[0][0],p=landNear(t,z.c==0&&WMAP?(x,y)=>{const q=wmAt(x,y);return q>0}:null);s={x:p.x,y:p.y,name:'bến đổ bộ gần '+t.name,race:z.c,land:1};txt=`→ đổ bộ gần ${t.name} · chưa có thành`}
  if(dist(pl,s)<400)continue;const k=tpCost(s);(ss.length?bo:bl).push([`${z.n} ${txt} · 💰${fmt(k.g)} · ⏳${k.d} ngày`,()=>tpGo(s),G.gold<k.g])}
 const btn=[...bo,...bl];if(!btn.length)btn.push(['Chưa có châu lục nào khác để dịch chuyển',close,1]);btn.push(['Đóng',close]);
 menu('🌐 Dịch chuyển',`<p style="font-size:12.5px">Dịch chuyển tới mọi châu lục đã mở. Về thành của bạn thì rẻ hơn; tới châu lục chưa có thành (đổ bộ viễn chinh) tốn thêm 50% vàng và lâu hơn. Tốn vàng và ngày theo khoảng cách; trong lúc đi thời gian vẫn trôi.</p><p>💰 Vàng hiện có: <b>${fmt(G.gold)}</b></p>`,btn)}
function tpGo(s){const pl=P0(),k=tpCost(s);if(G.gold<k.g)return;G.gold-=k.g;close();stopPl();for(let i=0;i<k.d;i++){newDay();G.dayT=0}
 pl.x=s.x+(s.land?0:rnd(-30,30));pl.y=s.y+(s.land?0:40);pl.tx=pl.x;pl.ty=pl.y;pl.safe=5;MC.follow=1;
 if(G.call)for(const g of myGens()){g.x=pl.x+rnd(-90,90);g.y=pl.y+rnd(-60,60);g.tx=g.x;g.ty=g.y;g.goS=g.goP=null}
 SFX.fan();if(s.land)pl.safe=8;toast(`🌐 Đã ${s.land?'đổ bộ tới':'dịch chuyển tới'} ${s.name} (${RACE[s.race].n}) — tốn ${fmt(k.g)} vàng, ${k.d} ngày`,'#9ff0ff');addLog(`Dịch chuyển tới ${s.name} (-${fmt(k.g)} vàng, ${k.d} ngày).`,'#9cf');save()}
function portal(go){const pl=P0();let s;if(go){const ss=S.filter(s=>s.race>=9&&s.type==2);s=ss[ri(0,ss.length-1)]}else{const own=S.filter(s=>s.fac==pl.fac&&s.race<9);s=own.find(x=>x.own===0)||own[0]}if(!s)return;close();stopPl();pl.x=s.x+rnd(-80,80);pl.y=s.y+120;pl.tx=pl.x;pl.ty=pl.y;pl.safe=6;MC.follow=1;
 for(const g of myGens())if(G.call){g.x=pl.x+rnd(-90,90);g.y=pl.y+rnd(-60,60);g.tx=g.x;g.ty=g.y;g.goS=g.goP=null}SFX.fan();toast(go?'🌀 Truyền tống tới Cửu Thiên Huyền Giới!':'🌀 Truyền tống về cố hương','#9ff0ff')}
function unlockDivine(){G.divine=1;unlockWorld();const n0=G.F.length;addConts();const nw=G.F.map((f,i)=>i).filter(i=>i>=n0);
 for(const i of nw)for(let j=0;j<G.F.length;j++){if(i==j)continue;const fj=G.F[j];const w=j==P0().fac||fj.race==4?1:fj.race>=5?(fj.race!=G.F[i].race?1:G.war[i][j]):Math.random()<.4?1:0;G.war[i][j]=G.war[j][i]=w}
 terr();SFX.fan();setTimeout(()=>SFX.war(),900);const r=rank(P0());
 toast(`🌟 THỜI ĐẠI THẦN LINH KHAI MỞ!<br>Phong ấn bị phá — 4 châu lục thần linh xuất hiện:<br>🗿 Titan · 👼 Thiên Thần · 👹 Quỷ tộc · 🦊 Vạn Yêu<br><small>Chiếm 2/4 lục địa này để mở 🌀 Cửu Thiên Huyền Giới</small><br>Bạn được tôn là <b>${r[2]} ${r[0]}</b> — dẫn tới ${fmt(r[1])} quân!`,'#fff07a',1);addLog(`🌟 Thời đại Thần linh khai mở. Bạn xưng ${r[0]}.`,'#fff07a');save()}
function calcCH(){G.ch=G.ch||[];for(let c=0;c<NC();c++){const ss=S.filter(s=>s.race==c);if(!ss.length)continue;const f=ss[0].fac,u=ss.every(s=>s.fac==f)?f:-1;if(G.ch[c]==null)G.ch[c]=-1;if(u!==G.ch[c]){G.ch[c]=u;if(u>=0&&G.F[u]){const k=G.L[G.F[u].king],me=k&&k.kind=='pl';
  const m=`${CHT[c][1]} ${me?'BẠN':facN(u)} thống nhất châu lục ${RACE[c].n} — xưng ${CHT[c][0].toUpperCase()}!`;toast(m,CHT[c][2],1);addLog(m,CHT[c][2])}}}}
function calcMV(q){calcCH();progress();const ds=G.F.map((f,i)=>i).filter(i=>G.F[i].race==4&&!G.F[i].dead&&S.some(s=>s.fac==i));if(!ds.length){G.mv=-1;return}
 const SCv=new Map(ds.map(i=>[i,0]));for(const s of S)if(SCv.has(s.fac))SCv.set(s.fac,SCv.get(s.fac)+1e6+tot(s.gar));for(const p of G.L)if(!p.dead&&SCv.has(p.fac))SCv.set(p.fac,SCv.get(p.fac)+tot(p.t));const b=ds.sort((x,y)=>SCv.get(y)-SCv.get(x))[0];if(b===G.mv)return;const old=G.mv;G.mv=b;const k=G.L[G.F[b].king];
 if(!q&&k){const me=k.kind=='pl';if(me||ACT==4)toast(me?'😈 BẠN đã trở thành MA VƯƠNG — kẻ mạnh nhất Vùng Đất Chết!':`😈 ${k.name} của ${facN(b)} trở thành MA VƯƠNG Vùng Đất Chết!`,'#c04cff',me);addLog(`😈 ${me?'Bạn':k.name} (${facN(b)}) trở thành Ma Vương.`,'#d58cff')}}
