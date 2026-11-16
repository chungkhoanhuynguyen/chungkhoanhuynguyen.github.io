function menu(title,html,btns){paused=true;const m=$('#menu');m.innerHTML=`<h2>${title}</h2>${html}`;
 for(const [l,f,dis] of btns){const b=document.createElement('button');b.className='b';b.innerHTML=l;b.disabled=!!dis;b.onclick=f;m.appendChild(b)}m.style.display='block';m.scrollTop=0}
function close(){$('#menu').style.display='none';paused=false}
function stopPl(){const pl=P0();pl.goS=pl.goP=pl.goF=pl.goV=null;pl.tx=pl.x;pl.ty=pl.y}
const near=(p,r,fac)=>G.L.filter(q=>q!==p&&!q.dead&&!q.inF&&q.kind!='rf'&&q.kind!='pl'&&q.fac==fac&&fac>=0&&dist(q,p)<r);
const srcs=(cfg,sd)=>cfg[sd].map(p=>p.t).concat(cfg.gar==sd?[cfg.s.gar]:[]);
function sideTxt(cfg,sd){return tt(comb(srcs(cfg,sd)))+(cfg[sd].length>1?` <small>(${cfg[sd].length} đạo quân)</small>`:'')+(cfg.gar==sd?' <small>+ quân trấn thành</small>':'')}
function battleMenu(title,info,cfg){const pl=P0();stopPl();if(G.ac){autoFight(cfg);return}const A=comb(srcs(cfg,'A')),D=comb(srcs(cfg,'D'));
 menu(title,info+`<p>🟦 Phe ta: ${sideTxt(cfg,'A')}</p><p>🟥 Phe địch: ${sideTxt(cfg,'D')}</p><p>Sức mạnh: ta <b>${fmt(str(A))}</b> — địch <b>${fmt(str(D)*(cfg.wall?1.5:1))}</b></p><p style="font-size:12px;color:#cdb">Đạo quân đồng minh ở gần tự động nhập trận cùng hai bên.</p>`,
 [['⚔ Giao chiến (tự chỉ huy, đủ quân)',()=>{close();startBattle(cfg)}],['🎲 Đánh nhanh (tự động)',()=>{close();quick(cfg)}],
  cfg.fight?['Bỏ qua',()=>{close();pl.safe=3}]:['🏃 Rút lui (mất ~15% quân)',()=>{close();retreat(cfg)}]])}
const AR=()=>G.call?900:450;
function retreat(cfg){const pl=P0(),e=cfg.D[0];kill(pl.t,Math.ceil(tot(pl.t)*.15));pl.safe=4;if(e){const a=Math.atan2(pl.y-e.y,pl.x-e.x);pl.tx=cl(pl.x+Math.cos(a)*160,30,WW-30);pl.ty=cl(pl.y+Math.sin(a)*160,30,WH-30)}cfg.D.forEach(q=>{q.goP=null;q.th=4;q.tx=q.x;q.ty=q.y})}
function encounter(e){const pl=P0();const cfg={A:[pl,...near(pl,AR(),pl.fac)],D:[e,...near(e,450,e.fac)],s:null,gar:null,wall:0};
 battleMenu(`⚔ Chạm trán: ${pname(e)}`,`<p>Phe: <b style="color:${facC(e.fac)}">${facN(e.fac)}</b> · ${badge(e)}</p>`,cfg)}
function joinFight(f){const pl=P0(),P=fightPow(f);let side=null;
 if(pl.fac==f.af||(f.af>=0&&!atWar(pl.fac,f.af)&&atWar(pl.fac,f.df)))side='A';else if(pl.fac==f.df||(f.df>=0&&!atWar(pl.fac,f.df)&&atWar(pl.fac,f.af)))side='D';
 if(!side||!tot(pl.t)){toast('Trận này không liên quan tới phe bạn.','#ccc');return}
 const mine=side=='A'?P.A:P.D,their=side=='A'?P.D:P.A,s=P.s;
 const cfg={A:[pl,...mine,...near(pl,AR(),pl.fac).filter(q=>!mine.includes(q))],D:their,s,gar:s?(side=='A'?'D':'A'):null,wall:s&&side=='A'?1:0,fight:f};
 battleMenu(`⚔ Tham chiến${s?' tại '+s.name:''}`,`<p>${facN(side=='A'?f.af:f.df)} ⚔ ${facN(side=='A'?f.df:f.af)} — bạn nhập trận cùng đồng minh.</p>`,cfg)}
const COST={inf:5,arc:8,cav:16},KN={inf:'bộ binh',arc:'cung thủ',cav:'kỵ binh'},TYN=['Kinh đô','Thành','Lâu đài'];
function townMenu(s){const pl=P0();stopPl();const o=G.L[s.own],on=o&&!o.dead?pname(o):'(trống)';
 const head=`<p>${TYN[s.type]} của <b style="color:${facC(s.fac)}">${facN(s.fac)}</b> · ${CC[s.cn].n} · ${RACE[s.race].n}</p><p>Lãnh chúa: ${o&&!o.dead?badge(o)+' <b>'+(o.kind=='pl'?'Bạn':o.name)+'</b>':'(trống)'}</p><p>Quan hệ: <b style="color:${rel(s.fac)}">${relI(s.fac)} ${s.fac==pl.fac?'Phe ta':atWar(pl.fac,s.fac)?'Đang chiến tranh':'Hòa bình'}</b></p><p>Trấn giữ: ${tt(s.gar)}</p>`;
 if(s.fac!=pl.fac){const war=atWar(pl.fac,s.fac),scfg=()=>({A:[pl,...near(pl,AR(),pl.fac)],D:G.L.filter(q=>!q.dead&&!q.inF&&q.fac==s.fac&&q.kind!='rf'&&q.kind!='pl'&&dist(q,s)<150),s,gar:'D',wall:1});
  menu(`🏰 ${s.name}`,head+`<p>Quân ta: ${tt(pl.t)}</p><p>${war?'Đang giao chiến — quân thủ có tường thành (+50%).':'🕊 Đang hòa bình với phe này.'}</p>`,
  [...(!war&&isMyKing()?[[`⚔ Tuyên chiến với ${facN(s.fac)}`,()=>{dWar(s.fac);close();townMenu(s)}]]:[]),['🏰 Công thành (tự chỉ huy)',()=>{close();startBattle(scfg())},!war||!tot(pl.t)],['🎲 Công thành nhanh',()=>{close();quick(scfg())},!war||!tot(pl.t)],['Rời đi',()=>{close();pl.safe=1}]]);return}
 const cap=rank(pl)[1],room=Math.max(0,cap-tot(pl.t));
 const rec=(k,n)=>{n=Math.min(n,s.pool,room,Math.floor(G.gold/COST[k]));if(n<1)return;G.gold-=COST[k]*n;s.pool-=n;pl.t[k]+=n;townMenu(s)};
 const btn=[...KS.map(k=>[`Chiêu 100 ${KN[k]} (${COST[k]*100} vàng)`,()=>rec(k,100),!s.pool||!room||G.gold<COST[k]])];
 btn.push([`Chiêu tối đa bộ binh`,()=>rec('inf',1e9),!s.pool||!room||G.gold<COST.inf]);
 if(s.own===0&&isMyKing()&&myGens().length){btn.push([`🎖 Ban thành này cho tướng (tướng nhận viện binh, giữ & bảo vệ vùng này)`,()=>{const g=myGens().sort((a,b)=>fiefs(a)-fiefs(b))[0];s.own=g.id;toast(`🎖 Ban ${s.name} cho ${pname(g)}`,'#ffd23a');terr();close()}])}
 if(s.own===0){btn.push(['Để lại 200 quân giữ thành',()=>{add(s.gar,take(pl.t,200));townMenu(s)},tot(pl.t)<1],['Rút 200 quân từ thành',()=>{add(pl.t,take(s.gar,Math.min(200,room)));townMenu(s)},tot(s.gar)<1||!room])}
 btn.push([`Viện binh tự động về bạn: <b>${G.rf?'BẬT':'TẮT'}</b>`,()=>{G.rf=!G.rf;townMenu(s)}],['Rời đi',()=>{close();pl.safe=1}]);
 menu(`🏯 ${s.name}`,head+`<p>Tân binh sẵn có: <b>${fmt(s.pool)}</b> · Vàng: <b>${fmt(G.gold)}</b></p><p>Quân ta: ${tt(pl.t)} / tối đa ${fmt(cap)} (${rank(pl)[0]})</p>`,btn)}
function villageMenu(v){const pl=P0();stopPl();const s=S[v.p],o=G.L[v.own],mine=v.own===0;
 const head=`<p>Thuộc ${TYN[s.type].toLowerCase()} <b style="color:${rel(s.fac)}">${s.name}</b> · ${facN(s.fac)}</p><p>Chủ đất: ${o&&!o.dead?badge(o)+' <b>'+(mine?'Bạn':o.name)+'</b>':'(trống)'}</p><p>${v.burn?`🔥 Đang bị đốt phá, hồi phục sau ${v.burn} ngày`:`🌾 Thu ${VINC} vàng/ngày · Tân binh: <b>${v.pool}</b>`}</p>`;
 if(mine){const room=rank(pl)[1]-tot(pl.t);menu(`🌾 ${v.name} — đất phong của bạn`,head+`<p style="font-size:12px;color:#cdb">Làng tự nộp vàng liên tục và cứ 3 ngày tự gửi tân binh tới bạn.</p>`,
  [[`Nhận ngay ${Math.min(v.pool,Math.max(0,room))} tân binh`,()=>{const k=Math.min(v.pool,Math.max(0,room));v.pool-=k;add(pl.t,mix(k));villageMenu(v)},!v.pool||room<1],[`Tự động chiêu mộ ở thành: <b>${G.auto?'BẬT':'TẮT'}</b>`,()=>{G.auto=!G.auto;villageMenu(v)}],['Rời đi',()=>{close();pl.safe=1}]]);return}
 const war=atWar(pl.fac,s.fac);menu(`🌾 ${v.name}`,head,[[`🔥 Cướp làng (lấy vàng, đốt làng 8 ngày)`,()=>{const g=ri(150,350);G.gold+=g;v.burn=8;v.pool=0;close();toast(`🔥 Bạn cướp ${v.name}, thu ${g} vàng`,'#ff9a5a');addLog(`Bạn cướp ${v.name}, thu ${g} vàng.`,'#fc8')},!war||!!v.burn],['Rời đi',()=>{close();pl.safe=1}]])}
function quick(cfg){const pl=P0(),b4=tot(pl.t),la=srcs(cfg,'A'),ld=srcs(cfg,'D'),A=comb(la),D=comb(ld),iA={...A},iD={...D},d0=tot(D);
 const r=auto(A,D,cfg.wall?1.5:1);distrib(la,iA,A);distrib(ld,iD,D);finish(r,cfg,0,b4-tot(pl.t),d0-tot(comb(ld)))}
function finish(win,cfg,ret,lost,kills){const pl=P0(),f=cfg.fight;
 if(f){const i=G.fights.indexOf(f);if(i>=0)G.fights.splice(i,1);[...f.A,...f.D].forEach(id=>{const p=G.L[id];if(p){p.inF=0;p.safe=3}})}
 [...cfg.A,...cfg.D].forEach(p=>{if(p!==pl&&!p.dead&&!tot(p.t))defeat(p)});
 if(ret){pl.safe=5;retreat({D:cfg.D,A:[]});addLog(`Bạn rút lui, mất ${fmt(lost)} lính.`,'#fc8');SFX.bad();mot('🏳 Rút lui',`<p>Mất ${fmt(lost)} lính. Còn: ${tt(pl.t)}</p>`,[['Tiếp tục',close]]);save();return}
 if(win&&tot(pl.t)>0){const loot=ri(100,300)+Math.round(kills*.6),cap=cfg.s&&cfg.gar=='D';G.gold+=loot;pl.safe=3;pl.ren=(pl.ren||0)+kills/4+(cap?150:0);
  cfg.D.forEach(p=>{if(p.dead)return;if(isMyKing()&&p.kind=='lord'&&Math.random()<.4){p.fac=pl.fac;p.t=mix(150);p.inF=0;p.goS=p.goP=null;p.safe=5;toast(`🤝 ${p.name} quy hàng, xin làm tướng dưới trướng bạn!`,'#7dff8a');addLog(`${p.name} quy hàng bạn.`,'#8f8')}else defeat(p)});
  if(cap)capture(cfg.s,pl);else addLog(`Bạn thắng trận, diệt ${fmt(kills)} địch, thu ${fmt(loot)} vàng.`,'#8f8');
  if(cfg.s&&cfg.gar=='A')toast(`🛡 Bạn đã giải vây ${cfg.s.name}!`,'#7dff8a');
  SFX.fan();mot('🏆 Chiến thắng!',`<p>${cap?`Bạn chiếm <b>${cfg.s.name}</b> — lãnh địa riêng của bạn (viền vàng trên bản đồ). 25% quân ở lại trấn giữ.`:'Địch tan tác.'}</p><p>Tước vị: ${badge(pl)} · Danh vọng ⭐ <b>${fmt(pl.ren)}</b></p><p>Diệt ${fmt(kills)} địch · Ta mất ${fmt(lost)} · Thu ${fmt(loot)} vàng</p><p>Quân còn: ${tt(pl.t)}</p>`,[['Tiếp tục',close]]);checkRank()}
 else{SFX.bad();const w=cfg.D.find(p=>!p.dead&&tot(p.t));if(cfg.s&&cfg.gar=='A'&&w)capture(cfg.s,w);cfg.D.forEach(p=>{p.goP=null});playerDown();mot('💀 Thua trận',`<p>Đạo quân bị đánh tan. Bạn mất 40% vàng và rút về thành gần nhất.</p>`,[['Tiếp tục',close]])}
 save()}
const TABS=[['tq','👤 Bản thân'],['tg','🧑‍✈️ Tướng'],['ng','🏛 Ngoại giao'],['tl','⚔ Thế lực'],['hd','❓ Hướng dẫn']];
let PTAB='tq',PCON=-1;
function partyMenu(p){const pl=P0();stopPl();const w=atWar(pl.fac,p.fac),me=p.fac==pl.fac,f=G.F[p.fac];
 menu(`${badge(p)} ${pname(p)}`,`<p>Phe <b style="color:${facC(p.fac)}">${facN(p.fac)}</b> · ${RACE[raceOf(p)].n} · ${fmt(tot(p.t))} quân${f&&f.heirs!=null?` · 👶 ${f.heirs} người kế vị`:''}</p><p>${me?'★ Cùng phe với bạn.':w?'⚔ Đang chiến tranh với bạn.':'🕊 Đang hòa bình với bạn.'}</p>`,
 [['💬 Trò chuyện',()=>chat(p)],...(!me&&!w&&isMyKing()?[[`⚔ Tuyên chiến với ${facN(p.fac)}`,()=>{dWar(p.fac);close()}]]:[]),...(w?[['⚔ Đuổi đánh',()=>{close();pl.goP=p}]]:[['🚶 Đi theo',()=>{close();pl.goP=p}]]),['Đóng',close]])}
function exileMenu(p){const pl=P0();stopPl();const f=G.F[p.fac],k=isMyKing(),cost=500;
 menu(`🥀 Hoàng tử ${p.name}`,`<p>Con trai ${ordN(p.ord||3)} ${f&&f.race?'hoàng tộc '+f.sur:'hoàng tộc họ '+(f?f.sur:'')}, dòng dõi ${f?f.n:''} (${RACE[f?f.race||0:0].n}) — nay đã vong quốc.</p><p>Tàn quân: ${fmt(tot(p.t))}</p><p style="font-size:12px;color:#cdb">${k?'Hoàng tử muốn nương nhờ một minh quân để phục quốc.':'Chỉ Vua mới có thể thu nạp hoàng tử làm tướng.'}</p>`,
 [['💬 Trò chuyện',()=>chat(p)],[`🤝 Thu nạp làm tướng (${cost} vàng)`,()=>{G.gold-=cost;p.kind='lord';p.fac=pl.fac;p.ren=100;p.merc=1;add(p.t,mix(500));p.home=null;close();toast(`🤝 Hoàng tử ${p.name} quỳ tạ ân, trở thành tướng dưới trướng bạn!`,'#7dff8a');addLog(`${p.name} gia nhập làm tướng.`,'#8f8');save()},!k||G.gold<cost],['Đóng',close]])}
/* ---------- trò chuyện với vua (Claude nhập vai) ---------- */
const PERS=['kiêu ngạo, tự phụ','khôn ngoan, thâm trầm','hiếu chiến, nóng nảy','nhân từ, trọng nghĩa','đa nghi, xảo quyệt','tham lam, thực dụng','già dặn, điềm tĩnh','trẻ tuổi, đầy tham vọng'];
const pick=a=>a[ri(0,a.length-1)];
function botReply(p,msg){const pl=P0(),m=msg.toLowerCase(),me=p.fac==pl.fac,w=atWar(pl.fac,p.fac),per=p.id%PERS.length,ex=p.kind=='exile',king=p.kind=='king';
 const T=king?'Trẫm':'Ta',N=me?(king?'khanh':'ngươi'):'ngươi',fn=facN(p.fac),mp=str(p.t)+S.filter(s=>s.fac==p.fac).reduce((a,s)=>a+str(s.gar),0),pp=str(pl.t)+S.filter(s=>s.fac==pl.fac).reduce((a,s)=>a+str(s.gar),0),strong=mp>pp*1.3,weak=mp*1.3<pp;
 const proud=per==0||per==2||per==7,kind=per==3||per==6,greedy=per==5,sly=per==4;
 const has=re=>re.test(m);
 if(ex){if(has(/về|theo|gia nhập|làm tướng|phục vụ|thu nạp|quy thuận/)){if(isMyKing())return pick([`Nước mất nhà tan, ${T} chỉ mong gặp minh quân. Nguyện theo ${N} đến cùng! [THEO]`,`Ân đức của ${N}, ${T} khắc cốt ghi tâm. Xin nhận ${T} làm tướng! [THEO]`]);return `${N} chưa phải bậc đế vương. Khi nào ${N} xưng Vua, ${T} sẽ nghĩ lại.`}
  if(has(/phục quốc|báo thù|trả thù/))return pick([`Mối thù mất nước, ${T} chưa ngày nào quên. Chỉ tiếc binh lực mỏng manh…`,`Một ngày nào đó cờ của dòng tộc ${T} sẽ lại tung bay.`]);
  return pick([`${T} chỉ là kẻ lưu vong, còn gì để nói nữa đâu…`,`Giang sơn đã mất, ${T} lang bạt khắp nơi. ${N} có lòng thương thì cho ${T} một con đường.`,`Ngày trước dòng tộc ${T} cũng từng hiển hách lắm.`])}
 if(me){if(has(/vàng|tiền|ban|thưởng/))return kind?`Khanh lao khổ nhiều rồi, cầm lấy chút vàng này. [VANG:${ri(150,400)}]`:`Quốc khố còn eo hẹp, khanh tự lo liệu đi.`;
  if(has(/đánh|chinh phạt|tấn công|diệt/))return pick([`Tốt! Hãy dẫn quân ra trận, Trẫm sẽ phái viện binh theo sau.`,`Khanh có chí lớn. Mang đầu kẻ địch về đây, Trẫm trọng thưởng!`]);
  return pick([`Khanh vất vả rồi. Hãy giữ vững biên cương cho Trẫm.`,`Trẫm tin tưởng khanh, đừng phụ lòng.`,`Thiên hạ chưa yên, khanh phải luyện binh cho tốt.`])}
 if(has(/hòa|đình chiến|ngừng chiến|thôi đánh/)){if(!w)return pick([`Giữa ta và ${N} vốn đang yên ổn, cần gì phải nói chuyện hòa?`,`Hòa hiếu đã có từ lâu, ${N} cứ yên tâm.`]);
  const ch=(weak?.7:strong?.12:.38)+(kind?.2:0)-(proud?.18:0);
  if(Math.random()<ch)return pick([`Binh đao mãi cũng hao tổn dân chúng… Được, ${T} chấp thuận giảng hòa. [HOA]`,`${N} biết điều đấy. Từ nay hai bên thu quân. [HOA]`,`Thôi được, ${T} cho ${N} một cơ hội. Hòa! [HOA]`]);
  return strong?pick([`Hòa? Khi quân ${T} sắp san bằng thành ${N}? Nực cười!`,`Quỳ xuống xin thì may ra ${T} còn nghĩ.`]):pick([`${T} chưa tin ${N}. Hãy chứng tỏ thành ý trước đã.`,`Máu của tướng sĩ ${T} chưa khô, nói hòa còn quá sớm.`])}
 if(has(/liên minh|đồng minh|hợp tác|kết giao/)){if(w)return `Đang đánh nhau mà ${N} lại đòi liên minh? ${T} không phải kẻ ngốc.`;
  return kind||sly?pick([`Liên minh ư… ${T} thấy cũng có lợi. Hai nước ta cứ giữ hòa hiếu, cùng chống kẻ thù chung.`,`Bạn hơn thù. ${T} ghi nhận thành ý của ${N}.`]):pick([`${fn} không cần dựa dẫm vào ai.`,`Liên minh với kẻ yếu hơn để làm gì?`])}
 if(has(/vàng|tiền|cống|tặng|cho ta/)){if(w)return `Muốn vàng thì đến mà lấy, nếu ${N} có bản lĩnh!`;
  if(greedy)return `Vàng? Ngươi nên cống nạp cho ${T} mới phải.`;if(kind&&Math.random()<.6)return `Coi như quà kết giao, ${N} nhận lấy. [VANG:${ri(100,350)}]`;return `${T} không ban phát vàng cho kẻ lạ.`}
 if(has(/diệt|giết|chết|tiêu diệt|san bằng|đánh ngươi|tuyên chiến|xâm lược/)){if(w)return pick([`Cứ đến đây! Thành trì của ${T} đang chờ ${N}.`,`Lời lẽ to tát lắm. Ra chiến trường rồi hẵng nói!`]);
  if(proud||strong)return pick([`Dám uy hiếp ${T}?! Được lắm, từ hôm nay ${fn} và ${N} là kẻ thù! [CHIEN]`,`Ngươi tự chuốc lấy họa! ${T} tuyên chiến! [CHIEN]`]);return pick([`${N} nên cẩn trọng lời nói. ${T} không muốn binh đao, nhưng cũng chẳng sợ.`,`Hừ… ${T} sẽ nhớ lời này.`])}
 if(has(/thiên hạ|thời cuộc|tình hình|nghĩ gì|thế nào/)){const ss=S.filter(s=>s.fac==p.fac).length,mv=G.mv>=0&&G.F[G.mv]?G.F[G.mv].n:'';
  return pick([`${fn} hiện giữ ${ss} thành. Thiên hạ rồi sẽ thuộc về kẻ mạnh nhất.`,`Bốn bể dậy sóng, ${mv?mv+' ở Vùng Đất Chết đang lăm le khắp nơi. ':''}Ai không mạnh thì sẽ bị nuốt chửng.`,`${T} chỉ lo cho con dân của ${fn}. Chuyện khác, để trời định.`])}
 if(has(/xin chào|chào|kính|bái kiến|tham kiến/))return w?`Kẻ thù mà cũng biết lễ nghĩa sao?`:pick([`${N} đến có việc gì?`,`Miễn lễ. ${N} cứ nói.`]);
 return w?pick([`Ngươi còn dám đến trước mặt ${T}? Chiến trường sẽ phân định!`,`Lời ngươi nói chẳng đáng một đồng.`,`${T} không rảnh nghe kẻ thù lải nhải.`]):pick([`${T} nghe đây. Có việc gì cứ nói thẳng.`,`Hừm… ${N} nói tiếp đi.`,`Thiên hạ loạn lạc, giữ hòa khí với nhau cũng là phúc.`])}
function chat(p){const pl=P0();G.chat=G.chat||{};const H=(G.chat[p.id]=G.chat[p.id]||[]);
 const draw=()=>{const box=$('#chatBox');if(!box)return;box.innerHTML=H.map(m=>`<div class="cm ${m.r}">${m.r=='u'?'<b>Bạn:</b> ':`<b style="color:${facC(p.fac)}">${p.name}:</b> `}${m.t.replace(/</g,'&lt;')}</div>`).join('')||'<div class="cm a" style="opacity:.7">Hãy mở lời trước…</div>';box.scrollTop=1e9};
 menu(`💬 ${pname(p)}`,`<div id="chatBox"></div><div class="crow"><input id="chatIn" maxlength="200" placeholder="Nói gì đó… (vd: ta muốn giảng hòa)"><button class="sb" id="chatGo">Gửi</button></div><div class="tabs sm" style="margin-top:6px">${['Ta muốn giảng hòa','Hãy liên minh với ta','Ngươi nghĩ gì về thiên hạ?','Ta sẽ diệt ngươi!'].map(s=>`<button onclick="document.querySelector('#chatIn').value='${s}'">${s}</button>`).join('')}</div>`,[['Đóng',close]]);
 draw();const go=async()=>{const inp=$('#chatIn'),msg=inp.value.trim();if(!msg||$('#chatGo').disabled)return;inp.value='';H.push({r:'u',t:msg});H.push({r:'a',t:'…'});draw();$('#chatGo').disabled=true;
  await new Promise(r=>setTimeout(r,500+Math.random()*700));let rep=botReply(p,msg);
  const tag=(rep.match(/\[([A-Z]+)(?::(\d+))?\]/)||[]);H[H.length-1].t=rep.replace(/\[[A-Z]+(:\d+)?\]/g,'').trim();while(H.length>24)H.shift();draw();$('#chatGo').disabled=false;
  if(tag[1]=='HOA'&&atWar(pl.fac,p.fac)&&p.fac>=0){G.war[pl.fac][p.fac]=G.war[p.fac][pl.fac]=0;if(G.rev&&G.rev[1]==p.fac)G.rev=null;terr();toast(`🕊 ${facN(p.fac)} đồng ý giảng hòa!`,'#7dff8a');addLog(`Giảng hòa với ${facN(p.fac)} qua đàm phán.`,'#8f8')}
  else if(tag[1]=='CHIEN'&&p.fac>=0&&p.fac!=pl.fac&&!atWar(pl.fac,p.fac)){G.war[pl.fac][p.fac]=G.war[p.fac][pl.fac]=1;terr();SFX.war();toast(`⚔ ${facN(p.fac)} tuyên chiến với bạn!`,'#ff6a5a')}
  else if(tag[1]=='VANG'){const g=Math.min(500,+tag[2]||0);if(g>0){G.gold+=g;toast(`💰 ${p.name} tặng bạn ${g} vàng`,'#ffd77a')}}
  else if(tag[1]=='THEO'&&p.kind=='exile'&&isMyKing()){p.kind='lord';p.fac=pl.fac;p.ren=100;p.merc=1;add(p.t,mix(500));toast(`🤝 Hoàng tử ${p.name} về làm tướng của bạn!`,'#7dff8a')}};
 $('#chatGo').onclick=go;$('#chatIn').onkeydown=e=>{if(e.key=='Enter')go()};setTimeout(()=>{try{$('#chatIn').focus()}catch(e){}},50)}
function goSee(x,y,z){close();MC.follow=0;MC.x=x;MC.y=y;MC.z=z||.6}
function facRow(i,act){const pl=P0(),f=G.F[i],ss=S.filter(s=>s.fac==i),me=i==pl.fac,w=atWar(pl.fac,i),cap=ss.find(s=>s.type==0)||ss[0];
 const st=me?'<span style="color:#7dff8a">★ Phe ta</span>':w?'<span style="color:#ff6a5a">⚔ Chiến</span>':'<span style="color:#ddd">🕊 Hòa</span>';
 const kg=G.L[f.king];let b=kg&&!kg.dead&&kg.kind!='pl'?`<button class="sb" onclick="chat(G.L[${f.king}])">💬</button>`:'';if(act&&!me&&isMyKing()){const cost=Math.round(800+facPow(i)*.3);b+=w?`<button class="sb" onclick="dPeace(${i})">🕊 Cầu hòa ${fmt(cost)}💰</button>`:`<button class="sb war" onclick="dWar(${i})">⚔ Tuyên chiến</button>`}
 return`<tr><td style="color:${f.c}"><b>${f.n}</b></td><td>${ss.length}🏰</td><td>${fmt(facPow(i))}</td><td>${st}</td><td>${cap?`<button class="sb" onclick="goSee(${cap.x},${cap.y},.45)">📍</button>`:''}${b}</td></tr>`}
function dWar(i){const me=P0().fac;G.war[me][i]=G.war[i][me]=1;terr();SFX.war();toast(`⚔ Bạn TUYÊN CHIẾN với ${G.F[i].n}!`,'#ff6a5a');addLog(`Bạn tuyên chiến với ${G.F[i].n}.`,'#f88');panel(PTAB)}
function dPeace(i){const me=P0().fac,f=G.F[i],ep=facPow(i),cost=Math.round(800+ep*.3);if(G.gold<cost){toast('Không đủ vàng để cống nạp','#f88');return}
 const ok=Math.random()<(f.race==4?.08:cl(.35+(facPow(me)/(ep||1))*.35,.15,.95));if(ok){G.gold-=cost;G.war[me][i]=G.war[i][me]=0;if(G.rev&&G.rev[1]==i)G.rev=null;terr();toast(`🕊 ${f.n} chấp nhận giảng hòa!`,'#7dff8a');addLog(`Giảng hòa với ${f.n} (-${fmt(cost)} vàng).`,'#8f8')}else toast(`✋ ${f.n} khước từ lời cầu hòa!`,'#ff6a5a');panel(PTAB)}
function tgl(k){G[k]=!G[k];panel(PTAB)}
function panel(tab){if(!G)return;if(typeof tab=='string')PTAB=tab;const pl=P0(),cur=contOf(pl.x,pl.y),king=isMyKing();let h=`<div class="tabs">${TABS.map(([k,n])=>`<button class="${k==PTAB?'on':''}" onclick="panel('${k}')">${n}</button>`).join('')}</div>`,btn=[];
 if(PTAB=='tq'){const cs=S.filter(s=>s.own===0),vs=V.filter(v=>v.own===0),canInd=fiefs(pl)>=2&&!king;
  h+=`<p>${badge(pl)} · ⭐ Danh vọng ${fmt(pl.ren||0)} · Quân ${fmt(tot(pl.t))}/${fmt(rank(pl)[1])}</p><p>🏰 Thành: <b>${cs.length}</b> · 🌾 Đất phong: <b>${vs.length}</b> · 💰 ${fmt(income())}/ngày, lương ${fmt(wages())}/ngày</p>
  <p style="font-size:12px;color:#cdb">Lên tước nhờ số thành hoặc ⭐: 🎖Nam tước 1 thành/300⭐ · 🏅Tử tước 2/1.000⭐ · 🥇Bá tước 3/3.000⭐ · 💠Hầu tước 5/8.000⭐ · ⚜️Công tước 8/20.000⭐ · 👑Vua (tự lập) · 🐉Hoàng đế (thống nhất 1 nước)</p>`;
  btn.push([`🪖 Tự động chiêu mộ: <b>${G.auto?'BẬT':'TẮT'}</b>`,()=>tgl('auto')],[`📯 Viện binh tự về bạn: <b>${G.rf?'BẬT':'TẮT'}</b>`,()=>tgl('rf')]);
  btn.push([`🤖 Tự chinh phạt: <b>${G.ac?'BẬT':'TẮT'}</b>`,()=>{close();acToggle()}],['🌐 Dịch chuyển về châu lục đã chiếm',tpMenu],[`📶 Đồng hồ đo lag: <b>${LAGON?'BẬT':'TẮT'}</b>`,()=>{LAGON=!LAGON;try{localStorage.setItem('ltlc-lag',LAGON?'1':'0')}catch(e){}LF.t0=0;close();toast(LAGON?'📶 Hiện đồng hồ đo lag (góc trên trái)':'📶 Đã ẩn đồng hồ đo lag','#9cf')}]);
  if(G.xian)btn.push(['🌀 Xem Thông đạo gần nhất',()=>{mkPortals();const ps=G.portals.filter(q=>q.w==WRLD(pl.y)).sort((a,b)=>dist(a,pl)-dist(b,pl));if(ps[0])goSee(ps[0].x,ps[0].y,.7)}]);
  if(!king)btn.push([`👑 Tự lập vương quốc ${canInd?'':'(cần ≥2 thành)'}`,()=>{indep();close()},!canInd]);
  btn.push(['💾 Lưu game',()=>{save();toast('💾 Đã lưu game','#9f9');close()}],['🏠 Màn hình chính',()=>{save();close();titleMenu()}])}
 else if(PTAB=='tg'){const gs=king?myGens():G.L.filter(q=>!q.dead&&q.fac==pl.fac&&q.kind!='rf'&&q.kind!='pl'&&dist(q,pl)<1500);
  const RO=x=>RK.indexOf(rank(x)[0]);gs.sort((a,b)=>RO(b)-RO(a)||tot(b.t)-tot(a.t));
  h+=king?`<p style="font-size:12.5px">🧑‍✈️ <b>${gs.length}</b> tướng · ${fmt(gs.reduce((a,g)=>a+tot(g.t),0))} quân · 🏯 ${gs.filter(g=>g.vuong).length} Vương · Châu lục chiếm: <b>${contsHeld()}</b>/5${contsHeld()>=4?' <span style="color:#ff8a6a">⚠ Vương có thể phản loạn!</span>':''}</p>`:`<p style="font-size:12.5px">Bạn chưa là Vua — dưới đây là lãnh chúa cùng phe ở gần.</p>`;
  {const kg=myKing();if(kg)h+=`<p style="background:#3a2550;padding:5px;border-radius:8px;font-size:12.5px">👑 <b>${pname(kg)}</b> · ${fmt(tot(kg.t))} <button class="sb" onclick="followKing()">🚶 Theo</button> <button class="sb" onclick="chat(G.L[${kg.id}])">💬</button></p>`}
  const LC=l=>l>=70?'#7dff8a':l>=45?'#ffd23a':'#ff6a5a',ST=g=>g.inF?'⚔':G.call&&king&&g.kind=='lord'?'📯':g.goS?(g.goS.fac==g.fac?'🏰':'⚔'):'🚶';
  h+='<table class="gt"><tr style="color:#cdb;font-size:10.5px"><td>Tước · Tên</td><td>Quân · Thành</td><td>❤</td><td></td><td></td></tr>'+gs.slice(0,60).map(g=>{const l=Math.round(g.loy??70),r=rank(g);
   const cs=S.filter(s=>s.own===g.id),cg=cs.reduce((a,s)=>a+tot(s.gar),0);
   return`<tr><td><span class="bdg" style="background:${r[3]};font-size:10px;padding:0 5px">${r[2]} ${r[0]}</span> <b>${g.name}</b>${g.lieg>=0&&G.L[g.lieg]&&!G.L[g.lieg].dead&&g.lieg!=null?' <small style="color:#ff8a3a">↳'+G.L[g.lieg].name.split(' ').pop()+'</small>':''}</td><td>🗡${fmt(tot(g.t))}${cs.length?`<br><small style="color:#ffd77a">🏰${cs.length} · 🛡${fmt(cg)}</small>`:''}</td><td style="color:${LC(l)}">❤${l}</td><td>${ST(g)}</td><td><button class="sb" onclick="goSee(${g.x},${g.y},.8)">📍</button>${king&&!g.vuong&&g.kind=='lord'?`<button class="sb" onclick="crown(${g.id})">🏯</button>`:''}</td></tr>`}).join('')+'</table>'+(gs.length>60?`<p style="font-size:11px;opacity:.7">…và ${gs.length-60} tướng nữa</p>`:'')+(king?'<p style="font-size:11px;color:#cdb">❤ trung thành · 🏯 phong Vương (5.000 vàng): Vương thu thuế thành của mình và tự chiêu tướng riêng. Khi bạn chiếm từ 4 châu lục, Vương ❤ thấp mà mạnh bằng 1/4 bạn sẽ phản loạn.</p>':'');
  if(king){btn.push([`🧑‍✈️ Chiêu mộ tướng mới (${fmt(genCost())} vàng)`,()=>{hireGen();panel('tg')},G.gold<genCost()],[`💰 Chiêu mộ hết vàng: ${hireMaxN()} tướng`,()=>{const n=hireMax();toast(`🧑‍✈️ Đã chiêu mộ ${n} tướng mới, mỗi tướng 800 quân!`,'#7dff8a');panel('tg')},hireMaxN()<1],[`🤖 Tự động chiêu mộ tướng: <b>${G.autoGen?'BẬT':'TẮT'}</b>`,()=>tgl('autoGen')],[`📯 Triệu tập tướng theo bạn: <b>${G.call?'BẬT':'TẮT'}</b>`,()=>tgl('call')])}}
 else if(PTAB=='ng'||PTAB=='tl'){const c=PCON>=0?PCON:cur;
  h+=`<div class="tabs sm">${[...Array(NC()).keys()].filter(OPEN).map(k=>`<button class="${k==c?'on':''}" onclick="PCON=${k};panel()">${RIC[k]} ${RACE[k].n}${k==cur?' (đang ở)':''}</button>`).join('')}</div>`;
  if(PTAB=='ng')h+=king?`<p style="font-size:12px;color:#cdb">Bạn là Vua: bấm ⚔ để tuyên chiến, 🕊 để cầu hòa (phải cống vàng). Bấm 📍 để xem kinh đô phe đó.</p>`:`<p>Chỉ <b>Vua</b> mới tuyên chiến/cầu hòa được. Hãy chiếm đủ 2 thành rồi Tự lập ở tab 👤 Bản thân.</p>`;
  CC.forEach((cc,ci)=>{if(cc.race!=c)return;const fs=G.F.map((f,i)=>i).filter(i=>G.F[i].cn==ci&&!G.F[i].dead&&S.some(s=>s.fac==i));if(!fs.length)return;
   h+=`<h3>${cc.n} <button class="sb" onclick="goSee(${cc.x},${cc.y},.3)">📍 xem</button></h3><table>${fs.map(i=>facRow(i,PTAB=='ng')).join('')}</table>`});
  if(PCON>=0&&PCON!=cur)btn.push([`🌍 Xem châu lục ${RACE[c].n} trên bản đồ`,()=>goSee(OX[c]+CWc[c]/2,OY[c]+CHc[c]/2,.15)])}
 else{h+=GUIDE}
 btn.push(['Đóng',()=>{PCON=-1;close()}]);menu('📜 Thế cục',h,btn)}
function diplo(){PCON=-1;panel('ng')}
const GUIDE=`<p><b>🎯 Mục tiêu:</b> từ Hiệp sĩ chiếm thành → lên tước → tự lập làm Vua → thống nhất 5 châu lục.</p>
<p><b>🗺 Bản đồ:</b> chạm đất để đi · chạm thành/làng để vào · chạm đạo quân để đuổi · kéo để xem · chụm 2 ngón hoặc ＋/－ để phóng to · 📍 về chỗ bạn.</p>
<p><b>🎨 Màu:</b> <span style="color:#7dff8a">xanh = phe ta</span> · <span style="color:#ff6a5a">đỏ = kẻ thù</span> · trắng = đang hòa. Bấm 🧭 để hiện mũi tên chỉ hướng các nước trong vài giây.</p>
<p><b>💰 Kinh tế:</b> làng & thành của bạn nộp vàng liên tục và tự gửi tân binh. Vua ban quân mỗi 5 ngày. Tự động chiêu mộ dùng vàng mua lính.</p>
<p><b>⚔ Đánh trận:</b> gặp địch chọn Tự chỉ huy (Giữ trận / Xung phong) hoặc Đánh nhanh. Đồng minh gần đó tự nhập trận. Thấy vòng ⚔ đỏ trên bản đồ = trận đang diễn ra, chạm vào để tham chiến.</p>
<p><b>🏰 Công thành:</b> đến thành địch → Công thành. Thắng = thành thành lãnh địa của bạn.</p>
<p><b>👑 Làm Vua:</b> có 2 thành → tab Bản thân → Tự lập. Sau đó chiêu mộ tướng (tab Tướng), ban thành cho tướng, tuyên chiến/cầu hòa (tab Ngoại giao).</p>
<p><b>💀 Vùng Đất Chết:</b> mỗi thành là một Tử Vương riêng, tự đánh nhau. Kẻ có nhiều thành và quân nhất được tôn là 😈 <b>Ma Vương</b>. Mọi châu lục đều có thể vượt biển sang đánh chiếm nhau.</p><p><b>💬 Ngoại giao bằng lời:</b> chạm vào một vị vua (hoặc nút 💬 ở tab Ngoại giao) để trò chuyện. Vua có tính cách riêng và có thể đồng ý giảng hòa, tặng vàng hay nổi giận tuyên chiến. Nước vong quốc để lại hoàng tử 🥀 lưu lạc — Vua có thể thu nạp làm tướng. Ai thống nhất cả một châu lục sẽ xưng ☀️Nhân Hoàng / ⛰️Thạch Hoàng / 🌙Tinh Hoàng / 🐺Lang Hoàng / ☠️Minh Hoàng.</p><p><b>🌊 Sang châu lục khác:</b> đi thẳng ra biển (quân lên thuyền), hoặc xem trước ở tab Ngoại giao/Thế lực → chọn châu lục → 📍 xem. Muốn đánh thì tuyên chiến với phe ở đó trước.</p>
<p><b>👑 Vua của bạn:</b> có vòng tím và vương miện trên bản đồ. Bấm nút 👑 bên phải để xem Vua đang làm gì và chọn Đi theo Vua để cùng đánh.</p><p><b>⚙ Nút bên phải:</b> 🌐 dịch chuyển về các châu lục đã chiếm (tốn vàng + ngày) · 🧭 hiện mũi tên chỉ hướng các nước trong vài giây · 🔊 âm thanh · 🗺 kiểu màu bản đồ · 🎨/⚙/⚡ đổi đồ họa Đẹp → Nhẹ → <b>Siêu mượt</b> (máy giật thì chọn ⚡) · ⛶ toàn màn hình.</p>`;
function indep(){const pl=P0(),old=pl.fac,ni=G.F.length;G.F.push({sur:'Bạn',n:'Vương quốc của Bạn',race:G.F[old]?G.F[old].race||0:0,cn:G.F[old]?G.F[old].cn:0,c:'#ffd23a',king:0,dead:0,emp:0});
 G.war.forEach((r,i)=>r.push(i==old?0:(G.war[old]?G.war[old][i]:1)));G.war.push(G.F.map((f,i)=>i==ni||i==old?0:(G.war[old]?G.war[old][i]:1)));G.rev=[G.day+6,old];S.forEach(s=>{if(s.own===0)s.fac=ni});pl.fac=ni;G.pf=ni;
 addLog('👑 Bạn tự lập vương quốc và xưng Vua! Nhà cũ của bạn coi bạn là phản tặc.','#ffd23a');G.gold+=3000;hireGen();hireGen();G.call=1;toast('👑 Bạn đã xưng Vua! 2 tướng đầu tiên đã gia nhập và đang theo bạn.<br><small>Nhà cũ sẽ tuyên chiến sau 6 ngày — hãy chuẩn bị! Chiêu thêm tướng trong 📜 Thế cục.</small>','#ffd23a',1);terr();save()}
$('#bFac').onclick=()=>{if(!paused)panel()};

/* ================= TRẬN ĐÁNH (1 lính = 1 hình người que) ================= */
const SP=8,UT=[{hp:100,atk:14,rng:9,sp:30,cd:1},{hp:70,atk:10,rng:260,sp:28,cd:2},{hp:140,atk:20,rng:10,sp:70,cd:1.1}];
const GT=document.createElement('canvas');GT.width=GT.height=160;{const g=GT.getContext('2d');g.fillStyle='#62893f';g.fillRect(0,0,160,160);
 for(let i=0;i<70;i++){g.fillStyle=Math.random()<.5?'rgba(255,255,190,.07)':'rgba(0,40,0,.09)';E(g,Math.random()*160,Math.random()*160,rnd(10,40),rnd(5,14))}
 g.strokeStyle='rgba(30,60,20,.45)';for(let i=0;i<260;i++){const x=Math.random()*160,y=Math.random()*160;g.beginPath();g.moveTo(x,y);g.lineTo(x+rnd(-2,2),y-rnd(2,5));g.stroke()}}
