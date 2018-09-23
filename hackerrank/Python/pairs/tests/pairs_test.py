import json
import os

import pytest

import pairs

test_cases = None
with open(os.path.join(os.path.dirname(__file__), "test_input.json"), "rt") as f:
    test_cases = json.load(f)

for testcase in test_cases:
    input_file_loc = os.path.join(os.path.dirname(__file__), testcase["input"])
    output_file_loc = os.path.join(os.path.dirname(__file__), testcase["output"])
    n = k = arr = expected = None

    with open(input_file_loc) as input_contents:
        lines = input_contents.readlines()
        n, k = map(int, lines[0].strip().split(" "))
        arr = map(int, lines[1].strip().split(" "))

    with open(output_file_loc) as output_contents:
        lines = output_contents.readlines()
        expected = int(lines[0].strip())

def test_pair_difference_k():
    assert (n is not None) and (k is not None) and (arr is not None) and (expected is not None)
    assert pairs.pairs_difference_of_k(k, arr) == expected
