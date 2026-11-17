// Phim RAC1: mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/bảy mã/g, "7 mã"], [/bảy lần/g, "7 lần"], [/Cả bảy/g, "Cả 7"], [/cả bảy/g, "cả 7"],
  [/Một trăm mười bốn triệu đô la/g, "114 triệu đô la"], [/một trăm mười bốn triệu đô la/g, "114 triệu đô la"], [/ba mươi năm/g, "30 năm"], [/hai mươi chín tỷ đô/g, "29 tỷ đô"],
  [/mười sáu tháng mười một/g, "16/11"], [/tháng mười một/g, "tháng 11"], [/năm phẩy hai phần trăm/g, "5,2%"], [/ba mươi lần/g, "30 lần"], [/bảy mươi bảy tỷ đô la/g, "77 tỷ đô la"],
  [/một phần năm/g, "1/5"], [/bảy mã/g, "7 mã"], [/Tháng ba/g, "Tháng 3"], [/hai mươi phần trăm/g, "20%"], [/Tháng sáu/g, "Tháng 6"], [/lỗ ba mươi/g, "lỗ 30%"], [/Tháng chín/g, "Tháng 9"],
  [/hai mươi tuổi/g, "20 tuổi"], [/năm mươi hai cân/g, "52 cân"], [/Mười năm, ba buổi/g, "10 năm, 3 buổi"], [/ba buổi/g, "3 buổi"], [/mười năm/g, "10 năm"], [/bốn câu/g, "4 câu"],
  [/Ba tháng/g, "3 tháng"], [/ba doanh nghiệp/g, "3 doanh nghiệp"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["lỗ", "tin nóng", "khí thải", "tranh cãi", "cạnh tranh", "vay"];
export const GOOD = ["dòng tiền", "nhàn rỗi", "chia vốn", "kiên nhẫn", "giữ được", "lãi"];
