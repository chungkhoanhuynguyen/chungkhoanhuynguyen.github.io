"""Giữ khung hook (ảnh bìa) đứng yên N giây đầu video, xóa phụ đề trên khung đó.
python3 giu_bia.py in.mp4 out.mp4 [giay=1.2]  -> out.mp4 + out_bia.jpg"""
import sys,subprocess
from PIL import Image
src,dst=sys.argv[1],sys.argv[2];g=float(sys.argv[3]) if len(sys.argv)>3 else 1.2
bia=dst.rsplit('.',1)[0]+'_bia.jpg';tmp='/tmp/_hk0.png'
subprocess.run(['ffmpeg','-v','error','-y','-ss','0','-i',src,'-frames:v','1',tmp],check=True)
im=Image.open(tmp).convert('RGB');W,H=im.size;k=H/1280
y0,y1=int(960*k),int(1040*k);patch=im.crop((0,int(1045*k),W,int(1045*k)+(y1-y0)))
im.paste(patch,(0,y0));im.save(tmp);im.save(bia,quality=93)
fps=subprocess.run(['ffprobe','-v','error','-select_streams','v','-show_entries','stream=r_frame_rate','-of','csv=p=0',src],capture_output=True,text=True).stdout.strip()
ms=int(g*1000)
subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-t',str(g),'-r',fps,'-i',tmp,'-i',src,'-filter_complex',
 f'[0:v]format=yuv420p,setsar=1[a];[1:v]format=yuv420p,setsar=1[b];[a][b]concat=n=2:v=1:a=0[v];[1:a]adelay={ms}|{ms}[au]',
 '-map','[v]','-map','[au]','-c:v','libx264','-preset','veryfast','-crf','20','-c:a','aac','-b:a','160k','-movflags','+faststart',dst],check=True)
print('XONG',dst,bia)
