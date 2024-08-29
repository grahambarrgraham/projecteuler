# https://projecteuler.net/problem=31
from cgitb import reset
from time import time

coins = [200, 100, 50, 20, 10, 5, 2, 1]


def coin_sums(n: int, current: tuple = (), coin_index=0):
    result = []
    sum_current = sum(current)
    coin = coins[coin_index]
    for i in range(sum_current, n + 1, coin):
        option = current + (i - sum_current,)
        if i == n:
            result.append(option)
        elif coin_index < len(coins) - 1:
            options = coin_sums(n, option, coin_index + 1)
            result += options
    return result


now = time()
result = coin_sums(200)
# for r in result:
#     print(r)
print(len(result), f"{round(time() - now, 2)} seconds")
