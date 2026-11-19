// Ảnh soát chuẩn chi tiết (đăng ký trong src/index_chitiet.tsx, KHÔNG trong index.tsx → không đổi mã băm phim cũ).
//  SuaXe2Demo: khung 30*i + 15 = set cũ "suaxe" + nhân vật cast2 (vang/stage), 90 + 30*i + 15 = "suaxe2" + cast2 nâng trang phục (stage_ct, chiTiet).
//  DangGrid: tờ lưới dáng thẻ 2D (không cần WebGL) – mỗi nhân vật 2 hàng: cũ / mới.
import React from "react";
import * as THREE from "three";
import { AbsoluteFill, Sequence } from "remotion";
import { Stage as StageOld, Run as RunOld } from "../vang/stage";
import { Stage, Run, Cast, V } from "./stage_ct";
import { Actor, OUT, Pose, NGAN } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { ActorX } from "./cast2x";

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
const FILM = { chiTiet: true }; // cờ cấp phim: bật trang phục mới + set chi tiết
const runsOld: RunOld[] = CAMS.map((c, i) => ({ a: i * 30, b: i * 30 + 30, s: { set: "suaxe", light: "golden", from: c.cam, to: c.cam, cast: c.cast } }));
const runsNew: Run[] = CAMS.map((c, i) => ({ a: i * 30, b: i * 30 + 30, s: { set: "suaxe2", light: "golden", from: c.cam, to: c.cam, cast: c.cast } }));
export const SUAXE2_FRAMES = 180;
export const SuaXe2Demo: React.FC = () => (
  <AbsoluteFill style={{ background: "#000" }}>
    <Sequence from={0} durationInFrames={90}><StageOld set="suaxe" runs={runsOld} /></Sequence>
    <Sequence from={90} durationInFrames={90}><Stage set="suaxe2" runs={runsNew} chiTiet={FILM.chiTiet} /></Sequence>
  </AbsoluteFill>
);

// ---------- tờ lưới dáng ----------
export const DANG: [string, Pose][] = [
  ["đứng nghiêng", { expr: "neutral", side: 1, mode: "stand" }],
  ["đi", { expr: "smile", side: 1, mode: "stroll", phase: 0.25 }],
  ["với tay", { expr: "stern", side: 1, mode: "stand", reach: [0.55, 0.15] }],
  ["chính diện", { expr: "neutral", mode: "stand" }],
  ["giơ tay", { expr: "grin", mode: "stand", wave: 1 }],
  ["cầm điện thoại", { expr: "nervous", mode: "stand", acc: ["phone"] }],
  ["cầm giấy", { expr: "shock", mode: "stand", acc: ["paper"] }],
  ["ngồi", { expr: "neutral", mode: "sit" }],
];
const WHO: [string, string][] = [["hung", "Hùng"], ["chien", "Chiến"], ["ngan", "Ngân (nữ tóc dài)"]];
const mk = (w: string, x: boolean) => { const o = OUT[w]?.o ?? NGAN, h = OUT[w]?.h ?? 1.58, sd = OUT[w]?.seed ?? 9; return x ? new ActorX(o, h, sd, w) : new Actor(o, h, sd); };
export const DangGrid: React.FC = () => {
  const cam = new THREE.PerspectiveCamera(); cam.position.set(0, 1, 3); const tint = new THREE.Color(1, 1, 1);
  const rows = WHO.flatMap(([w, nm]) => [false, true].map((x) => ({ lab: `${nm} – ${x ? "MỚI" : "cũ"}`, imgs: DANG.map(([, p]) => { const a = mk(w, x); a.pose(p, cam, tint); return ((a as unknown as { c: HTMLCanvasElement }).c).toDataURL(); }) })));
  return <AbsoluteFill style={{ background: "#e9dcb8", padding: 10, fontFamily: "DejaVu Sans, Arial" }}>
    <div style={{ display: "flex", marginLeft: 150 }}>{DANG.map(([n]) => <div key={n} style={{ width: 210, textAlign: "center", fontSize: 20, fontWeight: 800 }}>{n}</div>)}</div>
    {rows.map((r) => <div key={r.lab} style={{ display: "flex", alignItems: "center", background: r.lab.includes("MỚI") ? "rgba(255,255,255,.35)" : "transparent" }}>
      <div style={{ width: 150, fontSize: 18, fontWeight: 800 }}>{r.lab}</div>{r.imgs.map((s, i) => <img key={i} src={s} style={{ width: 210, height: 350 }} />)}</div>)}
  </AbsoluteFill>;
};
