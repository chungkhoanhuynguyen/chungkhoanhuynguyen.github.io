// Ảnh tĩnh thử cho chuẩn chi tiết (điểm vào src/index_chitiet.tsx). Ảnh 3D < 1 giây = 3D không chạy (lỗi); tờ lưới Luoi* chỉ vẽ 2D nên vài giây là bình thường.
// node chitiet_vst.mjs <comp[,comp2,...]> <frames> [scale] [outdir]  → <outdir>/<comp>_f<khung>.png
import { bundle } from "@remotion/bundler";
import { renderStill, selectComposition } from "@remotion/renderer";
import path from "node:path";
const [comps, frames, scale = "0.4", outdir = "/tmp/st"] = process.argv.slice(2);
const chromiumOptions = { gl: "swiftshader" };
const serveUrl = await bundle({ entryPoint: path.resolve("src/index_chitiet.tsx") });
for (const comp of comps.split(",")) { const composition = await selectComposition({ serveUrl, id: comp, chromiumOptions });
  for (const f of frames.split(",").map(Number)) { const t0 = Date.now();
    await renderStill({ composition, serveUrl, frame: f, output: `${outdir}/${comp}_f${String(f).padStart(5, "0")}.png`, scale: Number(scale), chromiumOptions, timeoutInMilliseconds: 300000, onBrowserLog: (l) => { if (/VA CHẠM|lỗi/.test(l.text)) console.log("[trình duyệt]", l.text); } });
    console.log("still", comp, f, ((Date.now() - t0) / 1000).toFixed(1) + "s"); } }
