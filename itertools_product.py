from itertools import product

a = list(map(int, list(input().split(' '))))
b = list(map(int, list(input().split(' '))))

c = product(a, b)

for each in c:
    print(str(each) + str(' '), end='')
