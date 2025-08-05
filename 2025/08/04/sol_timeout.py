import sys
input = sys.stdin.readline

def longest_increasing_subsequence_size(numbers: list[int]) -> int:
    n = len(numbers)
    size = 0

    stack = []

    stack.append((0, tuple()))

    while stack:
        cur = stack.pop()
        idx, comb = cur

        if idx == n:
            size = max(size, len(comb))
            continue

        number = numbers[idx]
        stack.append((idx + 1, comb))
        if len(comb) == 0:
            comb = (number,)
            stack.append((idx + 1, comb))
        elif number > comb[-1]:
            comb = (*comb, number)
            stack.append((idx + 1, comb))

    return size

n = int(input())
numbers = list(map(int, input().split()))
res = longest_increasing_subsequence_size(numbers)
print(res)
