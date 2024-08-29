# https://projecteuler.net/problem=2


def fibonacci():
    stack = [0, 1]
    yield 1
    while True:
        nxt = sum(stack)
        yield nxt
        stack = [stack[-1], nxt]


def fibonacci_n(n):
    f = fibonacci()
    a = next(f)
    while a < n:
        yield a
        a = next(f)


def sum_of_even_fibonacci(n):
    even_fibonacci = [f for f in fibonacci_n(n) if f % 2 == 0]
    return sum(even_fibonacci)


if __name__ == "__main__":
    print(sum_of_even_fibonacci(4000000))

