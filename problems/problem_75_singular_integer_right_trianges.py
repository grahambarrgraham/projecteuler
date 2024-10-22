# https://projecteuler.net/problem=75
import math
from collections import defaultdict
from time import time


def pythagorean_primitive_triplets_gen(hypotenuse_limit):
    a, b, c, m = 0, 0, 0, 2

    while c <= hypotenuse_limit:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            if c > hypotenuse_limit:
                break

            if math.gcd(a, b, c) == 1:
                yield tuple(sorted([a, b, c]))

        m = m + 1


def pythagorean_triplets(circumference_limit: int) -> set[tuple]:

    def wire_limit(a_, b_, c_):
        return a_ + b_ + c_ <= circumference_limit

    primitives = set(pythagorean_primitive_triplets_gen(circumference_limit))

    result_ = set()
    for a, b, c in primitives:
        k = 1
        while wire_limit(ka := k * a, kb := k * b, kc := k * c):
            result_.add((ka, kb, kc))
            k += 1

    return result_


def singular_integer_right_triangles(limit):
    triplets = pythagorean_triplets(limit)
    circumference_to_solutions = defaultdict(int)
    for a, b, c in triplets:
        circumference_to_solutions[a + b + c] += 1
    return [k for k, v in circumference_to_solutions.items() if v == 1]


if __name__ == "__main__":
    now = time()
    result = len(singular_integer_right_triangles(1500000))
    print(result, f"{round(time() - now, 2)} seconds")