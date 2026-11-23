// ===== ĐỒ HOẠ 2.5D ISOMETRIC — thành Lạc Dương =====
var R = (function () {
  var S = Sim;
  var HW = 32, HH = 16;                // nửa ô
  var LX = [0, 13];                    // độ lệch làn theo trục x thế giới
  var FLIP = 17;                       // y_render = FLIP - y_sim (quái đi từ gần -> xa, thành ở phía sau)
  function iso(wx, wy) { return { x: (wx - wy) * HW, y: (wx + wy) * HH }; }
  function L(lane, x, y) { return iso(LX[lane] + x, FLIP - y); }  // toạ độ sim -> pixel thế giới
  function depth(lane, x, y) { return LX[lane] + x + FLIP - y; }

  // ---------- sprite phát sáng (cache) ----------
  var glowCache = {};
  function glow(col) {
    if (glowCache[col]) return glowCache[col];
    var c = document.createElement('canvas'); c.width = c.height = 64; var g = c.getContext('2d');
    var gr = g.createRadialGradient(32, 32, 0, 32, 32, 32);
    gr.addColorStop(0, col); gr.addColorStop(0.25, col); gr.addColorStop(1, 'rgba(0,0,0,0)');
    g.globalAlpha = 1; g.fillStyle = gr; g.fillRect(0, 0, 64, 64);
    var c2 = document.createElement('canvas'); c2.width = c2.height = 64; var g2 = c2.getContext('2d');
    var gr2 = g2.createRadialGradient(32, 32, 0, 32, 32, 32);
    gr2.addColorStop(0, 'rgba(255,255,255,1)'); gr2.addColorStop(0.12, hexA(col, 0.95)); gr2.addColorStop(0.45, hexA(col, 0.35)); gr2.addColorStop(1, hexA(col, 0));
    g2.fillStyle = gr2; g2.fillRect(0, 0, 64, 64);
    glowCache[col] = c2; return c2;
  }
  function hexA(h, a) { var n = parseInt(h.slice(1), 16); return 'rgba(' + (n >> 16 & 255) + ',' + (n >> 8 & 255) + ',' + (n & 255) + ',' + a + ')'; }
  function shade(h, k) { var n = parseInt(h.slice(1), 16), r = n >> 16 & 255, g = n >> 8 & 255, b = n & 255;
    if (k < 0) { r *= 1 + k; g *= 1 + k; b *= 1 + k; } else { r += (255 - r) * k; g += (255 - g) * k; b += (255 - b) * k; }
    return 'rgb(' + (r | 0) + ',' + (g | 0) + ',' + (b | 0) + ')'; }
  function blit(ctx, col, x, y, r, a) { ctx.globalAlpha = a; ctx.drawImage(glow(col), x - r, y - r, r * 2, r * 2); }

  // seeded random cho cảnh tĩnh
  var srs = 7; function sr() { srs = (srs * 16807) % 2147483647; return (srs - 1) / 2147483646; }

  // ---------- CẢNH NỀN (vẽ 1 lần) ----------
  var BG = null, BGS = 1.25, BOX = { x0: -1150, y0: -420, w: 2450, h: 1360 };
  function diamond(g, cx, cy, w, h) { g.beginPath(); g.moveTo(cx, cy - h); g.lineTo(cx + w, cy); g.lineTo(cx, cy + h); g.lineTo(cx - w, cy); g.closePath(); }
  function tile(g, wx, wy, col, line) {
    var p = iso(wx + 0.5, wy + 0.5); diamond(g, p.x, p.y, HW, HH); g.fillStyle = col; g.fill();
    if (line) { g.strokeStyle = line; g.lineWidth = 1; g.stroke(); }
  }
  function quad(g, pts, fill, stroke) { g.beginPath(); g.moveTo(pts[0].x, pts[0].y); for (var i = 1; i < pts.length; i++) g.lineTo(pts[i].x, pts[i].y); g.closePath(); if (fill) { g.fillStyle = fill; g.fill(); } if (stroke) { g.strokeStyle = stroke; g.stroke(); } }
  function up(p, h) { return { x: p.x, y: p.y - h }; }

  // Nhà mái ngói đỏ cong kiểu cổ: x,y góc, w (theo x), d (theo y), wallH, roofH
  function building(g, x, y, w, d, wallH, roofH, opt) {
    opt = opt || {};
    var wallC = opt.wall || '#e9dcc3', pillar = opt.pillar || '#8e1b14', roof = opt.roof || '#c0392b';
    var A = iso(x, y), B = iso(x + w, y), C = iso(x + w, y + d), D = iso(x, y + d);
    // nền bệ đá
    var base = 6;
    quad(g, [up(D, 0), up(C, 0), up(C, base), up(D, base)], '#9a8f80');
    quad(g, [up(B, 0), up(C, 0), up(C, base), up(B, base)], '#b5aa98');
    // tường mặt trước-trái (D-C) và phải (B-C)
    var h = wallH + base;
    var gl = g.createLinearGradient(0, D.y - h, 0, D.y);
    gl.addColorStop(0, shade(wallC, -0.25)); gl.addColorStop(1, shade(wallC, -0.05));
    quad(g, [up(D, base), up(C, base), up(C, h), up(D, h)], gl);
    quad(g, [up(B, base), up(C, base), up(C, h), up(B, h)], shade(wallC, -0.32));
    // cột đỏ + cửa sổ
    var n = Math.max(2, Math.round(w)), m = Math.max(2, Math.round(d));
    g.lineWidth = 3; g.strokeStyle = pillar;
    for (var i = 0; i <= n; i++) { var t = i / n, P = { x: D.x + (C.x - D.x) * t, y: D.y + (C.y - D.y) * t }; g.beginPath(); g.moveTo(P.x, P.y - base); g.lineTo(P.x, P.y - h); g.stroke(); }
    for (var j = 0; j <= m; j++) { var t2 = j / m, Q = { x: B.x + (C.x - B.x) * t2, y: B.y + (C.y - B.y) * t2 }; g.beginPath(); g.moveTo(Q.x, Q.y - base); g.lineTo(Q.x, Q.y - h); g.stroke(); }
    // ô cửa lưới
    g.lineWidth = 1;
    for (var k = 0; k < n; k++) {
      var t3 = (k + 0.5) / n, P2 = { x: D.x + (C.x - D.x) * t3, y: D.y + (C.y - D.y) * t3 };
      var ww = (C.x - D.x) / n * 0.32;
      g.fillStyle = k === (n >> 1) && opt.door ? '#3b120c' : 'rgba(120,30,20,0.55)';
      g.beginPath(); g.moveTo(P2.x - ww, P2.y - ww * 0.5 - base - 2); g.lineTo(P2.x + ww, P2.y + ww * 0.5 - base - 2);
      g.lineTo(P2.x + ww, P2.y + ww * 0.5 - h * 0.78); g.lineTo(P2.x - ww, P2.y - ww * 0.5 - h * 0.78); g.closePath(); g.fill();
      g.strokeStyle = 'rgba(255,220,150,0.35)'; g.stroke();
    }
    // xà ngang
    g.strokeStyle = pillar; g.lineWidth = 4;
    g.beginPath(); g.moveTo(D.x, D.y - h); g.lineTo(C.x, C.y - h); g.lineTo(B.x, B.y - h); g.stroke();
    // MÁI: tràn ra ngoài, góc vểnh
    var o = 0.55, ex = function (px, py) { return iso(px, py); };
    var a = ex(x - o, y - o), b = ex(x + w + o, y - o), c = ex(x + w + o, y + d + o), dd = ex(x - o, y + d + o);
    var rh = h + 2, top = h + roofH;
    var r1 = w >= d ? ex(x + w * 0.22, y + d / 2) : ex(x + w / 2, y + d * 0.22), r2 = w >= d ? ex(x + w * 0.78, y + d / 2) : ex(x + w / 2, y + d * 0.78);
    var Ar = up(a, rh), Br = up(b, rh), Cr = up(c, rh), Dr = up(dd, rh), R1 = up(r1, top), R2 = up(r2, top);
    var curl = 9;
    function roofFace(p1, p2, q1, q2, col) {
      g.beginPath(); g.moveTo(p1.x, p1.y - curl);
      g.quadraticCurveTo((p1.x + p2.x) / 2, (p1.y + p2.y) / 2 + 4, p2.x, p2.y - curl);
      g.lineTo(q2.x, q2.y); g.lineTo(q1.x, q1.y); g.closePath(); g.fillStyle = col; g.fill();
    }
    var w1 = w >= d;
    // mặt sau trước để mặt trước đè lên
    roofFace(Ar, Br, w1 ? R1 : R1, w1 ? R2 : R1, shade(roof, -0.35));
    roofFace(Ar, Dr, R1, w1 ? R1 : R2, shade(roof, -0.15));
    var rg = g.createLinearGradient(0, R1.y, 0, Dr.y);
    rg.addColorStop(0, shade(roof, 0.1)); rg.addColorStop(1, shade(roof, -0.12));
    roofFace(Dr, Cr, w1 ? R1 : R2, w1 ? R2 : R2, rg);
    roofFace(Br, Cr, w1 ? R2 : R1, R2, shade(roof, -0.3));
    // sọc ngói
    g.strokeStyle = 'rgba(70,10,5,0.35)'; g.lineWidth = 1;
    for (var s = 1; s < 14; s++) {
      var t4 = s / 14, E = { x: Dr.x + (Cr.x - Dr.x) * t4, y: Dr.y + (Cr.y - Dr.y) * t4 - curl * (1 - Math.abs(t4 - 0.5) * 2) * 0.2 };
      var Rt = w1 ? { x: R1.x + (R2.x - R1.x) * t4, y: R1.y + (R2.y - R1.y) * t4 } : R2;
      g.beginPath(); g.moveTo(E.x, E.y); g.lineTo(Rt.x, Rt.y); g.stroke();
    }
    // nóc + đầu đao vàng
    g.strokeStyle = '#5a0c07'; g.lineWidth = 5; g.beginPath(); g.moveTo(R1.x, R1.y); g.lineTo(R2.x, R2.y); g.stroke();
    g.strokeStyle = '#e8b04a'; g.lineWidth = 1.5; g.beginPath(); g.moveTo(R1.x, R1.y - 2); g.lineTo(R2.x, R2.y - 2); g.stroke();
    [R1, R2].forEach(function (R) { g.fillStyle = '#e8b04a'; g.beginPath(); g.moveTo(R.x - 4, R.y); g.quadraticCurveTo(R.x - 8, R.y - 12, R.x - 1, R.y - 14); g.quadraticCurveTo(R.x - 3, R.y - 6, R.x + 2, R.y); g.fill(); });
    [Ar, Br, Cr, Dr].forEach(function (P) { g.strokeStyle = '#5a0c07'; g.lineWidth = 3; g.beginPath(); g.moveTo(P.x, P.y - curl); g.quadraticCurveTo(P.x, P.y - curl - 6, P.x + (P.x > R1.x ? 5 : -5), P.y - curl - 9); g.stroke(); });
    // đèn lồng treo mái
    if (opt.lanterns !== false) for (var li = 0; li < n; li++) {
      var t5 = (li + 0.5) / n, Lp = { x: Dr.x + (Cr.x - Dr.x) * t5, y: Dr.y + (Cr.y - Dr.y) * t5 + 6 };
      lantern(g, Lp.x, Lp.y, 1);
      LANTERNS.push({ x: Lp.x, y: Lp.y + 6 });
    }
  }
  function lantern(g, x, y, s) {
    g.strokeStyle = '#3a1a0a'; g.lineWidth = 1; g.beginPath(); g.moveTo(x, y - 4); g.lineTo(x, y); g.stroke();
    var gr = g.createRadialGradient(x - 1, y + 5, 1, x, y + 6, 6 * s);
    gr.addColorStop(0, '#ffe08a'); gr.addColorStop(0.5, '#ff5a2a'); gr.addColorStop(1, '#a3150c');
    g.fillStyle = gr; g.beginPath(); g.ellipse(x, y + 6 * s, 4.5 * s, 6 * s, 0, 0, 6.283); g.fill();
    g.fillStyle = '#e8b04a'; g.fillRect(x - 2.5 * s, y, 5 * s, 1.5 * s); g.fillRect(x - 2.5 * s, y + 11.5 * s, 5 * s, 1.5 * s);
  }
  var LANTERNS = [], TREES = [], POSTS = [];
  function tree(g, wx, wy, sc, blossom) {
    var p = iso(wx, wy);
    g.fillStyle = 'rgba(40,20,10,0.25)'; g.beginPath(); g.ellipse(p.x, p.y, 26 * sc, 12 * sc, 0, 0, 6.283); g.fill();
    g.strokeStyle = '#4a2a18'; g.lineWidth = 5 * sc; g.lineCap = 'round';
    g.beginPath(); g.moveTo(p.x, p.y); g.quadraticCurveTo(p.x - 4 * sc, p.y - 20 * sc, p.x + 2 * sc, p.y - 36 * sc); g.stroke();
    g.lineWidth = 2.5 * sc; g.beginPath(); g.moveTo(p.x, p.y - 22 * sc); g.lineTo(p.x - 14 * sc, p.y - 34 * sc); g.moveTo(p.x + 1, p.y - 28 * sc); g.lineTo(p.x + 15 * sc, p.y - 38 * sc); g.stroke();
    var cols = blossom ? ['#e2344a', '#ff6f7d', '#b71c35', '#ff9aa6'] : ['#2e6b3a', '#3f8a4a', '#24572f', '#5aa860'];
    for (var i = 0; i < 26; i++) {
      var a = sr() * 6.283, r = sr() * 22 * sc;
      g.fillStyle = cols[i % 4]; g.globalAlpha = 0.85;
      g.beginPath(); g.arc(p.x + Math.cos(a) * r * 1.2, p.y - 40 * sc + Math.sin(a) * r * 0.75, (5 + sr() * 6) * sc, 0, 6.283); g.fill();
    }
    g.globalAlpha = 1;
  }
  function post(g, wx, wy) {
    var p = iso(wx, wy);
    g.fillStyle = '#6d5f50'; g.fillRect(p.x - 3, p.y - 26, 6, 26);
    g.fillStyle = '#8c7d6c'; g.fillRect(p.x - 5, p.y - 30, 10, 5);
    g.fillStyle = '#4a3f35'; g.fillRect(p.x - 6, p.y - 36, 12, 4);
    lantern(g, p.x, p.y - 30, 0.9); LANTERNS.push({ x: p.x, y: p.y - 24 });
  }
  function gateTower(g, lane) {
    var x0 = LX[lane] + 0.6, y0 = -3.6;
    // tường thành
    var A = iso(x0 - 0.6, y0 + 1.3), B = iso(x0 + 8.4, y0 + 1.3);
    var wallH = 46;
    var Bk = iso(x0 + 8.4, y0 - 0.2);
    quad(g, [A, B, up(B, wallH), up(A, wallH)], '#8a7d6c');
    quad(g, [B, Bk, up(Bk, wallH), up(B, wallH)], '#6e6355');
    for (var i = 0; i <= 10; i++) { var t = i / 10, P = { x: A.x + (B.x - A.x) * t, y: A.y + (B.y - A.y) * t }; g.fillStyle = '#7a6e5f'; g.fillRect(P.x - 5, P.y - wallH - 8, 10, 8); }
    g.strokeStyle = 'rgba(40,30,20,0.3)'; for (var r = 1; r < 6; r++) { g.beginPath(); g.moveTo(A.x, A.y - r * 8); g.lineTo(B.x, B.y - r * 8); g.stroke(); }
    // cổng vòm
    var M = iso(x0 + 3.9, y0 + 1.3);
    g.fillStyle = '#2a0d08'; g.beginPath(); g.moveTo(M.x - 22, M.y - 11); g.lineTo(M.x + 18, M.y + 9); g.lineTo(M.x + 18, M.y + 9 - 30); g.quadraticCurveTo(M.x - 2, M.y - 46, M.x - 22, M.y - 41); g.closePath(); g.fill();
    g.strokeStyle = '#c9a24a'; g.lineWidth = 2; g.stroke();
    // lầu trên cổng
    building(g, x0 + 1.7, y0 - 0.4, 4.4, 1.6, 26, 30, { wall: '#d9c7a6', door: false });
    // biển hiệu
    var Pz = iso(x0 + 3.9, y0 + 1.25);
    g.fillStyle = '#1b2a4a'; g.fillRect(Pz.x - 22, Pz.y - 64, 44, 14); g.strokeStyle = '#e8b04a'; g.lineWidth = 1.5; g.strokeRect(Pz.x - 22, Pz.y - 64, 44, 14);
    g.fillStyle = '#f3d27a'; g.font = 'bold 9px "Playfair Display", serif'; g.textAlign = 'center'; g.fillText(lane === 0 ? 'LẠC DƯƠNG' : 'BIỆN KINH', Pz.x, Pz.y - 54);
    // cờ
    [iso(x0 - 0.4, y0 + 1.3), iso(x0 + 8.2, y0 + 1.3)].forEach(function (F) {
      g.strokeStyle = '#3a2a1a'; g.lineWidth = 2; g.beginPath(); g.moveTo(F.x, F.y - wallH); g.lineTo(F.x, F.y - wallH - 40); g.stroke();
      g.fillStyle = lane === 0 ? '#2f6fd0' : '#c62828'; g.beginPath(); g.moveTo(F.x, F.y - wallH - 40); g.lineTo(F.x + 22, F.y - wallH - 34); g.lineTo(F.x, F.y - wallH - 26); g.fill();
    });
  }

  function buildBG() {
    LANTERNS = []; srs = 7;
    BG = document.createElement('canvas'); BG.width = Math.round(BOX.w * BGS); BG.height = Math.round(BOX.h * BGS);
    var g = BG.getContext('2d'); g.scale(BGS, BGS); g.translate(-BOX.x0, -BOX.y0);
    // trời/nền xa
    var sky = g.createLinearGradient(0, BOX.y0, 0, BOX.y0 + BOX.h); sky.addColorStop(0, '#3a2a22'); sky.addColorStop(1, '#5a4636');
    g.fillStyle = sky; g.fillRect(BOX.x0, BOX.y0, BOX.w, BOX.h);
    // sân lát đá toàn cảnh
    for (var wy = -12; wy < 27; wy++) for (var wx = -10; wx < 33; wx++) {
      var v = sr();
      var c = v < 0.33 ? '#cbbfac' : v < 0.66 ? '#c4b8a5' : '#d2c7b5';
      if ((wx + wy) % 7 === 0) c = '#bdb19e';
      tile(g, wx, wy, c, 'rgba(90,75,60,0.28)');
    }
    // lối đi đá lớn quanh
    for (var lane = 0; lane < 2; lane++) {
      var ox = LX[lane];
      for (var y = -1; y < 19; y++) for (var x = 0; x < 9; x++) {
        var simY = FLIP - y - 0.5; // y render -> sim
        var col;
        if (simY >= 14.5 || y < 2) col = ((x + y) & 1) ? '#b9a48c' : '#b19b82';            // cấm địa sát thành
        else if (simY < 1.5) col = ((x + y) & 1) ? '#7d3b33' : '#74342c';                  // bãi xuất quân
        else col = ((x + y) & 1) ? '#ebe2d2' : '#e2d8c6';                                  // khu xây
        tile(g, ox + x, y, col, 'rgba(110,90,70,0.35)');
      }
      // thảm đỏ giữa đường về thành
      for (var y2 = -1; y2 < 3; y2++) for (var x2 = 3; x2 < 6; x2++) tile(g, ox + x2, y2, x2 === 4 ? '#a3241a' : '#8b1d15', 'rgba(232,176,74,0.5)');
      // bờ đá nổi hai bên làn
      [[0, -1, 0, 18.2], [9, -1, 9, 18.2]].forEach(function (e) {
        var P1 = iso(ox + e[0], e[1]), P2 = iso(ox + e[2], e[3]);
        quad(g, [P1, P2, up(P2, 7), up(P1, 7)], e[0] === 0 ? '#9c8f7c' : '#8a7e6c');
        g.strokeStyle = '#efe6d4'; g.lineWidth = 1.5; g.beginPath(); g.moveTo(P1.x, P1.y - 7); g.lineTo(P2.x, P2.y - 7); g.stroke();
      });
      // trận pháp xuất quân (gần người xem)
      var SP = iso(ox + 4.5, 17.7);
      for (var rr = 4; rr > 0; rr--) { g.strokeStyle = rr % 2 ? 'rgba(160,40,200,0.55)' : 'rgba(255,90,60,0.5)'; g.lineWidth = 2; g.beginPath(); g.ellipse(SP.x, SP.y, rr * 34, rr * 17, 0, 0, 6.283); g.stroke(); }
      for (var k = 0; k < 8; k++) { var a = k / 8 * 6.283; g.fillStyle = 'rgba(255,120,80,0.6)'; g.beginPath(); g.arc(SP.x + Math.cos(a) * 120, SP.y + Math.sin(a) * 60, 3, 0, 6.283); g.fill(); }
      gateTower(g, lane);
    }
    // giải phân cách: vườn giữa hai làn
    for (var y3 = -1; y3 < 19; y3++) for (var x3 = 9; x3 < 13; x3++) tile(g, x3, y3, ((x3 + y3) & 1) ? '#6e8a4a' : '#668244', 'rgba(40,60,30,0.35)');
    for (var y4 = 0; y4 < 18; y4 += 3) { post(g, 9.6, y4 + 0.5); post(g, 12.4, y4 + 2); }
    for (var y5 = 1; y5 < 18; y5 += 4) tree(g, 11, y5 + 0.5, 0.95, true);
    // nhà hai bên (trái: x<0, phải: x>22) và dãy cung điện phía sau
    building(g, -6.5, -9, 5, 3.2, 34, 34, { door: true });
    building(g, -5.6, -3.5, 3.6, 3.4, 30, 28);
    building(g, -5.8, 2.5, 3.6, 3.6, 28, 28, { door: true });
    building(g, -5.6, 8.6, 3.6, 3.4, 30, 30);
    building(g, -5.8, 14.6, 3.6, 3.6, 26, 26);
    building(g, 24.6, -3.5, 3.4, 3.4, 26, 26);
    building(g, 24.8, 2.5, 3.4, 3.6, 28, 28, { door: true });
    building(g, 24.6, 8.6, 3.4, 3.4, 26, 26);
    building(g, 24.8, 14.6, 3.4, 3.6, 24, 24);
    building(g, 8.2, -10.5, 6.6, 4.4, 48, 46, { door: true, wall: '#f0e2c6' });   // điện chính giữa
    building(g, 1, -11, 5.5, 3, 34, 34);
    building(g, 17, -11, 5.5, 3, 34, 34);
    tree(g, -1.5, 5.8, 1.0, true); tree(g, -1.6, 12, 0.9, false); tree(g, 23.6, 6, 1.0, false); tree(g, 23.8, 12.2, 0.9, true);
    tree(g, 7.2, -6.2, 1.1, true); tree(g, 15.6, -6.2, 1.1, true);
    // dây đèn lồng giăng qua sân sau
    for (var s2 = 0; s2 < 2; s2++) {
      var P1 = iso(-1 + s2 * 13, -5.5), P2 = iso(11.5 + s2 * 13, -5.5);
      g.strokeStyle = 'rgba(60,30,15,0.7)'; g.lineWidth = 1; g.beginPath(); g.moveTo(P1.x, P1.y - 60); g.quadraticCurveTo((P1.x + P2.x) / 2, (P1.y + P2.y) / 2 - 30, P2.x, P2.y - 60); g.stroke();
      for (var q = 1; q < 12; q++) { var t = q / 12, mx = P1.x + (P2.x - P1.x) * t, my = P1.y - 60 + (P2.y - P1.y) * t + Math.sin(t * Math.PI) * 30 - 0; my = (1 - t) * (1 - t) * (P1.y - 60) + 2 * (1 - t) * t * ((P1.y + P2.y) / 2 - 30) + t * t * (P2.y - 60); lantern(g, mx, my, 0.7); LANTERNS.push({ x: mx, y: my + 4 }); }
    }
    // làm tối viền ngoài (vignette)
    var vg = g.createRadialGradient(-100, 250, 300, -100, 250, 1300); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(20,8,4,0.55)');
    g.fillStyle = vg; g.fillRect(BOX.x0, BOX.y0, BOX.w, BOX.h);
  }

  // ---------- NHÂN VẬT ----------
  var LOOK = {
    thienvuong: { skin: '#f0c9a0', hair: '#2a1a10', hat: 'helmet', robe: '#c8941e', robe2: '#6b3f10', trim: '#ffe08a' },
    thieulam: { skin: '#f0c49a', hair: null, hat: 'bald', robe: '#e8a33d', robe2: '#9a3c0c', trim: '#c0392b', sash: '#c0392b' },
    duongmon: { skin: '#eac39d', hair: '#151515', hat: 'hood', robe: '#2e7d5b', robe2: '#0f3324', trim: '#c9e6b0', mask: true },
    ngudoc: { skin: '#e7c0a0', hair: '#1a0f20', hat: 'headdress', robe: '#6a3d9a', robe2: '#24103a', trim: '#b3ff6a' },
    ngamy: { skin: '#f6d5bd', hair: '#120c0c', hat: 'longhair', robe: '#f06292', robe2: '#ffffff', trim: '#ffd1e3', female: true },
    vodang: { skin: '#efc8a2', hair: '#161616', hat: 'topknot', robe: '#4a90d9', robe2: '#e9f2ff', trim: '#ffffff' },
    conlon: { skin: '#eec5a0', hair: '#202020', hat: 'taoist', robe: '#00acc1', robe2: '#08333b', trim: '#ffeb3b' },
    caibang: { skin: '#d9a77c', hair: '#3a2612', hat: 'messy', robe: '#8d6e63', robe2: '#4e342e', trim: '#7cb342', patches: true }
  };
  var CLOOK = {
    sontac: { skin: '#d9a77c', hair: '#2a1a10', hat: 'bandana', robe: '#7a5a44', robe2: '#3d2a1e', trim: '#b23a2a', weapon: 'saber' },
    cungtac: { skin: '#d9a77c', hair: '#2a1a10', hat: 'bandana', robe: '#5d6b3a', robe2: '#2c3319', trim: '#a08050', weapon: 'bow' },
    thietgiap: { skin: '#cfa27a', hair: '#222', hat: 'ironhelm', robe: '#6c7a86', robe2: '#2d353d', trim: '#a9b6c0', weapon: 'shield', armor: true },
    trai_chu: { skin: '#b98a66', hair: '#111', hat: 'ironhelm', robe: '#2f3a44', robe2: '#101418', trim: '#c0392b', weapon: 'axe', armor: true },
    huyetma: { skin: '#c97c6e', hair: '#5a0000', hat: 'horns', robe: '#8e0000', robe2: '#2a0000', trim: '#ff5252', weapon: 'saber', aura: '#ff1744' },
    mavuong: { skin: '#b9a0c8', hair: '#120020', hat: 'horns', robe: '#4a148c', robe2: '#12002a', trim: '#e040fb', weapon: 'axe', aura: '#d500f9' },
    hacy: { skin: '#d9a77c', hair: '#000', hat: 'hood', robe: '#1f1f1f', robe2: '#050505', trim: '#b71c1c', weapon: 'saber', mask: true },
    matang: { skin: '#d9a07a', hair: null, hat: 'bald', robe: '#880e4f', robe2: '#3a0020', trim: '#ffd54f', weapon: 'staff', sash: '#ffd54f' }
  };

  // vẽ người: (x,y) = điểm chân, sc tỉ lệ, o: tuỳ chọn
  function human(ctx, x, y, sc, lk, o) {
    var f = o.face || 1, wk = o.walk || 0, at = o.atk || 0;
    ctx.save(); ctx.translate(x, y); ctx.scale(sc * f, sc);
    if (o.alpha !== undefined) ctx.globalAlpha = o.alpha;
    var bob = o.moving ? Math.abs(Math.sin(wk)) * 2 : Math.sin((o.t || 0) * 2) * 0.6;
    // chân
    ctx.strokeStyle = shade(lk.robe2, -0.4); ctx.lineWidth = 3.4; ctx.lineCap = 'round';
    var l1 = o.moving ? Math.sin(wk) * 4 : 0;
    ctx.beginPath(); ctx.moveTo(-3, -12); ctx.lineTo(-3 + l1, -1); ctx.moveTo(3, -12); ctx.lineTo(3 - l1, -1); ctx.stroke();
    ctx.translate(0, -bob);
    // áo choàng sau (tướng nâng cấp / linh vật)
    if (o.cape) {
      ctx.fillStyle = o.cape; ctx.beginPath(); ctx.moveTo(-6, -29); ctx.quadraticCurveTo(-14 - Math.sin((o.t || 0) * 3) * 2, -14, -10, -3); ctx.lineTo(6, -6); ctx.lineTo(6, -29); ctx.closePath(); ctx.fill();
    }
    // tay sau
    ctx.strokeStyle = shade(lk.robe, -0.25); ctx.lineWidth = 4;
    ctx.beginPath(); ctx.moveTo(-5, -27); ctx.lineTo(-8, -18); ctx.stroke();
    // thân áo
    var gr = ctx.createLinearGradient(0, -31, 0, -6); gr.addColorStop(0, lk.robe); gr.addColorStop(1, shade(lk.robe, -0.3));
    ctx.fillStyle = gr; ctx.beginPath(); ctx.moveTo(-6.5, -30); ctx.lineTo(6.5, -30); ctx.lineTo(lk.female ? 11 : 9, -6); ctx.quadraticCurveTo(0, -3.5, lk.female ? -11 : -9, -6); ctx.closePath(); ctx.fill();
    ctx.fillStyle = lk.robe2; ctx.beginPath(); ctx.moveTo(-1.5, -30); ctx.lineTo(1.5, -30); ctx.lineTo(4, -6); ctx.lineTo(-1, -5); ctx.closePath(); ctx.fill();
    if (lk.armor) { ctx.fillStyle = lk.trim; for (var i = 0; i < 3; i++) ctx.fillRect(-6, -27 + i * 6, 12, 2); }
    if (lk.patches) { ctx.fillStyle = '#5d4037'; ctx.fillRect(-6, -14, 4, 4); ctx.fillStyle = '#827717'; ctx.fillRect(3, -22, 3, 4); }
    ctx.fillStyle = lk.sash || lk.trim; ctx.fillRect(-6.5, -19, 13, 2.6);
    ctx.strokeStyle = lk.trim; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(-6.5, -30); ctx.lineTo(0, -24); ctx.lineTo(6.5, -30); ctx.stroke();
    // đầu
    ctx.fillStyle = lk.skin; ctx.beginPath(); ctx.arc(0, -36, 6.3, 0, 6.283); ctx.fill();
    hat(ctx, lk, o);
    if (lk.mask) { ctx.fillStyle = shade(lk.robe, -0.3); ctx.fillRect(-1, -35, 7.5, 4); }
    ctx.fillStyle = '#1a1010'; ctx.fillRect(2.2, -37.5, 1.6, 1.8); ctx.fillRect(5.2, -37.5, 1.4, 1.8);
    // tay trước + vũ khí
    var ang = -0.5 + at * 2.4;
    ctx.save(); ctx.translate(4, -27); ctx.rotate(ang);
    ctx.strokeStyle = shade(lk.robe, -0.1); ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, 9); ctx.stroke();
    ctx.fillStyle = lk.skin; ctx.beginPath(); ctx.arc(0, 10, 2, 0, 6.283); ctx.fill();
    ctx.translate(0, 10); weapon(ctx, o.weapon || lk.weapon, o);
    ctx.restore();
    ctx.restore();
  }
  function hat(ctx, lk, o) {
    var h = lk.hat, t = o.t || 0;
    ctx.fillStyle = lk.hair || '#222';
    switch (h) {
      case 'bald': ctx.fillStyle = shade(lk.skin, 0.15); ctx.beginPath(); ctx.arc(-1, -39, 3, 0, 6.283); ctx.fill(); ctx.fillStyle = '#7a4a2a'; for (var i = 0; i < 3; i++) ctx.fillRect(-4 + i * 3, -42, 1.2, 1.2); break;
      case 'helmet': ctx.fillStyle = '#d4a017'; ctx.beginPath(); ctx.arc(0, -38, 7, Math.PI, 0); ctx.fill(); ctx.fillRect(-8, -38, 16, 2.4); ctx.fillStyle = '#c62828'; ctx.beginPath(); ctx.moveTo(0, -45); ctx.quadraticCurveTo(-6, -52, -10, -48); ctx.quadraticCurveTo(-5, -47, 0, -44); ctx.fill(); break;
      case 'hood': ctx.fillStyle = shade(lk.robe, -0.35); ctx.beginPath(); ctx.arc(0, -37, 7.4, Math.PI * 0.8, Math.PI * 2.15); ctx.lineTo(-7, -30); ctx.fill(); break;
      case 'headdress': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.6, Math.PI, 0); ctx.fill(); ctx.fillStyle = '#c0c0c0'; ctx.beginPath(); ctx.moveTo(-7, -40); ctx.lineTo(-3, -50); ctx.lineTo(0, -42); ctx.lineTo(3, -51); ctx.lineTo(7, -40); ctx.fill(); ctx.fillStyle = lk.trim; ctx.beginPath(); ctx.arc(0, -43, 1.6, 0, 6.283); ctx.fill(); break;
      case 'longhair': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.8, Math.PI * 0.9, Math.PI * 2.1); ctx.fill();
        ctx.beginPath(); ctx.moveTo(-6, -38); ctx.quadraticCurveTo(-11 - Math.sin(t * 3) * 1.5, -24, -7, -14); ctx.lineTo(-3, -16); ctx.quadraticCurveTo(-5, -28, -2, -36); ctx.fill();
        ctx.beginPath(); ctx.arc(-2, -45, 3.2, 0, 6.283); ctx.fill(); ctx.fillStyle = '#ffd1e3'; ctx.beginPath(); ctx.arc(1, -45, 1.8, 0, 6.283); ctx.fill(); break;
      case 'topknot': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.6, Math.PI, 0); ctx.fill(); ctx.beginPath(); ctx.arc(0, -45, 2.8, 0, 6.283); ctx.fill(); ctx.fillStyle = '#c9a24a'; ctx.fillRect(-1, -48.5, 2, 6); break;
      case 'taoist': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.6, Math.PI, 0); ctx.fill(); ctx.fillStyle = '#263238'; ctx.fillRect(-5, -48, 10, 6); ctx.fillStyle = lk.trim; ctx.fillRect(-5, -45.5, 10, 1.2); break;
      case 'messy': ctx.fillStyle = lk.hair; for (var j = 0; j < 7; j++) { ctx.beginPath(); ctx.arc(-6 + j * 2, -40 - (j % 2) * 2, 3, 0, 6.283); ctx.fill(); } ctx.fillStyle = '#7cb342'; ctx.fillRect(-7, -40, 14, 2); break;
      case 'bandana': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.6, Math.PI, 0); ctx.fill(); ctx.fillStyle = lk.trim; ctx.fillRect(-7, -40, 14, 2.6); ctx.beginPath(); ctx.moveTo(-7, -40); ctx.lineTo(-12, -37); ctx.lineTo(-10, -41); ctx.fill(); break;
      case 'ironhelm': ctx.fillStyle = '#78909c'; ctx.beginPath(); ctx.arc(0, -38, 7.2, Math.PI, 0); ctx.fill(); ctx.fillRect(-7.5, -38, 15, 3); ctx.fillStyle = '#455a64'; ctx.fillRect(-1, -46, 2, 8); break;
      case 'horns': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.8, Math.PI, 0); ctx.fill(); ctx.fillStyle = '#e0d0c0'; ctx.beginPath(); ctx.moveTo(-5, -42); ctx.quadraticCurveTo(-11, -48, -9, -55); ctx.quadraticCurveTo(-7, -48, -2, -44); ctx.fill(); ctx.beginPath(); ctx.moveTo(5, -42); ctx.quadraticCurveTo(11, -48, 9, -55); ctx.quadraticCurveTo(7, -48, 2, -44); ctx.fill(); break;
      case 'crown': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.8, Math.PI * 0.9, Math.PI * 2.1); ctx.fill(); ctx.beginPath(); ctx.moveTo(-6, -38); ctx.quadraticCurveTo(-10 - Math.sin(t * 3) * 2, -26, -8, -18); ctx.lineTo(-4, -20); ctx.quadraticCurveTo(-5, -30, -2, -36); ctx.fill(); ctx.fillStyle = '#e8c26a'; ctx.beginPath(); ctx.moveTo(-4, -43); ctx.lineTo(-2, -49); ctx.lineTo(0, -45); ctx.lineTo(2, -49); ctx.lineTo(4, -43); ctx.fill(); break;
      case 'plume': ctx.fillStyle = '#d4a017'; ctx.beginPath(); ctx.arc(0, -38, 7.2, Math.PI, 0); ctx.fill(); ctx.fillRect(-8, -38, 16, 2.5); ctx.fillStyle = '#e53935'; ctx.beginPath(); ctx.moveTo(0, -45); ctx.quadraticCurveTo(-4 - Math.sin(t * 4) * 2, -58, -14, -56); ctx.quadraticCurveTo(-6, -52, 0, -44); ctx.fill(); break;
      case 'ponytail': ctx.fillStyle = lk.hair; ctx.beginPath(); ctx.arc(0, -38, 6.8, Math.PI * 0.95, Math.PI * 2.05); ctx.fill(); ctx.beginPath(); ctx.moveTo(-3, -44); ctx.quadraticCurveTo(-14, -42 + Math.sin(t * 4) * 3, -13, -28); ctx.lineTo(-10, -29); ctx.quadraticCurveTo(-10, -39, -2, -41); ctx.fill(); ctx.fillStyle = '#ff1744'; ctx.fillRect(-5, -45, 4, 3); break;
    }
  }
  function weapon(ctx, w, o) {
    var gl = o.wglow;
    switch (w) {
      case 'sword': case 'saber':
        ctx.strokeStyle = '#5d4037'; ctx.lineWidth = 2.4; ctx.beginPath(); ctx.moveTo(0, -2); ctx.lineTo(0, 3); ctx.stroke();
        ctx.fillStyle = '#c9a24a'; ctx.fillRect(-3, 2, 6, 1.6);
        ctx.fillStyle = w === 'saber' ? '#cfd8dc' : '#eef6ff'; ctx.beginPath(); ctx.moveTo(-1.3, 3.5); ctx.lineTo(1.3, 3.5); ctx.lineTo(w === 'saber' ? 2.8 : 0.9, 18); ctx.lineTo(0, 20); ctx.lineTo(-1, 18); ctx.closePath(); ctx.fill();
        if (gl) { ctx.globalCompositeOperation = 'lighter'; ctx.drawImage(glow(gl), -6, 2, 12, 20); ctx.globalCompositeOperation = 'source-over'; }
        break;
      case 'staff': ctx.strokeStyle = '#8d5a2b'; ctx.lineWidth = 2.4; ctx.beginPath(); ctx.moveTo(0, -12); ctx.lineTo(0, 18); ctx.stroke(); ctx.fillStyle = '#e8b04a'; ctx.fillRect(-2, -13, 4, 3); ctx.fillRect(-2, 16, 4, 3); break;
      case 'stick': ctx.strokeStyle = '#7cb342'; ctx.lineWidth = 2.6; ctx.beginPath(); ctx.moveTo(0, -10); ctx.lineTo(0, 17); ctx.stroke(); ctx.strokeStyle = '#33691e'; ctx.lineWidth = 1; for (var i = -6; i < 16; i += 6) { ctx.beginPath(); ctx.moveTo(-1.5, i); ctx.lineTo(1.5, i); ctx.stroke(); } break;
      case 'hammer': ctx.strokeStyle = '#6d4c41'; ctx.lineWidth = 2.4; ctx.beginPath(); ctx.moveTo(0, -3); ctx.lineTo(0, 16); ctx.stroke(); ctx.fillStyle = '#d4a017'; ctx.beginPath(); ctx.ellipse(0, 17, 6, 4.5, 0, 0, 6.283); ctx.fill(); ctx.fillStyle = '#fff3c4'; ctx.fillRect(-1, 14, 2, 2); break;
      case 'dart': ctx.fillStyle = '#cfd8dc'; for (var k = 0; k < 3; k++) { ctx.beginPath(); ctx.moveTo(-3 + k * 3, 0); ctx.lineTo(-2 + k * 3, 8); ctx.lineTo(-4 + k * 3, 8); ctx.fill(); } break;
      case 'claw': ctx.strokeStyle = '#b3ff6a'; ctx.lineWidth = 1.4; for (var m = -1; m <= 1; m++) { ctx.beginPath(); ctx.moveTo(m * 2, 0); ctx.quadraticCurveTo(m * 3, 5, m * 2 + 2, 8); ctx.stroke(); } ctx.globalCompositeOperation = 'lighter'; ctx.drawImage(glow('#76ff03'), -6, -2, 12, 12); ctx.globalCompositeOperation = 'source-over'; break;
      case 'fan': ctx.fillStyle = '#ffd1e3'; ctx.beginPath(); ctx.moveTo(0, 0); ctx.arc(0, 0, 10, 0.9, 2.3); ctx.closePath(); ctx.fill(); ctx.strokeStyle = '#c2185b'; ctx.lineWidth = 0.7; for (var n = 0; n < 6; n++) { var a = 0.9 + n * 0.28; ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(Math.cos(a) * 10, Math.sin(a) * 10); ctx.stroke(); } break;
      case 'talisman': ctx.fillStyle = '#ffeb3b'; ctx.fillRect(-3, 1, 6, 11); ctx.strokeStyle = '#d50000'; ctx.lineWidth = 0.8; ctx.beginPath(); ctx.moveTo(0, 2); ctx.lineTo(-1.5, 6); ctx.lineTo(1.5, 7); ctx.lineTo(0, 11); ctx.stroke(); ctx.globalCompositeOperation = 'lighter'; ctx.drawImage(glow('#18ffff'), -7, -1, 14, 14); ctx.globalCompositeOperation = 'source-over'; break;
      case 'bow': ctx.strokeStyle = '#6d4c41'; ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(4, 6, 10, -1.3, 1.3); ctx.stroke(); ctx.strokeStyle = '#eee'; ctx.lineWidth = 0.6; ctx.beginPath(); ctx.moveTo(6.7, -3.6); ctx.lineTo(6.7, 15.6); ctx.stroke(); break;
      case 'axe': ctx.strokeStyle = '#4e342e'; ctx.lineWidth = 2.6; ctx.beginPath(); ctx.moveTo(0, -4); ctx.lineTo(0, 20); ctx.stroke(); ctx.fillStyle = '#90a4ae'; ctx.beginPath(); ctx.moveTo(0, 12); ctx.quadraticCurveTo(12, 14, 10, 24); ctx.quadraticCurveTo(5, 19, 0, 20); ctx.fill(); break;
      case 'shield': ctx.fillStyle = '#546e7a'; ctx.beginPath(); ctx.ellipse(2, 4, 6, 8, 0, 0, 6.283); ctx.fill(); ctx.fillStyle = '#b0bec5'; ctx.beginPath(); ctx.arc(2, 4, 2, 0, 6.283); ctx.fill(); break;
      case 'spear': ctx.strokeStyle = '#6d4c41'; ctx.lineWidth = 2.2; ctx.beginPath(); ctx.moveTo(0, -14); ctx.lineTo(0, 24); ctx.stroke(); ctx.fillStyle = '#eceff1'; ctx.beginPath(); ctx.moveTo(-2.2, 24); ctx.lineTo(2.2, 24); ctx.lineTo(0, 33); ctx.fill(); ctx.fillStyle = '#e53935'; ctx.beginPath(); ctx.moveTo(-3, 22); ctx.lineTo(3, 22); ctx.lineTo(0, 19); ctx.fill(); break;
      case 'twin': weapon(ctx, 'sword', o); ctx.translate(-5, -2); ctx.rotate(0.5); weapon(ctx, 'sword', o); break;
    }
  }
  // thú: sói, hổ, yêu hồ
  function beast(ctx, x, y, sc, type, o) {
    var f = o.face || 1, wk = o.walk || 0, t = o.t || 0;
    var col = S.CREEPS[type].col, dark = shade(col, -0.45), tails = type === 'yeuho' ? 3 : 1;
    ctx.save(); ctx.translate(x, y); ctx.scale(sc * f, sc);
    var lg = o.moving ? Math.sin(wk * 1.4) * 4 : 0;
    ctx.strokeStyle = dark; ctx.lineWidth = 3; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(-8, -9); ctx.lineTo(-8 + lg, 0); ctx.moveTo(-4, -9); ctx.lineTo(-4 - lg, 0); ctx.moveTo(7, -9); ctx.lineTo(7 - lg, 0); ctx.moveTo(10, -9); ctx.lineTo(10 + lg, 0); ctx.stroke();
    for (var i = 0; i < tails; i++) {
      ctx.strokeStyle = type === 'yeuho' ? '#ffccbc' : col; ctx.lineWidth = type === 'yeuho' ? 4 : 3;
      ctx.beginPath(); ctx.moveTo(-11, -14); ctx.quadraticCurveTo(-20, -18 - i * 5 + Math.sin(t * 5 + i) * 3, -22, -26 - i * 4); ctx.stroke();
    }
    var gr = ctx.createLinearGradient(0, -22, 0, -6); gr.addColorStop(0, shade(col, 0.15)); gr.addColorStop(1, dark);
    ctx.fillStyle = gr; ctx.beginPath(); ctx.ellipse(0, -14, 13, 6.5, 0, 0, 6.283); ctx.fill();
    if (type === 'hovuong') { ctx.strokeStyle = '#2a1a0a'; ctx.lineWidth = 1.6; for (var s = -8; s < 10; s += 4) { ctx.beginPath(); ctx.moveTo(s, -20); ctx.lineTo(s + 2, -13); ctx.stroke(); } }
    ctx.fillStyle = shade(col, 0.1); ctx.beginPath(); ctx.ellipse(13, -19, 6, 5, 0.2, 0, 6.283); ctx.fill();
    ctx.beginPath(); ctx.moveTo(15, -18); ctx.lineTo(22, -16); ctx.lineTo(16, -14); ctx.fill();
    ctx.fillStyle = dark; ctx.beginPath(); ctx.moveTo(10, -23); ctx.lineTo(11, -29); ctx.lineTo(14, -24); ctx.fill(); ctx.beginPath(); ctx.moveTo(14, -23); ctx.lineTo(16, -28); ctx.lineTo(17, -22); ctx.fill();
    ctx.fillStyle = type === 'yeuho' ? '#00e5ff' : '#ffeb3b'; ctx.fillRect(16, -21, 2, 1.6);
    if (o.atk > 0) { ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.moveTo(18, -15); ctx.lineTo(21, -13); ctx.lineTo(18, -13); ctx.fill(); }
    ctx.restore();
  }

  // LINH VẬT — tướng chủ đạo cực đẹp
  var MASCOTS = {
    bachy: { name: 'Bạch Y Tiên Nữ', bonus: '+25 vàng khởi đầu', look: { skin: '#fbe3d2', hair: '#0e0a0a', hat: 'crown', robe: '#f7f9ff', robe2: '#9fd3ff', trim: '#7ec8ff', female: true, sash: '#ff8fb1' }, weapon: 'fan', ribbon: '#ff8fb1', aura: '#9fd3ff', cape: 'rgba(200,230,255,0.75)' },
    honglien: { name: 'Hồng Liên Kiếm Cơ', bonus: '+8 máu thành', look: { skin: '#f8d8c2', hair: '#1a0806', hat: 'ponytail', robe: '#d32f2f', robe2: '#ffcc80', trim: '#ffd54f', female: true, sash: '#ffd54f' }, weapon: 'twin', ribbon: '#ffd54f', aura: '#ff5252', cape: 'rgba(183,28,28,0.85)', wglow: '#ff8a65' },
    thanhlong: { name: 'Thanh Long Kiếm Khách', bonus: '+2 thu nhập mỗi đợt', look: { skin: '#f1cba6', hair: '#0d0d0d', hat: 'topknot', robe: '#00897b', robe2: '#e0f2f1', trim: '#80cbc4', sash: '#004d40' }, weapon: 'sword', ribbon: '#64ffda', aura: '#1de9b6', cape: 'rgba(0,77,64,0.85)', wglow: '#64ffda' },
    kimgiap: { name: 'Kim Giáp Thiên Tướng', bonus: 'Tướng +10% máu', look: { skin: '#eec39e', hair: '#111', hat: 'plume', robe: '#d4a017', robe2: '#7a4a12', trim: '#fff3b0', armor: true, sash: '#b71c1c' }, weapon: 'spear', ribbon: '#ff5252', aura: '#ffd740', cape: 'rgba(183,28,28,0.9)' }
  };
  var MASCOT_ORDER = ['bachy', 'honglien', 'thanhlong', 'kimgiap'];
  function mascot(ctx, x, y, sc, key, o) {
    var M = MASCOTS[key], t = o.t || 0;
    // hào quang dưới chân
    ctx.save(); ctx.globalCompositeOperation = 'lighter';
    ctx.globalAlpha = 0.5 + Math.sin(t * 3) * 0.15; ctx.drawImage(glow(M.aura), x - 30 * sc, y - 14 * sc, 60 * sc, 28 * sc);
    ctx.restore();
    ctx.strokeStyle = hexA(M.aura, 0.8); ctx.lineWidth = 1.5; ctx.beginPath(); ctx.ellipse(x, y, 16 * sc, 7.5 * sc, 0, 0, 6.283); ctx.stroke();
    ctx.fillStyle = 'rgba(0,0,0,0.3)'; ctx.beginPath(); ctx.ellipse(x, y, 11 * sc, 5 * sc, 0, 0, 6.283); ctx.fill();
    // dải lụa bay
    var fy = y - 4 * sc - Math.sin(t * 2) * 2 * sc;
    ctx.save(); ctx.translate(x, fy); ctx.scale(sc, sc);
    ctx.strokeStyle = hexA(M.ribbon, 0.85); ctx.lineWidth = 2.4; ctx.lineCap = 'round';
    for (var r = 0; r < 2; r++) {
      ctx.beginPath(); var sgn = r ? 1 : -1; ctx.moveTo(sgn * 7, -24);
      for (var k = 1; k <= 8; k++) ctx.lineTo(sgn * (7 + k * 2.6), -24 + k * 3.2 + Math.sin(t * 4 + k * 0.7 + r) * 3.2);
      ctx.stroke();
    }
    ctx.restore();
    human(ctx, x, fy, sc, M.look, { face: o.face, walk: o.walk, moving: o.moving, atk: o.atk, t: t, weapon: M.weapon, cape: M.cape, wglow: M.wglow });
    // hạt sáng quanh người
    ctx.save(); ctx.globalCompositeOperation = 'lighter';
    for (var i = 0; i < 5; i++) { var a = t * 1.5 + i * 1.256, px = x + Math.cos(a) * 14 * sc, py = fy - 22 * sc + Math.sin(a * 1.3) * 16 * sc; blit(ctx, M.aura, px, py, 4 * sc, 0.8); }
    ctx.restore();
  }

  function drawUnitIcon(cv, type, kind) {
    var g = cv.getContext('2d'), W = cv.width, H = cv.height; g.clearRect(0, 0, W, H);
    var gr = g.createRadialGradient(W / 2, H * 0.55, 2, W / 2, H * 0.55, W * 0.6);
    var col = kind === 'mascot' ? MASCOTS[type].aura : kind === 'send' ? S.CREEPS[type].col : S.UNITS[type].col;
    gr.addColorStop(0, hexA(col, 0.55)); gr.addColorStop(1, 'rgba(0,0,0,0)'); g.fillStyle = gr; g.fillRect(0, 0, W, H);
    var sc = H / 52;
    if (kind === 'mascot') mascot(g, W / 2, H * 0.94, sc * 0.95, type, { face: 1, t: performance.now() / 1000 });
    else if (kind === 'send') { if (S.CREEPS[type].beast) beast(g, W / 2 - 2 * sc, H * 0.82, sc * 1.1, type, { face: 1 }); else human(g, W / 2, H * 0.92, sc * 0.95, CLOOK[type], { face: 1 }); }
    else human(g, W / 2, H * 0.94, sc, LOOK[type], { face: 1, weapon: S.UNITS[type].weapon });
  }

  return { iso: iso, L: L, depth: depth, LX: LX, FLIP: FLIP, HW: HW, HH: HH, glow: glow, blit: blit, hexA: hexA, shade: shade,
    buildBG: buildBG, getBG: function () { return BG; }, BOX: BOX, BGS: BGS, LANTERNS: function () { return LANTERNS; },
    human: human, beast: beast, mascot: mascot, LOOK: LOOK, CLOOK: CLOOK, MASCOTS: MASCOTS, MASCOT_ORDER: MASCOT_ORDER, drawUnitIcon: drawUnitIcon, diamond: diamond };
})();
