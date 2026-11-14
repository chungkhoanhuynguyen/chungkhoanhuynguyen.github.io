// Phim #4 "Lương 30 triệu": mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/ma két tinh/g, "marketing"], [/Ngân Săn Seo/g, "Ngân Săn Sale"], 
  [/hai mươi lăm tháng mười/g, "25/10"], [/mười tám triệu/g, "18 triệu"], [/mười hai triệu/g, "12 triệu"], [/Mười một ngày sau, mười một giờ đêm ngày năm tháng mười một/g, "11 ngày sau, 23 giờ ngày 5/11"],
  [/ba trăm mười hai nghìn đồng/g, "312.000 đồng"], [/ba trăm mười hai nghìn/g, "312 nghìn"], [/hai mươi triệu/g, "20 triệu"], [/ba mươi triệu/g, "30 triệu"], [/ba mươi lăm tuổi/g, "35 tuổi"], [/mười lăm triệu/g, "15 triệu"],
  [/hộp thứ mười hai/g, "hộp thứ 12"], [/không giờ/g, "0 giờ"], [/năm mươi phần trăm/g, "50%"], [/chín phẩy hai triệu/g, "9,2 triệu"], [/mười một phẩy hai triệu/g, "11,2 triệu"], [/quý ba/g, "quý III"],
  [/Tính chín tháng/g, "Tính 9 tháng"], [/gấp hơn ba lần/g, "gấp hơn 3 lần"], [/ngày năm/g, "ngày 5"], [/chín triệu/g, "9 triệu"], [/ba triệu rưỡi/g, "3,5 triệu"], [/hai triệu rưỡi/g, "2,5 triệu"],
  [/sáu triệu/g, "6 triệu"], [/bốn triệu/g, "4 triệu"], [/hai triệu/g, "2 triệu"], [/ba triệu/g, "3 triệu"], [/mười triệu/g, "10 triệu"], [/bảy triệu/g, "7 triệu"],
  [/ba mươi tám phẩy tám phần trăm/g, "38,8%"], [/ba phẩy chín chín phần trăm/g, "3,99%"], [/Ngày tám tháng mười một/g, "Ngày 8/11"], [/ba mươi phần trăm/g, "30%"],
  [/năm phút/g, "5 phút"], [/Bảy ngày/g, "7 ngày"], [/hai mươi phần trăm/g, "20%"], [/gần bốn nghìn phần trăm/g, "gần 4.000%"], [/Ngày thứ tám/g, "Ngày thứ 8"],
  [/năm năm nay/g, "5 năm nay"], [/sáu tháng/g, "6 tháng"], [/ba điều/g, "3 điều"], [/mười đến 20%/g, "10 đến 20%"], [/mười đến hai mươi phần trăm/g, "10 đến 20%"], [/ba đến 6 tháng/g, "3 đến 6 tháng"], [/ba đến sáu tháng/g, "3 đến 6 tháng"],
  [/Một: /g, "1. "], [/Hai: /g, "2. "], [/Ba: /g, "3. "], [/Hai tháng sau/g, "2 tháng sau"], [/Ba năm sau/g, "3 năm sau"], [/ba mươi sáu tháng/g, "36 tháng"], [/hai trăm mười sáu triệu/g, "216 triệu"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["cháy túi", "nợ", "phạt", "cắt giảm", "vay", "phí", "đòi nợ", "nằm viện", "lãi"];
export const GOOD = ["trả cho mình trước", "quỹ dự phòng", "tích lũy", "để riêng", "việc mới"];
