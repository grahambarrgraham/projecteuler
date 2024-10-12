# https://projecteuler.net/problem=45
from time import time

from problems.problem_12_higest_divisable_triangle_number import triangle_number_gen
from problems.problem_44_pentagon_numbers import generate_n, pentagon_numbers_gen


def hexagon_numbers_gen():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1


def triangular_pentagonal_hexagonal():
    triangle_nums = generate_n(triangle_number_gen(), 100000)
    pentagon_nums = set(generate_n(pentagon_numbers_gen(), 100000))
    hexagon_nums = set(generate_n(hexagon_numbers_gen(), 100000))
    for i in range(285, 100000):
        if triangle_nums[i] in pentagon_nums and triangle_nums[i] in hexagon_nums:
            return triangle_nums[i]


if __name__ == "__main__":
    now = time()
    triangle_num = triangular_pentagonal_hexagonal()
    print(triangle_num, f"{round(time() - now, 2)} seconds")
