# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# Decorator Function
def floorIt(func):
    # Wrapper Function
    def wrapperFunction(*args, **kwargs):
        print('Going to Call Wrapper Function')
        result = int(func(*args, **kwargs))
        print('Completed Call to Wrapper Function')
        return result
    return wrapperFunction


# MainFunction
@floorIt
def multiplyIt(a, b):
    # a, b = list(map(float,(input("Please provide 2 args separated by SPACE").split())))
    c = a/b
    print(c)
    return c


if __name__ == '__main__':
    # calling the function.
    # factorial(10)
    k = multiplyIt(552.7, 66.8)
    print(k)
