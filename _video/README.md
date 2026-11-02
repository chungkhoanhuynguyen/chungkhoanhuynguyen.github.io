# Xưởng video (GitHub Actions, miễn phí)
1. Đẩy lô vào `_video/queue/<LÔ>/`: `video_dai.py` (S["KEY"] = danh sách cảnh, mẫu NV1), `px_tuan.json` (nến tuần), `meta.json`.
2. Workflow `video.yml` tự chạy: giọng chốt Huy70_HaiDang30 (VieNeu-TTS v3 Turbo, Apache-2.0, `engine/giong.bin`) → dựng dx2 khung NGANG 1920x1080 cho YouTube video dài → nhạc nền → `KEY.mp4`, `KEY_bia.png`, `KEY_chuong.txt` (mốc chương thật).
3. Lấy kết quả: `git fetch origin video-out` (thư mục `<LÔ>/`) hoặc Release `video-<LÔ>`.
Loại cảnh hỗ trợ: hook (+chart nến tuần), cards, bars, checklist, image (ảnh trong engine/img), text, end.
