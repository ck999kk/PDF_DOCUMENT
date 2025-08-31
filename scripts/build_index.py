import json, glob, os, subprocess
from pdfminer.high_level import extract_text
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams

TEXT_DIR="_text"
BASE="https://ck999kk.github.io/PDF_DOUCUMENT"
def pages(pdf):
    with open(pdf,"rb") as f: return sum(1 for _ in PDFPage.get_pages(f))
def cut(s,n=420):
    s=" ".join((s or "").split())
    return s[:n]+("…" if len(s)>n else "")

def page_text(pdf,i):
    lap=LAParams()
    txt=extract_text(pdf,page_numbers=[i-1],codec="utf-8",laparams=lap) or ""
    if txt.count("(cid:")>2:
        base=os.path.splitext(os.path.basename(pdf))[0]+".txt"
        sidecar=os.path.join(TEXT_DIR,base)
        if not os.path.exists(sidecar):
            os.makedirs(TEXT_DIR,exist_ok=True)
            tmp=pdf+".ocr.pdf"
            try:
                subprocess.run(["ocrmypdf","--sidecar",sidecar,pdf,tmp],
                               check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
            except Exception as e:
                print(f"[WARN] OCR failed for {pdf}: {e}")
            finally:
                if os.path.exists(tmp): os.remove(tmp)
        if os.path.exists(sidecar):
            with open(sidecar,encoding="utf-8") as f:
                pages=f.read().split("\f")
                if 0<=i-1<len(pages): txt=pages[i-1]
    return txt

out=open("index.jsonl","w",encoding="utf-8")
for pdf in sorted(glob.glob("*.pdf")):
    try:
        n=pages(pdf)
        for i in range(1,n+1):
            txt=page_text(pdf,i)
            if txt.strip():
                out.write(json.dumps({"file":os.path.basename(pdf),"page":i,"text":cut(txt),
                                      "url":f"{BASE}/{os.path.basename(pdf)}#page={i}"},
                                     ensure_ascii=False)+"\n")
    except Exception as e:
        print(f"[WARN] {pdf}: {e}")
out.close()
