# timeout
import sys
input = sys.stdin.readline

def longest_increasing_subsequence_size(numbers):
    n = len(numbers)
    dp = [1] * n
    for cur in range(1, n):
        for prev in range(cur):
            if numbers[prev] < numbers[cur]:
                dp[cur] = max(dp[prev] + 1, dp[cur])
    return max(dp)

n = int(input())
numbers = [int(number) for number in input().split()]
res = longest_increasing_subsequence_size(numbers)
print(res)
