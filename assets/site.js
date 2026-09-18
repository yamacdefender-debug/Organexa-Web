(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#navigation');
  const mobile = window.matchMedia('(max-width: 760px)');
  const close = () => { toggle.setAttribute('aria-expanded', 'false'); nav.classList.remove('is-open'); };
  toggle.hidden = false;
  nav.classList.add('enhanced');
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  nav.addEventListener('click', event => { if (event.target.closest('a')) close(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') { close(); toggle.focus(); }
  });
  mobile.addEventListener('change', close);
  const email = window.ORGANEXA_CONFIG?.supportEmail?.trim();
  if (email && /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(email)) {
    document.querySelectorAll('[data-support-email]').forEach(link => {
      link.href = 'mailto:' + email;
      // Keep the CTA label and icon; update only links displaying the address.
      if (!link.classList.contains('button')) link.textContent = email;
    });
  }
})();
