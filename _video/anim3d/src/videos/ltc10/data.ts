// "Lớp học Lý thuyết trò chơi – Bài 4" (bản 7: mở bài kể đủ, 15/11/2026): mốc giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Bài bốn/g, "Bài 4"],
  [/chín nghìn/g, "9.000"],
  [/năm mươi triệu/g, "50 triệu"],
  [/một nghìn năm trăm tám mươi tám/g, "1588"],  
  [/hai nghìn không trăm mười/g, "2010"],  
  [/một trăm ba mươi/g, "130"],  
  [/năm mươi triệu/g, "50.000.000"],  
  [/chín nghìn/g, "9.000"],  
  [/Chín nghìn/g, "9.000"],  
  [/hai nghìn/g, "2000"],  
  [/Mười/g, "10"],  
  [/mười/g, "10"],  
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/ phần trăm/g, "%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["phá sản", "sập", "mất", "thua", "giảm", "lỗ", "giải chấp", "thất nghiệp", "hoảng loạn", "nợ"];
export const GOOD = ["sống", "thắng", "lợi thế", "bình tĩnh", "ngủ ngon", "sống sót"];
