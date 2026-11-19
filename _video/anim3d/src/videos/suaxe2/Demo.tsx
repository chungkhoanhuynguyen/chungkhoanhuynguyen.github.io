// Ảnh so sánh tiệm sửa xe: set cũ "suaxe" + nhân vật thẻ 2D cast2 (như DN1) vs set chi tiết "suaxe2" + CÙNG nhân vật đó nâng trang phục (cast2x).
// 3 góc máy (trung_a, trung_b, cận mặt), mỗi góc 30 khung. Khung 30*i + 15 = bản cũ, 90 + 30*i + 15 = bản mới.
import React from "react";
import { AbsoluteFill, Sequence } from "remotion";
import { Stage, Run, Cast, V } from "../vang/stage";
import { Pose } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { CAST2X } from "./cast2x";

type PO = Omit<Pose, "expr">;
const P = (expr: Expr, o: PO = {}) => (_t: number): Pose => ({ expr, blink: false, ...o });
const C = (a: string, p: V, pose: Cast["pose"]): Cast => ({ a, p, pose });
const CH = (e: Expr, x = 0.2, o: PO = {}) => C("chien", [x, 0, 0.7], P(e, { side: -1, mode: "stand", ...o }));
const HG = (e: Expr, x = 0.95, o: PO = {}) => C("hung", [x, 0, 0.7], P(e, { side: 1, mode: "stand", ...o }));
type Cam = [V, V, number];
export const CAMS: { name: string; cam: Cam; cast: Cast[] }[] = [
  { name: "trung_a", cam: [[0.4, 1.45, -3.2], [0.4, 1.25, 3], 42], cast: [CH("smug"), HG("neutral", 0.95)] },
  { name: "trung_b", cam: [[2.2, 1.5, -2.0], [0.0, 1.2, 1.6], 40], cast: [CH("dazed", 0.1), HG("stern", 0.95)] },
  { name: "can_mat", cam: [[0.575, 1.22, -0.75], [0.575, 1.1, 0.7], 30], cast: [CH("smug"), HG("sad")] },
];
CAST2X.light = "golden";
CAST2X.shots = CAMS.map((c) => ({ cam: c.cam[0], chars: c.cast.map((k) => ({ who: k.a, p: k.p, pose: k.pose(0, 1) })) }));
const runs = (set: "suaxe" | "suaxe2"): Run[] => CAMS.map((c, i) => ({ a: i * 30, b: i * 30 + 30, s: { set, light: "golden", from: c.cam, to: c.cam, cast: set === "suaxe" ? c.cast : [] } }));
export const SUAXE2_FRAMES = 180;
export const SuaXe2Demo: React.FC = () => (
  <AbsoluteFill style={{ background: "#000" }}>
    <Sequence from={0} durationInFrames={90}><Stage set="suaxe" runs={runs("suaxe")} /></Sequence>
    <Sequence from={90} durationInFrames={90}><Stage set="suaxe2" runs={runs("suaxe2")} /></Sequence>
  </AbsoluteFill>
);
/** soát thẻ nhân vật 2D (không cần WebGL): trái = cast2 gốc, phải = bản nâng trang phục */
import * as THREE from "three";
import { Actor, OUT } from "../vang/cast2";
import { ActorX } from "./cast2x";
export const CardTest: React.FC = () => {
  const cam = new THREE.PerspectiveCamera(); cam.position.set(0, 1, -3); const tint = new THREE.Color(1, 1, 1);
  const imgs: string[] = [];
  for (const [w, e, sd] of [["hung", "neutral", 1], ["chien", "smug", -1]] as [string, Expr, 1 | -1][]) {
    const a = new Actor(OUT[w].o, OUT[w].h, OUT[w].seed); a.pose({ expr: e, side: sd, mode: "stand" }, cam, tint);
    const b = new ActorX(w); b.pose({ expr: e, side: sd, mode: "stand" }, cam, tint);
    for (const x of [a, b]) imgs.push(((x as unknown as { c: HTMLCanvasElement }).c).toDataURL());
  }
  return <AbsoluteFill style={{ background: "#d8c8a0", flexDirection: "row" }}>{imgs.map((s, i) => <img key={i} src={s} style={{ width: 480, height: 800 }} />)}</AbsoluteFill>;
};
