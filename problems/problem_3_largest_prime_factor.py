# https://projecteuler.net/problem=3

# uses factorisation tree
def prime_factors(n: int) -> list[int]:
    queue = [n]
    result = []
    while len(queue) > 0:
        v = queue.pop()
        for i in range(2, v + 1):
            if v % i == 0:
                if v == i:
                    result.append(v)
                else:
                    queue += [i, v // i]
                break
    return result


def largest_prime_factor(n):
    return max(prime_factors(n))


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
