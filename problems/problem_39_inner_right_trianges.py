# https://projecteuler.net/problem=38
from time import time

one_to_nine = [a for a in '123456789']


def is_right_angled(a, b, c) -> int:
    return a ** 2 + b ** 2 == c ** 2


def inner_right_triangles(p):
    return [(a, b, p - a - b) for a in range(1, p) for b in range(a, p) if a < p - a - b and b < p - a - b and is_right_angled(a, b, p - a - b)]


def all_inner_right_triangles(n):
    return [inner_right_triangles(i) for i in range(1, n)]


now = time()
result = [(len(a), sum(a[0]), a) for a in all_inner_right_triangles(1000) if len(a) > 0]
print(max(result)[1], f"{round(time() - now, 2)} seconds")
