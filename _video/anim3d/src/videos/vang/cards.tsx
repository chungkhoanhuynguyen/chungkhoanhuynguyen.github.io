// Thẻ "form cũ" (điện thoại, biểu đồ giá thật, hoá đơn, sổ tay đóng dấu, chat, TV, tin nóng, bài học, kêu gọi) + lớp phủ trên cảnh 3D.
import React from "react";
import { AbsoluteFill } from "remotion";
export const F = "'Be Vietnam Pro', 'DejaVu Sans', Arial, sans-serif";
export const sm = (t: number) => { t = Math.max(0, Math.min(1, t)); return t * t * t * (t * (t * 6 - 15) + 10); };
const pop = (t: number) => { t = Math.max(0, Math.min(1, t)); const c = 1.7; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2; };
const vn = (x: number, d = 0) => x.toLocaleString("vi-VN", { minimumFractionDigits: d, maximumFractionDigits: d });

/** nền tối có bokeh vàng trôi chậm */
export const Bg: React.FC<{ t: number; hue?: "navy" | "red" | "warm" | "night" }> = ({ t, hue = "navy" }) => {
  const G = { navy: ["#0b1124", "#1b2550"], red: ["#1a0608", "#4a0d14"], warm: ["#1a1208", "#3d2a10"], night: ["#05070f", "#141a36"] }[hue];
  return (
    <AbsoluteFill style={{ background: `radial-gradient(120% 90% at 30% 20%, ${G[1]} 0%, ${G[0]} 70%)`, overflow: "hidden" }}>
      {Array.from({ length: 14 }).map((_, i) => { const x = (i * 137) % 1920, y = (i * 263) % 1080, r = 40 + (i * 37) % 120;
        return <div key={i} style={{ position: "absolute", left: x + Math.sin(t * 0.3 + i) * 40, top: y + Math.cos(t * 0.25 + i) * 30, width: r, height: r, borderRadius: "50%", background: hue === "red" ? "rgba(255,80,80,.07)" : "rgba(255,200,90,.07)", filter: "blur(6px)" }} />; })}
    </AbsoluteFill>
  );
};

// ---------------- phone lock screen with notifications ----------------
export type Notif = { app: string; col: string; title: string; body: string; at: number };
export const PhoneCard: React.FC<{ t: number; time: string; date: string; notifs: Notif[]; quote?: [string, string]; qAt?: number; hue?: "navy" | "red" | "night" }> = ({ t, time, date, notifs, quote, qAt = 1.2, hue = "night" }) => {
  const k = sm(t / 0.5), q = sm((t - qAt) / 0.45);
  return (
    <AbsoluteFill>
      <Bg t={t} hue={hue} />
      <div style={{ position: "absolute", left: 150, top: 46 + (1 - k) * 90, width: 470, height: 840, borderRadius: 66, background: "linear-gradient(180deg,#141a2c,#2b2238)", border: "7px solid #3b4058", boxShadow: "0 30px 80px rgba(0,0,0,.6)", fontFamily: F, color: "#fff", textAlign: "center", opacity: k, transform: `rotate(${-2 + Math.sin(t * 0.7) * 0.4}deg)` }}>
        <div style={{ position: "absolute", left: "50%", top: 22, width: 128, height: 36, marginLeft: -64, borderRadius: 18, background: "#05060a" }} />
        <div style={{ marginTop: 80, fontSize: 118, fontWeight: 800, letterSpacing: -2 }}>{time}</div>
        <div style={{ fontSize: 32, opacity: 0.85, fontWeight: 500 }}>{date}</div>
        {notifs.map((n, i) => { const a = pop((t - n.at) / 0.35); if (t < n.at) return null; const shake = t - n.at < 0.5 ? Math.sin((t - n.at) * 60) * 6 * (1 - (t - n.at) / 0.5) : 0;
          return (
            <div key={i} style={{ margin: "26px 24px 0", padding: "20px 22px", borderRadius: 28, background: "rgba(236,239,246,.96)", color: "#15181f", textAlign: "left", transform: `translateX(${shake}px) scale(${0.85 + 0.15 * a})`, opacity: Math.min(1, a) }}>
              <div style={{ display: "flex", alignItems: "center", fontSize: 22, color: "#5b6272", fontWeight: 700 }}>
                <span style={{ width: 32, height: 32, borderRadius: 9, background: n.col, color: "#fff", fontWeight: 900, textAlign: "center", lineHeight: "32px", marginRight: 10, fontSize: 18 }}>{n.app[0]}</span>{n.app.toUpperCase()}<span style={{ marginLeft: "auto", fontWeight: 500 }}>bây giờ</span></div>
              <div style={{ fontSize: 29, fontWeight: 800, marginTop: 8 }}>{n.title}</div>
              <div style={{ fontSize: 25, lineHeight: 1.3, marginTop: 4 }}>{n.body}</div>
            </div>); })}
      </div>
      {quote && (
        <div style={{ position: "absolute", left: 730, top: 340, fontFamily: F, fontWeight: 900, fontSize: 100, lineHeight: 1.12, opacity: q, transform: `translateY(${(1 - q) * 30}px)`, textShadow: "0 6px 0 rgba(0,0,0,.45)" }}>
          <div style={{ color: "#fff" }}>{quote[0]}</div><div style={{ color: "#ff4d3d" }}>{quote[1]}</div>
          <div style={{ width: 130, height: 10, background: "#f5c518", marginTop: 22 }} />
        </div>)}
    </AbsoluteFill>
  );
};

// ---------------- price chart (real data) ----------------
export type Mark = { i: number; label: string; col?: string; at?: number; up?: boolean };
export const ChartCard: React.FC<{ t: number; d: number; title: string; sub: string; data: [string, number][]; unit: string; scale?: number; marks?: Mark[]; mode?: "up" | "down" | "auto"; reveal?: number; src: string; bracket?: { a: number; b: number; label: string; at: number }; dec?: number }> = ({ t, d, title, sub, data, unit, scale = 1000, marks = [], mode = "auto", reveal = 0.7, src, bracket, dec = 1 }) => {
  const W = 1500, H = 640, P = { l: 120, r: 60, t: 40, b: 80 }, vals = data.map((x) => x[1] / scale), mx = Math.max(...vals), mn = Math.min(...vals), pad = (mx - mn) * 0.15 || 1;
  const lo = mn - pad, hi = mx + pad, X = (i: number) => P.l + (i / (data.length - 1)) * (W - P.l - P.r), Y = (v: number) => P.t + (1 - (v - lo) / (hi - lo)) * (H - P.t - P.b);
  const pr = sm((t - 0.35) / Math.max(0.8, Math.min(d * 0.55, 6) * reveal)), n = pr * (data.length - 1), k = sm(t / 0.45);
  const pts: string[] = []; for (let i = 0; i <= Math.floor(n); i++) pts.push(`${X(i)},${Y(vals[i])}`);
  const fi = Math.floor(n), fr = n - fi; let hx = X(0), hy = Y(vals[0]);
  if (fi < data.length - 1) { hx = X(fi) + (X(fi + 1) - X(fi)) * fr; hy = Y(vals[fi] + (vals[fi + 1] - vals[fi]) * fr); pts.push(`${hx},${hy}`); } else { hx = X(data.length - 1); hy = Y(vals[data.length - 1]); }
  const last = fi < data.length - 1 ? vals[fi] + (vals[fi + 1] - vals[fi]) * fr : vals[vals.length - 1];
  const up = mode === "up" ? true : mode === "down" ? false : last >= vals[0];
  const col = up ? "#2bd17e" : "#ff4d5e";
  const grid = 5, ticks = Array.from({ length: grid + 1 }, (_, i) => lo + ((hi - lo) * i) / grid);
  return (
    <AbsoluteFill>
      <Bg t={t} hue={up ? "navy" : "red"} />
      <div style={{ position: "absolute", left: 160, top: 110, fontFamily: F, color: "#fff", opacity: k, transform: `translateY(${(1 - k) * 20}px)` }}>
        <div style={{ fontSize: 58, fontWeight: 900 }}>{title}</div>
        <div style={{ fontSize: 30, fontWeight: 500, color: "#b8c2d8", marginTop: 4 }}>{sub}</div>
      </div>
      <div style={{ position: "absolute", right: 170, top: 110, fontFamily: F, textAlign: "right", opacity: k }}>
        <div style={{ fontSize: 96, fontWeight: 900, color: col, lineHeight: 1 }}>{vn(last, dec)}</div>
        <div style={{ fontSize: 26, color: "#b8c2d8", fontWeight: 600 }}>{unit}</div>
      </div>
      <svg width={W} height={H} style={{ position: "absolute", left: 210, top: 300, opacity: k, overflow: "visible" }}>
        {ticks.map((v, i) => <g key={i}><line x1={P.l} x2={W - P.r} y1={Y(v)} y2={Y(v)} stroke="rgba(255,255,255,.09)" strokeWidth={2} /><text x={P.l - 16} y={Y(v) + 9} fill="#8f9ab3" fontSize={24} fontFamily={F} textAnchor="end">{vn(v, 0)}</text></g>)}
        {data.map((x, i) => (i % Math.ceil(data.length / 8) === 0 || i === data.length - 1) && <text key={i} x={X(i)} y={H - P.b + 42} fill="#8f9ab3" fontSize={24} fontFamily={F} textAnchor="middle">{x[0]}</text>)}
        <polyline points={pts.join(" ") + ` ${hx},${H - P.b} ${X(0)},${H - P.b}`} fill={up ? "rgba(43,209,126,.12)" : "rgba(255,77,94,.12)"} stroke="none" />
        <polyline points={pts.join(" ")} fill="none" stroke={col} strokeWidth={8} strokeLinejoin="round" strokeLinecap="round" />
        <circle cx={hx} cy={hy} r={13} fill={col} stroke="#fff" strokeWidth={4} />
        {bracket && t > bracket.at && (() => { const a = sm((t - bracket.at) / 0.4), x1 = X(bracket.a), x2 = X(bracket.b), y1 = Y(vals[bracket.a]), y2 = Y(vals[bracket.b]);
          return <g opacity={a}><line x1={x2 + 40} x2={x2 + 40} y1={y1} y2={y2} stroke="#ff4d5e" strokeWidth={6} /><line x1={x1} x2={x2 + 52} y1={y1} y2={y1} stroke="#ff4d5e" strokeWidth={3} strokeDasharray="10 8" />
            <text x={x2 > W - 500 ? x2 - 30 : x2 + 64} y={(y1 + y2) / 2 + 20} textAnchor={x2 > W - 500 ? "end" : "start"} fill="#ff4d5e" fontSize={58} fontWeight={900} fontFamily={F} stroke="#1a0608" strokeWidth={8} paintOrder="stroke">{bracket.label}</text></g>; })()}
        {marks.map((m, j) => { const at = m.at ?? 0; if (n < m.i - 0.01 || t < at) return null; const a = pop((t - Math.max(at, 0.35 + (m.i / (data.length - 1)) * 0)) / 0.35), mx2 = X(m.i), my = Y(vals[m.i]), c = m.col ?? "#f5c518", upL = m.up ?? true;
          return <g key={j} opacity={Math.min(1, a)}><circle cx={mx2} cy={my} r={16 * Math.min(1.2, a)} fill="none" stroke={c} strokeWidth={6} />
            <rect x={mx2 - 150} y={upL ? my - 110 : my + 34} width={300} height={70} rx={16} fill={c} /><text x={mx2} y={upL ? my - 62 : my + 82} textAnchor="middle" fontSize={34} fontWeight={900} fill="#111" fontFamily={F}>{m.label}</text></g>; })}
      </svg>
      <div style={{ position: "absolute", left: 160, bottom: 200, fontFamily: F, fontSize: 22, color: "#7f8aa5" }}>{src}</div>
    </AbsoluteFill>
  );
};

// ---------------- paper: receipt / notebook with stamp ----------------
export type PLine = { text: string; at: number; big?: boolean; col?: string; under?: boolean };
export const PaperCard: React.FC<{ t: number; title: string; sub?: string; lines: PLine[]; stamp?: { text: string; at: number; col?: string }; sign?: string; kind?: "receipt" | "note"; side?: React.ReactNode; hue?: "navy" | "red" | "warm" | "night" }> = ({ t, title, sub, lines, stamp, sign, kind = "note", side, hue = "warm" }) => {
  const k = sm(t / 0.5), st = stamp ? sm((t - stamp.at) / 0.22) : 0, sc = stamp ? 1.8 - 0.8 * st : 1, shake = stamp && t - stamp.at > 0 && t - stamp.at < 0.25 ? Math.sin((t - stamp.at) * 90) * 5 : 0;
  return (
    <AbsoluteFill>
      <Bg t={t} hue={hue} />
      <div style={{ position: "absolute", left: 160, top: 46 + (1 - k) * 120, width: 760, height: 840, backgroundColor: kind === "receipt" ? "#fbf8ef" : "#f3ecdc", transform: `rotate(${kind === "receipt" ? 1.5 : -2}deg) translate(${shake}px,${shake * 0.6}px)`, boxShadow: "0 30px 70px rgba(0,0,0,.55)", opacity: k, fontFamily: F, color: "#1c1b19", padding: "56px 56px", boxSizing: "border-box",
        backgroundImage: kind === "note" ? "repeating-linear-gradient(180deg, transparent 0 63px, rgba(70,110,180,.18) 63px 65px), linear-gradient(180deg,#f6f0e1,#ece4d2)" : "linear-gradient(180deg,#fffdf6,#f3eee2)" }}>
        <div style={{ fontSize: 50, fontWeight: 900, textAlign: "center", letterSpacing: 1 }}>{title}</div>
        {sub && <div style={{ fontSize: 26, textAlign: "center", color: "#6b665c", marginTop: 6 }}>{sub}</div>}
        {kind === "receipt" && <div style={{ borderTop: "3px dashed #9c958a", margin: "26px 0 10px" }} />}
        <div style={{ marginTop: 34 }}>
          {lines.map((l, i) => { const a = sm((t - l.at) / 0.3); return (
            <div key={i} style={{ marginTop: l.big ? 40 : 26, fontSize: l.big ? 52 : 36, fontWeight: l.big ? 900 : 700, color: l.col ?? "#1c1b19", opacity: a, transform: `translateX(${(1 - a) * -20}px)` }}>
              <span style={{ borderBottom: l.under ? "5px solid #e23b2e" : undefined, paddingBottom: 4, backgroundSize: `${a * 100}% 100%` }}>{l.text}</span></div>); })}
        </div>
        {sign && <div style={{ position: "absolute", left: 56, bottom: 64, width: 250, borderTop: "3px solid #8b857a", fontSize: 24, color: "#6b665c", paddingTop: 8, textAlign: "center" }}>{sign}</div>}
        {stamp && t > stamp.at && <div style={{ position: "absolute", right: 46, bottom: 50, width: 260, height: 260, borderRadius: "50%", border: `9px solid ${stamp.col ?? "#d8372b"}`, color: stamp.col ?? "#d8372b", fontSize: 40, fontWeight: 900, display: "flex", alignItems: "center", justifyContent: "center", textAlign: "center", lineHeight: 1.1, opacity: st * 0.92, transform: `rotate(-14deg) scale(${sc})`, padding: 20, boxSizing: "border-box" }}>{stamp.text}</div>}
      </div>
      {side && <div style={{ position: "absolute", left: 1010, top: 0, width: 800, height: 1080, display: "flex", alignItems: "center" }}>{side}</div>}
    </AbsoluteFill>
  );
};
export const SideText: React.FC<{ t: number; at: number; l1: string; l2?: string; c2?: string }> = ({ t, at, l1, l2, c2 = "#ff4d3d" }) => { const q = sm((t - at) / 0.45);
  return <div style={{ fontFamily: F, fontWeight: 900, fontSize: 92, lineHeight: 1.12, opacity: q, transform: `translateY(${(1 - q) * 30}px)`, textShadow: "0 6px 0 rgba(0,0,0,.45)" }}><div style={{ color: "#fff" }}>{l1}</div>{l2 && <div style={{ color: c2 }}>{l2}</div>}<div style={{ width: 130, height: 10, background: "#f5c518", marginTop: 22 }} /></div>; };

// ---------------- chat (messenger) ----------------
export type Msg = { who: string; text: string; at: number; me?: boolean; col?: string };
export const ChatCard: React.FC<{ t: number; title: string; msgs: Msg[]; side?: React.ReactNode }> = ({ t, title, msgs, side }) => {
  const k = sm(t / 0.45);
  return (
    <AbsoluteFill>
      <Bg t={t} hue="night" />
      <div style={{ position: "absolute", left: 180, top: 50 + (1 - k) * 80, width: 640, height: 830, borderRadius: 56, background: "#eef1f6", border: "7px solid #2d3246", overflow: "hidden", opacity: k, fontFamily: F, boxShadow: "0 30px 80px rgba(0,0,0,.6)" }}>
        <div style={{ height: 120, background: "#2f6fd1", color: "#fff", display: "flex", alignItems: "center", padding: "0 34px", fontSize: 36, fontWeight: 800 }}><span style={{ width: 64, height: 64, borderRadius: 32, background: "#ffffff33", marginRight: 20 }} />{title}</div>
        <div style={{ padding: "26px 26px" }}>
          {msgs.filter((m) => t >= m.at).map((m, i) => { const a = pop((t - m.at) / 0.3);
            return <div key={i} style={{ display: "flex", flexDirection: "column", alignItems: m.me ? "flex-end" : "flex-start", marginTop: 18, transform: `scale(${0.8 + 0.2 * Math.min(1, a)})`, transformOrigin: m.me ? "right" : "left", opacity: Math.min(1, a) }}>
              {!m.me && <div style={{ fontSize: 22, color: "#6b7385", fontWeight: 700, margin: "0 0 4px 12px" }}>{m.who}</div>}
              <div style={{ maxWidth: 470, padding: "18px 24px", borderRadius: 30, background: m.me ? "#2f6fd1" : "#fff", color: m.me ? "#fff" : "#151820", fontSize: 32, fontWeight: 600, lineHeight: 1.3, boxShadow: "0 4px 10px rgba(0,0,0,.08)" }}>{m.text}</div></div>; })}
        </div>
      </div>
      {side && <div style={{ position: "absolute", left: 900, top: 0, width: 900, height: 1080, display: "flex", alignItems: "center" }}>{side}</div>}
    </AbsoluteFill>
  );
};

// ---------------- TV: phim truyền hình mẹ chồng nàng dâu (minh hoạ, không phải cảnh phim thật) ----------------
export const TvCard: React.FC<{ t: number; quote: string; qAt: number }> = ({ t, quote, qAt }) => {
  const k = sm(t / 0.5), q = sm((t - qAt) / 0.4), flick = 0.92 + 0.08 * Math.sin(t * 50);
  return (
    <AbsoluteFill style={{ filter: "sepia(.35)" }}>
      <Bg t={t} hue="warm" />
      <div style={{ position: "absolute", left: 400, top: 40 + (1 - k) * 60, width: 1120, height: 640, borderRadius: 40, background: "#3a2a1e", boxShadow: "0 40px 90px rgba(0,0,0,.6)", opacity: k }}>
        <div style={{ position: "absolute", left: 40, top: 40, width: 1040, height: 560, borderRadius: 30, overflow: "hidden", background: "linear-gradient(180deg,#e9c99a,#b88a5a)", opacity: flick }}>
          {/* phòng khách + hai bóng người */}
          <div style={{ position: "absolute", left: 0, bottom: 0, width: 1100, height: 150, background: "#7a5532" }} />
          <div style={{ position: "absolute", left: 120, top: 70, width: 260, height: 200, background: "#5c3d22", borderRadius: 10 }} />
          {[[300, "#2b1d16", 1.0], [700, "#3b2a22", 0.95]].map(([x, c, s], i) => <div key={i} style={{ position: "absolute", left: x as number, bottom: 110, width: 170 * (s as number), height: 380 * (s as number) }}>
            <div style={{ width: 110, height: 110, borderRadius: "50%", background: c as string, margin: "0 auto" }} /><div style={{ width: 170, height: 270, borderRadius: "80px 80px 20px 20px", background: c as string, marginTop: 6 }} /></div>)}
          <div style={{ position: "absolute", left: 30, top: 24, fontFamily: F, fontWeight: 800, fontSize: 28, color: "#fff", background: "rgba(200,30,40,.85)", padding: "6px 16px", borderRadius: 8 }}>PHIM TRUYỀN HÌNH · 21:40</div>
          <div style={{ position: "absolute", left: 0, top: 0, width: "100%", height: "100%", backgroundImage: "repeating-linear-gradient(180deg, rgba(0,0,0,.08) 0 2px, transparent 2px 5px)" }} />
        </div>
      </div>
      <div style={{ position: "absolute", left: 300, top: 560, width: 1320, padding: "30px 50px", borderRadius: 40, background: "#fffaf0", color: "#1c1b19", fontFamily: F, fontSize: 52, fontWeight: 800, lineHeight: 1.25, boxShadow: "0 20px 50px rgba(0,0,0,.5)", opacity: q, transform: `scale(${0.9 + 0.1 * q})`, textAlign: "center" }}>{quote}
        <div style={{ fontSize: 24, fontWeight: 500, color: "#7b7466", marginTop: 12 }}>(lời thoại đại ý – hình minh hoạ)</div></div>
    </AbsoluteFill>
  );
};

// ---------------- title / big quote ----------------
export const TitleCard: React.FC<{ t: number; kicker?: string; l1: string; l2: string; sub?: string; hue?: "navy" | "red" | "warm" | "night" }> = ({ t, kicker, l1, l2, sub, hue = "red" }) => {
  const a = sm(t / 0.4), b = sm((t - 0.35) / 0.4), c = sm((t - 0.8) / 0.4);
  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", textAlign: "center", fontFamily: F }}>
      <Bg t={t} hue={hue} />
      {Array.from({ length: 16 }).map((_, i) => { const y = ((t * (120 + i * 13) + i * 97) % 1300) - 150; return <div key={i} style={{ position: "absolute", left: (i * 121) % 1920, top: y, width: 70, height: 34, borderRadius: 6, background: "linear-gradient(180deg,#ffe27a,#d59a1e)", transform: `rotate(${i * 23 + t * 40}deg)`, opacity: 0.35, boxShadow: "0 0 20px rgba(255,200,80,.5)" }} />; })}
      <div style={{ position: "relative" }}>
        {kicker && <div style={{ fontSize: 40, fontWeight: 700, color: "#f5c518", letterSpacing: 6, opacity: a }}>{kicker}</div>}
        <div style={{ fontSize: 128, fontWeight: 900, color: "#fff", lineHeight: 1.05, marginTop: 14, opacity: a, transform: `scale(${1.15 - 0.15 * a})`, textShadow: "0 8px 0 rgba(0,0,0,.5)" }}>{l1}</div>
        <div style={{ fontSize: 140, fontWeight: 900, color: "#ffcf3a", lineHeight: 1.05, opacity: b, transform: `scale(${1.2 - 0.2 * b})`, textShadow: "0 8px 0 rgba(0,0,0,.5)" }}>{l2}</div>
        {sub && <div style={{ fontSize: 40, color: "#e8dfe0", fontWeight: 600, marginTop: 30, opacity: c }}>{sub}</div>}
      </div>
    </AbsoluteFill>
  );
};

// ---------------- news headlines ----------------
export const NewsCard: React.FC<{ t: number; items: { src: string; head: string; at: number; col?: string }[]; tag: string }> = ({ t, items, tag }) => (
  <AbsoluteFill style={{ fontFamily: F }}>
    <Bg t={t} hue="red" />
    <div style={{ position: "absolute", left: 160, top: 90, fontSize: 40, fontWeight: 900, color: "#fff", background: "#d8212f", padding: "10px 26px", borderRadius: 10, opacity: sm(t / 0.3) }}>{tag}</div>
    {items.map((it, i) => { const a = pop((t - it.at) / 0.35); if (t < it.at) return null;
      return <div key={i} style={{ position: "absolute", left: 160 + i * 40, top: 220 + i * 205, width: 1480, padding: "30px 40px", borderRadius: 26, background: "rgba(250,248,244,.97)", boxShadow: "0 18px 40px rgba(0,0,0,.45)", transform: `translateX(${(1 - Math.min(1, a)) * 120}px) scale(${0.9 + 0.1 * Math.min(1, a)})`, opacity: Math.min(1, a) }}>
        <div style={{ fontSize: 24, fontWeight: 800, color: it.col ?? "#b3131f", letterSpacing: 2 }}>{it.src}</div>
        <div style={{ fontSize: 50, fontWeight: 900, color: "#15161c", lineHeight: 1.2, marginTop: 6 }}>{it.head}</div></div>; })}
  </AbsoluteFill>
);

// ---------------- lessons ----------------
export const LessonCard: React.FC<{ t: number; items: { n: string; head: string; body: string; at: number; icon: string }[]; title: string; tAt?: number }> = ({ t, items, title, tAt = 0 }) => (
  <AbsoluteFill style={{ fontFamily: F }}>
    <Bg t={t} hue="navy" />
    <div style={{ position: "absolute", left: 160, top: 90, fontSize: 64, fontWeight: 900, color: "#fff", opacity: sm((t - tAt) / 0.4) }}>{title}</div>
    {items.map((it, i) => { const a = pop((t - it.at) / 0.4); if (t < it.at) return null;
      return <div key={i} style={{ position: "absolute", left: 160, top: (items.length > 3 ? 190 : 230) + i * (items.length > 3 ? 172 : 230), width: 1600, height: items.length > 3 ? 155 : 200, borderRadius: 30, background: "rgba(255,255,255,.07)", border: "3px solid rgba(245,197,24,.6)", display: "flex", alignItems: "center", opacity: Math.min(1, a), transform: `translateY(${(1 - Math.min(1, a)) * 40}px)` }}>
        <div style={{ width: 160, fontSize: 110, fontWeight: 900, color: "#f5c518", textAlign: "center" }}>{it.n}</div>
        <div style={{ fontSize: 80, width: 120, textAlign: "center" }}>{it.icon}</div>
        <div style={{ marginLeft: 20 }}><div style={{ fontSize: 52, fontWeight: 900, color: "#fff" }}>{it.head}</div><div style={{ fontSize: 32, fontWeight: 500, color: "#c5cde0", marginTop: 6 }}>{it.body}</div></div></div>; })}
  </AbsoluteFill>
);

// ---------------- money split bar ----------------
export const SplitCard: React.FC<{ t: number; title: string; parts: { label: string; v: number; col: string; at: number }[]; total: string }> = ({ t, title, parts, total }) => {
  const sum = parts.reduce((s, p) => s + p.v, 0);
  return (
    <AbsoluteFill style={{ fontFamily: F }}>
      <Bg t={t} hue="night" />
      <div style={{ position: "absolute", left: 160, top: 130, fontSize: 60, fontWeight: 900, color: "#fff", opacity: sm(t / 0.4) }}>{title}</div>
      <div style={{ position: "absolute", right: 160, top: 120, fontSize: 96, fontWeight: 900, color: "#f5c518", opacity: sm(t / 0.4) }}>{total}</div>
      <div style={{ position: "absolute", left: 160, top: 330, width: 1600, height: 170, borderRadius: 26, background: "rgba(255,255,255,.08)", display: "flex", overflow: "hidden" }}>
        {parts.map((p, i) => { const a = sm((t - p.at) / 0.6); return <div key={i} style={{ width: `${(p.v / sum) * 100 * a}%`, background: p.col, height: "100%", display: "flex", alignItems: "center", justifyContent: "center", color: "#fff", fontSize: 54, fontWeight: 900, whiteSpace: "nowrap", overflow: "hidden" }}>{a > 0.6 ? `${p.v} triệu` : ""}</div>; })}
      </div>
      {parts.map((p, i) => { const a = sm((t - p.at - 0.3) / 0.4); return <div key={i} style={{ position: "absolute", left: 160, top: 560 + i * 120, display: "flex", alignItems: "center", opacity: a, transform: `translateX(${(1 - a) * -30}px)` }}>
        <div style={{ width: 54, height: 54, borderRadius: 12, background: p.col, marginRight: 26 }} /><div style={{ fontSize: 50, fontWeight: 800, color: "#fff" }}>{p.label}</div><div style={{ fontSize: 50, fontWeight: 900, color: p.col, marginLeft: 26 }}>{p.v} triệu</div></div>; })}
    </AbsoluteFill>
  );
};

// ---------------- savings bars (10 năm) ----------------
export const SavingsCard: React.FC<{ t: number }> = ({ t }) => {
  const yrs = Array.from({ length: 10 }, (_, i) => 2016 + i), k = sm((t - 0.2) / 3.0);
  return (
    <AbsoluteFill style={{ fontFamily: F }}>
      <Bg t={t} hue="warm" />
      <div style={{ position: "absolute", left: 160, top: 110, fontSize: 60, fontWeight: 900, color: "#fff", opacity: sm(t / 0.4) }}>10 năm tằn tiện của anh Tân</div>
      <div style={{ position: "absolute", right: 160, top: 96, fontSize: 104, fontWeight: 900, color: "#2bd17e" }}>{vn(Math.round(600 * k))} triệu</div>
      {yrs.map((y, i) => { const h = 60 * (i + 1) * Math.min(1, Math.max(0, k * 10 - i)); return <div key={i} style={{ position: "absolute", left: 220 + i * 150, bottom: 260, width: 100 }}>
        <div style={{ height: h, background: "linear-gradient(180deg,#ffe27a,#d59a1e)", borderRadius: "14px 14px 0 0" }} /><div style={{ textAlign: "center", color: "#cdbf9f", fontSize: 26, marginTop: 10, fontWeight: 700 }}>{y}</div></div>; })}
      <div style={{ position: "absolute", left: 160, bottom: 200, fontSize: 24, color: "#9a8f78" }}>Nhân vật và con số trong truyện là minh hoạ</div>
    </AbsoluteFill>
  );
};

// ---------------- "người mua cuối cùng" ----------------
export const LastBuyerCard: React.FC<{ t: number; d: number }> = ({ t, d }) => {
  const N = 40, k = sm((t - 0.3) / Math.max(1, d * 0.55)), fill = Math.floor(N * k), full = fill >= N;
  return (
    <AbsoluteFill style={{ fontFamily: F }}>
      <Bg t={t} hue={full ? "red" : "navy"} />
      <div style={{ position: "absolute", left: 160, top: 110, fontSize: 60, fontWeight: 900, color: "#fff" }}>Ai cũng đã mua…</div>
      <div style={{ position: "absolute", left: 200, top: 290, width: 1520, display: "flex", flexWrap: "wrap", gap: 18 }}>
        {Array.from({ length: N }).map((_, i) => <div key={i} style={{ width: 120, height: 150, opacity: i < fill ? 1 : 0.18, transform: `scale(${i === fill - 1 ? 1.15 : 1})` }}>
          <div style={{ width: 54, height: 54, borderRadius: "50%", background: i < fill ? "#f5c518" : "#8890a8", margin: "0 auto" }} /><div style={{ width: 90, height: 80, borderRadius: "40px 40px 12px 12px", background: i < fill ? "#f5c518" : "#8890a8", margin: "6px auto 0" }} /></div>)}
      </div>
      {full && <div style={{ position: "absolute", right: 160, top: 100, fontSize: 84, fontWeight: 900, color: "#ff4d5e", transform: `rotate(-4deg) scale(${pop((t - 0.3 - d * 0.55) / 0.35)})` }}>HẾT NGƯỜI MUA MỚI</div>}
    </AbsoluteFill>
  );
};

// ---------------- CTA ----------------
export const CtaCard: React.FC<{ t: number; webAt: number }> = ({ t, webAt }) => {
  const a = sm(t / 0.5), w = pop((t - webAt) / 0.45), clickT = t - webAt - 1.4, sub = clickT > 0.35;
  return (
    <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}>
      <Bg t={t} hue="navy" />
      <div style={{ position: "relative", opacity: a }}>
        <div style={{ fontSize: 60, fontWeight: 800, color: "#fff" }}>Nhà mình đã từng xếp hàng mua vàng chưa?</div>
        <div style={{ fontSize: 44, fontWeight: 600, color: "#c5cde0", marginTop: 14 }}>💬 Kể cho em nghe ở phần bình luận nhé</div>
        <div style={{ marginTop: 70, opacity: Math.min(1, w), transform: `scale(${0.8 + 0.2 * Math.min(1.1, w)})` }}>
          <div style={{ fontSize: 42, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>CHỨNG KHOÁN HUY NGUYỄN</div>
          <div style={{ fontSize: 96, fontWeight: 900, color: "#fff", marginTop: 6 }}>chungkhoanhuynguyen.com</div>
          <div style={{ display: "inline-block", marginTop: 40, padding: "22px 60px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 46, fontWeight: 900, transform: `scale(${clickT > 0.2 && clickT < 0.35 ? 0.94 : 1})` }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI"}</div>
        </div>
      </div>
      {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 960 + 120 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 860 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
    </AbsoluteFill>
  );
};
export const EndCard: React.FC<{ t: number }> = ({ t }) => (
  <AbsoluteFill style={{ background: "#0b1124", justifyContent: "center", alignItems: "center", fontFamily: F, textAlign: "center" }}>
    <div style={{ position: "absolute", right: 40, bottom: 28, fontSize: 18, color: "#5f6a85", opacity: sm((t - 1.5) / 0.5) }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư</div>
    <div style={{ opacity: sm(t / 0.6), transform: `scale(${0.95 + 0.05 * sm(t / 1.5)})` }}>
      <div style={{ fontSize: 120, fontWeight: 900, color: "#fff", letterSpacing: 2 }}>TRẢI QUA RỒI MỚI HIỂU</div>
      <div style={{ fontSize: 46, fontWeight: 700, color: "#f5c518", marginTop: 26, letterSpacing: 6 }}>CHỨNG KHOÁN HUY NGUYỄN</div>
      
    </div>
  </AbsoluteFill>
);

// ---------------- overlays on 3D ----------------
export const Bubble: React.FC<{ t: number; at?: number; text: string; x: number; y: number; kind?: "say" | "think" | "whisper"; w?: number; tail?: "l" | "r" }> = ({ t, at = 0, text, x, y, kind = "say", w = 640, tail = "l" }) => {
  const a = pop((t - at) / 0.3); if (t < at) return null;
  const bg = kind === "whisper" ? "rgba(30,30,40,.92)" : "#fffdf6", fg = kind === "whisper" ? "#e9e3ff" : "#15161c";
  return <div style={{ position: "absolute", left: x, top: y, width: w, padding: "26px 34px", borderRadius: kind === "think" ? 60 : 34, background: bg, color: fg, fontFamily: F, fontSize: 44, fontWeight: 800, lineHeight: 1.25, boxShadow: "0 14px 34px rgba(0,0,0,.4)", border: kind === "whisper" ? "3px dashed #9c8cff" : "5px solid #15161c", transform: `scale(${Math.min(1.05, a)})`, transformOrigin: tail === "l" ? "0% 100%" : "100% 100%", opacity: Math.min(1, a), fontStyle: kind === "whisper" ? "italic" : "normal" }}>
    {text}
    {kind !== "think" ? <div style={{ position: "absolute", [tail === "l" ? "left" : "right"]: 60, bottom: -30, width: 0, height: 0, borderLeft: "22px solid transparent", borderRight: "22px solid transparent", borderTop: `32px solid ${kind === "whisper" ? "rgba(30,30,40,.92)" : "#15161c"}` } as React.CSSProperties} />
      : <><div style={{ position: "absolute", left: tail === "l" ? 50 : undefined, right: tail === "r" ? 50 : undefined, bottom: -36, width: 30, height: 30, borderRadius: "50%", background: bg, border: "5px solid #15161c" }} /><div style={{ position: "absolute", left: tail === "l" ? 30 : undefined, right: tail === "r" ? 30 : undefined, bottom: -66, width: 18, height: 18, borderRadius: "50%", background: bg, border: "4px solid #15161c" }} /></>}
  </div>;
};
export const LocTag: React.FC<{ t: number; l1: string; l2?: string; d?: number }> = ({ t, l1, l2, d = 4 }) => { const a = sm(t / 0.4) * (1 - sm((t - d) / 0.5));
  return <div style={{ position: "absolute", left: 110, top: 90, fontFamily: F, opacity: a, transform: `translateX(${(1 - sm(t / 0.4)) * -40}px)` }}>
    <div style={{ display: "inline-block", background: "#f5c518", color: "#111", fontWeight: 900, fontSize: 44, padding: "10px 24px", borderRadius: 8 }}>📍 {l1}</div>
    {l2 && <div style={{ color: "#fff", fontSize: 34, fontWeight: 700, marginTop: 12, textShadow: "0 3px 8px rgba(0,0,0,.8)" }}>{l2}</div>}</div>; };
export const LiveHud: React.FC<{ t: number; viewers: number }> = ({ t, viewers }) => <div style={{ position: "absolute", right: 90, top: 80, fontFamily: F, display: "flex", gap: 14, opacity: sm(t / 0.3) }}>
  <div style={{ background: "#e62117", color: "#fff", fontWeight: 900, fontSize: 34, padding: "8px 20px", borderRadius: 10 }}>● LIVE</div>
  <div style={{ background: "rgba(0,0,0,.6)", color: "#fff", fontWeight: 800, fontSize: 34, padding: "8px 20px", borderRadius: 10 }}>👁 {vn(viewers)}</div></div>;
export const BigText: React.FC<{ t: number; at?: number; text: string; col?: string; y?: number; size?: number }> = ({ t, at = 0, text, col = "#fff", y = 380, size = 130 }) => { const a = pop((t - at) / 0.35); if (t < at) return null;
  return <div style={{ position: "absolute", left: 0, top: y, width: 1920, textAlign: "center", fontFamily: F, fontWeight: 900, fontSize: size, color: col, WebkitTextStroke: "8px #120a10", paintOrder: "stroke fill", transform: `scale(${Math.min(1.1, a)}) rotate(-3deg)`, opacity: Math.min(1, a) } as React.CSSProperties}>{text}</div>; };
export const ClockTag: React.FC<{ t: number; text: string }> = ({ t, text }) => <div style={{ position: "absolute", left: 110, top: 90, fontFamily: F, fontWeight: 900, fontSize: 64, color: "#fff", background: "rgba(10,12,30,.7)", padding: "8px 26px", borderRadius: 14, opacity: sm(t / 0.3) }}>🕒 {text}</div>;
export const Vignette: React.FC<{ k: number; col?: string }> = ({ k, col = "0,0,0" }) => <AbsoluteFill style={{ background: `radial-gradient(ellipse at center, rgba(${col},0) 45%, rgba(${col},${0.75 * k}) 100%)`, pointerEvents: "none" }} />;
