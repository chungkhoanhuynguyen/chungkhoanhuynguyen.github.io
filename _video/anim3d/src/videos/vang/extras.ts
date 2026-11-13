// "Sự sống" nền cho từng bối cảnh: xe máy có người lái chạy qua (đêm bật đèn pha), người đi bộ / chạy bộ, chó, mèo, chim bay.
// Tất cả chạy tự động theo thời gian, đặt ngoài vùng diễn của nhân vật chính để không che mặt.
import * as THREE from "three";
import { motorbike, car, stool, box, cyl, lam, glow, boat, RX, SX, HX, BX, GX, VX, GOLD_X, HOME_X } from "./sets";
import { Actor, crowd } from "./cast2";
import { NOINK } from "../pho/ink";
import { rng } from "../pho/paint";

type Upd = (t: number, cam: THREE.Camera, tint: THREE.Color, jam?: boolean) => void;
const cv = (w: number, h: number) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return [c, c.getContext("2d")!] as const; };

/** animal card (side view) that billboards around Y like the cast */
class Pet {
  root = new THREE.Group(); private g: CanvasRenderingContext2D; private t: THREE.CanvasTexture; private k = ""; card: THREE.Mesh;
  constructor(public kind: "dog" | "cat" | "catsleep", public col: string, size = 0.55) {
    const [c, g] = cv(400, 280); this.g = g; this.t = new THREE.CanvasTexture(c); this.t.colorSpace = THREE.SRGBColorSpace;
    const geo = new THREE.PlaneGeometry(size * 1.43, size); geo.translate(0, size / 2, 0);
    const m = new THREE.MeshBasicMaterial({ map: this.t, alphaTest: 0.4, side: THREE.DoubleSide });
    m.onBeforeCompile = (sh) => { sh.vertexShader = sh.vertexShader.replace("#include <project_vertex>", "#include <project_vertex>\n{ vec4 q = projectionMatrix * ( mvPosition + vec4( 0.0, 0.0, 0.25, 0.0 ) ); gl_Position.z = q.z / q.w * gl_Position.w; }"); };
    m.customProgramCacheKey = () => "petBias";
    this.card = new THREE.Mesh(geo, m); this.card.layers.set(NOINK); this.root.add(this.card);
  }
  draw(ph: number, dir: number) {
    const key = this.kind + Math.round(ph * 8) + dir; if (key === this.k) return; this.k = key;
    const g = this.g; g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, 400, 280); if (dir < 0) { g.translate(400, 0); g.scale(-1, 1); }
    g.lineJoin = "round"; g.lineCap = "round"; g.strokeStyle = "#241726"; g.lineWidth = 9; g.fillStyle = this.col;
    const legs = (xs: number[], y0: number, y1: number) => { for (let i = 0; i < xs.length; i++) { const a = Math.sin(ph * Math.PI * 2 + (i % 2 ? Math.PI : 0)) * 16; g.beginPath(); g.moveTo(xs[i], y0); g.lineTo(xs[i] + a, y1); g.stroke(); } };
    if (this.kind === "dog") {
      legs([120, 150, 250, 280], 170, 262);
      g.beginPath(); g.ellipse(200, 150, 105, 48, 0, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.ellipse(318, 108, 46, 40, 0, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.ellipse(352, 120, 24, 16, 0, 0, 7); g.fill(); g.stroke();
      g.fillStyle = "#241726"; g.beginPath(); g.arc(372, 116, 7, 0, 7); g.fill(); g.beginPath(); g.arc(326, 98, 6, 0, 7); g.fill();
      g.fillStyle = this.col; g.beginPath(); g.ellipse(296, 82, 16, 30, -0.5, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.moveTo(98, 140); g.quadraticCurveTo(60, 110 + Math.sin(ph * 12) * 14, 56, 80); g.stroke();
    } else if (this.kind === "cat") {
      g.beginPath(); g.ellipse(190, 200, 80, 62, 0, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.arc(240, 120, 48, 0, 7); g.fill(); g.stroke();
      for (const s of [-1, 1]) { g.beginPath(); g.moveTo(240 + s * 20, 82); g.lineTo(240 + s * 40, 50); g.lineTo(240 + s * 46, 96); g.closePath(); g.fill(); g.stroke(); }
      g.fillStyle = "#241726"; g.beginPath(); g.arc(226, 118, 6, 0, 7); g.arc(256, 118, 6, 0, 7); g.fill();
      g.beginPath(); g.moveTo(112, 220); g.quadraticCurveTo(50, 190 + Math.sin(ph * 6) * 20, 70, 130); g.stroke();
    } else {
      g.beginPath(); g.ellipse(200, 210, 120, 52, 0, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.arc(285, 190, 40, 0, 7); g.fill(); g.stroke();
      for (const s of [-1, 1]) { g.beginPath(); g.moveTo(285 + s * 16, 160); g.lineTo(285 + s * 32, 134); g.lineTo(285 + s * 38, 172); g.closePath(); g.fill(); g.stroke(); }
      g.beginPath(); g.moveTo(268, 192); g.lineTo(282, 192); g.moveTo(292, 192); g.lineTo(306, 192); g.stroke();
      g.beginPath(); g.moveTo(84, 220); g.quadraticCurveTo(140, 262, 230, 250); g.stroke();
    }
    this.t.needsUpdate = true;
  }
  face(cam: THREE.Camera, tint: THREE.Color) { (this.card.material as THREE.MeshBasicMaterial).color.copy(tint); const wp = this.root.getWorldPosition(new THREE.Vector3()); this.card.rotation.y = Math.atan2(cam.position.x - wp.x, cam.position.z - wp.z); }
}

function birds(n: number, seed: number) {
  const pos = new Float32Array(n * 4 * 3), geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const m = new THREE.LineSegments(geo, new THREE.LineBasicMaterial({ color: "#2a2430" })); m.layers.set(NOINK); m.frustumCulled = false; const r = rng(seed);
  const B = Array.from({ length: n }, () => ({ x: r() * 80 - 40, y: 10 + r() * 9, z: -25 - r() * 30, v: 3 + r() * 3, p: r() * 6, s: 0.35 + r() * 0.25 }));
  const up = (t: number, c: THREE.Vector3) => { B.forEach((b, i) => { const x = c.x + ((b.x + t * b.v + 60) % 120) - 60, y = b.y + Math.sin(t * 0.7 + b.p) * 0.6, z = c.z + b.z, w = Math.sin(t * 10 + b.p) * 0.35 * b.s;
    pos.set([x - b.s, y + w, z, x, y, z, x, y, z, x + b.s, y + w, z], i * 12); }); geo.attributes.position.needsUpdate = true; };
  return { m, up };
}

/** add ambient life to a set; returns per-frame updater */
export function buildExtras(set: string, root: THREE.Group): Upd {
  const ups: Upd[] = []; const r = rng(set.length * 31 + 7);
  const rider = (i: number) => { const a = new Actor(crowd(i + 40), 1.55, 60 + i); a.root.visible = true; return a; };
  const traffic = (X: number, lanes: [number, number][], n: number, spanA: number, spanB: number, night: boolean) => {
    const BC = ["#c0392b", "#2c3e50", "#f4f4f2", "#2980b9", "#111216", "#8e44ad", "#d35400"], CC = ["#f4f4f2", "#111216", "#8a1c22", "#2c3e50", "#9aa3ab", "#1f4e8a"];
    for (let i = 0; i < n; i++) {
      const [z0, dir] = lanes[i % lanes.length], isCar = i % 3 === 2, z = isCar ? z0 * 1.25 : z0;
      const veh = isCar ? car(CC[i % CC.length], i % 2 ? "suv" : "sedan") : motorbike(BC[i % BC.length], (["sh", "vision", "wave"] as const)[i % 3]);
      const rd = isCar ? null : rider(i); const grp = new THREE.Group(); grp.add(veh); root.add(grp); if (rd) root.add(rd.root);
      if (night) { const beam = new THREE.Mesh(new THREE.ConeGeometry(isCar ? 1.6 : 0.9, isCar ? 6 : 4, 16, 1, true), new THREE.MeshBasicMaterial({ color: new THREE.Color(1.2, 1.1, 0.8), transparent: true, opacity: 0.12, depthWrite: false, side: THREE.DoubleSide }));
        beam.rotation.x = -Math.PI / 2; beam.position.set(0, isCar ? 0.6 : 0.9, isCar ? 5.2 : 2.6); beam.layers.set(NOINK); veh.add(beam); }
      veh.rotation.y = dir > 0 ? Math.PI / 2 : -Math.PI / 2;
      const v = (isCar ? 7 : 6) + r() * 4, off = r() * (spanB - spanA), L = spanB - spanA;
      ups.push((t, cam, tint) => { const s = ((off + t * v) % L + L) % L, x = dir > 0 ? spanA + s : spanB - s; grp.position.set(X + x, 0, z);
        if (rd) { rd.root.position.set(X + x - dir * 0.25, 0.72, z + 0.02); rd.pose({ expr: i % 3 ? "neutral" : "smile", mode: "sit", acc: i % 4 === 0 ? ["nonla"] : [] }, cam, tint); } });
    }
  };
  const walkers = (X: number, z: number, n: number, spanA: number, spanB: number, speed: [number, number], jog = false) => {
    for (let i = 0; i < n; i++) {
      const a = new Actor(crowd(i + 60), 1.5 + (i % 3) * 0.08, 80 + i); root.add(a.root); const dir = i % 2 ? 1 : -1, v = speed[0] + r() * (speed[1] - speed[0]), L = spanB - spanA, off = r() * L;
      ups.push((t, cam, tint) => { const s = ((off + t * v) % L + L) % L, x = dir > 0 ? spanA + s : spanB - s; a.root.position.set(X + x, 0.15, z + (i % 3) * 0.35);
        a.pose({ expr: jog ? "grin" : i % 2 ? "smile" : "neutral", mode: jog ? "march" : "stroll", phase: Math.round(((t * (jog ? 1.8 : 1.1) + i * 0.3) % 1) * 12) / 12 }, cam, tint); });
    }
  };
  const pet = (kind: "dog" | "cat" | "catsleep", col: string, X: number, p: THREE.Vector3, move?: { a: number; b: number; v: number }) => {
    const pt = new Pet(kind, col, kind === "dog" ? 0.6 : 0.42); root.add(pt.root);
    ups.push((t, cam, tint) => { let x = p.x, dir = 1; if (move) { const L = move.b - move.a, s = (t * move.v) % (2 * L); x = s < L ? move.a + s : move.b - (s - L); dir = s < L ? 1 : -1; }
      pt.root.position.set(X + x, p.y, p.z); pt.draw(move ? (t * 2.2) % 1 : (t * 0.2) % 1, dir); pt.face(cam, tint); });
  };
  /** quán vỉa hè: bàn thấp + ghế nhựa + ô dù + khách ngồi ăn uống (quán vắng thì chỉ ghế xếp chồng) */
  const cafe = (X: number, x0: number, z: number, nT: number, open: boolean, sign = 1) => {
    for (let k = 0; k < nT; k++) { const x = x0 + k * 1.9, tb = new THREE.Group();
      const top = box(0.62, 0.04, 0.62, lam(["#cfd6dc", "#2f6fd1", "#e8e2d6"][k % 3])); top.position.y = 0.5; tb.add(top); const lg = cyl(0.04, 0.05, 0.48, lam("#9aa1a8"), 6); lg.position.y = 0.25; tb.add(lg);
      if (open) { for (const [dx, dz] of [[-0.25, 0], [0.22, 0.1]]) { const cup = cyl(0.04, 0.035, 0.1, lam(k % 2 ? "#d4a15a" : "#3b2418"), 8); cup.position.set(dx * 0.6, 0.57, dz * 0.6); tb.add(cup); }
        if (k % 3 === 1) { const bowl = new THREE.Mesh(new THREE.SphereGeometry(0.1, 12, 6, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), lam("#f3f0ea")); bowl.rotation.x = Math.PI; bowl.position.set(0, 0.63, -0.05); tb.add(bowl); }
        if (k % 2 === 0) { const um = new THREE.Mesh(new THREE.ConeGeometry(1.25, 0.5, 10, 1, true), lam(["#d9342b", "#2f7fd0", "#f1b51c"][k % 3])); (um.material as THREE.Material).side = THREE.DoubleSide; um.position.y = 2.3; tb.add(um); const pole = cyl(0.025, 0.025, 2.1, lam("#ddd"), 6); pole.position.y = 1.05; tb.add(pole); } }
      tb.position.set(X + x, 0.15, z); root.add(tb);
      for (const [dx, dz] of open ? [[-0.55, 0.0], [0.55, 0.05], [0, 0.55 * sign]] : [[0.55, 0]]) { const st = stool(["#d93636", "#2f6fd1"][(k + Math.round(dx * 10)) % 2]); st.position.set(X + x + dx, 0.15, z + dz); root.add(st);
        if (!open) { for (let h = 1; h < 4; h++) { const s2 = stool("#d93636"); s2.position.set(X + x + dx, 0.15 + h * 0.12, z + dz); root.add(s2); } } }
      if (open) for (const [j, dx, dz] of [[0, -0.55, 0.0], [1, 0.55, 0.05], [2, 0, 0.55 * sign]] as const) { if ((k + j) % 4 === 3) continue;
        const a = new Actor(crowd(k * 3 + j + 90), 1.5 + ((k + j) % 3) * 0.07, 120 + k * 3 + j); root.add(a.root); const ex = (["smile", "grin", "neutral", "laugh", "smile_closed"] as const)[(k * 3 + j) % 5];
        const cup = (k + j) % 2 === 0;
        ups.push((t, cam, tint) => { a.root.position.set(X + x + dx, 0.48, z + dz - 0.18 * sign); a.pose({ expr: ex, mode: "sit", acc: cup ? ["cup"] : [], blink: Math.floor((t + j) * 30) % 83 < 4, t: cup ? Math.round(t * 6) / 6 : 0 }, cam, tint); }); }
    }
  };
  /** quần chúng "ngứa mắt": anh tập boxing múa đấm trên vỉa hè, anh gym cơ bắp áo ba lỗ */
  const boxer = (X: number, x: number, z: number) => { const a = new Actor({ jacket: "#e23b2e", pants: "#1f2430", boots: "#f4f4f2", hat: "cap", cap: "#111", belt: null, buttons: "#e23b2e", skin: "#d9a77e", build: "stout" }, 1.72, 150); root.add(a.root);
    ups.push((t, cam, tint) => { const k = Math.floor(t * 4) % 2; a.root.position.set(X + x + Math.sin(t * 2) * 0.15, 0.15, z); a.pose({ expr: k ? "stern" : "grin", prop: k ? "type" : "hold2", acc: ["gloves"], tilt: k ? 4 : -4 }, cam, tint); }); };
  const gym = (X: number, z: number, a0: number, b0: number) => { const a = new Actor({ jacket: "#2b2b2b", pants: "#3a4a6a", boots: "#f4f4f2", hat: "hair", hair: "#111", belt: null, buttons: "#2b2b2b", skin: "#c98a5a", build: "stout" }, 1.8, 151); root.add(a.root);
    const L = b0 - a0; ups.push((t, cam, tint) => { const s2 = (t * 1.0) % (2 * L), x = s2 < L ? a0 + s2 : b0 - (s2 - L); a.root.position.set(X + x, 0.15, z); a.pose({ expr: "smug", mode: "stroll", phase: Math.round(((t * 1.0) % 1) * 12) / 12, acc: ["muscle"] }, cam, tint); }); };
  /** tắc đường: xe đứng im, đèn pha, còi (âm thanh làm riêng) – chỉ hiện ở cảnh có jam */
  const jamGroup = (X: number) => { const jg = new THREE.Group(); root.add(jg);
    for (let k = 0; k < 7; k++) { const c = car(["#f4f4f2", "#111216", "#8a1c22", "#2c3e50", "#9aa3ab", "#1f4e8a", "#c0392b"][k], k % 2 ? "suv" : "sedan"); c.position.set(X - 40 + k * 5.2, 0, k % 2 ? -2.2 : 2.0); c.rotation.y = Math.PI / 2 * (k % 2 ? 1 : -1); jg.add(c); }
    for (let k = 0; k < 9; k++) { const b = motorbike(["#c0392b", "#2c3e50", "#f4f4f2"][k % 3], (["sh", "vision", "wave"] as const)[k % 3]); b.position.set(X - 41 + k * 3.7, 0, k % 2 ? -0.6 : 0.6); b.rotation.y = Math.PI / 2; jg.add(b); }
    jg.visible = false; ups.push((_t, _c, _ti, jam) => { jg.visible = !!jam; }); };
  const sky = (n: number) => { const b = birds(n, set.length); root.add(b.m); ups.push((t, cam) => b.up(t, cam.position)); };

  if (set === "street" || set === "streetday") {
    const night = set === "street";
    traffic(SX, [[-1.8, 1], [1.8, -1]], night ? 4 : 9, -55, 60, night);
    walkers(SX, -5.4, night ? 2 : 5, -50, 55, [0.9, 1.4]);
    if (!night) walkers(SX, -4.9, 1, -50, 55, [2.4, 2.8], true);
    pet("dog", night ? "#8a6a4a" : "#c98a4a", SX, new THREE.Vector3(0, 0.15, -5.0), { a: -14, b: 26, v: 1.6 });
    pet("cat", "#e8a050", SX, new THREE.Vector3(-4.5, 0.15, 6.5));
    // quán xá: bờ bên kia đường (z âm) và vài cụm bên này, tránh chỗ diễn của nhân vật chính
    cafe(SX, -40, -5.6, 6, !night, -1); cafe(SX, 8, -5.6, 7, !night, -1); cafe(SX, 34, -5.6, 5, !night, -1);
    if (!night) { cafe(SX, HOME_X - 9.5, 5.95, 3, true); cafe(SX, GOLD_X + 16, 5.95, 5, true); boxer(SX, -26, -5.0); gym(SX, -4.6, -30, 20); boxer(SX, GOLD_X + 30, 5.4); }
    else jamGroup(SX);
    if (!night) sky(9);
  } else if (set === "lake") {
    walkers(GX, 10.1, 3, -45, 25, [2.2, 2.8], true);
    walkers(GX, 10.6, 2, -45, 25, [0.8, 1.1]);
    pet("dog", "#d8c8b0", GX, new THREE.Vector3(0, 0.12, 10.4), { a: -30, b: 4, v: 1.3 });
  } else if (set === "bt") {
    traffic(BX, [[4, 1], [7, 1], [12, -1], [15, -1]], 15, -70, 70, false);
    walkers(BX, -2.5, 6, -40, 40, [0.8, 1.3]);
    cafe(BX, -30, -6.5, 6, true); cafe(BX, 24, -6.5, 5, true); boxer(BX, -12, -3.2); gym(BX, -2.0, -30, 30);
    sky(10);
  } else if (set === "hue") {
    sky(12);
    const boat = new THREE.Group(); const hull = new THREE.Mesh(new THREE.CapsuleGeometry(0.5, 3, 4, 8), new THREE.MeshLambertMaterial({ color: "#5a3b22" })); hull.rotation.x = Math.PI / 2; hull.scale.set(1, 1, 0.4); boat.add(hull); root.add(boat);
    ups.push((t) => { boat.position.set(HX - 24 + Math.sin(t * 0.05) * 3, -1.0, -20 + t * 0.6); });
  } else if (set === "villa") {
    for (let i = 0; i < 4; i++) { const b = boat(["#9aa0a8", "#c0392b", "#2f6fd1", "#d8d3c8"][i]); const rw = new Actor(crowd(i + 140), 1.6, 170 + i); root.add(b, rw.root); const v = 0.9 + r() * 0.5, off = r() * 80, z = (i % 2 ? -2.2 : 2.4);
      ups.push((t, cam, tint) => { const x = -40 + ((off + t * v) % 80); b.position.set(VX + x, 0.3 + Math.sin(t * 1.3 + i) * 0.04, z); b.rotation.y = Math.PI / 2 + Math.sin(t * 0.7 + i) * 0.05;
        rw.root.position.set(VX + x, 0.38, z); rw.pose({ expr: i % 2 ? "smug" : "neutral", mode: "sit", acc: i % 2 ? ["raincoat"] : ["umbrella"], umb: "#2b4f8a" }, cam, tint); }); }
    pet("dog", "#c98a4a", VX, new THREE.Vector3(6, 3.45, 7.4));
  } else if (set === "room") {
    pet("catsleep", "#e8a050", RX, new THREE.Vector3(2.75, 0.58, 1.55));
  }
  return (t, cam, tint, jam) => { for (const u of ups) u(t, cam, tint, jam); };
}
