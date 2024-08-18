# https://projecteuler.net/problem=16
from time import time


def power_digit_sum(n: int):
    return sum([int(i) for i in str(2 ** n)])


print(power_digit_sum(1000))
