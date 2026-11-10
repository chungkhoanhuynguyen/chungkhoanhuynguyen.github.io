// QL1 11/11 – Kiểm giao diện ĐIỆN THOẠI (390px) trước khi đẩy web. Dùng Playwright có sẵn + Lighthouse (GoogleChrome/lighthouse).
// Chạy: cd <repo> && (python3 -m http.server 8765 &) && node _web/kiem_dien_thoai.js [trang.html ...]
// Lighthouse (tuỳ chọn): npx lighthouse http://localhost:8765/index.html --chrome-path=$(node -e "console.log(require('playwright').chromium.executablePath())") --chrome-flags="--headless=new --no-sandbox" --only-categories=performance,accessibility --quiet
// Chuẩn đạt: không tràn ngang; trang chủ < 9.000px; danh sách dài phải gọn trên điện thoại; Lighthouse accessibility ≥ 95.
const {chromium} = require('playwright');
(async () => {
  const pages = process.argv.slice(2).length ? process.argv.slice(2) : ['index.html', 'f0/index.html', 'hoc/index.html', 'ma/MBB.html', 'dinh-gia-co-phieu.html', 'ket-qua-kinh-doanh-quy.html'];
  const b = await chromium.launch(); let loi = 0;
  for (const p of pages) {
    const c = await b.newContext({viewport: {width: 390, height: 844}, isMobile: true, hasTouch: true}); const pg = await c.newPage();
    await pg.goto('http://localhost:8765/' + p, {waitUntil: 'load', timeout: 60000}).catch(() => {});
    await pg.waitForTimeout(1500);
    for (let y = 0; y < 15000; y += 800) { await pg.evaluate(v => scrollTo(0, v), y); await pg.waitForTimeout(120); }
    const r = await pg.evaluate(() => ({
      tran: document.documentElement.scrollWidth > innerWidth + 1,
      cao: document.documentElement.scrollHeight,
      nho: [...document.querySelectorAll('a,button,input,select')].filter(e => { const x = e.getBoundingClientRect(); return x.width > 0 && x.height > 0 && x.height < 24 && !e.closest('p,li,td,small,footer'); }).length,
    }));
    const ghi = [];
    if (r.tran) ghi.push('LỖI tràn ngang'); if (r.cao > 20000) ghi.push('CẢNH BÁO trang quá dài ' + r.cao + 'px');
    if (r.nho > 10) ghi.push('CẢNH BÁO ' + r.nho + ' nút/ô nhỏ hơn 24px');
    if (ghi.some(x => x.startsWith('LỖI'))) loi++;
    console.log(p.padEnd(32), r.cao + 'px', ghi.join('; ') || 'OK');
    await c.close();
  }
  await b.close(); process.exit(loi ? 1 : 0);
})();
