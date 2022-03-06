import pathlib

# import pytest

from xxp._ref import xxd
from xxp import format

BIN_FILE_DIR = pathlib.Path(__file__).parent / "files"


def get_file_contents(name: str) -> bytes:
    path = BIN_FILE_DIR / (name + ".bin")
    with open(path, mode="rb") as f:
        data = f.read()
    return data


def test_basic():
    data = get_file_contents("0thru255")
    ref_output = xxd(data)
    xxp_output = format(data)

    assert ref_output == xxp_output
