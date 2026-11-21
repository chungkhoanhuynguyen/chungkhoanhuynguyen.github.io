"""render.py bản tiết kiệm đĩa: chụp từng đoạn 96 khung -> mã hóa đoạn -> xóa khung -> nối + ghép âm."""
import sys,os,json,subprocess,shutil,tempfile
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import render as R
from concurrent.futures import ProcessPoolExecutor
def seg(a):
    k,f0,f1,plan,fps,W,out=a
    tmp=tempfile.mkdtemp(prefix="seg_")
    R.chup((k,f0,f1,plan,fps,W,tmp))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(fps),"-start_number",str(f0),"-i",os.path.join(tmp,"f%05d.jpg"),"-c:v","libx264","-preset","medium","-crf","24","-pix_fmt","yuv420p","-g",str(fps*2),out],check=True)
    shutil.rmtree(tmp,ignore_errors=True);return out
if __name__=="__main__":
    cfgp,tmp_,outp=[os.path.abspath(x) for x in sys.argv[1:4]];fps=int(sys.argv[4]);W=int(sys.argv[5])
    os.chdir(R.ROOT)
    cfg=json.load(open(cfgp));tm=json.load(open(tmp_))
    plan={"cfg":cfg,"timing":tm,"px":R.lay(cfg["ma"],cfg.get("gia_n",125))}
    n=int((tm["total"]+0.3)*fps);S=96;work=tempfile.mkdtemp(prefix="segout_")
    jobs=[(i,f,min(f+S,n),plan,fps,W,os.path.join(work,"s%03d.mp4"%i)) for i,f in enumerate(range(0,n,S))]
    with ProcessPoolExecutor(2) as ex: segs=list(ex.map(seg,jobs))
    lst=os.path.join(work,"l.txt");open(lst,"w").write("".join("file '%s'\n"%s for s in segs))
    wav=os.path.join(os.path.dirname(tmp_),"mix.wav")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-i",wav,"-c:v","copy","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",outp],check=True)
    shutil.rmtree(work,ignore_errors=True);print("XONG",outp)
