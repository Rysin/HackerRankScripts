from itertools import combinations

string, n = input().split()
n = int(n) + 1
string = sorted(string)

for i in range(1, n):
    [print("".join(each))for each in combinations(string, int(i))]


