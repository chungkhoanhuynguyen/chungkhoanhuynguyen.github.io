// Phim GD1: mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/ba chi tiết/g, "3 chi tiết"], [/Ba chi tiết/g, "3 chi tiết"], [/mười giây/g, "10 giây"],
  [/hai nghìn không trăm hai mươi bốn/g, "2024"], [/hai nghìn không trăm hai mươi lăm/g, "2025"], [/Mười giờ tối/g, "10 giờ tối"], [/năm mươi triệu/g, "50 triệu"], [/mười giây/g, "10 giây"],
  [/Bốn phút/g, "4 phút"], [/ba mươi mốt tuổi/g, "31 tuổi"], [/ba video/g, "3 video"], [/mười một tháng/g, "11 tháng"], [/sáu nghìn tỷ đồng/g, "6.000 tỷ đồng"],
  [/tháng bảy/g, "tháng 7"], [/trên mười triệu đồng/g, "trên 10 triệu đồng"], [/trên hai mươi triệu/g, "trên 20 triệu"], [/ba tháng/g, "3 tháng"], [/mười phần trăm/g, "10%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["lừa", "giả", "đâm xe", "hoảng loạn", "thiệt hại", "kẻ gian", "lạ", "đường tắt"];
export const GOOD = ["mật khẩu", "gọi lại", "riêng tư", "hạn mức", "còn nguyên", "Bánh Bao"];
