import random


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def checksum(list):
    control_sum = 0
    for i in range(len(list)):
        control_sum += list[i]
        control_sum = (control_sum * 113) % 10000007
    return control_sum


def pipeline():
    primes_list = primes(1000)
    random.seed(100)
    random.shuffle(primes_list)
    result = checksum(primes_list)
    return result
