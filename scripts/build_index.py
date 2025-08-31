import json, glob, os
from pdfminer.high_level import extract_text
from pdfminer.pdfpage import PDFPage

BASE="https://ck999kk.github.io/PDF_DOUCUMENT"
def pages(pdf):
    with open(pdf,"rb") as f:
        return sum(1 for _ in PDFPage.get_pages(f))
def cut(s,n=420):
    s=" ".join((s or "").split())
    return s[:n]+("…" if len(s)>n else "")
out=open("index.jsonl","w",encoding="utf-8")
for pdf in sorted(glob.glob("*.pdf")):
    try:
        n=pages(pdf)
        for i in range(1,n+1):
            txt=extract_text(pdf,page_numbers=[i-1]) or ""
            if txt.strip():
                out.write(json.dumps({
                    "file": os.path.basename(pdf),
                    "page": i,
                    "text": cut(txt),
                    "url": f"{BASE}/{os.path.basename(pdf)}#page={i}"
                }, ensure_ascii=False)+"\n")
    except Exception as e:
        print(f"[WARN] {pdf}: {e}")
out.close()
