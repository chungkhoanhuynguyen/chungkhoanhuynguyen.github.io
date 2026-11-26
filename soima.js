/* A5 (26/11/2026) Trang /soi-ma-mien-phi.html: gõ mã → hiện ngay thẻ Soi 3 dòng (data/bctc/_soi.bin do soi3.py ghi) → nút gửi Zalo.
   Giải mã cùng thuật toán HD trong index.html (hncodec.py). Link nhanh: /soi-ma-mien-phi.html#HPG */
(function(){var F=document.getElementById("soima"),I=document.getElementById("soima-m"),O=document.getElementById("soima-o"),T=document.getElementById("soima-t");if(!F||!I||!O)return;
var K="hn-ck-2026-x7",S=null,P=null,D={xanh:"Ổn",vang:"Cần để ý",do:"Cảnh báo",xam:"Thiếu số"};
function e(x){return String(x==null?"":x).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function seed(n){var h=2166136261,s=unescape(encodeURIComponent(K+"|"+n));for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)>>>0}return h||1}
function xor(u,n){var s=seed(n);for(var i=0;i<u.length;i++){s^=s<<13;s>>>=0;s^=s>>>17;s^=s<<5;s>>>=0;u[i]^=s&255}return u}
function load(){if(P)return P;if(!window.DecompressionStream)return P=Promise.reject(new Error("old"));
P=fetch("/data/bctc/_soi.bin").then(function(r){if(!r.ok)throw new Error(r.status);return r.arrayBuffer()}).then(function(b){return new Response(new Blob([xor(new Uint8Array(b),"_soi")]).stream().pipeThrough(new DecompressionStream("deflate"))).text()}).then(function(t){S=JSON.parse(t);return S});return P}
function card(o){return '<section class="s3" id="soi3" aria-label="Soi 3 dòng báo cáo tài chính '+e(o.ma)+'"><h2>Soi 3 dòng BCTC '+e(o.ma)+'</h2><p class="s3k">Đèn xanh, vàng, đỏ cho 3 dòng hay giấu rủi ro nhất · số liệu tỷ đồng, BCTC hợp nhất đến '+e(o.ky)+' · <a href="/ma/'+e(o.ma)+'.html">Trang '+e(o.ma)+'</a></p><ul>'+o.rows.map(function(r){return '<li class="'+e(r.den)+'"><i aria-hidden="true"></i><div><b>'+e(r.ten)+(r.den=="na"?"":'<span class="s3d">'+(D[r.den]||"")+'</span>')+'</b>'+(r.so?'<div class="s3s">'+e(r.so)+'</div>':'')+'<p>'+e(r.cau)+'</p>'+(r.ky?'<small>Kỳ dữ liệu: '+e(r.ky)+'</small>':'')+'</div></li>'}).join("")+'</ul><p class="s3g">Đọc vẫn rối? <button type="button" data-soima="'+e(o.ma)+'">Gửi mã này để em soi cùng</button> <span class="s3t" aria-live="polite"></span></p></section>'}
function ma(){return(I.value||"").trim().toUpperCase().replace(/[^A-Z0-9]/g,"").slice(0,6)}
function show(m){if(m.length<3){O.innerHTML="";return}load().then(function(s){if(ma()!==m)return;var o=s[m];O.innerHTML=o?card(o):'<p class="note">Chưa có dữ liệu Soi 3 dòng cho mã '+e(m)+'. Anh chị bấm "Gửi qua Zalo", em xem trực tiếp.</p>';
try{if(window.hnDo&&o)hnDo("xem_soi3",{ma:m,noi:"trang_soi_ma"})}catch(x){}}).catch(function(){O.innerHTML='<p class="note">Trình duyệt này chưa mở được thẻ Soi 3 dòng. Anh chị bấm "Gửi qua Zalo", em soi trực tiếp.</p>'})}
var tm;I.addEventListener("input",function(){clearTimeout(tm);var m=ma();tm=setTimeout(function(){show(m)},250)});
F.addEventListener("submit",function(ev){ev.preventDefault();var m=ma();if(m.length<3){I.focus();return}var c="Em chào anh Huy, anh xem giúp em mã "+m+" với ạ.";
try{navigator.clipboard.writeText(c);T.textContent="Đã chép sẵn câu hỏi về mã "+m+". Mở Zalo xong anh chị chỉ cần dán và gửi."}catch(x){T.textContent="Mở Zalo xong anh chị nhắn: "+c}
try{if(window.hnDo)hnDo("soi_ma",{ma:m,noi:"trang_soi_ma"})}catch(x){}show(m);window.open("https://zalo.me/0365188286","_blank","noopener")});
var h=(location.hash.match(/^#([A-Za-z0-9]{3,6})$/)||[])[1]||(location.search.match(/[?&]ma=([A-Za-z0-9]{3,6})/)||[])[1];if(h){I.value=h.toUpperCase();show(ma())}})();
