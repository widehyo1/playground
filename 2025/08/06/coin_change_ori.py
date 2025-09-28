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
        # print(dp, idx)
        # for idx in range(min(coins), value + 1): <- otherwise
        if dp[idx] == -1:
            temp = -1
            newval = None
            for coin in coins:
                if idx - coin > 0 and dp[idx - coin] > 0:
                    cur = dp[idx - coin] + 1
                    if newval is None:
                        newval = cur
                    else:
                        newval = min(cur, newval)
            dp[idx] = newval

    # print(dp)
    return dp[value]

if __name__ == '__main__':
    value = 11
    coins = [1,2,5]
    res = coin_change(value, coins)
    print(res)
