// CAST2X (thử nghiệm 19/11/2026, anh Huy chốt): GIỮ NGUYÊN nhân vật thẻ 2D của cast2 (dáng que, đầu tròn, mặt, tỉ lệ như DN1),
// chỉ vẽ THÊM trang phục + chi tiết nhỏ lên thẻ sau khi cast2 vẽ xong. KHÔNG sửa cast2 → phim cũ không phải dựng lại.
// Cách làm: cast2 vẽ thẻ như cũ → dò điểm ảnh theo màu áo / quần / giày → vẽ chi tiết cắt theo đúng mảng màu đó:
//  - áo: cổ áo, nẹp cúc hoặc khoá kéo + áo phông trong, túi có nắp, đường may chấm, nếp gấp nhẹ, bo gấu; tô bóng 2 tông (lưng tối ấm, mép trước sáng)
//  - Hùng (áo xanh): bảng tên, bút cắm túi, vết dầu, giẻ lau giắt túi sau
//  - quần: mảng sáng dọc + nếp gối; giày: đế sẫm + vạch
// Dùng: Demo ghi CAST2X.shots[i] (mỗi cảnh 30 khung, kèm vị trí máy để thẻ quay về máy); set suaxe2 gọi tick(t).
import * as THREE from "three";
import { Actor, OUT, Pose } from "../vang/cast2";
import { L as LIGHT } from "../vang/look";
import { INK } from "../pho/toon";

type V3 = [number, number, number];
export type Fit = "mech" | "jacket";
export type X2 = { who: string; p: V3; pose: Pose };
export type Shot2X = { cam: V3; chars: X2[] };
export const CAST2X: { shots: Shot2X[]; light: keyof typeof LIGHT } = { shots: [], light: "golden" };
export const FIT: Record<string, { fit: Fit; tag?: string; stains?: boolean; rag?: boolean }> = { hung: { fit: "mech", tag: "HÙNG", stains: true, rag: true }, chien: { fit: "jacket" } };

const hex = (c: string) => { const n = parseInt(c.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; };
const near = (d: Uint8ClampedArray, i: number, c: number[], tol: number) => d[i + 3] > 200 && Math.abs(d[i] - c[0]) <= tol && Math.abs(d[i + 1] - c[1]) <= tol && Math.abs(d[i + 2] - c[2]) <= tol;
const dark = (c: string, k: number) => { const [r, g, b] = hex(c); return `rgb(${Math.round(r * k)},${Math.round(g * k)},${Math.round(b * k)})`; };
/** mặt nạ (canvas) + khung bao + biên trái/phải từng hàng cho các điểm ảnh CÙNG SẮC với màu c (chấp nhận đậm/nhạt do thẻ cũ tô chuyển sắc) */
function mask(src: ImageData, c: string, tol = 26, kLo = 0.35, kHi = 1.25, y0lim = 0, y1lim = 1e9, seed?: [number, number]) {
  const W = src.width, H = src.height, d = src.data, col = hex(c), cc = col[0] * col[0] + col[1] * col[1] + col[2] * col[2] || 1; const m = document.createElement("canvas"); m.width = W; m.height = H; const mg = m.getContext("2d")!; const md = mg.createImageData(W, H);
  const ok = (x: number, y: number) => { if (y < y0lim || y >= y1lim) return false; const i = (y * W + x) * 4; if (d[i + 3] < 200) return false; const k = (d[i] * col[0] + d[i + 1] * col[1] + d[i + 2] * col[2]) / cc; if (k < kLo || k > kHi) return false;
    return Math.abs(d[i] - k * col[0]) + Math.abs(d[i + 1] - k * col[1]) + Math.abs(d[i + 2] - k * col[2]) <= tol * 3; };
  let x0 = W, x1 = -1, y0 = H, y1 = -1; const rowL = new Int32Array(H).fill(-1), rowR = new Int32Array(H).fill(-1); let n = 0;
  const mark = (x: number, y: number) => { md.data[(y * W + x) * 4 + 3] = 255; n++; if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; if (rowL[y] < 0 || x < rowL[y]) rowL[y] = x; if (x > rowR[y]) rowR[y] = x; };
  if (seed) { // chỉ lấy MẢNG LIỀN chứa điểm mồi (thân áo) – tóc/da cùng sắc nằm sau nét mực nên không bị lấy
    let sx = -1, sy = -1; for (let rr = 0; rr < 200 && sx < 0; rr += 2) for (let a = 0; a < 16 && sx < 0; a++) { const x = Math.round(seed[0] + Math.cos(a / 8 * Math.PI) * rr), y = Math.round(seed[1] + Math.sin(a / 8 * Math.PI) * rr); if (x >= 0 && x < W && y >= 0 && y < H && ok(x, y)) { sx = x; sy = y; } }
    if (sx >= 0) { const seen = new Uint8Array(W * H), st = [sx + sy * W]; seen[st[0]] = 1; while (st.length) { const q = st.pop()!, x = q % W, y = (q - x) / W; mark(x, y);
      for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const nx = x + dx, ny = y + dy; if (nx < 0 || ny < 0 || nx >= W || ny >= H) continue; const p = nx + ny * W; if (seen[p]) continue; seen[p] = 1; if (ok(nx, ny)) st.push(p); } } }
  } else for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) if (ok(x, y)) mark(x, y);
  mg.putImageData(md, 0, 0); return { m, x0, x1, y0, y1, rowL, rowR, n };
}
/** chân que (nét mực dưới thân áo): giữ viền mực 3 px, lòng nét tô màu quần → quần có màu mà không đổi dáng */
function legMask(src: ImageData, yA: number, yB: number) {
  const W = src.width, d = src.data, ink = hex(INK); const m = document.createElement("canvas"); m.width = W; m.height = src.height; const mg = m.getContext("2d")!; const md = mg.createImageData(W, src.height);
  const isInk = (x: number, y: number) => { const i = (y * W + x) * 4; return d[i + 3] > 200 && Math.abs(d[i] - ink[0]) + Math.abs(d[i + 1] - ink[1]) + Math.abs(d[i + 2] - ink[2]) < 60; };
  let n = 0, x0 = W, x1 = -1; for (let y = yA; y < yB; y++) for (let x = 3; x < W - 3; x++) if (isInk(x, y) && isInk(x - 3, y) && isInk(x + 3, y)) { md.data[(y * W + x) * 4 + 3] = 255; n++; if (x < x0) x0 = x; if (x > x1) x1 = x; }
  mg.putImageData(md, 0, 0); return { m, n, x0, x1, y0: yA, y1: yB };
}
/** vẽ fn lên lớp riêng rồi chỉ giữ phần nằm trong mặt nạ */
function clipTo(g: CanvasRenderingContext2D, mk: HTMLCanvasElement, fn: (x: CanvasRenderingContext2D) => void) {
  const l = document.createElement("canvas"); l.width = mk.width; l.height = mk.height; const x = l.getContext("2d")!; fn(x); x.globalCompositeOperation = "destination-in"; x.drawImage(mk, 0, 0); g.drawImage(l, 0, 0);
}

export class ActorX extends Actor {
  private xk = ""; private seedX: number;
  constructor(public who: string) { super(OUT[who].o, OUT[who].h, OUT[who].seed); this.seedX = OUT[who].seed; }
  pose(p: Pose, cam: THREE.Camera, tint: THREE.Color) {
    super.pose(p, cam, tint);
    const self = this as unknown as { key: string; g: CanvasRenderingContext2D; t: THREE.CanvasTexture };
    if (self.key === this.xk) return; this.xk = self.key; this.dress(self.g, p.side ?? 1); self.t.needsUpdate = true;
  }
  private dress(g: CanvasRenderingContext2D, side: number) {
    const o = this.o, F = FIT[this.who]; if (!F) return; let s = this.seedX * 7 + 3; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
    g.setTransform(1, 0, 0, 1, 0, 0); const img = g.getImageData(0, 0, 600, 1000);
    const J = mask(img, o.jacket, 26, 0.35, 1.25, 0, 1e9, [300, 600]); const S = mask(img, o.boots ?? "#e9e6df", 14, 0.7, 1.2, J.y1 + 20, 1000);
    if (J.n < 200) return; const P = legMask(img, J.y1 + 4, S.n > 30 ? S.y0 - 2 : 990); 
    const fr = side >= 0 ? 1 : -1, W = J.x1 - J.x0, H = J.y1 - J.y0, cx = (J.x0 + J.x1) / 2;
    const front = (y: number) => (fr > 0 ? J.rowR[Math.round(y)] : J.rowL[Math.round(y)]), back = (y: number) => (fr > 0 ? J.rowL[Math.round(y)] : J.rowR[Math.round(y)]);
    const fy = (k: number) => J.y0 + H * k, top2 = dark(o.jacket, 0.78), seam = "rgba(255,255,255,.32)";
    // ---- ÁO: bóng 2 tông + nếp + đường may (cắt theo mảng áo) ----
    clipTo(g, J.m, (x) => {
      const gb = x.createLinearGradient(fr > 0 ? J.x0 : J.x1, 0, fr > 0 ? J.x1 : J.x0, 0); gb.addColorStop(0, "rgba(70,25,45,.34)"); gb.addColorStop(0.42, "rgba(70,25,45,.12)"); gb.addColorStop(0.62, "rgba(70,25,45,0)"); gb.addColorStop(0.88, "rgba(255,214,150,0)"); gb.addColorStop(1, "rgba(255,214,150,.28)");
      x.fillStyle = gb; x.fillRect(0, 0, 600, 1000);
      const gv = x.createLinearGradient(0, J.y0, 0, J.y1); gv.addColorStop(0, "rgba(255,230,190,.12)"); gv.addColorStop(0.7, "rgba(0,0,0,0)"); gv.addColorStop(1, "rgba(60,20,30,.25)"); x.fillStyle = gv; x.fillRect(0, 0, 600, 1000);
      x.lineCap = "round"; x.strokeStyle = "rgba(36,23,38,.35)"; x.lineWidth = 3.5;
      for (let k = 0; k < 4; k++) { const y = fy(0.55 + k * 0.1), xb = back(y), xf = front(y); if (xb < 0 || xf < 0) continue; x.beginPath(); x.moveTo(xb + fr * W * (0.12 + r() * 0.1), y); x.quadraticCurveTo(xb + fr * W * 0.35, y - H * 0.04, xb + fr * W * (0.5 + r() * 0.15), y - H * (0.06 + r() * 0.04)); x.stroke(); }
      for (let k = 0; k < 3; k++) { const y = fy(0.25 + k * 0.08), xf = front(y); if (xf < 0) continue; x.beginPath(); x.moveTo(xf - fr * 4, y); x.quadraticCurveTo(xf - fr * W * 0.15, y + H * 0.02, xf - fr * W * 0.25, y + H * 0.05); x.stroke(); }
      x.setLineDash([5, 6]); x.strokeStyle = seam; x.lineWidth = 2;
      x.beginPath(); for (let y = fy(0.1); y < fy(0.95); y += 4) { const xb = back(y); if (xb >= 0) x.lineTo(xb + fr * 10, y); } x.stroke();
      x.beginPath(); for (let xx = J.x0; xx < J.x1; xx += 4) x.lineTo(xx, fy(F.fit === "jacket" ? 0.86 : 0.93)); x.stroke(); x.setLineDash([]);
      if (F.fit === "jacket") { // bo gấu + áo phông trắng + khoá kéo
        x.fillStyle = top2; x.fillRect(0, fy(0.88), 600, H); x.strokeStyle = "rgba(0,0,0,.25)"; x.lineWidth = 2; for (let xx = J.x0; xx < J.x1; xx += 7) { x.beginPath(); x.moveTo(xx, fy(0.885)); x.lineTo(xx, J.y1); x.stroke(); }
        x.beginPath(); for (let y = J.y0; y <= fy(0.88); y += 3) { const xf = front(y); if (xf >= 0) x.lineTo(xf - fr * W * 0.2, y); } for (let y = fy(0.88); y >= J.y0; y -= 3) { const xf = front(y); if (xf >= 0) x.lineTo(xf + fr * 20, y); } x.closePath(); x.fillStyle = "#f2efe6"; x.fill();
        x.strokeStyle = "#3a3a40"; x.lineWidth = 5; x.beginPath(); for (let y = J.y0; y <= fy(0.88); y += 3) { const xf = front(y); if (xf >= 0) x.lineTo(xf - fr * W * 0.2, y); } x.stroke();
        x.strokeStyle = "#c9cdd3"; x.lineWidth = 2; x.setLineDash([3, 3]); x.beginPath(); for (let y = J.y0; y <= fy(0.88); y += 3) { const xf = front(y); if (xf >= 0) x.lineTo(xf - fr * W * 0.2, y); } x.stroke(); x.setLineDash([]);
        const zy = fy(0.3), zx = front(zy) - fr * W * 0.2; x.fillStyle = "#c9cdd3"; x.fillRect(zx - 4, zy, 8, 16); x.strokeStyle = INK; x.lineWidth = 2; x.strokeRect(zx - 4, zy, 8, 16);
        x.strokeStyle = "rgba(36,23,38,.55)"; x.lineWidth = 3.5; const py = fy(0.6), pxs = back(py) + fr * W * 0.45; x.beginPath(); x.moveTo(pxs, py); x.lineTo(pxs + fr * W * 0.12, py + H * 0.16); x.stroke(); // túi chéo
      } else { // áo thợ: nẹp cúc, túi nắp, bảng tên, vết dầu
        x.strokeStyle = "rgba(36,23,38,.5)"; x.lineWidth = 3; x.beginPath(); for (let y = fy(0.12); y < J.y1; y += 4) { const xf = front(y); if (xf >= 0) x.lineTo(xf - fr * W * 0.2, y); } x.stroke();
        const py = fy(0.3), pw = W * 0.26, ph = H * 0.14, pxs = front(py) - fr * W * 0.3 - (fr > 0 ? pw : 0);
        x.fillStyle = top2; x.fillRect(pxs, py, pw, ph); x.strokeStyle = "rgba(36,23,38,.75)"; x.lineWidth = 3; x.strokeRect(pxs, py, pw, ph); x.fillRect(pxs - 2, py - 6, pw + 4, ph * 0.38); x.strokeRect(pxs - 2, py - 6, pw + 4, ph * 0.38);
        x.setLineDash([3, 4]); x.strokeStyle = seam; x.lineWidth = 1.5; x.strokeRect(pxs + 4, py + ph * 0.4, pw - 8, ph * 0.5); x.setLineDash([]);
        if (F.tag) { const ty = py + ph + 10, tw = pw * 1.15; x.fillStyle = "#f4f1e6"; x.fillRect(pxs, ty, tw, 22); x.strokeStyle = INK; x.lineWidth = 2; x.strokeRect(pxs, ty, tw, 22); x.fillStyle = "#1f3d8a"; x.font = `900 17px 'Be Vietnam Pro', 'DejaVu Sans', Arial`; x.textAlign = "center"; x.fillText(F.tag, pxs + tw / 2, ty + 17, tw - 4); }
        if (F.stains) for (let k = 0; k < 9; k++) { const sx = J.x0 + r() * W, sy = fy(0.35 + r() * 0.6), q = 5 + r() * 13; const gg = x.createRadialGradient(sx, sy, 0, sx, sy, q); gg.addColorStop(0, "rgba(22,18,16,.7)"); gg.addColorStop(1, "rgba(22,18,16,0)"); x.fillStyle = gg; x.beginPath(); x.ellipse(sx, sy, q, q * 0.7, r() * 3, 0, 7); x.fill(); }
      }
    });
    // ---- CỔ ÁO (vẽ đè, có viền mực, nằm trên mép trên thân) ----
    g.lineJoin = "round"; g.strokeStyle = INK; g.lineWidth = 4;
    const cy0 = J.y0 + 4, cf = front(cy0 + 6), cb = back(cy0 + 6);
    if (cf >= 0 && cb >= 0) {
      if (F.fit === "mech") { g.fillStyle = top2; g.beginPath(); g.moveTo(cb + fr * 6, cy0 + 2); g.quadraticCurveTo(cx, cy0 - 8, cf - fr * 10, cy0 + 2); g.lineTo(cf - fr * W * 0.18, cy0 + H * 0.12); g.lineTo(cf - fr * W * 0.3, cy0 + 6); g.closePath(); g.fill(); g.stroke(); }
      else { g.fillStyle = top2; g.beginPath(); g.moveTo(cb + fr * 4, cy0 + 8); g.lineTo(cb + fr * 4, cy0 - 10); g.quadraticCurveTo(cx, cy0 - 18, cf - fr * 4, cy0 - 10); g.lineTo(cf - fr * 4, cy0 + 8); g.quadraticCurveTo(cx, cy0, cb + fr * 4, cy0 + 8); g.fill(); g.stroke(); }
    }
    if (F.fit === "mech") { // bút cắm túi + giẻ lau giắt túi sau
      const py = fy(0.3), px0 = front(py) - fr * W * 0.4; g.fillStyle = "#f4f4f2"; g.fillRect(px0 - 3, py - 22, 6, 24); g.strokeRect(px0 - 3, py - 22, 6, 24); g.fillStyle = "#c8202f"; g.fillRect(px0 - 3, py - 26, 6, 6); g.strokeRect(px0 - 3, py - 26, 6, 6);
      if (FIT[this.who].rag) { const ry = J.y1 - 10, rx = back(ry - 6) + fr * 10; g.fillStyle = "#c8202f"; g.beginPath(); g.moveTo(rx, ry - 6); g.quadraticCurveTo(rx - fr * 24, ry + 30, rx - fr * 14, ry + 74); g.lineTo(rx + fr * 8, ry + 70); g.quadraticCurveTo(rx + fr * 2, ry + 30, rx + fr * 20, ry - 4); g.closePath(); g.fill(); g.stroke();
        g.strokeStyle = "rgba(255,255,255,.7)"; g.lineWidth = 2.5; for (const k of [0.3, 0.55, 0.8]) { g.beginPath(); g.moveTo(rx - fr * 16 * k, ry + 70 * k); g.lineTo(rx + fr * 10, ry + 70 * k - 4); g.stroke(); } g.strokeStyle = INK; g.lineWidth = 4; }
    }
    // ---- QUẦN: mảng sáng dọc + nếp gối; GIÀY: đế sẫm ----
    if (P.n > 60) clipTo(g, P.m, (x) => { x.fillStyle = o.pants; x.fillRect(0, P.y0, 600, P.y1 - P.y0); const gp = x.createLinearGradient(0, P.y0, 0, P.y1); gp.addColorStop(0, "rgba(0,0,0,.25)"); gp.addColorStop(0.3, "rgba(0,0,0,0)"); gp.addColorStop(1, "rgba(0,0,0,.15)"); x.fillStyle = gp; x.fillRect(0, P.y0, 600, P.y1 - P.y0);
      x.strokeStyle = "rgba(20,10,20,.5)"; x.lineWidth = 3; const ky = P.y0 + (P.y1 - P.y0) * 0.45; for (const d of [-6, 6]) { x.beginPath(); x.moveTo(P.x0, ky + d); x.lineTo(P.x1, ky + d + 5); x.stroke(); }
      if (FIT[this.who].stains) { x.fillStyle = "rgba(20,16,14,.6)"; for (let k = 0; k < 4; k++) { x.beginPath(); x.ellipse(P.x0 + r() * (P.x1 - P.x0), P.y0 + r() * (P.y1 - P.y0), 4, 6, 0, 0, 7); x.fill(); } } });
    if (S.n > 30) clipTo(g, S.m, (x) => { const h = S.y1 - S.y0; x.fillStyle = "#4a4048"; x.fillRect(0, S.y1 - h * 0.28, 600, h); x.fillStyle = "#c8202f"; x.fillRect(0, S.y0 + h * 0.45, 600, 3); x.fillStyle = "rgba(255,255,255,.35)"; x.fillRect(0, S.y0 + 2, 600, 3); });
  }
}

/** dựng nhân vật cast2 bản nâng trang phục cho các cảnh trong CAST2X.shots (nhóm con huỷ phép xoay 180° của set) */
export function buildCast2X(set: THREE.Group) {
  if (!CAST2X.shots.length) return;
  const g = new THREE.Group(); g.rotation.y = Math.PI; set.add(g);
  const who = new Set<string>(); CAST2X.shots.forEach((s) => s.chars.forEach((c) => who.add(c.who)));
  const actors: Record<string, ActorX> = {}; for (const w of who) if (OUT[w]) { actors[w] = new ActorX(w); g.add(actors[w].root); actors[w].root.visible = false; }
  const cam = new THREE.PerspectiveCamera(), tint = new THREE.Color(LIGHT[CAST2X.light].tint);
  g.userData.tick = (t: number) => { const sh = CAST2X.shots[Math.min(CAST2X.shots.length - 1, Math.max(0, Math.floor(t + 1e-4)))]; for (const a of Object.values(actors)) a.root.visible = false; if (!sh) return;
    cam.position.set(...sh.cam); for (const c of sh.chars) { const a = actors[c.who]; if (!a) continue; a.root.visible = true; a.root.position.set(...c.p); a.pose(c.pose, cam, tint); } };
}
