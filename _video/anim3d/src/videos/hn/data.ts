// Phim #3 "Thế giới chuẩn bị cho chiến tranh hạt nhân? – Quang Hà": mốc thời gian giọng đọc + phụ đề.
import TIM from "./timing.json";
export type Sen = { text: string; a: number; b: number };
export type ScT = { id: string; a: number; b: number; sens: Sen[] };
export const TIMING = TIM as { total: number; scenes: ScT[] };
export const FPS = 30;
export const TAIL = 4.0;
export const TOTAL_F = Math.ceil((TIMING.total + TAIL) * FPS);
export const sc = (id: string) => TIMING.scenes.find((s) => s.id === id)!;
const REP: [RegExp, string][] = [
  [/Cường Sô xiu/g, "Cường Sociu"], [/ép pê tê/gi, "FPT"], [/vê xê bê/gi, "VCB"], [/hát pê giê/gi, "HPG"], [/vê en em/gi, "VNM"], [/pích bôn/g, "pickleball"],
  [/chứng khoán huy nguyễn chấm com/g, "chungkhoanhuynguyen.com"], [/viên i ốt/g, "viên i-ốt"], [/Ucraina/g, "Ukraine"], [/sô pha/g, "sofa"],
  [/một trăm bốn mươi triệu/g, "140 triệu"], [/ba trăm triệu/g, "300 triệu"], [/một tỷ một lượng/g, "1 tỷ một lượng"], [/ba mươi nghìn/g, "30 nghìn"], [/ba trăm nghìn/g, "300 nghìn"], [/ba triệu/g, "3 triệu"],
  [/ba lượng/g, "3 lượng"], [/hai lượng/g, "2 lượng"], [/Mười một giờ đêm/g, "11 giờ đêm"], [/ngày mười hai tháng mười một/g, "ngày 12/11"], [/Đêm mười hai tháng mười một/g, "Đêm 12/11"],
  [/ngày mười ba tháng mười một/g, "ngày 13/11"], [/Tối mười ba tháng mười một/g, "Tối 13/11"], [/Sáng mười bốn/g, "Sáng 14/11"], [/một tỷ hai/g, "1,2 tỷ"],
  [/sáu trăm triệu/g, "600 triệu"], [/một trăm năm mươi triệu/g, "150 triệu"], [/Năm năm/g, "5 năm"], [/năm năm/g, "5 năm"], [/một mét bốn bảy/g, "1m47"],
  [/một triệu lượt xem/g, "1 triệu lượt xem"], [/tám mươi lăm giây/g, "85 giây"], [/ba ngày/g, "3 ngày"], [/chín mươi ngày/g, "90 ngày"], [/chín mươi tám ký/g, "98 ký"],
  [/năm sáu hai/gi, "năm 1962"], [/Năm sáu hai/g, "Năm 1962"], [/chín triệu chín/g, "9,9 triệu"], [/mười suất/g, "10 suất"], [/ba combo/g, "3 combo"], [/Ba combo/g, "3 combo"],
  [/ba thùng/g, "3 thùng"], [/Ba thùng/g, "3 thùng"], [/gần ba mươi triệu/g, "gần 30 triệu"], [/Năm hai nghìn không trăm linh một/g, "Năm 2001"], [/mười một tháng chín/g, "11/9"],
  [/bốn ngày/g, "4 ngày"], [/Năm hai nghìn không trăm hai mươi hai/g, "Năm 2022"], [/Hai mươi phút/g, "20 phút"], [/Sáu giờ sáng/g, "6 giờ sáng"], [/Tám giờ/g, "8 giờ"],
  [/một trăm ba mươi lăm triệu/g, "135 triệu"], [/một trăm ba mươi tám triệu/g, "138 triệu"], [/hai trăm bảy mươi sáu triệu/g, "276 triệu"], [/sáu triệu/g, "6 triệu"],
  [/Chín giờ sáng/g, "9 giờ sáng"], [/bốn mươi chín nghìn một trăm đồng/g, "49.100 đồng"], [/năm mươi ba nghìn sáu/g, "53.600"], [/hai mươi mốt nghìn/g, "21.000"],
  [/năm mươi ba nghìn năm/g, "53.500"], [/năm mươi nghìn một trăm/g, "50.100"], [/gần mười bảy triệu/g, "gần 17 triệu"], [/hai mươi chín triệu bảy/g, "29,7 triệu"],
  [/Mười, chín, ba, hai, một/g, "10, 9… 3, 2, 1"], [/bốn dòng/g, "4 dòng"], [/từ ba đến sáu tháng/g, "từ 3 đến 6 tháng"], [/Một, quỹ/g, "1. Quỹ"], [/Hai, không/g, "2. Không"],
  [/Ba, viết/g, "3. Viết"], [/Bốn, trước/g, "4. Trước"], [/một đêm/g, "một đêm"], [/một tỷ, mà/g, "1 tỷ, mà"], [/Tháng Một/g, "Tháng 1"], [/Tháng Hai/g, "Tháng 2"], [/Tháng Mười/g, "Tháng 10"],
];
export const subText = (s: string) => REP.reduce((x, [r, v]) => x.replace(r, v), s);
export const BAD = ["mất", "giả", "hoảng", "nợ", "bán sạch", "thiệt", "chiến tranh", "hạt nhân", "giảm", "hết tiền", "vay"];
export const GOOD = ["kế hoạch", "cái đầu lạnh", "quỹ dự phòng", "hồi lại", "chuẩn bị"];
