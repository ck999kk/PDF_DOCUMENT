# Repository usage

This repository stores evidence PDFs alongside plain‑text extracts.
The text files live in the [`_text/`](./_text) directory and enable
search for both humans and downstream AI tools.

## Quick search from the command line

```bash
python search.py "water damage"
```

The script prints one matching line per file and is case‑insensitive.
Use `-n` to limit the number of results:

```bash
python search.py "rent" -n 5
```

## Browser search interface

Open [`docs/index.html`](./docs/index.html) in a web browser to perform
client‑side searches with a graphical interface.

## Updating the index

When new PDFs are added:

1. Run [`make_pdfs_searchable.sh`](./make_pdfs_searchable.sh) to OCR any
   files lacking a text layer.
2. Run [`setup_search_pages.sh`](./setup_search_pages.sh) to rebuild the
   text extracts and search index.

These steps keep the repository fully accessible for humans and AI
systems.
