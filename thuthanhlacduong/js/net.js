// ===== MẠNG: ghép trận qua PeerJS (kết nối thẳng giữa 2 máy, độ trễ thấp) =====
// Lockstep: chủ phòng chạy mô phỏng, gửi lệnh từng nhịp (20 nhịp/giây); khách chạy y hệt (mô phỏng tất định).
var NETM = (function () {
  var self;
  var PFX = 'ttld26-';
  function rid(n) { var s = ''; for (var i = 0; i < n; i++) s += 'abcdefghjkmnpqrstuvwxyz23456789'[Math.floor(Math.random() * 31)]; return s; }
  function mk(role, conn, peer, mode) {
    var N = { role: role, conn: conn, peer: peer, mode: mode, q: [], frames: [], lost: false, onmsg: null, onclose: null,
      send: function (m) { try { if (conn && conn.open) conn.send(m); } catch (e) {} },
      close: function () { try { conn && conn.close(); } catch (e) {} try { peer && peer.destroy(); } catch (e) {} } };
    conn.on('data', function (m) { if (m.t === 'f') N.frames.push(m); else if (m.t === 'cmd') { N.q.push(m.c); } else if (N.onmsg) N.onmsg(m); });
    conn.on('close', function () { N.lost = true; if (N.onclose) N.onclose(); });
    conn.on('error', function () {});
    return N;
  }
  // Ghép nhanh: thử giữ một "ghế chờ"; nếu ghế có người chờ thì vào làm khách.
  function quick(mode, onStatus, onReady, onFail) {
    var slot = 1, done = false, timer = null, peers = [];
    function fail(msg) { if (done) return; done = true; peers.forEach(function (p) { try { p.destroy(); } catch (e) {} }); onFail(msg); }
    function trySlot() {
      if (done) return;
      if (slot > 6) { fail('Không tìm thấy kết nối'); return; }
      var id = PFX + mode + '-' + slot;
      var hp = new Peer(id, { debug: 0 }); peers.push(hp);
      hp.on('open', function () {           // giữ được ghế -> làm chủ phòng, chờ người vào
        onStatus('Đang chờ người chơi khác…');
        hp.on('connection', function (c) {
          if (done) { c.on('open', function () { c.send({ t: 'full' }); setTimeout(function () { c.close(); }, 300); }); return; }
          c.on('open', function () { done = true; clearTimeout(timer); onReady(mk('host', c, hp, mode)); });
        });
        timer = setTimeout(function () { fail('timeout'); }, 30000);
      });
      hp.on('error', function (e) {
        if (e.type === 'unavailable-id') {   // ghế đã có người chờ -> vào làm khách
          try { hp.destroy(); } catch (x) {}
          var gp = new Peer(PFX + 'g-' + rid(8), { debug: 0 }); peers.push(gp);
          gp.on('open', function () {
            var c = gp.connect(id, { reliable: true, serialization: 'json' }), ok = false;
            var opened = false; c.on('open', function () { opened = true; onStatus('Đã tìm thấy người chơi, đang vào trận…'); c.send({ t: 'hello', h: NETM.me }); });
            c.on('data', function (m) { if (m.t === 'full') { try { gp.destroy(); } catch (x) {} slot++; trySlot(); } else if (m.t === 'start' && !ok) { ok = true; done = true; var N = mk('guest', c, gp, mode); onReady(N, m); } });
            var chk = function (n) { setTimeout(function () { if (ok || done) return; if (opened && n < 3) { chk(n + 1); return; } try { gp.destroy(); } catch (x) {} slot++; trySlot(); }, 10000); }; chk(0);
          });
          gp.on('error', function () { slot++; trySlot(); });
        } else if (e.type === 'network' || e.type === 'server-error' || e.type === 'socket-error' || e.type === 'browser-incompatible') fail('Mạng lỗi');
      });
    }
    onStatus('Đang tìm trận…'); trySlot();
    return { cancel: function () { fail('cancel'); } };
  }
  // Phòng riêng theo mã (rủ bạn bè)
  function host(code, mode, onStatus, onReady, onFail) {
    var p = new Peer(PFX + 'room-' + code, { debug: 0 }), done = false;
    p.on('open', function () { onStatus('Mã phòng: ' + code + ' — gửi mã cho bạn'); p.on('connection', function (c) { if (done) return; c.on('open', function () { done = true; onReady(mk('host', c, p, mode)); }); }); });
    p.on('error', function (e) { if (!done) { done = true; onFail(e.type === 'unavailable-id' ? 'Mã phòng đã có người dùng' : 'Mạng lỗi'); } });
    return { cancel: function () { done = true; try { p.destroy(); } catch (e) {} } };
  }
  function join(code, onStatus, onReady, onFail) {
    var p = new Peer(PFX + 'g-' + rid(8), { debug: 0 }), done = false;
    p.on('open', function () { onStatus('Đang vào phòng ' + code + '…'); var c = p.connect(PFX + 'room-' + code, { reliable: true, serialization: 'json' }); c.on('open', function () { c.send({ t: 'hello', h: NETM.me }); });
      c.on('data', function (m) { if (m.t === 'start' && !done) { done = true; onReady(mk('guest', c, p, m.mode), m); } });
      setTimeout(function () { if (!done) { done = true; try { p.destroy(); } catch (e) {} onFail('Không thấy phòng ' + code); } }, 20000); });
    p.on('error', function () { if (!done) { done = true; onFail('Không vào được phòng'); } });
    return { cancel: function () { done = true; try { p.destroy(); } catch (e) {} } };
  }
  return { me: null, quick: quick, host: host, join: join, rid: rid, ok: function () { return typeof Peer !== 'undefined'; } };
})();
