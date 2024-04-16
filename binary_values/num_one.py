def num_one_bits(a: int) -> int:
    """checks the set bits and returns their count"""
    one_cnt = 0
    for i in range(32):
        if a & (1 << i):
            one_cnt += 1
    return one_cnt


def check_bit(n: int, i: int) -> bool:
    """check whether particular bit is set or unset"""
    if 1 << i & n:
        return True
    else:
        return False


def set_bit(n: int, i: int) -> int:
    """Sets particular bit """
    return n | (1 << i)


def unset_bit(n: int, i: int) -> int:
    """Unset particular nit"""
    return n & ~(1 << i)


def toggle_bit(n: int, i: int) -> int:
    """toggle the particular bit i.e if bit is set then it will unset and vice versa"""
    return n ^ (1 << i)


def toggle_all_bits(n: int) -> int:
    """ toggle all bits starting from right most set bit"""
    for i in range(32):
        if not check_bit(n, i):
            n = set_bit(n, i)
        else:
            n = toggle_bit(n, i)
            break
    return n
