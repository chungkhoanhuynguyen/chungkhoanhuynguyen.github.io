// CAST2X – chuẩn chi tiết 19/11/2026 (anh Huy duyệt): GIỮ NGUYÊN nhân vật thẻ 2D của cast2 (dáng que, đầu tròn, mặt, tỉ lệ như DN1),
// chỉ vẽ THÊM trang phục + chi tiết nhỏ lên thẻ sau khi cast2 vẽ xong. KHÔNG sửa cast2 → phim cũ không phải dựng lại.
// Cách làm: cast2 vẽ thẻ như cũ → lấy MẢNG ÁO (mảng liền lớn nhất cùng sắc màu áo, chấp nhận đậm nhạt, dừng ở nét mực) →
// vẽ các "món" trang phục theo toạ độ tương đối (u: -1 lưng/trái → +1 ngực/phải, v: 0 cổ → 1 gấu) cắt đúng theo mảng áo.
// Món: cổ (sơ mi, polo, cổ tròn, cổ đứng, mũ trùm, chữ V, bà ba), nẹp cúc / khoá kéo + áo phông trong / vest, túi (ngực, 2 túi dưới, kangaroo, túi chéo),
// bảng tên, bút, logo/chữ in, quân hàm + phù hiệu, tạp dề, len gân, áo ba lỗ (hở vai), dây chuyền, khăn quàng, bo gấu, vết dầu, giẻ lau;
// quần: lòng nét chân que tô màu quần (giữ viền mực) + nếp gối; giày: đế sẫm + vạch; mũ lưỡi trai: phù hiệu.
// Bóng 2 tông (lưng tối ấm, mép trước sáng vàng) khớp đèn ấm của set chi tiết.
// Dùng: stage_ct.tsx (cờ chiTiet) tạo ActorX thay Actor cho mọi nhân vật; trang phục chọn theo khoá cast (FIT) hoặc mặc định theo outfit.
import * as THREE from "three";
import { Actor, Outfit, Pose } from "../vang/cast2";
import { INK } from "../pho/toon";

type Collar = "shirt" | "polo" | "round" | "stand" | "hood" | "v" | "baba" | "none";
export type FitX = {
  vai?: string;
  collar?: Collar; placket?: "buttons" | "zip" | "suit" | "cardigan" | "none";
  pockets?: ("chest" | "chest2" | "lower2" | "kangaroo" | "slant")[];
  tag?: string; pen?: boolean; print?: string; logo?: string; stains?: boolean; rag?: boolean; hem?: boolean;
  epaulette?: boolean; badge?: boolean; capBadge?: string; apron?: string; knit?: boolean; tank?: boolean; chain?: boolean; scarf?: string; dots?: boolean; waist?: boolean; stripe?: string;
  pants?: string; o?: Partial<Outfit>;
};
const SHIRT: FitX = { collar: "shirt", placket: "buttons", pockets: ["chest"] };
const BLOUSE: FitX = { collar: "v", dots: true, waist: true };
const TEE: FitX = { collar: "round" };
/** trang phục theo khoá cast (vai suy từ tên + phim đã dùng) */
export const FIT: Record<string, FitX> = {
  hung: { vai: "Hùng Xa Lộ – thợ sửa xe (DN1)", ...SHIRT, tag: "HÙNG", pen: true, stains: true, rag: true },
  hung5: { vai: "Hùng – học viên lớp LTTC", ...SHIRT, pen: true },
  chien: { vai: "Chiến – bạn Hùng, áo khoác cam (DN1)", collar: "stand", placket: "zip", pockets: ["slant"], hem: true, pants: "#3f64a8" },
  huy: { vai: "Huy – người dẫn chuyện / chuyên gia", ...SHIRT, pen: true, o: { tie: "#1f3d8a" } },
  tan: { vai: "Tân Mông To – streamer (Vàng đỉnh)", collar: "hood", pockets: ["kangaroo"], hem: true, print: "LIVE" },
  ngan: { vai: "Ngân – người yêu Tân (Vàng)", ...BLOUSE },
  vest: { vai: "doanh nhân áo vest", placket: "suit", pockets: ["chest"], o: { collar: "#f6f4ee", tie: "#7a1424" } },
  clerk: { vai: "nhân viên tiệm vàng", ...SHIRT, tag: "NHÂN VIÊN", logo: "VÀNG", scarf: "#f2d36b" },
  me: { vai: "mẹ (Vàng) – trung niên", collar: "v", placket: "cardigan", knit: true, pockets: ["lower2"] },
  gym: { vai: "dân gym", tank: true, print: "GYM" },
  gym2: { vai: "dân gym (áo trắng)", tank: true, print: "FIT" },
  boxer: { vai: "võ sĩ boxing", tank: true, print: "BOXING", capBadge: "#f2d36b" },
  xoi: { vai: "chị bán xôi", ...BLOUSE, apron: "#f4f1e6" },
  kieu: { vai: "Kiều – nữ trẻ", ...BLOUSE },
  thuong: { vai: "Thương – nữ văn phòng", collar: "shirt", placket: "buttons", waist: true },
  thuyto: { vai: "Thuý Tô – nữ trung niên", ...BLOUSE },
  lannhi: { vai: "Lan Nhi – bé gái", collar: "round", print: "★" },
  hanhdo: { vai: "Hạnh Đỏ – nữ cá tính, áo da", collar: "stand", placket: "zip", hem: true },
  oanh: { vai: "Oanh – nữ cao", ...BLOUSE },
  thay5: { vai: "thầy giáo (lớp LTTC)", ...SHIRT, pen: true, o: { tie: "#7a1424" } },
  phu5: { vai: "Phú – đại gia (LTTC)", collar: "polo", chain: true },
  phu: { vai: "Phú Dê Già – đại gia", collar: "polo", chain: true },
  qha5: { vai: "Quang Hà – học viên, mũ đỏ", collar: "polo", capBadge: "#ffffff" },
  quang: { vai: "Quang Hà", ...SHIRT },
  vy5: { vai: "Vy – học viên nữ", ...BLOUSE }, vy: { vai: "Vy Kim Khâu", ...BLOUSE },
  trang5: { vai: "Trang – nữ nhỏ (LTTC)", collar: "round", print: "♥" }, trang: { vai: "Trang Trâu – nữ trẻ", collar: "round", print: "♥" },
  linh5: { vai: "Linh – học viên nữ", ...BLOUSE }, linh: { vai: "Linh – nữ trẻ", ...BLOUSE },
  dung: { vai: "Dũng Gymmer", tank: true, print: "GYM" },
  thang: { vai: "Thắng – shipper, mũ đen", collar: "stand", placket: "zip", stripe: "#f4f1e6", logo: "SHIP", hem: true },
  bohung: { vai: "bố Hùng – ông cụ", collar: "v", placket: "cardigan", knit: true, pockets: ["lower2"] },
  mehung: { vai: "mẹ Hùng – bà cụ, áo bà ba", collar: "baba", pockets: ["lower2"] },
  lam: { vai: "Lâm – thanh niên", ...TEE, print: "HN" },
  tu: { vai: "ông Tư – cụ ông", collar: "v", placket: "cardigan", knit: true, pockets: ["lower2"] },
  ba: { vai: "bà – cụ bà, áo bà ba", collar: "baba", pockets: ["lower2"] },
  khach: { vai: "khách", ...SHIRT },
  nv: { vai: "nhân viên ngân hàng (nữ)", collar: "shirt", placket: "buttons", tag: "NGÂN HÀNG", scarf: "#c8202f", logo: "BANK" },
  cuong: { vai: "Cường Sociu", ...TEE, print: "SOCIU", chain: true },
  tai: { vai: "Ân Hữu Tài – shipper/xe ôm, mũ đỏ", collar: "stand", placket: "zip", stripe: "#f2d36b", capBadge: "#ffffff", hem: true },
  longbh: { vai: "Long – tư vấn bảo hiểm", ...SHIRT, tag: "BẢO HIỂM", o: { tie: "#7a1424" } },
  ngans: { vai: "Ngân – nhân viên bán hàng", ...BLOUSE, tag: "TƯ VẤN" },
  hoast: { vai: "Hoa – nhân viên bán hàng", collar: "shirt", placket: "buttons", tag: "SALE", waist: true },
  baove: { vai: "bảo vệ", ...SHIRT, pockets: ["chest2"], epaulette: true, badge: true, capBadge: "#f2d36b" },
  tronghau: { vai: "Trọng Hậu – áo đấu bóng đá, mũ xanh", collar: "round", print: "4", stripe: "#ffffff", capBadge: "#ffffff" },
  toanbop: { vai: "Toàn Bốp – trung niên chắc người", collar: "polo", pockets: ["chest"] },
  ninhkoi: { vai: "Ninh Koi – thanh niên cao", collar: "stand", placket: "zip", hem: true },
};

const hex = (c: string) => { const n = parseInt(c.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; };
const dark = (c: string, k: number) => { const [r, g, b] = hex(c); return `rgb(${Math.round(r * k)},${Math.round(g * k)},${Math.round(b * k)})`; };
const lum = (c: string) => { const [r, g, b] = hex(c); return 0.299 * r + 0.587 * g + 0.114 * b; };
const IK = hex(INK);
const FONT = "'Be Vietnam Pro', 'DejaVu Sans', Arial";
/** mặt nạ các điểm ảnh CÙNG SẮC với màu c; big → chỉ giữ mảng liền lớn nhất (thân áo; tóc/da cùng sắc nằm sau nét mực, tay áo là nét mảnh) */
function mask(src: ImageData, c: string, tol = 26, kLo = 0.35, kHi = 1.25, y0lim = 0, y1lim = 1e9, big = false) {
  const W = src.width, H = src.height, d = src.data, col = hex(c), cc = col[0] * col[0] + col[1] * col[1] + col[2] * col[2] || 1; const m = document.createElement("canvas"); m.width = W; m.height = H; const mg = m.getContext("2d")!; const md = mg.createImageData(W, H);
  const dk = lum(c) < 60;
  const ok = (x: number, y: number) => { if (y < y0lim || y >= y1lim) return false; const i = (y * W + x) * 4; if (d[i + 3] < 200) return false;
    if (Math.abs(d[i] - IK[0]) + Math.abs(d[i + 1] - IK[1]) + Math.abs(d[i + 2] - IK[2]) < 34) return false; // không bao giờ lấy nét mực
    if (dk) return Math.abs(d[i] - col[0]) + Math.abs(d[i + 1] - col[1]) + Math.abs(d[i + 2] - col[2]) <= 18;
    if (d[i] + d[i + 1] + d[i + 2] < 120) return false;
    const k = (d[i] * col[0] + d[i + 1] * col[1] + d[i + 2] * col[2]) / cc; if (k < kLo || k > kHi) return false;
    return Math.abs(d[i] - k * col[0]) + Math.abs(d[i + 1] - k * col[1]) + Math.abs(d[i + 2] - k * col[2]) <= tol * 3; };
  let x0 = W, x1 = -1, y0 = H, y1 = -1; const rowL = new Int32Array(H).fill(-1), rowR = new Int32Array(H).fill(-1); let n = 0;
  const mark = (x: number, y: number) => { md.data[(y * W + x) * 4 + 3] = 255; n++; if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; if (rowL[y] < 0 || x < rowL[y]) rowL[y] = x; if (x > rowR[y]) rowR[y] = x; };
  if (big) {
    const lab = new Int32Array(W * H), st: number[] = []; let best = -1, bestN = 0, id = 0;
    for (let ys = Math.max(0, y0lim); ys < Math.min(H, y1lim); ys += 4) for (let xs = 40; xs < W - 40; xs += 4) { const p0 = xs + ys * W; if (lab[p0] || !ok(xs, ys)) continue; id++; let cnt = 0; st.push(p0); lab[p0] = id;
      while (st.length) { const q = st.pop()!, x = q % W, y = (q - x) / W; cnt++; for (const [dx, dy] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) { const nx = x + dx, ny = y + dy; if (nx < 0 || ny < 0 || nx >= W || ny >= H) continue; const p = nx + ny * W; if (lab[p] || !ok(nx, ny)) continue; lab[p] = id; st.push(p); } }
      if (cnt > bestN) { bestN = cnt; best = id; } }
    if (best > 0) for (let p = 0; p < W * H; p++) if (lab[p] === best) mark(p % W, (p - (p % W)) / W);
  } else for (let y = Math.max(0, y0lim); y < Math.min(H, y1lim); y++) for (let x = 0; x < W; x++) if (ok(x, y)) mark(x, y);
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
function clipTo(g: CanvasRenderingContext2D, mk: HTMLCanvasElement, fn: (x: CanvasRenderingContext2D) => void) {
  const l = document.createElement("canvas"); l.width = mk.width; l.height = mk.height; const x = l.getContext("2d")!; fn(x); x.globalCompositeOperation = "destination-in"; x.drawImage(mk, 0, 0); g.drawImage(l, 0, 0);
}

/** lấp các khe mảnh (nét tay, hàng cúc của thẻ cũ) trong mặt nạ để chữ in không bị đứt; vật to cầm trước ngực (giấy, điện thoại) vẫn là lỗ */
function closeMask(J: MK, R = 7) {
  const W = J.m.width, H = J.m.height, src = J.m.getContext("2d")!.getImageData(0, 0, W, H).data; const c = document.createElement("canvas"); c.width = W; c.height = H; const g = c.getContext("2d")!; const out = g.createImageData(W, H);
  const at = (x: number, y: number) => x >= 0 && x < W && y >= 0 && y < H && src[(y * W + x) * 4 + 3] > 0;
  for (let y = J.y0; y <= J.y1; y++) for (let x = J.x0; x <= J.x1; x++) { let ok = at(x, y); if (!ok) { let l = false, r = false, u = false, d = false; for (let k = 1; k <= R; k++) { l = l || at(x - k, y); r = r || at(x + k, y); u = u || at(x, y - k); d = d || at(x, y + k); } ok = (l && r) || (u && d); } if (ok) out.data[(y * W + x) * 4 + 3] = 255; }
  g.putImageData(out, 0, 0); return c;
}
/** toạ độ tương đối trên mảng áo: u -1 (lưng / trái màn) → +1 (ngực / phải màn), v 0 (cổ) → 1 (gấu) */
class Geo {
  W: number; H: number; cx: number;
  neck: number; // hàng đầu tiên thân áo hiện đủ rộng (phía trên bị cằm/đầu che) – chỗ đặt cổ áo
  constructor(public J: MK, public fr: number) { this.W = J.x1 - J.x0; this.H = J.y1 - J.y0; this.cx = (J.x0 + J.x1) / 2; let y = J.y0; while (y < J.y0 + this.H * 0.4 && (J.rowL[y] < 0 || J.rowR[y] - J.rowL[y] < this.W * 0.62)) y++; this.neck = y; }
  y(v: number) { return this.J.y0 + this.H * v; }
  private edge(a: Int32Array, y: number) { for (let d = 0; d < 40; d++) { const v = a[Math.round(y) + d]; if (v >= 0) return v; } return -1; }
  lo(y: number) { return this.fr < 0 ? this.edge(this.J.rowR, y) : this.edge(this.J.rowL, y); }
  hi(y: number) { return this.fr < 0 ? this.edge(this.J.rowL, y) : this.edge(this.J.rowR, y); }
  X(u: number, v: number) { const y = this.y(v), a = this.lo(y), b = this.hi(y); return a + (b - a) * (u + 1) / 2; }
  get side() { return this.fr !== 0; }
}

export class ActorX extends Actor {
  private xk = ""; private F: FitX;
  constructor(o: Outfit, h: number, private seedX: number, key: string) {
    const F = FIT[key] ?? ({ collar: o.long ? "v" : (["shirt", "polo", "round"] as Collar[])[seedX % 3], placket: o.long || seedX % 3 === 2 ? "none" : "buttons", dots: !!o.long && seedX % 2 === 0, waist: !!o.long, pockets: o.long ? [] : ["chest"] } as FitX);
    super({ ...o, ...(F.o ?? {}) } as Outfit, h, seedX); this.F = F;
  }
  pose(p: Pose, cam: THREE.Camera, tint: THREE.Color) {
    super.pose(p, cam, tint);
    const self = this as unknown as { key: string; g: CanvasRenderingContext2D; t: THREE.CanvasTexture };
    if (self.key === this.xk || this.o.anime) return; this.xk = self.key; this.dress(self.g, p); self.t.needsUpdate = true;
  }
  private dress(g: CanvasRenderingContext2D, p: Pose) {
    const o = this.o, F = this.F, acc = p.acc ?? []; let s = this.seedX * 7 + 3; const r = () => (s = (s * 16807) % 2147483647) / 2147483647;
    g.setTransform(1, 0, 0, 1, 0, 0); const img = g.getImageData(0, 0, 600, 1000);
    const J = mask(img, o.jacket, 26, 0.35, 1.25, 330, 960, true);
    const okJ = J.n > 1500 && !acc.includes("raincoat");
    const yLeg = okJ ? J.y1 + 4 : 700, S = mask(img, o.boots ?? "#e9e6df", 14, 0.7, 1.2, Math.max(yLeg + 6, 800), 1000), P = legMask(img, yLeg, S.n > 30 ? S.y0 - 2 : 990);
    if (okJ) { const G = new Geo(J, p.side ? (p.side > 0 ? 1 : -1) : 0); this.torso(g, G, r); this.over(g, G); }
    if (o.hat === "cap" && F.capBadge && okJ) this.cap(g, img, J, p.side ?? 0);
    this.legsShoes(g, S, P, r);
  }
  /** các món vẽ TRONG mảng áo */
  private torso(g: CanvasRenderingContext2D, G: Geo, r: () => number) {
    const o = this.o, F = this.F, { W, H, J } = G, top2 = dark(o.jacket, 0.78), seam = lum(o.jacket) > 170 ? "rgba(80,70,90,.35)" : "rgba(255,255,255,.32)", inkA = (a: number) => `rgba(36,23,38,${a})`;
    const pu = G.side ? 0.6 : 0;
    clipTo(g, J.m, (x) => {
      const a0 = G.side ? G.X(-1, 0.5) : J.x0, a1 = G.side ? G.X(1, 0.5) : J.x1, gb = x.createLinearGradient(a0, 0, a1, 0);
      if (G.side) { gb.addColorStop(0, "rgba(70,25,45,.34)"); gb.addColorStop(0.42, "rgba(70,25,45,.12)"); gb.addColorStop(0.62, "rgba(70,25,45,0)"); gb.addColorStop(0.88, "rgba(255,214,150,0)"); gb.addColorStop(1, "rgba(255,214,150,.28)"); }
      else { gb.addColorStop(0, "rgba(255,214,150,.22)"); gb.addColorStop(0.35, "rgba(255,214,150,0)"); gb.addColorStop(0.7, "rgba(70,25,45,.08)"); gb.addColorStop(1, "rgba(70,25,45,.32)"); }
      x.fillStyle = gb; x.fillRect(0, 0, 600, 1000);
      const gv = x.createLinearGradient(0, J.y0, 0, J.y1); gv.addColorStop(0, "rgba(255,230,190,.1)"); gv.addColorStop(0.72, "rgba(0,0,0,0)"); gv.addColorStop(1, "rgba(60,20,30,.25)"); x.fillStyle = gv; x.fillRect(0, 0, 600, 1000);
      if (F.knit) { x.strokeStyle = "rgba(0,0,0,.16)"; x.lineWidth = 2; for (let y = J.y0; y < J.y1; y += 7) { x.beginPath(); x.moveTo(J.x0, y); x.lineTo(J.x1, y); x.stroke(); } x.strokeStyle = "rgba(255,255,255,.12)"; for (let xx = J.x0; xx < J.x1; xx += 9) { x.beginPath(); x.moveTo(xx, J.y0); x.lineTo(xx, J.y1); x.stroke(); } }
      if (F.dots) for (let k = 0; k < 30; k++) { x.fillStyle = ["rgba(255,255,255,.55)", "rgba(255,240,160,.5)"][k % 2]; x.beginPath(); x.arc(J.x0 + r() * W, G.y(0.12 + r() * 0.82), 3 + r() * 3, 0, 7); x.fill(); }
      if (F.stripe) { x.fillStyle = F.stripe; for (const u of G.side ? [-0.2] : [-0.7, 0.7]) { const xx = G.X(u, 0.5); x.fillRect(xx - 5, J.y0, 10, H); } }
      x.lineCap = "round"; x.strokeStyle = inkA(0.32); x.lineWidth = 3.5;
      for (let k = 0; k < 3; k++) { const v = 0.56 + k * 0.12; for (const sg of G.side ? [1] : [-1, 1]) { const u0 = G.side ? -0.7 : sg * 0.85, u1 = G.side ? 0.1 : sg * (0.3 + r() * 0.15); x.beginPath(); x.moveTo(G.X(u0, v), G.y(v)); x.quadraticCurveTo(G.X((u0 + u1) / 2, v - 0.03), G.y(v - 0.03), G.X(u1, v - 0.06), G.y(v - 0.06)); x.stroke(); } }
      x.setLineDash([5, 6]); x.strokeStyle = seam; x.lineWidth = 2; const hem = F.hem ? 0.86 : 0.93;
      if (G.side) { x.beginPath(); for (let v = 0.3; v < 0.95; v += 0.02) x.lineTo(G.X(-0.85, v), G.y(v)); x.stroke(); }
      x.beginPath(); x.moveTo(J.x0, G.y(hem)); x.lineTo(J.x1, G.y(hem)); x.stroke(); x.setLineDash([]);
      if (F.hem) { x.fillStyle = top2; x.fillRect(0, G.y(0.88), 600, H); x.strokeStyle = "rgba(0,0,0,.25)"; x.lineWidth = 2; for (let xx = J.x0; xx < J.x1; xx += 7) { x.beginPath(); x.moveTo(xx, G.y(0.885)); x.lineTo(xx, J.y1); x.stroke(); } }
      if (F.tank) { // áo ba lỗ: khoét nách lộ vai (da) – theo khung bao vì mép trên thân rất hẹp
        x.fillStyle = o.skin ?? "#f1cfa8"; x.strokeStyle = INK; x.lineWidth = 4;
        const holes: [number, number][] = G.side ? [[G.X(-0.25, 0.14), G.y(0.1)]] : [[J.x0 + W * 0.08, J.y0 + H * 0.06], [J.x1 - W * 0.08, J.y0 + H * 0.06]];
        for (const [hx, hy] of holes) { x.beginPath(); x.ellipse(hx, hy, W * (G.side ? 0.24 : 0.2), H * 0.17, 0, 0, 7); x.fill(); x.stroke(); } }
      if (F.placket === "buttons" || F.placket === "cardigan") { x.strokeStyle = inkA(0.5); x.lineWidth = 3; x.beginPath(); for (let v = F.placket === "cardigan" ? 0.3 : 0.12; v <= 1; v += 0.02) x.lineTo(G.X(pu + 0.06, v), G.y(v)); x.stroke();
        if (F.placket === "cardigan") for (let k = 0; k < 4; k++) { const v = 0.4 + k * 0.15; x.fillStyle = "#e8dcc0"; x.beginPath(); x.arc(G.X(pu, v), G.y(v), 5, 0, 7); x.fill(); x.strokeStyle = INK; x.lineWidth = 1.5; x.stroke(); } }
      if (F.placket === "zip") { const uw = G.side ? 0.3 : 0.2; x.beginPath(); for (let v = 0; v <= 0.88; v += 0.02) x.lineTo(G.X(pu - uw, v), G.y(v)); for (let v = 0.88; v >= 0; v -= 0.02) x.lineTo(G.side ? G.X(1.2, v) : G.X(uw, v), G.y(v)); x.closePath(); x.fillStyle = "#f2efe6"; x.fill();
        for (const u of G.side ? [pu - uw] : [-uw, uw]) { x.strokeStyle = "#3a3a40"; x.lineWidth = 5; x.beginPath(); for (let v = 0; v <= 0.88; v += 0.02) x.lineTo(G.X(u, v), G.y(v)); x.stroke(); x.strokeStyle = "#c9cdd3"; x.lineWidth = 2; x.setLineDash([3, 3]); x.stroke(); x.setLineDash([]); }
        const zx = G.X(G.side ? pu - uw : uw, 0.3); x.fillStyle = "#c9cdd3"; x.fillRect(zx - 4, G.y(0.3), 8, 16); x.strokeStyle = INK; x.lineWidth = 2; x.strokeRect(zx - 4, G.y(0.3), 8, 16); }
      if (F.placket === "suit") {
        x.strokeStyle = inkA(0.6); x.lineWidth = 3.5; for (const sg of G.side ? [1] : [-1, 1]) { const uc = G.side ? 0.55 : 0; x.beginPath(); x.moveTo(G.X(uc + sg * 0.45, 0), G.y(0)); x.lineTo(G.X(uc + sg * 0.12, 0.45), G.y(0.45)); x.lineTo(G.X(uc + sg * 0.5, 0.2), G.y(0.2)); x.stroke(); }
        x.fillStyle = "#e8e4dc"; for (let k = 0; k < 2; k++) { const v = 0.55 + k * 0.14; x.beginPath(); x.arc(G.X(G.side ? 0.62 : 0.05, v), G.y(v), 5, 0, 7); x.fill(); } }
      const pocket = (u: number, v: number, pw: number, ph: number, flap = true) => { const px = G.X(u, v) - pw / 2, py = G.y(v); x.fillStyle = top2; x.fillRect(px, py, pw, ph); x.strokeStyle = inkA(0.75); x.lineWidth = 3; x.strokeRect(px, py, pw, ph);
        if (flap) { x.fillRect(px - 2, py - 6, pw + 4, ph * 0.38); x.strokeRect(px - 2, py - 6, pw + 4, ph * 0.38); } x.setLineDash([3, 4]); x.strokeStyle = seam; x.lineWidth = 1.5; x.strokeRect(px + 4, py + ph * (flap ? 0.4 : 0.15), pw - 8, ph * (flap ? 0.5 : 0.7)); x.setLineDash([]); };
      for (const pk of F.pockets ?? []) {
        if (pk === "chest") pocket(G.side ? 0.15 : -0.45, 0.27, W * (G.side ? 0.26 : 0.24), H * 0.13);
        if (pk === "chest2") for (const u of G.side ? [0.15] : [-0.45, 0.45]) pocket(u, 0.27, W * 0.24, H * 0.13);
        if (pk === "lower2") for (const u of G.side ? [0.3] : [-0.45, 0.45]) pocket(u, 0.62, W * 0.26, H * 0.16, false);
        if (pk === "kangaroo") { x.fillStyle = top2; x.strokeStyle = inkA(0.7); x.lineWidth = 3; const ua = G.side ? 0.1 : -0.55, ub = G.side ? 1.1 : 0.55; x.beginPath(); x.moveTo(G.X(ua + 0.15, 0.6), G.y(0.6)); x.lineTo(G.X(ub - 0.15, 0.6), G.y(0.6)); x.lineTo(G.X(ub, 0.84), G.y(0.84)); x.lineTo(G.X(ua, 0.84), G.y(0.84)); x.closePath(); x.fill(); x.stroke(); }
        if (pk === "slant") { x.strokeStyle = inkA(0.55); x.lineWidth = 3.5; for (const u of G.side ? [-0.1] : [-0.55, 0.55]) { const du = G.side ? 0.18 : (u < 0 ? 0.18 : -0.18); x.beginPath(); x.moveTo(G.X(u, 0.6), G.y(0.6)); x.lineTo(G.X(u + du, 0.76), G.y(0.76)); x.stroke(); } }
      }
      if (F.apron) { const ua = G.side ? 0.0 : -0.6, ub = G.side ? 1.2 : 0.6; x.fillStyle = F.apron; x.strokeStyle = inkA(0.6); x.lineWidth = 3; x.beginPath(); x.moveTo(G.X(ua + 0.15, 0.32), G.y(0.32)); x.lineTo(G.X(ub - 0.15, 0.32), G.y(0.32)); x.lineTo(G.X(ub, 1), J.y1 + 4); x.lineTo(G.X(ua, 1), J.y1 + 4); x.closePath(); x.fill(); x.stroke();
        x.fillStyle = "rgba(200,32,47,.8)"; x.fillRect(G.X(ua, 0.45), G.y(0.45), G.X(ub, 0.45) - G.X(ua, 0.45), 5); x.strokeStyle = "#c8202f"; x.lineWidth = 3; x.beginPath(); x.moveTo(G.X(ua + 0.2, 0.32), G.y(0.32)); x.lineTo(G.X(G.side ? 0.4 : 0, 0), J.y0); x.lineTo(G.X(ub - 0.2, 0.32), G.y(0.32)); x.stroke(); }
      if (F.stains) for (let k = 0; k < 9; k++) { const sx = J.x0 + r() * W, sy = G.y(0.35 + r() * 0.6), q = 5 + r() * 13; const gg = x.createRadialGradient(sx, sy, 0, sx, sy, q); gg.addColorStop(0, "rgba(22,18,16,.7)"); gg.addColorStop(1, "rgba(22,18,16,0)"); x.fillStyle = gg; x.beginPath(); x.ellipse(sx, sy, q, q * 0.7, r() * 3, 0, 7); x.fill(); }
      if (F.waist) { x.strokeStyle = inkA(0.4); x.lineWidth = 3; x.beginPath(); for (let u = -1.1; u <= 1.1; u += 0.1) x.lineTo(G.X(u, 0.62), G.y(0.62) + (1 - u * u) * 4); x.stroke(); }
    });
    clipTo(g, closeMask(J), (x) => {
      const txt = (t: string, u: number, v: number, sz: number, col: string, bg?: string) => { x.font = `900 ${sz}px ${FONT}`; x.textAlign = "center"; const tw = Math.min(x.measureText(t).width, W * 0.8); const xx = G.X(u, v); if (bg) { x.fillStyle = bg; x.fillRect(xx - tw / 2 - 5, G.y(v) - sz, tw + 10, sz + 7); x.strokeStyle = INK; x.lineWidth = 2; x.strokeRect(xx - tw / 2 - 5, G.y(v) - sz, tw + 10, sz + 7); } x.fillStyle = col; x.fillText(t, xx, G.y(v) + 1, W * 0.8); };
      const pcol = lum(o.jacket) > 150 ? "#1f2a44" : "#f4f1e6";
      if (F.print) txt(F.print, G.side ? 0.25 : 0, 0.5, F.print.length <= 2 ? 44 : F.print.length <= 4 ? 30 : 22, pcol);
      if (F.logo) txt(F.logo, G.side ? 0.2 : 0.45, 0.24, 15, lum(o.jacket) > 150 ? "#c8202f" : "#f2d36b");
      if (F.tag) { const has = (F.pockets ?? []).includes("chest") || (F.pockets ?? []).includes("chest2"); txt(F.tag, G.side ? 0.2 : -0.45, has ? 0.5 : 0.36, 14, "#1f3d8a", "#f4f1e6"); }
      if (F.badge) { const bx = G.X(G.side ? 0.15 : 0.45, 0.48), by = G.y(0.48); x.fillStyle = "#f2d36b"; x.strokeStyle = INK; x.lineWidth = 2.5; x.beginPath(); x.moveTo(bx - 12, by - 12); x.lineTo(bx + 12, by - 12); x.lineTo(bx + 12, by + 4); x.lineTo(bx, by + 14); x.lineTo(bx - 12, by + 4); x.closePath(); x.fill(); x.stroke(); x.fillStyle = "#c8202f"; x.beginPath(); x.arc(bx, by - 2, 4, 0, 7); x.fill(); }
    });
  }
  /** các món vẽ ĐÈ lên mép trên thân (cổ áo, mũ trùm, quân hàm, khăn, dây chuyền, bút, giẻ lau) – có viền mực */
  private over(g0: CanvasRenderingContext2D, G: Geo) {
    // vẽ lên lớp riêng rồi chỉ giữ phần trong thân áo + dải cổ (không đè lên giấy/điện thoại cầm trước ngực, tay, mặt)
    const lay = document.createElement("canvas"); lay.width = 600; lay.height = 1000; const g = lay.getContext("2d")!;
    const mk = document.createElement("canvas"); mk.width = 600; mk.height = 1000; const mg = mk.getContext("2d")!; mg.drawImage(G.J.m, 0, 0); mg.fillStyle = "#000"; mg.fillRect(G.J.x0 - 30, G.neck - 30, G.W + 60, 30 + 8);
    this.overDraw(g, G); g.globalCompositeOperation = "destination-in"; g.drawImage(mk, 0, 0); g0.drawImage(lay, 0, 0); this.rag(g0, G);
  }
  private overDraw(g: CanvasRenderingContext2D, G: Geo) {
    const o = this.o, F = this.F, { W, H, J, cx } = G, top2 = lum(o.jacket) < 110 ? dark(o.jacket, 1.45) : dark(o.jacket, 0.78); g.lineJoin = "round"; g.strokeStyle = INK; g.lineWidth = 4;
    const cy0 = G.neck + 4, c = F.collar ?? "none";
    const vN = (G.neck - J.y0) / H + 0.02, L = G.X(G.side ? -0.75 : -0.45, vN), R = G.X(G.side ? 0.85 : 0.45, vN), mid = (L + R) / 2;
    const poly = (pts: [number, number][], col: string) => { g.fillStyle = col; g.beginPath(); pts.forEach(([a, b], i) => (i ? g.lineTo(a, b) : g.moveTo(a, b))); g.closePath(); g.fill(); g.stroke(); };
    if (c === "shirt" || c === "polo") { const d = c === "polo" ? 0.9 : 1, col = c === "polo" ? top2 : (F.placket === "suit" ? "#f6f4ee" : top2);
      if (G.side) { const fr = G.fr; poly([[L, cy0 + 2], [R - fr * 10, cy0 + 2], [R - fr * W * 0.18 * d, cy0 + H * 0.12 * d], [R - fr * W * 0.3 * d, cy0 + 6]], col); }
      else for (const sg of [-1, 1]) poly([[cx, cy0 + H * 0.1 * d], [cx + sg * W * 0.3, cy0], [cx + sg * W * 0.1, cy0 - 4]], col);
      if (c === "polo") for (let k = 0; k < 2; k++) { g.fillStyle = "#e8e4dc"; g.beginPath(); g.arc(G.side ? R - G.fr * W * 0.18 : cx, cy0 + H * (0.13 + k * 0.07), 4, 0, 7); g.fill(); } }
    else if (c === "stand") { g.fillStyle = top2; g.beginPath(); g.moveTo(L, cy0 + 8); g.lineTo(L, cy0 - 10); g.quadraticCurveTo(mid, cy0 - 18, R, cy0 - 10); g.lineTo(R, cy0 + 8); g.quadraticCurveTo(mid, cy0, L, cy0 + 8); g.fill(); g.stroke(); }
    else if (c === "round") { g.strokeStyle = top2; g.lineWidth = 9; g.beginPath(); g.moveTo(L, cy0); g.quadraticCurveTo(mid, cy0 + 16, R, cy0); g.stroke(); g.strokeStyle = INK; g.lineWidth = 2; g.stroke(); g.lineWidth = 4; }
    else if (c === "v" || c === "baba") { const deep = c === "v" ? H * 0.16 : H * 0.07; g.strokeStyle = c === "v" && !F.knit ? "#f4f1e6" : top2; g.lineWidth = 6; g.beginPath(); g.moveTo(L, cy0); g.lineTo(G.side ? R - G.fr * W * 0.12 : cx, cy0 + deep); g.lineTo(R, cy0); g.stroke(); g.strokeStyle = INK; g.lineWidth = 4;
      if (c === "baba") { g.strokeStyle = "rgba(36,23,38,.5)"; g.lineWidth = 3; for (const u of G.side ? [0.6] : [-0.2]) { g.beginPath(); g.moveTo(G.X(u, 0.05), G.y(0.05)); g.quadraticCurveTo(G.X(u + 0.35, 0.2), G.y(0.2), G.X(u + 0.3, 0.55), G.y(0.55)); g.stroke(); } g.strokeStyle = INK; g.lineWidth = 4; } }
    else if (c === "hood") { const hx = G.side ? G.X(-0.6, 0) : cx, hw = G.side ? W * 0.45 : W * 0.75; g.fillStyle = top2; g.beginPath(); g.ellipse(hx, cy0 + 2, hw / 2, 16, 0, Math.PI, 0); g.lineTo(hx + hw / 2, cy0 + 8); g.quadraticCurveTo(hx, cy0 + 20, hx - hw / 2, cy0 + 8); g.closePath(); g.fill(); g.stroke();
      g.strokeStyle = "#f4f1e6"; g.lineWidth = 3; for (const dx of G.side ? [0] : [-10, 10]) { const sx = G.side ? R - G.fr * 18 : cx + dx; g.beginPath(); g.moveTo(sx, cy0 + 10); g.lineTo(sx + dx * 0.2, cy0 + H * 0.25); g.stroke(); } g.strokeStyle = INK; g.lineWidth = 4; }
    if (F.epaulette) for (const ex of G.side ? [G.X(-0.1, 0.05)] : [J.x0 + W * 0.17, J.x1 - W * 0.17]) { const ey = cy0 + 2; g.fillStyle = "#2a2f2a"; g.fillRect(ex - 16, ey - 6, 32, 12); g.strokeRect(ex - 16, ey - 6, 32, 12); g.fillStyle = "#f2d36b"; for (let k = 0; k < 2; k++) g.fillRect(ex - 10 + k * 10, ey - 3, 6, 6); }
    if (F.scarf) { const kx = G.side ? R - G.fr * 14 : cx, ky = cy0 + 10; g.fillStyle = F.scarf; g.beginPath(); g.moveTo(kx - 12, ky - 6); g.lineTo(kx + 12, ky - 6); g.lineTo(kx + 4, ky + 6); g.lineTo(kx + 10, ky + 28); g.lineTo(kx - 2, ky + 24); g.lineTo(kx - 10, ky + 30); g.lineTo(kx - 4, ky + 6); g.closePath(); g.fill(); g.stroke(); }
    if (F.chain) { g.strokeStyle = "#e8c22a"; g.lineWidth = 4; g.setLineDash([4, 3]); g.beginPath(); g.moveTo(L + (R - L) * 0.15, cy0 + 4); g.quadraticCurveTo(G.side ? R - G.fr * W * 0.15 : cx, cy0 + H * 0.2, R - (R - L) * 0.15, cy0 + 4); g.stroke(); g.setLineDash([]); g.strokeStyle = INK; g.lineWidth = 4; }
    if (F.pen && (F.pockets ?? []).length) { const px = G.X(G.side ? 0.05 : -0.38, 0.27), py = G.y(0.27); g.lineWidth = 2.5; g.fillStyle = "#f4f4f2"; g.fillRect(px - 3, py - 20, 6, 22); g.strokeRect(px - 3, py - 20, 6, 22); g.fillStyle = "#c8202f"; g.fillRect(px - 3, py - 24, 6, 6); g.lineWidth = 4; }
  }
  private rag(g: CanvasRenderingContext2D, G: Geo) {
    const F = this.F, { J } = G; g.lineJoin = "round"; g.strokeStyle = INK; g.lineWidth = 4;
    if (F.rag && G.side) { const ry = J.y1 - 10, rx = G.X(-0.85, 0.97); const fr = G.fr; g.fillStyle = "#c8202f"; g.beginPath(); g.moveTo(rx, ry - 6); g.quadraticCurveTo(rx - fr * 24, ry + 30, rx - fr * 14, ry + 74); g.lineTo(rx + fr * 8, ry + 70); g.quadraticCurveTo(rx + fr * 2, ry + 30, rx + fr * 20, ry - 4); g.closePath(); g.fill(); g.stroke();
      g.strokeStyle = "rgba(255,255,255,.7)"; g.lineWidth = 2.5; for (const k of [0.3, 0.55, 0.8]) { g.beginPath(); g.moveTo(rx - fr * 16 * k, ry + 70 * k); g.lineTo(rx + fr * 10, ry + 70 * k - 4); g.stroke(); } g.strokeStyle = INK; g.lineWidth = 4; }
  }
  /** phù hiệu trên mũ lưỡi trai */
  private cap(g: CanvasRenderingContext2D, img: ImageData, J: MK, side: number) {
    const C = mask(img, this.o.cap ?? "#111", 22, 0.5, 1.2, 0, J.y0 - 20, true); if (C.n < 300) return;
    const bx = side ? (side > 0 ? C.x0 + (C.x1 - C.x0) * 0.62 : C.x0 + (C.x1 - C.x0) * 0.38) : (C.x0 + C.x1) / 2, by = C.y0 + (C.y1 - C.y0) * 0.45;
    g.fillStyle = this.F.capBadge!; g.strokeStyle = INK; g.lineWidth = 2.5; g.beginPath(); for (let k = 0; k < 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5, rr = k % 2 ? 6 : 13; g.lineTo(bx + Math.cos(a) * rr, by + Math.sin(a) * rr); } g.closePath(); g.fill(); g.stroke();
  }
  private legsShoes(g: CanvasRenderingContext2D, S: MK, P: LM, r: () => number) {
    const o = this.o, F = this.F;
    if (P.n > 60) clipTo(g, P.m, (x) => { x.fillStyle = F.pants ?? o.pants; x.fillRect(0, P.y0, 600, P.y1 - P.y0); const gp = x.createLinearGradient(0, P.y0, 0, P.y1); gp.addColorStop(0, "rgba(0,0,0,.25)"); gp.addColorStop(0.3, "rgba(0,0,0,0)"); gp.addColorStop(1, "rgba(0,0,0,.15)"); x.fillStyle = gp; x.fillRect(0, P.y0, 600, P.y1 - P.y0);
      x.strokeStyle = "rgba(20,10,20,.5)"; x.lineWidth = 3; const ky = P.y0 + (P.y1 - P.y0) * 0.45; for (const d of [-6, 6]) { x.beginPath(); x.moveTo(P.x0, ky + d); x.lineTo(P.x1, ky + d + 5); x.stroke(); }
      if (F.stains) { x.fillStyle = "rgba(20,16,14,.6)"; for (let k = 0; k < 4; k++) { x.beginPath(); x.ellipse(P.x0 + r() * (P.x1 - P.x0), P.y0 + r() * (P.y1 - P.y0), 4, 6, 0, 0, 7); x.fill(); } } });
    if (S.n > 30) clipTo(g, S.m, (x) => { const h = S.y1 - S.y0; x.fillStyle = "#4a4048"; x.fillRect(0, S.y1 - h * 0.28, 600, h); x.fillStyle = "#c8202f"; x.fillRect(0, S.y0 + h * 0.45, 600, 3); x.fillStyle = "rgba(255,255,255,.35)"; x.fillRect(0, S.y0 + 2, 600, 3); });
  }
}
