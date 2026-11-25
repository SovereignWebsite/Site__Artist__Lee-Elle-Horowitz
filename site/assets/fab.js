// The floating language button steps aside while an enquiry button is under it, so it never covers one.
// The same switch is always in the top bar. Nothing is sent anywhere; without this script the button simply stays.
(() => {
  const fab = document.querySelector('.lang-fab'); if (!fab) return;
  const ctas = [...document.querySelectorAll('main .btn, main .cta a, main a.button')]; if (!ctas.length) return;
  const under = new Set();
  const io = new IntersectionObserver((es) => { es.forEach(e => e.isIntersecting ? under.add(e.target) : under.delete(e.target)); fab.classList.toggle('clear', under.size > 0); },
    { rootMargin: '-' + Math.max(0, innerHeight - 110) + 'px 0px 0px 0px' });
  ctas.forEach(c => io.observe(c));
})();
