def prefix_sum(a: list) -> list:
    """ Returns the cumulative sum of new array each index contains sum of all left side values"""
    ps = list()
    n = len(a)
    for i in range(n):
        ps.append(a[i]) if i == 0 else ps.append(ps[i - 1] + a[i])

    return ps


def range_sum(a: list, b: list[list]) -> list:
    """ Returns sum of list in the given range """
    result = []
    for i in b:
        s, e = i
        ps = prefix_sum(a)
        if s == 0:
            psum = ps[e]
        else:
            psum = ps[e] - ps[s - 1]
        result.append(psum)
    return result


# print(range_sum([1, 2, 3, 4, 5], [[0, 3], [1, 2]]))
