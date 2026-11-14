// Ảnh bìa phim #4 "Lương 30 triệu" (bản kể + ảnh thật): ảnh thật + chữ to.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, getInputProps, staticFile, delayRender, continueRender } from "remotion";
import { F } from "../vang/cards";
const T: Record<string, [string, string, string]> = { A: ["LƯƠNG 30 TRIỆU", "NGÀY 5 CÒN 312K", "dt_nganhang"], B: ["LƯƠNG 30 TRIỆU", "VẪN HẾT TIỀN?", "toanha"], C: ["NGÀY 5 CÒN", "312 NGHÌN", "dem_hn"] };
export const BiaLuong2: React.FC = () => {
  const v = ((getInputProps() as { v?: string }).v ?? "A") as "A" | "B" | "C"; const [h] = useState(() => delayRender("f")); const [ok, setOk] = useState(false);
  useEffect(() => { new FontFace("Be Vietnam Pro", `url(${staticFile("fonts/BeVietnamPro-Black.ttf")})`, { weight: "900" }).load().then((f) => { document.fonts.add(f); setOk(true); continueRender(h); }); }, [h]);
  if (!ok) return null; const [l1, l2, img] = T[v];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <img src={staticFile(`luong/${img}.jpg`)} style={{ width: "100%", height: "100%", objectFit: "cover", filter: "brightness(.8) saturate(1.1)" }} />
      <AbsoluteFill style={{ background: "linear-gradient(90deg, rgba(8,8,20,.9) 0%, rgba(8,8,20,.6) 50%, rgba(8,8,20,0) 75%)" }} />
      <div style={{ position: "absolute", left: 70, top: 150, width: 1300, fontFamily: F, fontWeight: 900 }}>
        <div style={{ fontSize: 140, whiteSpace: "nowrap", lineHeight: 1.02, color: "#fff", WebkitTextStroke: "6px #000", paintOrder: "stroke fill", textShadow: "0 8px 0 rgba(0,0,0,.6)" } as React.CSSProperties}>{l1}</div>
        <div style={{ display: "inline-block", marginTop: 44, fontSize: 128, whiteSpace: "nowrap", lineHeight: 1.05, color: "#ffe14d", background: "#e62117", padding: "14px 30px", borderRadius: 14, transform: "rotate(-2deg)", boxShadow: "0 12px 30px rgba(0,0,0,.6)" }}>{l2}</div>
      </div>
      <div style={{ position: "absolute", right: 60, bottom: 50, fontFamily: F, fontWeight: 900, fontSize: 40, color: "#f5c518", textShadow: "0 3px 8px #000" }}>CHỨNG KHOÁN HUY NGUYỄN</div>
    </AbsoluteFill>
  );
};
