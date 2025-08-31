import argparse
import glob
import json
import os

from pdfminer.high_level import extract_text
from pdfminer.pdfpage import PDFPage


def pages(pdf: str) -> int:
    with open(pdf, "rb") as f:
        return sum(1 for _ in PDFPage.get_pages(f))


def cut(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s[:n] + ("…" if len(s) > n else "")


def main() -> None:
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
                n = pages(pdf)
                for i in range(1, n + 1):
                    txt = extract_text(pdf, page_numbers=[i - 1]) or ""
                    if txt.strip():
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
