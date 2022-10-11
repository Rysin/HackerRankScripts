from itertools import permutations

a, b = input().split(' ')
b = int(b)

permuts = list(permutations(a, b))
print(permuts)
permuts.sort(key=lambda x: x[0])

for permute in permuts:
    print(''.join(permute))
