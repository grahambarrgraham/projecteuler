# https://projecteuler.net/problem=86
from time import time

from problems.problem_75_singular_integer_right_trianges import pythagorean_triplets


# produces all triples such that a <= b <= c, a <= side_length, b <= side_length
def pythagorean_triples_(side_limit: int) -> set[tuple]:
    return pythagorean_triplets(
        lambda a, b, c: a <= side_limit,
        lambda a, b, c: a <= side_limit // 2 and b <= side_limit)


def find_cubes(triple, m) -> set[tuple]:
    a, b, _ = triple
    result = set()

    # the shortest path is √(x² + y²) + √z² if x <= y <= z

    def generate_cubes(p, q):
        for i in range(1, m):
            x, y, z = [i, p - i, q]
            if x <= y <= z:
                result.add(tuple((x, y, z)))

    if b == m:
        generate_cubes(a, b)
    if a == m:
        generate_cubes(b, a)

    return result


def build_cuboids(m, triples) -> set[tuple]:
    return {cuboid for triple in triples for cuboid in find_cubes(triple, m)}


def cuboid_route(target_cuboids, limit_m=1900) -> int:
    # generate more triples than required, up to a limit correlated to m, the cube edge length
    # multiply limit_m by two as the flattened cube requires 2 sides of the cube to form one edge of the triple
    triples = pythagorean_triples_(limit_m * 2)
    num_cuboids, m = 0, 0
    while num_cuboids < target_cuboids:
        m += 1
        cuboids = build_cuboids(m, triples)
        num_cuboids += len(cuboids)
    return m


now = time()
print(cuboid_route(1000000), f"{round(time() - now, 2)} seconds")
