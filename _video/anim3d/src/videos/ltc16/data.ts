// "Lớp học Lý thuyết trò chơi – Bài 9" (bản 7: mở bài kể đủ, 15/11/2026): mốc giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Cường Sô xiu/g, "Cường Sociu"],
  [/Ti Pi Bank/g, "TPB"],
  [/P trên B/g, "P/B"],
  [/hai nghìn không trăm hai mươi sáu/g, "2026"],
  [/hai nghìn không trăm hai mươi lăm/g, "2025"],
  [/hai nghìn không trăm hai mươi ba/g, "2023"],
  [/hai nghìn không trăm mười tám/g, "2018"],
  [/hai nghìn không trăm mười chín/g, "2019"],
  [/một trăm hai mươi bốn phẩy bốn phần trăm/g, "124,4%"],
  [/bảy trăm ba mươi mốt phẩy một phần trăm/g, "731,1%"],
  [/bảy mươi chín phẩy năm phần trăm/g, "79,5%"],
  [/sáu mươi lăm phẩy hai phần trăm/g, "65,2%"],
  [/hai mươi phần trăm/g, "20%"],
  [/mười hai phẩy bảy/g, "12,7"],
  [/ngày mười sáu tháng mười một/g, "ngày 16/11"],
  [/ngày ba mươi mốt tháng ba/g, "ngày 31/3"],
  [/ngày hai mươi hai tháng tám/g, "ngày 22/8"],
  [/tháng một năm/g, "tháng 1 năm"],
  [/tháng tám năm/g, "tháng 8 năm"],
  [/một nghìn lệnh/g, "1.000 lệnh"],
  [/một giờ sáng/g, "1 giờ sáng"],
  [/chín giờ/g, "9 giờ"],
  [/bảy, tám/g, "7, 8"],
  [/ba đến năm năm/g, "3 đến 5 năm"],
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/ phần trăm/g, "%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["phá sản", "sập", "mất", "thua", "giảm", "lỗ", "giải chấp", "thất nghiệp", "hoảng loạn", "nợ"];
export const GOOD = ["sống", "thắng", "lợi thế", "bình tĩnh", "ngủ ngon", "sống sót"];
