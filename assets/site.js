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
  const phone = window.ORGANEXA_CONFIG?.contactPhone;
  if (phone?.uri && /^tel:\+[1-9]\d{6,14}$/.test(phone.uri) && phone.display) {
    document.querySelectorAll('[data-contact-phone]').forEach(link => {
      link.href = phone.uri;
      link.textContent = phone.display;
    });
    document.querySelectorAll('[data-phone-slot]').forEach(slot => {
      const link = document.createElement('a');
      link.href = phone.uri;
      link.textContent = phone.display;
      slot.appendChild(link);
    });
  }

  const code = window.ORGANEXA_CONFIG?.goatcounterCode?.trim();
  if (!code || !/^[a-z0-9][a-z0-9-]*$/i.test(code)) return;
  if (['localhost', '127.0.0.1', '::1'].includes(window.location.hostname)) return;
  const origin = `https://${code}.goatcounter.com`;
  if (!document.querySelector('script[data-goatcounter]')) {
    const script = document.createElement('script');
    script.src = 'https://gc.zgo.at/count.js';
    script.async = true;
    script.dataset.goatcounter = `${origin}/count`;
    document.head.appendChild(script);
  }

  const counter = document.querySelector('[data-visitor-count]');
  if (!counter) return;
  fetch(`${origin}/counter/TOTAL.json`)
    .then(response => { if (!response.ok) throw new Error('Counter unavailable'); return response.json(); })
    .then(data => {
      if (typeof data.count !== 'string' || !/^[\d.,\s]+$/.test(data.count)) return;
      counter.querySelector('[data-visitor-value]').textContent = data.count;
      counter.hidden = false;
    })
    .catch(() => {});
})();
