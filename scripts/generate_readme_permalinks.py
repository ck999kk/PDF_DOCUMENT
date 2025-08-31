# This script generates the README_PERMALINKS.md file.
# It reads the EVIDENCE_MANIFEST.csv file to get information about PDF documents,
# and then generates a Markdown file with permalinks to each document on GitHub.
#
# Input: EVIDENCE_MANIFEST.csv file.
# Output: README_PERMALINKS.md file.

import csv
import os


if __name__ == "__main__":
    """
    Main script to generate the README_PERMALINKS.md file.
    This file contains permalinks for each PDF document based on EVIDENCE_MANIFEST.csv.
    """
    rows = []
    if os.path.exists('EVIDENCE_MANIFEST.csv'):
        with open('EVIDENCE_MANIFEST.csv', newline='', encoding='utf-8') as r:
            rows = list(csv.DictReader(r))

    rows.sort(key=lambda x: x['filename'])

    with open('README_PERMALINKS.md', 'w', encoding='utf-8') as w:
        w.write('# Evidence Permalinks (main)\n\n')
        w.write('> Canonical branch: `main`. Links are immutable per commit.\n\n')
        for r in rows:
            w.write(f"- **{r['filename']}**\n")
            w.write(f"  - Blob: {r['permalink_blob']}\n")
            w.write(f"  - Raw: {r['permalink_raw']}\n")
            w.write(f"  - SHA256: `{r['sha256']}`\n")

    print('README_PERMALINKS.md generated')
