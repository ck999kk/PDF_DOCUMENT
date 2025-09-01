const test = require('node:test');
const assert = require('node:assert/strict');

const { esc } = require('../docs/search.js');

test('escapes HTML characters', () => {
  assert.strictEqual(esc('<script>'), '&lt;script&gt;');
});

