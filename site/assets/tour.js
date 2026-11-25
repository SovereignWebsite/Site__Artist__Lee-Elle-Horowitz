// Guided tour: move between slides with the arrow keys (left / right, up / down, Page Up / Page Down, Home / End).
// The arrows on each slide are plain links, so the slides work without this script too. Nothing is sent anywhere.
(() => {
  const slides = [...document.querySelectorAll('.slide')];
  if (!slides.length) return;
  const current = () => { let best = 0, bestD = Infinity; slides.forEach((s, i) => { const d = Math.abs(s.getBoundingClientRect().top - 60); if (d < bestD) { bestD = d; best = i; } }); return best; };
  let idx = 0, moving = 0, lastGo = 0;
  const fromHash = slides.findIndex(s => '#' + s.id === location.hash); if (fromHash >= 0) idx = fromHash;
  addEventListener('scroll', () => { clearTimeout(moving); moving = setTimeout(() => { moving = 0; if (Date.now() - lastGo > 900) idx = current(); }, 150); }, { passive: true });
  const go = (i) => { i = Math.max(0, Math.min(slides.length - 1, i)); idx = i; lastGo = Date.now(); slides[i].scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' }); history.replaceState(null, '', '#' + slides[i].id); };
  document.addEventListener('keydown', (e) => {
    if (e.altKey || e.ctrlKey || e.metaKey || /input|textarea|select/i.test(e.target.tagName)) return;
    const k = e.key, i = (moving || Date.now() - lastGo < 900) ? idx : current();
    if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || (k === ' ' && !e.shiftKey)) { e.preventDefault(); go(i + 1); }
    else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp' || (k === ' ' && e.shiftKey)) { e.preventDefault(); go(i - 1); }
    else if (k === 'Home') { e.preventDefault(); go(0); } else if (k === 'End') { e.preventDefault(); go(slides.length - 1); }
  });
  document.addEventListener('click', (e) => { const a = e.target.closest('.s-nav a'); if (!a) return; e.preventDefault(); go(slides.findIndex(s => '#' + s.id === a.getAttribute('href'))); });
})();
