import re

if __name__ == '__main__':
    # N = int(input())
    # code_string = ''
    # for _ in range(N):
    #     code_string += '\n' + str(input())
    code_string = 'c $&1|| or && && &|&&| & | | &&c'
    string = '''11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.'''

    pattern_1 = ' \&\& '
    pattern_2 = ' \|\| '

    and_string = re.sub(pattern_1, ' and ', code_string)
    or_string = re.sub(pattern_2, ' or ', and_string)

    counter = 0
    while re.search(pattern_1, or_string) is not None or re.search(pattern_2, or_string) is not None:
        or_string = re.sub(pattern_1, ' and ', or_string)
        or_string = re.sub(pattern_2, ' or ', or_string)
        counter += 1

    print(or_string)
