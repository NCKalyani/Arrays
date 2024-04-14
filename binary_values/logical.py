import numpy


def monkeys_doors(n: int) -> int:
    """Returns doors remained opened after all operations"""
    remain_opened = 0
    for i in range(int(n ** 0.5)):
        if i * i <= n:
            remain_opened += 1
    return remain_opened


def majority_number(a: list) -> int:
    """Returns the number which appeared  more than 50 percentage"""
    n = len(a)
    count = n // 2 + 1
    ele = a[0]
    cnt = 1
    for i in range(n):
        if a[i] == ele:
            cnt += 1
        elif a[i] != ele:
            if cnt > 0:
                cnt -= 1
            else:
                ele = a[i]
                cnt = 1
    print(ele)
    maj = 0
    for num in a:
        if num == ele:
            maj += 1
    print(maj)
    if maj >= count:
        return ele
    else:
        return -1


def one_third_appeared_num(a: list) -> int:
    """Returns the number which appeared more than one third"""
    n = len(a)
    if n == 1:
        return a[0]
    cnt = n // 3
    ele1, c1 = a[0], 1
    ele2, c2 = 0, 0
    for num in a[1:]:
        if num == ele1:
            c1 += 1
        elif c1 == 0:
            ele1, c1 = num, 1
        elif num == ele2:
            c2 += 1
        elif c2 == 0:
            ele2, c2 = num, 1
        else:
            c1 -= 1
            c2 -= 1
    ec1, ec2 = 0, 0
    for n in a:
        if n == ele1:
            ec1 += 1
        elif n == ele2:
            ec2 += 1
    if ec1 >= cnt:
        return ele1
    elif ec2 >= cnt:
        return ele2
    else:
        return -1
