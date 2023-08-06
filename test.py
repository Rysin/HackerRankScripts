test_list = [1, 'ff', 3, 'x', 5]
# test_tuple = tuple(test_list)
# print(test_list)
# print(test_tuple)
# test_tuple = (test_list[0], test_list[len(test_list) - 1], len(test_list))

input_list = [4, 5, 3, 1, 0]
input_list.sort()
print(input_list)

for i in range(len(input_list) + 1):
    print(i)
    diff = input_list[i + 1] - input_list[i]
    if diff != 1:
        print(f'missing number: {input_list[i]} to {input_list[i] + diff}')




