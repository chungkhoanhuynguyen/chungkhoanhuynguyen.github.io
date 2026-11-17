// Phim 3D PNJ1 "Thật tệ khi chiếc nhẫn cầu hôn kéo theo nửa tiền cưới". Khung 1920x1080, 30 fps.
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
    <img src={staticFile(`pnj1/${img}.jpg`)} style={{ width: 1600, height: 900, marginTop: -110, objectFit: "contain", opacity: a, transform: `scale(${0.97 + 0.03 * a + t * 0.002})` }} />
    {head && <div style={{ position: "absolute", top: 40, right: 80, padding: "10px 26px", borderRadius: 12, background: "#ffd23f", color: "#1a0f33", fontSize: 40, fontWeight: 900, opacity: sm((t - 0.6) / 0.3) }}>{head}</div>}
    {foot && <div style={{ position: "absolute", bottom: 175, width: "100%", textAlign: "center", fontSize: 26, color: "rgba(255,255,255,.6)" }}>{foot}</div>}</AbsoluteFill>; };
const Ask: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.5), clickT = t - 3.6, sub = clickT > 0.35;
  return <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><Bg t={t} hue="navy" />
    <div style={{ opacity: a, position: "relative" }}><div style={{ fontSize: 40, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>CÂU HỎI CHO ANH CHỊ</div>
      <div style={{ fontSize: 88, fontWeight: 900, color: "#fff", marginTop: 20, lineHeight: 1.15 }}>MÃ GIẢM SÂU TRONG TAY<br />ANH CHỊ ĐANG CHỜ ĐIỀU GÌ?</div>
      <div style={{ display: "inline-block", marginTop: 50, padding: "22px 64px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 48, fontWeight: 900 }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI KÊNH"}</div></div>
    {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 1060 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 820 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
    <div style={{ position: "absolute", left: 40, bottom: 22, fontSize: 28, fontWeight: 700, color: "rgba(255,255,255,.55)" }}>chungkhoanhuynguyen.com</div>
    <div style={{ position: "absolute", right: 40, bottom: 20, fontSize: 22, color: "rgba(255,255,255,.5)" }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư · Ảnh: Wikimedia Commons (CC BY / CC BY-SA)</div></AbsoluteFill>; };
const Photo: React.FC<{ t: number; img: string; d?: number; dir?: number }> = ({ t, img, d = 7, dir = 1 }) => { const k = Math.min(1, t / Math.max(d, 1)); const z = 1.06 + 0.08 * k;
  return <AbsoluteFill style={{ background: "#000" }}><img src={staticFile(`pnj1/${img}.jpg`)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z}) translateX(${dir * (k - 0.5) * 30}px)`, filter: "brightness(.82) saturate(1.05)" }} />
    <AbsoluteFill style={{ background: "linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 28%,rgba(0,0,0,0) 62%,rgba(0,0,0,.55) 100%)" }} /></AbsoluteFill>; };
const PR = (img: string, ov?: (t: number) => React.ReactNode, dir = 1) => (t: number) => <><Photo t={t} img={img} dir={dir} />{ov?.(t)}</>;
// ---------- dàn cảnh ----------
// Phòng trọ (room): máy nhìn −z → +x bên PHẢI màn. Toàn trái màn (side +1), Hằng phải màn (side −1).
const roomTwo2: [[V, V, number], [V, V, number]] = [[[0, 1.5, 4.2], [0, 1.15, 0.7], 40], [[0, 1.45, 3.6], [0, 1.15, 0.7], 36]];
const LX = -0.7, NX = 0.7, RZ = 0.8;
const HOME: Shot3D["set"] = "canho";
const toan = (e: Expr, o: PO = {}) => C("toanbop", [LX, 0, RZ], P(e, { side: 1, mode: "stand", ...o }));
const hang = (e: Expr, o: PO = {}) => C("nv", [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }));
const RM = { chat: "off" as const, game: false };
const PH = (bg: string, fit: [number, number], cast: Cast[], cam: [[V, V, number], [V, V, number]], x: Partial<Shot3D> = {}) => S("photo", "room", cam[0], cam[1], cast, { bg: `pnj1/${bg}.jpg`, bgFit: fit, ...x });
const pcam = (x = 0): [[V, V, number], [V, V, number]] => [[[x, 1.45, -3.2], [x, 1.25, 3], 42], [[x, 1.42, -2.8], [x, 1.25, 3], 40]];
const pclose = (x = 0.4): [[V, V, number], [V, V, number]] => [[[x, 1.4, -2.2], [x, 1.2, 3], 38], [[x, 1.38, -1.9], [x, 1.2, 3], 36]];
const duo = (a: string, ea: Expr, b: string, eb: Expr, oa: PO = {}, ob: PO = {}): Cast[] => [C(a, [-0.15, 0, 0.7], P(ea, { side: -1, mode: "stand", ...oa })), C(b, [0.95, 0, 0.7], P(eb, { side: 1, mode: "stand", ...ob }))];
const BL = (x: number, y: number, text: string, at0: number, tail: "l" | "r" = "l") => (t: number) => <Bubble t={t} at={at0} text={text} x={x} y={y} tail={tail} w={640} />;
const closeT = (e: Expr, o: PO = {}, light: Shot3D["light"] = "roomdim") => S(HOME, light, [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [toan(e, o)], RM);
const thumb = (e: Expr, o: PO = {}) => S(HOME, "roomdim", [[0.75, 1.35, 2.7], [LX, 1.05, RZ], 36], [[0.65, 1.32, 2.25], [LX, 1.05, RZ], 32], [toan(e, { acc: ["phone", "glow"], ...o })], { ...RM, shake: 0.2 });
// tiệm vàng chỗ Hằng (phố ban ngày) + hàng người bán lại nhẫn
const qx = (i: number) => GOLD_X + 1.4 + i * 1.15;
const queue = (n = 20, e: Expr = "worried"): Cast[] => Array.from({ length: n }, (_, i) => C("c" + i, [qx(i), 0.15, 5.25 + (i % 2) * 0.25], P(i % 3 === 1 ? "shock" : e, { mode: "stand", acc: i % 2 ? ["box"] : ["phone"], phase: i * 0.37, side: 1 })));
const shopDay = (cast: Cast[], from: [V, V, number], to: [V, V, number], x: Partial<Shot3D> = {}) => S("streetday", "day", from, to, cast, x);
const qWide: [[V, V, number], [V, V, number]] = [[[qx(14), 9, -4], [qx(8), 1.4, 5.3], 50], [[qx(7), 3.5, 0], [qx(6), 1.3, 5.3], 46]];
const qPan: [[V, V, number], [V, V, number]] = [[[GOLD_X - 1, 1.6, 1.8], [GOLD_X + 3, 1.3, 5.4], 46], [[qx(16), 1.6, 1.8], [qx(20), 1.3, 5.4], 46]];
const HQ: V = [GOLD_X + 0.3, 0.15, 5.1];
// trong cửa hàng trang sức lớn
const shopIn = (te: Expr, he: Expr, ce: Expr = "smile", x: Partial<Shot3D> = {}) => S("shop", "day", [[-2.2, 1.7, 3.6], [0, 1.2, -1], 46], [[-1.4, 1.55, 2.6], [0, 1.2, -1], 42], [C("toanbop", [0.5, 0, 0.55], P(te)), C("nv", [1.3, 0, 0.6], P(he, { side: -1 })), C("clerk", [0, 0, -1.4], P(ce)), ...runners(4, -3, -3.2, 1.8)], x);

// quán trà đá đầu hẻm (phố ban ngày, cạnh tiệm vàng): +x bên TRÁI màn
const TT: V = [GOLD_X + 6.3, 0.15, 5.45], TH: V = [GOLD_X + 7.45, 0.15, 5.3];
const tea = (te: Expr, he: Expr, ot: PO = {}, oh: PO = {}): Cast[] => [C("toanbop", TT, P(te, { side: -1, ...ot })), C("huy", TH, P(he, { side: 1, acc: ["cup"], ...oh })), ...queue(3, "neutral").map((c, i) => ({ ...c, p: [GOLD_X - 2 - i * 1.2, 0.15, 5.4] as V }))];
const teaW: [[V, V, number], [V, V, number]] = [[[GOLD_X + 9.4, 1.5, 2.6], [GOLD_X + 6.9, 1.15, 5.5], 44], [[GOLD_X + 8.8, 1.45, 3.1], [GOLD_X + 6.9, 1.15, 5.5], 40]];
const teaT: [[V, V, number], [V, V, number]] = [[[GOLD_X + 5.6, 1.4, 3.4], [GOLD_X + 6.3, 1.3, 5.45], 36], [[GOLD_X + 5.8, 1.4, 3.8], [GOLD_X + 6.3, 1.32, 5.45], 32]];
const teaH: [[V, V, number], [V, V, number]] = [[[GOLD_X + 8.2, 1.4, 3.4], [GOLD_X + 7.45, 1.3, 5.3], 36], [[GOLD_X + 8.0, 1.4, 3.8], [GOLD_X + 7.45, 1.32, 5.3], 32]];
// trước cửa nhà bà Tư (phố, HX): bà Tư phải màn, khách trái màn
const bt = (e: Expr, o: PO = {}) => C("mehung", [HX - 0.55, 0.15, 5.3], P(e, { side: -1, ...o }));
const guest = (a: string, e: Expr, o: PO = {}) => C(a, [HX + 0.55, 0.15, 5.3], P(e, { side: 1, ...o }));
const hx2 = two(HX), hxT = (x: number): [[V, V, number], [V, V, number]] => [[[x - 0.3, 1.45, 3.4], [x, 1.3, 5.3], 34], [[x - 0.2, 1.42, 3.8], [x, 1.32, 5.3], 30]];
// Hằng trong tiệm (cạnh quầy)
const hangShop = (e: Expr, o: PO = {}) => C("nv", HQ, P(e, { side: -1, ...o }));
const hqT: [[V, V, number], [V, V, number]] = [[[GOLD_X + 0.9, 1.45, 3.4], [GOLD_X + 0.3, 1.3, 5.1], 34], [[GOLD_X + 0.7, 1.42, 3.8], [GOLD_X + 0.3, 1.32, 5.1], 30]];
const night = (cast: Cast[], cam: [[V, V, number], [V, V, number]], x: Partial<Shot3D> = {}) => S("street", "night", cam[0], cam[1], cast, x);

const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => D3(S(HOME, "roomdim", [[2.4, 2.4, 3.6], [LX, 1.0, RZ], 52], [[1.0, 1.4, 2.4], [LX, 1.0, RZ], 38], [toan("nervous", { acc: ["phone", "glow"] })], { ...RM, rain: true, ease: "out" }), (t) => <BigText t={t} at={0.4} text="THẬT TỆ KHI…" col="#ffd23f" y={90} size={120} />)],
    [1, () => D3(S(HOME, "roomdim", [[1.6, 1.6, 2.6], [LX, 1.0, RZ], 42], [[1.0, 1.4, 2.1], [LX, 1.0, RZ], 36], [toan("nervous", { acc: ["phone", "glow", "sweat"] })], { ...RM, rain: true }), (t) => <><ClockTag t={t} text="23:40 · 20/10" /><LocTag t={t} l1="PHÒNG TRỌ · PHÚ NHUẬN" l2="TP. Hồ Chí Minh" /></>)],
    [2, () => CD((t) => <PhoneCard t={t} time="23:41" date="20/10" notifs={[{ app: "Bảng giá", col: "#b03ad0", title: "PNJ  19,75  ▲ TRẦN", body: "Dư mua 4 triệu cổ phiếu", at: 0.3 }, { app: "Tin nhắn", col: "#2ecc71", title: "Phú Dê Già", body: "Có người đang gom, vào nốt đi mày!", at: at("S01", 2, 3) }]} hue="night" />)],
    [4, () => D3(thumb("nervous", { anim: true }), (t) => <BigText t={t} at={0.3} text="200 TRIỆU CUỐI CÙNG" col="#ffd23f" y={90} size={100} />)],
    [5, () => D3(S(HOME, "roomdim", [[0.65, 1.32, 2.25], [LX, 1.05, RZ], 32], [[0.5, 1.25, 1.5], [LX, 1.1, RZ], 22], [toan("shock", { acc: ["phone", "glow", "sweat"], anim: true })], { ...RM, shake: 0.4 }))],
  ] },
  { id: "S02", shots: [[0, () => D3(S(HOME, "roomdim", [[0.55, 1.26, 1.6], [LX, 1.05, RZ], 26], [[2.2, 2.2, 3.4], [LX, 1.0, RZ], 50], [toan("nervous", { acc: ["phone", "glow"] })], { ...RM, ease: "out" }), (t) => <BigText t={t} at={0.1} text="KHOAN ĐÃ…" col="#fff" y={100} size={120} />)],
    [1, () => D3(S("streetday", "day", [[HX + 12, 6, -2], [HX + 2, 1.2, 5.3], 50], [[HX + 4, 2.2, 1.5], [HX, 1.2, 5.3], 44], [C("toanbop", [HX + 5, 0.15, 5.0], walk("grin", { side: 1 }), [HX + 1.5, 0.15, 5.0]), ...runners(3, HX + 8, HX - 4, 4.4)], { ease: "sm" }), (t) => <LocTag t={t} l1="8 THÁNG TRƯỚC" l2="Một con hẻm ở Phú Nhuận, Sài Gòn" />)]] },
  { id: "S03", shots: [
    [0, () => D3(S("streetday", "day", [[HX + 1.2, 1.45, 3.2], [HX + 0.55, 1.25, 5.3], 36], [[HX + 1.0, 1.42, 3.7], [HX + 0.55, 1.28, 5.3], 32], [guest("toanbop", "grin", { acc: ["box"] })]), (t) => <><BigText t={t} at={0.3} text="TOÀN BỚP" col="#ffd23f" y={170} size={120} /><LocTag t={t} l1="31 tuổi · thợ điện" /></>)],
    [1, () => D3(S("streetday", "day", ...hx2, [guest("toanbop", "stern", { wave: 1 }), C("bohung", [HX - 0.55, 0.15, 5.3], P("worried", { side: -1 }))]), (t) => <>{BL(1060, 110, "Láo nháo anh cắt điện cả khu!", 0.2, "r")(t)}</>)],
    [2, () => D3(night([C("toanbop", [HOME_X + 3.6, 0.15, 5.3], walk("smile", { side: 1, acc: ["box"] }), [HOME_X + 2.2, 0.15, 5.3])], [[[HOME_X + 4, 1.5, 2.4], [HOME_X + 3.6, 1.2, 5.3], 42], [[HOME_X + 3.8, 1.45, 2.9], [HOME_X + 3.0, 1.2, 5.3], 38]]), (t) => <><ClockTag t={t} text="00:30" />{BL(120, 120, "Có anh đây, đừng lo!", 0.8)(t)}</>)],
    [3, () => D3(closeT("smile", { acc: ["paper"] }, "room"), (t) => <BigText t={t} at={0.5} text="400 TRIỆU ĐỂ CƯỚI" col="#5dff9b" y={90} size={110} />)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(shopDay([hangShop("smile"), ...queue(3, "smile")], [[GOLD_X + 3.4, 1.5, 2.4], [GOLD_X + 1.0, 1.3, 5.2], 40], [[GOLD_X + 3.0, 1.45, 2.9], [GOLD_X + 1.0, 1.3, 5.2], 36]), (t) => <><BigText t={t} at={0.4} text="HẰNG HỘT XOÀN" col="#ffd23f" y={170} size={110} /><LocTag t={t} l1="TIỆM VÀNG ĐẦU CHỢ BÀ CHIỂU" /></>)],
    [1, () => D3(S("streetday", "day", ...hx2, [bt("stern", { wave: 1 }), guest("nv", "smile")]), (t) => <>{BL(1060, 110, "Con lấy ai cũng được, miễn đừng có nợ.", 0.5, "r")(t)}</>)],
  ] },
  { id: "S05", shots: [
    [0, () => D3(shopIn("grin", "laugh"), (t) => <LocTag t={t} l1="ĐẦU THÁNG 3/2026" l2="Cửa hàng trang sức lớn" />)],
    [1, () => D3(shopIn("smile", "smile", "grin", { shake: 0.2 }), (t) => <BigText t={t} at={0.3} text="KHÁCH XẾP HÀNG CHỜ" col="#fff" y={90} size={96} />)],
    [2, () => D3(S("shop", "day", [[-0.2, 1.6, 2.2], [0.5, 1.4, 0.55], 34], [[0.0, 1.55, 1.9], [0.5, 1.4, 0.55], 30], [C("toanbop", [0.5, 0, 0.55], P("smug", { side: -1 }))]), (t) => <Bubble t={t} at={0.6} x={1040} y={160} w={700} kind="think" text="Bán đắt như tôm tươi thế này… sao không mua luôn cổ phiếu của nó?" tail="r" />)],
  ] },
  { id: "S06", shots: [
    [0, () => D3(closeT("grin", { acc: ["phone", "glow"] }), (t) => <ClockTag t={t} text="22:00 · 02/3" />)],
    [1, () => CD((t) => <PhoneCard t={t} time="22:05" date="02/3" notifs={[{ app: "Lệnh khớp", col: "#2ecc71", title: "MUA PNJ · 2.400 cổ phiếu", body: "Giá khớp 83,00 · ≈ 200 triệu đồng", at: 0.4 }]} hue="navy" />)],
    [2, () => D3(thumb("laugh"), (t) => <BigText t={t} at={0.3} text="GẦN ĐỈNH 84,6" col="#ff4d5e" y={90} size={110} />)],
    [3, () => D3(S(HOME, "room", ...roomTwo2, [toan("laugh", { acc: ["phone"] }), hang("smile")], RM), (t) => <Bubble t={t} at={0.3} x={120} y={120} w={640} kind="think" text="Đến ngày cưới, lãi đủ trả tiền tiệc!" />)],
  ] },
  { id: "S07", shots: [
    [0, () => D3(S("pho", "room", ...roomTwo2, [toan("smile"), hang("worried")], RM), (t) => <>{BL(1060, 110, "Anh bỏ nửa tiền cưới vào một mã thôi à?", 0.2, "r")(t)}</>)],
    [1, () => D3(S("pho", "room", [[1.0, 1.35, 2.4], [LX, 1.05, RZ], 34], [[0.9, 1.32, 2.0], [LX, 1.05, RZ], 30], [toan("smug", { wave: 1 }), hang("neutral")], RM), (t) => <>{BL(120, 110, "Công ty to, năm nào cũng lãi, chia cổ tức đều!", 0.3)(t)}</>)],
    [2, () => D3(S("pho", "room", ...roomTwo2, [toan("laugh"), hang("nervous")], RM), (t) => <>{BL(120, 110, "Có sập thì cả thị trường sập trước.", 0.2)(t)}</>)],
  ] },
  { id: "S08", shots: [
    [0, () => D3(S("streetday", "day", ...teaW, tea("laugh", "neutral", { acc: ["phone"] })), (t) => <LocTag t={t} l1="THÁNG 3 – 5/2026" l2="Quán trà đá đầu hẻm" />)],
    [1, () => CD((t) => <Big2 t={t} head="Doanh thu 6 tháng đầu 2026 của công ty" src="Nguồn: BCTC bán niên 2026, theo VnBusiness 28/9/2026" items={[{ a: "+49%", b: "so với cùng kỳ", at: 0.6, col: "#5dff9b" }]} />)],
    [2, () => D3(S("streetday", "day", ...teaT, tea("grin", "neutral", { acc: ["phone"], wave: 1 })), (t) => <>{BL(1060, 110, "Thấy chưa, cổ phiếu anh lãi rồi đấy!", 0.2, "r")(t)}</>)],
    [3, () => D3(S("streetday", "day", ...teaH, tea("laugh", "worried")), (t) => <BigText t={t} at={rel("S08", 4, sc("S08").sens[3].a)} text="NIỀM TIN" col="#ffd23f" y={90} size={150} />)],
  ] },
  { id: "S08B", shots: [
    [0, () => D3(S(HOME, "roomdim", ...roomTwo2, [toan("neutral", { acc: ["phone", "glow"] }), hang("shock", { acc: ["phone", "glow"] })], RM), (t) => <><LiveHud t={t} viewers={120430} /><BigText t={t} at={0.6} text="🔴 LIVESTREAM" col="#ff4d5e" y={90} size={100} /></>)],
    [1, () => CD((t) => <PhoneCard t={t} time="21:00" date="Cuối tháng 5" notifs={[{ app: "LIVESTREAM", col: "#e62117", title: "🔴 Nữ đại gia đang phát trực tiếp", body: "\"Kim cương không khớp mã kiểm định?\" · 120K người xem", at: 0.2 }]} quote={["Bình luận", "Ai mua kim cương thì đi kiểm lại ngay!"]} qAt={1.2} hue="red" />)],
    [2, () => D3(shopDay([hangShop("shock"), ...queue(20)], ...qWide), (t) => <LocTag t={t} l1="SÁNG HÔM SAU" l2="Tiệm vàng chỗ Hằng làm" />)],
    [3, () => D3(shopDay([hangShop("worried"), ...queue(20)], ...qPan, { ease: "lin" }), (t) => <BigText t={t} at={0.2} text="AI CŨNG ĐÒI BÁN LẠI" col="#ff4d5e" y={90} size={110} />)],
  ] },
  { id: "S08C", shots: [
    [0, () => D3(shopDay([hangShop("sad", { acc: ["paper"] }), ...queue(6, "stern")], [[GOLD_X + 3.4, 1.5, 2.4], [GOLD_X + 1.0, 1.3, 5.2], 40], [[GOLD_X + 3.0, 1.45, 2.9], [GOLD_X + 1.0, 1.3, 5.2], 36]), (t) => <BigText t={t} at={0.6} text="TẠM NGƯNG THU ĐỔI" col="#ff4d5e" y={90} size={110} />)],
    [1, () => CD((t) => <NewsCard t={t} tag="BÁO CHÍ ĐƯA TIN" items={[{ src: "Báo Đầu tư · 17/6/2026", head: "Ngành kim cương chao đảo vì làn sóng bán lại", at: 0.3 }, { src: "Người Quan Sát · 2026", head: "Có tiệm hơn 90% khách mang kim cương đến bán lại", at: 1.6, col: "#ff4d5e" }]} />)],
    [2, () => D3(S("cafe", "room", ...roomTwo2, [toan("laugh"), hang("worried")], RM), (t) => <>{BL(120, 110, "Tiệm nhỏ thôi em, công ty anh mua là công ty lớn, khác!", 0.6)(t)}</>)],
  ] },
  { id: "S08D", shots: [
    [0, () => CD((t) => <NewsCard t={t} tag="20/6/2026" items={[{ src: "Theo báo chí", head: "Triệt phá đường dây buôn lậu hơn 28.000 viên kim cương", at: 0.3 }, { src: "Theo báo chí", head: "Khởi tố 22 người", at: 1.8, col: "#ff4d5e" }]} />)],
    [1, () => D3(thumb("nervous"), (t) => <BigText t={t} at={0.2} text="CỔ PHIẾU BẮT ĐẦU ĐỎ" col="#ff4d5e" y={90} size={100} />)],
    [2, () => D3(closeT("smug", { acc: ["phone", "glow"] }), (t) => <Bubble t={t} at={0.2} x={1040} y={160} w={560} kind="think" text="Không liên quan…" tail="r" />)],
  ] },
  { id: "S09", shots: [
    [0, () => CD((t) => <NewsCard t={t} tag="ĐẦU THÁNG 7/2026" items={[{ src: "BBW · 6/7/2026", head: "Lãnh đạo đơn vị giám định kim cương của công ty bị bắt", at: 0.3, col: "#ff4d5e" }, { src: "Phản hồi của công ty", head: "Lô 28.000 viên không liên quan hệ thống bán hàng", at: at("S09", 0, 1) }]} />)],
    [2, () => D3(S("streetday", "day", ...teaW, tea("shock", "worried", { acc: ["phone"] }), { shake: 0.3 }), (t) => <BigText t={t} at={0.3} text="…NHƯNG AI ĐỌC KỸ?" col="#fff" y={90} size={110} />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(S("streetday", "day", ...hx2, [bt("shock", { acc: ["phone"] }), guest("bohung", "worried")]), (t) => <>{BL(1060, 110, "Con ơi, cái nhẫn của con Hằng có sao không?", 0.6, "r")(t)}<ClockTag t={t} text="07:10 · 05/7" /></>)],
    [1, () => D3(S("streetday", "day", ...hxT(HX - 0.55), [bt("worried", { acc: ["phone"], wave: 1 })]), (t) => <>{BL(1060, 110, "Cả xóm đang rủ nhau ra bán lại kìa!", 0.2, "r")(t)}</>)],
    [2, () => D3(S("streetday", "day", [[GOLD_X + 14, 1.5, 1.8], [GOLD_X + 9, 1.2, 5.3], 46], [[GOLD_X + 10, 1.5, 2.2], [GOLD_X + 6, 1.2, 5.3], 44], [C("toanbop", [GOLD_X + 14, 0.15, 4.6], walk("shock", { side: 1 }), [GOLD_X + 8, 0.15, 4.6]), ...queue(20)], { ease: "lin" }))],
    [3, () => D3(shopDay([...queue(20, "nervous")], [[qx(4), 1.35, 3.2], [qx(4), 1.3, 5.4], 40], [[qx(5), 1.35, 3.5], [qx(5), 1.3, 5.4], 36], { shake: 0.3 }), (t) => <BigText t={t} at={1.2} text="THẬT HAY GIẢ?" col="#ff4d5e" y={90} size={130} />)],
  ] },
  { id: "S11", shots: [
    [0, () => D3(thumb("shock", { anim: true, acc: ["phone", "glow", "sweat"] }), (t) => <BigText t={t} at={0.2} text="SÀN · SÀN" col="#4dd2ff" y={90} size={130} />)],
    [1, () => CD((t) => <PhoneCard t={t} time="14:45" date="06/7" notifs={[{ app: "Bảng giá", col: "#4dd2ff", title: "PNJ  54,60  ▼ SÀN", body: "Dư bán hơn 11,4 triệu cổ phiếu", at: 0.3 }, { app: "Tài khoản", col: "#ff4d5e", title: "Giá trị cổ phiếu", body: "200 triệu → ~131 triệu", at: at("S11", 1, 2) - at("S11", 1, 1) + 0.3 }]} hue="night" />)],
  ] },
  { id: "S12", shots: [
    [0, () => D3(S(HOME, "roomdim", ...roomTwo2, [toan("stern"), hang("worried")], RM), (t) => <>{BL(1060, 110, "Hay mình bán đi anh, giữ lại chừng nào hay chừng ấy.", 0.2, "r")(t)}</>)],
    [1, () => D3(S(HOME, "roomdim", [[1.0, 1.35, 2.4], [LX, 1.05, RZ], 34], [[0.9, 1.32, 2.0], [LX, 1.05, RZ], 30], [toan("stern", { wave: 1 }), hang("sad")], RM), (t) => <>{BL(120, 110, "Bán lúc này là bán đáy!", 0.2)(t)}</>)],
    [2, () => D3(S(HOME, "roomdim", ...roomTwo2, [toan("smug"), hang("sad")], RM), (t) => <>{BL(120, 110, "Công ty lớn thế, tin xấu nhất thời thôi.", 0.2)(t)}</>)],
    [3, () => D3(closeT("smug", { acc: ["phone", "glow"] }), (t) => <BigText t={t} at={0.4} text="VAY THÊM ĐỂ MUA BÌNH QUÂN?" col="#ff4d5e" y={90} size={92} />)],
    [4, () => D3(S(HOME, "roomdim", [[1.3, 1.35, 2.3], [0.8, 1.05, RZ], 36], [[1.2, 1.32, 2.0], [0.8, 1.05, RZ], 32], [toan("shock"), hang("stern", { wave: 1 })], RM), (t) => <>{BL(1060, 110, "Mẹ em dặn rồi: không có nợ.", 0.3, "r")(t)}</>)],
  ] },
  { id: "S13", shots: [
    [0, () => D3(shopDay([hangShop("worried", { acc: ["paper"] }), ...queue(12, "stern")], [[GOLD_X + 3.4, 1.5, 2.4], [GOLD_X + 1.0, 1.3, 5.2], 40], [[GOLD_X + 3.0, 1.45, 2.9], [GOLD_X + 1.0, 1.3, 5.2], 36]), (t) => <LocTag t={t} l1="CHÍNH SÁCH THU ĐỔI" l2="Để giữ khách" />)],
    [2, () => CD((t) => <Big2 t={t} head="Riêng tháng 7/2026, hàng khách mang trả lại" src="Nguồn: tài liệu ĐHCĐ bất thường 21/10/2026, theo VnBusiness" items={[{ a: "~6.000 TỶ", b: "đồng", at: 0.5, col: "#ff4d5e" }]} />)],
    [3, () => D3(shopDay([hangShop("sad"), ...queue(20, "neutral")], ...qPan, { ease: "lin" }), (t) => <BigText t={t} at={0.2} text="QUAY VỀ KHO + KHOẢN LỖ" col="#ff4d5e" y={90} size={96} />)],
  ] },
  { id: "S14", shots: [
    [0, () => D3(S("streetday", "day", ...teaW, tea("worried", "smile", {}, { wave: 1 })), (t) => <>{BL(120, 110, "Như ông bán bánh mì cả ngày, tối khách mang bánh quay lại đòi tiền.", 0.3)(t)}</>)],
    [1, () => CD((t) => <Big2 t={t} items={[{ a: "DOANH THU", b: "vẫn còn trên giấy", at: 0.2, col: "#5dff9b" }, { a: "TIỀN MẶT", b: "chảy ngược ra", at: 1.6, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S15", shots: [
    [0, () => D3(closeT("worried", { acc: ["phone", "glow"] }), (t) => <ClockTag t={t} text="Cuối tháng 9" />)],
    [1, () => CD((t) => <Rows t={t} title="Kế hoạch 2026 trình cổ đông (cuối tháng 9)" foot="Nguồn: VnBusiness 28/9/2026, Người Quan Sát 26/9/2026" stamp={{ text: "LỖ KỶ LỤC", at: at("S15", 1, 2) - at("S15", 1, 1) + 1.5 }} rows={[
      { l: "Giả định khách trả/đổi lại", v: "80% hàng đã bán", at: 0.3 }, { l: "Dự phòng dự kiến", v: "7.071 tỷ", at: 2.5, col: "#ff4d5e" },
      { l: "Lợi nhuận sau thuế cả năm", v: "lỗ ~6.270 tỷ", at: at("S15", 1, 2) - at("S15", 1, 1) + 0.5, big: true, col: "#ff4d5e" }, { l: "Cổ tức tiền mặt còn lại", v: "0 đồng", at: at("S15", 1, 3) - at("S15", 1, 1), col: "#ff4d5e" }]} />)],
  ] },
  { id: "S16", shots: [
    [0, () => D3(thumb("shock", { acc: ["phone", "glow", "sweat"] }), (t) => <BigText t={t} at={0.3} text="33 NGHÌN" col="#ff4d5e" y={90} size={130} />)],
    [1, () => CD((t) => <BankCard t={t} clock="Tài khoản chứng khoán · 25/9" amt="≈ 80 triệu" at={0.3} note="200 triệu ban đầu" />)],
    [2, () => D3(night([C("toanbop", [HOME_X + 3.6, 0.48, 5.6], P("sad", { mode: "sit" }))], [[[HOME_X + 4, 1.5, 2.4], [HOME_X + 3.6, 1.0, 5.6], 42], [[HOME_X + 3.8, 1.3, 3.2], [HOME_X + 3.6, 1.0, 5.6], 34]], { rain: true }))],
  ] },
  { id: "S16B", shots: [[0, () => CD((t) => <Img t={t} img="bd_2026" head="PNJ · nến tuần" />)]] },
  { id: "S17", shots: [
    [0, () => D3(night([bt("neutral"), guest("nv", "nervous")], hx2), (t) => <>{BL(1060, 110, "Thằng Toàn đâu, sao không qua?", 0.4, "r")(t)}</>)],
    [1, () => D3(night([bt("neutral"), guest("nv", "nervous")], hxT(HX + 0.55)), (t) => <>{BL(120, 110, "Anh ấy trực điện mẹ ạ.", 0.2)(t)}</>)],
    [2, () => D3(night([C("nv", [HX + 0.55, 0.48, 5.6], P("sad", { mode: "sit", acc: ["tears"] }))], [[[HX + 1.6, 1.4, 3.0], [HX + 0.55, 1.0, 5.6], 40], [[HX + 1.2, 1.3, 3.6], [HX + 0.55, 1.0, 5.6], 32]], { rain: true }), (t) => <BigText t={t} at={1} text="💍" col="#fff" y={120} size={120} />)],
  ] },
  { id: "S18", shots: [
    [0, () => D3(closeT("worried", { acc: ["phone", "glow"] }, "room"), (t) => <LocTag t={t} l1="21/10/2026 · ĐHĐCĐ BẤT THƯỜNG" l2="Theo tài liệu công bố" />)],
    [1, () => CD((t) => <Rows t={t} title="Những con số tại đại hội" foot="Nguồn: VnBusiness 21/10/2026" rows={[
      { l: "Quý III/2026 (chưa tính dự phòng)", v: "lỗ 258 tỷ", at: 0.3, col: "#ff4d5e" }, { l: "Tiền và tiền gửi cuối tháng 6", v: "~3.700 tỷ", at: at("S18", 1, 2) - at("S18", 1, 1) + 0.3 },
      { l: "Tiền và tiền gửi cuối tháng 9", v: "770 tỷ", at: at("S18", 1, 2) - at("S18", 1, 1) + 2.6, col: "#ff4d5e" }, { l: "Cần huy động", v: "~8.000 tỷ", at: at("S18", 1, 3) - at("S18", 1, 1) + 0.4, big: true },
      { l: "Phát hành riêng lẻ tối đa", v: "550 triệu cp", at: at("S18", 1, 3) - at("S18", 1, 1) + 3, col: "#ffd23f" }]} />)],
  ] },
  { id: "S19", shots: [
    [0, () => D3(S("streetday", "day", ...teaW, tea("worried", "neutral")), (t) => <><LocTag t={t} l1="QUÁN TRÀ ĐÁ ĐẦU HẺM" l2="Huy – bạn cùng hẻm, làm ngành chứng khoán" />{BL(1060, 300, "Phát hành thêm thì sao hả Huy?", 0.8, "r")(t)}</>)],
    [1, () => D3(S("streetday", "day", ...teaH, tea("neutral", "smile", {}, { wave: 1 })), (t) => <>{BL(120, 110, "Cái bánh chia 8 miếng, ông giữ 1 miếng…", 0.3)(t)}</>)],
    [2, () => CD((t) => <Big2 t={t} head="🍕 Pha loãng" items={[{ a: "1/8", b: "miếng của ông lúc đầu", at: 0.3, col: "#5dff9b" }, { a: "1/16", b: "sau khi cắt thêm để bán", at: at("S19", 2, 3) - at("S19", 2, 2), col: "#ff4d5e" }]} />)],
    [4, () => D3(S("streetday", "day", ...teaT, tea("shock", "neutral")), (t) => <BigText t={t} at={0.2} text="PHA LOÃNG" col="#ffd23f" y={90} size={130} />)],
  ] },
  { id: "S20", shots: [
    [0, () => D3(S(HOME, "roomdim", [[2.2, 2.2, 3.4], [LX, 1.0, RZ], 50], [[0.6, 1.3, 2.0], [LX, 1.05, RZ], 32], [toan("nervous", { acc: ["phone", "glow"] })], { ...RM, rain: true, ease: "out" }), (t) => <ClockTag t={t} text="23:40 · 20/10" />)],
    [1, () => CD((t) => <PhoneCard t={t} time="23:41" date="20/10" notifs={[{ app: "Bảng giá", col: "#b03ad0", title: "PNJ  19,75  ▲ TRẦN", body: "Dư mua 4 triệu cp · Khối ngoại mua ròng ~3,5 triệu cp", at: 0.3 }]} hue="night" />)],
    [3, () => D3(S("canhovip", "room", [[-0.6, 1.5, 2.4], [-0.3, 1.1, 0.6], 40], [[-0.5, 1.45, 2.0], [-0.3, 1.1, 0.6], 34], [C("phu", [-0.3, 0, 0.6], P("laugh", { side: 1, acc: ["phone", "glow"], wave: 1 }))], RM), (t) => <>{BL(1060, 110, "Đáy rồi! Có tay to gom, vào hết đi!", 0.2, "r")(t)}<LocTag t={t} l1="PHÚ DÊ GIÀ" /></>)],
    [4, () => CD((t) => <BankCard t={t} clock="Tài khoản chứng khoán" amt="≈ 48 triệu" at={0.4} note="200 triệu ban đầu" />)],
    [5, () => D3(thumb("nervous", { anim: true, acc: ["phone", "glow", "sweat"] }), (t) => <BigText t={t} at={rel("S20", 6, sc("S20").sens[5].a)} text="TIỀN ĐẶT TIỆC CƯỚI" col="#ff4d5e" y={90} size={100} />)],
  ] },
  { id: "S20B", shots: [
    [0, () => D3(S(HOME, "roomdim", [[0.65, 1.32, 2.25], [LX, 1.05, RZ], 32], [[2.0, 2.0, 3.2], [LX, 1.0, RZ], 46], [toan("nervous", { acc: ["phone", "glow"] })], { ...RM, ease: "out" }), (t) => <BigText t={t} at={0.1} text="NẾU BẤM?" col="#ffd23f" y={90} size={130} />)],
    [1, () => CD((t) => <Img t={t} img="bd_tran" head="Sau phiên kịch trần" />)],
    [5, () => CD((t) => <Big2 t={t} head="Nếu mua ở giá trần 20/10" items={[{ a: "−27%", b: "đến 16/11/2026", at: 0.3, col: "#ff4d5e" }, { a: "~146 TR", b: "còn lại của 200 triệu", at: at("S20B", 5, 6) - at("S20B", 5, 5), col: "#ff4d5e" }]} />)],
  ] },
  { id: "S21", shots: [
    [0, () => D3(thumb("shock"), (t) => <ClockTag t={t} text="23:42" />)],
    [1, () => D3(night([C("nv", [HX + 0.55, 0.48, 5.6], P("smile", { mode: "sit", acc: ["phone", "glow"] }))], [[[HX + 1.6, 1.4, 3.0], [HX + 0.55, 1.0, 5.6], 40], [[HX + 1.2, 1.3, 3.6], [HX + 0.55, 1.0, 5.6], 32]]), (t) => <LocTag t={t} l1="HẰNG" l2="vừa đi kiểm định lại chiếc nhẫn" />)],
    [2, () => CD((t) => <ChatCard t={t} title="Hằng ❤" msgs={[{ who: "Hằng", text: "📄 [Ảnh] Giấy kiểm định nhẫn", at: 0.2 }, { who: "Hằng", text: "Anh ơi, nhẫn em mang đi kiểm lại rồi. Kim cương thật.", at: 1.2 }]} />)],
    [3, () => CD((t) => <Big2 t={t} head="Mẫu lấy ngẫu nhiên, gửi kiểm định độc lập" src="Theo VnBusiness 28/9/2026" items={[{ a: "100%", b: "là kim cương thiên nhiên", at: 0.4, col: "#5dff9b" }]} />)],
    [4, () => D3(S(HOME, "roomdim", [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.55, 1.26, 1.5], [LX, 1.05, RZ], 24], [toan("sad", { acc: ["phone", "glow"] })], RM))],
  ] },
  { id: "S22", shots: [
    [0, () => D3(S("streetday", "day", ...hx2, [bt("neutral"), guest("toanbop", "sad")]), (t) => <LocTag t={t} l1="NHÀ BÀ TƯ · HÔM SAU" />)],
    [1, () => D3(S("streetday", "day", ...hxT(HX - 0.55), [bt("neutral"), guest("toanbop", "sad")]), (t) => <>{BL(1060, 110, "Thế viên đá có lỗi gì không con?", 0.6, "r")(t)}</>)],
    [2, () => D3(S("streetday", "day", ...hxT(HX + 0.55), [bt("neutral"), guest("toanbop", "sad")]), (t) => <BigText t={t} at={0.1} text="…" col="#fff" y={90} size={130} />)],
    [3, () => D3(S("streetday", "day", ...hxT(HX - 0.55), [bt("stern", { wave: 1 }), guest("toanbop", "sad")]), (t) => <>{BL(1060, 110, "Cái sai không nằm ở viên đá.", 0.2, "r")(t)}</>)],
    [4, () => D3(S("streetday", "day", ...hx2, [bt("stern"), guest("toanbop", "cry")]), (t) => <BigText t={t} at={0.8} text="SỐNG BẰNG LÒNG TIN CỦA NGƯỜI KHÁC" col="#ffd23f" y={90} size={80} />)],
  ] },
  { id: "S23", shots: [[0, () => D3(S("streetday", "day", ...teaH, [C("huy", TH, P("smile", { side: 1, acc: ["cup"] }))]), (t) => <LocTag t={t} l1="HUY NGUYỄN" l2="4 điều rút ra" />)], [1, () => D3(S("streetday", "day", ...teaW, tea("neutral", "smile", {}, { wave: 1 })))]] },
  { id: "S24", shots: [[0, () => CD((t) => <LessonCard t={t} title="1. Tiền có hạn dùng" items={[{ n: "1", icon: "💍", head: "Tiền cưới, tiền học, tiền nhà trong 1–2 năm", body: "Không đặt vào cổ phiếu", at: 0.3 }, { n: "!", icon: "📉", head: "Cổ phiếu có thể giảm 60–70% trong vài tháng", body: "Kể cả công ty lớn", at: at("S24", 0, 2) }, { n: "✓", icon: "🏦", head: "Để ở chỗ chắc chắn còn nguyên", body: "đến đúng ngày cần", at: at("S24", 0, 3) }]} />)]] },
  { id: "S25", shots: [[0, () => CD((t) => <LessonCard t={t} title="2. Không dồn một mã" items={[{ n: "2", icon: "🧺", head: "Chia nhiều mã, nhiều ngành", body: "mỗi mã một phần nhỏ", at: at("S25", 0, 2) }, { n: "✓", icon: "🛡", head: "Một mã gặp sự cố", body: "cả danh mục vẫn đứng được", at: at("S25", 0, 3) }]} />)]] },
  { id: "S26", shots: [[0, () => CD((t) => <LessonCard t={t} title="3. Doanh nghiệp tốt ≠ cổ phiếu an toàn" items={[{ n: "3", icon: "💎", head: "Ngành bán lòng tin", body: "vàng, kim cương, ngân hàng, bảo hiểm", at: at("S26", 0, 2) }, { n: "?", icon: "💧", head: "Nếu niềm tin mất", body: "dòng tiền sẽ ra sao?", at: at("S26", 0, 3) }]} />)], [2, () => D3(shopDay([hangShop("worried"), ...queue(20)], ...qWide), (t) => <BigText t={t} at={0.2} text="NIỀM TIN MẤT NHANH HƠN BÁO CÁO" col="#ff4d5e" y={90} size={84} />)]] },
  { id: "S27", shots: [
    [0, () => D3(S("streetday", "day", ...teaH, [C("huy", TH, P("neutral", { side: 1, acc: ["cup"], wave: 1 }))]), (t) => <BigText t={t} at={0.1} text="4. TRƯỚC KHI BẮT ĐÁY" col="#ffd23f" y={90} size={100} />)],
    [2, () => CD((t) => <LessonCard t={t} title="Mình đang chờ điều gì?" items={[{ n: "1", icon: "💵", head: "Phát hành ~8.000 tỷ", body: "chốt giá bao nhiêu, ai mua?", at: at("S27", 2, 3) - at("S27", 2, 2) }, { n: "2", icon: "↩", head: "Tỷ lệ khách trả hàng thực tế", body: "thấp hơn giả định 80%? → hoàn nhập dự phòng", at: at("S27", 2, 4) - at("S27", 2, 2) }, { n: "3", icon: "📊", head: "Biên lợi nhuận gộp", body: "từ 18,5% xuống ~10% – có quay lại?", at: at("S27", 2, 5) - at("S27", 2, 2) }]} />)],
    [6, () => CD((t) => <Img t={t} img="bd_tran" head="1 phiên trần ≠ câu trả lời" />)],
  ] },
  { id: "S28", shots: [
    [0, () => D3(thumb("neutral"), (t) => <BigText t={t} at={rel("S28", 1, sc("S28").a)} text="KHÔNG BẤM" col="#5dff9b" y={90} size={130} />)],
    [2, () => D3(PH("dam_cuoi_que", [0.5, 0.6], [C("toanbop", [-0.15, 0, 0.7], P("laugh", { side: -1, mode: "stand" })), C("nv", [0.95, 0, 0.7], P("laugh", { side: 1, mode: "stand" })), C("mehung", [2.0, 0, 1.0], P("smile", { side: -1, mode: "stand" }))], pcam(0.6)), (t) => <LocTag t={t} l1="ĐÁM CƯỚI NHỎ Ở QUÊ" />)],
    [3, () => D3(PH("dam_cuoi_que", [0.5, 0.6], [C("toanbop", [-0.15, 0, 0.7], P("smile", { side: -1, mode: "stand" })), C("nv", [0.95, 0, 0.7], P("laugh", { side: 1, mode: "stand", wave: 1 }))], pclose(0.4)), (t) => <BigText t={t} at={rel("S28", 4, sc("S28").sens[3].a)} text="BÀI HỌC ĐẮT HƠN CHIẾC NHẪN" col="#ffd23f" y={90} size={92} />)],
  ] },
  { id: "S29", shots: [[0, () => CD((t) => <Ask t={t} />)]] },
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
export const PNJ1_FRAMES = TOTAL_F;
export const Pnj1Video: React.FC = () => {
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
        {audio ? <Audio src={staticFile("pnj1/voice.wav")} /> : null}
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
