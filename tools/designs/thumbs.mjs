// Screenshots of each design, in each language, for the "Choose a design" cards:
//   node tools/designs/thumbs.mjs <built _site dir> <png dir>   then   python3 tools/designs/thumbs.py <png dir>
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const [root, out] = process.argv.slice(2);
const site = JSON.parse(fs.readFileSync('site/data/content/site.json', 'utf8'));
const types = { '.css': 'text/css', '.webp': 'image/webp', '.jpg': 'image/jpeg' };
const srv = http.createServer((q, r) => { let p = path.join(root, decodeURIComponent(q.url.split('?')[0])); if (fs.existsSync(p) && fs.statSync(p).isDirectory()) p = path.join(p, 'index.html');
  if (!fs.existsSync(p)) { r.statusCode = 404; return r.end(); } r.setHeader('content-type', types[path.extname(p)] || 'text/html;charset=utf-8'); r.end(fs.readFileSync(p)); });
await new Promise(ok => srv.listen(8773, ok)); fs.mkdirSync(out, { recursive: true });
const b = await chromium.launch(); const pg = await (await b.newContext({ viewport: { width: 1280, height: 800 }, reducedMotion: 'reduce', colorScheme: 'light' })).newPage();
for (const lang of ['en', 'he']) for (const s of site.designs) {
  await pg.goto(`http://localhost:8773${lang === 'he' ? '/he' : ''}/designs/${s}/`);
  await pg.addStyleTag({ content: '.switch,.lang-fab,.family-credit{display:none!important}' });
  await pg.screenshot({ path: `${out}/${s}.${lang}.png` });
}
await b.close(); srv.close(); console.log('thumbs written to', out);
