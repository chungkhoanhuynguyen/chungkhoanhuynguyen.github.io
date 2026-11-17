/* ================= LINH THẠCH & CẢNH GIỚI (từ Cửu Thiên Huyền Giới) =================
 1.000.000 vàng = 1 linh thạch hạ phẩm · 100 hạ = 1 trung · 100 trung = 1 thượng phẩm.
 Linh thạch dùng để đột phá cảnh giới; cảnh giới nhân giới hạn quân dẫn theo (quân = tu vi). */
const LSR=1e6,LSKEEP=2e6,CGR=.3;
const CGL=[['Phàm Thể',0,1],['Luyện Khí',1,1.2],['Trúc Cơ',3,1.4],['Kim Đan',8,1.7],['Nguyên Anh',20,2],['Hóa Thần',50,2.4],['Luyện Hư',100,2.8],['Hợp Thể',200,3.3],['Đại Thừa',400,3.9],['Độ Kiếp',800,4.6],['Chân Tiên',1500,5.4],['Kim Tiên',3000,6.3],['Thái Ất Kim Tiên',5000,7.4],['Đại La Kim Tiên',8000,8.7],['Chuẩn Thánh',12000,10],['Thánh Nhân',20000,12]];
const CGP=[0,.2,.45,.75,1.1,1.5,1.95,2.45,3,3.6,4.3,5.1,6,7,8.2,9.5],cgP=g=>CGP[Math.min(g==null?((G&&G.cg)||0):g,CGP.length-1)];
const cgM=()=>G&&G.cg?CGL[Math.min(G.cg,CGL.length-1)][2]:1;
const cgN=()=>CGL[Math.min((G&&G.cg)||0,CGL.length-1)][0];
function fmtLS(n){n=Math.max(0,Math.floor(n||0));const c=Math.floor(n/10000),t=Math.floor(n%10000/100),h=n%100,a=[];if(c)a.push(`${fmt(c)} thượng`);if(t)a.push(`${t} trung`);if(h||!a.length)a.push(`${h} hạ`);return a.join(' · ')}
function lsInit(){if(!G||!G.xian||G.lsOn)return;G.lsOn=1;G.ls=G.ls||0;G.cg=G.cg||0;if(G.lsAuto==null)G.lsAuto=1;const k=Math.floor(Math.max(0,G.gold-LSKEEP)/LSR);if(k>0){G.ls+=k;G.gold-=k*LSR}
 setTimeout(()=>toast(`💎 <b>LINH THẠCH</b> — tiền tệ của giới tu tiên!<br>${k?`Đã đổi ${fmt(k*LSR)} vàng thành <b>${fmtLS(k)}</b> linh thạch.<br>`:''}1.000.000 vàng = 1 hạ phẩm · 100 hạ = 1 trung · 100 trung = 1 thượng<br><small>Dùng linh thạch để ☯ đột phá cảnh giới — cảnh giới càng cao dẫn càng nhiều quân (quân chính là tu vi)</small>`,'#9ff0ff',1),2500);addLog('💎 Mở linh thạch & cảnh giới tu tiên.','#9ff0ff')}
function lsDay(){if(!G.lsOn)return;if(G.lsAuto){const k=Math.floor(Math.max(0,G.gold-LSKEEP)/LSR);if(k>0){G.ls+=k;G.gold-=k*LSR}}}
function lsGain(s,p){if(!G.lsOn||s.race<9||!G.L[0]||p.fac!=G.L[0].fac)return;const k=Math.max(1,Math.round([5,2,1][s.type]*(s.race==12?TMv():1)));G.ls+=k;if(p.kind=='pl')mfx.push({x:s.x,y:s.y-40,s:`+${k} 💎`,c:'#9ff0ff',t:2})}
function cgUp(){const n=(G.cg||0)+1;if(n>=CGL.length)return;const c=CGL[n][1],pl=P0(),cap=rank(pl)[1];if(G.ls<c){toast(`Cần ${fmtLS(c)} linh thạch`,'#f88');return}if(tot(pl.t)<cap*CGR){toast(`Tu vi chưa đủ — cần quân đạt ${CGR*100}% giới hạn (${fmt(Math.ceil(cap*CGR))}) mới đột phá được`,'#f88');return}
 G.ls-=c;G.cg=n;close();save();thienKiep(n>=10?6:3,`☯ ĐỘT PHÁ ${CGL[n][0].toUpperCase()}`,`${CGL[n][0].toUpperCase()}!`,()=>{toast(`☯ <b>ĐỘT PHÁ ${CGL[n][0].toUpperCase()}!</b><br>Thiên địa linh khí cuồn cuộn đổ về — giới hạn quân dẫn theo ${G.lk?'+'+Math.round(cgP(n)*100)+'%':'×'+CGL[n][2]} (tối đa ${fmt(rank(pl)[1])})`,'#bfffd8',1);addLog(`☯ Đột phá cảnh giới ${CGL[n][0]}.`,'#bfffd8')},1)}
function cgMenu(){if(!G||!G.lsOn)return;const pl=P0(),cap=rank(pl)[1],n=G.cg||0,nx=CGL[n+1],tv=tot(pl.t);
 let h=`<p>💎 Linh thạch: <b>${fmtLS(G.ls)}</b> · 💰 ${fmt(G.gold)} vàng</p><p>☯ Cảnh giới: <b>${cgN()}</b> · Tu vi (quân dẫn theo): <b>${fmt(tv)}</b> / ${fmt(cap)}</p>`;
 h+='<div style="max-height:34vh;overflow:auto;font-size:12.5px;line-height:1.5">'+CGL.map((c,i)=>`<div style="color:${i<n?'#9c9':i==n?'#ffe066':i==n+1?'#c9b8ff':'#778'}">${i<n?'✅':i==n?'☯':i==n+1?'🔮':'·'} ${c[0]} — giới hạn quân ${G.lk?'+'+Math.round(cgP(i)*100)+'%':'×'+c[2]}${i>0?` · ${fmtLS(c[1])}`:''}</div>`).join('')+'</div>';
 h+=`<p style="font-size:12px;color:#cdb">Linh thạch có được khi đổi vàng (tự đổi phần vàng vượt ${fmt(LSKEEP)} mỗi ngày nếu bật) và khi chiếm thành ở Cửu Thiên / Tầng Trời. Đột phá cần tu vi (quân dẫn theo) đạt ${CGR*100}% giới hạn.</p>`;
 const b=[];if(nx){const okL=G.ls>=nx[1],okT=tv>=cap*CGR;b.push([`☯ Đột phá ${nx[0]} (${fmtLS(nx[1])})${okL&&okT?'':`<br><small style="color:#f99">${!okL?'thiếu linh thạch':''}${!okL&&!okT?' · ':''}${!okT?`cần tu vi ${fmt(Math.ceil(cap*CGR))} (${CGR*100}% giới hạn) — đang ${fmt(tv)}`:''}</small>`}`,cgUp])}
 const k=Math.floor(G.gold/LSR);b.push([`💱 Đổi ${fmt(k*LSR)} vàng → ${fmtLS(k)}`,()=>{G.ls+=k;G.gold-=k*LSR;cgMenu()},k<1]);
 b.push([`🔁 Tự đổi vàng thừa mỗi ngày: ${G.lsAuto?'BẬT':'TẮT'}`,()=>{G.lsAuto=G.lsAuto?0:1;cgMenu()}],['Đóng',close]);menu('☯ Cảnh giới & 💎 Linh thạch',h,b)}
