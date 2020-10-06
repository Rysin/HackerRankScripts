if __name__ == '__main__':
    arr = [2, 4, 5, 5, 5, 6, 6, 6]
    # get duplicates removed
    arr_ = set(arr)
    arr_ = list(arr_)
    # Find first maximum and remove it
    topper = max(arr_)
    arr_.remove(topper)

    # Get 2nd Max and show it
    second_topper = max(arr_)
    print(second_topper)