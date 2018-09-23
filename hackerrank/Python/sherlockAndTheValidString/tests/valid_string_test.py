import json
import os

import pytest

from sherlockAndTheValidString import valid_string

test_cases = None
with open(os.path.join(os.path.dirname(__file__), "test_input.json"), "rt") as f:
    test_cases = json.load(f)

for testcase in test_cases:
    input_file_loc = os.path.join(os.path.dirname(__file__), testcase["input"])
    output_file_loc = os.path.join(os.path.dirname(__file__), testcase["output"])
    s = None

    with open(input_file_loc) as input_contents:
        lines = input_contents.readlines()
        s = lines[0].strip()

    with open(output_file_loc) as output_contents:
        lines = output_contents.readlines()
        expected = lines[0].strip()

def test_is_valid():
    assert valid_string.is_valid(s) == expected
