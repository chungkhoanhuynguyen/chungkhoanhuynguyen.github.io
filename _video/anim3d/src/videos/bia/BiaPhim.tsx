// Ảnh bìa chung cho phim kênh chính: ảnh nền + 2 dòng chữ to (dòng 2 nền đỏ). inputProps: { l1, l2, img }
import React, { useEffect, useState } from "react";
import { AbsoluteFill, getInputProps, staticFile, delayRender, continueRender } from "remotion";
import { F } from "../vang/cards";
export const BiaPhim: React.FC = () => {
  const p = getInputProps() as { l1?: string; l2?: string; img?: string }; const [h] = useState(() => delayRender("f")); const [ok, setOk] = useState(false);
  useEffect(() => { new FontFace("Be Vietnam Pro", `url(${staticFile("fonts/BeVietnamPro-Black.ttf")})`, { weight: "900" }).load().then((f) => { document.fonts.add(f); setOk(true); continueRender(h); }); }, [h]);
  if (!ok) return null;
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <img src={staticFile(p.img ?? "bia/gd1.jpg")} style={{ width: "100%", height: "100%", objectFit: "cover", filter: "brightness(.85) saturate(1.15)" }} />
      <AbsoluteFill style={{ background: "linear-gradient(90deg, rgba(8,8,20,.92) 0%, rgba(8,8,20,.65) 48%, rgba(8,8,20,0) 72%)" }} />
      <div style={{ position: "absolute", left: 70, top: 170, width: 1400, fontFamily: F, fontWeight: 900 }}>
        <div style={{ fontSize: 138, whiteSpace: "nowrap", lineHeight: 1.02, color: "#fff", WebkitTextStroke: "6px #000", paintOrder: "stroke fill", textShadow: "0 8px 0 rgba(0,0,0,.6)" } as React.CSSProperties}>{p.l1}</div>
        <div style={{ display: "inline-block", marginTop: 44, fontSize: 124, whiteSpace: "nowrap", lineHeight: 1.05, color: "#ffe14d", background: "#e62117", padding: "14px 30px", borderRadius: 14, transform: "rotate(-2deg)", boxShadow: "0 12px 30px rgba(0,0,0,.6)" }}>{p.l2}</div>
      </div>
      <div style={{ position: "absolute", left: 76, bottom: 56, fontFamily: F, fontWeight: 900, fontSize: 40, color: "#f5c518", textShadow: "0 3px 8px #000" }}>CHỨNG KHOÁN HUY NGUYỄN</div>
    </AbsoluteFill>
  );
};
