// "Lớp học Lý thuyết trò chơi – Bài 1: Vì sao kẻ nghèo hay thắng kẻ giàu?" – bản người que 3D (15/11/2026). Khung 1920x1080, 30 fps.
// Lời kể là xương sống; mỗi ví dụ lịch sử có bối cảnh riêng (núi Tần, cung Sở, sa mạc, Athens, Uruk, Tenochtitlan, thảo nguyên, Plaza, hội thảo).
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, staticFile, delayRender, continueRender, Audio, getInputProps } from "remotion";
import { Stage, Shot3D, Run, SetKey, Cast, V } from "../vang/stage";
import { Pose, Acc } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { LOP_SEATS } from "./sets_ltc";
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
const CtaLtc: React.FC<{ t: number }> = ({ t }) => <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 35%,#3a1d5a,#0b0820)", fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}>
  <div style={{ fontSize: 46, fontWeight: 800, color: "#f5c518", opacity: sm(t / 0.4) }}>BÀI TẬP CHO ANH CHỊ</div>
  <div style={{ fontSize: 86, fontWeight: 900, color: "#fff", marginTop: 16, opacity: sm((t - 0.4) / 0.4) }}>Gia đình mình được mấy điểm?</div>
  <div style={{ display: "flex", gap: 40, marginTop: 40 }}>{[["NĂNG LƯỢNG", "#ff9f3a"], ["CỞI MỞ", "#3ddc84"], ["GẮN KẾT", "#4aa3ff"]].map(([w, c], i) => <div key={w} style={{ fontSize: 50, fontWeight: 900, color: c, border: `4px solid ${c}`, borderRadius: 18, padding: "14px 30px", opacity: sm((t - 0.9 - i * 0.3) / 0.3) }}>{w} /10</div>)}</div>
  <div style={{ fontSize: 40, fontWeight: 700, color: "#e9eef5", marginTop: 50, opacity: sm((t - 5) / 0.5) }}>📄 Tóm tắt lý thuyết trò chơi cho nhà đầu tư – miễn phí tại chungkhoanhuynguyen.com</div>
  <div style={{ fontSize: 40, fontWeight: 700, color: "#e9eef5", marginTop: 16, opacity: sm((t - 8) / 0.5) }}>👥 Nhóm cộng đồng thảo luận mỗi tuần – đường dẫn ở phần mô tả</div>
  <div style={{ position: "absolute", right: 40, bottom: 20, fontSize: 22, color: "rgba(255,255,255,.55)" }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư</div>
</AbsoluteFill>;
const crowd = (n: number, x0: number, z0: number, dx = 0.8, dz = 0.9, cols = 4, e: Expr = "neutral", base = 0, y = 0): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (base + i), [x0 + (i % cols) * dx, y, z0 + Math.floor(i / cols) * dz], P(e, { phase: i * 0.31 })));

const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => D3(S("tan", "morning", [[34, 26, 30], [0, 2, -24], 44], [[14, 16, 14], [0, 2, -24], 42], []), (t) => <><Place t={t} l1="TRUNG HOA" l2="Thời Chiến Quốc · ~2.200 năm trước" /><Big t={t} at={1.2} text="AI SẼ THẮNG?" y={300} /></>)],
    [1, () => D3(S("so", "morning", [[-12, 4.5, 20], [0, 5, -18], 42], [[10, 4.5, 18], [0, 5, -18], 40], []), (t) => <><Place t={t} l1="NƯỚC SỞ" l2="Giàu nhất · đông dân nhất" /></>)],
    [2, () => D3(S("tan", "morning", [[3.2, 1.7, 3], [0, 1.6, -20], 40], [[2.6, 1.6, 0.5], [0, 1.6, -20], 36], []), (t) => <><Place t={t} l1="NƯỚC TẦN" l2="Núi khô cằn · rìa phía tây" /></>)],
    [3, () => D3(S("so", "morning", [[4.5, 2.2, -0.5], [-2, 1.4, -7], 40], [[3.5, 2.0, -1.5], [-2, 1.4, -7], 36], []), (t) => <><Big t={t} at={0.4} text="SỞ hay TẦN?" col="#f5c518" y={260} /></>)],
  ] },
  { id: "S02", shots: [
    [0, () => D3(lop(FACE("phu5"), [...allStu("phu5", "smug")]), (t) => <NameTag t={t} k="phu5" />)],
    [1, () => D3(lop(BOARD(), [thay("smile")], ["SỞ hay TẦN?"]), (t) => <NameTag t={t} k="thay5" />)],
    [2, () => D3(S("tan", "morning", [[0, 40, 40], [0, 4, -40], 46], [[0, 30, 24], [0, 4, -40], 44], []), (t) => <Big t={t} at={0.5} text="221 TCN · TẦN THỐNG NHẤT" col="#f5c518" y={250} size={96} />)],
  ] },
  { id: "S03", shots: [
    [0, () => CD((t) => <TitleCard t={t} kicker="LỚP HỌC LÝ THUYẾT TRÒ CHƠI" l1="BÀI 1" l2="VÌ SAO KẺ NGHÈO HAY THẮNG KẺ GIÀU?" hue="night" />)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu()], ["MỌI CHUYỆN LÀ", "MỘT VÁN CỜ"], 2.5), (t) => <Place t={t} l1="HỌC VIỆN ST. ALDEN" l2="Lớp Lý thuyết trò chơi" />)],
    [1, () => D3(lop(BOARD(), [thay("stern")], ["1. AI LÀ NGƯỜI CHƠI?", "2. MỖI NGƯỜI MUỐN GÌ?", "3. LUẬT THƯỞNG PHẠT?"], 6))],
    [2, () => D3(lop(TEACH(), [thay("grin")], ["CÁC QUỐC GIA", "LÊN VÀ XUỐNG"], 1.5))],
  ] },
  { id: "S05", shots: [
    [0, () => D3(S("sa", "dawn", [[3.2, 1.5, 3.6], [0.5, 0.7, 0], 38], [[2.6, 1.4, 2.9], [0.5, 0.7, 0], 34], [C("c7", [0.2, 0.05, 0.4], P("neutral", { mode: "sit", acc: ["paper"] }))]), (t) => <Place t={t} l1="BẮC PHI · THẾ KỶ 14" l2="Học giả Ibn Khaldun" />)],
    [1, () => D3(S("sa", "morning", [[-10, 3, 6], [-12, 1, -10], 40], [[-6, 3, 6], [-12, 1, -10], 38], crowd(6, -14, -8, 1.3, 1.2, 3, "grin", 20)))],
    [2, () => D3(S("sa", "morning", [[2, 6, 4], [10, 6, -72], 36], [[8, 6, 4], [10, 6, -72], 32], []))],
    [3, () => D3(S("sa", "morning", [[-20, 2.2, 2], [6, 2, -60], 40], [[-14, 2.2, -4], [6, 2, -60], 36], crowd(8, -17, -10, 1.0, 1.0, 4, "stern", 30)))],
    [4, () => D3(S("sa", "dawn", [[1.8, 1.1, 1.6], [0.5, 0.6, 0.2], 34], [[1.5, 1.0, 1.3], [0.5, 0.6, 0.2], 30], [C("c7", [0.2, 0.05, 0.4], P("smile", { mode: "sit", acc: ["paper"] }))]), (t) => <Big t={t} at={0.6} text="TINH THẦN GẮN KẾT" col="#4aa3ff" y={260} size={100} />)],
  ] },
  { id: "S06", shots: [
    [0, () => D3(lop(BOARD(), [thay("smile")], ["NĂNG LƯỢNG", "CỞI MỞ", "GẮN KẾT"], 0.01, "morning"), (t) => <Small text="3 thước đo sức mạnh" />)],
    [1, () => D3(lop(TEACH(), [thay("grin")], ["NĂNG LƯỢNG"]), (t) => <Big t={t} at={0.3} text="⚡ NĂNG LƯỢNG" col="#ff9f3a" y={200} size={96} />)],
    [2, () => D3(lop(CLASS(), [...allStu(undefined, "neutral", "smile")], ["CỞI MỞ"]), (t) => <Big t={t} at={0.3} text="🔓 CỞI MỞ" col="#3ddc84" y={200} size={96} />)],
    [3, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "smile")], ["GẮN KẾT"]), (t) => <Big t={t} at={0.3} text="🤝 GẮN KẾT" col="#4aa3ff" y={200} size={96} />)],
  ] },
  { id: "S07", shots: [
    [0, () => D3(lop(BOARD(), [thay("stern")], ["GIÀU LÊN", "→ RƠI RỤNG?"], 1.5))],
    [1, () => D3(S("so", "morning", [[5, 2.3, -1], [-3, 1.3, -7], 40], [[3.5, 2.1, -2], [-3, 1.3, -7], 36], []), (t) => <Big t={t} at={0.8} text="NĂNG LƯỢNG ✗" col="#ff6a6a" y={230} size={92} />)],
    [2, () => D3(S("so", "morning", [[-6, 9, 8], [0, 7, -22], 40], [[-3, 8, 5], [0, 7, -22], 36], []), (t) => <Big t={t} at={0.6} text="CỞI MỞ ✗" col="#ff6a6a" y={230} size={92} />)],
    [3, () => D3(S("so", "morning", [[14, 3, 12], [0, 2, -8], 44], [[10, 3, 10], [0, 2, -8], 40], []), (t) => <Big t={t} at={0.6} text="GẮN KẾT ✗" col="#ff6a6a" y={230} size={92} />)],
    [4, () => D3(S("tan", "morning", [[2.6, 1.6, 1.0], [0, 1.6, -18], 38], [[2.2, 1.6, -1.5], [0, 1.6, -18], 34], []))],
  ] },
  { id: "S08", shots: [
    [0, () => D3(lop(FACE("vy5"), [...allStu("vy5", "stern")]), (t) => <NameTag t={t} k="vy5" />)],
    [1, () => D3(lop(TEACH(), [thay("smile")]))],
    [3, () => D3(lop(BOARD(), [thay("stern")], ["THOÁT NGHÈO", "PHẢI CÓ CẢ 3"], 1.8))],
  ] },
  { id: "S09", shots: [
    [0, () => D3(S("athens", "day", [[40, 14, 60], [0, 14, -30], 44], [[24, 12, 48], [0, 14, -30], 40], []), (t) => <Place t={t} l1="HY LẠP CỔ ĐẠI" l2="Thế kỷ 5–4 trước Công nguyên" />)],
    [2, () => D3(S("athens", "day", [[14, 22, -6], [0, 19, -33], 40], [[8, 21, -10], [0, 19, -33], 36], []), (t) => <Place t={t} l1="ATHENS" l2="Giàu nhất · hạm đội mạnh nhất" />)],
    [3, () => D3(S("athens", "day", [[-6, 20, -18], [0, 20.5, -33], 38], [[-3, 19.6, -20], [0, 20.5, -33], 34], []))],
    [4, () => D3(S("athens", "day", [[-20, 3, 46], [0, 2, 26], 40], [[-12, 3, 40], [0, 2, 26], 38], []))],
    [5, () => D3(S("athens", "day", [[0, 30, -40], [0, 22, -170], 44], [[0, 28, -60], [0, 22, -170], 40], []), (t) => <Place t={t} l1="MACEDONIA" l2="Phía bắc · bị chê là quê mùa" />)],
    [6, () => D3(S("athens", "day", [[0, 30, -60], [0, 22, -170], 40], [[0, 34, -80], [0, 22, -170], 34], []), (t) => <Big t={t} at={1} text="ALEXANDER → BA TƯ" col="#f5c518" y={240} size={92} />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(S("athens", "day", [[-30, 6, 40], [-10, 4, 10], 44], [[-20, 6, 34], [-10, 4, 10], 40], []), (t) => <Place t={t} l1="LA MÃ" l2="Một dân tộc nhỏ, nghèo ở bán đảo Ý" />)],
    [1, () => D3(S("athens", "day", [[0, 60, 80], [0, 0, -30], 46], [[0, 70, 60], [0, 0, -30], 44], []), (t) => <Big t={t} at={0.4} text="Ý → HY LẠP → CARTHAGE" col="#f5c518" y={260} size={86} />)],
  ] },
  { id: "S11", shots: [
    [0, () => D3(S("uruk", "morning", [[-30, 12, 20], [6, 5, -28], 44], [[-20, 8, 12], [6, 5, -28], 40], []), (t) => <Place t={t} l1="LƯỠNG HÀ · SUMER" l2="Giữa sông Tigris và Euphrates" />)],
    [1, () => D3(S("uruk", "morning", [[3, 1.8, 4], [-1, 1, -6], 42], [[1, 1.7, 2.5], [-1, 1, -6], 38], []), (t) => <Place t={t} l1="URUK" l2="Ngã ba buôn bán giàu nhất thời ấy" />)],
    [2, () => D3(S("uruk", "morning", [[30, 4, -40], [8, 6, -30], 40], [[24, 4, -36], [8, 6, -30], 36], crowd(10, 20, -48, 0.8, 0.9, 5, "stern", 40)), (t) => <Big t={t} at={1.5} text="AKKAD: LÍNH ĐÁNH THUÊ" col="#ff6a6a" y={240} size={86} />)],
  ] },
  { id: "S12", shots: [
    [0, () => D3(S("tenoch", "day", [[-60, 30, 60], [0, 5, -40], 44], [[-40, 22, 44], [0, 5, -40], 40], []), (t) => <Place t={t} l1="CHÂU MỸ · THẾ KỶ 14–16" l2="Người Aztec" />)],
    [1, () => D3(S("tenoch", "day", [[-30, 3, 4], [-20, 0.5, -4], 42], [[-22, 3, 4], [-20, 0.5, -4], 38], []))],
    [2, () => D3(S("tenoch", "day", [[-24, 12, 20], [0, 7, -42], 42], [[-12, 10, 16], [0, 7, -42], 38], []), (t) => <Place t={t} l1="TENOCHTITLAN" l2="Thành phố trên hồ" />)],
  ] },
  { id: "S13", shots: [
    [0, () => D3(S("tenoch", "day", [[136, 2.6, -8], [138, 2.5, 26], 44], [[140, 2.6, -5], [138, 2.5, 26], 40], []), (t) => <Big t={t} at={1} text="1519 · ~500 NGƯỜI" col="#f5c518" y={230} size={96} />)],
    [1, () => D3(S("tenoch", "day", [[-10, 6, 10], [0, 6, -42], 40], [[-6, 5, 6], [0, 6, -42], 36], []), (t) => <Big t={t} at={0.5} text="2 NĂM SAU: SỤP ĐỔ" col="#ff6a6a" y={230} size={96} />)],
    [2, () => D3(lop(BOARD(), [thay("stern")], ["DỊCH BỆNH", "ĐỒNG MINH BẢN ĐỊA", "TƯỞNG LÀ THẦN"], 5))],
    [3, () => D3(lop(TEACH(), [thay("smile")], ["…CHƯA ĐỦ"], 1))],
    [4, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "neutral")], ["MỖI NGƯỜI CHƠI", "MUỐN GÌ?"], 2))],
  ] },
  { id: "S14", shots: [
    [0, () => D3(lop(BOARD(), [thay("smile")], ["VÒNG ĐỜI 7 NẤC"], 1), (t) => <Small text="Một cách nhìn đọc trên mạng" />)],
    [1, () => D3(lop(BOARD(), [thay("smile")], ["1. KHỞI NGHIỆP: HỢP TÁC ĐỂ SỐNG"], 1.2))],
    [3, () => D3(lop(BOARD(), [thay("grin")], ["1. KHỞI NGHIỆP", "2. ĐẶC QUYỀN CHA TRUYỀN CON NỐI"], 1.2))],
    [4, () => D3(lop(BOARD(), [thay("grin")], ["1. KHỞI NGHIỆP", "2. ĐẶC QUYỀN", "3. ĐÔNG CON ÍT GHẾ → CHIA PHE"], 1.2))],
  ] },
  { id: "S15", shots: [
    [0, () => D3(lop(BOARD(), [thay("grin")], ["1. KHỞI NGHIỆP · 2. ĐẶC QUYỀN · 3. CHIA PHE", "4. TRANH NHAU → SÁNG TẠO RỰC RỠ"], 1.2))],
    [1, () => D3(lop(BOARD(), [thay("smile")], ["1 · 2 · 3 · 4", "5. QUYỀN QUÝ KẾT THÔNG GIA, GIỮ GHẾ"], 1.2))],
    [2, () => D3(lop(BOARD(), [thay("stern")], ["1 · 2 · 3 · 4 · 5", "6. HỘI KÍN: KHÉP KÍN, THAM NHŨNG, CHIA RẼ"], 1.2))],
    [3, () => D3(lop(BOARD(), [thay("stern")], ["1 · 2 · 3 · 4 · 5 · 6", "7. THUÊ LÍNH ĐÁNH THUÊ"], 1.2))],
    [4, () => D3(S("tan", "morning", [[6, 4, 4], [0, 2, -40], 40], [[3, 3, 0], [0, 2, -40], 34], []), (t) => <Big t={t} at={0.6} text="LÍNH ĐÁNH THUÊ THAY CHỦ" col="#ff6a6a" y={230} size={86} />)],
    [5, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "shock")], ["TẦN → TRUNG NGUYÊN", "MACEDONIA → HY LẠP"], 2))],
  ] },
  { id: "S16", shots: [
    [0, () => D3(lop(FACE("qha5"), [...allStu("qha5", "nervous")]), (t) => <NameTag t={t} k="qha5" />)],
    [1, () => D3(lop(BOARD(), [thay("smile")], ["NĂNG LƯỢNG · CỞI MỞ · GẮN KẾT", "hay", "THAM NHŨNG · KHÉP KÍN · CHIA RẼ"], 3))],
  ] },
  { id: "S17", shots: [
    [0, () => D3(lop(TEACH(), [thay("grin")], ["TRÒ CHƠI THẾ GIỚI"], 1.2), (t) => <Small text="Câu chuyện đọc được trên mạng" />)],
    [1, () => D3(lop(CLASS(), [...allStu(undefined, "neutral", "grin")], ["MỸ · ANH · ẤN ĐỘ · PAKISTAN · NHẬT"], 2.5), (t) => <Big t={t} at={0.4} text="MỖI NHÓM MỘT NƯỚC" col="#f5c518" y={200} size={86} />)],
    [2, () => D3(lop(BOARD(), [thay("smile")], ["PHONG BÌ: GIẤY · KÉO · THƯỚC", "có nhóm gần như TRẮNG TAY"], 2.5))],
    [3, () => D3(lop(BOARD(), [thay("smile")], ["NGÂN HÀNG THẾ GIỚI MUA:", "▲  ●  ■"], 1.5))],
    [4, () => D3(lop(WIDE(), [thay("grin", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "laugh")], ["BUÔN BÁN · VAY MƯỢN · ĐI XIN"], 2))],
  ] },
  { id: "S18", shots: [
    [0, () => D3(lop(BOARD(), [thay("smile")], ["1. MỸ"], 0.6))],
    [1, () => D3(lop(BOARD(), [thay("grin")], ["1. MỸ", "2. PAKISTAN"], 0.8), (t) => <Big t={t} at={0.6} text="TRẮNG TAY MÀ VỀ NHÌ" col="#3ddc84" y={230} size={90} />)],
    [2, () => D3(lop(CLASS(), [...allStu(undefined, "neutral", "shock")], ["1. MỸ", "2. PAKISTAN"]))],
  ] },
  { id: "S19", shots: [
    [0, () => D3(S("xuong", "day", [[0, 3.2, 9], [0, 1.6, -4], 46], [[3, 3, 7], [0, 1.6, -4], 42], [], { score: 1 }), (t) => <Place t={t} l1="HỘI THẢO GIÁO VIÊN" l2="10 đội · 2 ngày" />)],
    [1, () => D3(S("xuong", "day", ...fixed([0, 3.6, -1.5], [0, 3.6, -8.8], 40), [], { score: 2 }), (t) => <Big t={t} at={0.8} text="BẢNG XẾP HẠNG ĐẢO NGƯỢC" col="#f5c518" y={180} size={80} />)],
    [2, () => D3(S("xuong", "day", [[-6, 1.8, -0.5], [-10, 1, -4], 40], [[-5, 1.7, -1.5], [-10, 1, -4], 36], [], { score: 2 }), (t) => <Big t={t} at={0.4} text="TỰ MÃN" col="#ff6a6a" y={220} size={110} />)],
    [3, () => D3(S("xuong", "day", [[6, 1.8, 5.5], [10, 1, 2], 40], [[5, 1.7, 4.5], [10, 1, 2], 36], [], { score: 2 }), (t) => <Big t={t} at={0.4} text="CHỊU LẮNG NGHE" col="#3ddc84" y={220} size={110} />)],
  ] },
  { id: "S20", shots: [
    [0, () => D3(lop(FACE("trang5"), [...allStu("trang5", "nervous")]), (t) => <NameTag t={t} k="trang5" />)],
    [1, () => D3(lop(TEACH(), [thay("stern")]))],
    [2, () => D3(lop(FACE("hung5"), [...allStu("hung5", "dazed")]), (t) => <NameTag t={t} k="hung5" />)],
    [3, () => D3(lop(BOARD(), [thay("smile")], ["KHÔNG CÓ", "→ PHẢI SÁNG TẠO"], 1.5))],
  ] },
  { id: "S21", shots: [
    [0, () => D3(lop(FACE("linh5"), [...allStu("linh5", "grin")]), (t) => <NameTag t={t} k="linh5" />)],
    [1, () => D3(lop(TEACH(), [thay("stern")], ["SỨC MẠNH =", "ĐẶT LUẬT CHƠI"], 1.5))],
    [2, () => D3(S("plaza", "room", [[0, 3, 7.5], [0, 1.4, -3], 44], [[0, 2.6, 5.6], [0, 1.4, -3], 40], crowd(5, -3.6, -2.7, 1.8, 1, 5, "stern", 60)), (t) => <Place t={t} l1="KHÁCH SẠN PLAZA · NEW YORK" l2="22/9/1985 · 5 nước lớn" />)],
    [3, () => D3(S("plaza", "room", [[2.5, 2, 2], [0, 1.3, -1], 38], [[1.5, 1.9, 1.6], [0, 1.3, -1], 34], crowd(5, -3.6, -2.7, 1.8, 1, 5, "worried", 60)), (t) => <Big t={t} at={0.5} text="ĐỒNG YÊN TĂNG VỌT" col="#ff6a6a" y={230} size={96} />)],
    [4, () => D3(lop(BOARD(), [thay("smile")], ["CÁCH NHÌN 1:", "NHẬT BỊ KÉO VÀO LUẬT CHƠI"], 1.5))],
    [5, () => D3(lop(BOARD(), [thay("smile")], ["CÁCH NHÌN 2:", "BONG BÓNG + CHÍNH SÁCH TRONG NƯỚC"], 1.5))],
    [6, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "neutral")], ["HAI CÁCH NHÌN", "TỰ CÂN NHẮC"], 1.2))],
  ] },
  { id: "S22", shots: [
    [0, () => D3(lop(TEACH(), [thay("smile")], ["NGHÈO → MỘT KHỐI?"], 1.2))],
    [1, () => D3(S("thao", "morning", [[-16, 4, 14], [2, 3, -10], 42], [[-6, 4, 12], [2, 3, -10], 40], []), (t) => <Place t={t} l1="THẢO NGUYÊN MÔNG CỔ" l2="Thế kỷ 13" />)],
    [2, () => D3(S("thao", "morning", [[8, 7, 6], [0, 6, -16], 40], [[5, 7, 3], [0, 6, -16], 36], [C("c9", [0, 5.35, -16], P("stern", { phase: 0.3 }))]), (t) => <Big t={t} at={0.8} text="THÀNH CÁT TƯ HÃN" col="#f5c518" y={220} size={96} />)],
  ] },
  { id: "S23", shots: [
    [0, () => D3(lop(FACE("linh5"), [...allStu("linh5", "grin")]), (t) => <NameTag t={t} k="linh5" />)],
    [1, () => D3(lop(BOARD(), [thay("stern")], ["GIẢ ĐỊNH"], 0.8), (t) => <Small text="Giả định đọc trên mạng – không phải dự báo" />)],
    [3, () => D3(lop(BOARD(), [thay("smile")], ["GIẢ ĐỊNH 1", "ĐỨC · NHẬT TRỖI DẬY TRỞ LẠI?"], 1.5), (t) => <Small text="Giả định đọc trên mạng – không phải dự báo" />)],
    [4, () => D3(lop(BOARD(), [thay("smile")], ["GIẢ ĐỊNH 2", "MỸ · TRUNG QUỐC KHÓ GIỮ ĐÀ?"], 1.5), (t) => <Small text="Giả định đọc trên mạng – không phải dự báo" />)],
    [5, () => D3(lop(BOARD(), [thay("smile")], ["GIẢ ĐỊNH 3", "TRIỀU TIÊN MỞ CỬA → BỨT LÊN?"], 1.5), (t) => <Small text="Giả định đọc trên mạng – không phải dự báo" />)],
    [6, () => D3(lop(TEACH(), [thay("stern")], ["VIỆN TRỢ → PHỤ THUỘC?"], 1.2), (t) => <Small text="Giả định đọc trên mạng – không phải dự báo" />)],
  ] },
  { id: "S24", shots: [
    [0, () => D3(lop(FACE("vy5"), [...allStu("vy5", "stern")], ["GIẢ ĐỊNH  |  PHẢN BIỆN"]), (t) => <NameTag t={t} k="vy5" />)],
    [1, () => D3(lop(BOARD(), [thay("smile")], ["GIẢ ĐỊNH  |  PHẢN BIỆN", "Mỹ dẫn đầu công nghệ", "Trung Quốc: công xưởng thế giới", "Đức, Nhật già đi nhanh"], 3))],
    [3, () => D3(lop(TEACH(), [thay("smile")], ["ĐẶT CÂU HỎI,", "ĐỪNG TIN NGAY"], 1.2))],
    [4, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "neutral")], ["THỜI GIAN SẼ CHẤM"], 1.2))],
  ] },
  { id: "S25", shots: [
    [0, () => CD((t) => <TimelineCard t={t} />)],
  ] },
  { id: "S26", shots: [
    [0, () => D3(lop(FACE("phu5"), [...allStu("phu5", "grin")]), (t) => <NameTag t={t} k="phu5" />)],
    [1, () => D3(lop(BOARD(), [thay("smile")], ["TRƯỚC KHI MUA CỔ PHIẾU"], 1))],
    [2, () => D3(lop(BOARD(), [thay("smile")], ["1. LÃNH ĐẠO CÒN ĐÓI KHÁT?"], 1))],
    [3, () => D3(lop(BOARD(), [thay("smile")], ["1. LÃNH ĐẠO CÒN ĐÓI KHÁT?", "2. CHỊU ĐỔI KHI THỊ TRƯỜNG ĐỔI?"], 1))],
    [4, () => D3(lop(BOARD(), [thay("smile")], ["1. LÃNH ĐẠO CÒN ĐÓI KHÁT?", "2. CHỊU ĐỔI KHI THỊ TRƯỜNG ĐỔI?", "3. CÙNG MỘT PHÍA?"], 1))],
    [5, () => D3(lop(TEACH(), [thay("stern")], ["TO MÀ MẤT CẢ 3", "= CÁI BÓNG QUÁ KHỨ"], 1.4))],
  ] },
  { id: "S27", shots: [
    [0, () => D3(lop(WIDE(), [thay("smile", true, [-0.5, 0, -1.2]), ...allStu(undefined, "neutral", "smile")], ["BÀI TẬP: CHẤM GIA ĐÌNH", "THANG 10 ĐIỂM"], 2, "golden"))],
    [1, () => D3(lop(FACE("phu5"), [...allStu("phu5", "nervous")], [], 0, "golden"), (t) => <NameTag t={t} k="phu5" />)],
    [2, () => D3(lop(TEACH(), [thay("laugh")], [], 0, "golden"))],
    [3, () => D3(lop(BOARD(), [thay("stern")], ["MỘT CÁCH NHÌN,", "KHÔNG PHẢI ĐỊNH LUẬT"], 1.5, "golden"))],
    [4, () => D3(lop(CLASS(), [...allStu(undefined, "neutral", "smile")], ["ĐẶT CÂU HỎI,", "ĐỪNG PHÁN CHẮC"], 0, "golden"))],
  ] },
  { id: "S28", shots: [
    [0, () => CD((t) => <CtaLtc t={t} />)],
  ] },
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
export const LTC5_FRAMES = TOTAL_F;
export const Ltc5Video: React.FC = () => {
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
        {audio ? <Audio src={staticFile("ltc5/voice.wav")} /> : null}
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
