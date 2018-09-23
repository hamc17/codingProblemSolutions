import json
import os

import pytest

from shortestBFSReach import shortest_bfs_reach

test_cases = None
with open(os.path.join(os.path.dirname(__file__), "test_input.json"), "rt") as f:
    test_cases = json.load(f)

for testcase in test_cases:
    input_file_loc = os.path.join(os.path.dirname(__file__), testcase["input"])
    output_file_loc = os.path.join(
                    os.path.dirname(__file__), testcase["output"])
    nodes = edge_count = edges = cases = None

    with open(input_file_loc) as input_contents:
        lines = input_contents.readlines()
        case_count = int(lines[0])
        cases = []
        parsed = 1
        # test cases difficult to parse but not worth refactoring originals
        for i in xrange(case_count):
            nodes, edge_count = map(int, lines[parsed].strip().split(" "))
            parsed += 1
            edges = []
            for j in xrange(edge_count):
                edges.append(map(int, lines[j + parsed].strip().split(" ")))
            parsed += edge_count
            start_val = int(lines[parsed].strip())
            parsed += 1
            cases.append([nodes, edge_count, start_val, edges])

    with open(output_file_loc) as output_contents:
        lines = output_contents.readlines()
        outputs = []
        for i in xrange(case_count):
            outputs.append(map(int, lines[i].strip().split(" ")))
    cases = zip(cases, outputs)

    def test_shortest_distance():
        for case in cases:
            g = shortest_bfs_reach.Graph(case[0][0])
            for e in xrange(case[0][1]):
                x, y = case[0][3][e]
                g.connect(x, y)
            # testcases have edge distance of 6
            assert g.find_all_distances(case[0][2], 6) == case[1]
