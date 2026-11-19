import { NodeIO } from "@gltf-transform/core"; import { ALL_EXTENSIONS } from "@gltf-transform/extensions";
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS); const doc = await io.read(process.argv[2]); const [x0,x1,y0,y1,z0,z1] = process.argv[3].split(",").map(Number);
for (const n of doc.getRoot().listNodes()) { const m = n.getMesh(); if (!m) continue; const W = n.getWorldMatrix();
  for (const p of m.listPrimitives()) { const pos = p.getAttribute("POSITION"), idx = p.getIndices(); const cnt = idx ? idx.getCount() : pos.getCount(); let hit = 0, tot = cnt / 3; const v = [0,0,0];
    const tr = (i) => { pos.getElement(i, v); const [a,b,c] = v; return [W[0]*a+W[4]*b+W[8]*c+W[12], W[1]*a+W[5]*b+W[9]*c+W[13], W[2]*a+W[6]*b+W[10]*c+W[14]]; };
    for (let t = 0; t < cnt; t += 3) { const ids = [0,1,2].map((k) => idx ? idx.getScalar(t+k) : t+k); const P = ids.map(tr); const c = [0,1,2].map((k) => (P[0][k]+P[1][k]+P[2][k])/3); if (c[0]>x0&&c[0]<x1&&c[1]>y0&&c[1]<y1&&c[2]>z0&&c[2]<z1) hit++; }
    if (hit) console.log(n.getName(), p.getMaterial()?.getName(), "hit", hit, "/", tot); } }
