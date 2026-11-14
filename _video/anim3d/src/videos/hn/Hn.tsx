// Phim 3D #3 "Thế giới chuẩn bị cho chiến tranh hạt nhân? – Quang Hà". Khung 1920x1080, 30 fps.
// Mỗi câu thoại có mốc thời gian thật (timing.json do giọng Huy70_HaiDang30 đọc) → cắt cảnh đúng câu, phụ đề đúng chữ.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, staticFile, delayRender, continueRender, Audio, getInputProps } from "remotion";
import { Stage, Shot3D, Run, SetKey, Cast, V } from "../vang/stage";
import { Pose, Acc } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { GOLD_X, HOME_X } from "../vang/sets";
import { Article, AlertCard, BoardCard, GoldBoard, DoomClock, HistoryCard } from "./cards_hn";
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
const DREAM: React.FC<{ t: number }> = ({ t }) => <><Vignette k={0.9} col="70,0,0" /><div style={{ position: "absolute", left: 60, top: 50, fontFamily: F, fontWeight: 900, fontSize: 34, color: "#ffd0d0", background: "rgba(80,0,0,.55)", padding: "8px 20px", borderRadius: 10, opacity: Math.min(1, t / 0.4) }}>GIẤC MƠ CỦA QUANG</div></>;
const Flash: React.FC<{ t: number; at?: number }> = ({ t, at: a0 = 0.2 }) => { const x = t - a0; if (x < 0 || x > 2.2) return null; const k = x < 0.12 ? x / 0.12 : Math.exp(-(x - 0.12) * 2.4); return <AbsoluteFill style={{ background: `rgba(255,250,235,${0.92 * k})` }} />; };
const runners = (n: number, x0: number, x1: number, z: number, acc: Acc[] = ["box"]): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (30 + i), [x0 + (i % 4) * 0.7, 0, z + (i % 3) * 0.55], (t: number) => ({ ...P(i % 2 ? "shock" : "worried", { acc: i % 3 ? acc : [] })(t), mode: "stroll", phase: (t * 1.6 + i * 0.37) % 1, side: x1 < x0 ? 1 : -1 }), [x1 + (i % 4) * 0.7, 0, z + (i % 3) * 0.55]));
const queue = (n: number): Cast[] => Array.from({ length: n }, (_, i) => C("c" + (40 + i), [-3.6 + i * 0.85, 0, 2.6 + (i % 2) * 0.35], P(i % 3 === 0 ? "worried" : i % 3 === 1 ? "nervous" : "neutral", { acc: i % 4 === 0 ? ["phone"] : [], phase: i * 0.3, anim: true })));
const AtmCard: React.FC<{ t: number }> = ({ t }) => <AbsoluteFill style={{ background: "radial-gradient(circle,#2a0606,#070101)", fontFamily: F, justifyContent: "center", alignItems: "center" }}><DREAM t={t} />
  <div style={{ width: 1000, height: 640, borderRadius: 30, background: "#1b2a3a", border: "14px solid #5a6b7d", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", gap: 30 }}>
    <div style={{ fontSize: 44, color: "#9fc3e6", fontWeight: 800 }}>MÁY RÚT TIỀN TỰ ĐỘNG</div>
    <div style={{ fontSize: 150, color: "#ff4d5e", fontWeight: 900, opacity: 0.6 + 0.4 * Math.abs(Math.sin(t * 4)) }}>HẾT TIỀN</div>
    <div style={{ fontSize: 40, color: "#e6eef6", fontWeight: 700 }}>Máy tạm ngừng phục vụ. Xin lỗi quý khách.</div></div></AbsoluteFill>;
const BreadCard: React.FC<{ t: number; a: number; b: number }> = ({ t, a, b }) => { const p = t < a ? "30.000đ" : t < b ? "300.000đ" : "3.000.000đ", lbl = t < a ? "SÁNG" : t < b ? "CHIỀU" : "TỐI";
  return <AbsoluteFill style={{ background: "radial-gradient(circle,#2b1a08,#0a0502)", fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><DREAM t={t} />
    <div style={{ fontSize: 200 }}>🥖</div><div style={{ fontSize: 60, color: "#ffd9a0", fontWeight: 900 }}>BÁNH MÌ · {lbl}</div>
    <div key={p} style={{ fontSize: 190, color: "#ff4d5e", fontWeight: 900, transform: `scale(${1 + 0.25 * Math.max(0, 1 - ((t - (t < a ? 0 : t < b ? a : b)) / 0.25))})` }}>{p}</div></AbsoluteFill>; };
const DreamGold: React.FC<{ t: number; a: number; b: number }> = ({ t, a, b }) => { const v = t < a ? "140" : t < b ? "300" : "1.000";
  return <><GoldBoard t={t} dream shop="BẢNG GIÁ VÀNG" date="(trong mơ)" rows={[{ name: "Vàng miếng 1 lượng", buy: v === "1.000" ? "—" : v, sell: v, at: 0 }]} /><DREAM t={t} /></>; };
const PlanCard: React.FC<{ t: number }> = ({ t }) => <PaperCard t={t} kind="note" hue="warm" title="KẾ HOẠCH NHÀ MÌNH KHI CÓ BIẾN" sub="Quang & Trang · 14/11/2026" lines={[
  { text: "Quỹ dự phòng 6 tháng chi tiêu – có 1 phần tiền mặt ở nhà", at: 0.6 }, { text: "Nước, thuốc, đèn, đài pin cho 3 ngày", at: 1.4 },
  { text: "KHÔNG vay để chạy theo tin đồn", at: 2.2, big: true, col: "#d8212f" }, { text: "Muốn bán: kiểm tin chính thức + chờ 1 đêm", at: 3.0, big: true }]} sign="Ký: Quang – Trang" />;

const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => D3(S("photo", "night", ...fixed([0, 1.6, -8], [0, 1.9, 6], 46), [], { bg: "hn/hanoi_night.jpg", bgFit: [0.6, 0.45], shake: 0.6 }), (t) => <><Flash t={t} at={0.9} /><DREAM t={t} /></>)],
    [1, () => D3(S("photo", "night", [[0, 1.4, -7], [0, 1.3, 4], 46], [[0.6, 1.4, -6.4], [0, 1.3, 4], 44], runners(10, 6, -6, 0.4, ["box", "phone"]), { bg: "hn/street_night.jpg", bgFit: [0.5, 0.55], shake: 0.9, ease: "lin" }), (t) => <><DREAM t={t} /><BigText t={t} at={0.2} text="🚨 BÁO ĐỘNG" col="#ff4d5e" y={90} size={96} /></>)],
    [4, () => CD((t) => <AtmCard t={t} />)],
    [5, () => CD((t) => <BreadCard t={t} a={at("S01", 5, 5) + 1.4} b={at("S01", 5, 5) + 2.7} />)],
    [6, () => CD((t) => <DreamGold t={t} a={1.9} b={3.0} />)],
    [7, () => D3(S("street", "night", [[TS + 2.6, 1.45, 2.2], [TS + 2.6, 1.1, 5.6], 40], [[TS + 2.6, 1.42, 2.6], [TS + 2.6, 1.1, 5.6], 37], [C("ba", [TS + 1.9, 0.15, 5.6], P("stern", { side: -1 })), C("quang", [TS + 3.3, 0.15, 5.5], P("worried", { side: 1, acc: ["goldbag", "sweat"] }))]), (t) => <><DREAM t={t} />{t > at("S01", 7, 8) && <Bubble t={t} at={at("S01", 7, 8)} x={1040} y={110} w={760} tail="r" text="Vàng không ăn được, tôi chỉ đổi gạo lấy thuốc thôi." />}</>)],
    [9, () => D3(S("room", "roomdim", [[1.3, 1.25, 2.6], [1.56, 0.95, 0.9], 40], [[1.4, 1.2, 2.2], [1.56, 0.95, 0.9], 34], [C("quang", [1.56, 0.4, 0.9], seq([[0, "shock"], [1.6, "worried"]], { mode: "sit", acc: ["sweat"] }))], { shake: 0.6, chat: "off", game: false }), (t) => <ClockTag t={t} text={t > at("S01", 9, 10) ? "23:00 · 12/11" : "…"} />)],
    [12, () => CD((t) => <AlertCard t={t} title="CẢNH BÁO HẠT NHÂN" body="Hãy tìm nơi trú ẩn ngay lập tức." time="23:00" />)],
    [13, () => CD((t) => <PhoneCard t={t} hue="red" time="23:02" date="Ứng dụng chứng khoán" notifs={[{ app: "Lệnh bán", col: "#b3131f", title: "Đặt lệnh BÁN toàn bộ danh mục", body: "FPT · VCB · HPG · VNM – tổng 1,2 tỷ đồng", at: 0.3 }]} quote={["BÁN SẠCH", "1,2 TỶ"]} qAt={1.0} />)],
    [14, () => D3(S("room", "roomdim", [[1.2, 1.3, 2.4], [1.56, 1.0, 0.9], 38], [[1.2, 1.3, 2.4], [1.56, 1.0, 0.9], 38], [C("quang", [1.56, 0.4, 0.9], P("worried", { mode: "sit", acc: ["phone", "glow"] }))], { chat: "off", game: false }), (t) => <><BigText t={t} at={0.2} text="CHỈ LÀ GIẤC MƠ" col="#ffffff" y={90} size={96} />{t > at("S01", 14, 16) && <BigText t={t} at={at("S01", 14, 16)} text="LỆNH BÁN LÀ THẬT" col="#ff4d5e" y={230} size={110} />}</>)],
  ] },
  { id: "S02", shots: [[0, () => CD((t) => <TitleCard t={t} kicker="THẾ GIỚI ĐANG CHUẨN BỊ CHO" l1="CHIẾN TRANH" l2="HẠT NHÂN?" sub="Và tiền của bạn nên làm gì · Chuyện Quang Hà" />)]] },
  { id: "S03", shots: [
    [0, () => D3(S("streetday", "morning", ...two(HX + 0.6), [C("c3", [HX + 2.0, 0.15, 5.6], P("laugh", { side: 1, wave: 0.8 })), C("quang", [HX - 0.2, 0.15, 5.3], P("nervous", { side: -1 }))]), (t) => <><LocTag t={t} l1="PHỐ LÒ ĐÚC – HÀ NỘI" l2="1 tuần trước" />
      {t > at("S03", 0, 1) + 2.2 && <Bubble t={t} at={at("S03", 0, 1) + 2.2} x={140} y={130} w={520} text="Quang Hà ơi!" />}{t > at("S03", 0, 1) + 5.0 && <Bubble t={t} at={at("S03", 0, 1) + 5.0} x={1160} y={300} w={560} tail="r" text="Có sao không em?" />}</>)],
    [2, () => D3(S("room", "room", [[0.95, 1.4, 1.8], [0.9, 1.3, 0.4], 36], [[0.92, 1.38, 1.5], [0.9, 1.3, 0.4], 32], [C("quang", [0.9, 0, 0.4], P("neutral", { acc: ["glasses"], prop: "type" }))], { chat: "off", game: false }), (t) => <LocTag t={t} l1="QUANG HÀ – KẾ TOÁN" l2="5 năm mua đều cổ phiếu, không vay" />)],
    [4, () => CD((t) => { const b = at("S03", 4, 4); const R: [string, number, string, number][] = [["FPT", 600, "#f26a21", b + 2.6], ["VCB", 300, "#2b9a5a", b + 4.6], ["HPG", 150, "#2f6fd1", b + 6.4], ["VNM", 150, "#8a5ac9", b + 8.0]];
      return <AbsoluteFill style={{ fontFamily: F, padding: "80px 150px" }}><Bg t={t} hue="navy" />
        <div style={{ position: "relative", display: "flex", alignItems: "baseline" }}><div style={{ fontSize: 62, fontWeight: 900, color: "#fff" }}>Danh mục tích sản 5 năm của Quang</div><div style={{ marginLeft: "auto", fontSize: 96, fontWeight: 900, color: "#ffd23f" }}>1,2 tỷ</div></div>
        <div style={{ position: "relative", marginTop: 40, display: "flex", flexDirection: "column", gap: 26 }}>{R.map(([n, v, c, a0], i) => { const k = sm((t - a0) / 0.6); return <div key={i} style={{ display: "flex", alignItems: "center", gap: 30, opacity: Math.min(1, k * 3) }}>
          <div style={{ width: 190, fontSize: 76, fontWeight: 900, color: "#fff" }}>{n}</div>
          <div style={{ height: 84, width: 1000 * (v / 600) * k, background: c, borderRadius: 14 }} />
          <div style={{ fontSize: 64, fontWeight: 900, color: c }}>{v} triệu</div></div>; })}</div>
        <div style={{ position: "absolute", left: 150, bottom: 170, fontSize: 30, color: "#9aa3bd", fontWeight: 600 }}>Mua đều mỗi tháng · không vay</div></AbsoluteFill>; })],
    [5, () => D3(S("streetday", "golden", ...two(HX + 0.6), [C("trang", [HX + 1.3, 0.15, 5.4], P("smile", { side: 1, acc: ["box"] })), C("quang", [HX - 0.2, 0.15, 5.3], P("smile", { side: -1 }))]), (t) => <><LocTag t={t} l1="TRANG TRÂU" l2="Bình Ngọc – Móng Cái · cao 1m47 · buôn hàng biên giới" />{t > at("S03", 5, 6) && <Bubble t={t} at={at("S03", 5, 6)} x={160} y={120} w={720} text="Số tiền này là để mua nhà cho con." />}</>)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(S("room", "room", ...roomTwo, [C("quang", [0.3, 0, 0.6], P("neutral", { side: 1 })), C("tai", [1.3, 0, 0.6], P("shock", { side: -1, acc: ["phone"], anim: true }))], { chat: "off", game: false }), (t) => <><LocTag t={t} l1="ÂN HỮU TÀI" l2="Mê game, tin TikTok nhất xóm" /><Bubble t={t} at={4.0} x={1000} y={110} w={800} tail="r" text="Anh ơi, 13/11 là tận thế, có bài báo khoa học đàng hoàng!" /></>)],
    [1, () => CD((t) => <PhoneCard t={t} hue="red" time="21:40" date="TikTok · Dành cho bạn" notifs={[{ app: "TikTok", col: "#111", title: "\"13/11/2026 – NGÀY TẬN THẾ?\"", body: "1,2 triệu lượt xem · \"có bài báo khoa học năm 1960\"", at: 0.2 }]} quote={["13/11", "TẬN THẾ?"]} qAt={0.6} />)],
    [2, () => D3(S("room", "room", ...roomTwo, [C("quang", [0.3, 0, 0.6], P("shock", { side: 1, acc: ["sweat"] })), C("tai", [1.3, 0, 0.6], P("grin", { side: -1, acc: ["phone"], wave: 0.6 }))], { chat: "off", game: false }), (t) => <><Bubble t={t} at={0.1} x={140} y={130} w={560} text="Có sao không em?" /><Bubble t={t} at={0.9} x={1040} y={330} w={760} tail="r" text="Video này 1 triệu lượt xem rồi anh ạ!" /></>)],
  ] },
  { id: "S05", shots: [
    [0, () => D3(S("room", "roomdim", [[0.8, 1.45, 1.4], [0.6, 1.32, -0.2], 40], [[0.75, 1.42, 1.15], [0.6, 1.32, -0.2], 36], [C("quang", [0.6, 0, -0.2], P("worried", { acc: ["phone", "glow"] }))], { chat: "off", game: false }), (t) => <BigText t={t} at={at("S05", 0, 1)} text="KHÔNG PHẢI TIN ĐỒN" col="#ffd23f" y={90} size={92} />)],
    [2, () => CD((t) => <DoomClock t={t} />)],
    [3, () => CD((t) => <Article t={t} src="NPR" srcCol="#1a1a1a" cat="Thế giới" date="04/02/2026" head="Lần đầu sau nhiều thập kỷ, Mỹ và Nga không còn giới hạn vũ khí hạt nhân" quote="Hiệp ước New START – thỏa thuận kiểm soát vũ khí hạt nhân cuối cùng giữa hai nước – đã hết hạn ngày 5/2/2026." tail="Dịch ý từ bản gốc tiếng Anh" hiAt={1.2} />)],
    [5, () => CD((t) => <Article t={t} src="REUTERS" srcCol="#ff8000" cat="Anh Quốc" date="23/10/2026" head="Anh khuyên mọi gia đình trữ nước, đồ ăn và tiền mặt đủ dùng 3 ngày" quote="Chiến dịch “Be Ready”: chuẩn bị cho mất điện, tấn công mạng, thời tiết cực đoan." tail="Nguồn: gov.uk, Reuters (The National dẫn lại) – dịch ý" hiAt={1.0} />)],
    [6, () => CD((t) => <Article t={t} src="NEWSWEEK" srcCol="#d71920" cat="Quốc phòng Mỹ" date="26/10/2026" head="Kế hoạch FORTRESS: căn cứ quân sự Mỹ phải tự trụ 90 ngày" quote="Các căn cứ lớn phải tự lo điện, nhiên liệu, đạn dược, thuốc men – không cần tiếp tế từ bên ngoài." tail="Theo Fox News, Newsweek đưa lại – dịch ý" hiAt={1.0} />)],
    [7, () => D3(S("room", "roomdim", [[0.75, 1.42, 1.0], [0.6, 1.36, -0.2], 30], [[0.72, 1.4, 0.85], [0.6, 1.36, -0.2], 26], [C("quang", [0.6, 0, -0.2], P("shock", { acc: ["phone", "glow", "sweat"], anim: true }))], { shake: 0.7, chat: "off", game: false }), (t) => <Vignette k={0.6} col="40,0,0" />)],
  ] },
  { id: "S06", shots: [
    [0, () => D3(S("streetday", "day", [[TS + 11, 2.4, 1.6], [TS + 7, 1.0, 5.9], 46], [[TS + 10, 2.0, 2.2], [TS + 7, 1.0, 5.9], 42], [C("tu", [TS + 5.2, 0.48, 5.72], P("grin", { mode: "sit", acc: ["cup"] })), C("c8", [TS + 8.6, 0.48, 5.72], P("laugh", { mode: "sit" })), C("cuong", [TS + 7.2, 0.15, 5.4], P("laugh", { wave: 0.9, acc: ["sweat"], anim: true })), C("quang", [TS + 6.2, 0.15, 5.4], P("nervous"))]), (t) => <><LocTag t={t} l1="CƯỜNG SOCIU" l2="98 ký · vừa đánh pickleball về" /><Bubble t={t} at={4.6} x={240} y={110} w={760} text="Tận thế thì phải ăn cho sướng, hôm nay anh bao cả quán!" /></>)],
    [1, () => D3(S("streetday", "day", [[TS + 5.6, 1.35, 3.2], [TS + 5.6, 1.0, 5.6], 38], [[TS + 5.6, 1.33, 3.5], [TS + 5.6, 1.0, 5.6], 34], [C("tu", [TS + 5.2, 0.48, 5.72], seq([[0, "laugh"], [3.0, "neutral"]], { mode: "sit", acc: ["cup"] })), C("quang", [TS + 6.2, 0.15, 5.4], P("worried", { side: 1 }))]), (t) => <>
      <Bubble t={t} at={1.2} x={1060} y={110} w={720} tail="r" text="Năm 62 bác cũng nghe bảo sắp tận thế rồi đấy." />
      {t > at("S06", 1, 2) && <Bubble t={t} at={at("S06", 1, 2)} x={160} y={330} w={620} text="Thế hồi đấy có sao không bác?" />}
      {t > at("S06", 1, 3) && <Bubble t={t} at={at("S06", 1, 3)} x={1000} y={360} w={780} tail="r" text="Có, cả xóm hoảng, bán cả trâu đi mua muối." />}</>)],
  ] },
  { id: "S07", shots: [
    [0, () => D3(S("room", "room", [[0.6, 1.45, 2.6], [0.6, 1.3, 0.4], 36], [[0.6, 1.43, 2.2], [0.6, 1.3, 0.4], 32], [C("linh", [0.6, 0, 0.4], P("laugh", { acc: ["phone", "mic"], wave: 0.7, anim: true }))]), (t) => <><LiveHud t={t} viewers={12480} /><LocTag t={t} l1="LINH LIVESTREAM" l2="Bán “combo sinh tồn”" />
      <div style={{ position: "absolute", left: 90, bottom: 190, fontFamily: F, background: "rgba(255,255,255,.95)", borderRadius: 22, padding: "22px 30px", width: 760, opacity: Math.min(1, (t - 1.5) / 0.4) }}>
        <div style={{ fontSize: 34, fontWeight: 900, color: "#b3131f" }}>COMBO SINH TỒN · 9.900.000đ</div>
        <div style={{ fontSize: 30, fontWeight: 700, color: "#222", marginTop: 6 }}>Mì tôm · nước · đèn pin · đài · 1 vỉ viên i-ốt</div>
        {t > at("S07", 0, 1) && <div style={{ fontSize: 34, fontWeight: 900, color: "#e62117", marginTop: 8 }}>⏰ CHỈ CÒN 10 SUẤT!</div>}</div></>)],
    [2, () => CD((t) => <PhoneCard t={t} hue="night" time="21:58" date="Đơn hàng" notifs={[{ app: "Đặt hàng", col: "#e62117", title: "Đã đặt 3 × Combo sinh tồn", body: "Tổng: 29.700.000đ · Giao trong 24h", at: 0.2 }]} quote={["3 COMBO", "29,7 TRIỆU"]} qAt={0.7} />)],
    [3, () => CD((t) => <PaperCard t={t} kind="receipt" hue="red" title="LƯU Ý VỀ VIÊN I-ỐT (KI)" sub="Theo khuyến cáo của Tổ chức Y tế Thế giới (WHO)" lines={[{ text: "Là THUỐC, không phải thực phẩm", at: 0.3, big: true }, { text: "Chỉ uống khi cơ quan y tế hướng dẫn", at: 1.0, big: true, col: "#d8212f" }, { text: "Tự uống có thể gây hại – nhất là người có bệnh tuyến giáp", at: 1.8 }]} />)],
  ] },
  { id: "S08", shots: [
    [0, () => D3(S("room", "room", ...roomTwo, [C("trang", [1.3, 0, 0.6], P("shock", { side: -1 })), C("quang", [0.3, 0, 0.6], P("nervous", { side: 1, acc: ["box"] }))], { chat: "off", game: false }), (t) => <>
      {t > at("S08", 0, 1) && <Bubble t={t} at={at("S08", 0, 1)} x={1000} y={110} w={760} tail="r" text="Anh mua 3 thùng mì gần 30 triệu à?" />}
      {t > at("S08", 0, 2) && <Bubble t={t} at={at("S08", 0, 2)} x={140} y={300} w={560} text="Phòng thân thôi em." />}</>)],
    [3, () => D3(S("room", "room", [[1.0, 1.4, 2.4], [1.3, 1.2, 0.6], 34], [[1.05, 1.38, 2.1], [1.3, 1.2, 0.6], 30], [C("trang", [1.3, 0, 0.6], P("stern", { side: -1 }))], { chat: "off", game: false }), (t) => <Bubble t={t} at={0.3} x={940} y={110} w={860} tail="r" text="Ở Móng Cái, tuần nào chẳng có tin đồn đóng cửa khẩu. Ai hoảng là người đầu tiên bán rẻ hàng của mình." />)],
  ] },
  { id: "S09", shots: [
    [0, () => D3(S("streetday", "day", [[TS + 3.4, 1.5, 2.6], [TS + 2.4, 1.15, 5.6], 42], [[TS + 3.1, 1.45, 3.1], [TS + 2.4, 1.15, 5.6], 38], [C("huy", [TS + 2.0, 0.48, 5.72], P("stern", { mode: "sit", acc: ["glasses", "cup"] })), C("quang", [TS + 3.2, 0.15, 5.45], P("worried", { side: -1 }))]), (t) => <><LocTag t={t} l1="HUY NGUYỄN" l2="Ít nói, hay hỏi về rủi ro" />{t > at("S09", 0, 1) && <Bubble t={t} at={at("S09", 0, 1)} x={1000} y={110} w={800} tail="r" text="Nếu không có chiến tranh, anh bán cổ phiếu rồi định mua lại ở đâu?" />}</>)],
    [4, () => CD((t) => <HistoryCard t={t} items={[{ yr: "1962", name: "Khủng hoảng tên lửa Cuba", note: "Chứng khoán Mỹ giảm mạnh, hồi lại sau vài tháng", at: 0.2 }, { yr: "2001", name: "Sự kiện 11/9", note: "Sàn Mỹ đóng cửa 4 ngày, giảm sâu, rồi hồi lại", at: at("S09", 4, 5) }, { yr: "2022", name: "Xung đột Nga – Ukraine", note: "Dầu, vàng tăng vọt rồi hạ nhiệt", at: at("S09", 4, 6) }]} />)],
    [7, () => D3(S("streetday", "day", [[TS + 2.2, 1.3, 3.8], [TS + 2.0, 1.05, 5.72], 32], [[TS + 2.2, 1.28, 4.1], [TS + 2.0, 1.05, 5.72], 28], [C("huy", [TS + 2.0, 0.48, 5.72], P("neutral", { mode: "sit", acc: ["glasses"] }))]), (t) => <BigText t={t} at={0.4} text="BÁN TRONG HOẢNG LOẠN = MẤT NHIỀU NHẤT" col="#ffd23f" y={90} size={70} />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(S("room", "roomdim", [[1.3, 1.25, 2.6], [1.56, 0.95, 0.9], 40], [[1.4, 1.2, 2.2], [1.56, 0.95, 0.9], 34], [C("quang", [1.56, 0.4, 0.9], P("sleepy", { mode: "sit", acc: ["phone"] }))], { chat: "off", game: false }), (t) => <ClockTag t={t} text="Đêm 12/11" />)],
    [2, () => D3(S("photo", "night", ...fixed([0, 1.6, -8], [0, 1.9, 6], 46), [], { bg: "hn/hanoi_night.jpg", bgFit: [0.6, 0.45], shake: 0.5 }), (t) => <><Flash t={t} at={0.3} /><DREAM t={t} /></>)],
    [3, () => CD((t) => <AlertCard t={t} title="CẢNH BÁO HẠT NHÂN" body="Hãy tìm nơi trú ẩn ngay lập tức." time="23:00" fake={at("S10", 3, 7) - 0.2} />)],
    [5, () => CD((t) => <PhoneCard t={t} hue="red" time="23:05" date="Ứng dụng chứng khoán" notifs={[{ app: "Lệnh chờ", col: "#b3131f", title: "BÁN toàn bộ: FPT · VCB · HPG · VNM", body: "Chờ phiên sáng 13/11", at: 0.2 }, { app: "Điện thoại", col: "#2b9a5a", title: "Đang gọi: Em trai", body: "“Cho anh vay 300 triệu, mai trả…”", at: at("S10", 5, 6) }]} quote={["VAY 300 TRIỆU", "MUA VÀNG"]} qAt={at("S10", 5, 6) + 0.8} />)],
    [9, () => CD((t) => <Article t={t} src="CARNEGIE" srcCol="#0f3d6b" cat="Proliferation News" date="05/11/2026" head="App báo động ở Ukraine và Nga bị hack, gửi cả cảnh báo hạt nhân giả" quote="Người dùng nhận được các cảnh báo giả mạo, trong đó có cảnh báo hạt nhân." tail="Dịch ý từ bản tổng hợp tin tiếng Anh" hiAt={0.8} />)],
    [10, () => D3(S("street", "night", [[HX - 4, 1.4, 2.0], [HX + 1, 1.0, 5.2], 44], [[HX + 2, 1.4, 2.0], [HX + 5, 1.0, 5.2], 44], [C("quang", [HX - 2, 0.15, 5.2], (t: number) => ({ ...P("worried", { acc: ["sweat"] })(t), mode: "stroll", phase: (t * 1.4) % 1, side: -1 }), [HX + 4, 0.15, 5.2])], { ease: "lin" }), (t) => <ClockTag t={t} text="00:00" />)],
  ] },
  { id: "S11", shots: [
    [0, () => D3(S("photo", "dawn", [[0.4, 1.5, -5.6], [0.4, 1.3, 2.2], 44], [[0.2, 1.48, -5.0], [0.4, 1.3, 2.2], 42], [...queue(9), C("quang", [3.9, 0, 2.9], P("worried", { acc: ["sweat"] }))], { bg: "hn/gold_shop.jpg", bgFit: [0.35, 0.55] }), (t) => <LocTag t={t} l1="6 GIỜ SÁNG · 13/11" l2="Xếp hàng trước tiệm vàng" />)],
    [2, () => CD((t) => <GoldBoard t={t} date="Sáng 13/11/2026" rows={[{ name: "Vàng miếng SJC", buy: "135", sell: "138", at: 0.3 }]} spread={"Mua 2 lượng: 276 triệu · Bán lại ngay: mất 6 triệu"} spreadAt={at("S11", 2, 4) - 0.2} />)],
  ] },
  { id: "S12", shots: [
    [0, () => CD((t) => { const b = at("S12", 0, 2); return <BoardCard t={t} title="BẢNG ĐIỆN HOSE · DANH MỤC CỦA QUANG" time="09:00 · 13/11/2026" rows={[{ sym: "FPT", ref: 49550, px: 49100, vol: "600 tr", at: b }, { sym: "VCB", ref: 53900, px: 53600, vol: "300 tr", at: at("S12", 0, 3) }, { sym: "HPG", ref: 21050, px: 21000, vol: "150 tr", at: at("S12", 0, 4) }, { sym: "VNM", ref: 54200, px: 53500, vol: "150 tr", at: at("S12", 0, 5) }]} note="Lệnh thị trường → khớp đúng vùng giá thấp nhất phiên" noteAt={at("S12", 0, 1) + 0.5} />; })],
    [6, () => CD((t) => <BoardCard t={t} title="ĐÓNG CỬA PHIÊN 13/11 – TIỀN BẮT ĐÁY VÀO" time="14:45" idx={{ name: "VN-Index", v: "1.734,93", ch: "+0,18", col: "#2fd36b" }} rows={[{ sym: "FPT", ref: 49550, px: 50100, vol: "Quang bán 49,10", at: at("S12", 6, 7) }, { sym: "VCB", ref: 53900, px: 53800, vol: "Quang bán 53,60", at: at("S12", 6, 7) + 0.3 }, { sym: "HPG", ref: 21050, px: 21050, vol: "Quang bán 21,00", at: at("S12", 6, 7) + 0.6 }, { sym: "VNM", ref: 54200, px: 53600, vol: "Quang bán 53,50", at: at("S12", 6, 7) + 0.9 }]} note="Mất gần 17 triệu so với giá đóng cửa (gồm phí + thuế)" noteAt={at("S12", 6, 8)} />)],
    [9, () => D3(S("room", "roomdim", [[0.8, 1.45, 1.4], [0.6, 1.32, -0.2], 40], [[0.75, 1.42, 1.15], [0.6, 1.32, -0.2], 36], [C("quang", [0.6, 0, -0.2], P("sad", { acc: ["phone"] }))], { chat: "off", game: false }), (t) => <BigText t={t} at={0.6} text="5 NĂM TÍCH SẢN → TIỀN MẶT" col="#ffd23f" y={90} size={86} />)],
  ] },
  { id: "S13", shots: [
    [0, () => D3(S("street", "night", [[TS + 11, 2.2, 1.8], [TS + 7, 1.0, 5.9], 46], [[TS + 10, 1.9, 2.4], [TS + 7, 1.0, 5.9], 42], [C("tu", [TS + 5.2, 0.48, 5.72], P("grin", { mode: "sit", acc: ["cup"] })), C("cuong", [TS + 7.2, 0.15, 5.4], P("grin", { acc: ["cup"] })), C("tai", [TS + 8.4, 0.15, 5.4], P("nervous", { acc: ["phone"] })), C("quang", [TS + 6.2, 0.15, 5.4], P("worried", { acc: ["sweat"] })), C("c8", [TS + 8.6, 0.48, 5.72], P("neutral", { mode: "sit" })), C("c5", [TS + 9.6, 0.15, 5.6], P("nervous"))]), (t) => { const b = at("S13", 0, 1); const nums = ["10", "9", "…", "3", "2", "1"]; const k = Math.floor((t - b) / 0.35); return <>{t > b && k < nums.length ? <BigText t={t} at={b + k * 0.35} text={nums[Math.max(0, k)]} col="#ffd23f" y={260} size={260} /> : null}{t > at("S13", 0, 2) && <BigText t={t} at={at("S13", 0, 2)} text="00:00 · KHÔNG GÌ XẢY RA" col="#ffffff" y={90} size={80} />}</>; })],
    [5, () => D3(S("street", "night", ...two(TS + 7.8, 5.4, 3.6), [C("tai", [TS + 8.4, 0.15, 5.4], P("grin", { side: -1, acc: ["phone"] })), C("quang", [TS + 7.2, 0.15, 5.4], P("sad", { side: 1 }))]), (t) => <><Bubble t={t} at={0.2} x={160} y={110} w={640} text="Chắc lệch múi giờ anh ạ." />{t > at("S13", 5, 7) && <BigText t={t} at={at("S13", 5, 7)} text="CHỈ QUANG KHÔNG CƯỜI" col="#ff4d5e" y={640} size={80} />}</>)],
  ] },
  { id: "S14", shots: [
    [0, () => CD((t) => { const b = (j: number) => at("S14", 0, j); return <PaperCard t={t} kind="note" hue="warm" title="SỔ GHI CHÉP NHÀ MÌNH" sub="Trang ghi · sáng 14/11/2026" lines={[{ text: "Bán cổ phiếu ở giá thấp nhất phiên: −17 triệu", at: b(1) }, { text: "Chênh lệch mua – bán vàng: −6 triệu", at: b(2) }, { text: "3 combo sinh tồn: −29,7 triệu", at: b(3) }, { text: "NỢ EM TRAI: 300 TRIỆU", at: b(4), big: true, col: "#d8212f", under: true }]} stamp={{ text: "THIỆT HƠN 52 TRIỆU", at: b(5) }} />; })],
    [6, () => D3(S("room", "room", ...roomTwo, [C("trang", [1.3, 0, 0.6], P("sad", { side: -1, acc: ["paper"] })), C("quang", [0.3, 0, 0.6], P("sad", { side: 1, headTilt: 6 }))], { chat: "off", game: false }), (t) => <Bubble t={t} at={0.2} x={980} y={110} w={820} tail="r" kind="whisper" text="Anh sợ chiến tranh. Nhưng anh làm nhà mình thiệt trước cả chiến tranh." />)],
  ] },
  { id: "S15", shots: [
    [0, () => D3(S("room", "room", ...roomTwo, [C("huy", [1.3, 0, 0.6], P("neutral", { side: -1, acc: ["glasses"] })), C("quang", [0.3, 0, 0.6], P("sad", { side: 1 }))], { chat: "off", game: false }), (t) => <>{t > at("S15", 0, 1) && <Bubble t={t} at={at("S15", 0, 1)} x={140} y={110} w={560} text="Em ơi, anh sai ở đâu?" />}{t > at("S15", 0, 2) && <Bubble t={t} at={at("S15", 0, 2)} x={1060} y={300} w={640} tail="r" text="Chuẩn bị không sai." />}</>)],
    [3, () => CD((t) => <Article t={t} src="GOV.UK" srcCol="#0b0c0c" cat="Be Ready" date="22/10/2026" head="Mỗi gia đình nên chuẩn bị cho 3 ngày gián đoạn" quote="Phòng mất điện, tấn công mạng, thời tiết cực đoan: nước, đồ ăn khô, đèn pin, đài pin, một ít tiền mặt." tail="Không khuyên bán tháo tài sản – dịch ý" hiAt={0.6} />)],
    [5, () => CD((t) => <><GoldBoard t={t} dream shop="NHỚ LẠI GIẤC MƠ" date="" rows={[{ name: "Vàng 1 lượng", buy: "—", sell: "1.000", at: 0 }]} spread="…nhưng KHÔNG đổi được bao gạo" spreadAt={at("S15", 5, 6) + 0.6} /><DREAM t={t} /></>)],
    [7, () => D3(S("room", "room", [[1.0, 1.4, 2.4], [1.3, 1.2, 0.6], 34], [[1.05, 1.38, 2.1], [1.3, 1.2, 0.6], 30], [C("huy", [1.3, 0, 0.6], P("smile", { side: -1, acc: ["glasses"] }))], { chat: "off", game: false }), (t) => <BigText t={t} at={0.6} text="NƯỚC · THUỐC · TIỀN MẶT · HÀNG XÓM" col="#ffd23f" y={90} size={72} />)],
  ] },
  { id: "S16", shots: [[0, () => CD((t) => <LessonCard t={t} title="4 dòng Huy viết cho Quang" items={[
    { n: "1", icon: "🏦", head: "Quỹ dự phòng 3–6 tháng chi tiêu", body: "Có một phần tiền mặt để ở nhà", at: at("S16", 0, 1) },
    { n: "2", icon: "🚫", head: "Không vay để chạy theo tin đồn", body: "Vay để mua vàng lúc hoảng = lỗ chắc", at: at("S16", 0, 2) },
    { n: "3", icon: "📝", head: "Viết sẵn kế hoạch cho ngày hoảng loạn", body: "Lúc đầu còn lạnh – đến lúc ấy chỉ việc làm theo", at: at("S16", 0, 3) },
    { n: "4", icon: "🔎", head: "Kiểm tin chính thức, chờ 1 đêm", body: "Rồi mới quyết định bán", at: at("S16", 0, 4) }]} />)]] },
  { id: "S17", shots: [
    [0, () => D3(S("streetday", "morning", [[HX - 4, 1.4, 2.0], [HX + 1, 1.0, 5.2], 44], [[HX + 1, 1.4, 2.0], [HX + 4, 1.0, 5.2], 44], [C("quang", [HX - 1.5, 0.15, 5.2], (t: number) => ({ ...P("smile_closed", { acc: ["box"] })(t), mode: "stroll", phase: (t * 1.1) % 1, side: -1 }), [HX + 3.5, 0.15, 5.2])], { ease: "lin" }), (t) => <LocTag t={t} l1="TUẦN SAU" l2="Bán 2 lượng vàng trả em · tặng 3 thùng combo cho trường mầm non" d={6} />)],
    [2, () => CD((t) => <PlanCard t={t} />)],
  ] },
  { id: "S18", shots: [[0, () => D3(S("photo", "night", [[0, 1.6, -8], [0, 1.9, 6], 46], [[0, 1.6, -7], [0, 1.9, 6], 44], [], { bg: "hn/hanoi_night.jpg", bgFit: [0.6, 0.45], ease: "sm" }), (t) => <><BigText t={t} at={at("S18", 0, 1)} text="CHUẨN BỊ MỘT CÁI ĐẦU LẠNH" col="#ffd23f" y={400} size={108} /></>)]] },
  { id: "S19", shots: [[0, () => CD((t) => <TitleCard t={t} kicker="CÂU HỎI CHO BẠN" l1="ĐÊM 12/11" l2="BẠN CÓ NHẬN TIN ĐỒN?" sub="Kể cho mình nghe ở phần bình luận nhé" hue="navy" />)]] },
  { id: "S20", shots: [[0, () => CD((t) => <HnCta t={t} webAt={2.4} />)]] },
];

function teaStall() { return [] as Cast[]; }
const Meme: React.FC<{ t: number; at?: number; top: string; bot: string; small?: boolean; noSubGap?: boolean; y?: number }> = ({ t, at = 0, top, bot, small, noSubGap, y }) => { if (t < at) return null; const a = Math.min(1, (t - at) / 0.18), sz = small ? 150 : 92;
  const st = { position: "absolute", left: 0, width: 1920, textAlign: "center", fontFamily: F, fontWeight: 900, fontSize: sz, color: "#fff", WebkitTextStroke: "10px #000", paintOrder: "stroke fill", letterSpacing: 1, transform: `scale(${1.25 - 0.25 * a})`, opacity: a } as React.CSSProperties;
  return <>{top && <div style={{ ...st, top: 70 }}>{top}</div>}{bot && <div style={{ ...st, top: y ?? (small ? 690 : noSubGap ? 175 : 620), color: small ? "#ffe14d" : "#fff", fontSize: small ? 130 : sz }}>{bot}</div>}</>; };


const HnCta: React.FC<{ t: number; webAt: number }> = ({ t, webAt }) => { const a = sm(t / 0.5), w = sm((t - webAt) / 0.45), clickT = t - webAt - 7.2, sub = clickT > 0.35;
  return <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><Bg t={t} hue="navy" />
    <div style={{ position: "relative", opacity: a }}>
      <div style={{ fontSize: 58, fontWeight: 800, color: "#fff" }}>Kế hoạch tài chính cho gia đình khi có khủng hoảng</div>
      <div style={{ marginTop: 50, opacity: w, transform: `scale(${0.9 + 0.1 * w})` }}>
        <div style={{ fontSize: 40, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>HỌC MIỄN PHÍ TẠI</div>
        <div style={{ fontSize: 96, fontWeight: 900, color: "#fff", marginTop: 8 }}>chungkhoanhuynguyen.com</div>
        <div style={{ display: "flex", gap: 30, justifyContent: "center", marginTop: 34 }}>{["Quỹ dự phòng bao nhiêu là đủ?", "Chia vốn thế nào?", "Khi nào KHÔNG được bán?"].map((s, i) => <div key={i} style={{ padding: "18px 30px", borderRadius: 18, background: "rgba(255,255,255,.1)", border: "2px solid rgba(255,255,255,.25)", color: "#dfe5f2", fontSize: 36, fontWeight: 700, opacity: sm((t - webAt - 0.6 - i * 0.35) / 0.4) }}>{s}</div>)}</div>
        <div style={{ display: "inline-block", marginTop: 44, padding: "22px 60px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 46, fontWeight: 900 }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI KÊNH"}</div>
      </div></div>
    {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 1080 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 900 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
    <div style={{ position: "absolute", right: 40, bottom: 20, fontSize: 22, color: "rgba(255,255,255,.55)" }}>Quan điểm cá nhân, không phải khuyến nghị đầu tư · Ảnh: Wikimedia Commons (CC BY / CC BY-SA)</div>
  </AbsoluteFill>; };
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
export const HN_FRAMES = TOTAL_F;
export const HnVideo: React.FC = () => {
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
