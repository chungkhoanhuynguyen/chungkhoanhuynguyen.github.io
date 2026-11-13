// Nhân vật video "Vàng đỉnh": thẻ hoạt hình 2D đứng trong cảnh 3D (billboard trụ) + phụ kiện vẽ tay (tai nghe, nón lá, ô, áo mưa, nước mắt, điện thoại, túi vàng, hộp kim cương, cốc trà, tờ giấy).
import * as THREE from "three";
import { Pen, bodyFront, Outfit, Expr, Prop, INK } from "../pho/toon";
import { NOINK } from "../pho/ink";

export const DO: Outfit = { jacket: "#2b2d38", pants: "#3a3f52", boots: "#e9e6df", hat: "hair", hair: "#141215", belt: null, buttons: "#565b6e", build: "stout", skin: "#f3cfa8" };
export const NGAN: Outfit = { jacket: "#f39bb5", pants: "#5b4a6e", boots: "#f3e8dc", hat: "hair", hair: "#2a1d1b", belt: null, buttons: "#ffffff", skin: "#ffe0c6" };
export const VEST: Outfit = { jacket: "#1f2430", pants: "#1f2430", boots: "#111", hat: "hair", hair: "#3a2a20", belt: null, buttons: "#c9a64a", skin: "#e8c39e", moustache: "#2a1d18" };
export const ME2: Outfit = { jacket: "#7a5a3c", pants: "#2e2c30", boots: "#5a3b2a", hat: "hair", hair: "#cfcac4", belt: null, buttons: "#d8c7a8", build: "stout", skin: "#eec39a" };
export const CLERK: Outfit = { jacket: "#c8202f", pants: "#2b2b33", boots: "#222", hat: "hair", hair: "#1d1616", belt: null, buttons: "#f2d36b", skin: "#ffdcc0" };
const CROWD_J = ["#3a78c2", "#2f8a52", "#8a5a3a", "#6b4fa0", "#c9572e", "#4a4a52", "#9c2f45", "#2e6f7a", "#7a7f3a", "#d08a2a"];
const HAIR = ["#1c1719", "#2a1d1b", "#4a3426", "#b9b6b2", "#151515"];
export const crowd = (i: number): Outfit => ({ jacket: CROWD_J[i % CROWD_J.length], pants: ["#2f3546", "#3d3a36", "#26262b", "#4a4a42"][i % 4], boots: ["#2a2a2a", "#5a3b2a", "#e9e6df"][i % 3],
  hat: i % 5 === 3 ? "cap" : "hair", cap: ["#c0392b", "#2f6fd1", "#2f8a52"][i % 3], hair: HAIR[(i * 3) % HAIR.length], belt: null, buttons: "#d8dde4",
  skin: ["#ffe2c2", "#f5c9a0", "#ecd0b6", "#e3b48c"][i % 4], build: i % 4 === 1 ? "stout" : "adult" });

export type Acc = "gloves" | "muscle" | "headset" | "nonla" | "umbrella" | "raincoat" | "tears" | "phone" | "goldbag" | "gembox" | "cup" | "paper" | "sweat" | "zzz" | "glow" | "ring";
export type Pose = { expr: Expr; blink?: boolean; mode?: "stand" | "sit" | "stroll" | "march"; phase?: number; tilt?: number; headTilt?: number; wave?: number; prop?: Prop; acc?: Acc[]; t?: number; umb?: string };

export class Actor {
  root = new THREE.Group();
  card: THREE.Mesh;
  shadow: THREE.Mesh;
  private c: HTMLCanvasElement; private g: CanvasRenderingContext2D; private t: THREE.CanvasTexture; private key = "";
  constructor(public o: Outfit, public h = 1.72, public seed = 3) {
    this.c = document.createElement("canvas"); this.c.width = 600; this.c.height = 1000; this.g = this.c.getContext("2d")!;
    this.t = new THREE.CanvasTexture(this.c); this.t.colorSpace = THREE.SRGBColorSpace;
    const H = h / 0.95, W = H * 0.6; const geo = new THREE.PlaneGeometry(W, H); geo.translate(0, H / 2 - H * 0.025, 0);
    const mat = new THREE.MeshBasicMaterial({ map: this.t, alphaTest: 0.45, side: THREE.DoubleSide });
    // nhân vật là thẻ phẳng: đẩy độ sâu về phía camera ~0,45 m để ghế/giường/ghế đá nằm "trong thân người" không cắt xuyên qua hình
    mat.onBeforeCompile = (sh) => { sh.vertexShader = sh.vertexShader.replace("#include <project_vertex>", "#include <project_vertex>\n{ vec4 q = projectionMatrix * ( mvPosition + vec4( 0.0, 0.0, 0.45, 0.0 ) ); gl_Position.z = q.z / q.w * gl_Position.w; }"); };
    mat.customProgramCacheKey = () => "cardBias45";
    this.card = new THREE.Mesh(geo, mat); this.card.layers.set(NOINK);
    this.shadow = new THREE.Mesh(new THREE.CircleGeometry(0.42, 24), new THREE.MeshBasicMaterial({ color: "#1d1a2a", transparent: true, opacity: 0.35, depthWrite: false }));
    this.shadow.rotation.x = -Math.PI / 2; this.shadow.scale.set(1, 0.45, 1); this.shadow.position.y = 0.02; this.shadow.layers.set(NOINK);
    this.root.add(this.card, this.shadow);
  }
  pose(p: Pose, cam: THREE.Camera, tint: THREE.Color) {
    const k = JSON.stringify(p);
    if (k !== this.key) {
      this.key = k; const g = this.g; g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, 600, 1000);
      const pen = new Pen(g), acc = p.acc ?? [];
      if (acc.includes("umbrella")) umbrellaTop(g, p.umb ?? "#2b4f8a", -1);
      const G = bodyFront(pen, this.o, { expr: p.expr, blink: p.blink ? 1 : 0, mode: p.mode ?? "stand", seed: this.seed, wave: p.wave, phase: p.phase ?? 0, tilt: p.tilt ?? 0, headTilt: p.headTilt ?? 0,
        prop: p.prop ?? (acc.some((a) => a === "phone" || a === "goldbag" || a === "cup" || a === "gembox" || a === "paper") ? (acc.includes("gembox") || acc.includes("paper") ? "hold2" : "hold") : acc.includes("umbrella") ? "up" : null) });
      if (G) drawAcc(g, pen, G, acc, p.t ?? 0, p.umb);
      this.t.needsUpdate = true;
    }
    (this.card.material as THREE.MeshBasicMaterial).color.copy(tint);
    const wp = this.root.getWorldPosition(new THREE.Vector3());
    this.card.rotation.y = Math.atan2(cam.position.x - wp.x, cam.position.z - wp.z) - this.root.rotation.y;
  }
}

type G = { hc: number; crown: number; chin: number; W: number; HH: number; u: number; sole: number; torsoBot: number; tcx: number; Ta: number; hands: [number, number][] };
function umbrellaTop(g: CanvasRenderingContext2D, col: string, _s: number) {
  // canopy drawn first (behind head would hide face) – sits high above the head
  g.save(); g.lineJoin = "round";
  g.beginPath(); g.moveTo(40, 150); g.quadraticCurveTo(300, -40, 560, 150);
  for (let i = 0; i < 6; i++) { const x0 = 560 - i * 86.7, x1 = x0 - 86.7; g.quadraticCurveTo((x0 + x1) / 2, 120, x1, 150); }
  g.closePath(); g.fillStyle = col; g.fill(); g.lineWidth = 9; g.strokeStyle = INK; g.stroke();
  g.strokeStyle = "rgba(255,255,255,.35)"; g.lineWidth = 5; for (const x of [170, 300, 430]) { g.beginPath(); g.moveTo(300, 52); g.quadraticCurveTo(x, 90, x, 146); g.stroke(); }
  g.restore();
}
function drawAcc(g: CanvasRenderingContext2D, p: Pen, G: G, acc: Acc[], t: number, _umb?: string) {
  const { hc, crown, W, u, chin, tcx, Ta, HH } = G; const R = G.hands[G.hands.length - 1] ?? [tcx + 40, chin + 60], L = G.hands[0] ?? R;
  if (acc.includes("umbrella")) { g.save(); g.strokeStyle = INK; g.lineWidth = 7; g.beginPath(); g.moveTo(300, 60); g.lineTo(R[0] - 6, R[1]); g.stroke(); g.restore(); p.dot(R[0], R[1], 5.5 * u); }
  if (acc.includes("raincoat")) { // áo mưa: thân áo trong suốt có khoá kéo + mũ trùm ôm sát đầu, dây rút dưới cằm
    const ry = (chin - crown) / 2, rx = W * 0.5, top = chin + 0.04 * HH, bot = G.torsoBot + 0.38 * HH;
    g.save(); g.lineJoin = "round"; g.globalAlpha = 0.62; g.fillStyle = "#58b4d6";
    g.beginPath(); g.moveTo(tcx - Ta * 0.95, top); g.lineTo(tcx + Ta * 0.95, top); g.lineTo(tcx + Ta * 1.45, bot); g.quadraticCurveTo(tcx, bot + 0.06 * HH, tcx - Ta * 1.45, bot); g.closePath(); g.fill();
    g.globalAlpha = 1; g.lineWidth = 4.5; g.strokeStyle = "#1f6a87"; g.stroke();
    g.strokeStyle = "rgba(255,255,255,.55)"; g.lineWidth = 4; g.beginPath(); g.moveTo(tcx - Ta * 0.55, top + 0.1 * HH); g.lineTo(tcx - Ta * 0.8, bot - 0.1 * HH); g.stroke();
    g.strokeStyle = "#1f6a87"; g.lineWidth = 3; g.beginPath(); g.moveTo(tcx, top); g.lineTo(tcx, bot); g.stroke();
    // mũ trùm: vành ôm quanh mặt (vòng ngoài – vòng trong), chỉ phủ trên cằm
    g.globalAlpha = 0.9; g.fillStyle = "#4aa6cc"; g.beginPath();
    g.ellipse(300, hc - 2 * u, rx * 1.2, ry * 1.18, 0, 0, Math.PI * 2); g.ellipse(300, hc + 3 * u, rx * 0.86, ry * 0.86, 0, 0, Math.PI * 2, true);
    g.save(); g.beginPath(); g.rect(0, 0, 600, hc + ry * 0.7); g.clip(); g.beginPath(); g.ellipse(300, hc - 2 * u, rx * 1.2, ry * 1.18, 0, 0, Math.PI * 2); g.ellipse(300, hc + 3 * u, rx * 0.86, ry * 0.86, 0, 0, Math.PI * 2, true); g.fill("evenodd");
    g.globalAlpha = 1; g.lineWidth = 4.5; g.strokeStyle = "#1f6a87"; g.beginPath(); g.ellipse(300, hc - 2 * u, rx * 1.2, ry * 1.18, 0, 0, Math.PI * 2); g.stroke(); g.restore();
    g.globalAlpha = 1; g.strokeStyle = "#f2f2f2"; g.lineWidth = 3;
    for (const sx of [-1, 1]) { g.beginPath(); g.moveTo(300 + sx * rx * 0.95, hc + ry * 0.62); g.quadraticCurveTo(300 + sx * rx * 0.4, chin + 4 * u, 300 + sx * 3 * u, chin + 10 * u); g.stroke(); }
    g.fillStyle = "#f2f2f2"; g.beginPath(); g.arc(300 - 4 * u, chin + 13 * u, 2.6 * u, 0, 7); g.arc(300 + 4 * u, chin + 13 * u, 2.6 * u, 0, 7); g.fill(); g.restore(); }
  if (acc.includes("headset")) { g.save(); g.strokeStyle = "#1a1a22"; g.lineWidth = 9 * u; g.beginPath(); g.ellipse(300, hc, W * 0.56, W * 0.6, 0, Math.PI * 1.05, Math.PI * 1.95); g.stroke();
    for (const s of [-1, 1]) { g.fillStyle = "#22222c"; g.beginPath(); g.ellipse(300 + s * W * 0.53, hc + 4 * u, 9 * u, 15 * u, 0, 0, 7); g.fill(); g.fillStyle = "#7b4dff"; g.beginPath(); g.ellipse(300 + s * W * 0.55, hc + 4 * u, 4 * u, 9 * u, 0, 0, 7); g.fill(); }
    g.strokeStyle = "#1a1a22"; g.lineWidth = 3.5 * u; g.beginPath(); g.moveTo(300 - W * 0.53, hc + 14 * u); g.quadraticCurveTo(300 - W * 0.45, hc + 34 * u, 300 - W * 0.18, hc + 30 * u); g.stroke(); g.restore(); }
  if (acc.includes("nonla")) { g.save(); g.fillStyle = "#f2e2b4"; g.strokeStyle = INK; g.lineWidth = 6; g.beginPath(); g.moveTo(300, crown - 0.55 * W); g.lineTo(300 + W * 0.95, crown + 0.08 * W); g.quadraticCurveTo(300, crown + 0.2 * W, 300 - W * 0.95, crown + 0.08 * W); g.closePath(); g.fill(); g.stroke();
    g.strokeStyle = "rgba(140,110,50,.6)"; g.lineWidth = 3; for (let i = 1; i < 4; i++) { g.beginPath(); g.moveTo(300, crown - 0.55 * W); g.lineTo(300 - W * 0.95 + i * 0.475 * W, crown + 0.12 * W); g.stroke(); } g.restore(); }
  if (acc.includes("tears")) { const k = (t * 0.9) % 1; g.save(); g.fillStyle = "#6ec6ff"; g.strokeStyle = "#2a7fc0"; g.lineWidth = 2;
    for (const s of [-1, 1]) for (const d of [0, 0.5]) { const kk = (k + d) % 1, x = 300 + s * W * 0.2, y = hc + 6 * u + kk * 0.5 * HH; g.globalAlpha = 1 - kk; g.beginPath(); g.ellipse(x, y, 3.2 * u, 5 * u, 0, 0, 7); g.fill(); g.stroke(); }
    g.globalAlpha = 0.8; g.fillStyle = "#8fd3ff"; for (const s of [-1, 1]) { g.fillRect(300 + s * W * 0.2 - 2 * u, hc + 4 * u, 4 * u, 0.25 * HH); } g.restore(); }
  if (acc.includes("sweat")) { g.save(); g.fillStyle = "#9fdcff"; g.strokeStyle = "#2a7fc0"; g.lineWidth = 3; g.beginPath(); const x = 300 + W * 0.42, y = hc - 18 * u + ((t * 30) % 12) * u; g.moveTo(x, y - 9 * u); g.quadraticCurveTo(x + 7 * u, y + 3 * u, x, y + 6 * u); g.quadraticCurveTo(x - 7 * u, y + 3 * u, x, y - 9 * u); g.fill(); g.stroke(); g.restore(); }
  if (acc.includes("zzz")) { g.save(); g.fillStyle = "#e9eef5"; g.strokeStyle = INK; g.lineWidth = 3; g.font = "900 46px 'DejaVu Sans'"; const k = (t * 0.6) % 1; g.globalAlpha = 1 - k; g.strokeText("z", 300 + W * 0.6, crown - k * 60); g.fillText("z", 300 + W * 0.6, crown - k * 60); g.restore(); }
  if (acc.includes("phone")) { // điện thoại đời mới: viền mỏng, cụm 3 camera, "đảo" trên màn hình
    const [x, y] = R; g.save(); g.lineJoin = "round"; const w = 24 * u, h = 46 * u, x0 = x - w / 2, y0 = y - h + 6 * u, rr = 5 * u;
    const rnd = (X: number, Y: number, W2: number, H2: number, r2: number) => { g.beginPath(); g.moveTo(X + r2, Y); g.arcTo(X + W2, Y, X + W2, Y + H2, r2); g.arcTo(X + W2, Y + H2, X, Y + H2, r2); g.arcTo(X, Y + H2, X, Y, r2); g.arcTo(X, Y, X + W2, Y, r2); g.closePath(); };
    rnd(x0, y0, w, h, rr); g.fillStyle = "#8f8a84"; g.fill(); g.lineWidth = 3; g.strokeStyle = INK; g.stroke();
    rnd(x0 + 1.6 * u, y0 + 1.6 * u, w - 3.2 * u, h - 3.2 * u, rr * 0.8); g.fillStyle = acc.includes("glow") ? "#cfe8ff" : "#22324f"; g.fill();
    if (acc.includes("glow")) { g.fillStyle = "#2f6fd1"; g.fillRect(x0 + 4 * u, y0 + 12 * u, w - 8 * u, 6 * u); g.fillStyle = "#e9eef5"; g.fillRect(x0 + 4 * u, y0 + 21 * u, w - 8 * u, 4 * u); }
    g.fillStyle = "#0b0b0e"; rnd(x - 4.5 * u, y0 + 3 * u, 9 * u, 2.6 * u, 1.3 * u); g.fill(); g.restore(); p.dot(x, y, 5.5 * u); }
  if (acc.includes("cup")) { const [x, y] = R; g.save(); g.fillStyle = "#e9e1cf"; g.strokeStyle = INK; g.lineWidth = 4; g.fillRect(x - 10 * u, y - 18 * u, 20 * u, 22 * u); g.strokeRect(x - 10 * u, y - 18 * u, 20 * u, 22 * u); g.strokeStyle = "rgba(255,255,255,.8)"; g.lineWidth = 3;
    for (const d of [-4, 4]) { g.beginPath(); g.moveTo(x + d * u, y - 22 * u); g.quadraticCurveTo(x + (d + 5) * u, y - 32 * u - Math.sin(t * 4 + d) * 4 * u, x + d * u, y - 44 * u); g.stroke(); } g.restore(); p.dot(x, y, 5.5 * u); }
  if (acc.includes("goldbag")) { const [x, y] = R; g.save(); g.fillStyle = "#c8202f"; g.strokeStyle = INK; g.lineWidth = 4; g.fillRect(x - 16 * u, y - 4 * u, 32 * u, 30 * u); g.strokeRect(x - 16 * u, y - 4 * u, 32 * u, 30 * u); g.fillStyle = "#f5c518"; g.font = `900 ${Math.round(16 * u)}px 'DejaVu Sans'`; g.textAlign = "center"; g.fillText("VÀNG", x, y + 18 * u); g.restore(); p.dot(x, y, 5.5 * u); }
  if (acc.includes("gembox")) { const x = (L[0] + R[0]) / 2, y = (L[1] + R[1]) / 2; g.save(); g.fillStyle = "#8a1022"; g.strokeStyle = INK; g.lineWidth = 4; g.fillRect(x - 36 * u, y - 8 * u, 72 * u, 22 * u); g.strokeRect(x - 36 * u, y - 8 * u, 72 * u, 22 * u);
    g.fillStyle = "#b0182e"; g.fillRect(x - 36 * u, y - 34 * u, 72 * u, 26 * u); g.strokeRect(x - 36 * u, y - 34 * u, 72 * u, 26 * u);
    for (const d of [-20, 0, 20]) { g.fillStyle = "#e9fbff"; g.beginPath(); g.moveTo(x + d * u, y - 6 * u); g.lineTo(x + (d + 7) * u, y); g.lineTo(x + d * u, y + 10 * u); g.lineTo(x + (d - 7) * u, y); g.closePath(); g.fill(); g.lineWidth = 2; g.stroke();
      const s = 0.5 + 0.5 * Math.sin(t * 6 + d); g.strokeStyle = `rgba(255,255,255,${s})`; g.lineWidth = 3; g.beginPath(); g.moveTo(x + d * u, y - 16 * u); g.lineTo(x + d * u, y - 10 * u); g.stroke(); g.strokeStyle = INK; } g.restore();
    p.dot(L[0], L[1], 5.5 * u); p.dot(R[0], R[1], 5.5 * u); }
  if (acc.includes("paper")) { const x = (L[0] + R[0]) / 2, y = (L[1] + R[1]) / 2; g.save(); g.translate(x, y - 20 * u); g.rotate(-0.05); g.fillStyle = "#fbf6e8"; g.strokeStyle = INK; g.lineWidth = 3; g.fillRect(-30 * u, -36 * u, 60 * u, 64 * u); g.strokeRect(-30 * u, -36 * u, 60 * u, 64 * u);
    g.strokeStyle = "#8b857a"; g.lineWidth = 2; for (let i = 0; i < 5; i++) { g.beginPath(); g.moveTo(-22 * u, (-22 + i * 10) * u); g.lineTo(22 * u, (-22 + i * 10) * u); g.stroke(); } g.strokeStyle = "#d8372b"; g.lineWidth = 3; g.beginPath(); g.arc(14 * u, 14 * u, 9 * u, 0, 7); g.stroke(); g.restore();
    p.dot(L[0], L[1], 5.5 * u); p.dot(R[0], R[1], 5.5 * u); }
  if (acc.includes("gloves")) for (const [x, y] of G.hands) { g.save(); g.fillStyle = "#d8212f"; g.strokeStyle = INK; g.lineWidth = 4; g.beginPath(); g.ellipse(x, y, 13 * u, 11 * u, 0, 0, 7); g.fill(); g.stroke(); g.fillStyle = "#fff"; g.fillRect(x - 10 * u, y + 7 * u, 20 * u, 4 * u); g.restore(); }
  if (acc.includes("muscle")) { g.save(); g.fillStyle = "#c98a5a"; g.strokeStyle = INK; g.lineWidth = 4;
    for (const s2 of [-1, 1]) { g.beginPath(); g.ellipse(tcx + s2 * Ta * 1.12, chin + 0.32 * HH, 15 * u, 22 * u, s2 * 0.3, 0, 7); g.fill(); g.stroke(); }
    g.strokeStyle = "rgba(60,30,20,.45)"; g.lineWidth = 3; g.beginPath(); g.moveTo(tcx - Ta * 0.5, chin + 0.25 * HH); g.quadraticCurveTo(tcx, chin + 0.35 * HH, tcx + Ta * 0.5, chin + 0.25 * HH); g.stroke(); g.restore(); }
  if (acc.includes("ring")) { const [x, y] = R; g.save(); g.strokeStyle = "#f5c518"; g.lineWidth = 5 * u; g.beginPath(); g.arc(x, y - 12 * u, 9 * u, 0, 7); g.stroke(); g.restore(); }
}
