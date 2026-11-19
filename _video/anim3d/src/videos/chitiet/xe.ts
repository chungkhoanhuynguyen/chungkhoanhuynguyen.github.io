// BỘ XE CHI TIẾT (chuẩn 20/11/2026) – toon + viền mực, vật liệu toonmat. Tất cả tự thiết kế dáng CHUNG, KHÔNG logo/tên hãng thật.
// Quy ước: đầu xe hướng +z, bánh chạm y = 0, tâm xe ở gốc; bên trái người lái = +x (xe Việt Nam lái bên trái).
// Ô tô: biên dạng nhìn ngang (thân) đùn theo bề ngang có vát mép + khoét hốc bánh; khoang kính trong suốt nhìn thấy ghế, taplô, vô-lăng;
// trụ A/B/C + nóc màu thân; đèn pha/hậu phát sáng; gương; tay nắm; khe cửa; lưới tản nhiệt; biển số giả kiểu VN.
import * as THREE from "three";
import { tm, glow } from "./toonmat";
import { xeSo } from "./suaxe2";
import { paint, loft, pw, sieuXeNem, sieuXeCanhChim, speedster, hyperChuTich, sportbike } from "./xe_sang";

const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";
type P2 = [number, number];
const M = (geo: THREE.BufferGeometry, m: THREE.Material, x = 0, y = 0, z = 0, cast = true) => { const k = new THREE.Mesh(geo, m); k.position.set(x, y, z); k.castShadow = cast; k.receiveShadow = true; return k; };
const B = (w: number, h: number, d: number, m: THREE.Material, x = 0, y = 0, z = 0) => M(new THREE.BoxGeometry(w, h, d), m, x, y, z);
const C = (r1: number, r2: number, h: number, m: THREE.Material, x = 0, y = 0, z = 0, s = 18) => M(new THREE.CylinderGeometry(r1, r2, h, s), m, x, y, z);
const glass = (tint = "#22303e", op = 0.45) => { const m = new THREE.MeshLambertMaterial({ color: tint, transparent: true, opacity: op, depthWrite: false, side: THREE.DoubleSide }); return m; };
const chrome = () => tm("#e3e7ec"), black = () => tm("#16171b"), rubber = () => tm("#1b1b1f");

/** biển số giả kiểu Việt Nam (nền trắng chữ đen); 2 dòng cho xe máy */
export function plate(text: string, w = 0.52, h = 0.12, two = false) {
  const c = document.createElement("canvas"); c.width = 512; c.height = Math.round(512 * h / w); const x = c.getContext("2d")!, H = c.height;
  x.fillStyle = "#f6f6f2"; x.fillRect(0, 0, 512, H); x.strokeStyle = "#111"; x.lineWidth = 10; x.strokeRect(6, 6, 500, H - 12); x.fillStyle = "#111"; x.textAlign = "center"; x.textBaseline = "middle";
  if (two) { const [a, b] = text.split(" "); x.font = `900 ${H * 0.36}px ${F}`; x.fillText(a, 256, H * 0.3, 470); x.fillText(b ?? "", 256, H * 0.74, 470); } else { x.font = `900 ${H * 0.72}px ${F}`; x.fillText(text, 256, H * 0.54, 480); }
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4;
  const m = M(new THREE.PlaneGeometry(w, h), new THREE.MeshLambertMaterial({ map: t }), 0, 0, 0, false); return m;
}
const label = (text: string, w: number, h: number, bg: string, fg: string) => { const c = document.createElement("canvas"); c.width = 512; c.height = Math.round(512 * h / w); const x = c.getContext("2d")!; x.fillStyle = bg; x.fillRect(0, 0, 512, c.height); x.fillStyle = fg; x.textAlign = "center"; x.textBaseline = "middle"; x.font = `900 ${c.height * 0.6}px ${F}`; x.fillText(text, 256, c.height * 0.54, 490); const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t; };

/** bánh ô tô: lốp + la-zăng n chấu + moay-ơ (+ kẹp phanh đỏ nếu thể thao) – trục theo x */
function wheel(r: number, w: number, spokes = 5, sport = false, chromeRim = false) {
  const g = new THREE.Group(); const t = C(r, r, w, rubber(), 0, 0, 0, 28); t.rotation.z = Math.PI / 2; g.add(t);
  const side = M(new THREE.TorusGeometry(r * 0.86, r * 0.09, 8, 28), tm("#232327"), 0, 0, 0); side.rotation.y = Math.PI / 2; g.add(side);
  for (const s of [-1, 1]) { const rimM = chromeRim ? chrome() : tm(sport ? "#2b2d33" : "#9aa0a8"); const rim = C(r * 0.64, r * 0.64, 0.02, tm("#2a2c31"), s * (w / 2 + 0.005), 0, 0, 24); rim.rotation.z = Math.PI / 2; g.add(rim); const lip = M(new THREE.TorusGeometry(r * 0.62, 0.015, 6, 28), rimM, s * (w / 2 + 0.012), 0, 0); lip.rotation.y = Math.PI / 2; g.add(lip);
    for (let k = 0; k < spokes; k++) { const a = (k / spokes) * Math.PI * 2; const sp = B(0.02, r * 0.56, 0.035, rimM, s * (w / 2 + 0.015), Math.cos(a) * r * 0.31, Math.sin(a) * r * 0.31); sp.rotation.x = a; g.add(sp); }
    const hub = C(r * 0.12, r * 0.12, 0.03, chrome(), s * (w / 2 + 0.025), 0, 0, 12); hub.rotation.z = Math.PI / 2; g.add(hub);
    if (sport) { const cal = B(0.04, r * 0.3, r * 0.5, tm("#d8212f"), s * (w / 2 - 0.02), r * 0.32, -r * 0.1); g.add(cal); } }
  return g;
}
const shape = (pts: P2[]) => { const s = new THREE.Shape(); pts.forEach(([z, y], i) => (i ? s.lineTo(z, y) : s.moveTo(z, y))); s.closePath(); return s; };
/** đùn biên dạng (z, y) theo bề ngang w, có vát; khoét hốc bánh tại các tâm (z, y, r) */
function extrude(pts: P2[], w: number, m: THREE.Material, bev = 0.05, holes: [number, number, number][] = []) {
  const s = shape(pts); for (const [z, y, r] of holes) { const h = new THREE.Path(); h.absarc(z, y, r, 0, Math.PI * 2, true); s.holes.push(h); }
  const geo = new THREE.ExtrudeGeometry(s, { depth: w - 2 * bev, bevelEnabled: bev > 0, bevelSize: bev, bevelThickness: bev, bevelSegments: 3, curveSegments: 16 }); geo.translate(0, 0, -(w - 2 * bev) / 2);
  const k = M(geo, m); k.rotation.y = -Math.PI / 2; return k; // sau xoay: trục z của hình → x thế giới
}
/** thanh nối 2 điểm (z, y) ở bên x – làm trụ kính, viền crôm */
function bar(a: P2, b: P2, x: number, t: number, d: number, m: THREE.Material) { const len = Math.hypot(b[0] - a[0], b[1] - a[1]); const k = B(d, len, t, m, x, (a[1] + b[1]) / 2, (a[0] + b[0]) / 2); k.rotation.x = Math.atan2(b[0] - a[0], b[1] - a[1]); return k; }

export type CarSpec = {
  L: number; W: number; col: string; body: P2[]; cab?: P2[]; wr: number; wb: number; wz?: number; ww?: number; spokes?: number; sport?: boolean; chromeRim?: boolean;
  head: [number, number, number]; tail: [number, number, number]; // y đèn, cao đèn, z đặt (đầu/đuôi)
  plateF: [number, number]; plateR: [number, number]; plateText: string; grille?: "dark" | "chrome" | "none"; chromeTrim?: boolean;
  seats: number; open?: boolean; doors?: number[]; mirrorZ?: number; mirrorY?: number; extra?: (g: THREE.Group) => void;
};
/** ô tô theo thông số: thân + khoang kính + nội thất + đèn + gương + biển */
export function oto(s: CarSpec) {
  const g = new THREE.Group(), body = paint(s.col, { metalness: 0.45, roughness: 0.35 }), dark = tm("#26272c"), ww = s.ww ?? 0.24, wz = s.wz ?? 0;
  const axF = wz + s.wb / 2, axR = wz - s.wb / 2;
  g.add(extrude(s.body, s.W, body, 0.06, [[axF, s.wr, s.wr + 0.05], [axR, s.wr, s.wr + 0.05]]));
  for (const z of [axF, axR]) { for (const sx of [-1, 1]) { const w = wheel(s.wr, ww, s.spokes ?? 5, s.sport, s.chromeRim); w.position.set(sx * (s.W / 2 - ww / 2 - 0.02), s.wr, z); g.add(w); }
    const well = C(s.wr + 0.05, s.wr + 0.05, s.W - 0.12, tm("#0e0e10"), 0, s.wr, z, 20); well.rotation.z = Math.PI / 2; well.castShadow = false; g.add(well); }
  // khoang kính + trụ + nóc
  if (s.cab && !s.open) { const cab = s.cab; const gl = extrude(cab, s.W * 0.86, glass(), 0.02); gl.castShadow = false; g.add(gl);
    for (const sx of [-1, 1]) { const x = sx * s.W * 0.43; g.add(bar(cab[0], cab[1], x, 0.07, 0.05, body)); g.add(bar(cab[cab.length - 2], cab[cab.length - 1], x, 0.09, 0.05, body));
      const midZ = (cab[1][0] + cab[2][0]) / 2; g.add(bar([midZ, cab[cab.length - 1][1]], [midZ, Math.max(cab[1][1], cab[2][1]) - 0.02], x, 0.07, 0.05, body));
      if (s.chromeTrim) { g.add(bar(cab[1], cab[2], sx * s.W * 0.435, 0.02, 0.03, chrome())); g.add(bar([cab[0][0], cab[0][1] + 0.01], [cab[cab.length - 1][0], cab[cab.length - 1][1] + 0.01], sx * s.W * 0.44, 0.02, 0.03, chrome())); } }
    const roofLen = Math.abs(cab[1][0] - cab[2][0]), roofY = Math.max(cab[1][1], cab[2][1]); g.add(B(s.W * 0.88, 0.05, roofLen + 0.06, body, 0, roofY, (cab[1][0] + cab[2][0]) / 2)); }
  // nội thất: ghế, taplô, vô-lăng
  const belt = s.cab ? s.cab[0][1] : s.body.reduce((a, p) => Math.max(a, p[1]), 0) - 0.1, seatM = tm(s.chromeTrim ? "#c9b38a" : "#3a3a40");
  const zFront = s.cab ? Math.min(s.cab[0][0], s.cab[1][0]) - 0.35 : axF - 0.9, rows = s.seats > 4 ? 3 : s.seats > 2 ? 2 : 1;
  for (let rI = 0; rI < rows; rI++) { const z = zFront - 0.15 - rI * 0.85; for (const sx of rows === 1 || rI > 0 ? [-1, 1] : [-1, 1]) { g.add(B(0.46, 0.12, 0.5, seatM, sx * s.W * 0.22, belt - 0.42, z)); const bk = B(0.46, 0.55, 0.1, seatM, sx * s.W * 0.22, belt - 0.12, z - 0.26); bk.rotation.x = -0.18; g.add(bk); g.add(B(0.22, 0.12, 0.08, seatM, sx * s.W * 0.22, belt + 0.2, z - 0.3)); } }
  g.add(B(s.W * 0.9, 0.16, 0.35, dark, 0, belt - 0.08, zFront + 0.42));
  const sw = M(new THREE.TorusGeometry(0.17, 0.022, 8, 20), black(), s.W * 0.22, belt + 0.02, zFront + 0.2); sw.rotation.x = -0.35; g.add(sw);
  // đèn
  const [hy, hh, hz] = s.head, [ty, th, tz] = s.tail;
  for (const sx of [-1, 1]) { g.add(B(s.W * 0.26, hh, 0.06, glow(2.6, 2.5, 2.2), sx * s.W * 0.33, hy, hz)); g.add(B(s.W * 0.27, 0.025, 0.065, glow(2.2, 2.4, 2.6), sx * s.W * 0.33, hy - hh / 2 - 0.03, hz - 0.01));
    g.add(B(s.W * 0.26, th, 0.06, glow(2.5, 0.25, 0.2), sx * s.W * 0.33, ty, tz)); }
  if (s.grille !== "none") { const gm = s.grille === "chrome" ? chrome() : tm("#141416"); const gr = B(s.W * (s.grille === "chrome" ? 0.36 : 0.42), s.grille === "chrome" ? hh * 2.6 : hh * 1.2, 0.05, gm, 0, hy - (s.grille === "chrome" ? hh * 0.6 : hh * 0.7), hz + 0.005); g.add(gr);
    if (s.grille === "chrome") for (let k = 0; k < 7; k++) g.add(B(0.012, hh * 2.4, 0.06, tm("#1a1a1e"), -s.W * 0.16 + k * s.W * 0.053, hy - hh * 0.6, hz + 0.01)); }
  // gương + tay nắm + khe cửa
  const mz = s.mirrorZ ?? (s.cab ? s.cab[0][0] - 0.12 : axF - 0.6), my = s.mirrorY ?? belt + 0.05;
  for (const sx of [-1, 1]) { const mr = B(0.16, 0.1, 0.12, body, sx * (s.W / 2 + 0.08), my, mz); g.add(mr); g.add(B(0.02, 0.08, 0.09, tm("#7b8a99"), sx * (s.W / 2 + 0.16), my, mz - 0.01)); g.add(B(0.1, 0.03, 0.03, black(), sx * (s.W / 2 + 0.02), my - 0.02, mz + 0.03));
    for (const dz of s.doors ?? []) { g.add(B(0.012, belt - 0.32, 0.012, tm("#111"), sx * (s.W / 2 + 0.001), (belt + 0.32) / 2, dz)); g.add(B(0.02, 0.03, 0.14, s.chromeTrim ? chrome() : tm("#2a2a2e"), sx * (s.W / 2 + 0.005), belt - 0.1, dz - 0.25)); } }
  // biển số
  const pf = plate(s.plateText); pf.position.set(0, s.plateF[0], s.plateF[1] + 0.01); g.add(pf);
  const pr = plate(s.plateText); pr.position.set(0, s.plateR[0], s.plateR[1] - 0.01); pr.rotation.y = Math.PI; g.add(pr);
  s.extra?.(g);
  return g;
}

// ---------- dàn xe đầy đủ ----------
export const XE = {
  /** ô tô con phổ thông (sedan nhỏ 5 chỗ) */
  phoThong: (col = "#b8c2cc", bien = "30A-215.68") => oto({ L: 4.4, W: 1.74, col, wr: 0.31, wb: 2.6, seats: 5, plateText: bien, doors: [0.55, -0.45],
    body: [[2.2, 0.32], [2.2, 0.62], [2.05, 0.8], [0.95, 0.9], [-1.35, 0.92], [-2.1, 0.88], [-2.2, 0.72], [-2.2, 0.32]],
    cab: [[0.95, 0.9], [0.25, 1.42], [-0.95, 1.42], [-1.6, 0.92]], head: [0.72, 0.09, 2.17], tail: [0.8, 0.1, -2.21], plateF: [0.48, 2.21], plateR: [0.55, -2.22] }),
  /** taxi (thân sedan phổ thông, trắng sọc xanh, hộp đèn TAXI trên nóc, chữ cửa – tên hãng tự đặt) */
  taxi: () => { const g = XE.phoThong("#f4f4f0", "30F-468.27"); const st = tm("#1d8a4a"); for (const sx of [-1, 1]) { const b = B(0.01, 0.1, 3.6, st, sx * 0.875, 0.62, 0); g.add(b);
      const t = M(new THREE.PlaneGeometry(1.1, 0.2), new THREE.MeshLambertMaterial({ map: label("TAXI PHỐ · 024.38xx.xxxx", 1.1, 0.2, "#f4f4f0", "#1d8a4a"), side: THREE.DoubleSide }), sx * 0.882, 0.76, 0.05, false); t.rotation.y = sx * Math.PI / 2; g.add(t); }
    const box = B(0.6, 0.18, 0.22, tm("#f2d36b"), 0, 1.55, -0.3); g.add(box); for (const sz of [-1, 1]) { const p = M(new THREE.PlaneGeometry(0.56, 0.15), new THREE.MeshBasicMaterial({ map: label("TAXI", 0.56, 0.15, "#f2d36b", "#1d2a44") }), 0, 1.55, -0.3 + sz * 0.112, false); p.rotation.y = sz > 0 ? 0 : Math.PI; g.add(p); } return g; },
  /** SUV 7 chỗ: cao, vuông, giá nóc, ốp cản bạc */
  suv7: (col = "#3a4a5e", bien = "30K-777.18") => oto({ L: 4.85, W: 1.9, col, wr: 0.38, wb: 2.85, seats: 7, plateText: bien, doors: [0.65, -0.4], grille: "dark",
    body: [[2.42, 0.42], [2.42, 0.86], [2.25, 1.02], [1.15, 1.1], [-2.3, 1.12], [-2.42, 1.0], [-2.42, 0.42]], cab: [[1.15, 1.1], [0.55, 1.72], [-2.15, 1.74], [-2.33, 1.12]],
    head: [0.9, 0.1, 2.39], tail: [1.0, 0.16, -2.43], plateF: [0.6, 2.43], plateR: [0.68, -2.44],
    extra: (g) => { for (const sx of [-1, 1]) g.add(B(0.04, 0.05, 2.5, tm("#2a2a2e"), sx * 0.75, 1.8, -0.75)); for (const z of [0.2, -1.7]) g.add(B(1.5, 0.03, 0.05, tm("#2a2a2e"), 0, 1.82, z)); for (const z of [2.42, -2.42]) g.add(B(1.6, 0.12, 0.08, tm("#c9cdd3"), 0, 0.5, z)); } }),
  /** sedan sang "xe chủ tịch": đen, dài, nắp capo dài, lưới crôm lớn, viền kính crôm, la-zăng crôm, ghế da kem */
  chuTich: (bien = "30H-999.99") => oto({ L: 5.3, W: 1.95, col: "#0f1012", wr: 0.36, wb: 3.2, seats: 5, plateText: bien, grille: "chrome", chromeTrim: true, chromeRim: true, spokes: 10, doors: [0.6, -0.55],
    body: [[2.65, 0.36], [2.65, 0.72], [2.5, 0.86], [0.85, 0.98], [-1.75, 1.0], [-2.55, 0.94], [-2.65, 0.78], [-2.65, 0.36]],
    cab: [[0.85, 0.98], [0.1, 1.48], [-1.25, 1.48], [-1.95, 1.0]], head: [0.76, 0.08, 2.62], tail: [0.86, 0.08, -2.66], plateF: [0.5, 2.66], plateR: [0.62, -2.67],
    extra: (g) => { for (const sx of [-1, 1]) g.add(B(0.012, 0.035, 4.4, tm("#e3e7ec"), sx * 0.985, 0.55, 0)); const orn = C(0.012, 0.03, 0.09, tm("#e3e7ec"), 0, 0.95, 2.45, 8); g.add(orn); } }),
  /** siêu xe thể thao 2 cửa: thấp, dáng nêm, hút gió sườn, cánh gió sau, bánh to kẹp phanh đỏ (tự thiết kế, không logo) */
  sieuXe: (col = "#f2c230", bien = "51K-888.88") => oto({ L: 4.6, W: 2.0, col, wr: 0.36, wb: 2.7, sport: true, spokes: 6, ww: 0.3, seats: 2, plateText: bien, grille: "none", doors: [0.35],
    body: [[2.3, 0.2], [2.3, 0.42], [1.3, 0.72], [0.55, 0.86], [-1.6, 0.98], [-2.3, 0.9], [-2.3, 0.2]],
    cab: [[0.75, 0.82], [-0.05, 1.12], [-0.8, 1.12], [-1.75, 0.94]], head: [0.5, 0.05, 2.18], tail: [0.78, 0.05, -2.31], plateF: [0.3, 2.31], plateR: [0.45, -2.31], mirrorY: 0.92,
    extra: (g) => { const blk = tm("#15161a"); for (const sx of [-1, 1]) { const intake = B(0.04, 0.26, 0.7, blk, sx * 1.0, 0.62, -0.55); intake.rotation.x = -0.15; g.add(intake); g.add(B(0.05, 0.06, 2.6, blk, sx * 0.99, 0.24, 0)); }
      const wing = B(1.8, 0.04, 0.32, blk, 0, 1.22, -2.05); wing.rotation.x = 0.08; g.add(wing); for (const sx of [-0.55, 0.55]) g.add(B(0.05, 0.26, 0.12, blk, sx, 1.06, -2.0)); g.add(B(1.7, 0.12, 0.3, blk, 0, 0.18, -2.18));
      for (const sx of [-1, 1]) for (let k = 0; k < 2; k++) { const ex = C(0.05, 0.05, 0.1, tm("#9aa0a8"), sx * (0.2 + k * 0.12), 0.32, -2.33, 12); ex.rotation.x = Math.PI / 2; g.add(ex); } } }),
  /** xe mui trần 2 chỗ (mui hạ): kính chắn gió có khung, 2 vòm bảo vệ sau ghế, ghế da đỏ nhìn rõ */
  muiTran: (col = "#c8202f", bien = "30E-246.80") => oto({ L: 4.2, W: 1.8, col, wr: 0.33, wb: 2.5, seats: 2, open: true, plateText: bien, spokes: 7, doors: [0.25],
    body: [[2.1, 0.28], [2.1, 0.58], [1.85, 0.74], [0.75, 0.82], [-1.95, 0.84], [-2.1, 0.74], [-2.1, 0.28]],
    head: [0.64, 0.07, 2.07], tail: [0.72, 0.07, -2.11], plateF: [0.42, 2.11], plateR: [0.5, -2.12], mirrorZ: 0.55, mirrorY: 0.95,
    extra: (g) => { const fr = tm("#2a2a2e"); const ws = M(new THREE.PlaneGeometry(1.6, 0.42), glass("#5a7a90", 0.35), 0, 1.03, 0.62, false); ws.rotation.x = -0.55; g.add(ws);
      for (const sx of [-0.8, 0.8]) g.add(bar([0.75, 0.84], [0.5, 1.22], sx, 0.04, 0.04, fr)); g.add(bar([0.5, 1.22], [0.5, 1.22], 0, 0.04, 1.6, fr)); { const top = B(1.62, 0.04, 0.04, fr, 0, 1.22, 0.5); g.add(top); }
      const red = tm("#8a1c22"); for (const sx of [-1, 1]) { g.add(B(0.5, 0.14, 0.55, red, sx * 0.4, 0.5, -0.45)); const bk = B(0.5, 0.62, 0.12, red, sx * 0.4, 0.82, -0.78); bk.rotation.x = -0.22; g.add(bk); g.add(B(0.26, 0.16, 0.12, red, sx * 0.4, 1.2, -0.86));
        const hoop = M(new THREE.TorusGeometry(0.2, 0.025, 6, 14, Math.PI), tm("#c9cdd3"), sx * 0.4, 0.92, -1.0); hoop.rotation.y = Math.PI / 2; hoop.rotation.z = 0; g.add(hoop); }
      g.add(B(1.5, 0.16, 0.3, tm("#26272c"), 0, 0.78, 0.4)); const sw = M(new THREE.TorusGeometry(0.16, 0.022, 8, 20), tm("#16171b"), 0.4, 0.9, 0.2); sw.rotation.x = -0.4; g.add(sw);
      g.add(B(1.6, 0.06, 0.9, tm("#3a3a40"), 0, 0.82, -1.45)); } }),
  /** xe tải nhỏ 1,5 tấn: cabin + thùng kín chữ quảng cáo + bánh đôi sau */
  taiNho: (col = "#2f6fb0", bien = "29C-135.79") => { const g = oto({ L: 5.4, W: 1.9, col, wr: 0.36, wb: 3.0, wz: 0.1, seats: 2, plateText: bien, doors: [1.8], grille: "dark",
      body: [[2.7, 0.42], [2.7, 1.1], [2.55, 1.25], [1.5, 1.28], [1.45, 0.75], [-2.7, 0.75], [-2.7, 0.42]], cab: [[2.55, 1.25], [2.35, 2.0], [1.5, 2.02], [1.5, 1.28]],
      head: [0.95, 0.12, 2.68], tail: [0.62, 0.1, -2.71], plateF: [0.62, 2.71], plateR: [0.55, -2.72], mirrorZ: 2.45, mirrorY: 1.55 });
    const box = B(1.96, 1.65, 3.85, tm("#f4f1e6"), 0, 1.62, -0.78); g.add(box);
    for (const sx of [-1, 1]) { const t = M(new THREE.PlaneGeometry(3.4, 0.6), new THREE.MeshLambertMaterial({ map: label("CHUYỂN NHÀ · 09xx.xxx.xxx", 3.4, 0.6, "#f4f1e6", "#c8202f"), side: THREE.DoubleSide }), sx * 0.985, 1.7, -0.78, false); t.rotation.y = sx * Math.PI / 2; g.add(t); }
    for (const sx of [-1, 1]) { const w = wheel(0.36, 0.22); w.position.set(sx * 0.62, 0.36, -1.4); g.add(w); }
    return g; },
};

// ---------- xe máy ----------
/** xe tay ga phổ thông: sàn để chân phẳng, yếm trước, thân sau bọc nhựa, bánh nhỏ, cốp dưới yên */
export function xeGa(col = "#e9e7e2", bien = "29-G1 357.24") {
  const g = new THREE.Group(), body = paint(col, { metalness: 0.2, roughness: 0.3 }), dark = tm("#1e1e22"), chromeM = chrome(), R = 0.24, WB = 0.64;
  for (const z of [-WB, WB]) { const t = C(R, R, 0.11, rubber(), 0, R, z, 24); t.rotation.z = Math.PI / 2; g.add(t); const rim = C(R * 0.62, R * 0.62, 0.115, tm("#3a3d44"), 0, R, z, 18); rim.rotation.z = Math.PI / 2; g.add(rim);
    for (let k = 0; k < 5; k++) { const a = k / 5 * Math.PI * 2; for (const sx of [-1, 1]) { const sp = B(0.02, R * 0.52, 0.04, tm("#c9cdd3"), sx * 0.06, R + Math.cos(a) * R * 0.3, z + Math.sin(a) * R * 0.3); sp.rotation.x = -a; g.add(sp); } } }
  // thân liền: đuôi bọc nhựa → sàn để chân lõm → yếm trước dựng cao (quét mặt cắt)
  g.add(M(loft({ z0: -1.0, z1: 0.74, hw: pw([[-1.0, 0.08], [-0.8, 0.18], [-0.2, 0.19], [0.1, 0.17], [0.4, 0.17], [0.58, 0.2], [0.74, 0.12]]), yb: pw([[-1.0, 0.66], [-0.75, 0.46], [-0.3, 0.3], [0.3, 0.28], [0.5, 0.52], [0.74, 0.62]]),
    yt: pw([[-1.0, 0.76], [-0.8, 0.8], [-0.25, 0.74], [-0.12, 0.4], [0.32, 0.38], [0.48, 0.9], [0.6, 1.02], [0.74, 0.86]]), n: () => 2.8, tb: () => 0.2, N: 100, Mr: 40 }), body));
  g.add(M(loft({ z0: -0.92, z1: -0.12, hw: () => 0.16, yb: () => 0.74, yt: pw([[-0.92, 0.84], [-0.5, 0.88], [-0.12, 0.84]]), n: () => 3, N: 24, Mr: 24 }), tm("#1e1a1b"))); // yên
  g.add(M(loft({ z0: 0.5, z1: 0.86, hw: pw([[0.5, 0.06], [0.7, 0.11], [0.86, 0.05]]), yb: () => 0.5, yt: pw([[0.5, 0.56], [0.7, 0.6], [0.86, 0.54]]), n: () => 2.4, N: 16, Mr: 20 }), body)); // chắn bùn
  const fork = C(0.025, 0.025, 0.6, chromeM, 0, 0.55, 0.66, 8); fork.rotation.x = -0.35; g.add(fork);
  const head = M(new THREE.SphereGeometry(0.15, 20, 12), body, 0, 1.05, 0.56); head.scale.set(1.25, 0.55, 1.0); g.add(head);
  g.add(B(0.24, 0.05, 0.04, glow(2.6, 2.4, 2.0), 0, 0.95, 0.74)); const bar2 = C(0.014, 0.014, 0.66, chromeM, 0, 1.1, 0.52, 8); bar2.rotation.z = Math.PI / 2; g.add(bar2);
  for (const sx of [-0.31, 0.31]) { const gr = C(0.02, 0.02, 0.1, rubber(), sx, 1.1, 0.52, 8); gr.rotation.z = Math.PI / 2; g.add(gr); const st = C(0.006, 0.006, 0.22, chromeM, sx * 0.72, 1.2, 0.5, 5); st.rotation.z = -Math.sign(sx) * 0.3; g.add(st); const mi = M(new THREE.SphereGeometry(0.045, 10, 8), dark, sx * 0.92, 1.3, 0.5); mi.scale.set(1.3, 0.8, 0.3); g.add(mi); }
  g.add(B(0.2, 0.05, 0.05, glow(2.4, 0.25, 0.2), 0, 0.76, -0.99)); const ex = C(0.045, 0.04, 0.42, tm("#2a2a2e"), 0.15, 0.32, -0.5, 12); ex.rotation.x = Math.PI / 2; g.add(ex);
  const pl = plate(bien, 0.19, 0.14, true); pl.position.set(0, 0.58, -1.0); pl.rotation.y = Math.PI; pl.rotation.x = 0.2; g.add(pl);
  const stand = C(0.012, 0.012, 0.3, dark, -0.16, 0.13, -0.1, 6); stand.rotation.z = 0.55; g.add(stand);
  return g;
}
/** xe máy chở hàng: xe số + giá chở hàng gỗ sau yên + thùng xốp + bao tải buộc dây */
export function xeHang(col = "#1f3f8a", bien = "29-K2 861.05") {
  const g = xeSo(col, bien); const wood = tm("#a8793e");
  g.add(B(0.5, 0.04, 0.7, wood, 0, 0.92, -0.62)); for (const sx of [-0.22, 0.22]) g.add(B(0.04, 0.2, 0.04, wood, sx, 0.82, -0.32)); for (const sx of [-0.22, 0.22]) g.add(B(0.04, 0.22, 0.04, wood, sx, 0.82, -0.92));
  g.add(B(0.62, 0.42, 0.55, tm("#f4f4f0"), 0, 1.15, -0.65)); // thùng xốp
  const sack = M(new THREE.SphereGeometry(0.28, 14, 10), tm("#d9c79a"), 0, 1.55, -0.68); sack.scale.set(1.1, 0.7, 0.9); g.add(sack);
  for (const dz of [-0.5, -0.8]) g.add(B(0.64, 0.02, 0.025, tm("#c8202f"), 0, 1.37, dz)); for (const sx of [-0.32, 0.32]) for (const dz of [-0.5, -0.8]) g.add(B(0.02, 0.42, 0.025, tm("#c8202f"), sx, 1.16, dz));
  return g;
}

export type XeKey = string;
export const XE_DS: { k: XeKey; ten: string; L: number; H: number; make: () => THREE.Group }[] = [
  { k: "wave", ten: "Xe số kiểu Wave (đỏ)", L: 1.9, H: 1.1, make: () => xeSo("#c8202f", "29-B1 168.86") },
  { k: "dream", ten: "Xe số kiểu Dream (nâu)", L: 1.9, H: 1.1, make: () => xeSo("#7a2e24", "29-H7 052.19", true) },
  { k: "xega", ten: "Xe tay ga", L: 1.95, H: 1.15, make: () => xeGa("#f4f4f2") },
  { k: "xehang", ten: "Xe máy chở hàng", L: 1.95, H: 1.8, make: () => xeHang() },
  { k: "sportbike", ten: "Mô tô sportbike phân khối lớn (vàng, dáng chung, không chữ hãng)", L: 2.1, H: 1.25, make: () => sportbike() },
  { k: "photong", ten: "Ô tô con phổ thông 5 chỗ", L: 4.4, H: 1.45, make: () => XE.phoThong() },
  { k: "taxi", ten: "Taxi (hãng tự đặt: TAXI PHỐ)", L: 4.4, H: 1.65, make: () => XE.taxi() },
  { k: "suv7", ten: "SUV 7 chỗ", L: 4.85, H: 1.85, make: () => XE.suv7() },
  { k: "chutich", ten: "Sedan sang \"xe chủ tịch\"", L: 5.3, H: 1.5, make: () => XE.chuTich() },
  { k: "tainho", ten: "Xe tải nhỏ thùng kín", L: 5.4, H: 2.5, make: () => XE.taiNho() },
  { k: "sx_nem", ten: "Siêu xe nêm góc cạnh – xanh rêu ánh tím (tự thiết kế)", L: 4.62, H: 1.3, make: () => sieuXeNem() },
  { k: "sx_canhchim", ten: "Siêu xe cong mượt – xám bạc, cửa cánh chim mở (tự thiết kế)", L: 4.5, H: 1.9, make: () => sieuXeCanhChim(true) },
  { k: "speedster", ten: "Speedster mui trần – đen (tự thiết kế)", L: 4.55, H: 1.1, make: () => speedster() },
  { k: "hyper", ten: "Hypercar sang \"chủ tịch\" – đen gương (tự thiết kế)", L: 4.75, H: 1.2, make: () => hyperChuTich() },
];
