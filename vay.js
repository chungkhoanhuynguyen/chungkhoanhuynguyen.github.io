/* C1 (Phòng Web 28/11): máy tính vay mua nhà, đất – trả gốc đều hoặc trả đều hằng tháng, lãi ưu đãi rồi thả nổi. Chạy hoàn toàn trên máy người dùng. */
(function(){
var $=function(i){return document.getElementById(i)},F=$('vayf');if(!F)return;
function num(i){var v=String($(i).value).replace(/\./g,'').replace(',','.');v=parseFloat(v);return isFinite(v)&&v>=0?v:0}
function vn(x,d){return (+x).toLocaleString('vi-VN',{maximumFractionDigits:d==null?0:d})}
function tr(x){return vn(x/1e6,x>=1e8?0:1)}
function lich(P,n,m1,r1,r2,deu){var rows=[],du=P,tl=0;for(var k=1;k<=n;k++){var r=(k<=m1?r1:r2)/1200,lai=du*r,goc;
 if(deu){goc=P/n}else{var con=n-k+1;var a=r?du*r/(1-Math.pow(1+r,-con)):du/con;goc=a-lai}
 if(k===n)goc=du;du-=goc;tl+=lai;rows.push([k,goc+lai,goc,lai,Math.max(du,0)])}return {rows:rows,tl:tl}}
function tinh(){var P=num('vay-so')*1e6,y=num('vay-nam'),m1=Math.round(num('vay-ud-thang')),r1=num('vay-ud'),r2=num('vay-tn'),tn=num('vay-thu')*1e6,deu=$('vay-kieu').value==='goc';
 var n=Math.round(y*12),o=$('vay-o');if(!P||!n){o.innerHTML='<p>Nhập số tiền vay và số năm.</p>';return}
 m1=Math.min(m1,n);var L=lich(P,n,m1,r1,r2,deu),R=L.rows,a=R[0][1],b=m1<n?R[m1][1]:null,mx=0;R.forEach(function(x){if(x[1]>mx)mx=x[1]});
 var h='<div class="vk"><div><p class="k">Tháng đầu trả</p><p class="v">'+tr(a)+' tr</p></div>';
 if(b!==null)h+='<div><p class="k">Tháng '+(m1+1)+' (hết ưu đãi)</p><p class="v do">'+tr(b)+' tr</p></div>';
 h+='<div><p class="k">Tổng tiền lãi</p><p class="v">'+tr(L.tl)+' tr</p></div><div><p class="k">Tổng phải trả</p><p class="v">'+tr(P+L.tl)+' tr</p></div></div>';
 if(b!==null&&b>a)h+='<p>Hết ưu đãi, tiền trả mỗi tháng tăng thêm <b>'+tr(b-a)+' triệu</b> ('+vn((b/a-1)*100,0)+'%).</p>';
 if(tn>0){var p=mx/tn*100;h+='<p class="'+(p>30?'xau':'tot')+'">Tháng trả cao nhất <b>'+tr(mx)+' triệu</b> = <b>'+vn(p,0)+'% thu nhập</b>. '+(p>30?'Vượt mốc 30% của phép thử nợ: thu nhập giảm hoặc lãi tăng là áp lực ngay.':'Trong mốc 30% của phép thử nợ.')+'</p>'}
 var s=[1,2,3,6,12,m1,m1+1,24,36,60,120,n].filter(function(k,i,A){return k>=1&&k<=n&&A.indexOf(k)===i}).sort(function(x,y){return x-y});
 h+='<div style="overflow-x:auto"><table class="mt"><tr><td><b>Tháng</b></td><td class="r"><b>Phải trả</b></td><td class="r"><b>Gốc</b></td><td class="r"><b>Lãi</b></td><td class="r"><b>Còn nợ</b></td></tr>'+s.map(function(k){var x=R[k-1];return '<tr><td>'+k+'</td><td class="r"><b>'+tr(x[1])+'</b></td><td class="r">'+tr(x[2])+'</td><td class="r">'+tr(x[3])+'</td><td class="r">'+tr(x[4])+'</td></tr>'}).join('')+'</table></div><p class="vgt">Đơn vị: triệu đồng. Kết quả tính theo số anh chị nhập, chưa gồm phí trả nợ trước hạn, bảo hiểm khoản vay.</p>';
 o.innerHTML=h}
F.addEventListener('input',tinh);F.addEventListener('change',tinh);F.addEventListener('submit',function(e){e.preventDefault();tinh()});tinh();
})();
