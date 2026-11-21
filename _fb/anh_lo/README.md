# Ảnh "sổ lỗ" FB chính (QL1 21/11)
Kiểu ảnh anh Huy chọn (FB chính từng lên view nhiều): màn hình app chứng khoán nền tối + thẻ trắng Giá vốn/Giá hiện tại/Lãi-Lỗ + câu meme to trong khung trắng + biểu đồ nến giảm.
- Giá THẬT (WiData eod_adjust). KHÔNG thẻ giá vốn/lãi lỗ, KHÔNG chữ chú thích/thương hiệu cuối ảnh (anh Huy 21/11).
- KHÔNG dùng ảnh người thật (lãnh đạo DN), không chế giễu cá nhân. Ưu tiên mã GIẢM mạnh (viral hơn). KHÔNG làm hình mua/bán: không điểm Mua/Bán trên biểu đồ, không kiểu "bán non" (anh Huy 21/11). Chú thích ghi "nắm giữ … từ ngày X".
- Câu meme ≤ 22 ký tự, không hô mua/bán, không dự báo.
- Chạy: sửa data.py (chuỗi giá đóng cửa, chỉ số phiên mua, số lượng, meme) → python3 data.py && python3 anh_lo.py lo.json
- Caption FB: dòng đầu IN HOA gây tò mò ("TIN SỐC MỚI NHẬN!!!"), không link/Zalo/hashtag.

## Bản chuẩn (anh Huy 21/11): chart ngày giống chungkhoanhuynguyen.com
- Dùng _fb/anh_lo/chart_web: nền trắng, nến xanh #1f8a57 / đỏ #c43c32, MA20 cam, MA50 tím, khối lượng dưới (lightweight-charts lwc.js của web).
- ohlc.txt: "MÃ MM-DD open high low close volume" (WiData eod_adjust ~6 tháng) → python3 lam.py → node shot.js (copy lwc.js từ gốc repo vào cùng thư mục).
- Bố cục: tên + giá + % đổi, câu meme khung đen, chart ngày. Không thẻ lãi/lỗ, không chú thích cuối, không điểm mua/bán. Ảnh người thật: anh Huy tự chèn khi đăng.

## Bản 3 (học ảnh mẫu VIX "Thư xin lỗi…" của anh Huy, 21/11)
- Đầu tối (#0b1222): tên, giá to + %, dòng Tham chiếu/Mở cửa/Thấp–Cao/KL.
- HOOK: dải trắng full ngang, chữ IN HOA đậm 1 dòng, kiểu câu chuyện/drama (không phải câu meme lửng).
- Chart ngày kiểu web + ĐIỂM KỸ THUẬT nhìn thấy: mũi tên đỏ + nhãn vàng viền đỏ (gãy nền, hồi chạm MA50, đỉnh, KL kỷ lục), đường ngang đứt đoạn (đáy/hỗ trợ đã thủng). cfg.json: hook, muc, diem.
- Chữ nhỏ chungkhoanhuynguyen.com góc phải dưới. Ảnh lãnh đạo: anh Huy tự chèn góc phải dưới khi đăng.

## Bản 4 (21/11): ẢNH VUÔNG 1080x1080
- HOOK phải hay tuyệt đối, hài hước tinh tế (chơi chữ/tục ngữ, không chế giễu cá nhân), 1 dòng tự co chữ. Vd: "Vàng thật không sợ lửa. Cổ phiếu vàng thì có." / "AI làm được hết, trừ giữ giá FPT."
- Điểm kỹ thuật kiểu chuyên nghiệp: vùng giá tô mờ (nền/kháng cự, nhãn phải), đường đứt đoạn xám (đáy), chấm tròn + nhãn viên thuốc đen chữ trắng + dây dẫn mảnh. Không mũi tên đỏ to.

## Bản 5 (21/11): phân tích sâu + ảnh minh họa từ web
- Chart bên trái; cột phải: hộp "GÓC NHÌN KỸ THUẬT" (xu hướng, cấu trúc/mô hình, tín hiệu, dòng tiền, kháng cự/hỗ trợ) + thẻ KQKD THẬT lấy từ data/kqkd.bin của web (giải mã xor+zlib, khoá trong index.html). Không bịa cảnh báo cũ.
- Bỏ chữ MA20/MA50 góc trái. Chỗ trống cột phải dưới: anh Huy dán ảnh lãnh đạo.
- Hook: chơi chữ tinh tế gắn với số thật (vd "Tiệm vàng mà cũng lỗ? PNJ làm được." / "Lãi tăng 12%, giá giảm 35%: thị trường chấm bằng AI à?").
