

if __name__ == '__main__':
    # x = ('a', 'b', 'c')
    x = (1, 2, 3)
    y = (1, 2, 3)

    print(id(x))
    print(id(y))

    print(f'x : {x}')
    print(f'y : {y}')
    print(f'z : {y}')

    print(id(x))
    print(id(y))

    print(*x)