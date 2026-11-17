'use strict';
const $=s=>document.querySelector(s);
const C=$('#c');let X=C.getContext('2d');
let W=0,H=0,DPR=1;
const MOB=matchMedia('(pointer:coarse)').matches;let QL=(()=>{try{const v=localStorage.getItem('ltlc-q');if(v)return +v||0}catch(e){}return matchMedia('(pointer:coarse)').matches?1:0})(),LOWQ=QL>=1,ULQ=QL==2,VG=null;
let DSR=1;function rs(){DPR=(ULQ?.75:LOWQ?1:Math.min(2,devicePixelRatio||1))*DSR;VG=null;W=innerWidth;H=innerHeight;C.width=W*DPR|0;C.height=H*DPR|0;document.body.classList.toggle('sm',W<720||H<520)}
addEventListener('resize',rs);rs();
let sd=7771;const R=()=>(sd=sd*16807%2147483647)/2147483647;
const rnd=(a,b)=>a+Math.random()*(b-a),ri=(a,b)=>Math.floor(rnd(a,b+1)),dist=(a,b)=>Math.hypot(a.x-b.x,a.y-b.y),cl=(v,a,b)=>v<a?a:v>b?b:v;
const E=(g,x,y,rx,ry)=>{g.beginPath();g.ellipse(x,y,rx,ry,0,0,7);g.fill()},CI=(g,x,y,r)=>{g.beginPath();g.arc(x,y,r,0,7);g.fill()};
const TRI=(g,a,b,c,d,e,f)=>{g.beginPath();g.moveTo(a,b);g.lineTo(c,d);g.lineTo(e,f);g.closePath();g.fill()};
const fmt=n=>{n=Math.round(n)||0;const a=n<0?'-':'',v=''+Math.abs(n);return v.length<4?a+v:a+v.replace(/\B(?=(\d{3})+(?!\d))/g,'.')};
const KS=['inf','arc','cav'],tot=t=>t.inf+t.arc+t.cav,str=t=>t.inf+t.arc*1.15+t.cav*1.7;
const Z3=()=>({inf:0,arc:0,cav:0}),add=(a,b)=>KS.forEach(k=>a[k]+=Math.max(0,Math.floor(b[k])||0));
function take(t,n){const o=Z3(),T=tot(t);n=Math.min(Math.round(n),T);if(!T||!(n>0))return o;let rem=n;
 for(const k of KS){const c=Math.min(t[k],Math.floor(n*t[k]/T));t[k]-=c;o[k]+=c;rem-=c}
 for(const k of KS){const c=Math.min(t[k],rem);t[k]-=c;o[k]+=c;rem-=c}return o}
const kill=(t,n)=>{take(t,n)};
const mix=n=>{n=Math.max(0,Math.round(n)||0);const a=Math.round(n*.55),b=Math.round(n*.3);return{inf:a,arc:b,cav:n-a-b}};
const fk=n=>{n=Math.round(n)||0;const a=Math.abs(n),s=n<0?'-':'';return a>=1e9?s+(a/1e9).toFixed(a>=1e10?0:1)+'tỷ':a>=1e6?s+(a/1e6).toFixed(a>=1e7?0:1)+'tr':a>=1e4?s+Math.round(a/1e3)+'k':fmt(n)};
const tt=t=>`🗡${fmt(t.inf)} 🏹${fmt(t.arc)} 🐎${fmt(t.cav)} <b>(${fmt(tot(t))})</b>`;
function auto(a,b,bb){for(let r=0;r<120&&tot(a)&&tot(b);r++){const sa=str(a),sb=str(b)*bb;kill(b,Math.max(1,Math.round(sa*rnd(.03,.06)/bb)));kill(a,Math.max(1,Math.round(sb*rnd(.03,.06))))}
 if(!tot(b))return 1;if(!tot(a))return 0;return str(a)>str(b)*bb?1:0}

let AC=null,muted=0;
function au(){if(!AC){try{AC=new(window.AudioContext||window.webkitAudioContext)()}catch(e){}}if(AC&&AC.state=='suspended')AC.resume();return AC}
addEventListener('pointerdown',au);
function tone(f,d,ty='sine',v=.15,f2){const a=au();if(!a||muted)return;const o=a.createOscillator(),g=a.createGain(),t0=a.currentTime;o.type=ty;o.frequency.setValueAtTime(f,t0);if(f2)o.frequency.exponentialRampToValueAtTime(f2,t0+d);g.gain.setValueAtTime(v,t0);g.gain.exponentialRampToValueAtTime(.001,t0+d);o.connect(g);g.connect(a.destination);o.start(t0);o.stop(t0+d+.02)}
let NB=null;function nz(d,v,fq){const a=au();if(!a||muted)return;if(!NB){NB=a.createBuffer(1,a.sampleRate,a.sampleRate);const c=NB.getChannelData(0);for(let i=0;i<c.length;i++)c[i]=Math.random()*2-1}
 const s=a.createBufferSource(),f=a.createBiquadFilter(),g=a.createGain(),t0=a.currentTime;s.buffer=NB;f.type='bandpass';f.frequency.value=fq;f.Q.value=.8;g.gain.setValueAtTime(v,t0);g.gain.exponentialRampToValueAtTime(.001,t0+d);s.connect(f);f.connect(g);g.connect(a.destination);s.start(t0,Math.random()*.5,d+.05)}
const SFX={horn(){tone(196,1.1,'sawtooth',.07);setTimeout(()=>tone(294,1,'sawtooth',.06),300)},clash(){nz(.09,.16,2800+Math.random()*1500);tone(2200+Math.random()*1200,.06,'square',.02)},arrow(){nz(.22,.07,5200)},drum(){tone(85,.3,'sine',.3,40)},
 fan(){[523,659,784,1046].forEach((f,i)=>setTimeout(()=>tone(f,.4,'triangle',.12),i*150))},bad(){[392,330,262].forEach((f,i)=>setTimeout(()=>tone(f,.45,'triangle',.1),i*200))},ping(){tone(880,.18,'triangle',.08);setTimeout(()=>tone(1320,.2,'triangle',.06),90)},war(){tone(110,.6,'sawtooth',.08,80);nz(.4,.1,600)}};
let RFS=0,RFT=0;const TQ=[];function toast(m,c='#ffd77a',big){if(mode=='battle'){if(big)TQ.push([m,c,big]);return}const d=document.createElement('div');d.className='tst'+(big?' big':'');d.style.borderColor=c;d.innerHTML=m;const T=$('#toast');T.appendChild(d);while(T.children.length>(SMALL()?1:2))T.firstChild.remove();setTimeout(()=>d.remove(),big?5000:(SMALL()?2600:3600));(big?SFX.fan:SFX.ping)()}
const comb=l=>{const t=Z3();l.forEach(o=>add(t,o));return t};
function distrib(l,init,surv){KS.forEach(k=>{const r=init[k]?surv[k]/init[k]:0;l.forEach(o=>o[k]=Math.round(o[k]*r))})}

/* ================= THẾ GIỚI ================= */
const WMAP=(()=>{try{if(sessionStorage.getItem('ltlc-newmap'))return true;if(!localStorage.getItem('loan-the-lanh-chua-v3'))return true;return localStorage.getItem('ltlc-map')=='2'}catch(e){return true}})();
