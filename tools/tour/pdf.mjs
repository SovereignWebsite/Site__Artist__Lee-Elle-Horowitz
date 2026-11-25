// Print each tour deck to a PDF, one 1280 x 720 slide per page: node tools/tour/pdf.mjs <built _site dir>
// Writes site/tour/<deck>.pdf (and the same into _site/tour/). Run after the site is built.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const root = process.argv[2];
const tour = JSON.parse(fs.readFileSync('site/data/content/tour.json', 'utf8'));
const types = { '.css': 'text/css', '.webp': 'image/webp', '.jpg': 'image/jpeg' };
const srv = http.createServer((q, r) => { let p = path.join(root, decodeURIComponent(q.url.split('?')[0])); if (fs.existsSync(p) && fs.statSync(p).isDirectory()) p = path.join(p, 'index.html');
  if (!fs.existsSync(p)) { r.statusCode = 404; return r.end(); } r.setHeader('content-type', types[path.extname(p)] || 'text/html;charset=utf-8'); r.end(fs.readFileSync(p)); });
await new Promise(ok => srv.listen(8768, ok));
const b = await chromium.launch(); const pg = await (await b.newContext({ viewport: { width: 1280, height: 720 } })).newPage();
for (const d of tour.decks) {
  await pg.goto(`http://localhost:8768/tour/${d.id}/`, { waitUntil: 'networkidle' });
  await pg.evaluate(() => Promise.all([...document.images].map(i => { i.loading = 'eager'; return i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }); })));
  await pg.emulateMedia({ media: 'print' });
  const pdf = await pg.pdf({ width: '1280px', height: '720px', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  fs.writeFileSync(`site/tour/${d.pdf_name}`, pdf); fs.writeFileSync(path.join(root, 'tour', d.pdf_name), pdf); console.log(d.pdf_name, pdf.length, 'bytes');
}
await b.close(); srv.close();
