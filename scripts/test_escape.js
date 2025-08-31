const assert = require('assert');
const { esc } = require('../docs/search.js');

assert.strictEqual(esc('<script>'), '&lt;script&gt;');

console.log('escape ok');
