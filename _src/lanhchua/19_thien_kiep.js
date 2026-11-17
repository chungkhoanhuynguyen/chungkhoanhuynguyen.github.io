/* ================= CẢNH THIÊN KIẾP (phi thăng / đột phá) =================
 thienKiep(n, tieuDe, phuDe, xong): mây kiếp xoáy tụ → n đạo lôi kiếp giáng xuống → cột sáng phi thăng → xong() */
let TKON=0;
function thienKiep(n,title,sub,done,gold){if(TKON){done&&done();return}TKON=1;const pp=paused;paused=true;MC.follow=1;
 const cv=document.createElement('canvas');cv.style.cssText='position:fixed;inset:0;width:100vw;height:100vh;z-index:30;pointer-events:auto';document.body.appendChild(cv);
 const D=Math.min(2,devicePixelRatio||1)*(LOWQ?.75:1),w=innerWidth,h=innerHeight;cv.width=w*D|0;cv.height=h*D|0;const g=cv.getContext('2d');g.scale(D,D);
 const px=w/2,py=h*.55,vx=w/2,vy=Math.max(70,h*.12),T0=performance.now(),gap=n>6?.42:.55,tS=1.3,tE=tS+n*gap,tP=tE+.3,tEnd=tP+(n>3?2.4:1.6);
 const CL=Array.from({length:LOWQ?26:46},(_,i)=>({a:Math.random()*6.28,r:30+Math.random()*Math.max(w,h)*.55,s:(.25+Math.random()*.5)*(Math.random()<.5?-1:1),z:50+Math.random()*110,d:.35+Math.random()*.4}));
 const SP=[];let bolts=[],fl=0,shake=0,hit=-1,ended=0;
 const bolt=(x0,y0,x1,y1,dv)=>{let P=[[x0,y0],[x1,y1]];for(let k=0;k<6;k++){const Q=[P[0]];for(let i=1;i<P.length;i++){const a=P[i-1],b=P[i],l=Math.hypot(b[0]-a[0],b[1]-a[1]);Q.push([(a[0]+b[0])/2+(Math.random()-.5)*l*dv,(a[1]+b[1])/2+(Math.random()-.5)*l*dv*.3]);Q.push(b)}P=Q}return P};
 const strike=i=>{const tx=px+(Math.random()-.5)*40,P=bolt(vx+(Math.random()-.5)*120,vy,tx,py,.55),br=[];for(let k=0;k<3;k++){const s=P[(P.length*(.25+Math.random()*.4))|0];br.push(bolt(s[0],s[1],s[0]+(Math.random()-.5)*260,s[1]+60+Math.random()*160,.6))}
  bolts.push({P,br,t:0});fl=1;shake=14+i*1.5;for(let k=0;k<26;k++)SP.push({x:tx,y:py,vx:(Math.random()-.5)*420,vy:-Math.random()*360,l:.7+Math.random()*.5,c:Math.random()<.5?'#bfe6ff':'#fff'});
  try{nz(.9,.45,90+Math.random()*60);tone(70,1.1,'sawtooth',.14,28);setTimeout(()=>nz(.5,.25,1400),40)}catch(e){}};
 const line=(P,wd,c)=>{g.strokeStyle=c;g.lineWidth=wd;g.beginPath();g.moveTo(P[0][0],P[0][1]);for(let i=1;i<P.length;i++)g.lineTo(P[i][0],P[i][1]);g.stroke()};
 const txt=(s,y,sz,col,a)=>{g.globalAlpha=a;g.font=`900 ${sz}px system-ui,sans-serif`;g.textAlign='center';g.lineWidth=Math.max(4,sz/7);g.strokeStyle='rgba(0,0,0,.85)';g.strokeText(s,w/2,y);g.fillStyle=col;g.fillText(s,w/2,y);g.globalAlpha=1};
 let last=T0;
 const fr=now=>{if(ended)return;const t=(now-T0)/1000,dt=Math.min(.05,(now-last)/1000);last=now;
  const k=Math.floor((t-tS)/gap);if(t>=tS&&k<n&&k>hit){hit=k;strike(k)}
  g.setTransform(D,0,0,D,0,0);const sx=shake?(Math.random()-.5)*shake:0,sy=shake?(Math.random()-.5)*shake:0;shake*=.86;if(shake<.4)shake=0;g.translate(sx,sy);
  const dk=Math.min(1,t/1.1)*(t>tP?Math.max(.15,1-(t-tP)/1.4):1);g.clearRect(-30,-30,w+60,h+60);
  g.fillStyle=`rgba(6,4,18,${.88*dk})`;g.fillRect(-30,-30,w+60,h+60);
  for(const c of CL){c.a+=c.s*dt*(1+fl*2);const r=c.r*(1-Math.min(.35,t*.08)),x=vx+Math.cos(c.a)*r,y=vy+Math.sin(c.a)*r*.32;const gr=g.createRadialGradient(x,y,0,x,y,c.z);
   const lit=fl*.6;gr.addColorStop(0,`rgba(${60+lit*160|0},${40+lit*150|0},${90+lit*165|0},${c.d*dk})`);gr.addColorStop(1,'rgba(20,10,40,0)');g.fillStyle=gr;g.fillRect(x-c.z,y-c.z,c.z*2,c.z*2)}
  if(t>tS-.4&&t<tP+.6){const a=Math.min(1,(t-tS+.4)*2)*(t>tP?Math.max(0,1-(t-tP)/.6):1),gr=g.createRadialGradient(vx,vy,0,vx,vy,90+fl*60);gr.addColorStop(0,`rgba(220,200,255,${.6*a})`);gr.addColorStop(1,'rgba(120,60,255,0)');g.fillStyle=gr;g.beginPath();g.arc(vx,vy,150+fl*60,0,7);g.fill()}
  g.lineCap='round';g.lineJoin='round';
  for(let i=bolts.length-1;i>=0;i--){const b=bolts[i];b.t+=dt;const a=Math.max(0,1-b.t/.35);if(a<=0){bolts.splice(i,1);continue}g.globalAlpha=a;
   line(b.P,14,'rgba(140,110,255,.35)');for(const q of b.br)line(q,6,'rgba(140,110,255,.3)');line(b.P,5,'rgba(190,225,255,.9)');for(const q of b.br)line(q,2,'rgba(200,230,255,.8)');line(b.P,2,'#fff');g.globalAlpha=1}
  if(fl>0){g.fillStyle=`rgba(225,235,255,${fl*.55})`;g.fillRect(-30,-30,w+60,h+60);fl=Math.max(0,fl-dt*4.5)}
  const pa=t<tS?0:Math.min(1,(t-tS)/.5)*(t>tP?Math.max(0,1-(t-tP)/2.2):1);
  if(pa>0){const gr=g.createRadialGradient(px,py,0,px,py,60);gr.addColorStop(0,`rgba(255,255,255,${pa})`);gr.addColorStop(.4,`rgba(170,210,255,${.6*pa})`);gr.addColorStop(1,'rgba(120,80,255,0)');g.fillStyle=gr;g.beginPath();g.arc(px,py,60,0,7);g.fill();
   g.fillStyle=`rgba(255,240,180,${pa})`;g.font='38px system-ui';g.textAlign='center';g.fillText(gold?'🧘':'🛡',px,py+12)}
  if(t>tE){const u=t-tE,a=Math.min(1,u*2)*Math.max(0,1-(u-1.4)/1),wd=40+u*90,gr=g.createLinearGradient(px-wd,0,px+wd,0);gr.addColorStop(0,'rgba(255,220,120,0)');gr.addColorStop(.5,`rgba(255,248,215,${.95*a})`);gr.addColorStop(1,'rgba(255,220,120,0)');g.fillStyle=gr;g.fillRect(px-wd,-30,wd*2,py+30);
   for(let k=0;k<3;k++){const rr=((u*1.2+k*.33)%1),r=20+rr*Math.max(w,h)*.6;g.strokeStyle=`rgba(255,226,140,${(1-rr)*.8*a})`;g.lineWidth=3+6*(1-rr);g.beginPath();g.ellipse(px,py,r,r*.32,0,0,7);g.stroke()}
   if(Math.random()<.9)for(let k=0;k<4;k++)SP.push({x:px+(Math.random()-.5)*wd*1.6,y:py,vx:(Math.random()-.5)*40,vy:-200-Math.random()*400,l:1.2,c:Math.random()<.5?'#ffe28a':'#fff8d8'})}
  for(let i=SP.length-1;i>=0;i--){const s=SP[i];s.l-=dt;if(s.l<=0){SP.splice(i,1);continue}s.x+=s.vx*dt;s.y+=s.vy*dt;s.vy+=s.c=='#fff'||s.c=='#bfe6ff'?600*dt:-60*dt;g.globalAlpha=Math.min(1,s.l*1.5);g.fillStyle=s.c;g.fillRect(s.x-1.5,s.y-1.5,3,3)}g.globalAlpha=1;
  g.setTransform(D,0,0,D,0,0);const big=Math.min(64,w/9);
  txt(title,h*.3,big,gold?'#ffe066':'#e4d8ff',Math.min(1,t/.8)*(t>tE?Math.max(0,1-(t-tE)/.3):1));
  if(t>=tS&&t<tE+.2)txt(`Đạo lôi kiếp ${Math.min(n,hit+1)}/${n}`,h*.3+big*.9,Math.min(26,w/18),'#bfe6ff',1);
  if(t>tE+.32)txt(sub,h*.3,big*1.15,'#ffe066',Math.min(1,(t-tE-.32)*2.5)*(t>tEnd-.5?Math.max(0,(tEnd-t)/.5):1));
  if(t>tEnd-.45){g.fillStyle=`rgba(255,250,235,${Math.min(1,(t-(tEnd-.45))/.45)})`;g.fillRect(0,0,w,h)}
  if(t>=tEnd){ended=1;finish();return}requestAnimationFrame(fr)};
 const finish=()=>{const TT=$('#toast');if(TT)TT.style.visibility='';cv.style.transition='opacity .5s';cv.style.opacity='0';setTimeout(()=>cv.remove(),550);TKON=0;paused=pp;try{done&&done()}catch(e){console.error(e)}};
 cv.onclick=()=>{if(performance.now()-T0>2500&&!ended){ended=1;finish()}};
 const TT=$('#toast');if(TT)TT.style.visibility='hidden';const fin0=finish;SFX.war();requestAnimationFrame(fr)}
