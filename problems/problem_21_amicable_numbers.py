# https://projecteuler.net/problem=21
from itertools import combinations

from numpy import product

from problems.problem_3_largest_prime_factor import prime_factors


def proper_divisors(n: int):
    p = prime_factors(n)
    all_divisors = {1}
    for i in range(1, len(p)):
        divisors = [product(s) for s in set(combinations(p, i))]
        all_divisors.update(divisors)
    return all_divisors


def sum_amicable_numbers(n: int):
    divisors = {}
    for i in range(n):
        divisors[i] = sum(proper_divisors(i))

    amicable_numbers = set()
    for a, b in divisors.items():
        if a != b and b in divisors and divisors[b] == a:
            amicable_numbers.update([a, b])
    return sum(amicable_numbers)


if __name__ == "__main__":
    print(sum_amicable_numbers(10000))
