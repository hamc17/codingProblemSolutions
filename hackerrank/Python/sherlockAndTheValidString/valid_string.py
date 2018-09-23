from collections import Counter


"""Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
"""


def is_valid(s):
    """Checks if all characters in a string appear the same number of times, or all characters appear the same number of times if 1 character is removed at 1 index.
    
    Arguments:
        s {string} -- A string of characters.
    
    Returns:
        string -- Either 'YES' or 'NO'
    """

    if len(s) == 1 or not len(s):
        return "YES"
    counts = Counter(s)
    counts_counts = Counter([counts[k] for k in counts.keys()])
    if len(counts_counts.keys()) == 1:
        return "YES"
    if len(counts_counts.keys()) > 2:
        return "NO"
    keys = counts_counts.keys()
    larger_key = max(keys)
    smaller_key = min(keys)
    if counts_counts[larger_key] == 1:
        diff = abs(keys[0] - keys[1])
        if diff != 1:
            return "NO"
        return "YES"
    if counts_counts[smaller_key] == 1 and smaller_key == 1:
        return "YES"
    return "NO"
