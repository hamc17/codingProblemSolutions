import os

import pytest

from dfsConnectedCells import connected_cells_in_grid


def get_input(input_file):
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        m = int(lines[1].strip())
        grid = [map(int, lines[2 + i].strip().split(" ")) for i in range(n)]
        case = [n, m, grid]
    return case


def get_output(output_file):
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        output = int(lines[0].strip())
    return output


def test_small_grid_connected_cells_in_grid():
    case_input = get_input("small_grid_case_input.txt")
    case_output = get_output("small_grid_case_output.txt")
    n, m, grid = case_input
    output = case_output
    assert connected_cells_in_grid.maxRegion(grid) == output


def test_larger_grid_connected_cells_in_grid():
    case_input = get_input("larger_grid_case_input.txt")
    case_output = get_output("larger_grid_case_output.txt")
    n, m, grid = case_input
    output = case_output
    assert connected_cells_in_grid.maxRegion(grid) == output
