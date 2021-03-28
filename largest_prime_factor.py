
# Find largest prime factor of given number
'''
Algorithm
1. Take the Number in account, find sqrt
2. Create List Of the Prime number less than the sqrt number.
3. Iter the list in reverse and see if prime number is factor of that number
'''

import math

check_num = 4352
primes = [2]
def get_prime_list(limit):
    global current_num, primes, factors
    for num in range(2, limit):
        div_limit = int(math.sqrt(num)) + 2
        flag = False
        for div in range(2, div_limit):
            if num % div == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            primes.append(num)
    return primes
def get_max_prime_factor(number):
    primes = get_prime_list(number)
    prime_factors = [f for f in primes if number % f == 0]
    print(prime_factors)
    print(max(prime_factors))
    return None

if __name__ == '__main__':
        listwa = get_prime_list(limit=100)
        print(listwa)
        get_max_prime_factor(2598)
