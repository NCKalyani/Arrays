# spiral matrix
li = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]  # square matrix
b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
c = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def spiral_mat(a: list[list]) -> None:
    """Prints the matrix elements in spiral order"""
    n = len(a) - 1
    i = j = 0
    while n > 0:
        for k in range(n):
            print(a[i][j], end=' ')
            j += 1
        print()
        for k in range(n):
            print(a[i][j], end=' ')
            i += 1
        print()
        for k in range(n):
            print(a[i][j], end=' ')
            j -= 1
        print()
        for k in range(n):
            print(a[i][j], end=' ')
            i -= 1
        print()
        i += 1
        j += 1
        n = n - 2
    if n == 0:
        print(a[i][j])


spiral_mat(li)