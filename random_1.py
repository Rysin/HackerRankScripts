from datetime import time, datetime
import random

randInts = []

def get3rands():
    global randInts
    while len(randInts) < 3:
        rand_int = random.randint(1, 100)
        if rand_int not in randInts:
            randInts.append(rand_int)

    return randInts


if __name__ == '__main__':
    lst = get3rands()
    print(lst)
