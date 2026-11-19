// Ảnh soát chuẩn chi tiết (đăng ký trong src/index_chitiet.tsx, KHÔNG trong index.tsx → không đổi mã băm phim cũ).
//  SuaXe2Demo: khung 30*i + 15 = set cũ "suaxe" + nhân vật cast2 (vang/stage), 90 + 30*i + 15 = "suaxe2" + cast2 nâng trang phục (stage_ct, chiTiet).
//  DangGrid: tờ lưới dáng thẻ 2D (không cần WebGL) – mỗi nhân vật 2 hàng: cũ / mới.
import React from "react";
import * as THREE from "three";
import { AbsoluteFill, Sequence } from "remotion";
import { Stage as StageOld, Run as RunOld } from "../vang/stage";
import { Stage, Run, Cast, V } from "./stage_ct";
import { OUT, Pose, Outfit, crowd, DO, NGAN, VEST, CLERK, ME2, GYM, BOXER, XOI } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { ActorX, FIT } from "./cast2x";

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

// ---------- tờ lưới dáng: MỌI nhân vật của xưởng (cast2: hằng số + OUT + quần chúng c0..c9), mỗi hàng 1 nhân vật ----------
export const DANG: [string, Pose][] = [
  ["nghiêng phải", { expr: "neutral", side: 1, mode: "stand" }],
  ["chính diện", { expr: "neutral", mode: "stand" }],
  ["đi", { expr: "smile", side: 1, mode: "stroll", phase: 0.25 }],
  ["ngồi", { expr: "neutral", mode: "sit" }],
  ["nghiêng trái", { expr: "stern", side: -1, mode: "stand" }],
  ["áo mưa", { expr: "neutral", side: 1, mode: "stand", acc: ["raincoat"] }],
  ["cầm giấy", { expr: "shock", mode: "stand", acc: ["paper"] }],
];
type Who = { k: string; o: Outfit; h: number; seed: number; ten: string };
const NAMED: [string, Outfit, number, number, string][] = [["tan", DO, 1.7, 3, "Tân (DO)"], ["ngan", NGAN, 1.58, 9, "Ngân (NGAN)"], ["vest", VEST, 1.76, 5, "Vest"], ["clerk", CLERK, 1.55, 5, "Clerk"], ["me", ME2, 1.48, 5, "Mẹ (ME2)"],
  ["gym", GYM, 1.82, 5, "Gym"], ["gym2", { ...GYM, jacket: "#f4f4f2", skin: "#d9a77e", hair: "#3a2a20" }, 1.82, 5, "Gym2"], ["boxer", BOXER, 1.55, 5, "Boxer"], ["xoi", XOI, 1.55, 5, "Xôi"]];
export const ALL: Who[] = [...NAMED.map(([k, o, h, seed, ten]) => ({ k, o, h, seed, ten })), ...Object.entries(OUT).map(([k, v]) => ({ k, o: v.o, h: v.h, seed: v.seed, ten: k })),
  ...Array.from({ length: 10 }, (_, i) => ({ k: "c" + i, o: crowd(i), h: 1.55 + (i % 5) * 0.05, seed: 5 + i * 3, ten: "quần chúng c" + i }))];
export const PER = 8, PAGES = Math.ceil(ALL.length / PER);
export const Luoi: React.FC<{ page: number; keys?: string[] }> = ({ page, keys }) => {
  const cam = new THREE.PerspectiveCamera(); cam.position.set(0, 1, 3); const tint = new THREE.Color(1, 1, 1);
  const rows = (keys ? ALL.filter((w) => keys.includes(w.k)) : ALL.slice(page * PER, page * PER + PER)).map((w) => ({ w, imgs: DANG.map(([, p]) => { const a = new ActorX(w.o, w.h, w.seed, w.k); a.pose(p, cam, tint); return ((a as unknown as { c: HTMLCanvasElement }).c).toDataURL(); }) }));
  return <AbsoluteFill style={{ background: "#eeeae2", padding: "8px 10px", fontFamily: "DejaVu Sans, Arial" }}>
    <div style={{ display: "flex" }}>{DANG.map(([n]) => <div key={n} style={{ width: 190, textAlign: "center", fontSize: 19, fontWeight: 800, color: "#333" }}>{n}</div>)}</div>
    {rows.map(({ w, imgs }) => <div key={w.k} style={{ borderBottom: "2px solid #d6cfc2" }}><div style={{ display: "flex" }}>{imgs.map((s, i) => <img key={i} src={s} style={{ width: 190, height: 317 }} />)}</div>
      <div style={{ fontSize: 19, fontWeight: 800, color: "#222", margin: "0 0 4px 8px" }}>{w.ten} <span style={{ fontWeight: 500, color: "#555" }}>– {FIT[w.k]?.vai ?? (w.o.anime ? "nhân vật anime (giữ nguyên đồng phục vẽ sẵn)" : w.o.long ? "mặc định: áo nữ cổ V" : "mặc định: sơ mi/polo/phông")}{w.o.anime ? " · anime" : ""}</span></div></div>)}
  </AbsoluteFill>;
};
