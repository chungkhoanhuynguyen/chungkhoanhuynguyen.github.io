// XE MẪU CC BY 4.0 (Sketchfab) đã làm nhẹ + gỡ logo/tên hãng + biển VN giả (public/xe/*.glb, nén meshopt + webp).
// Nạp → chuẩn hoá kích thước/hướng (đầu xe +z, bánh chạm y = 0) → vật liệu: sơn phủ bóng clearcoat, kính tối, phản chiếu HDRI; viền mực tự có (InkPass).
// Ghi công tác giả: GHI_CONG trong file này (dán vào mô tả video).
import * as THREE from "three";
import { staticFile, delayRender, continueRender } from "remotion";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { MeshoptDecoder } from "three/examples/jsm/libs/meshopt_decoder.module.js";
import { clone as skClone } from "three/examples/jsm/utils/SkeletonUtils.js";
import { applyEnv } from "./xe_sang";
import { plate } from "./xe";

export type MauKey = "goblin" | "abyss" | "neon" | "muitran" | "bike" | "spy";
type Spec = { recolor?: [RegExp, string, number, number][]; extra?: (g: THREE.Group) => void; hide?: RegExp; file: string; ten: string; len: number; ry: number; paint?: RegExp; paintCol?: string; glass?: RegExp; seat?: [number, number, number]; plateF?: [number, number, number] | null; plateR?: [number, number, number] | null; plateText?: string; moto?: boolean; tacgia: string; link: string; goc: string };
export const MAU: Record<MauKey, Spec> = {
  goblin: { recolor: [[/clearcoat/i, "#c4691f", 0.75, 0.28]], hide: /car_shadow/i, file: "xe/goblin.glb", ten: "Siêu xe \"V12 Goblin\" (mẫu hư cấu)", len: 4.6, ry: 0, paint: /car_body|clearcoat/i, glass: /glass/i, plateR: null, plateF: null, tacgia: "ollitei", goc: "Fictional supercar - V12 Goblin", link: "https://sketchfab.com/3d-models/fictional-supercar-v12-goblin-0a20e49ad5774d778567cb5c3f345786" },
  abyss: { file: "xe/abyss.glb", ten: "Hypercar \"Abyss GT.7\" (mẫu hư cấu)", len: 4.7, ry: 0, paint: /CarPaint/i, glass: /^Glass$/i, plateText: "30H-999.99", tacgia: "Nyx421", goc: "Tokii Abyss GT.7 V12", link: "https://sketchfab.com/3d-models/tokii-abyss-gt7-v12-c399568541104e0e903cf138b1e24908" },
  neon: { file: "xe/neon.glb", ten: "Hypercar neon (cyberpunk, mẫu hư cấu)", len: 4.6, ry: 0, paint: /Azul/i, glass: /Vidrio/i, plateText: "51K-777.77", tacgia: "ImADefaultCube117", goc: "Cyberpunk Car HyperCar Stylized", link: "https://sketchfab.com/3d-models/cyberpunk-car-hypercar-stylized-c0d1ea5206bc4eadad4afe51577c31f6" },
  muitran: { file: "xe/muitran.glb", ten: "Mui trần (cắt mui từ hypercar neon)", len: 4.6, ry: 0, paint: /Azul/i, glass: /Vidrio/i, plateText: "30E-246.80", plateF: [0, 0.3, 2.27], plateR: [0, 0.5, -2.3], extra: (g) => cockpit(g), tacgia: "ImADefaultCube117", goc: "Cyberpunk Car HyperCar Stylized", link: "https://sketchfab.com/3d-models/cyberpunk-car-hypercar-stylized-c0d1ea5206bc4eadad4afe51577c31f6" },
  bike: { file: "xe/bike.glb", ten: "Mô tô sport concept", len: 2.1, ry: 0, paint: /^Main$/i, moto: true, plateR: [0, 0.58, -0.86], plateText: "29-A1 999.99", tacgia: "3DHorse", goc: "Free Concept Sport Bike", link: "https://sketchfab.com/3d-models/free-concept-sport-bike-57b48aa4e3e441868123f47a7145fe87" },
  spy: { file: "xe/spy.glb", ten: "Siêu mô tô \"SPY\" (đã xoá chữ lốp)", len: 2.1, ry: 0, moto: true, plateR: [0, 0.6, -0.86], plateText: "29-A2 868.68", tacgia: "Amvall", goc: "SPY-HYPERSPORT", link: "https://sketchfab.com/3d-models/spy-hypersport-158b48d550144451a59731720f63650a" },
};
const loader = new GLTFLoader(); loader.setMeshoptDecoder(MeshoptDecoder);
const cache = new Map<string, Promise<THREE.Object3D>>();
function load(k: MauKey) {
  if (!cache.has(k)) cache.set(k, loader.loadAsync(staticFile(MAU[k].file)).then((gl) => { const S = MAU[k], root = gl.scene;
    const drop: THREE.Object3D[] = []; root.traverse((o) => { const m = o as THREE.Mesh; if (!m.isMesh) return; if (S.hide && [m.material].flat().some((x) => S.hide!.test((x as THREE.Material).name ?? ""))) { drop.push(m); return; } m.castShadow = true; m.receiveShadow = true;
      const mats = (Array.isArray(m.material) ? m.material : [m.material]) as THREE.MeshStandardMaterial[];
      const nm = mats.map((x) => { const nmn = x.name ?? "";
        if (S.glass?.test(nmn)) { const g = new THREE.MeshPhysicalMaterial({ color: "#0b0f15", metalness: 0.1, roughness: 0.05, transparent: true, opacity: 0.82, clearcoat: 1 }); g.name = nmn; return g; }
        if (S.paint?.test(nmn) && !(x as THREE.MeshPhysicalMaterial).isMeshPhysicalMaterial) { const p = new THREE.MeshPhysicalMaterial(); THREE.MeshStandardMaterial.prototype.copy.call(p, x); p.clearcoat = 1; p.clearcoatRoughness = 0.04; p.roughness = Math.min(p.roughness, 0.35); p.name = nmn; return p; }
        return x; }).map((x) => { for (const [re, col, met, rou] of S.recolor ?? []) if (re.test(x.name ?? "")) { const p = x as THREE.MeshPhysicalMaterial; p.color.set(col); p.metalness = met; p.roughness = rou; if (p.isMeshPhysicalMaterial) { p.clearcoat = 1; p.clearcoatRoughness = 0.03; } } return x; });
      m.material = Array.isArray(m.material) ? nm : nm[0]; for (const x of nm) applyEnv(x as THREE.MeshStandardMaterial); });
    for (const d of drop) d.removeFromParent();
    // chuẩn hoá: trục dài nằm ngang → z, chiều dài = len, đáy chạm 0
    const w = new THREE.Group(); w.add(root); let bb = new THREE.Box3().setFromObject(root); let sz = bb.getSize(new THREE.Vector3());
    if (sz.x > sz.z) { root.rotation.y = Math.PI / 2; bb = new THREE.Box3().setFromObject(root); sz = bb.getSize(new THREE.Vector3()); }
    root.rotation.y += S.ry; bb = new THREE.Box3().setFromObject(root); sz = bb.getSize(new THREE.Vector3());
    const s = S.len / sz.z; root.scale.multiplyScalar(s); bb = new THREE.Box3().setFromObject(root); const c = bb.getCenter(new THREE.Vector3()); root.position.sub(new THREE.Vector3(c.x, bb.min.y, c.z));
    return w; }));
  return cache.get(k)!;
}
/** khoang lái mui trần (toạ độ sau chuẩn hoá, xe dài 4.6 m): viền mép cắt màu thân, kính chắn gió thấp có khung, 2 ghế, vô-lăng, taplô.
 *  Ghế lái bên trái (+x). Chỗ ngồi/vô-lăng xuất ở MUITRAN_SEAT / MUITRAN_WHEEL để đặt người + tay. */
export const MUITRAN_SEAT: [number, number, number] = [0.36, 0.36, -0.38], MUITRAN_WHEEL: [number, number, number] = [0.36, 0.74, 0.3];
function cockpit(g: THREE.Group) {
  const body = new THREE.MeshPhysicalMaterial({ color: "#b3131c", metalness: 0.5, roughness: 0.3, clearcoat: 1 }); applyEnv(body);
  const dark = new THREE.MeshStandardMaterial({ color: "#16171b", roughness: 0.6 }), leather = new THREE.MeshStandardMaterial({ color: "#2a2b30", roughness: 0.55 }), stitch = new THREE.MeshStandardMaterial({ color: "#d8212f", roughness: 0.4 });
  const M = (geo: THREE.BufferGeometry, m: THREE.Material, x: number, y: number, z: number) => { const k = new THREE.Mesh(geo, m); k.position.set(x, y, z); k.castShadow = true; k.receiveShadow = true; g.add(k); return k; };
  // viền mép cắt: ống bo tròn quanh khoang (che mép thân bị hở)
  const sh = new THREE.Shape(); const W = 0.8, z0 = -1.02, z1 = 0.78, r = 0.32; sh.moveTo(-W + r, z0); sh.lineTo(W - r, z0); sh.quadraticCurveTo(W, z0, W, z0 + r); sh.lineTo(W, z1 - r); sh.quadraticCurveTo(W, z1, W - r, z1); sh.lineTo(-W + r, z1); sh.quadraticCurveTo(-W, z1, -W, z1 - r); sh.lineTo(-W, z0 + r); sh.quadraticCurveTo(-W, z0, -W + r, z0);
  const pts = sh.getSpacedPoints(80).map((p) => new THREE.Vector3(p.x, 0.92 + (p.y > 0.4 ? -0.06 * (p.y - 0.4) : 0), -p.y));
  M(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts, true), 160, 0.045, 10, true), body, 0, 0, 0);
  // sàn + bồn khoang tối (che lỗ nhìn xuống gầm)
  const tub = M(new THREE.BoxGeometry(1.5, 0.5, 1.75), dark, 0, 0.52, -0.12); tub.scale.set(1, 1, 1);
  // ghế thể thao: đệm, tựa cao, gối đầu, chỉ đỏ
  for (const sx of [-1, 1]) { const x = sx * 0.36; M(new THREE.BoxGeometry(0.46, 0.12, 0.5), leather, x, 0.38, -0.38); const bk = M(new THREE.BoxGeometry(0.46, 0.62, 0.12), leather, x, 0.66, -0.66); bk.rotation.x = -0.28;
    M(new THREE.BoxGeometry(0.3, 0.2, 0.1), leather, x, 1.04, -0.78).rotation.x = -0.28; M(new THREE.BoxGeometry(0.03, 0.6, 0.125), stitch, x, 0.66, -0.66).rotation.x = -0.28;
    for (const w of [-1, 1]) M(new THREE.BoxGeometry(0.06, 0.4, 0.14), leather, x + w * 0.22, 0.6, -0.62).rotation.x = -0.28; }
  // taplô + vô-lăng (đáy phẳng) + đồng hồ
  M(new THREE.BoxGeometry(1.5, 0.18, 0.32), dark, 0, 0.78, 0.52); const scr = M(new THREE.PlaneGeometry(0.34, 0.1), new THREE.MeshBasicMaterial({ color: new THREE.Color(0.4, 1.2, 2.2) }), 0.36, 0.84, 0.355); scr.rotation.x = -0.5;
  const sw = M(new THREE.TorusGeometry(0.17, 0.026, 10, 28), dark, ...MUITRAN_WHEEL); sw.rotation.x = -0.45; M(new THREE.CylinderGeometry(0.035, 0.035, 0.22, 10), dark, 0.36, 0.78, 0.4).rotation.x = Math.PI / 2 - 0.45;
  for (const a of [0, 2.1, -2.1]) { const sp = M(new THREE.BoxGeometry(0.02, 0.17, 0.02), dark, 0.36 + Math.sin(a) * 0.08, 0.74 - Math.cos(a) * 0.075, 0.3 - Math.cos(a) * 0.035); sp.rotation.set(-0.45, 0, -a); }
  // kính chắn gió thấp: khung + kính khói, nghiêng về sau
  const ws = new THREE.Group(); ws.position.set(0, 0.9, 0.86); ws.rotation.x = -0.75; g.add(ws);
  const glassM = new THREE.MeshPhysicalMaterial({ color: "#0d1520", metalness: 0.1, roughness: 0.05, transparent: true, opacity: 0.55, clearcoat: 1 }); applyEnv(glassM);
  const gl = new THREE.Mesh(new THREE.PlaneGeometry(1.5, 0.34), glassM); gl.position.y = 0.17; ws.add(gl);
  for (const [w, h, x, y] of [[1.56, 0.04, 0, 0.34], [0.04, 0.36, -0.77, 0.17], [0.04, 0.36, 0.77, 0.17]] as number[][]) { const f = new THREE.Mesh(new THREE.BoxGeometry(w, h, 0.04), dark); f.position.set(x, y, 0); f.castShadow = true; ws.add(f); }
  // 2 thanh chống lật sau ghế
  for (const sx of [-1, 1]) { const hoop = M(new THREE.TorusGeometry(0.17, 0.03, 8, 16, Math.PI), new THREE.MeshPhysicalMaterial({ color: "#c9cdd3", metalness: 1, roughness: 0.2 }), sx * 0.36, 0.95, -0.95); hoop.rotation.y = Math.PI / 2; applyEnv(hoop.material as THREE.MeshStandardMaterial); }
}
/** nhóm xe (nạp bất đồng bộ, giữ delayRender tới khi xong) */
export function mau(k: MauKey) {
  const g = new THREE.Group(), h = delayRender("xe " + k, { timeoutInMilliseconds: 200000 });
  g.userData.ready = load(k).then((src) => { const m = skClone(src); /* SkeletonUtils: mẫu có SkinnedMesh (Abyss) phải nối lại xương của bản sao, nếu không xe bỏ qua phép đặt/xoay → sai chỗ, xuyên xe khác */ g.add(m); const S = MAU[k]; const bb = new THREE.Box3().setFromObject(m), sz = bb.getSize(new THREE.Vector3());
    if (S.plateText && S.plateR !== null) { const two = !!S.moto; const pr = plate(S.plateText, two ? 0.19 : 0.52, two ? 0.14 : 0.12, two); const p = S.plateR ?? [0, sz.y * (two ? 0.55 : 0.35), bb.min.z - 0.01]; pr.position.set(...p); pr.rotation.y = Math.PI; g.add(pr);
      if (!two && S.plateF !== null) { const pf = plate(S.plateText); const q = S.plateF ?? [0, sz.y * 0.25, bb.max.z + 0.01]; pf.position.set(...q); g.add(pf); } }
    S.extra?.(g);
    g.userData.size = sz; continueRender(h); }).catch((e) => { console.error("xe mẫu lỗi " + k + " " + String(e) + " " + (e as Error).stack); continueRender(h); });
  return g;
}
export const MAU_DS: { k: MauKey; ten: string; L: number; H: number; make: () => THREE.Group }[] = (Object.keys(MAU) as MauKey[]).map((k) => ({ k, ten: MAU[k].ten + " – " + MAU[k].tacgia + " (CC BY 4.0)", L: MAU[k].len, H: MAU[k].moto ? 1.2 : 1.25, make: () => mau(k) }));

// ---------- đặt nhiều xe KHÔNG đè nhau ----------
/** Đợi các xe nạp xong rồi kiểm hộp bao thật (sau scale/xoay) + khoảng cách tối thiểu `gap` (m) trên mặt sàn.
 *  Giao nhau → console.error "VA CHẠM" và đẩy xe sau ra xa dọc đường nối tâm cho tới khi đủ khoảng cách.
 *  people: điểm đứng của người (x, z) – báo lỗi nếu nằm trong hộp xe nới thêm 0.3 m. Trả về Promise (đã giữ delayRender). */
export function khongDe(root: THREE.Object3D, cars: THREE.Object3D[], gap = 0.8, people: [number, number][] = []) {
  const h = delayRender("kiem va cham");
  const box = (o: THREE.Object3D) => { root.updateWorldMatrix(true, true); const b = new THREE.Box3().setFromObject(o, true); b.min.y = -1e3; b.max.y = 1e3; return b; };
  return Promise.all(cars.map((c) => c.userData.ready ?? Promise.resolve())).then(() => {
    for (let i = 0; i < cars.length; i++) for (let j = 0; j < i; j++) { let tries = 0;
      while (tries++ < 50) { const a = box(cars[j]).expandByScalar(gap / 2), b = box(cars[i]).expandByScalar(gap / 2); if (!a.intersectsBox(b)) break;
        if (tries === 1) console.error(`VA CHẠM: xe ${i} đè xe ${j} – tự đẩy ra`);
        const d = b.getCenter(new THREE.Vector3()).sub(a.getCenter(new THREE.Vector3())); d.y = 0; if (d.lengthSq() < 1e-6) d.set(1, 0, 0); d.normalize().multiplyScalar(0.25);
        const p = cars[i].parent!; const w = cars[i].getWorldPosition(new THREE.Vector3()).add(d); cars[i].position.copy(p.worldToLocal(w)); } }
    for (const [x, z] of people) for (let i = 0; i < cars.length; i++) { const b = box(cars[i]).expandByScalar(0.3); if (b.containsPoint(new THREE.Vector3(x, 0, z))) console.error(`VA CHẠM: người tại (${x}, ${z}) đứng trong xe ${i}`); }
    continueRender(h); }).catch((e) => { console.error(e); continueRender(h); });
}
