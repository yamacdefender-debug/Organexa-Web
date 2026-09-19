const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const source = fs.readFileSync('assets/site.js', 'utf8');
const run = async (code, hostname, fetchImpl) => {
  const scripts = [];
  const phoneLinks = [{ classList: { contains: () => false } }];
  const slots = [{
    link: { isConnected: true },
    querySelector() { return this.link; },
    appendChild(link) { this.link = link; }
  }];
  const value = { textContent: '' };
  const counter = { hidden: true, querySelector: () => value };
  const toggle = { hidden: true, setAttribute() {}, addEventListener() {}, getAttribute: () => 'false' };
  const nav = { classList: { add() {}, remove() {}, toggle() {} }, addEventListener() {} };
  const document = {
    head: { appendChild: script => scripts.push(script) },
    querySelector: selector => ({ '.menu-toggle': toggle, '#navigation': nav, '[data-visitor-count]': counter })[selector] || null,
    querySelectorAll: selector => ({ '[data-contact-phone]': phoneLinks, '[data-phone-slot]': slots })[selector] || [],
    createElement: () => ({ dataset: {} }),
    addEventListener() {}
  };
  let requests = 0;
  const context = {
    document,
    window: {
      location: { hostname },
      matchMedia: () => ({ addEventListener() {} }),
      ORGANEXA_CONFIG: {
        contactPhone: { display: '0543 461 5884', uri: 'tel:+905434615884' },
        goatcounterCode: code
      }
    },
    fetch: async url => { requests++; return fetchImpl(url); }
  };
  vm.runInNewContext(source, context);
  await new Promise(resolve => setImmediate(resolve));
  return { scripts, phoneLinks, slots, counter, value, requests };
};

(async () => {
  const off = await run('', 'organexa.com.tr', async () => { throw Error('unexpected'); });
  assert.equal(off.scripts.length, 0);
  assert.equal(off.requests, 0);
  assert.equal(off.counter.hidden, true);
  assert.equal(off.phoneLinks[0].href, 'tel:+905434615884');
  assert.equal(off.slots[0].link.href, 'tel:+905434615884');

  const local = await run('demo', 'localhost', async () => { throw Error('unexpected'); });
  assert.equal(local.scripts.length, 0);
  assert.equal(local.requests, 0);

  const live = await run('demo', 'organexa.com.tr', async url => {
    assert.equal(url, 'https://demo.goatcounter.com/counter/TOTAL.json');
    return { ok: true, json: async () => ({ count: '12,458' }) };
  });
  assert.equal(live.scripts.length, 1);
  assert.equal(live.scripts[0].dataset.goatcounter, 'https://demo.goatcounter.com/count');
  assert.equal(live.requests, 1);
  assert.equal(live.value.textContent, '12,458');
  assert.equal(live.counter.hidden, false);

  const failed = await run('demo', 'organexa.com.tr', async () => { throw Error('offline'); });
  assert.equal(failed.counter.hidden, true);
  console.log('SITE SMOKE TEST: PASS');
})().catch(error => { console.error(error); process.exitCode = 1; });
