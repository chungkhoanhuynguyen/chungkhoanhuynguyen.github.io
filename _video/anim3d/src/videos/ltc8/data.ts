// "Lớp học Lý thuyết trò chơi – Bài 2" (bản 7: mở bài kể đủ, 15/11/2026): mốc giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/ba, bốn phần trăm/g, "3–4%"], [/mười hai, mười ba phần trăm/g, "12–13%"], [/hai phần ba/g, "2/3"],
  [/Pô tô xi/g, "Potosí"],
  [/Đi ê gô Oan pa/g, "Diego Huallpa"],
  [/Bô li vi a/g, "Bolivia"],
  [/Phê líp Đệ nhị/g, "Philip II"],
  [/Phê líp/g, "Philip"],
  [/Am xtéc đam/g, "Amsterdam"],
  [/Uy li am xứ Ô ranh/g, "William xứ Orange"],
  [/Bài hai/g, "Bài 2"],
  [/sáu học trò/g, "6 học trò"],
  [/hai nghìn không trăm hai mươi hai/g, "2022"],  
  [/một nghìn năm trăm chín mươi sáu/g, "1596"],  
  [/một nghìn năm trăm bốn mươi lăm/g, "1545"],  
  [/một nghìn năm trăm năm mươi bảy/g, "1557"],  
  [/một nghìn năm trăm bảy mươi lăm/g, "1575"],  
  [/một nghìn sáu trăm bảy mươi hai/g, "1672"],  
  [/một nghìn sáu trăm tám mươi tám/g, "1688"],  
  [/một nghìn sáu trăm chín mươi tư/g, "1694"],  
  [/một nghìn chín trăm bốn mươi tư/g, "1944"],  
  [/một nghìn sáu trăm ba mươi bảy/g, "1637"],  
  [/một nghìn sáu trăm linh chín/g, "1609"],  
  [/một nghìn năm trăm sáu mươi/g, "1560"],  
  [/một nghìn sáu trăm linh hai/g, "1602"],  
  [/một triệu hai trăm nghìn/g, "1.200.000"],  
  [/mười ba phần trăm/g, "13%"],  
  [/bốn phần trăm/g, "4%"],  
  [/tám phần trăm/g, "8%"],  
  [/bốn mươi/g, "40"],  
  [/mười tám/g, "18"],  
  [/năm mươi/g, "50"],  
  [/một trăm/g, "100"],  
  [/hai trăm/g, "200"],  
  [/mười hai/g, "12"],  
  [/ba mươi/g, "30"],  
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/ phần trăm/g, "%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["vỡ nợ", "phá sản", "quỵt", "sập", "nợ", "lãi rất cao", "chậm trả", "ôm nợ", "không trả"];
export const GOOD = ["lòng tin", "giữ lời", "minh bạch", "thắng", "bền"];
