// A Vietnamese street (tube houses, shop signs, power-line tangles, motorbikes, plastic stools) in the toon style.
import * as THREE from "three";
import { facade, sign, tiles, asphalt, WALLS, SHOPS, rng, chartCanvas, drawChart } from "./paint";
import { twoTone, TONE } from "./shade";
import { LIGHTS } from "./lights";
import { NOINK } from "./ink";
import { Actor, TUAN, ME, KHACH, CHI } from "./cast";

const lam = (c: THREE.ColorRepresentation, map?: THREE.Texture) => twoTone(new THREE.MeshLambertMaterial({ color: c, map: map ?? null }));
const box = (w: number, h: number, d: number, m: THREE.Material) => { const b = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), m); b.castShadow = b.receiveShadow = true; return b; };
const cyl = (r1: number, r2: number, h: number, m: THREE.Material, s = 16) => { const b = new THREE.Mesh(new THREE.CylinderGeometry(r1, r2, h, s), m); b.castShadow = b.receiveShadow = true; return b; };

function house(x: number, side: 1 | -1, w: number, floors: number, seed: number, shop: string | null) {
  const r = rng(seed), g = new THREE.Group(), fh = 3.4, H = floors * fh + 0.6, D = 14, o = -side;
  const wall = WALLS[Math.floor(r() * WALLS.length)];
  const plain = lam(wall), front = lam("#ffffff", facade(w, floors, wall, shop, seed));
  const mats = [plain, plain, plain, plain, side === -1 ? front : plain, side === 1 ? front : plain];
  const b = new THREE.Mesh(new THREE.BoxGeometry(w, H, D), mats); b.castShadow = b.receiveShadow = true;
  b.position.set(0, H / 2, side * D / 2); g.add(b);
  // balconies with railings and pots
  const slab = lam("#e8e2d6"), rail = lam("#2b2f33"), pot = lam("#b5562e"), leaf = lam("#3f9a4a");
  for (let f = 1; f < floors; f++) {
    const s = box(w - 0.2, 0.18, 1.0, slab); s.position.set(0, f * fh, o * 0.5); g.add(s);
    const rl = box(w - 0.3, 0.06, 0.06, rail); rl.position.set(0, f * fh + 1.0, o * 0.97); g.add(rl);
    for (let x = -w / 2 + 0.25; x < w / 2 - 0.2; x += 0.22) { const p = box(0.035, 1.0, 0.035, rail); p.position.set(x, f * fh + 0.5, o * 0.97); g.add(p); }
    if (r() < 0.7) for (let k = 0; k < 2; k++) { const pp = cyl(0.17, 0.12, 0.28, pot, 10); pp.position.set(-w / 2 + 0.5 + r() * (w - 1), f * fh + 0.23, o * 0.6); g.add(pp);
      const lf = new THREE.Mesh(new THREE.IcosahedronGeometry(0.32, 0), leaf); lf.position.set(pp.position.x, pp.position.y + 0.38, pp.position.z); lf.castShadow = true; g.add(lf); }
  }
  // shop: sign board + awning
  if (shop) {
    const sg = new THREE.Mesh(new THREE.BoxGeometry(w - 0.3, 0.8, 0.1), [rail, rail, rail, rail, side === -1 ? lam("#fff", sign(shop, seed)) : rail, side === 1 ? lam("#fff", sign(shop, seed)) : rail]);
    sg.position.set(0, 3.25, o * 0.08); g.add(sg);
    const aw = box(w, 0.05, 1.6, lam(["#d9342b", "#2f7fd0", "#f1b51c", "#2b9a5a"][Math.floor(r() * 4)])); aw.position.set(0, 2.85, o * 0.8); aw.rotation.x = o * 0.22; g.add(aw);
  }
  // roof: water tank + antenna
  const inox = lam("#d9dde2"); const tank = cyl(0.45, 0.45, 1.3, inox); tank.rotation.z = Math.PI / 2; tank.position.set(-w / 2 + 0.9 + r() * (w - 1.8), H + 0.6, side * 5); g.add(tank);
  const leg = box(1.2, 0.5, 0.8, lam("#7a7f86")); leg.position.set(tank.position.x, H + 0.1, tank.position.z); g.add(leg);
  g.position.set(x, 0, side * 7);
  return g;
}

function motorbike(col: string) {
  const g = new THREE.Group(), blk = lam("#1d1d22"), body = lam(col), chrome = lam("#c9cdd3"), seat = lam("#2a2324");
  for (const z of [-0.62, 0.62]) { const w = new THREE.Mesh(new THREE.TorusGeometry(0.24, 0.06, 8, 20), blk); w.rotation.y = Math.PI / 2; w.position.set(0, 0.33, z); w.castShadow = true; g.add(w); }
  const b1 = box(0.32, 0.38, 0.9, body); b1.position.set(0, 0.62, -0.25); g.add(b1);
  const b2 = box(0.3, 0.16, 0.75, seat); b2.position.set(0, 0.88, -0.28); g.add(b2);
  const fr = box(0.26, 0.6, 0.18, body); fr.position.set(0, 0.68, 0.45); fr.rotation.x = -0.35; g.add(fr);
  const hb = box(0.7, 0.05, 0.05, chrome); hb.position.set(0, 1.05, 0.55); g.add(hb);
  const lamp = box(0.18, 0.14, 0.1, lam("#fff2c0")); lamp.position.set(0, 0.98, 0.64); g.add(lamp);
  const ex = cyl(0.05, 0.05, 0.7, chrome, 8); ex.rotation.x = Math.PI / 2; ex.position.set(0.2, 0.35, -0.45); g.add(ex);
  return g;
}

function stool(col: string) {
  const g = new THREE.Group(), m = lam(col);
  const top = cyl(0.17, 0.17, 0.04, m, 12); top.position.y = 0.42; g.add(top);
  const leg = cyl(0.15, 0.19, 0.38, m, 4); leg.position.y = 0.2; g.add(leg);
  return g;
}

export const SKY = { day: ["#4f8fd8", "#bcd6ef"], golden: ["#6a4f8c", "#ffcf8f"] };

export class World {
  root = new THREE.Group();
  sun = new THREE.DirectionalLight("#ffffff", 2.5);
  hemi = new THREE.HemisphereLight("#dcecff", "#b49a78", 0.5);
  skyMat: THREE.ShaderMaterial;
  tuan = new Actor(TUAN, 1.72, 3);
  me = new Actor(ME, 1.55, 7);
  khach = new Actor(KHACH, 1.7, 5);
  chi = new Actor(CHI, 1.6, 9);
  bikeT: THREE.Group;
  tv: { c: HTMLCanvasElement; g: CanvasRenderingContext2D; t: THREE.CanvasTexture; mesh: THREE.Mesh };
  phone: { c: HTMLCanvasElement; g: CanvasRenderingContext2D; t: THREE.CanvasTexture; mesh: THREE.Group };
  constructor() {
    const R = this.root, r = rng(42);
    // sky dome
    this.skyMat = new THREE.ShaderMaterial({ side: THREE.BackSide, depthWrite: false, uniforms: { top: { value: new THREE.Color(SKY.day[0]) }, hor: { value: new THREE.Color(SKY.day[1]) } },
      vertexShader: "varying vec3 p; void main(){ p = normalize(position); gl_Position = projectionMatrix*modelViewMatrix*vec4(position,1.0);}",
      fragmentShader: "uniform vec3 top; uniform vec3 hor; varying vec3 p; void main(){ float t = smoothstep(-0.05, 0.6, p.y); gl_FragColor = vec4(mix(hor, top, t), 1.0); }" });
    const sky = new THREE.Mesh(new THREE.SphereGeometry(400, 32, 16), this.skyMat); sky.layers.set(NOINK); R.add(sky);
    // ground
    const road = new THREE.Mesh(new THREE.PlaneGeometry(260, 8), lam("#ffffff", asphalt())); road.rotation.x = -Math.PI / 2; road.receiveShadow = true;
    ((road.material as THREE.MeshLambertMaterial).map as THREE.Texture).repeat.set(60, 2); R.add(road);
    const lane = new THREE.Mesh(new THREE.PlaneGeometry(260, 0.12), lam("#f2efe6")); lane.rotation.x = -Math.PI / 2; lane.position.y = 0.01; R.add(lane);
    for (const s of [1, -1]) {
      const sw = new THREE.Mesh(new THREE.BoxGeometry(260, 0.15, 3), lam("#ffffff", tiles())); sw.position.set(0, 0.075, s * 5.5); sw.receiveShadow = true;
      ((sw.material as THREE.MeshLambertMaterial).map as THREE.Texture).repeat.set(130, 1.5); R.add(sw);
      const curb = box(260, 0.17, 0.18, lam("#d8d3c8")); curb.position.set(0, 0.085, s * 4.05); R.add(curb);
      // tube houses
      let x = -60;
      let i = 0;
      while (x < 60) { const w = 3.6 + r() * 1.6, fl = 3 + Math.floor(r() * 3); const shop = r() < 0.7 ? SHOPS[(i * 3 + (s > 0 ? 1 : 0)) % SHOPS.length] : null;
        const h = house(x + w / 2, s as 1 | -1, w, fl, 100 + i * 7 + (s > 0 ? 1 : 0), shop); R.add(h); x += w + 0.02; i++; }
      // poles + tangled power lines
      const poleM = lam("#b9b4aa"), wireM = new THREE.LineBasicMaterial({ color: "#151515" });
      const poles: THREE.Vector3[] = [];
      for (let px = -49; px <= 49; px += 14) { const p = cyl(0.13, 0.2, 9.5, poleM, 8); p.position.set(px, 4.75, s * 4.4); R.add(p);
        const arm = box(1.4, 0.12, 0.12, poleM); arm.position.set(px, 8.6, s * 4.4); arm.rotation.y = Math.PI / 2; R.add(arm);
        for (let k = 0; k < 3; k++) { const bx = box(0.35, 0.45, 0.25, lam("#8d9196")); bx.position.set(px, 6.2 - k * 0.6, s * 4.25); R.add(bx); }
        poles.push(new THREE.Vector3(px, 8.4, s * 4.4)); }
      for (let k = 0; k < poles.length - 1; k++) for (let wI = 0; wI < 7; wI++) {
        const a = poles[k].clone().add(new THREE.Vector3(0, -wI * 0.35 - r() * 0.3, (r() - 0.5) * 0.9)), b = poles[k + 1].clone().add(new THREE.Vector3(0, -wI * 0.35 - r() * 0.3, (r() - 0.5) * 0.9));
        const pts: THREE.Vector3[] = []; const sag = 0.6 + r() * 1.2;
        for (let t = 0; t <= 20; t++) { const u = t / 20; pts.push(new THREE.Vector3().lerpVectors(a, b, u).add(new THREE.Vector3(0, -sag * 4 * u * (1 - u), 0))); }
        const ln = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), wireM); ln.layers.set(NOINK); R.add(ln);
      }
      // trees
      const trunk = lam("#7a5638"), leaves = [lam("#4f9e3f"), lam("#3d8a3a"), lam("#6bb04a")];
      for (let tx = -52; tx <= 52; tx += 21) { const t = cyl(0.18, 0.26, 4.2, trunk, 8); t.position.set(tx + s * 3, 2.1, s * 4.7); R.add(t);
        for (let k = 0; k < 4; k++) { const c = new THREE.Mesh(new THREE.IcosahedronGeometry(1.4 + r() * 0.6, 1), leaves[k % 3]); c.position.set(tx + s * 3 + (r() - 0.5) * 2.2, 4.6 + r() * 1.4, s * 4.7 + (r() - 0.5) * 1.6); c.castShadow = true; R.add(c); } }
      // parked motorbikes on the sidewalk
      for (let k = 0; k < 9; k++) { const m = motorbike(["#c0392b", "#2c3e50", "#ecf0f1", "#2980b9", "#16a085", "#8e44ad"][Math.floor(r() * 6)]); m.position.set(-40 + k * 9 + r() * 3, 0.15, s * 5.2); m.rotation.y = Math.PI / 2 + (r() - 0.5) * 0.4; R.add(m); }
    }
    // café corner: plastic stools + low table near x=0 north side
    const tbl = box(0.7, 0.04, 0.7, lam("#cfd6dc")); tbl.position.set(1.2, 0.62, 5.3); R.add(tbl);
    const tl = cyl(0.04, 0.04, 0.45, lam("#9aa1a8"), 6); tl.position.set(1.2, 0.38, 5.3); R.add(tl);
    for (const [dx, dz, c] of [[-0.6, 0, "#d93636"], [0.6, 0.1, "#2f6fd1"], [0, 0.65, "#d93636"]] as const) { const st = stool(c); st.position.set(1.2 + dx, 0.15, 5.3 + dz); R.add(st); }
    // TV on the café wall showing the board
    const [tc, tg] = chartCanvas(640, 400); const tt = new THREE.CanvasTexture(tc); tt.colorSpace = THREE.SRGBColorSpace;
    const tvm = new THREE.Mesh(new THREE.BoxGeometry(1.9, 1.2, 0.08), [lam("#111"), lam("#111"), lam("#111"), lam("#111"), new THREE.MeshBasicMaterial({ map: tt }), lam("#111")]);
    tvm.position.set(2.6, 2.1, 7.0 - 0.06); tvm.rotation.y = Math.PI; R.add(tvm);
    this.tv = { c: tc, g: tg, t: tt, mesh: tvm };
    // Tuấn's own motorbike (to be sold)
    this.bikeT = motorbike("#c0392b"); this.bikeT.position.set(-3.2, 0.15, 5.0); this.bikeT.rotation.y = Math.PI / 2; R.add(this.bikeT);
    // phone prop for inserts
    const [pc, pg] = chartCanvas(360, 720); const pt = new THREE.CanvasTexture(pc); pt.colorSpace = THREE.SRGBColorSpace;
    const ph = new THREE.Group(); const body = box(0.42, 0.84, 0.04, lam("#16181d")); ph.add(body);
    const scr = new THREE.Mesh(new THREE.PlaneGeometry(0.38, 0.76), new THREE.MeshBasicMaterial({ map: pt })); scr.position.z = 0.021; scr.layers.set(NOINK); ph.add(scr);
    
    R.add(ph); ph.visible = false;
    this.phone = { c: pc, g: pg, t: pt, mesh: ph };
    // actors
    for (const a of [this.tuan, this.me, this.khach, this.chi]) { R.add(a.root); a.root.visible = false; }
    // lights
    this.sun.castShadow = true; this.sun.shadow.mapSize.set(2048, 2048);
    const sc = this.sun.shadow.camera as THREE.OrthographicCamera; sc.left = -30; sc.right = 30; sc.top = 30; sc.bottom = -30; sc.near = 1; sc.far = 200;
    this.sun.shadow.bias = -0.0004; this.sun.shadow.normalBias = 0.02;
    R.add(this.sun, this.sun.target, this.hemi);
  }
  setLight(light: "day" | "golden", camPos: THREE.Vector3) {
    const L = LIGHTS[light];
    TONE.uLitCol.value.set(...L.lit); TONE.uShadeCol.value.set(...L.shade); TONE.uShadeLift.value.set(...L.lift);
    TONE.uLambert.value = L.lambert; TONE.uSideK.value = L.sideK; TONE.uTerm.value = L.term; TONE.uSat.value = light === "day" ? 1.08 : 1.0;
    // world-fixed sun from the north (road side of the south row) so the facades we film are lit
    const off = light === "day" ? new THREE.Vector3(22, 55, -40) : new THREE.Vector3(-45, 16, -40);
    this.sun.position.set(camPos.x + off.x, off.y, camPos.z + off.z);
    this.sun.target.position.set(camPos.x, 0, camPos.z);
    this.sun.color.set(L.sunCol); this.sun.intensity = L.sunI;
    const S = SKY[light]; (this.skyMat.uniforms.top.value as THREE.Color).set(S[0]); (this.skyMat.uniforms.hor.value as THREE.Color).set(S[1]);
  }
}
