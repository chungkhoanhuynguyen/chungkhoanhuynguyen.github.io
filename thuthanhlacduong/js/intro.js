// ===== MỞ ĐẦU CHƠI ĐƯỢC: điều khiển nhân vật đi trên phố hiện đại vào quán net, rồi xuyên không =====
var INTRO = (function () {
  var T = THREE, rr, sc, cam, cv, ui, me, raf = 0, done = null, keys = {}, joy = null, tgt = null, t0 = 0, portal = 0, last = 0, door, arrow, signs = [];
  var D = new T.Vector3(0, 0, -22);   // cửa quán net

  function tex(w, h, f) { var c = document.createElement('canvas'); c.width = w; c.height = h; f(c.getContext('2d'), w, h); var t = new T.CanvasTexture(c); t.anisotropy = 4; return t; }
  function box(w, h, d, col, x, y, z, em) { var m = new T.Mesh(new T.BoxGeometry(w, h, d), new T.MeshLambertMaterial({ color: col, emissive: em || 0 })); m.position.set(x, y, z); sc.add(m); return m; }
  function sign(txt, col, w, h, x, y, z, ry, font) {
    var t = tex(512, 128, function (g) { g.fillStyle = '#0b0b12'; g.fillRect(0, 0, 512, 128); g.font = font || '900 70px "Be Vietnam Pro",sans-serif'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.shadowColor = col; g.shadowBlur = 24; g.fillStyle = col; g.fillText(txt, 256, 68); g.shadowBlur = 0; g.fillStyle = '#fff'; g.globalAlpha = 0.85; g.fillText(txt, 256, 66); });
    var m = new T.Mesh(new T.PlaneGeometry(w, h), new T.MeshBasicMaterial({ map: t })); m.position.set(x, y, z); m.rotation.y = ry || 0; sc.add(m); signs.push(m); return m;
  }
  function build() {
    sc = new T.Scene(); sc.background = new T.Color('#0a0c1c'); sc.fog = new T.Fog('#0a0c1c', 25, 70);
    sc.add(new T.HemisphereLight('#7f8cff', '#1a1020', 0.55));
    var moon = new T.DirectionalLight('#9fb4ff', 0.45); moon.position.set(-10, 20, 10); sc.add(moon);
    // đường + vỉa hè
    var road = new T.Mesh(new T.PlaneGeometry(14, 80), new T.MeshLambertMaterial({ map: tex(64, 256, function (g) { g.fillStyle = '#26262c'; g.fillRect(0, 0, 64, 256); g.fillStyle = '#e8e8e8'; for (var y = 0; y < 256; y += 40) g.fillRect(30, y, 4, 22); }) }));
    road.material.map.wrapT = T.RepeatWrapping; road.material.map.repeat.set(1, 4); road.rotation.x = -Math.PI / 2; road.position.set(6, 0, -15); sc.add(road);
    var walk = new T.Mesh(new T.PlaneGeometry(8, 80), new T.MeshLambertMaterial({ map: tex(64, 64, function (g) { g.fillStyle = '#8a8478'; g.fillRect(0, 0, 64, 64); g.strokeStyle = '#6a655c'; for (var i = 0; i <= 64; i += 16) { g.beginPath(); g.moveTo(i, 0); g.lineTo(i, 64); g.moveTo(0, i); g.lineTo(64, i); g.stroke(); } }) }));
    walk.material.map.wrapS = walk.material.map.wrapT = T.RepeatWrapping; walk.material.map.repeat.set(4, 40); walk.rotation.x = -Math.PI / 2; walk.position.set(-5, 0.02, -15); sc.add(walk);
    box(0.3, 0.15, 80, '#bbb', -1, 0.07, -15);
    // dãy nhà phố
    var cols = ['#4a3f5a', '#3a4a5a', '#5a4a3a', '#3f5a4a', '#4a4a4a'];
    for (var i = 0; i < 9; i++) { var z = 12 - i * 6.5, h = 6 + (i * 37 % 5); box(6, h, 6, cols[i % 5], -12, h / 2, z);
      for (var f = 1; f < h - 1; f += 1.6) for (var k = -1; k <= 1; k++) box(0.05, 0.8, 1, Math.random() < 0.55 ? '#ffd27a' : '#20263a', -8.98, f, z + k * 1.7, Math.random() < 0.55 ? 0x553300 : 0);
      if (i !== 5) sign(['PHỞ 24', 'TẠP HOÁ', 'TRÀ SỮA', 'CẦM ĐỒ', 'KARAOKE', '', 'SPA', 'BIA HƠI', 'THUỐC'][i], ['#ff5252', '#40c4ff', '#ff80ab', '#ffd740', '#e040fb', '', '#69f0ae', '#ffab40', '#18ffff'][i], 4, 1, -8.9, 3.2, z, Math.PI / 2); }
    // bên kia đường
    for (var j = 0; j < 8; j++) { var z2 = 10 - j * 7, h2 = 7 + (j * 29 % 6); box(6, h2, 6, cols[(j + 2) % 5], 17, h2 / 2, z2); }
    // QUÁN NET
    box(6.2, 7.5, 6.2, '#1a1a2a', -12, 3.75, D.z);
    door = new T.Mesh(new T.PlaneGeometry(2, 2.6), new T.MeshBasicMaterial({ color: '#59a7ff' })); door.position.set(-8.88, 1.3, D.z); door.rotation.y = Math.PI / 2; sc.add(door);
    sign('NET 24H', '#4fa3ff', 4.8, 1.2, -8.85, 4.4, D.z, Math.PI / 2);
    var ban = tex(1024, 256, function (g) { var gr = g.createLinearGradient(0, 0, 0, 256); gr.addColorStop(0, '#b71c1c'); gr.addColorStop(1, '#4a0806'); g.fillStyle = gr; g.fillRect(0, 0, 1024, 256); g.strokeStyle = '#e8b04a'; g.lineWidth = 12; g.strokeRect(8, 8, 1008, 240); g.fillStyle = '#ffdf8a'; g.font = 'italic 900 110px "Playfair Display",serif'; g.textAlign = 'center'; g.fillText('Thủ Thành Lạc Dương', 512, 140); g.font = '700 34px "Be Vietnam Pro"'; g.fillStyle = '#fff'; g.fillText('Ai giữ được thành sẽ đổi được vận mệnh', 512, 210); });
    var bm = new T.Mesh(new T.PlaneGeometry(5.5, 1.4), new T.MeshBasicMaterial({ map: ban })); bm.position.set(-8.85, 2.9, D.z + 0.02); bm.rotation.y = Math.PI / 2; bm.position.x = -8.84; bm.position.y = 6.2; sc.add(bm);
    var dl = new T.PointLight('#4fa3ff', 2.5, 10); dl.position.set(-7.5, 2.5, D.z); sc.add(dl);
    // đèn đường + xe máy
    for (var q = 0; q < 6; q++) { var lz = 10 - q * 9; box(0.12, 5, 0.12, '#444', -1.3, 2.5, lz); box(1.2, 0.1, 0.25, '#555', -0.8, 5, lz); var pl = new T.PointLight('#ffcf8a', 1.3, 12); pl.position.set(-0.4, 4.8, lz); sc.add(pl); box(0.5, 0.1, 0.3, '#fff3c0', -0.3, 4.92, lz, 0xffcf8a); }
    for (var m2 = 0; m2 < 7; m2++) { var mz = 6 - m2 * 4.3, c3 = ['#c62828', '#1565c0', '#ffffff', '#212121'][m2 % 4]; box(0.5, 0.55, 1.6, c3, -2.3, 0.55, mz); box(0.15, 0.6, 0.15, '#333', -2.3, 1.0, mz - 0.65); box(0.12, 0.45, 0.45, '#111', -2.3, 0.25, mz + 0.6); box(0.12, 0.45, 0.45, '#111', -2.3, 0.25, mz - 0.6); }
    // mũi tên chỉ đường
    arrow = new T.Mesh(new T.ConeGeometry(0.4, 0.9, 4), new T.MeshBasicMaterial({ color: '#ffd740' })); arrow.rotation.x = Math.PI; sc.add(arrow);
    var ring = new T.Mesh(new T.RingGeometry(0.9, 1.15, 32), new T.MeshBasicMaterial({ color: '#4fa3ff', side: T.DoubleSide, transparent: true, opacity: 0.8 })); ring.rotation.x = -Math.PI / 2; ring.position.set(-7.6, 0.05, D.z); sc.add(ring); signs.push(ring);
    // nhân vật hiện đại (tự dựng)
    me = V.makeHuman({ skin: '#f1cba6', hair: '#141215', hat: 'topknot', robe: '#2b3346', robe2: '#e8e8e8', trim: '#4fa3ff', sash: '#222' }, {});
    me.scale.setScalar(1.05); me.position.set(-4, 0, 9); me.rotation.y = Math.PI; sc.add(me);
    cam = new T.PerspectiveCamera(55, 1, 0.1, 150);
  }
  function resize() { var w = innerWidth, h = innerHeight; rr.setSize(w, h, false); cam.aspect = w / h; cam.updateProjectionMatrix(); }
  function loop(now) {
    raf = requestAnimationFrame(loop); var dt = Math.min(0.05, (now - last) / 1000 || 0.016); last = now; var t = now / 1000;
    var mx = 0, mz = 0;
    if (keys.KeyW || keys.ArrowUp) mz -= 1; if (keys.KeyS || keys.ArrowDown) mz += 1; if (keys.KeyA || keys.ArrowLeft) mx -= 1; if (keys.KeyD || keys.ArrowRight) mx += 1;
    if (joy && joy.on) { mx += joy.dx; mz += joy.dy; }
    if (!mx && !mz && tgt) { var dx = tgt.x - me.position.x, dz = tgt.z - me.position.z, dd = Math.hypot(dx, dz); if (dd > 0.3) { mx = dx / dd; mz = dz / dd; } else tgt = null; }
    var len = Math.hypot(mx, mz), moving = len > 0.1 && !portal;
    if (moving) { mx /= Math.max(1, len); mz /= Math.max(1, len); me.position.x += mx * 6 * dt; me.position.z += mz * 6 * dt; me.rotation.y = Math.atan2(mx, mz); }
    me.position.x = Math.max(-8.4, Math.min(12, me.position.x)); me.position.z = Math.max(-50, Math.min(14, me.position.z));
    V.animHuman(me, { moving: moving, atk: 0, ph: 0 }, t, dt);
    // camera theo sau
    var cp = new T.Vector3(me.position.x + 4.5, 5.2, me.position.z + 7.5); cam.position.lerp(cp, Math.min(1, dt * 4)); cam.lookAt(me.position.x - 0.5, 1.2, me.position.z - 2);
    arrow.position.set(-7.6, 3 + Math.sin(t * 4) * 0.3, D.z); arrow.rotation.y = t * 2;
    signs.forEach(function (s, i) { if (s.material.opacity !== undefined && s.geometry.type === 'RingGeometry') s.scale.setScalar(1 + Math.sin(t * 3) * 0.08); });
    door.material.color.setHSL(0.6, 1, 0.5 + Math.sin(t * 5) * 0.15);
    var dist = Math.hypot(me.position.x - (-7.8), me.position.z - D.z);
    ui.hint.textContent = portal ? '' : dist < 6 ? 'Đi vào cửa quán NET 24H' : 'Đi tới quán NET 24H có băng rôn đỏ (theo mũi tên vàng)';
    if (dist < 1.3 && !portal) { portal = t; ui.flash.style.opacity = 1; try { Sfx.play('magic'); Sfx.play('thunder'); } catch (e) {} ui.cap.textContent = 'Màn hình loé sáng… một trận pháp tím kéo bạn vào trong!'; }
    if (portal) { me.rotation.y += dt * 12; me.position.y += dt * 0.6; cam.fov = Math.max(20, cam.fov - dt * 20); cam.updateProjectionMatrix(); if (t - portal > 2.2) finish(); }
    rr.render(sc, cam);
  }
  function finish() { if (!done) return; cancelAnimationFrame(raf); var f = done; done = null; removeEventListener('keydown', kd); removeEventListener('keyup', ku); removeEventListener('resize', resize); setTimeout(function () { ui.root.remove(); rr.dispose(); }, 600); ui.root.style.transition = 'opacity .6s'; ui.root.style.opacity = 0; f(); }
  function kd(e) { keys[e.code] = true; } function ku(e) { keys[e.code] = false; }
  function start(cb) {
    done = cb; portal = 0;
    var root = document.createElement('div'); root.style.cssText = 'position:fixed;inset:0;z-index:20;background:#000;touch-action:none';
    cv = document.createElement('canvas'); cv.style.cssText = 'position:absolute;inset:0;width:100%;height:100%'; root.appendChild(cv);
    var hint = document.createElement('div'); hint.style.cssText = 'position:absolute;top:14px;left:50%;transform:translateX(-50%);background:rgba(10,10,20,.75);border:1px solid #4fa3ff;color:#fff;padding:6px 14px;border-radius:20px;font:700 14px "Be Vietnam Pro";white-space:nowrap;pointer-events:none'; root.appendChild(hint);
    var cap = document.createElement('div'); cap.style.cssText = 'position:absolute;bottom:18%;left:0;right:0;text-align:center;color:#fff;font:700 18px "Be Vietnam Pro";text-shadow:0 2px 6px #000;pointer-events:none';
    cap.textContent = 'Hà Nội, 2 giờ sáng. Bạn đi tìm một quán net để chơi game…'; root.appendChild(cap);
    var flash = document.createElement('div'); flash.style.cssText = 'position:absolute;inset:0;background:radial-gradient(circle,#fff,#b388ff 30%,#311b92 70%);opacity:0;transition:opacity 1.6s;pointer-events:none'; root.appendChild(flash);
    var skip = document.createElement('button'); skip.textContent = 'Bỏ qua'; skip.style.cssText = 'position:absolute;top:12px;right:12px;min-height:40px;padding:0 14px;border-radius:8px;background:rgba(0,0,0,.5);border:1px solid #888;color:#fff;font:700 13px "Be Vietnam Pro"'; root.appendChild(skip);
    skip.onclick = function (e) { e.stopPropagation(); finish(); };
    var help = document.createElement('div'); help.style.cssText = 'position:absolute;bottom:12px;right:14px;color:#bbb;font:600 12px "Be Vietnam Pro";pointer-events:none;text-align:right'; help.innerHTML = 'Máy tính: W A S D / phím mũi tên · Điện thoại: kéo cần điều khiển<br>Hoặc chạm xuống mặt đất để đi tới đó'; root.appendChild(help);
    // cần điều khiển ảo
    var base = document.createElement('div'); base.style.cssText = 'position:absolute;left:28px;bottom:28px;width:120px;height:120px;border-radius:50%;background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.3)'; var knob = document.createElement('div'); knob.style.cssText = 'position:absolute;left:35px;top:35px;width:50px;height:50px;border-radius:50%;background:rgba(79,163,255,.7)'; base.appendChild(knob); root.appendChild(base);
    joy = { on: false, dx: 0, dy: 0 };
    base.addEventListener('pointerdown', function (e) { joy.on = true; base.setPointerCapture(e.pointerId); mv(e); e.stopPropagation(); });
    function mv(e) { if (!joy.on) return; var r = base.getBoundingClientRect(), x = e.clientX - r.left - 60, y = e.clientY - r.top - 60, l = Math.hypot(x, y), k = Math.min(1, 45 / (l || 1)); joy.dx = x / 45 * Math.min(1, l / 45) / Math.max(1, l / 45) ; joy.dy = y / 45 * Math.min(1, l / 45) / Math.max(1, l / 45); knob.style.left = (35 + x * k) + 'px'; knob.style.top = (35 + y * k) + 'px'; }
    base.addEventListener('pointermove', mv); base.addEventListener('pointerup', function () { joy.on = false; joy.dx = joy.dy = 0; knob.style.left = knob.style.top = '35px'; });
    // chạm để đi
    var ray = new T.Raycaster(), pl0 = new T.Plane(new T.Vector3(0, 1, 0), 0);
    cv.addEventListener('pointerdown', function (e) { var v = new T.Vector2(e.clientX / innerWidth * 2 - 1, -(e.clientY / innerHeight) * 2 + 1); ray.setFromCamera(v, cam); var h = new T.Vector3(); if (ray.ray.intersectPlane(pl0, h)) tgt = h; try { Sfx.init(); } catch (x) {} });
    document.body.appendChild(root); ui = { root: root, hint: hint, cap: cap, flash: flash };
    rr = new T.WebGLRenderer({ canvas: cv, antialias: true }); rr.setPixelRatio(Math.min(devicePixelRatio || 1, 1.5));
    build(); resize(); addEventListener('resize', resize); addEventListener('keydown', kd); addEventListener('keyup', ku);
    setTimeout(function () { if (!portal) cap.textContent = ''; }, 5000);
    last = performance.now(); raf = requestAnimationFrame(loop);
  }
  return { start: start, skip: function () { finish(); } };
})();
