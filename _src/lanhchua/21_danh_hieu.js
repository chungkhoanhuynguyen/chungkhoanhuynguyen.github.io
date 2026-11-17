/* ================= DANH HIỆU (chứng minh thực lực, mỗi danh hiệu tăng giới hạn quân) ================= */
const DHL=[
 ['ch4','Bá Chủ Tứ Châu','🗺','#7fe3ff',.10,()=>G.open&&G.open.includes(4),'Mở Vùng Đất Chết'],
 ['tv','Diệt Tử Vực Ma','💀','#c58cff',.12,()=>G.divine,'Chiếm 1/2 Vùng Đất Chết'],
 ['tg','Chinh Phạt Thần Giới','⚡','#fff07a',.15,()=>G.xian,'Chiếm 2/4 lục địa Thần linh'],
 ['lk','Linh Khí Chi Chủ','✨','#bfffd8',.15,()=>G.lk,'Mở Thời đại Linh khí'],
 ['pt','Phi Thăng Giả','🌌','#d8c8ff',.20,()=>G.tang,'Phi thăng lên Tầng Trời'],
 ...[1,5,10,15,20,23].map(n=>['t'+n,`Chinh Phạt ${n} Tầng Trời`,'☁️','#c9e6ff',.10,()=>(G.tdone||0)>=n,`Bình định ${n} tầng trời`]),
 ['dd','Đại Đế Vạn Giới','🐲','#ffe066',.50,()=>G.dd,'Thống nhất Tiên Giới'],
 ...[[50,'Lãnh Chúa Ngũ Thập Thành'],[150,'Bá Chủ Bách Thành'],[300,'Vương Giả Tam Bách Thành'],[600,'Hoàng Giả Lục Bách Thành'],[1000,'Đế Quân Thiên Thành']].map(([n,s])=>['s'+n,s,'🏯','#ffcf3a',.08,()=>dhS()>=n,`Giữ ${n} thành`]),
 ...[[1e4,'Thanh Danh Lừng Lẫy'],[1e5,'Danh Chấn Thiên Hạ'],[1e6,'Vạn Cổ Lưu Danh'],[1e7,'Thiên Địa Đồng Tôn']].map(([n,s])=>['r'+n,s,'⭐','#ffd27a',.08,()=>(P0().ren||0)>=n,`Đạt ${fmt(n)} danh vọng`]),
 ...[[30,'Chủ Soái Tam Thập Tướng'],[100,'Bách Tướng Triều Bái']].map(([n,s])=>['g'+n,s,'🎖','#ff9a6a',.06,()=>myGens().length>=n,`Có ${n} tướng`]),
 ...[[1000,'Thiên Niên Bá Nghiệp'],[3000,'Vạn Thế Trường Tồn']].map(([n,s])=>['d'+n,s,'⏳','#c9b8a0',.05,()=>G.day>=n,`Sống tới ngày ${n}`]),
 ...[[100,'Linh Thạch Phú Hộ'],[10000,'Phú Khả Địch Thiên']].map(([n,s])=>['l'+n,s,'💎','#9ff0ff',.05,()=>(G.ls||0)>=n,`Có ${fmtLS(n)} linh thạch`])];
let DHS=-1;const dhS=()=>DHS>=0?DHS:(DHS=S.filter(s=>s.fac==P0().fac).length);
function dhList(){const me=P0().fac,o=[];for(const d of DHL){try{if(d[5]())o.push({id:d[0],n:d[1],ic:d[2],c:d[3],b:d[4]})}catch(e){}}
 if(G.ch)G.ch.forEach((f,c)=>{if(f===me&&CHT[c])o.push({id:'ch'+c,n:CHT[c][0],ic:CHT[c][1],c:CHT[c][2],b:.10})});return o}
function dhUpdate(quiet){if(!G||!G.L)return;DHS=-1;const L=dhList();G.dhm=1+L.reduce((a,d)=>a+d.b,0);G.dhv=L.sort((a,b)=>b.b-a.b).map(d=>[d.n,d.ic,d.c]);
 const old=new Set(G.dhid||[]),nw=L.filter(d=>!old.has(d.id));G.dhid=L.map(d=>d.id);
 if(!quiet&&old.size&&nw.length)for(const d of nw.slice(0,3)){toast(`🏅 Đạt danh hiệu <b style="color:${d.c}">${d.ic} ${d.n}</b><br>Giới hạn quân +${Math.round(d.b*100)}%`,d.c,1);addLog(`🏅 Đạt danh hiệu ${d.n}.`,d.c)}}
const dhM=()=>G&&G.dhm||1;
function dhMenu(){if(!G)return;dhUpdate(1);const L=dhList(),have=new Set(L.map(d=>d.id));let h=`<p>Mỗi danh hiệu tăng giới hạn quân dẫn theo. Hiện có <b>${L.length}</b> danh hiệu → ${G.lk?`giới hạn quân <b>${Math.round(plPct()*100)}%</b> sức mạnh chuẩn của tiên nhân (200% gốc + ${Math.round((dhM()-1)*100)}% danh hiệu + ${Math.round(cgP()*100)}% cảnh giới)`:`giới hạn quân <b>×${dhM().toFixed(2)}</b>${G.cg?` · cảnh giới ×${cgM()}`:''}`}</p><div style="max-height:52vh;overflow:auto;font-size:13px;line-height:1.6">`;
 h+=L.sort((a,b)=>b.b-a.b).map(d=>`<div><span style="color:${d.c}">${d.ic} <b>${d.n}</b></span> <small style="color:#9c9">+${Math.round(d.b*100)}%</small></div>`).join('');
 const lock=DHL.filter(d=>!have.has(d[0]));if(lock.length){h+='<div style="margin-top:6px;color:#889">— Chưa đạt —</div>';let shown=0;const seen=new Set();for(const d of lock){const g=d[0].replace(/\d+$/,'');if(seen.has(g))continue;seen.add(g);if(shown++>8)break;h+=`<div style="color:#778">🔒 ??? <small>(${d[6]} · +${Math.round(d[4]*100)}%)</small></div>`}}
 h+='</div>';menu('🏅 Danh hiệu',h,[[`👁 Hiện trên đầu: ${G.dhAll?'TẤT CẢ danh hiệu':'chỉ '+(SMALL()?3:6)+' danh hiệu mạnh nhất'} (bấm để đổi)`,()=>{G.dhAll=G.dhAll?0:1;dhMenu()}],['Đóng',close]])}
function dhPlates(x,y,t){const v=G&&G.dhv;if(!v||!v.length)return;const mx=G.dhAll?99:SMALL()?3:6,n=Math.min(mx,v.length);X.textAlign='center';X.font='800 9.5px system-ui,sans-serif';
 for(let i=0;i<n;i++){const [s,ic,c]=v[i],yy=y-i*15,l=ic+' '+s,tw=X.measureText(l).width+12,gl=.6+Math.sin(t*2.5+i)*.4;
  X.fillStyle='rgba(14,10,24,.82)';X.beginPath();X.moveTo(x-tw/2,yy-10);X.lineTo(x+tw/2,yy-10);X.lineTo(x+tw/2+5,yy-4.5);X.lineTo(x+tw/2,yy+1);X.lineTo(x-tw/2,yy+1);X.lineTo(x-tw/2-5,yy-4.5);X.closePath();X.fill();
  X.strokeStyle=c;X.globalAlpha=.55+.45*gl;X.lineWidth=1.2;X.stroke();X.globalAlpha=1;X.fillStyle=c;X.fillText(l,x,yy-1.5)}
 if(v.length>n){X.font='700 9px system-ui';X.fillStyle='#ffe9a8';X.fillText(`+${v.length-n} danh hiệu`,x,y-n*15)}}
const dhN=()=>{const v=G&&G.dhv;if(!v||!v.length)return 0;const mx=G.dhAll?99:SMALL()?3:6;return Math.min(mx,v.length)+(v.length>mx?1:0)};
