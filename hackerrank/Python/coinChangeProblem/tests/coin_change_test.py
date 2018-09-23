import os

import pytest

from coinChangeProblem import coin_change


def get_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        n, coin_count = map(int, lines[0].strip().split(" "))
        coins = map(int, lines[1].strip().split(" "))
        case = [n, coin_count, coins]
    return case

def get_output(output_file):
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        output = int(lines[0].strip())
    return output


def test_large_amount_get_ways():
    case_input = get_input("large_amount_case_input.txt")
    case_output = get_output("large_amount_case_output.txt")
    n, coin_count, coins = case_input
    output = case_output
    assert coin_change.getWays(n, coins) == output
