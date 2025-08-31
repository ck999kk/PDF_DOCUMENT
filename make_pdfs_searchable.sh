#!/usr/bin/env bash
set -euo pipefail
shopt -s nullglob
# ต้องติดตั้ง ocrmypdf ไว้แล้ว

for f in *.pdf; do
  if ! ocrmypdf --version >/dev/null 2>&1; then
    echo "Install ocrmypdf first (brew install ocrmypdf)"; exit 1
  fi
  # ตรวจว่ามี text layer ไหม: ถ้าไม่มีจะมีคำว่า "no text"
  if pdffonts "$f" 2>/dev/null | grep -qi "no fonts\|no text"; then
    tmp="ocr_$f"
    ocrmypdf --skip-text "$f" "$tmp"
    mv "$tmp" "$f"
    echo "OCR done: $f"
  else
    echo "Has text: $f"
  fi
done
