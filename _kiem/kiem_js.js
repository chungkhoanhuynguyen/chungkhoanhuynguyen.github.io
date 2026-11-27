// Kiểm lỗi JavaScript bằng Playwright không đầu (rd_kiem_js_2511, NV2 27/11/2026)
// Dùng: node _kiem/kiem_js.js [gốc, mặc định http://localhost:8765]
// LỖI khi: pageerror, console error cùng miền, còn chữ "Đang tải" sau khi chờ, hoặc ô dữ liệu chính rỗng.
const { chromium } = require('playwright');
const GOC = process.argv[2] || 'http://localhost:8765';
const TRANG = [
  ['/', ['#hnbar, header', 'body']],
  ['/dinh-gia-co-phieu.html', ['table']],
  ['/ma/VNM.html', ['body']],
  ['/the-gioi-hang-hoa.html', ['table, canvas, svg']],
  ['/mo-tai-khoan-chung-khoan.html', ['main, article, body']],
];
const NGOAI = /googlesyndication|google-analytics|googletagmanager|doubleclick|posthog|adtrafficquality|fundingchoices|gstatic|youtube|ERR_|Failed to load resource|Content Security Policy|favicon/i;
(async () => {
  const t0 = Date.now(); const b = await chromium.launch(); let loi = 0; const ra = [];
  for (const w of [390, 1440]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } });
    // chặn quảng cáo/đo lường để kết quả ổn định
    await ctx.route(/googlesyndication|google-analytics|googletagmanager|doubleclick|posthog|adtrafficquality/, r => r.abort());
    for (const [duong, chon] of TRANG) {
      const p = await ctx.newPage(); const err = [];
      p.on('pageerror', e => err.push('pageerror: ' + e.message.slice(0, 160)));
      p.on('console', m => { if (m.type() === 'error' && !NGOAI.test(m.text())) err.push('console: ' + m.text().slice(0, 160)); });
      try { await p.goto(GOC + duong, { waitUntil: 'load', timeout: 45000 }); } catch (e) { err.push('tai trang: ' + e.message.slice(0, 120)); }
      // cuộn hết trang để các khối tải-khi-gần (IntersectionObserver) chạy
      await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 200)); } scrollTo(0, 0); }).catch(() => {});
      await p.waitForTimeout(4000);
      const kq = await p.evaluate((chon) => {
        const thieu = chon.filter(s => { const el = document.querySelector(s); return !el || (el.innerText || '').trim().length + el.querySelectorAll('canvas,svg,img').length === 0; });
        const dangTai = [...document.querySelectorAll('td,div,span,p')].filter(e => e.children.length === 0 && /^\s*(Đang tải|Loading)/i.test(e.textContent) && e.offsetParent).length;
        const rongBang = [...document.querySelectorAll('table')].filter(t => t.offsetParent && t.querySelectorAll('tbody tr').length === 0 && t.querySelectorAll('tr').length <= 1).length;
        return { thieu, dangTai, rongBang, chu: document.body.innerText.length };
      }, chon).catch(e => ({ thieu: ['evaluate'], dangTai: 0, rongBang: 0, chu: 0 }));
      if (kq.thieu.length) err.push('o du lieu rong: ' + kq.thieu.join(','));
      if (kq.dangTai) err.push('con "Dang tai": ' + kq.dangTai);
      if (kq.chu < 300) err.push('trang qua it chu: ' + kq.chu);
      ra.push(`${w}px ${duong}: ${err.length ? 'LOI ' + err.length : 'OK'} (bang rong ${kq.rongBang})`);
      err.forEach(e => ra.push('   - ' + e)); loi += err.length; await p.close();
    }
    await ctx.close();
  }
  await b.close();
  console.log(ra.join('\n')); console.log(`Tong loi JS/du lieu: ${loi} · ${((Date.now() - t0) / 1000).toFixed(1)} giay`);
  process.exit(loi ? 1 : 0);
})();
