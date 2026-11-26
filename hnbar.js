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
function go(){d.body.appendChild(b);d.body.classList.add("hnbar")}
if(d.body)go();else d.addEventListener("DOMContentLoaded",go);
b.addEventListener("click",function(ev){var a=ev.target.closest&&ev.target.closest("a.s");if(a)try{if(W.hnDo)hnDo("bar_soi",{ma:m||""})}catch(x){}});
function go2(ev){var t=ev.target,g=t&&/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)&&!/^(button|submit|checkbox|radio)$/i.test(t.type||"");if(g)b.classList.add("an")}
d.addEventListener("focusin",go2);d.addEventListener("focusout",function(){setTimeout(function(){var a=d.activeElement;if(!a||!/^(INPUT|TEXTAREA|SELECT)$/.test(a.tagName))b.classList.remove("an")},120)});})();
