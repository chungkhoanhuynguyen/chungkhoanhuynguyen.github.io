// Bối cảnh 3D cho "Lớp học Lý thuyết trò chơi – Bài 1" (bản người que, 15/11/2026).
// Mỗi bối cảnh dựng quanh gốc toạ độ (Stage chỉ dựng 1 bối cảnh/đoạn). Tất cả mesh đổ bóng + nhận bóng.
import * as THREE from "three";
import { rng } from "../pho/paint";
import { lam, glow, box, cyl, treeV, waterTex } from "../vang/sets";

const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";
const cvs = (w: number, h: number) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return [c, c.getContext("2d")!] as const; };
const ctex = (c: HTMLCanvasElement, rep = false) => { const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; if (rep) t.wrapS = t.wrapT = THREE.RepeatWrapping; return t; };
const sh = <T extends THREE.Object3D>(o: T) => { o.traverse((m) => { const k = m as THREE.Mesh; if (k.isMesh) { k.castShadow = !k.userData.nc; k.receiveShadow = true; } }); return o; };
const at = <T extends THREE.Object3D>(o: T, x: number, y: number, z: number, ry = 0) => { o.position.set(x, y, z); o.rotation.y = ry; return o; };
const ground = (col: string, size = 400) => { const m = new THREE.Mesh(new THREE.PlaneGeometry(size, size), lam(col)); m.rotation.x = -Math.PI / 2; m.receiveShadow = true; return m; };
const water = (col: string, y = -0.3, size = 600, rep = 30) => { const tx = waterTex(col, "rgba(255,240,210,.35)", 7); tx.repeat.set(rep, rep); const m = new THREE.Mesh(new THREE.PlaneGeometry(size, size), new THREE.MeshLambertMaterial({ map: tx })); m.rotation.x = -Math.PI / 2; m.position.y = y; m.receiveShadow = true; return m; };
const hillM = (r: number, col: string, sx = 1, sy = 0.4, sz = 1) => { const h = new THREE.Mesh(new THREE.SphereGeometry(r, 20, 10, 0, Math.PI * 2, 0, Math.PI / 2), lam(col)); h.scale.set(sx, sy, sz); h.castShadow = h.receiveShadow = true; return h; };
const peak = (r: number, h: number, col: string, snow?: string) => { const g = new THREE.Group(); const c = new THREE.Mesh(new THREE.ConeGeometry(r, h, 14, 1), lam(col)); c.position.y = h / 2; g.add(c); if (snow) { const s = new THREE.Mesh(new THREE.ConeGeometry(r * 0.28, h * 0.28, 14), lam(snow)); s.position.y = h * 0.86; g.add(s); } return sh(g); };
/** người que nền (lính, dân): thân trụ + đầu cầu, có thể cầm giáo/cờ */
function extra(col: string, skin = "#e9c29a", spear = false, hatC?: string) {
  const g = new THREE.Group(); const b = cyl(0.17, 0.24, 0.95, lam(col), 8); b.position.y = 0.75; g.add(b);
  const h = new THREE.Mesh(new THREE.SphereGeometry(0.17, 10, 8), lam(skin)); h.position.y = 1.4; g.add(h);
  for (const s of [-1, 1]) { const l = cyl(0.06, 0.06, 0.5, lam("#2a2522"), 6); l.position.set(s * 0.09, 0.25, 0); g.add(l); }
  if (hatC) { const hat = cyl(0.19, 0.19, 0.12, lam(hatC), 10); hat.position.y = 1.55; g.add(hat); }
  if (spear) { const sp = cyl(0.025, 0.025, 2.4, lam("#6a4a32"), 5); sp.position.set(0.3, 1.2, 0); g.add(sp); const tip = new THREE.Mesh(new THREE.ConeGeometry(0.06, 0.25, 5), lam("#c9ced4")); tip.position.set(0.3, 2.5, 0); g.add(tip); }
  return sh(g);
}
function banner(col: string, h = 4, txt?: string) {
  const g = new THREE.Group(); const p = cyl(0.05, 0.05, h, lam("#5a3b2a"), 6); p.position.y = h / 2; g.add(p);
  const [c, x] = cvs(128, 192); x.fillStyle = col; x.fillRect(0, 0, 128, 192); if (txt) { x.fillStyle = "#f2d36b"; x.font = `900 84px ${F}`; x.textAlign = "center"; x.fillText(txt, 64, 120); }
  const f = new THREE.Mesh(new THREE.PlaneGeometry(0.9, 1.35), new THREE.MeshLambertMaterial({ map: ctex(c), side: THREE.DoubleSide })); f.position.set(0.47, h - 0.75, 0); g.add(f); return sh(g);
}
function roofCurved(w: number, d: number, col: string, h = 1.2) { // mái cong kiểu cung điện Á Đông
  const g = new THREE.Group(); const m = lam(col); m.side = THREE.DoubleSide;
  for (const s of [-1, 1]) { const shape = new THREE.Shape(); shape.moveTo(0, 0); shape.quadraticCurveTo(d * 0.25, h * 0.15, d / 2, h); shape.lineTo(d / 2, h + 0.08); shape.quadraticCurveTo(d * 0.22, h * 0.25, -0.2, 0.25); shape.lineTo(0, 0);
    const geo = new THREE.ExtrudeGeometry(shape, { depth: w, bevelEnabled: false }); const r = new THREE.Mesh(geo, m); r.rotation.y = s > 0 ? -Math.PI / 2 : Math.PI / 2; r.position.set(s > 0 ? -w / 2 : w / 2, 0, s * d / 2); r.scale.z = 1; if (s > 0) r.position.z = d / 2; else { r.position.z = -d / 2; }
    r.rotation.y = s > 0 ? Math.PI / 2 : -Math.PI / 2; r.position.x = s > 0 ? -w / 2 : w / 2; g.add(r); }
  const ridge = box(w + 0.4, 0.18, 0.25, lam("#2a1d14")); ridge.position.y = h + 0.05; g.add(ridge);
  return sh(g);
}
function pagoda(w: number, d: number, tiers: number, wall = "#b8322c", roof = "#2f4a3a") {
  const g = new THREE.Group(); let y = 0;
  const base = box(w + 2, 1, d + 2, lam("#cfc4ae")); base.position.y = 0.5; g.add(base); y = 1;
  for (let i = 0; i < tiers; i++) { const k = 1 - i * 0.22, ww = w * k, dd = d * k, hh = 3 - i * 0.6;
    const body = box(ww, hh, dd, lam("#f1e6cf")); body.position.y = y + hh / 2; g.add(body);
    for (let c = 0; c < 6; c++) for (const s of [-1, 1]) { const col = cyl(0.16, 0.16, hh, lam(wall), 8); col.position.set(-ww / 2 + (c + 0.5) * ww / 6, y + hh / 2, s * (dd / 2 + 0.25)); g.add(col); }
    const r = roofCurved(ww + 1.6, dd + 2.2, roof, 1.1); r.position.y = y + hh; g.add(r); y += hh + 1.1; }
  return sh(g);
}
function lantern(c = [2.4, 1.2, 0.4] as [number, number, number]) { const g = new THREE.Group(); const l = new THREE.Mesh(new THREE.SphereGeometry(0.22, 10, 8), glow(...c)); l.scale.y = 1.25; g.add(l); return g; }
function house(w: number, h: number, d: number, wall: string, roof: string, flat = false) {
  const g = new THREE.Group(); const b = box(w, h, d, lam(wall)); b.position.y = h / 2; g.add(b);
  if (flat) { const r = box(w + 0.15, 0.18, d + 0.15, lam(roof)); r.position.y = h + 0.09; g.add(r); }
  else { const r = new THREE.Mesh(new THREE.ConeGeometry(Math.max(w, d) * 0.78, h * 0.55, 4), lam(roof)); r.rotation.y = Math.PI / 4; r.scale.set(w / Math.max(w, d), 1, d / Math.max(w, d)); r.position.y = h + h * 0.27; g.add(r); }
  const door = box(0.5, 0.9, 0.05, lam("#4a3426"), false); door.position.set(0, 0.45, d / 2 + 0.03); g.add(door);
  const win = box(0.4, 0.35, 0.05, lam("#2a2f3a"), false); win.position.set(w * 0.28, h * 0.62, d / 2 + 0.03); g.add(win);
  return sh(g);
}
function palm(r: () => number) {
  const g = new THREE.Group(); const h = 4 + r() * 2, lean = (r() - 0.5) * 0.6;
  for (let k = 0; k < 6; k++) { const s = cyl(0.17 - k * 0.012, 0.19 - k * 0.012, h / 6, lam(k % 2 ? "#7a5a3c" : "#8a6a48"), 7); s.position.set(lean * k / 6, h * (k + 0.5) / 6, 0); g.add(s); }
  const fm = lam("#3f8a3a"); fm.side = THREE.DoubleSide;
  for (let k = 0; k < 8; k++) { const f = new THREE.Mesh(new THREE.PlaneGeometry(0.5, 2.6), fm); const a = k / 8 * Math.PI * 2; f.position.set(lean + Math.cos(a) * 1.1, h - 0.1, Math.sin(a) * 1.1); f.rotation.set(-Math.PI / 2 + 0.5, 0, 0); f.rotation.y = -a + Math.PI / 2; f.rotateX(0.9); g.add(f); }
  return sh(g);
}
function column(h: number, r = 0.32) { const g = new THREE.Group(); const c = cyl(r * 0.9, r, h, lam("#eee7d8"), 14); c.position.y = h / 2; g.add(c); const cap = box(r * 2.6, 0.2, r * 2.6, lam("#e5dccb")); cap.position.y = h + 0.1; g.add(cap); return g; }
function temple(nx: number, nz: number, h = 4) {
  const g = new THREE.Group(), sp = 1.3, w = (nx - 1) * sp + 1.6, d = (nz - 1) * sp + 1.6;
  for (let i = 0; i < 3; i++) { const s = box(w + 1.2 - i * 0.4, 0.25, d + 1.2 - i * 0.4, lam("#e2d8c4")); s.position.y = 0.125 + i * 0.25; g.add(s); }
  for (let i = 0; i < nx; i++) for (let j = 0; j < nz; j++) if (i === 0 || j === 0 || i === nx - 1 || j === nz - 1) { const c = column(h); c.position.set(-w / 2 + 0.8 + i * sp, 0.75, -d / 2 + 0.8 + j * sp); g.add(c); }
  const cella = box(w - 3, h - 0.4, d - 3.2, lam("#ddd3bf")); cella.position.y = 0.75 + (h - 0.4) / 2; g.add(cella);
  const ent = box(w + 0.3, 0.6, d + 0.3, lam("#e7dfcf")); ent.position.y = 0.75 + h + 0.4; g.add(ent);
  const tri = new THREE.Shape(); tri.moveTo(-w / 2 - 0.15, 0); tri.lineTo(w / 2 + 0.15, 0); tri.lineTo(0, 1.3); tri.lineTo(-w / 2 - 0.15, 0);
  const ped = new THREE.Mesh(new THREE.ExtrudeGeometry(tri, { depth: d + 0.3, bevelEnabled: false }), lam("#e9e1d0")); ped.position.set(0, 0.75 + h + 0.7, -d / 2 - 0.15); g.add(ped);
  const frieze = box(w + 0.32, 0.18, d + 0.32, lam("#b8452f")); frieze.position.y = 0.75 + h + 0.15; g.add(frieze);
  return sh(g);
}
function boatHull(len: number, col: string, oars = 0) {
  const g = new THREE.Group(); const b = new THREE.Mesh(new THREE.CapsuleGeometry(len * 0.11, len * 0.78, 4, 10), lam(col)); b.rotation.z = Math.PI / 2; b.scale.set(0.7, 1, 0.75); b.position.y = 0.15; g.add(b);
  const deck = box(len * 0.8, 0.08, len * 0.16, lam("#a07a52")); deck.position.y = 0.32; g.add(deck);
  for (let i = 0; i < oars; i++) for (const s of [-1, 1]) { const o = cyl(0.03, 0.03, len * 0.25, lam("#d8c7a8"), 4); o.rotation.x = s * 1.1; o.position.set(-len * 0.35 + i * len * 0.7 / Math.max(1, oars - 1), 0.1, s * len * 0.14); g.add(o); }
  return sh(g);
}
function sail(w: number, h: number, col: string, cross?: string) { const [c, x] = cvs(128, 160); x.fillStyle = col; x.fillRect(0, 0, 128, 160); if (cross) { x.fillStyle = cross; x.fillRect(54, 20, 20, 120); x.fillRect(24, 60, 80, 20); } const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h, 6, 1), new THREE.MeshLambertMaterial({ map: ctex(c), side: THREE.DoubleSide })); const p = m.geometry.attributes.position; for (let i = 0; i < p.count; i++) p.setZ(i, Math.sin((p.getX(i) / w + 0.5) * Math.PI) * 0.35); p.needsUpdate = true; m.geometry.computeVertexNormals(); m.castShadow = true; return m; }
function galleon() {
  const g = new THREE.Group(); const hull = boatHull(9, "#5a3b22"); hull.scale.y = 2.2; g.add(hull);
  const stern = box(1.8, 1.4, 2, lam("#6b4a2e")); stern.position.set(-3.6, 1.4, 0); g.add(stern);
  for (const [x, h] of [[-1.5, 6], [1.2, 7], [3.4, 4.5]] as [number, number][]) { const m = cyl(0.08, 0.1, h, lam("#4a3426"), 6); m.position.set(x, 0.7 + h / 2, 0); g.add(m);
    const s1 = sail(2.6, h * 0.42, "#f2ead6", x === 1.2 ? "#c0392b" : undefined); s1.position.set(x + 0.1, 0.7 + h * 0.5, 0.15); g.add(s1);
    const s2 = sail(2.0, h * 0.28, "#efe5cf"); s2.position.set(x + 0.1, 0.7 + h * 0.86, 0.15); g.add(s2); }
  return sh(g);
}
export type Board = { c: HTMLCanvasElement; g: CanvasRenderingContext2D; t: THREE.CanvasTexture; last: string };

// ---------- LỚP HỌC QUÝ TỘC (Học viện St. Alden) ----------
export const LOP_SEATS: Record<string, [number, number]> = { phu: [-2.6, 0.6], qha: [0, 0.6], vy: [2.6, 0.6], trang: [-2.6, 3.0], hung: [0, 3.0], linh: [2.6, 3.0] };
export function buildLop() {
  const g = new THREE.Group(), r = rng(5);
  const [fc, fx] = cvs(512, 512); fx.fillStyle = "#7a4a2a"; fx.fillRect(0, 0, 512, 512); for (let i = 0; i < 16; i++) { fx.fillStyle = i % 2 ? "#6e4226" : "#83522f"; fx.fillRect(0, i * 32, 512, 30); for (let k = 0; k < 4; k++) { fx.fillStyle = "rgba(0,0,0,.25)"; fx.fillRect((k * 131 + i * 57) % 512, i * 32, 2, 30); } }
  const ft = ctex(fc, true); ft.repeat.set(4, 4); const floor = new THREE.Mesh(new THREE.PlaneGeometry(22, 22), lam("#ffffff", ft)); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; g.add(floor);
  const rug = box(8.6, 0.02, 7, lam("#8e1d24")); rug.position.set(0, 0.01, 1.8); g.add(rug); const rugB = box(9, 0.015, 7.4, lam("#c9a64a")); rugB.position.set(0, 0.005, 1.8); g.add(rugB);
  const wallM = lam("#efe2c6"), wood = lam("#5a2e1c");
  const back = box(22, 7, 0.3, wallM); back.position.set(0, 3.5, -4.5); back.userData.nc = 1; g.add(back);
  for (const s of [-1, 1]) { const side = box(0.3, 7, 22, wallM); side.position.set(s * 8, 3.5, 4); side.userData.nc = 1; g.add(side); const wain = box(0.1, 1.3, 22, wood); wain.position.set(s * 7.82, 0.65, 4); g.add(wain); }
  const wainB = box(22, 1.3, 0.1, wood); wainB.position.set(0, 0.65, -4.32); g.add(wainB);
  const front = box(22, 7, 0.3, wallM); front.position.set(0, 3.5, 11); front.userData.nc = 1; g.add(front); const wf = box(22, 1.3, 0.1, wood); wf.position.set(0, 0.65, 10.82); g.add(wf);
  const door = box(1.8, 3.2, 0.12, wood); door.position.set(5, 1.6, 10.8); g.add(door);
  for (const [x, col] of [[-4, "#6a4a7a"], [0, "#3a5a6a"], [-1.5 + 9, "#7a5a3a"]] as [number, string][]) { if (x > 6) continue; const fr2 = box(2, 1.4, 0.08, lam("#c9a24a")); fr2.position.set(x, 3.6, 10.8); g.add(fr2); const pic = box(1.8, 1.2, 0.06, lam(col), false); pic.position.set(x, 3.6, 10.76); g.add(pic); }
  const ceil = box(22, 0.3, 22, lam("#f4ecd8")); ceil.position.set(0, 7.1, 4); ceil.userData.nc = 1; g.add(ceil);
  for (let i = -2; i <= 2; i++) { const beam = box(0.35, 0.35, 22, wood); beam.position.set(i * 3.4, 6.85, 4); beam.userData.nc = 1; g.add(beam); }
  // cửa sổ vòm bên trái (ánh nắng chiếu vào) + rèm đỏ
  for (let k = 0; k < 3; k++) { const z = -1.5 + k * 3.6;
    const pane = new THREE.Mesh(new THREE.PlaneGeometry(1.6, 2.8), glow(1.9, 1.8, 1.45)); pane.position.set(-7.84, 3.3, z); pane.rotation.y = Math.PI / 2; g.add(pane);
    const arch = new THREE.Mesh(new THREE.CircleGeometry(0.8, 16, 0, Math.PI), glow(1.9, 1.8, 1.45)); arch.position.set(-7.84, 4.7, z); arch.rotation.y = Math.PI / 2; g.add(arch);
    const tree = new THREE.Mesh(new THREE.CircleGeometry(0.55, 12), glow(0.5, 0.95, 0.45)); tree.position.set(-7.83, 2.6, z + 0.3); tree.rotation.y = Math.PI / 2; g.add(tree);
    for (const s of [-1, 1]) { const cur = box(0.12, 3.8, 0.55, lam("#9b1c26")); cur.position.set(-7.7, 3.4, z + s * 1.05); cur.userData.nc = 1; g.add(cur); const tie = box(0.14, 0.12, 0.6, lam("#d9b04a")); tie.position.set(-7.66, 2.4, z + s * 1.05); g.add(tie); } }
  // bảng đen khung mạ vàng (canvas để viết phấn)
  const [bc, bg] = cvs(1024, 512); const bt = ctex(bc);
  const board = new THREE.Mesh(new THREE.PlaneGeometry(6.4, 3.2), new THREE.MeshLambertMaterial({ map: bt })); board.position.set(0, 3.4, -4.33); board.receiveShadow = true; g.add(board);
  const fr = lam("#c9a24a"); for (const [w, h, x, y] of [[6.8, 0.2, 0, 5.1], [6.8, 0.2, 0, 1.7], [0.2, 3.6, -3.3, 3.4], [0.2, 3.6, 3.3, 3.4]] as number[][]) { const b = box(w, h, 0.14, fr); b.position.set(x, y, -4.28); g.add(b); }
  const ledge = box(6.6, 0.08, 0.25, wood); ledge.position.set(0, 1.62, -4.18); g.add(ledge);
  // bàn thầy + bình sứ cắm hoa + sách
  const desk = box(2.4, 0.9, 1, wood); desk.position.set(3.6, 0.45, -2.6); g.add(desk);
  const vase = cyl(0.12, 0.2, 0.5, lam("#e9eef5"), 14); vase.position.set(4.3, 1.15, -2.6); g.add(vase); const band = cyl(0.205, 0.205, 0.1, lam("#2b4f8a"), 14); band.position.set(4.3, 1.1, -2.6); g.add(band);
  for (let k = 0; k < 7; k++) { const fl = new THREE.Mesh(new THREE.SphereGeometry(0.1, 8, 6), lam(["#e74c6f", "#f2d36b", "#ffffff"][k % 3])); fl.position.set(4.3 + (r() - 0.5) * 0.4, 1.55 + r() * 0.25, -2.6 + (r() - 0.5) * 0.3); g.add(fl); }
  for (let k = 0; k < 3; k++) { const b = box(0.5, 0.08, 0.35, lam(["#7a2a2a", "#2a4a6a", "#3a5a2a"][k])); b.position.set(3.0, 0.94 + k * 0.08, -2.5); g.add(b); }
  // tủ sách bên phải
  for (let k = 0; k < 2; k++) { const sh2 = box(0.5, 4, 2.4, wood); sh2.position.set(7.5, 2, -1.5 + k * 3.2); g.add(sh2);
    for (let row = 0; row < 4; row++) for (let b = 0; b < 8; b++) { const bk = box(0.1, 0.55, 0.22, lam(["#8e1d24", "#2b4f8a", "#3f6b3a", "#c9a24a", "#4a2a5a"][(b + row) % 5]), false); bk.position.set(7.22, 0.6 + row * 0.95, -1.5 + k * 3.2 - 0.95 + b * 0.25); g.add(bk); } }
  // bàn ghế học trò bọc nhung
  for (const [x, z] of Object.values(LOP_SEATS)) { const d = box(1.5, 0.08, 0.75, wood); d.position.set(x, 0.78, z - 0.65); g.add(d); for (const sx of [-0.65, 0.65]) { const l = box(0.08, 0.78, 0.6, wood); l.position.set(x + sx, 0.39, z - 0.65); g.add(l); }
    const bk = box(0.4, 0.05, 0.3, lam("#f4ecd8")); bk.position.set(x - 0.3, 0.84, z - 0.6); g.add(bk);
    const seat = box(0.55, 0.12, 0.5, lam("#8e1d24")); seat.position.set(x, 0.47, z + 0.05); g.add(seat); const back2 = box(0.55, 0.7, 0.08, lam("#8e1d24")); back2.position.set(x, 0.85, z + 0.33); g.add(back2);
    for (const sx of [-0.22, 0.22]) for (const sz of [-0.18, 0.28]) { const l = cyl(0.03, 0.03, 0.42, wood, 5); l.position.set(x + sx, 0.21, z + sz); g.add(l); } }
  // đèn chùm
  for (const z of [0.2, 4.6]) { const ch = new THREE.Group(); const rod = cyl(0.03, 0.03, 1.2, lam("#c9a24a"), 6); rod.position.y = 6.3; ch.add(rod); const ring = new THREE.Mesh(new THREE.TorusGeometry(0.8, 0.05, 6, 24), lam("#c9a24a")); ring.rotation.x = Math.PI / 2; ring.position.y = 5.7; ch.add(ring);
    for (let k = 0; k < 8; k++) { const a = k / 8 * Math.PI * 2; const b = new THREE.Mesh(new THREE.SphereGeometry(0.09, 8, 6), glow(2.6, 2.1, 1.3)); b.position.set(Math.cos(a) * 0.8, 5.85, Math.sin(a) * 0.8); ch.add(b); } ch.position.z = z; g.add(ch); }
  const pl = new THREE.PointLight("#ffd9a0", 6, 14, 1.6); pl.position.set(0, 5.4, 2); g.add(pl);
  const b2: Board = { c: bc, g: bg, t: bt, last: "" };
  return { g: sh(g), board: b2 };
}
export function drawBoard(B: Board, lines: string[], prog = 1) {
  const key = lines.join("|") + "@" + Math.round(prog * 40); if (B.last === key) return; B.last = key;
  const g = B.g, W = B.c.width, H = B.c.height; const gr = g.createLinearGradient(0, 0, W, H); gr.addColorStop(0, "#22392c"); gr.addColorStop(1, "#1a2e24"); g.fillStyle = gr; g.fillRect(0, 0, W, H);
  g.fillStyle = "rgba(255,255,255,.05)"; for (let i = 0; i < 30; i++) g.fillRect((i * 173) % W, (i * 97) % H, 120, 3);
  const n = lines.length, fs = n <= 1 ? 120 : n <= 3 ? 86 : n <= 5 ? 62 : 50; g.font = `800 ${fs}px ${F}`; g.textAlign = "center"; g.textBaseline = "middle"; g.fillStyle = "#f4f1e6";
  const total = lines.reduce((a, l) => a + l.length, 0); let budget = Math.ceil(total * prog);
  lines.forEach((l, i) => { const y = H / 2 + (i - (n - 1) / 2) * fs * 1.22; const s = l.slice(0, Math.max(0, budget)); budget -= l.length; g.fillText(s, W / 2, y, W - 60); });
  B.t.needsUpdate = true;
}

// ---------- NƯỚC TẦN: núi khô cằn phía tây, đoàn quân áo đen, cửa ải ----------
export function buildTan() {
  const g = new THREE.Group(), r = rng(11); g.add(ground("#a88a5e"));
  for (let i = 0; i < 26; i++) { const a = r() * Math.PI * 2, d = 40 + r() * 90; const p = peak(10 + r() * 14, 16 + r() * 26, ["#8a6a48", "#7a5e40", "#9a7a52", "#6e5438"][i % 4], d > 100 ? "#efe9dc" : undefined); p.position.set(Math.cos(a) * d, -1, Math.sin(a) * d - 20); g.add(p); }
  for (let i = 0; i < 12; i++) { const h = hillM(6 + r() * 6, ["#9a7a52", "#a8865a"][i % 2], 1.4, 0.45, 1); h.position.set(-40 + r() * 80, 0, -30 + r() * 20); g.add(h); }
  const road = box(4, 0.04, 140, lam("#c2a576"), false); road.position.set(0, 0.02, -20); g.add(road);
  // cửa ải: hai tường thành + lầu
  for (const s of [-1, 1]) { const w = box(18, 6, 3, lam("#8d7a62")); w.position.set(s * 11, 3, -40); g.add(w); for (let k = 0; k < 8; k++) { const m = box(1, 0.8, 3.1, lam("#7d6a52")); m.position.set(s * (3 + k * 2.2), 6.4, -40); g.add(m); } }
  const gate = box(4, 2, 3, lam("#7d6a52")); gate.position.set(0, 5, -40); g.add(gate);
  const tw = pagoda(6, 3, 1, "#2a2a2a", "#1d1d1d"); tw.position.set(0, 6, -40); tw.scale.setScalar(0.8); g.add(tw);
  // đoàn quân áo đen + cờ đen
  for (let row = 0; row < 14; row++) for (let c = 0; c < 6; c++) { const s = extra("#1b1b1f", "#d9b08a", true, "#2a2a2a"); s.position.set(-1.6 + c * 0.65 + (r() - 0.5) * 0.1, 0, -6 - row * 1.1); g.add(s); }
  for (let k = 0; k < 6; k++) { const b = banner("#121214", 4.5, "秦"); b.position.set(k % 2 ? 2.4 : -2.6, 0, -8 - k * 3.2); g.add(b); }
  for (let k = 0; k < 8; k++) { const t = treeV(r, "bui"); t.position.set(-12 + r() * 24, 0, -2 - r() * 20); t.position.x += t.position.x > 0 ? 3 : -3; g.add(t); }
  return { g: sh(g) };
}
// ---------- NƯỚC SỞ: cung điện bên sông, đèn lồng, tiệc ----------
export function buildSo() {
  const g = new THREE.Group(), r = rng(13); g.add(water("#3f7a8a", -0.3)); const land = box(120, 1, 40, lam("#5e9a4a")); land.position.set(0, 0.2, -18); g.add(land);
  const pal = pagoda(14, 8, 3); pal.position.set(0, 0.7, -22); g.add(pal);
  for (const s of [-1, 1]) { const p2 = pagoda(7, 5, 2, "#b8322c", "#2f4a3a"); p2.position.set(s * 16, 0.7, -20); g.add(p2); }
  for (let k = 0; k < 18; k++) { const l = lantern(); l.position.set(-14 + k * 1.65, 4.2 + Math.sin(k) * 0.2, -11); g.add(l); }
  const cord = box(30, 0.03, 0.03, lam("#3a2a20"), false); cord.position.set(0, 4.5, -11); g.add(cord);
  for (let k = 0; k < 4; k++) { const t = box(3, 0.8, 1.2, lam("#8e1d24")); t.position.set(-6 + k * 4, 1.1, -7); g.add(t);
    for (let j = 0; j < 4; j++) { const d = cyl(0.18, 0.12, 0.1, lam(["#f2d36b", "#e9eef5"][j % 2]), 10); d.position.set(-7 + k * 4 + j * 0.6, 1.55, -7); g.add(d); }
    for (const s of [-1, 1]) { const e = extra(["#c0392b", "#8e44ad", "#d35400", "#2980b9"][k], "#f1cfa8", false, "#2a1d14"); e.position.set(-6 + k * 4 + s * 0.8, 0.7, -7 + s * 1.1); e.rotation.y = s > 0 ? Math.PI : 0; g.add(e); } }
  for (let k = 0; k < 16; k++) { const t = treeV(r, k % 3 ? "bang" : "sau"); t.position.set(-50 + k * 6.5 + r() * 2, 0.7, -4 - r() * 6); if (Math.abs(t.position.x) < 12) t.position.z -= 30; g.add(t); }
  for (let k = 0; k < 4; k++) { const b = boatHull(5, "#7a4a2a"); b.position.set(-20 + k * 12, -0.3, 4 + (k % 2) * 6); b.rotation.y = 0.2 * k; const rf = cyl(0.6, 0.6, 1.6, lam("#3b2a1e"), 10); rf.rotation.z = Math.PI / 2; rf.scale.y = 1; rf.position.set(0, 0.6, 0); b.add(rf); g.add(b); }
  for (let i = 0; i < 6; i++) { const h = hillM(30, "#5d7f6a", 1.6, 0.35, 0.6); h.position.set(-120 + i * 50, -1, -90); g.add(h); }
  return { g: sh(g) };
}
// ---------- SA MẠC BẮC PHI: lều học giả, đèn dầu, du mục, thành giàu xa xa ----------
export function buildSa() {
  const g = new THREE.Group(), r = rng(17); g.add(ground("#e3c48a"));
  for (let i = 0; i < 30; i++) { const d = hillM(8 + r() * 14, ["#e8c98e", "#d9b678", "#efd29c"][i % 3], 2, 0.22, 1); d.position.set(-120 + r() * 240, 0, -20 - r() * 120); g.add(d); }
  // lều học giả
  const tent = new THREE.Mesh(new THREE.ConeGeometry(3, 2.6, 4, 1, true), lam("#a8502e")); (tent.material as THREE.Material).side = THREE.DoubleSide; tent.rotation.y = Math.PI / 4; tent.position.set(-0.6, 1.3, -3.4); tent.scale.set(1.1, 1, 0.9); g.add(tent);
  const rugT = box(3, 0.03, 2.2, lam("#8e1d24")); rugT.position.set(0, 0.02, 0.4); g.add(rugT);
  const desk = box(0.9, 0.35, 0.5, lam("#6a4a32")); desk.position.set(0.6, 0.18, 0.2); g.add(desk);
  const paper = box(0.5, 0.01, 0.36, lam("#f3ead2")); paper.position.set(0.6, 0.37, 0.2); g.add(paper);
  const lamp = new THREE.Mesh(new THREE.SphereGeometry(0.08, 8, 6), glow(3, 2, 0.8)); lamp.position.set(0.95, 0.5, 0.15); g.add(lamp); const pl = new THREE.PointLight("#ffb060", 4, 6, 1.5); pl.position.set(0.95, 0.8, 0.4); g.add(pl);
  // du mục: lều, lạc đà
  for (let k = 0; k < 7; k++) { const t = new THREE.Mesh(new THREE.ConeGeometry(1.6, 1.8, 6), lam(["#6b4a2e", "#8a6a48", "#4a3426"][k % 3])); t.position.set(-18 + k * 2.6 + r(), 0.9, -10 - r() * 6); g.add(t); }
  for (let k = 0; k < 4; k++) { const c = new THREE.Group(); const body = new THREE.Mesh(new THREE.SphereGeometry(0.7, 10, 8), lam("#c49a62")); body.scale.set(1.5, 0.8, 0.7); body.position.y = 1.7; c.add(body); const hump = new THREE.Mesh(new THREE.SphereGeometry(0.45, 8, 6), lam("#c49a62")); hump.position.set(0, 2.2, 0); c.add(hump);
    const neck = cyl(0.15, 0.2, 1.1, lam("#c49a62"), 6); neck.position.set(1, 2.2, 0); neck.rotation.z = -0.6; c.add(neck); const head = box(0.5, 0.25, 0.25, lam("#c49a62")); head.position.set(1.45, 2.7, 0); c.add(head);
    for (const [x, z] of [[-0.6, -0.2], [-0.6, 0.2], [0.6, -0.2], [0.6, 0.2]]) { const l = cyl(0.08, 0.08, 1.4, lam("#b48a52"), 5); l.position.set(x, 0.7, z); c.add(l); } c.position.set(-8 + k * 3.5, 0, -6 - (k % 2) * 2); c.rotation.y = r(); g.add(sh(c)); }
  for (let k = 0; k < 6; k++) { const p = palm(r); p.position.set(6 + r() * 10, 0, -4 - r() * 8); g.add(p); }
  // thành phố giàu xa xa: tường + mái vòm + tháp
  const cityW = box(60, 5, 2, lam("#d8c49e")); cityW.position.set(10, 2.5, -70); g.add(cityW);
  for (let k = 0; k < 9; k++) { const h2 = house(5, 4 + r() * 5, 5, "#e9dcc0", "#e9dcc0", true); h2.position.set(-14 + k * 6, 0, -76); g.add(h2); }
  for (let k = 0; k < 3; k++) { const dm = new THREE.Mesh(new THREE.SphereGeometry(3, 16, 8, 0, Math.PI * 2, 0, Math.PI / 2), lam(["#2f8a8a", "#c9a24a", "#2f8a8a"][k])); dm.position.set(-4 + k * 14, 8, -76); g.add(dm); const mn = cyl(0.6, 0.8, 14, lam("#e9dcc0"), 8); mn.position.set(3 + k * 14, 7, -74); g.add(mn); }
  return { g: sh(g) };
}
// ---------- HY LẠP: A-ten trên đồi, đền cột, biển và thuyền chiến; Macedonia núi phía bắc ----------
export function buildAthens() {
  const g = new THREE.Group(), r = rng(19); g.add(water("#2f78a8", -0.4, 800, 40));
  const isl = hillM(40, "#b8a77a", 1.2, 0.45, 1); isl.position.set(0, -0.4, -30); g.add(isl);
  const acro = box(26, 3, 18, lam("#c8b48a")); acro.position.set(0, 16.5, -32); g.add(acro);
  const tp = temple(8, 5, 4.2); tp.position.set(0, 18, -33); g.add(tp);
  const tp2 = temple(5, 3, 3); tp2.position.set(9, 18, -27); tp2.rotation.y = 0.4; g.add(tp2);
  for (let i = 0; i < 70; i++) { const a = r() * Math.PI * 2, d = 12 + r() * 26; const x = Math.cos(a) * d, z = -30 + Math.sin(a) * d * 0.8; const y = Math.max(0, 18 * (1 - (d / 40) ** 1.6)) - 0.4; if (z > -5 && Math.abs(x) < 6) continue;
    const h = house(1.8 + r(), 1.4 + r() * 0.8, 1.8 + r(), "#f4efe4", ["#c8552f", "#d26a3a", "#b8452f"][i % 3]); h.position.set(x, y, z); h.rotation.y = r() * 3; g.add(h); }
  for (let i = 0; i < 20; i++) { const t = treeV(r, "bui"); t.scale.setScalar(1.6); const a = r() * 6.28, d = 20 + r() * 18; t.position.set(Math.cos(a) * d, Math.max(0, 18 * (1 - (d / 40) ** 1.6)) - 0.3, -30 + Math.sin(a) * d * 0.8); g.add(t); }
  for (let k = 0; k < 7; k++) { const b = boatHull(7, "#4a3426", 6); const s1 = sail(2.4, 2.6, "#f2ead6"); s1.position.set(0, 2.2, 0); s1.rotation.y = Math.PI / 2; const m = cyl(0.06, 0.06, 3.6, lam("#3a2a20"), 5); m.position.y = 1.9; b.add(m, s1); b.position.set(-30 + k * 9, -0.3, 22 + (k % 3) * 7); b.rotation.y = 0.3; g.add(b); }
  // núi Macedonia phía bắc
  for (let i = 0; i < 10; i++) { const p = peak(16 + r() * 10, 30 + r() * 20, "#6e7a5a", "#eef0f2"); p.position.set(-160 + i * 34, -1, -170); g.add(p); }
  return { g: sh(g) };
}
// ---------- LƯỠNG HÀ: thành Uruk, tháp ziggurat, chợ bên sông, thuyền sậy ----------
export function buildUruk() {
  const g = new THREE.Group(), r = rng(23); g.add(ground("#cdb184")); const riv = water("#5a8a8a", 0.02, 1, 1); riv.scale.set(18, 300, 1); riv.position.set(-16, 0.03, 0); g.add(riv);
  for (let i = 0; i < 4; i++) { const w = 22 - i * 4.5; const st = box(w, 2.4, w, lam(["#b8955e", "#c4a06a", "#b08a54", "#caa86f"][i])); st.position.set(8, 1.2 + i * 2.4, -30); g.add(st); }
  const ramp = box(3, 0.3, 16, lam("#a8854f")); ramp.position.set(8, 4.6, -19); ramp.rotation.x = 0.55; g.add(ramp);
  const shrine = box(5, 2.6, 5, lam("#e9e1d0")); shrine.position.set(8, 10.9, -30); g.add(shrine); const sh3 = box(5.2, 0.4, 5.2, lam("#2f6f8a")); sh3.position.set(8, 12.3, -30); g.add(sh3);
  for (let i = 0; i < 40; i++) { const h = house(2.4 + r() * 2, 2 + r() * 1.5, 2.4 + r() * 2, ["#c9a978", "#d4b688", "#bf9c68"][i % 3], "#a8854f", true); h.position.set(-6 + r() * 40, 0, -50 + r() * 30); if (Math.abs(h.position.x - 8) < 13 && Math.abs(h.position.z + 30) < 13) continue; h.rotation.y = r() * 0.3; g.add(h); }
  // chợ: sạp + mái vải + chum + người
  for (let k = 0; k < 8; k++) { const s = new THREE.Group(); const t = box(1.8, 0.8, 1, lam("#8a6a48")); t.position.y = 0.4; s.add(t); for (const sx of [-0.85, 0.85]) { const p = cyl(0.05, 0.05, 2.2, lam("#5a3b2a"), 5); p.position.set(sx, 1.1, -0.45); s.add(p); }
    const aw = box(2.2, 0.05, 1.5, lam(["#c0392b", "#e0a22a", "#2f8a6a", "#f2ead6"][k % 4])); aw.position.set(0, 2.2, 0); aw.rotation.x = 0.25; s.add(aw);
    for (let j = 0; j < 3; j++) { const p = new THREE.Mesh(new THREE.SphereGeometry(0.2, 8, 6), lam(["#c8552f", "#e0b04a", "#7aa83a"][j])); p.position.set(-0.5 + j * 0.5, 0.9, 0); s.add(p); }
    const jar = cyl(0.2, 0.28, 0.6, lam("#a85a3a"), 10); jar.position.set(1.2, 0.3, 0.3); s.add(jar);
    s.position.set(-4 + (k % 4) * 3.4, 0, -4 - Math.floor(k / 4) * 4); g.add(sh(s));
    const e = extra(["#d8c7a8", "#8a6a48", "#c0392b", "#2f6f8a"][k % 4], "#c98a5a"); e.position.set(-4 + (k % 4) * 3.4 + 0.3, 0, -2.8 - Math.floor(k / 4) * 4); g.add(e); }
  for (let k = 0; k < 5; k++) { const b = boatHull(4, "#c9b06a"); b.position.set(-16 + (r() - 0.5) * 8, 0.05, -10 + k * 9); b.rotation.y = Math.PI / 2 + (r() - 0.5) * 0.4; g.add(b); }
  for (let k = 0; k < 18; k++) { const p = palm(r); p.position.set(-7 - r() * 4, 0, -60 + k * 6); if (k % 2) p.position.x = -25 - r() * 4; g.add(p); }
  for (let i = 0; i < 6; i++) { const p = peak(20, 22, "#7a6a58"); p.position.set(60 + i * 30, -1, -150); g.add(p); }
  return { g: sh(g) };
}
// ---------- TENOCHTITLAN: thành phố trên hồ, kim tự tháp bậc, ruộng nổi; tàu Tây Ban Nha cập bờ ----------
export function buildTenoch() {
  const g = new THREE.Group(), r = rng(29); g.add(water("#3f8a8a", -0.3, 800, 40));
  const isl = box(60, 0.6, 50, lam("#9a8a6a")); isl.position.set(0, 0, -40); g.add(isl);
  const py = new THREE.Group(); for (let i = 0; i < 5; i++) { const w = 18 - i * 3; const st = box(w, 2, w, lam(["#e2d8c4", "#d8ccb4"][i % 2])); st.position.y = 1 + i * 2; py.add(st); }
  const stair = box(3, 0.2, 12, lam("#c8b89c")); stair.position.set(0, 5, 7); stair.rotation.x = -0.7; py.add(stair);
  for (const s of [-1, 1]) { const t = box(3, 3, 3, lam(s > 0 ? "#2f6f8a" : "#b8322c")); t.position.set(s * 2.4, 11.5, 0); py.add(t); const rf = box(3.2, 0.3, 3.2, lam("#f2ead6")); rf.position.set(s * 2.4, 13.1, 0); py.add(rf); }
  py.position.set(0, 0.3, -42); g.add(sh(py));
  for (let i = 0; i < 60; i++) { const h = house(2 + r() * 1.6, 1.6 + r(), 2 + r() * 1.6, "#f2ead6", "#c8b89c", true); h.position.set(-27 + r() * 54, 0.3, -63 + r() * 44); if (Math.abs(h.position.x) < 11 && Math.abs(h.position.z + 42) < 11) continue; g.add(h); }
  for (let i = 0; i < 24; i++) { const c = box(5, 0.25, 2.5, lam(["#5e9a4a", "#7aa83a", "#4f8a3a"][i % 3])); c.position.set(-40 + (i % 8) * 6, -0.15, -6 + Math.floor(i / 8) * 4); g.add(c); if (i % 2) { const t = treeV(r, "bui"); t.position.set(c.position.x + 1.5, 0, c.position.z); g.add(t); } }
  for (const [x, z, L, ry] of [[0, 30, 60, 0], [-50, -40, 40, Math.PI / 2]] as number[][]) { const cw = box(4, 0.4, L, lam("#b8a57e")); cw.position.set(x, 0, z - (ry ? 0 : 0)); cw.rotation.y = ry; g.add(cw); }
  for (let k = 0; k < 8; k++) { const b = boatHull(3, "#6a4a32"); b.position.set(-30 + k * 8, -0.25, 8 + (k % 3) * 4); b.rotation.y = r() * 3; g.add(b); }
  for (let i = 0; i < 9; i++) { const p = peak(26 + r() * 10, 34 + r() * 26, "#5e6e5a", i % 3 === 0 ? "#f4f4f4" : undefined); p.position.set(-200 + i * 50, -1, -200); g.add(p); }
  // bờ biển và tàu Tây Ban Nha (đặt xa về phía +x để quay riêng)
  const beach = box(60, 0.5, 30, lam("#e3cf9a")); beach.position.set(140, 0, 0); g.add(beach);
  for (let k = 0; k < 4; k++) { const sh4 = galleon(); sh4.position.set(126 + k * 9, -0.4, 26 + (k % 2) * 6); sh4.rotation.y = 0.15 * k; g.add(sh4); }
  for (let row = 0; row < 6; row++) for (let c = 0; c < 10; c++) { const s = extra("#8a8f96", "#e9c29a", c % 3 === 0, "#c9ced4"); s.position.set(132 + c * 0.8, 0.25, 10 - row * 1.0); g.add(s); }
  for (let k = 0; k < 10; k++) { const p = palm(r); p.position.set(118 + r() * 40, 0.25, -10 - r() * 12); g.add(p); }
  return { g: sh(g) };
}
// ---------- THẢO NGUYÊN MÔNG CỔ: đồi cỏ, lều tròn, ngựa, thủ lĩnh trên đồi ----------
export function buildThao() {
  const g = new THREE.Group(), r = rng(31); g.add(ground("#7aa84a"));
  for (let i = 0; i < 24; i++) { const h = hillM(14 + r() * 20, ["#8ab858", "#6e9a42", "#9cc464"][i % 3], 2, 0.25, 1.2); h.position.set(-160 + r() * 320, 0, -30 - r() * 150); g.add(h); }
  const hill = hillM(12, "#86b454", 1.4, 0.45, 1); hill.position.set(0, 0, -16); g.add(hill);
  for (let k = 0; k < 12; k++) { const y = new THREE.Group(); const w = cyl(1.4, 1.4, 1.3, lam("#f2ead6"), 16); w.position.y = 0.65; y.add(w); const rf = new THREE.Mesh(new THREE.ConeGeometry(1.55, 0.9, 16), lam("#e4d6b8")); rf.position.y = 1.75; y.add(rf);
    const bd = cyl(1.42, 1.42, 0.15, lam(["#c0392b", "#2b4f8a"][k % 2]), 16); bd.position.y = 1.0; y.add(bd); y.position.set(-26 + (k % 6) * 5 + r(), 0, 2 - Math.floor(k / 6) * 7); g.add(sh(y)); }
  const horse = (col: string) => { const h = new THREE.Group(); const b = new THREE.Mesh(new THREE.CapsuleGeometry(0.4, 1.1, 4, 8), lam(col)); b.rotation.z = Math.PI / 2; b.position.y = 1.2; h.add(b);
    const n = cyl(0.17, 0.24, 0.9, lam(col), 6); n.position.set(0.75, 1.65, 0); n.rotation.z = -0.7; h.add(n); const hd = box(0.6, 0.25, 0.25, lam(col)); hd.position.set(1.1, 1.95, 0); hd.rotation.z = -0.3; h.add(hd);
    for (const [x, z] of [[-0.5, -0.18], [-0.5, 0.18], [0.5, -0.18], [0.5, 0.18]]) { const l = cyl(0.07, 0.06, 0.95, lam(col), 5); l.position.set(x, 0.48, z); h.add(l); } return sh(h); };
  for (let k = 0; k < 20; k++) { const h = horse(["#5a3b2a", "#2a2522", "#8a6a48", "#d8c7a8"][k % 4]); h.position.set(4 + r() * 22, 0, -4 - r() * 14); h.rotation.y = r() * 6; g.add(h);
    if (k % 2) { const rd = extra(["#2b4f8a", "#8e1d24", "#5a6a4a"][k % 3], "#d9a77e", true, "#5a3b2a"); rd.position.set(0, 0.95, 0); rd.scale.setScalar(0.85); h.add(rd); } }
  for (let k = 0; k < 6; k++) { const b = banner(["#8e1d24", "#f2ead6", "#2b4f8a"][k % 3], 5); b.position.set(-4 + k * 1.8, 5.2, -16 + (r() - 0.5) * 2); g.add(b); }
  return { g: sh(g) };
}
// ---------- KHÁCH SẠN PLAZA 1985: phòng họp, bàn dài, 5 lá cờ, cửa sổ thấy phố New York ----------
function flagTex(k: number) { const [c, x] = cvs(192, 128);
  if (k === 0) { for (let i = 0; i < 13; i++) { x.fillStyle = i % 2 ? "#fff" : "#b22234"; x.fillRect(0, i * 128 / 13, 192, 128 / 13 + 1); } x.fillStyle = "#3c3b6e"; x.fillRect(0, 0, 80, 69); x.fillStyle = "#fff"; for (let i = 0; i < 30; i++) x.fillRect(6 + (i % 6) * 12, 5 + Math.floor(i / 6) * 13, 3, 3); }
  else if (k === 1) { x.fillStyle = "#fff"; x.fillRect(0, 0, 192, 128); x.fillStyle = "#bc002d"; x.beginPath(); x.arc(96, 64, 38, 0, 7); x.fill(); }
  else if (k === 2) { x.fillStyle = "#012169"; x.fillRect(0, 0, 192, 128); x.strokeStyle = "#fff"; x.lineWidth = 22; x.beginPath(); x.moveTo(0, 0); x.lineTo(192, 128); x.moveTo(192, 0); x.lineTo(0, 128); x.stroke(); x.strokeStyle = "#c8102e"; x.lineWidth = 8; x.stroke(); x.fillStyle = "#fff"; x.fillRect(80, 0, 32, 128); x.fillRect(0, 48, 192, 32); x.fillStyle = "#c8102e"; x.fillRect(86, 0, 20, 128); x.fillRect(0, 54, 192, 20); }
  else if (k === 3) { ["#002395", "#fff", "#ed2939"].forEach((col, i) => { x.fillStyle = col; x.fillRect(i * 64, 0, 64, 128); }); }
  else { ["#000", "#dd0000", "#ffce00"].forEach((col, i) => { x.fillStyle = col; x.fillRect(0, i * 128 / 3, 192, 128 / 3 + 1); }); }
  return ctex(c); }
export function buildPlaza() {
  const g = new THREE.Group(); const fl = box(20, 0.1, 16, lam("#7a2a2a")); fl.position.y = -0.05; g.add(fl);
  const wallM = lam("#e9dcc0"); const bw = box(20, 6, 0.3, wallM); bw.position.set(0, 3, -6); bw.userData.nc = 1; g.add(bw); for (const s of [-1, 1]) { const sw = box(0.3, 6, 16, wallM); sw.position.set(s * 10, 3, 2); sw.userData.nc = 1; g.add(sw); }
  for (let k = 0; k < 3; k++) { const w = new THREE.Mesh(new THREE.PlaneGeometry(2.4, 3.4), glow(0.9, 1.1, 1.5)); w.position.set(9.83, 3.2, -3 + k * 3.6); w.rotation.y = -Math.PI / 2; g.add(w);
    for (let b = 0; b < 5; b++) { const t = box(0.02, 0.6 + (b * 37 % 5) * 0.4, 0.35, lam("#3a4a6a"), false); t.position.set(9.82, 1.6 + (0.6 + (b * 37 % 5) * 0.4) / 2, -4 + k * 3.6 + b * 0.45); g.add(t); } }
  const table = box(9, 0.12, 2.4, lam("#3a2416")); table.position.set(0, 0.95, 0); g.add(table); const cloth = box(9.2, 0.02, 2.6, lam("#2f5a3a")); cloth.position.set(0, 1.02, 0); g.add(cloth);
  for (const sx of [-4, 4]) for (const sz of [-1, 1]) { const l = box(0.15, 0.9, 0.15, lam("#3a2416")); l.position.set(sx, 0.45, sz * 1); g.add(l); }
  for (let k = 0; k < 5; k++) { const x = -3.6 + k * 1.8; for (const s of [-1, 1]) { const ch = box(0.6, 1.1, 0.6, lam("#5a2e1c")); ch.position.set(x, 0.55, s * 1.7); g.add(ch); }
    const plate = box(0.4, 0.03, 0.3, lam("#f4f1e6")); plate.position.set(x, 1.05, -0.6); g.add(plate); const mic = cyl(0.02, 0.02, 0.35, lam("#222"), 5); mic.position.set(x + 0.3, 1.2, -0.7); g.add(mic);
    const fg = new THREE.Mesh(new THREE.PlaneGeometry(0.4, 0.27), new THREE.MeshLambertMaterial({ map: flagTex(k), side: THREE.DoubleSide })); fg.position.set(x, 1.32, 0); g.add(fg); const st = cyl(0.01, 0.01, 0.35, lam("#c9a24a"), 4); st.position.set(x - 0.21, 1.2, 0); g.add(st); }
  for (let k = 0; k < 5; k++) { const p = cyl(0.04, 0.04, 3.4, lam("#c9a24a"), 6); p.position.set(-4 + k * 2, 1.7, -5.4); g.add(p);
    const fg = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 1), new THREE.MeshLambertMaterial({ map: flagTex(k), side: THREE.DoubleSide })); fg.position.set(-4 + k * 2 + 0.78, 2.8, -5.4); g.add(fg); }
  for (const x of [-4, 4]) { const ch = new THREE.Group(); for (let k = 0; k < 10; k++) { const a = k / 10 * Math.PI * 2; const b = new THREE.Mesh(new THREE.SphereGeometry(0.08, 8, 6), glow(2.6, 2.2, 1.5)); b.position.set(Math.cos(a) * 0.7, 0, Math.sin(a) * 0.7); ch.add(b); } ch.position.set(x, 5.2, 0); g.add(ch); }
  const pl = new THREE.PointLight("#ffe2b0", 5, 14, 1.6); pl.position.set(0, 4.8, 0); g.add(pl);
  return { g: sh(g) };
}
// ---------- HỘI THẢO GIÁO VIÊN: 10 bàn, ô tô đồ chơi, máy bay giấy, máy bắn đá, bảng xếp hạng ----------
export function buildXuong() {
  const g = new THREE.Group(), r = rng(37); const fl = box(30, 0.1, 22, lam("#c9c2b4")); fl.position.y = -0.05; g.add(fl);
  const bw = box(30, 6, 0.3, lam("#dfe6ea")); bw.position.set(0, 3, -9); bw.userData.nc = 1; g.add(bw); for (const s of [-1, 1]) { const sw = box(0.3, 6, 22, lam("#dfe6ea")); sw.position.set(s * 15, 3, 2); sw.userData.nc = 1; g.add(sw); }
  for (let k = 0; k < 4; k++) { const w = new THREE.Mesh(new THREE.PlaneGeometry(3, 2.4), glow(1.5, 1.6, 1.7)); w.position.set(-14.83, 3.4, -6 + k * 5); w.rotation.y = Math.PI / 2; g.add(w); }
  const [sc, sx] = cvs(1024, 512); const st = ctex(sc); const scb = new THREE.Mesh(new THREE.PlaneGeometry(7, 3.5), new THREE.MeshLambertMaterial({ map: st })); scb.position.set(0, 3.6, -8.82); g.add(scb);
  for (let k = 0; k < 10; k++) { const x = -10 + (k % 5) * 5, z = -4 + Math.floor(k / 5) * 6;
    const t = box(2.6, 0.08, 1.4, lam("#e9dcc0")); t.position.set(x, 0.8, z); g.add(t); for (const a of [-1.2, 1.2]) for (const b of [-0.6, 0.6]) { const l = cyl(0.04, 0.04, 0.8, lam("#888"), 5); l.position.set(x + a, 0.4, z + b); g.add(l); }
    if (k % 3 === 0) { const car = box(0.6, 0.18, 0.3, lam(["#c0392b", "#2980b9", "#f39c12"][k % 3])); car.position.set(x - 0.6, 0.94, z); g.add(car); for (const a of [-0.2, 0.2]) for (const b of [-0.17, 0.17]) { const w = cyl(0.07, 0.07, 0.05, lam("#222"), 10); w.rotation.x = Math.PI / 2; w.position.set(x - 0.6 + a, 0.88, z + b); g.add(w); } }
    else if (k % 3 === 1) { const pl = new THREE.Mesh(new THREE.ConeGeometry(0.2, 0.7, 3), lam("#f4f4f2")); pl.rotation.z = Math.PI / 2; pl.scale.z = 0.3; pl.position.set(x - 0.4, 0.95, z); g.add(pl); }
    else { const base = box(0.6, 0.1, 0.4, lam("#8a6a48")); base.position.set(x - 0.4, 0.89, z); g.add(base); const arm = box(0.05, 0.05, 0.7, lam("#6a4a32")); arm.position.set(x - 0.4, 1.1, z); arm.rotation.x = 0.8; arm.rotation.y = Math.PI / 2; g.add(arm); }
    for (let j = 0; j < 4; j++) { const p = box(0.25, 0.01, 0.35, lam("#f4f1e6")); p.position.set(x + 0.4 + (r() - 0.5) * 0.6, 0.85, z + (r() - 0.5) * 0.6); p.rotation.y = r(); g.add(p); }
    for (const s of [-1, 1]) { const e = extra(["#2b4f8a", "#8e1d24", "#3f6b3a", "#c9a24a", "#6b4fa0"][k % 5], ["#f1cfa8", "#c98a5a", "#e9c29a"][k % 3]); e.position.set(x + s * 0.7, 0, z + 1.1); e.rotation.y = Math.PI; g.add(e); } }
  return { g: sh(g), score: { c: sc, g: sx, t: st, last: "" } as Board };
}
export function drawScore(B: Board, day: 1 | 2) {
  const key = "d" + day; if (B.last === key) return; B.last = key; const g = B.g, W = B.c.width, H = B.c.height;
  g.fillStyle = "#11161f"; g.fillRect(0, 0, W, H); g.fillStyle = "#f5c518"; g.font = `900 46px ${F}`; g.textAlign = "center"; g.fillText(day === 1 ? "BẢNG XẾP HẠNG – NGÀY 1" : "BẢNG XẾP HẠNG – NGÀY 2", W / 2, 60);
  const order = day === 1 ? [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
  g.textAlign = "left"; order.forEach((team, i) => { const col = i % 2, row = Math.floor(i / 2); const x = 60 + col * 480, y = 130 + row * 74;
    g.fillStyle = team === 1 ? "#ff5a5a" : team === 10 ? "#3ddc84" : "#e6ebf0"; g.font = `800 40px ${F}`; g.fillText(`${i + 1}. Đội ${team}`, x, y); });
  B.t.needsUpdate = true;
}
