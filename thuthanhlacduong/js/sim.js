// ===== THỦ THÀNH LẠC DƯƠNG — mô phỏng tất định (deterministic) =====
// Chạy theo tick cố định + RNG có seed + lệnh (command) => sẵn sàng cho đấu online lockstep.
var Sim = (function () {
  'use strict';
  var DT = 0.05;            // 20 tick / giây
  var LANE_W = 11;           // số ô ngang
  var BUILD_Y0 = 2, BUILD_Y1 = 13; // hàng được xây
  var LEAK_Y = 15.2, GATE_Y = 17.4;
  var MAX_WAVE = 20;
  var SAVE = [[50, 0.04], [120, 0.06], [250, 0.08], [500, 0.10], [900, 0.12]];   // [mốc vàng, lãi]
  // ĐƯỜNG VÒNG: giặc đi zíc-zắc qua cả sân rồi mới tới cổng thành
  var PATH = [[5.5, -0.4], [1.3, 1.2], [9.7, 3.6], [1.3, 6.2], [9.7, 8.8], [1.3, 11.4], [9.7, 13.6], [5.5, 15.4]];

  // ---- Môn phái (tướng của người chơi) ----
  var UNITS = {
    thienvuong: { name: 'Thiên Vương', role: 'Cận chiến chém lan', cost: 15, hp: 170, dmg: 13, cd: 1.0, range: 0.95, spd: 2.3, melee: true, dt: 'phys',
      col: '#d4a017', col2: '#7a4a12', weapon: 'hammer',
      skill: { name: 'Thiên Vương Chiến', cd: 6, type: 'whirl', r: 1.5, mult: 1.6 },
      up: { name: 'Thiên Vương Bá Thể', cost: 30, hp: 420, dmg: 31 } },
    thieulam: { name: 'Thiếu Lâm', role: 'Đỡ đòn, choáng', cost: 20, hp: 330, dmg: 9, cd: 1.1, range: 0.95, spd: 2.0, melee: true, dt: 'phys', armor: 0.2,
      col: '#e8a33d', col2: '#8b3a0e', weapon: 'staff',
      skill: { name: 'Kim Cương Chưởng', cd: 7, type: 'shock', r: 1.9, mult: 1.4, stun: 1.2 },
      up: { name: 'La Hán Kim Thân', cost: 40, hp: 780, dmg: 21 } },
    duongmon: { name: 'Đường Môn', role: 'Ám khí tầm xa', cost: 25, hp: 95, dmg: 15, cd: 0.85, range: 4.6, spd: 2.2, dt: 'phys', proj: 'dart',
      col: '#2e7d5b', col2: '#123d2c', weapon: 'dart',
      skill: { name: 'Bạo Vũ Lê Hoa', cd: 6, type: 'fan', n: 9, mult: 0.9 },
      up: { name: 'Đường Môn Thần Châm', cost: 45, hp: 210, dmg: 34, range: 5.0 } },
    ngudoc: { name: 'Ngũ Độc', role: 'Độc sát thương theo thời gian', cost: 30, hp: 110, dmg: 7, cd: 1.2, range: 4.2, spd: 2.1, dt: 'magic', proj: 'poison', dot: 7,
      col: '#6a3d9a', col2: '#2a1240', weapon: 'claw',
      skill: { name: 'Vạn Độc Vụ', cd: 8, type: 'cloud', r: 1.7, dps: 16, dur: 4 },
      up: { name: 'Ngũ Độc Giáo Chủ', cost: 55, hp: 240, dmg: 16, dot: 16 } },
    ngamy: { name: 'Nga My', role: 'Hồi máu đồng đội', cost: 35, hp: 125, dmg: 7, cd: 1.2, range: 3.8, spd: 2.1, dt: 'magic', proj: 'petal', heal: 17,
      col: '#f06292', col2: '#7b1f45', weapon: 'fan',
      skill: { name: 'Phổ Độ Chúng Sinh', cd: 9, type: 'massheal', r: 3.2, amt: 60 },
      up: { name: 'Nga My Tiên Tử', cost: 60, hp: 270, dmg: 15, heal: 38, amt: 140 } },
    vodang: { name: 'Võ Đang', role: 'Kiếm khí đánh lan', cost: 40, hp: 115, dmg: 24, cd: 1.5, range: 4.3, spd: 2.1, dt: 'magic', proj: 'sword', splash: 1.1,
      col: '#4a90d9', col2: '#1b3a66', weapon: 'sword',
      skill: { name: 'Vạn Kiếm Quy Tông', cd: 8, type: 'swordrain', r: 1.7, n: 9, mult: 0.85 },
      up: { name: 'Thái Cực Kiếm Thánh', cost: 70, hp: 250, dmg: 52 } },
    conlon: { name: 'Côn Lôn', role: 'Sét lan nhiều mục tiêu', cost: 45, hp: 115, dmg: 25, cd: 1.6, range: 4.3, spd: 2.1, dt: 'magic', proj: 'chain', chain: 3,
      col: '#00bcd4', col2: '#0d4a57', weapon: 'talisman',
      skill: { name: 'Lôi Động Cửu Thiên', cd: 9, type: 'thunder', r: 1.6, mult: 3.0 },
      up: { name: 'Côn Lôn Lôi Thần', cost: 75, hp: 255, dmg: 54, chain: 4 } },
    caibang: { name: 'Cái Bang', role: 'Chưởng rồng sát thương lớn', cost: 55, hp: 440, dmg: 36, cd: 1.2, range: 1.0, spd: 2.6, melee: true, dt: 'phys',
      col: '#a1887f', col2: '#4e342e', weapon: 'stick',
      skill: { name: 'Giáng Long Thập Bát Chưởng', cd: 7, type: 'dragon', len: 4.5, w: 0.9, mult: 2.4 },
      up: { name: 'Bang Chủ Cái Bang', cost: 95, hp: 1000, dmg: 82 } }
  };
  var UNIT_ORDER = ['thienvuong', 'thieulam', 'duongmon', 'ngudoc', 'ngamy', 'vodang', 'conlon', 'caibang'];

  // ---- Giặc (quái theo đợt) ----
  var CREEPS = {
    sontac:  { name: 'Giặc Khăn Vàng', hp: 70, dmg: 7, cd: 1.0, range: 0.9, spd: 1.4, bounty: 2, leak: 1, col: '#8d6e63', size: 1 },
    soi:     { name: 'Chiến Khuyển Mông Nguyên', hp: 45, dmg: 5, cd: 0.8, range: 0.8, spd: 2.5, bounty: 1, leak: 1, col: '#9e9e9e', size: 0.9, beast: true },
    cungtac: { name: 'Cung Thủ Khăn Vàng', hp: 52, dmg: 8, cd: 1.3, range: 3.4, spd: 1.3, bounty: 2, leak: 1, col: '#6d4c41', size: 1, ranged: true },
    thietgiap:{ name: 'Thiết Kỵ Mông Nguyên', hp: 135, dmg: 9, cd: 1.2, range: 0.9, spd: 1.0, bounty: 3, leak: 2, col: '#607d8b', size: 1.15, armor: 0.45 },
    yeuho:   { name: 'Yêu Hồ', hp: 85, dmg: 10, cd: 0.9, range: 0.9, spd: 1.9, bounty: 3, leak: 1, col: '#ff7043', size: 0.95, mres: 0.45, beast: true },
    hovuong: { name: 'Hổ Vương', hp: 1300, dmg: 38, cd: 1.4, range: 1.2, spd: 1.1, bounty: 30, leak: 5, col: '#ff9800', size: 2.0, boss: true, beast: true },
    trai_chu:{ name: 'Hoàng Cân Đại Soái', hp: 1500, dmg: 42, cd: 1.3, range: 1.2, spd: 1.0, bounty: 40, leak: 6, col: '#37474f', size: 2.0, boss: true, armor: 0.3 },
    huyetma: { name: 'Phiến Tướng Biện Kinh', hp: 1600, dmg: 46, cd: 1.2, range: 1.2, spd: 1.2, bounty: 50, leak: 7, col: '#c62828', size: 2.1, boss: true, mres: 0.3 },
    mavuong: { name: 'Mông Nguyên Đại Hãn', hp: 2000, dmg: 55, cd: 1.2, range: 1.3, spd: 1.0, bounty: 80, leak: 10, col: '#4a148c', size: 2.4, boss: true, armor: 0.25, mres: 0.25 },
    // quân phái đi (sends)
    hacy:    { name: 'Thích Khách Biện Kinh', hp: 150, dmg: 14, cd: 0.8, range: 0.9, spd: 2.2, bounty: 0, leak: 2, col: '#212121', size: 1, send: true },
    langvuong:{ name: 'Lang Vương', hp: 360, dmg: 22, cd: 0.9, range: 1.0, spd: 2.3, bounty: 0, leak: 3, col: '#cfd8dc', size: 1.4, send: true, beast: true },
    matang:  { name: 'Ma Tăng Tây Vực', hp: 800, dmg: 34, cd: 1.3, range: 1.1, spd: 1.2, bounty: 0, leak: 5, col: '#880e4f', size: 1.7, send: true, armor: 0.2 }
  };
  var SENDS = {
    hacy: { cost: 20, inc: 2 },
    langvuong: { cost: 45, inc: 5 },
    matang: { cost: 90, inc: 10 }
  };
  var SEND_ORDER = ['hacy', 'langvuong', 'matang'];

  var WAVE_PATTERNS = [
    [['sontac', 8]],
    [['soi', 11]],
    [['sontac', 6], ['cungtac', 4]],
    [['thietgiap', 6]],
    [['hovuong', 1], ['soi', 6]],
    [['yeuho', 8]],
    [['sontac', 6], ['cungtac', 6]],
    [['thietgiap', 7], ['cungtac', 3]],
    [['soi', 12], ['yeuho', 4]],
    [['trai_chu', 1], ['sontac', 6]],
    [['yeuho', 7], ['thietgiap', 4]],
    [['sontac', 8], ['cungtac', 6]],
    [['soi', 16]],
    [['thietgiap', 10]],
    [['huyetma', 1], ['yeuho', 6]],
    [['cungtac', 8], ['thietgiap', 5]],
    [['yeuho', 12]],
    [['sontac', 10], ['soi', 8]],
    [['thietgiap', 8], ['yeuho', 6], ['cungtac', 4]],
    [['mavuong', 1], ['huyetma', 1], ['thietgiap', 6]]
  ];

  function hpScale(w) { var k = w - 1; return 1 + 0.19 * k + 0.0155 * k * k; }
  function dmgScale(w) { var k = w - 1; return 1 + 0.16 * k + 0.012 * k * k; }

  // Toán tất định (giống hệt nhau trên mọi trình duyệt) cho đấu online lockstep
  var PI = 3.141592653589793, TAU = 6.283185307179586;
  function dsin(x) { x = x % TAU; if (x > PI) x -= TAU; else if (x < -PI) x += TAU; var x2 = x * x; return x * (1 - x2 / 6 * (1 - x2 / 20 * (1 - x2 / 42 * (1 - x2 / 72 * (1 - x2 / 110))))); }
  function dcos(x) { return dsin(x + PI / 2); }
  function datan(z) { var a = z < 0 ? -z : z, inv = a > 1; if (inv) a = 1 / a; var r = 0, t = a, z2 = a * a; // chuỗi với giảm góc
    var red = a > 0.2679491924311227; if (red) a = (a * 1.7320508075688772 - 1) / (a + 1.7320508075688772); z2 = a * a;
    r = a * (1 - z2 * (0.3333333333 - z2 * (0.2 - z2 * (0.1428571429 - z2 * (0.1111111111 - z2 * 0.0909090909)))));
    if (red) r += PI / 6; if (inv) r = PI / 2 - r; return z < 0 ? -r : r; }
  function datan2(y, x) { if (x > 0) return datan(y / x); if (x < 0) return y >= 0 ? datan(y / x) + PI : datan(y / x) - PI; return y > 0 ? PI / 2 : y < 0 ? -PI / 2 : 0; }
  function mulberry32(a) {
    return function () {
      a |= 0; a = a + 0x6D2B79F5 | 0;
      var t = Math.imul(a ^ a >>> 15, 1 | a);
      t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }

  function create(opts) {
    opts = opts || {};
    var G = {
      tick: 0, time: 0, seed: opts.seed || 12345,
      phase: 'build', phaseT: 40, wave: 1,
      players: [mkPlayer(), mkPlayer()],
      units: [], creeps: [], projs: [], zones: [], strikes: [],
      nextId: 1, ev: [], spawnQ: [[], []], laneDone: [false, false],
      winner: -1, over: false, waveLeaks: [0, 0], firstBlood: false
    };
    G.rs = G.seed | 0;
    G.rng = function () { G.rs = G.rs + 0x6D2B79F5 | 0; var t = Math.imul(G.rs ^ G.rs >>> 15, 1 | G.rs); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
    G.mascots = opts.mascots || ['bachy', 'thanhlong'];
    for (var i = 0; i < 2; i++) {
      var m = G.mascots[i], P = G.players[i];
      if (m === 'bachy') P.gold += 25; else if (m === 'honglien') P.hp += 8; else if (m === 'thanhlong') P.income += 2; else if (m === 'kimgiap') P.hpMul = 1.1;
    }
    return G;
  }
  function mkPlayer() { return { gold: 100, income: 14, hp: 30, value: 0, sendQ: [], ready: false, sentThisWave: 0, kills: 0, leaked: 0 }; }

  var MAX_TIER = 4, TIER_MUL = [1, 2.15, 3.5, 5.3, 7.8], TIER_COST = [1.2, 1.7, 2.4, 3.3];
  function upCost(u) { return u.tier >= MAX_TIER ? 0 : Math.round(UNITS[u.type].cost * TIER_COST[u.tier]); }
  function stat(u, k) { var d = UNITS[u.type], v = d[k];
    if (k === 'amt' && v === undefined) v = d.skill.amt;
    if (u.tier > 0) { if (k === 'hp' || k === 'dmg' || k === 'heal' || k === 'dot' || k === 'amt') v = v * TIER_MUL[u.tier]; else if (k === 'range' && !d.melee) v = v + 0.15 * u.tier; else if (k === 'chain') v = d.chain + (u.tier >= 3 ? 1 : 0); } if (k === 'hp' && u.hpMul) v = Math.round(v * u.hpMul); return v; }

  function cellFree(G, p, cx, cy) {
    for (var i = 0; i < G.units.length; i++) { var u = G.units[i]; if (u.owner === p && u.cx === cx && u.cy === cy) return false; }
    return true;
  }

  // ---- LỆNH (command) — đường duy nhất để người chơi/AI/đối thủ online thay đổi trạng thái ----
  function apply(G, c) {
    if (G.over) return false;
    var P = G.players[c.p];
    if (c.t === 'place') {
      var d = UNITS[c.u]; if (!d) return false;
      if (c.cx < 0 || c.cx >= LANE_W || c.cy < BUILD_Y0 || c.cy > BUILD_Y1) return false;
      if (!cellFree(G, c.p, c.cx, c.cy) || P.gold < d.cost) return false;
      P.gold -= d.cost; P.value += d.cost;
      var u = { id: G.nextId++, owner: c.p, type: c.u, tier: 0, cx: c.cx, cy: c.cy, x: c.cx + 0.5, y: c.cy + 0.5,
        hp: Math.round(d.hp * (P.hpMul || 1)), hpMul: P.hpMul || 1, active: G.phase === 'build', dead: false, cd: 0, scd: d.skill.cd * 0.5, tgt: 0, retarget: 0, fresh: G.phase === 'build', spent: d.cost, face: 1, atkAnim: 0 };
      G.units.push(u);
      G.ev.push({ e: 'place', p: c.p, id: u.id });
      return true;
    }
    if (c.t === 'upgrade') {
      var u2 = findUnit(G, c.id); if (!u2 || u2.owner !== c.p || u2.tier >= MAX_TIER) return false;
      if (G.phase !== 'build' && u2.active) return false;
      var uc = upCost(u2); if (P.gold < uc) return false;
      P.gold -= uc; P.value += uc; u2.spent += uc; u2.tier++; u2.hp = stat(u2, 'hp');
      G.ev.push({ e: 'upgrade', p: c.p, id: u2.id });
      return true;
    }
    if (c.t === 'sell') {
      var u3 = findUnit(G, c.id); if (!u3 || u3.owner !== c.p) return false;
      if (G.phase !== 'build' && u3.active) return false;
      var refund = u3.fresh ? u3.spent : Math.floor(u3.spent * 0.6);
      P.gold += refund; P.value -= u3.spent;
      G.units.splice(G.units.indexOf(u3), 1);
      G.ev.push({ e: 'sell', p: c.p, x: u3.x, y: u3.y, g: refund });
      return true;
    }
    if (c.t === 'send') {
      var s = SENDS[c.k]; if (!s || P.gold < s.cost) return false;
      if (P.sentThisWave >= 6 + G.wave) return false;
      P.gold -= s.cost; P.income += s.inc; P.sentThisWave++;
      P.sendQ.push(c.k);
      G.ev.push({ e: 'send', p: c.p, k: c.k });
      return true;
    }
    if (c.t === 'ready') { P.ready = true; return true; }
    return false;
  }

  function findUnit(G, id) { for (var i = 0; i < G.units.length; i++) if (G.units[i].id === id) return G.units[i]; return null; }
  function findCreep(G, id) { for (var i = 0; i < G.creeps.length; i++) if (G.creeps[i].id === id) return G.creeps[i]; return null; }

  function startFight(G) {
    G.phase = 'fight'; G.phaseT = 120; G.fightT = 0;
    G.waveLeaks = [0, 0];
    var pat = WAVE_PATTERNS[G.wave - 1];
    for (var lane = 0; lane < 2; lane++) {
      var q = [], t = 0.3;
      for (var i = 0; i < pat.length; i++) { var cnt = CREEPS[pat[i][0]].boss ? pat[i][1] : Math.round(pat[i][1] * 1.8); for (var n = 0; n < cnt; n++) { q.push({ k: pat[i][0], t: t }); t += CREEPS[pat[i][0]].boss ? 0.9 : 0.6; } }
      var opp = G.players[1 - lane];
      t += 0.8;
      for (var j = 0; j < opp.sendQ.length; j++) { q.push({ k: opp.sendQ[j], t: t, from: 1 - lane }); t += 0.45; }
      opp.sendQ = [];
      G.spawnQ[lane] = q; G.laneDone[lane] = false;
    }
    for (var k = 0; k < G.units.length; k++) {
      var u = G.units[k]; u.active = true; u.fresh = false; u.dead = false; u.hp = stat(u, 'hp');
      u.x = u.cx + 0.5; u.y = u.cy + 0.5; u.cd = 0.2 + G.rng() * 0.4; u.scd = UNITS[u.type].skill.cd * (0.4 + G.rng() * 0.3); u.tgt = 0;
    }
    G.players[0].ready = G.players[1].ready = false;
    G.players[0].sentThisWave = G.players[1].sentThisWave = 0;
    G.ev.push({ e: 'waveStart', w: G.wave, boss: pat.some(function (x) { return CREEPS[x[0]].boss; }) });
  }

  function spawnCreep(G, lane, k, from) {
    var d = CREEPS[k], w = G.wave;
    var hm = hpScale(w), dm = dmgScale(w);
    if (d.send) { hm = 1 + 0.13 * (w - 1); dm = 1 + 0.08 * (w - 1); }
    var hp = Math.round(d.hp * hm * (d.boss || d.send ? 1 : 1.85));
    var c = { id: G.nextId++, lane: lane, type: k, x: 4.5 + G.rng() * 2, y: -0.8 - G.rng() * 0.8, wp: 1, hp: hp, max: hp,
      dmg: d.dmg * dm, cd: G.rng() * 0.5, tgt: 0, stun: 0, poison: 0, poisonT: 0, leaked: false, slow: 0, from: from, face: 1, atkAnim: 0, wob: G.rng() * 6 };
    G.creeps.push(c);
  }

  function endFight(G) {
    G.creeps = []; G.projs = []; G.zones = []; G.strikes = [];
    for (var p = 0; p < 2; p++) {
      var P = G.players[p];
      P.gold += P.income; P.income += 3;
      G.ev.push({ e: 'income', p: p, g: P.income, perfect: G.waveLeaks[p] === 0 });
    }
    for (var k = 0; k < G.units.length; k++) { var u = G.units[k]; u.dead = false; u.hp = stat(u, 'hp'); u.x = u.cx + 0.5; u.y = u.cy + 0.5; u.tgt = 0; }
    G.ev.push({ e: 'waveEnd', w: G.wave, leaks: G.waveLeaks.slice() });
    var a = G.players[0].hp, b = G.players[1].hp;
    if (a <= 0 || b <= 0 || G.wave >= MAX_WAVE) {
      G.over = true; G.phase = 'over';
      G.winner = a > b ? 0 : b > a ? 1 : -1;
      G.ev.push({ e: 'over', winner: G.winner });
      return;
    }
    G.wave++;
    G.phase = 'build'; G.phaseT = 25;
  }

  function dist2(a, b) { var dx = a.x - b.x, dy = a.y - b.y; return dx * dx + dy * dy; }

  function damageCreep(G, c, amt, dt, srcOwner, fx) {
    if (c.hp <= 0) return;
    var d = CREEPS[c.type];
    if (dt === 'phys' && d.armor) amt *= 1 - d.armor;
    if (dt === 'magic' && d.mres) amt *= 1 - d.mres;
    c.hp -= amt;
    if (c.hp <= 0) {
      c.hp = 0;
      var P = G.players[c.lane];
      P.gold += d.bounty; P.kills++;
      var fb = !G.firstBlood; G.firstBlood = true;
      G.ev.push({ e: 'kill', lane: c.lane, x: c.x, y: c.y, type: c.type, g: d.bounty, boss: !!d.boss, fb: fb, fx: fx || dt });
    }
  }
  function damageUnit(G, u, amt) {
    if (u.dead) return;
    var a = stat(u, 'armor'); if (a) amt *= 1 - a;
    u.hp -= amt;
    if (u.hp <= 0) { u.hp = 0; u.dead = true; G.ev.push({ e: 'unitDie', p: u.owner, x: u.x, y: u.y, type: u.type }); }
  }

  function creepsInLane(G, lane) { var r = []; for (var i = 0; i < G.creeps.length; i++) { var c = G.creeps[i]; if (c.lane === lane && c.hp > 0 && !c.leaked && c.y > -0.2) r.push(c); } return r; }
  function nearestCreep(G, lane, x, y, maxR, exclude) {
    var best = null, bd = maxR * maxR;
    for (var i = 0; i < G.creeps.length; i++) {
      var c = G.creeps[i];
      if (c.lane !== lane || c.hp <= 0 || c.leaked || c.y < -0.2) continue;
      if (exclude && exclude.indexOf(c.id) >= 0) continue;
      var dx = c.x - x, dy = c.y - y, dd = dx * dx + dy * dy;
      if (dd < bd) { bd = dd; best = c; }
    }
    return best;
  }

  function aoeCreeps(G, lane, x, y, r, amt, dt, owner, stun, fx) {
    var n = 0;
    for (var i = 0; i < G.creeps.length; i++) {
      var c = G.creeps[i];
      if (c.lane !== lane || c.hp <= 0 || c.leaked) continue;
      var dx = c.x - x, dy = c.y - y;
      if (dx * dx + dy * dy <= r * r) { damageCreep(G, c, amt, dt, owner, fx); if (stun) c.stun = Math.max(c.stun, stun); n++; }
    }
    return n;
  }

  function castSkill(G, u, tgt) {
    var d = UNITS[u.type], s = d.skill, dmg = stat(u, 'dmg');
    var lane = u.owner;
    switch (s.type) {
      case 'whirl':
        aoeCreeps(G, lane, u.x, u.y, s.r, dmg * s.mult, 'phys', u.owner, 0, 'whirl');
        G.ev.push({ e: 'skill', k: 'whirl', lane: lane, x: u.x, y: u.y, r: s.r, id: u.id });
        break;
      case 'shock':
        aoeCreeps(G, lane, u.x, u.y, s.r, dmg * s.mult, 'phys', u.owner, s.stun, 'shock');
        G.ev.push({ e: 'skill', k: 'shock', lane: lane, x: u.x, y: u.y, r: s.r, id: u.id });
        break;
      case 'fan':
        var ang = datan2(tgt.y - u.y, tgt.x - u.x);
        for (var i = 0; i < s.n; i++) {
          var a = ang + (i - (s.n - 1) / 2) * 0.13;
          G.projs.push({ k: 'fandart', lane: lane, side: 0, x: u.x, y: u.y, vx: dcos(a) * 11, vy: dsin(a) * 11, life: (stat(u, 'range') + 1.5) / 11, dmg: dmg * s.mult, dt: 'phys', owner: u.owner, hit: [] });
        }
        G.ev.push({ e: 'skill', k: 'fan', lane: lane, x: u.x, y: u.y, id: u.id });
        break;
      case 'cloud':
        G.zones.push({ lane: lane, x: tgt.x, y: tgt.y, r: s.r, dps: TIER_MUL[u.tier] * s.dps, t: s.dur, dur: s.dur, owner: u.owner });
        G.projs.push({ k: 'poisonbomb', lane: lane, side: 0, x: u.x, y: u.y, sx: u.x, sy: u.y, tx: tgt.x, ty: tgt.y, t: 0, dur: 0.5, owner: u.owner });
        G.ev.push({ e: 'skill', k: 'cloud', lane: lane, x: tgt.x, y: tgt.y, id: u.id });
        break;
      case 'massheal':
        var amt = stat(u, 'amt') || s.amt;
        for (var j = 0; j < G.units.length; j++) {
          var a2 = G.units[j];
          if (a2.owner !== u.owner || a2.dead || !a2.active) continue;
          if (dist2(a2, u) <= s.r * s.r) { a2.hp = Math.min(stat(a2, 'hp'), a2.hp + amt); G.ev.push({ e: 'healed', lane: lane, x: a2.x, y: a2.y, v: amt }); }
        }
        G.ev.push({ e: 'skill', k: 'massheal', lane: lane, x: u.x, y: u.y, r: s.r, id: u.id });
        break;
      case 'swordrain':
        for (var m = 0; m < s.n; m++) {
          var rr = Math.sqrt(G.rng()) * s.r, aa = G.rng() * 6.283;
          G.strikes.push({ lane: lane, x: tgt.x + dcos(aa) * rr, y: tgt.y + dsin(aa) * rr, t: 0.25 + m * 0.07, r: 0.75, dmg: dmg * s.mult, dt: 'magic', owner: u.owner, fx: 'sword' });
        }
        G.ev.push({ e: 'skill', k: 'swordrain', lane: lane, x: tgt.x, y: tgt.y, r: s.r, id: u.id, n: s.n });
        break;
      case 'thunder':
        G.strikes.push({ lane: lane, x: tgt.x, y: tgt.y, t: 0.45, r: s.r, dmg: dmg * s.mult, dt: 'magic', owner: u.owner, fx: 'thunder', stun: 0.6 });
        G.ev.push({ e: 'skill', k: 'thunder', lane: lane, x: tgt.x, y: tgt.y, r: s.r, id: u.id });
        break;
      case 'dragon':
        var ang2 = datan2(tgt.y - u.y, tgt.x - u.x);
        G.projs.push({ k: 'dragon', lane: lane, side: 0, x: u.x, y: u.y, sx: u.x, sy: u.y, vx: dcos(ang2) * 7, vy: dsin(ang2) * 7, life: s.len / 7, dmg: dmg * s.mult, dt: 'phys', w: s.w, owner: u.owner, hit: [] });
        G.ev.push({ e: 'skill', k: 'dragon', lane: lane, x: u.x, y: u.y, id: u.id, a: ang2 });
        break;
    }
  }

  function unitAttack(G, u, c) {
    var d = UNITS[u.type], dmg = stat(u, 'dmg'), lane = u.owner;
    u.atkAnim = 0.25; u.face = c.x >= u.x ? 1 : -1;
    if (d.melee) {
      damageCreep(G, c, dmg, d.dt, u.owner, 'slash');
      G.ev.push({ e: 'hit', lane: lane, x: c.x, y: c.y, k: 'slash', id: u.id });
      return;
    }
    if (d.proj === 'chain') {
      var pts = [{ x: u.x, y: u.y }], hit = [], cur = c, amt = dmg, n = stat(u, 'chain');
      for (var i = 0; i < n && cur; i++) {
        pts.push({ x: cur.x, y: cur.y }); hit.push(cur.id);
        damageCreep(G, cur, amt, 'magic', u.owner, 'bolt');
        amt *= 0.75;
        cur = nearestCreep(G, lane, cur.x, cur.y, 2.3, hit);
      }
      G.ev.push({ e: 'chain', lane: lane, pts: pts, id: u.id });
      return;
    }
    G.projs.push({ k: d.proj, lane: lane, side: 0, x: u.x, y: u.y - 0.1, sx: u.x, sy: u.y, tid: c.id, tx: c.x, ty: c.y, spd: d.proj === 'sword' ? 9 : d.proj === 'dart' ? 13 : 8,
      dmg: dmg, dt: d.dt, splash: d.splash || 0, dot: stat(u, 'dot') || 0, owner: u.owner });
    G.ev.push({ e: 'shoot', lane: lane, k: d.proj, id: u.id });
  }

  function stepUnits(G) {
    for (var i = 0; i < G.units.length; i++) {
      var u = G.units[i];
      if (!u.active || u.dead) continue;
      if (u.atkAnim > 0) u.atkAnim -= DT;
      var d = UNITS[u.type], lane = u.owner;
      u.cd -= DT; u.scd -= DT;
      // Nga My: hồi máu
      if (d.heal) {
        if (u.cd <= 0) {
          var best = null, br = 0.92;
          for (var j = 0; j < G.units.length; j++) {
            var a = G.units[j];
            if (a.owner !== u.owner || a.dead || !a.active || a === u && false) continue;
            var ratio = a.hp / stat(a, 'hp');
            if (ratio < br && dist2(a, u) <= (stat(u, 'range') + 0.5) * (stat(u, 'range') + 0.5)) { br = ratio; best = a; }
          }
          if (best) {
            u.cd = d.cd; u.atkAnim = 0.25;
            G.projs.push({ k: 'healorb', lane: lane, side: 0, x: u.x, y: u.y - 0.1, tid: best.id, heal: stat(u, 'heal'), spd: 7, owner: u.owner, ally: true });
            if (u.scd <= 0) { u.scd = d.skill.cd; castSkill(G, u, best); }
            continue;
          }
        }
      }
      var t = u.tgt ? findCreep(G, u.tgt) : null;
      if (t && (t.hp <= 0 || t.leaked)) t = null;
      u.retarget -= DT;
      if (!t || u.retarget <= 0) {
        var nt = nearestCreep(G, lane, u.x, u.y, 30);
        if (nt && (!t || dist2(nt, u) < dist2(t, u) * 0.7)) t = nt;
        u.retarget = 0.5;
      }
      if (!t) {
        // trở về vị trí
        var hx = u.cx + 0.5, hy = u.cy + 0.5, dx = hx - u.x, dy = hy - u.y, dd = Math.sqrt(dx * dx + dy * dy);
        if (dd > 0.05) { var st = Math.min(dd, d.spd * DT); u.x += dx / dd * st; u.y += dy / dd * st; u.moving = true; } else u.moving = false;
        u.tgt = 0; continue;
      }
      u.tgt = t.id;
      var rng = stat(u, 'range') + (CREEPS[t.type].size - 1) * 0.3;
      var ddx = t.x - u.x, ddy = t.y - u.y, dist = Math.sqrt(ddx * ddx + ddy * ddy);
      u.face = ddx >= 0 ? 1 : -1;
      if (dist > rng) {
        var step = Math.min(dist - rng + 0.05, d.spd * DT);
        u.x += ddx / dist * step; u.y += ddy / dist * step; u.moving = true;
      } else {
        u.moving = false;
        if (u.scd <= 0) { u.scd = d.skill.cd; castSkill(G, u, t); u.cd = Math.max(u.cd, 0.35); u.atkAnim = 0.4; }
        else if (u.cd <= 0) { u.cd = d.cd; unitAttack(G, u, t); }
      }
    }
  }

  function nearestUnit(G, lane, x, y, maxR) {
    var best = null, bd = maxR * maxR;
    for (var i = 0; i < G.units.length; i++) {
      var u = G.units[i];
      if (u.owner !== lane || u.dead || !u.active) continue;
      var dx = u.x - x, dy = u.y - y, dd = dx * dx + dy * dy;
      if (dd < bd) { bd = dd; best = u; }
    }
    return best;
  }

  function stepCreeps(G) {
    var rush = G.fightT > 110;
    for (var i = G.creeps.length - 1; i >= 0; i--) {
      var c = G.creeps[i], d = CREEPS[c.type];
      if (c.hp <= 0) { G.creeps.splice(i, 1); continue; }
      if (c.atkAnim > 0) c.atkAnim -= DT;
      if (c.poisonT > 0) { c.poisonT -= DT; damageCreep(G, c, c.poison * DT, 'magic', c.lane, 'poison'); if (c.hp <= 0) continue; }
      if (c.stun > 0) { c.stun -= DT; continue; }
      var spd = d.spd * (rush ? 1.8 : 1);
      if (c.leaked) {
        var gx = LANE_W / 2, gy = GATE_Y, dx0 = gx - c.x, dy0 = gy - c.y, dd0 = Math.sqrt(dx0 * dx0 + dy0 * dy0);
        if (dd0 < 0.3) {
          var P = G.players[c.lane]; P.hp = Math.max(0, P.hp - d.leak); P.leaked += d.leak; G.waveLeaks[c.lane] += d.leak;
          G.ev.push({ e: 'gateHit', lane: c.lane, v: d.leak, x: c.x, y: c.y });
          G.creeps.splice(i, 1); continue;
        }
        c.x += dx0 / dd0 * spd * DT; c.y += dy0 / dd0 * spd * DT; c.moving = true; continue;
      }
      c.cd -= DT;
      var t = (!rush && c.tgt) ? findUnit(G, c.tgt) : null;
      if (t && (t.dead || !t.active || dist2(t, c) > 9)) t = null;
      if (!t && !rush) t = nearestUnit(G, c.lane, c.x, c.y, d.ranged ? 3.4 : 2.0);
      if (t) {
        c.tgt = t.id;
        var dx = t.x - c.x, dy = t.y - c.y, dist = Math.sqrt(dx * dx + dy * dy) || 0.01;
        c.face = dx >= 0 ? 1 : -1;
        var rg = d.range + (d.size - 1) * 0.3;
        if (dist > rg) { var st = Math.min(dist - rg + 0.05, spd * DT); c.x += dx / dist * st; c.y += dy / dist * st; c.moving = true; }
        else {
          c.moving = false;
          if (c.cd <= 0) {
            c.cd = d.cd; c.atkAnim = 0.25;
            if (d.ranged) G.projs.push({ k: 'arrow', lane: c.lane, side: 1, x: c.x, y: c.y, sx: c.x, sy: c.y, tid: t.id, tx: t.x, ty: t.y, spd: 10, dmg: c.dmg });
            else { damageUnit(G, t, c.dmg); G.ev.push({ e: 'chit', lane: c.lane, x: t.x, y: t.y, boss: !!d.boss }); }
          }
        }
      } else {
        c.tgt = 0;
        var wp = PATH[c.wp || 1], ox = dsin(c.wob) * 0.6, wx = wp[0] + ox, wy = wp[1];
        var ddx = wx - c.x, ddy = wy - c.y, dl = Math.sqrt(ddx * ddx + ddy * ddy);
        if (dl < 0.45) { c.wp = (c.wp || 1) + 1; if (c.wp >= PATH.length) { c.leaked = true; G.ev.push({ e: 'leak', lane: c.lane, x: c.x, y: c.y }); } }
        else { c.x += ddx / dl * spd * DT; c.y += ddy / dl * spd * DT; }
        c.moving = true; c.face = ddx >= 0 ? 1 : -1;
      }
    }
  }

  function separate(G) {
    // đẩy nhẹ cho không chồng lên nhau
    var all = [];
    for (var i = 0; i < G.units.length; i++) { var u = G.units[i]; if (u.active && !u.dead) all.push(u); }
    for (var j = 0; j < G.creeps.length; j++) { var c = G.creeps[j]; if (c.hp > 0 && !c.leaked && c.y > -0.5) all.push(c); }
    for (var a = 0; a < all.length; a++) {
      var A = all[a], la = A.owner !== undefined ? A.owner : A.lane, ra = A.owner !== undefined ? 0.3 : 0.28 * CREEPS[A.type].size;
      for (var b = a + 1; b < all.length; b++) {
        var B = all[b], lb = B.owner !== undefined ? B.owner : B.lane; if (la !== lb) continue;
        var rb = B.owner !== undefined ? 0.3 : 0.28 * CREEPS[B.type].size;
        var dx = B.x - A.x, dy = B.y - A.y, dd = dx * dx + dy * dy, R = ra + rb;
        if (dd < R * R && dd > 1e-6) {
          var dist = Math.sqrt(dd), push = (R - dist) * 0.25;
          dx /= dist; dy /= dist;
          A.x -= dx * push; A.y -= dy * push; B.x += dx * push; B.y += dy * push;
        }
      }
      if (A.x < 0.2) A.x = 0.2; if (A.x > LANE_W - 0.2) A.x = LANE_W - 0.2;
    }
  }

  function stepProjs(G) {
    for (var i = G.projs.length - 1; i >= 0; i--) {
      var p = G.projs[i];
      if (p.k === 'fandart' || p.k === 'dragon') {
        p.x += p.vx * DT; p.y += p.vy * DT; p.life -= DT;
        var hr = p.k === 'dragon' ? p.w : 0.38;
        for (var j = 0; j < G.creeps.length; j++) {
          var c = G.creeps[j];
          if (c.lane !== p.lane || c.hp <= 0 || c.leaked || p.hit.indexOf(c.id) >= 0) continue;
          var r = hr + 0.2 * CREEPS[c.type].size;
          if (dist2(c, p) < r * r) {
            p.hit.push(c.id); damageCreep(G, c, p.dmg, p.dt, p.owner, p.k);
            G.ev.push({ e: 'hit', lane: p.lane, x: c.x, y: c.y, k: p.k });
            if (p.k === 'fandart') { p.life = 0; break; }
          }
        }
        if (p.life <= 0) G.projs.splice(i, 1);
        continue;
      }
      if (p.k === 'poisonbomb') { p.t += DT; if (p.t >= p.dur) G.projs.splice(i, 1); continue; }
      var tgt = p.ally ? findUnit(G, p.tid) : p.side === 1 ? findUnit(G, p.tid) : findCreep(G, p.tid);
      if (tgt && !p.ally && p.side === 0 && (tgt.hp <= 0 || tgt.leaked)) tgt = null;
      if (tgt && (p.ally || p.side === 1) && tgt.dead) tgt = null;
      if (tgt) { p.tx = tgt.x; p.ty = tgt.y; }
      var dx = p.tx - p.x, dy = p.ty - p.y, dist = Math.sqrt(dx * dx + dy * dy), st = p.spd * DT;
      if (dist <= st + 0.05) {
        G.projs.splice(i, 1);
        if (p.ally) { if (tgt) { tgt.hp = Math.min(stat(tgt, 'hp'), tgt.hp + p.heal); G.ev.push({ e: 'healed', lane: p.lane, x: tgt.x, y: tgt.y, v: p.heal }); } continue; }
        if (p.side === 1) { if (tgt) damageUnit(G, tgt, p.dmg); G.ev.push({ e: 'chit', lane: p.lane, x: p.tx, y: p.ty, arrow: true }); continue; }
        if (p.splash) { aoeCreeps(G, p.lane, p.tx, p.ty, p.splash, p.dmg, p.dt, p.owner, 0, p.k); }
        else if (tgt) { damageCreep(G, tgt, p.dmg, p.dt, p.owner, p.k); if (p.dot && tgt.hp > 0) { tgt.poison = Math.max(tgt.poison, p.dot); tgt.poisonT = 3; } }
        G.ev.push({ e: 'hit', lane: p.lane, x: p.tx, y: p.ty, k: p.k });
      } else { p.x += dx / dist * st; p.y += dy / dist * st; p.ang = datan2(dy, dx); }
    }
    for (var z = G.zones.length - 1; z >= 0; z--) {
      var Z = G.zones[z]; Z.t -= DT;
      aoeCreeps(G, Z.lane, Z.x, Z.y, Z.r, Z.dps * DT, 'magic', Z.owner, 0, 'poison');
      if (Z.t <= 0) G.zones.splice(z, 1);
    }
    for (var s = G.strikes.length - 1; s >= 0; s--) {
      var S = G.strikes[s]; S.t -= DT;
      if (S.t <= 0) {
        aoeCreeps(G, S.lane, S.x, S.y, S.r, S.dmg, S.dt, S.owner, S.stun || 0, S.fx);
        G.ev.push({ e: 'strike', lane: S.lane, x: S.x, y: S.y, r: S.r, fx: S.fx });
        G.strikes.splice(s, 1);
      }
    }
  }

  function step(G) {
    if (G.over) return;
    G.tick++; G.time += DT;
    if (G.phase === 'build') {
      G.phaseT -= DT;
      if (G.players[0].ready && G.players[1].ready && G.phaseT > 1.2) G.phaseT = 1.2;
      if (G.phaseT <= 0) startFight(G);
      return;
    }
    if (G.phase !== 'fight') return;
    G.fightT += DT;
    for (var lane = 0; lane < 2; lane++) {
      var q = G.spawnQ[lane];
      for (var i = 0; i < q.length; i++) { q[i].t -= DT; }
      while (q.length && q[0].t <= 0) { var s = q.shift(); spawnCreep(G, lane, s.k, s.from); }
    }
    stepUnits(G); stepCreeps(G); stepProjs(G); separate(G);
    for (var l = 0; l < 2; l++) {
      if (!G.laneDone[l] && !G.spawnQ[l].length) {
        var any = false;
        for (var k = 0; k < G.creeps.length; k++) if (G.creeps[k].lane === l) { any = true; break; }
        if (!any) { G.laneDone[l] = true; G.ev.push({ e: 'laneClear', lane: l, perfect: G.waveLeaks[l] === 0 }); }
      }
    }
    if (G.laneDone[0] && G.laneDone[1]) endFight(G);
  }

  // ---- AI đối thủ ----
  function aiThink(G, p, diff) {
    var P = G.players[p];
    if (G.phase !== 'build' || P.ready) return;
    var since = (G.wave === 1 ? 40 : 25) - G.phaseT;
    if (since < (diff === 'easy' ? 4 : 2)) return;
    var rng = G.rng;
    var mine = G.units.filter(function (u) { return u.owner === p; });
    var nextPat = WAVE_PATTERNS[G.wave - 1];
    var armored = nextPat.some(function (x) { return CREEPS[x[0]].armor; });
    var mres = nextPat.some(function (x) { return CREEPS[x[0]].mres; });
    var spendFrac = diff === 'easy' ? 0.7 : 1;
    // phái quân
    var sendEvery = diff === 'hard' ? 2 : diff === 'normal' ? 3 : 99;
    if (G.wave >= 3 && G.wave % sendEvery === 0 && G.wave < 19) {
      var budget = Math.floor(P.gold * (diff === 'hard' ? 0.4 : 0.3));
      for (var s = SEND_ORDER.length - 1; s >= 0; s--) {
        var sk = SEND_ORDER[s];
        while (SENDS[sk].cost <= budget && apply(G, { t: 'send', p: p, k: sk })) budget -= SENDS[sk].cost;
      }
    }
    var reserve = P.gold * (1 - spendFrac);
    var guard = 0;
    while (guard++ < 40) {
      var front = 0, back = 0, sup = 0;
      mine = G.units.filter(function (u) { return u.owner === p; });
      mine.forEach(function (u) { var d = UNITS[u.type]; if (d.melee) front += u.spent; else if (d.heal || d.dot) sup += u.spent; else back += u.spent; });
      var avail = P.gold - reserve;
      // nâng cấp nếu có
      var upCand = mine.filter(function (u) { return u.tier < MAX_TIER && upCost(u) <= avail; });
      if (upCand.length && (mine.length >= 7 || rng() < 0.35)) {
        upCand.sort(function (a, b) { return a.tier - b.tier || UNITS[b.type].cost - UNITS[a.type].cost; });
        if (apply(G, { t: 'upgrade', p: p, id: upCand[0].id })) continue;
      }
      var tot = front + back + sup + 1, pick;
      if (front / tot < 0.42) pick = avail >= 55 && rng() < 0.5 ? 'caibang' : (rng() < 0.55 ? 'thieulam' : 'thienvuong');
      else if (sup / tot < 0.14 && G.wave >= 3) pick = rng() < 0.6 ? 'ngamy' : 'ngudoc';
      else {
        var opts2 = mres ? ['duongmon', 'duongmon', 'vodang'] : armored ? ['vodang', 'conlon', 'ngudoc'] : ['duongmon', 'vodang', 'conlon'];
        if (diff === 'easy') opts2 = ['duongmon', 'vodang', 'conlon', 'ngudoc'];
        pick = opts2[Math.floor(rng() * opts2.length)];
      }
      if (UNITS[pick].cost > avail) {
        var cheap = UNIT_ORDER.filter(function (k) { return UNITS[k].cost <= avail; });
        if (!cheap.length) break;
        pick = cheap[Math.floor(rng() * cheap.length)];
      }
      var d = UNITS[pick];
      var rows = d.melee ? [6, 5, 7, 4] : d.heal ? [9, 10, 8] : [8, 9, 10, 11];
      var placed = false;
      for (var ri = 0; ri < rows.length && !placed; ri++) {
        var xs = [5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10];
        for (var xi = 0; xi < xs.length; xi++) { if (apply(G, { t: 'place', p: p, u: pick, cx: xs[xi], cy: rows[ri] })) { placed = true; break; } }
      }
      if (!placed) break;
    }
    apply(G, { t: 'ready', p: p });
  }

  function checksum(G) {
    var h = G.tick * 31 + G.rs;
    G.units.forEach(function (u) { h = (h * 31 + Math.round(u.x * 100) * 7 + Math.round(u.y * 100) * 13 + Math.round(u.hp)) | 0; });
    G.creeps.forEach(function (c) { h = (h * 31 + Math.round(c.x * 100) * 7 + Math.round(c.y * 100) * 13 + Math.round(c.hp)) | 0; });
    G.players.forEach(function (P) { h = (h * 31 + P.gold * 3 + P.hp * 5 + P.income) | 0; });
    return h;
  }
  var api = { SAVE: SAVE, PATH: PATH, DT: DT, LANE_W: LANE_W, BUILD_Y0: BUILD_Y0, BUILD_Y1: BUILD_Y1, LEAK_Y: LEAK_Y, GATE_Y: GATE_Y, MAX_WAVE: MAX_WAVE,
    UNITS: UNITS, UNIT_ORDER: UNIT_ORDER, CREEPS: CREEPS, SENDS: SENDS, SEND_ORDER: SEND_ORDER, WAVE_PATTERNS: WAVE_PATTERNS,
    upCost: upCost, MAX_TIER: MAX_TIER, checksum: checksum, dsin: dsin, datan2: datan2, create: create, apply: apply, step: step, aiThink: aiThink, stat: stat, findUnit: findUnit, findCreep: findCreep, hpScale: hpScale };
  if (typeof module !== 'undefined') module.exports = api;
  return api;
})();
