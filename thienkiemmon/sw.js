// Thiên Kiếm Môn: lưu tài nguyên (model, texture, thư viện) trong máy để lần sau vào nhanh.
const C='tkm-v1';
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||r.headers.has('range'))return;const u=new URL(r.url);
 if(u.origin!==location.origin||!u.pathname.startsWith('/thienkiemmon/'))return;if(r.mode==='navigate'||u.pathname.endsWith('.html')||u.pathname.endsWith('/'))return;
 e.respondWith(caches.open(C).then(async c=>{const hit=await c.match(r);const net=fetch(r).then(res=>{if(res.ok&&res.type==='basic')c.put(r,res.clone()).catch(()=>{});return res});if(hit){e.waitUntil(net.catch(()=>{}));return hit}return net}))});

// Tải ngầm (Background Fetch trên Chrome Android): vẫn tải khi người chơi chuyển app / tắt màn hình.
async function bfStore(reg){const c=await caches.open(C);const recs=await reg.matchAll();await Promise.all(recs.map(async r=>{try{const res=await r.responseReady;if(res&&res.ok)await c.put(r.request.url,res)}catch(_){}}))}
self.addEventListener('backgroundfetchsuccess',e=>e.waitUntil((async()=>{await bfStore(e.registration);try{await e.updateUI({title:'Huyền Kiếm Tiên Đồ: đã tải xong ✓'})}catch(_){}for(const cl of await self.clients.matchAll())cl.postMessage({t:'warm',done:1,total:1})})()));
self.addEventListener('backgroundfetchfail',e=>e.waitUntil(bfStore(e.registration)));
self.addEventListener('backgroundfetchclick',e=>e.waitUntil(self.clients.openWindow('/thienkiemmon/')));
// Dự phòng: tự tải trước trong service worker (6 luồng) khi trình duyệt không có Background Fetch
let warming=null;self.addEventListener('message',e=>{if(!e.data||e.data.t!=='warm'||warming)return;warming=(async()=>{const c=await caches.open(C);let list=[];try{list=await(await fetch('/thienkiemmon/preload.json',{cache:'no-store'})).json()}catch(_){return}
 let done=0,i=0;const tell=async()=>{for(const cl of await self.clients.matchAll())cl.postMessage({t:'warm',done,total:list.length})};
 const one=async()=>{while(i<list.length){const u=list[i++];try{if(!(await c.match(u))){const r=await fetch(u);if(r.ok)await c.put(u,r)}}catch(_){}done++;if(done%15===0||done===list.length)tell()}};
 await Promise.all([one(),one(),one(),one()])})();e.waitUntil(warming)});
