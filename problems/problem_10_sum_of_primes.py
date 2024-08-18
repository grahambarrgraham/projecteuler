# https://projecteuler.net/problem=10
from time import time

from problems.problem_7_find_nth_prime import is_prime


def sum_of_primes_below(n):
    primes = []
    i = 2
    while True:
        if is_prime(i):
            if i > n:
                return sum(primes)
            primes.append(i)
        i += 1


now = time()
print(sum_of_primes_below(2000000), f"{time() - now} seconds")
