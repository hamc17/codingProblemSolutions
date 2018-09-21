"""
Given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.
"""

def pairDiffK(k, arr):
    """Given an array of integers, gets the total number of pairs
        with a distance of k.
    
    Arguments:
        k {integer} -- The target difference value.
        arr {list} -- An array of integers.
    
    Returns:
        integer -- The total number of pairs whose difference
        is equal to k.
    """

    match_dict = {}
    count = 0
    for i in arr:
        if k <= i:
            # if k is smaller or equal to i, the matching
            # integer can either be smaller or greater than i
            diffs = [abs(k - i), k+i]
        else:
            diffs = [k+i]
        for dif in diffs:
            if match_dict.get(dif, False):
                count += 1
            else:
                match_dict[i] = True
    return count