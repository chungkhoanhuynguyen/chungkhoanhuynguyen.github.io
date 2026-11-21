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
