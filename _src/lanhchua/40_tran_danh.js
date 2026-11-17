function startBattle(cfg){const pl=P0();close();mode='battle';stopPl();
 const la=srcs(cfg,'A'),ld=srcs(cfg,'D'),A=comb(la),D=comb(ld),s=cfg.wall?cfg.s:null,e=null,n0=tot(A),n1=tot(D);
 const rc=[raceOf(pl),cfg.D.length?raceOf(cfg.D[0]):(G.F[cfg.s.fac]&&G.F[cfg.s.fac].race)||0];
 const dvb=rc[0]>=5||rc[1]>=5||!!G.divine,wOf=n=>Math.max(1,Math.ceil(n/(G.divine?(ULQ?70:LOWQ?160:300):(ULQ?280:LOWQ?700:1500)*(dvb?.5:1)))),w0=wOf(n0),w1=wOf(n1),nu=(t,w)=>KS.reduce((a,k)=>a+Math.ceil(t[k]/w),0),u0=nu(A,w0),u1=nu(D,w1),N=u0+u1;
 const sp0=SP*Math.sqrt(w0),sp1=SP*Math.sqrt(w1),rows=n=>cl(Math.ceil(Math.sqrt(n*1.6)),10,200),R0=rows(u0),R1=rows(u1);
 const d0=Math.ceil(u0/R0)*sp0,d1=Math.ceil(u1/R1)*sp1,gap=s?560:440,FH=Math.max(440,Math.max(R0*sp0,R1*sp1)+220),f0=170+d0,f1=f0+gap,FW=f1+d1+170;
 B={cfg,e,s,FW,FH,N,rc,t:0,acc:0,tick:0,spd:1,order:'hold',done:0,x:new Float32Array(N),y:new Float32Array(N),hp:new Float32Array(N),uh:new Float32Array(N),sz:new Float32Array(N),wt:new Uint16Array(N),cd:new Float32Array(N),an:new Float32Array(N),
  ty:new Uint8Array(N),sd:new Uint8Array(N),al:new Uint8Array(N),tg:new Int32Array(N).fill(-1),fc:new Int8Array(N),cnt:[[0,0,0],[0,0,0]],ac:[[0,0,0],[0,0,0]],ar:[],w:[w0,w1],
  wall:s?{x:f1-34,hp:2500*Math.max(1,w1),mh:2500*Math.max(1,w1)}:null,src:[la,ld],init:[{...A},{...D}],lost0:tot(pl.t),d0:n1,hc:0,sc:0,snd:0,dr:0,gx:Math.ceil(FW/20)+1,gy:Math.ceil(FH/20)+1,lst:[[],[]],cols:['#4aa3ff','#ff5040']};
 B.head=new Int32Array(B.gx*B.gy);B.nx=new Int32Array(N);
 B.cp=document.createElement('canvas');B.cp.width=Math.ceil(FW/2);B.cp.height=Math.ceil(FH/2);B.cpx=B.cp.getContext('2d');
 let i=0;const place=(t,side,front,dir,Rr,w,sp)=>{let k=0;const st=RACE[rc[side]].st;for(let ty=0;ty<3;ty++){const c=t[KS[ty]];B.cnt[side][ty]=c;const nn=Math.ceil(c/w);
  for(let j=0;j<nn;j++,k++,i++){const wt=Math.floor(c/nn)+(j<c%nn?1:0),col=k/Rr|0,row=k%Rr;B.x[i]=front-dir*col*sp+rnd(-1.5,1.5);B.y[i]=FH/2+(row-(Rr-1)/2)*sp+rnd(-1.5,1.5);
   B.ty[i]=ty;B.sd[i]=side;B.uh[i]=UT[ty].hp*st.hp;B.hp[i]=B.uh[i]*wt;B.wt[i]=wt;B.sz[i]=Math.min(G.divine?14:dvb?7:4.5,G.divine?Math.sqrt(wt)*.9:Math.sqrt(wt));B.al[i]=1;B.cd[i]=Math.random();B.fc[i]=dir;B.an[i]=Math.random()*6}}};
 place(A,0,f0,1,R0,w0,sp0);place(D,1,f1,-1,R1,w1,sp1);{let mx=1;for(let q=0;q<N;q++)if(B.sz[q]>mx)mx=B.sz[q];B.mxs=mx}
 BC.z=Math.min(W/FW,(H-100)/FH);BC.x=FW/2;BC.y=FH/2;B.zf=BC.z;
 $('#top').style.display='none';$('#log').style.display='none';$('#bbar').style.display='flex';$('#binfo').style.display='block';B.spd=BSPD;setOrder(BAUTO?'charge':'hold');$('#bSpd').textContent='⏩ x'+B.spd;$('#bAuto').classList.toggle('on',BAUTO);SFX.horn();
 if(w0>1||w1>1)toast(`⚔ Quân quá đông: mỗi lính khổng lồ = nhiều lính (ta ×${w0}, địch ×${w1}) — số quân vẫn tính đủ`,'#ffd77a',0)}
function setOrder(o){B.order=o;document.querySelectorAll('#bbar [data-o]').forEach(b=>b.classList.toggle('on',b.dataset.o==o))}
function gnear(px,py,s,r){const b=B,gx=b.gx,gy=b.gy,ci=px/20|0,cj=py/20|0;let best=-1,bd=1e12;
 for(let j=Math.max(0,cj-r);j<=Math.min(gy-1,cj+r);j++)for(let k=Math.max(0,ci-r);k<=Math.min(gx-1,ci+r);k++){let u=b.head[j*gx+k];
  while(u>=0){if(b.sd[u]!=s&&b.al[u]){const dd=(b.x[u]-px)**2+(b.y[u]-py)**2;if(dd<bd){bd=dd;best=u}}u=b.nx[u]}}return best}
function samp(i){const L=B.lst[1-B.sd[i]];if(!L.length)return -1;let best=-1,bd=1e12;for(let k=0;k<10;k++){const u=L[Math.random()*L.length|0];if(!B.al[u])continue;const dd=(B.x[u]-B.x[i])**2+(B.y[u]-B.y[i])**2;if(dd<bd){bd=dd;best=u}}return best}
function hitU(t,dmg){const b=B;if(b.wall&&b.wall.hp>0&&b.sd[t]==1)dmg*=.6;b.hp[t]-=dmg*rnd(.8,1.2);b.hc++;
 if(b.hp[t]<=0&&b.al[t]){b.al[t]=0;const z=b.sz[t];b.cpx.fillStyle=b.sd[t]?'rgba(90,30,30,.55)':'rgba(60,40,30,.55)';b.cpx.fillRect(b.x[t]/2-1.2*z,b.y[t]/2-.5*z,2.4*z,1.1*z)}}
function tickB(dt){const b=B,N=b.N,{x,y,hp,uh,sz,cd,ty,sd,al,tg,fc,an,head,nx}=b,gx=b.gx;b.t+=dt;b.tick++;
 head.fill(-1);const ac=[[0,0,0],[0,0,0]];
 for(let i=0;i<N;i++){if(!al[i])continue;const c=(y[i]/20|0)*gx+(x[i]/20|0);nx[i]=head[c];head[c]=i;ac[sd[i]][ty[i]]+=Math.ceil(hp[i]/uh[i])}
 b.ac=ac;const a0=ac[0][0]+ac[0][1]+ac[0][2],a1=ac[1][0]+ac[1][1]+ac[1][2];
 if(!a0||!a1||b.t>900){endBattle(a0>0&&(!a1||a0>a1*(b.s?1.5:1)),0);return}
 if(b.tick%10==1){b.lst=[[],[]];for(let i=0;i<N;i++)if(al[i])b.lst[sd[i]].push(i)}
 const wu=b.wall&&b.wall.hp>0,wx=wu?b.wall.x:0,ST=[RACE[b.rc[0]].st,RACE[b.rc[1]].st];
 for(let i=0;i<N;i++){if(!al[i])continue;const s=sd[i],U=UT[ty[i]],st=ST[s],na=Math.ceil(hp[i]/uh[i]);cd[i]-=dt;
  if((b.tick+i)%6==0){const n=gnear(x[i],y[i],s,2);if(n>=0)tg[i]=n;else if(tg[i]<0||!al[tg[i]]||(b.tick+i)%30==0)tg[i]=samp(i)}
  let t=tg[i];if(t>=0&&!al[t])t=tg[i]=samp(i);if(t<0)continue;
  const dx=x[t]-x[i],dy=y[t]-y[i],d=Math.hypot(dx,dy)||1,rg=U.rng*st.rng;fc[i]=dx>0?1:-1;
  const hold=s==0&&b.order=='hold'&&d>(ty[i]==1?rg:150);let mv=0;
  if(ty[i]==1){if(d<=rg){if(cd[i]<=0&&b.ar.length<8000){b.sc++;b.ar.push(x[i],y[i]-8*sz[i],x[t]+rnd(-10,10),y[t]+rnd(-7,7),0,.3+d/450,s,U.atk*st.atk*na);cd[i]=U.cd*rnd(.8,1.3)}}else if(!hold)mv=1}
  else if(d<=U.rng+3*(sz[i]+sz[t])+(wu?9:0)){if(cd[i]<=0){hitU(t,U.atk*st.atk*na);cd[i]=U.cd*rnd(.8,1.2)}}
  else if(wu&&s==0&&x[i]>=wx-11-3*sz[i]&&x[t]>wx){if(cd[i]<=0){b.wall.hp-=U.atk*na;cd[i]=U.cd}}
  else if(!hold)mv=1;
  if(mv){const m=U.sp*st.sp*dt;x[i]+=dx/d*m;y[i]+=dy/d*m;an[i]+=dt*9/Math.sqrt(sz[i])}}
 for(let i=0;i<N;i++){if(!al[i])continue;const ci=x[i]/20|0,cj=y[i]/20|0;
  for(let j=Math.max(0,cj-1);j<=Math.min(b.gy-1,cj+1);j++)for(let k=Math.max(0,ci-1);k<=Math.min(gx-1,ci+1);k++){let u=head[j*gx+k];
   while(u>=0){if(u>i&&al[u]){const ddx=x[u]-x[i],ddy=y[u]-y[i],q=ddx*ddx+ddy*ddy,rr=3*(sz[i]+sz[u]);if(q<rr*rr&&q>1e-4){const dd=Math.sqrt(q),p=(rr-dd)/2/dd*.8;x[i]-=ddx*p;y[i]-=ddy*p;x[u]+=ddx*p;y[u]+=ddy*p}}u=nx[u]}}}
 for(let i=0;i<N;i++){if(!al[i])continue;x[i]=cl(x[i],6,b.FW-6);y[i]=cl(y[i],14,b.FH-6);if(wu)x[i]=sd[i]==0?Math.min(x[i],wx-9-2*sz[i]):Math.max(x[i],wx+9+2*sz[i])}
 const A=b.ar;let w=0;for(let k=0;k<A.length;k+=8){A[k+4]+=dt;if(A[k+4]>=A[k+5]){const u=gnear(A[k+2],A[k+3],A[k+6],1);if(u>=0){const r=10+6*b.sz[u];if((b.x[u]-A[k+2])**2+(b.y[u]-A[k+3])**2<r*r)hitU(u,A[k+7])}}else{for(let q=0;q<8;q++)A[w+q]=A[k+q];w+=8}}A.length=w}
function upBattle(dt){if(!B||B.done)return;B.acc+=dt;let n=0;while(B&&!B.done&&B.acc>=.05&&n<5){B.acc-=.05;tickB(.05);n++}if(B&&n==5)B.acc=0;
 if(!B)return;B.snd-=dt;if(B.snd<=0){B.snd=.14;if(B.hc)SFX.clash();if(B.sc&&Math.random()<.6)SFX.arrow();B.hc=B.sc=0}B.dr-=dt;if(B.dr<=0){B.dr=.85;SFX.drum()}
 const ac=B.ac,s=a=>a[0]+a[1]+a[2];
 $('#bInfoT').innerHTML=`<span style="color:#7cc4ff">Ta ${fmt(s(ac[0]))}</span> (🗡${fmt(ac[0][0])} 🏹${fmt(ac[0][1])} 🐎${fmt(ac[0][2])}) ⚔ <span style="color:#ff8a7a">Địch ${fmt(s(ac[1]))}</span> (🗡${fmt(ac[1][0])} 🏹${fmt(ac[1][1])} 🐎${fmt(ac[1][2])})${B.w[0]>1||B.w[1]>1?` · 🗿 lính khổng lồ ta ×${B.w[0]} địch ×${B.w[1]}`:''}${B.wall?` · Tường ${Math.max(0,B.wall.hp|0)}`:''}${B.t<8&&B.order=='hold'?'<br>Bấm ⚔ Xung phong để tấn công · kéo/chụm để xem':''}`}
function endBattle(win,ret){if(!B||B.done)return;B.done=1;const pl=P0(),b=B;
 for(let s=0;s<2;s++){const ac=Z3();for(let i=0;i<b.N;i++)if(b.al[i]&&b.sd[i]==s)ac[KS[b.ty[i]]]+=Math.ceil(b.hp[i]/b.uh[i]);distrib(b.src[s],b.init[s],ac)}
 const lost=b.lost0-tot(pl.t),kills=b.d0-tot(comb(b.src[1]));B=null;mode='map';
 $('#top').style.display='flex';$('#log').style.display='block';$('#bbar').style.display='none';$('#binfo').style.display='none';finish(win,b.cfg,ret,lost,kills);TQ.splice(0).forEach((q,i)=>setTimeout(()=>toast(...q),600+i*1800))}
document.querySelectorAll('#bbar [data-o]').forEach(b=>b.onclick=()=>B&&setOrder(b.dataset.o));
let BSPD=+(localStorage.getItem('ltlc-spd')||4)||4,BAUTO=localStorage.getItem('ltlc-auto')!='0';
$('#bSpd').onclick=()=>{if(!B)return;B.spd=B.spd==1?2:B.spd==2?4:1;BSPD=B.spd;try{localStorage.setItem('ltlc-spd',BSPD)}catch(e){}$('#bSpd').textContent='⏩ x'+B.spd};
$('#bAuto').onclick=()=>{BAUTO=!BAUTO;try{localStorage.setItem('ltlc-auto',BAUTO?'1':'0')}catch(e){}$('#bAuto').classList.toggle('on',BAUTO);if(B&&BAUTO){setOrder('charge');B.spd=Math.max(B.spd,4);BSPD=B.spd;$('#bSpd').textContent='⏩ x'+B.spd}};
$('#bSkip').onclick=()=>{if(!B||B.skip)return;B.skip=1;setOrder('charge');$('#bSkip').textContent='⏳ Đang tính...';const run=()=>{let n=0;while(B&&!B.done&&n<150){tickB(.05);n++}if(B&&!B.done)setTimeout(run,0);else $('#bSkip').textContent='⏭ Xem kết quả'};setTimeout(run,30)};
$('#bRet').onclick=()=>B&&endBattle(0,1);
function drawBattle(t){const b=B,z=BC.z;X.setTransform(DPR,0,0,DPR,0,0);X.fillStyle='#2c4420';X.fillRect(0,0,W,H);
 BC.x=cl(BC.x,0,b.FW);BC.y=cl(BC.y,0,b.FH);
 X.setTransform(DPR*z,0,0,DPR*z,DPR*(W/2-BC.x*z),DPR*(H/2-BC.y*z));
 X.fillStyle=X.createPattern(GT,'repeat');X.fillRect(0,0,b.FW,b.FH);{const tc=b.rc.includes(7)?'rgba(90,20,10,.5)':b.rc.includes(4)?'rgba(60,40,50,.55)':b.rc.includes(6)?'rgba(255,250,220,.25)':b.rc.includes(5)?'rgba(120,100,70,.3)':b.rc.includes(8)?'rgba(10,60,30,.3)':0;if(tc){X.fillStyle=tc;X.fillRect(0,0,b.FW,b.FH)}}X.drawImage(b.cp,0,0,b.FW,b.FH);
 const vx0=BC.x-W/2/z-10,vx1=BC.x+W/2/z+10,vy0=BC.y-H/2/z-10,vy1=BC.y+H/2/z+20;
 if(b.wall){const w=b.wall,s=b.s;X.fillStyle='rgba(150,135,100,.4)';X.fillRect(w.x,0,b.FW-w.x,b.FH);
  for(let y=40;y<b.FH;y+=150){const hx=w.x+120+(y/150%2)*70;X.fillStyle='#dccca6';X.fillRect(hx-22,y-6,44,20);X.fillStyle='#9a4a2a';TRI(X,hx-26,y-6,hx+26,y-6,hx,y-24)}
  if(w.hp>0){X.fillStyle='rgba(0,0,0,.3)';X.fillRect(w.x+8,0,8,b.FH);X.fillStyle='#b4a990';X.fillRect(w.x-8,0,16,b.FH);X.fillStyle='#8f856f';X.fillRect(w.x+2,0,6,b.FH);
   X.fillStyle='#d2c8b0';for(let y=0;y<b.FH;y+=14)X.fillRect(w.x-10,y,6,8);
   for(let y=60;y<b.FH;y+=180){X.fillStyle='#a69b82';X.fillRect(w.x-16,y-20,32,40);X.fillStyle=facC(s.fac);TRI(X,w.x-18,y-20,w.x+18,y-20,w.x,y-40)}}
  else{X.fillStyle='#8f856f';for(let i=0;i<b.FH/8;i++)X.fillRect(w.x-14+((i*37)%28),(i*97)%b.FH,10,7)}}
 const lo=z*(b.mxs||1)<(ULQ?1.2:.5),lw=lo?Math.max(1.4,1.6/z):1.3,LS=Math.max(1,.6/z);
 const HC=['#151515','#151515','#151515','#2a2a2a','#ece7da','#8d939b','#f6e3c8','#b3261e','#e0802a','#f0d2b0','#f0d2b0','#e8d0e8'],BODY=['#121212','#121212','#121212','#121212','#e6e0d0','#5c6168','#f3ead2','#2a0606','#3a2410','#dfe9ff','#fff0c0','#3a1450'];
 for(let s=0;s<2;s++){const{x,y,al,sd,ty,fc,an,sz}=b,rc=b.rc[s],hf=RACE[rc].st.h,col=b.cols[s],U=[];
  for(let i=0;i<b.N;i++){if(!al[i]||sd[i]!=s)continue;const px=x[i],py=y[i],k=sz[i];if(px<vx0-20*k||px>vx1+20*k||py<vy0||py>vy1+20*k)continue;U.push(i)}
  if(lo){X.beginPath();for(const i of U){const k=sz[i];X.rect(x[i]-lw*k/2,y[i]-lw*2.6*k*hf,lw*k,lw*2.6*k*hf)}X.fillStyle=col;X.fill();
   X.beginPath();for(const i of U){const k=sz[i];X.rect(x[i]-lw*k/2,y[i]-lw*3.4*k*hf,lw*k,lw*.9*k)}X.fillStyle='#111';X.fill();continue}
  const P=(f)=>{X.beginPath();for(const i of U)f(i,x[i],y[i],sz[i],sz[i]*hf,fc[i],Math.sin(an[i])*2*sz[i])};
  X.lineCap='round';X.lineJoin='round';
  // ngựa
  P((i,px,py,k,v,f,sw)=>{if(ty[i]!=2)return;X.moveTo(px-5*k,py-5*k);X.lineTo(px+4*k,py-5*k);X.moveTo(px-4*k+sw*.4,py);X.lineTo(px-4*k,py-5*k);X.moveTo(px+3.5*k-sw*.4,py);X.lineTo(px+3.5*k,py-5*k);X.moveTo(px+4*k*f,py-5*k);X.lineTo(px+7*k*f,py-8.5*k);X.moveTo(px-5*k*f,py-5*k);X.lineTo(px-7*k*f,py-3*k)});
  X.strokeStyle='#5a3b22';X.lineWidth=2.6*LS;X.stroke();
  // thân người que (đen)
  P((i,px,py,k,v,f,sw)=>{const by=ty[i]==2?py-5*k:py;
   if(ty[i]!=2){X.moveTo(px-2*k+sw*.5,by);X.lineTo(px,by-3.5*v);X.lineTo(px+2*k-sw*.5,by)}
   X.moveTo(px,by-3.5*v);X.lineTo(px,by-7.5*v);
   X.moveTo(px,by-6.6*v);X.lineTo(px+3*k*f,by-5*v);X.moveTo(px,by-6.6*v);X.lineTo(px-2*k*f,by-4.6*v)});
  X.strokeStyle=BODY[rc]||RACE[rc].bd||'#222';X.lineWidth=1.6*LS;X.stroke();
  // vũ khí
  P((i,px,py,k,v,f)=>{const by=ty[i]==2?py-5*k:py;
   if(ty[i]==0){if(rc==3){X.moveTo(px+3*k*f,by-5*v);X.lineTo(px+5*k*f,by-6.5*v);X.moveTo(px+3*k*f,by-5*v);X.lineTo(px+5.3*k*f,by-4.6*v)}
    else if(rc==1){X.moveTo(px+3*k*f,by-4*v);X.lineTo(px+3*k*f,by-11*v)}else{X.moveTo(px+2.6*k*f,by-4.6*v);X.lineTo(px+7.5*k*f,by-11*v)}}
   else if(ty[i]==2){X.moveTo(px-2*k*f,by-4.2*v);X.lineTo(px+11*k*f,by-8*v)}});
  X.strokeStyle='#d8dde4';X.lineWidth=1.3*LS;X.stroke();
  P((i,px,py,k,v,f)=>{if(ty[i]!=1)return;X.moveTo(px+3*k*f,(py)-9*v);X.quadraticCurveTo(px+6.5*k*f,(py)-5.5*v,px+3*k*f,(py)-2*v)});
  X.strokeStyle='#7a4a22';X.lineWidth=1.4*LS;X.stroke();
  // rìu người lùn
  if(rc==1){P((i,px,py,k,v,f)=>{if(ty[i]!=0)return;X.moveTo(px+3*k*f,py-11*v);X.lineTo(px+5.5*k*f,py-10*v);X.lineTo(px+5.5*k*f,py-8*v);X.lineTo(px+3*k*f,py-9*v)});X.fillStyle='#c9ced6';X.fill()}
  // khiên/ống tên màu phe
  P((i,px,py,k,v,f)=>{const b2=ty[i]==2?py-5*k:py;if(ty[i]==0&&rc!=3){X.moveTo(px-1.6*k*f+2*k,b2-5.2*v);X.ellipse(px-1.6*k*f,b2-5.2*v,2*k,2.6*v,0,0,7)}
   else if(ty[i]==1){X.rect(px-2.6*k*f-.8*k,b2-8*v,1.6*k,3.6*v)}else if(ty[i]==2){X.moveTo(px+11*k*f,b2-8*v);X.lineTo(px+8*k*f,b2-9.4*v);X.lineTo(px+8.4*k*f,b2-7.2*v)}});
  X.fillStyle=col;X.fill();X.strokeStyle='#111';X.lineWidth=.8*LS;X.stroke();
  // đầu tròn
  P((i,px,py,k,v)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v,r=1.9*k;X.moveTo(px+r,hy);X.arc(px,hy,r,0,7)});X.fillStyle=HC[rc]||RACE[rc].hc||'#222';X.fill();
  // nhận dạng tộc
  if(rc==4){P((i,px,py,k,v)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.rect(px-1.1*k,hy-.5*k,.8*k,.8*k);X.rect(px+.3*k,hy-.5*k,.8*k,.8*k);X.rect(px-.4*k,hy+.9*k,.8*k,.4*k)});X.fillStyle='#111';X.fill()}
  if(rc==0){P((i,px,py,k,v)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.moveTo(px-2.2*k,hy-.3*k);X.lineTo(px+2.2*k,hy-.3*k);X.lineTo(px,hy-3.2*k)});X.fillStyle='#8a9099';X.fill()}
  if(rc==1){P((i,px,py,k,v)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.moveTo(px-1.8*k,hy+.6*k);X.lineTo(px+1.8*k,hy+.6*k);X.lineTo(px,hy+4.4*k)});X.fillStyle='#c0662a';X.fill();
   P((i,px,py,k,v)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.moveTo(px-1.7*k,hy-1*k);X.lineTo(px-3.6*k,hy-3.8*k);X.lineTo(px-.9*k,hy-1.9*k);X.moveTo(px+1.7*k,hy-1*k);X.lineTo(px+3.6*k,hy-3.8*k);X.lineTo(px+.9*k,hy-1.9*k)});X.fillStyle='#eee';X.fill()}
  if(rc==2){P((i,px,py,k,v,f)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.moveTo(px+1.9*k,hy);X.arc(px,hy,1.95*k,Math.PI*1.05,-.05);X.rect(px-f*2.1*k-.5*k,hy-.4*k,1*k,3.6*k)});X.fillStyle='#f3e3a0';X.fill();
   P((i,px,py,k,v)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.moveTo(px-1.6*k,hy);X.lineTo(px-4*k,hy-2.4*k);X.moveTo(px+1.6*k,hy);X.lineTo(px+4*k,hy-2.4*k)});X.strokeStyle='#151515';X.lineWidth=1.2*LS;X.stroke()}
  if(rc==3){P((i,px,py,k,v,f)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.moveTo(px-1.8*k,hy-.8*k);X.lineTo(px-1.3*k,hy-4*k);X.lineTo(px-.1*k,hy-1.6*k);X.moveTo(px+1.8*k,hy-.8*k);X.lineTo(px+1.3*k,hy-4*k);X.lineTo(px+.1*k,hy-1.6*k);X.moveTo(px+1*k*f,hy-.2*k);X.lineTo(px+3.6*k*f,hy+.6*k);X.lineTo(px+1*k*f,hy+1.4*k)});X.fillStyle='#2a2a2a';X.fill()}
  const HY=(i,py,k,v)=>(ty[i]==2?py-5*k:py)-9.2*v;
  if(rc==5){P((i,px,py,k,v)=>{const hy=HY(i,py,k,v);X.rect(px-2.2*k,hy-2.6*k,4.4*k,1.3*k);X.moveTo(px-2*k,hy-2.6*k);X.lineTo(px-1.4*k,hy-4.6*k);X.lineTo(px-.8*k,hy-2.6*k);X.moveTo(px-.6*k,hy-2.6*k);X.lineTo(px,hy-5.2*k);X.lineTo(px+.6*k,hy-2.6*k);X.moveTo(px+.8*k,hy-2.6*k);X.lineTo(px+1.4*k,hy-4.6*k);X.lineTo(px+2*k,hy-2.6*k)});X.fillStyle='#e0b878';X.fill()}
  if(rc==6){P((i,px,py,k,v,f)=>{const by=ty[i]==2?py-5*k:py;X.moveTo(px-f*.5*k,by-6.8*v);X.quadraticCurveTo(px-f*7*k,by-11*v,px-f*6*k,by-3.5*v);X.closePath()});X.fillStyle='#ffffff';X.fill();X.strokeStyle='#d9cfa0';X.lineWidth=.6*LS;X.stroke();
   P((i,px,py,k,v)=>{const hy=HY(i,py,k,v);X.moveTo(px+2.4*k,hy-3*k);X.ellipse(px,hy-3*k,2.4*k,.8*k,0,0,7)});X.strokeStyle='#ffd23a';X.lineWidth=1.2*LS;X.stroke()}
  if(rc==7){P((i,px,py,k,v)=>{const hy=HY(i,py,k,v);X.moveTo(px-1.4*k,hy-1.2*k);X.quadraticCurveTo(px-3.6*k,hy-2.4*k,px-2.6*k,hy-4.6*k);X.lineTo(px-.6*k,hy-1.8*k);X.moveTo(px+1.4*k,hy-1.2*k);X.quadraticCurveTo(px+3.6*k,hy-2.4*k,px+2.6*k,hy-4.6*k);X.lineTo(px+.6*k,hy-1.8*k)});X.fillStyle='#111';X.fill();
   P((i,px,py,k,v)=>{const hy=HY(i,py,k,v);X.rect(px-1.1*k,hy-.4*k,.8*k,.6*k);X.rect(px+.3*k,hy-.4*k,.8*k,.6*k)});X.fillStyle='#ffd23a';X.fill()}
  if(rc==8){P((i,px,py,k,v,f)=>{const hy=HY(i,py,k,v),by=ty[i]==2?py-5*k:py;X.moveTo(px-1.8*k,hy-.6*k);X.lineTo(px-1.6*k,hy-4.2*k);X.lineTo(px-.2*k,hy-1.8*k);X.moveTo(px+1.8*k,hy-.6*k);X.lineTo(px+1.6*k,hy-4.2*k);X.lineTo(px+.2*k,hy-1.8*k);X.moveTo(px-f*.4*k,by-3.6*v);X.quadraticCurveTo(px-f*6*k,by-4*v,px-f*5*k,by-8*v);X.quadraticCurveTo(px-f*3.5*k,by-4.5*v,px-f*.4*k,by-2.6*v)});X.fillStyle='#e0802a';X.fill();
   P((i,px,py,k,v,f)=>{const by=ty[i]==2?py-5*k:py;X.moveTo(px-f*5*k+1.2*k,by-8*v);X.arc(px-f*5*k,by-8*v,1.2*k,0,7)});X.fillStyle='#fff';X.fill()}
  if(rc>=9){P((i,px,py,k,v)=>{const hy=HY(i,py,k,v);X.moveTo(px+1.1*k,hy-2.4*k);X.arc(px,hy-2.4*k,1.1*k,0,7);X.rect(px-1.9*k,hy-1.6*k,3.8*k,.9*k)});X.fillStyle='#111';X.fill();
   P((i,px,py,k,v,f)=>{const hy=HY(i,py,k,v);X.moveTo(px-f*3*k,hy-5*k);X.lineTo(px+f*6*k,hy-7*k)});X.strokeStyle=rc==11?'#d06cff':rc==10?'#ffd23a':'#7fe3ff';X.lineWidth=1.3*LS;X.stroke()}
  // dải màu phe trên đầu
  P((i,px,py,k,v)=>{const hy=(ty[i]==2?py-5*k:py)-9.2*v;X.rect(px-1.9*k,hy-.2*k,3.8*k,.9*k)});X.fillStyle=col;X.fill()}
 const A=b.ar;X.beginPath();for(let k=0;k<A.length;k+=8){
const p=A[k+4]/A[k+5],hh=Math.min(70,A[k+5]*55),px=A[k]+(A[k+2]-A[k])*p,py=A[k+1]+(A[k+3]-A[k+1])*p-Math.sin(p*Math.PI)*hh;
  if(px<vx0||px>vx1||py<vy0||py>vy1)continue;const dir=A[k+2]>A[k]?1:-1,sl=Math.cos(p*Math.PI)*hh/40;X.moveTo(px,py);X.lineTo(px-dir*6,py+sl*6)}
 X.strokeStyle='rgba(245,235,210,.85)';X.lineWidth=lo?1/z:1;X.stroke();X.setTransform(DPR,0,0,DPR,0,0)}

/* ================= VẼ BẢN ĐỒ ================= */
function soldier(x,y,k,c,f,t,rc=0){const b=Math.abs(Math.sin(t*10))*1.5;X.fillStyle='rgba(0,0,0,.28)';E(X,x+1,y+1,k=='cav'?12:6,3);let by=y-b;
 if(k=='cav'){X.fillStyle='#5a3b22';X.fillRect(x-9,y-7,2.5,7);X.fillRect(x+6,y-7,2.5,7);E(X,x,y-9-b*.4,11,5);X.fillRect(x+f*8-2,y-18-b*.4,4,9);E(X,x+f*11,y-18-b*.4,4,2.5);by=y-13-b*.4}
 else{X.fillStyle='#3a2f28';X.fillRect(x-3,by-4,2.5,5);X.fillRect(x+.5,by-4,2.5,5)}
 X.fillStyle=c;X.fillRect(x-4,by-13,8,10);X.fillStyle='rgba(255,255,255,.18)';X.fillRect(x-4,by-13,2,10);X.fillStyle='#f0c8a0';CI(X,x,by-16,3.6);X.fillStyle='#5b5f66';X.beginPath();X.arc(x,by-17,3.9,Math.PI,0);X.fill();
 X.strokeStyle='#dcdcdc';X.lineWidth=1.4;X.beginPath();X.moveTo(x+f*5,by-4);X.lineTo(x+f*(k=='cav'?19:12),by-(k=='cav'?13:23));X.stroke();
 const hy=by-16;if(rc==1){X.fillStyle='#b5651d';TRI(X,x-3.8,hy+1,x+3.8,hy+1,x,hy+9);X.fillStyle='#eee';TRI(X,x-4,hy-2,x-7,hy-8,x-2,hy-4);TRI(X,x+4,hy-2,x+7,hy-8,x+2,hy-4)}
 else if(rc==2){X.fillStyle='#f3e3a0';X.beginPath();X.arc(x,hy-.5,4.2,Math.PI,0);X.fill();X.fillRect(x-f*4.4,hy-1,2,8);X.fillStyle='#f8ead8';TRI(X,x-3.5,hy,x-8,hy-4,x-3.5,hy+2);TRI(X,x+3.5,hy,x+8,hy-4,x+3.5,hy+2)}
 else if(rc==5){X.fillStyle='#8d939b';CI(X,x,hy,4.4);X.fillStyle='#e0b878';X.fillRect(x-4.5,hy-5,9,2.2);TRI(X,x-4,hy-5,x-2.5,hy-9,x-1,hy-5);TRI(X,x-1.5,hy-5,x,hy-10,x+1.5,hy-5);TRI(X,x+1,hy-5,x+2.5,hy-9,x+4,hy-5)}
 else if(rc==6){X.fillStyle='#fff';X.beginPath();X.moveTo(x-f*2,hy+6);X.quadraticCurveTo(x-f*14,hy-2,x-f*12,hy+14);X.fill();X.strokeStyle='#ffd23a';X.lineWidth=1.4;X.beginPath();X.ellipse(x,hy-6,4.5,1.6,0,0,7);X.stroke()}
 else if(rc==7){X.fillStyle='#b3261e';CI(X,x,hy,4);X.fillStyle='#111';TRI(X,x-3,hy-2,x-6,hy-9,x-1,hy-4);TRI(X,x+3,hy-2,x+6,hy-9,x+1,hy-4);X.fillStyle='#ffd23a';X.fillRect(x-2,hy-1,1.3,1.3);X.fillRect(x+.8,hy-1,1.3,1.3)}
 else if(rc==8){X.fillStyle='#e0802a';CI(X,x,hy,4);TRI(X,x-4,hy-1,x-3.5,hy-9,x-.5,hy-3);TRI(X,x+4,hy-1,x+3.5,hy-9,x+.5,hy-3);X.beginPath();X.moveTo(x-f*3,y-8);X.quadraticCurveTo(x-f*14,y-8,x-f*12,y-18);X.lineWidth=4;X.strokeStyle='#e0802a';X.stroke()}
 else if(rc>=9){X.fillStyle='#111';CI(X,x,hy-4.5,2.2);X.strokeStyle=rc==11?'#d06cff':rc==10?'#ffd23a':'#7fe3ff';X.lineWidth=1.6;X.beginPath();X.moveTo(x-8,hy-10);X.lineTo(x+8,hy-13);X.stroke()}
 else if(rc==4){X.fillStyle='#ece7da';CI(X,x,hy,4.2);X.fillStyle='#111';CI(X,x-1.5,hy-.5,1.1);CI(X,x+1.5,hy-.5,1.1);X.fillRect(x-1,hy+2,2,1)}
 else if(rc==3){X.fillStyle='#7d7d7d';CI(X,x,hy,4);TRI(X,x-4,hy-1,x-3,hy-8,x-.5,hy-3);TRI(X,x+4,hy-1,x+3,hy-8,x+.5,hy-3);X.fillStyle='#555';E(X,x+f*3,hy+1.5,3,2);X.fillStyle='#ffd23a';CI(X,x+f*1.3,hy-1,.9)}}
function flag(c,t,s,top){X.fillStyle='#3a2a1a';X.fillRect(-.6,top,1.4,15);X.fillStyle=c;const wv=Math.sin(t*3+s.id)*2;X.beginPath();X.moveTo(.8,top);X.quadraticCurveTo(8,top-2+wv,15,top+1+wv);X.lineTo(15,top+8+wv);X.quadraticCurveTo(8,top+5+wv,.8,top+7);X.fill()}
function keep(s,c,t){const r=s.race,fl=Math.sin(t*6+s.id)*.5+.5;
 if(r==0){X.fillStyle='rgba(0,0,0,.28)';E(X,6,4,36,11);X.fillStyle='#8c7c5a';E(X,0,0,31,9);
 if(s.type<2)for(const i of[-1,1]){const hx=i*42;X.fillStyle='rgba(0,0,0,.25)';E(X,hx+3,3,10,3);X.fillStyle='#dccca6';X.fillRect(hx-7,-8,14,9);X.fillStyle='#9a4a2a';TRI(X,hx-9,-8,hx+9,-8,hx,-16)}
 X.fillStyle=RACE[s.race].wall;X.fillRect(-20,-16,40,16);X.fillStyle='#93886f';X.fillRect(-20,-4,40,4);X.fillStyle='#c9bfa8';for(let i=0;i<38;i+=6)X.fillRect(-20+i,-19,4,3);
 X.fillStyle='#4a3622';X.fillRect(-4,-9,8,9);
 for(const i of[-1,1]){const tx=i*20;X.fillStyle=i<0?'#b2a68e':'#9a8f78';X.fillRect(tx-5,-24,10,24);X.fillStyle=c;TRI(X,tx-7,-24,tx+7,-24,tx,-35);X.fillStyle='rgba(0,0,0,.25)';TRI(X,tx,-35,tx+7,-24,tx,-24)}
 X.fillStyle='#c6bca6';X.fillRect(-7,-30,14,22);X.fillStyle='rgba(0,0,0,.15)';X.fillRect(0,-30,7,22);X.fillStyle=c;TRI(X,-9,-30,9,-30,0,-43);X.fillStyle='rgba(0,0,0,.25)';TRI(X,0,-43,9,-30,0,-30);
 X.fillStyle='#3a2a1a';X.fillRect(-.6,-58,1.4,15);X.fillStyle=c;const wv=Math.sin(t*3+s.id)*2;X.beginPath();X.moveTo(.8,-58);X.quadraticCurveTo(8,-60+wv,15,-57+wv);X.lineTo(15,-50+wv);X.quadraticCurveTo(8,-53+wv,.8,-51);X.fill();return}
 X.fillStyle='rgba(0,0,0,.28)';E(X,6,4,38,11);
 if(r==1){X.fillStyle='#6f6a63';TRI(X,-40,0,0,-48,40,0);X.fillStyle='#57524c';TRI(X,0,-48,40,0,0,0);X.fillStyle='#eef0f2';TRI(X,-9,-37,0,-48,9,-37);
  X.fillStyle='#3e3a35';X.beginPath();X.moveTo(-10,0);X.lineTo(-10,-12);X.arc(0,-12,10,Math.PI,0);X.lineTo(10,0);X.fill();X.fillStyle='#ffb040';X.fillRect(-2,-8,4,8);
  for(const i of[-1,1]){X.fillStyle='#4a4038';X.fillRect(i*17-2,-10,4,10);X.fillStyle=`rgba(255,${140+fl*80|0},40,.95)`;CI(X,i*17,-13,3+fl*1.5)}X.fillStyle=c;X.fillRect(-14,-24,28,4);flag(c,t,s,-62);return}
 if(r==2){X.fillStyle='#6b4a2a';X.fillRect(-5,-34,10,34);X.fillRect(-14,-4,28,4);X.fillStyle='#2f6e2a';CI(X,0,-44,22);CI(X,-17,-32,13);CI(X,17,-32,13);X.fillStyle='#4fa040';CI(X,-6,-48,12);CI(X,10,-38,9);X.fillStyle='rgba(200,255,150,.3)';CI(X,-9,-52,6);
  for(const [hx,hy] of[[-14,-20],[13,-24]]){X.fillStyle='#f2ead2';X.fillRect(hx-6,hy-5,12,6);X.fillStyle=c;TRI(X,hx-8,hy-5,hx+8,hy-5,hx,hy-12)}X.fillStyle=`rgba(255,240,120,${.5+fl*.5})`;CI(X,-20,-28,1.8);CI(X,20,-30,1.8);CI(X,0,-30,2);flag(c,t,s,-80);return}
 if(r==3){X.fillStyle='#7a5530';for(let a=0;a<6.28;a+=.35){const px=Math.cos(a)*30,py=Math.sin(a)*10-2;X.fillRect(px-1.8,py-12,3.6,12);TRI(X,px-1.8,py-12,px+1.8,py-12,px,py-16)}
  for(const [hx,hy] of[[-10,-4],[11,-2],[0,-10]]){X.fillStyle=c;TRI(X,hx-8,hy,hx+8,hy,hx,hy-14);X.fillStyle='rgba(0,0,0,.25)';TRI(X,hx,hy-14,hx+8,hy,hx,hy)}
  X.fillStyle='#5a3a1e';X.fillRect(-2,-34,4,26);X.fillStyle='#eee';CI(X,0,-36,5);TRI(X,-4,-38,-6,-45,-1,-40);TRI(X,4,-38,6,-45,1,-40);X.fillStyle=`rgba(255,${120+fl*90|0},30,.9)`;CI(X,18,-4,3+fl*2);flag(c,t,s,-58);return}
 if(r==4){X.fillStyle='#2e2a2e';X.fillRect(-9,-46,18,46);X.fillStyle='#3e383e';X.fillRect(-22,-22,10,22);X.fillRect(12,-22,10,22);
  X.fillStyle='#1e1a1e';TRI(X,-11,-46,11,-46,0,-60);TRI(X,-23,-22,-11,-22,-17,-32);TRI(X,11,-22,23,-22,17,-32);X.fillStyle=`rgba(190,90,255,${.6+fl*.4})`;X.fillRect(-3,-38,6,8);X.fillRect(-19,-16,4,5);X.fillRect(15,-16,4,5);
  X.fillStyle='#777';for(const gx of[-30,-26,26,31]){X.fillRect(gx-2,-6,4,6);CI(X,gx,-6,2)}flag(c,t,s,-75);return}
 if(r==5){X.fillStyle='#b8a888';X.fillRect(-34,-10,68,10);X.fillStyle='#a8987a';X.fillRect(-26,-20,52,10);X.fillStyle='#988a6c';X.fillRect(-18,-30,36,10);X.fillStyle='#8a7c60';X.fillRect(-10,-40,20,10);
  for(const i of[-1,1]){X.fillStyle='#c9bc9c';X.fillRect(i*40-4,-46,8,46);X.fillStyle='#e0b878';X.fillRect(i*40-6,-50,12,4)}X.fillStyle='#e0b878';TRI(X,-10,-40,10,-40,0,-52);X.fillStyle=c;X.fillRect(-26,-14,52,3);flag(c,t,s,-70);return}
 if(r==6){X.fillStyle='#ffffff';X.fillRect(-30,-6,60,6);X.fillRect(-26,-10,52,4);for(let i=-20;i<=20;i+=10){X.fillStyle='#f4efe2';X.fillRect(i-2,-30,4,20)}X.fillStyle='#ffffff';X.fillRect(-26,-34,52,4);
  X.fillStyle='#ffd23a';X.beginPath();X.arc(0,-34,14,Math.PI,0);X.fill();X.fillStyle='rgba(255,255,255,.4)';X.beginPath();X.arc(-4,-38,6,Math.PI,0);X.fill();
  X.strokeStyle=`rgba(255,220,80,${.6+fl*.4})`;X.lineWidth=2;X.beginPath();X.ellipse(0,-56,10,3,0,0,7);X.stroke();X.fillStyle='#fff';for(const i of[-1,1]){X.beginPath();X.moveTo(i*28,-24);X.quadraticCurveTo(i*48,-44,i*44,-12);X.quadraticCurveTo(i*38,-18,i*28,-14);X.fill()}flag(c,t,s,-78);return}
 if(r==7){X.fillStyle='#1c1012';X.beginPath();X.moveTo(-32,0);X.lineTo(-26,-26);X.lineTo(-18,-14);X.lineTo(-10,-44);X.lineTo(0,-24);X.lineTo(10,-50);X.lineTo(18,-16);X.lineTo(26,-30);X.lineTo(32,0);X.fill();
  X.strokeStyle=`rgba(255,${80+fl*90|0},20,.95)`;X.lineWidth=1.6;X.beginPath();X.moveTo(-20,-2);X.lineTo(-14,-12);X.lineTo(-8,-6);X.moveTo(6,-2);X.lineTo(10,-20);X.lineTo(16,-10);X.stroke();X.fillStyle=`rgba(255,${60+fl*120|0},20,.9)`;CI(X,10,-52,4+fl*2);X.fillStyle='#ff3a20';X.fillRect(-4,-14,8,14);flag(c,t,s,-70);return}
 if(r>=9){const rf=r==11?'#5a2a7a':r==10?'#c08a20':'#2a6a8a';X.fillStyle='#7d8a7a';TRI(X,-34,0,-4,-50,26,0);X.fillStyle='#667060';TRI(X,-4,-50,26,0,-4,0);X.fillStyle='#8fa08a';TRI(X,8,0,26,-34,40,0);
  for(const [hx,hy,w] of[[-6,-44,12],[14,-26,10],[-18,-20,10]]){X.fillStyle='#f2ecd8';X.fillRect(hx-w/2,hy,w,6);X.fillStyle=rf;X.beginPath();X.moveTo(hx-w/2-4,hy);X.quadraticCurveTo(hx,hy-7,hx+w/2+4,hy);X.fill()}
  X.fillStyle=`rgba(255,255,255,${.55+fl*.25})`;E(X,-22,-8,14,4);E(X,20,-14,12,3.5);E(X,0,-30,10,3);X.strokeStyle=r==11?'#d06cff':r==10?'#ffd23a':'#7fe3ff';X.lineWidth=1.5;X.beginPath();X.moveTo(-26,-60-fl*3);X.lineTo(-12,-64-fl*3);X.stroke();flag(c,t,s,-72);return}
 if(r==8){for(let i=0;i<3;i++){const w=30-i*8,y0=-i*14;X.fillStyle='#5a2a1a';X.fillRect(-w*.6,y0-12,w*1.2,12);X.fillStyle=i==0?c:'#b03020';X.beginPath();X.moveTo(-w-6,y0-12);X.quadraticCurveTo(0,y0-20,w+6,y0-12);X.lineTo(w*.6,y0-16);X.lineTo(-w*.6,y0-16);X.fill()}
  X.fillStyle='#ffd23a';TRI(X,-3,-44,3,-44,0,-56);X.fillStyle=`rgba(255,80,40,${.6+fl*.4})`;CI(X,-22,-8,2.5);CI(X,22,-8,2.5);X.fillStyle='#3a8a3a';for(const bx of[-34,-30,32,36]){X.fillRect(bx,-26,2,26)}flag(c,t,s,-74);return}}
const SPC=new Map();function SPR(key,w,h,ox,oy,fn){let cv=SPC.get(key);if(cv)return cv;cv=document.createElement('canvas');const R2=2;cv.width=w*R2;cv.height=h*R2;const g=cv.getContext('2d');const ox0=X;X=g;g.setTransform(R2,0,0,R2,ox*R2,oy*R2);try{fn()}finally{X=ox0}SPC.set(key,cv);if(SPC.size>400)SPC.delete(SPC.keys().next().value);return cv}
