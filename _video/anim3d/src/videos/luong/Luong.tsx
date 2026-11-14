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

const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => CD((t) => <PhoneCard t={t} time="17:30" date="Thứ Bảy, 25/10" notifs={[{ app: "Ngân hàng", col: "#2ecc71", title: "Lương tháng 10 · Long", body: "+18.000.000 đ", at: at("S01", 0, 1) + 0.9 }, { app: "Ngân hàng", col: "#2ecc71", title: "Lương tháng 10 · Ngân", body: "+12.000.000 đ", at: at("S01", 0, 1) + 2.4 }]} hue="navy" />)],
    [2, () => D3(S("room", "room", ...roomTwo, [lg("laugh", { wave: 1 }), ng("laugh")], RM), (t) => <>{BL(140, 120, "Tối nay đi ăn nướng!", at("S01", 2, 3))(t)}</>)],
    [4, () => CD((t) => <BankCard t={t} clock="23:00 · 05/11" amt="312.000 đ" at={at("S01", 4, 6)} />)],
    [7, () => CD((t) => <PhoneCard t={t} time="23:01" date="05/11" notifs={[{ app: "Điện thoại", col: "#2ecc71", title: "Mẹ đang gọi…", body: "Cuộc gọi đến", at: 0.2 }]} quote={["Mẹ", "Con ơi, bố nằm viện rồi, con có 20 triệu không?"]} qAt={1.0} hue="red" />)],
    [8, () => D3(S("room", "roomdim", [[1.3, 1.35, 2.3], [NX, 1.05, RZ], 34], [[1.3, 1.32, 2.0], [NX, 1.05, RZ], 30], [ng("sad", { acc: ["phone", "glow", "tears"] })], RM))],
  ] },
  { id: "S02", shots: [[0, () => CD((t) => <TitleCard t={t} kicker="CHUYỆN TIỀN CÓ THẬT" l1="LƯƠNG 30 TRIỆU" l2="NGÀY 5 CÒN 312 NGHÌN" sub="Vậy tiền đã đi đâu?" hue="red" />)]] },
  { id: "S03", shots: [
    [0, () => D3(PH("chungcu", [0.5, 0.6], [C("longbh", [-1.4, 0, 2.6], P("smile", { side: -1, mode: "stand", acc: ["box"] }))], ccam), (t) => <LocTag t={t} l1="CHUNG CƯ · CẦU GIẤY" l2="Long Bóc Hộp – lập trình viên, lương 18 triệu" />)],
    [1, () => D3(S("room", "room", [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [lg("laugh", { acc: ["box", "phone"] })], RM), (t) => <BigText t={t} at={0.3} text="LONG BÓC HỘP" col="#ffd23f" y={90} size={100} />)],
    [2, () => D3(PH("chungcu", [0.5, 0.6], [C("baove", [-2.2, 0, 2.6], P("neutral", { side: 1, mode: "stand", acc: ["box"] })), C("longbh", [-1.2, 0, 2.6], P("smile", { side: -1, mode: "stand" }))], ccam), (t) => <>{BL(1080, 110, "Lại hàng của anh Long à? Tháng này là hộp thứ 12 rồi đấy.", 0.3, "r")(t)}</>)],
    [3, () => D3(S("room", "roomdim", [[1.4, 1.3, 2.2], [NX, 1.0, RZ], 34], [[1.4, 1.28, 1.9], [NX, 1.0, RZ], 30], [ng("smile", { acc: ["phone", "glow"] })], RM), (t) => <><LocTag t={t} l1="NGÂN SĂN SALE" l2="Marketing, lương 12 triệu" /><ClockTag t={t} text="00:00" /></>)],
    [5, () => D3(S("room", "roomdim", ...roomTwo, [lg("smile"), ng("grin", { acc: ["phone", "glow"] })], RM), (t) => <>{BL(1060, 110, "Anh ơi, mã giảm 50%, chỉ đến 0 giờ thôi!", 0.2, "r")(t)}{BL(120, 300, "Mua đi em, mình làm ra tiền mà.", at("S03", 5, 6))(t)}</>)],
  ] },
  { id: "S04", shots: [
    [0, () => CD((t) => <Bars t={t} title="Thu nhập mỗi tháng (triệu đồng)" max={30} src="Nguồn: Cục Thống kê, lao động – việc làm quý III và 9 tháng 2026" rows={[
      { l: "Bình quân cả nước, quý III/2026", v: 9.2, lab: "9,2", col: "#7aa7ff", at: at("S04", 0, 1) + 0.6 },
      { l: "Làm công hưởng lương, thành thị", v: 11.2, lab: "11,2", col: "#a88bff", at: at("S04", 0, 2) + 0.6 },
      { l: "Nhà Long – Ngân", v: 30, lab: "30", col: "#ffd23f", at: at("S04", 0, 3) }]} />)],
    [4, () => CD((t) => <BankCard t={t} clock="Ngày 05 hằng tháng" amt="312.000 đ" at={0.5} note="Gấp hơn 3 lần bình quân… vẫn cháy túi" />)],
  ] },
  { id: "S05", shots: [[0, () => CD((t) => <Rows t={t} title="Tiền lương nhà Long đi đâu? (mỗi tháng)" foot="Số liệu chi tiêu trong phim" stamp={{ text: "LƯƠNG VỪA VỀ ĐÃ CÓ CHỦ", at: at("S05", 0, 9) }} rows={[
    { l: "🏠 Thuê căn hộ", v: "9 triệu", at: at("S05", 0, 1) }, { l: "📱 Trả góp điện thoại mới", v: "3,5 triệu", at: at("S05", 0, 2) },
    { l: "🛵 Trả góp xe máy", v: "3 triệu", at: at("S05", 0, 3) }, { l: "💳 Thẻ tín dụng (trả tối thiểu)", v: "2,5 triệu", at: at("S05", 0, 4) },
    { l: "🍜 Đồ ăn giao tận nơi, cà phê", v: "6 triệu", at: at("S05", 0, 5) }, { l: "🛒 Chợ, điện, nước, xăng", v: "4 triệu", at: at("S05", 0, 6) },
    { l: "🛍 Mua trước trả sau", v: "2 triệu", at: at("S05", 0, 7) }, { l: "CỘNG", v: "30 triệu", at: at("S05", 0, 8), big: true, col: "#ff4d5e" }]} />)]] },
  { id: "S06", shots: [
    [0, () => D3(PH("vanphong", [0.5, 0.55], [C("ngans", [-0.15, 0, 0.7], P("smile", { side: -1, mode: "stand", acc: ["cup"] })), C("hoast", [0.95, 0, 0.7], P("neutral", { side: 1, mode: "stand", acc: ["paper"] }))], pcam(0.4)), (t) => <LocTag t={t} l1="VĂN PHÒNG · GIỜ NGHỈ TRƯA" l2="Chị Hoa Sổ Tay – lương 15 triệu" />)],
    [2, () => D3(PH("vanphong", [0.5, 0.55], [C("ngans", [-0.15, 0, 0.7], P("worried", { side: -1, mode: "stand", acc: ["cup"] })), C("hoast", [0.95, 0, 0.7], P("smile", { side: 1, mode: "stand", acc: ["paper"] }))], [[[0.4, 1.4, -2.2], [0.4, 1.2, 3], 38], [[0.4, 1.38, -1.9], [0.4, 1.2, 3], 36]]), (t) => <>{BL(1080, 110, "Chị Hoa ơi, lương chị ít hơn nhà em, sao chị chẳng bao giờ hết tiền?", 0.2, "r")(t)}{BL(120, 330, "Vì lương về, chị trả cho chị trước, em ạ.", at("S06", 2, 3))(t)}{t > at("S06", 2, 4) && BL(1080, 520, "Chị nói như trong sách ấy.", at("S06", 2, 4), "r")(t)}</>)],
  ] },
  { id: "S07", shots: [
    [0, () => CD((t) => <Big2 t={t} img="luong/thetd.jpg" head="Cái bẫy không nằm ở một món to" items={[{ a: "TRẢ GÓP", b: "vài trăm nghìn mỗi tháng", at: at("S07", 0, 1), col: "#ffd23f" }, { a: "MUA TRƯỚC", b: "trả sau", at: at("S07", 0, 1) + 1.2, col: "#ff9d4d" }]} />)],
    [3, () => CD((t) => <Big2 t={t} head="Lãi thẻ tín dụng nếu chỉ trả tối thiểu" src="Nguồn: Báo Đầu tư, 4/12/2025 – mức cao nhất ở một số ngân hàng" items={[{ a: "38,8%", b: "một năm", at: at("S07", 3, 4) + 1.5, col: "#ff4d5e" }, { a: "3,99%", b: "một tháng", at: at("S07", 3, 4) + 3.5, col: "#ff4d5e" }]} />)],
    [5, () => CD((t) => <Big2 t={t} items={[{ a: "TRỄ HẠN", b: "bị phạt và bị ghi vào lịch sử tín dụng", at: 0.2, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S08", shots: [
    [0, () => D3(S("room", "roomdim", [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [lg("shock", { acc: ["phone", "glow"] })], { ...RM, rain: true }), (t) => <ClockTag t={t} text="08/11 · Bị cắt giảm" />)],
    [1, () => D3(S("room", "roomdim", ...roomTwo, [lg("sad"), ng("worried")], { ...RM, rain: true }), (t) => <>{BL(120, 110, "Em ơi, phòng anh cắt 30%, có anh.", 0.2)(t)}{BL(1080, 330, "Thế tiền nhà tháng sau thì sao anh?", at("S08", 1, 2), "r")(t)}</>)],
    [3, () => D3(S("room", "roomdim", [[0.6, 1.3, 2.0], [LX, 1.05, RZ], 32], [[0.6, 1.28, 1.7], [LX, 1.05, RZ], 28], [lg("sad", { acc: ["sweat"] })], { ...RM, rain: true }))],
    [4, () => CD((t) => <Big2 t={t} items={[{ a: "30 TRIỆU", b: "lương mỗi tháng", at: 0.2, col: "#ffd23f" }, { a: "0 ĐỒNG", b: "tiền dự phòng", at: 1.4, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S09", shots: [
    [0, () => CD((t) => <PhoneCard t={t} time="23:40" date="08/11" notifs={[{ app: "Quảng cáo", col: "#ff4d5e", title: "💸 VAY NHANH TRONG 5 PHÚT", body: "Không cần thẩm định · Giải ngân ngay", at: 0.6 }]} hue="night" />)],
    [1, () => CD((t) => <PaperCard t={t} kind="receipt" hue="night" title="HỢP ĐỒNG VAY QUA ỨNG DỤNG" sub="Tình huống trong phim" lines={[
      { text: "Số tiền vay: 10.000.000 đ", at: 0.3 }, { text: "Phí hồ sơ: −3.000.000 đ", at: at("S09", 1, 2), col: "#d8212f" },
      { text: "Thực nhận: 7.000.000 đ", at: at("S09", 1, 2) + 1.5, big: true }, { text: "Sau 7 ngày phải trả: 12.000.000 đ", at: at("S09", 1, 3), big: true, col: "#d8212f", under: true }]} />)],
    [4, () => CD((t) => <Big2 t={t} head="Lãi tính trên một năm" src="Bộ luật Dân sự 2015, Điều 468 · Em tính theo lãi đơn: trả thêm 5 triệu cho 7 triệu thực nhận trong 7 ngày" items={[{ a: "20%", b: "mức tối đa luật cho phép", at: 0.3, col: "#5dff9b" }, { a: "≈ 3.700%", b: "khoản vay của Long", at: at("S09", 4, 5) + 0.5, col: "#ff4d5e" }]} />)],
  ] },
  { id: "S10", shots: [
    [0, () => CD((t) => <ChatCard t={t} title="Tin nhắn gửi tới danh bạ của Long" msgs={[
      { who: "Số lạ", text: "Anh Long nợ quá hạn 12 triệu. Đề nghị người thân nhắc anh ấy trả ngay.", at: at("S10", 0, 1) },
      { who: "Số lạ", text: "Gửi sếp cũ, đồng nghiệp của Long: …", at: at("S10", 0, 1) + 1.6 },
      { who: "Số lạ", text: "Gửi mẹ vợ của Long: …", at: at("S10", 0, 1) + 3.0 }]} />)],
    [2, () => CD((t) => <PhoneCard t={t} time="09:12" date="16/11" notifs={[{ app: "Điện thoại", col: "#2ecc71", title: "Mẹ đang gọi…", body: "Cuộc gọi đến", at: 0.2 }]} quote={["Mẹ", "Thằng Long nó nợ ai hả con?"]} qAt={0.9} hue="red" />)],
    [3, () => D3(S("room", "roomdim", ...roomTwo, [lg("sad"), ng("stern", { acc: ["tears"] })], RM), (t) => <>{BL(1080, 110, "Sao anh không nói với em?", 0.2, "r")(t)}{BL(120, 330, "Anh sợ em lo.", at("S10", 3, 4))(t)}</>)],
  ] },
  { id: "S11", shots: [
    [0, () => D3(PH("canho", [0.5, 0.55], [C("ngans", [-0.15, 0, 0.7], P("sad", { side: -1, mode: "stand", acc: ["tears"] })), C("hoast", [0.95, 0, 0.7], P("neutral", { side: 1, mode: "stand", acc: ["paper"] }))], pcam(0.4)), (t) => <LocTag t={t} l1="NHÀ CHỊ HOA · SÁNG HÔM SAU" />)],
    [1, () => CD((t) => <PaperCard t={t} kind="note" hue="warm" title="SỔ TAY CỦA HOA" sub="5 năm ghi chép" lines={[
      { text: "Lương về → chuyển ngay 3 triệu sang tài khoản riêng", at: 0.4 }, { text: "Rồi mới tiêu phần còn lại", at: 1.6 },
      { text: "Quỹ dự phòng: đủ 6 tháng chi tiêu", at: at("S11", 1, 2), big: true }, { text: "Tích lũy cho con", at: at("S11", 1, 2) + 1.4 }]} />)],
    [3, () => D3(PH("canho", [0.5, 0.55], [C("ngans", [-0.15, 0, 0.7], P("worried", { side: -1, mode: "stand" })), C("hoast", [0.95, 0, 0.7], P("smile", { side: 1, mode: "stand", acc: ["paper"] }))], [[[0.4, 1.4, -2.2], [0.4, 1.2, 3], 38], [[0.4, 1.38, -1.9], [0.4, 1.2, 3], 36]]), (t) => <>{BL(120, 110, "Chị cho em mượn 10 triệu, trả dứt khoản vay kia ngay hôm nay.", 0.2)(t)}{BL(120, 340, "Nhưng em phải hứa với chị 3 điều.", at("S11", 3, 4))(t)}</>)],
  ] },
  { id: "S12", shots: [[0, () => CD((t) => <LessonCard t={t} title="3 điều chị Hoa dặn" items={[
    { n: "1", icon: "💰", head: "Lương về, trả cho mình trước", body: "Chuyển ngay 10–20% sang tài khoản riêng, rồi mới tiêu", at: 0.2 },
    { n: "2", icon: "🛟", head: "Quỹ dự phòng 3–6 tháng chi tiêu", body: "Làm trước mọi khoản đầu tư – cái phao khi mất việc, ốm đau", at: at("S12", 0, 2) },
    { n: "3", icon: "📈", head: "Tích lũy đều vào tài sản sinh ra tiền", body: "Không vay để tiêu, nhất là ứng dụng vay không rõ nguồn gốc", at: at("S12", 0, 4) }]} />)]] },
  { id: "S13", shots: [
    [0, () => D3(S("room", "room", ...roomTwo, [lg("smile"), ng("smile")], RM), (t) => <LocTag t={t} l1="2 THÁNG SAU" l2="Long có việc mới" />)],
    [1, () => D3(S("room", "room", [[0.5, 1.35, 2.6], [0.8, 1.05, RZ], 38], [[0.5, 1.33, 2.3], [0.8, 1.05, RZ], 36], [lg("neutral", { acc: ["glasses"] }), ng("smile", { acc: ["paper"] })], RM), (t) => <Laptop t={t} />)],
    [2, () => CD((t) => <Rows t={t} title="Viết lại 30 triệu" rows={[
      { l: "🏠 Tiền nhà (căn nhỏ hơn)", v: "9 → 6 triệu", at: 0.3, col: "#5dff9b" }, { l: "🍜 Đồ ăn giao", v: "6 → 3 triệu", at: at("S13", 2, 3), col: "#5dff9b" },
      { l: "📱 Trả góp món mới", v: "→ 0", at: at("S13", 2, 4), col: "#5dff9b" }, { l: "💰 Để riêng ngay khi lương về", v: "6 triệu (20%)", at: at("S13", 2, 5), big: true, col: "#5dff9b" }]} />)],
    [6, () => D3(S("room", "room", [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [lg("neutral", { acc: ["box"] })], RM), (t) => <BigText t={t} at={0.4} text="BÁN BỚT ĐỒ CÒN NGUYÊN HỘP" col="#ffd23f" y={90} size={84} />)],
  ] },
  { id: "S14", shots: [
    [0, () => D3(S("room", "room", ...roomTwo, [lg("laugh"), ng("laugh")], RM), (t) => <LocTag t={t} l1="3 NĂM SAU" />)],
    [1, () => CD((t) => <Big2 t={t} head="Tiền để riêng sau 3 năm (chưa tính lời)" items={[{ a: "6 tr × 36", b: "tháng", at: 0.3, col: "#ffd23f" }, { a: "216 TRIỆU", b: "tiền gốc", at: at("S14", 1, 1) + 2.4, col: "#5dff9b" }]} />)],
    [2, () => D3(S("room", "room", [[0.6, 1.3, 2.2], [LX, 1.0, RZ], 34], [[0.6, 1.28, 1.9], [LX, 1.0, RZ], 30], [lg("laugh", { acc: ["box", "phone"] })], RM), (t) => <>{t > at("S14", 2, 3) && <BigText t={t} at={at("S14", 2, 3)} text="📒 MỘT CUỐN SỔ TAY MỚI" col="#ffd23f" y={90} size={92} />}</>)],
    [4, () => CD((t) => <BankCard t={t} clock="Ngày 05 hằng tháng" amt="312.000 đ" at={0.3} ok note="Không còn cháy túi" />)],
  ] },
  { id: "S15", shots: [
    [0, () => CD((t) => <PhoneCard t={t} time="20:05" date="Tháng Chạp" notifs={[{ app: "Điện thoại", col: "#2ecc71", title: "Mẹ đang gọi…", body: "Cuộc gọi đến", at: 0.2 }]} quote={["Mẹ", "Tết này các con có về không?"]} qAt={0.9} hue="navy" />)],
    [1, () => D3(S("room", "room", [[1.3, 1.35, 2.3], [NX, 1.05, RZ], 34], [[1.3, 1.32, 2.0], [NX, 1.05, RZ], 30], [ng("laugh", { acc: ["phone"] })], RM), (t) => <>{BL(1060, 140, "Con về mẹ ạ. Lần này con có quà cho bố mẹ.", 0.2, "r")(t)}</>)],
  ] },
  { id: "S16", shots: [[0, () => CD((t) => <Ask t={t} />)]] },
];


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
export const LUONG_FRAMES = TOTAL_F;
export const LuongVideo: React.FC = () => {
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
