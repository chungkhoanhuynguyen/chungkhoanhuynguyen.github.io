// QL1 11/11 – bản ổn định của up.js (dán qua javascript_tool, KHÔNG eval được vì CSP):
// - meta lấy qua api.github.com (raw.githubusercontent bị cache)
// - __go(tiền_tố_khối, KEY_meta, 'kenh5.json'): ghép khối <tiền_tố>_pNN, điền tiêu đề/mô tả ({LINK} thay bằng window.__LINK)
// - KHÔNG chạy cả chuỗi trong 1 lệnh: gọi __next3() rồi __fin(ngày,'HH:MM') ở lệnh riêng (chuỗi dài > 45s làm CDP treo, vòng lặp nền bị kẹt ở lịch)
// Quy trình: __open() → __go(...) → upload bìa vào input file của "Hình thu nhỏ" → __next3() → __fin(18,'20:00')
// (Hàm giống phiên QL1 11/11; xem lịch sử commit để lấy mã đầy đủ.)
