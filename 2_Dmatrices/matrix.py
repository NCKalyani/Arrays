def row_wise_ele(a: list[list]) -> int:
    """ Returns row wise elements total"""
    row_sum = 0
    for i in range(len(a)):
        total = 0
        for j in range(len(a[0])):
            total += a[i][j]
            print(a[i][j], end=' ')
        print('')
        row_sum += total
    return row_sum


def col_wise_ele(a: list[list]) -> str:
    """Returns col wise elements total"""
    col_sum = 0
    for i in range(len(a[0])):
        total = 0
        for j in range(len(a)):
            total += a[j][i]
            print(a[j][i], end=' ')
        col_sum += total
        print('-', total)
    return ' ' * 8 + str(col_sum)
