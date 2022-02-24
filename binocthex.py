def print_formatted(number):
    for num in range(1, number+1):
        padding = number.bit_length()
        print(f'{num:{padding}d} {num:{padding}o} {num:{padding}X} {num:{padding}b}')


if __name__ == '__main__':
    n = 17
    print_formatted(n)
