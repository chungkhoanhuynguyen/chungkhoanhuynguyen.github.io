// 4 ảnh cảnh xe (stage_ct, cờ chiTiet): siêu xe trong showroom đèn tím xanh, siêu xe cánh chim đỗ trước tiệm suaxe2,
// speedster mui trần có người lái trên phố, mô tô sportbike vàng có nhân vật nữ ngồi (áo sơ mi, quần dài – kín đáo).
import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { Stage, Run, Cast, V, SetKey } from "./stage_ct";
import { Pose } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { LK } from "../vang/look";
import { MUI_SEAT, MOTO_SEAT } from "./canh_xe";

const P = (expr: Expr, o: Omit<Pose, "expr"> = {}) => (_t: number): Pose => ({ expr, blink: false, ...o });
const C = (a: string, p: V, pose: Cast["pose"], ride = false): Cast => ({ a, p, pose, ride });
type Sh = { set: SetKey; light: LK; cam: [V, V, number]; cast: Cast[] };
export const XE_CANH: Sh[] = [
  { set: "showroom", light: "room", cam: [[4.6, 1.35, 4.9], [0, 0.6, 0], 36], cast: [C("vest", [-3.9, 0, 1.2], P("smile", { side: 1, mode: "stand" }))] },
  { set: "suaxe2xe", light: "golden", cam: [[-5.6, 1.45, -13.2], [-0.4, 0.75, -6.2], 40], cast: [C("hung", [1.6, 0, -6.5], P("shock", { side: -1, mode: "stand" }))] },
  { set: "phoxe", light: "day", cam: [[6.3, 1.5, -1.2], [11.6, 0.75, 2.9], 38], cast: [C("cuong", MUI_SEAT() as V, P("grin", { mode: "stand" }), true)] },
  { set: "phoxe", light: "day", cam: [[-8.3, 1.25, -1.9], [-8.1, 0.85, 3.2], 34], cast: [C("thuong", MOTO_SEAT() as V, P("smile", { side: -1, mode: "stand" }), true)] },
];
export const XeCanh: React.FC = () => <AbsoluteFill style={{ background: "#000" }}>
  {XE_CANH.map((s, i) => { const runs: Run[] = [{ a: 0, b: 30, s: { set: s.set, light: s.light, from: s.cam, to: s.cam, cast: s.cast } }];
    return <Sequence key={i} from={i * 30} durationInFrames={30}><Stage set={s.set} runs={runs} chiTiet /></Sequence>; })}
</AbsoluteFill>;
