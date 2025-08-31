const test = require('node:test');
const assert = require('node:assert/strict');

const esc = s => s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));

test('escapes HTML special characters', () => {
  assert.strictEqual(esc('<script>'), '&lt;script&gt;');
});
