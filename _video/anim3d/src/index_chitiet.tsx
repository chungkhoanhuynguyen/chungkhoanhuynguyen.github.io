// Điểm vào riêng cho ảnh soát chuẩn chi tiết (tên có "chitiet" → plan_units.py không tính vào mã băm phim cũ).
// Dựng thử: node chitiet_vst.mjs <comp> <frames> [scale] [outdir]
import React from "react";
import { Composition, registerRoot } from "remotion";
import { SuaXe2Demo, SUAXE2_FRAMES, Luoi, PAGES } from "./videos/chitiet/Demo";
import { XeLuoi, XE_N, MAU_N } from "./videos/chitiet/XeLuoi";
import { XeCanh, XeCanh2 } from "./videos/chitiet/XeCanh";
import { Canh3D, CANH3D_MAU, Canh3DProps } from "./videos/chitiet/Canh3D";
const Root: React.FC = () => <>
  <Composition id="SuaXe2Demo" component={SuaXe2Demo} durationInFrames={SUAXE2_FRAMES} fps={30} width={1920} height={1080} />
  {Array.from({ length: PAGES }, (_, p) => <Composition key={p} id={`Luoi${p + 1}`} component={Luoi} defaultProps={{ page: p }} durationInFrames={1} fps={30} width={1350} height={2830} />)}
  <Composition id="LuoiSua" component={Luoi} defaultProps={{ page: 0, keys: ["gym", "gym2", "dung", "boxer", "me"] }} durationInFrames={1} fps={30} width={1350} height={1800} />
  <Composition id="XeLuoi" component={XeLuoi} durationInFrames={XE_N} fps={30} width={1920} height={410} />
  <Composition id="XeCanh" component={XeCanh} durationInFrames={120} fps={30} width={1920} height={1080} />
  <Composition id="XeMau" component={XeLuoi} defaultProps={{ bo: "mau" as const }} durationInFrames={MAU_N} fps={30} width={1920} height={410} />
  <Composition id="XeCanh2" component={XeCanh2} durationInFrames={180} fps={30} width={1920} height={1080} />
  <Composition id="Canh3D" component={Canh3D} defaultProps={CANH3D_MAU} durationInFrames={60} fps={30} width={1920} height={1080}
    calculateMetadata={({ props }: { props: Canh3DProps }) => ({ durationInFrames: Math.max(1, props.frames), fps: props.fps ?? 30 })} />
</>;
registerRoot(Root);
