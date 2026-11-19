// CAST3 (thử nghiệm 19/11/2026): nhân vật 3D toon cho bối cảnh chi tiết suaxe2 – thay thẻ 2D của cast2 (KHÔNG đụng cast2).
// Tỉ lệ gần người thật (đầu ~1/7 chiều cao), có cổ, vai, bàn tay 5 ngón, giày; mắt (lòng trắng + mống + con ngươi + điểm sáng + mí),
// lông mày biểu cảm, mũi, tai, miệng nhiều dạng (vẽ canvas dán cong theo mặt), tóc khối có vòng sáng, áo có nếp/cổ/túi/thắt lưng/vết dầu.
// Dùng chung vật liệu toon của set (toonmat.ts) nên nắng + đèn ấm của set lên được nhân vật.
// Đặt cảnh: Demo ghi CAST3.shots[i] = danh sách tư thế của cảnh quay i (mỗi cảnh 30 khung); set gọi tick(t) → cảnh floor(t).
import * as THREE from "three";
import { tm, glow } from "./toonmat";
import { NOINK } from "../pho/ink";

const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";
type V3 = [number, number, number];
export type Expr3 = "neutral" | "smug" | "dazed" | "stern" | "talk" | "worried" | "smile";
export type Arm3 = { f: number; out: number; el: number; palm?: number }; // giơ trước, dang ngang, gập khuỷu, xoay cổ tay
export type Pose3 = { who: string; p: V3; ry: number; e: Expr3; armL?: Arm3; armR?: Arm3; head?: number; gaze?: number; prop?: "wrench" | "phone" };
export const CAST3: { shots: Pose3[][] } = { shots: [] };

type Look = { top: string; top2: string; pants: string; shoe: string; sole: string; hair: string; hairHi: string; skin: string; iris: string; h: number; wide: number;
  kind: "mech" | "jacket" | "blouse"; hairStyle: "short" | "messy" | "long"; stains?: boolean; beard?: boolean; name?: string };
// Nhận diện theo cast2 của phim DN1: Hùng = áo xanh công nhân (thợ sửa xe, người chắc), Chiến = áo khoác cam, tóc nâu.
export const LOOKS: Record<string, Look> = {
  hung: { top: "#3a6ea5", top2: "#2c5684", pants: "#3a3f52", shoe: "#e9e6df", sole: "#6b625c", hair: "#161214", hairHi: "#4a4250", skin: "#e6b98e", iris: "#3a2418", h: 1.72, wide: 1.12, kind: "mech", hairStyle: "short", stains: true, beard: true, name: "HÙNG" },
  chien: { top: "#ff7a1a", top2: "#d85e0a", pants: "#2b2b33", shoe: "#f4f4f2", sole: "#8a8a90", hair: "#7a3e1c", hairHi: "#c27a44", skin: "#f0c49c", iris: "#4a2a14", h: 1.7, wide: 1.0, kind: "jacket", hairStyle: "messy" },
  lan: { top: "#f2b8c6", top2: "#d98ea2", pants: "#3b4f7a", shoe: "#c8202f", sole: "#5a1a1a", hair: "#1b1416", hairHi: "#5a4a5a", skin: "#f3cfb0", iris: "#2a1a10", h: 1.58, wide: 0.9, kind: "blouse", hairStyle: "long" },
};

const cvs = (w: number, h: number) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return [c, c.getContext("2d")!] as const; };
const ctex = (c: HTMLCanvasElement) => { const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t; };
const M = (geo: THREE.BufferGeometry, m: THREE.Material, x = 0, y = 0, z = 0) => { const k = new THREE.Mesh(geo, m); k.position.set(x, y, z); k.castShadow = true; k.receiveShadow = true; return k; };
/** capsule treo từ khớp xuống (đỉnh ở y = 0) */
const limb = (r: number, len: number, m: THREE.Material) => { const g = new THREE.CapsuleGeometry(r, len, 4, 12); g.translate(0, -len / 2 - r * 0.6, 0); return M(g, m); };
const sph = (r: number, m: THREE.Material, sx = 1, sy = 1, sz = 1, seg = 16) => { const k = M(new THREE.SphereGeometry(r, seg, Math.round(seg * 0.75)), m); k.scale.set(sx, sy, sz); return k; };

/** áo: canvas quấn quanh thân (u = 0.5 là chính giữa ngực) – nếp nhăn, nẹp cúc, túi, cổ, vết dầu */
function topTex(L: Look) {
  const [c, x] = cvs(512, 256); x.fillStyle = L.top; x.fillRect(0, 0, 512, 256); let s = 7; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
  const shade = (a: number) => `rgba(0,0,30,${a})`;
  x.strokeStyle = shade(0.22); x.lineCap = "round";
  for (const [u0, dir] of [[150, 1], [362, -1], [110, 1], [400, -1]] as [number, number][]) for (let k = 0; k < 3; k++) { x.lineWidth = 5 - k; x.beginPath(); x.moveTo(u0 + k * 14 * dir, 230 - k * 10); x.quadraticCurveTo(u0 + 40 * dir, 160 - k * 20, u0 + 70 * dir + k * 8, 120 - k * 16); x.stroke(); } // nếp kéo ở eo/nách
  x.strokeStyle = shade(0.16); x.lineWidth = 3; for (let k = 0; k < 5; k++) { const u = 200 + k * 25; x.beginPath(); x.moveTo(u, 255); x.lineTo(u + (r() - 0.5) * 20, 215); x.stroke(); } // nếp chùng gấu áo
  const g = x.createLinearGradient(0, 0, 0, 256); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(0.75, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(0,0,20,.25)"); x.fillStyle = g; x.fillRect(0, 0, 512, 256);
  if (L.kind === "mech") {
    x.strokeStyle = shade(0.45); x.lineWidth = 3; x.beginPath(); x.moveTo(256, 0); x.lineTo(256, 256); x.stroke(); x.fillStyle = L.top2; x.fillRect(250, 0, 12, 256);
    for (let k = 0; k < 5; k++) { x.fillStyle = "#e8e4dc"; x.beginPath(); x.arc(256, 30 + k * 48, 5, 0, 7); x.fill(); x.strokeStyle = "#222"; x.lineWidth = 1.5; x.stroke(); }
    for (const u of [205, 307]) { x.fillStyle = L.top2; x.fillRect(u - 26, 50, 52, 58); x.strokeStyle = shade(0.6); x.lineWidth = 2.5; x.strokeRect(u - 26, 50, 52, 58); x.fillRect(u - 28, 44, 56, 16); x.strokeRect(u - 28, 44, 56, 16); }
    x.fillStyle = "#d9d4c8"; x.fillRect(282, 72, 4, 30); x.fillStyle = "#c8202f"; x.fillRect(281, 68, 6, 6); // bút cắm túi
    if (L.name) { x.fillStyle = "#f4f1e6"; x.fillRect(176, 112, 58, 20); x.fillStyle = "#1f3d8a"; x.font = `900 15px ${F}`; x.textAlign = "center"; x.fillText(L.name, 205, 127); }
  } else if (L.kind === "jacket") {
    x.fillStyle = "#f4f1e6"; x.fillRect(224, 0, 64, 256); x.fillStyle = "rgba(0,0,0,.08)"; x.fillRect(224, 0, 64, 256); // áo phông trắng bên trong
    x.fillStyle = "#3a3a40"; x.fillRect(218, 0, 7, 256); x.fillRect(287, 0, 7, 256); // khoá kéo 2 mép
    x.fillStyle = L.top2; x.fillRect(0, 226, 512, 30); x.strokeStyle = shade(0.25); x.lineWidth = 1.5; for (let u = 0; u < 512; u += 6) { x.beginPath(); x.moveTo(u, 228); x.lineTo(u, 256); x.stroke(); } // bo gấu
    x.strokeStyle = shade(0.5); x.lineWidth = 3; for (const [a, b] of [[150, 175], [362, 337]]) { x.beginPath(); x.moveTo(a, 150); x.lineTo(b, 210); x.stroke(); } // túi chéo
    x.fillStyle = "#1f2a44"; x.font = `900 22px ${F}`; x.textAlign = "center"; x.fillText("·•·", 256, 120);
  } else {
    for (let k = 0; k < 60; k++) { x.fillStyle = ["#ffffff", "#e86a92", "#f6e27a"][k % 3]; x.beginPath(); x.arc(r() * 512, r() * 256, 4 + r() * 4, 0, 7); x.fill(); } // hoa nhí
    x.strokeStyle = shade(0.35); x.lineWidth = 2.5; x.beginPath(); x.moveTo(222, 0); x.lineTo(256, 50); x.lineTo(290, 0); x.stroke(); // cổ chữ V
  }
  if (L.stains) for (let k = 0; k < 14; k++) { const px = 140 + r() * 240, py = 90 + r() * 160, q = 5 + r() * 16; const gg = x.createRadialGradient(px, py, 0, px, py, q); gg.addColorStop(0, "rgba(25,20,18,.75)"); gg.addColorStop(1, "rgba(25,20,18,0)"); x.fillStyle = gg; x.beginPath(); x.ellipse(px, py, q, q * 0.7, r() * 3, 0, 7); x.fill(); }
  return ctex(c);
}
function pantsTex(L: Look) {
  const [c, x] = cvs(128, 256); x.fillStyle = L.pants; x.fillRect(0, 0, 128, 256); x.strokeStyle = "rgba(0,0,0,.25)"; x.lineWidth = 2; for (let k = 0; k < 6; k++) { x.beginPath(); x.moveTo(10 + k * 20, 0); x.lineTo(14 + k * 20, 256); x.stroke(); }
  x.strokeStyle = "rgba(0,0,0,.3)"; x.lineWidth = 3; for (const y of [150, 165, 178]) { x.beginPath(); x.moveTo(30, y); x.quadraticCurveTo(64, y + 10, 98, y); x.stroke(); } // nếp đầu gối
  if (L.stains) for (let k = 0; k < 8; k++) { const px = Math.random() * 128, py = 60 + Math.random() * 180; x.fillStyle = "rgba(20,18,16,.45)"; x.beginPath(); x.ellipse(px, py, 4 + Math.random() * 8, 3 + Math.random() * 5, 1, 0, 7); x.fill(); }
  return ctex(c);
}
function hairTex(L: Look) {
  const [c, x] = cvs(256, 128); x.fillStyle = L.hair; x.fillRect(0, 0, 256, 128);
  x.strokeStyle = "rgba(0,0,0,.35)"; x.lineWidth = 2; for (let k = 0; k < 40; k++) { const u = k * 6.4; x.beginPath(); x.moveTo(u, 0); x.quadraticCurveTo(u + 6, 64, u - 4, 128); x.stroke(); }
  const g = x.createLinearGradient(0, 30, 0, 70); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(0.5, L.hairHi); g.addColorStop(1, "rgba(0,0,0,0)"); x.fillStyle = g; x.globalAlpha = 0.9; x.fillRect(0, 30, 256, 40); // vòng sáng tóc
  x.globalAlpha = 1; x.strokeStyle = L.hairHi; x.lineWidth = 2; for (let k = 0; k < 30; k++) { const u = k * 8.5 + 3; x.beginPath(); x.moveTo(u, 38); x.lineTo(u + 3, 62); x.stroke(); }
  return ctex(c);
}
/** miệng + râu lún phún + má hồng (dán lên vùng mặt dưới) */
function mouthTex(L: Look, e: Expr3) {
  const [c, x] = cvs(256, 128); x.clearRect(0, 0, 256, 128);
  if (L.beard) { for (let k = 0; k < 420; k++) { const a = Math.random() * Math.PI, rr = 60 + Math.random() * 60; const px = 128 + Math.cos(a) * rr * 1.05, py = 18 + Math.sin(a) * rr * 0.9; if (py > 126) continue; x.fillStyle = "rgba(60,45,40,.35)"; x.fillRect(px, py, 2, 2); } }
  for (const s of [-1, 1]) { const gg = x.createRadialGradient(128 + s * 88, 22, 0, 128 + s * 88, 22, 26); gg.addColorStop(0, L.kind === "blouse" ? "rgba(240,110,120,.55)" : "rgba(230,120,100,.3)"); gg.addColorStop(1, "rgba(230,120,100,0)"); x.fillStyle = gg; x.fillRect(128 + s * 88 - 30, 0, 60, 52); }
  const ink = "#2a1614", lip = "#7a2a26"; x.lineCap = "round"; x.lineJoin = "round"; x.strokeStyle = ink; x.lineWidth = 7; const cx = 128, cy = 74; x.translate(cx, cy); x.scale(1.45, 1.35); x.translate(-cx, -cy);
  const open = (w: number, h: number, up: number, teeth = true) => { x.beginPath(); x.moveTo(cx - w, cy - up); x.quadraticCurveTo(cx, cy - up - 4, cx + w, cy - up); x.quadraticCurveTo(cx, cy + h, cx - w, cy - up); x.closePath(); x.fillStyle = lip; x.fill();
    if (teeth) { x.save(); x.clip(); x.fillStyle = "#f6f2ea"; x.fillRect(cx - w, cy - up - 6, w * 2, 10); x.fillStyle = "#c8505a"; x.beginPath(); x.ellipse(cx, cy + h * 0.55, w * 0.5, h * 0.3, 0, 0, 7); x.fill(); x.restore(); } x.stroke(); };
  if (e === "talk") open(26, 30, 2);
  else if (e === "smile") open(34, 26, 6);
  else if (e === "dazed") { x.beginPath(); x.ellipse(cx, cy + 4, 10, 13, 0, 0, 7); x.fillStyle = lip; x.fill(); x.stroke(); }
  else if (e === "smug") { x.beginPath(); x.moveTo(cx - 26, cy + 4); x.quadraticCurveTo(cx, cy + 8, cx + 30, cy - 10); x.stroke(); x.lineWidth = 3; x.beginPath(); x.moveTo(cx + 30, cy - 10); x.lineTo(cx + 36, cy - 14); x.stroke(); }
  else if (e === "stern") { x.beginPath(); x.moveTo(cx - 26, cy + 4); x.quadraticCurveTo(cx, cy - 2, cx + 26, cy + 4); x.stroke(); }
  else if (e === "worried") { x.beginPath(); x.moveTo(cx - 24, cy + 8); x.quadraticCurveTo(cx - 10, cy - 6, cx, cy + 2); x.quadraticCurveTo(cx + 10, cy - 6, cx + 24, cy + 8); x.stroke(); }
  else { x.beginPath(); x.moveTo(cx - 24, cy); x.quadraticCurveTo(cx, cy + 9, cx + 24, cy); x.stroke(); }
  x.strokeStyle = "rgba(42,22,20,.35)"; x.lineWidth = 3; if (e !== "dazed") { x.beginPath(); x.moveTo(cx - 8, cy + 26); x.quadraticCurveTo(cx, cy + 30, cx + 8, cy + 26); x.stroke(); } // bóng môi dưới
  return ctex(c);
}
// mí (0 = mở to, 1 = nhắm), lông mày [cao, nghiêng trong] cho từng biểu cảm (trái/phải theo nhân vật)
const FACE: Record<Expr3, { lid: [number, number]; brow: [[number, number], [number, number]] }> = {
  neutral: { lid: [0.28, 0.28], brow: [[0, 0.05], [0, 0.05]] },
  smug: { lid: [0.52, 0.42], brow: [[0.004, -0.15], [0.016, 0.22]] },
  dazed: { lid: [0.05, 0.05], brow: [[0.018, 0.15], [0.018, 0.15]] },
  stern: { lid: [0.4, 0.4], brow: [[-0.008, -0.42], [-0.008, -0.42]] },
  talk: { lid: [0.22, 0.22], brow: [[0.008, 0.08], [0.01, 0.1]] },
  worried: { lid: [0.32, 0.32], brow: [[0.008, 0.45], [0.008, 0.45]] },
  smile: { lid: [0.55, 0.55], brow: [[0.01, 0.1], [0.01, 0.1]] },
};

export class Person3 {
  root = new THREE.Group(); head = new THREE.Group(); private sh: THREE.Group[] = []; private el: THREE.Group[] = []; private hand: THREE.Group[] = [];
  private lids: THREE.Mesh[] = []; private brows: THREE.Mesh[] = []; private iris: THREE.Group[] = []; private mouth: THREE.Mesh; private mtex: Partial<Record<Expr3, THREE.Texture>> = {};
  private props: Record<string, THREE.Object3D> = {};
  constructor(public L: Look) {
    const k = L.h / 1.72, w = L.wide, skin = tm(L.skin), top = tm("#ffffff", topTex(L)), topPlain = tm(L.top), pants = tm("#ffffff", pantsTex(L)), shoe = tm(L.shoe), sole = tm(L.sole), hairM = tm("#ffffff", hairTex(L)), hairC = tm(L.hair);
    const body = new THREE.Group(); body.scale.setScalar(k); this.root.add(body);
    // chân + giày
    for (const s of [-1, 1]) { const hip = new THREE.Group(); hip.position.set(s * 0.095 * w, 0.9, 0); body.add(hip); hip.add(limb(0.072 * Math.sqrt(w), 0.34, pants));
      const knee = new THREE.Group(); knee.position.y = -0.43; hip.add(knee); knee.add(limb(0.058 * Math.sqrt(w), 0.3, pants)); hip.rotation.z = s * 0.03;
      const cuff = M(new THREE.CylinderGeometry(0.062, 0.064, 0.03, 14), tm(L.pants), 0, -0.37, 0); knee.add(cuff);
      const foot = new THREE.Group(); foot.position.y = -0.42; knee.add(foot);
      const sg = new THREE.CapsuleGeometry(0.047, 0.15, 4, 12); sg.rotateX(Math.PI / 2); const sm = M(sg, shoe, 0, 0.0, 0.045); sm.scale.set(1.05, 0.85, 1); foot.add(sm);
      foot.add(M(new THREE.BoxGeometry(0.1, 0.022, 0.26), sole, 0, -0.04, 0.045));
      if (L.shoe === "#f4f4f2" || L.shoe === "#e9e6df") foot.add(M(new THREE.BoxGeometry(0.098, 0.012, 0.03), tm("#c8202f"), 0, 0.0, -0.055)); }
    // hông + thắt lưng
    const pel = M(new THREE.CapsuleGeometry(0.1, 0.12 * w, 4, 12), pants, 0, 0.93, 0); pel.rotation.z = Math.PI / 2; pel.scale.set(1, 1, 0.78); body.add(pel);
    // thân áo (tiện quanh trục, đường may ở lưng)
    const y0 = L.kind === "mech" ? 0.96 : 0.86, pr: [number, number][] = L.kind === "mech" ? [[0.158, 0.96], [0.168, 1.02], [0.178, 1.1], [0.185, 1.2], [0.19, 1.3], [0.178, 1.38], [0.13, 1.44], [0.06, 1.47]]
      : [[0.175, 0.86], [0.172, 0.92], [0.17, 1.02], [0.176, 1.12], [0.188, 1.24], [0.192, 1.32], [0.178, 1.39], [0.13, 1.45], [0.06, 1.48]];
    const lathe = new THREE.LatheGeometry(pr.map(([r, y]) => new THREE.Vector2(r, y)), 28, Math.PI, Math.PI * 2); const torso = M(lathe, top); torso.scale.set(w, 1, 0.68 * Math.sqrt(w)); body.add(torso);
    if (L.kind === "mech") { const belt = M(new THREE.CylinderGeometry(0.163, 0.163, 0.045, 28), tm("#2a2220"), 0, 0.965, 0); belt.scale.set(w, 1, 0.7 * Math.sqrt(w)); body.add(belt); body.add(M(new THREE.BoxGeometry(0.06, 0.045, 0.012), tm("#c9cdd3"), 0, 0.965, 0.118 * Math.sqrt(w))); }
    void y0;
    // cổ áo
    if (L.kind === "mech") { for (const s of [-1, 1]) { const fl = M(new THREE.BoxGeometry(0.075, 0.055, 0.012), tm(L.top2), s * 0.045, 1.43, 0.075); fl.rotation.set(-0.5, 0, s * 0.75); body.add(fl); }
      const band = M(new THREE.TorusGeometry(0.068, 0.016, 6, 20), tm(L.top2), 0, 1.455, -0.005); band.rotation.x = Math.PI / 2; band.scale.set(1, 0.85, 1); body.add(band); }
    else if (L.kind === "jacket") { const band = M(new THREE.CylinderGeometry(0.075, 0.085, 0.07, 20, 1, true), tm(L.top2, null, { side: THREE.DoubleSide }), 0, 1.47, -0.01); body.add(band); }
    // cổ + đầu
    body.add(M(new THREE.CylinderGeometry(0.05 * Math.sqrt(w), 0.056 * Math.sqrt(w), 0.12, 14), skin, 0, 1.47, 0.0));
    this.head.position.set(0, 1.6, 0.01); body.add(this.head); const H = this.head;
    const skull = sph(0.12, skin, 0.96 * Math.sqrt(w), 1.08, 1.0, 28); H.add(skull);
    const jaw = sph(0.1, skin, 0.92 * Math.sqrt(w), 0.75, 0.95, 20); jaw.position.set(0, -0.045, 0.012); H.add(jaw);
    for (const s of [-1, 1]) { const ear = sph(0.03, skin, 0.45, 1, 0.75, 12); ear.position.set(s * 0.115 * Math.sqrt(w), -0.005, -0.005); H.add(ear); const inr = sph(0.016, tm("#c98a6a"), 0.3, 0.8, 0.6, 8); inr.position.set(s * 0.127 * Math.sqrt(w), -0.005, 0.0); H.add(inr); }
    const nose = sph(0.016, skin, 0.75, 1.1, 1.0, 12); nose.position.set(0, -0.022, 0.113); H.add(nose);
    // mắt
    for (const s of [-1, 1]) {
      const eg = new THREE.Group(); eg.position.set(s * 0.043, 0.018, 0.098); eg.scale.set(1, 1.15, 0.55); H.add(eg);
      eg.add(sph(0.026, tm("#fbfaf6"), 1, 1, 1, 16));
      const lidG = new THREE.SphereGeometry(0.0275, 16, 8, 0, Math.PI * 2, 0, Math.PI / 2); const lid = M(lidG, skin); eg.add(lid); this.lids.push(lid);
      const ig = new THREE.Group(); ig.position.set(s * 0.043, 0.016, 0.1135); H.add(ig);
      const ir = new THREE.Mesh(new THREE.CircleGeometry(0.0135, 20), new THREE.MeshBasicMaterial({ color: L.iris })); ig.add(ir);
      const pu = new THREE.Mesh(new THREE.CircleGeometry(0.0072, 16), new THREE.MeshBasicMaterial({ color: "#050505" })); pu.position.z = 0.0004; ig.add(pu);
      const hl = new THREE.Mesh(new THREE.CircleGeometry(0.0035, 10), glow(2.2, 2.2, 2.2)); hl.position.set(0.004, 0.005, 0.0008); ig.add(hl);
      ig.traverse((o) => o.layers.set(NOINK)); this.iris.push(ig);
      const br = M(new THREE.CapsuleGeometry(0.0075, 0.04, 3, 8), hairC); br.rotation.z = Math.PI / 2; br.position.set(s * 0.045, 0.062, 0.108); H.add(br); this.brows.push(br);
    }
    // miệng (dán cong trên mặt)
    const mg = new THREE.SphereGeometry(0.1215, 20, 10, Math.PI / 2 - 0.62, 1.24, 1.6, 0.62); this.mtex.neutral = mouthTex(L, "neutral"); this.mouth = new THREE.Mesh(mg, tm("#ffffff", this.mtex.neutral, { alphaTest: 0.4 })); this.mouth.scale.set(0.96 * Math.sqrt(w), 1.08, 1.0); this.mouth.layers.set(NOINK); H.add(this.mouth);
    // tóc
    const capG = new THREE.SphereGeometry(0.127, 28, 14, 0, Math.PI * 2, 0, L.hairStyle === "long" ? 1.9 : 1.72); const cap = M(capG, hairM); cap.scale.set(0.98 * Math.sqrt(w), 1.1, 1.04); cap.position.set(0, 0.014, -0.012); cap.rotation.x = -0.62; H.add(cap);
    const clump = (x: number, y: number, z: number, rx: number, rz: number, r = 0.032, h = 0.08) => { const c = M(new THREE.ConeGeometry(r, h, 8), hairC, x, y, z); c.rotation.set(rx, 0, rz); H.add(c); };
    if (L.hairStyle === "short") { for (let i = 0; i < 6; i++) clump(-0.075 + i * 0.03, 0.1, 0.078, 2.0, (i - 2.5) * 0.15, 0.026, 0.05); for (const s of [-1, 1]) { const sb = M(new THREE.BoxGeometry(0.012, 0.05, 0.025), hairC, s * 0.112 * Math.sqrt(w), 0.03, 0.03); H.add(sb); } }
    else if (L.hairStyle === "messy") { for (let i = 0; i < 9; i++) { const a = (i / 9) * Math.PI * 2; clump(Math.cos(a) * 0.06, 0.12 + Math.sin(i * 1.7) * 0.01, Math.sin(a) * 0.05 - 0.01, -0.6 + Math.sin(a) * 0.4, -Math.cos(a) * 0.6, 0.035, 0.09); }
      for (let i = 0; i < 5; i++) clump(-0.06 + i * 0.03, 0.098, 0.084, 1.95, (i - 2) * 0.25, 0.028, 0.065); }
    else { const back = M(new THREE.CapsuleGeometry(0.105, 0.3, 4, 14), hairM, 0, -0.2, -0.055); back.scale.set(1.05, 1, 0.55); H.add(back);
      for (const s of [-1, 1]) { const lock = M(new THREE.CapsuleGeometry(0.035, 0.26, 4, 10), hairC, s * 0.1, -0.15, 0.03); lock.rotation.z = s * 0.08; H.add(lock); }
      for (let i = 0; i < 5; i++) clump(-0.06 + i * 0.03, 0.08, 0.092, 2.25, (i - 2) * 0.2, 0.03, 0.07);
      const clip = M(new THREE.TorusGeometry(0.02, 0.006, 6, 12), tm("#e86a92"), 0.085, 0.07, 0.05); H.add(clip); }
    // tay: vai → khuỷu → cổ tay → bàn tay 5 ngón
    for (const s of [-1, 1]) {
      const shg = new THREE.Group(); shg.position.set(s * 0.205 * w, 1.37, 0); body.add(shg); this.sh.push(shg);
      const dl = sph(0.052 * Math.sqrt(w), topPlain, 1, 0.9, 0.85, 14); dl.position.x = -s * 0.012; shg.add(dl); shg.add(limb(0.05 * Math.sqrt(w), 0.2, topPlain));
      const elg = new THREE.Group(); elg.position.y = -0.28; shg.add(elg); this.el.push(elg);
      const rolled = L.kind === "mech"; elg.add(limb(0.043 * Math.sqrt(w), 0.19, rolled ? skin : topPlain));
      if (rolled) { const cf = M(new THREE.TorusGeometry(0.05 * Math.sqrt(w), 0.016, 6, 14), tm(L.top2), 0, -0.01, 0); cf.rotation.x = Math.PI / 2; elg.add(cf); }
      else { const cf = M(new THREE.CylinderGeometry(0.046, 0.046, 0.04, 14), tm(L.top2), 0, -0.23, 0); elg.add(cf); }
      const hg = new THREE.Group(); hg.position.y = -0.26; elg.add(hg); this.hand.push(hg);
      const palm = sph(0.04, skin, 0.55, 1.05, 1.0, 12); palm.position.y = -0.04; hg.add(palm);
      for (let f = 0; f < 4; f++) { const fg = new THREE.Group(); fg.position.set(0, -0.078, 0.027 - f * 0.018); fg.rotation.x = 0.2 + f * 0.05; fg.rotation.z = s * -0.15; hg.add(fg); fg.add(limb(0.0085, 0.035 - Math.abs(f - 1.2) * 0.004, skin)); }
      const th = new THREE.Group(); th.position.set(s * -0.012, -0.035, 0.032); th.rotation.set(0.5, 0, s * 0.6); hg.add(th); th.add(limb(0.0095, 0.03, skin));
    }
    // đồ đi kèm: khăn vắt vai (thợ), cờ lê, điện thoại
    if (false && L.kind === "mech") { const [c, x] = cvs(64, 256); x.fillStyle = "#f2efe6"; x.fillRect(0, 0, 64, 256); x.fillStyle = "#3a6ea5"; for (const y of [30, 40, 216, 226]) x.fillRect(0, y, 64, 5); x.fillStyle = "rgba(40,30,20,.4)"; x.beginPath(); x.arc(30, 140, 18, 0, 7); x.fill();
      const tw = new THREE.Group(); const tmM = tm("#ffffff", ctex(c), { side: THREE.DoubleSide }); const fr = M(new THREE.PlaneGeometry(0.1, 0.3), tmM, 0, -0.12, 0.13); fr.rotation.x = -0.12; tw.add(fr); const bk = M(new THREE.PlaneGeometry(0.1, 0.34), tmM, 0, -0.14, -0.13); bk.rotation.x = 0.15; tw.add(bk);
      const tp = M(new THREE.BoxGeometry(0.1, 0.012, 0.26), tmM, 0, 0.025, 0); tw.add(tp);
      tw.position.set(0.12 * w, 1.43, 0); body.add(tw); }
    const wr = new THREE.Group(); wr.add(M(new THREE.BoxGeometry(0.018, 0.2, 0.01), tm("#b5bac0"), 0, -0.06, 0)); const jaw2 = M(new THREE.TorusGeometry(0.025, 0.009, 6, 12, Math.PI * 1.4), tm("#b5bac0"), 0, -0.17, 0); jaw2.rotation.z = -Math.PI * 0.2; wr.add(jaw2); wr.add(M(new THREE.BoxGeometry(0.022, 0.07, 0.014), tm("#c8202f"), 0, 0.03, 0)); wr.position.set(0, -0.06, 0.02); wr.rotation.x = 1.2; this.hand[1].add(wr); this.props.wrench = wr;
    const ph = new THREE.Group(); ph.add(M(new THREE.BoxGeometry(0.075, 0.15, 0.009), tm("#1a1a1e"))); const scr = new THREE.Mesh(new THREE.PlaneGeometry(0.066, 0.135), glow(0.6, 0.9, 1.4)); scr.position.z = 0.0052; ph.add(scr); ph.position.set(0, -0.08, 0.03); ph.rotation.x = -0.3; this.hand[1].add(ph); this.props.phone = ph;
    this.root.traverse((o) => { if ((o as THREE.Mesh).isMesh && o.layers.mask !== 1 << NOINK) { (o as THREE.Mesh).castShadow = true; } });
  }
  pose(p: Pose3) {
    this.root.position.set(...p.p); this.root.rotation.y = p.ry; this.head.rotation.set(0.06, p.head ?? 0, (p.head ?? 0) * -0.15);
    const fc = FACE[p.e]; [0, 1].forEach((i) => { const lid = fc.lid[i]; this.lids[i].rotation.x = -1.45 + lid * 2.6; const [dy, tilt] = fc.brow[i]; const s = i === 0 ? -1 : 1; this.brows[i].position.y = 0.062 + dy; this.brows[i].rotation.z = Math.PI / 2 + s * tilt; this.brows[i].rotation.y = s * 0.25;
      const g = p.gaze ?? 0; this.iris[i].position.x = s * 0.043 + g * 0.007; this.iris[i].position.y = 0.016 - (p.e === "worried" ? 0.003 : 0); this.iris[i].scale.setScalar(p.e === "dazed" ? 0.8 : 1); });
    if (!this.mtex[p.e]) this.mtex[p.e] = mouthTex(this.L, p.e); const mm = this.mouth.material as THREE.MeshLambertMaterial; if (mm.map !== this.mtex[p.e]) { mm.map = this.mtex[p.e]!; mm.needsUpdate = true; }
    const rest: Arm3 = { f: 0.05, out: 0.1, el: 0.15 };
    [p.armR ?? rest, p.armL ?? rest].forEach((a, i) => { const s = i === 0 ? -1 : 1; const sh = this.sh[i]; sh.rotation.set(-a.f, 0, s * a.out); this.el[i].rotation.set(-a.el, 0, 0); this.hand[i].rotation.set(0, (a.palm ?? 0) * -s, 0); });
    for (const [k, o] of Object.entries(this.props)) o.visible = p.prop === k;
  }
}

/** dựng các nhân vật cần dùng trong CAST3.shots, gắn vào set (nhóm con huỷ phép xoay 180° của set → toạ độ thế giới) */
export function buildCast3(set: THREE.Group) {
  const g = new THREE.Group(); g.rotation.y = Math.PI; set.add(g);
  const who = new Set<string>(); CAST3.shots.forEach((s) => s.forEach((p) => who.add(p.who)));
  const people: Record<string, Person3> = {}; for (const w of who) if (LOOKS[w]) { people[w] = new Person3(LOOKS[w]); g.add(people[w].root); people[w].root.visible = false; }
  g.userData.tick = (t: number) => { const shot = CAST3.shots[Math.min(CAST3.shots.length - 1, Math.max(0, Math.floor(t + 1e-4)))] ?? []; for (const p of Object.values(people)) p.root.visible = false;
    for (const p of shot) { const o = people[p.who]; if (!o) continue; o.root.visible = true; o.pose(p); } };
}
