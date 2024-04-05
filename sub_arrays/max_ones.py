def max_ones(a: list) -> int:
    """ Returns length of maximum sub array containing all 1's by replacing any 0 in the array"""
    l = r = ans = max_ans = 0
    flag = False
    for i in range(len(a)):
        if a[i] == 0:
            flag = True
            if l == 0:
                j = i - 1
                while j >= 0:
                    if a[j] == 1:
                        l += 1
                    else:
                        break
                    j -= 1
            for k in range(i + 1, len(a)):
                if a[k] == 1:
                    r += 1
                else:
                    break
            ans = l + r + 1
            max_ans = max(max_ans, ans)
            if l > 0:
                l = r
            r = 0
    if not flag:
        return len(a)
    return max_ans


def max1_by_replace(a: list) -> int:
    """ Returns length of maximum sub array of 1's by replacing one of 0 with existing 1"""
    n = len(a)
    l = r = ans = max_ans = 0
    flag = False
    for i in range(n):
        if a[i] == 0:
            flag = True
            if l == 0:
                j = i - 1
                while j >= 0:
                    if a[j] == 1:
                        l += 1
                    else:
                        break
                    j -= 1
            for k in range(i + 1, n):
                if a[k] == 1:
                    r += 1
                else:
                    break
        if l + r < a.count(1):
            ans = l + r + 1
        elif l + r == a.count(1):
            ans = l + r
        max_ans = max(ans, max_ans)
        l, r = r, 0
    if not flag:
        return n
    return max_ans
