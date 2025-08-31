#!/usr/bin/env bash
set -euo pipefail

# 0) ตรวจเครื่องมือพื้นฐาน
need() { command -v "$1" >/dev/null 2>&1 || { echo "Missing: $1"; exit 1; }; }
need git
need shasum
need awk
if ! command -v pdftotext >/dev/null 2>&1; then
  echo "Installing poppler (pdftotext/pdffonts) is required. On macOS: brew install poppler"; exit 1
fi

# 1) Normalize line endings + กัน CRLF
cat > .gitattributes <<'G'
* text=auto eol=lf
*.pdf -text
G

# 2) สร้างโฟลเดอร์ข้อความและดัชนี
mkdir -p _text
: > index.jsonl

# 3) แปลง PDF -> TXT แบบปลอดภัยต่อไฟล์ที่มี text อยู่แล้ว
#    ใช้ pdftotext สำหรับทำดัชนี (ไม่แก้ไฟล์ PDF ต้นฉบับ)
pdf_count=0
for f in *.pdf; do
  [ -e "$f" ] || continue
  pdf_count=$((pdf_count+1))
  base="${f%.*}"
  txt="_text/${base}.txt"
  # แปลงเป็นข้อความ
  pdftotext "$f" "$txt" || { echo "pdftotext failed: $f"; continue; }
  # เก็บเมตาดาต้า
  size=$(stat -f%z "$f" 2>/dev/null || stat -c%s "$f")
  sha=$(shasum -a 256 "$f" | awk '{print $1}')
  pages=$(pdfinfo "$f" 2>/dev/null | awk -F': *' '/Pages/{print $2; exit}'); pages=${pages:-0}
  title=$(pdfinfo "$f" 2>/dev/null | awk -F': *' '/Title/{sub(/"/,""); print $2; exit}')
  # ตัดข้อความตัวอย่างเล็กน้อยสำหรับพรีวิว
  preview=$(tr '\n' ' ' < "$txt" | awk '{print substr($0,1,400)}')
  jq -c --arg file "$f" \
        --arg sha "$sha" \
        --arg size "$size" \
        --arg pages "$pages" \
        --arg title "${title:-}" \
        --arg preview "$preview" \
        '{file:$file, sha256:$sha, size:($size|tonumber), pages:($pages|tonumber), title:$title, preview:$preview}' \
        <<< '{}' >> index.jsonl 2>/dev/null || {
    # fallback ไม่มี jq: เขียน JSONL แบบง่าย
    printf '{"file":"%s","sha256":"%s","size":%s,"pages":%s,"title":"%s","preview":"%s"}\n' \
      "$f" "$sha" "${size:-0}" "${pages:-0}" "${title//\"/\\\"}" "${preview//\"/\\\"}" >> index.jsonl
  }
done

# 4) หน้าเว็บค้นหาแบบสแตติก (ไม่พึ่ง build tools)
mkdir -p docs
cat > docs/index.html <<'H'
<!doctype html><meta charset="utf-8">
<title>PDF_DOUCUMENT — Search</title>
<style>body{font-family:system-ui,Arial,sans-serif;max-width:900px;margin:40px auto;padding:0 12px}
input{width:100%;padding:10px;font-size:16px} .hit{padding:10px 0;border-bottom:1px solid #eee}
.small{color:#555;font-size:12px;}</style>
<h1>Repository Search</h1>
<input id="q" placeholder="Type to search filename/title/text preview...">
<div id="out"></div>
<script>
async function load() {
  const res = await fetch('../index.jsonl').then(r=>r.text());
  const rows = res.trim().split(/\n/).map(l=>{try{return JSON.parse(l)}catch(e){return null}}).filter(Boolean);
  const q = document.getElementById('q'), out = document.getElementById('out');
  const esc = s => (s||'').replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
  function render(list){
    out.innerHTML = list.slice(0,200).map(r=>`
      <div class="hit">
        <a href="../${encodeURIComponent(r.file)}" target="_blank">${esc(r.file)}</a>
        ${r.title?`<div class="small">Title: ${esc(r.title)}</div>`:''}
        <div class="small">SHA-256: ${r.sha256.slice(0,16)}… · pages: ${r.pages} · size: ${r.size} bytes</div>
        <div>${esc(r.preview).slice(0,300)}</div>
      </div>`).join('');
  }
  render(rows);
  q.addEventListener('input', ()=>{
    const k = q.value.toLowerCase();
    const filtered = rows.filter(r =>
      r.file.toLowerCase().includes(k) ||
      (r.title||'').toLowerCase().includes(k) ||
      (r.preview||'').toLowerCase().includes(k)
    );
    render(filtered);
  });
}
load();
</script>
H

# 5) GitHub Pages with Actions (deploy docs/ เป็น Pages)
mkdir -p .github/workflows
cat > .github/workflows/pages.yml <<'Y'
name: deploy-pages
on:
  push:
    branches: [ "main" ]
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: "pages"
  cancel-in-progress: true
jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: docs
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
Y

# 6) Commit & push
git add .gitattributes _text index.jsonl docs .github/workflows/pages.yml
git commit -m "Add searchable index + static search page + Pages workflow"
git push origin main

echo
echo "Done. After workflow finishes, open the Pages URL shown in the Actions logs."
