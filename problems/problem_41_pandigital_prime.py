# https://projecteuler.net/problem=41
from itertools import permutations
from time import time

from problems.problem_38_pandigital_multiples import is_pandigital
from problems.problem_7_find_nth_prime import is_prime


def pandigital_primes(n):
    for perm in permutations(range(1, n + 1)):
        i = int(''.join([str(a) for a in perm]))
        if is_prime(i):
            yield i


now = time()
result = []
for i in range(5, 10):
    result.extend(pandigital_primes(i))
print(max(result), f"{round(time() - now, 2)} seconds")
