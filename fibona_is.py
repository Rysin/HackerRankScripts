# PROGRAME TO CHECK WHETHER GIVEN NO IS FIBONA OR NOT
sum = 0
num = 1
check_num = 610
fib_list = []

while sum <= check_num:
    sum = sum+num
    num = sum-num
    print(sum)
    fib_list.append(sum)

if check_num in fib_list:
    print(f'{check_num} is fibona')
else:
    print(f'{check_num} is fibona\nclosest fibona number is {fib_list[-1]}')

print(fib_list)







