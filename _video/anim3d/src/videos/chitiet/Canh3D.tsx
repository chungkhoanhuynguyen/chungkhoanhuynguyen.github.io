// CẢNH 3D CHO VIDEO TIN NÓNG (render.py, 'k': '3d'): một đoạn 3D đúng thời lượng câu đọc, dựng từ inputProps.
// props: { set, light?, cam: { from: [pos, look, fov], to?: [...] }, cast: [{ a, p, to?, act, side?, expr?, lean? }], xe?: [{ k, p, ry }], frames, fps }
// act (hành động cơ bản): "noi" (đứng nói), "dienthoai" (xem điện thoại; + ngoi: true để ngồi), "omdau" (ôm mặt/đầu), "di" (đi từ p tới to),
//   "chitay" (chỉ tay, nhìn nghiêng), "ngoi" (ngồi yên), "dung" (đứng yên), "goi" (nghe điện thoại).
import React from "react";
import { AbsoluteFill } from "remotion";
import { Stage, Run, Cast, V, SetKey } from "./stage_ct";
import { Pose, Acc } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { LK } from "../vang/look";

export type Act = "noi" | "dienthoai" | "omdau" | "di" | "chitay" | "ngoi" | "dung" | "goi" | "giay";
// acc: đồ cầm thêm (paper, cup, box, sweat...); giay = cầm giấy tờ + nói
export type CastIn = { a: string; p: V; to?: V; act?: Act; side?: 1 | -1; expr?: Expr; ngoi?: boolean; lean?: number; ride?: boolean; acc?: Acc[] };
export type Canh3DProps = { set: SetKey; light?: LK; cam: { from: [V, V, number]; to?: [V, V, number]; ease?: "sm" | "lin" | "out" }; cast: CastIn[]; frames: number; fps?: number; px?: number; tat?: string[] };

const bl = (t: number, k = 71) => Math.floor(t * 30) % k < 4;
const NOI: Expr[] = ["grin", "neutral", "smile", "neutral"];
// 20/11 (anh Huy: lo lắng thì không cười): có expr thì khi nói chỉ đổi qua lại giữa expr và nét "mở miệng" CÙNG cảm xúc
const TALK: Partial<Record<Expr, Expr>> = { worried: "nervous", nervous: "worried", stern: "neutral", pained: "worried", sad: "worried", smile: "grin", grin: "smile", relief: "relief_open", relief_open: "relief", neutral: "smile_closed", shock: "nervous", smug: "grin" };
const VUI = new Set<Expr>(["smile", "grin", "relief", "relief_open", "smug", "laugh"]);
const noiExpr = (c: CastIn, t: number, ph: number): Expr => { const k = Math.floor(t * 2.6 + ph); return c.expr ? (k % 2 ? TALK[c.expr] ?? c.expr : c.expr) : NOI[k % NOI.length]; };
export function poseOf(c: CastIn, i: number): Cast["pose"] {
  const side = c.ngoi ? undefined : c.side, ph = i * 0.37;
  return (t: number): Pose => {
    const base: Pose = { expr: c.expr ?? "neutral", blink: bl(t + ph * 3), side, mode: c.ngoi ? "sit" : "stand", acc: c.acc };
    const A = (x: Acc[]) => [...x, ...(c.acc ?? [])];
    switch (c.act) {
      case "noi": return { ...base, expr: noiExpr(c, t, ph), wave: (!c.expr || VUI.has(c.expr)) && !c.acc && Math.floor(t * 0.7 + ph) % 3 === 0 ? 1 : undefined };
      case "giay": return { ...base, expr: noiExpr(c, t, ph), acc: A(["paper"]) };
      case "dienthoai": return { ...base, expr: c.expr ?? "worried", acc: A(["phone"]), side: undefined };
      case "goi": return { ...base, expr: c.expr ?? "nervous", acc: A(["phone"]) };
      case "omdau": return { ...base, expr: c.expr ?? "pained", prop: "face", side: undefined };
      case "di": return { ...base, expr: c.expr ?? "neutral", mode: "stroll", phase: (t * 1.1 + ph) % 1, side: side ?? 1 };
      case "chitay": return { ...base, expr: noiExpr({ ...c, expr: c.expr ?? "stern" }, t, ph), side: side ?? 1, reach: [0.6, 0.15 + 0.05 * Math.sin(t * 2 + ph)] };
      default: return base;
    }
  };
}
export const Canh3D: React.FC<Canh3DProps> = (p) => {
  const cast: Cast[] = (p.cast ?? []).map((c, i) => ({ a: c.a, p: c.p, to: c.to, pose: poseOf(c, i), ride: c.ride, lean: c.lean }));
  const runs: Run[] = [{ a: 0, b: p.frames, s: { set: p.set, light: p.light ?? "day", from: p.cam.from, to: p.cam.to ?? p.cam.from, cast, ease: p.cam.ease ?? "sm" } }];
  return <AbsoluteFill style={{ background: "#000" }}><Stage set={p.set} runs={runs} chiTiet fps={p.fps ?? 30} px={p.px} tat={p.tat} /></AbsoluteFill>;
};
export const CANH3D_MAU: Canh3DProps = { set: "sapvai", light: "golden", cam: { from: [[0.2, 1.55, 4.2], [0.2, 1.0, -1.0], 40], to: [[0.1, 1.45, 3.4], [0.2, 1.0, -1.0], 36] }, cast: [{ a: "thuyto", p: [0.9, 0, -0.4], act: "dienthoai", ngoi: true }], frames: 60, fps: 30 };
