#!/bin/bash
# soat.sh TAG KEY  (NV1 15/11: soát video dài 1 lệnh; OUT=thư mục ra, mặc định /tmp/soat)
TAG=$1; K=$2; D=${OUT:-/tmp/soat}/$K; mkdir -p $D; cd $D
U=https://github.com/chungkhoanhuynguyen/chungkhoanhuynguyen.github.io/releases/download/$TAG
for f in $K.mp4 $K.srt ${K}_qc.txt ${K}_anh.txt ${K}_canh.json ${K}_bia.png ${K}_bia_b.png ${K}_bia_c.png ${K}_S1.mp4 ${K}_S2.mp4 ${K}_S3.mp4 ${K}_shorts.json; do timeout 180 curl -sSfL -o $f $U/$f || echo "thieu $f"; done
echo "== QC"; cat ${K}_qc.txt; echo
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $K.mp4); echo "dur $DUR"
ffmpeg -nostats -i $K.mp4 -filter_complex ebur128 -f null - 2>&1 | grep -A1 "Integrated loudness" | tail -1
ffmpeg -v error -y -i $K.mp4 -vf "fps=1/20,scale=384:-1,drawtext=text='%{pts\:hms}':x=5:y=5:fontsize=18:fontcolor=yellow:box=1:boxcolor=black" -frames:v 1 -vsync vfr x.png 2>/dev/null
ffmpeg -v error -y -i $K.mp4 -vf "fps=1/20,scale=384:-1,drawtext=text='%{pts\:hms}':x=5:y=5:fontsize=18:fontcolor=yellow:box=1:boxcolor=black,tile=5x5" -frames:v 1 tile1.png
ffmpeg -v error -y -ss 500 -i $K.mp4 -vf "fps=1/20,scale=384:-1,drawtext=text='%{pts\:hms}':x=5:y=5:fontsize=18:fontcolor=yellow:box=1:boxcolor=black,tile=5x5" -frames:v 1 tile2.png
ffmpeg -v error -y -i ${K}_bia.png -i ${K}_bia_b.png -i ${K}_bia_c.png -filter_complex "[0]scale=640:-1[a];[1]scale=640:-1[b];[2]scale=640:-1[c];[a][b][c]hstack=3" bia3.png
for s in 1 2 3; do [ -f ${K}_S$s.mp4 ] && ffmpeg -v error -y -ss 1 -i ${K}_S$s.mp4 -vf "fps=1/8,scale=200:-1,tile=6x1" -frames:v 1 s$s.png; done
echo "== SRT grep"; grep -nE "Mỗi 5|20[0-9]0 [a-zà-ỹ]|phần 100|em em|[0-9] [a-zà-ỹ]+\?|[0-9],[0-9] [0-9]|000\.000 tỷ|[0-9]\.[0-9]{3}\.[0-9]{3}" $K.srt | head -20
echo "== ANH"; cat ${K}_anh.txt | head -40
