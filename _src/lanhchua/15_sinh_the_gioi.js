function genWorld(){const RC=RACE[0],ox=OX[0],oy=OY[0],s0=S.length,cc0=CC.length;
 WREG.forEach((n,r)=>{const cs=WMD.C.filter(q=>q[1]==r);let x=0,y=0,m=0;for(const q of cs){const w=q[2].length;x+=q[2][0][0]*w;y+=q[2][0][1]*w;m+=w}CC.push({x:ox+x/m*20,y:oy+y/m*20,n,race:0})});
 const DIR=(dx,dy)=>{const a=Math.atan2(dy,dx)*180/Math.PI;return a<-157||a>157?'Tây':a<-112?'Tây Bắc':a<-67?'Bắc':a<-22?'Đông Bắc':a<22?'Đông':a<67?'Đông Nam':a<112?'Nam':'Tây Nam'};
 WMD.C.forEach((q,k)=>{const fi=F0.length,hue=(k*137.5)%360;F0.push({sur:q[0],n:q[0],cn:cc0+q[1],race:0,wm:q[1],c:`hsl(${hue|0},${55+(k%3)*12}%,${40+(k%4)*7}%)`});
  const cap={x:ox+q[2][0][0]*20,y:oy+q[2][0][1]*20},used={};WKS[k+1]=[];
  q[2].forEach((p,j)=>{const x=ox+p[0]*20,y=oy+p[1]*20;let nm=q[0];if(j){const d=DIR(x-cap.x,y-cap.y),b=d+' '+q[0];used[b]=(used[b]||0)+1;nm=used[b]>1?b+' '+used[b]:b}
   const o={id:S.length,name:nm,x,y,type:j==0?0:j<3?1:2,f0:fi,cn:cc0+q[1],race:0,fac:fi,own:-1,gar:null,pool:0};S.push(o);WKS[k+1].push(o)})});
 return s0}
function genCont(c){const ox=OX[c],oy=OY[c],RC=RACE[c],cs=[],f00=F0.length,s0=c==0&&WMAP?genWorld():S.length,CWx=CWc[c],CHx=CHc[c],WMx=c==0&&WMAP;
 if(!WMx){
 for(let tr=0;cs.length<5&&tr<40000;tr++){const x=ox+700+R()*(CWx-1400),y=oy+600+R()*(CHx-1200);if(okLand(x,y)&&cs.every(q=>Math.hypot(q.x-x,q.y-y)>(tr<20000?2100:1500)))cs.push({x,y,n:RC.cn[cs.length],race:c})}
 const cc0=CC.length;CC.push(...cs);
 cs.forEach((q,k0)=>{const ci=cc0+k0;for(let k=0;k<3;k++){const a=k*2.094+R(),sx=q.x+Math.cos(a)*520,sy=q.y+Math.sin(a)*420,fi=F0.length,sur=RC.sur[(fi-f00)%RC.sur.length];
  F0.push({sur,n:RC.pre+sur,cn:ci,race:c,c:`hsl(${RC.hue[k0]+(k-1)*14},${[70,60,75][k]}%,${[46,60,36][k]}%)`});
  for(let m=0;m<4;m++)for(let tr=0;tr<6000;tr++){const sp=300+tr*.25,x=sx+(R()-.5)*sp,y=sy+(R()-.5)*sp;
   if(x-ox<150||y-oy<150||x-ox>CWx-150||y-oy>CHx-150||!okLand(x,y))continue;if(S.some(s=>Math.hypot(s.x-x,s.y-y)<(tr>4000?120:180)))continue;
   S.push({id:S.length,name:unameR(c),x,y,type:m==0?0:m==1?1:2,f0:fi,cn:ci,race:c,fac:fi,own:-1,gar:null,pool:0});break}}});}
 const VN=['Thôn','Trang','Điền','Khê','Ấp','Hòa'];
 const SV=S.slice(s0),vs0=V.length,dS=WMx?62:110,dV=WMx?55:90;for(const s of SV)for(let k=0;k<2;k++)for(let tr=0;tr<(WMx?60:400);tr++){const a=R()*6.283,r=(WMx?80:140)+R()*(WMx?90:120)+tr*.3,x=s.x+Math.cos(a)*r,y=s.y+Math.sin(a)*r*.8;
  if(x-ox<100||y-oy<100||x-ox>CWx-100||y-oy>CHx-100||!okLand(x,y)||(WMx&&wmAt(x,y)!=wmAt(s.x,s.y))||SV.some(o=>Math.abs(o.x-x)<dS&&Math.abs(o.y-y)<dS&&Math.hypot(o.x-x,o.y-y)<dS)||V.some((o,ii)=>ii>=vs0&&Math.abs(o.x-x)<dV&&Math.hypot(o.x-x,o.y-y)<dV))continue;V.push({id:V.length,name:RC.vl+' '+RC.SA[R()*RC.SA.length|0]+' '+VN[R()*6|0],x,y,p:s.id,own:-1,pool:20,burn:0});break}
 const dn=new Set(),SS=S.slice(s0);for(const s of SS){SS.filter(o=>o!==s&&dist(o,s)<900&&(!WMx||(o.f0==s.f0||dist(o,s)<420)&&hW((o.x+s.x)/2,(o.y+s.y)/2)>.37)).sort((a,b)=>dist(a,s)-dist(b,s)).slice(0,2).forEach(o=>{const k=[s.id,o.id].sort().join();if(dn.has(k))return;dn.add(k);ROADS.push([s.x,s.y,(s.x+o.x)/2+(R()-.5)*160,(s.y+o.y)/2+(R()-.5)*160,o.x,o.y])})}}
genCont(0);for(let c=1;c<5;c++){NZ[c]=[noise(7,5),noise(19,12),noise(55,35),noise(30,19)];genCont(c)}
const SN0=S.length,VN0=V.length,CN0=CC.length,FN0=F0.length,RN0=ROADS.length;for(let c=5;c<9;c++){NZ[c]=[noise(7,5),noise(19,12),noise(55,35),noise(30,19)];genCont(c)}
const SN1=S.length,VN1=V.length,CN1=CC.length,FN1=F0.length,RN1=ROADS.length;for(let c=9;c<12;c++){NZ[c]=[noise(7,5),noise(19,12),noise(55,35),noise(30,19)];genCont(c)}
const DS2=S.splice(SN1),DV2=V.splice(VN1),DCC2=CC.splice(CN1),DF02=F0.splice(FN1),DR2=ROADS.splice(RN1);
const DS=S.splice(SN0),DV=V.splice(VN0),DCC=CC.splice(CN0),DF0=F0.splice(FN0),DR=ROADS.splice(RN0);
const WB=[{x0:0,y0:0,w:WW,h:2*CH+GAP},{x0:0,y0:2*(CH+GAP),w:3*CW+2*GAP,h:CH}],WRLD=y=>y>2*CH+1.5*GAP?1:0,CWB=()=>WB[G&&G.L?WRLD(P0().y):0];
const NC=()=>G&&G.xian?12:G&&G.divine?9:5;
const OPEN=c=>!G||!G.open?true:c>=9?!!G.xian:c>=5?!!G.divine:G.open.includes(c);
function unlockWorld2(){if(S.length>SN0+DS.length)return;unlockWorld();S.push(...DS2);V.push(...DV2);CC.push(...DCC2);F0.push(...DF02);ROADS.push(...DR2);nearFor(9)}
function unlockWorld(){if(S.length>SN0)return;S.push(...DS);V.push(...DV);CC.push(...DCC);F0.push(...DF0);ROADS.push(...DR);nearFor(5)}
const raceOf=p=>p.fac>=0&&G&&G.F[p.fac]?G.F[p.fac].race||0:contOf(p.x,p.y);
const BGC=[],BGP=300;
const DET=[];const BKX=Math.ceil(WW/512),BKY=Math.ceil(WH/512);for(let i=0;i<BKX*BKY;i++)DET.push([]);
const TCS=40,TC=document.createElement('canvas');TC.width=Math.ceil(WW/TCS);TC.height=Math.ceil(WH/TCS);const NEAR=new Int16Array(TC.width*TC.height).fill(-1);
const LOW=document.createElement('canvas');LOW.width=Math.ceil(WW/40);LOW.height=Math.ceil(WH/40);const baked=new Array(12).fill(0);
function pix(wx,wy,P){const hh=hW(wx,wy);let r,g,b;
 if(hh<.36){const k=cl((hh-.15)/.21,0,1);r=24+44*k;g=62+72*k;b=112+56*k;{const oc=contOf(wx,wy);if(oc==4&&(WMAP||wx>2*CW+1.5*GAP+250)){r=r*.55+18;g=g*.4;b=b*.6+10}else if(oc==7){r=r*.5+70;g=g*.35;b=b*.4+10}else if(oc==6){r=r*.6+60;g=g*.75+50;b=b*.8+50}}}
 else{const c=contOf(wx,wy),Q=P[c],f=fW(wx,wy);
  if(hh<.372){r=214;g=198;b=146}else if(hh>.68){if(hh>.78){r=236;g=238;b=242}else{const k=(hh-.68)/.1;r=128+40*k;g=118+38*k;b=104+42*k}}
  else{const k=(hh-.372)/.31;r=Q[0]-Q[3]*k;g=Q[1]-Q[4]*k;b=Q[2]-Q[5]*k;if(f>.6){r-=32;g-=28;b-=20}}
  const sh=cl((hh-hW(wx-10,wy-10))*2200,-34,34);r+=sh;g+=sh;b+=sh}return[r,g,b]}
const PAL=[[112,170,70,38,40,24],[118,150,92,40,30,20],[96,176,92,30,50,30],[120,140,64,40,30,20],[104,96,74,30,30,22],[150,138,104,40,36,26],[150,206,128,30,26,16],[118,52,44,40,24,20],[64,150,96,22,46,34],[124,190,140,30,40,30],[176,170,112,40,40,30],[96,72,112,30,26,30]];
function bakeLow(){const g=LOW.getContext('2d'),w=LOW.width,h=LOW.height,im=g.createImageData(w,h),d=im.data;
 for(let y=0;y<h;y++)for(let x=0;x<w;x++){const[r,gg,b]=pix(x*40+20,y*40+20,PAL),i=(y*w+x)*4;d[i]=r;d[i+1]=gg;d[i+2]=b;d[i+3]=255}g.putImageData(im,0,0);
 nearFor(0)}
function nearFor(c0){const tw=TC.width,SC=[];for(const s of S)(SC[s.race]||(SC[s.race]=[])).push(s);for(let j=0;j<TC.height;j++)for(let i=0;i<tw;i++){const x=i*TCS+20,y=j*TCS+20;const c=contOf(x,y);if(c<c0)continue;let L=SC[c]||[],lim=700000;if(c==0&&WMAP){const k=wmAt(x,y);if(!k&&hW(x,y)<.36)continue;if(k&&WKS[k]&&WKS[k].length){L=WKS[k];lim=1e12}}else if(hW(x,y)<.36)continue;let b=-1,bd=lim;for(const s of L){const dd=(s.x-x)**2+(s.y-y)**2;if(dd<bd){bd=dd;b=s.id}}NEAR[j*tw+i]=b}}
const BKC=new Map();
function bakeCont(c){if(baked[c])return;baked[c]=1;BKC.clear();const cv=document.createElement('canvas'),w=Math.ceil((CWc[c]+2*BGP)/BS),h=Math.ceil((CHc[c]+2*BGP)/BS);cv.width=w;cv.height=h;BGC[c]=cv;const bg=cv.getContext('2d'),x0=Math.floor((OX[c]-BGP)/BS),y0=Math.floor((OY[c]-BGP)/BS),im=bg.createImageData(w,h),d=im.data;
 for(let y=0;y<h;y++)for(let x=0;x<w;x++){const wx=(x0+x)*BS,wy=(y0+y)*BS;if(contOf(wx,wy)!=c)continue;const[r,g,b]=pix(wx,wy,PAL),n=((x*7919^y*104729)&7)-4,i=(y*w+x)*4;d[i]=r+n;d[i+1]=g+n;d[i+2]=b+n;d[i+3]=255}
 bg.putImageData(im,0,0);
 const i0=Math.floor(x0*BS/T),j0=Math.floor(y0*BS/T),i1=Math.min(GW,Math.ceil((x0+w)*BS/T)),j1=Math.min(GH,Math.ceil((y0+h)*BS/T));
 for(let j=j0;j<j1;j++)for(let i=i0;i<i1;i++){const x=i*T,y=j*T;if(contOf(x+T/2,y+T/2)!=c)continue;const hh=hW(x+T/2,y+T/2),t=hh<.36?0:hh<.372?4:hh>.68?3:fW(x+T/2,y+T/2)>.6?2:1;TER[j*GW+i]=t;
  if(t==0)continue;if(S.some(s=>Math.abs(s.x-x)<70&&Math.abs(s.y-y)<55)||V.some(v=>Math.abs(v.x-x)<45&&Math.abs(v.y-y)<35))continue;const bk=DET[(y>>9)*BKX+(x>>9)];
  if(t==3&&Math.random()<.55)bk.push([x+Math.random()*T,y+Math.random()*T,16+Math.random()*18,1,hh]);
  const tk=c==4||c==7?2:0;if(t==2)for(let k=0;k<(c==4||c==7?2:c==8?4:3);k++)bk.push([x+Math.random()*T,y+Math.random()*T,6+Math.random()*5,tk]);else if(t==1&&Math.random()<.06)bk.push([x+Math.random()*T,y+Math.random()*T,6+Math.random()*5,tk])}
 DET.forEach(b=>b.sort((a,q)=>a[1]-q[1]));terr()}
function bake(){bakeLow()}
let baking=0;function ensureCont(){if(!G||baking)return;const c=contOf(P0().x,P0().y);if(baked[c])return;baking=1;const L=document.createElement('div');L.id='load2';L.style.cssText='position:fixed;inset:0;display:flex;align-items:center;justify-content:center;font-size:18px;color:#ffd77a;background:rgba(20,16,8,.85);z-index:9';
 L.textContent=`🌍 Đang tải châu lục ${RACE[c].n}...`;document.body.appendChild(L);const first=!baked.some(x=>x);setTimeout(()=>{bakeCont(c);L.remove();baking=0;if(!first)toast(`🌍 Bạn đã đặt chân tới châu lục ${RACE[c].n}`,'#5cc9ff');showArrows(7)},40)}
const tAt=(x,y)=>TER[cl(y/T|0,0,GH-1)*GW+cl(x/T|0,0,GW-1)];
const MMW=[0,1].map(w=>{const c=document.createElement('canvas');c.width=300;c.height=w?Math.round(300*CH/(3*CW+2*GAP)):Math.round(300*(2*CH+GAP)/WW);return c}),MM=MMW[0];MM.height=Math.round(240*WH/WW);
let TD=0,tdT=0;function terr(){TD=1}
const CRGB=new Map(),CCX=document.createElement('canvas').getContext('2d');function rgbOf(c){let v=CRGB.get(c);if(!v){CCX.fillStyle='#000';CCX.fillStyle=c;const h=CCX.fillStyle;if(h[0]=='#')v=[parseInt(h.slice(1,3),16),parseInt(h.slice(3,5),16),parseInt(h.slice(5,7),16)];else{const m=h.match(/[\d.]+/g)||[0,0,0];v=[+m[0],+m[1],+m[2]]}CRGB.set(c,v)}return v}
function terrNow(){TD=0;const g=TC.getContext('2d'),w=TC.width,h=TC.height,own=NEAR;
 const FF=G?G.F:F0,me=G&&G.L?P0().fac:-9,rm=G&&G.L&&G.mm!='fac',im=g.createImageData(w,h),d=im.data;
 const SF=new Int32Array(S.length),SO=new Array(S.length),COL=[],MN=new Uint8Array(S.length);for(let k=0;k<S.length;k++){SF[k]=S[k].fac;SO[k]=S[k].own;MN[k]=G&&G.L&&S[k].own===0?1:0}
 const colOf=f=>{let c=COL[f];if(!c){c=COL[f]=rgbOf(rm?(f==me?'#36d65a':atWar(me,f)?'#ff2d2d':'#c9c9c9'):FF[f].c)}return c},GOLD=[255,210,58],WHT=[255,255,255];
 for(let j=0;j<h;j++)for(let i=0;i<w;i++){const q=j*w+i,o=own[q];if(o<0)continue;const f=SF[o];if(!FF[f])continue;
  const a=i>0?own[q-1]:-1,b=i<w-1?own[q+1]:-1,c=j>0?own[q-w]:-1,e=j<h-1?own[q+w]:-1;
  const fb=a<0||SF[a]!=f||b<0||SF[b]!=f||c<0||SF[c]!=f||e<0||SF[e]!=f,so=SO[o],ob=(a>=0&&a!=o&&SO[a]!=so)||(b>=0&&b!=o&&SO[b]!=so)||(c>=0&&c!=o&&SO[c]!=so)||(e>=0&&e!=o&&SO[e]!=so),mine=MN[o];
  let col,al;if(fb){col=colOf(f);al=.9}else if(ob){col=WHT;al=.4}else{al=mine?.5:rm?.3:.2;col=mine?GOLD:colOf(f)}
  const p=q*4;d[p]=col[0];d[p+1]=col[1];d[p+2]=col[2];d[p+3]=al*255|0}
 g.putImageData(im,0,0);
 g.globalAlpha=1;for(let w=0;w<2;w++){const b=WB[w],cv=MMW[w],m=cv.getContext('2d');m.clearRect(0,0,cv.width,cv.height);m.drawImage(LOW,b.x0/40,b.y0/40,b.w/40,b.h/40,0,0,cv.width,cv.height);m.globalAlpha=.8;m.drawImage(TC,b.x0/40,b.y0/40,b.w/40,b.h/40,0,0,cv.width,cv.height);m.globalAlpha=1}}
const clouds=Array.from({length:70},()=>({x:Math.random()*WW,y:Math.random()*WH,r:rnd(110,230),v:rnd(8,16)}));

/* ================= TRẠNG THÁI ================= */
const VINC=60,mfx=[];let G=null,mode='title',paused=false,B=null;
const MC={x:WW/2,y:WH/2,z:.2,follow:0},BC={x:0,y:0,z:1,follow:0};
const BAN=-1;
const P0=()=>G.L[0];
const atWar=(a,b)=>a==b?false:(a<0||b<0)?true:!!(G.war[a]&&G.war[a][b]);
const TT=[['Hiệp sĩ',400,'🛡','#a9b4bf',0,0],['Nam tước',1000,'🎖','#d08a43',1,300],['Tử tước',2000,'🏅','#d6dbe2',2,1000],['Bá tước',3500,'🥇','#ffcf3a',3,3000],['Hầu tước',6000,'💠','#5cc9ff',5,8000],['Công tước',9000,'⚜️','#ff86dd',8,20000]];
const CHT=[['Nhân Hoàng','☀️','#ffcf3a'],['Thạch Hoàng','⛰️','#ff9a4a'],['Tinh Hoàng','🌙','#7fe3ff'],['Lang Hoàng','🐺','#ff5a5a'],['Minh Hoàng','☠️','#d06cff'],['Titan Chí Tôn','🗿','#e8c27a'],['Thánh Chủ','👼','#fff6b0'],['Ma Thần Chí Tôn','👹','#ff3030'],['Vạn Yêu Chi Chủ','🦊','#8dff6a']];
const GODT=[['Titan Thần','🗿','#e0b878'],['Thiên Thần Vương','👼','#fff3a0'],['Quỷ Thần','👹','#ff4a3a'],['Yêu Thần','🦊','#7dff6a']];
const DIVT=[['Nhân Thần Đế','🌟','#fff07a'],['Sơn Thần Đế','💎','#ffb070'],['Tinh Linh Thần Đế','✨','#9ff0ff'],['Lang Thần Đế','🌕','#ff8080'],['Minh Thần Đế','🔮','#e090ff']];
const RK=['Lính đánh thuê','Hoàng tử vong quốc','Hiệp sĩ','Nam tước','Tử tước','Bá tước','Hầu tước','Công tước','Vương','Vua','Tử Vương','Hoàng đế','Ma Vương','Nhân Hoàng','Thạch Hoàng','Tinh Hoàng','Lang Hoàng','Minh Hoàng','Titan Thần','Thiên Thần Vương','Quỷ Thần','Yêu Thần','Titan Chí Tôn','Thánh Chủ','Ma Thần Chí Tôn','Vạn Yêu Chi Chủ','Nhân Thần Đế','Sơn Thần Đế','Tinh Linh Thần Đế','Lang Thần Đế','Minh Thần Đế','Trúc Cơ','Nguyên Anh','Địa Tiên','Nhân Tiên'];
function vills(p){let n=0;for(const v of V)if(v.own===p.id)n++;return n}
function fiefs(p){let n=0;for(const s of S)if(s.own===p.id)n++;return n}
function rank(p){if(p.kind=='bandit')return['Thủ lĩnh phỉ',700,'☠','#999'];if(p.kind=='rf')return['Viện binh',1e9,'➕','#9cf'];const f=G.F[p.fac];
  if(p.kind=='exile')return['Hoàng tử vong quốc',800,'🥀','#c9a8e0'];
 if(p.kind=='pl'&&G.divine&&isMyKing()){const r=DIVT[Math.min(4,(G.F[p.fac]&&G.F[p.fac].race)||0)];return[r[0],100000,r[1],r[2]]}
 if(f&&f.race>=9&&p.kind!='pl'){if(f.king===p.id){const n=S.filter(s=>s.fac==p.fac).length;return n>=5?['Nhân Tiên',150000,'☯️','#9ff0ff']:['Địa Tiên',100000,'🌄','#ffd27a']}return fiefs(p)?['Nguyên Anh',40000,'🔆','#c9a0ff']:['Trúc Cơ',20000,'🌱','#8fe08a']}
 if(f&&f.king===p.id&&f.race>=5){const r=GODT[f.race-5];return[r[0],12000,r[1],r[2]]}
 if(p.vuong&&p.kind=='lord')return['Vương',10000,'🏯','#ff8a3a'];
 if(f&&f.king===p.id&&G.ch){const c=G.ch.indexOf(p.fac);if(c>=0)return[CHT[c][0],40000,CHT[c][1],CHT[c][2]]}
 if(f&&f.king===p.id&&f.race==4)return G.mv===p.fac?['Ma Vương',20000,'😈','#c04cff']:['Tử Vương',12000,'💀','#9aa3b5'];
 if(f&&f.king===p.id)return f.emp?['Hoàng đế',20000,'🐉','#ff6a4a']:['Vua',12000,'👑','#ffd23a'];const n=fiefs(p)+Math.floor(vills(p)/2),rn=p.ren||0;if(p.merc&&!n&&rn<100)return['Lính đánh thuê',800,'🗡','#9aa0a8'];let r=TT[0];for(const t of TT)if(n>=t[4]||rn>=t[5])r=t;return r}
const badge=p=>{const r=rank(p);return`<span class="bdg" style="background:${r[3]}">${r[2]} ${r[0]}</span>`};
const pname=p=>p.kind=='exile'?`Hoàng tử ${p.name}`:p.kind=='pl'?`${rank(p)[0]} (Bạn)`:p.kind=='bandit'?'Thổ phỉ':p.kind=='rf'?p.name:`${rank(p)[0]} ${p.name}`;
const rel=f=>!G?'#fff':f==P0().fac?'#7dff8a':atWar(P0().fac,f)?'#ff6a5a':'#f2f2f2';
const relI=f=>!G?'':f==P0().fac?'★':atWar(P0().fac,f)?'⚔':'🕊';
function grantVillage(start){const pl=P0(),f=G.F[pl.fac];if(!f||f.king===0)return;const k=G.L[f.king];
 const c=V.filter(v=>v.own!==0&&S[v.p].fac==pl.fac&&!v.burn).sort((a,b)=>(a.own===f.king?0:1)-(b.own===f.king?0:1)||dist(a,S.find(s=>s.fac==pl.fac&&s.type==0)||pl)-dist(b,S.find(s=>s.fac==pl.fac&&s.type==0)||pl))[0];
 if(!c)return;c.own=0;toast(`🌾 ${k&&!k.dead?pname(k):'Nhà vua'} ban cho bạn đất phong:<br><b>${c.name}</b> (thuộc ${S[c.p].name})<br><small>Làng nộp vàng liên tục và tự gửi tân binh cho bạn</small>`,'#9be36b',1);addLog(`🌾 Được ban đất phong ${c.name}.`,'#9be36b')}
const facPow=i=>G.L.filter(p=>p.fac==i&&!p.dead).reduce((a,p)=>a+tot(p.t),0)+S.filter(s=>s.fac==i).reduce((a,s)=>a+tot(s.gar),0);
const myKing=()=>{if(!G)return null;const f=G.F[P0().fac],k=f&&G.L[f.king];return k&&k.kind!='pl'&&!k.dead?k:null};
function followKing(){const k=myKing(),pl=P0();if(!k){toast(isMyKing()?'Bạn chính là Vua!':'Vua của bạn hiện không còn','#ccc');return}close();stopPl();pl.goP=k;MC.follow=1;MC.z=Math.max(MC.z,.6);toast(`👑 Đang đi theo ${pname(k)} — tới gần sẽ cùng nhập trận`,'#c58cff')}
const isMyKing=()=>{const f=G.F[P0().fac];return f&&f.king===0};
const myGens=()=>G.L.filter(q=>q.kind=='lord'&&!q.dead&&q.fac==P0().fac);
const genCost=()=>1500+Math.min(myGens().length,30)*500;
const contsHeld=()=>{const f=P0().fac;let n=0;for(let c=0;c<5;c++){const ss=S.filter(s=>s.race==c);if(ss.filter(s=>s.fac==f).length>=ss.length*.6)n++}return n};
function crown(id){const g=G.L[id],pl=P0();if(!g||g.dead||!isMyKing())return;if(G.gold<5000){toast('Cần 5.000 vàng để phong Vương','#f88');return}G.gold-=5000;g.vuong=1;g.gold=g.gold||0;g.loy=Math.min(100,(g.loy??70)+15);
 toast(`🏯 Bạn phong ${g.name} làm VƯƠNG!`,'#ff8a3a',1);addLog(`Phong ${g.name} làm Vương.`,'#ffb070');panel('tg')}
const vPow=g=>tot(g.t)+S.filter(s=>s.own===g.id).reduce((a,s)=>a+tot(s.gar),0)+G.L.filter(q=>!q.dead&&q.lieg===g.id).reduce((a,q)=>a+tot(q.t),0);
function rebel(g){const pl=P0(),old=pl.fac,ni=G.F.length,R0=G.F[old];G.F.push({sur:g.name.split(' ')[0],n:'Vương quốc '+g.name,race:R0.race||0,cn:R0.cn,c:`hsl(${ri(0,359)},70%,50%)`,king:g.id,dead:0,emp:0});
 G.war.forEach((r,i)=>r.push(i==old?1:r[old]?1:0));G.war.push(G.F.map((f,i)=>i==ni?0:i==old?1:(G.war[old]&&G.war[old][i])?1:0));
 g.kind='king';g.fac=ni;g.vuong=0;S.forEach(s=>{if(s.own===g.id)s.fac=ni});G.L.forEach(q=>{if(!q.dead&&q.lieg===g.id){q.fac=ni;q.lieg=null}});
 terr();SFX.war();toast(`🔥 ${g.name} PHẢN LOẠN! Lập ${G.F[ni].n} với ${S.filter(s=>s.fac==ni).length} thành và tuyên chiến với bạn!`,'#ff4a3a',1);addLog(`🔥 ${g.name} phản loạn, lập ${G.F[ni].n}.`,'#ff6a5a')}
function vassalDay(){const pl=P0(),king=isMyKing(),pp=facPow(pl.fac),held=contsHeld();
 for(const g of G.L){if(g.dead||g.kind!='lord'||g.fac!=pl.fac)continue;if(g.loy==null)g.loy=ri(60,80);
  const tg=55+4*fiefs(g)+(G.gold>0?8:-25)-(g.vuong?12:0)+(G.call?3:0)-(vPow(g)>pp*.15?10:0);g.loy=cl(g.loy+(tg>g.loy?.6:-.6)+rnd(-.3,.3),0,100);
  if(g.vuong){g.gold=(g.gold||0)+S.filter(s=>s.own===g.id).length*150+60;const sub=G.L.filter(q=>!q.dead&&q.lieg===g.id).length;
   if(G.day%6==g.id%6&&g.gold>=2500&&sub<5){g.gold-=2500;const n=pushP({kind:'lord',name:newName(G.F[pl.fac]),fac:pl.fac,x:g.x+rnd(-30,30),y:g.y+30,t:mix(700),loy:ri(55,75),lieg:g.id,merc:1});if(contOf(g.x,g.y)==ACT&&Math.random()<.5)addLog(`🏯 Vương ${g.name} chiêu mộ tướng ${n.name}.`,'#ffb070')}
   if(king&&held>=4&&G.day%5==0&&g.loy<55&&vPow(g)>=pp/4){rebel(g);break}}}
 if(king&&G.autoGen&&G.day%3==0&&G.gold>=genCost()+2000){const g=hireGen(1);if(g){g.x=pl.x+rnd(-30,30);g.y=pl.y+30;g.tx=g.x;g.ty=g.y;toast(`🤖 Tự động chiêu mộ tướng ${g.name} (-${fmt(genCost())} vàng)`,'#9cf')}}}
function aiRecruit(){if(G.L.length>1800)return;for(let i=0;i<G.F.length;i++){const f=G.F[i];if(f.dead||i==P0().fac||f.king<0)continue;const ss=S.filter(s=>s.fac==i);if(!ss.length)continue;
 f.gold=(f.gold||0)+ss.length*60;const n=G.L.filter(q=>!q.dead&&q.fac==i&&q.kind=='lord').length,cost=2500+n*150;
 if(f.gold>=cost&&n<ss.length+2&&G.day%6==i%6){f.gold-=cost;const cap=ss.find(s=>s.type==0)||ss[0];pushP({kind:'lord',name:newName(f),fac:i,x:cap.x+rnd(-30,30),y:cap.y+rnd(25,45),t:mix(f.race>=9?ri(15000,30000):ri(500,900))})}}}
function hireMaxN(){let g=G.gold,n=myGens().length,k=0;while(k<200){const c=1500+Math.min(n,30)*500;if(g<c)break;g-=c;n++;k++}return k}
function hireMax(){const pl=P0(),k=hireMaxN();for(let i=0;i<k;i++){const g=hireGen(1);if(g){g.x=pl.x+rnd(-40,40);g.y=pl.y+rnd(20,50);g.tx=g.x;g.ty=g.y}}addLog(`Chiêu mộ ${k} tướng.`,'#8f8');save();return k}
function hireGen(q){const pl=P0(),cost=genCost();if(G.gold<cost){toast(`Cần ${fmt(cost)} vàng để chiêu mộ tướng`,'#f88');return}
 const s=pl;G.gold-=cost;
 const g=pushP({kind:'lord',name:SUR[ri(0,SUR.length-1)]+' '+GIV[ri(0,GIV.length-1)],fac:pl.fac,x:s.x+rnd(-20,20),y:s.y+30,t:mix(800),ren:0,merc:1,loy:ri(60,80)});if(q)return g;
 toast(`🧑‍✈️ Tướng ${g.name} cùng 800 quân gia nhập dưới trướng bạn!`,'#7dff8a');addLog(`Chiêu mộ tướng ${g.name} (-${fmt(cost)} vàng).`,'#8f8');save()}
function checkRank(){const pl=P0(),r=rank(pl)[0];if(r==G.lastRank)return;const up=RK.indexOf(r)>RK.indexOf(G.lastRank);G.lastRank=r;if(!up)return;
 const k=G.F[pl.fac]&&G.L[G.F[pl.fac].king],by=k&&k!==pl&&!k.dead?`${pname(k)} ban sắc phong`:'Thiên hạ tôn xưng';
 toast(`📜 SẮC PHONG<br>${by}:<br>${badge(pl)}<br><small>Quân tối đa ${fmt(rank(pl)[1])}</small>`,rank(pl)[3],1);setTimeout(grantVillage,2500);addLog(`🎖 Bạn được phong ${r}!`,'#ffd65a')}
const facN=f=>f<0?'Thổ phỉ':G.F[f].n;const facC=f=>f<0?'#777':(G?G.F:F0)[f].c;
