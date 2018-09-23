import os

import pytest

from pairs import pairs


def get_input(input_file):
    cases = []
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        n, k = map(int, lines[0].strip().split(" "))
        arr = map(int, lines[1].strip().split(" "))
        cases.append((n, k, arr))
    return cases


def get_output(output_file):
    output = []
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        output.append(int(lines[0].strip()))
    return output


def test_large_case_pair_difference_k():
    case_input = get_input("large_case_input.txt")
    case_output = get_output("large_case_output.txt")
    n, k, arr = case_input[0]
    output = case_output[0]
    assert pairs.pairs_difference_of_k(k, arr) == output
