// เรนเดอร์ evidence/*.html เป็น PNG 1080x1920 ลงโฟลเดอร์ images/
// ใช้: node render.js [ชื่อไฟล์...]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = path.join(__dirname, 'evidence'), out = path.join(__dirname, 'images');
  fs.mkdirSync(out, { recursive: true });
  const files = process.argv.slice(2).length ? process.argv.slice(2)
    : fs.readdirSync(dir).filter(f => /^\d+_.*\.html$/.test(f)).sort();
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  for (const f of files) {
    await page.goto('file://' + path.join(dir, f), { waitUntil: 'networkidle' });
    await page.evaluate(async () => { await document.fonts.ready; for (const fr of document.querySelectorAll("iframe")) { try { await fr.contentDocument.fonts.ready; } catch (e) {} } });
    await page.waitForTimeout(800);
    const png = path.join(out, f.replace('.html', '.png'));
    await page.screenshot({ path: png });
    console.log('ok', png);
  }
  await browser.close();
})();
