import json
import os

import pytest

from shortestBFSReach import shortest_bfs_reach


def get_input(input_file):
    cases = []
    with open(os.path.join(os.path.dirname(__file__), input_file), "rt") as f:
        lines = f.readlines()
        case_count = int(lines[0])
        parsed = 1
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
        return cases

def get_output(output_file):
    output = []
    with open(os.path.join(os.path.dirname(__file__), output_file), "rt") as f:
        lines = f.readlines()
        output = []
        for line in lines:
            output.append(map(int, line.strip().split(" ")))
        return output

def test_small_case():
    case_input = get_input("short_case_input.txt")
    case_output = get_output("short_case_output.txt")
    for _ in xrange(len(case_input)):
        case = case_input[_]
        nodes, edge_count, start_val, edges = case
        g = shortest_bfs_reach.Graph(nodes)
        for e in xrange(edge_count):
            g.connect(*edges[e])
        assert g.find_all_distances(start_val, 6) == case_output[_]


def test_larger_case():
    case_input = get_input("larger_case_input.txt")
    case_output = get_output("larger_case_output.txt")
    for _ in xrange(len(case_input)):
        case = case_input[_]
        nodes, edge_count, start_val, edges = case
        g = shortest_bfs_reach.Graph(nodes)
        for e in xrange(edge_count):
            g.connect(*edges[e])
        assert g.find_all_distances(start_val, 6) == case_output[_]

def test_largest_case():
    case_input = get_input("largest_case_input.txt")
    case_output = get_output("largest_case_output.txt")
    for _ in xrange(len(case_input)):
        case = case_input[_]
        nodes, edge_count, start_val, edges = case
        g = shortest_bfs_reach.Graph(nodes)
        for e in xrange(edge_count):
            g.connect(*edges[e])
        assert g.find_all_distances(start_val, 6) == case_output[_]