// CAST2X – chuẩn chi tiết 19/11/2026 (anh Huy duyệt): GIỮ NGUYÊN nhân vật thẻ 2D của cast2 (dáng que, đầu tròn, mặt, tỉ lệ như DN1),
// chỉ vẽ THÊM trang phục + chi tiết nhỏ lên thẻ sau khi cast2 vẽ xong. KHÔNG sửa cast2 → phim cũ không phải dựng lại.
// Cách làm: cast2 vẽ thẻ như cũ → loang màu từ giữa thân lấy MẢNG ÁO (chấp nhận đậm nhạt, dừng ở nét mực) → vẽ chi tiết cắt theo mảng:
//  - áo: cổ áo, nẹp cúc hoặc khoá kéo + áo phông trong, túi có nắp, đường may chấm, nếp gấp nhẹ, bo gấu; bóng 2 tông (lưng tối ấm, mép trước sáng)
//  - Hùng (áo xanh): bảng tên, bút cắm túi, vết dầu, giẻ lau giắt túi sau; Chiến (áo cam): quần jeans xanh
//  - quần: lòng nét chân que tô màu quần (giữ viền mực) + nếp gối; giày: đế sẫm + vạch
// Dùng: stage_ct.tsx (cờ chiTiet) tạo ActorX thay Actor cho mọi nhân vật; trang phục chọn theo khoá cast (FIT) hoặc mặc định theo outfit.
import * as THREE from "three";
import { Actor, Outfit, Pose } from "../vang/cast2";
import { INK } from "../pho/toon";

export type Fit = "mech" | "jacket" | "blouse" | "plain";
export type FitX = { fit: Fit; tag?: string; stains?: boolean; rag?: boolean; pants?: string };
/** trang phục theo khoá cast; khoá khác: nữ tóc dài → blouse, còn lại → plain (cổ áo + nếp + đường may + bóng 2 tông) */
export const FIT: Record<string, FitX> = { hung: { fit: "mech", tag: "HÙNG", stains: true, rag: true }, chien: { fit: "jacket", pants: "#3f64a8" } };

const hex = (c: string) => { const n = parseInt(c.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; };
const dark = (c: string, k: number) => { const [r, g, b] = hex(c); return `rgb(${Math.round(r * k)},${Math.round(g * k)},${Math.round(b * k)})`; };
const FONT = "'Be Vietnam Pro', 'DejaVu Sans', Arial";
/** mặt nạ cho các điểm ảnh CÙNG SẮC với màu c (chấp nhận đậm/nhạt do thẻ cũ tô chuyển sắc); có seed → chỉ lấy mảng liền chứa điểm mồi */
function mask(src: ImageData, c: string, tol = 26, kLo = 0.35, kHi = 1.25, y0lim = 0, y1lim = 1e9, seed?: [number, number]) {
  const W = src.width, H = src.height, d = src.data, col = hex(c), cc = col[0] * col[0] + col[1] * col[1] + col[2] * col[2] || 1; const m = document.createElement("canvas"); m.width = W; m.height = H; const mg = m.getContext("2d")!; const md = mg.createImageData(W, H);
  const ok = (x: number, y: number) => { if (y < y0lim || y >= y1lim) return false; const i = (y * W + x) * 4; if (d[i + 3] < 200) return false; const k = (d[i] * col[0] + d[i + 1] * col[1] + d[i + 2] * col[2]) / cc; if (k < kLo || k > kHi) return false;
    return Math.abs(d[i] - k * col[0]) + Math.abs(d[i + 1] - k * col[1]) + Math.abs(d[i + 2] - k * col[2]) <= tol * 3; };
  let x0 = W, x1 = -1, y0 = H, y1 = -1; const rowL = new Int32Array(H).fill(-1), rowR = new Int32Array(H).fill(-1); let n = 0;
  const mark = (x: number, y: number) => { md.data[(y * W + x) * 4 + 3] = 255; n++; if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; if (rowL[y] < 0 || x < rowL[y]) rowL[y] = x; if (x > rowR[y]) rowR[y] = x; };
  if (seed) { // lấy MẢNG LIỀN LỚN NHẤT cùng sắc (thân áo); tóc/da cùng sắc nằm sau nét mực, tay áo là nét mảnh → đều nhỏ hơn thân
    const lab = new Int32Array(W * H), st: number[] = []; let best = -1, bestN = 0, id = 0;
    for (let y0s = 200; y0s < 950; y0s += 5) for (let x0s = 60; x0s < W - 60; x0s += 5) { const p0 = x0s + y0s * W; if (lab[p0] || !ok(x0s, y0s)) continue; id++; let cnt = 0; st.push(p0); lab[p0] = id;
      while (st.length) { const q = st.pop()!, x = q % W, y = (q - x) / W; cnt++; for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const nx = x + dx, ny = y + dy; if (nx < 0 || ny < 0 || nx >= W || ny >= H) continue; const p = nx + ny * W; if (lab[p] || !ok(nx, ny)) continue; lab[p] = id; st.push(p); } }
      if (cnt > bestN) { bestN = cnt; best = id; } }
    if (best > 0) for (let p = 0; p < W * H; p++) if (lab[p] === best) mark(p % W, (p - (p % W)) / W);
  } else for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) if (ok(x, y)) mark(x, y);
  mg.putImageData(md, 0, 0); return { m, x0, x1, y0, y1, rowL, rowR, n };
}
type MK = ReturnType<typeof mask>;
/** lòng nét chân que (nét mực dày dưới thân áo), chừa viền mực 3 px */
function legMask(src: ImageData, yA: number, yB: number) {
  const W = src.width, d = src.data, ink = hex(INK); const m = document.createElement("canvas"); m.width = W; m.height = src.height; const mg = m.getContext("2d")!; const md = mg.createImageData(W, src.height);
  const isInk = (x: number, y: number) => { const i = (y * W + x) * 4; return d[i + 3] > 200 && Math.abs(d[i] - ink[0]) + Math.abs(d[i + 1] - ink[1]) + Math.abs(d[i + 2] - ink[2]) < 60; };
  let n = 0, x0 = W, x1 = -1; for (let y = Math.max(0, yA); y < Math.min(src.height, yB); y++) for (let x = 3; x < W - 3; x++) if (isInk(x, y) && isInk(x - 3, y) && isInk(x + 3, y)) { md.data[(y * W + x) * 4 + 3] = 255; n++; if (x < x0) x0 = x; if (x > x1) x1 = x; }
  mg.putImageData(md, 0, 0); return { m, n, x0, x1, y0: yA, y1: yB };
}
type LM = ReturnType<typeof legMask>;
/** vẽ fn lên lớp riêng rồi chỉ giữ phần nằm trong mặt nạ */
function clipTo(g: CanvasRenderingContext2D, mk: HTMLCanvasElement, fn: (x: CanvasRenderingContext2D) => void) {
  const l = document.createElement("canvas"); l.width = mk.width; l.height = mk.height; const x = l.getContext("2d")!; fn(x); x.globalCompositeOperation = "destination-in"; x.drawImage(mk, 0, 0); g.drawImage(l, 0, 0);
}
const stain = (x: CanvasRenderingContext2D, sx: number, sy: number, q: number, a: number) => { const gg = x.createRadialGradient(sx, sy, 0, sx, sy, q); gg.addColorStop(0, "rgba(22,18,16,.7)"); gg.addColorStop(1, "rgba(22,18,16,0)"); x.fillStyle = gg; x.beginPath(); x.ellipse(sx, sy, q, q * 0.7, a, 0, 7); x.fill(); };
function pocket(x: CanvasRenderingContext2D, px: number, py: number, pw: number, ph: number, col: string) {
  x.fillStyle = col; x.fillRect(px, py, pw, ph); x.strokeStyle = "rgba(36,23,38,.75)"; x.lineWidth = 3; x.strokeRect(px, py, pw, ph); x.fillRect(px - 2, py - 6, pw + 4, ph * 0.38); x.strokeRect(px - 2, py - 6, pw + 4, ph * 0.38);
  x.setLineDash([3, 4]); x.strokeStyle = "rgba(255,255,255,.32)"; x.lineWidth = 1.5; x.strokeRect(px + 4, py + ph * 0.4, pw - 8, ph * 0.5); x.setLineDash([]);
}
function nameTag(x: CanvasRenderingContext2D, tx: number, ty: number, tw: number, text: string) { x.fillStyle = "#f4f1e6"; x.fillRect(tx, ty, tw, 21); x.strokeStyle = INK; x.lineWidth = 2; x.strokeRect(tx, ty, tw, 21); x.fillStyle = "#1f3d8a"; x.font = `900 16px ${FONT}`; x.textAlign = "center"; x.fillText(text, tx + tw / 2, ty + 16, tw - 4); }
function pen(g: CanvasRenderingContext2D, px: number, py: number) { g.fillStyle = "#f4f4f2"; g.fillRect(px - 3, py - 22, 6, 24); g.strokeRect(px - 3, py - 22, 6, 24); g.fillStyle = "#c8202f"; g.fillRect(px - 3, py - 26, 6, 6); g.strokeRect(px - 3, py - 26, 6, 6); }

export class ActorX extends Actor {
  private xk = ""; private F: FitX;
  constructor(o: Outfit, h: number, private seedX: number, key: string) { super(o, h, seedX); this.F = FIT[key] ?? { fit: o.long ? "blouse" : "plain" }; }
  pose(p: Pose, cam: THREE.Camera, tint: THREE.Color) {
    super.pose(p, cam, tint);
    const self = this as unknown as { key: string; g: CanvasRenderingContext2D; t: THREE.CanvasTexture };
    if (self.key === this.xk || this.o.anime) return; this.xk = self.key; this.dress(self.g, p.side ?? 0, p.mode === "sit"); self.t.needsUpdate = true;
  }
  private dress(g: CanvasRenderingContext2D, side: number, sit: boolean) {
    const o = this.o; let s = this.seedX * 7 + 3; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
    g.setTransform(1, 0, 0, 1, 0, 0); const img = g.getImageData(0, 0, 600, 1000);
    const J = mask(img, o.jacket, 26, 0.35, 1.25, 0, 1e9, [300, sit ? 640 : 600]); if (J.n < 200) return;
    const S = mask(img, o.boots ?? "#e9e6df", 14, 0.7, 1.2, J.y1 + 10, 1000), P = legMask(img, J.y1 + 4, S.n > 30 ? S.y0 - 2 : 990);
    if (side) this.side(g, J, side > 0 ? 1 : -1, r); else this.front(g, J, r);
    this.legsShoes(g, S, P, r);
  }
  /** nhìn nghiêng: fr = +1 mặt quay phải canvas */
  private side(g: CanvasRenderingContext2D, J: MK, fr: number, r: () => number) {
    const o = this.o, F = this.F, W = J.x1 - J.x0, H = J.y1 - J.y0, cx = (J.x0 + J.x1) / 2;
    const row = (a: Int32Array, y: number) => { for (let d = 0; d < 30; d++) { const v = a[Math.round(y) + d]; if (v >= 0) return v; } return -1; };
    const front = (y: number) => row(fr > 0 ? J.rowR : J.rowL, y), back = (y: number) => row(fr > 0 ? J.rowL : J.rowR, y);
    const fy = (k: number) => J.y0 + H * k, top2 = dark(o.jacket, 0.78), seam = "rgba(255,255,255,.32)", hem = F.fit === "jacket" ? 0.86 : 0.93;
    clipTo(g, J.m, (x) => {
      const gb = x.createLinearGradient(fr > 0 ? J.x0 : J.x1, 0, fr > 0 ? J.x1 : J.x0, 0); gb.addColorStop(0, "rgba(70,25,45,.34)"); gb.addColorStop(0.42, "rgba(70,25,45,.12)"); gb.addColorStop(0.62, "rgba(70,25,45,0)"); gb.addColorStop(0.88, "rgba(255,214,150,0)"); gb.addColorStop(1, "rgba(255,214,150,.28)");
      x.fillStyle = gb; x.fillRect(0, 0, 600, 1000);
      const gv = x.createLinearGradient(0, J.y0, 0, J.y1); gv.addColorStop(0, "rgba(255,230,190,.12)"); gv.addColorStop(0.7, "rgba(0,0,0,0)"); gv.addColorStop(1, "rgba(60,20,30,.25)"); x.fillStyle = gv; x.fillRect(0, 0, 600, 1000);
      x.lineCap = "round"; x.strokeStyle = "rgba(36,23,38,.35)"; x.lineWidth = 3.5;
      for (let k = 0; k < 4; k++) { const y = fy(0.55 + k * 0.1), xb = back(y); if (xb < 0) continue; x.beginPath(); x.moveTo(xb + fr * W * (0.12 + r() * 0.1), y); x.quadraticCurveTo(xb + fr * W * 0.35, y - H * 0.04, xb + fr * W * (0.5 + r() * 0.15), y - H * (0.06 + r() * 0.04)); x.stroke(); }
      for (let k = 0; k < 3; k++) { const y = fy(0.25 + k * 0.08), xf = front(y); if (xf < 0) continue; x.beginPath(); x.moveTo(xf - fr * 4, y); x.quadraticCurveTo(xf - fr * W * 0.15, y + H * 0.02, xf - fr * W * 0.25, y + H * 0.05); x.stroke(); }
      x.setLineDash([5, 6]); x.strokeStyle = seam; x.lineWidth = 2;
      x.beginPath(); for (let y = fy(0.3); y < fy(0.95); y += 4) { const xb = back(y); if (xb >= 0) x.lineTo(xb + fr * 10, y); } x.stroke();
      x.beginPath(); x.moveTo(J.x0, fy(hem)); x.lineTo(J.x1, fy(hem)); x.stroke(); x.setLineDash([]);
      const along = (k: number, off: number) => { x.beginPath(); for (let y = J.y0; y <= fy(k); y += 3) { const xf = front(y); if (xf >= 0) x.lineTo(xf - fr * off, y); } };
      if (F.fit === "jacket") { // bo gấu + áo phông trắng + khoá kéo + túi chéo
        x.fillStyle = top2; x.fillRect(0, fy(0.88), 600, H); x.strokeStyle = "rgba(0,0,0,.25)"; x.lineWidth = 2; for (let xx = J.x0; xx < J.x1; xx += 7) { x.beginPath(); x.moveTo(xx, fy(0.885)); x.lineTo(xx, J.y1); x.stroke(); }
        along(0.88, W * 0.2); for (let y = fy(0.88); y >= J.y0; y -= 3) { const xf = front(y); if (xf >= 0) x.lineTo(xf + fr * 20, y); } x.closePath(); x.fillStyle = "#f2efe6"; x.fill();
        x.strokeStyle = "#3a3a40"; x.lineWidth = 5; along(0.88, W * 0.2); x.stroke(); x.strokeStyle = "#c9cdd3"; x.lineWidth = 2; x.setLineDash([3, 3]); along(0.88, W * 0.2); x.stroke(); x.setLineDash([]);
        const zy = fy(0.3), zx = front(zy) - fr * W * 0.2; x.fillStyle = "#c9cdd3"; x.fillRect(zx - 4, zy, 8, 16); x.strokeStyle = INK; x.lineWidth = 2; x.strokeRect(zx - 4, zy, 8, 16);
        x.strokeStyle = "rgba(36,23,38,.55)"; x.lineWidth = 3.5; const py = fy(0.6), pxs = back(py) + fr * W * 0.45; x.beginPath(); x.moveTo(pxs, py); x.lineTo(pxs + fr * W * 0.12, py + H * 0.16); x.stroke();
      } else if (F.fit === "mech") { // áo thợ: nẹp cúc, túi nắp, bảng tên, vết dầu
        x.strokeStyle = "rgba(36,23,38,.5)"; x.lineWidth = 3; x.beginPath(); for (let y = fy(0.12); y < J.y1; y += 4) { const xf = front(y); if (xf >= 0) x.lineTo(xf - fr * W * 0.2, y); } x.stroke();
        const py = fy(0.3), pw = W * 0.26, ph = H * 0.14, pxs = front(py) - fr * W * 0.3 - (fr > 0 ? pw : 0); pocket(x, pxs, py, pw, ph, top2);
        if (F.tag) nameTag(x, pxs, py + ph + 10, pw * 1.15, F.tag);
        if (F.stains) for (let k = 0; k < 9; k++) stain(x, J.x0 + r() * W, fy(0.35 + r() * 0.6), 5 + r() * 13, r() * 3);
      } else if (F.fit === "blouse") { // áo nữ: chiết eo + dây buộc + chấm hoa nhỏ
        for (let k = 0; k < 26; k++) { x.fillStyle = ["rgba(255,255,255,.55)", "rgba(255,240,160,.5)"][k % 2]; x.beginPath(); x.arc(J.x0 + r() * W, fy(0.12 + r() * 0.8), 3 + r() * 3, 0, 7); x.fill(); }
        x.strokeStyle = "rgba(36,23,38,.45)"; x.lineWidth = 3; x.beginPath(); x.moveTo(J.x0, fy(0.62)); x.quadraticCurveTo(cx, fy(0.66), J.x1, fy(0.62)); x.stroke();
      }
    });
    g.lineJoin = "round"; g.strokeStyle = INK; g.lineWidth = 4;
    const cy0 = J.y0 + 4, cf = front(cy0 + 6), cb = back(cy0 + 6);
    if (cf >= 0 && cb >= 0) {
      if (F.fit === "mech" || F.fit === "plain") { const d = F.fit === "mech" ? 1 : 0.8; g.fillStyle = top2; g.beginPath(); g.moveTo(cb + fr * 6, cy0 + 2); g.quadraticCurveTo(cx, cy0 - 8, cf - fr * 10, cy0 + 2); g.lineTo(cf - fr * W * 0.18 * d, cy0 + H * 0.12 * d); g.lineTo(cf - fr * W * 0.3 * d, cy0 + 6); g.closePath(); g.fill(); g.stroke(); }
      else if (F.fit === "jacket") { g.fillStyle = top2; g.beginPath(); g.moveTo(cb + fr * 4, cy0 + 8); g.lineTo(cb + fr * 4, cy0 - 10); g.quadraticCurveTo(cx, cy0 - 18, cf - fr * 4, cy0 - 10); g.lineTo(cf - fr * 4, cy0 + 8); g.quadraticCurveTo(cx, cy0, cb + fr * 4, cy0 + 8); g.fill(); g.stroke(); }
      else { g.strokeStyle = "#f4f1e6"; g.lineWidth = 5; g.beginPath(); g.moveTo(cb + fr * 10, cy0 + 2); g.quadraticCurveTo(cx, cy0 + 10, cf - fr * W * 0.12, cy0 + H * 0.14); g.stroke(); g.strokeStyle = INK; g.lineWidth = 4; }
    }
    if (F.fit === "mech") { pen(g, front(fy(0.3)) - fr * W * 0.4, fy(0.3));
      if (F.rag) { const ry = J.y1 - 10, rx = back(ry - 6) + fr * 10; g.fillStyle = "#c8202f"; g.beginPath(); g.moveTo(rx, ry - 6); g.quadraticCurveTo(rx - fr * 24, ry + 30, rx - fr * 14, ry + 74); g.lineTo(rx + fr * 8, ry + 70); g.quadraticCurveTo(rx + fr * 2, ry + 30, rx + fr * 20, ry - 4); g.closePath(); g.fill(); g.stroke();
        g.strokeStyle = "rgba(255,255,255,.7)"; g.lineWidth = 2.5; for (const k of [0.3, 0.55, 0.8]) { g.beginPath(); g.moveTo(rx - fr * 16 * k, ry + 70 * k); g.lineTo(rx + fr * 10, ry + 70 * k - 4); g.stroke(); } g.strokeStyle = INK; g.lineWidth = 4; } }
  }
  /** chính diện: nẹp/khoá giữa ngực, cổ đối xứng, túi 2 bên, bóng trái sáng – phải tối */
  private front(g: CanvasRenderingContext2D, J: MK, r: () => number) {
    const o = this.o, F = this.F, W = J.x1 - J.x0, H = J.y1 - J.y0, cx = (J.x0 + J.x1) / 2, fy = (k: number) => J.y0 + H * k, top2 = dark(o.jacket, 0.78), hem = F.fit === "jacket" ? 0.86 : 0.93;
    clipTo(g, J.m, (x) => {
      const gb = x.createLinearGradient(J.x0, 0, J.x1, 0); gb.addColorStop(0, "rgba(255,214,150,.22)"); gb.addColorStop(0.35, "rgba(255,214,150,0)"); gb.addColorStop(0.7, "rgba(70,25,45,.08)"); gb.addColorStop(1, "rgba(70,25,45,.32)"); x.fillStyle = gb; x.fillRect(0, 0, 600, 1000);
      const gv = x.createLinearGradient(0, J.y0, 0, J.y1); gv.addColorStop(0, "rgba(255,230,190,.1)"); gv.addColorStop(0.75, "rgba(0,0,0,0)"); gv.addColorStop(1, "rgba(60,20,30,.25)"); x.fillStyle = gv; x.fillRect(0, 0, 600, 1000);
      x.lineCap = "round"; x.strokeStyle = "rgba(36,23,38,.32)"; x.lineWidth = 3.5;
      for (const sg of [-1, 1]) for (let k = 0; k < 2; k++) { const y = fy(0.6 + k * 0.13); x.beginPath(); x.moveTo(cx + sg * W * 0.42, y); x.quadraticCurveTo(cx + sg * W * 0.3, y - H * 0.03, cx + sg * W * (0.15 + r() * 0.08), y - H * 0.05); x.stroke(); }
      x.setLineDash([5, 6]); x.strokeStyle = "rgba(255,255,255,.32)"; x.lineWidth = 2; x.beginPath(); x.moveTo(J.x0, fy(hem)); x.lineTo(J.x1, fy(hem)); x.stroke(); x.setLineDash([]);
      if (F.fit === "jacket") { x.fillStyle = top2; x.fillRect(0, fy(0.88), 600, H); x.fillStyle = "#f2efe6"; x.fillRect(cx - W * 0.14, J.y0, W * 0.28, fy(0.88) - J.y0); x.fillStyle = "#3a3a40"; x.fillRect(cx - W * 0.14 - 3, J.y0, 6, fy(0.88) - J.y0); x.fillRect(cx + W * 0.14 - 3, J.y0, 6, fy(0.88) - J.y0); x.fillStyle = "#c9cdd3"; x.fillRect(cx + W * 0.14 - 4, fy(0.32), 8, 16); }
      else if (F.fit === "mech") { x.strokeStyle = "rgba(36,23,38,.5)"; x.lineWidth = 3; x.beginPath(); x.moveTo(cx + 8, fy(0.1)); x.lineTo(cx + 8, J.y1); x.stroke();
        for (const sg of [-1, 1]) pocket(x, cx + sg * W * 0.2 - W * 0.12, fy(0.27), W * 0.24, H * 0.13, top2);
        if (F.tag) nameTag(x, cx - W * 0.34, fy(0.27) + H * 0.13 + 8, W * 0.28, F.tag);
        if (F.stains) for (let k = 0; k < 9; k++) stain(x, J.x0 + r() * W, fy(0.35 + r() * 0.6), 5 + r() * 13, r() * 3); }
      else if (F.fit === "blouse") { for (let k = 0; k < 26; k++) { x.fillStyle = ["rgba(255,255,255,.55)", "rgba(255,240,160,.5)"][k % 2]; x.beginPath(); x.arc(J.x0 + r() * W, fy(0.12 + r() * 0.8), 3 + r() * 3, 0, 7); x.fill(); } }
    });
    g.lineJoin = "round"; g.strokeStyle = INK; g.lineWidth = 4; const cy0 = J.y0 + 4;
    if (F.fit === "mech" || F.fit === "plain") { g.fillStyle = top2; for (const sg of [-1, 1]) { g.beginPath(); g.moveTo(cx, cy0 + H * 0.1); g.lineTo(cx + sg * W * 0.3, cy0); g.lineTo(cx + sg * W * 0.1, cy0 - 4); g.closePath(); g.fill(); g.stroke(); } }
    else if (F.fit === "jacket") { g.fillStyle = top2; g.beginPath(); g.moveTo(cx - W * 0.3, cy0 + 6); g.quadraticCurveTo(cx, cy0 - 14, cx + W * 0.3, cy0 + 6); g.quadraticCurveTo(cx, cy0 - 2, cx - W * 0.3, cy0 + 6); g.closePath(); g.fill(); g.stroke(); }
    else { g.strokeStyle = "#f4f1e6"; g.lineWidth = 5; g.beginPath(); g.moveTo(cx - W * 0.25, cy0); g.lineTo(cx, cy0 + H * 0.16); g.lineTo(cx + W * 0.25, cy0); g.stroke(); g.strokeStyle = INK; g.lineWidth = 4; }
    if (F.fit === "mech") pen(g, cx + W * 0.2, fy(0.27));
  }
  private legsShoes(g: CanvasRenderingContext2D, S: MK, P: LM, r: () => number) {
    const o = this.o, F = this.F;
    if (P.n > 60) clipTo(g, P.m, (x) => { x.fillStyle = F.pants ?? o.pants; x.fillRect(0, P.y0, 600, P.y1 - P.y0); const gp = x.createLinearGradient(0, P.y0, 0, P.y1); gp.addColorStop(0, "rgba(0,0,0,.25)"); gp.addColorStop(0.3, "rgba(0,0,0,0)"); gp.addColorStop(1, "rgba(0,0,0,.15)"); x.fillStyle = gp; x.fillRect(0, P.y0, 600, P.y1 - P.y0);
      x.strokeStyle = "rgba(20,10,20,.5)"; x.lineWidth = 3; const ky = P.y0 + (P.y1 - P.y0) * 0.45; for (const d of [-6, 6]) { x.beginPath(); x.moveTo(P.x0, ky + d); x.lineTo(P.x1, ky + d + 5); x.stroke(); }
      if (F.stains) { x.fillStyle = "rgba(20,16,14,.6)"; for (let k = 0; k < 4; k++) { x.beginPath(); x.ellipse(P.x0 + r() * (P.x1 - P.x0), P.y0 + r() * (P.y1 - P.y0), 4, 6, 0, 0, 7); x.fill(); } } });
    if (S.n > 30) clipTo(g, S.m, (x) => { const h = S.y1 - S.y0; x.fillStyle = "#4a4048"; x.fillRect(0, S.y1 - h * 0.28, 600, h); x.fillStyle = "#c8202f"; x.fillRect(0, S.y0 + h * 0.45, 600, 3); x.fillStyle = "rgba(255,255,255,.35)"; x.fillRect(0, S.y0 + 2, 600, 3); });
  }
}
