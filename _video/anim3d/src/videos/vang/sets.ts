// Các bối cảnh 3D của video "Vàng đỉnh": gác livestream, phố Trần Nhân Tông đêm mưa, tiệm vàng, cầu Trường Tiền (Huế),
// chợ Bến Thành (Sài Gòn), Hồ Gươm – cầu Thê Húc – Tháp Rùa. Mỗi bối cảnh đặt cách xa nhau trên trục x, bật/tắt theo cảnh.
import * as THREE from "three";
import { facade, sign, tiles, asphalt, WALLS, rng } from "../pho/paint";
import { twoTone } from "../pho/shade";
import { NOINK } from "../pho/ink";

export const lam = (c: THREE.ColorRepresentation, map?: THREE.Texture | null) => twoTone(new THREE.MeshLambertMaterial({ color: c, map: map ?? null }));
export const glow = (r: number, g: number, b: number) => { const m = new THREE.MeshBasicMaterial({ color: new THREE.Color(r, g, b) }); m.toneMapped = true; return m; };
export const box = (w: number, h: number, d: number, m: THREE.Material | THREE.Material[], cast = true) => { const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); b.castShadow = cast; b.receiveShadow = true; return b; };
export const cyl = (r1: number, r2: number, h: number, m: THREE.Material, s = 16) => { const b = new THREE.Mesh(new THREE.CylinderGeometry(r1, r2, h, s), m); b.castShadow = b.receiveShadow = true; return b; };
const cvs = (w: number, h: number) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return [c, c.getContext("2d")!] as const; };
const ctex = (c: HTMLCanvasElement, rep = false) => { const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; if (rep) t.wrapS = t.wrapT = THREE.RepeatWrapping; return t; };
const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";

export const RX = -400, SX = 0, IX = 400, HX = 800, BX = 1300, GX = 1800;

// ---------- shared pieces ----------
export type BikeK = "wave" | "sh" | "vision";
/** xe máy 3 dáng: xe số (wave), tay ga lớn (sh: sàn phẳng, bánh lớn, yếm cao), tay ga nhỏ (vision) */
export function motorbike(col: string, kind: BikeK = "wave") {
  const g = new THREE.Group(), blk = lam("#1d1d22"), body = lam(col), chrome = lam("#c9cdd3"), seat = lam("#2a2324"), dark = lam("#3a3d44");
  const wr = kind === "sh" ? 0.3 : kind === "vision" ? 0.24 : 0.27, wz = kind === "sh" ? 0.68 : 0.62;
  for (const z of [-wz, wz]) { const w = new THREE.Mesh(new THREE.TorusGeometry(wr, 0.07, 8, 22), blk); w.rotation.y = Math.PI / 2; w.position.set(0, wr + 0.06, z); w.castShadow = true; g.add(w);
    const hub = cyl(wr * 0.55, wr * 0.55, 0.05, chrome, 12); hub.rotation.z = Math.PI / 2; hub.position.copy(w.position); g.add(hub); }
  if (kind === "wave") {
    const tank = box(0.22, 0.2, 0.55, body); tank.position.set(0, 0.62, 0.1); tank.rotation.x = 0.25; g.add(tank);
    const rear = box(0.3, 0.3, 0.7, body); rear.position.set(0, 0.62, -0.38); g.add(rear);
    const st = box(0.28, 0.1, 0.72, seat); st.position.set(0, 0.82, -0.3); g.add(st);
    const eng = box(0.24, 0.24, 0.32, dark); eng.position.set(0, 0.36, 0.0); g.add(eng);
    const fork = box(0.06, 0.62, 0.06, chrome); fork.position.set(0, 0.62, wz - 0.05); fork.rotation.x = -0.3; g.add(fork);
    const ex = cyl(0.04, 0.05, 0.75, chrome, 8); ex.rotation.x = Math.PI / 2; ex.position.set(0.17, 0.3, -0.35); g.add(ex);
  } else {
    const H = kind === "sh" ? 1 : 0.85;
    const floor = box(0.36, 0.1, 0.55, dark); floor.position.set(0, 0.32 * H + 0.05, 0.02); g.add(floor);
    const apron = box(0.42, 0.62 * H, 0.14, body); apron.position.set(0, 0.62 * H, wz - 0.22); apron.rotation.x = -0.18; g.add(apron);
    const rear = box(0.4, 0.38 * H, 0.82, body); rear.position.set(0, 0.6 * H, -0.42); g.add(rear);
    const st = box(0.36, 0.12, 0.78, seat); st.position.set(0, 0.86 * H, -0.36); g.add(st);
    const fend = box(0.2, 0.08, 0.4, body); fend.position.set(0, wr * 2 + 0.1, wz); g.add(fend);
    if (kind === "sh") { const rack = box(0.3, 0.04, 0.32, chrome); rack.position.set(0, 0.96, -0.78); g.add(rack); const tail = box(0.3, 0.06, 0.05, glow(2.2, 0.3, 0.3)); tail.position.set(0, 0.74, -0.84); g.add(tail); }
  }
  const hb = box(0.72, 0.05, 0.05, chrome); hb.position.set(0, kind === "sh" ? 1.12 : 1.05, wz - 0.12); g.add(hb);
  for (const sx of [-0.18, 0.18]) { const m = box(0.03, 0.18, 0.03, blk); m.position.set(sx, (kind === "sh" ? 1.22 : 1.15), wz - 0.14); g.add(m); }
  const lamp = box(kind === "wave" ? 0.16 : 0.3, 0.12, 0.08, glow(2.4, 2.2, 1.6)); lamp.position.set(0, kind === "wave" ? 0.98 : 0.95, wz - 0.06); g.add(lamp);
  return g;
}
export type CarK = "sedan" | "suv";
/** ô tô đời mới: thân bo + cabin kính tối + la-zăng + đèn LED */
export function car(col: string, kind: CarK = "sedan") {
  const g = new THREE.Group(), body = twoTone(new THREE.MeshPhongMaterial({ color: col, shininess: 80, specular: "#ffffff" })), glass = lam("#1b2430"), blk = lam("#16171b"), rim = lam("#c9cdd3");
  const L = kind === "suv" ? 4.6 : 4.5, W = 1.85, h0 = kind === "suv" ? 0.85 : 0.68;
  const lower = box(W, h0 - 0.25, L, body); lower.position.set(0, 0.25 + (h0 - 0.25) / 2 + 0.12, 0); g.add(lower);
  const cab = box(W * 0.92, kind === "suv" ? 0.68 : 0.52, L * (kind === "suv" ? 0.62 : 0.5), glass); cab.position.set(0, h0 + 0.12 + (kind === "suv" ? 0.34 : 0.26), kind === "suv" ? -0.25 : -0.15); g.add(cab);
  const roof = box(W * 0.9, 0.06, L * (kind === "suv" ? 0.6 : 0.46), body); roof.position.set(0, cab.position.y + (kind === "suv" ? 0.36 : 0.28), cab.position.z); g.add(roof);
  for (const z of [-L * 0.32, L * 0.32]) for (const x of [-W / 2, W / 2]) { const w = cyl(0.34, 0.34, 0.24, blk, 16); w.rotation.z = Math.PI / 2; w.position.set(x, 0.34, z); g.add(w); const r = cyl(0.2, 0.2, 0.25, rim, 10); r.rotation.z = Math.PI / 2; r.position.set(x, 0.34, z); g.add(r); }
  const hl = box(W * 0.9, 0.06, 0.05, glow(2.6, 2.5, 2.2)); hl.position.set(0, h0 - 0.02, L / 2 + 0.01); g.add(hl);
  const tl = box(W * 0.9, 0.06, 0.05, glow(2.6, 0.25, 0.25)); tl.position.set(0, h0 - 0.02, -L / 2 - 0.01); g.add(tl);
  const gr = box(W * 0.5, 0.16, 0.04, blk); gr.position.set(0, 0.42, L / 2 + 0.01); g.add(gr);
  return g;
}

export function stool(col: string) { const g = new THREE.Group(), m = lam(col); const top = cyl(0.17, 0.17, 0.04, m, 12); top.position.y = 0.42; g.add(top); const leg = cyl(0.15, 0.19, 0.38, m, 4); leg.position.y = 0.2; g.add(leg); return g; }
function tree(r: () => number, h = 4.2, cols = ["#4f9e3f", "#3d8a3a", "#6bb04a"]) {
  const g = new THREE.Group(); const t = cyl(0.18, 0.26, h, lam("#6a4a32"), 8); t.position.y = h / 2; g.add(t);
  for (let k = 0; k < 4; k++) { const c = new THREE.Mesh(new THREE.IcosahedronGeometry(1.3 + r() * 0.6, 1), lam(cols[k % cols.length])); c.position.set((r() - 0.5) * 2, h + 0.3 + r() * 1.3, (r() - 0.5) * 1.6); c.castShadow = true; g.add(c); }
  return g;
}
/** cây nhiều loại: "bang" tán rộng nhiều cành, "sau" thân cao tán tròn, "cau" thân mảnh lá xoè, "bui" bụi thấp */
export function treeV(r: () => number, kind: "bang" | "sau" | "cau" | "bui", night = false) {
  const g = new THREE.Group(), bark = lam(night ? "#3a2a20" : "#6a4a32"), G = night ? ["#1d3a26", "#244630", "#2c5236", "#1a3322"] : ["#3f8f3a", "#4fa042", "#2f7a36", "#6bb04a", "#89b83e"];
  const leaf = (x: number, y: number, z: number, s: number) => { const c = new THREE.Mesh(new THREE.IcosahedronGeometry(s, 1), lam(G[Math.floor(r() * G.length)])); c.position.set(x, y, z); c.scale.y = 0.75 + r() * 0.2; c.castShadow = true; g.add(c); };
  const limb = (x0: number, y0: number, z0: number, x1: number, y1: number, z1: number, rad: number) => { const a = new THREE.Vector3(x0, y0, z0), b = new THREE.Vector3(x1, y1, z1), L = a.distanceTo(b);
    const m = cyl(rad * 0.7, rad, L, bark, 7); m.position.copy(a).add(b).multiplyScalar(0.5); m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), b.clone().sub(a).normalize()); g.add(m); };
  if (kind === "bang") { const h = 2.6 + r() * 0.6; limb(0, 0, 0, 0, h, 0, 0.26);
    for (let k = 0; k < 5; k++) { const a = (k / 5) * Math.PI * 2 + r(), L = 1.6 + r() * 0.8, ex = Math.cos(a) * L, ez = Math.sin(a) * L * 0.7, ey = h + 0.5 + r() * 0.9;
      limb(0, h - 0.2, 0, ex, ey, ez, 0.11); leaf(ex, ey + 0.35, ez, 0.9 + r() * 0.4); leaf(ex * 0.5, ey + 0.6, ez * 0.5, 0.8 + r() * 0.3); }
    leaf(0, h + 1.5, 0, 1.2); }
  else if (kind === "sau") { const h = 4.2 + r() * 1.2; limb(0, 0, 0, 0.2, h, 0, 0.22);
    for (let k = 0; k < 3; k++) { const a = r() * 6.28, ex = Math.cos(a) * 0.9, ez = Math.sin(a) * 0.6; limb(0.15, h - 0.8, 0, ex, h + 0.4, ez, 0.08); }
    for (let k = 0; k < 7; k++) leaf((r() - 0.5) * 2.2, h + 0.4 + r() * 1.4, (r() - 0.5) * 1.6, 0.75 + r() * 0.35); }
  else if (kind === "cau") { const h = 5 + r() * 2, lean = (r() - 0.5) * 0.5; limb(0, 0, 0, lean, h, 0, 0.13);
    const fm = lam(night ? "#1f3a24" : "#4c9a3a"); fm.side = THREE.DoubleSide;
    for (let k = 0; k < 8; k++) { const f = new THREE.Mesh(new THREE.ConeGeometry(0.35, 2.6, 4, 1, true), fm); const a = (k / 8) * Math.PI * 2;
      f.position.set(lean + Math.cos(a) * 1.0, h - 0.25, Math.sin(a) * 1.0); f.rotation.set(Math.sin(a) * 1.25, 0, -Math.cos(a) * 1.25); f.scale.set(1, 1, 0.25); f.castShadow = true; g.add(f); } }
  else { for (let k = 0; k < 4; k++) leaf((r() - 0.5) * 0.9, 0.35 + r() * 0.3, (r() - 0.5) * 0.6, 0.38 + r() * 0.15); }
  return g;
}
function willow(r: () => number) {
  const g = new THREE.Group(); const t = cyl(0.2, 0.32, 3.6, lam("#4a3626"), 8); t.position.y = 1.8; t.rotation.z = (r() - 0.5) * 0.3; g.add(t);
  for (let k = 0; k < 7; k++) { const c = new THREE.Mesh(new THREE.ConeGeometry(1.1 + r() * 0.5, 3.6, 7, 1, true), lam(["#2f6e3a", "#3c8048", "#28603a"][k % 3])); c.position.set((r() - 0.5) * 2.4, 3.2 + r() * 0.8, (r() - 0.5) * 2.0); c.castShadow = true; (c.material as THREE.Material).side = THREE.DoubleSide; g.add(c); }
  return g;
}
function lampPost(head = [2.6, 2.0, 1.1] as [number, number, number], h = 4.5) {
  const g = new THREE.Group(); const p = cyl(0.07, 0.1, h, lam("#2a2d33"), 8); p.position.y = h / 2; g.add(p);
  const arm = box(0.9, 0.06, 0.06, lam("#2a2d33")); arm.position.set(0.4, h - 0.05, 0); g.add(arm);
  const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.2, 12, 8), glow(...head)); bulb.position.set(0.8, h - 0.2, 0); bulb.layers.set(NOINK); g.add(bulb);
  const halo = new THREE.Mesh(new THREE.SphereGeometry(0.55, 12, 8), new THREE.MeshBasicMaterial({ color: new THREE.Color(head[0] * 0.35, head[1] * 0.3, head[2] * 0.25), transparent: true, opacity: 0.35, depthWrite: false }));
  halo.position.copy(bulb.position); halo.layers.set(NOINK); g.add(halo);
  return g;
}
/** night facade: same tube house but windows lit warm */
function nightFacade(w: number, floors: number, wall: string, shop: string | null, seed: number, gold: boolean) {
  const t = facade(w, floors, wall, shop, seed); const c = t.image as HTMLCanvasElement, g = c.getContext("2d")!;
  // darken and light up some windows
  g.fillStyle = "rgba(10,14,40,0.45)"; g.fillRect(0, 0, c.width, c.height);
  const r = rng(seed + 3), PX = 96, fh = 3.4, H = c.height;
  for (let f = 1; f < floors; f++) if (r() < 0.75) { const dw = Math.min(1.6, w * 0.42), dx = (w - dw) / 2; g.fillStyle = r() < 0.5 ? "rgba(255,205,120,.9)" : "rgba(255,236,190,.85)"; g.fillRect((dx + 0.08) * PX, H - (f * fh + 2.35) * PX, (dw - 0.16) * PX, 2.0 * PX); }
  if (gold) { // bright gold shop interior + red/gold glow
    const ig = g.createLinearGradient(0, H - 2.9 * PX, 0, H); ig.addColorStop(0, "#fff0b8"); ig.addColorStop(1, "#e8a640");
    g.fillStyle = ig; g.fillRect(0.2 * PX, H - 2.9 * PX, (w - 0.4) * PX, 2.9 * PX);
    g.fillStyle = "#b8bec6"; g.fillRect(0.2 * PX, H - 2.9 * PX, (w - 0.4) * PX, 1.3 * PX); // shutter still half down (before opening)
    g.strokeStyle = "#8d949c"; g.lineWidth = 2; for (let k = 0; k < 14; k++) { g.beginPath(); g.moveTo(0.2 * PX, H - 2.9 * PX + k * 9); g.lineTo((w - 0.2) * PX, H - 2.9 * PX + k * 9); g.stroke(); }
    g.fillStyle = "#c8202f"; for (let x = 0.5; x < w - 0.6; x += 0.7) g.fillRect(x * PX, H - 1.2 * PX, 0.5 * PX, 1.2 * PX); // red display cases
    g.fillStyle = "#ffd84a"; for (let x = 0.55; x < w - 0.6; x += 0.7) for (let y = 0; y < 3; y++) g.fillRect((x + 0.05) * PX, H - (1.1 - y * 0.32) * PX, 0.4 * PX, 0.12 * PX);
  }
  t.needsUpdate = true; return t;
}
function goldSign(text: string, seed: number) {
  const [c, g] = cvs(640, 140), r = rng(seed); const bg = ["#b3131f", "#8f0e18", "#c8202f"][Math.floor(r() * 3)];
  g.fillStyle = bg; g.fillRect(0, 0, 640, 140); g.strokeStyle = "#f5c518"; g.lineWidth = 8; g.strokeRect(10, 10, 620, 120);
  g.fillStyle = "#ffd84a"; g.font = `900 ${text.length > 12 ? 58 : 66}px ${F}`; g.textAlign = "center"; g.textBaseline = "middle"; g.fillText(text, 320, 74, 600);
  return ctex(c);
}
function house(x: number, side: 1 | -1, w: number, floors: number, seed: number, shop: string | null, night: boolean, gold = false) {
  const r = rng(seed), g = new THREE.Group(), fh = 3.4, H = floors * fh + 0.6, D = 12, o = -side;
  const wall = WALLS[Math.floor(r() * WALLS.length)];
  const plain = lam(wall), ftex = night ? nightFacade(w, floors, wall, gold ? null : shop, seed, gold) : facade(w, floors, wall, shop, seed);
  const front = night ? new THREE.MeshBasicMaterial({ map: ftex }) : lam("#ffffff", ftex);
  if (night) (front as THREE.MeshBasicMaterial).color.setRGB(gold ? 1.15 : 0.85, gold ? 1.05 : 0.82, gold ? 0.95 : 0.95);
  const mats = [plain, plain, plain, plain, side === -1 ? front : plain, side === 1 ? front : plain];
  const b = new THREE.Mesh(new THREE.BoxGeometry(w, H, D), mats); b.castShadow = b.receiveShadow = true; b.position.set(0, H / 2, side * D / 2); g.add(b);
  const slab = lam("#e8e2d6"), rail = lam("#2b2f33");
  for (let f = 1; f < floors; f++) {
    const s = box(w - 0.2, 0.18, 1.0, slab); s.position.set(0, f * fh, o * 0.5); g.add(s);
    const rl = box(w - 0.3, 0.06, 0.06, rail); rl.position.set(0, f * fh + 1.0, o * 0.97); g.add(rl);
    for (let xx = -w / 2 + 0.25; xx < w / 2 - 0.2; xx += 0.24) { const p = box(0.035, 1.0, 0.035, rail, false); p.position.set(xx, f * fh + 0.5, o * 0.97); g.add(p); }
  }
  if (shop) {
    const sm = gold ? new THREE.MeshBasicMaterial({ map: goldSign(shop, seed) }) : night ? new THREE.MeshBasicMaterial({ map: sign(shop, seed) }) : lam("#fff", sign(shop, seed));
    if (gold) (sm as THREE.MeshBasicMaterial).color.setRGB(1.6, 1.45, 1.3); else if (night) (sm as THREE.MeshBasicMaterial).color.setRGB(0.95, 0.9, 0.9);
    const sg = new THREE.Mesh(new THREE.BoxGeometry(w - 0.3, 0.85, 0.1), [rail, rail, rail, rail, side === -1 ? sm : rail, side === 1 ? sm : rail]);
    sg.position.set(0, 3.3, o * 0.08); g.add(sg);
    const aw = box(w, 0.05, 1.6, lam(gold ? "#b3131f" : ["#d9342b", "#2f7fd0", "#f1b51c", "#2b9a5a"][Math.floor(r() * 4)])); aw.position.set(0, 2.85, o * 0.8); aw.rotation.x = o * 0.22; g.add(aw);
  }
  g.position.set(x, 0, side * 7);
  return g;
}
export function rainStreaks(n = 1600) {
  const pos = new Float32Array(n * 6), base = new Float32Array(n * 3), r = rng(77);
  for (let i = 0; i < n; i++) { base[i * 3] = (r() - 0.5) * 30; base[i * 3 + 1] = r() * 14; base[i * 3 + 2] = (r() - 0.5) * 24; }
  const geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const m = new THREE.LineSegments(geo, new THREE.LineBasicMaterial({ color: "#a9c4ee", transparent: true, opacity: 0.55, depthWrite: false })); m.layers.set(NOINK); m.frustumCulled = false;
  const update = (t: number, c: THREE.Vector3, on: boolean) => {
    m.visible = on; if (!on) return;
    for (let i = 0; i < n; i++) { const y = ((base[i * 3 + 1] - t * 9) % 14 + 14) % 14; const x = c.x + base[i * 3] - 0.06 * y, z = c.z + base[i * 3 + 2];
      pos.set([x, y, z, x + 0.05, y + 0.55, z], i * 6); }
    geo.attributes.position.needsUpdate = true;
  };
  return { m, update };
}
function waterTex(base: string, streak: string, seed: number) {
  const [c, g] = cvs(512, 512), r = rng(seed); g.fillStyle = base; g.fillRect(0, 0, 512, 512);
  for (let i = 0; i < 260; i++) { g.fillStyle = `rgba(255,255,255,${0.03 + r() * 0.06})`; g.fillRect(r() * 512, r() * 512, 20 + r() * 90, 2); }
  g.fillStyle = streak; for (let i = 0; i < 40; i++) g.fillRect(r() * 512, r() * 512, 30 + r() * 60, 3);
  return ctex(c, true);
}

// ---------- ROOM: căn gác tầng năm của anh Đô ----------
export type Screen = { c: HTMLCanvasElement; g: CanvasRenderingContext2D; t: THREE.CanvasTexture };
export function buildRoom() {
  const g = new THREE.Group(); g.position.x = RX; const r = rng(5);
  const [fc, fg] = cvs(256, 256); fg.fillStyle = "#8a5a3c"; fg.fillRect(0, 0, 256, 256); for (let i = 0; i < 8; i++) { fg.fillStyle = i % 2 ? "#7e5236" : "#946243"; fg.fillRect(0, i * 32, 256, 30); }
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(8, 7), lam("#ffffff", ctex(fc, true))); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; ((floor.material as THREE.MeshLambertMaterial).map!).repeat.set(3, 3); g.add(floor);
  const wallM = lam("#3b3560"), wallM2 = lam("#4a4270");
  const back = box(8, 3.6, 0.15, wallM, false); back.position.set(0, 1.8, -2.6); g.add(back);
  const left = box(0.15, 3.6, 7, wallM2, false); left.position.set(-3.6, 1.8, 0.8); g.add(left);
  const right = box(0.15, 3.6, 7, wallM2, false); right.position.set(3.6, 1.8, 0.8); g.add(right);
  const ceil = box(8, 0.1, 7, lam("#2a2546"), false); ceil.position.set(0, 3.6, 0.8); g.add(ceil);
  // LED strips (HDR -> bloom)
  const led1 = box(7.6, 0.05, 0.05, glow(1.9, 0.5, 3.0), false); led1.position.set(0, 3.45, -2.5); led1.layers.set(NOINK); g.add(led1);
  const led2 = box(0.05, 0.05, 6.6, glow(0.4, 1.6, 3.0), false); led2.position.set(-3.5, 3.45, 0.8); led2.layers.set(NOINK); g.add(led2);
  // window with night city
  const [wc, wg] = cvs(512, 320); const sk = wg.createLinearGradient(0, 0, 0, 320); sk.addColorStop(0, "#0b1030"); sk.addColorStop(1, "#2c2f62"); wg.fillStyle = sk; wg.fillRect(0, 0, 512, 320);
  for (let i = 0; i < 18; i++) { const bw = 20 + r() * 40, bh = 60 + r() * 200, bx = r() * 512; wg.fillStyle = "#151937"; wg.fillRect(bx, 320 - bh, bw, bh); wg.fillStyle = "rgba(255,210,130,.85)"; for (let k = 0; k < 10; k++) if (r() < 0.5) wg.fillRect(bx + 3 + r() * (bw - 8), 320 - bh + r() * bh, 4, 5); }
  const win = new THREE.Mesh(new THREE.PlaneGeometry(1.8, 1.2), new THREE.MeshBasicMaterial({ map: ctex(wc) })); win.position.set(-3.5, 2.0, -0.6); win.rotation.y = Math.PI / 2; win.layers.set(NOINK); g.add(win);
  const wf = box(0.08, 1.35, 1.95, lam("#1d1a2e")); wf.position.set(-3.53, 2.0, -0.6); g.add(wf);
  // posters
  for (const [x, txt, col] of [[-2.2, "LỬA CHÙA", "#ff6a2a"], [2.3, "TOP 1", "#3ad0ff"]] as const) {
    const [pc, pg] = cvs(256, 360); const gg = pg.createLinearGradient(0, 0, 0, 360); gg.addColorStop(0, col); gg.addColorStop(1, "#1a1030"); pg.fillStyle = gg; pg.fillRect(0, 0, 256, 360);
    pg.fillStyle = "#fff"; pg.font = `900 46px ${F}`; pg.textAlign = "center"; pg.fillText(txt, 128, 300, 230); pg.fillStyle = "rgba(255,255,255,.25)"; pg.beginPath(); pg.arc(128, 140, 70, 0, 7); pg.fill();
    const ps = new THREE.Mesh(new THREE.PlaneGeometry(0.8, 1.1), lam("#ffffff", ctex(pc))); ps.position.set(x, 2.3, -2.5); g.add(ps);
  }
  // desk + monitors + keyboard + mic
  const desk = box(2.6, 0.08, 0.9, lam("#1c1c24")); desk.position.set(0, 0.78, -1.9); g.add(desk);
  for (const x of [-1.2, 1.2]) { const l = box(0.06, 0.78, 0.8, lam("#15151b")); l.position.set(x, 0.39, -1.9); g.add(l); }
  const mk = (w: number, h: number): Screen => { const [c, gg] = cvs(Math.round(w * 400), Math.round(h * 400)); return { c, g: gg, t: ctex(c) }; };
  const game = mk(1.15, 0.65), chat = mk(0.75, 0.65);
  const mon = (s: Screen, w: number, h: number, x: number, ry: number) => {
    const fr = box(w + 0.06, h + 0.06, 0.05, lam("#0d0d12")); fr.position.set(x, 1.32, -2.2); fr.rotation.y = ry; g.add(fr);
    const sc = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: s.t })); sc.position.set(x + Math.sin(ry) * 0.03, 1.32, -2.17 + Math.cos(ry) * 0.0); sc.rotation.y = ry; sc.layers.set(NOINK); g.add(sc);
    const st = box(0.06, 0.45, 0.06, lam("#0d0d12")); st.position.set(x, 1.0, -2.25); g.add(st);
  };
  mon(game, 1.15, 0.65, -0.35, 0.05); mon(chat, 0.75, 0.65, 0.78, -0.25);
  const kb = box(0.7, 0.03, 0.22, glow(1.4, 0.6, 2.2)); kb.position.set(-0.3, 0.83, -1.7); kb.layers.set(NOINK); g.add(kb);
  const mic = cyl(0.05, 0.05, 0.18, lam("#202028"), 10); mic.position.set(0.35, 1.18, -1.65); mic.rotation.x = 0.4; g.add(mic);
  const arm = box(0.03, 0.03, 0.6, lam("#202028")); arm.position.set(0.5, 1.25, -1.9); arm.rotation.y = 0.4; g.add(arm);
  // case PC kính cường lực: đèn RGB, card đồ hoạ 3 quạt phát sáng, quạt tản nhiệt
  const pc = new THREE.Group(); const caseM = lam("#15151b"); const shell = box(0.26, 0.55, 0.5, caseM); shell.position.y = 0.275; pc.add(shell);
  const [pcC, pcG] = cvs(260, 540); pcG.fillStyle = "#0b0b12"; pcG.fillRect(0, 0, 260, 540); pcG.fillStyle = "#1e2230"; pcG.fillRect(20, 20, 220, 300);
  for (let k = 0; k < 3; k++) { pcG.strokeStyle = ["#ff3cc8", "#3cc8ff", "#8a5cff"][k]; pcG.lineWidth = 8; pcG.beginPath(); pcG.arc(60 + k * 70, 400, 30, 0, 7); pcG.stroke(); pcG.fillStyle = "#222"; pcG.beginPath(); pcG.arc(60 + k * 70, 400, 22, 0, 7); pcG.fill(); }
  pcG.fillStyle = "#2a2e3c"; pcG.fillRect(20, 340, 220, 14); pcG.fillStyle = "#c0c6d4"; pcG.fillRect(30, 60, 70, 70); pcG.strokeStyle = "#3cffb4"; pcG.lineWidth = 6; pcG.strokeRect(14, 14, 232, 512);
  for (let y = 140; y < 320; y += 22) { pcG.fillStyle = y % 44 ? "#ff3cc8" : "#3cc8ff"; pcG.fillRect(140, y, 80, 8); }
  const pm = new THREE.MeshBasicMaterial({ map: ctex(pcC) }); pm.color.setRGB(1.6, 1.6, 1.8);
  const panel = new THREE.Mesh(new THREE.PlaneGeometry(0.24, 0.5), pm); panel.position.set(0, 0.28, 0.252); panel.layers.set(NOINK); pc.add(panel);
  pc.position.set(-1.6, 0, -1.8); pc.rotation.y = 0.35; g.add(pc);
  const lampB = cyl(0.08, 0.1, 0.03, lam("#202028"), 12); lampB.position.set(-1.0, 0.83, -2.05); g.add(lampB);
  const lampA = box(0.02, 0.45, 0.02, lam("#202028")); lampA.position.set(-1.0, 1.05, -2.05); lampA.rotation.z = -0.3; g.add(lampA);
  const lampH = cyl(0.04, 0.09, 0.12, glow(2.8, 2.4, 1.6), 12); lampH.position.set(-0.9, 1.26, -2.0); lampH.rotation.z = 0.8; lampH.layers.set(NOINK); g.add(lampH);
  const led3 = box(2.6, 0.03, 0.03, glow(0.4, 2.6, 2.0), false); led3.position.set(0, 0.76, -1.46); led3.layers.set(NOINK); g.add(led3);
  // gaming chair (back seen from behind when shooting over shoulder)
  const ch = new THREE.Group(); const seat = box(0.6, 0.12, 0.6, lam("#d12e5b")); seat.position.y = 0.5; ch.add(seat); const bk = box(0.56, 0.6, 0.12, lam("#d12e5b")); bk.position.set(0, 0.85, 0.3); ch.add(bk);
  const bks = box(0.36, 0.3, 0.13, lam("#222")); bks.position.set(0, 0.88, 0.31); ch.add(bks); const cb = cyl(0.04, 0.04, 0.4, lam("#222"), 8); cb.position.y = 0.25; ch.add(cb);
  ch.rotation.y = Math.PI; ch.position.set(-0.2, 0, -1.0); g.add(ch);
  // bed + safe + wardrobe
  const bed = box(1.7, 0.45, 2.2, lam("#f0eee8")); bed.position.set(2.5, 0.25, 0.9); g.add(bed);
  const bl = box(1.72, 0.12, 1.4, lam("#5d7fc9")); bl.position.set(2.5, 0.52, 1.3); g.add(bl);
  const pil = box(0.6, 0.12, 0.35, lam("#ffffff")); pil.position.set(2.5, 0.54, 0.05); g.add(pil);
  const safe = box(0.45, 0.32, 0.4, lam("#3c3f47")); safe.position.set(2.2, 0.16, 1.85); g.add(safe);
  const dial = cyl(0.06, 0.06, 0.03, lam("#c9ccd3"), 12); dial.rotation.x = Math.PI / 2; dial.position.set(2.2, 0.18, 2.06); g.add(dial);
  const war = box(1.2, 2.2, 0.55, lam("#b98a5e")); war.position.set(3.2, 1.1, -1.6); war.rotation.y = -Math.PI / 2; g.add(war);
  
  return { g, game, chat, safe, bed };
}

// ---------- STREET: phố Trần Nhân Tông đêm mưa + hàng người xếp hàng ----------
type HL = { x: number; w: number; fl: number; seed: number; name: string | null; gold: boolean };
const LAYOUT = (() => {
  const out: Record<"n" | "s", HL[]> = { n: [], s: [] }, r = rng(11);
  for (const side of ["n", "s"] as const) { let x = -50, i = 0;
    while (x < 60) { const w = 3.6 + r() * 1.6, fl = 3 + Math.floor(r() * 3), nm = r() < 0.5 ? ["TẠP HÓA", "PHỞ BÒ", "CÀ PHÊ", "THUỐC TÂY", "BÁNH MÌ", "ĐỒNG HỒ"][Math.floor(r() * 6)] : null;
      out[side].push({ x: x + w / 2, w, fl, seed: 300 + i * 7 + (side === "n" ? 1 : 0), name: nm, gold: false }); x += w + 0.02; i++; } }
  const near = (L: HL[], x: number) => L.reduce((b, h, i) => (Math.abs(h.x - x) < Math.abs(L[b].x - x) ? i : b), 0);
  const g0 = near(out.n, 0); [["BẢO TÍN MINH ANH", 0], ["BẢO TÍN MẠNH ĐỨC", 1], ["VÀNG BẠC KIM HOÀN", 3]].forEach(([n, k]) => { const h = out.n[g0 + (k as number)]; h.name = n as string; h.gold = true; });
  const sg = near(out.s, 4); out.s[sg].name = "BẢO TÍN MINH ANH"; out.s[sg].gold = true;
  const xc = near(out.n, -22); out.n[xc].name = "XE MÁY CŨ"; out.n[xc].gold = false;
  const tn = near(out.n, -9); out.n[tn].name = null; // nhà anh Tân (cửa sắt)
  return out;
})();
export const GOLD_X = LAYOUT.n.find((h) => h.gold)!.x, XECU_X = LAYOUT.n.find((h) => h.name === "XE MÁY CŨ")!.x, HOME_X = LAYOUT.n.reduce((b, h) => (Math.abs(h.x + 9) < Math.abs(b.x + 9) ? h : b)).x;
export function buildStreet(night = true) {
  const g = new THREE.Group(); g.position.x = SX; const r = rng(11);
  const road = new THREE.Mesh(new THREE.PlaneGeometry(200, 8), night ? new THREE.MeshBasicMaterial({ map: waterTex("#1b2036", "rgba(255,190,90,.35)", 3) }) : lam("#ffffff", asphalt()));
  road.rotation.x = -Math.PI / 2; ((road.material as THREE.MeshBasicMaterial).map!).repeat.set(30, 1.3); road.receiveShadow = true; g.add(road);
  for (const s of [1, -1]) {
    const sw = new THREE.Mesh(new THREE.BoxGeometry(200, 0.15, 3), lam("#ffffff", tiles())); sw.position.set(0, 0.075, s * 5.5); sw.receiveShadow = true; ((sw.material as THREE.MeshLambertMaterial).map!).repeat.set(100, 1.5); g.add(sw);
    const curb = box(200, 0.17, 0.18, lam("#d8d3c8")); curb.position.set(0, 0.085, s * 4.05); g.add(curb);
    for (const h of LAYOUT[s > 0 ? "n" : "s"]) g.add(house(h.x, s as 1 | -1, h.w, h.fl, h.seed, h.name, night, h.gold));
    for (let px = -46; px <= 50; px += 12) { const lp = lampPost(); lp.position.set(px + (s > 0 ? 0 : 6), 0.15, s * 4.4); lp.rotation.y = s > 0 ? -Math.PI / 2 : Math.PI / 2; g.add(lp); }
    for (let tx = -46; tx <= 52; tx += 11) { if (s > 0 && tx > -2 && tx < 32) continue; const k = (["bang", "sau", "bang", "bui"] as const)[Math.floor(r() * 4)]; const t = treeV(r, k, night); t.position.set(tx + s * 2 + r() * 2, 0.15, s * 4.75); g.add(t); }
    for (let k = 0; k < 8; k++) { const m = motorbike(["#c0392b", "#2c3e50", "#ecf0f1", "#2980b9", "#16a085"][Math.floor(r() * 5)], (["wave", "sh", "vision"] as const)[k % 3]); m.position.set(-38 + k * 11 + r() * 3, 0.15, -s * 0 + s * 6.4); m.rotation.y = Math.PI / 2 + (r() - 0.5) * 0.4; if (s > 0 && k >= 3 && k <= 5) continue; g.add(m); }
  }
  // queue props: plastic stools along the line
  const stoolX = [2, 7, 12, 17, 22].map((i) => GOLD_X + 1.4 + i * 1.15).concat([2.0, 5.2, 8.6, 11.8].map((d) => GOLD_X + d));
  stoolX.forEach((x, k) => { const st = stool(["#d93636", "#2f6fd1"][k % 2]); st.position.set(x, 0.15, 5.92); g.add(st); });
  // chỗ mẹ ngồi bán rau (phố huyện): ghế nhựa + thúng rau
  const ms = stool("#2f6fd1"); ms.position.set(-30, 0.15, 6.05); g.add(ms);
  for (const [bx, bz] of [[-29.1, 5.75], [-30.9, 5.8]]) { const bk = cyl(0.34, 0.26, 0.26, lam("#a8793e"), 14); bk.position.set(bx, 0.28, bz); g.add(bk);
    for (let k = 0; k < 6; k++) { const v = new THREE.Mesh(new THREE.IcosahedronGeometry(0.11, 0), lam(["#3f9a4a", "#6bb04a", "#e0532e"][k % 3])); v.position.set(bx + (k % 3 - 1) * 0.14, 0.45, bz + (k < 3 ? -0.08 : 0.08)); g.add(v); } }
  // own bike of Đô (to wheel out)
  const bikeDo = motorbike("#8e2c2c", "wave"); bikeDo.position.set(HOME_X + 1.2, 0.15, 5.0); bikeDo.rotation.y = Math.PI / 2; g.add(bikeDo);
  return { g, bikeDo };
}

// ---------- GOLD SHOP INTERIOR ----------
export function buildShop() {
  const g = new THREE.Group(); g.position.x = IX;
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(10, 8), lam("#e9dfcf")); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; g.add(floor);
  const red = lam("#a3121d"), back = box(10, 3.6, 0.15, red, false); back.position.set(0, 1.8, -3); g.add(back);
  for (const s of [-1, 1]) { const w = box(0.15, 3.6, 8, lam("#8f0e18"), false); w.position.set(s * 5, 1.8, 0.5); g.add(w); }
  // big golden letters on the back wall
  const [lc, lg] = cvs(1024, 200); lg.fillStyle = "rgba(0,0,0,0)"; lg.clearRect(0, 0, 1024, 200); lg.fillStyle = "#ffd84a"; lg.font = `900 130px ${F}`; lg.textAlign = "center"; lg.textBaseline = "middle"; lg.fillText("BẢO TÍN MINH ANH", 512, 104, 990);
  const lm = new THREE.MeshBasicMaterial({ map: ctex(lc), transparent: true }); lm.color.setRGB(1.7, 1.5, 1.2);
  const letters = new THREE.Mesh(new THREE.PlaneGeometry(6, 1.2), lm); letters.position.set(0, 2.9, -2.9); letters.layers.set(NOINK); g.add(letters);
  // price LED board
  const [pc, pg] = cvs(900, 360); const pt = ctex(pc);
  const pb = new THREE.Mesh(new THREE.PlaneGeometry(2.5, 1.0), new THREE.MeshBasicMaterial({ map: pt })); pb.position.set(-3.2, 2.1, -2.9); pb.layers.set(NOINK); g.add(pb);
  // shelves of gold
  const shelfM = lam("#6b0b12"), goldM = glow(1.9, 1.45, 0.45);
  for (const y of [0.9, 1.45]) { const sh = box(8, 0.06, 0.5, shelfM); sh.position.set(0, y, -2.7); g.add(sh);
    for (let x = -3.7; x < 3.8; x += 0.35) { const gb = box(0.22, 0.08, 0.12, goldM); gb.position.set(x, y + 0.08, -2.65); gb.layers.set(NOINK); g.add(gb); } }
  // glass counter with rings
  const cnt = box(7, 0.9, 0.8, lam("#3a0a10")); cnt.position.set(0, 0.45, -0.6); g.add(cnt);
  const glass = new THREE.Mesh(new THREE.BoxGeometry(7, 0.35, 0.8), new THREE.MeshBasicMaterial({ color: "#bfe8ff", transparent: true, opacity: 0.18, depthWrite: false })); glass.position.set(0, 1.08, -0.6); glass.layers.set(NOINK); g.add(glass);
  for (let x = -3.2; x < 3.3; x += 0.32) for (const z of [-0.8, -0.45]) { const rg = new THREE.Mesh(new THREE.TorusGeometry(0.07, 0.022, 6, 16), goldM); rg.rotation.x = -Math.PI / 2.4; rg.position.set(x, 0.96, z); rg.layers.set(NOINK); g.add(rg); }
  const lights = box(8, 0.05, 0.3, glow(2.4, 2.2, 1.8), false); lights.position.set(0, 3.5, -1); lights.layers.set(NOINK); g.add(lights);
  return { g, board: { c: pc, g: pg, t: pt } as Screen };
}

// ---------- HUẾ: cầu Trường Tiền rạng sáng ----------
export function buildHue() {
  const g = new THREE.Group(); g.position.x = HX; const r = rng(23);
  const river = new THREE.Mesh(new THREE.PlaneGeometry(400, 300), new THREE.MeshBasicMaterial({ map: waterTex("#4a6fa0", "rgba(255,200,170,.5)", 9) })); river.rotation.x = -Math.PI / 2; river.position.y = -1.2; ((river.material as THREE.MeshBasicMaterial).map!).repeat.set(20, 15); g.add(river);
  for (const s of [-1, 1]) { const bank = box(400, 1.4, 40, lam("#5e7e46")); bank.position.set(0, -0.6, s * 62); g.add(bank);
    for (let k = 0; k < 18; k++) { const t = treeV(r, (["bang", "sau", "cau", "bang"] as const)[k % 4]); t.position.set(-90 + k * 11 + r() * 4, 0.1, s * (46 + r() * 10)); g.add(t); } }
  // far hills (Núi Ngự Bình)
  const hill = new THREE.Mesh(new THREE.SphereGeometry(60, 24, 12, 0, Math.PI * 2, 0, Math.PI / 2), lam("#5d6f8e")); hill.scale.set(1.6, 0.35, 0.6); hill.position.set(40, -2, -170); g.add(hill);
  // bridge along z (from bank z=-42 to z=42), deck at y=1.2, 6 spans
  const steel = lam("#cfd6de"), deckM = lam("#8b8f96"), N = 6, Lspan = 14, z0 = -42;
  const deck = box(7, 0.35, N * Lspan, deckM); deck.position.set(0, 1.0, 0); g.add(deck);
  for (let i = 0; i <= N; i++) { const pier = box(7.5, 2.4, 1.4, lam("#a9a196")); pier.position.set(0, -0.2, z0 + i * Lspan); g.add(pier); }
  for (let i = 0; i < N; i++) for (const sx of [-3.4, 3.4]) {
    const za = z0 + i * Lspan, pts: THREE.Vector3[] = [];
    for (let k = 0; k <= 16; k++) { const u = k / 16; pts.push(new THREE.Vector3(sx, 1.2 + 4.2 * Math.sin(Math.PI * u) ** 0.8, za + u * Lspan)); }
    const curve = new THREE.CatmullRomCurve3(pts); const arch = new THREE.Mesh(new THREE.TubeGeometry(curve, 32, 0.14, 6), steel); arch.castShadow = true; g.add(arch);
    const bot = box(0.22, 0.22, Lspan, steel); bot.position.set(sx, 1.25, za + Lspan / 2); g.add(bot);
    for (let k = 1; k < 8; k++) { const u = k / 8, h = 4.2 * Math.sin(Math.PI * u) ** 0.8; const v = box(0.1, h, 0.1, steel); v.position.set(sx, 1.2 + h / 2, za + u * Lspan); g.add(v);
      const u2 = (k + 1) / 8, h2 = 4.2 * Math.sin(Math.PI * Math.min(u2, 1)) ** 0.8; const dz = Lspan / 8, len = Math.hypot(dz, (h + h2) / 2);
      const d = box(0.07, len, 0.07, steel); d.position.set(sx, 1.2 + (h + h2) / 4, za + (u + u2) / 2 * Lspan); d.rotation.x = Math.atan2(dz, (h + h2) / 2); g.add(d); }
  }
  for (let k = 0; k < 13; k++) for (const sx of [-3.6, 3.6]) { const lp = lampPost([2.4, 1.9, 1.3], 2.6); lp.scale.setScalar(0.8); lp.position.set(sx, 1.2, z0 + k * 7); lp.rotation.y = sx > 0 ? Math.PI : 0; g.add(lp); }
  // a few sampan boats
  for (let k = 0; k < 3; k++) { const b = new THREE.Mesh(new THREE.CapsuleGeometry(0.6, 3.5, 4, 8), lam("#6b4a2e")); b.rotation.x = Math.PI / 2; b.scale.set(1, 1, 0.4); b.position.set(-18 - k * 9, -1.0, -12 + k * 10); g.add(b);
    const roof = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.7, 2, 10, 1, true, 0, Math.PI), lam("#3b2a1e")); roof.rotation.z = Math.PI / 2; roof.rotation.y = Math.PI / 2; roof.position.set(b.position.x, -0.6, b.position.z); (roof.material as THREE.Material).side = THREE.DoubleSide; g.add(roof); }
  return { g };
}

// ---------- SÀI GÒN: chợ Bến Thành buổi sáng ----------
function clockTex(h = 7, m = 10) {
  const [c, g] = cvs(256, 256); g.fillStyle = "#f7f3e6"; g.beginPath(); g.arc(128, 128, 120, 0, 7); g.fill(); g.lineWidth = 10; g.strokeStyle = "#2b2b2b"; g.stroke();
  for (let i = 0; i < 12; i++) { const a = i / 12 * Math.PI * 2; g.fillStyle = "#2b2b2b"; g.fillRect(128 + Math.sin(a) * 100 - 4, 128 - Math.cos(a) * 100 - 4, 8, 8); }
  const hand = (a: number, L: number, w: number) => { g.strokeStyle = "#1a1a1a"; g.lineWidth = w; g.lineCap = "round"; g.beginPath(); g.moveTo(128, 128); g.lineTo(128 + Math.sin(a) * L, 128 - Math.cos(a) * L); g.stroke(); };
  hand(((h % 12) + m / 60) / 12 * Math.PI * 2, 60, 12); hand(m / 60 * Math.PI * 2, 92, 8); return ctex(c);
}
export function buildBenThanh() {
  const g = new THREE.Group(); g.position.x = BX; const r = rng(31);
  const road = new THREE.Mesh(new THREE.PlaneGeometry(240, 22), lam("#ffffff", asphalt())); road.rotation.x = -Math.PI / 2; road.position.z = 10; ((road.material as THREE.MeshLambertMaterial).map!).repeat.set(50, 5); road.receiveShadow = true; g.add(road);
  const plaza = new THREE.Mesh(new THREE.PlaneGeometry(240, 14), lam("#ffffff", tiles())); plaza.rotation.x = -Math.PI / 2; plaza.position.set(0, 0.02, -7); ((plaza.material as THREE.MeshLambertMaterial).map!).repeat.set(120, 7); g.add(plaza);
  // facade texture: cream wall with arched windows
  const [fc, fg] = cvs(1024, 256); fg.fillStyle = "#efd58c"; fg.fillRect(0, 0, 1024, 256); fg.fillStyle = "#d9b968"; fg.fillRect(0, 0, 1024, 26); fg.fillRect(0, 120, 1024, 12);
  for (let x = 20; x < 1024; x += 64) { fg.fillStyle = "#3b2a22"; fg.beginPath(); fg.moveTo(x, 250); fg.lineTo(x, 175); fg.arc(x + 20, 175, 20, Math.PI, 0); fg.lineTo(x + 40, 250); fg.fill(); fg.fillStyle = "#5c4636"; fg.fillRect(x + 6, 45, 28, 60); }
  const fac = lam("#ffffff", ctex(fc, true)); ((fac.map!) as THREE.Texture).repeat.set(4, 1);
  const main = box(80, 9, 30, [lam("#efd58c"), lam("#efd58c"), lam("#b4532c"), lam("#efd58c"), fac, lam("#efd58c")]); main.position.set(0, 4.5, -30); g.add(main);
  const roof = box(82, 1.2, 31, lam("#a8482a")); roof.position.set(0, 9.4, -30); g.add(roof);
  // clock tower (iconic)
  const tower = box(8, 18, 8, lam("#f1db97")); tower.position.set(0, 9, -14.5); g.add(tower);
  const t2 = box(6.4, 4, 6.4, lam("#f6e3a8")); t2.position.set(0, 20, -14.5); g.add(t2);
  const cap = new THREE.Mesh(new THREE.ConeGeometry(4.8, 3, 4), lam("#a8482a")); cap.rotation.y = Math.PI / 4; cap.position.set(0, 23.5, -14.5); cap.castShadow = true; g.add(cap);
  const ck = clockTex(7, 10);
  for (const [dx, dz, ry] of [[0, 3.22, 0], [3.22, 0, Math.PI / 2], [-3.22, 0, -Math.PI / 2]] as const) { const cf = new THREE.Mesh(new THREE.CircleGeometry(1.6, 32), lam("#ffffff", ck)); cf.position.set(dx, 20, -14.5 + dz); cf.rotation.y = ry; g.add(cf); }
  const [nc, ng] = cvs(1024, 160); ng.fillStyle = "#efd58c"; ng.fillRect(0, 0, 1024, 160); ng.fillStyle = "#7a2a17"; ng.font = `900 110px ${F}`; ng.textAlign = "center"; ng.textBaseline = "middle"; ng.fillText("CHỢ BẾN THÀNH", 512, 84, 980);
  const nm = new THREE.Mesh(new THREE.PlaneGeometry(7.6, 1.2), lam("#ffffff", ctex(nc))); nm.position.set(0, 15.5, -10.45); g.add(nm);
  const gate = box(4.4, 5, 0.3, lam("#3b2a22")); gate.position.set(0, 2.5, -10.4); g.add(gate);
  // palm/tamarind trees along plaza
  for (let k = 0; k < 14; k++) { const t = treeV(r, k % 3 === 1 ? "bang" : "cau"); t.position.set(-60 + k * 9 + r() * 2, 0, -1.5 - r() * 2); g.add(t); }
  for (let k = 0; k < 10; k++) { const b = treeV(r, "bui"); b.position.set(-45 + k * 9, 0, -8.5); g.add(b); }
  // a gold shop row across the road (queue)
  for (let k = 0; k < 4; k++) g.add(house(-30 + k * 5, 1, 4.8, 4, 700 + k, k === 1 ? "TIỆM VÀNG" : k === 2 ? "VÀNG BẠC" : null, false, false)).children.slice(-1)[0].position.z = 28;
  return { g };
}

// ---------- HỒ GƯƠM: cầu Thê Húc đêm ----------
export function buildHoGuom() {
  const g = new THREE.Group(); g.position.x = GX; const r = rng(41);
  const lake = new THREE.Mesh(new THREE.PlaneGeometry(400, 300), new THREE.MeshBasicMaterial({ map: waterTex("#121a3e", "rgba(255,150,90,.55)", 13) })); lake.rotation.x = -Math.PI / 2; lake.position.y = -0.6; ((lake.material as THREE.MeshBasicMaterial).map!).repeat.set(25, 18); g.add(lake);
  // shore promenade (camera side, z>8)
  const shore = box(200, 0.8, 30, lam("#6b7a5a")); shore.position.set(0, -0.3, 24); g.add(shore);
  const walk = new THREE.Mesh(new THREE.PlaneGeometry(200, 5), lam("#ffffff", tiles())); walk.rotation.x = -Math.PI / 2; walk.position.set(0, 0.11, 11.5); ((walk.material as THREE.MeshLambertMaterial).map!).repeat.set(100, 2.5); g.add(walk);
  for (let k = 0; k < 16; k++) { const w = willow(r); w.position.set(-70 + k * 9 + r() * 3, 0.1, 9.6 + r() * 1.5); g.add(w); }
  for (let k = 0; k < 12; k++) { const t = treeV(r, k % 2 ? "bang" : "sau", true); t.position.set(-66 + k * 11 + r() * 3, 0.1, 16 + r() * 3); g.add(t); }
  for (let k = 0; k < 14; k++) { const lp = lampPost([2.8, 2.1, 1.2], 3.6); lp.position.set(-60 + k * 9, 0.1, 13.8); lp.rotation.y = -Math.PI / 2; g.add(lp); }
  // bench for the couple
  const bench = new THREE.Group(); const bs = box(1.8, 0.08, 0.45, lam("#6b4a2e")); bs.position.y = 0.45; bench.add(bs); const bb = box(1.8, 0.4, 0.06, lam("#6b4a2e")); bb.position.set(0, 0.75, -0.22); bench.add(bb);
  for (const x of [-0.8, 0.8]) { const l = box(0.06, 0.45, 0.4, lam("#222")); l.position.set(x, 0.22, 0); bench.add(l); } bench.position.set(-6, 0.1, 12.4); g.add(bench);
  // Thê Húc bridge: red arched deck from the shore (z=8.5) to Ngọc Sơn island (z=-22), offset in x
  const red = lam("#d0202a"), redD = lam("#a8141e"), lanternM = glow(3.0, 1.6, 0.6), bx0 = 6, N = 30;
  for (let k = 0; k < N; k++) { const u0 = k / N, u1 = (k + 1) / N, z0 = 8.5 - u0 * 30.5, z1 = 8.5 - u1 * 30.5, y0 = 0.2 + 2.6 * Math.sin(Math.PI * u0), y1 = 0.2 + 2.6 * Math.sin(Math.PI * u1);
    const len = Math.hypot(z1 - z0, y1 - y0), seg = box(2.4, 0.18, len + 0.02, redD); seg.position.set(bx0, (y0 + y1) / 2, (z0 + z1) / 2); seg.rotation.x = Math.atan2(y1 - y0, z0 - z1); g.add(seg);
    for (const sx of [-1.15, 1.15]) { const rl = box(0.1, 0.08, len + 0.02, red); rl.position.set(bx0 + sx, (y0 + y1) / 2 + 0.75, (z0 + z1) / 2); rl.rotation.x = seg.rotation.x; g.add(rl);
      const post = box(0.1, 0.75, 0.1, red); post.position.set(bx0 + sx, y0 + 0.38, z0); g.add(post);
      if (k % 3 === 0) { const ln = new THREE.Mesh(new THREE.SphereGeometry(0.13, 10, 8), lanternM); ln.position.set(bx0 + sx, y0 + 0.95, z0); ln.layers.set(NOINK); g.add(ln); } }
    if (k % 5 === 2) { const leg = box(0.25, 3, 0.25, redD); leg.position.set(bx0, y0 - 1.5, z0); g.add(leg); }
  }
  // gate at shore end (Thê Húc gate)
  const gt = new THREE.Group(); const gb = box(3.6, 3.2, 1.2, lam("#b81d24")); gb.position.y = 1.6; gt.add(gb); const gr = box(4.4, 0.4, 1.8, lam("#4a2a20")); gr.position.y = 3.4; gt.add(gr);
  const gr2 = box(3.0, 0.9, 1.3, lam("#c9a64a")); gr2.position.y = 4.0; gt.add(gr2); const gr3 = box(3.6, 0.3, 1.6, lam("#4a2a20")); gr3.position.y = 4.6; gt.add(gr3);
  gt.position.set(bx0, 0.1, 10); g.add(gt);
  // Ngọc Sơn temple on the island
  const isl = box(26, 1.2, 14, lam("#3d5a3a")); isl.position.set(bx0, -0.3, -29); g.add(isl);
  const temple = box(10, 3.4, 6, lam("#c9a07a")); temple.position.set(bx0, 1.9, -29); g.add(temple);
  const troof = new THREE.Mesh(new THREE.ConeGeometry(7.5, 2.4, 4), lam("#5a2e22")); troof.rotation.y = Math.PI / 4; troof.scale.set(1, 1, 0.55); troof.position.set(bx0, 4.6, -29); troof.castShadow = true; g.add(troof);
  const tl = box(8, 1.2, 0.05, glow(2.2, 1.4, 0.6), false); tl.position.set(bx0, 1.4, -25.95); tl.layers.set(NOINK); g.add(tl);
  for (let k = 0; k < 5; k++) { const t = tree(r, 3.6, ["#1f3d2a", "#294b31", "#1a3424"]); t.position.set(bx0 - 11 + k * 5.5, 0.3, -33 + r() * 3); g.add(t); }
  // Tháp Rùa on its islet (far left)
  const tr = new THREE.Group(); const ti = box(7, 0.8, 5, lam("#3d5a3a")); ti.position.y = -0.2; tr.add(ti);
  const [tc, tg] = cvs(256, 256); tg.fillStyle = "#d8cfbf"; tg.fillRect(0, 0, 256, 256); tg.fillStyle = "#2a2a35"; for (const x of [40, 110, 180]) { tg.beginPath(); tg.moveTo(x, 230); tg.lineTo(x, 150); tg.arc(x + 18, 150, 18, Math.PI, 0); tg.lineTo(x + 36, 230); tg.fill(); }
  const tm = lam("#ffffff", ctex(tc));
  const lv = [[4.2, 2.6, 2.4], [3.2, 1.8, 1.8], [2.2, 1.4, 1.3]];
  let y = 0.2; for (const [w, h, d] of lv) { const b = box(w, h, d, tm); b.position.y = y + h / 2; tr.add(b); y += h; const rf = box(w + 0.2, 0.15, d + 0.2, lam("#8a8070")); rf.position.y = y; tr.add(rf); }
  const top = cyl(0.4, 0.6, 0.8, lam("#d8cfbf"), 8); top.position.y = y + 0.4; tr.add(top);
  const tlit = box(4.3, 0.6, 0.05, glow(2.4, 1.7, 0.9), false); tlit.position.set(0, 1.0, 1.25); tlit.layers.set(NOINK); tr.add(tlit);
  tr.position.set(-34, 0, -48); g.add(tr);
  // distant city skyline lights across the lake
  const [sc, sg] = cvs(2048, 256); sg.clearRect(0, 0, 2048, 256);
  for (let i = 0; i < 70; i++) { const bw = 20 + r() * 60, bh = 40 + r() * 170, bxx = r() * 2048; sg.fillStyle = "#121733"; sg.fillRect(bxx, 256 - bh, bw, bh); sg.fillStyle = "rgba(255,200,120,.9)"; for (let k = 0; k < 8; k++) if (r() < 0.6) sg.fillRect(bxx + 3 + r() * (bw - 8), 256 - bh + r() * bh, 4, 5); }
  const sky = new THREE.Mesh(new THREE.PlaneGeometry(300, 37), new THREE.MeshBasicMaterial({ map: ctex(sc), transparent: true })); sky.position.set(0, 16, -110); sky.layers.set(NOINK); g.add(sky);
  return { g };
}
