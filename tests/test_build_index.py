import base64
import json
import subprocess
from pathlib import Path

PDF_B64 = (
    "JVBERi0xLjMKMyAwIG9iago8PC9UeXBlIC9QYWdlCi9QYXJlbnQgMSAwIFIKL1Jlc291cmNlcyAyIDAgUgovQ29udGVudHMgNCAwIFI+PgplbmRvYmoKNCAwIG9iago8PC9GaWx0ZXIgL0ZsYXRlRGVjb2RlIC9MZW5ndGggNzE+PgpzdHJlYW0KeJwzUvDiMtAzNVco53IKUdB3M1QwNNIzMFAISVNwDQEJGRvqGVoqmFua6pmbK4SkKGh4pObk5CsEuLhpKoRkgRQBAOCiDwcKZW5kc3RyZWFtCmVuZG9iagoxIDAgb2JqCjw8L1R5cGUgL1BhZ2VzCi9LaWRzIFszIDAgUiBdCi9Db3VudCAxCi9NZWRpYUJveCBbMCAwIDU5NS4yOCA4NDEuODldCj4+CmVuZG9iago1IDAgb2JqCjw8L1R5cGUgL0ZvbnQKL0Jhc2VGb250IC9IZWx2ZXRpY2EKL1N1YnR5cGUgL1R5cGUxCi9FbmNvZGluZyAvV2luQW5zaUVuY29kaW5nCj4+CmVuZG9iagoyIDAgb2JqCjw8Ci9Qcm9jU2V0IFsvUERGIC9UZXh0IC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJXQovRm9udCA8PAovRjEgNSAwIFIKPj4KL1hPYmplY3QgPDwKPj4KPj4KZW5kb2JqCjYgMCBvYmoKPDwKL1Byb2R1Y2VyIChQeUZQREYgMS43LjIgaHR0cDovL3B5ZnBkZi5nb29nbGVjb2RlLmNvbS8pCi9DcmVhdGlvbkRhdGUgKEQ6MjAyNTA4MzExMTE0NTkpCj4+CmVuZG9iago3IDAgb2JqCjw8Ci9UeXBlIC9DYXRhbG9nCi9QYWdlcyAxIDAgUgovT3BlbkFjdGlvbiBbMyAwIFIgL0ZpdEggbnVsbF0KL1BhZ2VMYXlvdXQgL09uZUNvbHVtbgo+PgplbmRvYmoKeHJlZgowIDgKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDAwMjI3IDAwMDAwIG4gCjAwMDAwMDA0MTAgMDAwMDAgbiAKMDAwMDAwMDAwOSAwMDAwMCBuIAowMDAwMDAwMDg3IDAwMDAwIG4gCjAwMDAwMDAzMTQgMDAwMDAgbiAKMDAwMDAwMDUxNCAwMDAwMCBuIAowMDAwMDAwNjIzIDAwMDAwIG4gCnRyYWlsZXIKPDwKL1NpemUgOAovUm9vdCA3IDAgUgovSW5mbyA2IDAgUgo+PgpzdGFydHhyZWYKNzI2CiUlRU9GCg=="
)


def test_build_index_outputs_expected_json(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    pdf_path.write_bytes(base64.b64decode(PDF_B64))
    repo_root = Path(__file__).resolve().parents[1]
    subprocess.run(
        ["python", str(repo_root / "scripts" / "build_index.py"), "--base-url", "http://example"],
        cwd=tmp_path,
        check=True,
    )
    lines = (tmp_path / "index.jsonl").read_text().strip().splitlines()
    assert len(lines) == 1
    record = json.loads(lines[0])
    assert record == {
        "file": "sample.pdf",
        "page": 1,
        "text": "Hello PDF",
        "url": "http://example/sample.pdf#page=1",
    }
