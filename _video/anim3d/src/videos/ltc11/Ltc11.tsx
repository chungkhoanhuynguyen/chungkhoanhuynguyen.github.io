// Lớp học Lý thuyết trò chơi – Bài 5 (16/11/2026), khung 1920x1080, 30 fps.
// Lời kể là xương sống; mỗi ví dụ lịch sử có bối cảnh riêng (núi Tần, cung Sở, sa mạc, Athens, Uruk, Tenochtitlan, thảo nguyên, Plaza, hội thảo).
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, staticFile, delayRender, continueRender, Audio, getInputProps } from "remotion";
import { Stage, Shot3D, Run, SetKey, Cast, V } from "../vang/stage";
import { Pose, Acc } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { LOP_SEATS } from "../ltc5/sets_ltc";
import { TIMING, FPS, TOTAL_F, TAIL, sc, subText, BAD, GOOD } from "./data";
import { F, sm, TitleCard, EndCard, BigText, LocTag, Vignette } from "../vang/cards";

const bl = (t: number, k = 71) => Math.floor(t * 30) % k < 4;
type PO = Omit<Pose, "expr"> & { anim?: boolean };
const P = (expr: Expr, o: PO = {}) => (t: number): Pose => { const { anim, ...r } = o; return { expr, blink: expr === "laugh" || expr === "cry" || expr === "sleepy" ? false : bl(t + (r.phase ?? 0) * 3), ...r, ...(anim ? { t: Math.round(t * 15) / 15 } : {}) }; };
const C = (a: string, p: V, pose: Cast["pose"], to?: V): Cast => ({ a, p, pose, to });
const S = (set: SetKey, light: Shot3D["light"], from: [V, V, number], to: [V, V, number], cast: Cast[], x: Partial<Shot3D> = {}): Shot3D => ({ set, light, from, to, cast, ...x });
type Seg = { k: "3d"; s: Shot3D; ov?: (t: number, d: number) => React.ReactNode } | { k: "card"; r: (t: number, d: number) => React.ReactNode };
const D3 = (s: Shot3D, ov?: (t: number, d: number) => React.ReactNode): Seg => ({ k: "3d", s, ov });
const CD = (r: (t: number, d: number) => React.ReactNode): Seg => ({ k: "card", r });
type Plan = { id: string; shots: [number, (a: number) => Seg][] };

// ---------- dàn nhân vật: mỗi người 2 điểm nhận dạng cố định ----------
// Thầy Huy: kính + sơ mi trắng · Phú Dê Già: ria + nhẫn vàng (áo tím) · Quang Hà: mũ lưỡi trai đỏ + áo xanh · Vy Kim Khâu: kính + áo đỏ tóc dài
// Trang Trâu: nhỏ nhất lớp + tai nghe (áo hồng) · Hùng Xa Lộ: mũ bảo hiểm xanh + người to · Linh Livestream: điện thoại + áo tím tóc dài
const ACC: Record<string, Acc[]> = { thay5: ["glasses"], phu5: ["ring"], qha5: [], vy5: ["glasses"], trang5: ["headset"], hung5: ["helmet"], linh5: ["phone"] };
const NAME: Record<string, string> = { thay5: "Thầy Huy", phu5: "Phú Dê Già", qha5: "Quang Hà", vy5: "Vy Kim Khâu", trang5: "Trang Trâu", hung5: "Hùng Xa Lộ", linh5: "Linh Livestream" };
const SEAT: Record<string, string> = { phu5: "phu", qha5: "qha", vy5: "vy", trang5: "trang", hung5: "hung", linh5: "linh" };
const ST = ["phu5", "qha5", "vy5", "trang5", "hung5", "linh5"];
const seatP = (k: string): V => { const [x, z] = LOP_SEATS[SEAT[k]]; return [x, 0.45, z + 0.05]; };
const TP: V = [-2.1, 0, -3.0]; // chỗ thầy đứng (trái bảng nhìn từ cuối lớp)
// lớp: máy nhìn về −z (về phía bảng) nên +x nằm bên PHẢI màn
const stu = (k: string, expr: Expr = "neutral", talk = false, extra: Acc[] = []) => C(k, seatP(k), P(expr, { mode: "sit", acc: [...ACC[k], ...extra], anim: talk, phase: ST.indexOf(k) * 0.37 }));
const allStu = (talker?: string, expr: Expr = "grin", rest: Expr = "neutral") => ST.map((k) => stu(k, k === talker ? expr : rest, k === talker));
const thay = (expr: Expr = "smile", talk = true, p: V = TP, side: 1 | -1 = 1) => C("thay5", p, P(expr, { acc: ACC.thay5, anim: talk, side }));
const fixed = (c: V, l: V, f: number): [[V, V, number], [V, V, number]] => [[c, l, f], [c, l, f]];
const drift = (c: V, l: V, f: number, dx = 0.35, dz = -0.25, df = -2): [[V, V, number], [V, V, number]] => [[c, l, f], [[c[0] + dx, c[1], c[2] + dz], l, f + df]];
// góc máy lớp học
const WIDE = (): [[V, V, number], [V, V, number]] => [[[3.2, 3.4, 9.6], [0, 2.0, -2.5], 48], [[-1.6, 3.2, 9.0], [0, 2.0, -2.5], 46]];
const BOARD = (): [[V, V, number], [V, V, number]] => [[[0.3, 3.35, 2.4], [0, 3.35, -4.3], 36], [[-0.2, 3.35, 1.9], [0, 3.35, -4.3], 34]];
const TEACH = (): [[V, V, number], [V, V, number]] => [[[-0.6, 1.75, -0.4], [-2.1, 1.45, -3.0], 36], [[-0.9, 1.7, -0.7], [-2.1, 1.45, -3.0], 33]];
const FACE = (k: string): [[V, V, number], [V, V, number]] => { const [x, , z] = seatP(k); return [[[x + 0.75, 1.45, z - 2.4], [x, 1.05, z], 36], [[x + 0.5, 1.4, z - 2.1], [x, 1.05, z], 33]]; };
const CLASS = (): [[V, V, number], [V, V, number]] => [[[-2.0, 2.4, -3.6], [0.3, 0.9, 2.2], 52], [[-1.2, 2.3, -3.8], [0.3, 0.9, 2.2], 49]];
const lop = (cam: [[V, V, number], [V, V, number]], cast: Cast[], chalk: string[] = [], chalkT = 0, light: Shot3D["light"] = "morning") => S("lop", light, cam[0], cam[1], cast, { chalk, chalkT });

// ---------- lớp phủ 2D ----------
const NameTag: React.FC<{ t: number; k: string }> = ({ t, k }) => { const a = sm(t / 0.3) * (1 - sm((t - 3.2) / 0.4)); if (a <= 0.01) return null;
  return <div style={{ position: "absolute", left: 90, top: 640, opacity: a, transform: `translateX(${(1 - a) * -30}px)`, fontFamily: F, fontWeight: 900, fontSize: 40, color: "#fff", background: "linear-gradient(90deg,#6b2fa0,#8e1d24)", padding: "10px 26px", borderRadius: 14, boxShadow: "0 6px 18px rgba(0,0,0,.4)" }}>{NAME[k]}</div>; };
const Place: React.FC<{ t: number; l1: string; l2?: string }> = ({ t, l1, l2 }) => <LocTag t={t} l1={l1} l2={l2} d={4.5} />;
const Small: React.FC<{ text: string }> = ({ text }) => <div style={{ position: "absolute", right: 34, top: 28, fontFamily: F, fontWeight: 700, fontSize: 24, color: "rgba(255,255,255,.82)", background: "rgba(0,0,0,.45)", padding: "6px 14px", borderRadius: 8 }}>{text}</div>;
const Big: React.FC<{ t: number; text: string; at?: number; col?: string; y?: number; size?: number }> = (p) => <BigText {...p} />;
const TimelineCard: React.FC<{ t: number }> = ({ t }) => { const rows: [string, string, string, number][] = [["1975", "KODAK", "Kỹ sư Kodak làm ra máy ảnh kỹ thuật số đầu tiên", 0.3], ["2012", "KODAK", "Nộp đơn phá sản", 2.6], ["2007", "NOKIA", "Vẫn là vua điện thoại", 5.6], ["2013", "NOKIA", "Bán mảng điện thoại", 8.0]];
  return <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 30%,#22305a,#0b1124)", fontFamily: F, padding: "90px 160px" }}>
    <div style={{ fontSize: 58, fontWeight: 900, color: "#f5c518", marginBottom: 40, opacity: sm(t / 0.4) }}>TO MÀ KHÔNG ĐỔI, CŨNG THUA</div>
    {rows.map(([y, co, tx, a], i) => { const k = sm((t - a) / 0.4); return <div key={i} style={{ display: "flex", alignItems: "center", gap: 36, marginBottom: 30, opacity: k, transform: `translateX(${(1 - k) * 40}px)` }}>
      <div style={{ width: 170, fontSize: 64, fontWeight: 900, color: "#fff" }}>{y}</div><div style={{ width: 200, fontSize: 40, fontWeight: 900, color: co === "KODAK" ? "#ffcc33" : "#4aa3ff" }}>{co}</div>
      <div style={{ fontSize: 42, fontWeight: 700, color: i % 2 ? "#ff6a6a" : "#e9eef5" }}>{tx}</div></div>; })}
  </AbsoluteFill>; };
const crowd = (n: number, x0: number, z0: number, dx = 0.8, dz = 0.9, cols = 4, e: Expr = "neutral", base = 0, y = 0): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (base + i), [x0 + (i % cols) * dx, y, z0 + Math.floor(i / cols) * dz], P(e, { phase: i * 0.31 })));

// ================= BẢN 6: ẢNH THẬT LÀ CHÍNH, 3D LÀ GIA VỊ =================
// Ảnh thật Ken Burns + thẻ chữ rõ (nền đặc, chữ to, biểu tượng). Lớp học 3D chỉ cho cảnh hỏi – đáp.
const Photo: React.FC<{ t: number; img: string; dir?: number; d?: number; dim?: number }> = ({ t, img, dir = 1, d = 6, dim = 0 }) => {
  const k = Math.min(1, t / d), e = k * k * (3 - 2 * k), z = 1.04 + 0.08 * e, punch = 1 + 0.03 * Math.max(0, 1 - t / 0.28);
  return <AbsoluteFill style={{ background: "#000", overflow: "hidden" }}>
    <img src={staticFile(img + ".jpg")} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z * punch}) translate(${dir * (e - 0.5) * 30}px, ${(0.5 - e) * 8}px)` }} />
    <AbsoluteFill style={{ background: "linear-gradient(180deg,rgba(0,0,0,.42) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 60%,rgba(0,0,0,.6) 100%)" }} />
    {dim > 0 ? <AbsoluteFill style={{ background: `rgba(6,8,20,${dim})` }} /> : null}
  </AbsoluteFill>; };
const PH = (img: string, ov?: (t: number) => React.ReactNode, dir = 1, dim = 0) => CD((t) => <><Photo t={t} img={img} dir={dir} dim={dim} />{ov?.(t)}</>);
const pop = (t: number, a = 0) => Math.min(1.06, sm((t - a) / 0.35) * 1.06);
// nhãn chữ rõ đặt trên ảnh: nền đặc, chữ to, tối đa 2 dòng
const Label: React.FC<{ t: number; l1: string; l2?: string; col?: string; at?: number; pos?: "tl" | "c" }> = ({ t, l1, l2, col = "#f5c518", at: a0 = 0.3, pos = "c" }) => { const a = sm((t - a0) / 0.35); if (a <= 0) return null;
  const box: React.CSSProperties = pos === "tl" ? { position: "absolute", left: 80, top: 150 } : { position: "absolute", left: 0, right: 0, top: 330, display: "flex", flexDirection: "column", alignItems: "center" };
  return <div style={{ ...box, fontFamily: F, opacity: a, transform: `translateY(${(1 - a) * 24}px)` }}>
    <div style={{ display: "inline-block", fontSize: 84, fontWeight: 900, color: "#111", background: col, padding: "10px 34px", borderRadius: 16, boxShadow: "0 10px 30px rgba(0,0,0,.5)" }}>{l1}</div>
    {l2 ? <div style={{ display: "inline-block", marginTop: 14, fontSize: 50, fontWeight: 800, color: "#fff", background: "rgba(8,10,24,.82)", padding: "8px 26px", borderRadius: 12 }}>{l2}</div> : null}</div>; };
// thẻ ghi chú cho cảnh 3D lớp học (thay chữ phấn mờ)
const Note: React.FC<{ t: number; lines: string[]; title?: string; col?: string }> = ({ t, lines, title, col = "#6b2fa0" }) => { const a = sm((t - 0.25) / 0.35);
  return <div style={{ position: "absolute", right: 70, top: 90, width: 820, fontFamily: F, opacity: a, transform: `translateX(${(1 - a) * 40}px)`, background: "rgba(10,12,26,.84)", border: "2px solid rgba(255,255,255,.14)", borderRadius: 22, padding: "26px 36px", boxShadow: "0 14px 40px rgba(0,0,0,.45)", borderLeft: `14px solid ${col}` }}>
    {title ? <div style={{ fontSize: 34, fontWeight: 800, color: "#f5c518", marginBottom: 8 }}>{title}</div> : null}
    {lines.map((l, i) => <div key={i} style={{ fontSize: lines.length > 2 ? 48 : 60, fontWeight: 900, color: "#fff", lineHeight: 1.2, opacity: sm((t - 0.4 - i * 0.35) / 0.3) }}>{l}</div>)}</div>; };
// Sở – Tần đặt cạnh nhau
const DUEL: [string, string, string, string[]][] = [["SỞ", "ltc6/so_song", "#3ddc84", ["Đất rộng nhất", "Dân đông nhất", "Sông ngòi màu mỡ", "Văn chương rực rỡ"]], ["TẦN", "ltc6/tan_nui", "#ff9f3a", ["Núi non khô cằn", "Rìa phía tây", "Bị gọi là man di"]]];
const Duel: React.FC<{ t: number; mode: "so" | "tan" | "both" | "win" }> = ({ t, mode }) => <AbsoluteFill style={{ background: "#0b0d18", fontFamily: F }}>
  {DUEL.map(([name, img, col, pts], i) => { const on = mode === "both" || mode === "win" || (mode === "so" ? i === 0 : i === 1 || true); const act = mode === "so" ? i === 0 : mode === "tan" ? i === 1 : true;
    const lose = mode === "win" && i === 0, k = Math.min(1, t / 7), z = 1.04 + 0.06 * k;
    return <div key={name} style={{ position: "absolute", top: 0, bottom: 0, left: i * 960, width: 960, overflow: "hidden", borderLeft: i ? "6px solid #0b0d18" : undefined }}>
      <img src={staticFile(img + ".jpg")} style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${z})`, filter: lose ? "grayscale(1) brightness(.45)" : act ? "none" : "brightness(.35) saturate(.6)" }} />
      <AbsoluteFill style={{ background: "linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 35%,rgba(0,0,0,.25) 60%,rgba(0,0,0,.7) 100%)" }} />
      <div style={{ position: "absolute", left: 50, top: 60, fontSize: 120, fontWeight: 900, color: col, textShadow: "0 6px 20px #000", opacity: on ? 1 : 0.4 }}>{name}</div>
      <div style={{ position: "absolute", left: 54, top: 200 }}>{pts.map((p, j) => { const a = act ? sm((t - 0.3 - j * 0.45) / 0.3) : mode === "both" || mode === "win" ? 1 : 0;
        return <div key={j} style={{ fontSize: 46, fontWeight: 800, color: "#fff", background: "rgba(8,10,24,.78)", padding: "6px 20px", borderRadius: 10, marginBottom: 12, display: "table", opacity: a }}>{i === 0 ? "✔ " : "✘ "}{p}</div>; })}</div>
      {mode === "win" && i === 1 ? <div style={{ position: "absolute", right: 60, top: 600, fontSize: 70, fontWeight: 900, color: "#111", background: "#f5c518", padding: "12px 30px", borderRadius: 14, transform: `rotate(-6deg) scale(${pop(t, 0.6)})` }}>🏆 THẮNG · 221 TCN</div> : null}
      {mode === "win" && i === 0 ? <div style={{ position: "absolute", left: 60, top: 600, fontSize: 64, fontWeight: 900, color: "#fff", background: "#c62828", padding: "10px 28px", borderRadius: 14, transform: `rotate(5deg) scale(${pop(t, 1.0)})` }}>BỊ TẦN DIỆT</div> : null}
    </div>; })}
  {mode === "both" ? <div style={{ position: "absolute", left: 960 - 95, top: 470, width: 190, height: 190, borderRadius: 95, background: "#e62117", color: "#fff", fontSize: 80, fontWeight: 900, display: "flex", alignItems: "center", justifyContent: "center", transform: `scale(${pop(t, 0.1)})`, boxShadow: "0 0 0 10px rgba(255,255,255,.9)" }}>VS</div> : null}
  {mode === "both" ? <div style={{ position: "absolute", left: 0, right: 0, top: 700, textAlign: "center" }}><span style={{ fontSize: 76, fontWeight: 900, color: "#111", background: "#f5c518", padding: "8px 36px", borderRadius: 16, opacity: sm((t - 0.6) / 0.3) }}>Nếu là bạn, bạn cược ai?</span></div> : null}
</AbsoluteFill>;
// 3 thước đo (cur = số ô đã hiện; lose = gạch đỏ)
const MEAS: [string, string, string, string][] = [["⚡", "NĂNG LƯỢNG", "Khát khao · chịu khó · mục tiêu rõ", "#ff9f3a"], ["🔓", "CỞI MỞ", "Chịu học cái mới · chịu nhận sai", "#3ddc84"], ["🤝", "GẮN KẾT", "Coi nhau như người nhà · dám hy sinh", "#4aa3ff"]];
const LOSE = ["Trên bóc lột · dưới ngập nợ", "Kiêu ngạo · khép kín", "Giàu nghèo chênh lệch · mỗi người một ngả"];
const Three: React.FC<{ t: number; cur: number; lose?: boolean; bg?: string; title: string }> = ({ t, cur, lose, bg, title }) => <AbsoluteFill style={{ fontFamily: F }}>
  {bg ? <Photo t={t} img={bg} dim={0.62} /> : <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 30%,#2a1d50,#0b0820)" }} />}
  <div style={{ position: "absolute", left: 0, right: 0, top: 70, textAlign: "center", fontSize: 64, fontWeight: 900, color: "#f5c518" }}>{title}</div>
  <div style={{ position: "absolute", left: 90, right: 90, top: 200, display: "flex", gap: 40 }}>{MEAS.map(([ic, h, b, c], i) => { const vis = i < cur, a = i === cur - 1 ? pop(t, 0.15) : vis ? 1 : 0, x = lose && vis;
    return <div key={h} style={{ flex: 1, height: 480, background: "rgba(255,255,255,.95)", borderRadius: 26, borderTop: `16px solid ${c}`, padding: "30px 26px", textAlign: "center", opacity: Math.min(1, a), transform: `scale(${0.92 + 0.08 * Math.min(1, a)})`, position: "relative" }}>
      <div style={{ fontSize: 120 }}>{ic}</div><div style={{ fontSize: 58, fontWeight: 900, color: c, marginTop: 10 }}>{h}</div>
      <div style={{ fontSize: 40, fontWeight: 700, color: "#222", marginTop: 18, lineHeight: 1.25 }}>{x ? LOSE[i] : b}</div>
      {x ? <div style={{ position: "absolute", inset: 0, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 260, color: "rgba(214,40,40,.5)", fontWeight: 900, transform: `scale(${pop(t, i === cur - 1 ? 0.5 : -1)})` }}>✗</div> : null}</div>; })}</div>
</AbsoluteFill>;
// danh sách có biểu tượng, hiện dần (cur)
const List: React.FC<{ t: number; title: string; items: [string, string][]; cur: number; bg?: string; small?: string }> = ({ t, title, items, cur, bg, small }) => <AbsoluteFill style={{ fontFamily: F }}>
  {bg ? <Photo t={t} img={bg} dim={0.66} /> : <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 30%,#22305a,#0b1124)" }} />}
  <div style={{ position: "absolute", left: 160, top: 80, fontSize: 62, fontWeight: 900, color: "#f5c518" }}>{title}</div>
  <div style={{ position: "absolute", left: 160, right: 160, top: 200 }}>{items.map(([ic, s], i) => { const a = i < cur ? (i === cur - 1 ? sm((t - 0.2) / 0.3) : 1) : 0;
    return <div key={i} style={{ display: "flex", alignItems: "center", gap: 30, background: i === cur - 1 ? "rgba(255,255,255,.97)" : "rgba(255,255,255,.82)", borderRadius: 20, padding: "16px 30px", marginBottom: 22, opacity: a, transform: `translateX(${(1 - a) * 50}px)` }}>
      <div style={{ fontSize: 70, width: 90, textAlign: "center" }}>{ic}</div><div style={{ fontSize: 54, fontWeight: 900, color: "#151528" }}>{s}</div></div>; })}</div>
  {small ? <Small text={small} /> : null}</AbsoluteFill>;
// vòng đời 7 nấc (một cách nhìn)
const STEPS: [string, string][] = [["🌱", "Khởi nghiệp: hợp tác để sống"], ["👑", "Đặc quyền truyền cho con cháu"], ["⚔️", "Đông con, ít ghế → chia phe, mở đất"], ["✨", "Tranh nhau → sáng tạo rực rỡ"], ["💍", "Quyền quý kết thông gia, giữ ghế"], ["🕳️", "Hội kín: khép kín · tham nhũng · chia rẽ"], ["🗡️", "Thuê lính đánh thuê → lính thay chủ"]];
const Ladder: React.FC<{ t: number; cur: number }> = ({ t, cur }) => <AbsoluteFill style={{ background: "radial-gradient(circle at 30% 20%,#2b2050,#0a0a1a)", fontFamily: F }}>
  <div style={{ position: "absolute", left: 120, top: 46, fontSize: 56, fontWeight: 900, color: "#f5c518" }}>VÒNG ĐỜI MỘT NỀN VĂN MINH</div>
  <div style={{ position: "absolute", left: 124, top: 116, fontSize: 30, fontWeight: 700, color: "#b9c0d8" }}>Một cách nhìn thầy đọc được trên mạng – không phải định luật</div>
  <div style={{ position: "absolute", left: 120, right: 120, top: 170 }}>{STEPS.map(([ic, s], i) => { const n = i + 1, now = n === cur, vis = n <= cur, a = now ? sm((t - 0.15) / 0.3) : vis ? 1 : 0.18;
    const bad = n >= 5; return <div key={i} style={{ display: "flex", alignItems: "center", gap: 22, height: 78, marginBottom: 8, opacity: a, transform: now ? `translateX(${(1 - sm(t / 0.3)) * 40}px)` : undefined }}>
      <div style={{ width: 70, height: 70, borderRadius: 35, background: now ? (bad ? "#e53935" : "#f5c518") : "rgba(255,255,255,.18)", color: now ? "#111" : "#fff", fontSize: 40, fontWeight: 900, display: "flex", alignItems: "center", justifyContent: "center" }}>{n}</div>
      <div style={{ fontSize: 44, width: 60 }}>{ic}</div>
      <div style={{ fontSize: now ? 50 : 42, fontWeight: now ? 900 : 700, color: now ? "#fff" : "#cfd5e6", background: now ? (bad ? "rgba(229,57,53,.35)" : "rgba(245,197,24,.22)") : undefined, padding: now ? "6px 20px" : 0, borderRadius: 12 }}>{s}</div></div>; })}</div>
</AbsoluteFill>;
// hai cột (cách nhìn 1 | 2, lên | xuống, giả định | phản biện)
const Two: React.FC<{ t: number; L: [string, string, string[]]; R: [string, string, string[]]; cur: 1 | 2; bg?: string }> = ({ t, L, R, cur, bg }) => <AbsoluteFill style={{ fontFamily: F }}>
  {bg ? <Photo t={t} img={bg} dim={0.66} /> : <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 30%,#22305a,#0b1124)" }} />}
  <div style={{ position: "absolute", left: 100, right: 100, top: 110, display: "flex", gap: 50 }}>{[L, R].map(([h, c, ls], i) => { const a = i === 0 ? (cur === 1 ? sm((t - 0.2) / 0.3) : 1) : cur === 2 ? sm((t - 0.2) / 0.3) : 0;
    return <div key={i} style={{ flex: 1, background: "rgba(255,255,255,.96)", borderRadius: 24, borderTop: `16px solid ${c}`, padding: "30px 36px", minHeight: 440, opacity: a, transform: `translateY(${(1 - a) * 30}px)` }}>
      <div style={{ fontSize: 56, fontWeight: 900, color: c }}>{h}</div>{ls.map((l, j) => <div key={j} style={{ fontSize: 46, fontWeight: 800, color: "#1a1a2e", marginTop: 18, lineHeight: 1.2 }}>{l}</div>)}</div>; })}</div>
</AbsoluteFill>;
const Rank: React.FC<{ t: number; cur: number }> = ({ t, cur }) => <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 30%,#1f3b2e,#08140e)", fontFamily: F }}>
  <div style={{ position: "absolute", left: 0, right: 0, top: 80, textAlign: "center", fontSize: 62, fontWeight: 900, color: "#f5c518" }}>KẾT QUẢ TRÒ CHƠI THẾ GIỚI</div>
  {[["🥇", "1. Nhóm MỸ", "giàu nhất từ đầu", "#e9eef5"], ["🥈", "2. Nhóm PAKISTAN", "khởi đầu gần như TRẮNG TAY", "#5dff9b"]].map(([ic, a, b, c], i) => { const v = i < cur ? (i === cur - 1 ? pop(t, 0.2) : 1) : 0;
    return <div key={i} style={{ position: "absolute", left: 300, right: 300, top: 220 + i * 230, background: "rgba(255,255,255,.95)", borderRadius: 24, padding: "24px 40px", display: "flex", alignItems: "center", gap: 30, opacity: Math.min(1, v), transform: `scale(${0.9 + 0.1 * Math.min(1, v)})` }}>
      <div style={{ fontSize: 110 }}>{ic}</div><div><div style={{ fontSize: 64, fontWeight: 900, color: "#151528" }}>{a}</div><div style={{ fontSize: 42, fontWeight: 800, color: i ? "#1b8a4c" : "#555" }}>{b}</div></div></div>; })}
</AbsoluteFill>;
const GD = "Giả định đọc trên mạng – không phải dự báo";

const CtaLtc: React.FC<{ t: number }> = ({ t }) => <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 35%,#3a1d5a,#0b0820)", fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}>
  <div style={{ fontSize: 46, fontWeight: 800, color: "#f5c518", opacity: sm(t / 0.4) }}>CÂU HỎI CHO ANH CHỊ</div>
  <div style={{ fontSize: 76, fontWeight: 900, color: "#fff", marginTop: 16, padding: "0 120px", opacity: sm((t - 0.4) / 0.4) }}>Đã bao giờ mua thêm chỉ vì không muốn nhận sai?</div>
  <div style={{ fontSize: 40, fontWeight: 700, color: "#cfc3ff", marginTop: 40, opacity: sm((t - 4) / 0.4) }}>Bài tóm tắt miễn phí: chungkhoanhuynguyen.com · Nhóm cộng đồng: link ở mô tả</div>
</AbsoluteFill>;
const FQ = (k: string, e: Expr, l: string[], c: string) => D3(lop(FACE(k), [...allStu(k, e)]), (t) => <><NameTag t={t} k={k} /><Note t={t} lines={l} col={c} /></>);
const TQ = (e: Expr, l: string[], c?: string, title?: string) => D3(lop(TEACH(), [thay(e)]), (t) => <Note t={t} lines={l} col={c} title={title} />);
const ESC: [string, string][] = [["🛒", "Mua lần 1 → giảm"], ["🙈", "Không muốn nhận sai → mua thêm"], ["💸", "Đã bỏ nhiều quá → mua thêm nữa"], ["🔥", "Đốt dần đường lui"]];
const RULE: [string, string][] = [["🧊", "Biết mình dừng ở đâu TRƯỚC khi vào"], ["🪜", "Mỗi bước chừa 1 bậc để lùi · không vay quá sức"], ["🙇", "Chấp nhận mất mặt · giữ quyền chơi ván sau"]];

const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => PH("ltc10/san_gd", (t) => <Label t={t} at={0.5} l1="CỔ PHIẾU GIẢM 20%" l2="Bán · hay mua thêm cho giá vốn thấp?" col="#ff6a6a" />)],
    [1, () => PH("ltc11/havana", (t) => <Label t={t} at={0.4} l1="MỘT ĐÊM NĂM 1962" l2="Thứ đặt lên bàn: bom hạt nhân" col="#ff9f3a" />)],
    [2, () => PH("ltc11/tau_ngam", (t) => <Label t={t} at={0.4} l1="NGƯỜI CỨU THẾ GIỚI" l2="là người biết DỪNG LẠI" col="#3ddc84" />)],
  ] },
  { id: "S02", shots: [
    [0, () => FQ("hung5", "cry", ["Tối thứ Sáu", "Hùng Xa Lộ bơ phờ"], "#1565c0")],
    [1, () => FQ("hung5", "nervous", ["“Mua thêm 3 lần bình quân giá", "hết tiền mà nó vẫn giảm”"], "#1565c0")],
    [2, () => TQ("stern", ["Hôm nay em", "nghe kỹ nhé"])],
    [3, () => PH("ltc11/cuba", (t) => <Place t={t} l1="13 NGÀY NGHẸT THỞ" l2="Thế kỷ 20" />)],
  ] },
  { id: "S03", shots: [
    [0, () => TQ("smile", ["Thầy kể…"])],
    [1, () => PH("ltc11/u2_anh", (t) => <Place t={t} l1="THÁNG 10/1962" l2="Ảnh do thám: bãi phóng tên lửa trên đảo Cuba" />)],
    [2, () => PH("ltc11/ten_lua", (t) => <Label t={t} at={0.4} l1="~150 KM TỚI BỜ BIỂN MỸ" l2="Tên lửa có thể mang đầu đạn hạt nhân" col="#ff6a6a" />)],
  ] },
  { id: "S04", shots: [
    [0, () => PH("ltc11/phong_hop", (t) => <Label t={t} at={0.4} l1="TƯỚNG LĨNH: NÉM BOM NGAY" col="#ff6a6a" />)],
    [1, () => PH("ltc11/cuba", (t) => <Label t={t} at={0.4} l1="NƯỚC ĐI KHÁC: PHONG TỎA ĐƯỜNG BIỂN" col="#f5c518" />)],
    [2, () => PH("ltc11/cuba", (t) => <Label t={t} at={0.3} l1="LEO THANG · NHƯNG CHỪA ĐƯỜNG LUI" col="#3ddc84" />, -1)],
  ] },
  { id: "S05", shots: [
    [0, () => PH("ltc11/havana", (t) => <Place t={t} l1="24/10/1962" l2="Tàu Liên Xô tiến tới vòng phong tỏa" />)],
    [1, () => PH("ltc11/havana", (t) => <Label t={t} at={0.2} l1="CẢ THẾ GIỚI NÍN THỞ" />, -1, 0.3)],
    [2, () => PH("ltc11/havana", (t) => <Label t={t} at={0.4} l1="CÁC CON TÀU DỪNG LẠI" l2="Có chiếc quay đầu" col="#3ddc84" />)],
    [3, () => PH("ltc11/phong_hop", (t) => <Label t={t} at={0.4} l1="“BÊN KIA ĐÃ CHỚP MẮT TRƯỚC”" l2="Đại ý lời một quan chức Mỹ" />)],
  ] },
  { id: "S06", shots: [
    [0, () => PH("ltc11/tau_ngam", (t) => <Label t={t} at={0.3} l1="CHUYỆN ĐÁNG SỢ NHẤT: DƯỚI ĐÁY BIỂN" col="#ff6a6a" />, 1, 0.3)],
    [1, () => PH("ltc11/tau_ngam", (t) => <Place t={t} l1="27/10/1962" l2="Bom chìm loại nhỏ ép tàu ngầm nổi lên" />)],
    [2, () => PH("ltc11/tau_ngam", (t) => <Label t={t} at={0.4} l1="MẤT LIÊN LẠC · TƯỞNG CHIẾN TRANH ĐÃ NỔ" l2="Chỉ huy muốn phóng ngư lôi hạt nhân" col="#ff6a6a" />, -1, 0.35)],
  ] },
  { id: "S07", shots: [
    [0, () => CD((t) => <List t={t} title="CẦN CẢ 3 SĨ QUAN ĐỒNG Ý" items={[["✅", "Sĩ quan 1: đồng ý"], ["✅", "Sĩ quan 2: đồng ý"], ["❌", "Arkhipov: KHÔNG"]]} cur={2} bg="ltc11/tau_ngam" />)],
    [1, () => CD((t) => <List t={t} title="CẦN CẢ 3 SĨ QUAN ĐỒNG Ý" items={[["✅", "Sĩ quan 1: đồng ý"], ["✅", "Sĩ quan 2: đồng ý"], ["❌", "Arkhipov: KHÔNG"]]} cur={3} bg="ltc11/tau_ngam" />)],
    [2, () => PH("ltc11/tau_ngam", (t) => <Label t={t} at={0.3} l1="NGƯ LÔI KHÔNG ĐƯỢC PHÓNG" col="#3ddc84" />)],
    [3, () => PH("ltc11/havana", (t) => <Label t={t} at={0.4} l1="“NGƯỜI ĐÃ CỨU THẾ GIỚI”" l2="Theo nhiều sử gia" col="#3ddc84" />)],
  ] },
  { id: "S08", shots: [
    [0, () => TQ("grin", ["Khủng hoảng", "kết thúc thế nào?"], "#e62117")],
    [1, () => FQ("phu5", "smug", ["“Bên nào mạnh hơn", "thì bên kia chịu thua”"], "#7b3fbf")],
    [2, () => FQ("vy5", "stern", ["“Em đoán", "cả hai cùng lùi”"], "#c62828")],
  ] },
  { id: "S09", shots: [
    [0, () => TQ("laugh", ["Vy đúng."], "#1b8a4c")],
    [1, () => CD((t) => <Two t={t} L={["LIÊN XÔ", "#ff9f3a", ["Rút tên lửa khỏi Cuba"]]} R={["MỸ", "#4aa3ff", ["Hứa không đánh Cuba", "BÍ MẬT rút tên lửa khỏi Thổ Nhĩ Kỳ"]]} cur={1} />)],
    [2, () => CD((t) => <Two t={t} L={["LIÊN XÔ", "#ff9f3a", ["Rút tên lửa khỏi Cuba"]]} R={["MỸ", "#4aa3ff", ["Hứa không đánh Cuba", "BÍ MẬT rút tên lửa khỏi Thổ Nhĩ Kỳ"]]} cur={2} />)],
    [3, () => PH("ltc11/ten_lua", (t) => <Label t={t} at={0.4} l1="MỘT BẬC THANG ĐỂ BƯỚC XUỐNG" l2="Mà không mất mặt" col="#3ddc84" />)],
  ] },
  { id: "S10", shots: [[0, () => CD((t) => <TitleCard t={t} kicker="LỚP HỌC LÝ THUYẾT TRÒ CHƠI" l1="BÀI 5" l2="LUẬT LEO THANG" hue="night" />)]] },
  { id: "S11", shots: [
    [0, () => PH("ltc11/duong", (t) => <Label t={t} at={0.4} l1="HAI CHIẾC XE LAO VÀO NHAU" />)],
    [1, () => PH("ltc11/duong", (t) => <Label t={t} at={0.4} l1="BẺ LÁI TRƯỚC = NHÁT GAN" l2="Không ai bẻ = cả hai cùng chết" col="#ff6a6a" />, -1)],
    [2, () => PH("ltc11/duong", (t) => <Label t={t} at={0.3} l1="TRÒ CHƠI KẺ NHÁT GAN" col="#f5c518" />)],
    [3, () => TQ("stern", ["Mạnh hơn", "chưa chắc thắng"], "#e62117")],
    [4, () => TQ("smile", ["Kiểm soát mức leo thang", "+ chừa đường lui cho CẢ HAI"], "#1b8a4c", "NGƯỜI THẮNG")],
  ] },
  { id: "S12", shots: [
    [0, () => FQ("qha5", "grin", ["“Sao không leo thang", "thật mạnh cho sợ luôn?”"], "#00838f")],
    [1, () => TQ("stern", ["Leo quá mạnh =", "tự đốt đường lui"], "#e62117")],
    [2, () => TQ("stern", ["Trò chơi sẽ", "điều khiển em"])],
  ] },
  { id: "S13", shots: [
    [0, () => PH("ltc11/san_choi", (t) => <Place t={t} l1="Ở SÂN TRƯỜNG" l2="Hai cậu bé cãi nhau" />)],
    [2, () => CD((t) => <List t={t} title="LEO THANG Ở SÂN TRƯỜNG" items={[["👐", "Xô"], ["💥", "Xô lại mạnh hơn"], ["👊", "Đấm"], ["👥", "Gọi anh em tới"]]} cur={2} bg="ltc11/san_choi" />)],
    [3, () => CD((t) => <List t={t} title="LEO THANG Ở SÂN TRƯỜNG" items={[["👐", "Xô"], ["💥", "Xô lại mạnh hơn"], ["👊", "Đấm"], ["👥", "Gọi anh em tới"]]} cur={3} bg="ltc11/san_choi" />)],
    [4, () => CD((t) => <List t={t} title="LEO THANG Ở SÂN TRƯỜNG" items={[["👐", "Xô"], ["💥", "Xô lại mạnh hơn"], ["👊", "Đấm"], ["👥", "Gọi anh em tới"]]} cur={4} bg="ltc11/san_choi" />)],
    [5, () => PH("ltc11/san_choi", (t) => <Label t={t} at={0.4} l1="MỖI BƯỚC ĐỀU CÓ VẺ HỢP LÝ" l2="Vì lùi lại thì mất mặt" col="#ff9f3a" />, -1)],
    [6, () => PH("ltc11/san_choi", (t) => <Label t={t} at={0.2} l1="LEO THANG SINH RA LEO THANG" col="#ff6a6a" />)],
  ] },
  { id: "S14", shots: [
    [0, () => FQ("trang5", "nervous", ["“Liên quan gì chuyện", "Hùng mua thêm ạ?”"], "#2e7d32")],
    [1, () => FQ("hung5", "dazed", ["Thầy: em đang chơi trò", "leo thang với thị trường"], "#1565c0")],
  ] },
  { id: "S15", shots: [
    [0, () => CD((t) => <List t={t} title="BẪY LEO THANG CAM KẾT" items={ESC} cur={1} bg="ltc10/san_gd" />)],
    [1, () => CD((t) => <List t={t} title="BẪY LEO THANG CAM KẾT" items={ESC} cur={2} bg="ltc10/san_gd" />)],
    [2, () => CD((t) => <List t={t} title="BẪY LEO THANG CAM KẾT" items={ESC} cur={3} bg="ltc10/san_gd" />)],
    [3, () => CD((t) => <List t={t} title="BẪY LEO THANG CAM KẾT" items={ESC} cur={4} bg="ltc10/san_gd" />)],
  ] },
  { id: "S16", shots: [
    [0, () => PH("ltc11/concorde", (t) => <Label t={t} at={0.3} l1="MỘT VÍ DỤ NỔI TIẾNG" />)],
    [1, () => PH("ltc11/concorde", (t) => <Label t={t} at={0.4} l1="ANH + PHÁP: MÁY BAY SIÊU THANH CONCORDE" />, -1)],
    [2, () => PH("ltc11/concorde", (t) => <Label t={t} at={0.4} l1="CHI PHÍ ĐỘI GẤP NHIỀU LẦN" l2="Vẫn rót tiền vì đã bỏ quá nhiều" col="#ff6a6a" />)],
    [3, () => PH("ltc11/concorde", (t) => <Label t={t} at={0.3} l1="“SAI LẦM CONCORDE”" col="#f5c518" />, -1)],
  ] },
  { id: "S17", shots: [
    [0, () => FQ("linh5", "grin", ["“Thị trường có", "bom chìm không thầy?”"], "#ad1457")],
    [1, () => TQ("stern", ["Có:", "VAY KÝ QUỸ"], "#e62117")],
    [2, () => PH("ltc10/san_gd", (t) => <Label t={t} at={0.4} l1="GIẢM TỚI MỨC → BỊ BÁN KHÔNG CẦN HỎI" col="#ff6a6a" />)],
    [3, () => PH("ltc10/san_gd", (t) => <Label t={t} at={0.3} l1="MẤT QUYỀN QUYẾT ĐỊNH" col="#ff6a6a" />, -1, 0.3)],
  ] },
  { id: "S18", shots: [
    [0, () => PH("ltc1/saigon", (t) => <Place t={t} l1="VIỆT NAM 2022" l2="Bán giải chấp hàng loạt" />)],
    [1, () => CD((t) => <List t={t} title="VÒNG XOÁY GIẢI CHẤP" items={[["📉", "Người này bị bán → giá giảm"], ["📉", "Giá giảm → người khác bị bán"], ["🌀", "Không ai điều khiển được"]]} cur={2} bg="ltc10/san_gd" />)],
    [2, () => CD((t) => <List t={t} title="VÒNG XOÁY GIẢI CHẤP" items={[["📉", "Người này bị bán → giá giảm"], ["📉", "Giá giảm → người khác bị bán"], ["🌀", "Không ai điều khiển được"]]} cur={3} bg="ltc10/san_gd" />)],
  ] },
  { id: "S19", shots: [
    [0, () => FQ("hung5", "nervous", ["“Vậy em phải", "làm sao hả thầy?”"], "#1565c0")],
    [1, () => TQ("smile", ["Học người chỉ huy tàu ngầm", "và cách kết thúc khủng hoảng Cuba"])],
    [2, () => CD((t) => <List t={t} title="3 ĐIỀU KHI ĐÃ LỠ LEO THANG" items={RULE} cur={1} />)],
  ] },
  { id: "S20", shots: [
    [0, () => CD((t) => <List t={t} title="3 ĐIỀU KHI ĐÃ LỠ LEO THANG" items={RULE} cur={2} />)],
    [2, () => CD((t) => <List t={t} title="3 ĐIỀU KHI ĐÃ LỠ LEO THANG" items={RULE} cur={3} />)],
  ] },
  { id: "S21", shots: [
    [0, () => FQ("vy5", "stern", ["“Có người mua thêm khi", "giảm mà vẫn giàu đó thầy”"], "#c62828")],
    [1, () => TQ("smile", ["Đúng."])],
    [2, () => CD((t) => <Two t={t} L={["CHIẾN LƯỢC", "#3ddc84", ["Công ty tốt, giá rẻ", "Kế hoạch định trước", "Tiền nhàn rỗi"]]} R={["LEO THANG", "#ff6a6a", ["Không chịu nhận sai", "Quyết lúc đang nóng", "Tiền đi vay"]]} cur={1} />)],
    [3, () => CD((t) => <Two t={t} L={["CHIẾN LƯỢC", "#3ddc84", ["Công ty tốt, giá rẻ", "Kế hoạch định trước", "Tiền nhàn rỗi"]]} R={["LEO THANG", "#ff6a6a", ["Không chịu nhận sai", "Quyết lúc đang nóng", "Tiền đi vay"]]} cur={2} />)],
  ] },
  { id: "S22", shots: [
    [0, () => FQ("phu5", "dazed", ["“Sao biết mình chiến lược", "hay đang leo thang?”"], "#7b3fbf")],
    [1, () => TQ("smile", ["Tự hỏi một câu…"])],
    [2, () => PH("ltc10/san_gd", (t) => <Label t={t} at={0.4} l1="HÔM NAY CHƯA CÓ MÃ NÀY" l2="Có mua ở giá này không?" col="#f5c518" />)],
    [3, () => PH("ltc10/san_gd", (t) => <Label t={t} at={0.3} l1="KHÔNG → ĐANG LEO THANG" col="#ff6a6a" />, -1)],
  ] },
  { id: "S23", shots: [
    [0, () => TQ("smile", ["Nhiều chi tiết khủng hoảng Cuba", "vẫn còn tranh luận"], undefined, "LƯU Ý")],
    [1, () => D3(lop(CLASS(), [...allStu(undefined, "neutral", "smile")]), (t) => <Note t={t} lines={["Một cách nhìn,", "không phải công thức thắng chắc"]} />)],
  ] },
  { id: "S24", shots: [
    [0, () => TQ("smile", ["Mỗi mã đang cầm: giảm tới đâu thì dừng?", "Viết TRƯỚC giờ mở cửa"], "#1b8a4c", "BÀI VỀ NHÀ")],
    [1, () => FQ("hung5", "grin", ["Hùng lấy bút", "ghi ngay"], "#1565c0")],
    [2, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "smile")]), (t) => <Note t={t} lines={["Giữ cái đầu lạnh", "khi xung quanh đang nóng"]} />)],
  ] },
  { id: "S25", shots: [[0, () => CD((t) => <CtaLtc t={t} />)]] },
];

function teaStall() { return [] as Cast[]; }
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
export const LTC11_FRAMES = TOTAL_F;
export const Ltc11Video: React.FC = () => {
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
        {audio ? <Audio src={staticFile("ltc11/voice.wav")} /> : null}
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
