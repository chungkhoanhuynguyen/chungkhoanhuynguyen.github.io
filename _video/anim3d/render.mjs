// node render.mjs <comp> <from> <to> <out.mp4> [scale]
import { bundle } from "@remotion/bundler";
import { renderMedia, selectComposition } from "@remotion/renderer";
import path from "node:path";
const [comp, a, b, out, scale = "0.6667"] = process.argv.slice(2);
const chromiumOptions = { gl: "swiftshader" };
const serveUrl = await bundle({ entryPoint: path.resolve("src/index.tsx") });
const composition = await selectComposition({ serveUrl, id: comp, chromiumOptions });
const t0 = Date.now();
await renderMedia({ composition, serveUrl, codec: "h264", crf: 18, outputLocation: out, frameRange: [Number(a), Number(b)], scale: Number(scale), chromiumOptions, concurrency: 2, timeoutInMilliseconds: 900000, muted: true,
  onProgress: ({ renderedFrames }) => { if (renderedFrames % 5 === 0) console.log("frames", renderedFrames, ((Date.now() - t0) / 1000).toFixed(0) + "s"); } });
console.log("done", ((Date.now() - t0) / 1000).toFixed(0) + "s");
