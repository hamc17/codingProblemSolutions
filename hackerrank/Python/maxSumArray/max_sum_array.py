# /usr/bin/python3


def get_max_nonadj_subset_val(arr):
    """Gets the maximum value of a non-adjacent sub-array
    within arr. Sub-array can be empty.

    Arguments:
        arr {list} -- The list of values.
    Returns:
        integer -- The max value of a non-adjacent sub-arry.
    """

    max_val = 0
    print(type(arr))
    print(arr)
    # As the constraint is a non-adjacent sub-array, the max
    # can either be the the current element's value, the current
    # max or the max of the element at i-2.
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
        max_val = max(max_val, (
                        arr[i] + arr[i-2] if i >= 2 else arr[i]))
        arr[i] = max_val
    return max_val
