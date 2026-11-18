// Phim GD1. Khung 1920x1080, 30 fps.
// Mỗi câu thoại có mốc thời gian thật (timing.json do giọng Huy70_HaiDang30 đọc) → cắt cảnh đúng câu, phụ đề đúng chữ.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, staticFile, delayRender, continueRender, Audio, getInputProps } from "remotion";
import { Stage, Shot3D, Run, SetKey, Cast, V } from "../vang/stage";
import { Pose, Acc } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { GOLD_X, HOME_X } from "../vang/sets";
import { NewsCard } from "../vang/cards";
import { Article, AlertCard, BoardCard, GoldBoard, DoomClock, HistoryCard } from "../hn/cards_hn";
import { TIMING, FPS, TOTAL_F, TAIL, sc, subText, BAD, GOOD } from "./data";
import { F, sm, PhoneCard, PaperCard, ChatCard, TitleCard, LessonCard, SplitCard, EndCard, Bubble, LocTag, BigText, ClockTag, Vignette, Bg, LiveHud } from "../vang/cards";

// ---------- pose helpers ----------
const bl = (t: number, k = 71) => Math.floor(t * 30) % k < 4;
type PO = Omit<Pose, "expr"> & { anim?: boolean };
const P = (expr: Expr, o: PO = {}) => (t: number): Pose => { const { anim, ...r } = o; return { expr, blink: expr === "laugh" || expr === "cry" || expr === "sleepy" ? false : bl(t + (r.phase ?? 0) * 3), ...r, ...(anim ? { t: Math.round(t * 15) / 15 } : {}) }; };
const seq = (pairs: [number, Expr][], o: PO = {}) => (t: number): Pose => { let e = pairs[0][1]; for (const [at, x] of pairs) if (t >= at) e = x; return P(e, o)(t); };
const walk = (expr: Expr, o: PO = {}) => (t: number): Pose => ({ ...P(expr, o)(t), mode: "stroll", phase: (t * 1.1) % 1 });
const C = (a: string, p: V, pose: Cast["pose"], to?: V): Cast => ({ a, p, pose, to });
const S = (set: SetKey, light: Shot3D["light"], from: [V, V, number], to: [V, V, number], cast: Cast[], x: Partial<Shot3D> = {}): Shot3D => ({ set, light, from, to, cast, ...x });


type Seg = { k: "3d"; s: Shot3D; ov?: (t: number, d: number) => React.ReactNode } | { k: "card"; r: (t: number, d: number) => React.ReactNode };
const D3 = (s: Shot3D, ov?: (t: number, d: number) => React.ReactNode): Seg => ({ k: "3d", s, ov });
const CD = (r: (t: number, d: number) => React.ReactNode): Seg => ({ k: "card", r });
const rel = (id: string, j: number, ref: number) => sc(id).sens[Math.min(j, sc(id).sens.length - 1)].a - ref;
type Plan = { id: string; shots: [number, (a: number) => Seg][] };

// thời điểm (giây, tính từ đầu cảnh quay bắt đầu ở câu k) khi câu j của cảnh id bắt đầu
const at = (id: string, k: number, j: number) => { const s = sc(id), q = (i: number) => s.sens[Math.min(i, s.sens.length - 1)]; return q(j).a - (k === 0 ? s.a : q(k).a - 0.12); };
// ---------- blocking ----------
// Phố: máy nhìn về +z nên +x nằm bên TRÁI màn. Phòng (room): máy nhìn về −z nên +x nằm bên PHẢI màn. side = hướng mặt trên MÀN (+1 quay phải).
const HX = HOME_X + 3.6;                                   // vỉa hè trước nhà Quang (phố Lò Đúc), tránh xe máy dựng cửa
const two = (x: number, z = 5.3, d = 4.3, h = 1.5): [[V, V, number], [V, V, number]] => [[[x + 0.2, h, z - d], [x, 1.1, z], 40], [[x + 0.1, h - 0.05, z - d + 0.5], [x, 1.1, z], 37]];
const roomTwo: [[V, V, number], [V, V, number]] = [[[0.8, 1.45, 3.4], [0.8, 1.15, 0.6], 40], [[0.8, 1.42, 3.0], [0.8, 1.15, 0.6], 37]];
const TS = GOLD_X;                                          // quán trà đá bác Tư (vỉa hè, ban ngày)
const fixed = (c: V, l: V, f: number): [[V, V, number], [V, V, number]] => [[c, l, f], [c, l, f]];


const runners = (n: number, x0: number, x1: number, z: number, acc: Acc[] = ["box"]): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (30 + i), [x0 + (i % 4) * 0.7, 0, z + (i % 3) * 0.55], (t: number) => ({ ...P(i % 2 ? "shock" : "worried", { acc: i % 3 ? acc : [] })(t), mode: "stroll", phase: (t * 1.6 + i * 0.37) % 1, side: x1 < x0 ? 1 : -1 }), [x1 + (i % 4) * 0.7, 0, z + (i % 3) * 0.55]));// ---------- thẻ riêng phim #4 ----------
const W2 = (s: string) => <span style={{ color: "#ffd23f" }}>{s}</span>;
const BankCard: React.FC<{ t: number; clock: string; amt: string; at?: number; note?: string; ok?: boolean }> = ({ t, clock, amt, at: a0 = 0.4, note, ok }) => { const a = sm((t - a0) / 0.35);
  return <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 40%,#1b2340,#05070f)", fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <div style={{ width: 620, height: 960, borderRadius: 60, background: "#0d1326", border: "10px solid #2a3350", padding: 50, boxSizing: "border-box", textAlign: "center" }}>
      <div style={{ fontSize: 40, color: "#9fb0d8", fontWeight: 700 }}>{clock}</div>
      <div style={{ marginTop: 60, fontSize: 44, color: "#dfe6f8", fontWeight: 800 }}>🏦 Ứng dụng ngân hàng</div>
      <div style={{ marginTop: 120, fontSize: 36, color: "#9fb0d8" }}>Số dư khả dụng</div>
      <div style={{ marginTop: 20, fontSize: 88, whiteSpace: "nowrap", fontWeight: 900, color: ok ? "#5dff9b" : "#ff4d5e", opacity: a, transform: `scale(${1.3 - 0.3 * a})`, textDecoration: ok ? "line-through" : "none" }}>{amt}</div>
      {note && <div style={{ marginTop: 50, fontSize: 40, color: ok ? "#5dff9b" : "#ffb3b3", fontWeight: 800, opacity: sm((t - a0 - 0.8) / 0.4) }}>{note}</div>}
    </div></AbsoluteFill>; };
const Rows: React.FC<{ t: number; title: string; rows: { l: string; v: string; at: number; col?: string; big?: boolean }[]; foot?: string; stamp?: { text: string; at: number } }> = ({ t, title, rows, foot, stamp }) =>
  <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center" }}><Bg t={t} hue="navy" />
    <div style={{ width: 1300, position: "relative" }}>
      <div style={{ fontSize: 58, fontWeight: 900, color: "#fff", marginBottom: 30 }}>{title}</div>
      {rows.map((r, i) => { const a = sm((t - r.at) / 0.3); return <div key={i} style={{ display: "flex", justifyContent: "space-between", padding: r.big ? "20px 30px" : "12px 30px", marginTop: 8, borderRadius: 16, background: r.big ? "rgba(255,77,94,.18)" : "rgba(255,255,255,.07)", border: r.big ? "3px solid #ff4d5e" : "2px solid rgba(255,255,255,.12)", opacity: a, transform: `translateX(${(1 - a) * 60}px)`, fontSize: r.big ? 64 : 46, fontWeight: r.big ? 900 : 700, color: "#fff" }}><span>{r.l}</span><span style={{ color: r.col ?? "#ffd23f" }}>{r.v}</span></div>; })}
      {foot && <div style={{ marginTop: 22, fontSize: 26, color: "rgba(255,255,255,.55)" }}>{foot}</div>}
      {stamp && t > stamp.at && <div style={{ position: "absolute", left: 260, top: 300, transform: `rotate(-10deg) scale(${1.4 - 0.4 * sm((t - stamp.at) / 0.25)})`, border: "8px solid #ff4d5e", color: "#ff4d5e", fontSize: 58, fontWeight: 900, padding: "10px 30px", borderRadius: 14, background: "rgba(20,0,0,.6)" }}>{stamp.text}</div>}
    </div></AbsoluteFill>;
const Bars: React.FC<{ t: number; title: string; rows: { l: string; v: number; at: number; col: string; lab: string }[]; max: number; src: string }> = ({ t, title, rows, max, src }) =>
  <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center" }}><Bg t={t} hue="navy" />
    <div style={{ width: 1500, position: "relative" }}><div style={{ fontSize: 58, fontWeight: 900, color: "#fff", marginBottom: 50 }}>{title}</div>
      {rows.map((r, i) => { const a = sm((t - r.at) / 0.6); return <div key={i} style={{ display: "flex", alignItems: "center", marginTop: 34, opacity: sm((t - r.at) / 0.2) }}>
        <div style={{ width: 470, fontSize: 40, color: "#dfe6f8", fontWeight: 700 }}>{r.l}</div>
        <div style={{ height: 80, width: (900 * r.v / max) * a, background: r.col, borderRadius: 12 }} />
        <div style={{ marginLeft: 24, fontSize: 60, fontWeight: 900, color: r.col }}>{r.lab}</div></div>; })}
      <div style={{ marginTop: 50, fontSize: 26, color: "rgba(255,255,255,.55)" }}>{src}</div></div></AbsoluteFill>;
const Big2: React.FC<{ t: number; items: { a: string; b: string; at: number; col: string }[]; src?: string; head?: string; img?: string }> = ({ t, items, src, head, img }) =>
  <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}>
    {img ? <AbsoluteFill><img src={staticFile(img)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${1.05 + t * 0.008})`, filter: "brightness(.35)" }} /></AbsoluteFill> : <Bg t={t} hue="red" />}
    {head && <div style={{ position: "absolute", top: 110, width: "100%", fontSize: 54, fontWeight: 900, color: "#fff" }}>{head}</div>}
    <div style={{ display: "flex", gap: 90, position: "relative" }}>{items.map((x, i) => { const a = sm((t - x.at) / 0.35); return <div key={i} style={{ opacity: a, transform: `scale(${1.25 - 0.25 * a})` }}><div style={{ fontSize: 150, fontWeight: 900, color: x.col }}>{x.a}</div><div style={{ fontSize: 42, fontWeight: 800, color: "#fff", maxWidth: 700 }}>{x.b}</div></div>; })}</div>
    {src && <div style={{ position: "absolute", bottom: 170, width: "100%", fontSize: 26, color: "rgba(255,255,255,.6)" }}>{src}</div>}</AbsoluteFill>;
// ---------- thẻ riêng phim PNJ1 ----------
const Img: React.FC<{ t: number; img: string; head?: string; foot?: string }> = ({ t, img, head, foot }) => { const a = sm(t / 0.5);
  return <AbsoluteFill style={{ background: "#160c2e", fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <img src={staticFile(`dn1/${img}.jpg`)} style={{ width: 1600, height: 900, marginTop: -110, objectFit: "contain", opacity: a, transform: `scale(${0.97 + 0.03 * a + t * 0.002})` }} />
    {head && <div style={{ position: "absolute", top: 40, right: 80, padding: "10px 26px", borderRadius: 12, background: "#ffd23f", color: "#1a0f33", fontSize: 40, fontWeight: 900, opacity: sm((t - 0.6) / 0.3) }}>{head}</div>}
    {foot && <div style={{ position: "absolute", bottom: 175, width: "100%", textAlign: "center", fontSize: 26, color: "rgba(255,255,255,.6)" }}>{foot}</div>}</AbsoluteFill>; };
const Ask: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.5), clickT = t - 3.6, sub = clickT > 0.35;
  return <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><Bg t={t} hue="navy" />
    <div style={{ opacity: a, position: "relative" }}><div style={{ fontSize: 40, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>CÂU HỎI CHO ANH CHỊ</div>
      <div style={{ fontSize: 88, fontWeight: 900, color: "#fff", marginTop: 20, lineHeight: 1.15 }}>ANH CHỊ CÓ ĐỌC TIẾP<br />DÒNG THỨ HAI KHÔNG?</div>
      <div style={{ display: "inline-block", marginTop: 50, padding: "22px 64px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 48, fontWeight: 900 }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI KÊNH"}</div></div>
    {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 1060 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 820 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
    <div style={{ position: "absolute", left: 0, right: 0, bottom: 150, textAlign: "center" }}><span style={{ display: "inline-block", padding: "14px 40px", borderRadius: 18, background: "#ffd23f", color: "#1a1040", fontSize: 56, fontWeight: 900, letterSpacing: 1, boxShadow: "0 8px 30px rgba(0,0,0,.45)" }}>chungkhoanhuynguyen.com</span></div>
    <div style={{ position: "absolute", right: 40, bottom: 20, fontSize: 22, color: "rgba(255,255,255,.5)" }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư · Ảnh: Wikimedia Commons (CC BY / CC BY-SA)</div></AbsoluteFill>; };
const Photo: React.FC<{ t: number; img: string; d?: number; dir?: number }> = ({ t, img, d = 7, dir = 1 }) => { const k = Math.min(1, t / Math.max(d, 1)); const z = 1.06 + 0.08 * k;
  return <AbsoluteFill style={{ background: "#000" }}><img src={staticFile(`dn1/${img}.jpg`)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z}) translateX(${dir * (k - 0.5) * 30}px)`, filter: "brightness(.82) saturate(1.05)" }} />
    <AbsoluteFill style={{ background: "linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 28%,rgba(0,0,0,0) 62%,rgba(0,0,0,.55) 100%)" }} /></AbsoluteFill>; };
const PR = (img: string, ov?: (t: number) => React.ReactNode, dir = 1) => (t: number) => <><Photo t={t} img={img} dir={dir} />{ov?.(t)}</>;
// ---------- dàn cảnh phim TP1 ----------
// Phòng/căn hộ/cafe (room-like): máy nhìn −z → +x bên PHẢI màn. Người trái màn side +1, người phải màn side −1.
const roomTwo2: [[V, V, number], [V, V, number]] = [[[0, 1.5, 4.2], [0, 1.15, 0.7], 40], [[0, 1.45, 3.6], [0, 1.15, 0.7], 36]];
const LX = -0.7, NX = 0.7, RZ = 0.8;
const HOME: Shot3D["set"] = "canho";
const RM = { chat: "off" as const, game: false };
const TH = (e: Expr, o: PO = {}) => C("thuong", [LX, 0, RZ], P(e, { side: 1, mode: "stand", ...o }));
const ME = (e: Expr, o: PO = {}) => C("mehung", [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }));
const CH = (e: Expr, o: PO = {}) => C("chien", [LX, 0, RZ], P(e, { side: 1, mode: "stand", ...o }));
const HU = (e: Expr, o: PO = {}) => C("huy", [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }));
const closeL = (set: Shot3D["set"], a: string, e: Expr, o: PO = {}, light: Shot3D["light"] = "room") => S(set, light, [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [C(a, [LX, 0, RZ], P(e, { side: 1, mode: "stand", ...o }))], RM);
const closeR = (set: Shot3D["set"], a: string, e: Expr, o: PO = {}, light: Shot3D["light"] = "room") => S(set, light, [[1.3, 1.35, 2.3], [NX, 1.05, RZ], 34], [[1.3, 1.32, 2.0], [NX, 1.05, RZ], 30], [C(a, [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }))], RM);
const BL = (x: number, y: number, text: string, at0: number, tail: "l" | "r" = "l") => (t: number) => <Bubble t={t} at={at0} text={text} x={x} y={y} tail={tail} w={640} />;
// Ngân hàng (set bank): quầy z=-1.2, nhân viên sau quầy, khách đứng trước quầy; khách xếp hàng trên ghế chờ.
const crowdB = (n = 6): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (60 + i), [-2.6 + (i % 3) * 0.9 + (i > 2 ? 3.6 : 0), 0, 2.2 + (i % 2) * 0.3], P(i % 2 ? "neutral" : "worried", { mode: "stand", acc: i % 2 ? ["phone"] : ["paper"], phase: i * 0.4, side: 1 })));
const bank = (cast: Cast[], from: [V, V, number], to: [V, V, number], x: Partial<Shot3D> = {}) => S("bank", "day", from, to, [...cast, ...crowdB()], x);
const bWide: [[V, V, number], [V, V, number]] = [[[-2.6, 1.7, 3.2], [0, 1.2, -1.2], 48], [[-1.8, 1.55, 2.4], [0, 1.2, -1.2], 42]];
const bClerk: [[V, V, number], [V, V, number]] = [[[0.9, 1.45, 0.6], [0, 1.35, -2.0], 34], [[0.75, 1.42, 0.3], [0, 1.35, -2.0], 30]];
const bCust: [[V, V, number], [V, V, number]] = [[[-1.2, 1.4, -1.0], [0.1, 1.2, -0.2], 36], [[-1.0, 1.38, -0.8], [0.1, 1.2, -0.2], 32]];
const NV = (e: Expr, o: PO = {}) => C("nv", [0, 0, -2.0], P(e, o));
const BA = (e: Expr, o: PO = {}, x = 0.1) => C("mehung", [x, 0, -0.2], P(e, { side: -1, ...o }));
const THb = (e: Expr, o: PO = {}) => C("thuong", [-0.6, 0, -0.25], P(e, { side: 1, ...o }));
// ảnh thật + nhân vật
const PH = (bg: string, fit: [number, number], cast: Cast[], cam: [[V, V, number], [V, V, number]], x: Partial<Shot3D> = {}) => S("photo", "room", cam[0], cam[1], cast, { bg: `dn1/${bg}.jpg`, bgFit: fit, ...x });
const pcam = (x = 0): [[V, V, number], [V, V, number]] => [[[x, 1.45, -3.2], [x, 1.25, 3], 42], [[x, 1.42, -2.8], [x, 1.25, 3], 40]];
const walkers = (n: number, z = 1.6): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (40 + i), [i % 2 ? 2.6 : -2.2, 0, z + i * 0.35], (t: number) => ({ ...P(i % 3 ? "neutral" : "smile", { acc: i % 2 ? ["box"] : ["phone"] })(t), mode: "stroll", phase: (t * 1.4 + i * 0.3) % 1, side: i % 2 ? 1 : -1 }), [i % 2 ? -2.4 : 2.8, 0, z + i * 0.35]));
const Clues: React.FC<{ t: number; title: string; items: { text: string; at: number; ok?: string }[]; src?: string }> = ({ t, title, items, src }) =>
  <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center" }}><Bg t={t} hue="night" />
    <div style={{ width: 1400, position: "relative" }}><div style={{ fontSize: 46, fontWeight: 900, color: "#ffd23f", letterSpacing: 3, marginBottom: 30, opacity: sm(t / 0.3) }}>{title}</div>
      {items.map((x, i) => { const a = sm((t - x.at) / 0.35), ok = x.ok && t > x.at + 1.2; return <div key={i} style={{ display: "flex", alignItems: "center", gap: 30, marginTop: 24, padding: "22px 34px", borderRadius: 20, background: "rgba(255,210,63,.08)", border: "3px solid " + (ok ? "#5dff9b" : "rgba(255,210,63,.6)"), opacity: a, transform: `translateX(${(1 - a) * 80}px)` }}>
        <div style={{ fontSize: 64, fontWeight: 900, color: "#ffd23f", width: 70 }}>{i + 1}</div><div style={{ fontSize: 46, fontWeight: 800, color: "#fff", flex: 1 }}>{x.text}</div>
        {ok && <div style={{ fontSize: 40, fontWeight: 900, color: "#5dff9b" }}>{x.ok}</div>}</div>; })}
      {src && <div style={{ marginTop: 24, fontSize: 26, color: "rgba(255,255,255,.55)" }}>{src}</div>}</div></AbsoluteFill>;
const Sign: React.FC<{ t: number; lines: string[]; title: string; foot?: string }> = ({ t, lines, title, foot }) => { const a = sm(t / 0.4);
  return <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 40%,#2a2f3a,#0b0d12)", fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <div style={{ width: 1100, padding: "60px 70px", background: "#fffdf3", borderRadius: 12, transform: `rotate(-1.5deg) scale(${0.94 + 0.06 * a})`, opacity: a, boxShadow: "0 30px 80px rgba(0,0,0,.6)" }}>
      <div style={{ fontSize: 72, fontWeight: 900, color: "#c8202f", textAlign: "center" }}>{title}</div>
      {lines.map((l, i) => <div key={i} style={{ marginTop: 26, fontSize: 48, fontWeight: 800, color: "#222", textAlign: "center", opacity: sm((t - 0.6 - i * 0.7) / 0.3) }}>{l}</div>)}
      {foot && <div style={{ marginTop: 40, fontSize: 32, color: "#666", textAlign: "center" }}>{foot}</div>}
    </div></AbsoluteFill>; };
const CH_ = (e: Expr, o: PO = {}, x = 0.2) => C("chien", [x, 0, 0.7], P(e, { side: -1, mode: "stand", ...o }));
const HG_ = (e: Expr, o: PO = {}, x = 0.95) => C("hung", [x, 0, 0.7], P(e, { side: 1, mode: "stand", ...o }));
const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => CD((t) => <NewsCard t={t} tag="TIN SÁNG NAY" items={[{ src: "Báo điện tử", head: "182.000 doanh nghiệp rời cuộc chơi trong 10 tháng", at: 0.3, col: "#ff4d5e" }]} />)],
    [1, () => D3(closeL("canho", "chien", "shock", { acc: ["phone", "glow"] }), (t) => <><ClockTag t={t} text="8:00" />{BL(1060, 110, "Huy ơi, 182.000 doanh nghiệp rời cuộc chơi! Tao bán hết đây!", 0.8, "r")(t)}</>)],
  ] },
  { id: "S02", shots: [
    [0, () => D3(closeR("cafe", "huy", "neutral", { acc: ["phone", "glow"] }), (t) => <>{BL(120, 110, "Khoan bấm. Chiều ra tiệm xe của Hùng Xa Lộ đã.", 0.2)(t)}</>)],
    [2, () => CD((t) => <Clues t={t} title="NHỚ 3 CHI TIẾT" items={[{ text: "Tờ giấy dán trên cửa tiệm", at: 1.4 }, { text: "Lá thư của cơ quan thuế", at: 2.6 }, { text: "Cửa hàng mới bên kia đường", at: 3.8 }]} />)],
  ] },
  { id: "S03", shots: [
    [0, () => D3(PH("shop_ngoai", [0.5, 0.6], [HG_("neutral", { acc: ["helmet"] }, 0.4)], pcam(0.4)), (t) => <><BigText t={t} at={0.3} text="HÙNG XA LỘ" col="#ffd23f" y={200} size={120} /><LocTag t={t} l1="42 tuổi · 10 năm chạy xe tải" l2="5 năm mở tiệm xe máy đầu ngõ" /></>)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(PH("shop_ngoai", [0.5, 0.6], [CH_("dazed", {}, 0.2), C("huy", [0.95, 0, 0.7], P("neutral", { side: 1, mode: "stand" }))], pcam(0.4)), (t) => <LocTag t={t} l1="CHIỀU ĐÓ" l2="Tiệm xe đầu ngõ" />)],
    [1, () => CD((t) => <Sign t={t} title="SANG NHƯỢNG CỬA HÀNG" lines={["Thanh lý toàn bộ phụ tùng", "Liên hệ chủ tiệm"]} foot="🔍 Chi tiết thứ nhất" />)],
    [2, () => D3(PH("shop_ngoai", [0.5, 0.6], [CH_("smug", { wave: 1 }, 0.2), C("huy", [0.95, 0, 0.7], P("neutral", { side: 1, mode: "stand" }))], pcam(0.4)), (t) => <>{BL(1000, 110, "Đấy, tao nói rồi mà!", 0.3, "r")(t)}</>)],
  ] },
  { id: "S05", shots: [
    [0, () => D3(PH("tiem_hn", [0.5, 0.6], [HG_("sad", { acc: ["cup"] }, 0.4)], pcam(0.4)), (t) => <LocTag t={t} l1="TIỆM CỦA HÙNG" l2="Sửa xe, bán xe đầu ngõ" />)],
    [2, () => CD((t) => <LessonCard t={t} title="Vì sao tiệm của Hùng vắng khách" items={[{ n: "1", icon: "⚡", head: "Khách chuyển sang xe điện", body: "", at: 0.2 }, { n: "2", icon: "📦", head: "Mua phụ tùng trên mạng", body: "", at: 1.4 }, { n: "3", icon: "🏠", head: "Tiền thuê mặt bằng tăng mỗi năm", body: "", at: 2.8 }]} />)],
    [3, () => D3(PH("tiem_hn", [0.5, 0.6], [HG_("sad", {}, 0.4)], pcam(0.4)), (t) => <BigText t={t} at={0.3} text="CẢ THÁNG BÁN 2 CHIẾC XE" col="#ff4d5e" y={90} size={100} />)],
  ] },
  { id: "S06", shots: [
    [0, () => CD(PR("pho", (t) => <BigText t={t} at={0.3} text="KHÔNG HIẾM" col="#fff" y={90} size={120} />))],
    [1, () => CD((t) => <Rows t={t} title="Doanh nghiệp hoàn tất giải thể, 10 tháng 2026" foot="Cục Thống kê (Bộ Tài chính), qua VCCI và Thời báo Tài chính" rows={[{ l: "Tổng số", v: "gần 56.300 (+109,8%)", at: 0.6, big: true }, { l: "Bán buôn, bán lẻ, sửa chữa ô tô, xe máy", v: "21.673 (+120,1%)", at: at("S06", 1, 2), col: "#ff4d5e" }]} />)],
  ] },
  { id: "S07", shots: [[0, () => CD((t) => <Rows t={t} title="182.000 doanh nghiệp “rời cuộc chơi” gồm" foot="Cục Thống kê, 10 tháng 2026" rows={[{ l: "Tạm ngừng kinh doanh có thời hạn", v: "gần 92.000", at: 0.4 }, { l: "Ngừng hoạt động chờ giải thể", v: "hơn 33.700", at: 1.6 }, { l: "Hoàn tất giải thể", v: "gần 56.300", at: 2.8 }, { l: "Bình quân mỗi tháng", v: "khoảng 18.200", at: at("S07", 0, 1), big: true, col: "#ffd23f" }]} />)]] },
  { id: "S08", shots: [
    [0, () => D3(PH("tiem_hn", [0.5, 0.6], [CH_("smug", {}, 0.2), HG_("neutral", {}, 0.95)], pcam(0.4)), (t) => <>{BL(120, 110, "Thấy chưa, sập thật rồi!", 0.3)(t)}</>)],
    [1, () => D3(PH("tiem_hn", [0.5, 0.6], [CH_("dazed", {}, 0.2), HG_("stern", { acc: ["paper"], wave: 1 }, 0.95)], pcam(0.4)))],
    [2, () => CD((t) => <PaperCard t={t} title="THÔNG BÁO CỦA CƠ QUAN THUẾ" sub="V/v rà soát, làm sạch mã số thuế" lines={[{ text: "Doanh nghiệp đã ngừng hoạt động", at: 0.6 }, { text: "đề nghị hoàn tất thủ tục giải thể", at: 1.2, under: true, col: "#c8202f" }]} stamp={{ text: "CHI TIẾT THỨ HAI", at: 2.0 }} />)],
  ] },
  { id: "S09", shots: [
    [0, () => D3(PH("tiem_hn", [0.5, 0.6], [CH_("neutral", {}, 0.2), HG_("neutral", { acc: ["paper"] }, 0.95)], pcam(0.4)), (t) => <>{BL(1000, 110, "Công ty ông anh họ tôi đóng cửa từ 2023, năm nay mới giải thể xong.", 0.3, "r")(t)}</>)],
    [2, () => CD((t) => <Big2 t={t} items={[{ a: "2023", b: "đã ngừng hoạt động", at: 0.2, col: "#dfe6f8" }, { a: "2026", b: "mới được đếm là giải thể", at: 1.4, col: "#ffd23f" }]} />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(closeR("cafe", "huy", "neutral"), (t) => <LocTag t={t} l1="HUY NGUYỄN" l2="Chỗ ít ai đọc kỹ" />)],
    [1, () => CD((t) => <NewsCard t={t} tag="NĂM 2026" items={[{ src: "Bộ Tài chính", head: "Chiến dịch làm sạch mã số thuế: nhiều doanh nghiệp ngừng từ các năm trước nay mới hoàn tất giải thể", at: 0.3, col: "#ffd23f" }]} />)],
    [2, () => CD((t) => <Big2 t={t} head="Ông Phạm Bình An, Viện Nghiên cứu phát triển TP.HCM" src="Theo Tạp chí Nhà đầu tư, đăng lại trên VCCI 9/11/2026" items={[{ a: "“", b: "có yếu tố kỹ thuật và hành chính, không hoàn toàn phản ánh sức khỏe thật của doanh nghiệp", at: 0.3, col: "#ffd23f" }]} />)],
  ] },
  { id: "S11", shots: [
    [0, () => CD((t) => <Big2 t={t} items={[{ a: "2 CON SỐ", b: "đi ngược chiều mà ít ai nhắc", at: 0.2, col: "#ffd23f" }]} />)],
    [1, () => CD((t) => <Rows t={t} title="10 tháng 2026 so với cùng kỳ" foot="Cục Thống kê (Bộ Tài chính)" rows={[{ l: "Tạm ngừng kinh doanh", v: "−12,7%", at: 0.4, col: "#5dff9b", big: true }, { l: "Ngừng hoạt động chờ giải thể", v: "−42,3%", at: at("S11", 1, 2), col: "#5dff9b", big: true }]} />)],
    [3, () => CD((t) => <Big2 t={t} items={[{ a: "SẬP THẬT", b: "thì 2 con số này phải TĂNG", at: 0.2, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S12", shots: [
    [0, () => D3(PH("pho", [0.5, 0.6], [CH_("shock", {}, 0.2), ...walkers(3)], pcam(0.2)), (t) => <LocTag t={t} l1="RA KHỎI TIỆM" l2="Bên kia đường" />)],
    [1, () => CD((t) => <Sign t={t} title="KHAI TRƯƠNG" lines={["Chuỗi cửa hàng xe điện", "🎈 Lái thử miễn phí 🎈", "Khách xếp hàng kín vỉa hè"]} foot="🔍 Chi tiết thứ ba" />)],
    [2, () => D3(PH("pho", [0.5, 0.6], [CH_("dazed", {}, 0.2), C("huy", [0.95, 0, 0.7], P("neutral", { side: 1, mode: "stand" }))], pcam(0.4)), (t) => <>{BL(120, 110, "Thế rốt cuộc kinh tế xấu hay tốt?", 0.3)(t)}</>)],
  ] },
  { id: "S13", shots: [
    [0, () => D3(closeR("cafe", "huy", "neutral"), (t) => <LocTag t={t} l1="HUY NGUYỄN" l2="Thêm 2 con số" />)],
    [1, () => CD((t) => <Rows t={t} title="Doanh nghiệp thành lập mới, 10 tháng 2026" foot="Cục Thống kê, qua Thời báo Tài chính 3/11/2026" rows={[{ l: "Số doanh nghiệp mới", v: "khoảng 162.300 (−0,4%)", at: 0.4 }, { l: "Vốn đăng ký bình quân/DN", v: "13,2 tỷ (+34,8%)", at: at("S13", 1, 2), col: "#5dff9b", big: true }, { l: "Lao động đăng ký", v: "−17,4%", at: at("S13", 1, 3), col: "#ff4d5e" }]} />)],
  ] },
  { id: "S14", shots: [
    [0, () => CD((t) => <Big2 t={t} items={[{ a: "🔍", b: "ghép 3 chi tiết lại", at: 0.1, col: "#ffd23f" }]} />)],
    [1, () => CD((t) => <Clues t={t} title="3 CHI TIẾT ĐẦU PHIM" items={[{ text: "Tờ giấy sang nhượng → nỗi đau của tiệm nhỏ là thật", at: 0.2, ok: "✓" }, { text: "Lá thư thuế → số liệu bị đẩy lên vì dọn sổ cũ", at: at("S14", 1, 2), ok: "✓" }, { text: "Cửa hàng mới → tiền chảy sang DN lớn, theo kịp thay đổi", at: at("S14", 1, 3), ok: "✓" }]} />)],
  ] },
  { id: "S15", shots: [[0, () => CD((t) => <Big2 t={t} items={[{ a: "KHÔNG SẬP", b: "", at: 0.2, col: "#5dff9b" }, { a: "ĐANG THAY MÁU", b: "và thay máu thì luôn có người đau", at: at("S15", 0, 1), col: "#ffd23f" }]} />)]] },
  { id: "S16", shots: [
    [0, () => D3(S("cafe", "room", ...roomTwo2, [CH("dazed", { acc: ["cup"] }), HU("neutral", { acc: ["cup"] })], RM), (t) => <>{BL(120, 110, "Thế tao có nên bán cổ phiếu không?", 0.3)(t)}</>)],
    [1, () => CD((t) => <Big2 t={t} head="Doanh nghiệp anh đang cầm thuộc phía nào?" items={[{ a: "🔧", b: "phía đang MẤT khách", at: at("S16", 1, 2), col: "#ff4d5e" }, { a: "⚡", b: "phía đang GIÀNH khách", at: at("S16", 1, 2) + 1.6, col: "#5dff9b" }]} />)],
  ] },
  { id: "S17", shots: [
    [0, () => D3(PH("tiem_hn", [0.5, 0.6], [C("huy", [0.2, 0, 0.7], P("smile", { side: -1, mode: "stand" })), HG_("sad", {}, 0.95)], pcam(0.4)), (t) => <>{BL(120, 110, "Anh không thất bại, anh chỉ đứng ở phía bị thay.", rel("S17", 1, sc("S17").sens[0].a))(t)}</>)],
    [2, () => CD((t) => <Big2 t={t} items={[{ a: "10 + 5 NĂM", b: "lái xe, sửa xe – tay nghề vẫn có giá", at: 0.2, col: "#ffd23f" }]} />)],
  ] },
  { id: "S18", shots: [
    [0, () => D3(PH("pho", [0.5, 0.6], [HG_("laugh", { acc: ["helmet"] }, 0.4)], pcam(0.4)), (t) => <><ClockTag t={t} text="2 TUẦN SAU" /><BigText t={t} at={0.6} text="TRƯỞNG XƯỞNG KỸ THUẬT" col="#5dff9b" y={200} size={96} /></>)],
    [1, () => D3(closeL("canho", "chien", "smile", { acc: ["phone", "glow"] }), (t) => <BigText t={t} at={0.4} text="ĐỌC ĐẾN DÒNG CUỐI" col="#ffd23f" y={90} size={110} />)],
  ] },
  { id: "S19", shots: [[0, () => CD((t) => <Ask t={t} />)]] },
];
function teaStall() { return [] as Cast[]; }



const Meme: React.FC<{ t: number; at?: number; top: string; bot: string; small?: boolean; noSubGap?: boolean; y?: number }> = ({ t, at = 0, top, bot, small, noSubGap, y }) => { if (t < at) return null; const a = Math.min(1, (t - at) / 0.18), sz = small ? 150 : 92;
  const st = { position: "absolute", left: 0, width: 1920, textAlign: "center", fontFamily: F, fontWeight: 900, fontSize: sz, color: "#fff", WebkitTextStroke: "10px #000", paintOrder: "stroke fill", letterSpacing: 1, transform: `scale(${1.25 - 0.25 * a})`, opacity: a } as React.CSSProperties;
  return <>{top && <div style={{ ...st, top: 70 }}>{top}</div>}{bot && <div style={{ ...st, top: y ?? (small ? 690 : noSubGap ? 175 : 620), color: small ? "#ffe14d" : "#fff", fontSize: small ? 130 : sz }}>{bot}</div>}</>; };



type GSeg = Seg & { a: number; b: number; id: string; n: number };
export const SEGS: GSeg[] = (() => {
  const out: GSeg[] = [];
  for (const p of PLAN) { const S0 = sc(p.id);
    const q = (i: number) => S0.sens[Math.min(i, S0.sens.length - 1)];
    p.shots.forEach(([j, mk], k) => { const a = k === 0 ? S0.a : q(j).a - 0.12, nb = k + 1 < p.shots.length ? q(p.shots[k + 1][0]).a - 0.12 : S0.b; out.push({ ...mk(a), a, b: nb, id: p.id, n: k }); }); }
  return out;
})();
const fr = (s: number) => Math.round(s * FPS);

// ---------- subtitles ----------
type Chunk = { a: number; b: number; text: string };
const CHUNKS: Chunk[] = (() => {
  const out: Chunk[] = [];
  for (const S0 of TIMING.scenes) for (const s of S0.sens) {
    const txt = subText(s.text); const parts: string[] = []; let cur = "";
    for (const piece of txt.split(/(?<=[,:;])\s+/)) { if ((cur + " " + piece).trim().length > 64 && cur) { parts.push(cur.trim()); cur = piece; } else cur = (cur + " " + piece).trim(); }
    if (cur) parts.push(cur);
    const fin: string[] = []; for (const p of parts) { if (p.length <= 80) { fin.push(p); continue; } const w = p.split(" "), h = Math.ceil(w.length / 2); fin.push(w.slice(0, h).join(" "), w.slice(h).join(" ")); }
    const tot = fin.reduce((x, p) => x + p.length, 0); let t = s.a;
    for (const p of fin) { const d = ((s.b - s.a) * p.length) / tot; out.push({ a: t, b: t + d, text: p }); t += d; }
  }
  return out;
})();
const hl = (w: string) => { const lw = w.toLowerCase(); if (/\d/.test(w)) return "#ffd23a"; if (BAD.some((b) => lw.includes(b))) return "#ff6a6a"; if (GOOD.some((g) => lw.includes(g))) return "#5dff9b"; return "#ffffff"; };
const Subs: React.FC = () => {
  const t = useCurrentFrame() / FPS; let c: Chunk | undefined; for (const x of CHUNKS) { if (x.a - 0.05 <= t) c = x; else break; } if (!c || t > c.b + 0.3) return null;
  const k = Math.min(1, (t - c.a + 0.05) / 0.14), s = 1.12 - 0.12 * k;
  // two-word phrases coloured as one
  const words = c.text.split(" "); const spans: React.ReactNode[] = []; for (let i = 0; i < words.length; i++) { const two = (words[i] + " " + (words[i + 1] ?? "")).toLowerCase(); const ph = [...BAD, ...GOOD].find((p) => p.includes(" ") && two.startsWith(p));
    if (ph) { const col = BAD.includes(ph) ? "#ff6a6a" : "#5dff9b"; spans.push(<span key={i} style={{ color: col }}>{words[i]} {words[i + 1]} </span>); i++; } else spans.push(<span key={i} style={{ color: hl(words[i]) }}>{words[i]} </span>); }
  return <div style={{ position: "absolute", left: 160, right: 160, bottom: 64, textAlign: "center", fontFamily: F, fontWeight: 800, fontSize: 54, lineHeight: 1.22, WebkitTextStroke: "9px rgba(12,10,20,.92)", paintOrder: "stroke fill", transform: `scale(${s})`, transformOrigin: "50% 100%", textShadow: "0 4px 14px rgba(0,0,0,.6)" } as React.CSSProperties}>{spans}</div>;
};

// ---------- fonts gate ----------
const FontGate: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [h] = useState(() => delayRender("fonts")); const [ok, setOk] = useState(false);
  useEffect(() => { const faces = [["BeVietnamPro-Medium.ttf", "500"], ["BeVietnamPro-SemiBold.ttf", "600"], ["BeVietnamPro-Bold.ttf", "700"], ["BeVietnamPro-ExtraBold.ttf", "800"], ["BeVietnamPro-Black.ttf", "900"]].map(([f, w]) => new FontFace("Be Vietnam Pro", `url(${staticFile("fonts/" + f)})`, { weight: w }));
    Promise.all(faces.map((x) => x.load().then((ff) => { document.fonts.add(ff); }))).then(() => { setOk(true); continueRender(h); }).catch(() => { setOk(true); continueRender(h); }); }, [h]);
  return ok ? <>{children}</> : null;
};

// ---------- composition ----------
export const DN1_FRAMES = TOTAL_F;
export const Dn1Video: React.FC = () => {
  const audio = (getInputProps() as { audio?: boolean }).audio;
  // group consecutive 3D segments of the same set into one Stage (one WebGL context per run)
  const groups: { set: SetKey; a: number; b: number; runs: Run[] }[] = [];
  for (const s of SEGS) if (s.k === "3d") { const A = fr(s.a), B = fr(s.b), g = groups[groups.length - 1];
    if (g && g.set === s.s.set && g.b === A) { g.runs.push({ a: A - g.a, b: B - g.a, s: s.s }); g.b = B; } else groups.push({ set: s.s.set, a: A, b: B, runs: [{ a: 0, b: B - A, s: s.s }] }); }
  const endA = fr(TIMING.total);
  return (
    <FontGate>
      <AbsoluteFill style={{ background: "#0b1124" }}>
        <FX>
        {groups.map((g, i) => <Sequence key={"g" + i} from={g.a} durationInFrames={g.b - g.a}><Stage set={g.set} runs={g.runs} /></Sequence>)}
        {SEGS.map((s, i) => { const A = fr(s.a), B = fr(s.b); if (B <= A) return null; const d = s.b - s.a;
          return <Sequence key={"s" + i} from={A} durationInFrames={B - A}><SegView seg={s} d={d} /></Sequence>; })}
        </FX>
        <Dip />
        <Sequence from={endA} durationInFrames={Math.max(1, TOTAL_F - endA)}><EndView /></Sequence>
        <Subs />
        {audio ? <Audio src={staticFile("dn1/voice.wav")} /> : null}
      </AbsoluteFill>
    </FontGate>
  );
};
// ---------- chuyển cảnh: mỗi lần cắt có lực (đẩy vào / lia ngang kèm nhoè), sang cảnh mới thì chìm tối rồi mở ra ----------
const CUTF = SEGS.map((x, i) => ({ f: fr(x.a), scene: i > 0 && SEGS[i - 1].id !== x.id, v: (parseInt(x.id.slice(1)) + x.n) % 3, end: fr(x.b), last: i + 1 >= SEGS.length || SEGS[i + 1].id !== x.id }));
const curCut = (f: number) => { let c = CUTF[0]; for (const x of CUTF) { if (x.f <= f) c = x; else break; } return c; };
const FX: React.FC<{ children: React.ReactNode }> = ({ children }) => { const f = useCurrentFrame(), c = curCut(f), dt = (f - c.f) / FPS;
  const e = 1 - Math.pow(1 - Math.min(1, dt / (c.scene ? 0.55 : 0.32)), 3), r = 1 - e;
  if (f < 8 || r < 0.002) return <AbsoluteFill>{children}</AbsoluteFill>;
  const tx = c.scene || c.v === 0 ? 0 : (c.v === 1 ? 34 : -34) * r, sc2 = 1 + (c.scene ? 0.09 : c.v === 0 ? 0.06 : 0.045) * r, blur = c.scene ? 0 : c.v === 0 ? 0 : 7 * r * r;
  return <AbsoluteFill style={{ transform: `translateX(${tx}px) scale(${sc2})`, filter: blur > 0.4 ? `blur(${blur.toFixed(1)}px)` : undefined }}>{children}</AbsoluteFill>; };
const Dip: React.FC = () => { const f = useCurrentFrame(), c = curCut(f), dt = (f - c.f) / FPS, out = c.last ? Math.max(0, 1 - (c.end - f) / 5) : 0;
  const inn = c.scene && f > 8 ? Math.max(0, 1 - dt / 0.3) : 0, k = Math.max(inn, out * 0.9); if (k < 0.01) return null;
  return <AbsoluteFill style={{ background: "#05060f", opacity: k }} />; };
const SegView: React.FC<{ seg: GSeg; d: number }> = ({ seg, d }) => { const t = useCurrentFrame() / FPS;
  return <AbsoluteFill>{seg.k === "card" ? seg.r(t, d) : seg.ov ? seg.ov(t, d) : null}</AbsoluteFill>; };
const EndView: React.FC = () => <EndCard t={useCurrentFrame() / FPS} />;
export { TAIL };
