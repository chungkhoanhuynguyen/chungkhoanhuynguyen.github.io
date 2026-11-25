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
      '#acctov{position:fixed;inset:0;z-index:40;display:flex;align-items:center;justify-content:center;background:#07050a url(load_bg.jpg) center/cover no-repeat;font-family:"Noto Serif",serif;color:#f3e6c8}' +
      '#acctov::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,3,8,.2),rgba(5,3,8,.85) 58%)}' +
      '#acctov .ab{position:relative;margin-left:auto;margin-right:5vw;width:min(340px,44vw);max-height:94vh;overflow:auto;background:rgba(20,13,6,.8);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);border:1px solid rgba(217,164,65,.7);border-radius:14px;padding:14px 16px;box-shadow:0 10px 40px rgba(0,0,0,.6)}' +
      '#acctov h2{margin:0;color:#ffd36b;font-size:19px;letter-spacing:.5px;text-align:center}#acctov .sub{text-align:center;font-size:11.5px;opacity:.75;margin:2px 0 10px}' +
      '#acctov input{width:100%;box-sizing:border-box;height:38px;margin:0 0 8px;border-radius:8px;border:1px solid rgba(232,194,106,.5);background:rgba(0,0,0,.5);color:#fff;font:600 15px system-ui,sans-serif;padding:0 12px}#acctov input:focus{outline:none;border-color:#ffd36b;box-shadow:0 0 0 2px rgba(255,211,107,.25)}' +
      '#acctov button{width:100%;height:38px;margin:3px 0;border-radius:8px;border:1px solid #b8893a;background:linear-gradient(180deg,#f2c75c,#b8862a);color:#2a1606;font:800 14px "Noto Serif",serif;cursor:pointer}#acctov button.alt{background:rgba(0,0,0,.35);color:#f0dcae}#acctov button:disabled{opacity:.5}' +
      '#acctov .row2{display:flex;gap:6px}#acctov .msg{min-height:16px;font-size:12px;color:#ff9a7a;text-align:center;margin:2px 0 4px}#acctov small{opacity:.7}' +
      '#acctov .ch{display:flex;align-items:center;gap:8px;border:1px solid rgba(184,137,58,.5);border-radius:8px;padding:7px 10px;margin:5px 0;background:rgba(0,0,0,.35);cursor:pointer}#acctov .ch b{color:#ffd36b}#acctov .ch .x{margin-left:auto;width:auto;height:26px;padding:0 8px;font-size:11px}' +
      '#acctov{animation:azin 1s ease}#acctov::after{content:"";position:absolute;inset:0;background:url(load_bg.jpg) center/cover;z-index:-1;animation:azoom 30s ease-in-out infinite alternate}@keyframes azoom{to{transform:scale(1.1)}}@keyframes azin{from{opacity:0}}'+'#acctov .logo{position:absolute;left:5vw;top:50%;transform:translateY(-55%);max-width:46vw;text-align:center;pointer-events:none}#acctov .logo b{display:block;font:900 clamp(30px,6vw,64px) "Noto Serif",serif;letter-spacing:3px;background:linear-gradient(#fff6d0,#ffd36b 45%,#b8701c);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 0 14px rgba(255,140,30,.8)) drop-shadow(0 3px 2px #000)}#acctov .logo i{display:block;font:700 clamp(12px,1.8vw,18px) "Noto Serif",serif;font-style:normal;color:#f3e6c8;letter-spacing:4px;text-shadow:0 2px 4px #000;margin-top:4px}'+'#acctov .srv{display:flex;align-items:center;gap:6px;justify-content:center;font-size:12px;margin:-4px 0 8px;color:#bfe8c0}#acctov .srv:before{content:"";width:8px;height:8px;border-radius:50%;background:#5dff8a;box-shadow:0 0 6px #5dff8a}'+'#acctov .lb2{position:absolute;left:5vw;right:5vw;bottom:14px;text-align:center;font:600 12px "Noto Serif",serif;color:#f3e6c8;text-shadow:0 1px 3px #000}#acctov .lb2 div{height:7px;border-radius:4px;background:rgba(255,255,255,.15);border:1px solid rgba(255,211,107,.45);overflow:hidden;margin-bottom:4px}#acctov .lb2 div i{display:block;height:100%;width:0;background:linear-gradient(90deg,#c99a3e,#ffe9a8);transition:width .4s}'+'#acctov .ver{position:absolute;right:10px;top:8px;font-size:11px;opacity:.6}'+'@media (max-width:620px){#acctov .ab{margin:0 auto;width:88vw}#acctov::before{background:rgba(5,3,8,.6)}#acctov .logo{display:none}}';
    document.head.appendChild(st);
  }
  function show(html) { if (!box) { css(); box = document.createElement('div'); box.id = 'acctov'; document.body.appendChild(box); } box.innerHTML = '<div class="ab">' + html + '</div><div class="lb2"><div><i id="albi"></i></div><span id="albt">Đang tải thế giới…</span></div><div class="ver">Máy chủ Thế Giới 1 · bản 1.0</div>';lbTick(); box.style.display = 'flex'; return box; }
  var lbT = 0;
  function lbTick() { if (lbT) return; lbT = setInterval(function () { var t = document.getElementById('albt'), i = document.getElementById('albi'); if (!t || !box || box.style.display === 'none') { clearInterval(lbT); lbT = 0; return; } var txt = (typeof window.loadTxt === 'function') ? window.loadTxt() : ''; var pc = parseInt(txt) || 0; var ready = !!document.querySelector('#cgo:not([disabled])') || !document.getElementById('load'); if (ready) pc = 100; i.style.width = Math.max(3, pc) + '%'; t.textContent = pc >= 100 ? '✓ Thế giới đã tải xong — đăng nhập là vào ngay' : 'Đang tải thế giới ' + txt + ' — đăng nhập trong lúc chờ'; }, 400); }
  function hide() { if (box) box.style.display = 'none'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function loginView(msg) {
    var b = show('<h2>Đăng nhập</h2><div class="srv">Thế Giới 1 · Đang mở</div><div class="sub">Lưu nhân vật, chơi cùng mọi người</div>' +
      '<input id="aid" placeholder="ID (3–16 ký tự không dấu)" autocomplete="username" maxlength="16" autocapitalize="none" spellcheck="false">' +
      '<input id="apw" type="password" placeholder="Mật khẩu (ít nhất 6 ký tự)" autocomplete="current-password">' +
      '<div class="msg" id="amsg">' + (msg || '') + '</div><div class="row2"><button id="alog">Đăng nhập</button><button id="areg" class="alt">Tạo tài khoản</button></div>' +
      '<button id="aoff" class="alt">Chơi thử ngay, không cần tài khoản</button>');
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
    var cs = prof.chars || [], n = cs.filter(Boolean).length, h = '<h2>Chọn nhân vật</h2><div class="sub">' + esc(prof.id || '') + ' · ' + n + '/' + MAXC + ' nhân vật</div>';
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
