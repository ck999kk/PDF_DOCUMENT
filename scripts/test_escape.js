// This script tests the HTML escaping function.
// It ensures that special HTML characters are correctly converted to their entity equivalents.
//
// Input: None.
// Output: "escape ok" if the test passes, otherwise an assertion error.

const assert = require('assert');

const esc = s => s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));

assert.strictEqual(esc('<script>'), '&lt;script&gt;');

console.log('escape ok');