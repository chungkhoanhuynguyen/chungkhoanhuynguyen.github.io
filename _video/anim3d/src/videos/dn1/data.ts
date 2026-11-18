// Phim DN1: mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/một trăm tám mươi hai nghìn/g, "182.000"], [/Tám giờ sáng/g, "8 giờ sáng"], [/ba chi tiết/g, "3 chi tiết"], [/Ba chi tiết/g, "3 chi tiết"], [/bốn mươi hai tuổi/g, "42 tuổi"],
  [/mười năm/g, "10 năm"], [/Năm năm trước/g, "5 năm trước"], [/năm năm/g, "5 năm"], [/ba năm/g, "3 năm"], [/hai chiếc xe/g, "2 chiếc xe"], [/mười tháng/g, "10 tháng"],
  [/năm mươi sáu nghìn ba trăm/g, "56.300"], [/hai mươi mốt nghìn sáu trăm/g, "21.600"], [/một trăm hai mươi phần trăm/g, "120%"], [/chín mươi hai nghìn/g, "92.000"],
  [/ba mươi ba nghìn bảy trăm/g, "33.700"], [/mười tám nghìn/g, "18.000"], [/hai nghìn không trăm hai mươi ba/g, "2023"], [/mười hai phẩy bảy phần trăm/g, "12,7%"],
  [/bốn mươi hai phần trăm/g, "42%"], [/một trăm sáu mươi hai nghìn/g, "162.000"], [/ba mươi tư phẩy tám phần trăm/g, "34,8%"], [/mười ba phẩy hai tỷ đồng/g, "13,2 tỷ đồng"],
  [/mười bảy phần trăm/g, "17%"], [/Hai tuần sau/g, "2 tuần sau"], [/hai con số/g, "2 con số"], [/Thành phố Hồ Chí Minh/g, "TP.HCM"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["sập", "giải thể", "rời cuộc chơi", "thanh lý", "sang nhượng", "mất khách", "đau", "giảm dần"];
export const GOOD = ["thay máu", "thành lập mới", "giành khách", "tay nghề", "có giá", "đọc hết"];
