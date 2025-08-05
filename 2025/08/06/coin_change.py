from functools import reduce

def coin_change(value: int, coins: list[int]) -> int:
    # assume coins are uniq and distinct
    # otherwise, comment out following

    # coins.sort()
    # seen = set()
    # uniq_coins = []
    # for coin in coins:
    #     assert coin > 0
    #     if coin not in seen:
    #         uniq_coins.append(coin)
    #         seen.add(coin)

    # init phase
    n = len(coins)
    if n == 0:
        # can not make value
        return -1
    dp = [-1] * (value + 1) # to use coin value as index, define (value + 1) size
    for coin in coins:
        dp[coin] = 1

    # biz logic
    for idx in range(coins[0], value + 1): # because coins are sorted
        # for idx in range(min(coins), value + 1): <- otherwise
        if dp[idx] == -1:
            idx_value = -1
            gen = (coin for coin in coins if idx - coin > 0 and dp[idx - coin] > 0)
            dp[idx] = min(dp[idx - coin] + 1 for coin in gen)

    print(dp)
    return dp[value]

if __name__ == '__main__':
    value = 11
    coins = [2,3,5]
    res = coin_change(value, coins)
    print(res)
