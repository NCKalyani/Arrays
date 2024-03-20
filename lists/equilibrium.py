from prefixsum import prefix_sum


def equilibrium_ind(li: list) -> int:
    """Returns the index value of the list where sum of left side values equals to right sides values"""
    ps = prefix_sum(li)
    print(ps)
    for i in range(len(ps)):
        if i == (ps[-1] - ps[i]) == 0:
            print(i)
            return i
        elif ps[i - 1] == ps[-1] - ps[i]:
            return i
    return -1


print(equilibrium_ind([0]))
