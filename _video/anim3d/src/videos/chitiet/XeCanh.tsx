// 4 ảnh cảnh xe (stage_ct, cờ chiTiet): siêu xe trong showroom đèn tím xanh, siêu xe cánh chim đỗ trước tiệm suaxe2,
// speedster mui trần có người lái trên phố, mô tô sportbike vàng có nhân vật nữ ngồi (áo sơ mi, quần dài – kín đáo).
import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { Stage, Run, Cast, V, SetKey } from "./stage_ct";
import { Pose } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { LK } from "../vang/look";
import { MUI_SEAT, MOTO_SEAT, MUI2_SEAT, SPY_SEAT_W, BIKE2_SEAT_W, SHOW2, LEAN_MOTO, LEAN_XE } from "./canh_xe";

const P = (expr: Expr, o: Omit<Pose, "expr"> = {}) => (_t: number): Pose => ({ expr, blink: false, ...o });
const C = (a: string, p: V, pose: Cast["pose"], ride = false, lean = 0): Cast => ({ a, p, pose, ride, lean });
type Sh = { set: SetKey; light: LK; cam: [V, V, number]; cast: Cast[] };
export const XE_CANH: Sh[] = [
  { set: "showroom", light: "room", cam: [[4.6, 1.35, 4.9], [0, 0.6, 0], 36], cast: [C("vest", [-3.9, 0, 1.2], P("smile", { side: 1, mode: "stand" }))] },
  { set: "suaxe2xe", light: "golden", cam: [[-5.6, 1.45, -13.2], [-0.4, 0.75, -6.2], 40], cast: [C("hung", [1.6, 0, -6.5], P("shock", { side: -1, mode: "stand" }))] },
  { set: "phoxe", light: "day", cam: [[6.3, 1.5, -1.2], [11.6, 0.75, 2.9], 38], cast: [C("cuong", MUI_SEAT() as V, P("grin", { mode: "stand" }), true)] },
  { set: "phoxe", light: "day", cam: [[-8.3, 1.25, -1.9], [-8.1, 0.85, 3.2], 34], cast: [C("thuong", MOTO_SEAT() as V, P("smile", { side: -1, mode: "stand" }), true)] },
];
// v7: xe mẫu CC BY (Goblin, Abyss, mui trần đã gỡ logo, siêu mô tô SPY, mô tô concept)
export const XE_CANH2: Sh[] = [
  { set: "showroom2", light: "room", cam: [[0.3, 2.1, 7.6], [-0.1, 0.7, -0.5], 54], cast: [C("vest", [SHOW2.people[0][0], 0, SHOW2.people[0][1]], P("smile", { mode: "stand" }))] },
  { set: "suaxe2mau", light: "golden", cam: [[-5.6, 1.45, -13.2], [-0.4, 0.75, -6.2], 40], cast: [C("hung", [1.7, 0, -6.4], P("shock", { side: -1, mode: "stand" }))] },
  { set: "phoxe2", light: "day", cam: [[6.3, 1.5, -1.2], [11.6, 0.75, 2.9], 38], cast: [C("cuong", MUI2_SEAT() as V, P("grin", { mode: "stand" }), true, LEAN_XE)] },
  { set: "phoxe2", light: "day", cam: [[-8.4, 1.15, 1.1], [-8.1, 0.8, 3.2], 46], cast: [C("thuong", SPY_SEAT_W() as V, P("smile", { side: -1, mode: "stand" }), true, LEAN_MOTO), C("lam", BIKE2_SEAT_W() as V, P("neutral", { side: -1, mode: "stand" }), true, LEAN_MOTO)] },
  { set: "phoxe2", light: "day", cam: [[9.4, 1.6, 0.6], [11.4, 0.7, 2.9], 40], cast: [C("cuong", MUI2_SEAT() as V, P("grin", { mode: "stand" }), true, LEAN_XE)] }, // soát khoang lái mui trần
  { set: "showroom2", light: "room", cam: [[0, 6.1, 0.3], [0, 0, 0], 110], cast: [] }, // soát từ trên xuống (va chạm)
];
export const XeCanh2: React.FC = () => <AbsoluteFill style={{ background: "#000" }}>
  {XE_CANH2.map((s, i) => { const runs: Run[] = [{ a: 0, b: 30, s: { set: s.set, light: s.light, from: s.cam, to: s.cam, cast: s.cast } }];
    return <Sequence key={i} from={i * 30} durationInFrames={30}><Stage set={s.set} runs={runs} chiTiet /></Sequence>; })}
</AbsoluteFill>;
export const XeCanh: React.FC = () => <AbsoluteFill style={{ background: "#000" }}>
  {XE_CANH.map((s, i) => { const runs: Run[] = [{ a: 0, b: 30, s: { set: s.set, light: s.light, from: s.cam, to: s.cam, cast: s.cast } }];
    return <Sequence key={i} from={i * 30} durationInFrames={30}><Stage set={s.set} runs={runs} chiTiet /></Sequence>; })}
</AbsoluteFill>;
