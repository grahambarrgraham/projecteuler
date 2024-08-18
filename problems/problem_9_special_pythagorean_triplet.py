# https://projecteuler.net/problem=9


def special_pythagorean_triplet(n):
    for i in range(1, 1000):
        for j in range(i + 1, 1000):
            for k in range(j + 1, 1000):
                if i + j + k == 1000 and i * i + j * j == k * k:
                    return i * j * k


print(special_pythagorean_triplet(1000))
