# Convert Given Number to binary form

def decimal_to_binary(decimal_number):
    binary_lst = []
    while decimal_number / 2 != 0:
        binary_lst.append(decimal_number%2)
        decimal_number = decimal_number // 2

    # binary_lst.append(decimal_number%2)

    binary_lst.reverse()
    print(binary_lst)
    return None

if __name__ == '__main__':
    decimal_to_binary(64)