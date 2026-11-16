// "Lớp học Lý thuyết trò chơi – Bài 5" (bản 7: mở bài kể đủ, 15/11/2026): mốc giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Bài năm/g, "Bài 5"],
  [/Cu ba/g, "Cuba"],
  [/Cường Sô xiu/g, "Cường Sociu"],
  [/Mát xcơ va/g, "Moscow"],
  [/A khíp pốp/g, "Arkhipov"],
  [/Công cót/g, "Concorde"],
  [/hai mươi phần trăm/g, "20%"],
  [/hai nghìn không trăm hai mươi hai/g, "2022"],  
  [/một nghìn chín trăm sáu mươi hai/g, "1962"],  
  [/hai mươi phần trăm/g, "20%"],  
  [/một trăm năm mươi/g, "150"],  
  [/hai mươi bốn/g, "24"],  
  [/hai mươi bảy/g, "27"],  
  [/hai mươi/g, "20"],  
  [/mười ba/g, "13"],  
  [/mười/g, "10"],  
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/ phần trăm/g, "%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["phá sản", "sập", "mất", "thua", "giảm", "lỗ", "giải chấp", "thất nghiệp", "hoảng loạn", "nợ"];
export const GOOD = ["sống", "thắng", "lợi thế", "bình tĩnh", "ngủ ngon", "sống sót"];
