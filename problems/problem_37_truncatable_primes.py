# https://projecteuler.net/problem=37
from decimal import Decimal
from itertools import combinations
from time import time

from numpy import product

from problems.problem_7_find_nth_prime import is_prime


def truncations(n):
    result_ = []
    s = str(n)
    for i in range(1, len(s)):
        result_.append(int(s[i:]))
        result_.append(int(s[0: (-1) * i]))
    return result_


def truncatable_primes(n):
    result_ = set()
    for i in range(11, n):
        if i not in result_ and is_prime(i) and all(is_prime(b) for b in truncations(i)):
            result_.add(i)
    return result_


now = time()
result = truncatable_primes(1000000)
print(sorted(result))
print(sum(result), f"{round(time() - now, 2)} seconds")
