# NV1 15/11: khung giữa mỗi cảnh (KEY_canh.json) + khung lớn 960px; chạy sau soat.sh
import json,subprocess,sys,os
K=sys.argv[1]; D=os.environ.get('OUT','/tmp/soat')+'/'+K; os.chdir(D)
c=json.load(open(K+'_canh.json')); fs=[]
for i,s in enumerate(c):
    t=s['a']+min(4.5,(s['e']-s['a'])*0.7); f='c%02d.png'%i
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',K+'.mp4','-frames:v','1','-vf','scale=480:-1,drawtext=text=%d %s:x=6:y=6:fontsize=20:fontcolor=yellow:box=1:boxcolor=black'%(i+1,s['k']),f]); fs.append(f)
    if s['k'] in ('bars','text','cards','bignum','checklist'):
        subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',K+'.mp4','-frames:v','1','-vf','scale=960:-1','L%02d_%s.png'%(i+1,s['k'])])
# tile 4 cols
import math
n=len(fs); rows=math.ceil(n/4)
for part in range(0,n,16):
    sub=fs[part:part+16]; args=[]
    for f in sub: args+=['-i',f]
    k=len(sub); cols=4; r=math.ceil(k/cols)
    lay='|'.join('%d_%d'%((j%cols)*480, (j//cols)*270) for j in range(k))
    subprocess.run(['ffmpeg','-v','error','-y']+args+['-filter_complex','xstack=inputs=%d:layout=%s:fill=black'%(k,lay) if k>1 else 'null','g%d.png'%(part//16)])
print(n,'canh')
