// Video kênh chính "Vì sao thật tệ khi xếp hàng mua vàng ở đỉnh?" – kể chuyện anh Tân Mông To. Khung 1920x1080, 30 fps.
// Mỗi câu thoại có mốc thời gian thật (timing.json do giọng Huy70_HaiDang30 đọc) → cắt cảnh đúng câu, phụ đề đúng chữ.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, staticFile, delayRender, continueRender, Audio, getInputProps } from "remotion";
import { Stage, Shot3D, Run, SetKey, Cast, V } from "./stage";
import { Pose, Acc } from "./cast2";
import { Expr } from "../pho/toon";
import { GOLD_X, XECU_X, HOME_X } from "./sets";
import { TIMING, FPS, TOTAL_F, TAIL, sc, subText, BAD, GOOD, RING_M, SJC_D, RING_26, SJC_NOW, WORLD, VNI_26 } from "./data";
import { F, sm, PhoneCard, ChartCard, PaperCard, SideText, ChatCard, TvCard, TitleCard, NewsCard, LessonCard, SplitCard, SavingsCard, LastBuyerCard, CtaCard, EndCard, Bubble, LocTag, LiveHud, BigText, ClockTag, Vignette, Bg } from "./cards";

// ---------- pose helpers ----------
const bl = (t: number, k = 71) => Math.floor(t * 30) % k < 4;
type PO = Omit<Pose, "expr"> & { anim?: boolean };
const P = (expr: Expr, o: PO = {}) => (t: number): Pose => { const { anim, ...r } = o; return { expr, blink: expr === "laugh" || expr === "cry" || expr === "sleepy" ? false : bl(t + (r.phase ?? 0) * 3), ...r, ...(anim ? { t: Math.round(t * 15) / 15 } : {}) }; };
const seq = (pairs: [number, Expr][], o: PO = {}) => (t: number): Pose => { let e = pairs[0][1]; for (const [at, x] of pairs) if (t >= at) e = x; return P(e, o)(t); };
const walk = (expr: Expr, o: PO = {}) => (t: number): Pose => ({ ...P(expr, o)(t), mode: "stroll", phase: (t * 1.1) % 1 });
const C = (a: string, p: V, pose: Cast["pose"], to?: V): Cast => ({ a, p, pose, to });
const S = (set: SetKey, light: Shot3D["light"], from: [V, V, number], to: [V, V, number], cast: Cast[], x: Partial<Shot3D> = {}): Shot3D => ({ set, light, from, to, cast, ...x });

// ---------- recurring blocking ----------
const TAN_DESK: V = [-0.2, 0.45, -0.66];
const tanDesk = (e: Expr | ((t: number) => Pose), acc: Acc[] = ["headset"], o: PO = {}) => C("tan", TAN_DESK, typeof e === "string" ? P(e, { mode: "sit", acc, ...o }) : e);
const qx = (i: number) => GOLD_X + 1.4 + i * 1.15;
const RAINACC: Acc[][] = [["raincoat"], ["umbrella"], [], ["raincoat"], ["umbrella"], ["raincoat"]];
const UMB = ["#2b4f8a", "#b3263a", "#2f8a52", "#6b4fa0", "#d08a2a"];
const queue = (n = 24, from = 0, e: Expr = "neutral", sitEvery = 5): Cast[] => Array.from({ length: n }, (_, k) => { const i = from + k, sit = i % sitEvery === 2, acc = RAINACC[i % 6];
  return C("c" + i, [qx(i), sit ? 0.48 : 0.15, sit ? 5.72 : 5.25 + (i % 2) * 0.25], P(sit ? (i % 3 ? "sleepy" : e) : (i % 4 === 1 ? "worried" : e), { mode: sit ? "sit" : "stand", acc: sit ? [...acc.filter((a) => a !== "umbrella"), ...(i % 3 ? ["zzz" as Acc] : [])] : acc, umb: UMB[i % 5], anim: sit && i % 3 !== 0, phase: i * 0.37 })); });
const TQ: V = [qx(24) + 0.6, 0.15, 5.35];
const tanQ = (e: Expr | ((t: number) => Pose), acc: Acc[] = ["umbrella", "cup"]) => C("tan", TQ, typeof e === "string" ? P(e, { acc, umb: "#2b2d38", anim: true }) : e);
const ROOMW: [V, V, number] = [[-2.6, 2.3, 2.9], [0.2, 1.0, -1.2], 50];
const MEP: V = [-30, 0.48, 5.78]; // mẹ ngồi bán rau (phố huyện, ánh chiều)
const me = (e: Expr, acc: Acc[] = ["nonla"]) => C("me", MEP, P(e, { mode: "sit", acc }));
const meCam = (z0 = 2.2, z1 = 3.1): [[V, V, number], [V, V, number]] => [[[-32.5, 1.6, z0], [-30, 1.25, 5.85], 40], [[-31.6, 1.45, z1], [-30, 1.25, 5.85], 34]];
const LAKE_T: V = [-6.4, 0.56, 12.62], LAKE_N: V = [-5.6, 0.56, 12.62];
const BED1: V = [1.56, 0.4, 0.9], BED_A: V = [1.56, 0.4, 0.25], BED_B: V = [1.56, 0.4, 1.65];

// ---------- plan ----------
type Seg = { k: "3d"; s: Shot3D; ov?: (t: number, d: number) => React.ReactNode } | { k: "card"; r: (t: number, d: number) => React.ReactNode };
const D3 = (s: Shot3D, ov?: (t: number, d: number) => React.ReactNode): Seg => ({ k: "3d", s, ov });
const CD = (r: (t: number, d: number) => React.ReactNode): Seg => ({ k: "card", r });
/** time (s) of sentence j in scene id, relative to a reference start */
const rel = (id: string, j: number, ref: number) => sc(id).sens[Math.min(j, sc(id).sens.length - 1)].a - ref;

type Plan = { id: string; shots: [number, (a: number) => Seg][] };
const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => D3(S("room", "room", ROOMW, [[-1.3, 1.6, 1.7], [0, 1.05, -1.1], 42], [tanDesk("laugh")], { chat: "calm" }), (t) => <><ClockTag t={t} text="21:00" /><LiveHud t={t} viewers={2134} /></>)],
    [2, () => D3(S("room", "room", [[0.4, 1.4, 0.95], [-0.2, 1.27, -0.66], 38], [[0.3, 1.37, 0.72], [-0.2, 1.27, -0.66], 34], [tanDesk(seq([[0, "grin"], [0.9, "neutral"]], { mode: "sit", acc: ["headset", "phone", "glow"] }))], { chat: "calm" }), (t) => <LiveHud t={t} viewers={2141} />)],
    [3, () => CD((t) => <PhoneCard t={t} time="21:03" date="Thứ Sáu, 13 tháng 11" notifs={[{ app: "Tin vàng", col: "#d59a1e", title: "Giá vàng hôm nay 13/11", body: "Vàng miếng SJC giảm 1 triệu đồng/lượng, còn 138 triệu.", at: 0.5 }]} quote={["GIÁ VÀNG", "LẠI GIẢM"]} qAt={1.3} />)],
    [4, () => D3(S("room", "room", [[0.12, 1.37, 0.62], [-0.2, 1.34, -0.66], 30], [[0.08, 1.35, 0.42], [-0.2, 1.34, -0.66], 26], [tanDesk("shock", ["headset", "phone", "glow"])], { chat: "fast", shake: 1.2 }))],
    [5, () => D3(S("room", "room", [[0.62, 1.2, -1.42], [0.78, 1.2, -2.2], 44], [[0.72, 1.2, -1.62], [0.78, 1.2, -2.2], 40], [], { chat: "fast" }))],
    [6, () => D3(S("room", "room", [[0.95, 1.55, 1.6], [-0.2, 1.22, -0.66], 40], [[0.75, 1.5, 1.3], [-0.2, 1.22, -0.66], 36], [tanDesk("worried", ["headset", "sweat"], { anim: true })], { chat: "fast" }), (t) => <Vignette k={sm(t / 1)} />)],
    [7, () => D3(S("room", "roomdim", [[1.4, 0.6, 3.5], [2.2, 0.2, 1.9], 42], [[1.95, 0.4, 2.8], [2.2, 0.18, 1.9], 36], [], { chat: "fast", ease: "out" }), (t) => <BigText t={t} at={1.4} text="5 LƯỢNG VÀNG" col="#ffcf3a" y={700} size={110} />)],
    [8, () => CD((t) => <PaperCard t={t} kind="receipt" hue="red" title="SỔ TIẾT KIỆM" sub="Chủ sổ: Mẹ – Nam Định" lines={[{ text: "Số dư: 120.000.000 đ", at: 0.6, big: true }, { text: "Tiền bán rau, gom từng đồng lẻ", at: 1.4 }]} stamp={{ text: "ĐÃ RÚT HẾT", at: 2.6 }} side={<SideText t={t} at={1.0} l1="CẢ ĐỜI" l2="CỦA MẸ" />} />)],
  ] },
  { id: "S02", shots: [[0, () => CD((t) => <TitleCard t={t} kicker="VÌ SAO THẬT TỆ KHI" l1="XẾP HÀNG MUA VÀNG" l2="Ở ĐỈNH?" sub="Chuyện anh Tân Mông To" />)]] },
  { id: "S03", shots: [
    [0, () => D3(S("streetday", "day", [[HOME_X - 10, 7, -1], [HOME_X, 1.8, 5.4], 50], [[HOME_X - 3, 1.7, 1.6], [HOME_X, 1.35, 5.4], 42], [C("tan", [HOME_X, 0.15, 5.4], P("grin", { wave: 0.8 }))]))],
    [1, () => D3(S("streetday", "morning", [[HOME_X + 1.9, 1.5, 1.9], [HOME_X + 3.4, 1.25, 5.5], 46], [[HOME_X + 2.3, 1.45, 2.5], [HOME_X + 3.4, 1.25, 5.5], 42], [C("c2", [HOME_X + 2.5, 0.15, 5.6], P("laugh", { wave: 0.9, anim: true })), C("tan", [HOME_X + 6.0, 0.15, 5.4], walk("grin", { side: 1 }), [HOME_X + 4.2, 0.15, 5.4])]), (t) => <><Bubble t={t} at={0.5} x={1040} y={150} w={700} tail="r" text="Tân Mông To ơi, xuống uống trà!" /><Bubble t={t} at={2.6} x={200} y={330} w={520} text="Em xuống ngay đây bác!" /></>)],
    [2, () => D3(S("streetday", "day", [[HOME_X - 1.2, 1.45, 2.6], [HOME_X, 1.35, 5.4], 38], [[HOME_X - 0.9, 1.4, 3.0], [HOME_X, 1.35, 5.4], 34], [C("tan", [HOME_X, 0.15, 5.4], P("laugh")), C("c3", [HOME_X - 1.4, 0.15, 5.7], P("laugh")), C("c7", [HOME_X + 1.5, 0.15, 5.8], P("grin"))]), (t) => <BigText t={t} at={0.9} text="“TÂN MÔNG TO”" col="#ffcf3a" y={120} />)],
    [3, () => D3(S("room", "roomdim", [[-0.6, 1.7, 3.2], [1.56, 1.1, 0.9], 44], [[-0.1, 1.5, 2.7], [1.56, 1.1, 0.9], 40], [C("tan", BED1, P("sleepy", { mode: "sit", acc: ["zzz"], anim: true }))], { chat: "off", game: false }))],
    [4, () => D3(S("room", "room", [[0.35, 1.4, 1.1], [-0.2, 1.27, -0.66], 38], [[0.28, 1.37, 0.85], [-0.2, 1.27, -0.66], 34], [tanDesk(P("laugh", { mode: "sit", acc: ["headset"], wave: 0.6 }))], { chat: "calm" }), (t) => <><LiveHud t={t} viewers={1980} /><Bubble t={t} at={0.9} x={1080} y={180} w={700} text="Anh em ơi, lương anh có 7 triệu thôi!" /></>)],
    [5, () => D3(S("streetday", "morning", [[HOME_X - 2.5, 1.4, 2.2], [HOME_X + 0.6, 1.0, 5.3], 42], [[HOME_X - 1.6, 1.3, 2.9], [HOME_X + 0.6, 1.0, 5.3], 38], [C("tan", [HOME_X - 0.2, 0.15, 5.3], P("smile_closed", { acc: ["cup"], anim: true }))]), (t) => <BigText t={t} at={rel("S03", 6, sc("S03").sens[5].a) - 0.1} text="MÌ TÔM · XE CŨ 8 NĂM" col="#fff" y={130} size={90} />)],
    [7, () => CD((t) => <SavingsCard t={t} />)],
    [8, () => CD((t) => <PaperCard t={t} kind="receipt" hue="navy" title="HỢP ĐỒNG HỘI VIÊN" sub="Phòng tập thể hình · gói 3 năm" lines={[{ text: "Giá trị: 36.000.000 đ", at: 0.5, big: true }, { text: "Trả góp: 3.000.000 đ/tháng × 12", at: 1.2 }, { text: "Quyền lợi: “tập trọn đời”", at: 2.0, col: "#b3131f" }]} stamp={{ text: "ĐÃ KÝ", at: 2.6, col: "#1f4e8a" }} side={<SideText t={t} at={1.6} l1="“TẬP" l2="TRỌN ĐỜI”" c2="#f5c518" />} />)],
    [9, () => D3(S("room", "room", [[-1.2, 1.5, 2.4], [0.6, 1.0, -0.6], 44], [[-0.7, 1.4, 1.9], [0.6, 1.0, -0.6], 40], [tanDesk("nervous", ["headset", "sweat"], { anim: true }), C("ngan", [1.0, 0, 0.1], P("stern"))], { chat: "calm" }))],
    [10, () => CD((t) => <DreamCard t={t} />)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(S("streetday", "golden", [[-36, 3.8, 0.5], [-30, 1.4, 5.85], 46], meCam(2.0)[0], [me("smile_closed")]), (t) => <LocTag t={t} l1="NAM ĐỊNH" l2="Quê mẹ anh Tân" />)],
    [1, () => D3(S("streetday", "golden", ...meCam(2.2, 3.0), [me("smile")]))],
    [2, () => CD((t) => <PaperCard t={t} kind="receipt" hue="warm" title="SỔ TIẾT KIỆM" sub="Chủ sổ: Mẹ" lines={[{ text: "Số dư: 120.000.000 đ", at: 0.6, big: true, col: "#1d6b3a" }, { text: "Gom từng đồng lẻ trong mấy chục năm", at: 1.6 }]} side={<SideText t={t} at={1.2} l1="ĐỂ DÀNH" l2="LÚC ỐM ĐAU" c2="#f5c518" />} />)],
    [3, () => D3(S("streetday", "golden", [[-31.4, 1.35, 3.6], [-30, 1.35, 5.85], 32], [[-31.1, 1.3, 4.1], [-30, 1.35, 5.85], 28], [me("smile_closed")]), (t) => <Bubble t={t} at={0.5} x={1080} y={200} w={720} text="Tiền này để dành lúc ốm đau, không phiền đến con." />)],
  ] },
  { id: "S05", shots: [
    [0, () => D3(S("streetday", "day", [[GOLD_X + 14, 2.8, 0.5], [GOLD_X + 8, 1.2, 5.9], 46], [[GOLD_X + 11, 1.9, 1.6], [GOLD_X + 7, 1.15, 5.9], 40], teaStall()))],
    [1, () => CD((t, d) => <ChartCard t={t} d={d} title="Giá vàng nhẫn SJC 99,99" sub="Giá bán ra cuối tháng · 1/2025 → vía Thần Tài 26/2/2026" data={RING_M} unit="triệu đồng/lượng" mode="up" marks={[{ i: 0, label: "88 triệu", col: "#8fd3ff", up: false }, { i: RING_M.length - 1, label: "184 triệu ×2", col: "#f5c518" }]} src="Nguồn: SJC (dữ liệu WiData), giá bán ra, nghìn đồng/lượng quy đổi triệu đồng" />)],
    [2, () => D3(S("streetday", "day", [[GOLD_X + 9.5, 1.5, 1.6], [GOLD_X + 8.5, 1.1, 5.6], 48], [[GOLD_X + 7.6, 1.45, 2.2], [GOLD_X + 6.6, 1.1, 5.6], 44], [...teaStall("grin", false), C("tan", [GOLD_X + 14, 0.15, 5.2], walk("smile", { side: 1 }), [GOLD_X + 6.3, 0.15, 5.2])], { ease: "lin" }))],
    [3, () => D3(S("streetday", "day", [[GOLD_X + 5.9, 1.4, 3.3], [GOLD_X + 5.7, 1.2, 5.6], 38], [[GOLD_X + 5.8, 1.38, 3.7], [GOLD_X + 5.7, 1.2, 5.6], 34], [...teaStall("laugh", false), C("tan", [GOLD_X + 6.3, 0.15, 5.45], P("smile", { side: 1 }))], { shake: 0.3 }), (t) => <Bubble t={t} at={0.5} x={1040} y={150} w={720} tail="r" text="Tao mua từ đầu năm, giờ lãi gấp đôi rồi đấy!" />)],
    [4, () => D3(S("streetday", "day", [[GOLD_X + 9.4, 1.45, 2.9], [GOLD_X + 8.6, 1.15, 5.6], 42], [[GOLD_X + 9.0, 1.4, 3.4], [GOLD_X + 8.6, 1.15, 5.6], 38], [...teaStall("smile", false), C("c9", [GOLD_X + 7.45, 0.15, 5.25], P("grin", { acc: ["xoi"] })), C("c14", [GOLD_X + 9.9, 0.15, 5.3], P("smile", { side: -1 }))]), (t) => <Bubble t={t} at={0.8} x={620} y={110} w={760} text="Vàng thì cứ mua, có bao giờ mất đâu!" />)],
    [5, () => D3(S("streetday", "day", [[GOLD_X + 6.5, 1.4, 3.7], [GOLD_X + 6.3, 1.3, 5.45], 34], [[GOLD_X + 6.45, 1.4, 4.0], [GOLD_X + 6.3, 1.32, 5.45], 30], [C("tan", [GOLD_X + 6.3, 0.15, 5.45], P("nervous", { anim: true, acc: ["sweat"] }))]), (t) => <Bubble t={t} at={0.5} x={1060} y={170} w={640} kind="whisper" text="Giờ mua… còn kịp không cô?" />)],
    [6, () => D3(S("streetday", "day", [[GOLD_X + 7, 2.6, 1.2], [GOLD_X + 7, 1.0, 5.9], 48], [[GOLD_X + 7, 2.2, 1.7], [GOLD_X + 7, 1.0, 5.9], 44], [...teaStall("laugh", false), C("tan", [GOLD_X + 6.3, 0.15, 5.45], P("shock")), C("c9", [GOLD_X + 7.45, 0.15, 5.25], P("laugh", { acc: ["xoi"] }))], { shake: 1.0 }), (t) => <Meme t={t} at={0.5} top="CẢ QUÁN:" bot="“KỊP!!!”" small y={250} />)],
    [7, () => D3(S("streetday", "day", [[GOLD_X + 7, 3.2, 0.8], [GOLD_X + 7, 1.0, 5.9], 48], [[GOLD_X + 7, 2.2, 1.6], [GOLD_X + 7, 1.0, 5.9], 44], [...teaStall("grin", false), C("tan", [GOLD_X + 6.3, 0.15, 5.45], P("smile"))]), (t) => <BigText t={t} at={0.6} text="VÀNG LÚC NÀO CŨNG GIỮ GIÁ" col="#ffcf3a" y={110} size={96} />)],
    [8, () => D3(S("streetday", "day", [[GOLD_X + 6.0, 1.25, 3.4], [GOLD_X + 6.3, 1.3, 5.45], 38], [[GOLD_X + 6.2, 1.3, 4.2], [GOLD_X + 6.3, 1.35, 5.45], 30], [C("tan", [GOLD_X + 6.3, 0.15, 5.45], seq([[0, "smile"], [1.4, "nervous"]]))], { shake: 0.6 }))],
  ] },
  { id: "S06", shots: [
    [0, () => D3(S("room", "roomdim", [[0.9, 1.4, 2.0], [0.6, 1.0, -0.2], 42], [[0.8, 1.35, 1.5], [0.6, 1.0, -0.2], 38], [C("tan", [0.6, 0, -0.2], P("nervous", { acc: ["phone", "glow"] }))], { chat: "off", game: false }), (t) => <ClockTag t={t} text="Mùng 8 Tết" />)],
    [1, () => D3(S("room", "roomdim", [[0.8, 1.45, 1.4], [0.6, 1.32, -0.2], 40], [[0.75, 1.42, 1.15], [0.6, 1.32, -0.2], 36], [C("tan", [0.6, 0, -0.2], P("nervous", { acc: ["phone", "glow", "sweat"], anim: true }))], { chat: "off", game: false, shake: 0.5 }), (t) => <Bubble t={t} at={0.3} x={1080} y={200} w={700} text="Mẹ ơi… con cần ít tiền sửa lại căn gác." />)],
    [2, () => D3(S("streetday", "golden", ...meCam(2.6, 3.3), [me("smile_closed", ["nonla", "phone"])]))],
    [3, () => CD((t) => <PhoneCard t={t} hue="warm" time="07:42" date="Mùng 9 tháng Giêng" notifs={[{ app: "Ngân hàng", col: "#1d6b3a", title: "Biến động số dư", body: "+120.000.000 đ · Người chuyển: MẸ", at: 0.5 }, { app: "Tin nhắn", col: "#2f6fd1", title: "Mẹ", body: "Con cứ cầm mà lo, khi nào có thì trả mẹ.", at: 2.6 }]} quote={["MẸ KHÔNG HỎI", "MỘT CÂU NÀO"]} qAt={1.4} />)],
  ] },
  { id: "S07", shots: [
    [0, () => D3(S("room", "room", ROOMW, [[-1.6, 1.8, 2.1], [0, 1.05, -1.1], 44], [tanDesk(P("smile", { mode: "sit", acc: ["headset"], prop: "type" }))], { chat: "calm" }), (t) => <><ClockTag t={t} text="Đêm mùng 9" /><LiveHud t={t} viewers={2050} /></>)],
    [1, () => D3(S("room", "room", [[0.6, 1.2, -1.4], [0.78, 1.2, -2.2], 44], [[0.7, 1.2, -1.58], [0.78, 1.2, -2.2], 40], [], { chat: "calm" }), (t) => <Bubble t={t} at={0.3} x={560} y={160} w={800} text="Mai anh nghỉ live một buổi nhé anh em!" />)],
    [2, () => D3(S("street", "night", [[HOME_X - 4, 1.4, 2.0], [HOME_X + 1, 1.0, 5.2], 44], [[HOME_X + 2, 1.4, 2.0], [HOME_X + 5, 1.0, 5.2], 44], [C("tan", [HOME_X + 1.3 + PUSH[0], 0.15, 5.0 + PUSH[1]], pushPose("nervous"), [HOME_X + 6.3 + PUSH[0], 0.15, 5.0 + PUSH[1]]), C("bike", [HOME_X + 1.3, 0.15, 5.0], () => P("neutral")(0), [HOME_X + 6.3, 0.15, 5.0])], { ease: "lin" }), (t) => <ClockTag t={t} text="03:00" />)],
    [3, () => CD((t) => <NoteCard t={t} />)],
  ] },
  { id: "S08", shots: [
    [0, () => D3(S("street", "night", [[qx(10), 14, -6], [qx(8), 1.5, 5.3], 50], [[qx(6), 4.5, -1], [qx(6), 1.4, 5.3], 46], queue(), { rain: true }), (t) => <LocTag t={t} l1="PHỐ TRẦN NHÂN TÔNG" l2="Hà Nội · 4 giờ sáng · mưa phùn" d={4.5} />)],
    [1, () => D3(S("street", "night", [[qx(4), 1.35, 3.2], [qx(4), 1.3, 5.4], 40], [[qx(4.6), 1.35, 3.5], [qx(4.6), 1.3, 5.4], 36], queue(), { rain: true, shake: 0.4 }))],
    [2, () => D3(S("street", "night", [[GOLD_X - 1, 1.6, 1.8], [GOLD_X + 3, 1.3, 5.4], 46], [[qx(18), 1.6, 1.8], [qx(22), 1.3, 5.4], 46], queue(), { rain: true, ease: "lin" }))],
    [3, () => D3(S("street", "night", [[qx(11), 1.35, 3.6], [qx(12), 1.15, 5.8], 40], [[qx(12.5), 1.35, 3.9], [qx(12.5), 1.15, 5.8], 38], queue(), { rain: true }))],
    [4, () => D3(S("street", "night", [[-19.5, 2.8, 7.6], [-28, 0.8, 0.5], 48], [[-21, 2.2, 6.8], [-28, 0.9, 0.5], 46], [C("c30", [-27.5, 0, 3.4], P("stern")), C("c31", [-25.9, 0, 3.45], P("shock"))], { rain: true, jam: true }), (t) => <BigText t={t} at={0.6} text="TẮC CỨNG!" col="#ff4d5e" y={110} size={110} />)],
    [5, () => D3(S("street", "night", [[-26.7, 1.45, 6.4], [-26.7, 1.35, 3.4], 40], [[-26.7, 1.42, 5.9], [-26.7, 1.35, 3.4], 36], [C("c30", [-27.5, 0, 3.4], seq([[0, "stern"], [1.2, "shock"]])), C("c31", [-25.9, 0, 3.45], seq([[0, "shock"], [0.9, "stern"]]))], { rain: true, jam: true, shake: 1.0 }), (t) => <><Bubble t={t} at={0.2} x={180} y={150} w={620} text="Lùi xe ra! Ai cho ông đỗ đây?!" /><Bubble t={t} at={1.1} x={1100} y={190} w={620} tail="r" text="Đường nhà ông à?!" /></>)],
    [6, () => D3(S("villa", "night", [[-26, 10, -4], [0, 1, 0], 52], [[-15, 5, -2], [0, 1, 0], 48], [], { rain: true }), (t) => <LocTag t={t} l1="KHU BIỆT THỰ CIPUCHACHA" l2="dân mạng gọi vui: “làng chài”" d={4.5} />)],
    [7, () => D3(S("villa", "night", [[-9.5, 1.6, 4.2], [-9, 0.9, 0.3], 42], [[-4, 1.6, 4.2], [-3.5, 0.9, 0.3], 42], [C("boat", [-10, 0.42, 0.3], () => P("neutral")(0), [-4, 0.42, 0.3]), C("vest", [-10, 0.52, 0.3], P("smug", { mode: "sit", acc: ["raincoat"] }), [-4, 0.52, 0.3])], { rain: true, ease: "lin" }), (t) => <BigText t={t} at={0.8} text="ĐẠI GIA CHÈO THUYỀN ĐI MUA VÀNG" col="#ffcf3a" y={110} size={84} />)],
    [8, () => D3(S("street", "night", [[qx(15), 1.45, 2.9], [qx(16), 1.25, 5.3], 42], [[qx(16.5), 1.45, 3.1], [qx(17.5), 1.25, 5.3], 40], [...queue(22), C("clerk", [qx(14.2), 0.15, 4.75], walk("smile", { acc: ["ticket"], num: "101" }), [qx(18.4), 0.15, 4.75])], { rain: true, ease: "lin" }), (t) => <BigText t={t} at={0.8} text="PHÁT SỐ THỨ TỰ" col="#ffcf3a" y={110} size={96} />)],
    [9, () => D3(S("street", "night", ...SEATCAM, seatCast("smile", "neutral"), { rain: true }), (t) => <BigText t={t} at={1.0} text="SỐ 102" col="#fff" y={110} size={110} />)],
    [10, () => D3(S("street", "night", [[GOLD_X + 3.4, 1.5, 2.4], [GOLD_X + 1.4, 1.3, 5.3], 42], [[GOLD_X + 3.0, 1.45, 2.9], [GOLD_X + 1.2, 1.3, 5.3], 38], [...queue(4), C("clerk", [GOLD_X + 0.3, 0.15, 5.1], P("grin", { acc: ["mega"], anim: true }))], { rain: true, shake: 0.4 }), (t) => <Bubble t={t} at={0.5} x={1100} y={150} w={600} tail="r" text="Mời số 87… số 87!" />)],
    [11, () => D3(S("street", "night", ...SEATCAM, seatCast("smile", "grin"), { rain: true }), (t) => <Bubble t={t} at={0.6} x={220} y={170} w={560} text="Cháu mua mấy chỉ?" />)],
    [12, () => D3(S("street", "night", ...SEATCAM, seatCast("nervous", "smile"), { rain: true }), (t) => <Bubble t={t} at={0.5} x={1100} y={170} w={620} tail="r" kind="whisper" text="Dạ… cháu mua 5 lượng ạ." />)],
    [13, () => D3(S("street", "night", [[qx(23) + 0.5, 1.2, 3.9], [qx(23), 1.12, 5.72], 30], [[qx(23) + 0.4, 1.2, 4.2], [qx(23), 1.12, 5.72], 26], [C("c31", [qx(23), 0.48, 5.72], P("shock", { mode: "sit", acc: ["nonla"] }))], { rain: true, shake: 1.0 }), (t) => <Meme t={t} at={0.4} top="" bot="“GHÊ THẾ!”" small y={130} />)],
    [14, () => D3(S("street", "night", [[qx(22) + 1.6, 1.3, 3.2], [qx(22), 1.1, 5.72], 38], [[qx(22) + 1.0, 1.25, 3.7], [qx(22), 1.12, 5.72], 32], [...queue(22), C("tan", [qx(22), 0.48, 5.72], seq([[0, "smile"], [2.2, "grin"]], { mode: "sit", acc: ["cup"], anim: true })), C("c31", [qx(23), 0.48, 5.72], P("smile", { mode: "sit", acc: ["nonla"] }))], { rain: true }), (t, d) => <Bubble t={t} at={Math.min(2.4, d * 0.4)} x={1040} y={150} w={700} kind="think" text="Lên vài giá là đủ tiền xây nhà cho mẹ…" />)],
  ] },
  { id: "S09", shots: [
    [0, () => D3(S("street", "night", [[TQ[0] + 2, 2, 2], [qx(16), 1.2, 5.3], 46], [[qx(14), 22, -4], [qx(10), 0, 5.3], 54], queue(), { rain: true, ease: "out" }))],
    [1, () => D3(S("hue", "dawn", [[-34, 5, 34], [0, 3, 0], 50], [[-27, 3.5, 24], [0, 3, -2], 46], hueWalkers()), (t) => <LocTag t={t} l1="CẦU TRƯỜNG TIỀN" l2="Huế · trời còn tối" />)],
    [2, () => D3(S("bt", "morning", [[14, 2.2, 18], [0, 9, -14], 52], [[6, 2.0, 14], [0, 10, -14], 48], btCrowd()), (t) => <LocTag t={t} l1="CHỢ BẾN THÀNH" l2="TP. Hồ Chí Minh" />)],
    [3, () => D3(S("street", "night", [[qx(2), 1.5, 2.2], [qx(6), 1.3, 5.4], 44], [[qx(9), 1.5, 2.2], [qx(13), 1.3, 5.4], 44], queue(), { rain: true, ease: "lin" }), (t) => <BigText t={t} at={0.5} text="PHẢI CÓ VÀNG, KẺO LỠ!" col="#ffcf3a" y={110} size={110} />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(S("street", "night", [[TQ[0] - 1.2, 1.45, 2.4], [TQ[0] + 0.6, 1.3, 5.35], 44], [[TQ[0] - 0.6, 1.45, 2.8], [TQ[0] + 0.8, 1.3, 5.35], 40], [...queue(4, 20), tanQ("smile"), C("vest", [TQ[0] + 5, 0.15, 4.9], walk("smug"), [TQ[0] + 1.25, 0.15, 5.0])], { rain: true }))],
    [1, () => D3(S("street", "night", [[TQ[0] + 0.9, 1.4, 3.6], [TQ[0] + 1.25, 1.25, 5.0], 34], [[TQ[0] + 1.0, 1.35, 3.9], [TQ[0] + 1.25, 1.2, 5.0], 30], [C("vest", [TQ[0] + 1.25, 0.15, 5.0], P("smug", { acc: ["gembox"], anim: true })), tanQ("shock")], { rain: true }))],
    [2, () => D3(S("street", "night", [[TQ[0] + 0.6, 1.4, 3.0], [TQ[0] + 0.6, 1.3, 5.2], 38], [[TQ[0] + 0.6, 1.4, 3.3], [TQ[0] + 0.6, 1.3, 5.2], 35], [C("vest", [TQ[0] + 1.25, 0.15, 5.0], P("smug", { acc: ["gembox"], anim: true })), tanQ("smile")], { rain: true }), (t) => <><Bubble t={t} at={0.2} x={200} y={150} w={680} kind="whisper" text="Xếp hàng làm gì cho khổ…" />{t > rel("S10", 3, sc("S10").sens[2].a) && <Bubble t={t} at={rel("S10", 3, sc("S10").sens[2].a)} x={160} y={360} w={760} kind="whisper" text="Có giấy kiểm định của Mỹ đấy, để lâu còn lên giá hơn vàng!" />}</>)],
    [4, () => D3(S("street", "night", [[TQ[0] - 0.2, 1.45, 3.9], [TQ[0], 1.4, 5.35], 30], [[TQ[0] - 0.15, 1.45, 4.3], [TQ[0], 1.4, 5.35], 26], [tanQ(seq([[0, "smile"], [1.0, "nervous"]]), ["umbrella", "sweat"])], { rain: true, shake: 0.5 }))],
  ] },
  { id: "S11", shots: [
    [0, () => CD((t) => <TvCard t={t} qAt={rel("S11", 1, sc("S11").a) + 0.2} quote="“Mua vàng thì còn biết đường mà giữ, chứ đá quý với tờ giấy kiểm định nước ngoài, mình biết đâu mà lần.”" />)],
    [2, () => D3(S("street", "night", [[TQ[0] + 1.6, 1.4, 2.9], [TQ[0] + 0.6, 1.3, 5.2], 40], [[TQ[0] + 1.2, 1.4, 3.3], [TQ[0] + 0.6, 1.3, 5.2], 36], [tanQ(seq([[0, "stern"], [1.2, "smug"]])), C("vest", [TQ[0] + 1.25, 0.15, 5.0], walk("stern"), [TQ[0] + 6, 0.15, 4.6])], { rain: true }))],
    [3, () => D3(S("street", "night", [[TQ[0] + 1.6, 1.4, 3.0], [TQ[0], 1.3, 5.35], 40], [[qx(12), 16, -6], [qx(9), 0, 5.3], 56], queue(), { rain: true, ease: "sm" }), (t) => <><Vignette k={sm(t / 2) * 0.9} col="40,0,0" /><BigText t={t} at={rel("S11", 4, sc("S11").sens[3].a)} text="CÁI BẪY THẬT SỰ" col="#ff4d5e" y={120} size={120} /></>)],
  ] },
  { id: "S12", shots: [
    [0, () => D3(S("shop", "day", [[-2.2, 1.7, 3.6], [0, 1.2, -1], 46], [[-1.4, 1.55, 2.6], [0, 1.2, -1], 42], [C("tan", [0.5, 0, 0.55], P("grin", { acc: [] })), C("clerk", [0, 0, -1.4], P("smile"))]), (t) => <ClockTag t={t} text="08:00" />)],
    [1, () => D3(S("shop", "day", [[-4.6, 1.55, -0.45], [-1.5, 1.25, -0.45], 40], [[-4.2, 1.5, -0.45], [-1.5, 1.25, -0.45], 36], [C("tan", [-1.5, 0, 0.45], P("grin", { side: -1 })), C("clerk", [-1.5, 0, -1.4], P("smile", { side: 1 }))]), (t) => <Bubble t={t} at={0.5} x={220} y={150} w={560} text="Anh lấy mấy chỉ ạ?" />)],
    [2, () => D3(S("shop", "day", [[-4.6, 1.55, -0.45], [-1.5, 1.25, -0.45], 40], [[-4.2, 1.5, -0.45], [-1.5, 1.25, -0.45], 36], [C("tan", [-1.5, 0, 0.45], P("laugh", { side: -1 })), C("clerk", [-1.5, 0, -1.4], seq([[0, "smile"], [1.6, "shock"]], { side: 1 }))], { shake: 0.6 }), (t) => <><Bubble t={t} at={0.9} x={1100} y={150} w={600} tail="r" text="Cho anh… 5 lượng nhẫn!" /><Meme t={t} at={2.0} top="" bot="5 LƯỢNG?!" small y={420} /></>)],
    [3, () => D3(S("shop", "day", [[-3.1, 2.1, -0.7], [-3.2, 2.1, -2.9], 46], [[-3.15, 2.1, -1.0], [-3.2, 2.1, -2.9], 42], [], { board: "buy" }))],
    [4, () => CD((t) => <PaperCard t={t} kind="receipt" hue="warm" title="HOÁ ĐƠN BÁN HÀNG" sub="Ngày 26/02/2026 · vía Thần Tài" lines={[{ text: "Nhẫn tròn 9999 × 5 lượng", at: 0.2 }, { text: "Đơn giá: 184.000.000 đ", at: 0.5 }, { text: "THÀNH TIỀN: 920.000.000 đ", at: 0.9, big: true, under: true }]} stamp={{ text: "ĐÃ THANH TOÁN", at: 1.8, col: "#1d6b3a" }} />)],
    [5, () => CD((t) => <SplitCard t={t} title="920 triệu đến từ đâu?" total="920 triệu" parts={[{ label: "Tiết kiệm 10 năm", v: 600, col: "#2b9a5a", at: 0.3 }, { label: "Vay bạn bè", v: 200, col: "#e0832a", at: rel("S12", 6, sc("S12").sens[5].a) }, { label: "Sổ tiết kiệm của mẹ", v: 120, col: "#d8212f", at: rel("S12", 7, sc("S12").sens[5].a) }]} />)],
    [8, () => D3(S("shop", "day", [[0.2, 1.4, 2.6], [0.5, 1.3, 0.55], 38], [[0.3, 1.35, 2.1], [0.5, 1.3, 0.55], 32], [C("tan", [0.5, 0, 0.55], P("laugh", { acc: ["goldbag"] }))]))],
  ] },
  { id: "S13", shots: [
    [0, () => CD((t, d) => <ChartCard t={t} d={d} title="Vàng miếng SJC lập đỉnh" sub="Giá bán ra từng ngày · 10/2 → 2/3/2026" data={SJC_D.slice(0, 11)} unit="triệu đồng/lượng" mode="up" marks={[{ i: 8, label: "Ngày mua 184", col: "#8fd3ff", up: false }, { i: 10, label: "ĐỈNH 190,9", col: "#f5c518" }]} src="Nguồn: SJC (dữ liệu WiData), giá bán ra" />)],
    [2, () => D3(S("room", "room", [[0.4, 1.43, 1.25], [-0.2, 1.27, -0.66], 40], [[0.3, 1.39, 0.85], [-0.2, 1.27, -0.66], 34], [tanDesk(P("laugh", { mode: "sit", acc: ["headset"], wave: 0.9 }))], { chat: "boom" }), (t) => <><LiveHud t={t} viewers={5870} /><Bubble t={t} at={rel("S13", 3, sc("S13").sens[2].a)} x={1060} y={170} w={740} text="Lương anh 7 triệu, mà một tuần anh lãi mấy chục triệu!" /></>)],
    [4, () => D3(S("room", "room", [[0.6, 1.2, -1.38], [0.78, 1.2, -2.2], 44], [[0.74, 1.2, -1.64], [0.78, 1.2, -2.2], 38], [], { chat: "boom" }), (t) => <Bubble t={t} at={rel("S13", 5, sc("S13").sens[4].a)} x={600} y={140} w={760} text="Mai em đi mua có kịp không anh??" />)],
    [6, () => D3(S("room", "room", [[0.0, 1.35, 2.2], [1.0, 0.9, 0.6], 40], [[0.1, 1.3, 1.8], [1.0, 0.95, 0.6], 36], [C("tan", [0.9, 0, 0.4], P("smile_closed", { acc: ["ring"] })), C("ngan", BED_B, P("sleepy", { mode: "sit", acc: ["zzz"], anim: true }))], { chat: "off" }))],
    [7, () => D3(S("room", "room", [[0.95, 1.4, 1.8], [0.9, 1.3, 0.4], 36], [[0.92, 1.38, 1.5], [0.9, 1.3, 0.4], 32], [C("tan", [0.9, 0, 0.4], seq([[0, "neutral"], [1.0, "smug"]], { acc: [] }))], { chat: "off" }), (t) => <BigText t={t} at={rel("S13", 8, sc("S13").sens[7].a)} text="ĐỂ LÃI THÊM CHÚT NỮA ĐÃ…" col="#fff" y={130} size={96} />)],
  ] },
  { id: "S14", shots: [
    [0, () => D3(S("room", "room", [[0.4, 1.4, 1.0], [-0.2, 1.29, -0.66], 36], [[0.3, 1.37, 0.75], [-0.2, 1.29, -0.66], 32], [tanDesk("laugh")], { chat: "boom" }), (t) => <AbsoluteFill style={{ background: `rgba(30,30,40,${0.35 * sm(t / 1.5)})`, mixBlendMode: "saturation" } as React.CSSProperties} />)],
    [1, () => CD((t, d) => <LastBuyerCard t={t} d={d} />)],
    [2, () => D3(S("streetday", "day", [[GOLD_X + 9.0, 1.4, 3.7], [GOLD_X + 8.6, 1.25, 5.8], 34], [[GOLD_X + 8.8, 1.4, 4.0], [GOLD_X + 8.6, 1.25, 5.8], 30], teaStall("grin")), (t) => <Meme t={t} top="KHI CẢ CÔ BÁN XÔI" bot="CŨNG KHUYÊN MUA VÀNG" />)],
    [3, () => CD((t) => <TitleCard t={t} hue="navy" kicker="QUY LUẬT CŨ" l1="ĐỈNH GIÁ ĐẾN" l2="KHI AI CŨNG CHẮC CHẮN" />)],
  ] },
  { id: "S15", shots: [
    [0, () => CD((t, d) => <ChartCard t={t} d={d} title="Vàng miếng SJC trượt dốc" sub="Giá bán ra từng ngày · 10/2 → 25/3/2026" data={SJC_D} unit="triệu đồng/lượng" mode="down" marks={[{ i: 10, label: "ĐỈNH 190,9", col: "#f5c518" }]} bracket={{ a: 22, b: 25, label: "−17 TRIỆU / 3 PHIÊN", at: rel("S15", 1, sc("S15").a) + 1.0 }} src="Nguồn: SJC (dữ liệu WiData), giá bán ra" />)],
    [2, () => CD((t, d) => <><ChartCard t={t} d={d} title="Không chỉ vàng: VN-Index cũng rơi" sub="Điểm đóng cửa · 10/2 → 13/11/2026" data={VNI_26} unit="điểm" scale={1} dec={1} mode="down" reveal={0.9} marks={[{ i: 7, label: "Vía Thần Tài 1.879,6", col: "#8fd3ff" }, { i: 24, label: "23/3: 1.591,2", col: "#ff4d5e", up: false, at: 2.2 }]} src="Nguồn: VN-Index đóng cửa (HOSE, dữ liệu WiData; 13/11 theo Vietstock)" /><Meme t={t} at={rel("S15", 3, sc("S15").sens[2].a) + 2.0} top="" bot="ÉT O ÉT!" small /></>)],
    [4, () => CD((t) => <ChatCard t={t} title="Hội anh em xóm trọ" msgs={[{ who: "Hùng", text: "Vàng giảm ghê quá ông ơi 😨", at: 0.3 }, { who: "Tân", text: "Chỉnh tí thôi, vàng là phải giữ dài 😎", at: 1.3, me: true }]} side={<SideText t={t} at={1.8} l1="“CHỈNH" l2="TÍ THÔI”" />} />)],
    [5, () => D3(S("room", "roomdim", [[-0.4, 1.5, 3.0], [1.56, 1.2, 0.9], 40], [[0.0, 1.4, 2.6], [1.56, 1.2, 0.9], 34], [C("tan", BED1, P("worried", { mode: "sit", acc: ["phone", "glow"] })), C("ngan", BED_B, P("sleepy", { mode: "sit" }))], { chat: "off", game: false }), (t) => <ClockTag t={t} text={t < rel("S15", 6, sc("S15").sens[5].a) ? "02:14" : "06:00"} />)],
  ] },
  { id: "S16", shots: [
    [0, () => D3(S("room", "roomdim", [[1.2, 1.5, 0.8], [2.7, 1.2, -1.3], 42], [[1.6, 1.45, 0.4], [2.7, 1.2, -1.3], 36], [C("ngan", [2.6, 0, -1.1], seq([[0, "neutral"], [1.4, "shock"]], { acc: ["paper"] }))], { chat: "off", game: false }))],
    [1, () => CD((t) => <PaperCard t={t} kind="receipt" hue="red" title="HOÁ ĐƠN BÁN HÀNG" sub="Ngày 26/02/2026" lines={[{ text: "Nhẫn tròn 9999 × 5 lượng", at: 0.2 }, { text: "THÀNH TIỀN: 920.000.000 đ", at: 0.5, big: true, under: true, col: "#b3131f" }]} stamp={{ text: "920 TRIỆU", at: 1.0 }} />)],
    [2, () => D3(S("room", "roomdim", [[-0.2, 1.45, 2.8], [1.56, 1.15, 0.9], 40], [[0.3, 1.35, 2.3], [1.56, 1.15, 0.9], 34], [C("ngan", BED1, P("sad", { mode: "sit", acc: ["paper"] }))], { chat: "off", game: false, ease: "lin" }))],
    [3, () => D3(S("room", "roomdim", [[0.6, 1.25, 2.0], [1.56, 1.25, 0.9], 32], [[0.75, 1.25, 1.8], [1.56, 1.25, 0.9], 28], [C("ngan", BED1, P("sad", { mode: "sit" }))], { chat: "off", game: false }), (t) => <Bubble t={t} at={0.6} x={1060} y={180} w={720} text="Tiền của mẹ cũng ở trong đó, phải không anh?" />)],
    [4, () => D3(S("room", "roomdim", [[0.3, 1.45, 1.6], [0.5, 1.32, -0.2], 40], [[0.35, 1.42, 1.3], [0.5, 1.3, -0.2], 36], [C("tan", [0.5, 0, -0.2], P("sad", { headTilt: 8 }))], { chat: "off", game: false }))],
    [5, () => D3(S("room", "roomdim", [[0.65, 1.2, 1.85], [1.56, 1.25, 0.9], 30], [[0.8, 1.2, 1.65], [1.56, 1.25, 0.9], 26], [C("ngan", BED1, P("cry", { mode: "sit", acc: ["tears"], anim: true }))], { chat: "off", game: false }))],
    [7, () => D3(S("room", "roomdim", [[-1.6, 2.0, 3.3], [1.56, 1.0, 0.9], 46], [[-1.0, 1.8, 2.8], [1.56, 1.0, 0.9], 42], [C("tan", BED_A, P("sad", { mode: "sit", headTilt: 6 })), C("ngan", BED_B, P("sad", { mode: "sit", headTilt: -5 }))], { chat: "off", game: false, ease: "lin" }), (t) => <Vignette k={0.8} />)],
  ] },
  { id: "S17", shots: [
    [0, () => CD((t, d) => <ChartCard t={t} d={d} title="Vàng nhẫn hồi lên mùa hè" sub="Giá bán ra · 26/2 → 13/11/2026" data={RING_26.slice(0, 8)} unit="triệu đồng/lượng" mode="down" marks={[{ i: 0, label: "Mua 184", col: "#8fd3ff" }, { i: 7, label: "29/8: 148,2", col: "#2bd17e", at: 0.5 }]} src="Nguồn: SJC (dữ liệu WiData), giá bán ra" />)],
    [2, () => CD((t) => <PhoneCard t={t} hue="red" time="14:26" date="Thứ Bảy, 29 tháng 8" notifs={[{ app: "Điện thoại", col: "#2b9a5a", title: "Cuộc gọi đến", body: "Mẹ", at: 0.3 }, { app: "Tin nhắn", col: "#2f6fd1", title: "Mẹ", body: "Bác sĩ bảo mẹ phải mổ sớm con ạ.", at: rel("S17", 3, sc("S17").sens[2].a) + 0.3 }]} quote={["MẸ PHẢI", "MỔ SỚM"]} qAt={rel("S17", 3, sc("S17").sens[2].a) + 0.8} />)],
    [4, () => D3(S("room", "roomdim", [[0.8, 1.45, 1.4], [0.6, 1.32, -0.2], 40], [[0.75, 1.42, 1.1], [0.6, 1.32, -0.2], 34], [C("tan", [0.6, 0, -0.2], seq([[0, "shock"], [1.0, "sad"]], { acc: ["phone"] }))], { chat: "off", game: false }))],
    [5, () => D3(S("room", "roomdim", [[1.4, 0.6, 3.5], [2.2, 0.2, 1.9], 42], [[1.95, 0.4, 2.8], [2.2, 0.18, 1.9], 36], [], { chat: "off", game: false }), (t) => <BigText t={t} at={1.0} text="ĐANG LỖ" col="#ff4d5e" y={640} size={120} />)],
    [6, () => D3(S("streetday", "day", [[GOLD_X + 4.4, 1.4, 3.0], [GOLD_X + 5.0, 1.2, 5.6], 38], [[GOLD_X + 4.6, 1.4, 3.4], [GOLD_X + 5.0, 1.2, 5.6], 34], [C("c3", [GOLD_X + 4.4, 0.15, 5.6], P("worried", { side: -1 })), C("tan", [GOLD_X + 5.6, 0.15, 5.6], seq([[0, "neutral"], [1.0, "stern"]], { side: 1 }))]), (t) => <><Bubble t={t} at={0.3} x={1040} y={170} w={600} tail="r" text="Bán bớt đi mà trả nợ, ông ơi!" /><Bubble t={t} at={rel("S17", 7, sc("S17").sens[6].a)} x={300} y={170} w={600} text="Chờ về bờ đã, giờ bán là lỗ!" /></>)],
    [8, () => D3(S("streetday", "golden", [[XECU_X + 7, 1.4, 2.0], [XECU_X + 4, 1.0, 5.2], 44], [[XECU_X + 2.5, 1.4, 2.4], [XECU_X, 1.0, 5.2], 44], [C("tan", [XECU_X + 4.1 - PUSH[0], 0.15, 5.0 + PUSH[1]], pushPose("sad", 1), [XECU_X - 0.3 - PUSH[0], 0.15, 5.0 + PUSH[1]]), C("bike", [XECU_X + 4.1, 0.15, 5.0], () => P("neutral")(0), [XECU_X - 0.3, 0.15, 5.0])], { ease: "lin" }), (t, d) => <BigText t={t} at={d * 0.6} text="BÁN XE: 24 TRIỆU" col="#fff" y={120} size={96} />)],
    [9, () => CD((t) => <PhoneCard t={t} hue="warm" time="20:15" date="Thứ Năm, 3 tháng 9" notifs={[{ app: "Tin nhắn", col: "#2f6fd1", title: "Mẹ", body: "Con nhớ ăn uống đầy đủ.", at: 0.5 }]} quote={["MẸ KHÔNG TRÁCH", "MỘT CÂU"]} qAt={0.2} />)],
    [11, () => CD((t, d) => <><TitleCard t={t} hue="red" kicker="CÂU NÓI ĐẮT GIÁ NHẤT" l1="“CHỜ VỀ BỜ" l2="ĐÃ…”" /><Meme t={t} at={Math.max(1.6, d * 0.55)} top="" bot="…BỜ ĐÂU?" small y={110} /></>)],
  ] },
  { id: "S18", shots: [
    [0, () => CD((t) => <NewsCard t={t} tag="DRAMA PHÒNG TẬP · 26/10/2026" items={[{ src: "BÁO VĂN HÓA · 26/10", head: "California Fitness tạm dừng toàn bộ cơ sở tại Hà Nội", at: 0.4 }, { src: "HỘI VIÊN", head: "Đã trả tiền thẻ nhiều năm, vẫn trả góp ngân hàng – chưa có phương án hoàn tiền", at: 2.4, col: "#1f4e8a" }]} />)],
    [1, () => CD((t) => <PhoneCard t={t} hue="red" time="08:00" date="Ngày 5 tháng 11" notifs={[{ app: "Ngân hàng", col: "#b3131f", title: "Nhắc thanh toán trả góp", body: "Kỳ 9/12: 3.000.000 đ · Hợp đồng hội viên phòng tập", at: 0.4 }]} quote={["VẪN TRẢ GÓP", "MÀ HẾT CHỖ TẬP"]} qAt={1.2} />)],
    [2, () => D3(S("streetday", "day", [[GX0 + 1.5, 2.4, 0.2], [GX0, 1.2, 5.3], 52], [[GX0 + 0.8, 1.7, 1.2], [GX0, 1.2, 5.3], 48], gymCast(), { shake: 0.4 }), (t) => <Meme t={t} top="PHÒNG GYM ĐÓNG CỬA" bot="TẬP LUÔN TRÊN VỈA HÈ" />)],
    [3, () => D3(S("streetday", "day", [[GX0 + 1.5, 1.5, 2.6], [GX0 + 1.3, 1.3, 5.3], 40], [[GX0 + 1.45, 1.45, 3.0], [GX0 + 1.3, 1.3, 5.3], 36], [C("gym", [GX0 + 1.5, 0.15, 5.3], P("smug", { acc: ["flex"], anim: true })), C("c4", [GX0 + 3.6, 0.15, 5.75], walk("worried", { side: 1 }), [GX0 + 0.2, 0.15, 5.75])], { ease: "lin" }), (t) => <Bubble t={t} at={0.9} x={1080} y={130} w={600} tail="r" text="Tay anh to không em? 💪" />)],
    [4, () => D3(S("streetday", "day", [[GX0 - 1.4, 1.5, 2.9], [GX0 - 1.8, 1.25, 5.3], 40], [[GX0 - 1.5, 1.45, 3.3], [GX0 - 1.8, 1.25, 5.3], 36], [C("boxer", [GX0 - 1.8, 0.15, 5.3], P("stern", { acc: ["box"], anim: true })), C("c8", [GX0 - 3.3, 0.15, 5.1], P("shock", { tilt: -10 })), C("c12", [GX0 - 0.2, 0.15, 5.1], P("worried", { tilt: 10 }))], { shake: 0.8 }), (t) => <Meme t={t} at={0.5} top="" bot="VÈO! VÈO!" small y={110} />)],
    [5, () => D3(S("streetday", "day", [[GX0 - 0.2, 1.5, 2.2], [GX0 - 0.2, 1.25, 5.3], 44], [[GX0 - 0.2, 1.45, 2.7], [GX0 - 0.2, 1.25, 5.3], 40], [C("boxer", [GX0 - 1.8, 0.15, 5.3], P("grin", { acc: ["box"], anim: true })), C("gym", [GX0 + 1.5, 0.15, 5.3], P("smug", { acc: ["flex"], anim: true })), C("tan", [GX0 + 0.6, 0.15, 4.9], walk("nervous", { acc: ["sweat"] }), [GX0 - 0.7, 0.15, 4.9])], { ease: "lin" }), (t) => <Bubble t={t} at={0.6} x={560} y={110} w={800} kind="think" text="Mất tiền thẻ tập đã đành, giờ ra đường còn suýt ăn đấm…" />)],
    [6, () => CD((t) => <NewsCard t={t} tag="TIN NÓNG · 11–13/11/2026" items={[{ src: "VNEXPRESS · 11/11", head: "Lạm phát Mỹ cao hơn dự kiến, vàng mất gần 130 USD", at: rel("S18", 7, sc("S18").sens[6].a) - 0.6 }, { src: "VNEXPRESS · 13/11", head: "Ông Trump: Mỹ “không cần thỏa thuận” với Iran", at: rel("S18", 7, sc("S18").sens[6].a) + 1.2 }, { src: "TUỔI TRẺ · 13/11", head: "USD lên cao nhất 19 tháng, vàng thế giới mất hơn 100 USD", at: rel("S18", 8, sc("S18").sens[6].a) }]} />)],
    [9, () => CD((t, d) => <ChartCard t={t} d={d} title="Vàng thế giới" sub="Giá cuối tuần · 2026" data={WORLD} unit="USD/ounce" scale={1} dec={0} mode="down" marks={[{ i: 2, label: "ĐỈNH 5.387", col: "#f5c518" }, { i: WORLD.length - 1, label: "3.892", col: "#ff4d5e", up: false }]} src="Nguồn: CME (dữ liệu WiData)" />)],
    [10, () => CD((t) => <NewsCard t={t} tag="TIN ĐỒN TRÊN MẠNG · CHƯA KIỂM CHỨNG" items={[{ src: "HỘI BÀN TRÀ ĐÁ · TIN ĐỒN", head: "CEO hãng card đồ họa INDIAVIA (Ấn Độ) “yêu nhầm” một nữ gián điệp?!", at: 0.3, col: "#6b4fa0" }, { src: "BÌNH LUẬN NỔI BẬT", head: "“Bảo sao card nhà em dạo này chạy nóng thế…”", at: 2.6, col: "#1f4e8a" }]} />)],
    [11, () => D3(S("room", "roomdim", [[0.2, 1.2, 1.0], [-1.3, 0.75, -1.5], 46], [[0.05, 1.15, 0.75], [-1.3, 0.72, -1.5], 42], [C("tan", [-1.95, 0, -1.15], seq([[0, "neutral"], [1.0, "worried"]], { acc: ["sweat"], anim: true }))], { chat: "off", game: false, shake: 0.3 }), (t) => <Bubble t={t} at={1.2} x={1040} y={130} w={700} kind="think" text="Hèn gì dạo này nó cứ nháy đèn nhìn mình…" />)],
    [12, () => D3(S("room", "roomdim", [[0.05, 1.15, 0.75], [-1.3, 0.72, -1.5], 42], [[0.0, 1.12, 0.6], [-1.3, 0.72, -1.5], 40], [C("tan", [-1.95, 0, -1.15], P("stern", { prop: "hold2" }))], { chat: "off", game: false }), (t) => <Meme t={t} at={0.7} top="XOAY MÁY VÀO TƯỜNG" bot="CHO CHẮC ĂN" />)],
    [13, () => CD((t, d) => <ChartCard t={t} d={d} title="Vàng miếng SJC 4 phiên gần nhất" sub="Giá bán ra · 9/11 → 13/11/2026" data={SJC_NOW} unit="triệu đồng/lượng" mode="down" reveal={0.5} bracket={{ a: 0, b: 4, label: "−3,2 TRIỆU", at: 1.6 }} src="Nguồn: SJC (dữ liệu WiData), giá bán ra" />)],
  ] },
  { id: "S19", shots: [
    [0, () => CD((t) => <ChatCard t={t} title="Hùng" msgs={[{ who: "Hùng", text: "Tân ơi, vợ tao sắp sinh, mày xoay được ít nào không?", at: 0.4 }]} side={<SideText t={t} at={1.6} l1="ĐẾN HẠN" l2="TRẢ NỢ" />} />)],
    [1, () => D3(S("street", "night", [[GOLD_X + 12, 1.4, 2.2], [GOLD_X + 8, 1.1, 5.2], 44], [[GOLD_X + 5, 1.4, 2.2], [GOLD_X + 1.5, 1.1, 5.2], 44], [C("tan", [GOLD_X + 9, 0.15, 5.2], walk("sad", { acc: ["goldbag"] }), [GOLD_X + 1.6, 0.15, 5.2])], { ease: "lin" }))],
    [2, () => D3(S("shop", "day", [[-4.6, 1.55, -0.45], [-1.5, 1.25, -0.45], 40], [[-4.2, 1.5, -0.45], [-1.5, 1.25, -0.45], 36], [C("tan", [-1.5, 0, 0.45], P("worried", { side: -1 })), C("clerk", [-1.5, 0, -1.4], P("smile", { side: 1 }))], { board: "sell" }), (t) => <Bubble t={t} at={1.2} x={200} y={140} w={700} text="Bên em mua lại 133,8 triệu một lượng anh ạ." />)],
    [3, () => D3(S("shop", "day", [[-3.1, 2.1, -0.7], [-3.2, 2.1, -2.9], 46], [[-3.15, 2.1, -1.0], [-3.2, 2.1, -2.9], 42], [], { board: "sell" }), (t) => <Bubble t={t} at={0.6} x={1180} y={24} w={640} tail="r" text="Nhưng bảng ghi 137,8 cơ mà?!" />)],
    [4, () => D3(S("shop", "day", [[-4.6, 1.55, -0.45], [-1.5, 1.25, -0.45], 40], [[-4.2, 1.5, -0.45], [-1.5, 1.25, -0.45], 36], [C("tan", [-1.5, 0, 0.45], seq([[0, "shock"], [1.6, "sad"]], { side: -1 })), C("clerk", [-1.5, 0, -1.4], P("smile_closed", { side: 1 }))], { board: "sell" }), (t) => <><Bubble t={t} at={0.4} x={200} y={140} w={680} text="Đấy là giá tiệm BÁN RA anh ơi." /><Meme t={t} at={1.8} top="" bot="BÁN RA ≠ MUA LẠI" small y={560} /></>)],
    [5, () => D3(S("street", "night", [[GOLD_X - 2.9, 1.0, 2.8], [GOLD_X - 1.7, 0.8, 5.6], 40], [[GOLD_X - 2.4, 0.95, 3.3], [GOLD_X - 1.7, 0.8, 5.6], 34], [C("tan", [GOLD_X - 1.7, 0.15, 5.6], P("sad", { mode: "sit", acc: ["paper"] }))]), (t) => <><Vignette k={0.6} /><Meme t={t} at={0.4} top="KỲ VỌNG: XÂY NHÀ CHO MẸ" bot="" /><Meme t={t} at={1.4} top="" bot="THỰC TẾ: NGỒI BẬC THỀM" noSubGap /></>)],
    [6, () => CD((t) => <PaperCard t={t} kind="note" hue="night" title="SỔ TAY CỦA TÂN" sub="13/11/2026" lines={[
      { text: "Mua 26/2: 5 lượng × 184 = 920 triệu", at: 0.4 },
      { text: "Bán 13/11: 5 lượng × 133,8 = 669 triệu", at: rel("S19", 7, sc("S19").sens[6].a) },
      { text: "MẤT: 251 TRIỆU", at: rel("S19", 8, sc("S19").sens[6].a), big: true, col: "#d8212f", under: true },
      { text: "Trả bạn 200 · Trả mẹ 120", at: rel("S19", 9, sc("S19").sens[6].a) },
      { text: "Còn lại: 349 triệu", at: rel("S19", 9, sc("S19").sens[6].a) + 1.6, big: true }]}
      stamp={{ text: "MẤT 251 TRIỆU", at: rel("S19", 8, sc("S19").sens[6].a) + 0.9 }} sign="Người ghi: Tân"
      side={<SideText t={t} at={rel("S19", 9, sc("S19").sens[6].a) + 2.4} l1="10 NĂM" l2="CÒN 349 TRIỆU" />} />)],
  ] },
  { id: "S20", shots: [
    [0, () => CD((t) => <TitleCard t={t} hue="navy" kicker="BÀI HỌC" l1="KHÔNG PHẢI VÌ" l2="VÀNG XẤU" sub="Vàng vẫn là một tài sản tốt" />)],
    [2, () => CD((t) => { const a = sc("S20").sens[2].a; return <><LessonCard t={t} title="Cái sai nằm ở 4 chỗ" items={[
      { n: "1", icon: "🔥", head: "Mua khi cả xã hội phát sốt", body: "Phải đội mưa xếp hàng = giá đã chạy rất xa", at: rel("S20", 3, a) },
      { n: "2", icon: "💸", head: "Dùng tiền vay, tiền dưỡng già của người thân", body: "Vàng không trả lãi, nhưng nợ vẫn đến hạn", at: rel("S20", 5, a) },
      { n: "3", icon: "🏷️", head: "Nhầm giá giữ với giá bán", body: "Tiệm mua lại thấp hơn giá niêm yết vài triệu mỗi lượng", at: rel("S20", 7, a) },
      { n: "4", icon: "📜", head: "Trả trước cho những lời hứa", body: "“Giữ giá”, “tập trọn đời” – đẹp cho đến ngày mình cần", at: rel("S20", 9, a) }]} />
      {t > rel("S20", 11, a) && <AbsoluteFill style={{ background: `rgba(5,8,20,${0.78 * sm((t - rel("S20", 11, a)) / 0.4)})` }} />}
      <BigText t={t} at={rel("S20", 11, a)} text="LỜI HỨA ≠ TÀI SẢN" col="#ffcf3a" y={400} size={130} /></>; })],
  ] },
  { id: "S21", shots: [
    [0, () => D3(S("lake", "lake", [[-30, 12, 30], [0, 1, -10], 52], [[-14, 3.0, 20], [2, 1.2, -6], 46], [C("tan", LAKE_T, P("sad", { mode: "sit" })), C("ngan", LAKE_N, P("neutral", { mode: "sit" }))]), (t) => <LocTag t={t} l1="HỒ GƯƠM" l2="Hà Nội · cầu Thê Húc" />)],
    [1, () => D3(S("lake", "lake", [[-9.5, 1.3, 16.5], [-2, 1.2, 6], 46], [[-8.6, 1.25, 15.6], [-1.5, 1.2, 6], 42], [C("tan", LAKE_T, P("sad", { mode: "sit" })), C("ngan", LAKE_N, P("neutral", { mode: "sit" }))]))],
    [2, () => D3(S("lake", "lake", [[-7.0, 1.45, 14.7], [-6.4, 1.38, 12.6], 34], [[-6.9, 1.45, 14.4], [-6.4, 1.38, 12.6], 30], [C("tan", LAKE_T, P("sad", { mode: "sit", acc: ["phone"] }))]))],
    [3, () => D3(S("lake", "lake", [[-6.75, 1.45, 14.4], [-6.4, 1.4, 12.6], 30], [[-6.7, 1.45, 14.1], [-6.4, 1.4, 12.6], 26], [C("tan", LAKE_T, P("worried", { mode: "sit", acc: ["phone"] }))], { ease: "lin" }))],
    [4, () => D3(S("streetday", "golden", [[-31.2, 1.3, 3.8], [-30, 1.35, 5.85], 30], [[-31.0, 1.3, 4.2], [-30, 1.35, 5.85], 26], [me("smile_closed", ["nonla", "phone"])]), (t) => <><Bubble t={t} at={0.4} x={1060} y={180} w={700} text="Con biết sai là được rồi." />{t > rel("S21", 5, sc("S21").sens[4].a) && <Bubble t={t} at={rel("S21", 5, sc("S21").sens[4].a)} x={1060} y={420} w={700} text="Tiền thì mẹ con mình làm lại." />}</>)],
    [6, () => D3(S("lake", "lake", [[-6.8, 1.45, 14.6], [-6.1, 1.38, 12.6], 34], [[-6.7, 1.45, 14.3], [-6.1, 1.38, 12.6], 30], [C("tan", LAKE_T, P("cry", { mode: "sit", acc: ["tears"], anim: true })), C("ngan", LAKE_N, P("sad", { mode: "sit" }))]))],
    [8, () => D3(S("lake", "lake", [[-6.0, 1.4, 14.6], [-6.0, 1.35, 12.4], 36], [[-6.0, 1.4, 14.2], [-6.0, 1.35, 12.4], 32], [C("tan", LAKE_T, P("relief", { mode: "sit" })), C("ngan", LAKE_N, P("smile_closed", { mode: "sit" }))]), (t) => <Bubble t={t} at={0.6} x={1060} y={170} w={720} text="Từ nay nhà mình có kế hoạch, và không giấu nhau nữa." />)],
    [9, () => D3(S("lake", "lake", [[-5.5, 1.45, 14.4], [-5.6, 1.35, 12.6], 32], [[-5.55, 1.45, 14.0], [-5.6, 1.35, 12.6], 28], [C("ngan", LAKE_N, P("smile", { mode: "sit", acc: ["phone", "glow"] }))]), (t) => <Bubble t={t} at={0.4} x={1060} y={170} w={600} text="Em kể anh nghe một bí mật…" />)],
    [10, () => CD((t, d) => <DcaCard t={t} d={d} a2={rel("S21", 12, sc("S21").sens[10].a)} a3={rel("S21", 14, sc("S21").sens[10].a)} />)],
    [13, () => D3(S("lake", "lake", [[-6.0, 1.5, 14.6], [-6.0, 1.35, 12.6], 36], [[-6.0, 1.5, 14.2], [-6.0, 1.35, 12.6], 32], [C("tan", LAKE_T, P("dazed", { mode: "sit" })), C("ngan", LAKE_N, P("smile_closed", { mode: "sit" }))]), (t) => <><Bubble t={t} at={0.3} x={1060} y={150} w={700} text="Không phải chứng khoán thần kỳ đâu anh." />{t > rel("S21", 15, sc("S21").sens[13].a) && <Bubble t={t} at={rel("S21", 15, sc("S21").sens[13].a)} x={1060} y={400} w={700} text="Khác nhau là có kế hoạch, và không dồn hết tiền vào một ngày." />}</>)],
    [16, () => D3(S("lake", "lake", [[-8.6, 1.3, 15.6], [-1.5, 1.2, 6], 42], [[-26, 16, 34], [-20, 2, -30], 50], [C("tan", LAKE_T, P("smile_closed", { mode: "sit" })), C("ngan", LAKE_N, P("smile_closed", { mode: "sit" }))], { ease: "sm" }), (t) => <QuoteOv t={t} at={rel("S21", 17, sc("S21").sens[16].a) + 0.6} />)],
  ] },
  { id: "S22", shots: [[0, () => CD((t) => <CtaCard t={t} webAt={rel("S22", 3, sc("S22").a)} />)]] },
];

function teaStall(e: Expr = "grin", withTan = true): Cast[] {
  const r = [C("c0", [GOLD_X + 5.2, 0.48, 5.72], P(e, { mode: "sit", acc: ["cup"], anim: true })), C("xoi", [GOLD_X + 8.6, 0.48, 5.72], P(e === "laugh" ? "grin" : e, { mode: "sit", acc: ["nonla"] })),
    C("c8", [GOLD_X + 2.0, 0.48, 5.72], P("laugh", { mode: "sit" })), C("c6", [GOLD_X + 11.8, 0.48, 5.72], P("smile", { mode: "sit", acc: ["cup"], anim: true }))];
  return withTan ? [...r, C("tan", [GOLD_X + 6.3, 0.15, 5.45], P("smile"))] : r;
}
const GX0 = HOME_X + 5;
const gymCast = (): Cast[] => [C("gym", [GX0 + 1.5, 0.15, 5.3], P("smug", { acc: ["flex"], anim: true })), C("gym2", [GX0 + 2.8, 0.15, 5.5], P("grin", { acc: ["flex"], anim: true, phase: 0.5 })), C("boxer", [GX0 - 1.8, 0.15, 5.3], P("stern", { acc: ["box"], anim: true })), C("c15", [GX0 - 3.4, 0.15, 5.0], P("worried"))];
const SEATCAM: [[V, V, number], [V, V, number]] = [[[qx(22.5) + 1.3, 1.3, 3.1], [qx(22.5), 1.05, 5.72], 38], [[qx(22.5) + 0.9, 1.25, 3.5], [qx(22.5), 1.05, 5.72], 34]];
const seatCast = (eT: Expr, eB: Expr): Cast[] => [...queue(22), C("tan", [qx(22), 0.48, 5.72], P(eT, { mode: "sit", acc: ["ticket"], num: "102" })), C("c31", [qx(23), 0.48, 5.72], P(eB, { mode: "sit", acc: ["nonla"] }))];
/** dắt xe: người đứng cạnh tay lái, nhìn nghiêng theo hướng đi, hai tay nắm ghi-đông */
const PUSH: [number, number] = [-0.2, -0.45];
const pushPose = (e: Expr, dir: 1 | -1 = -1) => (t: number): Pose => ({ expr: e, side: dir, mode: "march", phase: Math.round(((t * 1.0) % 1) * 14) / 14, reach: [500, 440] });
function hueWalkers(): Cast[] { return Array.from({ length: 8 }, (_, i) => C("c" + i, [(i % 2 ? 1.6 : -1.6), 1.38, -30 + i * 7], walk(i % 3 ? "neutral" : "smile", { acc: ["nonla"], phase: i * 0.3 }), [(i % 2 ? 1.6 : -1.6), 1.38, -30 + i * 7 + (i % 2 ? -6 : 6)])); }
function btCrowd(): Cast[] { return Array.from({ length: 14 }, (_, i) => C("c" + i, [5 + i * 1.1, 0.02, -4.5 + (i % 2) * 0.3], P(i % 4 === 1 ? "worried" : "neutral", { acc: i % 3 === 0 ? ["nonla"] : [], phase: i * 0.4 }))); }

const Meme: React.FC<{ t: number; at?: number; top: string; bot: string; small?: boolean; noSubGap?: boolean; y?: number }> = ({ t, at = 0, top, bot, small, noSubGap, y }) => { if (t < at) return null; const a = Math.min(1, (t - at) / 0.18), sz = small ? 150 : 92;
  const st = { position: "absolute", left: 0, width: 1920, textAlign: "center", fontFamily: F, fontWeight: 900, fontSize: sz, color: "#fff", WebkitTextStroke: "10px #000", paintOrder: "stroke fill", letterSpacing: 1, transform: `scale(${1.25 - 0.25 * a})`, opacity: a } as React.CSSProperties;
  return <>{top && <div style={{ ...st, top: 70 }}>{top}</div>}{bot && <div style={{ ...st, top: y ?? (small ? 690 : noSubGap ? 175 : 620), color: small ? "#ffe14d" : "#fff", fontSize: small ? 130 : sz }}>{bot}</div>}</>; };
const DcaCard: React.FC<{ t: number; d: number; a2: number; a3: number }> = ({ t, a2, a3 }) => {
  const rows = [{ l: "Anh Tân: dồn hết vào đỉnh vàng 26/2", v: -27.3, at: 0.6 }, { l: "Mua vàng nhẫn đều mỗi tháng từ 1/2025", v: 1.2, at: a3 }, { l: "Chị Ngân: mua cổ phiếu theo chỉ số đều mỗi tháng từ 1/2025", v: 10.4, at: a2 }];
  return <AbsoluteFill style={{ fontFamily: F }}><Bg t={t} hue="navy" />
    <div style={{ position: "absolute", left: 160, top: 90, fontSize: 60, fontWeight: 900, color: "#fff", opacity: sm(t / 0.4) }}>Cùng một khoảng thời gian, khác nhau ở cách làm</div>
    {rows.map((r, i) => { const k = sm((t - r.at) / 0.8), w = Math.abs(r.v) / 27.3 * 620 * k, pos = r.v >= 0; if (t < r.at) return null;
      return <div key={i} style={{ position: "absolute", left: 160, top: 250 + i * 190, width: 1600 }}>
        <div style={{ fontSize: 36, fontWeight: 700, color: "#dfe5f2" }}>{r.l}</div>
        <div style={{ position: "relative", height: 80, marginTop: 14 }}>
          <div style={{ position: "absolute", left: 800, top: 0, width: 4, height: 80, background: "#8f9ab3" }} />
          <div style={{ position: "absolute", top: 8, height: 64, borderRadius: 12, background: pos ? "#2bd17e" : "#ff4d5e", left: pos ? 804 : 800 - w, width: w }} />
          <div style={{ position: "absolute", top: 4, fontSize: 60, fontWeight: 900, color: pos ? "#2bd17e" : "#ff4d5e", left: pos ? 820 + w : 780 - w - 260, width: 260, textAlign: pos ? "left" : "right", opacity: k }}>{(r.v > 0 ? "+" : "") + r.v.toLocaleString("vi-VN", { maximumFractionDigits: 1 })}%</div>
        </div></div>; })}
    <div style={{ position: "absolute", left: 160, bottom: 200, width: 1600, fontSize: 22, color: "#8f9ab3", lineHeight: 1.4 }}>Minh hoạ tính theo VN-Index và giá vàng nhẫn SJC (mua đầu/cuối mỗi tháng, định giá 13/11/2026 theo giá tiệm mua lại / điểm đóng cửa), chưa gồm cổ tức, phí, thuế.</div>
  </AbsoluteFill>; };
const DreamCard: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.5), b = sm((t - 1.2) / 0.8);
  return <AbsoluteFill style={{ fontFamily: F }}><Bg t={t} hue="warm" />
    <div style={{ position: "absolute", left: 220, top: 300, opacity: a * (1 - b * 0.6) }}><House w={520} old /></div>
    <div style={{ position: "absolute", left: 800, top: 430, fontSize: 120, color: "#f5c518", opacity: b }}>➜</div>
    <div style={{ position: "absolute", left: 1060, top: 200, opacity: b, transform: `scale(${0.8 + 0.2 * b})` }}><House w={620} /></div>
    <div style={{ position: "absolute", left: 0, top: 90, width: 1920, textAlign: "center", fontSize: 72, fontWeight: 900, color: "#fff", opacity: a }}>Ước mơ: xây lại nhà cho mẹ</div></AbsoluteFill>; };
const House: React.FC<{ w: number; old?: boolean }> = ({ w, old }) => <div style={{ width: w, position: "relative" }}>
  <div style={{ width: 0, height: 0, borderLeft: `${w / 2}px solid transparent`, borderRight: `${w / 2}px solid transparent`, borderBottom: `${w * 0.32}px solid ${old ? "#7a5a3c" : "#c8202f"}` }} />
  <div style={{ width: w * 0.86, height: old ? w * 0.42 : w * 0.62, margin: "0 auto", background: old ? "#bfae92" : "#f6efe2", border: "6px solid #2a2026", display: "flex", justifyContent: "space-around", alignItems: "flex-end", paddingBottom: 0 }}>
    <div style={{ width: w * 0.18, height: w * 0.26, background: old ? "#5c4636" : "#8a5a3a" }} /><div style={{ width: w * 0.2, height: w * 0.16, background: old ? "#4a3a30" : "#9fd3ff", marginBottom: w * 0.12, border: "4px solid #2a2026" }} /></div></div>;
const NoteCard: React.FC<{ t: number }> = ({ t }) => { const a = sm(t / 0.4);
  return <AbsoluteFill style={{ fontFamily: F }}><Bg t={t} hue="night" />
    <div style={{ position: "absolute", left: 640, top: 200 + (1 - a) * 60, width: 640, height: 600, background: "#ffe97a", transform: "rotate(-3deg)", boxShadow: "0 30px 60px rgba(0,0,0,.5)", padding: 60, boxSizing: "border-box", opacity: a }}>
      <div style={{ width: 60, height: 60, borderRadius: 30, background: "#d8212f", position: "absolute", left: 290, top: -20, boxShadow: "0 6px 10px rgba(0,0,0,.4)" }} />
      <div style={{ fontSize: 66, fontWeight: 800, color: "#2a2026", lineHeight: 1.35, marginTop: 70, fontStyle: "italic" }}>Anh đi tập<br />thể dục 💪</div>
      <div style={{ fontSize: 40, color: "#5c4a3a", marginTop: 40, textAlign: "right" }}>— Tân, 3:00</div></div></AbsoluteFill>; };
const QuoteOv: React.FC<{ t: number; at: number }> = ({ t, at }) => { const a = sm((t - at) / 0.8); if (t < at) return null;
  return <AbsoluteFill style={{ background: `rgba(5,7,20,${0.55 * a})`, justifyContent: "center", alignItems: "center", textAlign: "center", fontFamily: F }}>
    <div style={{ opacity: a, transform: `translateY(${(1 - a) * 20}px)`, maxWidth: 1500 }}>
      <div style={{ fontSize: 40, color: "#f5c518", fontWeight: 800, letterSpacing: 6 }}>TÀI SẢN GIỮ GIÁ THẬT SỰ</div>
      <div style={{ fontSize: 66, color: "#fff", fontWeight: 800, lineHeight: 1.3, marginTop: 24 }}>là thứ mình hiểu rõ, mua có kế hoạch,<br />và không làm người mình thương phải lo lắng.</div></div></AbsoluteFill>; };

// ---------- build segments from the plan + timing ----------
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
export const VANG_FRAMES = TOTAL_F;
export const VangVideo: React.FC = () => {
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
        {audio ? <Audio src={staticFile("vang/voice.wav")} /> : null}
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
