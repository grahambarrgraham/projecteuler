# https://projecteuler.net/problem=86
import math
from itertools import permutations
from time import time

from problems.problem_75_singular_integer_right_trianges import pythagorean_primitive_triplets_gen


def build_cuboids(m: int):
    seen = set()
    cuboids = []
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            for z in range(1, m + 1):
                t = (x, y, z)
                if t not in seen:
                    rotations = set(permutations(t, 3))
                    seen.update(rotations)
                    cuboids.append(t)
    return cuboids


def shortest_path(x: int, y: int, z: int):
    solution_1 = (x + z) ** 2 + y ** 2
    solution_2 = x ** 2 + (y + z) ** 2
    solution_3 = (x + y) ** 2 + z ** 2
    return (x, y, z), math.sqrt(min(solution_1, solution_2, solution_3))


def cuboid_route(cuboids):
    cuboids_short_path = [shortest_path(*cuboid) for cuboid in cuboids]
    return [(cuboid, path_length) for cuboid, path_length in cuboids_short_path if path_length.is_integer()]


def pythagorean_pairs(limit: int) -> set[tuple]:
    def side_limit(a_, b_):
        return (a_ <= limit and b_ <= limit * 2) or (b_ <= limit and a_ <= limit * 2)

    primitives = set(pythagorean_primitive_triplets_gen(limit * 100))

    result_ = set()
    for a, b, c in primitives:
        k = 1
        while side_limit(ka := k * a, kb := k * b):
            result_.add((ka, kb))
            k += 1

    return result_


def find_cubes(pair, m, integer_side_pairs):
    a, b = pair
    cubes_ = set()
    if b <= m:
        for i in range(1, a):
            x, y, z = sorted([i, a - i, b])
            if x <= m and y <= m and z <= m:
                cubes_.add((x, y, z))
    if a <= m:
        for i in range(1, b):
            x, y, z = sorted([i, b - i, a])
            if x <= m and y <= m and z <= m:
                cubes_.add((x, y, z))

    return cubes_


def build_cuboids_v2(m):
    pairs = pythagorean_pairs(m)
    # print(sorted(pairs))
    result = set()
    for triplet in pairs:
        cubes = find_cubes(triplet, m, pairs)
        result.update(cubes)
    return result


now = time()
for lim in range(100, 101):
    v1 = cuboid_route(build_cuboids(lim))
    v2_cuboids = build_cuboids_v2(lim)
    v2 = cuboid_route(v2_cuboids)
    v3 = v2_cuboids

    print(len(v1))
    print(len(v2))
    print(len(v3))

# print(sorted(v1))
# print(sorted(v2))
# print(sorted(v1.difference(v2)))

    print(lim, len(v2), f"{round(time() - now, 2)} seconds")
# print(math.sqrt((105 ** 2) + (100 ** 2)))