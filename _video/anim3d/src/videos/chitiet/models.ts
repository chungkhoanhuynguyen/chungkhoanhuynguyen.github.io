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

import { mergeGeometries } from "three/examples/jsm/utils/BufferGeometryUtils.js";
/** GỘP lưới tĩnh của bối cảnh theo vật liệu (swiftshader chậm vì SỐ LỆNH VẼ: mỗi khung vẽ cảnh 3 lần – bóng, viền mực, màu).
 *  Chỉ gộp Mesh thường, cùng vật liệu + cùng cờ đổ bóng + cùng lớp; bỏ qua vật có userData.tick/noMerge, Points/Line, InstancedMesh, SkinnedMesh. Gọi sau khi dựng xong phần đồng bộ của set. */
export function gopTinh(root: THREE.Group) {
  root.updateMatrixWorld(true); const inv = new THREE.Matrix4().copy(root.matrixWorld).invert();
  const groups = new Map<string, { m: THREE.Material; cast: boolean; layers: number; geos: THREE.BufferGeometry[]; src: THREE.Mesh[] }>();
  root.traverse((o) => { const k = o as THREE.Mesh; if (!k.isMesh || (k as unknown as THREE.SkinnedMesh).isSkinnedMesh || (k as unknown as THREE.InstancedMesh).isInstancedMesh || Array.isArray(k.material)) return;
    let p: THREE.Object3D | null = k; while (p && p !== root) { if (p.userData.tick || p.userData.noMerge) return; p = p.parent; }
    const mat = k.material as THREE.Material; if ((mat as THREE.MeshBasicMaterial).transparent) return;
    const key = mat.uuid + "|" + k.castShadow + "|" + k.layers.mask + "|" + k.renderOrder; let G = groups.get(key); if (!G) { G = { m: mat, cast: k.castShadow, layers: k.layers.mask, geos: [], src: [] }; groups.set(key, G); }
    let geo = k.geometry.index ? k.geometry.toNonIndexed() : k.geometry.clone(); for (const n of Object.keys(geo.attributes)) if (!["position", "normal", "uv"].includes(n)) geo.deleteAttribute(n);
    if (!geo.attributes.normal) geo.computeVertexNormals(); if (!geo.attributes.uv) geo.setAttribute("uv", new THREE.Float32BufferAttribute(new Float32Array(geo.attributes.position.count * 2), 2));
    geo.applyMatrix4(new THREE.Matrix4().multiplyMatrices(inv, k.matrixWorld)); G.geos.push(geo); G.src.push(k); });
  let n0 = 0, n1 = 0;
  for (const G of groups.values()) { n0 += G.src.length; if (G.src.length < 2) { n1 += G.src.length; continue; }
    const mg = mergeGeometries(G.geos, false); if (!mg) { n1 += G.src.length; continue; }
    for (const s of G.src) s.removeFromParent(); const m = new THREE.Mesh(mg, G.m); m.castShadow = G.cast; m.receiveShadow = true; m.layers.mask = G.layers; root.add(m); n1++; }
  root.userData.gop = `${n0} → ${n1}`; return root;
}
