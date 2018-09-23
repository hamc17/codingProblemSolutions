import json
import os

import pytest

from dfsConnectedCells import connected_cells_in_grid

test_cases = None
with open(os.path.join(os.path.dirname(__file__), "test_input.json"), "rt") as f:
    test_cases = json.load(f)

for testcase in test_cases:
    input_file_loc = os.path.join(os.path.dirname(__file__), testcase["input"])
    output_file_loc = os.path.join(os.path.dirname(__file__), testcase["output"])
    n = m = grid = None

    with open(input_file_loc) as input_contents:
        lines = input_contents.readlines()
        n = int(lines[0].strip())
        m = int(lines[1].strip())
        grid = [map(int, lines[2 + i].strip().split(" ")) for i in range(n)]

    with open(output_file_loc) as output_contents:
        lines = output_contents.readlines()
        expected = int(lines[0].strip())

def test_connected_cells_in_grid():
    assert connected_cells_in_grid.maxRegion(grid) == expected
