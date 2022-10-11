def rightAngleTriangleLeft(n):
    pattern = [print('* ' * i) for i in range(n)]

def rightAngleTriangleRight(n):
    pattern = ['* ' * i for i in range(n)]
    pattern = pattern[::-1]
    for each in pattern:
        print(each)



if __name__ == '__main__':
    rightAngleTriangleLeft(8)
    rightAngleTriangleRight(8)
