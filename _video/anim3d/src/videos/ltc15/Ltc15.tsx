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
const ACC: Record<string, Acc[]> = { thay5: ["glasses"], phu5: ["ring"], qha5: [], vy5: ["glasses"], trang5: ["headset"], hung5: ["helmet"], linh5: ["phone"], cuong: ["cup"], ninhkoi: [], tronghau: [] };
const NAME: Record<string, string> = { thay5: "Thầy Huy", phu5: "Phú Dê Già", qha5: "Quang Hà", vy5: "Vy Kim Khâu", trang5: "Trang Trâu", hung5: "Hùng Xa Lộ", linh5: "Linh Livestream", cuong: "Cường Sociu", ninhkoi: "Ninh Kòi", tronghau: "Trọng Hậu" };
const SEAT: Record<string, string> = { phu5: "phu", qha5: "qha", vy5: "vy", trang5: "trang", hung5: "hung", linh5: "linh", cuong: "cuong", ninhkoi: "ninh", tronghau: "hau" };
const ST = ["phu5", "qha5", "vy5", "trang5", "hung5", "linh5", "cuong", "ninhkoi", "tronghau"];
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
const FACE2 = (k: string): [[V, V, number], [V, V, number]] => { const [x, , z] = seatP(k); return [[[x - 0.95, 1.2, z - 1.9], [x, 1.15, z], 33], [[x - 0.7, 1.25, z - 1.7], [x, 1.15, z], 30]]; };
const OTS = (k: string): [[V, V, number], [V, V, number]] => { const [x, , z] = seatP(k); return [[[-2.55, 2.05, -4.0], [x, 1.1, z], 30], [[-2.45, 2.0, -3.85], [x, 1.1, z], 27]]; };
const TEACH2 = (): [[V, V, number], [V, V, number]] => [[[0.9, 2.5, 4.6], [-2.1, 1.3, -3.0], 23], [[0.5, 2.45, 4.2], [-2.1, 1.3, -3.0], 21]];
const TEACH3 = (): [[V, V, number], [V, V, number]] => [[[-3.5, 1.75, -0.5], [-2.1, 1.45, -3.0], 36], [[-3.3, 1.75, -0.8], [-2.1, 1.45, -3.0], 33]];
const TOP = (): [[V, V, number], [V, V, number]] => [[[0.5, 6.3, 9.4], [0, 0.8, 1.8], 50], [[-0.5, 6.0, 9.0], [0, 0.8, 1.8], 47]];
const SIDE = (): [[V, V, number], [V, V, number]] => [[[6.6, 2.2, 6.8], [-1.0, 1.0, 1.8], 46], [[6.4, 2.1, 5.6], [-1.0, 1.0, 1.8], 43]];
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
  <div style={{ fontSize: 76, fontWeight: 900, color: "#fff", marginTop: 16, padding: "0 120px", opacity: sm((t - 0.4) / 0.4) }}>Đã bao giờ cho người thân vay rồi mất cả tiền lẫn tình?</div>
  <div style={{ fontSize: 40, fontWeight: 700, color: "#cfc3ff", marginTop: 40, opacity: sm((t - 4) / 0.4) }}>Bài tóm tắt miễn phí: chungkhoanhuynguyen.com · Nhóm cộng đồng: link ở mô tả</div>
</AbsoluteFill>;
const hsh = (x: string) => { let h = 7; for (let i = 0; i < x.length; i++) h = (h * 31 + x.charCodeAt(i)) >>> 0; return h; };
const FQ = (k: string, e: Expr, l: string[], c: string) => { const m0 = hsh(k + l.join("")) % 3; const m = m0 === 2 && seatP(k)[2] > 4 ? 1 : m0; return D3(lop(m === 0 ? FACE(k) : m === 1 ? FACE2(k) : OTS(k), [...allStu(k, e), ...(m === 2 ? [thay("smile", false, TP)] : [])]), (t) => <><NameTag t={t} k={k} /><Note t={t} lines={l} col={c} /></>); };
const TQ = (e: Expr, l: string[], c?: string, title?: string) => { const m = hsh(l.join("")) % 3; return D3(lop(m === 0 ? TEACH() : m === 1 ? TEACH2() : TEACH3(), [thay(e), ...(m === 1 ? allStu(undefined, "neutral", "neutral") : [])]), (t) => <Note t={t} lines={l} col={c} title={title} />); };
const ESC: [string, string][] = [["🛒", "Mua lần 1 → giảm"], ["🙈", "Không muốn nhận sai → mua thêm"], ["💸", "Đã bỏ nhiều quá → mua thêm nữa"], ["🔥", "Đốt dần đường lui"]];
const RULE: [string, string][] = [["🧊", "Biết mình dừng ở đâu TRƯỚC khi vào"], ["🪜", "Mỗi bước chừa 1 bậc để lùi · không vay quá sức"], ["🙇", "Chấp nhận mất mặt · giữ quyền chơi ván sau"]];

const Drop: React.FC<{ t: number; title: string; a: string; b: string; la: string; lb: string; pct: string; src: string; bg?: string }> = ({ t, title, a, b, la, lb, pct, src, bg }) => <AbsoluteFill style={{ fontFamily: F }}>
  {bg ? <Photo t={t} img={bg} dim={0.72} /> : <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 30%,#3a1420,#12060a)" }} />}
  <div style={{ position: "absolute", left: 0, right: 0, top: 90, textAlign: "center", fontSize: 60, fontWeight: 900, color: "#f5c518" }}>{title}</div>
  <div style={{ position: "absolute", left: 0, right: 0, top: 260, display: "flex", justifyContent: "center", alignItems: "center", gap: 60 }}>
    <div style={{ textAlign: "center", opacity: sm((t - 0.2) / 0.3) }}><div style={{ fontSize: 120, fontWeight: 900, color: "#fff" }}>{a}</div><div style={{ fontSize: 34, color: "#ddd", fontWeight: 700 }}>{la}</div></div>
    <div style={{ fontSize: 110, color: "#ff5252", fontWeight: 900, opacity: sm((t - 0.8) / 0.3) }}>➜</div>
    <div style={{ textAlign: "center", opacity: sm((t - 1.1) / 0.3) }}><div style={{ fontSize: 120, fontWeight: 900, color: "#ff5252" }}>{b}</div><div style={{ fontSize: 34, color: "#ddd", fontWeight: 700 }}>{lb}</div></div>
  </div>
  <div style={{ position: "absolute", left: 0, right: 0, top: 560, textAlign: "center" }}><span style={{ fontSize: 64, fontWeight: 900, color: "#fff", background: "#d32f2f", borderRadius: 16, padding: "8px 34px", opacity: pop(t, 1.6) }}>{pct}</span></div>
  <div style={{ position: "absolute", right: 60, bottom: 200, fontSize: 24, color: "rgba(255,255,255,.75)", fontWeight: 600 }}>Nguồn: {src}</div>
</AbsoluteFill>;
const TRUST: [string, string][] = [["💵", "A có 10 đô, gửi B bao nhiêu tùy ý"], ["🔺", "Số gửi đi được nhân 3"], ["🤔", "B tự quyết trả lại bao nhiêu"], ["🙈", "Không biết mặt, không ràng buộc"]];
const TFT: [string, string][] = [["🤝", "Vòng đầu: tin"], ["😊", "Đối phương tốt → tốt lại"], ["✋", "Đối phương lừa → thôi hợp tác"]];
const SCAM: [string, string][] = [["🎁", "Vài tuần đầu cho thắng lệnh nhỏ"], ["💸", "Có khi tự bù tiền để thấy lãi"], ["🪜", "Lòng tin xây từng bậc"], ["💣", "Dồn khoản lớn → ván cuối → biến mất"]];
const SIGN: [string, string][] = [["🎯", "Hứa lãi cao và chắc chắn"], ["🏦", "Nạp tiền vào TK cá nhân / ứng dụng lạ"], ["⏳", "Giục làm ngay kẻo lỡ"], ["🔑", "Xin mật khẩu, mã xác thực"]];
const SUM15: [string, string][] = [["🪜", "Tin từng bước, phản ứng khi bị phụ"], ["🎣", "Phím hàng: cho thắng nhỏ, lấy khoản lớn"], ["🏦", "Tiền luôn ở tài khoản đứng tên mình"]];
const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => PH("ltc9/do_la2", (t) => <Label t={t} at={0.4} l1="CHO ANH HỌ VAY 200 TRIỆU" l2="Không giấy tờ · không lãi" col="#f5c518" />)],
    [1, () => PH("luong/dt_nganhang", (t) => <Label t={t} at={0.4} l1="“NHÓM CHUYÊN GIA PHÍM MÃ”" l2="Hứa 3 tháng trả" col="#ff9f3a" />)],
    [2, () => PH("ltc15/vi_tien", (t) => <Label t={t} at={0.4} l1="NHÓM CHÁT BIẾN MẤT" l2="Tài khoản còn 20 triệu" col="#ff6a6a" />)],
    [3, () => PH("ltc15/dem_pho", (t) => <Label t={t} at={0.4} l1="MẤT LUÔN MỘT NGƯỜI ANH" col="#ff6a6a" />)],
  ] },
  { id: "S02", shots: [
    [0, () => FQ("ninhkoi", "sad", ["Tin nhắn đã đọc,", "2 tuần không trả lời"], "#5d4037")],
    [1, () => FQ("tronghau", "worried", ["“Lại vay tiền à?”"], "#7b3fbf")],
    [2, () => FQ("ninhkoi", "sad", ["“Em không tiếc tiền", "bằng tiếc người”"], "#5d4037")],
  ] },
  { id: "S03", shots: [
    [0, () => FQ("phu5", "smug", ["“Cho vay là", "coi như cho luôn”"], "#6d4c41")],
    [1, () => FQ("qha5", "stern", ["“Thế thì ai dám", "giúp ai nữa hả bác?”"], "#2e7d32")],
    [2, () => D3(lop(SIDE(), [thay("smile", false), ...allStu("qha5", "stern", "grin")]), (t) => <Note t={t} lines={["Hai người cãi nhau một hồi"]} />)],
    [3, () => TQ("smile", ["Cả hai đúng một nửa"], undefined, "TRÒ CHƠI LÒNG TIN")],
  ] },
  { id: "S04", shots: [
    [0, () => PH("luong/duong_pho", (t) => <Place t={t} l1="MỸ · NĂM 1995" l2="Một thí nghiệm về lòng tin" />)],
    [1, () => CD((t) => <List t={t} title="TRÒ CHƠI LÒNG TIN" items={TRUST} cur={2} />)],
    [2, () => CD((t) => <List t={t} title="TRÒ CHƠI LÒNG TIN" items={TRUST} cur={3} />)],
    [3, () => CD((t) => <List t={t} title="TRÒ CHƠI LÒNG TIN" items={TRUST} cur={4} />)],
  ] },
  { id: "S05", shots: [
    [0, () => TQ("stern", ["Tính lạnh lùng:", "B không trả → A không gửi"])],
    [1, () => PH("ltc1/gia_dinh", (t) => <Label t={t} at={0.4} l1="THỰC TẾ: A GỬI KHOẢNG MỘT NỬA" l2="Nhiều người B có trả lại" col="#3ddc84" />)],
    [2, () => PH("ltc1/gia_dinh", (t) => <Label t={t} at={0.4} l1="CON NGƯỜI TIN NHAU" l2="nhiều hơn sách vở tưởng" col="#3ddc84" />, -1)],
    [3, () => PH("ltc15/vi_tien", (t) => <Label t={t} at={0.4} l1="NHƯNG: NHẬN VỀ ≈ SỐ ĐÃ GỬI" l2="Không ít người A mất trắng" col="#ff6a6a" />)],
  ] },
  { id: "S06", shots: [
    [0, () => FQ("linh5", "dazed", ["“Làm sao biết", "ai đáng tin hả thầy?”"], "#7b1fa2")],
    [1, () => TQ("smile", ["Một lần chơi:", "gần như không biết được"])],
    [2, () => TQ("grin", ["Chơi nhiều lần:", "khác hẳn"])],
    [3, () => PH("ltc15/may_tinh", (t) => <Label t={t} at={0.4} l1="GIẢI ĐẤU MÁY TÍNH" l2="Chơi lòng tin lặp lại nhiều vòng" col="#4aa3ff" />)],
  ] },
  { id: "S07", shots: [
    [0, () => PH("ltc15/may_tinh", (t) => <Label t={t} at={0.4} l1="VÔ ĐỊCH: “ĂN MIẾNG TRẢ MIẾNG”" col="#f5c518" />)],
    [1, () => CD((t) => <List t={t} title="ĂN MIẾNG TRẢ MIẾNG" items={TFT} cur={1} bg="ltc15/cau_thang" />)],
    [2, () => CD((t) => <List t={t} title="ĂN MIẾNG TRẢ MIẾNG" items={TFT} cur={3} bg="ltc15/cau_thang" />)],
    [3, () => PH("ltc15/cau_thang", (t) => <Label t={t} at={0.4} l1="TIN TỪNG BƯỚC NHỎ" l2="Phản ứng ngay khi bị phụ lòng" col="#3ddc84" />)],
  ] },
  { id: "S08", shots: [
    [0, () => TQ("stern", ["Ninh à,", "em đã làm ngược lại"], "#c62828")],
    [1, () => PH("ltc9/do_la2", (t) => <Label t={t} at={0.4} l1="LẦN ĐẦU ĐÃ TIN 200 TRIỆU" l2="Không giấy tờ, không mốc kiểm tra" col="#ff6a6a" />)],
    [2, () => PH("luong/dt_nganhang", (t) => <Label t={t} at={0.4} l1="ANH HỌ TIN NGƯỜI LẠ" l2="chỉ vì được thắng vài lệnh nhỏ" col="#ff6a6a" />, -1)],
  ] },
  { id: "S09", shots: [
    [0, () => PH("luong/dt_nganhang", (t) => <Label t={t} at={0.4} l1="CÁCH NHÓM PHÍM HÀNG LỪA ĐẢO LÀM" col="#ff6a6a" />)],
    [1, () => CD((t) => <List t={t} title="CHIÊU “TRÒ CHƠI LẶP LẠI”" items={SCAM} cur={1} bg="luong/dt_nganhang" />)],
    [2, () => CD((t) => <List t={t} title="CHIÊU “TRÒ CHƠI LẶP LẠI”" items={SCAM} cur={2} bg="luong/dt_nganhang" />)],
    [3, () => CD((t) => <List t={t} title="CHIÊU “TRÒ CHƠI LẶP LẠI”" items={SCAM} cur={3} bg="luong/dt_nganhang" />)],
    [4, () => CD((t) => <List t={t} title="CHIÊU “TRÒ CHƠI LẶP LẠI”" items={SCAM} cur={4} bg="luong/dt_nganhang" />)],
  ] },
  { id: "S10", shots: [
    [0, () => FQ("trang5", "shock", ["“Thế làm sao", "nhận ra ạ?”"], "#c2185b")],
    [1, () => CD((t) => <List t={t} title="4 DẤU HIỆU – GẶP LÀ DỪNG" items={SIGN} cur={0} bg="ltc12/rut_tien" />)],
    [2, () => CD((t) => <List t={t} title="4 DẤU HIỆU – GẶP LÀ DỪNG" items={SIGN} cur={1} bg="ltc12/rut_tien" />)],
    [3, () => CD((t) => <List t={t} title="4 DẤU HIỆU – GẶP LÀ DỪNG" items={SIGN} cur={2} bg="ltc12/rut_tien" />)],
    [4, () => CD((t) => <List t={t} title="4 DẤU HIỆU – GẶP LÀ DỪNG" items={SIGN} cur={3} bg="ltc12/rut_tien" />)],
    [5, () => CD((t) => <List t={t} title="4 DẤU HIỆU – GẶP LÀ DỪNG" items={SIGN} cur={4} bg="ltc12/rut_tien" />)],
    [6, () => PH("ltc12/rut_tien", (t) => <Label t={t} at={0.3} l1="GẶP 1 DẤU HIỆU LÀ DỪNG" col="#ff6a6a" />)],
  ] },
  { id: "S11", shots: [
    [0, () => FQ("hung5", "dazed", ["“Tiền anh họ Ninh", "mất ở đâu thầy?”"], "#1565c0")],
    [1, () => TQ("stern", ["Nhiều khả năng", "ở dấu hiệu thứ hai"])],
    [2, () => PH("ltc15/vi_tien", (t) => <Label t={t} at={0.4} l1="TIỀN RỜI TÀI KHOẢN ĐỨNG TÊN MÌNH" l2="= gần như rời khỏi tay mình" col="#ff6a6a" />)],
  ] },
  { id: "S12", shots: [
    [0, () => TQ("smile", ["Cho người thân vay"], undefined, "QUY TẮC 1")],
    [1, () => PH("ltc9/do_la2", (t) => <Label t={t} at={0.4} l1="CHỈ CHO VAY SỐ TIỀN" l2="mất vẫn ngủ ngon, vẫn giữ được tình" col="#3ddc84" />)],
    [2, () => PH("ltc1/gia_dinh", (t) => <Label t={t} at={0.4} l1="QUÁ SỐ ĐÓ" l2="hãy giúp bằng cách khác" col="#f5c518" />)],
  ] },
  { id: "S13", shots: [
    [0, () => PH("ltc15/cau_thang", (t) => <Label t={t} at={0.4} l1="QUY TẮC 2 · TIN TỪNG BƯỚC" col="#3ddc84" />)],
    [1, () => PH("ltc15/ky_giay", (t) => <Label t={t} at={0.4} l1="KHOẢN NHỎ TRƯỚC" l2="Giấy tờ đơn giản · mốc trả rõ" col="#f5c518" />)],
    [2, () => PH("ltc15/ky_giay", (t) => <Label t={t} at={0.4} l1="TRẢ ĐÚNG HẸN" l2="lần sau mới tính tiếp" col="#3ddc84" />, -1)],
    [3, () => PH("ltc15/ky_giay", (t) => <Label t={t} at={0.4} l1="GIẤY TỜ KHÔNG PHẢI VÌ NGHI NGỜ" l2="mà để cùng nhớ đã hứa gì" col="#4aa3ff" />)],
  ] },
  { id: "S14", shots: [
    [0, () => PH("ltc12/rut_tien", (t) => <Label t={t} at={0.4} l1="QUY TẮC 3 · KHÔNG CHO VAY ĐỂ ĐẦU TƯ" l2="nhất là theo nhóm phím hàng" col="#ff6a6a" />)],
    [1, () => PH("luong/dt_nganhang", (t) => <Label t={t} at={0.4} l1="ĐẶT CƯỢC VÀO CẢ NGƯỜI LẠ" l2="mà người thân đang tin" col="#ff9f3a" />)],
  ] },
  { id: "S15", shots: [
    [0, () => FQ("vy5", "worried", ["“Nếu đã lỡ rồi,", "như Ninh thì sao ạ?”"], "#00897b")],
    [1, () => TQ("smile", ["Trò chơi lặp lại", "có một bí mật nữa"])],
    [2, () => TQ("smile", ["Chương trình vô địch", "không thù dai"])],
    [3, () => PH("ltc1/gia_dinh", (t) => <Label t={t} at={0.4} l1="ĐỐI PHƯƠNG QUAY LẠI HỢP TÁC" l2="nó cũng hợp tác lại" col="#3ddc84" />)],
    [4, () => TQ("smile", ["Tha thứ đúng lúc", "là chiến lược, không phải yếu đuối"], "#1b8a4c")],
  ] },
  { id: "S16", shots: [
    [0, () => FQ("ninhkoi", "shock", ["Điện thoại rung lên…"], "#5d4037")],
    [1, () => PH("luong/dt_nganhang", (t) => <Label t={t} at={0.4} l1="“ANH XIN LỖI…”" l2="“Anh không dám nhìn mặt em”" col="#f5c518" />)],
    [2, () => PH("luong/dt_nganhang", (t) => <Label t={t} at={0.4} l1="“THÁNG NÀY ANH GOM ĐƯỢC 5 TRIỆU”" l2="“Anh trả dần, mỗi tháng một ít”" col="#3ddc84" />, -1)],
    [3, () => D3(lop(TOP(), [thay("smile", false), ...allStu("ninhkoi", "cry", "sad")]), (t) => <Note t={t} lines={["Ninh đọc to cho cả lớp nghe"]} />)],
  ] },
  { id: "S17", shots: [
    [0, () => FQ("cuong", "grin", ["“Ăn miếng trả miếng", "phiên bản tử tế rồi”"], "#e65100")],
    [1, () => FQ("ninhkoi", "relief", ["“Em nhận, anh trả dần,", "nhưng đừng vào mấy nhóm đó nữa”"], "#5d4037")],
    [2, () => TQ("smile", ["Tiền mất một nửa,", "giữ được người: chưa thua hết"], "#1b8a4c")],
  ] },
  { id: "S18", shots: [
    [0, () => CD((t) => <List t={t} title="TÓM TẮT BÀI 8" items={SUM15} cur={0} />)],
    [1, () => CD((t) => <List t={t} title="TÓM TẮT BÀI 8" items={SUM15} cur={1} />)],
    [2, () => CD((t) => <List t={t} title="TÓM TẮT BÀI 8" items={SUM15} cur={2} />)],
    [3, () => CD((t) => <List t={t} title="TÓM TẮT BÀI 8" items={SUM15} cur={3} />)],
  ] },
  { id: "S19", shots: [
    [0, () => TQ("smile", ["Nhóm nào từng hứa lãi chắc,", "rủ nạp tiền ra ngoài?"], "#1b8a4c", "BÀI VỀ NHÀ")],
    [1, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "smile")]), (t) => <Note t={t} lines={["Rời nhóm đó", "ngay hôm nay"]} />)],
  ] },
  { id: "S20", shots: [[0, () => CD((t) => <CtaLtc t={t} />)]] },
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
export const LTC15_FRAMES = TOTAL_F;
export const Ltc15Video: React.FC = () => {
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
        {audio ? <Audio src={staticFile("ltc15/voice.wav")} /> : null}
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
