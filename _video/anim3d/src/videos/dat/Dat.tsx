// Phim 3D #2 "Hùng Xa Lộ đu đỉnh đất nền". Khung 1920x1080, 30 fps.
// Mỗi câu thoại có mốc thời gian thật (timing.json do giọng Huy70_HaiDang30 đọc) → cắt cảnh đúng câu, phụ đề đúng chữ.
import React, { useEffect, useState } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, staticFile, delayRender, continueRender, Audio, getInputProps } from "remotion";
import { Stage, Shot3D, Run, SetKey, Cast, V } from "../vang/stage";
import { Pose, Acc } from "../vang/cast2";
import { Expr } from "../pho/toon";
import { GOLD_X, HOME_X } from "../vang/sets";
import { TIMING, FPS, TOTAL_F, TAIL, sc, subText, BAD, GOOD } from "./data";
import { F, sm, PhoneCard, PaperCard, ChatCard, TitleCard, LessonCard, SplitCard, EndCard, Bubble as B0, LocTag, BigText, ClockTag, Vignette, Bg } from "../vang/cards";

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

// Máy nhìn hướng +z nên +x nằm bên TRÁI màn: lật ngang mọi bóng thoại cho đúng người nói.
const Bubble: React.FC<React.ComponentProps<typeof B0>> = (p) => <B0 {...p} x={1920 - p.x - (p.w ?? 640)} tail={p.tail === "r" ? "l" : "r"} />;
// ---------- blocking ----------
const HUNG_F: V = [0.6, 0, 1.2];                      // Hùng đứng giữa lô đất cỏ cao
const HX = HOME_X + 3.6;                                // khoảng sân trước nhà, tránh xe máy dựng ở cửa
const HOMEP: V = [HX, 0.15, 5.3];                  // trước cửa nhà ở Thủy Nguyên (phố ban ngày)
const TS = (dx: number): V => [GOLD_X + dx, 0.15, 5.45]; // quán trà đá
const twoShot = (x: number, z = 5.3, d = 4.3, h = 1.5): [[V, V, number], [V, V, number]] => [[[x + 0.2, h, z - d], [x, 1.1, z], 40], [[x + 0.1, h - 0.05, z - d + 0.5], [x, 1.1, z], 37]];
const ride = (who: string, extra: Cast[] = [], e: Expr = "sad"): Cast[] => [C("bike", [HOME_X + 14, 0.15, 5.0], () => P("neutral")(0), [HOME_X + 2, 0.15, 5.0]), C(who, [HOME_X + 14.1, 0.62, 5.15], P(e, { mode: "sit", acc: ["helmet"] }), [HOME_X + 2.1, 0.62, 5.15]), ...extra];

const PLAN: Plan[] = [
  { id: "S01", shots: [
    [0, () => D3(S("field", "night", [[-7, 6, -11], [0.6, 1.0, 3], 50], [[-1.6, 1.9, -2.6], [0.6, 1.3, 1.2], 42], [C("hung", HUNG_F, P("worried", { acc: ["phone", "glow"] }))]), (t) => <><ClockTag t={t} text="02:00" /><LocTag t={t} l1="HIỆP HÒA – BẮC GIANG CŨ" l2="Một lô đất nền, 2 giờ sáng" d={4.5} /></>)],
    [2, () => D3(S("field", "night", [[0.9, 1.5, -0.6], [0.6, 1.45, 1.2], 32], [[0.8, 1.5, -0.3], [0.6, 1.45, 1.2], 28], [C("hung", HUNG_F, P("worried", { acc: ["phone", "glow", "sweat"], anim: true }))], { shake: 0.3 }))],
    [3, () => CD((t) => <PhoneCard t={t} hue="night" time="02:07" date="Thứ Bảy" notifs={[{ app: "Điện thoại", col: "#2b9a5a", title: "Thắng Cò Đất", body: "Đang gọi… (lần thứ 17)", at: 0.2 }, { app: "Tổng đài", col: "#b3131f", title: "Không liên lạc được", body: "Thuê bao quý khách vừa gọi tạm thời không liên lạc được.", at: 1.0 }]} quote={["THUÊ BAO", "KHÔNG LIÊN LẠC ĐƯỢC"]} qAt={1.6} />)],
    [4, () => D3(S("field", "night", [[3.2, 1.3, -1.8], [0.6, 1.3, 1.2], 40], [[2.4, 1.3, -1.2], [0.6, 1.3, 1.2], 36], [C("hung", HUNG_F, P("sad", { acc: ["phone"] }))]), (t) => <BigText t={t} at={0.4} text="HÙNG XA LỘ" col="#ffcf3a" y={110} size={120} />)],
    [5, () => CD((t) => <PaperCard t={t} kind="note" hue="night" title="5 NĂM Ở HÀN QUỐC" sub="Còn lại gì?" lines={[{ text: "1 lô đất nền 90 m² – không ai mua", at: 0.5 }, { text: "Nợ ngân hàng: 3 tỷ đồng", at: 1.4, big: true, col: "#d8212f" }]} side={<BigText t={t} at={2.2} text="" />} />)],
    [6, () => CD((t) => <PaperCard t={t} kind="receipt" hue="red" title="SỔ ĐỎ" sub="Nhà bố mẹ – Thủy Nguyên, Hải Phòng" lines={[{ text: "Tài sản bảo đảm khoản vay 3 tỷ", at: 0.6 }]} stamp={{ text: "ĐANG THẾ CHẤP", at: 1.3 }} />)],
  ] },
  { id: "S02", shots: [[0, () => CD((t) => <TitleCard t={t} kicker="VÌ SAO ĐU ĐỈNH ĐẤT NỀN" l1="CHÊNH 300 TRIỆU" l2="TRẢ CẢ CHỤC NĂM" sub="Chuyện Hùng Xa Lộ" />)]] },
  { id: "S03", shots: [
    [0, () => D3(S("streetday", "morning", [[HX - 9, 6, -1], [HX, 1.6, 5.3], 50], [[HX - 2.6, 1.6, 2.2], [HX, 1.3, 5.3], 42], [C("hung", HOMEP, P("grin", { wave: 0.8 }))]), (t) => <LocTag t={t} l1="THỦY NGUYÊN – HẢI PHÒNG" l2="Quê Hùng" />)],
    [1, () => D3(S("streetday", "morning", ...twoShot(HX + 1.2), [C("tu", [HX + 2.6, 0.15, 5.5], P("laugh", { wave: 0.9, side: -1 })), C("hung", [HX + 0.4, 0.15, 5.3], P("laugh", { side: 1 }))]), (t) => <><Bubble t={t} at={0.4} x={1080} y={140} w={620} tail="r" text="Hùng Xa Lộ ơi, lại phi đâu đấy?" /><Bubble t={t} at={2.4} x={180} y={330} w={680} text="Đời là xa lộ, cứ thế mà phi!" /></>)],
    [2, () => D3(S("street", "night", [[HX - 2.4, 1.5, 2.6], [HX, 1.3, 5.3], 40], [[HX - 1.8, 1.45, 3.1], [HX, 1.3, 5.3], 36], [C("hung", HOMEP, P("laugh", { acc: ["mic"], anim: true })), C("c3", [HX + 1.6, 0.15, 5.6], P("worried"))]), (t) => <Meme t={t} at={0.8} top="" bot="KARAOKE 12 GIỜ ĐÊM 🎤" small y={120} />)],
    [3, () => D3(S("korea", "room", [[-6, 2.2, 3.5], [-6.5, 1.4, -3], 46], [[-5.6, 1.9, 2.4], [-6.5, 1.4, -3], 42], [C("hung", [-5.8, 0, -2.0], P("stern", { acc: ["helmet", "sweat"], prop: "type" }))]), (t) => <LocTag t={t} l1="HÀN QUỐC" l2="Xưởng ép nhựa – 12 tiếng/ngày" />)],
    [5, () => D3(S("korea", "dawn", [[-2, 1.6, 10.5], [-1.5, 1.2, 15], 44], [[-1.8, 1.55, 11.2], [-1.5, 1.2, 15], 40], [C("hung", [-1.5, 0, 13.6], P("sad", { anim: true }))]), (t) => <BigText t={t} at={0.4} text="−10°C" col="#9fdcff" y={110} size={120} />)],
    [6, () => CD((t) => <PhoneCard t={t} hue="night" time="22:10" date="Gọi video về nhà" notifs={[{ app: "Gọi video", col: "#2f6fd1", title: "Mẹ", body: "Con khỏe lắm, bên này sướng lắm mẹ ạ!", at: 0.6 }]} quote={["NỬA LƯƠNG GỬI MẸ", "NỬA BỎ ỐNG"]} qAt={1.2} />)],
    [7, () => CD((t) => <PaperCard t={t} kind="receipt" hue="warm" title="TIẾT KIỆM 5 NĂM" sub="Hùng Xa Lộ" lines={[{ text: "1,5 TỶ ĐỒNG", at: 0.3, big: true, col: "#1d6b3a" }]} />)],
    [8, () => D3(S("streetday", "morning", ...twoShot(HX + 0.6), [C("mehung", [HX + 1.5, 0.15, 5.4], P("worried", { side: -1 })), C("hung", [HX - 0.3, 0.15, 5.3], P("grin", { side: 1 }))]), (t) => <><Bubble t={t} at={rel("S03", 9, sc("S03").sens[8].a) + 0.2} x={1060} y={130} w={680} tail="r" text="Về rồi thì kiếm việc gần nhà, gửi tiết kiệm cho chắc con ạ." />{t > rel("S03", 10, sc("S03").sens[8].a) && <Bubble t={t} at={rel("S03", 10, sc("S03").sens[8].a)} x={160} y={380} w={640} text="Gửi tiết kiệm thì bao giờ mới giàu hả mẹ!" />}</>)],
  ] },
  { id: "S04", shots: [
    [0, () => D3(S("streetday", "day", [[GOLD_X + 14, 2.8, 0.5], [GOLD_X + 7, 1.2, 5.9], 46], [[GOLD_X + 10, 1.9, 1.8], [GOLD_X + 6, 1.15, 5.9], 40], teaStall()), (t) => <BigText t={t} at={rel("S04", 1, sc("S04").a)} text="SẮP LÊN THÀNH PHỐ?!" col="#ffcf3a" y={110} size={100} />)],
    [2, () => D3(S("streetday", "day", [[GOLD_X + 5.9, 1.4, 3.2], [GOLD_X + 5.4, 1.15, 5.7], 38], [[GOLD_X + 5.8, 1.38, 3.6], [GOLD_X + 5.4, 1.15, 5.7], 34], teaStall("laugh")), (t) => <Bubble t={t} at={0.6} x={1000} y={130} w={760} tail="r" text="Thằng cháu tao mua đất Hiệp Hòa, một tuần chênh 300 triệu!" />)],
    [3, () => D3(S("streetday", "day", ...twoShot(GOLD_X + 20), [C("phu", [GOLD_X + 20, 0.15, 5.3], P("smug", { acc: ["phone"], anim: true })), C("c11", [GOLD_X + 21.5, 0.15, 5.6], P("shock", { side: -1 })), C("c13", [GOLD_X + 18.6, 0.15, 5.6], P("grin", { side: 1 }))]), (t) => <><LocTag t={t} l1="PHÚ DÊ GIÀ" l2="Beijing X7 – hay quay phim khoe" /><Bubble t={t} at={1.6} x={1000} y={130} w={640} tail="r" text="Anh vừa chốt 2 lô, Tết đổi Mẹc!" /></>)],
    [4, () => D3(S("streetday", "day", ...twoShot(GOLD_X + 19.4, 5.3, 3.3), [C("phu", [GOLD_X + 20.2, 0.15, 5.3], P("smug", { side: -1, wave: 0.6 })), C("hung", [GOLD_X + 18.6, 0.15, 5.3], P("nervous", { side: 1 }))]), (t) => <><Bubble t={t} at={0.2} x={1060} y={120} w={700} tail="r" text="Hùng Xa Lộ! Cầm tiền Hàn về mà để ngân hàng à?" />{t > rel("S04", 6, sc("S04").sens[4].a) && <Bubble t={t} at={rel("S04", 6, sc("S04").sens[4].a)} x={1000} y={380} w={760} tail="r" text="Đất chạy như xe trên xa lộ, chậm chân là ăn bụi!" />}</>)],
    [7, () => D3(S("street", "night", [[HX - 1.8, 1.5, 3.0], [HX, 1.35, 5.3], 38], [[HX - 1.4, 1.45, 3.5], [HX, 1.35, 5.3], 34], [C("hung", HOMEP, P("worried", { acc: ["phone", "glow"] }))]), (t) => <ClockTag t={t} text="01:30" />)],
    [8, () => CD((t) => <ChatCard t={t} title="Đất nền tăng trưởng 🔥 (2.814 thành viên)" msgs={[{ who: "Thắng Cò", text: "Lô góc vừa chốt, chênh 280 tr sau 5 ngày 💰", at: 0.3 }, { who: "Hà Đất Nền", text: "[Ảnh sổ đỏ] [Ảnh cọc tiền]", at: 1.2 }, { who: "Thắng Cò", text: "Đất không đẻ thêm, chỉ có người đẻ thêm!", at: 2.2 }]} />)],
  ] },
  { id: "S05", shots: [[0, () => CD((t) => <PaperCard t={t} kind="receipt" hue="navy" title="GIÁ RAO ĐỈNH – QUÝ IV/2025" sub="Đất nền vùng ven phía Bắc" lines={[{ text: "Mê Linh (KĐT Minh Giang Đầm Và): ~60 triệu/m²", at: rel("S05", 1, sc("S05").a) }, { text: "Hiệp Hòa – lô 90 m²: ~5,5 tỷ", at: rel("S05", 2, sc("S05").a), big: true }, { text: "Nguồn: VietnamFinance, CafeF dẫn giá rao Batdongsan (lô Hiệp Hòa ước từ mức giảm ~65,5%)", at: rel("S05", 2, sc("S05").a) + 0.8 }]} />)]] },
  { id: "S06", shots: [
    [0, () => D3(S("fieldfever", "golden", [[-30, 9, -16], [0, 1, 2], 52], [[-6, 3, -8], [0, 1.2, 0], 46], [...feverCrowd(), C("thang", [-1.4, 0, -2.6], walk("grin", { side: 1 }), [-0.2, 0, -2.6]), C("hung", [-2.4, 0, -2.6], walk("neutral", { side: 1 }), [-1.2, 0, -2.6])], { ease: "lin" }), (t) => <LocTag t={t} l1="PHIÊN ĐẤU GIÁ ĐẤT" l2="Tháng 12/2025" />)],
    [2, () => D3(S("fieldfever", "golden", ...twoShot(0, -2.6, 3.9), [C("thang", [0.5, 0, -2.6], P("smug", { side: -1 })), C("hung", [-0.5, 0, -2.6], P("nervous", { side: 1 }))]), (t) => <Bubble t={t} at={0.3} x={1040} y={130} w={700} tail="r" kind="whisper" text="Anh Hùng chốt luôn đi, mai là người khác cọc rồi!" />)],
    [3, () => D3(S("fieldfever", "golden", ...twoShot(0, -2.6, 3.2), [C("thang", [0.5, 0, -2.6], P("grin", { side: -1, wave: 0.7 })), C("hung", [-0.5, 0, -2.6], P("shock", { side: 1 }))], { shake: 0.5 }), (t) => <BigText t={t} at={0.3} text="5,5 TỶ → 7 TỶ?" col="#ffcf3a" y={110} size={120} />)],
    [4, () => D3(S("fieldfever", "golden", [[-4, 1.6, -6], [2, 1.2, -1], 48], [[3, 1.6, -6], [6, 1.2, -1], 48], feverCrowd(true), { ease: "lin" }))],
    [6, () => D3(S("fieldfever", "golden", [[-0.5, 1.45, -4.6], [-0.5, 1.4, -2.6], 30], [[-0.5, 1.45, -4.2], [-0.5, 1.4, -2.6], 26], [C("hung", [-0.5, 0, -2.6], P("nervous", { acc: ["sweat"], anim: true }))], { shake: 0.8 }), (t) => <><Vignette k={0.7} col="40,0,0" /><BigText t={t} at={0.4} text="SỢ LỠ TÀU" col="#ff4d5e" y={110} size={120} /></>)],
    [7, () => D3(S("fieldfever", "golden", ...twoShot(0, -2.6, 3.9), [C("thang", [0.5, 0, -2.6], seq([[0, "neutral"], [2.0, "laugh"]], { side: -1 })), C("hung", [-0.5, 0, -2.6], P("worried", { side: 1 }))]), (t) => <>
      <Bubble t={t} at={0.1} x={160} y={120} w={520} text="Sổ đỏ có chưa em?" />
      {t > rel("S06", 8, sc("S06").sens[7].a) && <Bubble t={t} at={rel("S06", 8, sc("S06").sens[7].a)} x={1060} y={120} w={700} tail="r" text="Đang làm, sắp có, cả làng ai chả mua thế!" />}
      {t > rel("S06", 9, sc("S06").sens[7].a) && <Bubble t={t} at={rel("S06", 9, sc("S06").sens[7].a)} x={160} y={340} w={640} text="Có đường, có trường, có chợ không?" />}
      {t > rel("S06", 10, sc("S06").sens[7].a) && <Bubble t={t} at={rel("S06", 10, sc("S06").sens[7].a)} x={1000} y={360} w={760} tail="r" text="Mua đất là mua tương lai, ai mua hiện tại!" />}</>)],
  ] },
  { id: "S07", shots: [
    [0, () => CD((t) => { const a = sc("S07").a; return <SplitCard t={t} title="5,5 tỷ đến từ đâu?" total="5,5 tỷ" parts={[{ label: "Tiết kiệm 5 năm ở Hàn", v: 1500, col: "#2b9a5a", at: 0.3 }, { label: "Vay ngân hàng (thế chấp sổ đỏ nhà bố mẹ)", v: 3000, col: "#d8212f", at: rel("S07", 2, a) }, { label: "Vay Dũng Gymmer", v: 800, col: "#e0832a", at: rel("S07", 6, a) }, { label: "Vay Vy Kim Khâu", v: 200, col: "#8a5ac9", at: rel("S07", 7, a) }]} />; })],
    [3, () => D3(S("streetday", "golden", ...twoShot(HX + 0.6), [C("bohung", [HX + 1.4, 0.15, 5.4], P("sad", { side: -1, acc: ["redbook"] })), C("hung", [HX - 0.3, 0.15, 5.3], P("grin", { side: 1 }))]), (t) => <><Bubble t={t} at={1.2} x={1080} y={130} w={460} tail="r" text="Con chắc chứ?" />{t > rel("S07", 4, sc("S07").sens[3].a) && <Bubble t={t} at={rel("S07", 4, sc("S07").sens[3].a)} x={160} y={360} w={640} text="Bố cứ yên tâm, đời là xa lộ!" />}</>)],
    [6, () => D3(S("streetday", "day", ...twoShot(HOME_X + 6), [C("dung", [HOME_X + 6.6, 0.15, 5.3], P("smug", { acc: ["flex"], anim: true })), C("hung", [HOME_X + 5.3, 0.15, 5.3], P("grin", { side: 1 }))]), (t) => <><LocTag t={t} l1="DŨNG GYMMER" l2="7 năm ở Nhật – sống theo quy tắc" /><Bubble t={t} at={1.8} x={1040} y={130} w={680} tail="r" text="800 triệu. Đúng hạn là phải trả!" /></>)],
    [7, () => D3(S("streetday", "day", ...twoShot(HOME_X + 6), [C("vy", [HOME_X + 6.6, 0.15, 5.3], P("stern", { side: -1, acc: ["paper"] })), C("hung", [HOME_X + 5.3, 0.15, 5.3], P("smile", { side: 1 }))]), (t) => <><LocTag t={t} l1="VY KIM KHÂU" l2="“Băng Bi Gơn” – sòng phẳng nhất họ" /><Bubble t={t} at={1.6} x={1040} y={130} w={620} tail="r" text="200 triệu, giấy vay viết tay nhé anh." /></>)],
  ] },
  { id: "S08", shots: [
    [0, () => CD((t) => <PaperCard t={t} kind="receipt" hue="warm" title="HỢP ĐỒNG ĐẶT CỌC" sub="Ngày 20/12/2025 · Lô 90 m² – Hiệp Hòa" lines={[{ text: "Giá chuyển nhượng: 5.500.000.000 đ", at: 0.5, big: true, under: true }]} stamp={{ text: "ĐÃ KÝ", at: 1.4, col: "#1f4e8a" }} />)],
    [2, () => D3(S("street", "night", [[HX - 3, 1.6, 2.4], [HX, 1.3, 5.3], 44], [[HX - 2, 1.5, 3.0], [HX, 1.3, 5.3], 40], [C("hung", HOMEP, P("laugh", { acc: ["mic"], anim: true })), C("tu", [HX + 1.5, 0.15, 5.6], P("laugh", { side: -1 })), C("lam", [HX - 1.5, 0.15, 5.6], P("grin", { side: 1 })), C("c5", [HX + 2.8, 0.15, 5.9], P("laugh"))]), (t) => <Meme t={t} at={0.5} top="" bot="ĐỜI LÀ XA LỘ 🎤" small y={120} />)],
  ] },
  { id: "S09", shots: [
    [0, () => D3(S("streetday", "day", [[GOLD_X + 3.4, 1.5, 2.6], [GOLD_X + 2.4, 1.15, 5.6], 42], [[GOLD_X + 3.1, 1.45, 3.1], [GOLD_X + 2.4, 1.15, 5.6], 38], [C("huy", [GOLD_X + 2.0, 0.48, 5.72], P("neutral", { mode: "sit", acc: ["glasses", "cup"] })), C("hung", [GOLD_X + 3.0, 0.15, 5.45], P("laugh", { acc: ["paper"] }))]), (t) => <LocTag t={t} l1="HUY NGUYỄN" l2="Người kể chuyện – ít nói, hay hỏi về rủi ro" />)],
    [2, () => D3(S("streetday", "day", [[GOLD_X + 1.4, 1.2, 3.8], [GOLD_X + 2.0, 1.05, 5.72], 34], [[GOLD_X + 1.5, 1.2, 4.1], [GOLD_X + 2.0, 1.05, 5.72], 30], [C("huy", [GOLD_X + 2.0, 0.48, 5.72], P("stern", { mode: "sit", acc: ["glasses"] }))]), (t) => <Bubble t={t} at={0.6} x={1040} y={120} w={720} tail="r" text="Nếu đất đứng im 3 năm, mỗi tháng anh lấy đâu ra tiền trả lãi?" />)],
    [3, () => CD((t) => <PaperCard t={t} kind="note" hue="night" title="PHÉP TÍNH CỦA HUY" sub="Lãi vay mua nhà đất ~12–14%/năm (CafeF, Q2/2026)" lines={[{ text: "3 tỷ × 13% ÷ 12 tháng", at: 0.4 }, { text: "≈ 32,5 TRIỆU / THÁNG", at: 1.2, big: true, col: "#d8212f", under: true }, { text: "Chưa tính tiền gốc", at: 2.2 }]} />)],
    [4, () => D3(S("streetday", "day", [[GOLD_X + 3.6, 1.45, 3.4], [GOLD_X + 3.0, 1.3, 5.45], 36], [[GOLD_X + 3.4, 1.45, 3.8], [GOLD_X + 3.0, 1.3, 5.45], 32], [C("hung", [GOLD_X + 3.0, 0.15, 5.45], P("laugh", { anim: true, wave: 0.9 }))], { shake: 0.4 }), (t) => <Bubble t={t} at={0.8} x={1000} y={130} w={720} tail="r" text="Đứng im thế nào được, đất chỉ có lên!" />)],
  ] },
  { id: "S10", shots: [
    [0, () => D3(S("field", "day", [[-12, 5, -10], [0.6, 1, 2], 50], [[-4, 2.4, -5], [0.6, 1, 2], 46], [C("hung", HUNG_F, P("neutral"))]), (t) => <ClockTag t={t} text="Sau Tết 2026" />)],
    [2, () => CD((t) => <ChatCard t={t} title="Đất nền tăng trưởng (2.814 thành viên)" msgs={[{ who: "Hùng", text: "Lô Hiệp Hòa có ai hỏi không anh em?", at: 0.3, me: true }, { who: "Hệ thống", text: "Đã xem bởi 1.204 người", at: 1.4 }]} />)],
    [3, () => CD((t) => <PaperCard t={t} kind="receipt" hue="navy" title="GIAO DỊCH ĐẤT QUÝ II/2026" sub="Cả nước – Bộ Xây dựng (CafeF dẫn)" lines={[{ text: "73.438 giao dịch thành công", at: 0.4, big: true }, { text: "= 59,9% cùng kỳ 2025", at: 1.2, col: "#d8212f", big: true }]} />)],
  ] },
  { id: "S11", shots: [
    [0, () => CD((t) => <PhoneCard t={t} hue="red" time="08:00" date="Ngày 15 hằng tháng" notifs={[{ app: "Ngân hàng", col: "#b3131f", title: "Biến động số dư", body: "−32.500.000 đ · Thu lãi khoản vay", at: 0.3 }]} quote={["NGÀY 15", "LẠI TRỪ TIỀN"]} qAt={1.0} />)],
    [2, () => D3(S("street", "night", [[HOME_X + 6, 1.4, 2.4], [HOME_X + 9, 1.0, 5.1], 44], [[HOME_X + 2, 1.4, 2.4], [HOME_X + 4, 1.0, 5.1], 44], ride("hung"), { rain: true, ease: "lin" }), (t) => <BigText t={t} at={rel("S11", 3, sc("S11").sens[2].a) + 0.3} text="12 TRIỆU < 32,5 TRIỆU" col="#ff4d5e" y={110} size={104} />)],
    [5, () => D3(S("street", "night", [[HOME_X + 9, 1.3, 3.2], [HOME_X + 10, 1.0, 5.1], 40], [[HOME_X + 3.5, 1.3, 3.2], [HOME_X + 4.5, 1.0, 5.1], 40], ride("hung", [C("khach", [HOME_X + 14.6, 0.66, 5.2], P("sad", { mode: "sit" }), [HX + 2.6, 0.66, 5.2])]), { rain: true, ease: "lin" }), (t) => <>{t > rel("S11", 6, sc("S11").sens[5].a) && <Bubble t={t} at={rel("S11", 6, sc("S11").sens[5].a)} x={980} y={110} w={800} tail="r" text="Chỗ này năm ngoái anh mua 60 triệu một mét, giờ rao 30 không ai hỏi…" />}</>)],
    [7, () => D3(S("street", "night", [[HOME_X + 5.4, 1.15, 3.6], [HOME_X + 5.4, 1.05, 5.15], 30], [[HOME_X + 5.4, 1.15, 3.9], [HOME_X + 5.4, 1.05, 5.15], 26], [C("hung", [HOME_X + 5.4, 0.62, 5.15], P("stern", { mode: "sit", acc: ["helmet"] }))], { rain: true }))],
  ] },
  { id: "S12", shots: [
    [0, () => D3(S("streetday", "day", ...twoShot(GOLD_X + 4.2, 5.45), [C("lam", [GOLD_X + 4.9, 0.15, 5.45], P("laugh", { side: -1, wave: 0.6 })), C("hung", [GOLD_X + 3.6, 0.15, 5.45], P("neutral", { side: 1 })), ...teaStall("laugh", false)]), (t) => <><LocTag t={t} l1="LÂM CHỐT NON" l2="Lãi 2% là bán" /><Bubble t={t} at={1.0} x={1000} y={120} w={760} tail="r" text="Em mà mua đất thì lãi 2% là em bán rồi anh ạ!" /></>)],
    [1, () => D3(S("streetday", "day", [[GOLD_X + 7, 2.4, 1.6], [GOLD_X + 6, 1.0, 5.9], 46], [[GOLD_X + 7, 2.1, 2.0], [GOLD_X + 6, 1.0, 5.9], 42], [...teaStall("laugh", false), C("lam", [GOLD_X + 4.9, 0.15, 5.45], P("laugh"))], { shake: 0.4 }), (t) => <Meme t={t} at={0.3} top="" bot="LÃI 2% LÀ BÁN… ĐẤT BÁN CHO AI?" y={120} />)],
    [2, () => D3(S("streetday", "day", [[GOLD_X + 3.6, 1.45, 4.0], [GOLD_X + 3.6, 1.4, 5.45], 28], [[GOLD_X + 3.6, 1.45, 4.3], [GOLD_X + 3.6, 1.4, 5.45], 24], [C("hung", [GOLD_X + 3.6, 0.15, 5.45], P("sad"))]))],
    [3, () => CD((t) => <ChatCard t={t} title="Dũng Gymmer 💪" msgs={[{ who: "Dũng Gymmer", text: "Tháng 7 đến hạn nhé.", at: 0.3 }, { who: "Dũng Gymmer", text: "Quy tắc bàn tay phải: vay thì trả, không có ngoại lệ ✋", at: rel("S12", 4, sc("S12").sens[3].a) }]} />)],
  ] },
  { id: "S13", shots: [
    [0, () => D3(S("field", "day", [[5.5, 2.0, -9.5], [0.8, 1.6, -1.8], 46], [[4.6, 1.9, -8.2], [0.8, 1.6, -1.8], 42], [C("hung", [-0.6, 0, -2.4], P("worried", { acc: ["phone"] }))]), (t) => <BigText t={t} at={0.4} text="RAO 4,5 TỶ" col="#ffcf3a" y={70} size={100} />)],
    [2, () => CD((t) => <PhoneCard t={t} hue="night" time="19:42" date="Tháng 8/2026" notifs={[{ app: "Điện thoại", col: "#2b9a5a", title: "Số lạ", body: "Hỏi giá lô 3,5 tỷ… (2 phút)", at: 0.3 }, { app: "Zalo", col: "#2f6fd1", title: "Người dùng này đã chặn bạn", body: "Bạn không thể gửi tin nhắn.", at: rel("S13", 3, sc("S13").sens[2].a) }]} quote={["RAO 3,5 TỶ", "VẪN KHÔNG AI MUA"]} qAt={1.0} />)],
    [4, () => CD((t) => <PaperCard t={t} kind="receipt" hue="red" title="GIÁ RAO ĐẤT NỀN – 2026" sub="CafeF dẫn Batdongsan (giá rao)" lines={[{ text: "Minh Giang Đầm Và (Mê Linh): 60 → 30 tr/m²", at: 0.3, big: true }, { text: "Vĩnh Tiến (Kim Bôi): ~20 → 5 tr/m² (−75%)", at: rel("S13", 5, sc("S13").sens[4].a), big: true, col: "#d8212f" }]} stamp={{ text: "−50% ĐẾN −75%", at: rel("S13", 5, sc("S13").sens[4].a) + 1.0 }} />)],
  ] },
  { id: "S14", shots: [
    [0, () => D3(S("streetday", "golden", [[HX - 1.6, 1.4, 3.0], [HX, 1.3, 5.3], 38], [[HX - 1.2, 1.38, 3.5], [HX, 1.3, 5.3], 34], [C("mehung", HOMEP, P("worried", { acc: ["paper"] }))]), (t) => <BigText t={t} at={rel("S14", 1, sc("S14").a) + 1.4} text="NỢ QUÁ HẠN" col="#ff4d5e" y={110} size={120} />)],
    [2, () => CD((t) => <PhoneCard t={t} hue="night" time="21:15" date="Tháng 10/2026" notifs={[{ app: "Điện thoại", col: "#2b9a5a", title: "Cuộc gọi đến", body: "Bố", at: 0.3 }]} quote={["BỐ GỌI", ""]} qAt={0.8} />)],
    [4, () => D3(S("street", "night", [[HX - 1.4, 1.35, 3.4], [HX, 1.25, 5.3], 34], [[HX - 1.2, 1.33, 3.8], [HX, 1.25, 5.3], 30], [C("bohung", HOMEP, P("sad", { acc: ["phone"], headTilt: 6 }))]), (t) => <Bubble t={t} at={0.9} x={1040} y={140} w={720} tail="r" text="Con ơi, bố mẹ già rồi, còn nhà để ở không con?" />)],
    [5, () => D3(S("street", "night", [[HOME_X + 7.6, 0.95, 3.6], [HOME_X + 8, 0.7, 5.6], 36], [[HOME_X + 7.8, 0.92, 4.0], [HOME_X + 8, 0.7, 5.6], 30], [C("hung", [HOME_X + 8, 0.15, 5.6], P("cry", { mode: "sit", acc: ["tears", "phone"], anim: true }))]), (t) => <Vignette k={0.7} />)],
  ] },
  { id: "S15", shots: [
    [0, () => D3(S("streetday", "day", ...twoShot(HX + 0.6), [C("vy", [HX + 4, 0.15, 5.3], walk("stern", { side: -1 }), [HX + 1.5, 0.15, 5.3]), C("hung", [HX - 0.3, 0.15, 5.3], P("sad", { side: 1 }))], { ease: "out" }))],
    [1, () => D3(S("streetday", "day", ...twoShot(HX + 0.6, 5.3, 2.6), [C("vy", [HX + 1.5, 0.15, 5.3], P("stern", { side: -1 })), C("hung", [HX - 0.3, 0.15, 5.3], P("sad", { side: 1 }))]), (t) => <><Bubble t={t} at={0.3} x={1000} y={120} w={780} tail="r" text="Em không đòi ngay. Nhưng anh định làm gì với lô đất đó?" />{t > rel("S15", 2, sc("S15").sens[1].a) && <Bubble t={t} at={rel("S15", 2, sc("S15").sens[1].a)} x={160} y={380} w={520} kind="whisper" text="Chờ về bờ đã em…" />}</>)],
    [3, () => D3(S("streetday", "day", [[HX + 0.8, 1.45, 2.2], [HX + 1.5, 1.2, 5.3], 36], [[HX + 1.0, 1.45, 2.8], [HX + 1.5, 1.2, 5.3], 32], [C("vy", [HX + 1.5, 0.15, 5.3], P("smug", { side: -1 }))], { shake: 0.5 }), (t) => <Meme t={t} at={0.5} top="VỀ BỜ…" bot="HAY VỀ ĐỒI CỎ?" />)],
  ] },
  { id: "S16", shots: [
    [0, () => D3(S("field", "night", [[-1.6, 1.9, -2.6], [0.6, 1.3, 1.2], 42], [[-0.6, 1.6, -1.2], [0.6, 1.35, 1.2], 36], [C("hung", HUNG_F, P("sad", { acc: ["phone", "glow"] }))]), (t) => <ClockTag t={t} text="02:00" />)],
    [1, () => CD((t) => <PhoneCard t={t} hue="night" time="08:12" date="Sáng hôm sau" notifs={[{ app: "Điện thoại", col: "#2b9a5a", title: "Số lạ", body: "Em mua để ở thật, nhưng chỉ 1,8 tỷ thôi anh.", at: 0.4 }]} quote={["TRẢ GIÁ", "1,8 TỶ"]} qAt={1.0} />)],
    [3, () => D3(S("field", "day", [[1.6, 1.5, -1.0], [0.6, 1.45, 1.2], 34], [[1.4, 1.5, -0.6], [0.6, 1.45, 1.2], 30], [C("hung", HUNG_F, seq([[0, "stern"], [2.4, "sad"]], { acc: ["phone"] }))]), (t) => <><Bubble t={t} at={0.2} x={160} y={120} w={640} text="Em biết anh mua bao nhiêu không?" />{t > rel("S16", 4, sc("S16").sens[3].a) && <Bubble t={t} at={rel("S16", 4, sc("S16").sens[3].a)} x={1000} y={360} w={760} tail="r" kind="whisper" text="Em biết. Nhưng giá đất là giá người mua trả anh ạ." />}</>)],
    [5, () => CD((t) => { const a = sc("S16").sens[5].a; return <PaperCard t={t} kind="note" hue="night" title="SỔ TAY CỦA HÙNG" sub="Tháng 11/2026" lines={[{ text: "Mua vào: 5,5 tỷ", at: 0.2 }, { text: "Lãi đã trả ~11 tháng: ~357 triệu", at: rel("S16", 6, a) }, { text: "Bán ra: 1,8 tỷ", at: rel("S16", 7, a) }, { text: "MẤT: GẦN 4 TỶ", at: rel("S16", 8, a), big: true, col: "#d8212f", under: true }, { text: "Còn nợ: NH 1,2 tỷ · Dũng 800 tr · Vy 200 tr", at: rel("S16", 9, a), big: true }]} stamp={{ text: "CẮT LỖ", at: rel("S16", 8, a) + 0.8 }} sign="Người ghi: Hùng" />; })],
  ] },
  { id: "S17", shots: [
    [0, () => D3(S("streetday", "day", ...twoShot(GOLD_X + 2.6, 5.45, 2.8), [C("huy", [GOLD_X + 3.2, 0.15, 5.45], P("neutral", { side: -1, acc: ["glasses"] })), C("hung", [GOLD_X + 2.0, 0.15, 5.45], P("sad", { side: 1 }))]), (t) => <Bubble t={t} at={0.4} x={1020} y={120} w={700} tail="r" text="Đất không có lỗi. Cái sai nằm ở cách mình mua." />)],
    [2, () => CD((t) => { const a = sc("S17").sens[2].a; return <LessonCard t={t} title="4 lỗi quản trị rủi ro của Hùng" items={[
      { n: "1", icon: "💸", head: "Vay quá sức", body: "Trả nợ mỗi tháng nên ≤ khoảng 1/3 thu nhập ổn định", at: rel("S17", 3, a) },
      { n: "2", icon: "🌾", head: "Tài sản không tạo dòng tiền", body: "Đất trống không cho thuê – chỉ chờ người sau mua giá cao hơn", at: rel("S17", 6, a) },
      { n: "3", icon: "📣", head: "Mua theo đám đông, tin đồn", body: "Cả nhóm Zalo khoe chênh = người vào cuối trả giá", at: rel("S17", 9, a) },
      { n: "4", icon: "🛑", head: "Không có điểm dừng", body: "Viết trước “sai đến đâu thì bán” – đừng chờ về bờ", at: rel("S17", 11, a) }]} />; })],
  ] },
  { id: "S18", shots: [
    [0, () => D3(S("bank", "day", [[-2.6, 1.6, 2.6], [0, 1.2, -1.2], 44], [[-1.8, 1.5, 2.0], [0, 1.2, -1.2], 40], [C("nv", [0, 0, -2.0], P("smile")), C("hung", [0.2, 0, -0.2], P("neutral", { acc: ["paper"] }))]), (t) => <LocTag t={t} l1="NGÂN HÀNG" l2="Xin giãn nợ – giữ căn nhà của bố mẹ" />)],
    [1, () => D3(S("streetday", "day", ...twoShot(HOME_X + 6), [C("dung", [HOME_X + 6.5, 0.15, 5.3], P("smile_closed", { side: -1, wave: 0.5 })), C("hung", [HOME_X + 5.5, 0.15, 5.3], P("relief", { side: 1 }))]), (t) => <Bubble t={t} at={0.6} x={1020} y={120} w={720} tail="r" text="Chậm cũng được, nhưng không được trốn. Quy tắc bàn tay phải!" />)],
    [2, () => D3(S("streetday", "dawn", ...twoShot(HX + 1.0, 5.3, 5.0), [C("bohung", [HX + 1.5, 0.15, 5.4], P("smile_closed", { side: -1 })), C("mehung", [HX + 2.4, 0.15, 5.6], P("smile", { side: -1, acc: ["xoi"] })), C("hung", [HX - 0.3, 0.15, 5.3], P("smile_closed", { side: 1 }))]), (t) => { const a = sc("S18").sens[2].a; return <>
      {t > rel("S18", 3, a) && <Bubble t={t} at={rel("S18", 3, a)} x={1060} y={40} w={720} tail="r" text="Nhà còn thì người còn, tiền mất thì mình làm lại con ạ." />}
      {t > rel("S18", 4, a) && <Bubble t={t} at={rel("S18", 4, a)} x={160} y={40} w={600} text="Lần này con làm có kế hoạch." />}
      {t > rel("S18", 5, a) && <Bubble t={t} at={rel("S18", 5, a)} x={1060} y={250} w={720} tail="r" text="Đi đường cẩn thận, đời không phải xa lộ đâu con." />}</>; })],
    [6, () => D3(S("streetday", "dawn", [[HX - 0.3, 1.45, 3.6], [HX - 0.3, 1.4, 5.3], 30], [[HX - 0.3, 1.45, 3.9], [HX - 0.3, 1.4, 5.3], 26], [C("hung", [HX - 0.3, 0.15, 5.3], P("smile_closed"))]))],
  ] },
  { id: "S19", shots: [[0, () => D3(S("field", "dawn", [[-2, 1.6, -4], [0.6, 1.2, 2], 46], [[-30, 14, -30], [0, 1, 10], 52], [C("hung", HUNG_F, P("relief"))], { ease: "sm" }), (t) => <BigText t={t} at={rel("S19", 2, sc("S19").a) + 0.3} text="BIẾT PHANH Ở ĐÂU" col="#ffcf3a" y={420} size={130} />)]] },
  { id: "S20", shots: [[0, () => CD((t) => <DatCta t={t} webAt={rel("S20", 2, sc("S20").a)} />)]] },
];

function teaStall(e: Expr = "grin", withTan = true): Cast[] {
  const r = [C("tu", [GOLD_X + 5.2, 0.48, 5.72], P(e, { mode: "sit", acc: ["cup"], anim: true })), C("ba", [GOLD_X + 8.6, 0.48, 5.72], P(e === "laugh" ? "grin" : e, { mode: "sit", acc: ["nonla"] })),
    C("c8", [GOLD_X + 7.0, 0.48, 5.72], P("laugh", { mode: "sit" })), C("c6", [GOLD_X + 11.8, 0.48, 5.72], P("smile", { mode: "sit", acc: ["cup"], anim: true }))];
  return withTan ? [...r, C("hung", [GOLD_X + 6.3, 0.15, 5.45], P("smile"))] : r;
}
function feverCrowd(phones = false): Cast[] { return Array.from({ length: 12 }, (_, i) => C("c" + (20 + i), [-8 + i * 1.6, 0, -1.2 + (i % 3) * 0.6], P(i % 3 === 0 ? "grin" : i % 3 === 1 ? "nervous" : "neutral", { acc: phones || i % 2 ? ["phone"] : [], phase: i * 0.3, anim: true }))); }
const Meme: React.FC<{ t: number; at?: number; top: string; bot: string; small?: boolean; noSubGap?: boolean; y?: number }> = ({ t, at = 0, top, bot, small, noSubGap, y }) => { if (t < at) return null; const a = Math.min(1, (t - at) / 0.18), sz = small ? 150 : 92;
  const st = { position: "absolute", left: 0, width: 1920, textAlign: "center", fontFamily: F, fontWeight: 900, fontSize: sz, color: "#fff", WebkitTextStroke: "10px #000", paintOrder: "stroke fill", letterSpacing: 1, transform: `scale(${1.25 - 0.25 * a})`, opacity: a } as React.CSSProperties;
  return <>{top && <div style={{ ...st, top: 70 }}>{top}</div>}{bot && <div style={{ ...st, top: y ?? (small ? 690 : noSubGap ? 175 : 620), color: small ? "#ffe14d" : "#fff", fontSize: small ? 130 : sz }}>{bot}</div>}</>; };

const DatCta: React.FC<{ t: number; webAt: number }> = ({ t, webAt }) => { const a = sm(t / 0.5), w = sm((t - webAt) / 0.45), clickT = t - webAt - 2.2, sub = clickT > 0.35;
  return <AbsoluteFill style={{ fontFamily: F, justifyContent: "center", alignItems: "center", textAlign: "center" }}><Bg t={t} hue="navy" />
    <div style={{ position: "relative", opacity: a }}>
      <div style={{ fontSize: 58, fontWeight: 800, color: "#fff" }}>Đang giữ đất, vàng hay cổ phiếu mà không biết nên giữ hay bán?</div>
      <div style={{ marginTop: 50, opacity: w, transform: `scale(${0.9 + 0.1 * w})` }}>
        <div style={{ fontSize: 40, fontWeight: 800, color: "#f5c518", letterSpacing: 4 }}>HỌC QUẢN TRỊ RỦI RO MIỄN PHÍ</div>
        <div style={{ fontSize: 96, fontWeight: 900, color: "#fff", marginTop: 8 }}>chungkhoanhuynguyen.com</div>
        <div style={{ display: "flex", gap: 30, justifyContent: "center", marginTop: 34 }}>{["Vay bao nhiêu là vừa?", "Chia vốn thế nào?", "Khi nào phải cắt lỗ?"].map((s, i) => <div key={i} style={{ padding: "18px 30px", borderRadius: 18, background: "rgba(255,255,255,.1)", border: "2px solid rgba(255,255,255,.25)", color: "#dfe5f2", fontSize: 36, fontWeight: 700, opacity: sm((t - webAt - 0.6 - i * 0.35) / 0.4) }}>{s}</div>)}</div>
        <div style={{ display: "inline-block", marginTop: 44, padding: "22px 60px", borderRadius: 60, background: sub ? "#3a3f52" : "#e62117", color: "#fff", fontSize: 46, fontWeight: 900 }}>{sub ? "✓ ĐÃ THEO DÕI" : "+ THEO DÕI KÊNH"}</div>
      </div></div>
    {clickT > -0.6 && clickT < 1.2 && <div style={{ position: "absolute", left: 1080 - Math.min(1, (clickT + 0.6) / 0.6) * 60, top: 900 - Math.min(1, (clickT + 0.6) / 0.6) * 40, fontSize: 70 }}>👆</div>}
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
export const DAT_FRAMES = TOTAL_F;
export const DatVideo: React.FC = () => {
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
        {audio ? <Audio src={staticFile("dat/voice.wav")} /> : null}
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
