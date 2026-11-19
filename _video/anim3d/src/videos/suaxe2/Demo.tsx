// Ảnh so sánh bối cảnh tiệm sửa xe: set cũ "suaxe" + nhân vật thẻ 2D (cast2) vs set chi tiết "suaxe2" + nhân vật 3D toon (cast3).
// 5 góc máy, mỗi góc 30 khung. Khung 30*i + 15 = bản cũ, 150 + 30*i + 15 = bản mới.
import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { Stage, Run, Cast, V } from "../vang/stage";
import { Pose } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { CAST3, Pose3 } from "./cast3";

type PO = Omit<Pose, "expr">;
const P = (expr: Expr, o: PO = {}) => (_t: number): Pose => ({ expr, blink: false, ...o });
const C = (a: string, p: V, pose: Cast["pose"]): Cast => ({ a, p, pose });
const CH = (e: Expr, x = 0.2) => C("chien", [x, 0, 0.7], P(e, { side: -1, mode: "stand" }));
const HG = (e: Expr, x = 0.95, o: PO = {}) => C("hung", [x, 0, 0.7], P(e, { side: 1, mode: "stand", ...o }));
type Cam = [V, V, number];
// máy ở -z nhìn về +z: +x nằm bên TRÁI màn. Chiến x = 0.2 (phải màn), Hùng x = 0.95 (trái màn), quay mặt vào nhau.
const RYC = Math.PI - 0.6, RYH = -(Math.PI - 0.6);
export const CAMS: { name: string; cam: Cam; cast: Cast[]; c3: Pose3[] }[] = [
  { name: "rong_a", cam: [[0.4, 1.75, -4.8], [0.4, 1.45, 3], 46], cast: [], c3: [{ who: "lan", p: [2.55, 0, -0.95], ry: Math.PI - 0.5, e: "smile", armL: { f: 0.5, out: 0.1, el: 1.3 }, prop: "phone", gaze: 0.3 }] },
  { name: "rong_b", cam: [[-3.0, 2.2, -4.2], [1.2, 1.1, 2.2], 52], cast: [], c3: [{ who: "lan", p: [2.55, 0, -0.95], ry: Math.PI - 0.9, e: "smile", armL: { f: 0.5, out: 0.1, el: 1.3 }, prop: "phone", gaze: 0.3 }] },
  { name: "trung_a", cam: [[0.4, 1.45, -3.2], [0.4, 1.25, 3], 42], cast: [CH("smug"), HG("neutral", 0.95, { acc: ["paper"] })],
    c3: [{ who: "chien", p: [0.2, 0, 0.7], ry: RYC, e: "smug", gaze: 0.6, armR: { f: 0.15, out: 0.55, el: 1.9 }, armL: { f: 0.35, out: 0.4, el: 1.3, palm: 1.2 } },
      { who: "hung", p: [0.95, 0, 0.7], ry: RYH, e: "neutral", gaze: -0.6, armL: { f: 0.15, out: 0.12, el: 0.9 }, prop: "wrench" }] },
  { name: "trung_b", cam: [[2.2, 1.5, -2.0], [0.0, 1.2, 1.6], 40], cast: [CH("dazed", 0.1), HG("stern", 0.95)],
    c3: [{ who: "chien", p: [0.1, 0, 0.7], ry: RYC + 0.2, e: "dazed", gaze: 0.5, armR: { f: 0.5, out: 0.35, el: 1.5 }, armL: { f: 0.5, out: 0.35, el: 1.5 } },
      { who: "hung", p: [0.95, 0, 0.7], ry: RYH, e: "stern", gaze: -0.7, armR: { f: 0.15, out: 0.55, el: 1.9 }, armL: { f: 0.45, out: 0.15, el: 1.0 }, prop: "wrench" }] },
  { name: "can_mat", cam: [[0.575, 1.6, -0.95], [0.575, 1.55, 0.7], 28], cast: [CH("smug"), HG("sad")],
    c3: [{ who: "chien", p: [0.2, 0, 0.7], ry: RYC - 0.15, e: "talk", gaze: 0.7, head: 0.15, armL: { f: 0.45, out: 0.35, el: 1.4, palm: 1.0 } },
      { who: "hung", p: [0.95, 0, 0.7], ry: RYH + 0.15, e: "worried", gaze: -0.7, head: -0.1 }] },
];
CAST3.shots = CAMS.map((c) => c.c3);
const runs = (set: "suaxe" | "suaxe2"): Run[] => CAMS.map((c, i) => ({ a: i * 30, b: i * 30 + 30, s: { set, light: "golden", from: c.cam, to: c.cam, cast: set === "suaxe" ? c.cast : [] } }));
export const SUAXE2_FRAMES = 300;
export const SuaXe2Demo: React.FC = () => (
  <AbsoluteFill style={{ background: "#000" }}>
    <Sequence from={0} durationInFrames={150}><Stage set="suaxe" runs={runs("suaxe")} /></Sequence>
    <Sequence from={150} durationInFrames={150}><Stage set="suaxe2" runs={runs("suaxe2")} /></Sequence>
  </AbsoluteFill>
);
