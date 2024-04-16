def triplets(a: list):
    """Returns the count of three elements of list that are in ascending order"""
    n = len(a)
    res = 0
    for i in range(1, n - 1):
        l, r = 0, 0
        j = i
        while j >= 0:
            if a[j] < a[i]:
                l += 1
            j -= 1
        for k in range(i + 1, n):
            if a[k] > a[i]:
                r += 1

        res += l * r
    return res


def trees_min_cost(a: list, b: list) -> int:
    """Returns the minimum total of three elements that are ascending order in the list"""
    if len(a) < 3:
        return -1
    if len(a) == 3 and a[0] < a[1] < a[2]:
        return b[0] + b[1] + b[2]
    ind = 1
    cost = sum(b)
    while ind < len(a):
        lft = []
        for i in range(ind):
            if a[i] < a[ind]:
                lft.append(b[i])
        if len(lft) == 0:
            ind += 1
            continue
        rht = []
        for j in range(ind + 1, len(a)):
            if a[j] > a[ind]:
                rht.append(b[j])
        if len(rht) == 0:
            ind += 1
            continue
        lc = min(lft)
        rc = min(rht)
        cost = min(cost, lc + rc + b[ind])
        ind += 1
    return cost
