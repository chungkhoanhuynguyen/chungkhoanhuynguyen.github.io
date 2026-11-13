// node render_units.mjs <plan.json> <group_index> <outdir> : dựng từng đơn vị cảnh của nhóm (mỗi cảnh một file mp4 riêng)
import { bundle } from "@remotion/bundler";
import { renderMedia, selectComposition } from "@remotion/renderer";
import path from "node:path"; import fs from "node:fs";
const [planF, gi, outDir] = process.argv.slice(2);
const plan = JSON.parse(fs.readFileSync(planF, "utf8")); const names = plan.groups[Number(gi)] ?? [];
if (!names.length) { console.log("khong co viec"); process.exit(0); }
fs.mkdirSync(outDir, { recursive: true });
const chromiumOptions = { gl: "swiftshader" };
const serveUrl = await bundle({ entryPoint: path.resolve("src/index.tsx") });
const composition = await selectComposition({ serveUrl, id: plan.comp, chromiumOptions });
const byName = Object.fromEntries(plan.units.map((u) => [u.name, u]));
for (const n of names) { const u = byName[n], t0 = Date.now();
  await renderMedia({ composition, serveUrl, codec: "h264", crf: 18, outputLocation: path.join(outDir, n), frameRange: [u.f0, u.f1], scale: 1, chromiumOptions, concurrency: 2, timeoutInMilliseconds: 900000, muted: true });
  console.log("xong", u.id, u.f1 - u.f0 + 1, "khung", ((Date.now() - t0) / 1000).toFixed(0) + "s"); }
