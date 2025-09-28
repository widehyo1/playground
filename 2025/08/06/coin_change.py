from functools import reduce

def coin_change(amount: int, coins: list[int]) -> int:
    n = len(coins)
    if n == 0:
        return -1
    dp = [-1] * (amount + 1) # to use coin amount as index, define (amount + 1) size
    dp[0] = 0
    coins.sort()
    for coin in coins:
        if coin <= amount:
            dp[coin] = 1

    for idx in range(coins[0], amount + 1): # because coins are sorted
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
            dp[idx] = newval if newval else -1

    return dp[amount]

if __name__ == '__main__':
    amount = 264
    coins = [474,83,404,3]
    res = coin_change(amount, coins)
    print(res)
