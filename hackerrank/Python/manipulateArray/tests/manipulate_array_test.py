import json
import os

import pytest

from manipulateArray import manipulate_array

test_cases = None
with open(os.path.join(os.path.dirname(__file__), "test_input.json"), "rt") as f:
    test_cases = json.load(f)

for testcase in test_cases:
    input_file_loc = os.path.join(os.path.dirname(__file__), testcase["input"])
    output_file_loc = os.path.join(os.path.dirname(__file__), testcase["output"])
    item_count = op_count = op_array = expected = None

    with open(input_file_loc) as input_contents:
        lines = input_contents.readlines()
        item_count, op_count = map(int, lines[0].strip().split(" "))
        op_array = lines[1:]

    with open(output_file_loc) as output_contents:
        lines = output_contents.readlines()
        expected = int(lines[0].strip())

def test_manipulate_array():
    assert manipulate_array.manipulate_array(item_count, op_count, op_array) == expected
