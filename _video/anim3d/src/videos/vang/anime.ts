// Nhân vật phong cách ANIME (từ 15/11/2026, chỉ dùng cho phim mới): mắt to có tròng + ánh sáng, tóc nhiều lọn,
// tỉ lệ thiếu niên ~1:6, đồng phục quý tộc (blazer, cổ áo, cà vạt, huy hiệu), váy xếp ly cho nữ.
// Vẽ lên canvas 600x1000 (cùng khung với nhân vật cũ), chân chạm y = 975, tâm x = 300.
import type { Expr } from "../pho/toon";

export type AnimeLook = {
  skin: string; hair: string; eye: string; jacket: string; pants: string; shoes: string;
  collar?: string; tie?: string; crest?: string; girl?: boolean; style: "spiky" | "neat" | "long" | "pony" | "bob" | "old" | "wavy";
  moustache?: string; glasses?: boolean; h?: number;
};
type Ctx = CanvasRenderingContext2D;
const INK = "#2a1b2e";
const shade = (hex: string, k: number) => { const n = parseInt(hex.slice(1), 16); const f = (v: number) => Math.max(0, Math.min(255, Math.round(v * k)));
  return `rgb(${f(n >> 16)},${f((n >> 8) & 255)},${f(n & 255)})`; };
const path = (g: Ctx, pts: [number, number][], close = true) => { g.beginPath(); g.moveTo(pts[0][0], pts[0][1]); for (const p of pts.slice(1)) g.lineTo(p[0], p[1]); if (close) g.closePath(); };
const fillStroke = (g: Ctx, fill: string, lw = 5) => { g.fillStyle = fill; g.fill(); g.lineWidth = lw; g.strokeStyle = INK; g.lineJoin = "round"; g.lineCap = "round"; g.stroke(); };

export type AnimePose = { expr: Expr; blink?: boolean; side?: 1 | -1; t?: number; talk?: boolean; wave?: number; book?: boolean };

export function drawAnime(g: Ctx, L: AnimeLook, P: AnimePose) {
  const s = (L.h ?? 1.7) / 1.7;                    // thầy cao hơn trò một chút
  const look = P.side ? 1 : 0;                     // 3/4 mặt hướng về phía nói chuyện (đã lật gương ngoài hàm)
  const cx = 300, sole = 975;
  const headH = 205 * (0.92 + 0.08 * s), headW = 176 * (0.92 + 0.08 * s);
  const bodyTop = sole - 660 * s;                  // vai
  const hy = bodyTop - headH * 0.46;               // tâm đầu
  const fx = cx + look * 14;                       // tâm mặt lệch về hướng nhìn
  const legTop = bodyTop + 300 * s, hipW = 82;
  g.save();
  // ---------- tóc sau (nữ tóc dài / đuôi ngựa) ----------
  if (L.style === "long" || L.style === "wavy") { g.beginPath(); g.moveTo(cx - headW * 0.55, hy - headH * 0.2);
    g.quadraticCurveTo(cx - headW * 0.75, hy + headH * 0.9, cx - headW * 0.48, bodyTop + 170 * s); g.lineTo(cx + headW * 0.48, bodyTop + 170 * s);
    g.quadraticCurveTo(cx + headW * 0.75, hy + headH * 0.9, cx + headW * 0.55, hy - headH * 0.2); g.closePath(); fillStroke(g, shade(L.hair, 0.82)); }
  if (L.style === "pony") { g.beginPath(); g.moveTo(cx - look * 40 - 30, hy - headH * 0.35); g.quadraticCurveTo(cx - look * 140 - 60, hy + 40, cx - look * 90 - 20, bodyTop + 120);
    g.quadraticCurveTo(cx - look * 60, hy + 60, cx - look * 40 + 30, hy - headH * 0.35); g.closePath(); fillStroke(g, shade(L.hair, 0.85)); }
  // ---------- chân + giày ----------
  const skirt = !!L.girl;
  for (const sd of [-1, 1]) {
    const x0 = cx + sd * 34, x1 = cx + sd * 40;
    path(g, [[x0 - 24, legTop], [x0 + 24, legTop], [x1 + 20, sole - 40], [x1 - 20, sole - 40]]);
    fillStroke(g, skirt ? "#f4f2ee" : L.pants);                  // nữ: tất trắng cao
    if (skirt) { path(g, [[x1 - 21, legTop + 150], [x1 + 21, legTop + 150], [x1 + 21, legTop + 175], [x1 - 21, legTop + 175]]); g.fillStyle = L.skin; g.fill(); }
    g.beginPath(); g.ellipse(x1 + sd * 6, sole - 22, 38, 22, 0, 0, Math.PI * 2); fillStroke(g, L.shoes);
    g.beginPath(); g.ellipse(x1 + sd * 2, sole - 30, 14, 6, 0, 0, Math.PI * 2); g.fillStyle = "rgba(255,255,255,.35)"; g.fill();
  }
  // ---------- thân: blazer ----------
  const sw = 118 * (0.95 + 0.05 * s);
  path(g, [[cx - sw, bodyTop + 20], [cx - sw * 0.55, bodyTop - 8], [cx + sw * 0.55, bodyTop - 8], [cx + sw, bodyTop + 20], [cx + hipW + 18, legTop + 20], [cx - hipW - 18, legTop + 20]]);
  fillStroke(g, L.jacket, 6);
  // váy xếp ly
  if (skirt) { path(g, [[cx - hipW - 10, legTop - 10], [cx + hipW + 10, legTop - 10], [cx + hipW + 40, legTop + 120], [cx - hipW - 40, legTop + 120]]); fillStroke(g, shade(L.pants, 1));
    g.strokeStyle = shade(L.pants, 0.7); g.lineWidth = 3; for (let i = -3; i <= 3; i++) { g.beginPath(); g.moveTo(cx + i * 22, legTop); g.lineTo(cx + i * 30, legTop + 118); g.stroke(); } }
  // cổ áo sơ mi + cà vạt + ve áo
  path(g, [[cx - 46, bodyTop - 6], [cx + 46, bodyTop - 6], [cx + look * 6, bodyTop + 110]]); fillStroke(g, L.collar ?? "#f8f6f0", 4);
  if (L.tie) { path(g, [[cx - 11 + look * 4, bodyTop + 8], [cx + 11 + look * 4, bodyTop + 8], [cx + 16 + look * 5, bodyTop + 130], [cx + look * 5, bodyTop + 152], [cx - 16 + look * 5, bodyTop + 130]]); fillStroke(g, L.tie, 4);
    g.strokeStyle = "rgba(255,255,255,.35)"; g.lineWidth = 4; for (const y of [50, 85, 120]) { g.beginPath(); g.moveTo(cx - 10 + look * 5, bodyTop + y); g.lineTo(cx + 10 + look * 5, bodyTop + y - 10); g.stroke(); } }
  for (const sd of [-1, 1]) { path(g, [[cx + sd * 46, bodyTop - 6], [cx + sd * 74, bodyTop + 16], [cx + sd * 30, bodyTop + 150], [cx + sd * 8, bodyTop + 120]]); fillStroke(g, shade(L.jacket, 0.85), 4); }
  if (L.crest) { const x = cx - 62, y = bodyTop + 82; path(g, [[x - 16, y - 16], [x + 16, y - 16], [x + 16, y + 4], [x, y + 20], [x - 16, y + 4]]); fillStroke(g, L.crest, 3); g.fillStyle = "#7a1424"; g.beginPath(); g.arc(x, y - 2, 5, 0, 7); g.fill(); }
  for (const y of [190, 240]) { g.beginPath(); g.arc(cx + 8, bodyTop + y, 6, 0, 7); g.fillStyle = "#e0b54a"; g.fill(); g.strokeStyle = INK; g.lineWidth = 2; g.stroke(); }
  // ---------- tay ----------
  const wave = P.wave ?? 0;
  for (const sd of [-1, 1]) {
    const shx = cx + sd * (sw - 14), shy = bodyTop + 26;
    const up = sd === 1 && wave > 0;
    const hx = up ? shx + 60 : shx + sd * 14, hy2 = up ? shy - 150 + 10 * Math.sin((P.t ?? 0) * 12) : shy + 270 * s;
    g.lineCap = "round"; g.strokeStyle = INK; g.lineWidth = 50; g.beginPath(); g.moveTo(shx, shy); g.lineTo(hx, hy2); g.stroke();
    g.strokeStyle = L.jacket; g.lineWidth = 40; g.beginPath(); g.moveTo(shx, shy); g.lineTo(hx, hy2); g.stroke();
    g.beginPath(); g.arc(hx, hy2 + (up ? -14 : 16), 19, 0, 7); fillStroke(g, L.skin, 4);
  }
  if (P.book) { path(g, [[cx + sw - 30, bodyTop + 200], [cx + sw + 40, bodyTop + 190], [cx + sw + 46, bodyTop + 290], [cx + sw - 24, bodyTop + 300]]); fillStroke(g, "#6b1424", 4); }
  // ---------- cổ + đầu ----------
  path(g, [[cx - 22, bodyTop - 40], [cx + 22, bodyTop - 40], [cx + 24, bodyTop + 4], [cx - 24, bodyTop + 4]]); fillStroke(g, shade(L.skin, 0.9), 4);
  // tai
  for (const sd of [-1, 1]) { g.beginPath(); g.ellipse(fx + sd * headW * 0.47, hy + 14, 15, 24, 0, 0, 7); fillStroke(g, L.skin, 4); }
  // mặt: tròn trên, cằm nhọn
  g.beginPath(); g.moveTo(fx - headW * 0.48, hy - headH * 0.12);
  g.bezierCurveTo(fx - headW * 0.5, hy - headH * 0.62, fx + headW * 0.5, hy - headH * 0.62, fx + headW * 0.48, hy - headH * 0.12);
  g.bezierCurveTo(fx + headW * 0.46, hy + headH * 0.22, fx + headW * 0.2, hy + headH * 0.44, fx + look * 6, hy + headH * 0.5);
  g.bezierCurveTo(fx - headW * 0.2, hy + headH * 0.44, fx - headW * 0.46, hy + headH * 0.22, fx - headW * 0.48, hy - headH * 0.12); g.closePath();
  fillStroke(g, L.skin, 5);
  // má hồng
  g.fillStyle = "rgba(255,120,130,.28)"; for (const sd of [-1, 1]) { g.beginPath(); g.ellipse(fx + sd * headW * 0.27, hy + headH * 0.17, 20, 10, 0, 0, 7); g.fill(); }
  drawFace(g, L, P, fx, hy, headW, headH, look);
  drawHairFront(g, L, cx + look * 8, hy, headW, headH, look);
  if (L.glasses) { g.strokeStyle = "#b8862e"; g.lineWidth = 4; for (const sd of [-1, 1]) { g.beginPath(); g.ellipse(fx + sd * 38 + look * 4, hy + 4, 30, 24, 0, 0, 7); g.stroke(); } g.beginPath(); g.moveTo(fx - 8, hy); g.lineTo(fx + 8, hy); g.stroke(); }
  g.restore();
}

function drawFace(g: Ctx, L: AnimeLook, P: AnimePose, fx: number, hy: number, W: number, H: number, look: number) {
  const e = P.expr, closed = P.blink || e === "sleepy" || e === "laugh" || e === "smile_closed" || e === "relief";
  const ey = hy + H * 0.02, ex = W * 0.21, shock = e === "shock" || e === "dazed";
  // lông mày
  const brow: Record<string, number> = { stern: 0.35, worried: -0.35, sad: -0.4, nervous: -0.3, shock: -0.1, smug: 0.15, cry: -0.4 };
  const bt = brow[e] ?? 0;
  g.strokeStyle = shade(L.hair, 0.6); g.lineWidth = 6; g.lineCap = "round";
  for (const sd of [-1, 1]) { g.beginPath(); g.moveTo(fx + sd * ex - 22 + look * 6, ey - 52 + sd * bt * -12 * -1 + (sd < 0 ? bt * 10 : -bt * 10) * 0);
    const inner = sd < 0 ? 22 : -22; g.moveTo(fx + sd * ex + inner * -1 + look * 6, ey - 50); g.lineTo(fx + sd * ex - inner * -1 + look * 6, ey - 50); g.stroke(); }
  // nếu mày nhíu/buồn: vẽ lại nghiêng
  if (bt !== 0) { g.strokeStyle = shade(L.hair, 0.6); g.lineWidth = 6; for (const sd of [-1, 1]) { const xIn = fx + sd * (ex - 20) + look * 6, xOut = fx + sd * (ex + 22) + look * 6;
    g.beginPath(); g.moveTo(xIn, ey - 50 + bt * 14); g.lineTo(xOut, ey - 50 - bt * 6); g.stroke(); } }
  for (const sd of [-1, 1]) {
    const x = fx + sd * ex + look * 8, y = ey;
    if (closed) { g.strokeStyle = INK; g.lineWidth = 6; g.beginPath(); if (e === "laugh" || e === "relief" || e === "smile_closed") { g.arc(x, y + 6, 18, Math.PI * 1.1, Math.PI * 1.9); } else { g.moveTo(x - 20, y); g.lineTo(x + 20, y); } g.stroke(); continue; }
    const ew = shock ? 21 : 20, eh = shock ? 30 : 27;
    // tròng trắng
    g.beginPath(); g.ellipse(x, y, ew, eh, 0, 0, 7); g.fillStyle = "#fff"; g.fill();
    // tròng màu (gradient)
    const ir = shock ? 11 : 16; const ix = x + look * 6, iy = y + 3;
    const gr = g.createLinearGradient(ix, iy - ir * 1.3, ix, iy + ir * 1.3); gr.addColorStop(0, shade(L.eye, 0.55)); gr.addColorStop(1, shade(L.eye, 1.25));
    g.beginPath(); g.ellipse(ix, iy, ir, ir * 1.3, 0, 0, 7); g.fillStyle = gr; g.fill();
    g.beginPath(); g.ellipse(ix, iy + 2, ir * 0.45, ir * 0.6, 0, 0, 7); g.fillStyle = "#140c18"; g.fill();
    // ánh sáng
    g.fillStyle = "#fff"; g.beginPath(); g.arc(ix - ir * 0.4, iy - ir * 0.55, ir * 0.38, 0, 7); g.fill(); g.beginPath(); g.arc(ix + ir * 0.45, iy + ir * 0.45, ir * 0.18, 0, 7); g.fill();
    // mi trên dày + mi dưới
    g.strokeStyle = INK; g.lineWidth = 7; g.beginPath(); g.ellipse(x, y, ew + 1, eh + 1, 0, Math.PI * 1.08, Math.PI * 1.92); g.stroke();
    g.lineWidth = 3; g.beginPath(); g.ellipse(x, y, ew - 2, eh - 2, 0, Math.PI * 0.25, Math.PI * 0.75); g.stroke();
    if (L.girl) { g.lineWidth = 4; g.beginPath(); g.moveTo(x + sd * (ew - 2), y - eh * 0.6); g.lineTo(x + sd * (ew + 8), y - eh * 0.9); g.stroke(); }
    if (e === "cry" || e === "sad") { g.fillStyle = "rgba(120,190,255,.85)"; g.beginPath(); g.ellipse(x + 4, y + eh + 14, 5, 9, 0, 0, 7); g.fill(); }
  }
  // mũi
  g.strokeStyle = shade(L.skin, 0.7); g.lineWidth = 3; g.beginPath(); g.moveTo(fx + look * 12, hy + H * 0.13); g.lineTo(fx + look * 12 + 4, hy + H * 0.17); g.stroke();
  // miệng
  const my = hy + H * 0.29, mx = fx + look * 10; g.strokeStyle = INK; g.lineWidth = 5;
  const talk = P.talk && Math.floor((P.t ?? 0) * 9) % 2 === 0;
  if (e === "laugh" || e === "grin" || e === "relief_open" || talk || e === "shock") {
    g.beginPath(); if (e === "shock") g.ellipse(mx, my + 4, 11, 15, 0, 0, 7); else { g.moveTo(mx - 20, my - 2); g.quadraticCurveTo(mx, my + (talk ? 16 : 26), mx + 20, my - 2); g.closePath(); }
    g.fillStyle = "#7a2030"; g.fill(); g.stroke(); g.fillStyle = "#ff8a9a"; g.beginPath(); g.ellipse(mx, my + 8, 8, 5, 0, 0, 7); g.fill();
  } else if (e === "smile" || e === "smug" || e === "relief" || e === "smile_closed") { g.beginPath(); g.moveTo(mx - 16, my); g.quadraticCurveTo(mx, my + 12, mx + 16, my - (e === "smug" ? 6 : 0)); g.stroke(); }
  else if (e === "sad" || e === "worried" || e === "cry" || e === "nervous") { g.beginPath(); g.moveTo(mx - 14, my + 6); g.quadraticCurveTo(mx, my - 4, mx + 14, my + 6); g.stroke(); }
  else { g.beginPath(); g.moveTo(mx - 10, my + 2); g.lineTo(mx + 10, my + 2); g.stroke(); }
  if (e === "nervous") { g.fillStyle = "rgba(140,200,255,.9)"; g.beginPath(); g.ellipse(fx + W * 0.42, hy - H * 0.2, 7, 12, 0, 0, 7); g.fill(); }
  if (L.moustache) { g.fillStyle = L.moustache; g.beginPath(); g.ellipse(mx - 14, my - 12, 16, 7, 0.2, 0, 7); g.ellipse(mx + 14, my - 12, 16, 7, -0.2, 0, 7); g.fill(); }
}

function drawHairFront(g: Ctx, L: AnimeLook, cx: number, hy: number, W: number, H: number, look: number) {
  const top = hy - H * 0.6, c = L.hair;
  // chỏm tóc + mái cong mềm (các lọn chĩa xuống, mép dưới uốn cong)
  const side0 = L.style === "bob" ? H * 0.32 : L.style === "old" ? -H * 0.05 : H * 0.05;
  g.beginPath(); g.moveTo(cx - W * 0.56, hy + side0);
  g.bezierCurveTo(cx - W * 0.64, top - 14, cx + W * 0.64, top - 14, cx + W * 0.56, hy + side0);
  const n = L.style === "spiky" ? 6 : L.style === "old" ? 3 : 5;
  const tipY = hy - H * (L.style === "old" ? 0.36 : 0.12), rootY = hy - H * (L.style === "old" ? 0.44 : 0.3);
  for (let i = 0; i < n; i++) {
    const x0 = cx + W * 0.54 - (i / n) * W * 1.08, x1 = cx + W * 0.54 - ((i + 1) / n) * W * 1.08, xm = (x0 + x1) / 2 + look * 8;
    const ty = tipY + (L.style === "neat" ? (i / n) * H * 0.12 - H * 0.06 : (i % 2 ? -H * 0.05 : 0));
    g.quadraticCurveTo(x0 - (x0 - x1) * 0.15, (rootY + ty) / 2, xm, ty);
    g.quadraticCurveTo(x1 + (x0 - x1) * 0.15, (rootY + ty) / 2, x1, rootY + (i === n - 1 ? H * 0.3 : 0));
  }
  g.closePath(); fillStroke(g, c, 5);
  // gai tóc trên đỉnh (spiky)
  if (L.style === "spiky") for (const [dx, dy] of [[-40, -30], [10, -44], [55, -26]]) { path(g, [[cx + dx - 26, top + 30], [cx + dx + 8, top + dy], [cx + dx + 30, top + 34]]); fillStroke(g, c, 5); }
  // ánh sáng tóc
  g.strokeStyle = "rgba(255,255,255,.45)"; g.lineWidth = 7; g.beginPath(); g.arc(cx - 10, hy - H * 0.2, W * 0.4, Math.PI * 1.15, Math.PI * 1.45); g.stroke();
  // lọn tóc hai bên (nữ)
  if (L.style === "long" || L.style === "wavy" || L.style === "bob") for (const sd of [-1, 1]) { path(g, [[cx + sd * W * 0.5, hy - H * 0.3], [cx + sd * W * 0.6, hy + H * 0.55], [cx + sd * W * 0.36, hy + H * 0.25]]); fillStroke(g, c, 4); }
  if (L.style === "pony") { g.fillStyle = "#c8202f"; g.beginPath(); g.ellipse(cx - look * 40, top + 22, 22, 12, 0.4, 0, 7); g.fill(); }
}
