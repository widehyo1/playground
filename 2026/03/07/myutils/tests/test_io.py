import subprocess
import sys
from pathlib import Path
import pytest

CASE_DIR = Path(__file__).parent / "cases"


def run_case(input_file):
    result = subprocess.run(
        [sys.executable, "main.py"],
        stdin=input_file.open(),
        capture_output=True,
        text=True,
    )
    return result.stdout


def normalize(s):
    return s.strip()


cases = []

for input_file in sorted(CASE_DIR.glob("input*.txt")):
    idx = input_file.stem.replace("input", "")
    output_file = CASE_DIR / f"output{idx}.txt"
    cases.append((input_file, output_file))


@pytest.mark.parametrize("input_file,output_file", cases)
def test_io(input_file, output_file):
    expected = normalize(output_file.read_text())
    actual = normalize(run_case(input_file))

    assert actual == expected
