"""
There exists a staircase with N steps, and you can climb up
either 1 or 2 steps at a time. Given N, write a function that
returns the number of unique ways you can climb the staircase.
The order of the steps matters.
"""


def get_ways(stair_count, steps):
    ways = [0] * (stair_count + 1)
    ways[0] = 1

    for stair in xrange(1, stair_count + 1):
        for step in steps:
            if stair >= step:
                ways[stair] += ways[stair-step]
    return ways[-1]
