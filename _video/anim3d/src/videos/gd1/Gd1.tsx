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
const at = (id: string, k: number, j: number) => { const s = sc(id); return s.sens[j].a - (k === 0 ? s.a : s.sens[k].a - 0.12); };
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
    <img src={staticFile(`gd1/${img}.jpg`)} style={{ width: 1600, height: 900, marginTop: -110, objectFit: "contain", opacity: a, transform: `scale(${0.97 + 0.03 * a + t * 0.002})` }} />
    {head && <div style={{ position: "absolute", top: 40, right: 80, padding: "10px 26px", borderRadius: 12, background: "#ffd23f", color: "#1a0f33", fontSize: 40, fontWeight: 900, opacity: sm((t - 0.6) / 0.3) }}>{head}</div>}
    {foot && <div style={{ position: "absolute", bottom: 175, width: "100%", textAlign: "center", fontSize: 26, color: "rgba(255,255,255,.6)" }}>{foot}</div>}</AbsoluteFill>; };
const Ask: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.5), clickT = t - 3.6, sub = clickT > 0.35;
  return <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><Bg t={t} hue="navy" />
    <div style={{ opacity: a, position: "relative" }}><div style={{ fontSize: 40, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>CÂU HỎI CHO ANH CHỊ</div>
      <div style={{ fontSize: 88, fontWeight: 900, color: "#fff", marginTop: 20, lineHeight: 1.15 }}>NHÀ ANH CHỊ ĐÃ CÓ<br />CÂU MẬT KHẨU CHƯA?</div>
      <div style={{ display: "inline-block", marginTop: 50, padding: "22px 64px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 48, fontWeight: 900 }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI KÊNH"}</div></div>
    {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 1060 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 820 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
    <div style={{ position: "absolute", left: 40, bottom: 22, fontSize: 28, fontWeight: 700, color: "rgba(255,255,255,.55)" }}>chungkhoanhuynguyen.com</div>
    <div style={{ position: "absolute", right: 40, bottom: 20, fontSize: 22, color: "rgba(255,255,255,.5)" }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư · Ảnh: Wikimedia Commons (CC BY / CC BY-SA)</div></AbsoluteFill>; };
const Photo: React.FC<{ t: number; img: string; d?: number; dir?: number }> = ({ t, img, d = 7, dir = 1 }) => { const k = Math.min(1, t / Math.max(d, 1)); const z = 1.06 + 0.08 * k;
  return <AbsoluteFill style={{ background: "#000" }}><img src={staticFile(`gd1/${img}.jpg`)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z}) translateX(${dir * (k - 0.5) * 30}px)`, filter: "brightness(.82) saturate(1.05)" }} />
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
const PH = (bg: string, fit: [number, number], cast: Cast[], cam: [[V, V, number], [V, V, number]], x: Partial<Shot3D> = {}) => S("photo", "room", cam[0], cam[1], cast, { bg: `gd1/${bg}.jpg`, bgFit: fit, ...x });
const pcam = (x = 0): [[V, V, number], [V, V, number]] => [[[x, 1.45, -3.2], [x, 1.25, 3], 42], [[x, 1.42, -2.8], [x, 1.25, 3], 40]];
const walkers = (n: number, z = 1.6): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (40 + i), [i % 2 ? 2.6 : -2.2, 0, z + i * 0.35], (t: number) => ({ ...P(i % 3 ? "neutral" : "smile", { acc: i % 2 ? ["box"] : ["phone"] })(t), mode: "stroll", phase: (t * 1.4 + i * 0.3) % 1, side: i % 2 ? 1 : -1 }), [i % 2 ? -2.4 : 2.8, 0, z + i * 0.35]));
const VCall: React.FC<{ t: number; name: string; lines: string[]; blur?: boolean; end?: number }> = ({ t, name, lines, blur = true, end }) => { const a = sm(t / 0.4), gone = end !== undefined && t > end;
  return <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 40%,#1b2340,#05070f)", fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <div style={{ width: 600, height: 960, borderRadius: 60, background: "#0d1326", border: "10px solid #2a3350", overflow: "hidden", position: "relative", opacity: a }}>
      <div style={{ position: "absolute", inset: 0, background: "linear-gradient(180deg,#3a2a40,#1a1222)", filter: blur ? `blur(${4 + Math.sin(t * 9) * 2}px)` : undefined }}>
        <div style={{ position: "absolute", left: 150, top: 230, width: 300, height: 360, borderRadius: "50% 50% 45% 45%", background: "#f2c9a8", opacity: gone ? 0.15 : 0.9 }} />
        <div style={{ position: "absolute", left: 110, top: 170, width: 380, height: 260, borderRadius: "50% 50% 10% 10%", background: "#5a3322", opacity: gone ? 0.15 : 1 }} /></div>
      <div style={{ position: "absolute", top: 40, width: "100%", textAlign: "center", color: "#fff", fontSize: 40, fontWeight: 800 }}>📹 {name}</div>
      {gone ? <div style={{ position: "absolute", top: 440, width: "100%", textAlign: "center", color: "#ff4d5e", fontSize: 50, fontWeight: 900 }}>Cuộc gọi đã kết thúc</div>
        : <div style={{ position: "absolute", bottom: 60, left: 30, right: 30, color: "#fff", fontSize: 36, fontWeight: 700, textAlign: "center" }}>{lines.map((l, i) => <div key={i} style={{ opacity: sm((t - 0.6 - i * 1.4) / 0.3) }}>{l}</div>)}</div>}
    </div></AbsoluteFill>; };
const Bio: React.FC<{ t: number; at0?: number }> = ({ t, at0 = 0.6 }) => { const a = sm((t - at0) / 0.35), r = 140 + Math.sin(t * 4) * 6;
  return <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 40%,#1b2340,#05070f)", fontFamily: F, justifyContent: "center", alignItems: "center" }}>
    <div style={{ width: 620, height: 960, borderRadius: 60, background: "#0d1326", border: "10px solid #2a3350", padding: 50, boxSizing: "border-box", textAlign: "center" }}>
      <div style={{ marginTop: 20, fontSize: 44, color: "#dfe6f8", fontWeight: 800 }}>🏦 Chuyển tiền</div>
      <div style={{ marginTop: 40, fontSize: 80, color: "#ffd23f", fontWeight: 900 }}>50.000.000 đ</div>
      <div style={{ margin: "70px auto 0", width: r * 2, height: r * 2.4, borderRadius: "50%", border: "8px dashed #4dd2ff", opacity: a }} />
      <div style={{ marginTop: 50, fontSize: 40, color: "#4dd2ff", fontWeight: 800, opacity: a }}>Vui lòng xác thực khuôn mặt</div>
    </div></AbsoluteFill>; };
const Clues: React.FC<{ t: number; title: string; items: { text: string; at: number; ok?: string }[]; src?: string }> = ({ t, title, items, src }) =>
  <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center" }}><Bg t={t} hue="night" />
    <div style={{ width: 1400 }}><div style={{ fontSize: 46, fontWeight: 900, color: "#ffd23f", letterSpacing: 3, marginBottom: 30, opacity: sm(t / 0.3) }}>🔍 {title}</div>
      {items.map((x, i) => { const a = sm((t - x.at) / 0.35), ok = x.ok && t > x.at + 1.2; return <div key={i} style={{ display: "flex", alignItems: "center", gap: 30, marginTop: 24, padding: "22px 34px", borderRadius: 20, background: "rgba(255,210,63,.08)", border: "3px solid " + (ok ? "#5dff9b" : "rgba(255,210,63,.6)"), opacity: a, transform: `translateX(${(1 - a) * 80}px)` }}>
        <div style={{ fontSize: 64, fontWeight: 900, color: "#ffd23f", width: 70 }}>{i + 1}</div><div style={{ fontSize: 48, fontWeight: 800, color: "#fff", flex: 1 }}>{x.text}</div>
        {ok && <div style={{ fontSize: 40, fontWeight: 900, color: "#5dff9b" }}>{x.ok}</div>}</div>; })}
      {src && <div style={{ marginTop: 24, fontSize: 26, color: "rgba(255,255,255,.55)" }}>{src}</div>}</div></AbsoluteFill>;
const wideB = (set: Shot3D["set"], a: string, e: Expr, o: PO = {}, light: Shot3D["light"] = "room") => S(set, light, [[1.9, 1.5, 3.4], [NX, 1.0, RZ], 34], [[1.75, 1.47, 3.0], [NX, 1.0, RZ], 32], [C(a, [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }))], RM);
const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => CD((t) => <VCall t={t} name="Kiều 💕" lines={[]} />)],
    [1, () => D3(wideB("canhovip", "bohung", "neutral", { acc: ["phone", "glow"] }, "roomdim"), (t) => <><ClockTag t={t} text="22:00" /><BigText t={t} at={0.3} text="THẬT TỆ KHI…" col="#ffd23f" y={90} size={110} /></>)],
    [3, () => CD((t) => <VCall t={t} name="Kiều 💕" lines={["Bố ơi, con đâm xe…", "Người ta giữ con ở đây", "Bố chuyển gấp cho con 50 triệu!"]} />)],
  ] },
  { id: "S02", shots: [
    [0, () => CD((t) => <VCall t={t} name="Kiều 💕" lines={["…"]} end={1.2} />)],
    [1, () => CD((t) => <PhoneCard t={t} time="22:01" date="Tin nhắn" notifs={[{ app: "Tin nhắn", col: "#ff4d5e", title: "Bố chuyển vào tài khoản này giúp con", body: "STK 0xxx xxx · NGUYEN VAN X", at: 0.3 }]} hue="red" />)],
    [2, () => D3(wideB("canhovip", "bohung", "nervous", { acc: ["phone", "glow", "sweat"] }, "roomdim"))],
    [3, () => CD((t) => <Clues t={t} title="NHỚ 3 CHI TIẾT" items={[{ text: "Con gọi bằng “BỐ”", at: 1.4 }, { text: "Cuộc gọi chỉ 10 giây", at: 2.8 }, { text: "Tài khoản đứng tên người lạ", at: 4.0 }]} />)],
  ] },
  { id: "S03", shots: [
    [0, () => D3(closeL("cafe", "kieu", "laugh", { acc: ["phone", "glow"] }), (t) => <><BigText t={t} at={0.3} text="KIỀU SOCIU" col="#ffd23f" y={90} size={120} /><LocTag t={t} l1="31 tuổi · quen nửa thành phố" /></>)],
    [2, () => CD(PR("cafe", (t) => <BigText t={t} at={0.3} text="3 VIDEO MỖI NGÀY" col="#fff" y={90} size={110} />))],
    [3, () => CD((t) => <Big2 t={t} head="Tất cả đều có trên mạng" items={[{ a: "😀", b: "mặt", at: 0.2, col: "#ffd23f" }, { a: "🎙", b: "giọng", at: 0.8, col: "#ffd23f" }, { a: "👨‍👩‍👧", b: "tên bố mẹ", at: 1.6, col: "#ff4d5e" }]} />)],
    [4, () => D3(closeL("cafe", "kieu", "laugh", { acc: ["phone"] }), (t) => <BigText t={t} at={rel("S03", 5, sc("S03").sens[4].a)} text="“BA”, KHÔNG BAO GIỜ “BỐ”" col="#ffd23f" y={90} size={100} />)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(PH("gym", [0.5, 0.6], [C("dung", [0.4, 0, 0.7], P("stern", { side: -1, mode: "stand", acc: ["muscle"] }))], pcam(0.4)), (t) => <><BigText t={t} at={0.3} text="DŨNG GYMMER" col="#ffd23f" y={90} size={120} /><LocTag t={t} l1="Huấn luyện viên phòng tập" l2="Ít nói, cẩn thận" /></>)],
    [1, () => D3(S("cafe", "room", ...roomTwo2, [C("dung", [LX, 0, RZ], P("stern", { side: 1, mode: "stand", wave: 1 })), C("kieu", [NX, 0, RZ], P("laugh", { side: -1, mode: "stand", acc: ["phone"] }))], RM), (t) => <>{BL(120, 110, "Em đăng ít thôi, kẻ gian nó lấy giọng em đi lừa đấy.", 0.2)(t)}{BL(1060, 330, "Anh lại lo xa rồi, ai rảnh mà làm thế!", rel("S04", 2, sc("S04").sens[1].a), "r")(t)}</>)],
  ] },
  { id: "S05", shots: [
    [0, () => CD((t) => <Big2 t={t} items={[{ a: "CÓ NGƯỜI RẢNH", b: "", at: 0.1, col: "#ff4d5e" }]} />)],
    [1, () => CD((t) => <Big2 t={t} head="Lừa đảo trên mạng ở Việt Nam, 11 tháng năm 2025" src="Bộ Công an, qua NCA – báo SGGP 7/1/2026" items={[{ a: ">6.000 tỷ", b: "thiệt hại ước tính", at: 0.4, col: "#ff4d5e" }]} />)],
    [2, () => CD((t) => <NewsCard t={t} tag="CẢNH BÁO 2026" items={[{ src: "Chuyên gia an ninh mạng (NCA)", head: "Kẻ gian sẽ dùng giả mặt, giả giọng bằng AI nhiều hơn", at: 0.3, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S06", shots: [
    [0, () => CD((t) => <Big2 t={t} items={[{ a: "?", b: "làm sao họ có mặt và giọng của Kiều", at: 0.2, col: "#ffd23f" }]} />)],
    [2, () => CD((t) => <LessonCard t={t} title="Kẻ gian cần gì?" items={[{ n: "1", icon: "🎙", head: "Vài chục giây video có tiếng", body: "đủ để bắt chước giọng", at: 0.2 }, { n: "2", icon: "📷", head: "Vài tấm ảnh rõ mặt", body: "ghép vào cuộc gọi video ngắn, hình hơi mờ", at: at("S06", 2, 3) }, { n: "3", icon: "😰", head: "Người nghe đang hoảng loạn", body: "là đủ để tin", at: at("S06", 2, 3) + 3 }]} />)],
  ] },
  { id: "S07", shots: [
    [0, () => D3(wideB("canhovip", "bohung", "nervous", { acc: ["phone", "glow"] }, "roomdim"), (t) => <LocTag t={t} l1="ÔNG HÙNG" l2="Bố của Kiều" />)],
    [1, () => CD((t) => <BankCard t={t} clock="22:03" amt="50.000.000 đ" note="Đang chuyển…" />)],
    [3, () => CD((t) => <Bio t={t} />)],
  ] },
  { id: "S08", shots: [
    [0, () => CD((t) => <Rows t={t} title="Từ 1/7/2024: phải xác thực khuôn mặt khi" foot="Quyết định 2345/QĐ-NHNN" rows={[{ l: "Chuyển trên 10 triệu đồng/lần", v: "✓", at: 0.6, big: true }, { l: "Tổng trên 20 triệu đồng/ngày", v: "✓", at: 2.0 }]} />)],
    [1, () => D3(wideB("canhovip", "bohung", "dazed", { acc: ["phone", "glow"] }, "roomdim"), (t) => <BigText t={t} at={0.3} text="KHỰNG LẠI" col="#4dd2ff" y={90} size={130} />)],
  ] },
  { id: "S09", shots: [
    [0, () => D3(S("canhovip", "room", ...roomTwo2, [C("dung", [LX, 0, RZ], P("stern", { side: 1, mode: "stand", wave: 1 })), C("bohung", [NX, 0, RZ], P("neutral", { side: -1, mode: "stand" }))], RM), (t) => <ClockTag t={t} text="HỒI TẾT" />)],
    [2, () => CD((t) => <LessonCard t={t} title="Lời dặn của Dũng" items={[{ n: "1", icon: "📵", head: "Ai gọi xin tiền gấp, dù là ai", body: "cúp máy, gọi lại số cũ", at: 0.2 }, { n: "2", icon: "🔑", head: "Hỏi câu mật khẩu của nhà mình", body: "", at: at("S09", 2, 3) }]} />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(wideB("canhovip", "bohung", "worried", { acc: ["phone", "glow"] }, "roomdim"), (t) => <>{BL(1000, 110, "Dũng ơi, Kiều đâm xe à?", rel("S10", 1, sc("S10").a), "r")(t)}</>)],
    [2, () => D3(PH("gym", [0.5, 0.6], [C("dung", [-0.15, 0, 0.7], P("neutral", { side: -1, mode: "stand", acc: ["phone"] })), C("kieu", [0.95, 0, 0.7], P("smile", { side: 1, mode: "stand" }))], pcam(0.4)), (t) => <><LocTag t={t} l1="PHÒNG TẬP" l2="Cùng lúc đó" />{BL(120, 110, "Dạ không bố ơi, Kiều đang ngồi cạnh con đây.", rel("S10", 3, sc("S10").sens[2].a))(t)}</>)],
  ] },
  { id: "S11", shots: [
    [0, () => D3(PH("gym", [0.5, 0.6], [C("kieu", [0.4, 0, 0.7], P("worried", { side: -1, mode: "stand", acc: ["phone"] }))], pcam(0.4)), (t) => <>{BL(1000, 110, "Ba ơi, con đây.", 0.2, "r")(t)}</>)],
    [2, () => D3(wideB("canhovip", "bohung", "stern", { acc: ["phone", "glow"] }, "roomdim"), (t) => <>{BL(1000, 110, "Con mèo nhà mình hồi bé tên gì?", 0.3, "r")(t)}</>)],
    [3, () => D3(PH("gym", [0.5, 0.6], [C("kieu", [0.4, 0, 0.7], P("laugh", { side: -1, mode: "stand", acc: ["phone", "tears"] }))], pcam(0.4)), (t) => <BigText t={t} at={0.5} text="🐱 BÁNH BAO" col="#ffd23f" y={90} size={140} />)],
  ] },
  { id: "S12", shots: [
    [0, () => D3(wideB("canhovip", "bohung", "relief", {}, "roomdim"), (t) => <BigText t={t} at={0.6} text="50 TRIỆU = 3 THÁNG LƯƠNG HƯU" col="#5dff9b" y={90} size={90} />)],
    [2, () => CD((t) => <Rows t={t} title="Dũng làm ngay" rows={[{ l: "Chụp lại số tài khoản lạ", v: "📸", at: 0.4 }, { l: "Báo công an phường", v: "🚓", at: 1.6, big: true }, { l: "Báo ngân hàng", v: "🏦", at: 2.8 }]} />)],
  ] },
  { id: "S13", shots: [
    [0, () => D3(closeL("canho", "kieu", "sad", { acc: ["phone", "glow"] }, "roomdim"), (t) => <BigText t={t} at={0.4} text="XÓA TỪNG VIDEO CŨ" col="#fff" y={90} size={110} />)],
    [2, () => CD((t) => <Big2 t={t} items={[{ a: "🧩", b: "mỗi video là một mảnh ghép để dựng một Kiều giả", at: 0.3, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S14", shots: [
    [0, () => D3(closeR("cafe", "huy", "neutral"), (t) => <LocTag t={t} l1="HUY NGUYỄN" l2="Trong đầu tư cũng vậy" />)],
    [2, () => CD((t) => <PhoneCard t={t} time="20:15" date="Nhóm kín" notifs={[{ app: "Video quảng cáo", col: "#ff4d5e", title: "“Chuyên gia” mời vào nhóm VIP", body: "Cam kết lợi nhuận 10%/tháng", at: 0.3 }]} hue="red" />)],
    [3, () => CD((t) => <Big2 t={t} items={[{ a: "MẶT THẬT", b: "", at: 0.1, col: "#5dff9b" }, { a: "LỜI MỜI GIẢ", b: "", at: 1.2, col: "#ff4d5e" }]} />)],
    [4, () => D3(PH("gym", [0.5, 0.6], [C("dung", [0.4, 0, 0.7], P("smile", { side: -1, mode: "stand", acc: ["muscle"] }))], pcam(0.4)), (t) => <BigText t={t} at={0.6} text="KHÔNG CÓ ĐƯỜNG TẮT" col="#ffd23f" y={90} size={120} />)],
  ] },
  { id: "S15", shots: [
    [0, () => D3(closeR("cafe", "huy", "neutral"), (t) => <LocTag t={t} l1="HUY NGUYỄN" l2="Nhìn lại 3 chi tiết đầu phim" />)],
    [1, () => CD((t) => <Clues t={t} title="3 CHI TIẾT ĐẦU PHIM" items={[{ text: "Gọi “bố” – Kiều chỉ gọi “ba”", at: 0.2, ok: "GIẢ" }, { text: "Chỉ 10 giây – giả lâu là lộ", at: at("S15", 1, 2), ok: "GIẢ" }, { text: "Tài khoản người lạ – con thật không làm thế", at: at("S15", 1, 3), ok: "GIẢ" }]} />)],
    [4, () => CD((t) => <Big2 t={t} items={[{ a: "10 GIÂY", b: "bình tĩnh, không cần công nghệ nào", at: 0.2, col: "#5dff9b" }]} />)],
  ] },
  { id: "S16", shots: [[0, () => CD((t) => <LessonCard t={t} title="1. Kiểm tra lại bằng kênh khác" items={[{ n: "1", icon: "📵", head: "Cúp máy", body: "", at: at("S16", 0, 2) }, { n: "2", icon: "📞", head: "Gọi lại số cũ đã lưu", body: "không gọi lại số vừa gọi đến", at: at("S16", 0, 2) + 1.2 }]} />)]] },
  { id: "S17", shots: [[0, () => CD((t) => <LessonCard t={t} title="2. Câu mật khẩu của cả nhà" items={[{ n: "1", icon: "🔑", head: "Chỉ người trong nhà mới biết", body: "không bao giờ đăng lên mạng", at: at("S17", 0, 2) }, { n: "2", icon: "🐱", head: "Tên con mèo, món ăn hồi bé…", body: "", at: at("S17", 0, 3) }]} />)]] },
  { id: "S18", shots: [[0, () => CD((t) => <LessonCard t={t} title="3. Bớt mảnh ghép trên mạng" items={[{ n: "1", icon: "🎙", head: "Bớt đăng giọng + mặt rõ + thông tin gia đình", body: "", at: at("S18", 0, 1) }, { n: "2", icon: "🔒", head: "Chế độ riêng tư", body: "cho những gì không cần công khai", at: at("S18", 0, 2) }]} />)]] },
  { id: "S19", shots: [[0, () => CD((t) => <LessonCard t={t} title="4. Bảo vệ bố mẹ lớn tuổi" items={[{ n: "1", icon: "📉", head: "Đặt hạn mức chuyển khoản thấp", body: "", at: at("S19", 0, 1) }, { n: "2", icon: "⏳", head: "Không ai thật bắt chuyển tiền trong vài phút", body: "ngân hàng, công an hay con cái", at: at("S19", 0, 1) + 3 }]} />)]] },
  { id: "S20", shots: [
    [0, () => D3(wideB("canhovip", "bohung", "smile", { acc: ["phone", "glow"] }), (t) => <BigText t={t} at={0.4} text="XEM ÍT HƠN, GỌI NHIỀU HƠN" col="#5dff9b" y={90} size={96} />)],
    [3, () => CD((t) => <Big2 t={t} items={[{ a: "🐱", b: "bí mật quan trọng nhất của cả nhà", at: 0.3, col: "#ffd23f" }]} />)],
  ] },
  { id: "S21", shots: [[0, () => CD((t) => <Ask t={t} />)]] },
];
function teaStall() { return [] as Cast[]; }



const Meme: React.FC<{ t: number; at?: number; top: string; bot: string; small?: boolean; noSubGap?: boolean; y?: number }> = ({ t, at = 0, top, bot, small, noSubGap, y }) => { if (t < at) return null; const a = Math.min(1, (t - at) / 0.18), sz = small ? 150 : 92;
  const st = { position: "absolute", left: 0, width: 1920, textAlign: "center", fontFamily: F, fontWeight: 900, fontSize: sz, color: "#fff", WebkitTextStroke: "10px #000", paintOrder: "stroke fill", letterSpacing: 1, transform: `scale(${1.25 - 0.25 * a})`, opacity: a } as React.CSSProperties;
  return <>{top && <div style={{ ...st, top: 70 }}>{top}</div>}{bot && <div style={{ ...st, top: y ?? (small ? 690 : noSubGap ? 175 : 620), color: small ? "#ffe14d" : "#fff", fontSize: small ? 130 : sz }}>{bot}</div>}</>; };



type GSeg = Seg & { a: number; b: number; id: string; n: number };
export const SEGS: GSeg[] = (() => {
  const out: GSeg[] = [];
  for (const p of PLAN) { const S0 = sc(p.id);
    p.shots.forEach(([j, mk], k) => { const a = k === 0 ? S0.a : S0.sens[j].a - 0.12, nb = k + 1 < p.shots.length ? S0.sens[p.shots[k + 1][0]].a - 0.12 : S0.b; out.push({ ...mk(a), a, b: nb, id: p.id, n: k }); }); }
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
export const GD1_FRAMES = TOTAL_F;
export const Gd1Video: React.FC = () => {
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
        {audio ? <Audio src={staticFile("gd1/voice.wav")} /> : null}
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
