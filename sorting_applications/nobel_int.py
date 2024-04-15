def nobel_int(a: list) -> int:
    """Returns count of numbers that are same as their index value"""
    ans = 0
    a.sort()
    for i in range(len(a)):
        if a[i] == i:
            ans += 1
    return ans


def nobel_int_wth_duplicates(a: list) -> int:
    """Returns the count of numbers that are same as their index value ,Note: array contains duplicates"""
    ans = 0
    a.sort()
    if a[0] == 0:
        ans += 1
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            less = i
            if a[i] == less:
                ans += 1
    return ans


def nobel_int_gtr_wth_dup(a: list) -> int:
    """returns true when any number is same as the values greater than that"""
    a.sort()
    n = len(a) - 1
    for i in range(n):
        if a[i] == n - i and a[i] != a[i + 1]:
            return 1
    return 0





