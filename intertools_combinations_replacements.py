from itertools import combinations_with_replacement

string, n = input().split(' ')
n = int(n)

result = [''.join(each) for each in list(combinations_with_replacement(string, n))]
result = sorted(result)

for each in result:
    print(each)
