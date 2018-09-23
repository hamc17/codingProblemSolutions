import os

import pytest

from journeyToTheMoon import journey_to_the_moon


def get_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        n, p = map(int, lines[0].strip().split(" "))
        astronauts = [map(
            int, lines[i].strip().split(" ")) for i in xrange(1, p+1)]
        case = [n, p, astronauts]
    return case


def get_output(output_file):
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        expected = int(lines[0].strip())
        output = expected
    return output


def test_large_case_journey_to_the_moon():
    case_input = get_input("large_case_input.txt")
    case_output = get_output("large_case_output.txt")
    n, p, astronauts = case_input
    output = case_output
    assert journey_to_the_moon.get_pairs(n, astronauts) == output


def test_short_case_journey_to_the_moon():
    case_input = get_input("short_case_input.txt")
    case_output = get_output("short_case_output.txt")
    n, p, astronauts = case_input
    output = case_output
    assert journey_to_the_moon.get_pairs(n, astronauts) == output
