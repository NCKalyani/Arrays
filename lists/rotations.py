from reverse import reverse_list


def rotate(li: list, k: int) -> list:
    """takes list as an input argument and rotates k elements in clockwise direction"""
    # Handling testcase k greater than length of list
    k = k % len(li)
    lis = reverse_list(li)
    lis1 = reverse_list(lis[0:k]) + reverse_list(lis[k:len(li)])
    return lis1


print(rotate([1, 2, 3, 4, 5, 6], 1))
