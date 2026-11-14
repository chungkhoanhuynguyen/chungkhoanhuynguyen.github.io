// Phim 3D #4 "Lương 30 triệu – ngày 5 còn 312 nghìn". Khung 1920x1080, 30 fps.
// Mỗi câu thoại có mốc thời gian thật (timing.json do giọng Huy70_HaiDang30 đọc) → cắt cảnh đúng câu, phụ đề đúng chữ.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, staticFile, delayRender, continueRender, Audio, getInputProps } from "remotion";
import { Stage, Shot3D, Run, SetKey, Cast, V } from "../vang/stage";
import { Pose, Acc } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { GOLD_X, HOME_X } from "../vang/sets";
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
const Laptop: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.6);
  return <div style={{ position: "absolute", right: 90, top: 150, width: 640, opacity: a, transform: `translateY(${(1 - a) * 40}px)`, fontFamily: F }}>
    <div style={{ background: "#0f1420", border: "12px solid #2a2f3a", borderRadius: 18, overflow: "hidden" }}>
      <div style={{ background: "#2a2f3a", padding: "6px 14px", fontSize: 20, color: "#cfd6e4" }}>🔒 chungkhoanhuynguyen.com</div>
      <div style={{ background: "linear-gradient(135deg,#3a1d6e,#1d1240)", padding: 26, color: "#fff" }}>
        <div style={{ fontSize: 22, color: "#f5c518", fontWeight: 800 }}>HỌC CHO NGƯỜI MỚI</div>
        <div style={{ fontSize: 36, fontWeight: 900, marginTop: 6 }}>Quỹ dự phòng bao nhiêu là đủ?</div>
        <div style={{ marginTop: 14, fontSize: 22, color: "#d9d2f0" }}>Chi tiêu thiết yếu × 3–6 tháng</div>
        <div style={{ marginTop: 10, height: 14, width: 420, background: "rgba(255,255,255,.15)", borderRadius: 7 }}><div style={{ height: 14, width: 420 * Math.min(1, t / 6), background: "#5dff9b", borderRadius: 7 }} /></div></div></div>
    <div style={{ height: 22, margin: "0 -40px", background: "#3a404c", borderRadius: "0 0 20px 20px" }} /></div>; };
const Ask: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.5), clickT = t - 3.6, sub = clickT > 0.35;
  return <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><Bg t={t} hue="navy" />
    <div style={{ opacity: a, position: "relative" }}><div style={{ fontSize: 40, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>CÂU HỎI CHO NHÀ MÌNH</div>
      <div style={{ fontSize: 96, fontWeight: 900, color: "#fff", marginTop: 20, lineHeight: 1.15 }}>LƯƠNG VỀ ĐƯỢC<br />MẤY NGÀY THÌ HẾT?</div>
      <div style={{ display: "inline-block", marginTop: 50, padding: "22px 64px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 48, fontWeight: 900 }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI KÊNH"}</div></div>
    {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 1060 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 820 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
    <div style={{ position: "absolute", left: 40, bottom: 22, fontSize: 28, fontWeight: 700, color: "rgba(255,255,255,.55)" }}>chungkhoanhuynguyen.com</div>
    <div style={{ position: "absolute", right: 40, bottom: 20, fontSize: 22, color: "rgba(255,255,255,.5)" }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư · Ảnh: Wikimedia Commons (CC BY / CC BY-SA)</div></AbsoluteFill>; };


// ===== Nâng cấp motion (học từ awesome-opus5-5-videos 14/11): lò xo đóng, mờ khi cắt, hạt phim, vệt sáng, tối viền =====
const spr = (t: number, w = 14, z = 0.62) => t <= 0 ? 0 : 1 - Math.exp(-z * w * t) * Math.cos(w * Math.sqrt(1 - z * z) * t);   // lò xo đóng, vượt nhẹ
const Grain: React.FC<{ t: number; o?: number }> = ({ t, o = 0.09 }) => <AbsoluteFill style={{ opacity: o, mixBlendMode: "overlay", pointerEvents: "none" }}>
  <svg width="100%" height="100%"><filter id={"g" + (Math.floor(t * 24) % 6)}><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves={2} seed={Math.floor(t * 24) % 6} /></filter><rect width="100%" height="100%" filter={`url(#g${Math.floor(t * 24) % 6})`} /></svg></AbsoluteFill>;
const Leak: React.FC<{ t: number; dir: number }> = ({ t, dir }) => <AbsoluteFill style={{ pointerEvents: "none", mixBlendMode: "screen", opacity: 0.22, background: `radial-gradient(circle at ${50 + dir * (20 + 12 * Math.sin(t * 0.5))}% ${30 + 8 * Math.cos(t * 0.4)}%, rgba(255,170,90,.55), rgba(255,120,60,0) 45%)` }} />;
const Photo: React.FC<{ t: number; img: string; d?: number; dir?: number }> = ({ t, img, d = 7, dir = 1 }) => { const k = Math.min(1, t / Math.max(d, 1)); const e = k * k * (3 - 2 * k); const z = 1.05 + 0.09 * e;
  const cut = Math.max(0, 1 - t / 0.28); const punch = 1 + 0.035 * cut;   // mờ + đẩy nhẹ khi vào cảnh, không fade đen
  return <AbsoluteFill style={{ background: "#000", overflow: "hidden" }}><img src={staticFile(`ltc1/${img}.jpg`)} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z * punch}) translate(${dir * (e - 0.5) * 34}px, ${(0.5 - e) * 10}px)`, filter: `brightness(.8) saturate(1.08) contrast(1.06) blur(${(cut * 9).toFixed(2)}px)` }} />
    <Leak t={t} dir={dir} />
    <AbsoluteFill style={{ background: "radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.55) 100%)" }} />
    <AbsoluteFill style={{ background: "linear-gradient(180deg,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 28%,rgba(0,0,0,0) 62%,rgba(0,0,0,.55) 100%)" }} /><Grain t={t} /></AbsoluteFill>; };
const PR = (img: string, ov?: (t: number) => React.ReactNode, dir = 1) => (t: number) => <><Photo t={t} img={img} dir={dir} />{ov?.(t)}</>;
// ---------- dàn cảnh ----------
// Phòng (room): máy nhìn −z → +x bên PHẢI màn. Long đứng trái màn (side +1), Ngân phải màn (side −1).
const LX = 0.35, NX = 1.3, RZ = 0.6;
const lg = (e: Expr, o: PO = {}) => C("longbh", [LX, 0, RZ], P(e, { side: 1, mode: "stand", ...o }));
const ng = (e: Expr, o: PO = {}) => C("ngans", [NX, 0, RZ], P(e, { side: -1, mode: "stand", ...o }));
const RM = { chat: "off" as const, game: false };
const PH = (bg: string, fit: [number, number], cast: Cast[], cam: [[V, V, number], [V, V, number]], x: Partial<Shot3D> = {}) => S("photo", "room", cam[0], cam[1], cast, { bg: `luong/${bg}.jpg`, bgFit: fit, ...x });
const ccam: [[V, V, number], [V, V, number]] = [[[0.2, 1.5, -6], [0.2, 3.7, 10], 46], [[0.2, 1.5, -5.6], [0.2, 3.7, 10], 45]];
const pcam = (x = 0, z = 2.2): [[V, V, number], [V, V, number]] => [[[x, 1.45, -3.2], [x, 1.25, 3], 42], [[x, 1.42, -2.8], [x, 1.25, 3], 40]];
const BL = (x: number, y: number, text: string, at0: number, tail: "l" | "r" = "l") => (t: number) => <Bubble t={t} at={at0} text={text} x={x} y={y} tail={tail} w={620} />;

// ===== LỚP HỌC LÝ THUYẾT TRÒ CHƠI – BÀI 1 (kể + ảnh thật, lớp học bằng ảnh + thẻ tên + bóng thoại) =====
const NameCard: React.FC<{ t: number; name: string; sub: string }> = ({ t, name, sub }) => { const a = Math.min(1.08, spr(t - 0.15));
  return <div style={{ position: "absolute", left: 90, bottom: 300, fontFamily: F, opacity: Math.min(1, a * 1.4), transform: `translateX(${(1 - a) * -120}px)` }}>
    <div style={{ display: "inline-block", fontSize: 92, fontWeight: 900, color: "#fff", background: "#e62117", padding: "6px 28px", borderRadius: 12 }}>{name}</div>
    <div style={{ marginTop: 14, fontSize: 46, fontWeight: 800, color: "#ffe14d", textShadow: "0 3px 10px #000" }}>{sub}</div></div>; };
const Chalk: React.FC<{ t: number; text: string; at?: number; size?: number }> = ({ t, text, at: a0 = 0.2, size = 110 }) => { const a = sm((t - a0) / 0.6); if (t < a0) return null;
  return <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}><div style={{ fontFamily: F, fontWeight: 900, fontSize: size, color: "#f4f1e4", textAlign: "center", maxWidth: 1600, lineHeight: 1.15, whiteSpace: "pre-line", padding: "30px 60px", background: "rgba(20,40,32,.82)", border: "10px solid #7a5a33", borderRadius: 18, clipPath: `inset(0 ${100 - a * 100}% 0 0)`, textShadow: "0 0 6px rgba(255,255,255,.35)" }}>{text}</div></AbsoluteFill>; };
const CDNC = (img: string, name: string, sub: string, dir = 1) => CD(PR(img, (t) => <NameCard t={t} name={name} sub={sub} />, dir));
const CDCH = (img: string, text: string, size?: number, a0 = 0.2) => CD(PR(img, (t) => <Chalk t={t} text={text} size={size} at={a0} />));
const CDBT = (img: string, text: string, col = "#ffd23f", size = 100, dir = 1) => CD(PR(img, (t) => <BigText t={t} at={0.2} text={text} col={col} y={90} size={Math.min(size, Math.floor(1560 / (text.length * 0.6)))} />, dir));
const CDLT = (img: string, l1: string, l2: string) => CD(PR(img, (t) => <LocTag t={t} l1={l1} l2={l2} d={6} />));
const CDSAY = (img: string, text: string, a0: number, dir = 1) => CD(PR(img, (t) => <>{BL(140, 120, text, a0)(t)}</>, dir));
const CDLS = (title: string, id: string, k: number, its: [number, string, string, string][]) => CD((t) => <LessonCard t={t} title={title} items={its.map(([j, icon, head, body], i) => ({ n: String(i + 1), icon, head, body, at: at(id, k, j) }))} />);
const AskL: React.FC<{ t: number }> = ({ t }) => <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center" }}><Bg t={t} hue="navy" />
  <div style={{ position: "relative", textAlign: "center", opacity: sm(t / 0.5) }}><div style={{ fontSize: 44, color: "#f5c518", fontWeight: 800 }}>BÀI TẬP CHO BẠN</div>
    <div style={{ fontSize: 96, color: "#fff", fontWeight: 900, marginTop: 20 }}>Gia đình bạn được mấy điểm?</div>
    <div style={{ fontSize: 60, color: "#ffe14d", fontWeight: 800, marginTop: 30 }}>⚡ Năng lượng · 🚪 Cởi mở · 🤝 Gắn kết</div>
    <div style={{ fontSize: 40, color: "#c5cde0", marginTop: 30 }}>Kể cho mình nghe ở phần bình luận nhé</div></div></AbsoluteFill>;
const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => CDLT("lop_hoc", "LỚP HỌC LÝ THUYẾT TRÒ CHƠI", "Buổi 1")],
    [1, () => CDCH("bang_phan", "PHÚ KHÔNG QUÁ BA ĐỜI", 130, 0.6)],
    [3, () => CDBT("lop_hoc", "6 HỌC TRÒ · 6 GIA TỘC GIÀU NHẤT", "#ffd23f", 86, -1)],
    [4, () => CDCH("bang_phan", "VÌ SAO GIA TỘC CÁC EM RỒI SẼ THUA?", 88)]] },
  { id: "S02", shots: [
    [0, () => CD((t) => <TitleCard t={t} kicker="LỚP HỌC LÝ THUYẾT TRÒ CHƠI" l1="BÀI 1: VÁN CỜ THẾ GIỚI" l2="VÌ SAO KẺ NGHÈO HAY THẮNG KẺ GIÀU?" sub="Phú không quá ba đời" hue="night" />)]] },
  { id: "S03", shots: [
    [0, () => CDNC("zurich", "HANA", "🇨🇭 Gia tộc ngân hàng Thụy Sĩ · 300 năm")],
    [1, () => CDNC("seoul", "JI-HO", "🇰🇷 Cháu đích tôn tập đoàn Hàn Quốc", -1)],
    [2, () => CDNC("dau_mo", "KHALID", "🛢 Gia đình sở hữu mỏ dầu")],
    [3, () => CDNC("silicon", "SOPHIA", "💻 Bố lập công ty công nghệ ở Thung lũng Silicon", -1)],
    [4, () => CDNC("xe_nhat", "KENJI", "🚗 Gia tộc làm ô tô ở Nhật")],
    [5, () => CDNC("saigon", "BẢO NAM", "🏙 Con trai ông trùm bất động sản Việt Nam", -1)],
    [6, () => CDSAY("lop_hoc", "Thưa thầy, nhà em giàu ba đời rồi, vẫn đang giàu mà!", at("S03", 6, 6) + 0.6)],
    [7, () => CDCH("bang_phan", "THẾ CÒN ĐỜI THỨ TƯ?", 120)]] },
  { id: "S04", shots: [
    [0, () => CDBT("co_vua", "MỌI CHUYỆN TRÊN ĐỜI LÀ MỘT VÁN CỜ", "#ffd23f", 80)],
    [1, () => CDLS("LUẬT CỦA LỚP: 3 CÂU HỎI", "S04", 1, [[2, "👥", "NGƯỜI CHƠI", "Ai đang ngồi vào bàn cờ?"], [3, "📜", "LUẬT CHƠI", "Được làm gì, không được làm gì?"], [4, "🏆", "PHẦN THƯỞNG", "Thắng được gì, thua mất gì?"]])],
    [5, () => CDBT("ban_co_vua", "VÁN CỜ GIỮA CÁC QUỐC GIA", "#ffd23f", 96, -1)]] },
  { id: "S05", shots: [
    [0, () => CDCH("bang_phan", "GIÀU · ĐÔNG · MẠNH\nhay NGHÈO · NHỎ · Ở RÌA?", 92)],
    [1, () => CDSAY("lop_hoc", "Nước giàu, thưa thầy! Tiền mua được mọi thứ.", at("S05", 1, 1) + 0.5)],
    [2, () => CDSAY("lop_hoc", "Và có công nghệ tốt hơn nữa.", at("S05", 2, 2) + 0.5, -1)],
    [3, () => CDCH("bang_phan", "LỊCH SỬ THƯỜNG NÓI NGƯỢC", 110)]] },
  { id: "S06", shots: [
    [0, () => CDLT("chien_quoc", "VÍ DỤ 1", "Trung Hoa thời Chiến Quốc")],
    [2, () => CDBT("binh_ma", "221 TCN: NƯỚC TẦN Ở RÌA THỐNG NHẤT TRUNG HOA", "#ffd23f", 70)]] },
  { id: "S07", shots: [
    [0, () => CDLT("macedonia", "VÍ DỤ 2", "Hy Lạp – Macedonia")],
    [3, () => CDBT("alexander", "338 TCN: MACEDONIA THẮNG ATHENS", "#ffd23f", 80)]] },
  { id: "S08", shots: [
    [0, () => CDLT("tenochtitlan", "VÍ DỤ 3", "Mexico, năm 1519")],
    [2, () => CDBT("tenochtitlan", "500 LÍNH · 2 NĂM · ĐẾ QUỐC AZTEC SỤP ĐỔ", "#ffd23f", 70, -1)],
    [3, () => CDBT("chinh_phuc", "+ HÀNG CHỤC NGHÌN ĐỒNG MINH BẢN ĐỊA + ĐẬU MÙA", "#ff8a8a", 64)],
    [4, () => CDCH("bang_phan", "VÌ SAO KẺ THÙ TÌM ĐƯỢC NHIỀU ĐỒNG MINH?", 84)]] },
  { id: "S09", shots: [
    [0, () => CDSAY("lop_hoc", "Vậy có quy luật nào không, thưa thầy?", at("S09", 0, 0) + 0.4)],
    [1, () => CDNC("ibn_khaldun", "IBN KHALDUN", "Học giả Bắc Phi, thế kỷ 14")],
    [3, () => CDBT("ibn_khaldun", "1377: SÁCH VỀ HƯNG VONG CÁC TRIỀU ĐẠI", "#ffd23f", 72)],
    [4, () => CDCH("bang_phan", "MỘT TRIỀU ĐẠI: 3–4 THẾ HỆ", 110)]] },
  { id: "S10", shots: [
    [0, () => CDLS("3 THƯỚC ĐO SỨC MẠNH CỦA MỘT NHÓM NGƯỜI", "S10", 0, [[1, "⚡", "NĂNG LƯỢNG", "Khát khao muốn đi lên"], [2, "🚪", "CỞI MỞ", "Chịu học cái mới, chịu nhận người giỏi"], [3, "🤝", "GẮN KẾT", "Sẵn sàng hy sinh cho nhau"]])],
    [4, () => CDCH("bang_phan", "KẺ NGHÈO CÓ CẢ BA · KẺ GIÀU ĐÁNH RƠI CẢ BA", 84)]] },
  { id: "S11", shots: [
    [0, () => CDLS("VÌ SAO GIÀU LẠI ĐÁNH RƠI?", "S11", 0, [[1, "😴", "LƯỜI", "Có tiền thì ít ai muốn chịu khổ"], [2, "😤", "KIÊU", "Nghĩ mình đúng, không chịu học ai"], [3, "⚔️", "CHIA RẼ", "Anh em bắt đầu chia nhau"]])],
    [4, () => CDCH("gia_dinh", "PHÚ KHÔNG QUÁ BA ĐỜI", 120)]] },
  { id: "S12", shots: [
    [0, () => CDSAY("lop_hoc", "Nhưng gia tộc em giàu 300 năm rồi, thưa thầy!", at("S12", 0, 0) + 0.5, -1)],
    [2, () => CDBT("zurich", "DẠY CON NHƯ THỂ NHÀ VẪN NGHÈO", "#ffd23f", 90)],
    [4, () => CDCH("bang_phan", "QUY LUẬT KHÔNG PHẢI ĐỊNH MỆNH", 104)]] },
  { id: "S13", shots: [
    [0, () => CDCH("bang_phan", "KHÔNG CHỈ QUỐC GIA – CẢ DOANH NGHIỆP", 90)],
    [1, () => CDNC("kodak_cam", "KODAK", "Ông vua phim ảnh · 1975: kỹ sư Kodak làm ra máy ảnh số đầu tiên")],
    [3, () => CDBT("kodak", "2012: KODAK NỘP ĐƠN PHÁ SẢN", "#ff8a8a", 90)],
    [4, () => CDBT("nokia", "2013: NOKIA BÁN MẢNG ĐIỆN THOẠI", "#ff8a8a", 90, -1)],
    [5, () => CDCH("bang_phan", "KẺ THẮNG: NHỎ HƠN · ĐÓI HƠN · HỌC NHANH HƠN", 80)]] },
  { id: "S14", shots: [
    [0, () => CDSAY("lop_hoc", "Vậy đầu tư chứng khoán thì sao hả thầy?", at("S14", 0, 0) + 0.4)],
    [2, () => CDLS("3 CÂU HỎI TRƯỚC KHI MUA CỔ PHIẾU", "S14", 2, [[3, "⚡", "Lãnh đạo còn đói khát không?", "Năng lượng"], [4, "🔄", "Có chịu thay đổi khi thị trường đổi?", "Cởi mở"], [5, "🤝", "Người trong công ty có cùng một phía?", "Gắn kết"]])],
    [6, () => CDBT("san_ck", "TO MÀ MẤT CẢ BA = CÁI BÓNG CỦA QUÁ KHỨ", "#ffd23f", 74)]] },
  { id: "S15", shots: [
    [0, () => CDCH("bang_phan", "BÀI TẬP: CHẤM ĐIỂM GIA TỘC MÌNH · THANG 10", 84)],
    [1, () => CDSAY("lop_hoc", "Nhà em chắc năng lượng chỉ được 3 điểm…", at("S15", 1, 1) + 0.5, -1)],
    [3, () => CDCH("bang_phan", "TUẦN SAU: VÁN CỜ TIẾP THEO", 110)]] },
  { id: "S16", shots: [
    [0, () => CD((t) => <AskL t={t} />)]] },
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
export const LTC1_FRAMES = TOTAL_F;
export const Ltc1Video: React.FC = () => {
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
        {audio ? <Audio src={staticFile("hn/voice.wav")} /> : null}
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
