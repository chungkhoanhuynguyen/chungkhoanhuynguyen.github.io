// "Lớp học Lý thuyết trò chơi – Bài 3" (bản 7: mở bài kể đủ, 15/11/2026): mốc giọng đọc + phụ đề.
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
  [/Ních xơn/g, "Nixon"],
  [/Brét tơn Út/g, "Bretton Woods"],
  [/ao xơ/g, "ounce"],
  [/Tơ ri phin/g, "Triffin"],
  [/A rập Xê út/g, "Ả Rập Xê Út"],
  [/Vôn cơ/g, "Volcker"],
  [/Lê man Bờ ra đơ/g, "Lehman Brothers"],
  [/Oa sinh tơn/g, "Washington"],
  [/Bài ba/g, "Bài 3"],
  [/hai nghìn không trăm hai mươi hai/g, "2022"],  
  [/một nghìn chín trăm bảy mươi mốt/g, "1971"],  
  [/một nghìn chín trăm bốn mươi tư/g, "1944"],  
  [/một nghìn chín trăm bảy mươi tư/g, "1974"],  
  [/hai nghìn không trăm linh tám/g, "2008"],  
  [/một nghìn chín trăm sáu mươi/g, "1960"],  
  [/một nghìn chín trăm tám mươi/g, "1980"],  
  [/sáu mươi sáu phần trăm/g, "66%"],  
  [/hai mươi phần trăm/g, "20%"],  
  [/một nghìn năm trăm/g, "1.500"],  
  [/sáu mươi phần trăm/g, "60%"],  
  [/mười ba phần trăm/g, "13%"],  
  [/mười phần trăm/g, "10%"],  
  [/chín trăm mười/g, "910"],  
  [/bốn phần trăm/g, "4%"],  
  [/Năm mươi lăm/g, "55"],  
  [/hai mươi bảy/g, "27"],  
  [/Bốn mươi bốn/g, "44"],  
  [/ba mươi lăm/g, "35"],  
  [/chín mươi/g, "90"],  
  [/mười lăm/g, "15"],  
  [/sáu mươi/g, "60"],  
  [/tám trăm/g, "800"],  
  [/bốn mươi/g, "40"],  
  [/mười một/g, "11"],  
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/ phần trăm/g, "%"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["mất", "phá sản", "khủng hoảng", "quỵt", "giảm", "lạm phát", "đổ vỡ", "hoảng loạn", "mất giá", "thất nghiệp"];
export const GOOD = ["lòng tin", "bình tĩnh", "sống sót", "rẻ nhất"];
