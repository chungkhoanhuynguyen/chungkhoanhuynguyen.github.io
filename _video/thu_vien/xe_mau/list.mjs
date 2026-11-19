import { NodeIO } from "@gltf-transform/core";
import { ALL_EXTENSIONS } from "@gltf-transform/extensions";
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(process.argv[2]); const r = doc.getRoot();
const tex = r.listTextures().map((t, i) => `${i}:${t.getName() || t.getURI()}(${t.getMimeType()} ${t.getSize()?.join("x")})`);
console.log("TEX", tex.join(" | "));
console.log("MAT", r.listMaterials().map((m) => m.getName()).join(" | "));
const nodes = r.listNodes().filter((n) => n.getMesh()).map((n) => n.getName() + "<" + n.getMesh().listPrimitives().map((p) => p.getMaterial()?.getName()).join(",") + ">");
console.log("NODES", nodes.length, nodes.join(" | ").slice(0, 3000));
