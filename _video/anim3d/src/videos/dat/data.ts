// Phim #2 "Hùng Xa Lộ – đất nền": mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Bây jing ích bảy/g, "Beijing X7"], [/Dũng Gym mơ/g, "Dũng Gymmer"], [/chứng khoán huy nguyễn chấm com/g, "chungkhoanhuynguyen.com"],
  [/Hai giờ sáng/g, "2 giờ sáng"], [/hai giờ sáng/g, "2 giờ sáng"], [/mười bảy/g, "17"], [/Năm năm/g, "5 năm"], [/năm năm/g, "5 năm"],
  [/chín mươi mét vuông/g, "90 m²"], [/ba tỷ đồng/g, "3 tỷ đồng"], [/ba trăm triệu/g, "300 triệu"], [/hai mươi sáu tuổi/g, "26 tuổi"],
  [/mười hai tiếng/g, "12 tiếng"], [/âm mười độ/g, "âm 10 độ"], [/một tỷ rưỡi/g, "1,5 tỷ"], [/Tháng Mười năm ngoái/g, "Tháng 10 năm ngoái"],
  [/quý bốn năm hai nghìn không trăm hai mươi lăm/g, "quý IV/2025"], [/sáu mươi triệu đồng một mét vuông/g, "60 triệu đồng/m²"], [/sáu mươi triệu một mét vuông/g, "60 triệu/m²"],
  [/sáu mươi triệu một mét/g, "60 triệu một mét"], [/năm tỷ rưỡi/g, "5,5 tỷ"], [/Năm tỷ rưỡi/g, "5,5 tỷ"], [/tháng Mười Hai/g, "tháng 12"], [/ba tháng nữa bảy tỷ/g, "3 tháng nữa 7 tỷ"],
  [/bốn tỷ rưỡi/g, "4,5 tỷ"], [/ba tỷ rưỡi/g, "3,5 tỷ"], [/bốn tỷ/g, "4 tỷ"], [/ba tỷ/g, "3 tỷ"], [/Ba tỷ/g, "3 tỷ"], [/Một tỷ/g, "1 tỷ"],
  [/tám trăm triệu/g, "800 triệu"], [/hai trăm triệu/g, "200 triệu"], [/Ngày hai mươi tháng Mười Hai/g, "Ngày 20/12"], [/ba năm/g, "3 năm"],
  [/mười ba phần trăm/g, "13%"], [/hơn ba mươi hai triệu/g, "hơn 32 triệu"], [/Ba tháng/g, "3 tháng"], [/Quý hai năm nay/g, "Quý II năm nay"],
  [/hơn bảy mươi ba nghìn/g, "hơn 73.000"], [/sáu mươi phần trăm/g, "60%"], [/Ngày mười lăm/g, "Ngày 15"], [/ba mươi hai triệu năm trăm nghìn đồng/g, "32,5 triệu đồng"],
  [/bốn trăm nghìn/g, "400 nghìn"], [/mười hai triệu/g, "12 triệu"], [/một phần ba/g, "1/3"], [/hai phần trăm/g, "2%"], [/tháng Bảy/g, "tháng 7"],
  [/Tháng Sáu/g, "Tháng 6"], [/Tháng Tám/g, "Tháng 8"], [/ba mươi triệu/g, "30 triệu"], [/hai mươi triệu/g, "20 triệu"], [/năm triệu một mét vuông/g, "5 triệu/m²"],
  [/Tháng Mười,/g, "Tháng 10,"], [/ba chữ/g, "ba chữ"], [/một tỷ tám/g, "1,8 tỷ"], [/Gần mười một tháng/g, "Gần 11 tháng"], [/ba trăm năm mươi bảy triệu/g, "357 triệu"],
  [/gần bốn tỷ/g, "gần 4 tỷ"], [/một tỷ hai/g, "1,2 tỷ"], [/Đọc năm phút/g, "Đọc 5 phút"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["nợ", "mất", "lỗ", "khóc", "quá hạn", "chặn", "thiếu", "lãi ngân hàng", "đặt cược", "sợ", "giảm", "cắt lỗ", "thế chấp", "vay"];
export const GOOD = ["kế hoạch", "giữ được", "nhẹ tênh", "làm lại", "điểm dừng"];
