// usage: node render.js <timeline.json> <cast.json> <out.mp4> [stillTimes,comma]
const { chromium } = require('playwright');
const { spawn } = require('child_process'); const fs = require('fs'); const path = require('path');
(async () => {
  const [tlF, castF, out, stills] = process.argv.slice(2);
  const tl = JSON.parse(fs.readFileSync(tlF)), cast = JSON.parse(fs.readFileSync(castF));
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + path.resolve(__dirname, 'engine.html')); await p.evaluate(() => document.fonts.ready);
  await p.evaluate(([a, c]) => window.setup(a, c), [tl, cast]);
  await p.evaluate(() => { const c = document.createElement('canvas'); const x = c.getContext('2d'); x.font = '800 40px Kanit'; x.fillText('ก', 0, 0); });
  await p.waitForTimeout(300);
  if (stills) { let i = 0; for (const T of stills.split(',').map(Number)) { await p.evaluate(T => window.render(T), T); const d = await p.evaluate(() => window.grab(.85)); fs.writeFileSync(`${out}_${i++}.jpg`, Buffer.from(d.split(',')[1], 'base64')); } await b.close(); return; }
  const fps = 30, N = Math.round(tl.total * fps);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = 0; f < N; f++) {
    const d = await p.evaluate(T => { window.render(T); return window.grab(.9); }, f / fps);
    if (!ff.stdin.write(Buffer.from(d.split(',')[1], 'base64'))) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 300 === 0) console.log('frame', f, '/', N);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close();
})();
