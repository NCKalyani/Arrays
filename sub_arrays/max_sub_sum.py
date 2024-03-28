import math


def max_subarray(a: list) -> int:
    """ Returns maximum sub_array sum"""
    lst_max = 0
    largest = -math.inf
    for i in range(len(a)):
        lst_max += a[i]
        if largest < lst_max:
            largest = lst_max
            print(largest)
        if lst_max < 0:
            lst_max = 0

    return largest


def sum_sub_arrays(a: list) -> int:
    """Returns sum of all individual sub arrays"""
    total = 0
    for i in range(len(a)):
        presence = (i + 1) * (len(a) - i)
        contribution = presence * a[i]
        total += contribution
    return total
