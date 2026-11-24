// Thiên Kiếm Môn: lưu tài nguyên (model, texture, thư viện) trong máy để lần sau vào nhanh.
const C='tkm-v1';
self.addEventListener('install',()=>self.skipWaiting());
self.addEventListener('activate',e=>e.waitUntil(self.clients.claim()));
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET'||r.headers.has('range'))return;const u=new URL(r.url);
 if(u.origin!==location.origin||!u.pathname.startsWith('/thienkiemmon/'))return;if(r.mode==='navigate'||u.pathname.endsWith('.html')||u.pathname.endsWith('/'))return;
 e.respondWith(caches.open(C).then(async c=>{const hit=await c.match(r);const net=fetch(r).then(res=>{if(res.ok&&res.type==='basic')c.put(r,res.clone()).catch(()=>{});return res});if(hit){e.waitUntil(net.catch(()=>{}));return hit}return net}))});
