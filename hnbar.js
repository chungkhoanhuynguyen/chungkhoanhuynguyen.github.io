/* A3 (26/11/2026) Thanh nút cố định đáy màn hình điện thoại: "Nhắn Zalo" + "Soi mã miễn phí". Cao 56px, chừa chỗ cuối trang (không che nội dung),
   ẩn khi đang gõ (bàn phím mở). Trang mã /ma/XXX.html: nút Soi dẫn tới /soi-ma-mien-phi.html#XXX. Gắn mọi trang qua _ads.py. */
(function(){var W=window,d=document;if(!W.matchMedia||!W.matchMedia("(max-width:760px)").matches||d.getElementById("hnbar"))return;
var p=location.pathname,m=(p.match(/^\/ma\/([A-Z0-9]{3,6})\.html$/)||[])[1],trangSoi=/soi-ma-mien-phi/.test(p);
var st=d.createElement("style");st.textContent="#hnbar{position:fixed;left:0;right:0;bottom:0;z-index:95;display:flex;gap:8px;padding:6px 10px calc(6px + env(safe-area-inset-bottom,0px));background:rgba(33,16,48,.96);border-top:1px solid rgba(243,210,122,.35);box-shadow:0 -6px 18px -10px rgba(0,0,0,.5);transition:transform .2s ease;font-family:\"Be Vietnam Pro\",system-ui,sans-serif}"+
"#hnbar a{flex:1 1 0;display:flex;align-items:center;justify-content:center;gap:6px;min-height:44px;border-radius:10px;font-weight:700;font-size:15px;line-height:1.2;font-family:inherit;text-decoration:none;white-space:nowrap}"+
"#hnbar .z{background:#0068ff;color:#fff}#hnbar .s{background:#f3d27a;color:#2a1640}#hnbar.an{transform:translateY(110%)}"+
"body.hnbar{padding-bottom:calc(64px + env(safe-area-inset-bottom,0px))}body.hnbar #totop{bottom:calc(72px + env(safe-area-inset-bottom,0px))!important}"+
"@media(prefers-reduced-motion:reduce){#hnbar{transition:none}}";d.head.appendChild(st);
var b=d.createElement("nav");b.id="hnbar";b.setAttribute("aria-label","Liên hệ nhanh");
b.innerHTML='<a class="z" href="https://zalo.me/0365188286" rel="noopener">Nhắn Zalo</a>'+(trangSoi?'':'<a class="s" href="/soi-ma-mien-phi.html'+(m?'#'+m:'')+'">Soi '+(m?m:'mã')+' miễn phí</a>');
var vis={};function go(){d.body.appendChild(b);d.body.classList.add("hnbar");var h=d.querySelector(".hero-act")||d.getElementById("soima");if(h&&W.IntersectionObserver){var sm=d.getElementById("soima")||h;var io=new IntersectionObserver(function(es){es.forEach(function(e){vis[e.target===h?"a":"b"]=e.isIntersecting});b.classList.toggle("an",!!(vis.a||vis.b))});io.observe(h);if(sm!==h)io.observe(sm)}}
if(d.body)go();else d.addEventListener("DOMContentLoaded",go);
b.addEventListener("click",function(ev){var a=ev.target.closest&&ev.target.closest("a.s");if(a)try{if(W.hnDo)hnDo("bar_soi",{ma:m||""})}catch(x){}});
function go2(ev){var t=ev.target,g=t&&/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)&&!/^(button|submit|checkbox|radio)$/i.test(t.type||"");if(g)b.classList.add("an")}
d.addEventListener("focusin",go2);d.addEventListener("focusout",function(){setTimeout(function(){var a=d.activeElement;if(!a||!/^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName))if(!(vis.a||vis.b))b.classList.remove("an")},120)});})();

/* 26/11 QL1: bảng trên điện thoại không bị cắt cột.
   - Bảng ≤6 cột: thu gọn chữ/khoảng cách cho vừa màn hình.
   - Bảng nhiều cột dạng danh sách (lệnh, mã…): đổi thành thẻ, mỗi ô có nhãn cột.
   - Bảng số liệu theo quý/năm (BCTC): giữ vuốt ngang, khoá cột đầu + dòng "Vuốt ngang xem thêm". */
(function(){var W=window,d=document;if(!W.matchMedia||!W.matchMedia("(max-width:600px)").matches)return;
var st=d.createElement("style");st.textContent=
"table.tfit{font-size:13px!important;table-layout:auto;min-width:0!important;width:100%!important}table.tfit th,table.tfit td{padding:6px 5px!important;white-space:normal!important;word-break:normal}table.tfit th{font-size:11.5px!important;line-height:1.25}"+
"table.tcard small{max-width:none!important;white-space:normal!important}table.tcard tr.thd{display:none!important}table.tcard,table.tcard tbody{display:block!important;width:100%!important;min-width:0!important}table.tcard thead{display:none!important}"+
"table.tcard tr{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px 10px;padding:10px 10px;border-bottom:1px solid rgba(128,120,150,.25)}"+
"table.tcard td{display:block!important;padding:0!important;border:0!important;text-align:left!important;font-size:14px;min-width:0!important;white-space:normal!important;background:none!important}"+
"table.tcard td:first-child{grid-column:1/-1;font-weight:800;font-size:15px}"+
"table.tcard td[data-l]:not(:first-child)::before{content:attr(data-l);display:block;font:500 12px/1.3 system-ui,-apple-system,sans-serif;color:#8a8496;margin-bottom:1px;text-transform:none;letter-spacing:0}"+
"table.tmat th:first-child,table.tmat td:first-child{position:sticky;left:0;z-index:1;background:var(--panel,#fff);box-shadow:4px 0 6px -4px rgba(0,0,0,.25)}"+
".tvuot{font-size:12.5px;opacity:.7;margin:4px 0 2px;text-align:right}";
d.head.appendChild(st);
function cotH(t){var r=t.tHead&&t.tHead.rows[0]||t.rows[0];return r?[].map.call(r.cells,function(c){return c.textContent.replace(/\s+/g," ").trim()}):[]}
function scr(t){var p=t.parentElement;while(p&&p!==d.body){var o=getComputedStyle(p).overflowX;if(o=="auto"||o=="scroll")return p;p=p.parentElement}return null}
function lam(){[].forEach.call(d.querySelectorAll("table:not([data-tb])"),function(t){var r=t.getBoundingClientRect();if(!r.width)return;
 var box=scr(t)||t.parentElement,bw=box.getBoundingClientRect().width||innerWidth;if(t.scrollWidth<=bw+2&&r.right<=innerWidth+2){t.dataset.tb="ok";return}
 var h=cotH(t),n=h.length,mat=h.slice(1).filter(function(x){return /^(Q\d\/\d{4}|\d{4}|T\d{1,2}\/\d{4})$/.test(x)}).length>=Math.max(2,n-2);
 if(mat){t.dataset.tb="mat";t.classList.add("tmat");if(!box.previousElementSibling||!box.previousElementSibling.classList.contains("tvuot")){var v=d.createElement("p");v.className="tvuot";v.textContent="Vuốt ngang để xem thêm →";box.parentElement.insertBefore(v,box)}return}
 if(n&&n<=6){t.classList.add("tfit");if(t.scrollWidth<=bw+2){t.dataset.tb="fit";return}t.classList.remove("tfit")}
 var r0=t.rows[0],hb=!t.tHead&&r0&&!r0.querySelector("th")&&[].every.call(r0.cells,function(c){return c.querySelector("b,strong")&&c.textContent.trim()==c.querySelector("b,strong").textContent.trim()});if(!t.tHead&&!r0.querySelector("th")&&!hb){t.dataset.tb="bo";return}if(hb)r0.classList.add("thd");
 [].forEach.call((t.tHead&&t.tBodies.length)?t.tBodies[0].rows:[].slice.call(t.rows,1),function(row){[].forEach.call(row.cells,function(c,i){if(h[i]&&!c.dataset.l)c.dataset.l=h[i]})});
 t.classList.add("tcard");t.dataset.tb="card"})}
var tm;function hen(){clearTimeout(tm);tm=setTimeout(lam,300)}
if(d.readyState!="loading")hen();else d.addEventListener("DOMContentLoaded",hen);W.addEventListener("load",hen);
try{new MutationObserver(function(ms){for(var i=0;i<ms.length;i++){var a=ms[i].addedNodes;for(var j=0;j<a.length;j++){var x=a[j];if(x.nodeType==1&&(x.tagName=="TABLE"||x.querySelector&&x.querySelector("table"))){hen();return}}}}).observe(d.documentElement,{childList:true,subtree:true})}catch(e){}
d.addEventListener("toggle",hen,true);d.addEventListener("click",function(){setTimeout(hen,400)},true)})();
