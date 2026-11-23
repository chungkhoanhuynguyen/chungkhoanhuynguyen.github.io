// ===== TƯỚNG ANIME: dựng model VRM của anh Huy, chụp sẵn từng tư thế thành THẺ để điện thoại chạy mượt =====
var CARDS = (function () {
  var T = THREE, ready = false, F = {};
  var BASE = window.VRM_BASE || 'vrm/';
  var HERO = {
    vodang: ['S2_darkD', 'sword', '#4a90d9'], ngamy: ['N7_flow', 'fan', '#f06292'], ngudoc: ['N8_kokuyou', 'claw', '#9c4dcc'],
    duongmon: ['M5_aoppoiyo', 'dart', '#2e9d6b'], conlon: ['N78_noise', 'talisman', '#00bcd4'], thienvuong: ['S2_darkD', 'hammer', '#d4a017'],
    thieulam: ['M5_aoppoiyo', 'staff', '#e8952a'], caibang: ['N8_kokuyou', 'stick', '#8d6e63'],
    m_bachy: ['N7_flow', 'fan', '#9fd3ff'], m_honglien: ['S2_darkD', 'twin', '#ff5252'], m_thanhlong: ['M5_aoppoiyo', 'sword', '#1de9b6'], m_kimgiap: ['N78_noise', 'spear', '#ffd740']
  };
  var FRAMES = ['idle0', 'idle1', 'walk0', 'walk1', 'atk', 'cast'];
  var CW = 256, CH = 400, VH = 2.05;   // khung chụp: cao 2,05 m
  var models = {};

  function rotW(b, axisW, ang) { var pq = new T.Quaternion(); b.parent.getWorldQuaternion(pq); var R = new T.Quaternion().setFromAxisAngle(axisW, ang); b.quaternion.premultiply(pq.clone().invert().multiply(R).multiply(pq)); b.updateMatrixWorld(true); }
  function aim(b, child, dirW) { if (!b || !child) return; var a = b.getWorldPosition(new T.Vector3()), c = child.getWorldPosition(new T.Vector3()); var cur = c.sub(a).normalize(); var R = new T.Quaternion().setFromUnitVectors(cur, dirW.clone().normalize()); var pq = new T.Quaternion(); b.parent.getWorldQuaternion(pq); b.quaternion.premultiply(pq.clone().invert().multiply(R).multiply(pq)); b.updateMatrixWorld(true); }

  function load(cb) {
    var names = []; Object.keys(HERO).forEach(function (k) { if (names.indexOf(HERO[k][0]) < 0) names.push(HERO[k][0]); });
    var left = names.length, ld = new T.GLTFLoader();
    names.forEach(function (n) { ld.load(BASE + n + '.glb', function (g) { models[n] = g.scene; if (--left === 0) cb(); }, undefined, function () { if (--left === 0) cb(); }); });
  }

  function bake(cb) {
    if (!T.GLTFLoader || !window.VRM_BONES) { cb(); return; }
    load(function () {
      var rr = new T.WebGLRenderer({ alpha: true, antialias: true, preserveDrawingBuffer: true }); rr.setSize(CW, CH, false); rr.setPixelRatio(1);
      var sc = new T.Scene(); sc.add(new T.HemisphereLight('#ffffff', '#806070', 1.0));
      var cam = new T.PerspectiveCamera(20, CW / CH, 0.1, 50); cam.position.set(0, 2.1, 6.6); cam.lookAt(0, VH * 0.47, 0);
      Object.keys(HERO).forEach(function (key) {
        var h = HERO[key], src = models[h[0]]; if (!src) return;
        F[key] = {};
        FRAMES.forEach(function (fr) {
          var o = T.SkeletonUtils.clone(src), B = VRM_BONES[h[0]];
          var root = new T.Group(); root.add(o); sc.add(root);
          o.rotation.y = (B.ver ? 0 : Math.PI);
          root.rotation.y = 0.45;                       // nghiêng 3/4 sang phải màn hình
          o.traverse(function (m) { if (m.isMesh) m.frustumCulled = false; });
          root.updateMatrixWorld(true);
          var rq = new T.Quaternion(); root.getWorldQuaternion(rq);
          var ax = function (x, y, z) { return new T.Vector3(x, y, z).applyQuaternion(rq); };  // trục theo thân (mặt hướng +Z, trái +X)
          var b = function (k) { return o.getObjectByName(B.bones[k]); };
          // tay buông tự nhiên
          aim(b('leftUpperArm'), b('leftLowerArm'), ax(0.28, -1, 0.12));
          aim(b('rightUpperArm'), b('rightLowerArm'), ax(-0.28, -1, 0.12));
          var X = ax(1, 0, 0), Y = ax(0, 1, 0), Z = ax(0, 0, 1);
          var sp = b('spine'), ch = b('chest') || sp, hd = b('head');
          var lUL = b('leftUpperLeg'), rUL = b('rightUpperLeg'), lLL = b('leftLowerLeg'), rLL = b('rightLowerLeg');
          var lUA = b('leftUpperArm'), rUA = b('rightUpperArm'), lLA = b('leftLowerArm'), rLA = b('rightLowerArm');
          if (lLA) rotW(lLA, X, -0.25); if (rLA) rotW(rLA, X, -0.35);
          if (fr === 'idle1') { if (sp) rotW(sp, X, 0.05); if (hd) rotW(hd, Z, 0.06); }
          if (fr === 'walk0' || fr === 'walk1') { var s = fr === 'walk0' ? 1 : -1; if (lUL) rotW(lUL, X, -0.5 * s); if (rUL) rotW(rUL, X, 0.5 * s); if (lLL) rotW(lLL, X, s > 0 ? 0.2 : 0.6); if (rLL) rotW(rLL, X, s > 0 ? 0.6 : 0.2); if (lUA) rotW(lUA, X, 0.45 * s); if (rUA) rotW(rUA, X, -0.45 * s); if (sp) rotW(sp, X, 0.12); }
          if (fr === 'atk') { if (rUA) aim(rUA, rLA, ax(-0.25, 0.85, 0.75)); if (rLA) rotW(rLA, X, -0.2); if (ch) rotW(ch, Y, 0.35); if (lUA) aim(lUA, lLA, ax(0.6, -0.5, 0.4)); if (lUL) rotW(lUL, X, -0.35); if (rUL) rotW(rUL, X, 0.25); }
          if (fr === 'cast') { if (rUA) aim(rUA, rLA, ax(-0.55, 0.9, 0.35)); if (lUA) aim(lUA, lLA, ax(0.55, 0.9, 0.35)); if (hd) rotW(hd, X, -0.18); if (sp) rotW(sp, X, -0.08); }
          // vũ khí theo cẳng tay
          var hand = b('rightHand') || rLA, fore = rLA;
          if (hand && h[1]) {
            var wg = new T.Group(); V.weapon3(wg, h[1] === 'twin' ? 'sword' : h[1], { wglow: (fr === 'atk' || fr === 'cast') ? h[2] : null });
            wg.scale.setScalar(1.75);
            var hp = hand.getWorldPosition(new T.Vector3()), fp = fore ? fore.getWorldPosition(new T.Vector3()) : hp.clone().add(new T.Vector3(0, 0.2, 0));
            var dir = hp.clone().sub(fp).normalize();
            wg.quaternion.setFromUnitVectors(new T.Vector3(0, -1, 0), dir); wg.position.copy(hp); sc.add(wg);
            if (h[1] === 'twin') { var lh = b('leftHand') || lLA; if (lh) { var w2 = new T.Group(); V.weapon3(w2, 'sword', {}); w2.scale.setScalar(1.75); var l0 = lh.getWorldPosition(new T.Vector3()), l1 = (lLA ? lLA.getWorldPosition(new T.Vector3()) : l0); w2.quaternion.setFromUnitVectors(new T.Vector3(0, -1, 0), l0.clone().sub(l1).normalize()); w2.position.copy(l0); sc.add(w2); root.userData.w2 = w2; } }
            root.userData.wg = wg;
          }
          rr.setClearColor(0x000000, 0); rr.render(sc, cam);
          var c = document.createElement('canvas'); c.width = CW; c.height = CH; c.getContext('2d').drawImage(rr.domElement, 0, 0);
          var t = new T.CanvasTexture(c); t.encoding = T.LinearEncoding; t.anisotropy = 4;
          F[key][fr] = { t: t, c: c };
          sc.remove(root); if (root.userData.wg) sc.remove(root.userData.wg); if (root.userData.w2) sc.remove(root.userData.w2);
        });
      });
      rr.dispose(); Object.keys(models).forEach(function (k) { models[k] = null; });
      ready = Object.keys(F).length > 0; cb();
    });
  }

  // ---------- thẻ trong trận ----------
  var planeG = null;
  function make(key, scale) {
    if (!F[key]) return null;
    if (!planeG) { planeG = new T.PlaneGeometry(VH * CW / CH, VH); planeG.translate(0, VH / 2 - 0.06, 0); }
    var root = new T.Group(), holder = new T.Group(); root.add(holder); holder.scale.setScalar(scale || 1);
    var mat = new T.MeshBasicMaterial({ map: F[key].idle0.t, transparent: true, alphaTest: 0.35, side: T.DoubleSide, color: '#fff1e4' });
    var card = new T.Mesh(planeG, mat); holder.add(card);
    var sh = new T.Mesh(new T.CircleGeometry(0.42, 20), new T.MeshBasicMaterial({ color: '#1a0e14', transparent: true, opacity: 0.4, depthWrite: false }));
    sh.rotation.x = -Math.PI / 2; sh.scale.set(1, 0.55, 1); sh.position.y = 0.03; root.add(sh);
    root.userData = { card: true, key: key, holder: holder, mesh: card, fr: 'idle0', ph: Math.random() * 3, face: 1, atkT: 0, castT: 0, lastCast: 0, body: holder, head: holder, armL: holder, armR: holder, legL: holder, legR: holder };
    return root;
  }
  function glowify(v, col) {   // tướng nâng cấp: áo + vũ khí phát sáng
    var U = v.userData; if (U.glow) return;
    var gm = new T.MeshBasicMaterial({ map: U.mesh.material.map, color: col, transparent: true, opacity: 0.55, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide, alphaTest: 0.2 });
    var g = new T.Mesh(planeG, gm); g.scale.set(1.08, 1.04, 1); g.position.z = -0.02; U.holder.add(g); U.glow = g;
  }
  function anim(v, st, dt, t, camera) {
    var U = v.userData, fr;
    if (st.cast && st.cast !== U.lastCast) { U.lastCast = st.cast; U.castT = 0.45; }
    if (st.atk > 0.2 && U.atkT <= 0) U.atkT = 0.28;
    U.castT -= dt; U.atkT -= dt;
    if (U.castT > 0) fr = 'cast'; else if (U.atkT > 0) fr = 'atk';
    else if (st.moving) fr = Math.floor(t * 6 + U.ph) % 2 ? 'walk0' : 'walk1';
    else fr = Math.floor(t * 1.6 + U.ph) % 2 ? 'idle0' : 'idle1';
    if (fr !== U.fr) { U.fr = fr; var tx = F[U.key][fr].t; U.mesh.material.map = tx; if (U.glow) U.glow.material.map = tx; }
    // luôn quay mặt thẻ về camera, lật trái/phải theo hướng đánh
    var wp = v.getWorldPosition(new T.Vector3());
    U.holder.rotation.y = Math.atan2(camera.position.x - wp.x, camera.position.z - wp.z) - v.rotation.y;
    if (st.face) U.face = st.face;
    U.holder.scale.x = Math.abs(U.holder.scale.x) * U.face;
    U.mesh.rotation.z = st.dead ? 0 : (U.fr === 'atk' ? -0.05 * U.face : 0);
    if (st.dead) { U.mesh.material.opacity = 0.35; } else U.mesh.material.opacity = 1;
    if (U.glow) U.glow.material.opacity = 0.4 + Math.sin(t * 4 + U.ph) * 0.2;
  }
  function bbox(c) { var d = c.getContext('2d').getImageData(0, 0, CW, CH).data, x0 = CW, x1 = 0, y0 = CH, y1 = 0; for (var y = 0; y < CH; y += 2) for (var x = 0; x < CW; x += 2) if (d[(y * CW + x) * 4 + 3] > 40) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; } return { x0: x0, x1: x1, y0: y0, y1: y1 }; }
  function portrait(key, face) {
    if (!F[key]) return null; var c = F[key].idle0.c, o = document.createElement('canvas'), s = face ? 128 : 200; o.width = s; o.height = s;
    var b = bbox(c), hgt = b.y1 - b.y0, g = o.getContext('2d');
    if (face) { var w = hgt * 0.3, cx = (b.x0 + b.x1) / 2; g.drawImage(c, cx - w / 2, b.y0 - w * 0.05, w, w, 0, 0, s, s); }
    else { var w2 = hgt * 1.0, cx2 = (b.x0 + b.x1) / 2; g.drawImage(c, cx2 - w2 / 2, b.y0 - hgt * 0.02, w2, w2, 0, 0, s, s); }
    return o.toDataURL();
  }
  return { bake: bake, make: make, anim: anim, glowify: glowify, portrait: portrait, has: function (k) { return !!F[k]; }, ready: function () { return ready; }, HERO: HERO };
})();
