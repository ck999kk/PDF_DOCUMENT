// Helper function: load a JSON lines file and parse each line into an object.
async function load(url) {
  const response = await fetch(url);
  const text = await response.text();
  return text
    .split('\n')
    .filter(Boolean)
    .map(JSON.parse);
}

// Helper function: determine if a record's text contains the query string.
function hit(record, query) {
  query = query.toLowerCase();
  return record.text.toLowerCase().includes(query);
}

// Helper function: escape HTML entities to keep rendered text safe.
function esc(s) {
  return s.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
}

// Export esc so Node scripts can reuse it without duplication.
if (typeof module !== 'undefined') {
  module.exports = { esc };
}

// Only execute DOM-related logic when running in a browser.
if (typeof window !== 'undefined') {
  (async () => {
    const data = await load('../index.jsonl');
    const q = document.getElementById('q');
    const res = document.getElementById('res');

    function render(list) {
      res.innerHTML = list
        .slice(0, 200)
        .map(
          r =>
            `<div><a href="${r.url}" target="_blank">${r.file}</a> — p.${r.page}<br>${esc(r.text)}</div><hr>`
        )
        .join('');
    }

    // Event listener: update results as the user types in the search box.
    q.addEventListener('input', () => {
      const v = q.value.trim();
      if (!v) {
        res.innerHTML = '';
        return;
      }
      render(data.filter(r => hit(r, v)));
    });
  })();
}
