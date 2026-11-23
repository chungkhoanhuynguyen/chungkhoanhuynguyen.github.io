// ===== TÀI KHOẢN: ID + mật khẩu (Firebase Auth), lưu rank trên mạng (Firestore ttld_players) =====
var ACCT = (function () {
  var cfg = { apiKey: 'AIzaSyCclpMymMk9lLZcilbntyyjCH3XAP_6My4', authDomain: 'chungkhoanhuynguyen-web.firebaseapp.com', projectId: 'chungkhoanhuynguyen-web', storageBucket: 'chungkhoanhuynguyen-web.firebasestorage.app', messagingSenderId: '495753057756', appId: '1:495753057756:web:7f46fd4224f7b93cb3eb19' };
  var app = null, auth = null, db = null, user = null, prof = null, listeners = [];
  function ok() { return typeof firebase !== 'undefined'; }
  function init() {
    if (!ok() || app) return;
    app = firebase.initializeApp(cfg, 'ttld'); auth = app.auth(); db = app.firestore();
    auth.onAuthStateChanged(function (u) { user = u; if (!u) { prof = null; emit(); return; }
      db.collection('ttld_players').doc(u.uid).get().then(function (s) { prof = s.exists ? s.data() : null; emit(); }).catch(function () { emit(); }); });
  }
  function emit() { listeners.forEach(function (f) { try { f(user, prof); } catch (e) {} }); }
  function mail(id) { return id.toLowerCase().replace(/[^a-z0-9_.]/g, '') + '@ttld.game'; }
  function viErr(e) { var c = (e && e.code) || ''; return { 'auth/email-already-in-use': 'ID này đã có người dùng', 'auth/weak-password': 'Mật khẩu cần ít nhất 6 ký tự', 'auth/invalid-credential': 'Sai ID hoặc mật khẩu', 'auth/wrong-password': 'Sai mật khẩu', 'auth/user-not-found': 'Chưa có tài khoản này', 'auth/too-many-requests': 'Thử lại sau ít phút', 'auth/network-request-failed': 'Mất mạng', 'permission-denied': 'Máy chủ chưa mở quyền lưu dữ liệu game' }[c] || ('Lỗi: ' + (e && e.message || c)); }
  function register(id, pw, mascot) {
    init(); if (!/^[a-zA-Z0-9_.]{3,16}$/.test(id)) return Promise.reject({ message: 'ID 3–16 ký tự, chỉ chữ không dấu, số, _ hoặc .' });
    return auth.createUserWithEmailAndPassword(mail(id), pw).then(function (r) {
      prof = { name: id, pts: 0, win: 0, lose: 0, mascot: mascot || 'honglien', updated: Date.now() };
      return db.collection('ttld_players').doc(r.user.uid).set(prof).then(function () { emit(); return prof; });
    });
  }
  function login(id, pw) { init(); return auth.signInWithEmailAndPassword(mail(id), pw); }
  function logout() { if (auth) auth.signOut(); }
  function saveResult(pts, won) {
    if (!user || !prof) return Promise.resolve();
    var np = Math.max(0, Math.round(pts)); var d = np - prof.pts; if (Math.abs(d) > 80) np = prof.pts + (d > 0 ? 80 : -80);
    var upd = { name: prof.name, pts: np, win: (prof.win || 0) + (won === 1 ? 1 : 0), lose: (prof.lose || 0) + (won === 0 ? 1 : 0), mascot: prof.mascot || 'honglien', updated: Date.now() };
    return db.collection('ttld_players').doc(user.uid).set(upd).then(function () { prof = upd; });
  }
  function top(n) { init(); return db.collection('ttld_players').orderBy('pts', 'desc').limit(n || 20).get().then(function (q) { return q.docs.map(function (d) { return d.data(); }); }); }
  return { init: init, ok: ok, register: register, login: login, logout: logout, saveResult: saveResult, top: top, viErr: viErr, on: function (f) { listeners.push(f); }, get user() { return user; }, get prof() { return prof; } };
})();
