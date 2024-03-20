def prefix_sum(a: list) -> list:
    """ Returns the cumulative sum of new array each index contains sum of all left side values"""
    ps = list()
    n = len(a)
    for i in range(n):
        ps.append(a[i]) if i == 0 else ps.append(ps[i - 1] + a[i])

    return ps
