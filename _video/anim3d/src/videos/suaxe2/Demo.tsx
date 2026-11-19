// Ảnh so sánh bối cảnh tiệm sửa xe: set cũ "suaxe" vs set chi tiết "suaxe2" (cùng 4 góc máy, cùng nhân vật).
// Khung 30*i + 15 (i = 0..3) = set cũ, 120 + 30*i + 15 = set mới.
import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { Stage, Run, Cast, V, SetKey } from "../vang/stage";
import { Pose } from "../vang/cast2";
import { Expr } from "../pho/toon";

type PO = Omit<Pose, "expr">;
const P = (expr: Expr, o: PO = {}) => (_t: number): Pose => ({ expr, blink: false, ...o });
const C = (a: string, p: V, pose: Cast["pose"]): Cast => ({ a, p, pose });
const CH = (e: Expr, x = 0.2) => C("chien", [x, 0, 0.7], P(e, { side: -1, mode: "stand" }));
const HG = (e: Expr, x = 0.95, o: PO = {}) => C("hung", [x, 0, 0.7], P(e, { side: 1, mode: "stand", ...o }));
type Cam = [V, V, number];
export const CAMS: { name: string; cam: Cam; cast: Cast[] }[] = [
  { name: "rong_a", cam: [[0.4, 1.75, -4.8], [0.4, 1.45, 3], 46], cast: [] },
  { name: "rong_b", cam: [[-3.0, 2.2, -4.2], [1.2, 1.1, 2.2], 52], cast: [] },
  { name: "trung_a", cam: [[0.4, 1.45, -3.2], [0.4, 1.25, 3], 42], cast: [CH("smug"), HG("neutral", 0.95, { acc: ["paper"] })] },
  { name: "trung_b", cam: [[2.2, 1.5, -2.0], [0.0, 1.2, 1.6], 40], cast: [CH("dazed", 0.1), HG("stern", 0.95)] },
];
const runs: Run[] = CAMS.map((c, i) => ({ a: i * 30, b: i * 30 + 30, s: { set: "suaxe", light: "golden", from: c.cam, to: c.cam, cast: c.cast } }));
const withSet = (set: SetKey): Run[] => runs.map((r) => ({ ...r, s: { ...r.s, set } }));
export const SUAXE2_FRAMES = 240;
export const SuaXe2Demo: React.FC = () => (
  <AbsoluteFill style={{ background: "#000" }}>
    <Sequence from={0} durationInFrames={120}><Stage set="suaxe" runs={withSet("suaxe")} /></Sequence>
    <Sequence from={120} durationInFrames={120}><Stage set="suaxe2" runs={withSet("suaxe2")} /></Sequence>
  </AbsoluteFill>
);
