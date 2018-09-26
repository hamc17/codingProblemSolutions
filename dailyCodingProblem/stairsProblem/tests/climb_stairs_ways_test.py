import os

import pytest

from stairsProblem import climb_stairs_ways


def get_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        stair_count = int(lines[0].strip())
        steps = map(int, lines[1].strip().split(" "))
        case = [stair_count, steps]
    return case


def get_output(output_file):
    output = []
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        output = int(lines[0].strip())
    return output


def test_small_case():
    case_input = get_input("short_case_input.txt")
    case_output = get_output("short_case_output.txt")
    stair_count = case_input[0]
    steps = case_input[1]
    output = case_output
    assert climb_stairs_ways.get_ways(stair_count, steps) == output


def test_larger_case():
    case_input = get_input("larger_case_input.txt")
    case_output = get_output("larger_case_output.txt")
    stair_count = case_input[0]
    steps = case_input[1]
    output = case_output
    assert climb_stairs_ways.get_ways(stair_count, steps) == output
