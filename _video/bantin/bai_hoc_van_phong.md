# Sổ tự cải tiến lời văn Bản tin Phong Thần
Cập nhật mỗi Chủ nhật (QL1) và ngay khi anh Huy góp ý. NV1 đọc file này TRƯỚC khi viết mỗi bản tin.

## Đã duyệt (giữ)
- 6/11 – anh Huy chấm bản 1: 70%, "chưa đủ hài, muốn thâm thúy, ngẫm xong mới thấy hay". Bản 2 đạt.
- Công thức mỗi cảnh: số liệu thật → ví von đời thường lật ngược cách nhìn → 1 câu đúc kết ngắn.
- Hook trên khung là câu tò mò theo sự kiện chính của phiên (VD "VIC KÉO CẢ LỚP").
- Câu kết hỏi về chính người xem (bán / mua / ngồi im).

## Tránh
- Đùa nhạt, chơi chữ vô nghĩa (VD "vườn cà chua").
- Câu dài trên 30 từ, câu cụt thiếu chủ ngữ, câu miễn trừ, xin bình luận.

## Đo hiệu quả (mỗi Chủ nhật)
- Lấy lượt xem, % xem hết, bình luận của 5 bản tin trong tuần (TikTok, Shorts, Reels).
- Bản tin top 1 và bản thấp nhất: ghi 1 dòng vì sao (hook, câu ví von, chủ đề), rút 1 quy tắc mới vào mục "Đã duyệt" hoặc "Tránh".

## 6/11 tối – anh Huy: "bổ sung thêm tin tức và nhiều hình ảnh hơn, nhất là tin tức thế giới"
- Mỗi số BẮT BUỘC có khối THẾ GIỚI (2–3 cảnh) ngay sau câu mở: Mỹ đêm qua (ảnh Phố Wall/NYSE) → thẻ hinh/the_gioi.png (S&P, Nasdaq, Dow, Nikkei, KOSPI, vàng, Brent, DXY) → so sánh với VN (ảnh sàn châu Á).
- Câu mở nêu luôn tin thế giới lớn nhất + VN-Index (điểm, %). Hook 2 tầng kiểu "MỸ –4%, NHẬT HÀN –6%" / "VIỆT NAM CHỈ –0,9%".
- Xen ảnh thật giữa các thẻ số: không để 2 thẻ số liền nhau quá 3 cảnh.
- Câu thâm thúy mẫu đã dùng: "Kỳ vọng giống chiếc thang máy: đi lên từng tầng, đi xuống một mạch." / "Tiền không biến mất, tiền chỉ chạy về chỗ nó thấy an toàn." / "Thế giới hắt hơi, Việt Nam có khi cảm muộn vài phiên." (không lặp lại ở số sau)
- Dữ liệu: du_lieu.json có the_gioi.chi_so (pct từng mã), the_gioi.tin (tiêu đề mac.bin), vn_index.

## 6/11 – bài học của QL1 (anh Huy nhắc "từ đầu không bổ sung luôn")
- Khi dựng chương trình mới: rà HẾT nguồn dữ liệu web đang có (mw, mwh, rs, news, wm, mac, vimo…) và đưa vào ngay bản đầu, không chờ anh Huy nhắc.
- Ngày thế giới biến động mạnh (chỉ số lớn ±2% trở lên) thì tin thế giới lên câu mở, không để cuối.

## 7/11 – Video dài YouTube (anh Huy chê "đang ngang đổi sang dọc", nhạc to, thumb chưa chuẩn)
- Cảnh chữ video ngang phải là ảnh tràn khung 16:9 (land_text.py), cấm dán khung dọc reel vào giữa.
- Nhạc nền: chuẩn hoá RMS, thấp hơn giọng ~20 dB; video kể chuyện dùng lo-fi cả bài ("nhac": "lofi" trong meta.json).
- Bìa: giữ đúng 2 dòng bia_hook + nhãn đỏ (badge); không dùng ký tự →; không nến giả lập khi có ảnh thật.
- Trước khi giao: rút 12 khung (ffmpeg tile) xem tận mắt + đo âm lượng, rồi mới tải lên.
- Thay video đã hẹn: tải bản mới cùng giờ rồi chuyển bản cũ sang Riêng tư (không xoá).
