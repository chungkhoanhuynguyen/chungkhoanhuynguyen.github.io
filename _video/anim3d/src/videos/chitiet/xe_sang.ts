// XE SANG (chuẩn 20/11/2026): 3 siêu xe tự thiết kế + 1 hypercar sang + 1 mô tô sportbike – vật liệu BÓNG (MeshPhysical: sơn kim loại
// phủ bóng clearcoat, carbon đen dệt, crôm, kính tối) phản chiếu môi trường HDRI Poly Haven (CC0), vẫn có viền mực InkPass của xưởng.
// Dáng TỰ THIẾT KẾ, chung chung – KHÔNG chép dáng/logo/tên của hãng thật. Biển số VN giả.
// Thân xe = "loft": quét mặt cắt siêu elip dọc thân (bề ngang, gầm, nóc, độ vuông, độ thu nóc thay đổi theo z) → khối cong liền;
// hốc bánh: điểm thân thấp hơn cung bánh trong vùng bánh bị kéo vào trong (thân dưới hẹp) → bánh nằm dưới vè như xe thật.
// Quy ước: đầu xe +z, bánh chạm y = 0, bên người lái = +x.
import * as THREE from "three";
import { staticFile, delayRender, continueRender } from "remotion";
import { RGBELoader } from "three/examples/jsm/loaders/RGBELoader.js";
import { glow } from "./toonmat";
import { plate } from "./xe";

// ---------- môi trường phản chiếu (HDRI) ----------
const envUsers: THREE.MeshPhysicalMaterial[] = []; let envTex: THREE.Texture | null = null, envReq = false;
function needEnv() { if (envReq) return; envReq = true; const h = delayRender("hdri", { timeoutInMilliseconds: 120000 });
  new RGBELoader().load(staticFile("chitiet/hdri/studio_small_09.hdr"), (t) => { t.mapping = THREE.EquirectangularReflectionMapping; envTex = t; for (const m of envUsers) { m.envMap = t; m.needsUpdate = true; } continueRender(h); }, undefined, () => continueRender(h)); }
function phys(o: THREE.MeshPhysicalMaterialParameters, envI = 1) { needEnv(); const m = new THREE.MeshPhysicalMaterial({ envMapIntensity: envI, ...o }); if (envTex) m.envMap = envTex; envUsers.push(m); return m; }
export const paint = (col: string, o: Partial<THREE.MeshPhysicalMaterialParameters> = {}, envI = 0.75) => phys({ color: col, metalness: 0.35, roughness: 0.35, clearcoat: 1, clearcoatRoughness: 0.04, ...o }, envI);
export const chromeP = () => phys({ color: "#f2f4f6", metalness: 1, roughness: 0.08 }, 1.2);
export const darkGlass = () => phys({ color: "#07090d", metalness: 0.2, roughness: 0.04, clearcoat: 1, clearcoatRoughness: 0.02 }, 1.3);
let carbonTex: THREE.Texture | null = null;
export const carbon = () => { if (!carbonTex) { const c = document.createElement("canvas"); c.width = c.height = 64; const x = c.getContext("2d")!; for (let i = 0; i < 8; i++) for (let j = 0; j < 8; j++) { x.fillStyle = (i + j) % 2 ? "#1d1f24" : "#0c0d10"; x.fillRect(i * 8, j * 8, 8, 8); x.fillStyle = "rgba(255,255,255,.06)"; x.fillRect(i * 8 + ((i + j) % 2 ? 0 : 3), j * 8, 2, 8); }
    carbonTex = new THREE.CanvasTexture(c); carbonTex.wrapS = carbonTex.wrapT = THREE.RepeatWrapping; carbonTex.repeat.set(6, 6); carbonTex.colorSpace = THREE.SRGBColorSpace; }
  return phys({ color: "#ffffff", map: carbonTex, metalness: 0.2, roughness: 0.5, clearcoat: 0.6, clearcoatRoughness: 0.15 }, 0.28); };
const rubberP = () => phys({ color: "#141416", roughness: 0.85, metalness: 0 }, 0.3);
const leather = (col: string) => phys({ color: col, roughness: 0.55, metalness: 0, sheen: 0.4 }, 0.5);
const M = (geo: THREE.BufferGeometry, m: THREE.Material, x = 0, y = 0, z = 0) => { const k = new THREE.Mesh(geo, m); k.position.set(x, y, z); k.castShadow = true; k.receiveShadow = true; return k; };
const B = (w: number, h: number, d: number, m: THREE.Material, x = 0, y = 0, z = 0) => M(new THREE.BoxGeometry(w, h, d), m, x, y, z);
const Cy = (r1: number, r2: number, h: number, m: THREE.Material, x = 0, y = 0, z = 0, s = 24) => M(new THREE.CylinderGeometry(r1, r2, h, s), m, x, y, z);

// ---------- dựng khối loft ----------
type K = [number, number][]; // mốc (z, giá trị)
export const pw = (k: K) => (z: number) => { if (z <= k[0][0]) return k[0][1]; for (let i = 1; i < k.length; i++) if (z <= k[i][0]) { const [z0, a] = k[i - 1], [z1, b] = k[i], t = (z - z0) / (z1 - z0), s = t * t * (3 - 2 * t); return a + (b - a) * s; } return k[k.length - 1][1]; };
export type LoftSpec = { z0: number; z1: number; hw: (z: number) => number; yb: (z: number) => number; yt: (z: number) => number; n?: (z: number) => number; tb?: (z: number) => number; fd?: (z: number) => number;
  arches?: { z: number; y: number; r: number; tub: number }[]; N?: number; Mr?: number };
/** quét mặt cắt siêu elip dọc trục z; arches: khoét hốc bánh (điểm dưới cung bánh trong vùng bánh kéo vào bề ngang tub) */
export function loft(s: LoftSpec) {
  const N = s.N ?? 120, Mr = s.Mr ?? 64, pos: number[] = [], idx: number[] = [];
  for (let i = 0; i <= N; i++) { const z = s.z0 + (s.z1 - s.z0) * (i / N), hw = Math.max(0.005, s.hw(z)), yb = s.yb(z), yt = Math.max(yb + 0.01, s.yt(z)), n = s.n?.(z) ?? 3, tb = s.tb?.(z) ?? 0, fd = s.fd?.(z) ?? 0, ym = (yb + yt) / 2, hh = (yt - yb) / 2;
    for (let j = 0; j < Mr; j++) { const th = (j / Mr) * Math.PI * 2, c = Math.cos(th), sn = Math.sin(th);
      let x = hw * Math.sign(c) * Math.pow(Math.abs(c), 2 / n), y = ym + hh * Math.sign(sn) * Math.pow(Math.abs(sn), 2 / n);
      if (sn > 0) { x *= 1 - tb * Math.pow(sn, 1.5); y += fd * Math.pow(Math.abs(c), 3) * sn; }
      for (const a of s.arches ?? []) { const dz = z - a.z; if (Math.abs(dz) < a.r) { const lim = a.y + Math.sqrt(a.r * a.r - dz * dz); if (y < lim) x = Math.sign(x) * Math.min(Math.abs(x), a.tub); } }
      pos.push(x, y, z); } }
  for (let i = 0; i < N; i++) for (let j = 0; j < Mr; j++) { const a = i * Mr + j, b = i * Mr + ((j + 1) % Mr), c2 = (i + 1) * Mr + j, d = (i + 1) * Mr + ((j + 1) % Mr); idx.push(a, c2, b, b, c2, d); }
  for (const [ring, flip] of [[0, true], [N, false]] as [number, boolean][]) { let cx = 0, cy = 0; for (let j = 0; j < Mr; j++) { cx += pos[(ring * Mr + j) * 3]; cy += pos[(ring * Mr + j) * 3 + 1]; } const ci = pos.length / 3; pos.push(cx / Mr, cy / Mr, pos[ring * Mr * 3 + 2]);
    for (let j = 0; j < Mr; j++) { const a = ring * Mr + j, b = ring * Mr + ((j + 1) % Mr); if (flip) idx.push(ci, a, b); else idx.push(ci, b, a); } }
  const g = new THREE.BufferGeometry(); g.setAttribute("position", new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals(); return g;
}

/** bánh thể thao: lốp mỏng + mâm nhiều chấu kép + đĩa phanh khoan lỗ + kẹp phanh màu */
export function sportWheel(r: number, w: number, spokes = 10, rimCol = "#5b5f66", cal = "#d8212f", chromeRim = false) {
  const g = new THREE.Group(), rimM = chromeRim ? chromeP() : phys({ color: rimCol, metalness: 0.9, roughness: 0.28 }, 1.1);
  const tyre = Cy(r, r, w, rubberP(), 0, 0, 0, 40); tyre.rotation.z = Math.PI / 2; g.add(tyre);
  const wall = M(new THREE.TorusGeometry(r * 0.83, r * 0.07, 10, 40), rubberP()); wall.rotation.y = Math.PI / 2; g.add(wall);
  const disc = Cy(r * 0.6, r * 0.6, 0.03, phys({ color: "#8d9096", metalness: 0.9, roughness: 0.35 }), w * 0.18, 0, 0, 32); disc.rotation.z = Math.PI / 2; g.add(disc);
  g.add(B(0.07, r * 0.32, r * 0.42, phys({ color: cal, metalness: 0.2, roughness: 0.3, clearcoat: 1 }), w * 0.22, r * 0.36, -r * 0.18));
  for (const sx of [1]) { const barrel = Cy(r * 0.76, r * 0.76, 0.04, rimM, sx * (w / 2 - 0.01), 0, 0, 40); barrel.rotation.z = Math.PI / 2; g.add(barrel);
    for (let k = 0; k < spokes; k++) for (const da of [-0.06, 0.06]) { const a = (k / spokes) * Math.PI * 2 + da; const sp = B(0.03, r * 0.62, 0.045, rimM, sx * (w / 2 + 0.01), Math.cos(a) * r * 0.36, Math.sin(a) * r * 0.36); sp.rotation.x = -a; g.add(sp); }
    const hub = Cy(r * 0.13, r * 0.13, 0.05, rimM, sx * (w / 2 + 0.02), 0, 0, 16); hub.rotation.z = Math.PI / 2; g.add(hub); }
  // mặt trong (phía gầm) tối
  const inner = Cy(r * 0.76, r * 0.76, 0.02, phys({ color: "#0c0c0e", roughness: 0.9 }), -w / 2 + 0.02, 0, 0, 24); inner.rotation.z = Math.PI / 2; g.add(inner);
  return g;
}
/** đặt 4 bánh (mặt mâm hướng ra ngoài) + hốc tối */
function wheels(g: THREE.Group, axF: number, axR: number, xF: number, xR: number, rF: number, rR: number, wF: number, wR: number, o: { spokes?: number; rim?: string; cal?: string; chrome?: boolean } = {}) {
  for (const [z, x, r, w] of [[axF, xF, rF, wF], [axR, xR, rR, wR]] as [number, number, number, number][]) for (const sx of [-1, 1]) {
    const wh = sportWheel(r, w, o.spokes, o.rim, o.cal, o.chrome); wh.position.set(sx * x, r, z); if (sx < 0) wh.rotation.y = Math.PI; g.add(wh);
    const well = Cy(r + 0.06, r + 0.06, 0.05, phys({ color: "#060607", roughness: 1 }, 0.05), sx * (x - w / 2 - 0.05), r, z, 28); well.rotation.z = Math.PI / 2; well.castShadow = false; g.add(well); }
}
/** dải LED: chuỗi đoạn thẳng phát sáng nối các điểm (x, y, z) */
function led(g: THREE.Group, pts: [number, number, number][], col: [number, number, number], t = 0.018) { const m = glow(...col);
  for (let i = 0; i < pts.length - 1; i++) { const a = new THREE.Vector3(...pts[i]), b = new THREE.Vector3(...pts[i + 1]), len = a.distanceTo(b); const k = new THREE.Mesh(new THREE.BoxGeometry(t, t, len), m); k.position.copy(a).add(b).multiplyScalar(0.5); k.lookAt(b); g.add(k); } }
const mirror = (g: THREE.Group, x: number, y: number, z: number, m: THREE.Material) => { for (const sx of [-1, 1]) { const st = B(0.03, 0.03, 0.16, carbon(), sx * (x - 0.06), y - 0.04, z + 0.02); st.rotation.y = sx * 0.4; g.add(st); const h = M(new THREE.SphereGeometry(0.08, 16, 10), m, sx * x, y, z); h.scale.set(1.4, 0.75, 0.9); g.add(h); } };
const plates = (g: THREE.Group, text: string, yf: number, zf: number, yr: number, zr: number) => { const a = plate(text); a.position.set(0, yf, zf); g.add(a); const b = plate(text); b.position.set(0, yr, zr); b.rotation.y = Math.PI; g.add(b); };
function seats(g: THREE.Group, col: string, y: number, z: number, sx = 0.38) { const L = leather(col); for (const s of [-1, 1]) { g.add(B(0.46, 0.12, 0.5, L, s * sx, y, z)); const bk = B(0.46, 0.62, 0.12, L, s * sx, y + 0.32, z - 0.28); bk.rotation.x = -0.35; g.add(bk); } }
const wheelSW = (g: THREE.Group, x: number, y: number, z: number) => { const sw = M(new THREE.TorusGeometry(0.16, 0.024, 10, 24), carbon(), x, y, z); sw.rotation.x = -0.45; g.add(sw); };

// ================= 1. SIÊU XE NÊM góc cạnh – xanh rêu ánh tím (sơn đổi màu) =================
export function sieuXeNem(bien = "51K-868.88") {
  const g = new THREE.Group(), L = 4.62, axF = 1.4, axR = -1.36, wr = 0.36, body = paint("#4f6a2a", { metalness: 0.4, roughness: 0.3, iridescence: 0.8, iridescenceIOR: 1.5, iridescenceThicknessRange: [300, 520], sheen: 0.5, sheenColor: new THREE.Color("#8a5ae0") });
  const hw = (z: number) => 1.0 * (0.84 + 0.16 * Math.max(Math.exp(-(((z - axF) / 0.55) ** 2)), Math.exp(-(((z - axR) / 0.6) ** 2)))) * (1 - 0.3 * Math.max(0, (z - 1.9) / 0.4) ** 2) * (1 - 0.06 * Math.max(0, (-z - 1.9) / 0.4));
  const yt = pw([[-2.31, 0.86], [-2.0, 0.98], [-0.9, 1.0], [0.55, 0.82], [1.6, 0.66], [2.31, 0.36]]);
  const yb = pw([[-2.31, 0.3], [-2.0, 0.16], [2.0, 0.13], [2.31, 0.18]]);
  g.add(M(loft({ z0: -L / 2, z1: L / 2, hw, yb, yt, n: () => 5.5, tb: () => 0.18, fd: (z) => 0.16 * Math.exp(-(((z - axF) / 0.5) ** 2)) + 0.12 * Math.exp(-(((z - axR) / 0.55) ** 2)), arches: [{ z: axF, y: wr, r: wr + 0.07, tub: 0.6 }, { z: axR, y: wr, r: wr + 0.08, tub: 0.6 }] }), body));
  // buồng lái nêm (kính tối, cạnh sắc)
  g.add(M(loft({ z0: -0.95, z1: 0.75, hw: (z) => 0.66 * (1 - 0.35 * Math.max(0, (z - 0.2) / 0.55) ** 2), yb: (z) => yt(z) - 0.06, yt: pw([[-0.95, 0.96], [-0.5, 1.13], [0.05, 1.15], [0.75, 0.84]]), n: () => 4, tb: () => 0.42, N: 60 }), darkGlass()));
  // carbon: lưỡi cản trước, ốp sườn, hút gió, khuếch tán sau, cánh gió
  const cb = carbon(); g.add(B(1.5, 0.03, 0.26, cb, 0, 0.12, 2.06)); for (const sx of [-1, 1]) { g.add(B(0.03, 0.07, 1.9, cb, sx * hw(0) * 0.99, 0.2, 0));
    const iz = -0.45, intake = B(0.02, 0.3, 0.75, cb, sx * (hw(iz) + 0.002), 0.56, iz); intake.rotation.x = 0.3; g.add(intake); for (let k = 0; k < 3; k++) g.add(B(0.03, 0.01, 0.6, phys({ color: "#3a3d44", metalness: 0.9, roughness: 0.3 }), sx * (hw(iz) + 0.012), 0.47 + k * 0.08, iz)); }
  g.add(B(1.5, 0.12, 0.22, cb, 0, 0.2, -2.18)); for (let k = -3; k <= 3; k++) g.add(B(0.015, 0.12, 0.24, cb, k * 0.2, 0.2, -2.2));
  const wing = B(1.86, 0.05, 0.36, cb, 0, 1.28, -2.02); wing.rotation.x = 0.1; g.add(wing); for (const sx of [-0.62, 0.62]) { const st = B(0.04, 0.3, 0.16, cb, sx, 1.1, -1.95); st.rotation.x = -0.25; g.add(st); } for (const sx of [-1, 1]) g.add(B(0.03, 0.18, 0.4, cb, sx * 0.94, 1.25, -2.02));
  // đèn LED dải: chữ "Λ" trước, thanh ngang sau + 4 ống xả lục giác giữa
  for (const sx of [-1, 1]) { led(g, [[sx * 0.82, 0.55, 1.98], [sx * 0.5, 0.62, 2.08], [sx * 0.3, 0.5, 2.22]], [2.6, 2.6, 2.8], 0.022); led(g, [[sx * 0.82, 0.48, 1.96], [sx * 0.62, 0.42, 2.06]], [2.6, 2.6, 2.8], 0.016); }
  led(g, [[-0.85, 0.86, -2.29], [0.85, 0.86, -2.29]], [3.0, 0.25, 0.2], 0.035); for (const sx of [-1, 1]) led(g, [[sx * 0.85, 0.86, -2.29], [sx * 0.95, 0.7, -2.22]], [3.0, 0.25, 0.2], 0.03);
  for (const sx of [-0.12, 0.12]) for (const sy of [0.42, 0.52]) { const ex = Cy(0.045, 0.045, 0.12, chromeP(), sx, sy, -2.3, 6); ex.rotation.x = Math.PI / 2; g.add(ex); }
  mirror(g, 0.98, 0.93, 0.45, body); seats(g, "#2a2a2e", 0.42, -0.35, 0.34);
  wheels(g, axF, axR, 0.84, 0.86, wr, wr + 0.01, 0.27, 0.33, { spokes: 10, rim: "#7a7e86", cal: "#7ad83a" });
  plates(g, bien, 0.3, 2.3, 0.55, -2.31);
  return g;
}

// ================= 2. SIÊU XE CONG MƯỢT – xám bạc, cửa cánh chim mở =================
export function sieuXeCanhChim(open = true, bien = "30L-555.68") {
  const g = new THREE.Group(), L = 4.5, axF = 1.38, axR = -1.32, wr = 0.35, body = paint("#b7bbc1", { metalness: 0.9, roughness: 0.22 });
  const hw = (z: number) => 0.99 * (0.82 + 0.18 * Math.max(Math.exp(-(((z - axF) / 0.6) ** 2)), Math.exp(-(((z - axR) / 0.65) ** 2)))) * (1 - 0.35 * Math.max(0, (z - 1.75) / 0.5) ** 2) * (1 - 0.12 * Math.max(0, (-z - 1.8) / 0.45) ** 2);
  const yt = pw([[-2.25, 0.78], [-1.9, 0.95], [-1.0, 0.98], [0.5, 0.8], [1.5, 0.66], [2.25, 0.36]]), yb = pw([[-2.25, 0.3], [-1.9, 0.15], [1.9, 0.14], [2.25, 0.2]]);
  g.add(M(loft({ z0: -L / 2, z1: L / 2, hw, yb, yt, n: () => 2.6, tb: () => 0.22, fd: (z) => 0.14 * Math.exp(-(((z - axF) / 0.55) ** 2)) + 0.13 * Math.exp(-(((z - axR) / 0.6) ** 2)), arches: [{ z: axF, y: wr, r: wr + 0.07, tub: 0.58 }, { z: axR, y: wr, r: wr + 0.08, tub: 0.58 }] }), body));
  const cab = loft({ z0: -1.2, z1: 0.75, hw: (z) => 0.68 * (1 - 0.4 * Math.max(0, (z - 0.1) / 0.65) ** 2) * (1 - 0.25 * Math.max(0, (-z - 0.6) / 0.6) ** 2), yb: (z) => yt(z) - 0.05, yt: pw([[-1.2, 0.95], [-0.6, 1.14], [0.0, 1.16], [0.75, 0.82]]), n: () => 2.3, tb: () => 0.4, N: 70 });
  g.add(M(cab, darkGlass()));
  // cửa cánh chim: tấm cửa (biên dạng cửa đùn mỏng + ô kính tối) bản lề dọc nóc, mở hất lên ~130°; chỗ cửa trên thân: ốp tối lộ ghế
  for (const sx of [-1, 1]) { const piv = new THREE.Group(); piv.position.set(sx * 0.34, 1.13, -0.12); g.add(piv);
    const ds = new THREE.Shape([[-0.6, 0], [0.45, 0], [0.62, -0.3], [0.5, -0.72], [-0.55, -0.74]].map(([a2, b2]) => new THREE.Vector2(a2, b2)));
    const dg = new THREE.ExtrudeGeometry(ds, { depth: 0.04, bevelEnabled: true, bevelSize: 0.015, bevelThickness: 0.015, bevelSegments: 2 }); dg.translate(0, 0, -0.02); const door = M(dg, body); door.rotation.y = -Math.PI / 2; piv.add(door);
    const wg = new THREE.ExtrudeGeometry(new THREE.Shape([[-0.48, -0.03], [0.38, -0.03], [0.52, -0.28], [-0.48, -0.3]].map(([a2, b2]) => new THREE.Vector2(a2, b2))), { depth: 0.05, bevelEnabled: false }); wg.translate(0, 0, -0.025); const win = M(wg, darkGlass()); win.rotation.y = -Math.PI / 2; piv.add(win);
    piv.rotation.z = sx * (open ? 2.25 : 0.72);
    if (open) { const hole = B(0.03, 0.4, 1.05, phys({ color: "#0e0f12", roughness: 0.7 }, 0.2), sx * (hw(-0.1) - 0.02), 0.66, -0.12); g.add(hole); } }
  seats(g, "#c46a2e", 0.4, -0.3, 0.33); wheelSW(g, 0.33, 0.78, 0.2); g.add(B(1.4, 0.14, 0.3, carbon(), 0, 0.72, 0.42));
  const cb = carbon(); g.add(B(1.8, 0.04, 0.3, cb, 0, 0.13, 2.05)); for (const sx of [-1, 1]) { const sc = M(new THREE.SphereGeometry(0.2, 16, 10), cb, sx * 0.86, 0.6, -0.7); sc.scale.set(0.25, 0.9, 1.6); g.add(sc); }
  g.add(B(1.6, 0.14, 0.3, cb, 0, 0.22, -2.12)); const spoiler = B(1.5, 0.03, 0.2, cb, 0, 0.98, -2.12); spoiler.rotation.x = -0.12; g.add(spoiler);
  for (const sx of [-1, 1]) { led(g, [[sx * 0.78, 0.6, 1.9], [sx * 0.45, 0.6, 2.05], [sx * 0.35, 0.55, 2.12]], [2.6, 2.6, 2.8], 0.02); led(g, [[sx * 0.4, 0.82, -2.2], [sx * 0.9, 0.76, -2.0]], [3.0, 0.3, 0.2], 0.028); }
  const ex = Cy(0.06, 0.06, 0.12, chromeP(), 0, 0.62, -2.24, 20); ex.rotation.x = Math.PI / 2; g.add(ex);
  mirror(g, 0.98, 0.92, 0.45, body);
  wheels(g, axF, axR, 0.82, 0.84, wr, wr + 0.01, 0.26, 0.31, { spokes: 7, rim: "#9a9ea6", cal: "#ff7a1a" });
  plates(g, bien, 0.3, 2.25, 0.5, -2.25);
  return g;
}

// ================= 3. SPEEDSTER MUI TRẦN – đen bóng, 2 bướu sau ghế, kính chắn gió thấp =================
export const SPEEDSTER_SEAT = { x: 0.33, y: 0.4, z: -0.2 }; // chỗ người lái (bên trái = +x)
export function speedster(bien = "30E-246.80") {
  const g = new THREE.Group(), L = 4.55, axF = 1.42, axR = -1.36, wr = 0.35, body = paint("#0c0d10", { metalness: 0.6, roughness: 0.2 });
  const hw = (z: number) => 0.98 * (0.83 + 0.17 * Math.max(Math.exp(-(((z - axF) / 0.55) ** 2)), Math.exp(-(((z - axR) / 0.6) ** 2)))) * (1 - 0.32 * Math.max(0, (z - 1.85) / 0.43) ** 2);
  const yt = pw([[-2.27, 0.82], [-1.7, 0.86], [-0.65, 0.84], [-0.5, 0.64], [0.35, 0.66], [0.55, 0.78], [1.5, 0.68], [2.27, 0.38]]), yb = pw([[-2.27, 0.28], [-2.0, 0.15], [2.0, 0.13], [2.27, 0.2]]);
  g.add(M(loft({ z0: -L / 2, z1: L / 2, hw, yb, yt, n: () => 3.2, tb: () => 0.15, fd: (z) => 0.14 * Math.exp(-(((z - axF) / 0.5) ** 2)) + 0.12 * Math.exp(-(((z - axR) / 0.55) ** 2)), arches: [{ z: axF, y: wr, r: wr + 0.07, tub: 0.6 }, { z: axR, y: wr, r: wr + 0.08, tub: 0.6 }] }), body));
  for (const sx of [-1, 1]) { const hump = M(loft({ z0: -1.6, z1: -0.55, hw: pw([[-1.6, 0.05], [-1.0, 0.2], [-0.55, 0.19]]), yb: () => 0.8, yt: pw([[-1.6, 0.86], [-0.8, 1.08], [-0.55, 1.08]]), n: () => 2.2, N: 30, Mr: 32 }), body); hump.position.x = sx * 0.33; g.add(hump); }
  const ws = M(loft({ z0: 0.45, z1: 0.62, hw: () => 0.72, yb: () => 0.78, yt: pw([[0.45, 0.96], [0.62, 0.8]]), n: () => 4, N: 8, Mr: 32 }), darkGlass()); g.add(ws);
  const cog = "#b0552a"; seats(g, cog, SPEEDSTER_SEAT.y, SPEEDSTER_SEAT.z, 0.33); wheelSW(g, 0.33, 0.78, 0.25); g.add(B(1.5, 0.16, 0.3, carbon(), 0, 0.68, 0.42)); g.add(B(0.3, 0.12, 1.0, carbon(), 0, 0.5, -0.1));
  for (const sx of [-1, 1]) g.add(B(0.02, 0.02, 3.6, phys({ color: "#ff7a1a", metalness: 0.3, roughness: 0.3, clearcoat: 1 }), sx * 0.985, 0.5, 0)); // chỉ cam dọc sườn
  const cb = carbon(); g.add(B(1.85, 0.04, 0.35, cb, 0, 0.12, 2.1)); g.add(B(1.7, 0.18, 0.32, cb, 0, 0.24, -2.14));
  for (const sx of [-1, 1]) { led(g, [[sx * 0.8, 0.58, 1.95], [sx * 0.38, 0.6, 2.13]], [2.6, 2.6, 2.8], 0.022); led(g, [[sx * 0.2, 0.8, -2.26], [sx * 0.88, 0.78, -2.12]], [3.0, 0.25, 0.2], 0.03); }
  for (const sx of [-0.2, 0.2]) { const ex = Cy(0.05, 0.05, 0.12, chromeP(), sx, 0.32, -2.3, 16); ex.rotation.x = Math.PI / 2; g.add(ex); }
  mirror(g, 0.97, 0.88, 0.5, body);
  wheels(g, axF, axR, 0.83, 0.85, wr, wr + 0.01, 0.26, 0.32, { spokes: 12, rim: "#6a6d73", cal: "#ff7a1a" });
  plates(g, bien, 0.3, 2.27, 0.5, -2.28);
  return g;
}

// ================= 4. HYPERCAR SANG "chủ tịch" – đen gương, sống lưng giữa, lưới crôm bầu dục ngang, mâm crôm =================
export function hyperChuTich(bien = "30H-999.99") {
  const g = new THREE.Group(), L = 4.75, axF = 1.48, axR = -1.42, wr = 0.37, body = paint("#050507", { metalness: 0.5, roughness: 0.12, clearcoatRoughness: 0.01 });
  const hw = (z: number) => 1.02 * (0.85 + 0.15 * Math.max(Math.exp(-(((z - axF) / 0.6) ** 2)), Math.exp(-(((z - axR) / 0.7) ** 2)))) * (1 - 0.28 * Math.max(0, (z - 1.9) / 0.48) ** 2) * (1 - 0.1 * Math.max(0, (-z - 1.9) / 0.48) ** 2);
  const yt = pw([[-2.37, 0.8], [-2.0, 0.98], [-0.9, 1.02], [0.6, 0.86], [1.7, 0.74], [2.37, 0.48]]), yb = pw([[-2.37, 0.3], [-2.0, 0.15], [2.0, 0.15], [2.37, 0.22]]);
  g.add(M(loft({ z0: -L / 2, z1: L / 2, hw, yb, yt, n: () => 2.4, tb: () => 0.2, fd: (z) => 0.15 * Math.exp(-(((z - axF) / 0.55) ** 2)) + 0.16 * Math.exp(-(((z - axR) / 0.7) ** 2)), arches: [{ z: axF, y: wr, r: wr + 0.07, tub: 0.6 }, { z: axR, y: wr, r: wr + 0.08, tub: 0.6 }] }), body));
  g.add(M(loft({ z0: -1.15, z1: 0.75, hw: (z) => 0.7 * (1 - 0.38 * Math.max(0, (z - 0.1) / 0.65) ** 2) * (1 - 0.3 * Math.max(0, (-z - 0.5) / 0.65) ** 2), yb: (z) => yt(z) - 0.05, yt: pw([[-1.15, 1.0], [-0.55, 1.17], [0.05, 1.19], [0.75, 0.88]]), n: () => 2.3, tb: () => 0.42, N: 70 }), darkGlass()));
  // sống lưng giữa chạy dọc nóc → đuôi (vây), viền crôm cong hình chữ C bên sườn
  g.add(M(loft({ z0: -2.3, z1: 1.9, hw: () => 0.025, yb: (z) => yt(z) - 0.05, yt: (z) => (z > -1.15 && z < 0.75 ? 1.2 : yt(z) + 0.05), n: () => 2, N: 80, Mr: 12 }), body));
  const ch = chromeP(); for (const sx of [-1, 1]) { const arc = M(new THREE.TorusGeometry(0.55, 0.018, 8, 40, Math.PI * 0.9), ch, sx * 1.005, 0.62, 0.1); arc.rotation.y = Math.PI / 2; arc.rotation.x = Math.PI * 0.55; arc.scale.set(1, 0.7, 1.4); g.add(arc); }
  const gr = M(new THREE.SphereGeometry(0.3, 28, 14), ch, 0, 0.42, 2.27); gr.scale.set(1.9, 0.45, 0.25); g.add(gr); const grIn = M(new THREE.SphereGeometry(0.28, 24, 12), phys({ color: "#050506", metalness: 0.6, roughness: 0.4 }), 0, 0.42, 2.29); grIn.scale.set(1.8, 0.38, 0.22); g.add(grIn);
  for (let k = -5; k <= 5; k++) g.add(B(0.008, 0.18, 0.04, ch, k * 0.045, 0.42, 2.33));
  for (const sx of [-1, 1]) { for (let k = 0; k < 4; k++) led(g, [[sx * (0.55 + k * 0.08), 0.62 + k * 0.012, 2.06 - k * 0.05], [sx * (0.6 + k * 0.08), 0.62 + k * 0.012, 2.02 - k * 0.05]], [2.6, 2.6, 2.8], 0.02); }
  led(g, [[-0.88, 0.86, -2.34], [0.88, 0.86, -2.34]], [3.0, 0.22, 0.18], 0.03); for (const y of [0.72, 0.62]) led(g, [[-0.7, y, -2.36], [0.7, y, -2.36]], [2.2, 0.18, 0.15], 0.018);
  for (const sx of [-1, 1]) { const ex = Cy(0.06, 0.06, 0.1, ch, sx * 0.3, 0.3, -2.36, 20); ex.rotation.x = Math.PI / 2; g.add(ex); }
  mirror(g, 1.0, 0.95, 0.48, body); seats(g, "#d8c3a0", 0.4, -0.3, 0.34);
  wheels(g, axF, axR, 0.85, 0.87, wr, wr + 0.01, 0.27, 0.32, { spokes: 16, chrome: true, cal: "#1a1a1e" });
  plates(g, bien, 0.3, 2.36, 0.5, -2.37);
  return g;
}

// ================= 5. MÔ TÔ SPORTBIKE PHÂN KHỐI LỚN – vàng (dáng chung, không chữ hãng) =================
export const BIKE_SEAT = { y: 0.98, z: -0.4 };
export function sportbike(col = "#f5c400", bien = "29-A1 999.99") {
  const g = new THREE.Group(), paintY = paint(col, { metalness: 0.35, roughness: 0.25 }), blk = phys({ color: "#121316", metalness: 0.5, roughness: 0.4 }), gold = phys({ color: "#d9a43a", metalness: 1, roughness: 0.2 }), R = 0.31;
  const WB = 0.72;
  for (const [z, w] of [[WB, 0.12], [-WB + 0.02, 0.19]] as [number, number][]) { const wh = new THREE.Group(); const t = Cy(R, R, w, rubberP(), 0, 0, 0, 36); t.rotation.z = Math.PI / 2; wh.add(t);
    const rim = Cy(R * 0.74, R * 0.74, w + 0.01, phys({ color: "#111214", metalness: 0.7, roughness: 0.3 }), 0, 0, 0, 32); rim.rotation.z = Math.PI / 2; wh.add(rim);
    for (let k = 0; k < 3; k++) for (const da of [0, 0.25]) { const a = k / 3 * Math.PI * 2 + da; const sp = B(w + 0.02, R * 0.6, 0.03, phys({ color: "#1b1c20", metalness: 0.7, roughness: 0.3 }), 0, Math.cos(a) * R * 0.33, Math.sin(a) * R * 0.33); sp.rotation.x = -a; wh.add(sp); }
    for (const sx of z > 0 ? [-1, 1] : [1]) { const d = Cy(R * 0.62, R * 0.62, 0.01, phys({ color: "#9a9ca2", metalness: 0.9, roughness: 0.3 }), sx * (w / 2 + 0.02), 0, 0, 32); d.rotation.z = Math.PI / 2; wh.add(d); wh.add(B(0.05, 0.12, 0.1, phys({ color: "#d8212f", metalness: 0.2, roughness: 0.3, clearcoat: 1 }), sx * (w / 2 + 0.05), R * 0.42, -R * 0.2)); }
    wh.position.set(0, R, z); g.add(wh); }
  // phuộc trước vàng đồng (nghiêng) + càng sau 1 bên + khung sườn đen
  for (const sx of [-1, 1]) { const fk = Cy(0.035, 0.035, 0.74, gold, sx * 0.09, R + 0.34, WB - 0.15, 14); fk.rotation.x = -0.42; g.add(fk); }
  const arm = B(0.07, 0.11, 0.66, blk, 0.13, R + 0.1, -0.4); arm.rotation.x = 0.14; g.add(arm);
  const spar = B(0.05, 0.1, 0.62, blk, 0, 0.78, 0.3); spar.rotation.x = 0.55; spar.position.x = 0; g.add(spar);
  // dàn áo: biên dạng nhìn ngang đùn theo bề ngang có vát (mũi nhọn, sườn ôm máy, bình xăng, đuôi vểnh mảnh)
  const ext = (pts: [number, number][], w: number, m: THREE.Material, bev = 0.045) => { const sh = new THREE.Shape(pts.map(([a2, b2]) => new THREE.Vector2(a2, b2))); const geo = new THREE.ExtrudeGeometry(sh, { depth: w - 2 * bev, bevelEnabled: true, bevelSize: bev, bevelThickness: bev, bevelSegments: 4, curveSegments: 12 }); geo.translate(0, 0, -(w - 2 * bev) / 2); const k = M(geo, m); k.rotation.y = -Math.PI / 2; return k; };
  g.add(ext([[0.92, 0.9], [0.84, 0.72], [0.66, 0.48], [0.36, 0.33], [0.02, 0.33], [-0.04, 0.5], [0.12, 0.6], [0.36, 0.8], [0.58, 0.98], [0.82, 1.02]], 0.36, paintY, 0.06));
  g.add(ext([[0.52, 1.0], [0.32, 0.8], [-0.18, 0.82], [-0.26, 0.96], [0.0, 1.1], [0.34, 1.1]], 0.32, paintY, 0.07));
  g.add(ext([[-0.22, 0.86], [-0.24, 0.98], [-0.62, 1.04], [-1.0, 1.1], [-1.02, 1.04], [-0.7, 0.92], [-0.4, 0.84]], 0.22, paintY, 0.05));
  g.add(ext([[-0.2, 0.98], [-0.6, 1.04], [-0.62, 1.0], [-0.24, 0.93]], 0.25, leather("#1a1a1d"), 0.03));
  g.add(ext([[0.9, 0.98], [0.74, 1.2], [0.66, 1.18], [0.78, 1.0]], 0.24, darkGlass(), 0.02)); // kính chắn gió khói
  for (const sx of [-1, 1]) g.add(B(0.02, 0.16, 0.34, blk, sx * 0.185, 0.6, 0.45)); // khe hút gió sườn
  const fend = ext([[0.98, 0.58], [0.8, 0.66], [0.55, 0.6], [0.6, 0.56], [0.8, 0.6]], 0.12, paintY, 0.02); g.add(fend);
  // máy + ống xả gầm + gác chân
  g.add(B(0.28, 0.3, 0.42, phys({ color: "#2b2d33", metalness: 0.8, roughness: 0.35 }), 0, 0.42, 0.06)); g.add(B(0.24, 0.12, 0.36, phys({ color: "#3a3c42", metalness: 0.9, roughness: 0.3 }), 0, 0.22, -0.1));
  for (const sx of [-0.06, 0.06]) { const tip = Cy(0.04, 0.04, 0.08, chromeP(), sx, 0.22, -0.3, 12); tip.rotation.x = Math.PI / 2; g.add(tip); }
  for (const sx of [-1, 1]) { g.add(B(0.1, 0.02, 0.02, blk, sx * 0.17, 0.36, -0.1)); const cl = Cy(0.014, 0.014, 0.2, blk, sx * 0.19, 1.06, 0.52, 8); cl.rotation.z = Math.PI / 2 - 0.25; g.add(cl); const mi = M(new THREE.SphereGeometry(0.045, 12, 8), blk, sx * 0.23, 1.13, 0.7); mi.scale.set(1.5, 0.7, 0.4); g.add(mi); }
  // đèn LED đôi mắt sắc + đèn hậu + biển
  for (const sx of [-1, 1]) led(g, [[sx * 0.03, 0.86, 0.95], [sx * 0.1, 0.88, 0.9], [sx * 0.16, 0.94, 0.8]], [2.8, 2.8, 3.0], 0.022);
  led(g, [[-0.05, 1.06, -1.03], [0.05, 1.06, -1.03]], [3, 0.25, 0.2], 0.022);
  const pl = plate(bien, 0.19, 0.14, true); pl.position.set(0, 0.72, -0.98); pl.rotation.y = Math.PI; pl.rotation.x = 0.35; g.add(pl); g.add(B(0.02, 0.24, 0.02, blk, 0, 0.84, -0.96));
  return g;
}
/** chân người ngồi (3D, màu quần + giày) – dùng với thẻ nhân vật cắt ngang hông khi ngồi xe */
export function riderLegs(pants: string, shoe: string, hip: [number, number, number], knee: [number, number, number], foot: [number, number, number]) {
  const g = new THREE.Group(), pm = phys({ color: pants, roughness: 0.8 }, 0.2), sm = phys({ color: shoe, roughness: 0.5 }, 0.3);
  const seg = (a: THREE.Vector3, b: THREE.Vector3, r: number, m: THREE.Material) => { const len = a.distanceTo(b); const k = new THREE.Mesh(new THREE.CapsuleGeometry(r, len, 4, 10), m); k.position.copy(a).add(b).multiplyScalar(0.5); k.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), b.clone().sub(a).normalize()); k.castShadow = true; g.add(k); };
  for (const sx of [-1, 1]) { const H = new THREE.Vector3(sx * hip[0], hip[1], hip[2]), K2 = new THREE.Vector3(sx * knee[0], knee[1], knee[2]), Ft = new THREE.Vector3(sx * foot[0], foot[1], foot[2]); seg(H, K2, 0.05, pm); seg(K2, Ft, 0.042, pm); const sh = new THREE.Mesh(new THREE.BoxGeometry(0.09, 0.07, 0.22), sm); sh.position.set(Ft.x, Ft.y - 0.03, Ft.z + 0.05); g.add(sh); }
  return g;
}
export const phys0 = (o: THREE.MeshPhysicalMaterialParameters, envI = 1) => phys(o, envI);
/** nhân độ phản chiếu môi trường cho mọi vật liệu bóng đã tạo (cảnh tối như showroom cần thấp) */
export function envScale(k: number) { for (const m of envUsers) { if (m.userData.e0 === undefined) m.userData.e0 = m.envMapIntensity; m.envMapIntensity = m.userData.e0 * k; } }
/** gắn phản chiếu HDRI cho vật liệu có sẵn (xe mẫu ngoài) */
export function applyEnv(m: THREE.MeshStandardMaterial, k = 1) { if (!(m as THREE.MeshStandardMaterial).isMeshStandardMaterial) return; needEnv(); m.envMapIntensity = k; if (envTex) m.envMap = envTex; envUsers.push(m as THREE.MeshPhysicalMaterial); m.needsUpdate = true; }

/** tay người lái 3D (2 tay): vai → khuỷu (hơi chùng xuống, bẻ ra ngoài) → bàn tay nắm ghi-đông / vô-lăng; toạ độ cục bộ của xe, x đối xứng quanh 0 (hoặc quanh x của vai nếu cx) */
export function riderArms(sleeve: string, skin: string, shoulder: [number, number, number], hand: [number, number, number], spread?: number) {
  const g = new THREE.Group(), sm = phys({ color: sleeve, roughness: 0.8 }, 0.2), km = phys({ color: skin, roughness: 0.7 }, 0.2);
  const seg = (a: THREE.Vector3, b: THREE.Vector3, r: number, m: THREE.Material) => { const len = a.distanceTo(b); const k = new THREE.Mesh(new THREE.CapsuleGeometry(r, len, 4, 10), m); k.position.copy(a).add(b).multiplyScalar(0.5); k.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), b.clone().sub(a).normalize()); k.castShadow = true; g.add(k); };
  const cx = spread !== undefined ? shoulder[0] : 0;
  for (const s of [-1, 1]) { const ox = spread !== undefined ? spread : 0; const S = new THREE.Vector3(spread !== undefined ? cx + s * ox : s * shoulder[0], shoulder[1], shoulder[2]); const Hn = new THREE.Vector3(spread !== undefined ? hand[0] + s * (ox - 0.02) : s * hand[0], hand[1], hand[2]);
    const E = S.clone().lerp(Hn, 0.5); E.y -= 0.1; E.x += (spread !== undefined ? s : Math.sign(S.x)) * 0.05;
    seg(S, E, 0.034, sm); seg(E, Hn, 0.03, sm); const h = new THREE.Mesh(new THREE.SphereGeometry(0.04, 10, 8), km); h.position.copy(Hn); g.add(h); }
  return g;
}
