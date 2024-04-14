# Which number survives at last?
import math


def survives(n: int) -> int:
    """Return the person who survives at last 'josesphus problem'"""
    y = 2 ** (int(math.log(n, 2)))
    print(y)
    got_killed = n - y
    survived = 2 * got_killed + 1
    return survived

