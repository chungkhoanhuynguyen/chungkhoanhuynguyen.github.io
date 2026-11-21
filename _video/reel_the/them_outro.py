"""Thêm cảnh OUTRO không lời vào timing.json + đệm im lặng cho voice.wav (để nhạc nền chạy hết outro), TRƯỚC khi mix/render:
python3 them_outro.py timing.json [voice.wav] [giay=3]"""
import json,sys,subprocess,os
p=sys.argv[1];w=sys.argv[2] if len(sys.argv)>2 else None;d=float(sys.argv[3]) if len(sys.argv)>3 else 3.0
t=json.load(open(p))
if not any(s["id"]=="OUT" for s in t["scenes"]):
    a=t["total"];t["scenes"].append({"id":"OUT","a":a,"b":round(a+d,3),"sens":[]});t["total"]=round(a+d,3)
    json.dump(t,open(p,"w"))
    if w:
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",w,"-af","apad=whole_dur=%f"%(t["total"]+1.2),w+".p.wav"],check=True);os.replace(w+".p.wav",w)
print("total",t["total"])
