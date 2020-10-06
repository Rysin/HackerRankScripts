if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    i_ = list(range(0, x+1))
    j_ = list(range(0, y+1))
    k_ = list(range(0, z+1))


    inputs = [x, y, z]

    final_list = [[i, j, k] for i in i_ for j in j_ for k in k_ if i + j + k != n]
    print(final_list)
