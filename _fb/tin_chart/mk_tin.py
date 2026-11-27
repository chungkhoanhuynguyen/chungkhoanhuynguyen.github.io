"""ĐÃ THAY (anh Huy 27/11 11:00 chọn kiểu ảnh 'VIC metro'): dùng mk_chart.py – file này chỉ chuyển tiếp.
Cấu hình (mảng JSON, mỗi phần tử 1 ảnh 1080x1080), mẫu đã làm: out/fb_2711.json (VN-Index nến, SJC đường, tỷ giá đường):
 ra: _fb/tin_chart/out/<KEY>.jpg · ten, sym (dòng phụ: nguồn/đơn vị) · gia (số to), doi (dòng dưới số), mau_doi 'xanh'|'do'
 st: [[nhãn, giá trị], …] 3 cặp số thật · hook1 (dòng đen, câu chuyện/trớ trêu) · hook2 (dòng nền vàng, chốt bằng con số)
 loai 'nen': ma (mã có trong data/c, vd VNINDEX/VIC), den_ngay (phiên đã đóng cửa), n · loai 'duong': series [{mau, diem:[[YYYY-MM-DD, số], …]}]
 diem: [{t, g, chu, dx, dy}] nhãn viên thuốc đen chỉ vào mốc THẬT (đỉnh, đáy, ngày có tin) · muc: [{g, chu}] đường đứt đoạn
 vung: [{tren, duoi, chu, trai}] vùng tô mờ · nguon: dòng nguồn nhỏ cuối ảnh (BẮT BUỘC).
Luật: số nào trên ảnh cũng phải khớp nguồn; không điểm mua/bán, không dự báo; mở ảnh xem lại (chữ không đè nhau) trước khi giao."""
import os, sys, runpy
sys.argv[0] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mk_chart.py')
runpy.run_path(sys.argv[0], run_name='__main__')
