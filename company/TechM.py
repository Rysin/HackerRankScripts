# print(map(lambda x: x + 5, [1, 2, 3]))
# print(reversed([1, 2, 3, 4]))
# print([4, 7, 2, 9].sort())


def sum_it_up(numbers):
    result = 0
    for num in numbers:
        if isinstance(num, list):
            result += sum_it_up(num)
        else:
            result += num

    return result


def bubble_sort(arr):
    for iteration in range(len(arr)):
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        print(iteration)
    return arr


def bubble_sort_recursion(arr):
    swapped = False
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            swapped = True
            bubble_sort_recursion(arr)
    return arr


if __name__ == '__main__':
    # Sum of Nested Lists
    # numba = [2, 5, [2, 1, 23], [2, 3, 4, [7, 3], 78]]
    # f = sum_it_up(numba)
    # print(f)

    # Bubble Sort
    bubble = [7, 3, 5, 1, 65, 4, 1, 2, 0, 22, 17]
    # s = bubble_sort(bubble)
    s = bubble_sort_recursion(bubble)
    print(s)
