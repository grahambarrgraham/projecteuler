# https://projecteuler.net/problem=33
from decimal import Decimal
from itertools import combinations
from time import time

from numpy import product


def matches_digit_cancelled_fraction(a, b) -> bool:
    s_a, s_b = str(a), str(b)
    if s_a[0] == s_b[0]:
        a1, b1 = s_a[1], s_b[1]
    elif s_a[0] == s_b[1]:
        a1, b1 = s_a[1], s_b[0]
    elif s_a[1] == s_b[0]:
        a1, b1 = s_a[0], s_b[1]
    elif s_a[1] == s_b[1]:
        a1, b1 = s_a[1], s_b[1]
    else:
        return False
    return Decimal(a) / Decimal(b) == Decimal(a1) / Decimal(b1)


def digit_cancelling_fractions():
    fractions = [(n, d) for n, d in combinations(range(10, 100), 2) if n % 10 != 0 and d % 10 != 0 and d > n]
    fractions = [(n, d) for n, d in fractions if matches_digit_cancelled_fraction(n, d)]
    fraction = product([a for a, b in fractions]), product([b for a, b in fractions])
    return fraction


now = time()
n, d = digit_cancelling_fractions()
# luckily n divides d exactly, so easy to derive the denominator in the lowest common terms
print(d / n, f"{round(time() - now, 2)} seconds")
