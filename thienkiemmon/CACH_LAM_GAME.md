# Bộ cách làm game: rút từ Vương Quốc Huyền Thoại và các game khác

Dành cho các buổi làm Thiên Kiếm Môn sau này. Trước khi sửa game, đọc hết file này.
Nguồn: World of ClaudeCraft (MIT), bản fork là `chungkhoanhuynguyen/vuongquoc`. Đây là game MMO đã được kiểm thử kỹ trên điện thoại.

## 0. Nguyên tắc chung
- Người chơi chủ yếu dùng **điện thoại, màn ngang**. Mọi thứ phải thử trên trình duyệt giả lập điện thoại trước khi báo xong.
- **Không đụng tới web chứng khoán** và Firebase của nó. Game chỉ sửa trong thư mục của mình (`thienkiemmon/`, `vuongquoc/`…).
- Tiết kiệm token: sửa đúng chỗ bằng script thay chuỗi, không đọc lại cả file 230KB.
- Nội dung luôn bằng **tiếng Việt**, kể cả tên riêng (đọc kiểu Hán-Việt).

## 1. Điều khiển di chuyển (đã áp dụng cho Thiên Kiếm Môn ngày 24/11)
Các thông số lấy từ `src/game/mobile_controls.ts` và `camera_follow.ts` của bản gốc:
- **Cần gạt**: vùng chết `0.22` (chạm nhẹ không trôi), bán kính `48px`. Lượng gạt vượt qua vùng chết được co giãn lại thành 0..1.
- Khi không chạm, cần gạt **nằm sẵn ở góc trái dưới** với độ mờ 45%. Chạm vào nửa trái màn hình thì cần gạt nhảy tới chỗ ngón tay.
- **Rung nhẹ 6ms** khi bắt đầu nắm cần gạt (`navigator.vibrate(6)`).
- **Camera tự theo sau lưng** khi đi tới:
  - Tốc độ bám theo `6`, mỗi khung hình xoay tối đa `0.16`, trần `3.6 rad/s`.
  - Chỉ bám theo phần "đi tới" của cần gạt. Đi ngang thì camera không xoay, để nhân vật không đi vòng tròn.
  - Khi đang vuốt xoay camera bằng tay thì tắt bám theo.
- **Vuốt xoay camera** có vùng chết `6px`, để chạm bấm không làm giật camera.
- **Chụm hoặc mở 2 ngón** để zoom (độ nhạy `0.035`).
- **Chạm đúp** vào màn hình (trong 300ms) để đưa camera về sau lưng nhân vật.
- Nhân vật quay mặt mượt theo hướng đi. Tốc độ tăng và giảm dần, không đổi đột ngột.

## 2. Giữ màn hình sáng
Dùng `navigator.wakeLock.request('screen')`. Gọi lại khi trang hiện lại (`visibilitychange`), khi chạm màn hình và mỗi 15 giây. Thiên Kiếm Môn đã có.

## 3. Cài ra màn hình chính (PWA)
- Mỗi game có `app.webmanifest` riêng: `start_url`, `scope` và `id` đều là `/thienkiemmon/`. Có tên ngắn và biểu tượng **dạng hình** (không dùng chữ) cỡ 192 và 512, `purpose: any maskable`.
- Trong thẻ `<head>` thêm: `rel=manifest`, `apple-touch-icon` và `apple-mobile-web-app-title`.
- Thêm `?v=` vào đường dẫn biểu tượng mỗi khi đổi, để điện thoại không dùng bản cũ.
- Nếu manifest để `start_url: "/"`, bấm vào biểu tượng sẽ mở trang chứng khoán. Đây là lỗi đã gặp.

## 4. Tải nhanh, tải ngầm
- **Service worker** (`sw.js`, phạm vi thư mục game):
  - File có mã băm trong tên hoặc có `?v=` thì lấy từ bộ nhớ trước.
  - File không có mã băm thì trả bản đang lưu, rồi tải bản mới ở nền.
  - Trang HTML luôn lấy bản mới.
- **Danh sách tải trước** (`preload.json`): ghi lại mọi URL mà game tải khi vào thế giới, dùng một lần chạy Playwright để ghi. **Mỗi lần build lại phải tạo lại danh sách**, vì tên file JS đổi mã băm.
- **Tải ngầm** bằng Background Fetch (Chrome Android): vẫn tải khi người chơi chuyển app hay tắt màn hình, có thanh tiến trình ở thanh thông báo.
  - Nếu sau 20 giây chưa tải được gì thì hủy và chuyển sang tự tải trong service worker, 6 luồng cùng lúc.
- Hiện nhãn "Đang tải thế giới… %" ở đáy màn hình.
- Kết quả đo ở Vương Quốc Huyền Thoại: lần vào thứ hai chỉ còn 11 lượt tải mạng, so với khoảng 1.300 ở lần đầu.
- Không tải boss hay vật thể ở xa lúc mới vào. Tự hạ chất lượng khi FPS thấp (Thiên Kiếm Môn đã có hàm `adapt()`).

## 5. Tài khoản ID + mật khẩu (không cần máy chủ riêng)
- Dùng Firebase project **`thuthanhlacduong`**, là project riêng cho game, không phải của web chứng khoán.
  - Đăng ký và đăng nhập: `ID@<game>.game` kèm mật khẩu (Email/Password Auth).
  - ID dài 3–16 ký tự không dấu, mật khẩu ít nhất 6 ký tự.
- Dữ liệu nhân vật lưu ở `<game>_players/{uid}` dưới dạng `{name, save: chuỗi JSON, updated}`.
  - Tự lưu 30 giây một lần, và lưu ngay khi `pagehide` hoặc khi trang bị ẩn.
- **Quy tắc Firestore** cho mỗi bảng mới (chèn vào trước `match /{document=**}`):
  `match /<game>_players/{uid} { allow read, write: if request.auth != null && request.auth.uid == uid; }`
- Có nút "Chơi thử không lưu".
- Bản mẫu: `vuongquoc/acct/vq_acct.js`.

## 6. Lồng tiếng bằng giọng chủ game
- Bộ giọng nằm ở `_video/engine/giong.bin`, nạp bằng `hncodec.py` ở gốc kho. Đọc bằng `pip install vieneu` (chạy trên CPU được).
- Đoạn code mẫu: `_video/anim3d/vang/tts.py`. Cắt câu theo dấu chấm, cắt khoảng lặng, mỗi câu nghỉ 0,35 giây, xuất mp3 mono 64kbps.
- Thay `$N` và `{name}` bằng "hiệp sĩ" (hoặc "đại hiệp"). Đổi tên riêng sang Hán-Việt trước khi đọc.
- Tốc độ: khoảng 520 câu mất 40 phút với 2 tiến trình.

## 7. Việt hoá
- Ép ngôn ngữ ngay trong `<head>`: `localStorage.setItem('locale','vi')`.
- Tên riêng tiếng Anh đổi qua một hàm từ điển (`src/ui/vi_names.ts`): tên ghép dịch theo từng phần (Redbrook thành Hồng Khê, Highwatch thành Cao Vọng), tên người phiên âm.

## 8. Lối chơi người chủ game thích
- Thế giới mở, **ít nhiệm vụ bắt buộc**, tự khám phá. Không có đảo hướng dẫn bắt buộc.
- Lên cấp nhanh, quái đông. Có **người chơi ảo** đi lại, đánh quái, chat cho thế giới đông vui.
- Giao diện gọn: nút nhỏ, biểu tượng gọn, không che màn hình.

## 9. Kiểm thử trước khi báo xong
- Dùng Playwright giả lập điện thoại: `isMobile, hasTouch`, kích thước 844×390 (màn ngang).
  - Chạm và gạt bằng CDP `Input.dispatchTouchEvent`.
  - Dùng hàm `window.__mv()` để đọc vị trí, hướng và camera.
- swiftshader rất chậm với Thiên Kiếm Môn, chụp màn hình có thể quá thời gian. Hãy kiểm tra bằng số liệu, không cần ảnh.
- Thử cả trên link thật sau khi đưa lên (đợi khoảng 1–2 phút để GitHub Pages cập nhật).

## 10. Đưa lên web (kho `chungkhoanhuynguyen.github.io`)
- Dùng sparse checkout, chỉ lấy thư mục game.
- Commit xong thì `git rebase --onto origin/main <commit ngay trước commit của mình>`. **Không** rebase thường, vì sẽ phát lại commit của phiên khác.
- Đẩy lên bằng `git -c push.negotiate=true push origin HEAD:main`.
- Có thể có phiên khác đang sửa cùng game: luôn lấy bản mới nhất (`git checkout origin/main -- thienkiemmon`) trước khi sửa.

## 11. Bản quyền và quyền riêng tư
- Chỉ dùng mã nguồn có giấy phép MIT, Apache hoặc CC0. Model và âm thanh có ghi "phi thương mại" (NC) phải thay trước khi kiếm tiền.
- Gỡ mã theo dõi của bên thứ ba có trong mã nguồn gốc (Google Analytics, Meta Pixel của game cũ).

## 12. Chuyển động nhân vật bằng mocap (Thiên Kiếm Môn, 24/11)
- Bộ chuyển động lấy từ **KayKit Adventurers 1.0 (CC0)**, file `anim/kk.glb` chỉ còn khung xương và 27 clip (chạy, đi, đứng, nhảy, đòn 1 tay và 2 tay, bắn, thi pháp, trúng đòn, chết, ngồi…). Tạo lại bằng `stripanim.py` (bỏ mesh, chỉ giữ kênh xoay và độ cao hông).
- Chuyển sang xương VRM bằng cách so **độ lệch xoay so với tư thế chuẩn trong không gian nhân vật**: `target = deltaNguồn * restĐích`, rồi đổi về toạ độ của xương cha. Hàm `rtDrive()` làm việc này. Không cần đảo trục cho VRM0/VRM1.
- Tên xương có dấu chấm (`upperarm.l`) bị three.js đổi thành `upperarml`, nên phải dùng `PropertyBinding.sanitizeNodeName`.
- Vũ khí tự **đeo chéo sau lưng** sau 1,5 giây không đánh; đánh thì rút ra tay.
- Bot và lính ở xa hơn 35m (điện thoại) / 60m (máy tính) quay về hoạt ảnh tự viết cho nhẹ.
