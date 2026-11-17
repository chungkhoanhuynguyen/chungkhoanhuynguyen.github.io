const CIC=new Map();function CICON(c,rl,ty){const key=c+'|'+rl+'|'+ty;let cv=CIC.get(key);if(cv)return cv;cv=document.createElement('canvas');cv.width=cv.height=64;const g=cv.getContext('2d'),B=54,ST='#e4dbc4',SD='#b9ac8e',SK='#8c7f64';
 g.fillStyle='rgba(0,0,0,.35)';g.beginPath();g.ellipse(32,B+3,[26,21,15][ty],5,0,0,7);g.fill();g.strokeStyle=rl;g.lineWidth=3;g.beginPath();g.ellipse(32,B+1,[25,20,14][ty],5,0,0,7);g.stroke();
 const tower=(x,w,h)=>{const y=B-h;g.fillStyle=ST;g.fillRect(x,y,w,h);g.fillStyle=SD;g.fillRect(x+w*.62,y,w*.38,h);g.strokeStyle=SK;g.lineWidth=1;g.strokeRect(x+.5,y+.5,w-1,h-1);g.fillStyle='#3b3226';g.fillRect(x+w/2-1.2,y+h*.3,2.4,4);
  g.fillStyle=c;g.beginPath();g.moveTo(x-2,y+1);g.lineTo(x+w/2,y-w*1.15);g.lineTo(x+w+2,y+1);g.fill();g.fillStyle='rgba(0,0,0,.25)';g.beginPath();g.moveTo(x+w/2,y-w*1.15);g.lineTo(x+w+2,y+1);g.lineTo(x+w/2,y+1);g.fill();
  const fy=y-w*1.15;g.strokeStyle='#4a3a28';g.lineWidth=1.2;g.beginPath();g.moveTo(x+w/2,fy);g.lineTo(x+w/2,fy-9);g.stroke();g.fillStyle=c;g.beginPath();g.moveTo(x+w/2,fy-9);g.lineTo(x+w/2+8,fy-6.5);g.lineTo(x+w/2,fy-4);g.fill()};
 const wall=(x0,w)=>{g.fillStyle=ST;g.fillRect(x0,B-12,w,12);g.fillStyle=SD;g.fillRect(x0,B-4,w,4);for(let i=0;i<w-2;i+=5){g.fillStyle=ST;g.fillRect(x0+i,B-15,3,3)}g.strokeStyle=SK;g.lineWidth=1;g.strokeRect(x0+.5,B-11.5,w-1,11);g.fillStyle='#3b3226';g.beginPath();g.arc(32,B-4,3.5,Math.PI,0);g.lineTo(35.5,B);g.lineTo(28.5,B);g.fill()};
 if(ty==0){wall(12,40);tower(8,10,26);tower(46,10,26);tower(26,12,36)}else if(ty==1){wall(16,32);tower(13,10,24);tower(41,10,24)}else{wall(22,20);tower(27,10,26)}
 CIC.set(key,cv);if(CIC.size>900)CIC.delete(CIC.keys().next().value);return cv}
function keepHD(ty,wc,c){const g=X;
 const shade=(x0,x1,y0,y1,a)=>{const gr=g.createLinearGradient(x0,0,x1,0);gr.addColorStop(0,`rgba(255,255,255,${a*.35})`);gr.addColorStop(.45,'rgba(0,0,0,0)');gr.addColorStop(1,`rgba(0,0,0,${a})`);g.fillStyle=gr;g.fillRect(x0,y0,x1-x0,y1-y0)};
 const bricks=(x0,x1,y0,y1)=>{g.strokeStyle='rgba(60,45,30,.22)';g.lineWidth=.6;g.beginPath();for(let y=y1-4,r=0;y>y0;y-=4,r++){g.moveTo(x0,y);g.lineTo(x1,y);for(let x=x0+(r%2?3:0);x<x1;x+=7){g.moveTo(x,y);g.lineTo(x,y-4)}}g.stroke()};
 const cren=(x0,x1,y,col)=>{g.fillStyle=col;for(let x=x0;x<x1-1;x+=5)g.fillRect(x,y-4,3,4)};
 const win=(x,y,w,h)=>{g.fillStyle='#2a1c10';g.beginPath();g.moveTo(x-w/2,y+h);g.lineTo(x-w/2,y+w/2);g.arc(x,y+w/2,w/2,Math.PI,0);g.lineTo(x+w/2,y+h);g.fill();g.fillStyle='rgba(255,200,90,.85)';g.fillRect(x-w/2+.8,y+h*.45,w-1.6,h*.5)};
 const flag=(x,y,s)=>{g.strokeStyle='#3a2a1a';g.lineWidth=1.3;g.beginPath();g.moveTo(x,y);g.lineTo(x,y-14*s);g.stroke();g.fillStyle=c;g.beginPath();g.moveTo(x,y-14*s);g.quadraticCurveTo(x+6*s,y-16*s,x+12*s,y-12*s);g.lineTo(x+12*s,y-7*s);g.quadraticCurveTo(x+6*s,y-10*s,x,y-8*s);g.fill();g.fillStyle='rgba(255,255,255,.25)';g.fillRect(x+1,y-13.5*s,4*s,1.4)};
 const tower=(x,yb,w,h,rh,fl)=>{const y0=yb-h;g.fillStyle=wc;g.fillRect(x-w/2,y0,w,h);bricks(x-w/2,x+w/2,y0,yb);shade(x-w/2,x+w/2,y0,yb,.4);
  g.fillStyle=wc;g.fillRect(x-w/2-2,y0-3,w+4,4);cren(x-w/2-2,x+w/2+2,y0-2,wc);g.fillStyle='rgba(0,0,0,.25)';g.fillRect(x-w/2-2,y0+1,w+4,1.5);
  for(let yy=y0+8;yy<yb-10;yy+=14)win(x,yy,Math.max(3,w*.22),6);
  const gr=g.createLinearGradient(x-w/2,0,x+w/2,0);gr.addColorStop(0,c);gr.addColorStop(1,c);g.fillStyle=gr;g.beginPath();g.moveTo(x-w/2-4,y0-2);g.lineTo(x,y0-2-rh);g.lineTo(x+w/2+4,y0-2);g.closePath();g.fill();
  g.fillStyle='rgba(255,255,255,.22)';g.beginPath();g.moveTo(x-w/2-4,y0-2);g.lineTo(x,y0-2-rh);g.lineTo(x-w*.1,y0-2);g.fill();g.fillStyle='rgba(0,0,0,.28)';g.beginPath();g.moveTo(x,y0-2-rh);g.lineTo(x+w/2+4,y0-2);g.lineTo(x+w*.15,y0-2);g.fill();
  g.strokeStyle='rgba(0,0,0,.25)';g.lineWidth=.6;for(let k=1;k<4;k++){const yy=y0-2-rh*k/4,hw=(w/2+4)*(1-k/4);g.beginPath();g.moveTo(x-hw,yy);g.lineTo(x+hw,yy);g.stroke()}
  if(fl)flag(x,y0-2-rh,fl)};
 const wall=(x0,x1,yb,h)=>{g.fillStyle=wc;g.fillRect(x0,yb-h,x1-x0,h);bricks(x0,x1,yb-h,yb);g.fillStyle='rgba(0,0,0,.12)';g.fillRect(x0,yb-h,x1-x0,h);cren(x0,x1,yb-h,wc);g.fillStyle='rgba(0,0,0,.3)';g.fillRect(x0,yb-3,x1-x0,3)};
 const gate=(yb,w,h)=>{g.fillStyle='#24180e';g.beginPath();g.moveTo(-w/2,yb);g.lineTo(-w/2,yb-h+w/2);g.arc(0,yb-h+w/2,w/2,Math.PI,0);g.lineTo(w/2,yb);g.fill();g.strokeStyle='rgba(150,130,100,.7)';g.lineWidth=.8;g.beginPath();for(let x=-w/2+2;x<w/2;x+=3){g.moveTo(x,yb-h+w/2-1);g.lineTo(x,yb)}for(let y=yb-2;y>yb-h+w/2;y-=3){g.moveTo(-w/2,y);g.lineTo(w/2,y)}g.stroke();
  for(const sx of[-1,1]){g.fillStyle='#3a2a1a';g.fillRect(sx*(w/2+4)-1,yb-h*.7,2,6);g.fillStyle='rgba(255,170,60,.9)';g.beginPath();g.arc(sx*(w/2+4),yb-h*.7-1,2.2,0,7);g.fill();g.fillStyle='rgba(255,170,60,.18)';g.beginPath();g.arc(sx*(w/2+4),yb-h*.7-1,7,0,7);g.fill()}};
 const R=[96,74,52][ty];g.fillStyle='rgba(0,0,0,.28)';g.beginPath();g.ellipse(6,5,R,R*.26,0,0,7);g.fill();
 {const gr=g.createRadialGradient(0,-2,4,0,0,R);gr.addColorStop(0,'#9c8a5c');gr.addColorStop(.75,'#7d9a4c');gr.addColorStop(1,'rgba(90,130,60,0)');g.fillStyle=gr;g.beginPath();g.ellipse(0,0,R,R*.27,0,0,7);g.fill()}
 if(ty==0){wall(-60,60,-24,14);tower(-62,-20,16,30,18,.7);tower(62,-20,16,30,18,.7);tower(0,-26,34,62,30,1.1);tower(-24,-22,18,44,22,0);tower(24,-22,18,44,22,0);wall(-72,72,0,22);gate(0,14,18);tower(-76,2,20,40,22,.8);tower(76,2,20,40,22,.8);
  for(const hx of[-104,96]){g.fillStyle='#e2d2ac';g.fillRect(hx,-8,12,8);g.fillStyle='#a5522c';g.beginPath();g.moveTo(hx-2,-8);g.lineTo(hx+6,-15);g.lineTo(hx+14,-8);g.fill()}}
 else if(ty==1){wall(-40,40,-16,12);tower(0,-18,26,50,24,1);wall(-50,50,0,18);gate(0,12,15);tower(-52,2,18,34,20,.7);tower(52,2,18,34,20,.7)}
 else{wall(-30,30,0,14);gate(0,10,12);tower(0,-6,22,46,22,.9)}}
function kGround(R,col){const g=X;g.fillStyle='rgba(0,0,0,.28)';g.beginPath();g.ellipse(6,5,R,R*.26,0,0,7);g.fill();const gr=g.createRadialGradient(0,-2,4,0,0,R);gr.addColorStop(0,col||'#9c8a5c');gr.addColorStop(.75,'#7d9a4c');gr.addColorStop(1,'rgba(90,130,60,0)');g.fillStyle=gr;g.beginPath();g.ellipse(0,0,R,R*.27,0,0,7);g.fill()}
function kFlag(x,y,s,c){const g=X;g.strokeStyle='#3a2a1a';g.lineWidth=1.3;g.beginPath();g.moveTo(x,y);g.lineTo(x,y-14*s);g.stroke();g.fillStyle=c;g.beginPath();g.moveTo(x,y-14*s);g.quadraticCurveTo(x+6*s,y-16*s,x+12*s,y-12*s);g.lineTo(x+12*s,y-7*s);g.quadraticCurveTo(x+6*s,y-10*s,x,y-8*s);g.fill()}
function kShade(x0,x1,y0,y1,a){const g=X,gr=g.createLinearGradient(x0,0,x1,0);gr.addColorStop(0,`rgba(255,255,255,${a*.3})`);gr.addColorStop(.45,'rgba(0,0,0,0)');gr.addColorStop(1,`rgba(0,0,0,${a})`);g.fillStyle=gr;g.fillRect(x0,y0,x1-x0,y1-y0)}
/* Châu Á: thành Á Đông — nền đá, lầu gỗ cột đỏ, mái cong */
function keepAsia(ty,c){const g=X;kGround([96,74,50][ty],'#8e8a62');
 const roof=(x,y,w,h,col)=>{g.fillStyle=col||'#33343c';g.beginPath();g.moveTo(x-w/2-10,y-7);g.quadraticCurveTo(x-w/2-2,y+1,x-w/2+8,y);g.lineTo(x+w/2-8,y);g.quadraticCurveTo(x+w/2+2,y+1,x+w/2+10,y-7);g.lineTo(x+w/2-7,y-h);g.lineTo(x-w/2+7,y-h);g.closePath();g.fill();
  g.strokeStyle='rgba(255,255,255,.18)';g.lineWidth=.7;g.beginPath();for(let k=x-w/2+10;k<x+w/2-8;k+=4){g.moveTo(k,y-1);g.lineTo(k+(x-k)*.15,y-h+1)}g.stroke();g.fillStyle=c;g.fillRect(x-w/2+7,y-h-2,w-14,2.5);g.fillStyle='#d8b04a';g.beginPath();g.arc(x-w/2+7,y-h-1,2,0,7);g.arc(x+w/2-7,y-h-1,2,0,7);g.fill()};
 const hall=(x,yb,w,h)=>{g.fillStyle='#efe6d2';g.fillRect(x-w/2,yb-h,w,h);g.fillStyle='#a8261c';for(let k=0;k<=4;k++)g.fillRect(x-w/2+k*(w-3)/4,yb-h,3,h);g.fillStyle='rgba(60,30,20,.55)';for(let k=0;k<4;k++)g.fillRect(x-w/2+3+k*(w-3)/4+2,yb-h+3,(w-3)/4-5,h*.55);g.fillStyle='#7a1a12';g.fillRect(x-w/2-3,yb-1.5,w+6,3)};
 const base=(x0,x1,yb,h)=>{g.fillStyle='#8f8a80';g.fillRect(x0,yb-h,x1-x0,h);g.strokeStyle='rgba(40,35,30,.3)';g.lineWidth=.6;g.beginPath();for(let y=yb-4,r=0;y>yb-h;y-=4,r++){g.moveTo(x0,y);g.lineTo(x1,y);for(let x=x0+(r%2?4:0);x<x1;x+=9){g.moveTo(x,y);g.lineTo(x,y-4)}}g.stroke();kShade(x0,x1,yb-h,yb,.25);g.fillStyle='#6e6a60';for(let x=x0;x<x1-2;x+=6)g.fillRect(x,yb-h-3,4,3)};
 const gateA=(yb,w,h)=>{g.fillStyle='#2a1d12';g.beginPath();g.moveTo(-w/2,yb);g.lineTo(-w/2,yb-h+w/2);g.arc(0,yb-h+w/2,w/2,Math.PI,0);g.lineTo(w/2,yb);g.fill();g.fillStyle='#7a1a12';g.fillRect(-w/2+1,yb-h+w/2,w/2-1.5,h-w/2);g.fillRect(.5,yb-h+w/2,w/2-1.5,h-w/2);g.fillStyle='#d8b04a';for(const sx of[-1,1])for(let k=0;k<3;k++){g.beginPath();g.arc(sx*w/4,yb-h+w/2+3+k*4,.9,0,7);g.fill()}};
 const lantern=(x,y)=>{g.strokeStyle='#3a2a1a';g.lineWidth=.8;g.beginPath();g.moveTo(x,y-4);g.lineTo(x,y);g.stroke();g.fillStyle='#e8402a';g.beginPath();g.ellipse(x,y+3,2.6,3.4,0,0,7);g.fill();g.fillStyle='rgba(255,180,80,.35)';g.beginPath();g.arc(x,y+3,6,0,7);g.fill()};
 const pagoda=(x,yb,w,n)=>{let y=yb;for(let k=0;k<n;k++){const ww=w*(1-k*.16);g.fillStyle='#efe6d2';g.fillRect(x-ww/2+3,y-12,ww-6,12);g.fillStyle='#a8261c';g.fillRect(x-ww/2+3,y-12,2.5,12);g.fillRect(x+ww/2-5.5,y-12,2.5,12);roof(x,y-12,ww+4,9);y-=21}g.strokeStyle='#d8b04a';g.lineWidth=1.4;g.beginPath();g.moveTo(x,y+12);g.lineTo(x,y-2);g.stroke()};
 if(ty==0){base(-82,82,0,24);gateA(0,16,20);hall(0,-24,64,18);roof(0,-42,72,14);hall(0,-56,40,10);roof(0,-66,48,12);for(const sx of[-1,1]){hall(sx*66,-24,20,12);roof(sx*66,-36,24,10);lantern(sx*30,-40)}kFlag(-84,-24,.9,c);kFlag(84,-24,.9,c);
  for(const hx of[-104,96]){g.fillStyle='#efe6d2';g.fillRect(hx,-8,12,8);roof(hx+6,-8,12,6,'#5a4a3a')}}
 else if(ty==1){base(-56,56,0,20);gateA(0,14,17);hall(0,-20,46,15);roof(0,-35,54,13);hall(0,-48,28,8);roof(0,-56,34,10);lantern(-22,-34);lantern(22,-34);kFlag(-58,-20,.8,c)}
 else{g.fillStyle='#8f8a80';g.fillRect(-26,-6,52,6);pagoda(0,-6,28,3);kFlag(24,-6,.7,c)}}
/* Châu Phi: kiến trúc đất nung Sahel */
function keepAfrica(ty,c){const g=X;kGround([94,72,50][ty],'#b08a52');const M='#c58a52',MD='#9c6638';
 const sticks=(x0,x1,y)=>{g.strokeStyle='#4a3020';g.lineWidth=1.2;g.beginPath();for(let x=x0+3;x<x1-1;x+=6){g.moveTo(x,y);g.lineTo(x,y+2.5)}g.stroke()};
 const tw=(x,yb,w,h)=>{g.fillStyle=M;g.beginPath();g.moveTo(x-w/2,yb);g.lineTo(x-w*.32,yb-h);g.quadraticCurveTo(x,yb-h-w*.5,x+w*.32,yb-h);g.lineTo(x+w/2,yb);g.closePath();g.fill();kShade(x-w/2,x+w/2,yb-h-w*.5,yb,.35);sticks(x-w*.4,x+w*.4,yb-h*.45);sticks(x-w*.3,x+w*.3,yb-h*.8);g.fillStyle='#3a2414';g.fillRect(x-1.5,yb-h*.6,3,5)};
 const wl=(x0,x1,yb,h)=>{g.fillStyle=M;g.beginPath();g.moveTo(x0,yb);g.lineTo(x0,yb-h);for(let x=x0;x<x1;x+=8)g.quadraticCurveTo(x+4,yb-h-5,x+8,yb-h);g.lineTo(x1,yb);g.closePath();g.fill();g.fillStyle='rgba(0,0,0,.12)';g.fillRect(x0,yb-4,x1-x0,4);sticks(x0,x1,yb-h*.55);g.fillStyle=MD;g.fillRect(x0,yb-h*.3,x1-x0,1.5)};
 const door=(yb,w,h)=>{g.fillStyle='#3a2414';g.beginPath();g.moveTo(-w/2,yb);g.lineTo(-w/2,yb-h+w/2);g.arc(0,yb-h+w/2,w/2,Math.PI,0);g.lineTo(w/2,yb);g.fill()};
 if(ty==0){wl(-80,80,0,22);door(0,14,18);tw(-80,0,20,36);tw(80,0,20,36);tw(-26,-20,20,40);tw(26,-20,20,40);tw(0,-22,28,56);kFlag(0,-80,1,c);for(const hx of[-104,96]){g.fillStyle=M;g.fillRect(hx,-9,13,9);g.fillStyle='#d6b468';g.beginPath();g.moveTo(hx-2,-9);g.lineTo(hx+6.5,-17);g.lineTo(hx+15,-9);g.fill()}}
 else if(ty==1){wl(-54,54,0,18);door(0,12,15);tw(-54,0,18,30);tw(54,0,18,30);tw(0,-16,24,44);kFlag(0,-66,.9,c)}
 else{wl(-30,30,0,13);door(0,9,11);tw(0,-8,20,38);kFlag(0,-54,.8,c)}}
/* Bắc Mỹ: đồn gỗ hàng rào cọc + lô cốt */
function keepFort(ty,c){const g=X;kGround([94,72,50][ty]);const L='#8a5a34',LD='#5e3c22';
 const pal=(x0,x1,yb,h)=>{for(let x=x0;x<x1;x+=4.2){g.fillStyle=(x/4.2|0)%2?L:'#7a4e2c';g.beginPath();g.moveTo(x,yb);g.lineTo(x,yb-h);g.lineTo(x+2,yb-h-4);g.lineTo(x+4,yb-h);g.lineTo(x+4,yb);g.fill()}g.fillStyle='rgba(0,0,0,.25)';g.fillRect(x0,yb-h*.35,x1-x0,1.6);g.fillRect(x0,yb-h*.75,x1-x0,1.6)};
 const bh=(x,yb,w,h)=>{g.fillStyle=L;g.fillRect(x-w/2,yb-h*.5,w,h*.5);g.fillStyle='#9a6a40';g.fillRect(x-w/2-3,yb-h,w+6,h*.5);g.strokeStyle=LD;g.lineWidth=.7;g.beginPath();for(let y=yb-2;y>yb-h;y-=3){g.moveTo(x-w/2-3,y);g.lineTo(x+w/2+3,y)}g.stroke();g.fillStyle='#2a1a10';g.fillRect(x-3,yb-h*.8,6,3);
  g.fillStyle=c;g.beginPath();g.moveTo(x-w/2-6,yb-h);g.lineTo(x,yb-h-w*.55);g.lineTo(x+w/2+6,yb-h);g.fill();g.fillStyle='rgba(0,0,0,.25)';g.beginPath();g.moveTo(x,yb-h-w*.55);g.lineTo(x+w/2+6,yb-h);g.lineTo(x,yb-h);g.fill()};
 if(ty==0){pal(-74,74,-26,20);bh(0,-24,30,38);bh(-74,-22,16,26);bh(74,-22,16,26);pal(-80,80,0,22);g.fillStyle='#2a1a10';g.fillRect(-8,-18,16,18);g.fillStyle=L;g.fillRect(-7,-17,6.5,17);g.fillRect(.5,-17,6.5,17);bh(-82,2,18,30);bh(82,2,18,30);kFlag(0,-70,1.1,c)}
 else if(ty==1){bh(0,-16,26,34);pal(-54,54,0,20);g.fillStyle='#2a1a10';g.fillRect(-7,-16,14,16);bh(-56,2,16,28);bh(56,2,16,28);kFlag(0,-60,.9,c)}
 else{pal(-30,30,0,16);bh(0,-4,22,30);kFlag(0,-46,.8,c)}}
/* Nam Mỹ: kim tự tháp bậc thang (Maya/Inca) */
function keepPyramid(ty,c){const g=X;kGround([96,74,52][ty],'#7f8a52');const n=[5,4,3][ty],W=[150,112,76][ty],sh=[11,10,9][ty];let y=0;
 for(let k=0;k<n;k++){const w=W*(1-k*.17);g.fillStyle=k%2?'#bdb093':'#b0a283';g.fillRect(-w/2,y-sh,w,sh);kShade(-w/2,w/2,y-sh,y,.3);g.fillStyle='rgba(0,0,0,.25)';g.fillRect(-w/2,y-1.5,w,1.5);g.strokeStyle='rgba(60,50,30,.25)';g.lineWidth=.5;g.beginPath();for(let x=-w/2+5;x<w/2;x+=7){g.moveTo(x,y);g.lineTo(x,y-sh)}g.stroke();y-=sh}
 g.fillStyle='#8d7f62';g.beginPath();g.moveTo(-9,0);g.lineTo(-6,y);g.lineTo(6,y);g.lineTo(9,0);g.fill();g.strokeStyle='rgba(255,255,255,.3)';g.lineWidth=.7;g.beginPath();for(let yy=-2;yy>y;yy-=2.5){g.moveTo(-8,yy);g.lineTo(8,yy)}g.stroke();
 const tw=[30,24,18][ty];g.fillStyle='#d8ccb0';g.fillRect(-tw/2,y-16,tw,16);g.fillStyle='#2a1d12';g.fillRect(-4,y-12,8,12);g.fillStyle=c;g.beginPath();g.moveTo(-tw/2-4,y-16);g.lineTo(tw/2+4,y-16);g.lineTo(tw/2-2,y-26);g.lineTo(-tw/2+2,y-26);g.fill();g.fillStyle='#e0b040';for(let x=-tw/2+2;x<tw/2-1;x+=5)g.fillRect(x,y-29,3,3);
 kFlag(tw/2+4,y-16,.8,c);if(ty<2)for(const sx of[-1,1]){g.fillStyle='rgba(255,150,50,.85)';g.beginPath();g.arc(sx*(W*.45),-14,2.5,0,7);g.fill();g.fillStyle='rgba(255,150,50,.2)';g.beginPath();g.arc(sx*(W*.45),-14,7,0,7);g.fill()}}
/* Châu Đại Dương: làng rào gỗ, nhà mái lá */
function keepPacific(ty,c){const g=X;kGround([92,70,50][ty],'#c8b47a');
 const hut=(x,yb,w,h)=>{g.fillStyle='#8a5a34';g.fillRect(x-w*.35,yb-h*.45,w*.7,h*.45);g.fillStyle='#2a1a10';g.fillRect(x-2,yb-h*.35,4,h*.35);g.fillStyle='#c9a45a';g.beginPath();g.moveTo(x-w/2-3,yb-h*.4);g.lineTo(x,yb-h-4);g.lineTo(x+w/2+3,yb-h*.4);g.fill();g.strokeStyle='rgba(90,60,20,.5)';g.lineWidth=.7;g.beginPath();for(let k=-3;k<=3;k++){g.moveTo(x,yb-h-4);g.lineTo(x+k*w/7,yb-h*.4)}g.stroke();g.fillStyle=c;g.fillRect(x-2,yb-h-7,4,4)};
 const post=(x,yb,h)=>{g.fillStyle='#6e3e22';g.fillRect(x-2.2,yb-h,4.4,h);g.fillStyle='#e8d2a0';g.fillRect(x-1.5,yb-h+3,3,2);g.fillRect(x-1.5,yb-h+8,3,2);g.fillStyle='#2a1a10';g.fillRect(x-1,yb-h+4,.8,.8);g.fillRect(x+.4,yb-h+4,.8,.8)};
 const fence=(x0,x1,yb,h)=>{for(let x=x0;x<x1;x+=4){g.fillStyle=(x/4|0)%2?'#8a5a34':'#a06a3e';g.fillRect(x,yb-h,3.2,h);g.beginPath();g.moveTo(x,yb-h);g.lineTo(x+1.6,yb-h-3);g.lineTo(x+3.2,yb-h);g.fill()}};
 if(ty==0){fence(-70,70,-30,12);hut(-34,-24,28,26);hut(34,-24,28,26);hut(0,-20,44,46);fence(-84,84,0,16);post(-10,0,24);post(10,0,24);for(const sx of[-1,1])post(sx*84,0,22);kFlag(30,-60,1,c)}
 else if(ty==1){hut(-22,-14,24,22);hut(16,-16,34,38);fence(-56,56,0,14);post(-8,0,20);post(8,0,20);kFlag(26,-50,.9,c)}
 else{hut(0,-4,30,32);fence(-30,30,0,11);post(-6,0,17);post(6,0,17);kFlag(14,-34,.8,c)}}
const KREG=[keepAsia,null,keepAfrica,keepFort,keepPyramid,keepPacific];
const regOf=s=>{if(s.race!==0||!WMAP)return -1;const cc=CC[s.cn];return cc?WREG.indexOf(cc.n):-1};
const RIC2=new Map();function CICONR(c,rl,ty,rg){const key=rg+'|'+c+'|'+rl+'|'+ty;let cv=RIC2.get(key);if(cv)return cv;cv=document.createElement('canvas');cv.width=cv.height=72;const g=cv.getContext('2d');g.strokeStyle=rl;g.lineWidth=3.2;g.beginPath();g.ellipse(36,61,[30,25,19][ty],6,0,0,7);g.stroke();
 const X0=X;X=g;try{g.setTransform(.36,0,0,.36,36,60);KREG[rg](ty,c)}finally{X=X0}RIC2.set(key,cv);if(RIC2.size>900)RIC2.delete(RIC2.keys().next().value);return cv}
function castle(s,t,z){const x=s.x,y=s.y,c=facC(s.fac);
 if(z<.42){const r=[9,7,5][s.type]/z,rg=regOf(s),sp=rg>=0&&KREG[rg]?CICONR(c,G?rel(s.fac):'#222',s.type,rg):CICON(c,G?rel(s.fac):'#222',s.type),sw=[34,28,22][s.type]/z;if(G&&s.own===0){X.fillStyle='rgba(255,210,58,.45)';X.beginPath();X.ellipse(x,y+sw*.32,sw*.6,sw*.17,0,0,7);X.fill()}X.drawImage(sp,x-sw/2,y-sw*.82,sw,sw);
  if((SMALL()?s.type==0:s.type<2)&&z>.14&&(!G||s.race==PC())){X.font=`bold ${11/z}px system-ui,sans-serif`;X.textAlign='center';X.lineWidth=3/z;X.strokeStyle='rgba(0,0,0,.8)';X.strokeText(s.name,x,y+r+12/z);X.fillStyle=G?rel(s.fac):'#fff';X.fillText(s.name,x,y+r+12/z)}return}
 const k=[1.5,1.2,1][s.type];X.save();X.translate(x,y);X.scale(k,k);
 X.restore();{const rg=regOf(s),kf=rg>=0&&KREG[rg],sp=kf?SPR(`kr${rg}|${s.type}|${c}`,240,200,120,160,()=>kf(s.type,c)):SPR(`kh${s.type}|${RACE[s.race].wall}|${c}`,240,200,120,160,()=>keepHD(s.type,RACE[s.race].wall,c)),q=[.95,.9,.9][s.type];X.drawImage(sp,x-120*q,y-160*q,240*q,200*q)}
 if(G&&s.race!=PC())return;const o=G&&G.L[s.own],mine=o&&o.kind=='pl',on=(!SMALL()||z>.95)&&o&&!o.dead?`${rank(o)[2]} ${o.kind=='pl'?rank(o)[0]+' (Bạn)':pname(o)}`:'',nm=`${relI(s.fac)} ${s.name}${s.type==0?' 👑':''}`+(SMALL()&&s.gar?` · 🛡${fmt(tot(s.gar))}`:''),bh=on?46:SMALL()?18:32;
 X.font='bold 13px system-ui,sans-serif';const w1=X.measureText(nm).width;X.font='11px system-ui,sans-serif';const tw=Math.max(w1,X.measureText(on).width);
 LBL.push({p:mine?1:2+s.type,x:x-tw/2-8,y:y+10,w:tw+16,h:bh,d:()=>{X.textAlign='center';X.fillStyle='rgba(18,12,6,.86)';X.fillRect(x-tw/2-8,y+10,tw+16,bh);X.fillStyle=c;X.fillRect(x-tw/2-8,y+10,4,bh);if(mine){X.strokeStyle='#ffd23a';X.lineWidth=2;X.strokeRect(x-tw/2-8,y+10,tw+16,bh)}
 X.font='bold 13px system-ui,sans-serif';X.fillStyle=G?rel(s.fac):'#fff';X.fillText(nm,x,y+24);X.font='11px system-ui,sans-serif';
 if(on){X.fillStyle=mine?'#ffd23a':'#e9dcc0';X.fillText(on,x,y+38)}X.fillStyle='#ffd77a';if(s.gar&&bh>18)X.fillText('🛡 '+fmt(tot(s.gar)),x,y+(on?52:38))}})}
function village(v,t,z){const x=v.x,y=v.y,s=S[v.p],mine=G&&v.own===0;
 if(z<.42){X.fillStyle=mine?'#ffd23a':G?rel(s.fac):'#ddd';CI(X,x,y,3.2/z);X.fillStyle=v.burn?'#333':'#8a6a3a';CI(X,x,y,2/z);return}
 {const vb=v.burn?1:0;const sp=SPR('v'+vb,120,80,60,30,()=>{for(let i=0;i<4;i++){X.fillStyle=vb?'#4a4036':['#c9b45a','#8fae4a','#b9a04a','#9dbb55'][i];X.save();X.rotate(.3);X.fillRect(-46+i*22,8+(i%2)*10,20,13);X.restore()}
 for(const [hx,hy] of[[-14,-2],[6,-8],[18,4],[-2,8]]){X.fillStyle='rgba(0,0,0,.25)';E(X,hx+3,hy+3,8,3);X.fillStyle=vb?'#3a3530':'#e2d2ac';X.fillRect(hx-6,hy-6,12,8);X.fillStyle=vb?'#1e1a18':'#a5522c';TRI(X,hx-8,hy-6,hx+8,hy-6,hx,hy-13)}});X.drawImage(sp,x-60,y-30,120,80)}X.save();X.translate(x,y);
 if(v.burn){X.fillStyle='rgba(60,60,60,.35)';for(let i=0;i<4;i++)CI(X,Math.sin(t+i)*6,-18-((t*12+i*9)%30),5+i)}X.restore();
 if(SMALL()&&!mine&&z<1.1)return;if(G&&s.race!=PC())return;const o=G&&G.L[v.own],nm=`🌾 ${v.name}`,on=!SMALL()&&o&&!o.dead?(mine?'⭐ Đất phong của bạn':`${rank(o)[2]} ${pname(o)}`):mine?'⭐ của bạn':'';
 X.font='bold 11px system-ui,sans-serif';const tw=Math.max(X.measureText(nm).width,X.measureText(on).width),bh=on?28:15;
 LBL.push({p:mine?1.5:8,x:x-tw/2-6,y:y+22,w:tw+12,h:bh,d:()=>{X.textAlign='center';X.font='bold 11px system-ui,sans-serif';X.fillStyle='rgba(18,12,6,.78)';X.fillRect(x-tw/2-6,y+22,tw+12,bh);if(mine){X.strokeStyle='#ffd23a';X.lineWidth=1.5;X.strokeRect(x-tw/2-6,y+22,tw+12,bh)}
 X.fillStyle=mine?'#ffd23a':G?rel(s.fac):'#fff';X.fillText(nm,x,y+33);if(on){X.font='10px system-ui,sans-serif';X.fillStyle=mine?'#ffe9a0':'#d9ccb0';X.fillText(on,x,y+46)}}})}
function blob(c,z){const k=Math.min(2.4,1/Math.min(1,z)),r=cl(5+Math.log10(c.n+1)*3,7,20)*k,col=facC(c.fac),re=rel(c.fac);
 X.fillStyle='rgba(0,0,0,.3)';E(X,c.x+2*k,c.y+3*k,r*1.1,r*.5);X.fillStyle=re;CI(X,c.x,c.y,r+2.5*k);X.fillStyle=col;CI(X,c.x,c.y,r);X.fillStyle='rgba(255,255,255,.25)';CI(X,c.x-r*.3,c.y-r*.3,r*.35);
 const l=`${c.k?'👑 ':''}${fmt(c.n)}`;X.font=`900 ${10*k}px system-ui`;X.textAlign='center';X.lineWidth=3*k;X.strokeStyle='#000';X.strokeText(l,c.x,c.y+3.5*k);X.fillStyle='#fff';X.fillText(l,c.x,c.y+3.5*k);
 X.font=`700 ${8.5*k}px system-ui`;const s=`${c.m} đạo quân`;X.strokeText(s,c.x,c.y+r+11*k);X.fillStyle=re;X.fillText(s,c.x,c.y+r+11*k)}
function party(p,t,z){const c=facC(p.fac),x=p.x,y=p.y,n=tot(p.t);
 if(z<.42||(ULQ&&p.kind!='pl')){const zq=z<.42?z:.55;const r=(p.kind=='pl'?5:p.kind=='rf'?2.5:cl(2+Math.log10(n+1)*1.2,2.5,6))/zq;
  if(p.kind=='pl'){X.strokeStyle='#ffd65a';X.lineWidth=2.5/zq;X.beginPath();X.arc(x,y,r+4/zq,0,7);X.stroke()}
  X.fillStyle=rel(p.fac);CI(X,x,y,r+1.8/zq);X.fillStyle=c;CI(X,x,y,r);
  if(p.kind=='pl'||(p.kind=='king'&&z>.15)){X.font=`bold ${10/zq}px system-ui`;X.textAlign='center';X.lineWidth=3/zq;X.strokeStyle='#000';const l=(p.kind=='pl'?'★ Bạn ':'')+fmt(n);X.strokeText(l,x,y-r-4/zq);X.fillStyle=p.kind=='pl'?'#ffd65a':'#fff';X.fillText(l,x,y-r-4/zq)}return}
 if(p.kind=='pl'){X.strokeStyle='#ffd65a';X.lineWidth=2.5;X.beginPath();X.ellipse(x,y+1,17,7,0,0,7);X.stroke()}else if(p.kind!='rf'){X.strokeStyle=rel(p.fac);X.globalAlpha=.85;X.lineWidth=2;X.beginPath();X.ellipse(x,y+1,15,6,0,0,7);X.stroke();X.globalAlpha=1}
 if(p.kind=='rf'){X.fillStyle='rgba(0,0,0,.3)';E(X,x+1,y+1,9,3);X.fillStyle='#7a5a32';X.fillRect(x-8,y-9,16,8);X.fillStyle=c;X.fillRect(x-8,y-12,16,3);X.fillStyle='#3a2a1a';CI(X,x-5,y,2.5);CI(X,x+5,y,2.5)}
 else{const k=p.t.cav>p.t.inf*.5?'cav':'inf';if(tAt(x,y)==0){X.fillStyle='#6b4423';X.beginPath();X.moveTo(x-20,y-6);X.lineTo(x+20,y-6);X.lineTo(x+14,y+4);X.lineTo(x-14,y+4);X.fill();X.fillStyle='#3a2a1a';X.fillRect(x-1,y-40,2,34);X.fillStyle='#efe6d0';TRI(X,x+1,y-40,x+16,y-12,x+1,y-12)}X.save();X.translate(x,y-(tAt(x,y)==0?6:0));X.scale(1.3,1.3);soldier(0,0,k,c,p.face,p.mv?t:0,raceOf(p));X.restore();
  X.fillStyle='#3a2a1a';X.fillRect(x-13,y-38,1.6,36);X.fillStyle=c;const wv=Math.sin(t*4+x)*1.5;X.beginPath();X.moveTo(x-11.5,y-38);X.lineTo(x+1,y-37+wv);X.lineTo(x+1,y-28+wv);X.lineTo(x-11.5,y-29);X.fill();
  if(p.kind=='king'){X.fillStyle='#ffd23a';TRI(X,x-10,y-41,x-6,y-41,x-8,y-46)}}
 if(p.kind=='rf'&&SMALL())return;if(p.kind!='pl'&&contOf(x,y)!=PC())return;X.font='bold 10px system-ui,sans-serif';const full=p.kind=='pl'||p.kind=='king'||(z>(SMALL()?.95:.6)),lb=(p.kind=='lord'||p.kind=='king'||p.kind=='pl'?rank(p)[2]+' ':'')+(full||p.kind!='lord'?pname(p)+' · ':'')+fmt(n),tw=X.measureText(lb).width;
 const rk=rank(p),ri0=RK.indexOf(rk[0]),plate=(p.kind=='pl'||p.kind=='king'||p.kind=='exile'||ri0>=4||(p._gl||0)>=3)&&p.kind!='rf'&&p.kind!='bandit';
 LBL.push({p:p.kind=='pl'?0:p.kind=='king'?5:atWar(P0().fac,p.fac)?6:p.kind=='rf'?9:7,x:x-tw/2-4,y:y+5,w:tw+8,h:13,d:()=>{if(plate)titlePlate(x,y-50,rk,t);if(p.kind=='pl')dhPlates(x,y-72,t);X.textAlign='center';X.font='bold 10px system-ui,sans-serif';X.fillStyle='rgba(15,10,6,.74)';X.fillRect(x-tw/2-4,y+5,tw+8,13);X.fillStyle=p.kind=='pl'?'#ffd65a':p.kind=='rf'?'#9cf':rel(p.fac);X.fillText(lb,x,y+15)}})}
function titlePlate(x,y,rk,t){const txt=rk[0].toUpperCase(),hi=RK.indexOf(rk[0]),big=hi>=9,ic=rk[2],col=rk[3],gl=.55+Math.sin(t*3+x*.01)*.45;
 X.font='800 8.5px system-ui,sans-serif';const tw=X.measureText(txt).width,w=tw+26,h=13;X.save();X.translate(x,y);
 if(!LOWQ){X.shadowColor=col;X.shadowBlur=(big?18:hi>=7?12:7)*gl}
 if(big||hi>=7){X.fillStyle=col;X.globalAlpha=.85;for(const s of[-1,1]){X.beginPath();X.moveTo(s*(w/2-2),-2);X.quadraticCurveTo(s*(w/2+12),-11,s*(w/2+16),-3);X.quadraticCurveTo(s*(w/2+9),-3,s*(w/2+13),3);X.quadraticCurveTo(s*(w/2+5),1,s*(w/2-2),4);X.fill()}X.globalAlpha=1}
 const g=X.createLinearGradient(0,-h/2,0,h/2);g.addColorStop(0,'#4a3618');g.addColorStop(.5,'#120c06');g.addColorStop(1,'#3a2a12');X.fillStyle=g;
 X.beginPath();X.moveTo(-w/2+6,-h/2);X.lineTo(w/2-6,-h/2);X.lineTo(w/2,0);X.lineTo(w/2-6,h/2);X.lineTo(-w/2+6,h/2);X.lineTo(-w/2,0);X.closePath();X.fill();
 X.lineWidth=1.6;X.strokeStyle=col;X.stroke();X.shadowBlur=0;X.lineWidth=.6;X.strokeStyle='rgba(255,240,200,.55)';X.beginPath();X.moveTo(-w/2+8,-h/2+2);X.lineTo(w/2-8,-h/2+2);X.lineTo(w/2-3,0);X.lineTo(w/2-8,h/2-2);X.lineTo(-w/2+8,h/2-2);X.lineTo(-w/2+3,0);X.closePath();X.stroke();
 for(const s of[-1,1]){X.fillStyle=col;X.beginPath();X.moveTo(s*(w/2+1),0);X.lineTo(s*(w/2-3),-3);X.lineTo(s*(w/2-7),0);X.lineTo(s*(w/2-3),3);X.fill();X.fillStyle='#fff';X.fillRect(s*(w/2-3)-.6,-.6,1.2,1.2)}
 if(hi>=6){X.fillStyle=col;X.beginPath();X.moveTo(-6,-h/2);X.lineTo(-6,-h/2-4);X.lineTo(-3,-h/2-2);X.lineTo(0,-h/2-6);X.lineTo(3,-h/2-2);X.lineTo(6,-h/2-4);X.lineTo(6,-h/2);X.fill()}
 X.textAlign='center';X.font='800 8.5px system-ui,sans-serif';const tg=X.createLinearGradient(0,-4,0,4);tg.addColorStop(0,'#fffbe8');tg.addColorStop(1,col);X.fillStyle=tg;X.fillText(txt,0,3.2);
 X.font='9px system-ui';X.fillText(ic,0,-h/2-(hi>=6?8:3));X.restore()}
function drawFights(t,z){for(const f of G.fights){const P=fightPow(f),pu=1+Math.sin(t*6)*.15;
 if(z<.42){X.strokeStyle='#ff4a3a';X.lineWidth=3/z;X.beginPath();X.arc(f.x,f.y,12*pu/z,0,7);X.stroke();X.font=`${15/z}px system-ui`;X.textAlign='center';X.fillStyle='#fff';X.fillText('⚔',f.x,f.y+5/z);continue}
 X.fillStyle='rgba(140,110,70,.28)';for(let i=0;i<7;i++){const a=t*1.5+i,r=18+((t*20+i*13)%24);E(X,f.x+Math.cos(a)*r,f.y+Math.sin(a)*r*.5,11,5)}
 X.strokeStyle='rgba(255,70,50,.9)';X.lineWidth=2.5;X.beginPath();X.ellipse(f.x,f.y,42*pu,17*pu,0,0,7);X.stroke();X.font='24px system-ui';X.textAlign='center';X.fillText('⚔️',f.x,f.y-34);
 const l=`${facN(f.af)} ${fmt(P.ta)} ⚔ ${fmt(P.td)} ${f.s>=0?S[f.s].name:facN(f.df)}`;X.font='bold 11px system-ui';const tw=X.measureText(l).width;X.fillStyle='rgba(70,12,6,.88)';X.fillRect(f.x-tw/2-6,f.y-80,tw+12,16);X.fillStyle='#fff';X.fillText(l,f.x,f.y-68);
 const k=P.sa/((P.sa+P.sd)||1);X.fillStyle='#ff5040';X.fillRect(f.x-42,f.y-61,84,5);X.fillStyle='#4aa3ff';X.fillRect(f.x-42,f.y-61,84*k,5)}}
function mmRect(){const sm=H<520,b=CWB(),w=Math.min(240,Math.max(120,W*(sm?.17:.22))),h=w*b.h/b.w;return{x:W-w-(sm?52:6),y:H-h-6,w,h}}
function clampCam(c){const hw=W/2/c.z,hh=H/2/c.z,b=G&&G.L?CWB():{x0:0,y0:0,w:WW,h:2*CH+GAP};c.x=b.w>hw*2?cl(c.x,b.x0+hw,b.x0+b.w-hw):b.x0+b.w/2;c.y=b.h>hh*2?cl(c.y,b.y0+hh,b.y0+b.h-hh):b.y0+b.h/2}
function drawMap(t){const c=MC;if(G&&c.follow){c.x=P0().x;c.y=P0().y}if(!G)c.x+=Math.sin(t*.1)*.3;clampCam(c);const z=c.z;
 X.setTransform(DPR,0,0,DPR,0,0);X.fillStyle='#1d4570';X.fillRect(0,0,W,H);
 X.setTransform(DPR*z,0,0,DPR*z,DPR*(W/2-c.x*z),DPR*(H/2-c.y*z));
 const vx0=c.x-W/2/z,vy0=c.y-H/2/z,vx1=c.x+W/2/z,vy1=c.y+H/2/z;
 
 X.imageSmoothingEnabled=true;X.drawImage(LOW,Math.max(0,vx0/40),Math.max(0,vy0/40),Math.min(LOW.width,vx1/40)-Math.max(0,vx0/40),Math.min(LOW.height,vy1/40)-Math.max(0,vy0/40),Math.max(0,vx0),Math.max(0,vy0),(Math.min(LOW.width,vx1/40)-Math.max(0,vx0/40))*40,(Math.min(LOW.height,vy1/40)-Math.max(0,vy0/40))*40);if(z>.1)for(let c=0;c<13;c++){const cv=BGC[c];if(!cv)continue;const ox=OX[c]-BGP,oy=OY[c]-BGP,a0=Math.max(vx0,ox),b0=Math.max(vy0,oy),a1=Math.min(vx1,ox+cv.width*BS),b1=Math.min(vy1,oy+cv.height*BS);if(a1<=a0||b1<=b0)continue;X.drawImage(cv,(a0-ox)/BS,(b0-oy)/BS,(a1-a0)/BS,(b1-b0)/BS,a0,b0,a1-a0,b1-b0)}
 if(G)for(let c=0;c<12;c++){if(OPEN(c))continue;if(OX[c]>vx1||OX[c]+CWc[c]<vx0||OY[c]>vy1||OY[c]+CHc[c]<vy0)continue;X.fillStyle=c>=9?'rgba(10,20,40,.82)':'rgba(18,6,36,.78)';X.fillRect(OX[c]-GAP/2,OY[c]-GAP/2,CWc[c]+GAP,CHc[c]+GAP);X.textAlign='center';X.font=`900 ${Math.min(CW/12,Math.max(40,34/z))}px system-ui`;X.fillStyle='#d9c2ff';X.fillText('🔒 '+RACE[c].n.toUpperCase(),OX[c]+CWc[c]/2,OY[c]+CHc[c]/2);X.font=`700 ${Math.min(CW/32,Math.max(18,15/z))}px system-ui`;X.fillText(LOCKT(c),OX[c]+CWc[c]/2,OY[c]+CHc[c]/2+Math.max(50,42/z));if(c>=5&&c<9){X.fillStyle='#9ff0ff';X.fillText('Sau đó chiếm 2/4 lục địa Thần linh → mở 🌀 Cửu Thiên Huyền Giới',OX[c]+CWc[c]/2,OY[c]+CHc[c]/2+Math.max(95,80/z))}}
 X.globalAlpha=z<.12?.95:z<.4?.75:z<.8?.5:.32;{const a0=Math.max(0,Math.floor(vx0/TCS)),b0=Math.max(0,Math.floor(vy0/TCS)),a1=Math.min(TC.width,Math.ceil(vx1/TCS)+1),b1=Math.min(TC.height,Math.ceil(vy1/TCS)+1);if(a1>a0&&b1>b0)X.drawImage(TC,a0,b0,a1-a0,b1-b0,a0*TCS,b0*TCS,(a1-a0)*TCS,(b1-b0)*TCS)}X.globalAlpha=1;
 if(z>(ULQ?.5:.22)){const RV=[];for(const r of ROADS){if((r[0]<vx0-80&&r[4]<vx0-80)||(r[0]>vx1+80&&r[4]>vx1+80)||(r[1]<vy0-80&&r[5]<vy0-80)||(r[1]>vy1+80&&r[5]>vy1+80))continue;RV.push(r)}X.lineCap='round';for(const [w,col] of[[7,'rgba(90,66,36,.5)'],[3.5,'#c9ab78']]){X.strokeStyle=col;X.lineWidth=Math.max(w,w*.4/z);X.beginPath();for(const r of RV){X.moveTo(r[0],r[1]);X.quadraticCurveTo(r[2],r[3],r[4],r[5])}X.stroke()}}
 if(!ULQ&&z>(LOWQ?.55:.38)){const bx0=Math.max(0,vx0>>9),bx1=Math.min(BKX-1,vx1>>9),by0=Math.max(0,vy0>>9),by1=Math.min(BKY-1,(vy1+60)>>9);
  for(let j=by0;j<=by1;j++)for(let i=bx0;i<=bx1;i++){const idx=j*BKX+i;if(!DET[idx].length)continue;let cv=BKC.get(idx);
   if(!cv){cv=document.createElement('canvas');const S2=.75;cv.width=592*S2;cv.height=592*S2;const g=cv.getContext('2d'),X0=X;X=g;g.setTransform(S2,0,0,S2,(-(i<<9)+40)*S2,(-(j<<9)+60)*S2);const its=DET[idx];try{
  const pth=(f,st)=>{X.beginPath();for(const d of its)f(d);X.fillStyle=st;X.fill()};
  pth(d=>{if(d[3]==0){X.moveTo(d[0]+d[2]*1.5,d[1]+1);X.ellipse(d[0]+d[2]*.5,d[1]+1,d[2],d[2]*.4,0,0,7)}else if(d[3]==1){X.moveTo(d[0]-d[2],d[1]);X.lineTo(d[0]+d[2]*1.4,d[1]);X.lineTo(d[0]+d[2]*.2,d[1]-d[2]*.4)}},'rgba(0,0,0,.2)');
  pth(d=>{if(d[3]==1){X.moveTo(d[0]-d[2],d[1]);X.lineTo(d[0],d[1]-d[2]*1.3);X.lineTo(d[0],d[1])}},'#a49a8e');
  pth(d=>{if(d[3]==1){X.moveTo(d[0],d[1]-d[2]*1.3);X.lineTo(d[0]+d[2],d[1]);X.lineTo(d[0],d[1])}},'#776e64');
  pth(d=>{if(d[3]==1&&d[4]>.73){X.moveTo(d[0]-d[2]*.38,d[1]-d[2]*.8);X.lineTo(d[0],d[1]-d[2]*1.3);X.lineTo(d[0]+d[2]*.38,d[1]-d[2]*.8)}},'#f4f6f8');
  X.beginPath();for(const d of its)if(d[3]==2){const s=d[2];X.moveTo(d[0],d[1]);X.lineTo(d[0],d[1]-s*1.6);X.moveTo(d[0],d[1]-s*.9);X.lineTo(d[0]-s*.6,d[1]-s*1.4);X.moveTo(d[0],d[1]-s*1.2);X.lineTo(d[0]+s*.7,d[1]-s*1.7);X.moveTo(d[0]-s*.3,d[1]-s*1.15);X.lineTo(d[0]-s*.7,d[1]-s*1.2)}X.strokeStyle='#3e3530';X.lineWidth=1.6;X.lineCap='round';X.stroke();
  pth(d=>{if(d[3]==0)X.rect(d[0]-1,d[1]-d[2]*.5,2.2,d[2]*.6)},'#4a3020');
  pth(d=>{if(d[3]==0){X.moveTo(d[0]+d[2]*.85,d[1]-d[2]*.9);X.arc(d[0],d[1]-d[2]*.9,d[2]*.85,0,7)}},'#2c5622');
  pth(d=>{if(d[3]==0){X.moveTo(d[0]+d[2]*.3,d[1]-d[2]*1.1);X.arc(d[0]-d[2]*.25,d[1]-d[2]*1.1,d[2]*.55,0,7)}},'#3d7a2c')
   }finally{X=X0}BKC.set(idx,cv);if(BKC.size>70)BKC.delete(BKC.keys().next().value)}
   X.drawImage(cv,(i<<9)-40,(j<<9)-60,592,592)}}
 if(G&&G.mk){X.strokeStyle='rgba(255,220,100,'+cl(G.mk.t,0,1)+')';X.lineWidth=2/Math.min(1,z);X.beginPath();X.ellipse(G.mk.x,G.mk.y,10/Math.min(1,z),4/Math.min(1,z),0,0,7);X.stroke()}
 const vis=o=>o.x>vx0-90&&o.x<vx1+90&&o.y>vy0-90&&o.y<vy1+90;
 const ob=S.filter(s=>vis(s)&&OPEN(s.race)).map(s=>({y:s.y,d:()=>castle(s,t,z)}));if(z>(ULQ?.3:.16))for(const v of V)if(vis(v)&&OPEN(S[v.p].race))ob.push({y:v.y-1,d:()=>village(v,t,z)});if(G){const VP=G.L.filter(p=>!p.dead&&vis(p)&&(p.kind=='pl'||(z>.1&&OPEN(contOf(p.x,p.y))))),dense=VP.length>(ULQ?6:LOWQ?14:24)||(G.ngen||0)>=200,CS=Math.max(140,90/z),CL=new Map();
 const rfDot=tot(P0().t)>=20000;
 for(const p of VP){if(rfDot&&p.kind=='rf'){ob.push({y:p.y,d:()=>{const k=1/Math.min(1,z),r=3.5*k;X.fillStyle='#000';CI(X,p.x,p.y,r+1.2*k);X.fillStyle=p.to===0?'#7cc4ff':facC(p.fac);CI(X,p.x,p.y,r)}});continue}
  if(p.kind=='pl'||!dense||p.inF){ob.push({y:p.y+(p.kind=='pl'?.1:0),d:()=>party(p,t,z)});continue}
  const k=(p.fac)+'|'+Math.floor(p.x/CS)+'|'+Math.floor(p.y/CS);let c=CL.get(k);if(!c){c={n:0,m:0,x:0,y:0,fac:p.fac,k:0,ps:[]};CL.set(k,c)}c.n+=tot(p.t);c.m++;c.x+=p.x;c.y+=p.y;c.ps.push(p);if(p.kind=='king')c.k=1}
 for(const c of CL.values()){if(c.m==1){const p=c.ps[0];ob.push({y:p.y,d:()=>party(p,t,z)});continue}c.x/=c.m;c.y/=c.m;ob.push({y:c.y,d:()=>blob(c,z)})}}
 LBL.length=0;ob.sort((a,b)=>a.y-b.y).forEach(o=>o.d());
 {LBL.sort((a,b)=>a.p-b.p);const pl=[],mg=4/Math.min(1,z),cap=SMALL()?28:80;let n=0;const top=[];for(const L of LBL){if(L.p===0){top.push(L);continue}if(n>=cap&&L.p>1)break;if(pl.some(q=>L.x<q.x+q.w+mg&&L.x+L.w+mg>q.x&&L.y<q.y+q.h+mg&&L.y+L.h+mg>q.y))continue;pl.push(L);L.d();n++}top.forEach(L=>{const hit=pl.some(q=>L.x<q.x+q.w&&L.x+L.w>q.x&&L.y<q.y+q.h&&L.y+L.h>q.y);if(hit){X.save();X.translate(0,-62);L.d();X.restore()}else L.d()})}
 if(G&&G.xian&&G.portals)for(const q of G.portals){if(!vis(q))continue;const k=z<.42?.45/z:1,pu=1+Math.sin(t*3)*.08;X.save();X.translate(q.x,q.y);X.scale(k,k);
  X.fillStyle='rgba(0,0,0,.3)';E(X,0,4,30,8);X.fillStyle='#3a3048';X.fillRect(-24,-46,7,46);X.fillRect(17,-46,7,46);X.fillRect(-26,-50,52,7);
  const gr=X.createRadialGradient(0,-22,2,0,-22,20);gr.addColorStop(0,'rgba(255,255,255,.95)');gr.addColorStop(.4,'rgba(150,220,255,.85)');gr.addColorStop(1,'rgba(120,60,255,.15)');X.fillStyle=gr;X.beginPath();X.ellipse(0,-22,16*pu,22*pu,0,0,7);X.fill();
  X.strokeStyle='rgba(200,240,255,.9)';X.lineWidth=2;X.beginPath();X.ellipse(0,-22,12*pu,17*pu,t*2,0,4.5);X.stroke();
  X.font='bold 11px system-ui';X.textAlign='center';X.lineWidth=3;X.strokeStyle='#000';const l=q.w?'🌀 Thông đạo về Thần giới':'🌀 Thông đạo Cửu Thiên Huyền Giới';X.strokeText(l,0,14);X.fillStyle='#bff2ff';X.fillText(l,0,14);X.restore()}
 if(G)drawFights(t,z);
 if(G){const kg=myKing();if(kg&&contOf(kg.x,kg.y)==PC()){const k=1/Math.min(1,z),pu=1+Math.sin(t*4)*.15;X.strokeStyle='#c58cff';X.lineWidth=3*k;X.beginPath();X.ellipse(kg.x,kg.y+1,24*k*pu,10*k*pu,0,0,7);X.stroke();
  const ay=kg.y-(z<.42?22:80)*k;X.font=`${22*k}px system-ui`;X.textAlign='center';X.fillText('👑',kg.x,ay);X.font=`900 ${11*k}px system-ui`;X.lineWidth=3*k;X.strokeStyle='#000';X.strokeText('VUA '+fmt(tot(kg.t)),kg.x,ay-22*k);X.fillStyle='#e6c8ff';X.fillText('VUA '+fmt(tot(kg.t)),kg.x,ay-22*k)}}
 if(G){const p=P0(),k=1/Math.min(1,z),pu=1+Math.sin(t*5)*.18;X.strokeStyle='#ffd23a';X.lineWidth=3*k;X.beginPath();X.ellipse(p.x,p.y+1,22*k*pu,9*k*pu,0,0,7);X.stroke();X.strokeStyle='rgba(255,210,58,.35)';X.lineWidth=8*k;X.stroke();
  const ay=p.y-(z<.42?22:74+(dhN()?dhN()*15+30:0))*k-Math.abs(Math.sin(t*4))*6*k;X.fillStyle='#ffd23a';X.strokeStyle='#000';X.lineWidth=2*k;X.beginPath();X.moveTo(p.x-9*k,ay-12*k);X.lineTo(p.x+9*k,ay-12*k);X.lineTo(p.x,ay);X.closePath();X.fill();X.stroke();
  X.font=`900 ${12*k}px system-ui`;X.textAlign='center';X.lineWidth=3*k;X.strokeText('BẠN',p.x,ay-16*k);X.fillText('BẠN',p.x,ay-16*k)}
 X.textAlign='center';for(const m of mfx){if(!vis(m))continue;X.globalAlpha=cl(m.t,0,1);X.font=`bold ${Math.max(14,12/z)}px system-ui`;X.lineWidth=3/Math.min(1,z);X.strokeStyle='#000';X.strokeText(m.s,m.x,m.y);X.fillStyle=m.c;X.fillText(m.s,m.x,m.y);X.globalAlpha=1}
 if(!LOWQ&&z>.38)for(const cd of clouds){if(!vis({x:cd.x,y:cd.y}))continue;X.fillStyle='rgba(0,0,0,.07)';E(X,cd.x+40,cd.y+60,cd.r,cd.r*.45);X.fillStyle='rgba(255,255,255,.08)';E(X,cd.x,cd.y,cd.r,cd.r*.45);E(X,cd.x+cd.r*.4,cd.y-cd.r*.15,cd.r*.6,cd.r*.35)}
 X.textAlign='center';const fz=Math.min(CW/16,Math.max(26,22/z));X.font=`900 ${fz}px system-ui,sans-serif`;
 if(z<.12){X.font=`900 ${Math.min(CW/11,40/z)}px system-ui`;for(let c=0;c<NC();c++){const q={x:OX[c]+CWc[c]/2,y:OY[c]+CHc[c]*.12};X.lineWidth=8/z;X.strokeStyle='rgba(0,0,0,.7)';X.strokeText('🌍 '+RACE[c].n.toUpperCase(),q.x,q.y);X.fillStyle='#ffe9a8';X.fillText('🌍 '+RACE[c].n.toUpperCase(),q.x,q.y)}X.font=`900 ${fz}px system-ui,sans-serif`}
 for(const cc of CC){if(G&&cc.race!=PC())continue;if(cc.x<vx0-400||cc.x>vx1+400||cc.y<vy0-300||cc.y>vy1+300)continue;X.globalAlpha=z<.5?.95:.55;X.lineWidth=fz/5;X.strokeStyle='rgba(0,0,0,.7)';X.strokeText(cc.n.toUpperCase(),cc.x,cc.y-fz*1.2);X.fillStyle='#fff0c8';X.fillText(cc.n.toUpperCase(),cc.x,cc.y-fz*1.2);X.globalAlpha=1}
 if(G&&z<.65){const kz=Math.max(13,12/z);X.font=`800 ${kz}px system-ui,sans-serif`;const FA=new Map(),pc=PC();for(const s of S){if(s.race!=pc)continue;let a=FA.get(s.fac);if(!a)FA.set(s.fac,a=[0,0,0]);a[0]+=s.x;a[1]+=s.y;a[2]++}G.F.forEach((f,i)=>{if(f.dead)return;const a=FA.get(i);if(!a)return;const cx=a[0]/a[2],cy=a[1]/a[2];if(cx<vx0-300||cx>vx1+300||cy<vy0-200||cy>vy1+200)return;
  const l=`${relI(i)} ${f.n}`;X.lineWidth=kz/4;X.strokeStyle='rgba(0,0,0,.8)';X.strokeText(l,cx,cy-kz*2.5);X.fillStyle=rel(i);X.fillText(l,cx,cy-kz*2.5)})}
 X.setTransform(DPR,0,0,DPR,0,0);
 if(!LOWQ){if(!VG){VG=X.createRadialGradient(W/2,H/2,Math.min(W,H)*.45,W/2,H/2,Math.max(W,H)*.75);VG.addColorStop(0,'rgba(0,0,0,0)');VG.addColorStop(1,'rgba(0,0,0,.32)')}X.fillStyle=VG;X.fillRect(0,0,W,H)}
 if(G){const p=P0(),sx=(p.x-MC.x)*z+W/2,sy=(p.y-MC.y)*z+H/2;if(sx<0||sx>W||sy<0||sy>H){const a=Math.atan2(sy-H/2,sx-W/2),k2=Math.min(Math.abs((W/2-40)/Math.cos(a)),Math.abs((H/2-50)/Math.sin(a))),px=W/2+Math.cos(a)*k2,py=H/2+Math.sin(a)*k2;
  X.fillStyle='#ffd23a';X.strokeStyle='#000';X.lineWidth=2;X.save();X.translate(px,py);X.rotate(a);X.beginPath();X.moveTo(16,0);X.lineTo(-8,-11);X.lineTo(-8,11);X.closePath();X.fill();X.stroke();X.restore();X.font='bold 12px system-ui';X.textAlign='center';X.lineWidth=3;X.strokeText('📍 Bạn',px-Math.cos(a)*30,py-Math.sin(a)*22+4);X.fillText('📍 Bạn',px-Math.cos(a)*30,py-Math.sin(a)*22+4)}}
 {const kg=myKing();if(kg&&contOf(kg.x,kg.y)==PC()){const sx=(kg.x-MC.x)*z+W/2,sy=(kg.y-MC.y)*z+H/2;if(sx<0||sx>W||sy<0||sy>H){const a=Math.atan2(sy-H/2,sx-W/2),k2=Math.min(Math.abs((W/2-60)/Math.cos(a)),Math.abs((H/2-70)/Math.sin(a))),px=W/2+Math.cos(a)*k2,py=H/2+Math.sin(a)*k2;
  X.fillStyle='#c58cff';X.strokeStyle='#000';X.lineWidth=2;X.save();X.translate(px,py);X.rotate(a);X.beginPath();X.moveTo(16,0);X.lineTo(-8,-11);X.lineTo(-8,11);X.closePath();X.fill();X.stroke();X.restore();X.font='bold 12px system-ui';X.textAlign='center';X.lineWidth=3;X.strokeText('👑 Vua',px-Math.cos(a)*32,py-Math.sin(a)*22+4);X.fillText('👑 Vua',px-Math.cos(a)*32,py-Math.sin(a)*22+4)}}}
 if(!G)return;const m0=mmRect(),wb=CWB();X.fillStyle='#000';X.fillRect(m0.x-2,m0.y-2,m0.w+4,m0.h+4);X.drawImage(MMW[WRLD(P0().y)],m0.x,m0.y,m0.w,m0.h);
 const kx=m0.w/wb.w,ky=m0.h/wb.h,m={x:m0.x-wb.x0*kx,y:m0.y-wb.y0*ky,w:m0.w,h:m0.h};X.strokeStyle='rgba(255,255,255,.8)';X.lineWidth=1;X.strokeRect(m.x+vx0*kx,m.y+vy0*ky,(vx1-vx0)*kx,(vy1-vy0)*ky);
 X.font='bold 9px system-ui';X.textAlign='center';X.font='bold 10px system-ui';for(let c=0;c<NC();c++){if(CW_OF(c)!=WRLD(P0().y))continue;const q={x:OX[c]+CWc[c]/2,y:OY[c]+CHc[c]/2};X.lineWidth=3;X.strokeStyle='#000';X.strokeText(RACE[c].n,m.x+q.x*kx,m.y+q.y*ky);X.fillStyle='#fff0c8';X.fillText(RACE[c].n,m.x+q.x*kx,m.y+q.y*ky)}
 if(false)for(const cc of CC){X.lineWidth=3;X.strokeStyle='#000';X.strokeText(cc.n,m.x+cc.x*kx,m.y+cc.y*ky);X.fillStyle='#fff0c8';X.fillText(cc.n,m.x+cc.x*kx,m.y+cc.y*ky)}
 {const kg=myKing();if(kg){X.fillStyle='#c58cff';CI(X,m.x+kg.x*kx,m.y+kg.y*ky,3.5)}}X.fillStyle='#fff';CI(X,m.x+P0().x*kx,m.y+P0().y*ky,3.5);X.strokeStyle='#000';X.lineWidth=1;X.stroke();X.strokeStyle='#c9a052';X.strokeRect(m0.x-2,m0.y-2,m0.w+4,m0.h+4);
 // mũi tên chỉ hướng các nước nằm ngoài màn hình
 const aL=(ARW-performance.now())/1000;if(aL>0){X.globalAlpha=cl(aL,0,1);X.font='bold 11px system-ui';const cur=contOf(MC.x,MC.y),PTS=CC.filter(q=>q.race==cur).sort((a,b)=>dist(a,MC)-dist(b,MC)).slice(0,SMALL()?3:6);const PL=[],port=W<H*1.1;for(const cc of PTS){if((cc.x>vx0&&cc.x<vx1&&cc.y>vy0&&cc.y<vy1)||Math.hypot(cc.x-MC.x,cc.y-MC.y)<900)continue;const dx=cc.x-MC.x,dy=cc.y-MC.y,a=Math.atan2(dy,dx),hw=SMALL()?Math.max(60,W/2-80):W/2-140,hh=SMALL()?H/2-90:H/2-62,k=Math.min(Math.abs(hw/Math.cos(a)),Math.abs(hh/Math.sin(a)));
  const px=W/2+Math.cos(a)*k-30;let py=H/2+Math.sin(a)*k;if(px>m0.x-70&&py>m0.y-14)py=m0.y-16;if(PL.some(q=>Math.abs(q[1]-py)<24&&Math.abs(q[0]-px)<170))continue;PL.push([px,py]);const ci=CC.indexOf(cc),fs=G.F.filter(f=>(cc.cont?f.race==cc.race:f.cn==ci)&&!f.dead).map(f=>G.F.indexOf(f)),en=fs.some(f=>atWar(P0().fac,f)),my=fs.includes(P0().fac),col=my?'#7dff8a':en?'#ff6a5a':'#f2f2f2';
  const l=SMALL()?cc.n:`${cc.n} ${fmt(Math.hypot(dx,dy)/100)} dặm`,tw=X.measureText(l).width;X.fillStyle='rgba(15,10,6,.85)';X.fillRect(px-tw/2-8,py-10,tw+16,20);X.strokeStyle=col;X.lineWidth=1.5;X.strokeRect(px-tw/2-8,py-10,tw+16,20);X.fillStyle=col;X.fillText(l,px,py+4);
  X.save();X.translate(px+Math.cos(a)*(tw/2+18),py+Math.sin(a)*18);X.rotate(a);TRI(X,9,0,-5,-7,-5,7);X.restore()}X.globalAlpha=1}}
