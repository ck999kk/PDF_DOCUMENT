const assert = require('assert');

const esc = s => s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

assert.strictEqual(esc('<script>'), '&lt;script&gt;');

console.log('escape ok');
