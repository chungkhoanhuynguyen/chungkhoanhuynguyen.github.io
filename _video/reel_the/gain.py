import sys,subprocess,re
w=sys.argv[1];tgt=-13.0
def meas(f):
    o=subprocess.run(["ffmpeg","-nostats","-i",f,"-af","ebur128","-f","null","-"],capture_output=True,text=True).stderr
    return float(re.findall(r"I:\s+(-?[0-9.]+) LUFS",o)[-1])
import os
for it in range(4):
    a=meas(w)
    if abs(a-tgt)<0.15:break
    g=tgt-a
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",w,"-af","volume=%fdB,alimiter=limit=0.89:level=disabled"%g,"-ar","44100",w+".t.wav"],check=True)
    os.replace(w+".t.wav",w)
print("after",meas(w))
