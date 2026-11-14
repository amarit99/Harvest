// เรนเดอร์ evidence/**/*.html เป็น PNG 1080x1920 ลงโฟลเดอร์ images/ (โครงโฟลเดอร์เดียวกัน)
// ใช้: node render.js                       -> ทุกไฟล์ในโฟลเดอร์ evidence/ ชั้นบนสุด
//      node render.js ep02                  -> ทุกไฟล์ในโฟลเดอร์ evidence/ep02
//      node render.js ep02/04_er.html?s=2   -> ไฟล์เดียวพร้อมพารามิเตอร์ (ได้ images/ep02/04_er_s2.png)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.join(__dirname, 'evidence'), out = path.join(__dirname, 'images');
  let args = process.argv.slice(2);
  const list = (sub) => fs.readdirSync(path.join(dir, sub)).filter(f => /^\d+_.*\.html$/.test(f)).sort().map(f => path.join(sub, f));
  let jobs = [];
  if (!args.length) jobs = list('');
  for (const a of args) {
    if (fs.existsSync(path.join(dir, a)) && fs.statSync(path.join(dir, a)).isDirectory()) jobs.push(...list(a));
    else jobs.push(a);
  }
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const j of jobs) {
    const [f, q] = j.split('?');
    await page.goto('file://' + path.join(dir, f) + (q ? '?' + q : ''), { waitUntil: 'networkidle' });
    await page.evaluate(async () => { await document.fonts.ready; for (const fr of document.querySelectorAll('iframe')) { try { await fr.contentDocument.fonts.ready; } catch (e) {} } });
    await page.waitForTimeout(800);
    const suffix = q ? '_' + q.replace(/[=&]/g, '') : '';
    const png = path.join(out, f.replace('.html', suffix + '.png'));
    fs.mkdirSync(path.dirname(png), { recursive: true });
    await page.screenshot({ path: png });
    console.log('ok', path.relative(__dirname, png));
  }
  await browser.close();
})();
