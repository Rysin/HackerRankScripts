# num = int(input("Pass A Number"))

def sqaureIT(num):
    result = 0
    for i in range(num):
        result = num + result

    return result


if __name__ == '__main__':
    sq = sqaureIT(5)
    print(sq)
