# https://projecteuler.net/problem=47
from functools import cache
from time import time

from problems.problem_3_largest_prime_factor import prime_factors


def distinct_prime_factors(k, max_=1000000):
    for n in range(max_):
        if k_distinct_prime_in_a_row(n, k):
            return n
    return None


def k_distinct_prime_in_a_row(n, k):
    for j in range(k):
        if not has_k_distinct_prime_factors(n + j, k):
            return False
    return True


@cache
def has_k_distinct_prime_factors(n, k):
    return len(set(prime_factors(n))) == k


if __name__ == "__main__":
    now = time()
    result = distinct_prime_factors(4)
    print(result, f"{round(time() - now, 2)} seconds")
