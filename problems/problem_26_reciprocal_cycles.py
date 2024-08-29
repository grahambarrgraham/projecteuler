# https://projecteuler.net/problem=26
from decimal import *
from time import time

from problems.problem_3_largest_prime_factor import prime_factors
from problems.problem_7_find_nth_prime import is_prime


def find_repeated_pattern(s: str):
    for length in range(1, len(s) // 2):
        for index in range(len(s) // 2):
            pattern_ = s[index:index + length]
            found = 0
            for i in range(index + length, len(s) - length, length):
                if s[i:i + length] != pattern_:
                    found = 0
                    break
                else:
                    found += 1
            if found:
                return pattern_
            index += 1
        length += 1
    return None


def reciprocal_cycles(n: int):
    result = []
    getcontext().rounding = ROUND_DOWN
    starting_precision = 10
    for denominator_ in range(1, n):
        terminating = len(set(prime_factors(denominator_)).difference({2, 5})) == 0
        if terminating:
            continue
        # coarse rule for estimating the required precision, could be improved
        precision = denominator_ if is_prime(denominator_) else starting_precision
        for precision_iter in range(1, 5):
            getcontext().prec = precision * precision_iter
            dec = Decimal(1) / Decimal(denominator_)
            pattern = find_repeated_pattern(str(dec)[2:])
            if pattern is not None:
                result.append((denominator_, pattern, dec))
                break
    return sorted(result, key=lambda p: len(p[1]))


now = time()
cycles = reciprocal_cycles(1000)
# for den, pat, dec in cycles:
#     print(den, len(pat), pat, dec)
denominator, _, _ = cycles[-1]
print(denominator, f"{time() - now} seconds")
