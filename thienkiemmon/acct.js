// ===== Huyền Kiếm Tiên Đồ — tài khoản ID + mật khẩu, tối đa 5 nhân vật, lưu trên mạng =====
// Firebase project riêng cho game (thuthanhlacduong), KHÔNG dùng Firebase của web chứng khoán.
// Bảng: tkm_players/{uid} = {id, chars:[{name,lv,save,updated}], updated}
//       tkm_online/{uid}  = vị trí người chơi đang online (cùng 1 bản đồ)
var TKACCT = (function () {
  var cfg = { apiKey: 'AIzaSyDuPm6aG0nltOIrTbtKMKMWgzGtQk5k7n8', authDomain: 'thuthanhlacduong.firebaseapp.com', projectId: 'thuthanhlacduong', storageBucket: 'thuthanhlacduong.firebasestorage.app', messagingSenderId: '827806903370', appId: '1:827806903370:web:b7d01cf63f504d000e8ab3' };
  var KEYS = ['tkm_inv', 'tkm_pk', 'tkm_tl', 'tkm_bc', 'tkm_look2'], MAXC = 5;
  var app = null, auth = null, db = null, user = null, prof = null, slot = -1, fbLoading = null, denied = false;
  var ss = function (k, v) { try { if (v === undefined) return sessionStorage.getItem(k); if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) { } };
  function loadFB() {
    if (fbLoading) return fbLoading;
    var base = '/thienkiemmon/lib/fb/';
    var one = function (f) { return new Promise(function (ok, no) { var s = document.createElement('script'); s.src = base + f + '?v=1'; s.onload = ok; s.onerror = no; document.head.appendChild(s); }); };
    fbLoading = one('fb-app.js').then(function () { return Promise.all([one('fb-auth.js'), one('fb-firestore.js')]); }).then(function () {
      app = firebase.initializeApp(cfg, 'tkm'); auth = app.auth(); db = app.firestore();
    });
    return fbLoading;
  }
  function mail(id) { return id.toLowerCase().replace(/[^a-z0-9_.]/g, '') + '@tkm.game'; }
  function viErr(e) { var c = (e && e.code) || ''; return { 'auth/email-already-in-use': 'ID này đã có người dùng', 'auth/weak-password': 'Mật khẩu cần ít nhất 6 ký tự', 'auth/invalid-credential': 'Sai ID hoặc mật khẩu', 'auth/invalid-login-credentials': 'Sai ID hoặc mật khẩu', 'auth/wrong-password': 'Sai mật khẩu', 'auth/user-not-found': 'Chưa có tài khoản này', 'auth/too-many-requests': 'Thử lại sau ít phút', 'auth/network-request-failed': 'Mất mạng — kiểm tra kết nối', 'permission-denied': 'Máy chủ chưa mở quyền lưu nhân vật (chủ game cần thêm quy tắc Firestore)' }[c] || ('Lỗi: ' + ((e && e.message) || c)); }
  function readProf() { return db.collection('tkm_players').doc(user.uid).get().then(function (s) { prof = s.exists ? s.data() : { id: (user.email || '').split('@')[0], chars: [] }; if (!prof.chars) prof.chars = []; return prof; }).catch(function (e) { if (e && e.code === 'permission-denied') denied = true; prof = { id: (user.email || '').split('@')[0], chars: [] }; return prof; }); }
  function snapshot() { var o = {}; KEYS.forEach(function (k) { try { var v = localStorage.getItem(k); if (v != null) o[k] = v; } catch (e) { } }); return JSON.stringify(o); }
  function restore(save) { KEYS.forEach(function (k) { try { localStorage.removeItem(k); } catch (e) { } }); if (!save) return; try { var o = JSON.parse(save); Object.keys(o).forEach(function (k) { if (KEYS.indexOf(k) >= 0) localStorage.setItem(k, o[k]); }); } catch (e) { } }
  var lastSave = 0;
  function save(force) {
    if (!user || !prof || slot < 0 || denied) return Promise.resolve();
    var now = Date.now(); if (!force && now - lastSave < 20000) return Promise.resolve(); lastSave = now;
    var g = window.TKGAME || {}; var c = { name: g.name ? g.name() : 'Đại hiệp', lv: g.lv ? g.lv() : '', save: snapshot(), updated: now };
    prof.chars[slot] = c; prof.updated = now;
    return db.collection('tkm_players').doc(user.uid).set({ id: prof.id, chars: prof.chars, updated: now }).catch(function (e) { if (e && e.code === 'permission-denied') denied = true; });
  }
  // ---------- giao diện ----------
  var box = null;
  function css() {
    var st = document.createElement('style'); st.textContent =
      '#acctov{position:fixed;inset:0;z-index:40;display:flex;align-items:center;justify-content:center;background:radial-gradient(ellipse at center,rgba(20,14,8,.72),rgba(5,4,3,.92));font-family:"Noto Serif",serif;color:#f3e6c8}' +
      '#acctov .ab{width:min(380px,92vw);max-height:92vh;overflow:auto;background:linear-gradient(180deg,#2a1d10,#150e07);border:1px solid #b8893a;border-radius:12px;padding:16px 18px;box-shadow:0 0 40px rgba(0,0,0,.7),inset 0 0 0 1px rgba(255,220,150,.08)}' +
      '#acctov h2{margin:0 0 4px;text-align:center;color:#ffd36b;letter-spacing:1px;font-size:20px}#acctov .sub{text-align:center;font-size:12px;opacity:.75;margin-bottom:12px}' +
      '#acctov input{width:100%;box-sizing:border-box;min-height:42px;margin:4px 0 8px;border-radius:8px;border:1px solid rgba(232,194,106,.55);background:rgba(0,0,0,.45);color:#fff;font:600 15px sans-serif;padding:0 12px}' +
      '#acctov button{width:100%;min-height:42px;margin:4px 0;border-radius:8px;border:1px solid #b8893a;background:linear-gradient(180deg,#5a3d16,#2e1f0b);color:#ffe9b0;font:700 14px "Noto Serif",serif;cursor:pointer}#acctov button.alt{background:rgba(0,0,0,.35);color:#e8d6ae}#acctov button:disabled{opacity:.45}' +
      '#acctov .row2{display:flex;gap:8px}#acctov .msg{min-height:18px;font-size:12.5px;color:#ff9a7a;text-align:center}#acctov small{opacity:.7}' +
      '#acctov .ch{display:flex;align-items:center;gap:8px;border:1px solid rgba(184,137,58,.5);border-radius:8px;padding:8px 10px;margin:6px 0;background:rgba(0,0,0,.3);cursor:pointer}#acctov .ch:hover{border-color:#ffd36b}#acctov .ch b{color:#ffd36b}#acctov .ch .x{margin-left:auto;width:auto;min-height:28px;padding:0 8px;font-size:12px}';
    document.head.appendChild(st);
  }
  function show(html) { if (!box) { css(); box = document.createElement('div'); box.id = 'acctov'; document.body.appendChild(box); } box.innerHTML = '<div class="ab">' + html + '</div>'; box.style.display = 'flex'; return box; }
  function hide() { if (box) box.style.display = 'none'; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function loginView(msg) {
    var b = show('<h2>Huyền Kiếm Tiên Đồ</h2><div class="sub">Đăng nhập để lưu nhân vật và gặp người chơi khác trên cùng bản đồ</div>' +
      '<label><small>ID (3–16 ký tự không dấu)</small></label><input id="aid" autocomplete="username" maxlength="16">' +
      '<label><small>Mật khẩu (ít nhất 6 ký tự)</small></label><input id="apw" type="password" autocomplete="current-password">' +
      '<div class="msg" id="amsg">' + (msg || '') + '</div><div class="row2"><button id="alog">Đăng nhập</button><button id="areg" class="alt">Tạo tài khoản</button></div>' +
      '<button id="aoff" class="alt">Chơi thử không lưu (ngoại tuyến)</button>');
    var id = b.querySelector('#aid'), pw = b.querySelector('#apw'), m = b.querySelector('#amsg');
    try { id.value = localStorage.getItem('tkm_lastid') || ''; } catch (e) { }
    function go(reg) {
      var v = id.value.trim(); if (!/^[a-zA-Z0-9_.]{3,16}$/.test(v)) { m.textContent = 'ID 3–16 ký tự: chữ không dấu, số, _ hoặc .'; return; }
      if (pw.value.length < 6) { m.textContent = 'Mật khẩu cần ít nhất 6 ký tự'; return; }
      m.style.color = '#ffe9b0'; m.textContent = 'Đang kết nối máy chủ…'; b.querySelectorAll('button').forEach(function (x) { x.disabled = true; });
      loadFB().then(function () { return reg ? auth.createUserWithEmailAndPassword(mail(v), pw.value) : auth.signInWithEmailAndPassword(mail(v), pw.value); })
        .then(function (r) { user = r.user; try { localStorage.setItem('tkm_lastid', v); } catch (e) { } return readProf(); }).then(function () { if (!prof.id) prof.id = v; charView(); })
        .catch(function (e) { m.style.color = '#ff9a7a'; m.textContent = viErr(e); b.querySelectorAll('button').forEach(function (x) { x.disabled = false; }); });
    }
    b.querySelector('#alog').onclick = function () { go(false); }; b.querySelector('#areg').onclick = function () { go(true); };
    pw.onkeydown = function (e) { if (e.key === 'Enter') go(false); };
    b.querySelector('#aoff').onclick = function () { ss('tkm_slot', 'off'); hide(); };
  }
  function charView() {
    var cs = prof.chars || [], h = '<h2>Chọn nhân vật</h2><div class="sub">Tài khoản <b>' + esc(prof.id || '') + '</b> · ' + cs.filter(Boolean).length + '/' + MAXC + ' nhân vật</div>';
    cs.forEach(function (c, i) { if (c) h += '<div class="ch" data-i="' + i + '"><div><b>' + esc(c.name || 'Nhân vật ' + (i + 1)) + '</b><br><small>' + esc(c.lv || '') + '</small></div><button class="x alt" data-del="' + i + '">Xóa</button></div>'; });
    if (cs.filter(Boolean).length < MAXC) h += '<button id="anew">+ Tạo nhân vật mới</button>';
    h += (denied ? '<div class="msg">Máy chủ chưa mở quyền lưu — nhân vật chỉ lưu trên máy này.</div>' : '') + '<button id="aout" class="alt">Đăng xuất</button>';
    var b = show(h);
    b.querySelectorAll('.ch').forEach(function (el) { el.onclick = function (ev) { if (ev.target.dataset.del) return; pick(+el.dataset.i); }; });
    b.querySelectorAll('[data-del]').forEach(function (el) { el.onclick = function () { var i = +el.dataset.del; if (!confirm('Xóa vĩnh viễn nhân vật "' + (cs[i].name || '') + '"? Không thể khôi phục.')) return; cs[i] = null; while (cs.length && !cs[cs.length - 1]) cs.pop(); db.collection('tkm_players').doc(user.uid).set({ id: prof.id, chars: cs, updated: Date.now() }).catch(function () { }); charView(); }; });
    var nb = b.querySelector('#anew'); if (nb) nb.onclick = function () { var i = cs.findIndex(function (c) { return !c; }); if (i < 0) i = cs.length; ss('tkm_slot', user.uid + ':' + i); ss('tkm_new', '1'); restore(null); location.reload(); };
    b.querySelector('#aout').onclick = function () { auth.signOut(); user = null; prof = null; ss('tkm_slot', null); loginView(); };
  }
  function pick(i) { ss('tkm_slot', user.uid + ':' + i); ss('tkm_new', null); ss('tkm_auto', '1'); restore(prof.chars[i].save); location.reload(); }
  // Khi trang vừa nạp: nếu phiên này đã chọn nhân vật thì vào thẳng, không hỏi lại
  function boot() {
    if (/noacct/.test(location.search)) return;
    var s = ss('tkm_slot');
    if (s === 'off') { hide(); return; }
    if (s && s.indexOf(':') > 0) {
      show('<h2>Huyền Kiếm Tiên Đồ</h2><div class="sub">Đang kết nối tài khoản…</div>');
      var uid = s.split(':')[0], i = +s.split(':')[1];
      loadFB().then(function () { return new Promise(function (ok) { var un = auth.onAuthStateChanged(function (u) { un(); ok(u); }); }); }).then(function (u) {
        if (!u || u.uid !== uid) { ss('tkm_slot', null); loginView('Phiên đăng nhập đã hết, hãy đăng nhập lại.'); return; }
        user = u; return readProf().then(function () { slot = i; hide(); if (window.TKGAME && window.TKGAME.ready) window.TKGAME.ready(ss('tkm_new') === '1', ss('tkm_auto') === '1'); ss('tkm_auto', null); });
      }).catch(function () { ss('tkm_slot', 'off'); show('<h2>Mất kết nối</h2><div class="sub">Không tới được máy chủ — chơi ngoại tuyến.</div><button onclick="document.getElementById(\'acctov\').style.display=\'none\'">Vào game</button>'); });
      return;
    }
    var had = false; try { had = !!localStorage.getItem('tkm_lastid'); } catch (e) { }
    if (!had) { loginView(); return; }
    show('<h2>Huyền Kiếm Tiên Đồ</h2><div class="sub">Đang kết nối…</div>');
    loadFB().then(function () { return new Promise(function (ok) { var un = auth.onAuthStateChanged(function (u) { un(); ok(u); }); }); })
      .then(function (u) { if (!u) { loginView(); return; } user = u; return readProf().then(charView); }).catch(function () { loginView('Không tới được máy chủ — có thể chơi thử ngoại tuyến.'); });
  }
  setInterval(function () { save(false); }, 30000);
  addEventListener('pagehide', function () { save(true); });
  document.addEventListener('visibilitychange', function () { if (document.hidden) save(true); });
  return { boot: boot, save: save, viErr: viErr, get db() { return db; }, get user() { return user; }, get slot() { return slot; }, get online() { return !!(user && db && !denied); }, get denied() { return denied; }, set denied(v) { denied = v; }, switchChar: function () { save(true).then(function () { ss('tkm_slot', null); location.reload(); }); } };
})();
