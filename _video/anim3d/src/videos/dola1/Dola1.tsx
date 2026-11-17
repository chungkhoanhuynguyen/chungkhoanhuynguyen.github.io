// Phim 3D DOLA1 "Thật tệ khi một cuộc họp ở Mỹ quyết định lô hàng của chị buôn Móng Cái". Khung 1920x1080, 30 fps.
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
    <img src={staticFile(`dola1/${img}.jpg`)} style={{ width: 1600, height: 900, marginTop: -110, objectFit: "contain", opacity: a, transform: `scale(${0.97 + 0.03 * a + t * 0.002})` }} />
    {head && <div style={{ position: "absolute", top: 40, right: 80, padding: "10px 26px", borderRadius: 12, background: "#ffd23f", color: "#1a0f33", fontSize: 40, fontWeight: 900, opacity: sm((t - 0.6) / 0.3) }}>{head}</div>}
    {foot && <div style={{ position: "absolute", bottom: 175, width: "100%", textAlign: "center", fontSize: 26, color: "rgba(255,255,255,.6)" }}>{foot}</div>}</AbsoluteFill>; };
const Ask: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.5), clickT = t - 3.6, sub = clickT > 0.35;
  return <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><Bg t={t} hue="navy" />
    <div style={{ opacity: a, position: "relative" }}><div style={{ fontSize: 40, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>CÂU HỎI CHO ANH CHỊ</div>
      <div style={{ fontSize: 88, fontWeight: 900, color: "#fff", marginTop: 20, lineHeight: 1.15 }}>MÙA MỸ TĂNG LÃI SUẤT<br />ANH CHỊ Ở ĐẦU NÀO SỢI DÂY?</div>
      <div style={{ display: "inline-block", marginTop: 50, padding: "22px 64px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 48, fontWeight: 900 }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI KÊNH"}</div></div>
    {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 1060 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 820 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
    <div style={{ position: "absolute", left: 40, bottom: 22, fontSize: 28, fontWeight: 700, color: "rgba(255,255,255,.55)" }}>chungkhoanhuynguyen.com</div>
    <div style={{ position: "absolute", right: 40, bottom: 20, fontSize: 22, color: "rgba(255,255,255,.5)" }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư · Ảnh: Wikimedia Commons (CC BY / CC BY-SA)</div></AbsoluteFill>; };
const Photo: React.FC<{ t: number; img: string; d?: number; dir?: number }> = ({ t, img, d = 7, dir = 1 }) => { const k = Math.min(1, t / Math.max(d, 1)); const z = 1.06 + 0.08 * k;
  return <AbsoluteFill style={{ background: "#000" }}><img src={staticFile(`dola1/${img}.jpg`)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z}) translateX(${dir * (k - 0.5) * 30}px)`, filter: "brightness(.82) saturate(1.05)" }} />
    <AbsoluteFill style={{ background: "linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 28%,rgba(0,0,0,0) 62%,rgba(0,0,0,.55) 100%)" }} /></AbsoluteFill>; };
const PR = (img: string, ov?: (t: number) => React.ReactNode, dir = 1) => (t: number) => <><Photo t={t} img={img} dir={dir} />{ov?.(t)}</>;
// ---------- dàn cảnh ----------
// Phòng trọ (room): máy nhìn −z → +x bên PHẢI màn. Toàn trái màn (side +1), Hằng phải màn (side −1).
const roomTwo2 = roomTwo;
const LX = 0.35, NX = 1.3, RZ = 0.6;
const toan = (e: Expr, o: PO = {}) => C("quang", [LX, 0, RZ], P(e, { side: 1, mode: "stand", ...o }));
const hang = (e: Expr, o: PO = {}) => C("trang", [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }));
const RM = { chat: "off" as const, game: false };
const PH = (bg: string, fit: [number, number], cast: Cast[], cam: [[V, V, number], [V, V, number]], x: Partial<Shot3D> = {}) => S("photo", "room", cam[0], cam[1], cast, { bg: `dola1/${bg}.jpg`, bgFit: fit, ...x });
const pcam = (x = 0): [[V, V, number], [V, V, number]] => [[[x, 1.45, -3.2], [x, 1.25, 3], 42], [[x, 1.42, -2.8], [x, 1.25, 3], 40]];
const pclose = (x = 0.4): [[V, V, number], [V, V, number]] => [[[x, 1.4, -2.2], [x, 1.2, 3], 38], [[x, 1.38, -1.9], [x, 1.2, 3], 36]];
const duo = (a: string, ea: Expr, b: string, eb: Expr, oa: PO = {}, ob: PO = {}): Cast[] => [C(a, [-0.15, 0, 0.7], P(ea, { side: -1, mode: "stand", ...oa })), C(b, [0.95, 0, 0.7], P(eb, { side: 1, mode: "stand", ...ob }))];
const BL = (x: number, y: number, text: string, at0: number, tail: "l" | "r" = "l") => (t: number) => <Bubble t={t} at={at0} text={text} x={x} y={y} tail={tail} w={640} />;
const closeT = (e: Expr, o: PO = {}, light: Shot3D["light"] = "roomdim") => S("room", light, [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [toan(e, o)], RM);
const thumb = (e: Expr, o: PO = {}) => S("room", "roomdim", [[0.75, 1.35, 2.7], [LX, 1.05, RZ], 36], [[0.65, 1.32, 2.25], [LX, 1.05, RZ], 32], [toan(e, { acc: ["phone", "glow"], ...o })], { ...RM, shake: 0.2 });
// tiệm vàng chỗ Hằng (phố ban ngày) + hàng người bán lại nhẫn
const qx = (i: number) => GOLD_X + 1.4 + i * 1.15;
const queue = (n = 20, e: Expr = "worried"): Cast[] => Array.from({ length: n }, (_, i) => C("c" + i, [qx(i), 0.15, 5.25 + (i % 2) * 0.25], P(i % 3 === 1 ? "shock" : e, { mode: "stand", acc: i % 2 ? ["box"] : ["phone"], phase: i * 0.37, side: -1 })));
const shopDay = (cast: Cast[], from: [V, V, number], to: [V, V, number], x: Partial<Shot3D> = {}) => S("streetday", "day", from, to, cast, x);
const qWide: [[V, V, number], [V, V, number]] = [[[qx(14), 9, -4], [qx(8), 1.4, 5.3], 50], [[qx(7), 3.5, 0], [qx(6), 1.3, 5.3], 46]];
const qPan: [[V, V, number], [V, V, number]] = [[[GOLD_X - 1, 1.6, 1.8], [GOLD_X + 3, 1.3, 5.4], 46], [[qx(16), 1.6, 1.8], [qx(20), 1.3, 5.4], 46]];
const HQ: V = [GOLD_X + 0.3, 0.15, 5.1];
// trong cửa hàng trang sức lớn
const shopIn = (te: Expr, he: Expr, ce: Expr = "smile", x: Partial<Shot3D> = {}) => S("shop", "day", [[-2.2, 1.7, 3.6], [0, 1.2, -1], 46], [[-1.4, 1.55, 2.6], [0, 1.2, -1], 42], [C("toanbop", [0.5, 0, 0.55], P(te)), C("nv", [1.3, 0, 0.6], P(he, { side: -1 })), C("clerk", [0, 0, -1.4], P(ce)), ...runners(4, -3, -3.2, 1.8)], x);

// quán trà đá đầu hẻm (phố ban ngày, cạnh tiệm vàng): +x bên TRÁI màn
const TT: V = [GOLD_X + 6.3, 0.15, 5.45], TH: V = [GOLD_X + 7.45, 0.15, 5.3];
const tea = (te: Expr, he: Expr, ot: PO = {}, oh: PO = {}): Cast[] => [C("trang", TT, P(te, { side: 1, ...ot })), C("huy", TH, P(he, { side: -1, acc: ["cup"], ...oh })), ...queue(3, "neutral").map((c, i) => ({ ...c, p: [GOLD_X - 2 - i * 1.2, 0.15, 5.4] as V }))];
const teaW: [[V, V, number], [V, V, number]] = [[[GOLD_X + 9.4, 1.5, 2.6], [GOLD_X + 6.9, 1.15, 5.5], 44], [[GOLD_X + 8.8, 1.45, 3.1], [GOLD_X + 6.9, 1.15, 5.5], 40]];
const teaT: [[V, V, number], [V, V, number]] = [[[GOLD_X + 5.6, 1.4, 3.4], [GOLD_X + 6.3, 1.3, 5.45], 36], [[GOLD_X + 5.8, 1.4, 3.8], [GOLD_X + 6.3, 1.32, 5.45], 32]];
const teaH: [[V, V, number], [V, V, number]] = [[[GOLD_X + 8.2, 1.4, 3.4], [GOLD_X + 7.45, 1.3, 5.3], 36], [[GOLD_X + 8.0, 1.4, 3.8], [GOLD_X + 7.45, 1.32, 5.3], 32]];
// trước cửa nhà bà Tư (phố, HX): bà Tư phải màn, khách trái màn
const bt = (e: Expr, o: PO = {}) => C("mehung", [HX - 0.55, 0.15, 5.3], P(e, { side: -1, ...o }));
const guest = (a: string, e: Expr, o: PO = {}) => C(a, [HX + 0.55, 0.15, 5.3], P(e, { side: 1, ...o }));
const hx2 = two(HX), hxT = (x: number): [[V, V, number], [V, V, number]] => [[[x - 0.3, 1.45, 3.4], [x, 1.3, 5.3], 34], [[x - 0.2, 1.42, 3.8], [x, 1.32, 5.3], 30]];
// Hằng trong tiệm (cạnh quầy)
const hangShop = (e: Expr, o: PO = {}) => C("trang", HQ, P(e, { side: 1, ...o }));
const hqT: [[V, V, number], [V, V, number]] = [[[GOLD_X + 0.9, 1.45, 3.4], [GOLD_X + 0.3, 1.3, 5.1], 34], [[GOLD_X + 0.7, 1.42, 3.8], [GOLD_X + 0.3, 1.32, 5.1], 30]];
const night = (cast: Cast[], cam: [[V, V, number], [V, V, number]], x: Partial<Shot3D> = {}) => S("street", "night", cam[0], cam[1], cast, x);

const D_ = (e: Expr, o: PO = {}) => C("quang", [LX, 0, RZ], P(e, { side: 1, mode: "stand", ...o }));
const T_ = (e: Expr, o: PO = {}) => C("trang", [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }));
const doi = (cast: Cast[], from: [V, V, number], to: [V, V, number], x: Partial<Shot3D> = {}) => S("street", "night", from, to, cast, x);
const trangRun = (e: Expr = "nervous") => C("trang", [GOLD_X + 8, 0.15, 4.6], walk(e, { side: -1, acc: ["box"] }), [GOLD_X + 1.5, 0.15, 4.6]);
const walkers = (n: number, z = 1.6): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (40 + i), [i % 2 ? 2.6 : -2.2, 0, z + i * 0.35], (t: number) => ({ ...P(i % 3 ? "neutral" : "smile", { acc: i % 2 ? ["box"] : ["phone"] })(t), mode: "stroll", phase: (t * 1.4 + i * 0.3) % 1, side: i % 2 ? -1 : 1 }), [i % 2 ? -2.4 : 2.8, 0, z + i * 0.35]));
const MC = (bg: string, cast: Cast[], cam: [[V, V, number], [V, V, number]] = pcam(0.4)) => PH(bg, [0.5, 0.6], [...cast, ...walkers(3)], cam);
const trangAt = (e: Expr, o: PO = {}, x = 0.4) => C("trang", [x, 0, 0.7], P(e, { side: 1, mode: "stand", ...o }));
const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => D3(doi([trangRun(), ...queue(4, "neutral")], [[GOLD_X + 10, 2.2, 1.4], [GOLD_X + 5, 1.2, 5], 46], [[GOLD_X + 6, 1.6, 2.2], [GOLD_X + 2, 1.2, 5], 42], { rain: true, ease: "lin" }), (t) => <BigText t={t} at={0.4} text="THẬT TỆ KHI…" col="#ffd23f" y={90} size={120} />)],
    [1, () => D3(doi([C("trang", [GOLD_X + 1.4, 0.15, 4.8], P("nervous", { side: 1, acc: ["box", "sweat"] })), hangShop("neutral")].slice(0, 1).concat([C("clerk", HQ, P("neutral", { side: 1 }))]), [[GOLD_X + 3.2, 1.5, 2.4], [GOLD_X + 1.0, 1.3, 5.0], 40], [[GOLD_X + 2.8, 1.45, 2.9], [GOLD_X + 1.0, 1.3, 5.0], 36], { rain: true }), (t) => <><ClockTag t={t} text="22:00 · 10/2022" /><LocTag t={t} l1="MÓNG CÁI · QUẢNG NINH" l2="Tiệm đổi tiền thứ ba trong đêm" /></>)],
    [3, () => D3(doi([C("trang", [GOLD_X + 1.4, 0.15, 4.8], P("shock", { side: 1, acc: ["box"] })), C("clerk", HQ, P("stern", { side: 1, wave: 1 }))], [[GOLD_X + 1.9, 1.45, 3.4], [GOLD_X + 0.6, 1.3, 5.0], 34], [[GOLD_X + 1.8, 1.42, 3.8], [GOLD_X + 0.6, 1.32, 5.0], 30], { rain: true }), (t) => <>{BL(1060, 110, "Hết đô rồi chị ơi! Mai quay lại, giá lại khác.", 0.2, "r")(t)}</>)],
  ] },
  { id: "S02", shots: [
    [0, () => D3(S("room", "roomdim", [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [D_("shock", { acc: ["phone", "glow", "sweat"] })], RM), (t) => <LocTag t={t} l1="CÙNG LÚC · HÀ NỘI" l2="Đức Đô La" />)],
    [1, () => CD((t) => <PhoneCard t={t} time="22:05" date="10/2022" notifs={[{ app: "Công ty chứng khoán", col: "#ff4d5e", title: "YÊU CẦU NỘP THÊM TIỀN KÝ QUỸ", body: "Hạn chót 9:00 sáng mai", at: 0.3 }]} hue="red" />)],
    [2, () => CD((t) => <Big2 t={t} items={[{ a: "$", b: "đồng đô la", at: 0.2, col: "#5dff9b" }]} head="Hai vợ chồng, hai thành phố, cùng mất ngủ vì…" />)],
  ] },
  { id: "S03", shots: [
    [0, () => CD(PR("mc_toancanh", (t) => <LocTag t={t} l1="MÓNG CÁI · QUẢNG NINH" l2="Thành phố cửa khẩu, nơi địa đầu Tổ quốc" />))],
    [1, () => D3(MC("mc_cho", [trangAt("grin", { acc: ["box"] })]), (t) => <><BigText t={t} at={0.3} text="TRANG TRÂU" col="#ffd23f" y={240} size={120} /><LocTag t={t} l1="CHỢ TRUNG TÂM MÓNG CÁI" l2="34 tuổi · 1m47 · 10 năm buôn hàng biên giới" /></>)],
    [2, () => D3(MC("mc_bacluan", [C("trang", [-1.2, 0, 0.9], walk("laugh", { side: 1, acc: ["box"] }), [1.6, 0, 0.9])], pcam(0.3)), (t) => <><LocTag t={t} l1="CẦU BẮC LUÂN II" l2="Ngày nào cũng chở hàng qua biên giới" />{BL(1060, 300, "Trang ơi, một mình bốc cả xe à?", 0.6, "r")(t)}</>)],
    [3, () => D3(MC("mc_cuakhau", [trangAt("neutral", { acc: ["paper"] })]), (t) => <><LocTag t={t} l1="CỬA KHẨU MÓNG CÁI" />{BL(1060, 110, "Lô này thanh toán 40.000 đô la.", 0.4, "r")(t)}</>)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(PH("hn_vanphong", [0.5, 0.6], [C("quang", [0.4, 0, 0.7], P("smug", { side: 1, mode: "stand", acc: ["phone"] }))], pcam(0.4)), (t) => <><BigText t={t} at={0.3} text="ĐỨC ĐÔ LA" col="#ffd23f" y={170} size={120} /><LocTag t={t} l1="Nhân viên văn phòng · Hà Nội" /></>)],
    [1, () => D3(S("room", "room", ...roomTwo2, [D_("smug", { wave: 1 }), T_("neutral")], RM), (t) => <>{BL(120, 110, "Tiền Việt thì mất giá, giàu là phải có đô!", 0.2)(t)}</>)],
    [2, () => D3(closeT("grin", { acc: ["phone", "glow"] }, "room"), (t) => <BigText t={t} at={0.5} text="…NHƯNG TIỀN NẰM HẾT TRONG CHỨNG KHOÁN" col="#ff4d5e" y={90} size={76} />)],
  ] },
  { id: "S05", shots: [
    [0, () => CD((t) => <Big2 t={t} head="Đầu năm 2022" src="VN-Index đầu năm 2022 lập đỉnh 1.528,6 điểm – Người Quan Sát" items={[{ a: "~1.500", b: "điểm chứng khoán", at: 0.4, col: "#5dff9b" }]} />)],
    [1, () => D3(S("room", "room", ...roomTwo2, [D_("laugh", { acc: ["phone"] }), T_("laugh")], RM), (t) => <>{BL(120, 110, "Năm nay anh mua nhà cho mẹ!", 0.2)(t)}</>)],
    [2, () => D3(MC("mc_pho", [trangAt("laugh", { acc: ["box"] }), C("c50", [1.3, 0, 0.8], P("smile", { side: -1, mode: "stand", acc: ["phone"] }))]), (t) => <LocTag t={t} l1="PHỐ MÓNG CÁI" l2="Hàng kín cả tháng" />)],
  ] },
  { id: "S06", shots: [
    [0, () => CD(PR("eccles", (t) => <LocTag t={t} l1="WASHINGTON · THÁNG 3/2022" l2="Cục Dự trữ Liên bang Mỹ (Fed)" />))],
    [1, () => CD((t) => <Big2 t={t} head="Lãi suất Fed năm 2022" src="Theo các quyết định của Fed, 3/2022 – 12/2022" items={[{ a: "~0%", b: "tháng 3/2022", at: 0.4, col: "#5dff9b" }, { a: "4,25–4,5%", b: "tháng 12/2022", at: 1.8, col: "#ff4d5e" }]} />)],
    [3, () => D3(closeT("neutral", { acc: ["phone", "glow"] }, "room"), (t) => <BigText t={t} at={0.3} text="NHANH NHẤT 40 NĂM" col="#ff4d5e" y={90} size={110} />)],
  ] },
  { id: "S07", shots: [
    [0, () => D3(S("streetday", "day", ...teaW, tea("worried", "neutral")), (t) => <><LocTag t={t} l1="HUY · em họ, làm ngành chứng khoán" />{BL(1060, 300, "Mỹ tăng lãi suất thì liên quan gì hàng của em?", 0.4, "r")(t)}</>)],
    [2, () => D3(S("streetday", "day", ...teaH, tea("neutral", "smile", {}, { wave: 1 })), (t) => <>{BL(120, 110, "Tiền như nước: chảy về chỗ lãi cao.", 0.3)(t)}</>)],
    [4, () => CD((t) => <Big2 t={t} items={[{ a: "💧→🇺🇸", b: "tiền khắp thế giới rút về Mỹ", at: 0.3, col: "#4dd2ff" }, { a: "$ ↑", b: "ai cũng cần đô la", at: 1.6, col: "#ffd23f" }]} />)],
  ] },
  { id: "S08", shots: [
    [0, () => CD((t) => <Bars t={t} title="Tỷ trọng trong dự trữ ngoại hối thế giới (cuối 2025)" max={60} src="Nguồn: IMF COFER, qua VnEconomy 12/6/2026" rows={[{ l: "Đô la Mỹ", v: 56.8, lab: "56,8%", col: "#5dff9b", at: 0.6 }, { l: "Euro", v: 20.2, lab: "20,2%", col: "#7aa7ff", at: 1.2 }, { l: "Yên Nhật", v: 5.8, lab: "5,8%", col: "#a88bff", at: 1.6 }, { l: "Nhân dân tệ", v: 2, lab: "~2%", col: "#ff9d4d", at: 2.0 }]} />)],
    [2, () => CD(PR("container", (t) => <BigText t={t} at={0.4} text="ĐỒNG TIỀN CỦA NGÂN HÀNG THẾ GIỚI" col="#ffd23f" y={90} size={86} />))],
  ] },
  { id: "S09", shots: [
    [0, () => CD((t) => <Rows t={t} title="Đến giữa tháng 10/2022" foot="Nguồn: VnBusiness 13/10/2022 (ước tính VinaCapital, ACBS)" rows={[{ l: "Giá USD tại ngân hàng so với cuối 2021", v: "+4,7%", at: 0.4, col: "#ff4d5e" }, { l: "NHNN bán ra (ước tính)", v: "~21 tỷ USD", at: at("S09", 0, 1) + 0.4, big: true }, { l: "Dự trữ ngoại hối còn", v: "~89–90 tỷ USD", at: at("S09", 0, 1) + 2.4 }]} />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(MC("mc_cho", [trangAt("worried", { acc: ["paper"] })]), (t) => <BigText t={t} at={0.4} text="4–5% = TIỀN LỜI CẢ LÔ" col="#ff4d5e" y={90} size={100} />)],
    [1, () => D3(shopDay([hangShop("sad"), C("c1", [GOLD_X + 1.6, 0.15, 4.6], P("stern", { side: -1, wave: 1 }))], ...hqT), (t) => <>{BL(120, 110, "Tăng giá à? Thôi chị để tôi lấy chỗ khác.", 0.2)(t)}</>)],
    [2, () => D3(S("room", "roomdim", [[1.3, 1.35, 2.3], [NX, 1.05, RZ], 34], [[1.3, 1.32, 2.0], [NX, 1.05, RZ], 30], [T_("sad", { acc: ["paper"] })], RM), (t) => <BigText t={t} at={0.3} text="BÁN HẾT HÀNG VẪN LỖ" col="#ff4d5e" y={90} size={110} />)],
  ] },
  { id: "S11", shots: [
    [0, () => D3(closeT("worried", { acc: ["phone", "glow"] }), (t) => <BigText t={t} at={0.3} text="KHỐI NGOẠI BÁN RA" col="#ff4d5e" y={90} size={110} />)],
    [1, () => CD((t) => <Big2 t={t} head="Chỉ số chứng khoán Việt Nam 2022" src="Đỉnh 1.528,6 điểm đầu năm, đáy ~874 điểm giữa tháng 11 – Người Quan Sát" items={[{ a: "~1.500", b: "đầu năm", at: 0.3, col: "#5dff9b" }, { a: "~870", b: "giữa tháng 11", at: 1.6, col: "#ff4d5e" }]} />)],
    [3, () => CD((t) => <Big2 t={t} items={[{ a: "−40%", b: "hơn bốn mươi phần trăm", at: 0.2, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S12", shots: [
    [0, () => CD((t) => <PhoneCard t={t} time="14:45" date="11/2022" notifs={[{ app: "Công ty chứng khoán", col: "#ff4d5e", title: "BÁN GIẢI CHẤP", body: "Phiên thứ 3 liên tiếp", at: 0.3 }]} hue="red" />)],
    [1, () => D3(closeT("cry", { acc: ["phone", "tears"] }), (t) => <>{BL(1040, 110, "Em ơi, có tiền không, cho anh vay tạm…", 0.3, "r")(t)}</>)],
    [2, () => D3(S("room", "roomdim", [[1.3, 1.35, 2.3], [NX, 1.05, RZ], 34], [[1.3, 1.32, 2.0], [NX, 1.05, RZ], 30], [T_("sad", { acc: ["phone", "glow"] })], RM), (t) => <>{BL(120, 110, "Tiền hàng của em cũng đang lỗ đây anh.", rel("S12", 3, sc("S12").sens[2].a))(t)}</>)],
  ] },
  { id: "S13", shots: [
    [0, () => D3(S("room", "roomdim", [[1.3, 1.35, 2.3], [NX, 1.05, RZ], 34], [[1.25, 1.32, 1.8], [NX, 1.05, RZ], 26], [T_("nervous", { acc: ["phone", "glow"] })], RM), (t) => <BigText t={t} at={0.3} text="SAI LẦM CỦA TRANG" col="#ff4d5e" y={90} size={110} />)],
    [1, () => D3(MC("dh_pho", [trangAt("nervous", { acc: ["box"] }), C("c51", [1.3, 0, 0.8], P("grin", { side: -1, mode: "stand", acc: ["phone"], wave: 1 }))]), (t) => <><LocTag t={t} l1="ĐÔNG HƯNG · BÊN KIA CẦU" />{BL(1060, 110, "Đô còn lên nữa! Ai giữ đô người ấy thắng!", 0.2, "r")(t)}</>)],
    [2, () => D3(doi([trangRun("worried"), ...queue(4, "neutral")], [[GOLD_X + 10, 2.2, 1.4], [GOLD_X + 5, 1.2, 5], 46], [[GOLD_X + 6, 1.6, 2.2], [GOLD_X + 2, 1.2, 5], 42], { rain: true, ease: "lin" }), (t) => <BigText t={t} at={0.4} text="MUA ĐÔ Ở GIÁ CAO NHẤT NĂM" col="#ff4d5e" y={90} size={96} />)],
  ] },
  { id: "S14", shots: [
    [0, () => CD(PR("mc_kalong", (t) => <BigText t={t} at={0.3} text="TIỀN CHẠY THEO TIN ĐỒN…" col="#fff" y={90} size={96} />))],
    [1, () => CD((t) => <Big2 t={t} head="Giá USD bán ra tại một ngân hàng lớn" src="VnExpress International, 3/1/2023: 23.660 đồng" items={[{ a: "~23.660", b: "đầu tháng 1/2023", at: 0.4, col: "#5dff9b" }]} />)],
    [3, () => D3(S("room", "roomdim", [[1.3, 1.35, 2.3], [NX, 1.05, RZ], 34], [[1.3, 1.32, 2.0], [NX, 1.05, RZ], 30], [T_("cry", { acc: ["tears"] })], RM), (t) => <BigText t={t} at={0.5} text="LỖ THÊM LẦN NỮA" col="#ff4d5e" y={90} size={110} />)],
  ] },
  { id: "S15", shots: [
    [0, () => D3(S("room", "roomdim", ...roomTwo2, [D_("sad"), T_("sad", { acc: ["paper"] })], RM), (t) => <LocTag t={t} l1="NHÀ TRANG · MÓNG CÁI · TẾT 2023" l2="Cộng lại thiệt hại của một năm" />)],
    [1, () => D3(S("room", "roomdim", [[1.0, 1.35, 2.4], [LX, 1.05, RZ], 34], [[0.9, 1.32, 2.0], [LX, 1.05, RZ], 30], [D_("sad"), T_("neutral")], RM), (t) => <>{BL(120, 110, "Mình không thua thị trường. Mình thua vì không hiểu một cuộc họp ở Mỹ.", 0.2)(t)}</>)],
  ] },
  { id: "S16", shots: [
    [0, () => D3(S("streetday", "day", ...teaH, tea("neutral", "smile", {}, { acc: ["paper"] })), (t) => <BigText t={t} at={0.3} text="SỢI DÂY" col="#ffd23f" y={90} size={130} />)],
    [1, () => CD((t) => <LessonCard t={t} title="Sợi dây lãi suất" items={[{ n: "1", icon: "🇺🇸", head: "Lãi suất Mỹ tăng", body: "kéo đầu dây", at: 0.3 }, { n: "2", icon: "💵", head: "Đô la mạnh lên", body: "tỷ giá trong nước chịu sức ép", at: at("S16", 1, 3) - at("S16", 1, 1) }, { n: "3", icon: "🏦", head: "Bán dự trữ / giữ lãi suất cao", body: "vay khó hơn", at: at("S16", 1, 4) - at("S16", 1, 1) }, { n: "4", icon: "📉", head: "Tiền rời chứng khoán", body: "ai đứng cuối dây bị giật ngã", at: at("S16", 1, 5) - at("S16", 1, 1) }]} />)],
  ] },
  { id: "S17", shots: [
    [0, () => CD(PR("eccles", (t) => <LocTag t={t} l1="THÁNG 9/2026" l2="Sợi dây được kéo lại" />))],
    [1, () => CD((t) => <Big2 t={t} head="Lãi suất Fed" src="Báo Pháp luật 29/10/2026" items={[{ a: "+0,25%", b: "tháng 9/2026", at: 0.3, col: "#ff4d5e" }, { a: "3,75–4%", b: "giữ nguyên 28/10/2026", at: 1.6, col: "#ffd23f" }]} />)],
    [2, () => CD((t) => <Big2 t={t} items={[{ a: "12/2026", b: "thị trường đặt cược tăng tiếp", at: 0.3, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S18", shots: [[0, () => CD((t) => <Rows t={t} title="Tỷ giá ngày 11/11/2026" foot="Nguồn: Thị trường Tài chính Tiền tệ, 11/11/2026" rows={[{ l: "Tỷ giá trung tâm", v: "25.611 đ/USD", at: 0.6, big: true }, { l: "Giá bán ra tại một ngân hàng lớn", v: "25.820 đ/USD", at: at("S18", 0, 1) + 0.4 }]} />)]] },
  { id: "S19", shots: [
    [0, () => D3(closeT("nervous", { acc: ["phone", "glow"] }), (t) => <ClockTag t={t} text="11/2026" />)],
    [1, () => D3(S("room", "room", [[-0.6, 1.5, 2.4], [-0.3, 1.1, 0.6], 40], [[-0.5, 1.45, 2.0], [-0.3, 1.1, 0.6], 34], [C("cuong", [-0.3, 0, 0.6], P("laugh", { side: 1, acc: ["phone", "glow"], wave: 1 }))], RM), (t) => <>{BL(1060, 110, "Vay ký quỹ gấp đôi mà bắt đáy đi!", 0.2, "r")(t)}<LocTag t={t} l1="BÌNH BẮT ĐÁY" /></>)],
    [2, () => D3(S("room", "room", ...roomTwo2, [D_("nervous", { acc: ["phone"] }), T_("stern", { acc: ["paper"], wave: 1 })], RM), (t) => <BigText t={t} at={rel("S19", 3, sc("S19").sens[2].a)} text="TỜ GIẤY CÓ SỢI DÂY" col="#ffd23f" y={90} size={100} />)],
  ] },
  { id: "S20", shots: [[0, () => D3(S("streetday", "day", ...teaH, [C("huy", TH, P("smile", { side: -1, acc: ["cup"] }))]), (t) => <LocTag t={t} l1="HUY NGUYỄN" l2="4 điều rút ra" />)], [1, () => D3(S("streetday", "day", ...teaW, tea("neutral", "smile", {}, { wave: 1 })))]] },
  { id: "S21", shots: [[0, () => CD((t) => <LessonCard t={t} title="1. Nhìn lãi suất Mỹ trước khi nhìn mã" items={[{ n: "1", icon: "🇺🇸", head: "Mỹ đang tăng lãi suất?", body: "tiền có xu hướng rút khỏi thị trường như Việt Nam", at: at("S21", 0, 1) }]} />)]] },
  { id: "S22", shots: [[0, () => CD((t) => <LessonCard t={t} title="2. Không vay ký quỹ khi dây đang bị kéo" items={[{ n: "2", icon: "⚠", head: "Thị trường giảm 20%", body: "tài khoản vay ký quỹ có thể mất gần hết", at: at("S22", 0, 1) }]} />)], [1, () => D3(closeT("sad", { acc: ["phone"] }))]] },
  { id: "S23", shots: [[0, () => CD((t) => <LessonCard t={t} title="3. Chốt tỷ giá qua ngân hàng" items={[{ n: "3", icon: "🚫", head: "Không mua đô ở kênh không chính thức", body: "rủi ro pháp lý, thường mua đúng đỉnh", at: at("S23", 0, 1) }, { n: "✓", icon: "🏦", head: "Hợp đồng mua ngoại tệ kỳ hạn", body: "chốt trước tỷ giá cho lô hàng", at: at("S23", 0, 2) }]} />)]] },
  { id: "S24", shots: [[0, () => CD((t) => <LessonCard t={t} title="4. Doanh nghiệp đứng ở đầu nào?" items={[{ n: "+", icon: "🚢", head: "Xuất khẩu thu đô", body: "thường được lợi về tỷ giá", at: at("S24", 0, 1) }, { n: "−", icon: "📦", head: "Vay nợ / nhập nguyên liệu bằng đô", body: "chịu thiệt", at: at("S24", 0, 2) }, { n: "?", icon: "📑", head: "Đọc báo cáo tài chính", body: "tìm nợ vay ngoại tệ, doanh thu xuất khẩu", at: at("S24", 0, 3) }]} />)]] },
  { id: "S25", shots: [
    [0, () => D3(S("room", "room", ...roomTwo2, [D_("smile", { acc: ["phone"] }), T_("smile")], RM), (t) => <BigText t={t} at={0.4} text="KHÔNG VAY" col="#5dff9b" y={90} size={130} />)],
    [2, () => D3(closeT("smile", { acc: ["phone", "glow"] }, "room"), (t) => <BigText t={t} at={0.4} text="MUA ĐỀU BẰNG TIỀN NHÀN RỖI" col="#5dff9b" y={90} size={92} />)],
    [3, () => D3(MC("mc_cuakhau2", [trangAt("laugh", { acc: ["paper"] })]), (t) => <BigText t={t} at={0.3} text="CHỐT TỶ GIÁ LÔ HÀNG TẾT" col="#5dff9b" y={90} size={100} />)],
    [4, () => D3(PH("mc_savi", [0.5, 0.6], [C("quang", [-0.15, 0, 0.7], P("laugh", { side: -1, mode: "stand" })), C("trang", [0.95, 0, 0.7], P("laugh", { side: 1, mode: "stand", wave: 1 }))], pcam(0.4)), (t) => <><LocTag t={t} l1="MŨI SA VĨ · ĐỊA ĐẦU TỔ QUỐC" /><BigText t={t} at={0.6} text="NGỦ NGON" col="#ffd23f" y={240} size={130} /></>)],
  ] },
  { id: "S26", shots: [[0, () => CD((t) => <Ask t={t} />)]] },
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
export const DOLA1_FRAMES = TOTAL_F;
export const Dola1Video: React.FC = () => {
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
        {audio ? <Audio src={staticFile("dola1/voice.wav")} /> : null}
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
