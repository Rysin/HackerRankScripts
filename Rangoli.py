import string


# n = number of unique characters to be used

# Horizontal
# 3  : 4  :: 4-1-4
# 5  : 8  :: 8-1-8
# 10 : 18 :: 18-1-18
# one horizontal symmetry side = 2*(n-1)
# Width = 4*(n-1) + 1

# Vertical
# 3   : 2 :: 2-1-2
# 5   : 4 :: 4-1-4
# 10  : 9 :: 9-1-9
# one vertical symmetry side = n-1
# Height = 2(n-1) + 1

# Conclusion
# Width = 2*Height


def print_rangoli(size):
    alphabets = list(string.ascii_lowercase)
    h_symm_side = 2 * (size - 1)
    _h_symm_side = h_symm_side
    v_symm_side = size - 1
    width = 2 * h_symm_side + 1
    height = 2 * v_symm_side + 1

    print(f'H-Symm_Side: {h_symm_side}')
    print(f'v_symm_side: {v_symm_side}')
    print(f'width: {width}')
    print(f'height:{height}')

    # Calculate Upper Left Part
    sides = []
    for _ in range(v_symm_side):
        side = '-' * _h_symm_side
        _h_symm_side -= 2
        sides.append(side)
        print(sides)

    # Calculate Middle Part of row
    chars = []
    _char = ''
    for i in range(v_symm_side):
        chars.append(_char + '-' + (alphabets[v_symm_side - i]))
        print(chars)



if __name__ == '__main__':
    # n = int(input())
    print_rangoli(5)
