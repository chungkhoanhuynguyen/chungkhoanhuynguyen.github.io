// "Lớp học Lý thuyết trò chơi – Bài 1" (bản 7: mở bài kể đủ, 15/11/2026): mốc giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/I bơn Khan đun/g, "Ibn Khaldun"], [/A-ten/g, "Athens"], [/Hô me/g, "Homer"], [/Pla tông/g, "Plato"], [/Ma xê đô ni a/g, "Macedonia"], [/A lếch xan đơ/g, "Alexander"],
  [/Các ta gơ/g, "Carthage"], [/Su me/g, "Sumer"], [/Ti gơ rơ/g, "Tigris"], [/Ơ phơ rát/g, "Euphrates"], [/U rúc/g, "Uruk"], [/Ác cát/g, "Akkad"],
  [/A dơ tếch/g, "Aztec"], [/Cóc tê/g, "Cortés"], [/Pa kít xtan/g, "Pakistan"], [/Pla da/g, "Plaza"], [/Niu Oóc/g, "New York"], [/Cô đắc/g, "Kodak"], [/Nô ki a/g, "Nokia"],
  [/chứng khoán Huy Nguyễn/g, "Chứng Khoán Huy Nguyễn"],
  [/hai nghìn hai trăm năm/g, "2.200 năm"], [/hơn hai trăm năm/g, "hơn 200 năm"], [/hai nghìn năm/g, "2.000 năm"], [/Năm hai trăm hai mươi ba trước Công nguyên/g, "Năm 223 trước Công nguyên"], [/mười lạng/g, "10 lạng"], [/năm mươi lạng/g, "50 lạng"], [/sáu học trò/g, "6 học trò"],
  [/Hai nghìn hai trăm năm/g, "2.200 năm"], [/bảy nước/g, "7 nước"], [/Năm hai trăm hai mươi mốt trước Công nguyên/g, "Năm 221 trước Công nguyên"], [/Bài một/g, "Bài 1"],
  [/Hơn sáu trăm năm/g, "Hơn 600 năm"], [/ba thước đo/g, "3 thước đo"], [/khoảng mười năm/g, "khoảng 10 năm"], [/Năm một nghìn năm trăm mười chín/g, "Năm 1519"],
  [/khoảng năm trăm người/g, "khoảng 500 người"], [/Hai năm sau/g, "2 năm sau"], [/Năm một nghìn chín trăm tám mươi lăm/g, "Năm 1985"], [/năm nước lớn/g, "5 nước lớn"],
  [/mười đội/g, "10 đội"], [/hai ngày/g, "2 ngày"], [/Năm một nghìn chín trăm bảy mươi lăm/g, "Năm 1975"], [/Năm hai nghìn không trăm mười hai/g, "Năm 2012"],
  [/năm hai nghìn không trăm mười ba/g, "năm 2013"], [/ba câu/g, "3 câu"], [/thang mười điểm/g, "thang 10 điểm"], [/ba điểm/g, "3 điểm"], [/mười điểm/g, "10 điểm"],
  [/Giả định thứ nhất/g, "Giả định 1"], [/Giả định thứ hai/g, "Giả định 2"], [/Giả định thứ ba/g, "Giả định 3"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["mất", "thua", "suy", "sụp đổ", "phá sản", "tham nhũng", "chia rẽ", "khép kín", "bóc lột", "nợ"];
export const GOOD = ["năng lượng", "cởi mở", "gắn kết", "thắng", "sáng tạo", "thống nhất"];
