// "Lớp học Lý thuyết trò chơi – Bài 6" (bản 7: mở bài kể đủ, 15/11/2026): mốc giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Bài sáu/g, "Bài 6"],
  [/Cường Sô xiu/g, "Cường Sociu"],
  [/A cơ lốp/g, "Akerlof"],
  [/Nô ben/g, "Nobel"],
  [/một nghìn chín trăm bảy mươi/g, "1970"],
  [/ba mươi phần trăm/g, "30%"],
  [/hai trăm triệu/g, "200 triệu"],
  [/ba trăm triệu/g, "300 triệu"],
  [/ba mươi mốt/g, "31"],
  [/Mười một/g, "11"],
  [/mười lăm/g, "15"],
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/ phần trăm/g, "%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["phá sản", "sập", "mất", "thua", "giảm", "lỗ", "giải chấp", "thất nghiệp", "hoảng loạn", "nợ"];
export const GOOD = ["sống", "thắng", "lợi thế", "bình tĩnh", "ngủ ngon", "sống sót"];
