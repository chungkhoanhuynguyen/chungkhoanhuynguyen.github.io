// Vietnamese street textures painted with Canvas2D: tube-house facades, shop signs, roller shutters, tiles, asphalt.
import * as THREE from "three";

export const rng = (seed: number) => { let s = seed * 9301 + 49297; return () => { s = (s * 16807) % 2147483647; return s / 2147483647; }; };
const tex = (c: HTMLCanvasElement, rep = false) => {
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4;
  if (rep) { t.wrapS = t.wrapT = THREE.RepeatWrapping; }
  return t;
};
const cv = (w: number, h: number) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return [c, c.getContext("2d")!] as const; };
const shadeHex = (hex: string, k: number) => {
  const n = parseInt(hex.slice(1), 16), f = (v: number) => Math.max(0, Math.min(255, Math.round(v * k)));
  return `rgb(${f((n >> 16) & 255)},${f((n >> 8) & 255)},${f(n & 255)})`;
};

export const WALLS = ["#f2d36b", "#9fd3c7", "#f4b6a6", "#f6efe2", "#b9d48a", "#f0a868", "#c7b8e8", "#e9e4a6"];
export const SHOPS = ["TẠP HÓA", "PHỞ BÒ", "CÀ PHÊ", "SỬA XE", "ĐIỆN THOẠI", "BÁNH MÌ", "THUỐC TÂY", "VÀNG BẠC"];
const SIGNCOL = ["#d62f2f", "#1f5fbf", "#e8b10f", "#2a8a4a", "#7a2fb0", "#f05a1a"];

/** facade of one tube house: w metres wide, floors, px per metre 96 */
export function facade(w: number, floors: number, wall: string, shop: string | null, seed: number) {
  const PX = 96, fh = 3.4, H = floors * fh + 0.6;
  const [c, g] = cv(Math.round(w * PX), Math.round(H * PX));
  const r = rng(seed), W = c.width, HH = c.height, y = (m: number) => HH - m * PX;
  g.fillStyle = wall; g.fillRect(0, 0, W, HH);
  // soft weathering streaks
  for (let i = 0; i < 14; i++) { g.fillStyle = `rgba(60,40,30,${0.03 + r() * 0.04})`; g.fillRect(r() * W, r() * HH * 0.6, 6 + r() * 20, HH * (0.2 + r() * 0.5)); }
  g.fillStyle = shadeHex(wall, 0.82); g.fillRect(0, 0, W, 0.35 * PX); // parapet band
  // upper floors: french doors with green shutters + iron balcony shadow
  for (let f = 1; f < floors; f++) {
    const base = f * fh, dw = Math.min(1.6, w * 0.42), dx = (w - dw) / 2;
    g.fillStyle = shadeHex(wall, 0.7); g.fillRect((dx - 0.12) * PX, y(base + 2.55), (dw + 0.24) * PX, 2.3 * PX);
    g.fillStyle = "#2a3a3f"; g.fillRect(dx * PX, y(base + 2.45), dw * PX, 2.2 * PX);
    // glass reflection
    g.fillStyle = "rgba(170,210,235,.55)"; g.fillRect((dx + 0.08) * PX, y(base + 2.35), (dw / 2 - 0.12) * PX, 2.0 * PX);
    g.fillStyle = "rgba(170,210,235,.35)"; g.fillRect((dx + dw / 2 + 0.04) * PX, y(base + 2.35), (dw / 2 - 0.12) * PX, 2.0 * PX);
    // shutters
    const sh = ["#2f7d5a", "#3b6fa8", "#7a5130"][Math.floor(r() * 3)];
    for (const sx of [dx - 0.55, dx + dw + 0.05]) {
      if (sx < 0.05 || sx + 0.5 > w - 0.05) continue;
      g.fillStyle = sh; g.fillRect(sx * PX, y(base + 2.45), 0.5 * PX, 2.2 * PX);
      g.strokeStyle = shadeHex(sh, 0.7); g.lineWidth = 2;
      for (let k = 0; k < 14; k++) { g.beginPath(); g.moveTo(sx * PX + 4, y(base + 2.4) + k * 15); g.lineTo(sx * PX + 0.5 * PX - 4, y(base + 2.4) + k * 15); g.stroke(); }
    }
    // small air conditioner unit
    if (r() < 0.6) { const ax = r() < 0.5 ? 0.15 : w - 0.85; g.fillStyle = "#e9ecef"; g.fillRect(ax * PX, y(base + 3.0), 0.7 * PX, 0.45 * PX); g.fillStyle = "#9aa3ab"; for (let k = 0; k < 5; k++) g.fillRect(ax * PX + 8, y(base + 2.95) + k * 7, 0.7 * PX - 16, 2); }
  }
  // ground floor: shop or house gate
  if (shop) {
    const ig = g.createLinearGradient(0, y(2.9), 0, HH); ig.addColorStop(0, "#9a7a52"); ig.addColorStop(1, "#6e5136");
    g.fillStyle = ig; g.fillRect(0.2 * PX, y(2.9), (w - 0.4) * PX, 2.9 * PX); // warm lit interior
    g.fillStyle = "#fff6d8"; g.fillRect((w / 2 - 0.5) * PX, y(2.8), 1.0 * PX, 0.05 * PX); // tube light
    g.fillStyle = "#5a3f28"; for (const sh of [0.55, 1.05, 1.55]) g.fillRect(0.35 * PX, y(sh), (w - 0.7) * PX, 0.05 * PX); // shelves
    // half-raised roller shutter
    g.fillStyle = "#b8bec6"; g.fillRect(0.2 * PX, y(2.9), (w - 0.4) * PX, 0.9 * PX);
    g.strokeStyle = "#8d949c"; g.lineWidth = 2; for (let k = 0; k < 10; k++) { g.beginPath(); g.moveTo(0.2 * PX, y(2.9) + k * 9); g.lineTo((w - 0.2) * PX, y(2.9) + k * 9); g.stroke(); }
    // goods / shelves silhouettes
    for (const sh of [0.55, 1.05, 1.55]) for (let x = 0.4; x < w - 0.5; x += 0.17 + r() * 0.08) { const hh = 0.18 + r() * 0.2; g.fillStyle = ["#e94b3c", "#f2c14e", "#4aa3df", "#6cc070", "#f08bb5", "#ffffff"][Math.floor(r() * 6)]; g.fillRect(x * PX, y(sh + hh), 0.13 * PX, hh * PX); }
  } else {
    g.fillStyle = "#4a5a5e"; g.fillRect(0.3 * PX, y(2.7), (w - 0.6) * PX, 2.7 * PX); // folding iron gate
    g.strokeStyle = "#2c3638"; g.lineWidth = 4; for (let x = 0.3; x < w - 0.3; x += 0.12) { g.beginPath(); g.moveTo(x * PX, y(2.7)); g.lineTo(x * PX, HH); g.stroke(); }
  }
  // floor slab lines
  g.fillStyle = shadeHex(wall, 0.75); for (let f = 1; f < floors; f++) g.fillRect(0, y(f * fh) - 6, W, 12);
  return tex(c);
}

/** shop sign board text */
export function sign(text: string, seed: number) {
  const [c, g] = cv(512, 128), r = rng(seed);
  const bg = SIGNCOL[Math.floor(r() * SIGNCOL.length)];
  g.fillStyle = bg; g.fillRect(0, 0, 512, 128);
  g.strokeStyle = "#ffffff"; g.lineWidth = 6; g.strokeRect(8, 8, 496, 112);
  g.fillStyle = bg === "#e8b10f" ? "#7a1010" : "#fff8e0"; g.font = "900 64px 'DejaVu Sans', Arial, sans-serif"; g.textAlign = "center"; g.textBaseline = "middle";
  g.fillText(text, 256, 64, 470);
  return tex(c);
}

export function tiles() {
  const [c, g] = cv(256, 256);
  g.fillStyle = "#c98b6a"; g.fillRect(0, 0, 256, 256);
  for (let i = 0; i < 4; i++) for (let j = 0; j < 4; j++) { g.fillStyle = (i + j) % 2 ? "#d39a78" : "#bf7f5f"; g.fillRect(i * 64 + 2, j * 64 + 2, 60, 60); }
  const t = tex(c, true); return t;
}
export function asphalt() {
  const [c, g] = cv(256, 256), r = rng(5);
  g.fillStyle = "#5b5f66"; g.fillRect(0, 0, 256, 256);
  for (let i = 0; i < 900; i++) { g.fillStyle = `rgba(${r() < 0.5 ? "30,30,35" : "150,150,155"},${0.15 + r() * 0.2})`; g.fillRect(r() * 256, r() * 256, 2, 2); }
  return tex(c, true);
}

/** price board / phone screen: VN-Index chart, green rally (t<0) or crash progress 0..1 */
export function chartCanvas(w = 512, h = 320) { return cv(w, h); }
export function drawChart(g: CanvasRenderingContext2D, w: number, h: number, crash: number, title: string) {
  g.fillStyle = "#0e1726"; g.fillRect(0, 0, w, h);
  g.fillStyle = "#e9eef5"; g.font = `800 ${Math.round(h * 0.09)}px 'DejaVu Sans', Arial`; g.textAlign = "left"; g.fillText(title, w * 0.05, h * 0.13);
  const r = rng(11), N = 60, P: number[] = []; let v = 1100;
  for (let i = 0; i < N; i++) { v *= i < 30 ? 1.011 + (r() - 0.5) * 0.02 : 0.985 + (r() - 0.5) * 0.02; P.push(v); }
  const n = Math.round(30 + 30 * Math.max(0, Math.min(1, crash))), mx = Math.max(...P), mn = Math.min(...P) * 0.98;
  const X = (i: number) => w * 0.05 + (i / N) * w * 0.9, Y = (p: number) => h * 0.92 - ((p - mn) / (mx - mn)) * h * 0.72;
  for (let i = 1; i < n; i++) { const up = P[i] >= P[i - 1]; g.fillStyle = up ? "#2bd17e" : "#ff4d5e"; g.fillRect(X(i), Math.min(Y(P[i]), Y(P[i - 1])), w * 0.011, Math.max(3, Math.abs(Y(P[i]) - Y(P[i - 1])))); }
  const last = P[n - 1];
  g.font = `900 ${Math.round(h * 0.12)}px 'DejaVu Sans', Arial`; g.textAlign = "right"; g.fillStyle = crash > 0.05 ? "#ff4d5e" : "#2bd17e";
  g.fillText(Math.round(last).toLocaleString("vi-VN"), w * 0.95, h * 0.14);
}
