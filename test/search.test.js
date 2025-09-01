const test = require('node:test');
const assert = require('node:assert/strict');
const { JSDOM } = require('jsdom');

test('search renders results', async () => {
  const dom = new JSDOM(`<!DOCTYPE html><input id="q" /><div id="res"></div>`);
  global.window = dom.window;
  global.document = dom.window.document;
  global.fetch = async () => ({
    text: async () => `{"text":"Hello World","url":"u","file":"f.pdf","page":1}\n`
  });

  require('../docs/search.js');

  await new Promise(r => setTimeout(r));

  const q = dom.window.document.getElementById('q');
  q.value = 'hello';
  q.dispatchEvent(new dom.window.Event('input'));

  assert.match(dom.window.document.getElementById('res').innerHTML, /Hello World/);
});
