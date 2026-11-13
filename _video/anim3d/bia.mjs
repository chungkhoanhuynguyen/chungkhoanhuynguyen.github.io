import { bundle } from "@remotion/bundler";
import { renderStill, selectComposition } from "@remotion/renderer";
import path from "node:path";
const chromiumOptions = { gl: "swiftshader" };
const serveUrl = await bundle({ entryPoint: path.resolve("src/index.tsx"), publicDir: path.resolve("public") });
for (const v of (process.argv[2] ?? "A,B,C").split(",")) { const inputProps = { v };
  const composition = await selectComposition({ serveUrl, id: "Bia", chromiumOptions, inputProps });
  await renderStill({ composition, serveUrl, inputProps, frame: 0, output: `${process.argv[3] ?? "/tmp"}/bia_${v}.png`, scale: 1280 / 1920, chromiumOptions, timeoutInMilliseconds: 300000 }); console.log("bia", v); }
