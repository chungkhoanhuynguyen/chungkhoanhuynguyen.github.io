# CHẤM GÓC KHÁN GIẢ KHÓ TÍNH – NONG2511A (vàng miếng lỗ 58 triệu)

Người chấm đóng vai người xem YouTube tài chính, không phải người viết. Số cảnh đếm từ 1 theo thứ tự trong video_dai.py (22 cảnh).

## Bảng điểm

| Mục | Điểm | Lý do ngắn |
|---|---|---|
| Hook 15 giây | 6 | Ba cái tên (Duyên, Thơm, nhóm Zalo) và nghề nghiệp dồn vào 15 giây đầu. Con số 58 triệu tới khoảng giây thứ 10, nằm giữa câu dài. Người lỗ là chị Thơm nhưng không lên hình. |
| Tiêu đề + bìa (CTR) | 6 | Tiêu đề 80 ký tự với hai con số. Trên điện thoại vế "Đắt Hơn Thế Giới 21 Triệu" bị cắt. Chữ "Vàng miếng lỗ" nghe lạ, vì người lỗ chứ vàng không lỗ. Bìa A "ĐU ĐỈNH LỖ 58 TRIỆU / ĐÁY Ở ĐÂU?" ổn (7). Badge "NÓNG" cho số liệu ngày 19/11 mà đăng 25/11 làm mất lòng tin. |
| Giữ chân giữa video | 6 | Muốn tắt ở cảnh 7 (quy đổi ounce sang lượng), ở chuỗi cảnh 13–14–15 (ba thẻ số liền nhau, khoảng 80 giây, cảnh 14 đọc tên ba tổ chức) và ở cảnh 20 (nhắc lại cảnh 2). Cảnh 16 là độc thoại dài qua điện thoại, nhồi ba chính sách. Ý "lỗ 5,6 triệu ở quầy" lặp ba lần ở cảnh 10, 12 và 13. |
| Cú lật | 6 | Ý lật "rẻ so với đỉnh, đắt so với thế giới" đã lộ ở tiêu đề, ở bìa B và ở cảnh 2. Tới cảnh 11 người xem đã biết trước nên không còn bất ngờ. |
| Bài học dùng được | 7 | Bốn việc đều đúng. Riêng việc 1 ("tự quy đổi") không ai làm được khi đứng ở tiệm nếu chưa có công thức nhẩm. Việc 4 hay và cụ thể. |
| Câu hỏi kết (bình luận) | 7 | Dễ trả lời bằng một con số. Nhưng câu hỏi bảo khán giả đoán GIÁ đáy, trái với bài học vừa nói ("đừng đo bằng giá, đo bằng khoảng chênh"). Nó cũng mời người xem dự báo. |
| Không hô mua/bán, không dự báo | 6 | Cảnh 14 nêu "UBS cân nhắc mua thêm khi dưới 4.000 USD" trong khi giá đang 3.725 USD, người xem nghe ra là "UBS bảo mua". Cảnh 15 có câu "người vội bắt đáy có thể đang mua ở giữa dốc", nghe như dự báo còn giảm. Bìa C "CÒN 15 TRIỆU NỮA?" cũng giống dự báo. Cảnh 19 đưa ra ngưỡng mua cụ thể ("chênh còn 15 triệu thì mua"), người xem sẽ chép làm tín hiệu. |

**Điểm trung bình: 6,3/10.** Bản tự chấm trong CHAM.md cho đồng loạt 8/10, như vậy là chấm cao hơn thực tế.

Điểm mạnh thật: ý "đáy có hai tầng" rõ và mới. Các phép tính khớp nhau (5,6 / 11,9 / 12,9 / 122,6 triệu). Cảnh tỷ dụ "thang máy – cầu thang bộ" (cảnh 5) đắt. Câu chốt ở cảnh 19 "mua vàng chứ không mua khoảng chênh" đáng nhớ.

## Sửa cụ thể từng mục dưới 8

### 1. Hook (cảnh 1). Đưa con số lỗ lên câu đầu, bớt nhân vật
Thay toàn bộ `say` cảnh 1:
> "Một trăm chín mươi mốt triệu lúc mua. Một trăm ba mươi ba triệu lúc bán. Chị Thơm mua một lượng vàng miếng đúng đỉnh tháng một, chiều nay lỗ hơn năm mươi tám triệu. Vậy mà nhóm Zalo của chị vẫn hô: vàng về đáy năm rồi, gom đi. Đêm qua vàng thế giới rơi hơn ba phần trăm, vàng trong nước chỉ nhích xuống năm trăm nghìn. Đáy thật nằm ở đâu, và ai đang trả tiền cho khoảng lệch đó?"

Giới thiệu chị Duyên (kế toán xưởng gỗ) dời sang đầu cảnh 3.

### 2. Tiêu đề, bìa và độ "nóng"
- Tiêu đề thay (khoảng 55 ký tự, trên điện thoại không bị cắt):
  **"Mua Vàng Đỉnh Tháng 1, Giờ Lỗ 58 Triệu: Đáy Thật Ở Đâu?"**
  Phương án B: **"Vàng Rơi 3%, Vàng Miếng Gần Như Không Giảm: Vì Sao?"**
- Bỏ bìa C ("CÒN 15 TRIỆU NỮA?") vì giống dự báo. Thay bằng: `["RẺ SO VỚI ĐỈNH", "ĐẮT SO VỚI THẾ GIỚI"]`.
- Đăng 25/11 thì phải cập nhật giá sáng 24–25/11 vào cảnh 1, 2, 7, 8, 15. Nếu không cập nhật thì bỏ chữ "NÓNG" và đổi mọi "chiều nay / đêm qua" thành ngày cụ thể.

### 3. Giữ chân giữa video
- Cảnh 7: rút lời còn 2 câu: "Giá thế giới quy ra tiền Việt khoảng một trăm mười sáu triệu một lượng. Vàng miếng bán một trăm ba mươi bảy triệu hai: cứ một trăm đồng bỏ ra, mười tám đồng là phần trả thêm." Chi tiết ounce và tỷ giá chỉ để trên tờ giấy.
- Cảnh 13–15: chèn một cảnh 3D ngắn giữa cảnh 14 và 15, hoặc biến cảnh 14 thành lời anh Khải nói. Ví dụ, anh Khải qua điện thoại: "Bên Tai Wong bảo có thể về ba nghìn ba, ba nghìn bốn trong vài tuần. Goldman thì bảo ba đến sáu tháng tới còn sóng. Chẳng ai dám nói chắc đâu chị." Thẻ cards cảnh 14 bỏ dòng UBS.
- Cảnh 12 và 13: bỏ câu "vừa bước khỏi cửa tiệm là đã lỗ năm triệu sáu" ở cảnh 12 (đã nói ở cảnh 10).
- Cảnh 16: cắt còn một chính sách. Thay bằng: "Khách xếp hàng mua khi thế giới rơi, khoảng chênh phình ra. Đám đông ngừng mua, nó xẹp rất nhanh. Phần vàng thật thì còn, phần chênh là phần dễ bốc hơi nhất." Chuyện 11 hồ sơ, thuế và sàn vàng chuyển thành 1 dòng `cap`.
- Cảnh 20: bỏ, hoặc gộp câu "đo bằng khoảng chênh, đừng đo bằng mức giảm từ đỉnh" vào lời cảnh 21.

### 4. Cú lật. Giấu đến cảnh 11
- Cảnh 2: không nói "hai tầng" và "đắt hơn thế giới" ngay. Thay lời bằng câu treo: "Trước khi trả lời đáy ở đâu, anh chị nhớ giúp em con số này: hai mươi mốt triệu. Nó nằm trong giá mỗi lượng vàng anh chị mua, nhưng không nằm trong miếng vàng. Đến chương bốn anh chị sẽ thấy vì sao nó quyết định lời lỗ." Thẻ bignum đổi `top` thành "PHẦN TIỀN KHÔNG NẰM TRONG MIẾNG VÀNG".
- Bìa B ("ĐẮT HƠN THẾ GIỚI 21 TRIỆU") chỉ dùng cho A/B test, không dùng làm bìa chính.

### 5. Bài học. Cho công thức nhẩm đứng tại quầy
Cảnh 17, việc 1 đổi thành: `('Giá thế giới (USD) × 31 = nghìn đồng/lượng', GREEN)`. Lời đọc:
> "Một, lấy giá thế giới tính bằng đô nhân ba mươi mốt, ra số nghìn đồng một lượng. Ví dụ ba nghìn bảy trăm hai mươi lăm nhân ba mươi mốt, khoảng một trăm mười sáu triệu. Lấy giá tiệm trừ đi số đó là ra khoảng chênh."

### 6. Câu hỏi kết. Hỏi đúng bài học, không mời đoán giá
Cảnh 22, `cap` và lời thay:
> cap: ("VÀNG ĐẮT HƠN THẾ GIỚI BAO NHIÊU", "THÌ ANH CHỊ MỚI MUA?")
> say: "Còn anh chị thì sao? Chị Thơm đang chờ hồi vốn, chị Duyên đang chờ khoảng chênh. Bảng quy đổi em để trên chungkhoanhuynguyen.com. Anh chị ghi một con số xuống bình luận: vàng trong nước đắt hơn thế giới bao nhiêu triệu một lượng thì anh chị mới thấy đáng mua? Và anh chị đang ở phe chị Thơm hay phe chị Duyên?"

Fb_post cũng đổi câu hỏi tương tự.

### 7. Gỡ chỗ nghe như hô mua hoặc dự báo
- Cảnh 14: bỏ thẻ UBS "Dưới 4.000 USD – Cân nhắc mua thêm" và bỏ câu đọc về UBS.
- Cảnh 15, câu cuối thay bằng: "Không ai biết kịch bản này có xảy ra hay không. Nhưng nó cho thấy: giá đã giảm nhiều chưa chắc đã hết đường giảm, vì còn tầng khoảng chênh." Bỏ cụm "mua ở giữa dốc".
- Cảnh 19: đổi ngưỡng cố định thành nguyên tắc của riêng nhân vật. Thay câu đó bằng: "Chị tự đặt cho mình một mức chênh chấp nhận được, thấp hơn hôm nay khá nhiều, và chỉ mua dần từng chỉ khi chạm mức đó." `cap` đổi thành ("EM GỬI TIẾP 150 TRIỆU", "40 TRIỆU CHỜ KHOẢNG CHÊNH HẠ").

## 5 sửa quan trọng nhất (theo thứ tự)
1. Cập nhật số liệu 24–25/11, hoặc bỏ chữ "NÓNG" và "đêm qua": đăng tin 6 ngày tuổi dưới badge NÓNG là mất lòng tin ngay.
2. Viết lại cảnh 1: con số "191 mua, 133 bán, lỗ 58 triệu" lên câu đầu, chỉ một nhân vật trong 15 giây.
3. Gỡ ba chỗ nghe như khuyến nghị hay dự báo: thẻ UBS (cảnh 14), câu "mua ở giữa dốc" (cảnh 15), ngưỡng "15 triệu thì mua" (cảnh 19). Bỏ bìa C.
4. Phá chuỗi thẻ số ở cảnh 13–15 bằng lời anh Khải hoặc một cảnh 3D. Cắt cảnh 20 và các câu lặp "5,6 triệu".
5. Đổi câu hỏi kết thành "đắt hơn thế giới bao nhiêu thì mới mua, ghi một con số" và rút tiêu đề còn khoảng 55 ký tự.

Sau khi sửa đủ 7 mục trên, ước tính điểm trung bình lên khoảng 7,8–8.
