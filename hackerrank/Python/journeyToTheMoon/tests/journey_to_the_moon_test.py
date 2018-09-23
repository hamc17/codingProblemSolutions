import json
import os

import pytest

from journeyToTheMoon import journey_to_the_moon

test_cases = None
with open(os.path.join(os.path.dirname(__file__), "test_input.json"), "rt") as f:
    test_cases = json.load(f)

for testcase in test_cases:
    input_file_loc = os.path.join(os.path.dirname(__file__), testcase["input"])
    output_file_loc = os.path.join(os.path.dirname(__file__), testcase["output"])
    n = p = astronauts = None

    with open(input_file_loc) as input_contents:
        lines = input_contents.readlines()
        n, p = map(int, lines[0].strip().split(" "))
        astronauts = [map(int, lines[i].strip().split(" ")) for i in xrange(1, p+1)]

    with open(output_file_loc) as output_contents:
        lines = output_contents.readlines()
        expected = int(lines[0].strip())

def test_journey_to_the_moon():
    assert journey_to_the_moon.get_pairs(n, astronauts) == expected
