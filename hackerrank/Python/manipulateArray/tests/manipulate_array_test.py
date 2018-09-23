import os

import pytest

from manipulateArray import manipulate_array


def get_input(input_file):
    cases = []
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        item_count, op_count = map(int, lines[0].strip().split(" "))
        op_array = lines[1:]
        cases.append((item_count, op_count, op_array))
    return cases


def get_output(output_file):
    output = []
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        expected = int(lines[0].strip())
        output.append(expected)
    return output


def test_large_case_manipulate_array():
    case_input = get_input("large_case_input.txt")
    case_output = get_output("large_case_output.txt")
    for _ in xrange(len(case_input)):
        case = case_input[_]
        item_count, op_count, op_array = case
        output = case_output[_]
    assert manipulate_array.manipulate_array(
        item_count, op_count, op_array) == output
