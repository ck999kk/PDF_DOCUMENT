# This script generates the EVIDENCE_MANIFEST.csv file.
# It scans the current directory for PDF files, calculates their SHA256 hash,
# and records various metadata including file size, modification time, and GitHub permalinks.
#
# Input: PDF files in the current directory.
# Output: EVIDENCE_MANIFEST.csv file.

import os
import csv
import hashlib
from datetime import datetime, timezone


def sha256(path):
    """
    Calculates the SHA256 hash of a file.

    Args:
        path: The path to the file.

    Returns:
        The SHA256 hash of the file as a hexadecimal string.
    """
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1<<20), b''):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    """
    Main script to generate the EVIDENCE_MANIFEST.csv file.
    This file contains metadata for each PDF document in the repository.
    """
    rows = []
    for f in sorted(os.listdir('.')):
        if f.lower().endswith('.pdf') and os.path.isfile(f):
            rows.append({
                'filename': f,
                'size_bytes': os.path.getsize(f),
                'sha256': sha256(f),
                'modified_iso': datetime.fromtimestamp(os.path.getmtime(f), tz=timezone.utc).isoformat(),
                'permalink_blob': f"https://github.com/ck999kk/PDF_DOCUMENT/blob/main/{f}",
                'permalink_raw':  f"https://raw.githubusercontent.com/ck999kk/PDF_DOCUMENT/main/{f}",
            })

    fields = ['filename','size_bytes','sha256','modified_iso','permalink_blob','permalink_raw']
    with open('EVIDENCE_MANIFEST.csv','w',newline='',encoding='utf-8') as w:
        writer = csv.DictWriter(w, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    print(f"Wrote {len(rows)} rows to EVIDENCE_MANIFEST.csv")
