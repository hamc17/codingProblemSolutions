"""
   Problem:
   "Starting with a 1-indexed array of zeros and a list of operations,
    for each operation add the given value to each of the array elements
    between the two given indices, inclusive.
    Once all operations have been performed, return the maximum value in your
    array."
"""


def manipulate_array(item_count, op_count, op_array):
    """Performs the addition operations specified in
    op_array on an array of size item_count

    Arguments:
        item_count {integer} -- The number of items in the array.
        op_count {integer} -- The number of operations to perform.
        op_array {list} -- The array of operations.

    Returns:
        integer -- The maximum value after all operations have been
        perormed.
    """

    max_val = 0
    value_array = [0] * (item_count + 1)
    total = 0
    for op in op_array:
        first, last, incr = map(int, op.strip().split(" "))
        value_array[first-1] += incr
        value_array[last] -= incr

    for val in value_array:
        total += val
        max_val = (total if total > max_val else max_val)

    return max_val
