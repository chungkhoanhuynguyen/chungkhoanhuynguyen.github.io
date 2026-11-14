// Ảnh bìa A/B/C phim #2 "Hùng Xa Lộ – đu đỉnh đất nền": cảnh 3D thật của phim + chữ to.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, getInputProps, staticFile, delayRender, continueRender } from "remotion";
import { Stage, Shot3D, Cast, V } from "../vang/stage";
import { HOME_X } from "../vang/sets";
import { F } from "../vang/cards";
import { Pose } from "../vang/cast2";
const P = (p: Pose) => () => p;
const fix = (c: V, l: V, f: number): [[V, V, number], [V, V, number]] => [[c, l, f], [c, l, f]];
const SHOTS: Record<string, Shot3D> = {
  A: { set: "field", light: "night", ...((): { from: [V, V, number]; to: [V, V, number] } => { const [a, b] = fix([0.0, 1.45, -0.6], [1.5, 1.3, 1.2], 40); return { from: a, to: b }; })(),
    cast: [{ a: "hung", p: [0.6, 0, 1.2], pose: P({ expr: "shock", acc: ["phone", "glow", "sweat"] }) }] },
  B: { set: "street", light: "night", ...((): { from: [V, V, number]; to: [V, V, number] } => { const [a, b] = fix([HOME_X + 7.2, 1.0, 3.7], [HOME_X + 9.0, 0.75, 5.6], 38); return { from: a, to: b }; })(),
    cast: [{ a: "hung", p: [HOME_X + 8, 0.15, 5.6], pose: P({ expr: "cry", mode: "sit", acc: ["tears", "phone"] }) }] },
  C: { set: "fieldfever", light: "golden", ...((): { from: [V, V, number]; to: [V, V, number] } => { const [a, b] = fix([0.3, 1.45, -6.2], [1.3, 1.2, -2.6], 38); return { from: a, to: b }; })(),
    cast: [{ a: "thang", p: [0.5, 0, -2.6], pose: P({ expr: "smug", side: -1 }) }, { a: "hung", p: [-0.5, 0, -2.6], pose: P({ expr: "shock", side: 1, acc: ["sweat"] }) }] },
};
const T: Record<string, [string, string, string]> = { A: ["ĐẤT NỀN", "MẤT GẦN 4 TỶ", "#e62117"], B: ["VAY 3 TỶ", "SỔ ĐỎ BỐ MẸ", "#e62117"], C: ["MUA 5,5 TỶ", "BÁN 1,8 TỶ", "#e62117"] };
export const BiaDat: React.FC = () => {
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
