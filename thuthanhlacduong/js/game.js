// ===== ĐIỀU KHIỂN TRÒ CHƠI, GIAO DIỆN, BOT CHAT =====
{
  const S = Sim, $ = (id) => document.getElementById(id);
  let ME = 0, OP = 1, NET = null;
  let G = null, running = false, acc = 0, speed = 1, slow = 1, slowT = 0, view = { lane: 0 }, diff = 'normal', myMascot = 'honglien', opMascot = 'bachy';
  let PNAME = ''; try { PNAME = localStorage.getItem('ttld_name') || ''; } catch (e) {}
  let selCard = null, selUnitId = null, hoverCell = null;
  const ICON = {};
  try { const m = localStorage.getItem('ttld_mascot'); if (m && R.MASCOTS[m]) myMascot = m; const d = localStorage.getItem('ttld_diff'); if (d) diff = d; } catch (e) {}

  // ---------- khởi tạo đồ hoạ ----------
  V.init($('c3d'), $('ov'));
  window.addEventListener('resize', () => { V.resize(); V.setView(view.lane); });

  // ảnh thẻ: dựng nhân vật 3D rồi chụp
  function makeIcons() {
    const T = THREE, rr = new T.WebGLRenderer({ alpha: true, antialias: true, preserveDrawingBuffer: true });
    const sc = new T.Scene(); sc.add(new T.HemisphereLight('#ffe0c0', '#40283a', 0.9));
    const dl = new T.DirectionalLight('#ffffff', 0.8); dl.position.set(2, 4, 5); sc.add(dl);
    const cam = new T.PerspectiveCamera(30, 1, 0.1, 50);
    function shot(obj, size, h, d, face) {
      rr.setSize(size, size, false); if (face) { cam.position.set(0, h * 0.97, d * 0.36); cam.lookAt(0, h * 0.9, 0); } else { cam.position.set(0.0, h * 0.62, d); cam.lookAt(0, h * 0.5, 0); }
      obj.rotation.y = 0.35; sc.add(obj); rr.render(sc, cam); const url = rr.domElement.toDataURL(); sc.remove(obj); return url;
    }
    const pose = (o) => { if (o.userData.mixer) o.userData.mixer.update(0.4); return o; };
    const um = (k) => { const m = V.UNIT_MODEL[k]; return (V.modelsReady() && V.makeModel(m[0], m[1], 1.55)) || V.makeHuman(R.LOOK[k], { weapon: S.UNITS[k].weapon }); };
    S.UNIT_ORDER.forEach((k) => { ICON[k] = shot(V.makeHuman(R.LOOK[k], { weapon: S.UNITS[k].weapon }), 160, 1.75, 3.8, true); });
    S.SEND_ORDER.forEach((k) => { const m = V.CREEP_MODEL[k]; const o = S.CREEPS[k].beast ? V.makeBeast(k) : V.makeHuman(R.CLOOK[k], { weapon: R.CLOOK[k].weapon }); ICON['s_' + k] = shot(pose(o), 128, 1.3, 3.4); });
    R.MASCOT_ORDER.forEach((k) => { ICON['m_' + k] = A3.portrait('m_' + k, 256, false); ICON['f_' + k] = A3.portrait('m_' + k, 128, true); if (!ICON['m_' + k]) { const o = V.makeMascot(k); o.scale.setScalar(1); ICON['m_' + k] = shot(pose(o), 256, 1.9, 4.2); ICON['f_' + k] = shot(pose(V.makeMascot(k)), 128, 2.4, 4.2, true); } });
    rr.dispose();
  }

  // ---------- thẻ môn phái ----------
  const cardsEl = $('cards');
  function buildCards() { cardsEl.innerHTML = S.UNIT_ORDER.map((k) => `<button class="card" data-u="${k}" aria-label="${S.UNITS[k].name}" style="--c:${S.UNITS[k].col}"><img src="${ICON[k]}" alt=""><span class="nm">${S.UNITS[k].name}</span><span class="cost"><span class="coin"></span>${S.UNITS[k].cost}</span></button>`).join(''); }
  cardsEl.addEventListener('click', (e) => {
    const b = e.target.closest('.card'); if (!b) return; Sfx.init(); Sfx.play('click');
    const k = b.dataset.u; selCard = selCard === k ? null : k; selUnitId = null; hidePanels(); showUnitInfo(k); refreshCards();
    if (!selCard) $('pUnit').hidden = true;
  });
  function refreshCards() {
    const P = G ? G.players[ME] : null;
    cardsEl.querySelectorAll('.card').forEach((c) => { c.classList.toggle('sel', c.dataset.u === selCard); c.classList.toggle('poor', !!P && P.gold < S.UNITS[c.dataset.u].cost); });
  }

  // ---------- bảng thông tin ----------
  function statBlock(d, u) {
    const st = (k) => u ? S.stat(u, k) : d[k];
    const hp = u ? S.stat(u, 'hp') : d.hp;
    return `<div class="stats"><div>Máu<b>${Math.round(u ? u.hp : hp)}${u ? '/' + hp : ''}</b></div><div>Công<b>${d.heal ? st('heal') + '♥' : st('dmg')}</b></div><div>Tốc<b>${d.cd}s</b></div><div>Tầm<b>${st('range')}</b></div></div>`;
  }
  function skillDesc(d) {
    const s = d.skill;
    const m = { whirl: 'Xoay búa chém mọi kẻ địch xung quanh', shock: 'Chưởng vàng làm choáng giặc quanh mình', fan: 'Phóng một quạt ám khí xuyên hàng', cloud: 'Thả mây độc gây sát thương liên tục', massheal: 'Hồi máu lớn cho đồng môn quanh mình', swordrain: 'Gọi mưa kiếm từ trời giáng xuống', thunder: 'Giáng sét khổng lồ, làm choáng', dragon: 'Rồng vàng lao xuyên qua hàng giặc' };
    return `<div class="skill">Tuyệt chiêu: <b>${s.name}</b> — ${m[s.type]} (hồi ${s.cd}s)</div>`;
  }
  function showUnitInfo(k) {
    const d = S.UNITS[k], p = $('pUnit');
    p.innerHTML = `<button class="x" data-x>×</button><h3>${d.name}</h3><div class="sub">${d.role} · ${d.cost} vàng · Chạm ô trên sân của bạn để đặt</div>${statBlock(d)}${skillDesc(d)}`;
    p.hidden = false;
  }
  function showUnit(u) {
    const d = S.UNITS[u.type], p = $('pUnit'), mine = u.owner === ME, P = G.players[ME];
    const canUp = mine && u.tier < S.MAX_TIER && (G.phase === 'build' || !u.active), uc = S.upCost(u), refund = u.fresh ? u.spent : Math.floor(u.spent * 0.6);
    p.innerHTML = `<button class="x" data-x>×</button><h3>${u.tier >= S.MAX_TIER ? d.up.name : d.name} <span style="color:#ffd740">${'★'.repeat(u.tier + 1)}${'☆'.repeat(S.MAX_TIER - u.tier)}</span></h3><div class="sub">Cấp ${u.tier + 1}/5 · ${d.role}${mine ? '' : ' · của đối thủ'}</div>${statBlock(d, u)}${skillDesc(d)}` +
      (mine ? `<div class="row">${u.tier < S.MAX_TIER ? `<button class="big bUp" data-up ${canUp && P.gold >= uc ? '' : 'disabled'}>Lên cấp ${u.tier + 2} · ${uc}</button>` : '<span style="align-self:center;color:#ffd740;font-weight:800">Tối thượng</span>'}<button class="big bSell" data-sell ${G.phase === 'build' || !u.active ? '' : 'disabled'}>Bán +${refund}</button></div>` : '');
    p.hidden = false; p.dataset.id = u.id;
  }
  $('pUnit').addEventListener('click', (e) => {
    if (e.target.closest('[data-x]')) { hidePanels(); selCard = null; selUnitId = null; refreshCards(); return; }
    const id = +$('pUnit').dataset.id;
    if (e.target.closest('[data-up]')) { if (doCmd({ t: 'upgrade', id })) { const u = S.findUnit(G, id); flushEvents(); if (u) showUnit(u); } else Sfx.play('deny'); }
    if (e.target.closest('[data-sell]')) { if (doCmd({ t: 'sell', id })) { flushEvents(); hidePanels(); selUnitId = null; } else Sfx.play('deny'); }
  });
  function hidePanels() { $('pUnit').hidden = true; $('pSend').hidden = true; $('quick').hidden = true; V.setSelected(null); }

  // phái quân
  $('btnSend').addEventListener('click', () => {
    Sfx.init(); Sfx.play('click');
    const p = $('pSend'); if (!p.hidden) { p.hidden = true; return; }
    hidePanels(); selCard = null; refreshCards();
    renderSend(); p.hidden = false;
  });
  function renderSend() {
    const P = G.players[ME];
    $('pSend').innerHTML = `<button class="x" data-x>×</button><h3>Phái quân</h3><div class="sub">Gửi giặc sang đánh đối thủ ở đợt kế tiếp. Mỗi lần gửi tăng thu nhập vĩnh viễn.</div>` +
      S.SEND_ORDER.map((k) => { const s = S.SENDS[k], c = S.CREEPS[k]; return `<button class="sendrow" data-k="${k}" ${P.gold >= s.cost ? '' : 'disabled'}><img src="${ICON['s_' + k]}" alt=""><span><span class="nm">${c.name}</span><br><span class="ds">Lọt thành: −${c.leak} máu địch</span></span><span class="pr">${s.cost} vàng<small>+${s.inc} thu nhập</small></span></button>`; }).join('');
  }
  $('pSend').addEventListener('click', (e) => {
    if (e.target.closest('[data-x]')) { $('pSend').hidden = true; return; }
    const b = e.target.closest('[data-k]'); if (!b) return;
    if (doCmd({ t: 'send', k: b.dataset.k })) { flushEvents(); renderSend(); } else Sfx.play('deny');
  });
  $('btnReady').addEventListener('click', () => { Sfx.init(); if (G && G.phase === 'build') { doCmd({ t: 'ready' }); Sfx.play('click'); toast('Đã sẵn sàng — chờ đối thủ'); } });

  // công cụ
  $('tView').addEventListener('click', () => { view.lane = 1 - view.lane; V.setView(view.lane); $('tView').innerHTML = view.lane === ME ? 'Xem<br>bên kia' : 'Xem<br>ta'; Sfx.play('click'); });
  $('tSpeed').addEventListener('click', () => { speed = speed === 1 ? 2 : speed === 2 ? 3 : 1; $('tSpeed').textContent = 'x' + speed; Sfx.play('click'); });
  $('tSound').addEventListener('click', () => { Sfx.init(); const on = Sfx.toggle(); $('tSound').classList.toggle('off', !on); });
  $('tMusic').addEventListener('click', () => { Sfx.init(); const on = Sfx.toggleMusic(); $('tMusic').classList.toggle('off', !on); });
  $('tSound').classList.toggle('off', !Sfx.isOn()); $('tMusic').classList.toggle('off', !Sfx.isMusic());
  const QUICK = [['hello', 'Chào nha 👋'], ['gg', 'GG'], ['praise', 'Đỉnh quá!'], ['taunt', 'Chờ đấy!'], ['haha', 'Haha 😂'], ['gift', 'Gửi quà nè 🎁']];
  $('quick').innerHTML = QUICK.map((q) => `<button data-q="${q[0]}">${q[1]}</button>`).join('');
  $('tChat').addEventListener('click', () => { const q = $('quick'); const was = q.hidden; hidePanels(); q.hidden = !was; });
  $('quick').addEventListener('click', (e) => { const b = e.target.closest('[data-q]'); if (!b) return; $('quick').hidden = true; chatMsg('Bạn', b.textContent, true); if (NET) NET.send({ t: 'chat', s: b.textContent }); else Bot.reply(b.dataset.q); });

  // ---------- chạm / kéo trên sân ----------
  const cv = $('c3d'), ptrs = new Map(); let drag = null, pinch0 = 0, zoom0 = 1;
  V.cam.zoom = 1;
  cv.addEventListener('pointerdown', (e) => { cv.setPointerCapture(e.pointerId); ptrs.set(e.pointerId, { x: e.clientX, y: e.clientY, x0: e.clientX, y0: e.clientY, t: performance.now() });
    if (ptrs.size === 2) { const [a, b] = [...ptrs.values()]; pinch0 = Math.hypot(a.x - b.x, a.y - b.y); zoom0 = V.cam.zoom; drag = 'pinch'; } else drag = null; Sfx.init(); });
  cv.addEventListener('pointermove', (e) => {
    const p = ptrs.get(e.pointerId);
    if (!p) { if (e.pointerType === 'mouse' && selCard && G) { const h = V.pick(e.clientX, e.clientY); hoverCell = h && h.lane === ME ? h : null; } return; }
    const dx = e.clientX - p.x, dy = e.clientY - p.y; p.x = e.clientX; p.y = e.clientY;
    if (ptrs.size === 2) { const [a, b] = [...ptrs.values()]; const d = Math.hypot(a.x - b.x, a.y - b.y); V.cam.zoom = Math.max(0.55, Math.min(1.6, zoom0 * pinch0 / d)); V.cam.tdist = V.fitDist() * V.cam.zoom; return; }
    if (drag !== 'pan' && Math.hypot(p.x - p.x0, p.y - p.y0) > 9) drag = 'pan';
    if (drag === 'pan') { const k = V.cam.dist / 520; V.cam.tx -= dx * k; V.cam.tz -= dy * k * 1.4; V.cam.x = V.cam.tx; V.cam.z = V.cam.tz; V.cam.tx = Math.max(-10, Math.min(V.LCX[1] + 10, V.cam.tx)); V.cam.tz = Math.max(-8, Math.min(14, V.cam.tz)); }
    if (e.pointerType === 'mouse' && selCard) { const h = V.pick(e.clientX, e.clientY); hoverCell = h && h.lane === ME ? h : null; }
  });
  const up = (e) => { const p = ptrs.get(e.pointerId); ptrs.delete(e.pointerId); if (!p) return; if (!drag && performance.now() - p.t < 600) tap(e.clientX, e.clientY); if (ptrs.size === 0) drag = null; };
  cv.addEventListener('pointerup', up); cv.addEventListener('pointercancel', (e) => { ptrs.delete(e.pointerId); drag = null; });
  cv.addEventListener('wheel', (e) => { V.cam.zoom = Math.max(0.55, Math.min(1.6, V.cam.zoom * (e.deltaY > 0 ? 1.08 : 0.93))); V.cam.tdist = V.fitDist() * V.cam.zoom; }, { passive: true });
  function tap(x, y) {
    if (!G || !running) return;
    const h = V.pick(x, y); if (!h) return;
    $('quick').hidden = true; $('pSend').hidden = true;
    if (selCard && h.lane === ME) {
      if (h.cy < S.BUILD_Y0 || h.cy > S.BUILD_Y1 || h.cx < 0 || h.cx > S.LANE_W - 1) { toast('Chỉ đặt được trong khu xây (ô sáng)'); Sfx.play('deny'); return; }
      const ex = G.units.find((u) => u.owner === ME && u.cx === h.cx && u.cy === h.cy);
      if (ex) { selectUnit(ex); return; }
      if (G.players[ME].gold < S.UNITS[selCard].cost) { toast('Không đủ vàng'); Sfx.play('deny'); return; }
      if (doCmd({ t: 'place', u: selCard, cx: h.cx, cy: h.cy })) { flushEvents(); if (G.phase === 'fight') toast('Đệ tử mới sẽ vào trận từ đợt sau'); }
      return;
    }
    // chọn đệ tử gần điểm chạm
    if (h.lane >= 0) {
      let best = null, bd = 0.85;
      G.units.forEach((u) => { if (u.owner !== h.lane) return; const d = Math.hypot(u.x - h.x, u.y - h.y); if (d < bd) { bd = d; best = u; } });
      if (best) { selectUnit(best); return; }
    }
    selUnitId = null; hidePanels();
  }
  function selectUnit(u) { selUnitId = u.id; selCard = null; refreshCards(); hidePanels(); showUnit(u); Sfx.play('click'); }

  // ---------- thông báo ----------
  function toast(s, warn) { const d = document.createElement('div'); d.textContent = s; if (warn) d.className = 'warn'; $('toast').appendChild(d); setTimeout(() => d.remove(), 2600); while ($('toast').children.length > 3) $('toast').firstChild.remove(); }
  let annT = 0;
  function announce(big, small, red) {
    const a = $('announce'); a.className = red ? 'red' : ''; a.innerHTML = `<span class="t">${big}</span>${small ? `<span class="s">${small}</span>` : ''}`;
    clearTimeout(annT); annT = setTimeout(() => { a.innerHTML = ''; }, 1900);
  }
  function chatMsg(name, text, me, typing) {
    const c = $('chat'), d = document.createElement('div'); d.className = 'msg' + (me ? ' me' : '') + (typing ? ' typing' : '');
    d.innerHTML = `<b>${name}:</b> `; d.appendChild(document.createTextNode(text)); c.appendChild(d);
    while (c.children.length > 4) c.firstChild.remove();
    if (!typing) setTimeout(() => { d.style.transition = 'opacity .6s'; d.style.opacity = '0'; setTimeout(() => d.remove(), 700); }, 7000);
    return d;
  }

  // ---------- BOT CHAT có cảm xúc ----------
  const Bot = (() => {
    const NAMES = ['deoyeuanh2005', 'hoangtucodon9x', 'boyhanoi_97', 'tieuthu_kute', 'xxsatthuxx', 'conan_vn', 'anhbaduoc123', 'meomeo2k3', 'buonvl_9x', 'kiemsi_codon', 'chimse_nho', 'datvietpro', 'langtu_ha', 'tuanbeo98', 'congchua_bongbong', 'quanghai_fan', 'thanhnien_nghiem', 'saobang9x', 'hoaxuong_rong', 'zZbatbaiZz', 'nhoxkute2006', 'vuaphongthu', 'anhtrai_mua', 'pikachu_vn', 'lananh_99', 'sieunhan_do', 'khongten123', 'thichthiquay', 'tuyetnhi_vl', 'kenzie_sg'];
    const L = {
      greet: { k: ['Vào đi, ta chấp ngươi 5 đợt 😏', 'Thành Lạc Dương sắp đổi chủ rồi', 'Lại một kẻ muốn thử sức à'], v: ['Chào bạn nha, chơi vui vẻ! 😄', 'Hello gl hf nhé', 'Trận này căng đây hihi'], c: ['Lại ghép trúng người lạ...', 'gl. nhanh lên', 'Ờ chào'] },
      pLeak: { k: ['Thủng thành rồi kìa haha', 'Phòng thủ như giấy vậy?', 'Ta đếm được mấy con lọt rồi đó 😏'], v: ['Ối, lọt mất mấy con rồi', 'Cố lên bạn ơi!', 'Nguy hiểm quá 😳'], c: ['Hehe đáng đời', 'Thấy chưa', 'Lọt nữa đi 😂'] },
      bLeak: { k: ['Chỉ là sơ suất...', 'Hừ, may cho ngươi', 'Đợt sau ta không để lọt nữa'], v: ['Ui da lọt rồi 😭', 'Mình xây hơi ẩu', 'Toang rồi toang rồi'], c: ['Gì vậy trời!!', 'Lag à??', 'Con này bug à 😤', 'Bực thật sự'] },
      pSend: { k: ['Gửi quân à? Sợ gì', 'Thêm thức ăn cho đệ tử ta', 'Chút quân đó mà đòi phá thành?'], v: ['Ơ gửi quân sang thật à 😳', 'Thôi xong, phải xây thêm', 'Bạn ác quá à'], c: ['Chơi bẩn vậy', 'Ok ok nhớ mặt nhé', 'Gửi nữa đi xem nào 😤'] },
      bSend: { k: ['Quà tặng ngươi đấy 🎁', 'Đỡ được không?', 'Nếm thử Lang Vương của ta'], v: ['Gửi chút quà nha hihi', 'Thử thách xíu nè 😝'], c: ['Nhận lấy!', 'Trả đũa đây'] },
      boss: { k: ['{b} tới. Ta không sợ', 'Để xem ai trụ được {b}'], v: ['{b} kìa 😨', 'Boss tới rồi!!'], c: ['Lại {b}...', 'Ghét con {b} này'] },
      bPerfect: { k: ['Không lọt con nào. Thấy chưa?', 'Dễ như ăn cháo', 'Bức tường thép 😎'], v: ['Yeah giữ được rồi!', 'Phù, sạch sẽ'], c: ['Ít ra lần này ổn'] },
      pPerfect: { k: ['Cũng khá đấy', 'Tạm được'], v: ['Bạn xây khéo ghê', 'Đỉnh thật 👏'], c: ['Hên thôi', 'Xây copy mạng à'] },
      bAhead: { k: ['Đầu hàng sớm cho đỡ mệt', 'GG sớm nhé 😏', 'Ngươi không phải đối thủ của ta'], v: ['Mình đang dẫn nè hihi', 'Cố lên nha bạn'], c: ['Biết điều thì gg đi', 'Dễ quá'] },
      bBehind: { k: ['Đợi đấy, ta mới khởi động', 'Còn sớm lắm', 'Ngươi chỉ gặp may'], v: ['Bạn mạnh quá 😅', 'Cho mình xin bí kíp với', 'Huhu thua mất'], c: ['Cay thật sự', 'Máy lag quá', 'Ghép trận kiểu gì vậy 😤'] },
      pCombo: { k: ['Ăn may thôi', 'Combo nhỏ thôi mà'], v: ['Wow combo đẹp!', 'Ngũ sát luôn 😮'], c: ['Hack à', 'Ủa??'] },
      win: { k: ['Lạc Dương là của ta! GG', 'Về luyện thêm đi 😏'], v: ['GG bạn ơi, trận hay!', 'Thắng sát nút, gg wp'], c: ['GG. Dễ', 'Thấy chưa'] },
      lose: { k: ['...Lần sau ta sẽ phục thù', 'Hừ. GG'], v: ['GG! Bạn chơi hay quá', 'Thua tâm phục khẩu phục 🙇'], c: ['Lag. Không tính', 'GG... ván nữa không?'] },
      r_hello: { k: ['Chào. Chuẩn bị thua đi', 'Hừ'], v: ['Chào bạn 👋', 'Hi hi'], c: ['Ừ', 'Chào'] },
      r_gg: { k: ['Chưa xong đâu', 'GG cái gì, còn đánh'], v: ['GG!', 'gg wp 😄'], c: ['gg', 'Ừ gg'] },
      r_praise: { k: ['Biết là vậy mà 😎', 'Đương nhiên'], v: ['Hehe cảm ơn nha', 'Bạn cũng đỉnh mà'], c: ['Thường thôi', 'Ờ'] },
      r_taunt: { k: ['Ta chờ', 'Sợ quá cơ 😂', 'Nói ít làm nhiều'], v: ['Haha mình run quá', 'Đừng mà 😆'], c: ['Ai sợ ai', 'Lại đây'] },
      r_haha: { k: ['Cười gì', 'Cười sớm thế'], v: ['😂😂', 'Hihi'], c: ['Hài lắm à', '-_-'] },
      r_gift: { k: ['Quà của ngươi yếu quá', 'Cảm ơn, đệ tử ta đang đói'], v: ['Thôi đừng mà 😭', 'Quà gì mà ghê vậy'], c: ['Ok nhớ đấy', 'Gửi nữa đi'] }
    };
    let name = '', per = 'v', busy = false, lastT = -99, mood = 0;
    function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
    function say(cat, force, vars) {
      const now = performance.now() / 1000;
      if (!force && (busy || now - lastT < 6)) return;
      const set = L[cat]; if (!set) return;
      let line = pick(set[per] || set.v); if (vars) Object.keys(vars).forEach((k) => { line = line.replace('{' + k + '}', vars[k]); });
      busy = true; lastT = now;
      const typing = chatMsg(name, 'đang gõ…', false, true);
      setTimeout(() => { typing.remove(); chatMsg(name, line); Sfx.play('msg'); busy = false; }, 700 + line.length * 45 + Math.random() * 600);
    }
    return {
      start() { name = pick(NAMES); per = pick(['k', 'v', 'c']); mood = 0; busy = false; lastT = -99; setTimeout(() => say('greet', true), 2200); return name; },
      get name() { return name; },
      ev(cat, p, vars) { if (Math.random() < p) say(cat, false, vars); },
      force(cat, vars) { say(cat, true, vars); },
      reply(q) { setTimeout(() => say('r_' + q, true), 400); }
    };
  })();

  // ---------- xử lý sự kiện ----------
  let streak = 0, streakT = 0, totalKills = 0;
  const STREAK = { 2: 'Song Sát', 3: 'Tam Sát', 4: 'Tứ Sát', 5: 'Ngũ Sát', 7: 'Huyết Tẩy Giang Hồ', 10: 'Vô Địch Thiên Hạ', 15: 'Thần Cản Sát Thần' };
  function handle(e) {
    V.onEvent(e, G);
    const vis = (lane) => lane === view.lane;
    switch (e.e) {
      case 'kill':
        if (e.lane === ME) {
          totalKills++;
          Sfx.play('kill', e.boss);
          if (e.fb) { announce('Nhất Huyết!', 'Hạ địch đầu tiên của trận'); Sfx.play('jackpot', 4); V.cheer(ME); }
          const now = G.time;
          streak = now - streakT < 1.4 ? streak + 1 : 1; streakT = now;
          if (STREAK[streak]) { announce(STREAK[streak] + '!', streak >= 5 ? 'Chưởng môn hài lòng' : ''); Sfx.play('jackpot', Math.min(14, streak * 2)); V.cheer(ME); if (streak === 5) botEv('pCombo', 0.6); }
          if (e.boss) { slow = 0.35; slowT = 0.9; announce('Hạ ' + S.CREEPS[e.type].name + '!', '+' + e.g + ' vàng'); Sfx.play('gong', true); }
        } else if (vis(OP)) Sfx.play('kill', e.boss);
        if (e.g && e.lane === ME) coinFly(e, Math.min(e.boss ? 18 : 6, 2 + e.g));
        break;
      case 'hit': if (vis(e.lane)) { if (e.k === 'slash') { Sfx.play('slash'); Sfx.play('clang'); } else if (e.k === 'dart' || e.k === 'fandart') Sfx.play('thud'); else if (e.k === 'sword') Sfx.play('sword'); else if (e.k === 'poison') Sfx.play('poison'); else if (e.k === 'dragon') Sfx.play('boom'); else Sfx.play('magic'); } break;
      case 'shoot': if (vis(e.lane)) Sfx.play(e.k === 'dart' ? 'dart' : e.k === 'sword' ? 'sword' : 'magic'); break;
      case 'chain': if (vis(e.lane)) Sfx.play('zap'); break;
      case 'chit': if (vis(e.lane)) Sfx.play(e.boss ? 'boom' : 'thud'); break;
      case 'skill': if (vis(e.lane)) Sfx.play({ whirl: 'whirl', shock: 'boom', fan: 'dart', cloud: 'poison', massheal: 'heal', swordrain: 'swordrain', thunder: 'magic', dragon: 'dragon' }[e.k]); break;
      case 'strike': if (vis(e.lane) && e.fx === 'thunder') Sfx.play('thunder'); else if (vis(e.lane)) Sfx.play('sword'); break;
      case 'gateHit':
        if (e.lane === ME) { Sfx.play('gateHit'); $('vig').style.opacity = 1; setTimeout(() => { $('vig').style.opacity = 0; }, 350); botEv('pLeak', 0.3); }
        else { if (vis(OP)) Sfx.play('gateHit'); botEv('bLeak', 0.4); }
        break;
      case 'leak': if (e.lane === ME) toast('Giặc lọt qua phòng tuyến!', true); break;
      case 'waveStart': {
        Sfx.setFight(true); Sfx.play('gong', e.boss); streak = 0;
        const pat = S.WAVE_PATTERNS[e.w - 1], boss = pat.find((x) => S.CREEPS[x[0]].boss);
        if (boss) { announce(S.CREEPS[boss[0]].name, 'Đợt ' + e.w + ' — trùm xuất hiện!', true); botEv('boss', 0.6, { b: S.CREEPS[boss[0]].name }); }
        else announce('Đợt ' + e.w, pat.map((x) => x[1] + ' ' + S.CREEPS[x[0]].name).join(' · '));
        hidePanels(); selUnitId = null;
        break;
      }
      case 'laneClear':
        if (e.lane === ME && e.perfect) { announce('Hoàn Hảo!', 'Không để lọt tên giặc nào'); Sfx.play('perfect'); V.cheer(ME); botEv('pPerfect', 0.3); }
        if (e.lane === OP && e.perfect) botEv('bPerfect', 0.25);
        break;
      case 'income': if (e.p === ME) { toast('+' + e.g + ' vàng thu nhập'); Sfx.play('coin'); } break;
      case 'waveEnd': {
        Sfx.setFight(false);
        const d = G.players[OP].hp - G.players[ME].hp;
        if (d >= 8) botEv('bAhead', 0.4); else if (d <= -8) botEv('bBehind', 0.45);
        break;
      }
      case 'send':
        if (e.p === OP) { toast('Đối thủ phái ' + S.CREEPS[e.k].name + ' sang thành bạn!', true); botEv('bSend', 0.5); }
        else { toast('Đã phái ' + S.CREEPS[e.k].name + ' — tới đợt sau'); Sfx.play('send'); botEv('pSend', 0.7); }
        break;
      case 'place': if (e.p === ME) Sfx.play('place'); break;
      case 'upgrade': if (e.p === ME) Sfx.play('upgrade'); break;
      case 'sell': if (e.p === ME) Sfx.play('sell'); break;
      case 'unitDie': if (vis(e.p)) Sfx.play('thud'); break;
      case 'over': setTimeout(endGame, 1200); break;
    }
  }
  function botEv(c, p, v) { if (!NET) Bot.ev(c, p, v); }
  function botForce(c, v) { if (!NET) Bot.force(c, v); }
  function doCmd(c) {
    c.p = ME;
    if (NET && NET.role === 'guest') { NET.send({ t: 'cmd', c: c }); Sfx.play('click'); return true; }
    if (NET && NET.role === 'host') { NET.q.push(c); Sfx.play('click'); return true; }
    const ok = S.apply(G, c); if (!ok) Sfx.play('deny'); return ok;
  }
  function flushEvents() { for (const e of G.ev) handle(e); G.ev.length = 0; refreshCards(); updateHUD(true); }

  // ---------- Tiền bay về túi kiểu máy xèng ----------
  let goldShown = 0, coinT = 0;
  function coinFly(e, n) {
    const tgt = $('gold').getBoundingClientRect(), tx = tgt.left + 8, ty = tgt.top + tgt.height / 2;
    setTimeout(() => {
      const sp = V.screenOf(e.lane, e.x, e.y, 0.3);
      for (let i = 0; i < n; i++) {
        const d = document.createElement('div'); d.className = 'flycoin';
        const ox = (Math.random() - 0.5) * 60, oy = (Math.random() - 0.5) * 30;
        d.style.transform = `translate(${sp.x + ox}px,${sp.y + oy}px)`; document.body.appendChild(d);
        setTimeout(() => { d.style.transition = `transform ${0.45 + Math.random() * 0.25}s cubic-bezier(.5,-0.4,.7,1), opacity .2s ${0.5}s`; d.style.transform = `translate(${tx}px,${ty}px) scale(.6)`; }, 20 + i * 45);
        setTimeout(() => { d.remove(); Sfx.play('coin'); const g = $('res'); g.classList.remove('bump'); void g.offsetWidth; g.classList.add('bump'); }, 560 + i * 45);
      }
    }, 450);
  }
  // ---------- HUD ----------
  let hudT = 0;
  function updateHUD(force) {
    if (!G) return; hudT -= 1; if (!force && hudT > 0) return; hudT = 2;
    const P = G.players[ME], O = G.players[OP], maxA = G.maxHp[ME], maxB = G.maxHp[OP];
    $('wave').textContent = 'Đợt ' + G.wave + '/' + S.MAX_WAVE;
    $('phase').innerHTML = G.phase === 'build' ? 'Xây dựng <b>' + Math.max(0, Math.ceil(G.phaseT)) + 's</b>' : G.phase === 'fight' ? 'Giao chiến' : 'Kết thúc';
    goldShown += (P.gold - goldShown) * 0.25; if (Math.abs(P.gold - goldShown) < 0.6) goldShown = P.gold; $('gold').textContent = Math.round(goldShown); { let tr = 0; S.SAVE.forEach((m, i) => { if (P.gold >= m[0]) tr = i + 1; }); const nx = S.SAVE[tr]; $('inc').textContent = '+' + P.income + '/đợt · Tích luỹ ' + tr + '/5' + (tr ? ' (+' + Math.round(S.SAVE[tr - 1][1] * 100) + '%)' : '') + (nx ? ' · mốc sau ' + nx[0] : ''); }
    $('hpMe').style.width = (100 * P.hp / maxA) + '%'; $('hpOp').style.width = (100 * O.hp / maxB) + '%';
    $('hpMeN').textContent = 'Thành ' + P.hp + '/' + maxA + ' · Lực ' + P.value; $('hpOpN').textContent = 'Thành ' + O.hp + '/' + maxB + ' · Lực ' + O.value;
    const rb = $('btnReady'); rb.disabled = G.phase !== 'build' || P.ready; rb.textContent = G.phase === 'build' ? (P.ready ? 'Chờ…' : 'Sẵn sàng') : 'Chiến';
    // thanh boss
    const boss = G.creeps.find((c) => c.lane === view.lane && S.CREEPS[c.type].boss && c.hp > 0);
    if (boss) { $('bossbar').style.display = 'block'; $('bossN').textContent = S.CREEPS[boss.type].name; $('bossB').style.width = (100 * boss.hp / boss.max) + '%'; } else $('bossbar').style.display = 'none';
    refreshCards();
    if (selUnitId && !$('pUnit').hidden) { const u = S.findUnit(G, selUnitId); if (u) { V.setSelected(u); const hp = $('pUnit').querySelector('.stats b'); if (hp) hp.textContent = Math.round(u.hp) + '/' + S.stat(u, 'hp'); } else { hidePanels(); selUnitId = null; } }
    if (!$('pSend').hidden) { $('pSend').querySelectorAll('.sendrow').forEach((b) => { b.disabled = P.gold < S.SENDS[b.dataset.k].cost; }); }
  }

  // ---------- vòng lặp ----------
  let last = performance.now();
  function loop(now) {
    let dt = Math.min(0.05, (now - last) / 1000); last = now;
    if (G && running && !G.over) {
      if (slowT > 0) { slowT -= dt; if (slowT <= 0) slow = 1; }
      acc += dt * (NET ? 1 : speed) * slow; if (NET && NET.role === 'guest' && NET.frames.length > 4) acc += S.DT * Math.min(6, NET.frames.length - 3);
      let n = 0;
      while (acc >= S.DT && n < 8) {
        acc -= S.DT; n++;
        for (const o of G.units) { o.px = o.x; o.py = o.y; }
        for (const o of G.creeps) { o.px = o.x; o.py = o.y; }
        for (const o of G.projs) { o.px = o.x; o.py = o.y; }
        if (NET && NET.role === 'guest') { const f = NET.frames.shift(); if (!f) { acc = 0; break; } f.c.forEach((c) => S.apply(G, c)); }
        else if (NET && NET.role === 'host') { const cs = NET.q.splice(0); cs.forEach((c) => S.apply(G, c)); NET.send({ t: 'f', k: G.tick, c: cs }); if (NET.lost) S.aiThink(G, OP, 'normal'); }
        else S.aiThink(G, OP, diff);
        S.step(G);
        flushEvents();
      }
    } else if (G && G.over) { acc = 0; }
    if (G) {
      V.setGhost(selCard && hoverCell && view.lane === ME ? selCard : null, hoverCell, hoverCell && G.players[ME].gold >= (selCard ? S.UNITS[selCard].cost : 0) && hoverCell.cy >= S.BUILD_Y0 && hoverCell.cy <= S.BUILD_Y1 && !G.units.some((u) => u.owner === ME && u.cx === hoverCell.cx && u.cy === hoverCell.cy));
      V.frame(G, Math.min(1, acc / S.DT), dt, view);
      updateHUD();
    }
    requestAnimationFrame(loop);
  }

  // ---------- bắt đầu / kết thúc ----------
  function newGame() {
    if (NET) { try { NET.close(); } catch (e) {} } NET = null; ME = 0; OP = 1; $('btnSend').hidden = false;
    const others = R.MASCOT_ORDER.filter((k) => k !== myMascot); opMascot = others[Math.floor(Math.random() * others.length)];
    G = S.create({ seed: (Math.random() * 1e9) | 0, mascots: [myMascot, opMascot] });
    G.maxHp = [G.players[0].hp, G.players[1].hp];
    V.initMascots(G.mascots); view.lane = 0; V.cam.orbit = false; V.setView(0, true); $('tView').innerHTML = 'Xem<br>địch';
    $('avaMe').style.backgroundImage = `url(${ICON['f_' + myMascot]})`; $('avaOp').style.backgroundImage = `url(${ICON['f_' + opMascot]})`;
    const bn = Bot.start(); V.setCastleNames(['Thành ' + PNAME, 'Thành ' + bn]);
    $('nmMe').innerHTML = PNAME.replace(/&/g,'&amp;') + ' <small>' + R.MASCOTS[myMascot].name + '</small>';
    $('nmOp').innerHTML = bn + ' <small>' + RANK.title(RANK.botPts) + '</small>';
    $('chat').innerHTML = ''; streak = 0; totalKills = 0; selCard = null; selUnitId = null; hidePanels();
    running = true; acc = 0; flushEvents();
    toast('Chạm thẻ môn phái, rồi chạm ô trên sân để đặt đệ tử');
  }
  function endGame() {
    running = false; const w = G.winner === -1 ? -1 : (G.winner === ME ? 0 : 1), P = G.players[ME];
    const coop = NET && NET.mode === 'coop', okc = coop && G.players[0].hp > 0 && G.players[1].hp > 0; $('endT').textContent = coop ? (okc ? 'Thủ Thành Thành Công' : 'Thất Thủ') : w === 0 ? 'Chiến Thắng' : w === 1 ? 'Thất Thủ' : 'Hoà';
    $('endT').style.color = (coop ? okc : w === 0) ? '#ffdf8a' : '#ff7a6a';
    $('endS').textContent = coop ? (okc ? 'Hai thành cùng trụ vững 20 đợt giặc' : 'Một thành đã thất thủ — cùng luyện thêm rồi phục thù') : w === 0 ? 'Thành Lạc Dương vững như bàn thạch' : w === 1 ? 'Thành đã bị phá — luyện thêm rồi phục thù' : 'Hai bên ngang tài ngang sức';
    $('endStats').innerHTML = `<div>Đợt<b>${G.wave}</b></div><div>Hạ giặc<b>${P.kills}</b></div><div>Máu thành<b>${P.hp}</b></div>`;
    $('end').hidden = false; Sfx.play((coop ? okc : w === 0) ? 'win' : 'lose'); rankResult(coop ? (okc ? 0 : 1) : w); Sfx.setFight(false);
    botForce(w === 1 ? 'win' : 'lose');
  }
  $('btnAgain').addEventListener('click', () => { $('end').hidden = true; newGame(); });
  $('btnMenu').addEventListener('click', () => { $('end').hidden = true; showStart(); });

  // màn hình chọn linh vật
  function showStart() {
    $('start').hidden = false; running = false; document.body.classList.add('menu'); $('pname').value = PNAME; showRank(); document.querySelectorAll('.rk').forEach((x) => x.remove());
    $('mrow').innerHTML = R.MASCOT_ORDER.map((k) => `<button class="mc${k === myMascot ? ' sel' : ''}" data-m="${k}"><img src="${ICON['m_' + k]}" alt=""><div class="nm">${R.MASCOTS[k].name}</div><div class="bn">${R.MASCOTS[k].bonus}</div></button>`).join('');
    document.querySelectorAll('#diff button').forEach((b) => b.classList.toggle('on', b.dataset.d === diff));
    G = S.create({ seed: 1, mascots: [myMascot, R.MASCOT_ORDER.find((k) => k !== myMascot)] }); G.maxHp = [G.players[0].hp, G.players[1].hp];
    V.initMascots(G.mascots); V.cam.orbit = true; V.cam.zoom = 0.85; V.setView(0, true);
  }
  $('mrow').addEventListener('click', (e) => { const b = e.target.closest('[data-m]'); if (!b) return; Sfx.init(); Sfx.play('click'); myMascot = b.dataset.m; try { localStorage.setItem('ttld_mascot', myMascot); } catch (x) {} showStart(); });
  $('diff').addEventListener('click', (e) => { const b = e.target.closest('[data-d]'); if (!b) return; diff = b.dataset.d; try { localStorage.setItem('ttld_diff', diff); } catch (x) {} Sfx.init(); Sfx.play('click'); document.querySelectorAll('#diff button').forEach((x) => x.classList.toggle('on', x.dataset.d === diff)); });
  $('btnPlay').addEventListener('click', () => { if (!nameOk()) return; diff = RANK.pickBot(); playStory(() => { Sfx.init(); Sfx.play('gong', true); $('start').hidden = true; document.body.classList.remove('menu'); V.cam.zoom = 1; newGame(); }); });
  // ---------- XẾP HẠNG: 7 bậc × 10 mốc ----------
  const RANK = (() => {
    const TIERS = [['Đồng', '#c08457'], ['Bạc', '#c9d3dc'], ['Vàng', '#ffd54f'], ['Bạch Kim', '#7fe0d8'], ['Kim Cương', '#82b1ff'], ['Cao Thủ', '#e040fb'], ['Đại Tông Sư', '#ff5252']];
    const HERO = ['Tân Binh', 'Hiệp Khách', 'Thiếu Hiệp', 'Đại Hiệp', 'Chưởng Môn', 'Tông Sư', 'Võ Lâm Minh Chủ'];
    let pts = 0; try { pts = +localStorage.getItem('ttld_rank') || 0; } catch (e) {}
    const per = 100;   // 100 điểm mỗi mốc, 10 mốc mỗi bậc
    const info = (p) => { const t = Math.min(TIERS.length - 1, Math.floor(p / (per * 10))), m = Math.min(10, Math.floor((p - t * per * 10) / per) + 1); return { t, m, name: TIERS[t][0] + ' ' + m, col: TIERS[t][1], hero: HERO[t] }; };
    return {
      get pts() { return pts; }, info, botPts: 0,
      title: (p) => info(p).name,
      pickBot() { this.botPts = Math.max(0, pts + Math.round((Math.random() - 0.4) * 260)); const t = info(this.botPts).t; return t <= 0 ? 'easy' : t <= 2 ? 'normal' : 'hard'; },
      add(d) { pts = Math.max(0, pts + d); try { localStorage.setItem('ttld_rank', pts); } catch (e) {} }
    };
  })();
  function rankResult(w) {
    if (NET && NET.mode === 'coop') return;
    const before = RANK.info(RANK.pts), d = w === 0 ? 35 + Math.round(Math.max(0, RANK.botPts - RANK.pts) / 20) : w === 1 ? -22 : 0;
    RANK.add(d); const after = RANK.info(RANK.pts);
    const up = after.t > before.t ? ' · Thăng bậc: ' + after.hero + '!' : '';
    $('endStats').insertAdjacentHTML('afterend', `<div class="tag rk">Rank: <b style="color:${after.col}">${after.name}</b> (${d >= 0 ? '+' : ''}${d} điểm)${up}</div>`);
    showRank();
  }
  function showRank() { const r = RANK.info(RANK.pts); const el = $('rankBox'); if (el) el.innerHTML = `Rank của bạn: <b style="color:${r.col}">${r.name}</b> · Danh hiệu tướng chính: <b>${r.hero}</b>`; }

  // ---------- CỐT TRUYỆN MỞ ĐẦU ----------
  const STORY = [
    ['p0', 'Hà Nội, 2 giờ sáng. Quán net 24H vắng tanh, chỉ còn tiếng quạt máy và ánh đèn xanh của dàn máy chơi game.'],
    ['p1', 'Trên tường dán tấm băng rôn đỏ rực: "THỦ THÀNH LẠC DƯƠNG — Ai giữ được thành sẽ đổi được vận mệnh". Bạn ngồi xuống, bấm Vào trận…'],
    ['p2', 'Màn hình loé sáng. Một vòng trận pháp tím xoáy kéo bạn vào trong. Tai ù đi, mọi thứ quay cuồng…'],
    ['p3', 'Bạn tỉnh dậy trên tường thành cổ. Khói lửa phía xa — quân Khăn Vàng, phiến quân Biện Kinh và kỵ binh Mông Nguyên đang kéo tới. Các binh sĩ nhìn bạn: "Chưởng môn, xin hạ lệnh!"']
  ];
  let stI = 0, stDone = null, stTyping = null;
  function storyShow() { const [cls, txt] = STORY[stI]; $('stPic').className = cls; const el = $('stTxt'); el.textContent = ''; let k = 0; clearInterval(stTyping); stTyping = setInterval(() => { el.textContent = txt.slice(0, ++k); if (k >= txt.length) clearInterval(stTyping); }, 22); $('stNext').textContent = stI === STORY.length - 1 ? 'Giữ thành!' : 'Tiếp'; }
  function playStory(cb) { let seen = false; try { seen = localStorage.getItem('ttld_story') === '1'; } catch (e) {} if (seen) { cb(); return; } stI = 0; stDone = cb; $('story').hidden = false; storyShow(); }
  function storyEnd() { clearInterval(stTyping); $('story').hidden = true; try { localStorage.setItem('ttld_story', '1'); } catch (e) {} const f = stDone; stDone = null; if (f) f(); }
  $('stNext').addEventListener('click', () => { Sfx.init(); Sfx.play('click'); if (++stI >= STORY.length) storyEnd(); else storyShow(); });
  $('stSkip').addEventListener('click', storyEnd);

  // ---------- ONLINE ----------
  let pend = null;
  function nameOk() { const nm = ($('pname').value || '').trim().replace(/[<>]/g, '').slice(0, 16); if (!nm) { $('pname').focus(); $('pname').placeholder = 'Nhập tên để vào trận'; return false; } PNAME = nm; try { localStorage.setItem('ttld_name', nm); } catch (e) {} return true; }
  function onlUI(busy, msg) { $('onlStatus').textContent = msg || ''; $('btnCancel').hidden = !busy; ['btnCoop', 'btnVs', 'btnRoom', 'btnJoin', 'btnPlay'].forEach((id) => { $(id).disabled = busy; }); }
  function startNet(N, st) {
    pend = null; onlUI(false, '');
    const go = (st2) => {
      NET = N; ME = N.role === 'host' ? 0 : 1; OP = 1 - ME;
      G = S.create({ seed: st2.seed, mascots: st2.mascots }); G.maxHp = [G.players[0].hp, G.players[1].hp];
      const names = st2.names; V.setCastleNames(['Thành ' + names[0], 'Thành ' + names[1]]);
      V.initMascots(G.mascots); view.lane = ME; V.cam.orbit = false; V.cam.zoom = 1; V.setView(ME, true); $('tView').innerHTML = 'Xem<br>bạn';
      $('avaMe').style.backgroundImage = `url(${ICON['f_' + G.mascots[ME]]})`; $('avaOp').style.backgroundImage = `url(${ICON['f_' + G.mascots[OP]]})`;
      $('nmMe').innerHTML = esc(names[ME]) + ' <small>' + (N.mode === 'coop' ? 'Đồng đội' : 'Online') + '</small>';
      $('nmOp').innerHTML = esc(names[OP]) + ' <small>' + (N.mode === 'coop' ? 'Đồng đội · online' : 'Đối thủ · online') + '</small>';
      $('btnSend').hidden = N.mode === 'coop';
      $('start').hidden = true; document.body.classList.remove('menu'); $('chat').innerHTML = '';
      streak = 0; selCard = null; selUnitId = null; hidePanels(); running = true; acc = 0; flushEvents();
      Sfx.init(); Sfx.play('gong', true);
      announce(N.mode === 'coop' ? 'Cùng Thủ Thành' : 'Đấu Online', names[0] + ' · ' + names[1]);
      N.onmsg = (m) => { if (m.t === 'chat') chatMsg(names[OP], m.s); };
      N.onclose = () => { toast((N.mode === 'coop' ? 'Đồng đội' : 'Đối thủ') + ' mất kết nối — máy chơi thay', true); if (N.role === 'guest') { NET = null; } };
    };
    if (N.role === 'guest') { go(st); return; }
    N.onmsg = (m) => { if (m.t !== 'hello') return; const h = m.h || {}; const st2 = { t: 'start', mode: N.mode, seed: (Math.random() * 1e9) | 0, mascots: [myMascot, R.MASCOTS[h.mascot] ? h.mascot : 'bachy'], names: [PNAME, String(h.name || 'Hiệp khách').slice(0, 16)] }; N.send(st2); go(st2); };
  }
  function esc(x) { return String(x).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
  function fallbackBot(mode) { onlUI(false, ''); pend = null; toast('Chưa có người chơi — máy vào thay'); $('start').hidden = true; document.body.classList.remove('menu'); V.cam.zoom = 1; newGame(); if (mode === 'coop') $('btnSend').hidden = true; }
  function quickMatch(mode) {
    if (!nameOk()) return; Sfx.init(); Sfx.play('click');
    if (!NETM.ok()) { onlUI(false, 'Trình duyệt chưa tải được phần online'); return; }
    NETM.me = { name: PNAME, mascot: myMascot }; onlUI(true, 'Đang tìm trận…');
    pend = NETM.quick(mode, (m) => onlUI(true, m), (N, st) => startNet(N, st), (why) => { if (why === 'cancel') { onlUI(false, 'Đã huỷ'); return; } fallbackBot(mode); });
  }
  $('btnCoop').addEventListener('click', () => quickMatch('coop'));
  $('btnVs').addEventListener('click', () => quickMatch('vs'));
  $('btnRoom').addEventListener('click', () => { if (!nameOk()) return; NETM.me = { name: PNAME, mascot: myMascot }; const code = String(1000 + Math.floor(Math.random() * 9000)); onlUI(true, 'Đang tạo phòng…'); pend = NETM.host(code, 'coop', (m) => onlUI(true, m), (N) => startNet(N), (why) => onlUI(false, why)); });
  $('btnJoin').addEventListener('click', () => { if (!nameOk()) return; const code = ($('roomCode').value || '').trim(); if (!/^\d{4}$/.test(code)) { onlUI(false, 'Nhập mã phòng 4 số'); return; } NETM.me = { name: PNAME, mascot: myMascot }; onlUI(true, 'Đang vào phòng…'); pend = NETM.join(code, (m) => onlUI(true, m), (N, st) => startNet(N, st), (why) => onlUI(false, why)); });
  $('btnCancel').addEventListener('click', () => { if (pend) pend.cancel(); pend = null; onlUI(false, 'Đã huỷ'); });
  document.addEventListener('visibilitychange', () => { last = performance.now(); });

  $('mrow').innerHTML = '<div class="tag">Đang tải nhân vật…</div>';
  V.loadModels(() => A3.load(() => { V.spawnNPCs(); makeIcons(); buildCards(); showStart(); requestAnimationFrame(loop); }));
  window.__game = { get G() { return G; }, newGame, tap, setSpeed: (s) => { speed = s; } };
}
