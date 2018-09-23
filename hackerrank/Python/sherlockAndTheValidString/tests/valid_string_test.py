import os

import pytest

from sherlockAndTheValidString import valid_string


def get_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        return lines[0].strip()


def get_output(output_file):
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        return lines[0].strip()


def test_is_valid_short_string():
    case_input = get_input("short_case_input.txt")
    case_output = get_output("short_case_output.txt")
    assert valid_string.is_valid(case_input) == case_output
