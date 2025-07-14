def tribonacchi(n):
    if n == 0:
        return 
    if n == 1:
        return 1
    if n == 2:
        return 1
    sol = [0, 1, 1] + [-1]*34
    for i in range(3, n + 1):
        sol[i] = sol[i-1] + sol[i-2] + sol[i-3]
    return sol[n]

for i in range(10):
    print(tribonacchi(i))

print(tribonacchi(25))

