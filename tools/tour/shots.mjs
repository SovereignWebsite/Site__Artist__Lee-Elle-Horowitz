// Screenshots of this site for the guided tour: node tools/tour/shots.mjs <built _site dir> <output png dir>
// Then tools/tour/build-images.py converts them to site/tour/img/*.webp.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const [root, out] = process.argv.slice(2);
const types = { '.css': 'text/css', '.webp': 'image/webp', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml' };
const srv = http.createServer((q, r) => { let p = path.join(root, decodeURIComponent(q.url.split('?')[0])); if (fs.existsSync(p) && fs.statSync(p).isDirectory()) p = path.join(p, 'index.html');
  if (!fs.existsSync(p)) { r.statusCode = 404; return r.end(); } r.setHeader('content-type', types[path.extname(p)] || 'text/html;charset=utf-8'); r.end(fs.readFileSync(p)); });
await new Promise(ok => srv.listen(8767, ok));
const b = await chromium.launch(); fs.mkdirSync(out, { recursive: true });
const desk = [['alef', '/designs/alef-bet/'], ['conv', '/designs/conversation/'], ['tense', '/designs/three-tenses/'], ['stage', '/designs/the-stage/'], ['note', '/designs/notebook/'], ['he', '/he/designs/alef-bet/']];
let c = await b.newContext({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1, reducedMotion: 'reduce', colorScheme: 'light' }); let pg = await c.newPage();
for (const [n, u] of desk) { await pg.goto('http://localhost:8767' + u); await pg.addStyleTag({ content: '.lang-fab{display:none}' }); await pg.screenshot({ path: `${out}/${n}.png` }); }
await c.close();
c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, reducedMotion: 'reduce', colorScheme: 'light' }); pg = await c.newPage();
await pg.goto('http://localhost:8767/designs/alef-bet/'); await pg.screenshot({ path: `${out}/phone.png` });
// Each design's first phone screen, in English and Hebrew, and a close-up of the detail that makes it.
const detail = { 'alef-bet': '.wall', 'conversation': '.quick', 'three-tenses': '.panels', 'the-stage': '.bill', 'notebook': '.ex' };
c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, reducedMotion: 'reduce', colorScheme: 'light' }); pg = await c.newPage();
for (const lang of ['', '/he']) for (const s of Object.keys(detail)) {
  await pg.goto(`http://localhost:8767${lang}/designs/${s}/`); await pg.addStyleTag({ content: '.lang-fab{display:none!important}' });
  await pg.screenshot({ path: `${out}/phone-${s}${lang ? '-he' : ''}.png` });
}
await c.close();
c = await b.newContext({ viewport: { width: 1280, height: 800 }, deviceScaleFactor: 1, reducedMotion: 'reduce', colorScheme: 'light' }); pg = await c.newPage();
for (const [s, sel] of Object.entries(detail)) {
  await pg.goto(`http://localhost:8767/designs/${s}/`);
  if (s === 'conversation') await pg.click('.quick details:first-child summary');
  await pg.locator(sel).first().screenshot({ path: `${out}/detail-${s}.png` });
}
await b.close(); srv.close(); console.log('shots written to', out);
