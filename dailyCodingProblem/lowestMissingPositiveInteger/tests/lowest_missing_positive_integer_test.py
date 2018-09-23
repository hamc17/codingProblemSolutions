import os

import pytest

from lowestMissingPositiveInteger import lowest_missing_positive_integer


def get_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        arr = map(int, lines[0].strip().split(" "))
        case = arr
    return case


def get_output(output_file):
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        output = int(lines[0].strip())
    return output


def test_mixed_case_lowest_missing_positive_integer():
    case_input = get_input("mixed_case_input.txt")
    case_output = get_output("mixed_case_output.txt")
    arr = case_input
    output = case_output
    assert (lowest_missing_positive_integer.lowest_missing_positive_integer(
            arr) == output)


def test_positive_case_lowest_missing_positive_integer():
    case_input = get_input("positive_case_input.txt")
    case_output = get_output("positive_case_output.txt")
    arr = case_input
    output = case_output
    assert lowest_missing_positive_integer.lowest_missing_positive_integer(
        arr) == output


def test_single_neg_case_lowest_missing_positive_integer():
    case_input = get_input("single_negative_case_input.txt")
    case_output = get_output("single_negative_case_output.txt")
    arr = case_input
    output = case_output
    assert lowest_missing_positive_integer.lowest_missing_positive_integer(
        arr) == output


def test_single_pos_case_lowest_missing_positive_integer():
    case_input = get_input("single_positive_case_input.txt")
    case_output = get_output("single_positive_case_output.txt")
    arr = case_input
    output = case_output
    assert lowest_missing_positive_integer.lowest_missing_positive_integer(
        arr) == output
