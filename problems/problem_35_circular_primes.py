# https://projecteuler.net/problem=35
from decimal import Decimal
from itertools import combinations
from time import time

from numpy import product

from problems.problem_7_find_nth_prime import is_prime


def rotations(n):
    result_ = []
    s = str(n)
    for i in range(len(s)):
        s = s[-1] + s[0:-1]
        result_.append(int(s))
    return result_


def circular_primes(n):
    result_ = set()
    for i in range(n):
        if i not in result_ and is_prime(i) and all(is_prime(b) for b in rotations(i)):
            result_.add(i)
    return result_


now = time()
result = circular_primes(1000000)
# result = circular_primes(100)
# print(sorted(result))
print(len(result), f"{round(time() - now, 2)} seconds")
