import math


def isPrime(number):
    is_prime = True
    prime_list = {2}

    # for num in range(2, int(math.sqrt(number)+1)):
    for num in prime_list:
        rem = number % num
        print(f'{number} % {num} = {rem}')
        if rem == 0:
            is_prime = False
            break

        prime_list.add(num)

    print(f"{number} {prime_list}")
    return is_prime


if __name__ == '__main__':
    num_list = list(range(1, 101))
    primes = list(filter(isPrime, num_list))
    # primes_ = list(filter(lambda x: isPrime(x), num_list))
    # print(primes_)
