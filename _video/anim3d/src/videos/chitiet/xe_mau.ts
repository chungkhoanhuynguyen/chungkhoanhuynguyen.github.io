// XE MẪU CC BY 4.0 (Sketchfab) đã làm nhẹ + gỡ logo/tên hãng + biển VN giả (public/xe/*.glb, nén meshopt + webp).
// Nạp → chuẩn hoá kích thước/hướng (đầu xe +z, bánh chạm y = 0) → vật liệu: sơn phủ bóng clearcoat, kính tối, phản chiếu HDRI; viền mực tự có (InkPass).
// Ghi công tác giả: GHI_CONG trong file này (dán vào mô tả video).
import * as THREE from "three";
import { staticFile, delayRender, continueRender } from "remotion";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { MeshoptDecoder } from "three/examples/jsm/libs/meshopt_decoder.module.js";
import { applyEnv } from "./xe_sang";
import { plate } from "./xe";

export type MauKey = "goblin" | "abyss" | "neon" | "roadster" | "bike" | "spy";
type Spec = { badges?: [number, number, number, number, number, number?][]; hide?: RegExp; file: string; ten: string; len: number; ry: number; paint?: RegExp; paintCol?: string; glass?: RegExp; seat?: [number, number, number]; plateF?: [number, number, number] | null; plateR?: [number, number, number] | null; plateText?: string; moto?: boolean; tacgia: string; link: string; goc: string };
export const MAU: Record<MauKey, Spec> = {
  goblin: { hide: /car_shadow/i, file: "xe/goblin.glb", ten: "Siêu xe \"V12 Goblin\" (mẫu hư cấu)", len: 4.6, ry: 0, paint: /car_body|clearcoat/i, glass: /glass/i, plateR: null, plateF: null, tacgia: "ollitei", goc: "Fictional supercar - V12 Goblin", link: "https://sketchfab.com/3d-models/fictional-supercar-v12-goblin-0a20e49ad5774d778567cb5c3f345786" },
  abyss: { file: "xe/abyss.glb", ten: "Hypercar \"Abyss GT.7\" (mẫu hư cấu)", len: 4.7, ry: 0, paint: /CarPaint/i, glass: /^Glass$/i, plateText: "30H-999.99", tacgia: "Nyx421", goc: "Tokii Abyss GT.7 V12", link: "https://sketchfab.com/3d-models/tokii-abyss-gt7-v12-c399568541104e0e903cf138b1e24908" },
  neon: { file: "xe/neon.glb", ten: "Hypercar neon (cyberpunk, mẫu hư cấu)", len: 4.6, ry: 0, paint: /Azul/i, glass: /Vidrio/i, plateText: "51K-777.77", tacgia: "ImADefaultCube117", goc: "Cyberpunk Car HyperCar Stylized", link: "https://sketchfab.com/3d-models/cyberpunk-car-hypercar-stylized-c0d1ea5206bc4eadad4afe51577c31f6" },
  roadster: { badges: [[0, 0.51, 2.235, 0, 0.088, -0.6], [0, 0.56, -2.21, Math.PI, 0.085, -0.35], [0.9, 0.345, 1.27, Math.PI / 2, 0.055], [-0.9, 0.345, 1.27, -Math.PI / 2, 0.055], [0.9, 0.345, -1.37, Math.PI / 2, 0.055], [-0.9, 0.345, -1.37, -Math.PI / 2, 0.055]], plateF: [0, 0.3, 2.19], plateR: [0, 0.48, -2.2], file: "xe/roadster.glb", ten: "Mui trần concept (đã gỡ logo)", len: 4.4, ry: 0, paint: /^paint$/i, glass: /^glass$/i, plateText: "30E-246.80", tacgia: "Max Hordin", goc: "Sportcar concept roadster (Max Hordin)", link: "https://sketchfab.com/3d-models/sportcar-concept-chanel-roadster-by-max-hordin-41a55cde9adb45a9b54e146ea0b421d7" },
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
        return x; });
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
/** huy hiệu thay logo hãng: tròn xanh đậm viền vàng, chữ "CK HN" (Chứng Khoán Huy Nguyễn) */
let bt: THREE.Texture | null = null;
function badgeTex() { if (bt) return bt; const c = document.createElement("canvas"); c.width = c.height = 256; const x = c.getContext("2d")!; x.fillStyle = "#c9a43a"; x.beginPath(); x.arc(128, 128, 126, 0, 7); x.fill(); x.fillStyle = "#13204a"; x.beginPath(); x.arc(128, 128, 112, 0, 7); x.fill();
  x.fillStyle = "#f2d36b"; x.textAlign = "center"; x.font = "900 86px 'Be Vietnam Pro', 'DejaVu Sans'"; x.fillText("CK", 128, 120); x.font = "900 70px 'Be Vietnam Pro', 'DejaVu Sans'"; x.fillText("HN", 128, 196); bt = new THREE.CanvasTexture(c); bt.colorSpace = THREE.SRGBColorSpace; return bt; }
/** nhóm xe (nạp bất đồng bộ, giữ delayRender tới khi xong) */
export function mau(k: MauKey) {
  const g = new THREE.Group(), h = delayRender("xe " + k, { timeoutInMilliseconds: 200000 });
  load(k).then((src) => { const m = src.clone(true); g.add(m); const S = MAU[k]; const bb = new THREE.Box3().setFromObject(m), sz = bb.getSize(new THREE.Vector3());
    if (S.plateText && S.plateR !== null) { const two = !!S.moto; const pr = plate(S.plateText, two ? 0.19 : 0.52, two ? 0.14 : 0.12, two); const p = S.plateR ?? [0, sz.y * (two ? 0.55 : 0.35), bb.min.z - 0.01]; pr.position.set(...p); pr.rotation.y = Math.PI; g.add(pr);
      if (!two && S.plateF !== null) { const pf = plate(S.plateText); const q = S.plateF ?? [0, sz.y * 0.25, bb.max.z + 0.01]; pf.position.set(...q); g.add(pf); } }
    for (const [x, y, z, ry, r, rx] of S.badges ?? []) { const b = new THREE.Mesh(new THREE.CircleGeometry(r, 32), new THREE.MeshStandardMaterial({ map: badgeTex(), metalness: 0.4, roughness: 0.3, polygonOffset: true, polygonOffsetFactor: -4 })); b.position.set(x, y, z); b.rotation.set(rx ?? 0, ry, 0, "YXZ"); g.add(b); }
    g.userData.size = sz; continueRender(h); }).catch((e) => { console.error("xe mẫu lỗi", k, e); continueRender(h); });
  return g;
}
export const MAU_DS: { k: MauKey; ten: string; L: number; H: number; make: () => THREE.Group }[] = (Object.keys(MAU) as MauKey[]).map((k) => ({ k, ten: MAU[k].ten + " – " + MAU[k].tacgia + " (CC BY 4.0)", L: MAU[k].len, H: MAU[k].moto ? 1.2 : 1.25, make: () => mau(k) }));
