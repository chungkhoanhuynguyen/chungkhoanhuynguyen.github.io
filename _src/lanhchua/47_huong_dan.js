/* ================= HƯỚNG DẪN NGƯỜI MỚI: 🎯 nhiệm vụ, ❓ chú thích nút, giải thích ô số ================= */
const WOF=c=>c>=12?2:c>=9?1:0;
const Z0={inf:0,arc:0,cav:0};
function qNearS(ok,conts){const pl=P0(),my=Math.max(1,str(pl.t)),pw=WOF(contOf(pl.x,pl.y));let b=null,bd=1e18;
 for(const s of S){if(!ok(s)||!OPEN(s.race))continue;if(conts&&!conts.includes(s.race))continue;const g=str(s.gar||Z0)*1.5;let d=Math.hypot(s.x-pl.x,s.y-pl.y)*(1+g/my);if(WOF(s.race)!=pw)d*=50;if(d<bd){bd=d;b=s}}return b}
const qEnemy=c=>{const me=P0().fac;return qNearS(s=>s.fac!=me&&atWar(me,s.fac),c)};
const qPct=x=>Math.round(cl(x,0,1)*100)+'%';
function qBest(cs,n,th){const h=cs.map(c=>[c,held(c)]).sort((a,b)=>b[1]-a[1]);const top=h.slice(0,n);return{p:top.reduce((a,x)=>a+Math.min(x[1],th),0)/(n*th),tg:(h.find(x=>x[1]<th)||h[0])[0],h}}
function qCur(){const pl=P0(),me=pl.fac,king=isMyKing(),nf=fiefs(pl),cap=rank(pl)[1],army=tot(pl.t),gens=myGens().length;
 const low=army<cap*.4&&G.gold>=400&&!G.lsOn;
 const rec=()=>({ic:'🪖',t:'Chiêu mộ thêm lính',d:`Quân bạn đang ít (<b>${fmt(army)}</b>/${fmt(cap)}). Vào một thành <span style="color:#7dff8a">phe ta (tên xanh)</span> → bấm <b>Chiêu bộ binh / cung thủ / kỵ binh</b>. Kỵ binh mạnh nhất nhưng đắt nhất.`,tg:qNearS(s=>s.fac==me),go:'Tới thành chiêu mộ'});
 if(!king&&nf==0&&(pl.ren||0)<300){if(low)return rec();
  const pr=P0();let bb=null,bd=1e18;for(const q of G.L){if(q.dead||q.kind!='bandit'||q.inF)continue;const d=Math.hypot(q.x-pr.x,q.y-pr.y)*(1+str(q.t)/Math.max(1,str(pr.t)));if(d<bd){bd=d;bb=q}}
  return{ic:'⭐',t:`Lên Nam tước · ⭐${fmt(pl.ren||0)}/300`,p:(pl.ren||0)/300,d:'Đánh tan các toán <b>☠ Thổ phỉ</b> (đạo quân cờ xám) để lấy ⭐ danh vọng. Đủ <b>300⭐</b> hoặc chiếm được <b>1 thành</b> là lên <b>Nam tước</b> — tước càng cao càng mang được nhiều quân.<br><small>Gặp địch, nếu không muốn tự điều quân thì chọn 🎲 Đánh nhanh.</small>',tgP:bb,go:'Đuổi đánh thổ phỉ gần nhất'}}
 if(!king&&nf<2){if(low)return rec();const s=qEnemy();
  return{ic:'🏰',t:`Chiếm thành địch · ${nf}/2`,p:nf/2,d:`Có <b>2 thành</b> là đủ điều kiện <b>xưng Vua</b>. Tìm thành <span style="color:#ff6a5a">tên đỏ</span> có quân trấn giữ ít hơn quân bạn, tới sát rồi bấm <b>⚔ Công thành</b>.${s?`<br>Gợi ý: <b>${s.name}</b> — trấn giữ ${fmt(tot(s.gar||Z0))}, quân bạn ${fmt(army)}${str(s.gar||Z0)*1.5>str(pl.t)?' <span style="color:#f99">(còn mạnh hơn bạn — nên chiêu thêm lính hoặc đợi Vua cùng đánh)</span>':''}.`:''}`,tg:s,go:'Hành quân tới thành này'}}
 if(!king)return{ic:'👑',t:'Xưng Vua!',d:'Bạn đã có đủ 2 thành. Tự lập vương quốc để được <b>chiêu mộ tướng</b>, <b>tuyên chiến</b>, <b>cầu hòa</b>.<br><small>Nhà cũ sẽ coi bạn là phản tặc và tuyên chiến sau 6 ngày — hãy giữ đủ quân.</small>',act:['👑 Mở bảng tự lập',()=>panel('tq')]};
 if(gens<3&&G.open.length==1)return{ic:'🧑‍✈️',t:`Chiêu mộ tướng · ${gens}/3`,p:gens/3,d:'Tướng tự dẫn quân đi đánh chiếm cho bạn và tự lên tước. Mở <b>📜 Thế cục → 🧑‍✈️ Tướng</b> để chiêu mộ, ban thành cho tướng.',act:['🧑‍✈️ Mở tab Tướng',()=>panel('tg')]};
 const st=(ic,t,p,d,c)=>({ic,t:`${t} · ${qPct(p)}`,p,d,tg:qEnemy(c),go:'Đánh thành địch gần nhất'});
 if(G.open.length==1){const h=held(G.open[0]);return st('🗺','Chinh phục quê nhà',h/.75,`Chiếm <b>75%</b> thành của châu lục quê (đang ${qPct(h)}) để mở bản đồ 4 châu lục.`,[G.open[0]])}
 if(!G.open.includes(4)){const b=qBest([0,1,2,3],2,.75);return st('🌍','Làm chủ 2 châu lục',b.p,`Chiếm <b>75%</b> thành ở <b>2 châu lục</b> để mở 💀 Vùng Đất Chết.<br>${b.h.map(([c,v])=>`${RACE[c].n}: ${qPct(v)}`).join(' · ')}`,[b.tg])}
 if(!G.divine)return st('💀','Chinh phục Vùng Đất Chết',held(4)/.5,`Chiếm <b>1/2</b> thành Vùng Đất Chết (đang ${qPct(held(4))}) để mở Thời đại Thần linh.`,[4]);
 if(!G.xian){const b=qBest([5,6,7,8],2,.75);return st('⚡','Chinh phạt Thần giới',b.p,`Chiếm <b>75%</b> thành ở <b>2 lục địa Thần linh</b> để mở 🌀 Cửu Thiên Huyền Giới.<br>${b.h.map(([c,v])=>`${RACE[c].n}: ${qPct(v)}`).join(' · ')}`,[b.tg])}
 if(!G.lk){const b=qBest([9,10,11],1,.75);return st('✨','Đánh chiếm một lục địa tu tiên',b.p,`Đi qua 🌀 Thông đạo lên Cửu Thiên, chiếm <b>75%</b> thành của 1 lục địa tu tiên để mở ✨ Linh khí khôi phục.<br><small>Ở Cửu Thiên vàng đổi thành 💎 linh thạch — dùng để ☯ đột phá cảnh giới, tăng số quân dẫn theo.</small>`,[b.tg])}
 if(canUp()&&(!G.tang||G.tang==(G.tmax||G.tang)))return{ic:'⚡',t:G.tang?`Lên ${G.tang+1>=24?'Tiên Giới':'Tầng '+(G.tang+1)}!`:'Phi thăng!',p:1,d:'Đã đủ điều kiện. Mở 🌌 Thiên Lộ để lên tầng mới (có thể quay về tầng cũ bất cứ lúc nào).',act:['🌌 Mở Thiên Lộ',thienLo]};
 if(!G.tang){const b=qBest([9,10,11],2,.67);return st('🌌','Chuẩn bị phi thăng',b.p,`Chiếm <b>2/3</b> thành ở <b>2 lục địa Cửu Thiên</b> để phi thăng lên 23 Tầng Trời.<br>${b.h.map(([c,v])=>`${RACE[c].n}: ${qPct(v)}`).join(' · ')}`,[b.tg])}
 if(G.tang<(G.tmax||0))return{ic:'🌌',t:`Đang ở Tầng ${G.tang} (đã tới ${G.tmax>=24?'Tiên Giới':'Tầng '+G.tmax})`,d:'Tầng này đã bình định. Mở 🌌 Thiên Lộ để trở lại tầng cao nhất và chinh phạt tiếp.',act:['🌌 Mở Thiên Lộ',thienLo]};
 if(G.tang>=24&&!G.dd)return st('🐲','Thống nhất Tiên Giới',held(12)/(2/3),'Chiếm <b>2/3</b> thành Tiên Giới để đăng cơ <b>Đại Đế</b>.',[12]);
 if(G.tang<24)return st('☁️',`Bình định Tầng ${G.tang}`,held(12)/(2/3),`Chiếm <b>2/3</b> thành của tầng này để lên tầng tiếp theo (đang ${qPct(held(12))}).`,[12]);
 return{ic:'🐲',t:'Đại Đế Vạn Giới',d:'Bạn đã đi hết hành trình! Hãy tiếp tục quét sạch thế lực còn lại.',tg:qEnemy([12]),go:'Đánh thành địch gần nhất'}}
function qHints(){const pl=P0(),o=[],cap=rank(pl)[1],army=tot(pl.t);
 if(G.lsOn&&G.cg<CGL.length-1){const nx=CGL[G.cg+1];if(G.ls>=nx[1]&&army>=cap*CGR)o.push(['☯',`Đủ linh thạch đột phá <b>${nx[0]}</b> (tăng % quân dẫn theo).`,cgMenu])}
 if(!G.lsOn&&G.gold>3000&&army<cap*.7)o.push(['💰','Bạn đang dư vàng — vào thành phe ta để chiêu thêm lính.']);
 if(income()-wages()<0)o.push(['⚠️','Thu không đủ trả lương lính — cần chiếm thêm thành/làng hoặc bớt quân.']);
 if(isMyKing()&&!G.F.some((f,i)=>i!=pl.fac&&!f.dead&&atWar(pl.fac,i)&&OPEN(f.race==null?0:f.race)))o.push(['🏛','Bạn chưa có kẻ thù nào — tuyên chiến trong 📜 Thế cục → Ngoại giao.',()=>panel('ng')]);
 if(isMyKing()&&myGens().length<3&&G.open.length>1)o.push(['🧑‍✈️','Bạn có ít tướng — chiêu mộ thêm trong 📜 Thế cục → Tướng để họ đánh chiếm giúp.',()=>panel('tg')]);
 if(G.ac)o.push(['🤖','Đang bật Tự chinh phạt: nhân vật tự đi đánh. Bấm 🤖 để tắt nếu muốn tự điều khiển.']);
 return o}
let QC=null;
function qGo(q){const pl=P0();close();if(q.tgP){pl.goS=null;pl.goP=q.tgP;G.mk={x:q.tgP.x,y:q.tgP.y,t:3}}
 else if(q.tg){if(WOF(q.tg.race)!=WOF(contOf(pl.x,pl.y))){toast('🌀 Mục tiêu ở thế giới khác — đi qua Thông đạo 🌀 hoặc dùng 🌐 dịch chuyển.','#9ff0ff',1);tpMenu();return}
  pl.goP=null;pl.goS=q.tg;G.mk={x:q.tg.x,y:q.tg.y,t:3}}MC.follow=1;if(G.ac)acToggle();toast(`🚶 Đang tiến về <b>${q.tgP?pname(q.tgP):q.tg.name}</b>`,'#9cf')}
function qMenu(){if(!G||paused||mode!='map')return;const q=qCur();QC=q;const H=qHints();
 let h=`<p style="font-size:15px"><b>${q.ic} ${q.t}</b></p>${q.p!=null?`<div style="height:8px;background:#2a1d10;border-radius:4px;overflow:hidden;margin:4px 0 6px"><div style="height:100%;width:${qPct(q.p)};background:linear-gradient(90deg,#c9a052,#ffe08a)"></div></div>`:''}<p>${q.d}</p>`;
 if(H.length)h+=`<h3>💡 Gợi ý</h3>`+H.map((x,i)=>`<p style="font-size:13px">${x[0]} ${x[1]}${x[2]?` <a href="#" onclick="event.preventDefault();qHint(${i})" style="color:#ffd77a">mở ›</a>`:''}</p>`).join('');
 const b=[];if(q.tg||q.tgP)b.push([`📍 ${q.go||'Dẫn đường'}`,()=>qGo(q)]);if(q.act)b.push([q.act[0],()=>{close();q.act[1]()}]);
 b.push(['📖 Hướng dẫn đầy đủ',()=>{close();panel('hd')}],['Đóng',close]);menu('🎯 Việc nên làm tiếp',h,b)}
function qHint(i){const x=qHints()[i];if(x&&x[2]){close();x[2]()}}
function qTick(){const e=$('#cQ');if(!e||!G)return;if(mode!='map'){e.style.display='none';return}let q;try{q=qCur()}catch(err){e.style.display='none';return}
 e.style.display='';e.innerHTML=`🎯 ${q.t}`;const hs=qHints().length;e.classList.toggle('qh',hs>0)}
setInterval(qTick,1200);

/* ❓ chú thích các nút */
const ZLBL={zIn:'Phóng to',zOut:'Thu nhỏ',zMe:'Về chỗ bạn',zTp:'Dịch chuyển',zAc:'Tự chinh phạt (AI)',zTs:'Tốc độ thời gian',zTl:'Thiên Lộ · tầng trời',zSv:'Lưu ván',zCg:'Cảnh giới · linh thạch',zKg:'Vua của bạn',zCo:'La bàn chỉ hướng',zMu:'Âm thanh',zMap:'Màu bản đồ',zQ:'Đồ họa (máy giật chọn ⚡)',zFs:'Toàn màn hình',zMore:'Thêm nút',zHelp:'Tắt chú thích'};
for(const k in ZLBL){const e=document.getElementById(k);if(e)e.dataset.l=ZLBL[k]}
function lblSet(on,quiet){document.body.classList.toggle('lbl',!!on);if(G)G.lbl=on?1:2;if(on&&!quiet)toast('🏷 Đã hiện tên các nút. Bấm <b>❓</b> lần nữa để ẩn.<br><small>Chạm vào các ô số trên cùng (ngày, vàng, quân, tước) để xem giải thích.</small>','#ffe9a8')}
$('#zHelp').onclick=()=>{if(!G)return;lblSet(!document.body.classList.contains('lbl'))};
$('#cQ').onclick=()=>qMenu();
$('#cDay').onclick=()=>{if(!paused&&G)toast(`📅 <b>Ngày ${G.day}</b> trong game. Mỗi ngày làng & thành của bạn nộp vàng, tân binh tự tìm tới.${G.xian?' Nút ⏩ để tua nhanh thời gian.':''}`,'#ffe9a8')};
$('#cGold').addEventListener('click',()=>{if(paused||!G||G.lsOn)return;toast(`💰 <b>Vàng ${fmt(G.gold)}</b> · thu ${fmt(income())}/ngày · lương lính −${fmt(wages())}/ngày.<br>Dùng vàng để chiêu mộ lính (vào thành phe ta) và chiêu mộ tướng. Càng nhiều thành/làng càng thu nhiều.`,'#ffe9a8')});
$('#cArmy').addEventListener('click',()=>{if(paused||!G||G.lsOn)return;const pl=P0(),r=rank(pl);toast(`⚔ <b>Quân của bạn</b>: 🗡 bộ ${fmt(pl.t.inf)} · 🏹 cung ${fmt(pl.t.arc)} · 🐎 kỵ ${fmt(pl.t.cav)} = <b>${fmt(tot(pl.t))}</b> / tối đa ${fmt(r[1])}.<br>Tối đa phụ thuộc tước <b>${r[0]}</b> — lên tước để mang nhiều quân hơn.`,'#ffe9a8')});
const INTRO=`<p>Bạn là một <b>hiệp sĩ vô danh</b>. Hành trình: đánh thổ phỉ → chiếm thành → lên tước → <b>xưng Vua</b> → chinh phục thế giới, rồi tới những cõi bí ẩn hơn…</p>
<p><b>1. Điều khiển:</b> 👆 chạm đất để đi · chạm <b>thành/làng</b> để vào · chạm <b>đạo quân</b> để đuổi đánh · kéo để xem · chụm 2 ngón (hoặc ＋/－) để phóng to.</p>
<p><b>2. Không biết làm gì?</b> Nhìn ô <b style="color:#ffe08a">🎯 Nhiệm vụ</b> ở góc trên — chạm vào rồi bấm <b>📍 Dẫn đường</b>, nhân vật sẽ tự đi tới mục tiêu.</p>
<p><b>3. Màu:</b> <span style="color:#7dff8a">xanh = phe ta</span> · <span style="color:#ff6a5a">đỏ = kẻ thù</span> · trắng = đang hòa.</p>
<p><b>4. Không hiểu nút nào?</b> Bấm <b>❓</b> ở cột phải để hiện tên tất cả các nút (đang bật sẵn mấy ngày đầu).</p>`;
const GUIDE_X=`<p><b>💎 Linh thạch & ☯ Cảnh giới:</b> từ Cửu Thiên, vàng đổi thành linh thạch (1 triệu vàng = 1 hạ phẩm). Bấm ☯ để đột phá cảnh giới: tốn linh thạch, cần quân ≥30% giới hạn, thành công 50% (mỗi lần xịt +10%), xịt thì mất linh thạch và 20–40% quân. Cảnh giới càng cao càng dẫn được nhiều quân.</p>
<p><b>🏅 Danh hiệu:</b> đạt mốc (chiếm châu lục, số thành, danh vọng…) được danh hiệu, mỗi cái cộng thêm chút % quân. Bấm ô tước trên cùng để xem tất cả; chạm vào chồng danh hiệu trên đầu nhân vật để ẩn/hiện.</p>
<p><b>🌌 Tầng Trời:</b> chiếm 2/3 mỗi tầng thì được hỏi có muốn lên tầng tiếp. Tầng cũ đã chiếm vẫn giữ, quay về qua 🌌 Thiên Lộ. Tướng tự chinh phạt, tự lên tước.</p>
<p><b>💾 Lưu ván:</b> game tự lưu trên máy. Nút 💾 có 5 ô lưu, xuất file save để chơi tiếp trên máy khác.</p>`;
function GUIDE_D(){return`<details><summary>🚀 Bắt đầu nhanh</summary>${INTRO}</details>`+(GUIDE+GUIDE_X).split('</p>').filter(x=>x.trim()).map(x=>{const m=x.match(/<p><b>(.*?)<\/b>\s*([\s\S]*)/);return m?`<details><summary>${m[1].replace(/:\s*$/,'')}</summary><p>${m[2]}</p></details>`:x+'</p>'}).join('')}
