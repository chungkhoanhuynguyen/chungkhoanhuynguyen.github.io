// QL1 11/11 – quy trình đăng YouTube Studio qua Claude in Chrome (dán từng khối bằng javascript_tool; CSP chặn eval).
// 0) Mở https://studio.youtube.com/channel/<ID>/videos/upload?d=ud ; chia video: split -b 8500000 -d KEY.mp4 /mnt/user-data/uploads/hn_chunks/<lô>/KEY_p
// 1) Dán khối HELPER dưới đây, find "HNCHUNK" -> file_upload từng khối KEY_pNN (mỗi lần 1 file <10MB)
// 2) await __up('KEY')  (ghép khối, điền tiêu đề/mô tả từ main_1111.json / kenh5.json, chọn "không dành cho trẻ em")
//    video dài: file_upload bìa vào input "Hình thu nhỏ" (find 'thumbnail file input')
// 3) await __sch(ngày,'HH:MM') ; 4) await __done() – CHỈ bấm Lên lịch khi ngày/giờ đúng như __sch đặt (11/11: 1 Short bị đăng lịch mặc định vì lịch chưa hiện kịp).
// LỊCH CHƯA HIỆN: __sch thử lại tối đa 8 lần; trả 'KHONG THAY NGAY' thì làm lại, KHÔNG gọi __done.
// HELPER:
window.__parts={};
let i=document.createElement('input');i.type='file';i.id='hnc';i.setAttribute('aria-label','HNCHUNK');i.style.cssText='position:fixed;top:0;left:0;width:20px;height:20px;z-index:99999';document.body.appendChild(i);
i.onchange=()=>{for(const f of i.files) window.__parts[f.name]=f;};
window.__up=async(key,meta='main_1111.json')=>{const S=ms=>new Promise(r=>setTimeout(r,ms));
 const ks=Object.keys(window.__parts).filter(k=>k.startsWith(key+'_p')).sort();
 const f=new File(ks.map(k=>window.__parts[k]),key+'.mp4',{type:'video/mp4'});
 const inp=document.querySelector('ytcp-uploads-dialog input[type=file]'); const dt=new DataTransfer(); dt.items.add(f); inp.files=dt.files; inp.dispatchEvent(new Event('change',{bubbles:true}));
 await S(6000);
 const M=await fetch('https://api.github.com/repos/chungkhoanhuynguyen/chungkhoanhuynguyen.github.io/contents/_video/yt/'+meta,{headers:{Accept:'application/vnd.github.raw'},cache:'no-store'}).then(r=>r.json());
 const m=M[key]; const tb=[...document.querySelectorAll('ytcp-uploads-dialog #textbox')];
 const setT=(el,t)=>{el.focus();document.execCommand('selectAll',false,null);document.execCommand('insertText',false,t);el.dispatchEvent(new Event('input',{bubbles:true}));};
 setT(tb[0],m.t); setT(tb[1],m.d.replaceAll('{LINK}',window.__LINK||''));
 await S(800); document.querySelector('ytcp-uploads-dialog tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').click();
 return [ks, f.size, tb[0].innerText];};
window.__sch=async(day,hh)=>{const S=ms=>new Promise(r=>setTimeout(r,ms));
 for(let k=0;k<3;k++){document.querySelector('ytcp-uploads-dialog #next-button').click(); await S(2000);}
 const link=[...document.querySelectorAll('ytcp-uploads-dialog a')].map(x=>x.href).filter(h=>/youtu\.be|shorts/.test(h))[0];
 document.querySelector('ytcp-uploads-dialog #second-container-expand-button').click(); await S(1200);
 document.querySelector('ytcp-uploads-dialog #datepicker-trigger').click(); await S(1200);
 let c=null;
 for(let t=0;t<8 && !c;t++){ if(t%3==0){document.querySelector('ytcp-uploads-dialog #datepicker-trigger').click();} await S(800);
   c=[...document.querySelectorAll('ytcp-scrollable-calendar .calendar-day')].filter(x=>!x.className.includes('invisible') && !x.className.includes('disabled') && x.innerText.trim()===String(day))[0]; }
 if(!c) return 'KHONG THAY NGAY';
 c.click(); await S(1000);
 const ti=document.querySelector('ytcp-uploads-dialog #time-of-day-container input'); ti.click(); await S(1200);
 const its=[...document.querySelectorAll('tp-yt-paper-item')].filter(x=>x.innerText.trim()===hh); const it=its.find(x=>x.offsetParent)||its[0]; if(it){it.scrollIntoView(); it.click();} await S(800);
 window.__want=[day+' thg 11, 2026',hh];   // sửa 'thg 11' theo tháng
 return [link, document.querySelector('ytcp-uploads-dialog #datepicker-trigger').innerText, ti.value];};
window.__done=async()=>{const S=ms=>new Promise(r=>setTimeout(r,ms));
 const d=document.querySelector('ytcp-uploads-dialog #datepicker-trigger').innerText, h=document.querySelector('ytcp-uploads-dialog #time-of-day-container input').value;
 if(!window.__want || d!==window.__want[0] || h!==window.__want[1]) return 'SAI LICH, KHONG BAM: '+d+' '+h;
 document.querySelector('ytcp-uploads-dialog #done-button').click(); await S(3500);
 const ok=[...document.querySelectorAll('ytcp-button, tp-yt-paper-button, button')].find(b=>b.innerText.trim()==='Đã hiểu' && b.offsetParent); if(ok){ok.click(); await S(3000);}
 window.__want=null; return document.body.innerText.match(/công khai vào lúc [^\n]{0,30}/)?.[0];};
// Kênh @5 (UCbeiGmJ1yZL4kLE5bwf471g): nếu Studio báo "Rất tiếc" -> youtube.com/account -> chọn kênh "Vĩ Mô Nóng" rồi mở lại.
