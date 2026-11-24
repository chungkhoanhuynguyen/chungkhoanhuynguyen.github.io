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

  // ---- Nguyên mẫu chiến đấu (dùng để sinh tướng cho từng hệ phái) ----
  var ARCH = {
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
      up: { name: 'Nga My Tiên Tử', cost: 60, hp: 270, dmg: 15, heal: 20, amt: 140 } },
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
  ARCH.summonR = { cost: 35, hp: 130, dmg: 12, cd: 1.2, range: 4.0, spd: 2.1, dt: 'magic', proj: 'petal', skill: { type: 'summon', n: 3, life: 16, smul: 0.6, cd: 99 } };
  ARCH.summonM = { cost: 40, hp: 340, dmg: 18, cd: 1.1, range: 0.95, spd: 2.2, melee: true, dt: 'phys', armor: 0.1, skill: { type: 'summon', n: 2, life: 16, smul: 0.55, cd: 99, tank: 1 } };
  var ROLE = { thienvuong: 'Cận chiến chém lan', thieulam: 'Đỡ đòn, làm choáng', duongmon: 'Ám khí tầm xa', ngudoc: 'Độc sát thương theo thời gian', ngamy: 'Hồi máu đồng môn', vodang: 'Kiếm khí đánh lan', conlon: 'Sét lan nhiều mục tiêu', caibang: 'Chưởng xuyên hàng sát thương lớn', summonR: 'Tầm xa · dùng nội lực triệu hồi đệ tử cận chiến', summonM: 'Cận chiến · dùng nội lực triệu hồi đệ tử đỡ đòn' };
  // Tướng càng đắt càng "lời" sức mạnh trên mỗi lượng vàng => phải dùng tướng mạnh + nâng cấp mới qua được đợt cuối
  function eff(c) { return Math.pow(c / 15, 0.3); }
  var UNITS = {}, SECTS = {}, SECT_ORDER = [];
  var COST = [15, 20, 25, 30, 35, 45, 55, 70];
  var SKN = { thienvuong: 'Toàn Phong Trảm', thieulam: 'Trấn Địa Chưởng', duongmon: 'Phi Châm Tán Hoa', ngudoc: 'Độc Vụ Mê Hồn', ngamy: 'Hồi Xuân Thuật', vodang: 'Kiếm Vũ Phi Tiên', conlon: 'Ngũ Lôi Chính Pháp', caibang: 'Kháng Long Hữu Hối', summonR: 'Triệu Đệ Tử', summonM: 'Triệu Hộ Vệ' };
  var AW = { thieulam: 'staff', duongmon: 'dart', ngudoc: 'claw', ngamy: 'fan', vodang: 'sword', conlon: 'talisman', summonR: 'talisman' };
  function shadeHex(h, k) { var n = parseInt(h.slice(1), 16), r = n >> 16, g = n >> 8 & 255, b = n & 255; function f(v) { return Math.max(0, Math.min(255, Math.round(k > 0 ? v + (255 - v) * k : v * (1 + k)))); } return '#' + ((1 << 24) + (f(r) << 16) + (f(g) << 8) + f(b)).toString(16).slice(1); }
  // S: { k, name, ch, col, col2, pw (độ mạnh), motto, look:{skin,hair,hat,trim,female?,alt:[hat nữ]}, wp (vũ khí sở trường), fem:[slot nữ], u:[[tên, nguyên mẫu, (tuyệt chiêu), (ghi đè)] x8], ult:{...tuyệt kỹ chưởng môn} }
  function sect(S) {
    var keys = [];
    // chỉ vài phái có thuật triệu hồi (Ngũ Độc, Bạch Đà Sơn, Toàn Chân); phái khác đổi sang lối đánh của phái
    if (SUMMON_OK.indexOf(S.k) < 0) S.u = S.u.map(function (a) { if (a[1] !== 'summonR' && a[1] !== 'summonM') return a;
      var na = a[1] === 'summonR' ? (S.wp === 'dart' || S.wp === 'fan' ? 'duongmon' : S.wp === 'talisman' || S.wp === 'staff' ? 'conlon' : 'vodang') : 'caibang';
      var o = a[3] ? Object.assign({}, a[3]) : null; if (o) { delete o.proj; delete o.dt; delete o.dot; }
      return [a[0], na, /Triệu|Trận|Hiệu/.test(a[2] || '') ? null : a[2], o]; });
    S.u.forEach(function (a, i) {
      var k = S.k + '_' + i, b = ARCH[a[1]], cost = COST[i], m = (cost / b.cost) * eff(cost) / eff(b.cost) * S.pw, u = {};
      for (var f in b) u[f] = b[f];
      u.skill = {}; for (var f2 in b.skill) u.skill[f2] = b.skill[f2];
      u.name = a[0]; u.arch = a[1]; u.cost = cost; u.sect = S.k; u.slot = i; u.role = ROLE[a[1]];
      u.hp = Math.round(b.hp * m); u.dmg = Math.round(b.dmg * m * 10) / 10;
      if (b.heal) u.heal = Math.round(b.heal * m); if (b.dot) u.dot = Math.round(b.dot * m);
      if (b.skill.amt) u.skill.amt = Math.round(b.skill.amt * m); if (b.skill.dps) u.skill.dps = Math.round(b.skill.dps * m);
      u.skill.name = a[2] || SKN[a[1]]; u.up = { name: a[0] + ' · Đại Thành' };
      var fem = S.fem.indexOf(i) >= 0, L0 = S.look, C = COSTUME[S.k] || {};
      // TRANG PHỤC CHUẨN THEO PHÁI: mũ/tóc, màu áo, phụ kiện (cà sa, chuỗi hạt, hồ lô...), vũ khí sở trường
      var pal = C.robes || [S.col, shadeHex(S.col, -0.15), shadeHex(S.col, 0.12)], robe = pal[i % pal.length];
      var hat = fem ? (C.fhat || L0.fhat || 'longhair') : (C.hat || L0.hat);
      if (C.hat7 && i === 7 && !fem) hat = C.hat7; if (C.fhat7 && i === 7 && fem) hat = C.fhat7;
      var skins = ['#f0c8a2', '#e8b890', '#f3d0b0', '#d9a77c', '#efc39e', '#e3b48c', '#f6d5bd', '#eec5a0'];
      u.look = { skin: fem ? '#f6d5bd' : skins[i], hair: i >= 6 && !fem ? '#d8d2c8' : (C.hair || L0.hair), hat: hat, robe: robe, robe2: C.robe2 || S.col2, trim: i >= 6 ? (C.trim7 || '#ffd54f') : (C.trim || L0.trim), female: fem,
        sash: C.sash || L0.sash, mask: !fem && (C.mask || L0.mask), armor: !fem && (C.armor === true || (C.armor === 'tank' && (a[1] === 'thieulam' || a[1] === 'summonM'))), patches: C.patches || L0.patches,
        kasaya: C.kasaya && !(fem && !C.fkasaya) ? C.kasaya : null, beads: C.beads && (i >= 2 || C.beadsAll) ? C.beads : null, gourd: C.gourd || null, collar: C.collar || null };
      if (fem && /Ni Cô|Nữ Ni|Sư Thái/.test(a[0])) { u.look.hat = 'hood'; u.look.beads = '#6d4c41'; }
      if (hat === 'bald') u.look.hair = null;
      u.cape = i >= 6 && C.cape !== false ? (C.cape || shadeHex(S.col, -0.3)) : null;
      var cw = C.wp || {};
      u.weapon = (a[3] && a[3].weapon) || (i === 7 && C.wp7) || cw[a[1]] || C.w || (a[1] === 'thieulam' ? (S.wp === 'staff' || S.wp === 'stick' ? S.wp : 'shield') : AW[a[1]]) || S.wp;
      u.col = S.col; u.col2 = S.col2; u.ch = S.ch; u.fxc = S.fxc || S.col;
      if (i === 7 && S.ult) { for (var f4 in S.ult) u.skill[f4] = S.ult[f4]; u.ult = true; u.wglow = S.fxc || S.col; u.up = { name: S.ult.title || a[0] }; }
      if (a[3]) for (var f3 in a[3]) if (f3 !== 'weapon') u[f3] = a[3][f3];
      UNITS[k] = u; keys.push(k);
    });
    S.u.forEach(function (a, i) { var u = UNITS[keys[i]]; if (u.skill.type === 'summon') u.skill.unit = u.skill.tank ? keys[1] : keys[0]; });
    SECTS[S.k] = { name: S.name, motto: S.motto, col: S.col, ch: S.ch, pw: S.pw, units: keys, ult: S.ult && S.ult.name }; SECT_ORDER.push(S.k);
  }
  // Trang phục theo phái (tham khảo hình tượng kiếm hiệp quen thuộc)
  var SUMMON_OK = ['ngudoc', 'bachda', 'toanchan'];
  var COSTUME = {
    thieulam: { hat: 'bald', robes: ['#e3a046', '#d68a2e', '#e9b05a'], robe2: '#7a3a10', trim: '#ffd54f', sash: '#b71c1c', kasaya: '#b71c1c', beads: '#4e342e', beadsAll: true, w: 'staff', wp: { thienvuong: 'stick', summonR: 'ringstaff', ngamy: 'ringstaff' }, wp7: 'ringstaff', cape: false, trim7: '#ffd54f' },
    thienvuong: { hat: 'ironhelm', hat7: 'helmet', robes: ['#b8860b', '#8d6e1a', '#c9a23a'], robe2: '#4a3410', trim: '#ffe08a', armor: true, w: 'hammer', wp: { thienvuong: 'axe', duongmon: 'bow', caibang: 'spear', thieulam: 'shield' } },
    duongmon: { hat: 'hood', fhat: 'ponytail', robes: ['#2e7d5b', '#1f5a40', '#3d8f6a'], robe2: '#0f3324', trim: '#c9e6b0', mask: true, w: 'dart', wp: { thienvuong: 'saber', thieulam: 'shield' }, cape: '#0f3324' },
    ngudoc: { hat: 'headdress', fhat: 'headdress', robes: ['#5e2f8e', '#3d1b5e', '#7b4bb0'], robe2: '#1a0a2a', trim: '#c0c0c0', beads: '#c0c0c0', w: 'claw', collar: '#c0c0c0' },
    ngamy: { hat: 'bald', fhat: 'longhair', fhat7: 'longhair', robes: ['#f8bbd0', '#f06292', '#fff0f5'], robe2: '#ad1457', trim: '#ffd1e3', w: 'sword', wp: { ngamy: 'fan', thieulam: 'staff' }, wp7: 'sword' },
    thuyyen: { fhat: 'ponytail', robes: ['#4db6ac', '#26a69a', '#b2dfdb'], robe2: '#004d40', trim: '#e0f2f1', w: 'twin', wp: { duongmon: 'fan', ngamy: 'fan', summonR: 'fan' } },
    caibang: { hat: 'messy', fhat: 'ponytail', robes: ['#8d6e63', '#6d4c41', '#a1887f'], robe2: '#3e2723', trim: '#7cb342', patches: true, gourd: '#c89b3c', w: 'stick', wp: { duongmon: 'dart' }, cape: false },
    thiennhan: { hat: 'hood', fhat: 'hood', robes: ['#b71c1c', '#7f0000', '#212121'], robe2: '#0a0000', trim: '#ff8a65', mask: true, armor: 'tank', w: 'spear', wp: { ngudoc: 'talisman', conlon: 'talisman' } },
    vodang: { hat: 'taoist', fhat: 'ponytail', robes: ['#3f7fc6', '#e3eef9', '#2d5f99'], robe2: '#e9f2ff', trim: '#ffffff', collar: '#ffffff', w: 'sword', wp: { conlon: 'talisman' } },
    conlon: { hat: 'taoist', fhat: 'longhair', robes: ['#0097a7', '#006978', '#4dd0e1'], robe2: '#08333b', trim: '#ffeb3b', collar: '#ffeb3b', w: 'sword', wp: { conlon: 'talisman', summonR: 'talisman' } },
    tinhtuc: { hat: 'messy', fhat: 'longhair', robes: ['#673ab7', '#4527a0', '#311b92'], robe2: '#12052a', trim: '#e1bee7', w: 'claw', wp: { vodang: 'sword', conlon: 'fan' } },
    hoason: { hat: 'topknot', fhat: 'ponytail', robes: ['#eceff1', '#90a4ae', '#cfd8dc'], robe2: '#37474f', trim: '#546e7a', w: 'sword' },
    minhgiao: { hat: 'hood', fhat: 'hood', robes: ['#e65100', '#bf360c', '#ff8f00'], robe2: '#3e1200', trim: '#ffd54f', w: 'saber', wp: { conlon: 'talisman', duongmon: 'bow' }, cape: '#bf360c' },
    tieudao: { hat: 'topknot', fhat: 'longhair', robes: ['#e8f5e9', '#81c784', '#c8e6c9'], robe2: '#2e7d32', trim: '#fff59d', w: 'fan' },
    doanthi: { hat: 'topknot', hat7: 'crown', fhat: 'crown', robes: ['#fbc02d', '#f9a825', '#fff176'], robe2: '#6d4c41', trim: '#ffffff', w: 'sword', cape: '#c62828' },
    comoo: { hat: 'topknot', fhat: 'longhair', robes: ['#fafafa', '#eceff1', '#f5f5f5'], robe2: '#90a4ae', trim: '#b0bec5', w: 'sword' },
    nhatnguyet: { hat: 'hood', fhat: 'ponytail', robes: ['#880e4f', '#4a0026', '#ad1457'], robe2: '#1a0010', trim: '#ffd54f', w: 'saber', wp: { duongmon: 'dart' } },
    toanchan: { hat: 'taoist', fhat: 'ponytail', robes: ['#5c6bc0', '#e8eaf6', '#3949ab'], robe2: '#1a237e', trim: '#ffffff', collar: '#ffffff', w: 'sword', wp: { conlon: 'talisman' } },
    bachda: { hat: 'messy', fhat: 'longhair', robes: ['#f5f5f5', '#d7ccc8', '#efebe9'], robe2: '#5d4037', trim: '#aeea00', w: 'stick', wp: { ngudoc: 'claw' } },
    daohoa: { hat: 'topknot', fhat: 'longhair', robes: ['#f48fb1', '#a5d6a7', '#fce4ec'], robe2: '#2e7d32', trim: '#ffffff', w: 'sword', wp: { duongmon: 'dart', ngamy: 'fan', conlon: 'fan' } },
    modung: { hat: 'topknot', fhat: 'longhair', robes: ['#3949ab', '#283593', '#5c6bc0'], robe2: '#0d1240', trim: '#c5cae9', w: 'sword' }
  };
  var LK = function (skin, hair, hat, trim, x) { var o = { skin: skin, hair: hair, hat: hat, trim: trim }; for (var k in x) o[k] = x[k]; return o; };
  sect({ k: 'thieulam', name: 'Thiếu Lâm', ch: '少', col: '#e8a33d', col2: '#8b3a0e', pw: 1.02, wp: 'staff', fem: [], motto: 'Phật môn chính tông · đỡ đòn cứng, chưởng lực bao trùm',
    look: LK('#f0c49a', null, 'bald', '#c0392b', { sash: '#c0392b' }), fxc: '#ffca28',
    u: [['Tiểu Sa Di', 'thienvuong', 'La Hán Quyền', { weapon: 'stick' }], ['La Hán Đường', 'thieulam', 'Kim Cương Chưởng'], ['Hộ Tự Võ Tăng', 'summonM', 'Triệu Tập La Hán'], ['Giới Đao Tăng', 'thienvuong', 'Nhiên Mộc Đao Pháp', { weapon: 'saber' }],
        ['Đạt Ma Viện Thủ Toạ', 'summonR', 'Bách Tăng Trận', { proj: 'dart', dt: 'phys' }], ['Dịch Cân Kinh Tăng', 'ngamy', 'Dịch Cân Hồi Xuân'], ['Kim Cương Hộ Pháp', 'thieulam', 'Sư Tử Hống', { weapon: 'hammer', armor: 0.3 }], ['Phương Trượng', 'thieulam']],
    ult: { name: 'Giáng Long Thập Bát Chưởng', type: 'shock', r: 3.4, mult: 3.2, stun: 1.6, cd: 8, big: 1, title: 'Vạn Phật Triều Tông' } });
  sect({ k: 'thienvuong', name: 'Thiên Vương', ch: '天', col: '#d4a017', col2: '#6b3f10', pw: 1.0, wp: 'hammer', fem: [4], motto: 'Bang hội thuỷ trại · cận chiến bạo lực, chém lan',
    look: LK('#e8b890', '#2a1a10', 'helmet', '#ffe08a', { armor: true }), fxc: '#ffd740',
    u: [['Thuỷ Binh', 'thienvuong', 'Phá Lãng Trảm', { weapon: 'saber' }], ['Thiết Thuẫn Vệ', 'thieulam', 'Kim Chung Tráo', { weapon: 'shield' }], ['Thương Kỵ', 'thienvuong', 'Đoạt Hồn Thương', { weapon: 'spear' }], ['Truy Tinh Cung Thủ', 'duongmon', 'Truy Tinh Tiễn', { weapon: 'bow' }],
        ['Thuỷ Trại Đầu Lĩnh', 'summonM', 'Hiệu Triệu Thuỷ Binh'], ['Phá Thiên Chuỳ', 'thienvuong', 'Phá Thiên Trảm'], ['Bá Vương Thương', 'caibang', 'Bá Vương Thương Pháp', { weapon: 'spear' }], ['Thiên Vương Bang Chủ', 'thienvuong']],
    ult: { name: 'Thiên Vương Chiến Ý', type: 'whirl', r: 3.0, mult: 3.4, cd: 6, big: 1, title: 'Bá Chủ Thiên Vương' } });
  sect({ k: 'duongmon', name: 'Đường Môn', ch: '唐', col: '#2e7d5b', col2: '#0f3324', pw: 1.04, wp: 'dart', fem: [2, 5], motto: 'Thế gia Tứ Xuyên · ám khí tầm xa sát thương dồn dập',
    look: LK('#eac39d', '#151515', 'hood', '#c9e6b0', { mask: true }), fxc: '#b2ff59',
    u: [['Gia Đinh Đường Gia', 'thienvuong', 'Phi Đao Loạn Trảm', { weapon: 'saber' }], ['Thiết Giáp Thủ Vệ', 'thieulam', 'Cơ Quan Trấn'], ['Phi Đao Nữ Hiệp', 'duongmon', 'Liễu Diệp Phi Đao'], ['Cơ Quan Sư', 'conlon', 'Tích Lịch Đạn'],
        ['Độc Châm Thích Khách', 'duongmon', 'Truy Hồn Châm'], ['Đường Gia Tiểu Thư', 'summonR', 'Triệu Gia Đinh', { proj: 'dart', dt: 'phys' }], ['Ám Khí Đại Sư', 'duongmon', 'Thiên La Địa Võng'], ['Đường Môn Môn Chủ', 'duongmon']],
    ult: { name: 'Bạo Vũ Lê Hoa Châm', type: 'fan', n: 21, sp: 0.075, mult: 1.4, cd: 5, big: 1, title: 'Ám Khí Tông Sư' } });
  sect({ k: 'ngudoc', name: 'Ngũ Độc', ch: '毒', col: '#6a3d9a', col2: '#24103a', pw: 1.08, wp: 'claw', fem: [1, 4, 7], motto: 'Giáo phái Miêu Cương · kịch độc, triệu hồi đệ tử trùng độc',
    look: LK('#e7c0a0', '#1a0f20', 'headdress', '#b3ff6a', { fhat: 'headdress' }), fxc: '#76ff03',
    u: [['Độc Nhân', 'thienvuong', 'Độc Trảo'], ['Độc Nữ Hộ Giáo', 'thieulam', 'Thi Độc Chấn Địa'], ['Xà Cơ', 'summonR', 'Vạn Xà Triệu Hồi', { proj: 'poison', dot: 5 }], ['Ngũ Độc Độc Sư', 'ngudoc', 'Vạn Độc Vụ'],
        ['Cổ Nữ', 'summonR', 'Thiên Cổ Triệu Đồ', { proj: 'poison', dot: 7 }], ['Thiết Thi Vương', 'summonM', 'Thi Vương Hiệu Triệu'], ['Độc Vương Hộ Pháp', 'ngudoc', 'Hủ Cốt Độc Vụ'], ['Ngũ Độc Giáo Chủ', 'summonR', null, { proj: 'poison', dot: 10 }]],
    ult: { name: 'Vạn Độc Triệu Đệ Tử', type: 'summon', n: 5, life: 22, smul: 0.85, cd: 99, title: 'Độc Tôn Thiên Hạ' } });
  sect({ k: 'ngamy', name: 'Nga My', ch: '峨', col: '#f06292', col2: '#7b1f45', pw: 0.97, wp: 'sword', fem: [0, 1, 2, 3, 4, 5, 6, 7], motto: 'Nữ hiệp Phật môn · hồi máu, bông sen, kiếm pháp nhu hoà',
    look: LK('#f6d5bd', '#120c0c', 'longhair', '#ffd1e3'), fxc: '#ff80ab',
    u: [['Tiểu Ni Cô', 'thienvuong', 'Phất Trần Quét'], ['Hộ Pháp Nữ Ni', 'thieulam', 'Kim Đỉnh Phật Quang', { weapon: 'staff' }], ['Nga My Kiếm Nữ', 'vodang', 'Phiêu Tuyết Xuyên Vân'], ['Nga My Y Nữ', 'ngamy', 'Phổ Độ Chúng Sinh'],
        ['Cầm Tiên', 'summonR', 'Thiên Âm Triệu Đồ', { weapon: 'fan' }], ['Hoa Vũ Tiên Tử', 'duongmon', 'Hoa Vũ Mãn Thiên', { proj: 'petal', dt: 'magic', weapon: 'fan' }], ['Tuệ Tâm Sư Thái', 'ngamy', 'Đại Bi Quán Âm'], ['Chưởng Môn Nga My', 'ngamy']],
    ult: { name: 'Liên Hoa Phổ Độ', type: 'massheal', r: 4.2, amt: 260, cd: 8, dmgmult: 2.6, big: 1, title: 'Nga My Thánh Nữ' } });
  sect({ k: 'thuyyen', name: 'Thuý Yên', ch: '翠', col: '#26a69a', col2: '#004d40', pw: 1.0, wp: 'sword', fem: [0, 1, 2, 3, 4, 5, 6, 7], motto: 'Tiên nữ Đại Lý · băng tuyết làm chậm, song đao uyển chuyển',
    look: LK('#f6d5bd', '#0c1210', 'longhair', '#e0f2f1'), fxc: '#80deea',
    u: [['Thuý Yên Môn Đồ', 'thienvuong', 'Song Đao Hồi Phong', { weapon: 'twin' }], ['Băng Tâm Hộ Vệ', 'thieulam', 'Băng Phong Trấn'], ['Phi Hoa Nữ Hiệp', 'duongmon', 'Phi Hoa Tống Ngọc', { proj: 'petal', dt: 'magic', weapon: 'fan' }], ['Tuyết Liên Y Nữ', 'ngamy', 'Tuyết Liên Hồi Xuân'],
        ['Băng Kiếm Tiên Tử', 'vodang', 'Băng Tâm Kiếm Vũ'], ['Cầm Ca Tiên Nữ', 'summonR', 'Lăng Ba Triệu Muội', { weapon: 'fan' }], ['Hàn Băng Song Đao', 'caibang', 'Phong Hoa Tuyết Nguyệt', { weapon: 'twin' }], ['Thuý Yên Chưởng Môn', 'vodang']],
    ult: { name: 'Tuyết Ảnh Phi Hoa', type: 'swordrain', r: 3.0, n: 18, mult: 1.0, cd: 7, slow: 1, big: 1, title: 'Băng Tâm Tiên Tử' } });
  sect({ k: 'caibang', name: 'Cái Bang', ch: '丐', col: '#a1887f', col2: '#4e342e', pw: 1.03, wp: 'stick', fem: [3], motto: 'Thiên hạ đệ nhất bang · chưởng rồng xuyên hàng, máu trâu',
    look: LK('#d9a77c', '#3a2612', 'messy', '#7cb342', { patches: true }), fxc: '#ffd740',
    u: [['Tiểu Khất Cái', 'thienvuong', 'Đả Cẩu Bổng'], ['Ô Y Đệ Tử', 'thieulam', 'Bổng Trấn'], ['Bố Đại Trưởng Lão', 'summonM', 'Hiệu Triệu Khất Cái'], ['Nữ Khất Hiệp', 'duongmon', 'Liên Hoàn Phi Thạch'],
        ['Chấp Pháp Trưởng Lão', 'caibang', 'Kiến Long Tại Điền'], ['Tửu Cái', 'thienvuong', 'Tuý Bát Tiên'], ['Cửu Đại Trưởng Lão', 'caibang', 'Phi Long Tại Thiên'], ['Cái Bang Bang Chủ', 'caibang']],
    ult: { name: 'Cửu Long Xuất Hải', type: 'dragon', n: 9, spread: 1.25, len: 11, w: 1.0, mult: 2.8, cd: 9, big: 1, title: 'Thiên Hạ Đệ Nhất Bang Chủ' } });
  sect({ k: 'thiennhan', name: 'Thiên Nhẫn', ch: '忍', col: '#c62828', col2: '#1a0000', pw: 1.02, wp: 'spear', fem: [2, 5], motto: 'Thần giáo Kim quốc · hoả công thiêu đốt diện rộng',
    look: LK('#e0b48c', '#111', 'hood', '#ff8a65', { mask: true }), fxc: '#ff6d00',
    u: [['Thiên Nhẫn Giáo Đồ', 'thienvuong', 'Liệt Hoả Thương', { weapon: 'spear' }], ['Hắc Giáp Hộ Giáo', 'thieulam', 'Hắc Viêm Trấn'], ['Hoả Vũ Nữ', 'ngudoc', 'Hoả Vân Thiêu', { proj: 'poison' }], ['Ma Diễm Pháp Sư', 'conlon', 'Ma Diễm Liên Hoàn'],
        ['Huyết Ảnh Sát Thủ', 'thienvuong', 'Huyết Ảnh Trảm', { weapon: 'saber' }], ['Hoả Tế Ti', 'summonR', 'Triệu Giáo Đồ'], ['Thiên Hoả Trưởng Lão', 'ngudoc', 'Liệt Diễm Phần Thiên'], ['Thiên Nhẫn Giáo Chủ', 'ngudoc']],
    ult: { name: 'Thiên Hoả Liệu Nguyên', type: 'cloud', r: 3.2, dps: 70, dur: 5, cd: 8, fire: 1, big: 1, title: 'Hoả Thần Thiên Nhẫn' } });
  sect({ k: 'vodang', name: 'Võ Đang', ch: '武', col: '#4a90d9', col2: '#1b3a66', pw: 1.03, wp: 'sword', fem: [2], motto: 'Đạo gia chính tông · kiếm khí gió trắng xanh, đánh lan',
    look: LK('#efc8a2', '#161616', 'topknot', '#ffffff'), fxc: '#4fc3f7',
    u: [['Đạo Đồng', 'thienvuong', 'Thái Cực Quyền'], ['Chân Vũ Thủ Vệ', 'thieulam', 'Chân Vũ Trấn Thế'], ['Kiếm Đồng', 'vodang', 'Kiếm Khí Tung Hoành'], ['Phù Lục Đạo Sĩ', 'conlon', 'Ngũ Lôi Phù'],
        ['Thất Tiệt Trận Chủ', 'summonR', 'Chân Vũ Thất Tiệt Trận', { proj: 'sword', weapon: 'sword' }], ['Võ Đang Kiếm Khách', 'vodang', 'Thái Cực Kiếm Ý'], ['Thái Cực Đạo Trưởng', 'caibang', 'Thái Cực Âm Dương', { weapon: 'sword' }], ['Võ Đang Chưởng Môn', 'vodang']],
    ult: { name: 'Vạn Kiếm Quy Tông', type: 'swordrain', r: 3.2, n: 22, mult: 1.05, cd: 7, wind: 1, big: 1, title: 'Đạo Tổ Tam Phong' } });
  sect({ k: 'conlon', name: 'Côn Lôn', ch: '崑', col: '#00acc1', col2: '#08333b', pw: 1.02, wp: 'talisman', fem: [5], motto: 'Đạo phái Tây Vực · lôi pháp, sét lan nhiều mục tiêu',
    look: LK('#eec5a0', '#202020', 'taoist', '#ffeb3b'), fxc: '#40c4ff',
    u: [['Côn Lôn Đệ Tử', 'thienvuong', 'Lôi Quyền', { weapon: 'sword' }], ['Thiết Phù Hộ Pháp', 'thieulam', 'Trấn Sơn Phù'], ['Phong Lôi Đạo Đồng', 'conlon', 'Chưởng Tâm Lôi'], ['Ngự Phong Kiếm Khách', 'vodang', 'Ngự Phong Kiếm'],
        ['Lôi Phù Đạo Trưởng', 'conlon', 'Ngũ Lôi Oanh Đỉnh'], ['Tiên Hạc Đạo Cô', 'summonR', 'Triệu Đạo Binh'], ['Lôi Đình Chân Nhân', 'conlon', 'Cửu Thiên Lôi Động'], ['Côn Lôn Chưởng Môn', 'conlon']],
    ult: { name: 'Lôi Động Cửu Thiên', type: 'thunder', r: 2.0, n: 7, mult: 3.4, cd: 7, big: 1, title: 'Cửu Thiên Lôi Thần' } });
  sect({ k: 'tinhtuc', name: 'Tinh Túc', ch: '星', col: '#7e57c2', col2: '#1a0f3a', pw: 0.96, wp: 'sword', fem: [3, 6], motto: 'Tà phái Tây Hạ · tinh kiếm từ trời, độc chưởng',
    look: LK('#e3c0a8', '#0c0814', 'messy', '#e1bee7'), fxc: '#b388ff',
    u: [['Tinh Túc Đệ Tử', 'thienvuong', 'Hoá Công Chưởng'], ['Đại Lực Hộ Pháp', 'thieulam', 'Hấp Tinh Trấn'], ['Tinh Kiếm Đồ', 'vodang', 'Tinh Quang Kiếm'], ['Độc Chưởng Nữ', 'ngudoc', 'Hủ Thi Độc'],
        ['Mê Hồn Sư', 'summonR', 'Triệu Tinh Đồ'], ['Tinh La Kiếm Khách', 'vodang', 'Tinh La Kiếm Trận'], ['Tinh Túc Thánh Nữ', 'conlon', 'Tinh Thần Lôi'], ['Tinh Túc Lão Tiên', 'vodang']],
    ult: { name: 'Tinh Túc Kiếm Vũ', type: 'swordrain', r: 3.4, n: 26, mult: 1.0, cd: 7, big: 1, title: 'Tinh Túc Lão Quái' } });
  sect({ k: 'hoason', name: 'Hoa Sơn', ch: '華', col: '#90a4ae', col2: '#263238', pw: 1.0, wp: 'sword', fem: [3], motto: 'Ngũ Nhạc kiếm phái · kiếm pháp cận chiến tinh xảo',
    look: LK('#efc8a2', '#141414', 'topknot', '#eceff1'), fxc: '#80d8ff',
    u: [['Hoa Sơn Kiếm Đồ', 'thienvuong', 'Hữu Phượng Lai Nghi'], ['Kiếm Tông Thủ Vệ', 'thieulam', 'Kiếm Trận Thủ'], ['Khí Tông Đệ Tử', 'vodang', 'Tử Hà Kiếm Khí'], ['Ngọc Nữ Kiếm', 'duongmon', 'Ngọc Nữ Tố Tâm', { proj: 'sword', dt: 'magic' }],
        ['Hoa Sơn Sư Huynh', 'summonM', 'Hiệu Triệu Sư Đệ'], ['Cuồng Phong Kiếm', 'thienvuong', 'Cuồng Phong Khoái Kiếm'], ['Tử Hà Kiếm Khách', 'caibang', 'Tử Hà Thần Công', { weapon: 'sword' }], ['Phong Thanh Dương', 'thienvuong']],
    ult: { name: 'Độc Cô Cửu Kiếm', type: 'whirl', r: 3.2, mult: 4.4, cd: 5, sword: 1, big: 1, title: 'Kiếm Thánh Hoa Sơn' } });
  sect({ k: 'minhgiao', name: 'Minh Giáo', ch: '明', col: '#ef6c00', col2: '#3e1200', pw: 1.04, wp: 'saber', fem: [5], motto: 'Thánh hoả giáo phái · lửa thiêng, cột lửa nện xuống',
    look: LK('#d9a77c', '#1a0a00', 'nonla', '#ffd54f'), fxc: '#ff9100',
    u: [['Minh Giáo Giáo Đồ', 'thienvuong', 'Thánh Hoả Đao'], ['Hộ Giáo Pháp Vương', 'thieulam', 'Hoả Diễm Thuẫn'], ['Ngũ Hành Kỳ Sứ', 'conlon', 'Ngũ Hành Hoả Phù'], ['Thánh Hoả Cung Thủ', 'duongmon', 'Hoả Tiễn', { weapon: 'bow' }],
        ['Tán Nhân', 'summonM', 'Hiệu Triệu Giáo Đồ'], ['Ba Tư Thánh Nữ', 'ngudoc', 'Thánh Hoả Liệu Nguyên', { proj: 'poison' }], ['Quang Minh Hữu Sứ', 'caibang', 'Càn Khôn Đại Na Di', { weapon: 'saber' }], ['Minh Giáo Giáo Chủ', 'conlon']],
    ult: { name: 'Thánh Hoả Lệnh', type: 'thunder', r: 2.2, n: 6, mult: 3.6, cd: 7, fire: 1, big: 1, title: 'Quang Minh Giáo Chủ' } });
  sect({ k: 'tieudao', name: 'Tiêu Dao', ch: '逍', col: '#66bb6a', col2: '#1b3d1e', pw: 1.03, wp: 'fan', fem: [1, 4, 6], motto: 'Ẩn môn thần bí · chưởng khí lan, khống chế, triệu hồi',
    look: LK('#f0cba8', '#ececec', 'topknot', '#fff59d'), fxc: '#b2ff59',
    u: [['Tiêu Dao Đồng Tử', 'thienvuong', 'Thiên Sơn Chiết Mai Thủ'], ['Lăng Ba Thị Nữ', 'thieulam', 'Lăng Ba Vi Bộ'], ['Bắc Minh Đệ Tử', 'conlon', 'Bắc Minh Thần Công'], ['Cầm Kỳ Thư Sĩ', 'summonR', 'Triệu Đồng Tử'],
        ['Thiên Sơn Đồng Lão', 'ngudoc', 'Sinh Tử Phù', { proj: 'petal' }], ['Họa Tiên', 'duongmon', 'Thần Bút Điểm Huyệt', { proj: 'petal', dt: 'magic' }], ['Lý Thu Thuỷ', 'conlon', 'Bạch Hồng Chưởng'], ['Tiêu Dao Tử', 'conlon']],
    ult: { name: 'Thiên Sơn Lục Dương Chưởng', type: 'thunder', r: 2.4, n: 6, mult: 2.6, stun: 1.4, cd: 7, jade: 1, big: 1, title: 'Tiêu Dao Thần Tiên' } });
  sect({ k: 'doanthi', name: 'Đoàn Thị', ch: '段', col: '#fbc02d', col2: '#5d4037', pw: 1.01, wp: 'sword', fem: [4], motto: 'Hoàng tộc Đại Lý · chỉ lực kiếm khí bắn xuyên',
    look: LK('#f0c8a0', '#141010', 'topknot', '#ffffff'), fxc: '#ffd740',
    u: [['Đại Lý Thị Vệ', 'thienvuong', 'Ngự Tiền Đao', { weapon: 'saber' }], ['Thiên Long Tự Tăng', 'thieulam', 'Thiên Long Trấn', { weapon: 'staff' }], ['Nhất Dương Chỉ Đệ Tử', 'duongmon', 'Nhất Dương Chỉ', { proj: 'sword', dt: 'magic' }], ['Hoàng Gia Ngự Y', 'ngamy', 'Hoàng Gia Linh Dược'],
        ['Quận Chúa Đại Lý', 'summonR', 'Triệu Thị Vệ'], ['Thiên Long Kiếm Khách', 'vodang', 'Thiên Long Kiếm'], ['Nhất Đăng Đại Sư', 'conlon', 'Tiên Thiên Công'], ['Đoàn Dự', 'duongmon', null, { proj: 'sword', dt: 'magic' }]],
    ult: { name: 'Lục Mạch Thần Kiếm', type: 'fan', n: 6, sp: 0.16, mult: 4.0, cd: 4, sword: 1, big: 1, title: 'Thiên Long Hoàng Đế' } });
  // ---- Các phái nhỏ (kiếm hiệp Kim Dung) ----
  sect({ k: 'comoo', name: 'Cổ Mộ', ch: '墓', col: '#eceff1', col2: '#37474f', pw: 0.97, wp: 'sword', fem: [0, 2, 4, 5, 7], motto: 'Mộ cổ Chung Nam · Ngọc Nữ Tâm Kinh, ong ngọc độc châm',
    look: LK('#f0d0b8', '#0a0a0a', 'longhair', '#b0bec5'), fxc: '#ffe57f',
    u: [['Cổ Mộ Thị Nữ', 'thienvuong', 'Thiên La Địa Võng Thủ'], ['Thủ Mộ Nhân', 'thieulam', 'Huyền Thiết Trấn', { weapon: 'sword' }], ['Ngọc Phong Nữ', 'summonR', 'Triệu Thị Nữ', { proj: 'petal' }], ['Huyền Thiết Kiếm Khách', 'caibang', 'Huyền Thiết Trọng Kiếm', { weapon: 'sword' }],
        ['Ngọc Nữ Kiếm Tiên', 'vodang', 'Ngọc Nữ Tố Tâm Kiếm'], ['Băng Phách Ngân Châm', 'duongmon', 'Băng Phách Ngân Châm', { proj: 'dart' }], ['Thần Điêu Hiệp', 'thienvuong', 'Ảm Nhiên Tiêu Hồn Chưởng'], ['Tiểu Long Nữ', 'duongmon', null, { proj: 'petal', dt: 'magic' }]],
    ult: { name: 'Ngọc Phong Vạn Châm', type: 'fan', n: 24, sp: 0.07, mult: 1.3, cd: 5, bee: 1, big: 1, title: 'Cổ Mộ Tiên Tử' } });
  sect({ k: 'nhatnguyet', name: 'Nhật Nguyệt Thần Giáo', ch: '月', col: '#ad1457', col2: '#1a0010', pw: 1.05, wp: 'saber', fem: [4], motto: 'Ma giáo Hắc Mộc Nhai · Hấp Tinh Đại Pháp hút máu địch',
    look: LK('#e0b090', '#0a0005', 'hood', '#ffd54f'), fxc: '#ff4081',
    u: [['Ma Giáo Giáo Đồ', 'thienvuong', 'Hắc Mộc Đao'], ['Hắc Mộc Hộ Vệ', 'thieulam', 'Hắc Mộc Trấn'], ['Thần Giáo Trưởng Lão', 'summonM', 'Hiệu Triệu Giáo Đồ'], ['Tam Thi Não Thần Đan Sứ', 'ngudoc', 'Tam Thi Độc'],
        ['Thánh Cô', 'summonR', 'Triệu Thần Giáo Binh', { weapon: 'fan' }], ['Quỳ Hoa Sát Thủ', 'duongmon', 'Quỳ Hoa Châm', { proj: 'dart' }], ['Hướng Hữu Sứ', 'caibang', 'Phá Thiên Chưởng', { weapon: 'saber' }], ['Nhậm Ngã Hành', 'thienvuong']],
    ult: { name: 'Hấp Tinh Đại Pháp', type: 'drain', r: 3.2, mult: 2.6, heal: 0.6, cd: 6, big: 1, title: 'Nhật Nguyệt Giáo Chủ' } });
  sect({ k: 'toanchan', name: 'Toàn Chân', ch: '全', col: '#5c6bc0', col2: '#1a237e', pw: 1.08, wp: 'sword', fem: [5], motto: 'Đạo môn Chung Nam · Thiên Cương Bắc Đẩu trận, triệu hồi đạo sĩ',
    look: LK('#efc8a2', '#1a1a1a', 'taoist', '#ffffff'), fxc: '#8c9eff',
    u: [['Toàn Chân Đạo Đồng', 'thienvuong', 'Toàn Chân Kiếm Pháp'], ['Bắc Đẩu Thủ Vệ', 'thieulam', 'Bắc Đẩu Trấn'], ['Thiên Cương Trận Chủ', 'summonR', 'Thiên Cương Bắc Đẩu Trận', { proj: 'sword' }], ['Đồng Tử Công Đạo Sĩ', 'conlon', 'Đồng Tử Công'],
        ['Thất Tử Đạo Trưởng', 'summonM', 'Thất Tử Hiệu Triệu'], ['Ngọc Thanh Đạo Cô', 'ngamy', 'Ngọc Thanh Đan'], ['Kim Nhạn Kiếm Khách', 'vodang', 'Kim Nhạn Công'], ['Vương Trùng Dương', 'conlon']],
    ult: { name: 'Tiên Thiên Công', type: 'thunder', r: 2.3, n: 7, mult: 3.0, cd: 7, jade: 1, big: 1, title: 'Trung Thần Thông' } });
  sect({ k: 'bachda', name: 'Bạch Đà Sơn', ch: '駝', col: '#8d6e63', col2: '#1f1410', pw: 0.98, wp: 'stick', fem: [3], motto: 'Tây Độc Âu Dương · Cáp Mô Công chấn địa, rắn độc',
    look: LK('#d7a77c', '#0a0a0a', 'nonla', '#a5d6a7'), fxc: '#aeea00',
    u: [['Bạch Đà Đệ Tử', 'thienvuong', 'Linh Xà Quyền'], ['Xà Trận Hộ Vệ', 'thieulam', 'Xà Trận Trấn'], ['Xà Phu', 'summonR', 'Triệu Xà Đồ', { proj: 'poison', dot: 6 }], ['Độc Xà Nữ', 'ngudoc', 'Xà Độc Vụ'],
        ['Linh Xà Trượng Khách', 'thienvuong', 'Linh Xà Trượng Pháp'], ['Bạch Đà Thiếu Chủ', 'summonM', 'Hiệu Triệu Xà Nô'], ['Âu Dương Trưởng Lão', 'ngudoc', 'Thông Tý Độc'], ['Âu Dương Phong', 'thieulam']],
    ult: { name: 'Cáp Mô Công', type: 'shock', r: 3.6, mult: 3.4, stun: 1.2, cd: 7, toad: 1, big: 1, title: 'Tây Độc' } });
  sect({ k: 'daohoa', name: 'Đào Hoa Đảo', ch: '桃', col: '#ec407a', col2: '#3a0a1e', pw: 1.01, wp: 'fan', fem: [1, 4, 6], motto: 'Đông Tà Hoàng Dược Sư · Lạc Anh Thần Kiếm, Đạn Chỉ Thần Thông',
    look: LK('#f0c8a8', '#0c0808', 'topknot', '#ffd1e3'), fxc: '#ff80ab',
    u: [['Đào Hoa Đồng Tử', 'thienvuong', 'Lạc Anh Chưởng'], ['Á Bộc', 'thieulam', 'Đào Hoa Trận'], ['Ngọc Tiêu Thị Nữ', 'summonR', 'Triệu Đồng Tử', { weapon: 'fan' }], ['Đạn Chỉ Đệ Tử', 'duongmon', 'Đạn Chỉ Thần Thông', { proj: 'dart' }],
        ['Bích Hải Cầm Nữ', 'conlon', 'Bích Hải Triều Sinh Khúc'], ['Lạc Anh Kiếm Khách', 'vodang', 'Lạc Anh Thần Kiếm'], ['Hoàng Dung', 'ngamy', 'Cửu Hoa Ngọc Lộ Hoàn'], ['Hoàng Dược Sư', 'vodang']],
    ult: { name: 'Lạc Anh Thần Kiếm Vũ', type: 'swordrain', r: 3.4, n: 24, mult: 1.05, cd: 7, petal: 1, big: 1, title: 'Đông Tà' } });
  sect({ k: 'modung', name: 'Mộ Dung', ch: '慕', col: '#3949ab', col2: '#0d1240', pw: 1.03, wp: 'sword', fem: [2, 5], motto: 'Cô Tô thế gia · Đấu Chuyển Tinh Di, lấy đạo người trả lại người',
    look: LK('#efc8a2', '#101010', 'topknot', '#c5cae9'), fxc: '#82b1ff',
    u: [['Yến Tử Ổ Gia Nhân', 'thienvuong', 'Cô Tô Quyền'], ['Tứ Đại Gia Tướng', 'thieulam', 'Gia Tướng Trận', { weapon: 'spear' }], ['Vương Cô Nương', 'summonR', 'Triệu Gia Nhân'], ['Bao Bất Đồng', 'thienvuong', 'Phi Cáp Trảm'],
        ['Phong Ba Ác', 'caibang', 'Phong Ba Đao', { weapon: 'saber' }], ['A Châu', 'ngamy', 'Dịch Dung Hồi Phục'], ['Mộ Dung Bác', 'conlon', 'Tham Hợp Chỉ'], ['Mộ Dung Phục', 'vodang']],
    ult: { name: 'Đấu Chuyển Tinh Di', type: 'drain', r: 3.0, mult: 2.8, heal: 0.4, reflect: 1, cd: 6, big: 1, title: 'Cô Tô Mộ Dung' } });
  // ---- NHÂN VẬT CHÍNH: linh vật ra trận, mạnh dần theo đợt, nâng được 5 cấp ----
  var HEROES = {
    bachy: { name: 'Bạch Y Tiên Nữ', arch: 'ngamy', hp: 360, dmg: 15, cd: 1.0, range: 4.2, spd: 2.6, dt: 'magic', proj: 'petal', heal: 38, fxc: '#9fd3ff',
      skill: { name: 'Băng Liên Phổ Độ', type: 'massheal', r: 4.0, amt: 90, cd: 7, dmgmult: 2, big: 1 } },
    honglien: { name: 'Hồng Liên Kiếm Cơ', arch: 'thienvuong', hp: 620, dmg: 21, cd: 0.8, range: 1.0, spd: 3.0, melee: true, dt: 'phys', fxc: '#ff5252',
      skill: { name: 'Hồng Liên Song Kiếm Vũ', type: 'whirl', r: 2.6, mult: 3.0, cd: 5, sword: 1, big: 1 } },
    thanhlong: { name: 'Thanh Long Kiếm Khách', arch: 'vodang', hp: 400, dmg: 24, cd: 1.2, range: 4.4, spd: 2.6, dt: 'magic', proj: 'sword', splash: 1.0, fxc: '#64ffda',
      skill: { name: 'Thanh Long Kiếm Trận', type: 'swordrain', r: 3.0, n: 16, mult: 1.1, cd: 6, wind: 1, big: 1 } },
    kimgiap: { name: 'Kim Giáp Thiên Tướng', arch: 'thieulam', hp: 820, dmg: 18, cd: 1.0, range: 1.1, spd: 2.4, melee: true, dt: 'phys', armor: 0.25, fxc: '#ffd740',
      skill: { name: 'Thiên Tướng Phá Quân', type: 'shock', r: 3.0, mult: 2.8, stun: 1.4, cd: 6, big: 1 } }
  };
  for (var hk in HEROES) { var H = HEROES[hk]; H.cost = 60; H.hero = true; H.sect = 'hero'; H.col = H.fxc; H.col2 = '#2a1a10'; H.ch = '主'; H.role = 'Nhân vật chính · mạnh dần mỗi đợt'; H.up = { name: H.name + ' · Tuyệt Thế' }; H.ult = true; UNITS['hero_' + hk] = H; }
  var UNIT_ORDER = Object.keys(UNITS).filter(function (k) { return !UNITS[k].hero; });

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

  function hpScale(w) { var k = w - 1; return 1 + 0.2 * k + 0.021 * k * k; }
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
    // Vượt Ải (đánh máy): hệ số độ khó nhân máu/sát thương giặc, số đợt theo ải
    G.pve = !!opts.pve; G.hpM = opts.hpM || 1; G.dmM = opts.dmM || 1; G.maxWave = opts.maxWave || MAX_WAVE;
    G.sects = (opts.sects || ['thieulam', 'vodang']).map(function (k, i) { return SECTS[k] ? k : SECT_ORDER[i % SECT_ORDER.length]; });
    for (var i = 0; i < 2; i++) {
      var m = G.mascots[i], P = G.players[i];
      var hu = { id: G.nextId++, owner: i, type: 'hero_' + (HEROES[m] ? m : 'bachy'), tier: 0, cx: 5, cy: 4, x: 5.5, y: 4.5, hero: true, hp: 0, active: true, dead: false, cd: 0, scd: 3, tgt: 0, retarget: 0, fresh: false, spent: 0, face: 1, atkAnim: 0 };
      // linh vật không ra trận (theo yêu cầu) — chỉ đứng ở cổng triệu hồi tướng
      if (m === 'bachy') P.gold += 25; else if (m === 'honglien') P.hp += 8; else if (m === 'thanhlong') P.income += 2; else if (m === 'kimgiap') P.hpMul = 1.1;
    }
    G.units.forEach(function (u) { if (u.hero) { u.hpMul = G.players[u.owner].hpMul || 1; u.hp = stat(u, 'hp'); } });
    return G;
  }
  function mkPlayer() { return { gold: 100, income: 14, hp: 30, value: 0, sendQ: [], ready: false, sentThisWave: 0, kills: 0, leaked: 0 }; }

  var MAX_TIER = 4, TIER_MUL = [1, 2.3, 3.9, 6.1, 9.2], TIER_COST = [1.2, 1.7, 2.4, 3.3];
  // Mua trùng tướng đắt dần (+20%/con) — khuyến khích đội hình đa dạng & nâng cấp thay vì rải 1 loại
  function placeCost(G, p, k) { var n = 0; for (var i = 0; i < G.units.length; i++) { var x = G.units[i]; if (x.owner === p && x.type === k && !x.summon) n++; } return Math.round(UNITS[k].cost * (1 + 0.2 * n)); }
  // Đồng môn hợp sức: càng nhiều loại tướng khác nhau càng mạnh
  var SYN = [[8, 0.3], [6, 0.2], [4, 0.1]];
  function synOf(G, p) { var seen = {}, n = 0; for (var i = 0; i < G.units.length; i++) { var x = G.units[i]; if (x.owner === p && !x.summon && !seen[x.type]) { seen[x.type] = 1; n++; } } for (var j = 0; j < SYN.length; j++) if (n >= SYN[j][0]) return { n: n, b: SYN[j][1] }; return { n: n, b: 0 }; }
  function applySyn(G, p) { var sb = synOf(G, p).b; for (var i = 0; i < G.units.length; i++) if (G.units[i].owner === p) G.units[i].syn = sb; }
  function upCost(u) { return u.tier >= MAX_TIER ? 0 : Math.round(UNITS[u.type].cost * TIER_COST[u.tier]); }
  function popCap(G) { return Math.min(22, 9 + G.wave); }
  function popOf(G, p) { var n = 0; for (var i = 0; i < G.units.length; i++) if (G.units[i].owner === p && !G.units[i].summon && !G.units[i].hero) n++; return n; }
  function stat(u, k) { var d = UNITS[u.type], v = d[k];
    if (u.smul && (k === 'hp' || k === 'dmg')) v = v * u.smul;
    if (u.syn && (k === 'hp' || k === 'dmg' || k === 'heal' || k === 'amt' || k === 'dps')) v = v * (1 + u.syn);
    if (u.hero && u.lv && (k === 'hp' || k === 'dmg' || k === 'heal' || k === 'amt')) v = v * (1 + 0.06 * u.lv);
    if (k === 'amt' && v === undefined) v = d.skill.amt;
    if (u.tier > 0) { if (k === 'hp' || k === 'dmg' || k === 'heal' || k === 'dot' || k === 'amt') v = v * TIER_MUL[u.tier]; else if (k === 'range' && !d.melee) v = v + 0.15 * u.tier; else if (k === 'chain') v = d.chain + (u.tier >= 3 ? 1 : 0); } if (k === 'hp' && u.hpMul) v = Math.round(v * u.hpMul); return v; }

  function cellFree(G, p, cx, cy) {
    for (var i = 0; i < G.units.length; i++) { var u = G.units[i]; if (u.owner === p && !u.summon && u.cx === cx && u.cy === cy) return false; }
    return true;
  }

  // ---- LỆNH (command) — đường duy nhất để người chơi/AI/đối thủ online thay đổi trạng thái ----
  function apply(G, c) {
    if (G.over) return false;
    var P = G.players[c.p];
    if (c.t === 'place') {
      var d = UNITS[c.u]; if (!d) return false;
      if (d.sect !== G.sects[c.p]) return false;
      if (popOf(G, c.p) >= popCap(G)) return false;
      if (c.cx < 0 || c.cx >= LANE_W || c.cy < BUILD_Y0 || c.cy > BUILD_Y1) return false;
      var pc = placeCost(G, c.p, c.u);
      if (!cellFree(G, c.p, c.cx, c.cy) || P.gold < pc) return false;
      P.gold -= pc; P.value += pc;
      var u = { id: G.nextId++, owner: c.p, type: c.u, tier: 0, cx: c.cx, cy: c.cy, x: c.cx + 0.5, y: c.cy + 0.5,
        hp: Math.round(d.hp * (P.hpMul || 1)), hpMul: P.hpMul || 1, active: G.phase === 'build', dead: false, cd: 0, scd: d.skill.cd * 0.5, tgt: 0, retarget: 0, fresh: G.phase === 'build', spent: pc, face: 1, atkAnim: 0 };
      G.units.push(u); applySyn(G, c.p);
      G.ev.push({ e: 'place', p: c.p, id: u.id });
      return true;
    }
    if (c.t === 'upgrade') {
      var u2 = findUnit(G, c.id); if (!u2 || u2.owner !== c.p || u2.summon || u2.tier >= MAX_TIER) return false;
      if (G.phase !== 'build' && u2.active) return false;
      var uc = upCost(u2); if (P.gold < uc) return false;
      P.gold -= uc; P.value += uc; u2.spent += uc; u2.tier++; u2.hp = stat(u2, 'hp');
      G.ev.push({ e: 'upgrade', p: c.p, id: u2.id });
      return true;
    }
    if (c.t === 'sell') {
      var u3 = findUnit(G, c.id); if (!u3 || u3.owner !== c.p || u3.summon || u3.hero) return false;
      if (G.phase !== 'build' && u3.active) return false;
      var refund = u3.fresh ? u3.spent : Math.floor(u3.spent * 0.6);
      P.gold += refund; P.value -= u3.spent;
      G.units.splice(G.units.indexOf(u3), 1); applySyn(G, c.p);
      G.ev.push({ e: 'sell', p: c.p, x: u3.x, y: u3.y, g: refund });
      return true;
    }
    if (c.t === 'send') { if (G.pve) return false;
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
      var u = G.units[k]; u.mp = 0; u.active = true; if (u.hero) u.lv = G.wave - 1; u.fresh = false; u.dead = false; u.hp = stat(u, 'hp');
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
    var hp = Math.round(d.hp * hm * (d.boss || d.send ? 1 : 0.8) * (G.hpM || 1)); dm *= (G.dmM || 1);
    var c = { id: G.nextId++, lane: lane, type: k, x: 1.2 + G.rng() * (LANE_W - 2.4), y: -0.6 - G.rng() * 0.8, hp: hp, max: hp,
      dmg: d.dmg * dm, cd: G.rng() * 0.5, tgt: 0, stun: 0, poison: 0, poisonT: 0, leaked: false, slow: 0, from: from, face: 1, atkAnim: 0, wob: G.rng() * 6 };
    G.creeps.push(c);
  }

  function endFight(G) {
    G.creeps = []; G.projs = []; G.zones = []; G.strikes = [];
    G.units = G.units.filter(function (u) { return !u.summon; });
    for (var p = 0; p < 2; p++) {
      var P = G.players[p], tr = 0;
      for (var si = 0; si < SAVE.length; si++) if (P.gold >= SAVE[si][0]) tr = si + 1;
      var intr = tr ? Math.min(160, Math.floor(P.gold * SAVE[tr - 1][1])) : 0;
      P.gold += P.income + intr; P.income += 3;
      G.ev.push({ e: 'income', p: p, g: P.income, interest: intr, tier: tr, perfect: G.waveLeaks[p] === 0 });
    }
    for (var k = 0; k < G.units.length; k++) { var u = G.units[k]; u.dead = false; u.hp = stat(u, 'hp'); u.x = u.cx + 0.5; u.y = u.cy + 0.5; u.tgt = 0; }
    G.ev.push({ e: 'waveEnd', w: G.wave, leaks: G.waveLeaks.slice() });
    var a = G.players[0].hp, b = G.players[1].hp;
    if (G.pve ? (a <= 0 || G.wave >= G.maxWave) : (a <= 0 || b <= 0 || G.wave >= MAX_WAVE)) {
      G.over = true; G.phase = 'over';
      G.winner = G.pve ? (a > 0 ? 0 : 1) : a > b ? 0 : b > a ? 1 : -1;
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

  function creepsInLane(G, lane) { var r = []; for (var i = 0; i < G.creeps.length; i++) { var c = G.creeps[i]; if (c.lane === lane && c.hp > 0 && !c.leaked && c.y > -1.6) r.push(c); } return r; }
  function nearestCreep(G, lane, x, y, maxR, exclude) {
    var best = null, bd = maxR * maxR;
    for (var i = 0; i < G.creeps.length; i++) {
      var c = G.creeps[i];
      if (c.lane !== lane || c.hp <= 0 || c.leaked || c.y < -1.6) continue; // đánh được cả giặc vừa ra khỏi trận pháp (tránh kẹt)
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
    var lane = u.owner, col = d.fxc || d.col, big = !!s.big;
    switch (s.type) {
      case 'whirl':
        aoeCreeps(G, lane, u.x, u.y, s.r, dmg * s.mult, 'phys', u.owner, 0, 'whirl');
        G.ev.push({ e: 'skill', k: 'whirl', lane: lane, x: u.x, y: u.y, r: s.r, id: u.id, c: col, big: big, sw: !!s.sword });
        break;
      case 'shock':
        aoeCreeps(G, lane, u.x, u.y, s.r, dmg * s.mult, 'phys', u.owner, s.stun, 'shock');
        G.ev.push({ e: 'skill', k: 'shock', lane: lane, x: u.x, y: u.y, r: s.r, id: u.id, c: col, big: big, toad: !!s.toad });
        break;
      case 'drain':
        var hitN = aoeCreeps(G, lane, u.x, u.y, s.r, dmg * s.mult, 'magic', u.owner, 0.5, 'drain');
        var pool = hitN * dmg * s.mult * s.heal, al = [];
        for (var q = 0; q < G.units.length; q++) { var w = G.units[q]; if (w.owner === u.owner && !w.dead && w.active && dist2(w, u) <= 16) al.push(w); }
        al.forEach(function (w) { var h = Math.round(pool / al.length), h0 = w.hp; w.hp = Math.min(stat(w, 'hp'), w.hp + h); if (w.hp - h0 >= 1) G.ev.push({ e: 'healed', lane: lane, x: w.x, y: w.y, v: w.hp - h0 }); });
        G.ev.push({ e: 'skill', k: 'drain', lane: lane, x: u.x, y: u.y, r: s.r, id: u.id, c: col, big: big, galaxy: !!s.reflect });
        break;
      case 'fan':
        var ang = datan2(tgt.y - u.y, tgt.x - u.x), sp = s.sp || 0.13, vis = s.sword ? 'sword' : s.bee ? 'bee' : null;
        for (var i = 0; i < s.n; i++) {
          var a = ang + (i - (s.n - 1) / 2) * sp;
          G.projs.push({ k: 'fandart', lane: lane, side: 0, x: u.x, y: u.y, vx: dcos(a) * 11, vy: dsin(a) * 11, life: (stat(u, 'range') + (big ? 4 : 1.5)) / 11, dmg: dmg * s.mult, dt: s.sword ? 'magic' : 'phys', owner: u.owner, hit: [], col: col, vis: vis, pierce: big });
        }
        G.ev.push({ e: 'skill', k: 'fan', lane: lane, x: u.x, y: u.y, id: u.id, c: col, big: big });
        break;
      case 'cloud':
        G.zones.push({ lane: lane, x: tgt.x, y: tgt.y, r: s.r, dps: TIER_MUL[u.tier] * s.dps, t: s.dur, dur: s.dur, owner: u.owner, col: s.fire ? '#ff6d00' : null });
        G.projs.push({ k: 'poisonbomb', lane: lane, side: 0, x: u.x, y: u.y, sx: u.x, sy: u.y, tx: tgt.x, ty: tgt.y, t: 0, dur: 0.5, owner: u.owner, col: s.fire ? '#ff6d00' : null });
        G.ev.push({ e: 'skill', k: 'cloud', lane: lane, x: tgt.x, y: tgt.y, id: u.id, c: col, big: big, fire: !!s.fire, r: s.r });
        break;
      case 'massheal':
        var amt = stat(u, 'amt') || s.amt;
        for (var j = 0; j < G.units.length; j++) {
          var a2 = G.units[j];
          if (a2.owner !== u.owner || a2.dead || !a2.active) continue;
          if (dist2(a2, u) <= s.r * s.r) { var h0 = a2.hp; a2.hp = Math.min(stat(a2, 'hp'), a2.hp + amt); if (a2.hp - h0 >= 1) G.ev.push({ e: 'healed', lane: lane, x: a2.x, y: a2.y, v: a2.hp - h0 }); }
        }
        if (s.dmgmult) { var lt = tgt && tgt.lane !== undefined ? tgt : nearestCreep(G, lane, u.x, u.y, 8) || u; aoeCreeps(G, lane, lt.x, lt.y, s.r * 0.8, amt * 0.5, 'magic', u.owner, 0.8, 'lotus'); G.ev.push({ e: 'skill', k: 'lotus', lane: lane, x: lt.x, y: lt.y, r: s.r * 0.8, id: u.id, c: col, big: true }); }
        G.ev.push({ e: 'skill', k: 'massheal', lane: lane, x: u.x, y: u.y, r: s.r, id: u.id, c: col, big: big });
        break;
      case 'swordrain':
        var scol = s.wind ? '#e0f7fa' : s.petal ? '#ff80ab' : col, sty = s.wind ? 'wind' : s.petal ? 'petal' : s.slow ? 'ice' : d.sect === 'tinhtuc' ? 'star' : '';
        for (var m = 0; m < s.n; m++) {
          var rr = Math.sqrt(G.rng()) * s.r, aa = G.rng() * 6.283;
          G.strikes.push({ lane: lane, x: tgt.x + dcos(aa) * rr, y: tgt.y + dsin(aa) * rr, t: 0.25 + m * (big ? 0.045 : 0.07), r: 0.75, dmg: dmg * s.mult, dt: 'magic', owner: u.owner, fx: 'sword', col: scol, sty: sty, big: big, stun: s.slow ? 0.35 : 0 });
        }
        G.ev.push({ e: 'skill', k: 'swordrain', lane: lane, x: tgt.x, y: tgt.y, r: s.r, id: u.id, n: s.n, c: scol, big: big, wind: !!s.wind });
        break;
      case 'thunder':
        var tcol = s.fire ? '#ff6d00' : s.jade ? '#b9f6ca' : col, nb = s.n || 1, used = [];
        for (var b = 0; b < nb; b++) {
          var tc = b === 0 ? tgt : nearestCreep(G, lane, tgt.x + (G.rng() - 0.5) * 5, tgt.y + (G.rng() - 0.5) * 5, 6, used);
          var tx = tc ? tc.x : tgt.x + (G.rng() - 0.5) * 3, ty = tc ? tc.y : tgt.y + (G.rng() - 0.5) * 3; if (tc) used.push(tc.id);
          G.strikes.push({ lane: lane, x: tx, y: ty, t: 0.45 + b * 0.12, r: s.r, dmg: dmg * s.mult, dt: 'magic', owner: u.owner, fx: s.fire ? 'fire' : s.jade ? 'palm' : 'thunder', stun: s.stun || 0.6, col: tcol, big: big });
        }
        G.ev.push({ e: 'skill', k: 'thunder', lane: lane, x: tgt.x, y: tgt.y, r: s.r, id: u.id, c: tcol, big: big, fx: s.fire ? 'fire' : s.jade ? 'palm' : 'thunder' });
        break;
      case 'summon':
        var mine = 0; for (var q2 = 0; q2 < G.units.length; q2++) if (G.units[q2].from === u.id && !G.units[q2].dead) mine++;
        var nmax = s.n * 2 + (u.tier >= 3 ? 1 : 0), sd = UNITS[s.unit];
        for (var z = 0; z < s.n + (u.tier >= 2 ? 1 : 0) && mine < nmax; z++, mine++) {
          var ox = (z - s.n / 2) * 0.55, sx = Math.max(0.4, Math.min(LANE_W - 0.4, u.x + ox)), sy = u.y - 0.7 - (z % 2) * 0.3;
          var su = { id: G.nextId++, owner: u.owner, type: s.unit, tier: u.tier, cx: -1, cy: -1, x: sx, y: sy, smul: s.smul, summon: true, from: u.id, life: s.life,
            hpMul: u.hpMul, active: true, dead: false, cd: 0.3, scd: sd.skill.cd * 0.6, tgt: 0, retarget: 0, fresh: false, spent: 0, face: 1, atkAnim: 0 };
          su.hp = stat(su, 'hp'); G.units.push(su);
        }
        G.ev.push({ e: 'skill', k: 'summon', lane: lane, x: u.x, y: u.y - 0.7, r: 1.2, id: u.id, unit: s.unit, c: col, big: big });
        break;
      case 'dragon':
        var ang2 = datan2(tgt.y - u.y, tgt.x - u.x), nd = s.n || 1, spr = s.spread || 0;
        for (var dd = 0; dd < nd; dd++) {
          var a3 = nd > 1 ? ang2 - spr + 2 * spr * dd / (nd - 1) : ang2;
          G.projs.push({ k: 'dragon', lane: lane, side: 0, x: u.x, y: u.y, sx: u.x, sy: u.y, vx: dcos(a3) * 7, vy: dsin(a3) * 7, life: s.len / 7, dmg: dmg * s.mult, dt: 'phys', w: s.w, owner: u.owner, hit: [], col: col, big: big });
        }
        G.ev.push({ e: 'skill', k: 'dragon', lane: lane, x: u.x, y: u.y, id: u.id, a: ang2, c: col, big: big, n: nd });
        break;
    }
  }

  function unitAttack(G, u, c) {
    var d = UNITS[u.type], dmg = stat(u, 'dmg'), lane = u.owner;
    u.atkAnim = 0.25; u.face = c.x >= u.x ? 1 : -1; if (d.skill.type === 'summon') u.mp = (u.mp || 0) + 6;
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
      if (u.summon) { u.life -= DT; if (u.life <= 0) { u.dead = true; u.gone = true; G.ev.push({ e: 'unsummon', p: u.owner, x: u.x, y: u.y }); continue; } }
      if (d.skill.type === 'summon') { u.mp = Math.min(100, (u.mp || 0) + 10 * DT); u.scd = 99;
        if (u.mp >= 100 && nearestCreep(G, lane, u.x, u.y, 9)) { u.mp = 0; castSkill(G, u, null); u.atkAnim = 0.5; } }
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
        if (u.summon) { u.moving = false; u.tgt = 0; continue; }
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
        var tx = Math.max(1, Math.min(LANE_W - 1, c.x + dsin(c.wob + G.time * 0.7) * 0.4));
        c.x += (tx - c.x) * 0.02;
        c.y += spd * DT; c.moving = true; c.face = 1;
        if (c.y >= LEAK_Y) { c.leaked = true; G.ev.push({ e: 'leak', lane: c.lane, x: c.x, y: c.y }); }
      }
    }
  }

  function separate(G) {
    // đẩy nhẹ cho không chồng lên nhau
    var all = [];
    for (var i = 0; i < G.units.length; i++) { var u = G.units[i]; if (u.active && !u.dead) all.push(u); }
    for (var j = 0; j < G.creeps.length; j++) { var c = G.creeps[j]; if (c.hp > 0 && !c.leaked && c.y > -1.6) all.push(c); }
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
      if (A.y < -1.5) A.y = -1.5; // không bị đẩy lùi vào trận pháp (tránh kẹt không đánh được)
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
            if (p.k === 'fandart' && !p.pierce) { p.life = 0; break; }
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
        if (p.ally) { if (tgt) { var hh0 = tgt.hp; tgt.hp = Math.min(stat(tgt, 'hp'), tgt.hp + p.heal); if (tgt.hp - hh0 >= 1) G.ev.push({ e: 'healed', lane: p.lane, x: tgt.x, y: tgt.y, v: tgt.hp - hh0 }); } continue; }
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
        G.ev.push({ e: 'strike', lane: S.lane, x: S.x, y: S.y, r: S.r, fx: S.fx, c: S.col, big: S.big, sty: S.sty });
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
    stepUnits(G); if (G.units.some(function (u) { return u.gone || (u.summon && u.dead); })) G.units = G.units.filter(function (u) { return !(u.gone || (u.summon && u.dead)); });
    stepCreeps(G); stepProjs(G); separate(G);
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
    if (since < (diff === 'easy' ? 4 : 2) && !G.players[1 - p].ready) return; // người chơi đã sẵn sàng thì bot xây nhanh rồi sẵn sàng luôn
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
    var SU = SECTS[G.sects[p]].units, guard = 0, cap = popCap(G);
    function role(k) { var d = UNITS[k]; return d.melee ? 'f' : (d.heal || d.dot) ? 's' : 'b'; }
    while (guard++ < 40) {
      var front = 0, back = 0, sup = 0;
      mine = G.units.filter(function (u) { return u.owner === p && !u.summon; });
      mine.forEach(function (u) { var r = role(u.type); if (r === 'f') front += u.spent; else if (r === 's') sup += u.spent; else back += u.spent; });
      var avail = P.gold - reserve, full = mine.length >= cap;
      var upCand = mine.filter(function (u) { return u.tier < MAX_TIER && upCost(u) <= avail; });
      if (upCand.length && (full || mine.length >= 6 && rng() < 0.55 || rng() < 0.2)) {
        upCand.sort(function (a, b) { return UNITS[b.type].cost - UNITS[a.type].cost || a.tier - b.tier; });
        if (apply(G, { t: 'upgrade', p: p, id: upCand[0].id })) continue;
      }
      if (full) break;
      var tot = front + back + sup + 1, want = front / tot < 0.42 ? 'f' : (sup / tot < 0.14 && G.wave >= 3) ? 's' : 'b';
      var opts = SU.filter(function (k) { return placeCost(G, p, k) <= avail; });
      if (!opts.length) break;
      // bot giỏi: để dành mua tướng đắt khi đã có đội hình cơ bản
      if (mine.length >= 5 && diff !== 'easy' && G.wave >= 4) { var best = opts[opts.length - 1]; if (UNITS[best].cost < UNITS[SU[Math.min(7, 3 + (G.wave >> 2))]].cost) break; }
      var byRole = opts.filter(function (k) { return role(k) === want; }); if (!byRole.length) byRole = opts;
      var pick = byRole[byRole.length - 1 - (rng() < 0.3 && byRole.length > 1 ? 1 : 0)];
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

  // khôi phục trận đã lưu (JSON) — gắn lại hàm ngẫu nhiên có seed
  function revive(G) { G.rng = function () { G.rs = G.rs + 0x6D2B79F5 | 0; var t = Math.imul(G.rs ^ G.rs >>> 15, 1 | G.rs); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; G.ev = []; return G; }
  function checksum(G) {
    var h = G.tick * 31 + G.rs;
    G.units.forEach(function (u) { h = (h * 31 + Math.round(u.x * 100) * 7 + Math.round(u.y * 100) * 13 + Math.round(u.hp)) | 0; });
    G.creeps.forEach(function (c) { h = (h * 31 + Math.round(c.x * 100) * 7 + Math.round(c.y * 100) * 13 + Math.round(c.hp)) | 0; });
    G.players.forEach(function (P) { h = (h * 31 + P.gold * 3 + P.hp * 5 + P.income) | 0; });
    return h;
  }
  var api = { SAVE: SAVE, PATH: PATH, DT: DT, LANE_W: LANE_W, BUILD_Y0: BUILD_Y0, BUILD_Y1: BUILD_Y1, LEAK_Y: LEAK_Y, GATE_Y: GATE_Y, MAX_WAVE: MAX_WAVE,
    UNITS: UNITS, UNIT_ORDER: UNIT_ORDER, SECTS: SECTS, SECT_ORDER: SECT_ORDER, popCap: popCap, popOf: popOf, CREEPS: CREEPS, SENDS: SENDS, SEND_ORDER: SEND_ORDER, WAVE_PATTERNS: WAVE_PATTERNS,
    revive: revive, placeCost: placeCost, synOf: synOf, upCost: upCost, MAX_TIER: MAX_TIER, checksum: checksum, dsin: dsin, datan2: datan2, create: create, apply: apply, step: step, aiThink: aiThink, stat: stat, findUnit: findUnit, findCreep: findCreep, hpScale: hpScale };
  if (typeof module !== 'undefined') module.exports = api;
  return api;
})();
