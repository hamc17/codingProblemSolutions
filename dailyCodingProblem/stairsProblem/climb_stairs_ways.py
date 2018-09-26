"""
There exists a staircase with N steps, and you can climb up
either 1 or 2 steps at a time. Given N, write a function that
returns the number of unique ways you can climb the staircase.
The order of the steps matters.
"""


def get_ways(staircase_size, steps):
    """Counts the number of ways to climb a staircase given
    the staircase step count and the number of steps allowed
    to climb at once.

    Arguments:
        stair_count {integer} -- The size of the staircase.
        steps {list} -- The number of stairs allowed to climb at
        once.

    Returns:
        integer -- The total number of possible ways to climb the stairs
        given the inputs.
    """

    ways = [0] * (staircase_size + 1)
    ways[0] = 1

    for stair in xrange(1, staircase_size + 1):
        for step in steps:
            if stair >= step:
                ways[stair] += ways[stair-step]
    return ways[-1]
