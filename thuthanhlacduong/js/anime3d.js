// ===== TƯỚNG 3D THẬT (model VRM của anh Huy) — khung xương điều khiển bằng code, chuyển động liên tục, không dùng thẻ giấy =====
var A3 = (function () {
  var T = THREE, ready = false, TPL = {};
  var BASE = window.VRM_BASE || 'vrm/';
  var HERO = {
    vodang: ['S2_darkD', 'sword', '#4a90d9'], ngamy: ['N7_flow', 'fan', '#f06292'], ngudoc: ['N8_kokuyou', 'claw', '#b06ad0'],
    duongmon: ['M5_aoppoiyo', 'dart', '#2e9d6b'], conlon: ['N78_noise', 'talisman', '#00bcd4'], thienvuong: ['S2_darkD', 'hammer', '#d4a017'],
    thieulam: ['M5_aoppoiyo', 'staff', '#e8952a'], caibang: ['N8_kokuyou', 'stick', '#8d6e63'],
    m_bachy: ['N7_flow', 'fan', '#9fd3ff'], m_honglien: ['S2_darkD', 'twin', '#ff5252'], m_thanhlong: ['M5_aoppoiyo', 'sword', '#1de9b6'], m_kimgiap: ['N78_noise', 'spear', '#ffd740']
  };
  var BONES = ['hips', 'spine', 'chest', 'neck', 'head', 'leftUpperArm', 'leftLowerArm', 'rightUpperArm', 'rightLowerArm', 'leftUpperLeg', 'leftLowerLeg', 'rightUpperLeg', 'rightLowerLeg', 'rightHand', 'leftHand'];

  function load(cb, onProg) {
    var PR = {}, prog = function () { if (!onProg) return; var l = 0, t = 0; for (var k in PR) { l += PR[k][0]; t += PR[k][1]; } onProg(t ? l / t : 0); };
    if (!T.GLTFLoader || !window.VRM_BONES) { cb(); return; }
    var names = []; Object.keys(HERO).forEach(function (k) { if (k.indexOf('m_') === 0 && names.indexOf(HERO[k][0]) < 0) names.push(HERO[k][0]); }); // chỉ tải model linh vật
    var left = names.length, ld = new T.GLTFLoader();
    names.forEach(function (n) {
      ld.load(BASE + n + '.glb', function (g) {
        var o = g.scene; o.traverse(function (m) { if (m.isMesh) { m.frustumCulled = false; m.castShadow = true; } });
        var box = new T.Box3().setFromObject(o); TPL[n] = { scene: o, h: box.max.y - box.min.y, B: VRM_BONES[n] };
        if (--left === 0) { ready = Object.keys(TPL).length > 0; cb(); }
      }, function (e) { PR[n] = [e.loaded, e.total || 1500000]; prog(); }, function () { if (--left === 0) { ready = Object.keys(TPL).length > 0; cb(); } });
    });
  }

  var _q = new T.Quaternion(), _q2 = new T.Quaternion(), _v = new T.Vector3();
  function aimRest(b, child, dirW) {
    if (!b || !child) return;
    var a = b.getWorldPosition(new T.Vector3()), c = child.getWorldPosition(new T.Vector3()), cur = c.sub(a).normalize();
    var R = new T.Quaternion().setFromUnitVectors(cur, dirW.clone().normalize()), pq = new T.Quaternion(); b.parent.getWorldQuaternion(pq);
    b.quaternion.premultiply(pq.clone().invert().multiply(R).multiply(pq)); b.updateMatrixWorld(true);
  }

  function make(key, height, opt) {
    opt = opt || {};
    var h = HERO[key]; if (!h || !TPL[h[0]]) return null;
    var tp = TPL[h[0]], o = T.SkeletonUtils.clone(tp.scene), B = tp.B;
    var root = new T.Group(), pivot = new T.Group(); root.add(pivot); pivot.add(o);
    o.rotation.y = B.ver ? 0 : Math.PI;
    var sc = height / tp.h; pivot.scale.setScalar(sc);
    root.updateMatrixWorld(true);
    var bn = {}; BONES.forEach(function (k) { var b = o.getObjectByName(B.bones[k]); if (b) bn[k] = b; });
    // tư thế nghỉ: buông tay tự nhiên
    aimRest(bn.leftUpperArm, bn.leftLowerArm, new T.Vector3(0.3, -1, 0.1));
    aimRest(bn.rightUpperArm, bn.rightLowerArm, new T.Vector3(-0.3, -1, 0.1));
    // lưu tư thế nghỉ + trục quay theo thân (mặt hướng +Z, trái +X) quy về hệ trục cha của từng xương
    var rig = {};
    Object.keys(bn).forEach(function (k) {
      var b = bn[k], pq = new T.Quaternion(); b.parent.getWorldQuaternion(pq); var inv = pq.clone().invert();
      rig[k] = { b: b, rest: b.quaternion.clone(), x: new T.Vector3(1, 0, 0).applyQuaternion(inv), y: new T.Vector3(0, 1, 0).applyQuaternion(inv), z: new T.Vector3(0, 0, 1).applyQuaternion(inv) };
    });
    var hipsY = bn.hips ? bn.hips.position.y : 0;
    // vũ khí gắn vào bàn tay, hướng theo cẳng tay
    function attach(handK, foreK, type, glowCol) {
      var hand = bn[handK] || bn[foreK], fore = bn[foreK]; if (!hand) return null;
      var wg = new T.Group(); V.weapon3(wg, type, { wglow: glowCol }); wg.scale.setScalar(1.7 / sc);
      var hp = hand.getWorldPosition(new T.Vector3()), fp = fore ? fore.getWorldPosition(new T.Vector3()) : hp.clone().add(new T.Vector3(0, 0.2, 0));
      var dirW = hp.clone().sub(fp).normalize(), qW = new T.Quaternion().setFromUnitVectors(new T.Vector3(0, -1, 0), dirW);
      var hq = new T.Quaternion(); hand.getWorldQuaternion(hq); wg.quaternion.copy(hq.invert().multiply(qW));
      hand.add(wg); return wg;
    }
    var wcol = opt.glow ? h[2] : null;
    var w1 = h[1] ? attach('rightHand', 'rightLowerArm', h[1] === 'twin' ? 'sword' : h[1], wcol) : null;
    var w2 = h[1] === 'twin' ? attach('leftHand', 'leftLowerArm', 'sword', wcol) : null;
    // bóng chân
    var sh = new T.Mesh(new T.CircleGeometry(0.45, 20), new T.MeshBasicMaterial({ color: '#1a0e14', transparent: true, opacity: 0.35, depthWrite: false }));
    sh.rotation.x = -Math.PI / 2; sh.position.y = 0.025; root.add(sh);
    root.userData = { a3: true, key: key, rig: rig, pivot: pivot, model: o, hipsY: hipsY, w: [w1, w2], walkP: Math.random() * 6, atkT: 0, castT: 0, lastCast: 0, dieT: 0, col: h[2], sc: sc,
      body: pivot, head: pivot, armL: pivot, armR: pivot, legL: pivot, legR: pivot };
    return root;
  }

  // áo + vũ khí phát sáng khi nâng cấp: viền sáng bao quanh thân (vỏ phồng theo pháp tuyến)
  function glowify(v, col) {
    var U = v.userData; if (U.glow) return; U.glow = [];
    U.model.traverse(function (m) {
      if (!m.isSkinnedMesh) return;
      var gm = new T.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.5, blending: T.AdditiveBlending, depthWrite: false, side: T.BackSide });
      gm.onBeforeCompile = function (s) { s.vertexShader = s.vertexShader.replace('#include <begin_vertex>', '#include <begin_vertex>\n transformed += normalize(objectNormal) * 0.012;'); };
      var g = new T.SkinnedMesh(m.geometry, gm); g.bind(m.skeleton, m.bindMatrix); g.frustumCulled = false; m.parent.add(g); g.position.copy(m.position); g.quaternion.copy(m.quaternion); g.scale.copy(m.scale);
      U.glow.push(gm);
    });
    U.w.forEach(function (w) { if (!w) return; var s = V.glowSprite(col, 1.2 / U.sc, 0.6); s.position.y = -0.4 / U.sc; w.add(s); });
  }

  function rot(r, ax, ay, az) {
    if (!r) return;
    r.b.quaternion.copy(r.rest);
    if (ax) { _q.setFromAxisAngle(r.x, ax); r.b.quaternion.premultiply(_q); }
    if (ay) { _q.setFromAxisAngle(r.y, ay); r.b.quaternion.premultiply(_q); }
    if (az) { _q.setFromAxisAngle(r.z, az); r.b.quaternion.premultiply(_q); }
  }
  function ease(x) { return x < 0 ? 0 : x > 1 ? 1 : x * x * (3 - 2 * x); }

  // st: { moving, atk, cast, dead, speed }
  function anim(v, st, dt, t) {
    var U = v.userData, R = U.rig;
    if (st.cast && st.cast !== U.lastCast) { U.lastCast = st.cast; U.castT = 0.6; }
    if (st.atk > 0.2 && U.atkT <= 0) U.atkT = 0.36;
    U.castT -= dt; U.atkT -= dt;
    if (st.dead) { U.dieT = Math.min(1, U.dieT + dt * 3); } else U.dieT = Math.max(0, U.dieT - dt * 4);
    var mv = st.moving ? 1 : 0; U.mvB = (U.mvB || 0) + (mv - (U.mvB || 0)) * Math.min(1, dt * 8);
    if (st.moving) U.walkP += dt * 10;
    var p = U.walkP, s1 = Math.sin(p), c1 = Math.cos(p), w = U.mvB, br = Math.sin(t * 2.4 + U.walkP * 0.1);
    // chân
    rot(R.leftUpperLeg, -0.6 * s1 * w, 0, 0); rot(R.rightUpperLeg, 0.6 * s1 * w, 0, 0);
    rot(R.leftLowerLeg, (0.1 + 0.7 * Math.max(0, -c1)) * w, 0, 0); rot(R.rightLowerLeg, (0.1 + 0.7 * Math.max(0, c1)) * w, 0, 0);
    // thân + đầu
    var atkK = U.atkT > 0 ? (U.atkT > 0.22 ? ease((0.36 - U.atkT) / 0.14) : 1 - ease((0.22 - U.atkT) / 0.22) * 0.4) : 0;   // 0..1 giơ lên rồi chém
    var strike = U.atkT > 0 && U.atkT <= 0.22 ? ease((0.22 - U.atkT) / 0.1) : 0;
    var castK = U.castT > 0 ? Math.sin(Math.min(1, (0.6 - U.castT) / 0.6) * Math.PI) : 0;
    rot(R.spine, 0.12 * w + 0.03 * br * (1 - w) + 0.15 * strike - 0.1 * castK, 0.14 * s1 * w - 0.35 * atkK * (1 - strike) + 0.35 * strike, 0);
    rot(R.chest, 0.04 * br, 0, 0);
    rot(R.head, -0.15 * castK, 0, 0.04 * br * (1 - w));
    // tay
    var lA = 0.5 * s1 * w, rA = -0.5 * s1 * w;
    rot(R.leftUpperArm, lA - 1.9 * castK, 0, -0.08 * br * (1 - w) - 0.6 * castK);
    rot(R.leftLowerArm, -0.3 - 0.4 * castK, 0, 0);
    var rRaise = -2.6 * atkK * (1 - strike) - 1.3 * strike;            // giơ kiếm sau đầu rồi chém xuống trước
    rot(R.rightUpperArm, rA + rRaise - 1.9 * castK, 0, 0.08 * br * (1 - w) + 0.6 * castK - 0.3 * strike);
    rot(R.rightLowerArm, -0.35 - 0.5 * atkK * (1 - strike) - 0.4 * castK, 0, 0);
    // nhún người khi chạy
    U.pivot.position.y = (Math.abs(s1) * 0.06 * w) + 0;
    // ngã khi tử trận
    U.pivot.rotation.x = -U.dieT * 1.45; U.pivot.position.y -= U.dieT * 0.1;
    if (U.glow) { var gl = 0.35 + Math.sin(t * 4 + U.walkP) * 0.2 + castK * 0.4; U.glow.forEach(function (m) { m.opacity = gl; }); }
  }

  function portrait(key, size, face) {   // ảnh chân dung: dựng 1 lần
    if (!ready) return null;
    var v = make(key, 2); if (!v) return null;
    anim(v, {}, 0.01, 0);
    var rr = portrait.rr || (portrait.rr = new T.WebGLRenderer({ alpha: true, antialias: true, preserveDrawingBuffer: true }));
    rr.setSize(size, size, false);
    var sc = new T.Scene(); sc.add(new T.HemisphereLight('#fff', '#888', 1)); sc.add(v); v.rotation.y = 0.35;
    var cam = new T.PerspectiveCamera(face ? 16 : 26, 1, 0.1, 50);
    if (face) { cam.position.set(0, 1.75, 3.2); cam.lookAt(0, 1.68, 0); } else { cam.position.set(0, 1.4, 6); cam.lookAt(0, 1.0, 0); }
    rr.setClearColor(0, 0); rr.render(sc, cam); return rr.domElement.toDataURL();
  }

  return { load: load, make: make, anim: anim, glowify: glowify, portrait: portrait, ready: function () { return ready; }, has: function (k) { return !!HERO[k] && ready && !!TPL[HERO[k][0]]; }, HERO: HERO };
})();
