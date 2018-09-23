#!/usr/bin/python

"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
"""

def segregate(arr):
    """Separates an array of integers into negative and positive.
    Return: 
    
    Arguments:
        arr {list} -- An array of integers.
    
    Returns:
        integer -- The index of last negative integer.
    """


    j = i = 0
    for i in xrange(len(arr)):
        if arr[i] <= 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return j

def findMissingInt(arr):
    """Iterates through the array of positive ints;
    For each x, changes the value at arr[x] to negative.
    Iterates through the array again and finds the first
    non negative int if present, else returns the length + 1

    Arguments:
        arr {list} -- An array of integers.
    
    Returns:
        integer -- The index of the first
    """

    for i in xrange(len(arr)):
        if abs(arr[i]) - 1 < len(arr) and arr[abs(arr[i]) - 1] > 0:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
    for i in xrange(len(arr)):
        if arr[i] > 0:
            return i + 1
    return len(arr) + 1

def lowest_missing_positive_integer(arr):
    """Finds the index of the lowest positive integer missing from an array.
    
    Arguments:
        arr {list} -- An array of integers.
    
    Returns:
        integer -- The index of the lowest positive integer missing.
    """

    last_neg = segregate(arr)
    return findMissingInt(arr[last_neg:])

