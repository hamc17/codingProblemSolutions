import os

import pytest

from maxSumArray import max_sum_array


def get_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        n = list(map(int, lines[0].strip().split(" ")))
        arr = list(map(int, lines[1].strip().split(" ")))
        case = [n, arr]
    return case


def get_output(output_file):
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        output = int(lines[0].strip())
    return output


def test_small_case_get_max_nonadj_subset_val():
    case_input = get_input("small_case_input.txt")
    case_output = get_output("small_case_output.txt")
    n, arr = case_input
    output = case_output
    assert max_sum_array.get_max_nonadj_subset_val(arr) == output


def test_small_case2_get_max_nonadj_subset_val():
    case_input = get_input("small_case2_input.txt")
    case_output = get_output("small_case2_output.txt")
    n, arr = case_input
    output = case_output
    assert max_sum_array.get_max_nonadj_subset_val(arr) == output


def test_small_with_neg_case_get_max_nonadj_subset_val():
    case_input = get_input("small_with_neg_case_input.txt")
    case_output = get_output("small_with_neg_case_output.txt")
    n, arr = case_input
    output = case_output
    assert max_sum_array.get_max_nonadj_subset_val(arr) == output


def test_small_case_get_max_nonadj_subset_val():
    case_input = get_input("large_case_input.txt")
    case_output = get_output("large_case_output.txt")
    n, arr = case_input
    output = case_output
    assert max_sum_array.get_max_nonadj_subset_val(arr) == output
