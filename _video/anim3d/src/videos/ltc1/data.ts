// Lớp học Lý thuyết trò chơi – Bài 1: mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Ha na/g, "Hana"], [/Chi Hô/g, "Ji-ho"], [/Kha lít/g, "Khalid"], [/Xô phi a/g, "Sophia"], [/Ken chi/g, "Kenji"], [/I bơn Khan đun/g, "Ibn Khaldun"],
  [/Cô đắc/g, "Kodak"], [/Nô ki a/g, "Nokia"], [/A lếch xan đơ/g, "Alexander"], [/Ma xê đô ni a/g, "Macedonia"], [/A dơ tếch/g, "Aztec"], [/Xi li côn/g, "Silicon"], [/Mê hi cô/g, "Mexico"],
  [/năm hai trăm hai mươi mốt trước Công nguyên/g, "năm 221 TCN"], [/Năm ba trăm ba mươi tám trước Công nguyên/g, "Năm 338 TCN"], [/Năm một nghìn năm trăm mười chín/g, "Năm 1519"],
  [/Năm một nghìn ba trăm bảy mươi bảy/g, "Năm 1377"], [/Năm một nghìn chín trăm bảy mươi lăm/g, "Năm 1975"], [/Năm hai nghìn không trăm mười hai/g, "Năm 2012"], [/năm hai nghìn không trăm mười ba/g, "năm 2013"],
  [/ba trăm năm/g, "300 năm"], [/sáu chữ/g, "6 chữ"], [/sáu học trò/g, "6 học trò"], [/năm trăm lính/g, "500 lính"], [/hơn sáu trăm năm/g, "hơn 600 năm"], [/ba đến bốn thế hệ/g, "3 đến 4 thế hệ"],
  [/thang mười điểm/g, "thang 10 điểm"], [/ba điểm/g, "3 điểm"], [/Bài một/g, "Bài 1"], [/hàng trăm nghìn dân/g, "hàng trăm nghìn dân"], [/Hai năm sau/g, "2 năm sau"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["thua", "sụp đổ", "phá sản", "đánh rơi", "lười", "chia nhau", "đậu mùa"];
export const GOOD = ["năng lượng", "cởi mở", "gắn kết", "thống nhất"];
