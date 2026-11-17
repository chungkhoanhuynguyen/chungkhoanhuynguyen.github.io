// Phim DOLA1: mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Phét/g, "Fed"], [/hai nghìn không trăm hai mươi hai/g, "2022"], [/hai nghìn không trăm hai mươi ba/g, "2023"], [/hai nghìn không trăm hai mươi lăm/g, "2025"], [/hai nghìn không trăm hai mươi sáu/g, "2026"],
  [/tháng mười một/g, "tháng 11"], [/tháng mười hai/g, "tháng 12"], [/tháng mười/g, "tháng 10"], [/tháng chín/g, "tháng 9"], [/tháng ba/g, "tháng 3"], [/Mười giờ đêm/g, "10 giờ đêm"],
  [/ba tiệm/g, "3 tiệm"], [/chín giờ sáng/g, "9 giờ sáng"], [/ba mươi tư tuổi/g, "34 tuổi"], [/một mét bốn bảy/g, "1m47"], [/mười năm/g, "10 năm"],
  [/một nghìn năm trăm điểm/g, "1.500 điểm"], [/tám trăm bảy mươi điểm/g, "870 điểm"], [/bốn phẩy hai lăm đến bốn phẩy năm phần trăm/g, "4,25–4,5%"], [/bốn mươi năm/g, "40 năm"],
  [/năm mươi sáu phẩy tám phần trăm/g, "56,8%"], [/bốn phẩy bảy phần trăm/g, "4,7%"], [/hai mươi mốt tỷ đô la/g, "21 tỷ USD"], [/tám mươi chín đến chín mươi tỷ/g, "89–90 tỷ USD"],
  [/bốn, năm phần trăm/g, "4–5%"], [/bốn mươi phần trăm/g, "40%"], [/ba phiên/g, "3 phiên"], [/hai mươi ba nghìn sáu/g, "23.600"], [/không phẩy hai lăm phần trăm/g, "0,25%"], [/ba phẩy bảy lăm đến bốn phần trăm/g, "3,75–4%"],
  [/ngày mười một tháng 11/g, "ngày 11/11"], [/hai mươi lăm nghìn sáu trăm mười một đồng/g, "25.611 đồng"], [/hai mươi lăm nghìn tám trăm hai mươi đồng/g, "25.820 đồng"], [/hai mươi phần trăm/g, "20%"],
  [/bốn điều/g, "4 điều"], [/Một\./g, "1."], [/Hai\./g, "2."], [/Ba\./g, "3."], [/Bốn\./g, "4."],
];


export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["lỗ", "giải chấp", "ký quỹ", "tin đồn", "rút", "mất giá", "nợ", "cháy túi", "nợ", "phạt", "cắt giảm", "vay", "phí", "đòi nợ", "nằm viện", "lãi"];
export const GOOD = ["ngủ ngon", "kỳ hạn", "không vay", "được lợi", "trả cho mình trước", "quỹ dự phòng", "tích lũy", "để riêng", "việc mới"];
