// up3.js (QL1 12/11/2026) – TẢI VIDEO LÊN YOUTUBE KHÔNG CẦN CHUNK: trình duyệt tự lấy mp4 + bìa + meta thẳng từ GitHub (nhánh video-out).
// Dùng: 1) chuyển kênh (youtube.com/channel_switcher → bấm kênh → mở studio.youtube.com/ kiểm tên kênh)
//       2) mở studio.youtube.com/channel/<ID>/videos/upload?d=ud  3) dán file này vào javascript_tool
//       4) __U('<LÔ>','<KEY>') → đợi __st có 'READY'  5) __sch(ngày,'19:00') → đợi __st2 có 'SCHED'  6) __done(ngày,'19:00')
// An toàn: tự DỪNG nếu mp4 < 2MB / bìa < 50KB / thiếu mốc chương (tránh tạo bản nháp hỏng).
window.__st=[];window.__st2=[];
window.__U=async(batch,key)=>{const S=ms=>new Promise(r=>setTimeout(r,ms));const L=m=>window.__st.push(m);try{
 const G='https://api.github.com/repos/chungkhoanhuynguyen/chungkhoanhuynguyen.github.io/contents/';const raw={headers:{Accept:'application/vnd.github.raw'},cache:'no-store'};
 const M=(await fetch(G+'_video/queue/'+batch+'/meta.json',raw).then(r=>r.json()))[key];
 const ch=await fetch(G+batch+'/'+key+'_chuong.txt?ref=video-out',raw).then(r=>r.text());
 const vb=await fetch(G+batch+'/'+key+'.mp4?ref=video-out',raw).then(r=>r.blob());L('mp4 '+vb.size);
 const bb=await fetch(G+batch+'/'+key+'_bia.png?ref=video-out',raw).then(r=>r.blob());L('bia '+bb.size);
 if(vb.size<2e6||bb.size<5e4||!/^0:00/.test(ch.trim())){L('ERR file thieu, DUNG');return;}
 const D=()=>document.querySelector('ytcp-uploads-dialog');const inp=D().querySelector('input[type=file]');
 let dt=new DataTransfer();dt.items.add(new File([vb],key+'.mp4',{type:'video/mp4'}));inp.files=dt.files;inp.dispatchEvent(new Event('change',{bubbles:true}));
 for(let i=0;i<40&&D().querySelectorAll('#textbox').length<2;i++)await S(500);await S(2500);
 const tb=[...D().querySelectorAll('#textbox')];const setT=(el,t)=>{el.focus();document.execCommand('selectAll',false,null);document.execCommand('insertText',false,t);el.dispatchEvent(new Event('input',{bubbles:true}));};
 setT(tb[0],M.title.slice(0,100));await S(400);setT(tb[1],M.mo_ta.replace('{CHUONG}',ch.trim()));await S(800);L('title '+tb[0].innerText.length+' desc '+tb[1].innerText.length);
 const ti=[...D().querySelectorAll('input[type=file]')].find(x=>/image/.test(x.accept||''));
 if(ti){dt=new DataTransfer();dt.items.add(new File([bb],key+'_bia.png',{type:'image/png'}));ti.files=dt.files;ti.dispatchEvent(new Event('change',{bubbles:true}));await S(4000);L('thumb set');}else L('NO THUMB INPUT (kenh chua xac minh?)');
 D().querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').click();await S(500);
 const b=[...D().querySelectorAll('ytcp-button,button')].find(x=>/Hiện thêm/.test(x.innerText));if(b){b.click();await S(1800);}
 const bar=D().querySelector('ytcp-chip-bar');
 if(bar){for(let k=0;k<40;k++){const x=bar.querySelector('ytcp-chip #delete-icon, ytcp-chip yt-icon');if(!x)break;x.click();await S(80);}
  const q=bar.querySelector('#text-input');q.focus();q.value=M.tags.join(',')+',';q.dispatchEvent(new Event('input',{bubbles:true}));await S(500);q.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',keyCode:13,bubbles:true}));await S(500);q.blur();L('tags '+bar.querySelectorAll('ytcp-chip').length);}else L('NO TAG BAR');
 L('READY');}catch(e){L('ERR '+e.message)}};
window.__sch=async(day,hh)=>{const S=ms=>new Promise(r=>setTimeout(r,ms));const L=m=>window.__st2.push(m);try{const D=document.querySelector('ytcp-uploads-dialog');
 for(let k=0;k<3;k++){D.querySelector('#next-button').click();await S(2000);}
 L([...D.querySelectorAll('a')].map(x=>x.href).filter(h=>/youtu\.be|shorts/.test(h))[0]);
 D.querySelector('#second-container-expand-button').click();await S(1200);let c=null;
 for(let t=0;t<8&&!c;t++){if(t%3==0)D.querySelector('#datepicker-trigger').click();await S(800);
  c=[...document.querySelectorAll('ytcp-scrollable-calendar .calendar-day')].filter(x=>!x.className.includes('invisible')&&!x.className.includes('disabled')&&x.innerText.trim()===String(day))[0];}
 if(!c){L('KHONG THAY NGAY');return;}c.click();await S(1000);
 const ti=D.querySelector('#time-of-day-container input');ti.click();await S(1200);
 const its=[...document.querySelectorAll('tp-yt-paper-item')].filter(x=>x.innerText.trim()===hh);const it=its.find(x=>x.offsetParent)||its[0];if(it){it.scrollIntoView();it.click();}await S(800);
 L(D.querySelector('#datepicker-trigger').innerText+' | '+ti.value);L('SCHED');}catch(e){L('ERR '+e.message)}};
window.__done=async(day,hh,thg='thg 11, 2026')=>{const S=ms=>new Promise(r=>setTimeout(r,ms));const D=document.querySelector('ytcp-uploads-dialog');
 const d=D.querySelector('#datepicker-trigger').innerText,h=D.querySelector('#time-of-day-container input').value;
 if(d!==day+' '+thg||h!==hh)return 'SAI LICH, KHONG BAM: '+d+' '+h;
 for(let i=0;i<25&&/Đang tải lên/.test(D.innerText);i++)await S(1000);
 D.querySelector('#done-button').click();await S(5000);
 const t=document.body.innerText.match(/[^\n]*(Đã lên lịch|công khai vào)[^\n]{0,60}/)?.[0];
 const ok=[...document.querySelectorAll('ytcp-button,button')].find(b=>/Đã hiểu|Đóng/.test(b.innerText.trim())&&b.offsetParent);if(ok)ok.click();return t;};
