def magic_number(a: int) -> int :
    """Returns a number i.e either power of 5 or sum of 5 powers"""
    val = 1
    base = 5
    total = 0
    if a == 1:
        return 5
    if a == 2:
        return 25
    for i in range(32):
        mask = 1 << i
        if mask & a:
            total += pow(base, val)
            print(total)
        val += 1
        if val == a:
            return total
