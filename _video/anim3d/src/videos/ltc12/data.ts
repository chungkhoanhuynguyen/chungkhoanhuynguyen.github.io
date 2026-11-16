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
  [/Bài năm/g, "Bài 5"],
  [/Đao Giôn/g, "Dow Jones"],
  [/phố Uôn/g, "phố Wall"],
  [/Niu tơn/g, "Newton"],
  [/một nghìn một trăm bảy mươi/g, "1.170"],
  [/năm mươi phần trăm/g, "50%"],
  [/một nghìn chín trăm hai mươi chín/g, "1929"],  
  [/một nghìn chín trăm ba mươi hai/g, "1932"],  
  [/một nghìn chín trăm năm mươi tư/g, "1954"],  
  [/hai nghìn không trăm linh chín/g, "2009"],  
  [/hai nghìn không trăm linh tám/g, "2008"],  
  [/hai nghìn không trăm linh bảy/g, "2007"],  
  [/hai nghìn không trăm mười tám/g, "2018"],  
  [/một nghìn bảy trăm hai mươi/g, "1720"],  
  [/một nghìn một trăm bảy mươi/g, "1170"],  
  [/hai trăm ba mươi lăm/g, "235"],  
  [/chín mươi phần trăm/g, "90%"],  
  [/tám mươi phần trăm/g, "80%"],  
  [/năm mươi phần trăm/g, "50%"],  
  [/ba trăm tám mươi/g, "380"],  
  [/hai mươi chín/g, "29"],  
  [/bốn mươi mốt/g, "41"],  
  [/hai mươi lăm/g, "25"],  
  [/hai mươi tư/g, "24"],  
  [/một trăm/g, "100"],  
  [/mười/g, "10"],  
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/ phần trăm/g, "%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["phá sản", "sập", "mất", "thua", "giảm", "lỗ", "giải chấp", "thất nghiệp", "hoảng loạn", "nợ"];
export const GOOD = ["sống", "thắng", "lợi thế", "bình tĩnh", "ngủ ngon", "sống sót"];
