# a = 10
# b = a
# print(f'ID A: {id(a)}')
# print(f'ID B: {id(b)}')
# print(a)
# print(b)
# a = 20
# print(b)
# print(f'ID A: {id(a)}')
# print(f'ID B: {id(b)}')
# print(a)
# print(b)

# string = 'abcdefgh'
# # string2 = 'def'
# # string2 = 'fed'
# string2 = 'abcd'
#
# for i in range(len(string)):
#     if string[i:i+3] == string2:
#         print(string[i:i + 3])
#         print('success')
#     else:
#         # print(string[i:i + 3])
#         continue


intList = list(range(10, 20))
print(intList)

newList = [i**2 for i in intList]
print(newList)

intList2 = list(map(lambda x: x**2 if not x % 2 else ..., intList))
# intList3 = list(filter(lambda x:x%2==1, intList))
print(intList2)
