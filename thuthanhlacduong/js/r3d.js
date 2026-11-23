// ===== ĐỒ HOẠ 3D (three.js) — thành Lạc Dương lúc hoàng hôn =====
var V = (function () {
  var S = Sim, T = THREE, shade = R.shade;
  var LOW = (window.matchMedia && matchMedia('(pointer:coarse)').matches) || Math.min(screen.width, screen.height) < 820;   // điện thoại: giảm tải
  var LW = Sim.LANE_W, HL = LW / 2, LCX = [0, LW + 10], MX = LCX[1] / 2;
  function W(lane, x, y, h) { return new T.Vector3(LCX[lane] + x - HL, h || 0, 9 - y); }

  var renderer, scene, camera, composer, bloom, sun, overlay, octx, Wd = 1, Hd = 1, DPR = 1;
  var clock = 0;

  // ---------- vật liệu ----------
  var gradTex;
  function makeGrad() {
    var d = new Uint8Array([90, 90, 90, 255, 170, 170, 170, 255, 255, 255, 255, 255]);
    gradTex = new T.DataTexture(d, 3, 1, T.RGBAFormat); gradTex.minFilter = gradTex.magFilter = T.NearestFilter; gradTex.generateMipmaps = false; gradTex.needsUpdate = true;
  }
  var mats = {};
  function M(col, o) {
    o = o || {}; var key = col + JSON.stringify(o);
    if (mats[key]) return mats[key];
    var m;
    if (o.basic) m = new T.MeshBasicMaterial({ color: col, transparent: !!o.op, opacity: o.op || 1, side: o.side || T.FrontSide, blending: o.add ? T.AdditiveBlending : T.NormalBlending, depthWrite: !o.add && !o.op });
    else m = new T.MeshToonMaterial({ color: col, gradientMap: gradTex, emissive: o.em || 0x000000, emissiveIntensity: o.ei || 1, side: o.side || T.FrontSide, map: o.map || null, transparent: !!o.op, opacity: o.op || 1 });
    mats[key] = m; return m;
  }
  var OUT = null;
  var geos = {};
  var GDEF = {
    capeR: function () { var g = new T.PlaneGeometry(0.56, 1.25, 4, 8); g.translate(0, -0.62, 0); return g; },
    helm: function () { return new T.SphereGeometry(0.26, 16, 10, 0, Math.PI * 2, 0, Math.PI * 0.5); },
    lcap: function () { return new T.CylinderGeometry(0.1, 0.1, 0.05, 8); },
    pad: function () { var g = new T.CircleGeometry(0.55, 14, 0.35, Math.PI * 2 - 0.35); g.rotateX(-Math.PI / 2); return g; },
    rock: function () { return new T.DodecahedronGeometry(0.35, 0); },
    stud: function () { return new T.SphereGeometry(0.06, 6, 4); },
    plane1: function () { return new T.PlaneGeometry(1, 1); }
  };
  function G(key, fn) { return geos[key] || (geos[key] = (fn || GDEF[key])()); }
  function mesh(geo, mat, x, y, z, shadow) { var m = new T.Mesh(geo, mat); m.position.set(x || 0, y || 0, z || 0); if (shadow !== false) { m.castShadow = true; } return m; }
  function outline(m, s) { if (LOW) return m; var o = new T.Mesh(m.geometry, OUT); o.scale.setScalar(s || 1.08); o.castShadow = false; m.add(o); return m; }

  // ---------- texture canvas ----------
  function canvasTex(w, h, draw, rep) { var c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); var t = new T.CanvasTexture(c); if (rep) { t.wrapS = t.wrapT = T.RepeatWrapping; t.repeat.set(rep[0], rep[1]); } t.anisotropy = 4; return t; }
  var glowTex, ringTex, lotusTex, runeTex, smokeTex;
  function makeTextures() {
    glowTex = canvasTex(64, 64, function (g) { var r = g.createRadialGradient(32, 32, 0, 32, 32, 32); r.addColorStop(0, 'rgba(255,255,255,1)'); r.addColorStop(0.2, 'rgba(255,255,255,0.8)'); r.addColorStop(0.5, 'rgba(255,255,255,0.25)'); r.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = r; g.fillRect(0, 0, 64, 64); });
    smokeTex = canvasTex(64, 64, function (g) { for (var i = 0; i < 14; i++) { var x = 16 + Math.random() * 32, y = 16 + Math.random() * 32, r = g.createRadialGradient(x, y, 0, x, y, 14); r.addColorStop(0, 'rgba(255,255,255,0.35)'); r.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = r; g.fillRect(0, 0, 64, 64); } });
    ringTex = canvasTex(256, 256, function (g) { g.strokeStyle = '#fff'; g.lineWidth = 10; g.beginPath(); g.arc(128, 128, 110, 0, 6.283); g.stroke(); g.lineWidth = 3; g.beginPath(); g.arc(128, 128, 90, 0, 6.283); g.stroke(); for (var i = 0; i < 24; i++) { var a = i / 24 * 6.283; g.beginPath(); g.moveTo(128 + Math.cos(a) * 92, 128 + Math.sin(a) * 92); g.lineTo(128 + Math.cos(a) * 106, 128 + Math.sin(a) * 106); g.stroke(); } });
    lotusTex = canvasTex(256, 256, function (g) { g.translate(128, 128); for (var k = 0; k < 2; k++) for (var i = 0; i < 8; i++) { g.save(); g.rotate(i / 8 * 6.283 + k * 0.39); var gr = g.createLinearGradient(0, 0, 0, -110 + k * 25); gr.addColorStop(0, 'rgba(255,255,255,0.9)'); gr.addColorStop(1, 'rgba(255,255,255,0.1)'); g.fillStyle = gr; g.beginPath(); g.moveTo(0, 0); g.quadraticCurveTo(36 - k * 8, -60, 0, -112 + k * 25); g.quadraticCurveTo(-36 + k * 8, -60, 0, 0); g.fill(); g.restore(); } });
    runeTex = canvasTex(256, 256, function (g) { g.translate(128, 128); g.strokeStyle = '#fff'; g.lineWidth = 4; [118, 96, 60].forEach(function (r) { g.beginPath(); g.arc(0, 0, r, 0, 6.283); g.stroke(); });
      for (var i = 0; i < 6; i++) { var a = i / 6 * 6.283, b = a + 2.094; g.beginPath(); g.moveTo(Math.cos(a) * 96, Math.sin(a) * 96); g.lineTo(Math.cos(b) * 96, Math.sin(b) * 96); g.stroke(); }
      g.font = 'bold 18px serif'; g.fillStyle = '#fff'; for (var j = 0; j < 12; j++) { g.save(); g.rotate(j / 12 * 6.283); g.fillText(['乾', '坤', '震', '巽', '坎', '離', '艮', '兌'][j % 8], -8, -100); g.restore(); } });
  }
  function spriteMat(col, op, tex) { var k = 'spr' + col + op + (tex ? tex.uuid : ''); if (mats[k]) return mats[k]; return mats[k] = new T.SpriteMaterial({ map: tex || glowTex, color: col, transparent: true, opacity: op === undefined ? 1 : op, blending: T.AdditiveBlending, depthWrite: false }); }
  function glowSprite(col, s, op) { var sp = new T.Sprite(spriteMat(col, op)); sp.scale.set(s, s, 1); return sp; }

  // ---------- MÁI NGÓI CONG ----------
  function roofGeo(w, d, h, lift, o) {
    var Wt = w + o * 2, Dt = d + o * 2, seg = 22;
    var g = new T.PlaneGeometry(Wt, Dt, seg, seg); g.rotateX(-Math.PI / 2);
    var p = g.attributes.position, uv = g.attributes.uv;
    var ridge = Math.max(0, (Wt - Dt) / 2);
    for (var i = 0; i < p.count; i++) {
      var x = p.getX(i), z = p.getZ(i), ax = Math.abs(x), az = Math.abs(z);
      var ex = ridge > 0 ? Math.max(0, ax - ridge) / (Dt / 2) : ax / (Wt / 2), ez = az / (Dt / 2);
      var e = Math.min(1, Math.max(ex, ez));
      var nx = ax / (Wt / 2), nz = az / (Dt / 2);
      var y = h * Math.pow(1 - e, 1.5) + lift * Math.pow(nx * nz, 6) * 1.0 + lift * 0.25 * Math.pow(e, 8);
      p.setY(i, y);
      uv.setXY(i, x * 1.2, (ex > ez ? ax : az) * 1.5 + (ex > ez ? 0.5 : 0));
    }
    g.computeVertexNormals(); return g;
  }
  var roofTex;
  function makeRoofTex() {
    roofTex = canvasTex(64, 64, function (g) { g.fillStyle = '#fff'; g.fillRect(0, 0, 64, 64); for (var i = 0; i < 4; i++) { var gr = g.createLinearGradient(i * 16, 0, i * 16 + 16, 0); gr.addColorStop(0, '#8a8a8a'); gr.addColorStop(0.5, '#ffffff'); gr.addColorStop(1, '#8a8a8a'); g.fillStyle = gr; g.fillRect(i * 16, 0, 16, 64); } g.fillStyle = 'rgba(0,0,0,0.25)'; for (var j = 0; j < 4; j++) g.fillRect(0, j * 16 + 14, 64, 2); }, [1, 1]);
    roofTex.wrapS = roofTex.wrapT = T.RepeatWrapping;
  }
  // nhà cổ: tâm (x,z), rộng w (x), sâu d (z)
  function hall(x, z, w, d, wallH, roofH, opt) {
    opt = opt || {};
    var grp = new T.Group(); grp.position.set(x, 0, z); if (opt.rot) grp.rotation.y = opt.rot;
    var base = mesh(new T.BoxGeometry(w + 0.6, 0.35, d + 0.6), M('#a59a88'), 0, 0.17, 0); base.receiveShadow = true; grp.add(base);
    var step = mesh(new T.BoxGeometry(1.4, 0.18, 0.5), M('#b8ad9a'), 0, 0.09, d / 2 + 0.5); grp.add(step);
    var wall = mesh(new T.BoxGeometry(w - 0.3, wallH, d - 0.3), M(opt.wall || '#efe2c8'), 0, 0.35 + wallH / 2, 0); wall.receiveShadow = true; grp.add(wall);
    // cửa
    var door = mesh(new T.BoxGeometry(Math.min(1.1, w * 0.3), wallH * 0.75, 0.05), M('#5a1a10'), 0, 0.35 + wallH * 0.375, d / 2 - 0.13, false); grp.add(door);
    for (var wi = -1; wi <= 1; wi += 2) { var win = mesh(new T.BoxGeometry(w * 0.18, wallH * 0.35, 0.05), M('#ffcf7a', { em: '#ff9d3a', ei: 0.9 }), wi * w * 0.3, 0.35 + wallH * 0.55, d / 2 - 0.13, false); grp.add(win); }
    // cột đỏ
    var colG = G('col' + wallH, function () { return new T.CylinderGeometry(0.09, 0.1, wallH, 8); });
    var nx = Math.max(2, Math.round(w / 1.2)), nz = Math.max(2, Math.round(d / 1.2));
    for (var i = 0; i <= nx; i++) for (var j = 0; j <= nz; j++) {
      if (i !== 0 && i !== nx && j !== 0 && j !== nz) continue;
      grp.add(mesh(colG, M('#a3150c'), -w / 2 + w * i / nx, 0.35 + wallH / 2, -d / 2 + d * j / nz));
    }
    var beam = mesh(new T.BoxGeometry(w + 0.1, 0.18, d + 0.1), M('#7a1009'), 0, 0.35 + wallH, 0); grp.add(beam);
    var y0 = 0.35 + wallH + 0.05;
    var roofs = opt.tiers || 1;
    for (var t = 0; t < roofs; t++) {
      var sc = 1 - t * 0.32, rw = w * sc, rd = d * sc;
      if (t > 0) { var up = mesh(new T.BoxGeometry(rw * 0.8, 0.7, rd * 0.8), M(opt.wall || '#efe2c8'), 0, y0 + 0.3, 0); grp.add(up); for (var q = -1; q <= 1; q += 2) for (var r = -1; r <= 1; r += 2) grp.add(mesh(G('colS', function () { return new T.CylinderGeometry(0.07, 0.07, 0.7, 6); }), M('#a3150c'), q * rw * 0.42, y0 + 0.3, r * rd * 0.42)); y0 += 0.65; }
      var rg = roofGeo(rw, rd, roofH * sc, 0.55 * sc, 0.55 * sc);
      var rm = new T.MeshToonMaterial({ color: opt.roof || '#c4321f', gradientMap: gradTex, map: roofTex, side: T.DoubleSide });
      var roof = mesh(rg, rm, 0, y0, 0); roof.receiveShadow = true; grp.add(roof);
      // nóc vàng + đầu rồng
      var rl = Math.max(0.2, rw - rd) + 0.3;
      var ridge = mesh(new T.BoxGeometry(rl, 0.16, 0.16), M('#7a1009'), 0, y0 + roofH * sc + 0.02, 0); grp.add(ridge);
      for (var s = -1; s <= 1; s += 2) { var orn = mesh(G('orn', function () { return new T.ConeGeometry(0.1, 0.45, 6); }), M('#e8b04a', { em: '#a06a10', ei: 0.3 }), s * rl / 2, y0 + roofH * sc + 0.2, 0); orn.rotation.z = -s * 0.5; grp.add(orn); }
      // đèn lồng dưới hiên
      if (opt.lanterns !== false && t === 0) for (var k = -1; k <= 1; k += 2) { var L = lanternMesh(); L.position.set(k * (w / 2 - 0.2), y0 - 0.35, d / 2 + 0.35); grp.add(L); }
      y0 += roofH * sc * 0.55;
    }
    scene.add(grp); return grp;
  }
  function lanternMesh() {
    var g = new T.Group();
    var body = mesh(G('lant', function () { var s = new T.SphereGeometry(0.17, 10, 8); s.scale(1, 1.25, 1); return s; }), M('#ff3d1a', { em: '#ff4a20', ei: 1.6 }), 0, 0, 0, false);
    g.add(body);
    g.add(mesh(G('lcap', function () { return new T.CylinderGeometry(0.1, 0.1, 0.05, 8); }), M('#e8b04a'), 0, 0.22, 0, false));
    g.add(mesh(G('lcap', null), M('#e8b04a'), 0, -0.22, 0, false));
    var gl = glowSprite('#ff7a3a', 1.1, 0.55); g.add(gl);
    LANT.push(gl);
    return g;
  }
  var LANT = [];
  function lanternPost(x, z) {
    var g = new T.Group(); g.position.set(x, 0, z);
    g.add(mesh(G('pb', function () { return new T.BoxGeometry(0.3, 0.2, 0.3); }), M('#8c7d6c'), 0, 0.1, 0));
    g.add(mesh(G('pp', function () { return new T.CylinderGeometry(0.06, 0.07, 1.3, 6); }), M('#5a4a3a'), 0, 0.8, 0));
    g.add(mesh(G('pt', function () { return new T.ConeGeometry(0.28, 0.2, 4); }), M('#3a2a1a'), 0, 1.62, 0));
    var L = lanternMesh(); L.position.y = 1.35; g.add(L);
    scene.add(g);
  }
  // Cây chi tiết: thân cong nhiều cành + tán gồm hàng trăm chùm hoa/lá (instanced)
  var blobG = null;
  function branchMesh(g, p0, p1, r0, r1, mat) {
    var d = new T.Vector3().subVectors(p1, p0), len = d.length();
    var m = new T.Mesh(cyl(r1, r0, 1, 6), mat); m.scale.y = len; m.castShadow = true;
    m.position.copy(p0).addScaledVector(d, 0.5); m.quaternion.setFromUnitVectors(new T.Vector3(0, 1, 0), d.clone().normalize()); g.add(m);
  }
  function blossomTree(x, z, s, pink) {
    var g = new T.Group(); g.position.set(x, 0, z); g.scale.setScalar(s);
    var bark = M('#3e2418'), tips = [];
    function grow(p, dir, len, r, depth) {
      var end = p.clone().addScaledVector(dir, len); branchMesh(g, p, end, r, r * 0.68, bark);
      if (depth === 0) { tips.push(end); return; }
      var n = depth > 2 ? 2 : 3;
      for (var i = 0; i < n; i++) { var nd = dir.clone().add(new T.Vector3((Math.random() - 0.5) * 1.3, 0.35 + Math.random() * 0.3, (Math.random() - 0.5) * 1.3)).normalize(); grow(end, nd, len * (0.62 + Math.random() * 0.15), r * 0.66, depth - 1); }
      if (depth < 3) tips.push(end);
    }
    grow(new T.Vector3(0, 0, 0), new T.Vector3(0.1, 1, 0.05).normalize(), 1.05, 0.17, 3);
    if (!blobG) blobG = new T.IcosahedronGeometry(0.16, 0);
    var cols = pink ? ['#ff6f8e', '#ff9db3', '#f04d78', '#ffc2d1', '#ffe0ea'] : ['#3f8a4a', '#5aa860', '#2e6b3a', '#78c27a', '#4d9a40'];
    var per = 22, im = new T.InstancedMesh(blobG, new T.MeshLambertMaterial({ color: '#ffffff' }), tips.length * per), mtx = new T.Matrix4(), q = new T.Quaternion(), sc = new T.Vector3(), pp = new T.Vector3(), c = new T.Color(), k = 0;
    tips.forEach(function (tp) { for (var j = 0; j < per; j++) { pp.set(tp.x + (Math.random() - 0.5) * 0.75, tp.y + (Math.random() - 0.3) * 0.5, tp.z + (Math.random() - 0.5) * 0.75); q.setFromEuler(new T.Euler(Math.random() * 3, Math.random() * 3, 0)); var ss = 0.7 + Math.random() * 0.9; sc.set(ss, ss, ss); mtx.compose(pp, q, sc); im.setMatrixAt(k, mtx); c.set(cols[(Math.random() * cols.length) | 0]); im.setColorAt(k, c); k++; } });
    im.castShadow = true; g.add(im);
    if (pink) { var fg = glowSprite('#ff9db3', 2.6, 0.18); fg.position.y = 2.2; g.add(fg); }
    scene.add(g); TREES.push(g);
  }
  // liễu rủ bên hồ
  var WILLOWS = [];
  function willow(x, z, s) {
    var g = new T.Group(); g.position.set(x, 0, z); g.scale.setScalar(s);
    var bark = M('#4a3322');
    branchMesh(g, new T.Vector3(0, 0, 0), new T.Vector3(0.3, 2.2, 0), 0.22, 0.14, bark);
    branchMesh(g, new T.Vector3(0.3, 2.2, 0), new T.Vector3(-0.5, 3.0, 0.3), 0.13, 0.07, bark);
    branchMesh(g, new T.Vector3(0.3, 2.2, 0), new T.Vector3(1.0, 3.1, -0.3), 0.13, 0.07, bark);
    var strandG = G('strand', function () { var pg = new T.PlaneGeometry(0.12, 2.0, 1, 8); pg.translate(0, -1, 0); return pg; });
    var sm = new T.MeshLambertMaterial({ color: '#8ec24a', side: T.DoubleSide, transparent: true, opacity: 0.95 });
    var strands = [];
    for (var i = 0; i < 70; i++) { var a = Math.random() * 6.28, r = 0.2 + Math.random() * 1.3; var st = new T.Mesh(strandG, sm); st.position.set(0.2 + Math.cos(a) * r, 3.0 + Math.random() * 0.4, Math.sin(a) * r); st.rotation.y = Math.random() * 3; st.scale.y = 0.7 + Math.random() * 0.6; g.add(st); strands.push(st); }
    g.userData.strands = strands; scene.add(g); WILLOWS.push(g);
  }
  // gạch tường thành
  var brickTex = null;
  var bumpTex = null;
  function wallMat(w, h, tint) {
    if (!brickTex) {
      var cw = 512, rows = 12, bump = document.createElement('canvas'); bump.width = bump.height = cw; var bg = bump.getContext('2d');
      brickTex = canvasTex(cw, cw, function (gg) {
        gg.fillStyle = '#5a5248'; gg.fillRect(0, 0, cw, cw); bg.fillStyle = '#202020'; bg.fillRect(0, 0, cw, cw);
        var rh = cw / rows;
        for (var y = 0; y < rows; y++) { var x = -(y % 2) * 30 - Math.random() * 20; while (x < cw) { var bw = 50 + Math.random() * 50;
          var v = 110 + Math.random() * 45 | 0, warm = Math.random() * 14;
          var gr = gg.createLinearGradient(0, y * rh, 0, y * rh + rh); gr.addColorStop(0, 'rgb(' + (v + 12 + warm) + ',' + (v + 4) + ',' + (v - 12) + ')'); gr.addColorStop(1, 'rgb(' + (v - 18 + warm) + ',' + (v - 24) + ',' + (v - 38) + ')');
          gg.fillStyle = gr; gg.fillRect(x + 2, y * rh + 2, bw - 4, rh - 4);
          for (var k = 0; k < 18; k++) { gg.fillStyle = 'rgba(' + (Math.random() < 0.5 ? '0,0,0' : '255,240,220') + ',' + (Math.random() * 0.12) + ')'; gg.fillRect(x + 2 + Math.random() * (bw - 6), y * rh + 2 + Math.random() * (rh - 6), 2 + Math.random() * 5, 1 + Math.random() * 3); }
          var bgr = bg.createRadialGradient(x + bw / 2, y * rh + rh / 2, 2, x + bw / 2, y * rh + rh / 2, bw * 0.6); bgr.addColorStop(0, '#f0f0f0'); bgr.addColorStop(1, '#9a9a9a'); bg.fillStyle = bgr; bg.fillRect(x + 3, y * rh + 3, bw - 6, rh - 6);
          if (Math.random() < 0.15) { gg.strokeStyle = 'rgba(20,15,10,.5)'; gg.lineWidth = 1.5; gg.beginPath(); gg.moveTo(x + Math.random() * bw, y * rh + 3); gg.lineTo(x + Math.random() * bw, y * rh + rh - 3); gg.stroke(); }
          x += bw; } }
        for (var i = 0; i < 70; i++) { gg.fillStyle = 'rgba(70,100,45,' + (Math.random() * 0.3) + ')'; gg.beginPath(); gg.arc(Math.random() * cw, cw * 0.72 + Math.random() * cw * 0.28, 6 + Math.random() * 22, 0, 6.3); gg.fill(); }
        var dg = gg.createLinearGradient(0, 0, 0, cw); dg.addColorStop(0, 'rgba(0,0,0,0)'); dg.addColorStop(1, 'rgba(20,15,10,.35)'); gg.fillStyle = dg; gg.fillRect(0, 0, cw, cw);
      });
      bumpTex = new T.CanvasTexture(bump);
    }
    var t = brickTex.clone(), b2 = bumpTex.clone(); [t, b2].forEach(function (x) { x.needsUpdate = true; x.wrapS = x.wrapT = T.RepeatWrapping; x.repeat.set(Math.max(1, w / 3.2), Math.max(1, h / 3.2)); });
    return new T.MeshPhongMaterial({ color: tint || '#ffffff', map: t, bumpMap: b2, bumpScale: 0.06, shininess: 6, specular: '#2a2620' });
  }
  var TREES = [];

  // ---------- CẢNH ----------
  var laneMeshes = [], gridLines = [], portals = [], gates = [], petals;
  function buildScene() {
    scene = new T.Scene();
    var sky = canvasTex(4, 256, function (g, w, h) { var gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, '#1d1638'); gr.addColorStop(0.45, '#6b2f4a'); gr.addColorStop(0.75, '#e0794a'); gr.addColorStop(1, '#ffc27a'); g.fillStyle = gr; g.fillRect(0, 0, w, h); });
    scene.background = sky;
    scene.fog = new T.Fog('#7a4248', 45, 110);
    scene.add(new T.HemisphereLight('#ffd0b0', '#3a2440', 0.42));
    sun = new T.DirectionalLight('#ffc48a', 0.85); sun.position.set(-14, 24, 12); sun.target.position.set(MX, 0, 0);
    sun.castShadow = true; sun.shadow.mapSize.set(LOW ? 1024 : 2048, LOW ? 1024 : 2048);
    var sc = sun.shadow.camera; sc.left = -28; sc.right = 28; sc.top = 26; sc.bottom = -26; sc.near = 1; sc.far = 70; sun.shadow.bias = -0.0006; sun.shadow.normalBias = 0.02;
    scene.add(sun); scene.add(sun.target);
    var rim = new T.DirectionalLight('#8a7bff', 0.35); rim.position.set(14, 10, -20); scene.add(rim);

    // nền đá
    var stone = canvasTex(256, 256, function (g) {
      g.fillStyle = '#4e4a44'; g.fillRect(0, 0, 256, 256);
      for (var y = 0; y < 8; y++) for (var x = 0; x < 8; x++) { var v = 104 + Math.random() * 26 | 0; g.fillStyle = 'rgb(' + (v + 2) + ',' + v + ',' + (v - 6) + ')'; g.fillRect(x * 32 + 1, y * 32 + 1, 30, 30); }
      g.fillStyle = 'rgba(0,0,0,0.05)'; for (var i = 0; i < 300; i++) g.fillRect(Math.random() * 256, Math.random() * 256, 2, 2);
    }, [40, 30]);
    var ground = mesh(new T.PlaneGeometry(130, 56), M('#ffffff', { map: stone }), MX, 0, -17, false); ground.rotation.x = -Math.PI / 2; ground.receiveShadow = true; scene.add(ground);

    for (var lane = 0; lane < 2; lane++) {
      var lt = canvasTex(LW * 20, 400, function (g, w, h) {
        // 9 ô x 20 hàng (sim y -1..19). trục canvas: trên = phía thành (sim y lớn)
        for (var r = 0; r < 20; r++) for (var c = 0; c < LW; c++) {
          var simY = 19 - r - 1 + 0.5 - 1; // r=0 -> simY 17.5
          var col;
          if (simY > 14.6) col = ((r + c) & 1) ? '#8c735e' : '#836b57';
          else if (simY < 1.6) col = ((r + c) & 1) ? '#6e2a24' : '#64241f';
          else col = ((r + c) & 1) ? '#b8a88e' : '#ad9c82';
          g.fillStyle = col; g.fillRect(c * 20, r * 20, 20, 20);
          g.strokeStyle = 'rgba(60,40,25,0.45)'; g.strokeRect(c * 20 + 0.5, r * 20 + 0.5, 19, 19); g.fillStyle='rgba(255,240,210,0.08)'; g.fillRect(c*20+2,r*20+2,16,3);
        }
        var cx0 = (HL - 1.5) * 20; g.fillStyle = '#9b1f16'; g.fillRect(cx0, 0, 60, 70); g.fillStyle = '#b8291d'; g.fillRect(cx0 + 20, 0, 20, 70);
        g.strokeStyle = '#e8b04a'; g.lineWidth = 2; g.strokeRect(cx0 + 1, -2, 58, 72);
      });
      lt.magFilter = T.LinearFilter;
      var lm = mesh(new T.PlaneGeometry(LW, 20), M('#ffffff', { map: lt }), LCX[lane], 0.02, -0.5, false);
      // sim y -1..19 -> z 10..-10, tâm z=0 ; tâm plane ở z = 9 - 9 = 0
      lm.position.z = 0; lm.rotation.x = -Math.PI / 2; lm.receiveShadow = true; scene.add(lm); laneMeshes.push(lm);
      // bờ đá
      for (var sgn = -1; sgn <= 1; sgn += 2) { var cb = mesh(G('curb', function () { return new T.BoxGeometry(0.22, 0.22, 20); }), M('#a39680'), LCX[lane] + sgn * (HL + 0.12), 0.11, 0); cb.receiveShadow = true; scene.add(cb); }
      // lưới xây
      var pts = [];
      for (var cx = 0; cx <= LW; cx++) { var a = W(lane, cx, 2, 0.035), b = W(lane, cx, 14, 0.035); pts.push(a, b); }
      for (var cy = 2; cy <= 14; cy++) { var a2 = W(lane, 0, cy, 0.035), b2 = W(lane, LW, cy, 0.035); pts.push(a2, b2); }
      var gl = new T.LineSegments(new T.BufferGeometry().setFromPoints(pts), new T.LineBasicMaterial({ color: '#e8b04a', transparent: true, opacity: 0.0 }));
      scene.add(gl); gridLines.push(gl);
      // trận pháp xuất quân (gần camera)
      var pg = new T.Group(); pg.position.copy(W(lane, HL, -0.6, 0.05));
      var disk = new T.Mesh(new T.PlaneGeometry(5.2, 5.2), new T.MeshBasicMaterial({ map: runeTex, color: '#c64dff', transparent: true, opacity: 0.85, blending: T.AdditiveBlending, depthWrite: false }));
      disk.rotation.x = -Math.PI / 2; pg.add(disk);
      var disk2 = new T.Mesh(new T.PlaneGeometry(3.4, 3.4), new T.MeshBasicMaterial({ map: runeTex, color: '#ff5a3a', transparent: true, opacity: 0.8, blending: T.AdditiveBlending, depthWrite: false }));
      disk2.rotation.x = -Math.PI / 2; disk2.position.y = 0.02; pg.add(disk2);
      var beam = new T.Mesh(new T.CylinderGeometry(1.3, 1.6, 3, 24, 1, true), new T.MeshBasicMaterial({ color: '#b03cff', transparent: true, opacity: 0.12, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide }));
      beam.position.y = 1.5; pg.add(beam);
      scene.add(pg); portals.push({ g: pg, d1: disk, d2: disk2, beam: beam });
      gates.push(gateFort(lane));
    }
    buildLake();
    buildGrass();
    buildAmbient();
    buildProps();
    buildBackdrop();
    // vườn giữa
    var grass = canvasTex(64, 64, function (g) { g.fillStyle = '#5e7f3e'; g.fillRect(0, 0, 64, 64); for (var i = 0; i < 160; i++) { g.fillStyle = Math.random() < 0.5 ? '#6f9448' : '#4f6e32'; g.fillRect(Math.random() * 64, Math.random() * 64, 2, 3); } }, [3, 12]);
    var gm = mesh(new T.PlaneGeometry(LCX[1] - LW - 0.3, 20), M('#ffffff', { map: grass }), MX, 0.015, 0, false); gm.rotation.x = -Math.PI / 2; gm.receiveShadow = true; scene.add(gm);
    for (var z = -7; z <= 9; z += 4) { lanternPost(MX - 2.4, z); lanternPost(MX + 2.4, z + 2); }
    for (var z2 = -6; z2 <= 9; z2 += 5) blossomTree(MX, z2, 1.15, true);
    // nhà hai bên
    [[-HL - 5, -6], [-HL - 5, -0.5], [-HL - 5, 5], [-HL - 5.5, 10.5]].forEach(function (p, i) { hall(p[0], p[1], 3.2, 4.2, 1.4, 1.5, { rot: Math.PI / 2, tiers: i === 1 ? 2 : 1 }); });
    [[LCX[1] + HL + 5, -6], [LCX[1] + HL + 5, -0.5], [LCX[1] + HL + 5, 5], [LCX[1] + HL + 5.5, 10.5]].forEach(function (p, i) { hall(p[0], p[1], 3.2, 4.2, 1.4, 1.5, { rot: -Math.PI / 2, tiers: i === 2 ? 2 : 1 }); });
    blossomTree(-HL - 1.9, 2.3, 1.1, true); blossomTree(-HL - 2.1, 8, 1, false); blossomTree(LCX[1] + HL + 1.9, 2.3, 1.1, false); blossomTree(LCX[1] + HL + 2.1, 8, 1, true);
    blossomTree(-HL - 1.6, -9, 1.2, true); blossomTree(LCX[1] + HL + 1.6, -9, 1.2, true); blossomTree(-HL - 2, -3.5, 0.9, false); blossomTree(LCX[1] + HL + 2, -3.5, 0.9, true);
    // điện chính phía xa
    hall(MX, -17, 9, 4.4, 2.4, 2.6, { tiers: 2, wall: '#f3e6cc' });
    hall(MX - 11, -16.5, 5, 3, 1.6, 1.8, {}); hall(MX + 11, -16.5, 5, 3, 1.6, 1.8, {}); hall(MX - 19, -15, 4, 3, 1.4, 1.6, {}); hall(MX + 19, -15, 4, 3, 1.4, 1.6, {});
    // tường thành dài + tháp canh
    var wallM2 = M('#8f8270');
    var wl = mesh(new T.BoxGeometry(LCX[1] + LW + 34, 3.2, 1.4), wallMat(LCX[1] + LW + 34, 3.2), MX, 1.6, -13.6); wl.receiveShadow = true; scene.add(wl);
    var crM = wallMat(0.6, 0.5); for (var cx2 = MX - (LCX[1] + LW + 32) / 2; cx2 < MX + (LCX[1] + LW + 32) / 2; cx2 += 1.1) scene.add(mesh(G('cren2', function () { return new T.BoxGeometry(0.6, 0.5, 0.4); }), crM, cx2, 3.45, -12.95));
    [MX - (LCX[1] + LW + 30) / 2, MX + (LCX[1] + LW + 30) / 2].forEach(function (tx) { var tw = mesh(new T.BoxGeometry(3.2, 5, 3.2), wallMat(3.2, 5), tx, 2.5, -13.6); scene.add(tw); var th = hall(tx, -13.6, 3.4, 3.4, 1.1, 1.3, { tiers: 2 }); th.position.y = 5; });
    // bảo tháp 7 tầng phía xa
    var tower = new T.Group(); tower.position.set(MX, 0, -26);
    for (var lv = 0; lv < 7; lv++) { var sz = 5.2 - lv * 0.55, y0 = lv * 2.1; var blk = mesh(new T.CylinderGeometry(sz * 0.42, sz * 0.46, 1.5, 8), M(lv % 2 ? '#e9d8b8' : '#f1e3c6'), 0, y0 + 0.75, 0); tower.add(blk); var rf = mesh(roofGeo(sz, sz, 0.9, 0.55, 0.55), new T.MeshToonMaterial({ color: '#b52a1a', gradientMap: gradTex, map: roofTex, side: T.DoubleSide }), 0, y0 + 1.5, 0); tower.add(rf); var tl3 = lanternMesh(); tl3.position.set(0, y0 + 1.2, sz * 0.5 + 0.3); tower.add(tl3); }
    var spire = mesh(new T.ConeGeometry(0.35, 3, 8), M('#e8b04a', { em: '#a06a10', ei: 0.5 }), 0, 7 * 2.1 + 1.5, 0); tower.add(spire);
    var tg = glowSprite('#ffcf7a', 3, 0.6); tg.position.y = 7 * 2.1 + 3; tower.add(tg);
    scene.add(tower);
    // sư tử đá trước cổng
    for (var ln = 0; ln < 2; ln++) for (var sd2 = -1; sd2 <= 1; sd2 += 2) {
      var lg = new T.Group(); lg.position.set(LCX[ln] + sd2 * 2.4, 0, -9.3);
      lg.add(mesh(new T.BoxGeometry(0.9, 0.5, 0.9), M('#9e9384'), 0, 0.25, 0));
      lg.add(mesh(G('lionb', function () { var g = new T.SphereGeometry(0.38, 10, 8); g.scale(0.8, 1, 1.1); return g; }), M('#b3a893'), 0, 0.85, 0));
      lg.add(mesh(G('lionh', function () { return new T.SphereGeometry(0.3, 10, 8); }), M('#b3a893'), 0, 1.35, 0.18));
      lg.add(mesh(G('lionm', function () { return new T.TorusGeometry(0.28, 0.1, 6, 12); }), M('#a39882'), 0, 1.33, 0.12));
      scene.add(lg);
    }
    // lư hương giữa vườn
    var urn = new T.Group(); urn.position.set(MX, 0, -9);
    urn.add(mesh(new T.CylinderGeometry(0.7, 0.5, 0.8, 10), M('#6d5a3a', { em: '#2a1a00', ei: 0.2 }), 0, 0.6, 0)); urn.add(mesh(new T.CylinderGeometry(0.9, 0.9, 0.12, 12), M('#8d7a4a'), 0, 1.05, 0));
    var smoke = glowSprite('#ffe0b0', 1.4, 0.35); smoke.position.y = 1.6; urn.add(smoke); scene.add(urn); LANT.push(smoke);
    // núi xa
    for (var m = 0; m < 9; m++) { var mt = mesh(new T.ConeGeometry(8 + (m % 3) * 4, 12 + (m % 4) * 5, 5), M(m % 2 ? '#4a3150' : '#5a3a58'), MX - 36 + m * 9, 3, -38 - (m % 2) * 6, false); scene.add(mt); }
    // mặt trời lặn
    var sunDisc = glowSprite('#ffb060', 22, 0.8); sunDisc.position.set(MX - 10, 7, -50); scene.add(sunDisc);
    // dây đèn lồng phía sau
    for (var s = 0; s < 2; s++) for (var k = 0; k < 9; k++) { var L = lanternMesh(); var t = k / 8; L.position.set(LCX[s] - HL + t * LW, 3.4 - Math.sin(t * Math.PI) * 0.6, -12.6); L.scale.setScalar(0.8); scene.add(L); }
    // cánh hoa rơi
    var pc = 140, pgeo = new T.BufferGeometry(), pp = new Float32Array(pc * 3);
    for (var i = 0; i < pc; i++) { pp[i * 3] = MX - 18 + Math.random() * 36; pp[i * 3 + 1] = Math.random() * 9; pp[i * 3 + 2] = -14 + Math.random() * 26; }
    pgeo.setAttribute('position', new T.BufferAttribute(pp, 3));
    var petalTex = canvasTex(32, 32, function (g) { g.fillStyle = '#fff'; g.beginPath(); g.ellipse(16, 16, 12, 6, 0.6, 0, 6.283); g.fill(); });
    petals = new T.Points(pgeo, new T.PointsMaterial({ color: '#ffb3c6', size: 0.22, map: petalTex, transparent: true, depthWrite: false, opacity: 0.9 }));
    scene.add(petals);
  }
  // ---------- HỒ SEN phía trước + nước thật ----------
  var water = null, LOTUS = [], GRASSM = null, SWAY = [];
  function buildLake() {
    var wn = new T.TextureLoader().load(window.TEX_WATER, function (t) { t.wrapS = t.wrapT = T.RepeatWrapping; });
    wn.wrapS = wn.wrapT = T.RepeatWrapping;
    var geo = new T.PlaneGeometry(110, 30);
    water = new T.Water(geo, { textureWidth: LOW ? 192 : 512, textureHeight: LOW ? 192 : 512, waterNormals: wn, sunDirection: new T.Vector3(-0.5, 0.6, 0.6).normalize(), sunColor: 0xffc88a, waterColor: 0x1c3a44, distortionScale: 2.4, fog: true, alpha: 1 });
    water.rotation.x = -Math.PI / 2; water.position.set(MX, -0.32, 26); scene.add(water);
    // bờ kè đá
    var bank = mesh(new T.BoxGeometry(110, 0.7, 0.9), wallMat(110, 0.7), MX, -0.25, 11.4); bank.receiveShadow = true; scene.add(bank);
    var cap = mesh(new T.BoxGeometry(110, 0.12, 1.1), M('#b5a891'), MX, 0.12, 11.4); scene.add(cap);
    for (var x = -HL - 10; x < LCX[1] + HL + 10; x += 2.2) { var post = mesh(G('rail', function () { return new T.BoxGeometry(0.16, 0.55, 0.16); }), M('#c9bca4'), x, 0.45, 11.75); scene.add(post); }
    var railTop = mesh(new T.BoxGeometry(110, 0.08, 0.1), M('#c9bca4'), MX, 0.7, 11.75); scene.add(railTop);
    // bậc đá từ trận pháp xuống nước (cho cảnh giặc lội lên)
    for (var lane = 0; lane < 2; lane++) for (var k = 0; k < 3; k++) { var st = mesh(new T.BoxGeometry(3.4 - k * 0.2, 0.18, 0.6), M('#9e917c'), LCX[lane], -0.05 - k * 0.12, 11.9 + k * 0.6); st.receiveShadow = true; scene.add(st); }
    // lá sen + hoa sen
    var padG = G('pad', function () { var g = new T.CircleGeometry(0.55, 14, 0.35, Math.PI * 2 - 0.35); g.rotateX(-Math.PI / 2); return g; });
    for (var i = 0; i < 70; i++) {
      var px = MX - 40 + Math.random() * 80, pz = 13 + Math.random() * 14;
      if (Math.abs(px - LCX[0]) < 2.5 && pz < 15) continue; if (Math.abs(px - LCX[1]) < 2.5 && pz < 15) continue;
      var g = new T.Group(); g.position.set(px, -0.27, pz); g.rotation.y = Math.random() * 6.28;
      var pad = mesh(padG, M(i % 3 ? '#3f7d3a' : '#4f9446', { side: T.DoubleSide }), 0, 0, 0, false); pad.scale.setScalar(0.7 + Math.random() * 0.7); pad.receiveShadow = true; g.add(pad);
      if (i % 3 === 0) {
        var fl = new T.Group(); fl.position.y = 0.12;
        for (var j = 0; j < 7; j++) { var pt = mesh(G('lpetal', function () { var c = new T.SphereGeometry(0.12, 8, 6); c.scale(0.55, 1.3, 0.35); c.translate(0, 0.14, 0); return c; }), M(j % 2 ? '#ff8fb1' : '#ffc1d6', { em: '#ff5c8a', ei: 0.15 }), 0, 0, 0, false); pt.rotation.y = j / 7 * 6.28; pt.rotation.z = 0.55; fl.add(pt); }
        fl.add(mesh(sph(0.07, 8, 6), M('#ffd54f', { em: '#ffb300', ei: 0.6 }), 0, 0.08, 0, false));
        g.add(fl);
      }
      scene.add(g); LOTUS.push(g);
    }
    [-HL - 13, -HL - 6.5, MX - 1.5, MX + 1.5, LCX[1] + HL + 6.5, LCX[1] + HL + 13].forEach(function (wx, i) { willow(wx, 12.2 + (i % 2) * 0.3, 0.9 + (i % 3) * 0.12); });
    // thuyền nhỏ
    var boat = new T.Group(); boat.position.set(MX + 9, -0.25, 19);
    boat.add(mesh(new T.BoxGeometry(3, 0.35, 0.9), M('#6d4c41'), 0, 0.1, 0));
    var roofB = mesh(new T.CylinderGeometry(0.7, 0.7, 1.4, 12, 1, true, 0, Math.PI), M('#8d6e63', { side: T.DoubleSide }), 0, 0.35, 0); roofB.rotation.z = Math.PI / 2; roofB.rotation.y = Math.PI / 2; boat.add(roofB);
    var bl = lanternMesh(); bl.position.set(1.3, 0.7, 0); boat.add(bl);
    scene.add(boat); LOTUS.push(boat); boat.userData.boat = 1;
    // đèn hoa đăng trôi
    for (var q = 0; q < 14; q++) { var fl2 = glowSprite('#ffb15a', 0.9, 0.85); fl2.position.set(MX - 30 + Math.random() * 60, -0.15, 13 + Math.random() * 12); scene.add(fl2); var base = mesh(G('lbase', function () { return new T.CylinderGeometry(0.14, 0.18, 0.1, 6); }), M('#ff7043', { em: '#ff5722', ei: 1.4 }), 0, -0.05, 0, false); fl2.add(base); LOTUS.push(fl2); fl2.userData.drift = 0.2 + Math.random() * 0.3; }
  }
  // cỏ bay theo gió (instanced, uốn trong shader)
  var windU = { value: 0 };
  function buildGrass() {
    var bl = new T.ConeGeometry(0.035, 0.42, 3); bl.translate(0, 0.21, 0);
    GRASSM = new T.MeshToonMaterial({ color: '#7fae4c', gradientMap: gradTex });
    GRASSM.onBeforeCompile = function (sh) {
      sh.uniforms.uTime = windU;
      sh.vertexShader = 'uniform float uTime;\n' + sh.vertexShader.replace('#include <begin_vertex>', '#include <begin_vertex>\n vec4 ip = instanceMatrix[3]; float h = position.y; transformed.x += sin(uTime*2.2 + ip.x*0.6 + ip.z*0.45) * 0.16 * h * h * 4.0; transformed.z += cos(uTime*1.7 + ip.x*0.3) * 0.06 * h;');
    };
    var n = LOW ? 1100 : 2600, im = new T.InstancedMesh(bl, GRASSM, n), m = new T.Matrix4(), q = new T.Quaternion(), sc = new T.Vector3(), ps = new T.Vector3(), col = new T.Color();
    var w = LCX[1] - LW - 0.6;
    for (var i = 0; i < n; i++) {
      var zone = i % 5, x, z;
      if (zone < 3) { x = MX + (Math.random() - 0.5) * w; z = -9.8 + Math.random() * 19.6; }
      else if (zone === 3) { x = -HL - 1.2 - Math.random() * 1.4; z = -9 + Math.random() * 19; }
      else { x = LCX[1] + HL + 1.2 + Math.random() * 1.4; z = -9 + Math.random() * 19; }
      ps.set(x, 0, z); q.setFromAxisAngle(new T.Vector3(0, 1, 0), Math.random() * 6.28); var s2 = 0.6 + Math.random() * 0.9; sc.set(s2, s2 * (0.7 + Math.random() * 0.8), s2);
      m.compose(ps, q, sc); im.setMatrixAt(i, m); col.setHSL(0.22 + Math.random() * 0.06, 0.45, 0.32 + Math.random() * 0.14); im.setColorAt(i, col);
    }
    im.receiveShadow = true; scene.add(im);
    // trúc xanh hai bên
    for (var k = 0; k < 16; k++) {
      var side = k % 2 ? -HL - 2.6 : LCX[1] + HL + 2.6, bz = -9 + (k >> 1) * 2.6 + Math.random();
      var bam = new T.Group(); bam.position.set(side + (Math.random() - 0.5), 0, bz);
      for (var c = 0; c < 4; c++) {
        var cg = new T.Group(); cg.position.set((Math.random() - 0.5) * 0.6, 0, (Math.random() - 0.5) * 0.6); cg.rotation.z = (Math.random() - 0.5) * 0.15;
        var hh = 2.4 + Math.random() * 1.4;
        for (var sgi = 0; sgi < 5; sgi++) { var seg = mesh(G('bseg', function () { return new T.CylinderGeometry(0.045, 0.05, 0.6, 6); }), M('#6f9a3a'), 0, sgi * hh / 5 + 0.3, 0); seg.scale.y = hh / 3; cg.add(seg); cg.add(mesh(G('bnode', function () { return new T.CylinderGeometry(0.055, 0.055, 0.04, 6); }), M('#4e6e28'), 0, (sgi + 1) * hh / 5, 0, false)); }
        for (var lf = 0; lf < 6; lf++) { var leaf = mesh(G('bleaf', function () { var g = new T.PlaneGeometry(0.08, 0.45); g.translate(0, 0.22, 0); return g; }), M('#86b84a', { side: T.DoubleSide }), 0, hh * (0.55 + lf * 0.08), 0, false); leaf.rotation.set(0.9, lf * 1.1, 0); cg.add(leaf); }
        bam.add(cg); SWAY.push({ o: cg, a: 0.05, ph: Math.random() * 6 });
      }
      scene.add(bam);
    }
  }

  // ---------- TIỂU CẢNH quanh bản đồ ----------
  function stoneLantern(x, z, s) {
    var g = new T.Group(); g.position.set(x, 0, z); g.scale.setScalar(s || 1); var st = M('#a8a294');
    g.add(mesh(cyl(0.32, 0.38, 0.2, 6), st, 0, 0.1, 0)); g.add(mesh(cyl(0.09, 0.12, 0.8, 6), st, 0, 0.6, 0)); g.add(mesh(cyl(0.3, 0.22, 0.12, 6), st, 0, 1.05, 0));
    g.add(mesh(box(0.34, 0.3, 0.34), M('#ffd18a', { em: '#ff9d3a', ei: 1.3 }), 0, 1.26, 0)); g.add(mesh(cone(0.42, 0.32, 6), st, 0, 1.58, 0)); g.add(mesh(sph(0.06), st, 0, 1.78, 0));
    var gl = glowSprite('#ffb15a', 1.2, 0.5); gl.position.y = 1.26; g.add(gl); LANT.push(gl); scene.add(g);
  }
  function pine(x, z, s) {
    var g = new T.Group(); g.position.set(x, 0, z); g.scale.setScalar(s);
    branchMesh(g, new T.Vector3(0, 0, 0), new T.Vector3(0.25, 1.6, 0.1), 0.16, 0.09, M('#4a3322'));
    [[0.25, 1.7, 0.1, 1.1], [-0.4, 1.3, 0.2, 0.8], [0.7, 1.25, -0.2, 0.75], [0.2, 2.15, 0, 0.7]].forEach(function (c) { var pad = mesh(G('pinepad', function () { var gg = new T.SphereGeometry(0.6, 10, 6); gg.scale(1.2, 0.35, 1.1); return gg; }), M('#2f5d36'), c[0], c[1], c[2]); pad.scale.setScalar(c[3]); g.add(pad); });
    scene.add(g); TREES.push(g);
  }
  function stall(x, z, rot, col) {
    var g = new T.Group(); g.position.set(x, 0, z); g.rotation.y = rot || 0; var wood = M('#6d4c41');
    g.add(mesh(box(2, 0.12, 0.9), wood, 0, 0.8, 0)); g.add(mesh(box(1.9, 0.7, 0.8), M('#8d6e63'), 0, 0.38, 0));
    [[-0.95, -0.4], [0.95, -0.4], [-0.95, 0.4], [0.95, 0.4]].forEach(function (p2) { g.add(mesh(cyl(0.04, 0.04, 2, 5), wood, p2[0], 1, p2[1])); });
    var aw = mesh(G('awning', function () { return new T.PlaneGeometry(2.3, 1.3, 1, 1); }), M(col, { side: T.DoubleSide }), 0, 2.0, 0.1); aw.rotation.x = -1.2; g.add(aw);
    var goods = ['#ff7043', '#ffca28', '#8bc34a', '#e91e63', '#ffffff'];
    for (var i = 0; i < 9; i++) g.add(mesh(i % 2 ? sph(0.09, 6, 5) : box(0.16, 0.12, 0.16), M(goods[i % 5]), -0.8 + i * 0.2, 0.93, (i % 3 - 1) * 0.2));
    var L = lanternMesh(); L.position.set(0.95, 1.7, 0.6); L.scale.setScalar(0.7); g.add(L);
    g.add(mesh(cyl(0.22, 0.22, 0.5, 8), M('#795548'), 1.4, 0.25, 0.3)); g.add(mesh(box(0.45, 0.4, 0.45), M('#a1887f'), -1.4, 0.2, 0.2));
    scene.add(g);
  }
  function pondBridge(x, z, r) {
    var pm = new T.Mesh(new T.CircleGeometry(r, 32), new T.MeshPhongMaterial({ color: '#2b5560', shininess: 120, specular: '#ffd9a0', transparent: true, opacity: 0.92 }));
    pm.rotation.x = -Math.PI / 2; pm.position.set(x, 0.03, z); scene.add(pm);
    var rim = new T.Mesh(new T.TorusGeometry(r, 0.18, 6, 40), M('#9e9384')); rim.rotation.x = Math.PI / 2; rim.position.set(x, 0.05, z); scene.add(rim);
    var br = new T.Mesh(new T.TorusGeometry(r * 0.85, 0.16, 6, 20, Math.PI), M('#c62828')); br.position.set(x, -r * 0.35, z); br.scale.set(1, 0.6, 3.5); scene.add(br);
    for (var i = 0; i < 6; i++) { var a = Math.random() * 6.28, rr = Math.random() * r * 0.8; var pad = mesh(G('pad', null), M('#4f9446', { side: T.DoubleSide }), x + Math.cos(a) * rr, 0.06, z + Math.sin(a) * rr, false); scene.add(pad); }
    for (var k = 0; k < 10; k++) { var a2 = k / 10 * 6.28; var rk = mesh(G('rock', function () { return new T.DodecahedronGeometry(0.35, 0); }), M(k % 2 ? '#8d8a82' : '#a29e94'), x + Math.cos(a2) * (r + 0.4), 0.15, z + Math.sin(a2) * (r + 0.4)); rk.scale.set(1 + Math.random(), 0.6 + Math.random() * 0.5, 1 + Math.random()); scene.add(rk); }
  }
  function rockGarden(x, z, n) {
    for (var i = 0; i < n; i++) { var rk = mesh(G('rock', null), M(['#8d8a82', '#a29e94', '#7b776e'][i % 3]), x + (Math.random() - 0.5) * 2.4, 0.2, z + (Math.random() - 0.5) * 2.4); rk.scale.set(0.8 + Math.random() * 1.4, 0.6 + Math.random() * 1.6, 0.8 + Math.random() * 1.2); rk.rotation.y = Math.random() * 3; rk.receiveShadow = true; scene.add(rk); }
    var sand = new T.Mesh(new T.CircleGeometry(2, 24), M('#d8ccb4')); sand.rotation.x = -Math.PI / 2; sand.position.set(x, 0.02, z); sand.receiveShadow = true; scene.add(sand);
  }
  function planter(x, z, w) {
    var g = new T.Group(); g.position.set(x, 0, z);
    g.add(mesh(new T.BoxGeometry(w, 0.45, 0.8), wallMat(w, 0.45, '#e0d0b8'), 0, 0.22, 0));
    var cols = ['#ff5c8a', '#ffd54f', '#ff8a65', '#ba68c8', '#ffffff'];
    for (var i = 0; i < w * 6; i++) g.add(mesh(G('flw', function () { return new T.IcosahedronGeometry(0.09, 0); }), M(cols[i % 5]), (Math.random() - 0.5) * (w - 0.2), 0.52 + Math.random() * 0.1, (Math.random() - 0.5) * 0.6, false));
    for (var j = 0; j < w * 3; j++) g.add(mesh(G('flleaf', function () { return new T.IcosahedronGeometry(0.13, 0); }), M('#4f8a3a'), (Math.random() - 0.5) * (w - 0.2), 0.47, (Math.random() - 0.5) * 0.6, false));
    scene.add(g);
  }
  function buildProps() {
    var L0 = -HL - 13, R0 = LCX[1] + HL + 13;   // khu phố ngoài cùng hai bên
    // phố chợ
    [[-1, -8], [1, -3.5], [-1, 1], [1, 5.5]].forEach(function (p, i) { stall(L0 + p[0] * 1.5, p[1], Math.PI / 2, ['#c62828', '#1565c0', '#2e7d32', '#ef6c00'][i]); stall(R0 - p[0] * 1.5, p[1] + 1, -Math.PI / 2, ['#6a1b9a', '#c62828', '#00838f', '#f9a825'][i]); });
    // dãy nhà ngoài
    [-10, -3.5, 3, 9.5].forEach(function (z, i) { hall(L0 - 6, z, 3.6, 4.8, 1.5, 1.6, { rot: Math.PI / 2, tiers: i === 1 ? 2 : 1 }); hall(R0 + 6, z, 3.6, 4.8, 1.5, 1.6, { rot: -Math.PI / 2, tiers: i === 2 ? 2 : 1 }); });
    // ao + cầu, vườn đá, thông, đèn đá
    pondBridge(L0 + 4, -18, 3); pondBridge(R0 - 4, -18, 3);
    rockGarden(-HL - 8, -11, 7); rockGarden(LCX[1] + HL + 8, -11, 7); rockGarden(MX, -11.8, 5);
    [[-HL - 9, -2], [-HL - 9, 7], [LCX[1] + HL + 9, -2], [LCX[1] + HL + 9, 7], [L0 - 2, -14], [R0 + 2, -14], [MX - 4, -15], [MX + 4, -15]].forEach(function (p, i) { pine(p[0], p[1], 0.9 + (i % 3) * 0.15); });
    for (var z = -9; z <= 9; z += 3) { stoneLantern(-HL - 3.3, z, 0.9); stoneLantern(LCX[1] + HL + 3.3, z, 0.9); }
    [[-HL - 4, 10.3], [LCX[1] + HL + 4, 10.3], [MX - 3, 10.4], [MX + 3, 10.4]].forEach(function (p) { planter(p[0], p[1], 3); });
    // cờ xí dọc đường
    for (var f = 0; f < 6; f++) { [L0 + 3.2, R0 - 3.2].forEach(function (fx, si) { var pole = mesh(G('pole2', function () { return new T.CylinderGeometry(0.05, 0.05, 4, 5); }), M('#3a2a1a'), fx, 2, -10 + f * 3.8); scene.add(pole); var fl = mesh(G('flag2', function () { return new T.PlaneGeometry(0.7, 1.8, 3, 6); }), M(['#c62828', '#f9a825', '#1565c0'][(f + si) % 3], { side: T.DoubleSide }), fx + 0.36, 3.0, -10 + f * 3.8); scene.add(fl); FLAGS.push(fl); }); }
    // đá cuội & thùng gỗ rải rác
    for (var i = 0; i < 40; i++) { var side = i % 2 ? 1 : -1, bx = side < 0 ? L0 + (Math.random() - 0.5) * 8 : R0 + (Math.random() - 0.5) * 8; var o = mesh(i % 4 ? G('rock', null) : box(0.5, 0.5, 0.5), M(i % 4 ? '#8d8a82' : '#8d6e63'), bx, 0.2, -12 + Math.random() * 22); o.scale.multiplyScalar(0.4 + Math.random() * 0.4); o.rotation.y = Math.random() * 3; scene.add(o); }
  }

  // ---------- PHỐ PHƯỜNG + ĐỒI THÔNG phía xa (instanced: rất nhẹ cho điện thoại) ----------
  function buildBackdrop() {
    var houses = [], rnd = function (a, b) { return a + Math.random() * (b - a); };
    // phố sau tường thành và hai góc trên
    for (var z = -17.5; z >= -34; z -= rnd(4.2, 5.5)) for (var x = MX - 62; x <= MX + 62; x += rnd(4.4, 6.2)) {
      if (Math.abs(x - MX) < 7 && z > -30) continue;              // chừa điện chính + bảo tháp
      if (Math.random() < 0.12) continue;
      houses.push({ x: x + rnd(-0.8, 0.8), z: z + rnd(-0.6, 0.6), w: rnd(2.6, 4.2), d: rnd(2.2, 3.2), h: rnd(1.1, 1.9), r: Math.random() < 0.5 ? 0 : Math.PI / 2, tier: Math.random() < 0.18 });
    }
    // hai bên ngoài cùng (trái/phải, phía trên bản đồ)
    for (var z2 = -15; z2 <= 6; z2 += rnd(4.5, 6)) for (var k = 0; k < 2; k++) { var sx = k ? LCX[1] + HL + rnd(25, 34) : -HL - rnd(25, 34); houses.push({ x: sx, z: z2, w: rnd(2.6, 3.8), d: rnd(2.2, 3), h: rnd(1.1, 1.7), r: Math.PI / 2, tier: false }); }
    var n = houses.length + houses.filter(function (h) { return h.tier; }).length;
    var wallI = new T.InstancedMesh(new T.BoxGeometry(1, 1, 1), new T.MeshLambertMaterial({ color: '#e6d6ba' }), houses.length);
    var colI = new T.InstancedMesh(new T.BoxGeometry(1, 1, 1), new T.MeshLambertMaterial({ color: '#8e1b14' }), houses.length);
    var roofI = new T.InstancedMesh(roofGeo(1, 0.75, 0.42, 0.22, 0.22), new T.MeshToonMaterial({ color: '#b52a1a', gradientMap: gradTex, map: roofTex, side: T.DoubleSide }), n);
    var winI = new T.InstancedMesh(new T.BoxGeometry(1, 1, 1), new T.MeshBasicMaterial({ color: '#ffc46a' }), houses.length);
    var m4 = new T.Matrix4(), q = new T.Quaternion(), ri = 0, col = new T.Color();
    houses.forEach(function (h, i) {
      q.setFromAxisAngle(new T.Vector3(0, 1, 0), h.r);
      m4.compose(new T.Vector3(h.x, h.h / 2, h.z), q, new T.Vector3(h.w, h.h, h.d)); wallI.setMatrixAt(i, m4);
      m4.compose(new T.Vector3(h.x, h.h + 0.06, h.z), q, new T.Vector3(h.w + 0.1, 0.14, h.d + 0.1)); colI.setMatrixAt(i, m4);
      var fwd = new T.Vector3(0, 0, h.d / 2 + 0.01).applyQuaternion(q);
      m4.compose(new T.Vector3(h.x + fwd.x, h.h * 0.5, h.z + fwd.z), q, new T.Vector3(h.w * 0.5, h.h * 0.32, 0.04)); winI.setMatrixAt(i, m4);
      m4.compose(new T.Vector3(h.x, h.h + 0.1, h.z), q, new T.Vector3(h.w * 1.15, h.w * 1.05, h.d * 1.45)); roofI.setMatrixAt(ri, m4); col.setHSL(0.01 + Math.random() * 0.02, 0.6, 0.38 + Math.random() * 0.12); roofI.setColorAt(ri++, col);
      if (h.tier) { m4.compose(new T.Vector3(h.x, h.h + h.w * 0.42, h.z), q, new T.Vector3(h.w * 0.75, h.w * 0.7, h.d * 0.95)); roofI.setMatrixAt(ri, m4); roofI.setColorAt(ri++, col); }
    });
    roofI.count = ri; [wallI, colI, roofI].forEach(function (o) { o.castShadow = true; o.receiveShadow = true; scene.add(o); }); scene.add(winI);
    // đồi xanh + rừng thông hai góc
    var hillM = new T.MeshLambertMaterial({ color: '#4d6b38' }), hillG = new T.SphereGeometry(1, 20, 12, 0, Math.PI * 2, 0, Math.PI / 2);
    var hills = [[MX - 58, -20, 16, 5], [MX - 44, -32, 14, 6], [MX + 58, -20, 16, 5], [MX + 44, -32, 14, 6], [MX - 66, -4, 12, 4], [MX + 66, -4, 12, 4], [MX, -44, 30, 7]];
    hills.forEach(function (hh) { var m = new T.Mesh(hillG, hillM); m.position.set(hh[0], -0.2, hh[1]); m.scale.set(hh[2], hh[3], hh[2] * 0.7); m.receiveShadow = true; scene.add(m); });
    var trees = [], cone = new T.ConeGeometry(0.7, 2.2, 7); cone.translate(0, 1.6, 0);
    var trunk = new T.CylinderGeometry(0.1, 0.14, 0.7, 5); trunk.translate(0, 0.35, 0);
    hills.forEach(function (hh) { for (var i = 0; i < 40; i++) { var a = Math.random() * 6.28, r = Math.sqrt(Math.random()) * hh[2] * 0.92; var tx = hh[0] + Math.cos(a) * r, tz = hh[1] + Math.sin(a) * r * 0.7; var k2 = 1 - (r / hh[2]) * (r / hh[2]); var ty = hh[3] * Math.sqrt(Math.max(0, k2)) - 0.3; trees.push([tx, ty, tz, 0.7 + Math.random() * 0.8]); } });
    var tI = new T.InstancedMesh(cone, new T.MeshLambertMaterial({ color: '#ffffff' }), trees.length), trI = new T.InstancedMesh(trunk, new T.MeshLambertMaterial({ color: '#4a3322' }), trees.length);
    trees.forEach(function (tr, i) { m4.compose(new T.Vector3(tr[0], tr[1], tr[2]), new T.Quaternion(), new T.Vector3(tr[3], tr[3], tr[3])); tI.setMatrixAt(i, m4); trI.setMatrixAt(i, m4); col.setHSL(0.3 + Math.random() * 0.05, 0.45, 0.2 + Math.random() * 0.12); tI.setColorAt(i, col); });
    tI.castShadow = true; scene.add(tI); scene.add(trI);
    // sương mù nhẹ giữa phố
    for (var f = 0; f < 8; f++) { var fg = new T.Sprite(new T.SpriteMaterial({ map: smokeTex, color: '#ffd6c0', transparent: true, opacity: 0.35, depthWrite: false })); fg.scale.set(22, 6, 1); fg.position.set(MX - 56 + f * 16, 2.5, -24 - (f % 2) * 6); scene.add(fg); }
  }

  // ---------- DÂN CHÚNG, LÍNH TUẦN, NGƯỜI BÁN HÀNG ----------
  var NPC = [];
  function spawnNPCs() {
    var L0 = -HL - 13, R0 = LCX[1] + HL + 13;
    var looks = [
      { skin: '#e8c39e', hair: '#1a1410', hat: 'nonla', robe: '#8d7b5a', robe2: '#4e4030', trim: '#c8b080' },
      { skin: '#f2d2b4', hair: '#120c0c', hat: 'longhair', robe: '#c2185b', robe2: '#f8bbd0', trim: '#ffd1e3', female: true },
      { skin: '#e3b48c', hair: '#2a1a10', hat: 'topknot', robe: '#3e5f8a', robe2: '#c5d6ea', trim: '#e0e8f0' },
      { skin: '#f3d0b0', hair: '#1c1416', hat: 'longhair', robe: '#2e7d5b', robe2: '#c8e6c9', trim: '#e8f5e9', female: true },
      { skin: '#d9a77c', hair: '#2a1a10', hat: 'nonla', robe: '#6d4c41', robe2: '#3e2723', trim: '#a1887f' },
      { skin: '#eec39e', hair: '#cfc8c0', hat: 'topknot', robe: '#5d4037', robe2: '#d7ccc8', trim: '#e0c080' }
    ];
    var guard = { skin: '#e0b48c', hair: '#111', hat: 'helmet', robe: '#a3241a', robe2: '#3a0a06', trim: '#e8b04a', armor: true };
    function add(lk, weapon, path, speed, scale, y) {
      var v = makeHuman(lk, { weapon: weapon }); v.scale.setScalar(scale || 1.05); scene.add(v);
      var n = { v: v, path: path, i: 0, p: path[0].clone(), sp: speed, wait: Math.random() * 2, y: y || 0, ph: Math.random() * 6 };
      v.position.copy(n.p); NPC.push(n);
    }
    var P = function (x, z) { return new T.Vector3(x, 0, z); };
    for (var i = 0; i < 6; i++) {
      add(looks[i], null, [P(L0 + 0.3, -10 + i * 3), P(L0 + 0.3, 9 - i), P(L0 - 2.4, 9 - i), P(L0 - 2.4, -10 + i * 3)], 0.9 + Math.random() * 0.5);
      add(looks[(i + 3) % 6], null, [P(R0 - 0.3, 9 - i * 3), P(R0 - 0.3, -10 + i), P(R0 + 2.4, -10 + i), P(R0 + 2.4, 9 - i * 3)], 0.9 + Math.random() * 0.5);
    }
    [[-1, -8], [1, -3.5], [-1, 1], [1, 5.5]].forEach(function (p, k) { add(looks[(k * 2) % 6], null, [P(L0 + p[0] * 1.5 - 0.8, p[1]), P(L0 + p[0] * 1.5 - 0.8, p[1] + 0.01)], 0.01); add(looks[(k * 2 + 1) % 6], null, [P(R0 - p[0] * 1.5 + 0.8, p[1] + 1), P(R0 - p[0] * 1.5 + 0.8, p[1] + 1.01)], 0.01); });
    for (var g = 0; g < 4; g++) { var x0 = MX - 40 + g * 22; add(guard, 'spear', [P(x0, -13.4), P(x0 + 14, -13.4)], 1.1, 1.1, 3.2); }
    add(guard, 'spear', [P(-HL - 10, 11.3), P(-HL - 2, 11.3)], 0.8, 1.1, 0.2); add(guard, 'spear', [P(LCX[1] + HL + 2, 11.3), P(LCX[1] + HL + 10, 11.3)], 0.8, 1.1, 0.2);
  }
  function stepNPCs(dt) {
    NPC.forEach(function (n) {
      var v = n.v, tgt = n.path[(n.i + 1) % n.path.length], moving = false;
      if (n.wait > 0) n.wait -= dt;
      else {
        var d = _tmpV3.subVectors(tgt, n.p), L = d.length();
        if (L < 0.1) { n.i = (n.i + 1) % n.path.length; n.wait = n.sp < 0.05 ? 99 : Math.random() < 0.3 ? 1 + Math.random() * 2 : 0; }
        else { d.multiplyScalar(Math.min(L, n.sp * dt) / L); n.p.add(d); moving = n.sp > 0.05; faceTo(v, 1, Math.atan2(d.x, d.z), dt); }
      }
      v.position.set(n.p.x, n.y, n.p.z);
      n.ph += dt * 0.7; animHuman(v, { moving: moving, atk: 0, ph: n.ph }, clock * 0.75 + n.ph, dt);
    });
  }
  var _tmpV3 = new T.Vector3();

  // ---------- HIỆU ỨNG MÔI TRƯỜNG ----------
  var flies = null, embers = [], rays = [];
  function buildAmbient() {
    var n = 90, geo = new T.BufferGeometry(), pos = new Float32Array(n * 3), ph = [];
    for (var i = 0; i < n; i++) { pos[i * 3] = MX - 25 + Math.random() * 50; pos[i * 3 + 1] = 0.4 + Math.random() * 2.2; pos[i * 3 + 2] = -10 + Math.random() * 26; ph.push(Math.random() * 6.28); }
    geo.setAttribute('position', new T.BufferAttribute(pos, 3));
    flies = new T.Points(geo, new T.PointsMaterial({ color: '#d4ff7a', size: 0.32, map: glowTex, transparent: true, blending: T.AdditiveBlending, depthWrite: false }));
    flies.userData.ph = ph; scene.add(flies);
    // tia nắng hoàng hôn
    var rayTex = canvasTex(64, 256, function (g, w, h) { var gr = g.createLinearGradient(0, 0, 0, h); gr.addColorStop(0, 'rgba(255,210,150,0)'); gr.addColorStop(0.3, 'rgba(255,200,140,0.5)'); gr.addColorStop(1, 'rgba(255,190,120,0)'); g.fillStyle = gr; g.fillRect(0, 0, w, h); var gx = g.createLinearGradient(0, 0, w, 0); gx.addColorStop(0, 'rgba(0,0,0,1)'); gx.addColorStop(0.5, 'rgba(0,0,0,0)'); gx.addColorStop(1, 'rgba(0,0,0,1)'); g.globalCompositeOperation = 'destination-out'; g.fillStyle = gx; g.fillRect(0, 0, w, h); });
    for (var r = 0; r < 6; r++) { var m = new T.Mesh(new T.PlaneGeometry(3 + Math.random() * 3, 40), new T.MeshBasicMaterial({ map: rayTex, transparent: true, opacity: 0.12, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide })); m.position.set(MX - 26 + r * 10, 12, -16 + r * 2); m.rotation.set(0.15, 0.4, -0.65); scene.add(m); rays.push(m); }
  }
  function stepAmbient(dt, t) {
    if (!flies) return;
    var p = flies.geometry.attributes.position, ph = flies.userData.ph;
    for (var i = 0; i < p.count; i++) { p.setX(i, p.getX(i) + Math.sin(t * 0.7 + ph[i]) * dt * 0.5); p.setY(i, 0.4 + 1.2 + Math.sin(t * 0.9 + ph[i] * 2) * 1.0); p.setZ(i, p.getZ(i) + Math.cos(t * 0.6 + ph[i]) * dt * 0.5); }
    p.needsUpdate = true; flies.material.opacity = 0.6 + Math.sin(t * 3) * 0.3;
    rays.forEach(function (r, i) { r.material.opacity = 0.08 + Math.sin(t * 0.4 + i) * 0.05; });
    // tàn lửa bay lên từ đèn lồng
    if (Math.random() < 0.35) { var L = LANT[(Math.random() * LANT.length) | 0]; if (L) { var wp2 = new T.Vector3(); L.getWorldPosition(wp2); var e = glowSprite('#ffab40', 0.12, 1); e.position.copy(wp2); addFX({ obj: e, t: 0, life: 1.6, vx: (Math.random() - 0.5) * 0.4, up: function (f, d, k) { f.obj.position.y += d * 0.8; f.obj.position.x += f.vx * d; f.obj.material.opacity = 1 - k; } }); } }
  }
  function dustAt(p, col) { var sp = new T.Sprite(spriteMat(col || '#d7c4a8', 0.5, smokeTex)); sp.position.copy(p).setY(0.15); sp.scale.set(0.4, 0.4, 1); sp.material = sp.material.clone(); sp.material.blending = T.NormalBlending; addFX({ obj: sp, t: 0, life: 0.7, up: function (f, d, k) { var s3 = 0.4 + k * 0.9; f.obj.scale.set(s3, s3 * 0.7, 1); f.obj.position.y += d * 0.3; f.obj.material.opacity = 0.5 * (1 - k); }, dispose: true }); }
  function portalBurst(lane) {
    var p = W(lane, HL, -0.6);
    ringFX(p, '#c64dff', 0.5, 3.2, 0.6); pillar(p, '#b03cff', 5, 0.5, 1.2); burst(p.clone().setY(0.6), '#e040fb', 14, 3, 0.25, 0.6, 2);
    boltLine([W(lane, HL - 1.5, -0.6, 4), W(lane, HL - 0.5, -0.8, 2), W(lane, HL, -0.6, 0.1)], '#ea80fc', 0.25, 0.04);
  }

  function gateFort(lane) {
    var cx = LCX[lane], z = -10.6, grp = new T.Group(); grp.position.set(cx, 0, z); grp.scale.x = LW / 9;
    var wallM = M('#9a8c78');
    var wl = mesh(new T.BoxGeometry(3.6, 2.6, 1.6), wallMat(3.6, 2.6, '#f0e0c8'), -3.3, 1.3, 0); wl.receiveShadow = true; grp.add(wl);
    var wr = mesh(new T.BoxGeometry(3.6, 2.6, 1.6), wallMat(3.6, 2.6, '#f0e0c8'), 3.3, 1.3, 0); wr.receiveShadow = true; grp.add(wr);
    var top = mesh(new T.BoxGeometry(10.4, 0.9, 1.6), wallMat(10.4, 0.9, '#f0e0c8'), 0, 2.15, 0); grp.add(top);
    var arch = mesh(new T.BoxGeometry(3, 1.75, 1.7), M('#2a0d08'), 0, 0.85, 0.02, false); grp.add(arch);
    var doorL = mesh(new T.BoxGeometry(1.45, 1.7, 0.12), M('#7a1a10'), -0.73, 0.85, 0.75); grp.add(doorL);
    var doorR = mesh(new T.BoxGeometry(1.45, 1.7, 0.12), M('#7a1a10'), 0.73, 0.85, 0.75); grp.add(doorR);
    for (var i = 0; i < 3; i++) for (var j = 0; j < 3; j++) { grp.add(mesh(G('stud', function () { return new T.SphereGeometry(0.06, 6, 4); }), M('#e8b04a'), -1.2 + i * 0.25 + (j > 1 ? 0 : 0), 0.4 + j * 0.45, 0.82, false)); grp.add(mesh(G('stud', null), M('#e8b04a'), 0.7 + i * 0.25, 0.4 + j * 0.45, 0.82, false)); }
    var crm2 = wallMat(0.55, 0.4, '#f0e0c8'); for (var k = 0; k < 11; k++) grp.add(mesh(G('cren', function () { return new T.BoxGeometry(0.55, 0.4, 0.3); }), crm2, -5 + k * 1, 2.8, 0.65));
    // lầu trên cổng 2 tầng
    var tower = hall(0, 0, 5.4, 1.6, 1.1, 1.2, { tiers: 2, wall: '#e6d4b4' }); scene.remove(tower); tower.position.set(0, 2.6, -0.1); grp.add(tower);
    // biển
    var pc = document.createElement('canvas'); pc.width = 512; pc.height = 200; var plaque = new T.CanvasTexture(pc); plaque.anisotropy = 8;
    var drawPlaque = function () {
      var g = pc.getContext('2d'), W2 = 512, H2 = 200; g.clearRect(0, 0, W2, H2);
      // khung gỗ chạm, viền vàng, nền sơn mài xanh thẫm
      var fr = g.createLinearGradient(0, 0, 0, H2); fr.addColorStop(0, '#7a1a10'); fr.addColorStop(1, '#3a0a06'); g.fillStyle = fr; g.fillRect(0, 0, W2, H2);
      g.strokeStyle = '#e8b04a'; g.lineWidth = 6; g.strokeRect(10, 10, W2 - 20, H2 - 20); g.lineWidth = 2; g.strokeRect(22, 22, W2 - 44, H2 - 44);
      var bgc = g.createLinearGradient(0, 30, 0, H2 - 30); bgc.addColorStop(0, '#16285a'); bgc.addColorStop(1, '#0b1636'); g.fillStyle = bgc; g.fillRect(26, 26, W2 - 52, H2 - 52);
      for (var c = 0; c < 4; c++) { var cx = c % 2 ? W2 - 26 : 26, cy = c > 1 ? H2 - 26 : 26; g.fillStyle = '#e8b04a'; g.beginPath(); g.arc(cx, cy, 12, 0, 6.3); g.fill(); g.fillStyle = '#7a1a10'; g.beginPath(); g.arc(cx, cy, 5, 0, 6.3); g.fill(); }
      var vi = lane === 0 ? 'Lạc Dương' : 'Biện Kinh';
      var gold = g.createLinearGradient(0, 40, 0, 150); gold.addColorStop(0, '#fff4c2'); gold.addColorStop(0.5, '#ffd257'); gold.addColorStop(1, '#c07a10');
      g.textAlign = 'center'; g.textBaseline = 'middle';
      g.font = 'italic 900 96px "Playfair Display", serif';
      g.lineWidth = 8; g.strokeStyle = '#3a1a00'; g.strokeText(vi, W2 / 2, 104);
      g.shadowColor = 'rgba(255,200,90,.55)'; g.shadowBlur = 14; g.fillStyle = gold; g.fillText(vi, W2 / 2, 104); g.shadowBlur = 0;
      g.strokeStyle = 'rgba(255,255,255,.35)'; g.lineWidth = 1.5; g.strokeText(vi, W2 / 2, 100);
      g.fillStyle = '#b71c1c'; g.fillRect(W2 - 92, H2 - 82, 44, 44); g.fillStyle = '#ffd0c0'; g.font = '700 15px "Playfair Display", serif'; g.fillText('THÀNH', W2 - 70, H2 - 60);
      plaque.needsUpdate = true;
    };
    drawPlaque(); if (document.fonts && document.fonts.load) document.fonts.load('italic 900 96px "Playfair Display"', 'Lạc Dương Biện Kinh').then(drawPlaque).catch(function () {});
    var pl = mesh(new T.PlaneGeometry(3.6, 1.4), new T.MeshBasicMaterial({ map: plaque }), 0, 2.2, 0.83, false); pl.scale.x = 9 / LW; grp.add(pl);
    var plGlow = glowSprite('#ffcf7a', 3.6, 0.25); plGlow.position.set(0, 2.2, 0.9); grp.add(plGlow);
    // cờ
    for (var s = -1; s <= 1; s += 2) {
      var pole = mesh(G('pole', function () { return new T.CylinderGeometry(0.04, 0.04, 2.4, 5); }), M('#3a2a1a'), s * 5, 4.1, 0.5); grp.add(pole);
      var flag = mesh(G('flag', function () { return new T.PlaneGeometry(1.1, 0.7, 8, 1); }), M(lane === 0 ? '#2f6fd0' : '#c62828', { side: T.DoubleSide }), s * 5 + 0.55, 4.9, 0.5); grp.add(flag); FLAGS.push(flag);
    }
    // ngọn lửa trên tường
    for (var f = -1; f <= 1; f += 2) { var br = glowSprite('#ff8a3a', 1.6, 0.7); br.position.set(f * 2, 2.1, 0.95); grp.add(br); LANT.push(br); }
    scene.add(grp);
    var flash = new T.Mesh(new T.BoxGeometry(10.6, 3.2, 1.8), new T.MeshBasicMaterial({ color: '#ff2a1a', transparent: true, opacity: 0, blending: T.AdditiveBlending, depthWrite: false }));
    flash.position.set(0, 1.5, 0); grp.add(flash);
    return { g: grp, flash: flash, shake: 0 };
  }
  var FLAGS = [];

  // ---------- NHÂN VẬT 3D (chibi) ----------
  function sph(r, ws, hs) { return G('s' + r + '_' + (ws || 12), function () { return new T.SphereGeometry(r, ws || 12, hs || 10); }); }
  function cyl(rt, rb, h, s) { return G('c' + rt + '_' + rb + '_' + h, function () { var g = new T.CylinderGeometry(rt, rb, h, s || 10); return g; }); }
  function cone(r, h, s) { return G('k' + r + '_' + h + '_' + (s || 8), function () { return new T.ConeGeometry(r, h, s || 8); }); }
  function box(x, y, z) { return G('b' + x + '_' + y + '_' + z, function () { return new T.BoxGeometry(x, y, z); }); }
  function limb(len, r, mat) { var p = new T.Group(); var m = mesh(cyl(r, r * 0.9, len, 7), mat, 0, -len / 2, 0); p.add(m); p.userData.m = m; return p; }

  // Người tỉ lệ thật (~1.75), chi tiết kiểu tướng Kiếm Thế: váy áo nhiều lớp, giáp vai, tay áo loe, đai lưng, ủng
  function lathe(key, pts, seg) { return G(key, function () { return new T.LatheGeometry(pts.map(function (p) { return new T.Vector2(p[0], p[1]); }), seg || 14); }); }
  function makeHuman(lk, o) {
    o = o || {};
    var root = new T.Group(), body = new T.Group(); root.add(body);
    var robe = M(lk.robe), robe2 = M(lk.robe2), skin = M(lk.skin), trim = M(lk.trim), dark = M(shade(lk.robe2, -0.45)), boot = M('#2a1a12');
    var fem = !!lk.female;
    // chân + ủng
    function leg() { var p = new T.Group(); p.add(mesh(cyl(0.07, 0.06, 0.62, 8), dark, 0, -0.31, 0)); var b = mesh(box(0.12, 0.12, 0.2), boot, 0, -0.62, 0.04); p.add(b); return p; }
    var legL = leg(), legR = leg(); legL.position.set(-0.1, 0.7, 0); legR.position.set(0.1, 0.7, 0); body.add(legL, legR);
    // váy áo dưới (vạt dài, loe)
    var skirt = mesh(lathe(fem ? 'skirtF' : 'skirtM', fem ? [[0.0, 0.0], [0.38, 0.0], [0.33, 0.25], [0.24, 0.55], [0.19, 0.72], [0, 0.72]] : [[0, 0.25], [0.3, 0.25], [0.27, 0.45], [0.21, 0.72], [0, 0.72]], 16), robe, 0, 0.26, 0);
    skirt.scale.z = 0.85; outline(skirt, 1.04); body.add(skirt);
    var skirtTrim = mesh(G(fem ? 'strimF' : 'strimM', function () { var t = new T.TorusGeometry(fem ? 0.37 : 0.29, 0.02, 4, 20); t.rotateX(Math.PI / 2); return t; }), trim, 0, fem ? 0.27 : 0.52, 0, false); skirtTrim.scale.z = 0.85; body.add(skirtTrim);
    var front = mesh(box(0.12, fem ? 0.68 : 0.46, 0.02), robe2, 0, fem ? 0.6 : 0.73, fem ? 0.27 : 0.24, false); front.rotation.x = fem ? -0.2 : -0.16; body.add(front);
    // thân trên
    var torso = mesh(lathe('torso', [[0, 0], [0.19, 0], [0.21, 0.12], [0.23, 0.3], [0.2, 0.42], [0.09, 0.48], [0, 0.48]], 14), robe, 0, 0.96, 0); torso.scale.z = 0.72; outline(torso, 1.05); body.add(torso);
    var lapel = mesh(box(0.05, 0.36, 0.02), trim, 0.05, 1.22, 0.15, false); lapel.rotation.z = 0.35; lapel.rotation.x = -0.1; body.add(lapel);
    var lapel2 = mesh(box(0.05, 0.36, 0.02), trim, -0.05, 1.22, 0.15, false); lapel2.rotation.z = -0.35; lapel2.rotation.x = -0.1; body.add(lapel2);
    var belt = mesh(cyl(0.205, 0.205, 0.08, 14), M(lk.sash || lk.trim), 0, 0.98, 0); belt.scale.z = 0.75; body.add(belt);
    body.add(mesh(box(0.08, 0.07, 0.03), M('#e8b04a', { em: '#8a5a00', ei: 0.4 }), 0, 0.98, 0.16, false));
    var sash = mesh(box(0.07, 0.3, 0.02), M(lk.sash || lk.trim), 0.08, 0.82, 0.17, false); sash.rotation.z = 0.12; body.add(sash);
    // giáp vai
    var heavy = lk.armor || o.pads;
    for (var sd = -1; sd <= 1; sd += 2) {
      var pad = mesh(G(heavy ? 'padH' : 'padL', function () { var g = new T.SphereGeometry(heavy ? 0.13 : 0.095, 10, 6, 0, Math.PI * 2, 0, Math.PI * 0.55); g.scale(1.1, 0.75, 1); return g; }), heavy ? M(lk.trim, { em: shade(lk.trim, -0.6), ei: 0.2 }) : robe, sd * 0.23, 1.37, 0);
      pad.rotation.z = -sd * 0.35; body.add(pad);
    }
    if (lk.armor) { var cp = mesh(cyl(0.215, 0.2, 0.26, 12), M(lk.trim, { em: shade(lk.trim, -0.7), ei: 0.2 }), 0, 1.12, 0.01); cp.scale.z = 0.76; body.add(cp); for (var r = 0; r < 3; r++) { var band = mesh(box(0.34, 0.025, 0.02), M(shade(lk.trim, -0.35)), 0, 1.04 + r * 0.08, 0.165, false); body.add(band); } }
    // cổ + đầu (dùng khối đầu chi tiết rồi thu nhỏ)
    body.add(mesh(cyl(0.055, 0.065, 0.1, 8), skin, 0, 1.47, 0));
    var head = new T.Group(); head.position.y = 1.62; head.scale.setScalar(0.6); body.add(head);
    var hg = G('headR', function () { var g = new T.SphereGeometry(0.23, 18, 14); g.scale(0.92, 1.08, 0.98); return g; });
    var hm = mesh(hg, skin, 0, 0, 0); outline(hm, 1.05); head.add(hm);
    head.add(mesh(G('jaw', function () { var g = new T.SphereGeometry(0.16, 12, 8); g.scale(1, 0.8, 1); return g; }), skin, 0, -0.1, 0.04));
    var eyeG = G('eyeR', function () { var g = new T.SphereGeometry(0.028, 8, 6); g.scale(1.5, 0.75, 0.5); return g; }), eyeM = M('#120a08');
    head.add(mesh(eyeG, eyeM, -0.075, 0.02, 0.205, false), mesh(eyeG, eyeM, 0.075, 0.02, 0.205, false));
    var brow = M(lk.hair || '#2a1a12');
    var b1 = mesh(box(0.08, 0.016, 0.02), brow, -0.08, 0.075, 0.2, false), b2 = mesh(box(0.08, 0.016, 0.02), brow, 0.08, 0.075, 0.2, false);
    b1.rotation.z = fem ? 0.08 : -0.15; b2.rotation.z = fem ? -0.08 : 0.15; head.add(b1, b2);
    head.add(mesh(box(0.05, 0.012, 0.02), M(fem ? '#c2185b' : '#8d4a3a'), 0, -0.11, 0.19, false));
    if (fem) { var bl = M('#ff8a80', { op: 0.45 }); head.add(mesh(sph(0.035, 6, 4), bl, -0.12, -0.04, 0.17, false)); head.add(mesh(sph(0.035, 6, 4), bl, 0.12, -0.04, 0.17, false)); }
    if (!fem && (lk.hat === 'topknot' || lk.hat === 'taoist' || lk.hat === 'messy' || lk.hat === 'helmet' || lk.hat === 'plume' || lk.hat === 'horns')) { var bd = mesh(G('beard', function () { var g = new T.ConeGeometry(0.07, 0.2, 6); g.rotateX(Math.PI); return g; }), M(lk.hair || '#222'), 0, -0.24, 0.12, false); bd.rotation.x = -0.35; head.add(bd); }
    hat3(head, lk, o);
    if (lk.mask) { var mk = mesh(box(0.36, 0.12, 0.1), M(shade(lk.robe, -0.3)), 0, -0.09, 0.15, false); head.add(mk); }
    // tay + tay áo loe
    function arm() {
      var p = new T.Group();
      p.add(mesh(cyl(0.058, 0.05, 0.5, 8), robe, 0, -0.25, 0));
      var sl = mesh(G('sleeve', function () { var g = new T.CylinderGeometry(0.07, 0.13, 0.24, 10, 1, true); return g; }), M(lk.robe, { side: T.DoubleSide }), 0, -0.44, 0); p.add(sl);
      p.add(mesh(G('cuff', function () { var t = new T.TorusGeometry(0.125, 0.016, 4, 12); t.rotateX(Math.PI / 2); return t; }), trim, 0, -0.56, 0, false));
      p.add(mesh(sph(0.055, 8, 6), skin, 0, -0.58, 0));
      return p;
    }
    var armL = arm(), armR = arm();
    armL.position.set(-0.27, 1.36, 0); armR.position.set(0.27, 1.36, 0); body.add(armL, armR);
    var wp = new T.Group(); wp.position.set(0, -0.6, 0); wp.scale.setScalar(1.45); armR.add(wp); weapon3(wp, o.weapon || lk.weapon, o);
    if (o.weapon === 'twin') { var wp2 = new T.Group(); wp2.position.set(0, -0.6, 0); wp2.scale.setScalar(1.45); armL.add(wp2); weapon3(wp2, 'sword', o); }
    armL.rotation.z = 0.16; armR.rotation.z = -0.16;
    if (o.cape) { var cpe = mesh(G('capeR', function () { var g = new T.PlaneGeometry(0.56, 1.25, 4, 8); g.translate(0, -0.62, 0); return g; }), M(o.cape, { side: T.DoubleSide }), 0, 1.42, -0.17); cpe.rotation.x = 0.12; body.add(cpe); root.userData.cape = cpe; }
    if (lk.patches) { body.add(mesh(box(0.1, 0.1, 0.02), M('#5d4037'), -0.12, 0.72, 0.25, false)); body.add(mesh(box(0.08, 0.1, 0.02), M('#827717'), 0.12, 1.15, 0.16, false)); }
    root.userData = Object.assign(root.userData, { body: body, head: head, armL: armL, armR: armR, legL: legL, legR: legR, tall: true });
    return root;
  }
  function hat3(head, lk, o) {
    var hair = M(lk.hair || '#222');
    var cap = function (r) { var m = mesh(G('cap' + r, function () { return new T.SphereGeometry(r, 16, 10, 0, Math.PI * 2, 0, Math.PI * 0.55); }), hair, 0, 0.02, -0.01); return m; };
    switch (lk.hat) {
      case 'bald': head.add(mesh(sph(0.018, 5, 4), M('#7a4a2a'), -0.06, 0.2, 0.08, false)); head.add(mesh(sph(0.018, 5, 4), M('#7a4a2a'), 0, 0.22, 0.09, false)); head.add(mesh(sph(0.018, 5, 4), M('#7a4a2a'), 0.06, 0.2, 0.08, false)); break;
      case 'helmet': head.add(mesh(G('helm', function () { return new T.SphereGeometry(0.26, 16, 10, 0, Math.PI * 2, 0, Math.PI * 0.5); }), M('#d4a017', { em: '#6a4a00', ei: 0.3 }), 0, 0.03, 0)); var pl = mesh(cone(0.06, 0.3), M('#d32f2f'), 0, 0.33, 0); head.add(pl); break;
      case 'hood': var hd = mesh(G('hood', function () { return new T.SphereGeometry(0.27, 16, 12, 0, Math.PI * 2, 0, Math.PI * 0.62); }), M(shade(lk.robe, -0.35)), 0, 0.0, -0.02); hd.rotation.x = -0.3; head.add(hd); break;
      case 'headdress': head.add(cap(0.245)); for (var i = -2; i <= 2; i++) { var sp = mesh(cone(0.04, 0.26), M('#cfd8dc'), i * 0.07, 0.3 - Math.abs(i) * 0.04, 0.05); sp.rotation.z = -i * 0.25; head.add(sp); } head.add(mesh(sph(0.04), M(lk.trim, { em: lk.trim, ei: 0.8 }), 0, 0.22, 0.17)); break;
      case 'longhair': case 'crown':
        head.add(cap(0.25));
        var back = mesh(G('lhair', function () { var g = new T.CylinderGeometry(0.17, 0.12, 0.62, 10, 1, true); g.translate(0, -0.3, 0); return g; }), M(lk.hair, { side: T.DoubleSide }), 0, 0.02, -0.12); back.rotation.x = 0.2; head.add(back); head.userData.hair = back;
        head.add(mesh(sph(0.11), hair, 0, 0.24, -0.06));
        if (lk.hat === 'crown') { for (var c = -1; c <= 1; c++) head.add(mesh(cone(0.035, 0.16, 5), M('#ffd56a', { em: '#ffb300', ei: 0.7 }), c * 0.07, 0.36 - Math.abs(c) * 0.03, 0.02)); head.add(mesh(sph(0.03), M('#7ec8ff', { em: '#7ec8ff', ei: 1.5 }), 0, 0.3, 0.1)); }
        else head.add(mesh(sph(0.05), M('#ffd1e3', { em: '#ff80ab', ei: 0.6 }), 0.1, 0.24, 0.02));
        break;
      case 'topknot': head.add(cap(0.245)); head.add(mesh(sph(0.09), hair, 0, 0.3, -0.02)); head.add(mesh(box(0.03, 0.14, 0.03), M('#e8b04a'), 0, 0.33, 0.02)); break;
      case 'taoist': head.add(cap(0.245)); head.add(mesh(box(0.3, 0.13, 0.22), M('#263238'), 0, 0.27, -0.02)); head.add(mesh(box(0.31, 0.03, 0.23), M(lk.trim, { em: lk.trim, ei: 0.4 }), 0, 0.24, -0.02, false)); break;
      case 'messy': head.add(cap(0.25)); for (var j = 0; j < 6; j++) head.add(mesh(sph(0.08, 6, 5), hair, Math.cos(j) * 0.15, 0.2 + (j % 2) * 0.05, Math.sin(j) * 0.12 - 0.04)); head.add(mesh(G('band', function () { return new T.TorusGeometry(0.235, 0.025, 6, 16); }), M('#7cb342'), 0, 0.1, 0, false)).rotation.x = Math.PI / 2; break;
      case 'yellowband': head.add(cap(0.245)); var yb = mesh(G('band3', function () { return new T.TorusGeometry(0.24, 0.045, 6, 16); }), M('#f2c400', { em: '#806000', ei: 0.3 }), 0, 0.09, 0, false); yb.rotation.x = Math.PI / 2; head.add(yb); var tl = mesh(box(0.06, 0.3, 0.02), M('#f2c400'), -0.05, -0.05, -0.25, false); tl.rotation.x = 0.4; head.add(tl); break;
      case 'mongol': head.add(cap(0.245)); head.add(mesh(G('furhat', function () { var g = new T.CylinderGeometry(0.3, 0.28, 0.16, 12); return g; }), M('#6d4c2e'), 0, 0.14, 0)); head.add(mesh(cone(0.2, 0.32, 10), M('#8b1a10'), 0, 0.36, 0)); head.add(mesh(sph(0.04), M('#e8b04a', { em: '#a06a10', ei: 0.5 }), 0, 0.54, 0, false)); break;
      case 'nonla': head.add(cap(0.245)); head.add(mesh(G('nonla', function () { return new T.ConeGeometry(0.55, 0.32, 18, 1, true); }), M('#e8d39a', { side: T.DoubleSide }), 0, 0.3, 0)); break;
      case 'bandana': head.add(cap(0.245)); var bd = mesh(G('band2', function () { return new T.TorusGeometry(0.235, 0.035, 6, 16); }), M(lk.trim), 0, 0.09, 0, false); bd.rotation.x = Math.PI / 2; head.add(bd); break;
      case 'ironhelm': head.add(mesh(G('helm', null), M('#78909c'), 0, 0.03, 0)); head.add(mesh(box(0.04, 0.2, 0.04), M('#455a64'), 0, 0.3, 0)); break;
      case 'horns': head.add(cap(0.25)); for (var s = -1; s <= 1; s += 2) { var hn = mesh(cone(0.05, 0.3, 6), M('#e8dcc8'), s * 0.15, 0.24, 0); hn.rotation.z = -s * 0.6; head.add(hn); } break;
      case 'plume': head.add(mesh(G('helm', null), M('#e0b020', { em: '#7a5200', ei: 0.4 }), 0, 0.03, 0)); var pm = mesh(G('plumeg', function () { var g = new T.SphereGeometry(0.09, 8, 6); g.scale(0.6, 0.6, 2.4); return g; }), M('#e53935'), 0, 0.33, -0.12); pm.rotation.x = 0.5; head.add(pm); head.userData.hair = pm; break;
      case 'ponytail': head.add(cap(0.25)); var pt = mesh(G('pony', function () { var g = new T.CylinderGeometry(0.07, 0.03, 0.55, 8); g.translate(0, -0.27, 0); return g; }), hair, 0, 0.2, -0.18); pt.rotation.x = 0.8; head.add(pt); head.userData.hair = pt; head.add(mesh(sph(0.045), M('#ff1744'), 0, 0.22, -0.18)); break;
    }
  }
  function weapon3(g, w, o) {
    var glw = o.wglow;
    switch (w) {
      case 'sword': case 'saber':
        g.add(mesh(box(0.14, 0.03, 0.04), M('#e8b04a'), 0, 0, 0));
        var bl = mesh(box(0.045, 0.62, 0.015), M(w === 'saber' ? '#cfd8dc' : '#eef6ff', { em: glw || (w === 'sword' ? '#7ab8ff' : '#000000'), ei: glw ? 1.4 : 0.35 }), 0, -0.32, 0); g.add(bl);
        break;
      case 'staff': g.add(mesh(cyl(0.025, 0.025, 1.1, 6), M('#8d5a2b'), 0, -0.2, 0)); g.add(mesh(sph(0.05), M('#e8b04a'), 0, 0.35, 0)); g.add(mesh(sph(0.05), M('#e8b04a'), 0, -0.75, 0)); break;
      case 'stick': g.add(mesh(cyl(0.028, 0.028, 1.0, 6), M('#7cb342'), 0, -0.15, 0)); break;
      case 'hammer': g.add(mesh(cyl(0.025, 0.025, 0.65, 6), M('#6d4c41'), 0, -0.25, 0)); var hh = mesh(cyl(0.13, 0.13, 0.22, 10), M('#d4a017', { em: '#6a4a00', ei: 0.4 }), 0, -0.58, 0); hh.rotation.z = Math.PI / 2; g.add(hh); break;
      case 'dart': for (var i = -1; i <= 1; i++) { var d = mesh(cone(0.015, 0.16, 4), M('#eceff1', { em: '#76ff03', ei: 0.4 }), i * 0.04, -0.06, 0.04); d.rotation.x = Math.PI; g.add(d); } break;
      case 'claw': for (var j = -1; j <= 1; j++) { var c = mesh(cone(0.015, 0.16, 4), M('#b3ff6a', { em: '#76ff03', ei: 1.2 }), j * 0.03, -0.08, 0.03); c.rotation.x = Math.PI + 0.4; g.add(c); } break;
      case 'fan': var fn = mesh(G('fan', function () { return new T.CircleGeometry(0.26, 12, 0, Math.PI * 0.75); }), M('#ffd1e3', { side: T.DoubleSide, em: '#ff80ab', ei: 0.3 }), 0, -0.05, 0.02); fn.rotation.z = -Math.PI * 0.9; g.add(fn); break;
      case 'talisman': g.add(mesh(box(0.1, 0.2, 0.01), M('#ffeb3b', { em: '#ffeb3b', ei: 0.6 }), 0, -0.1, 0.04)); g.add(glowSprite('#18ffff', 0.35, 0.8)); break;
      case 'bow': var bw = mesh(G('bow', function () { return new T.TorusGeometry(0.3, 0.018, 4, 12, Math.PI * 0.9); }), M('#6d4c41'), 0, -0.05, 0); bw.rotation.z = Math.PI * 0.55; g.add(bw); break;
      case 'axe': g.add(mesh(cyl(0.03, 0.03, 0.9, 6), M('#4e342e'), 0, -0.3, 0)); var ax = mesh(box(0.28, 0.24, 0.03), M('#90a4ae'), 0.12, -0.65, 0); g.add(ax); break;
      case 'shield': var sh = mesh(cyl(0.2, 0.2, 0.05, 12), M('#546e7a'), -0.02, -0.05, 0.12); sh.rotation.x = Math.PI / 2; g.add(sh); g.add(mesh(sph(0.05), M('#b0bec5'), -0.02, -0.05, 0.16)); break;
      case 'spear': g.add(mesh(cyl(0.022, 0.022, 1.4, 6), M('#6d4c41'), 0, -0.3, 0)); var tip = mesh(cone(0.05, 0.22, 6), M('#eceff1', { em: '#ffd740', ei: 0.6 }), 0, -1.1, 0); tip.rotation.x = Math.PI; g.add(tip); g.add(mesh(cone(0.07, 0.1, 6), M('#e53935'), 0, -0.95, 0)); break;
      case 'twin': weapon3(g, 'sword', o); break;
    }
  }
  function makeBeast(type) {
    var d = S.CREEPS[type], col = d.col, root = new T.Group(), body = new T.Group(); root.add(body);
    var bm = M(col), dk = M(shade(col, -0.4));
    var tor = mesh(G('btor', function () { var g = new T.SphereGeometry(0.3, 14, 10); g.scale(0.75, 0.7, 1.35); return g; }), type === 'hovuong' ? M('#ffffff', { map: tigerTex() }) : bm, 0, 0.42, 0); outline(tor, 1.06); body.add(tor);
    var head = new T.Group(); head.position.set(0, 0.6, 0.45); body.add(head);
    var hm = mesh(sph(0.2, 12, 10), bm, 0, 0, 0); outline(hm, 1.07); head.add(hm);
    head.add(mesh(G('snout', function () { var g = new T.ConeGeometry(0.1, 0.24, 8); g.rotateX(Math.PI / 2); return g; }), M(shade(col, 0.2)), 0, -0.05, 0.2));
    head.add(mesh(sph(0.03, 6, 4), M('#111'), 0, -0.03, 0.33, false));
    for (var s = -1; s <= 1; s += 2) { var ear = mesh(cone(0.06, 0.16, 4), dk, s * 0.11, 0.18, -0.02); ear.rotation.z = -s * 0.3; head.add(ear); head.add(mesh(sph(0.028, 6, 4), M(type === 'yeuho' ? '#00e5ff' : '#ffeb3b', { em: type === 'yeuho' ? '#00e5ff' : '#ffc400', ei: 1.5 }), s * 0.08, 0.04, 0.17, false)); }
    var legs = [];
    [[-0.13, 0.3], [0.13, 0.3], [-0.13, -0.28], [0.13, -0.28]].forEach(function (p) { var l = limb(0.3, 0.05, dk); l.position.set(p[0], 0.32, p[1]); body.add(l); legs.push(l); });
    var tails = [];
    var nt = type === 'yeuho' ? 3 : 1;
    for (var i = 0; i < nt; i++) { var t = mesh(G('tail', function () { var g = new T.ConeGeometry(0.08, 0.55, 8); g.translate(0, 0.27, 0); return g; }), type === 'yeuho' ? M('#ffccbc', { em: '#ff7043', ei: 0.4 }) : bm, (i - (nt - 1) / 2) * 0.1, 0.5, -0.42); t.rotation.x = -0.9; body.add(t); tails.push(t); }
    root.userData = { body: body, head: head, legs: legs, tails: tails, beast: true };
    return root;
  }
  var _tiger; function tigerTex() { if (_tiger) return _tiger; _tiger = canvasTex(64, 64, function (g) { g.fillStyle = '#ff9800'; g.fillRect(0, 0, 64, 64); g.fillStyle = '#2a1a0a'; for (var i = 0; i < 8; i++) g.fillRect(i * 8, 0, 3, 64); }); return _tiger; }

  // ---------- LINH VẬT ----------
  var MASCOTS = R.MASCOTS, MASCOT_ORDER = R.MASCOT_ORDER;
  function makeMascot(key) {
    var Md = MASCOTS[key];
    var mm = MASCOT_MODEL[key];
    if (window.A3 && A3.has('m_' + key)) {
      var r3 = A3.make('m_' + key, 3.1, { glow: true }); A3.glowify(r3, Md.aura);
      var au3 = new T.Mesh(new T.RingGeometry(0.42, 0.52, 32), new T.MeshBasicMaterial({ color: Md.aura, transparent: true, opacity: 0.8, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide }));
      au3.rotation.x = -Math.PI / 2; au3.position.y = 0.03; au3.scale.setScalar(1.5); r3.add(au3);
      var mo3 = []; for (var q3 = 0; q3 < 6; q3++) { var sp3 = glowSprite(Md.aura, 0.22, 0.95); r3.add(sp3); mo3.push(sp3); }
      r3.userData.motes = mo3; r3.userData.aura = au3; r3.userData.rib = [];
      return r3;
    }
    if (modelsReady && MODELS[mm[0]]) {
      var r2 = makeModel(mm[0], mm[1], 2.4);
      var au2 = new T.Mesh(new T.RingGeometry(0.42, 0.52, 32), new T.MeshBasicMaterial({ color: Md.aura, transparent: true, opacity: 0.8, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide }));
      au2.rotation.x = -Math.PI / 2; au2.position.y = 0.03; au2.scale.setScalar(1.4); r2.add(au2);
      var ha = glowSprite(Md.aura, 2.4, 0.4); ha.position.y = 1.1; r2.add(ha);
      var mo = []; for (var qq = 0; qq < 6; qq++) { var sp2 = glowSprite(Md.aura, 0.2, 0.95); r2.add(sp2); mo.push(sp2); }
      r2.userData.motes = mo; r2.userData.aura = au2; r2.userData.rib = [];
      return r2;
    }
    var root = makeHuman(Md.look, { weapon: Md.weapon, cape: Md.cape.replace(/rgba\((\d+),(\d+),(\d+),[^)]+\)/, function (_, r, g, b) { return '#' + [r, g, b].map(function (v) { return (+v).toString(16).padStart(2, '0'); }).join(''); }), wglow: Md.wglow });
    root.scale.setScalar(1.22);
    var aura = new T.Mesh(new T.RingGeometry(0.42, 0.52, 32), new T.MeshBasicMaterial({ color: Md.aura, transparent: true, opacity: 0.8, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide }));
    aura.rotation.x = -Math.PI / 2; aura.position.y = 0.03; root.add(aura);
    var halo = glowSprite(Md.aura, 1.8, 0.4); halo.position.y = 1.0; root.add(halo);
    // dải lụa
    var rib = [];
    for (var r = 0; r < 2; r++) {
      var geo = new T.PlaneGeometry(0.08, 1.5, 1, 12); geo.translate(0, -0.75, 0);
      var m = new T.Mesh(geo, new T.MeshBasicMaterial({ color: Md.ribbon, side: T.DoubleSide, transparent: true, opacity: 0.9 }));
      m.position.set(r ? 0.3 : -0.3, 1.25, -0.08); root.userData.body.add(m); rib.push(m);
      geo.userData.base = geo.attributes.position.array.slice();
    }
    var motes = [];
    for (var i = 0; i < 5; i++) { var sp = glowSprite(Md.aura, 0.16, 0.95); root.add(sp); motes.push(sp); }
    root.userData.rib = rib; root.userData.motes = motes; root.userData.aura = aura;
    return root;
  }

  // ---------- MODEL 3D THẬT (GLB có khung xương, CC0 Quaternius) ----------
  var MODELS = {}, MODEL_BASE = window.MODEL_BASE || 'models/', modelsReady = false, modelTex = {};
  var MODEL_NAMES = ['Warrior', 'Monk', 'Rogue', 'Cleric', 'Wizard', 'Ranger'];
  var UNIT_MODEL = { thienvuong: ['Warrior', '#ffd54f'], thieulam: ['Monk', '#ffb74d'], duongmon: ['Rogue', '#7bd389'], ngudoc: ['Rogue', '#b39ddb'], ngamy: ['Cleric', '#f8bbd0'], vodang: ['Warrior', '#90caf9'], conlon: ['Wizard', '#80deea'], caibang: ['Monk', '#c8b4a8'] };
  var CREEP_MODEL = { sontac: ['Warrior', '#a1887f'], cungtac: ['Ranger', '#c0ca33'], thietgiap: ['Warrior', '#90a4ae'], trai_chu: ['Warrior', '#546e7a'], huyetma: ['Monk', '#ef5350'], mavuong: ['Wizard', '#9575cd'], hacy: ['Rogue', '#555555'], matang: ['Monk', '#d81b60'] };
  var MASCOT_MODEL = { bachy: ['Cleric', '#ffffff'], honglien: ['Rogue', '#ff9e80'], thanhlong: ['Ranger', '#7dffd6'], kimgiap: ['Warrior', '#ffe082'] };
  function loadModels(cb) {
    if (!T.GLTFLoader) { cb && cb(); return; }
    var ld = new T.GLTFLoader(), left = MODEL_NAMES.length, tl = new T.TextureLoader();
    MODEL_NAMES.forEach(function (n) {
      ld.load(MODEL_BASE + n + '.glb', function (g) {
        var box = new T.Box3().setFromObject(g.scene), h = box.max.y - box.min.y;
        MODELS[n] = { scene: g.scene, clips: g.animations, h: h || 1 };
        var names = []; g.scene.traverse(function (o) { if (o.isMesh) (Array.isArray(o.material) ? o.material : [o.material]).forEach(function (m) { if (names.indexOf(m.name) < 0) names.push(m.name); }); });
        var tl2 = names.length || 1, done = function () { if (--tl2 <= 0 && --left === 0) { modelsReady = true; cb && cb(); } };
        if (!names.length) done(); else names.forEach(function (nm) { texFor(nm, done); });
      }, undefined, function () { if (--left === 0) { modelsReady = Object.keys(MODELS).length > 0; cb && cb(); } });
    });
  }
  function texFor(name, cb) {
    if (modelTex[name] !== undefined) { cb && cb(); return modelTex[name]; }
    var t = new T.TextureLoader().load(MODEL_BASE + ({ Bow_Texture: 'Ranger_Bow_Texture' }[name] || name) + '.png', function () { cb && cb(); }, undefined, function () { cb && cb(); }); t.flipY = false; t.encoding = T.LinearEncoding; t.anisotropy = 4;
    return modelTex[name] = t;
  }
  var tintMats = {};
  function makeModel(name, tint, height) {
    var Md = MODELS[name]; if (!Md) return null;
    var obj = T.SkeletonUtils.clone(Md.scene);
    obj.traverse(function (o) {
      if (!o.isMesh) return;
      o.castShadow = true; o.frustumCulled = false;
      var mats = Array.isArray(o.material) ? o.material : [o.material];
      var nm = mats.map(function (m) {
        var key = (m.name || 'm') + tint;
        if (!tintMats[key]) { var c = new T.Color('#ffffff').lerp(new T.Color(tint), 0.3); tintMats[key] = new T.MeshLambertMaterial({ color: c, map: texFor(m.name || (name + '_Texture')), side: T.DoubleSide, emissive: new T.Color(tint).multiplyScalar(0.12) }); }
        return tintMats[key];
      });
      o.material = Array.isArray(o.material) ? nm : nm[0];
    });
    var root = new T.Group(), holder = new T.Group(); root.add(holder); holder.add(obj);
    holder.scale.setScalar(height / Md.h);
    var mixer = new T.AnimationMixer(obj), acts = {};
    Md.clips.forEach(function (c) { acts[c.name] = mixer.clipAction(c); });
    function pick() { for (var i = 0; i < arguments.length; i++) if (acts[arguments[i]]) return acts[arguments[i]]; return null; }
    var findAtk = function () { var k = Object.keys(acts).filter(function (n) { return /Attack/.test(n) && !/Idle/.test(n); }); return k.length ? acts[k[0]] : pick('Punch'); };
    var A = { walk: pick('Walk'), idle: pick('Idle_Weapon', 'Idle_Attacking', 'Attacking_Idle', 'Attack_Idle', 'Idle'), run: pick('Run_Weapon', 'Run', 'Walk'), atk: findAtk(), cast: pick('Spell1', 'Staff_Attack', 'Attack2', 'Dagger_Attack2', 'Sword_AttackFast') || findAtk(), die: pick('Death'), hit: pick('RecieveHit_Attacking', 'RecieveHit') };
    if (A.die) { A.die.setLoop(T.LoopOnce); A.die.clampWhenFinished = true; }
    [A.atk, A.cast, A.hit].forEach(function (a) { if (a) { a.setLoop(T.LoopOnce); a.clampWhenFinished = false; } });
    if (A.idle) { A.idle.play(); A.idle.time = Math.random() * 2; }
    root.userData = { model: true, mixer: mixer, A: A, cur: A.idle, body: holder, head: holder, armL: holder, armR: holder, legL: holder, legR: holder };
    return root;
  }
  function playA(v, a, fade) { var U = v.userData; if (!a || U.cur === a) return; if (U.cur) U.cur.fadeOut(fade || 0.15); a.reset().fadeIn(fade || 0.15).play(); U.cur = a; }
  function animModel(v, st, dt) {
    var U = v.userData, A = U.A;
    if (st.dead) { if (U.cur !== A.die) playA(v, A.die, 0.1); }
    else if (st.cast && st.cast !== U.lastCast) { U.lastCast = st.cast; playA(v, A.cast, 0.08); U.lock = 0.5; }
    else if (st.atk > 0.2 && !U.atkOn) { U.atkOn = true; var a = A.atk; if (a) { a.timeScale = Math.max(1, a.getClip().duration / 0.55); } playA(v, a, 0.06); U.lock = 0.45; }
    else if ((U.lock || 0) <= 0) { playA(v, st.moving ? A.run : A.idle, 0.2); }
    if (st.atk <= 0.05) U.atkOn = false;
    U.lock = (U.lock || 0) - dt;
    U.mixer.update(dt);
  }

  // ---------- THUÊ BAO HIỂN THỊ ----------
  var VU = {}, VC = {}, VP = new Map(), VZ = new Map(), FX = [], mascots = [null, null], ghost = null, ghostCell = null;
  function addFX(o) { FX.push(o); if (o.obj) scene.add(o.obj); return o; }

  var badgeCache = {};
  var SECT_CH = { thienvuong: '天', thieulam: '少', duongmon: '唐', ngudoc: '毒', ngamy: '峨', vodang: '武', conlon: '崑', caibang: '丐' };
  function sectBadge(type) {
    if (badgeCache[type]) return badgeCache[type];
    return badgeCache[type] = canvasTex(64, 64, function (g) { g.fillStyle = '#fff8e1'; g.beginPath(); g.arc(32, 32, 29, 0, 6.3); g.fill(); g.lineWidth = 5; g.strokeStyle = S.UNITS[type].col2; g.stroke(); g.fillStyle = S.UNITS[type].col2; g.font = 'bold 38px serif'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(SECT_CH[type], 32, 34); });
  }
  function visualUnit(u) {
    var v = VU[u.id];
    if (!v) {
      var d = S.UNITS[u.type], um = UNIT_MODEL[u.type];
      var g = makeHuman(R.LOOK[u.type], { weapon: d.weapon, wglow: u.type === 'vodang' ? '#7ab8ff' : null });
      if (g.userData.model || g.userData.card) { var sg = glowSprite(d.col, 0.9, 0.35); sg.position.y = 0.15; g.add(sg); }
      g.userData.tier = -1; g.userData.pop = 0; g.userData.hidden = 0.0;
      var ring = new T.Mesh(G('uring', function () { return new T.RingGeometry(0.34, 0.44, 24); }), new T.MeshBasicMaterial({ color: d.col, transparent: true, opacity: 0.85, side: T.DoubleSide, depthWrite: false }));
      var tring = new T.Mesh(G('tring2', function () { return new T.RingGeometry(0.46, 0.5, 24); }), new T.MeshBasicMaterial({ color: u.owner === 0 ? '#4fc3ff' : '#ff6b5a', transparent: true, opacity: 0.7, side: T.DoubleSide, depthWrite: false }));
      tring.rotation.x = -Math.PI / 2; tring.position.y = 0.035; g.add(tring);
      // cờ lưng môn phái — nhìn là biết phái nào
      var flagG = new T.Group(); flagG.position.set(-0.16, 0, -0.18);
      flagG.add(mesh(G('fpole', function () { return new T.CylinderGeometry(0.015, 0.015, 2.5, 4); }), M('#4e342e'), 0, 1.25, 0, false));
      var fl = mesh(G('fbanner', function () { var g2 = new T.PlaneGeometry(0.34, 0.62, 2, 4); g2.translate(0.17, -0.31, 0); return g2; }), M(d.col, { side: T.DoubleSide, em: d.col, ei: 0.25 }), 0.01, 2.45, 0, false);
      flagG.add(fl); flagG.add(mesh(G('ftip', function () { return new T.ConeGeometry(0.035, 0.12, 5); }), M('#ffd54f', { em: '#ffb300', ei: 0.8 }), 0, 2.56, 0, false));
      var emb = new T.Sprite(new T.SpriteMaterial({ map: sectBadge(u.type), transparent: true, depthWrite: false })); emb.scale.set(0.26, 0.26, 1); emb.position.set(0.18, 2.12, 0.02); flagG.add(emb);
      g.add(flagG); g.userData.flag = fl;
      ring.rotation.x = -Math.PI / 2; ring.position.y = 0.03; g.add(ring); g.userData.ring = ring;
      scene.add(g); v = VU[u.id] = g;
    }
    if (v.userData.tier !== u.tier) {
      v.userData.tier = u.tier;
      if (u.tier > 0) {
        var col = S.UNITS[u.type].col;
        var au = new T.Mesh(G('tring', function () { return new T.RingGeometry(0.38, 0.5, 32); }), new T.MeshBasicMaterial({ color: '#ffd740', transparent: true, opacity: 0.7, blending: T.AdditiveBlending, side: T.DoubleSide, depthWrite: false }));
        au.rotation.x = -Math.PI / 2; au.position.y = 0.04; v.add(au); v.userData.aura = au;
        var gs = glowSprite(col, 1.2, 0.35); gs.position.y = 0.6; v.add(gs);
        if (v.userData.a3) { A3.glowify(v, S.UNITS[u.type].col); } else if (v.userData.card) { CARDS.glowify(v, S.UNITS[u.type].col); } else if (!v.userData.model) { var cp = mesh(G('capeR', null), M(S.UNITS[u.type].col2, { side: T.DoubleSide }), 0, 1.42, -0.17); cp.rotation.x = 0.12; v.userData.body.add(cp); v.userData.cape = cp; } else { var cr = mesh(cone(0.09, 0.2, 5), M('#ffd740', { em: '#ffb300', ei: 1.2 }), 0, 1.95, 0, false); v.add(cr); }
        v.userData.scaleBase = 1.12;
      }
    }
    return v;
  }
  function visualCreep(c) {
    var v = VC[c.id];
    if (!v) {
      var d = S.CREEPS[c.type];
      var cm = CREEP_MODEL[c.type];
      v = d.beast ? makeBeast(c.type) : makeHuman(R.CLOOK[c.type], { weapon: R.CLOOK[c.type].weapon });
      v.userData.size = d.size;
      if (R.CLOOK[c.type] && R.CLOOK[c.type].aura) { var a = glowSprite(R.CLOOK[c.type].aura, 2.2, 0.5); a.position.y = 0.6; v.add(a); }
      if (d.boss) { var br = new T.Mesh(new T.RingGeometry(0.5, 0.62, 32), new T.MeshBasicMaterial({ color: '#ff1744', transparent: true, opacity: 0.8, side: T.DoubleSide, depthWrite: false, blending: T.AdditiveBlending })); br.rotation.x = -Math.PI / 2; br.position.y = 0.04; v.add(br); }
      if (d.send) { var sr = glowSprite('#ff1744', 1.0, 0.4); sr.position.y = 0.5; v.add(sr); }
      v.scale.setScalar(d.size * (d.beast ? 1.5 : 1.2));
      scene.add(v); VC[c.id] = v;
    }
    return v;
  }

  function animHuman(v, o, t, dt) {
    var U = v.userData;
    var sw = o.moving ? Math.sin(t * 11) * 0.7 : 0;
    U.legL.rotation.x = sw; U.legR.rotation.x = -sw;
    var atk = o.atk > 0 ? Math.sin((1 - o.atk / 0.3) * Math.PI) : 0;
    U.armL.rotation.x = -sw * 0.6;
    U.armR.rotation.x = o.moving ? sw * 0.6 : -atk * 2.0 - 0.15;
    U.body.position.y = o.moving ? Math.abs(Math.sin(t * 11)) * 0.06 : Math.sin(t * 2.5 + (o.ph || 0)) * 0.012;
    U.body.rotation.x = atk * 0.25;
    if (U.head.userData.hair) U.head.userData.hair.rotation.x = (U.head.userData.hair.userData.bx || (U.head.userData.hair.userData.bx = U.head.userData.hair.rotation.x)) + Math.sin(t * 4 + (o.ph || 0)) * 0.12;
    if (U.cape) { U.cape.rotation.x = 0.2 + (o.moving ? 0.5 : 0) + Math.sin(t * 5 + (o.ph || 0)) * 0.08; }
  }
  function animBeast(v, o, t) {
    var U = v.userData, sw = o.moving ? Math.sin(t * 14) * 0.8 : 0;
    U.legs[0].rotation.x = sw; U.legs[3].rotation.x = sw; U.legs[1].rotation.x = -sw; U.legs[2].rotation.x = -sw;
    U.body.position.y = o.moving ? Math.abs(Math.sin(t * 14)) * 0.05 : 0;
    var atk = o.atk > 0 ? Math.sin((1 - o.atk / 0.3) * Math.PI) : 0;
    U.head.position.z = 0.45 + atk * 0.18; U.head.rotation.x = -atk * 0.4;
    U.tails.forEach(function (tl, i) { tl.rotation.z = Math.sin(t * 6 + i) * 0.4; });
  }
  function faceTo(v, f, targetAng, dt) {
    var cur = v.rotation.y, d = targetAng - cur; while (d > Math.PI) d -= 6.283; while (d < -Math.PI) d += 6.283;
    v.rotation.y = cur + d * Math.min(1, dt * 10);
  }
  function lerpPos(e, a) { var px = e.px === undefined ? e.x : e.px, py = e.py === undefined ? e.y : e.py; return [px + (e.x - px) * a, py + (e.y - py) * a]; }

  // ---------- Hiệu ứng ----------
  function burst(pos, col, n, spd, size, life, grav) {
    for (var i = 0; i < n; i++) {
      var sp = new T.Sprite(spriteMat(col, 1)); var s = size * (0.6 + Math.random() * 0.8); sp.scale.set(s, s, 1); sp.position.copy(pos);
      var a = Math.random() * 6.283, el = Math.random() * 1.2 + 0.2, v = spd * (0.4 + Math.random() * 0.8);
      addFX({ obj: sp, t: 0, life: life * (0.6 + Math.random() * 0.6), vx: Math.cos(a) * Math.cos(el) * v, vy: Math.sin(el) * v, vz: Math.sin(a) * Math.cos(el) * v, g: grav === undefined ? 6 : grav, s0: s,
        up: function (f, dt, k) { f.obj.position.x += f.vx * dt; f.obj.position.y = Math.max(0.03, f.obj.position.y + f.vy * dt); f.obj.position.z += f.vz * dt; f.vy -= f.g * dt; f.obj.material.opacity = 1; var sc = f.s0 * (1 - k); f.obj.scale.set(sc, sc, 1); } });
    }
  }
  function ringFX(pos, col, r0, r1, life, tex, op) {
    var m = new T.Mesh(G('plane1', function () { return new T.PlaneGeometry(1, 1); }), new T.MeshBasicMaterial({ map: tex || ringTex, color: col, transparent: true, opacity: op || 1, blending: T.AdditiveBlending, depthWrite: false }));
    m.rotation.x = -Math.PI / 2; m.position.copy(pos); m.position.y = 0.06;
    return addFX({ obj: m, t: 0, life: life, up: function (f, dt, k) { var r = r0 + (r1 - r0) * (1 - Math.pow(1 - k, 3)); f.obj.scale.set(r * 2, r * 2, 1); f.obj.material.opacity = (op || 1) * (1 - k); f.obj.rotation.z += dt * 1.5; }, dispose: true });
  }
  function pillar(pos, col, h, life, r) {
    var m = new T.Mesh(G('pil', function () { return new T.CylinderGeometry(1, 1, 1, 20, 1, true); }), new T.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.6, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide }));
    m.position.copy(pos);
    addFX({ obj: m, t: 0, life: life, up: function (f, dt, k) { var rr = (r || 0.5) * (1 - k * 0.6); f.obj.scale.set(rr, h * (0.3 + k), rr); f.obj.position.y = h * (0.3 + k) / 2; f.obj.material.opacity = 0.6 * (1 - k); }, dispose: true });
  }
  function boltLine(pts, col, life, width) {
    var grp = new T.Group();
    var mk = function () {
      while (grp.children.length) { var c = grp.children.pop(); c.geometry.dispose(); }
      var arr = [];
      for (var i = 0; i < pts.length - 1; i++) {
        var a = pts[i], b = pts[i + 1];
        for (var s = 0; s <= 6; s++) { var k = s / 6, j = (s === 0 || s === 6) ? 0 : 0.18; arr.push(new T.Vector3(a.x + (b.x - a.x) * k + (Math.random() - 0.5) * j, a.y + (b.y - a.y) * k + (Math.random() - 0.5) * j, a.z + (b.z - a.z) * k + (Math.random() - 0.5) * j)); }
      }
      var curve = new T.CatmullRomCurve3(arr);
      var tube = new T.Mesh(new T.TubeGeometry(curve, arr.length * 2, width || 0.035, 4, false), new T.MeshBasicMaterial({ color: '#ffffff', transparent: true, blending: T.AdditiveBlending, depthWrite: false }));
      var tube2 = new T.Mesh(new T.TubeGeometry(curve, arr.length * 2, (width || 0.035) * 3, 4, false), new T.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.6, blending: T.AdditiveBlending, depthWrite: false }));
      grp.add(tube, tube2);
    };
    mk();
    pts.forEach(function (p) { var gs = glowSprite(col, 0.9, 0.9); gs.position.copy(p); grp.add(gs); });
    addFX({ obj: grp, t: 0, life: life, nx: 0, up: function (f, dt, k) { f.nx -= dt; if (f.nx <= 0 && k < 0.7) { f.nx = 0.05; var keep = grp.children.filter(function (c) { return c.isSprite; }); mk(); keep.forEach(function (s) { grp.add(s); }); } grp.children.forEach(function (c) { if (c.material) c.material.opacity = (c.isSprite ? 0.9 : 0.8) * (1 - k); }); }, disposeGroup: true });
  }
  function shakeCam(a) { camShake = Math.max(camShake, a); }
  var camShake = 0;

  // ---------- Văn bản nổi (overlay 2D) ----------
  var TXT = [];
  function ftext(pos, str, col, size, life, rise, font) { TXT.push({ p: pos.clone(), s: str, c: col, z: size || 16, t: 0, life: life || 1, rise: rise === undefined ? 1.2 : rise, font: font }); }

  // ---------- SỰ KIỆN từ mô phỏng ----------
  function onEvent(e, G) {
    var lane = e.lane !== undefined ? e.lane : e.p;
    switch (e.e) {
      case 'hit': {
        var p = W(e.lane, e.x, e.y, 0.55);
        var col = { slash: '#ffffff', dart: '#c8ff8a', fandart: '#ffe082', sword: '#7ab8ff', poison: '#76ff03', petal: '#ff80ab', dragon: '#ffd740' }[e.k] || '#ffffff';
        burst(p, col, e.k === 'slash' ? 5 : 4, 3, 0.18, 0.3, 4);
        if (e.k === 'slash') slashFX(p, col);
        if (e.k === 'sword') ringFX(W(e.lane, e.x, e.y), '#7ab8ff', 0.2, 1.1, 0.35);
        if (e.k === 'poison') burst(p, '#64dd17', 5, 1.5, 0.22, 0.6, -1);
        break;
      }
      case 'kill': {
        var p2 = W(e.lane, e.x, e.y, 0.5);
        var cols = e.fx === 'poison' ? '#76ff03' : e.fx === 'bolt' || e.fx === 'thunder' ? '#80deea' : e.fx === 'sword' ? '#7ab8ff' : e.fx === 'dragon' ? '#ffd740' : '#ff5252';
        burst(p2, cols, e.boss ? 40 : 12, e.boss ? 7 : 4, e.boss ? 0.5 : 0.25, e.boss ? 1.2 : 0.6, 7);
        burst(p2, '#ffffff', 4, 2, 0.3, 0.4, 0);
        var soul = glowSprite('#b3e5fc', 0.6, 0.9); soul.position.copy(p2);
        addFX({ obj: soul, t: 0, life: 1.2, up: function (f, dt, k) { f.obj.position.y += dt * 1.6; f.obj.position.x += Math.sin(k * 12) * 0.01; f.obj.material.opacity = 0.9 * (1 - k); } });
        if (e.g) { ftext(W(e.lane, e.x, e.y, 1.1), '+' + e.g, '#ffd54f', e.boss ? 26 : 15, 0.9); coinBurst(W(e.lane, e.x, e.y, 0.5), Math.min(e.boss ? 36 : 12, 3 + e.g * 2)); }
        if (e.boss) { ringFX(W(e.lane, e.x, e.y), '#ff8a3a', 0.5, 4, 0.9); shakeCam(0.5); }
        break;
      }
      case 'skill': skillFX(e, G); break;
      case 'chain': boltLine(e.pts.map(function (q) { return W(e.lane, q.x, q.y, 0.6); }), '#18ffff', 0.25); break;
      case 'strike': {
        var p3 = W(e.lane, e.x, e.y);
        if (e.fx === 'thunder') {
          var top = W(e.lane, e.x + 0.6, e.y - 0.5, 11);
          boltLine([top, W(e.lane, e.x - 0.3, e.y + 0.2, 6), W(e.lane, e.x + 0.2, e.y, 2.5), W(e.lane, e.x, e.y, 0.05)], '#40c4ff', 0.45, 0.06);
          ringFX(p3, '#80d8ff', 0.3, e.r * 1.3, 0.6); burst(W(e.lane, e.x, e.y, 0.2), '#e1f5fe', 22, 6, 0.3, 0.6, 8); pillar(p3, '#80d8ff', 5, 0.35, 0.8); shakeCam(0.35);
          flashLight(p3, '#80d8ff', 0.25);
        } else { ringFX(p3, '#82b1ff', 0.1, 0.9, 0.35); burst(W(e.lane, e.x, e.y, 0.15), '#bbdefb', 6, 3, 0.18, 0.35, 6); }
        break;
      }
      case 'healed': ftext(W(e.lane, e.x, e.y, 1.25), '+' + Math.round(e.v), '#69f0ae', 13, 0.8); burst(W(e.lane, e.x, e.y, 0.5), '#69f0ae', 4, 1, 0.2, 0.6, -1.5); break;
      case 'gateHit': {
        var gt = gates[e.lane]; gt.flash.material.opacity = 0.7; gt.shake = 0.4;
        ftext(W(e.lane, HL, 17.6, 3.2), '-' + e.v, '#ff5252', 30, 1.1, 1.4);
        burst(W(e.lane, e.x, 17.3, 0.6), '#ff8a65', 14, 4, 0.3, 0.6);
        break;
      }
      case 'place': case 'upgrade': {
        var u = S.findUnit(G, e.id); if (!u) break;
        var pos = W(u.owner, u.cx + 0.5, u.cy + 0.5);
        var mv = mascots[u.owner];
        var delay = 0;
        if (mv && G.phase === 'build') { if (mv.q.length > 1) mv.q.splice(0, mv.q.length - 1); delay = Math.min(0.7, mascotGo(mv, u.cx + 0.5, u.cy + 0.5)); }
        var vu = visualUnit(u);
        if (e.e === 'place') { vu.userData.hidden = delay; vu.visible = delay <= 0; }
        (function (pp, col, d, isUp) { addFX({ t: -d, life: 0.01, up: function () {}, end: function () { pillar(pp, isUp ? '#ffd740' : col, 4, 0.6, 0.55); ringFX(pp, isUp ? '#ffd740' : col, 0.2, 1.3, 0.6); burst(pp.clone().setY(0.4), isUp ? '#fff59d' : col, 16, 3, 0.2, 0.7, -1); } }); })(pos, S.UNITS[u.type].col, delay, e.e === 'upgrade');
        if (e.e === 'upgrade') ftext(W(u.owner, u.cx + 0.5, u.cy + 0.5, 1.8), S.UNITS[u.type].up.name, '#ffd740', 16, 1.4, 0.8, 'serif');
        break;
      }
      case 'sell': burst(W(e.p, e.x, e.y, 0.4), '#ffd54f', 12, 2.5, 0.2, 0.6); ftext(W(e.p, e.x, e.y, 1), '+' + e.g, '#ffd54f', 16, 0.9); break;
      case 'unitDie': burst(W(e.p, e.x, e.y, 0.5), '#ffffff', 10, 2.5, 0.22, 0.6); break;
      case 'leak': burst(W(e.lane, e.x, e.y, 0.3), '#ff1744', 6, 1.5, 0.25, 0.5, -1); break;
    }
  }
  // tiền vàng tung toé kiểu máy xèng
  function coinBurst(p, n) {
    var cg = G('coin', function () { var g = new T.CylinderGeometry(0.13, 0.13, 0.035, 14); g.rotateX(Math.PI / 2); return g; });
    var cm = M('#ffcf40', { em: '#ff9d00', ei: 0.9 });
    for (var i = 0; i < n; i++) {
      var c = new T.Mesh(cg, cm); c.position.copy(p); c.castShadow = true;
      var a = Math.random() * 6.283, sp = 1.2 + Math.random() * 2.2;
      addFX({ obj: c, t: -i * 0.012, life: 0.6, vx: Math.cos(a) * sp, vz: Math.sin(a) * sp, vy: 4 + Math.random() * 3.5, spin: 10 + Math.random() * 14,
        up: function (f, dt) { var o = f.obj; f.vy -= 16 * dt; o.position.x += f.vx * dt; o.position.z += f.vz * dt; o.position.y += f.vy * dt; if (o.position.y < 0.08) { o.position.y = 0.08; f.vy = Math.abs(f.vy) * 0.45; f.vx *= 0.7; f.vz *= 0.7; } o.rotation.y += f.spin * dt; o.rotation.x += f.spin * 0.6 * dt; } });
    }
    var gs = glowSprite('#ffd740', 1.6, 0.9); gs.position.copy(p);
    addFX({ obj: gs, t: 0, life: 0.35, up: function (f, dt, k) { var s2 = 1.6 + k * 2; f.obj.scale.set(s2, s2, 1); f.obj.material.opacity = 0.9 * (1 - k); } });
  }
  function slashFX(p, col) {
    var m = new T.Mesh(G('slash', function () { return new T.RingGeometry(0.28, 0.42, 16, 1, 0, Math.PI * 0.9); }), new T.MeshBasicMaterial({ color: col, transparent: true, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide }));
    m.position.copy(p); m.lookAt(camera.position); m.rotation.z = Math.random() * 6.28;
    addFX({ obj: m, t: 0, life: 0.18, up: function (f, dt, k) { f.obj.material.opacity = 1 - k; f.obj.scale.setScalar(1 + k * 0.6); f.obj.rotation.z += dt * 12; }, dispose: true });
  }
  var flashes = [];
  function flashLight(p, col, life) {
    var l = new T.PointLight(col, 4, 8); l.position.copy(p).setY(2);
    addFX({ obj: l, t: 0, life: life, up: function (f, dt, k) { f.obj.intensity = 4 * (1 - k); } });
  }
  function skillName(e, G) {
    var u = S.findUnit(G, e.id); if (!u) return;
    ftext(W(e.lane, u.x, u.y, 2.4), S.UNITS[u.type].skill.name, S.UNITS[u.type].col, 15, 1.3, 0.7, 'serif');
  }
  function skillFX(e, G) {
    var p = W(e.lane, e.x, e.y);
    var cu = S.findUnit(G, e.id); if (cu) cu._castT = (cu._castT || 0) + 1;
    skillName(e, G);
    switch (e.k) {
      case 'whirl':
        for (var i = 0; i < 3; i++) (function (i) {
          var m = new T.Mesh(G2('whirl', function () { return new T.TorusGeometry(1, 0.06, 6, 32, Math.PI * 1.3); }), new T.MeshBasicMaterial({ color: '#ffd740', transparent: true, blending: T.AdditiveBlending, depthWrite: false }));
          m.position.copy(p).setY(0.35 + i * 0.2); m.rotation.x = Math.PI / 2;
          addFX({ obj: m, t: 0, life: 0.55, up: function (f, dt, k) { f.obj.rotation.z += dt * 18; var s = e.r * (0.5 + k * 0.6); f.obj.scale.set(s, s, 1); f.obj.material.opacity = 1 - k; }, dispose: true });
        })(i);
        burst(p.clone().setY(0.3), '#ffe082', 18, 4, 0.2, 0.5, 2);
        break;
      case 'shock':
        ringFX(p, '#ffc107', 0.2, e.r * 1.2, 0.6); ringFX(p, '#fff59d', 0.1, e.r * 0.8, 0.45);
        pillar(p, '#ffd740', 3.5, 0.5, 0.7);
        var palm = new T.Mesh(G2('plane1', function () { return new T.PlaneGeometry(1, 1); }), new T.MeshBasicMaterial({ map: lotusTex, color: '#ffca28', transparent: true, blending: T.AdditiveBlending, depthWrite: false }));
        palm.rotation.x = -Math.PI / 2; palm.position.copy(p).setY(0.08);
        addFX({ obj: palm, t: 0, life: 0.7, up: function (f, dt, k) { var s = e.r * 2 * (0.5 + k * 0.6); f.obj.scale.set(s, s, 1); f.obj.material.opacity = 1 - k; }, dispose: true });
        burst(p.clone().setY(0.2), '#ffe082', 20, 5, 0.22, 0.5, 6); shakeCam(0.2);
        break;
      case 'fan': burst(p.clone().setY(0.7), '#ffe082', 10, 2, 0.2, 0.3, 0); break;
      case 'cloud': break;
      case 'massheal':
        var lot = new T.Mesh(G2('plane1', function () { return new T.PlaneGeometry(1, 1); }), new T.MeshBasicMaterial({ map: lotusTex, color: '#ff80ab', transparent: true, blending: T.AdditiveBlending, depthWrite: false }));
        lot.rotation.x = -Math.PI / 2; lot.position.copy(p).setY(0.07);
        addFX({ obj: lot, t: 0, life: 1.4, up: function (f, dt, k) { var s = e.r * 2 * Math.min(1, k * 4); f.obj.scale.set(s, s, 1); f.obj.rotation.z += dt * 0.8; f.obj.material.opacity = k < 0.7 ? 0.95 : (1 - k) / 0.3 * 0.95; }, dispose: true });
        for (var j = 0; j < 24; j++) { var a = Math.random() * 6.28, r = Math.random() * e.r; var sp = glowSprite(j % 2 ? '#ff80ab' : '#b9f6ca', 0.22, 1); sp.position.set(p.x + Math.cos(a) * r, 0.1, p.z + Math.sin(a) * r); addFX({ obj: sp, t: -Math.random() * 0.4, life: 1.2, up: function (f, dt, k) { f.obj.position.y += dt * 1.5; f.obj.material.opacity = 1 - k; } }); }
        break;
      case 'swordrain':
        G.strikes.forEach(function (s) {
          if (s._v || s.fx !== 'sword' || s.lane !== e.lane) return; s._v = 1;
          var sw = swordMesh('#7ab8ff', 1.4); var target = W(s.lane, s.x, s.y, 0.15), tt = s.t;
          sw.rotation.set(Math.PI, 0, 0); sw.position.copy(target).setY(9);
          var gs = glowSprite('#448aff', 1.2, 0.9); sw.add(gs);
          addFX({ obj: sw, t: 0, life: tt + 0.15, up: function (f, dt, k) { var kk = Math.min(1, f.t / tt); f.obj.position.y = 9 - 8.85 * kk * kk; f.obj.visible = true; }, disposeGroup: true });
        });
        ringFX(p, '#448aff', e.r * 1.2, e.r * 1.2, 0.9, runeTex, 0.8);
        break;
      case 'thunder':
        ringFX(p, '#40c4ff', e.r, e.r, 0.5, runeTex, 0.9);
        break;
      case 'dragon': shakeCam(0.15); break;
    }
  }
  function G2(k, f) { return G(k, f); }
  function swordMesh(col, s) {
    var g = new T.Group();
    var bl = mesh(G('swb', function () { var g = new T.ConeGeometry(0.06, 1, 4); g.translate(0, 0.5, 0); g.scale(1, 1, 0.3); return g; }), new T.MeshBasicMaterial({ color: '#e3f2fd' }), 0, 0.08, 0, false);
    var gd = mesh(box(0.24, 0.04, 0.05), M('#e8b04a', { em: '#a06a10', ei: 0.5 }), 0, 0.06, 0, false);
    var hl = mesh(cyl(0.025, 0.025, 0.2, 5), M('#4e342e'), 0, -0.06, 0, false);
    g.add(bl, gd, hl); g.scale.setScalar(s || 1);
    var gl = glowSprite(col, 0.7, 0.9); gl.position.y = 0.4; g.add(gl);
    return g;
  }

  // ---------- Đạn ----------
  function projVisual(p) {
    var g = new T.Group(), col;
    switch (p.k) {
      case 'dart': case 'fandart':
        col = p.k === 'dart' ? '#b2ff59' : '#ffd740';
        var nd = mesh(G('needle', function () { var c = new T.ConeGeometry(0.03, 0.34, 4); c.rotateZ(-Math.PI / 2); return c; }), new T.MeshBasicMaterial({ color: '#ffffff' }), 0, 0, 0, false);
        g.add(nd); g.add(glowSprite(col, 0.5, 0.9)); g.userData.trail = col; g.userData.ts = 0.26; break;
      case 'poison': col = '#76ff03'; g.add(mesh(sph(0.1, 10, 8), M('#64dd17', { em: '#76ff03', ei: 1.5 }), 0, 0, 0, false)); g.add(glowSprite(col, 0.8, 0.8)); g.userData.trail = '#33691e'; g.userData.ts = 0.3; g.userData.bub = 1; break;
      case 'petal': case 'healorb': col = '#ff80ab'; g.add(glowSprite(col, 0.75, 1)); for (var i = 0; i < 3; i++) { var pt = mesh(G('petal', function () { var s = new T.SphereGeometry(0.06, 6, 4); s.scale(1, 0.3, 2); return s; }), M('#ffc1d9', { em: '#ff80ab', ei: 1 }), 0, 0, 0, false); g.add(pt); } g.userData.orbit = 1; g.userData.trail = p.k === 'healorb' ? '#69f0ae' : '#ff80ab'; g.userData.ts = 0.3; break;
      case 'sword': col = '#7ab8ff'; var sw = swordMesh('#448aff', 0.75); sw.rotation.z = -Math.PI / 2; g.add(sw); g.userData.trail = '#448aff'; g.userData.ts = 0.4; break;
      case 'arrow': g.add(mesh(G('arrow', function () { var c = new T.CylinderGeometry(0.012, 0.012, 0.5, 4); c.rotateZ(Math.PI / 2); return c; }), M('#8d6e63'), 0, 0, 0, false)); g.add(mesh(G('ahead', function () { var c = new T.ConeGeometry(0.03, 0.08, 4); c.rotateZ(-Math.PI / 2); c.translate(0.27, 0, 0); return c; }), M('#cfd8dc'), 0, 0, 0, false)); break;
      case 'dragon': return dragonVisual(p);
      case 'poisonbomb': g.add(mesh(sph(0.16, 10, 8), M('#64dd17', { em: '#76ff03', ei: 1.2 }), 0, 0, 0, false)); g.add(glowSprite('#76ff03', 1.1, 0.9)); g.userData.trail = '#76ff03'; g.userData.ts = 0.35; break;
    }
    scene.add(g); return g;
  }
  function dragonVisual(p) {
    var g = new T.Group(); g.userData.dragon = true; g.userData.hist = [];
    var segs = [];
    var mat = M('#ffca28', { em: '#ff8f00', ei: 1.4 }), mat2 = M('#ffe082', { em: '#ffb300', ei: 1.2 });
    for (var i = 0; i < 16; i++) { var r = 0.2 * (1 - i / 22); var s = mesh(sph(0.2, 10, 8), i % 2 ? mat : mat2, 0, 0, 0, false); s.scale.setScalar(r / 0.2); g.add(s); segs.push(s);
      if (i % 3 === 1) { var fin = mesh(cone(0.05, 0.2, 4), M('#ff6f00', { em: '#ff3d00', ei: 1 }), 0, 0.18 * (r / 0.2), 0, false); s.add(fin); } }
    var head = new T.Group();
    head.add(mesh(G('dhead', function () { var c = new T.SphereGeometry(0.26, 12, 10); c.scale(1.4, 0.9, 1); return c; }), mat, 0, 0, 0, false));
    head.add(mesh(G('djaw', function () { var c = new T.ConeGeometry(0.16, 0.42, 6); c.rotateZ(-Math.PI / 2); return c; }), mat2, 0.32, -0.04, 0, false));
    for (var s2 = -1; s2 <= 1; s2 += 2) { var horn = mesh(cone(0.04, 0.34, 5), M('#fff8e1', { em: '#ffe082', ei: 0.8 }), -0.12, 0.2, s2 * 0.12, false); horn.rotation.z = 0.9; head.add(horn); head.add(mesh(sph(0.04, 6, 4), M('#ff1744', { em: '#ff1744', ei: 2 }), 0.15, 0.08, s2 * 0.13, false)); var wh = mesh(cyl(0.01, 0.005, 0.5, 3), M('#fff59d', { em: '#fff59d', ei: 1 }), 0.2, -0.05, s2 * 0.15, false); wh.rotation.z = 1.2; wh.rotation.x = s2 * 0.5; head.add(wh); }
    head.add(glowSprite('#ffab00', 1.8, 0.8));
    g.add(head); g.userData.segs = segs; g.userData.head = head;
    scene.add(g); return g;
  }

  function trailPuff(pos, col, s) {
    var sp = new T.Sprite(spriteMat(col, 0.8)); sp.position.copy(pos); sp.scale.set(s, s, 1);
    addFX({ obj: sp, t: 0, life: 0.25, up: function (f, dt, k) { var ss = s * (1 - k); f.obj.scale.set(ss, ss, 1); } });
  }

  // ---------- Mascot ----------
  function mascotHome(lane) { return { x: HL + (lane ? -1.8 : 1.8), y: 15.7 }; }
  function initMascots(keys) {
    for (var i = 0; i < 2; i++) {
      if (mascots[i]) scene.remove(mascots[i].v);
      var v = makeMascot(keys[i]); scene.add(v);
      var h = mascotHome(i);
      mascots[i] = { v: v, lane: i, x: h.x, y: h.y, q: [], state: 'idle', cast: 0, key: keys[i], cheer: 0, face: Math.PI };
      v.position.copy(W(i, h.x, h.y));
    }
  }
  function mascotGo(m, x, y) {
    // trả về thời gian (s) tới khi đến nơi
    var lx = m.q.length ? m.q[m.q.length - 1].x : m.x, ly = m.q.length ? m.q[m.q.length - 1].y : m.y;
    var tPrev = m.q.reduce(function (a, q) { return a + q.d; }, 0) + m.cast;
    var d = Math.hypot(x - lx, y - ly) / 14 + 0.25;
    m.q.push({ x: x, y: y, d: d });
    return tPrev + d - 0.05;
  }
  function U0(v) { return v.userData.model; }
  function stepMascot(m, dt, t, G) {
    var v = m.v, moving = false;
    if (m.cast > 0) { m.cast -= dt; }
    else if (m.q.length) {
      var q = m.q[0], dx = q.x - m.x, dy = q.y - m.y, dd = Math.hypot(dx, dy), sp = 14 * dt;
      if (dd <= sp + 0.3) { m.x = q.x - (dx / (dd || 1)) * 0.45; m.y = q.y - (dy / (dd || 1)) * 0.45; m.q.shift(); m.cast = 0.25; m.castId = (m.castId || 0) + 1; m.face = Math.atan2(dx, -dy); }
      else { m.x += dx / dd * sp; m.y += dy / dd * sp; moving = true; m.face = Math.atan2(dx, -dy); if (Math.random() < 0.8) trailPuff(W(m.lane, m.x, m.y, 0.7), R.MASCOTS[m.key].aura, 0.7); }
    } else {
      var h = mascotHome(m.lane), dx2 = h.x - m.x, dy2 = h.y - m.y, d2 = Math.hypot(dx2, dy2);
      if (d2 > 0.1) { var s2 = Math.min(d2, 5 * dt); m.x += dx2 / d2 * s2; m.y += dy2 / d2 * s2; moving = true; m.face = Math.atan2(dx2, -dy2); }
      else m.face = 0;
    }
    v.position.copy(W(m.lane, m.x, m.y));
    if (m.cheer > 0) { m.cheer -= dt; v.position.y = Math.abs(Math.sin(m.cheer * 10)) * 0.4; }
    else if (!moving && !v.userData.model && !v.userData.a3) v.position.y = 0.15 + Math.sin(t * 2) * 0.06; // bay lơ lửng
    var U = v.userData;
    if (!U.card) faceTo(v, 1, m.face, dt);
    if (U.a3) { faceTo(v, 1, m.face, dt); A3.anim(v, { moving: moving, atk: 0, cast: m.castId || 0 }, dt, t); }
    else if (U.card) { CARDS.anim(v, { moving: moving, atk: 0, cast: m.castId || 0, face: Math.sin(m.face) >= 0 ? 1 : -1 }, dt, t, camera); }
    else if (U.model) { animModel(v, { moving: moving, atk: 0, cast: m.castId || 0 }, dt); }
    else { animHuman(v, { moving: moving, atk: m.cast > 0 ? m.cast * 1.2 : 0, ph: m.lane }, t, dt); if (m.cast > 0) U.armL.rotation.x = -2.6; }
    U.rib.forEach(function (r, i) { var a = r.geometry.attributes.position, base = r.geometry.userData.base; for (var k = 0; k < a.count; k++) { var y = base[k * 3 + 1]; a.setZ(k, base[k * 3 + 2] - Math.sin(t * 4 + y * 5 + i) * 0.12 * (-y) - (moving ? -y * 0.5 : 0)); } a.needsUpdate = true; });
    U.motes.forEach(function (s, i) { var a = t * 1.6 + i * 1.256; s.position.set(Math.cos(a) * 0.6, 1.0 + Math.sin(a * 1.3) * 0.6, Math.sin(a) * 0.6); });
    U.aura.rotation.z = t;
    if (U.cape) U.cape.rotation.x = 0.25 + (moving ? 0.9 : 0) + Math.sin(t * 4) * 0.1;
  }

  // ---------- Khởi tạo ----------
  function init(canvas, ov) {
    renderer = new T.WebGLRenderer({ canvas: canvas, antialias: true, powerPreference: 'high-performance' });
    DPR = Math.min(window.devicePixelRatio || 1, LOW ? 1.25 : 1.75);
    renderer.setPixelRatio(DPR);
    renderer.shadowMap.enabled = true; renderer.shadowMap.type = LOW ? T.PCFShadowMap : T.PCFSoftShadowMap;
    makeGrad(); makeTextures(); makeRoofTex();
    OUT = new T.MeshBasicMaterial({ color: '#1a0e0a', side: T.BackSide });
    buildScene();
    camera = new T.PerspectiveCamera(42, 1, 0.5, 260);
    composer = new T.EffectComposer(renderer);
    composer.addPass(new T.RenderPass(scene, camera));
    bloom = new T.UnrealBloomPass(new T.Vector2(256, 256), 0.55, 0.4, 0.93);
    composer.addPass(bloom);
    var grade = new T.ShaderPass({ uniforms: { tDiffuse: { value: null } }, vertexShader: 'varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0); }',
      fragmentShader: 'uniform sampler2D tDiffuse; varying vec2 vUv; void main(){ vec4 c=texture2D(tDiffuse,vUv); vec3 x=c.rgb; x = x*x*(3.0-2.0*x)*0.35 + x*0.65; float l=dot(x,vec3(0.299,0.587,0.114)); x=mix(vec3(l),x,1.18); x*=vec3(1.03,0.99,0.95); vec2 d=vUv-0.5; x*=1.0-dot(d,d)*0.9; gl_FragColor=vec4(x,1.0); }' });
    composer.addPass(grade);
    overlay = ov; octx = ov.getContext('2d');
    ghost = new T.Group(); scene.add(ghost);
    var cellM = new T.Mesh(new T.PlaneGeometry(0.96, 0.96), new T.MeshBasicMaterial({ color: '#69f0ae', transparent: true, opacity: 0.45, depthWrite: false }));
    cellM.rotation.x = -Math.PI / 2; cellM.position.y = 0.05; ghost.add(cellM); ghost.userData.cell = cellM; ghost.visible = false;
    var rangeM = new T.Mesh(new T.RingGeometry(0.97, 1, 48), new T.MeshBasicMaterial({ color: '#ffffff', transparent: true, opacity: 0.5, depthWrite: false, side: T.DoubleSide }));
    rangeM.rotation.x = -Math.PI / 2; rangeM.position.y = 0.05; ghost.add(rangeM); ghost.userData.range = rangeM;
    selRing = new T.Mesh(new T.RingGeometry(0.42, 0.52, 32), new T.MeshBasicMaterial({ color: '#ffd740', transparent: true, opacity: 0.9, depthWrite: false, side: T.DoubleSide, blending: T.AdditiveBlending }));
    selRing.rotation.x = -Math.PI / 2; selRing.visible = false; scene.add(selRing);
    selRange = new T.Mesh(new T.RingGeometry(0.98, 1, 64), new T.MeshBasicMaterial({ color: '#ffd740', transparent: true, opacity: 0.35, depthWrite: false, side: T.DoubleSide }));
    selRange.rotation.x = -Math.PI / 2; selRange.visible = false; scene.add(selRange);
    resize();
  }
  var selRing, selRange, ghostMesh = null, ghostType = null;
  function resize() {
    Wd = window.innerWidth; Hd = window.innerHeight;
    renderer.setSize(Wd, Hd, false); composer.setSize(Wd, Hd);
    bloom.resolution.set(Wd / (LOW ? 3 : 2), Hd / (LOW ? 3 : 2));
    camera.aspect = Wd / Hd; camera.updateProjectionMatrix();
    overlay.width = Wd * DPR; overlay.height = Hd * DPR; overlay.style.width = Wd + 'px'; overlay.style.height = Hd + 'px';
  }

  // ---------- Camera ----------
  var cam = { x: 0, z: 1, dist: 1, tx: 0, tz: 1, tdist: 1, yaw: 0, orbit: false };
  function fitDist() { var a = camera.aspect; return a >= 1.3 ? 27 : a >= 0.9 ? 33 : 42; }
  function setView(lane, instant) { cam.tx = LCX[lane]; cam.tz = 2.6; cam.tdist = fitDist() * (cam.zoom || 1); if (instant) { cam.x = cam.tx; cam.z = cam.tz; cam.dist = cam.tdist; } }
  function updateCam(dt) {
    var k = Math.min(1, dt * 5);
    cam.x += (cam.tx - cam.x) * k; cam.z += (cam.tz - cam.z) * k; cam.dist += (cam.tdist - cam.dist) * k;
    var pitch = 0.6, yaw = cam.orbit ? Math.sin(clock * 0.15) * 0.5 : 0;
    var cx = cam.x + Math.sin(yaw) * Math.cos(pitch) * cam.dist, cz = cam.z + Math.cos(yaw) * Math.cos(pitch) * cam.dist + 2.2;
    camera.position.set(cx, Math.sin(pitch) * cam.dist, cz);
    camera.lookAt(cam.x, 0, cam.z - 2.2);
    if (camShake > 0) { camShake -= dt; var s = camShake * 0.35; camera.position.x += (Math.random() - 0.5) * s; camera.position.y += (Math.random() - 0.5) * s; }
  }

  // ---------- Pick ----------
  var ray = new T.Raycaster(), ndc = new T.Vector2(), plane0 = new T.Plane(new T.Vector3(0, 1, 0), 0);
  function pick(px, py) {
    ndc.set(px / Wd * 2 - 1, -(py / Hd) * 2 + 1); ray.setFromCamera(ndc, camera);
    var hit = new T.Vector3(); if (!ray.ray.intersectPlane(plane0, hit)) return null;
    for (var lane = 0; lane < 2; lane++) {
      var x = hit.x - LCX[lane] + HL, y = 9 - hit.z;
      if (x >= -0.3 && x <= LW + 0.3) return { lane: lane, x: x, y: y, cx: Math.floor(x), cy: Math.floor(y) };
    }
    return { lane: -1, x: hit.x, y: hit.z };
  }

  function setGhost(type, cell, okk) {
    if (!type || !cell) { ghost.visible = false; return; }
    ghost.visible = true;
    if (ghostType !== type) {
      if (ghostMesh) ghost.remove(ghostMesh);
      ghostMesh = makeHuman(R.LOOK[type], { weapon: S.UNITS[type].weapon });
      ghostMesh.traverse(function (o) { if (o.isMesh) { o.material = o.material.clone(); o.material.transparent = true; o.material.opacity = 0.55; o.castShadow = false; } });
      ghost.add(ghostMesh); ghostType = type;
    }
    ghost.position.copy(W(0, cell.cx + 0.5, cell.cy + 0.5));
    ghost.userData.cell.material.color.set(okk ? '#69f0ae' : '#ff5252');
    var r = S.UNITS[type].range; ghost.userData.range.visible = r > 2; ghost.userData.range.scale.set(r, r, 1);
  }
  function setSelected(u) {
    if (!u) { selRing.visible = selRange.visible = false; return; }
    selRing.visible = true; selRing.position.copy(W(u.owner, u.x, u.y, 0.05));
    var r = S.stat(u, 'range'); selRange.visible = r > 2; selRange.position.copy(selRing.position); selRange.scale.set(r, r, 1);
  }

  // ---------- VẼ MỖI KHUNG ----------
  var prevT = 0;
  var fpsAcc = 0, fpsN = 0, fpsDone = false;
  function frame(G, alpha, dt, view) {
    clock += dt; var t = clock;
    if (!fpsDone && clock > 3) { fpsAcc += dt; fpsN++; if (fpsAcc > 4) { fpsDone = true; var fps = fpsN / fpsAcc; if (fps < 40 && DPR > 1) { DPR = 1; renderer.setPixelRatio(1); resize(); } if (fps < 28) { renderer.shadowMap.enabled = false; scene.traverse(function (o) { if (o.material) o.material.needsUpdate = true; }); } } }
    gridLines.forEach(function (gl, i) { gl.material.opacity = G.phase === 'build' && i === view.lane ? 0.45 + Math.sin(t * 3) * 0.12 : 0; });
    // tướng
    var seen = {};
    for (var i = 0; i < G.units.length; i++) {
      var u = G.units[i], v = visualUnit(u); seen[u.id] = 1;
      var pr = lerpPos(u, alpha), pos = W(u.owner, pr[0], pr[1]);
      if (v.userData.hidden > 0) { v.userData.hidden -= dt; v.visible = v.userData.hidden <= 0; if (v.visible) v.userData.pop = 0.0001; }
      v.position.copy(pos);
      var sb = (v.userData.scaleBase || 1) * 1.3;
      if (v.userData.pop > 0 && v.userData.pop < 1) { v.userData.pop = Math.min(1, v.userData.pop + dt * 3); var k = v.userData.pop, el = 1 + Math.sin(k * Math.PI * 2.5) * (1 - k) * 0.5; v.scale.setScalar(sb * k * el); } else v.scale.setScalar(sb);
      var tgt = u.tgt ? S.findCreep(G, u.tgt) : null, ang;
      if (tgt) ang = Math.atan2(tgt.x - u.x, -(tgt.y - u.y)) + 0; else ang = (u.moving ? Math.atan2((u.cx + 0.5 - u.x), -((u.cy + 0.5) - u.y)) : Math.PI);
      // sim y tăng -> z giảm; atan2(dx, dz) với dz = -(dy)
      if (!v.userData.card) faceTo(v, 1, tgt || u.moving ? ang : 0, dt);
      if (v.userData.a3) { A3.anim(v, { dead: u.dead, moving: u.moving && G.phase === 'fight', atk: u.atkAnim, cast: u._castT }, dt, t); }
      else if (v.userData.card) { CARDS.anim(v, { dead: u.dead, moving: u.moving && G.phase === 'fight', atk: u.atkAnim, cast: u._castT, face: tgt ? (tgt.x >= u.x ? 1 : -1) : (u.owner === 0 ? 1 : -1) }, dt, t, camera); }
      else if (v.userData.model) { animModel(v, { dead: u.dead, moving: u.moving && G.phase === 'fight', atk: u.atkAnim, cast: u._castT }, dt); }
      else if (u.dead) { v.userData.body.rotation.z = Math.min(1.5, (v.userData.body.rotation.z || 0) + dt * 6); }
      else v.userData.body.rotation.z = 0;
      v.userData.ring.material.opacity = u.active ? 0.75 : 0.3;
      if (u.moving && G.phase === 'fight' && Math.random() < 0.08) dustAt(v.position);
      if (!u.dead && !v.userData.model && !v.userData.card && !v.userData.a3) animHuman(v, { moving: u.moving && G.phase === 'fight', atk: u.atkAnim, ph: u.id }, t, dt);
      if (v.userData.aura) v.userData.aura.rotation.z = t * 1.5;
      if (v.userData.flag) v.userData.flag.rotation.y = Math.sin(t * 3 + u.id) * 0.35 - (u.moving ? 0.5 : 0);
      v.userData.dead = u.dead;
    }
    for (var id in VU) if (!seen[id]) { disposeObj(VU[id]); delete VU[id]; }
    // quái
    var seenC = {};
    for (var j = 0; j < G.creeps.length; j++) {
      var c = G.creeps[j]; if (c.hp <= 0) continue;
      var isNew = !VC[c.id]; var cv = visualCreep(c); seenC[c.id] = 1;
      if (isNew && Math.random() < 0.5) portalBurst(c.lane);
      if (c.moving && Math.random() < 0.06) dustAt(cv.position);
      var pc = lerpPos(c, alpha); cv.position.copy(W(c.lane, pc[0], pc[1]));
      var ut = c.tgt ? S.findUnit(G, c.tgt) : null;
      var ca = ut ? Math.atan2(ut.x - c.x, -(ut.y - c.y)) : (c.leaked ? Math.atan2(HL - c.x, -(17.4 - c.y)) : Math.PI);
      faceTo(cv, 1, ca, dt);
      if (cv.userData.beast) animBeast(cv, { moving: c.moving, atk: c.atkAnim }, t + c.id, dt); else if (cv.userData.model) animModel(cv, { moving: c.moving || c.leaked, atk: c.atkAnim }, dt); else animHuman(cv, { moving: c.moving, atk: c.atkAnim, ph: c.id }, t, dt);
      cv.userData.stun = c.stun > 0; cv.userData.poison = c.poisonT > 0; cv.userData.hp = c.hp / c.max; cv.userData.boss = S.CREEPS[c.type].boss;
      if (c.stun > 0 && Math.random() < 0.15) burst(W(c.lane, c.x, c.y, 1.1), '#fff59d', 1, 0.6, 0.12, 0.4, 0);
      if (c.poisonT > 0 && Math.random() < 0.12) burst(W(c.lane, c.x, c.y, 0.6), '#76ff03', 1, 0.6, 0.15, 0.5, -1);
    }
    for (var cid in VC) if (!seenC[cid]) { dieAnim(VC[cid]); delete VC[cid]; }
    // đạn
    var live = new Set();
    for (var k2 = 0; k2 < G.projs.length; k2++) {
      var p = G.projs[k2]; live.add(p);
      var pv = VP.get(p); if (!pv) { pv = projVisual(p); VP.set(p, pv); }
      var pp = lerpPos(p, alpha), h = 0.6;
      if (p.k === 'poisonbomb') { var kk = Math.min(1, (p.t + dt * alpha) / p.dur); pp = [p.sx + (p.tx - p.sx) * kk, p.sy + (p.ty - p.sy) * kk]; h = 0.6 + Math.sin(kk * Math.PI) * 2.2; }
      var wp = W(p.lane, pp[0], pp[1], h);
      if (pv.userData.dragon) { updateDragon(pv, wp, p, t); continue; }
      var dirx = (p.vx !== undefined) ? p.vx : (p.tx - p.x), diry = (p.vy !== undefined) ? p.vy : (p.ty - p.y);
      pv.position.copy(wp); pv.rotation.y = Math.atan2(diry, dirx); // trục x cục bộ hướng theo đường bay (sim y -> -z)
      if (pv.userData.orbit) pv.children.forEach(function (ch, ci) { if (ci > 0) { var a = t * 10 + ci * 2.1; ch.position.set(Math.cos(a) * 0.18, Math.sin(a) * 0.12, Math.sin(a) * 0.18); ch.rotation.y = a; } });
      if (pv.userData.trail) trailPuff(wp, pv.userData.trail, pv.userData.ts);
    }
    VP.forEach(function (v, p) { if (!live.has(p)) { disposeObj(v); VP.delete(p); } });
    // vùng độc
    var liveZ = new Set();
    G.zones.forEach(function (z) {
      liveZ.add(z); var zv = VZ.get(z);
      if (!zv) {
        zv = new T.Group();
        var d1 = new T.Mesh(G2('plane1', null), new T.MeshBasicMaterial({ map: smokeTex, color: '#76ff03', transparent: true, opacity: 0.8, blending: T.AdditiveBlending, depthWrite: false })); d1.rotation.x = -Math.PI / 2; d1.position.y = 0.08; zv.add(d1);
        var d2 = new T.Mesh(G2('plane1', null), new T.MeshBasicMaterial({ map: runeTex, color: '#aa00ff', transparent: true, opacity: 0.6, blending: T.AdditiveBlending, depthWrite: false })); d2.rotation.x = -Math.PI / 2; d2.position.y = 0.07; zv.add(d2);
        zv.position.copy(W(z.lane, z.x, z.y)); scene.add(zv); VZ.set(z, zv);
      }
      var s = z.r * 2.2, f = Math.min(1, (z.dur - z.t) * 4) * Math.min(1, z.t * 2);
      zv.children[0].scale.set(s, s, 1); zv.children[0].rotation.z = t * 0.7; zv.children[0].material.opacity = 0.8 * f;
      zv.children[1].scale.set(s * 0.95, s * 0.95, 1); zv.children[1].rotation.z = -t * 0.5; zv.children[1].material.opacity = 0.55 * f;
      if (Math.random() < 0.5) { var a = Math.random() * 6.28, r = Math.random() * z.r; var b = glowSprite('#b2ff59', 0.18, 0.9); b.position.copy(W(z.lane, z.x + Math.cos(a) * r, z.y + Math.sin(a) * r, 0.1)); addFX({ obj: b, t: 0, life: 0.9, up: function (f2, dt2, k) { f2.obj.position.y += dt2 * 0.9; f2.obj.material.opacity = 0.9 * (1 - k); } }); }
    });
    VZ.forEach(function (v, z) { if (!liveZ.has(z)) { disposeObj(v); VZ.delete(z); } });
    // linh vật
    mascots.forEach(function (m) { if (m) stepMascot(m, dt, t, G); });
    // FX
    for (var f = FX.length - 1; f >= 0; f--) {
      var F = FX[f]; F.t += dt; if (F.t < 0) { if (F.obj) F.obj.visible = false; continue; }
      if (F.obj) F.obj.visible = true;
      var kf = Math.min(1, F.t / F.life);
      F.up(F, dt, kf);
      if (F.t >= F.life) { if (F.end) F.end(); if (F.obj) { scene.remove(F.obj); if (F.disposeGroup) F.obj.traverse(function (o) { if (o.geometry && !isShared(o.geometry)) o.geometry.dispose(); if (o.material && o.material.dispose && !o.isSprite && F.dispose !== false) {} }); if (F.dispose && F.obj.material) F.obj.material.dispose(); } FX.splice(f, 1); }
    }
    // môi trường
    portals.forEach(function (p, i) { p.d1.rotation.z = t * 0.4; p.d2.rotation.z = -t * 0.7; p.beam.material.opacity = 0.1 + (G.phase === 'fight' ? 0.12 : 0) + Math.sin(t * 3) * 0.03; });
    gates.forEach(function (g) { g.flash.material.opacity *= 0.9; if (g.shake > 0) { g.shake -= dt; g.g.position.x = LCX[gates.indexOf(g)] + (Math.random() - 0.5) * g.shake * 0.3; } });
    LANT.forEach(function (l, i) { var s = (l.userData.s0 || (l.userData.s0 = l.scale.x)); var k = 1 + Math.sin(t * 6 + i * 1.7) * 0.06 + Math.sin(t * 13 + i) * 0.03; l.scale.set(s * k, s * k, 1); });
    FLAGS.forEach(function (fl, i) { fl.rotation.y = Math.sin(t * 2 + i) * 0.25; });
    var pa = petals.geometry.attributes.position;
    for (var q = 0; q < pa.count; q++) { var y = pa.getY(q) - dt * 0.5; var x = pa.getX(q) + Math.sin(t + q) * dt * 0.4 + dt * 0.25; if (y < 0) { y = 8 + Math.random() * 2; x = MX - 18 + Math.random() * 36; } pa.setY(q, y); pa.setX(q, x); }
    pa.needsUpdate = true;
    var wind = 0.55 + Math.sin(t * 0.35) * 0.3 + Math.sin(t * 1.3) * 0.15;
    windU.value = t * (0.8 + wind * 0.4);
    if (water) { water.material.uniforms.time.value = t * 0.45; }
    TREES.forEach(function (tr, i) { tr.rotation.z = Math.sin(t * 1.4 + i) * 0.025 * wind; tr.rotation.x = Math.cos(t * 1.1 + i) * 0.015 * wind; });
    WILLOWS.forEach(function (w, wi) { w.userData.strands.forEach(function (st, si) { st.rotation.x = Math.sin(t * 1.6 + si * 0.7 + wi) * 0.12 * wind; st.rotation.z = Math.cos(t * 1.2 + si) * 0.08 * wind; }); });
    stepAmbient(dt, t); stepNPCs(dt);
    SWAY.forEach(function (sw) { sw.o.rotation.x = Math.sin(t * 1.8 + sw.ph) * sw.a * wind; });
    LOTUS.forEach(function (lo, i) { if (lo.userData.drift) { lo.position.x += dt * lo.userData.drift; if (lo.position.x > MX + 36) lo.position.x = MX - 36; lo.position.y = -0.15 + Math.sin(t * 1.5 + i) * 0.03; } else if (lo.userData.boat) { lo.position.x = MX + 9 + Math.sin(t * 0.07) * 14; lo.rotation.z = Math.sin(t * 1.2) * 0.04; lo.position.y = -0.25 + Math.sin(t * 1.6) * 0.04; } else { lo.position.y = -0.27 + Math.sin(t * 1.3 + i * 0.7) * 0.02; lo.rotation.y += Math.sin(t * 0.5 + i) * 0.0008; } });
    updateCam(dt);
    composer.render();
    drawOverlay(G, view);
  }
  var sharedGeos = null;
  function isShared(g) { if (!sharedGeos) sharedGeos = new Set(); for (var k in geos) sharedGeos.add(geos[k]); return sharedGeos.has(g); }
  function disposeObj(o) { scene.remove(o); }
  function dieAnim(v) {
    if (v.userData.model) { playA(v, v.userData.A.die, 0.05); addFX({ obj: null, t: 0, life: 1.6, up: function (f, dt, k) { v.userData.mixer.update(dt); if (k > 0.6) v.position.y = -(k - 0.6) * 1.2; }, end: function () { scene.remove(v); } }); return; }
    addFX({ obj: null, t: 0, life: 0.7, up: function (f, dt, k) { v.rotation.z = k * 1.4; v.position.y = -k * 0.4; v.scale.multiplyScalar(0.995); }, end: function () { scene.remove(v); } });
  }
  function updateDragon(g, wp, p, t) {
    var H = g.userData.hist; H.unshift(wp.clone()); if (H.length > 40) H.pop();
    var segs = g.userData.segs, head = g.userData.head;
    head.position.copy(wp); head.position.y += Math.sin(t * 12) * 0.12;
    head.rotation.y = Math.atan2(p.vy, p.vx);
    for (var i = 0; i < segs.length; i++) { var h = H[Math.min(H.length - 1, (i + 1) * 2)]; segs[i].position.copy(h); segs[i].position.y += Math.sin(t * 12 - i * 0.6) * 0.15; }
    if (Math.random() < 0.9) burst(wp, '#ffd740', 2, 1.5, 0.2, 0.4, 0);
  }

  // ---------- Overlay 2D: thanh máu, chữ ----------
  var tmpV = new T.Vector3();
  function proj(p) { tmpV.copy(p).project(camera); return { x: (tmpV.x + 1) / 2 * Wd, y: (1 - tmpV.y) / 2 * Hd, vis: tmpV.z < 1 }; }
  function drawOverlay(G, view) {
    var g = octx; g.setTransform(DPR, 0, 0, DPR, 0, 0); g.clearRect(0, 0, Wd, Hd);
    // thanh máu quái
    for (var id in VC) {
      var v = VC[id]; if (v.userData.hp === undefined || v.userData.hp >= 0.999 && !v.userData.boss) continue;
      var sz = v.userData.size || 1, s = proj(tmpV.set(v.position.x, (v.userData.beast ? 1.05 * 1.45 : 2.0 * 0.9) * sz + 0.15, v.position.z));
      var w = v.userData.boss ? 54 : 26;
      g.fillStyle = 'rgba(0,0,0,0.6)'; g.fillRect(s.x - w / 2 - 1, s.y - 1, w + 2, 5);
      g.fillStyle = v.userData.poison ? '#9ccc65' : '#ff5252'; g.fillRect(s.x - w / 2, s.y, w * Math.max(0, v.userData.hp), 3);
    }
    for (var i = 0; i < G.units.length; i++) {
      var u = G.units[i]; if (u.dead || !u.active) continue; var mx = S.stat(u, 'hp'); if (u.hp >= mx) continue;
      var vu = VU[u.id]; if (!vu) continue; var s2 = proj(tmpV.set(vu.position.x, 2.05 * (vu.userData.scaleBase || 1), vu.position.z));
      g.fillStyle = 'rgba(0,0,0,0.6)'; g.fillRect(s2.x - 14, s2.y - 1, 28, 5); g.fillStyle = u.owner === 0 ? '#4fc3ff' : '#ffab40'; g.fillRect(s2.x - 13, s2.y, 26 * u.hp / mx, 3);
    }
    // sao vàng tướng nâng cấp
    // chữ nổi
    for (var k = TXT.length - 1; k >= 0; k--) {
      var tx = TXT[k]; tx.t += 1 / 60; var kk = tx.t / tx.life; if (kk >= 1) { TXT.splice(k, 1); continue; }
      var sp = proj(tmpV.set(tx.p.x, tx.p.y + tx.rise * kk, tx.p.z)); if (!sp.vis) continue;
      var sc = kk < 0.15 ? 0.6 + kk / 0.15 * 0.6 : kk < 0.3 ? 1.2 - (kk - 0.15) / 0.15 * 0.2 : 1;
      g.globalAlpha = kk > 0.7 ? (1 - kk) / 0.3 : 1;
      g.font = (tx.font ? '900 ' : '800 ') + Math.round(tx.z * sc) + 'px ' + (tx.font ? '"Playfair Display", serif' : '"Be Vietnam Pro", sans-serif');
      g.textAlign = 'center'; g.lineWidth = 3.5; g.strokeStyle = 'rgba(20,6,2,0.9)'; g.strokeText(tx.s, sp.x, sp.y); g.fillStyle = tx.c; g.fillText(tx.s, sp.x, sp.y);
      g.globalAlpha = 1;
    }
  }

  function screenOf(lane, x, y, h) { return proj(W(lane, x, y, h || 0)); }

  return { spawnNPCs: spawnNPCs, weapon3: weapon3, glowSprite: glowSprite, loadModels: loadModels, modelsReady: function () { return modelsReady; }, makeModel: makeModel, UNIT_MODEL: UNIT_MODEL, CREEP_MODEL: CREEP_MODEL, MASCOT_MODEL: MASCOT_MODEL, LW: LW, HL: HL, MX: MX, _VU: VU, init: init, resize: resize, frame: frame, onEvent: onEvent, setView: setView, cam: cam, pick: pick, setGhost: setGhost, setSelected: setSelected, initMascots: initMascots, mascots: mascots,
    screenOf: screenOf, fitDist: fitDist, W: W, LCX: LCX, renderIcon: null, cheer: function (p) { if (mascots[p]) mascots[p].cheer = 0.8; },
    makeHuman: makeHuman, makeBeast: makeBeast, makeMascot: makeMascot, getRenderer: function () { return renderer; }, getScene: function () { return scene; }, getCamera: function () { return camera; }, M: M, T: T };
})();
