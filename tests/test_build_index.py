import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "build_index",
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "build_index.py",
)
build_index = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_index)


def test_cut_truncates_with_ellipsis():
    assert build_index.cut("abcdefghij", 5) == "abcde…"
