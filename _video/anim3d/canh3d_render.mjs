// Dựng 1 cảnh 3D cho video tin nóng: node canh3d_render.mjs <props.json> <out.mp4> [scale]
// Gói bundle được giữ lại ở /tmp/canh3d_bundle_<mã nguồn> để các cảnh sau dùng lại (đỡ ~1 phút/cảnh).
import { bundle } from "@remotion/bundler";
import { renderMedia, selectComposition } from "@remotion/renderer";
import path from "node:path"; import fs from "node:fs";
const [pj, out, scale = "1"] = process.argv.slice(2);
const inputProps = JSON.parse(fs.readFileSync(pj, "utf8")); const chromiumOptions = { gl: "swiftshader" };
const BD = process.env.CANH3D_BUNDLE;
let serveUrl = BD && fs.existsSync(path.join(BD, "index.html")) ? BD : null;
if (!serveUrl) { serveUrl = await bundle({ entryPoint: path.resolve("src/index_chitiet.tsx") }); if (BD) { fs.cpSync(serveUrl, BD, { recursive: true }); } }
const composition = await selectComposition({ serveUrl, id: "Canh3D", inputProps, chromiumOptions });
const t0 = Date.now(); const RG = (process.env.CANH3D_RANGE || "").split("-").map(Number); const frameRange = RG.length === 2 && RG.every(Number.isFinite) ? RG : null; // khúc khung (dựng song song nhiều máy)
await renderMedia({ composition, serveUrl, codec: "h264", outputLocation: out, inputProps, chromiumOptions, scale: Number(scale), concurrency: Number(process.env.CANH3D_CONC || 1), timeoutInMilliseconds: 300000, crf: 18, ...(frameRange ? { frameRange } : {}),
  onBrowserLog: (l) => { if (/VA CHẠM|lỗi/.test(l.text)) console.log("[trình duyệt]", l.text); } });
console.log("canh3d", inputProps.set, inputProps.frames, "khung", ((Date.now() - t0) / 1000).toFixed(0) + "s");
