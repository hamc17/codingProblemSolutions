import json
import os

import pytest

from coinChangeProblem import coin_change

test_cases = None
with open(os.path.join(os.path.dirname(__file__), "test_input.json"), "rt") as f:
    test_cases = json.load(f)

for testcase in test_cases:
    input_file_loc = os.path.join(os.path.dirname(__file__), testcase["input"])
    output_file_loc = os.path.join(os.path.dirname(__file__), testcase["output"])
    n = coin_count = coins = None

    with open(input_file_loc) as input_contents:
        lines = input_contents.readlines()
        n, coin_count = map(int, lines[0].strip().split(" "))
        coins = map(int, lines[1].strip().split(" "))

    with open(output_file_loc) as output_contents:
        lines = output_contents.readlines()
        expected = int(lines[0].strip())

def test_get_ways():
    assert coin_change.getWays(n, coins) == expected
