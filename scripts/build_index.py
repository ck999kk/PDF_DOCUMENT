"""Generate a JSONL index with searchable snippets for each PDF page.

The script scans the current directory for PDF files and produces an
``index.jsonl`` file where every line contains metadata for a single page:
the file name, page number, shortened text snippet and a link to the page on
the hosted site.
"""

import argparse
import glob
import json
import os

from pdfminer.high_level import extract_text
from pdfminer.pdfpage import PDFPage


def pages(pdf: str) -> int:
    """Return the number of pages in the given PDF file.

    Args:
        pdf: Path to the PDF file.

    Returns:
        The total count of pages contained in the PDF.
    """

    with open(pdf, "rb") as f:
        # Count each page to determine the iteration range.
        return sum(1 for _ in PDFPage.get_pages(f))


def cut(s: str, n: int) -> str:
    """Trim and shorten a string to ``n`` characters.

    Consecutive whitespace is collapsed and the result is truncated with an
    ellipsis when it exceeds ``n`` characters.

    Args:
        s: The string to normalize and cut.
        n: Maximum length of the returned string.

    Returns:
        The processed string, optionally suffixed with an ellipsis.
    """

    s = " ".join((s or "").split())
    return s[:n] + ("…" if len(s) > n else "")


def main() -> None:
    """Build ``index.jsonl`` with metadata for each page in every PDF.

    The function parses command-line arguments, iterates over discovered PDF
    files, extracts text snippets from each page and writes a JSON object per
    line to ``index.jsonl``.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-url",
        default="https://ck999kk.github.io/PDF_DOUCUMENT",
        help="Base URL for generated links.",
    )
    parser.add_argument(
        "--snippet-length",
        type=int,
        default=420,
        help="Maximum number of characters per text snippet.",
    )
    args = parser.parse_args()

    with open("index.jsonl", "w", encoding="utf-8") as out:
        for pdf in sorted(glob.glob("*.pdf")):
            try:
                n = pages(pdf)  # Determine how many pages the PDF contains.
                for i in range(1, n + 1):
                    # Extract text for the current page and normalize it.
                    txt = extract_text(pdf, page_numbers=[i - 1]) or ""
                    if txt.strip():
                        # Write metadata and snippet as a single JSON line.
                        out.write(
                            json.dumps(
                                {
                                    "file": os.path.basename(pdf),
                                    "page": i,
                                    "text": cut(txt, args.snippet_length),
                                    "url": f"{args.base_url}/{os.path.basename(pdf)}#page={i}",
                                },
                                ensure_ascii=False,
                            )
                            + "\n"
                        )
            except Exception as e:
                print(f"[WARN] {pdf}: {e}")


if __name__ == "__main__":
    main()
