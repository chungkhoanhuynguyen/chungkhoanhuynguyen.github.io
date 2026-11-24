/* Giá trực tiếp trên trang từng mã: nguồn công khai VPS, lấy ngay trên máy người xem */
(function(){var el=document.getElementById('rtpx');if(!el||!window.fetch)return;var s=el.getAttribute('data-s');
function ses(){var t=new Date(Date.now()+7*36e5),w=t.getUTCDay(),m=t.getUTCHours()*60+t.getUTCMinutes();return w>=1&&w<=5&&m>=540&&m<=915}
function nf(x){return x.toLocaleString('vi-VN',{minimumFractionDigits:2,maximumFractionDigits:2})}
function sg(x){return x>0?'+':x<0?'−':''}
var mo=null;function chk(){return fetch('https://bgapidatafeed.vps.com.vn/getlistindexdetail/10',{cache:'no-store',credentials:'omit'}).then(function(r){return r.json()}).then(function(a){mo=!(a&&a[0]&&a[0].status==='E')}).catch(function(){mo=false})}
function go(){(mo===null?chk():Promise.resolve()).then(function(){return fetch('https://bgapidatafeed.vps.com.vn/getliststockdata/'+s,{cache:'no-store',credentials:'omit'}).then(function(r){return r.json()}).then(function(a){var x=a&&a[0];if(!x)return;var r=+x.r,c=+x.lastPrice||r;if(!(r>0))return;
 var d=c-r,p=d/r*100,cl=Math.abs(d)<.005?'':d>0?'up':'dn',v=(+x.lot||0)*10,on=ses()&&mo;
 el.innerHTML=(on?'Giá trực tiếp':'Phiên gần nhất')+': <b class="'+cl+'">'+nf(c)+'</b> <span class="'+cl+'">'+sg(d)+nf(Math.abs(d))+' ('+sg(p)+nf(Math.abs(p))+'%)</span> · KL khớp '+v.toLocaleString('vi-VN')+' cp · TC '+nf(r)+' · Trần '+nf(+x.c)+' · Sàn '+nf(+x.f)+(on?' · lúc '+new Date().toLocaleTimeString('vi-VN',{hour:'2-digit',minute:'2-digit'}):'');
 el.hidden=false})}).catch(function(){})}
go();setInterval(function(){if(!document.hidden&&ses()){mo=null;go()}},20000)})();
