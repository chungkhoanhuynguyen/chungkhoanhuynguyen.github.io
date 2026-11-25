#!/bin/bash
# tu_soat.sh OUTDIR KEY – SOÁT TỰ ĐỘNG ngay trên GitHub Actions sau khi dựng (anh Huy 21/11: "tận dụng GitHub", tiết kiệm token).
# Làm sẵn mọi bước máy móc mà trước đây NV1/QL1 phải ngồi chờ rồi tự làm trong phiên Claude (soat.sh):
#   KEY_khung1.png, KEY_khung2.png (khung mỗi 20s, lưới 5x5), KEY_bia3.png (3 bìa), KEY_shorts.png (khung 3 Shorts),
#   KEY_soat.txt: QC + whisper + âm lượng + dò phụ đề lỗi + danh sách ảnh + (nếu có GEMINI_API_KEY) Gemini xem khung tìm lỗi hình.
# Người soát chỉ cần tải KEY_soat.txt + các ảnh png này (vài trăm KB) thay vì tải cả video.
TD="$(cd "$(dirname "$0")" && pwd)"; O=$1; K=$2; cd "$O" || exit 0; O="$(pwd)"  # 22/11 QL1: đường dẫn tuyệt đối – trước đó gemini_soat.py không chạy được sau cd
[ -f "$K.mp4" ] || { echo "LỖI: không có $K.mp4 (dựng hỏng)" > ${K}_soat.txt; exit 0; }
DT="drawtext=text='%{pts\:hms}':x=5:y=5:fontsize=18:fontcolor=yellow:box=1:boxcolor=black"
# chỉ dùng ffmpeg (máy reel có thể không có ffprobe): lấy thời lượng + chiều khung từ dòng thông tin
INFO=$(ffmpeg -hide_banner -i $K.mp4 2>&1)
DUR=$(echo "$INFO" | grep -o "Duration: [0-9:]*" | head -1 | awk -F'[: ]' '{print $3*3600+$4*60+$5}')
WH=$(echo "$INFO" | grep -o "Video:.* [0-9]\{3,4\}x[0-9]\{3,4\}" | grep -o "[0-9]\{3,4\}x[0-9]\{3,4\}" | head -1)
W=${WH%x*}; H=${WH#*x}
if [ "${H:-0}" -gt "${W:-1}" ]; then   # video dọc (reel/Shorts): khung mỗi 4s, lưới 6x2
  ffmpeg -v error -y -i $K.mp4 -vf "fps=1/4,scale=200:-1,$DT,tile=6x2" -frames:v 1 ${K}_khung1.png
  [ "${DUR:-0}" -gt 48 ] && ffmpeg -v error -y -ss 48 -i $K.mp4 -vf "fps=1/4,scale=200:-1,$DT,tile=6x2" -frames:v 1 ${K}_khung2.png
else
  ffmpeg -v error -y -i $K.mp4 -vf "fps=1/20,scale=384:-1,$DT,tile=5x5" -frames:v 1 ${K}_khung1.png
  [ "${DUR:-0}" -gt 500 ] && ffmpeg -v error -y -ss 500 -i $K.mp4 -vf "fps=1/20,scale=384:-1,$DT,tile=5x5" -frames:v 1 ${K}_khung2.png
fi
B=""; for s in "" _b _c; do [ -f ${K}_bia$s.png ] && B="$B -i ${K}_bia$s.png"; done
N=$(echo $B | grep -o -- "-i" | wc -l)
if [ "$N" -ge 2 ]; then
  F=""; L=""; for i in $(seq 0 $((N-1))); do F="$F[$i]scale=640:-1[v$i];"; L="$L[v$i]"; done
  ffmpeg -v error -y $B -filter_complex "${F}${L}hstack=$N" ${K}_bia3.png
fi
S=""; for s in 1 2 3; do [ -f ${K}_S$s.mp4 ] && ffmpeg -v error -y -ss 1 -i ${K}_S$s.mp4 -vf "fps=1/8,scale=200:-1,tile=6x1" -frames:v 1 /tmp/s$s.png && S="$S -i /tmp/s$s.png"; done
NS=$(echo $S | grep -o -- "-i" | wc -l); [ "$NS" -ge 1 ] && ffmpeg -v error -y $S -filter_complex "vstack=$NS" ${K}_shorts.png 2>/dev/null || { [ "$NS" = 1 ] && cp /tmp/s1.png ${K}_shorts.png; }
{
  echo "== SOÁT TỰ ĐỘNG $K ($(date -u +%F' '%H:%M) UTC) – thời lượng ${DUR}s"
  echo "== QC (dòng LỖI = không được đăng)"; cat ${K}_qc.txt 2>/dev/null || echo "(xưởng không tạo file QC cho loại video này)"
  echo "== ÂM LƯỢNG"; ffmpeg -nostats -i $K.mp4 -filter_complex ebur128 -f null - 2>&1 | grep -A1 "Integrated loudness" | tail -1
  echo "== PHỤ ĐỀ ĐÁNG NGỜ"
  grep -nE "Mỗi 5|20[0-9]0 [a-zà-ỹ]|phần 100|em em|[0-9] [a-zà-ỹ]+\?|[0-9],[0-9] [0-9]|000\.000 tỷ|[0-9]\.[0-9]{3}\.[0-9]{3}|[0-9] 0 |nhà em|phần 1[0-9]{2}| 1 phần" $K.srt 2>/dev/null | head -20 || true
  echo "== ẢNH DÙNG"; head -40 ${K}_anh.txt 2>/dev/null
  echo "== FILE"; ls ${K}* | tr '\n' ' '; echo
} > ${K}_soat.txt 2>&1
if [ -n "$GEMINI_API_KEY" ]; then
  timeout 480 python3 "$TD/gemini_soat.py" "$O" "$K" >> ${K}_soat.txt 2>&1 || echo "== GEMINI: lỗi/hết giờ (bỏ qua)" >> ${K}_soat.txt
else
  echo "== GEMINI: chưa có secret GEMINI_API_KEY (bỏ qua bước xem khung bằng AI)" >> ${K}_soat.txt
fi
exit 0
