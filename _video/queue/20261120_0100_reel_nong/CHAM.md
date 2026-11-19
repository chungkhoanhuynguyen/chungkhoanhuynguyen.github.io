# TỰ CHẤM – lô 20261120_0100_reel_nong (bản 2, sau chấm độc lập)

Còn 4 Short. Đã bỏ SN2011MY (tin cũ từ 13/11, lạc đề) và SN2011DAU (vướng luật trung lập, lặp số) khỏi reel.json.

**Đã sửa theo chấm độc lập:**
- Mọi chữ "sáng nay / hôm nay / chiều nay / phiên như hôm nay" đổi thành mốc cụ thể "sáng 19/11", "phiên 19/11", "ngày 19/11", vì lô đăng từ 20/11.
- Giá Vietcombank 25.980 không còn ở Short nào. Short USD dùng số mới ngày 19/11 (VCB bán 25.900). Short IPO quy đổi theo tỷ giá trung tâm.

**Kiểm tra đã chạy:** kiem_loi đạt cả 4, JSON hợp lệ, hook ≤18 ký tự mỗi dòng. Dựng thử 20 thẻ the_so: không tràn chữ.

Độ dài ước theo âm tiết, lấy RV1911MY làm chuẩn, toc 1.12: VANG 50s, USD 46s, IPO 52s, XANG 47s. Riêng XANG đặt `keo_web: null` nên không có cảnh web.

| Key | Hook 2s | Đúng số | Giữ chân | Câu hỏi | TB |
|---|---|---|---|---|---|
| SN2011VANG | 9 | 9 | 8 | 9 | 8,8 |
| SN2011USD | 9 | 9 | 8 | 8 | 8,5 |
| SN2011IPO | 9 | 9 | 8 | 9 | 8,8 |
| SN2011XANG | 9 | 9 | 8 | 8 | 8,5 |

## Chi tiết từng Short
- **VANG:** câu hỏi đổi thành "thấy rẻ rồi / còn rẻ nữa". Cảnh 1: "Sáng 19/11, vàng thế giới vừa về 3.737 đô". Giữ chữ "vừa" để kiem_loi nhận ra cảnh 1 là tin mới. Số vàng nhẫn và SJC lấy từ bài gốc Tuổi Trẻ năm 2026.
- **USD:**
  - Hook mới "1.000 ĐÔ ĐẮT THÊM / 534 NGHÌN ĐỒNG?".
  - Số mới ngày 19/11: tỷ giá trung tâm 25.656 (tăng 4 đồng, kỷ lục mới), VCB 25.900, đô tự do 26.130.
  - 534 = 25.656 trừ mức đầu năm 25.122, mà mức đầu năm suy ra từ bài VnExpress 17/11.
  - Câu trần tỷ giá bị bỏ cho ngắn, thay bằng thẻ "nhận 1.000 USD kiều hối: thêm 534.000đ".
- **IPO:**
  - Đã đối chiếu: 83 USD, 81,3 tỷ, lỗ 104 tỷ là của 9 tháng đầu 2026.
  - Con số khoảng 80 tỷ ở bài tháng 10 là lỗ 6 tháng đầu năm (104 − 23,3 lỗ quý 3).
  - Lời đổi thành "chào sàn Nasdaq ngày 19/11", "như phiên 19/11 ở sàn HOSE". Quy đổi theo tỷ giá trung tâm cho ra gần 140 phiên.
- **XANG:**
  - Giá E5 18.576 khớp Tạp chí Công Thương và VTV.
  - Chuỗi là 5 lần giảm liên tiếp kể từ 1/11: 1/11, 3/11, 5/11, 12/11, 19/11. Ngày 29/10 xăng tăng.
  - Cảnh 1: "Từ 15 giờ ngày 19/11, xăng vừa giảm lần thứ 5 liên tiếp kể từ 1/11". Cảnh 5 đã cắt 1 câu.

## 3 điểm yếu thật
1. **Short USD có một số tự suy.** Con số 534 đồng / 534 nghìn ở hook là phép tính từ mức đầu năm 25.122, mà mức này suy từ bài VnExpress 17/11, chưa có bài nào ghi thẳng. Nếu NHNN công bố mức đầu năm khác thì hook lệch vài đồng. Trước khi dựng nên tra tỷ giá trung tâm ngày 2/1/2026.
2. **Thời lượng mới là ước tính.** Chưa đo bằng TTS thật. IPO ước 52s nhưng có nhiều số đọc dài ("tám mươi mốt phẩy ba", "một trăm lẻ tư") nên dễ vượt 55s. Nếu vượt, đặt `keo_web: null` như XANG.
3. **Lời đã cũ nếu đăng muộn.** Lô dùng mốc 19/11 nên đăng từ 22/11 trở đi là tin cũ. Riêng XANG sẽ sai thời sự ngay sau kỳ điều hành 26/11. Nên đăng hết trong 20–21/11. Ngoài ra, khi đăng phải dùng short_caption, không dùng file _mo_ta.txt (reel.py tự gắn web và Zalo vào file đó).

Ghi chú: Short IPO nói về Anthropic, công ty làm ra Claude. Lời giữ trung lập: nói rõ khoản lỗ, nói rõ kỳ lỗ, câu hỏi để ngỏ "cơ hội hay bong bóng".
