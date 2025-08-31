# PDF Document Archive

This repository collects PDF documents and provides a minimal search experience over their contents.  It is intended as an easily browsable archive with a searchable index.

## Directory structure

- `docs/` – Static web user interface for searching the index (`index.html`, `search.js`).
- `scripts/` – Utilities such as `build_index.py` for generating the search index.
- `*.pdf` – Source PDF files stored at the repository root.
- `_text/` – Plain‑text exports corresponding to each PDF.

## Installation

Python 3 is required.  Install dependencies with:

```bash
pip install -r requirements.txt
```

## Building the index

Generate or refresh `index.jsonl` from the PDFs:

```bash
python scripts/build_index.py
```

Run this whenever PDFs change to keep the search results up to date.

## Running the web UI

Serve the `docs/` directory and open it in a browser to search the archive.  For example:

```bash
python -m http.server -d docs
```

Then visit http://localhost:8000/ to access the search page.
