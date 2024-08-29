# https://projecteuler.net/problem=23
from time import time

from problems.problem_21_amicable_numbers import proper_divisors


def is_abundant(n):
    return 0 < n < sum(proper_divisors(n))


def abundant_numbers_to(n: int) -> list[int]:
    return [i for i in range(n) if is_abundant(i)]


def pairs(lst: list):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            yield lst[i], lst[j]


def non_abundant_sum(n):
    abundant_nums = abundant_numbers_to(n)
    abundant_pair_sums = {sum(c) for c in pairs(abundant_nums)}
    non_abundant_nums = [n for n in range(n) if n not in abundant_pair_sums]
    return sum(non_abundant_nums)


now = time()
print(non_abundant_sum(28123), f"{time() - now} seconds")


