/* ================= 23 TẦNG TRỜI + TIÊN GIỚI =================
 Một "ô thế giới" (châu lục số 12) ở hàng dưới cùng của bản đồ, tái sinh theo từng tầng.
 Tầng đã chiếm 2/3 thì khóa lại thành lãnh thổ ổn định (chỉ cộng thu nhập), ô thế giới sinh tầng mới. */
const TLD=`Thanh Minh Thiên|Phong Tộc|🌪|Phong bộ |Phong Đế|Phong Hầu|Phong Sứ|Phong,Lam,Vân,Khinh,Toàn,Phiêu,Thanh,Lưu|120,190,170,30,40,30|.8,1,1.1|Gió bão không bao giờ ngừng thổi, cả đại lục trôi giữa biển mây.
Lôi Âm Thiên|Lôi Tộc|⚡|Lôi bộ |Lôi Đế|Lôi Hầu|Lôi Tướng|Lôi,Điện,Chấn,Tử,Cửu,Thiên,Oanh,Bôn|110,120,150,30,30,40|.7,.7,1.2|Sấm sét giáng xuống ngày đêm, người Lôi tộc tắm mình trong thiên kiếp.
Hỏa Vân Thiên|Viêm Tộc|🔥|Viêm bộ |Viêm Đế|Viêm Hầu|Hỏa Sứ|Viêm,Hỏa,Xích,Liệt,Chu,Dung,Diệm,Nham|170,110,70,40,40,30|1.4,.6,.5|Biển mây bốc lửa, dung nham chảy thành sông giữa trời.
Băng Phách Thiên|Băng Tộc|❄️|Băng cung |Băng Hoàng|Hàn Hầu|Tuyết Sứ|Băng,Hàn,Tuyết,Sương,Lãnh,Ngọc,Tinh,Phách|200,215,225,40,40,30|.8,1,1.3|Vạn dặm băng nguyên, một hơi thở cũng đóng thành băng.
Thanh Mộc Thiên|Mộc Linh Tộc|🌳|Mộc tộc |Mộc Thần Vương|Thụ Hầu|Diệp Sứ|Mộc,Diệp,Lâm,Thụ,Thanh,Bích,Linh,Đằng|70,150,60,20,50,20|.7,1.1,.8|Cổ thụ cao tận trời, mỗi gốc cây là một tòa thành.
Kim Cang Thiên|Kim Thân Tộc|🛡|Kim thân |Kim Cang Đế|Kim Hầu|Kim Vệ|Kim,Cương,Thiết,Ngân,Đồng,Chân,Bảo,Phong|190,170,110,40,40,30|1.1,1,.7|Thân thể bất hoại, đao kiếm chém vào chỉ tóe lửa.
Hậu Thổ Thiên|Thạch Nhân Tộc|🪨|Thạch tộc |Thổ Hoàng|Nham Hầu|Thạch Vệ|Thổ,Thạch,Nham,Sơn,Hoàng,Hậu,Khôn,Trầm|160,130,90,40,40,30|1,.9,.7|Đại địa trôi nổi giữa trời, núi non biết đi.
Bích Hải Thiên|Hải Tộc|🌊|Hải tộc |Hải Hoàng|Triều Hầu|Lãng Sứ|Hải,Lam,Triều,Lãng,Thủy,Ba,Uyên,Bích|90,170,160,30,40,40|.6,1,1.3|Trời là biển, biển là trời — chiến hạm bay trên sóng mây.
Long Uyên Thiên|Long Tộc|🐉|Long tộc |Long Hoàng|Long Quân|Long Vệ|Long,Ngao,Uyên,Thanh,Xích,Hắc,Kim,Ứng|100,150,110,30,40,30|.7,1,1|Vực sâu vạn trượng, nơi Long tộc vừa tỉnh giấc. Long Hoàng thì thầm: Thiên Đình đã để mắt tới ngươi…
Phượng Minh Thiên|Phượng Tộc|🦚|Phượng tộc |Phượng Hoàng|Phượng Quân|Loan Sứ|Phượng,Loan,Hoàng,Đan,Thải,Vũ,Xích,Minh|190,130,90,40,40,30|1.3,.8,.6|Lửa niết bàn không tắt, Phượng tộc chết đi lại hồi sinh.
Kỳ Lân Thiên|Lân Tộc|🦄|Lân tộc |Lân Hoàng|Lân Quân|Lân Vệ|Lân,Kỳ,Thụy,Tường,Ngọc,Cát,Nhân,Hòa|140,180,120,30,40,30|.9,1.1,.9|Thụy thú cai quản — kẻ ác bước vào sẽ bị thiên phạt.
Huyền Vũ Thiên|Quy Xà Tộc|🐢|Huyền tộc |Huyền Vũ Đế|Quy Hầu|Xà Vệ|Huyền,Quy,Xà,Thủy,Bắc,Minh,Hắc,Trấn|80,110,110,30,30,30|.6,.8,1.2|Thành trì dựng trên lưng rùa thần — phòng thủ vững nhất cửu thiên.
Bạch Hổ Thiên|Hổ Tộc|🐅|Hổ tộc |Bạch Hổ Đế|Hổ Quân|Hổ Vệ|Hổ,Bạch,Sát,Kim,Tây,Phong,Khiếu,Uy|170,160,130,40,40,30|1,1,1|Sát khí ngút trời, chiến binh Hổ tộc chỉ biết tiến không lùi.
Tinh Thần Thiên|Tinh Không Tộc|✨|Tinh tộc |Tinh Đế|Tinh Quân|Tinh Sứ|Tinh,Thần,Đẩu,Khôi,Ngân,Hà,Thiên,Diệu|90,90,150,30,30,40|.5,.5,1.1|Đất liền lơ lửng giữa dải ngân hà, sao trời rơi như mưa.
Nguyệt Hoa Thiên|Nguyệt Tộc|🌙|Nguyệt cung |Nguyệt Hoàng|Nguyệt Quân|Thiềm Sứ|Nguyệt,Hằng,Quế,Thiềm,Ngân,Lãnh,Hoa,Thanh|170,180,200,40,40,40|.8,.9,1.2|Đêm vĩnh hằng dưới vầng trăng khổng lồ.
Thái Dương Thiên|Kim Ô Tộc|☀️|Kim Ô |Dương Đế|Ô Quân|Nhật Sứ|Kim,Ô,Dương,Nhật,Hi,Diệu,Quang,Xích|200,170,90,40,40,30|1.3,1.1,.6|Mười mặt trời cùng mọc, chỉ kẻ mạnh mới không tan thành tro.
Huyễn Mộng Thiên|Huyễn Tộc|🎭|Huyễn tộc |Mộng Đế|Huyễn Quân|Ảo Sứ|Huyễn,Mộng,Ảo,Mê,Kính,Hoa,Thủy,Hư|170,130,180,40,30,40|1.1,.8,1.2|Thật giả khó phân — có kẻ đánh trăm năm mới biết mình đang trong mộng.
Tu La Thiên|Tu La Tộc|👺|Tu La |Tu La Vương|Sát Quân|Chiến Quỷ|Tu,La,Huyết,Chiến,Sát,Cuồng,Ma,Ngục|130,70,60,40,30,20|1.3,.5,.5|Chiến trường bất tận, Tu La sống chỉ để chém giết.
Cự Linh Thiên|Cự Linh Thần Tộc|🗿|Cự Linh |Cự Linh Đế|Cự Thần|Cự Vệ|Cự,Linh,Thần,Bàn,Sơn,Hồng,Hoang,Vạn|150,140,110,40,40,30|1,.95,.85|Người khổng lồ cao vạn trượng, một bước chân rung chuyển tầng trời.
Vu Thần Thiên|Vu Tộc|🔮|Vu tộc |Tổ Vu|Đại Vu|Vu Sư|Vu,Tổ,Hậu,Chúc,Cộng,Huyền,Cú,Đế|120,90,120,30,30,30|.9,.6,1|Mười hai Tổ Vu từng đối đầu Yêu Đình — nay hậu duệ của họ vẫn chờ báo thù.
Thời Không Thiên|Thời Không Tộc|⏳|Thời tộc |Thời Không Đế|Thời Quân|Không Sứ|Thời,Không,Luân,Hồi,Vĩnh,Tịch,Hư,Kỷ|150,160,170,30,40,40|.9,.9,1|Quá khứ và tương lai đan xen — thành chiếm hôm nay có thể mất từ hôm qua.
Hỗn Độn Thiên|Hỗn Độn Ma Thần|🌑|Hỗn Độn |Ma Thần Tổ|Ma Thần|Hỗn Độn Thú|Hỗn,Độn,Hư,Vô,Hoang,Thái,Sơ,Diệt|90,70,100,30,30,30|.5,.4,.7|Nơi trời đất chưa phân, ma thần nguyên thủy còn say ngủ.
Đại La Thiên|Đại La Thiên Binh|☯️|Đại La |Đại La Thiên Tôn|Kim Tiên|Thiên Binh|Đại,La,Thái,Thanh,Ngọc,Thượng,Nguyên,Đạo|180,200,180,40,40,30|1,1.05,1.1|Cổng trời cuối cùng — mười vạn thiên binh canh giữ lối vào TIÊN GIỚI.`.split('\n').map(l=>{const a=l.split('|');return{n:a[0],r:a[1],ic:a[2],pre:a[3],kt:a[4],ft:a[5],lt:a[6],SA:a[7].split(','),pal:a[8].split(',').map(Number),sea:a[9].split(',').map(Number),rm:a[10]}});
const TG_K=[['Thiên Đình','Ngọc Hoàng Thượng Đế','Thác Tháp Thiên Vương','Nhị Lang Chân Quân'],['Tây Thiên Linh Sơn','Như Lai Phật Tổ','Quan Âm Bồ Tát','Văn Thù Bồ Tát'],['Đông Hải Long Cung','Đông Hải Long Vương','Nam Hải Long Vương','Bắc Hải Long Vương'],['Yêu Đình','Yêu Hoàng Đế Tuấn','Đông Hoàng Thái Nhất','Bạch Trạch Yêu Sư'],['Ma Giới','Ma Tổ La Hầu','Huyết Hải Minh Hà','Thiên Ma Ba Tuần'],['Địa Phủ U Minh','Thập Điện Diêm La','Địa Tạng Vương','Phong Đô Đại Đế'],['Bồng Lai Tiên Đảo','Đông Hoa Đế Quân','Bát Tiên Động Phủ','Bồng Lai Tán Nhân'],['Côn Lôn Tiên Sơn','Tây Vương Mẫu','Nguyên Thủy Thiên Tôn','Thái Thượng Lão Quân'],['Bích Du Cung','Thông Thiên Giáo Chủ','Đa Bảo Đạo Nhân','Kim Linh Thánh Mẫu'],['Hồng Hoang Cổ Địa','Hồng Quân Lão Tổ','Bàn Cổ Di Tộc','Nữ Oa Cung']];
const TNX=['Tiêu','Minh','Vân','Phong','Cực','Hư'],TGN=['Tử','Quân','Tôn','Kiếm','Hà','Thần','Đạo','Dương','Vân','Phong','Hải','Vũ','Viêm','Uyên'],TKG=['Thiên Cung','Thần Vực','Đế Đô','Thánh Địa','Bảo Điện'];
const TMv=n=>1+((n||(G&&G.tang)||1)-1)*.12;
const PW=r=>LKM()*(r==12&&G&&G.tang?TMv():1);
const TINFO=n=>n>=24?{n:'Tiên Giới',r:'Chư Thần Tiên Giới',ic:'🏯',rm:'Tiên giới chính thống — Thiên Đình, Tây Thiên, Long Cung, Yêu Đình, Ma Giới, Địa Phủ… thống nhất Tiên Giới để đăng cơ ĐẠI ĐẾ.'}:TLD[n-1];
const SN2=SN0+DS.length+DS2.length,VN2=VN0+DV.length+DV2.length,CN2=CN0+DCC.length+DCC2.length,FN2=FN0+DF0.length+DF02.length,RN2=RN0+DR.length+DR2.length;
let TCUR=0;const UN0=new Set(usedN);
function tRace(n){const T=n>=24;if(T){return{n:'Tiên Giới',pre:'',cn:TG_K.map(k=>k[0]),hue:[48,30,195,120,0,270,175,90,300,20],sur:TG_K.flatMap(k=>k.slice(1)),
  giv:['Na Tra','Dương Tiễn','Thiên Bồng','Quyển Liêm','Thái Bạch','Cự Linh','Lôi Công','Điện Mẫu','Ngao Quảng','Khổng Tuyên','Triệu Công Minh','Văn Trọng','Quảng Thành Tử','Xích Tinh Tử','Hằng Nga','Thanh Hư','Huyền Đô','Vân Tiêu','Kim Linh','Đa Bảo'],
  SA:['Thiên','Tiên','Ngọc','Thần','Linh','Thánh','Bảo','Kim','Vân','Hư'],SB:['Tiên Cung','Bảo Điện','Thiên Môn','Linh Đài','Tiên Phủ','Thần Các','Kim Khuyết'],vl:'Tiên hương',
  st:{hp:1.4,atk:1.4,sp:1.2,rng:1.2,h:1.1},wall:'#fff4cc',kt:'Chí Tôn',ft:'Đại La Kim Tiên',lt:'Thiên Tướng',ic:'🏯',pal:[150,200,130,30,40,30],sea:[.9,1,1.15],hc:'#f6e3c8',bd:'#fff6d8',cpf:4}}
 const L=TLD[n-1],SA=L.SA,k=1+n*.015;return{n:`Tầng ${n} · ${L.n}`,pre:L.pre,cn:[0,1,2,3,4,5].map(i=>SA[i]+' '+TKG[i%5]),hue:[0,1,2,3,4,5].map(i=>(n*47+i*60)%360),
  sur:Array.from({length:18},(_,i)=>SA[(i*3+1)%8]+' '+TNX[(i+n)%6]),giv:Array.from({length:20},(_,i)=>SA[i%8]+' '+TGN[(i*5+n)%TGN.length]),SA,SB:['Thiên Cung','Thần Điện','Linh Đài','Bảo Tháp','Tiên Phủ','Vân Các','Đạo Cung'],vl:'Linh thôn',
  st:{hp:k,atk:k,sp:1.1,rng:1.1,h:1.05},wall:'#e8e2d0',kt:L.kt,ft:L.ft,lt:L.lt,ic:L.ic,pal:L.pal,sea:L.sea,hc:'#f0d2b0',bd:'#e6e6f0',cpf:4}}
function genTangWorld(n){const sd0=sd;sd=9001+n*7919;const T=n>=24;
 unlockWorld2();usedN.clear();UN0.forEach(x=>usedN.add(x));S.length=SN2;V.length=VN2;CC.length=CN2;F0.length=FN2;ROADS.length=RN2;
 CWc[12]=3*CW+2*GAP;CHc[12]=T?2*CH+GAP:CH;OX[12]=0;OY[12]=3*(CH+GAP);WB[2].w=CWc[12];WB[2].h=CHc[12];
 const MC2=MMW[2];MC2.width=300;MC2.height=Math.round(300*CHc[12]/CWc[12]);
 RACE[12]=tRace(n);RIC[12]=RACE[12].ic;PAL[12]=RACE[12].pal;CHT[12]=['Chúa tể '+(T?'Tiên Giới':TLD[n-1].n),RACE[12].ic,'#fff2a8'];
 NZ[12]=T?[noise(10,6),noise(26,16),noise(70,44),noise(40,26)]:[noise(9,3),noise(24,8),noise(66,22),noise(36,12)];
 genCont(12);
 if(BGC[12]){BGC[12].width=BGC[12].height=0;BGC[12]=null}baked[12]=0;
 const yb=Math.floor((3*CH+2*GAP)/512);for(let by=yb;by<BKY;by++)for(let bx=0;bx<BKX;bx++)DET[by*BKX+bx].length=0;
 for(let j=Math.floor((3*CH+2*GAP)/T0());j<GH;j++)TER.fill(0,j*GW,(j+1)*GW);
 bakeLowRect(OY[12]-GAP/2,WH);nearFor(12);TCUR=n;sd=sd0}
const T0=()=>T;
function bakeLowRect(ya,yb){const g=LOW.getContext('2d'),w=LOW.width,y0=Math.max(0,Math.floor(ya/40)),y1=Math.min(LOW.height,Math.ceil(yb/40)),h=y1-y0;if(h<=0)return;const im=g.createImageData(w,h),d=im.data;
 for(let y=0;y<h;y++)for(let x=0;x<w;x++){const[r,gg,b]=pix(x*40+20,(y0+y)*40+20,PAL),i=(y*w+x)*4;d[i]=r;d[i+1]=gg;d[i+2]=b;d[i+3]=255}g.putImageData(im,0,y0)}
/* phe của tầng mới: dùng lại ô phe cũ của tầng trước để danh sách phe không phình ra */
function tangFacs(){const pl=P0(),me=pl.fac;G.cmap=G.cmap||{};const list=[];
 const KK=[];for(let k=FN2;k<F0.length;k++){let ni=G.cmap[k];if(ni==null){ni=G.F.length;G.cmap[k]=ni;G.F.push(null)}
  G.F[ni]={...F0[k],king:-1,dead:0,emp:0,heirs:ri(1,3)};list.push(ni);KK.push([ni,k])}
 const N=G.F.length;G.war.forEach(r=>{while(r.length<N)r.push(0)});while(G.war.length<N)G.war.push(new Array(N).fill(0));
 for(const i of list){G.war[i].fill(0);G.war.forEach(r=>r[i]=0)}
 const used=new Set(list);for(let i=0;i<N;i++)if(G.F[i]&&G.F[i].race==12&&!used.has(i)){G.F[i].dead=1}
 for(const [i,k] of KK)setupFac(i,k);
 for(const i of list){G.war[i][me]=G.war[me][i]=1}initWar(list);extraWar(list);
 for(const i of list)for(const j of list)if(i!=j&&Math.random()<.25)G.war[i][j]=G.war[j][i]=1;
 if(G.ch)G.ch[12]=-1}
function tangLand(){const ss=S.filter(s=>s.race==12).sort((a,b)=>a.x-b.x),s=ss[0];const p=s?landNear(s):{x:OX[12]+800,y:OY[12]+CHc[12]/2};return p}
let TGO=0;function tangGo(n,first){if(TGO)return;TGO=1;const pl=P0(),me=pl.fac,inSlot=p=>contOf(p.x,p.y)==12;
 const L=document.createElement('div');L.id='load2';L.style.cssText='position:fixed;inset:0;display:flex;align-items:center;justify-content:center;font-size:18px;color:#ffe9a8;background:rgba(8,10,24,.9);z-index:9;text-align:center;padding:20px';
 L.innerHTML=`${n>=24?'🏯':'🌌'} Đang mở ${n>=24?'<b>TIÊN GIỚI</b>':'<b>Tầng '+n+' · '+TLD[n-1].n+'</b>'}...`;document.body.appendChild(L);const pp=paused;paused=true;
 setTimeout(()=>{try{
  let cr=null;if(!first){const gs=G.L.filter(q=>!q.dead&&q.kind=='lord'&&q.fac==me);let best=null,bf=0;for(const g of gs){const f=S.filter(s=>s.race==12&&s.own===g.id).length;if(f){g.ren=(g.ren||0)+f*2500;if(f>bf){bf=f;best=g}}}
   const pf=S.filter(s=>s.race==12&&s.own===0).length;if(best&&bf>=pf)cr=[best,bf]}
  for(const q of G.L){if(q.dead||q.fac==me||q.kind=='pl')continue;if(inSlot(q)||(G.F[q.fac]&&G.F[q.fac].race==12)){q.dead=-1;q.t=Z3();q.goS=q.goP=null}}
  G.fights=(G.fights||[]).filter(f=>!(contOf(f.x,f.y)==12||(f.s>=0&&S[f.s]&&S[f.s].race==12)));
  for(const q of G.L)if(!q.dead){if(q.goS&&q.goS.race==12)q.goS=null;q.inF=0}
  const mov=G.L.filter(q=>!q.dead&&q.fac==me&&(q.kind=='pl'||(q.kind=='lord'&&(inSlot(q)||!S.some(s=>s.own===q.id)))));
  if(!first){G.tdone=(G.tdone||0)+1}G.tang=n;G.tease=0;genTangWorld(n);tangFacs();
  const p=tangLand();for(const q of mov){q.x=p.x+(q.kind=='pl'?0:rnd(-120,120));q.y=p.y+(q.kind=='pl'?0:rnd(-80,80));q.tx=q.x;q.ty=q.y;q.goS=q.goP=null;q.safe=8}
  MC.follow=1;sanitize();terr();
  const I=TINFO(n),nx=n<24?TINFO(n+1):null;
  if(cr)setTimeout(()=>toast(`🙇 Đại tướng <b>${pname(cr[0])}</b> đã tự mình bình định ${cr[1]} thành của Tầng ${n-1} — công lao vượt cả Chí Tôn!<br>Hắn quỳ dâng toàn bộ lãnh thổ, tôn bạn là <b>CỬU NGŨ CHÍ TÔN</b>.`,'#ffe066',1),5600);
  toast(`${I.ic} ${n>=24?'<b>TIÊN GIỚI</b> HIỆN RA!':(first?'⚡ PHI THĂNG! 23 TẦNG TRỜI MỞ RA<br>':'')+`<b>TẦNG ${n} · ${I.n.toUpperCase()}</b>`}<br>${I.r} cai quản. ${I.rm}<br><small>${n<24?`Chiếm 2/3 thành để lên tầng ${n+1}. Phía trên chỉ toàn mây mù… chiếm 1/2 để dò thám.`:'Chiếm 2/3 Tiên Giới để đăng cơ ĐẠI ĐẾ.'}${G.tdone?` · ${G.tdone} tầng đã bình định nộp cống ${fmt(tribute())} vàng/ngày`:''}</small>`,'#d8c8ff',1);
  addLog(`${I.ic} ${n>=24?'Tiến vào Tiên Giới':'Phi thăng tới Tầng '+n+' · '+I.n}.`,'#d8c8ff');SFX.fan();setTimeout(()=>SFX.war(),900)}catch(e){console.error(e)}
  L.remove();paused=pp;TGO=0;save()},60)}
const tribute=()=>(G&&G.tdone||0)*800*LKM();
function tangCheck(){if(!G.lk||TGO)return;const pl=P0();
 if(!G.tang){if([9,10,11].filter(c=>held(c)>=.67).length>=2)tangGo(1,1);return}
 const h=held(12);
 if(h>=.5&&G.tease!=G.tang){G.tease=G.tang;if(G.tang<24){const I=TINFO(G.tang+1);toast(`🔮 Thám tử vén mây trở về:<br>Phía trên là <b>${G.tang+1<24?'Tầng '+(G.tang+1)+' · ':''}${I.n}</b> — ${I.r} ${I.ic}<br><small>${I.rm}</small>`,'#c9b8ff',1)}
  else toast('🏯 Chư thần Tiên Giới bắt đầu sợ hãi… Ngọc Hoàng triệu tập thiên binh!','#ffe066',1)}
 if(G.tang<24&&h>=2/3)tangGo(G.tang+1);
 else if(G.tang>=24&&h>=2/3&&!G.dd){G.dd=1;SFX.fan();toast(`👑 <b>ĐĂNG CƠ ĐẠI ĐẾ!</b><br>Bạn đã thống nhất Tiên Giới, chư thần quỳ bái.<br>Từ một hiệp sĩ vô danh, bạn trở thành <b>ĐẠI ĐẾ</b> vạn giới — ngày ${G.day}.`,'#ffe066',1);addLog('👑 Đăng cơ Đại Đế, thống nhất Tiên Giới!','#ffe066');save()}}
function thienLo(){const n=G.tang||0,b=[];let h='<p style="font-size:12.5px">Con đường phi thăng: chiếm 2/3 thành mỗi tầng để lên tầng tiếp. Tầng đã bình định khóa lại và nộp cống hằng ngày.</p>';
 if(!G.lk)h+='<p>🔒 Chưa mở. Chiếm 3/4 thành 1 lục địa tu tiên để mở ✨ Linh khí khôi phục, rồi 2/3 Cửu Thiên Huyền Giới để phi thăng.</p>';
 else if(!n)h+=`<p>🔒 Chiếm 2/3 thành của 2 lục địa Cửu Thiên Huyền Giới để <b>phi thăng</b>. Đang: ${[9,10,11].map(c=>RIC[c]+' '+Math.round(held(c)*100)+'%').join(' · ')}</p>`;
 h+='<div style="max-height:52vh;overflow:auto;font-size:13px;line-height:1.55">';
 for(let i=1;i<=24;i++){const I=TINFO(i),nm=i<24?`Tầng ${i} · ${I.n}`:'🏯 TIÊN GIỚI';
  if(i<n)h+=`<div>✅ ${nm} <span style="color:#9c9">— đã bình định</span></div>`;
  else if(i==n)h+=`<div style="color:#ffe066">⚔ <b>${nm}</b> — ${I.r} ${I.ic} · bạn giữ ${Math.round(held(12)*100)}%</div>`;
  else if(i==n+1&&G.tease==n&&n)h+=`<div style="color:#c9b8ff">🔮 ${nm} — ${I.r} ${I.ic}<br><small>${I.rm}</small></div>`;
  else if(i==24)h+=`<div style="color:#bba">🏯 TIÊN GIỚI — <i>nơi Thiên Đình ngự trị… đỉnh cao của vạn giới</i></div>`;
  else if(i==n+1)h+=`<div style="color:#99a">☁️ Tầng ${i} · ??? <small>(chiếm 1/2 tầng hiện tại để dò thám)</small></div>`;
  else if(i==9||i==18)h+=`<div style="color:#889">☁️ Tầng ${i} · ??? <small>${i==9?'— nghe đồn có tiếng rồng gầm':'— mây nhuộm đỏ máu'}</small></div>`;
  else h+=`<div style="color:#667">☁️ Tầng ${i} · ???</div>`}
 h+='</div>';if(G.tdone)h+=`<p>💰 Cống nạp từ ${G.tdone} tầng đã bình định: <b>${fmt(tribute())}</b> vàng/ngày</p>`;if(G.dd)h+='<p style="color:#ffe066">👑 Bạn đã là ĐẠI ĐẾ vạn giới.</p>';
 if(n&&contOf(P0().x,P0().y)!=12)b.push([`🌌 Về Tầng ${n<24?n:'Tiên Giới'} (miễn phí)`,()=>{close();const p=tangLand(),pl=P0();stopPl();pl.x=p.x;pl.y=p.y;pl.tx=pl.x;pl.ty=pl.y;pl.safe=6;MC.follow=1;if(G.call)for(const g of myGens()){g.x=pl.x+rnd(-90,90);g.y=pl.y+rnd(-60,60);g.tx=g.x;g.ty=g.y;g.goS=g.goP=null}}]);
 b.push(['Đóng',close]);menu('🌌 Thiên Lộ — 23 Tầng Trời',h,b)}
