// Số liệu thật (WiData, giá SJC – nghìn đồng/lượng; vàng thế giới CME – USD/ounce) + tiện ích mốc thời gian.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0; // logo cuối
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;

// vàng nhẫn SJC 99,99 bán ra – cuối tháng (1224247)
export const RING_M: [string, number][] = [["01/25", 88000], ["02/25", 90400], ["03/25", 101200], ["04/25", 116500], ["05/25", 114000], ["06/25", 116000], ["07/25", 117100], ["08/25", 125000], ["09/25", 132900], ["10/25", 146700], ["11/25", 151900], ["12/25", 148900], ["01/26", 180000], ["26/02", 184000]];
// vàng miếng SJC bán ra – từng ngày 10/2 → 25/3/2026 (1224211)
export const SJC_D: [string, number][] = [["10/2", 181020], ["11/2", 181020], ["12/2", 181020], ["13/2", 179020], ["14/2", 181020], ["23/2", 184620], ["24/2", 184620], ["25/2", 185320], ["26/2", 184020], ["27/2", 184020], ["2/3", 190920], ["3/3", 188220], ["4/3", 184220], ["5/3", 184720], ["6/3", 183820], ["9/3", 184120], ["10/3", 186120], ["11/3", 187220], ["12/3", 186320], ["13/3", 184820], ["16/3", 183120], ["17/3", 183020], ["18/3", 183020], ["19/3", 175520], ["20/3", 176120], ["23/3", 166020], ["24/3", 170220], ["25/3", 173520]];
// vàng nhẫn bán ra – cuối tháng 2/2026 → 13/11/2026
export const RING_26: [string, number][] = [["26/2", 184000], ["2/3", 189400], ["31/3", 174700], ["29/4", 165500], ["31/5", 158800], ["30/6", 146900], ["31/7", 141400], ["29/8", 148200], ["30/9", 143600], ["31/10", 135800], ["13/11", 137800]];
// vàng miếng SJC bán ra – 5 phiên gần nhất
export const SJC_NOW: [string, number][] = [["9/11", 141220], ["10/11", 140920], ["11/11", 140020], ["12/11", 139020], ["13/11", 138020]];
// vàng thế giới CME (USD/oz) – cuối tuần 2026
export const WORLD: [string, number][] = [["4/1", 4372.5], ["1/2", 4740.37], ["1/3", 5386.98], ["29/3", 4447.65], ["3/5", 4614.01], ["31/5", 4539.67], ["28/6", 4062.71], ["26/7", 4094.18], ["23/8", 4624.29], ["20/9", 4372.82], ["18/10", 4184.99], ["1/11", 3898.31], ["6/11", 4074.9], ["13/11", 3892.0]];

/** tiêu đề phụ đề: đổi chữ số đọc thành con số cho dễ nhìn */
const REP: [RegExp, string][] = [
  [/một trăm ba mươi ba triệu tám trăm nghìn đồng/g, "133,8 triệu đồng"], [/một trăm tám mươi tư triệu/g, "184 triệu"], [/một trăm chín mươi mốt triệu/g, "191 triệu"],
  [/một trăm bốn mươi tám triệu/g, "148 triệu"], [/một trăm hai mươi triệu/g, "120 triệu"], [/chín trăm hai mươi triệu/g, "920 triệu"], [/sáu trăm sáu mươi chín triệu/g, "669 triệu"],
  [/hai trăm năm mươi mốt triệu/g, "251 triệu"], [/ba trăm bốn mươi chín triệu/g, "349 triệu"], [/sáu trăm triệu/g, "600 triệu"], [/[Hh]ai trăm triệu/g, "200 triệu"],
  [/tám mươi tám triệu/g, "88 triệu"], [/hai mươi tư triệu/g, "24 triệu"], [/mười bảy triệu/g, "17 triệu"], [/bảy triệu/g, "7 triệu"], [/hơn ba triệu/g, "hơn 3 triệu"],
  [/ba nghìn chín trăm đô la một ounce/g, "3.900 USD/ounce"], [/hai nghìn người/g, "2.000 người"], [/năm lượng/g, "5 lượng"], [/Mười năm/g, "10 năm"], [/mười năm/g, "10 năm"],
  [/tám năm/g, "8 năm"], [/mười tuổi/g, "10 tuổi"], [/mùng tám/g, "mùng 8"], [/mùng chín/g, "mùng 9"], [/Ba giờ sáng/g, "3 giờ sáng"], [/Bốn giờ sáng/g, "4 giờ sáng"],
  [/Tám giờ sáng/g, "8 giờ sáng"], [/Chín giờ tối/g, "21 giờ"], [/hai tiếng/g, "2 tiếng"], [/ba viên/g, "3 viên"], [/Bốn ngày sau, mùng hai tháng Ba/g, "4 ngày sau, mùng 2/3"],
  [/Chỉ hai tuần sau/g, "Chỉ 2 tuần sau"], [/Từ ngày mười tám đến ngày hai mươi ba tháng Ba/g, "Từ 18/3 đến 23/3"], [/ba phiên/g, "3 phiên"], [/bốn phiên/g, "4 phiên"],
  [/tháng Tám/g, "tháng 8"], [/Tháng Mười Một/g, "Tháng 11"], [/mười chín tháng/g, "19 tháng"], [/chứng khoán huy nguyễn chấm com/g, "chungkhoanhuynguyen.com"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["giảm", "mất", "lỗ", "trượt", "nợ", "khóc", "mổ", "ốm", "bẫy", "sai", "nước mắt", "nói dối", "giấu", "rơi", "lạnh buốt", "đòi", "vay"];
export const GOOD = ["lãi", "tăng", "kế hoạch", "giữ giá", "đỉnh", "tỉnh táo"];
