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

## Kiểu "so sánh 2 thời điểm" (học mẫu VIC vs vàng SJC của anh Huy)
- cfg "hop": khung đỏ quanh 2 nến + chữ đỏ to viền trắng ("PNJ: 68.200 đ/cp / Vàng SJC: 147,2 tr/lượng"), số thật (WiData; SJC id 1224211). Hook ngắn đối lập số: "Vàng giảm 9%. Tiệm bán vàng giảm 80%."
- Mẫu MSR (meme + % tăng to khoanh đỏ): KHÔNG dùng nhân vật có bản quyền (Minion…) và KHÔNG bịa câu nói của người thật; dùng ý tưởng: 1 ý duy nhất, chữ ít, % đổi to.

## Học kênh Phan Linh Stock (bài PNJ 20/11: 1,8K cảm xúc, 298 bình luận)
- Sức hút nằm ở CAPTION: "Tin sốc mới nhận!!!" + tin NÓNG có báo đăng (nhân sự, kết quả kinh doanh) kể như chuyện, ẩn dụ đời thường, kết bằng 1 câu đùa tình huống ("bao giờ về lại 85 thì gọi tao dậy").
- Bình luận đầu của tác giả: phân tích cân bằng (vấn đề + điểm sáng), tạo thảo luận.
- Ảnh: 1 ý, hook nói kiểu đời thường + emoji; gắn TIN lên chart (mốc ngày tin ra).
- Mình: kiểm tin trên báo trước khi viết, không hashtag/link trong caption, không hô mua bán, không bịa số.

## Đăng FB chính (anh Huy 21/11 15:05)
- Viết bài ở facebook.com/post/create?locale=vi_VN → mục "Chia sẻ lên nhóm" → giữ/chọn 9 nhóm chứng khoán (FB giới hạn 9) → Đăng. Đăng NGAY (khi chọn nhóm, nút Lên lịch bị khoá).
- Ảnh: device_stage_files ảnh từ máy anh (file ai\anh_fb) rồi file_upload đường dẫn /mnt/user-data/uploads/... (đường dẫn D:\ và /mnt/user-data/outputs bị từ chối; fetch raw.githubusercontent bị CSP chặn).
- Sau khi đăng: bình luận đầu phân tích 2 chiều dưới bài.

## VĂN PHONG ANH HUY (21/11 – anh sửa: "không là ko, được là đc")
- Viết tắt như anh: ko (không), đc (được), cp (cổ phiếu), cty (công ty), 1 (một) với số đếm.
- Câu ngắn, nói thẳng, hơi cà khịa, ít văn hoa/ẩn dụ dài. Dùng "???" khi bức xúc/mỉa. Tối đa 1 emoji (🥲) cuối bài.
- Xưng "Huy" trong bài công khai, gọi "mọi người"/"anh chị". Không "ạ", không lời lẽ kiểu báo chí.
- Mở "TIN SỐC MỚI NHẬN!!!" khi có tin nóng thật; kết bằng 1 câu đùa tình huống hoặc câu hỏi mở.
- Caption bài FPT 21/11 theo văn phong này: _fb/anh_lo/out/FPT_2111.txt (dùng bản này khi đăng 20:00).
