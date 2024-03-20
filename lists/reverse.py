def reverse_list(li: list) -> list:
    """Takes list as an argument and gives reverse of list as output"""
    # initialise i,j
    i = 0
    j = len(li) - 1
    # loop runs until mid_length 
    while i < j:
        # swap list
        temp = li[i]
        li[i] = li[j]
        li[j] = temp
        # modify variables to avoid infinite loop
        i += 1
        j -= 1

    return li
