# https://projecteuler.net/problem=12
from itertools import combinations
from time import time

from numpy import product

from problems.problem_3_largest_prime_factor import prime_factors


# factors can be calculated more efficiently from prime factors, which themselves
# can be efficient derived from a factorisation tree.
# https://math.stackexchange.com/questions/2782625/how-to-get-all-the-factors-of-a-number-using-its-prime-factorization
def num_factors(n: int):
    p = prime_factors(n)
    result = 2
    for i in range(1, len(p)):
        result += len(set(combinations(p, i)))
    return result


def fast_factors(n: int):
    p = prime_factors(n)
    all_factors = {1, n}
    for i in range(1, len(p)):
        c = [product(s) for s in set(combinations(p, i))]
        all_factors.update(c)
    return all_factors


def triangle_numbers():
    triangle_number = 1
    yield triangle_number
    last_val = 1
    while True:
        last_val += 1
        triangle_number += last_val
        yield triangle_number


def highly_divisible_triangle_number(max_divisors):
    for triangle_number in triangle_numbers():
        if num_factors(triangle_number) > max_divisors:
            return triangle_number


# Properties of triangle numbers: https://en.wikipedia.org/wiki/Triangular_number,
# includes sum of subsequent triangular numbers is a square number, and fast test for
# triangle number 'So an integer x is triangular if and only if 8x + 1 is a square.'

now = time()
print(highly_divisible_triangle_number(500), f"{time() - now} seconds")