const assert = require('assert');
const { hit, esc } = require('../docs/search.js');

describe('search utilities', () => {
  it('escapes HTML entities', () => {
    assert.strictEqual(esc('<script>'), '&lt;script&gt;');
  });

  it('filters records case-insensitively', () => {
    const records = [
      { text: 'Hello PDF' },
      { text: 'Another file' }
    ];
    const result = records.filter(r => hit(r, 'pdf'));
    assert.deepStrictEqual(result, [{ text: 'Hello PDF' }]);
  });
});
