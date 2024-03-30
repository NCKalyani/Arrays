def transpose_mat(a: list[list]) -> list[list]:
    """Returns Transpose of a given matrix"""
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


def rotate_90_dg(a: list[list]) -> list:
    """Returns the given matrix in a 90-degree rotation clockwise """
    a = transpose_mat(a)
    a = rotate_row_wise(a)
    return a


def rotate_row_wise(a: list[list]) -> list:
    """Returns the given matrix by shifting elements row wise"""
    n = len(a) // 2
    for i in range(len(a)):
        cnt = len(a) - 1
        for j in range(n):
            a[i][j], a[i][cnt] = a[i][cnt], a[i][j]
            cnt -= 1
    return a


def rotate_col_wise(a: list[list]) -> list:
    """Returns the given matrix by shifting elements col wise"""
    n = len(a) // 2
    cnt = len(a) - 1
    for i in range(n):
        for j in range(len(a)):
            a[i][j], a[cnt][j] = a[cnt][j], a[i][j]
        cnt -= 1
    return a


def rotate_180_dg(a: list[list]) -> list:
    """Returns 180 degree rotated list"""
    a = rotate_row_wise(a)
    a = rotate_col_wise(a)
    return a


