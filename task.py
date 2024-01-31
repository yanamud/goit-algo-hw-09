
import timeit
import random

coins = [50, 25, 10, 5, 2, 1]
def find_coins_greedy(coins, change):
    count_coins = {}
    for coin in coins:
        count = change // coin
        if count > 0:
            count_coins[coin] = count
        change = change - coin * count
    return count_coins

change = 113
print(f"Оптимальний спосіб видачі решти {change} покупцеві за допомогою жадібного алгоритму:\n{find_coins_greedy(coins, change)}")


def find_min_coins(coins, change):
    # Тут індекс це сума
    min_item = [0] + [float("inf")] * change  # мінімальна кілкість монет
    bigest_coin = [0] * (change + 1)  # остання монета для цієї суми

    for s in range(1, change + 1):
        for coin in coins:
            if s >= coin and min_item[s - coin] + 1 < min_item[s]:
                min_item[s] = min_item[s - coin] + 1
                bigest_coin[s] = coin

    count_coins = {}
    current_sum = change
    while current_sum > 0:
        coin = bigest_coin[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin

    return count_coins

change = 113
print(f"Оптимальний спосіб видачі решти {change} покупцеві за допомогою динамічного програмування:\n{find_min_coins(coins, change)}")

change_small = random.randint(0, 10)
change_medium = random.randint(10, 100)
change_big = random.randint(100, 1000)

time_small_greedy = timeit.timeit(lambda: find_coins_greedy(coins, change_small), number=10)
time_small_dynamic = timeit.timeit(lambda: find_min_coins(coins, change_small), number=10)

time_medium_greedy = timeit.timeit(lambda: find_coins_greedy(coins, change_medium), number=10)
time_smedium_dynamic = timeit.timeit(lambda: find_min_coins(coins, change_medium), number=10)

time_big_greedy = timeit.timeit(lambda: find_coins_greedy(coins, change_big), number=10)
time_big_dynamic = timeit.timeit(lambda: find_min_coins(coins, change_big), number=10)

print(f":{'-'*24} | :{'-'*19} | :{'-'*19} | :{'-'*19} |")
print(f"{'| Algorithm': <25} | {'Time small data': <20} | {'Time medium data': <20} | {'Time big data': <20} |")
print(f":{'-'*24} | :{'-'*19} | :{'-'*19} | :{'-'*19} |")
print(f"{'| Жадібний алгоритм': <25} | {time_small_greedy:<20.5f} | {time_medium_greedy:<20.5f} | {time_big_greedy:<20.5f} |")
print(f"{'| Динамічне програмування': <20} | {time_small_dynamic:<20.5f} | {time_smedium_dynamic:<20.5f} | {time_big_dynamic:<20.5f} |")
print(f":{'-'*24} | :{'-'*19} | :{'-'*19} | :{'-'*19} |")