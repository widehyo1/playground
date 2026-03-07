import io
import sys
from pathlib import Path
import pytest

from main import main

CASE_DIR = Path(__file__).parent / "cases"


def run_case(input_text, capsys):
    sys.stdin = io.StringIO(input_text)
    main()
    return capsys.readouterr().out


def normalize(s):
    return s.strip()


cases = []

for input_file in sorted(CASE_DIR.glob("input*.txt")):
    idx = input_file.stem.replace("input", "")
    output_file = CASE_DIR / f"output{idx}.txt"
    cases.append((input_file, output_file))


@pytest.mark.parametrize("input_file,output_file", cases)
def test_io(input_file, output_file, capsys):
    actual = normalize(run_case(input_file.read_text(), capsys))
    expected = normalize(output_file.read_text())

    assert actual == expected

