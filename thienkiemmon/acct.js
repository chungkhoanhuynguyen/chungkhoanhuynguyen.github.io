// ===== Huyền Kiếm Tiên Đồ — tài khoản ID + mật khẩu, tối đa 5 nhân vật, chơi chung bản đồ =====
// Dùng thẳng REST API của Firebase (không tải SDK 500KB) — project riêng cho game `thuthanhlacduong`.
// Bảng: tkm_players/{uid} {j: JSON hồ sơ}, tkm_online/{uid} {j, t}, tkm_chat/{auto} {n, m, t}
var TKACCT = (function () {
  var KEY = 'AIzaSyDuPm6aG0nltOIrTbtKMKMWgzGtQk5k7n8', PID = 'thuthanhlacduong';
  var FS = 'https://firestore.googleapis.com/v1/projects/' + PID + '/databases/(default)/documents';
  var KEYS = ['tkm_inv', 'tkm_pk', 'tkm_tl', 'tkm_bc', 'tkm_look2', 'tkm_bank'], MAXC = 5;
  var user = null, prof = null, slot = -1, denied = false, tok = null, tokExp = 0;
  var ls = function (k, v) { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { } };
  var ss = function (k, v) { try { if (v === undefined) return sessionStorage.getItem(k); if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) { } };
  function mail(id) { return id.toLowerCase().replace(/[^a-z0-9_.]/g, '') + '@tkm.game'; }
  function err(code, msg) { var e = new Error(msg || code); e.code = code; return e; }
  function post(url, body, form) {
    var ctl = new AbortController(); var tm = setTimeout(function () { ctl.abort(); }, 15000);
    return fetch(url, { method: 'POST', signal: ctl.signal, headers: { 'Content-Type': form ? 'application/x-www-form-urlencoded' : 'application/json' }, body: form ? body : JSON.stringify(body) })
      .then(function (r) { clearTimeout(tm); return r.json().then(function (j) { if (!r.ok) throw err((j.error && j.error.message) || ('HTTP' + r.status)); return j; }); },
        function (e) { clearTimeout(tm); throw err('NETWORK', e && e.name === 'AbortError' ? 'Máy chủ phản hồi quá lâu' : 'Mất mạng'); });
  }
  function setTok(j) { user = { uid: j.localId || j.user_id, email: j.email }; tok = j.idToken || j.id_token; tokExp = Date.now() + (+(j.expiresIn || j.expires_in || 3600) - 60) * 1000; ls('tkm_auth', JSON.stringify({ r: j.refreshToken || j.refresh_token, u: user.uid, e: user.email })); }
  function token() {
    if (tok && Date.now() < tokExp) return Promise.resolve(tok);
    var a; try { a = JSON.parse(ls('tkm_auth') || 'null'); } catch (e) { }
    if (!a || !a.r) return Promise.reject(err('NO_SESSION'));
    return post('https://securetoken.googleapis.com/v1/token?key=' + KEY, 'grant_type=refresh_token&refresh_token=' + encodeURIComponent(a.r), true).then(function (j) { j.email = a.e; setTok(j); return tok; });
  }
  function fsReq(method, path, body) {
    return token().then(function (t) {
      return fetch(FS + path, { method: method, headers: { 'Authorization': 'Bearer ' + t, 'Content-Type': 'application/json' }, body: body ? JSON.stringify(body) : undefined })
        .then(function (r) { if (r.status === 404 && method === 'GET') return null; return r.json().then(function (j) { if (!r.ok) { var c = (j.error && j.error.status) || 'HTTP' + r.status; if (c === 'PERMISSION_DENIED') { denied = true; c = 'permission-denied'; } throw err(c); } return j; }); });
    });
  }
  function viErr(e) {
    var c = (e && e.code) || '';
    var M = { EMAIL_EXISTS: 'ID này đã có người dùng — chọn ID khác hoặc bấm Đăng nhập', INVALID_LOGIN_CREDENTIALS: 'Sai ID hoặc mật khẩu', INVALID_PASSWORD: 'Sai mật khẩu', EMAIL_NOT_FOUND: 'Chưa có tài khoản này — bấm Tạo tài khoản', TOO_MANY_ATTEMPTS_TRY_LATER: 'Thử lại sau ít phút', OPERATION_NOT_ALLOWED: 'Máy chủ chưa bật đăng nhập bằng mật khẩu (chủ game cần bật Email/Password trong Firebase)', NETWORK: (e && e.message) || 'Mất mạng', 'permission-denied': 'Máy chủ chưa mở quyền lưu nhân vật (chủ game cần thêm quy tắc Firestore)' };
    if (M[c]) return M[c]; if (/WEAK_PASSWORD/.test(c)) return 'Mật khẩu cần ít nhất 6 ký tự';
    return 'Không kết nối được (' + (c || 'lỗi lạ') + ')';
  }
  function readProf() {
    return fsReq('GET', '/tkm_players/' + user.uid).then(function (d) {
      var p = null; try { p = d && d.fields && JSON.parse(d.fields.j.stringValue); } catch (e) { }
      prof = p || { id: (user.email || '').split('@')[0], chars: [] }; if (!prof.chars) prof.chars = []; return prof;
    }).catch(function (e) { prof = { id: (user.email || '').split('@')[0], chars: [] }; if (e.code === 'permission-denied') denied = true; return prof; });
  }
  function writeProf() { return fsReq('PATCH', '/tkm_players/' + user.uid, { fields: { j: { stringValue: JSON.stringify(prof) }, t: { integerValue: String(Date.now()) } } }).catch(function () { }); }
  function snapshot() { var o = {}; KEYS.forEach(function (k) { var v = ls(k); if (v != null) o[k] = v; }); return JSON.stringify(o); }
  function restore(save) { KEYS.forEach(function (k) { ls(k, null); }); if (!save) return; try { var o = JSON.parse(save); Object.keys(o).forEach(function (k) { if (KEYS.indexOf(k) >= 0) ls(k, o[k]); }); } catch (e) { } }
  var lastSave = 0;
  function save(force) {
    if (!user || !prof || slot < 0 || denied) return Promise.resolve();
    var now = Date.now(); if (!force && now - lastSave < 20000) return Promise.resolve(); lastSave = now;
    var g = window.TKGAME || {}; prof.chars[slot] = { name: g.name ? g.name() : 'Đại hiệp', lv: g.lv ? g.lv() : '', save: snapshot(), updated: now }; prof.updated = now;
    return writeProf();
  }
  // ---------- trực tuyến: vị trí + chat thế giới (thăm dò định kỳ) ----------
  function setOnline(o) { o.t = Date.now(); return fsReq('PATCH', '/tkm_online/' + user.uid, { fields: { j: { stringValue: JSON.stringify(o) }, t: { integerValue: String(o.t) } } }); }
  function delOnline() { if (!user || !tok) return; try { fetch(FS + '/tkm_online/' + user.uid, { method: 'DELETE', keepalive: true, headers: { 'Authorization': 'Bearer ' + tok } }); } catch (e) { } }
  function query(col, since, lim) {
    return token().then(function (t) {
      return fetch(FS + ':runQuery', { method: 'POST', headers: { 'Authorization': 'Bearer ' + t, 'Content-Type': 'application/json' }, body: JSON.stringify({ structuredQuery: { from: [{ collectionId: col }], where: { fieldFilter: { field: { fieldPath: 't' }, op: 'GREATER_THAN', value: { integerValue: String(since) } } }, limit: lim || 60 } }) })
        .then(function (r) { return r.json().then(function (j) { if (!r.ok) { var c = (j[0] && j[0].error && j[0].error.status) || (j.error && j.error.status) || 'HTTP' + r.status; if (c === 'PERMISSION_DENIED') c = 'permission-denied'; throw err(c); } return (Array.isArray(j) ? j : []).filter(function (x) { return x.document; }).map(function (x) { var f = x.document.fields || {}, id = x.document.name.split('/').pop(), o = {}; Object.keys(f).forEach(function (k) { var v = f[k]; o[k] = v.stringValue != null ? v.stringValue : v.integerValue != null ? +v.integerValue : v.doubleValue; }); o._id = id; return o; }); }); });
    });
  }
  function queryOnline() { return query('tkm_online', Date.now() - 90000, 80).then(function (a) { return a.map(function (o) { var d = {}; try { d = JSON.parse(o.j); } catch (e) { } d.t = o.t; d._id = o._id; return d; }); }); }
  function sendChat(n, m) { return fsReq('POST', '/tkm_chat', { fields: { n: { stringValue: n }, m: { stringValue: m }, t: { integerValue: String(Date.now()) } } }); }
  function pollChat(since) { return query('tkm_chat', since, 30); }
  // ---------- giao diện: gọn, vừa màn ngang điện thoại ----------
  var box = null;
  function css() {
    var st = document.createElement('style'); st.textContent =
      '#acctov{position:fixed;inset:0;z-index:40;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;overflow:auto;background:#e8b8c0 url(login_bg.jpg?v=3) center/cover no-repeat;font-family:"Noto Serif",serif;color:#f3e6c8;animation:azin 1s ease}' +
      '#acctov::after{content:"";position:fixed;inset:0;background:url(login_bg.jpg?v=3) center/cover;z-index:-1;animation:azoom 40s ease-in-out infinite alternate}@keyframes azoom{to{transform:scale(1.08)}}@keyframes azin{from{opacity:0}}' +
      '#acctov::before{content:"";position:fixed;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(0,0,0,.25),transparent 18%,transparent 70%,rgba(0,10,20,.45)),url("data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%27100%25%27 height=%27100%25%27%3E%3C/svg%3E")}' +
      '#acctov .logo{position:relative;margin-top:max(3vh,10px);text-align:center;padding:14px 46px 10px;pointer-events:none}' +
      '#acctov .logo:before{content:"";position:absolute;inset:-10px -30px;z-index:-1;background:radial-gradient(ellipse at 50% 45%,rgba(120,40,170,.85),rgba(70,20,120,.55) 40%,rgba(40,10,80,0) 70%);filter:blur(4px)}' +
      '#acctov .logo b{display:block;font:900 clamp(30px,5.4vw,62px) "Noto Serif",serif;letter-spacing:3px;line-height:1.02;background:linear-gradient(#fffbe6,#ffd36b 42%,#c07a1c 75%,#ffe9a8);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 10px rgba(255,170,40,.8)) drop-shadow(0 3px 2px rgba(40,10,0,.9))}' +
      '#acctov .logo i{display:inline-block;margin-top:6px;font:800 clamp(11px,1.6vw,16px) "Noto Serif",serif;font-style:normal;color:#fff;letter-spacing:4px;padding:3px 26px;background:linear-gradient(90deg,transparent,rgba(110,30,160,.9) 18%,rgba(110,30,160,.9) 82%,transparent);text-shadow:0 0 8px #d08aff}' +
      '#acctov .ab{position:relative;margin:min(4vh,26px) auto 70px;width:min(460px,92vw);padding:16px 40px 14px;background:linear-gradient(90deg,transparent,rgba(12,16,22,.84) 9%,rgba(12,16,22,.84) 91%,transparent);border-top:2px solid rgba(20,20,20,.0);-webkit-mask:none}' +
      '#acctov .ab:before,#acctov .ab:after{content:"";position:absolute;left:4%;right:4%;height:10px;background:radial-gradient(ellipse at center,rgba(12,16,22,.9),transparent 70%)}#acctov .ab:before{top:-6px}#acctov .ab:after{bottom:-6px}' +
      '#acctov h2{margin:0 0 2px;color:#ffd36b;font-size:17px;letter-spacing:1px;text-align:center}#acctov .sub{text-align:center;font-size:11.5px;opacity:.8;margin:0 0 8px}' +
      '#acctov .fr{display:flex;align-items:center;gap:12px}#acctov .fr .col{flex:1}' +
      '#acctov input{width:100%;box-sizing:border-box;height:34px;margin:0 0 7px;border-radius:17px;border:1px solid rgba(232,194,106,.55);background:rgba(0,0,0,.6);color:#fff;font:600 14px system-ui,sans-serif;padding:0 14px}#acctov input:focus{outline:none;border-color:#ffd36b;box-shadow:0 0 0 2px rgba(255,211,107,.25)}' +
      '#acctov button{width:100%;height:36px;margin:3px 0;border-radius:18px;border:1px solid #b8893a;background:linear-gradient(180deg,#f7d270,#b8862a);color:#2a1606;font:800 14px "Noto Serif",serif;cursor:pointer}#acctov button.alt{background:rgba(0,0,0,.45);color:#f0dcae}#acctov button:disabled{opacity:.5}' +
      '#acctov button.go{width:78px;height:78px;flex:none;border-radius:50%;border:3px solid #6a4a1a;background:radial-gradient(circle at 40% 35%,#fff2b0,#f2b93a 45%,#9a5a10);box-shadow:0 0 0 3px #e8c06a,0 0 18px rgba(255,190,60,.8),inset 0 -4px 8px rgba(80,30,0,.5);font:900 15px/1.05 "Noto Serif",serif;color:#3a1a00;padding:0}#acctov button.go:hover{filter:brightness(1.1)}' +
      '#acctov .links{display:flex;gap:8px;margin-top:4px}#acctov .links button{height:30px;font-size:12.5px}' +
      '#acctov .row2{display:flex;gap:6px}#acctov .msg{min-height:16px;font-size:12px;color:#ff9a7a;text-align:center;margin:2px 0 4px}#acctov small{opacity:.75}' +
      '#acctov .ch{display:flex;align-items:center;gap:8px;border:1px solid rgba(184,137,58,.55);border-radius:10px;padding:7px 12px;margin:5px 0;background:rgba(0,0,0,.4);cursor:pointer}#acctov .ch:hover{border-color:#ffd36b}#acctov .ch b{color:#ffd36b}#acctov .ch .x{margin-left:auto;width:auto;height:26px;padding:0 10px;font-size:11px}' +
      '#acctov .srvs{display:grid;grid-template-columns:1fr 1fr;gap:5px;margin:0 0 9px}#acctov .sv{display:flex;align-items:center;gap:6px;padding:5px 9px;border-radius:8px;border:1px solid rgba(184,137,58,.45);background:rgba(0,0,0,.4);font:700 12.5px "Noto Serif",serif;color:#f0dcae;cursor:pointer}#acctov .sv.on{border-color:#ffd36b;background:rgba(120,80,10,.45);box-shadow:0 0 8px rgba(255,211,107,.4)}#acctov .sv em{margin-left:auto;font:800 10.5px system-ui,sans-serif;font-style:normal;padding:1px 6px;border-radius:8px;color:#fff}#acctov .sv em.r{background:#c0262a}#acctov .sv em.o{background:#d07a10}#acctov .sv i{width:8px;height:8px;border-radius:50%;background:#ff4a3a;box-shadow:0 0 6px #ff4a3a}#acctov .sv i.o{background:#ffb02a;box-shadow:0 0 6px #ffb02a}' +
      '#acctov .lb2{position:fixed;left:8vw;right:8vw;bottom:10px;text-align:center;font:600 12px "Noto Serif",serif;color:#fff;text-shadow:0 1px 3px #000}#acctov .lb2 div{height:6px;border-radius:4px;background:rgba(0,0,0,.35);border:1px solid rgba(255,211,107,.5);overflow:hidden;margin-bottom:3px}#acctov .lb2 div i{display:block;height:100%;width:0;background:linear-gradient(90deg,#c99a3e,#ffe9a8);transition:width .4s}' +
      '#acctov .ver{position:fixed;right:10px;top:8px;font-size:11px;color:#fff;text-shadow:0 1px 2px #000;opacity:.85}' +
      '@media (max-height:520px){#acctov .logo{margin-top:2px;padding:4px 30px 2px}#acctov .logo b{font-size:24px}#acctov .logo i{font-size:10px;margin-top:2px}#acctov .ab{margin:4px auto 34px;padding:8px 28px}#acctov h2{font-size:13px}#acctov .srvs{grid-template-columns:repeat(4,1fr);gap:4px;margin-bottom:6px}#acctov .sv{padding:3px 6px;font-size:11px;flex-wrap:wrap}#acctov .sv em{margin-left:0;font-size:9px}#acctov input{height:30px;margin-bottom:5px}#acctov button.go{width:64px;height:64px;font-size:13px}#acctov .links button{height:26px}#acctov .msg{min-height:0}#acctov .lb2{bottom:3px}#acctov .lb2 span{font-size:10px}}';
    document.head.appendChild(st);
  }
  var LMUS = null;
  function lmusStart() { try { if (!LMUS) { LMUS = new Audio('audio/login.mp3'); LMUS.loop = true; LMUS.volume = 0.55; } if (LMUS.paused && !LMUS._stop) LMUS.play().catch(function () { }); } catch (e) { } }
  window.tkLoginMusStop = function () { if (!LMUS) { LMUS = { _stop: 1 }; return; } LMUS._stop = 1; var a = LMUS; if (!a.pause) return; var t = setInterval(function () { a.volume = Math.max(0, a.volume - 0.05); if (a.volume <= 0.01) { clearInterval(t); a.pause(); } }, 120); };
  (function () { var f = function () { if (document.getElementById('acctov') || (document.getElementById('load') && document.getElementById('load').style.display !== 'none') || document.querySelector('#cgo')) lmusStart(); document.removeEventListener('pointerdown', f, true); document.removeEventListener('keydown', f, true); }; document.addEventListener('pointerdown', f, true); document.addEventListener('keydown', f, true); setTimeout(lmusStart, 300); })();
  var SRV = [['Thanh Long', 'Đông nghịt', 'r'], ['Bạch Hổ', 'Rất đông', 'r'], ['Chu Tước', 'Rất đông', 'r'], ['Huyền Vũ', 'Đông', 'o']];
  function srvName() { var v = +(ls('tkm_srv') || 0); return SRV[v] ? SRV[v][0] : SRV[0][0]; }
  window.tkSrvName = srvName;
  function srvHtml() { var v = +(ls('tkm_srv') || 0); return '<div class="srvs">' + SRV.map(function (s, i) { return '<div class="sv' + (i === v ? ' on' : '') + '" data-sv="' + i + '"><i class="' + (s[2] === 'o' ? 'o' : '') + '"></i>' + s[0] + '<em class="' + s[2] + '">' + s[1] + '</em></div>'; }).join('') + '</div>'; }
  function srvWire(b) { b.querySelectorAll('.sv').forEach(function (x) { x.onclick = function () { ls('tkm_srv', x.dataset.sv); b.querySelectorAll('.sv').forEach(function (y) { y.classList.toggle('on', y === x); }); var v = document.querySelector('#acctov .ver'); if (v) v.textContent = 'Máy chủ ' + srvName() + ' · bản 1.0'; }; }); }
  function show(html) { if (!box) { css(); box = document.createElement('div'); box.id = 'acctov'; document.body.appendChild(box); } box.innerHTML = '<div class="logo"><b>HUYỀN KIẾM<br>TIÊN ĐỒ</b><i>✦ TU TIÊN GIỚI ✦</i></div><div class="ab">' + html + '</div><div class="lb2"><div><i id="albi"></i></div><span id="albt">Đang tải thế giới…</span></div><div class="ver">Máy chủ ' + srvName() + ' · bản 1.0</div>'; srvWire(box); lbTick(); box.style.display = 'flex'; return box; }
  var lbT = 0;
  function lbTick() { if (lbT) return; lbT = setInterval(function () { var t = document.getElementById('albt'), i = document.getElementById('albi'); if (!t || !box || box.style.display === 'none') { clearInterval(lbT); lbT = 0; return; } var txt = (typeof window.loadTxt === 'function') ? window.loadTxt() : ''; var pc = parseInt(txt) || 0; var ready = !!document.querySelector('#cgo:not([disabled])') || !document.getElementById('load'); if (ready) pc = 100; i.style.width = Math.max(3, pc) + '%'; t.textContent = pc >= 100 ? '✓ Thế giới đã tải xong — đăng nhập là vào ngay' : 'Đang tải thế giới ' + txt + ' — đăng nhập trong lúc chờ'; }, 400); }
  function hide() { if (box) box.style.display = 'none'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function loginView(msg) {
    var b = show('<h2>Chọn máy chủ</h2>' + srvHtml() +
      '<div class="fr"><div class="col"><input id="aid" placeholder="Tài khoản (3–16 ký tự không dấu)" autocomplete="username" maxlength="16" autocapitalize="none" spellcheck="false">' +
      '<input id="apw" type="password" placeholder="Mật khẩu (ít nhất 6 ký tự)" autocomplete="current-password"></div><button id="alog" class="go">Vào<br>game</button></div>' +
      '<div class="msg" id="amsg">' + (msg || '') + '</div><div class="links"><button id="areg" class="alt">Tạo tài khoản</button><button id="aoff" class="alt">Chơi thử ngay</button></div>');
    var id = b.querySelector('#aid'), pw = b.querySelector('#apw'), m = b.querySelector('#amsg');
    id.value = ls('tkm_lastid') || '';
    function go(reg) {
      var v = id.value.trim().toLowerCase(); if (!/^[a-z0-9_.]{3,16}$/.test(v)) { m.textContent = 'ID 3–16 ký tự: chữ không dấu, số, _ hoặc .'; return; }
      if (pw.value.length < 6) { m.textContent = 'Mật khẩu cần ít nhất 6 ký tự'; return; }
      m.style.color = '#ffe9b0'; m.textContent = 'Đang kết nối máy chủ…'; b.querySelectorAll('button').forEach(function (x) { x.disabled = true; });
      post('https://identitytoolkit.googleapis.com/v1/accounts:' + (reg ? 'signUp' : 'signInWithPassword') + '?key=' + KEY, { email: mail(v), password: pw.value, returnSecureToken: true })
        .then(function (j) { setTok(j); ls('tkm_lastid', v); return readProf(); }).then(function () { if (!prof.id) prof.id = v; charView(); })
        .catch(function (e) { m.style.color = '#ff9a7a'; m.textContent = viErr(e); b.querySelectorAll('button').forEach(function (x) { x.disabled = false; }); });
    }
    b.querySelector('#alog').onclick = function () { go(false); }; b.querySelector('#areg').onclick = function () { go(true); };
    pw.onkeydown = function (e) { e.stopPropagation(); if (e.key === 'Enter') go(false); }; id.onkeydown = function (e) { e.stopPropagation(); };
    b.querySelector('#aoff').onclick = function () { ss('tkm_slot', 'off'); hide(); };
  }
  function charView() {
    var cs = prof.chars || [], n = cs.filter(Boolean).length, h = '<h2>Chọn máy chủ</h2>' + srvHtml() + '<h2>Chọn nhân vật</h2><div class="sub">' + esc(prof.id || '') + ' · ' + n + '/' + MAXC + ' nhân vật</div>';
    cs.forEach(function (c, i) { if (c) h += '<div class="ch" data-i="' + i + '"><div><b>' + esc(c.name || 'Nhân vật ' + (i + 1)) + '</b><br><small>' + esc(c.lv || '') + '</small></div><button class="x alt" data-del="' + i + '">Xóa</button></div>'; });
    if (n < MAXC) h += '<button id="anew">+ Tạo nhân vật mới</button>';
    h += (denied ? '<div class="msg">Máy chủ chưa mở quyền lưu — nhân vật chỉ lưu trên máy này.</div>' : '') + '<button id="aout" class="alt">Đăng xuất</button>';
    var b = show(h);
    b.querySelectorAll('.ch').forEach(function (el) { el.onclick = function (ev) { if (ev.target.dataset.del) return; pick(+el.dataset.i); }; });
    b.querySelectorAll('[data-del]').forEach(function (el) { el.onclick = function () { var i = +el.dataset.del; if (!confirm('Xóa vĩnh viễn nhân vật "' + (cs[i].name || '') + '"?')) return; cs[i] = null; while (cs.length && !cs[cs.length - 1]) cs.pop(); writeProf(); charView(); }; });
    var nb = b.querySelector('#anew'); if (nb) nb.onclick = function () { var i = cs.findIndex(function (c) { return !c; }); if (i < 0) i = cs.length; ss('tkm_slot', user.uid + ':' + i); ss('tkm_new', '1'); restore(null); location.reload(); };
    b.querySelector('#aout').onclick = function () { ls('tkm_auth', null); user = null; prof = null; tok = null; ss('tkm_slot', null); loginView(); };
  }
  function pick(i) { ss('tkm_slot', user.uid + ':' + i); ss('tkm_new', null); ss('tkm_auto', '1'); restore(prof.chars[i].save); location.reload(); }
  function resume() { var a; try { a = JSON.parse(ls('tkm_auth') || 'null'); } catch (e) { } if (!a) return Promise.reject(err('NO_SESSION')); user = { uid: a.u, email: a.e }; return token(); }
  function boot() {
    if (/noacct/.test(location.search)) return;
    var s = ss('tkm_slot');
    if (s === 'off') { hide(); return; }
    if (s && s.indexOf(':') > 0) {
      show('<h2>Huyền Kiếm Tiên Đồ</h2><div class="sub">Đang vào thế giới…</div>');
      var uid = s.split(':')[0], i = +s.split(':')[1];
      resume().then(function () { if (user.uid !== uid) throw err('NO_SESSION'); return readProf(); }).then(function () {
        slot = i; hide(); if (window.TKGAME && window.TKGAME.ready) window.TKGAME.ready(ss('tkm_new') === '1', ss('tkm_auto') === '1'); ss('tkm_auto', null);
      }).catch(function () { ss('tkm_slot', null); loginView('Phiên đăng nhập đã hết, hãy đăng nhập lại.'); });
      return;
    }
    if (!ls('tkm_auth')) { loginView(); return; }
    show('<h2>Huyền Kiếm Tiên Đồ</h2><div class="sub">Đang kết nối…</div>');
    resume().then(readProf).then(charView).catch(function () { loginView(); });
  }
  setInterval(function () { save(false); }, 30000);
  addEventListener('pagehide', function () { save(true); delOnline(); });
  document.addEventListener('visibilitychange', function () { if (document.hidden) save(true); });
  return { boot: boot, save: save, viErr: viErr, setOnline: setOnline, delOnline: delOnline, queryOnline: queryOnline, sendChat: sendChat, pollChat: pollChat,
    get user() { return user; }, get slot() { return slot; }, get online() { return !!(user && slot >= 0 && !denied); }, get denied() { return denied; }, set denied(v) { denied = v; },
    switchChar: function () { save(true).then(function () { ss('tkm_slot', null); location.reload(); }); } };
})();
