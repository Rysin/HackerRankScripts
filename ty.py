# Given a list of integers you need to arrange the numbers in descending order of the first digit of number and also the descending order of those number.
# sample input:
# [10, 8, 90, 34, 5, 20, 11, 45, 1, 0]
#
# sample output:
# [90, 8, 5, 45, 34, 20, 11, 10, 1, 0]

list_1 = [10, 8, 90, 34, 5, 20, 11, 45, 1, 0]
# list_2 = [num*10 for num in list_1 if not num//10]
# list_2 =[]
# for num in list_1:
#     if not num//10:
#         list_2.append(num*10)
#     else:
#         list_2.append(num)
# print(list_2)
# list_2.sort(reverse=True, key=lambda x: x // 10)
# print(list_1)

list_2 = [str(num) for num in list_1]
list_3 = ['0' + str(num) for num in list_2 if not int(num) // 10]

print(list_3)
