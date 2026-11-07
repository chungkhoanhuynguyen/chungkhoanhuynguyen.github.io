# Bộ sinh nội dung NV1 (8/11/2026)
Dùng lại để đỡ tốn token: `CW=/tmp/cw python3 build.py <lô> [--ghi]` sinh lô kênh chính + `_kp`, tự kiểm kiem_loi + cap tuple.
- lib.py: số → chữ cho lời đọc (doc), nến tuần (weekly/circles), kqkd/fund/bctc.
- gen.py: mẫu dữ liệu thật – Đọc BCTC (bank/dn), HI (định giá), Y2 (soi BCTC: biên gộp, nợ vay, dòng tiền), TS (góp đều 3 triệu/tháng), K2 (so sánh nhóm + tỷ trọng cả nhóm). Mỗi video ≥1.250 chữ lời.
- hand.py: kịch bản viết tay (đổi KEY/nội dung mỗi lô). tp.py: trang phụ 7 ngày; fbc.py: 35 caption FB chính + nhom_fb.json; f0.py: bài F0 (mẫu).
Đổi mã/ngày trong build.py (lo_chinh, lo_kp) và ngày trong tp.py/fbc.py trước khi chạy.
