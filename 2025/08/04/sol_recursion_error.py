import sys
input = sys.stdin.readline

def longest_increasing_subsequence_size(numbers: list[int]) -> int:
    n = len(numbers)
    size = 0
    def backtrack(idx, comb):
        nonlocal numbers, size, n

        if len(comb) > 1:
            seen_max, cur = comb[-2], comb[-1]
            if cur <= seen_max:
                return

        if idx == n:
            size = max(size, len(comb))
            return

        number = numbers[idx]
        comb.append(number)
        backtrack(idx + 1, comb)
        comb.pop()
        backtrack(idx + 1, comb)

    backtrack(0, [])
    return size

n = int(input())
numbers = [int(num) for num in input().split()]
res = longest_increasing_subsequence_size(numbers)
print(res)
