# Đọc chọn lọc tệp trong zip ở xa (GitHub release) bằng HTTP Range – không tải cả gói.
import re, subprocess, struct, zlib, json, os, sys
API="https://api.github.com/repos/chungkhoanhuynguyen/chungkhoanhuynguyen.github.io/releases/assets/"
def url(aid): return subprocess.run(["curl","-sS","-o","/dev/null","-w","%{redirect_url}","-H","Accept: application/octet-stream",API+str(aid)],capture_output=True,text=True).stdout
def rng(u,a,b): return subprocess.run(["curl","-sS","-r",f"{a}-{b}",u],capture_output=True).stdout
def cdir(aid,size):
    u=url(aid); tail=rng(u,size-65557,size-1); i=tail.rfind(b"PK\x05\x06")
    n,cs,co=struct.unpack("<HII",tail[i+10:i+20])
    cd=rng(u,co,co+cs-1); out={}; p=0
    while p<len(cd) and cd[p:p+4]==b"PK\x01\x02":
        meth,=struct.unpack("<H",cd[p+10:p+12]); csz,usz,fl,el,cl=struct.unpack("<IIHHH",cd[p+20:p+34]); off,=struct.unpack("<I",cd[p+42:p+46])
        nm=cd[p+46:p+46+fl].decode(); out[nm]=(meth,csz,usz,off); p+=46+fl+el+cl
    return u,out
def get(u,ent):
    meth,csz,usz,off=ent; h=rng(u,off,off+29); fl,el=struct.unpack("<HH",h[26:30]); d=rng(u,off+30+fl+el,off+30+fl+el+csz-1)
    return d if meth==0 else zlib.decompress(d,-15)
if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="index":
        idx={}
        for aid,size in [(764591203,928500968),(764592813,527874378),(764593599,841724965)]:
            u,cd=cdir(aid,size); idx[aid]={k:v for k,v in cd.items()}; print(aid,len(cd))
        json.dump(idx,open(sys.argv[2],"w"))
    elif cmd=="pull":
        idx=json.load(open(sys.argv[2])); out=sys.argv[3]; names=sys.argv[4].split(",")
        for aid,cd in idx.items():
            want=[k for k in cd if k.split("/")[2:3] and k.split("/")[2] in names and not k.endswith("/") and not re.search(r"_(arm|nor_gl|nor_dx|rough|metal|ao|disp|spec|bump)_",k)]
            if not want: continue
            u=url(aid)
            for k in want:
                dst=os.path.join(out,"/".join(k.split("/")[2:])); os.makedirs(os.path.dirname(dst),exist_ok=True)
                open(dst,"wb").write(get(u,cd[k])); print(k,cd[k][2])
