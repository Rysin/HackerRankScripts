# string = "abcdefg"
#
# _string = list(string)
#
# reversed_string = _string[::-1]
# # reversed_string = str(reversed_string)
# # print(reversed_string)
# print(' '.join(str(letter) for letter in reversed_string))
# # for i in range(len(string)-1, 0, -1):
# #     print(string[i], sep=" ")


# Replace First Max with First Min and Second Max with Second Min and so on.
# [7, 22, 59, 41] -> [59, 41, 7, 22]
# [7, 22, 59, 41, 33, 45, 4, 8] ->
# [45, 33, 4, 8, 22, 7, 59, 41]

list_origin = [7, 22, 59, 41, 33, 45, 4, 8]
list_copy = list_origin.copy()

while list_copy:
    maxIndex = list_origin.index(max(list_copy))
    minIndex = list_origin.index(min(list_copy))

    _max = max(list_copy)
    _min = min(list_copy)

    list_origin[maxIndex], list_origin[minIndex] = _min, _max

    # remove the max, min
    list_copy.remove(_min)
    list_copy.remove(_max)

    print(f'list1 : {list_origin}')
    print(f'list_copy : {list_copy}')





