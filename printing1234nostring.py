def num2string_1(n):
    return ''.join([str(n) for n in range(1, n + 1)])


def num2string_2(n):
    return sum((n - index) * 10 ** index for index in range(n))


if __name__ == '__main__':
    # n = int(input())
    result = num2string_2(11)
    print(result)
