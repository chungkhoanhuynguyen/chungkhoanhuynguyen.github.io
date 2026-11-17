// Phim TP1: mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/hai mươi lăm tháng mười một/g, "25/11"], [/hôm nay mới mười tám/g, "hôm nay mới 18"], [/ba chi tiết/g, "3 chi tiết"],
  [/hai nghìn không trăm mười tám/g, "2018"], [/hai nghìn không trăm hai mươi hai/g, "2022"],
  [/Chín giờ sáng/g, "9 giờ sáng"], [/bảy trăm triệu/g, "700 triệu"], [/lãi chín phần trăm/g, "lãi 9%"], [/hai mươi chín tuổi/g, "29 tuổi"],
  [/một trăm hai mươi lăm triệu đồng/g, "125 triệu đồng"], [/tháng mười một/g, "tháng 11"], [/tháng mười/g, "tháng 10"],
  [/mười ba lô/g, "13 lô"], [/mười lăm nghìn sáu trăm tỷ đồng/g, "15.600 tỷ đồng"], [/tám phẩy bảy phần trăm/g, "8,7%"], [/chín phẩy chín/g, "9,9%"],
  [/từ nửa đến một điểm phần trăm/g, "từ 0,5 đến 1 điểm %"], [/trang mười hai/g, "trang 12"], [/hai mươi năm/g, "20 năm"],
  [/ba mươi lăm nghìn tám trăm người/g, "35.800 người"], [/ba mươi nghìn tỷ đồng/g, "30.000 tỷ đồng"], [/bốn câu/g, "4 câu"], [/câu thứ tư/g, "câu thứ 4"],
  [/một hai năm/g, "1–2 năm"], [/vài phần trăm/g, "vài %"], [/Một, /g, "1, "], [/Hai, /g, "2, "], [/Ba, /g, "3, "], [/Bốn, /g, "4, "],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["tự chịu rủi ro", "chiếm đoạt", "không có bảo hiểm", "lạnh người", "hối thúc", "giảm", "mất", "nhầm", "rủi ro"];
export const GOOD = ["sổ tiết kiệm", "bảo hiểm tiền gửi", "an toàn", "chia vốn", "đọc kỹ", "mua đều", "không vay", "hủy được"];
