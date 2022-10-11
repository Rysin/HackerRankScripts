from itertools import groupby

string = input()
string = sorted(string)

result = groupby(list(string))

for k, v in result:
    print(f'{k}, {v.__str__()}')
