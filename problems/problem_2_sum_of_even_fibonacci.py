# https://projecteuler.net/problem=2


def fibonacci(max_: int) -> list[int]:
    stack = [0, 1]
    while True:
        nxt = sum(stack)
        if nxt <= max_:
            yield nxt
            stack = [stack[-1], nxt]
        else:
            break


def sum_of_even_fibonacci(n):
    even_fibonacci = [f for f in fibonacci(n) if f % 2 == 0]
    return sum(even_fibonacci)


print(sum_of_even_fibonacci(4000000))
