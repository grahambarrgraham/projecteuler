# https://projecteuler.net/problem=5
from math import factorial


def evenly_divisible(lst: list[int], val) -> bool:
    return all(val % i == 0 for i in lst)


def smallest_multiple(n: int):
    result = factorial(n)
    r = list(reversed(range(1, n + 1)))
    for n in r:
        nxt = result // n
        if evenly_divisible(r, nxt):
            result = nxt
    return result


print(smallest_multiple(20))
