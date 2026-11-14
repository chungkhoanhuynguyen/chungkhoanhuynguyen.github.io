// Nhân vật video "Vàng đỉnh": thẻ hoạt hình 2D đứng trong cảnh 3D (billboard trụ) + phụ kiện vẽ tay (tai nghe, nón lá, ô, áo mưa, nước mắt, điện thoại, túi vàng, hộp kim cương, cốc trà, tờ giấy).
import * as THREE from "three";
import { Pen, bodyFront, bodySide, Outfit as Outfit0, Expr, Prop, INK } from "../pho/toon";
export type Outfit = Outfit0 & { long?: boolean };
import { NOINK } from "../pho/ink";

export const DO: Outfit = { jacket: "#2b2d38", pants: "#3a3f52", boots: "#e9e6df", hat: "hair", hair: "#141215", belt: null, buttons: "#565b6e", build: "stout", skin: "#f3cfa8" };
export const NGAN: Outfit = { jacket: "#f39bb5", pants: "#5b4a6e", boots: "#f3e8dc", hat: "hair", hair: "#2a1d1b", belt: null, buttons: "#ffffff", skin: "#ffe0c6", long: true };
export const VEST: Outfit = { jacket: "#1f2430", pants: "#1f2430", boots: "#111", hat: "hair", hair: "#3a2a20", belt: null, buttons: "#c9a64a", skin: "#e8c39e", moustache: "#2a1d18" };
export const ME2: Outfit = { jacket: "#7a5a3c", pants: "#2e2c30", boots: "#5a3b2a", hat: "hair", hair: "#cfcac4", belt: null, buttons: "#d8c7a8", build: "stout", skin: "#eec39a" };
export const CLERK: Outfit = { jacket: "#c8202f", pants: "#2b2b33", boots: "#222", hat: "hair", hair: "#1d1616", belt: null, buttons: "#f2d36b", skin: "#ffdcc0", long: true };
export const GYM: Outfit = { jacket: "#2b2b2b", pants: "#3a4a6a", boots: "#f4f4f2", hat: "hair", hair: "#111", belt: null, buttons: "#2b2b2b", skin: "#c98a5a", build: "stout" };
export const BOXER: Outfit = { jacket: "#e23b2e", pants: "#1f2430", boots: "#f4f4f2", hat: "cap", cap: "#111", belt: null, buttons: "#e23b2e", skin: "#d9a77e", build: "stout" };
export const XOI: Outfit = { jacket: "#8a3fa0", pants: "#2e2c30", boots: "#5a3b2a", hat: "hair", hair: "#241a18", belt: null, buttons: "#e8d8f0", build: "stout", skin: "#f1c9a0", long: true };
/** nhân vật phim #2 (Hùng Xa Lộ) – tra theo khoá cast */
export const OUT: Record<string, { o: Outfit; h: number; seed: number }> = {
  hung: { o: { jacket: "#3a6ea5", pants: "#3a3f52", boots: "#e9e6df", hat: "hair", hair: "#161214", belt: null, buttons: "#d8dde4", skin: "#e6b98e", build: "stout" }, h: 1.72, seed: 17 },
  huy: { o: { jacket: "#f4f6f8", pants: "#2b3346", boots: "#3a2a20", hat: "hair", hair: "#141215", belt: null, buttons: "#9aa3ab", skin: "#f1cfa8" }, h: 1.72, seed: 21 },
  dung: { o: { jacket: "#2b2b2b", pants: "#3a4a6a", boots: "#f4f4f2", hat: "hair", hair: "#111", belt: null, buttons: "#2b2b2b", skin: "#c98a5a", build: "stout" }, h: 1.8, seed: 23 },
  vy: { o: { jacket: "#c8202f", pants: "#1f2430", boots: "#f3e8dc", hat: "hair", hair: "#1c1416", belt: null, buttons: "#ffffff", skin: "#ffe0c6", long: true }, h: 1.6, seed: 29 },
  phu: { o: { jacket: "#6b4fa0", pants: "#1f2430", boots: "#111", hat: "hair", hair: "#3a2a20", belt: null, buttons: "#f2d36b", skin: "#e8c39e", moustache: "#2a1d18", build: "stout" }, h: 1.7, seed: 31 },
  thang: { o: { jacket: "#e0832a", pants: "#2f3546", boots: "#2a2a2a", hat: "cap", cap: "#111", belt: null, buttons: "#d8dde4", skin: "#ecd0b6" }, h: 1.68, seed: 37 },
  bohung: { o: { jacket: "#5a6a4a", pants: "#2e2c30", boots: "#5a3b2a", hat: "hair", hair: "#cfcac4", belt: null, buttons: "#d8c7a8", skin: "#e3b48c" }, h: 1.62, seed: 41 },
  mehung: { o: { jacket: "#8a5a3a", pants: "#2e2c30", boots: "#5a3b2a", hat: "hair", hair: "#6b625c", belt: null, buttons: "#d8c7a8", build: "stout", skin: "#eec39a", long: true }, h: 1.5, seed: 43 },
  lam: { o: { jacket: "#2f8a52", pants: "#3d3a36", boots: "#e9e6df", hat: "hair", hair: "#2a1d1b", belt: null, buttons: "#d8dde4", skin: "#ffe2c2" }, h: 1.66, seed: 47 },
  tu: { o: { jacket: "#9c2f45", pants: "#2e2c30", boots: "#5a3b2a", hat: "hair", hair: "#b9b6b2", belt: null, buttons: "#d8c7a8", skin: "#e3b48c", build: "stout" }, h: 1.6, seed: 53 },
  ba: { o: { jacket: "#8a3fa0", pants: "#2e2c30", boots: "#5a3b2a", hat: "hair", hair: "#241a18", belt: null, buttons: "#e8d8f0", build: "stout", skin: "#f1c9a0", long: true }, h: 1.55, seed: 59 },
  khach: { o: { jacket: "#4a4a52", pants: "#2f3546", boots: "#2a2a2a", hat: "hair", hair: "#151515", belt: null, buttons: "#d8dde4", skin: "#ecd0b6" }, h: 1.7, seed: 61 },
  nv: { o: { jacket: "#1f4e8a", pants: "#2b2b33", boots: "#222", hat: "hair", hair: "#1d1616", belt: null, buttons: "#f2d36b", skin: "#ffdcc0", long: true }, h: 1.58, seed: 67 },
  quang: { o: { jacket: "#4f6d8f", pants: "#2b3346", boots: "#3a2a20", hat: "hair", hair: "#1a1517", belt: null, buttons: "#e6ebf0", skin: "#efc9a2" }, h: 1.68, seed: 71 },
  trang: { o: { jacket: "#e86a92", pants: "#2b2b33", boots: "#f3e8dc", hat: "hair", hair: "#1c1416", belt: null, buttons: "#ffffff", skin: "#f6d2b2", long: true }, h: 1.47, seed: 73 },
  cuong: { o: { jacket: "#e8c22a", pants: "#1f2430", boots: "#f4f4f2", hat: "hair", hair: "#121212", belt: null, buttons: "#1f2430", skin: "#d9a77e", build: "stout" }, h: 1.74, seed: 79 },
  tai: { o: { jacket: "#2fa39a", pants: "#3a3f52", boots: "#e9e6df", hat: "cap", cap: "#d8212f", belt: null, buttons: "#d8dde4", skin: "#f2cfae" }, h: 1.66, seed: 83 },
  linh: { o: { jacket: "#b03ad0", pants: "#1f2430", boots: "#f3e8dc", hat: "hair", hair: "#3a1f16", belt: null, buttons: "#ffffff", skin: "#ffe0c6", long: true }, h: 1.6, seed: 89 },
};
const CROWD_J = ["#3a78c2", "#2f8a52", "#8a5a3a", "#6b4fa0", "#c9572e", "#4a4a52", "#9c2f45", "#2e6f7a", "#7a7f3a", "#d08a2a"];
const HAIR = ["#1c1719", "#2a1d1b", "#4a3426", "#b9b6b2", "#151515"];
export const crowd = (i: number): Outfit => ({ jacket: CROWD_J[i % CROWD_J.length], pants: ["#2f3546", "#3d3a36", "#26262b", "#4a4a42"][i % 4], boots: ["#2a2a2a", "#5a3b2a", "#e9e6df"][i % 3],
  hat: i % 5 === 3 ? "cap" : "hair", cap: ["#c0392b", "#2f6fd1", "#2f8a52"][i % 3], hair: HAIR[(i * 3) % HAIR.length], belt: null, buttons: "#d8dde4",
  skin: ["#ffe2c2", "#f5c9a0", "#ecd0b6", "#e3b48c"][i % 4], build: i % 4 === 1 ? "stout" : "adult", long: FEM(i) });
/** nhân vật quần chúng nữ (tóc dài, áo màu tươi) */
export const FEM = (i: number) => i % 5 !== 3 && (i % 3 === 1 || i % 7 === 4);

export type Acc = "gloves" | "muscle" | "headset" | "nonla" | "umbrella" | "raincoat" | "tears" | "phone" | "goldbag" | "gembox" | "cup" | "paper" | "sweat" | "zzz" | "glow" | "ring" | "flex" | "box" | "ticket" | "mega" | "xoi" | "glasses" | "mic" | "helmet" | "redbook";
export type Pose = { expr: Expr; blink?: boolean; mode?: "stand" | "sit" | "stroll" | "march"; phase?: number; tilt?: number; headTilt?: number; wave?: number; prop?: Prop; acc?: Acc[]; t?: number; umb?: string; side?: 1 | -1; reach?: [number, number]; num?: string };

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
      const long = !!this.o.long && !acc.includes("raincoat");
      if (p.side) { // nhìn nghiêng (quay mặt về phải; side = -1 thì lật gương): dùng cho cảnh hai người đối thoại, dắt xe
        if (p.side < 0) { g.translate(600, 0); g.scale(-1, 1); }
        if (long) { const G0 = bodyFront(pen, this.o, { expr: "neutral", mode: "stand", seed: this.seed }) as G; g.clearRect(0, 0, 600, 1000); const { hc, crown, chin, W, HH } = G0, hx = 304;
          g.fillStyle = this.o.hair ?? "#1c1719"; g.strokeStyle = INK; g.lineWidth = 6; g.lineJoin = "round"; g.beginPath(); g.moveTo(hx - W * 0.1, crown + 6); g.quadraticCurveTo(hx - W * 0.72, hc - (hc - crown) * 0.5, hx - W * 0.62, chin); g.quadraticCurveTo(hx - W * 0.66, chin + 0.42 * HH, hx - W * 0.3, chin + 0.5 * HH); g.quadraticCurveTo(hx - W * 0.02, chin + 0.3 * HH, hx - W * 0.05, hc); g.closePath(); g.fill(); g.stroke(); }
        bodySide(pen, this.o, { expr: p.expr, blink: p.blink ? 1 : 0, mode: p.mode === "stroll" || p.mode === "march" ? "march" : "stand", phase: p.phase ?? 0, stomp: 0.35, stride: 0.55, seed: this.seed, ...(p.reach ? { reach: true, pose: 1, hand: p.reach } : {}) });
        g.setTransform(1, 0, 0, 1, 0, 0); this.t.needsUpdate = true;
      } else {
      const fo = { expr: p.expr, blink: p.blink ? 1 : 0, mode: p.mode ?? "stand", seed: this.seed, wave: p.wave, phase: p.phase ?? 0, tilt: p.tilt ?? 0, headTilt: p.headTilt ?? 0,
        prop: p.prop ?? (acc.includes("flex") || acc.includes("box") ? "none" : acc.some((a) => a === "phone" || a === "goldbag" || a === "cup" || a === "gembox" || a === "paper" || a === "xoi" || a === "mic" || a === "redbook") ? (acc.includes("gembox") || acc.includes("paper") || acc.includes("redbook") ? "hold2" : "hold") : acc.includes("umbrella") || acc.includes("ticket") || acc.includes("mega") ? "up" : null) } as const;
      if (long) { const G0 = bodyFront(pen, this.o, fo as never); g.clearRect(0, 0, 600, 1000); if (G0) longHair(g, G0 as G, this.o.hair ?? "#1c1719", p.mode === "sit"); }
      if (acc.includes("umbrella")) umbrellaTop(g, p.umb ?? "#2b4f8a", -1);
      const G = bodyFront(pen, this.o, { expr: p.expr, blink: p.blink ? 1 : 0, mode: p.mode ?? "stand", seed: this.seed, wave: p.wave, phase: p.phase ?? 0, tilt: p.tilt ?? 0, headTilt: p.headTilt ?? 0,
        prop: p.prop ?? (acc.some((a) => a === "phone" || a === "goldbag" || a === "cup" || a === "gembox" || a === "paper") ? (acc.includes("gembox") || acc.includes("paper") || acc.includes("redbook") ? "hold2" : "hold") : acc.includes("umbrella") ? "up" : null) });
      if (G) { drawAcc(g, pen, G, acc, p.t ?? 0, p.umb, p.num, this.o.skin ?? "#f3cfa8"); }
      this.t.needsUpdate = true; }
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
/** tóc dài nữ: mảng tóc sau lưng xoã qua vai (vẽ trước thân) + hai lọn ôm má (vẽ sau thân) */
function longHair(g: CanvasRenderingContext2D, G: G, col: string, sit: boolean) { const { hc, crown, chin, W, HH } = G, bot = chin + (sit ? 0.42 : 0.55) * HH;
  g.save(); g.lineJoin = "round"; g.fillStyle = col; g.strokeStyle = INK; g.lineWidth = 6; g.beginPath(); g.moveTo(300 - W * 0.56, hc - (hc - crown) * 0.3);
  g.quadraticCurveTo(300 - W * 0.82, chin, 300 - W * 0.7, bot); g.quadraticCurveTo(300, bot + 0.07 * HH, 300 + W * 0.7, bot); g.quadraticCurveTo(300 + W * 0.82, chin, 300 + W * 0.56, hc - (hc - crown) * 0.3); g.closePath(); g.fill(); g.stroke(); g.restore(); }
function longLocks(g: CanvasRenderingContext2D, G: G, col: string) { const { hc, chin, W, HH, u } = G;
  g.save(); g.lineJoin = "round"; g.fillStyle = col; g.strokeStyle = INK; g.lineWidth = 4;
  for (const s of [-1, 1]) { g.beginPath(); g.moveTo(300 + s * W * 0.5, hc - 14 * u); g.quadraticCurveTo(300 + s * W * 0.62, chin, 300 + s * W * 0.5, chin + 0.3 * HH); g.quadraticCurveTo(300 + s * W * 0.45, chin + 0.16 * HH, 300 + s * W * 0.475, hc + 4 * u); g.closePath(); g.fill(); g.stroke(); }
  g.restore(); }
function drawAcc(g: CanvasRenderingContext2D, p: Pen, G: G, acc: Acc[], t: number, _umb?: string, num?: string, skin = "#f3cfa8") {
  if (acc.includes("glasses")) { const { hc, W, u } = G; g.save(); g.strokeStyle = INK; g.lineWidth = 3.5 * u; for (const sx of [-1, 1]) { g.beginPath(); g.ellipse(300 + sx * W * 0.2, hc - 1 * u, 12 * u, 10 * u, 0, 0, 7); g.stroke(); } g.beginPath(); g.moveTo(300 - W * 0.08, hc - 2 * u); g.lineTo(300 + W * 0.08, hc - 2 * u); g.stroke(); g.restore(); }
  if (acc.includes("helmet")) { const { hc, crown, W, u } = G; g.save(); g.fillStyle = "#2fa84a"; g.strokeStyle = INK; g.lineWidth = 5; g.beginPath(); g.ellipse(300, crown + (hc - crown) * 0.35, W * 0.6, (hc - crown) * 0.75, 0, Math.PI, 0); g.closePath(); g.fill(); g.stroke(); g.fillStyle = "#1d6b2e"; g.fillRect(300 - W * 0.62, crown + (hc - crown) * 0.3, W * 1.24, 6 * u); g.restore(); }
  if (acc.includes("mic")) { const R2 = G.hands[G.hands.length - 1], u = G.u; g.save(); g.strokeStyle = INK; g.lineWidth = 7 * u; g.beginPath(); g.moveTo(R2[0], R2[1]); g.lineTo(R2[0] - 8 * u, R2[1] - 30 * u); g.stroke(); g.fillStyle = "#222"; g.beginPath(); g.arc(R2[0] - 10 * u, R2[1] - 36 * u, 9 * u, 0, 7); g.fill(); g.restore(); p.dot(R2[0], R2[1], 5.5 * u); }
  if (acc.includes("redbook")) { const x = (G.hands[0][0] + G.hands[G.hands.length - 1][0]) / 2, y = (G.hands[0][1] + G.hands[G.hands.length - 1][1]) / 2, u = G.u; g.save(); g.fillStyle = "#c8202f"; g.strokeStyle = INK; g.lineWidth = 4; g.fillRect(x - 26 * u, y - 36 * u, 52 * u, 40 * u); g.strokeRect(x - 26 * u, y - 36 * u, 52 * u, 40 * u); g.fillStyle = "#f5c518"; g.beginPath(); g.arc(x, y - 18 * u, 8 * u, 0, 7); g.fill(); g.restore(); }
  if (acc.includes("flex")) { // dân gym khoe cơ: hai tay gồng, bắp tay to phồng theo nhịp
    const { chin, tcx, Ta, HH, u } = G, k = 0.5 + 0.5 * Math.sin(t * 5); g.save(); g.lineCap = "round"; g.lineJoin = "round";
    for (const s of [-1, 1]) { const S = [tcx + s * Ta * 0.92, chin + 0.13 * HH], E = [tcx + s * Ta * 2.05, chin + (0.1 - 0.05 * k) * HH], Fz = [tcx + s * Ta * 1.6, chin - (0.32 + 0.05 * k) * HH];
      for (const [w, c] of [[30 * u, INK], [24 * u, skin]] as const) { g.strokeStyle = c; g.lineWidth = w; g.beginPath(); g.moveTo(S[0], S[1]); g.lineTo(E[0], E[1]); g.lineTo(Fz[0], Fz[1]); g.stroke(); }
      g.fillStyle = skin; g.strokeStyle = INK; g.lineWidth = 4; g.beginPath(); g.ellipse((S[0] + E[0]) / 2, (S[1] + E[1]) / 2 - (10 + 8 * k) * u, 26 * u, (17 + 7 * k) * u, s * 0.1, 0, 7); g.fill(); g.stroke();
      g.beginPath(); g.arc(Fz[0], Fz[1], 13 * u, 0, 7); g.fill(); g.stroke();
      g.strokeStyle = "rgba(255,255,255,.75)"; g.lineWidth = 3; g.beginPath(); g.arc((S[0] + E[0]) / 2 - s * 4 * u, (S[1] + E[1]) / 2 - (14 + 8 * k) * u, 12 * u, Math.PI * 1.1, Math.PI * 1.6); g.stroke(); }
    g.restore(); }
  if (acc.includes("box")) { // dân boxing đấm gió: tay thủ che cằm, tay kia tung thẳng, đổi tay liên tục + vệt gió
    const { chin, tcx, Ta, HH, u } = G, ph = (t * 3.2) % 2, s = ph < 1 ? 1 : -1, e = Math.sin(Math.PI * (ph % 1)); g.save(); g.lineCap = "round"; g.lineJoin = "round";
    const arm = (S: number[], E: number[], Fz: number[], big: boolean) => { for (const [w, c] of [[24 * u, INK], [18 * u, skin]] as const) { g.strokeStyle = c; g.lineWidth = w; g.beginPath(); g.moveTo(S[0], S[1]); g.lineTo(E[0], E[1]); g.lineTo(Fz[0], Fz[1]); g.stroke(); }
      g.fillStyle = "#d8212f"; g.strokeStyle = INK; g.lineWidth = 4; g.beginPath(); g.ellipse(Fz[0], Fz[1], (big ? 21 : 17) * u, (big ? 18 : 15) * u, 0, 0, 7); g.fill(); g.stroke(); g.fillStyle = "#fff"; g.fillRect(Fz[0] - 9 * u, Fz[1] - 3 * u, 18 * u, 5 * u); };
    arm([tcx - s * Ta * 0.9, chin + 0.13 * HH], [tcx - s * Ta * 1.35, chin + 0.36 * HH], [tcx - s * Ta * 0.55, chin + 0.04 * HH], false);
    const fx = tcx + s * Ta * (1.2 + 1.9 * e); arm([tcx + s * Ta * 0.9, chin + 0.13 * HH], [tcx + s * Ta * (1.3 + 0.7 * e), chin + (0.3 - 0.14 * e) * HH], [fx, chin + (0.08 + 0.06 * e) * HH], true);
    if (e > 0.45) { g.strokeStyle = "rgba(255,255,255,.9)"; g.lineWidth = 5; for (const dy of [-22, 0, 22]) { g.beginPath(); g.moveTo(fx + s * 30 * u, chin + 0.12 * HH + dy * u); g.lineTo(fx + s * (52 + (dy ? 0 : 14)) * u, chin + 0.12 * HH + dy * u * 1.3); g.stroke(); } }
    g.restore(); }
  if (acc.includes("ticket")) { const R2 = G.hands[G.hands.length - 1], x = R2[0], y = R2[1], u = G.u; g.save(); g.translate(x, y - 22 * u); g.rotate(0.08); g.fillStyle = "#fffbe8"; g.strokeStyle = INK; g.lineWidth = 4; g.fillRect(-26 * u, -24 * u, 52 * u, 40 * u); g.strokeRect(-26 * u, -24 * u, 52 * u, 40 * u);
    g.fillStyle = "#c8202f"; g.font = `900 ${Math.round(26 * u)}px 'DejaVu Sans'`; g.textAlign = "center"; g.fillText(num ?? "102", 0, 8 * u); g.restore(); p.dot(x, y, 5.5 * u); }
  if (acc.includes("mega")) { const R2 = G.hands[G.hands.length - 1], x = R2[0], y = R2[1], u = G.u; g.save(); g.fillStyle = "#e9e6df"; g.strokeStyle = INK; g.lineWidth = 4; g.beginPath(); g.moveTo(x - 6 * u, y - 10 * u); g.lineTo(x + 46 * u, y - 30 * u); g.lineTo(x + 46 * u, y + 14 * u); g.lineTo(x - 6 * u, y - 2 * u); g.closePath(); g.fill(); g.stroke();
    g.fillStyle = "#c8202f"; g.fillRect(x - 14 * u, y - 12 * u, 10 * u, 14 * u); g.strokeRect(x - 14 * u, y - 12 * u, 10 * u, 14 * u);
    const k = (t * 3) % 1; g.strokeStyle = `rgba(255,255,255,${1 - k})`; g.lineWidth = 4; for (const r of [14, 26]) { g.beginPath(); g.arc(x + 50 * u, y - 8 * u, (r + k * 12) * u, -0.7, 0.7); g.stroke(); } g.restore(); p.dot(x, y, 5.5 * u); }
  if (acc.includes("xoi")) { const R2 = G.hands[G.hands.length - 1], x = R2[0], y = R2[1], u = G.u; g.save(); g.fillStyle = "#3f8a3a"; g.strokeStyle = INK; g.lineWidth = 4; g.beginPath(); g.ellipse(x, y - 6 * u, 22 * u, 13 * u, 0, 0, 7); g.fill(); g.stroke(); g.fillStyle = "#f6d24a"; g.beginPath(); g.ellipse(x, y - 11 * u, 15 * u, 9 * u, 0, Math.PI, 0); g.fill(); g.stroke(); g.restore(); p.dot(x, y, 5.5 * u); }
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
