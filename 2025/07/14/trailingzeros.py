def trailing_zeros(n):
    if n == 0:
        return 0
    sieve = list(range(1, n + 1))
    res = 0
    while sieve:
        sieve = [item // 5 for item in sieve if item % 5 == 0]
        res += len(sieve)
    return res

# print(trailing_zeros(0))
# print(trailing_zeros(1))
print(trailing_zeros(5))
