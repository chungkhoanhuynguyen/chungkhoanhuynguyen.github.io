// Ảnh bìa A/B/C phim #3 "Quang Hà – cảnh báo hạt nhân giả": cảnh 3D thật của phim + chữ to.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, getInputProps, staticFile, delayRender, continueRender } from "remotion";
import { Stage, Shot3D, Cast, V } from "../vang/stage";
import { F } from "../vang/cards";
import { Pose } from "../vang/cast2";
const P = (p: Pose) => () => p;
const fix = (c: V, l: V, f: number): [[V, V, number], [V, V, number]] => [[c, l, f], [c, l, f]];
const SHOTS: Record<string, Shot3D> = {
  A: { set: "room", light: "roomdim", chat: "off", game: false, ...((): { from: [V, V, number]; to: [V, V, number] } => { const [a, b] = fix([2.1, 1.25, 2.4], [1.56, 1.0, 0.9], 34); return { from: a, to: b }; })(),
    cast: [{ a: "quang", p: [1.56, 0.4, 0.9], pose: P({ expr: "shock", mode: "sit", acc: ["phone", "glow", "sweat"] }) }] },
  B: { set: "photo", light: "dawn", bg: "hn/gold_shop.jpg", bgFit: [0.35, 0.55], ...((): { from: [V, V, number]; to: [V, V, number] } => { const [a, b] = fix([0.4, 1.5, -5.6], [0.4, 1.3, 2.2], 44); return { from: a, to: b }; })(),
    cast: [0, 1, 2, 3, 4, 5].map((i) => ({ a: "c" + (40 + i), p: [1.7 + (i + 1) * 0.42, 0, 0.2 + (i + 1) * 0.7] as V, pose: P({ expr: i % 2 ? "worried" : "nervous" }) })).concat([{ a: "quang", p: [1.7, 0, 0.2] as V, pose: P({ expr: "worried", acc: ["sweat"] }) }]) },
  C: { set: "photo", light: "night", bg: "hn/hanoi_night.jpg", bgFit: [0.6, 0.45], ...((): { from: [V, V, number]; to: [V, V, number] } => { const [a, b] = fix([0, 1.6, -8], [0, 1.9, 6], 46); return { from: a, to: b }; })(), cast: [] },
};
const T: Record<string, [string, string, string]> = { A: ["BÁN SẠCH 1,2 TỶ", "VÌ TIN TẬN THẾ", "#e62117"], B: ["NỬA ĐÊM", "XẾP HÀNG MUA VÀNG", "#e62117"], C: ["CẢNH BÁO", "HẠT NHÂN GIẢ", "#e62117"] };
export const BiaHn: React.FC = () => {
  const v = ((getInputProps() as { v?: string }).v ?? "A") as "A" | "B" | "C"; const [h] = useState(() => delayRender("f")); const [ok, setOk] = useState(false);
  useEffect(() => { new FontFace("Be Vietnam Pro", `url(${staticFile("fonts/BeVietnamPro-Black.ttf")})`, { weight: "900" }).load().then((f) => { document.fonts.add(f); setOk(true); continueRender(h); }); }, [h]);
  if (!ok) return null; const [l1, l2, c] = T[v];
  return (
    <AbsoluteFill>
      <Stage set={SHOTS[v].set} runs={[{ a: 0, b: 30, s: SHOTS[v] }]} />
      <AbsoluteFill style={{ background: "linear-gradient(90deg, rgba(8,8,20,.88) 0%, rgba(8,8,20,.55) 48%, rgba(8,8,20,0) 70%)" }} />
      <div style={{ position: "absolute", left: 70, top: 120, width: 1100, fontFamily: F, fontWeight: 900 }}>
        <div style={{ fontSize: 132, whiteSpace: "nowrap", lineHeight: 1.02, color: "#fff", WebkitTextStroke: "6px #000", paintOrder: "stroke fill", textShadow: "0 8px 0 rgba(0,0,0,.6)" } as React.CSSProperties}>{l1}</div>
        <div style={{ display: "inline-block", marginTop: 40, fontSize: 128, lineHeight: 1.05, color: "#ffe14d", background: c, padding: "14px 30px", borderRadius: 14, transform: "rotate(-2deg)", boxShadow: "0 12px 30px rgba(0,0,0,.6)" }}>{l2}</div>
      </div>
      <div style={{ position: "absolute", right: 60, bottom: 50, fontFamily: F, fontWeight: 900, fontSize: 40, color: "#f5c518", textShadow: "0 3px 8px #000" }}>CHỨNG KHOÁN HUY NGUYỄN</div>
    </AbsoluteFill>
  );
};
