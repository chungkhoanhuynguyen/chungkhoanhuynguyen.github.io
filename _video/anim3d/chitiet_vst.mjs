// Ảnh tĩnh thử cho chuẩn chi tiết (điểm vào src/index_chitiet.tsx). Ảnh 3D < 1 giây = 3D không chạy (lỗi); DangGrid chỉ vẽ 2D nên ~1 giây là bình thường.
import { bundle } from "@remotion/bundler";
import { renderStill, selectComposition } from "@remotion/renderer";
import path from "node:path";
const [comp, frames, scale = "0.4", outdir = "/tmp/st"] = process.argv.slice(2);
const chromiumOptions = { gl: "swiftshader" };
const serveUrl = await bundle({ entryPoint: path.resolve("src/index_chitiet.tsx") });
const composition = await selectComposition({ serveUrl, id: comp, chromiumOptions });
for (const f of frames.split(",").map(Number)) { const t0 = Date.now();
  await renderStill({ composition, serveUrl, frame: f, output: `${outdir}/f${String(f).padStart(5, "0")}.png`, scale: Number(scale), chromiumOptions, timeoutInMilliseconds: 300000 });
  console.log("still", f, ((Date.now() - t0) / 1000).toFixed(1) + "s"); }
