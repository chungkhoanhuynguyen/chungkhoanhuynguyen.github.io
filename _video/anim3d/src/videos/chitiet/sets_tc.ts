// BỐI CẢNH CHI TIẾT DÙNG CHUNG CHO TIN TÀI CHÍNH (chuẩn suaxe2: đồ Poly Haven + toon + đèn ấm), 20/11/2026.
// sapvai (sạp vải chợ), phongkhach (phòng khách căn hộ, tối), vanphong (phòng giao dịch có bảng điện), nganhang (quầy ngân hàng), cafevh (cà phê vỉa hè).
// Quy ước: tường sau ở z = -3, máy quay đứng phía +z nhìn về -z → +x nằm bên PHẢI màn. Vùng diễn nhân vật: x -1.5..1.5, z -1..1.5.
// Mỗi set trả { g, cho }: cho = các điểm đặt sẵn (người đứng/ngồi, máy quay gợi ý).
import * as THREE from "three";
import { tm, U, glow, setLook } from "./toonmat";
import { putModel, PO, gopTinh } from "./models";
import { mesh, bx, cy, cvs, ctex, grime, wallTex, floorTex, woodTex, metalTex, signTex, paperTex, plane, corrugated, plasticStool, blob, wire } from "./suaxe2";
import { rng } from "../pho/paint";
import { buildStreet, GOLD_X } from "../vang/sets";
import { NOINK } from "../pho/ink";

type V3 = [number, number, number];
const DIR = "chitiet/m";
const put = (g: THREE.Group, name: string, x: number, y: number, z: number, ry = 0, o: PO = {}) => putModel(g, DIR, name, x, y, z, ry, o, blob);
const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";
const lamps = (L: [V3, V3, number][]) => { for (let i = 0; i < 5; i++) { const l = L[i]; if (l) { U.uLampP.value[i].set(...l[0]); U.uLampC.value[i].set(...l[1]); U.uLampR.value[i] = l[2]; } else { U.uLampP.value[i].set(0, -99, 0); U.uLampC.value[i].set(0, 0, 0); } } };
/** PHONG CÁCH SÁNG (anh Huy 20/11): ban ngày trong nhà – nắng dịu + ambient cao, bóng nhạt, đèn trần trắng ấm */
const sangLook = (k = 1, a = 1) => { setLook("day"); U.uSun.value.set(0.62 * k, 0.6 * k, 0.55 * k); U.uAmbHi.value.set(1.0 * a, 0.98 * a, 0.95 * a); U.uAmbLo.value.set(0.74 * a, 0.72 * a, 0.7 * a); U.uSat.value = 1.04; };
/** vệt nắng qua cửa sổ trên sàn/tường (cộng sáng, không viền mực) */
function nang(g: THREE.Group, x: number, y: number, z: number, w: number, d: number, rx = -Math.PI / 2, ry = 0, a = 0.32) {
  const [c, cx] = cvs(256, 256); const gr = cx.createRadialGradient(128, 128, 20, 128, 128, 128); gr.addColorStop(0, "rgba(255,236,190,1)"); gr.addColorStop(1, "rgba(255,236,190,0)"); cx.fillStyle = gr; cx.fillRect(0, 0, 256, 256);
  cx.globalCompositeOperation = "destination-out"; cx.fillStyle = "#000"; cx.fillRect(124, 0, 8, 256); cx.fillRect(0, 124, 256, 8);
  const m = new THREE.Mesh(new THREE.PlaneGeometry(w, d), new THREE.MeshBasicMaterial({ map: ctex(c), transparent: true, opacity: a, blending: THREE.AdditiveBlending, depthWrite: false }));
  m.rotation.set(rx, ry, 0, "YXZ"); m.position.set(x, y, z); m.layers.set(NOINK); m.renderOrder = 2; g.add(m); }
const sh = (g: THREE.Group) => { g.traverse((o) => { const m = o as THREE.Mesh; if (m.isMesh && m.layers.mask !== 1 << NOINK) { m.receiveShadow = true; } }); return g; };

/** tường sơn sạch (căn hộ/văn phòng): màu + loang nhẹ + len chân tường */
function cleanWall(wm: number, hm: number, base: string, skirt: string, seed: number) {
  const PX = 120, W = Math.round(wm * PX), H = Math.round(hm * PX), r = rng(seed); const [c, x] = cvs(W, H); x.fillStyle = base; x.fillRect(0, 0, W, H);
  grime(x, W, H, r, 120, "rgba(255,255,255,A)", 30, 140, 0.06); grime(x, W, H, r, 80, "rgba(80,60,40,A)", 20, 100, 0.05);
  x.fillStyle = skirt; x.fillRect(0, H - 14, W, 14); x.fillStyle = "rgba(0,0,0,.25)"; x.fillRect(0, H - 15, W, 2); return ctex(c);
}
function woodFloor(wm: number, dm: number, seed: number, base = "#9a6a42", light = false) {
  const PX = 110, W = Math.round(wm * PX), H = Math.round(dm * PX), r = rng(seed); const [c, x] = cvs(W, H); x.fillStyle = base; x.fillRect(0, 0, W, H);
  for (let y = 0; y < H; y += 22) { let xx = -r() * 200; while (xx < W) { const len = 150 + r() * 160; const k = 0.82 + r() * 0.3; x.fillStyle = light ? `rgba(${Math.round(225 * k)},${Math.round(190 * k)},${Math.round(150 * k)},.45)` : `rgba(${Math.round(150 * k)},${Math.round(100 * k)},${Math.round(60 * k)},.5)`; x.fillRect(xx, y, len, 21); x.fillStyle = light ? "rgba(120,90,60,.35)" : "rgba(40,25,15,.5)"; x.fillRect(xx, y + 21, len, 1.5); x.fillRect(xx + len, y, 1.5, 22); xx += len; } }
  grime(x, W, H, r, 60, "rgba(255,230,190,A)", 30, 120, 0.08); return ctex(c);
}
function tiles(wm: number, dm: number, seed: number, a = "#d9d6cf", b = "#c9c5bc", cell = 60) {
  const PX = 100, W = Math.round(wm * PX), H = Math.round(dm * PX), r = rng(seed); const [c, x] = cvs(W, H);
  for (let y = 0; y < H; y += cell) for (let xx = 0; xx < W; xx += cell) { x.fillStyle = ((xx + y) / cell) % 2 ? a : b; x.fillRect(xx, y, cell, cell); }
  x.strokeStyle = "rgba(0,0,0,.18)"; x.lineWidth = 2; for (let y = 0; y < H; y += cell) { x.beginPath(); x.moveTo(0, y); x.lineTo(W, y); x.stroke(); } for (let xx = 0; xx < W; xx += cell) { x.beginPath(); x.moveTo(xx, 0); x.lineTo(xx, H); x.stroke(); }
  grime(x, W, H, r, 80, "rgba(60,50,40,A)", 20, 90, 0.07); return ctex(c);
}
function room(g: THREE.Group, W: number, D: number, H: number, wall: THREE.Texture, side: THREE.Texture, floor: THREE.Texture, ceil = "#e8e2d6") {
  const fl = mesh(new THREE.PlaneGeometry(W, D), tm("#ffffff", floor), 0, 0, -3 + D / 2, false); fl.rotation.x = -Math.PI / 2; g.add(fl);
  g.add(plane(W, H, wall, 0, H / 2, -3)); for (const s of [-1, 1]) g.add(plane(D, H, side, s * W / 2, H / 2, -3 + D / 2, -s * Math.PI / 2));
  const c = mesh(new THREE.PlaneGeometry(W, D), tm(ceil), 0, H, -3 + D / 2, false); c.rotation.x = Math.PI / 2; g.add(c);
  for (const [w, d, x, z] of [[W, 0.8, 0, -2.75], [0.8, D, -W / 2 + 0.25, -3 + D / 2], [0.8, D, W / 2 - 0.25, -3 + D / 2]] as number[][]) { const b = blob(w * 1.1, d * 1.1, 0.35); b.position.set(x, 0.01, z); g.add(b); }
}
function cityWin(w: number, h: number, night: boolean, seed: number) {
  const [c, x] = cvs(512, Math.round(512 * h / w)), r = rng(seed), H = c.height; const sky = x.createLinearGradient(0, 0, 0, H); sky.addColorStop(0, night ? "#0b1230" : "#8fc4ef"); sky.addColorStop(1, night ? "#3a2c5a" : "#dcefff"); x.fillStyle = sky; x.fillRect(0, 0, 512, H);
  for (let i = 0; i < 30; i++) { const bw = 20 + r() * 50, bh = H * (0.25 + r() * 0.65), bxx = r() * 512; x.fillStyle = night ? "#161c36" : "#9aa8b8"; x.fillRect(bxx, H - bh, bw, bh);
    for (let yy = H - bh + 6; yy < H - 6; yy += 10) for (let xx = bxx + 4; xx < bxx + bw - 4; xx += 9) if (r() < (night ? 0.45 : 0.2)) { x.fillStyle = night ? "#ffd27a" : "#c9dff0"; x.fillRect(xx, yy, 4, 5); } }
  const p = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: ctex(c) })); p.layers.set(NOINK); return p;
}
/** bảng điện chứng khoán: mã, giá, +/-%, xanh/đỏ/tím/vàng, kiểu bảng giá */
export function bangDien(w = 1024, h = 512, seed = 3, mood: "do" | "xanh" = "do") {
  const [c, x] = cvs(w, h), r = rng(seed); x.fillStyle = "#05070c"; x.fillRect(0, 0, w, h);
  const MA = ["VNM", "HPG", "VCB", "FPT", "MWG", "SSI", "VHM", "TCB", "MBB", "GAS", "MSN", "VIC", "ACB", "STB", "VPB", "DGC", "PNJ", "REE", "GMD", "POW"];
  x.fillStyle = "#f2d36b"; x.font = `900 ${h * 0.07}px ${F}`; x.fillText(mood === "do" ? "VN-INDEX 1.689,62  ▼ 13,39 (-0,79%)" : "VN-INDEX 1.712,40  ▲ 9,38 (+0,55%)", 16, h * 0.09);
  x.fillStyle = mood === "do" ? "#ff4d5e" : "#2bd17e"; x.fillRect(16, h * 0.115, w - 32, 3);
  const cols = 4, rows = 5, cw = (w - 32) / cols, rh = (h * 0.84) / rows;
  for (let i = 0; i < cols * rows; i++) { const cxp = 16 + (i % cols) * cw, cyp = h * 0.15 + Math.floor(i / cols) * rh; const up = mood === "do" ? r() < 0.22 : r() < 0.7, zero = r() < 0.1;
    const col = zero ? "#f2d36b" : up ? (r() < 0.1 ? "#d26bff" : "#2bd17e") : (r() < 0.1 ? "#4fd8ff" : "#ff4d5e");
    x.fillStyle = "rgba(255,255,255,.04)"; x.fillRect(cxp + 2, cyp + 2, cw - 4, rh - 4);
    x.fillStyle = "#e9eef5"; x.font = `800 ${rh * 0.32}px ${F}`; x.fillText(MA[i % MA.length], cxp + 10, cyp + rh * 0.42);
    const p = (20 + r() * 120).toFixed(2).replace(".", ","), pc = ((zero ? 0 : up ? 1 : -1) * (r() * 6.9)).toFixed(2).replace(".", ",");
    x.fillStyle = col; x.fillText(p, cxp + cw * 0.5, cyp + rh * 0.42); x.font = `700 ${rh * 0.26}px ${F}`; x.fillText((up && !zero ? "+" : "") + pc + "%", cxp + cw * 0.5, cyp + rh * 0.82); }
  return ctex(c);
}
const gl = (t: THREE.Texture, w: number, h: number, k = 1.4) => { const m = new THREE.MeshBasicMaterial({ map: t, color: new THREE.Color(k, k, k) }); const p = new THREE.Mesh(new THREE.PlaneGeometry(w, h), m); p.layers.set(NOINK); return p; };
function phone(g: THREE.Group, x: number, y: number, z: number) { const p = bx(0.08, 0.008, 0.16, tm("#16171b"), x, y, z); g.add(p); }

// ======================= SẠP VẢI CHỢ =======================
export function buildSapVai() {
  sangLook(1.5, 1.25); const g = new THREE.Group(), r = rng(51);
  lamps([[[0, 3.2, 0.5], [0.55, 0.52, 0.45], 6.5], [[-3.6, 3.2, -0.5], [0.45, 0.43, 0.38], 5.5], [[3.6, 3.2, -0.5], [0.45, 0.43, 0.38], 5.5], [[0, 3.0, 3.5], [0.4, 0.38, 0.34], 6]]);
  room(g, 12, 9, 4.2, wallTex(12, 4.2, 81, "#f1e9cf", 0.25), wallTex(9, 4.2, 82, "#eee4c6", 0.25), floorTex(12, 9, 83, [[6, 4, 0.25], [3, 6, 0.2]]), "#c9ced4");
  nang(g, 1.2, 0.012, 1.2, 4.5, 3.0); nang(g, -3.5, 0.012, 1.6, 3.5, 2.6, -Math.PI / 2, 0, 0.25);
  // mái tôn + kèo sắt
  for (let k = 0; k < 6; k++) g.add(bx(12, 0.1, 0.1, tm("#5a5c60"), 0, 4.05, -2.8 + k * 1.6));
  const roof = corrugated(12, 9, tm("#b8c4cc", metalTex(61, "#b8c4cc", 0.3), { side: THREE.DoubleSide })); roof.position.set(0, 4.15, 1.5); roof.rotation.x = Math.PI / 2; g.add(roof);
  // vải: cây vải cuộn (trụ có hoa văn) + xấp vải gấp (hộp sọc) + vải treo
  const PC = new Map<string, THREE.Texture>();
  const pat = (seed0: number, base: string) => { const seed = seed0 % 5, kk = base + seed; if (PC.has(kk)) return PC.get(kk)!; const [c, x] = cvs(128, 128), rr = rng(seed + 1); x.fillStyle = base; x.fillRect(0, 0, 128, 128); const k = Math.floor(rr() * 4);
    if (k === 0) for (let i = 0; i < 40; i++) { x.fillStyle = `hsla(${rr() * 360},70%,${55 + rr() * 30}%,.9)`; x.beginPath(); x.arc(rr() * 128, rr() * 128, 3 + rr() * 6, 0, 7); x.fill(); }
    else if (k === 1) for (let i = 0; i < 128; i += 16) { x.fillStyle = "rgba(255,255,255,.35)"; x.fillRect(i, 0, 6, 128); }
    else if (k === 2) { for (let i = 0; i < 128; i += 16) { x.fillStyle = "rgba(0,0,0,.18)"; x.fillRect(i, 0, 8, 128); x.fillRect(0, i, 128, 8); } }
    else for (let i = 0; i < 20; i++) { x.strokeStyle = "rgba(255,240,200,.6)"; x.lineWidth = 2; x.beginPath(); x.arc(rr() * 128, rr() * 128, 6 + rr() * 10, 0, 4); x.stroke(); }
    const t = ctex(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; PC.set(kk, t); return t; };
  const PM = new Map<THREE.Texture, THREE.Material>(); const pm = (t: THREE.Texture, ds = false) => { const k2 = ds ? 1 : 0; if (!PM.has(t)) PM.set(t, tm("#ffffff", t)); if (!ds) return PM.get(t)!; return tm("#ffffff", t, { side: THREE.DoubleSide }); };
  const COL = ["#c8202f", "#2b6cc4", "#f2c230", "#3f8a3a", "#e86a92", "#7a3e8a", "#f4f1e6", "#1f2a44", "#e07a2a", "#2fa39a"];
  const stall = (x0: number, z0: number, w: number, seed: number, main = false) => { const rr = rng(seed);
    g.add(bx(w, 0.6, 1.4, tm("#ffffff", woodTex(seed, "#7a5236")), x0, 0.3, z0)); g.add(bx(w + 0.04, 0.04, 1.44, tm("#5a3b2a"), x0, 0.61, z0));
    // cuộn vải đứng phía sau
    for (let k = 0; k < Math.floor(w / 0.22); k++) { const col = COL[Math.floor(rr() * COL.length)]; const h = 1.3 + rr() * 0.5; const roll = cy(0.1, 0.1, h, pm(pat(seed * 10 + k, col)), x0 - w / 2 + 0.12 + k * 0.22, 0.62 + h / 2, z0 - 0.55, 14); roll.rotation.z = (rr() - 0.5) * 0.12; g.add(roll); }
    // xấp vải gấp trên mặt sạp
    for (let k = 0; k < 6; k++) for (let j = 0; j < 2 + Math.floor(rr() * 3); j++) { const col = COL[Math.floor(rr() * COL.length)]; g.add(bx(0.38, 0.08, 0.3, pm(pat(seed * 100 + k * 7 + j, col)), x0 - w / 2 + 0.3 + (k % 3) * 0.45, 0.66 + j * 0.085, z0 + (k < 3 ? -0.1 : 0.35))); }
    // vải treo trên thanh ngang
    g.add(cy(0.02, 0.02, w, tm("#9aa3ad"), x0, 2.5, z0 - 0.75, 6).rotateZ(Math.PI / 2)); for (const s of [-1, 1]) g.add(cy(0.025, 0.025, 2.5, tm("#9aa3ad"), x0 + s * w / 2, 1.25, z0 - 0.75, 6));
    for (let k = 0; k < Math.floor(w / 0.5); k++) { const p = mesh(new THREE.PlaneGeometry(0.46, 1.1), pm(pat(seed * 1000 + k, COL[Math.floor(rr() * COL.length)])), x0 - w / 2 + 0.28 + k * 0.5, 1.93, z0 - 0.72, false); p.rotation.y = (rr() - 0.5) * 0.3; g.add(p); }
    g.add(plane(0.9, 0.32, signTex(main ? "VẢI HẠNH" : ["VẢI LỤA", "VẢI KATE", "ĐỒ BỘ", "VẢI THUN"][seed % 4], main ? "Sạp 112 · Lụa · Kate · Thun" : "Giá sỉ · lẻ", 0.9, 0.32, main ? "#c8202f" : "#1f5fae", "#ffffff", seed), x0, 2.78, z0 - 0.73));
    if (main) { phone(g, x0 + 0.5, 0.63, z0 + 0.45); g.add(bx(0.14, 0.03, 0.2, tm("#2b2b30"), x0 + 0.8, 0.63, z0 + 0.4)); put(g, "cardboard_box_01", x0 - w / 2 - 0.35, 0, z0 + 0.1, 0.3, { h: 0.45 }); put(g, "wicker_basket_01", x0 + w / 2 + 0.3, 0, z0 + 0.3, 0, { h: 0.3 }); } };
  stall(0, -1.6, 2.6, 7, true); stall(-3.6, -1.6, 2.4, 3); stall(3.6, -1.6, 2.4, 5);
  stall(-4.2, 3.6, 2.4, 9); stall(4.2, 3.6, 2.4, 11);
  // ghế nhựa, quạt cây, đèn tuýp, dây điện
  { const st = plasticStool("#2b6cc4"); st.position.set(0.9, 0, -0.4); g.add(st); }
  for (const x of [-3.6, 0, 3.6]) { const tube = bx(1.2, 0.05, 0.08, glow(2.2, 2.3, 2.4), x, 3.4, -1.0); g.add(tube); g.add(wire([x, 4.05, -1.0], [x, 3.45, -1.0], 0, tm("#111"), 0.006)); }
  g.add(wire([-6, 3.7, -2.9], [6, 3.6, -2.9], 0.15, tm("#141414")));
  put(g, "plastic_monobloc_chair_01", -1.6, 0, 0.3, 0.6, { h: 0.82 });
  gopTinh(g); return { g: sh(g), cho: { ngoi: [0.9, 0, -0.4] as V3, dung: [-0.6, 0, 0.2] as V3 } };
}

// ======================= PHÒNG KHÁCH CĂN HỘ (tối) =======================
export function buildPhongKhach(night = true) {
  sangLook(0.7, 0.78); night = false;
  lamps([[[1.8, 2.4, -1.6], [0.5, 0.45, 0.35], 4.5], [[0, 2.9, 0.4], [0.5, 0.48, 0.42], 6.5], [[-2.2, 1.6, -2.4], [0.55, 0.52, 0.45], 4.0]]);
  const g = new THREE.Group();
  room(g, 10, 8, 3.0, cleanWall(10, 3.0, "#f7f0e2", "#c9a882", 3), cleanWall(8, 3.0, "#e4efe6", "#c9a882", 4), woodFloor(10, 8, 5, "#d8b98f", true), "#fbf8f2");
  nang(g, -1.4, 0.012, -1.2, 3.4, 2.4); nang(g, -2.2, 1.0, -2.96, 3.6, 1.6, 0, 0, 0.12);
  // cửa sổ lớn nhìn thành phố đêm + rèm
  const win = cityWin(3.2, 1.6, night, 9); win.position.set(-2.2, 1.65, -2.98); g.add(win);
  for (const x of [-2.2 - 1.62, -2.2 + 1.62]) g.add(bx(0.06, 1.7, 0.06, tm("#f4f4f2"), x, 1.65, -2.95)); g.add(bx(3.3, 0.06, 0.06, tm("#f4f4f2"), -2.2, 2.5, -2.95)); g.add(bx(3.3, 0.06, 0.06, tm("#f4f4f2"), -2.2, 0.8, -2.95));
  for (const x of [-4.1, -0.3]) { const cur = mesh(new THREE.BoxGeometry(0.5, 2.5, 0.08), tm("#efe2c2"), x, 1.6, -2.9); g.add(cur); for (let k = 0; k < 4; k++) g.add(bx(0.02, 2.5, 0.1, tm("#dccba4"), x - 0.18 + k * 0.12, 1.6, -2.88)); }
  // sofa + gối + bàn trà + thảm
  put(g, "sofa_03", 1.0, 0, -2.25, 0, { h: 0.9 }); put(g, "throw_pillows_01", 0.3, 0.45, -2.25, 0, { h: 0.4, blob: 0 });
  { const [c, x] = cvs(512, 320); x.fillStyle = "#7a2e24"; x.fillRect(0, 0, 512, 320); x.strokeStyle = "#e8c36a"; x.lineWidth = 10; x.strokeRect(20, 20, 472, 280); x.strokeStyle = "#f4f1e6"; x.lineWidth = 4; x.strokeRect(40, 40, 432, 240);
    for (let i = 0; i < 9; i++) { x.fillStyle = "rgba(232,195,106,.6)"; x.beginPath(); x.arc(70 + i * 46, 160, 12, 0, 7); x.fill(); } const rug = mesh(new THREE.PlaneGeometry(3.0, 1.9), tm("#ffffff", ctex(c)), 0.9, 0.006, -0.9, false); rug.rotation.x = -Math.PI / 2; g.add(rug); }
  put(g, "modern_coffee_table_01", 0.9, 0, -1.0, Math.PI / 2, { h: 0.42 }); put(g, "tea_set_01", 0.8, 0.42, -1.0, 0, { h: 0.16, blob: 0 });
  // kệ TV tường trái + TV (màn hình bảng điện)
  g.add(bx(0.45, 0.5, 2.0, tm("#ffffff", woodTex(12, "#5a3b2a")), -4.75, 0.25, 0.4)); const tv = bx(0.06, 0.9, 1.6, tm("#111"), -4.9, 1.45, 0.4); g.add(tv);
  const scr = gl(bangDien(768, 432, 4, "do"), 1.5, 0.84, 1.1); scr.position.set(-4.86, 1.45, 0.4); scr.rotation.y = Math.PI / 2; g.add(scr);
  // tủ sách, cây, tranh, đồng hồ, đèn trần, đèn bàn
  put(g, "wooden_bookshelf_worn", 3.9, 0, -2.6, 0, { h: 2.0 }); put(g, "potted_plant_02", -0.4, 0, -2.4, 0, { h: 1.0 }); put(g, "side_table_01", 2.65, 0, -2.3, 0, { h: 0.5 });
  { const lamp = cy(0.16, 0.22, 0.3, tm("#f2e6c8"), 2.65, 0.85, -2.3, 18); g.add(lamp); g.add(cy(0.02, 0.02, 0.35, tm("#8a6a48"), 2.65, 0.6, -2.3, 6)); const b = new THREE.Mesh(new THREE.SphereGeometry(0.07, 12, 8), glow(3, 2.4, 1.4)); b.position.set(2.65, 0.85, -2.3); g.add(b); }
  { const [c, x] = cvs(384, 256); const gr = x.createLinearGradient(0, 0, 0, 256); gr.addColorStop(0, "#f2b46a"); gr.addColorStop(0.55, "#e9d39a"); gr.addColorStop(0.56, "#4f7a5a"); gr.addColorStop(1, "#2f4f3c"); x.fillStyle = gr; x.fillRect(0, 0, 384, 256);
    x.fillStyle = "#fff2c8"; x.beginPath(); x.arc(250, 120, 34, 0, 7); x.fill(); x.fillStyle = "#3a5a46"; x.beginPath(); x.moveTo(0, 170); x.lineTo(90, 100); x.lineTo(170, 160); x.lineTo(260, 110); x.lineTo(384, 170); x.lineTo(384, 256); x.lineTo(0, 256); x.fill();
    x.strokeStyle = "#6a4a2a"; x.lineWidth = 18; x.strokeRect(9, 9, 366, 238); g.add(plane(0.9, 0.6, ctex(c), 1.0, 1.85, -2.97)); } put(g, "wall_clock", 3.0, 2.3, -2.97, 0, { h: 0.32, blob: 0 }); put(g, "modern_ceiling_lamp_01", 0.6, 2.4, -0.6, 0, { h: 0.5, blob: 0 });
  g.add(plane(0.7, 0.5, paperTex([["LỊCH 11/2026", "#c8202f", 44], ["19", "#c8202f", 150]], 0.7, 0.5, "#ffffff"), 4.98, 1.7, 0.6, -Math.PI / 2));
  gopTinh(g); return { g: sh(g), cho: { sofaTrai: [0.25, 0, -1.95] as V3, sofaPhai: [1.7, 0, -1.95] as V3, dung: [-1.2, 0, -0.3] as V3 } };
}

// ======================= PHÒNG GIAO DỊCH / VĂN PHÒNG QUỸ (bảng điện lớn) =======================
export function buildVanPhong() {
  sangLook();
  lamps([[[0, 1.8, -2.2], [0.3, 0.22, 0.2], 4.0], [[-2.5, 3.1, 0], [0.42, 0.42, 0.4], 6], [[2.5, 3.1, 0], [0.42, 0.42, 0.4], 6], [[4.8, 1.8, 0.6], [0.45, 0.42, 0.36], 5]]);
  const g = new THREE.Group();
  room(g, 11, 8, 3.3, cleanWall(11, 3.3, "#f4f1ea", "#9aa6b4", 21), cleanWall(8, 3.3, "#e3edf5", "#9aa6b4", 22), tiles(11, 8, 23, "#e8e6e1", "#dcdad4", 70), "#fbfbf9");
  nang(g, 3.6, 0.012, 0.6, 3.0, 3.4, -Math.PI / 2, 0, 0.28);
  // bảng điện lớn tường sau + chữ phòng giao dịch
  g.add(bx(6.4, 2.1, 0.12, tm("#111317"), 0, 1.75, -2.95)); const bd = gl(bangDien(1280, 420, 7, "do"), 6.2, 1.95, 1.25); bd.position.set(0, 1.75, -2.88); g.add(bd);
  g.add(plane(3.2, 0.4, signTex("PHÒNG GIAO DỊCH", "Quỹ đầu tư · Tầng 12", 3.2, 0.4, "#13204a", "#f2d36b", 4), 0, 3.0, -2.9));
  // dãy bàn + màn hình đôi + ghế + laptop, giấy tờ
  const desk = (x: number, z: number, ry: number, seed: number) => { put(g, "metal_office_desk", x, 0, z, ry, { h: 0.76 });
    for (const dx of [-0.32, 0.32]) { const sc = bx(0.56, 0.36, 0.03, tm("#16171b"), x + dx * Math.cos(ry), 1.04, z - 0.18 - dx * Math.sin(ry)); sc.rotation.y = ry; g.add(sc);
      const s = gl(bangDien(384, 256, seed + dx * 10, "do"), 0.52, 0.32, 1.15); s.position.set(x + dx * Math.cos(ry) + 0.02 * Math.sin(ry), 1.04, z - 0.16 - dx * Math.sin(ry) + 0.02 * Math.cos(ry)); s.rotation.y = ry; g.add(s);
      g.add(bx(0.04, 0.2, 0.04, tm("#2a2b30"), x + dx * Math.cos(ry), 0.86, z - 0.2 - dx * Math.sin(ry))); }
    put(g, "SchoolChair_01", x, 0, z + 0.65, ry + Math.PI, { h: 0.85 }); put(g, "binder_notebook", x + 0.6, 0.76, z + 0.1, 0.4, { h: 0.04, blob: 0 }); };
  desk(-3.0, -0.6, 0, 31); desk(3.0, -0.6, 0, 37); desk(-3.0, 2.2, 0, 41); desk(3.0, 2.2, 0, 43);
  // cửa sổ rèm lá + cây + kệ hồ sơ + đèn tuýp + camera
  const win = cityWin(2.6, 1.6, false, 13); win.position.set(5.48, 1.7, 0.6); win.rotation.y = -Math.PI / 2; g.add(win); for (let k = 0; k < 12; k++) g.add(bx(0.03, 0.04, 2.6, tm("#e8ecf0"), 5.45, 0.95 + k * 0.13, 0.6));
  put(g, "potted_plant_02", -5.0, 0, -2.4, 0, { h: 1.1 }); put(g, "steel_frame_shelves_02", -5.15, 0, 0.6, Math.PI / 2, { h: 2.0 }); for (const x of [-3, 0, 3]) g.add(bx(1.2, 0.05, 0.25, glow(2.0, 2.1, 2.2), x, 3.25, 0.2));
  put(g, "security_camera_01", 5.2, 2.9, -2.7, -2.4, { h: 0.25, blob: 0 }); put(g, "wall_clock", -2.6, 2.75, -2.97, 0, { h: 0.3, blob: 0 });
  gopTinh(g); return { g: sh(g), cho: { banTrai: [-3.0, 0, 0.1] as V3, dung: [0.4, 0, 0.6] as V3 } };
}

// ======================= QUẦY NGÂN HÀNG =======================
export function buildNganHang() {
  sangLook(0.55, 0.66);
  lamps([[[0, 3.0, -1.4], [0.42, 0.42, 0.38], 6], [[-3, 3.0, 1], [0.36, 0.36, 0.34], 6], [[3, 3.0, 1], [0.36, 0.36, 0.34], 6]]);
  const g = new THREE.Group();
  room(g, 11, 8, 3.4, cleanWall(11, 3.4, "#e9e4d8", "#1f3d6a", 61), cleanWall(8, 3.4, "#e2ddd0", "#1f3d6a", 62), tiles(11, 8, 63, "#e9e6df", "#d6d2c8", 80), "#f4f2ee");
  g.add(plane(4.0, 0.55, signTex("NGÂN HÀNG PHỐ", "Giao dịch · Tiết kiệm · Cho vay", 4.0, 0.55, "#1f3d6a", "#f2d36b", 7), 0, 2.9, -2.95));
  // quầy dài + kính ngăn + số quầy + máy đếm tiền
  // 20/11: quầy thấp 0,85 m để thấy rõ nửa người nhân viên đứng sau quầy (đặt nhân viên y = 0,45, z ≈ -2,15)
  g.add(bx(7.6, 0.85, 0.7, tm("#ffffff", woodTex(64, "#b88a5e")), 0, 0.425, -1.6)); g.add(bx(7.7, 0.05, 0.8, tm("#e8e4dc"), 0, 0.87, -1.6));
  g.add(bx(7.6, 0.45, 0.04, tm("#e8e4dc"), 0, 0.225, -2.6)); g.add(bx(7.6, 0.04, 0.8, tm("#d6d2c8"), 0, 0.44, -2.25));
  const glass = new THREE.MeshPhysicalMaterial({ color: "#cfe3ea", transparent: true, opacity: 0.25, roughness: 0.05 });
  for (let k = 0; k < 4; k++) { const x = -2.85 + k * 1.9; const pnl = new THREE.Mesh(new THREE.PlaneGeometry(1.7, 0.75), glass); pnl.position.set(x, 1.3, -1.3); pnl.layers.set(NOINK); g.add(pnl);
    g.add(bx(0.04, 0.8, 0.04, tm("#9aa3ad"), x - 0.86, 1.3, -1.3)); g.add(plane(0.36, 0.28, paperTex([["QUẦY", "#ffffff", 50], [String(k + 1), "#f2d36b", 150]], 0.36, 0.28, "#1f3d6a"), x, 2.05, -1.32));
    put(g, "CashRegister_01", x + 0.55, 0.9, -1.75, Math.PI, { h: 0.22, blob: 0 }); }
  g.add(bx(7.7, 0.04, 0.04, tm("#9aa3ad"), 0, 1.7, -1.3));
  // bảng số thứ tự phát sáng + ghế chờ + cây + biển thông tin lãi suất
  g.add(bx(1.5, 0.5, 0.08, tm("#111"), 3.8, 2.3, -2.9)); { const [c, x] = cvs(384, 128); x.fillStyle = "#050505"; x.fillRect(0, 0, 384, 128); x.fillStyle = "#ff3b30"; x.font = `900 64px ${F}`; x.fillText("1024 → 3", 20, 88); const s = gl(ctex(c), 1.4, 0.44, 1.5); s.position.set(3.8, 2.3, -2.85); g.add(s); }
  g.add(plane(1.2, 1.5, paperTex([["LÃI SUẤT", "#c8202f", 60], ["TIẾT KIỆM", "#1f3d6a", 48], ["1 tháng ... 2,4%", "#222", 34], ["6 tháng ... 4,2%", "#222", 34], ["12 tháng .. 5,1%", "#222", 34], ["(minh hoạ)", "#888", 26]], 1.2, 1.5, "#fffdf3"), -4.2, 1.6, -2.95));
  for (let k = 0; k < 5; k++) put(g, "dining_chair_02", -3.2 + k * 0.6, 0, 2.6, Math.PI, { h: 0.9 });
  put(g, "potted_plant_02", 4.8, 0, 2.4, 0, { h: 1.0 }); put(g, "potted_plant_02", -5.0, 0, -0.4, 0, { h: 1.0 }); put(g, "security_camera_01", -5.2, 3.0, -2.7, 2.4, { h: 0.25, blob: 0 });
  for (const x of [-3, 0, 3]) g.add(bx(1.2, 0.05, 0.25, glow(2.0, 2.1, 2.2), x, 3.35, 0.2));
  gopTinh(g); return { g: sh(g), cho: { nhanVien: [0, 0.45, -2.15] as V3, khach: [0.1, 0, -0.55] as V3 } };
}

// ======================= XƯỞNG GỖ NHỎ (của anh Tín, 20/11) =======================
// đứng giữa [0.2,0,0.4]; bàn giấy: ngồi [1.7,0,-0.25] (ghế sau lưng), đứng cạnh bàn [0.9,0,-0.4]; bàn thợ trái x≈-2
export function buildXuongGo() {
  sangLook(0.85, 0.92);
  lamps([[[0, 3.1, -0.5], [0.5, 0.48, 0.42], 6.5], [[-2.6, 3.1, -1.2], [0.42, 0.4, 0.34], 5], [[2.6, 3.1, -0.8], [0.42, 0.4, 0.34], 5]]);
  const g = new THREE.Group(), r = rng(77);
  room(g, 11, 8, 3.5, cleanWall(11, 3.5, "#efe2c6", "#8a6a48", 71), cleanWall(8, 3.5, "#e9dcc0", "#8a6a48", 72), tiles(11, 8, 73, "#d2c9b8", "#c8bead", 90), "#d8d2c6");
  nang(g, 3.2, 1.3, -2.96, 2.4, 1.5, 0, 0, 0.12);
  for (let k = 0; k < 5; k++) g.add(bx(11, 0.12, 0.12, tm("#6a4a32"), 0, 3.38, -2.6 + k * 1.7));
  g.add(plane(3.0, 0.55, signTex("XƯỞNG GỖ TÍN", "Bàn ghế · Tủ kệ · Nhận đặt hàng", 3.0, 0.55, "#5a3b2a", "#f2d36b", 11), 0, 2.85, -2.95));
  // bàn thợ + ván đang làm + dụng cụ
  put(g, "WoodenTable_01", -2.1, 0, -1.6, 0, { h: 0.86 }); g.add(bx(1.5, 0.05, 0.4, tm("#ffffff", woodTex(74, "#c9965e")), -2.1, 0.9, -1.6));
  g.add(bx(0.3, 0.06, 0.08, tm("#c8202f"), -1.6, 0.95, -1.45)); g.add(bx(0.04, 0.04, 0.35, tm("#9aa3ad"), -2.6, 0.94, -1.5));
  // đống ván gỗ xếp tầng (phải, sát tường) + ván dựng tường (trái)
  for (let k = 0; k < 9; k++) { const y = 0.06 + k * 0.075; for (let j = 0; j < 3; j++) g.add(bx(2.6, 0.07, 0.28, tm("#ffffff", woodTex(80 + ((k + j) % 4), ["#b07a48", "#c9965e", "#9a6a3e", "#d1a26c"][(k + j) % 4])), 3.4, y, -2.55 + j * 0.31)); }
  for (let k = 0; k < 7; k++) { const p = bx(0.22, 2.4, 0.04, tm("#ffffff", woodTex(90 + (k % 3), ["#c9965e", "#a8743e", "#d6ad78"][k % 3])), -4.6 + k * 0.26, 1.15, -2.82); p.rotation.x = -0.12; g.add(p); }
  put(g, "wooden_crate_02", -3.9, 0, 0.2, 0.3, { h: 0.55 }); put(g, "wooden_crate_02", -3.85, 0.55, 0.15, -0.2, { h: 0.5 }); put(g, "steel_frame_shelves_02", 5.1, 0, 0.4, -Math.PI / 2, { h: 2.0 });
  // ghế gỗ thành phẩm chờ giao
  for (const [x, z, ry] of [[-0.9, -2.3, 0.2], [-0.3, -2.4, -0.3]] as number[][]) put(g, "dining_chair_02", x, 0, z, ry, { h: 0.9 });
  // bàn giấy: hoá đơn, giấy báo ngân hàng, máy tính
  put(g, "metal_office_desk", 1.7, 0, -1.0, 0, { h: 0.76 }); put(g, "SchoolChair_01", 1.7, 0, -0.35, Math.PI, { h: 0.85 });
  for (let k = 0; k < 7; k++) { const pp = plane(0.21, 0.29, paperTex([[k % 3 ? "HOÁ ĐƠN" : "THÔNG BÁO", k % 3 ? "#1f3d6a" : "#c8202f", 46], ["...........", "#888", 40], ["...........", "#888", 40]], 0.21, 0.29, "#fffdf3"), 1.25 + (k % 4) * 0.2 + r() * 0.05, 0.765 + k * 0.002, -1.05 + Math.floor(k / 4) * 0.22); pp.rotation.set(-Math.PI / 2, 0, (r() - 0.5) * 0.6); g.add(pp); }
  put(g, "classic_laptop", 2.25, 0.76, -1.15, 0.2, { h: 0.25, blob: 0 }); put(g, "stationery_supplies", 2.4, 0.76, -0.85, 0, { h: 0.12, blob: 0 });
  g.add(plane(0.7, 0.5, paperTex([["LỊCH 11/2026", "#c8202f", 44], ["45", "#c8202f", 150]], 0.7, 0.5, "#ffffff"), 1.7, 1.75, -2.97));
  g.add(plane(0.9, 0.6, paperTex([["ĐƠN HÀNG", "#1f3d6a", 52], ["Tủ 12 bộ – HUỶ", "#c8202f", 36], ["Bàn 30 bộ – HUỶ", "#c8202f", 36], ["Ghế 40 cái – chờ", "#222", 36]], 0.9, 0.6, "#fffdf3"), 2.8, 1.6, -2.97));
  // mạt cưa trên sàn + đèn tuýp
  for (const x of [-2.6, 0, 2.6]) g.add(bx(1.2, 0.05, 0.12, glow(2.1, 2.1, 2.0), x, 3.2, -0.6));
  gopTinh(g); return { g: sh(g), cho: { dung: [0.2, 0, 0.4] as V3, ngoiBan: [1.7, 0, -0.25] as V3 } };
}

// ======================= CÀ PHÊ VỈA HÈ (phố ban ngày) =======================
export const CAFE_X = -26.5;   // giữa 2 cây vỉa hè (x≈-31 và x≈-21), xa quán đông khách có sẵn của phố để không có thân cây che bàn
export function buildCafeVH() {
  setLook("day"); const st = buildStreet(false); const g = new THREE.Group(); g.add(st.g); const r = rng(91);
  const X = CAFE_X, Z = 5.2, Y = 0.15;
  for (const [x, z] of [[X - 1.2, Z], [X + 0.6, Z + 0.3], [X + 2.3, Z - 0.1]] as [number, number][]) {
    g.add(bx(0.6, 0.03, 0.45, tm("#c9a46a"), x, Y + 0.45, z)); for (const [a, b] of [[-0.25, -0.18], [0.25, -0.18], [-0.25, 0.18], [0.25, 0.18]]) g.add(bx(0.03, 0.45, 0.03, tm("#6a4a32"), x + a, Y + 0.22, z + b));
    for (const s of [-1, 1]) { const stl = plasticStool(r() < 0.5 ? "#d8212f" : "#2b6cc4"); stl.position.set(x + s * 0.55, Y, z); g.add(stl); }
    for (let k = 0; k < 2; k++) { g.add(cy(0.035, 0.03, 0.09, tm("#f4f1e6"), x - 0.12 + k * 0.24, Y + 0.51, z, 10)); g.add(cy(0.03, 0.03, 0.005, tm("#3a2214"), x - 0.12 + k * 0.24, Y + 0.555, z, 10)); } }
  { const um = new THREE.Group(); um.add(mesh(new THREE.ConeGeometry(1.6, 0.5, 10, 1, true), tm("#2f8a52", null, { side: THREE.DoubleSide }), 0, 2.4, 0)); um.add(cy(0.025, 0.025, 2.4, tm("#ddd"), 0, 1.2, 0, 6)); um.position.set(X + 0.6, Y, Z + 0.3); g.add(um); }
  g.add(plane(1.3, 0.5, signTex("CÀ PHÊ VỈA HÈ", "Nâu đá · Bạc xỉu · 20K", 1.3, 0.5, "#3a2214", "#f2d36b", 3), X - 2.2, 1.3, Z + 0.9, 0.3));
  gopTinh(g); return { g, cho: { ban: [X + 0.6, Y, Z + 0.3] as V3 } };
}
export { GOLD_X };
