// Accessibility (axe) on every page at phone width (390 px), light and dark; tools/check.sh runs axe at desktop width only.
// Run from a folder with @axe-core/playwright and playwright installed (see tools/check.sh): node axe-phone.mjs <built _site dir>
import { chromium } from 'playwright'; import AxeBuilder from '@axe-core/playwright';
import http from 'node:http'; import fs from 'node:fs'; import path from 'node:path';
const root=process.argv[2]; const types={'.css':'text/css','.webp':'image/webp'};
const srv=http.createServer((q,r)=>{let p=path.join(root,decodeURIComponent(q.url.split('?')[0]));if(fs.existsSync(p)&&fs.statSync(p).isDirectory())p=path.join(p,'index.html');if(!fs.existsSync(p)){r.statusCode=404;return r.end()}r.setHeader('content-type',types[path.extname(p)]||'text/html;charset=utf-8');r.end(fs.readFileSync(p))});
await new Promise(o=>srv.listen(8772,o)); const b=await chromium.launch(); let bad=0;
const pages=['/','/he/',...['alef-bet','conversation','three-tenses','the-stage','notebook'].flatMap(s=>[`/designs/${s}/`,`/he/designs/${s}/`]),'/designs/','/he/designs/','/start/','/admin/','/tour/','/tour/your-site/','/tour/behind-the-scenes/'];
for (const sch of ['light','dark']) for (const u of pages) { const c=await b.newContext({viewport:{width:390,height:844},colorScheme:sch}); const pg=await c.newPage(); await pg.goto('http://localhost:8772'+u); await pg.waitForTimeout(1800);
 const res=await new AxeBuilder({page:pg}).analyze(); for (const v of res.violations){bad++;console.log(sch,u,v.id,v.impact,v.nodes.length,v.nodes.map(n=>n.target.join(' ')+' '+(n.any[0]?.message||'')).join(' | '))} await c.close(); }
console.log('phone axe problems:',bad); await b.close(); srv.close(); if (bad) process.exitCode=1;
