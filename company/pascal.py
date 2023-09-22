# text = "Hibiscus Rosa sinesis is a red flower, favorite of Hindu Deity Lord Ganesh."
# text = "ddd jjj, i, ui tth."
# letters = list(text.strip())
# count = 0
# counts = {letter: count+1 for letter in letters}
#
#
# print(counts)

"""
                 1
               1   1
             1   2   1
           1   3   3   1
         1   4   6   4   1
       1   5  10   10  5   1
     1   6  15  20   15  6   1
   1   7  21  35   35  21  7   1
 1   8  28  56  70   56   28  8   1
"""


# def pascals_triangle(height=3):
#     triangle = [[1], [1, 1]]
#
#     for repeat in range(height-2):
#         result = []
#         step = triangle[-1]
#         for i in range(len(triangle[-1]) - 1):
#             result.append(step[i] + step[i + 1])
#         result.append(1)
#         result.insert(0, 1)
#         triangle.append(result)
#
#     return triangle
#
#
#
# tr = pascals_triangle(10)
# print(*tr, sep="\n")

def add_all_once(args):
    # return [args[i] + args[i+1] for i in range(len(args)-1) if args[i] == 1]
    print(args)
    _range = len(args)-1

    for i in range(_range):
        if args[i] == 1:
            args[i] += args[i+1]
            args.remove(args[i+1])
        _range = len(args) - 1

    return args


once_removed = add_all_once([1, 1, 2, 3, 4, 1, 5, 1, 1, 4, 1, 2])  # -> [2, 2, 3, 5, 6, 5, 3, 1]
print(once_removed)
