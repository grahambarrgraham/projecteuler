# https://projecteuler.net/problem=29
from time import time


def digit_nth_powers(n: int, power: int):
    result = []
    for a in range(10, n):
        sum_ = sum([int(i) ** power for i in str(a)])
        if a == sum_:
            result.append(a)
    return result


now = time()
# not clear what the upper bounds is, but tried up to 10M
powers = digit_nth_powers(200000, 5)
print(sum(powers), f"{round(time() - now, 2)} seconds")
