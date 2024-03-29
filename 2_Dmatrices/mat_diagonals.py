def diagonals_sq_mat(a: list[list]) -> int:
    """Returns long diagonals from both sides """
    count = i = j = 0
    while i < len(a):
        print(a[i][j], end=' ')
        i = j = i + 1
    count += 1
    print('\n')
    # right diagonal
    i = 0
    j = len(a) - 1
    while i < len(a) and j >= 0:
        print(a[i][j], end=' ')
        i += 1
        j -= 1
    count += 1
    return count


def all_diagonals_mat(a: list[list]) -> int:
    """Returns total number of diagonals i.e rows+columns-1"""
    count = 0
    for i in range(len(a[0])):
        count += 1
        k = 0
        j = i
        while k < len(a) and j >= 0:
            print(a[k][j], end=' ')
            k += 1
            j -= 1
        print('')
    for i in range(1, len(a)):
        count += 1
        k = i
        j = len(a[0]) - 1
        while k < len(a) and j >= 0:
            print(a[k][j], end=' ')
            k += 1
            j -= 1
        print('')
    return count


