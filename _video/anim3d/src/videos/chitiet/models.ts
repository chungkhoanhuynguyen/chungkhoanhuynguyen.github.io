// Nạp mô hình glTF (thư viện CC0 Poly Haven đã lọc: chỉ texture màu 512 px kiểu tranh vẽ) → vật liệu toon của set chi tiết.
// Thư mục là THAM SỐ (đường dẫn trong public/), dùng chung cho mọi bối cảnh chi tiết: putModel(g, "<set>/m", "<ten_mo_hinh>", x, y, z, ry, {h|s, rx, rz, blob}).
// Mỗi lần nạp giữ 1 delayRender → ảnh tĩnh/khung chỉ chụp khi mô hình đã vào cảnh.
import * as THREE from "three";
import { staticFile, delayRender, continueRender } from "remotion";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { tm } from "./toonmat";

const loader = new GLTFLoader();
const mcache = new Map<string, Promise<THREE.Object3D>>();
export function loadModel(dir: string, name: string) {
  const key = dir + "/" + name;
  if (!mcache.has(key)) mcache.set(key, loader.loadAsync(staticFile(`${dir}/${name}/${name}.gltf`)).then((gl) => {
    const conv = new Map<THREE.Material, THREE.Material>();
    gl.scene.traverse((o) => { const k = o as THREE.Mesh; if (!k.isMesh) return; const old = k.material as THREE.MeshStandardMaterial;
      if (!conv.has(old)) { if (old.map) old.map.colorSpace = THREE.SRGBColorSpace; conv.set(old, tm(old.color ?? "#fff", old.map ?? null, { alphaTest: old.alphaTest || (old.transparent ? 0.5 : 0), side: old.side })); }
      k.material = conv.get(old)!; k.castShadow = true; k.receiveShadow = true; });
    return gl.scene; }));
  return mcache.get(key)!;
}
export type PO = { s?: number; h?: number; rx?: number; rz?: number; blob?: number; sy?: number };
/** đặt mô hình: (x, y đáy, z) theo toạ độ nhóm g; h = chiều cao mong muốn (m) hoặc s = tỉ lệ; tự thêm bóng tiếp xúc nếu đặt sát sàn */
export function putModel(g: THREE.Group, dir: string, name: string, x: number, y: number, z: number, ry = 0, o: PO = {}, blob?: (w: number, d: number, op?: number) => THREE.Mesh) {
  const hd = delayRender("ct " + name, { timeoutInMilliseconds: 120000 });
  loadModel(dir, name).then((src) => {
    const m = src.clone(true); const w = new THREE.Group(); w.add(m); m.rotation.set(o.rx ?? 0, 0, o.rz ?? 0);
    let bb = new THREE.Box3().setFromObject(m); const sz = bb.getSize(new THREE.Vector3());
    const s = o.h ? o.h / sz.y : o.s ?? 1; m.scale.setScalar(s); if (o.sy) m.scale.y *= o.sy; bb = new THREE.Box3().setFromObject(m); const c = bb.getCenter(new THREE.Vector3());
    m.position.set(-c.x, -bb.min.y, -c.z); w.position.set(x, y, z); w.rotation.y = ry; g.add(w);
    if (blob && o.blob !== 0 && y < 0.05) { const f = bb.getSize(new THREE.Vector3()); const b = blob(f.x * 1.5 + 0.15, f.z * 1.5 + 0.15, o.blob ?? 0.55); b.position.set(x, 0.012, z); b.rotation.z = -ry; g.add(b); }
    continueRender(hd);
  }).catch((e) => { console.error("ct load fail", dir, name, e); continueRender(hd); });
}
