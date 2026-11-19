// SUAXE2 (thử nghiệm 19/11/2026) – tiệm sửa xe máy Hà Nội bản CHI TIẾT kiểu phim hoạt hình chiếu rạp.
// Giữ chất toon của xưởng (vật liệu 2 tông + viền mực InkPass) nhưng thêm: ~40 mô hình CC0 Poly Haven đổi sang vật liệu
// toon giữ màu texture gốc (texture đã làm mềm kiểu tranh vẽ), tường vữa ố/rêu/bong sơn, sàn xi măng loang dầu, dây điện
// võng, mái tôn, biển hiệu + giấy dán tiếng Việt, bàn thờ Thần Tài, xe số dựng hình học, đèn ấm + bóng đổ + AO giả
// (bóng tiếp xúc dưới đồ vật, tối góc tường), vệt nắng + bụi bay.
// Toạ độ dựng giống buildSuaXe (tường sau z = -3, cửa ra phố z = +5, rồi xoay 180°) → dùng chung góc máy, chỗ đứng nhân vật.
// Vùng trống cho nhân vật (toạ độ trước khi xoay): x -1.6..0.6, z -1.6..0.6.
import * as THREE from "three";
import { staticFile, delayRender, continueRender } from "remotion";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { rng } from "../pho/paint";
import { LFB } from "../pho/shade";
import { NOINK } from "../pho/ink";

const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";
type V3 = [number, number, number];

// ---------------- vật liệu toon riêng của set (2 tông nắng + ánh đèn ấm mềm + ambient bán cầu) ----------------
const NL = 5; // số đèn ấm tối đa
const U = {
  uSun: { value: new THREE.Vector3(1.55, 1.12, 0.72) },        // nắng chiều
  uAmbHi: { value: new THREE.Vector3(0.62, 0.55, 0.52) },      // trời / trần hắt xuống
  uAmbLo: { value: new THREE.Vector3(0.36, 0.3, 0.3) },        // sàn hắt lên
  uSat: { value: 1.08 },
  uLampP: { value: Array.from({ length: NL }, () => new THREE.Vector3(0, -99, 0)) },
  uLampC: { value: Array.from({ length: NL }, () => new THREE.Vector3()) },
  uLampR: { value: Array.from({ length: NL }, () => 1) },
};
const DECL = `#include <common>
uniform vec3 uSun; uniform vec3 uAmbHi; uniform vec3 uAmbLo; uniform float uSat;
uniform vec3 uLampP[${NL}]; uniform vec3 uLampC[${NL}]; uniform float uLampR[${NL}];`;
const SHADE = /* glsl */ `
#if NUM_DIR_LIGHTS > 0
{
  vec3 sunV = directionalLights[ 0 ].direction;
  vec3 upV = normalize( ( viewMatrix * vec4( 0.0, 1.0, 0.0, 0.0 ) ).xyz );
  float ndl = max( dot( geometryNormal, sunV ), 0.0 );
  float sunTerm = sunVis * smoothstep( 0.0, 0.22, ndl );
  float up = 0.5 + 0.5 * dot( geometryNormal, upV );
  vec3 alb = max( mix( vec3( dot( diffuseColor.rgb, vec3( 0.2126, 0.7152, 0.0722 ) ) ), diffuseColor.rgb, uSat ), 0.0 );
  vec3 lamp = vec3( 0.0 );
  for ( int i = 0; i < ${NL}; i ++ ) {
    vec3 lp = ( viewMatrix * vec4( uLampP[ i ], 1.0 ) ).xyz; vec3 d = lp - geometryPosition; float dist = length( d );
    float nl = max( dot( geometryNormal, d / dist ), 0.0 ); float att = clamp( 1.0 - dist / uLampR[ i ], 0.0, 1.0 ); att *= att;
    lamp += uLampC[ i ] * smoothstep( 0.0, 0.45, nl ) * att;
  }
  vec3 amb = mix( uAmbLo, uAmbHi, smoothstep( 0.1, 0.9, up ) );
  reflectedLight.directDiffuse = alb * ( amb + uSun * sunTerm * mix( 1.0, ndl, 0.25 ) + lamp );
  reflectedLight.indirectDiffuse = vec3( 0.0 );
}
#endif
`;
const matCache = new Map<string, THREE.MeshLambertMaterial>();
export function tm(color: THREE.ColorRepresentation = "#ffffff", map: THREE.Texture | null = null, o: { alphaTest?: number; side?: THREE.Side; vc?: boolean } = {}) {
  const key = map ? "" : `${new THREE.Color(color).getHexString()}_${o.side ?? 0}`;
  if (key && matCache.has(key)) return matCache.get(key)!;
  const m = new THREE.MeshLambertMaterial({ color, map, alphaTest: o.alphaTest ?? 0, side: o.side ?? THREE.FrontSide, vertexColors: !!o.vc });
  m.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, U);
    sh.fragmentShader = sh.fragmentShader.replace("#include <common>", DECL)
      .replace("#include <lights_fragment_begin>", "float sunVis = 1.0;\n" + LFB)
      .replace("#include <lights_fragment_end>", "#include <lights_fragment_end>\n" + SHADE);
  };
  m.customProgramCacheKey = () => "sx2toon1";
  if (key) matCache.set(key, m);
  return m;
}
const glow = (r: number, g: number, b: number) => new THREE.MeshBasicMaterial({ color: new THREE.Color(r, g, b) });

// ---------------- tiện ích hình học ----------------
const mesh = (geo: THREE.BufferGeometry, m: THREE.Material, x = 0, y = 0, z = 0, cast = true) => { const k = new THREE.Mesh(geo, m); k.position.set(x, y, z); k.castShadow = cast; k.receiveShadow = true; return k; };
const bx = (w: number, h: number, d: number, m: THREE.Material, x = 0, y = 0, z = 0, cast = true) => mesh(new THREE.BoxGeometry(w, h, d), m, x, y, z, cast);
const cy = (r1: number, r2: number, h: number, m: THREE.Material, x = 0, y = 0, z = 0, s = 16) => mesh(new THREE.CylinderGeometry(r1, r2, h, s), m, x, y, z);
const cvs = (w: number, h: number) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return [c, c.getContext("2d")!] as const; };
const ctex = (c: HTMLCanvasElement, rep?: [number, number]) => { const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; if (rep) { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(...rep); } return t; };
/** dây điện võng giữa 2 điểm */
function wire(a: V3, b: V3, sag: number, m: THREE.Material, r = 0.009) {
  const pts: THREE.Vector3[] = []; for (let i = 0; i <= 16; i++) { const t = i / 16; pts.push(new THREE.Vector3(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t - sag * 4 * t * (1 - t), a[2] + (b[2] - a[2]) * t)); }
  const k = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 24, r, 5), m); k.castShadow = true; return k;
}
/** đốm tối mềm (AO giả / bóng tiếp xúc / vết bẩn) dán trên mặt phẳng */
let blobTex: THREE.Texture | null = null;
function blob(w: number, d: number, op = 0.5, col = "#1a1210") {
  if (!blobTex) { const [c, x] = cvs(128, 128); const gr = x.createRadialGradient(64, 64, 4, 64, 64, 64); gr.addColorStop(0, "rgba(255,255,255,1)"); gr.addColorStop(0.55, "rgba(255,255,255,.55)"); gr.addColorStop(1, "rgba(255,255,255,0)"); x.fillStyle = gr; x.fillRect(0, 0, 128, 128); blobTex = new THREE.CanvasTexture(c); }
  const k = new THREE.Mesh(new THREE.PlaneGeometry(w, d), new THREE.MeshBasicMaterial({ color: col, alphaMap: blobTex, transparent: true, opacity: op, depthWrite: false, polygonOffset: true, polygonOffsetFactor: -2 }));
  k.rotation.x = -Math.PI / 2; k.layers.set(NOINK); k.renderOrder = 1; return k;
}

// ---------------- texture vẽ tay (canvas) ----------------
function grime(x: CanvasRenderingContext2D, W: number, H: number, r: () => number, n: number, col: string, rmin: number, rmax: number, a: number) {
  for (let i = 0; i < n; i++) { const px = r() * W, py = r() * H, rr = rmin + r() * (rmax - rmin); const g = x.createRadialGradient(px, py, 0, px, py, rr); g.addColorStop(0, col.replace("A", String(a * (0.4 + r() * 0.6)))); g.addColorStop(1, col.replace("A", "0")); x.fillStyle = g; x.fillRect(px - rr, py - rr, rr * 2, rr * 2); }
}
/** tường vữa vàng cũ: ố nước chảy từ trên, rêu + bẩn chân tường, mảng bong vữa lộ gạch, vết nứt, giấy quảng cáo dán */
function wallTex(wm: number, hm: number, seed: number, base: string, tileH = 1.1) {
  const PX = 170, W = Math.round(wm * PX), H = Math.round(hm * PX), r = rng(seed); const [c, x] = cvs(W, H);
  x.fillStyle = base; x.fillRect(0, 0, W, H);
  grime(x, W, H, r, 260, "rgba(255,245,220,A)", 20, 110, 0.18); grime(x, W, H, r, 220, "rgba(120,90,50,A)", 15, 90, 0.12);
  for (let i = 0; i < 70; i++) { const px = r() * W, len = H * (0.15 + r() * 0.45), w = 6 + r() * 26; const g = x.createLinearGradient(0, 0, 0, len); g.addColorStop(0, "rgba(95,75,45,.28)"); g.addColorStop(1, "rgba(95,75,45,0)"); x.fillStyle = g; x.fillRect(px, 0, w, len); }
  // mảng bong vữa lộ gạch đỏ
  for (let i = 0; i < 4; i++) { const px = r() * W, py = H * (0.15 + r() * 0.5), pw = 50 + r() * 100, ph = 30 + r() * 60;
    x.save(); x.beginPath(); for (let k = 0; k < 14; k++) { const a = (k / 14) * Math.PI * 2, rr = 0.75 + r() * 0.35; x.lineTo(px + Math.cos(a) * pw / 2 * rr, py + Math.sin(a) * ph / 2 * rr); } x.closePath(); x.clip();
    x.fillStyle = "#a8553a"; x.fillRect(px - pw, py - ph, pw * 2, ph * 2); x.strokeStyle = "#d8b9a0"; x.lineWidth = 3; for (let yy = py - ph; yy < py + ph; yy += 14) { x.beginPath(); x.moveTo(px - pw, yy); x.lineTo(px + pw, yy); x.stroke(); for (let xx = px - pw + ((yy / 14) % 2) * 15; xx < px + pw; xx += 30) { x.beginPath(); x.moveTo(xx, yy); x.lineTo(xx, yy + 14); x.stroke(); } }
    x.restore(); x.strokeStyle = "rgba(150,120,80,.35)"; x.lineWidth = 6; x.beginPath(); x.ellipse(px, py, pw / 2, ph / 2, 0, 0, 7); x.stroke(); }
  // vết nứt
  x.strokeStyle = "rgba(60,45,30,.55)"; x.lineWidth = 1.6; for (let i = 0; i < 10; i++) { let px = r() * W, py = r() * H * 0.7; x.beginPath(); x.moveTo(px, py); for (let k = 0; k < 9; k++) { px += (r() - 0.5) * 40; py += 8 + r() * 22; x.lineTo(px, py); } x.stroke(); }
  // chân tường: gạch men xanh cũ + rêu + bẩn bắn
  const ty = H - tileH * PX; x.fillStyle = "#5f8f7a"; x.fillRect(0, ty, W, H - ty);
  for (let yy = ty; yy < H; yy += 34) for (let xx = 0; xx < W; xx += 34) { x.fillStyle = `rgba(${r() < 0.5 ? "255,255,255" : "0,30,20"},${0.04 + r() * 0.08})`; x.fillRect(xx + 2, yy + 2, 30, 30); if (r() < 0.04) { x.fillStyle = "#c9cfc6"; x.fillRect(xx + 2, yy + 2, 30, 30); } }
  x.strokeStyle = "rgba(220,225,210,.7)"; x.lineWidth = 2.5; for (let yy = ty; yy < H; yy += 34) { x.beginPath(); x.moveTo(0, yy); x.lineTo(W, yy); x.stroke(); } for (let xx = 0; xx < W; xx += 34) { x.beginPath(); x.moveTo(xx, ty); x.lineTo(xx, H); x.stroke(); }
  x.fillStyle = "#e8e2cc"; x.fillRect(0, ty - 8, W, 8);
  const gb = x.createLinearGradient(0, H - 110, 0, H); gb.addColorStop(0, "rgba(40,30,20,0)"); gb.addColorStop(1, "rgba(40,30,20,.55)"); x.fillStyle = gb; x.fillRect(0, H - 110, W, 110);
  grime(x, W, H * 0.3, r, 90, "rgba(70,95,40,A)", 10, 50, 0.4); // rêu (vẽ vào dải trên? đặt lại toạ độ bên dưới)
  for (let i = 0; i < 160; i++) { const px = r() * W, py = H - r() * 90, rr = 3 + r() * 16; x.fillStyle = `rgba(${r() < 0.5 ? "60,80,35" : "50,40,30"},${0.2 + r() * 0.35})`; x.beginPath(); x.arc(px, py, rr, 0, 7); x.fill(); }
  // giấy quảng cáo dán tường kiểu Hà Nội
  const ads = ["KHOAN CẮT BÊ TÔNG", "HÚT BỂ PHỐT", "THÔNG TẮC CỐNG", "CHO VAY TIỀN NHANH", "SỬA ĐIỆN NƯỚC"];
  for (let i = 0; i < 9; i++) { const px = r() * (W - 130), py = H * (0.38 + r() * 0.3) - tileH * 40, aw = 110 + r() * 40, ah = 54;
    x.save(); x.translate(px, py); x.rotate((r() - 0.5) * 0.12); x.fillStyle = ["#f4f1e3", "#ffe25a", "#ffffff", "#ffd0d0"][i % 4]; x.globalAlpha = 0.75 + r() * 0.2; x.fillRect(0, 0, aw, ah);
    x.fillStyle = i % 3 ? "#c8202f" : "#1f3d8a"; x.font = `900 15px ${F}`; x.fillText(ads[i % ads.length], 6, 22, aw - 12); x.font = `800 17px ${F}`; x.fillText("09" + (12 + i) + ".xxx.xxx", 8, 44, aw - 14); x.restore(); }
  return ctex(c);
}
/** sàn xi măng: loang màu, vết dầu đen quanh chỗ sửa, vệt bánh xe, vết nứt, khe co giãn */
function floorTex(wm: number, dm: number, seed: number, oil: [number, number, number][]) {
  const PX = 150, W = Math.round(wm * PX), H = Math.round(dm * PX), r = rng(seed); const [c, x] = cvs(W, H);
  x.fillStyle = "#8f8a82"; x.fillRect(0, 0, W, H);
  grime(x, W, H, r, 420, "rgba(170,165,155,A)", 20, 120, 0.25); grime(x, W, H, r, 380, "rgba(60,55,50,A)", 10, 80, 0.16);
  for (let i = 0; i < 9000; i++) { x.fillStyle = `rgba(${r() < 0.5 ? "40,38,35" : "200,196,186"},${0.08 + r() * 0.12})`; x.fillRect(r() * W, r() * H, 2, 2); }
  x.strokeStyle = "rgba(55,50,45,.5)"; x.lineWidth = 2; for (let k = 1; k < 4; k++) { x.beginPath(); x.moveTo(0, (H * k) / 4 + (r() - 0.5) * 8); x.lineTo(W, (H * k) / 4 + (r() - 0.5) * 8); x.stroke(); }
  // vết dầu (toạ độ mét, gốc tại góc sàn)
  for (const [ox, oz, rr] of oil) for (let i = 0; i < 9; i++) { const px = (ox + (r() - 0.5) * rr) * PX, py = (oz + (r() - 0.5) * rr) * PX, q = (0.15 + r() * 0.5) * rr * PX;
    const g = x.createRadialGradient(px, py, 0, px, py, q); g.addColorStop(0, "rgba(28,24,22,.65)"); g.addColorStop(0.6, "rgba(35,30,28,.35)"); g.addColorStop(1, "rgba(35,30,28,0)"); x.fillStyle = g; x.beginPath(); x.ellipse(px, py, q, q * (0.6 + r() * 0.5), r() * 3, 0, 7); x.fill(); }
  // vệt bánh xe
  x.strokeStyle = "rgba(30,28,26,.18)"; x.lineWidth = 16; for (let i = 0; i < 7; i++) { x.beginPath(); const sx = r() * W; x.moveTo(sx, H); x.bezierCurveTo(sx + (r() - 0.5) * 300, H * 0.6, sx + (r() - 0.5) * 300, H * 0.35, sx + (r() - 0.5) * 400, H * (0.1 + r() * 0.3)); x.stroke(); }
  x.strokeStyle = "rgba(45,40,35,.6)"; x.lineWidth = 1.5; for (let i = 0; i < 12; i++) { let px = r() * W, py = r() * H; x.beginPath(); x.moveTo(px, py); for (let k = 0; k < 8; k++) { px += (r() - 0.5) * 50; py += (r() - 0.5) * 50; x.lineTo(px, py); } x.stroke(); }
  return ctex(c);
}
function woodTex(seed: number, base = "#7a5236") {
  const [c, x] = cvs(256, 256), r = rng(seed); x.fillStyle = base; x.fillRect(0, 0, 256, 256);
  for (let i = 0; i < 60; i++) { x.strokeStyle = `rgba(${r() < 0.5 ? "40,25,15" : "160,120,80"},${0.15 + r() * 0.2})`; x.lineWidth = 1 + r() * 3; x.beginPath(); const y = r() * 256; x.moveTo(0, y); x.bezierCurveTo(80, y + (r() - 0.5) * 20, 170, y + (r() - 0.5) * 20, 256, y + (r() - 0.5) * 10); x.stroke(); }
  grime(x, 256, 256, r, 30, "rgba(30,20,10,A)", 10, 40, 0.3); return ctex(c);
}
function metalTex(seed: number, base: string, rust = 0.5) {
  const [c, x] = cvs(256, 256), r = rng(seed); x.fillStyle = base; x.fillRect(0, 0, 256, 256);
  grime(x, 256, 256, r, 40, "rgba(255,255,255,A)", 10, 60, 0.08); grime(x, 256, 256, r, Math.round(60 * rust), "rgba(130,60,25,A)", 4, 30, 0.55); grime(x, 256, 256, r, 40, "rgba(20,20,20,A)", 8, 40, 0.2); return ctex(c);
}
/** biển hiệu tôn sơn: chữ to, viền gỉ, đinh vít */
function signTex(text: string, sub: string, w: number, h: number, bg: string, fg: string, seed = 5) {
  const [c, x] = cvs(1024, Math.round((1024 * h) / w)), r = rng(seed), H = c.height; x.fillStyle = bg; x.fillRect(0, 0, 1024, H);
  grime(x, 1024, H, r, 60, "rgba(255,255,255,A)", 20, 120, 0.1);
  x.fillStyle = fg; x.textAlign = "center"; x.textBaseline = "middle"; x.font = `900 ${Math.round(H * 0.42)}px ${F}`; x.fillText(text, 512, H * 0.38, 980);
  x.font = `800 ${Math.round(H * 0.17)}px ${F}`; x.fillText(sub, 512, H * 0.8, 960);
  grime(x, 1024, H, r, 50, "rgba(120,60,20,A)", 4, 26, 0.5); const g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, "rgba(0,0,0,0)"); g.addColorStop(1, "rgba(60,40,20,.35)"); x.fillStyle = g; x.fillRect(0, 0, 1024, H);
  for (let i = 0; i < 40; i++) { const px = r() * 1024; const gg = x.createLinearGradient(0, H * 0.6, 0, H); gg.addColorStop(0, "rgba(110,55,20,0)"); gg.addColorStop(1, "rgba(110,55,20,.4)"); x.fillStyle = gg; x.fillRect(px, H * 0.6, 3 + r() * 6, H * 0.4); }
  x.strokeStyle = "#3a2a20"; x.lineWidth = 10; x.strokeRect(5, 5, 1014, H - 10); x.fillStyle = "#c9cdd3"; for (const [px, py] of [[24, 24], [1000, 24], [24, H - 24], [1000, H - 24]]) { x.beginPath(); x.arc(px, py, 8, 0, 7); x.fill(); }
  return ctex(c);
}
function paperTex(lines: [string, string, number][], w: number, h: number, bg = "#fbf6e6", rot = 0) {
  const [c, x] = cvs(512, Math.round((512 * h) / w)), H = c.height; x.fillStyle = bg; x.fillRect(0, 0, 512, H); x.textAlign = "center"; x.translate(256, 0); x.rotate(rot);
  let y = 0; for (const [t, col, sz] of lines) { y += sz * 1.25; x.fillStyle = col; x.font = `800 ${sz}px ${F}`; x.fillText(t, 0, y, 480); }
  x.setTransform(1, 0, 0, 1, 0, 0); const g = x.createLinearGradient(0, 0, 512, H); g.addColorStop(0, "rgba(120,90,40,.0)"); g.addColorStop(1, "rgba(120,90,40,.25)"); x.fillStyle = g; x.fillRect(0, 0, 512, H); return ctex(c);
}
const plane = (w: number, h: number, map: THREE.Texture, x: number, y: number, z: number, ry = 0) => { const p = mesh(new THREE.PlaneGeometry(w, h), tm("#ffffff", map), x, y, z, false); p.rotation.y = ry; return p; };

// ---------------- tôn sóng (mái hiên, trần) ----------------
function corrugated(w: number, d: number, m: THREE.Material, pitch = 0.11, amp = 0.018) {
  const seg = Math.round(w / (pitch / 6)); const geo = new THREE.PlaneGeometry(w, d, seg, 1); const p = geo.attributes.position;
  for (let i = 0; i < p.count; i++) p.setZ(i, Math.sin((p.getX(i) / pitch) * Math.PI * 2) * amp);
  geo.computeVertexNormals(); const k = new THREE.Mesh(geo, m); k.rotation.x = -Math.PI / 2; k.castShadow = true; k.receiveShadow = true; return k;
}

// ---------------- XE SỐ VIỆT NAM (kiểu Wave / Dream) dựng hình học: đầu xe +z, bánh chạm y = 0 ----------------
export function xeSo(col: string, plate = "29-B1 168.86", dream = false) {
  const g = new THREE.Group(), body = tm(col), dark = tm("#1c1c20"), chrome = tm("#d5d9de"), alu = tm("#9da3aa"), seatM = tm(dream ? "#3a2a24" : "#1e1a1b"), rubber = tm("#16161a");
  const WB = 0.62, R = 0.3;
  for (const z of [-WB, WB]) {
    const tyre = mesh(new THREE.TorusGeometry(R - 0.045, 0.045, 10, 32), rubber, 0, R, z); tyre.rotation.y = Math.PI / 2; g.add(tyre);
    const rim = mesh(new THREE.TorusGeometry(R - 0.09, 0.012, 6, 32), chrome, 0, R, z); rim.rotation.y = Math.PI / 2; g.add(rim);
    const hub = cy(0.07, 0.07, 0.11, alu, 0, R, z, 14); hub.rotation.z = Math.PI / 2; g.add(hub);
    for (let k = 0; k < 18; k++) { const a = (k / 18) * Math.PI * 2, mid = (0.07 + R - 0.09) / 2; const sp = cy(0.003, 0.003, R - 0.16, chrome, (k % 2 ? 1 : -1) * 0.02, R + Math.sin(a) * mid, z + Math.cos(a) * mid, 4); sp.rotation.x = Math.PI / 2 - a; sp.castShadow = false; g.add(sp); }
  }
  // chắn bùn trước (cung) + phuộc đôi
  const ff = mesh(new THREE.TorusGeometry(R + 0.02, 0.05, 6, 20, Math.PI * 0.75), body, 0, R, WB); ff.rotation.y = Math.PI / 2; ff.rotation.z = 0; ff.scale.set(1, 1, 1.6); ff.rotateOnAxis(new THREE.Vector3(0, 0, 1), Math.PI * 0.15); g.add(ff);
  for (const sx of [-0.075, 0.075]) { const fk = cy(0.022, 0.022, 0.62, chrome, sx, R + 0.3, WB - 0.12, 10); fk.rotation.x = -0.42; g.add(fk); }
  // ống cổ + đầu đèn + ghi đông + gương
  const head = mesh(new THREE.SphereGeometry(0.13, 16, 12), body, 0, 0.98, WB - 0.3); head.scale.set(1.05, 0.8, 1.25); g.add(head);
  const lamp = mesh(new THREE.SphereGeometry(0.07, 14, 10), glow(2.4, 2.2, 1.7), 0, 0.97, WB - 0.17, false); lamp.scale.set(1.3, 0.8, 0.6); g.add(lamp);
  const bar = cy(0.014, 0.014, 0.66, chrome, 0, 1.04, WB - 0.36, 8); bar.rotation.z = Math.PI / 2; g.add(bar);
  for (const sx of [-0.31, 0.31]) { g.add(cy(0.02, 0.02, 0.12, rubber, sx, 1.04, WB - 0.36, 8).rotateZ(Math.PI / 2));
    const st = cy(0.006, 0.006, 0.28, chrome, sx * 0.75, 1.17, WB - 0.36, 5); st.rotation.z = -Math.sign(sx) * 0.35; g.add(st);
    const mi = mesh(new THREE.SphereGeometry(0.05, 10, 8), dark, sx * 0.97, 1.3, WB - 0.36); mi.scale.set(1.3, 0.8, 0.3); g.add(mi); }
  const meter = mesh(new THREE.SphereGeometry(0.08, 12, 8, 0, Math.PI * 2, 0, Math.PI / 2), dark, 0, 1.06, WB - 0.42); g.add(meter);
  // yếm (tấm che chân) cong: biên dạng nhìn ngang đùn theo bề ngang
  const prof = (pts: [number, number][]) => { const s = new THREE.Shape(); pts.forEach(([z, y], i) => (i ? s.lineTo(z, y) : s.moveTo(z, y))); s.closePath(); return s; };
  const ext = (s: THREE.Shape, w: number, m: THREE.Material, bev = 0.02) => { const geo = new THREE.ExtrudeGeometry(s, { depth: w, bevelEnabled: true, bevelSize: bev, bevelThickness: bev, bevelSegments: 3, curveSegments: 10 }); geo.translate(0, 0, -w / 2); const k = mesh(geo, m); k.rotation.y = -Math.PI / 2; return k; };
  const legS = new THREE.Shape(); legS.moveTo(0.34, 0.92); legS.quadraticCurveTo(0.5, 0.6, 0.38, 0.36); legS.lineTo(0.3, 0.36); legS.quadraticCurveTo(0.4, 0.62, 0.26, 0.9); legS.closePath();
  g.add(ext(legS, 0.28, body, 0.025));
  // khung xương (underbone) + thân sau ôm yên + ốp sườn
  const frame = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(0, 0.95, WB - 0.3), new THREE.Vector3(0, 0.6, 0.2), new THREE.Vector3(0, 0.45, -0.05), new THREE.Vector3(0, 0.62, -0.3)]), 20, 0.035, 8), dark); frame.castShadow = true; g.add(frame);
  g.add(ext(prof([[0.08, 0.6], [-0.08, 0.74], [-0.62, 0.8], [-0.86, 0.74], [-0.84, 0.62], [-0.55, 0.5], [-0.2, 0.46], [0.04, 0.5]]), 0.26, body, 0.035));
  const cover = ext(prof([[0.0, 0.56], [-0.3, 0.6], [-0.42, 0.5], [-0.15, 0.44]]), 0.3, dream ? tm("#c9b48a") : tm("#2a2a30"), 0.02); g.add(cover);
  // yên
  g.add(ext(prof([[0.05, 0.8], [-0.1, 0.86], [-0.6, 0.88], [-0.82, 0.83], [-0.8, 0.78], [-0.1, 0.78]]), 0.24, seatM, 0.04));
  // động cơ (lốc máy có cánh tản nhiệt) + cần đạp + gác chân + ống xả
  g.add(bx(0.24, 0.22, 0.34, alu, 0, 0.34, 0.02));
  for (let k = 0; k < 5; k++) { const fin = bx(0.2, 0.012, 0.16, alu, 0, 0.42 + k * 0.03, 0.2); fin.rotation.x = -0.9; g.add(fin); }
  const cov = mesh(new THREE.CylinderGeometry(0.11, 0.11, 0.04, 20), tm("#b5bac0"), 0.13, 0.32, -0.02); cov.rotation.z = Math.PI / 2; g.add(cov);
  g.add(bx(0.06, 0.08, 0.5, dark, -0.1, 0.33, -0.34)); // hộp xích
  for (const sx of [-0.2, 0.2]) { const pg = cy(0.015, 0.015, 0.14, rubber, sx, 0.28, 0.05, 6); pg.rotation.z = Math.PI / 2; g.add(pg); }
  const kick = cy(0.012, 0.012, 0.25, chrome, 0.17, 0.33, -0.15, 6); kick.rotation.x = 1.0; g.add(kick);
  const ex1 = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(0.05, 0.34, 0.2), new THREE.Vector3(0.12, 0.22, 0.1), new THREE.Vector3(0.15, 0.24, -0.2)]), 12, 0.022, 8), chrome); g.add(ex1);
  const muf = cy(0.05, 0.042, 0.5, dark, 0.16, 0.3, -0.45, 14); muf.rotation.x = Math.PI / 2 - 0.12; g.add(muf);
  const shield = cy(0.055, 0.055, 0.3, chrome, 0.17, 0.31, -0.38, 14); shield.rotation.x = Math.PI / 2 - 0.12; shield.scale.set(1, 1, 0.6); g.add(shield);
  // giảm xóc sau + tay dắt + chắn bùn sau + đèn hậu + biển số
  for (const sx of [-0.12, 0.12]) { const sk = cy(0.018, 0.018, 0.36, chrome, sx, 0.48, -0.55, 8); sk.rotation.x = 0.3; g.add(sk); const sp = cy(0.03, 0.03, 0.2, tm("#c8202f"), sx, 0.5, -0.56, 10); sp.rotation.x = 0.3; g.add(sp); }
  const grab = new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3([new THREE.Vector3(-0.12, 0.84, -0.5), new THREE.Vector3(-0.13, 0.86, -0.85), new THREE.Vector3(0, 0.86, -0.92), new THREE.Vector3(0.13, 0.86, -0.85), new THREE.Vector3(0.12, 0.84, -0.5)]), 20, 0.013, 6), chrome); g.add(grab);
  const rf = mesh(new THREE.TorusGeometry(R + 0.03, 0.06, 6, 16, Math.PI * 0.45), dark, 0, R, -WB); rf.rotation.y = Math.PI / 2; rf.rotateOnAxis(new THREE.Vector3(0, 0, 1), Math.PI * 0.45); g.add(rf);
  g.add(bx(0.16, 0.06, 0.05, glow(2.3, 0.25, 0.2), 0, 0.73, -0.92, false));
  for (const sx of [-0.13, 0.13]) g.add(bx(0.05, 0.04, 0.05, glow(2.4, 1.2, 0.1), sx, 0.72, -0.9, false));
  const [pc, px] = cvs(256, 192); px.fillStyle = "#f4f4f2"; px.fillRect(0, 0, 256, 192); px.strokeStyle = "#111"; px.lineWidth = 8; px.strokeRect(4, 4, 248, 184); px.fillStyle = "#111"; px.textAlign = "center"; px.font = `900 64px ${F}`; const [l1, l2] = plate.split(" "); px.fillText(l1, 128, 80); px.fillText(l2 ?? "", 128, 160);
  const pl = new THREE.Mesh(new THREE.PlaneGeometry(0.19, 0.14), new THREE.MeshLambertMaterial({ map: ctex(pc) })); pl.position.set(0, 0.58, -0.97); pl.rotation.y = Math.PI; pl.rotation.x = 0.25; g.add(pl);
  // chân chống nghiêng: xe hơi nghiêng trái
  const stand = cy(0.012, 0.012, 0.32, dark, -0.16, 0.14, -0.05, 6); stand.rotation.z = 0.55; g.add(stand);
  return g;
}
function helmet(col: string) { const g = new THREE.Group(); const s = mesh(new THREE.SphereGeometry(0.15, 16, 10, 0, Math.PI * 2, 0, Math.PI * 0.55), tm(col)); g.add(s); const v = mesh(new THREE.SphereGeometry(0.152, 14, 6, -0.9, 1.8, Math.PI * 0.32, Math.PI * 0.22), tm("#1d2430")); g.add(v); const br = mesh(new THREE.TorusGeometry(0.15, 0.008, 4, 24), tm("#222")); br.rotation.x = Math.PI / 2; br.position.y = 0.02; g.add(br); return g; }
function plasticStool(col: string) { const g = new THREE.Group(), m = tm(col); g.add(cy(0.17, 0.17, 0.035, m, 0, 0.43, 0, 18)); const leg = mesh(new THREE.CylinderGeometry(0.15, 0.2, 0.41, 4, 1, true), tm(col, null, { side: THREE.DoubleSide }), 0, 0.205, 0); leg.rotation.y = Math.PI / 4; g.add(leg); return g; }

// ---------------- nạp mô hình Poly Haven → vật liệu toon ----------------
const loader = new GLTFLoader();
const mcache = new Map<string, Promise<THREE.Object3D>>();
function loadM(name: string) {
  if (!mcache.has(name)) mcache.set(name, loader.loadAsync(staticFile(`suaxe2/m/${name}/${name}.gltf`)).then((gl) => {
    const conv = new Map<THREE.Material, THREE.Material>();
    gl.scene.traverse((o) => { const k = o as THREE.Mesh; if (!k.isMesh) return; const old = k.material as THREE.MeshStandardMaterial;
      if (!conv.has(old)) { if (old.map) old.map.colorSpace = THREE.SRGBColorSpace; conv.set(old, tm(old.color ?? "#fff", old.map ?? null, { alphaTest: old.alphaTest || (old.transparent ? 0.5 : 0), side: old.side })); }
      k.material = conv.get(old)!; k.castShadow = true; k.receiveShadow = true; });
    return gl.scene; }));
  return mcache.get(name)!;
}
type PO = { s?: number; h?: number; rx?: number; rz?: number; blob?: number; sy?: number };
/** đặt mô hình: (x, y đáy, z) toạ độ set trước khi xoay; h = chiều cao mong muốn (m) hoặc s = tỉ lệ */
function put(g: THREE.Group, name: string, x: number, y: number, z: number, ry = 0, o: PO = {}) {
  const hd = delayRender("sx2 " + name, { timeoutInMilliseconds: 120000 });
  loadM(name).then((src) => {
    const m = src.clone(true); const w = new THREE.Group(); w.add(m); m.rotation.set(o.rx ?? 0, 0, o.rz ?? 0);
    let bb = new THREE.Box3().setFromObject(m); const sz = bb.getSize(new THREE.Vector3());
    const s = o.h ? o.h / sz.y : o.s ?? 1; m.scale.setScalar(s); if (o.sy) m.scale.y *= o.sy; bb = new THREE.Box3().setFromObject(m); const c = bb.getCenter(new THREE.Vector3());
    m.position.set(-c.x, -bb.min.y, -c.z); w.position.set(x, y, z); w.rotation.y = ry; g.add(w);
    if (o.blob !== 0 && y < 0.05) { const f = bb.getSize(new THREE.Vector3()); const b = blob(f.x * 1.5 + 0.15, f.z * 1.5 + 0.15, o.blob ?? 0.55); b.position.set(x, 0.012, z); b.rotation.z = -ry; g.add(b); }
    continueRender(hd);
  }).catch((e) => { console.error("sx2 load fail", name, e); continueRender(hd); });
}

// ---------------- BỐI CẢNH ----------------
export function buildSuaXe2() {
  const g = new THREE.Group(), r = rng(77);
  const W = 11, D = 8, H = 4.0, Z0 = -3; // tường sau z = -3, cửa z = +5
  // sàn trong tiệm + vỉa hè + lòng đường
  const oil: [number, number, number][] = [[W / 2 + 3.3, 2.4, 1.4], [W / 2 - 3.4, 3.6, 1.0], [W / 2 + 3.0, 0.8, 0.8], [W / 2 - 4.4, 4.9, 0.8], [W / 2 + 0.2, 2.2, 0.7]];
  const fl = mesh(new THREE.PlaneGeometry(W, D), tm("#ffffff", floorTex(W, D, 3, oil)), 0, 0, Z0 + D / 2, false); fl.rotation.x = -Math.PI / 2; g.add(fl);
  const walk = mesh(new THREE.PlaneGeometry(W + 10, 3), tm("#ffffff", floorTex(8, 2, 9, [[1, 1, 0.5]])), 0, -0.02, 6.5, false); walk.rotation.x = -Math.PI / 2; g.add(walk);
  const kerb = bx(W + 10, 0.15, 0.25, tm("#b8b2a6"), 0, -0.07, 8.1, false); g.add(kerb);
  const road = mesh(new THREE.PlaneGeometry(60, 14), tm("#4a4a4f"), 0, -0.14, 15, false); road.rotation.x = -Math.PI / 2; g.add(road);
  // tường: sau + 2 bên (vữa ố, chân gạch men)
  const wb = plane(W, H, wallTex(W, H, 5, "#e9d49a"), 0, H / 2, Z0); g.add(wb);
  for (const s of [-1, 1]) { const ws = plane(D, H, wallTex(D, H, 11 + s, "#e4cf98"), s * W / 2, H / 2, Z0 + D / 2, -s * Math.PI / 2); g.add(ws);
    const back = bx(0.25, H + 0.3, D + 0.3, tm("#cdbb8a"), s * (W / 2 + 0.14), H / 2, Z0 + D / 2, true); back.userData.nc = 1; g.add(back); }
  const backB = bx(W + 0.6, H + 0.3, 0.25, tm("#cdbb8a"), 0, H / 2, Z0 - 0.14); g.add(backB);
  // AO giả: tối dọc chân tường + góc
  for (const [x, z, w, d] of [[0, Z0 + 0.25, W, 0.7], [-W / 2 + 0.25, Z0 + D / 2, 0.7, D], [W / 2 - 0.25, Z0 + D / 2, 0.7, D]] as [number, number, number, number][]) { const b = blob(w * 1.1, d * 1.1, 0.45); b.position.set(x, 0.01, z); g.add(b); }
  { const [c, x] = cvs(8, 256); const gr = x.createLinearGradient(0, 0, 0, 256); gr.addColorStop(0, "rgba(0,0,0,0)"); gr.addColorStop(1, "rgba(0,0,0,1)"); x.fillStyle = gr; x.fillRect(0, 0, 8, 256);
    const aoT = new THREE.CanvasTexture(c); const aoM = new THREE.MeshBasicMaterial({ color: "#1a120c", alphaMap: aoT, transparent: true, opacity: 0.45, depthWrite: false });
    const mk = (w: number, x: number, z: number, ry: number) => { const p = new THREE.Mesh(new THREE.PlaneGeometry(w, 0.8), aoM); p.position.set(x, 0.4, z); p.rotation.y = ry; p.layers.set(NOINK); p.renderOrder = 1; g.add(p); };
    mk(W, 0, Z0 + 0.01, 0); mk(D, -W / 2 + 0.01, Z0 + D / 2, Math.PI / 2); mk(D, W / 2 - 0.01, Z0 + D / 2, -Math.PI / 2);
    for (const s of [-1, 1]) { const cn = new THREE.Mesh(new THREE.PlaneGeometry(0.9, H), new THREE.MeshBasicMaterial({ color: "#1a120c", alphaMap: blobTex!, transparent: true, opacity: 0.35, depthWrite: false })); cn.position.set(s * (W / 2 - 0.02), H / 2, Z0 + 0.3); cn.rotation.y = -s * Math.PI / 2; cn.layers.set(NOINK); g.add(cn); } }
  // trần bê tông trong + dầm thép, phía trước là mái hiên tôn xanh dốc ra phố
  const ceil = mesh(new THREE.PlaneGeometry(W, 5.2), tm("#cfc3a6"), 0, H, Z0 + 2.6, true); ceil.rotation.x = Math.PI / 2; g.add(ceil);
  const fascia = bx(W, 0.45, 0.22, tm("#d9c48a", wallTex(W, 0.45, 41, "#d9c48a", 0)), 0, H - 0.2, Z0 + 5.2); g.add(fascia);
  const roof = corrugated(W + 1.2, 3.4, tm("#4f86a8", metalTex(4, "#5a8fb0", 0.6), { side: THREE.DoubleSide })); roof.position.set(0, H - 0.25, Z0 + 6.8); roof.rotation.x = -Math.PI / 2 + 0.17; g.add(roof);
  for (const x of [-W / 2 + 0.2, W / 2 - 0.2]) { g.add(cy(0.04, 0.04, H - 0.6, tm("#6a6d72", metalTex(6, "#6a6d72", 0.8)), x, (H - 0.6) / 2, Z0 + 8.2, 10)); }
  g.add(bx(W + 1, 0.08, 0.08, tm("#6a6d72"), 0, H - 0.75, Z0 + 8.2));
  for (let k = 0; k < 4; k++) g.add(bx(0.12, 0.2, 5.2, tm("#5a5c60", metalTex(8 + k, "#5a5c60", 0.4)), -4 + k * 2.65, H - 0.1, Z0 + 2.6));
  // biển hiệu chính (tôn sơn) trên tường sau + bảng giá viết tay + lịch + giấy SANG NHƯỢNG
  g.add(plane(5.0, 1.05, signTex("SỬA XE HÙNG XA LỘ", "Sửa chữa · Bảo dưỡng · Thay dầu · Vá lốp · Mua bán xe cũ", 5, 1.05, "#1f5fae", "#ffffff"), 0, 3.25, Z0 + 0.03));
  g.add(plane(1.0, 1.2, paperTex([["BẢNG GIÁ", "#c8202f", 54], ["Thay nhớt ....... 80K", "#222", 34], ["Vá săm ........... 20K", "#222", 34], ["Thay săm ........ 70K", "#222", 34], ["Bơm hơi ............ 5K", "#222", 34], ["Rửa xe ........... 30K", "#222", 34], ["Thay má phanh  60K", "#222", 34]], 1.0, 1.2, "#f2ead2", -0.02), -3.6, 1.95, Z0 + 0.03));
  g.add(plane(0.42, 0.6, paperTex([["THÁNG 11 · 2026", "#ffffff", 34], ["19", "#ffffff", 190], ["Thứ Năm", "#ffffff", 40], ["Âm lịch 30/9", "#ffe36b", 32]], 0.42, 0.6, "#c8202f"), 1.05, 2.15, Z0 + 0.03));
  g.add(plane(0.9, 0.6, paperTex([["SANG NHƯỢNG", "#c8202f", 70], ["Liên hệ chủ tiệm", "#333", 40]], 0.9, 0.6), W / 2 - 0.03, 1.7, Z0 + 5.0, -Math.PI / 2));
  const vx = plane(0.9, 0.6, paperTex([["VÁ XE", "#ffffff", 110], ["BƠM HƠI", "#ffe36b", 70]], 0.9, 0.6, "#c8202f"), -4.4, 0.52, Z0 + 7.0, 0.3); g.add(vx);
  // ---- góc trái sau: chồng lốp + vành gỉ + kệ sắt dầu nhớt ----
  const tyres: [number, number, number][] = [[-4.7, -2.45, 6], [-4.05, -2.5, 5], [-4.8, -1.75, 4], [-3.45, -2.55, 3]];
  for (const [x, z, n] of tyres) for (let k = 0; k < n; k++) put(g, "old_tyre", x + (r() - 0.5) * 0.06, k * 0.16, z + (r() - 0.5) * 0.06, r() * 6, { s: 0.95, rx: Math.PI / 2, blob: k ? 0 : 0.6 });
  put(g, "old_tyre", -3.3, 0, -1.7, 0.5, { h: 0.6, rz: 0.12 });
  put(g, "rusted_wheel_rim_01", -2.85, 0, -2.75, 0.2, { h: 0.45, rx: -1.3 });
  put(g, "steel_frame_shelves_01", -1.65, 0, -2.7, 0, { h: 1.9 });
  const cans = ["small_oil_can_01", "multi_cleaner_5_litre", "plastic_bottle_gallon", "lubricant_spray", "spray_paint_bottles", "cleaner_tin_01", "can_rusted", "multi_cleaner_bottle"];
  for (const [y, n] of [[0.03, 4], [0.47, 5], [0.93, 5], [1.37, 4]] as [number, number][]) for (let k = 0; k < n; k++) put(g, cans[(k * 3 + Math.round(y * 10)) % cans.length], -2.2 + k * (1.1 / (n - 1)), y + 0.02, -2.7 + (r() - 0.5) * 0.12, r() * 2, { h: 0.18 + r() * 0.14, blob: 0 });
  // lốp treo tường + mũ bảo hiểm treo đinh
  for (let k = 0; k < 5; k++) put(g, "old_tyre", -4.9 + k * 0.62, 1.85, Z0 + 0.13, 0, { h: 0.56, blob: 0 });
  for (const [x, c] of [[-0.2, "#c8202f"], [0.22, "#f4f4f2"], [0.62, "#2b6cc4"]] as [number, string][]) { const hm = helmet(c); hm.position.set(x, 1.5, Z0 + 0.16); hm.rotation.x = 0.55; hm.rotation.z = (x - 0.2) * 0.4; g.add(hm); }
  // ---- góc phải sau: bàn thợ gỗ, ê-tô, tủ đồ nghề đỏ, bảng treo dụng cụ, hộp điện, đồng hồ ----
  const wood = tm("#ffffff", woodTex(3, "#6b4a32"));
  g.add(bx(2.4, 0.08, 0.8, wood, 3.0, 0.9, -2.5)); for (const [a, b] of [[-1.1, -0.33], [1.1, -0.33], [-1.1, 0.33], [1.1, 0.33]]) g.add(bx(0.07, 0.9, 0.07, tm("#3e3f44"), 3.0 + a, 0.45, -2.5 + b));
  g.add(bx(2.3, 0.04, 0.7, wood, 3.0, 0.3, -2.5));
  put(g, "bench_vice_01", 3.85, 0.94, -2.35, -0.4, { h: 0.24, blob: 0 }); put(g, "Drill_01", 2.3, 0.94, -2.4, 0.6, { h: 0.22, blob: 0 });
  put(g, "pipe_wrench", 2.9, 0.94, -2.25, 1.3, { h: 0.05, blob: 0 }); put(g, "ratchet_wrench", 3.3, 0.94, -2.3, -0.5, { h: 0.03, blob: 0 }); put(g, "measuring_tape_01", 2.65, 0.94, -2.65, 0.2, { h: 0.07, blob: 0 });
  put(g, "cardboard_box_01", 3.0, 0.34, -2.55, 0.1, { h: 0.3, blob: 0 }); put(g, "can_rusted", 2.2, 0.34, -2.5, 0, { h: 0.18, blob: 0 });
  put(g, "metal_tool_chest", 4.75, 0, -2.45, -0.1, { h: 1.05 });
  const peg = bx(2.4, 1.2, 0.04, tm("#ffffff", metalTex(12, "#4a4f57", 0.3)), 3.0, 2.0, Z0 + 0.04); g.add(peg);
  for (let i = 0; i < 18; i++) { const tl = bx(0.04, 0.22 + r() * 0.25, 0.025, tm(["#c9cdd3", "#d8212f", "#f2c230", "#2b6cc4", "#1b1b1f"][i % 5]), 2.0 + (i % 9) * 0.25, 2.25 - Math.floor(i / 9) * 0.5, Z0 + 0.08); tl.rotation.z = (r() - 0.5) * 0.3; g.add(tl); }
  put(g, "power_box_01", 5.36, 2.3, -1.6, -Math.PI / 2, { h: 0.5, blob: 0 }); put(g, "wall_clock", 4.55, 3.05, Z0 + 0.06, 0, { h: 0.34, blob: 0 });
  put(g, "sledgehammer_01", 1.75, 0, -2.75, 0, { h: 0.8, rz: 0.15, blob: 0 }); put(g, "crowbar_01", 1.6, 0, -2.8, 0.3, { h: 0.7, rz: -0.12, blob: 0 });
  // ---- bục nâng + xe Wave đỏ đang sửa, đèn treo công nghiệp ----
  const liftM = tm("#ffffff", metalTex(21, "#e0b52a", 0.5)); g.add(bx(1.0, 0.28, 2.1, liftM, 3.3, 0.14, -0.6)); g.add(bx(0.2, 0.12, 0.6, tm("#2b2b30"), 3.3, 0.33, -1.35));
  { const b = blob(1.6, 2.6, 0.6); b.position.set(3.3, 0.012, -0.6); g.add(b); }
  const b1 = xeSo("#c8202f", "29-B1 168.86"); b1.position.set(3.3, 0.28, -0.6); g.add(b1);
  put(g, "hanging_industrial_lamp", 3.3, 2.6, -0.6, 0, { h: 0.5, blob: 0 }); g.add(wire([3.3, H, -0.6], [3.3, 3.1, -0.6], 0, tm("#111"), 0.008));
  put(g, "plastic_bottle_gallon", 2.6, 0, 0.35, 0.3, { h: 0.3 });
  // chậu nước thử săm + máy nén khí + cuộn dây hơi
  { const tub = mesh(new THREE.CylinderGeometry(0.34, 0.28, 0.22, 24, 1, true), tm("#3a7bd5", null, { side: THREE.DoubleSide }), 4.5, 0.11, 0.6); g.add(tub); const wat = mesh(new THREE.CircleGeometry(0.31, 24), tm("#6a7f86"), 4.5, 0.18, 0.6, false); wat.rotation.x = -Math.PI / 2; g.add(wat); const bt = blob(0.9, 0.9, 0.5); bt.position.set(4.5, 0.012, 0.6); g.add(bt); }
  { const comp = cy(0.27, 0.27, 0.85, tm("#ffffff", metalTex(31, "#c8202f", 0.4)), 4.8, 0.4, -1.25, 20); comp.rotation.x = Math.PI / 2; g.add(comp); g.add(bx(0.3, 0.25, 0.3, tm("#2b2b30"), 4.8, 0.78, -1.3)); const bc = blob(0.9, 1.3, 0.6); bc.position.set(4.8, 0.012, -1.25); g.add(bc);
    const hose = mesh(new THREE.TorusGeometry(0.2, 0.015, 6, 28), tm("#1d1d22"), 4.4, 0.02, -0.4); hose.rotation.x = Math.PI / 2; g.add(hose); g.add(wire([4.8, 0.7, -1.0], [4.4, 0.05, -0.55], 0.08, tm("#1d1d22"), 0.014)); }
  put(g, "portable_generator", 4.75, 0, 1.6, -Math.PI / 2 + 0.2, { h: 0.55 });
  put(g, "ladder_sectioned_01", 5.3, 0, 2.6, -Math.PI / 2, { h: 2.6, rz: 0.22 });
  put(g, "korean_fire_extinguisher_01", 5.25, 0, 0.0, -Math.PI / 2, { h: 0.5 });
  put(g, "utility_box_01", -5.7, 0, 7.3, 0.2, { h: 1.1 });
  // ---- chỗ uống trà: bàn gỗ thấp + ghế nhựa trắng/đỏ + ấm chén + phích ----
  g.add(bx(0.8, 0.04, 0.55, wood, 1.9, 0.45, 0.4)); for (const [a, b] of [[-0.35, -0.22], [0.35, -0.22], [-0.35, 0.22], [0.35, 0.22]]) g.add(bx(0.04, 0.45, 0.04, tm("#4a3222"), 1.9 + a, 0.22, 0.4 + b));
  { const bt = blob(1.3, 1.0, 0.45); bt.position.set(1.9, 0.012, 0.4); g.add(bt); }
  const pot = mesh(new THREE.SphereGeometry(0.08, 14, 10), tm("#e9e6df"), 1.78, 0.54, 0.38); pot.scale.y = 0.85; g.add(pot); g.add(cy(0.012, 0.02, 0.09, tm("#e9e6df"), 1.7, 0.56, 0.38, 6).rotateZ(1.0));
  for (const [x, z] of [[1.97, 0.5], [2.08, 0.42], [2.0, 0.3]]) g.add(cy(0.03, 0.025, 0.05, tm("#f4f1e6"), x, 0.495, z, 10));
  g.add(cy(0.06, 0.06, 0.34, tm("#d8212f"), 2.2, 0.64, 0.28, 14)); g.add(cy(0.035, 0.05, 0.06, tm("#c9cdd3"), 2.2, 0.84, 0.28, 12)); // phích nước
  put(g, "plastic_monobloc_chair_01", 2.55, 0, 0.75, -2.3, { h: 0.82 });
  { const st = plasticStool("#d8212f"); st.position.set(1.35, 0, 1.1); g.add(st); const b = blob(0.6, 0.6, 0.5); b.position.set(1.35, 0.012, 1.1); g.add(b); }
  for (let k = 0; k < 5; k++) { const st = plasticStool(k % 2 ? "#2b6cc4" : "#d8212f"); st.position.set(-5.0, k * 0.075, 0.6); g.add(st); }
  // ---- bàn thờ Thần Tài – Thổ Địa sát chân tường trái, đèn đỏ ----
  { const ax = -5.1, az = -0.6; g.add(bx(0.55, 0.45, 0.45, tm("#ffffff", woodTex(9, "#7a2e1f")), ax, 0.225, az)); g.add(bx(0.03, 0.5, 0.42, tm("#b8201c"), ax - 0.24, 0.7, az));
    g.add(plane(0.4, 0.46, paperTex([["THẦN TÀI", "#ffe36b", 60], ["THỔ ĐỊA", "#ffe36b", 60], ["Tài lộc", "#ffffff", 46]], 0.4, 0.46, "#b8201c"), ax - 0.22, 0.72, az, Math.PI / 2));
    for (const dz of [-0.1, 0.1]) { const fig = mesh(new THREE.SphereGeometry(0.06, 10, 8), tm(dz < 0 ? "#e8c36a" : "#d9a25a"), ax - 0.08, 0.52, az + dz); fig.scale.y = 1.3; g.add(fig); }
    g.add(cy(0.05, 0.04, 0.07, tm("#c9a24a"), ax + 0.12, 0.485, az, 12)); for (let k = 0; k < 3; k++) g.add(cy(0.003, 0.003, 0.2, tm("#c8202f"), ax + 0.12 + (k - 1) * 0.012, 0.6, az, 4));
    for (const dz of [-0.18, 0.18]) g.add(mesh(new THREE.SphereGeometry(0.03, 8, 6), glow(3.0, 0.3, 0.2), ax + 0.05, 0.9, az + dz, false));
    put(g, "planter_pot_clay", ax + 0.1, 0.45, az + 0.16, 0, { h: 0.08, blob: 0 }); const bt = blob(0.9, 0.9, 0.5); bt.position.set(ax, 0.012, az); g.add(bt); }
  // ---- phía trước / bên trái: phuy dầu, thùng rác, thùng các-tông, xe Dream nâu + Wave xanh, cây cảnh ----
  put(g, "Barrel_01", -4.85, 0, 2.2, 0.3, { h: 0.88 }); put(g, "barrel_03", -4.3, 0, 2.6, 1.0, { h: 0.85 });
  put(g, "metal_trash_can", -2.6, 0, 6.6, 0.1, { h: 0.95 });
  put(g, "cardboard_box_01", -5.0, 0, -1.6, 0.1, { h: 0.4 }); put(g, "cardboard_box_01", -4.95, 0.4, -1.62, 0.5, { h: 0.32, blob: 0 }); put(g, "wooden_crate_01", -4.35, 0, -1.2, 0.3, { h: 0.4 });
  const b2 = xeSo("#7a2e24", "29-H7 052.19", true); b2.position.set(-3.3, 0, 0.7); b2.rotation.y = 0.55; b2.rotation.z = -0.05; g.add(b2); { const b = blob(1.0, 2.0, 0.55); b.position.set(-3.3, 0.012, 0.7); b.rotation.z = -0.55; g.add(b); }
  const b3 = xeSo("#1f3f8a", "30-F1 279.04"); b3.position.set(-3.9, 0, 3.9); b3.rotation.y = -0.4; b3.rotation.z = -0.05; g.add(b3); { const b = blob(1.0, 2.0, 0.5); b.position.set(-3.9, 0.012, 3.9); b.rotation.z = 0.4; g.add(b); }
  put(g, "potted_plant_04", 4.9, 0, 4.4, 0, { h: 0.9 }); put(g, "folding_wooden_stool", -2.4, 0, 2.9, 0.7, { h: 0.45 });
  put(g, "small_lpg_tank", -4.4, 0, -0.1, 0.5, { h: 0.5 });
  put(g, "exterior_aircon_unit", 4.3, 2.75, 4.95, Math.PI, { h: 0.55, blob: 0 });
  // giẻ lau / ốc vít vãi trên sàn
  for (let i = 0; i < 26; i++) { const x0 = 2.4 + r() * 2.2, z0 = -1.8 + r() * 2.4; if (x0 < 2.6 && z0 > -1.6) continue; const nut = cy(0.012, 0.012, 0.01, tm("#9da3aa"), x0, 0.005, z0, 6); nut.castShadow = false; g.add(nut); }
  for (const [x, z, c] of [[2.4, -1.5, "#c9b48a"], [4.1, 0.15, "#5a6a8a"]] as [number, number, string][]) { const rag = mesh(new THREE.CircleGeometry(0.16, 7), tm(c), x, 0.008, z, false); rag.rotation.x = -Math.PI / 2; rag.scale.set(1.2, 0.8, 1); g.add(rag); }
  // ---- dây điện: chạy dọc tường sau, vòng xuống hộp điện, võng qua trần tới đèn tuýp ----
  const wm = tm("#141414");
  g.add(wire([-5.4, 3.75, Z0 + 0.05], [5.4, 3.7, Z0 + 0.05], 0.12, wm)); g.add(wire([-5.4, 3.65, Z0 + 0.06], [2.0, 3.6, Z0 + 0.06], 0.2, wm, 0.007));
  g.add(wire([5.4, 3.7, Z0 + 0.05], [5.38, 2.55, -1.6], 0.15, wm)); g.add(wire([5.38, 2.05, -1.6], [5.38, 0.4, -1.2], 0.05, wm));
  for (const x of [-2.6, 0.2]) g.add(wire([x, H - 0.02, Z0 + 0.1], [x, H - 0.02, 0.8], 0.25, wm, 0.007));
  g.add(wire([-5.4, 3.7, Z0 + 4.5], [5.4, 3.6, Z0 + 4.8], 0.35, wm)); // dây ngang cửa
  // bóng đèn treo dây ở cửa + đèn tuýp trần
  g.add(wire([-1.2, H, 1.6], [-1.2, 3.0, 1.6], 0, wm, 0.006)); g.add(mesh(new THREE.SphereGeometry(0.06, 12, 10), glow(3.2, 2.6, 1.6), -1.2, 2.94, 1.6, false));
  put(g, "mounted_fluorescent_lights", -2.6, H - 0.12, 0.6, Math.PI / 2, { s: 1, blob: 0 }); put(g, "mounted_fluorescent_lights", 0.2, H - 0.12, 0.2, Math.PI / 2, { s: 1, blob: 0 });
  // ---- ngoài phố: cột điện bê tông + búi dây, nhà đối diện (tranh vẽ), ô che ----
  { const pole = cy(0.12, 0.17, 8, tm("#9a968c", metalTex(51, "#9a968c", 0.15)), -6.2, 4, 7.9, 10); g.add(pole);
    for (let k = 0; k < 9; k++) g.add(wire([-6.2, 6.2 + (k % 3) * 0.15, 7.9], [6 + k * 0.4, 5.8 + (k % 4) * 0.2, 7.6 + (k % 2) * 0.3], 0.5 + r() * 0.4, wm, 0.012));
    for (let k = 0; k < 4; k++) g.add(wire([-6.2, 6.0 + k * 0.1, 7.9], [-5.2, 3.7, 5.0], 0.3 + k * 0.1, wm, 0.01));
    const coil = mesh(new THREE.TorusGeometry(0.22, 0.05, 6, 16), wm, -6.05, 5.5, 7.9); coil.rotation.y = Math.PI / 2; g.add(coil); }
  { const [c, x] = cvs(2048, 640), rr = rng(91); x.fillStyle = "#c9d8e6"; x.fillRect(0, 0, 2048, 640); let px = 0; const SG = ["TẠP HOÁ", "CƠM BÌNH DÂN", "PHỞ BÒ", "ĐIỆN THOẠI", "CẮT TÓC", "BÁNH MÌ", "THUỐC TÂY"];
    for (let i = 0; px < 2048; i++) { const w = 150 + rr() * 130, h = 380 + rr() * 240; x.fillStyle = ["#e8c07a", "#d9d2c0", "#f0e0b0", "#b8cfc0", "#e6b8a0", "#d0c8e0"][i % 6]; x.fillRect(px, 640 - h, w, h);
      for (let yy = 640 - h + 30; yy < 470; yy += 90) { x.fillStyle = "#4a5a6a"; x.fillRect(px + 22, yy, w - 44, 50); x.fillStyle = "#6a5a4a"; x.fillRect(px + 15, yy + 52, w - 30, 6); }
      x.fillStyle = ["#c8202f", "#1f5fae", "#1d8a4a", "#f2c230"][i % 4]; x.fillRect(px + 6, 480, w - 12, 46); x.fillStyle = "#fff"; x.font = `900 26px ${F}`; x.textAlign = "center"; x.fillText(SG[i % SG.length], px + w / 2, 512, w - 20);
      x.fillStyle = "#3a3d44"; x.fillRect(px + 10, 530, w - 20, 110); px += w; }
    const fac = new THREE.Mesh(new THREE.PlaneGeometry(36, 11.25), new THREE.MeshBasicMaterial({ map: ctex(c) })); fac.position.set(0, 5.4, 22); fac.rotation.y = Math.PI; fac.layers.set(NOINK); g.add(fac); }
  { const um = new THREE.Group(); const can = mesh(new THREE.ConeGeometry(1.4, 0.45, 8, 1, true), tm("#2f6fb0", null, { side: THREE.DoubleSide }), 0, 2.3, 0); um.add(can); um.add(cy(0.025, 0.025, 2.3, tm("#ddd"), 0, 1.15, 0, 6)); um.position.set(-4.6, 0, 6.6); g.add(um); }
  // ---- nắng chiều rọi xiên vào tiệm (vệt sáng) + bụi bay ----
  { const [c, x] = cvs(64, 256); const gr = x.createLinearGradient(0, 0, 0, 256); gr.addColorStop(0, "rgba(255,255,255,0)"); gr.addColorStop(0.3, "rgba(255,255,255,1)"); gr.addColorStop(1, "rgba(255,255,255,0)"); x.fillStyle = gr; x.fillRect(0, 0, 64, 256);
    const gx = x.createLinearGradient(0, 0, 64, 0); gx.addColorStop(0, "rgba(0,0,0,1)"); gx.addColorStop(0.5, "rgba(0,0,0,0)"); gx.addColorStop(1, "rgba(0,0,0,1)"); x.globalCompositeOperation = "destination-out"; x.fillStyle = gx; x.fillRect(0, 0, 64, 256);
    const sm = new THREE.MeshBasicMaterial({ color: new THREE.Color(1.0, 0.72, 0.4), alphaMap: new THREE.CanvasTexture(c), transparent: true, opacity: 0.075, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide });
    // hướng nắng "golden" của xưởng (sau khi xoay 180°): từ cửa vào trong, lệch sang +x của set
    for (let k = 0; k < 5; k++) { const p = new THREE.Mesh(new THREE.PlaneGeometry(0.5 + r() * 0.6, 7), sm); p.position.set(-1.5 + k * 1.3, 2.0, 2.6); p.rotation.set(-0.95, -0.65, 0.35); p.layers.set(NOINK); p.renderOrder = 5; g.add(p); } }
  { const N = 420, pos = new Float32Array(N * 3), base = new Float32Array(N * 3); for (let i = 0; i < N; i++) { base[i * 3] = -5 + r() * 10; base[i * 3 + 1] = 0.3 + r() * 3.4; base[i * 3 + 2] = -2.5 + r() * 7; }
    pos.set(base); const geo = new THREE.BufferGeometry(); geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const [c, x] = cvs(32, 32); const gr = x.createRadialGradient(16, 16, 0, 16, 16, 16); gr.addColorStop(0, "rgba(255,255,255,1)"); gr.addColorStop(1, "rgba(255,255,255,0)"); x.fillStyle = gr; x.fillRect(0, 0, 32, 32);
    const pts = new THREE.Points(geo, new THREE.PointsMaterial({ color: new THREE.Color(1.6, 1.25, 0.8), size: 0.022, map: new THREE.CanvasTexture(c), transparent: true, opacity: 0.7, depthWrite: false, blending: THREE.AdditiveBlending, sizeAttenuation: true }));
    pts.layers.set(NOINK); g.add(pts);
    pts.userData.tick = (t: number) => { for (let i = 0; i < N; i++) { pos[i * 3] = base[i * 3] + Math.sin(t * 0.3 + i) * 0.15; pos[i * 3 + 1] = base[i * 3 + 1] + Math.sin(t * 0.21 + i * 1.7) * 0.12; pos[i * 3 + 2] = base[i * 3 + 2] + Math.cos(t * 0.25 + i * 0.7) * 0.15; } geo.attributes.position.needsUpdate = true; }; }
  // ---- đèn ấm (chiếu theo vật liệu toon của set): toạ độ thế giới = (-x, y, -z) vì set xoay 180° ----
  const lamps: [V3, V3, number][] = [[[3.3, 2.5, -0.6], [1.3, 0.95, 0.6], 4.2], [[-2.6, 3.8, 0.6], [0.55, 0.6, 0.55], 6.5], [[0.2, 3.8, 0.2], [0.55, 0.6, 0.55], 6.5], [[-1.2, 2.94, 1.6], [0.9, 0.62, 0.3], 3.2], [[-5.0, 0.9, -0.6], [0.9, 0.08, 0.05], 1.3]];
  lamps.forEach(([p, c, rr], i) => { U.uLampP.value[i].set(-p[0], p[1], -p[2]); U.uLampC.value[i].set(...c); U.uLampR.value[i] = rr; });
  g.traverse((o) => { const k = o as THREE.Mesh; if (k.isMesh && k.userData.nc) k.castShadow = false; });
  g.rotation.y = Math.PI; return { g };
}
