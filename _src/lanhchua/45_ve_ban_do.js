function castle(s,t,z){const x=s.x,y=s.y,c=facC(s.fac);
 if(z<.42){const r=[9,7,5][s.type]/z;X.fillStyle=G?rel(s.fac):'rgba(0,0,0,.5)';X.fillRect(x-r-2.5/z,y-r-2.5/z,2*r+5/z,2*r+5/z);if(G&&s.own===0){X.strokeStyle='#ffd23a';X.lineWidth=3/z;X.strokeRect(x-r-5/z,y-r-5/z,2*r+10/z,2*r+10/z)}X.fillStyle=c;X.fillRect(x-r,y-r,2*r,2*r);
  if((SMALL()?s.type==0:s.type<2)&&z>.14&&(!G||s.race==PC())){X.font=`bold ${11/z}px system-ui,sans-serif`;X.textAlign='center';X.lineWidth=3/z;X.strokeStyle='rgba(0,0,0,.8)';X.strokeText(s.name,x,y+r+12/z);X.fillStyle=G?rel(s.fac):'#fff';X.fillText(s.name,x,y+r+12/z)}return}
 const k=[1.5,1.2,1][s.type];X.save();X.translate(x,y);X.scale(k,k);
 X.restore();{const sp=SPR(`k${s.race}|${c}`,200,180,100,150,()=>keep(s,c,0));X.drawImage(sp,x-100*k,y-150*k,200*k,180*k)}
 if(G&&s.race!=PC())return;const o=G&&G.L[s.own],mine=o&&o.kind=='pl',on=(!SMALL()||z>.95)&&o&&!o.dead?`${rank(o)[2]} ${o.kind=='pl'?rank(o)[0]+' (Bạn)':pname(o)}`:'',nm=`${relI(s.fac)} ${s.name}${s.type==0?' 👑':''}`+(SMALL()&&s.gar?` · 🛡${fmt(tot(s.gar))}`:''),bh=on?46:SMALL()?18:32;
 X.font='bold 13px system-ui,sans-serif';const w1=X.measureText(nm).width;X.font='11px system-ui,sans-serif';const tw=Math.max(w1,X.measureText(on).width);
 LBL.push({p:mine?1:2+s.type,x:x-tw/2-8,y:y+10,w:tw+16,h:bh,d:()=>{X.textAlign='center';X.fillStyle='rgba(18,12,6,.86)';X.fillRect(x-tw/2-8,y+10,tw+16,bh);X.fillStyle=c;X.fillRect(x-tw/2-8,y+10,4,bh);if(mine){X.strokeStyle='#ffd23a';X.lineWidth=2;X.strokeRect(x-tw/2-8,y+10,tw+16,bh)}
 X.font='bold 13px system-ui,sans-serif';X.fillStyle=G?rel(s.fac):'#fff';X.fillText(nm,x,y+24);X.font='11px system-ui,sans-serif';
 if(on){X.fillStyle=mine?'#ffd23a':'#e9dcc0';X.fillText(on,x,y+38)}X.fillStyle='#ffd77a';if(s.gar&&bh>18)X.fillText('🛡 '+fmt(tot(s.gar)),x,y+(on?52:38))}})}
function village(v,t,z){const x=v.x,y=v.y,s=S[v.p],mine=G&&v.own===0;
 if(z<.42){X.fillStyle=mine?'#ffd23a':G?rel(s.fac):'#ddd';CI(X,x,y,3.2/z);X.fillStyle=v.burn?'#333':'#8a6a3a';CI(X,x,y,2/z);return}
 {const vb=v.burn?1:0;const sp=SPR('v'+vb,120,80,60,30,()=>{for(let i=0;i<4;i++){X.fillStyle=vb?'#4a4036':['#c9b45a','#8fae4a','#b9a04a','#9dbb55'][i];X.save();X.rotate(.3);X.fillRect(-46+i*22,8+(i%2)*10,20,13);X.restore()}
 for(const [hx,hy] of[[-14,-2],[6,-8],[18,4],[-2,8]]){X.fillStyle='rgba(0,0,0,.25)';E(X,hx+3,hy+3,8,3);X.fillStyle=vb?'#3a3530':'#e2d2ac';X.fillRect(hx-6,hy-6,12,8);X.fillStyle=vb?'#1e1a18':'#a5522c';TRI(X,hx-8,hy-6,hx+8,hy-6,hx,hy-13)}});X.drawImage(sp,x-60,y-30,120,80)}X.save();X.translate(x,y);
 if(v.burn){X.fillStyle='rgba(60,60,60,.35)';for(let i=0;i<4;i++)CI(X,Math.sin(t+i)*6,-18-((t*12+i*9)%30),5+i)}X.restore();
 if(SMALL()&&!mine&&z<1.1)return;if(G&&s.race!=PC())return;const o=G&&G.L[v.own],nm=`🌾 ${v.name}`,on=!SMALL()&&o&&!o.dead?(mine?'⭐ Đất phong của bạn':`${rank(o)[2]} ${pname(o)}`):mine?'⭐ của bạn':'';
 X.font='bold 11px system-ui,sans-serif';const tw=Math.max(X.measureText(nm).width,X.measureText(on).width),bh=on?28:15;
 LBL.push({p:mine?1.5:8,x:x-tw/2-6,y:y+22,w:tw+12,h:bh,d:()=>{X.textAlign='center';X.font='bold 11px system-ui,sans-serif';X.fillStyle='rgba(18,12,6,.78)';X.fillRect(x-tw/2-6,y+22,tw+12,bh);if(mine){X.strokeStyle='#ffd23a';X.lineWidth=1.5;X.strokeRect(x-tw/2-6,y+22,tw+12,bh)}
 X.fillStyle=mine?'#ffd23a':G?rel(s.fac):'#fff';X.fillText(nm,x,y+33);if(on){X.font='10px system-ui,sans-serif';X.fillStyle=mine?'#ffe9a0':'#d9ccb0';X.fillText(on,x,y+46)}}})}
function blob(c,z){const k=Math.min(2.4,1/Math.min(1,z)),r=cl(5+Math.log10(c.n+1)*3,7,20)*k,col=facC(c.fac),re=rel(c.fac);
 X.fillStyle='rgba(0,0,0,.3)';E(X,c.x+2*k,c.y+3*k,r*1.1,r*.5);X.fillStyle=re;CI(X,c.x,c.y,r+2.5*k);X.fillStyle=col;CI(X,c.x,c.y,r);X.fillStyle='rgba(255,255,255,.25)';CI(X,c.x-r*.3,c.y-r*.3,r*.35);
 const l=`${c.k?'👑 ':''}${fmt(c.n)}`;X.font=`900 ${10*k}px system-ui`;X.textAlign='center';X.lineWidth=3*k;X.strokeStyle='#000';X.strokeText(l,c.x,c.y+3.5*k);X.fillStyle='#fff';X.fillText(l,c.x,c.y+3.5*k);
 X.font=`700 ${8.5*k}px system-ui`;const s=`${c.m} đạo quân`;X.strokeText(s,c.x,c.y+r+11*k);X.fillStyle=re;X.fillText(s,c.x,c.y+r+11*k)}
function party(p,t,z){const c=facC(p.fac),x=p.x,y=p.y,n=tot(p.t);
 if(z<.42||(ULQ&&p.kind!='pl')){const zq=z<.42?z:.55;const r=(p.kind=='pl'?5:p.kind=='rf'?2.5:cl(2+Math.log10(n+1)*1.2,2.5,6))/zq;
  if(p.kind=='pl'){X.strokeStyle='#ffd65a';X.lineWidth=2.5/zq;X.beginPath();X.arc(x,y,r+4/zq,0,7);X.stroke()}
  X.fillStyle=rel(p.fac);CI(X,x,y,r+1.8/zq);X.fillStyle=c;CI(X,x,y,r);
  if(p.kind=='pl'||(p.kind=='king'&&z>.15)){X.font=`bold ${10/zq}px system-ui`;X.textAlign='center';X.lineWidth=3/zq;X.strokeStyle='#000';const l=(p.kind=='pl'?'★ Bạn ':'')+fmt(n);X.strokeText(l,x,y-r-4/zq);X.fillStyle=p.kind=='pl'?'#ffd65a':'#fff';X.fillText(l,x,y-r-4/zq)}return}
 if(p.kind=='pl'){X.strokeStyle='#ffd65a';X.lineWidth=2.5;X.beginPath();X.ellipse(x,y+1,17,7,0,0,7);X.stroke()}else if(p.kind!='rf'){X.strokeStyle=rel(p.fac);X.globalAlpha=.85;X.lineWidth=2;X.beginPath();X.ellipse(x,y+1,15,6,0,0,7);X.stroke();X.globalAlpha=1}
 if(p.kind=='rf'){X.fillStyle='rgba(0,0,0,.3)';E(X,x+1,y+1,9,3);X.fillStyle='#7a5a32';X.fillRect(x-8,y-9,16,8);X.fillStyle=c;X.fillRect(x-8,y-12,16,3);X.fillStyle='#3a2a1a';CI(X,x-5,y,2.5);CI(X,x+5,y,2.5)}
 else{const k=p.t.cav>p.t.inf*.5?'cav':'inf';if(tAt(x,y)==0){X.fillStyle='#6b4423';X.beginPath();X.moveTo(x-20,y-6);X.lineTo(x+20,y-6);X.lineTo(x+14,y+4);X.lineTo(x-14,y+4);X.fill();X.fillStyle='#3a2a1a';X.fillRect(x-1,y-40,2,34);X.fillStyle='#efe6d0';TRI(X,x+1,y-40,x+16,y-12,x+1,y-12)}X.save();X.translate(x,y-(tAt(x,y)==0?6:0));X.scale(1.3,1.3);soldier(0,0,k,c,p.face,p.mv?t:0,raceOf(p));X.restore();
  X.fillStyle='#3a2a1a';X.fillRect(x-13,y-38,1.6,36);X.fillStyle=c;const wv=Math.sin(t*4+x)*1.5;X.beginPath();X.moveTo(x-11.5,y-38);X.lineTo(x+1,y-37+wv);X.lineTo(x+1,y-28+wv);X.lineTo(x-11.5,y-29);X.fill();
  if(p.kind=='king'){X.fillStyle='#ffd23a';TRI(X,x-10,y-41,x-6,y-41,x-8,y-46)}}
 if(p.kind=='rf'&&SMALL())return;if(p.kind!='pl'&&contOf(x,y)!=PC())return;X.font='bold 10px system-ui,sans-serif';const full=p.kind=='pl'||p.kind=='king'||(z>(SMALL()?.95:.6)),lb=(p.kind=='lord'||p.kind=='king'||p.kind=='pl'?rank(p)[2]+' ':'')+(full||p.kind!='lord'?pname(p)+' · ':'')+fmt(n),tw=X.measureText(lb).width;
 const rk=rank(p),ri0=RK.indexOf(rk[0]),plate=(p.kind=='pl'||p.kind=='king'||p.kind=='exile'||ri0>=4)&&p.kind!='rf'&&p.kind!='bandit';
 LBL.push({p:p.kind=='pl'?0:p.kind=='king'?5:atWar(P0().fac,p.fac)?6:p.kind=='rf'?9:7,x:x-tw/2-4,y:y+5,w:tw+8,h:13,d:()=>{if(plate)titlePlate(x,y-50,rk,t);X.textAlign='center';X.font='bold 10px system-ui,sans-serif';X.fillStyle='rgba(15,10,6,.74)';X.fillRect(x-tw/2-4,y+5,tw+8,13);X.fillStyle=p.kind=='pl'?'#ffd65a':p.kind=='rf'?'#9cf':rel(p.fac);X.fillText(lb,x,y+15)}})}
function titlePlate(x,y,rk,t){const txt=rk[0].toUpperCase(),hi=RK.indexOf(rk[0]),big=hi>=9,ic=rk[2],col=rk[3],gl=.55+Math.sin(t*3+x*.01)*.45;
 X.font='800 8.5px system-ui,sans-serif';const tw=X.measureText(txt).width,w=tw+26,h=13;X.save();X.translate(x,y);
 if(!LOWQ){X.shadowColor=col;X.shadowBlur=(big?18:hi>=7?12:7)*gl}
 if(big||hi>=7){X.fillStyle=col;X.globalAlpha=.85;for(const s of[-1,1]){X.beginPath();X.moveTo(s*(w/2-2),-2);X.quadraticCurveTo(s*(w/2+12),-11,s*(w/2+16),-3);X.quadraticCurveTo(s*(w/2+9),-3,s*(w/2+13),3);X.quadraticCurveTo(s*(w/2+5),1,s*(w/2-2),4);X.fill()}X.globalAlpha=1}
 const g=X.createLinearGradient(0,-h/2,0,h/2);g.addColorStop(0,'#4a3618');g.addColorStop(.5,'#120c06');g.addColorStop(1,'#3a2a12');X.fillStyle=g;
 X.beginPath();X.moveTo(-w/2+6,-h/2);X.lineTo(w/2-6,-h/2);X.lineTo(w/2,0);X.lineTo(w/2-6,h/2);X.lineTo(-w/2+6,h/2);X.lineTo(-w/2,0);X.closePath();X.fill();
 X.lineWidth=1.6;X.strokeStyle=col;X.stroke();X.shadowBlur=0;X.lineWidth=.6;X.strokeStyle='rgba(255,240,200,.55)';X.beginPath();X.moveTo(-w/2+8,-h/2+2);X.lineTo(w/2-8,-h/2+2);X.lineTo(w/2-3,0);X.lineTo(w/2-8,h/2-2);X.lineTo(-w/2+8,h/2-2);X.lineTo(-w/2+3,0);X.closePath();X.stroke();
 for(const s of[-1,1]){X.fillStyle=col;X.beginPath();X.moveTo(s*(w/2+1),0);X.lineTo(s*(w/2-3),-3);X.lineTo(s*(w/2-7),0);X.lineTo(s*(w/2-3),3);X.fill();X.fillStyle='#fff';X.fillRect(s*(w/2-3)-.6,-.6,1.2,1.2)}
 if(hi>=6){X.fillStyle=col;X.beginPath();X.moveTo(-6,-h/2);X.lineTo(-6,-h/2-4);X.lineTo(-3,-h/2-2);X.lineTo(0,-h/2-6);X.lineTo(3,-h/2-2);X.lineTo(6,-h/2-4);X.lineTo(6,-h/2);X.fill()}
 X.textAlign='center';X.font='800 8.5px system-ui,sans-serif';const tg=X.createLinearGradient(0,-4,0,4);tg.addColorStop(0,'#fffbe8');tg.addColorStop(1,col);X.fillStyle=tg;X.fillText(txt,0,3.2);
 X.font='9px system-ui';X.fillText(ic,0,-h/2-(hi>=6?8:3));X.restore()}
function drawFights(t,z){for(const f of G.fights){const P=fightPow(f),pu=1+Math.sin(t*6)*.15;
 if(z<.42){X.strokeStyle='#ff4a3a';X.lineWidth=3/z;X.beginPath();X.arc(f.x,f.y,12*pu/z,0,7);X.stroke();X.font=`${15/z}px system-ui`;X.textAlign='center';X.fillStyle='#fff';X.fillText('⚔',f.x,f.y+5/z);continue}
 X.fillStyle='rgba(140,110,70,.28)';for(let i=0;i<7;i++){const a=t*1.5+i,r=18+((t*20+i*13)%24);E(X,f.x+Math.cos(a)*r,f.y+Math.sin(a)*r*.5,11,5)}
 X.strokeStyle='rgba(255,70,50,.9)';X.lineWidth=2.5;X.beginPath();X.ellipse(f.x,f.y,42*pu,17*pu,0,0,7);X.stroke();X.font='24px system-ui';X.textAlign='center';X.fillText('⚔️',f.x,f.y-34);
 const l=`${facN(f.af)} ${fmt(P.ta)} ⚔ ${fmt(P.td)} ${f.s>=0?S[f.s].name:facN(f.df)}`;X.font='bold 11px system-ui';const tw=X.measureText(l).width;X.fillStyle='rgba(70,12,6,.88)';X.fillRect(f.x-tw/2-6,f.y-80,tw+12,16);X.fillStyle='#fff';X.fillText(l,f.x,f.y-68);
 const k=P.sa/((P.sa+P.sd)||1);X.fillStyle='#ff5040';X.fillRect(f.x-42,f.y-61,84,5);X.fillStyle='#4aa3ff';X.fillRect(f.x-42,f.y-61,84*k,5)}}
function mmRect(){const sm=H<520,b=CWB(),w=Math.min(240,Math.max(120,W*(sm?.17:.22))),h=w*b.h/b.w;return{x:W-w-(sm?52:6),y:H-h-6,w,h}}
function clampCam(c){const hw=W/2/c.z,hh=H/2/c.z,b=G&&G.L?CWB():{x0:0,y0:0,w:WW,h:2*CH+GAP};c.x=b.w>hw*2?cl(c.x,b.x0+hw,b.x0+b.w-hw):b.x0+b.w/2;c.y=b.h>hh*2?cl(c.y,b.y0+hh,b.y0+b.h-hh):b.y0+b.h/2}
function drawMap(t){const c=MC;if(G&&c.follow){c.x=P0().x;c.y=P0().y}if(!G)c.x+=Math.sin(t*.1)*.3;clampCam(c);const z=c.z;
 X.setTransform(DPR,0,0,DPR,0,0);X.fillStyle='#1d4570';X.fillRect(0,0,W,H);
 X.setTransform(DPR*z,0,0,DPR*z,DPR*(W/2-c.x*z),DPR*(H/2-c.y*z));
 const vx0=c.x-W/2/z,vy0=c.y-H/2/z,vx1=c.x+W/2/z,vy1=c.y+H/2/z;
 
 X.imageSmoothingEnabled=true;X.drawImage(LOW,Math.max(0,vx0/40),Math.max(0,vy0/40),Math.min(LOW.width,vx1/40)-Math.max(0,vx0/40),Math.min(LOW.height,vy1/40)-Math.max(0,vy0/40),Math.max(0,vx0),Math.max(0,vy0),(Math.min(LOW.width,vx1/40)-Math.max(0,vx0/40))*40,(Math.min(LOW.height,vy1/40)-Math.max(0,vy0/40))*40);if(z>.1)for(let c=0;c<13;c++){const cv=BGC[c];if(!cv)continue;const ox=OX[c]-BGP,oy=OY[c]-BGP,a0=Math.max(vx0,ox),b0=Math.max(vy0,oy),a1=Math.min(vx1,ox+cv.width*BS),b1=Math.min(vy1,oy+cv.height*BS);if(a1<=a0||b1<=b0)continue;X.drawImage(cv,(a0-ox)/BS,(b0-oy)/BS,(a1-a0)/BS,(b1-b0)/BS,a0,b0,a1-a0,b1-b0)}
 if(G)for(let c=0;c<12;c++){if(OPEN(c))continue;if(OX[c]>vx1||OX[c]+CWc[c]<vx0||OY[c]>vy1||OY[c]+CHc[c]<vy0)continue;X.fillStyle=c>=9?'rgba(10,20,40,.82)':'rgba(18,6,36,.78)';X.fillRect(OX[c]-GAP/2,OY[c]-GAP/2,CWc[c]+GAP,CHc[c]+GAP);X.textAlign='center';X.font=`900 ${Math.min(CW/12,Math.max(40,34/z))}px system-ui`;X.fillStyle='#d9c2ff';X.fillText('🔒 '+RACE[c].n.toUpperCase(),OX[c]+CWc[c]/2,OY[c]+CHc[c]/2);X.font=`700 ${Math.min(CW/32,Math.max(18,15/z))}px system-ui`;X.fillText(LOCKT(c),OX[c]+CWc[c]/2,OY[c]+CHc[c]/2+Math.max(50,42/z));if(c>=5&&c<9){X.fillStyle='#9ff0ff';X.fillText('Sau đó chiếm 2/4 lục địa Thần linh → mở 🌀 Cửu Thiên Huyền Giới',OX[c]+CWc[c]/2,OY[c]+CHc[c]/2+Math.max(95,80/z))}}
 X.globalAlpha=z<.4?.85:.4;X.drawImage(TC,0,0,WW,WH);X.globalAlpha=1;
 if(z>(ULQ?.5:.22)){X.lineCap='round';for(const [w,col] of[[7,'rgba(90,66,36,.5)'],[3.5,'#c9ab78']]){X.strokeStyle=col;X.lineWidth=Math.max(w,w*.4/z);X.beginPath();for(const r of ROADS){X.moveTo(r[0],r[1]);X.quadraticCurveTo(r[2],r[3],r[4],r[5])}X.stroke()}}
 if(!ULQ&&z>(LOWQ?.55:.38)){const bx0=Math.max(0,vx0>>9),bx1=Math.min(BKX-1,vx1>>9),by0=Math.max(0,vy0>>9),by1=Math.min(BKY-1,(vy1+60)>>9);
  for(let j=by0;j<=by1;j++)for(let i=bx0;i<=bx1;i++){const idx=j*BKX+i;if(!DET[idx].length)continue;let cv=BKC.get(idx);
   if(!cv){cv=document.createElement('canvas');const S2=.75;cv.width=592*S2;cv.height=592*S2;const g=cv.getContext('2d'),X0=X;X=g;g.setTransform(S2,0,0,S2,(-(i<<9)+40)*S2,(-(j<<9)+60)*S2);const its=DET[idx];try{
  const pth=(f,st)=>{X.beginPath();for(const d of its)f(d);X.fillStyle=st;X.fill()};
  pth(d=>{if(d[3]==0){X.moveTo(d[0]+d[2]*1.5,d[1]+1);X.ellipse(d[0]+d[2]*.5,d[1]+1,d[2],d[2]*.4,0,0,7)}else if(d[3]==1){X.moveTo(d[0]-d[2],d[1]);X.lineTo(d[0]+d[2]*1.4,d[1]);X.lineTo(d[0]+d[2]*.2,d[1]-d[2]*.4)}},'rgba(0,0,0,.2)');
  pth(d=>{if(d[3]==1){X.moveTo(d[0]-d[2],d[1]);X.lineTo(d[0],d[1]-d[2]*1.3);X.lineTo(d[0],d[1])}},'#a49a8e');
  pth(d=>{if(d[3]==1){X.moveTo(d[0],d[1]-d[2]*1.3);X.lineTo(d[0]+d[2],d[1]);X.lineTo(d[0],d[1])}},'#776e64');
  pth(d=>{if(d[3]==1&&d[4]>.73){X.moveTo(d[0]-d[2]*.38,d[1]-d[2]*.8);X.lineTo(d[0],d[1]-d[2]*1.3);X.lineTo(d[0]+d[2]*.38,d[1]-d[2]*.8)}},'#f4f6f8');
  X.beginPath();for(const d of its)if(d[3]==2){const s=d[2];X.moveTo(d[0],d[1]);X.lineTo(d[0],d[1]-s*1.6);X.moveTo(d[0],d[1]-s*.9);X.lineTo(d[0]-s*.6,d[1]-s*1.4);X.moveTo(d[0],d[1]-s*1.2);X.lineTo(d[0]+s*.7,d[1]-s*1.7);X.moveTo(d[0]-s*.3,d[1]-s*1.15);X.lineTo(d[0]-s*.7,d[1]-s*1.2)}X.strokeStyle='#3e3530';X.lineWidth=1.6;X.lineCap='round';X.stroke();
  pth(d=>{if(d[3]==0)X.rect(d[0]-1,d[1]-d[2]*.5,2.2,d[2]*.6)},'#4a3020');
  pth(d=>{if(d[3]==0){X.moveTo(d[0]+d[2]*.85,d[1]-d[2]*.9);X.arc(d[0],d[1]-d[2]*.9,d[2]*.85,0,7)}},'#2c5622');
  pth(d=>{if(d[3]==0){X.moveTo(d[0]+d[2]*.3,d[1]-d[2]*1.1);X.arc(d[0]-d[2]*.25,d[1]-d[2]*1.1,d[2]*.55,0,7)}},'#3d7a2c')
   }finally{X=X0}BKC.set(idx,cv);if(BKC.size>70)BKC.delete(BKC.keys().next().value)}
   X.drawImage(cv,(i<<9)-40,(j<<9)-60,592,592)}}
 if(G&&G.mk){X.strokeStyle='rgba(255,220,100,'+cl(G.mk.t,0,1)+')';X.lineWidth=2/Math.min(1,z);X.beginPath();X.ellipse(G.mk.x,G.mk.y,10/Math.min(1,z),4/Math.min(1,z),0,0,7);X.stroke()}
 const vis=o=>o.x>vx0-90&&o.x<vx1+90&&o.y>vy0-90&&o.y<vy1+90;
 const ob=S.filter(s=>vis(s)&&OPEN(s.race)).map(s=>({y:s.y,d:()=>castle(s,t,z)}));if(z>(ULQ?.3:.16))for(const v of V)if(vis(v)&&OPEN(S[v.p].race))ob.push({y:v.y-1,d:()=>village(v,t,z)});if(G){const VP=G.L.filter(p=>!p.dead&&vis(p)&&(p.kind=='pl'||(z>.1&&OPEN(contOf(p.x,p.y))))),dense=VP.length>(ULQ?6:LOWQ?14:24)||(G.ngen||0)>=200,CS=Math.max(140,90/z),CL=new Map();
 const rfDot=tot(P0().t)>=20000;
 for(const p of VP){if(rfDot&&p.kind=='rf'){ob.push({y:p.y,d:()=>{const k=1/Math.min(1,z),r=3.5*k;X.fillStyle='#000';CI(X,p.x,p.y,r+1.2*k);X.fillStyle=p.to===0?'#7cc4ff':facC(p.fac);CI(X,p.x,p.y,r)}});continue}
  if(p.kind=='pl'||!dense||p.inF){ob.push({y:p.y+(p.kind=='pl'?.1:0),d:()=>party(p,t,z)});continue}
  const k=(p.fac)+'|'+Math.floor(p.x/CS)+'|'+Math.floor(p.y/CS);let c=CL.get(k);if(!c){c={n:0,m:0,x:0,y:0,fac:p.fac,k:0,ps:[]};CL.set(k,c)}c.n+=tot(p.t);c.m++;c.x+=p.x;c.y+=p.y;c.ps.push(p);if(p.kind=='king')c.k=1}
 for(const c of CL.values()){if(c.m==1){const p=c.ps[0];ob.push({y:p.y,d:()=>party(p,t,z)});continue}c.x/=c.m;c.y/=c.m;ob.push({y:c.y,d:()=>blob(c,z)})}}
 LBL.length=0;ob.sort((a,b)=>a.y-b.y).forEach(o=>o.d());
 {LBL.sort((a,b)=>a.p-b.p);const pl=[],mg=4/Math.min(1,z),cap=SMALL()?28:80;let n=0;const top=[];for(const L of LBL){if(L.p===0){top.push(L);continue}if(n>=cap&&L.p>1)break;if(pl.some(q=>L.x<q.x+q.w+mg&&L.x+L.w+mg>q.x&&L.y<q.y+q.h+mg&&L.y+L.h+mg>q.y))continue;pl.push(L);L.d();n++}top.forEach(L=>{const hit=pl.some(q=>L.x<q.x+q.w&&L.x+L.w>q.x&&L.y<q.y+q.h&&L.y+L.h>q.y);if(hit){X.save();X.translate(0,-62);L.d();X.restore()}else L.d()})}
 if(G&&G.xian&&G.portals)for(const q of G.portals){if(!vis(q))continue;const k=z<.42?1/z:1,pu=1+Math.sin(t*3)*.08;X.save();X.translate(q.x,q.y);X.scale(k,k);
  X.fillStyle='rgba(0,0,0,.3)';E(X,0,4,30,8);X.fillStyle='#3a3048';X.fillRect(-24,-46,7,46);X.fillRect(17,-46,7,46);X.fillRect(-26,-50,52,7);
  const gr=X.createRadialGradient(0,-22,2,0,-22,20);gr.addColorStop(0,'rgba(255,255,255,.95)');gr.addColorStop(.4,'rgba(150,220,255,.85)');gr.addColorStop(1,'rgba(120,60,255,.15)');X.fillStyle=gr;X.beginPath();X.ellipse(0,-22,16*pu,22*pu,0,0,7);X.fill();
  X.strokeStyle='rgba(200,240,255,.9)';X.lineWidth=2;X.beginPath();X.ellipse(0,-22,12*pu,17*pu,t*2,0,4.5);X.stroke();
  X.font='bold 11px system-ui';X.textAlign='center';X.lineWidth=3;X.strokeStyle='#000';const l=q.w?'🌀 Thông đạo về Thần giới':'🌀 Thông đạo Cửu Thiên Huyền Giới';X.strokeText(l,0,14);X.fillStyle='#bff2ff';X.fillText(l,0,14);X.restore()}
 if(G)drawFights(t,z);
 if(G){const kg=myKing();if(kg&&contOf(kg.x,kg.y)==PC()){const k=1/Math.min(1,z),pu=1+Math.sin(t*4)*.15;X.strokeStyle='#c58cff';X.lineWidth=3*k;X.beginPath();X.ellipse(kg.x,kg.y+1,24*k*pu,10*k*pu,0,0,7);X.stroke();
  const ay=kg.y-(z<.42?22:80)*k;X.font=`${22*k}px system-ui`;X.textAlign='center';X.fillText('👑',kg.x,ay);X.font=`900 ${11*k}px system-ui`;X.lineWidth=3*k;X.strokeStyle='#000';X.strokeText('VUA '+fmt(tot(kg.t)),kg.x,ay-22*k);X.fillStyle='#e6c8ff';X.fillText('VUA '+fmt(tot(kg.t)),kg.x,ay-22*k)}}
 if(G){const p=P0(),k=1/Math.min(1,z),pu=1+Math.sin(t*5)*.18;X.strokeStyle='#ffd23a';X.lineWidth=3*k;X.beginPath();X.ellipse(p.x,p.y+1,22*k*pu,9*k*pu,0,0,7);X.stroke();X.strokeStyle='rgba(255,210,58,.35)';X.lineWidth=8*k;X.stroke();
  const ay=p.y-(z<.42?22:74)*k-Math.abs(Math.sin(t*4))*6*k;X.fillStyle='#ffd23a';X.strokeStyle='#000';X.lineWidth=2*k;X.beginPath();X.moveTo(p.x-9*k,ay-12*k);X.lineTo(p.x+9*k,ay-12*k);X.lineTo(p.x,ay);X.closePath();X.fill();X.stroke();
  X.font=`900 ${12*k}px system-ui`;X.textAlign='center';X.lineWidth=3*k;X.strokeText('BẠN',p.x,ay-16*k);X.fillText('BẠN',p.x,ay-16*k)}
 X.textAlign='center';for(const m of mfx){if(!vis(m))continue;X.globalAlpha=cl(m.t,0,1);X.font=`bold ${Math.max(14,12/z)}px system-ui`;X.lineWidth=3/Math.min(1,z);X.strokeStyle='#000';X.strokeText(m.s,m.x,m.y);X.fillStyle=m.c;X.fillText(m.s,m.x,m.y);X.globalAlpha=1}
 if(!LOWQ&&z>.38)for(const cd of clouds){if(!vis({x:cd.x,y:cd.y}))continue;X.fillStyle='rgba(0,0,0,.07)';E(X,cd.x+40,cd.y+60,cd.r,cd.r*.45);X.fillStyle='rgba(255,255,255,.08)';E(X,cd.x,cd.y,cd.r,cd.r*.45);E(X,cd.x+cd.r*.4,cd.y-cd.r*.15,cd.r*.6,cd.r*.35)}
 X.textAlign='center';const fz=Math.min(CW/16,Math.max(26,22/z));X.font=`900 ${fz}px system-ui,sans-serif`;
 if(z<.12){X.font=`900 ${Math.min(CW/11,40/z)}px system-ui`;for(let c=0;c<NC();c++){const q={x:OX[c]+CWc[c]/2,y:OY[c]+CHc[c]*.12};X.lineWidth=8/z;X.strokeStyle='rgba(0,0,0,.7)';X.strokeText('🌍 '+RACE[c].n.toUpperCase(),q.x,q.y);X.fillStyle='#ffe9a8';X.fillText('🌍 '+RACE[c].n.toUpperCase(),q.x,q.y)}X.font=`900 ${fz}px system-ui,sans-serif`}
 for(const cc of CC){if(G&&cc.race!=PC())continue;if(cc.x<vx0-400||cc.x>vx1+400||cc.y<vy0-300||cc.y>vy1+300)continue;X.globalAlpha=z<.5?.95:.55;X.lineWidth=fz/5;X.strokeStyle='rgba(0,0,0,.7)';X.strokeText(cc.n.toUpperCase(),cc.x,cc.y-fz*1.2);X.fillStyle='#fff0c8';X.fillText(cc.n.toUpperCase(),cc.x,cc.y-fz*1.2);X.globalAlpha=1}
 if(G&&z<.65){const kz=Math.max(13,12/z);X.font=`800 ${kz}px system-ui,sans-serif`;const FA=new Map(),pc=PC();for(const s of S){if(s.race!=pc)continue;let a=FA.get(s.fac);if(!a)FA.set(s.fac,a=[0,0,0]);a[0]+=s.x;a[1]+=s.y;a[2]++}G.F.forEach((f,i)=>{if(f.dead)return;const a=FA.get(i);if(!a)return;const cx=a[0]/a[2],cy=a[1]/a[2];if(cx<vx0-300||cx>vx1+300||cy<vy0-200||cy>vy1+200)return;
  const l=`${relI(i)} ${f.n}`;X.lineWidth=kz/4;X.strokeStyle='rgba(0,0,0,.8)';X.strokeText(l,cx,cy-kz*2.5);X.fillStyle=rel(i);X.fillText(l,cx,cy-kz*2.5)})}
 X.setTransform(DPR,0,0,DPR,0,0);
 if(!LOWQ){if(!VG){VG=X.createRadialGradient(W/2,H/2,Math.min(W,H)*.45,W/2,H/2,Math.max(W,H)*.75);VG.addColorStop(0,'rgba(0,0,0,0)');VG.addColorStop(1,'rgba(0,0,0,.32)')}X.fillStyle=VG;X.fillRect(0,0,W,H)}
 if(G){const p=P0(),sx=(p.x-MC.x)*z+W/2,sy=(p.y-MC.y)*z+H/2;if(sx<0||sx>W||sy<0||sy>H){const a=Math.atan2(sy-H/2,sx-W/2),k2=Math.min(Math.abs((W/2-40)/Math.cos(a)),Math.abs((H/2-50)/Math.sin(a))),px=W/2+Math.cos(a)*k2,py=H/2+Math.sin(a)*k2;
  X.fillStyle='#ffd23a';X.strokeStyle='#000';X.lineWidth=2;X.save();X.translate(px,py);X.rotate(a);X.beginPath();X.moveTo(16,0);X.lineTo(-8,-11);X.lineTo(-8,11);X.closePath();X.fill();X.stroke();X.restore();X.font='bold 12px system-ui';X.textAlign='center';X.lineWidth=3;X.strokeText('📍 Bạn',px-Math.cos(a)*30,py-Math.sin(a)*22+4);X.fillText('📍 Bạn',px-Math.cos(a)*30,py-Math.sin(a)*22+4)}}
 {const kg=myKing();if(kg&&contOf(kg.x,kg.y)==PC()){const sx=(kg.x-MC.x)*z+W/2,sy=(kg.y-MC.y)*z+H/2;if(sx<0||sx>W||sy<0||sy>H){const a=Math.atan2(sy-H/2,sx-W/2),k2=Math.min(Math.abs((W/2-60)/Math.cos(a)),Math.abs((H/2-70)/Math.sin(a))),px=W/2+Math.cos(a)*k2,py=H/2+Math.sin(a)*k2;
  X.fillStyle='#c58cff';X.strokeStyle='#000';X.lineWidth=2;X.save();X.translate(px,py);X.rotate(a);X.beginPath();X.moveTo(16,0);X.lineTo(-8,-11);X.lineTo(-8,11);X.closePath();X.fill();X.stroke();X.restore();X.font='bold 12px system-ui';X.textAlign='center';X.lineWidth=3;X.strokeText('👑 Vua',px-Math.cos(a)*32,py-Math.sin(a)*22+4);X.fillText('👑 Vua',px-Math.cos(a)*32,py-Math.sin(a)*22+4)}}}
 if(!G)return;const m0=mmRect(),wb=CWB();X.fillStyle='#000';X.fillRect(m0.x-2,m0.y-2,m0.w+4,m0.h+4);X.drawImage(MMW[WRLD(P0().y)],m0.x,m0.y,m0.w,m0.h);
 const kx=m0.w/wb.w,ky=m0.h/wb.h,m={x:m0.x-wb.x0*kx,y:m0.y-wb.y0*ky,w:m0.w,h:m0.h};X.strokeStyle='rgba(255,255,255,.8)';X.lineWidth=1;X.strokeRect(m.x+vx0*kx,m.y+vy0*ky,(vx1-vx0)*kx,(vy1-vy0)*ky);
 X.font='bold 9px system-ui';X.textAlign='center';X.font='bold 10px system-ui';for(let c=0;c<NC();c++){if(CW_OF(c)!=WRLD(P0().y))continue;const q={x:OX[c]+CWc[c]/2,y:OY[c]+CHc[c]/2};X.lineWidth=3;X.strokeStyle='#000';X.strokeText(RACE[c].n,m.x+q.x*kx,m.y+q.y*ky);X.fillStyle='#fff0c8';X.fillText(RACE[c].n,m.x+q.x*kx,m.y+q.y*ky)}
 if(false)for(const cc of CC){X.lineWidth=3;X.strokeStyle='#000';X.strokeText(cc.n,m.x+cc.x*kx,m.y+cc.y*ky);X.fillStyle='#fff0c8';X.fillText(cc.n,m.x+cc.x*kx,m.y+cc.y*ky)}
 {const kg=myKing();if(kg){X.fillStyle='#c58cff';CI(X,m.x+kg.x*kx,m.y+kg.y*ky,3.5)}}X.fillStyle='#fff';CI(X,m.x+P0().x*kx,m.y+P0().y*ky,3.5);X.strokeStyle='#000';X.lineWidth=1;X.stroke();X.strokeStyle='#c9a052';X.strokeRect(m0.x-2,m0.y-2,m0.w+4,m0.h+4);
 // mũi tên chỉ hướng các nước nằm ngoài màn hình
 const aL=(ARW-performance.now())/1000;if(aL>0){X.globalAlpha=cl(aL,0,1);X.font='bold 11px system-ui';const cur=contOf(MC.x,MC.y),PTS=CC.filter(q=>q.race==cur).sort((a,b)=>dist(a,MC)-dist(b,MC)).slice(0,SMALL()?3:6);const PL=[],port=W<H*1.1;for(const cc of PTS){if((cc.x>vx0&&cc.x<vx1&&cc.y>vy0&&cc.y<vy1)||Math.hypot(cc.x-MC.x,cc.y-MC.y)<900)continue;const dx=cc.x-MC.x,dy=cc.y-MC.y,a=Math.atan2(dy,dx),hw=SMALL()?Math.max(60,W/2-80):W/2-140,hh=SMALL()?H/2-90:H/2-62,k=Math.min(Math.abs(hw/Math.cos(a)),Math.abs(hh/Math.sin(a)));
  const px=W/2+Math.cos(a)*k-30;let py=H/2+Math.sin(a)*k;if(px>m0.x-70&&py>m0.y-14)py=m0.y-16;if(PL.some(q=>Math.abs(q[1]-py)<24&&Math.abs(q[0]-px)<170))continue;PL.push([px,py]);const ci=CC.indexOf(cc),fs=G.F.filter(f=>(cc.cont?f.race==cc.race:f.cn==ci)&&!f.dead).map(f=>G.F.indexOf(f)),en=fs.some(f=>atWar(P0().fac,f)),my=fs.includes(P0().fac),col=my?'#7dff8a':en?'#ff6a5a':'#f2f2f2';
  const l=SMALL()?cc.n:`${cc.n} ${fmt(Math.hypot(dx,dy)/100)} dặm`,tw=X.measureText(l).width;X.fillStyle='rgba(15,10,6,.85)';X.fillRect(px-tw/2-8,py-10,tw+16,20);X.strokeStyle=col;X.lineWidth=1.5;X.strokeRect(px-tw/2-8,py-10,tw+16,20);X.fillStyle=col;X.fillText(l,px,py+4);
  X.save();X.translate(px+Math.cos(a)*(tw/2+18),py+Math.sin(a)*18);X.rotate(a);TRI(X,9,0,-5,-7,-5,7);X.restore()}X.globalAlpha=1}}
