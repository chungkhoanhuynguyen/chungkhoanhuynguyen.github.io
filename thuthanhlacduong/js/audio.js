// ===== ÂM THANH tổng hợp bằng WebAudio (không cần file) =====
var Sfx = (function () {
  var ac = null, master, comp, musicGain, sfxGain, noiseBuf, on = true, musicOn = true, ends = [];
  var last = {}, voices = 0;
  try { var sv = localStorage.getItem('ttld_sound'); if (sv === '0') on = false; var mv = localStorage.getItem('ttld_music'); if (mv === '0') musicOn = false; } catch (e) {}

  function init() {
    if (ac) { if (ac.state === 'suspended') ac.resume(); return; }
    var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return;
    ac = new AC();
    comp = ac.createDynamicsCompressor(); comp.threshold.value = -14; comp.ratio.value = 5; comp.connect(ac.destination);
    master = ac.createGain(); master.gain.value = on ? 0.9 : 0; master.connect(comp);
    sfxGain = ac.createGain(); sfxGain.gain.value = 0.8; sfxGain.connect(master);
    musicGain = ac.createGain(); musicGain.gain.value = musicOn ? 0.32 : 0; musicGain.connect(master);
    var len = ac.sampleRate * 1.5; noiseBuf = ac.createBuffer(1, len, ac.sampleRate);
    var d = noiseBuf.getChannelData(0); for (var i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    startMusic();
  }
  function ok(name, gap) {
    if (!ac || !on) return false;
    if (ac.state === 'suspended') { try { ac.resume(); } catch (e) {} }
    var t = ac.currentTime; if (last[name] && t - last[name] < gap) return false;
    var now = ac.currentTime; while (ends.length && ends[0] < now) ends.shift(); if (ends.length > 40) return false;
    last[name] = t; return true;
  }
  function env(g, t, a, peak, dec) { g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(peak, t + a); g.gain.exponentialRampToValueAtTime(0.0001, t + a + dec); }
  function osc(type, f, t, dur, peak, f2, dest, a) {
    var o = ac.createOscillator(), g = ac.createGain(); o.type = type; o.frequency.setValueAtTime(f, t);
    if (f2) o.frequency.exponentialRampToValueAtTime(f2, t + dur);
    env(g, t, a || 0.005, peak, dur); o.connect(g); g.connect(dest || sfxGain); o.start(t); o.stop(t + dur + 0.05);
    ends.push(t + dur + 0.05); ends.sort(); return o;
  }
  function noise(t, dur, peak, ftype, f, q, dest, f2) {
    var s = ac.createBufferSource(); s.buffer = noiseBuf; s.playbackRate.value = 0.7 + Math.random() * 0.6;
    var fl = ac.createBiquadFilter(); fl.type = ftype || 'bandpass'; fl.frequency.setValueAtTime(f || 1500, t); fl.Q.value = q || 1;
    if (f2) fl.frequency.exponentialRampToValueAtTime(f2, t + dur);
    var g = ac.createGain(); env(g, t, 0.003, peak, dur);
    s.connect(fl); fl.connect(g); g.connect(dest || sfxGain); s.start(t, Math.random()); s.stop(t + dur + 0.05);
    ends.push(t + dur + 0.05); ends.sort();
  }
  var P = {
    slash: function () { if (!ok('slash', 0.05)) return; var t = ac.currentTime; noise(t, 0.09, 0.35, 'highpass', 2500, 0.7); osc('triangle', 900 + Math.random() * 500, t, 0.12, 0.08, 400); },
    clang: function () { if (!ok('clang', 0.07)) return; var t = ac.currentTime, f = 1200 + Math.random() * 600; osc('square', f, t, 0.18, 0.04); osc('sine', f * 2.76, t, 0.25, 0.05); noise(t, 0.04, 0.2, 'highpass', 4000); },
    thud: function () { if (!ok('thud', 0.06)) return; var t = ac.currentTime; osc('sine', 160, t, 0.14, 0.35, 50); noise(t, 0.06, 0.2, 'lowpass', 900); },
    dart: function () { if (!ok('dart', 0.05)) return; var t = ac.currentTime; noise(t, 0.08, 0.18, 'bandpass', 5000, 3, null, 2000); },
    sword: function () { if (!ok('sword', 0.08)) return; var t = ac.currentTime; osc('sine', 2400, t, 0.3, 0.06, 1200); osc('sine', 3600, t, 0.2, 0.04, 2000); noise(t, 0.2, 0.12, 'bandpass', 6000, 4, null, 2500); },
    magic: function () { if (!ok('magic', 0.08)) return; var t = ac.currentTime; osc('sine', 500, t, 0.25, 0.1, 900); osc('triangle', 750, t + 0.03, 0.2, 0.05, 1300); },
    poison: function () { if (!ok('poison', 0.1)) return; var t = ac.currentTime; for (var i = 0; i < 3; i++) osc('sine', 300 + Math.random() * 300, t + i * 0.05, 0.08, 0.07, 700); },
    zap: function () { if (!ok('zap', 0.08)) return; var t = ac.currentTime; noise(t, 0.18, 0.4, 'highpass', 3000, 0.5); osc('sawtooth', 120, t, 0.18, 0.1, 60); },
    thunder: function () { if (!ok('thunder', 0.2)) return; var t = ac.currentTime; noise(t, 0.08, 0.9, 'highpass', 2000); noise(t + 0.02, 1.2, 0.7, 'lowpass', 600, 0.7, null, 80); osc('sine', 70, t, 0.9, 0.6, 30); },
    boom: function () { if (!ok('boom', 0.1)) return; var t = ac.currentTime; osc('sine', 110, t, 0.5, 0.7, 35); noise(t, 0.45, 0.5, 'lowpass', 1500, 0.7, null, 100); },
    whirl: function () { if (!ok('whirl', 0.2)) return; var t = ac.currentTime; noise(t, 0.5, 0.35, 'bandpass', 500, 2, null, 2500); osc('sine', 200, t, 0.45, 0.15, 90); },
    dragon: function () { if (!ok('dragon', 0.3)) return; var t = ac.currentTime; osc('sawtooth', 90, t, 0.8, 0.25, 220); osc('sawtooth', 135, t, 0.8, 0.15, 330); noise(t, 0.9, 0.4, 'bandpass', 400, 1.5, null, 1800); osc('sine', 55, t + 0.1, 0.8, 0.5, 30); },
    heal: function () { if (!ok('heal', 0.25)) return; var t = ac.currentTime; [784, 988, 1175, 1568].forEach(function (f, i) { osc('sine', f, t + i * 0.06, 0.35, 0.06); }); },
    swordrain: function () { if (!ok('swordrain', 0.3)) return; var t = ac.currentTime; for (var i = 0; i < 6; i++) osc('sine', 2000 + i * 300, t + i * 0.06, 0.25, 0.05, 900); },
    kill: function (big) { if (!ok('kill', 0.045)) return; var t = ac.currentTime; osc('sine', big ? 120 : 220, t, big ? 0.5 : 0.18, big ? 0.7 : 0.4, 40); noise(t, 0.12, 0.35, 'bandpass', 1200, 1.2, null, 300); osc('triangle', 500 + Math.random() * 300, t, 0.1, 0.1, 150); },
    coin: function () { if (!ok('coin', 0.04)) return; var t = ac.currentTime, f = 1568 + Math.random() * 400; osc('square', f, t, 0.05, 0.035); osc('square', f * 1.335, t + 0.045, 0.1, 0.035); osc('sine', f * 2.7, t, 0.12, 0.03); },
    place: function () { if (!ok('place', 0.05)) return; var t = ac.currentTime; osc('sine', 300, t, 0.12, 0.3, 120); noise(t, 0.05, 0.2, 'lowpass', 2000); osc('triangle', 880, t + 0.04, 0.12, 0.06); },
    upgrade: function () { if (!ok('upgrade', 0.1)) return; var t = ac.currentTime; [523, 659, 784, 1047, 1319].forEach(function (f, i) { osc('triangle', f, t + i * 0.055, 0.25, 0.09); }); },
    sell: function () { if (!ok('sell', 0.1)) return; var t = ac.currentTime; osc('square', 1500, t, 0.05, 0.05); osc('square', 1100, t + 0.05, 0.08, 0.05); },
    click: function () { if (!ok('click', 0.03)) return; var t = ac.currentTime; osc('triangle', 1200, t, 0.04, 0.08, 800); },
    deny: function () { if (!ok('deny', 0.2)) return; var t = ac.currentTime; osc('square', 180, t, 0.15, 0.08); osc('square', 140, t + 0.12, 0.18, 0.08); },
    send: function () { if (!ok('send', 0.15)) return; var t = ac.currentTime; osc('sawtooth', 220, t, 0.3, 0.12, 440); noise(t, 0.3, 0.2, 'bandpass', 800, 2, null, 3000); },
    gong: function (big) {
      if (!ok('gong', 0.5)) return; var t = ac.currentTime, f = big ? 80 : 110;
      [1, 1.47, 2.09, 2.56, 3.42, 4.1].forEach(function (m, i) { osc('sine', f * m, t, (big ? 3.5 : 2.5) - i * 0.3, 0.22 / (i + 1)); });
      noise(t, 0.3, 0.3, 'lowpass', 800);
      if (big) for (var k = 0; k < 8; k++) osc('sine', 90, t + 0.6 + k * 0.09, 0.15, 0.3 + k * 0.04, 45);
    },
    gateHit: function () { if (!ok('gateHit', 0.25)) return; var t = ac.currentTime; osc('sine', 60, t, 0.6, 0.8, 35); noise(t, 0.3, 0.5, 'lowpass', 700); osc('square', 440, t + 0.05, 0.12, 0.06); osc('square', 330, t + 0.2, 0.15, 0.06); },
    stinger: function (lvl) {
      if (!ac || !on) return; var t = ac.currentTime;
      noise(t, 0.35, 0.3, 'bandpass', 300, 1, null, 5000);
      osc('sine', 55, t + 0.3, 0.9, 0.9, 28);
      noise(t + 0.3, 0.6, 0.6, 'lowpass', 2500, 0.7, null, 120);
      var base = [220, 247, 262, 294, 330][Math.min(4, lvl - 2)] || 220;
      [1, 1.5, 2, 2.5, 3].forEach(function (m, i) { var o = osc('sawtooth', base * m, t + 0.3, 1.1, 0.05); });
      osc('triangle', base * 4, t + 0.3, 0.8, 0.07);
    },
    jackpot: function (n) { if (!ac || !on) return; var t = ac.currentTime; n = n || 6; for (var i = 0; i < n; i++) { var f = 1760 + (i % 4) * 220 + Math.random() * 120, tt = t + i * 0.055; osc('square', f, tt, 0.05, 0.03); osc('square', f * 1.335, tt + 0.03, 0.08, 0.03); osc('sine', f * 2.7, tt, 0.14, 0.025); } },
    perfect: function () { if (!ac || !on) return; var t = ac.currentTime; [659, 784, 988, 1319].forEach(function (f, i) { osc('triangle', f, t + i * 0.09, 0.4, 0.1); }); },
    win: function () { if (!ac) return; var t = ac.currentTime; [392, 440, 523, 587, 659, 784, 1047].forEach(function (f, i) { osc('triangle', f, t + i * 0.13, 0.6, 0.12); osc('sine', f / 2, t + i * 0.13, 0.6, 0.08); }); P.gong(true); },
    lose: function () { if (!ac) return; var t = ac.currentTime; [440, 392, 330, 294, 220].forEach(function (f, i) { osc('triangle', f, t + i * 0.25, 0.8, 0.1); }); },
    msg: function () { if (!ok('msg', 0.3)) return; var t = ac.currentTime; osc('sine', 1046, t, 0.08, 0.06); osc('sine', 1568, t + 0.07, 0.1, 0.05); }
  };

  // ---- Nhạc nền ngũ cung (đàn tranh + trống) ----
  var musicTimer = null, nextNote = 0, step16 = 0, fightMode = false;
  var SCALE = [196, 220, 262, 294, 330, 392, 440, 523, 587, 659, 784];
  var MEL = [5, 7, 8, 7, 5, 4, 2, 4, 5, -1, 4, 2, 1, 2, 4, -1, 5, 8, 9, 8, 7, 5, 4, 5, 7, -1, 5, 4, 2, 1, 0, -1];
  function pluck(f, t, v) {
    var o = ac.createOscillator(), g = ac.createGain(), fl = ac.createBiquadFilter();
    o.type = 'sawtooth'; o.frequency.setValueAtTime(f, t); o.frequency.exponentialRampToValueAtTime(f * 0.995, t + 1);
    fl.type = 'lowpass'; fl.frequency.setValueAtTime(f * 6, t); fl.frequency.exponentialRampToValueAtTime(f * 1.2, t + 0.6);
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(v, t + 0.004); g.gain.exponentialRampToValueAtTime(0.0001, t + 1.4);
    o.connect(fl); fl.connect(g); g.connect(musicGain); o.start(t); o.stop(t + 1.5);
  }
  function drum(t, v, f) {
    var o = ac.createOscillator(), g = ac.createGain(); o.type = 'sine'; o.frequency.setValueAtTime(f || 120, t); o.frequency.exponentialRampToValueAtTime(40, t + 0.3);
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(v, t + 0.005); g.gain.exponentialRampToValueAtTime(0.0001, t + 0.4);
    o.connect(g); g.connect(musicGain); o.start(t); o.stop(t + 0.45);
  }
  function startMusic() {
    nextNote = ac.currentTime + 0.2;
    musicTimer = setInterval(function () {
      if (!ac) return;
      var spb = fightMode ? 0.16 : 0.24;
      while (nextNote < ac.currentTime + 0.4) {
        var i = step16 % MEL.length, n = MEL[i];
        if (n >= 0 && step16 % 2 === 0) pluck(SCALE[n], nextNote, 0.18);
        if (n >= 0 && step16 % 2 === 1 && Math.random() < 0.5) pluck(SCALE[Math.max(0, n - 2)], nextNote, 0.08);
        if (step16 % 8 === 0) pluck(SCALE[0] / 2, nextNote, 0.16);
        if (fightMode) {
          if (step16 % 4 === 0) drum(nextNote, 0.5, 110);
          if (step16 % 8 === 6) drum(nextNote, 0.35, 160);
          if (step16 % 16 === 14 || step16 % 16 === 15) drum(nextNote, 0.25, 200);
        } else if (step16 % 16 === 0) drum(nextNote, 0.25, 90);
        nextNote += spb; step16++;
      }
    }, 100);
  }

  // ---- Giọng đọc (nếu máy có giọng tiếng Việt) ----
  var viVoice = null;
  function findVoice() {
    try { var vs = speechSynthesis.getVoices(); viVoice = vs.filter(function (v) { return /^vi/i.test(v.lang); })[0] || null; } catch (e) {}
  }
  try { findVoice(); speechSynthesis.onvoiceschanged = findVoice; } catch (e) {}
  function say(text) {
    if (!on || !viVoice) return;
    try { speechSynthesis.cancel(); var u = new SpeechSynthesisUtterance(text); u.voice = viVoice; u.lang = viVoice.lang; u.rate = 1.05; u.pitch = 0.7; u.volume = 1; speechSynthesis.speak(u); } catch (e) {}
  }

  return {
    init: init, play: function (n, a) { if (P[n]) try { P[n](a); } catch (e) {} }, say: say,
    setFight: function (f) { fightMode = f; },
    toggle: function () { on = !on; if (master) master.gain.value = on ? 0.9 : 0; try { localStorage.setItem('ttld_sound', on ? '1' : '0'); } catch (e) {} return on; },
    toggleMusic: function () { musicOn = !musicOn; if (musicGain) musicGain.gain.value = musicOn ? 0.32 : 0; try { localStorage.setItem('ttld_music', musicOn ? '1' : '0'); } catch (e) {} return musicOn; },
    dbg: function () { return { st: ac && ac.state, n: ends.length }; }, isOn: function () { return on; }, isMusic: function () { return musicOn; }
  };
})();
