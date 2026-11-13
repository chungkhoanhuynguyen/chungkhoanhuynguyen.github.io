// Ảnh bìa A/B/C cho video "Vàng đỉnh": cảnh 3D thật của video + chữ to tương phản (≥110px trên khung 1280x720 tương đương).
import React, { useEffect, useState } from "react";
import { AbsoluteFill, getInputProps, staticFile, delayRender, continueRender } from "remotion";
import { Stage, Shot3D, Cast, V } from "./stage";
import { GOLD_X } from "./sets";
import { F } from "./cards";
import { Pose } from "./cast2";
const P = (p: Pose) => () => p;
const qx = (i: number) => GOLD_X + 1.4 + i * 1.15;
const crowdQ = (from: number, n: number): Cast[] => Array.from({ length: n }, (_, k) => ({ a: "c" + (from + k), p: [qx(from + k), 0.15, 5.25 + ((from + k) % 2) * 0.25] as V, pose: P({ expr: k % 2 ? "worried" : "neutral", acc: k % 3 === 0 ? ["umbrella"] : ["raincoat"], umb: ["#2b4f8a", "#b3263a", "#2f8a52"][k % 3] }) }));
const SHOTS: Record<string, Shot3D> = {
  A: { set: "street", light: "night", rain: true, from: [[qx(20) - 0.9, 1.45, 3.6], [qx(21), 1.3, 5.3], 40], to: [[qx(20) - 0.9, 1.45, 3.6], [qx(21), 1.3, 5.3], 40],
    cast: [...crowdQ(14, 10), { a: "tan", p: [qx(20) - 0.1, 0.15, 4.6], pose: P({ expr: "cry", acc: ["umbrella", "tears"], umb: "#2b2d38", t: 0.3 }) }] },
  B: { set: "room", light: "roomdim", chat: "off", game: false, from: [[-0.4, 1.35, 3.0], [1.3, 1.15, 0.9], 36], to: [[-0.4, 1.35, 3.0], [1.3, 1.15, 0.9], 36],
    cast: [{ a: "tan", p: [1.56, 0.4, 0.9], pose: P({ expr: "shock", mode: "sit", acc: ["paper"] }) }] },
  C: { set: "shop", light: "day", board: "sell", from: [[-0.9, 1.5, 0.9], [-2.9, 1.5, -2.9], 50], to: [[-0.9, 1.5, 0.9], [-2.9, 1.5, -2.9], 50],
    cast: [{ a: "tan", p: [-1.75, 0, -0.15], pose: P({ expr: "shock", acc: ["goldbag"] }) }] },
};
const T: Record<string, [string, string, string]> = { A: ["XẾP HÀNG MUA VÀNG", "MẤT 251 TRIỆU", "#e62117"], B: ["MUA VÀNG BẰNG", "TIỀN CỦA MẸ", "#e62117"], C: ["MUA 184", "BÁN 133,8", "#e62117"] };
export const Bia: React.FC = () => {
  const v = ((getInputProps() as { v?: string }).v ?? "A") as "A" | "B" | "C"; const [h] = useState(() => delayRender("f")); const [ok, setOk] = useState(false);
  useEffect(() => { new FontFace("Be Vietnam Pro", `url(${staticFile("fonts/BeVietnamPro-Black.ttf")})`, { weight: "900" }).load().then((f) => { document.fonts.add(f); setOk(true); continueRender(h); }); }, [h]);
  if (!ok) return null; const [l1, l2, c] = T[v];
  return (
    <AbsoluteFill>
      <Stage set={SHOTS[v].set} runs={[{ a: 0, b: 30, s: SHOTS[v] }]} />
      <AbsoluteFill style={{ background: "linear-gradient(90deg, rgba(8,8,20,.88) 0%, rgba(8,8,20,.55) 48%, rgba(8,8,20,0) 70%)" }} />
      <div style={{ position: "absolute", left: 70, top: 120, width: 1100, fontFamily: F, fontWeight: 900 }}>
        <div style={{ fontSize: 132, lineHeight: 1.02, color: "#fff", WebkitTextStroke: "6px #000", paintOrder: "stroke fill", textShadow: "0 8px 0 rgba(0,0,0,.6)" } as React.CSSProperties}>{l1}</div>
        <div style={{ display: "inline-block", marginTop: 40, fontSize: 128, lineHeight: 1.05, color: "#ffe14d", background: c, padding: "14px 30px", borderRadius: 14, transform: "rotate(-2deg)", boxShadow: "0 12px 30px rgba(0,0,0,.6)" }}>{l2}</div>
      </div>
      <div style={{ position: "absolute", right: 60, bottom: 50, fontFamily: F, fontWeight: 900, fontSize: 40, color: "#f5c518", textShadow: "0 3px 8px #000" }}>CHỨNG KHOÁN HUY NGUYỄN</div>
    </AbsoluteFill>
  );
};
