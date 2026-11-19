// Làm nhẹ + gỡ logo/tên hãng + biển VN cho các mẫu xe CC BY 4.0 (Sketchfab)
import { NodeIO } from "@gltf-transform/core"; import { ALL_EXTENSIONS } from "@gltf-transform/extensions";
import { dedup, prune, weld, simplify, textureCompress, metalRough, meshopt, resample, flatten, join } from "@gltf-transform/functions";
import { MeshoptSimplifier, MeshoptEncoder } from "meshoptimizer"; import sharp from "sharp"; import fs from "node:fs";
await MeshoptSimplifier.ready; await MeshoptEncoder.ready;
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({ "meshopt.encoder": MeshoptEncoder });
const [src, out, key] = process.argv.slice(2); const doc = await io.read(src); const R = doc.getRoot();
const tris = () => R.listMeshes().reduce((a, m) => a + m.listPrimitives().reduce((b, p) => b + (p.getIndices()?.getCount() ?? p.getAttribute("POSITION").getCount()) / 3, 0), 0);
const killNode = (name) => { for (const n of R.listNodes()) if (n.getName() === name) { n.dispose(); console.log("  gỡ", name); } };
const setTex = (i, file) => { const t = R.listTextures()[i]; t.setImage(fs.readFileSync(file)).setMimeType("image/png"); console.log("  thay texture", i); };
console.log(key, "tris trước", Math.round(tris()));
if (key === "goblin") { setTex(3, "edit/goblin_3.png"); await doc.transform(metalRough()); }
if (key === "abyss") for (const n of R.listNodes()) if (n.getMesh()?.listPrimitives().some((p) => p.getMaterial()?.getName() === "StickerLabels")) { console.log("  gỡ nhãn dán", n.getName()); n.dispose(); }
if (key === "roadster") { for (const k of ["Object_7", "Object_13", "Object_44", "Object_54", "Object_20"]) killNode(k); for (const m of R.listMaterials()) if (m.getName() === "gold_ish") { m.setBaseColorFactor([0.09, 0.09, 0.1, 1]).setMetallicFactor(1).setRoughnessFactor(0.28); console.log("  vàng → graphite"); } }
if (key === "spy") { setTex(22, "edit/spy_22.png"); setTex(23, "edit/spy_23.png"); setTex(24, "edit/spy_24.png"); }
await doc.transform(dedup(), prune(), resample(), weld({ tolerance: 0.0001 }));
const t0 = tris(); if (t0 > 350000) await doc.transform(simplify({ simplifier: MeshoptSimplifier, ratio: 350000 / t0, error: 0.0008, lockBorder: true }));
await doc.transform(prune(), textureCompress({ encoder: sharp, targetFormat: "webp", resize: [2048, 2048], quality: 82 }), meshopt({ encoder: MeshoptEncoder, level: "medium" }));
console.log("  tris sau", Math.round(tris())); await io.write(out, doc); console.log("  MB", (fs.statSync(out).size / 1e6).toFixed(2));
