/* Báo cáo tài chính đầy đủ trên trang mã cổ phiếu: Cân đối kế toán, KQKD, Lưu chuyển tiền tệ, Chỉ số tài chính – theo Quý/Năm */
(function(){
var el=document.getElementById('bctc');if(!el)return;var MA=el.getAttribute('data-ma'),K='hn-ck-2026-x7';
var css='#bctc{margin:10px 0 26px}#bctc .bt{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}#bctc .bt button{border:1px solid var(--line,#ccc);background:transparent;color:inherit;border-radius:999px;padding:7px 14px;font:inherit;font-size:14px;cursor:pointer}#bctc .bt button.on{background:var(--gold,#d6aa58);color:#111;border-color:transparent;font-weight:700}#bctc .bw{overflow-x:auto;border:1px solid var(--line,#ddd);border-radius:10px;max-height:640px}#bctc table{border-collapse:collapse;font-size:14px;min-width:100%}#bctc th,#bctc td{padding:7px 10px;border-bottom:1px solid var(--line,#eee);text-align:right;white-space:nowrap}#bctc th{position:sticky;top:0;background:var(--panel,#f6f6f6);z-index:2}#bctc td:first-child,#bctc th:first-child{text-align:left;position:sticky;left:0;background:var(--panel,#fafafa);white-space:normal;min-width:240px;max-width:340px;z-index:1}#bctc th:first-child{z-index:3}#bctc tr.l1 td:first-child{font-weight:700}#bctc tr.l2 td:first-child{padding-left:24px}#bctc tr.l3 td:first-child,#bctc tr.l4 td:first-child{padding-left:40px;font-size:13px}#bctc tr.an{display:none}#bctc .ng{color:#e5534f}#bctc .nt{font-size:13px;opacity:.75;margin-top:6px}#bctc .tg{cursor:pointer;user-select:none}#bctc .tg:before{content:"▸ ";opacity:.6}#bctc .tg.mo:before{content:"▾ "}';
var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
function seed(n){var h=2166136261,s=unescape(encodeURIComponent(K+'|'+n));for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)>>>0}return h||1}
function xor(u,n){var s=seed(n);for(var i=0;i<u.length;i++){s^=s<<13;s>>>=0;s^=s>>>17;s^=s<<5;s>>>=0;u[i]^=s&255}return u}
function inflate(u){if(window.DecompressionStream){return new Response(new Blob([u]).stream().pipeThrough(new DecompressionStream('deflate'))).text()}
 return new Promise(function(ok,no){var s=document.createElement('script');s.src='/zl.js?v=082';s.onload=function(){ok(new TextDecoder().decode(window.fflate.unzlibSync(u)))};s.onerror=no;document.head.appendChild(s)})}
var D,T='bs',P='q',MO=false;
function nf(v){if(v===null||v===undefined)return '–';var a=Math.abs(v),s=a.toLocaleString('vi-VN',{minimumFractionDigits:1,maximumFractionDigits:1});return v<0?'<span class="ng">-'+s+'</span>':s}
function lab(d,p){var y=d.slice(0,4),m=+d.slice(5,7);return p=='q'?'Q'+Math.ceil(m/3)+'/'+y:y}
function find(rows,re){for(var i=0;i<rows.length;i++)if(re.test(rows[i][0]))return rows[i][2];return null}
function ratios(){var R=D[P],bs=R.bs||[],is=R.is||[],n=R.d.length,out=[],bank=D.f=='bank';
 var ln=find(is,/^lợi nhuận sau thuế (của )?(cổ đông (của )?)?công ty mẹ|^lợi nhuận sau thuế (của )?chủ sở hữu|^lnst (của )?công ty mẹ/i)||find(is,/^lợi nhuận sau thuế/i);
 var vc=find(bs,/^vốn chủ sở hữu$|^tổng vốn chủ sở hữu|^vốn chủ sở hữu và lợi ích/i)||find(bs,/^vốn chủ sở hữu/i),ts=find(bs,/TỔNG CỘNG TÀI SẢN|tổng tài sản/i);
 function row(name,f,pct){var v=[];for(var i=0;i<n;i++){var x=f(i);v.push(x===null||!isFinite(x)?null:Math.round(x*(pct?1000:10))/10)}out.push([name,1,v,pct])}
 var k=P=='q'?4:1;
 function yoy(a){return function(i){return a&&a[i+(P=='q'?4:1)]&&a[i+(P=='q'?4:1)]>0&&a[i]!==null?(a[i]/a[i+(P=='q'?4:1)]-1)*100:null}}
 if(ln&&vc)row('ROE '+(P=='q'?'(quý, quy năm)':'(năm)')+' %',function(i){return vc[i]?ln[i]*k/vc[i]*100:null});
 if(ln&&ts)row('ROA '+(P=='q'?'(quý, quy năm)':'(năm)')+' %',function(i){return ts[i]?ln[i]*k/ts[i]*100:null});
 if(ln)row('Tăng trưởng LNST so với cùng kỳ %',yoy(ln));
 if(bank){var tn=find(is,/^thu nhập lãi thuần/i),toi=find(is,/tổng thu nhập hoạt động/i),cp=find(is,/^chi phí hoạt động$|^chi phí quản lý doanh nghiệp|^tổng chi phí hoạt động/i),dp=find(is,/^chi phí dự phòng rủi ro tín dụng/i),cv=find(bs,/^cho vay khách hàng|cho vay và cho thuê tài chính khách hàng/i),tg=find(bs,/^tiền gửi của khách hàng/i);
  if(tn)row('Tăng trưởng thu nhập lãi thuần %',yoy(tn));
  if(cp&&toi)row('Chi phí hoạt động / Tổng thu nhập (CIR) %',function(i){return toi[i]?Math.abs(cp[i])/toi[i]*100:null});
  if(dp&&toi)row('Chi phí dự phòng / Tổng thu nhập %',function(i){return toi[i]?Math.abs(dp[i])/toi[i]*100:null});
  if(cv&&tg)row('Cho vay / Tiền gửi khách hàng %',function(i){return tg[i]?cv[i]/tg[i]*100:null});
  if(vc&&ts)row('Vốn chủ sở hữu / Tổng tài sản %',function(i){return ts[i]?vc[i]/ts[i]*100:null});
 }else{var dt=find(is,/doanh thu thuần|^doanh thu hoạt động|cộng doanh thu hoạt động/i),lg=find(is,/lợi nhuận gộp/i),nv=find(bs,/^nợ phải trả|^NỢ PHẢI TRẢ/i),vay=find(bs,/vay và nợ thuê tài chính ngắn hạn/i),vayd=find(bs,/vay và nợ thuê tài chính dài hạn/i);
  if(dt)row('Tăng trưởng doanh thu %',yoy(dt));
  if(lg&&dt)row('Biên lợi nhuận gộp %',function(i){return dt[i]?lg[i]/dt[i]*100:null});
  if(ln&&dt)row('Biên lợi nhuận ròng %',function(i){return dt[i]?ln[i]/dt[i]*100:null});
  if(nv&&vc)row('Nợ phải trả / Vốn chủ sở hữu (lần)',function(i){return vc[i]?nv[i]/vc[i]:null});
  if(vay&&vc)row('Vay nợ tài chính / Vốn chủ sở hữu (lần)',function(i){return vc[i]?((vay[i]||0)+((vayd&&vayd[i])||0))/vc[i]:null});}
 return out}
function draw(){var R=D[P];if(!R||!R.d){el.querySelector('.bw').innerHTML='<p style="padding:12px">Chưa có dữ liệu.</p>';return}
 var rows=T=='cs'?ratios():(R[T]||[]),h='<table><tr><th>'+(T=='cs'?'Chỉ số':'Chỉ tiêu (tỷ đồng)')+'</th>'+R.d.map(function(d){return '<th>'+lab(d,P)+'</th>'}).join('')+'</tr>';
 rows.forEach(function(r,i){var nx=rows[i+1],con=nx&&nx[1]>r[1];h+='<tr class="l'+r[1]+(r[1]>1&&!MO&&T!='cs'?' an':'')+'" data-l="'+r[1]+'"><td'+(con&&T!='cs'?' class="tg'+(MO?' mo':'')+'"':'')+'>'+r[0]+'</td>'+r[2].map(function(v){return '<td>'+(r[3]&&v!==null?(v<0?'<span class="ng">':'')+v.toLocaleString('vi-VN',{maximumFractionDigits:1})+(v<0?'</span>':''):nf(v))+'</td>'}).join('')+'</tr>'});
 el.querySelector('.bw').innerHTML=h+'</table>';
 el.querySelectorAll('.tg').forEach(function(td){td.onclick=function(){var tr=td.parentNode,l=+tr.getAttribute('data-l'),open=!td.classList.contains('mo');td.classList.toggle('mo');var n=tr.nextElementSibling;while(n&&+n.getAttribute('data-l')>l){if(open){if(+n.getAttribute('data-l')==l+1)n.classList.remove('an')}else{n.classList.add('an');var t=n.querySelector('.tg');if(t)t.classList.remove('mo')}n=n.nextElementSibling}}})}
function ui(){var tabs=[['bs','Cân đối kế toán'],['is','Kết quả kinh doanh'],['cf','Lưu chuyển tiền tệ'],['cs','Chỉ số tài chính']];
 el.innerHTML='<div class="bt">'+tabs.map(function(t){return '<button data-t="'+t[0]+'"'+(t[0]==T?' class="on"':'')+'>'+t[1]+'</button>'}).join('')+'</div><div class="bt"><button data-p="q" class="on">Theo quý</button><button data-p="y">Theo năm</button><button data-mo="1">Mở rộng tất cả</button></div><div class="bw"></div><p class="nt">Đơn vị: tỷ đồng. Nguồn: BCTC hợp nhất doanh nghiệp công bố, cập nhật hằng tuần. Chỉ số do Chứng Khoán Huy Nguyễn tính từ BCTC. Bấm ▸ để xem chi tiết từng khoản.</p>';
 el.querySelectorAll('[data-t]').forEach(function(b){b.onclick=function(){T=b.getAttribute('data-t');el.querySelectorAll('[data-t]').forEach(function(x){x.classList.toggle('on',x==b)});draw()}});
 el.querySelectorAll('[data-p]').forEach(function(b){b.onclick=function(){P=b.getAttribute('data-p');el.querySelectorAll('[data-p]').forEach(function(x){x.classList.toggle('on',x==b)});draw()}});
 var bm=el.querySelector('[data-mo]');bm.onclick=function(){MO=!MO;bm.textContent=MO?'Thu gọn':'Mở rộng tất cả';draw()};draw()}
fetch('/data/bctc/'+MA+'.bin').then(function(r){if(!r.ok)throw 0;return r.arrayBuffer()}).then(function(b){return inflate(xor(new Uint8Array(b),MA))}).then(function(t){D=JSON.parse(t);ui()}).catch(function(){el.innerHTML='<p>Chưa tải được báo cáo tài chính. Thử tải lại trang.</p>'});
})();
