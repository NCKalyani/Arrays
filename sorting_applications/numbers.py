import functools


def arithmetic_progression(a: list) -> int:
    """Returns true when the diff of successive elements in the sorted array is same """
    a.sort()
    print(a)
    n = len(a) - 1
    diff = a[1] - a[0]
    print(diff)
    for i in range(1, n):
        if a[i + 1] - a[i] != diff:
            return -1
    return 1


def largest_number(a: list) -> str:
    """Returns largest number which is formed by elements in the given list"""
    if list(set(a)) == 0:
        return '0'

    def comparator(c: int, b: int):
        """Sorts the two elements"""
        c = str(c)
        b = str(b)
        x = int(c + b)
        y = int(b + c)
        if x > y:
            return -1
        elif y > x:
            return 1
        else:
            return 0

    a = sorted(a, key=functools.cmp_to_key(comparator))
    return ''.join([str(i) for i in a])


def min_cost(a: list) -> int:
    """Returns minimum cost to remove all elements from the list , Note: we are reducing cost by removing largest
    element"""
    a.sort(reverse=True)
    cost = 0
    j = 1
    n = len(a)
    for i in range(n):
        cost += a[i] * j
        j += 1
    return cost



