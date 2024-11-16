# https://projecteuler.net/problem=75
import math
from collections import defaultdict
from time import time


# a, b and c are co-prime, and a <= b <= c
def pythagorean_primitive_triplets_gen(limit_func):
    a, b, c, m = 0, 0, 0, 2

    # Euclid's formula

    while limit_func(a, b, c):
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if not limit_func(a, b, c):
                break

            if math.gcd(a, b, c) == 1:
                yield tuple(sorted([a, b, c]))

        m = m + 1


# Currently needs separate functions to limit primitives and non-primitives as the primitives limit function
# usually needs to be more permissive.  It's a leaky abstraction, but leverages Euclid's formula
def pythagorean_triplets(primitives_limit_func, k_limit_func) -> set[tuple]:

    primitives = set(pythagorean_primitive_triplets_gen(primitives_limit_func))

    # to derive all pythagorean triples from primitives, we can multiply a, b and c by k

    result_ = set()
    for a, b, c in primitives:
        k = 1
        while k_limit_func(ka := k * a, kb := k * b, kc := k * c):
            result_.add((ka, kb, kc))
            k += 1

    # a <= b <= c
    return result_


def pythagorean_triplets_(circumference_limit: int) -> set[tuple]:
    def wire_limit(a_, b_, c_):
        return a_ + b_ + c_ <= circumference_limit

    return pythagorean_triplets(lambda a, b, c: c <= circumference_limit, wire_limit)


def singular_integer_right_triangles(limit):
    triplets = pythagorean_triplets_(limit)
    circumference_to_solutions = defaultdict(int)
    for a, b, c in triplets:
        circumference_to_solutions[a + b + c] += 1
    return [k for k, v in circumference_to_solutions.items() if v == 1]


if __name__ == "__main__":
    now = time()
    result = len(singular_integer_right_triangles(1500000))
    print(result, f"{round(time() - now, 2)} seconds")