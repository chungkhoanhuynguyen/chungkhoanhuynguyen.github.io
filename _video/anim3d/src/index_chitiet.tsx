// Điểm vào riêng cho ảnh soát chuẩn chi tiết (tên có "chitiet" → plan_units.py không tính vào mã băm phim cũ).
// Dựng thử: node chitiet_vst.mjs <comp> <frames> [scale] [outdir]
import React from "react";
import { Composition, registerRoot } from "remotion";
import { SuaXe2Demo, SUAXE2_FRAMES, Luoi, PAGES } from "./videos/chitiet/Demo";
const Root: React.FC = () => <>
  <Composition id="SuaXe2Demo" component={SuaXe2Demo} durationInFrames={SUAXE2_FRAMES} fps={30} width={1920} height={1080} />
  {Array.from({ length: PAGES }, (_, p) => <Composition key={p} id={`Luoi${p + 1}`} component={Luoi} defaultProps={{ page: p }} durationInFrames={1} fps={30} width={1350} height={2830} />)}
</>;
registerRoot(Root);
