// Bối cảnh nội thất mới (17/11/2026, anh Huy: không lặp mãi 1 phòng livestream):
// quán cà phê, quán Phở Anh Hai, quán net (Home / Sparta), căn hộ chung cư trả góp, căn hộ cao cấp.
// Mỗi bối cảnh dựng quanh gốc toạ độ; máy đặt phía +z nhìn về -z (trục +x nằm bên PHẢI màn).
// Chỗ đứng nói chuyện chuẩn: người trái màn x = -0.7, người phải màn x = 0.7, z = 0.8.
import * as THREE from "three";
import { rng } from "../pho/paint";
import { lam, glow, box, cyl, stool, motorbike } from "./sets";
import { NOINK } from "../pho/ink";

const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";
const cvs = (w: number, h: number) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return [c, c.getContext("2d")!] as const; };
const ctex = (c: HTMLCanvasElement) => { const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t; };
const sh = <T extends THREE.Object3D>(o: T) => { o.traverse((m) => { const k = m as THREE.Mesh; if (k.isMesh) { k.castShadow = !k.userData.nc; k.receiveShadow = true; } }); return o; };
const at = <T extends THREE.Object3D>(o: T, x: number, y: number, z: number, ry = 0) => { o.position.set(x, y, z); o.rotation.y = ry; return o; };

/** biển hiệu chữ (canvas) */
function signBoard(text: string, w: number, h: number, bg: string, fg: string, sub?: string, lit = false) {
  const [c, x] = cvs(1024, Math.round(1024 * h / w)); x.fillStyle = bg; x.fillRect(0, 0, c.width, c.height);
  x.fillStyle = fg; x.textAlign = "center"; x.textBaseline = "middle"; x.font = `900 ${Math.round(c.height * (sub ? 0.42 : 0.55))}px ${F}`;
  x.fillText(text, c.width / 2, c.height * (sub ? 0.4 : 0.52), c.width * 0.94);
  if (sub) { x.font = `700 ${Math.round(c.height * 0.2)}px ${F}`; x.fillText(sub, c.width / 2, c.height * 0.8, c.width * 0.9); }
  const m = lit ? new THREE.MeshBasicMaterial({ map: ctex(c) }) : new THREE.MeshLambertMaterial({ map: ctex(c) });
  const p = new THREE.Mesh(new THREE.PlaneGeometry(w, h), m); p.layers.set(NOINK); return p;
}
/** tường + sàn hộp phòng (3 mặt) */
function shell(g: THREE.Group, W: number, D: number, H: number, wall: string, floor: string, side = wall) {
  const fl = box(W, 0.1, D, lam(floor)); fl.position.set(0, -0.05, D / 2 - 3); g.add(fl);
  const bw = box(W, H, 0.2, lam(wall)); bw.position.set(0, H / 2, -3); bw.userData.nc = 1; g.add(bw);
  for (const s of [-1, 1]) { const sw = box(0.2, H, D, lam(side)); sw.position.set(s * W / 2, H / 2, D / 2 - 3); sw.userData.nc = 1; g.add(sw); }
}
/** khách ngồi/đứng nền (người que) */
function patron(col: string, skin: string, sit = true) {
  const g = new THREE.Group(); const b = cyl(0.16, 0.22, sit ? 0.6 : 0.95, lam(col), 8); b.position.y = sit ? 0.75 : 0.75; g.add(b);
  const h = new THREE.Mesh(new THREE.SphereGeometry(0.16, 10, 8), lam(skin)); h.position.y = sit ? 1.2 : 1.4; g.add(h);
  const hair = new THREE.Mesh(new THREE.SphereGeometry(0.165, 10, 8, 0, Math.PI * 2, 0, Math.PI / 2), lam("#1b1416")); hair.position.y = sit ? 1.22 : 1.42; g.add(hair);
  return g;
}
const SKIN = ["#f1cfa8", "#e9c29a", "#d9a77e", "#f6d2b2"];
const SHIRT = ["#2b4f8a", "#c8202f", "#3f6b3a", "#f2d36b", "#6b4fa0", "#e86a92", "#f4f4f2", "#2b2b2b"];
function windowCity(w: number, h: number, night: boolean, seed = 3) {
  const [c, x] = cvs(512, Math.round(512 * h / w)), r = rng(seed); const H = c.height;
  const sky = x.createLinearGradient(0, 0, 0, H); sky.addColorStop(0, night ? "#0b1230" : "#8fc4ef"); sky.addColorStop(1, night ? "#2a2350" : "#dcefff"); x.fillStyle = sky; x.fillRect(0, 0, 512, H);
  for (let i = 0; i < 26; i++) { const bw = 20 + r() * 50, bh = H * (0.25 + r() * 0.6), bx = r() * 512; x.fillStyle = night ? "#141a33" : "#9aa8b8"; x.fillRect(bx, H - bh, bw, bh);
    for (let yy = H - bh + 6; yy < H - 6; yy += 10) for (let xx = bx + 4; xx < bx + bw - 4; xx += 9) if (r() < (night ? 0.45 : 0.25)) { x.fillStyle = night ? "#ffd27a" : "#c9dff0"; x.fillRect(xx, yy, 4, 5); } }
  const p = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map: ctex(c) })); p.layers.set(NOINK); return p;
}

// ---------- QUÁN CÀ PHÊ (bàn gỗ, quầy pha chế, cửa kính nhìn ra phố) ----------
export function buildCafe() {
  const g = new THREE.Group(), r = rng(11); shell(g, 12, 10, 3.6, "#8a4b32", "#a8743f", "#e9dcc0");
  // tường gạch trần
  for (let y = 0; y < 18; y++) for (let k = 0; k < 24; k++) { if (r() < 0.5) continue; const b = box(0.46, 0.16, 0.02, lam(r() < 0.5 ? "#9a5a3c" : "#7a3e28"), false); b.position.set(-5.8 + k * 0.5 + (y % 2) * 0.25, 0.2 + y * 0.19, -2.88); g.add(b); }
  g.add(at(signBoard("CÀ PHÊ PHỐ", 3.2, 0.7, "#1d2b22", "#f2d36b", "cà phê trứng · bạc xỉu · trà chanh", true), 0, 2.9, -2.86));
  const cnt = box(3.4, 1.05, 0.7, lam("#5a3b2a")); cnt.position.set(-3.8, 0.52, -1.9); g.add(cnt); const ct = box(3.5, 0.06, 0.8, lam("#d9c7a5"), false); ct.position.set(-3.8, 1.08, -1.9); g.add(ct);
  const mach = box(0.6, 0.5, 0.4, lam("#c9ced4")); mach.position.set(-4.6, 1.36, -2.05); g.add(mach); for (let k = 0; k < 5; k++) { const cup = cyl(0.05, 0.04, 0.1, lam("#f4f1e6"), 8); cup.position.set(-3.6 + k * 0.18, 1.16, -1.8); g.add(cup); }
  // cửa kính phải nhìn ra phố
  const win = windowCity(4, 2.2, false, 5); win.position.set(5.88, 1.7, -0.5); win.rotation.y = -Math.PI / 2; g.add(win);
  for (let k = 0; k < 3; k++) { const fr = box(0.06, 2.3, 0.06, lam("#2b2b2b"), false); fr.position.set(5.86, 1.7, -2.5 + k * 2); g.add(fr); }
  // bàn chính (giữa) + bàn khách
  const mainT = cyl(0.45, 0.45, 0.05, lam("#7a5236"), 20); mainT.position.set(0, 0.75, 0.4); g.add(mainT); const leg = cyl(0.05, 0.05, 0.75, lam("#2b2b2b"), 6); leg.position.set(0, 0.37, 0.4); g.add(leg);
  for (const x of [-0.12, 0.14]) { const c = cyl(0.05, 0.04, 0.11, lam("#f4f1e6"), 8); c.position.set(x, 0.83, 0.42); g.add(c); }
  const ph = box(0.08, 0.01, 0.15, lam("#111"), false); ph.position.set(0.25, 0.79, 0.3); g.add(ph);
  for (const [x, z] of [[-3, 1.4], [2.8, 1.6], [-2.6, -0.6], [3.2, -0.8]] as [number, number][]) {
    const t = cyl(0.4, 0.4, 0.05, lam("#7a5236"), 18); t.position.set(x, 0.72, z); g.add(t); const l = cyl(0.05, 0.05, 0.72, lam("#2b2b2b"), 6); l.position.set(x, 0.36, z); g.add(l);
    for (const s of [-1, 1]) { const st = stool("#3a2a20"); st.position.set(x + s * 0.65, 0, z); g.add(st); const p = patron(SHIRT[Math.floor(r() * 8)], SKIN[Math.floor(r() * 4)]); p.position.set(x + s * 0.65, 0, z); g.add(p); }
    const cup = cyl(0.05, 0.04, 0.1, lam("#f4f1e6"), 8); cup.position.set(x, 0.8, z); g.add(cup); }
  for (const x of [-5.4, 5.3]) { const pot = cyl(0.28, 0.22, 0.5, lam("#c9a24a"), 10); pot.position.set(x, 0.25, 2.6); g.add(pot); const lf = new THREE.Mesh(new THREE.IcosahedronGeometry(0.55, 0), lam("#3f8a3a")); lf.position.set(x, 1.0, 2.6); g.add(lf); }
  for (const x of [-2.6, 2.6]) { const cd = cyl(0.01, 0.01, 1.2, lam("#222"), 4); cd.position.set(x, 3.0, 0.4); g.add(cd); const b = new THREE.Mesh(new THREE.SphereGeometry(0.12, 10, 8), glow(2.4, 1.9, 1.2)); b.position.set(x, 2.35, 0.4); g.add(b); }
  const pl = new THREE.PointLight("#ffd9a0", 6, 12, 1.6); pl.position.set(0, 3, 1); g.add(pl);
  return { g: sh(g) };
}

// ---------- QUÁN PHỞ ANH HAI (nồi nước dùng, ghế nhựa, bàn inox, khách ăn) ----------
export function buildPho() {
  const g = new THREE.Group(), r = rng(21); shell(g, 12, 10, 3.4, "#e9e2d0", "#b9b4aa", "#f2ede0");
  for (let y = 0; y < 8; y++) for (let k = 0; k < 30; k++) { const t = box(0.38, 0.18, 0.02, lam((y + k) % 2 ? "#f4f4f2" : "#d6e4ea"), false); t.position.set(-5.8 + k * 0.4, 0.1 + y * 0.2, -2.88); g.add(t); }
  g.add(at(signBoard("PHỞ ANH HAI", 4.2, 0.9, "#c8202f", "#ffe36b", "Phở bò tái · chín · gầu · nạm · Mở cửa 6h–22h", true), 0, 2.75, -2.86));
  const menu = signBoard("PHỞ TÁI 50K · CHÍN 50K · ĐẶC BIỆT 70K", 3.6, 0.45, "#1f2a44", "#ffffff"); menu.position.set(0, 2.05, -2.86); g.add(menu);
  // bếp + nồi
  const bep = box(2.6, 0.9, 0.9, lam("#9aa3ad")); bep.position.set(-4.2, 0.45, -1.9); g.add(bep);
  for (const [x, rr] of [[-4.8, 0.42], [-3.7, 0.34]] as [number, number][]) { const pot = cyl(rr, rr * 0.92, 0.7, lam("#c9ced4"), 18); pot.position.set(x, 1.25, -1.9); g.add(pot);
    for (let k = 0; k < 4; k++) { const s = new THREE.Mesh(new THREE.SphereGeometry(0.12 + k * 0.04, 8, 6), new THREE.MeshBasicMaterial({ color: "#ffffff", transparent: true, opacity: 0.35 - k * 0.07 })); s.position.set(x + (k % 2 ? 0.06 : -0.05), 1.75 + k * 0.28, -1.9); s.layers.set(NOINK); g.add(s); } }
  const tu = box(1.6, 1.2, 0.6, lam("#f4f4f2")); tu.position.set(-2.6, 0.6, -2.4); g.add(tu); const kinh = box(1.5, 0.5, 0.02, glow(1.0, 1.1, 1.2), false); kinh.position.set(-2.6, 1.0, -2.08); g.add(kinh);
  // bàn inox + ghế nhựa đỏ/xanh + khách
  const table = (x: number, z: number, main = false) => { const t = box(1.1, 0.04, 0.7, lam("#c9ced4")); t.position.set(x, 0.62, z); g.add(t); for (const a of [-0.5, 0.5]) for (const b of [-0.3, 0.3]) { const l = cyl(0.02, 0.02, 0.62, lam("#9aa3ad"), 5); l.position.set(x + a, 0.31, z + b); g.add(l); }
    for (const s of [-0.25, 0.25]) { const bowl = new THREE.Mesh(new THREE.SphereGeometry(0.12, 12, 8, 0, Math.PI * 2, Math.PI / 2, Math.PI / 2), lam("#f4f1e6")); bowl.position.set(x + s, 0.76, z); g.add(bowl); const soup = cyl(0.115, 0.115, 0.01, lam("#c9852a"), 12); soup.position.set(x + s, 0.74, z); g.add(soup); }
    const chili = cyl(0.04, 0.04, 0.12, lam("#c0392b"), 8); chili.position.set(x - 0.45, 0.7, z - 0.25); g.add(chili); const nap = box(0.15, 0.1, 0.1, lam("#f4f4f2")); nap.position.set(x + 0.45, 0.69, z - 0.25); g.add(nap);
    if (!main) for (const s of [-1, 1]) { const st = stool(r() < 0.5 ? "#d8212f" : "#2b6cc4"); st.scale.set(0.9, 0.9, 0.9); st.position.set(x + s * 0.75, 0, z); g.add(st); const p = patron(SHIRT[Math.floor(r() * 8)], SKIN[Math.floor(r() * 4)]); p.position.set(x + s * 0.75, -0.1, z); g.add(p); } };
  table(0, 0.4, true); table(-3, 1.4); table(3, 1.4); table(2.8, -0.9); table(-0.2, -1.6);
  for (let k = 0; k < 6; k++) { const st = stool(k % 2 ? "#d8212f" : "#2b6cc4"); st.scale.set(0.9, 0.9, 0.9); st.position.set(4.6, 0.1 + k * 0.12, 2.6); g.add(st); }
  const fan = cyl(0.35, 0.35, 0.05, lam("#e9e6df"), 12); fan.position.set(5.6, 2.6, 0); fan.rotation.z = Math.PI / 2; g.add(fan);
  for (const x of [-2, 2]) { const tube = box(1.2, 0.05, 0.08, glow(2.2, 2.3, 2.4), false); tube.position.set(x, 3.25, 0.5); g.add(tube); }
  const pl = new THREE.PointLight("#fff4dc", 6, 12, 1.5); pl.position.set(0, 3, 1); g.add(pl);
  return { g: sh(g) };
}

/** màn hình game chiến thuật kiểu "Đế Chế" (đồ hoạ tự vẽ: cỏ, sông, nhà, quân 2 phe) */
function rtsTex(seed: number) {
  const [c, x] = cvs(256, 160), r = rng(seed); x.fillStyle = "#4f8a3a"; x.fillRect(0, 0, 256, 160);
  for (let i = 0; i < 40; i++) { x.fillStyle = r() < 0.5 ? "#3f7a30" : "#6a9a46"; x.beginPath(); x.arc(r() * 256, r() * 160, 6 + r() * 14, 0, 7); x.fill(); }
  x.fillStyle = "#3a7ac4"; x.beginPath(); x.moveTo(0, 90 + r() * 20); x.bezierCurveTo(80, 60, 160, 130, 256, 80 + r() * 20); x.lineTo(256, 100); x.bezierCurveTo(160, 150, 80, 80, 0, 112); x.fill();
  for (let i = 0; i < 9; i++) { x.fillStyle = "#8a6a48"; const hx = 20 + r() * 80, hy = 20 + r() * 50; x.fillRect(hx, hy, 12, 10); x.fillStyle = "#c0392b"; x.fillRect(hx, hy - 4, 12, 4); }
  for (let i = 0; i < 9; i++) { x.fillStyle = "#8a6a48"; const hx = 150 + r() * 90, hy = 110 + r() * 40; x.fillRect(hx, hy, 12, 10); x.fillStyle = "#2b6cc4"; x.fillRect(hx, hy - 4, 12, 4); }
  for (let i = 0; i < 40; i++) { x.fillStyle = i % 2 ? "#e74c3c" : "#3498db"; x.fillRect(90 + r() * 70, 50 + r() * 60, 3, 3); }
  x.fillStyle = "rgba(0,0,0,.6)"; x.fillRect(0, 140, 256, 20); x.fillStyle = "#f2d36b"; x.font = `700 11px ${F}`; x.fillText("Gỗ 1200  Lương 980  Vàng 450  Đá 300", 6, 154);
  const t = ctex(c); return t;
}
// ---------- QUÁN NET (Home: bình dân / Sparta: gaming LED) ----------
export function buildNet(kind: "home" | "sparta") {
  const g = new THREE.Group(), r = rng(kind === "home" ? 31 : 41), sp = kind === "sparta";
  shell(g, 14, 12, 3.4, sp ? "#141022" : "#2a2f3a", sp ? "#1b1830" : "#3a3f4a", sp ? "#161226" : "#2f3542");
  g.add(at(signBoard(sp ? "SPARTA GAMING" : "NET GAME HOME", 4.4, 0.85, sp ? "#0b0b14" : "#123a6a", sp ? "#ff3b5c" : "#7fe3ff", sp ? "Máy cấu hình khủng · 15K/giờ" : "Bình dân · 8K/giờ · có mì tôm", true), 0, 2.75, -2.86));
  const neon = (col: [number, number, number], y: number) => { const s = box(13.6, 0.05, 0.05, glow(...col), false); s.position.set(0, y, -2.8); g.add(s); };
  if (sp) { neon([2.6, 0.3, 0.9], 3.25); neon([0.3, 1.8, 2.6], 0.12); } else neon([0.6, 1.6, 2.4], 3.25);
  // dãy máy: 2 dãy dọc tường sau và 1 dãy giữa
  const pc = (x: number, z: number, ry: number, busy: boolean) => { const d = box(1.0, 0.05, 0.6, lam(sp ? "#1c1c24" : "#5a4a3a")); d.position.set(x, 0.75, z); d.rotation.y = ry; g.add(d);
    const scr = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.38), new THREE.MeshBasicMaterial({ map: rtsTex(Math.floor(r() * 999)) })); scr.layers.set(NOINK); scr.position.set(x - Math.sin(ry) * 0.2, 1.08, z - Math.cos(ry) * 0.2 + 0.02); scr.rotation.y = ry; g.add(scr);
    const bez = box(0.66, 0.42, 0.03, lam("#111"), false); bez.position.set(x - Math.sin(ry) * 0.2, 1.08, z - Math.cos(ry) * 0.2); bez.rotation.y = ry; g.add(bez);
    const ch = box(0.55, 1.0, 0.55, lam(sp ? (r() < 0.5 ? "#d8212f" : "#111") : "#2b2b2b")); ch.position.set(x + Math.sin(ry) * 0.45, 0.5, z + Math.cos(ry) * 0.45); g.add(ch);
    if (busy) { const p = patron(SHIRT[Math.floor(r() * 8)], SKIN[Math.floor(r() * 4)]); p.position.set(x + Math.sin(ry) * 0.42, 0.05, z + Math.cos(ry) * 0.42); g.add(p); } };
  for (let k = 0; k < 9; k++) pc(-6 + k * 1.5, -2.2, 0, r() < 0.75);
  for (let k = 0; k < 4; k++) { pc(-5.5 + k * 1.3, -0.4, 0, r() < 0.6); pc(1.9 + k * 1.3, -0.4, 0, r() < 0.6); }
  const poster = signBoard("ĐẾ CHẾ", 1.6, 2.2, sp ? "#2a0f0f" : "#1f2a44", "#f2d36b", "Thanh xuân của chúng ta · 1 ăn 3 · Giải tối thứ 7"); poster.position.set(-6.88, 1.8, 0.6); poster.rotation.y = Math.PI / 2; g.add(poster);
  const quay = box(1.8, 1.0, 0.6, lam(sp ? "#0e0e16" : "#6a4a32")); quay.position.set(5.6, 0.5, 2.2); quay.rotation.y = -Math.PI / 2; g.add(quay);
  const fridge = box(0.8, 1.8, 0.6, lam("#e9e6df")); fridge.position.set(6.4, 0.9, 0.4); g.add(fridge); const fg = box(0.7, 1.4, 0.02, glow(1.4, 1.6, 1.8), false); fg.position.set(6.08, 1.0, 0.4); fg.rotation.y = -Math.PI / 2; g.add(fg);
  const pl = new THREE.PointLight(sp ? "#b06bff" : "#9fd8ff", 5, 12, 1.6); pl.position.set(0, 3, 1); g.add(pl);
  return { g: sh(g) };
}

// ---------- CĂN HỘ: "tragop" = chung cư trả góp (Kim Văn – Kim Lũ, Văn Quán) / "vip" = cao cấp (Royal City) ----------
export function buildCanHo(kind: "tragop" | "vip", night = true) {
  const g = new THREE.Group(), vip = kind === "vip";
  shell(g, 10, 9, vip ? 3.4 : 2.8, vip ? "#e8e2d6" : "#e9e4c9", vip ? "#d9d4cc" : "#b98a5a", vip ? "#f2efe8" : "#ece6cf");
  // cửa sổ lớn nhìn ra thành phố
  const win = windowCity(vip ? 6 : 3, vip ? 2.4 : 1.5, night, vip ? 9 : 4); win.position.set(vip ? 0 : 2, vip ? 1.8 : 1.6, -2.88); g.add(win);
  if (!vip) for (let k = 0; k < 5; k++) { const bar = box(0.03, 1.5, 0.03, lam("#5a5a5a"), false); bar.position.set(0.6 + k * 0.7, 1.6, -2.86); g.add(bar); }
  // sofa + bàn trà + TV
  const sofa = box(vip ? 2.8 : 2.0, 0.45, 0.8, lam(vip ? "#cfc6b8" : "#6a7a8a")); sofa.position.set(-2.6, 0.32, -1.6); g.add(sofa); const back = box(vip ? 2.8 : 2.0, 0.5, 0.2, lam(vip ? "#bfb6a8" : "#5a6a7a")); back.position.set(-2.6, 0.75, -2.0); g.add(back);
  const tbl = box(1.0, 0.06, 0.6, lam(vip ? "#2b2b2b" : "#8a6a48")); tbl.position.set(-2.6, 0.42, -0.6); g.add(tbl);
  const tv = box(vip ? 1.8 : 1.1, vip ? 1.0 : 0.65, 0.05, glow(0.5, 0.7, 1.0), false); tv.position.set(4.9, 1.4, -0.8); tv.rotation.y = -Math.PI / 2; g.add(tv);
  const ke = box(0.4, 0.5, 1.8, lam(vip ? "#2b2b2b" : "#a07850")); ke.position.set(4.8, 0.25, -0.8); g.add(ke);
  // bếp góc phải sau
  const bep = box(2.4, 0.9, 0.6, lam(vip ? "#f4f4f2" : "#c9b48a")); bep.position.set(3.4, 0.45, -2.5); g.add(bep);
  if (vip) { const chand = new THREE.Group(); for (let k = 0; k < 12; k++) { const a = k / 12 * Math.PI * 2; const b = new THREE.Mesh(new THREE.SphereGeometry(0.06, 8, 6), glow(2.8, 2.5, 1.8)); b.position.set(Math.cos(a) * 0.5, 0, Math.sin(a) * 0.5); chand.add(b); } chand.position.set(0, 3.0, 0); g.add(chand);
    const art = signBoard("", 1.2, 0.8, "#c9a24a", "#000"); art.position.set(-2.6, 1.8, -2.88); g.add(art);
    const marble = box(9.9, 0.01, 8.9, lam("#efece6"), false); marble.position.set(0, 0.005, 1.5); g.add(marble); }
  else { const calendar = signBoard("LỊCH TRẢ GÓP", 0.8, 0.5, "#ffffff", "#c8202f", "kỳ 37/240"); calendar.position.set(-4.88, 1.6, -0.5); calendar.rotation.y = Math.PI / 2; g.add(calendar);
    const fanS = cyl(0.25, 0.25, 0.06, lam("#e9e6df"), 12); fanS.position.set(-4.2, 0.9, 1.2); fanS.rotation.x = Math.PI / 2; g.add(fanS);
    const ao = box(1.4, 0.02, 0.02, lam("#888"), false); ao.position.set(-0.5, 2.3, -2.8); g.add(ao); for (let k = 0; k < 4; k++) { const sh2 = box(0.3, 0.45, 0.02, lam(SHIRT[k + 2]), false); sh2.position.set(-1 + k * 0.35, 2.05, -2.78); g.add(sh2); } }
  const pl = new THREE.PointLight(vip ? "#fff1d8" : "#ffe6b8", vip ? 6 : 4.5, 10, 1.6); pl.position.set(0, 2.5, 1); g.add(pl);
  return { g: sh(g) };
}

// ---------- TIỆM SỬA XE MÁY HÀ NỘI (DN1811 – tiệm của Hùng Xa Lộ) ----------
// Dựng xoay 180°: tường sau nằm ở z = +3 để dùng chung máy quay kiểu ảnh nền (máy ở -z nhìn về +z). Chừa trống giữa tiệm cho nhân vật (x -1..1, z 0..1.5).
export function buildSuaXe() {
  const g = new THREE.Group(), r = rng(31); shell(g, 11, 8, 4.4, "#f1e6c8", "#9a958d", "#e8dcbc");
  // vạch gạch men xanh chân tường + vết dầu trên sàn
  const tile = box(11, 1.1, 0.04, lam("#5f8f7a")); tile.position.set(0, 0.55, -2.88); g.add(tile);
  for (let i = 0; i < 9; i++) { const st = new THREE.Mesh(new THREE.CircleGeometry(0.15 + r() * 0.3, 14), new THREE.MeshLambertMaterial({ color: "#5d5953", transparent: true, opacity: 0.55 })); st.rotation.x = -Math.PI / 2; st.position.set(-4.5 + r() * 9, 0.006, -2.4 + r() * 5); g.add(st); }
  g.add(at(signBoard("SỬA XE HÙNG XA LỘ", 5.2, 1.0, "#1f5fae", "#ffffff", "Sửa chữa · Bảo dưỡng · Thay dầu · Vá lốp · Mua bán xe cũ", true), 0, 3.15, -2.85));
  // bảng treo dụng cụ
  const peg = box(2.4, 1.3, 0.05, lam("#3b3f46")); peg.position.set(3, 2.1, -2.84); g.add(peg);
  for (let i = 0; i < 14; i++) { const tl = box(0.06, 0.32 + r() * 0.25, 0.03, lam(["#c9cdd3", "#d8212f", "#f2c230", "#2b6cc4"][i % 4])); tl.position.set(2 + (i % 7) * 0.32, 2.35 - Math.floor(i / 7) * 0.55, -2.8); tl.rotation.z = (r() - 0.5) * 0.4; g.add(tl); }
  // bàn thợ + hộp đồ đỏ + máy nén khí
  const bench = box(2.4, 0.9, 0.8, lam("#6b5a48")); bench.position.set(3, 0.45, -2.35); g.add(bench);
  const tb = box(0.7, 0.35, 0.35, lam("#c8202f")); tb.position.set(2.4, 1.08, -2.35); g.add(tb);
  const vise = box(0.25, 0.2, 0.2, lam("#2b6cc4")); vise.position.set(3.7, 1.0, -2.2); g.add(vise);
  const comp = cyl(0.28, 0.28, 0.9, lam("#d8212f"), 14); comp.rotation.z = Math.PI / 2; comp.position.set(4.6, 0.35, -1.6); g.add(comp);
  // kệ dầu nhớt
  const shelf = box(1.8, 0.05, 0.4, lam("#9aa3ad")); for (const y of [1.3, 1.9]) { const sh0 = shelf.clone(); sh0.position.set(-1.6, y, -2.7); g.add(sh0);
    for (let k = 0; k < 8; k++) { const can = cyl(0.08, 0.08, 0.3, lam(["#1d8a4a", "#d8212f", "#f2c230", "#1f2a44"][(k + Math.round(y)) % 4]), 10); can.position.set(-2.35 + k * 0.21, y + 0.17, -2.7); g.add(can); } }
  // lốp xe: chồng lốp + lốp treo tường
  const tyre = (x: number, y: number, z: number, rr = 0.3, stand = false) => { const t = new THREE.Mesh(new THREE.TorusGeometry(rr, 0.1, 8, 20), lam("#1d1d22")); if (!stand) t.rotation.x = Math.PI / 2; t.position.set(x, y, z); t.castShadow = true; g.add(t); };
  for (const [x, z, n] of [[-4.4, -2.3, 6], [-3.7, -2.4, 5], [-4.5, -1.5, 4]] as [number, number, number][]) for (let k = 0; k < n; k++) tyre(x, 0.1 + k * 0.2, z);
  for (let k = 0; k < 5; k++) tyre(-4.6 + k * 0.62, 2.2, -2.75, 0.24, true);
  // 2 xe đang sửa: 1 xe số trên bục nâng, 1 xe ga dựng bên trái
  const lift = box(1.0, 0.25, 2.0, lam("#f2c230")); lift.position.set(3.3, 0.12, -0.6); g.add(lift);
  const b1 = motorbike("#c8202f", "wave"); b1.position.set(3.3, 0.25, -0.6); g.add(b1);
  const b2 = motorbike("#f4f4f2", "vision"); b2.position.set(-3.4, 0, 0.6); b2.rotation.y = 0.5; g.add(b2);
  const b3 = motorbike("#1f2a44", "wave"); b3.position.set(-4.4, 0, 1.9); b3.rotation.y = -0.3; g.add(b3);
  // bàn trà nhỏ + ghế nhựa + ấm chén (chỗ Hùng rót nước)
  const tt = box(0.7, 0.04, 0.5, lam("#c9a46a")); tt.position.set(1.9, 0.45, 0.4); g.add(tt);
  for (const [a, b] of [[-0.3, -0.2], [0.3, -0.2], [-0.3, 0.2], [0.3, 0.2]]) { const l = box(0.04, 0.45, 0.04, lam("#8a6a48")); l.position.set(1.9 + a, 0.22, 0.4 + b); g.add(l); }
  const pot = new THREE.Mesh(new THREE.SphereGeometry(0.1, 12, 10), lam("#e9e6df")); pot.position.set(1.8, 0.56, 0.4); g.add(pot);
  for (const x of [1.98, 2.1]) { const c = cyl(0.035, 0.03, 0.06, lam("#f4f1e6"), 8); c.position.set(x, 0.5, 0.48); g.add(c); }
  for (const [x, z, c] of [[2.6, 0.5, "#2b6cc4"], [1.3, 1.1, "#d8212f"]] as [number, number, string][]) { const st = stool(c); st.position.set(x, 0, z); g.add(st); }
  // giấy SANG NHƯỢNG dán ở cột cửa (chi tiết thứ nhất)
  const paper = signBoard("SANG NHƯỢNG", 0.9, 0.6, "#fffbe8", "#c8202f", "Liên hệ chủ tiệm"); paper.position.set(5.38, 1.7, 2.2); paper.rotation.y = -Math.PI / 2; g.add(paper);
  // đèn tuýp + quạt treo tường
  for (const x of [-2.5, 0, 2.5]) { const tube = box(1.2, 0.05, 0.08, glow(2.2, 2.3, 2.4), false); tube.position.set(x, 4.25, -2.7); g.add(tube); }
  const fan = cyl(0.35, 0.35, 0.05, lam("#e9e6df"), 12); fan.position.set(-5.3, 3.0, -0.5); fan.rotation.z = Math.PI / 2; g.add(fan);
  const pl = new THREE.PointLight("#fff4dc", 7, 13, 1.5); pl.position.set(0, 3.6, 0.5); g.add(pl);
  sh(g); g.rotation.y = Math.PI; return { g };
}
