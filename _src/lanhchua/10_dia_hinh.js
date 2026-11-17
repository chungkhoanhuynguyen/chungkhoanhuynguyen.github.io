const CW=6400,CH=4000,GAP=900,C0W=WMAP?2*CW+GAP:CW,C0H=WMAP?2*CH+GAP:CH,CWc=[C0W,CW,CW,CW,CW,CW,CW,CW,CW,CW,CW,CW,0],CHc=[C0H,CH,CH,CH,CH,CH,CH,CH,CH,CH,CH,CH,0],
 OX=WMAP?[0,2*(CW+GAP),2*(CW+GAP),3*(CW+GAP),3*(CW+GAP),4*(CW+GAP),5*(CW+GAP),4*(CW+GAP),5*(CW+GAP),0,CW+GAP,2*(CW+GAP),0]:[0,CW+GAP,0,CW+GAP,2*(CW+GAP),3*(CW+GAP),4*(CW+GAP),3*(CW+GAP),4*(CW+GAP),0,CW+GAP,2*(CW+GAP),0],
 OY=WMAP?[0,0,CH+GAP,0,CH+GAP,0,0,CH+GAP,CH+GAP,2*(CH+GAP),2*(CH+GAP),2*(CH+GAP),3*(CH+GAP)]:[0,0,CH+GAP,CH+GAP,(CH+GAP)/2,0,0,CH+GAP,CH+GAP,2*(CH+GAP),2*(CH+GAP),2*(CH+GAP),3*(CH+GAP)],WW=WMAP?CW*6+GAP*5:CW*5+GAP*4,WH=CH*5+GAP*4,BS=5,T=32,GW=Math.ceil(WW/T),GH=Math.ceil(WH/T),TER=new Uint8Array(GW*GH),TSP=[.75,1,.75,.5,.9];
function noise(gx,gy){const g=new Float32Array((gx+1)*(gy+1));for(let i=0;i<g.length;i++)g[i]=R();
 return(u,v)=>{const x=cl(u,0,.9999)*gx,y=cl(v,0,.9999)*gy,i=x|0,j=y|0,fx=x-i,fy=y-j,sx=fx*fx*(3-2*fx),sy=fy*fy*(3-2*fy),w=gx+1,a=g[j*w+i],b=g[j*w+i+1],c=g[(j+1)*w+i],d=g[(j+1)*w+i+1];return a+(b-a)*sx+(c-a)*sy+(a-b-c+d)*sx*sy}}
const NZ=[[noise(7,5),noise(19,12),noise(55,35),noise(30,19)]];
const contOf=(x,y)=>{if(y>3*CH+2.5*GAP)return 12;for(let c=0;c<12;c++)if(x>=OX[c]-GAP/2&&x<OX[c]+CWc[c]+GAP/2&&y>=OY[c]-GAP/2&&y<OY[c]+CHc[c]+GAP/2)return c;return x<2*CW+1.5*GAP?0:4};
let WMB=null,WMF=null,WKS=[];
if(WMAP){const W=WMD.W,H=WMD.H,R0=WMD.R;WMB=new Uint16Array(W*H);let p=0;for(let i=0;i<R0.length;i+=2){WMB.fill(R0[i],p,p+R0[i+1]);p+=R0[i+1]}
 const INF=1e4,A=new Float32Array(W*H),B=new Float32Array(W*H);for(let i=0;i<W*H;i++){A[i]=WMB[i]?0:INF;B[i]=WMB[i]?INF:0}
 const ch=D=>{const s2=1.414;for(let y=0;y<H;y++)for(let x=0;x<W;x++){const i=y*W+x;let v=D[i];if(x>0)v=Math.min(v,D[i-1]+1);if(y>0){v=Math.min(v,D[i-W]+1);if(x>0)v=Math.min(v,D[i-W-1]+s2);if(x<W-1)v=Math.min(v,D[i-W+1]+s2)}D[i]=v}
  for(let y=H-1;y>=0;y--)for(let x=W-1;x>=0;x--){const i=y*W+x;let v=D[i];if(x<W-1)v=Math.min(v,D[i+1]+1);if(y<H-1){v=Math.min(v,D[i+W]+1);if(x<W-1)v=Math.min(v,D[i+W+1]+s2);if(x>0)v=Math.min(v,D[i+W-1]+s2)}D[i]=v}};
 ch(A);ch(B);WMF=new Float32Array(W*H);for(let i=0;i<W*H;i++)WMF[i]=WMB[i]?B[i]-.5:-(A[i]-.5)}
function wmD(u,v){const W=WMD.W,H=WMD.H,fx=cl(u*W-.5,0,W-1.001),fy=cl(v*H-.5,0,H-1.001),x=fx|0,y=fy|0,a=fx-x,b=fy-y,i=y*W+x;return(WMF[i]*(1-a)+WMF[i+1]*a)*(1-b)+(WMF[i+W]*(1-a)+WMF[i+W+1]*a)*b}
function wmAt(x,y){const W=WMD.W,H=WMD.H,i=cl((y-OY[0])/20|0,0,H-1)*W+cl((x-OX[0])/20|0,0,W-1);return WMB[i]}
function hW(x,y){const c=contOf(x,y),z=NZ[c];if(!z)return .1;const u=(x-OX[c])/CWc[c],v=(y-OY[c])/CHc[c];if(u<0||v<0||u>1||v>1)return .1;
 if(c==0&&WMAP){const d=wmD(u,v);if(d<=0)return .355+Math.max(d,-3)*.035;if(d<.6)return .37+d/.6*.045;const n=z[0](u,v)*.55+z[1](u,v)*.3+z[2](u,v)*.15;let h=.415+Math.min(d,4)/4*.05+Math.max(0,n-.5)*.9*Math.min(d-.6,3)/3;if(v<.16)h+=(.16-v)*2.2;return h}
 let h=z[0](u,v)*.55+z[1](u,v)*.3+z[2](u,v)*.15;const e=Math.min(u,v,1-u,1-v);if(e<.07)h-=(.07-e)*4.5;return h}
const fW=(x,y)=>{const c=contOf(x,y),z=NZ[c];return z?z[3]((x-OX[c])/CWc[c],(y-OY[c])/CHc[c]):0};
const okLand=(x,y)=>{const h=hW(x,y);return h>.41&&h<.65};
const RACE=[
 {n:'Nhân tộc',pre:'Nhà ',cn:['Nam Quốc','Bắc Quốc','Tây Vực','Đông Hải','Thảo Nguyên'],hue:[4,214,128,44,280],
  sur:['Phạm','Ngô','Vũ','Trần','Lý','Đỗ','Lê','Mạc','Hà','Đặng','Kiều','Bùi','Hoàng','Phan','Đinh'],
  giv:['Liệt','Thiết','Cường','Hải','Phong','Lâm','Hoành','Sơn','Kiệt','Vân','Thạch','Uy','Dũng','Quang','Minh','Tuấn','Hùng','Bảo','Khang','Nghĩa','Trung','Tín','Đạt','Toàn','Thắng','Long','Hổ','Báo','Ưng','Lực','Định','Khải','Vĩnh','Trác','Mãnh'],
  SA:['Long','Hoa','Bạch','Phong','Thiên','Vạn','Lam','Phú','Kim','Ngọc','Thanh','An','Bình','Hải','Vân','Thạch','Hồng','Lạc','Trường','Quảng','Định','Tân','Cẩm','Mỹ'],SB:['Thành','Châu','Lư','Kiếp','Quan','Đô','Xuyên','Lĩnh','Giang','Khẩu','Trấn','Lâm','Hưng','Ninh','Phong','Sơn','Bảo','Đài'],vl:'Làng',
  st:{hp:1,atk:1,sp:1,rng:1,h:1},wall:'#b8ad97'},
 {n:'Người Lùn',pre:'Gia tộc ',cn:['Thiết Sơn','Hắc Thạch','Kim Khoáng','Băng Phong','Hỏa Lò'],hue:[18,200,40,180,0],
  sur:['Búa Sắt','Râu Đá','Rìu Đồng','Đe Lửa','Mỏ Vàng','Khiên Đá','Chùy Bạc','Lò Rèn','Hang Sâu','Núi Xám','Đá Đen','Quặng Đỏ','Búa Sấm','Răng Đá','Giáp Đồng'],
  giv:['Brom','Grunda','Torvik','Haldor','Kragg','Bodvar','Ulfgar','Dorn','Rurik','Thrak','Gorm','Belgar','Morgrim','Skarn','Hegg','Barik','Dunmar','Korr'],
  SA:['Thiết','Thạch','Kim','Đồng','Hỏa','Băng','Hắc','Ngân','Lôi','Cương'],SB:['Sơn Bảo','Động','Lò Rèn','Khoáng Thành','Hầm Đá','Thạch Môn','Lĩnh Bảo'],vl:'Mỏ',
  st:{hp:1.3,atk:1.1,sp:.85,rng:.9,h:.72},wall:'#7f7a74'},
 {n:'Tộc Elf',pre:'Dòng ',cn:['Lục Lâm','Nguyệt Quang','Tinh Vân','Bạch Hoa','Thanh Diệp'],hue:[150,230,190,90,300],
  sur:['Lá Bạc','Trăng Non','Sao Mai','Hoa Tuyết','Gió Ngàn','Suối Ngọc','Cây Cổ','Sương Mai','Ánh Dương','Lam Thụ','Liễu Rủ','Mây Bạc','Cung Vàng','Lục Bảo','Thiên Thanh'],
  giv:['Aelar','Lirael','Thalion','Sylva','Elarion','Naeris','Faelyn','Ilyra','Calen','Mirae','Vaelis','Arannis','Elowen','Saelin','Theren','Ysolde','Caelum','Liora'],
  SA:['Lục','Nguyệt','Tinh','Bạch','Thanh','Lam','Ngọc','Vân','Diệp','Tuyết'],SB:['Diệp Lâm','Thụ Cung','Hoa Viên','Tuyết Đài','Lâm Uyển','Khê Cốc','Quang Điện'],vl:'Vườn',
  st:{hp:.9,atk:1,sp:1.1,rng:1.35,h:1.15},wall:'#e6e0d0'},
 {n:'Người Sói',pre:'Bầy ',cn:['Huyết Nguyệt','Lang Sơn','Hắc Lâm','Bạo Phong','Cuồng Dã'],hue:[0,30,260,350,20],
  sur:['Nanh Bạc','Vuốt Đỏ','Bờm Xám','Trăng Máu','Tru Đêm','Mắt Lửa','Lông Đen','Răng Sắt','Gió Bắc','Hú Dài','Sẹo Máu','Đuôi Trắng','Móng Đá','Bóng Sói','Giông Bão'],
  giv:['Fenrik','Ragnar','Vulka','Lykos','Garr','Skoll','Hrothi','Ulric','Varg','Lupa','Kaelo','Grimm','Torv','Raska','Wulfen','Brask','Morva','Tyrr'],
  SA:['Huyết','Lang','Hắc','Nguyệt','Cuồng','Phong','Nha','Trảo','Ám','Dã'],SB:['Sào Huyệt','Lang Thành','Nanh Đài','Hang Sói','Lâm Trại','Nguyệt Đài','Cốt Trại'],vl:'Trại',
  st:{hp:1.25,atk:1.3,sp:1.2,rng:.8,h:1.05},wall:'#8a6a46'},
 {n:'Vùng Đất Chết',pre:'Quân đoàn ',cn:['Hắc Ám','Tử Vực','U Minh','Cốt Sơn','Huyết Hải'],hue:[275,0,300,200,330],
  sur:['Xương Trắng','Sọ Đen','Mộ Cổ','Hồn Ma','Tro Tàn','Bóng Tối','Lưỡi Hái','Xích Sắt','Nanh Độc','Vực Thẳm','Hỏa Ngục','Đá Mộ','Trăng Tà','Gió Chết','Mắt Đỏ'],
  giv:['Malgor','Zarkul','Vorath','Skelra','Mordek','Grimhal','Azrol','Thalgrim','Velkor','Nyxar','Korvath','Draxis','Umbrak','Sorvel','Kethar','Gorvash','Ulthar','Xerath'],
  SA:['Hắc','Tử','U','Cốt','Huyết','Ám','Quỷ','Mộ','Tà','Diệt'],SB:['Cốt Thành','Tử Thành','Mộ Địa','U Linh Đài','Hắc Bảo','Huyệt Đài','Ma Thành'],vl:'Nghĩa địa',
  st:{hp:1,atk:1,sp:.95,rng:1,h:1},wall:'#4a4448'},
 {n:'Titan',pre:'Thần tộc ',cn:['Cự Thạch','Thiên Trụ','Lôi Sơn','Đại Địa','Cổ Thần'],hue:[30,45,200,20,0],sur:['Cự Nhân','Thạch Thần','Sơn Nhạc','Lôi Chấn','Địa Mẫu','Thiên Trụ','Cổ Nham','Hồng Hoang','Bàn Thạch','Vạn Cân','Kim Cương','Thái Sơn','Đại Lực','Chấn Thiên','Cự Phủ'],
  giv:['Kronos','Atlas','Hyperion','Krios','Oceanus','Rhea','Theia','Themis','Mnemos','Phoebe','Iapetos','Coeus','Gaion','Tethys','Typhon','Ymir','Surtr','Aegir'],SA:['Cự','Thạch','Lôi','Thiên','Địa','Cổ','Kim','Nham','Sơn','Hồng'],SB:['Thần Điện','Cự Trụ','Thạch Đàn','Thiên Đài','Cổ Tháp','Thần Thành'],vl:'Thôn',
  st:{hp:1.1,atk:1.05,sp:.9,rng:1,h:1.5},wall:'#a89a82'},
 {n:'Thiên Thần',pre:'Thánh vực ',cn:['Thiên Đường','Quang Minh','Thánh Vân','Kim Dực','Bạch Ngọc'],hue:[50,190,210,40,0],sur:['Kim Dực','Thánh Quang','Bạch Vũ','Thiên Hỏa','Lưu Ly','Tinh Tú','Hào Quang','Thanh Khiết','Ngọc Hư','Vân Tiêu','Bình Minh','Thánh Kiếm','Lục Dực','Thiên Âm','Phúc Âm'],
  giv:['Michael','Gabriel','Raphael','Uriel','Seraphiel','Azrael','Raziel','Cassiel','Ariel','Jophiel','Zadkiel','Haniel','Chamuel','Remiel','Sariel','Metatron','Sandalphon','Lumiel'],SA:['Thánh','Quang','Kim','Ngọc','Vân','Tinh','Thiên','Bạch','Lưu Ly','Hào'],SB:['Thánh Điện','Thiên Cung','Quang Đài','Vân Các','Ngọc Lâu','Thánh Đường'],vl:'Thánh thôn',
  st:{hp:.95,atk:1,sp:1.1,rng:1.15,h:1.15},wall:'#f4efe2'},
 {n:'Quỷ tộc',pre:'Ma vực ',cn:['Luyện Ngục','Huyết Hỏa','Hắc Diệm','Vô Gian','Địa Phủ'],hue:[0,15,350,330,25],sur:['Hỏa Diệm','Huyết Ma','Hắc Viêm','Luyện Ngục','Ác Quỷ','Ma Sừng','Dung Nham','Tà Hỏa','Diêm La','Huyết Trì','Hắc Nham','Lưu Huỳnh','Ma Trảo','Liệt Hỏa','Tro Đỏ'],
  giv:['Baal','Asmodeus','Belial','Mammon','Astaroth','Abaddon','Moloch','Azazel','Mephisto','Bael','Paimon','Belphegor','Leviathan','Amon','Furcas','Vepar','Gremory','Zagan'],SA:['Hỏa','Huyết','Hắc','Ma','Viêm','Luyện','Tà','Diêm','Nham','Lưu'],SB:['Ma Thành','Hỏa Ngục','Huyết Điện','Viêm Bảo','Ma Cung','Tà Đài'],vl:'Ma thôn',
  st:{hp:1.05,atk:1.05,sp:1,rng:1,h:1.2},wall:'#2a1416'},
 {n:'Vạn Yêu',pre:'Yêu tộc ',cn:['Thanh Khâu','Vạn Yêu Lâm','Hồ Ly Sơn','Xà Cốc','Ưng Phong'],hue:[110,140,25,280,170],sur:['Cửu Vĩ','Hồ Ly','Bạch Xà','Thanh Long','Kim Bằng','Hắc Hổ','Ngọc Thố','Linh Hầu','Lục Nha','Hỏa Phượng','Bích Thủy','Tử Vân','Thiên Hồ','Linh Lộc','Yêu Nguyệt'],
  giv:['Đát Kỷ','Bạch Tố','Thanh Xà','Ngưu Ma','Bạch Cốt','Kim Sí','Hắc Phong','Hồng Hài','Cửu Đầu','Ngọc Diện','Thanh Sư','Bạch Tượng','Hổ Lực','Lộc Lực','Dương Lực','Hạt Tử','Thiềm Thừ','Tri Chu'],SA:['Thanh','Hồ','Xà','Bằng','Hổ','Linh','Ngọc','Thiên','Yêu','Bích'],SB:['Yêu Động','Linh Sơn','Bảo Tháp','Lâm Cung','Thủy Phủ','Yêu Điện'],vl:'Yêu thôn',
  st:{hp:1,atk:1.05,sp:1.1,rng:1,h:1.1},wall:'#7a3a2a'},
 {n:'Thiên Nguyên Giới',pre:'Tông môn ',cn:['Thanh Vân Châu','Thiên Kiếm Vực','Huyền Thiên Châu','Lạc Hà Châu','Vân Mộng Trạch'],hue:[190,210,150,30,170],sur:['Thanh Vân','Thiên Kiếm','Huyền Thiên','Lạc Hà','Vân Mộng','Tử Tiêu','Ngọc Thanh','Thái Hư','Côn Lôn','Nga Mi','Thục Sơn','Linh Tiêu','Bích Du','Kim Ô','Tinh La'],
  giv:['Lăng Tiêu','Thái Hư','Vô Cực','Thanh Huyền','Diệp Phàm','Hàn Lập','Tiêu Viêm','Lâm Động','Mục Trần','Tần Vũ','Bạch Tiểu Thuần','Mạnh Hạo','Vương Lâm','Thạch Hạo','Đường Tam','Lý Thất Dạ','Sở Phong','Phương Hàn'],SA:['Thanh','Tử','Ngọc','Huyền','Linh','Kim','Thái','Vân','Bích','Tinh'],SB:['Tiêu Phong','Vân Sơn','Kiếm Phong','Linh Cốc','Tiên Đài','Đạo Cung'],vl:'Phàm nhân thôn',
  st:{hp:3,atk:3.2,sp:1.4,rng:1.6,h:1.05},wall:'#e8e4d8'},
 {n:'Huyền Hoang Vực',pre:'Thánh địa ',cn:['Hoang Cổ Vực','Thái Cổ Châu','Đế Lạc Châu','Bất Tử Sơn','Thần Khư'],hue:[45,30,15,55,0],sur:['Hoang Cổ','Thái Cổ','Đế Lạc','Bất Tử','Thần Khư','Dao Trì','Diêu Quang','Tử Vi','Thái Dương','Thái Âm','Kim Ô','Hư Không','Vạn Cổ','Thiên Đình','Luân Hồi'],
  giv:['Vô Thủy','Ngoan Nhân','Thanh Đế','Hư Không Đế','Hằng Vũ','Thái Âm Hoàng','Đấu Chiến','Thiên Hoàng','Cổ Hoàng','Bất Tử','Thạch Hoàng','Liễu Thần','Hoang Thiên','Đại Thành','Thánh Thể','Vạn Pháp','Huyền Nguyên','Thái Sơ'],SA:['Hoang','Thái','Đế','Thần','Dao','Diêu','Tử','Vạn','Luân','Cổ'],SB:['Thánh Sơn','Đế Cung','Thần Điện','Tiên Khư','Đạo Tràng','Bí Cảnh'],vl:'Phàm nhân thôn',
  st:{hp:3.4,atk:3.4,sp:1.35,rng:1.5,h:1.1},wall:'#f2e2b0'},
 {n:'Cửu U Tiên Vực',pre:'Ma tông ',cn:['Cửu U','Huyết Hải','Vạn Ma Quật','Âm Sát Vực','Thiên Ma Nguyên'],hue:[280,0,300,260,330],sur:['Cửu U','Huyết Thần','Vạn Ma','Âm Sát','Thiên Ma','Hợp Hoan','Huyết Sát','Quỷ Vương','Thi Âm','Luyện Hồn','Phệ Hồn','Bách Độc','U Minh','Ma Diễm','Huyền Âm'],
  giv:['Huyết Thần Tử','Ma Tôn','Quỷ Đế','Âm Cửu U','Phệ Thiên','Hắc Ma','Huyết Ảnh','Thiên Sát','Vạn Độc','La Sát','Tà Quân','Ma La','U Tuyền','Diệt Thế','Hồn Đế','Huyết Ma','Ám Dạ','Cuồng Ma'],SA:['U','Huyết','Ma','Âm','Quỷ','Sát','Thi','Tà','Ám','Hồn'],SB:['Ma Cung','Huyết Điện','U Cốc','Ma Phong','Âm Đài','Sát Tháp'],vl:'Phàm nhân thôn',
  st:{hp:3.3,atk:3.6,sp:1.4,rng:1.4,h:1.05},wall:'#3a2244'}];
const RIC=['🧑','🧔','🧝','🐺','💀','🗿','👼','👹','🦊','☁️','☀️','🌑'];
const CNN=RACE[0].cn,SUR=RACE[0].sur,GIV=RACE[0].giv,SA=RACE[0].SA,SB=RACE[0].SB;
const usedN=new Set(),unameR=c=>{const r=RACE[c];for(let k=0;;k++){const n=r.SA[R()*r.SA.length|0]+' '+r.SB[R()*r.SB.length|0]+(k>60?' '+k:'');if(!usedN.has(n)){usedN.add(n);return n}}};
const CC=[],F0=[],S=[],V=[],ROADS=[];
const WREG=['Châu Á','Châu Âu','Châu Phi','Bắc Mỹ','Nam Mỹ','Châu Đại Dương'];
const WNM=[['Minh','Hiro','Kenji','Vũ','Arjun','Ali','Rashid','Tuấn','Kim','Raj','Omar','Bảo','Somchai','Tenzin','Long','Akira'],['Henri','Karl','Ludwig','Alfonso','Ivan','Olaf','Edward','Otto','Carlos','Stefan','Viktor','Leopold','Pierre','Marco','Sven','Frederick'],['Kwame','Amadou','Sekou','Jomo','Tariq','Musa','Kofi','Obi','Zola','Tendai','Moussa','Hamid','Menelik','Shaka'],['John','George','Abraham','Pablo','Diego','Juan','Jack','Robert','Miguel','Henry','William','Benito'],['Simón','José','Pedro','Luis','Manuel','Bernardo','Antonio','Rafael','Andrés','Felipe','Tupac'],['Kai','Tane','Lachlan','Liam','Maui','Ariki','Koa','Oliver','Kamehameha']],ROMN=['I','II','III','IV','V','VI','VII','VIII','IX'];
const wmName=f=>WNM[f.wm][Math.random()*WNM[f.wm].length|0]+' '+ROMN[Math.random()*9|0];
