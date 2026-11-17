function absWar(CL){const pl=P0();for(const c of CL||[0,1,2,3,4,4,...(G.divine?[5,6,7,8]:[]),...(G.xian?[9,10,11]:[]),...(G.tang?[12]:[])]){if(c==ACT||Math.random()<.4)continue;
 const fs=G.F.map((f,i)=>i).filter(i=>(G.F[i].race||0)==c&&!G.F[i].dead&&i!=pl.fac&&S.some(s=>s.fac==i));if(!fs.length)continue;
 for(const p of G.L)if(!p.dead&&(p.kind=='lord'||p.kind=='king')&&p.fac>=0&&((G.F[p.fac]&&G.F[p.fac].race)||0)==c&&contOf(p.x,p.y)==c){const cap=rank(p)[1];if(tot(p.t)<cap)add(p.t,mix(Math.min(cap-tot(p.t),Math.ceil(cap*.03))))}
 const a=fs[ri(0,fs.length-1)],ls=G.L.filter(p=>!p.dead&&p.fac==a&&(p.kind=='lord'||p.kind=='king')),pw=ls.reduce((x,p)=>x+str(p.t),0)*.6+(c>=4?S.filter(s=>s.fac==a).reduce((x,s)=>x+str(s.gar)*.45,0):0),own=S.filter(s=>s.fac==a),xc=Math.random()<.2;
 const tg=S.filter(s=>(xc?s.race!=c&&s.race!=ACT&&OPEN(s.race)&&OPEN(c)&&(s.race==12)==(c==12):s.race==c)&&s.fac!=a&&atWar(a,s.fac)&&s.fac!=pl.fac).map(x=>{let m=1e12;for(const o of own){const dx=o.x-x.x,dy=o.y-x.y,q=dx*dx+dy*dy;if(q<m)m=q}x._d=m;return x}).sort((x,y)=>x._d-y._d)[0];
 if(!tg||!ls.length||pw<str(tg.gar)*(xc?2:c==4?.85:1.5))continue;if(xc)addLog(`⛵ ${facN(a)} (${RACE[c].n}) vượt biển chiếm ${tg.name} của ${RACE[tg.race].n}!`,'#ffb070');const lead=ls.sort((x,y)=>tot(y.t)-tot(x.t))[0];ls.forEach(p=>kill(p.t,Math.round(tot(p.t)*.15)));kill(tg.gar,tot(tg.gar));lead.x=tg.x+15;lead.y=tg.y+25;lead.tx=lead.x;lead.ty=lead.y;capture(tg,lead)}}
function addConts(){G.cmap=G.cmap||{};const nw=[];
 F0.forEach((f,k)=>{if(!f.race||G.cmap[k]!=null)return;const ni=G.F.length;G.cmap[k]=ni;G.F.push({...f,king:-1,dead:0,emp:0});nw.push([ni,k])});
 const N=G.F.length;G.war.forEach(r=>{while(r.length<N)r.push(0)});while(G.war.length<N)G.war.push(new Array(N).fill(0));
 if(!nw.length)return 0;nw.forEach(([ni,k])=>setupFac(ni,k));const lw=nw.map(a=>a[0]).filter(i=>G.F[i].race!=4);initWar(lw);extraWar(lw);darkWar();
 for(let i=0;i<(nw.length>15?36:8);i++){const b=pushP({kind:'bandit',fac:BAN,name:'Thổ phỉ'});respawn(b)}return nw.length}
function darkWar(){G.F.forEach((a,i)=>G.F.forEach((b,j)=>{if(i==j)return;const da=a.race==4,db=b.race==4;if(da!=db)G.war[i][j]=1;else if(da&&db)G.war[i][j]=1}))}
function newGame(k){JQ.length=0;G={day:1,dayT:0,gold:2000,log:[],L:[],rf:1,fights:[],pf:0,F:F0.filter(f=>!f.race).map(f=>({...f,king:-1,dead:0,emp:0})),war:[]};
 G.F.forEach((a,i)=>{G.war[i]=G.F.map(()=>0)});
 const cap0=S.find(s=>s.f0==k&&s.type==0);
 G.L.push(mkP({kind:'pl',name:'Bạn',fac:0,x:cap0.x+20,y:cap0.y+30,t:{inf:120,arc:60,cav:30}}));G.L[0].tx=G.L[0].x;G.L[0].ty=G.L[0].y;
 G.F.forEach((f,i)=>setupFac(i,i));S.forEach(s=>{if(!s.race){}});initWar(G.F.map((f,i)=>i));if(WMAP)extraWar(G.F.map((f,i)=>i));
 G.home=F0[k].race||0;G.open=[G.home];G.auto=1;for(let i=0;i<26;i++){const b=pushP({kind:'bandit',fac:BAN,name:'Thổ phỉ'});respawn(b)}
 addConts();const fi=F0[k].race?G.cmap[k]:k;G.pf=fi;G.L[0].fac=fi;splitDark();
 terr();MC.z=.7;MC.follow=1;
 addLog('Kéo để xem bản đồ, chụm 2 ngón hoặc ＋/－ để phóng to. Chạm để đi, chạm thành để vào/công thành.','#ffd77a');
 addLog(`Bạn là Hiệp sĩ ${RACE[G.F[fi].race||0].n} phụng sự ${G.F[fi].n} (${CC[G.F[fi].cn].n}). Chiếm đất để được phong tước!`,G.F[fi].c)}
function newName(f){if(f.wm!=null)return wmName(f);const RC=RACE[f.race||0],g=RC.giv[ri(0,RC.giv.length-1)];return f.race?g+' '+f.sur:f.sur+' '+g}
const ordN=n=>['','cả','thứ 2','thứ 3','thứ 4','thứ 5','thứ 6','thứ 7','thứ 8','thứ 9'][Math.min(9,n)]||('thứ '+n);
function respawn(p){p.goS=p.goP=null;p.dead=0;p.inF=0;
 if(p.kind=='king'&&G.F[p.fac]){const f=G.F[p.fac];f.heirs=f.heirs==null?ri(1,4):f.heirs;if(f.heirs>0){f.heirs--;f.gen=(f.gen||1)+1;p.name=newName(f);p.ren=0;const m=`👑 Thái tử ${p.name} kế vị ngai vàng ${f.n} (đời thứ ${f.gen}).`;addLog(m,'#ffd77a');if(p.fac==P0().fac||contOf(p.x,p.y)==ACT)toast(m,'#ffd77a')}}
 if(p.kind=='bandit'){const q=landPt();p.x=q.x;p.y=q.y;p.t=mix(ri(40,220))}
 else{if(G.tang&&p.kind=='lord'&&p.fac==P0().fac&&!S.some(s=>s.own===p.id&&s.race!=12)){const o12=S.filter(s=>s.fac==p.fac&&s.race==12),pl=P0(),b=o12.length?o12[ri(0,o12.length-1)]:contOf(pl.x,pl.y)==12?pl:tangLand();p.x=b.x+rnd(-40,40);p.y=b.y+rnd(25,50);p.tx=p.x;p.ty=p.y;p.t=mix(rank(p)[1]*.3|0);p.safe=3;return}const own=S.filter(s=>s.fac==p.fac);if(!own.length){p.dead=-1;return}const mine=own.filter(s=>s.own===p.id),s=(mine.length?mine:own)[0];p.x=s.x+rnd(-25,25);p.y=s.y+rnd(20,40);p.t=mix(Math.max(100,rank(p)[1]*.15|0))}
 p.tx=p.x;p.ty=p.y}
function addLog(m,c='#ddd'){if(!G)return;G.log.push({m:`Ngày ${G.day}: ${m}`,c});if(G.log.length>6)G.log.shift();rlog()}
const rlog=()=>{$('#log').innerHTML=G?G.log.map(l=>`<div style="color:${l.c}">${l.m}</div>`).join(''):''};
const KEY='loan-the-lanh-chua-v3';
const SVX=new Set(['_c','_i','mv','face','goF','goV','th','goP','goS']),SVR=new Set(['x','y','tx','ty']);
function svP(p){if(p.dead<0&&p.kind!='pl')return{id:p.id,kind:p.kind,name:p.name,fac:p.fac,x:p.x|0,y:p.y|0,dead:-1};const o={};for(const k in p){if(SVX.has(k))continue;let v=p[k];if(v==null||v===false)continue;if((k=='dead'||k=='inF')&&!v)continue;if(k=='safe'&&!(v>0))continue;if(typeof v=='number')v=SVR.has(k)?Math.round(v):Number.isInteger(v)?v:Math.round(v*10)/10;o[k]=v}if(p.goP)o.goP=p.goP.id;if(p.goS)o.goS=p.goS.id;return o}
function save(){try{localStorage.setItem('ltlc-map',WMAP?'2':'1');localStorage.setItem(KEY,JSON.stringify({...G,L:G.L.map(svP),war:G.war.map(r=>r.map(v=>v?1:0).join('')),SS:S.map(s=>[s.fac,s.own,s.gar,s.pool]),VV:V.map(v=>[v.own,v.pool,v.burn])}))}catch(e){}}
addEventListener('visibilitychange',()=>{if(document.hidden&&G&&G.L&&mode!='title')save()});addEventListener('pagehide',()=>{if(G&&G.L&&mode!='title')save()});
function load(){JQ.length=0;try{if(WMAP&&localStorage.getItem('ltlc-map')!='2')return 0;const d=JSON.parse(localStorage.getItem(KEY));if(!d||!d.SS)return 0;if(d.divine)unlockWorld();if(d.xian)unlockWorld2();if(d.tang)genTangWorld(d.tang);d.SS.forEach((a,i)=>{if(S[i]){S[i].fac=a[0];S[i].own=a[1];S[i].gar=a[2];S[i].pool=a[3]}});delete d.SS;(d.VV||[]).forEach((a,i)=>{if(V[i]){V[i].own=a[0];V[i].pool=a[1];V[i].burn=a[2]}});delete d.VV;
 if(d.war)d.war=d.war.map(r=>typeof r=='string'?r.split('').map(Number):r);d.L.forEach(p=>{if(p.th==null)p.th=Math.random()*2;if(!p.t)p.t={inf:0,arc:0,cav:0};if(p.goP==null)p.goP=-1;if(p.goS==null)p.goS=-1;if(p.face==null)p.face=1;if(p.tx==null){p.tx=p.x;p.ty=p.y}if(p.dead==null)p.dead=0;if(p.to==null)p.to=-1;p.goS=p.goS>=0?S[p.goS]:null});d.L.forEach(p=>{p.goP=p.goP>=0?d.L[p.goP]:null});d.fights=d.fights||[];G=d;if(G.cmap&&!G.xw){G.xw=1;extraWar(G.F.map((f,i)=>i).filter(i=>G.F[i].race))}{const na=addConts();if(na){G.won=0;setTimeout(()=>toast(na>15?'🌊 CÁC CHÂU LỤC MỚI xuất hiện bên kia biển!':'💀 VÙNG ĐẤT CHẾT trỗi dậy ở tận cùng phía Đông!<br>Quân đoàn xương bất tử thù địch với mọi tộc<br><small>Chúng sẽ vượt biển xâm lược — hãy phòng thủ!</small>','#c58cff',1),1500)}}sanitize();if(G.cmap&&!G.split)splitDark();slim();mySlim();terr();MC.z=.7;MC.follow=1;rlog();return 1}catch(e){return 0}}
const clearSave=()=>{try{localStorage.removeItem(KEY)}catch(e){}};

/* ================= AI BẢN ĐỒ ================= */
function speed(p){const n=tot(p.t)||1;let s=p.kind=='bandit'?64:p.kind=='rf'?115:(54+p.t.cav/n*36)*(1-Math.min(.45,n/22000));if(p.kind=='pl')s*=1.2;return s*TSP[tAt(p.x,p.y)]}
const nearestOf=(a,p)=>a.slice().sort((x,y)=>dist(x,p)-dist(y,p))[0];
function think(p){if(p.inF)return;if(p.kind=='exile'){if(Math.hypot(p.tx-p.x,p.ty-p.y)<10){const h=p.home||p;p.tx=cl(h.x+rnd(-320,320),60,WW-60);p.ty=cl(h.y+rnd(-260,260),60,WH-60);if(hW(p.tx,p.ty)<.36){p.tx=p.x;p.ty=p.y}}return}const st=str(p.t);
 if(p.kind=='rf'){const o=G.L[p.to];if(!o||o.dead||o.fac!=p.fac){const own=S.filter(s=>s.fac==p.fac);if(!own.length){p.dead=-1;return}p.goP=null;p.goS=nearestOf(own,p)}else{p.goP=o;p.goS=null}return}
 if(p.kind=='bandit'){const v=G.L.find(e=>!e.dead&&e.kind!='bandit'&&e.kind!='pl'&&dist(e,p)<260&&str(e.t)*1.4<st);if(v){p.goP=v;return}
  if(p.goP&&(p.goP.dead||dist(p.goP,p)>400))p.goP=null;
  if(!p.goP&&(Math.hypot(p.tx-p.x,p.ty-p.y)<10||Math.random()<.08)){p.tx=cl(p.x+rnd(-300,300),100,WW-100);p.ty=cl(p.y+rnd(-300,300),100,WH-100)}return}
 const hv=G.tang&&p.kind=='lord'&&p.fac==P0().fac&&!G.call&&contOf(p.x,p.y)==12,own=hv?S.filter(s=>s.fac==p.fac&&s.race==12):S.filter(s=>s.fac==p.fac),mine=own.filter(s=>s.own===p.id),cap=rank(p)[1];
if(p.kind=='lord'&&isMyKing()&&p.fac==P0().fac&&!G.call){const pl=P0(),pc=contOf(pl.x,pl.y);if(contOf(p.x,p.y)!=pc&&!S.some(s=>s.own===p.id&&s.race==contOf(p.x,p.y))){const ts=S.filter(s=>s.fac==p.fac&&s.race==pc);if(ts.length){p.goP=null;p.goS=nearestOf(ts,p);return}}}
 const fh=G.fights.find(f=>(f.af==p.fac||f.df==p.fac)&&dist(f,p)<650);if(fh&&tot(p.t)>100){p.goP=null;p.goS=null;p.tx=fh.x;p.ty=fh.y;return}
 if(G.call&&p.kind=='lord'&&isMyKing()&&p.fac==P0().fac){const pl=P0();if(dist(p,pl)>80){p.goS=p.goP=null;p.tx=pl.x+rnd(-60,60);p.ty=pl.y+rnd(-60,60)}return}
 let prey=null;for(const e of G.L){if(e.dead||e===p||!atWar(p.fac,e.fac))continue;const d=dist(e,p);if(d>320)continue;const se=str(e.t);
  if(se>st*1.25&&e.kind!='rf'&&own.length){p.goP=null;p.goS=nearestOf(own,p);return}
  if(se*1.3<st&&!prey)prey=e}
 if(p.kind!='bandit'&&tot(p.t)>=Math.min(cap*.3,900)){const sa0=st+allies(p,420).reduce((a,q)=>a+str(q.t),0),nt=S.find(s=>atWar(p.fac,s.fac)&&dist(s,p)<650&&sa0>str(s.gar)*AGR(p));if(nt){p.goS=nt;p.goP=null;return}}
 if(prey&&(p.chase=(p.chase||0)+1)<6){p.goP=prey;p.goS=null;return}if(!prey)p.chase=0;
 if(p.goP&&(p.goP.dead||dist(p.goP,p)>480||p.chase>=6))p.goP=null;if(p.chase>=10)p.chase=0;
 if(p.goS&&p.goS.fac!=p.fac&&atWar(p.fac,p.goS.fac))return;
 if(tot(p.t)<Math.min(cap*.3,900)&&own.length){p.goS=nearestOf(mine.length?mine:own,p);return}
 const k=G.F[p.fac]&&G.L[G.F[p.fac].king];
 if(p.kind=='lord'&&k&&!k.dead&&k.goS&&atWar(p.fac,k.goS.fac)&&tot(p.t)>120){if(dist(p,k)>60){p.goP=null;p.goS=null;p.tx=k.x+rnd(-40,40);p.ty=k.y+rnd(-40,40)}return}
 const sa=st+allies(p,420).reduce((a,q)=>a+str(q.t),0);
 const tg=(p.kind=='lord'&&!hv&&Math.random()<.85)?null:S.filter(s=>OPEN(s.race)&&s.race==contOf(p.x,p.y)&&atWar(p.fac,s.fac)&&dist(s,p)<(hv?6000:p.kind=="king"?2200:1500)&&sa>str(s.gar)*AGR(p)).sort((a,b)=>dist(a,p)-dist(b,p))[0];
 if(tg){p.goS=tg;return}
 if(!p.goS&&Math.hypot(p.tx-p.x,p.ty-p.y)<10){const b=own.length?own[ri(0,own.length-1)]:p;p.tx=cl(b.x+rnd(-260,260),100,WW-100);p.ty=cl(b.y+rnd(-260,260),100,WH-100)}}
function move(p,dt){let tx=p.tx,ty=p.ty;
 if(p.kind=='pl'&&p.goP&&p.goP.inF&&p.goP.fac==p.fac){const id=p.goP.id,f=G.fights.find(f=>f.A.includes(id)||f.D.includes(id));if(f){p.goP=null;p.goF=f}}
 if(p.goV){const v=p.goV,d=dist(p,v);if(d<14){p.goV=null;p.tx=p.x;p.ty=p.y;villageMenu(v);return}const m=Math.min(d,speed(p)*dt);p.x+=(v.x-p.x)/d*m;p.y+=(v.y-p.y)/d*m;p.mv=1;p.face=v.x>p.x?1:-1;return}
 if(p.goF){if(!G.fights.includes(p.goF))p.goF=null;else{const f=p.goF,d=dist(p,f);if(d<34){p.goF=null;p.tx=p.x;p.ty=p.y;joinFight(f);return}const m=Math.min(d,speed(p)*dt);p.x+=(f.x-p.x)/d*m;p.y+=(f.y-p.y)/d*m;p.mv=1;return}}
 if(p.goP){if(p.goP.dead)p.goP=null;else{tx=p.goP.x;ty=p.goP.y}}
 if(p.goS){tx=p.goS.x;ty=p.goS.y+10}
 const dx=tx-p.x,dy=ty-p.y,d=Math.hypot(dx,dy);
 if(p.goS&&d<14){const s=p.goS;p.goS=null;p.tx=p.x;p.ty=p.y;p.mv=0;arrive(p,s);return}
 if(p.kind=='rf'&&p.goP&&d<16){add(p.goP.t,p.t);if(p.goP.kind=='pl'){RFS+=tot(p.t);clearTimeout(RFT);RFT=setTimeout(()=>{toast(`➕ ${fmt(RFS)} viện binh đã nhập quân của bạn!`,'#9cf');RFS=0},900)}p.dead=-1;return}
 if(d<2){p.mv=0;return}const m=Math.min(d,speed(p)*dt);p.x+=dx/d*m;p.y+=dy/d*m;p.face=dx>0?1:-1;p.mv=1}
function sCfg(s){const pl=P0();return{A:[pl,...near(pl,AR(),pl.fac)],D:G.L.filter(q=>!q.dead&&!q.inF&&q.fac==s.fac&&q.kind!='rf'&&q.kind!='pl'&&dist(q,s)<150),s,gar:'D',wall:1}}
function powOf(cfg,sd){return str(comb(srcs(cfg,sd)))*(sd=='D'&&cfg.wall?1.5:1)}
function autoFight(cfg){const pl=P0(),a=powOf(cfg,'A'),d=powOf(cfg,'D');if(a>=d*1.1||cfg.fight&&a>=d*.8)quick(cfg);else if(cfg.fight){pl.safe=3;G.acSkip=cfg.fight}else{retreat(cfg);toast('🤖 Địch quá mạnh — tự rút lui','#fc8')}}
function mot(t,h,b){if(G.ac){toast(t+(h?'<br><small>'+h.replace(/<\/p><p>/g,' · ').replace(/<[^>]+>/g,'')+'</small>':''),'#ffd77a');paused=false;return}menu(t,h,b)}
function acRecruit(s){const pl=P0(),room=Math.max(0,rank(pl)[1]-tot(pl.t)),n=Math.min(s.pool,room,Math.floor(Math.max(0,G.gold-500)/COST.inf));if(n>0){G.gold-=n*COST.inf;s.pool-=n;pl.t.inf+=n;toast(`🤖 Chiêu ${fmt(n)} bộ binh tại ${s.name}`,'#9cf')}}
function acTick(){const pl=P0();if(!G.ac||paused||mode!='map'||pl.goS||pl.goF||pl.goV||pl.goP||pl.inF)return;if(Math.hypot(pl.tx-pl.x,pl.ty-pl.y)>3)return;
 const cap=rank(pl)[1],own=S.filter(s=>s.fac==pl.fac&&WRLD(s.y)==WRLD(pl.y));
 if(tot(pl.t)<cap*.35&&own.length){const s=nearestOf(own.filter(s=>s.pool>50).length?own.filter(s=>s.pool>50):own,pl);if(dist(s,pl)<20){acRecruit(s);if(tot(pl.t)<cap*.35){G.acW=(G.acW||0)+1;if(G.acW<8)return}}else{pl.goS=s;return}}
 G.acW=0;const A=[pl,...near(pl,AR(),pl.fac)];let my=0;for(const p of A)my+=str(p.t);
 const tg=S.filter(s=>s.fac!=pl.fac&&atWar(pl.fac,s.fac)&&OPEN(s.race)&&WRLD(s.y)==WRLD(pl.y)&&str(s.gar)*1.5*1.15<my).map(s=>[s,dist(s,pl)]).sort((a,b)=>a[1]-b[1])[0];
 const fg=G.fights.filter(f=>f!==G.acSkip&&(f.af==pl.fac||f.df==pl.fac)&&WRLD(f.y)==WRLD(pl.y)&&dist(f,pl)<1800).sort((a,b)=>dist(a,pl)-dist(b,pl))[0];
 if(fg){pl.goF=fg;if(G.acT!=='f'+fg.x){G.acT='f'+fg.x;toast('🤖 Tới hỗ trợ trận đánh của phe ta','#9cf')}return}
 if(tg&&tg[1]>5000){const c=own.map(s=>[s,dist(s,tg[0])]).sort((a,b)=>a[1]-b[1])[0];if(c&&c[1]<tg[1]-3000&&dist(c[0],pl)>200){const k=tpCost(c[0]);if(G.gold>=k.g+2000){toast(`🤖 Dịch chuyển tới ${c[0].name} để đánh ${tg[0].name}`,'#9ff0ff');tpGo(c[0]);return}}}
 if(tg){pl.goS=tg[0];if(G.acT!=tg[0].id){G.acT=tg[0].id;toast(`🤖 Tiến quân tới ${tg[0].name} (${facN(tg[0].fac)})`,'#9cf')}return}
 const pc=contOf(pl.x,pl.y),ep=G.L.filter(q=>!q.dead&&!q.inF&&q.kind!='rf'&&q.kind!='pl'&&q.kind!='exile'&&atWar(pl.fac,q.fac)&&contOf(q.x,q.y)==pc&&str(q.t)*1.05<my&&dist(q,pl)<4000).sort((a,b)=>dist(a,pl)-dist(b,pl))[0];
 if(ep){pl.goP=ep;if(G.acT!=='p'+ep.id){G.acT='p'+ep.id;toast(`🤖 Truy kích ${ep.kind=='bandit'?'thổ phỉ':pname(ep)}`,'#9cf')}return}
 if(tot(pl.t)<cap*.9&&own.length){const s=nearestOf(own,pl);if(dist(s,pl)>20){pl.goS=s;return}acRecruit(s)}
 if((G.acN=(G.acN||0)+1)%20==1)toast('🤖 Chưa có thành địch nào đủ sức chiếm — đang chờ thêm quân','#fc8')}
function acBtn(){const e=$('#zAc');if(e){e.style.background=G&&G.ac?'#2f7d3a':'';e.title='Tự chinh phạt'}}
function acToggle(){G.ac=!G.ac;G.acT=-1;const pl=P0();if(G.ac){pl.goS=pl.goP=pl.goF=pl.goV=null;pl.tx=pl.x;pl.ty=pl.y}acBtn();toast(G.ac?'🤖 TỰ CHINH PHẠT: BẬT — tự đi chiếm thành địch, tự đánh, yếu thì về thành bổ sung quân. Chạm bản đồ để tự điều khiển lại.':'🤖 Tự chinh phạt: TẮT','#7dff8a')}
function arrive(p,s){if(p.kind=='pl'){if(G.ac){if(s.fac==p.fac){acRecruit(s);return}if(atWar(p.fac,s.fac)&&tot(p.t)){autoFight(sCfg(s));return}}townMenu(s);return}
 if(p.kind=='rf'){if(s.fac==p.fac)add(s.gar,p.t);p.dead=-1;return}
 if(s.fac==p.fac){const n=Math.min(s.pool,Math.max(0,rank(p)[1]-tot(p.t)));if(n>0){s.pool-=n;add(p.t,mix(n))}
  if(tot(s.gar)<[300,200,120][s.type]&&tot(p.t)>300)add(s.gar,take(p.t,100));return}
 if(!atWar(p.fac,s.fac))return;const f=G.fights.find(f=>f.s==s.id);if(f){if(f.af==p.fac){f.A.push(p.id);p.inF=1}return}startFight(p,null,s)}
function capture(s,p){const old=s.fac,pl=P0(),me=p.kind=='pl';s.fac=p.fac;s.own=p.id;V.forEach(v=>{if(v.p==s.id){if(v.own===0&&!me)toast(`💔 Mất đất phong ${v.name}`,'#ff6a5a');v.own=p.id}});s.gar=take(p.t,Math.ceil(tot(p.t)*.25));s.pool=Math.floor(s.pool/2);
 if(me)toast(`🏰 Bạn chiếm được <b>${s.name}</b>! Đây là lãnh địa riêng của bạn.`,'#7dff8a');
 else if(p.fac==pl.fac)toast(`🏰 ${pname(p)} chiếm ${s.name} cho phe ta`,'#7dff8a');
 else if(old==pl.fac)toast(`💔 Phe ta mất ${s.name} vào tay ${facN(p.fac)}`,'#ff6a5a');
 if(me||p.fac==pl.fac||old==pl.fac||Math.random()<.25)addLog(`${me?'Bạn':pname(p)} (${facN(p.fac)}) chiếm ${s.name} từ ${facN(old)}`,p.fac==pl.fac?'#8f8':old==pl.fac?'#f77':'#ccc');
 if(!S.some(x=>x.fac==old)&&old>=0&&!G.F[old].dead){G.F[old].dead=1;addLog(`👑 ${facN(old)} đã diệt vong!`,'#ffd77a');toast(`☠ ${facN(old)} đã diệt vong!`,'#ffd77a');G.L.forEach(q=>{if(q.fac==old&&q.kind!='pl')q.dead=-1});
  const of=G.F[old];of.heirs=of.heirs==null?ri(1,4):of.heirs;G.war[old].fill(0);G.war.forEach(r=>r[old]=0);
  if(G.L.filter(q=>q.kind=='exile'&&!q.dead).length<14){const n=Math.max(2,of.heirs+1),e=pushP({kind:'exile',name:newName(of),fac:old,x:s.x+rnd(-60,60),y:s.y+rnd(40,80),t:mix(ri(80,320)),ord:n});e.home={x:s.x,y:s.y};
   const m=`🥀 ${e.name} — con trai ${ordN(n)} ${of.race?'hoàng tộc '+of.sur:'hoàng tộc họ '+of.sur} — lưu lạc sau khi ${of.n} vong quốc.`;addLog(m,'#c9a8e0');if(contOf(s.x,s.y)==ACT)toast(m+(isMyKing()?'<br><small>Chạm vào hoàng tử để chiêu nạp làm tướng</small>':''),'#c9a8e0')}}
 for(const f of G.F)if(f.emp&&S.some(x=>x.cn==f.cn&&G.F[x.fac]!==f))f.emp=0;
 const of=G.F[p.fac];if(of&&!of.emp&&S.filter(x=>x.cn==of.cn).every(x=>x.fac==p.fac)){of.emp=1;addLog(`🐉 ${of.n} thống nhất ${CC[of.cn].n}, vua lên ngôi Hoàng đế!`,'#ffd65a');toast(`🐉 ${of.n} thống nhất ${CC[of.cn].n} — lên ngôi Hoàng đế!`,'#ffd65a',1)}
 terr();if(me)checkRank();
 if(G.F.every((f,i)=>i==pl.fac||!S.some(x=>x.fac==i))&&!G.won){G.won=1;menu('👑 Nhất thống thiên hạ!',`<p>Sau ${G.day} ngày, ${facN(pl.fac)} làm chủ toàn bộ ${S.length} thành trì.</p>`,[['Tiếp tục',close]])}}
function defeat(p){p.t=Z3();p.goS=p.goP=null;p.inF=0;if(p.kind=='pl'){playerDown();return}
 if(p.kind=='rf'){p.dead=-1;return}p.dead=p.kind=='bandit'?rnd(20,40):S.some(s=>s.fac==p.fac)?rnd(12,22):-1}
/* ---- trận đánh giữa các đạo quân máy: kéo dài theo thời gian, đồng minh gần đó tự nhập trận ---- */
function startFight(a,b,s){const f={x:s?s.x:(a.x+b.x)/2,y:s?s.y+12:(a.y+b.y)/2,A:[a.id],D:b?[b.id]:[],s:s?s.id:-1,t:0,r:1,af:a.fac,df:s?s.fac:b.fac,n0:0};
 a.inF=1;if(b)b.inF=1;G.fights.push(f);joinNear(f);const pl=P0();
 if(!s&&dist(pl,f)<600&&(f.af==pl.fac||f.df==pl.fac))toast(`⚔ ${s?'Vây thành '+s.name:'Giao tranh'} gần bạn: ${facN(f.af)} đánh ${facN(f.df)}<br><small>Chạm biểu tượng ⚔ trên bản đồ để tham chiến</small>`,'#ff9a5a');
 else if(s&&s.fac==pl.fac)toast(`🏰 ${s.name} của phe ta đang bị ${facN(f.af)} vây!${dist(pl,f)<900?'<br><small>Chạm ⚔ trên bản đồ để cứu viện</small>':''}`,'#ff6a5a')}
function joinNear(f){for(const q of G.L){if(q.dead||q.inF||q.kind=='pl'||q.kind=='rf'||q.fac<0||dist(q,f)>230)continue;if(q.fac==f.af){f.A.push(q.id);q.inF=1}else if(q.fac==f.df){f.D.push(q.id);q.inF=1}}}
const mem=ids=>ids.map(i=>G.L[i]).filter(p=>p&&!p.dead&&tot(p.t)>0);
function fightPow(f){const A=mem(f.A),D=mem(f.D),s=f.s>=0?S[f.s]:null;return{A,D,s,ta:A.reduce((a,p)=>a+tot(p.t),0),td:D.reduce((a,p)=>a+tot(p.t),0)+(s?tot(s.gar):0),sa:A.reduce((a,p)=>a+str(p.t),0),sd:D.reduce((a,p)=>a+str(p.t),0)+(s?str(s.gar)*((G.F[s.fac]&&G.F[s.fac].race==4&&G.F[f.af]&&G.F[f.af].race==4)?1.15:1.8):0)}}
function spread(l,n){const T=l.reduce((a,t)=>a+tot(t),0);if(!T)return;for(const t of l)kill(t,Math.round(n*tot(t)/T))}
function upFights(dt){for(let i=G.fights.length-1;i>=0;i--){const f=G.fights[i];f.t+=dt;f.r-=dt;const P=fightPow(f);
 for(const p of P.A){p.x+=(f.x-16-p.x)*Math.min(1,dt*2);p.y+=(f.y-p.y)*Math.min(1,dt*2);p.mv=1;p.face=1}for(const p of P.D){p.x+=(f.x+16-p.x)*Math.min(1,dt*2);p.y+=(f.y-p.y)*Math.min(1,dt*2);p.mv=1;p.face=-1}
 if(f.r>0)continue;f.r=1;joinNear(f);if(!f.n0)f.n0=P.ta+P.td;
 spread(P.D.map(p=>p.t).concat(P.s?[P.s.gar]:[]),Math.max(1,Math.round(P.sa*rnd(.012,.024))));spread(P.A.map(p=>p.t),Math.max(1,Math.round(P.sd*rnd(.012,.024))));
 const Q=fightPow(f);let res=null;if(!Q.ta||(Q.sd>Q.sa*6&&f.t>12))res='D';else if(!Q.td||(Q.sa>Q.sd*6&&f.t>12))res='A';else if(f.t>70)res=Q.sa>Q.sd?'A':'D';
 if(res){G.fights.splice(i,1);endFight(f,res)}}}
function endFight(f,res){const P=fightPow(f),W=res=='A'?P.A:P.D,L=res=='A'?P.D:P.A,pl=P0(),s=P.s;
 for(const id of[...f.A,...f.D]){const p=G.L[id];if(p){p.inF=0;p.safe=3;if(!p.dead&&!tot(p.t))defeat(p)}}
 const lead=W[0];if(lead)lead.ren=(lead.ren||0)+Math.max(0,f.n0-P.ta-P.td)/6;
 L.forEach(p=>{if(!p.dead)defeat(p)});
 if(s&&res=='A'&&lead)capture(s,lead);
 else if(s&&res=='D'&&s.fac==pl.fac)toast(`🛡 ${s.name} đã đẩy lui quân vây thành!`,'#7dff8a');
 else if(!s&&(f.af==pl.fac||f.df==pl.fac)){const wf=res=='A'?f.af:f.df;addLog(`${wf==pl.fac?'Quân ta':facN(wf)} thắng một trận (${fmt(f.n0)} quân tham chiến)`,wf==pl.fac?'#8f8':'#f99')}}
const allies=(p,r)=>G.L.filter(q=>q!==p&&!q.dead&&!q.inF&&q.fac==p.fac&&(q.kind=='lord'||q.kind=='king')&&dist(q,p)<r);
function incoming(o){let n=0;for(const p of G.L)if(p.kind=='rf'&&!p.dead&&p.to===o.id)n+=tot(p.t);return n}
const myGarT=s=>(G.xian?[15000,10000,6000]:[6000,4000,2500])[s.type]*PW(s.race);
