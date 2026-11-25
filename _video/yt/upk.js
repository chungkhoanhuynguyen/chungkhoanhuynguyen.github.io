// upk.js (QL1 25/11/2026) – ĐĂNG SHORTS KÊNH PHỤ THEO LỊCH _video/yt/kp_lich_2611_3112.json, MỖI LỆNH 1 SHORT.
// Dùng: 1) Studio đang ở ĐÚNG kênh phụ (đọc "Kênh của bạn\n<tên>"), trang bất kỳ của studio.youtube.com
//       2) dán nguyên file này vào javascript_tool (Studio CSP chặn eval)
//       3) await __KP(i)  → trả 'OK <ngày giờ> <link>' hoặc 'ERR ...'. i = chỉ số dòng trong kp_lich (0..287).
//       4) Ghi i đã xong vào kho chi_dao kp_lich_2611 (trường xong_<kênh>), KHÔNG đăng lại i đã có.
// An toàn: kiểm tên kênh khớp ten_kenh của dòng i; mp4 < 300KB thì dừng; lịch sai thì KHÔNG bấm Lên lịch.
window.__KP=async(i)=>{const S=ms=>new Promise(r=>setTimeout(r,ms));
  const P=window.__P||(window.__P=await fetch('https://raw.githubusercontent.com/chungkhoanhuynguyen/chungkhoanhuynguyen.github.io/main/_video/yt/kp_lich_2611_3112.json',{cache:'no-store'}).then(r=>r.json()));
 const p=P[i];if(!p)return 'ERR khong co dong '+i;
 const ten=(document.body.innerText.match(/Kênh của bạn\n([^\n]+)/)||[])[1]||'';
 if(ten.trim()!==p.ten_kenh)return 'ERR SAI KENH: dang o "'+ten+'", can "'+p.ten_kenh+'"';
 const vb=await fetch(p.url).then(r=>r.blob());if(vb.size<3e5)return 'ERR mp4 '+vb.size;
 for(let k=0;k<3;k++){const c=[...document.querySelectorAll('ytcp-button,button')].find(x=>/^Đóng$/.test(x.innerText.trim())&&x.offsetParent);if(!c)break;c.click();await S(1200);}
 let D=document.querySelector('ytcp-uploads-dialog');
 if(!D||!D.offsetParent){(document.querySelector('#upload-icon')||[...document.querySelectorAll('ytcp-button,button')].find(x=>x.offsetParent&&x.innerText.trim()==='Tạo'))?.click();await S(1500);
  const up=[...document.querySelectorAll('tp-yt-paper-item')].find(x=>/Tải video lên/.test(x.innerText));if(up)up.click();await S(2000);D=document.querySelector('ytcp-uploads-dialog');}
 let inp=D&&D.querySelector('input[type=file]');
 if(!inp){location.href=location.pathname.split('/').slice(0,3).join('/')+'/videos/upload?d=ud';return 'ERR mo hop thoai tai len that bai – trang da tai lai, dan lai upk.js roi chay tiep tu '+i;}const dt=new DataTransfer();dt.items.add(new File([vb],p.key+'.mp4',{type:'video/mp4'}));inp.files=dt.files;inp.dispatchEvent(new Event('change',{bubbles:true}));
 for(let k=0;k<40&&D.querySelectorAll('#textbox').length<2;k++)await S(500);await S(2000);
 const tb=[...D.querySelectorAll('#textbox')];const setT=(el,t)=>{el.focus();document.execCommand('selectAll');document.execCommand('insertText',false,t);el.dispatchEvent(new Event('input',{bubbles:true}));};
 setT(tb[0],p.title.slice(0,100));await S(400);setT(tb[1],p.mo_ta);await S(600);
 D.querySelector('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]').click();await S(400);
 const b=[...D.querySelectorAll('ytcp-button,button')].find(x=>/Hiện thêm/.test(x.innerText));if(b){b.click();await S(1500);}
 const al=D.querySelector('tp-yt-paper-radio-button[name="VIDEO_HAS_ALTERED_CONTENT_NO"]');if(al)al.click();await S(400);
 for(let k=0;k<3;k++){D.querySelector('#next-button').click();await S(1800);}
 const link=[...D.querySelectorAll('a')].map(x=>x.href).find(h=>/youtu\.be|shorts/.test(h))||'';
 D.querySelector('#second-container-expand-button')?.click();await S(1200);
 const [y,m,d]=p.ngay.split('-').map(Number);const want=d+' thg '+m+', '+y;
 for(let t=0;t<4&&D.querySelector('#datepicker-trigger').innerText.trim()!==want;t++){D.querySelector('#datepicker-trigger').click();await S(1200);
  const di=[...document.querySelectorAll('ytcp-date-picker input, tp-yt-paper-dialog input')].find(x=>x.offsetParent&&/thg/.test(x.value));
  if(di){di.focus();di.select();document.execCommand('insertText',false,want);await S(300);di.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',keyCode:13,bubbles:true}));await S(1200);}}
 const ti=D.querySelector('#time-of-day-container input');ti.click();await S(1200);
 const its=[...document.querySelectorAll('tp-yt-paper-item')].filter(x=>x.innerText.trim()===p.gio);const it=its.find(x=>x.offsetParent)||its[0];if(it){it.scrollIntoView();it.click();}await S(800);
 const got=D.querySelector('#datepicker-trigger').innerText.trim(),gh=ti.value;
 if(got!==want||gh!==p.gio)return 'ERR SAI LICH '+got+' '+gh+' (can '+want+' '+p.gio+') – hop thoai con mo, sua tay roi bam Len lich';
 for(let k=0;k<30&&/Đang tải lên/.test(D.innerText);k++)await S(1000);
 D.querySelector('#done-button').click();await S(4000);
 const ok=[...document.querySelectorAll('ytcp-button,button')].find(x=>/Đã hiểu/.test(x.innerText.trim())&&x.offsetParent);if(ok){ok.click();await S(2500);}
 const t=(document.body.innerText.match(/công khai vào[^\n]{0,40}/)||[''])[0];const lk=(document.body.innerText.match(/https:\/\/youtube\.com\/shorts\/\S+/)||[''])[0];
 for(let k=0;k<8;k++){const cl=[...document.querySelectorAll('ytcp-button,button')].find(x=>/^Đóng$/.test(x.innerText.trim())&&x.offsetParent);if(cl){cl.click();break;}await S(1000);}
 return 'OK '+i+' '+p.kenh+' '+want+' '+p.gio+' '+(lk||link)+' '+t;};
'upk ready';
