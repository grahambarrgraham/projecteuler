# https://projecteuler.net/problem=24
from problems.problem_2_sum_of_even_fibonacci import fibonacci


def n_digit_fibonacci(n):
    f = fibonacci()
    count = 1
    while len(str(next(f))) < n:
        count += 1
    return count


print(n_digit_fibonacci(1000))
