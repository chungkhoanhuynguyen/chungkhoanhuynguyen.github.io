# Live -> Shorts và Soi video đối thủ
Ý tưởng học từ các công cụ clip/hook mã nguồn mở; workflow chỉ dùng pip: yt-dlp, auto-editor, faster-whisper, ffmpeg.

**A. live_shorts** (Actions > Live to Shorts > Run): `url` = link video/live của @chungkhoanhuynguyen, `so_clip` (mặc định 5), `max_phut` (45). Ra release `live-<id>`: clip_N.mp4 (1080x1920, phụ đề, loudnorm -13) + clip_N.txt (tiêu đề gợi ý + transcript).
**B. soi_video**: `url` = video đối thủ. Ra `_kiem/soi/<id>.md` (thời lượng, số cảnh, TB/cảnh, cảnh 15s đầu, hook 60s) + ảnh lưới 12 khung ở release `soi-<id>`.
Nếu YouTube chặn IP GitHub (bot check): upload mp4 vào release `nguon-video`, rồi điền `release_asset` = tên file (bỏ trống `url`).
